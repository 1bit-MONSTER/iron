// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <type_traits>

#define VECTOR_LENGTH 64

#define ROUNDING_MODE aie::rounding_mode::conv_even

extern "C" {
void matmul_scalar_bf16_bf16(bfloat16 *a_in, bfloat16 *b_in, bfloat16 *c_out);
void matmul_bf16_bf16(bfloat16 *a_in, bfloat16 *b_in, bfloat16 *c_out);
void matmul_bf16_bf16_rowmaj(bfloat16 *a_in, bfloat16 *b_in, bfloat16 *c_out);
void partial_softmax_bf16(bfloat16 *input,
                          bfloat16 *output,
                          bfloat16 *scale_buffer,
                          const int32_t input_size,
                          const int32_t row_idx,
                          const int32_t row_size,
                          const bfloat16 scale);
void passThroughLine(int32_t *in, int32_t *out, int32_t lineWidth);
void zero_bf16(bfloat16 *buffer);

void matmul_bf16_bf16_wrapper(bfloat16 *a_in, bfloat16 *b_in, bfloat16 *c_out, int32_t *idx_buffer)
{

    ::aie::set_rounding(ROUNDING_MODE);

    if (idx_buffer[0] > idx_buffer[1]) {
        return;
    }

    matmul_bf16_bf16(a_in, b_in, c_out);
}

void matmul_bf16_bf16_wrapper_scalar(bfloat16 *a_in, bfloat16 *b_in, bfloat16 *c_out)
{

    ::aie::set_rounding(ROUNDING_MODE);
    matmul_scalar_bf16_bf16(a_in, b_in, c_out);
}

void matmul_PV(bfloat16 *Q,
               bfloat16 *K,
               bfloat16 *out,
               bfloat16 *scale_buffer,
               const int32_t B_q,
               int32_t first_iter,
               int32_t *idx_buffer)
{

    ::aie::set_rounding(ROUNDING_MODE);

    if (idx_buffer[0] > idx_buffer[1]) {
        return;
    }

    // 64 emul: O dims = [(8, 512), (8, 8), (8, 64), (8, 1)]
    // VJUNG: Scale O_{i-1} by 1/exp(m_{i-1} - m_{i}) store in scale_buffer[3*B_q:3*B_q + B_q]
    // VJUNG: Skip this for the first iteration as 1/exp(m_{i-1} - m_{i}) degenerates to inf due to m intizalized to
    // -inf
    using Vec8bf16 = aie::vector<bfloat16, 8>;
    if (first_iter != 0) {
        for (int32_t l = 0; l < 8; l++) {
            // Load 8 scale values at once for the current l iteration
            Vec8bf16 scale_row = aie::load_v<8>(scale_buffer + 3 * B_q + l * 8);

            for (int32_t k = 0; k < 8; k++) {
                // Extract the scale value for this k from the loaded vector
                bfloat16 scale_val = scale_row[k];
                Vec8bf16 scale_vec = aie::broadcast<bfloat16, 8>(scale_val);

                for (int32_t j = 0; j < 8; j++) {
                    Vec8bf16 o_vec = aie::load_v<8>(out + j * 64 + k * 8 + l * 512);
                    o_vec = aie::mul(o_vec, scale_vec);
                    aie::store_v(out + j * 64 + k * 8 + l * 512, o_vec);
                }
            }
        }
    }

    matmul_bf16_bf16_rowmaj(Q, K, out);
}

void rescale_O(bfloat16 *O, bfloat16 *scale_buffer, int32_t B_q, int32_t *idx_buffer)
{

    ::aie::set_rounding(ROUNDING_MODE);

    for (int32_t i = 0; i < B_q; i += VECTOR_LENGTH) {
        using Vec64bf16 = aie::vector<bfloat16, VECTOR_LENGTH>;
        Vec64bf16 l_vec = aie::load_v<VECTOR_LENGTH>(scale_buffer + 2 * B_q + i);
        l_vec = aie::inv(l_vec);
        aie::store_v(scale_buffer + 2 * B_q + i, l_vec);
    }

    // VJUNG: Only after all KV are processed
    // VJUNG: TODO: Make this generic for every tile size
    // VJUNG: Need to scale depending on the data layout at the output of GEMM
    // VJUNG: Scale O_{i} by 1/l_{i}
    using Vec8bf16 = aie::vector<bfloat16, 8>;
    for (int32_t l = 0; l < 8; l++) {
        // Load 8 scale values at once for the current l iteration
        using Vec8bf16 = aie::vector<bfloat16, 8>;
        Vec8bf16 scale_row = aie::load_v<8>(scale_buffer + 2 * B_q + l * 8);

        for (int32_t k = 0; k < 8; k++) {
            // Extract the scale value for this k from the loaded vector
            bfloat16 scale_val = scale_row[k];
            Vec8bf16 scale_vec = aie::broadcast<bfloat16, 8>(scale_val);

            for (int32_t j = 0; j < 8; j++) {
                Vec8bf16 o_vec = aie::load_v<8>(O + j * 64 + k * 8 + l * 512);
                o_vec = aie::mul(o_vec, scale_vec);
                aie::store_v(O + j * 64 + k * 8 + l * 512, o_vec);
            }
        }
    }
}

void partial_softmax(bfloat16 *A,
                     bfloat16 *P,
                     bfloat16 *scale_buffer,
                     int32_t *idx_buffer,
                     bfloat16 inv_scale,
                     int32_t B_q,
                     int32_t B_kv)
{

    ::aie::set_rounding(ROUNDING_MODE);

    if (idx_buffer[0] == idx_buffer[1]) {
        int32_t q_block_idx = idx_buffer[1];
        int32_t kv_block_idx = idx_buffer[0];
        // VJUNG: Causal mask based on block position (naive implementation)
        for (int32_t i = 0; i < B_q; i++) {
            for (int32_t j = 0; j < B_kv; j++) {
                int32_t global_j = kv_block_idx * B_kv + j;
                int32_t global_i = q_block_idx * B_q + i;
                if (global_j > global_i) {
                    A[i * B_kv + j] = std::numeric_limits<bfloat16>::lowest();
                }
            }
        }
    }

    if (idx_buffer[0] > idx_buffer[1]) {
        zero_bf16(P);
        return;
    }

    using Vec64bf16 = aie::vector<bfloat16, VECTOR_LENGTH>;
    for (int32_t i = 0; i < B_q; i++) {
        partial_softmax_bf16(A + B_kv * i, P + B_kv * i, scale_buffer, B_kv, i, B_q, inv_scale);
    }

    for (int32_t i = 0; i < B_q; i += VECTOR_LENGTH) {

        Vec64bf16 m_i_minus_1 = aie::load_v<VECTOR_LENGTH>(scale_buffer + i);
        Vec64bf16 m_i = aie::load_v<VECTOR_LENGTH>(scale_buffer + B_q + i);
        Vec64bf16 l_i_minus_1 = aie::load_v<VECTOR_LENGTH>(scale_buffer + 2 * B_q + i);
        Vec64bf16 accum_exp_val = aie::load_v<VECTOR_LENGTH>(scale_buffer + 3 * B_q + i);

        aie::accum<accfloat, VECTOR_LENGTH> l_i_accum = aie::zeros<accfloat, VECTOR_LENGTH>();

        aie::accum<accfloat, VECTOR_LENGTH> diff = aie::accum<accfloat, VECTOR_LENGTH>(aie::sub(m_i_minus_1, m_i));
        l_i_accum = aie::exp2<bfloat16>(diff.to_vector<float>());
        Vec64bf16 max_diff_exp = l_i_accum.to_vector<bfloat16>();

        aie::store_v(scale_buffer + 3 * B_q + i, max_diff_exp);
        aie::accum<accfloat, VECTOR_LENGTH> l_i = aie::add(aie::mul(max_diff_exp, l_i_minus_1), accum_exp_val);
        aie::store_v(scale_buffer + 2 * B_q + i, l_i.to_vector<bfloat16>());
        aie::store_v(scale_buffer + i, m_i);
    }
}

void init_scale_buffer(bfloat16 *scale_buffer, int32_t size)
{
    ::aie::set_rounding(ROUNDING_MODE);

    using Vec64bf16 = aie::vector<bfloat16, VECTOR_LENGTH>;
    Vec64bf16 lowest_vec = aie::broadcast<bfloat16, VECTOR_LENGTH>(std::numeric_limits<bfloat16>::lowest());
    Vec64bf16 zeros_vec = aie::broadcast<bfloat16, VECTOR_LENGTH>(0.0f);

    for (int32_t i = 0; i < size; i += VECTOR_LENGTH) {
        // VJUNG: m_{i-1} vector
        aie::store_v(scale_buffer + i, lowest_vec);
        // VJUNG: m_{i} vector
        aie::store_v(scale_buffer + size + i, zeros_vec);
        // VJUNG: l_{i} vector
        aie::store_v(scale_buffer + 2 * size + i, zeros_vec);
    }
}
}