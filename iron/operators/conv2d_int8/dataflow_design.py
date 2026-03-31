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


def _factorize_3d(total: int) -> tuple[int, int, int]:
    """Factor total into three BD dims (d2, d1, d0).

    Used when d3 is reserved for an outer repeat dimension.
    d0 >= 4, d0 % 4 == 0, all dims <= 1023.

    Returns (d2, d1, d0) with d2*d1*d0 == total.
    """
    _D_MAX = 1023
    _D0_MIN = 4

    d0 = min(total, _D_MAX)
    while d0 % 4 != 0:
        d0 -= 1
    while d0 >= _D0_MIN:
        if total % d0 == 0:
            rest = total // d0
            d1 = min(rest, _D_MAX)
            while d1 > 1 and rest % d1 != 0:
                d1 -= 1
            d2 = rest // d1
            if d2 <= _D_MAX:
                return (d2, d1, d0)
        d0 -= 4
    raise ValueError(
        f"Cannot factorize total={total} into 3 BD dims "
        f"(d0>={_D0_MIN} and div by 4, d1,d2<={_D_MAX})"
    )


def _compute_oc_streaming_params(
    in_channels, out_channels, width, stride, l1_limit=65536
):
    """Find the best oc_chunk for OC streaming that fits in L1.

    For a k3 fused conv (stride-2), calculates the largest oc_chunk
    (multiple of 8) where all buffers fit within l1_limit.

    Returns (oc_chunk, n_oc_groups, input_depth).
    Raises ValueError if no feasible configuration exists.
    """
    out_w = width if stride == 1 else width // 2
    k_elems = 9
    _BD_WRAP_MAX = 64

    for try_depth in [4, 3]:
        phys_bufs = try_depth + 1
        input_fbs = phys_bufs * in_channels * width
        avail = l1_limit - 1040 - input_fbs
        if avail <= 0:
            continue
        for try_oc in range(out_channels, 0, -8):
            if out_channels % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_bytes = try_oc * in_channels * k_elems + try_oc * 4
            out_bytes = 2 * try_oc * out_w
            if wt_bytes + out_bytes > avail:
                continue
            n_oc = out_channels // try_oc
            if n_oc > _BD_WRAP_MAX:
                continue
            return (try_oc, n_oc, try_depth)

    raise ValueError(
        f"k3 fused OC streaming infeasible: "
        f"in_channels={in_channels}, out_channels={out_channels}, "
        f"width={width}. Cannot satisfy L1 budget ({l1_limit}B)."
    )


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
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            s1,
            s2,
        )
        of_in.release(1)
        of_out.release(1)

        # Middle rows: check=1
        for _ in range_(oh - 1):
            elems = of_in.acquire(3)
            elem_out = of_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                s1,
                s2,
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

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # L0


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
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            s1,
            s2,
        )
        of_in.release(1)
        of_inter.release(1)

        # Middle rows: check=1
        for _ in range_(oh - 1):
            elems = of_in.acquire(3)
            elem_out = of_inter.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                s1,
                s2,
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
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            s1,
            s2,
        )
        of_inter.release(1)
        of_out.release(1)

        # Middle rows: check=1
        for _ in range_(oh - 1):
            elems = of_inter.acquire(3)
            elem_out = of_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                s1,
                s2,
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

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # L0->L1


# ---------------------------------------------------------------------------
# Conv -> SiLU dataflow: two-core pipeline with split kernels
#
# Core 0 runs non-fused conv2dk3_i8 (stride 1 or 2) producing int8 output.
# Core 1 runs bias_silu_i8 applying bias + SiLU activation.
# They are connected via an inter-core ObjectFIFO: one row at a time.
#
# This avoids the Peano codegen issue when fusing SiLU into the same
# compilation unit as the vectorized conv MMUL kernel.
# ---------------------------------------------------------------------------


