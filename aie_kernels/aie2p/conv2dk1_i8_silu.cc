// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Fused int8 1x1 Conv + Bias + SiLU kernel using hardware tanh (AIE2+).
//
// Vectorized path (width%8==0, IC >= 8):
//   MMUL MAC for convolution, extract via to_vector<int8>(shift1) which
//   uses the srs_to_v64int8 hardware intrinsic for correct accumulator
//   depermutation, upconvert to bf16, add pre-scaled bias in bf16 domain,
//   apply vec-16 SiLU using hardware aie::tanh<bfloat16>(), requantize.
//
// SiLU(x) = x * sigmoid(x) = x * 0.5 * (1 + tanh(x/2))
//
// Interface: 3 buffers (input, weights_and_bias, output).
// Bias packed at end of weights: [weights: OC*IC bytes] [bias: OC*4 bytes]
//
// Data layouts:
//   Input:   [C_in/8, W, 8]
//   Weights: [C_out/8, C_in/8, 8, 8]  (last two: [ic8, oc8])
//   Bias:    [C_out]  (int32, pre-scaled, packed after weights)
//   Output:  [C_out/8, W, 8]
//
// Compile flags:
//   -DINT8_ACT       Required
//   -DSCALAR          Scalar path (Pade tanh)
//   (no -DSCALAR)    Vector path (MMUL MAC + aie::tanh<bfloat16>)

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define REL_WRITE 0
#define REL_READ 1

#ifdef INT8_ACT

// ---------------------------------------------------------------------------
// Pade rational approximation: tanh(z) ~ z(27+z^2)/(27+9z^2)
// Accurate to ~1e-4 for |z| < 4.5, clamps for |z| > ~4.5.
// ---------------------------------------------------------------------------
inline float pade_tanh(float z) {
    float z2 = z * z;
    if (z2 > 20.0f)
        return (z > 0.0f) ? 1.0f : -1.0f;
    return z * (27.0f + z2) / (27.0f + 9.0f * z2);
}

// ---------------------------------------------------------------------------
// SiLU(x) = x * sigmoid(x) = x * 0.5 * (1 + tanh(x/2))
// ---------------------------------------------------------------------------
inline float silu_float(float x) {
    float tanh_hx = pade_tanh(x * 0.5f);
    return x * 0.5f * (1.0f + tanh_hx);
}

// ---------------------------------------------------------------------------
// Round-to-nearest-even helper (AIE backend lacks __builtin_roundf).
// ---------------------------------------------------------------------------
inline int32_t float_to_int_round(float x) {
    return (x >= 0.0f) ? (int32_t)(x + 0.5f) : (int32_t)(x - 0.5f);
}

#ifdef SCALAR

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

                // Phase 1: 1x1 Convolution (int8 x int8 -> int32)
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

                // Phase 2: Add pre-scaled bias
                acc += bias[oc_g * 8 + oc8];

                // Phase 3: Dequant -> SiLU -> Requant
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

#else // Vector

// ---------------------------------------------------------------------------
// Vectorized SiLU post-processing using hardware aie::tanh<bfloat16>
//
// Processes 64 int8 values (one MMUL tile = 8 spatial x 8 channels):
//   1. int8 conv result (from SRS, correct depermutation) in conv_buf
//   2. Convert groups of 16 to bf16, add pre-scaled bias, apply SiLU
//   3. Requantize back to int8
//
// This function is marked noinline to prevent the Peano compiler from
// mixing MMUL register allocation with float SiLU operations.
// ---------------------------------------------------------------------------
__attribute__((noinline)) static void apply_silu_vec16_k1(
    int8_t *__restrict conv_buf,
    int32_t *__restrict bias, int32_t oc_g,
    int8_t *__restrict out_buf, int32_t shift1, int32_t shift2) {

    // Reset saturation/rounding modes for float SiLU computation.
    ::aie::set_saturation(aie::saturation_mode::none);
    ::aie::set_rounding(aie::rounding_mode::floor);

    float dequant = 1.0f / (float)(1 << shift1);
    float scale_out = (float)shift2 / 256.0f;

    // Pre-compute bias in bf16, replicated for vec-16
    alignas(64) bfloat16 bias_bf16[16];
    for (int ch = 0; ch < 8; ch++) {
        bfloat16 bv = (bfloat16)((float)bias[oc_g * 8 + ch] * dequant);
        bias_bf16[ch] = bv;
        bias_bf16[8 + ch] = bv;
    }

    // SiLU constants
    aie::vector<bfloat16, 16> half_v =
        aie::broadcast<bfloat16, 16>((bfloat16)0.5f);
    aie::vector<bfloat16, 16> one_v =
        aie::broadcast<bfloat16, 16>((bfloat16)1.0f);
    aie::vector<bfloat16, 16> scale_v =
        aie::broadcast<bfloat16, 16>((bfloat16)scale_out);
    aie::vector<bfloat16, 16> bias_v = aie::load_v<16>(bias_bf16);

    alignas(64) bfloat16 bf16_tmp[16];

    for (int g = 0; g < 4; g++) {
        // Convert 16 int8 values to bf16
        for (int i = 0; i < 16; i++) {
            bf16_tmp[i] = (bfloat16)(float)conv_buf[g * 16 + i];
        }

        // Load as vec-16, add bias, apply SiLU
        aie::vector<bfloat16, 16> x_bf16 = aie::load_v<16>(bf16_tmp);
        x_bf16 = aie::add(x_bf16, bias_v);

        // SiLU(x) = x * 0.5 * (1 + tanh(x/2))
        auto half_x = aie::mul(x_bf16, half_v);
        aie::vector<bfloat16, 16> tanh_hx =
            aie::tanh<bfloat16>(half_x.to_vector<float>());
        aie::vector<bfloat16, 16> one_plus_tanh = aie::add(tanh_hx, one_v);
        aie::vector<bfloat16, 16> sigmoid =
            aie::mul(one_plus_tanh, half_v).to_vector<bfloat16>();
        aie::vector<bfloat16, 16> silu =
            aie::mul(x_bf16, sigmoid).to_vector<bfloat16>();

        // Requantize: silu * scale_out -> int8
        aie::vector<bfloat16, 16> scaled =
            aie::mul(silu, scale_v).to_vector<bfloat16>();
        aie::store_v(bf16_tmp, scaled);

        for (int i = 0; i < 16; i++) {
            float sval = (float)bf16_tmp[i];
            int32_t oval = float_to_int_round(sval);
            oval = (oval > 127) ? 127 : (oval < -128) ? -128 : oval;
            out_buf[g * 16 + i] = (int8_t)oval;
        }
    }

    // Restore modes for the next MMUL iteration
    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);
}

