// Licensed under the Apache License, Version 2.0 (the License); you may
// not use this file except in compliance with the License.
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an AS IS BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//

// SPDX-FileCopyrightText:	Copyright (c) 2025, Advanced Micro Devices, Inc. All rights reserved.
//
// SPDX-License-Identifier: Apache-2.0

#include <aie_api/aie.hpp>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

template <typename T, int N>
void rope_kernel(const T *restrict input, const T *restrict lut, T *restrict output, int32_t dims)
{
    event0();

    for (int v = 0; v < dims; v += N) {
        ::aie::vector<T, N> x = ::aie::load_v<N>(input + v);
        ::aie::vector<T, N> cache = ::aie::load_v<N>(lut + v);

        // Extract even and odd elements
        ::aie::vector<T, N / 2> x_even = ::aie::filter_even(x, 1);
        ::aie::vector<T, N / 2> x_odd = ::aie::filter_odd(x, 1);
        ::aie::vector<T, N / 2> cos_val = ::aie::filter_even(cache, 1);
        ::aie::vector<T, N / 2> sin_val = ::aie::filter_odd(cache, 1);

        // Perform ROPE calculations
        ::aie::vector<T, N / 2> even_cos = ::aie::mul(x_even, cos_val);
        ::aie::vector<T, N / 2> even_sin = ::aie::mul(x_even, sin_val);
        ::aie::vector<T, N / 2> odd_cos = ::aie::mul(x_odd, cos_val);
        ::aie::vector<T, N / 2> odd_sin = ::aie::mul(x_odd, sin_val);

        ::aie::vector<T, N / 2> output_even = ::aie::sub(even_cos, odd_sin);
        ::aie::vector<T, N / 2> output_odd = ::aie::add(even_sin, odd_cos);

        auto [low, high] = ::aie::interleave_zip(output_even, output_odd, 1);
        ::aie::vector<T, N> y = ::aie::concat(low, high);
        ::aie::store_v(output + v, y);
    }
    event1();
}

extern "C" {
void rope(bfloat16 *input, bfloat16 *lut, bfloat16 *output, int32_t dims)
{
    rope_kernel<bfloat16, 16>(input, lut, output, dims);
}
}