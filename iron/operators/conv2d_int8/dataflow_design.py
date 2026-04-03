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

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # upsample2x


# ---------------------------------------------------------------------------
# Combined L12 C2f + Upsample + L15 C2f (1 PDI, 3 neck PDIs -> 1)
# ---------------------------------------------------------------------------


def my_dataflow_l12_l15(
    dev, l12_h, l12_w,
    l12_cv1_s1, l12_cv1_s2, l12_bn_cv1_s1, l12_bn_cv1_s2,
    l12_bn_cv2_s1, l12_bn_cv2_s2, l12_cv2_s1, l12_cv2_s2,
    l15_cv1_s1, l15_cv1_s2, l15_bn_cv1_s1, l15_bn_cv1_s2,
    l15_bn_cv2_s1, l15_bn_cv2_s2, l15_cv2_s1, l15_cv2_s2,
):
    """Combined L12 C2f + Upsample 2x + L15 C2f in one PDI.

    I  = L12 input (384ch, l12_h x l12_w)
    O  = [L15_final | L12_concat | L12_out | L15_concat | L15_c2f_concat]
         Host pre-fills P3(64ch) into L15_concat[128:192ch per row].

    TG1-3: L12 C2f (384->128) -> L12_out
    TG4:   Upsample 2x (L12_out -> L15_concat[0:128ch])
    TG5-7: L15 C2f (192->64) -> L15_final

    9 workers, 4 columns. 7 unique kernel symbols.
    """
    xfr_dtype = np.int8
    t = lambda n: np.ndarray[(n,), np.dtype[xfr_dtype]]

    # L12 params
    l12_ic, l12_cv1_oc, l12_bn_ch = 384, 128, 64
    l12_cv2_ic, l12_cv2_oc = 192, 128
    l12_input_row = l12_ic * l12_w
    l12_half_row = l12_bn_ch * l12_w
    l12_cv2_in_row = l12_cv2_ic * l12_w

    # L12 cv1 OC streaming
    avail = 65536 - 1040 - 2 * l12_input_row
    l12_cv1_chunk = l12_cv1_oc
    for try_oc in range(l12_cv1_oc, 0, -8):
        if l12_cv1_oc % try_oc != 0:
            continue
        if try_oc * l12_ic + try_oc * 4 + 2 * try_oc * l12_w <= avail:
            l12_cv1_chunk = try_oc
            break
    l12_cv1_n = l12_cv1_oc // l12_cv1_chunk
    l12_cv1_wc = l12_cv1_chunk * l12_ic + l12_cv1_chunk * 4
    l12_cv1_or = l12_cv1_chunk * l12_w
    l12_bn_wt = l12_bn_ch * l12_bn_ch * 9 + l12_bn_ch * 4
    l12_cv2_wt = l12_cv2_oc * l12_cv2_ic + l12_cv2_oc * 4
    l12_bd = 4

    # L15 params
    l15_h, l15_w = l12_h * 2, l12_w * 2
    l15_ic, l15_cv1_oc, l15_bn_ch = 192, 64, 32
    l15_cv2_ic, l15_cv2_oc = 96, 64
    l15_ir = l15_ic * l15_w
    l15_hr = l15_bn_ch * l15_w
    l15_cr = l15_cv2_ic * l15_w
    l15_c1w = l15_cv1_oc * l15_ic + l15_cv1_oc * 4
    l15_bw = l15_bn_ch * l15_bn_ch * 9 + l15_bn_ch * 4
    l15_c2w = l15_cv2_oc * l15_cv2_ic + l15_cv2_oc * 4
    l15_bd = 4
    ups_ir = l12_cv2_oc * l12_w
    ups_or = l12_cv2_oc * l15_w

    # DDR layout
    s0 = l15_cv2_oc * l15_h * l15_w      # L15 final
    s1 = l12_cv2_ic * l12_h * l12_w      # L12 concat
    s2 = l12_cv2_oc * l12_h * l12_w      # L12 out
    s3 = l15_ic * l15_h * l15_w          # L15 in concat
    s4 = l15_cv2_ic * l15_h * l15_w      # L15 c2f concat
    o0, o1, o2, o3, o4 = 0, s0, s0+s1, s0+s1+s2, s0+s1+s2+s3
    oT = o4 + s4
    total_input = l12_ic * l12_h * l12_w
    l12_cv1_tw = l12_cv1_n * l12_cv1_wc
    l12_tw = l12_cv1_tw + 2 * l12_bn_wt + l12_cv2_wt
    l15_tw = l15_c1w + 2 * l15_bw + l15_c2w
    wT = l12_tw + l15_tw
    dev_ty = NPU2()

    # Kernels (7)
    k12c1 = Kernel("conv2dk1_i8_silu", "conv2dk1_i8_silu.o",
        [t(l12_input_row), t(l12_cv1_wc), t(l12_cv1_or)] + [np.int32]*5)
    k12bn = Kernel("conv2dk3_i8_silu", "conv2dk3_i8_silu.o",
        [t(l12_half_row)]*3 + [t(l12_bn_wt), t(l12_half_row)] + [np.int32]*6)
    k12c2 = Kernel("conv2dk1_i8_silu_cv2", "conv2dk1_i8_silu_cv2.o",
        [t(l12_cv2_in_row), t(l12_cv2_wt), t(l12_cv2_oc*l12_w)] + [np.int32]*5)
    k15c1 = Kernel("conv2dk1_i8_silu_l15", "conv2dk1_i8_silu_l15.o",
        [t(l15_ir), t(l15_c1w), t(l15_cv1_oc*l15_w)] + [np.int32]*5)
    k15bn = Kernel("conv2dk3_i8_silu_l15", "conv2dk3_i8_silu_l15.o",
        [t(l15_hr)]*3 + [t(l15_bw), t(l15_hr)] + [np.int32]*6)
    k15c2 = Kernel("conv2dk1_i8_silu_l15cv2", "conv2dk1_i8_silu_l15cv2.o",
        [t(l15_cr), t(l15_c2w), t(l15_cv2_oc*l15_w)] + [np.int32]*5)
    kups = Kernel("upsample2x_row_i8", "upsample2x_i8.o",
        [t(ups_ir), t(ups_or), np.int32, np.int32])

    # FIFOs
    f = lambda ty, nm, d: ObjectFifo(ty, name=nm, depth=d)
    f12i=f(t(l12_input_row),"l12i",2); f12cw=f(t(l12_cv1_wc),"l12cw",1)
    f12co=f(t(l12_cv1_or),"l12co",2)
    f12bi=f(t(l12_half_row),"l12bi",l12_bd); f12bw1=f(t(l12_bn_wt),"l12bw1",1)
    f12bw2=f(t(l12_bn_wt),"l12bw2",1)
    f12bm=f(t(l12_half_row),"l12bm",l12_bd); f12bo=f(t(l12_half_row),"l12bo",2)
    f12vi=f(t(l12_cv2_in_row),"l12vi",2); f12vw=f(t(l12_cv2_wt),"l12vw",1)
    f12vo=f(t(l12_cv2_oc*l12_w),"l12vo",2)
    fui=f(t(ups_ir),"fui",2); fuo=f(t(ups_or),"fuo",2)
    f15i=f(t(l15_ir),"l15i",2); f15cw=f(t(l15_c1w),"l15cw",1)
    f15co=f(t(l15_cv1_oc*l15_w),"l15co",2)
    f15bi=f(t(l15_hr),"l15bi",l15_bd); f15bw1=f(t(l15_bw),"l15bw1",1)
    f15bw2=f(t(l15_bw),"l15bw2",1)
    f15bm=f(t(l15_hr),"l15bm",l15_bd); f15bo=f(t(l15_hr),"l15bo",2)
    f15vi=f(t(l15_cr),"l15vi",2); f15vw=f(t(l15_c2w),"l15vw",1)
    f15vo=f(t(l15_cv2_oc*l15_w),"l15vo",2)

    # Core fn factories
    def _k1oc(ci, co, n, s1, s2, h, w):
        def fn(oi, ow, oo, kf):
            for _ in range_(n):
                ww = ow.acquire(1)
                for _ in range_(h):
                    ei=oi.acquire(1); eo=oo.acquire(1)
                    kf(ei, ww, eo, w, ci, co, s1, s2)
                    oi.release(1); oo.release(1)
                ow.release(1)
        return fn
    def _k1(ci, co, s1, s2, h, w):
        def fn(oi, ow, oo, kf):
            ww = ow.acquire(1)
            for _ in range_(h):
                ei=oi.acquire(1); eo=oo.acquire(1)
                kf(ei, ww, eo, w, ci, co, s1, s2)
                oi.release(1); oo.release(1)
            ow.release(1)
        return fn
    def _k3(ci, co, s1, s2, h, w):
        def fn(oi, ow, oo, kf):
            ww = ow.acquire(1)
            e=oi.acquire(2); o=oo.acquire(1)
            kf(e[0],e[0],e[1],ww,o,w,ci,co,0,s1,s2); oo.release(1)
            for _ in range_(h-2):
                e=oi.acquire(3); o=oo.acquire(1)
                kf(e[0],e[1],e[2],ww,o,w,ci,co,1,s1,s2)
                oi.release(1); oo.release(1)
            e=oi.acquire(2); o=oo.acquire(1)
            kf(e[0],e[1],e[1],ww,o,w,ci,co,2,s1,s2)
            oi.release(2); oo.release(1); ow.release(1)
        return fn
    def _ups(oi, oo, kf):
        for _ in range_(l12_h):
            ei = oi.acquire(1)
            eo=oo.acquire(1); kf(ei, eo, l12_w, l12_cv2_oc); oo.release(1)
            eo=oo.acquire(1); kf(ei, eo, l12_w, l12_cv2_oc); oo.release(1)
            oi.release(1)

    # Workers (9, 4 columns)
    w0=Worker(_k1oc(l12_ic,l12_cv1_chunk,l12_cv1_n,l12_cv1_s1,l12_cv1_s2,l12_h,l12_w),
           [f12i.cons(),f12cw.cons(),f12co.prod(),k12c1], placement=Tile(0,2))
    w1=Worker(_k3(l12_bn_ch,l12_bn_ch,l12_bn_cv1_s1,l12_bn_cv1_s2,l12_h,l12_w),
           [f12bi.cons(l12_bd),f12bw1.cons(),f12bm.prod(),k12bn], placement=Tile(0,3))
    w2=Worker(_k3(l12_bn_ch,l12_bn_ch,l12_bn_cv2_s1,l12_bn_cv2_s2,l12_h,l12_w),
           [f12bm.cons(l12_bd),f12bw2.cons(),f12bo.prod(),k12bn], placement=Tile(1,2))
    w3=Worker(_k1(l12_cv2_ic,l12_cv2_oc,l12_cv2_s1,l12_cv2_s2,l12_h,l12_w),
           [f12vi.cons(),f12vw.cons(),f12vo.prod(),k12c2], placement=Tile(1,3))
    w4=Worker(_ups, [fui.cons(),fuo.prod(),kups], placement=Tile(1,4))
    w5=Worker(_k1(l15_ic,l15_cv1_oc,l15_cv1_s1,l15_cv1_s2,l15_h,l15_w),
           [f15i.cons(),f15cw.cons(),f15co.prod(),k15c1], placement=Tile(2,2))
    w6=Worker(_k3(l15_bn_ch,l15_bn_ch,l15_bn_cv1_s1,l15_bn_cv1_s2,l15_h,l15_w),
           [f15bi.cons(l15_bd),f15bw1.cons(),f15bm.prod(),k15bn], placement=Tile(2,3))
    w7=Worker(_k3(l15_bn_ch,l15_bn_ch,l15_bn_cv2_s1,l15_bn_cv2_s2,l15_h,l15_w),
           [f15bm.cons(l15_bd),f15bw2.cons(),f15bo.prod(),k15bn], placement=Tile(3,2))
    w8=Worker(_k1(l15_cv2_ic,l15_cv2_oc,l15_cv2_s1,l15_cv2_s2,l15_h,l15_w),
           [f15vi.cons(),f15vw.cons(),f15vo.prod(),k15c2], placement=Tile(3,3))

    # TAP helpers
    def _ct(buf, off, tot):
        d=_factorize_tensor(tot)
        return TensorAccessPattern((1,buf),offset=off,
            sizes=list(d),strides=[d[1]*d[2]*d[3],d[2]*d[3],d[3],1])
    def _sr(buf, off, rows, elem, stride):
        d0=min(elem,1023)
        while d0%4!=0: d0-=1
        while d0>=4 and elem%d0!=0: d0-=4
        return TensorAccessPattern((1,buf),offset=off,
            sizes=[1,rows,elem//d0,d0],strides=[0,stride,d0,1])
    def _od(buf, off, n, cw, rt_, h):
        d0=min(cw,1023)
        while d0%4!=0: d0-=1
        while d0>=4 and cw%d0!=0: d0-=4
        return TensorAccessPattern((1,buf),offset=off,
            sizes=[n,h,cw//d0,d0],strides=[cw,rt_,d0,1])
    def _of(buf, off, n, tot):
        d2,d1,d0=_factorize_3d(tot)
        return TensorAccessPattern((1,buf),offset=off,
            sizes=[n,d2,d1,d0],strides=[0,d1*d0,d0,1])

    wo = 0
    rt = Runtime()
    with rt.sequence(t(total_input), t(wT), t(oT)) as (I, W, O):
        rt.start(w0, w1, w2, w3, w4, w5, w6, w7, w8)
        # TG1: L12 cv1
        tg=rt.task_group()
        rt.fill(f12i.prod(),I,_of(total_input,0,l12_cv1_n,total_input),task_group=tg)
        rt.fill(f12cw.prod(),W,_ct(wT,wo,l12_cv1_tw),task_group=tg)
        rt.drain(f12co.cons(),O,_od(oT,o1,l12_cv1_n,l12_cv1_chunk*l12_w,l12_cv2_in_row,l12_h),wait=True,task_group=tg)
        rt.finish_task_group(tg); wo+=l12_cv1_tw
        # TG2: L12 bn0
        tg=rt.task_group()
        rt.fill(f12bi.prod(),O,_sr(oT,o1+l12_half_row,l12_h,l12_half_row,l12_cv2_in_row),task_group=tg)
        rt.fill(f12bw1.prod(),W,_ct(wT,wo,l12_bn_wt),task_group=tg)
        rt.fill(f12bw2.prod(),W,_ct(wT,wo+l12_bn_wt,l12_bn_wt),task_group=tg)
        rt.drain(f12bo.cons(),O,_sr(oT,o1+l12_cv1_oc*l12_w,l12_h,l12_half_row,l12_cv2_in_row),wait=True,task_group=tg)
        rt.finish_task_group(tg); wo+=2*l12_bn_wt
        # TG3: L12 cv2 → L12_out
        tg=rt.task_group()
        rt.fill(f12vi.prod(),O,_ct(oT,o1,s1),task_group=tg)
        rt.fill(f12vw.prod(),W,_ct(wT,wo,l12_cv2_wt),task_group=tg)
        rt.drain(f12vo.cons(),O,_sr(oT,o2,l12_h,l12_cv2_oc*l12_w,l12_cv2_oc*l12_w),wait=True,task_group=tg)
        rt.finish_task_group(tg); wo+=l12_cv2_wt
        # TG4: Upsample → L15_concat[0:128ch]
        tg=rt.task_group()
        rt.fill(fui.prod(),O,_ct(oT,o2,s2),task_group=tg)
        rt.drain(fuo.cons(),O,_sr(oT,o3,l15_h,ups_or,l15_ir),wait=True,task_group=tg)
        rt.finish_task_group(tg)
        # TG5: L15 cv1
        tg=rt.task_group()
        rt.fill(f15i.prod(),O,_ct(oT,o3,s3),task_group=tg)
        rt.fill(f15cw.prod(),W,_ct(wT,wo,l15_c1w),task_group=tg)
        rt.drain(f15co.cons(),O,_sr(oT,o4,l15_h,l15_cv1_oc*l15_w,l15_cr),wait=True,task_group=tg)
        rt.finish_task_group(tg); wo+=l15_c1w
        # TG6: L15 bn0
        tg=rt.task_group()
        rt.fill(f15bi.prod(),O,_sr(oT,o4+l15_hr,l15_h,l15_hr,l15_cr),task_group=tg)
        rt.fill(f15bw1.prod(),W,_ct(wT,wo,l15_bw),task_group=tg)
        rt.fill(f15bw2.prod(),W,_ct(wT,wo+l15_bw,l15_bw),task_group=tg)
        rt.drain(f15bo.cons(),O,_sr(oT,o4+l15_cv1_oc*l15_w,l15_h,l15_hr,l15_cr),wait=True,task_group=tg)
        rt.finish_task_group(tg); wo+=2*l15_bw
        # TG7: L15 cv2 → final
        tg=rt.task_group()
        rt.fill(f15vi.prod(),O,_ct(oT,o4,s4),task_group=tg)
        rt.fill(f15vw.prod(),W,_ct(wT,wo,l15_c2w),task_group=tg)
        rt.drain(f15vo.cons(),O,_sr(oT,o0,l15_h,l15_cv2_oc*l15_w,l15_cv2_oc*l15_w),wait=True,task_group=tg)
        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # l12_l15

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
# C2f L2 full: fused SiLU, 48ch concat [half1(16)|half2(16)|bn0_out(16)],
# optional residual add.
#
# Builds on the simplified C2f by:
#   1. Replacing non-fused conv with fused conv+SiLU (bias packed in weights)
#   2. Adding 48ch concat for cv2: [half1|half2|bn0_out] = 48ch
#   3. Core B forwards half2 to join while doing k3 conv (neighboring bn_inter
#      to Core C saves DMA channels, freeing an output DMA for half2_fwd)
#
# Core mapping (5 cores, 2 columns):
#   Core A (0,2): cv1 k1 SiLU, 32->32ch
#   Core B (0,3): bn0.cv1 k3s1 SiLU, 16->16ch + half2 fwd to join
#                 (bn_inter to Core C is neighboring -> no DMA channel used)
#   Core C (0,4): bn0.cv2 k3s1 SiLU, 16->16ch
#   Core D (1,2): passthrough 16ch (half1 -> join)
#   Core E (1,3): cv2 k1 SiLU, 48->32ch
#
# MemTile(0,1):
#   - wts_all split: 1 in -> 4 out (cv1, bn1, bn2, cv2)
#
# MemTile(1,1):
#   - cv1_out split: 1 in -> 2 out (half1_to_join, half2_to_bn)
#   - join: half1(16ch) + half2_fwd(16ch) + bn_out(16ch) -> cv2_in(48ch)
#
# DMA budget (Core B, key tile):
#   Input DMA 1: half2_to_bn (from MemTile split)
#   Input DMA 2: wt_bn1 (from MemTile weight split)
#   Output DMA 1: half2_fwd (to MemTile join)
#   Neighboring: bn_inter to Core C (no DMA channel)
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
    cv2_ic = 48  # 16ch half1 + 16ch half2 + 16ch bn0_out (joined at MemTile)
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

    # Core B: input(half2, depth=bn_depth) + wt + bn_inter(neighboring, depth=bn_depth)
    #         + j_h2(depth=2) output to join
    coreB = (
        1040 + (bn_depth + 1) * half_row + wt_slot + bn_depth * half_row + 2 * half_row
    )
    assert coreB <= 65536, f"Core B L1: {coreB}B"

    coreC = 1040 + (bn_depth + 1) * half_row + wt_slot + 2 * half_row
    assert coreC <= 65536, f"Core C L1: {coreC}B"

    coreE = 1040 + 2 * cv2_in_row + wt_slot + 2 * cv2_out_row
    assert coreE <= 65536, f"Core E (cv2) L1: {coreE}B"

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
        "conv2dk3_i8_silu_bn_fwd.o",
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

    # Passthrough for half2 forwarding — same .o as k3_silu_bn_kernel
    passthrough_fwd_kernel = Kernel(
        "passthrough_i8_fwd",
        "conv2dk3_i8_silu_bn_fwd.o",
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

    # Join at MemTile(1,1): [half1(16ch) | half2(16ch) | bn0_out(16ch)] = 48ch
    # j_h1 is fed by passthrough Core D (half1 from split)
    # j_h2 is fed by Core B (half2 forwarded during k3 conv)
    # j_bn is fed by Core C (bn0.cv2 output)
    cv2_in = ObjectFifo(cv2_in_row_ty, name="cv2_in", depth=2)
    j_h1, j_h2, j_bn = cv2_in.prod().join(
        offsets=[0, half_row, 2 * half_row],
        obj_types=[half_row_ty, half_row_ty, half_row_ty],
        names=["j_h1", "j_h2", "j_bn"],
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

    def core_fn_bn_with_fwd(of_in, of_wt, of_out, of_fwd, kernel_fn, fwd_fn):
        """bn0.cv1: k3 stride-1 SiLU + forward half2 rows to join.

        Interleaves half2 forwarding with k3 sliding window processing.
        Each input row is forwarded exactly once as it first appears:
          - Top: forward rows 0,1 (from acquire(2))
          - Each middle iter: forward the new row (elems[2] from acquire(3))
          - Bottom: no new rows to forward
        Total forwarded = 2 + (h-2) = h rows.
        """
        w = width
        ci = bn_ch
        co = bn_ch
        h = height
        sz = half_row
        s1 = bn_cv1_shift1
        s2 = bn_cv1_shift2

        elem_wt = of_wt.acquire(1)

        # --- Top row: check=0 ---
        elems = of_in.acquire(2)
        # Forward rows 0 and 1
        fwd0 = of_fwd.acquire(1)
        fwd_fn(elems[0], fwd0, sz)
        of_fwd.release(1)
        fwd1 = of_fwd.acquire(1)
        fwd_fn(elems[1], fwd1, sz)
        of_fwd.release(1)
        # Conv top
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo, w, ci, co, 0, s1, s2)
        of_out.release(1)

        # --- Middle rows: check=1 ---
        for _ in range_(h - 2):
            elems = of_in.acquire(3)
            # Forward the newly acquired row (elems[2])
            fwd_e = of_fwd.acquire(1)
            fwd_fn(elems[2], fwd_e, sz)
            of_fwd.release(1)
            # Conv middle
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo, w, ci, co, 1, s1, s2)
            of_in.release(1)
            of_out.release(1)

        # --- Bottom row: check=2 ---
        elems = of_in.acquire(2)
        # No new rows to forward (already forwarded in middle loop)
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo, w, ci, co, 2, s1, s2)
        of_in.release(2)
        of_out.release(1)

        of_wt.release(1)

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
    # Core B: k3 conv + half2 forwarding. bn_inter to Core C is neighboring
    # (same column, adjacent rows 3→4) so doesn't use DMA channels. This
    # frees an output DMA for half2_fwd (j_h2) to the MemTile join.
    worker_bn1 = Worker(
        core_fn_bn_with_fwd,
        [
            half2_to_bn.cons(bn_depth),
            wt_bn1_f.cons(),
            bn_inter.prod(),
            j_h2.prod(),
            k3_silu_bn_kernel,
            passthrough_fwd_kernel,
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
    # Core E: cv2 now takes 48ch input [half1|half2|bn0_out]
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


# ---------------------------------------------------------------------------
# Step 10: C2f L6 (n=2 bottlenecks) -- 128ch, 40x40
#
# Same multi-phase pattern as L4 with doubled channel widths:
#   Phase A: cv1(128->128, k1) -> drain to DDR scratch (half1+half2 in-place)
#   Phase B: half2(64ch) -> bn0.cv1(k3) -> bn0.cv2(k3) -> +half2(add) -> bn0_out to DDR
#   Phase C: bn0_out(64ch) -> bn1.cv1(k3) -> bn1.cv2(k3) -> +bn0_out(add) -> bn1_out to DDR
#   Phase D: Read concat [half1|half2|bn0_out|bn1_out]=256ch -> cv2(256->128, k1) -> output
#
# Core mapping (8 cores, 2 columns):
#   Col 0: cv1(0,2), bn0.cv1(0,3), bn0.cv2(0,4), bn0_add(0,5)
#   Col 1: bn1.cv1(1,2), bn1.cv2(1,3), bn1_add(1,4), cv2(1,5)
#
# L1 budget at 40x40:
#   cv1: 1040 + 2*5120 + 16384 + 2*5120 = 37904  (OK)
#   bn k3: 1040 + 5*2560 + 36864 + 2*2560 = 55824  (OK)
#   add:  1040 + 6*2560 = 16400  (OK)
#   cv2: 1040 + 2*10240 + 32768 + 2*5120 = 64528  (tight, fits 65536)
# ---------------------------------------------------------------------------


def my_dataflow_c2f_l6(
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
    """C2f block for L6: 128ch input, n=2 bottlenecks with residual add.

    Multi-phase execution building concat in-place:

    DDR output buffer: [final_output(128ch*H*W) | concat(256ch*H*W)]

    Phase A: cv1(128->128, k1) -> drain to concat[0:128ch]
             half1=[0:64ch], half2=[64:128ch] placed directly.
    Phase B: Read half2(64ch) from concat[64:128ch]
             -> bn0.cv1(k3) -> bn0.cv2(k3) -> add(+half2_skip)
             -> drain bn0_out to concat[128:192ch]
    Phase C: Read bn0_out(64ch) from concat[128:192ch]
             -> bn1.cv1(k3) -> bn1.cv2(k3) -> add(+bn0_out_skip)
             -> drain bn1_out to concat[192:256ch]
    Phase D: Read concat(256ch) linearly -> cv2(256->128, k1) -> output

    Core mapping:
      Phase A: cv1(0,2) [1 core]
      Phase B: bn0.cv1(0,3), bn0.cv2(0,4), bn0_add(0,5) [3 cores]
      Phase C: bn1.cv1(1,2), bn1.cv2(1,3), bn1_add(1,4) [3 cores]
      Phase D: cv2(1,5) [1 core]

    Args:
        dev: Device type string.
        height: Spatial height (40 for L6).
        width: Spatial width (40 for L6).
        in_channels: Input channels (128).
        cv1_scale-cv2_scale: requantization shifts.
    """
    xfr_dtype = np.int8

    assert in_channels == 128
    cv1_oc = 128
    bn_ch = 64
    cv2_ic = 256
    cv2_oc = 128

    # Row sizes
    input_row = in_channels * width
    cv1_out_row = cv1_oc * width
    half_row = bn_ch * width
    cv2_in_row = cv2_ic * width
    cv2_out_row = cv2_oc * width

    # Weight sizes (non-fused, no bias)
    cv1_wt = cv1_oc * in_channels  # 16384
    bn_k3_wt = bn_ch * bn_ch * 9  # 36864
    cv2_wt = cv2_oc * cv2_ic  # 32768

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

    # DDR output buffer: [final_output(128ch) | concat(256ch)]
    # concat = [half1(64ch) | half2(64ch) | bn0_out(64ch) | bn1_out(64ch)]
    concat_offset = total_output
    output_buf_size = total_output + total_concat

    # Weight layout: [cv1_wt | bn0cv1_wt | bn0cv2_wt | bn1cv1_wt | bn1cv2_wt | cv2_wt]
    bn_wt_slot = bn_k3_wt
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
    in_fifo = ObjectFifo(input_row_ty, name="c2f_l6_in", depth=2)
    cv1_wt_fifo = ObjectFifo(cv1_wt_ty, name="l6_cv1_wt", depth=1)
    cv1_out_fifo = ObjectFifo(cv1_out_row_ty, name="l6_cv1_out", depth=2)

    # --- Phase B FIFOs: bn0 pipeline ---
    bn0_in_fifo = ObjectFifo(half_row_ty, name="l6_bn0_in", depth=bn_depth)
    bn0_skip_fifo = ObjectFifo(half_row_ty, name="l6_bn0_skip", depth=2)
    bn0_wts_fifo = ObjectFifo(bn_wts_pair_ty, name="l6_bn0_wts", depth=1)
    bn0_wt1_f, bn0_wt2_f = bn0_wts_fifo.cons().split(
        offsets=[0, bn_wt_slot],
        obj_types=[bn_wt_ty, bn_wt_ty],
        names=["l6_bn0_wt1", "l6_bn0_wt2"],
        depths=[1, 1],
        placement=Tile(0, 1),
    )
    bn0_inter = ObjectFifo(half_row_ty, name="l6_bn0_inter", depth=bn_depth)
    bn0_cv2_out = ObjectFifo(half_row_ty, name="l6_bn0_cv2_out", depth=2)
    bn0_out_fifo = ObjectFifo(half_row_ty, name="l6_bn0_out", depth=2)

    # --- Phase C FIFOs: bn1 pipeline ---
    bn1_in_fifo = ObjectFifo(half_row_ty, name="l6_bn1_in", depth=bn_depth)
    bn1_skip_fifo = ObjectFifo(half_row_ty, name="l6_bn1_skip", depth=2)
    bn1_wts_fifo = ObjectFifo(bn_wts_pair_ty, name="l6_bn1_wts", depth=1)
    bn1_wt1_f, bn1_wt2_f = bn1_wts_fifo.cons().split(
        offsets=[0, bn_wt_slot],
        obj_types=[bn_wt_ty, bn_wt_ty],
        names=["l6_bn1_wt1", "l6_bn1_wt2"],
        depths=[1, 1],
        placement=Tile(1, 1),
    )
    bn1_inter = ObjectFifo(half_row_ty, name="l6_bn1_inter", depth=bn_depth)
    bn1_cv2_out = ObjectFifo(half_row_ty, name="l6_bn1_cv2_out", depth=2)
    bn1_out_fifo = ObjectFifo(half_row_ty, name="l6_bn1_out", depth=2)

    # --- Phase D FIFOs: cv2 ---
    cv2_in_fifo = ObjectFifo(cv2_in_row_ty, name="l6_cv2_in", depth=2)
    cv2_wt_fifo = ObjectFifo(cv2_wt_ty, name="l6_cv2_wt", depth=1)
    cv2_out_fifo = ObjectFifo(cv2_out_row_ty, name="l6_cv2_out", depth=2)

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

        # Drain cv1 output (128ch) with strided write into concat rows (256ch each).
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

        # Read half2 from concat[64:128ch] -- strided read from 256ch rows.
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

        # Drain bn0_out with strided write to concat[128:192ch]
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

        # Read bn0_out from concat[128:192ch] -- strided
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

        # Drain bn1_out with strided write to concat[192:256ch]
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

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # c2f_l6


# ---------------------------------------------------------------------------
# Step 11: Backbone Phase 1 — L0→L1→L2(C2f)→L3 in one PDI
#
# Three sequential task groups within one PDI:
#   TG1: L0(k3s2) -> L1(k3s2) pipeline, output to DDR scratch_A
#   TG2: C2f L2 full (cv1->split->{bn0.cv1->bn0.cv2,pass}->join(48ch)->cv2),
#        reads scratch_A, writes scratch_B
#   TG3: L3(k3s2), reads scratch_B, writes final output
#
# Tile placement (8 cores, 2 columns):
#   Col 0: L0(0,2), L1(0,3), passthrough(0,4), L3(0,5)
#   Col 1: cv1(1,2), bn0.cv1(1,3), bn0.cv2(1,4), cv2(1,5)
#
# bn0.cv1(1,3)->bn0.cv2(1,4) uses neighboring tile (same column, adjacent).
# passthrough(0,4) crosses columns for half1 routing to/from MemTile(1,1).
#
# Weight delivery:
#   MemTile(0,1): TG1 weight split -> wt_l0, wt_l1
#   MemTile(1,1): TG2 C2f weight split -> wt_cv1, wt_bn1, wt_bn2, wt_cv2
#                 Also hosts cv1_out split and 48ch join
#   L3 weight:   Direct DDR -> Tile(0,5)
#
# DDR output buffer: [L3_output | scratch_A | scratch_B]
# ---------------------------------------------------------------------------


def my_dataflow_backbone_phase1(
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
    # L2 C2f params (fused SiLU)
    cv1_shift1,
    cv1_shift2,
    bn_cv1_shift1,
    bn_cv1_shift2,
    bn_cv2_shift1,
    bn_cv2_shift2,
    cv2_shift1,
    cv2_shift2,
    # L3 params
    l3_oc,
    l3_shift1,
    l3_shift2,
):
    """Backbone Phase 1: L0->L1->L2(C2f)->L3 in one PDI.

    Chains four backbone layers with DDR scratch between task groups:
      TG1: L0(k3s2, IC->L0_OC) -> L1(k3s2, L0_OC->L1_OC) -> scratch_A
      TG2: C2f L2 (L1_OC->L1_OC, n=1 bottleneck, fused SiLU) -> scratch_B
      TG3: L3(k3s2, L1_OC->L3_OC) -> final output

    Args:
        dev: Device type string.
        l0_height, l0_width: Input spatial dims (e.g. 640, 640).
        l0_ic: Input channels (8 for padded RGB).
        l0_oc: L0 output channels (16).
        l0_shift1, l0_shift2: L0 fused SiLU params.
        l1_oc: L1 output channels (32).
        l1_shift1, l1_shift2: L1 fused SiLU params.
        cv1_shift1..cv2_shift2: C2f L2 fused SiLU params (4 layers).
        l3_oc: L3 output channels (64).
        l3_shift1, l3_shift2: L3 fused SiLU params.
    """
    xfr_dtype = np.int8

    # --- Derived dimensions ---
    l0_out_h = l0_height // 2
    l0_out_w = l0_width // 2

    l1_ic = l0_oc
    l1_height = l0_out_h
    l1_width = l0_out_w
    l1_out_h = l1_height // 2
    l1_out_w = l1_width // 2

    # C2f L2: same spatial dims as L1 output, ic = l1_oc
    c2f_ic = l1_oc
    c2f_height = l1_out_h
    c2f_width = l1_out_w
    assert c2f_ic == 32, f"C2f L2 requires 32ch input, got {c2f_ic}"
    cv1_oc = 32
    bn_ch = 16
    cv2_ic = 48  # 16 + 16 + 16
    cv2_oc = 32

    # L3: same spatial as C2f output (stride-1), then stride-2
    l3_ic = cv2_oc
    l3_height = c2f_height
    l3_width = c2f_width
    l3_out_h = l3_height // 2
    l3_out_w = l3_width // 2

    # --- Row sizes ---
    l0_input_row = l0_ic * l0_width
    inter01_row = l0_oc * l0_out_w
    l1_out_row = l1_oc * l1_out_w  # = c2f input row

    c2f_input_row = c2f_ic * c2f_width
    cv1_out_row = cv1_oc * c2f_width
    half_row = bn_ch * c2f_width
    cv2_in_row = cv2_ic * c2f_width
    cv2_out_row = cv2_oc * c2f_width  # = l3 input row

    l3_input_row = l3_ic * l3_width
    l3_output_row = l3_oc * l3_out_w

    # --- Weight sizes (fused: weights + int32 bias) ---
    l0_wt_size = l0_oc * l0_ic * 9 + l0_oc * 4
    l1_wt_size = l1_oc * l1_ic * 9 + l1_oc * 4
    tg1_wt_slot = max(l0_wt_size, l1_wt_size)
    tg1_total_wt = 2 * tg1_wt_slot

    cv1_wt_size = cv1_oc * c2f_ic + cv1_oc * 4  # k1 fused
    bn_cv1_wt_size = bn_ch * bn_ch * 9 + bn_ch * 4  # k3 fused
    bn_cv2_wt_size = bn_ch * bn_ch * 9 + bn_ch * 4  # k3 fused
    cv2_wt_size = cv2_oc * cv2_ic + cv2_oc * 4  # k1 fused
    c2f_wt_slot = max(cv1_wt_size, bn_cv1_wt_size, bn_cv2_wt_size, cv2_wt_size)
    c2f_total_wt = 4 * c2f_wt_slot

    l3_wt_size = l3_oc * l3_ic * 9 + l3_oc * 4

    total_weights = tg1_total_wt + c2f_total_wt + l3_wt_size

    # --- Tensor totals ---
    total_input = l0_ic * l0_height * l0_width
    scratch_a_size = l1_oc * l1_out_h * l1_out_w  # L1 output = C2f input
    scratch_b_size = cv2_oc * c2f_height * c2f_width  # C2f output = L3 input
    total_output = l3_oc * l3_out_h * l3_out_w
    total_output_buf = total_output + scratch_a_size + scratch_b_size

    # --- L1 budget checks ---
    # TG1: L0 and L1 use max_row for shared kernel type
    spine_max_row = max(l0_input_row, inter01_row, l1_out_row)

    l0_input_depth = 4
    l0_l1 = 1040 + (l0_input_depth + 1) * l0_input_row + tg1_wt_slot + 2 * inter01_row
    assert l0_l1 <= 65536, f"L0 L1 budget exceeded: {l0_l1}B"

    l1_input_depth = 4
    l1_l1 = 1040 + (l1_input_depth + 1) * inter01_row + tg1_wt_slot + 2 * l1_out_row
    assert l1_l1 <= 65536, f"L1 L1 budget exceeded: {l1_l1}B"

    # TG2: C2f cores
    bn_depth = 4
    cv1_l1 = 1040 + 2 * c2f_input_row + c2f_wt_slot + 2 * cv1_out_row
    assert cv1_l1 <= 65536, f"cv1 L1 budget exceeded: {cv1_l1}B"

    # bn0.cv1: input(half2, depth=bn_depth) + wt + bn_inter(neighboring) + j_h2
    bn1_l1 = (
        1040
        + (bn_depth + 1) * half_row
        + c2f_wt_slot
        + bn_depth * half_row
        + 2 * half_row
    )
    assert bn1_l1 <= 65536, f"bn0.cv1 L1 budget exceeded: {bn1_l1}B"

    # bn0.cv2: input(bn_inter, neighboring) + wt + output(j_bn)
    bn2_l1 = 1040 + (bn_depth + 1) * half_row + c2f_wt_slot + 2 * half_row
    assert bn2_l1 <= 65536, f"bn0.cv2 L1 budget exceeded: {bn2_l1}B"

    pass_l1 = 1040 + 2 * half_row + 2 * half_row
    assert pass_l1 <= 65536, f"passthrough L1 budget exceeded: {pass_l1}B"

    cv2_l1 = 1040 + 2 * cv2_in_row + c2f_wt_slot + 2 * cv2_out_row
    assert cv2_l1 <= 65536, f"cv2 L1 budget exceeded: {cv2_l1}B"

    # TG3: L3
    l3_input_depth = 4
    l3_l1 = 1040 + (l3_input_depth + 1) * l3_input_row + l3_wt_size + 2 * l3_output_row
    assert l3_l1 <= 65536, f"L3 L1 budget exceeded: {l3_l1}B"

    dev_ty = NPU2()

    # --- Types ---
    # TG1: shared row type for k3s2 kernel (IC*W is constant across stride-2 layers)
    spine_row_ty = np.ndarray[(spine_max_row,), np.dtype[xfr_dtype]]
    tg1_wt_ty = np.ndarray[(tg1_wt_slot,), np.dtype[xfr_dtype]]
    tg1_wts_all_ty = np.ndarray[(tg1_total_wt,), np.dtype[xfr_dtype]]

    # TG2: C2f types
    c2f_input_row_ty = np.ndarray[(c2f_input_row,), np.dtype[xfr_dtype]]
    cv1_out_row_ty = np.ndarray[(cv1_out_row,), np.dtype[xfr_dtype]]
    half_row_ty = np.ndarray[(half_row,), np.dtype[xfr_dtype]]
    cv2_in_row_ty = np.ndarray[(cv2_in_row,), np.dtype[xfr_dtype]]
    cv2_out_row_ty = np.ndarray[(cv2_out_row,), np.dtype[xfr_dtype]]
    c2f_wt_ty = np.ndarray[(c2f_wt_slot,), np.dtype[xfr_dtype]]
    c2f_wts_all_ty = np.ndarray[(c2f_total_wt,), np.dtype[xfr_dtype]]

    # TG3: L3 types
    l3_input_row_ty = np.ndarray[(l3_input_row,), np.dtype[xfr_dtype]]
    l3_output_row_ty = np.ndarray[(l3_output_row,), np.dtype[xfr_dtype]]
    l3_wt_ty = np.ndarray[(l3_wt_size,), np.dtype[xfr_dtype]]

    # DDR-level types
    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_weights,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_buf,), np.dtype[xfr_dtype]]

    # --- Kernel declarations ---
    # L0, L1, L3: shared k3s2 fused SiLU kernel
    k3s2_silu_kernel = Kernel(
        "conv2dk3s2_i8_silu",
        "conv2dk3_i8_silu.o",
        [
            spine_row_ty,
            spine_row_ty,
            spine_row_ty,
            tg1_wt_ty,
            spine_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # L3 needs its own kernel because weight type differs
    l3_k3s2_kernel = Kernel(
        "conv2dk3s2_i8_silu_l3",
        "conv2dk3_i8_silu_l3.o",
        [
            l3_input_row_ty,
            l3_input_row_ty,
            l3_input_row_ty,
            l3_wt_ty,
            l3_output_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # C2f kernels
    k1_silu_kernel = Kernel(
        "conv2dk1_i8_silu",
        "conv2dk1_i8_silu.o",
        [
            c2f_input_row_ty,
            c2f_wt_ty,
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
        "conv2dk3_i8_silu_bn_fwd.o",
        [
            half_row_ty,
            half_row_ty,
            half_row_ty,
            c2f_wt_ty,
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

    passthrough_fwd_kernel = Kernel(
        "passthrough_i8_fwd",
        "conv2dk3_i8_silu_bn_fwd.o",
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
            c2f_wt_ty,
            cv2_out_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # ===== ObjectFIFOs =====

    # --- TG1: L0->L1 ---
    in_fifo = ObjectFifo(spine_row_ty, name="l0_in", depth=l0_input_depth)

    tg1_wts_fifo = ObjectFifo(tg1_wts_all_ty, name="tg1_wts", depth=1)
    wt_l0, wt_l1 = tg1_wts_fifo.cons().split(
        offsets=[0, tg1_wt_slot],
        obj_types=[tg1_wt_ty, tg1_wt_ty],
        names=["wt_l0", "wt_l1"],
        depths=[1, 1],
        placement=Tile(0, 1),
    )

    inter01_fifo = ObjectFifo(spine_row_ty, name="inter_01", depth=l1_input_depth)
    l1_out_fifo = ObjectFifo(spine_row_ty, name="l1_out", depth=2)

    # --- TG2: C2f L2 ---
    c2f_in_fifo = ObjectFifo(c2f_input_row_ty, name="c2f_in", depth=2)

    c2f_wts_fifo = ObjectFifo(c2f_wts_all_ty, name="c2f_wts", depth=1)
    # Place C2f weight split at MemTile(0,1) to avoid exceeding
    # MemTile(1,1) output DMA limit (cv1_out split + join already use 3).
    wt_cv1_f, wt_bn1_f, wt_bn2_f, wt_cv2_f = c2f_wts_fifo.cons().split(
        offsets=[0, c2f_wt_slot, 2 * c2f_wt_slot, 3 * c2f_wt_slot],
        obj_types=[c2f_wt_ty] * 4,
        names=["wt_cv1", "wt_bn1", "wt_bn2", "wt_cv2"],
        depths=[1, 1, 1, 1],
        placement=Tile(0, 1),
    )

    cv1_out = ObjectFifo(cv1_out_row_ty, name="cv1_out", depth=2)

    # Split cv1_out at MemTile(1,1): half1 -> passthrough, half2 -> bn0.cv1
    half1_to_join, half2_to_bn = cv1_out.cons().split(
        offsets=[0, half_row],
        obj_types=[half_row_ty, half_row_ty],
        names=["half1_to_join", "half2_to_bn"],
        depths=[2, bn_depth],
        placement=Tile(1, 1),
    )

    # bn_inter: neighboring tile (1,3)->(1,4)
    bn_inter = ObjectFifo(half_row_ty, name="bn_inter", depth=bn_depth)

    # Join at MemTile(1,1): [half1|half2|bn0_out] = 48ch
    cv2_in = ObjectFifo(cv2_in_row_ty, name="cv2_in", depth=2)
    j_h1, j_h2, j_bn = cv2_in.prod().join(
        offsets=[0, half_row, 2 * half_row],
        obj_types=[half_row_ty, half_row_ty, half_row_ty],
        names=["j_h1", "j_h2", "j_bn"],
        placement=Tile(1, 1),
    )

    c2f_out_fifo = ObjectFifo(cv2_out_row_ty, name="c2f_out", depth=2)

    # --- TG3: L3 ---
    l3_in_fifo = ObjectFifo(l3_input_row_ty, name="l3_in", depth=l3_input_depth)
    l3_wt_fifo = ObjectFifo(l3_wt_ty, name="l3_wt", depth=1)
    l3_out_fifo = ObjectFifo(l3_output_row_ty, name="l3_out", depth=2)

    # ===== Core functions =====

    # TG1: k3s2 fused SiLU (reuse pattern from spine_5layer)
    def make_k3s2_silu_core_fn(in_width, in_ch, out_ch, out_h_val, s1, s2):
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

    # TG2: C2f core functions (reuse pattern from c2f_l2_full)
    def core_fn_cv1(of_in, of_wt, of_out, kernel_fn):
        w = c2f_width
        ci = c2f_ic
        co = cv1_oc
        s1 = cv1_shift1
        s2 = cv1_shift2
        elem_wt = of_wt.acquire(1)
        for _ in range_(c2f_height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, s1, s2)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    def core_fn_bn_with_fwd(of_in, of_wt, of_out, of_fwd, kernel_fn, fwd_fn):
        w = c2f_width
        ci = bn_ch
        co = bn_ch
        h = c2f_height
        sz = half_row
        s1 = bn_cv1_shift1
        s2 = bn_cv1_shift2

        elem_wt = of_wt.acquire(1)

        # Top row: check=0
        elems = of_in.acquire(2)
        fwd0 = of_fwd.acquire(1)
        fwd_fn(elems[0], fwd0, sz)
        of_fwd.release(1)
        fwd1 = of_fwd.acquire(1)
        fwd_fn(elems[1], fwd1, sz)
        of_fwd.release(1)
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo, w, ci, co, 0, s1, s2)
        of_out.release(1)

        # Middle rows: check=1
        for _ in range_(h - 2):
            elems = of_in.acquire(3)
            fwd_e = of_fwd.acquire(1)
            fwd_fn(elems[2], fwd_e, sz)
            of_fwd.release(1)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo, w, ci, co, 1, s1, s2)
            of_in.release(1)
            of_out.release(1)

        # Bottom row: check=2
        elems = of_in.acquire(2)
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo, w, ci, co, 2, s1, s2)
        of_in.release(2)
        of_out.release(1)

        of_wt.release(1)

    def core_fn_bn_cv2(of_in, of_wt, of_out, kernel_fn):
        w = c2f_width
        ci = bn_ch
        co = bn_ch
        h = c2f_height
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
        for _ in range_(c2f_height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, eo, sz)
            of_in.release(1)
            of_out.release(1)

    def core_fn_cv2(of_in, of_wt, of_out, kernel_fn):
        w = c2f_width
        ci = cv2_ic
        co = cv2_oc
        s1 = cv2_shift1
        s2 = cv2_shift2
        elem_wt = of_wt.acquire(1)
        for _ in range_(c2f_height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, s1, s2)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    # TG3: L3 k3s2 fused SiLU
    def core_fn_l3(of_in, of_wt, of_out, kernel_fn):
        x_dim = l3_width
        ci = l3_ic
        co = l3_oc
        oh = l3_out_h
        s1 = l3_shift1
        s2 = l3_shift2

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

    # ===== Workers =====
    # TG1
    worker_l0 = Worker(
        core_fn_l0,
        [in_fifo.cons(), wt_l0.cons(), inter01_fifo.prod(), k3s2_silu_kernel],
        placement=Tile(0, 2),
    )
    worker_l1 = Worker(
        core_fn_l1,
        [
            inter01_fifo.cons(l1_input_depth),
            wt_l1.cons(),
            l1_out_fifo.prod(),
            k3s2_silu_kernel,
        ],
        placement=Tile(0, 3),
    )

    # TG2
    worker_cv1 = Worker(
        core_fn_cv1,
        [c2f_in_fifo.cons(), wt_cv1_f.cons(), cv1_out.prod(), k1_silu_kernel],
        placement=Tile(1, 2),
    )
    worker_bn1 = Worker(
        core_fn_bn_with_fwd,
        [
            half2_to_bn.cons(bn_depth),
            wt_bn1_f.cons(),
            bn_inter.prod(),
            j_h2.prod(),
            k3_silu_bn_kernel,
            passthrough_fwd_kernel,
        ],
        placement=Tile(1, 3),
    )
    worker_bn2 = Worker(
        core_fn_bn_cv2,
        [
            bn_inter.cons(bn_depth),
            wt_bn2_f.cons(),
            j_bn.prod(),
            k3_silu_bn_kernel,
        ],
        placement=Tile(1, 4),
    )
    worker_pass = Worker(
        core_fn_passthrough,
        [half1_to_join.cons(), j_h1.prod(), passthrough_kernel],
        placement=Tile(0, 4),
    )
    worker_cv2 = Worker(
        core_fn_cv2,
        [cv2_in.cons(), wt_cv2_f.cons(), c2f_out_fifo.prod(), k1_silu_cv2_kernel],
        placement=Tile(1, 5),
    )

    # TG3
    worker_l3 = Worker(
        core_fn_l3,
        [l3_in_fifo.cons(), l3_wt_fifo.cons(), l3_out_fifo.prod(), l3_k3s2_kernel],
        placement=Tile(0, 5),
    )

    # ===== Runtime sequence =====
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W_buf, O):
        rt.start(
            worker_l0,
            worker_l1,
            worker_cv1,
            worker_bn1,
            worker_bn2,
            worker_pass,
            worker_cv2,
            worker_l3,
        )

        # ===== TG1: L0->L1 pipeline to DDR scratch_A =====
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

        # Fill TG1 weights
        tg1_wt_d3, tg1_wt_d2, tg1_wt_d1, tg1_wt_d0 = _factorize_tensor(tg1_total_wt)
        rt.fill(
            tg1_wts_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=0,
                sizes=[tg1_wt_d3, tg1_wt_d2, tg1_wt_d1, tg1_wt_d0],
                strides=[
                    tg1_wt_d2 * tg1_wt_d1 * tg1_wt_d0,
                    tg1_wt_d1 * tg1_wt_d0,
                    tg1_wt_d0,
                    1,
                ],
            ),
            task_group=tg1,
        )

        # Drain L1 output to scratch_A
        scratch_a_offset = total_output
        sa_d3, sa_d2, sa_d1, sa_d0 = _factorize_tensor(scratch_a_size)
        rt.drain(
            l1_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=scratch_a_offset,
                sizes=[sa_d3, sa_d2, sa_d1, sa_d0],
                strides=[sa_d2 * sa_d1 * sa_d0, sa_d1 * sa_d0, sa_d0, 1],
            ),
            wait=True,
            task_group=tg1,
        )

        rt.finish_task_group(tg1)

        # ===== TG2: C2f L2, reads scratch_A -> writes scratch_B =====
        tg2 = rt.task_group()

        # Fill C2f input from scratch_A
        c2f_in_d3, c2f_in_d2, c2f_in_d1, c2f_in_d0 = _factorize_tensor(scratch_a_size)
        rt.fill(
            c2f_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=scratch_a_offset,
                sizes=[c2f_in_d3, c2f_in_d2, c2f_in_d1, c2f_in_d0],
                strides=[
                    c2f_in_d2 * c2f_in_d1 * c2f_in_d0,
                    c2f_in_d1 * c2f_in_d0,
                    c2f_in_d0,
                    1,
                ],
            ),
            task_group=tg2,
        )

        # Fill C2f weights
        c2f_wt_offset = tg1_total_wt
        c2f_wt_d3, c2f_wt_d2, c2f_wt_d1, c2f_wt_d0 = _factorize_tensor(c2f_total_wt)
        rt.fill(
            c2f_wts_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=c2f_wt_offset,
                sizes=[c2f_wt_d3, c2f_wt_d2, c2f_wt_d1, c2f_wt_d0],
                strides=[
                    c2f_wt_d2 * c2f_wt_d1 * c2f_wt_d0,
                    c2f_wt_d1 * c2f_wt_d0,
                    c2f_wt_d0,
                    1,
                ],
            ),
            task_group=tg2,
        )

        # Drain C2f output to scratch_B
        scratch_b_offset = total_output + scratch_a_size
        sb_d3, sb_d2, sb_d1, sb_d0 = _factorize_tensor(scratch_b_size)
        rt.drain(
            c2f_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=scratch_b_offset,
                sizes=[sb_d3, sb_d2, sb_d1, sb_d0],
                strides=[sb_d2 * sb_d1 * sb_d0, sb_d1 * sb_d0, sb_d0, 1],
            ),
            wait=True,
            task_group=tg2,
        )

        rt.finish_task_group(tg2)

        # ===== TG3: L3, reads scratch_B -> writes final output =====
        tg3 = rt.task_group()

        # Fill L3 input from scratch_B
        l3_in_d3, l3_in_d2, l3_in_d1, l3_in_d0 = _factorize_tensor(scratch_b_size)
        rt.fill(
            l3_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=scratch_b_offset,
                sizes=[l3_in_d3, l3_in_d2, l3_in_d1, l3_in_d0],
                strides=[
                    l3_in_d2 * l3_in_d1 * l3_in_d0,
                    l3_in_d1 * l3_in_d0,
                    l3_in_d0,
                    1,
                ],
            ),
            task_group=tg3,
        )

        # Fill L3 weight
        l3_wt_offset = tg1_total_wt + c2f_total_wt
        l3_wt_d3, l3_wt_d2, l3_wt_d1, l3_wt_d0 = _factorize_tensor(l3_wt_size)
        rt.fill(
            l3_wt_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=l3_wt_offset,
                sizes=[l3_wt_d3, l3_wt_d2, l3_wt_d1, l3_wt_d0],
                strides=[
                    l3_wt_d2 * l3_wt_d1 * l3_wt_d0,
                    l3_wt_d1 * l3_wt_d0,
                    l3_wt_d0,
                    1,
                ],
            ),
            task_group=tg3,
        )

        # Drain L3 output to final (offset 0)
        out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output)
        rt.drain(
            l3_out_fifo.cons(),
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

        rt.finish_task_group(tg3)

    return Program(dev_ty, rt).resolve_program(
        SequentialPlacer()
    )  # backbone_phase1 L0->L1->L2(C2f)->L3


# ---------------------------------------------------------------------------
# Step 12: Combined L4(C2f) + L5(k3s2, single-core OC streaming) in one PDI
#
# Phases A-D: C2f L4 (identical to my_dataflow_c2f_l4)
# Phase E: L5 k3s2 64->128, single core with OC streaming
#          Re-streams L4 output for each OC group via stride-0 DMA
#          Uses proven OC streaming pattern from my_dataflow_fused_oc_streaming
#
# Tile placement (9 cores, 3 columns):
#   Col 0: L4.cv1(0,2), L4.bn0.cv1(0,3), L4.bn0.cv2(0,4), L4.bn0_add(0,5)
#   Col 1: L4.bn1.cv1(1,2), L4.bn1.cv2(1,3), L4.bn1_add(1,4), L4.cv2(1,5)
#   Col 2: L5(2,2) [single core, OC streaming]
#
# When l5_oc=0, only phases A-D run (L4-only mode for Step 1 testing).
# ---------------------------------------------------------------------------


def my_dataflow_l4_l5_combined(
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
    # L5 params (optional, set l5_oc=0 for L4-only mode)
    l5_oc=0,
    l5_shift1=0,
    l5_shift2=0,
):
    """Combined L4(C2f) + L5(k3s2) in one PDI.

    When l5_oc=0: L4-only mode (phases A-D, 8 cores, 2 columns).
    When l5_oc>0: L4+L5 mode (phases A-E, 9 cores, 3 columns).

    Phase A: cv1(64->64, k1) -> drain to concat[0:64ch]
    Phase B: bn0 pipeline (half2 -> k3 -> k3 -> add -> concat[64:96ch])
    Phase C: bn1 pipeline (bn0_out -> k3 -> k3 -> add -> concat[96:128ch])
    Phase D: cv2(128->64, k1) -> L4 output
    Phase E: L5 k3s2 64->l5_oc, single-core OC streaming -> L5 output

    DDR output buffer layout:
      L4-only: [L4_output(64ch*H*W) | concat(128ch*H*W)]
      L4+L5:   [L5_output(l5_oc*H/2*W/2) | L4_scratch(64ch*H*W) | concat(128ch*H*W)]

    Args:
        dev: Device type string.
        height: Spatial height (80 for L4).
        width: Spatial width (80 for L4).
        in_channels: Input channels (64).
        cv1_scale..cv2_scale: C2f requantization shifts.
        l5_oc: L5 output channels (128), or 0 for L4-only.
        l5_shift1, l5_shift2: L5 fused SiLU params.
    """
    xfr_dtype = np.int8
    l5_mode = l5_oc > 0

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

    # Weight sizes (non-fused, no bias for C2f)
    cv1_wt = cv1_oc * in_channels  # 4096
    bn_k3_wt = bn_ch * bn_ch * 9  # 9216
    cv2_wt = cv2_oc * cv2_ic  # 8192

    total_input = in_channels * height * width
    l4_output_size = cv2_oc * height * width
    total_concat = cv2_ic * height * width

    # --- L5 dimensions (single-core OC streaming) ---
    if l5_mode:
        l5_ic = cv2_oc  # 64
        l5_height = height  # 80
        l5_width = width  # 80
        l5_out_h = l5_height // 2  # 40
        l5_out_w = l5_width // 2  # 40
        l5_stride = 2

        # Compute OC streaming parameters
        l5_oc_chunk, l5_n_oc_groups, l5_input_depth = _compute_oc_streaming_params(
            l5_ic, l5_oc, l5_width, l5_stride
        )

        l5_input_row = l5_ic * l5_width
        l5_wt_chunk = l5_oc_chunk * l5_ic * 9 + l5_oc_chunk * 4
        l5_output_elem = l5_oc_chunk * l5_out_w
        l5_total_wt = l5_n_oc_groups * l5_wt_chunk

        l5_total_output = l5_oc * l5_out_h * l5_out_w
        l5_total_input = l5_ic * l5_height * l5_width
        l5_output_row_total = l5_oc * l5_out_w

    # --- L1 budget checks (L4 C2f) ---
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

    # --- DDR output buffer layout ---
    if l5_mode:
        # [L5_output | L4_scratch | concat]
        l4_scratch_offset = l5_total_output
        concat_offset = l5_total_output + l4_output_size
        output_buf_size = l5_total_output + l4_output_size + total_concat
    else:
        # [L4_output | concat]
        l4_scratch_offset = 0
        concat_offset = l4_output_size
        output_buf_size = l4_output_size + total_concat

    # Weight layout: [cv1 | bn0cv1 | bn0cv2 | bn1cv1 | bn1cv2 | cv2 | (l5 wt chunks)]
    bn_wt_slot = bn_k3_wt
    l4_total_wt = cv1_wt + 4 * bn_wt_slot + cv2_wt
    total_wt = l4_total_wt + (l5_total_wt if l5_mode else 0)

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

    if l5_mode:
        l5_input_row_ty = np.ndarray[(l5_input_row,), np.dtype[xfr_dtype]]
        l5_output_row_ty = np.ndarray[(l5_output_elem,), np.dtype[xfr_dtype]]
        l5_wt_ty = np.ndarray[(l5_wt_chunk,), np.dtype[xfr_dtype]]

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

    if l5_mode:
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

    # --- Phase A FIFOs: cv1 ---
    in_fifo = ObjectFifo(input_row_ty, name="p2_c2f_in", depth=2)
    cv1_wt_fifo = ObjectFifo(cv1_wt_ty, name="p2_cv1_wt", depth=1)
    cv1_out_fifo = ObjectFifo(cv1_out_row_ty, name="p2_cv1_out", depth=2)

    # --- Phase B FIFOs: bn0 pipeline ---
    bn0_in_fifo = ObjectFifo(half_row_ty, name="p2_bn0_in", depth=bn_depth)
    bn0_skip_fifo = ObjectFifo(half_row_ty, name="p2_bn0_skip", depth=2)
    bn0_wts_fifo = ObjectFifo(bn_wts_pair_ty, name="p2_bn0_wts", depth=1)
    bn0_wt1_f, bn0_wt2_f = bn0_wts_fifo.cons().split(
        offsets=[0, bn_wt_slot],
        obj_types=[bn_wt_ty, bn_wt_ty],
        names=["p2_bn0_wt1", "p2_bn0_wt2"],
        depths=[1, 1],
        placement=Tile(0, 1),
    )
    bn0_inter = ObjectFifo(half_row_ty, name="p2_bn0_inter", depth=bn_depth)
    bn0_cv2_out = ObjectFifo(half_row_ty, name="p2_bn0_cv2_out", depth=2)
    bn0_out_fifo = ObjectFifo(half_row_ty, name="p2_bn0_out", depth=2)

    # --- Phase C FIFOs: bn1 pipeline ---
    bn1_in_fifo = ObjectFifo(half_row_ty, name="p2_bn1_in", depth=bn_depth)
    bn1_skip_fifo = ObjectFifo(half_row_ty, name="p2_bn1_skip", depth=2)
    bn1_wts_fifo = ObjectFifo(bn_wts_pair_ty, name="p2_bn1_wts", depth=1)
    bn1_wt1_f, bn1_wt2_f = bn1_wts_fifo.cons().split(
        offsets=[0, bn_wt_slot],
        obj_types=[bn_wt_ty, bn_wt_ty],
        names=["p2_bn1_wt1", "p2_bn1_wt2"],
        depths=[1, 1],
        placement=Tile(1, 1),
    )
    bn1_inter = ObjectFifo(half_row_ty, name="p2_bn1_inter", depth=bn_depth)
    bn1_cv2_out = ObjectFifo(half_row_ty, name="p2_bn1_cv2_out", depth=2)
    bn1_out_fifo = ObjectFifo(half_row_ty, name="p2_bn1_out", depth=2)

    # --- Phase D FIFOs: cv2 ---
    cv2_in_fifo = ObjectFifo(cv2_in_row_ty, name="p2_cv2_in", depth=2)
    cv2_wt_fifo = ObjectFifo(cv2_wt_ty, name="p2_cv2_wt", depth=1)
    cv2_out_fifo = ObjectFifo(cv2_out_row_ty, name="p2_cv2_out", depth=2)

    # --- Phase E FIFOs: L5 (single core, OC streaming) ---
    if l5_mode:
        l5_in_fifo = ObjectFifo(l5_input_row_ty, name="l5_in", depth=l5_input_depth)
        l5_wt_fifo = ObjectFifo(l5_wt_ty, name="l5_wt", depth=1)
        l5_out_fifo = ObjectFifo(l5_output_row_ty, name="l5_out", depth=2)

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

    l5_worker = None
    if l5_mode:

        def core_fn_l5(of_in, of_wt, of_out, kernel_fn):
            x_dim = l5_width
            ci = l5_ic
            co = l5_oc_chunk
            oh = l5_out_h
            s1 = l5_shift1
            s2 = l5_shift2

            for _ in range_(l5_n_oc_groups):
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

                of_in.release(1)
                of_wt.release(1)

        l5_worker = Worker(
            core_fn_l5,
            [l5_in_fifo.cons(), l5_wt_fifo.cons(), l5_out_fifo.prod(), l5_kernel],
            placement=Tile(2, 2),
        )

    # --- Runtime ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        all_workers = [
            worker_cv1,
            worker_bn0cv1,
            worker_bn0cv2,
            worker_bn0add,
            worker_bn1cv1,
            worker_bn1cv2,
            worker_bn1add,
            worker_cv2,
        ]
        if l5_worker is not None:
            all_workers.append(l5_worker)
        rt.start(*all_workers)

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

        # Drain cv1 output with strided write into concat rows
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

        # === Phase B: bn0 ===
        tg_b = rt.task_group()

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

        # === Phase C: bn1 ===
        tg_c = rt.task_group()

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

        out_dims = _factorize_tensor(l4_output_size)
        rt.drain(
            cv2_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=l4_scratch_offset,
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

        # === Phase E: L5 k3s2 (single core, OC streaming) ===
        if l5_mode:
            tg_e = rt.task_group()

            # Input TAP: re-stream L4 output n_oc_groups times via stride-0
            l5_in_d2, l5_in_d1, l5_in_d0 = _factorize_3d(l5_total_input)
            rt.fill(
                l5_in_fifo.prod(),
                O,
                TensorAccessPattern(
                    (1, output_buf_size),
                    offset=l4_scratch_offset,
                    sizes=[l5_n_oc_groups, l5_in_d2, l5_in_d1, l5_in_d0],
                    strides=[0, l5_in_d1 * l5_in_d0, l5_in_d0, 1],
                ),
                task_group=tg_e,
            )

            # Weight TAP: contiguous read of all OC group weight chunks
            l5_wt_d3, l5_wt_d2, l5_wt_d1, l5_wt_d0 = _factorize_tensor(l5_total_wt)
            rt.fill(
                l5_wt_fifo.prod(),
                W,
                TensorAccessPattern(
                    (1, total_wt),
                    offset=l4_total_wt,
                    sizes=[l5_wt_d3, l5_wt_d2, l5_wt_d1, l5_wt_d0],
                    strides=[
                        l5_wt_d2 * l5_wt_d1 * l5_wt_d0,
                        l5_wt_d1 * l5_wt_d0,
                        l5_wt_d0,
                        1,
                    ],
                ),
                task_group=tg_e,
            )

            # Output TAP: strided drain to interleave OC chunks
            pe_d0 = min(l5_output_elem, 1023)
            while pe_d0 % 4 != 0:
                pe_d0 -= 1
            while pe_d0 >= 4:
                if l5_output_elem % pe_d0 == 0:
                    break
                pe_d0 -= 4
            pe_d1 = l5_output_elem // pe_d0

            rt.drain(
                l5_out_fifo.cons(),
                O,
                TensorAccessPattern(
                    (1, output_buf_size),
                    offset=0,
                    sizes=[l5_n_oc_groups, l5_out_h, pe_d1, pe_d0],
                    strides=[
                        l5_oc_chunk * l5_out_w,
                        l5_output_row_total,
                        pe_d0,
                        1,
                    ],
                ),
                wait=True,
                task_group=tg_e,
            )

            rt.finish_task_group(tg_e)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # l4_l5_combined


# ---------------------------------------------------------------------------
# Step 13: Combined L6(C2f) + L7(k3s2, single-core OC streaming) in one PDI
#
# Phases A-D: C2f L6 (identical to my_dataflow_c2f_l6)
# Phase E: L7 k3s2 128->256, single core with OC streaming
#          Re-streams L6 output for each OC group via stride-0 DMA
#          Uses proven OC streaming pattern from my_dataflow_fused_oc_streaming
#
# Tile placement (9 cores, 3 columns):
#   Col 0: L6.cv1(0,2), L6.bn0.cv1(0,3), L6.bn0.cv2(0,4), L6.bn0_add(0,5)
#   Col 1: L6.bn1.cv1(1,2), L6.bn1.cv2(1,3), L6.bn1_add(1,4), L6.cv2(1,5)
#   Col 2: L7(2,2) [single core, OC streaming]
#
# When l7_oc=0, only phases A-D run (L6-only mode for Step 1 testing).
# ---------------------------------------------------------------------------


def my_dataflow_l6_l7_combined(
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
    # L7 params (optional, set l7_oc=0 for L6-only mode)
    l7_oc=0,
    l7_shift1=0,
    l7_shift2=0,
):
    """Combined L6(C2f) + L7(k3s2) in one PDI.

    When l7_oc=0: L6-only mode (phases A-D, 8 cores, 2 columns).
    When l7_oc>0: L6+L7 mode (phases A-E, 9 cores, 3 columns).

    Phase A: cv1(128->128, k1) -> drain to concat[0:128ch]
    Phase B: bn0 pipeline (half2 -> k3 -> k3 -> add -> concat[128:192ch])
    Phase C: bn1 pipeline (bn0_out -> k3 -> k3 -> add -> concat[192:256ch])
    Phase D: cv2(256->128, k1) -> L6 output
    Phase E: L7 k3s2 128->l7_oc, single-core OC streaming -> L7 output

    DDR output buffer layout:
      L6-only: [L6_output(128ch*H*W) | concat(256ch*H*W)]
      L6+L7:   [L7_output(l7_oc*H/2*W/2) | L6_scratch(128ch*H*W) | concat(256ch*H*W)]

    Args:
        dev: Device type string.
        height: Spatial height (40 for L6).
        width: Spatial width (40 for L6).
        in_channels: Input channels (128).
        cv1_scale..cv2_scale: C2f requantization shifts.
        l7_oc: L7 output channels (256), or 0 for L6-only.
        l7_shift1, l7_shift2: L7 fused SiLU params.
    """
    xfr_dtype = np.int8
    l7_mode = l7_oc > 0

    assert in_channels == 128
    cv1_oc = 128
    bn_ch = 64
    cv2_ic = 256
    cv2_oc = 128

    # Row sizes
    input_row = in_channels * width
    cv1_out_row = cv1_oc * width
    half_row = bn_ch * width
    cv2_in_row = cv2_ic * width
    cv2_out_row = cv2_oc * width

    # Weight sizes (non-fused, no bias for C2f)
    cv1_wt = cv1_oc * in_channels  # 16384
    bn_k3_wt = bn_ch * bn_ch * 9  # 36864
    cv2_wt = cv2_oc * cv2_ic  # 32768

    total_input = in_channels * height * width
    l6_output_size = cv2_oc * height * width
    total_concat = cv2_ic * height * width

    # --- L7 dimensions (single-core OC streaming) ---
    if l7_mode:
        l7_ic = cv2_oc  # 128
        l7_height = height  # 40
        l7_width = width  # 40
        l7_out_h = l7_height // 2  # 20
        l7_out_w = l7_width // 2  # 20
        l7_stride = 2

        # Compute OC streaming parameters
        l7_oc_chunk, l7_n_oc_groups, l7_input_depth = _compute_oc_streaming_params(
            l7_ic, l7_oc, l7_width, l7_stride
        )

        l7_input_row = l7_ic * l7_width
        l7_wt_chunk = l7_oc_chunk * l7_ic * 9 + l7_oc_chunk * 4
        l7_output_elem = l7_oc_chunk * l7_out_w
        l7_total_wt = l7_n_oc_groups * l7_wt_chunk

        l7_total_output = l7_oc * l7_out_h * l7_out_w
        l7_total_input = l7_ic * l7_height * l7_width
        l7_output_row_total = l7_oc * l7_out_w

    # --- L1 budget checks (L6 C2f) ---
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

    # --- DDR output buffer layout ---
    if l7_mode:
        # [L7_output | L6_scratch | concat]
        l6_scratch_offset = l7_total_output
        concat_offset = l7_total_output + l6_output_size
        output_buf_size = l7_total_output + l6_output_size + total_concat
    else:
        # [L6_output | concat]
        l6_scratch_offset = 0
        concat_offset = l6_output_size
        output_buf_size = l6_output_size + total_concat

    # Weight layout: [cv1 | bn0cv1 | bn0cv2 | bn1cv1 | bn1cv2 | cv2 | (l7 wt chunks)]
    bn_wt_slot = bn_k3_wt
    l6_total_wt = cv1_wt + 4 * bn_wt_slot + cv2_wt
    total_wt = l6_total_wt + (l7_total_wt if l7_mode else 0)

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

    if l7_mode:
        l7_input_row_ty = np.ndarray[(l7_input_row,), np.dtype[xfr_dtype]]
        l7_output_row_ty = np.ndarray[(l7_output_elem,), np.dtype[xfr_dtype]]
        l7_wt_ty = np.ndarray[(l7_wt_chunk,), np.dtype[xfr_dtype]]

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

    if l7_mode:
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

    # --- Phase A FIFOs: cv1 ---
    in_fifo = ObjectFifo(input_row_ty, name="p3_c2f_in", depth=2)
    cv1_wt_fifo = ObjectFifo(cv1_wt_ty, name="p3_cv1_wt", depth=1)
    cv1_out_fifo = ObjectFifo(cv1_out_row_ty, name="p3_cv1_out", depth=2)

    # --- Phase B FIFOs: bn0 pipeline ---
    bn0_in_fifo = ObjectFifo(half_row_ty, name="p3_bn0_in", depth=bn_depth)
    bn0_skip_fifo = ObjectFifo(half_row_ty, name="p3_bn0_skip", depth=2)
    bn0_wts_fifo = ObjectFifo(bn_wts_pair_ty, name="p3_bn0_wts", depth=1)
    bn0_wt1_f, bn0_wt2_f = bn0_wts_fifo.cons().split(
        offsets=[0, bn_wt_slot],
        obj_types=[bn_wt_ty, bn_wt_ty],
        names=["p3_bn0_wt1", "p3_bn0_wt2"],
        depths=[1, 1],
        placement=Tile(0, 1),
    )
    bn0_inter = ObjectFifo(half_row_ty, name="p3_bn0_inter", depth=bn_depth)
    bn0_cv2_out = ObjectFifo(half_row_ty, name="p3_bn0_cv2_out", depth=2)
    bn0_out_fifo = ObjectFifo(half_row_ty, name="p3_bn0_out", depth=2)

    # --- Phase C FIFOs: bn1 pipeline ---
    bn1_in_fifo = ObjectFifo(half_row_ty, name="p3_bn1_in", depth=bn_depth)
    bn1_skip_fifo = ObjectFifo(half_row_ty, name="p3_bn1_skip", depth=2)
    bn1_wts_fifo = ObjectFifo(bn_wts_pair_ty, name="p3_bn1_wts", depth=1)
    bn1_wt1_f, bn1_wt2_f = bn1_wts_fifo.cons().split(
        offsets=[0, bn_wt_slot],
        obj_types=[bn_wt_ty, bn_wt_ty],
        names=["p3_bn1_wt1", "p3_bn1_wt2"],
        depths=[1, 1],
        placement=Tile(1, 1),
    )
    bn1_inter = ObjectFifo(half_row_ty, name="p3_bn1_inter", depth=bn_depth)
    bn1_cv2_out = ObjectFifo(half_row_ty, name="p3_bn1_cv2_out", depth=2)
    bn1_out_fifo = ObjectFifo(half_row_ty, name="p3_bn1_out", depth=2)

    # --- Phase D FIFOs: cv2 ---
    cv2_in_fifo = ObjectFifo(cv2_in_row_ty, name="p3_cv2_in", depth=2)
    cv2_wt_fifo = ObjectFifo(cv2_wt_ty, name="p3_cv2_wt", depth=1)
    cv2_out_fifo = ObjectFifo(cv2_out_row_ty, name="p3_cv2_out", depth=2)

    # --- Phase E FIFOs: L7 (single core, OC streaming) ---
    if l7_mode:
        l7_in_fifo = ObjectFifo(l7_input_row_ty, name="l7_in", depth=l7_input_depth)
        l7_wt_fifo = ObjectFifo(l7_wt_ty, name="l7_wt", depth=1)
        l7_out_fifo = ObjectFifo(l7_output_row_ty, name="l7_out", depth=2)

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

    l7_worker = None
    if l7_mode:

        def core_fn_l7(of_in, of_wt, of_out, kernel_fn):
            x_dim = l7_width
            ci = l7_ic
            co = l7_oc_chunk
            oh = l7_out_h
            s1 = l7_shift1
            s2 = l7_shift2

            for _ in range_(l7_n_oc_groups):
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

                of_in.release(1)
                of_wt.release(1)

        l7_worker = Worker(
            core_fn_l7,
            [l7_in_fifo.cons(), l7_wt_fifo.cons(), l7_out_fifo.prod(), l7_kernel],
            placement=Tile(2, 2),
        )

    # --- Runtime ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        all_workers = [
            worker_cv1,
            worker_bn0cv1,
            worker_bn0cv2,
            worker_bn0add,
            worker_bn1cv1,
            worker_bn1cv2,
            worker_bn1add,
            worker_cv2,
        ]
        if l7_worker is not None:
            all_workers.append(l7_worker)
        rt.start(*all_workers)

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

        # Drain cv1 output with strided write into concat rows
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

        # === Phase B: bn0 ===
        tg_b = rt.task_group()

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

        # === Phase C: bn1 ===
        tg_c = rt.task_group()

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

        out_dims = _factorize_tensor(l6_output_size)
        rt.drain(
            cv2_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=l6_scratch_offset,
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

        # === Phase E: L7 k3s2 (single core, OC streaming) ===
        if l7_mode:
            tg_e = rt.task_group()

            # Input TAP: re-stream L6 output n_oc_groups times via stride-0
            l7_in_d2, l7_in_d1, l7_in_d0 = _factorize_3d(l7_total_input)
            rt.fill(
                l7_in_fifo.prod(),
                O,
                TensorAccessPattern(
                    (1, output_buf_size),
                    offset=l6_scratch_offset,
                    sizes=[l7_n_oc_groups, l7_in_d2, l7_in_d1, l7_in_d0],
                    strides=[0, l7_in_d1 * l7_in_d0, l7_in_d0, 1],
                ),
                task_group=tg_e,
            )

            # Weight TAP: contiguous read of all OC group weight chunks
            l7_wt_d3, l7_wt_d2, l7_wt_d1, l7_wt_d0 = _factorize_tensor(l7_total_wt)
            rt.fill(
                l7_wt_fifo.prod(),
                W,
                TensorAccessPattern(
                    (1, total_wt),
                    offset=l6_total_wt,
                    sizes=[l7_wt_d3, l7_wt_d2, l7_wt_d1, l7_wt_d0],
                    strides=[
                        l7_wt_d2 * l7_wt_d1 * l7_wt_d0,
                        l7_wt_d1 * l7_wt_d0,
                        l7_wt_d0,
                        1,
                    ],
                ),
                task_group=tg_e,
            )

            # Output TAP: strided drain to interleave OC chunks
            pe_d0 = min(l7_output_elem, 1023)
            while pe_d0 % 4 != 0:
                pe_d0 -= 1
            while pe_d0 >= 4:
                if l7_output_elem % pe_d0 == 0:
                    break
                pe_d0 -= 4
            pe_d1 = l7_output_elem // pe_d0

            rt.drain(
                l7_out_fifo.cons(),
                O,
                TensorAccessPattern(
                    (1, output_buf_size),
                    offset=0,
                    sizes=[l7_n_oc_groups, l7_out_h, pe_d1, pe_d0],
                    strides=[
                        l7_oc_chunk * l7_out_w,
                        l7_output_row_total,
                        pe_d0,
                        1,
                    ],
                ),
                wait=True,
                task_group=tg_e,
            )

            rt.finish_task_group(tg_e)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # l6_l7_combined


# ---------------------------------------------------------------------------
# Step 14: L8 C2f (n=1 bottleneck, 256ch, OC streaming on all layers)
#
# All weight tensors exceed L1 (cv1=64KB, bn=144KB, cv2=96KB), so every
# layer uses single-core OC streaming.  Five sequential phases:
#   A: cv1 k1 256->256 (oc_chunk=128, 2 groups)
#   B: bn0.cv1 k3s1 128->128 (oc_chunk=32, 4 groups)
#   C: bn0.cv2 k3s1 128->128 (oc_chunk=32, 4 groups)
#   D: bn0_add elementwise 128ch
#   E: cv2 k1 384->256 (oc_chunk=64, 4 groups)
#
# Each worker on a separate column to avoid shim DMA contention:
#   Col 0: cv1(0,2)
#   Col 1: bn0.cv1(1,2)
#   Col 2: bn0.cv2(2,2)
#   Col 3: bn0_add(3,2)
#   Col 4: cv2(4,2)
#
# DDR output: [final(256*H*W) | concat(384*H*W) | scratchA(128*H*W) | scratchB(128*H*W)]
# ---------------------------------------------------------------------------


def my_dataflow_l8_c2f(
    dev,
    height,
    width,
    in_channels,
    cv1_scale,
    bn0_cv1_scale,
    bn0_cv2_scale,
    cv2_scale,
):
    """L8 C2f block: n=1 bottleneck, OC streaming on all layers.

    Five sequential phases, each with single-core OC streaming:
      Phase A: cv1(256->256, k1, OC streaming)
      Phase B: bn0.cv1(128->128, k3s1, OC streaming)
      Phase C: bn0.cv2(128->128, k3s1, OC streaming)
      Phase D: bn0_add(elementwise 128ch)
      Phase E: cv2(384->256, k1, OC streaming)

    DDR output buffer: [final | concat | scratchA | scratchB]

    Args:
        dev: Device type string.
        height: Spatial height (20 for L8).
        width: Spatial width (20 for L8).
        in_channels: Input channels (256).
        cv1_scale, bn0_cv1_scale, bn0_cv2_scale, cv2_scale: requant shifts.
    """
    xfr_dtype = np.int8

    assert in_channels == 256
    cv1_oc = 256
    half_ch = 128
    bn_ch = 128
    concat_ch = 384  # half1(128) + half2(128) + bn0_out(128)
    cv2_oc = 256

    # OC streaming parameters
    cv1_oc_chunk = 128
    cv1_n_groups = cv1_oc // cv1_oc_chunk  # 2
    bn_oc_chunk = 32
    bn_n_groups = bn_ch // bn_oc_chunk  # 4
    cv2_oc_chunk = 64
    cv2_n_groups = cv2_oc // cv2_oc_chunk  # 4

    # Row sizes
    input_row = in_channels * width
    cv1_out_elem = cv1_oc_chunk * width
    half_row = half_ch * width
    bn_out_elem = bn_oc_chunk * width
    concat_row = concat_ch * width
    cv2_out_elem = cv2_oc_chunk * width
    output_row = cv2_oc * width
    bn_full_row = bn_ch * width

    # Weight chunk sizes (no bias for non-fused C2f kernels)
    cv1_wt_chunk = cv1_oc_chunk * in_channels
    bn_wt_chunk = bn_oc_chunk * bn_ch * 9
    cv2_wt_chunk = cv2_oc_chunk * concat_ch

    # Total weight sizes
    cv1_total_wt = cv1_n_groups * cv1_wt_chunk
    bn_total_wt_each = bn_n_groups * bn_wt_chunk
    cv2_total_wt = cv2_n_groups * cv2_wt_chunk
    total_wt = cv1_total_wt + 2 * bn_total_wt_each + cv2_total_wt

    # Totals
    total_input = in_channels * height * width
    final_size = cv2_oc * height * width
    concat_size = concat_ch * height * width
    scratch_size = bn_ch * height * width

    # --- L1 budget checks ---
    bn_depth = 4
    cv1_l1 = 1040 + 2 * input_row + cv1_wt_chunk + 2 * cv1_out_elem
    assert cv1_l1 <= 65536, f"cv1 L1: {cv1_l1}B"

    bn_l1 = 1040 + (bn_depth + 1) * half_row + bn_wt_chunk + 2 * bn_out_elem
    assert bn_l1 <= 65536, f"bn L1: {bn_l1}B"

    add_l1 = 1040 + 2 * half_row + 2 * half_row + 2 * half_row
    assert add_l1 <= 65536, f"add L1: {add_l1}B"

    cv2_l1 = 1040 + 2 * concat_row + cv2_wt_chunk + 2 * cv2_out_elem
    assert cv2_l1 <= 65536, f"cv2 L1: {cv2_l1}B"

    dev_ty = NPU2()

    # DDR output buffer: [final | concat | scratchA | scratchB]
    concat_offset = final_size
    scratchA_offset = final_size + concat_size
    scratchB_offset = final_size + concat_size + scratch_size
    output_buf_size = final_size + concat_size + 2 * scratch_size

    # Weight layout: [cv1_chunks | bn0cv1_chunks | bn0cv2_chunks | cv2_chunks]
    bn0cv1_wt_offset = cv1_total_wt
    bn0cv2_wt_offset = cv1_total_wt + bn_total_wt_each
    cv2_wt_offset = cv1_total_wt + 2 * bn_total_wt_each

    # --- Types ---
    input_row_ty = np.ndarray[(input_row,), np.dtype[xfr_dtype]]
    cv1_wt_ty = np.ndarray[(cv1_wt_chunk,), np.dtype[xfr_dtype]]
    cv1_out_ty = np.ndarray[(cv1_out_elem,), np.dtype[xfr_dtype]]

    half_row_ty = np.ndarray[(half_row,), np.dtype[xfr_dtype]]
    bn_wt_ty = np.ndarray[(bn_wt_chunk,), np.dtype[xfr_dtype]]
    bn_out_ty = np.ndarray[(bn_out_elem,), np.dtype[xfr_dtype]]

    concat_row_ty = np.ndarray[(concat_row,), np.dtype[xfr_dtype]]
    cv2_wt_ty = np.ndarray[(cv2_wt_chunk,), np.dtype[xfr_dtype]]
    cv2_out_ty = np.ndarray[(cv2_out_elem,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(output_buf_size,), np.dtype[xfr_dtype]]

    # --- Kernels ---
    cv1_kernel = Kernel(
        "conv2dk1_i8",
        "conv2dk1_i8.o",
        [input_row_ty, cv1_wt_ty, cv1_out_ty, np.int32, np.int32, np.int32, np.int32],
    )

    bn_cv1_kernel = Kernel(
        "conv2dk3_i8_bn",
        "conv2dk3_i8_bn.o",
        [
            half_row_ty,
            half_row_ty,
            half_row_ty,
            bn_wt_ty,
            bn_out_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    bn_cv2_kernel = Kernel(
        "conv2dk3_i8_bn_cv2",
        "conv2dk3_i8_bn_cv2.o",
        [
            half_row_ty,
            half_row_ty,
            half_row_ty,
            bn_wt_ty,
            bn_out_ty,
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

    cv2_kernel = Kernel(
        "conv2dk1_i8_cv2",
        "conv2dk1_i8_cv2.o",
        [concat_row_ty, cv2_wt_ty, cv2_out_ty, np.int32, np.int32, np.int32, np.int32],
    )

    # --- ObjectFIFOs ---
    # Phase A: cv1
    cv1_in = ObjectFifo(input_row_ty, name="l8_cv1_in", depth=2)
    cv1_wt = ObjectFifo(cv1_wt_ty, name="l8_cv1_wt", depth=1)
    cv1_out = ObjectFifo(cv1_out_ty, name="l8_cv1_out", depth=2)

    # Phase B: bn0.cv1
    bn0cv1_in = ObjectFifo(half_row_ty, name="l8_bn0cv1_in", depth=bn_depth)
    bn0cv1_wt = ObjectFifo(bn_wt_ty, name="l8_bn0cv1_wt", depth=1)
    bn0cv1_out = ObjectFifo(bn_out_ty, name="l8_bn0cv1_out", depth=2)

    # Phase C: bn0.cv2
    bn0cv2_in = ObjectFifo(half_row_ty, name="l8_bn0cv2_in", depth=bn_depth)
    bn0cv2_wt = ObjectFifo(bn_wt_ty, name="l8_bn0cv2_wt", depth=1)
    bn0cv2_out = ObjectFifo(bn_out_ty, name="l8_bn0cv2_out", depth=2)

    # Phase D: bn0_add
    add_in_a = ObjectFifo(half_row_ty, name="l8_add_a", depth=2)
    add_in_b = ObjectFifo(half_row_ty, name="l8_add_b", depth=2)
    add_out = ObjectFifo(half_row_ty, name="l8_add_out", depth=2)

    # Phase E: cv2
    cv2_in = ObjectFifo(concat_row_ty, name="l8_cv2_in", depth=2)
    cv2_wt_fifo = ObjectFifo(cv2_wt_ty, name="l8_cv2_wt", depth=1)
    cv2_out_fifo = ObjectFifo(cv2_out_ty, name="l8_cv2_out", depth=2)

    # --- Core functions ---

    # k1 OC streaming: outer loop over OC groups
    def core_fn_cv1_ocs(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = in_channels
        co = cv1_oc_chunk
        sc = cv1_scale
        for _ in range_(cv1_n_groups):
            elem_wt = of_wt.acquire(1)
            for _ in range_(height):
                ei = of_in.acquire(1)
                eo = of_out.acquire(1)
                kernel_fn(ei, elem_wt, eo, w, ci, co, sc)
                of_in.release(1)
                of_out.release(1)
            of_wt.release(1)

    # k3s1 OC streaming (sliding window)
    def _make_k3s1_ocs_fn(h_val, ci_val, co_val, sc_val, n_groups_val):
        def core_fn(of_in, of_wt, of_out, kernel_fn):
            w = width
            ci = ci_val
            co = co_val
            sc = sc_val
            h = h_val
            for _ in range_(n_groups_val):
                elem_wt = of_wt.acquire(1)

                # Top row (check=0)
                elems = of_in.acquire(2)
                eo = of_out.acquire(1)
                kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo, w, ci, co, 0, sc)
                of_out.release(1)

                # Middle rows (check=1)
                for _ in range_(h - 2):
                    elems = of_in.acquire(3)
                    eo = of_out.acquire(1)
                    kernel_fn(
                        elems[0], elems[1], elems[2], elem_wt, eo, w, ci, co, 1, sc
                    )
                    of_in.release(1)
                    of_out.release(1)

                # Bottom row (check=2)
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

    def core_fn_cv2_ocs(of_in, of_wt, of_out, kernel_fn):
        w = width
        ci = concat_ch
        co = cv2_oc_chunk
        sc = cv2_scale
        for _ in range_(cv2_n_groups):
            elem_wt = of_wt.acquire(1)
            for _ in range_(height):
                ei = of_in.acquire(1)
                eo = of_out.acquire(1)
                kernel_fn(ei, elem_wt, eo, w, ci, co, sc)
                of_in.release(1)
                of_out.release(1)
            of_wt.release(1)

    # --- Workers (each on separate column for DMA channel budget) ---
    worker_cv1 = Worker(
        core_fn_cv1_ocs,
        [cv1_in.cons(), cv1_wt.cons(), cv1_out.prod(), cv1_kernel],
        placement=Tile(0, 2),
    )
    worker_bn0cv1 = Worker(
        _make_k3s1_ocs_fn(height, bn_ch, bn_oc_chunk, bn0_cv1_scale, bn_n_groups),
        [bn0cv1_in.cons(bn_depth), bn0cv1_wt.cons(), bn0cv1_out.prod(), bn_cv1_kernel],
        placement=Tile(1, 2),
    )
    worker_bn0cv2 = Worker(
        _make_k3s1_ocs_fn(height, bn_ch, bn_oc_chunk, bn0_cv2_scale, bn_n_groups),
        [bn0cv2_in.cons(bn_depth), bn0cv2_wt.cons(), bn0cv2_out.prod(), bn_cv2_kernel],
        placement=Tile(2, 2),
    )
    worker_add = Worker(
        core_fn_add,
        [add_in_a.cons(), add_in_b.cons(), add_out.prod(), add_kernel],
        placement=Tile(3, 2),
    )
    worker_cv2 = Worker(
        core_fn_cv2_ocs,
        [cv2_in.cons(), cv2_wt_fifo.cons(), cv2_out_fifo.prod(), cv2_kernel],
        placement=Tile(4, 2),
    )

    # --- Runtime ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker_cv1, worker_bn0cv1, worker_bn0cv2, worker_add, worker_cv2)

        # Helper for BD dim factorization of strided OC outputs
        def _oc_out_dims(elem_size):
            d0 = min(elem_size, 1023)
            while d0 % 4 != 0:
                d0 -= 1
            while d0 >= 4:
                if elem_size % d0 == 0:
                    break
                d0 -= 4
            return elem_size // d0, d0

        # === Phase A: cv1 k1 OC streaming ===
        tg_a = rt.task_group()

        # Fill input (re-stream for each OC group, stride-0)
        in_d2, in_d1, in_d0 = _factorize_3d(total_input)
        rt.fill(
            cv1_in.prod(),
            I,
            TensorAccessPattern(
                (1, total_input),
                offset=0,
                sizes=[cv1_n_groups, in_d2, in_d1, in_d0],
                strides=[0, in_d1 * in_d0, in_d0, 1],
            ),
            task_group=tg_a,
        )

        # Fill cv1 weights (contiguous)
        cv1w_d3, cv1w_d2, cv1w_d1, cv1w_d0 = _factorize_tensor(cv1_total_wt)
        rt.fill(
            cv1_wt.prod(),
            W,
            TensorAccessPattern(
                (1, total_wt),
                offset=0,
                sizes=[cv1w_d3, cv1w_d2, cv1w_d1, cv1w_d0],
                strides=[cv1w_d2 * cv1w_d1 * cv1w_d0, cv1w_d1 * cv1w_d0, cv1w_d0, 1],
            ),
            task_group=tg_a,
        )

        # Drain cv1 output (scatter OC chunks into 384ch concat rows)
        pe_d1, pe_d0 = _oc_out_dims(cv1_out_elem)
        rt.drain(
            cv1_out.cons(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset,
                sizes=[cv1_n_groups, height, pe_d1, pe_d0],
                strides=[cv1_oc_chunk * width, concat_row, pe_d0, 1],
            ),
            wait=True,
            task_group=tg_a,
        )
        rt.finish_task_group(tg_a)

        # === Phase B: bn0.cv1 k3s1 OC streaming ===
        tg_b = rt.task_group()

        # Fill half2 from concat[128:256ch] (strided, re-stream)
        hr_d0 = min(half_row, 1023)
        while hr_d0 % 4 != 0:
            hr_d0 -= 1
        while hr_d0 >= 4:
            if half_row % hr_d0 == 0:
                break
            hr_d0 -= 4
        hr_d1 = half_row // hr_d0

        rt.fill(
            bn0cv1_in.prod(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset + half_ch * width,
                sizes=[bn_n_groups, height, hr_d1, hr_d0],
                strides=[0, concat_row, hr_d0, 1],
            ),
            task_group=tg_b,
        )

        # Fill bn0cv1 weights (contiguous)
        bnw_d3, bnw_d2, bnw_d1, bnw_d0 = _factorize_tensor(bn_total_wt_each)
        rt.fill(
            bn0cv1_wt.prod(),
            W,
            TensorAccessPattern(
                (1, total_wt),
                offset=bn0cv1_wt_offset,
                sizes=[bnw_d3, bnw_d2, bnw_d1, bnw_d0],
                strides=[bnw_d2 * bnw_d1 * bnw_d0, bnw_d1 * bnw_d0, bnw_d0, 1],
            ),
            task_group=tg_b,
        )

        # Drain bn0cv1 output (scatter to scratchA, 128ch rows)
        bpe_d1, bpe_d0 = _oc_out_dims(bn_out_elem)
        rt.drain(
            bn0cv1_out.cons(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=scratchA_offset,
                sizes=[bn_n_groups, height, bpe_d1, bpe_d0],
                strides=[bn_oc_chunk * width, bn_full_row, bpe_d0, 1],
            ),
            wait=True,
            task_group=tg_b,
        )
        rt.finish_task_group(tg_b)

        # === Phase C: bn0.cv2 k3s1 OC streaming ===
        tg_c = rt.task_group()

        # Fill from scratchA (re-stream)
        sa_d2, sa_d1, sa_d0 = _factorize_3d(scratch_size)
        rt.fill(
            bn0cv2_in.prod(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=scratchA_offset,
                sizes=[bn_n_groups, sa_d2, sa_d1, sa_d0],
                strides=[0, sa_d1 * sa_d0, sa_d0, 1],
            ),
            task_group=tg_c,
        )

        # Fill bn0cv2 weights
        rt.fill(
            bn0cv2_wt.prod(),
            W,
            TensorAccessPattern(
                (1, total_wt),
                offset=bn0cv2_wt_offset,
                sizes=[bnw_d3, bnw_d2, bnw_d1, bnw_d0],
                strides=[bnw_d2 * bnw_d1 * bnw_d0, bnw_d1 * bnw_d0, bnw_d0, 1],
            ),
            task_group=tg_c,
        )

        # Drain to scratchB
        rt.drain(
            bn0cv2_out.cons(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=scratchB_offset,
                sizes=[bn_n_groups, height, bpe_d1, bpe_d0],
                strides=[bn_oc_chunk * width, bn_full_row, bpe_d0, 1],
            ),
            wait=True,
            task_group=tg_c,
        )
        rt.finish_task_group(tg_c)

        # === Phase D: bn0_add (scratchB + half2_skip -> concat[256:384ch]) ===
        tg_d = rt.task_group()

        # Fill bn0.cv2 output from scratchB (linear)
        sb_d3, sb_d2, sb_d1, sb_d0 = _factorize_tensor(scratch_size)
        rt.fill(
            add_in_a.prod(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=scratchB_offset,
                sizes=[sb_d3, sb_d2, sb_d1, sb_d0],
                strides=[sb_d2 * sb_d1 * sb_d0, sb_d1 * sb_d0, sb_d0, 1],
            ),
            task_group=tg_d,
        )

        # Fill half2 skip from concat[128:256ch] (strided)
        rt.fill(
            add_in_b.prod(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset + half_ch * width,
                sizes=[1, height, hr_d1, hr_d0],
                strides=[0, concat_row, hr_d0, 1],
            ),
            task_group=tg_d,
        )

        # Drain bn0_out to concat[256:384ch] (strided)
        rt.drain(
            add_out.cons(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset + 2 * half_ch * width,
                sizes=[1, height, hr_d1, hr_d0],
                strides=[0, concat_row, hr_d0, 1],
            ),
            wait=True,
            task_group=tg_d,
        )
        rt.finish_task_group(tg_d)

        # === Phase E: cv2 k1 OC streaming ===
        tg_e = rt.task_group()

        # Fill concat (re-stream for each OC group)
        cc_d2, cc_d1, cc_d0 = _factorize_3d(concat_size)
        rt.fill(
            cv2_in.prod(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset,
                sizes=[cv2_n_groups, cc_d2, cc_d1, cc_d0],
                strides=[0, cc_d1 * cc_d0, cc_d0, 1],
            ),
            task_group=tg_e,
        )

        # Fill cv2 weights
        cv2w_d3, cv2w_d2, cv2w_d1, cv2w_d0 = _factorize_tensor(cv2_total_wt)
        rt.fill(
            cv2_wt_fifo.prod(),
            W,
            TensorAccessPattern(
                (1, total_wt),
                offset=cv2_wt_offset,
                sizes=[cv2w_d3, cv2w_d2, cv2w_d1, cv2w_d0],
                strides=[cv2w_d2 * cv2w_d1 * cv2w_d0, cv2w_d1 * cv2w_d0, cv2w_d0, 1],
            ),
            task_group=tg_e,
        )

        # Drain cv2 output (scatter OC chunks into final)
        cpe_d1, cpe_d0 = _oc_out_dims(cv2_out_elem)
        rt.drain(
            cv2_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=0,
                sizes=[cv2_n_groups, height, cpe_d1, cpe_d0],
                strides=[cv2_oc_chunk * width, output_row, cpe_d0, 1],
            ),
            wait=True,
            task_group=tg_e,
        )
        rt.finish_task_group(tg_e)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # l8_c2f


# ---------------------------------------------------------------------------
# Step 15: Combined P1(L0-L3) + P2(L4+L5) in one PDI
#
# Merges two standalone designs into a single 17-core PDI:
#   P1 (8 cores, cols 0-1): L0->L1->C2f L2->L3 (backbone_phase1)
#   P2 (9 cores, cols 2-3-4): C2f L4 + L5 OC streaming (l4_l5_combined)
#
# Data flows through DDR scratch areas in the output buffer:
#   P1 TG3 drains L3 output -> P2 reads as input
#   P2 TG_E drains L5 output -> offset 0 (final result)
#
# Skip merge optimization: bn0_in + bn0_skip share one DDR-filled FIFO
# with doubled element size, split at MemTile. Same for bn1. This saves
# 2 fill channels (18->16), fitting within NPU2's 16 ShimDMA fill limit.
#
# 8 task groups in one rt.sequence, all 17 workers started at the top.
# ---------------------------------------------------------------------------


def my_dataflow_p1_p2_combined(
    dev,
    # P1 (backbone_phase1) params
    l0_height,
    l0_width,
    l0_ic,
    l0_oc,
    l0_shift1,
    l0_shift2,
    l1_oc,
    l1_shift1,
    l1_shift2,
    cv1_shift1,
    cv1_shift2,
    bn_cv1_shift1,
    bn_cv1_shift2,
    bn_cv2_shift1,
    bn_cv2_shift2,
    cv2_shift1,
    cv2_shift2,
    l3_oc,
    l3_shift1,
    l3_shift2,
    # P2 (l4_l5_combined, always l5_mode=True) params
    l4_cv1_scale,
    l4_bn0_cv1_scale,
    l4_bn0_cv2_scale,
    l4_bn1_cv1_scale,
    l4_bn1_cv2_scale,
    l4_cv2_scale,
    l5_oc,
    l5_shift1,
    l5_shift2,
):
    """Combined P1(L0-L3) + P2(L4+L5) in one PDI.

    17 cores across 5 columns:
      P1 cols 0-1: L0->L1->C2f L2->L3
      P2 cols 2-3-4: C2f L4 + L5 OC streaming

    8 task groups, sequential phases:
      TG1-TG3: P1 (L0->L1->scratch_A, C2f->scratch_B, L3->p2_input)
      TG_A-TG_E: P2 (cv1, bn0, bn1, cv2, L5->final output)

    DDR output buffer: [L5_final | P1_scratch_A | P1_scratch_B |
        P2_input | P2_concat | P2_L4_scratch]
    DDR weight buffer: [P1_weights | P2_weights]
    """
    xfr_dtype = np.int8

    # =====================================================================
    # P1 DIMENSIONS (from backbone_phase1)
    # =====================================================================
    p1_l0_out_h = l0_height // 2
    p1_l0_out_w = l0_width // 2

    p1_l1_ic = l0_oc
    p1_l1_height = p1_l0_out_h
    p1_l1_width = p1_l0_out_w
    p1_l1_out_h = p1_l1_height // 2
    p1_l1_out_w = p1_l1_width // 2

    p1_c2f_ic = l1_oc
    p1_c2f_height = p1_l1_out_h
    p1_c2f_width = p1_l1_out_w
    assert p1_c2f_ic == 32, f"C2f L2 requires 32ch input, got {p1_c2f_ic}"
    p1_cv1_oc = 32
    p1_bn_ch = 16
    p1_cv2_ic = 48  # 16 + 16 + 16
    p1_cv2_oc = 32

    p1_l3_ic = p1_cv2_oc
    p1_l3_height = p1_c2f_height
    p1_l3_width = p1_c2f_width
    p1_l3_out_h = p1_l3_height // 2
    p1_l3_out_w = p1_l3_width // 2

    # P1 row sizes
    p1_l0_input_row = l0_ic * l0_width
    p1_inter01_row = l0_oc * p1_l0_out_w
    p1_l1_out_row = l1_oc * p1_l1_out_w

    p1_c2f_input_row = p1_c2f_ic * p1_c2f_width
    p1_cv1_out_row = p1_cv1_oc * p1_c2f_width
    p1_half_row = p1_bn_ch * p1_c2f_width
    p1_cv2_in_row = p1_cv2_ic * p1_c2f_width
    p1_cv2_out_row = p1_cv2_oc * p1_c2f_width

    p1_l3_input_row = p1_l3_ic * p1_l3_width
    p1_l3_output_row = l3_oc * p1_l3_out_w

    # P1 weight sizes
    p1_l0_wt_size = l0_oc * l0_ic * 9 + l0_oc * 4
    p1_l1_wt_size = l1_oc * p1_l1_ic * 9 + l1_oc * 4
    p1_tg1_wt_slot = max(p1_l0_wt_size, p1_l1_wt_size)
    p1_tg1_total_wt = 2 * p1_tg1_wt_slot

    p1_cv1_wt_size = p1_cv1_oc * p1_c2f_ic + p1_cv1_oc * 4
    p1_bn_cv1_wt_size = p1_bn_ch * p1_bn_ch * 9 + p1_bn_ch * 4
    p1_bn_cv2_wt_size = p1_bn_ch * p1_bn_ch * 9 + p1_bn_ch * 4
    p1_cv2_wt_size = p1_cv2_oc * p1_cv2_ic + p1_cv2_oc * 4
    p1_c2f_wt_slot = max(
        p1_cv1_wt_size, p1_bn_cv1_wt_size, p1_bn_cv2_wt_size, p1_cv2_wt_size
    )
    p1_c2f_total_wt = 4 * p1_c2f_wt_slot

    p1_l3_wt_size = l3_oc * p1_l3_ic * 9 + l3_oc * 4

    p1_total_wt = p1_tg1_total_wt + p1_c2f_total_wt + p1_l3_wt_size

    # P1 tensor totals
    p1_total_input = l0_ic * l0_height * l0_width
    p1_scratch_a_size = l1_oc * p1_l1_out_h * p1_l1_out_w
    p1_scratch_b_size = p1_cv2_oc * p1_c2f_height * p1_c2f_width

    # =====================================================================
    # P2 DIMENSIONS (from l4_l5_combined, always l5_mode=True)
    # =====================================================================
    p2_in_channels = 64
    p2_height = p1_l3_out_h  # 80
    p2_width = p1_l3_out_w  # 80
    p2_cv1_oc = 64
    p2_bn_ch = 32
    p2_cv2_ic = 128
    p2_cv2_oc = 64

    p2_input_row = p2_in_channels * p2_width
    p2_cv1_out_row = p2_cv1_oc * p2_width
    p2_half_row = p2_bn_ch * p2_width
    p2_cv2_in_row = p2_cv2_ic * p2_width
    p2_cv2_out_row = p2_cv2_oc * p2_width

    p2_cv1_wt = p2_cv1_oc * p2_in_channels  # 4096
    p2_bn_k3_wt = p2_bn_ch * p2_bn_ch * 9  # 9216
    p2_cv2_wt = p2_cv2_oc * p2_cv2_ic  # 8192

    p2_total_input = p2_in_channels * p2_height * p2_width
    p2_l4_output_size = p2_cv2_oc * p2_height * p2_width
    p2_total_concat = p2_cv2_ic * p2_height * p2_width

    p2_bn_depth = 4
    # Broadcast depth: bn0/bn1 input FIFOs are consumed by BOTH the sliding
    # window conv (bn0cv1/bn1cv1, holds up to 3 at a time) AND the skip-add
    # (bn0add/bn1add, depth=1 but lags behind by ~height rows because
    # The skip data is forwarded through MemTile (edge-detect pattern).
    # The MemTile relay depth must cover the pipeline delay from bn0cv1
    # through bn0cv2 before bn0add can consume (~2*bn_depth rows).
    p2_bn_broadcast_depth = 2 * p2_bn_depth + 2  # 10

    # P2 L5 dimensions
    p2_l5_ic = p2_cv2_oc  # 64
    p2_l5_height = p2_height
    p2_l5_width = p2_width
    p2_l5_out_h = p2_l5_height // 2
    p2_l5_out_w = p2_l5_width // 2
    p2_l5_stride = 2

    p2_l5_oc_chunk, p2_l5_n_oc_groups, p2_l5_input_depth = _compute_oc_streaming_params(
        p2_l5_ic, l5_oc, p2_l5_width, p2_l5_stride
    )

    p2_l5_input_row = p2_l5_ic * p2_l5_width
    p2_l5_wt_chunk = p2_l5_oc_chunk * p2_l5_ic * 9 + p2_l5_oc_chunk * 4
    p2_l5_output_elem = p2_l5_oc_chunk * p2_l5_out_w
    p2_l5_total_wt = p2_l5_n_oc_groups * p2_l5_wt_chunk
    p2_l5_total_output = l5_oc * p2_l5_out_h * p2_l5_out_w
    p2_l5_total_input = p2_l5_ic * p2_l5_height * p2_l5_width
    p2_l5_output_row_total = l5_oc * p2_l5_out_w

    p2_bn_wt_slot = p2_bn_k3_wt
    p2_l4_total_wt = p2_cv1_wt + 4 * p2_bn_wt_slot + p2_cv2_wt
    p2_total_wt = p2_l4_total_wt + p2_l5_total_wt

    # =====================================================================
    # DDR BUFFER LAYOUTS
    # =====================================================================
    # Output buffer: [L5_final | P1_scratch_A | P1_scratch_B |
    #   P2_input | P2_concat | P2_L4_scratch]
    p1_scratch_a_offset = p2_l5_total_output
    p1_scratch_b_offset = p1_scratch_a_offset + p1_scratch_a_size
    p2_input_offset = p1_scratch_b_offset + p1_scratch_b_size
    p2_concat_offset = p2_input_offset + p2_total_input
    p2_l4_scratch_offset = p2_concat_offset + p2_total_concat
    total_output_buf = p2_l4_scratch_offset + p2_l4_output_size

    # Weight buffer: [P1_weights | P2_weights]
    p1_wt_offset = 0
    p2_wt_offset = p1_total_wt
    total_weights = p1_total_wt + p2_total_wt

    # =====================================================================
    # L1 BUDGET CHECKS
    # =====================================================================
    # P1 checks
    p1_spine_max_row = max(p1_l0_input_row, p1_inter01_row, p1_l1_out_row)
    p1_l0_input_depth = 4
    p1_l0_l1 = (
        1040
        + (p1_l0_input_depth + 1) * p1_l0_input_row
        + p1_tg1_wt_slot
        + 2 * p1_inter01_row
    )
    assert p1_l0_l1 <= 65536, f"P1 L0 L1 budget exceeded: {p1_l0_l1}B"

    p1_l1_input_depth = 4
    p1_l1_l1 = (
        1040
        + (p1_l1_input_depth + 1) * p1_inter01_row
        + p1_tg1_wt_slot
        + 2 * p1_l1_out_row
    )
    assert p1_l1_l1 <= 65536, f"P1 L1 L1 budget exceeded: {p1_l1_l1}B"

    p1_bn_depth = 4
    p1_cv1_l1 = 1040 + 2 * p1_c2f_input_row + p1_c2f_wt_slot + 2 * p1_cv1_out_row
    assert p1_cv1_l1 <= 65536, f"P1 cv1 L1 budget exceeded: {p1_cv1_l1}B"

    p1_bn1_l1 = (
        1040
        + (p1_bn_depth + 1) * p1_half_row
        + p1_c2f_wt_slot
        + p1_bn_depth * p1_half_row
        + 2 * p1_half_row
    )
    assert p1_bn1_l1 <= 65536, f"P1 bn0.cv1 L1 budget exceeded: {p1_bn1_l1}B"

    p1_bn2_l1 = (
        1040 + (p1_bn_depth + 1) * p1_half_row + p1_c2f_wt_slot + 2 * p1_half_row
    )
    assert p1_bn2_l1 <= 65536, f"P1 bn0.cv2 L1 budget exceeded: {p1_bn2_l1}B"

    p1_pass_l1 = 1040 + 2 * p1_half_row + 2 * p1_half_row
    assert p1_pass_l1 <= 65536, f"P1 passthrough L1 budget exceeded: {p1_pass_l1}B"

    p1_cv2_l1 = 1040 + 2 * p1_cv2_in_row + p1_c2f_wt_slot + 2 * p1_cv2_out_row
    assert p1_cv2_l1 <= 65536, f"P1 cv2 L1 budget exceeded: {p1_cv2_l1}B"

    p1_l3_input_depth = 4
    p1_l3_l1 = (
        1040
        + (p1_l3_input_depth + 1) * p1_l3_input_row
        + p1_l3_wt_size
        + 2 * p1_l3_output_row
    )
    assert p1_l3_l1 <= 65536, f"P1 L3 L1 budget exceeded: {p1_l3_l1}B"

    # P2 checks
    p2_core_cv1_l1 = 1040 + 2 * p2_input_row + p2_cv1_wt + 2 * p2_cv1_out_row
    assert p2_core_cv1_l1 <= 65536, f"P2 cv1 L1: {p2_core_cv1_l1}B"

    p2_core_bn_k3_l1 = (
        1040 + (p2_bn_depth + 1) * p2_half_row + p2_bn_k3_wt + 2 * p2_half_row
    )
    assert p2_core_bn_k3_l1 <= 65536, f"P2 bn k3 L1: {p2_core_bn_k3_l1}B"

    p2_core_add_l1 = 1040 + 2 * p2_half_row + 2 * p2_half_row + 2 * p2_half_row
    assert p2_core_add_l1 <= 65536, f"P2 add L1: {p2_core_add_l1}B"

    p2_core_cv2_l1 = 1040 + 2 * p2_cv2_in_row + p2_cv2_wt + 2 * p2_cv2_out_row
    assert p2_core_cv2_l1 <= 65536, f"P2 cv2 L1: {p2_core_cv2_l1}B"

    # MemTile budget for broadcast FIFOs (bn0 + bn1, each broadcast_depth buffers)
    p2_broadcast_memtile = 2 * (p2_bn_broadcast_depth + 1) * p2_half_row
    assert p2_broadcast_memtile <= 512 * 1024, (
        f"P2 broadcast MemTile: {p2_broadcast_memtile}B"
    )

    dev_ty = NPU2()

    # =====================================================================
    # TYPES
    # =====================================================================
    # --- P1 types ---
    p1_spine_row_ty = np.ndarray[(p1_spine_max_row,), np.dtype[xfr_dtype]]
    p1_tg1_wt_ty = np.ndarray[(p1_tg1_wt_slot,), np.dtype[xfr_dtype]]
    p1_tg1_wts_all_ty = np.ndarray[(p1_tg1_total_wt,), np.dtype[xfr_dtype]]

    p1_c2f_input_row_ty = np.ndarray[(p1_c2f_input_row,), np.dtype[xfr_dtype]]
    p1_cv1_out_row_ty = np.ndarray[(p1_cv1_out_row,), np.dtype[xfr_dtype]]
    p1_half_row_ty = np.ndarray[(p1_half_row,), np.dtype[xfr_dtype]]
    p1_cv2_in_row_ty = np.ndarray[(p1_cv2_in_row,), np.dtype[xfr_dtype]]
    p1_cv2_out_row_ty = np.ndarray[(p1_cv2_out_row,), np.dtype[xfr_dtype]]
    p1_c2f_wt_ty = np.ndarray[(p1_c2f_wt_slot,), np.dtype[xfr_dtype]]
    p1_c2f_wts_all_ty = np.ndarray[(p1_c2f_total_wt,), np.dtype[xfr_dtype]]

    p1_l3_input_row_ty = np.ndarray[(p1_l3_input_row,), np.dtype[xfr_dtype]]
    p1_l3_output_row_ty = np.ndarray[(p1_l3_output_row,), np.dtype[xfr_dtype]]
    p1_l3_wt_ty = np.ndarray[(p1_l3_wt_size,), np.dtype[xfr_dtype]]

    # --- P2 types ---
    p2_input_row_ty = np.ndarray[(p2_input_row,), np.dtype[xfr_dtype]]
    p2_cv1_out_row_ty = np.ndarray[(p2_cv1_out_row,), np.dtype[xfr_dtype]]
    p2_cv1_wt_ty = np.ndarray[(p2_cv1_wt,), np.dtype[xfr_dtype]]
    p2_half_row_ty = np.ndarray[(p2_half_row,), np.dtype[xfr_dtype]]
    p2_bn_wt_ty = np.ndarray[(p2_bn_wt_slot,), np.dtype[xfr_dtype]]
    p2_bn_wts_pair_ty = np.ndarray[(2 * p2_bn_wt_slot,), np.dtype[xfr_dtype]]
    p2_cv2_in_row_ty = np.ndarray[(p2_cv2_in_row,), np.dtype[xfr_dtype]]
    p2_cv2_out_row_ty = np.ndarray[(p2_cv2_out_row,), np.dtype[xfr_dtype]]
    p2_cv2_wt_ty = np.ndarray[(p2_cv2_wt,), np.dtype[xfr_dtype]]

    p2_l5_input_row_ty = np.ndarray[(p2_l5_input_row,), np.dtype[xfr_dtype]]
    p2_l5_output_row_ty = np.ndarray[(p2_l5_output_elem,), np.dtype[xfr_dtype]]
    p2_l5_wt_ty = np.ndarray[(p2_l5_wt_chunk,), np.dtype[xfr_dtype]]

    # --- DDR-level types ---
    input_l3_ty = np.ndarray[(p1_total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_weights,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_buf,), np.dtype[xfr_dtype]]

    # =====================================================================
    # KERNEL DECLARATIONS
    # =====================================================================
    # --- P1 kernels ---
    p1_k3s2_silu_kernel = Kernel(
        "conv2dk3s2_i8_silu",
        "conv2dk3_i8_silu.o",
        [
            p1_spine_row_ty,
            p1_spine_row_ty,
            p1_spine_row_ty,
            p1_tg1_wt_ty,
            p1_spine_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    p1_l3_k3s2_kernel = Kernel(
        "conv2dk3s2_i8_silu_l3",
        "conv2dk3_i8_silu_l3.o",
        [
            p1_l3_input_row_ty,
            p1_l3_input_row_ty,
            p1_l3_input_row_ty,
            p1_l3_wt_ty,
            p1_l3_output_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    p1_k1_silu_kernel = Kernel(
        "conv2dk1_i8_silu",
        "conv2dk1_i8_silu.o",
        [
            p1_c2f_input_row_ty,
            p1_c2f_wt_ty,
            p1_cv1_out_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    p1_k3_silu_bn_kernel = Kernel(
        "conv2dk3_i8_silu_bn",
        "conv2dk3_i8_silu_bn_fwd.o",
        [
            p1_half_row_ty,
            p1_half_row_ty,
            p1_half_row_ty,
            p1_c2f_wt_ty,
            p1_half_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    p1_passthrough_kernel = Kernel(
        "passthrough_i8",
        "passthrough_i8.o",
        [
            p1_half_row_ty,
            p1_half_row_ty,
            np.int32,
        ],
    )

    p1_passthrough_fwd_kernel = Kernel(
        "passthrough_i8_fwd",
        "conv2dk3_i8_silu_bn_fwd.o",
        [
            p1_half_row_ty,
            p1_half_row_ty,
            np.int32,
        ],
    )

    p1_k1_silu_cv2_kernel = Kernel(
        "conv2dk1_i8_silu_cv2",
        "conv2dk1_i8_silu_cv2.o",
        [
            p1_cv2_in_row_ty,
            p1_c2f_wt_ty,
            p1_cv2_out_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # --- P2 kernels ---
    p2_k1_kernel = Kernel(
        "conv2dk1_i8",
        "conv2dk1_i8.o",
        [
            p2_input_row_ty,
            p2_cv1_wt_ty,
            p2_cv1_out_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    p2_k3_bn_kernel = Kernel(
        "conv2dk3_i8_bn",
        "conv2dk3_i8_bn.o",
        [
            p2_half_row_ty,
            p2_half_row_ty,
            p2_half_row_ty,
            p2_bn_wt_ty,
            p2_half_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    p2_add_kernel = Kernel(
        "add_i8",
        "add_i8.o",
        [p2_half_row_ty, p2_half_row_ty, p2_half_row_ty, np.int32],
    )

    p2_k1_cv2_kernel = Kernel(
        "conv2dk1_i8_cv2",
        "conv2dk1_i8_cv2.o",
        [
            p2_cv2_in_row_ty,
            p2_cv2_wt_ty,
            p2_cv2_out_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    p2_l5_kernel = Kernel(
        "conv2dk3s2_i8_silu_l5",
        "conv2dk3_i8_silu_l5.o",
        [
            p2_l5_input_row_ty,
            p2_l5_input_row_ty,
            p2_l5_input_row_ty,
            p2_l5_wt_ty,
            p2_l5_output_row_ty,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
            np.int32,
        ],
    )

    # =====================================================================
    # P1 OBJECT FIFOs (cols 0-1, same placement as backbone_phase1)
    # =====================================================================
    # --- P1 TG1: L0->L1 ---
    p1_in_fifo = ObjectFifo(p1_spine_row_ty, name="p1_l0_in", depth=p1_l0_input_depth)

    p1_tg1_wts_fifo = ObjectFifo(p1_tg1_wts_all_ty, name="p1_tg1_wts", depth=1)
    p1_wt_l0, p1_wt_l1 = p1_tg1_wts_fifo.cons().split(
        offsets=[0, p1_tg1_wt_slot],
        obj_types=[p1_tg1_wt_ty, p1_tg1_wt_ty],
        names=["p1_wt_l0", "p1_wt_l1"],
        depths=[1, 1],
        placement=Tile(0, 1),
    )

    p1_inter01_fifo = ObjectFifo(
        p1_spine_row_ty, name="p1_inter_01", depth=p1_l1_input_depth
    )
    p1_l1_out_fifo = ObjectFifo(p1_spine_row_ty, name="p1_l1_out", depth=2)

    # --- P1 TG2: C2f L2 ---
    p1_c2f_in_fifo = ObjectFifo(p1_c2f_input_row_ty, name="p1_c2f_in", depth=2)

    p1_c2f_wts_fifo = ObjectFifo(p1_c2f_wts_all_ty, name="p1_c2f_wts", depth=1)
    p1_wt_cv1_f, p1_wt_bn1_f, p1_wt_bn2_f, p1_wt_cv2_f = p1_c2f_wts_fifo.cons().split(
        offsets=[
            0,
            p1_c2f_wt_slot,
            2 * p1_c2f_wt_slot,
            3 * p1_c2f_wt_slot,
        ],
        obj_types=[p1_c2f_wt_ty] * 4,
        names=["p1_wt_cv1", "p1_wt_bn1", "p1_wt_bn2", "p1_wt_cv2"],
        depths=[1, 1, 1, 1],
        placement=Tile(0, 1),
    )

    p1_cv1_out = ObjectFifo(p1_cv1_out_row_ty, name="p1_cv1_out", depth=2)

    p1_half1_to_join, p1_half2_to_bn = p1_cv1_out.cons().split(
        offsets=[0, p1_half_row],
        obj_types=[p1_half_row_ty, p1_half_row_ty],
        names=["p1_half1_to_join", "p1_half2_to_bn"],
        depths=[2, p1_bn_depth],
        placement=Tile(1, 1),
    )

    p1_bn_inter = ObjectFifo(p1_half_row_ty, name="p1_bn_inter", depth=p1_bn_depth)

    p1_cv2_in = ObjectFifo(p1_cv2_in_row_ty, name="p1_cv2_in", depth=2)
    p1_j_h1, p1_j_h2, p1_j_bn = p1_cv2_in.prod().join(
        offsets=[0, p1_half_row, 2 * p1_half_row],
        obj_types=[p1_half_row_ty, p1_half_row_ty, p1_half_row_ty],
        names=["p1_j_h1", "p1_j_h2", "p1_j_bn"],
        placement=Tile(1, 1),
    )

    p1_c2f_out_fifo = ObjectFifo(p1_cv2_out_row_ty, name="p1_c2f_out", depth=2)

    # --- P1 TG3: L3 ---
    p1_l3_in_fifo = ObjectFifo(
        p1_l3_input_row_ty, name="p1_l3_in", depth=p1_l3_input_depth
    )
    p1_l3_wt_fifo = ObjectFifo(p1_l3_wt_ty, name="p1_l3_wt", depth=1)
    p1_l3_out_fifo = ObjectFifo(p1_l3_output_row_ty, name="p1_l3_out", depth=2)

    # =====================================================================
    # P2 OBJECT FIFOs (cols 2-3-4, shifted from 0-1-2)
    # =====================================================================
    # --- Phase A FIFOs: cv1 ---
    p2_in_fifo = ObjectFifo(p2_input_row_ty, name="p2_c2f_in", depth=2)
    p2_cv1_wt_fifo = ObjectFifo(p2_cv1_wt_ty, name="p2_cv1_wt", depth=1)
    p2_cv1_out_fifo = ObjectFifo(p2_cv1_out_row_ty, name="p2_cv1_out", depth=2)

    # --- Phase B FIFOs: bn0 pipeline ---
    # Skip connection uses .forward() through MemTile (edge_detect pattern).
    # This creates a MemTile relay with independent buffering so the skip
    # consumer doesn't block the sliding-window consumer.
    p2_bn0_in_fifo = ObjectFifo(
        p2_half_row_ty, name="p2_bn0_in", depth=p2_bn_depth
    )
    p2_bn0_skip_fwd = p2_bn0_in_fifo.cons(p2_bn_broadcast_depth).forward(
        placement=Tile(2, 1), depth=p2_bn_broadcast_depth, name="p2_bn0_skip"
    )
    p2_bn0_wts_fifo = ObjectFifo(p2_bn_wts_pair_ty, name="p2_bn0_wts", depth=1)
    p2_bn0_wt1_f, p2_bn0_wt2_f = p2_bn0_wts_fifo.cons().split(
        offsets=[0, p2_bn_wt_slot],
        obj_types=[p2_bn_wt_ty, p2_bn_wt_ty],
        names=["p2_bn0_wt1", "p2_bn0_wt2"],
        depths=[1, 1],
        placement=Tile(2, 1),
    )
    p2_bn0_inter = ObjectFifo(p2_half_row_ty, name="p2_bn0_inter", depth=p2_bn_depth)
    p2_bn0_cv2_out = ObjectFifo(p2_half_row_ty, name="p2_bn0_cv2_out", depth=2)
    p2_bn0_out_fifo = ObjectFifo(p2_half_row_ty, name="p2_bn0_out", depth=2)

    # --- Phase C FIFOs: bn1 pipeline ---
    p2_bn1_in_fifo = ObjectFifo(
        p2_half_row_ty, name="p2_bn1_in", depth=p2_bn_depth
    )
    p2_bn1_skip_fwd = p2_bn1_in_fifo.cons(p2_bn_broadcast_depth).forward(
        placement=Tile(3, 1), depth=p2_bn_broadcast_depth, name="p2_bn1_skip"
    )
    p2_bn1_wts_fifo = ObjectFifo(p2_bn_wts_pair_ty, name="p2_bn1_wts", depth=1)
    p2_bn1_wt1_f, p2_bn1_wt2_f = p2_bn1_wts_fifo.cons().split(
        offsets=[0, p2_bn_wt_slot],
        obj_types=[p2_bn_wt_ty, p2_bn_wt_ty],
        names=["p2_bn1_wt1", "p2_bn1_wt2"],
        depths=[1, 1],
        placement=Tile(3, 1),
    )
    p2_bn1_inter = ObjectFifo(p2_half_row_ty, name="p2_bn1_inter", depth=p2_bn_depth)
    p2_bn1_cv2_out = ObjectFifo(p2_half_row_ty, name="p2_bn1_cv2_out", depth=2)
    p2_bn1_out_fifo = ObjectFifo(p2_half_row_ty, name="p2_bn1_out", depth=2)

    # --- Phase D FIFOs: cv2 ---
    p2_cv2_in_fifo = ObjectFifo(p2_cv2_in_row_ty, name="p2_cv2_in", depth=2)
    p2_cv2_wt_fifo = ObjectFifo(p2_cv2_wt_ty, name="p2_cv2_wt", depth=1)
    p2_cv2_out_fifo = ObjectFifo(p2_cv2_out_row_ty, name="p2_cv2_out", depth=2)

    # --- Phase E FIFOs: L5 (single core, OC streaming) ---
    p2_l5_in_fifo = ObjectFifo(
        p2_l5_input_row_ty, name="p2_l5_in", depth=p2_l5_input_depth
    )
    p2_l5_wt_fifo = ObjectFifo(p2_l5_wt_ty, name="p2_l5_wt", depth=1)
    p2_l5_out_fifo = ObjectFifo(p2_l5_output_row_ty, name="p2_l5_out", depth=2)

    # =====================================================================
    # P1 CORE FUNCTIONS
    # =====================================================================
    def p1_make_k3s2_silu_core_fn(in_width, in_ch, out_ch, out_h_val, s1, s2):
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

    p1_core_fn_l0 = p1_make_k3s2_silu_core_fn(
        l0_width, l0_ic, l0_oc, p1_l0_out_h, l0_shift1, l0_shift2
    )
    p1_core_fn_l1 = p1_make_k3s2_silu_core_fn(
        p1_l1_width, p1_l1_ic, l1_oc, p1_l1_out_h, l1_shift1, l1_shift2
    )

    def p1_core_fn_cv1(of_in, of_wt, of_out, kernel_fn):
        w = p1_c2f_width
        ci = p1_c2f_ic
        co = p1_cv1_oc
        s1 = cv1_shift1
        s2 = cv1_shift2
        elem_wt = of_wt.acquire(1)
        for _ in range_(p1_c2f_height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, s1, s2)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    def p1_core_fn_bn_with_fwd(of_in, of_wt, of_out, of_fwd, kernel_fn, fwd_fn):
        w = p1_c2f_width
        ci = p1_bn_ch
        co = p1_bn_ch
        h = p1_c2f_height
        sz = p1_half_row
        s1 = bn_cv1_shift1
        s2 = bn_cv1_shift2

        elem_wt = of_wt.acquire(1)

        # Top row: check=0
        elems = of_in.acquire(2)
        fwd0 = of_fwd.acquire(1)
        fwd_fn(elems[0], fwd0, sz)
        of_fwd.release(1)
        fwd1 = of_fwd.acquire(1)
        fwd_fn(elems[1], fwd1, sz)
        of_fwd.release(1)
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo, w, ci, co, 0, s1, s2)
        of_out.release(1)

        # Middle rows: check=1
        for _ in range_(h - 2):
            elems = of_in.acquire(3)
            fwd_e = of_fwd.acquire(1)
            fwd_fn(elems[2], fwd_e, sz)
            of_fwd.release(1)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo, w, ci, co, 1, s1, s2)
            of_in.release(1)
            of_out.release(1)

        # Bottom row: check=2
        elems = of_in.acquire(2)
        eo = of_out.acquire(1)
        kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo, w, ci, co, 2, s1, s2)
        of_in.release(2)
        of_out.release(1)

        of_wt.release(1)

    def p1_core_fn_bn_cv2(of_in, of_wt, of_out, kernel_fn):
        w = p1_c2f_width
        ci = p1_bn_ch
        co = p1_bn_ch
        h = p1_c2f_height
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

    def p1_core_fn_passthrough(of_in, of_out, kernel_fn):
        sz = p1_half_row
        for _ in range_(p1_c2f_height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, eo, sz)
            of_in.release(1)
            of_out.release(1)

    def p1_core_fn_cv2(of_in, of_wt, of_out, kernel_fn):
        w = p1_c2f_width
        ci = p1_cv2_ic
        co = p1_cv2_oc
        s1 = cv2_shift1
        s2 = cv2_shift2
        elem_wt = of_wt.acquire(1)
        for _ in range_(p1_c2f_height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, s1, s2)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    def p1_core_fn_l3(of_in, of_wt, of_out, kernel_fn):
        x_dim = p1_l3_width
        ci = p1_l3_ic
        co = l3_oc
        oh = p1_l3_out_h
        s1 = l3_shift1
        s2 = l3_shift2

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

    # =====================================================================
    # P2 CORE FUNCTIONS
    # =====================================================================
    def p2_core_fn_cv1(of_in, of_wt, of_out, kernel_fn):
        w = p2_width
        ci = p2_in_channels
        co = p2_cv1_oc
        sc = l4_cv1_scale
        elem_wt = of_wt.acquire(1)
        for _ in range_(p2_height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, sc)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    def p2_make_k3s1_core_fn(h_val, sc_val):
        def core_fn(of_in, of_wt, of_out, kernel_fn):
            w = p2_width
            ci = p2_bn_ch
            co = p2_bn_ch
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

    def p2_core_fn_add(of_a, of_b, of_out, kernel_fn):
        row_sz = p2_half_row
        for _ in range_(p2_height):
            ea = of_a.acquire(1)
            eb = of_b.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ea, eb, eo, row_sz)
            of_a.release(1)
            of_b.release(1)
            of_out.release(1)

    def p2_core_fn_cv2(of_in, of_wt, of_out, kernel_fn):
        w = p2_width
        ci = p2_cv2_ic
        co = p2_cv2_oc
        sc = l4_cv2_scale
        elem_wt = of_wt.acquire(1)
        for _ in range_(p2_height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, sc)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    def p2_core_fn_l5(of_in, of_wt, of_out, kernel_fn):
        x_dim = p2_l5_width
        ci = p2_l5_ic
        co = p2_l5_oc_chunk
        oh = p2_l5_out_h
        s1 = l5_shift1
        s2 = l5_shift2

        for _ in range_(p2_l5_n_oc_groups):
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

            of_in.release(1)
            of_wt.release(1)

    # =====================================================================
    # WORKERS
    # =====================================================================
    # --- P1 Workers (cols 0-1) ---
    p1_worker_l0 = Worker(
        p1_core_fn_l0,
        [
            p1_in_fifo.cons(),
            p1_wt_l0.cons(),
            p1_inter01_fifo.prod(),
            p1_k3s2_silu_kernel,
        ],
        placement=Tile(0, 2),
    )
    p1_worker_l1 = Worker(
        p1_core_fn_l1,
        [
            p1_inter01_fifo.cons(p1_l1_input_depth),
            p1_wt_l1.cons(),
            p1_l1_out_fifo.prod(),
            p1_k3s2_silu_kernel,
        ],
        placement=Tile(0, 3),
    )

    p1_worker_cv1 = Worker(
        p1_core_fn_cv1,
        [
            p1_c2f_in_fifo.cons(),
            p1_wt_cv1_f.cons(),
            p1_cv1_out.prod(),
            p1_k1_silu_kernel,
        ],
        placement=Tile(1, 2),
    )
    p1_worker_bn1 = Worker(
        p1_core_fn_bn_with_fwd,
        [
            p1_half2_to_bn.cons(p1_bn_depth),
            p1_wt_bn1_f.cons(),
            p1_bn_inter.prod(),
            p1_j_h2.prod(),
            p1_k3_silu_bn_kernel,
            p1_passthrough_fwd_kernel,
        ],
        placement=Tile(1, 3),
    )
    p1_worker_bn2 = Worker(
        p1_core_fn_bn_cv2,
        [
            p1_bn_inter.cons(p1_bn_depth),
            p1_wt_bn2_f.cons(),
            p1_j_bn.prod(),
            p1_k3_silu_bn_kernel,
        ],
        placement=Tile(1, 4),
    )
    p1_worker_pass = Worker(
        p1_core_fn_passthrough,
        [p1_half1_to_join.cons(), p1_j_h1.prod(), p1_passthrough_kernel],
        placement=Tile(0, 4),
    )
    p1_worker_cv2 = Worker(
        p1_core_fn_cv2,
        [
            p1_cv2_in.cons(),
            p1_wt_cv2_f.cons(),
            p1_c2f_out_fifo.prod(),
            p1_k1_silu_cv2_kernel,
        ],
        placement=Tile(1, 5),
    )

    p1_worker_l3 = Worker(
        p1_core_fn_l3,
        [
            p1_l3_in_fifo.cons(),
            p1_l3_wt_fifo.cons(),
            p1_l3_out_fifo.prod(),
            p1_l3_k3s2_kernel,
        ],
        placement=Tile(0, 5),
    )

    # --- P2 Workers (cols 2-3-4, shifted from 0-1-2) ---
    p2_worker_cv1 = Worker(
        p2_core_fn_cv1,
        [
            p2_in_fifo.cons(),
            p2_cv1_wt_fifo.cons(),
            p2_cv1_out_fifo.prod(),
            p2_k1_kernel,
        ],
        placement=Tile(2, 2),
    )
    p2_worker_bn0cv1 = Worker(
        p2_make_k3s1_core_fn(p2_height, l4_bn0_cv1_scale),
        [
            p2_bn0_in_fifo.cons(p2_bn_depth),
            p2_bn0_wt1_f.cons(),
            p2_bn0_inter.prod(),
            p2_k3_bn_kernel,
        ],
        placement=Tile(2, 3),
    )
    p2_worker_bn0cv2 = Worker(
        p2_make_k3s1_core_fn(p2_height, l4_bn0_cv2_scale),
        [
            p2_bn0_inter.cons(p2_bn_depth),
            p2_bn0_wt2_f.cons(),
            p2_bn0_cv2_out.prod(),
            p2_k3_bn_kernel,
        ],
        placement=Tile(2, 4),
    )
    p2_worker_bn0add = Worker(
        p2_core_fn_add,
        [
            p2_bn0_cv2_out.cons(),
            p2_bn0_skip_fwd.cons(),
            p2_bn0_out_fifo.prod(),
            p2_add_kernel,
        ],
        placement=Tile(2, 5),
    )
    p2_worker_bn1cv1 = Worker(
        p2_make_k3s1_core_fn(p2_height, l4_bn1_cv1_scale),
        [
            p2_bn1_in_fifo.cons(p2_bn_depth),
            p2_bn1_wt1_f.cons(),
            p2_bn1_inter.prod(),
            p2_k3_bn_kernel,
        ],
        placement=Tile(3, 2),
    )
    p2_worker_bn1cv2 = Worker(
        p2_make_k3s1_core_fn(p2_height, l4_bn1_cv2_scale),
        [
            p2_bn1_inter.cons(p2_bn_depth),
            p2_bn1_wt2_f.cons(),
            p2_bn1_cv2_out.prod(),
            p2_k3_bn_kernel,
        ],
        placement=Tile(3, 3),
    )
    p2_worker_bn1add = Worker(
        p2_core_fn_add,
        [
            p2_bn1_cv2_out.cons(),
            p2_bn1_skip_fwd.cons(),
            p2_bn1_out_fifo.prod(),
            p2_add_kernel,
        ],
        placement=Tile(3, 4),
    )
    p2_worker_cv2 = Worker(
        p2_core_fn_cv2,
        [
            p2_cv2_in_fifo.cons(),
            p2_cv2_wt_fifo.cons(),
            p2_cv2_out_fifo.prod(),
            p2_k1_cv2_kernel,
        ],
        placement=Tile(3, 5),
    )

    p2_worker_l5 = Worker(
        p2_core_fn_l5,
        [
            p2_l5_in_fifo.cons(),
            p2_l5_wt_fifo.cons(),
            p2_l5_out_fifo.prod(),
            p2_l5_kernel,
        ],
        placement=Tile(4, 2),
    )

    # =====================================================================
    # RUNTIME SEQUENCE
    # =====================================================================
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W_buf, O):
        rt.start(
            # P1 workers (8)
            p1_worker_l0,
            p1_worker_l1,
            p1_worker_cv1,
            p1_worker_bn1,
            p1_worker_bn2,
            p1_worker_pass,
            p1_worker_cv2,
            p1_worker_l3,
            # P2 workers (9)
            p2_worker_cv1,
            p2_worker_bn0cv1,
            p2_worker_bn0cv2,
            p2_worker_bn0add,
            p2_worker_bn1cv1,
            p2_worker_bn1cv2,
            p2_worker_bn1add,
            p2_worker_cv2,
            p2_worker_l5,
        )

        # =============================================================
        # P1 TG1: L0->L1 pipeline to P1_scratch_A
        # =============================================================
        p1_tg1 = rt.task_group()

        # Fill input (L0) from DDR input buffer I
        p1_in_d3, p1_in_d2, p1_in_d1, p1_in_d0 = _factorize_tensor(p1_total_input)
        rt.fill(
            p1_in_fifo.prod(),
            I,
            TensorAccessPattern(
                (1, p1_total_input),
                offset=0,
                sizes=[p1_in_d3, p1_in_d2, p1_in_d1, p1_in_d0],
                strides=[
                    p1_in_d2 * p1_in_d1 * p1_in_d0,
                    p1_in_d1 * p1_in_d0,
                    p1_in_d0,
                    1,
                ],
            ),
            task_group=p1_tg1,
        )

        # Fill TG1 weights
        p1_tg1_wt_d3, p1_tg1_wt_d2, p1_tg1_wt_d1, p1_tg1_wt_d0 = _factorize_tensor(
            p1_tg1_total_wt
        )
        rt.fill(
            p1_tg1_wts_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=p1_wt_offset,
                sizes=[
                    p1_tg1_wt_d3,
                    p1_tg1_wt_d2,
                    p1_tg1_wt_d1,
                    p1_tg1_wt_d0,
                ],
                strides=[
                    p1_tg1_wt_d2 * p1_tg1_wt_d1 * p1_tg1_wt_d0,
                    p1_tg1_wt_d1 * p1_tg1_wt_d0,
                    p1_tg1_wt_d0,
                    1,
                ],
            ),
            task_group=p1_tg1,
        )

        # Drain L1 output to P1_scratch_A
        p1_sa_d3, p1_sa_d2, p1_sa_d1, p1_sa_d0 = _factorize_tensor(p1_scratch_a_size)
        rt.drain(
            p1_l1_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p1_scratch_a_offset,
                sizes=[p1_sa_d3, p1_sa_d2, p1_sa_d1, p1_sa_d0],
                strides=[
                    p1_sa_d2 * p1_sa_d1 * p1_sa_d0,
                    p1_sa_d1 * p1_sa_d0,
                    p1_sa_d0,
                    1,
                ],
            ),
            wait=True,
            task_group=p1_tg1,
        )

        rt.finish_task_group(p1_tg1)

        # =============================================================
        # P1 TG2: C2f L2, reads P1_scratch_A -> writes P1_scratch_B
        # =============================================================
        p1_tg2 = rt.task_group()

        # Fill C2f input from P1_scratch_A
        p1_c2f_in_d3, p1_c2f_in_d2, p1_c2f_in_d1, p1_c2f_in_d0 = _factorize_tensor(
            p1_scratch_a_size
        )
        rt.fill(
            p1_c2f_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p1_scratch_a_offset,
                sizes=[
                    p1_c2f_in_d3,
                    p1_c2f_in_d2,
                    p1_c2f_in_d1,
                    p1_c2f_in_d0,
                ],
                strides=[
                    p1_c2f_in_d2 * p1_c2f_in_d1 * p1_c2f_in_d0,
                    p1_c2f_in_d1 * p1_c2f_in_d0,
                    p1_c2f_in_d0,
                    1,
                ],
            ),
            task_group=p1_tg2,
        )

        # Fill C2f weights
        p1_c2f_wt_ddr_offset = p1_wt_offset + p1_tg1_total_wt
        p1_c2f_wt_d3, p1_c2f_wt_d2, p1_c2f_wt_d1, p1_c2f_wt_d0 = _factorize_tensor(
            p1_c2f_total_wt
        )
        rt.fill(
            p1_c2f_wts_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=p1_c2f_wt_ddr_offset,
                sizes=[
                    p1_c2f_wt_d3,
                    p1_c2f_wt_d2,
                    p1_c2f_wt_d1,
                    p1_c2f_wt_d0,
                ],
                strides=[
                    p1_c2f_wt_d2 * p1_c2f_wt_d1 * p1_c2f_wt_d0,
                    p1_c2f_wt_d1 * p1_c2f_wt_d0,
                    p1_c2f_wt_d0,
                    1,
                ],
            ),
            task_group=p1_tg2,
        )

        # Drain C2f output to P1_scratch_B
        p1_sb_d3, p1_sb_d2, p1_sb_d1, p1_sb_d0 = _factorize_tensor(p1_scratch_b_size)
        rt.drain(
            p1_c2f_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p1_scratch_b_offset,
                sizes=[p1_sb_d3, p1_sb_d2, p1_sb_d1, p1_sb_d0],
                strides=[
                    p1_sb_d2 * p1_sb_d1 * p1_sb_d0,
                    p1_sb_d1 * p1_sb_d0,
                    p1_sb_d0,
                    1,
                ],
            ),
            wait=True,
            task_group=p1_tg2,
        )

        rt.finish_task_group(p1_tg2)

        # =============================================================
        # P1 TG3: L3, reads P1_scratch_B -> writes to P2_input area
        # =============================================================
        p1_tg3 = rt.task_group()

        # Fill L3 input from P1_scratch_B
        p1_l3_in_d3, p1_l3_in_d2, p1_l3_in_d1, p1_l3_in_d0 = _factorize_tensor(
            p1_scratch_b_size
        )
        rt.fill(
            p1_l3_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p1_scratch_b_offset,
                sizes=[
                    p1_l3_in_d3,
                    p1_l3_in_d2,
                    p1_l3_in_d1,
                    p1_l3_in_d0,
                ],
                strides=[
                    p1_l3_in_d2 * p1_l3_in_d1 * p1_l3_in_d0,
                    p1_l3_in_d1 * p1_l3_in_d0,
                    p1_l3_in_d0,
                    1,
                ],
            ),
            task_group=p1_tg3,
        )

        # Fill L3 weight
        p1_l3_wt_ddr_offset = p1_wt_offset + p1_tg1_total_wt + p1_c2f_total_wt
        p1_l3_wt_d3, p1_l3_wt_d2, p1_l3_wt_d1, p1_l3_wt_d0 = _factorize_tensor(
            p1_l3_wt_size
        )
        rt.fill(
            p1_l3_wt_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=p1_l3_wt_ddr_offset,
                sizes=[
                    p1_l3_wt_d3,
                    p1_l3_wt_d2,
                    p1_l3_wt_d1,
                    p1_l3_wt_d0,
                ],
                strides=[
                    p1_l3_wt_d2 * p1_l3_wt_d1 * p1_l3_wt_d0,
                    p1_l3_wt_d1 * p1_l3_wt_d0,
                    p1_l3_wt_d0,
                    1,
                ],
            ),
            task_group=p1_tg3,
        )

        # Drain L3 output to P2_input area (so P2 can read it)
        p1_l3_total_output = l3_oc * p1_l3_out_h * p1_l3_out_w
        p1_out_d3, p1_out_d2, p1_out_d1, p1_out_d0 = _factorize_tensor(
            p1_l3_total_output
        )
        rt.drain(
            p1_l3_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p2_input_offset,
                sizes=[p1_out_d3, p1_out_d2, p1_out_d1, p1_out_d0],
                strides=[
                    p1_out_d2 * p1_out_d1 * p1_out_d0,
                    p1_out_d1 * p1_out_d0,
                    p1_out_d0,
                    1,
                ],
            ),
            wait=True,
            task_group=p1_tg3,
        )

        rt.finish_task_group(p1_tg3)

        # =============================================================
        # P2 TG_A: cv1 -> strided drain to P2_concat
        # =============================================================
        p2_tg_a = rt.task_group()

        # Fill P2 input from P2_input area in O (L3 output)
        p2_in_dims = _factorize_tensor(p2_total_input)
        rt.fill(
            p2_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p2_input_offset,
                sizes=list(p2_in_dims),
                strides=[
                    p2_in_dims[1] * p2_in_dims[2] * p2_in_dims[3],
                    p2_in_dims[2] * p2_in_dims[3],
                    p2_in_dims[3],
                    1,
                ],
            ),
            task_group=p2_tg_a,
        )

        # Fill P2 cv1 weights
        p2_cv1w_dims = _factorize_tensor(p2_cv1_wt)
        rt.fill(
            p2_cv1_wt_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=p2_wt_offset,
                sizes=list(p2_cv1w_dims),
                strides=[
                    p2_cv1w_dims[1] * p2_cv1w_dims[2] * p2_cv1w_dims[3],
                    p2_cv1w_dims[2] * p2_cv1w_dims[3],
                    p2_cv1w_dims[3],
                    1,
                ],
            ),
            task_group=p2_tg_a,
        )

        # Drain cv1 output with strided write into P2_concat rows
        p2_cr_d0 = min(p2_cv1_out_row, 1023)
        while p2_cr_d0 % 4 != 0:
            p2_cr_d0 -= 1
        while p2_cr_d0 >= 4:
            if p2_cv1_out_row % p2_cr_d0 == 0:
                break
            p2_cr_d0 -= 4
        p2_cr_d1 = p2_cv1_out_row // p2_cr_d0

        rt.drain(
            p2_cv1_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p2_concat_offset,
                sizes=[1, p2_height, p2_cr_d1, p2_cr_d0],
                strides=[0, p2_cv2_in_row, p2_cr_d0, 1],
            ),
            wait=True,
            task_group=p2_tg_a,
        )

        rt.finish_task_group(p2_tg_a)

        # =============================================================
        # P2 TG_B: bn0 (broadcast input to cv1 + skip-add)
        # =============================================================
        p2_tg_b = rt.task_group()

        # Factorize p2_half_row for inner TAP dimensions
        p2_hr_d0 = min(p2_half_row, 1023)
        while p2_hr_d0 % 4 != 0:
            p2_hr_d0 -= 1
        while p2_hr_d0 >= 4:
            if p2_half_row % p2_hr_d0 == 0:
                break
            p2_hr_d0 -= 4
        p2_hr_d1 = p2_half_row // p2_hr_d0

        # Fill bn0_in_fifo: broadcast to both bn0cv1 and bn0add
        rt.fill(
            p2_bn0_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p2_concat_offset + p2_half_row,
                sizes=[1, p2_height, p2_hr_d1, p2_hr_d0],
                strides=[0, p2_cv2_in_row, p2_hr_d0, 1],
            ),
            task_group=p2_tg_b,
        )

        p2_bn0_wt_ddr_offset = p2_wt_offset + p2_cv1_wt
        p2_bn0_wt_dims = _factorize_tensor(2 * p2_bn_wt_slot)
        rt.fill(
            p2_bn0_wts_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=p2_bn0_wt_ddr_offset,
                sizes=list(p2_bn0_wt_dims),
                strides=[
                    p2_bn0_wt_dims[1] * p2_bn0_wt_dims[2] * p2_bn0_wt_dims[3],
                    p2_bn0_wt_dims[2] * p2_bn0_wt_dims[3],
                    p2_bn0_wt_dims[3],
                    1,
                ],
            ),
            task_group=p2_tg_b,
        )

        rt.drain(
            p2_bn0_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p2_concat_offset + 2 * p2_half_row,
                sizes=[1, p2_height, p2_hr_d1, p2_hr_d0],
                strides=[0, p2_cv2_in_row, p2_hr_d0, 1],
            ),
            wait=True,
            task_group=p2_tg_b,
        )

        rt.finish_task_group(p2_tg_b)

        # =============================================================
        # P2 TG_C: bn1 (broadcast input to cv1 + skip-add)
        # =============================================================
        p2_tg_c = rt.task_group()

        # Fill bn1_in_fifo: broadcast to both bn1cv1 and bn1add
        rt.fill(
            p2_bn1_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p2_concat_offset + 2 * p2_half_row,
                sizes=[1, p2_height, p2_hr_d1, p2_hr_d0],
                strides=[0, p2_cv2_in_row, p2_hr_d0, 1],
            ),
            task_group=p2_tg_c,
        )

        p2_bn1_wt_ddr_offset = p2_wt_offset + p2_cv1_wt + 2 * p2_bn_wt_slot
        p2_bn1_wt_dims = _factorize_tensor(2 * p2_bn_wt_slot)
        rt.fill(
            p2_bn1_wts_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=p2_bn1_wt_ddr_offset,
                sizes=list(p2_bn1_wt_dims),
                strides=[
                    p2_bn1_wt_dims[1] * p2_bn1_wt_dims[2] * p2_bn1_wt_dims[3],
                    p2_bn1_wt_dims[2] * p2_bn1_wt_dims[3],
                    p2_bn1_wt_dims[3],
                    1,
                ],
            ),
            task_group=p2_tg_c,
        )

        rt.drain(
            p2_bn1_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p2_concat_offset + 3 * p2_half_row,
                sizes=[1, p2_height, p2_hr_d1, p2_hr_d0],
                strides=[0, p2_cv2_in_row, p2_hr_d0, 1],
            ),
            wait=True,
            task_group=p2_tg_c,
        )

        rt.finish_task_group(p2_tg_c)

        # =============================================================
        # P2 TG_D: cv2 reads assembled P2_concat linearly -> P2_L4_scratch
        # =============================================================
        p2_tg_d = rt.task_group()

        p2_cv2i_dims = _factorize_tensor(p2_total_concat)
        rt.fill(
            p2_cv2_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p2_concat_offset,
                sizes=list(p2_cv2i_dims),
                strides=[
                    p2_cv2i_dims[1] * p2_cv2i_dims[2] * p2_cv2i_dims[3],
                    p2_cv2i_dims[2] * p2_cv2i_dims[3],
                    p2_cv2i_dims[3],
                    1,
                ],
            ),
            task_group=p2_tg_d,
        )

        p2_cv2w_dims = _factorize_tensor(p2_cv2_wt)
        p2_cv2_wt_ddr_offset = p2_wt_offset + p2_cv1_wt + 4 * p2_bn_wt_slot
        rt.fill(
            p2_cv2_wt_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=p2_cv2_wt_ddr_offset,
                sizes=list(p2_cv2w_dims),
                strides=[
                    p2_cv2w_dims[1] * p2_cv2w_dims[2] * p2_cv2w_dims[3],
                    p2_cv2w_dims[2] * p2_cv2w_dims[3],
                    p2_cv2w_dims[3],
                    1,
                ],
            ),
            task_group=p2_tg_d,
        )

        p2_out_dims = _factorize_tensor(p2_l4_output_size)
        rt.drain(
            p2_cv2_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p2_l4_scratch_offset,
                sizes=list(p2_out_dims),
                strides=[
                    p2_out_dims[1] * p2_out_dims[2] * p2_out_dims[3],
                    p2_out_dims[2] * p2_out_dims[3],
                    p2_out_dims[3],
                    1,
                ],
            ),
            wait=True,
            task_group=p2_tg_d,
        )

        rt.finish_task_group(p2_tg_d)

        # =============================================================
        # P2 TG_E: L5 k3s2 (OC streaming) -> final output at offset 0
        # =============================================================
        p2_tg_e = rt.task_group()

        # Input TAP: re-stream L4 output n_oc_groups times via stride-0
        p2_l5_in_d2, p2_l5_in_d1, p2_l5_in_d0 = _factorize_3d(p2_l5_total_input)
        rt.fill(
            p2_l5_in_fifo.prod(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=p2_l4_scratch_offset,
                sizes=[
                    p2_l5_n_oc_groups,
                    p2_l5_in_d2,
                    p2_l5_in_d1,
                    p2_l5_in_d0,
                ],
                strides=[0, p2_l5_in_d1 * p2_l5_in_d0, p2_l5_in_d0, 1],
            ),
            task_group=p2_tg_e,
        )

        # Weight TAP: contiguous read of all OC group weight chunks
        p2_l5_wt_d3, p2_l5_wt_d2, p2_l5_wt_d1, p2_l5_wt_d0 = _factorize_tensor(
            p2_l5_total_wt
        )
        rt.fill(
            p2_l5_wt_fifo.prod(),
            W_buf,
            TensorAccessPattern(
                (1, total_weights),
                offset=p2_wt_offset + p2_l4_total_wt,
                sizes=[
                    p2_l5_wt_d3,
                    p2_l5_wt_d2,
                    p2_l5_wt_d1,
                    p2_l5_wt_d0,
                ],
                strides=[
                    p2_l5_wt_d2 * p2_l5_wt_d1 * p2_l5_wt_d0,
                    p2_l5_wt_d1 * p2_l5_wt_d0,
                    p2_l5_wt_d0,
                    1,
                ],
            ),
            task_group=p2_tg_e,
        )

        # Output TAP: strided drain to interleave OC chunks at offset 0
        p2_pe_d0 = min(p2_l5_output_elem, 1023)
        while p2_pe_d0 % 4 != 0:
            p2_pe_d0 -= 1
        while p2_pe_d0 >= 4:
            if p2_l5_output_elem % p2_pe_d0 == 0:
                break
            p2_pe_d0 -= 4
        p2_pe_d1 = p2_l5_output_elem // p2_pe_d0

        rt.drain(
            p2_l5_out_fifo.cons(),
            O,
            TensorAccessPattern(
                (1, total_output_buf),
                offset=0,
                sizes=[
                    p2_l5_n_oc_groups,
                    p2_l5_out_h,
                    p2_pe_d1,
                    p2_pe_d0,
                ],
                strides=[
                    p2_l5_oc_chunk * p2_l5_out_w,
                    p2_l5_output_row_total,
                    p2_pe_d0,
                    1,
                ],
            ),
            wait=True,
            task_group=p2_tg_e,
        )

        rt.finish_task_group(p2_tg_e)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # p1_p2_combined


