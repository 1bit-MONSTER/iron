// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Element-wise int8 addition with saturation (AIE2+).
//
// Adds two int8 vectors element-by-element with saturation to [-128, 127].
// Vectorized using aie::add() with saturation mode enabled.
//
// Data layout: flat [size] array of int8 values.
// Both inputs and output must have the same layout and size.
//
// Compile flags:
//   -DINT8_ACT    Required

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

#ifdef INT8_ACT

extern "C" {

void elem_add_i8(int8_t *__restrict a, int8_t *__restrict b,
                 int8_t *__restrict out, const int32_t size) {

    ::aie::set_saturation(aie::saturation_mode::saturate);

    // Process 64 elements at a time using vec-64 int8 operations
    const int vec_iters = size / 64;
    const int vec_done = vec_iters * 64;

    for (int i = 0; i < vec_iters; i++) {
        aie::vector<int8, 64> va = aie::load_v<64>(a + i * 64);
        aie::vector<int8, 64> vb = aie::load_v<64>(b + i * 64);
        // aie::add_sat returns saturated sum
        aie::vector<int8, 64> vout = aie::add(va, vb);
        aie::store_v(out + i * 64, vout);
    }

    // Scalar remainder
    for (int i = vec_done; i < size; i++) {
        int32_t sum = (int32_t)a[i] + (int32_t)b[i];
        sum = (sum > 127) ? 127 : (sum < -128) ? -128 : sum;
        out[i] = (int8_t)sum;
    }

    ::aie::set_saturation(aie::saturation_mode::none);
}

} // extern "C"

#endif // INT8_ACT
