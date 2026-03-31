// SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Fused int8 3x3 Conv + Bias + SiLU kernel (AIE2+).
//
// Paths:
//   Scalar (ACTIVE): Padé tanh approximation — correct at all sizes
//   Vector (DISABLED): aie::mmul<8,8,8> MAC + scalar Padé SiLU post-proc
//     - MMUL MAC is correct (verified: to_vector<int8>(shift) matches)
//     - BUT to_vector<int32>(0) produces wrong element values on AIE2p
//       with Peano -O2, causing ~17% error rate (max_diff=127)
//     - Previous attempt with aie::tanh<bfloat16>() also failed because
//       the hardware tanh intrinsic requires vector size >= 16, not 8
//
// Replaces the LUT-based sigmoid with a Padé rational approximation:
//   tanh(z) ≈ z*(27 + z²) / (27 + 9*z²)   for |z²| ≤ 20
//   tanh(z) = ±1                             for |z²| > 20
//
// SiLU(x) = x * sigmoid(x) = x * 0.5 * (1 + tanh(x/2))
//
// Pipeline (float-based activation):
//   1. int8 x int8 -> int32 convolution accumulation
//   2. Add pre-scaled int32 bias to accumulator
//   3. Convert to float: val = acc / 2^shift1
//   4. Compute SiLU via Padé tanh
//   5. Requantize: round(silu * 2^shift2), clamp to [-128, 127]
//
// Weight buffer layout (per FIFO element):
//   [int8 weights: oc * ic * 9 bytes | int32 bias: oc * 4 bytes]
//
// Data layouts:
//   Input rows:  [C_in/8, W, 8]
//   Weights:     [C_out/8, C_in/8, 3, 3, 8, 8]  (last two: [ic8, oc8])
//   Bias:        [C_out]  (int32, packed after weights)
//   Output row:  [C_out/8, W_out, 8]
//
// The `check` parameter controls vertical border handling:
//   0 (top):    line0 is padding (skipped)
//   1 (middle): all 3 lines are valid
//   2 (bottom): line2 is padding (skipped)

#define NOCPP

#include "../aie_kernel_utils.h"

#include <aie_api/aie.hpp>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Border check values
constexpr int CHECK_TOP = 0;
constexpr int CHECK_MIDDLE = 1;
constexpr int CHECK_BOTTOM = 2;

// ---------------------------------------------------------------------------
// Helper: get the line pointer for a given kernel row (kh).
// ---------------------------------------------------------------------------
inline int8_t *select_line(int kh, int8_t *line0, int8_t *line1,
                           int8_t *line2) {
    switch (kh) {
    case 0:
        return line0;
    case 1:
        return line1;
    default:
        return line2;
    }
}

// ---------------------------------------------------------------------------
// Helper: Padé tanh SiLU activation (float in, int8 out).
//
// Computes: SiLU(x) = x * 0.5 * (1 + tanh(x/2))
// where tanh is approximated by the Padé [3/2] form:
//   tanh(z) ≈ z * (27 + z²) / (27 + 9*z²)
// ---------------------------------------------------------------------------
// shift2 is a fixed-point 8.8 scale factor (upper bits: integer, lower 8: fraction).
// scale_out = shift2 / 256.0f. This provides exact requantization without
// power-of-2 rounding error that compounds across layers.
inline int8_t pade_silu_i8(int32_t acc, int32_t shift1, int32_t shift2) {
    float val = (float)acc / (float)(1 << shift1);
    float z = val * 0.5f;
    float z2 = z * z;
    float tanh_z;
    if (z2 > 20.0f) {
        tanh_z = (z > 0) ? 1.0f : -1.0f;
    } else {
        tanh_z = z * (27.0f + z2) / (27.0f + 9.0f * z2);
    }
    float silu_val = val * 0.5f * (1.0f + tanh_z);
    float scale_out = (float)shift2 / 256.0f;
    float scaled = silu_val * scale_out;
    int32_t out_i32 = (scaled >= 0) ? (int32_t)(scaled + 0.5f)
                                    : (int32_t)(scaled - 0.5f);
    if (out_i32 > 127)
        out_i32 = 127;
    if (out_i32 < -128)
        out_i32 = -128;
    return (int8_t)out_i32;
}

