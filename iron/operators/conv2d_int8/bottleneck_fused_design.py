# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Fused bottleneck design: two chained 3x3 conv+SiLU via inter-core ObjectFIFO.

Pipeline:
  Input(DDR) -> Core0(k3_silu) -> inter-core ObjectFIFO -> Core1(k3_silu) -> Output(DDR)
  Weights delivered via MemTile split (single DDR transfer, split into wt1/wt2).

Eliminates one DDR round-trip compared to running two separate conv layers.

DMA channel budget:
  ShimDMA: 2 out (input + weights), 1 in (output)
  MemTile: 1 in (weights), 2 out (wt1 + wt2)
  Core0:   2 in (input + wt1), 1 out (inter)
  Core1:   2 in (inter + wt2), 1 out (output)

Limitations:
  - Both convs must fit without OC streaming (all weights in L1)
  - stride=1 only (same spatial dims in/out)
  - IC = OC = channels (symmetric bottleneck)
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


def bottleneck_l1_feasible(channels, width):
    """Check if a bottleneck config fits in L1 without OC streaming.

    Each core needs: sliding_window(5*C*W) + weights(C*C*9+C*4) + output(2*C*W) + stack(1040)
    The inter-core FIFO adds 4*C*W to one core's L1 (shared memory, worst case).

    Returns (feasible, core0_bytes, core1_bytes, details_str).
    """
    C = channels
    W = width
    wt_size = C * C * 9 + C * 4  # fused k3 weights + packed bias

    # Core0: input sliding window + weights + inter producer
    # Worst case: inter FIFO buffers (4*C*W) allocated in Core0
    core0_worst = 5 * C * W + wt_size + 4 * C * W + 1040
    # Core1: inter consumer + weights + output
    # Worst case: inter FIFO buffers (4*C*W) allocated in Core1
    core1_worst = 4 * C * W + wt_size + 2 * C * W + 1040

    # Check if either placement of inter buffers works
    # Scenario A: inter in Core0
    core0_a = 5 * C * W + wt_size + 4 * C * W + 1040
    core1_a = wt_size + 2 * C * W + 1040
    feasible_a = core0_a <= 65536 and core1_a <= 65536

    # Scenario B: inter in Core1
    core0_b = 5 * C * W + wt_size + 1040
    core1_b = 4 * C * W + wt_size + 2 * C * W + 1040
    feasible_b = core0_b <= 65536 and core1_b <= 65536

    feasible = feasible_a or feasible_b

    if feasible_a:
        details = (
            f"Inter in Core0: Core0={core0_a}B ({core0_a*100//65536}%), "
            f"Core1={core1_a}B ({core1_a*100//65536}%)"
        )
        return (True, core0_a, core1_a, details)
    elif feasible_b:
        details = (
            f"Inter in Core1: Core0={core0_b}B ({core0_b*100//65536}%), "
            f"Core1={core1_b}B ({core1_b*100//65536}%)"
        )
        return (True, core0_b, core1_b, details)
    else:
        details = (
            f"INFEASIBLE: worst Core0={core0_worst}B, Core1={core1_worst}B "
            f"(need OC streaming)"
        )
        return (False, core0_worst, core1_worst, details)