// ---------------------------------------------------------------------------
// Vectorized MAC + SiLU using MMUL int8 extraction + vec-16 hardware tanh
//
// MAC phase uses aie::mmul<8,8,8,int8,int8>.
// After accumulation, extracts int8 via SRS (correct depermutation),
// converts to bf16, adds bias, applies SiLU via hardware tanh, requantizes.
// ---------------------------------------------------------------------------
static void conv2dk1_i8_silu_vector_row(
    int8_t *input, int8_t *weights_and_bias, int8_t *output,
    const int32_t input_width, const int32_t input_channels,
    const int32_t output_channels, const int32_t shift1,
    const int32_t shift2) {

    constexpr int MMUL_M = 8;
    constexpr int MMUL_K = 8;
    constexpr int MMUL_N = 8;
    constexpr int CHANNEL_FACTOR = MMUL_K;
    constexpr int MMUL_MK = MMUL_M * MMUL_K;
    constexpr int MMUL_KN = MMUL_K * MMUL_N;
    constexpr int MMUL_MN = MMUL_M * MMUL_N;

    using MMUL8x8x8 = aie::mmul<MMUL_M, MMUL_K, MMUL_N, int8, int8>;
    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels);
    int8_t *kernels = weights_and_bias;

    const int iw = input_width;
    const int ic_iters = input_channels / CHANNEL_FACTOR;
    const int oc_groups = output_channels / CHANNEL_FACTOR;
    const int w_iters = iw / MMUL_M; // process 8 spatial cols at a time

    int8_t *input_base = input;

    // Temporary buffers on stack for SiLU processing
    alignas(64) int8_t conv_buf[MMUL_MN];
    alignas(64) int8_t out_buf[MMUL_MN];

    MMUL8x8x8 acc_mmul;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int wi = 0; wi < w_iters; wi++) {
            // Initialize accumulator
            acc_mmul = aie::zeros<acc32, MMUL_MN>();

            int8_t *in_ptr = input_base + wi * MMUL_MK;
            int8_t *wt_ptr = kernels + oc_g * ic_iters * MMUL_KN;

            // Vectorized MAC over all IC groups
            for (int ic = 0; ic < ic_iters; ic++) {
                aie::vector<int8, MMUL_KN> in_b =
                    aie::load_v<MMUL_KN>(wt_ptr);
                wt_ptr += MMUL_KN;

                aie::vector<int8, MMUL_MK> in_a =
                    aie::load_v<MMUL_MK>(in_ptr);
                in_ptr += iw * CHANNEL_FACTOR;

                acc_mmul.mac(in_a, in_b);
            }

            // Extract as int8 via SRS (correct depermutation)
            aie::store_v(conv_buf, acc_mmul.to_vector<int8>(shift1));

            // Apply vectorized SiLU (noinline, resets/restores modes)
            apply_silu_vec16_k1(conv_buf, bias, oc_g, out_buf, shift1, shift2);

            // Store 64 int8 output values
            int8_t *dst = output + oc_g * (iw * 8) + wi * MMUL_MN;
            aie::store_v(dst, aie::load_v<MMUL_MN>(out_buf));
        }
    }
}

#endif // SCALAR

// ---------------------------------------------------------------------------
// extern "C" wrapper
// ---------------------------------------------------------------------------
extern "C" {

void conv2dk1_i8_silu(int8_t *input, int8_t *weights_and_bias, int8_t *output,
                      const int32_t input_width,
                      const int32_t input_channels,
                      const int32_t output_channels, const int32_t shift1,
                      const int32_t shift2) {
    event0();
#ifdef SCALAR
    conv2dk1_i8_silu_scalar_row(input, weights_and_bias, output, input_width,
                                input_channels, output_channels, shift1,
                                shift2);
#else
    conv2dk1_i8_silu_vector_row(input, weights_and_bias, output, input_width,
                                input_channels, output_channels, shift1,
                                shift2);
#endif
    event1();
}

} // extern "C"

#endif // INT8_ACT
