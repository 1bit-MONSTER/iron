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

    int8_t *lines[3] = {line0, line1, line2};

    constexpr int NUM_W = 8;
    const int vec_iters = input_width / NUM_W;
    const int scalar_start = vec_iters * NUM_W;

    aie::vector<int8, MMUL::size_A> zeros_v =
        aie::zeros<int8, MMUL::size_A>();

    // Set saturation/rounding once at function start (same pattern as
    // working conv2dk1_i8). Applies to to_vector<int8>(scale) SRS.
    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {

        // ---- Vectorized: groups of 8 positions from x=0 ----
        for (int vi = 0; vi < vec_iters; vi++) {
            int x_base = vi * NUM_W;

            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            // kh=0: skip if top border (check == CHECK_TOP)
            if (check != CHECK_TOP) {
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    int8_t *__restrict lp =
                        lines[0] + ic_g * (input_width * 8);

                    aie::vector<int8, MMUL::size_A> v_c =
                        aie::load_v<MMUL::size_A>(lp + x_base * 8);

                    aie::vector<int8, MMUL::size_A> v_kw0;
                    if (vi > 0) {
                        v_kw0 = aie::shuffle_up_fill(
                            v_c,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_base - NUM_W) * 8),
                            8);
                    } else {
                        v_kw0 = aie::shuffle_up_fill(v_c, zeros_v, 8);
                    }

                    aie::vector<int8, MMUL::size_A> v_kw2;
                    if (x_base + NUM_W < input_width) {
                        v_kw2 = aie::shuffle_down_fill(
                            v_c,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_base + NUM_W) * 8),
                            8);
                    } else {
                        v_kw2 =
                            aie::shuffle_down_fill(v_c, zeros_v, 8);
                    }

                    int8_t *__restrict wp =
                        weights + oc_g * wt_stride_oc +
                        ic_g * wt_stride_ic + 0 * wt_stride_kh;

                    acc.mac(v_kw0,
                            aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_c,
                            aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
                    acc.mac(v_kw2,
                            aie::load_v<MMUL::size_B>(
                                wp + 2 * wt_stride_kw));
                }
            }

            // kh=1: always process (middle row is always valid)
            for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                int8_t *__restrict lp =
                    lines[1] + ic_g * (input_width * 8);

                aie::vector<int8, MMUL::size_A> v_c =
                    aie::load_v<MMUL::size_A>(lp + x_base * 8);

                aie::vector<int8, MMUL::size_A> v_kw0;
                if (vi > 0) {
                    v_kw0 = aie::shuffle_up_fill(
                        v_c,
                        aie::load_v<MMUL::size_A>(
                            lp + (x_base - NUM_W) * 8),
                        8);
                } else {
                    v_kw0 = aie::shuffle_up_fill(v_c, zeros_v, 8);
                }

                aie::vector<int8, MMUL::size_A> v_kw2;
                if (x_base + NUM_W < input_width) {
                    v_kw2 = aie::shuffle_down_fill(
                        v_c,
                        aie::load_v<MMUL::size_A>(
                            lp + (x_base + NUM_W) * 8),
                        8);
                } else {
                    v_kw2 =
                        aie::shuffle_down_fill(v_c, zeros_v, 8);
                }

                int8_t *__restrict wp =
                    weights + oc_g * wt_stride_oc +
                    ic_g * wt_stride_ic + 1 * wt_stride_kh;

                acc.mac(v_kw0,
                        aie::load_v<MMUL::size_B>(wp));
                acc.mac(v_c,
                        aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
                acc.mac(v_kw2,
                        aie::load_v<MMUL::size_B>(
                            wp + 2 * wt_stride_kw));
            }

            // kh=2: skip if bottom border (check == CHECK_BOTTOM)
            if (check != CHECK_BOTTOM) {
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    int8_t *__restrict lp =
                        lines[2] + ic_g * (input_width * 8);

                    aie::vector<int8, MMUL::size_A> v_c =
                        aie::load_v<MMUL::size_A>(lp + x_base * 8);

                    aie::vector<int8, MMUL::size_A> v_kw0;
                    if (vi > 0) {
                        v_kw0 = aie::shuffle_up_fill(
                            v_c,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_base - NUM_W) * 8),
                            8);
                    } else {
                        v_kw0 = aie::shuffle_up_fill(v_c, zeros_v, 8);
                    }

                    aie::vector<int8, MMUL::size_A> v_kw2;
                    if (x_base + NUM_W < input_width) {
                        v_kw2 = aie::shuffle_down_fill(
                            v_c,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_base + NUM_W) * 8),
                            8);
                    } else {
                        v_kw2 =
                            aie::shuffle_down_fill(v_c, zeros_v, 8);
                    }

                    int8_t *__restrict wp =
                        weights + oc_g * wt_stride_oc +
                        ic_g * wt_stride_ic + 2 * wt_stride_kh;

                    acc.mac(v_kw0,
                            aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_c,
                            aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
                    acc.mac(v_kw2,
                            aie::load_v<MMUL::size_B>(
                                wp + 2 * wt_stride_kw));
                }
            }

            aie::vector<int8, MMUL::size_C> result =
                acc.to_vector<int8>(scale);
            aie::store_v(output + oc_g * (output_width * 8) + x_base * 8,
                         result);
        }

        // ---- Scalar remainder (input_width not divisible by 8) ----
        for (int x = scalar_start; x < output_width; x++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                int32_t sum = 0;
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = 0; kh < 3; kh++) {
                            if (kh == 0 && check == CHECK_TOP)
                                continue;
                            if (kh == 2 && check == CHECK_BOTTOM)
                                continue;
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

    ::aie::set_saturation(aie::saturation_mode::none);
    ::aie::set_rounding(aie::rounding_mode::floor);

    event1();
}

