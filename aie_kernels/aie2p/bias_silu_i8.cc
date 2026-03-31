// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Standalone Bias + SiLU kernel for int8 dataflow pipelines (AIE2+).
//
// Designed to run on a separate core, chained after a non-fused conv kernel
// via ObjectFIFO: conv_core -> FIFO -> silu_core.
//
// Pipeline per element:
//   1. Dequantize: float val = (float)input_i8[i]
//   2. Add bias:  val += bias_float[channel]
//   3. SiLU via vec-16 aie::tanh<bfloat16>():
//      silu(x) = x * 0.5 * (1 + tanh(x/2))
//   4. Requantize: int8_out = clamp(round(silu * shift2/256.0), -128, 127)
//
// Data layout: [C/8, W, 8] — process 2 spatial positions (16 values)
// at a time using vec-16 aie::tanh<bfloat16>().
//
// Requires input_width >= 2 and even. The caller must guarantee this.

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

inline int32_t round_f2i(float x) {
    return (x >= 0.0f) ? (int32_t)(x + 0.5f) : (int32_t)(x - 0.5f);
}

extern "C" {

void bias_silu_i8(int8_t *__restrict input, int8_t *__restrict weights_bias,
                  int8_t *__restrict output, const int32_t input_width,
                  const int32_t channels, const int32_t shift1,
                  const int32_t shift2) {
    event0();

    int32_t *bias = (int32_t *)weights_bias;
    float dequant = 1.0f / (float)(1 << shift1);
    float scale_out = (float)shift2 / 256.0f;

    const int oc_groups = channels / 8;
    const int vec_iters = input_width / 2;

    // SiLU constants for vec-16
    aie::vector<bfloat16, 16> half_v =
        aie::broadcast<bfloat16, 16>((bfloat16)0.5f);
    aie::vector<bfloat16, 16> one_v =
        aie::broadcast<bfloat16, 16>((bfloat16)1.0f);

    alignas(64) bfloat16 bf16_buf[16];

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        // Precompute bias as bf16: [ch0..ch7, ch0..ch7]
        for (int ch = 0; ch < 8; ch++) {
            bfloat16 bv = (bfloat16)((float)bias[oc_g * 8 + ch] * dequant);
            bf16_buf[ch] = bv;
            bf16_buf[8 + ch] = bv;
        }
        aie::vector<bfloat16, 16> bias_v = aie::load_v<16>(bf16_buf);

        int8_t *__restrict in_base = input + oc_g * (input_width * 8);
        int8_t *__restrict out_base = output + oc_g * (input_width * 8);

        for (int vi = 0; vi < vec_iters; vi++) {
            int offset = vi * 16;

            // Int8 -> bf16 upconvert (16 elements)
            for (int j = 0; j < 16; j++) {
                bf16_buf[j] = (bfloat16)((float)in_base[offset + j]);
            }
            aie::vector<bfloat16, 16> x_bf16 = aie::load_v<16>(bf16_buf);

            // Add bias
            x_bf16 = aie::add(x_bf16, bias_v);

            // SiLU: x * 0.5 * (1 + tanh(x/2))
            auto half_x = aie::mul(x_bf16, half_v);
            auto tanh_hx = aie::tanh<bfloat16>(half_x.to_vector<float>());
            auto one_plus = aie::add(tanh_hx, one_v);
            aie::vector<bfloat16, 16> sigmoid =
                aie::mul(one_plus, half_v);
            auto silu_acc = aie::mul(x_bf16, sigmoid);
            aie::vector<bfloat16, 16> silu_bf16 =
                silu_acc.to_vector<bfloat16>();

            // Bf16 -> int8 requantize
            aie::store_v(bf16_buf, silu_bf16);
            for (int j = 0; j < 16; j++) {
                float sval = (float)bf16_buf[j];
                int32_t oval = round_f2i(sval * scale_out);
                oval = (oval > 127) ? 127 : (oval < -128) ? -128 : oval;
                out_base[offset + j] = (int8_t)oval;
            }
        }
    }

    event1();
}

} // extern "C"