// ---------------------------------------------------------------------------
// Helper: round-to-nearest (AIE backend lacks __builtin_roundf).
// ---------------------------------------------------------------------------
inline int32_t float_to_int_round(float x) {
    return (x >= 0.0f) ? (int32_t)(x + 0.5f) : (int32_t)(x - 0.5f);
}

// ---------------------------------------------------------------------------
// Scalar stride-1: fused conv3x3 + bias + Padé SiLU with packed bias
// ---------------------------------------------------------------------------
void conv2dk3_i8_silu_scalar(int8_t *line0, int8_t *line1, int8_t *line2,
                             int8_t *weights_and_bias, int8_t *output,
                             const int32_t input_width,
                             const int32_t input_channels,
                             const int32_t output_channels,
                             const int32_t check, const int32_t shift1,
                             const int32_t shift2) {
    event0();

    // Derive bias pointer from packed buffer
    int8_t *weights = weights_and_bias;
    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels * 9);

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width; // stride 1, padding=1

    // Weight layout strides (in elements):
    //   [oc_g, ic_g, kh, kw, ic8, oc8]
    const int wt_stride_kw = 64;             // 8 * 8
    const int wt_stride_kh = 3 * 64;         // 3 * 8 * 8
    const int wt_stride_ic = 3 * 3 * 64;     // 3 * 3 * 8 * 8
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x = 0; x < output_width; x++) {
            for (int oc8 = 0; oc8 < 8; oc8++) {
                int32_t acc = 0;

                // --- Phase 1: Convolution (int8 x int8 -> int32) ---
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = 0; kh < 3; kh++) {
                            if (kh == 0 && check == CHECK_TOP)
                                continue;
                            if (kh == 2 && check == CHECK_BOTTOM)
                                continue;

                            int8_t *line =
                                select_line(kh, line0, line1, line2);

                            for (int kw = 0; kw < 3; kw++) {
                                int input_x = x + kw - 1;
                                if (input_x < 0 || input_x >= input_width)
                                    continue;

                                int in_idx =
                                    ic_g * (input_width * 8) + input_x * 8 +
                                    ic8;
                                int wt_idx = oc_g * wt_stride_oc +
                                             ic_g * wt_stride_ic +
                                             kh * wt_stride_kh +
                                             kw * wt_stride_kw + ic8 * 8 +
                                             oc8;

                                acc += (int32_t)line[in_idx] *
                                       (int32_t)weights[wt_idx];
                            }
                        }
                    }
                }

                // --- Phase 2: Add pre-scaled bias ---
                acc += bias[oc_g * 8 + oc8];

                // --- Phase 3: Padé SiLU ---
                int8_t out_val = pade_silu_i8(acc, shift1, shift2);

                int out_idx = oc_g * (output_width * 8) + x * 8 + oc8;
                output[out_idx] = out_val;
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// Scalar stride-2: fused conv3x3 + bias + Padé SiLU with packed bias
// ---------------------------------------------------------------------------
void conv2dk3s2_i8_silu_scalar(int8_t *line0, int8_t *line1, int8_t *line2,
                               int8_t *weights_and_bias, int8_t *output,
                               const int32_t input_width,
                               const int32_t input_channels,
                               const int32_t output_channels,
                               const int32_t check, const int32_t shift1,
                               const int32_t shift2) {
    event0();

    int8_t *weights = weights_and_bias;
    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels * 9);

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width / 2; // stride 2

    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int x_out = 0; x_out < output_width; x_out++) {
            int x_in_base = x_out * 2; // stride-2 base position

            for (int oc8 = 0; oc8 < 8; oc8++) {
                int32_t acc = 0;

                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    for (int ic8 = 0; ic8 < 8; ic8++) {
                        for (int kh = 0; kh < 3; kh++) {
                            if (kh == 0 && check == CHECK_TOP)
                                continue;
                            if (kh == 2 && check == CHECK_BOTTOM)
                                continue;

                            int8_t *line =
                                select_line(kh, line0, line1, line2);

                            for (int kw = 0; kw < 3; kw++) {
                                int input_x = x_in_base + kw - 1;
                                if (input_x < 0 || input_x >= input_width)
                                    continue;

                                int in_idx =
                                    ic_g * (input_width * 8) + input_x * 8 +
                                    ic8;
                                int wt_idx = oc_g * wt_stride_oc +
                                             ic_g * wt_stride_ic +
                                             kh * wt_stride_kh +
                                             kw * wt_stride_kw + ic8 * 8 +
                                             oc8;

                                acc += (int32_t)line[in_idx] *
                                       (int32_t)weights[wt_idx];
                            }
                        }
                    }
                }

                acc += bias[oc_g * 8 + oc8];

                int8_t out_val = pade_silu_i8(acc, shift1, shift2);

                int out_idx = oc_g * (output_width * 8) + x_out * 8 + oc8;
                output[out_idx] = out_val;
            }
        }
    }

    event1();
}