// ---------------------------------------------------------------------------
// Vectorized stride-2 implementation
//
// Uses aie::mmul<8,8,8,int8,int8> to compute 8 output positions x 8 output
// channels at a time. Each group of 8 outputs consumes 16 input positions
// (stride 2). Even/odd positions are separated using filter_even/filter_odd
// with chunk_size=8 to gather stride-2 centers (even) and rights (odd).
//
// For 8 output positions at stride-2:
//   center[i] = input[2*i]    -> v_even = [pos0, pos2, ..., pos14]
//   right[i]  = input[2*i+1]  -> v_odd  = [pos1, pos3, ..., pos15]
//   left[i]   = input[2*i-1]  -> v_left = [pad/-1, pos1, pos3, ..., pos13]
//
// Output: acc32 right-shifted by `scale` with rounding, saturated to int8.
// ---------------------------------------------------------------------------

// Helper: extract even/odd 8-element groups from two consecutive vectors.
// vec_lo = [pos0..pos7], vec_hi = [pos8..pos15] (each pos = 8 int8 values).
// Returns v_even = [pos0, pos2, pos4, pos6, pos8, pos10, pos12, pos14]
//         v_odd  = [pos1, pos3, pos5, pos7, pos9, pos11, pos13, pos15]
//
// Uses filter_even/filter_odd (chunk_size=8) on each half independently,
// then concatenates. This avoids interleave_unzip which was producing
// incorrect results for int8 with step=8 on AIE2p hardware.
inline void stride2_gather(
    const aie::vector<int8, 64> &vec_lo,
    const aie::vector<int8, 64> &vec_hi,
    aie::vector<int8, 64> &v_even,
    aie::vector<int8, 64> &v_odd) {
    // filter_even(v, 8): from [G0,G1,G2,G3,G4,G5,G6,G7] -> [G0,G2,G4,G6]
    // filter_odd(v, 8):  from [G0,G1,G2,G3,G4,G5,G6,G7] -> [G1,G3,G5,G7]
    // Each returns vector<int8, 32> (half size).
    aie::vector<int8, 32> lo_even = aie::filter_even(vec_lo, 8);
    aie::vector<int8, 32> lo_odd = aie::filter_odd(vec_lo, 8);
    aie::vector<int8, 32> hi_even = aie::filter_even(vec_hi, 8);
    aie::vector<int8, 32> hi_odd = aie::filter_odd(vec_hi, 8);

    v_even = aie::concat(lo_even, hi_even);
    v_odd = aie::concat(lo_odd, hi_odd);
}

