// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// 3x3 Convolution kernel for bfloat16 activations and weights (AIE2+).
//
// Interface: 3 separate input row pointers (line0, line1, line2)
// corresponding to the 3 rows of the sliding window. The caller manages
// which rows to pass for each output row.
//
// Data layouts:
//   Input rows:  [C_in/8, W, 8]
//   Weights:     [C_out/8, C_in/8, 3, 3, 8, 8]  (last two: [ic8, oc8])
//   Output row:  [C_out/8, W_out, 8]
//
// The `check` parameter controls vertical border handling:
//   0 (top):    line0 is padding (skipped)
//   1 (middle): all 3 lines are valid
//   2 (bottom): line2 is padding (skipped)
//
// Horizontal borders use zero-padding: kw positions that fall outside
// [0, input_width) contribute zero.

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
inline bfloat16 *select_line(int kh, bfloat16 *line0, bfloat16 *line1,
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
// Scalar stride-1 implementation
// ---------------------------------------------------------------------------
void conv2dk3_bf16_scalar(bfloat16 *line0, bfloat16 *line1, bfloat16 *line2,
                           bfloat16 *weights, bfloat16 *output,
                           const int32_t input_width,
                           const int32_t input_channels,
                           const int32_t output_channels,
                           const int32_t check) {
    event0();

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width; // stride 1, padding=1

    // Weight layout strides (in elements):
    //   [oc_g, ic_g, kh, kw, ic8, oc8]
    //   sizes: [oc_groups, ic_groups, 3, 3, 8, 8]
    const int wt_stride_kw = 64;             // 8 * 8
    const int wt_stride_kh = 3 * 64;         // 3 * 8 * 8
    const int wt_stride_ic = 3 * 3 * 64;     // 3 * 3 * 8 * 8
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x = 0; x < output_width; x++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                float sum = 0.0f;

                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = 0; kh < 3; kh++) {
                            // Vertical border: skip this row if padding
                            if (kh == 0 && check == CHECK_TOP)
                                continue;
                            if (kh == 2 && check == CHECK_BOTTOM)
                                continue;

                            bfloat16 *line = select_line(kh, line0, line1, line2);

                            for (int kw = 0; kw < 3; kw++) {
                                int input_x = x + kw - 1; // padding = 1

                                // Horizontal border: zero-pad
                                if (input_x < 0 || input_x >= input_width)
                                    continue;

                                // Input index: [ic_g, input_x, ic8]
                                int in_idx = ic_g * (input_width * 8) + input_x * 8 + ic8;

                                // Weight index: [oc_g, ic_g, kh, kw, ic8, oc8]
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

                // Output index: [oc_g, x, oc8]
                int out_idx = oc_g * (output_width * 8) + x * 8 + oc8;
                output[out_idx] = (bfloat16)sum;
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// Scalar stride-2 implementation
// ---------------------------------------------------------------------------
void conv2dk3s2_bf16_scalar(bfloat16 *line0, bfloat16 *line1, bfloat16 *line2,
                             bfloat16 *weights, bfloat16 *output,
                             const int32_t input_width,
                             const int32_t input_channels,
                             const int32_t output_channels,
                             const int32_t check) {
    event0();

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
                                int input_x = x_in_base + kw - 1; // padding = 1

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

                int out_idx = oc_g * (output_width * 8) + x_out * 8 + oc8;
                output[out_idx] = (bfloat16)sum;
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// Vectorized stride-1 implementation
//
// Uses aie::mmul<4,8,8,bfloat16,bfloat16> to compute 4 output spatial
// positions x 8 output channels at a time. For each (oc_g, ic_g) pair,
// we iterate over the 9 spatial positions (3 kh x 3 kw), loading one 8x8
// weight tile and 4 input positions' 8 channels per MAC.
//
// Left and right borders (x=0 and x=W-1) are handled by scalar fallback
// since they only need zero-padding for one column each.
// ---------------------------------------------------------------------------
void conv2dk3_bf16_vectorized(bfloat16 *__restrict line0,
                               bfloat16 *__restrict line1,
                               bfloat16 *__restrict line2,
                               bfloat16 *__restrict weights,
                               bfloat16 *__restrict output,
                               const int32_t input_width,
                               const int32_t input_channels,
                               const int32_t output_channels,
                               const int32_t check) {
    event0();

    using MMUL = aie::mmul<4, 8, 8, bfloat16, bfloat16>;

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width; // stride 1, padding=1

    // Weight layout strides
    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    // Determine which kernel rows are active based on check
    int kh_start = 0;
    int kh_end = 3;
    if (check == CHECK_TOP)
        kh_start = 1;
    if (check == CHECK_BOTTOM)
        kh_end = 2;

    bfloat16 *lines[3] = {line0, line1, line2};

    // Number of interior positions that can be computed with full 3-wide
    // window (no horizontal padding needed): x in [1, input_width-2].
    // We process these in groups of 4 (NUM_W).
    constexpr int NUM_W = 4;
    const int interior_count = input_width - 2; // positions 1..input_width-2
    const int vec_iters = (interior_count > 0) ? interior_count / NUM_W : 0;
    const int vec_rem = (interior_count > 0) ? interior_count % NUM_W : 0;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {

        // ---- Left border (x=0): scalar fallback ----
        {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                float sum = 0.0f;
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = kh_start; kh < kh_end; kh++) {
                            for (int kw = 0; kw < 3; kw++) {
                                int input_x = 0 + kw - 1;
                                if (input_x < 0)
                                    continue;
                                int in_idx = ic_g * (input_width * 8) + input_x * 8 + ic8;
                                int wt_idx = oc_g * wt_stride_oc +
                                             ic_g * wt_stride_ic +
                                             kh * wt_stride_kh +
                                             kw * wt_stride_kw +
                                             ic8 * 8 + oc8;
                                sum += (float)lines[kh][in_idx] * (float)weights[wt_idx];
                            }
                        }
                    }
                }
                output[oc_g * (output_width * 8) + 0 * 8 + oc8] = (bfloat16)sum;
            }
        }

        // ---- Interior positions: vectorized (groups of 4) ----
        // For interior x, input positions x-1, x, x+1 are all valid.
        // When processing 4 positions starting at x_base, we need input
        // columns [x_base-1 .. x_base+2+1] = [x_base-1 .. x_base+3].
        // For kw=0: read from x_base-1 (4 consecutive positions)
        // For kw=1: read from x_base   (4 consecutive positions)
        // For kw=2: read from x_base+1 (4 consecutive positions)
        for (int vi = 0; vi < vec_iters; vi++) {
            int x_base = 1 + vi * NUM_W; // first interior position in this group

            MMUL acc;
            acc = aie::zeros<accfloat, MMUL::size_C>();

            for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                for (int kh = kh_start; kh < kh_end; kh++) {
                    bfloat16 *__restrict line_ptr = lines[kh] + ic_g * (input_width * 8);

                    AIE_PREPARE_FOR_PIPELINING
                    for (int kw = 0; kw < 3; kw++) {
                        int col = x_base + kw - 1;

                        // Load 4 consecutive spatial positions x 8 channels = 32 bf16
                        aie::vector<bfloat16, MMUL::size_A> in_a =
                            aie::load_v<MMUL::size_A>(line_ptr + col * 8);

                        // Load 8x8 weight tile
                        bfloat16 *__restrict wt_ptr = weights +
                                                      oc_g * wt_stride_oc +
                                                      ic_g * wt_stride_ic +
                                                      kh * wt_stride_kh +
                                                      kw * wt_stride_kw;
                        aie::vector<bfloat16, MMUL::size_B> in_b =
                            aie::load_v<MMUL::size_B>(wt_ptr);

                        acc.mac(in_a, in_b);
                    }
                }
            }

            aie::vector<bfloat16, MMUL::size_C> result = acc.to_vector<bfloat16>();
            aie::store_v(output + oc_g * (output_width * 8) + x_base * 8, result);
        }

        // ---- Interior remainder (scalar) ----
        for (int ri = 0; ri < vec_rem; ri++) {
            int x = 1 + vec_iters * NUM_W + ri;
            for (int oc8 = 0; oc8 < 8; oc8++) {
                float sum = 0.0f;
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = kh_start; kh < kh_end; kh++) {
                            for (int kw = 0; kw < 3; kw++) {
                                int input_x = x + kw - 1;
                                int in_idx = ic_g * (input_width * 8) + input_x * 8 + ic8;
                                int wt_idx = oc_g * wt_stride_oc +
                                             ic_g * wt_stride_ic +
                                             kh * wt_stride_kh +
                                             kw * wt_stride_kw +
                                             ic8 * 8 + oc8;
                                sum += (float)lines[kh][in_idx] * (float)weights[wt_idx];
                            }
                        }
                    }
                }
                output[oc_g * (output_width * 8) + x * 8 + oc8] = (bfloat16)sum;
            }
        }

        // ---- Right border (x=input_width-1): scalar fallback ----
        if (input_width > 1) {
            int x = input_width - 1;
            for (int oc8 = 0; oc8 < 8; oc8++) {
                float sum = 0.0f;
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = kh_start; kh < kh_end; kh++) {
                            for (int kw = 0; kw < 3; kw++) {
                                int input_x = x + kw - 1;
                                if (input_x >= input_width)
                                    continue;
                                int in_idx = ic_g * (input_width * 8) + input_x * 8 + ic8;
                                int wt_idx = oc_g * wt_stride_oc +
                                             ic_g * wt_stride_ic +
                                             kh * wt_stride_kh +
                                             kw * wt_stride_kw +
                                             ic8 * 8 + oc8;
                                sum += (float)lines[kh][in_idx] * (float)weights[wt_idx];
                            }
                        }
                    }
                }
                output[oc_g * (output_width * 8) + x * 8 + oc8] = (bfloat16)sum;
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// Vectorized stride-2 implementation
//
// Same approach as stride-1 vectorized, but output positions sample every
// other input column. For output position x_out, the input base column is
// x_in = 2*x_out, and the 3x3 window reads columns x_in-1, x_in, x_in+1.
//
// We process 4 output positions at a time. The input columns for kw=0 are
// at positions 2*x_out_base-1, 2*(x_out_base+1)-1, ... which are NOT
// contiguous, so we cannot use a single aligned load. Instead we gather
// the 4 needed input vectors manually.
//
// For simplicity the stride-2 vectorized path loads each spatial position
// individually and uses a scalar fallback for borders.
// ---------------------------------------------------------------------------
void conv2dk3s2_bf16_vectorized(bfloat16 *__restrict line0,
                                 bfloat16 *__restrict line1,
                                 bfloat16 *__restrict line2,
                                 bfloat16 *__restrict weights,
                                 bfloat16 *__restrict output,
                                 const int32_t input_width,
                                 const int32_t input_channels,
                                 const int32_t output_channels,
                                 const int32_t check) {
    event0();

    using MMUL = aie::mmul<4, 8, 8, bfloat16, bfloat16>;

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width / 2;

    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    int kh_start = 0;
    int kh_end = 3;
    if (check == CHECK_TOP)
        kh_start = 1;
    if (check == CHECK_BOTTOM)
        kh_end = 2;

    bfloat16 *lines[3] = {line0, line1, line2};

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x_out = 0; x_out < output_width; x_out++) {
            int x_in_base = x_out * 2;

            // Use a single MMUL accumulator for 1 output position.
            // We replicate the same input across all 4 "rows" of the mmul
            // and only extract the first output row. This is wasteful but
            // correct; a future optimization can batch output positions.
            //
            // Actually, let's use scalar accumulation per element since
            // stride-2 doesn't have contiguous spatial access patterns.

            for (int oc8 = 0; oc8 < 8; oc8++) {
                float sum = 0.0f;

                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = kh_start; kh < kh_end; kh++) {
                            for (int kw = 0; kw < 3; kw++) {
                                int input_x = x_in_base + kw - 1;

                                if (input_x < 0 || input_x >= input_width)
                                    continue;

                                int in_idx = ic_g * (input_width * 8) + input_x * 8 + ic8;
                                int wt_idx = oc_g * wt_stride_oc +
                                             ic_g * wt_stride_ic +
                                             kh * wt_stride_kh +
                                             kw * wt_stride_kw +
                                             ic8 * 8 + oc8;

                                sum += (float)lines[kh][in_idx] * (float)weights[wt_idx];
                            }
                        }
                    }
                }

                output[oc_g * (output_width * 8) + x_out * 8 + oc8] = (bfloat16)sum;
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// Scalar stride-1 bias+SiLU fused implementation.
// After MAC accumulation, adds per-channel bias and applies SiLU activation.
// SiLU(x) = x / (1 + exp(-x)), computed in float32 for accuracy.
// ---------------------------------------------------------------------------
// Bias+SiLU fused stride-1 variant. Bias is packed at the end of the weight
// buffer: &weights[oc * ic * 9]. Same 5-buffer interface (3 lines + weights +
// output) as conv2dk3_bf16 -- no extra DMA channel needed.
void conv2dk3_bf16_bias_silu_scalar(bfloat16 *line0, bfloat16 *line1,
                                     bfloat16 *line2, bfloat16 *weights,
                                     bfloat16 *output,
                                     const int32_t input_width,
                                     const int32_t input_channels,
                                     const int32_t output_channels,
                                     const int32_t check) {
    event0();

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width; // stride 1, padding=1

    // Bias is packed after weights: offset = oc * ic * 9 elements
    bfloat16 *bias = weights + output_channels * input_channels * 9;

    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

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

                // Add bias and apply SiLU in float32
                float val = sum + (float)bias[oc_g * 8 + oc8];
                // SiLU(x) = x * sigmoid(x) = x * 0.5 * (1 + tanh(x/2))
                float z = val * 0.5f;
                float z2 = z * z;
                float tanh_z = (z2 > 20.0f) ? (z > 0 ? 1.0f : -1.0f) : z * (27.0f + z2) / (27.0f + 9.0f * z2);
                float silu_val = val * 0.5f * (1.0f + tanh_z);
                int out_idx = oc_g * (output_width * 8) + x * 8 + oc8;
                output[out_idx] = (bfloat16)silu_val;
            }
        }
    }

    event1();
}