# ---------------------------------------------------------------------------
# Neck C2f dataflow block (parameterized for L12, L15, L18)
# ---------------------------------------------------------------------------


def my_dataflow_c2f_neck(
    dev,
    height,
    width,
    in_channels,
    cv1_oc,
    bn_ch,
    cv2_oc,
    cv1_shift1,
    cv1_shift2,
    bn0_cv1_shift1,
    bn0_cv1_shift2,
    bn0_cv2_shift1,
    bn0_cv2_shift2,
    cv2_shift1,
    cv2_shift2,
):
    """Generic C2f block for neck layers: n=1 bottleneck, no residual add.

    All sub-layers use fused conv+bias+SiLU (int8 in, int8 out).

    Multi-phase execution building concat in-place:

    DDR output buffer: [final_output(cv2_oc*H*W) | concat(cv2_ic*H*W)]

    Phase A: cv1(IC->cv1_oc, k1 fused SiLU), with OC streaming if needed
             -> strided drain to concat[0:cv1_oc*W]
    Phase B: Read half2(bn_ch) from concat -> bn0.cv1 -> bn0.cv2 (k3 fused SiLU)
             -> drain bn0_out to concat[cv1_oc*W:]
    Phase C: Read full concat linearly -> cv2(cv2_ic->cv2_oc, k1 fused SiLU) -> output

    Automatically determines:
    - Whether cv1 needs OC streaming based on L1 budget.
    - Whether bn0 cores can share adjacent tiles (same column) based on
      combined shared-memory budget, or need separate columns.

    Supported configurations:
      L12: IC=384, cv1_oc=128, bn_ch=64, cv2_oc=128, 40x40
      L15: IC=192, cv1_oc=64,  bn_ch=32, cv2_oc=64,  80x80
      L18: IC=192, cv1_oc=128, bn_ch=64, cv2_oc=128, 40x40

    Args:
        dev: Device type string.
        height, width: Spatial dims.
        in_channels: Input channels (384 for L12, 192 for L15/L18).
        cv1_oc: cv1 output channels (= 2 * bn_ch).
        bn_ch: Bottleneck channel count (half of cv1_oc).
        cv2_oc: cv2 output channels.
        cv1_shift1..cv2_shift2: Per-layer fused SiLU shift params.
    """
    xfr_dtype = np.int8

    cv2_ic = cv1_oc + bn_ch  # half1 + half2 + bn0_out

    # --- Row sizes ---
    input_row = in_channels * width
    half_row = bn_ch * width
    cv2_in_row = cv2_ic * width
    cv2_out_row = cv2_oc * width

    # --- OC streaming for cv1 (IC->cv1_oc, k1) ---
    # Determine if cv1 weights fit in L1 without chunking
    cv1_input_bufs = 2 * in_channels * width
    cv1_avail = 65536 - 1040 - cv1_input_bufs
    cv1_full_wt = cv1_oc * in_channels + cv1_oc * 4
    cv1_full_out = 2 * cv1_oc * width

    if cv1_full_wt + cv1_full_out <= cv1_avail:
        cv1_oc_chunk = cv1_oc
        cv1_n_oc = 1
    else:
        # Find largest OC chunk that fits
        cv1_oc_chunk = None
        for try_oc in range(cv1_oc, 0, -8):
            if cv1_oc % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt = try_oc * in_channels + try_oc * 4
            out = 2 * try_oc * width
            if wt + out <= cv1_avail:
                cv1_oc_chunk = try_oc
                break
        assert cv1_oc_chunk is not None, (
            f"cv1 infeasible: IC={in_channels}, OC={cv1_oc}, W={width}"
        )
        cv1_n_oc = cv1_oc // cv1_oc_chunk

    cv1_out_row = cv1_oc_chunk * width
    cv1_wt_chunk = cv1_oc_chunk * in_channels + cv1_oc_chunk * 4  # weights + bias

    cv2_wt_size = cv2_oc * cv2_ic + cv2_oc * 4  # weights + bias

    # bn k3 weights (fused: weights + bias)
    bn_k3_wt = bn_ch * bn_ch * 9 + bn_ch * 4

    # --- Totals ---
    total_input = in_channels * height * width
    total_output = cv2_oc * height * width
    total_concat = cv2_ic * height * width

    # DDR output buffer: [final_output | concat_scratch]
    concat_offset = total_output
    output_buf_size = total_output + total_concat

    # Weight layout: [cv1_chunks(n_oc × wt_chunk) | bn0cv1_wt | bn0cv2_wt | cv2_wt]
    cv1_total_wt = cv1_n_oc * cv1_wt_chunk
    total_wt = cv1_total_wt + 2 * bn_k3_wt + cv2_wt_size

    # --- L1 budget checks ---
    bn_depth = 4
    core_cv1_l1 = 1040 + 2 * input_row + cv1_wt_chunk + 2 * cv1_out_row
    assert core_cv1_l1 <= 65536, f"cv1 L1: {core_cv1_l1}B"

    core_bn_l1 = 1040 + (bn_depth + 1) * half_row + bn_k3_wt + 2 * half_row
    assert core_bn_l1 <= 65536, f"bn k3 L1: {core_bn_l1}B"

    core_cv2_l1 = 1040 + 2 * cv2_in_row + cv2_wt_size + 2 * cv2_out_row
    assert core_cv2_l1 <= 65536, f"cv2 L1: {core_cv2_l1}B"

    # --- Column layout ---
    # Always use 2 columns: even when bn0 weights fit in shared memory,
    # the k3 fused SiLU kernel can exceed 16KB program memory on some
    # channel configurations when placed in the same column.
    bn0_same_column = False

    dev_ty = NPU2()

    # --- Types ---
    input_row_ty = np.ndarray[(input_row,), np.dtype[xfr_dtype]]
    cv1_out_row_ty = np.ndarray[(cv1_out_row,), np.dtype[xfr_dtype]]
    cv1_wt_ty = np.ndarray[(cv1_wt_chunk,), np.dtype[xfr_dtype]]
    half_row_ty = np.ndarray[(half_row,), np.dtype[xfr_dtype]]
    bn_wt_ty = np.ndarray[(bn_k3_wt,), np.dtype[xfr_dtype]]
    cv2_in_row_ty = np.ndarray[(cv2_in_row,), np.dtype[xfr_dtype]]
    cv2_out_row_ty = np.ndarray[(cv2_out_row,), np.dtype[xfr_dtype]]
    cv2_wt_ty = np.ndarray[(cv2_wt_size,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(output_buf_size,), np.dtype[xfr_dtype]]

    # --- Kernels ---
    k1_silu_kernel = Kernel(
        "conv2dk1_i8_silu",
        "conv2dk1_i8_silu.o",
        [input_row_ty, cv1_wt_ty, cv1_out_row_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32],
    )

    k3_silu_kernel = Kernel(
        "conv2dk3_i8_silu",
        "conv2dk3_i8_silu.o",
        [half_row_ty, half_row_ty, half_row_ty, bn_wt_ty, half_row_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32, np.int32],
    )

    k1_cv2_kernel = Kernel(
        "conv2dk1_i8_silu_cv2",
        "conv2dk1_i8_silu_cv2.o",
        [cv2_in_row_ty, cv2_wt_ty, cv2_out_row_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32],
    )

    # --- Phase A FIFOs: cv1 with OC streaming ---
    in_fifo = ObjectFifo(input_row_ty, name="l12_in", depth=2)
    cv1_wt_fifo = ObjectFifo(cv1_wt_ty, name="l12_cv1_wt", depth=1)
    cv1_out_fifo = ObjectFifo(cv1_out_row_ty, name="l12_cv1_out", depth=2)

    # --- Phase B FIFOs: bn0 pipeline (core-to-core) ---
    # Separate weight FIFOs avoid a 74KB split buffer at MemTile
    bn0_in_fifo = ObjectFifo(half_row_ty, name="l12_bn0_in", depth=bn_depth)
    bn0_cv1_wt_fifo = ObjectFifo(bn_wt_ty, name="l12_bn0cv1_wt", depth=1)
    bn0_cv2_wt_fifo = ObjectFifo(bn_wt_ty, name="l12_bn0cv2_wt", depth=1)
    bn0_inter = ObjectFifo(half_row_ty, name="l12_bn0_inter", depth=bn_depth)
    bn0_out_fifo = ObjectFifo(half_row_ty, name="l12_bn0_out", depth=2)

    # --- Phase C FIFOs: cv2 ---
    cv2_in_fifo = ObjectFifo(cv2_in_row_ty, name="l12_cv2_in", depth=2)
    cv2_wt_fifo = ObjectFifo(cv2_wt_ty, name="l12_cv2_wt", depth=1)
    cv2_out_fifo = ObjectFifo(cv2_out_row_ty, name="l12_cv2_out", depth=2)

    # --- Core functions ---

    def core_fn_cv1(of_in, of_wt, of_out, kernel_fn):
        """cv1: k1 fused SiLU with OC streaming (n_oc groups)."""
        w = width
        ci = in_channels
        co = cv1_oc_chunk
        s1, s2 = cv1_shift1, cv1_shift2
        for _ in range_(cv1_n_oc):
            wt = of_wt.acquire(1)
            for _ in range_(height):
                ei = of_in.acquire(1)
                eo = of_out.acquire(1)
                kernel_fn(ei, wt, eo, w, ci, co, s1, s2)
                of_in.release(1)
                of_out.release(1)
            of_wt.release(1)

    def _make_k3_core_fn(shift1_val, shift2_val):
        def core_fn(of_in, of_wt, of_out, kernel_fn):
            w = width
            ci = bn_ch
            co = bn_ch
            h = height
            s1 = shift1_val
            s2 = shift2_val
            elem_wt = of_wt.acquire(1)

            # Top row (check=0)
            elems = of_in.acquire(2)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo,
                      w, ci, co, 0, s1, s2)
            of_out.release(1)

            # Middle rows (check=1)
            for _ in range_(h - 2):
                elems = of_in.acquire(3)
                eo = of_out.acquire(1)
                kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo,
                          w, ci, co, 1, s1, s2)
                of_in.release(1)
                of_out.release(1)

            # Bottom row (check=2)
            elems = of_in.acquire(2)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo,
                      w, ci, co, 2, s1, s2)
            of_in.release(2)
            of_out.release(1)

            of_wt.release(1)
        return core_fn

    def core_fn_cv2(of_in, of_wt, of_out, kernel_fn):
        """cv2: k1 fused SiLU, single group."""
        w = width
        ci = cv2_ic
        co = cv2_oc
        s1, s2 = cv2_shift1, cv2_shift2
        elem_wt = of_wt.acquire(1)
        for _ in range_(height):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, s1, s2)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    # --- Workers: column layout depends on bn0 shared-memory budget ---
    if bn0_same_column:
        # 1 column: all 4 cores stacked vertically (bn0 cores adjacent)
        bn0cv1_tile = Tile(0, 3)
        bn0cv2_tile = Tile(0, 4)
        cv2_tile = Tile(0, 5)
    else:
        # 2 columns: bn0.cv2 and cv2 on column 1 to avoid shared-memory overflow
        bn0cv1_tile = Tile(0, 3)
        bn0cv2_tile = Tile(1, 2)
        cv2_tile = Tile(1, 3)

    worker_cv1 = Worker(
        core_fn_cv1,
        [in_fifo.cons(), cv1_wt_fifo.cons(), cv1_out_fifo.prod(), k1_silu_kernel],
        placement=Tile(0, 2),
    )
    worker_bn0cv1 = Worker(
        _make_k3_core_fn(bn0_cv1_shift1, bn0_cv1_shift2),
        [bn0_in_fifo.cons(bn_depth), bn0_cv1_wt_fifo.cons(), bn0_inter.prod(),
         k3_silu_kernel],
        placement=bn0cv1_tile,
    )
    worker_bn0cv2 = Worker(
        _make_k3_core_fn(bn0_cv2_shift1, bn0_cv2_shift2),
        [bn0_inter.cons(bn_depth), bn0_cv2_wt_fifo.cons(), bn0_out_fifo.prod(),
         k3_silu_kernel],
        placement=bn0cv2_tile,
    )
    worker_cv2 = Worker(
        core_fn_cv2,
        [cv2_in_fifo.cons(), cv2_wt_fifo.cons(), cv2_out_fifo.prod(),
         k1_cv2_kernel],
        placement=cv2_tile,
    )

    # ===== Runtime sequence =====
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker_cv1, worker_bn0cv1, worker_bn0cv2, worker_cv2)

        # ===== TG-A: cv1 with OC streaming -> concat scratch =====
        tg_a = rt.task_group()

        # Fill input with stride-0 repeat for n_oc groups
        in_d2, in_d1, in_d0 = _factorize_3d(total_input)
        rt.fill(
            in_fifo.prod(), I,
            TensorAccessPattern(
                (1, total_input), offset=0,
                sizes=[cv1_n_oc, in_d2, in_d1, in_d0],
                strides=[0, in_d1 * in_d0, in_d0, 1],
            ),
            task_group=tg_a,
        )

        # Fill cv1 weights (contiguous: n_oc chunks)
        cv1_wt_d3, cv1_wt_d2, cv1_wt_d1, cv1_wt_d0 = _factorize_tensor(
            cv1_total_wt
        )
        rt.fill(
            cv1_wt_fifo.prod(), W,
            TensorAccessPattern(
                (1, total_wt), offset=0,
                sizes=[cv1_wt_d3, cv1_wt_d2, cv1_wt_d1, cv1_wt_d0],
                strides=[
                    cv1_wt_d2 * cv1_wt_d1 * cv1_wt_d0,
                    cv1_wt_d1 * cv1_wt_d0,
                    cv1_wt_d0, 1,
                ],
            ),
            task_group=tg_a,
        )

        # Drain cv1 output: strided interleave into concat[0:128ch] within 192ch rows
        # For OC group g, row r: offset = concat_offset + r*cv2_in_row + g*cv1_oc_chunk*width
        pe_d0 = min(cv1_out_row, 1023)
        while pe_d0 % 4 != 0:
            pe_d0 -= 1
        while pe_d0 >= 4:
            if cv1_out_row % pe_d0 == 0:
                break
            pe_d0 -= 4
        pe_d1 = cv1_out_row // pe_d0

        rt.drain(
            cv1_out_fifo.cons(), O,
            TensorAccessPattern(
                (1, output_buf_size), offset=concat_offset,
                sizes=[cv1_n_oc, height, pe_d1, pe_d0],
                strides=[cv1_oc_chunk * width, cv2_in_row, pe_d0, 1],
            ),
            wait=True,
            task_group=tg_a,
        )

        rt.finish_task_group(tg_a)

        # ===== TG-B: bn0 (half2 -> k3 -> k3 -> bn0_out) =====
        tg_b = rt.task_group()

        # Read half2(64ch) from concat[64:128ch] -- strided from 192ch rows
        hr_d0 = min(half_row, 1023)
        while hr_d0 % 4 != 0:
            hr_d0 -= 1
        while hr_d0 >= 4:
            if half_row % hr_d0 == 0:
                break
            hr_d0 -= 4
        hr_d1 = half_row // hr_d0

        rt.fill(
            bn0_in_fifo.prod(), O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset + half_row,
                sizes=[1, height, hr_d1, hr_d0],
                strides=[0, cv2_in_row, hr_d0, 1],
            ),
            task_group=tg_b,
        )

        # Fill bn0.cv1 weights
        bn0cv1_wt_offset = cv1_total_wt
        bn0cv1_wt_dims = _factorize_tensor(bn_k3_wt)
        rt.fill(
            bn0_cv1_wt_fifo.prod(), W,
            TensorAccessPattern(
                (1, total_wt), offset=bn0cv1_wt_offset,
                sizes=list(bn0cv1_wt_dims),
                strides=[
                    bn0cv1_wt_dims[1] * bn0cv1_wt_dims[2] * bn0cv1_wt_dims[3],
                    bn0cv1_wt_dims[2] * bn0cv1_wt_dims[3],
                    bn0cv1_wt_dims[3], 1,
                ],
            ),
            task_group=tg_b,
        )

        # Fill bn0.cv2 weights
        bn0cv2_wt_offset = cv1_total_wt + bn_k3_wt
        bn0cv2_wt_dims = _factorize_tensor(bn_k3_wt)
        rt.fill(
            bn0_cv2_wt_fifo.prod(), W,
            TensorAccessPattern(
                (1, total_wt), offset=bn0cv2_wt_offset,
                sizes=list(bn0cv2_wt_dims),
                strides=[
                    bn0cv2_wt_dims[1] * bn0cv2_wt_dims[2] * bn0cv2_wt_dims[3],
                    bn0cv2_wt_dims[2] * bn0cv2_wt_dims[3],
                    bn0cv2_wt_dims[3], 1,
                ],
            ),
            task_group=tg_b,
        )

        # Drain bn0_out with strided write to concat[128:192ch]
        rt.drain(
            bn0_out_fifo.cons(), O,
            TensorAccessPattern(
                (1, output_buf_size),
                offset=concat_offset + cv1_oc * width,
                sizes=[1, height, hr_d1, hr_d0],
                strides=[0, cv2_in_row, hr_d0, 1],
            ),
            wait=True,
            task_group=tg_b,
        )

        rt.finish_task_group(tg_b)

        # ===== TG-C: cv2 reads assembled concat -> final output =====
        tg_c = rt.task_group()

        # Fill cv2 input (192ch) linearly from concat scratch
        cv2i_dims = _factorize_tensor(total_concat)
        rt.fill(
            cv2_in_fifo.prod(), O,
            TensorAccessPattern(
                (1, output_buf_size), offset=concat_offset,
                sizes=list(cv2i_dims),
                strides=[
                    cv2i_dims[1] * cv2i_dims[2] * cv2i_dims[3],
                    cv2i_dims[2] * cv2i_dims[3],
                    cv2i_dims[3], 1,
                ],
            ),
            task_group=tg_c,
        )

        # Fill cv2 weights
        cv2_wt_offset = cv1_total_wt + 2 * bn_k3_wt
        cv2w_dims = _factorize_tensor(cv2_wt_size)
        rt.fill(
            cv2_wt_fifo.prod(), W,
            TensorAccessPattern(
                (1, total_wt), offset=cv2_wt_offset,
                sizes=list(cv2w_dims),
                strides=[
                    cv2w_dims[1] * cv2w_dims[2] * cv2w_dims[3],
                    cv2w_dims[2] * cv2w_dims[3],
                    cv2w_dims[3], 1,
                ],
            ),
            task_group=tg_c,
        )

        # Drain cv2 output (128ch) to final output (offset 0)
        out_dims = _factorize_tensor(total_output)
        rt.drain(
            cv2_out_fifo.cons(), O,
            TensorAccessPattern(
                (1, output_buf_size), offset=0,
                sizes=list(out_dims),
                strides=[
                    out_dims[1] * out_dims[2] * out_dims[3],
                    out_dims[2] * out_dims[3],
                    out_dims[3], 1,
                ],
            ),
            wait=True,
            task_group=tg_c,
        )

        rt.finish_task_group(tg_c)

    return Program(dev_ty, rt).resolve_program(
        SequentialPlacer()
    )  # c2f_neck