def my_dataflow_conv_silu(
    dev,
    height,
    width,
    in_channels,
    out_channels,
    shift1,
    shift2,
    conv_scale,
    stride=1,
):
    """Two-core dataflow: conv_core -> FIFO -> silu_core.

    Core 0: non-fused conv2dk3_i8 (or conv2dk3s2_i8) with `conv_scale`
            as the requantization shift. Produces int8 output.
    Core 1: bias_silu_i8 -- adds bias (pre-scaled) and applies SiLU,
            then requantizes to int8.

    The conv uses `conv_scale` to shift the int32 accumulator to int8.
    The silu kernel treats the conv int8 output as dequantized values
    (at scale 2^(-conv_scale)), adds bias scaled by the same factor,
    applies SiLU, and requantizes with shift2.

    Args:
        dev: Device type string.
        height: Input spatial height.
        width: Input spatial width.
        in_channels: Input channels (multiple of 8).
        out_channels: Output channels (multiple of 8).
        shift1: Dequantization shift for bias_silu (= conv_scale).
        shift2: Requantization shift for bias_silu output (8.8 fixed-point).
        conv_scale: Right-shift for conv accumulator -> int8.
        stride: Convolution stride (1 or 2).
    """
    xfr_dtype = np.int8

    assert in_channels % 8 == 0
    assert out_channels % 8 == 0
    assert stride in (1, 2)
    if stride == 2:
        assert height % 2 == 0
        assert width % 2 == 0

    out_h = height if stride == 1 else height // 2
    out_w = width if stride == 1 else width // 2

    input_row_size = in_channels * width
    inter_row_size = out_channels * out_w  # conv output row = silu input row
    output_row_size = out_channels * out_w  # silu output row

    total_input = in_channels * height * width
    total_output = out_channels * out_h * out_w

    # Conv weights: tiled [OC/8, IC/8, 3, 3, 8, 8] -- no bias
    conv_wt_size = out_channels * in_channels * 9

    # Bias buffer: int32 per output channel, cast as int8 bytes
    bias_size = out_channels * 4  # int32 = 4 bytes each

    # Total weights buffer: conv weights + bias (as int8 bytes)
    total_weights = conv_wt_size + bias_size

    # --- L1 budget checks ---
    # Core 0 (conv): input_fifo + conv_wt_fifo + inter_fifo(producer)
    if stride == 1:
        conv_input_depth = 4  # 3-row window + prefetch
    else:
        conv_input_depth = 4

    conv_l1 = (
        1040
        + (conv_input_depth + 1) * input_row_size  # input FIFO
        + conv_wt_size  # weight FIFO (depth=1)
        + 2 * inter_row_size  # inter FIFO producer (depth=2)
    )
    assert conv_l1 <= 65536, (
        f"Conv core L1 budget exceeded: {conv_l1}B > 64KB. "
        f"input={(conv_input_depth + 1) * input_row_size}, "
        f"wt={conv_wt_size}, inter_out={2 * inter_row_size}"
    )

    # Core 1 (silu): inter_fifo(consumer) + bias_fifo + output_fifo
    silu_l1 = (
        1040
        + 2 * inter_row_size  # inter FIFO consumer (depth=2)
        + bias_size  # bias FIFO (depth=1)
        + 2 * output_row_size  # output FIFO producer (depth=2)
    )
    assert silu_l1 <= 65536, (
        f"SiLU core L1 budget exceeded: {silu_l1}B > 64KB. "
        f"inter_in={2 * inter_row_size}, bias={bias_size}, "
        f"output={2 * output_row_size}"
    )

    dev_ty = NPU2()

    # Types
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    inter_row_ty = np.ndarray[(inter_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_row_size,), np.dtype[xfr_dtype]]
    conv_wt_ty = np.ndarray[(conv_wt_size,), np.dtype[xfr_dtype]]
    bias_ty = np.ndarray[(bias_size,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_weights,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # Kernel declarations -- two separate kernels, two separate .o files
    if stride == 1:
        conv_kernel = Kernel(
            "conv2dk3_i8",
            "conv2dk3_i8.o",
            [
                input_row_ty,
                input_row_ty,
                input_row_ty,
                conv_wt_ty,
                inter_row_ty,
                np.int32,
                np.int32,
                np.int32,
                np.int32,
                np.int32,
            ],
        )
    else:
        conv_kernel = Kernel(
            "conv2dk3s2_i8",
            "conv2dk3_i8.o",
            [
                input_row_ty,
                input_row_ty,
                input_row_ty,
                conv_wt_ty,
                inter_row_ty,
                np.int32,
                np.int32,
                np.int32,
                np.int32,
                np.int32,
            ],
        )

    silu_kernel = Kernel(
        "bias_silu_i8",
        "bias_silu_i8.o",
        [
            inter_row_ty,
            bias_ty,
            output_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # --- ObjectFIFOs ---
    # Input: DDR -> Core0
    in_fifo = ObjectFifo(input_row_ty, name="conv_in", depth=conv_input_depth)

    # Conv weights: DDR -> Core0
    conv_wt_fifo = ObjectFifo(conv_wt_ty, name="conv_wt", depth=1)

    # Inter-core: Core0 (conv output) -> Core1 (silu input)
    inter_fifo = ObjectFifo(inter_row_ty, name="conv_to_silu", depth=2)

    # Bias: DDR -> Core1
    bias_fifo = ObjectFifo(bias_ty, name="silu_bias", depth=1)

    # Output: Core1 -> DDR
    out_fifo = ObjectFifo(output_row_ty, name="silu_out", depth=2)

    # --- Core functions ---

    if stride == 1:
        # Stride-1: output same spatial dims as input
        def core_fn_conv(of_in, of_wt, of_inter, kernel_fn):
            x_dim = width
            ci = in_channels
            co = out_channels
            sc = conv_scale
            y_dim = height

            elem_wt = of_wt.acquire(1)

            # Top row: check=0 (line0 is padding)
            elems = of_in.acquire(2)
            elem_out = of_inter.acquire(1)
            kernel_fn(
                elems[0],
                elems[0],
                elems[1],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                0,
                sc,
            )
            of_inter.release(1)

            # Middle rows: check=1
            for _ in range_(y_dim - 2):
                elems = of_in.acquire(3)
                elem_out = of_inter.acquire(1)
                kernel_fn(
                    elems[0],
                    elems[1],
                    elems[2],
                    elem_wt,
                    elem_out,
                    x_dim,
                    ci,
                    co,
                    1,
                    sc,
                )
                of_in.release(1)
                of_inter.release(1)

            # Bottom row: check=2 (line2 is padding)
            elems = of_in.acquire(2)
            elem_out = of_inter.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[1],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                2,
                sc,
            )
            of_in.release(2)
            of_inter.release(1)

            of_wt.release(1)

    else:
        # Stride-2: output spatial = input / 2
        def core_fn_conv(of_in, of_wt, of_inter, kernel_fn):
            x_dim = width
            ci = in_channels
            co = out_channels
            oh = out_h
            sc = conv_scale

            elem_wt = of_wt.acquire(1)

            # Top row: check=0
            elems = of_in.acquire(2)
            elem_out = of_inter.acquire(1)
            kernel_fn(
                elems[0],
                elems[0],
                elems[1],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                0,
                sc,
            )
            of_in.release(1)
            of_inter.release(1)

            # Middle rows: check=1
            for _ in range_(oh - 1):
                elems = of_in.acquire(3)
                elem_out = of_inter.acquire(1)
                kernel_fn(
                    elems[0],
                    elems[1],
                    elems[2],
                    elem_wt,
                    elem_out,
                    x_dim,
                    ci,
                    co,
                    1,
                    sc,
                )
                of_in.release(2)
                of_inter.release(1)

            # Release last held row
            of_in.release(1)
            of_wt.release(1)

    # SiLU core: processes one row at a time
    def core_fn_silu(of_inter, of_bias, of_out, kernel_fn):
        w = out_w
        ch = out_channels
        s1 = shift1
        s2 = shift2
        n_rows = out_h

        elem_bias = of_bias.acquire(1)

        for _ in range_(n_rows):
            elem_in = of_inter.acquire(1)
            elem_out = of_out.acquire(1)
            kernel_fn(elem_in, elem_bias, elem_out, w, ch, s1, s2)
            of_inter.release(1)
            of_out.release(1)

        of_bias.release(1)

    # --- Workers ---
    worker_conv = Worker(
        core_fn_conv,
        [
            in_fifo.cons(),
            conv_wt_fifo.cons(),
            inter_fifo.prod(),
            conv_kernel,
        ],
        placement=Tile(0, 2),
    )
    worker_silu = Worker(
        core_fn_silu,
        [
            inter_fifo.cons(),
            bias_fifo.cons(),
            out_fifo.prod(),
            silu_kernel,
        ],
        placement=Tile(0, 3),
    )

    # --- Runtime sequence ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker_conv, worker_silu)

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

        # Fill conv weights (first conv_wt_size bytes of W)
        wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(conv_wt_size)
        rt.fill(
            conv_wt_fifo.prod(),
            W,
            TensorAccessPattern(
                (1, total_weights),
                offset=0,
                sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                strides=[wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1],
            ),
            task_group=tg,
        )

        # Fill bias (last bias_size bytes of W)
        b_d3, b_d2, b_d1, b_d0 = _factorize_tensor(bias_size)
        rt.fill(
            bias_fifo.prod(),
            W,
            TensorAccessPattern(
                (1, total_weights),
                offset=conv_wt_size,
                sizes=[b_d3, b_d2, b_d1, b_d0],
                strides=[b_d2 * b_d1 * b_d0, b_d1 * b_d0, b_d0, 1],
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

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # conv_silu


# ---------------------------------------------------------------------------
# Step 3: Three-layer chain -- L0 -> L1 -> L2.cv1 (non-fused)
# ---------------------------------------------------------------------------


def my_dataflow_l0_l1_l2cv1(
    dev,
    # L0 params
    l0_height,
    l0_width,
    l0_ic,
    l0_oc,
    l0_scale,
    # L1 params
    l1_oc,
    l1_scale,
    # L2.cv1 params
    l2cv1_oc,
    l2cv1_scale,
):
    """Three-core dataflow chain: L0 -> L1 -> L2.cv1 (non-fused convolutions).

    L0: k3s2, l0_ic -> l0_oc, height/2 x width/2
    L1: k3s2, l0_oc -> l1_oc, height/4 x width/4
    L2.cv1: k1s1, l1_oc -> l2cv1_oc, height/4 x width/4

    Uses NON-FUSED vectorized conv kernels (conv2dk3s2_i8 and conv2dk1_i8).
    No SiLU, no bias -- just pure int8 convolutions with shift-based
    requantization. This validates the k3->k3->k1 dataflow architecture
    before adding activation functions.

    Weight delivery: single DDR buffer, split at MemTile into wt0/wt1/wt2.

    DMA channel budget per tile:
      Core0 (0,2): 2 in (input + wt0), 1 out (inter01) -> OK
      Core1 (0,3): 2 in (inter01 + wt1), 1 out (inter12) -> OK
      Core2 (0,4): 2 in (inter12 + wt2), 1 out (output) -> OK
      MemTile (0,1): 1 in (wts_all), 3 out (wt0+wt1+wt2) -> OK (6 avail)
      ShimDMA: 2 out (input + weights), 1 in (output) -> OK
    """
    xfr_dtype = np.int8

    # --- Dimension calculations ---
    l0_out_h = l0_height // 2
    l0_out_w = l0_width // 2

    l1_ic = l0_oc
    l1_height = l0_out_h
    l1_width = l0_out_w
    l1_out_h = l1_height // 2
    l1_out_w = l1_width // 2

    l2cv1_ic = l1_oc
    l2cv1_height = l1_out_h
    l2cv1_width = l1_out_w

    # --- Row sizes ---
    l0_input_row = l0_ic * l0_width
    inter01_row = l0_oc * l0_out_w
    inter12_row = l1_oc * l1_out_w
    l2cv1_output_row = l2cv1_oc * l2cv1_width

    # --- Weight sizes (non-fused: no bias) ---
    l0_wt_size = l0_oc * l0_ic * 9
    l1_wt_size = l1_oc * l1_ic * 9
    l2cv1_wt_size = l2cv1_oc * l2cv1_ic  # k1: OC * IC

    # Pad each weight slot to the maximum for uniform MemTile split.
    wt_slot_size = max(l0_wt_size, l1_wt_size, l2cv1_wt_size)
    total_wt_size = 3 * wt_slot_size

    # --- Total tensor sizes ---
    total_input = l0_ic * l0_height * l0_width
    total_output = l2cv1_oc * l2cv1_height * l2cv1_width

    # --- L1 budget checks ---
    l0_input_depth = 4
    l0_l1 = 1040 + (l0_input_depth + 1) * l0_input_row + wt_slot_size + 2 * inter01_row
    assert l0_l1 <= 65536, f"L0 L1 budget exceeded: {l0_l1}B"

    l1_input_depth = 4
    l1_l1 = 1040 + (l1_input_depth + 1) * inter01_row + wt_slot_size + 2 * inter12_row
    assert l1_l1 <= 65536, f"L1 L1 budget exceeded: {l1_l1}B"

    l2cv1_l1 = 1040 + 2 * inter12_row + wt_slot_size + 2 * l2cv1_output_row
    assert l2cv1_l1 <= 65536, f"L2.cv1 L1 budget exceeded: {l2cv1_l1}B"

    dev_ty = NPU2()

    # --- Types ---
    k3_row_size = max(l0_input_row, inter01_row, inter12_row, l2cv1_output_row)
    k3_row_ty = np.ndarray[(k3_row_size,), np.dtype[xfr_dtype]]

    wt_slot_ty = np.ndarray[(wt_slot_size,), np.dtype[xfr_dtype]]
    wts_all_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # --- Kernel declarations ---
    k3s2_kernel = Kernel(
        "conv2dk3s2_i8",
        "conv2dk3_i8.o",
        [
            k3_row_ty,
            k3_row_ty,
            k3_row_ty,
            wt_slot_ty,
            k3_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    k1_kernel = Kernel(
        "conv2dk1_i8",
        "conv2dk1_i8.o",
        [
            k3_row_ty,
            wt_slot_ty,
            k3_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # --- ObjectFIFOs ---
    in_fifo = ObjectFifo(k3_row_ty, name="l0_in", depth=l0_input_depth)

    wts_all_fifo = ObjectFifo(wts_all_ty, name="wts_all", depth=1)
    wt0_fifo, wt1_fifo, wt2_fifo = wts_all_fifo.cons().split(
        offsets=[0, wt_slot_size, 2 * wt_slot_size],
        obj_types=[wt_slot_ty, wt_slot_ty, wt_slot_ty],
        names=["wt_l0", "wt_l1", "wt_l2cv1"],
        depths=[1, 1, 1],
        placement=Tile(0, 1),
    )

    inter01_fifo = ObjectFifo(k3_row_ty, name="inter_01", depth=l1_input_depth)
    inter12_fifo = ObjectFifo(k3_row_ty, name="inter_12", depth=2)
    out_fifo = ObjectFifo(k3_row_ty, name="l2cv1_out", depth=2)

    # --- Core functions ---

    def core_fn_l0(of_in, of_wt, of_inter, kernel_fn):
        x_dim = l0_width
        ci = l0_ic
        co = l0_oc
        oh = l0_out_h
        sc = l0_scale

        elem_wt = of_wt.acquire(1)

        elems = of_in.acquire(2)
        elem_out = of_inter.acquire(1)
        kernel_fn(
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            sc,
        )
        of_in.release(1)
        of_inter.release(1)

        for _ in range_(oh - 1):
            elems = of_in.acquire(3)
            elem_out = of_inter.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                sc,
            )
            of_in.release(2)
            of_inter.release(1)

        of_in.release(1)
        of_wt.release(1)

    def core_fn_l1(of_inter_in, of_wt, of_inter_out, kernel_fn):
        x_dim = l1_width
        ci = l1_ic
        co = l1_oc
        oh = l1_out_h
        sc = l1_scale

        elem_wt = of_wt.acquire(1)

        elems = of_inter_in.acquire(2)
        elem_out = of_inter_out.acquire(1)
        kernel_fn(
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            sc,
        )
        of_inter_in.release(1)
        of_inter_out.release(1)

        for _ in range_(oh - 1):
            elems = of_inter_in.acquire(3)
            elem_out = of_inter_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                sc,
            )
            of_inter_in.release(2)
            of_inter_out.release(1)

        of_inter_in.release(1)
        of_wt.release(1)

    def core_fn_l2cv1(of_inter_in, of_wt, of_out, kernel_fn):
        x_dim = l2cv1_width
        ci = l2cv1_ic
        co = l2cv1_oc
        h = l2cv1_height
        sc = l2cv1_scale

        elem_wt = of_wt.acquire(1)

        for _ in range_(h):
            elem_in = of_inter_in.acquire(1)
            elem_out = of_out.acquire(1)
            kernel_fn(elem_in, elem_wt, elem_out, x_dim, ci, co, sc)
            of_inter_in.release(1)
            of_out.release(1)

        of_wt.release(1)

    # --- Workers ---
    worker0 = Worker(
        core_fn_l0,
        [
            in_fifo.cons(),
            wt0_fifo.cons(),
            inter01_fifo.prod(),
            k3s2_kernel,
        ],
        placement=Tile(0, 2),
    )
    worker1 = Worker(
        core_fn_l1,
        [
            inter01_fifo.cons(l1_input_depth),
            wt1_fifo.cons(),
            inter12_fifo.prod(),
            k3s2_kernel,
        ],
        placement=Tile(0, 3),
    )
    worker2 = Worker(
        core_fn_l2cv1,
        [inter12_fifo.cons(), wt2_fifo.cons(), out_fifo.prod(), k1_kernel],
        placement=Tile(0, 4),
    )

    # --- Runtime sequence ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (
        I,
        W_buf,
        O,
    ):
        rt.start(worker0, worker1, worker2)

        tg = rt.task_group()

        in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input)
        rt.fill(
            in_fifo.prod(),
            I,
            TensorAccessPattern(
                (1, total_input),
                offset=0,
                sizes=[in_d3, in_d2, in_d1, in_d0],
                strides=[
                    in_d2 * in_d1 * in_d0,
                    in_d1 * in_d0,
                    in_d0,
                    1,
                ],
            ),
            task_group=tg,
        )

        wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt_size)
        rt.fill(
            wts_all_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_wt_size),
                offset=0,
                sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                strides=[
                    wt_d2 * wt_d1 * wt_d0,
                    wt_d1 * wt_d0,
                    wt_d0,
                    1,
                ],
            ),
            task_group=tg,
        )

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


# ---------------------------------------------------------------------------
# Step 4: Three-layer downsample chain -- L0 -> L1 -> L3 (non-fused, all k3s2)
# ---------------------------------------------------------------------------


def my_dataflow_l0_l1_l3(
    dev,
    # L0 params
    l0_height,
    l0_width,
    l0_ic,
    l0_oc,
    l0_scale,
    # L1 params
    l1_oc,
    l1_scale,
    # L3 params
    l3_oc,
    l3_scale,
):
    """Three-core downsample chain: L0 -> L1 -> L3 (all k3s2, non-fused).

    Skips C2f blocks (L2, L4) and chains only the stride-2 downsample layers
    to extend the dataflow backbone through more spatial scales.

    L0: k3s2, l0_ic -> l0_oc, height/2 x width/2        (640->320)
    L1: k3s2, l0_oc -> l1_oc, height/4 x width/4        (320->160)
    L3: k3s2, l1_oc -> l3_oc, height/8 x width/8        (160->80)

    Uses NON-FUSED conv2dk3s2_i8 kernel. No SiLU, no bias.

    Weight delivery: single DDR buffer, split at MemTile into wt0/wt1/wt2.

    DMA channel budget per tile:
      Core0 (0,2): 2 in (input + wt0), 1 out (inter01) -> OK
      Core1 (0,3): 2 in (inter01 + wt1), 1 out (inter13) -> OK
      Core2 (0,4): 2 in (inter13 + wt2), 1 out (output) -> OK
      MemTile (0,1): 1 in (wts_all), 3 out (wt0+wt1+wt2) -> OK (6 avail)
      ShimDMA: 2 out (input + weights), 1 in (output) -> OK
    """
    xfr_dtype = np.int8

    # --- Dimension calculations ---
    l0_out_h = l0_height // 2
    l0_out_w = l0_width // 2

    l1_ic = l0_oc
    l1_height = l0_out_h
    l1_width = l0_out_w
    l1_out_h = l1_height // 2
    l1_out_w = l1_width // 2

    l3_ic = l1_oc
    l3_height = l1_out_h
    l3_width = l1_out_w
    l3_out_h = l3_height // 2
    l3_out_w = l3_width // 2

    # --- Row sizes ---
    l0_input_row = l0_ic * l0_width
    inter01_row = l0_oc * l0_out_w
    inter13_row = l1_oc * l1_out_w
    l3_output_row = l3_oc * l3_out_w

    # --- Weight sizes (non-fused: no bias) ---
    l0_wt_size = l0_oc * l0_ic * 9
    l1_wt_size = l1_oc * l1_ic * 9
    l3_wt_size = l3_oc * l3_ic * 9

    # Pad each weight slot to the maximum for uniform MemTile split.
    wt_slot_size = max(l0_wt_size, l1_wt_size, l3_wt_size)
    total_wt_size = 3 * wt_slot_size

    # --- Total tensor sizes ---
    total_input = l0_ic * l0_height * l0_width
    total_output = l3_oc * l3_out_h * l3_out_w

    # --- L1 budget checks ---
    l0_input_depth = 4
    l0_l1 = 1040 + (l0_input_depth + 1) * l0_input_row + wt_slot_size + 2 * inter01_row
    assert l0_l1 <= 65536, f"L0 L1 budget exceeded: {l0_l1}B"

    l1_input_depth = 4
    l1_l1 = 1040 + (l1_input_depth + 1) * inter01_row + wt_slot_size + 2 * inter13_row
    assert l1_l1 <= 65536, f"L1 L1 budget exceeded: {l1_l1}B"

    l3_input_depth = 4
    l3_l1 = 1040 + (l3_input_depth + 1) * inter13_row + wt_slot_size + 2 * l3_output_row
    assert l3_l1 <= 65536, f"L3 L1 budget exceeded: {l3_l1}B"

    dev_ty = NPU2()

    # --- Types ---
    # All row sizes happen to be equal for YOLOv8n dims (5120 each),
    # but compute the max to be safe for arbitrary params.
    max_row_size = max(l0_input_row, inter01_row, inter13_row, l3_output_row)
    row_ty = np.ndarray[(max_row_size,), np.dtype[xfr_dtype]]

    wt_slot_ty = np.ndarray[(wt_slot_size,), np.dtype[xfr_dtype]]
    wts_all_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # --- Kernel declaration ---
    # Single kernel shared by all three workers (all use conv2dk3s2_i8).
    k3s2_kernel = Kernel(
        "conv2dk3s2_i8",
        "conv2dk3_i8.o",
        [
            row_ty,
            row_ty,
            row_ty,
            wt_slot_ty,
            row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # --- ObjectFIFOs ---
    in_fifo = ObjectFifo(row_ty, name="l0_in", depth=l0_input_depth)

    wts_all_fifo = ObjectFifo(wts_all_ty, name="wts_all", depth=1)
    wt0_fifo, wt1_fifo, wt2_fifo = wts_all_fifo.cons().split(
        offsets=[0, wt_slot_size, 2 * wt_slot_size],
        obj_types=[wt_slot_ty, wt_slot_ty, wt_slot_ty],
        names=["wt_l0", "wt_l1", "wt_l3"],
        depths=[1, 1, 1],
        placement=Tile(0, 1),
    )

    inter01_fifo = ObjectFifo(row_ty, name="inter_01", depth=l1_input_depth)
    inter13_fifo = ObjectFifo(row_ty, name="inter_13", depth=l3_input_depth)
    out_fifo = ObjectFifo(row_ty, name="l3_out", depth=2)

    # --- Core functions ---

    def core_fn_l0(of_in, of_wt, of_inter, kernel_fn):
        x_dim = l0_width
        ci = l0_ic
        co = l0_oc
        oh = l0_out_h
        sc = l0_scale

        elem_wt = of_wt.acquire(1)

        elems = of_in.acquire(2)
        elem_out = of_inter.acquire(1)
        kernel_fn(
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            sc,
        )
        of_in.release(1)
        of_inter.release(1)

        for _ in range_(oh - 1):
            elems = of_in.acquire(3)
            elem_out = of_inter.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                sc,
            )
            of_in.release(2)
            of_inter.release(1)

        of_in.release(1)
        of_wt.release(1)

    def core_fn_l1(of_inter_in, of_wt, of_inter_out, kernel_fn):
        x_dim = l1_width
        ci = l1_ic
        co = l1_oc
        oh = l1_out_h
        sc = l1_scale

        elem_wt = of_wt.acquire(1)

        elems = of_inter_in.acquire(2)
        elem_out = of_inter_out.acquire(1)
        kernel_fn(
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            sc,
        )
        of_inter_in.release(1)
        of_inter_out.release(1)

        for _ in range_(oh - 1):
            elems = of_inter_in.acquire(3)
            elem_out = of_inter_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                sc,
            )
            of_inter_in.release(2)
            of_inter_out.release(1)

        of_inter_in.release(1)
        of_wt.release(1)

    def core_fn_l3(of_inter_in, of_wt, of_out, kernel_fn):
        x_dim = l3_width
        ci = l3_ic
        co = l3_oc
        oh = l3_out_h
        sc = l3_scale

        elem_wt = of_wt.acquire(1)

        elems = of_inter_in.acquire(2)
        elem_out = of_out.acquire(1)
        kernel_fn(
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            sc,
        )
        of_inter_in.release(1)
        of_out.release(1)

        for _ in range_(oh - 1):
            elems = of_inter_in.acquire(3)
            elem_out = of_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                sc,
            )
            of_inter_in.release(2)
            of_out.release(1)

        of_inter_in.release(1)
        of_wt.release(1)

    # --- Workers ---
    worker0 = Worker(
        core_fn_l0,
        [
            in_fifo.cons(),
            wt0_fifo.cons(),
            inter01_fifo.prod(),
            k3s2_kernel,
        ],
        placement=Tile(0, 2),
    )
    worker1 = Worker(
        core_fn_l1,
        [
            inter01_fifo.cons(l1_input_depth),
            wt1_fifo.cons(),
            inter13_fifo.prod(),
            k3s2_kernel,
        ],
        placement=Tile(0, 3),
    )
    worker2 = Worker(
        core_fn_l3,
        [
            inter13_fifo.cons(l3_input_depth),
            wt2_fifo.cons(),
            out_fifo.prod(),
            k3s2_kernel,
        ],
        placement=Tile(0, 4),
    )

    # --- Runtime sequence ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (
        I,
        W_buf,
        O,
    ):
        rt.start(worker0, worker1, worker2)

        tg = rt.task_group()

        in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input)
        rt.fill(
            in_fifo.prod(),
            I,
            TensorAccessPattern(
                (1, total_input),
                offset=0,
                sizes=[in_d3, in_d2, in_d1, in_d0],
                strides=[
                    in_d2 * in_d1 * in_d0,
                    in_d1 * in_d0,
                    in_d0,
                    1,
                ],
            ),
            task_group=tg,
        )

        wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt_size)
        rt.fill(
            wts_all_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_wt_size),
                offset=0,
                sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                strides=[
                    wt_d2 * wt_d1 * wt_d0,
                    wt_d1 * wt_d0,
                    wt_d0,
                    1,
                ],
            ),
            task_group=tg,
        )

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

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # L0->L1->L3


# ---------------------------------------------------------------------------
# CBS L0: Conv+Bias+SiLU — 2 cores (conv_core + silu_core), k3 stride-2
# ---------------------------------------------------------------------------


def my_dataflow_cbs_l0(
    dev,
    height,
    width,
    in_channels,
    out_channels,
    conv_scale,
    shift1,
    shift2,
):
    """Two-core CBS (Conv+Bias+SiLU) dataflow for layer 0.

    Core 0 (Tile 0,2): conv2dk3s2_i8 — k3 stride-2 conv, no fused SiLU.
    Core 1 (Tile 0,3): bias_silu_i8 — adds bias and applies SiLU activation.

    Connected via inter-core ObjectFIFO (one row of OC * out_w elements).
    Delegates to my_dataflow_conv_silu() with stride=2.

    Args:
        dev: Device type string.
        height: Input spatial height.
        width: Input spatial width.
        in_channels: Input channels (multiple of 8).
        out_channels: Output channels (multiple of 8).
        conv_scale: Right-shift for conv accumulator -> int8.
        shift1: Dequantization shift for bias_silu (= conv_scale).
        shift2: Requantization shift for bias_silu output (8.8 fixed-point).
    """
    return my_dataflow_conv_silu(
        dev,
        height,
        width,
        in_channels,
        out_channels,
        shift1,
        shift2,
        conv_scale,
        stride=2,
    )


# ---------------------------------------------------------------------------
# CBS L0 -> L1: 4-core pipeline (conv0 + silu0 + conv1 + silu1)
# ---------------------------------------------------------------------------


