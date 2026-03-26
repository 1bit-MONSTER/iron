# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import argparse
import sys
from pathlib import Path

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_


def my_maxpool2d_int8(
    dev,
    height,
    width,
    channels,
    kernel_size,
    stride,
    padding,
    num_columns,
):
    """ObjectFIFO design for MaxPool2d on NPU2 with int8.

    Same strip-based approach as bf16: process one output row at a time.
    For each output row, the kernel receives one input strip
    (kernel_size rows of data as a single flat buffer) and produces one output row.
    """
    xfr_dtype = np.int8

    assert channels % 8 == 0, "channels must be a multiple of 8"
    assert stride == 1, "Only stride=1 is supported currently"

    padded_height = height + 2 * padding
    padded_width = width + 2 * padding
    out_height = (height + 2 * padding - kernel_size) // stride + 1
    out_width = (width + 2 * padding - kernel_size) // stride + 1

    # For each output row, we need kernel_size input rows as one contiguous strip
    input_strip_size = channels * padded_width * kernel_size
    output_row_size = channels * out_width

    # Total sizes
    total_input_size = channels * padded_height * padded_width
    total_output_size = channels * out_height * out_width

    # Row size in elements
    input_row_elems = channels * padded_width

    # Types
    input_strip_ty = np.ndarray[(input_strip_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_row_size,), np.dtype[xfr_dtype]]
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

    if dev == "npu":
        dev_ty = NPU1()
    else:
        dev_ty = NPU2()

    # Kernel: processes strip of kernel_size rows -> 1 output row
    maxpool_kernel = Kernel(
        "maxpool2d_5x5_i8_strip",
        "maxpool2d_i8.o",
        [input_strip_ty, output_row_ty, np.int32, np.int32, np.int32],
    )

    # ObjectFIFOs
    # For int8, element size is 1 byte (half of bf16), so L1 pressure is lower.
    strip_bytes = input_strip_size  # int8 = 1 byte
    in_depth = 1 if strip_bytes > 32768 else 2
    in_fifo = ObjectFifo(input_strip_ty, name="in_fifo", depth=in_depth)
    out_fifo = ObjectFifo(output_row_ty, name="out_fifo", depth=2)

    def core_fn(of_in, of_out, kernel_fn):
        ow = out_width
        ch = channels
        iw = padded_width

        for _ in range_(out_height):
            elem_in = of_in.acquire(1)
            elem_out = of_out.acquire(1)
            kernel_fn(elem_in, elem_out, ow, ch, iw)
            of_in.release(1)
            of_out.release(1)

    worker = Worker(
        core_fn,
        [in_fifo.cons(), out_fifo.prod(), maxpool_kernel],
    )

    # Input TAP: for each output row, send kernel_size consecutive input rows.
    # For int8, the innermost dimension must be >= 4 and divisible by 4.
    #
    # Layout per strip: [kernel_size, C/8, padded_width, 8] (contiguous)
    # The innermost contiguous chunk is one channel group's width data:
    #   padded_width * 8 elements (e.g., 12*8=96 for 8ch)
    #
    # 4D decomposition:
    #   d3 (innermost): padded_width * 8 elements per channel group row
    #   d2: C/8 channel groups per row
    #   d1: kernel_size rows per strip
    #   d0: out_height strips (sliding window advancement)
    cg_row_size = padded_width * 8  # one channel group's row data
    n_cg = channels // 8  # number of channel groups

    in_tap = TensorAccessPattern(
        (1, total_input_size),
        offset=0,
        sizes=[out_height, kernel_size, n_cg, cg_row_size],
        strides=[input_row_elems * stride, input_row_elems, cg_row_size, 1],
    )

    out_cg_row_size = out_width * 8
    out_tap = TensorAccessPattern(
        (1, total_output_size),
        offset=0,
        sizes=[1, 1, out_height * n_cg, out_cg_row_size],
        strides=[0, 0, out_cg_row_size, 1],
    )

    rt = Runtime()
    with rt.sequence(input_l3_ty, output_l3_ty) as (inp, out):
        rt.start(worker)
        tg = rt.task_group()
        rt.fill(in_fifo.prod(), inp, in_tap, task_group=tg)
        rt.drain(out_fifo.cons(), out, out_tap, wait=True, task_group=tg)
        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


if __name__ == "__main__":

    def str_to_device(device: str):
        if device == "npu":
            return NPU1()
        elif device == "npu2":
            return NPU2()
        else:
            raise ValueError(f"Device name {device} is unknown.")

    p = argparse.ArgumentParser()
    p.add_argument(
        "-d", "--dev", required=True, dest="device", help="AIE Device", type=str
    )
    p.add_argument("-H", "--height", required=True, type=int)
    p.add_argument("-W", "--width", required=True, type=int)
    p.add_argument("-C", "--channels", required=True, type=int)
    p.add_argument("--kernel-size", default=5, type=int)
    p.add_argument("--stride", default=1, type=int)
    p.add_argument("--padding", default=2, type=int)
    p.add_argument("--num-columns", default=1, type=int)
    p.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        help="Output file path for the generated MLIR module",
    )

    opts = p.parse_args(sys.argv[1:])

    module = my_maxpool2d_int8(
        opts.device,
        opts.height,
        opts.width,
        opts.channels,
        opts.kernel_size,
        opts.stride,
        opts.padding,
        opts.num_columns,
    )

    if opts.output_file_path:
        output_file_path = Path(opts.output_file_path)
        with open(output_file_path, "w") as f:
            f.write(str(module))
    else:
        print(module)