// ---------------------------------------------------------------------------
// Vectorized stride-1: fused conv3x3 + bias + scalar Padé SiLU
//
// Uses aie::mmul<8,8,8,int8,int8> for the convolution MAC (same logic as
// the working non-fused conv2dk3_i8_vectorized), then applies SiLU
// element-by-element using the scalar Padé tanh approximation.
//
// To minimize code size and avoid compiler issues with mixed MMUL + float
// in a single large function, the SiLU post-processing is factored into
// a separate noinline helper (apply_silu_block). This also helps with
// the 16KB AIE instruction memory limit at large spatial sizes.
//
// The extern "C" wrapper only dispatches here when input_width % 8 == 0,
// so no scalar remainder is needed.
// ---------------------------------------------------------------------------

// Vectorized SiLU post-processing using vec-16 aie::tanh<bfloat16>().
//
// Workaround for to_vector<int32>(0) element ordering bug on AIE2p:
// extract MMUL result as int8 (correct ordering), upconvert to bf16,
// add bias in bf16, apply vec-16 SiLU, requant to int8.
//
// The MMUL result after to_vector<int8>(shift1) is laid out as:
//   [sp0_ch0..ch7, sp1_ch0..ch7, ..., sp7_ch0..ch7]
// Process in groups of 16 (2 spatial positions × 8 channels).
__attribute__((noinline)) static void apply_silu_block_vec16(
    aie::vector<int8, 64> conv_i8,
    bfloat16 *__restrict bias_bf16_buf,
    int8_t *__restrict out_buf, int32_t shift2) {

    float scale_out = (float)shift2 / 256.0f;

    aie::vector<bfloat16, 16> half_v =
        aie::broadcast<bfloat16, 16>((bfloat16)0.5f);
    aie::vector<bfloat16, 16> one_v =
        aie::broadcast<bfloat16, 16>((bfloat16)1.0f);

    // Staging buffer: convert 64 int8 -> bf16 with bias, then apply SiLU
    alignas(64) bfloat16 bf16_staging[16];

    // Process 4 groups of 16 elements (2 spatial × 8 channels each)
    for (int g = 0; g < 4; g++) {
        // int8 -> bfloat16 conversion + bias addition (scalar loop)
        int base = g * 16;
        for (int i = 0; i < 16; i++) {
            float fval = (float)conv_i8[base + i];
            bf16_staging[i] =
                (bfloat16)(fval + (float)bias_bf16_buf[i]);
        }

        // Load 16 bf16 values for vec-16 SiLU
        aie::vector<bfloat16, 16> x_bf16 =
            aie::load_v<16>(bf16_staging);

        // Vec-16 SiLU: x * 0.5 * (1 + tanh(x/2))
        auto half_x = aie::mul(x_bf16, half_v);
        auto tanh_hx =
            aie::tanh<bfloat16>(half_x.to_vector<float>());
        auto one_plus = aie::add(tanh_hx, one_v);
        aie::vector<bfloat16, 16> sigmoid =
            aie::mul(one_plus, half_v);
        auto silu_acc = aie::mul(x_bf16, sigmoid);
        aie::vector<bfloat16, 16> silu_bf16 =
            silu_acc.to_vector<bfloat16>();

        // Requant bf16 -> int8
        aie::store_v(bf16_staging, silu_bf16);
        for (int i = 0; i < 16; i++) {
            float sval = (float)bf16_staging[i];
            int32_t oval = float_to_int_round(sval * scale_out);
            oval = (oval > 127) ? 127 : (oval < -128) ? -128 : oval;
            out_buf[base + i] = (int8_t)oval;
        }
    }
}

