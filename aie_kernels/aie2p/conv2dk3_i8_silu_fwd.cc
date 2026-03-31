// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Combined kernel: conv2dk3 fused SiLU + passthrough for C2f half2 forwarding.
//
// Includes the full conv2dk3_i8_silu implementation plus a simple passthrough
// function, compiled into a single .o so one Worker can call both.
// MLIR-AIE requires one .o per Worker — this file satisfies that constraint
// for Core B in the C2f design, which does k3 conv AND half2 row forwarding.

#include "conv2dk3_i8_silu.cc"

// Passthrough function for half2 row relay.
// Copies `size` bytes from input to output using vectorized loads/stores.
extern "C" {

void passthrough_i8_fwd(int8_t *__restrict input, int8_t *__restrict output,
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
