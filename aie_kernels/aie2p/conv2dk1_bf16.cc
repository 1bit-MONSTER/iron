// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// 1x1 Convolution kernel for bfloat16 activations and weights.
//
// Data layout (tiled, groups of 8 channels):
//   Input:  [H, C_in/8, W, 8]  -- one row of input at a time
//   Weight: [C_out/8, C_in/8, 8, 8]  -- all weights at once
//   Output: [H, C_out/8, W, 8] -- one row of output at a time
//
// For each output row, we iterate over output channel groups (C_out/8),
// accumulating the dot product across all input channel groups (C_in/8)
// for each spatial position in the row.
//
// The kernel uses the AIE2 4x8x8 bfloat16 mmul intrinsic.
// For each spatial position, we compute:
//   output[w, oc_group*8 + oc8] = sum_over_ic( input[w, ic_group*8 + ic8] * weight[oc_group, ic_group, ic8, oc8] )

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Scalar reference implementation for correctness validation.
// Input layout:  [C_in/8, W, 8]  (one row)
// Weight layout: [C_out/8, C_in/8, 8, 8]
// Output layout: [C_out/8, W, 8]  (one row)
void conv2dk1_bf16_scalar(bfloat16 *input, bfloat16 *weights, bfloat16 *output,
                          const int32_t input_width, const int32_t input_channels,
                          const int32_t output_channels) {
    event0();

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int w = 0; w < input_width; w++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                float sum = 0.0f;
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        // input index: [ic_g, w, ic8]
                        int in_idx = ic_g * (input_width * 8) + w * 8 + ic8;
                        // weight index: [oc_g, ic_g, ic8, oc8]
                        int wt_idx = oc_g * (ic_groups * 64) + ic_g * 64 + ic8 * 8 + oc8;
                        sum += (float)input[in_idx] * (float)weights[wt_idx];
                    }
                }
                // output index: [oc_g, w, oc8]
                int out_idx = oc_g * (input_width * 8) + w * 8 + oc8;
                output[out_idx] = (bfloat16)sum;
            }
        }
    }

    event1();
}

// Vectorized implementation using aie::mmul<4,8,8> for bf16.
//
// For each spatial position w, we treat it as a 1x(C_in) vector multiplied
// by a (C_in)x(C_out) weight matrix, in groups of 8 channels.
//
// We process 4 spatial positions at a time (NUM_W = 4) to amortize weight loads.
// The mmul<4,8,8> computes a [4,8] x [8,8] -> [4,8] tile.
//
// Inner loop over ic_groups accumulates partial products.
void conv2dk1_bf16_vectorized(bfloat16 *__restrict input, bfloat16 *__restrict weights,
                              bfloat16 *__restrict output, const int32_t input_width,
                              const int32_t input_channels, const int32_t output_channels) {
    event0();

    using MMUL = aie::mmul<4, 8, 8, bfloat16, bfloat16>;

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;

    // Process 4 spatial positions at a time
    constexpr int NUM_W = 4;
    const int w_iters = input_width / NUM_W;

    // Pointers
    bfloat16 *__restrict out_ptr = output;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int wi = 0; wi < w_iters; wi++) {
            // Initialize accumulators for NUM_W spatial positions x 8 output channels
            MMUL acc;
            acc = aie::zeros<accfloat, MMUL::size_C>();

            bfloat16 *__restrict in_ptr = input + wi * NUM_W * 8;
            bfloat16 *__restrict wt_ptr = weights + oc_g * ic_groups * 64;

            for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                // Load 4 spatial positions x 8 input channels = 32 bf16 values
                // Input layout: [ic_g, w, 8], stride between ic_groups is W*8
                aie::vector<bfloat16, MMUL::size_A> in_a = aie::load_v<MMUL::size_A>(in_ptr);
                in_ptr += input_width * 8; // advance to next ic_group

                // Load 8x8 weight tile for this (oc_g, ic_g) pair
                aie::vector<bfloat16, MMUL::size_B> in_b = aie::load_v<MMUL::size_B>(wt_ptr);
                wt_ptr += 64; // advance to next ic_group for same oc_group

                acc.mac(in_a, in_b);
            }

            // Store result: 4 spatial positions x 8 output channels
            aie::vector<bfloat16, MMUL::size_C> result = acc.to_vector<bfloat16>();
            aie::store_v(out_ptr, result);
            out_ptr += MMUL::size_C;
        }

        // Handle remaining spatial positions (width not divisible by NUM_W)
        int w_rem = input_width - w_iters * NUM_W;
        if (w_rem > 0) {
            // Fall back to scalar for remainder
            for (int w = w_iters * NUM_W; w < input_width; w++) {
                for (int oc8 = 0; oc8 < 8; oc8++) {
                    float sum = 0.0f;
                    for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                        for (int ic8 = 0; ic8 < 8; ic8++) {
                            int in_idx = ic_g * (input_width * 8) + w * 8 + ic8;
                            int wt_idx = oc_g * (ic_groups * 64) + ic_g * 64 + ic8 * 8 + oc8;
                            sum += (float)input[in_idx] * (float)weights[wt_idx];
                        }
                    }
                    *out_ptr++ = (bfloat16)sum;
                }
            }
        }
    }

    event1();
}

