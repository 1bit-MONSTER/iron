// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// MaxPool2d kernel for int8 with kernel_size=5, stride=1, padding=2.
//
// Input is pre-padded in Python and arrives as a strip of 5 consecutive rows.
// Data layout (tiled, groups of 8 channels):
//   Input strip: [5, C/8, W_padded, 8] = 5 consecutive rows
//   Output row:  [C/8, W_out, 8]
//
// Semi-vectorized: processes 2 output pixels at a time with the 8-channel
// max loop iterating over 16 contiguous bytes (matching int8 vector width).
// This enables compiler auto-vectorization of the inner max reduction.
// Falls back to 1-pixel scalar for odd output_width tail.

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>

void maxpool2d_5x5_strip_i8_impl(int8_t *__restrict strip,
                                  int8_t *__restrict output,
                                  const int32_t output_width,
                                  const int32_t channels,
                                  const int32_t input_width) {
    event0();

    const int cg = channels / 8;
    const int row_stride = channels * input_width;
    const int paired_width = output_width & ~1;

    for (int c = 0; c < cg; c++) {
        int in_cg_off = c * input_width * 8;
        int out_cg_off = c * output_width * 8;

        // Process 2 output pixels at a time (16 bytes = vector width)
        for (int x = 0; x < paired_width; x += 2) {
            int8_t mx[16];
            for (int i = 0; i < 16; i++)
                mx[i] = -128;

            for (int ky = 0; ky < 5; ky++) {
                int base = ky * row_stride + in_cg_off;
                for (int kx = 0; kx < 5; kx++) {
                    int8_t *p = strip + base + (x + kx) * 8;
                    for (int i = 0; i < 16; i++) {
                        if (p[i] > mx[i])
                            mx[i] = p[i];
                    }
                }
            }

            int8_t *out = output + out_cg_off + x * 8;
            for (int i = 0; i < 16; i++)
                out[i] = mx[i];
        }

        // Handle last pixel if output_width is odd
        if (paired_width < output_width) {
            int x = paired_width;
            int8_t mx[8];
            for (int i = 0; i < 8; i++)
                mx[i] = -128;

            for (int ky = 0; ky < 5; ky++) {
                int base = ky * row_stride + in_cg_off;
                for (int kx = 0; kx < 5; kx++) {
                    int8_t *p = strip + base + (x + kx) * 8;
                    for (int i = 0; i < 8; i++) {
                        if (p[i] > mx[i])
                            mx[i] = p[i];
                    }
                }
            }

            int8_t *out = output + out_cg_off + x * 8;
            for (int i = 0; i < 8; i++)
                out[i] = mx[i];
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