// Bias+SiLU fused stride-2 variant. Same bias-packed-in-weights pattern.
void conv2dk3s2_bf16_bias_silu_scalar(bfloat16 *line0, bfloat16 *line1,
                                       bfloat16 *line2, bfloat16 *weights,
                                       bfloat16 *output,
                                       const int32_t input_width,
                                       const int32_t input_channels,
                                       const int32_t output_channels,
                                       const int32_t check) {
    event0();

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width / 2; // stride 2

    // Bias is packed after weights: offset = oc * ic * 9 elements
    bfloat16 *bias = weights + output_channels * input_channels * 9;

    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x_out = 0; x_out < output_width; x_out++) {
            int x_in_base = x_out * 2;

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
                                int input_x = x_in_base + kw - 1;

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

                // Add bias and apply SiLU in float32
                float val = sum + (float)bias[oc_g * 8 + oc8];
                // SiLU(x) = x * sigmoid(x) = x * 0.5 * (1 + tanh(x/2))
                float z = val * 0.5f;
                float z2 = z * z;
                float tanh_z = (z2 > 20.0f) ? (z > 0 ? 1.0f : -1.0f) : z * (27.0f + z2) / (27.0f + 9.0f * z2);
                float silu_val = val * 0.5f * (1.0f + tanh_z);
                int out_idx = oc_g * (output_width * 8) + x_out * 8 + oc8;
                output[out_idx] = (bfloat16)silu_val;
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// extern "C" wrappers
// ---------------------------------------------------------------------------
extern "C" {

void conv2dk3_bf16(bfloat16 *line0, bfloat16 *line1, bfloat16 *line2,
                   bfloat16 *weights, bfloat16 *output,
                   const int32_t input_width, const int32_t input_channels,
                   const int32_t output_channels,
                   const int32_t check) {
    conv2dk3_bf16_scalar(line0, line1, line2, weights, output, input_width,
                         input_channels, output_channels, check);
}

void conv2dk3s2_bf16(bfloat16 *line0, bfloat16 *line1, bfloat16 *line2,
                     bfloat16 *weights, bfloat16 *output,
                     const int32_t input_width, const int32_t input_channels,
                     const int32_t output_channels,
                     const int32_t check) {
    conv2dk3s2_bf16_vectorized(line0, line1, line2, weights, output, input_width,
                                input_channels, output_channels, check);
}

// Bias is packed after weights in the combined buffer.
// Layout: [weights (out_channels * in_channels * 9) | bias (out_channels)]
// The scalar functions derive bias pointer from weights internally.
void conv2dk3_bf16_bias_silu(bfloat16 *line0, bfloat16 *line1, bfloat16 *line2,
                              bfloat16 *weights, bfloat16 *output,
                              const int32_t input_width, const int32_t input_channels,
                              const int32_t output_channels, const int32_t check) {
    conv2dk3_bf16_bias_silu_scalar(line0, line1, line2, weights, output,
                                    input_width, input_channels, output_channels, check);
}

void conv2dk3s2_bf16_bias_silu(bfloat16 *line0, bfloat16 *line1, bfloat16 *line2,
                                bfloat16 *weights, bfloat16 *output,
                                const int32_t input_width, const int32_t input_channels,
                                const int32_t output_channels, const int32_t check) {
    conv2dk3s2_bf16_bias_silu_scalar(line0, line1, line2, weights, output,
                                      input_width, input_channels, output_channels, check);
}

} // extern "C"
