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
    constexpr int VEC_SIZE = 64;

    // Process VEC_SIZE elements at a time
    const int n_vecs = row_size / VEC_SIZE;

    for (int i = 0; i < n_vecs; i++) {
        aie::vector<int8, VEC_SIZE> va = aie::load_v<VEC_SIZE>(a);
        aie::vector<int8, VEC_SIZE> vb = aie::load_v<VEC_SIZE>(b);

        // add_sat performs saturating addition
        aie::vector<int8, VEC_SIZE> vout = aie::add_sat(va, vb);

        aie::store_v(out, vout);

        a += VEC_SIZE;
        b += VEC_SIZE;
        out += VEC_SIZE;
    }

    // Handle remainder (should not happen if row_size is multiple of 64,
    // which it will be for our tiled layout with channels multiple of 8
    // and widths multiple of 8)
    int rem = row_size - n_vecs * VEC_SIZE;
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