// Scalar bias+SiLU fused implementation.
// After MAC accumulation, adds per-channel bias and applies SiLU activation.
// SiLU(x) = x / (1 + exp(-x)), computed in float32 for accuracy.
// Bias+SiLU fused variant. Bias is packed at the end of the weight buffer:
//   weights layout: [oc/8, ic/8, 8, 8] followed by [oc] bias values.
// Same 3-buffer interface as conv2dk1_bf16 (no extra DMA channel needed).
void conv2dk1_bf16_bias_silu_scalar(bfloat16 *input, bfloat16 *weights,
                                     bfloat16 *output,
                                     const int32_t input_width,
                                     const int32_t input_channels,
                                     const int32_t output_channels) {
    event0();

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;

    // Bias is packed after weights: offset = oc * ic elements
    bfloat16 *bias = weights + output_channels * input_channels;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int w = 0; w < input_width; w++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                float sum = 0.0f;
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        int in_idx = ic_g * (input_width * 8) + w * 8 + ic8;
                        int wt_idx = oc_g * (ic_groups * 64) + ic_g * 64 + ic8 * 8 + oc8;
                        sum += (float)input[in_idx] * (float)weights[wt_idx];
                    }
                }
                // Add bias and apply SiLU in float32
                float val = sum + (float)bias[oc_g * 8 + oc8];
                // SiLU(x) = x * sigmoid(x) = x * 0.5 * (1 + tanh(x/2))
                // Approximate tanh using rational Padé: tanh(z) ≈ z*(27+z²)/(27+9*z²) for |z|<4.5
                float z = val * 0.5f;
                float z2 = z * z;
                float tanh_z = (z2 > 20.0f) ? (z > 0 ? 1.0f : -1.0f) : z * (27.0f + z2) / (27.0f + 9.0f * z2);
                float silu_val = val * 0.5f * (1.0f + tanh_z);
                int out_idx = oc_g * (input_width * 8) + w * 8 + oc8;
                output[out_idx] = (bfloat16)silu_val;
            }
        }
    }

    event1();
}

extern "C" {

void conv2dk1_bf16(bfloat16 *input, bfloat16 *weights, bfloat16 *output, const int32_t input_width,
                   const int32_t input_channels, const int32_t output_channels) {
    conv2dk1_bf16_vectorized(input, weights, output, input_width, input_channels, output_channels);
}

// Bias is packed after weights in the combined buffer.
// Layout: [weights (out_channels * in_channels) | bias (out_channels)]
// The scalar function derives bias pointer from weights internally.
void conv2dk1_bf16_bias_silu(bfloat16 *input, bfloat16 *weights, bfloat16 *output,
                              const int32_t input_width, const int32_t input_channels,
                              const int32_t output_channels) {
    conv2dk1_bf16_bias_silu_scalar(input, weights, output, input_width, input_channels, output_channels);
}

} // extern "C"
