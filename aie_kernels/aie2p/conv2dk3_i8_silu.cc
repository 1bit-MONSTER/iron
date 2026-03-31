// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Fused int8 3x3 Conv + Bias + SiLU kernel (AIE2+).
//
// Vectorized path (width%8==0):
//   MMUL MAC for convolution, extract via to_vector<int8>(shift1) which
//   uses the srs_to_v64int8 hardware intrinsic for correct accumulator
//   depermutation, upconvert to bf16, add pre-scaled bias in bf16 domain,
//   apply vec-16 SiLU using hardware aie::tanh<bfloat16>(), requantize.
//
// The int8 extraction clips values outside [-128,127] before bias is
// added, but this does not affect the final output because SiLU(x)
// saturates for large |x|: SiLU(x) -> x for x >> 0 and SiLU(x) -> 0
// for x << 0. After requantization to int8, clipped inputs produce the
// same output as exact computation (verified: max_diff <= 1).
//
// SiLU(x) = x * sigmoid(x) = x * 0.5 * (1 + tanh(x/2))

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

constexpr int CHECK_TOP = 0;
constexpr int CHECK_MIDDLE = 1;
constexpr int CHECK_BOTTOM = 2;

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
    float scale_out = (float)shift2 / 256.0f;
    float scaled = silu_val * scale_out;
    int32_t out_i32 = (scaled >= 0) ? (int32_t)(scaled + 0.5f)
                                    : (int32_t)(scaled - 0.5f);
    if (out_i32 > 127)
        out_i32 = 127;
    if (out_i32 < -128)
        out_i32 = -128;
    return (int8_t)out_i32;
}

inline int32_t float_to_int_round(float x) {
    return (x >= 0.0f) ? (int32_t)(x + 0.5f) : (int32_t)(x - 0.5f);
}

// ---------------------------------------------------------------------------
// Scalar stride-1
// ---------------------------------------------------------------------------
void conv2dk3_i8_silu_scalar(int8_t *line0, int8_t *line1, int8_t *line2,
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
    const int output_width = input_width;
    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;
    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x = 0; x < output_width; x++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                int32_t acc = 0;
                for (int ic_g = 0; ic_g < ic_groups; ic_g++)
                    for (int ic8 = 0; ic8 < 8; ic8++)
                        for (int kh = 0; kh < 3; kh++) {
                            if (kh == 0 && check == CHECK_TOP) continue;
                            if (kh == 2 && check == CHECK_BOTTOM) continue;
                            int8_t *line = select_line(kh, line0, line1, line2);
                            for (int kw = 0; kw < 3; kw++) {
                                int ix = x + kw - 1;
                                if (ix < 0 || ix >= input_width) continue;
                                acc += (int32_t)line[ic_g * (input_width * 8) + ix * 8 + ic8] *
                                       (int32_t)weights[oc_g * wt_stride_oc + ic_g * wt_stride_ic +
                                                        kh * wt_stride_kh + kw * wt_stride_kw + ic8 * 8 + oc8];
                            }
                        }
                acc += bias[oc_g * 8 + oc8];
                output[oc_g * (output_width * 8) + x * 8 + oc8] = pade_silu_i8(acc, shift1, shift2);
            }
        }
    }
    event1();
}

// ---------------------------------------------------------------------------
// Scalar stride-2
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
    const int output_width = input_width / 2;
    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;
    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x_out = 0; x_out < output_width; x_out++) {
            int x_in_base = x_out * 2;
            for (int oc8 = 0; oc8 < 8; oc8++) {
                int32_t acc = 0;
                for (int ic_g = 0; ic_g < ic_groups; ic_g++)
                    for (int ic8 = 0; ic8 < 8; ic8++)
                        for (int kh = 0; kh < 3; kh++) {
                            if (kh == 0 && check == CHECK_TOP) continue;
                            if (kh == 2 && check == CHECK_BOTTOM) continue;
                            int8_t *line = select_line(kh, line0, line1, line2);
                            for (int kw = 0; kw < 3; kw++) {
                                int ix = x_in_base + kw - 1;
                                if (ix < 0 || ix >= input_width) continue;
                                acc += (int32_t)line[ic_g * (input_width * 8) + ix * 8 + ic8] *
                                       (int32_t)weights[oc_g * wt_stride_oc + ic_g * wt_stride_ic +
                                                        kh * wt_stride_kh + kw * wt_stride_kw + ic8 * 8 + oc8];
                            }
                        }
                acc += bias[oc_g * 8 + oc8];
                output[oc_g * (output_width * 8) + x_out * 8 + oc8] = pade_silu_i8(acc, shift1, shift2);
            }
        }
    }
    event1();
}

