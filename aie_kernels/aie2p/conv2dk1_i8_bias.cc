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
// Vectorized: MMUL + bias, no SiLU
//
// Extracts accumulator as int32 (not int8 via to_vector<int8>(shift))
// to avoid a Peano SRS codegen bug where to_vector<int8>(shift1) and
// to_vector<int8>(shift1+8) produce incorrect results when the outer
// loop trip count (w_iters) >= 10.  The int32 extraction + scalar
// post-processing is slower but correct at all widths.
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

    alignas(64) int8_t out_buf[MMUL::size_C];

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int wi = 0; wi < w_iters; wi++) {
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();
            mac_k1_bias_all_ic(acc, input_base, kernels,
                               oc_g, wi, iw, ic_iters);

            // Extract to int32 (avoids Peano SRS bug with int8 extraction)
            alignas(64) int32_t acc_i32[MMUL::size_C];
            aie::store_v(acc_i32, acc.to_vector<int32>(0));

            // Scalar bias + requant
            float dequant = 1.0f / (float)(1 << shift1);
            float scale_out = (float)shift2 / 256.0f;
            for (int i = 0; i < MMUL::size_C; i++) {
                float fval = (float)acc_i32[i] * dequant;
                fval += (float)bias[oc_g * 8 + (i % 8)];
                fval *= scale_out;
                int32_t oval = (fval >= 0.0f) ? (int32_t)(fval + 0.5f)
                                              : (int32_t)(fval - 0.5f);
                oval = (oval > 127) ? 127 : (oval < -128) ? -128 : oval;
                out_buf[i] = (int8_t)oval;
            }

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