def my_dataflow_c2f_l12(dev, height, width, cv1_s1, cv1_s2, bn_cv1_s1, bn_cv1_s2,
                         bn_cv2_s1, bn_cv2_s2, cv2_s1, cv2_s2):
    """L12 C2f: 384->128, bn_ch=64, 40x40."""
    return my_dataflow_c2f_neck(
        dev, height, width, 384, 128, 64, 128,
        cv1_s1, cv1_s2, bn_cv1_s1, bn_cv1_s2, bn_cv2_s1, bn_cv2_s2, cv2_s1, cv2_s2,
    )


# ---------------------------------------------------------------------------
# Neck C2f L21 dataflow block (all layers OC-streaming)
# ---------------------------------------------------------------------------


def my_dataflow_c2f_l21(
    dev,
    height,
    width,
    cv1_shift1,
    cv1_shift2,
    bn0_cv1_shift1,
    bn0_cv1_shift2,
    bn0_cv2_shift1,
    bn0_cv2_shift2,
    cv2_shift1,
    cv2_shift2,
):
    """C2f L21: 384->256, bn_ch=128, 20x20. All layers use OC streaming.

    Every sub-layer's weights exceed L1 (64KB), requiring OC streaming.
    This means bn0.cv1 and bn0.cv2 CANNOT be core-to-core chained (OC
    streaming re-reads the full input n_oc times per group). Each layer
    runs as a separate task group with DDR scratch between them.

    4 task groups, 4 workers (2 columns):
      TG-A: cv1 (384->256, k1 fused SiLU, oc_chunk=64, n_oc=4)
            -> concat[0:256ch]
      TG-B1: bn0.cv1 (128->128, k3s1 fused SiLU, oc_chunk=32, n_oc=4)
             reads half2(128ch) from concat[128:256ch]
             -> bn0_scratch
      TG-B2: bn0.cv2 (128->128, k3s1 fused SiLU, oc_chunk=32, n_oc=4)
             reads bn0_scratch -> concat[256:384ch]
      TG-C: cv2 (384->256, k1 fused SiLU, oc_chunk=64, n_oc=4)
            reads concat(384ch) -> final output
    """
    xfr_dtype = np.int8

    in_channels = 384
    cv1_oc = 256
    bn_ch = 128
    cv2_ic = cv1_oc + bn_ch  # 384
    cv2_oc = 256

    half_row = bn_ch * width

    # --- OC streaming params ---
    # cv1/cv2: k1, oc_chunk=64, n_oc=4
    cv1_oc_chunk = 64
    cv1_n_oc = cv1_oc // cv1_oc_chunk  # 4
    cv1_wt_chunk = cv1_oc_chunk * in_channels + cv1_oc_chunk * 4
    cv1_out_row = cv1_oc_chunk * width

    cv2_oc_chunk = 64
    cv2_n_oc = cv2_oc // cv2_oc_chunk  # 4
    cv2_wt_chunk = cv2_oc_chunk * cv2_ic + cv2_oc_chunk * 4
    cv2_out_row = cv2_oc_chunk * width
    cv2_in_row = cv2_ic * width

    # bn0: k3s1, oc_chunk=32, n_oc=4
    bn_oc_chunk, bn_n_oc, bn_depth = _compute_oc_streaming_params(
        bn_ch, bn_ch, width, 1
    )
    bn_wt_chunk = bn_oc_chunk * bn_ch * 9 + bn_oc_chunk * 4
    bn_out_row = bn_oc_chunk * width
    bn_in_row = bn_ch * width

    # --- Totals ---
    total_input = in_channels * height * width
    total_output = cv2_oc * height * width
    total_concat = cv2_ic * height * width
    bn_scratch_size = bn_ch * height * width

    # DDR output buffer: [final | concat | bn0_scratch]
    concat_offset = total_output
    bn_scratch_offset = total_output + total_concat
    output_buf_size = total_output + total_concat + bn_scratch_size

    # Weight layout: [cv1_wts | bn0cv1_wts | bn0cv2_wts | cv2_wts]
    cv1_total_wt = cv1_n_oc * cv1_wt_chunk
    bn_total_wt = bn_n_oc * bn_wt_chunk
    cv2_total_wt = cv2_n_oc * cv2_wt_chunk
    total_wt = cv1_total_wt + 2 * bn_total_wt + cv2_total_wt

    # --- L1 budget checks ---
    core_cv1_l1 = 1040 + 2 * in_channels * width + cv1_wt_chunk + 2 * cv1_out_row
    assert core_cv1_l1 <= 65536, f"cv1 L1: {core_cv1_l1}B"

    core_bn_l1 = (
        1040 + (bn_depth + 1) * bn_in_row + bn_wt_chunk + 2 * bn_out_row
    )
    assert core_bn_l1 <= 65536, f"bn L1: {core_bn_l1}B"

    core_cv2_l1 = 1040 + 2 * cv2_in_row + cv2_wt_chunk + 2 * cv2_out_row
    assert core_cv2_l1 <= 65536, f"cv2 L1: {core_cv2_l1}B"

    dev_ty = NPU2()

    # --- Types ---
    cv1_in_ty = np.ndarray[(in_channels * width,), np.dtype[xfr_dtype]]
    cv1_wt_ty = np.ndarray[(cv1_wt_chunk,), np.dtype[xfr_dtype]]
    cv1_out_ty = np.ndarray[(cv1_out_row,), np.dtype[xfr_dtype]]
    bn_in_ty = np.ndarray[(bn_in_row,), np.dtype[xfr_dtype]]
    bn_wt_ty = np.ndarray[(bn_wt_chunk,), np.dtype[xfr_dtype]]
    bn_out_ty = np.ndarray[(bn_out_row,), np.dtype[xfr_dtype]]
    cv2_in_ty = np.ndarray[(cv2_in_row,), np.dtype[xfr_dtype]]
    cv2_wt_ty = np.ndarray[(cv2_wt_chunk,), np.dtype[xfr_dtype]]
    cv2_out_ty = np.ndarray[(cv2_out_row,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(output_buf_size,), np.dtype[xfr_dtype]]

    # --- Kernels ---
    k1_cv1_kernel = Kernel(
        "conv2dk1_i8_silu", "conv2dk1_i8_silu.o",
        [cv1_in_ty, cv1_wt_ty, cv1_out_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32],
    )
    k3_bn_kernel = Kernel(
        "conv2dk3_i8_silu", "conv2dk3_i8_silu.o",
        [bn_in_ty, bn_in_ty, bn_in_ty, bn_wt_ty, bn_out_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32, np.int32],
    )
    k1_cv2_kernel = Kernel(
        "conv2dk1_i8_silu_cv2", "conv2dk1_i8_silu_cv2.o",
        [cv2_in_ty, cv2_wt_ty, cv2_out_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32],
    )

    # --- FIFOs (each layer independent — all go through DDR) ---
    cv1_in_fifo = ObjectFifo(cv1_in_ty, name="l21_cv1_in", depth=2)
    cv1_wt_fifo = ObjectFifo(cv1_wt_ty, name="l21_cv1_wt", depth=1)
    cv1_out_fifo = ObjectFifo(cv1_out_ty, name="l21_cv1_out", depth=2)

    bn_cv1_in_fifo = ObjectFifo(bn_in_ty, name="l21_bn_cv1_in", depth=bn_depth)
    bn_cv1_wt_fifo = ObjectFifo(bn_wt_ty, name="l21_bn_cv1_wt", depth=1)
    bn_cv1_out_fifo = ObjectFifo(bn_out_ty, name="l21_bn_cv1_out", depth=2)

    bn_cv2_in_fifo = ObjectFifo(bn_in_ty, name="l21_bn_cv2_in", depth=bn_depth)
    bn_cv2_wt_fifo = ObjectFifo(bn_wt_ty, name="l21_bn_cv2_wt", depth=1)
    bn_cv2_out_fifo = ObjectFifo(bn_out_ty, name="l21_bn_cv2_out", depth=2)

    cv2_in_fifo = ObjectFifo(cv2_in_ty, name="l21_cv2_in", depth=2)
    cv2_wt_fifo = ObjectFifo(cv2_wt_ty, name="l21_cv2_wt", depth=1)
    cv2_out_fifo = ObjectFifo(cv2_out_ty, name="l21_cv2_out", depth=2)

    # --- Core functions (closures capture integer params) ---

    def _make_k1_oc_fn(ci_val, co_val, n_oc_val, s1_val, s2_val):
        def core_fn(of_in, of_wt, of_out, kernel_fn):
            w = width
            ci = ci_val
            co = co_val
            s1 = s1_val
            s2 = s2_val
            for _ in range_(n_oc_val):
                wt = of_wt.acquire(1)
                for _ in range_(height):
                    ei = of_in.acquire(1)
                    eo = of_out.acquire(1)
                    kernel_fn(ei, wt, eo, w, ci, co, s1, s2)
                    of_in.release(1)
                    of_out.release(1)
                of_wt.release(1)
        return core_fn

    def _make_k3_oc_fn(ci_val, co_val, n_oc_val, s1_val, s2_val):
        def core_fn(of_in, of_wt, of_out, kernel_fn):
            w = width
            h = height
            ci = ci_val
            co = co_val
            s1 = s1_val
            s2 = s2_val
            for _ in range_(n_oc_val):
                elem_wt = of_wt.acquire(1)
                # top (check=0)
                elems = of_in.acquire(2)
                eo = of_out.acquire(1)
                kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo,
                          w, ci, co, 0, s1, s2)
                of_out.release(1)
                # middle (check=1)
                for _ in range_(h - 2):
                    elems = of_in.acquire(3)
                    eo = of_out.acquire(1)
                    kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo,
                              w, ci, co, 1, s1, s2)
                    of_in.release(1)
                    of_out.release(1)
                # bottom (check=2)
                elems = of_in.acquire(2)
                eo = of_out.acquire(1)
                kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo,
                          w, ci, co, 2, s1, s2)
                of_in.release(2)
                of_out.release(1)
                of_wt.release(1)
        return core_fn

    # --- Workers (2 columns) ---
    worker_cv1 = Worker(
        _make_k1_oc_fn(in_channels, cv1_oc_chunk, cv1_n_oc,
                        cv1_shift1, cv1_shift2),
        [cv1_in_fifo.cons(), cv1_wt_fifo.cons(), cv1_out_fifo.prod(),
         k1_cv1_kernel],
        placement=Tile(0, 2),
    )
    worker_bn_cv1 = Worker(
        _make_k3_oc_fn(bn_ch, bn_oc_chunk, bn_n_oc,
                        bn0_cv1_shift1, bn0_cv1_shift2),
        [bn_cv1_in_fifo.cons(bn_depth), bn_cv1_wt_fifo.cons(),
         bn_cv1_out_fifo.prod(), k3_bn_kernel],
        placement=Tile(0, 3),
    )
    worker_bn_cv2 = Worker(
        _make_k3_oc_fn(bn_ch, bn_oc_chunk, bn_n_oc,
                        bn0_cv2_shift1, bn0_cv2_shift2),
        [bn_cv2_in_fifo.cons(bn_depth), bn_cv2_wt_fifo.cons(),
         bn_cv2_out_fifo.prod(), k3_bn_kernel],
        placement=Tile(1, 2),
    )
    worker_cv2 = Worker(
        _make_k1_oc_fn(cv2_ic, cv2_oc_chunk, cv2_n_oc,
                        cv2_shift1, cv2_shift2),
        [cv2_in_fifo.cons(), cv2_wt_fifo.cons(), cv2_out_fifo.prod(),
         k1_cv2_kernel],
        placement=Tile(1, 3),
    )

    # --- Helper: factorize and create strided TAP ---
    def _oc_drain_tap(buf_size, offset, n_oc, oc_chunk_w, row_total, h):
        """Strided output TAP for OC interleaving."""
        pe_d0 = min(oc_chunk_w, 1023)
        while pe_d0 % 4 != 0:
            pe_d0 -= 1
        while pe_d0 >= 4:
            if oc_chunk_w % pe_d0 == 0:
                break
            pe_d0 -= 4
        pe_d1 = oc_chunk_w // pe_d0
        return TensorAccessPattern(
            (1, buf_size), offset=offset,
            sizes=[n_oc, h, pe_d1, pe_d0],
            strides=[oc_chunk_w, row_total, pe_d0, 1],
        )

    def _oc_fill_tap(buf_size, offset, n_oc, total_data):
        """Strided input TAP for OC re-streaming (stride-0)."""
        d2, d1, d0 = _factorize_3d(total_data)
        return TensorAccessPattern(
            (1, buf_size), offset=offset,
            sizes=[n_oc, d2, d1, d0],
            strides=[0, d1 * d0, d0, 1],
        )

    def _contiguous_tap(buf_size, offset, total_data):
        d3, d2, d1, d0 = _factorize_tensor(total_data)
        return TensorAccessPattern(
            (1, buf_size), offset=offset,
            sizes=[d3, d2, d1, d0],
            strides=[d2 * d1 * d0, d1 * d0, d0, 1],
        )

    # ===== Runtime sequence =====
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker_cv1, worker_bn_cv1, worker_bn_cv2, worker_cv2)

        # ===== TG-A: cv1 with OC streaming -> concat[0:256ch] =====
        tg_a = rt.task_group()
        rt.fill(cv1_in_fifo.prod(), I,
                _oc_fill_tap(total_input, 0, cv1_n_oc, total_input),
                task_group=tg_a)
        rt.fill(cv1_wt_fifo.prod(), W,
                _contiguous_tap(total_wt, 0, cv1_total_wt),
                task_group=tg_a)
        rt.drain(cv1_out_fifo.cons(), O,
                 _oc_drain_tap(output_buf_size, concat_offset,
                               cv1_n_oc, cv1_oc_chunk * width,
                               cv2_in_row, height),
                 wait=True, task_group=tg_a)
        rt.finish_task_group(tg_a)

        # ===== TG-B1: bn0.cv1 reads half2 from concat -> bn0_scratch =====
        tg_b1 = rt.task_group()

        # Read half2(128ch) from concat[128:256ch] — strided within 384ch rows
        half_d0 = min(half_row, 1023)
        while half_d0 % 4 != 0:
            half_d0 -= 1
        while half_d0 >= 4:
            if half_row % half_d0 == 0:
                break
            half_d0 -= 4
        half_d1 = half_row // half_d0

        rt.fill(bn_cv1_in_fifo.prod(), O,
                TensorAccessPattern(
                    (1, output_buf_size),
                    offset=concat_offset + half_row,
                    sizes=[bn_n_oc, height, half_d1, half_d0],
                    strides=[0, cv2_in_row, half_d0, 1],
                ),
                task_group=tg_b1)
        rt.fill(bn_cv1_wt_fifo.prod(), W,
                _contiguous_tap(total_wt, cv1_total_wt, bn_total_wt),
                task_group=tg_b1)

        # Drain to bn0_scratch with OC interleaving
        bn_full_row = bn_ch * width
        rt.drain(bn_cv1_out_fifo.cons(), O,
                 _oc_drain_tap(output_buf_size, bn_scratch_offset,
                               bn_n_oc, bn_oc_chunk * width,
                               bn_full_row, height),
                 wait=True, task_group=tg_b1)
        rt.finish_task_group(tg_b1)

        # ===== TG-B2: bn0.cv2 reads bn0_scratch -> concat[256:384ch] =====
        tg_b2 = rt.task_group()
        rt.fill(bn_cv2_in_fifo.prod(), O,
                _oc_fill_tap(output_buf_size, bn_scratch_offset,
                             bn_n_oc, bn_scratch_size),
                task_group=tg_b2)
        rt.fill(bn_cv2_wt_fifo.prod(), W,
                _contiguous_tap(total_wt, cv1_total_wt + bn_total_wt,
                                bn_total_wt),
                task_group=tg_b2)

        # Drain to concat[256:384ch] with strided write + OC interleave
        rt.drain(bn_cv2_out_fifo.cons(), O,
                 _oc_drain_tap(output_buf_size,
                               concat_offset + cv1_oc * width,
                               bn_n_oc, bn_oc_chunk * width,
                               cv2_in_row, height),
                 wait=True, task_group=tg_b2)
        rt.finish_task_group(tg_b2)

        # ===== TG-C: cv2 reads full concat -> final output =====
        tg_c = rt.task_group()
        cv2_total_input = cv2_ic * height * width
        rt.fill(cv2_in_fifo.prod(), O,
                _oc_fill_tap(output_buf_size, concat_offset,
                             cv2_n_oc, cv2_total_input),
                task_group=tg_c)
        rt.fill(cv2_wt_fifo.prod(), W,
                _contiguous_tap(total_wt,
                                cv1_total_wt + 2 * bn_total_wt,
                                cv2_total_wt),
                task_group=tg_c)
        rt.drain(cv2_out_fifo.cons(), O,
                 _oc_drain_tap(output_buf_size, 0,
                               cv2_n_oc, cv2_oc_chunk * width,
                               cv2_oc * width, height),
                 wait=True, task_group=tg_c)
        rt.finish_task_group(tg_c)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # c2f_l21