def my_dataflow_cbs_l0_l1(
    dev,
    # L0 params
    l0_height,
    l0_width,
    l0_ic,
    l0_oc,
    l0_conv_scale,
    l0_shift1,
    l0_shift2,
    # L1 params
    l1_oc,
    l1_conv_scale,
    l1_shift1,
    l1_shift2,
):
    """Four-core CBS dataflow chain: L0_conv -> L0_silu -> L1_conv -> L1_silu.

    L0 CBS: IC->l0_oc, k3s2 (split conv + SiLU)
    L1 CBS: l0_oc->l1_oc, k3s2 (split conv + SiLU)

    Intermediate activations flow core-to-core via ObjectFIFOs — they never
    touch DDR. Only the initial input and final output touch DDR.

    4 cores in a single column, chained:
      Core 0 (Tile 0,2): L0 conv2dk3s2_i8 (non-fused, produces int8)
      Core 1 (Tile 0,3): L0 bias_silu_i8 (bias + SiLU -> int8)
      Core 2 (Tile 0,4): L1 conv2dk3s2_i8 (non-fused, produces int8)
      Core 3 (Tile 0,5): L1 bias_silu_i8 (bias + SiLU -> int8)

    Weight delivery: single DDR buffer, split at MemTile into 4 sub-FIFOs
    (conv_wt0, bias0, conv_wt1, bias1).

    DMA channel budget:
      Core 0: 2 in (input + conv_wt0), 1 out (inter01) -> OK
      Core 1: 2 in (inter01 + bias0), 1 out (inter12) -> OK
      Core 2: 2 in (inter12 + conv_wt1), 1 out (inter23) -> OK
      Core 3: 2 in (inter23 + bias1), 1 out (output) -> OK
      MemTile: 1 in (wts_all), 4 out -> OK (6 available)
      ShimDMA: 2 out (input + weights), 1 in (output) -> OK
    """
    xfr_dtype = np.int8

    # --- Dimension calculations ---
    assert l0_ic % 8 == 0
    assert l0_oc % 8 == 0
    assert l0_height % 2 == 0
    assert l0_width % 2 == 0

    l0_out_h = l0_height // 2
    l0_out_w = l0_width // 2

    l1_ic = l0_oc
    l1_height = l0_out_h
    l1_width = l0_out_w
    l1_out_h = l1_height // 2
    l1_out_w = l1_width // 2

    assert l1_oc % 8 == 0
    assert l1_height % 2 == 0
    assert l1_width % 2 == 0

    # --- Row sizes ---
    l0_input_row = l0_ic * l0_width
    inter01_row = l0_oc * l0_out_w
    inter12_row = l0_oc * l0_out_w
    inter23_row = l1_oc * l1_out_w
    l1_output_row = l1_oc * l1_out_w

    # --- Weight sizes ---
    l0_conv_wt_size = l0_oc * l0_ic * 9
    l0_bias_size = l0_oc * 4
    l1_conv_wt_size = l1_oc * l1_ic * 9
    l1_bias_size = l1_oc * 4

    # Pad each weight slot to the maximum for uniform MemTile split
    wt_slot_size = max(l0_conv_wt_size, l0_bias_size, l1_conv_wt_size, l1_bias_size)
    total_wt_size = 4 * wt_slot_size

    # --- Total tensor sizes ---
    total_input = l0_ic * l0_height * l0_width
    total_output = l1_oc * l1_out_h * l1_out_w

    # --- L1 budget checks ---
    l0_input_depth = 4
    core0_l1 = (
        1040 + (l0_input_depth + 1) * l0_input_row + wt_slot_size + 2 * inter01_row
    )
    assert core0_l1 <= 65536, f"Core0 (L0 conv) L1 budget exceeded: {core0_l1}B > 64KB"

    core1_l1 = 1040 + 2 * inter01_row + wt_slot_size + 2 * inter12_row
    assert core1_l1 <= 65536, f"Core1 (L0 silu) L1 budget exceeded: {core1_l1}B > 64KB"

    l1_input_depth = 4
    core2_l1 = (
        1040 + (l1_input_depth + 1) * inter12_row + wt_slot_size + 2 * inter23_row
    )
    assert core2_l1 <= 65536, f"Core2 (L1 conv) L1 budget exceeded: {core2_l1}B > 64KB"

    core3_l1 = 1040 + 2 * inter23_row + wt_slot_size + 2 * l1_output_row
    assert core3_l1 <= 65536, f"Core3 (L1 silu) L1 budget exceeded: {core3_l1}B > 64KB"

    dev_ty = NPU2()

    # --- Types ---
    max_row = max(l0_input_row, inter01_row, inter12_row, inter23_row, l1_output_row)
    max_row_ty = np.ndarray[(max_row,), np.dtype[xfr_dtype]]
    wt_slot_ty = np.ndarray[(wt_slot_size,), np.dtype[xfr_dtype]]
    wts_all_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # --- Kernel declarations ---
    conv_kernel = Kernel(
        "conv2dk3s2_i8",
        "conv2dk3_i8.o",
        [
            max_row_ty,
            max_row_ty,
            max_row_ty,
            wt_slot_ty,
            max_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    silu_kernel = Kernel(
        "bias_silu_i8",
        "bias_silu_i8.o",
        [
            max_row_ty,
            wt_slot_ty,
            max_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # --- ObjectFIFOs ---
    in_fifo = ObjectFifo(max_row_ty, name="l0_in", depth=l0_input_depth)

    wts_all_fifo = ObjectFifo(wts_all_ty, name="wts_all", depth=1)
    wt0_fifo, bias0_fifo, wt1_fifo, bias1_fifo = wts_all_fifo.cons().split(
        offsets=[
            0,
            wt_slot_size,
            2 * wt_slot_size,
            3 * wt_slot_size,
        ],
        obj_types=[wt_slot_ty, wt_slot_ty, wt_slot_ty, wt_slot_ty],
        names=["wt_l0_conv", "wt_l0_bias", "wt_l1_conv", "wt_l1_bias"],
        depths=[1, 1, 1, 1],
        placement=Tile(0, 1),
    )

    inter01_fifo = ObjectFifo(max_row_ty, name="inter_01", depth=2)
    inter12_fifo = ObjectFifo(max_row_ty, name="inter_12", depth=l1_input_depth)
    inter23_fifo = ObjectFifo(max_row_ty, name="inter_23", depth=2)
    out_fifo = ObjectFifo(max_row_ty, name="l1_out", depth=2)

    # --- Core functions ---

    def core_fn_l0_conv(of_in, of_wt, of_inter, kernel_fn):
        x_dim = l0_width
        ci = l0_ic
        co = l0_oc
        oh = l0_out_h
        sc = l0_conv_scale

        elem_wt = of_wt.acquire(1)

        elems = of_in.acquire(2)
        elem_out = of_inter.acquire(1)
        kernel_fn(
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            sc,
        )
        of_in.release(1)
        of_inter.release(1)

        for _ in range_(oh - 1):
            elems = of_in.acquire(3)
            elem_out = of_inter.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                sc,
            )
            of_in.release(2)
            of_inter.release(1)

        of_in.release(1)
        of_wt.release(1)

    def core_fn_l0_silu(of_inter_in, of_bias, of_inter_out, kernel_fn):
        w = l0_out_w
        ch = l0_oc
        s1 = l0_shift1
        s2 = l0_shift2
        n_rows = l0_out_h

        elem_bias = of_bias.acquire(1)

        for _ in range_(n_rows):
            elem_in = of_inter_in.acquire(1)
            elem_out = of_inter_out.acquire(1)
            kernel_fn(elem_in, elem_bias, elem_out, w, ch, s1, s2)
            of_inter_in.release(1)
            of_inter_out.release(1)

        of_bias.release(1)

    def core_fn_l1_conv(of_inter_in, of_wt, of_inter_out, kernel_fn):
        x_dim = l1_width
        ci = l1_ic
        co = l1_oc
        oh = l1_out_h
        sc = l1_conv_scale

        elem_wt = of_wt.acquire(1)

        elems = of_inter_in.acquire(2)
        elem_out = of_inter_out.acquire(1)
        kernel_fn(
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            sc,
        )
        of_inter_in.release(1)
        of_inter_out.release(1)

        for _ in range_(oh - 1):
            elems = of_inter_in.acquire(3)
            elem_out = of_inter_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                sc,
            )
            of_inter_in.release(2)
            of_inter_out.release(1)

        of_inter_in.release(1)
        of_wt.release(1)

    def core_fn_l1_silu(of_inter_in, of_bias, of_out, kernel_fn):
        w = l1_out_w
        ch = l1_oc
        s1 = l1_shift1
        s2 = l1_shift2
        n_rows = l1_out_h

        elem_bias = of_bias.acquire(1)

        for _ in range_(n_rows):
            elem_in = of_inter_in.acquire(1)
            elem_out = of_out.acquire(1)
            kernel_fn(elem_in, elem_bias, elem_out, w, ch, s1, s2)
            of_inter_in.release(1)
            of_out.release(1)

        of_bias.release(1)

    # --- Workers ---
    worker0 = Worker(
        core_fn_l0_conv,
        [in_fifo.cons(), wt0_fifo.cons(), inter01_fifo.prod(), conv_kernel],
        placement=Tile(0, 2),
    )
    worker1 = Worker(
        core_fn_l0_silu,
        [
            inter01_fifo.cons(),
            bias0_fifo.cons(),
            inter12_fifo.prod(),
            silu_kernel,
        ],
        placement=Tile(0, 3),
    )
    worker2 = Worker(
        core_fn_l1_conv,
        [
            inter12_fifo.cons(l1_input_depth),
            wt1_fifo.cons(),
            inter23_fifo.prod(),
            conv_kernel,
        ],
        placement=Tile(0, 4),
    )
    worker3 = Worker(
        core_fn_l1_silu,
        [
            inter23_fifo.cons(),
            bias1_fifo.cons(),
            out_fifo.prod(),
            silu_kernel,
        ],
        placement=Tile(0, 5),
    )

    # --- Runtime sequence ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (
        I,
        W_buf,
        O,
    ):
        rt.start(worker0, worker1, worker2, worker3)

        tg = rt.task_group()

        in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input)
        rt.fill(
            in_fifo.prod(),
            I,
            TensorAccessPattern(
                (1, total_input),
                offset=0,
                sizes=[in_d3, in_d2, in_d1, in_d0],
                strides=[
                    in_d2 * in_d1 * in_d0,
                    in_d1 * in_d0,
                    in_d0,
                    1,
                ],
            ),
            task_group=tg,
        )

        wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt_size)
        rt.fill(
            wts_all_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_wt_size),
                offset=0,
                sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                strides=[
                    wt_d2 * wt_d1 * wt_d0,
                    wt_d1 * wt_d0,
                    wt_d0,
                    1,
                ],
            ),
            task_group=tg,
        )

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

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # CBS L0->L1


# ---------------------------------------------------------------------------
# Step 5: Four-layer chain -- L0 -> L1 -> L3 -> L4.cv1 (non-fused)
# ---------------------------------------------------------------------------


def my_dataflow_l0_l1_l3_l4cv1(
    dev,
    # L0 params
    l0_height,
    l0_width,
    l0_ic,
    l0_oc,
    l0_scale,
    # L1 params
    l1_oc,
    l1_scale,
    # L3 params
    l3_oc,
    l3_scale,
    # L4.cv1 params
    l4cv1_oc,
    l4cv1_scale,
):
    """Four-core chain: L0 -> L1 -> L3 -> L4.cv1 (non-fused).

    L0: k3s2, l0_ic -> l0_oc,  height/2 x width/2       (640->320)
    L1: k3s2, l0_oc -> l1_oc,  height/4 x width/4       (320->160)
    L3: k3s2, l1_oc -> l3_oc,  height/8 x width/8       (160->80)
    L4.cv1: k1s1, l3_oc -> l4cv1_oc, height/8 x width/8 (80->80)

    Uses 4 compute tiles in a single column: (0,2) through (0,5).
    Weight delivery: single DDR buffer, split at MemTile into 4 slots.

    DMA channel budget per tile:
      Core0 (0,2): 2 in (input + wt0), 1 out (inter01)       -> OK
      Core1 (0,3): 2 in (inter01 + wt1), 1 out (inter13)     -> OK
      Core2 (0,4): 2 in (inter13 + wt2), 1 out (inter3_4cv1) -> OK
      Core3 (0,5): 2 in (inter3_4cv1 + wt3), 1 out (output)  -> OK
      MemTile (0,1): 1 in (wts_all), 4 out -> OK (6 avail)
      ShimDMA: 2 out (input + weights), 1 in (output) -> OK
    """
    xfr_dtype = np.int8

    # --- Dimension calculations ---
    l0_out_h = l0_height // 2
    l0_out_w = l0_width // 2

    l1_ic = l0_oc
    l1_height = l0_out_h
    l1_width = l0_out_w
    l1_out_h = l1_height // 2
    l1_out_w = l1_width // 2

    l3_ic = l1_oc
    l3_height = l1_out_h
    l3_width = l1_out_w
    l3_out_h = l3_height // 2
    l3_out_w = l3_width // 2

    l4cv1_ic = l3_oc
    l4cv1_height = l3_out_h
    l4cv1_width = l3_out_w

    # --- Row sizes ---
    l0_input_row = l0_ic * l0_width
    inter01_row = l0_oc * l0_out_w
    inter13_row = l1_oc * l1_out_w
    inter3_4cv1_row = l3_oc * l3_out_w
    l4cv1_output_row = l4cv1_oc * l4cv1_width

    # --- Weight sizes (non-fused: no bias) ---
    l0_wt_size = l0_oc * l0_ic * 9
    l1_wt_size = l1_oc * l1_ic * 9
    l3_wt_size = l3_oc * l3_ic * 9
    l4cv1_wt_size = l4cv1_oc * l4cv1_ic  # k1: OC * IC

    # Pad each weight slot to the maximum for uniform MemTile split.
    wt_slot_size = max(l0_wt_size, l1_wt_size, l3_wt_size, l4cv1_wt_size)
    total_wt_size = 4 * wt_slot_size

    # --- Total tensor sizes ---
    total_input = l0_ic * l0_height * l0_width
    total_output = l4cv1_oc * l4cv1_height * l4cv1_width

    # --- L1 budget checks ---
    l0_input_depth = 4
    l0_l1 = 1040 + (l0_input_depth + 1) * l0_input_row + wt_slot_size + 2 * inter01_row
    assert l0_l1 <= 65536, f"L0 L1 budget exceeded: {l0_l1}B"

    l1_input_depth = 4
    l1_l1 = 1040 + (l1_input_depth + 1) * inter01_row + wt_slot_size + 2 * inter13_row
    assert l1_l1 <= 65536, f"L1 L1 budget exceeded: {l1_l1}B"

    l3_input_depth = 4
    l3_l1 = (
        1040 + (l3_input_depth + 1) * inter13_row + wt_slot_size + 2 * inter3_4cv1_row
    )
    assert l3_l1 <= 65536, f"L3 L1 budget exceeded: {l3_l1}B"

    l4cv1_l1 = (
        1040
        + 2 * inter3_4cv1_row  # k1: depth=2 input
        + wt_slot_size
        + 2 * l4cv1_output_row
    )
    assert l4cv1_l1 <= 65536, f"L4.cv1 L1 budget exceeded: {l4cv1_l1}B"

    dev_ty = NPU2()

    # --- Types ---
    max_row_size = max(
        l0_input_row,
        inter01_row,
        inter13_row,
        inter3_4cv1_row,
        l4cv1_output_row,
    )
    row_ty = np.ndarray[(max_row_size,), np.dtype[xfr_dtype]]

    wt_slot_ty = np.ndarray[(wt_slot_size,), np.dtype[xfr_dtype]]
    wts_all_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # --- Kernel declarations ---
    k3s2_kernel = Kernel(
        "conv2dk3s2_i8",
        "conv2dk3_i8.o",
        [
            row_ty,
            row_ty,
            row_ty,
            wt_slot_ty,
            row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    k1_kernel = Kernel(
        "conv2dk1_i8",
        "conv2dk1_i8.o",
        [
            row_ty,
            wt_slot_ty,
            row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # --- ObjectFIFOs ---
    in_fifo = ObjectFifo(row_ty, name="l0_in", depth=l0_input_depth)

    wts_all_fifo = ObjectFifo(wts_all_ty, name="wts_all", depth=1)
    wt0_fifo, wt1_fifo, wt2_fifo, wt3_fifo = wts_all_fifo.cons().split(
        offsets=[
            0,
            wt_slot_size,
            2 * wt_slot_size,
            3 * wt_slot_size,
        ],
        obj_types=[wt_slot_ty, wt_slot_ty, wt_slot_ty, wt_slot_ty],
        names=["wt_l0", "wt_l1", "wt_l3", "wt_l4cv1"],
        depths=[1, 1, 1, 1],
        placement=Tile(0, 1),
    )

    inter01_fifo = ObjectFifo(row_ty, name="inter_01", depth=l1_input_depth)
    inter13_fifo = ObjectFifo(row_ty, name="inter_13", depth=l3_input_depth)
    inter3_4cv1_fifo = ObjectFifo(row_ty, name="inter_3_4cv1", depth=2)
    out_fifo = ObjectFifo(row_ty, name="l4cv1_out", depth=2)

    # --- Core functions ---

    def core_fn_l0(of_in, of_wt, of_inter, kernel_fn):
        x_dim = l0_width
        ci = l0_ic
        co = l0_oc
        oh = l0_out_h
        sc = l0_scale

        elem_wt = of_wt.acquire(1)
        elems = of_in.acquire(2)
        elem_out = of_inter.acquire(1)
        kernel_fn(
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            sc,
        )
        of_in.release(1)
        of_inter.release(1)

        for _ in range_(oh - 1):
            elems = of_in.acquire(3)
            elem_out = of_inter.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                sc,
            )
            of_in.release(2)
            of_inter.release(1)

        of_in.release(1)
        of_wt.release(1)

    def core_fn_l1(of_inter_in, of_wt, of_inter_out, kernel_fn):
        x_dim = l1_width
        ci = l1_ic
        co = l1_oc
        oh = l1_out_h
        sc = l1_scale

        elem_wt = of_wt.acquire(1)
        elems = of_inter_in.acquire(2)
        elem_out = of_inter_out.acquire(1)
        kernel_fn(
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            sc,
        )
        of_inter_in.release(1)
        of_inter_out.release(1)

        for _ in range_(oh - 1):
            elems = of_inter_in.acquire(3)
            elem_out = of_inter_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                sc,
            )
            of_inter_in.release(2)
            of_inter_out.release(1)

        of_inter_in.release(1)
        of_wt.release(1)

    def core_fn_l3(of_inter_in, of_wt, of_inter_out, kernel_fn):
        x_dim = l3_width
        ci = l3_ic
        co = l3_oc
        oh = l3_out_h
        sc = l3_scale

        elem_wt = of_wt.acquire(1)
        elems = of_inter_in.acquire(2)
        elem_out = of_inter_out.acquire(1)
        kernel_fn(
            elems[0],
            elems[0],
            elems[1],
            elem_wt,
            elem_out,
            x_dim,
            ci,
            co,
            0,
            sc,
        )
        of_inter_in.release(1)
        of_inter_out.release(1)

        for _ in range_(oh - 1):
            elems = of_inter_in.acquire(3)
            elem_out = of_inter_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[1],
                elems[2],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                1,
                sc,
            )
            of_inter_in.release(2)
            of_inter_out.release(1)

        of_inter_in.release(1)
        of_wt.release(1)

    def core_fn_l4cv1(of_inter_in, of_wt, of_out, kernel_fn):
        x_dim = l4cv1_width
        ci = l4cv1_ic
        co = l4cv1_oc
        h = l4cv1_height
        sc = l4cv1_scale

        elem_wt = of_wt.acquire(1)
        for _ in range_(h):
            elem_in = of_inter_in.acquire(1)
            elem_out = of_out.acquire(1)
            kernel_fn(elem_in, elem_wt, elem_out, x_dim, ci, co, sc)
            of_inter_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    # --- Workers ---
    worker0 = Worker(
        core_fn_l0,
        [in_fifo.cons(), wt0_fifo.cons(), inter01_fifo.prod(), k3s2_kernel],
        placement=Tile(0, 2),
    )
    worker1 = Worker(
        core_fn_l1,
        [
            inter01_fifo.cons(l1_input_depth),
            wt1_fifo.cons(),
            inter13_fifo.prod(),
            k3s2_kernel,
        ],
        placement=Tile(0, 3),
    )
    worker2 = Worker(
        core_fn_l3,
        [
            inter13_fifo.cons(l3_input_depth),
            wt2_fifo.cons(),
            inter3_4cv1_fifo.prod(),
            k3s2_kernel,
        ],
        placement=Tile(0, 4),
    )
    worker3 = Worker(
        core_fn_l4cv1,
        [
            inter3_4cv1_fifo.cons(),
            wt3_fifo.cons(),
            out_fifo.prod(),
            k1_kernel,
        ],
        placement=Tile(0, 5),
    )

    # --- Runtime sequence ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (
        I,
        W_buf,
        O,
    ):
        rt.start(worker0, worker1, worker2, worker3)

        tg = rt.task_group()

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

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # L0->L1->L3->L4.cv1