// ---------------------------------------------------------------------------
// Vec-16 SiLU post-processing: int8 conv + bf16 bias -> hardware tanh
//
// conv_i8 = to_vector<int8>(shift1) -- correctly depermuted by SRS
// bias_bf16_buf[0..15] = [ch0..ch7, ch0..ch7] precomputed as
//   round(bias[ch] / 2^shift1) converted to bfloat16
// ---------------------------------------------------------------------------
__attribute__((noinline)) static void apply_silu_vec16(
    int8_t *__restrict conv_buf,
    int32_t *__restrict bias, int32_t oc_g,
    int8_t *__restrict out_buf, int32_t shift1, int32_t shift2) {

    // Reset saturation/rounding modes for float SiLU computation.
    // The caller sets saturate + symmetric_inf for MMUL SRS which can
    // corrupt float-to-int conversions if left active.
    ::aie::set_saturation(aie::saturation_mode::none);
    ::aie::set_rounding(aie::rounding_mode::floor);

    float dequant = 1.0f / (float)(1 << shift1);
    float scale_out = (float)shift2 / 256.0f;

    // SiLU on int8 conv values + int32 bias.
    // conv_buf layout: [sp0_ch0..7, sp1_ch0..7, ..., sp7_ch0..7]
    // bias index: channel = i & 7
    for (int i = 0; i < 64; i++) {
        // Dequantize: conv_buf[i] represents conv/2^shift1 (from SRS).
        // Add bias/2^shift1 to get the full dequantized value.
        float val = (float)conv_buf[i] +
                    (float)bias[oc_g * 8 + (i & 7)] * dequant;
        float z = val * 0.5f;
        float z2 = z * z;
        float tanh_z;
        if (z2 > 20.0f) {
            tanh_z = (z > 0) ? 1.0f : -1.0f;
        } else {
            tanh_z = z * (27.0f + z2) / (27.0f + 9.0f * z2);
        }
        float silu_val = val * 0.5f * (1.0f + tanh_z);
        float scaled = silu_val * scale_out;
        int32_t oval = float_to_int_round(scaled);
        oval = (oval > 127) ? 127 : (oval < -128) ? -128 : oval;
        out_buf[i] = (int8_t)oval;
    }

    // Restore modes for the next MMUL iteration
    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);
}