# ---------------------------------------------------------------------------
# Combined L16 CBS + L18 C2f (1 PDI)
# ---------------------------------------------------------------------------


def my_dataflow_l16_l18(
    dev,
    l16_height,
    l16_width,
    l16_shift1,
    l16_shift2,
    cv1_shift1,
    cv1_shift2,
    bn0_cv1_shift1,
    bn0_cv1_shift2,
    bn0_cv2_shift1,
    bn0_cv2_shift2,
    cv2_shift1,
    cv2_shift2,
):
    """Combined L16 CBS + L18 C2f in one PDI.

    I = L15 output (64ch, l16_height x l16_width)
    O = [L18_final(128ch,H18,W18) | concat(192ch,H18,W18)]
        Host pre-fills L12_skip(128ch) into concat[64:192ch] before execution.

    TG1: L16 k3s2 OC streaming (64->64, 80->40) -> concat[0:64ch]
    TG2: L18.cv1 (192->128, k1) -> concat2 area
    TG3: L18.bn0 (64->64 k3 x2, core-to-core) -> concat2 area
    TG4: L18.cv2 (192->128, k1) -> final output

    Workers (5 cores, 2 columns):
      L16:        Tile(0,2) - k3s2 OC streaming
      L18.cv1:    Tile(0,3) - k1 fused SiLU
      L18.bn0cv1: Tile(0,4) - k3 fused SiLU
      L18.bn0cv2: Tile(1,2) - k3 fused SiLU (sep column, shared mem)
      L18.cv2:    Tile(1,3) - k1 fused SiLU (renamed symbol)
    """
    xfr_dtype = np.int8

    # L16: 64->64, k3s2
    l16_ic = 64
    l16_oc = 64
    l16_oh = l16_height // 2
    l16_ow = l16_width // 2

    # L18: same spatial as L16 output
    l18_h = l16_oh
    l18_w = l16_ow
    l18_ic = 192  # L16_out(64) + L12_skip(128)
    l18_cv1_oc = 128
    l18_bn_ch = 64
    l18_cv2_ic = l18_cv1_oc + l18_bn_ch  # 192
    l18_cv2_oc = 128

    # --- L16 OC streaming params ---
    l16_oc_chunk, l16_n_oc, l16_depth = _compute_oc_streaming_params(
        l16_ic, l16_oc, l16_width, 2
    )
    l16_in_row = l16_ic * l16_width
    l16_wt_chunk = l16_oc_chunk * l16_ic * 9 + l16_oc_chunk * 4
    l16_out_row = l16_oc_chunk * l16_ow
    l16_total_input = l16_ic * l16_height * l16_width
    l16_total_wt = l16_n_oc * l16_wt_chunk

    # --- L18 params (no OC streaming for cv1/cv2, fits single group) ---
    l18_in_row = l18_ic * l18_w
    l18_half_row = l18_bn_ch * l18_w
    l18_cv2_in_row = l18_cv2_ic * l18_w
    l18_cv1_wt = l18_cv1_oc * l18_ic + l18_cv1_oc * 4
    l18_bn_wt = l18_bn_ch * l18_bn_ch * 9 + l18_bn_ch * 4
    l18_cv2_wt = l18_cv2_oc * l18_cv2_ic + l18_cv2_oc * 4
    l18_total_wt = l18_cv1_wt + 2 * l18_bn_wt + l18_cv2_wt
    bn_depth = 4

    # --- DDR buffer layout ---
    l18_total_output = l18_cv2_oc * l18_h * l18_w
    l18_total_concat = l18_cv2_ic * l18_h * l18_w
    concat_offset = l18_total_output
    output_buf_size = l18_total_output + l18_total_concat
    total_wt = l16_total_wt + l18_total_wt

    dev_ty = NPU2()

    # --- Types ---
    l16_in_ty = np.ndarray[(l16_in_row,), np.dtype[xfr_dtype]]
    l16_wt_ty = np.ndarray[(l16_wt_chunk,), np.dtype[xfr_dtype]]
    l16_out_ty = np.ndarray[(l16_out_row,), np.dtype[xfr_dtype]]

    l18_cv1_in_ty = np.ndarray[(l18_in_row,), np.dtype[xfr_dtype]]
    l18_cv1_wt_ty = np.ndarray[(l18_cv1_wt,), np.dtype[xfr_dtype]]
    l18_cv1_out_ty = np.ndarray[(l18_cv1_oc * l18_w,), np.dtype[xfr_dtype]]
    l18_half_ty = np.ndarray[(l18_half_row,), np.dtype[xfr_dtype]]
    l18_bn_wt_ty = np.ndarray[(l18_bn_wt,), np.dtype[xfr_dtype]]
    l18_cv2_in_ty = np.ndarray[(l18_cv2_in_row,), np.dtype[xfr_dtype]]
    l18_cv2_wt_ty = np.ndarray[(l18_cv2_wt,), np.dtype[xfr_dtype]]
    l18_cv2_out_ty = np.ndarray[(l18_cv2_oc * l18_w,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(l16_total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(output_buf_size,), np.dtype[xfr_dtype]]

    # --- Kernels ---
    k3s2_kernel = Kernel(
        "conv2dk3s2_i8_silu", "conv2dk3_i8_silu.o",
        [l16_in_ty, l16_in_ty, l16_in_ty, l16_wt_ty, l16_out_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32, np.int32],
    )
    k1_cv1_kernel = Kernel(
        "conv2dk1_i8_silu", "conv2dk1_i8_silu.o",
        [l18_cv1_in_ty, l18_cv1_wt_ty, l18_cv1_out_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32],
    )
    k3_bn_kernel = Kernel(
        "conv2dk3_i8_silu", "conv2dk3_i8_silu.o",
        [l18_half_ty, l18_half_ty, l18_half_ty, l18_bn_wt_ty, l18_half_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32, np.int32],
    )
    k1_cv2_kernel = Kernel(
        "conv2dk1_i8_silu_cv2", "conv2dk1_i8_silu_cv2.o",
        [l18_cv2_in_ty, l18_cv2_wt_ty, l18_cv2_out_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32],
    )

    # --- FIFOs ---
    l16_in_fifo = ObjectFifo(l16_in_ty, name="l16_in", depth=l16_depth)
    l16_wt_fifo = ObjectFifo(l16_wt_ty, name="l16_wt", depth=1)
    l16_out_fifo = ObjectFifo(l16_out_ty, name="l16_out", depth=2)

    cv1_in_fifo = ObjectFifo(l18_cv1_in_ty, name="l18_cv1_in", depth=2)
    cv1_wt_fifo = ObjectFifo(l18_cv1_wt_ty, name="l18_cv1_wt", depth=1)
    cv1_out_fifo = ObjectFifo(
        np.ndarray[(l18_cv1_oc * l18_w,), np.dtype[xfr_dtype]],
        name="l18_cv1_out", depth=2,
    )
    bn_in_fifo = ObjectFifo(l18_half_ty, name="l18_bn_in", depth=bn_depth)
    bn_cv1_wt_fifo = ObjectFifo(l18_bn_wt_ty, name="l18_bn_cv1_wt", depth=1)
    bn_cv2_wt_fifo = ObjectFifo(l18_bn_wt_ty, name="l18_bn_cv2_wt", depth=1)
    bn_inter = ObjectFifo(l18_half_ty, name="l18_bn_inter", depth=bn_depth)
    bn_out_fifo = ObjectFifo(l18_half_ty, name="l18_bn_out", depth=2)
    cv2_in_fifo = ObjectFifo(l18_cv2_in_ty, name="l18_cv2_in", depth=2)
    cv2_wt_fifo = ObjectFifo(l18_cv2_wt_ty, name="l18_cv2_wt", depth=1)
    cv2_out_fifo = ObjectFifo(l18_cv2_out_ty, name="l18_cv2_out", depth=2)

    # --- Core functions ---
    def _l16_core_fn(of_in, of_wt, of_out, kernel_fn):
        w = l16_width
        ci = l16_ic
        co = l16_oc_chunk
        oh = l16_oh
        s1 = l16_shift1
        s2 = l16_shift2
        for _ in range_(l16_n_oc):
            elem_wt = of_wt.acquire(1)
            elems = of_in.acquire(2)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo,
                      w, ci, co, 0, s1, s2)
            of_in.release(1)
            of_out.release(1)
            for _ in range_(oh - 1):
                elems = of_in.acquire(3)
                eo = of_out.acquire(1)
                kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo,
                          w, ci, co, 1, s1, s2)
                of_in.release(2)
                of_out.release(1)
            of_in.release(1)
            of_wt.release(1)

    def _cv1_core_fn(of_in, of_wt, of_out, kernel_fn):
        w = l18_w
        ci = l18_ic
        co = l18_cv1_oc
        s1 = cv1_shift1
        s2 = cv1_shift2
        elem_wt = of_wt.acquire(1)
        for _ in range_(l18_h):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, s1, s2)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    def _make_bn_fn(s1_val, s2_val):
        def core_fn(of_in, of_wt, of_out, kernel_fn):
            w = l18_w
            ci = l18_bn_ch
            co = l18_bn_ch
            h = l18_h
            s1 = s1_val
            s2 = s2_val
            elem_wt = of_wt.acquire(1)
            elems = of_in.acquire(2)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo,
                      w, ci, co, 0, s1, s2)
            of_out.release(1)
            for _ in range_(h - 2):
                elems = of_in.acquire(3)
                eo = of_out.acquire(1)
                kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo,
                          w, ci, co, 1, s1, s2)
                of_in.release(1)
                of_out.release(1)
            elems = of_in.acquire(2)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo,
                      w, ci, co, 2, s1, s2)
            of_in.release(2)
            of_out.release(1)
            of_wt.release(1)
        return core_fn

    def _cv2_core_fn(of_in, of_wt, of_out, kernel_fn):
        w = l18_w
        ci = l18_cv2_ic
        co = l18_cv2_oc
        s1 = cv2_shift1
        s2 = cv2_shift2
        elem_wt = of_wt.acquire(1)
        for _ in range_(l18_h):
            ei = of_in.acquire(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, elem_wt, eo, w, ci, co, s1, s2)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    # --- Workers (5 cores, 2 columns) ---
    worker_l16 = Worker(
        _l16_core_fn,
        [l16_in_fifo.cons(), l16_wt_fifo.cons(), l16_out_fifo.prod(), k3s2_kernel],
        placement=Tile(0, 2),
    )
    worker_cv1 = Worker(
        _cv1_core_fn,
        [cv1_in_fifo.cons(), cv1_wt_fifo.cons(), cv1_out_fifo.prod(), k1_cv1_kernel],
        placement=Tile(0, 3),
    )
    worker_bn_cv1 = Worker(
        _make_bn_fn(bn0_cv1_shift1, bn0_cv1_shift2),
        [bn_in_fifo.cons(bn_depth), bn_cv1_wt_fifo.cons(), bn_inter.prod(),
         k3_bn_kernel],
        placement=Tile(0, 4),
    )
    worker_bn_cv2 = Worker(
        _make_bn_fn(bn0_cv2_shift1, bn0_cv2_shift2),
        [bn_inter.cons(bn_depth), bn_cv2_wt_fifo.cons(), bn_out_fifo.prod(),
         k3_bn_kernel],
        placement=Tile(1, 2),
    )
    worker_cv2 = Worker(
        _cv2_core_fn,
        [cv2_in_fifo.cons(), cv2_wt_fifo.cons(), cv2_out_fifo.prod(), k1_cv2_kernel],
        placement=Tile(1, 3),
    )

    # --- L18 concat area dimensions ---
    l18_concat_row = l18_cv2_ic * l18_w  # 192 * W

    # ===== Runtime sequence =====
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker_l16, worker_cv1, worker_bn_cv1, worker_bn_cv2, worker_cv2)

        # ===== TG1: L16 k3s2 OC streaming -> concat[0:64ch] =====
        tg1 = rt.task_group()

        # Fill L16 input with stride-0 repeat
        l16_in_d2, l16_in_d1, l16_in_d0 = _factorize_3d(l16_total_input)
        rt.fill(l16_in_fifo.prod(), I,
                TensorAccessPattern(
                    (1, l16_total_input), offset=0,
                    sizes=[l16_n_oc, l16_in_d2, l16_in_d1, l16_in_d0],
                    strides=[0, l16_in_d1 * l16_in_d0, l16_in_d0, 1],
                ),
                task_group=tg1)

        # Fill L16 weights
        l16_wt_dims = _factorize_tensor(l16_total_wt)
        rt.fill(l16_wt_fifo.prod(), W,
                TensorAccessPattern(
                    (1, total_wt), offset=0,
                    sizes=list(l16_wt_dims),
                    strides=[l16_wt_dims[1] * l16_wt_dims[2] * l16_wt_dims[3],
                             l16_wt_dims[2] * l16_wt_dims[3],
                             l16_wt_dims[3], 1],
                ),
                task_group=tg1)

        # Drain L16 output to concat[0:64ch] with OC interleaving
        l16_full_out_row = l16_oc * l16_ow
        pe_d0 = min(l16_out_row, 1023)
        while pe_d0 % 4 != 0:
            pe_d0 -= 1
        while pe_d0 >= 4:
            if l16_out_row % pe_d0 == 0:
                break
            pe_d0 -= 4
        pe_d1 = l16_out_row // pe_d0
        rt.drain(l16_out_fifo.cons(), O,
                 TensorAccessPattern(
                     (1, output_buf_size), offset=concat_offset,
                     sizes=[l16_n_oc, l16_oh, pe_d1, pe_d0],
                     strides=[l16_oc_chunk * l16_ow, l18_concat_row, pe_d0, 1],
                 ),
                 wait=True, task_group=tg1)
        rt.finish_task_group(tg1)

        # After TG1: concat = [L16_out(64ch) | L12_skip(128ch)] (skip pre-filled)

        # ===== TG2: L18.cv1 reads concat -> cv1 concat2 =====
        # Reuse the same pattern as my_dataflow_c2f_neck TG-A (single group)
        tg2 = rt.task_group()

        cv1_in_dims = _factorize_tensor(l18_cv2_ic * l18_h * l18_w)
        rt.fill(cv1_in_fifo.prod(), O,
                TensorAccessPattern(
                    (1, output_buf_size), offset=concat_offset,
                    sizes=list(cv1_in_dims),
                    strides=[cv1_in_dims[1] * cv1_in_dims[2] * cv1_in_dims[3],
                             cv1_in_dims[2] * cv1_in_dims[3],
                             cv1_in_dims[3], 1],
                ),
                task_group=tg2)

        cv1_wt_dims = _factorize_tensor(l18_cv1_wt)
        rt.fill(cv1_wt_fifo.prod(), W,
                TensorAccessPattern(
                    (1, total_wt), offset=l16_total_wt,
                    sizes=list(cv1_wt_dims),
                    strides=[cv1_wt_dims[1] * cv1_wt_dims[2] * cv1_wt_dims[3],
                             cv1_wt_dims[2] * cv1_wt_dims[3],
                             cv1_wt_dims[3], 1],
                ),
                task_group=tg2)

        # Drain cv1 output to concat2 (reuse concat area for L18's internal concat)
        # L18 concat2 = [half1(64) | half2(64) | bn0_out(64)] = 192ch
        # cv1 produces 128ch, drain as contiguous into concat2[0:128ch]
        cv1_out_row_full = l18_cv1_oc * l18_w
        cv1_pe_d0 = min(cv1_out_row_full, 1023)
        while cv1_pe_d0 % 4 != 0:
            cv1_pe_d0 -= 1
        while cv1_pe_d0 >= 4:
            if cv1_out_row_full % cv1_pe_d0 == 0:
                break
            cv1_pe_d0 -= 4
        cv1_pe_d1 = cv1_out_row_full // cv1_pe_d0
        rt.drain(cv1_out_fifo.cons(), O,
                 TensorAccessPattern(
                     (1, output_buf_size), offset=concat_offset,
                     sizes=[1, l18_h, cv1_pe_d1, cv1_pe_d0],
                     strides=[0, l18_concat_row, cv1_pe_d0, 1],
                 ),
                 wait=True, task_group=tg2)
        rt.finish_task_group(tg2)

        # ===== TG3: L18.bn0 reads half2 -> bottleneck -> concat2[128:192] =====
        tg3 = rt.task_group()

        hr_d0 = min(l18_half_row, 1023)
        while hr_d0 % 4 != 0:
            hr_d0 -= 1
        while hr_d0 >= 4:
            if l18_half_row % hr_d0 == 0:
                break
            hr_d0 -= 4
        hr_d1 = l18_half_row // hr_d0

        rt.fill(bn_in_fifo.prod(), O,
                TensorAccessPattern(
                    (1, output_buf_size),
                    offset=concat_offset + l18_half_row,
                    sizes=[1, l18_h, hr_d1, hr_d0],
                    strides=[0, l18_concat_row, hr_d0, 1],
                ),
                task_group=tg3)

        # Fill bn0 weights separately
        bn_cv1_wt_dims = _factorize_tensor(l18_bn_wt)
        rt.fill(bn_cv1_wt_fifo.prod(), W,
                TensorAccessPattern(
                    (1, total_wt), offset=l16_total_wt + l18_cv1_wt,
                    sizes=list(bn_cv1_wt_dims),
                    strides=[bn_cv1_wt_dims[1] * bn_cv1_wt_dims[2] * bn_cv1_wt_dims[3],
                             bn_cv1_wt_dims[2] * bn_cv1_wt_dims[3],
                             bn_cv1_wt_dims[3], 1],
                ),
                task_group=tg3)
        rt.fill(bn_cv2_wt_fifo.prod(), W,
                TensorAccessPattern(
                    (1, total_wt), offset=l16_total_wt + l18_cv1_wt + l18_bn_wt,
                    sizes=list(bn_cv1_wt_dims),
                    strides=[bn_cv1_wt_dims[1] * bn_cv1_wt_dims[2] * bn_cv1_wt_dims[3],
                             bn_cv1_wt_dims[2] * bn_cv1_wt_dims[3],
                             bn_cv1_wt_dims[3], 1],
                ),
                task_group=tg3)

        rt.drain(bn_out_fifo.cons(), O,
                 TensorAccessPattern(
                     (1, output_buf_size),
                     offset=concat_offset + l18_cv1_oc * l18_w,
                     sizes=[1, l18_h, hr_d1, hr_d0],
                     strides=[0, l18_concat_row, hr_d0, 1],
                 ),
                 wait=True, task_group=tg3)
        rt.finish_task_group(tg3)

        # ===== TG4: L18.cv2 reads full concat2 -> final output =====
        tg4 = rt.task_group()

        cv2i_dims = _factorize_tensor(l18_cv2_ic * l18_h * l18_w)
        rt.fill(cv2_in_fifo.prod(), O,
                TensorAccessPattern(
                    (1, output_buf_size), offset=concat_offset,
                    sizes=list(cv2i_dims),
                    strides=[cv2i_dims[1] * cv2i_dims[2] * cv2i_dims[3],
                             cv2i_dims[2] * cv2i_dims[3],
                             cv2i_dims[3], 1],
                ),
                task_group=tg4)

        cv2_wt_dims = _factorize_tensor(l18_cv2_wt)
        rt.fill(cv2_wt_fifo.prod(), W,
                TensorAccessPattern(
                    (1, total_wt),
                    offset=l16_total_wt + l18_cv1_wt + 2 * l18_bn_wt,
                    sizes=list(cv2_wt_dims),
                    strides=[cv2_wt_dims[1] * cv2_wt_dims[2] * cv2_wt_dims[3],
                             cv2_wt_dims[2] * cv2_wt_dims[3],
                             cv2_wt_dims[3], 1],
                ),
                task_group=tg4)

        out_dims = _factorize_tensor(l18_total_output)
        rt.drain(cv2_out_fifo.cons(), O,
                 TensorAccessPattern(
                     (1, output_buf_size), offset=0,
                     sizes=list(out_dims),
                     strides=[out_dims[1] * out_dims[2] * out_dims[3],
                              out_dims[2] * out_dims[3],
                              out_dims[3], 1],
                 ),
                 wait=True, task_group=tg4)
        rt.finish_task_group(tg4)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # l16_l18


