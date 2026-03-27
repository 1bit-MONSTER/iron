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


def my_conv2d_int8(
    dev,
    height,
    width,
    in_channels,
    out_channels,
    scale,
    kernel_obj="conv2dk1_i8.o",
):
    """ObjectFIFO design for 1x1 int8 conv2d on NPU2.

    Data layout (tiled, groups of 8 channels):
      Input row:   [C_in/8, W, 8]   (int8)
      Weights:     [C_out/8, C_in/8, 8, 8]  (int8)
      Output row:  [C_out/8, W, 8]  (int8)

    Supports OC streaming when weights don't fit in L1: splits output
    channels into chunks, re-streams input for each chunk.
    """
    xfr_dtype = np.int8
    _BD_WRAP_MAX = 64

    assert in_channels % 8 == 0, "in_channels must be a multiple of 8"
    assert out_channels % 8 == 0, "out_channels must be a multiple of 8"

    # Sizes for one row of data
    input_row_size = in_channels * width

    # Total tensor sizes
    total_input_size = in_channels * height * width
    total_output_size = out_channels * height * width

    # --- L1 budget: find oc_chunk that fits ---
    # input_fifo: 2 * input_row_size (depth=2, ping-pong)
    # weight_fifo: 1 * oc_chunk * in_channels
    # output_fifo: 2 * oc_chunk * width
    # overhead: 1040 bytes (stack + misc)
    n_oc_groups = 1
    oc_chunk = out_channels
    input_bufs = 2 * input_row_size
    avail = 65536 - 1040 - input_bufs

    if avail <= 0:
        raise ValueError(
            f"k1 int8 conv2d infeasible: input row too large "
            f"(IC={in_channels}, W={width})"
        )

    wt_bytes = out_channels * in_channels
    out_bytes = 2 * out_channels * width
    if wt_bytes + out_bytes > avail:
        # Need OC streaming — find largest oc_chunk that fits
        found = False
        for try_oc in range(out_channels, 0, -8):
            if out_channels % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_b = try_oc * in_channels
            out_b = 2 * try_oc * width
            if wt_b + out_b > avail:
                continue
            n_oc = out_channels // try_oc
            if n_oc > _BD_WRAP_MAX:
                continue
            oc_chunk = try_oc
            n_oc_groups = n_oc
            found = True
            break
        if not found:
            raise ValueError(
                f"k1 int8 conv2d infeasible: "
                f"IC={in_channels}, OC={out_channels}, W={width}. "
                f"Cannot satisfy L1 budget (64KB)."
            )

    wt_chunk_size = oc_chunk * in_channels
    output_row_size = oc_chunk * width

    if dev == "npu":
        dev_ty = NPU1()
    else:
        dev_ty = NPU2()

    # Type definitions for ObjectFIFOs
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_row_size,), np.dtype[xfr_dtype]]
    weights_ty = np.ndarray[(wt_chunk_size,), np.dtype[xfr_dtype]]

    # L3 (DDR) tensor types for runtime sequence
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    weights_l3_ty = np.ndarray[(n_oc_groups * wt_chunk_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

    # Kernel declaration
    conv2dk1_i8_kernel = Kernel(
        "conv2dk1_i8",
        kernel_obj,
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

    # ObjectFIFOs with MemTile forwarding for input and output
    in_l3_fifo = ObjectFifo(input_row_ty, name="in_l3", depth=2)
    in_fifo = in_l3_fifo.cons().forward(obj_type=input_row_ty, name="in_l1")

    wt_fifo = ObjectFifo(weights_ty, name="wt_fifo", depth=1)

    out_fifo = ObjectFifo(output_row_ty, name="out_l1", depth=2)
    out_l3_fifo = out_fifo.cons().forward(obj_type=output_row_ty, name="out_l3")

    # Core function
    def core_fn(of_in, of_wt, of_out, kernel_fn):
        y_dim = height
        x_dim = width
        ci = in_channels
        co = oc_chunk
        sc = scale

        for _ in range_(n_oc_groups):
            elem_wt = of_wt.acquire(1)
            for _ in range_(y_dim):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                kernel_fn(elem_in, elem_wt, elem_out, x_dim, ci, co, sc)
                of_in.release(1)
                of_out.release(1)
            of_wt.release(1)

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

        if n_oc_groups == 1:
            # No OC streaming — contiguous transfers.
            # The FIFO hardware handles element-level buffering independently
            # of the TAP structure; just transfer all data contiguously.
            in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input_size)
            rt.fill(
                in_l3_fifo.prod(),
                I,
                TensorAccessPattern(
                    (1, total_input_size),
                    offset=0,
                    sizes=[in_d3, in_d2, in_d1, in_d0],
                    strides=[
                        in_d2 * in_d1 * in_d0,
                        in_d1 * in_d0,
                        in_d0,
                        1,
                    ],
                ),
            )
            wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(wt_chunk_size)
            rt.fill(
                wt_fifo.prod(),
                W,
                TensorAccessPattern(
                    (1, wt_chunk_size),
                    offset=0,
                    sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                    strides=[
                        wt_d2 * wt_d1 * wt_d0,
                        wt_d1 * wt_d0,
                        wt_d0,
                        1,
                    ],
                ),
            )
            out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output_size)
            rt.drain(
                out_l3_fifo.cons(),
                O,
                TensorAccessPattern(
                    (1, total_output_size),
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
            )
        else:
            # OC streaming: single TAPs with stride-0 repeat for input
            tg = rt.task_group()

            # Input: re-stream n_oc_groups times via stride-0 on d3
            in_d2, in_d1, in_d0 = _factorize_3d(total_input_size)
            rt.fill(
                in_l3_fifo.prod(),
                I,
                TensorAccessPattern(
                    (1, total_input_size),
                    offset=0,
                    sizes=[n_oc_groups, in_d2, in_d1, in_d0],
                    strides=[0, in_d1 * in_d0, in_d0, 1],
                ),
                task_group=tg,
            )

            # Weights: single contiguous transfer of all chunks
            total_wt = n_oc_groups * wt_chunk_size
            wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt)
            rt.fill(
                wt_fifo.prod(),
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

            # Output: scatter OC groups to correct DDR positions
            # Each element is one row of oc_chunk channels: oc_chunk * width bytes
            # In DDR, a full output row is out_channels * width bytes
            per_elem = output_row_size  # oc_chunk * width
            pe_d0 = min(per_elem, 1023)
            while pe_d0 % 4 != 0:
                pe_d0 -= 1
            while pe_d0 >= 4:
                if per_elem % pe_d0 == 0:
                    break
                pe_d0 -= 4
            pe_d1 = per_elem // pe_d0
            rt.drain(
                out_l3_fifo.cons(),
                O,
                TensorAccessPattern(
                    (1, total_output_size),
                    offset=0,
                    sizes=[n_oc_groups, height, pe_d1, pe_d0],
                    strides=[
                        oc_chunk * width,
                        out_channels * width,
                        pe_d0,
                        1,
                    ],
                ),
                wait=True,
                task_group=tg,
            )

            rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


def my_conv2d_int8_k3(
    dev,
    height,
    width,
    in_channels,
    out_channels,
    scale,
    stride,
):
    """ObjectFIFO design for 3x3 int8 conv2d on NPU2.

    Data layout (tiled, groups of 8 channels):
      Input row:   [C_in/8, W, 8]   (int8)
      Weights:     [C_out/8, C_in/8, 3, 3, 8, 8]  (int8)
      Output row:  [C_out/8, W_out, 8]  (int8)

    Supports stride=1 (same spatial) and stride=2 (halved spatial).
    The kernel handles vertical border (check=0/1/2) and horizontal zero-padding.
    Output quantization: int32 accumulate, right-shift by scale, saturate to int8.
    """
    xfr_dtype = np.int8

    assert in_channels % 8 == 0, "in_channels must be a multiple of 8"
    assert out_channels % 8 == 0, "out_channels must be a multiple of 8"
    assert height >= 2, "height must be >= 2 for 3x3 conv"
    assert stride in (1, 2), "Only stride 1 and 2 supported for 3x3 conv"

    if stride == 2:
        assert height % 2 == 0, "height must be even for stride=2"
        assert width % 2 == 0, "width must be even for stride=2"

    # Output spatial dims
    out_h = height if stride == 1 else height // 2
    out_w = width if stride == 1 else width // 2

    # Sizes for one row of data
    input_row_size = in_channels * width
    k_elems = 9  # 3x3

    # Total tensor sizes
    total_input_size = in_channels * height * width
    total_output_size = out_channels * out_h * out_w

    # --- L1 budget: find oc_chunk that fits ---
    # int8 = 1 byte per element
    # input_fifo:  (depth+1) * input_row_size bytes
    # weight_fifo: 1 * oc_chunk * in_channels * 9 bytes
    # output_fifo: 2 * oc_chunk * out_w bytes
    # overhead:    1040 bytes (stack + misc)
    n_oc_groups = 1
    oc_chunk = out_channels
    input_depth = 4  # preferred (3-row window + 1 prefetch)
    _BD_WRAP_MAX = 64  # Max for d3 (outermost) TAP dimension

    found = False
    for try_depth in [4, 3]:
        phys_bufs = try_depth + 1
        input_fbs = phys_bufs * input_row_size
        avail = 65536 - 1040 - input_fbs
        if avail <= 0:
            continue
        for try_oc in range(out_channels, 0, -8):
            if out_channels % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_bytes = try_oc * in_channels * k_elems
            out_bytes = 2 * try_oc * out_w
            if wt_bytes + out_bytes > avail:
                continue
            n_oc = out_channels // try_oc
            if n_oc > _BD_WRAP_MAX:
                continue
            oc_chunk = try_oc
            n_oc_groups = n_oc
            input_depth = try_depth
            found = True
            break
        if found:
            break

    if not found:
        raise ValueError(
            f"k3 int8 conv2d infeasible: "
            f"in_channels={in_channels}, out_channels={out_channels}, width={width}. "
            f"Cannot satisfy L1 budget (64KB)."
        )

    # Per-group sizes
    wt_chunk_elems = oc_chunk * in_channels * k_elems
    output_elem_size = oc_chunk * out_w

    if dev == "npu":
        dev_ty = NPU1()
    else:
        dev_ty = NPU2()

    # Type definitions for ObjectFIFOs
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_elem_size,), np.dtype[xfr_dtype]]
    weights_ty = np.ndarray[(wt_chunk_elems,), np.dtype[xfr_dtype]]

    # L3 (DDR) tensor types
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    weights_l3_ty = np.ndarray[(n_oc_groups * wt_chunk_elems,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

    # Kernel declaration: conv2dk3_i8 or conv2dk3s2_i8
    # Signature: (line0, line1, line2, weights, output, width, IC, OC, check, scale)
    if stride == 1:
        kernel = Kernel(
            "conv2dk3_i8",
            "conv2dk3_i8.o",
            [
                input_row_ty,
                input_row_ty,
                input_row_ty,
                weights_ty,
                output_row_ty,
                np.int32,
                np.int32,
                np.int32,
                np.int32,
                np.int32,
            ],
        )
    else:
        kernel = Kernel(
            "conv2dk3s2_i8",
            "conv2dk3_i8.o",
            [
                input_row_ty,
                input_row_ty,
                input_row_ty,
                weights_ty,
                output_row_ty,
                np.int32,
                np.int32,
                np.int32,
                np.int32,
                np.int32,
            ],
        )

    # ObjectFIFOs
    in_fifo = ObjectFifo(input_row_ty, name="in_fifo", depth=input_depth)
    wt_fifo = ObjectFifo(weights_ty, name="wt_fifo", depth=1)
    out_fifo = ObjectFifo(output_row_ty, name="out_fifo", depth=2)

    # Core function: sliding window pattern
    if stride == 1:

        def core_fn(of_in, of_wt, of_out, kernel_fn):
            y_dim = height
            x_dim = width
            ci = in_channels
            co = oc_chunk
            sc = scale

            for _ in range_(n_oc_groups):
                elem_wt = of_wt.acquire(1)

                # Top row: check=0 (line0 is padding, skipped)
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
                    sc,
                )
                of_out.release(1)

                # Middle rows: check=1
                for _ in range_(y_dim - 2):
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
                        sc,
                    )
                    of_in.release(1)
                    of_out.release(1)

                # Bottom row: check=2 (line2 is padding, skipped)
                elems = of_in.acquire(2)
                elem_out = of_out.acquire(1)
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
                of_out.release(1)

                of_wt.release(1)

    else:
        # Stride-2: output height = height // 2
        # Window advances by 2 rows between output rows.
        def core_fn(of_in, of_wt, of_out, kernel_fn):
            x_dim = width
            ci = in_channels
            co = oc_chunk
            oh = out_h
            sc = scale

            for _ in range_(n_oc_groups):
                elem_wt = of_wt.acquire(1)

                # Top row (output row 0): check=0
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
                    sc,
                )
                of_in.release(1)
                of_out.release(1)

                # Middle rows (output rows 1 to out_h-1): check=1
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
                        sc,
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
    )

    # Runtime sequence
    rt = Runtime()
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker)

        if n_oc_groups == 1:
            # No OC streaming — contiguous transfers with task_group
            tg = rt.task_group()

            in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input_size)
            rt.fill(
                in_fifo.prod(),
                I,
                TensorAccessPattern(
                    (1, total_input_size),
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
            wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(wt_chunk_elems)
            rt.fill(
                wt_fifo.prod(),
                W,
                TensorAccessPattern(
                    (1, wt_chunk_elems),
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
            out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output_size)
            rt.drain(
                out_fifo.cons(),
                O,
                TensorAccessPattern(
                    (1, total_output_size),
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
        else:
            # OC streaming: single TAPs with stride-0 repeat for input
            tg = rt.task_group()

            # Input: re-stream n_oc_groups times via stride-0 on d3
            in_d2, in_d1, in_d0 = _factorize_3d(total_input_size)
            rt.fill(
                in_fifo.prod(),
                I,
                TensorAccessPattern(
                    (1, total_input_size),
                    offset=0,
                    sizes=[n_oc_groups, in_d2, in_d1, in_d0],
                    strides=[0, in_d1 * in_d0, in_d0, 1],
                ),
                task_group=tg,
            )

            # Weights: single contiguous transfer of all chunks
            total_wt = n_oc_groups * wt_chunk_elems
            wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt)
            rt.fill(
                wt_fifo.prod(),
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

            # Output: scatter OC groups to correct DDR positions
            output_row_total = out_channels * out_w
            per_elem = output_elem_size
            pe_d0 = min(per_elem, 1023)
            while pe_d0 % 4 != 0:
                pe_d0 -= 1
            while pe_d0 >= 4:
                if per_elem % pe_d0 == 0:
                    break
                pe_d0 -= 4
            pe_d1 = per_elem // pe_d0
            rt.drain(
                out_fifo.cons(),
                O,
                TensorAccessPattern(
                    (1, total_output_size),
                    offset=0,
                    sizes=[n_oc_groups, out_h, pe_d1, pe_d0],
                    strides=[
                        oc_chunk * out_w,
                        output_row_total,
                        pe_d0,
                        1,
                    ],
                ),
                wait=True,
                task_group=tg,
            )

            rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


def my_conv2d_int8_k3_fused(
    dev,
    height,
    width,
    in_channels,
    out_channels,
    shift1,
    shift2,
    stride,
):
    """ObjectFIFO design for fused 3x3 int8 conv + bias + SiLU on NPU2.

    Uses the packed-bias kernel: int32 bias is appended to the int8 weight
    buffer, so we only need 2 input DMA channels (sliding window + weights).

    Data layout (tiled, groups of 8 channels):
      Input row:    [C_in/8, W, 8]   (int8)
      Weight FIFO:  [C_out/8, C_in/8, 3, 3, 8, 8] ++ [C_out int32 bias]
      Output row:   [C_out/8, W_out, 8]  (int8)
    """
    xfr_dtype = np.int8

    assert in_channels % 8 == 0, "in_channels must be a multiple of 8"
    assert out_channels % 8 == 0, "out_channels must be a multiple of 8"
    assert height >= 2, "height must be >= 2 for 3x3 conv"
    assert stride in (1, 2), "Only stride 1 and 2 supported for 3x3 conv"

    if stride == 2:
        assert height % 2 == 0, "height must be even for stride=2"
        assert width % 2 == 0, "width must be even for stride=2"

    # Output spatial dims
    out_h = height if stride == 1 else height // 2
    out_w = width if stride == 1 else width // 2

    # Sizes for one row of data
    input_row_size = in_channels * width
    k_elems = 9  # 3x3

    # Total tensor sizes
    total_input_size = in_channels * height * width
    total_output_size = out_channels * out_h * out_w

    # --- L1 budget: find oc_chunk that fits ---
    # Fused weights include bias: oc_chunk * ic * 9 + oc_chunk * 4 (int32 bias)
    n_oc_groups = 1
    oc_chunk = out_channels
    input_depth = 4
    _BD_WRAP_MAX = 64

    found = False
    for try_depth in [4, 3]:
        phys_bufs = try_depth + 1
        input_fbs = phys_bufs * input_row_size
        avail = 65536 - 1040 - input_fbs
        if avail <= 0:
            continue
        for try_oc in range(out_channels, 0, -8):
            if out_channels % try_oc != 0 or try_oc % 8 != 0:
                continue
            # Weight bytes + bias bytes (int32 = 4 bytes per OC element)
            wt_bytes = try_oc * in_channels * k_elems + try_oc * 4
            out_bytes = 2 * try_oc * out_w
            if wt_bytes + out_bytes > avail:
                continue
            n_oc = out_channels // try_oc
            if n_oc > _BD_WRAP_MAX:
                continue
            oc_chunk = try_oc
            n_oc_groups = n_oc
            input_depth = try_depth
            found = True
            break
        if found:
            break

    if not found:
        raise ValueError(
            f"k3 fused int8 conv2d infeasible: "
            f"in_channels={in_channels}, out_channels={out_channels}, "
            f"width={width}. Cannot satisfy L1 budget (64KB)."
        )

    # Per-group sizes (weights + bias packed together)
    wt_chunk_elems = oc_chunk * in_channels * k_elems + oc_chunk * 4
    output_elem_size = oc_chunk * out_w

    if dev == "npu":
        dev_ty = NPU1()
    else:
        dev_ty = NPU2()

    # Type definitions for ObjectFIFOs
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_elem_size,), np.dtype[xfr_dtype]]
    weights_ty = np.ndarray[(wt_chunk_elems,), np.dtype[xfr_dtype]]

    # L3 (DDR) tensor types
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    weights_l3_ty = np.ndarray[(n_oc_groups * wt_chunk_elems,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

    # Kernel declaration (packed bias: 5 buffer args + 6 scalar args)
    if stride == 1:
        kernel = Kernel(
            "conv2dk3_i8_silu",
            "conv2dk3_i8_silu.o",
            [
                input_row_ty,
                input_row_ty,
                input_row_ty,
                weights_ty,
                output_row_ty,
                np.int32,
                np.int32,
                np.int32,
                np.int32,
                np.int32,
                np.int32,
            ],
        )
    else:
        kernel = Kernel(
            "conv2dk3s2_i8_silu",
            "conv2dk3_i8_silu.o",
            [
                input_row_ty,
                input_row_ty,
                input_row_ty,
                weights_ty,
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
    in_fifo = ObjectFifo(input_row_ty, name="in_fifo", depth=input_depth)
    wt_fifo = ObjectFifo(weights_ty, name="wt_fifo", depth=1)
    out_fifo = ObjectFifo(output_row_ty, name="out_fifo", depth=2)

    # Core function: sliding window with fused activation
    if stride == 1:

        def core_fn(of_in, of_wt, of_out, kernel_fn):
            y_dim = height
            x_dim = width
            ci = in_channels
            co = oc_chunk
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
                of_out.release(1)

                # Middle rows: check=1
                for _ in range_(y_dim - 2):
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
                    of_in.release(1)
                    of_out.release(1)

                # Bottom row: check=2
                elems = of_in.acquire(2)
                elem_out = of_out.acquire(1)
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
                    s1,
                    s2,
                )
                of_in.release(2)
                of_out.release(1)

                of_wt.release(1)

    else:
        # Stride-2: output height = height // 2

        def core_fn(of_in, of_wt, of_out, kernel_fn):
            x_dim = width
            ci = in_channels
            co = oc_chunk
            oh = out_h
            s1 = shift1
            s2 = shift2

            for _ in range_(n_oc_groups):
                elem_wt = of_wt.acquire(1)

                # Top row (output row 0): check=0
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
    )

    # Runtime sequence
    rt = Runtime()
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(worker)

        if n_oc_groups == 1:
            # No OC streaming — contiguous transfers with task_group
            tg = rt.task_group()

            in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input_size)
            rt.fill(
                in_fifo.prod(),
                I,
                TensorAccessPattern(
                    (1, total_input_size),
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
            wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(wt_chunk_elems)
            rt.fill(
                wt_fifo.prod(),
                W,
                TensorAccessPattern(
                    (1, wt_chunk_elems),
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
            out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output_size)
            rt.drain(
                out_fifo.cons(),
                O,
                TensorAccessPattern(
                    (1, total_output_size),
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
        else:
            # OC streaming: single TAPs with stride-0 repeat for input
            tg = rt.task_group()

            # Input: re-stream n_oc_groups times via stride-0 on d3
            in_d2, in_d1, in_d0 = _factorize_3d(total_input_size)
            rt.fill(
                in_fifo.prod(),
                I,
                TensorAccessPattern(
                    (1, total_input_size),
                    offset=0,
                    sizes=[n_oc_groups, in_d2, in_d1, in_d0],
                    strides=[0, in_d1 * in_d0, in_d0, 1],
                ),
                task_group=tg,
            )

            # Weights: single contiguous transfer of all chunks
            total_wt = n_oc_groups * wt_chunk_elems
            wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt)
            rt.fill(
                wt_fifo.prod(),
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

            # Output: scatter OC groups to correct DDR positions
            output_row_total = out_channels * out_w
            per_elem = output_elem_size
            pe_d0 = min(per_elem, 1023)
            while pe_d0 % 4 != 0:
                pe_d0 -= 1
            while pe_d0 >= 4:
                if per_elem % pe_d0 == 0:
                    break
                pe_d0 -= 4
            pe_d1 = per_elem // pe_d0
            rt.drain(
                out_fifo.cons(),
                O,
                TensorAccessPattern(
                    (1, total_output_size),
                    offset=0,
                    sizes=[n_oc_groups, out_h, pe_d1, pe_d0],
                    strides=[
                        oc_chunk * out_w,
                        output_row_total,
                        pe_d0,
                        1,
                    ],
                ),
                wait=True,
                task_group=tg,
            )

            rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


def my_conv2d_int8_fused(
    dev, height, width, in_channels, out_channels, shift1, shift2,
):
    """Fused 1x1 int8 conv+bias+SiLU with OC streaming.

    Bias packed at end of weight buffer. Supports OC streaming when
    weights+bias don't fit in L1 (same as non-fused k1).
    """
    xfr_dtype = np.int8
    _BD_WRAP_MAX = 64
    assert in_channels % 8 == 0 and out_channels % 8 == 0

    input_row_size = in_channels * width
    total_input = in_channels * height * width
    total_output = out_channels * height * width

    # L1 budget: find oc_chunk that fits (including bias bytes)
    n_oc_groups = 1
    oc_chunk = out_channels
    input_bufs = 2 * input_row_size  # depth=2
    avail = 65536 - 1040 - input_bufs

    if avail <= 0:
        raise ValueError(f"k1 fused int8 infeasible: IC={in_channels}, W={width}")

    wt_bytes = out_channels * in_channels + out_channels * 4  # weights + bias
    out_bytes = 2 * out_channels * width  # depth=2 output
    if wt_bytes + out_bytes > avail:
        found = False
        for try_oc in range(out_channels, 0, -8):
            if out_channels % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_b = try_oc * in_channels + try_oc * 4
            out_b = 2 * try_oc * width
            if wt_b + out_b > avail:
                continue
            n_oc = out_channels // try_oc
            if n_oc > _BD_WRAP_MAX:
                continue
            oc_chunk = try_oc
            n_oc_groups = n_oc
            found = True
            break
        if not found:
            raise ValueError(
                f"k1 fused int8 infeasible: IC={in_channels}, OC={out_channels}, W={width}")

    wt_chunk_size = oc_chunk * in_channels + oc_chunk * 4  # per-chunk weights + bias
    output_row_size = oc_chunk * width
    total_wt = wt_chunk_size * n_oc_groups

    dev_ty = NPU2()
    in_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    wt_ty = np.ndarray[(wt_chunk_size,), np.dtype[xfr_dtype]]
    out_ty = np.ndarray[(output_row_size,), np.dtype[xfr_dtype]]
    in_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wt_l3_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]
    out_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    kernel = Kernel("conv2dk1_i8_fused", "conv2dk1_i8_fused.o",
                     [in_ty, wt_ty, out_ty, np.int32, np.int32, np.int32, np.int32, np.int32])

    # MemTile forwarding for input and output (same as non-fused k1)
    from aie.iron.device import AnyMemTile
    in_l3_fifo = ObjectFifo(in_ty, name="in_l3", depth=2)
    in_fifo = in_l3_fifo.cons().forward(obj_type=in_ty, name="in_l1")
    wt_fifo = ObjectFifo(wt_ty, name="wt", depth=1)
    out_fifo = ObjectFifo(out_ty, name="out_l1", depth=2)
    out_l3_fifo = out_fifo.cons().forward(obj_type=out_ty, name="out_l3")

    def core_fn(oi, ow, oo, k):
        s1, s2 = shift1, shift2
        co = oc_chunk
        for _ in range_(n_oc_groups):
            wt = ow.acquire(1)
            for _ in range_(height):
                ei = oi.acquire(1); eo = oo.acquire(1)
                k(ei, wt, eo, width, in_channels, co, s1, s2)
                oi.release(1); oo.release(1)
            ow.release(1)

    worker = Worker(core_fn, [in_fifo.cons(), wt_fifo.cons(), out_fifo.prod(), kernel])

    rt = Runtime()
    with rt.sequence(in_l3_ty, wt_l3_ty, out_l3_ty) as (I, W, O):
        rt.start(worker)

        if n_oc_groups == 1:
            in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input)
            rt.fill(in_l3_fifo.prod(), I, TensorAccessPattern((1, total_input), offset=0,
                sizes=[in_d3, in_d2, in_d1, in_d0],
                strides=[in_d2*in_d1*in_d0, in_d1*in_d0, in_d0, 1]))
            wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt)
            rt.fill(wt_fifo.prod(), W, TensorAccessPattern((1, total_wt), offset=0,
                sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                strides=[wt_d2*wt_d1*wt_d0, wt_d1*wt_d0, wt_d0, 1]))
            out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output)
            rt.drain(out_l3_fifo.cons(), O, TensorAccessPattern((1, total_output), offset=0,
                sizes=[out_d3, out_d2, out_d1, out_d0],
                strides=[out_d2*out_d1*out_d0, out_d1*out_d0, out_d0, 1]), wait=True)
        else:
            tg = rt.task_group()
            # Input: re-stream n_oc_groups times via stride-0 repeat
            in_d2, in_d1, in_d0 = _factorize_3d(total_input)
            rt.fill(in_l3_fifo.prod(), I, TensorAccessPattern((1, total_input), offset=0,
                sizes=[n_oc_groups, in_d2, in_d1, in_d0],
                strides=[0, in_d1*in_d0, in_d0, 1]), task_group=tg)
            # Weights: contiguous transfer of all chunks
            wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt)
            rt.fill(wt_fifo.prod(), W, TensorAccessPattern((1, total_wt), offset=0,
                sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                strides=[wt_d2*wt_d1*wt_d0, wt_d1*wt_d0, wt_d0, 1]), task_group=tg)
            # Output: scatter OC groups to correct DDR positions
            output_row_total = out_channels * width
            per_elem = output_row_size
            pe_d0 = min(per_elem, 1023)
            while pe_d0 % 4 != 0: pe_d0 -= 1
            while pe_d0 >= 4:
                if per_elem % pe_d0 == 0: break
                pe_d0 -= 4
            pe_d1 = per_elem // pe_d0
            rt.drain(out_l3_fifo.cons(), O, TensorAccessPattern((1, total_output), offset=0,
                sizes=[n_oc_groups, height, pe_d1, pe_d0],
                strides=[oc_chunk*width, output_row_total, pe_d0, 1]),
                wait=True, task_group=tg)
            rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


def my_conv2d_int8_silu(
    dev, height, width, in_channels, out_channels, shift1, shift2,
    kernel_obj="conv2dk1_i8_silu.o",
):
    """Fused 1x1 int8 conv+bias+SiLU using tanh (no LUT).

    Same structure as my_conv2d_int8_fused but uses the conv2dk1_i8_silu
    kernel which computes SiLU via Padé tanh (scalar) or hardware
    aie::tanh<bfloat16> (vector) instead of a sigmoid LUT.

    Bias packed at end of weight buffer. Supports OC streaming when
    weights+bias don't fit in L1 (same as non-fused k1).
    """
    xfr_dtype = np.int8
    _BD_WRAP_MAX = 64
    assert in_channels % 8 == 0 and out_channels % 8 == 0

    input_row_size = in_channels * width
    total_input = in_channels * height * width
    total_output = out_channels * height * width

    # L1 budget: find oc_chunk that fits (including bias bytes)
    n_oc_groups = 1
    oc_chunk = out_channels
    input_bufs = 2 * input_row_size  # depth=2
    avail = 65536 - 1040 - input_bufs

    if avail <= 0:
        raise ValueError(f"k1 silu int8 infeasible: IC={in_channels}, W={width}")

    wt_bytes = out_channels * in_channels + out_channels * 4  # weights + bias
    out_bytes = 2 * out_channels * width  # depth=2 output
    if wt_bytes + out_bytes > avail:
        found = False
        for try_oc in range(out_channels, 0, -8):
            if out_channels % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_b = try_oc * in_channels + try_oc * 4
            out_b = 2 * try_oc * width
            if wt_b + out_b > avail:
                continue
            n_oc = out_channels // try_oc
            if n_oc > _BD_WRAP_MAX:
                continue
            oc_chunk = try_oc
            n_oc_groups = n_oc
            found = True
            break
        if not found:
            raise ValueError(
                f"k1 silu int8 infeasible: "
                f"IC={in_channels}, OC={out_channels}, W={width}"
            )

    wt_chunk_size = oc_chunk * in_channels + oc_chunk * 4
    output_row_size = oc_chunk * width
    total_wt = wt_chunk_size * n_oc_groups

    dev_ty = NPU2()
    in_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    wt_ty = np.ndarray[(wt_chunk_size,), np.dtype[xfr_dtype]]
    out_ty = np.ndarray[(output_row_size,), np.dtype[xfr_dtype]]
    in_l3_ty = np.ndarray[(total_input,), np.dtype[xfr_dtype]]
    wt_l3_ty = np.ndarray[(total_wt,), np.dtype[xfr_dtype]]
    out_l3_ty = np.ndarray[(total_output,), np.dtype[xfr_dtype]]

    kernel = Kernel(
        "conv2dk1_i8_silu", kernel_obj,
        [in_ty, wt_ty, out_ty, np.int32, np.int32, np.int32, np.int32, np.int32],
    )

    from aie.iron.device import AnyMemTile

    in_l3_fifo = ObjectFifo(in_ty, name="in_l3", depth=2)
    in_fifo = in_l3_fifo.cons().forward(obj_type=in_ty, name="in_l1")
    wt_fifo = ObjectFifo(wt_ty, name="wt", depth=1)
    out_fifo = ObjectFifo(out_ty, name="out_l1", depth=2)
    out_l3_fifo = out_fifo.cons().forward(obj_type=out_ty, name="out_l3")

    def core_fn(oi, ow, oo, k):
        s1, s2 = shift1, shift2
        co = oc_chunk
        for _ in range_(n_oc_groups):
            wt = ow.acquire(1)
            for _ in range_(height):
                ei = oi.acquire(1)
                eo = oo.acquire(1)
                k(ei, wt, eo, width, in_channels, co, s1, s2)
                oi.release(1)
                oo.release(1)
            ow.release(1)

    worker = Worker(
        core_fn, [in_fifo.cons(), wt_fifo.cons(), out_fifo.prod(), kernel]
    )

    rt = Runtime()
    with rt.sequence(in_l3_ty, wt_l3_ty, out_l3_ty) as (I, W, O):
        rt.start(worker)

        if n_oc_groups == 1:
            in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input)
            rt.fill(
                in_l3_fifo.prod(), I,
                TensorAccessPattern(
                    (1, total_input), offset=0,
                    sizes=[in_d3, in_d2, in_d1, in_d0],
                    strides=[
                        in_d2 * in_d1 * in_d0, in_d1 * in_d0, in_d0, 1
                    ],
                ),
            )
            wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt)
            rt.fill(
                wt_fifo.prod(), W,
                TensorAccessPattern(
                    (1, total_wt), offset=0,
                    sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                    strides=[
                        wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1
                    ],
                ),
            )
            out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output)
            rt.drain(
                out_l3_fifo.cons(), O,
                TensorAccessPattern(
                    (1, total_output), offset=0,
                    sizes=[out_d3, out_d2, out_d1, out_d0],
                    strides=[
                        out_d2 * out_d1 * out_d0, out_d1 * out_d0, out_d0, 1
                    ],
                ),
                wait=True,
            )
        else:
            tg = rt.task_group()
            in_d2, in_d1, in_d0 = _factorize_3d(total_input)
            rt.fill(
                in_l3_fifo.prod(), I,
                TensorAccessPattern(
                    (1, total_input), offset=0,
                    sizes=[n_oc_groups, in_d2, in_d1, in_d0],
                    strides=[0, in_d1 * in_d0, in_d0, 1],
                ),
                task_group=tg,
            )
            wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(total_wt)
            rt.fill(
                wt_fifo.prod(), W,
                TensorAccessPattern(
                    (1, total_wt), offset=0,
                    sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                    strides=[
                        wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1
                    ],
                ),
                task_group=tg,
            )
            output_row_total = out_channels * width
            per_elem = output_row_size
            pe_d0 = min(per_elem, 1023)
            while pe_d0 % 4 != 0:
                pe_d0 -= 1
            while pe_d0 >= 4:
                if per_elem % pe_d0 == 0:
                    break
                pe_d0 -= 4
            pe_d1 = per_elem // pe_d0
            rt.drain(
                out_l3_fifo.cons(), O,
                TensorAccessPattern(
                    (1, total_output), offset=0,
                    sizes=[n_oc_groups, height, pe_d1, pe_d0],
                    strides=[
                        oc_chunk * width, output_row_total, pe_d0, 1
                    ],
                ),
                wait=True,
                task_group=tg,
            )
            rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())