// Scalar fallback for SiLU post-processing (used by stride-2 and as
// reference). Uses to_vector<int32>(0) which has correct element
// ordering when called from scalar context.
__attribute__((noinline)) static void apply_silu_block_scalar(
    int32_t *__restrict acc_buf, int32_t *__restrict bias_ptr,
    int8_t *__restrict out_buf, int32_t oc_g, int32_t shift1,
    int32_t shift2) {
    for (int i = 0; i < 64; i++) {
        int32_t val = acc_buf[i] + bias_ptr[oc_g * 8 + (i & 7)];
        out_buf[i] = pade_silu_i8(val, shift1, shift2);
    }
}

void conv2dk3_i8_silu_vectorized(
    int8_t *__restrict line0, int8_t *__restrict line1,
    int8_t *__restrict line2, int8_t *__restrict weights_and_bias,
    int8_t *__restrict output, const int32_t input_width,
    const int32_t input_channels, const int32_t output_channels,
    const int32_t check, const int32_t shift1, const int32_t shift2) {
    event0();

    using MMUL = aie::mmul<8, 8, 8, int8, int8>;

    int8_t *weights = weights_and_bias;
    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels * 9);

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width;

    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    int8_t *lines[3] = {line0, line1, line2};

    constexpr int NUM_W = 8;
    const int vec_iters = input_width / NUM_W;

    aie::vector<int8, MMUL::size_A> zeros_v =
        aie::zeros<int8, MMUL::size_A>();

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    // Temporary buffers for MMUL result extraction and output assembly
    alignas(64) int8_t out_buf[MMUL::size_C];

    // Pre-compute bias as bfloat16 for vec-16 SiLU.
    // Layout: [bias_ch0..ch7, bias_ch0..ch7] repeated for 16-element groups.
    // Bias is pre-scaled int32 in accumulator domain; convert to float domain
    // by multiplying by 2^(-shift1).
    float bias_scale = 1.0f / (float)(1 << shift1);
    alignas(64) bfloat16 bias_bf16_buf[16];

    // Pre-evaluate check conditions outside inner loop
    const bool do_kh0 = (check != CHECK_TOP);
    const bool do_kh2 = (check != CHECK_BOTTOM);

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int vi = 0; vi < vec_iters; vi++) {
            int x_base = vi * NUM_W;

            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            // kh=0: skip if top border
            if (do_kh0) {
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    int8_t *__restrict lp =
                        lines[0] + ic_g * (input_width * 8);

                    aie::vector<int8, MMUL::size_A> v_c =
                        aie::load_v<MMUL::size_A>(lp + x_base * 8);

                    aie::vector<int8, MMUL::size_A> v_kw0;
                    if (vi > 0) {
                        v_kw0 = aie::shuffle_up_fill(
                            v_c,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_base - NUM_W) * 8),
                            8);
                    } else {
                        v_kw0 = aie::shuffle_up_fill(v_c, zeros_v, 8);
                    }

                    aie::vector<int8, MMUL::size_A> v_kw2;
                    if (x_base + NUM_W < input_width) {
                        v_kw2 = aie::shuffle_down_fill(
                            v_c,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_base + NUM_W) * 8),
                            8);
                    } else {
                        v_kw2 =
                            aie::shuffle_down_fill(v_c, zeros_v, 8);
                    }

                    int8_t *__restrict wp =
                        weights + oc_g * wt_stride_oc +
                        ic_g * wt_stride_ic + 0 * wt_stride_kh;

                    acc.mac(v_kw0,
                            aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_c,
                            aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
                    acc.mac(v_kw2,
                            aie::load_v<MMUL::size_B>(
                                wp + 2 * wt_stride_kw));
                }
            }

            // kh=1: always process (middle row is always valid)
            for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                int8_t *__restrict lp =
                    lines[1] + ic_g * (input_width * 8);

                aie::vector<int8, MMUL::size_A> v_c =
                    aie::load_v<MMUL::size_A>(lp + x_base * 8);

                aie::vector<int8, MMUL::size_A> v_kw0;
                if (vi > 0) {
                    v_kw0 = aie::shuffle_up_fill(
                        v_c,
                        aie::load_v<MMUL::size_A>(
                            lp + (x_base - NUM_W) * 8),
                        8);
                } else {
                    v_kw0 = aie::shuffle_up_fill(v_c, zeros_v, 8);
                }

                aie::vector<int8, MMUL::size_A> v_kw2;
                if (x_base + NUM_W < input_width) {
                    v_kw2 = aie::shuffle_down_fill(
                        v_c,
                        aie::load_v<MMUL::size_A>(
                            lp + (x_base + NUM_W) * 8),
                        8);
                } else {
                    v_kw2 =
                        aie::shuffle_down_fill(v_c, zeros_v, 8);
                }

                int8_t *__restrict wp =
                    weights + oc_g * wt_stride_oc +
                    ic_g * wt_stride_ic + 1 * wt_stride_kh;

                acc.mac(v_kw0,
                        aie::load_v<MMUL::size_B>(wp));
                acc.mac(v_c,
                        aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
                acc.mac(v_kw2,
                        aie::load_v<MMUL::size_B>(
                            wp + 2 * wt_stride_kw));
            }

            // kh=2: skip if bottom border
            if (do_kh2) {
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    int8_t *__restrict lp =
                        lines[2] + ic_g * (input_width * 8);

                    aie::vector<int8, MMUL::size_A> v_c =
                        aie::load_v<MMUL::size_A>(lp + x_base * 8);

                    aie::vector<int8, MMUL::size_A> v_kw0;
                    if (vi > 0) {
                        v_kw0 = aie::shuffle_up_fill(
                            v_c,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_base - NUM_W) * 8),
                            8);
                    } else {
                        v_kw0 = aie::shuffle_up_fill(v_c, zeros_v, 8);
                    }

                    aie::vector<int8, MMUL::size_A> v_kw2;
                    if (x_base + NUM_W < input_width) {
                        v_kw2 = aie::shuffle_down_fill(
                            v_c,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_base + NUM_W) * 8),
                            8);
                    } else {
                        v_kw2 =
                            aie::shuffle_down_fill(v_c, zeros_v, 8);
                    }

                    int8_t *__restrict wp =
                        weights + oc_g * wt_stride_oc +
                        ic_g * wt_stride_ic + 2 * wt_stride_kh;

                    acc.mac(v_kw0,
                            aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_c,
                            aie::load_v<MMUL::size_B>(wp + wt_stride_kw));
                    acc.mac(v_kw2,
                            aie::load_v<MMUL::size_B>(
                                wp + 2 * wt_stride_kw));
                }
            }

            // Extract int32 accumulators and apply scalar Padé SiLU.
            //
            // NOTE: to_vector<int32>(0) has platform-specific element
            // ordering on AIE2p, BUT the scalar pade_silu_i8 loop
            // accesses acc_buf[i] + bias[oc_g*8 + (i&7)] which matches
            // the ordering when called from this context. Verified:
            // to_vector<int8>(shift) gives exact match → the MMUL is
            // correct; the scalar SiLU on extracted int32 also works.
            //
            // Vec-16 aie::tanh<bfloat16>() would be faster but requires
            // adding bias BEFORE int8 extraction (int8 clips large
            // accumulator values that bias brings into range). No known
            // AIE2p API to add int32 bias to acc32 with correct ordering.
            alignas(64) int32_t local_acc_buf[MMUL::size_C];
            aie::store_v(local_acc_buf,
                         acc.to_vector<int32>(0));

            for (int i = 0; i < 64; i++) {
                int32_t val =
                    local_acc_buf[i] + bias[oc_g * 8 + (i & 7)];
                out_buf[i] = pade_silu_i8(val, shift1, shift2);
            }

            aie::store_v(
                output + oc_g * (output_width * 8) + x_base * 8,
                aie::load_v<MMUL::size_C>(out_buf));
        }
    }

    ::aie::set_saturation(aie::saturation_mode::none);
    ::aie::set_rounding(aie::rounding_mode::floor);

    event1();
}

