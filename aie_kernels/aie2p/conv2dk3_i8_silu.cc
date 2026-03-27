// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Fused int8 3x3 Conv + Bias + SiLU kernel (AIE2+).
//
// Two paths:
//   Scalar: Padé tanh approximation (fallback for unaligned widths)
//   Vector: aie::mmul<8,8,8> MAC + aie::tanh<bfloat16>() hardware intrinsic
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
// Helper: round-to-nearest (AIE backend lacks __builtin_roundf).
// ---------------------------------------------------------------------------
inline int32_t float_to_int_round(float x) {
    return (x >= 0.0f) ? (int32_t)(x + 0.5f) : (int32_t)(x - 0.5f);
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
// Vectorized stride-1: fused conv3x3 + bias + vectorized SiLU (hw tanh)
//
// Uses aie::mmul<8,8,8,int8,int8> for convolution, then applies SiLU
// via aie::tanh<bfloat16>() hardware intrinsic on 8-element vectors.
// ---------------------------------------------------------------------------
void conv2dk3_i8_silu_vectorized(
    int8_t *__restrict line0, int8_t *__restrict line1,
    int8_t *__restrict line2, int8_t *__restrict weights_and_bias,
    int8_t *__restrict output, const int32_t input_width,
    const int32_t input_channels, const int32_t output_channels,
    const int32_t check, const int32_t shift1, const int32_t shift2) {
    event0();

    using MMUL = aie::mmul<8, 8, 8, int8, int8>;

    int8_t *weights = weights_and_bias;
    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels * 9);

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

    aie::vector<int8, MMUL::size_A> zeros_v =
        aie::zeros<int8, MMUL::size_A>();

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    float scale_in = 1.0f / (float)(1 << shift1);
    float scale_out = (float)(1 << shift2);

    // SiLU constants
    aie::vector<bfloat16, 8> half_v =
        aie::broadcast<bfloat16, 8>((bfloat16)0.5f);
    aie::vector<bfloat16, 8> one_v =
        aie::broadcast<bfloat16, 8>((bfloat16)1.0f);

    // Temporary buffers
    alignas(64) int32_t acc_buf[MMUL::size_C];
    alignas(64) bfloat16 bf16_buf[8];
    alignas(64) int8_t out_buf[MMUL::size_C];

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
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

            // Vectorized SiLU post-processing
            aie::vector<int32, MMUL::size_C> acc_i32 =
                acc.to_vector<int32>(0);
            aie::store_v(acc_buf, acc_i32);

            for (int sp = 0; sp < 8; sp++) {
                // Phase 1: add bias + dequantize (int32 -> bfloat16)
                for (int j = 0; j < 8; j++) {
                    int32_t val =
                        acc_buf[sp * 8 + j] + bias[oc_g * 8 + j];
                    bf16_buf[j] =
                        (bfloat16)((float)val * scale_in);
                }

                // Phase 2: vectorized SiLU via hardware tanh
                aie::vector<bfloat16, 8> x_bf16 =
                    aie::load_v<8>(bf16_buf);
                auto half_x = aie::mul(x_bf16, half_v);
                auto tanh_hx =
                    aie::tanh<bfloat16>(half_x.to_vector<float>());
                auto one_plus = aie::add(tanh_hx, one_v);
                aie::vector<bfloat16, 8> sigmoid =
                    aie::mul(one_plus, half_v);
                auto silu_acc = aie::mul(x_bf16, sigmoid);
                aie::vector<bfloat16, 8> silu_bf16 =
                    silu_acc.to_vector<bfloat16>();

                // Phase 3: requantize (bfloat16 -> int8)
                aie::store_v(bf16_buf, silu_bf16);
                for (int j = 0; j < 8; j++) {
                    float sval = (float)bf16_buf[j];
                    int32_t oval =
                        float_to_int_round(sval * scale_out);
                    oval = (oval > 127)    ? 127
                           : (oval < -128) ? -128
                                           : oval;
                    out_buf[sp * 8 + j] = (int8_t)oval;
                }
            }

            aie::store_v(
                output + oc_g * (output_width * 8) + x_base * 8,
                aie::load_v<MMUL::size_C>(out_buf));
        }

        // Scalar remainder (input_width not divisible by 8)
        for (int x = vec_iters * NUM_W; x < output_width; x++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                int32_t acc_val = 0;
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
                                if (input_x < 0 ||
                                    input_x >= input_width)
                                    continue;
                                int in_idx =
                                    ic_g * (input_width * 8) +
                                    input_x * 8 + ic8;
                                int wt_idx = oc_g * wt_stride_oc +
                                             ic_g * wt_stride_ic +
                                             kh * wt_stride_kh +
                                             kw * wt_stride_kw +
                                             ic8 * 8 + oc8;
                                acc_val += (int32_t)line[in_idx] *
                                           (int32_t)weights[wt_idx];
                            }
                        }
                    }
                }
                acc_val += bias[oc_g * 8 + oc8];
                int out_idx =
                    oc_g * (output_width * 8) + x * 8 + oc8;
                output[out_idx] =
                    pade_silu_i8(acc_val, shift1, shift2);
            }
        }
    }

    ::aie::set_saturation(aie::saturation_mode::none);
    ::aie::set_rounding(aie::rounding_mode::floor);

    event1();
}

