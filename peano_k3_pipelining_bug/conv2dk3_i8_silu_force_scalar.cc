// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Fused int8 3x3 Conv + Bias + SiLU kernel (AIE2+), v2.
//
// Fixes the clipping bug in v1: the v1 vectorized path extracts the MMUL
// accumulator as int8 via to_vector<int8>(shift1), which clips values
// outside [-128,127] BEFORE bias addition. For large accumulator values
// (common with higher input channel counts), this clipping corrupts the
// SiLU result.
//
// v2 approach -- "two-extract int16 reconstruction":
//   1. Set saturation=none, rounding=floor for raw bit extraction
//   2. lo8 = acc.to_vector<int8>(shift1)       -- lower 8 bits via SRS
//   3. hi8 = acc.to_vector<int8>(shift1 + 8)   -- upper 8 bits via SRS
//   4. Reconstruct int16: val = hi8 * 256 + (uint8)lo8
//   5. Convert to bf16, add pre-scaled bias, apply SiLU, requantize
//
// Both to_vector<int8>(shift) calls use SRS with CORRECT element ordering
// on AIE2p (unlike to_vector<int32>(0) which has a known ordering bug).
// Floor rounding ensures exact bit-slice extraction: lo8 captures bits
// [shift1..shift1+7] and hi8 captures bits [shift1+8..shift1+15] of the
// accumulator, allowing exact int16 reconstruction.
//
// Assumption: (acc >> shift1) fits in int16 range [-32768, 32767].
// For 3x3 conv with IC=8, shift1=10: max |acc >> shift1| ~ 1134. Safe.
// For IC=32, shift1=14: max |acc >> shift1| ~ 282. Safe.
//
// Option A structure retained: three separate vectorized functions
// (top/mid/bot) with compile-time kh selection, plus noinline SiLU
// barrier to prevent Peano auto-pipelining codegen issues.
//
// SiLU(x) = x * sigmoid(x) = x * 0.5 * (1 + tanh(x/2))

#define NOCPP

#include "../aie_kernels/aie_kernel_utils.h"

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
// Scalar tail helpers: process remaining width%8 elements after vectorized
// loop. Shared by all 3 vec functions per stride to avoid code duplication.
// ---------------------------------------------------------------------------

