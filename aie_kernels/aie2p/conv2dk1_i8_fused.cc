// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Fused int8 1x1 Conv + Bias + SiLU kernel for AIE2+.
//
// Computation (fully integer, no float between layers):
//   1. int8 x int8 -> int32 convolution accumulation (1x1 pointwise)
//   2. Add pre-scaled int32 bias to accumulator
//   3. Shift accumulator to int8 range (shift1) for SiLU LUT lookup
//   4. Look up sigmoid in a 256-entry uint8 LUT
//   5. Multiply: silu = acc_i8 * sigmoid_lut[acc_i8 + 128]
//   6. Shift product to output int8 range (shift2)
//
// The bias must be pre-scaled by the caller:
//   bias_int32[oc] = round(bias_float[oc] / (weight_scale * activation_scale))
// so that it matches the int32 accumulator's implicit scale.
//
// Interface: 3 buffers (input, weights_and_bias, output).
// The bias is packed at the end of the weights buffer:
//   weights_and_bias = [weights: OC*IC bytes] [bias: OC*4 bytes]
//
// Data layouts:
//   Input:   [C_in/8, W, 8]
//   Weights: [C_out/8, C_in/8, 8, 8]  (last two: [ic8, oc8])
//   Bias:    [C_out]  (int32, pre-scaled, packed after weights)
//   Output:  [C_out/8, W, 8]
//
// Shift parameters:
//   shift1: right-shift for acc -> int8 (for LUT index), determines the
//           effective input range to the sigmoid. With the default LUT
//           mapping int8 [-128,127] to real [-8,+8], shift1 should place
//           the typical accumulator range into [-128,127].
//   shift2: right-shift for the silu product (int8 * uint8) back to int8.
//           Since sigmoid output is [0,255] representing [0,1] scaled by
//           255, and the product is int8*uint8 -> int16, shift2 of ~7-8
//           (dividing by 128-256) rescales back to int8.

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Saturation limits
constexpr int32_t K1_SAT_MAX = 127;
constexpr int32_t K1_SAT_MIN = -128;

// ---------------------------------------------------------------------------
// Sigmoid LUT: 256 entries mapping int8 -> uint8.
//
// For index i in [0, 255], the corresponding int8 value is (i - 128),
// mapped to real value x = (i - 128) * 8.0 / 128.0 (range [-8, +8]).
// Entry = round(sigmoid(x) * 255), so 0 represents sigmoid ~ 0.0
// and 255 represents sigmoid ~ 1.0.
//
// sigmoid(-8) ~ 0.0003 -> 0
// sigmoid(0)  = 0.5    -> 128
// sigmoid(+8) ~ 0.9997 -> 255
// ---------------------------------------------------------------------------
// clang-format off
static const uint8_t sigmoid_lut[256] __attribute__((aligned(64))) = {
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   1,   1,
      1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,
      2,   2,   2,   2,   2,   2,   2,   3,   3,   3,   3,   3,   4,   4,   4,   4,
      5,   5,   5,   6,   6,   6,   7,   7,   7,   8,   8,   9,  10,  10,  11,  11,
     12,  13,  14,  14,  15,  16,  17,  18,  19,  20,  22,  23,  24,  26,  27,  29,
     30,  32,  34,  36,  38,  40,  42,  44,  47,  49,  51,  54,  57,  60,  62,  65,
     69,  72,  75,  78,  82,  85,  89,  93,  96, 100, 104, 108, 112, 116, 120, 124,
    128, 131, 135, 139, 143, 147, 151, 155, 159, 162, 166, 170, 173, 177, 180, 183,
    186, 190, 193, 195, 198, 201, 204, 206, 208, 211, 213, 215, 217, 219, 221, 223,
    225, 226, 228, 229, 231, 232, 233, 235, 236, 237, 238, 239, 240, 241, 241, 242,
    243, 244, 244, 245, 245, 246, 247, 247, 248, 248, 248, 249, 249, 249, 250, 250,
    250, 251, 251, 251, 251, 252, 252, 252, 252, 252, 253, 253, 253, 253, 253, 253,
    253, 253, 253, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254,
    254, 254, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255
};
// clang-format on

