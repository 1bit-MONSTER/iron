// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Fused int8 3x3 Conv + Bias + SiLU kernel using Padé tanh (AIE2+).
//
// Replaces the LUT-based sigmoid with a Padé rational approximation:
//   tanh(z) ≈ z*(27 + z²) / (27 + 9*z²)   for |z²| ≤ 20
//   tanh(z) = ±1                             for |z²| > 20
//
// SiLU(x) = x * sigmoid(x) = x * 0.5 * (1 + tanh(x/2))
//
// Pipeline (float-based activation):
//   1. int8 x int8 -> int32 convolution accumulation
//   2. Add pre-scaled int32 bias to accumulator
//   3. Convert to float: val = acc / 2^shift1
//   4. Compute SiLU via Padé tanh
//   5. Requantize: round(silu * 2^shift2), clamp to [-128, 127]
//
// Weight buffer layout (per FIFO element):
//   [int8 weights: oc * ic * 9 bytes | int32 bias: oc * 4 bytes]
//
// Data layouts:
//   Input rows:  [C_in/8, W, 8]
//   Weights:     [C_out/8, C_in/8, 3, 3, 8, 8]  (last two: [ic8, oc8])
//   Bias:        [C_out]  (int32, packed after weights)
//   Output row:  [C_out/8, W_out, 8]
//
// The `check` parameter controls vertical border handling:
//   0 (top):    line0 is padding (skipped)
//   1 (middle): all 3 lines are valid
//   2 (bottom): line2 is padding (skipped)

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
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
inline int8_t *select_line(int kh, int8_t *line0, int8_t *line1,
                           int8_t *line2) {
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
// Helper: Padé tanh SiLU activation (float in, int8 out).
//
// Computes: SiLU(x) = x * 0.5 * (1 + tanh(x/2))
// where tanh is approximated by the Padé [3/2] form:
//   tanh(z) ≈ z * (27 + z²) / (27 + 9*z²)
// ---------------------------------------------------------------------------
inline int8_t pade_silu_i8(int32_t acc, int32_t shift1, int32_t shift2) {
    float val = (float)acc / (float)(1 << shift1);
    float z = val * 0.5f;
    float z2 = z * z;
    float tanh_z;
    if (z2 > 20.0f) {
        tanh_z = (z > 0) ? 1.0f : -1.0f;
    } else {
        tanh_z = z * (27.0f + z2) / (27.0f + 9.0f * z2);
    }
    float silu_val = val * 0.5f * (1.0f + tanh_z);
    float scaled = silu_val * (float)(1 << shift2);
    int32_t out_i32 = (scaled >= 0) ? (int32_t)(scaled + 0.5f)
                                    : (int32_t)(scaled - 0.5f);
    if (out_i32 > 127)
        out_i32 = 127;
    if (out_i32 < -128)
        out_i32 = -128;
    return (int8_t)out_i32;
}

// ---------------------------------------------------------------------------
// Scalar stride-1: fused conv3x3 + bias + Padé SiLU with packed bias
// ---------------------------------------------------------------------------
void conv2dk3_i8_silu_scalar(int8_t *line0, int8_t *line1, int8_t *line2,
                             int8_t *weights_and_bias, int8_t *output,
                             const int32_t input_width,
                             const int32_t input_channels,
                             const int32_t output_channels,
                             const int32_t check, const int32_t shift1,
                             const int32_t shift2) {
    event0();

    // Derive bias pointer from packed buffer
    int8_t *weights = weights_and_bias;
    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels * 9);

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width; // stride 1, padding=1

    // Weight layout strides (in elements):
    //   [oc_g, ic_g, kh, kw, ic8, oc8]
    const int wt_stride_kw = 64;             // 8 * 8
    const int wt_stride_kh = 3 * 64;         // 3 * 8 * 8
    const int wt_stride_ic = 3 * 3 * 64;     // 3 * 3 * 8 * 8
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x = 0; x < output_width; x++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                int32_t acc = 0;

                // --- Phase 1: Convolution (int8 x int8 -> int32) ---
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = 0; kh < 3; kh++) {
                            if (kh == 0 && check == CHECK_TOP)
                                continue;
                            if (kh == 2 && check == CHECK_BOTTOM)
                                continue;

                            int8_t *line =
                                select_line(kh, line0, line1, line2);

                            for (int kw = 0; kw < 3; kw++) {
                                int input_x = x + kw - 1;
                                if (input_x < 0 || input_x >= input_width)
                                    continue;

                                int in_idx =
                                    ic_g * (input_width * 8) + input_x * 8 +
                                    ic8;
                                int wt_idx = oc_g * wt_stride_oc +
                                             ic_g * wt_stride_ic +
                                             kh * wt_stride_kh +
                                             kw * wt_stride_kw + ic8 * 8 +
                                             oc8;

                                acc += (int32_t)line[in_idx] *
                                       (int32_t)weights[wt_idx];
                            }
                        }
                    }
                }

                // --- Phase 2: Add pre-scaled bias ---
                acc += bias[oc_g * 8 + oc8];

                // --- Phase 3: Padé SiLU ---
                int8_t out_val = pade_silu_i8(acc, shift1, shift2);

                int out_idx = oc_g * (output_width * 8) + x * 8 + oc8;
                output[out_idx] = out_val;
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// Scalar stride-2: fused conv3x3 + bias + Padé SiLU with packed bias
// ---------------------------------------------------------------------------
void conv2dk3s2_i8_silu_scalar(int8_t *line0, int8_t *line1, int8_t *line2,
                               int8_t *weights_and_bias, int8_t *output,
                               const int32_t input_width,
                               const int32_t input_channels,
                               const int32_t output_channels,
                               const int32_t check, const int32_t shift1,
                               const int32_t shift2) {
    event0();

    int8_t *weights = weights_and_bias;
    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels * 9);

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width / 2; // stride 2

    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x_out = 0; x_out < output_width; x_out++) {
            int x_in_base = x_out * 2; // stride-2 base position

            for (int oc8 = 0; oc8 < 8; oc8++) {
                int32_t acc = 0;

                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = 0; kh < 3; kh++) {
                            if (kh == 0 && check == CHECK_TOP)
                                continue;
                            if (kh == 2 && check == CHECK_BOTTOM)
                                continue;

                            int8_t *line =
                                select_line(kh, line0, line1, line2);

                            for (int kw = 0; kw < 3; kw++) {
                                int input_x = x_in_base + kw - 1;
                                if (input_x < 0 || input_x >= input_width)
                                    continue;

                                int in_idx =
                                    ic_g * (input_width * 8) + input_x * 8 +
                                    ic8;
                                int wt_idx = oc_g * wt_stride_oc +
                                             ic_g * wt_stride_ic +
                                             kh * wt_stride_kh +
                                             kw * wt_stride_kw + ic8 * 8 +
                                             oc8;

                                acc += (int32_t)line[in_idx] *
                                       (int32_t)weights[wt_idx];
                            }
                        }
                    }
                }

                acc += bias[oc_g * 8 + oc8];

                int8_t out_val = pade_silu_i8(acc, shift1, shift2);

                int out_idx = oc_g * (output_width * 8) + x_out * 8 + oc8;
                output[out_idx] = out_val;
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// extern "C" wrappers
// ---------------------------------------------------------------------------
extern "C" {

void conv2dk3_i8_silu(int8_t *line0, int8_t *line1, int8_t *line2,
                      int8_t *weights_and_bias, int8_t *output,
                      const int32_t input_width, const int32_t input_channels,
                      const int32_t output_channels, const int32_t check,
                      const int32_t shift1, const int32_t shift2) {
    conv2dk3_i8_silu_scalar(line0, line1, line2, weights_and_bias, output,
                            input_width, input_channels, output_channels, check,
                            shift1, shift2);
}

void conv2dk3s2_i8_silu(int8_t *line0, int8_t *line1, int8_t *line2,
                        int8_t *weights_and_bias, int8_t *output,
                        const int32_t input_width, const int32_t input_channels,
                        const int32_t output_channels, const int32_t check,
                        const int32_t shift1, const int32_t shift2) {
    conv2dk3s2_i8_silu_scalar(line0, line1, line2, weights_and_bias, output,
                              input_width, input_channels, output_channels,
                              check, shift1, shift2);
}

} // extern "C"