# ---------------------------------------------------------------------------
# Step 6: Five-core fused downsample spine -- L0->L1->L3->L5->L7
# Each core runs fused conv+SiLU with vectorized MMUL + vec-16 hardware tanh.
# ---------------------------------------------------------------------------


def my_dataflow_spine_fused(
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
    # L3 params
    l3_oc,
    l3_shift1,
    l3_shift2,
    # L5 params
    l5_oc,
    l5_shift1,
    l5_shift2,
):
    """Four-core fused downsample spine: L0->L1->L3->L5.

    Each core runs fused conv+SiLU (conv2dk3s2_i8_silu) with vectorized
    MMUL + vec-16 hardware tanh. Intermediate activations flow core-to-core
    via ObjectFIFOs -- they never touch DDR.

    Uses 4 compute tiles in a single column: (0,2) through (0,5).
    NPU2 has 4 compute tiles per column (rows 2-5), so this is the
    maximum chain length in a single column.

    Weight delivery: single DDR buffer, split at MemTile into 4 slots.

    DMA channel budget per tile:
      Core0 (0,2): 2 in (input + wt0), 1 out (inter01) -> OK
      Core1 (0,3): 2 in (inter01 + wt1), 1 out (inter13) -> OK
      Core2 (0,4): 2 in (inter13 + wt2), 1 out (inter35) -> OK
      Core3 (0,5): 2 in (inter35 + wt3), 1 out (output) -> OK
      MemTile (0,1): 1 in (wts_all), 4 out -> OK (6 avail)
      ShimDMA: 2 out (input + weights), 1 in (output) -> OK
    """
    xfr_dtype = np.int8

    # --- Dimension calculations ---
    l0_out_h = l0_height // 2
    l0_out_w = l0_width // 2

    l1_ic = l0_oc
    l1_height = l0_out_h
    l1_width = l0_out_w
    l1_out_h = l1_height // 2
    l1_out_w = l1_width // 2

    l3_ic = l1_oc
    l3_height = l1_out_h
    l3_width = l1_out_w
    l3_out_h = l3_height // 2
    l3_out_w = l3_width // 2

    l5_ic = l3_oc
    l5_height = l3_out_h
    l5_width = l3_out_w
    l5_out_h = l5_height // 2
    l5_out_w = l5_width // 2

    # --- Row sizes ---
    l0_input_row = l0_ic * l0_width
    inter01_row = l0_oc * l0_out_w
    inter13_row = l1_oc * l1_out_w
    inter35_row = l3_oc * l3_out_w
    l5_output_row = l5_oc * l5_out_w

    # --- Weight sizes (fused: weights + int32 bias) ---
    l0_wt_size = l0_oc * l0_ic * 9 + l0_oc * 4
    l1_wt_size = l1_oc * l1_ic * 9 + l1_oc * 4
    l3_wt_size = l3_oc * l3_ic * 9 + l3_oc * 4
    l5_wt_size = l5_oc * l5_ic * 9 + l5_oc * 4

    # Pad all weight slots to the maximum for uniform MemTile split.
    # MLIR-AIE requires kernel func.call argument types to match exactly.
    wt_slot_size = max(l0_wt_size, l1_wt_size, l3_wt_size, l5_wt_size)
    total_wt_size = 4 * wt_slot_size

    # --- Total tensor sizes ---
    total_input = l0_ic * l0_height * l0_width
    total_output = l5_oc * l5_out_h * l5_out_w

    # --- L1 budget checks (use padded wt_slot_size for worst case) ---
    l0_input_depth = 4
    l0_l1 = 1040 + (l0_input_depth + 1) * l0_input_row + wt_slot_size + 2 * inter01_row
    assert l0_l1 <= 65536, f"L0 L1 budget exceeded: {l0_l1}B"

    l1_input_depth = 4
    l1_l1 = 1040 + (l1_input_depth + 1) * inter01_row + wt_slot_size + 2 * inter13_row
    assert l1_l1 <= 65536, f"L1 L1 budget exceeded: {l1_l1}B"

    l3_input_depth = 4
    l3_l1 = 1040 + (l3_input_depth + 1) * inter13_row + wt_slot_size + 2 * inter35_row
    assert l3_l1 <= 65536, f"L3 L1 budget exceeded: {l3_l1}B"

    l5_input_depth = 4
    l5_l1 = 1040 + (l5_input_depth + 1) * inter35_row + wt_slot_size + 2 * l5_output_row
    assert l5_l1 <= 65536, f"L5 L1 budget exceeded: {l5_l1}B"

    dev_ty = NPU2()

    # --- Types ---
    max_row_size = max(
        l0_input_row, inter01_row, inter13_row, inter35_row, l5_output_row
    )
    row_ty = np.ndarray[(max_row_size,), np.dtype[xfr_dtype]]
    wt_ty = np.ndarray[(wt_slot_size,), np.dtype[xfr_dtype]]
    wts_all_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # --- Kernel declaration (fused conv+SiLU, 11 args) ---
    k3s2_silu_kernel = Kernel(
        "conv2dk3s2_i8_silu",
        "conv2dk3_i8_silu.o",
        [
            row_ty,  # line0
            row_ty,  # line1
            row_ty,  # line2
            wt_ty,  # weights_and_bias
            row_ty,  # output
            np.int32,  # input_width
            np.int32,  # input_channels
            np.int32,  # output_channels
            np.int32,  # check
            np.int32,  # shift1
            np.int32,  # shift2
        ],
    )

    # --- ObjectFIFOs ---
    in_fifo = ObjectFifo(row_ty, name="l0_in", depth=l0_input_depth)

    wts_all_fifo = ObjectFifo(wts_all_ty, name="wts_all", depth=1)
    wt0_fifo, wt1_fifo, wt2_fifo, wt3_fifo = wts_all_fifo.cons().split(
        offsets=[0, wt_slot_size, 2 * wt_slot_size, 3 * wt_slot_size],
        obj_types=[wt_ty, wt_ty, wt_ty, wt_ty],
        names=["wt_l0", "wt_l1", "wt_l3", "wt_l5"],
        depths=[1, 1, 1, 1],
        placement=Tile(0, 1),
    )

    inter01_fifo = ObjectFifo(row_ty, name="inter_01", depth=l1_input_depth)
    inter13_fifo = ObjectFifo(row_ty, name="inter_13", depth=l3_input_depth)
    inter35_fifo = ObjectFifo(row_ty, name="inter_35", depth=l5_input_depth)
    out_fifo = ObjectFifo(row_ty, name="l5_out", depth=2)

    # --- Core functions (stride-2 sliding window with fused SiLU) ---

    def make_k3s2_silu_core_fn(in_width, in_channels, out_channels, out_h, s1, s2):
        """Create a stride-2 fused conv+SiLU core function."""

        def core_fn(of_in, of_wt, of_out, kernel_fn):
            x_dim = in_width
            ci = in_channels
            co = out_channels
            oh_val = out_h
            shift1_val = s1
            shift2_val = s2

            elem_wt = of_wt.acquire(1)

            # Top row: check=0
            elems = of_in.acquire(2)
            elem_out = of_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[0],
                elems[1],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                0,
                shift1_val,
                shift2_val,
            )
            of_in.release(1)
            of_out.release(1)

            # Middle rows: check=1
            for _ in range_(oh_val - 1):
                elems = of_in.acquire(3)
                elem_out = of_out.acquire(1)
                kernel_fn(
                    elems[0],
                    elems[1],
                    elems[2],
                    elem_wt,
                    elem_out,
                    x_dim,
                    ci,
                    co,
                    1,
                    shift1_val,
                    shift2_val,
                )
                of_in.release(2)
                of_out.release(1)

            # Release last held row
            of_in.release(1)
            of_wt.release(1)

        return core_fn

    core_fn_l0 = make_k3s2_silu_core_fn(
        l0_width, l0_ic, l0_oc, l0_out_h, l0_shift1, l0_shift2
    )
    core_fn_l1 = make_k3s2_silu_core_fn(
        l1_width, l1_ic, l1_oc, l1_out_h, l1_shift1, l1_shift2
    )
    core_fn_l3 = make_k3s2_silu_core_fn(
        l3_width, l3_ic, l3_oc, l3_out_h, l3_shift1, l3_shift2
    )
    core_fn_l5 = make_k3s2_silu_core_fn(
        l5_width, l5_ic, l5_oc, l5_out_h, l5_shift1, l5_shift2
    )

    # --- Workers ---
    worker0 = Worker(
        core_fn_l0,
        [in_fifo.cons(), wt0_fifo.cons(), inter01_fifo.prod(), k3s2_silu_kernel],
        placement=Tile(0, 2),
    )
    worker1 = Worker(
        core_fn_l1,
        [
            inter01_fifo.cons(l1_input_depth),
            wt1_fifo.cons(),
            inter13_fifo.prod(),
            k3s2_silu_kernel,
        ],
        placement=Tile(0, 3),
    )
    worker2 = Worker(
        core_fn_l3,
        [
            inter13_fifo.cons(l3_input_depth),
            wt2_fifo.cons(),
            inter35_fifo.prod(),
            k3s2_silu_kernel,
        ],
        placement=Tile(0, 4),
    )
    worker3 = Worker(
        core_fn_l5,
        [
            inter35_fifo.cons(l5_input_depth),
            wt3_fifo.cons(),
            out_fifo.prod(),
            k3s2_silu_kernel,
        ],
        placement=Tile(0, 5),
    )

    # --- Runtime sequence ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W_buf, O):
        rt.start(worker0, worker1, worker2, worker3)

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

        # Fill weights (MemTile splits into 5 slots)
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
                strides=[out_d2 * out_d1 * out_d0, out_d1 * out_d0, out_d0, 1],
            ),
            wait=True,
            task_group=tg,
        )

        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(
        SequentialPlacer()
    )  # spine_fused L0->L1->L3->L5


# ---------------------------------------------------------------------------
# C2f L2 simplified: cv1 -> channel split -> bottleneck -> cv2
#
# Only the bottleneck path (half2) feeds into cv2.
# half1 is drained to DDR (scratch region) to prevent deadlock.
# This validates the channel split mechanism at MemTile.
# ---------------------------------------------------------------------------


