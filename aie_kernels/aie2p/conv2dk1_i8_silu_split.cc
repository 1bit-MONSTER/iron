// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Fused int8 1x1 Conv + Bias + SiLU kernel (AIE2+), split compilation.
//
// Mirrors the k3 split pattern: MAC code in this TU, SiLU post-processing
// in a separate TU (silu_postproc_i8.o) linked via partial-link.
//
// This avoids Peano codegen bugs where co-compiling SiLU (hardware tanh)
// with MAC code causes accumulator corruption at small ic_iters (IC < 96).
// With split compilation, the register allocator sees a simpler function
// body and generates correct code for all IC values.
//
// Both scalar and vectorized paths are always compiled; dispatch is at
// runtime based on width % 8.

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define REL_WRITE 0
#define REL_READ 1

// ---------------------------------------------------------------------------
// Pade rational approximation for scalar fallback
// ---------------------------------------------------------------------------
inline float pade_tanh(float z) {
    float z2 = z * z;
    if (z2 > 20.0f)
        return (z > 0.0f) ? 1.0f : -1.0f;
    return z * (27.0f + z2) / (27.0f + 9.0f * z2);
}

inline float silu_float(float x) {
    float tanh_hx = pade_tanh(x * 0.5f);
    return x * 0.5f * (1.0f + tanh_hx);
}

inline int32_t float_to_int_round(float x) {
    return (x >= 0.0f) ? (int32_t)(x + 0.5f) : (int32_t)(x - 0.5f);
}

// ---------------------------------------------------------------------------
// Scalar: fused conv1x1 + bias + SiLU (Pade tanh)
// ---------------------------------------------------------------------------
static void conv2dk1_i8_silu_scalar_row(
    int8_t *input, int8_t *weights_and_bias, int8_t *output,
    const int32_t input_width, const int32_t input_channels,
    const int32_t output_channels, const int32_t shift1,
    const int32_t shift2) {

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int wt_stride_ic = 64; // 8 * 8
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels);

    float scale_in = 1.0f / (float)(1 << shift1);
    float scale_out = (float)shift2 / 256.0f;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x = 0; x < input_width; x++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                int32_t acc = 0;

                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        int in_idx =
                            ic_g * (input_width * 8) + x * 8 + ic8;
                        int wt_idx = oc_g * wt_stride_oc +
                                     ic_g * wt_stride_ic + ic8 * 8 + oc8;
                        acc += (int32_t)input[in_idx] *
                               (int32_t)weights_and_bias[wt_idx];
                    }
                }

                acc += bias[oc_g * 8 + oc8];

                float fval = (float)acc * scale_in;
                float sval = silu_float(fval);
                int32_t out_val = float_to_int_round(sval * scale_out);
                out_val = (out_val > 127)    ? 127
                          : (out_val < -128) ? -128
                                             : out_val;

                int out_idx =
                    oc_g * (input_width * 8) + x * 8 + oc8;
                output[out_idx] = (int8_t)out_val;
            }
        }
    }
}

// ---------------------------------------------------------------------------
// SiLU post-processing — compiled in a SEPARATE .o (silu_postproc_i8.o)
// ---------------------------------------------------------------------------
extern "C" void apply_silu_i8(
    int8_t *__restrict lo8_buf,
    int8_t *__restrict hi8_buf,
    int32_t *__restrict bias, int32_t oc_g,
    int8_t *__restrict out_buf, int32_t shift1, int32_t shift2);

// ---------------------------------------------------------------------------
// MAC helper for k1 vectorized: accumulate over all IC groups.
// INLINE so Peano sees acc.mac() writes, preventing LICM from hoisting
// the acc=zeros() zero-init out of the wi loop.
// ---------------------------------------------------------------------------
inline void mac_k1_all_ic(
    aie::mmul<8, 8, 8, int8, int8> &acc,
    int8_t *__restrict input_base, int8_t *__restrict kernels,
    int32_t oc_g, int32_t wi, int32_t iw, int32_t ic_iters) {

    using MMUL = aie::mmul<8, 8, 8, int8, int8>;

    int8_t *in_ptr = input_base + wi * MMUL::size_A;
    int8_t *wt_ptr = kernels + oc_g * ic_iters * MMUL::size_B;

    for (int ic = 0; ic < ic_iters; ic++) {
        aie::vector<int8, MMUL::size_B> in_b =
            aie::load_v<MMUL::size_B>(wt_ptr);
        wt_ptr += MMUL::size_B;

        aie::vector<int8, MMUL::size_A> in_a =
            aie::load_v<MMUL::size_A>(in_ptr);
        in_ptr += iw * 8;

        acc.mac(in_a, in_b);
    }
}