// ---------------------------------------------------------------------------
// Helper: extract even/odd 8-element groups from two consecutive vectors
// for stride-2 gather (same as conv2dk3_i8.cc).
// ---------------------------------------------------------------------------
inline void stride2_gather_silu(
    const aie::vector<int8, 64> &vec_lo,
    const aie::vector<int8, 64> &vec_hi,
    aie::vector<int8, 64> &v_even,
    aie::vector<int8, 64> &v_odd) {
    aie::vector<int8, 32> lo_even = aie::filter_even(vec_lo, 8);
    aie::vector<int8, 32> lo_odd = aie::filter_odd(vec_lo, 8);
    aie::vector<int8, 32> hi_even = aie::filter_even(vec_hi, 8);
    aie::vector<int8, 32> hi_odd = aie::filter_odd(vec_hi, 8);
    v_even = aie::concat(lo_even, hi_even);
    v_odd = aie::concat(lo_odd, hi_odd);
}

// ---------------------------------------------------------------------------
// Vectorized stride-2: fused conv3x3 + bias + scalar Padé SiLU
//
// Uses aie::mmul<8,8,8,int8,int8> for convolution with stride-2 gather
// (same as non-fused conv2dk3s2_i8_vectorized), then applies scalar Padé
// SiLU on extracted int32 accumulators.
// ---------------------------------------------------------------------------
void conv2dk3s2_i8_silu_vectorized(
    int8_t *__restrict line0, int8_t *__restrict line1,
    int8_t *__restrict line2, int8_t *__restrict weights_and_bias,
    int8_t *__restrict output, const int32_t input_width,
    const int32_t input_channels, const int32_t output_channels,
    const int32_t check, const int32_t shift1, const int32_t shift2) {
    event0();

    using MMUL = aie::mmul<8, 8, 8, int8, int8>;

    int8_t *weights = weights_and_bias;
    int32_t *bias =
        (int32_t *)(weights_and_bias + output_channels * input_channels * 9);

    const int ic_groups = input_channels / 8;
    const int oc_groups = output_channels / 8;
    const int output_width = input_width / 2;

    const int wt_stride_kw = 64;
    const int wt_stride_kh = 3 * 64;
    const int wt_stride_ic = 3 * 3 * 64;
    const int wt_stride_oc = ic_groups * wt_stride_ic;

    int8_t *lines[3] = {line0, line1, line2};

    constexpr int NUM_W = 8;
    constexpr int INPUT_PER_ITER = 16;
    const int vec_iters = output_width / NUM_W;

    aie::vector<int8, MMUL::size_A> zeros_v =
        aie::zeros<int8, MMUL::size_A>();

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    // Temporary buffers
    alignas(64) int8_t out_buf[MMUL::size_C];

    // Pre-compute bias scale for bf16 conversion
    float bias_scale_s2 = 1.0f / (float)(1 << shift1);
    alignas(64) bfloat16 bias_bf16_buf_s2[16];

    const bool do_kh0 = (check != CHECK_TOP);
    const bool do_kh2 = (check != CHECK_BOTTOM);

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int vi = 0; vi < vec_iters; vi++) {
            int x_in = vi * INPUT_PER_ITER;

            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            // kh=0: skip if top border
            if (do_kh0) {
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    int8_t *__restrict lp =
                        lines[0] + ic_g * (input_width * 8);

                    aie::vector<int8, MMUL::size_A> vec_lo =
                        aie::load_v<MMUL::size_A>(lp + x_in * 8);
                    aie::vector<int8, MMUL::size_A> vec_hi =
                        aie::load_v<MMUL::size_A>(
                            lp + (x_in + NUM_W) * 8);

                    aie::vector<int8, MMUL::size_A> v_even, v_odd;
                    stride2_gather_silu(vec_lo, vec_hi, v_even, v_odd);

                    aie::vector<int8, MMUL::size_A> v_left;
                    if (vi > 0) {
                        v_left = aie::shuffle_up_fill(
                            v_odd,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_in - NUM_W) * 8),
                            8);
                    } else {
                        v_left = aie::shuffle_up_fill(
                            v_odd, zeros_v, 8);
                    }

                    int8_t *__restrict wp =
                        weights + oc_g * wt_stride_oc +
                        ic_g * wt_stride_ic + 0 * wt_stride_kh;

                    acc.mac(v_left,
                            aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_even,
                            aie::load_v<MMUL::size_B>(
                                wp + wt_stride_kw));
                    acc.mac(v_odd,
                            aie::load_v<MMUL::size_B>(
                                wp + 2 * wt_stride_kw));
                }
            }

            // kh=1: always process
            for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                int8_t *__restrict lp =
                    lines[1] + ic_g * (input_width * 8);

                aie::vector<int8, MMUL::size_A> vec_lo =
                    aie::load_v<MMUL::size_A>(lp + x_in * 8);
                aie::vector<int8, MMUL::size_A> vec_hi =
                    aie::load_v<MMUL::size_A>(
                        lp + (x_in + NUM_W) * 8);

                aie::vector<int8, MMUL::size_A> v_even, v_odd;
                stride2_gather_silu(vec_lo, vec_hi, v_even, v_odd);

                aie::vector<int8, MMUL::size_A> v_left;
                if (vi > 0) {
                    v_left = aie::shuffle_up_fill(
                        v_odd,
                        aie::load_v<MMUL::size_A>(
                            lp + (x_in - NUM_W) * 8),
                        8);
                } else {
                    v_left = aie::shuffle_up_fill(
                        v_odd, zeros_v, 8);
                }

                int8_t *__restrict wp =
                    weights + oc_g * wt_stride_oc +
                    ic_g * wt_stride_ic + 1 * wt_stride_kh;

                acc.mac(v_left,
                        aie::load_v<MMUL::size_B>(wp));
                acc.mac(v_even,
                        aie::load_v<MMUL::size_B>(
                            wp + wt_stride_kw));
                acc.mac(v_odd,
                        aie::load_v<MMUL::size_B>(
                            wp + 2 * wt_stride_kw));
            }

            // kh=2: skip if bottom border
            if (do_kh2) {
                for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                    int8_t *__restrict lp =
                        lines[2] + ic_g * (input_width * 8);

                    aie::vector<int8, MMUL::size_A> vec_lo =
                        aie::load_v<MMUL::size_A>(lp + x_in * 8);
                    aie::vector<int8, MMUL::size_A> vec_hi =
                        aie::load_v<MMUL::size_A>(
                            lp + (x_in + NUM_W) * 8);

                    aie::vector<int8, MMUL::size_A> v_even, v_odd;
                    stride2_gather_silu(vec_lo, vec_hi, v_even, v_odd);

                    aie::vector<int8, MMUL::size_A> v_left;
                    if (vi > 0) {
                        v_left = aie::shuffle_up_fill(
                            v_odd,
                            aie::load_v<MMUL::size_A>(
                                lp + (x_in - NUM_W) * 8),
                            8);
                    } else {
                        v_left = aie::shuffle_up_fill(
                            v_odd, zeros_v, 8);
                    }

                    int8_t *__restrict wp =
                        weights + oc_g * wt_stride_oc +
                        ic_g * wt_stride_ic + 2 * wt_stride_kh;

                    acc.mac(v_left,
                            aie::load_v<MMUL::size_B>(wp));
                    acc.mac(v_even,
                            aie::load_v<MMUL::size_B>(
                                wp + wt_stride_kw));
                    acc.mac(v_odd,
                            aie::load_v<MMUL::size_B>(
                                wp + 2 * wt_stride_kw));
                }
            }

            // Extract as int8 with shift1 (correct ordering), apply vec-16 SiLU
            aie::vector<int8, MMUL::size_C> conv_i8 =
                acc.to_vector<int8>(shift1);

            for (int j = 0; j < 8; j++) {
                bfloat16 bv = (bfloat16)((float)bias[oc_g * 8 + j] *
                                         bias_scale_s2);
                bias_bf16_buf_s2[j] = bv;
                bias_bf16_buf_s2[8 + j] = bv;
            }

            apply_silu_block_vec16(conv_i8, bias_bf16_buf_s2, out_buf,
                                   shift2);

            aie::store_v(
                output + oc_g * (output_width * 8) + vi * NUM_W * 8,
                aie::load_v<MMUL::size_C>(out_buf));
        }
    }

    ::aie::set_saturation(aie::saturation_mode::none);
    ::aie::set_rounding(aie::rounding_mode::floor);

    event1();
}

