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


def my_upsample_int8(dev, height, width, channels, scale_factor, num_columns):
    """ObjectFIFO design for nearest-neighbor 2x upsampling on NPU with int8.

    Data layout (tiled, groups of 8 channels):
      Input row:  [C/8, W, 8]       -- channels * width elements
      Output row: [C/8, 2*W, 8]     -- channels * 2*width elements

    The design processes one input row at a time, producing two output rows
    (vertical duplication). The kernel handles horizontal duplication: each
    input pixel is duplicated to two adjacent output positions.
    """
    assert scale_factor == 2, "Only scale_factor=2 is supported"
    assert channels % 8 == 0, "channels must be a multiple of 8"

    xfr_dtype = np.int8

    out_height = height * scale_factor
    out_width = width * scale_factor

    # Row sizes in elements
    input_row_size = channels * width  # [C/8, W, 8] flattened
    output_row_size = channels * out_width  # [C/8, 2W, 8] flattened

    # Total tensor sizes
    total_input_size = channels * height * width
    total_output_size = channels * out_height * out_width

    # Type definitions for ObjectFIFOs
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_row_size,), np.dtype[xfr_dtype]]

    # L3 (DDR) tensor types
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

    if dev == "npu":
        dev_ty = NPU1()
    else:
        dev_ty = NPU2()

    # Kernel declaration
    upsample_kernel = Kernel(
        "upsample2x_row_i8",
        "upsample2x_i8.o",
        [input_row_ty, output_row_ty, np.int32, np.int32],
    )

    # ObjectFIFOs -- single column design
    in_fifo = ObjectFifo(input_row_ty, name="in_0", depth=2)
    out_fifo = ObjectFifo(output_row_ty, name="out_0", depth=2)

    # Core function: loop over input rows, produce 2 output rows per input row
    def core_fn(of_in, of_out, kernel_fn):
        y_dim = height
        w = width
        ch = channels

        for _ in range_(y_dim):
            elem_in = of_in.acquire(1)
            # Vertical duplication: call kernel twice for same input row
            for _ in range_(scale_factor):
                elem_out = of_out.acquire(1)
                kernel_fn(elem_in, elem_out, w, ch)
                of_out.release(1)
            of_in.release(1)

    # Worker
    worker = Worker(
        core_fn,
        [in_fifo.cons(), out_fifo.prod(), upsample_kernel],
    )

    # Input TAP: read entire input tensor contiguously
    in_tap = TensorAccessPattern(
        (1, total_input_size),
        offset=0,
        sizes=[1, 1, 1, total_input_size],
        strides=[0, 0, 0, 1],
    )

    # Output TAP: write entire output tensor contiguously
    out_tap = TensorAccessPattern(
        (1, total_output_size),
        offset=0,
        sizes=[1, 1, 1, total_output_size],
        strides=[0, 0, 0, 1],
    )

    # Runtime sequence
    rt = Runtime()
    with rt.sequence(input_l3_ty, output_l3_ty) as (inp, out):
        rt.start(worker)

        tg = rt.task_group()

        # Fill input FIFO
        rt.fill(in_fifo.prod(), inp, in_tap, task_group=tg)

        # Drain output FIFO
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
    p.add_argument("--scale-factor", default=2, type=int)
    p.add_argument("--num-columns", default=1, type=int)
    p.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        help="Output file path for the generated MLIR module",
    )

    opts = p.parse_args(sys.argv[1:])

    module = my_upsample_int8(
        opts.device,
        opts.height,
        opts.width,
        opts.channels,
        opts.scale_factor,
        opts.num_columns,
    )

    if opts.output_file_path:
        output_file_path = Path(opts.output_file_path)
        with open(output_file_path, "w") as f:
            f.write(str(module))
    else:
        print(module)