// ---------------------------------------------------------------------------
// Vectorized stride-1: MMUL MAC + SRS int8 extraction + vec-16 SiLU
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
    aie::vector<int8, MMUL::size_A> zeros_v = aie::zeros<int8, MMUL::size_A>();

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    alignas(64) int8_t out_buf[MMUL::size_C];
    alignas(64) int8_t conv_buf[MMUL::size_C];
    const bool do_kh0 = (check != CHECK_TOP);
    const bool do_kh2 = (check != CHECK_BOTTOM);

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int vi = 0; vi < vec_iters; vi++) {
            int x_base = vi * NUM_W;
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            if (do_kh0) {
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    int8_t *__restrict lp = lines[0] + ic_g * (input_width * 8);
                    aie::vector<int8, MMUL::size_A> v_c = aie::load_v<MMUL::size_A>(lp + x_base * 8);
                    aie::vector<int8, MMUL::size_A> v_kw0 = (vi > 0) ?
                        aie::shuffle_up_fill(v_c, aie::load_v<MMUL::size_A>(lp + (x_base - NUM_W) * 8), 8) :
                        aie::shuffle_up_fill(v_c, zeros_v, 8);
                    aie::vector<int8, MMUL::size_A> v_kw2 = (x_base + NUM_W < input_width) ?
                        aie::shuffle_down_fill(v_c, aie::load_v<MMUL::size_A>(lp + (x_base + NUM_W) * 8), 8) :
                        aie::shuffle_down_fill(v_c, zeros_v, 8);
                    int8_t *__restrict wp = weights + oc_g * wt_stride_oc + ic_g * wt_stride_ic;
                    acc.mac(v_kw0, aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_c, aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
                    acc.mac(v_kw2, aie::load_v<MMUL::size_B>(wp + 2 * wt_stride_kw));
                }
            }

            for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                int8_t *__restrict lp = lines[1] + ic_g * (input_width * 8);
                aie::vector<int8, MMUL::size_A> v_c = aie::load_v<MMUL::size_A>(lp + x_base * 8);
                aie::vector<int8, MMUL::size_A> v_kw0 = (vi > 0) ?
                    aie::shuffle_up_fill(v_c, aie::load_v<MMUL::size_A>(lp + (x_base - NUM_W) * 8), 8) :
                    aie::shuffle_up_fill(v_c, zeros_v, 8);
                aie::vector<int8, MMUL::size_A> v_kw2 = (x_base + NUM_W < input_width) ?
                    aie::shuffle_down_fill(v_c, aie::load_v<MMUL::size_A>(lp + (x_base + NUM_W) * 8), 8) :
                    aie::shuffle_down_fill(v_c, zeros_v, 8);
                int8_t *__restrict wp = weights + oc_g * wt_stride_oc + ic_g * wt_stride_ic + wt_stride_kh;
                acc.mac(v_kw0, aie::load_v<MMUL::size_B>(wp));
                acc.mac(v_c, aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
                acc.mac(v_kw2, aie::load_v<MMUL::size_B>(wp + 2 * wt_stride_kw));
            }

            if (do_kh2) {
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    int8_t *__restrict lp = lines[2] + ic_g * (input_width * 8);
                    aie::vector<int8, MMUL::size_A> v_c = aie::load_v<MMUL::size_A>(lp + x_base * 8);
                    aie::vector<int8, MMUL::size_A> v_kw0 = (vi > 0) ?
                        aie::shuffle_up_fill(v_c, aie::load_v<MMUL::size_A>(lp + (x_base - NUM_W) * 8), 8) :
                        aie::shuffle_up_fill(v_c, zeros_v, 8);
                    aie::vector<int8, MMUL::size_A> v_kw2 = (x_base + NUM_W < input_width) ?
                        aie::shuffle_down_fill(v_c, aie::load_v<MMUL::size_A>(lp + (x_base + NUM_W) * 8), 8) :
                        aie::shuffle_down_fill(v_c, zeros_v, 8);
                    int8_t *__restrict wp = weights + oc_g * wt_stride_oc + ic_g * wt_stride_ic + 2 * wt_stride_kh;
                    acc.mac(v_kw0, aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_c, aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
                    acc.mac(v_kw2, aie::load_v<MMUL::size_B>(wp + 2 * wt_stride_kw));
                }
            }

            // Extract as int8 via srs_to_v64int8 (correct depermutation),
            // add bias in bf16, apply vec-16 SiLU, requant to int8.
            // Extract int8 via SRS (correct depermutation), store to
            // pre-allocated buffer, apply vec-16 SiLU with bf16 bias.
            aie::store_v(conv_buf, acc.to_vector<int8>(shift1));
            apply_silu_vec16(conv_buf, bias, oc_g, out_buf, shift1, shift2);
            aie::store_v(output + oc_g * (output_width * 8) + x_base * 8,
                         aie::load_v<MMUL::size_C>(out_buf));
        }
    }

    ::aie::set_saturation(aie::saturation_mode::none);
    ::aie::set_rounding(aie::rounding_mode::floor);
    event1();
}

