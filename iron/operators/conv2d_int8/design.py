# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_


def _factorize_tensor(total: int) -> tuple[int, int, int, int]:
    """Factor total elements into four BD dims (d3, d2, d1, d0).

    For int8 transfers, d0*1 bytes must be >= 4, so d0 >= 4.
    d0 must also be divisible by 4 for alignment.

    Returns (d3, d2, d1, d0) with d3*d2*d1*d0 == total.
    """
    _BD_WRAP_MAX = 64
    _D0_MAX = 1023
    _D12_MAX = 1023
    _D0_MIN = 4  # Minimum 4 bytes for int8 DMA

    d3 = min(total, _BD_WRAP_MAX)
    while d3 >= 1:
        if total % d3 == 0:
            rest = total // d3
            # Find largest d0 divisible by 4 that divides rest
            d0 = min(rest, _D0_MAX)
            while d0 % 4 != 0:
                d0 -= 1
            while d0 >= _D0_MIN:
                if rest % d0 == 0:
                    rest2 = rest // d0
                    d1 = min(rest2, _D12_MAX)
                    while d1 > 1 and rest2 % d1 != 0:
                        d1 -= 1
                    d2 = rest2 // d1
                    if d2 <= _D12_MAX:
                        return (d3, d2, d1, d0)
                d0 -= 4
        d3 -= 1

    raise ValueError(
        f"Cannot factorize total={total} into valid BD dims "
        f"(d3<={_BD_WRAP_MAX}, d0>={_D0_MIN} and div by 4, d1,d2<={_D12_MAX})"
    )


def my_conv2d_int8(
    dev,
    height,
    width,
    in_channels,
    out_channels,
    scale,
):
    """ObjectFIFO design for 1x1 int8 conv2d on NPU2.

    Data layout (tiled, groups of 8 channels):
      Input row:   [C_in/8, W, 8]   (int8)
      Weights:     [C_out/8, C_in/8, 8, 8]  (int8)
      Output row:  [C_out/8, W, 8]  (int8)

    The kernel processes one input row at a time: acquires weights once,
    then loops over height rows.
    """
    xfr_dtype = np.int8

    assert in_channels % 8 == 0, "in_channels must be a multiple of 8"
    assert out_channels % 8 == 0, "out_channels must be a multiple of 8"

    # Sizes for one row of data
    input_row_size = in_channels * width
    output_row_size = out_channels * width

    # Weight size: [OC/8, IC/8, 8, 8] = OC * IC
    weights_size = out_channels * in_channels

    # Total tensor sizes
    total_input_size = in_channels * height * width
    total_output_size = out_channels * height * width

    if dev == "npu":
        dev_ty = NPU1()
    else:
        dev_ty = NPU2()

    # Type definitions for ObjectFIFOs
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_row_size,), np.dtype[xfr_dtype]]
    weights_ty = np.ndarray[(weights_size,), np.dtype[xfr_dtype]]

    # L3 (DDR) tensor types for runtime sequence
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    weights_l3_ty = np.ndarray[(weights_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

    # Kernel declaration: conv2dk1_i8(input, weights, output, width, IC, OC, scale)
    conv2dk1_i8_kernel = Kernel(
        "conv2dk1_i8",
        "conv2dk1_i8.o",
        [
            input_row_ty,
            weights_ty,
            output_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # ObjectFIFOs
    in_fifo = ObjectFifo(input_row_ty, name="in_fifo", depth=2)
    wt_fifo = ObjectFifo(weights_ty, name="wt_fifo", depth=1)
    out_fifo = ObjectFifo(output_row_ty, name="out_fifo", depth=2)

    # Core function
    def core_fn(of_in, of_wt, of_out, kernel_fn):
        y_dim = height
        x_dim = width
        ci = in_channels
        co = out_channels
        sc = scale

        elem_wt = of_wt.acquire(1)
        for _ in range_(y_dim):
            elem_in = of_in.acquire(1)
            elem_out = of_out.acquire(1)
            kernel_fn(elem_in, elem_wt, elem_out, x_dim, ci, co, sc)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    # Worker
    worker = Worker(
        core_fn,
        [
            in_fifo.cons(),
            wt_fifo.cons(),
            out_fifo.prod(),
            conv2dk1_i8_kernel,
        ],
    )

    # Runtime sequence
    rt = Runtime()
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker)

        # Input TAP: contiguous
        in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input_size)
        rt.fill(
            in_fifo.prod(),
            I,
            TensorAccessPattern(
                (1, total_input_size),
                offset=0,
                sizes=[in_d3, in_d2, in_d1, in_d0],
                strides=[in_d2 * in_d1 * in_d0, in_d1 * in_d0, in_d0, 1],
            ),
        )

        # Weight TAP: contiguous
        wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(weights_size)
        rt.fill(
            wt_fifo.prod(),
            W,
            TensorAccessPattern(
                (1, weights_size),
                offset=0,
                sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                strides=[wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1],
            ),
        )

        # Output TAP: contiguous
        out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output_size)
        rt.drain(
            out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_size),
                offset=0,
                sizes=[out_d3, out_d2, out_d1, out_d0],
                strides=[out_d2 * out_d1 * out_d0, out_d1 * out_d0, out_d0, 1],
            ),
            wait=True,
        )

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())
