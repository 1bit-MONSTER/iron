# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Test: use simple rt.fill without TAPs."""

import numpy as np
import torch
from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU2
from aie.iron.controlflow import range_
from iron.common import AIEContext, AIEOperatorBase, XclbinArtifact, InstsBinArtifact, KernelObjectArtifact, SourceArtifact, PythonGeneratedMLIRArtifact
from iron.operators.conv2d_int8.op import nchw_to_tiled_int8, tiled_to_nchw_int8, weights_to_tiled_int8
from iron.operators.conv2d_int8.reference import conv2d_int8_reference
from pathlib import Path


def simple_conv2d_int8(dev, height, width, in_channels, out_channels, scale, kernel_obj_name="conv2dk1_i8.o"):
    """Same as my_conv2d_int8 but using simple rt.fill without TAPs."""
    xfr_dtype = np.int8
    input_row_size = in_channels * width
    output_row_size = out_channels * width
    weights_size = out_channels * in_channels
    total_input_size = in_channels * height * width
    total_output_size = out_channels * height * width

    dev_ty = NPU2()

    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_row_size,), np.dtype[xfr_dtype]]
    weights_ty = np.ndarray[(weights_size,), np.dtype[xfr_dtype]]
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    weights_l3_ty = np.ndarray[(weights_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

    conv2dk1_i8_kernel = Kernel(
        "conv2dk1_i8", kernel_obj_name,
        [input_row_ty, weights_ty, output_row_ty, np.int32, np.int32, np.int32, np.int32],
    )

    in_fifo = ObjectFifo(input_row_ty, name="in_fifo", depth=2)
    wt_fifo = ObjectFifo(weights_ty, name="wt_fifo", depth=1)
    out_fifo = ObjectFifo(output_row_ty, name="out_fifo", depth=2)

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

    worker = Worker(core_fn, [in_fifo.cons(), wt_fifo.cons(), out_fifo.prod(), conv2dk1_i8_kernel])

    rt = Runtime()
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker)
        # Simple fill without explicit TAPs
        rt.fill(in_fifo.prod(), I)
        rt.fill(wt_fifo.prod(), W)
        rt.drain(out_fifo.cons(), O, wait=True)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


# Test it
torch.manual_seed(42)
ic, oc, h, w = 32, 32, 1, 32
scale = 10

# Write the design to MLIR
mlir = simple_conv2d_int8("npu2", h, w, ic, oc, scale)
print(mlir)