// ---------------------------------------------------------------------------
// Scalar tail for partial vectorization: processes elements [tail_start, iw)
// ---------------------------------------------------------------------------
inline void scalar_tail_k1(
    int8_t *input, int8_t *weights_and_bias, int8_t *output,
    int32_t input_width, int32_t input_channels, int32_t output_channels,
    int32_t oc_g, int32_t tail_start,
    int32_t shift1, int32_t shift2) {

    const int ic_groups = input_channels / 8;
    const int wt_stride_ic = 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;
    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels);

    float scale_in = 1.0f / (float)(1 << shift1);
    float scale_out = (float)shift2 / 256.0f;

    for (int x = tail_start; x < input_width; x++) {
        for (int oc8 = 0; oc8 < 8; oc8++) {
            int32_t acc = 0;
            for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                for (int ic8 = 0; ic8 < 8; ic8++) {
                    int in_idx = ic_g * (input_width * 8) + x * 8 + ic8;
                    int wt_idx = oc_g * wt_stride_oc +
                                 ic_g * wt_stride_ic + ic8 * 8 + oc8;
                    acc += (int32_t)input[in_idx] *
                           (int32_t)weights_and_bias[wt_idx];
                }
            }
            acc += bias[oc_g * 8 + oc8];

            float fval = (float)acc * scale_in;
            float sval = silu_float(fval);
            int32_t out_val = float_to_int_round(sval * scale_out);
            out_val = (out_val > 127)    ? 127
                      : (out_val < -128) ? -128
                                         : out_val;
            output[oc_g * (input_width * 8) + x * 8 + oc8] = (int8_t)out_val;
        }
    }
}

// ---------------------------------------------------------------------------
// Vectorized MAC + SiLU using MMUL int8 extraction + extern SiLU
//
// Uses two-extract int16 reconstruction (matching k3 split pattern).
// SiLU applied via extern apply_silu_i8 from silu_postproc_i8.o.
// Width chunking (MAX_VI=12) to avoid Peano pipelining bug.
// ---------------------------------------------------------------------------
static void conv2dk1_i8_silu_vector_row(
    int8_t *input, int8_t *weights_and_bias, int8_t *output,
    const int32_t input_width, const int32_t input_channels,
    const int32_t output_channels, const int32_t shift1,
    const int32_t shift2) {

    using MMUL = aie::mmul<8, 8, 8, int8, int8>;

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels);
    int8_t *kernels = weights_and_bias;

    const int iw = input_width;
    const int ic_iters = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int w_iters = iw / 8;

    int8_t *input_base = input;

    alignas(64) int8_t lo8_buf[MMUL::size_C];
    alignas(64) int8_t hi8_buf[MMUL::size_C];
    alignas(64) int8_t out_buf[MMUL::size_C];

    constexpr int MAX_VI = 12;
    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int wi_base = 0; wi_base < w_iters; wi_base += MAX_VI) {
            int wi_end = (wi_base + MAX_VI < w_iters) ? wi_base + MAX_VI : w_iters;
            for (int wi = wi_base; wi < wi_end; wi++) {
            // Fresh accumulator per iteration
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            // MAC over all IC groups
            mac_k1_all_ic(acc, input_base, kernels,
                          oc_g, wi, iw, ic_iters);

            // Two-extract with mode switching
            ::aie::set_saturation(aie::saturation_mode::none);
            ::aie::set_rounding(aie::rounding_mode::floor);
            aie::store_v(lo8_buf, acc.to_vector<int8>(shift1));
            aie::store_v(hi8_buf, acc.to_vector<int8>(shift1 + 8));
            ::aie::set_saturation(aie::saturation_mode::saturate);
            ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

            // Apply SiLU via extern (separate .o)
            apply_silu_i8(lo8_buf, hi8_buf, bias, oc_g, out_buf,
                          shift1, shift2);

            // Store 64 int8 output values
            int8_t *dst = output + oc_g * (iw * 8) + wi * MMUL::size_C;
            aie::store_v(dst, aie::load_v<MMUL::size_C>(out_buf));
            }
        }
        // Scalar tail for remaining width % 8 elements
        if (w_iters * 8 < iw) {
            scalar_tail_k1(input, weights_and_bias, output,
                           input_width, input_channels, output_channels,
                           oc_g, w_iters * 8, shift1, shift2);
        }
    }
}

// ---------------------------------------------------------------------------
// extern "C" wrapper — runtime dispatch based on width
// ---------------------------------------------------------------------------
extern "C" {

void conv2dk1_i8_silu(int8_t *input, int8_t *weights_and_bias, int8_t *output,
                      const int32_t input_width,
                      const int32_t input_channels,
                      const int32_t output_channels, const int32_t shift1,
                      const int32_t shift2) {
    event0();
    if (input_width >= 8) {
        conv2dk1_i8_silu_vector_row(input, weights_and_bias, output,
                                    input_width, input_channels,
                                    output_channels, shift1, shift2);
    } else {
        conv2dk1_i8_silu_scalar_row(input, weights_and_bias, output,
                                    input_width, input_channels,
                                    output_channels, shift1, shift2);
    }
    event1();
}

} // extern "C"
