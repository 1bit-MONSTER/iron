// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <type_traits>

// Nearest-neighbor 2x horizontal upsampling for one row.
//
// Input row layout:  [C/8, W, 8]   (channel_groups * input_width * 8 elements)
// Output row layout: [C/8, 2W, 8]  (channel_groups * 2*input_width * 8 elements)
//
// For each channel group and each input pixel, the 8-element channel vector
// is duplicated to two adjacent output positions (horizontal duplication).
void upsample2x_row_vectorized(bfloat16 *restrict input_row, bfloat16 *restrict output_row,
                                const int32_t input_width, const int32_t channels)
{
    event0();

    const int32_t channel_groups = channels >> 3; // channels / 8
    const int32_t output_width = input_width << 1; // input_width * 2

    for (int32_t cg = 0; cg < channel_groups; cg++) {
        // Pointers into the current channel group
        bfloat16 *in_cg = input_row + cg * input_width * 8;
        bfloat16 *out_cg = output_row + cg * output_width * 8;

        AIE_PREPARE_FOR_PIPELINING
        for (int32_t x = 0; x < input_width; x++) {
            // Load 8 bf16 values (one channel vector for pixel x)
            aie::vector<bfloat16, 8> val = aie::load_v<8>(in_cg + x * 8);

            // Store to output position 2*x and 2*x+1 (horizontal duplication)
            aie::store_v(out_cg + (2 * x) * 8, val);
            aie::store_v(out_cg + (2 * x + 1) * 8, val);
        }
    }

    event1();
}

extern "C" {

void upsample2x_row_bf16(bfloat16 *restrict input_row, bfloat16 *restrict output_row,
                          int32_t input_width, int32_t channels)
{
    upsample2x_row_vectorized(input_row, output_row, input_width, channels);
}

} // extern "C"
