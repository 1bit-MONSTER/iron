//===- conv2dk1_i8.cc -------------------------------------------*- C++ -*-===//

//
// This file is licensed under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
// Copyright (C) 2022-2025, Advanced Micro Devices, Inc.
//
//===----------------------------------------------------------------------===//

#define NOCPP

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "../aie_kernel_utils.h"
#include <aie_api/aie.hpp>

#define REL_WRITE 0
#define REL_READ 1

// N_ROWS: number of rows per FIFO element (compile-time constant).
// Set via -DN_ROWS=N. Defaults to 1 (single-row, original behavior).
#ifndef N_ROWS
#define N_ROWS 1
#endif

#ifdef SCALAR

const int32_t SMAX = 127;
const int32_t SMIN = 128;

#ifdef INT8_ACT
//*****************************************************************************
// conv2d 1x1 - scalar (single row)
// act: int8, wts: int8, out: int8
//*****************************************************************************
static void conv2dk1_i8_scalar_row(int8_t *input, int8_t *kernels,
                                   int8_t *output,
                                   const int32_t input_width,
                                   const int32_t input_channels,
                                   const int32_t output_channels,
                                   const int scale) {
  int x, ic, oc, ic8, oc8;
  for (oc = 0; oc < output_channels / 8; oc++) {
    for (x = 0; x < input_width; x++) { // col of output image
      for (oc8 = 0; oc8 < 8; oc8++) {
        int sum = 0;
        int sum_srs = 0;

        for (ic = 0; ic < input_channels / 8; ic++) {
          for (ic8 = 0; ic8 < 8; ic8++) {
            int val = input[(ic * input_width * 8) + (x * 8) + ic8];
            int k = kernels[(oc * (input_channels / 8) * 64) + (ic * 64) +
                            (ic8 * 8) + oc8];
            sum += val * k;
          }
        }

        sum_srs = (sum + (1 << (scale - 1))) >> scale;
        sum_srs = (sum_srs > SMAX) ? SMAX : (sum_srs < -SMIN) ? -SMIN : sum_srs;
        output[(oc * input_width * 8) + (x * 8) + oc8] = sum_srs;
      }
    }
  }
}
#endif // INT8_ACT

#else // Vector

#ifdef INT8_ACT

// NUM_ACC_COUNT controls the number of accumulators used in the inner loop.
// - NUM_ACC_COUNT=4: input_width must be a multiple of 32 (4*8). Best ILP.
// - NUM_ACC_COUNT=1: input_width must be a multiple of 8. Wider applicability.
// Set via compiler flag -DNUM_ACC_COUNT=N, defaults to 4.
#ifndef NUM_ACC_COUNT
#define NUM_ACC_COUNT 4
#endif

//*****************************************************************************
// conv2d 1x1 - vector (single row)
// act: int8, wts: int8, out: int8
//
// Assume IC >= 16 as that gives ideal inner loop schedule
//*****************************************************************************
static void conv2dk1_i8_vector_row(int8_t *input, int8_t *kernels,
                                   int8_t *output,
                                   const int32_t input_width,
                                   const int32_t input_channels,
                                   const int32_t output_channels,
                                   const int scale) {
  constexpr int NUM_ACC = NUM_ACC_COUNT;
  constexpr int MMUL_M = 8;
  constexpr int MMUL_K = 8;
  constexpr int MMUL_N = 8;
  constexpr int CHANNEL_FACTOR = MMUL_K;
  constexpr int MMUL_MK = MMUL_M * MMUL_K;
  constexpr int MMUL_KN = MMUL_K * MMUL_N;
  constexpr int MMUL_MN = MMUL_M * MMUL_N;

  using MMUL8x8x8 = aie::mmul<MMUL_M, MMUL_K, MMUL_N, int8, int8>;
  ::aie::set_saturation(aie::saturation_mode::saturate);
  ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

  int8_t *restrict out_ptr = output;

  const int scaleT = scale;

  MMUL8x8x8 acc_tmp[NUM_ACC];
  for (int x = 0; x < NUM_ACC; x++) {
    acc_tmp[x] = aie::zeros<acc32, MMUL_MN>();
  }

  const int iw = input_width;
  const int iw_partial = (input_width / MMUL_M) / NUM_ACC;

  // Requires: (input_width / MMUL_M) % NUM_ACC == 0
  // Requires: input_channels / CHANNEL_FACTOR > 2 (IC >= 24)
  const int iw_partial_rem = 0;

  int8_t *input_begin_ptr = input;

  if (iw_partial > 0) {

    for (int oc = 0; oc < (output_channels / CHANNEL_FACTOR); oc++) {
      for (int iw_partialc = 0; iw_partialc < iw_partial; iw_partialc++) {
        AIE_PREPARE_FOR_PIPELINING
        AIE_LOOP_MIN_ITERATION_COUNT(2)
        for (int ic = 0; ic < (input_channels / CHANNEL_FACTOR); ic++) {
          aie::vector<int8, MMUL_KN> in_b = aie::load_v<MMUL_KN>(kernels);
          kernels += MMUL_KN;

          for (int x = 0; x < NUM_ACC; x++) {
            aie::vector<int8, MMUL_MK> in_a = aie::load_v<MMUL_MK>(input);
            input += MMUL_MK;
            acc_tmp[x].mac(in_a, in_b);
          }
          input += (iw * CHANNEL_FACTOR) - MMUL_MK * NUM_ACC;
        }

        for (int xx = 0; xx < NUM_ACC; xx++) {
          aie::vector<int8, MMUL_MN> o1 = acc_tmp[xx].to_vector<int8>(scaleT);
          aie::store_v(out_ptr, o1);
          out_ptr += MMUL_MN;
          acc_tmp[xx] = aie::zeros<acc32, MMUL_MN>();
        }
        input -= (input_channels * iw) - MMUL_MK * NUM_ACC;
        kernels -= (input_channels / CHANNEL_FACTOR) * MMUL_KN;
      }
      input = input_begin_ptr;
      kernels += (input_channels / CHANNEL_FACTOR) * MMUL_KN;
      out_ptr += (iw_partial_rem * MMUL_MN);
    }

  } // if(iw_partial > 0)
}
#endif // INT8_ACT
#endif // Vector

//*****************************************************************************
// conv2d 1x1 wrappers — process N_ROWS rows per call
//*****************************************************************************
extern "C" {

#ifdef SCALAR

#ifdef INT8_ACT

void conv2dk1_i8(int8_t *input, int8_t *kernels, int8_t *output,
                 const int32_t input_width, const int32_t input_channels,
                 const int32_t output_channels, const int scale) {
  event0();
  // N_ROWS is a compile-time constant; the compiler fully unrolls this loop.
  for (int row = 0; row < N_ROWS; row++) {
    conv2dk1_i8_scalar_row(input + row * input_channels * input_width,
                           kernels,
                           output + row * output_channels * input_width,
                           input_width, input_channels, output_channels, scale);
  }
  event1();
}
#endif // INT8_ACT
#else  // Vector

#ifdef INT8_ACT

void conv2dk1_i8(int8_t *input, int8_t *kernels, int8_t *output,
                 const int32_t input_width, const int32_t input_channels,
                 const int32_t output_channels, const int scale) {
  event0();
  // N_ROWS is a compile-time constant; the compiler fully unrolls this loop.
  for (int row = 0; row < N_ROWS; row++) {
    conv2dk1_i8_vector_row(input + row * input_channels * input_width,
                           kernels,
                           output + row * output_channels * input_width,
                           input_width, input_channels, output_channels, scale);
  }
  event1();
}
#endif // INT8_ACT
#endif // Vector
} // extern "C"
