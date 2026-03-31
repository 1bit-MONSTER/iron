// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Simple int8 passthrough (memcpy) kernel for AIE2+.
//
// Copies `size` bytes from input to output using vectorized loads/stores.
// Used as a data routing helper in dataflow designs where data must
// pass through a compute tile to reach its destination.
//
// Compile flags:
//   -DINT8_ACT    Required

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

#ifdef INT8_ACT

extern "C" {

void passthrough_i8(int8_t *__restrict input, int8_t *__restrict output,
                    const int32_t size) {
    const int vec_iters = size / 64;
    const int vec_done = vec_iters * 64;

    for (int i = 0; i < vec_iters; i++) {
        aie::vector<int8, 64> v = aie::load_v<64>(input + i * 64);
        aie::store_v(output + i * 64, v);
    }

    // Scalar remainder
    for (int i = vec_done; i < size; i++) {
        output[i] = input[i];
    }
}

} // extern "C"

#endif // INT8_ACT
