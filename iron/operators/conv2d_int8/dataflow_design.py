# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Dataflow designs for YOLOv8n backbone layer chaining.

These designs map multiple layers onto separate AIE cores within a single PDI,
with intermediate activations flowing core-to-core via ObjectFIFOs instead of
going through DDR. Only the initial input and final output touch DDR.

Step 1: L0 alone (8->16, k3s2, 640x640->320x320, fused SiLU)
Step 2: L0 -> L1 chain (eliminates one DDR round-trip)
Step 3+: Continue adding layers
"""

import numpy as np

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU2, Tile
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
    _D0_MIN = 4

    d3 = min(total, _BD_WRAP_MAX)
    while d3 >= 1:
        if total % d3 == 0:
            rest = total // d3
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


# ---------------------------------------------------------------------------
# Step 1: Single-layer dataflow baseline — L0 only
# ---------------------------------------------------------------------------


def my_dataflow_l0(
    dev,
    height,
    width,
    in_channels,
    out_channels,
    shift1,
    shift2,
):
    """Single-core dataflow design for L0: k3s2 conv+SiLU.

    Maps L0 (8->16, k3s2, 640x640->320x320) onto one AIE core.
    This is functionally identical to the existing my_conv2d_int8_k3_fused
    with num_columns=1, but uses the same dataflow infrastructure that
    will be extended for multi-layer chaining.

    Args:
        dev: Device type string.
        height: Input spatial height (640).
        width: Input spatial width (640).
        in_channels: Input channels (8).
        out_channels: Output channels (16).
        shift1: Dequantization shift.
        shift2: Requantization shift.
    """
    xfr_dtype = np.int8
    stride = 2

    assert in_channels % 8 == 0
    assert out_channels % 8 == 0
    assert height % 2 == 0
    assert width % 2 == 0

    out_h = height // 2
    out_w = width // 2

    input_row_size = in_channels * width
    output_row_size = out_channels * out_w
    k_elems = 9

    total_input = in_channels * height * width
    total_output = out_channels * out_h * out_w

    # Weight size: tiled weights + packed int32 bias
    wt_size = out_channels * in_channels * k_elems + out_channels * 4
    total_weights = wt_size

    # L1 budget check
    input_depth = 4
    phys_bufs = input_depth + 1
    l1_input = phys_bufs * input_row_size
    l1_wt = wt_size
    l1_output = 2 * output_row_size
    l1_total = 1040 + l1_input + l1_wt + l1_output
    assert l1_total <= 65536, (
        f"L0 L1 budget exceeded: {l1_total}B > 64KB. "
        f"input={l1_input}, wt={l1_wt}, output={l1_output}"
    )

    dev_ty = NPU2()

    # Types
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_row_size,), np.dtype[xfr_dtype]]
    wt_ty = np.ndarray[(wt_size,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_weights,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # Kernel
    kernel = Kernel(
        "conv2dk3s2_i8_silu",
        "conv2dk3_i8_silu.o",
        [
            input_row_ty,
            input_row_ty,
            input_row_ty,
            wt_ty,
            output_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # ObjectFIFOs
    in_fifo = ObjectFifo(input_row_ty, name="l0_in", depth=input_depth)
    wt_fifo = ObjectFifo(wt_ty, name="l0_wt", depth=1)
    out_fifo = ObjectFifo(output_row_ty, name="l0_out", depth=2)

    # Core function: stride-2 sliding window
    def core_fn_l0(of_in, of_wt, of_out, kernel_fn):
        x_dim = width
        ci = in_channels
        co = out_channels
        oh = out_h
        s1 = shift1
        s2 = shift2

        elem_wt = of_wt.acquire(1)

        # Top row: check=0
        elems = of_in.acquire(2)
        elem_out = of_out.acquire(1)
        kernel_fn(
            elems[0], elems[0], elems[1], elem_wt, elem_out,
            x_dim, ci, co, 0, s1, s2,
        )
        of_in.release(1)
        of_out.release(1)

        # Middle rows: check=1
        for _ in range_(oh - 1):
            elems = of_in.acquire(3)
            elem_out = of_out.acquire(1)
            kernel_fn(
                elems[0], elems[1], elems[2], elem_wt, elem_out,
                x_dim, ci, co, 1, s1, s2,
            )
            of_in.release(2)
            of_out.release(1)

        # Release last held row
        of_in.release(1)
        of_wt.release(1)

    # Worker
    worker = Worker(
        core_fn_l0,
        [in_fifo.cons(), wt_fifo.cons(), out_fifo.prod(), kernel],
        placement=Tile(0, 2),
    )

    # Runtime sequence
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker)

        tg = rt.task_group()

        # Fill input
        in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input)
        rt.fill(
            in_fifo.prod(),
            I,
            TensorAccessPattern(
                (1, total_input),
                offset=0,
                sizes=[in_d3, in_d2, in_d1, in_d0],
                strides=[in_d2 * in_d1 * in_d0, in_d1 * in_d0, in_d0, 1],
            ),
            task_group=tg,
        )

        # Fill weights
        wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_weights)
        rt.fill(
            wt_fifo.prod(),
            W,
            TensorAccessPattern(
                (1, total_weights),
                offset=0,
                sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                strides=[wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1],
            ),
            task_group=tg,
        )

        # Drain output
        out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output)
        rt.drain(
            out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output),
                offset=0,
                sizes=[out_d3, out_d2, out_d1, out_d0],
                strides=[out_d2 * out_d1 * out_d0, out_d1 * out_d0, out_d0, 1],
            ),
            wait=True,
            task_group=tg,
        )

        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


# ---------------------------------------------------------------------------
# Step 2: Two-layer chain — L0 -> L1
# ---------------------------------------------------------------------------


def my_dataflow_l0_l1(
    dev,
    # L0 params
    l0_height,
    l0_width,
    l0_ic,
    l0_oc,
    l0_shift1,
    l0_shift2,
    # L1 params
    l1_oc,
    l1_shift1,
    l1_shift2,
):
    """Two-core dataflow chain: L0 -> L1 via inter-core ObjectFIFO.

    L0: 8->16, k3s2, 640x640 -> 320x320 (fused SiLU)
    L1: 16->32, k3s2, 320x320 -> 160x160 (fused SiLU)

    Intermediate activations (16ch, 320x320) flow directly from Core0
    to Core1 — they never touch DDR. Only the initial input (8ch, 640x640)
    and final output (32ch, 160x160) touch DDR.

    Weight delivery: single DDR buffer, split at MemTile into wt0/wt1.

    DMA channel budget:
      ShimDMA: 2 out (input + weights), 1 in (output) -> 3 total, OK
      MemTile: 1 in (weights), 2 out (wt0 + wt1) -> 3 total, OK
      Core0 (Tile 0,2): 2 in (input + wt0), 1 out (inter) -> OK
      Core1 (Tile 0,3): 2 in (inter + wt1), 1 out (output) -> OK

    Args:
        dev: Device type string.
        l0_height, l0_width: L0 input spatial dims (640, 640).
        l0_ic, l0_oc: L0 channels (8, 16).
        l0_shift1, l0_shift2: L0 requantization params.
        l1_oc: L1 output channels (32).
        l1_shift1, l1_shift2: L1 requantization params.
    """
    xfr_dtype = np.int8
    stride = 2

    # L0 dims
    l0_out_h = l0_height // 2  # 320
    l0_out_w = l0_width // 2  # 320

    # L1 dims (input = L0 output)
    l1_ic = l0_oc  # 16
    l1_height = l0_out_h  # 320
    l1_width = l0_out_w  # 320
    l1_out_h = l1_height // 2  # 160
    l1_out_w = l1_width // 2  # 160

    # Row sizes
    l0_input_row = l0_ic * l0_width  # 8 * 640 = 5120
    inter_row = l0_oc * l0_out_w  # 16 * 320 = 5120
    l1_output_row = l1_oc * l1_out_w  # 32 * 160 = 5120

    # Weight sizes (with packed int32 bias)
    l0_wt_size = l0_oc * l0_ic * 9 + l0_oc * 4  # 16*8*9 + 16*4 = 1216
    l1_wt_size = l1_oc * l1_ic * 9 + l1_oc * 4  # 32*16*9 + 32*4 = 4736

    # Both weight FIFOs use the same element size (the max of the two).
    # This allows a single Kernel declaration (MLIR requires unique function
    # symbols). The kernel only reads ic*oc*9+oc*4 bytes based on runtime
    # params, so padding bytes in the smaller buffer are ignored.
    wt_fifo_size = max(l0_wt_size, l1_wt_size)
    total_wt_size = 2 * wt_fifo_size  # both padded to same size

    # Total tensor sizes
    total_input = l0_ic * l0_height * l0_width  # 8*640*640 = 3,276,800
    total_output = l1_oc * l1_out_h * l1_out_w  # 32*160*160 = 819,200

    # L1 budget checks (use padded weight size for worst case)
    l0_input_depth = 4
    l0_l1_budget = (
        1040
        + (l0_input_depth + 1) * l0_input_row  # input FIFO
        + wt_fifo_size  # weights (padded)
        + 2 * inter_row  # output/inter producer (depth=2)
    )
    assert l0_l1_budget <= 65536, (
        f"L0 core L1 budget exceeded: {l0_l1_budget}B. "
        f"input={5 * l0_input_row}, wt={wt_fifo_size}, inter_out={2 * inter_row}"
    )

    l1_input_depth = 4
    l1_l1_budget = (
        1040
        + (l1_input_depth + 1) * inter_row  # inter FIFO consumer
        + wt_fifo_size  # weights (padded)
        + 2 * l1_output_row  # output FIFO
    )
    assert l1_l1_budget <= 65536, (
        f"L1 core L1 budget exceeded: {l1_l1_budget}B. "
        f"inter_in={5 * inter_row}, wt={wt_fifo_size}, output={2 * l1_output_row}"
    )

    dev_ty = NPU2()

    # Types — use max row size for all activation types so a single kernel
    # declaration covers both layers.
    max_row = max(l0_input_row, inter_row, l1_output_row)
    row_ty = np.ndarray[(max_row,), np.dtype[xfr_dtype]]
    wt_ty = np.ndarray[(wt_fifo_size,), np.dtype[xfr_dtype]]
    wts_all_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # Single kernel declaration — shared by both workers.
    # The C function signature uses int8_t* pointers; MLIR memref sizes
    # just control buffer allocation, and both cores pass their FIFO
    # buffers (which are all max_row or wt_fifo_size elements).
    kernel = Kernel(
        "conv2dk3s2_i8_silu",
        "conv2dk3_i8_silu.o",
        [
            row_ty,
            row_ty,
            row_ty,
            wt_ty,
            row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # --- ObjectFIFOs ---

    # Input: DDR -> Core0 (actual element size may be <= max_row)
    in_fifo = ObjectFifo(row_ty, name="l0_in", depth=l0_input_depth)

    # Weights: DDR -> MemTile -> split -> Core0 + Core1
    wts_all_fifo = ObjectFifo(wts_all_ty, name="wts_all", depth=1)
    wt0_fifo, wt1_fifo = wts_all_fifo.cons().split(
        offsets=[0, wt_fifo_size],
        obj_types=[wt_ty, wt_ty],
        names=["wt_l0", "wt_l1"],
        depths=[1, 1],
        placement=Tile(0, 1),  # MemTile
    )

    # Inter-core: Core0 -> Core1 (L0 output -> L1 input)
    inter_fifo = ObjectFifo(row_ty, name="inter_01", depth=l1_input_depth)

    # Output: Core1 -> DDR
    out_fifo = ObjectFifo(row_ty, name="l1_out", depth=2)

    # --- Core functions ---

    # L0: stride-2 sliding window, produces inter rows
    def core_fn_l0(of_in, of_wt, of_inter, kernel_fn):
        x_dim = l0_width
        ci = l0_ic
        co = l0_oc
        oh = l0_out_h
        s1 = l0_shift1
        s2 = l0_shift2

        elem_wt = of_wt.acquire(1)

        # Top row: check=0
        elems = of_in.acquire(2)
        elem_out = of_inter.acquire(1)
        kernel_fn(
            elems[0], elems[0], elems[1], elem_wt, elem_out,
            x_dim, ci, co, 0, s1, s2,
        )
        of_in.release(1)
        of_inter.release(1)

        # Middle rows: check=1
        for _ in range_(oh - 1):
            elems = of_in.acquire(3)
            elem_out = of_inter.acquire(1)
            kernel_fn(
                elems[0], elems[1], elems[2], elem_wt, elem_out,
                x_dim, ci, co, 1, s1, s2,
            )
            of_in.release(2)
            of_inter.release(1)

        # Release last held row
        of_in.release(1)
        of_wt.release(1)

    # L1: stride-2 sliding window on inter, produces output rows
    def core_fn_l1(of_inter, of_wt, of_out, kernel_fn):
        x_dim = l1_width
        ci = l1_ic
        co = l1_oc
        oh = l1_out_h
        s1 = l1_shift1
        s2 = l1_shift2

        elem_wt = of_wt.acquire(1)

        # Top row: check=0
        elems = of_inter.acquire(2)
        elem_out = of_out.acquire(1)
        kernel_fn(
            elems[0], elems[0], elems[1], elem_wt, elem_out,
            x_dim, ci, co, 0, s1, s2,
        )
        of_inter.release(1)
        of_out.release(1)

        # Middle rows: check=1
        for _ in range_(oh - 1):
            elems = of_inter.acquire(3)
            elem_out = of_out.acquire(1)
            kernel_fn(
                elems[0], elems[1], elems[2], elem_wt, elem_out,
                x_dim, ci, co, 1, s1, s2,
            )
            of_inter.release(2)
            of_out.release(1)

        # Release last held row
        of_inter.release(1)
        of_wt.release(1)

    # --- Workers ---
    worker0 = Worker(
        core_fn_l0,
        [in_fifo.cons(), wt0_fifo.cons(), inter_fifo.prod(), kernel],
        placement=Tile(0, 2),
    )
    worker1 = Worker(
        core_fn_l1,
        [inter_fifo.cons(l1_input_depth), wt1_fifo.cons(), out_fifo.prod(), kernel],
        placement=Tile(0, 3),
    )

    # --- Runtime sequence ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W_buf, O):
        rt.start(worker0, worker1)

        tg = rt.task_group()

        # Fill input
        in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input)
        rt.fill(
            in_fifo.prod(),
            I,
            TensorAccessPattern(
                (1, total_input),
                offset=0,
                sizes=[in_d3, in_d2, in_d1, in_d0],
                strides=[in_d2 * in_d1 * in_d0, in_d1 * in_d0, in_d0, 1],
            ),
            task_group=tg,
        )

        # Fill weights (MemTile splits into wt0/wt1)
        wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt_size)
        rt.fill(
            wts_all_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_wt_size),
                offset=0,
                sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                strides=[wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1],
            ),
            task_group=tg,
        )

        # Drain output
        out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output)
        rt.drain(
            out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output),
                offset=0,
                sizes=[out_d3, out_d2, out_d1, out_d0],
                strides=[
                    out_d2 * out_d1 * out_d0,
                    out_d1 * out_d0,
                    out_d0,
                    1,
                ],
            ),
            wait=True,
            task_group=tg,
        )

        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())
