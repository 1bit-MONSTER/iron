// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Nearest-neighbor 2x horizontal upsampling for one row (int8).
//
// Input row layout:  [C/8, W, 8]   (channel_groups * input_width * 8 elements)
// Output row layout: [C/8, 2W, 8]  (channel_groups * 2*input_width * 8 elements)
//
// For each channel group and each input pixel, the 8-element channel vector
// is duplicated to two adjacent output positions (horizontal duplication).

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

void upsample2x_row_i8_impl(int8_t *__restrict input_row,
                              int8_t *__restrict output_row,
                              const int32_t input_width,
                              const int32_t channels) {
    event0();

    const int32_t channel_groups = channels >> 3; // channels / 8
    const int32_t output_width = input_width << 1; // input_width * 2

    for (int32_t cg = 0; cg < channel_groups; cg++) {
        int32_t in_cg_off = cg * input_width * 8;
        int32_t out_cg_off = cg * output_width * 8;

        for (int32_t x = 0; x < input_width; x++) {
            for (int32_t c8 = 0; c8 < 8; c8++) {
                int8_t val = input_row[in_cg_off + x * 8 + c8];
                // Duplicate to output positions 2*x and 2*x+1
                output_row[out_cg_off + (2 * x) * 8 + c8] = val;
                output_row[out_cg_off + (2 * x + 1) * 8 + c8] = val;
            }
        }
    }

    event1();
}

extern "C" {

void upsample2x_row_i8(int8_t *input_row, int8_t *output_row,
                         int32_t input_width, int32_t channels) {
    upsample2x_row_i8_impl(input_row, output_row, input_width, channels);
}

} // extern "C"