// ---------------------------------------------------------------------------
// Helper: extract even/odd 8-element groups from two consecutive vectors
// for stride-2 gather (same as conv2dk3_i8.cc).
// ---------------------------------------------------------------------------
inline void stride2_gather_silu(
    const aie::vector<int8, 64> &vec_lo,
    const aie::vector<int8, 64> &vec_hi,
    aie::vector<int8, 64> &v_even,
    aie::vector<int8, 64> &v_odd) {
    aie::vector<int8, 32> lo_even = aie::filter_even(vec_lo, 8);
    aie::vector<int8, 32> lo_odd = aie::filter_odd(vec_lo, 8);
    aie::vector<int8, 32> hi_even = aie::filter_even(vec_hi, 8);
    aie::vector<int8, 32> hi_odd = aie::filter_odd(vec_hi, 8);
    v_even = aie::concat(lo_even, hi_even);
    v_odd = aie::concat(lo_odd, hi_odd);
}

// ---------------------------------------------------------------------------
// Vectorized stride-2: fused conv3x3 + bias + vectorized SiLU (hw tanh)
// ---------------------------------------------------------------------------
void conv2dk3s2_i8_silu_vectorized(
    int8_t *__restrict line0, int8_t *__restrict line1,
    int8_t *__restrict line2, int8_t *__restrict weights_and_bias,
    int8_t *__restrict output, const int32_t input_width,
    const int32_t input_channels, const int32_t output_channels,
    const int32_t check, const int32_t shift1, const int32_t shift2) {
    event0();

    using MMUL = aie::mmul<8, 8, 8, int8, int8>;

    int8_t *weights = weights_and_bias;
    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels * 9);

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

    float scale_in = 1.0f / (float)(1 << shift1);
    float scale_out = (float)(1 << shift2);

    aie::vector<bfloat16, 8> half_v =
        aie::broadcast<bfloat16, 8>((bfloat16)0.5f);
    aie::vector<bfloat16, 8> one_v =
        aie::broadcast<bfloat16, 8>((bfloat16)1.0f);

    alignas(64) int32_t acc_buf[MMUL::size_C];
    alignas(64) bfloat16 bf16_buf[8];
    alignas(64) int8_t out_buf[MMUL::size_C];

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
                    stride2_gather_silu(vec_lo, vec_hi, v_even, v_odd);

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
                stride2_gather_silu(vec_lo, vec_hi, v_even, v_odd);

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
                    stride2_gather_silu(vec_lo, vec_hi, v_even, v_odd);

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

            // Vectorized SiLU post-processing
            aie::vector<int32, MMUL::size_C> acc_i32 =
                acc.to_vector<int32>(0);
            aie::store_v(acc_buf, acc_i32);

            for (int sp = 0; sp < 8; sp++) {
                for (int j = 0; j < 8; j++) {
                    int32_t val =
                        acc_buf[sp * 8 + j] + bias[oc_g * 8 + j];
                    bf16_buf[j] =
                        (bfloat16)((float)val * scale_in);
                }

                aie::vector<bfloat16, 8> x_bf16 =
                    aie::load_v<8>(bf16_buf);
                auto half_x = aie::mul(x_bf16, half_v);
                auto tanh_hx =
                    aie::tanh<bfloat16>(half_x.to_vector<float>());
                auto one_plus = aie::add(tanh_hx, one_v);
                aie::vector<bfloat16, 8> sigmoid =
                    aie::mul(one_plus, half_v);
                auto silu_acc = aie::mul(x_bf16, sigmoid);
                aie::vector<bfloat16, 8> silu_bf16 =
                    silu_acc.to_vector<bfloat16>();

                aie::store_v(bf16_buf, silu_bf16);
                for (int j = 0; j < 8; j++) {
                    float sval = (float)bf16_buf[j];
                    int32_t oval =
                        float_to_int_round(sval * scale_out);
                    oval = (oval > 127)    ? 127
                           : (oval < -128) ? -128
                                           : oval;
                    out_buf[sp * 8 + j] = (int8_t)oval;
                }
            }

            aie::store_v(
                output + oc_g * (output_width * 8) + vi * NUM_W * 8,
                aie::load_v<MMUL::size_C>(out_buf));
        }
    }

    ::aie::set_saturation(aie::saturation_mode::none);
    ::aie::set_rounding(aie::rounding_mode::floor);

    event1();
}

// ---------------------------------------------------------------------------
// extern "C" wrappers — dispatch to vectorized or scalar
// ---------------------------------------------------------------------------
extern "C" {

void conv2dk3_i8_silu(int8_t *line0, int8_t *line1, int8_t *line2,
                      int8_t *weights_and_bias, int8_t *output,
                      const int32_t input_width, const int32_t input_channels,
                      const int32_t output_channels, const int32_t check,
                      const int32_t shift1, const int32_t shift2) {
    if (input_width % 8 == 0) {
        conv2dk3_i8_silu_vectorized(line0, line1, line2, weights_and_bias,
                                    output, input_width, input_channels,
                                    output_channels, check, shift1, shift2);
    } else {
        conv2dk3_i8_silu_scalar(line0, line1, line2, weights_and_bias, output,
                                input_width, input_channels, output_channels,
                                check, shift1, shift2);
    }
}

void conv2dk3s2_i8_silu(int8_t *line0, int8_t *line1, int8_t *line2,
                        int8_t *weights_and_bias, int8_t *output,
                        const int32_t input_width, const int32_t input_channels,
                        const int32_t output_channels, const int32_t check,
                        const int32_t shift1, const int32_t shift2) {
    int output_width = input_width / 2;
    if (input_width % 8 == 0 && output_width % 8 == 0) {
        conv2dk3s2_i8_silu_vectorized(line0, line1, line2, weights_and_bias,
                                      output, input_width, input_channels,
                                      output_channels, check, shift1, shift2);
    } else {
        conv2dk3s2_i8_silu_scalar(line0, line1, line2, weights_and_bias, output,
                                  input_width, input_channels, output_channels,
                                  check, shift1, shift2);
    }
}

} // extern "C"
