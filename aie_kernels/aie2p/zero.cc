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

#ifndef ZERO_CC
#define ZERO_CC

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <type_traits>

template <typename T, int M, int N> void zero_scalar(T *__restrict c)
{
    for (int i = 0; i < M * N; i++) {
        c[i] = 0;
    }
}

template <typename T, int M, int N> void zero_vectorized(T *__restrict c)
{
    constexpr int r = 512 / (sizeof(T) * 8); // 512 bit store units for AIE2P
    static_assert((M * N) % r == 0);
    const aie::vector<T, r> zeros = aie::zeros<T, r>();
    const T *__restrict c_end = c + M * N;
    event0();
    for (; c < c_end; c += r) {
        aie::store_v(c, zeros);
    }
    event1();
}

#endif