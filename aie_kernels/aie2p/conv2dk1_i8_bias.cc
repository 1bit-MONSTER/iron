// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Bare 1x1 int8 convolution + int32 bias, no activation.
//
// Used for YOLOv8n detection head cv3 layers which output raw logits
// (no SiLU). Same weight layout as conv2dk1_i8_silu: weights packed
// followed by int32 bias. Same MMUL MAC phase, but output is just
// round((acc + bias) / 2^shift) clamped to int8.
//
// Interface: (input, weights_and_bias, output, width, IC, OC, shift)

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

#ifdef SCALAR

// ---------------------------------------------------------------------------
// Scalar: conv1x1 + bias, no activation
// ---------------------------------------------------------------------------
static void conv2dk1_i8_bias_scalar_row(
    int8_t *input, int8_t *weights_and_bias, int8_t *output,
    const int32_t input_width, const int32_t input_channels,
    const int32_t output_channels, const int32_t shift) {

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int wt_stride_ic = 64; // 8 * 8
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels);

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

                // Add pre-scaled bias
                acc += bias[oc_g * 8 + oc8];

                // Shift-round-saturate to int8 (no SiLU)
                int32_t half = (shift > 0) ? (1 << (shift - 1)) : 0;
                int32_t out_val = (acc + half) >> shift;
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
// MAC helper (same as SiLU kernel's mac_k1_all_ic)
// ---------------------------------------------------------------------------
inline void mac_k1_bias_all_ic(
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
// Apply bias + requant (NO SiLU). Uses the same two-extract int16
// reconstruction as the SiLU kernel to avoid int8 clipping before bias,
// then adds bias in bf16 domain and requantizes.
// ---------------------------------------------------------------------------
__attribute__((noinline)) static void apply_bias_vec16_k1(
    int8_t *__restrict lo8_buf,
    int8_t *__restrict hi8_buf,
    int32_t *__restrict bias, int32_t oc_g,
    int8_t *__restrict out_buf, int32_t shift1, int32_t shift2) {

    float dequant = 1.0f / (float)(1 << shift1);
    float scale_out = (float)shift2 / 256.0f;

    // Pre-compute bias in bf16, replicated for vec-16
    alignas(64) bfloat16 bias_bf16[16];
    for (int i = 0; i < 8; i++) {
        bfloat16 bv = (bfloat16)(float)bias[oc_g * 8 + i];
        bias_bf16[i] = bv;
        bias_bf16[i + 8] = bv;
    }
    aie::vector<bfloat16, 16> bias_vec = aie::load_v<16>(bias_bf16);

    // Process 64 elements in 4 groups of 16
    for (int g = 0; g < 4; g++) {
        // Reconstruct int16 from two int8 extracts
        aie::vector<int8, 16> lo =
            aie::load_v<16>(lo8_buf + g * 16);
        aie::vector<int8, 16> hi =
            aie::load_v<16>(hi8_buf + g * 16);

        // Cast to int16 and reconstruct: val = hi*256 + (uint8)lo
        aie::vector<int16, 16> lo16 = aie::unpack(lo);
        aie::vector<int16, 16> hi16 = aie::unpack(hi);
        lo16 = aie::bit_and(lo16, aie::broadcast<int16, 16>(0x00FF));
        aie::vector<int16, 16> val16 =
            aie::add(aie::mul<int16>(hi16, 256).to_vector<int16>(0), lo16);

        // Convert to bf16, multiply by dequant, add bias
        aie::vector<bfloat16, 16> fval =
            aie::to_float<bfloat16>(val16, 0);
        fval = aie::mul(fval, (bfloat16)dequant);
        fval = aie::add(fval, bias_vec);

        // Requant to int8: round(fval * scale_out), NO SiLU
        fval = aie::mul(fval, (bfloat16)scale_out);
        aie::vector<int16, 16> ival =
            aie::to_fixed<int16>(fval, 0);
        aie::vector<int8, 16> result =
            aie::pack(ival);

        aie::store_v(out_buf + g * 16, result);
    }
}

// ---------------------------------------------------------------------------
// Vectorized: MMUL + bias, no SiLU
// ---------------------------------------------------------------------------
static void conv2dk1_i8_bias_vector_row(
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

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int wi = 0; wi < w_iters; wi++) {
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            mac_k1_bias_all_ic(acc, input_base, kernels,
                               oc_g, wi, iw, ic_iters);

            // Two-extract with mode switching
            ::aie::set_saturation(aie::saturation_mode::none);
            ::aie::set_rounding(aie::rounding_mode::floor);
            aie::store_v(lo8_buf, acc.to_vector<int8>(shift1));
            aie::store_v(hi8_buf, acc.to_vector<int8>(shift1 + 8));
            ::aie::set_saturation(aie::saturation_mode::saturate);
            ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

            // Apply bias + requant (NO SiLU)
            apply_bias_vec16_k1(lo8_buf, hi8_buf, bias, oc_g, out_buf,
                                shift1, shift2);

            int8_t *dst = output + oc_g * (iw * 8) + wi * MMUL::size_C;
            aie::store_v(dst, aie::load_v<MMUL::size_C>(out_buf));
        }
    }
}

#endif // SCALAR

// ---------------------------------------------------------------------------
// extern "C" wrapper
// ---------------------------------------------------------------------------
extern "C" {

void conv2dk1_i8_bias(int8_t *input, int8_t *weights_and_bias,
                      int8_t *output, const int32_t input_width,
                      const int32_t input_channels,
                      const int32_t output_channels,
                      const int32_t shift1, const int32_t shift2) {
    event0();
#ifdef SCALAR
    conv2dk1_i8_bias_scalar_row(input, weights_and_bias, output, input_width,
                                input_channels, output_channels, shift1);
#else
    conv2dk1_i8_bias_vector_row(input, weights_and_bias, output, input_width,
                                input_channels, output_channels, shift1,
                                shift2);
#endif
    event1();
}

} // extern "C"
