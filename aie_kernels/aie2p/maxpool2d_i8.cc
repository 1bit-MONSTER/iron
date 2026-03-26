// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// MaxPool2d kernel for int8 with kernel_size=5, stride=1, padding=2.
//
// Input is pre-padded in Python and arrives as a strip of 5 consecutive rows.
// Data layout (tiled, groups of 8 channels):
//   Input strip: [5, C/8, W_padded, 8] = 5 consecutive rows
//   Output row:  [C/8, W_out, 8]

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

// Process a strip of 5 input rows into 1 output row.
// The strip is contiguous: row k starts at strip + k * (channels * input_width).
void maxpool2d_5x5_strip_i8_impl(int8_t *__restrict strip,
                                  int8_t *__restrict output,
                                  const int32_t output_width,
                                  const int32_t channels,
                                  const int32_t input_width) {
    event0();

    const int cg = channels / 8;
    const int row_stride = channels * input_width; // elements per row

    for (int c = 0; c < cg; c++) {
        int in_cg_off = c * input_width * 8;
        int out_cg_off = c * output_width * 8;

        for (int x = 0; x < output_width; x++) {
            for (int c8 = 0; c8 < 8; c8++) {
                int8_t mx = -128; // INT8_MIN
                for (int ky = 0; ky < 5; ky++) {
                    int row_off = ky * row_stride;
                    for (int kx = 0; kx < 5; kx++) {
                        int8_t v = strip[row_off + in_cg_off + (x + kx) * 8 + c8];
                        if (v > mx)
                            mx = v;
                    }
                }
                output[out_cg_off + x * 8 + c8] = mx;
            }
        }
    }

    event1();
}

extern "C" {

void maxpool2d_5x5_i8_strip(int8_t *strip, int8_t *output,
                              const int32_t output_width,
                              const int32_t channels,
                              const int32_t input_width) {
    maxpool2d_5x5_strip_i8_impl(strip, output, output_width, channels,
                                 input_width);
}

} // extern "C"