def my_bottleneck_fused(
    dev,
    height,
    width,
    channels,
    shift1_a,
    shift2_a,
    shift1_b,
    shift2_b,
):
    """Fused bottleneck: two chained 3x3 conv+SiLU via inter-core ObjectFIFO.

    Both convs are channels->channels, stride=1, padding=1.
    Weights split at MemTile from a single DDR transfer.
    Inter-core data flows directly between adjacent compute tiles.

    Args:
        dev: Device type string ("npu" or "npu2").
        height: Spatial height of input/output.
        width: Spatial width of input/output.
        channels: Channel count (same for both convs).
        shift1_a: Conv1 dequantization shift.
        shift2_a: Conv1 requantization shift.
        shift1_b: Conv2 dequantization shift.
        shift2_b: Conv2 requantization shift.
    """
    xfr_dtype = np.int8
    C = channels
    H = height
    W = width

    assert C % 8 == 0, f"channels ({C}) must be a multiple of 8"
    assert H >= 2, f"height ({H}) must be >= 2 for 3x3 conv"

    # Row and weight sizes
    row_size = C * W
    k_elems = 9  # 3x3
    wt_size = C * C * k_elems + C * 4  # per-conv: tiled weights + packed int32 bias
    total_wt_size = 2 * wt_size

    # Total tensor sizes
    total_input = C * H * W
    total_output = C * H * W  # stride=1, same spatial dims

    # L1 budget check
    feasible, _, _, details = bottleneck_l1_feasible(C, W)
    if not feasible:
        raise ValueError(
            f"Bottleneck fused infeasible for C={C}, W={W}: {details}. "
            f"Weight size per conv = {wt_size}B. "
            f"Requires OC streaming (not implemented in fused design)."
        )

    # FIFO depths
    input_depth = 4  # sliding window for k3 (acquire up to 3)
    inter_depth = 4  # sliding window for k3 on consumer side
    output_depth = 2  # double-buffering

    dev_ty = NPU2()

    # ObjectFIFO element types
    row_ty = np.ndarray[(row_size,), np.dtype[xfr_dtype]]
    wt_ty = np.ndarray[(wt_size,), np.dtype[xfr_dtype]]
    wts_all_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]

    # L3 (DDR) tensor types
    input_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wts_l3_ty = np.ndarray[(total_wt_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    # Kernel (shared by both workers — same function, same types)
    kernel = Kernel(
        "conv2dk3_i8_silu",
        "conv2dk3_i8_silu.o",
        [
            row_ty,  # row0
            row_ty,  # row1
            row_ty,  # row2
            wt_ty,  # weights + bias
            row_ty,  # output
            np.int32,  # x_dim (width)
            np.int32,  # ci (input channels)
            np.int32,  # co (output channels)
            np.int32,  # check (0=top, 1=middle, 2=bottom)
            np.int32,  # shift1
            np.int32,  # shift2
        ],
    )

    # --- ObjectFIFOs ---

    # Input: DDR -> Core0
    in_fifo = ObjectFifo(row_ty, name="in_act", depth=input_depth)

    # Weights: DDR -> MemTile -> split -> Core0 + Core1
    wts_all_fifo = ObjectFifo(wts_all_ty, name="wts_all", depth=1)
    wt1_fifo, wt2_fifo = wts_all_fifo.cons().split(
        offsets=[0, wt_size],
        obj_types=[wt_ty, wt_ty],
        names=["wt_conv1", "wt_conv2"],
        depths=[1, 1],
        placement=Tile(0, 1),  # MemTile
    )

    # Inter-core: Core0 -> Core1 (direct between adjacent tiles)
    inter_fifo = ObjectFifo(row_ty, name="inter_act", depth=inter_depth)

    # Output: Core1 -> DDR
    out_fifo = ObjectFifo(row_ty, name="out_act", depth=output_depth)

    # --- Core functions ---

    # Conv1: sliding window on input, produce inter rows
    def core_fn_conv1(of_in, of_wt, of_inter, kernel_fn):
        y_dim = H
        x_dim = W
        ci = C
        co = C
        s1 = shift1_a
        s2 = shift2_a

        elem_wt = of_wt.acquire(1)

        # Top row: check=0 (pad top with row0)
        elems = of_in.acquire(2)
        elem_out = of_inter.acquire(1)
        kernel_fn(
            elems[0], elems[0], elems[1], elem_wt, elem_out, x_dim, ci, co, 0, s1, s2
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
                s1,
                s2,
            )
            of_in.release(1)
            of_inter.release(1)

        # Bottom row: check=2 (pad bottom with last row)
        elems = of_in.acquire(2)
        elem_out = of_inter.acquire(1)
        kernel_fn(
            elems[0], elems[1], elems[1], elem_wt, elem_out, x_dim, ci, co, 2, s1, s2
        )
        of_in.release(2)
        of_inter.release(1)

        of_wt.release(1)

    # Conv2: sliding window on inter, produce output rows
    def core_fn_conv2(of_inter, of_wt, of_out, kernel_fn):
        y_dim = H
        x_dim = W
        ci = C
        co = C
        s1 = shift1_b
        s2 = shift2_b

        elem_wt = of_wt.acquire(1)

        # Top row: check=0
        elems = of_inter.acquire(2)
        elem_out = of_out.acquire(1)
        kernel_fn(
            elems[0], elems[0], elems[1], elem_wt, elem_out, x_dim, ci, co, 0, s1, s2
        )
        of_out.release(1)

        # Middle rows: check=1
        for _ in range_(y_dim - 2):
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
            of_inter.release(1)
            of_out.release(1)

        # Bottom row: check=2
        elems = of_inter.acquire(2)
        elem_out = of_out.acquire(1)
        kernel_fn(
            elems[0], elems[1], elems[1], elem_wt, elem_out, x_dim, ci, co, 2, s1, s2
        )
        of_inter.release(2)
        of_out.release(1)

        of_wt.release(1)

    # --- Workers ---
    worker0 = Worker(
        core_fn_conv1,
        [in_fifo.cons(), wt1_fifo.cons(), inter_fifo.prod(), kernel],
        placement=Tile(0, 2),
    )
    worker1 = Worker(
        core_fn_conv2,
        [inter_fifo.cons(inter_depth), wt2_fifo.cons(), out_fifo.prod(), kernel],
        placement=Tile(0, 3),
    )

    # --- Runtime sequence ---
    rt = Runtime()
    with rt.sequence(input_l3_ty, wts_l3_ty, output_l3_ty) as (I, W_buf, O):
        rt.start(worker0, worker1)

        tg = rt.task_group()

        # Fill input from DDR
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

        # Fill all weights from DDR (MemTile will split)
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

        # Drain output to DDR
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


# --- L1 Feasibility Analysis for YOLOv8n Bottleneck Configs ---


def print_feasibility_report():
    """Print L1 feasibility for all YOLOv8n bottleneck configurations."""
    configs = [
        ("L2 (backbone)", 32, 160),
        ("L4 (backbone)", 64, 80),
        ("L6 (backbone)", 128, 40),
        ("L8 (backbone)", 256, 20),
        ("L12 (neck)", 64, 40),
        ("L15 (neck)", 32, 80),
        ("L18 (neck)", 64, 40),
        ("L21 (neck)", 128, 20),
    ]

    print("=" * 80)
    print("YOLOv8n Bottleneck Fused Chaining: L1 Feasibility Analysis")
    print("=" * 80)
    print(
        f"{'Layer':<16} {'C':>4} {'W':>4} {'Wt/conv':>8} {'Feasible':>9} {'Details'}"
    )
    print("-" * 80)

    feasible_count = 0
    for name, C, W in configs:
        wt_size = C * C * 9 + C * 4
        ok, c0, c1, details = bottleneck_l1_feasible(C, W)
        status = "YES" if ok else "NO"
        if ok:
            feasible_count += 1
        print(f"{name:<16} {C:>4} {W:>4} {wt_size:>7}B {status:>9}  {details}")

    print("-" * 80)
    print(
        f"Feasible: {feasible_count}/{len(configs)} bottleneck configs "
        f"can use core-to-core chaining"
    )
    print()
    print("Note: infeasible configs need OC streaming, which breaks direct")
    print("core-to-core chaining because Conv2 needs all IC channels at once.")
    print("Possible solutions: MemTile accumulation or weight tiling.")


if __name__ == "__main__":
    import sys

    if "--report" in sys.argv:
        print_feasibility_report()
    else:
        # Generate MLIR for a small test config
        C = 8
        H = W = 8
        print(f"Generating MLIR for bottleneck C={C}, H={H}, W={W}...")
        module = my_bottleneck_fused("npu2", H, W, C, 10, 7, 10, 7)
        print(module)
