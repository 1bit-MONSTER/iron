// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Elementwise int8 addition with saturation for residual connections.
//
// Computes: output[i] = saturate_int8(a[i] + b[i])
//
// Data layout: flat int8 arrays, size = channels * width (one row).
// Both inputs and output share the same layout (tiled [C/8, W, 8]).

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

#ifdef SCALAR

static void add_i8_scalar_row(int8_t *a, int8_t *b, int8_t *out,
                               const int32_t row_size) {
    for (int i = 0; i < row_size; i++) {
        int32_t sum = (int32_t)a[i] + (int32_t)b[i];
        if (sum > 127)
            sum = 127;
        if (sum < -128)
            sum = -128;
        out[i] = (int8_t)sum;
    }
}

#else // Vector

static void add_i8_vector_row(int8_t *restrict a, int8_t *restrict b,
                               int8_t *restrict out, const int32_t row_size) {
    // Process 32 int8 elements at a time: promote to int16 (fits 512-bit reg),
    // add, clamp to [-128,127], pack back to int8.
    constexpr int VEC8 = 32;

    const int n_vecs = row_size / VEC8;

    for (int i = 0; i < n_vecs; i++) {
        aie::vector<int8, VEC8> va = aie::load_v<VEC8>(a);
        aie::vector<int8, VEC8> vb = aie::load_v<VEC8>(b);

        aie::vector<int16, VEC8> va16 = aie::unpack(va);
        aie::vector<int16, VEC8> vb16 = aie::unpack(vb);
        aie::vector<int16, VEC8> sum16 = aie::add(va16, vb16);
        sum16 = aie::max(sum16, (int16)-128);
        sum16 = aie::min(sum16, (int16)127);
        aie::vector<int8, VEC8> vout = aie::pack(sum16);

        aie::store_v(out, vout);

        a += VEC8;
        b += VEC8;
        out += VEC8;
    }

    // Scalar remainder
    int rem = row_size - n_vecs * VEC8;
    for (int i = 0; i < rem; i++) {
        int32_t sum = (int32_t)a[i] + (int32_t)b[i];
        if (sum > 127)
            sum = 127;
        if (sum < -128)
            sum = -128;
        out[i] = (int8_t)sum;
    }
}

#endif // SCALAR

extern "C" {

void add_i8(int8_t *a, int8_t *b, int8_t *out, const int32_t row_size) {
    event0();
#ifdef SCALAR
    add_i8_scalar_row(a, b, out, row_size);
#else
    add_i8_vector_row(a, b, out, row_size);
#endif
    event1();
}

} // extern "C"