// ---------------------------------------------------------------------------
// Helper: right-shift with rounding and saturate to int8.
// ---------------------------------------------------------------------------
inline int8_t k1_srs_i8(int32_t val, int32_t shift) {
    int32_t rounded = (val + (1 << (shift - 1))) >> shift;
    rounded = (rounded > K1_SAT_MAX) ? K1_SAT_MAX
            : (rounded < K1_SAT_MIN) ? K1_SAT_MIN
                                     : rounded;
    return (int8_t)rounded;
}

// ---------------------------------------------------------------------------
// Scalar implementation: fused conv1x1 + bias + SiLU (all integer)
// ---------------------------------------------------------------------------
void conv2dk1_i8_fused_scalar(int8_t *input, int8_t *weights_and_bias,
                               int8_t *output, const int32_t input_width,
                               const int32_t input_channels,
                               const int32_t output_channels,
                               const int32_t shift1, const int32_t shift2) {
    event0();

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;

    // Weight layout strides (in elements):
    //   [oc_g, ic_g, ic8, oc8]
    //   sizes: [oc_groups, ic_groups, 8, 8]
    const int wt_stride_ic = 64; // 8 * 8
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    // Bias is packed after weights: weights are OC * IC bytes total
    int32_t *bias = (int32_t *)(weights_and_bias + output_channels * input_channels);

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x = 0; x < input_width; x++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                int32_t acc = 0;

                // --- Phase 1: 1x1 Convolution (int8 x int8 -> int32) ---
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        // Input index: [ic_g, x, ic8]
                        int in_idx = ic_g * (input_width * 8) + x * 8 + ic8;

                        // Weight index: [oc_g, ic_g, ic8, oc8]
                        int wt_idx = oc_g * wt_stride_oc + ic_g * wt_stride_ic +
                                     ic8 * 8 + oc8;

                        acc += (int32_t)input[in_idx] *
                               (int32_t)weights_and_bias[wt_idx];
                    }
                }

                // --- Phase 2: Add pre-scaled bias ---
                acc += bias[oc_g * 8 + oc8];

                // --- Phase 3: Integer SiLU via LUT ---
                // Step 3a: Shift accumulator to int8 range for LUT lookup
                int8_t acc_i8 = k1_srs_i8(acc, shift1);

                // Step 3b: Look up sigmoid value
                //   acc_i8 is in [-128, 127], adding 128 gives [0, 255]
                uint8_t sig = sigmoid_lut[(int)(acc_i8) + 128];

                // Step 3c: SiLU = x * sigmoid(x)
                //   acc_i8 (int8, [-128,127]) * sig (uint8, [0,255])
                //   Product range: [-128*255, 127*255] = [-32640, 32385]
                //   This fits in int16/int32.
                int32_t silu = (int32_t)acc_i8 * (int32_t)sig;

                // Step 3d: Shift the product to output int8 range
                int8_t out_val = k1_srs_i8(silu, shift2);

                // Output index: [oc_g, x, oc8]
                int out_idx = oc_g * (input_width * 8) + x * 8 + oc8;
                output[out_idx] = out_val;
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// extern "C" wrapper
// ---------------------------------------------------------------------------
extern "C" {

void conv2dk1_i8_fused(int8_t *input, int8_t *weights_and_bias, int8_t *output,
                        const int32_t input_width,
                        const int32_t input_channels,
                        const int32_t output_channels, const int32_t shift1,
                        const int32_t shift2) {
    conv2dk1_i8_fused_scalar(input, weights_and_bias, output, input_width,
                              input_channels, output_channels, shift1, shift2);
}

} // extern "C"