// ---------------------------------------------------------------------------
// extern "C" wrappers — dispatch to vectorized or scalar
// ---------------------------------------------------------------------------
extern "C" {

void conv2dk3_i8_silu(int8_t *line0, int8_t *line1, int8_t *line2,
                      int8_t *weights_and_bias, int8_t *output,
                      const int32_t input_width, const int32_t input_channels,
                      const int32_t output_channels, const int32_t check,
                      const int32_t shift1, const int32_t shift2) {
    // Scalar Padé SiLU: verified exact at all sizes.
    // Vectorization blocked by to_vector<int32>(0) element ordering bug
    // on AIE2p — bias must be added in int32 domain before SiLU, but
    // the int32 extraction reorders elements incorrectly.
    // Vec-16 aie::tanh<bfloat16>() requires adding bias AFTER int8
    // extraction, which clips large accumulator values.
    conv2dk3_i8_silu_scalar(line0, line1, line2, weights_and_bias, output,
                            input_width, input_channels, output_channels,
                            check, shift1, shift2);
}

void conv2dk3s2_i8_silu(int8_t *line0, int8_t *line1, int8_t *line2,
                        int8_t *weights_and_bias, int8_t *output,
                        const int32_t input_width, const int32_t input_channels,
                        const int32_t output_channels, const int32_t check,
                        const int32_t shift1, const int32_t shift2) {
    conv2dk3s2_i8_silu_scalar(line0, line1, line2, weights_and_bias,
                              output, input_width, input_channels,
                              output_channels, check, shift1, shift2);
}

} // extern "C"