// Stride-1 scalar tail: processes elements [tail_start, output_width)
inline void scalar_tail_s1(
    int8_t *line0, int8_t *line1, int8_t *line2,
    int8_t *weights_and_bias, int8_t *output,
    int32_t input_width, int32_t input_channels, int32_t output_channels,
    int32_t oc_g, int32_t tail_start, int32_t output_width,
    int32_t shift1, int32_t shift2, int skip_top, int skip_bot) {

    int8_t *weights = weights_and_bias;
    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels * 9);
    const int ic_groups = input_channels / 8;
    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    for (int x = tail_start; x < output_width; x++) {
        for (int oc8 = 0; oc8 < 8; oc8++) {
            int32_t acc = 0;
            for (int ic_g = 0; ic_g < ic_groups; ic_g++)
                for (int ic8 = 0; ic8 < 8; ic8++)
                    for (int kh = 0; kh < 3; kh++) {
                        if (kh == 0 && skip_top) continue;
                        if (kh == 2 && skip_bot) continue;
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

// Stride-2 scalar tail: processes output elements [tail_start, output_width)
inline void scalar_tail_s2(
    int8_t *line0, int8_t *line1, int8_t *line2,
    int8_t *weights_and_bias, int8_t *output,
    int32_t input_width, int32_t input_channels, int32_t output_channels,
    int32_t oc_g, int32_t tail_start, int32_t output_width,
    int32_t shift1, int32_t shift2, int skip_top, int skip_bot) {

    int8_t *weights = weights_and_bias;
    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels * 9);
    const int ic_groups = input_channels / 8;
    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    for (int x_out = tail_start; x_out < output_width; x_out++) {
        int x_in_base = x_out * 2;
        for (int oc8 = 0; oc8 < 8; oc8++) {
            int32_t acc = 0;
            for (int ic_g = 0; ic_g < ic_groups; ic_g++)
                for (int ic8 = 0; ic8 < 8; ic8++)
                    for (int kh = 0; kh < 3; kh++) {
                        if (kh == 0 && skip_top) continue;
                        if (kh == 2 && skip_bot) continue;
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
// SiLU post-processing — compiled in a SEPARATE .o (silu_postproc_i8.o)
// to avoid Peano codegen degradation when compiled alongside k3 MAC code.
// ---------------------------------------------------------------------------
extern "C" void apply_silu_i8(
    int8_t *__restrict lo8_buf,
    int8_t *__restrict hi8_buf,
    int32_t *__restrict bias, int32_t oc_g,
    int8_t *__restrict out_buf, int32_t shift1, int32_t shift2);

// ---------------------------------------------------------------------------
// Stride-1 vectorized: Option A -- three separate functions (v2)
// ---------------------------------------------------------------------------

// Helper: MAC one kh row for stride-1
template <int NUM_W>
inline void mac_kh_row_s1(
    aie::mmul<8, 8, 8, int8, int8> &acc,
    int8_t *__restrict line_ptr,
    int8_t *__restrict weights,
    int32_t oc_g, int32_t ic_groups, int32_t input_width,
    int32_t vi, int32_t x_base, int kh,
    int32_t wt_stride_oc, int32_t wt_stride_ic,
    int32_t wt_stride_kh, int32_t wt_stride_kw,
    const aie::vector<int8, 64> &zeros_v) {

    using MMUL = aie::mmul<8, 8, 8, int8, int8>;

    for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
        int8_t *__restrict lp = line_ptr + ic_g * (input_width * 8);
        aie::vector<int8, MMUL::size_A> v_c =
            aie::load_v<MMUL::size_A>(lp + x_base * 8);
        aie::vector<int8, MMUL::size_A> v_kw0 = (vi > 0)
            ? aie::shuffle_up_fill(
                  v_c, aie::load_v<MMUL::size_A>(lp + (x_base - NUM_W) * 8), 8)
            : aie::shuffle_up_fill(v_c, zeros_v, 8);
        aie::vector<int8, MMUL::size_A> v_kw2 =
            (x_base + NUM_W < input_width)
            ? aie::shuffle_down_fill(
                  v_c, aie::load_v<MMUL::size_A>(lp + (x_base + NUM_W) * 8), 8)
            : aie::shuffle_down_fill(v_c, zeros_v, 8);
        int8_t *__restrict wp = weights + oc_g * wt_stride_oc +
                                ic_g * wt_stride_ic + kh * wt_stride_kh;
        acc.mac(v_kw0, aie::load_v<MMUL::size_B>(wp));
        acc.mac(v_c, aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
        acc.mac(v_kw2, aie::load_v<MMUL::size_B>(wp + 2 * wt_stride_kw));
    }
}

// TOP: skip kh=0, process kh=1,2
void conv2dk3_i8_silu_vec_top_v2(
    int8_t *__restrict line0, int8_t *__restrict line1,
    int8_t *__restrict line2, int8_t *__restrict weights_and_bias,
    int8_t *__restrict output, const int32_t input_width,
    const int32_t input_channels, const int32_t output_channels,
    const int32_t shift1, const int32_t shift2) {

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
    constexpr int NUM_W = 8;
    const int vec_iters = input_width / NUM_W;
    aie::vector<int8, MMUL::size_A> zeros_v = aie::zeros<int8, MMUL::size_A>();

    // Initial modes for MAC phase (MAC doesn't depend on these, but
    // they're set here so the first iteration's extraction can switch).
    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    alignas(64) int8_t lo8_buf[MMUL::size_C];
    alignas(64) int8_t hi8_buf[MMUL::size_C];
    alignas(64) int8_t out_buf[MMUL::size_C];

    constexpr int MAX_VI = 12;
    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int vi_base = 0; vi_base < vec_iters; vi_base += MAX_VI) {
            int vi_end = (vi_base + MAX_VI < vec_iters) ? vi_base + MAX_VI : vec_iters;
            for (int vi = vi_base; vi < vi_end; vi++) {
            int x_base = vi * NUM_W;
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            // kh=1 (line1)
            mac_kh_row_s1<NUM_W>(acc, line1, weights, oc_g, ic_groups,
                                 input_width, vi, x_base, 1,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // kh=2 (line2)
            mac_kh_row_s1<NUM_W>(acc, line2, weights, oc_g, ic_groups,
                                 input_width, vi, x_base, 2,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // Two-extract: floor rounding + no saturation for exact bits
            ::aie::set_saturation(aie::saturation_mode::none);
            ::aie::set_rounding(aie::rounding_mode::floor);
            aie::store_v(lo8_buf, acc.to_vector<int8>(shift1));
            aie::store_v(hi8_buf, acc.to_vector<int8>(shift1 + 8));
            ::aie::set_saturation(aie::saturation_mode::saturate);
            ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

            apply_silu_i8(lo8_buf, hi8_buf, bias, oc_g, out_buf,
                          shift1, shift2);
            aie::store_v(output + oc_g * (output_width * 8) + x_base * 8,
                         aie::load_v<MMUL::size_C>(out_buf));
            }
        }
        // Scalar tail for remaining width % 8 elements
        if (vec_iters * NUM_W < output_width) {
            scalar_tail_s1(line0, line1, line2, weights_and_bias, output,
                           input_width, input_channels, output_channels,
                           oc_g, vec_iters * NUM_W, output_width,
                           shift1, shift2, /*skip_top=*/1, /*skip_bot=*/0);
        }
    }
}

// MIDDLE: process all three kh rows
void conv2dk3_i8_silu_vec_mid_v2(
    int8_t *__restrict line0, int8_t *__restrict line1,
    int8_t *__restrict line2, int8_t *__restrict weights_and_bias,
    int8_t *__restrict output, const int32_t input_width,
    const int32_t input_channels, const int32_t output_channels,
    const int32_t shift1, const int32_t shift2) {

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
    constexpr int NUM_W = 8;
    const int vec_iters = input_width / NUM_W;
    aie::vector<int8, MMUL::size_A> zeros_v = aie::zeros<int8, MMUL::size_A>();

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    alignas(64) int8_t lo8_buf[MMUL::size_C];
    alignas(64) int8_t hi8_buf[MMUL::size_C];
    alignas(64) int8_t out_buf[MMUL::size_C];

    constexpr int MAX_VI = 12;
    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int vi_base = 0; vi_base < vec_iters; vi_base += MAX_VI) {
            int vi_end = (vi_base + MAX_VI < vec_iters) ? vi_base + MAX_VI : vec_iters;
            for (int vi = vi_base; vi < vi_end; vi++) {
            int x_base = vi * NUM_W;
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            // kh=0 (line0)
            mac_kh_row_s1<NUM_W>(acc, line0, weights, oc_g, ic_groups,
                                 input_width, vi, x_base, 0,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // kh=1 (line1)
            mac_kh_row_s1<NUM_W>(acc, line1, weights, oc_g, ic_groups,
                                 input_width, vi, x_base, 1,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // kh=2 (line2)
            mac_kh_row_s1<NUM_W>(acc, line2, weights, oc_g, ic_groups,
                                 input_width, vi, x_base, 2,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // Two-extract: floor rounding + no saturation for exact bits
            ::aie::set_saturation(aie::saturation_mode::none);
            ::aie::set_rounding(aie::rounding_mode::floor);
            aie::store_v(lo8_buf, acc.to_vector<int8>(shift1));
            aie::store_v(hi8_buf, acc.to_vector<int8>(shift1 + 8));
            ::aie::set_saturation(aie::saturation_mode::saturate);
            ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

            apply_silu_i8(lo8_buf, hi8_buf, bias, oc_g, out_buf,
                          shift1, shift2);
            aie::store_v(output + oc_g * (output_width * 8) + x_base * 8,
                         aie::load_v<MMUL::size_C>(out_buf));
            }
        }
        // Scalar tail for remaining width % 8 elements
        if (vec_iters * NUM_W < output_width) {
            scalar_tail_s1(line0, line1, line2, weights_and_bias, output,
                           input_width, input_channels, output_channels,
                           oc_g, vec_iters * NUM_W, output_width,
                           shift1, shift2, /*skip_top=*/0, /*skip_bot=*/0);
        }
    }
}

// BOTTOM: process kh=0,1, skip kh=2
void conv2dk3_i8_silu_vec_bot_v2(
    int8_t *__restrict line0, int8_t *__restrict line1,
    int8_t *__restrict line2, int8_t *__restrict weights_and_bias,
    int8_t *__restrict output, const int32_t input_width,
    const int32_t input_channels, const int32_t output_channels,
    const int32_t shift1, const int32_t shift2) {

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
    constexpr int NUM_W = 8;
    const int vec_iters = input_width / NUM_W;
    aie::vector<int8, MMUL::size_A> zeros_v = aie::zeros<int8, MMUL::size_A>();

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    alignas(64) int8_t lo8_buf[MMUL::size_C];
    alignas(64) int8_t hi8_buf[MMUL::size_C];
    alignas(64) int8_t out_buf[MMUL::size_C];

    constexpr int MAX_VI = 12;
    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int vi_base = 0; vi_base < vec_iters; vi_base += MAX_VI) {
            int vi_end = (vi_base + MAX_VI < vec_iters) ? vi_base + MAX_VI : vec_iters;
            for (int vi = vi_base; vi < vi_end; vi++) {
            int x_base = vi * NUM_W;
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            // kh=0 (line0)
            mac_kh_row_s1<NUM_W>(acc, line0, weights, oc_g, ic_groups,
                                 input_width, vi, x_base, 0,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // kh=1 (line1)
            mac_kh_row_s1<NUM_W>(acc, line1, weights, oc_g, ic_groups,
                                 input_width, vi, x_base, 1,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // Two-extract: floor rounding + no saturation for exact bits
            ::aie::set_saturation(aie::saturation_mode::none);
            ::aie::set_rounding(aie::rounding_mode::floor);
            aie::store_v(lo8_buf, acc.to_vector<int8>(shift1));
            aie::store_v(hi8_buf, acc.to_vector<int8>(shift1 + 8));
            ::aie::set_saturation(aie::saturation_mode::saturate);
            ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

            apply_silu_i8(lo8_buf, hi8_buf, bias, oc_g, out_buf,
                          shift1, shift2);
            aie::store_v(output + oc_g * (output_width * 8) + x_base * 8,
                         aie::load_v<MMUL::size_C>(out_buf));
            }
        }
        // Scalar tail for remaining width % 8 elements
        if (vec_iters * NUM_W < output_width) {
            scalar_tail_s1(line0, line1, line2, weights_and_bias, output,
                           input_width, input_channels, output_channels,
                           oc_g, vec_iters * NUM_W, output_width,
                           shift1, shift2, /*skip_top=*/0, /*skip_bot=*/1);
        }
    }
}

// ---------------------------------------------------------------------------
// Stride-2 vectorized: Option A -- three separate functions (v2)
// ---------------------------------------------------------------------------

// Helper: MAC one kh row for stride-2
template <int NUM_W>
inline void mac_kh_row_s2(
    aie::mmul<8, 8, 8, int8, int8> &acc,
    int8_t *__restrict line_ptr,
    int8_t *__restrict weights,
    int32_t oc_g, int32_t ic_groups, int32_t input_width,
    int32_t vi, int32_t x_in, int kh,
    int32_t wt_stride_oc, int32_t wt_stride_ic,
    int32_t wt_stride_kh, int32_t wt_stride_kw,
    const aie::vector<int8, 64> &zeros_v) {

    using MMUL = aie::mmul<8, 8, 8, int8, int8>;

    for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
        int8_t *__restrict lp = line_ptr + ic_g * (input_width * 8);
        aie::vector<int8, MMUL::size_A> vec_lo =
            aie::load_v<MMUL::size_A>(lp + x_in * 8);
        aie::vector<int8, MMUL::size_A> vec_hi =
            aie::load_v<MMUL::size_A>(lp + (x_in + NUM_W) * 8);
        // Stride-2 gather: even/odd deinterleave
        aie::vector<int8, 64> v_even =
            aie::concat(aie::filter_even(vec_lo, 8), aie::filter_even(vec_hi, 8));
        aie::vector<int8, 64> v_odd =
            aie::concat(aie::filter_odd(vec_lo, 8), aie::filter_odd(vec_hi, 8));
        aie::vector<int8, MMUL::size_A> v_left = (vi > 0)
            ? aie::shuffle_up_fill(
                  v_odd, aie::load_v<MMUL::size_A>(lp + (x_in - NUM_W) * 8), 8)
            : aie::shuffle_up_fill(v_odd, zeros_v, 8);
        int8_t *__restrict wp = weights + oc_g * wt_stride_oc +
                                ic_g * wt_stride_ic + kh * wt_stride_kh;
        acc.mac(v_left, aie::load_v<MMUL::size_B>(wp));
        acc.mac(v_even, aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
        acc.mac(v_odd, aie::load_v<MMUL::size_B>(wp + 2 * wt_stride_kw));
    }
}

// Stride-2 TOP: skip kh=0, process kh=1,2
void conv2dk3s2_i8_silu_vec_top_v2(
    int8_t *__restrict line0, int8_t *__restrict line1,
    int8_t *__restrict line2, int8_t *__restrict weights_and_bias,
    int8_t *__restrict output, const int32_t input_width,
    const int32_t input_channels, const int32_t output_channels,
    const int32_t shift1, const int32_t shift2) {

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
    constexpr int NUM_W = 8;
    constexpr int INPUT_PER_ITER = 16;
    const int vec_iters = output_width / NUM_W;
    aie::vector<int8, MMUL::size_A> zeros_v = aie::zeros<int8, MMUL::size_A>();

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    alignas(64) int8_t lo8_buf[MMUL::size_C];
    alignas(64) int8_t hi8_buf[MMUL::size_C];
    alignas(64) int8_t out_buf[MMUL::size_C];

    constexpr int MAX_VI = 12;
    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int vi_base = 0; vi_base < vec_iters; vi_base += MAX_VI) {
            int vi_end = (vi_base + MAX_VI < vec_iters) ? vi_base + MAX_VI : vec_iters;
            for (int vi = vi_base; vi < vi_end; vi++) {
            int x_in = vi * INPUT_PER_ITER;
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            // kh=1 (line1)
            mac_kh_row_s2<NUM_W>(acc, line1, weights, oc_g, ic_groups,
                                 input_width, vi, x_in, 1,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // kh=2 (line2)
            mac_kh_row_s2<NUM_W>(acc, line2, weights, oc_g, ic_groups,
                                 input_width, vi, x_in, 2,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // Two-extract: floor rounding + no saturation for exact bits
            ::aie::set_saturation(aie::saturation_mode::none);
            ::aie::set_rounding(aie::rounding_mode::floor);
            aie::store_v(lo8_buf, acc.to_vector<int8>(shift1));
            aie::store_v(hi8_buf, acc.to_vector<int8>(shift1 + 8));
            ::aie::set_saturation(aie::saturation_mode::saturate);
            ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

            apply_silu_i8(lo8_buf, hi8_buf, bias, oc_g, out_buf,
                          shift1, shift2);
            aie::store_v(output + oc_g * (output_width * 8) + vi * NUM_W * 8,
                         aie::load_v<MMUL::size_C>(out_buf));
            }
        }
        // Scalar tail for remaining output_width % 8 elements
        if (vec_iters * NUM_W < output_width) {
            scalar_tail_s2(line0, line1, line2, weights_and_bias, output,
                           input_width, input_channels, output_channels,
                           oc_g, vec_iters * NUM_W, output_width,
                           shift1, shift2, /*skip_top=*/1, /*skip_bot=*/0);
        }
    }
}

// Stride-2 MIDDLE: process all three kh rows
void conv2dk3s2_i8_silu_vec_mid_v2(
    int8_t *__restrict line0, int8_t *__restrict line1,
    int8_t *__restrict line2, int8_t *__restrict weights_and_bias,
    int8_t *__restrict output, const int32_t input_width,
    const int32_t input_channels, const int32_t output_channels,
    const int32_t shift1, const int32_t shift2) {

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
    constexpr int NUM_W = 8;
    constexpr int INPUT_PER_ITER = 16;
    const int vec_iters = output_width / NUM_W;
    aie::vector<int8, MMUL::size_A> zeros_v = aie::zeros<int8, MMUL::size_A>();

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    alignas(64) int8_t lo8_buf[MMUL::size_C];
    alignas(64) int8_t hi8_buf[MMUL::size_C];
    alignas(64) int8_t out_buf[MMUL::size_C];

    constexpr int MAX_VI = 12;
    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int vi_base = 0; vi_base < vec_iters; vi_base += MAX_VI) {
            int vi_end = (vi_base + MAX_VI < vec_iters) ? vi_base + MAX_VI : vec_iters;
            for (int vi = vi_base; vi < vi_end; vi++) {
            int x_in = vi * INPUT_PER_ITER;
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            // kh=0 (line0)
            mac_kh_row_s2<NUM_W>(acc, line0, weights, oc_g, ic_groups,
                                 input_width, vi, x_in, 0,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // kh=1 (line1)
            mac_kh_row_s2<NUM_W>(acc, line1, weights, oc_g, ic_groups,
                                 input_width, vi, x_in, 1,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // kh=2 (line2)
            mac_kh_row_s2<NUM_W>(acc, line2, weights, oc_g, ic_groups,
                                 input_width, vi, x_in, 2,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // Two-extract: floor rounding + no saturation for exact bits
            ::aie::set_saturation(aie::saturation_mode::none);
            ::aie::set_rounding(aie::rounding_mode::floor);
            aie::store_v(lo8_buf, acc.to_vector<int8>(shift1));
            aie::store_v(hi8_buf, acc.to_vector<int8>(shift1 + 8));
            ::aie::set_saturation(aie::saturation_mode::saturate);
            ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

            apply_silu_i8(lo8_buf, hi8_buf, bias, oc_g, out_buf,
                          shift1, shift2);
            aie::store_v(output + oc_g * (output_width * 8) + vi * NUM_W * 8,
                         aie::load_v<MMUL::size_C>(out_buf));
            }
        }
        // Scalar tail for remaining output_width % 8 elements
        if (vec_iters * NUM_W < output_width) {
            scalar_tail_s2(line0, line1, line2, weights_and_bias, output,
                           input_width, input_channels, output_channels,
                           oc_g, vec_iters * NUM_W, output_width,
                           shift1, shift2, /*skip_top=*/0, /*skip_bot=*/0);
        }
    }
}

// Stride-2 BOTTOM: process kh=0,1, skip kh=2
void conv2dk3s2_i8_silu_vec_bot_v2(
    int8_t *__restrict line0, int8_t *__restrict line1,
    int8_t *__restrict line2, int8_t *__restrict weights_and_bias,
    int8_t *__restrict output, const int32_t input_width,
    const int32_t input_channels, const int32_t output_channels,
    const int32_t shift1, const int32_t shift2) {

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
    constexpr int NUM_W = 8;
    constexpr int INPUT_PER_ITER = 16;
    const int vec_iters = output_width / NUM_W;
    aie::vector<int8, MMUL::size_A> zeros_v = aie::zeros<int8, MMUL::size_A>();

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    alignas(64) int8_t lo8_buf[MMUL::size_C];
    alignas(64) int8_t hi8_buf[MMUL::size_C];
    alignas(64) int8_t out_buf[MMUL::size_C];

    constexpr int MAX_VI = 12;
    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int vi_base = 0; vi_base < vec_iters; vi_base += MAX_VI) {
            int vi_end = (vi_base + MAX_VI < vec_iters) ? vi_base + MAX_VI : vec_iters;
            for (int vi = vi_base; vi < vi_end; vi++) {
            int x_in = vi * INPUT_PER_ITER;
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            // kh=0 (line0)
            mac_kh_row_s2<NUM_W>(acc, line0, weights, oc_g, ic_groups,
                                 input_width, vi, x_in, 0,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // kh=1 (line1)
            mac_kh_row_s2<NUM_W>(acc, line1, weights, oc_g, ic_groups,
                                 input_width, vi, x_in, 1,
                                 wt_stride_oc, wt_stride_ic,
                                 wt_stride_kh, wt_stride_kw, zeros_v);

            // Two-extract: floor rounding + no saturation for exact bits
            ::aie::set_saturation(aie::saturation_mode::none);
            ::aie::set_rounding(aie::rounding_mode::floor);
            aie::store_v(lo8_buf, acc.to_vector<int8>(shift1));
            aie::store_v(hi8_buf, acc.to_vector<int8>(shift1 + 8));
            ::aie::set_saturation(aie::saturation_mode::saturate);
            ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

            apply_silu_i8(lo8_buf, hi8_buf, bias, oc_g, out_buf,
                          shift1, shift2);
            aie::store_v(output + oc_g * (output_width * 8) + vi * NUM_W * 8,
                         aie::load_v<MMUL::size_C>(out_buf));
            }
        }
        // Scalar tail for remaining output_width % 8 elements
        if (vec_iters * NUM_W < output_width) {
            scalar_tail_s2(line0, line1, line2, weights_and_bias, output,
                           input_width, input_channels, output_channels,
                           oc_g, vec_iters * NUM_W, output_width,
                           shift1, shift2, /*skip_top=*/0, /*skip_bot=*/1);
        }
    }
}

// ---------------------------------------------------------------------------
// extern "C" wrappers -- dispatch based on check value and width
// Force scalar path for benchmarking comparison.
// ---------------------------------------------------------------------------
extern "C" {

void conv2dk3_i8_silu(int8_t *input, int8_t *weights_and_bias, int8_t *output,
                      const int32_t input_width, const int32_t input_channels,
                      const int32_t output_channels, const int32_t tile_height,
                      const int32_t num_tiles, const int32_t shift1,
                      const int32_t shift2) {
    // Packed-element tiled interface. Force scalar path for comparison.
    event0();
    int row_stride = input_channels * input_width;
    int out_stride = output_channels * input_width;
    int in_tile_stride = (tile_height + 2) * row_stride;
    int out_tile_stride = tile_height * out_stride;
    for (int t = 0; t < num_tiles; t++) {
        int8_t *tile_in = input + t * in_tile_stride;
        int8_t *tile_out = output + t * out_tile_stride;
        for (int r = 0; r < tile_height; r++) {
            conv2dk3_i8_silu_scalar(
                tile_in + r * row_stride,
                tile_in + (r + 1) * row_stride,
                tile_in + (r + 2) * row_stride,
                weights_and_bias, tile_out + r * out_stride,
                input_width, input_channels, output_channels,
                CHECK_MIDDLE, shift1, shift2);
        }
    }
    event1();
}

void conv2dk3s2_i8_silu(int8_t *line0, int8_t *line1, int8_t *line2,
                        int8_t *weights_and_bias, int8_t *output,
                        const int32_t input_width, const int32_t input_channels,
                        const int32_t output_channels, const int32_t check,
                        const int32_t shift1, const int32_t shift2) {
    // Force scalar path for benchmarking comparison.
    conv2dk3s2_i8_silu_scalar(line0, line1, line2, weights_and_bias,
                              output, input_width, input_channels,
                              output_channels, check, shift1, shift2);
}

// Aliases for multi-kernel designs where different MLIR types need
// separate func.func symbols but call the same implementation.
void conv2dk3s2_i8_silu_l5(int8_t *line0, int8_t *line1, int8_t *line2,
                            int8_t *weights_and_bias, int8_t *output,
                            const int32_t input_width,
                            const int32_t input_channels,
                            const int32_t output_channels,
                            const int32_t check, const int32_t shift1,
                            const int32_t shift2) {
    conv2dk3s2_i8_silu(line0, line1, line2, weights_and_bias, output,
                        input_width, input_channels, output_channels, check,
                        shift1, shift2);
}

void conv2dk3s2_i8_silu_l7(int8_t *line0, int8_t *line1, int8_t *line2,
                            int8_t *weights_and_bias, int8_t *output,
                            const int32_t input_width,
                            const int32_t input_channels,
                            const int32_t output_channels,
                            const int32_t check, const int32_t shift1,
                            const int32_t shift2) {
    conv2dk3s2_i8_silu(line0, line1, line2, weights_and_bias, output,
                        input_width, input_channels, output_channels, check,
                        shift1, shift2);
}

} // extern "C"