# ---------------------------------------------------------------------------
# Combined L19 CBS + L21 C2f (1 PDI)
# ---------------------------------------------------------------------------


def my_dataflow_l19_l21(
    dev,
    l19_height,
    l19_width,
    l19_shift1,
    l19_shift2,
    cv1_shift1,
    cv1_shift2,
    bn0_cv1_shift1,
    bn0_cv1_shift2,
    bn0_cv2_shift1,
    bn0_cv2_shift2,
    cv2_shift1,
    cv2_shift2,
):
    """Combined L19 CBS + L21 C2f in one PDI.

    I = L18 output (128ch, l19_height x l19_width)
    O = [L21_final(256ch,H21,W21) | concat(384ch,H21,W21) | bn0_scratch(128ch,H21,W21)]
        Host pre-fills P5(256ch) into concat[128:384ch] before execution.

    TG1: L19 k3s2 OC streaming (128->128, 40->20) -> concat[0:128ch]
    TG2: L21.cv1 (384->256, k1 OC) -> overwrite concat[0:256ch]
    TG3: L21.bn0.cv1 (128->128, k3 OC) -> bn0_scratch
    TG4: L21.bn0.cv2 (128->128, k3 OC) -> concat[256:384ch]
    TG5: L21.cv2 (384->256, k1 OC) -> final output

    5 workers, 2 columns. All layers use OC streaming.
    """
    xfr_dtype = np.int8

    # L19: 128->128, k3s2
    l19_ic = 128
    l19_oc = 128
    l19_oh = l19_height // 2
    l19_ow = l19_width // 2

    # L21: same spatial as L19 output
    l21_h = l19_oh
    l21_w = l19_ow
    l21_ic = 384  # L19_out(128) + P5(256)
    l21_cv1_oc = 256
    l21_bn_ch = 128
    l21_cv2_ic = l21_cv1_oc + l21_bn_ch  # 384
    l21_cv2_oc = 256

    # --- L19 OC streaming ---
    l19_oc_chunk, l19_n_oc, l19_depth = _compute_oc_streaming_params(
        l19_ic, l19_oc, l19_width, 2
    )
    l19_in_row = l19_ic * l19_width
    l19_wt_chunk = l19_oc_chunk * l19_ic * 9 + l19_oc_chunk * 4
    l19_out_row = l19_oc_chunk * l19_ow
    l19_total_input = l19_ic * l19_height * l19_width
    l19_total_wt = l19_n_oc * l19_wt_chunk

    # --- L21 OC streaming (all layers) ---
    cv1_oc_chunk = 64
    cv1_n_oc = l21_cv1_oc // cv1_oc_chunk
    cv1_wt_chunk = cv1_oc_chunk * l21_ic + cv1_oc_chunk * 4
    cv1_out_row = cv1_oc_chunk * l21_w

    bn_oc_chunk, bn_n_oc, bn_depth = _compute_oc_streaming_params(
        l21_bn_ch, l21_bn_ch, l21_w, 1
    )
    bn_wt_chunk = bn_oc_chunk * l21_bn_ch * 9 + bn_oc_chunk * 4
    bn_out_row = bn_oc_chunk * l21_w
    bn_in_row = l21_bn_ch * l21_w

    cv2_oc_chunk = 64
    cv2_n_oc = l21_cv2_oc // cv2_oc_chunk
    cv2_wt_chunk = cv2_oc_chunk * l21_cv2_ic + cv2_oc_chunk * 4
    cv2_out_row_size = cv2_oc_chunk * l21_w
    cv2_in_row = l21_cv2_ic * l21_w

    # --- Weight buffer ---
    cv1_total_wt = cv1_n_oc * cv1_wt_chunk
    bn_total_wt = bn_n_oc * bn_wt_chunk
    cv2_total_wt = cv2_n_oc * cv2_wt_chunk
    total_wt = l19_total_wt + cv1_total_wt + 2 * bn_total_wt + cv2_total_wt

    # --- DDR output buffer ---
    l21_total_output = l21_cv2_oc * l21_h * l21_w
    l21_total_concat = l21_cv2_ic * l21_h * l21_w
    bn_scratch_size = l21_bn_ch * l21_h * l21_w
    concat_offset = l21_total_output
    bn_scratch_offset = l21_total_output + l21_total_concat
    output_buf_size = l21_total_output + l21_total_concat + bn_scratch_size
    l21_concat_row = l21_cv2_ic * l21_w

    dev_ty = NPU2()

    # --- Types ---
    l19_in_ty = np.ndarray[(l19_in_row,), np.dtype[xfr_dtype]]
    l19_wt_ty = np.ndarray[(l19_wt_chunk,), np.dtype[xfr_dtype]]
    l19_out_ty = np.ndarray[(l19_out_row,), np.dtype[xfr_dtype]]

    cv1_in_ty = np.ndarray[(l21_ic * l21_w,), np.dtype[xfr_dtype]]
    cv1_wt_ty = np.ndarray[(cv1_wt_chunk,), np.dtype[xfr_dtype]]
    cv1_out_ty = np.ndarray[(cv1_out_row,), np.dtype[xfr_dtype]]
    bn_in_ty = np.ndarray[(bn_in_row,), np.dtype[xfr_dtype]]
    bn_wt_ty = np.ndarray[(bn_wt_chunk,), np.dtype[xfr_dtype]]
    bn_out_ty = np.ndarray[(bn_out_row,), np.dtype[xfr_dtype]]
    cv2_in_ty = np.ndarray[(cv2_in_row,), np.dtype[xfr_dtype]]
    cv2_wt_ty = np.ndarray[(cv2_wt_chunk,), np.dtype[xfr_dtype]]
    cv2_out_ty = np.ndarray[(cv2_out_row_size,), np.dtype[xfr_dtype]]

    input_l3_ty = np.ndarray[(l19_total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(output_buf_size,), np.dtype[xfr_dtype]]

    # --- Kernels ---
    k3s2_kernel = Kernel(
        "conv2dk3s2_i8_silu", "conv2dk3_i8_silu.o",
        [l19_in_ty, l19_in_ty, l19_in_ty, l19_wt_ty, l19_out_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32, np.int32],
    )
    k1_cv1_kernel = Kernel(
        "conv2dk1_i8_silu", "conv2dk1_i8_silu.o",
        [cv1_in_ty, cv1_wt_ty, cv1_out_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32],
    )
    k3_bn_kernel = Kernel(
        "conv2dk3_i8_silu", "conv2dk3_i8_silu.o",
        [bn_in_ty, bn_in_ty, bn_in_ty, bn_wt_ty, bn_out_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32, np.int32],
    )
    k1_cv2_kernel = Kernel(
        "conv2dk1_i8_silu_cv2", "conv2dk1_i8_silu_cv2.o",
        [cv2_in_ty, cv2_wt_ty, cv2_out_ty,
         np.int32, np.int32, np.int32, np.int32, np.int32],
    )

    # --- FIFOs ---
    l19_in_fifo = ObjectFifo(l19_in_ty, name="l19_in", depth=l19_depth)
    l19_wt_fifo = ObjectFifo(l19_wt_ty, name="l19_wt", depth=1)
    l19_out_fifo = ObjectFifo(l19_out_ty, name="l19_out", depth=2)

    cv1_in_fifo = ObjectFifo(cv1_in_ty, name="l21_cv1_in", depth=2)
    cv1_wt_fifo = ObjectFifo(cv1_wt_ty, name="l21_cv1_wt", depth=1)
    cv1_out_fifo = ObjectFifo(cv1_out_ty, name="l21_cv1_out", depth=2)

    bn_cv1_in_fifo = ObjectFifo(bn_in_ty, name="l21_bn_cv1_in", depth=bn_depth)
    bn_cv1_wt_fifo = ObjectFifo(bn_wt_ty, name="l21_bn_cv1_wt", depth=1)
    bn_cv1_out_fifo = ObjectFifo(bn_out_ty, name="l21_bn_cv1_out", depth=2)

    bn_cv2_in_fifo = ObjectFifo(bn_in_ty, name="l21_bn_cv2_in", depth=bn_depth)
    bn_cv2_wt_fifo = ObjectFifo(bn_wt_ty, name="l21_bn_cv2_wt", depth=1)
    bn_cv2_out_fifo = ObjectFifo(bn_out_ty, name="l21_bn_cv2_out", depth=2)

    cv2_in_fifo = ObjectFifo(cv2_in_ty, name="l21_cv2_in", depth=2)
    cv2_wt_fifo = ObjectFifo(cv2_wt_ty, name="l21_cv2_wt", depth=1)
    cv2_out_fifo = ObjectFifo(cv2_out_ty, name="l21_cv2_out", depth=2)

    # --- Core functions (closures) ---
    def _l19_core_fn(of_in, of_wt, of_out, kernel_fn):
        w = l19_width
        ci = l19_ic
        co = l19_oc_chunk
        oh = l19_oh
        s1 = l19_shift1
        s2 = l19_shift2
        for _ in range_(l19_n_oc):
            elem_wt = of_wt.acquire(1)
            elems = of_in.acquire(2)
            eo = of_out.acquire(1)
            kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo,
                      w, ci, co, 0, s1, s2)
            of_in.release(1)
            of_out.release(1)
            for _ in range_(oh - 1):
                elems = of_in.acquire(3)
                eo = of_out.acquire(1)
                kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo,
                          w, ci, co, 1, s1, s2)
                of_in.release(2)
                of_out.release(1)
            of_in.release(1)
            of_wt.release(1)

    def _make_k1_oc(ci_val, co_val, n_oc_val, s1_val, s2_val):
        def core_fn(of_in, of_wt, of_out, kernel_fn):
            w = l21_w
            for _ in range_(n_oc_val):
                wt = of_wt.acquire(1)
                for _ in range_(l21_h):
                    ei = of_in.acquire(1)
                    eo = of_out.acquire(1)
                    kernel_fn(ei, wt, eo, w, ci_val, co_val, s1_val, s2_val)
                    of_in.release(1)
                    of_out.release(1)
                of_wt.release(1)
        return core_fn

    def _make_k3_oc(ci_val, co_val, n_oc_val, s1_val, s2_val):
        def core_fn(of_in, of_wt, of_out, kernel_fn):
            w = l21_w
            h = l21_h
            for _ in range_(n_oc_val):
                elem_wt = of_wt.acquire(1)
                elems = of_in.acquire(2)
                eo = of_out.acquire(1)
                kernel_fn(elems[0], elems[0], elems[1], elem_wt, eo,
                          w, ci_val, co_val, 0, s1_val, s2_val)
                of_out.release(1)
                for _ in range_(h - 2):
                    elems = of_in.acquire(3)
                    eo = of_out.acquire(1)
                    kernel_fn(elems[0], elems[1], elems[2], elem_wt, eo,
                              w, ci_val, co_val, 1, s1_val, s2_val)
                    of_in.release(1)
                    of_out.release(1)
                elems = of_in.acquire(2)
                eo = of_out.acquire(1)
                kernel_fn(elems[0], elems[1], elems[1], elem_wt, eo,
                          w, ci_val, co_val, 2, s1_val, s2_val)
                of_in.release(2)
                of_out.release(1)
                of_wt.release(1)
        return core_fn

    # --- Workers (5 cores, 2 columns) ---
    worker_l19 = Worker(
        _l19_core_fn,
        [l19_in_fifo.cons(), l19_wt_fifo.cons(), l19_out_fifo.prod(), k3s2_kernel],
        placement=Tile(0, 2),
    )
    worker_cv1 = Worker(
        _make_k1_oc(l21_ic, cv1_oc_chunk, cv1_n_oc, cv1_shift1, cv1_shift2),
        [cv1_in_fifo.cons(), cv1_wt_fifo.cons(), cv1_out_fifo.prod(), k1_cv1_kernel],
        placement=Tile(0, 3),
    )
    worker_bn_cv1 = Worker(
        _make_k3_oc(l21_bn_ch, bn_oc_chunk, bn_n_oc,
                     bn0_cv1_shift1, bn0_cv1_shift2),
        [bn_cv1_in_fifo.cons(bn_depth), bn_cv1_wt_fifo.cons(),
         bn_cv1_out_fifo.prod(), k3_bn_kernel],
        placement=Tile(0, 4),
    )
    worker_bn_cv2 = Worker(
        _make_k3_oc(l21_bn_ch, bn_oc_chunk, bn_n_oc,
                     bn0_cv2_shift1, bn0_cv2_shift2),
        [bn_cv2_in_fifo.cons(bn_depth), bn_cv2_wt_fifo.cons(),
         bn_cv2_out_fifo.prod(), k3_bn_kernel],
        placement=Tile(1, 2),
    )
    worker_cv2 = Worker(
        _make_k1_oc(l21_cv2_ic, cv2_oc_chunk, cv2_n_oc, cv2_shift1, cv2_shift2),
        [cv2_in_fifo.cons(), cv2_wt_fifo.cons(), cv2_out_fifo.prod(), k1_cv2_kernel],
        placement=Tile(1, 3),
    )

    # --- Helpers ---
    def _oc_drain(buf_sz, off, n, chunk_w, row_total, h):
        pd0 = min(chunk_w, 1023)
        while pd0 % 4 != 0:
            pd0 -= 1
        while pd0 >= 4:
            if chunk_w % pd0 == 0:
                break
            pd0 -= 4
        pd1 = chunk_w // pd0
        return TensorAccessPattern(
            (1, buf_sz), offset=off,
            sizes=[n, h, pd1, pd0], strides=[chunk_w, row_total, pd0, 1],
        )

    def _oc_fill(buf_sz, off, n, total_data):
        d2, d1, d0 = _factorize_3d(total_data)
        return TensorAccessPattern(
            (1, buf_sz), offset=off,
            sizes=[n, d2, d1, d0], strides=[0, d1 * d0, d0, 1],
        )

    def _cont(buf_sz, off, total_data):
        d3, d2, d1, d0 = _factorize_tensor(total_data)
        return TensorAccessPattern(
            (1, buf_sz), offset=off,
            sizes=[d3, d2, d1, d0], strides=[d2 * d1 * d0, d1 * d0, d0, 1],
        )

    # ===== Runtime sequence =====
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker_l19, worker_cv1, worker_bn_cv1, worker_bn_cv2, worker_cv2)

        # TG1: L19 k3s2 OC streaming -> concat[0:128ch]
        tg1 = rt.task_group()
        rt.fill(l19_in_fifo.prod(), I,
                _oc_fill(l19_total_input, 0, l19_n_oc, l19_total_input),
                task_group=tg1)
        rt.fill(l19_wt_fifo.prod(), W,
                _cont(total_wt, 0, l19_total_wt), task_group=tg1)
        l19_full_row = l19_oc * l19_ow
        rt.drain(l19_out_fifo.cons(), O,
                 _oc_drain(output_buf_size, concat_offset,
                           l19_n_oc, l19_oc_chunk * l19_ow,
                           l21_concat_row, l19_oh),
                 wait=True, task_group=tg1)
        rt.finish_task_group(tg1)

        # TG2: L21.cv1 reads concat(384ch) -> overwrite concat[0:256ch]
        tg2 = rt.task_group()
        cv1_total_data = l21_ic * l21_h * l21_w
        rt.fill(cv1_in_fifo.prod(), O,
                _oc_fill(output_buf_size, concat_offset, cv1_n_oc, cv1_total_data),
                task_group=tg2)
        rt.fill(cv1_wt_fifo.prod(), W,
                _cont(total_wt, l19_total_wt, cv1_total_wt), task_group=tg2)
        rt.drain(cv1_out_fifo.cons(), O,
                 _oc_drain(output_buf_size, concat_offset,
                           cv1_n_oc, cv1_oc_chunk * l21_w,
                           l21_concat_row, l21_h),
                 wait=True, task_group=tg2)
        rt.finish_task_group(tg2)

        # TG3: L21.bn0.cv1 reads half2 from concat[128:256ch] -> bn0_scratch
        tg3 = rt.task_group()
        half_row = l21_bn_ch * l21_w
        hd0 = min(half_row, 1023)
        while hd0 % 4 != 0:
            hd0 -= 1
        while hd0 >= 4:
            if half_row % hd0 == 0:
                break
            hd0 -= 4
        hd1 = half_row // hd0
        rt.fill(bn_cv1_in_fifo.prod(), O,
                TensorAccessPattern(
                    (1, output_buf_size),
                    offset=concat_offset + half_row,
                    sizes=[bn_n_oc, l21_h, hd1, hd0],
                    strides=[0, l21_concat_row, hd0, 1],
                ),
                task_group=tg3)
        rt.fill(bn_cv1_wt_fifo.prod(), W,
                _cont(total_wt, l19_total_wt + cv1_total_wt, bn_total_wt),
                task_group=tg3)
        bn_full_row = l21_bn_ch * l21_w
        rt.drain(bn_cv1_out_fifo.cons(), O,
                 _oc_drain(output_buf_size, bn_scratch_offset,
                           bn_n_oc, bn_oc_chunk * l21_w,
                           bn_full_row, l21_h),
                 wait=True, task_group=tg3)
        rt.finish_task_group(tg3)

        # TG4: L21.bn0.cv2 reads bn0_scratch -> concat[256:384ch]
        tg4 = rt.task_group()
        rt.fill(bn_cv2_in_fifo.prod(), O,
                _oc_fill(output_buf_size, bn_scratch_offset,
                         bn_n_oc, bn_scratch_size),
                task_group=tg4)
        rt.fill(bn_cv2_wt_fifo.prod(), W,
                _cont(total_wt, l19_total_wt + cv1_total_wt + bn_total_wt,
                      bn_total_wt),
                task_group=tg4)
        rt.drain(bn_cv2_out_fifo.cons(), O,
                 _oc_drain(output_buf_size, concat_offset + l21_cv1_oc * l21_w,
                           bn_n_oc, bn_oc_chunk * l21_w,
                           l21_concat_row, l21_h),
                 wait=True, task_group=tg4)
        rt.finish_task_group(tg4)

        # TG5: L21.cv2 reads full concat -> final output
        tg5 = rt.task_group()
        cv2_total_data = l21_cv2_ic * l21_h * l21_w
        rt.fill(cv2_in_fifo.prod(), O,
                _oc_fill(output_buf_size, concat_offset, cv2_n_oc, cv2_total_data),
                task_group=tg5)
        rt.fill(cv2_wt_fifo.prod(), W,
                _cont(total_wt,
                      l19_total_wt + cv1_total_wt + 2 * bn_total_wt,
                      cv2_total_wt),
                task_group=tg5)
        rt.drain(cv2_out_fifo.cons(), O,
                 _oc_drain(output_buf_size, 0,
                           cv2_n_oc, cv2_oc_chunk * l21_w,
                           l21_cv2_oc * l21_w, l21_h),
                 wait=True, task_group=tg5)
        rt.finish_task_group(tg5)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())  # l19_l21