void conv2dk3s2_i8_vectorized(int8_t *__restrict line0,
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
    const int output_width = input_width / 2;

    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    int8_t *lines[3] = {line0, line1, line2};

    constexpr int NUM_W = 8;
    constexpr int INPUT_PER_ITER = 16;
    const int vec_iters = output_width / NUM_W;

    aie::vector<int8, MMUL::size_A> zeros_v =
        aie::zeros<int8, MMUL::size_A>();

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {

        for (int vi = 0; vi < vec_iters; vi++) {
            int x_in = vi * INPUT_PER_ITER;

            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            // kh=0: skip if top border
            if (check != CHECK_TOP) {
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    int8_t *__restrict lp =
                        lines[0] + ic_g * (input_width * 8);

                    aie::vector<int8, MMUL::size_A> vec_lo =
                        aie::load_v<MMUL::size_A>(lp + x_in * 8);
                    aie::vector<int8, MMUL::size_A> vec_hi =
                        aie::load_v<MMUL::size_A>(
                            lp + (x_in + NUM_W) * 8);

                    aie::vector<int8, MMUL::size_A> v_even, v_odd;
                    stride2_gather(vec_lo, vec_hi, v_even, v_odd);

                    aie::vector<int8, MMUL::size_A> v_left;
                    if (vi > 0) {
                        v_left = aie::shuffle_up_fill(
                            v_odd,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_in - NUM_W) * 8),
                            8);
                    } else {
                        v_left = aie::shuffle_up_fill(
                            v_odd, zeros_v, 8);
                    }

                    int8_t *__restrict wp =
                        weights + oc_g * wt_stride_oc +
                        ic_g * wt_stride_ic + 0 * wt_stride_kh;

                    acc.mac(v_left,
                            aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_even,
                            aie::load_v<MMUL::size_B>(
                                wp + wt_stride_kw));
                    acc.mac(v_odd,
                            aie::load_v<MMUL::size_B>(
                                wp + 2 * wt_stride_kw));
                }
            }

            // kh=1: always process
            for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                int8_t *__restrict lp =
                    lines[1] + ic_g * (input_width * 8);

                aie::vector<int8, MMUL::size_A> vec_lo =
                    aie::load_v<MMUL::size_A>(lp + x_in * 8);
                aie::vector<int8, MMUL::size_A> vec_hi =
                    aie::load_v<MMUL::size_A>(
                        lp + (x_in + NUM_W) * 8);

                aie::vector<int8, MMUL::size_A> v_even, v_odd;
                stride2_gather(vec_lo, vec_hi, v_even, v_odd);

                aie::vector<int8, MMUL::size_A> v_left;
                if (vi > 0) {
                    v_left = aie::shuffle_up_fill(
                        v_odd,
                        aie::load_v<MMUL::size_A>(
                            lp + (x_in - NUM_W) * 8),
                        8);
                } else {
                    v_left = aie::shuffle_up_fill(
                        v_odd, zeros_v, 8);
                }

                int8_t *__restrict wp =
                    weights + oc_g * wt_stride_oc +
                    ic_g * wt_stride_ic + 1 * wt_stride_kh;

                acc.mac(v_left,
                        aie::load_v<MMUL::size_B>(wp));
                acc.mac(v_even,
                        aie::load_v<MMUL::size_B>(
                            wp + wt_stride_kw));
                acc.mac(v_odd,
                        aie::load_v<MMUL::size_B>(
                            wp + 2 * wt_stride_kw));
            }

            // kh=2: skip if bottom border
            if (check != CHECK_BOTTOM) {
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    int8_t *__restrict lp =
                        lines[2] + ic_g * (input_width * 8);

                    aie::vector<int8, MMUL::size_A> vec_lo =
                        aie::load_v<MMUL::size_A>(lp + x_in * 8);
                    aie::vector<int8, MMUL::size_A> vec_hi =
                        aie::load_v<MMUL::size_A>(
                            lp + (x_in + NUM_W) * 8);

                    aie::vector<int8, MMUL::size_A> v_even, v_odd;
                    stride2_gather(vec_lo, vec_hi, v_even, v_odd);

                    aie::vector<int8, MMUL::size_A> v_left;
                    if (vi > 0) {
                        v_left = aie::shuffle_up_fill(
                            v_odd,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_in - NUM_W) * 8),
                            8);
                    } else {
                        v_left = aie::shuffle_up_fill(
                            v_odd, zeros_v, 8);
                    }

                    int8_t *__restrict wp =
                        weights + oc_g * wt_stride_oc +
                        ic_g * wt_stride_ic + 2 * wt_stride_kh;

                    acc.mac(v_left,
                            aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_even,
                            aie::load_v<MMUL::size_B>(
                                wp + wt_stride_kw));
                    acc.mac(v_odd,
                            aie::load_v<MMUL::size_B>(
                                wp + 2 * wt_stride_kw));
                }
            }

            aie::vector<int8, MMUL::size_C> result =
                acc.to_vector<int8>(scale);
            aie::store_v(
                output + oc_g * (output_width * 8) + vi * NUM_W * 8,
                result);
        }

        // No remainder handling here — the extern "C" wrapper
        // dispatches to the scalar function when output_width % 8 != 0.
    }

    ::aie::set_saturation(aie::saturation_mode::none);
    ::aie::set_rounding(aie::rounding_mode::floor);

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
    // Vectorized path requires width*8 to be 64-byte aligned (i.e. width
    // must be a multiple of 8) because aie::load_v<64> needs 64-byte
    // alignment and the per-ic-group stride is width*8 bytes.  When
    // width % 8 != 0 the stride is not a multiple of 64 and the loads
    // for ic_g >= 1 silently read from a wrong aligned address.
    if (input_width % 8 == 0) {
        conv2dk3_i8_vectorized(line0, line1, line2, weights, output,
                                input_width, input_channels, output_channels,
                                check, scale);
    } else {
        conv2dk3_i8_scalar(line0, line1, line2, weights, output,
                            input_width, input_channels, output_channels,
                            check, scale);
    }
}

void conv2dk3s2_i8(int8_t *line0, int8_t *line1, int8_t *line2,
                    int8_t *weights, int8_t *output,
                    const int32_t input_width, const int32_t input_channels,
                    const int32_t output_channels, const int32_t check,
                    const int32_t scale) {
    // Vectorized path requires:
    //   1) input_width % 8 == 0 (64-byte aligned vector loads)
    //   2) output_width % 8 == 0 (full MMUL blocks, no remainder)
    // When output_width is not a multiple of 8, use the scalar path
    // to avoid remainder handling issues with the Chess compiler.
    int output_width = input_width / 2;
    if (input_width % 8 == 0 && output_width % 8 == 0) {
        conv2dk3s2_i8_vectorized(line0, line1, line2, weights, output,
                                  input_width, input_channels,
                                  output_channels, check, scale);
    } else {
        conv2dk3s2_i8_scalar(line0, line1, line2, weights, output,
                              input_width, input_channels, output_channels,
                              check, scale);
    }
}

} // extern "C"
