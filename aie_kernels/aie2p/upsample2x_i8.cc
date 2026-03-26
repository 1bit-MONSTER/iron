// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Nearest-neighbor 2x horizontal upsampling for one row (int8).
//
// Input row layout:  [C/8, W, 8]   (channel_groups * input_width * 8 elements)
// Output row layout: [C/8, 2W, 8]  (channel_groups * 2*input_width * 8 elements)
//
// Vectorized: loads 2 input pixels (16 int8 elements) at a time and uses
// interleave_zip with chunk_size=8 to duplicate each pixel's 8 channels,
// producing 2 x 16-element output vectors (4 output pixel slots total).

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
    // Number of input pixels we can process in pairs
    const int32_t paired_width = input_width & ~1;

    for (int32_t cg = 0; cg < channel_groups; cg++) {
        int8_t *in_cg = input_row + cg * input_width * 8;
        int8_t *out_cg = output_row + cg * output_width * 8;

        // Process 2 input pixels at a time.
        // Load 16 elements: [px_a ch0-7, px_b ch0-7]
        // interleave_zip(v, v, 8) produces:
        //   lo = [px_a ch0-7, px_a ch0-7] (pixel a duplicated)
        //   hi = [px_b ch0-7, px_b ch0-7] (pixel b duplicated)
        AIE_PREPARE_FOR_PIPELINING
        for (int32_t x = 0; x < paired_width; x += 2) {
            aie::vector<int8, 16> v = aie::load_v<16>(in_cg + x * 8);
            auto [lo, hi] = aie::interleave_zip(v, v, 8);
            aie::store_v(out_cg + (2 * x) * 8, lo);
            aie::store_v(out_cg + (2 * x + 2) * 8, hi);
        }

        // Handle last pixel if input_width is odd
        if (paired_width < input_width) {
            int32_t x = paired_width;
            for (int32_t c8 = 0; c8 < 8; c8++) {
                int8_t val = in_cg[x * 8 + c8];
                out_cg[(2 * x) * 8 + c8] = val;
                out_cg[(2 * x + 1) * 8 + c8] = val;
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
