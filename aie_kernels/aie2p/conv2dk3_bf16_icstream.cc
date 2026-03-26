// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// IC-streaming 3x3 convolution kernel for bfloat16 (AIE2+).
//
// NOTE: This kernel is currently DISABLED.  IC streaming was found to produce
// incorrect results for configurations where height > 1 because the static
// _ic_accum buffer (sized for one output row) gets overwritten as the IC-outer
// pass processes successive rows.  By the time IC group 1 starts accumulating
// on top of IC group 0's results, _ic_accum contains only the LAST row's
// partial sums from IC group 0 — not row 0's.
//
// The design.py k3 path now disables IC streaming entirely.  This file is
// retained for reference and future correctness work.
//
// Data layouts (for reference):
//   Input rows:  [ic_chunk/8, W, 8]
//   Weights:     [oc_chunk/8, ic_chunk/8, 3, 3, 8, 8]
//   Output row:  [oc_chunk/8, W_out, 8]

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Border check values
constexpr int CHECK_TOP = 0;
constexpr int CHECK_MIDDLE = 1;
constexpr int CHECK_BOTTOM = 2;

// ---------------------------------------------------------------------------
// Helper: get the line pointer for a given kernel row (kh).
// ---------------------------------------------------------------------------
static inline bfloat16 *select_line(int kh, bfloat16 *line0, bfloat16 *line1,
                                     bfloat16 *line2) {
    switch (kh) {
    case 0:
        return line0;
    case 1:
        return line1;
    default:
        return line2;
    }
}

// ---------------------------------------------------------------------------
// IC-streaming accumulation buffer.
// Retained for reference; not used in the disabled IC streaming path.
// ---------------------------------------------------------------------------
static float __attribute__((aligned(64))) _ic_accum[3200];

// ---------------------------------------------------------------------------
// IC-streaming stride-1 bias+SiLU fused scalar implementation (BROKEN).
//
// Bug: _ic_accum is sized for one output row but the IC-outer pass processes
// all H rows for IC group 0, leaving only row H-1's partial sums in the
// buffer when IC group 1 starts processing row 0.
//
// Retained for reference only; IC streaming is currently disabled in design.py.
// ---------------------------------------------------------------------------
void conv2dk3_bf16_bias_silu_icstream_scalar(
    bfloat16 *line0, bfloat16 *line1, bfloat16 *line2, bfloat16 *weights,
    bfloat16 *output, const int32_t input_width, const int32_t input_channels,
    const int32_t output_channels, const int32_t check,
    const int32_t ic_group_idx, const int32_t n_ic_groups) {

    event0();

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width; // stride 1, padding=1

    // Bias is packed after this IC group's weights: offset = oc * ic_chunk * 9
    // Bias is only read on the last IC group.
    bfloat16 *bias = weights + output_channels * input_channels * 9;

    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    const bool is_first = (ic_group_idx == 0);
    const bool is_last = (ic_group_idx == n_ic_groups - 1);

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x = 0; x < output_width; x++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                float sum = 0.0f;

                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = 0; kh < 3; kh++) {
                            if (kh == 0 && check == CHECK_TOP)
                                continue;
                            if (kh == 2 && check == CHECK_BOTTOM)
                                continue;

                            bfloat16 *line = select_line(kh, line0, line1, line2);

                            for (int kw = 0; kw < 3; kw++) {
                                int input_x = x + kw - 1;
                                if (input_x < 0 || input_x >= input_width)
                                    continue;

                                int in_idx = ic_g * (input_width * 8) + input_x * 8 + ic8;
                                int wt_idx = oc_g * wt_stride_oc +
                                             ic_g * wt_stride_ic +
                                             kh * wt_stride_kh +
                                             kw * wt_stride_kw +
                                             ic8 * 8 + oc8;

                                sum += (float)line[in_idx] * (float)weights[wt_idx];
                            }
                        }
                    }
                }

                int acc_idx = oc_g * (output_width * 8) + x * 8 + oc8;
                if (is_first)
                    _ic_accum[acc_idx] = sum;
                else
                    _ic_accum[acc_idx] += sum;

                if (is_last) {
                    // Apply bias and SiLU and write to output FIFO
                    float val = _ic_accum[acc_idx] + (float)bias[oc_g * 8 + oc8];
                    float z = val * 0.5f;
                    float z2 = z * z;
                    float tanh_z = (z2 > 20.0f) ? (z > 0 ? 1.0f : -1.0f)
                                                 : z * (27.0f + z2) / (27.0f + 9.0f * z2);
                    float silu_val = val * 0.5f * (1.0f + tanh_z);
                    output[acc_idx] = (bfloat16)silu_val;
                }
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// extern "C" wrappers (BROKEN - retained for reference only).
// IC streaming is currently disabled in design.py.
// ---------------------------------------------------------------------------
extern "C" {

// Accumulate-only: called for ic_group_idx < n_ic_groups-1.
// No output pointer — kernel only writes to the static _ic_accum buffer.
void conv2dk3_bf16_accum_icstream(
    bfloat16 *line0, bfloat16 *line1, bfloat16 *line2, bfloat16 *weights,
    const int32_t input_width, const int32_t input_channels,
    const int32_t output_channels, const int32_t check,
    const int32_t ic_group_idx, const int32_t n_ic_groups) {
    conv2dk3_bf16_bias_silu_icstream_scalar(line0, line1, line2, weights,
                                            nullptr, input_width,
                                            input_channels, output_channels,
                                            check, ic_group_idx, n_ic_groups);
}

// Flush: called for ic_group_idx == n_ic_groups-1.
// Reads _ic_accum, adds bias, applies SiLU, writes to output FIFO buffer.
void conv2dk3_bf16_flush_icstream(
    bfloat16 *line0, bfloat16 *line1, bfloat16 *line2, bfloat16 *weights,
    bfloat16 *output, const int32_t input_width, const int32_t input_channels,
    const int32_t output_channels, const int32_t check,
    const int32_t ic_group_idx, const int32_t n_ic_groups) {
    conv2dk3_bf16_bias_silu_icstream_scalar(line0, line1, line2, weights, output,
                                            input_width, input_channels,
                                            output_channels, check,
                                            ic_group_idx, n_ic_groups);
}

} // extern "C"
