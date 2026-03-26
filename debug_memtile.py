# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Test: use MemTile forwarding like upstream design."""

import numpy as np
import torch
from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU2
from aie.iron.controlflow import range_
from iron.common import (
    AIEContext, AIEOperatorBase, XclbinArtifact, InstsBinArtifact,
    KernelObjectArtifact, SourceArtifact, PythonGeneratedMLIRArtifact,
)
from iron.operators.conv2d_int8.op import nchw_to_tiled_int8, tiled_to_nchw_int8, weights_to_tiled_int8
from iron.operators.conv2d_int8.reference import conv2d_int8_reference
from pathlib import Path


def memtile_conv2d_int8(dev, height, width, in_channels, out_channels, scale, kernel_obj_name="conv2dk1_i8.o"):
    """1x1 int8 conv2d using MemTile forwarding (like upstream)."""
    xfr_dtype = np.int8
    input_row_size = in_channels * width
    buf_in_size = input_row_size * 2  # double-sized for MemTile
    output_row_size = out_channels * width
    buf_out_size = output_row_size * 2
    weights_size = out_channels * in_channels
    total_input_size = in_channels * height * width
    total_output_size = out_channels * height * width

    dev_ty = NPU2()

    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    buf_in_ty = np.ndarray[(buf_in_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_row_size,), np.dtype[xfr_dtype]]
    buf_out_ty = np.ndarray[(buf_out_size,), np.dtype[xfr_dtype]]
    weights_ty = np.ndarray[(weights_size,), np.dtype[xfr_dtype]]
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    weights_l3_ty = np.ndarray[(weights_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

    conv2dk1_i8_kernel = Kernel(
        "conv2dk1_i8", kernel_obj_name,
        [input_row_ty, weights_ty, output_row_ty, np.int32, np.int32, np.int32, np.int32],
    )

    # MemTile forwarding pattern (like upstream)
    in_l3l2 = ObjectFifo(buf_in_ty, name="in_l3l2")
    in_l2_ct = in_l3l2.cons().forward(obj_type=input_row_ty, name="in_l2_ct")

    wt_fifo = ObjectFifo(weights_ty, name="wt_fifo", depth=1)

    out_ct_l2 = ObjectFifo(output_row_ty, name="out_ct_l2")
    out_l2l3 = out_ct_l2.cons().forward(obj_type=buf_out_ty, name="out_l2l3")

    def core_fn(of_wt, of_in, of_out, kernel_fn):
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

    worker = Worker(core_fn, [wt_fifo.cons(), in_l2_ct.cons(), out_ct_l2.prod(), conv2dk1_i8_kernel])

    rt = Runtime()
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker)
        rt.fill(in_l3l2.prod(), I)
        rt.fill(wt_fifo.prod(), W)
        rt.drain(out_l2l3.cons(), O, wait=True)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


# Test setup
torch.manual_seed(42)
ic, oc, h, w, scale = 32, 32, 2, 32, 10

# Write design function to a temp file for the artifact system
import tempfile, textwrap
design_code = textwrap.dedent(f'''
import numpy as np
from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU2
from aie.iron.controlflow import range_

def memtile_conv2d(dev, height, width, in_channels, out_channels, scale, kernel_obj_name="conv2dk1_i8.o"):
    xfr_dtype = np.int8
    input_row_size = in_channels * width
    buf_in_size = input_row_size * 2
    output_row_size = out_channels * width
    buf_out_size = output_row_size * 2
    weights_size = out_channels * in_channels
    total_input_size = in_channels * height * width
    total_output_size = out_channels * height * width
    dev_ty = NPU2()
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    buf_in_ty = np.ndarray[(buf_in_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_row_size,), np.dtype[xfr_dtype]]
    buf_out_ty = np.ndarray[(buf_out_size,), np.dtype[xfr_dtype]]
    weights_ty = np.ndarray[(weights_size,), np.dtype[xfr_dtype]]
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    weights_l3_ty = np.ndarray[(weights_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]
    conv2dk1_i8_kernel = Kernel("conv2dk1_i8", kernel_obj_name,
        [input_row_ty, weights_ty, output_row_ty, np.int32, np.int32, np.int32, np.int32])
    in_l3l2 = ObjectFifo(buf_in_ty, name="in_l3l2")
    in_l2_ct = in_l3l2.cons().forward(obj_type=input_row_ty, name="in_l2_ct")
    wt_fifo = ObjectFifo(weights_ty, name="wt_fifo", depth=1)
    out_ct_l2 = ObjectFifo(output_row_ty, name="out_ct_l2")
    out_l2l3 = out_ct_l2.cons().forward(obj_type=buf_out_ty, name="out_l2l3")
    def core_fn(of_wt, of_in, of_out, kernel_fn):
        y_dim = height; x_dim = width; ci = in_channels; co = out_channels; sc = scale
        elem_wt = of_wt.acquire(1)
        for _ in range_(y_dim):
            elem_in = of_in.acquire(1)
            elem_out = of_out.acquire(1)
            kernel_fn(elem_in, elem_wt, elem_out, x_dim, ci, co, sc)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)
    worker = Worker(core_fn, [wt_fifo.cons(), in_l2_ct.cons(), out_ct_l2.prod(), conv2dk1_i8_kernel])
    rt = Runtime()
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker)
        rt.fill(in_l3l2.prod(), I)
        rt.fill(wt_fifo.prod(), W)
        rt.drain(out_l2l3.cons(), O, wait=True)
    return Program(dev_ty, rt).resolve_program(SequentialPlacer())
''')

# Generate MLIR
mlir = memtile_conv2d_int8("npu2", h, w, ic, oc, scale, "conv2dk1_i8.o")
print("Generated MLIR for memtile design (first 20 lines):")
for line in str(mlir).split('\n')[:20]:
    print(f"  {line}")

# Check buffer allocation
mlir_str = str(mlir)
print(f"\nFIFO sizes in MLIR:")
for line in mlir_str.split('\n'):
    if 'objectfifo' in line and 'memref' in line:
        print(f"  {line.strip()}")