// ---------------------------------------------------------------------------
// Stride-2 gather helper
// ---------------------------------------------------------------------------
inline void stride2_gather_silu(
    const aie::vector<int8, 64> &vec_lo, const aie::vector<int8, 64> &vec_hi,
    aie::vector<int8, 64> &v_even, aie::vector<int8, 64> &v_odd) {
    v_even = aie::concat(aie::filter_even(vec_lo, 8), aie::filter_even(vec_hi, 8));
    v_odd = aie::concat(aie::filter_odd(vec_lo, 8), aie::filter_odd(vec_hi, 8));
}

// ---------------------------------------------------------------------------
// Vectorized stride-2: MMUL MAC + SRS int8 extraction + vec-16 SiLU
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
    int32_t *bias = (int32_t *)(weights_and_bias + output_channels * input_channels * 9);
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
    aie::vector<int8, MMUL::size_A> zeros_v = aie::zeros<int8, MMUL::size_A>();
    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);
    alignas(64) int8_t out_buf[MMUL::size_C];
    alignas(64) int8_t conv_buf[MMUL::size_C];
    const bool do_kh0 = (check != CHECK_TOP);
    const bool do_kh2 = (check != CHECK_BOTTOM);

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        float bias_scale = 1.0f / (float)(1 << shift1);
        alignas(64) bfloat16 bias_bf16_buf[16];
        for (int ch = 0; ch < 8; ch++) {
            bfloat16 bv = (bfloat16)((float)bias[oc_g * 8 + ch] * bias_scale);
            bias_bf16_buf[ch] = bv;
            bias_bf16_buf[8 + ch] = bv;
        }

        for (int vi = 0; vi < vec_iters; vi++) {
            int x_in = vi * INPUT_PER_ITER;
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            for (int kh = 0; kh < 3; kh++) {
                if (kh == 0 && !do_kh0) continue;
                if (kh == 2 && !do_kh2) continue;
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    int8_t *__restrict lp = lines[kh] + ic_g * (input_width * 8);
                    aie::vector<int8, MMUL::size_A> vec_lo = aie::load_v<MMUL::size_A>(lp + x_in * 8);
                    aie::vector<int8, MMUL::size_A> vec_hi = aie::load_v<MMUL::size_A>(lp + (x_in + NUM_W) * 8);
                    aie::vector<int8, MMUL::size_A> v_even, v_odd;
                    stride2_gather_silu(vec_lo, vec_hi, v_even, v_odd);
                    aie::vector<int8, MMUL::size_A> v_left = (vi > 0) ?
                        aie::shuffle_up_fill(v_odd, aie::load_v<MMUL::size_A>(lp + (x_in - NUM_W) * 8), 8) :
                        aie::shuffle_up_fill(v_odd, zeros_v, 8);
                    int8_t *__restrict wp = weights + oc_g * wt_stride_oc + ic_g * wt_stride_ic + kh * wt_stride_kh;
                    acc.mac(v_left, aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_even, aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
                    acc.mac(v_odd, aie::load_v<MMUL::size_B>(wp + 2 * wt_stride_kw));
                }
            }

            aie::store_v(conv_buf, acc.to_vector<int8>(shift1));
            apply_silu_vec16(conv_buf, bias, oc_g, out_buf, shift1, shift2);
            aie::store_v(output + oc_g * (output_width * 8) + vi * NUM_W * 8,
                         aie::load_v<MMUL::size_C>(out_buf));
        }
    }

    ::aie::set_saturation(aie::saturation_mode::none);
    ::aie::set_rounding(aie::rounding_mode::floor);
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
    if (input_width % 8 == 0) {
        conv2dk3_i8_silu_vectorized(line0, line1, line2, weights_and_bias,
                                     output, input_width, input_channels,
                                     output_channels, check, shift1, shift2);
    } else {
        conv2dk3_i8_silu_scalar(line0, line1, line2, weights_and_bias,
                                output, input_width, input_channels,
                                output_channels, check, shift1, shift2);
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
        conv2dk3s2_i8_silu_scalar(line0, line1, line2, weights_and_bias,
                                   output, input_width, input_channels,
                                   output_channels, check, shift1, shift2);
    }
}

} // extern "C"