def my_dataflow_c2f_l2_simple(
    dev,
    height,
    width,
    in_channels,
    cv1_scale,
    bn_cv1_scale,
    bn_cv2_scale,
    cv2_scale,
):
    """Simplified C2f L2: cv1 -> split -> bottleneck path only -> cv2.

    Tests channel splitting without concat complexity. Only half2 (second
    16 channels from cv1 split) flows through the bottleneck to cv2.
    half1 (first 16 channels) is drained to a scratch region of the input
    buffer to prevent MemTile deadlock.

    Pipeline:
      input(32ch) -> cv1 k1 (32->32) -> split at MemTile ->
      half2(16ch) -> bn0.cv1 k3s1 (16->16) -> bn0.cv2 k3s1 (16->16) ->
      cv2 k1 (16->32) -> output(32ch)

    Core mapping (column 0):
      Core A (0,2): cv1 k1, 32->32ch
      Core B (0,3): bn0.cv1 k3s1, 16->16ch
      Core C (0,4): bn0.cv2 k3s1, 16->16ch
      Core D (0,5): cv2 k1, 16->32ch

    DMA channels per core: all <= 2 in + 1 out. OK.
    MemTile: wts split (1 in, 4 out) + cv1 split (1 in, 2 out).

    Args:
        dev: Device type string.
        height: Spatial height.
        width: Spatial width.
        in_channels: Input channels (32).
        cv1_scale: cv1 requantization shift.
        bn_cv1_scale: bn0.cv1 requantization shift.
        bn_cv2_scale: bn0.cv2 requantization shift.
        cv2_scale: cv2 requantization shift.
    """
    xfr_dtype = np.int8

    assert in_channels == 32
    cv1_oc = 32
    bn_ch = 16
    cv2_ic = 16
    cv2_oc = 32

    # Row sizes
    input_row = in_channels * width
    cv1_out_row = cv1_oc * width
    half_row = bn_ch * width
    cv2_out_row = cv2_oc * width

    # Weight sizes (non-fused, no bias)
    cv1_wt = cv1_oc * in_channels  # 1024
    bn_cv1_wt = bn_ch * bn_ch * 9  # 2304
    bn_cv2_wt = bn_ch * bn_ch * 9  # 2304
    cv2_wt = cv2_oc * cv2_ic  # 512

    wt_slot = max(cv1_wt, bn_cv1_wt, bn_cv2_wt, cv2_wt)
    total_wt = 4 * wt_slot

    total_input = in_channels * height * width
    total_output = cv2_oc * height * width
    half1_total = bn_ch * height * width

    # L1 budget checks
    bn_depth = 4

    coreA = 1040 + 2 * input_row + wt_slot + 2 * cv1_out_row
    assert coreA <= 65536, f"Core A L1: {coreA}B"

    coreB = 1040 + (bn_depth + 1) * half_row + wt_slot + 2 * half_row
    assert coreB <= 65536, f"Core B L1: {coreB}B"

    coreC = 1040 + (bn_depth + 1) * half_row + wt_slot + 2 * half_row
    assert coreC <= 65536, f"Core C L1: {coreC}B"

    coreD = 1040 + 2 * half_row + wt_slot + 2 * cv2_out_row
    assert coreD <= 65536, f"Core D L1: {coreD}B"

    dev_ty = NPU2()

    # --- Types ---
    max_row = max(input_row, cv1_out_row, half_row, cv2_out_row)
    max_row_ty = np.ndarray[(max_row,), np.dtype[xfr_dtype]]
    half_row_ty = np.ndarray[(half_row,), np.dtype[xfr_dtype]]
    wt_slot_ty = np.ndarray[(wt_slot,), np.dtype[xfr_dtype]]
    wts_all_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # --- Kernels ---
    # Single kernel declaration per function name (MLIR requires unique
    # symbols). Use max_row_ty for all buffer args -- the kernel only reads
    # ci*width bytes based on runtime params, so extra buffer space is unused.
    k1_kernel = Kernel(
        "conv2dk1_i8",
        "conv2dk1_i8.o",
        [
            max_row_ty,
            wt_slot_ty,
            max_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # Bottleneck k3 uses half_row_ty sized buffers (16ch).
    # Compiled from the same conv2dk3_i8.cc source but with the function
    # renamed via -Dconv2dk3_i8=conv2dk3_i8_bn to avoid MLIR symbol conflict.
    k3_bn_kernel = Kernel(
        "conv2dk3_i8_bn",
        "conv2dk3_i8_bn.o",
        [
            half_row_ty,
            half_row_ty,
            half_row_ty,
            wt_slot_ty,
            half_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # cv2 k1 reads half_row_ty input, writes max_row_ty output.
    # Renamed to avoid conflict with k1_kernel which has different arg types.
    k1_cv2_kernel = Kernel(
        "conv2dk1_i8_cv2",
        "conv2dk1_i8_cv2.o",
        [
            half_row_ty,
            wt_slot_ty,
            max_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # --- ObjectFIFOs ---
    in_fifo = ObjectFifo(max_row_ty, name="c2f_in", depth=2)

    wts_fifo = ObjectFifo(wts_all_ty, name="c2f_wts", depth=1)
    wt_cv1_f, wt_bn1_f, wt_bn2_f, wt_cv2_f = wts_fifo.cons().split(
        offsets=[0, wt_slot, 2 * wt_slot, 3 * wt_slot],
        obj_types=[wt_slot_ty] * 4,
        names=["wt_cv1", "wt_bn1", "wt_bn2", "wt_cv2"],
        depths=[1, 1, 1, 1],
        placement=Tile(0, 1),
    )

    # cv1 output -> MemTile for channel split
    cv1_out = ObjectFifo(max_row_ty, name="cv1_out", depth=2)

    # Channel split at MemTile: half_row_ty sub-FIFOs match bottleneck types
    half1_drain, half2_to_bn = cv1_out.cons().split(
        offsets=[0, half_row],
        obj_types=[half_row_ty, half_row_ty],
        names=["half1_drain", "half2_to_bn"],
        depths=[2, bn_depth],
        placement=Tile(0, 1),
    )

    # Bottleneck FIFOs (half_row_ty = 16ch * width)
    bn_inter = ObjectFifo(half_row_ty, name="bn_inter", depth=bn_depth)
    bn_out = ObjectFifo(half_row_ty, name="bn_out", depth=2)

    # Output
    out_fifo = ObjectFifo(max_row_ty, name="c2f_out", depth=2)

    # --- Core functions ---

    def core_fn_cv1(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = in_channels
        co = cv1_oc
        sc = cv1_scale
        elem_wt = of_wt.acquire(1)
        for _ in range_(height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, sc)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    def core_fn_bn_cv1(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = bn_ch
        co = bn_ch
        sc = bn_cv1_scale
        h = height
        elem_wt = of_wt.acquire(1)

        # Top row: check=0
        elems = of_in.acquire(2)
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo, w, ci, co, 0, sc)
        of_out.release(1)

        # Middle rows: check=1
        for _ in range_(h - 2):
            elems = of_in.acquire(3)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo, w, ci, co, 1, sc)
            of_in.release(1)
            of_out.release(1)

        # Bottom row: check=2
        elems = of_in.acquire(2)
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo, w, ci, co, 2, sc)
        of_in.release(2)
        of_out.release(1)

        of_wt.release(1)

    def core_fn_bn_cv2(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = bn_ch
        co = bn_ch
        sc = bn_cv2_scale
        h = height
        elem_wt = of_wt.acquire(1)

        elems = of_in.acquire(2)
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo, w, ci, co, 0, sc)
        of_out.release(1)

        for _ in range_(h - 2):
            elems = of_in.acquire(3)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo, w, ci, co, 1, sc)
            of_in.release(1)
            of_out.release(1)

        elems = of_in.acquire(2)
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo, w, ci, co, 2, sc)
        of_in.release(2)
        of_out.release(1)

        of_wt.release(1)

    def core_fn_cv2(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = cv2_ic
        co = cv2_oc
        sc = cv2_scale
        elem_wt = of_wt.acquire(1)
        for _ in range_(height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, sc)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    # --- Workers ---
    worker_cv1 = Worker(
        core_fn_cv1,
        [in_fifo.cons(), wt_cv1_f.cons(), cv1_out.prod(), k1_kernel],
        placement=Tile(0, 2),
    )
    worker_bn1 = Worker(
        core_fn_bn_cv1,
        [
            half2_to_bn.cons(bn_depth),
            wt_bn1_f.cons(),
            bn_inter.prod(),
            k3_bn_kernel,
        ],
        placement=Tile(0, 3),
    )
    worker_bn2 = Worker(
        core_fn_bn_cv2,
        [
            bn_inter.cons(bn_depth),
            wt_bn2_f.cons(),
            bn_out.prod(),
            k3_bn_kernel,
        ],
        placement=Tile(0, 4),
    )
    worker_cv2 = Worker(
        core_fn_cv2,
        [bn_out.cons(), wt_cv2_f.cons(), out_fifo.prod(), k1_cv2_kernel],
        placement=Tile(0, 5),
    )

    # --- Runtime ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker_cv1, worker_bn1, worker_bn2, worker_cv2)

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
                strides=[
                    in_d2 * in_d1 * in_d0,
                    in_d1 * in_d0,
                    in_d0,
                    1,
                ],
            ),
            task_group=tg,
        )

        # Fill weights
        wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt)
        rt.fill(
            wts_fifo.prod(),
            W,
            TensorAccessPattern(
                (1, total_wt),
                offset=0,
                sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                strides=[
                    wt_d2 * wt_d1 * wt_d0,
                    wt_d1 * wt_d0,
                    wt_d0,
                    1,
                ],
            ),
            task_group=tg,
        )

        # Drain half1 to scratch (prevents split deadlock).
        # Reuses the input buffer region as scratch since input is
        # already consumed by this point in the pipeline.
        h1_d3, h1_d2, h1_d1, h1_d0 = _factorize_tensor(half1_total)
        rt.drain(
            half1_drain.cons(),
            I,
            TensorAccessPattern(
                (1, total_input),
                offset=0,
                sizes=[h1_d3, h1_d2, h1_d1, h1_d0],
                strides=[
                    h1_d2 * h1_d1 * h1_d0,
                    h1_d1 * h1_d0,
                    h1_d0,
                    1,
                ],
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

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # c2f_l2_simple


# ---------------------------------------------------------------------------
# C2f L2 full: fused SiLU, 48ch concat [cv1_out(32) | bn0_out(16)],
# optional residual add.
#
# Builds on the simplified C2f by:
#   1. Replacing non-fused conv with fused conv+SiLU (bias packed in weights)
#   2. Adding 48ch concat for cv2 (was 16ch in simple)
#   3. Adding optional residual add (bn0.cv2 output += half2)
#
# Core mapping (5 cores, 2 columns):
#   Core A (0,2): cv1 k1 SiLU, 32->32ch
#   Core B (0,3): bn0.cv1 k3s1 SiLU, 16->16ch
#   Core C (0,4): bn0.cv2 k3s1 SiLU, 16->16ch
#   Core D (0,5): passthrough 32ch (cv1_fwd -> join input)
#   Core E (1,2): cv2 k1 SiLU, 48->32ch
#
# MemTile(0,1):
#   - wts_all split: 1 in -> 4 out (cv1, bn1, bn2, cv2)
#   - cv1_out split: 1 in -> 2 out (half2_to_bn, cv1_to_join)
#   Total: 2 in + 6 out = within MemTile DMA limits
#
# MemTile(1,1):
#   - join: cv1_fwd(32ch) + bn_out(16ch) -> cv2_in(48ch)
#
# The concat [half1|half2|bn0_out] = [cv1_out|bn0_out] since
# cv1_out already contains [half1|half2] in channel order.
# ---------------------------------------------------------------------------


def my_dataflow_c2f_l2_full(
    dev,
    height,
    width,
    in_channels,
    cv1_shift1,
    cv1_shift2,
    bn_cv1_shift1,
    bn_cv1_shift2,
    bn_cv2_shift1,
    bn_cv2_shift2,
    cv2_shift1,
    cv2_shift2,
):
    """Full C2f L2: fused SiLU on all 4 CBS, 48ch concat for cv2.

    Args:
        dev: Device type string.
        height: Spatial height (must be multiple of 8 for vec k3).
        width: Spatial width (must be multiple of 8 for vec k3).
        in_channels: Input channels (must be 32).
        cv1_shift1, cv1_shift2: cv1 fused SiLU params.
        bn_cv1_shift1, bn_cv1_shift2: bn0.cv1 fused SiLU params.
        bn_cv2_shift1, bn_cv2_shift2: bn0.cv2 fused SiLU params.
        cv2_shift1, cv2_shift2: cv2 fused SiLU params.
    """
    xfr_dtype = np.int8

    assert in_channels == 32
    cv1_oc = 32
    bn_ch = 16
    cv2_ic = 32  # 16ch half1 + 16ch bn0_out (joined at MemTile)
    cv2_oc = 32

    # Row sizes
    input_row = in_channels * width
    cv1_out_row = cv1_oc * width
    half_row = bn_ch * width
    cv2_in_row = cv2_ic * width
    cv2_out_row = cv2_oc * width

    # Weight sizes (fused: weights + int32 bias)
    cv1_wt = cv1_oc * in_channels + cv1_oc * 4
    bn_cv1_wt = bn_ch * bn_ch * 9 + bn_ch * 4
    bn_cv2_wt = bn_ch * bn_ch * 9 + bn_ch * 4
    cv2_wt = cv2_oc * cv2_ic + cv2_oc * 4

    wt_slot = max(cv1_wt, bn_cv1_wt, bn_cv2_wt, cv2_wt)
    total_wt = 4 * wt_slot

    total_input = in_channels * height * width
    total_output = cv2_oc * height * width

    bn_depth = 4

    # L1 budget checks
    coreA = 1040 + 2 * input_row + wt_slot + 2 * cv1_out_row
    assert coreA <= 65536, f"Core A L1: {coreA}B"

    coreB = 1040 + (bn_depth + 1) * half_row + wt_slot + 2 * half_row
    assert coreB <= 65536, f"Core B L1: {coreB}B"

    coreC = 1040 + (bn_depth + 1) * half_row + wt_slot + 2 * half_row
    assert coreC <= 65536, f"Core C L1: {coreC}B"

    coreD = 1040 + 2 * cv2_in_row + wt_slot + 2 * cv2_out_row
    assert coreD <= 65536, f"Core D (cv2) L1: {coreD}B"

    dev_ty = NPU2()

    # --- Types ---
    input_row_ty = np.ndarray[(input_row,), np.dtype[xfr_dtype]]
    cv1_out_row_ty = np.ndarray[(cv1_out_row,), np.dtype[xfr_dtype]]
    half_row_ty = np.ndarray[(half_row,), np.dtype[xfr_dtype]]
    cv2_in_row_ty = np.ndarray[(cv2_in_row,), np.dtype[xfr_dtype]]
    cv2_out_row_ty = np.ndarray[(cv2_out_row,), np.dtype[xfr_dtype]]
    wt_slot_ty = np.ndarray[(wt_slot,), np.dtype[xfr_dtype]]
    wts_all_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # --- Kernels ---
    k1_silu_kernel = Kernel(
        "conv2dk1_i8_silu",
        "conv2dk1_i8_silu.o",
        [
            input_row_ty,
            wt_slot_ty,
            cv1_out_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    k3_silu_bn_kernel = Kernel(
        "conv2dk3_i8_silu_bn",
        "conv2dk3_i8_silu_bn.o",
        [
            half_row_ty,
            half_row_ty,
            half_row_ty,
            wt_slot_ty,
            half_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    passthrough_kernel = Kernel(
        "passthrough_i8",
        "passthrough_i8.o",
        [
            half_row_ty,
            half_row_ty,
            np.int32,
        ],
    )

    k1_silu_cv2_kernel = Kernel(
        "conv2dk1_i8_silu_cv2",
        "conv2dk1_i8_silu_cv2.o",
        [
            cv2_in_row_ty,
            wt_slot_ty,
            cv2_out_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # --- ObjectFIFOs ---
    in_fifo = ObjectFifo(input_row_ty, name="c2f_in", depth=2)

    wts_fifo = ObjectFifo(wts_all_ty, name="c2f_wts", depth=1)
    wt_cv1_f, wt_bn1_f, wt_bn2_f, wt_cv2_f = wts_fifo.cons().split(
        offsets=[0, wt_slot, 2 * wt_slot, 3 * wt_slot],
        obj_types=[wt_slot_ty] * 4,
        names=["wt_cv1", "wt_bn1", "wt_bn2", "wt_cv2"],
        depths=[1, 1, 1, 1],
        placement=Tile(0, 1),
    )

    cv1_out = ObjectFifo(cv1_out_row_ty, name="cv1_out", depth=2)

    # Split cv1_out at MemTile(1,1) into equal halves:
    #   - half1_to_join: first 16ch (offset=0), feeds join for concat
    #   - half2_to_bn: second 16ch (offset=half_row), feeds bottleneck
    # Both sub-FIFOs have the same half_row_ty element type.
    # Placed at MemTile(1,1) to avoid overloading MemTile(0,1).
    half1_to_join, half2_to_bn = cv1_out.cons().split(
        offsets=[0, half_row],
        obj_types=[half_row_ty, half_row_ty],
        names=["half1_to_join", "half2_to_bn"],
        depths=[2, bn_depth],
        placement=Tile(1, 1),
    )

    bn_inter = ObjectFifo(half_row_ty, name="bn_inter", depth=bn_depth)

    # Join at MemTile(1,1): [half1(16ch) | bn0_out(16ch)] = 32ch
    # j_h1 is fed by half1_to_join from the split
    # j_bn is used directly as bn0.cv2's output FIFO (Core C writes to j_bn.prod())
    cv2_in = ObjectFifo(cv2_in_row_ty, name="cv2_in", depth=2)
    j_h1, j_bn = cv2_in.prod().join(
        offsets=[0, half_row],
        obj_types=[half_row_ty, half_row_ty],
        names=["j_h1", "j_bn"],
        placement=Tile(1, 1),
    )

    out_fifo = ObjectFifo(cv2_out_row_ty, name="c2f_out", depth=2)

    # --- Core functions ---

    def core_fn_cv1(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = in_channels
        co = cv1_oc
        s1 = cv1_shift1
        s2 = cv1_shift2
        elem_wt = of_wt.acquire(1)
        for _ in range_(height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, s1, s2)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    def core_fn_bn(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = bn_ch
        co = bn_ch
        h = height

        def _run_k3s1(s1, s2):
            elem_wt = of_wt.acquire(1)

            # Top row: check=0
            elems = of_in.acquire(2)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo, w, ci, co, 0, s1, s2)
            of_out.release(1)

            # Middle rows: check=1
            for _ in range_(h - 2):
                elems = of_in.acquire(3)
                eo = of_out.acquire(1)
                kernel_fn(
                    elems[0], elems[1], elems[2], elem_wt, eo, w, ci, co, 1, s1, s2
                )
                of_in.release(1)
                of_out.release(1)

            # Bottom row: check=2
            elems = of_in.acquire(2)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo, w, ci, co, 2, s1, s2)
            of_in.release(2)
            of_out.release(1)

            of_wt.release(1)

        _run_k3s1(bn_cv1_shift1, bn_cv1_shift2)

    def core_fn_bn_cv2(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = bn_ch
        co = bn_ch
        h = height
        s1 = bn_cv2_shift1
        s2 = bn_cv2_shift2
        elem_wt = of_wt.acquire(1)

        elems = of_in.acquire(2)
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo, w, ci, co, 0, s1, s2)
        of_out.release(1)

        for _ in range_(h - 2):
            elems = of_in.acquire(3)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo, w, ci, co, 1, s1, s2)
            of_in.release(1)
            of_out.release(1)

        elems = of_in.acquire(2)
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo, w, ci, co, 2, s1, s2)
        of_in.release(2)
        of_out.release(1)

        of_wt.release(1)

    def core_fn_passthrough(of_in, of_out, kernel_fn):
        sz = half_row
        for _ in range_(height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, eo, sz)
            of_in.release(1)
            of_out.release(1)

    def core_fn_cv2(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = cv2_ic
        co = cv2_oc
        s1 = cv2_shift1
        s2 = cv2_shift2
        elem_wt = of_wt.acquire(1)
        for _ in range_(height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, s1, s2)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    # --- Workers ---
    worker_cv1 = Worker(
        core_fn_cv1,
        [in_fifo.cons(), wt_cv1_f.cons(), cv1_out.prod(), k1_silu_kernel],
        placement=Tile(0, 2),
    )
    worker_bn1 = Worker(
        core_fn_bn,
        [
            half2_to_bn.cons(bn_depth),
            wt_bn1_f.cons(),
            bn_inter.prod(),
            k3_silu_bn_kernel,
        ],
        placement=Tile(0, 3),
    )
    worker_bn2 = Worker(
        core_fn_bn_cv2,
        [
            bn_inter.cons(bn_depth),
            wt_bn2_f.cons(),
            j_bn.prod(),
            k3_silu_bn_kernel,
        ],
        placement=Tile(0, 4),
    )
    worker_pass = Worker(
        core_fn_passthrough,
        [half1_to_join.cons(), j_h1.prod(), passthrough_kernel],
        placement=Tile(1, 2),
    )
    worker_cv2 = Worker(
        core_fn_cv2,
        [cv2_in.cons(), wt_cv2_f.cons(), out_fifo.prod(), k1_silu_cv2_kernel],
        placement=Tile(1, 3),
    )

    # --- Runtime ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker_cv1, worker_bn1, worker_bn2, worker_pass, worker_cv2)

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
        wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt)
        rt.fill(
            wts_fifo.prod(),
            W,
            TensorAccessPattern(
                (1, total_wt),
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

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # c2f_l2_full


# ---------------------------------------------------------------------------
# Step 7: Standalone fused k3s2 layer with OC streaming
# Enables layers where weights exceed 64KB L1 (e.g., L5: 64->128)
# ---------------------------------------------------------------------------


def my_dataflow_fused_oc_streaming(
    dev,
    height,
    width,
    in_channels,
    out_channels,
    shift1,
    shift2,
):
    """Single-core fused k3s2 conv+SiLU with OC streaming.

    When weights (OC * IC * 9 + OC * 4) exceed L1, splits output channels
    into chunks that fit. For each OC chunk the core:
      1. Acquires weight chunk from MemTile
      2. Processes ALL input rows (sliding window), producing output rows
         for this OC chunk's channels
      3. Releases weight chunk, acquires next

    The input DMA re-streams the full input n_oc_groups times via stride-0
    repeat. The output DMA uses strided writes to interleave OC chunks
    into the correct DDR positions.

    Args:
        dev: Device type string.
        height: Input spatial height.
        width: Input spatial width.
        in_channels: Input channels (multiple of 8).
        out_channels: Output channels (multiple of 8).
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
    k_elems = 9

    total_input = in_channels * height * width
    total_output = out_channels * out_h * out_w

    # --- Compute OC streaming parameters ---
    oc_chunk, n_oc_groups, input_depth = _compute_oc_streaming_params(
        in_channels, out_channels, width, stride
    )

    wt_chunk_elems = oc_chunk * in_channels * k_elems + oc_chunk * 4
    output_elem_size = oc_chunk * out_w
    total_weights = n_oc_groups * wt_chunk_elems

    dev_ty = NPU2()

    # Types
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_elem_size,), np.dtype[xfr_dtype]]
    wt_ty = np.ndarray[(wt_chunk_elems,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_weights,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # Kernel declaration (fused conv+SiLU, 11 args)
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
    in_fifo = ObjectFifo(input_row_ty, name="ocs_in", depth=input_depth)
    wt_fifo = ObjectFifo(wt_ty, name="ocs_wt", depth=1)
    out_fifo = ObjectFifo(output_row_ty, name="ocs_out", depth=2)

    # Core function: OC streaming with stride-2 sliding window
    def core_fn(of_in, of_wt, of_out, kernel_fn):
        x_dim = width
        ci = in_channels
        co = oc_chunk
        oh = out_h
        s1 = shift1
        s2 = shift2

        for _ in range_(n_oc_groups):
            elem_wt = of_wt.acquire(1)

            # Top row: check=0
            elems = of_in.acquire(2)
            elem_out = of_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[0],
                elems[1],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                0,
                s1,
                s2,
            )
            of_in.release(1)
            of_out.release(1)

            # Middle rows: check=1
            for _ in range_(oh - 1):
                elems = of_in.acquire(3)
                elem_out = of_out.acquire(1)
                kernel_fn(
                    elems[0],
                    elems[1],
                    elems[2],
                    elem_wt,
                    elem_out,
                    x_dim,
                    ci,
                    co,
                    1,
                    s1,
                    s2,
                )
                of_in.release(2)
                of_out.release(1)

            # Release last held row
            of_in.release(1)
            of_wt.release(1)

    # Worker
    worker = Worker(
        core_fn,
        [in_fifo.cons(), wt_fifo.cons(), out_fifo.prod(), kernel],
        placement=Tile(0, 2),
    )

    # --- Input TAP: re-stream n_oc_groups times via stride-0 ---
    in_d2, in_d1, in_d0 = _factorize_3d(total_input)
    in_tap = TensorAccessPattern(
        (1, total_input),
        offset=0,
        sizes=[n_oc_groups, in_d2, in_d1, in_d0],
        strides=[0, in_d1 * in_d0, in_d0, 1],
    )

    # --- Weight TAP: contiguous read of all n_oc_groups weight chunks ---
    wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_weights)
    wt_tap = TensorAccessPattern(
        (1, total_weights),
        offset=0,
        sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
        strides=[wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1],
    )

    # --- Output TAP: strided drain to interleave OC chunks ---
    # Each output element is oc_chunk * out_w bytes.
    # For OC group g, row r: DDR offset = r * OC * out_w + g * oc_chunk * out_w
    output_row_total = out_channels * out_w
    pe_d0 = min(output_elem_size, 1023)
    while pe_d0 % 4 != 0:
        pe_d0 -= 1
    while pe_d0 >= 4:
        if output_elem_size % pe_d0 == 0:
            break
        pe_d0 -= 4
    pe_d1 = output_elem_size // pe_d0

    out_tap = TensorAccessPattern(
        (1, total_output),
        offset=0,
        sizes=[n_oc_groups, out_h, pe_d1, pe_d0],
        strides=[oc_chunk * out_w, output_row_total, pe_d0, 1],
    )

    # --- Runtime sequence ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker)

        tg = rt.task_group()

        rt.fill(in_fifo.prod(), I, in_tap, task_group=tg)
        rt.fill(wt_fifo.prod(), W, wt_tap, task_group=tg)
        rt.drain(out_fifo.cons(), O, out_tap, wait=True, task_group=tg)

        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(
        SequentialPlacer()
    )  # oc_streaming standalone


# ---------------------------------------------------------------------------
# Step 8: Five-layer fused downsample spine with OC streaming
# L0->L1->L3 pipeline to DDR, then L5 (OC streaming), then L7 (OC streaming)
# ---------------------------------------------------------------------------


def my_dataflow_spine_5layer(
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
    # L3 params
    l3_oc,
    l3_shift1,
    l3_shift2,
    # L5 params
    l5_oc,
    l5_shift1,
    l5_shift2,
    # L7 params
    l7_oc,
    l7_shift1,
    l7_shift2,
):
    """Five-layer fused downsample spine: L0->L1->L3->L5->L7.

    L0-L3 are pipelined core-to-core (weights fit in L1).
    L5 and L7 use OC streaming (weights exceed L1).

    The design breaks into three sequential phases within one PDI:
      Phase 1: L0->L1->L3 pipeline, L3 output to DDR scratch
      Phase 2: L5 reads L3 output from DDR (re-streamed for OC groups),
               writes L5 output to DDR scratch
      Phase 3: L7 reads L5 output from DDR (re-streamed for OC groups),
               writes final output

    This eliminates 2 DDR round-trips (L0->L1, L1->L3) vs. fully
    sequential execution.

    Column 0: L0 (0,2), L1 (0,3), L3 (0,4)
    Column 1: L5 (1,2), L7 (1,3)

    Weight delivery:
      Col 0: single DDR buffer -> MemTile(0,1) split -> wt0/wt1/wt2
      Col 1: separate DDR fills for L5 and L7 weight streams

    Runtime buffer layout:
      Input:   [L0 input]
      Weights: [col0_wts (3 padded slots) | L5 wt chunks | L7 wt chunks]
      Output:  [L7 final output | L3->L5 scratch | L5->L7 scratch]
    """
    xfr_dtype = np.int8

    # --- Dimension calculations ---
    l0_out_h = l0_height // 2
    l0_out_w = l0_width // 2

    l1_ic = l0_oc
    l1_height = l0_out_h
    l1_width = l0_out_w
    l1_out_h = l1_height // 2
    l1_out_w = l1_width // 2

    l3_ic = l1_oc
    l3_height = l1_out_h
    l3_width = l1_out_w
    l3_out_h = l3_height // 2
    l3_out_w = l3_width // 2

    l5_ic = l3_oc
    l5_height = l3_out_h
    l5_width = l3_out_w
    l5_out_h = l5_height // 2
    l5_out_w = l5_width // 2

    l7_ic = l5_oc
    l7_height = l5_out_h
    l7_width = l5_out_w
    l7_out_h = l7_height // 2
    l7_out_w = l7_width // 2

    # --- Row sizes ---
    l0_input_row = l0_ic * l0_width
    inter01_row = l0_oc * l0_out_w
    inter13_row = l1_oc * l1_out_w
    inter35_row = l3_oc * l3_out_w

    # --- Column 0 weight sizes (fused: weights + int32 bias) ---
    l0_wt_size = l0_oc * l0_ic * 9 + l0_oc * 4
    l1_wt_size = l1_oc * l1_ic * 9 + l1_oc * 4
    l3_wt_size = l3_oc * l3_ic * 9 + l3_oc * 4
    col0_wt_slot = max(l0_wt_size, l1_wt_size, l3_wt_size)
    col0_total_wt = 3 * col0_wt_slot

    # --- Column 1: OC streaming params for L5 and L7 ---
    l5_oc_chunk, l5_n_oc_groups, l5_input_depth = _compute_oc_streaming_params(
        l5_ic, l5_oc, l5_width, 2
    )
    l7_oc_chunk, l7_n_oc_groups, l7_input_depth = _compute_oc_streaming_params(
        l7_ic, l7_oc, l7_width, 2
    )

    l5_wt_chunk = l5_oc_chunk * l5_ic * 9 + l5_oc_chunk * 4
    l5_total_wt = l5_n_oc_groups * l5_wt_chunk
    l5_output_elem = l5_oc_chunk * l5_out_w

    l7_wt_chunk = l7_oc_chunk * l7_ic * 9 + l7_oc_chunk * 4
    l7_total_wt = l7_n_oc_groups * l7_wt_chunk
    l7_output_elem = l7_oc_chunk * l7_out_w

    # --- L1 budget checks for column 0 ---
    l0_input_depth = 4
    l0_l1 = 1040 + (l0_input_depth + 1) * l0_input_row + col0_wt_slot + 2 * inter01_row
    assert l0_l1 <= 65536, f"L0 L1 budget exceeded: {l0_l1}B"

    l1_input_depth = 4
    l1_l1 = 1040 + (l1_input_depth + 1) * inter01_row + col0_wt_slot + 2 * inter13_row
    assert l1_l1 <= 65536, f"L1 L1 budget exceeded: {l1_l1}B"

    l3_input_depth = 4
    l3_l1 = 1040 + (l3_input_depth + 1) * inter13_row + col0_wt_slot + 2 * inter35_row
    assert l3_l1 <= 65536, f"L3 L1 budget exceeded: {l3_l1}B"

    # L5 and L7 OC streaming budgets
    l5_l1 = 1040 + (l5_input_depth + 1) * inter35_row + l5_wt_chunk + 2 * l5_output_elem
    assert l5_l1 <= 65536, f"L5 L1 budget exceeded: {l5_l1}B"

    l7_input_row_size = l7_ic * l7_width
    l7_l1 = (
        1040
        + (l7_input_depth + 1) * l7_input_row_size
        + l7_wt_chunk
        + 2 * l7_output_elem
    )
    assert l7_l1 <= 65536, f"L7 L1 budget exceeded: {l7_l1}B"

    dev_ty = NPU2()

    # --- Total tensor sizes ---
    total_input = l0_ic * l0_height * l0_width
    total_inter35 = l3_oc * l3_out_h * l3_out_w
    total_inter57 = l5_oc * l5_out_h * l5_out_w
    total_output = l7_oc * l7_out_h * l7_out_w

    # DDR weight layout: [col0_wts | l5_wts | l7_wts]
    total_weights = col0_total_wt + l5_total_wt + l7_total_wt

    # DDR output layout: [final_output | inter35_scratch | inter57_scratch]
    total_output_buf = total_output + total_inter35 + total_inter57

    # --- Types ---
    col0_max_row = max(l0_input_row, inter01_row, inter13_row, inter35_row)
    col0_row_ty = np.ndarray[(col0_max_row,), np.dtype[xfr_dtype]]
    col0_wt_ty = np.ndarray[(col0_wt_slot,), np.dtype[xfr_dtype]]
    col0_wts_all_ty = np.ndarray[(col0_total_wt,), np.dtype[xfr_dtype]]

    l5_input_row_ty = np.ndarray[(inter35_row,), np.dtype[xfr_dtype]]
    l5_output_row_ty = np.ndarray[(l5_output_elem,), np.dtype[xfr_dtype]]
    l5_wt_ty = np.ndarray[(l5_wt_chunk,), np.dtype[xfr_dtype]]

    l7_input_row_ty = np.ndarray[(l7_input_row_size,), np.dtype[xfr_dtype]]
    l7_output_row_ty = np.ndarray[(l7_output_elem,), np.dtype[xfr_dtype]]
    l7_wt_ty = np.ndarray[(l7_wt_chunk,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_weights,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_buf,), np.dtype[xfr_dtype]]

    # --- Kernel declarations ---
    col0_k3s2_kernel = Kernel(
        "conv2dk3s2_i8_silu",
        "conv2dk3_i8_silu.o",
        [
            col0_row_ty,
            col0_row_ty,
            col0_row_ty,
            col0_wt_ty,
            col0_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    l5_kernel = Kernel(
        "conv2dk3s2_i8_silu_l5",
        "conv2dk3_i8_silu_l5.o",
        [
            l5_input_row_ty,
            l5_input_row_ty,
            l5_input_row_ty,
            l5_wt_ty,
            l5_output_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    l7_kernel = Kernel(
        "conv2dk3s2_i8_silu_l7",
        "conv2dk3_i8_silu_l7.o",
        [
            l7_input_row_ty,
            l7_input_row_ty,
            l7_input_row_ty,
            l7_wt_ty,
            l7_output_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # --- Column 0 ObjectFIFOs ---
    in_fifo = ObjectFifo(col0_row_ty, name="l0_in", depth=l0_input_depth)

    col0_wts_all_fifo = ObjectFifo(col0_wts_all_ty, name="wts_col0", depth=1)
    wt0_fifo, wt1_fifo, wt2_fifo = col0_wts_all_fifo.cons().split(
        offsets=[0, col0_wt_slot, 2 * col0_wt_slot],
        obj_types=[col0_wt_ty, col0_wt_ty, col0_wt_ty],
        names=["wt_l0", "wt_l1", "wt_l3"],
        depths=[1, 1, 1],
        placement=Tile(0, 1),
    )

    inter01_fifo = ObjectFifo(col0_row_ty, name="inter_01", depth=l1_input_depth)
    inter13_fifo = ObjectFifo(col0_row_ty, name="inter_13", depth=l3_input_depth)
    col0_out_fifo = ObjectFifo(col0_row_ty, name="l3_out", depth=2)

    # --- L5 ObjectFIFOs ---
    l5_in_fifo = ObjectFifo(l5_input_row_ty, name="l5_in", depth=l5_input_depth)
    l5_wt_fifo = ObjectFifo(l5_wt_ty, name="l5_wt", depth=1)
    l5_out_fifo = ObjectFifo(l5_output_row_ty, name="l5_out", depth=2)

    # --- L7 ObjectFIFOs ---
    l7_in_fifo = ObjectFifo(l7_input_row_ty, name="l7_in", depth=l7_input_depth)
    l7_wt_fifo = ObjectFifo(l7_wt_ty, name="l7_wt", depth=1)
    l7_out_fifo = ObjectFifo(l7_output_row_ty, name="l7_out", depth=2)

    # --- Core functions ---

    def make_k3s2_silu_core_fn(in_width, in_ch, out_ch, out_h_val, s1, s2):
        """Standard fused k3s2 core function (no OC streaming)."""

        def core_fn(of_in, of_wt, of_out, kernel_fn):
            x_dim = in_width
            ci = in_ch
            co = out_ch
            oh = out_h_val
            shift1_val = s1
            shift2_val = s2

            elem_wt = of_wt.acquire(1)

            elems = of_in.acquire(2)
            elem_out = of_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[0],
                elems[1],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                0,
                shift1_val,
                shift2_val,
            )
            of_in.release(1)
            of_out.release(1)

            for _ in range_(oh - 1):
                elems = of_in.acquire(3)
                elem_out = of_out.acquire(1)
                kernel_fn(
                    elems[0],
                    elems[1],
                    elems[2],
                    elem_wt,
                    elem_out,
                    x_dim,
                    ci,
                    co,
                    1,
                    shift1_val,
                    shift2_val,
                )
                of_in.release(2)
                of_out.release(1)

            of_in.release(1)
            of_wt.release(1)

        return core_fn

    core_fn_l0 = make_k3s2_silu_core_fn(
        l0_width, l0_ic, l0_oc, l0_out_h, l0_shift1, l0_shift2
    )
    core_fn_l1 = make_k3s2_silu_core_fn(
        l1_width, l1_ic, l1_oc, l1_out_h, l1_shift1, l1_shift2
    )
    core_fn_l3 = make_k3s2_silu_core_fn(
        l3_width, l3_ic, l3_oc, l3_out_h, l3_shift1, l3_shift2
    )

    # L5: OC streaming core function
    def core_fn_l5(of_in, of_wt, of_out, kernel_fn):
        x_dim = l5_width
        ci = l5_ic
        co = l5_oc_chunk
        oh = l5_out_h
        s1 = l5_shift1
        s2 = l5_shift2

        for _ in range_(l5_n_oc_groups):
            elem_wt = of_wt.acquire(1)

            elems = of_in.acquire(2)
            elem_out = of_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[0],
                elems[1],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                0,
                s1,
                s2,
            )
            of_in.release(1)
            of_out.release(1)

            for _ in range_(oh - 1):
                elems = of_in.acquire(3)
                elem_out = of_out.acquire(1)
                kernel_fn(
                    elems[0],
                    elems[1],
                    elems[2],
                    elem_wt,
                    elem_out,
                    x_dim,
                    ci,
                    co,
                    1,
                    s1,
                    s2,
                )
                of_in.release(2)
                of_out.release(1)

            of_in.release(1)
            of_wt.release(1)

    # L7: OC streaming core function
    def core_fn_l7(of_in, of_wt, of_out, kernel_fn):
        x_dim = l7_width
        ci = l7_ic
        co = l7_oc_chunk
        oh = l7_out_h
        s1 = l7_shift1
        s2 = l7_shift2

        for _ in range_(l7_n_oc_groups):
            elem_wt = of_wt.acquire(1)

            elems = of_in.acquire(2)
            elem_out = of_out.acquire(1)
            kernel_fn(
                elems[0],
                elems[0],
                elems[1],
                elem_wt,
                elem_out,
                x_dim,
                ci,
                co,
                0,
                s1,
                s2,
            )
            of_in.release(1)
            of_out.release(1)

            for _ in range_(oh - 1):
                elems = of_in.acquire(3)
                elem_out = of_out.acquire(1)
                kernel_fn(
                    elems[0],
                    elems[1],
                    elems[2],
                    elem_wt,
                    elem_out,
                    x_dim,
                    ci,
                    co,
                    1,
                    s1,
                    s2,
                )
                of_in.release(2)
                of_out.release(1)

            of_in.release(1)
            of_wt.release(1)

    # --- Workers ---
    worker0 = Worker(
        core_fn_l0,
        [in_fifo.cons(), wt0_fifo.cons(), inter01_fifo.prod(), col0_k3s2_kernel],
        placement=Tile(0, 2),
    )
    worker1 = Worker(
        core_fn_l1,
        [
            inter01_fifo.cons(l1_input_depth),
            wt1_fifo.cons(),
            inter13_fifo.prod(),
            col0_k3s2_kernel,
        ],
        placement=Tile(0, 3),
    )
    worker2 = Worker(
        core_fn_l3,
        [
            inter13_fifo.cons(l3_input_depth),
            wt2_fifo.cons(),
            col0_out_fifo.prod(),
            col0_k3s2_kernel,
        ],
        placement=Tile(0, 4),
    )

    worker_l5 = Worker(
        core_fn_l5,
        [l5_in_fifo.cons(), l5_wt_fifo.cons(), l5_out_fifo.prod(), l5_kernel],
        placement=Tile(1, 2),
    )

    worker_l7 = Worker(
        core_fn_l7,
        [l7_in_fifo.cons(), l7_wt_fifo.cons(), l7_out_fifo.prod(), l7_kernel],
        placement=Tile(1, 3),
    )

    # --- Runtime sequence ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W_buf, O):
        rt.start(worker0, worker1, worker2, worker_l5, worker_l7)

        # ===== Phase 1: L0->L1->L3 pipeline to DDR scratch =====
        tg1 = rt.task_group()

        # Fill input (L0)
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
            task_group=tg1,
        )

        # Fill column 0 weights
        col0_wt_d3, col0_wt_d2, col0_wt_d1, col0_wt_d0 = _factorize_tensor(
            col0_total_wt
        )
        rt.fill(
            col0_wts_all_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=0,
                sizes=[col0_wt_d3, col0_wt_d2, col0_wt_d1, col0_wt_d0],
                strides=[
                    col0_wt_d2 * col0_wt_d1 * col0_wt_d0,
                    col0_wt_d1 * col0_wt_d0,
                    col0_wt_d0,
                    1,
                ],
            ),
            task_group=tg1,
        )

        # Drain L3 output to DDR scratch
        inter35_offset = total_output
        inter35_d3, inter35_d2, inter35_d1, inter35_d0 = _factorize_tensor(
            total_inter35
        )
        rt.drain(
            col0_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=inter35_offset,
                sizes=[inter35_d3, inter35_d2, inter35_d1, inter35_d0],
                strides=[
                    inter35_d2 * inter35_d1 * inter35_d0,
                    inter35_d1 * inter35_d0,
                    inter35_d0,
                    1,
                ],
            ),
            wait=True,
            task_group=tg1,
        )

        rt.finish_task_group(tg1)

        # ===== Phase 2: L5 with OC streaming =====
        tg2 = rt.task_group()

        # Fill L5 input: re-stream from DDR scratch
        l5_in_d2, l5_in_d1, l5_in_d0 = _factorize_3d(total_inter35)
        rt.fill(
            l5_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=inter35_offset,
                sizes=[l5_n_oc_groups, l5_in_d2, l5_in_d1, l5_in_d0],
                strides=[0, l5_in_d1 * l5_in_d0, l5_in_d0, 1],
            ),
            task_group=tg2,
        )

        # Fill L5 weights
        l5_wt_offset = col0_total_wt
        l5_wt_d3, l5_wt_d2, l5_wt_d1, l5_wt_d0 = _factorize_tensor(l5_total_wt)
        rt.fill(
            l5_wt_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=l5_wt_offset,
                sizes=[l5_wt_d3, l5_wt_d2, l5_wt_d1, l5_wt_d0],
                strides=[
                    l5_wt_d2 * l5_wt_d1 * l5_wt_d0,
                    l5_wt_d1 * l5_wt_d0,
                    l5_wt_d0,
                    1,
                ],
            ),
            task_group=tg2,
        )

        # Drain L5 output with strided interleaving
        inter57_offset = total_output + total_inter35
        l5_out_row_total = l5_oc * l5_out_w
        l5_pe_d0 = min(l5_output_elem, 1023)
        while l5_pe_d0 % 4 != 0:
            l5_pe_d0 -= 1
        while l5_pe_d0 >= 4:
            if l5_output_elem % l5_pe_d0 == 0:
                break
            l5_pe_d0 -= 4
        l5_pe_d1 = l5_output_elem // l5_pe_d0

        rt.drain(
            l5_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=inter57_offset,
                sizes=[l5_n_oc_groups, l5_out_h, l5_pe_d1, l5_pe_d0],
                strides=[l5_oc_chunk * l5_out_w, l5_out_row_total, l5_pe_d0, 1],
            ),
            wait=True,
            task_group=tg2,
        )

        rt.finish_task_group(tg2)

        # ===== Phase 3: L7 with OC streaming =====
        tg3 = rt.task_group()

        # Fill L7 input: re-stream from DDR scratch
        l7_in_d2, l7_in_d1, l7_in_d0 = _factorize_3d(total_inter57)
        rt.fill(
            l7_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=inter57_offset,
                sizes=[l7_n_oc_groups, l7_in_d2, l7_in_d1, l7_in_d0],
                strides=[0, l7_in_d1 * l7_in_d0, l7_in_d0, 1],
            ),
            task_group=tg3,
        )

        # Fill L7 weights
        l7_wt_offset = col0_total_wt + l5_total_wt
        l7_wt_d3, l7_wt_d2, l7_wt_d1, l7_wt_d0 = _factorize_tensor(l7_total_wt)
        rt.fill(
            l7_wt_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=l7_wt_offset,
                sizes=[l7_wt_d3, l7_wt_d2, l7_wt_d1, l7_wt_d0],
                strides=[
                    l7_wt_d2 * l7_wt_d1 * l7_wt_d0,
                    l7_wt_d1 * l7_wt_d0,
                    l7_wt_d0,
                    1,
                ],
            ),
            task_group=tg3,
        )

        # Drain L7 output (final output at offset 0)
        l7_out_row_total = l7_oc * l7_out_w
        l7_pe_d0 = min(l7_output_elem, 1023)
        while l7_pe_d0 % 4 != 0:
            l7_pe_d0 -= 1
        while l7_pe_d0 >= 4:
            if l7_output_elem % l7_pe_d0 == 0:
                break
            l7_pe_d0 -= 4
        l7_pe_d1 = l7_output_elem // l7_pe_d0

        if l7_n_oc_groups == 1:
            out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output)
            rt.drain(
                l7_out_fifo.cons(),
                O,
                TensorAccessPattern(
                    (1, total_output_buf),
                    offset=0,
                    sizes=[out_d3, out_d2, out_d1, out_d0],
                    strides=[out_d2 * out_d1 * out_d0, out_d1 * out_d0, out_d0, 1],
                ),
                wait=True,
                task_group=tg3,
            )
        else:
            rt.drain(
                l7_out_fifo.cons(),
                O,
                TensorAccessPattern(
                    (1, total_output_buf),
                    offset=0,
                    sizes=[l7_n_oc_groups, l7_out_h, l7_pe_d1, l7_pe_d0],
                    strides=[l7_oc_chunk * l7_out_w, l7_out_row_total, l7_pe_d0, 1],
                ),
                wait=True,
                task_group=tg3,
            )

        rt.finish_task_group(tg3)

    return Program(dev_ty, rt).resolve_program(
        SequentialPlacer()
    )  # spine_5layer L0->L1->L3->L5->L7


# ---------------------------------------------------------------------------
# Step 9: C2f L4 (n=2 bottlenecks) -- 64ch, 80x80
#
# Uses multi-phase execution to simplify MemTile routing:
#   Phase 1: cv1(64->64, k1) -> split -> half1 + half2 to DDR scratch
#   Phase 2: half2 -> bn0.cv1(k3) -> bn0.cv2(k3) -> +half2(add) -> bn0_out to DDR
#   Phase 3: bn0_out -> bn1.cv1(k3) -> bn1.cv2(k3) -> +bn0_out(add) -> bn1_out to DDR
#   Phase 4: Read concat [half1|half2|bn0_out|bn1_out] -> cv2(128->64, k1) -> output
#
# Core mapping (8 cores, 2 columns):
#   Col 0: cv1(0,2), bn0.cv1(0,3), bn0.cv2(0,4), bn0_add(0,5)
#   Col 1: bn1.cv1(1,2), bn1.cv2(1,3), bn1_add(1,4), cv2(1,5)
#
# Skip connections use MemTile buffering (forward pattern).
# Concat uses ObjectFIFO join at MemTile.
# ---------------------------------------------------------------------------


def my_dataflow_c2f_l4(
    dev,
    height,
    width,
    in_channels,
    cv1_scale,
    bn0_cv1_scale,
    bn0_cv2_scale,
    bn1_cv1_scale,
    bn1_cv2_scale,
    cv2_scale,
):
    """C2f block for L4: 64ch input, n=2 bottlenecks with residual add.

    Multi-phase execution building concat in-place:

    DDR output buffer: [final_output(64ch*H*W) | concat(128ch*H*W)]

    Phase A: cv1(64->64, k1) -> drain to concat[0:64ch]
             This places half1=[0:32ch] and half2=[32:64ch] directly.
    Phase B: Read half2(32ch) from concat[32:64ch]
             -> bn0.cv1(k3) -> bn0.cv2(k3) -> add(+half2_skip)
             -> drain bn0_out to concat[64:96ch]
    Phase C: Read bn0_out(32ch) from concat[64:96ch]
             -> bn1.cv1(k3) -> bn1.cv2(k3) -> add(+bn0_out_skip)
             -> drain bn1_out to concat[96:128ch]
    Phase D: Read concat(128ch) linearly -> cv2(128->64, k1) -> output

    Core mapping:
      Phase A: cv1(0,2) [1 core]
      Phase B: bn0.cv1(0,3), bn0.cv2(0,4), bn0_add(0,5) [3 cores]
      Phase C: bn1.cv1(1,2), bn1.cv2(1,3), bn1_add(1,4) [3 cores]
      Phase D: cv2(1,5) [1 core]

    Args:
        dev: Device type string.
        height: Spatial height (80 for L4).
        width: Spatial width (80 for L4).
        in_channels: Input channels (64).
        cv1_scale-cv2_scale: requantization shifts.
    """
    xfr_dtype = np.int8

    assert in_channels == 64
    cv1_oc = 64
    bn_ch = 32
    cv2_ic = 128
    cv2_oc = 64

    # Row sizes
    input_row = in_channels * width
    cv1_out_row = cv1_oc * width
    half_row = bn_ch * width
    cv2_in_row = cv2_ic * width
    cv2_out_row = cv2_oc * width

    # Weight sizes (non-fused, no bias)
    cv1_wt = cv1_oc * in_channels  # 4096
    bn_k3_wt = bn_ch * bn_ch * 9  # 9216
    cv2_wt = cv2_oc * cv2_ic  # 8192

    total_input = in_channels * height * width
    total_output = cv2_oc * height * width
    cv1_full_total = cv1_oc * height * width
    half_total = bn_ch * height * width
    total_concat = cv2_ic * height * width

    # --- L1 budget checks ---
    bn_depth = 4

    core_cv1_l1 = 1040 + 2 * input_row + cv1_wt + 2 * cv1_out_row
    assert core_cv1_l1 <= 65536, f"cv1 L1: {core_cv1_l1}B"

    core_bn_k3_l1 = 1040 + (bn_depth + 1) * half_row + bn_k3_wt + 2 * half_row
    assert core_bn_k3_l1 <= 65536, f"bn k3 L1: {core_bn_k3_l1}B"

    core_add_l1 = 1040 + 2 * half_row + 2 * half_row + 2 * half_row
    assert core_add_l1 <= 65536, f"add L1: {core_add_l1}B"

    core_cv2_l1 = 1040 + 2 * cv2_in_row + cv2_wt + 2 * cv2_out_row
    assert core_cv2_l1 <= 65536, f"cv2 L1: {core_cv2_l1}B"

    dev_ty = NPU2()

    # DDR scratch layout in output buffer:
    # [final_output | cv1_full_scratch | bn0_out_scratch | bn1_out_scratch]
    # DDR output buffer: [final_output(64ch) | concat(128ch)]
    # concat = [half1(32ch) | half2(32ch) | bn0_out(32ch) | bn1_out(32ch)]
    # Phase A writes cv1(64ch) to concat[0:64ch] (half1+half2 in-place)
    # Phase B writes bn0_out to concat[64:96ch]
    # Phase C writes bn1_out to concat[96:128ch]
    concat_offset = total_output
    output_buf_size = total_output + total_concat

    # Weight layout: [cv1_wt | bn0cv1_wt | bn0cv2_wt | bn1cv1_wt | bn1cv2_wt | cv2_wt]
    # Bottleneck weights share a padded slot via MemTile split (phases B,C)
    bn_wt_slot = bn_k3_wt  # no padding needed, all bn weights are same size
    total_wt = cv1_wt + 4 * bn_wt_slot + cv2_wt

    # --- Types ---
    input_row_ty = np.ndarray[(input_row,), np.dtype[xfr_dtype]]
    cv1_out_row_ty = np.ndarray[(cv1_out_row,), np.dtype[xfr_dtype]]
    cv1_wt_ty = np.ndarray[(cv1_wt,), np.dtype[xfr_dtype]]
    half_row_ty = np.ndarray[(half_row,), np.dtype[xfr_dtype]]
    bn_wt_ty = np.ndarray[(bn_wt_slot,), np.dtype[xfr_dtype]]
    bn_wts_pair_ty = np.ndarray[(2 * bn_wt_slot,), np.dtype[xfr_dtype]]
    cv2_in_row_ty = np.ndarray[(cv2_in_row,), np.dtype[xfr_dtype]]
    cv2_out_row_ty = np.ndarray[(cv2_out_row,), np.dtype[xfr_dtype]]
    cv2_wt_ty = np.ndarray[(cv2_wt,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(output_buf_size,), np.dtype[xfr_dtype]]

    # --- Kernels ---
    k1_kernel = Kernel(
        "conv2dk1_i8",
        "conv2dk1_i8.o",
        [
            input_row_ty,
            cv1_wt_ty,
            cv1_out_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    k3_bn_kernel = Kernel(
        "conv2dk3_i8_bn",
        "conv2dk3_i8_bn.o",
        [
            half_row_ty,
            half_row_ty,
            half_row_ty,
            bn_wt_ty,
            half_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    add_kernel = Kernel(
        "add_i8",
        "add_i8.o",
        [half_row_ty, half_row_ty, half_row_ty, np.int32],
    )

    k1_cv2_kernel = Kernel(
        "conv2dk1_i8_cv2",
        "conv2dk1_i8_cv2.o",
        [
            cv2_in_row_ty,
            cv2_wt_ty,
            cv2_out_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # --- Phase A FIFOs: cv1 ---
    in_fifo = ObjectFifo(input_row_ty, name="c2f_l4_in", depth=2)
    cv1_wt_fifo = ObjectFifo(cv1_wt_ty, name="cv1_wt", depth=1)
    cv1_out_fifo = ObjectFifo(cv1_out_row_ty, name="cv1_out", depth=2)

    # --- Phase B FIFOs: bn0 pipeline ---
    bn0_in_fifo = ObjectFifo(half_row_ty, name="bn0_in", depth=bn_depth)
    bn0_skip_fifo = ObjectFifo(half_row_ty, name="bn0_skip", depth=2)
    bn0_wts_fifo = ObjectFifo(bn_wts_pair_ty, name="bn0_wts", depth=1)
    bn0_wt1_f, bn0_wt2_f = bn0_wts_fifo.cons().split(
        offsets=[0, bn_wt_slot],
        obj_types=[bn_wt_ty, bn_wt_ty],
        names=["bn0_wt1", "bn0_wt2"],
        depths=[1, 1],
        placement=Tile(0, 1),
    )
    bn0_inter = ObjectFifo(half_row_ty, name="bn0_inter", depth=bn_depth)
    bn0_cv2_out = ObjectFifo(half_row_ty, name="bn0_cv2_out", depth=2)
    bn0_out_fifo = ObjectFifo(half_row_ty, name="bn0_out", depth=2)

    # --- Phase C FIFOs: bn1 pipeline ---
    bn1_in_fifo = ObjectFifo(half_row_ty, name="bn1_in", depth=bn_depth)
    bn1_skip_fifo = ObjectFifo(half_row_ty, name="bn1_skip", depth=2)
    bn1_wts_fifo = ObjectFifo(bn_wts_pair_ty, name="bn1_wts", depth=1)
    bn1_wt1_f, bn1_wt2_f = bn1_wts_fifo.cons().split(
        offsets=[0, bn_wt_slot],
        obj_types=[bn_wt_ty, bn_wt_ty],
        names=["bn1_wt1", "bn1_wt2"],
        depths=[1, 1],
        placement=Tile(1, 1),
    )
    bn1_inter = ObjectFifo(half_row_ty, name="bn1_inter", depth=bn_depth)
    bn1_cv2_out = ObjectFifo(half_row_ty, name="bn1_cv2_out", depth=2)
    bn1_out_fifo = ObjectFifo(half_row_ty, name="bn1_out", depth=2)

    # --- Phase D FIFOs: cv2 ---
    cv2_in_fifo = ObjectFifo(cv2_in_row_ty, name="cv2_in", depth=2)
    cv2_wt_fifo = ObjectFifo(cv2_wt_ty, name="cv2_wt", depth=1)
    cv2_out_fifo = ObjectFifo(cv2_out_row_ty, name="cv2_out", depth=2)

    # --- Core functions ---

    def core_fn_cv1(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = in_channels
        co = cv1_oc
        sc = cv1_scale
        elem_wt = of_wt.acquire(1)
        for _ in range_(height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, sc)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    def _make_k3s1_core_fn(h_val, sc_val):
        def core_fn(of_in, of_wt, of_out, kernel_fn):
            w = width
            ci = bn_ch
            co = bn_ch
            sc = sc_val
            h = h_val
            elem_wt = of_wt.acquire(1)

            elems = of_in.acquire(2)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo, w, ci, co, 0, sc)
            of_out.release(1)

            for _ in range_(h - 2):
                elems = of_in.acquire(3)
                eo = of_out.acquire(1)
                kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo, w, ci, co, 1, sc)
                of_in.release(1)
                of_out.release(1)

            elems = of_in.acquire(2)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo, w, ci, co, 2, sc)
            of_in.release(2)
            of_out.release(1)

            of_wt.release(1)

        return core_fn

    def core_fn_add(of_a, of_b, of_out, kernel_fn):
        row_sz = half_row
        for _ in range_(height):
            ea = of_a.acquire(1)
            eb = of_b.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ea, eb, eo, row_sz)
            of_a.release(1)
            of_b.release(1)
            of_out.release(1)

    def core_fn_cv2(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = cv2_ic
        co = cv2_oc
        sc = cv2_scale
        elem_wt = of_wt.acquire(1)
        for _ in range_(height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, sc)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    # --- Workers ---
    worker_cv1 = Worker(
        core_fn_cv1,
        [in_fifo.cons(), cv1_wt_fifo.cons(), cv1_out_fifo.prod(), k1_kernel],
        placement=Tile(0, 2),
    )
    worker_bn0cv1 = Worker(
        _make_k3s1_core_fn(height, bn0_cv1_scale),
        [bn0_in_fifo.cons(bn_depth), bn0_wt1_f.cons(), bn0_inter.prod(), k3_bn_kernel],
        placement=Tile(0, 3),
    )
    worker_bn0cv2 = Worker(
        _make_k3s1_core_fn(height, bn0_cv2_scale),
        [bn0_inter.cons(bn_depth), bn0_wt2_f.cons(), bn0_cv2_out.prod(), k3_bn_kernel],
        placement=Tile(0, 4),
    )
    worker_bn0add = Worker(
        core_fn_add,
        [bn0_cv2_out.cons(), bn0_skip_fifo.cons(), bn0_out_fifo.prod(), add_kernel],
        placement=Tile(0, 5),
    )
    worker_bn1cv1 = Worker(
        _make_k3s1_core_fn(height, bn1_cv1_scale),
        [bn1_in_fifo.cons(bn_depth), bn1_wt1_f.cons(), bn1_inter.prod(), k3_bn_kernel],
        placement=Tile(1, 2),
    )
    worker_bn1cv2 = Worker(
        _make_k3s1_core_fn(height, bn1_cv2_scale),
        [bn1_inter.cons(bn_depth), bn1_wt2_f.cons(), bn1_cv2_out.prod(), k3_bn_kernel],
        placement=Tile(1, 3),
    )
    worker_bn1add = Worker(
        core_fn_add,
        [bn1_cv2_out.cons(), bn1_skip_fifo.cons(), bn1_out_fifo.prod(), add_kernel],
        placement=Tile(1, 4),
    )
    worker_cv2 = Worker(
        core_fn_cv2,
        [cv2_in_fifo.cons(), cv2_wt_fifo.cons(), cv2_out_fifo.prod(), k1_cv2_kernel],
        placement=Tile(1, 5),
    )

    # --- Runtime ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(
            worker_cv1,
            worker_bn0cv1,
            worker_bn0cv2,
            worker_bn0add,
            worker_bn1cv1,
            worker_bn1cv2,
            worker_bn1add,
            worker_cv2,
        )

        # === Phase A: cv1 -> DDR scratch ===
        tg_a = rt.task_group()

        in_dims = _factorize_tensor(total_input)
        rt.fill(
            in_fifo.prod(),
            I,
            TensorAccessPattern(
                (1, total_input),
                offset=0,
                sizes=list(in_dims),
                strides=[
                    in_dims[1] * in_dims[2] * in_dims[3],
                    in_dims[2] * in_dims[3],
                    in_dims[3],
                    1,
                ],
            ),
            task_group=tg_a,
        )

        cv1w_dims = _factorize_tensor(cv1_wt)
        rt.fill(
            cv1_wt_fifo.prod(),
            W,
            TensorAccessPattern(
                (1, total_wt),
                offset=0,
                sizes=list(cv1w_dims),
                strides=[
                    cv1w_dims[1] * cv1w_dims[2] * cv1w_dims[3],
                    cv1w_dims[2] * cv1w_dims[3],
                    cv1w_dims[3],
                    1,
                ],
            ),
            task_group=tg_a,
        )

        # Drain cv1 output (64ch) with strided write into concat rows (128ch each).
        # Each cv1_out_row = 64*W goes to offset 0 within each cv2_in_row = 128*W.
        cr_d0 = min(cv1_out_row, 1023)
        while cr_d0 % 4 != 0:
            cr_d0 -= 1
        while cr_d0 >= 4:
            if cv1_out_row % cr_d0 == 0:
                break
            cr_d0 -= 4
        cr_d1 = cv1_out_row // cr_d0

        rt.drain(
            cv1_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset,
                sizes=[1, height, cr_d1, cr_d0],
                strides=[0, cv2_in_row, cr_d0, 1],
            ),
            wait=True,
            task_group=tg_a,
        )

        rt.finish_task_group(tg_a)

        # === Phase B: bn0 (half2 -> k3 -> k3 -> add -> bn0_out) ===
        tg_b = rt.task_group()

        # Read half2 from concat[32:64ch] -- strided read from 128ch rows.
        hr_d0 = min(half_row, 1023)
        while hr_d0 % 4 != 0:
            hr_d0 -= 1
        while hr_d0 >= 4:
            if half_row % hr_d0 == 0:
                break
            hr_d0 -= 4
        hr_d1 = half_row // hr_d0

        rt.fill(
            bn0_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset + half_row,
                sizes=[1, height, hr_d1, hr_d0],
                strides=[0, cv2_in_row, hr_d0, 1],
            ),
            task_group=tg_b,
        )

        # Same data for residual skip
        rt.fill(
            bn0_skip_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset + half_row,
                sizes=[1, height, hr_d1, hr_d0],
                strides=[0, cv2_in_row, hr_d0, 1],
            ),
            task_group=tg_b,
        )

        # Fill bn0 weights (bn0.cv1 + bn0.cv2)
        bn0_wt_offset = cv1_wt
        bn0_wt_dims = _factorize_tensor(2 * bn_wt_slot)
        rt.fill(
            bn0_wts_fifo.prod(),
            W,
            TensorAccessPattern(
                (1, total_wt),
                offset=bn0_wt_offset,
                sizes=list(bn0_wt_dims),
                strides=[
                    bn0_wt_dims[1] * bn0_wt_dims[2] * bn0_wt_dims[3],
                    bn0_wt_dims[2] * bn0_wt_dims[3],
                    bn0_wt_dims[3],
                    1,
                ],
            ),
            task_group=tg_b,
        )

        # Drain bn0_out with strided write to concat[64:96ch]
        rt.drain(
            bn0_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset + 2 * half_row,
                sizes=[1, height, hr_d1, hr_d0],
                strides=[0, cv2_in_row, hr_d0, 1],
            ),
            wait=True,
            task_group=tg_b,
        )

        rt.finish_task_group(tg_b)

        # === Phase C: bn1 (bn0_out -> k3 -> k3 -> add -> bn1_out) ===
        tg_c = rt.task_group()

        # Read bn0_out from concat[64:96ch] -- strided
        rt.fill(
            bn1_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset + 2 * half_row,
                sizes=[1, height, hr_d1, hr_d0],
                strides=[0, cv2_in_row, hr_d0, 1],
            ),
            task_group=tg_c,
        )

        # Same data for residual skip
        rt.fill(
            bn1_skip_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset + 2 * half_row,
                sizes=[1, height, hr_d1, hr_d0],
                strides=[0, cv2_in_row, hr_d0, 1],
            ),
            task_group=tg_c,
        )

        # Fill bn1 weights (bn1.cv1 + bn1.cv2)
        bn1_wt_offset = cv1_wt + 2 * bn_wt_slot
        bn1_wt_dims = _factorize_tensor(2 * bn_wt_slot)
        rt.fill(
            bn1_wts_fifo.prod(),
            W,
            TensorAccessPattern(
                (1, total_wt),
                offset=bn1_wt_offset,
                sizes=list(bn1_wt_dims),
                strides=[
                    bn1_wt_dims[1] * bn1_wt_dims[2] * bn1_wt_dims[3],
                    bn1_wt_dims[2] * bn1_wt_dims[3],
                    bn1_wt_dims[3],
                    1,
                ],
            ),
            task_group=tg_c,
        )

        # Drain bn1_out with strided write to concat[96:128ch]
        rt.drain(
            bn1_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset + 3 * half_row,
                sizes=[1, height, hr_d1, hr_d0],
                strides=[0, cv2_in_row, hr_d0, 1],
            ),
            wait=True,
            task_group=tg_c,
        )

        rt.finish_task_group(tg_c)

        # === Phase D: cv2 reads assembled concat linearly ===
        tg_d = rt.task_group()

        cv2i_dims = _factorize_tensor(total_concat)
        rt.fill(
            cv2_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset,
                sizes=list(cv2i_dims),
                strides=[
                    cv2i_dims[1] * cv2i_dims[2] * cv2i_dims[3],
                    cv2i_dims[2] * cv2i_dims[3],
                    cv2i_dims[3],
                    1,
                ],
            ),
            task_group=tg_d,
        )

        cv2w_dims = _factorize_tensor(cv2_wt)
        cv2_wt_ddr_offset = cv1_wt + 4 * bn_wt_slot
        rt.fill(
            cv2_wt_fifo.prod(),
            W,
            TensorAccessPattern(
                (1, total_wt),
                offset=cv2_wt_ddr_offset,
                sizes=list(cv2w_dims),
                strides=[
                    cv2w_dims[1] * cv2w_dims[2] * cv2w_dims[3],
                    cv2w_dims[2] * cv2w_dims[3],
                    cv2w_dims[3],
                    1,
                ],
            ),
            task_group=tg_d,
        )

        out_dims = _factorize_tensor(total_output)
        rt.drain(
            cv2_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=0,
                sizes=list(out_dims),
                strides=[
                    out_dims[1] * out_dims[2] * out_dims[3],
                    out_dims[2] * out_dims[3],
                    out_dims[3],
                    1,
                ],
            ),
            wait=True,
            task_group=tg_d,
        )

        rt.finish_task_group(tg_d)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # c2f_l4
