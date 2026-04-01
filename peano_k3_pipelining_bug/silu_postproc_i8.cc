// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// SiLU post-processing in a SEPARATE compilation unit.
//
// Peano generates 100x worse code for this function when compiled alongside
// the k3 MAC code (510 µs/call vs 5 µs/call for the identical function in
// the k1 compilation unit). Isolating it into its own .o file should give
// Peano a simpler optimization context and match k1's performance.
//
// This file compiles to silu_postproc_i8.o, which is archived with the k3
// MAC .o into a .a for linking.

#define NOCPP

#include "../aie_kernels/aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

inline int32_t float_to_int_round(float x) {
    return (x >= 0.0f) ? (int32_t)(x + 0.5f) : (int32_t)(x - 0.5f);
}

// ---------------------------------------------------------------------------
// Vectorized SiLU post-processing: two-extract int16 reconstruction
//
// Takes two int8 buffers (lo8, hi8) from the MMUL accumulator extracted at
// shifts shift1 and shift1+8 with saturation=none, rounding=floor.
// Reconstructs int16 = hi8 * 256 + (uint8)lo8 to recover the full
// (acc >> shift1) value without int8 clipping. Then converts to bf16,
// adds pre-scaled bias, applies vec-16 SiLU via hardware tanh, requantizes.
//
// NOINLINE to prevent the caller from inlining and re-mixing with MMUL.
// ---------------------------------------------------------------------------
extern "C" __attribute__((noinline)) void apply_silu_i8(
    int8_t *__restrict lo8_buf,
    int8_t *__restrict hi8_buf,
    int32_t *__restrict bias, int32_t oc_g,
    int8_t *__restrict out_buf, int32_t shift1, int32_t shift2) {

    float dequant = 1.0f / (float)(1 << shift1);
    float scale_out = (float)shift2 / 256.0f;

    // Pre-compute bias in bf16 for all 8 channels, replicated for vec-16
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
        // Reconstruct int16 from two int8 extractions, convert to bf16
        for (int i = 0; i < 16; i++) {
            int16_t val16 = (int16_t)hi8_buf[g * 16 + i] * (int16_t)256 +
                            (int16_t)(uint8_t)lo8_buf[g * 16 + i];
            bf16_tmp[i] = (bfloat16)(float)val16;
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
}
