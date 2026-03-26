// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// 3x3 Convolution kernel for int8 activations and weights (AIE2+).
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
// Output quantization: accumulate in int32, then right-shift by `scale`
// with rounding and saturate to int8 [-128, 127].

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

// Saturation limits
constexpr int32_t SAT_MAX = 127;
constexpr int32_t SAT_MIN = -128;

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
// Helper: right-shift with rounding and saturate to int8.
// ---------------------------------------------------------------------------
inline int8_t quantize_i8(int32_t sum, int32_t scale) {
    int32_t sum_srs = (sum + (1 << (scale - 1))) >> scale;
    sum_srs = (sum_srs > SAT_MAX) ? SAT_MAX : (sum_srs < SAT_MIN) ? SAT_MIN : sum_srs;
    return (int8_t)sum_srs;
}

// ---------------------------------------------------------------------------
// Scalar stride-1 implementation
// ---------------------------------------------------------------------------
void conv2dk3_i8_scalar(int8_t *line0, int8_t *line1, int8_t *line2,
                         int8_t *weights, int8_t *output,
                         const int32_t input_width,
                         const int32_t input_channels,
                         const int32_t output_channels,
                         const int32_t check,
                         const int32_t scale) {
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
                int32_t sum = 0;

                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = 0; kh < 3; kh++) {
                            // Vertical border: skip this row if padding
                            if (kh == 0 && check == CHECK_TOP)
                                continue;
                            if (kh == 2 && check == CHECK_BOTTOM)
                                continue;

                            int8_t *line = select_line(kh, line0, line1, line2);

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

                                sum += (int32_t)line[in_idx] * (int32_t)weights[wt_idx];
                            }
                        }
                    }
                }

                // Output index: [oc_g, x, oc8]
                int out_idx = oc_g * (output_width * 8) + x * 8 + oc8;
                output[out_idx] = quantize_i8(sum, scale);
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// Scalar stride-2 implementation
// ---------------------------------------------------------------------------
void conv2dk3s2_i8_scalar(int8_t *line0, int8_t *line1, int8_t *line2,
                           int8_t *weights, int8_t *output,
                           const int32_t input_width,
                           const int32_t input_channels,
                           const int32_t output_channels,
                           const int32_t check,
                           const int32_t scale) {
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
                int32_t sum = 0;

                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = 0; kh < 3; kh++) {
                            if (kh == 0 && check == CHECK_TOP)
                                continue;
                            if (kh == 2 && check == CHECK_BOTTOM)
                                continue;

                            int8_t *line = select_line(kh, line0, line1, line2);

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

                                sum += (int32_t)line[in_idx] * (int32_t)weights[wt_idx];
                            }
                        }
                    }
                }

                int out_idx = oc_g * (output_width * 8) + x_out * 8 + oc8;
                output[out_idx] = quantize_i8(sum, scale);
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// Vectorized stride-1 implementation
//
// Uses aie::mmul<8,8,8,int8,int8> to compute 8 output positions x 8 output
// channels at a time. Processes ALL positions (including borders) in aligned
// groups of 8, starting from x=0.
//
// Alignment: AIE vector load/store requires the address to be aligned to
// the vector width. For int8 with 8 channels/position, each position is
// 8 bytes, so a 64-element load (64 bytes) must start at a 64-byte-aligned
// address. Starting from x=0 (byte offset 0) ensures aligned stores.
// For kw=0 and kw=2 (offsets ±1 position = ±8 bytes), we use
// shuffle_up_fill / shuffle_down_fill to construct shifted input vectors
// from two aligned loads, avoiding misaligned memory access.
//
// Border handling: Left/right zero-padding is built into the vectorized
// path via shuffle with a zeros vector (no separate scalar border code).
//
// Output: acc32 right-shifted by `scale` with rounding, saturated to int8.
// ---------------------------------------------------------------------------
void conv2dk3_i8_vectorized(int8_t *__restrict line0,
                             int8_t *__restrict line1,
                             int8_t *__restrict line2,
                             int8_t *__restrict weights,
                             int8_t *__restrict output,
                             const int32_t input_width,
                             const int32_t input_channels,
                             const int32_t output_channels,
                             const int32_t check,
                             const int32_t scale) {
    event0();

    using MMUL = aie::mmul<8, 8, 8, int8, int8>;

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width;

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

    int8_t *lines[3] = {line0, line1, line2};

    constexpr int NUM_W = 8;
    const int vec_iters = input_width / NUM_W;
    const int scalar_start = vec_iters * NUM_W;

    aie::vector<int8, MMUL::size_A> zeros_v =
        aie::zeros<int8, MMUL::size_A>();

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {

        // ---- Vectorized: groups of 8 positions from x=0 ----
        for (int vi = 0; vi < vec_iters; vi++) {
            int x_base = vi * NUM_W;

            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                for (int kh = kh_start; kh < kh_end; kh++) {
                    int8_t *__restrict lp =
                        lines[kh] + ic_g * (input_width * 8);

                    // Center column (kw=1): aligned load at x_base
                    aie::vector<int8, MMUL::size_A> v_c =
                        aie::load_v<MMUL::size_A>(lp + x_base * 8);

                    // Left column (kw=0): positions [x_base-1 .. x_base+6]
                    // Shift v_c up by 8, fill bottom 8 from previous block
                    aie::vector<int8, MMUL::size_A> v_kw0;
                    if (vi > 0) {
                        aie::vector<int8, MMUL::size_A> v_prev =
                            aie::load_v<MMUL::size_A>(
                                lp + (x_base - NUM_W) * 8);
                        v_kw0 = aie::shuffle_up_fill(v_c, v_prev, 8);
                    } else {
                        v_kw0 = aie::shuffle_up_fill(v_c, zeros_v, 8);
                    }

                    // Right column (kw=2): positions [x_base+1 .. x_base+8]
                    // Shift v_c down by 8, fill top 8 from next block
                    aie::vector<int8, MMUL::size_A> v_kw2;
                    if (x_base + NUM_W < input_width) {
                        aie::vector<int8, MMUL::size_A> v_next =
                            aie::load_v<MMUL::size_A>(
                                lp + (x_base + NUM_W) * 8);
                        v_kw2 =
                            aie::shuffle_down_fill(v_c, v_next, 8);
                    } else {
                        v_kw2 =
                            aie::shuffle_down_fill(v_c, zeros_v, 8);
                    }

                    // Weight loads (each kw tile is 64 bytes, aligned)
                    int8_t *__restrict wp =
                        weights + oc_g * wt_stride_oc +
                        ic_g * wt_stride_ic + kh * wt_stride_kh;

                    acc.mac(v_kw0,
                            aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_c,
                            aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
                    acc.mac(v_kw2,
                            aie::load_v<MMUL::size_B>(
                                wp + 2 * wt_stride_kw));
                }
            }

            ::aie::set_saturation(aie::saturation_mode::saturate);
            ::aie::set_rounding(aie::rounding_mode::symmetric_inf);
            aie::vector<int8, MMUL::size_C> result =
                acc.to_vector<int8>(scale);
            ::aie::set_saturation(aie::saturation_mode::none);
            ::aie::set_rounding(aie::rounding_mode::floor);
            aie::store_v(output + oc_g * (output_width * 8) + x_base * 8,
                         result);
        }

        // ---- Scalar remainder (input_width not divisible by 8) ----
        for (int x = scalar_start; x < output_width; x++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                int32_t sum = 0;
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = kh_start; kh < kh_end; kh++) {
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
                                sum += (int32_t)lines[kh][in_idx] *
                                       (int32_t)weights[wt_idx];
                            }
                        }
                    }
                }
                output[oc_g * (output_width * 8) + x * 8 + oc8] =
                    quantize_i8(sum, scale);
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// extern "C" wrappers
// ---------------------------------------------------------------------------
extern "C" {

void conv2dk3_i8(int8_t *line0, int8_t *line1, int8_t *line2,
                  int8_t *weights, int8_t *output,
                  const int32_t input_width, const int32_t input_channels,
                  const int32_t output_channels, const int32_t check,
                  const int32_t scale) {
    conv2dk3_i8_vectorized(line0, line1, line2, weights, output,
                            input_width, input_channels, output_channels, check, scale);
}

void conv2dk3s2_i8(int8_t *line0, int8_t *line1, int8_t *line2,
                    int8_t *weights, int8_t *output,
                    const int32_t input_width, const int32_t input_channels,
                    const int32_t output_channels, const int32_t check,
                    const int32_t scale) {
    conv2dk3s2_i8_scalar(line0, line1, line2, weights, output,
                          input_width, input_channels, output_channels, check, scale);
}

} // extern "C"
