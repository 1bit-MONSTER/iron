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

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <type_traits>

void relu_vectorized_bf16(bfloat16 *restrict a, bfloat16 *restrict c, const int32_t vector_size)
{
    event0();

    const int v_factor = 32;
    v32bfloat16 zeroes = broadcast_zero_to_v32bfloat16();
    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_RANGE(32, 32)
    for (size_t i = 0; i < vector_size; i += v_factor) {
        v32bfloat16 input = *(v32bfloat16 *)(a + i);
        v32bfloat16 output = max(input, zeroes);
        *(v32bfloat16 *)(c + i) = output;
    }

    event1();

    return;
}

extern "C" {

void relu_bf16(bfloat16 *restrict input, bfloat16 *restrict output, int input_size)
{
    relu_vectorized_bf16(input, output, input_size);
}

} // extern "C"
