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
    num_columns=1,
):
    """ObjectFIFO design for 1x1 int8 conv2d on NPU2.

    Data layout (tiled, groups of 8 channels):
      Input row:   [C_in/8, W, 8]   (int8)
      Weights:     [C_out/8, C_in/8, 8, 8]  (int8)
      Output row:  [C_out/8, W, 8]  (int8)

    Supports OC streaming when weights don't fit in L1: splits output
    channels into chunks, re-streams input for each chunk.

    Each column handles out_channels/num_columns output channels.
    """
    xfr_dtype = np.int8
    _BD_WRAP_MAX = 64

    assert in_channels % 8 == 0, "in_channels must be a multiple of 8"
    assert out_channels % 8 == 0, "out_channels must be a multiple of 8"
    assert (
        out_channels % num_columns == 0
    ), "out_channels must be divisible by num_columns"

    # Per-column output channels
    oc_per_col = out_channels // num_columns

    # Sizes for one row of data
    input_row_size = in_channels * width
    output_row_size_per_col = oc_per_col * width

    # Total tensor sizes
    total_input_size = in_channels * height * width
    total_output_size = out_channels * height * width

    # --- L1 budget: find oc_chunk that fits ---
    # input_fifo: 2 * input_row_size (depth=2, ping-pong)
    # weight_fifo: 1 * oc_chunk * in_channels
    # output_fifo: 2 * oc_chunk * width
    # overhead: 1040 bytes (stack + misc)
    n_oc_groups = 1
    oc_chunk = oc_per_col
    input_bufs = 2 * input_row_size
    avail = 65536 - 1040 - input_bufs

    if avail <= 0:
        raise ValueError(
            f"k1 int8 conv2d infeasible: input row too large "
            f"(IC={in_channels}, W={width})"
        )

    wt_bytes = oc_per_col * in_channels
    out_bytes = 2 * oc_per_col * width
    if wt_bytes + out_bytes > avail:
        # Need OC streaming — find largest oc_chunk that fits
        found = False
        for try_oc in range(oc_per_col, 0, -8):
            if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_b = try_oc * in_channels
            out_b = 2 * try_oc * width
            if wt_b + out_b > avail:
                continue
            n_oc = oc_per_col // try_oc
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

    # Per-column weight size and total weight buffer
    weights_per_col = n_oc_groups * wt_chunk_size
    total_weights_size = weights_per_col * num_columns

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
    weights_l3_ty = np.ndarray[(total_weights_size,), np.dtype[xfr_dtype]]
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

    # ObjectFIFOs per column with MemTile forwarding for input and output
    from aie.iron.device import AnyMemTile

    in_l3_fifos = [
        ObjectFifo(input_row_ty, name=f"in_l3_{i}", depth=2)
        for i in range(num_columns)
    ]
    in_fifos = [
        in_l3_fifos[i].cons().forward(
            obj_type=input_row_ty, name=f"in_l1_{i}"
        )
        for i in range(num_columns)
    ]
    wt_fifos = [
        ObjectFifo(weights_ty, name=f"wt_{i}", depth=1)
        for i in range(num_columns)
    ]
    out_fifos = [
        ObjectFifo(output_row_ty, name=f"out_l1_{i}", depth=2)
        for i in range(num_columns)
    ]
    out_l3_fifos = [
        out_fifos[i].cons().forward(
            obj_type=output_row_ty, name=f"out_l3_{i}"
        )
        for i in range(num_columns)
    ]

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

    # Workers — one per column
    workers = [
        Worker(
            core_fn,
            [
                in_fifos[i].cons(),
                wt_fifos[i].cons(),
                out_fifos[i].prod(),
                conv2dk1_i8_kernel,
            ],
        )
        for i in range(num_columns)
    ]

    # Input TAPs: all columns receive the same contiguous input
    in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input_size)
    in_tap_contiguous = TensorAccessPattern(
        (1, total_input_size),
        offset=0,
        sizes=[in_d3, in_d2, in_d1, in_d0],
        strides=[in_d2 * in_d1 * in_d0, in_d1 * in_d0, in_d0, 1],
    )

    if n_oc_groups > 1:
        in_d2_3d, in_d1_3d, in_d0_3d = _factorize_3d(total_input_size)
        in_tap_streaming = TensorAccessPattern(
            (1, total_input_size),
            offset=0,
            sizes=[n_oc_groups, in_d2_3d, in_d1_3d, in_d0_3d],
            strides=[0, in_d1_3d * in_d0_3d, in_d0_3d, 1],
        )

    # Weight TAPs: each column gets its contiguous weight slice
    wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(weights_per_col)
    wt_taps = [
        TensorAccessPattern(
            (1, total_weights_size),
            offset=i * weights_per_col,
            sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
            strides=[wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1],
        )
        for i in range(num_columns)
    ]

    # Output TAPs: each column writes to its OC slice in DDR
    output_row_total = out_channels * width
    if n_oc_groups > 1:
        per_elem = output_row_size  # oc_chunk * width
        pe_d0 = min(per_elem, 1023)
        while pe_d0 % 4 != 0:
            pe_d0 -= 1
        while pe_d0 >= 4:
            if per_elem % pe_d0 == 0:
                break
            pe_d0 -= 4
        pe_d1 = per_elem // pe_d0
        out_taps = [
            TensorAccessPattern(
                (1, total_output_size),
                offset=i * oc_per_col * width,
                sizes=[n_oc_groups, height, pe_d1, pe_d0],
                strides=[oc_chunk * width, output_row_total, pe_d0, 1],
            )
            for i in range(num_columns)
        ]
    elif num_columns == 1:
        out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output_size)
        out_taps = [
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
            )
        ]
    else:
        per_row = output_row_size_per_col
        _BD_WRAP_MAX_OUT = 64
        if height <= _BD_WRAP_MAX_OUT:
            pr_d2, pr_d1, pr_d0 = _factorize_3d(per_row)
            out_taps = [
                TensorAccessPattern(
                    (1, total_output_size),
                    offset=i * oc_per_col * width,
                    sizes=[height, pr_d2, pr_d1, pr_d0],
                    strides=[output_row_total, pr_d1 * pr_d0, pr_d0, 1],
                )
                for i in range(num_columns)
            ]
        else:
            h_outer = min(height, _BD_WRAP_MAX_OUT)
            while h_outer >= 1 and (
                height % h_outer != 0 or height // h_outer > 1023
            ):
                h_outer -= 1
            assert h_outer >= 1, (
                f"Cannot split height={height} into valid BD dims"
            )
            h_inner = height // h_outer
            d0 = min(per_row, 1023)
            while d0 % 4 != 0:
                d0 -= 1
            while d0 >= 4 and per_row % d0 != 0:
                d0 -= 4
            assert d0 >= 4, (
                f"Cannot factorize per_row={per_row} into 2D BD dims"
            )
            d1 = per_row // d0
            assert d1 <= 1023, (
                f"per_row={per_row} too large for 2D BD factorization"
            )
            out_taps = [
                TensorAccessPattern(
                    (1, total_output_size),
                    offset=i * oc_per_col * width,
                    sizes=[h_outer, h_inner, d1, d0],
                    strides=[
                        output_row_total * h_inner,
                        output_row_total,
                        d0,
                        1,
                    ],
                )
                for i in range(num_columns)
            ]

    # Runtime sequence
    rt = Runtime()
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(*workers)

        tg = rt.task_group()

        # Fill input FIFOs: broadcast input to all columns
        if n_oc_groups > 1:
            for i in range(num_columns):
                rt.fill(
                    in_l3_fifos[i].prod(), I, in_tap_streaming, task_group=tg
                )
        else:
            for _g in range(n_oc_groups):
                for i in range(num_columns):
                    rt.fill(
                        in_l3_fifos[i].prod(),
                        I,
                        in_tap_contiguous,
                        task_group=tg,
                    )

        # Fill weight FIFOs: each column gets its weight slice
        for i in range(num_columns):
            rt.fill(wt_fifos[i].prod(), W, wt_taps[i], task_group=tg)

        # Drain output FIFOs: each column drains to correct DDR position
        for i in range(num_columns):
            rt.drain(
                out_l3_fifos[i].cons(),
                O,
                out_taps[i],
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
    num_columns=1,
):
    """ObjectFIFO design for 3x3 int8 conv2d on NPU2.

    Data layout (tiled, groups of 8 channels):
      Input row:   [C_in/8, W, 8]   (int8)
      Weights:     [C_out/8, C_in/8, 3, 3, 8, 8]  (int8)
      Output row:  [C_out/8, W_out, 8]  (int8)

    Supports stride=1 (same spatial) and stride=2 (halved spatial).
    The kernel handles vertical border (check=0/1/2) and horizontal zero-padding.
    Output quantization: int32 accumulate, right-shift by scale, saturate to int8.

    Each column handles out_channels/num_columns output channels.
    """
    xfr_dtype = np.int8

    assert in_channels % 8 == 0, "in_channels must be a multiple of 8"
    assert out_channels % 8 == 0, "out_channels must be a multiple of 8"
    assert (
        out_channels % num_columns == 0
    ), "out_channels must be divisible by num_columns"
    assert height >= 2, "height must be >= 2 for 3x3 conv"
    assert stride in (1, 2), "Only stride 1 and 2 supported for 3x3 conv"

    if stride == 2:
        assert height % 2 == 0, "height must be even for stride=2"
        assert width % 2 == 0, "width must be even for stride=2"

    # Output spatial dims
    out_h = height if stride == 1 else height // 2
    out_w = width if stride == 1 else width // 2

    # Per-column output channels
    oc_per_col = out_channels // num_columns

    # Sizes for one row of data
    input_row_size = in_channels * width
    k_elems = 9  # 3x3
    output_row_size_per_col = oc_per_col * out_w

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
    oc_chunk = oc_per_col
    input_depth = 4  # preferred (3-row window + 1 prefetch)
    _BD_WRAP_MAX = 64  # Max for d3 (outermost) TAP dimension

    found = False
    for try_depth in [4, 3]:
        phys_bufs = try_depth + 1
        input_fbs = phys_bufs * input_row_size
        avail = 65536 - 1040 - input_fbs
        if avail <= 0:
            continue
        for try_oc in range(oc_per_col, 0, -8):
            if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_bytes = try_oc * in_channels * k_elems
            out_bytes = 2 * try_oc * out_w
            if wt_bytes + out_bytes > avail:
                continue
            n_oc = oc_per_col // try_oc
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

    # Per-column weight size and total weight buffer
    weights_per_col = n_oc_groups * wt_chunk_elems
    total_weights_size = weights_per_col * num_columns

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
    weights_l3_ty = np.ndarray[(total_weights_size,), np.dtype[xfr_dtype]]
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

    # ObjectFIFOs per column
    in_fifos = [
        ObjectFifo(input_row_ty, name=f"in_{i}", depth=input_depth)
        for i in range(num_columns)
    ]
    wt_fifos = [
        ObjectFifo(weights_ty, name=f"wt_{i}", depth=1)
        for i in range(num_columns)
    ]
    out_fifos = [
        ObjectFifo(output_row_ty, name=f"out_{i}", depth=2)
        for i in range(num_columns)
    ]

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

    # Workers — one per column
    workers = [
        Worker(
            core_fn,
            [in_fifos[i].cons(), wt_fifos[i].cons(), out_fifos[i].prod(), kernel],
        )
        for i in range(num_columns)
    ]

    # Input TAPs: all columns receive the same contiguous input
    in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input_size)
    in_tap_contiguous = TensorAccessPattern(
        (1, total_input_size),
        offset=0,
        sizes=[in_d3, in_d2, in_d1, in_d0],
        strides=[in_d2 * in_d1 * in_d0, in_d1 * in_d0, in_d0, 1],
    )

    # For OC streaming: input re-streamed n_oc_groups times via stride-0
    if n_oc_groups > 1:
        in_d2_3d, in_d1_3d, in_d0_3d = _factorize_3d(total_input_size)
        in_tap_streaming = TensorAccessPattern(
            (1, total_input_size),
            offset=0,
            sizes=[n_oc_groups, in_d2_3d, in_d1_3d, in_d0_3d],
            strides=[0, in_d1_3d * in_d0_3d, in_d0_3d, 1],
        )

    # Weight TAPs: each column gets its contiguous weight slice
    wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(weights_per_col)
    wt_taps = [
        TensorAccessPattern(
            (1, total_weights_size),
            offset=i * weights_per_col,
            sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
            strides=[wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1],
        )
        for i in range(num_columns)
    ]

    # Output TAPs: each column writes to its OC slice in DDR
    output_row_total = out_channels * out_w
    if n_oc_groups > 1:
        # OC streaming: scatter [n_oc_groups, out_h] output rows
        per_elem = output_elem_size  # oc_chunk * out_w
        pe_d0 = min(per_elem, 1023)
        while pe_d0 % 4 != 0:
            pe_d0 -= 1
        while pe_d0 >= 4:
            if per_elem % pe_d0 == 0:
                break
            pe_d0 -= 4
        pe_d1 = per_elem // pe_d0
        out_taps = [
            TensorAccessPattern(
                (1, total_output_size),
                offset=i * oc_per_col * out_w,
                sizes=[n_oc_groups, out_h, pe_d1, pe_d0],
                strides=[oc_chunk * out_w, output_row_total, pe_d0, 1],
            )
            for i in range(num_columns)
        ]
    elif num_columns == 1:
        # Single column, no OC streaming: contiguous output
        out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output_size)
        out_taps = [
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
            )
        ]
    else:
        # Multi-column, no OC streaming: scatter per-column OC slices
        per_row = output_row_size_per_col  # oc_per_col * out_w
        _BD_WRAP_MAX_OUT = 64
        if out_h <= _BD_WRAP_MAX_OUT:
            pr_d2, pr_d1, pr_d0 = _factorize_3d(per_row)
            out_taps = [
                TensorAccessPattern(
                    (1, total_output_size),
                    offset=i * oc_per_col * out_w,
                    sizes=[out_h, pr_d2, pr_d1, pr_d0],
                    strides=[output_row_total, pr_d1 * pr_d0, pr_d0, 1],
                )
                for i in range(num_columns)
            ]
        else:
            h_outer = min(out_h, _BD_WRAP_MAX_OUT)
            while h_outer >= 1 and (
                out_h % h_outer != 0 or out_h // h_outer > 1023
            ):
                h_outer -= 1
            assert h_outer >= 1, (
                f"Cannot split out_h={out_h} into valid BD dims"
            )
            h_inner = out_h // h_outer
            d0 = min(per_row, 1023)
            while d0 % 4 != 0:
                d0 -= 1
            while d0 >= 4 and per_row % d0 != 0:
                d0 -= 4
            assert d0 >= 4, (
                f"Cannot factorize per_row={per_row} into 2D BD dims"
            )
            d1 = per_row // d0
            assert d1 <= 1023, (
                f"per_row={per_row} too large for 2D BD factorization"
            )
            out_taps = [
                TensorAccessPattern(
                    (1, total_output_size),
                    offset=i * oc_per_col * out_w,
                    sizes=[h_outer, h_inner, d1, d0],
                    strides=[
                        output_row_total * h_inner,
                        output_row_total,
                        d0,
                        1,
                    ],
                )
                for i in range(num_columns)
            ]

    # Runtime sequence
    rt = Runtime()
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(*workers)

        tg = rt.task_group()

        # Fill input FIFOs: broadcast input to all columns
        if n_oc_groups > 1:
            for i in range(num_columns):
                rt.fill(in_fifos[i].prod(), I, in_tap_streaming, task_group=tg)
        else:
            for _g in range(n_oc_groups):
                for i in range(num_columns):
                    rt.fill(
                        in_fifos[i].prod(), I, in_tap_contiguous, task_group=tg
                    )

        # Fill weight FIFOs: each column gets its weight slice
        for i in range(num_columns):
            rt.fill(wt_fifos[i].prod(), W, wt_taps[i], task_group=tg)

        # Drain output FIFOs: each column drains to correct DDR position
        for i in range(num_columns):
            rt.drain(
                out_fifos[i].cons(), O, out_taps[i], wait=True, task_group=tg
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
    num_columns=1,
):
    """ObjectFIFO design for fused 3x3 int8 conv + bias + SiLU on NPU2.

    Uses the packed-bias kernel: int32 bias is appended to the int8 weight
    buffer, so we only need 2 input DMA channels (sliding window + weights).

    Data layout (tiled, groups of 8 channels):
      Input row:    [C_in/8, W, 8]   (int8)
      Weight FIFO:  [C_out/8, C_in/8, 3, 3, 8, 8] ++ [C_out int32 bias]
      Output row:   [C_out/8, W_out, 8]  (int8)

    Each column handles out_channels/num_columns output channels.
    """
    xfr_dtype = np.int8

    assert in_channels % 8 == 0, "in_channels must be a multiple of 8"
    assert out_channels % 8 == 0, "out_channels must be a multiple of 8"
    assert (
        out_channels % num_columns == 0
    ), "out_channels must be divisible by num_columns"
    assert height >= 2, "height must be >= 2 for 3x3 conv"
    assert stride in (1, 2), "Only stride 1 and 2 supported for 3x3 conv"

    if stride == 2:
        assert height % 2 == 0, "height must be even for stride=2"
        assert width % 2 == 0, "width must be even for stride=2"

    # Output spatial dims
    out_h = height if stride == 1 else height // 2
    out_w = width if stride == 1 else width // 2

    # Per-column output channels
    oc_per_col = out_channels // num_columns

    # Sizes for one row of data
    input_row_size = in_channels * width
    k_elems = 9  # 3x3
    output_row_size_per_col = oc_per_col * out_w

    # Total tensor sizes
    total_input_size = in_channels * height * width
    total_output_size = out_channels * out_h * out_w

    # --- L1 budget: find oc_chunk that fits ---
    # Fused weights include bias: oc_chunk * ic * 9 + oc_chunk * 4 (int32 bias)
    n_oc_groups = 1
    oc_chunk = oc_per_col
    input_depth = 4
    _BD_WRAP_MAX = 64

    found = False
    for try_depth in [4, 3]:
        phys_bufs = try_depth + 1
        input_fbs = phys_bufs * input_row_size
        avail = 65536 - 1040 - input_fbs
        if avail <= 0:
            continue
        for try_oc in range(oc_per_col, 0, -8):
            if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                continue
            # Weight bytes + bias bytes (int32 = 4 bytes per OC element)
            wt_bytes = try_oc * in_channels * k_elems + try_oc * 4
            out_bytes = 2 * try_oc * out_w
            if wt_bytes + out_bytes > avail:
                continue
            n_oc = oc_per_col // try_oc
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

    # Per-column weight size and total weight buffer
    weights_per_col = n_oc_groups * wt_chunk_elems
    total_weights_size = weights_per_col * num_columns

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
    weights_l3_ty = np.ndarray[(total_weights_size,), np.dtype[xfr_dtype]]
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

    # ObjectFIFOs per column
    in_fifos = [
        ObjectFifo(input_row_ty, name=f"in_{i}", depth=input_depth)
        for i in range(num_columns)
    ]
    wt_fifos = [
        ObjectFifo(weights_ty, name=f"wt_{i}", depth=1)
        for i in range(num_columns)
    ]
    out_fifos = [
        ObjectFifo(output_row_ty, name=f"out_{i}", depth=2)
        for i in range(num_columns)
    ]

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

    # Workers — one per column
    workers = [
        Worker(
            core_fn,
            [in_fifos[i].cons(), wt_fifos[i].cons(), out_fifos[i].prod(), kernel],
        )
        for i in range(num_columns)
    ]

    # Input TAPs: all columns receive the same contiguous input
    in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input_size)
    in_tap_contiguous = TensorAccessPattern(
        (1, total_input_size),
        offset=0,
        sizes=[in_d3, in_d2, in_d1, in_d0],
        strides=[in_d2 * in_d1 * in_d0, in_d1 * in_d0, in_d0, 1],
    )

    # For OC streaming: input re-streamed n_oc_groups times via stride-0
    if n_oc_groups > 1:
        in_d2_3d, in_d1_3d, in_d0_3d = _factorize_3d(total_input_size)
        in_tap_streaming = TensorAccessPattern(
            (1, total_input_size),
            offset=0,
            sizes=[n_oc_groups, in_d2_3d, in_d1_3d, in_d0_3d],
            strides=[0, in_d1_3d * in_d0_3d, in_d0_3d, 1],
        )

    # Weight TAPs: each column gets its contiguous weight slice
    wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(weights_per_col)
    wt_taps = [
        TensorAccessPattern(
            (1, total_weights_size),
            offset=i * weights_per_col,
            sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
            strides=[wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1],
        )
        for i in range(num_columns)
    ]

    # Output TAPs: each column writes to its OC slice in DDR
    output_row_total = out_channels * out_w
    if n_oc_groups > 1:
        per_elem = output_elem_size
        pe_d0 = min(per_elem, 1023)
        while pe_d0 % 4 != 0:
            pe_d0 -= 1
        while pe_d0 >= 4:
            if per_elem % pe_d0 == 0:
                break
            pe_d0 -= 4
        pe_d1 = per_elem // pe_d0
        out_taps = [
            TensorAccessPattern(
                (1, total_output_size),
                offset=i * oc_per_col * out_w,
                sizes=[n_oc_groups, out_h, pe_d1, pe_d0],
                strides=[oc_chunk * out_w, output_row_total, pe_d0, 1],
            )
            for i in range(num_columns)
        ]
    elif num_columns == 1:
        out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output_size)
        out_taps = [
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
            )
        ]
    else:
        per_row = output_row_size_per_col
        _BD_WRAP_MAX_OUT = 64
        if out_h <= _BD_WRAP_MAX_OUT:
            pr_d2, pr_d1, pr_d0 = _factorize_3d(per_row)
            out_taps = [
                TensorAccessPattern(
                    (1, total_output_size),
                    offset=i * oc_per_col * out_w,
                    sizes=[out_h, pr_d2, pr_d1, pr_d0],
                    strides=[output_row_total, pr_d1 * pr_d0, pr_d0, 1],
                )
                for i in range(num_columns)
            ]
        else:
            h_outer = min(out_h, _BD_WRAP_MAX_OUT)
            while h_outer >= 1 and (
                out_h % h_outer != 0 or out_h // h_outer > 1023
            ):
                h_outer -= 1
            assert h_outer >= 1, (
                f"Cannot split out_h={out_h} into valid BD dims"
            )
            h_inner = out_h // h_outer
            d0 = min(per_row, 1023)
            while d0 % 4 != 0:
                d0 -= 1
            while d0 >= 4 and per_row % d0 != 0:
                d0 -= 4
            assert d0 >= 4, (
                f"Cannot factorize per_row={per_row} into 2D BD dims"
            )
            d1 = per_row // d0
            assert d1 <= 1023, (
                f"per_row={per_row} too large for 2D BD factorization"
            )
            out_taps = [
                TensorAccessPattern(
                    (1, total_output_size),
                    offset=i * oc_per_col * out_w,
                    sizes=[h_outer, h_inner, d1, d0],
                    strides=[
                        output_row_total * h_inner,
                        output_row_total,
                        d0,
                        1,
                    ],
                )
                for i in range(num_columns)
            ]

    # Runtime sequence
    rt = Runtime()
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (I, W, O):
        rt.start(*workers)

        tg = rt.task_group()

        # Fill input FIFOs: broadcast input to all columns
        if n_oc_groups > 1:
            for i in range(num_columns):
                rt.fill(in_fifos[i].prod(), I, in_tap_streaming, task_group=tg)
        else:
            for _g in range(n_oc_groups):
                for i in range(num_columns):
                    rt.fill(
                        in_fifos[i].prod(), I, in_tap_contiguous, task_group=tg
                    )

        # Fill weight FIFOs: each column gets its weight slice
        for i in range(num_columns):
            rt.fill(wt_fifos[i].prod(), W, wt_taps[i], task_group=tg)

        # Drain output FIFOs: each column drains to correct DDR position
        for i in range(num_columns):
            rt.drain(
                out_fifos[i].cons(), O, out_taps[i], wait=True, task_group=tg
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
    num_columns=1,
):
    """Fused 1x1 int8 conv+bias+SiLU using tanh (no LUT).

    Same structure as my_conv2d_int8_fused but uses the conv2dk1_i8_silu
    kernel which computes SiLU via Padé tanh (scalar) or hardware
    aie::tanh<bfloat16> (vector) instead of a sigmoid LUT.

    Bias packed at end of weight buffer. Supports OC streaming when
    weights+bias don't fit in L1 (same as non-fused k1).

    Each column handles out_channels/num_columns output channels.
    """
    xfr_dtype = np.int8
    _BD_WRAP_MAX = 64
    assert in_channels % 8 == 0 and out_channels % 8 == 0
    assert (
        out_channels % num_columns == 0
    ), "out_channels must be divisible by num_columns"

    # Per-column output channels
    oc_per_col = out_channels // num_columns

    input_row_size = in_channels * width
    output_row_size_per_col = oc_per_col * width
    total_input = in_channels * height * width
    total_output = out_channels * height * width

    # L1 budget: find oc_chunk that fits (including bias bytes)
    n_oc_groups = 1
    oc_chunk = oc_per_col
    input_bufs = 2 * input_row_size  # depth=2
    avail = 65536 - 1040 - input_bufs

    if avail <= 0:
        raise ValueError(f"k1 silu int8 infeasible: IC={in_channels}, W={width}")

    wt_bytes = oc_per_col * in_channels + oc_per_col * 4  # weights + bias
    out_bytes = 2 * oc_per_col * width  # depth=2 output
    if wt_bytes + out_bytes > avail:
        found = False
        for try_oc in range(oc_per_col, 0, -8):
            if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_b = try_oc * in_channels + try_oc * 4
            out_b = 2 * try_oc * width
            if wt_b + out_b > avail:
                continue
            n_oc = oc_per_col // try_oc
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
    weights_per_col = wt_chunk_size * n_oc_groups
    total_wt = weights_per_col * num_columns

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

    # ObjectFIFOs per column with MemTile forwarding
    in_l3_fifos = [
        ObjectFifo(in_ty, name=f"in_l3_{i}", depth=2)
        for i in range(num_columns)
    ]
    in_fifos = [
        in_l3_fifos[i].cons().forward(obj_type=in_ty, name=f"in_l1_{i}")
        for i in range(num_columns)
    ]
    wt_fifos = [
        ObjectFifo(wt_ty, name=f"wt_{i}", depth=1)
        for i in range(num_columns)
    ]
    out_fifos = [
        ObjectFifo(out_ty, name=f"out_l1_{i}", depth=2)
        for i in range(num_columns)
    ]
    out_l3_fifos = [
        out_fifos[i].cons().forward(obj_type=out_ty, name=f"out_l3_{i}")
        for i in range(num_columns)
    ]

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

    # Workers — one per column
    workers = [
        Worker(
            core_fn,
            [in_fifos[i].cons(), wt_fifos[i].cons(), out_fifos[i].prod(), kernel],
        )
        for i in range(num_columns)
    ]

    # Input TAPs: all columns receive the same contiguous input
    in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input)
    in_tap_contiguous = TensorAccessPattern(
        (1, total_input), offset=0,
        sizes=[in_d3, in_d2, in_d1, in_d0],
        strides=[in_d2 * in_d1 * in_d0, in_d1 * in_d0, in_d0, 1],
    )
    if n_oc_groups > 1:
        in_d2_3d, in_d1_3d, in_d0_3d = _factorize_3d(total_input)
        in_tap_streaming = TensorAccessPattern(
            (1, total_input), offset=0,
            sizes=[n_oc_groups, in_d2_3d, in_d1_3d, in_d0_3d],
            strides=[0, in_d1_3d * in_d0_3d, in_d0_3d, 1],
        )

    # Weight TAPs: each column gets its contiguous weight slice
    wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(weights_per_col)
    wt_taps = [
        TensorAccessPattern(
            (1, total_wt), offset=i * weights_per_col,
            sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
            strides=[wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1],
        )
        for i in range(num_columns)
    ]

    # Output TAPs: each column writes to its OC slice in DDR
    output_row_total = out_channels * width
    if n_oc_groups > 1:
        per_elem = output_row_size  # oc_chunk * width
        pe_d0 = min(per_elem, 1023)
        while pe_d0 % 4 != 0:
            pe_d0 -= 1
        while pe_d0 >= 4:
            if per_elem % pe_d0 == 0:
                break
            pe_d0 -= 4
        pe_d1 = per_elem // pe_d0
        out_taps = [
            TensorAccessPattern(
                (1, total_output), offset=i * oc_per_col * width,
                sizes=[n_oc_groups, height, pe_d1, pe_d0],
                strides=[oc_chunk * width, output_row_total, pe_d0, 1],
            )
            for i in range(num_columns)
        ]
    elif num_columns == 1:
        out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output)
        out_taps = [
            TensorAccessPattern(
                (1, total_output), offset=0,
                sizes=[out_d3, out_d2, out_d1, out_d0],
                strides=[
                    out_d2 * out_d1 * out_d0, out_d1 * out_d0, out_d0, 1
                ],
            )
        ]
    else:
        per_row = output_row_size_per_col
        _BD_WRAP_MAX_OUT = 64
        if height <= _BD_WRAP_MAX_OUT:
            pr_d2, pr_d1, pr_d0 = _factorize_3d(per_row)
            out_taps = [
                TensorAccessPattern(
                    (1, total_output), offset=i * oc_per_col * width,
                    sizes=[height, pr_d2, pr_d1, pr_d0],
                    strides=[output_row_total, pr_d1 * pr_d0, pr_d0, 1],
                )
                for i in range(num_columns)
            ]
        else:
            h_outer = min(height, _BD_WRAP_MAX_OUT)
            while h_outer >= 1 and (
                height % h_outer != 0 or height // h_outer > 1023
            ):
                h_outer -= 1
            h_inner = height // h_outer
            d0 = min(per_row, 1023)
            while d0 % 4 != 0:
                d0 -= 1
            while d0 >= 4 and per_row % d0 != 0:
                d0 -= 4
            d1 = per_row // d0
            out_taps = [
                TensorAccessPattern(
                    (1, total_output), offset=i * oc_per_col * width,
                    sizes=[h_outer, h_inner, d1, d0],
                    strides=[
                        output_row_total * h_inner, output_row_total, d0, 1
                    ],
                )
                for i in range(num_columns)
            ]

    rt = Runtime()
    with rt.sequence(in_l3_ty, wt_l3_ty, out_l3_ty) as (I, W, O):
        rt.start(*workers)

        tg = rt.task_group()

        # Fill input FIFOs: broadcast input to all columns
        if n_oc_groups > 1:
            for i in range(num_columns):
                rt.fill(
                    in_l3_fifos[i].prod(), I, in_tap_streaming, task_group=tg
                )
        else:
            for _g in range(n_oc_groups):
                for i in range(num_columns):
                    rt.fill(
                        in_l3_fifos[i].prod(), I, in_tap_contiguous,
                        task_group=tg,
                    )

        # Fill weight FIFOs: each column gets its weight slice
        for i in range(num_columns):
            rt.fill(wt_fifos[i].prod(), W, wt_taps[i], task_group=tg)

        # Drain output FIFOs
        for i in range(num_columns):
            rt.drain(
                out_l3_fifos[i].cons(), O, out_taps[i],
                wait=True, task_group=tg,
            )

        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())
