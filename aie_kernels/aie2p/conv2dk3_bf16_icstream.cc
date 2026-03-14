// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// IC-streaming 3x3 convolution kernel for bfloat16 (AIE2+).
//
// Used when in_channels is too large to fit the depth-4 sliding window
// FIFO alongside weights in L1 (64KB).  Input channels are split into
// ic_chunk-wide groups; this kernel is called n_ic_groups times per
// output row.  Partial products are accumulated in a static float32
// buffer.  On the final IC group, bias is added and SiLU is applied.
//
// Data layouts match conv2dk3_bf16.cc:
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
//
// Sized for max oc_chunk * out_w across IC-streaming configs:
//   40 * 80 = 3200 elements (from 80->80 k3s1 80x80 config).
//   3200 * 4 = 12800 bytes.
//
// This buffer lives in L1 static data and MUST be accounted for in the
// Python-side L1 budget calculations (IC_ACCUM_STATIC_BYTES = 12800).
// ---------------------------------------------------------------------------
static float __attribute__((aligned(64))) _ic_accum[3200];

// ---------------------------------------------------------------------------
// IC-streaming stride-1 bias+SiLU fused scalar implementation.
//
// Parameters:
//   input_channels   -- ic_chunk (channels in this group, multiple of 8)
//   output_channels  -- oc_chunk (output channels handled by this core)
//   ic_group_idx     -- index of this IC group (0 = initialize accum)
//   n_ic_groups      -- total number of IC groups (last = flush + SiLU)
//
// Accumulation: static float32 buffer.  Avoids extra DMA channel since
// the output FIFO is only written on the final IC group.
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
// extern "C" wrappers
//
// Two entry points with different signatures:
//   accum:  NO output pointer — used for non-last IC groups (accumulate only)
//   flush:  WITH output pointer — used for last IC group (bias + SiLU + write)
//
// This allows the MLIR-AIE core function to avoid acquiring the output FIFO
// for non-last IC groups, keeping the drain TAP simple (n_oc * height elements
// instead of n_oc * n_ic * height).
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
