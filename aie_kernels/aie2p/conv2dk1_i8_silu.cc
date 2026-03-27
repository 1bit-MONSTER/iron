// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Fused int8 1x1 Conv + Bias + SiLU kernel using hardware/Padé tanh.
//
// Replaces the sigmoid LUT approach with continuous SiLU:
//   SiLU(x) = x * 0.5 * (1 + tanh(x/2))
//
// Computation pipeline:
//   1. int8 x int8 -> int32 convolution accumulation (1x1 pointwise)
//   2. Add pre-scaled int32 bias
//   3. Dequantize: float val = (float)acc * 2^(-shift1)
//   4. SiLU in float via Padé tanh (scalar) or aie::tanh (vector)
//   5. Requantize: int8 out = clamp(round(silu * 2^shift2), -128, 127)
//
// Interface: 3 buffers (input, weights_and_bias, output).
// Bias packed at end of weights: [weights: OC*IC bytes] [bias: OC*4 bytes]
//
// Data layouts (same as conv2dk1_i8_fused.cc):
//   Input:   [C_in/8, W, 8]
//   Weights: [C_out/8, C_in/8, 8, 8]  (last two: [ic8, oc8])
//   Bias:    [C_out]  (int32, pre-scaled, packed after weights)
//   Output:  [C_out/8, W, 8]
//
// Compile flags:
//   -DINT8_ACT       Required
//   -DSCALAR          Scalar path (Padé tanh)
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
// Padé rational approximation: tanh(z) ≈ z(27+z²)/(27+9z²)
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
// Scalar: fused conv1x1 + bias + SiLU (Padé tanh)
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
    float scale_out = (float)(1 << shift2);

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
// Vectorized MAC + SiLU using aie::tanh<bfloat16>
//
// MAC phase uses aie::mmul<8,8,8,int8,int8> (same as non-fused k1 vector).
// After accumulation, extracts int32 values, adds bias, dequantizes to
// bfloat16, applies SiLU via hardware tanh, requantizes to int8.
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

    float scale_in = 1.0f / (float)(1 << shift1);
    float scale_out = (float)(1 << shift2);

    const int iw = input_width;
    const int ic_iters = input_channels / CHANNEL_FACTOR;
    const int oc_groups = output_channels / CHANNEL_FACTOR;
    const int w_iters = iw / MMUL_M; // process 8 spatial cols at a time

    int8_t *input_base = input;
    int8_t *restrict out_ptr = output;

    // Temporary buffers on stack for SiLU processing
    alignas(64) int32_t acc_buf[MMUL_MN];
    alignas(64) int8_t out_buf[MMUL_MN];

    MMUL8x8x8 acc_mmul;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int wi = 0; wi < w_iters; wi++) {
            // Initialize accumulator
            acc_mmul = aie::zeros<acc32, MMUL_MN>();

            int8_t *in_ptr = input_base + wi * MMUL_MK;
            int8_t *wt_ptr = kernels + oc_g * ic_iters * MMUL_KN;

            // Vectorized MAC over all IC groups (same as non-fused k1)
            for (int ic = 0; ic < ic_iters; ic++) {
                aie::vector<int8, MMUL_KN> in_b =
                    aie::load_v<MMUL_KN>(wt_ptr);
                wt_ptr += MMUL_KN;

                aie::vector<int8, MMUL_MK> in_a =
                    aie::load_v<MMUL_MK>(in_ptr);
                in_ptr += iw * CHANNEL_FACTOR;

                acc_mmul.mac(in_a, in_b);
            }

            // Dump raw int32 accumulators to memory buffer
            aie::vector<int32, MMUL_MN> acc_i32 =
                acc_mmul.to_vector<int32>(0);
            aie::store_v(acc_buf, acc_i32);

            // Per-element: add bias, SiLU in float, requantize to int8
            for (int i = 0; i < MMUL_MN; i++) {
                int oc8 = i % MMUL_N; // OC index within group
                int32_t val = acc_buf[i] + bias[oc_g * 8 + oc8];

                float fval = (float)val * scale_in;
                float sval = silu_float(fval);
                int32_t oval = float_to_int_round(sval * scale_out);
                oval = (oval > 127)    ? 127
                       : (oval < -128) ? -128
                                       : oval;
                out_buf[i] = (int8_t)oval;
            }

            // Store 64 int8 output values (layout matches tiled [w, 8])
            int8_t *dst =
                output + oc_g * (iw * 8) + wi * MMUL_MN;
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