# ---------------------------------------------------------------------------
# Standalone upsample 2× dataflow design
# ---------------------------------------------------------------------------


def my_dataflow_upsample2x(dev, height, width, channels):
    """Nearest-neighbor 2× spatial upsample on NPU.

    One core reads input rows (IC×W), duplicates pixels (width 2×) via
    upsample2x_row_i8 kernel, and writes each upsampled row twice (height 2×).

    Input:  IC × H × W
    Output: IC × 2H × 2W
    """
    xfr_dtype = np.int8

    in_row = channels * width
    out_row = channels * (width * 2)
    total_input = channels * height * width
    total_output = channels * (height * 2) * (width * 2)

    dev_ty = NPU2()

    in_ty = np.ndarray[(in_row,), np.dtype[xfr_dtype]]
    out_ty = np.ndarray[(out_row,), np.dtype[xfr_dtype]]
    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    kernel = Kernel(
        "upsample2x_row_i8",
        "upsample2x_i8.o",
        [in_ty, out_ty, np.int32, np.int32],
    )

    in_fifo = ObjectFifo(in_ty, name="ups_in", depth=2)
    out_fifo = ObjectFifo(out_ty, name="ups_out", depth=2)

    def core_fn(of_in, of_out, kernel_fn):
        w = width
        ic = channels
        for _ in range_(height):
            ei = of_in.acquire(1)
            # Produce 2 identical upsampled rows (height doubling)
            eo = of_out.acquire(1)
            kernel_fn(ei, eo, w, ic)
            of_out.release(1)
            eo = of_out.acquire(1)
            kernel_fn(ei, eo, w, ic)
            of_out.release(1)
            of_in.release(1)

    worker = Worker(
        core_fn,
        [in_fifo.cons(), out_fifo.prod(), kernel],
        placement=Tile(0, 2),
    )

    rt = Runtime()
    with rt.sequence(input_l3_ty, input_l3_ty, output_l3_ty) as (I, _W, O):
        rt.start(worker)
        tg = rt.task_group()

        in_dims = _factorize_tensor(total_input)
        rt.fill(
            in_fifo.prod(), I,
            TensorAccessPattern(
                (1, total_input), offset=0,
                sizes=list(in_dims),
                strides=[in_dims[1] * in_dims[2] * in_dims[3],
                         in_dims[2] * in_dims[3], in_dims[3], 1],
            ),
            task_group=tg,
        )

        out_dims = _factorize_tensor(total_output)
        rt.drain(
            out_fifo.cons(), O,
            TensorAccessPattern(
                (1, total_output), offset=0,
                sizes=list(out_dims),
                strides=[out_dims[1] * out_dims[2] * out_dims[3],
                         out_dims[2] * out_dims[3], out_dims[3], 1],
            ),
            wait=True, task_group=tg,
        )

        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())
