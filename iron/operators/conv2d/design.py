# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
from pathlib import Path
import numpy as np
import argparse
import sys

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_

# AIE NPU2 hardware constraint: all 4 BD wrap sizes (d0, d1, d2, d3) must be <= 64.
# TensorAccessPattern is 4D: sizes=[d3, d2, d1, d0].  All must satisfy this limit.
# For large tensors (e.g. 640x640 images) the total elements exceed 64^2, so we
# must find a 4D factorization of the total with all factors <= 64.
_BD_WRAP_MAX = 64


def _factorize_tensor(total: int) -> tuple[int, int, int, int]:
    """Factor total elements into four BD dims (d3, d2, d1, d0).

    Hardware constraints for NPU2 bf16 DMA BDs:
    - d3 (outermost, Size 3): must be in [1:64]
    - d2, d1 (Size 2, 1): up to ~1023
    - d0 (innermost, Size 0): up to 1023; must be even (d0*2 bytes % 4 == 0)

    Returns (d3, d2, d1, d0) with d3*d2*d1*d0 == total.
    """
    _D0_MAX = 1023
    _D12_MAX = 1023

    def _find_even_d0(rest: int) -> int | None:
        """Find the largest even divisor of rest that is <= _D0_MAX."""
        d0 = min(rest, _D0_MAX)
        if d0 % 2 != 0:
            d0 -= 1
        while d0 >= 2:
            if rest % d0 == 0:
                return d0
            d0 -= 2
        return None

    # Try each d3 from largest divisor <= 64 downward until a valid solution is found.
    d3 = min(total, _BD_WRAP_MAX)
    while d3 >= 1:
        if total % d3 == 0:
            rest = total // d3
            d0 = _find_even_d0(rest)
            if d0 is not None:
                rest2 = rest // d0
                # Split rest2 into d1 * d2
                d1 = min(rest2, _D12_MAX)
                while d1 > 1 and rest2 % d1 != 0:
                    d1 -= 1
                d2 = rest2 // d1
                if d2 <= _D12_MAX:
                    return (d3, d2, d1, d0)
        d3 -= 1

    raise ValueError(
        f"Cannot factorize total={total} into valid BD dims "
        f"(d3<={_BD_WRAP_MAX}, d0 even and <={_D0_MAX}, d1,d2<={_D12_MAX})"
    )


def my_conv2d(
    dev,
    height,
    width,
    in_channels,
    out_channels,
    kernel_size,
    stride,
    has_bias,
    activation,
    num_columns,
):
    """ObjectFIFO design for 1x1 conv2d on NPU2 with bfloat16.

    Data layout (tiled, groups of 8 channels):
      Input row:   [C_in/8, W, 8]
      Weights:     [C_out/8, C_in/8, 8, 8]
      Output row:  [C_out/8, W, 8]

    Each column handles out_channels/num_columns output channels.
    The core processes one input row at a time: acquires weights once,
    then loops over height rows acquiring input, calling the kernel,
    and releasing output.

    If has_bias is True, the bias is folded into the weight buffer
    (appended after weights) and the kernel is expected to handle it.
    For Phase 1, bias is handled in the Python forward() method instead.
    """
    xfr_dtype = bfloat16

    assert kernel_size == 1, "Only kernel_size=1 supported"
    assert in_channels % 8 == 0, "in_channels must be a multiple of 8"
    assert out_channels % 8 == 0, "out_channels must be a multiple of 8"
    assert (
        out_channels % num_columns == 0
    ), "out_channels must be divisible by num_columns"

    # Per-column output channels
    oc_per_col = out_channels // num_columns

    # Sizes for one row of data
    input_row_size = in_channels * width  # [C_in/8, W, 8] flattened
    output_row_size_per_col = oc_per_col * width  # per column

    # Weight size per column: [oc_per_col/8, C_in/8, 8, 8]
    weights_per_col = oc_per_col * in_channels

    # When bias+SiLU is fused, bias is packed at the end of each column's weights
    fused_bias_silu = has_bias and activation == "silu"
    if fused_bias_silu:
        weights_per_col += oc_per_col  # bias for this column's oc channels

    # Total tensor sizes for runtime sequence arguments
    total_input_size = in_channels * height * width
    total_weights_size = weights_per_col * num_columns
    total_output_size = out_channels * height * width

    # Type definitions for ObjectFIFOs
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_row_size_per_col,), np.dtype[xfr_dtype]]
    weights_ty = np.ndarray[(weights_per_col,), np.dtype[xfr_dtype]]

    # L3 (DDR) tensor types for runtime sequence
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    weights_l3_ty = np.ndarray[(total_weights_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

    if dev == "npu":
        dev_ty = NPU1()
    else:
        dev_ty = NPU2()

    # Kernel declaration -- select fused variant when bias+SiLU is requested
    if has_bias and activation == "silu":
        conv2dk1_kernel = Kernel(
            "conv2dk1_bf16_bias_silu",
            "conv2dk1_bf16.o",
            [input_row_ty, weights_ty, output_row_ty, np.int32, np.int32, np.int32],
        )
    else:
        conv2dk1_kernel = Kernel(
            "conv2dk1_bf16",
            "conv2dk1_bf16.o",
            [input_row_ty, weights_ty, output_row_ty, np.int32, np.int32, np.int32],
        )

    # ObjectFIFOs per column
    in_fifos = [
        ObjectFifo(input_row_ty, name=f"in_{i}", depth=2) for i in range(num_columns)
    ]
    wt_fifos = [
        ObjectFifo(weights_ty, name=f"wt_{i}", depth=1) for i in range(num_columns)
    ]
    out_fifos = [
        ObjectFifo(output_row_ty, name=f"out_{i}", depth=2) for i in range(num_columns)
    ]

    # Core function: acquire weights once, then loop over rows
    def core_fn(of_in, of_wt, of_out, kernel_fn):
        y_dim = height
        x_dim = width
        ci = in_channels
        co = oc_per_col

        elem_wt = of_wt.acquire(1)
        for _ in range_(y_dim):
            elem_in = of_in.acquire(1)
            elem_out = of_out.acquire(1)
            kernel_fn(elem_in, elem_wt, elem_out, x_dim, ci, co)
            of_in.release(1)
            of_out.release(1)
        of_wt.release(1)

    # Workers
    workers = [
        Worker(
            core_fn,
            [
                in_fifos[i].cons(),
                wt_fifos[i].cons(),
                out_fifos[i].prod(),
                conv2dk1_kernel,
            ],
        )
        for i in range(num_columns)
    ]

    # Input TAPs: every column gets the entire input tensor
    # Input TAPs: all columns receive the same contiguous input tensor.
    # Hardware constraint: all 4 BD sizes <= 64.
    # Since the input is fully contiguous, use a linear 4D factorization.
    in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input_size)
    in_taps = [
        TensorAccessPattern(
            (1, total_input_size),
            offset=0,
            sizes=[in_d3, in_d2, in_d1, in_d0],
            strides=[in_d2 * in_d1 * in_d0, in_d1 * in_d0, in_d0, 1],
        )
        for _ in range(num_columns)
    ]

    # Weight TAPs: each column's weights are a contiguous slice of the weight tensor.
    # Use linear 4D factorization of weights_per_col.
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

    # Output TAPs: each column drains its own contiguous chunk of the output tensor.
    # For single-column (num_columns=1): entire output is contiguous.
    # For multi-column: column i's output rows are interleaved with other columns'.
    # The per-column output per row (output_row_size_per_col elements) is contiguous,
    # but rows are separated by output_row_total = out_channels * width elements.
    # Express as [height, per_row_d2, per_row_d1, per_row_d0] with strided rows,
    # ensuring all dims <= 64.  height must also be <= 64; for larger heights use
    # the contiguous path (num_columns=1 where output is fully contiguous).
    output_row_total = out_channels * width
    if num_columns == 1:
        # Output is fully contiguous for single-column designs
        out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output_size)
        out_taps = [
            TensorAccessPattern(
                (1, total_output_size),
                offset=0,
                sizes=[out_d3, out_d2, out_d1, out_d0],
                strides=[out_d2 * out_d1 * out_d0, out_d1 * out_d0, out_d0, 1],
            )
        ]
    else:
        # Multi-column: strided output. height must be <= 64 for BD d3.
        assert height <= _BD_WRAP_MAX, (
            f"height={height} > {_BD_WRAP_MAX} not supported for multi-column conv2d. "
            "Use num_columns=1 or reduce spatial dimensions."
        )
        n_oc_groups = oc_per_col // 8
        per_row = output_row_size_per_col  # oc_per_col * width (contiguous per row)
        pr_d2, pr_d1, pr_d0 = _factorize_tensor(per_row)[1:]  # 3 inner dims
        out_taps = [
            TensorAccessPattern(
                (1, total_output_size),
                offset=i * oc_per_col * width,
                sizes=[height, pr_d2, pr_d1, pr_d0],
                strides=[output_row_total, pr_d1 * pr_d0, pr_d0, 1],
            )
            for i in range(num_columns)
        ]

    # Runtime sequence
    rt = Runtime()
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (inp, wts, out):
        rt.start(*workers)

        tg = rt.task_group()

        # Fill input FIFOs (all columns get the same input)
        for i in range(num_columns):
            rt.fill(in_fifos[i].prod(), inp, in_taps[i], task_group=tg)

        # Fill weight FIFOs (each column gets its own weights)
        for i in range(num_columns):
            rt.fill(wt_fifos[i].prod(), wts, wt_taps[i], task_group=tg)

        # Drain output FIFOs
        for i in range(num_columns):
            rt.drain(out_fifos[i].cons(), out, out_taps[i], wait=True, task_group=tg)

        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


def my_conv2d_k3(
    dev,
    height,
    width,
    in_channels,
    out_channels,
    kernel_size,
    stride,
    has_bias,
    activation,
    num_columns,
):
    """ObjectFIFO design for 3x3 conv2d on NPU2 with bfloat16.

    Data layout (tiled, groups of 8 channels):
      Input row:   [C_in/8, W, 8]
      Weights:     [C_out/8, C_in/8, 3, 3, 8, 8]
      Output row:  [C_out/8, W_out, 8]

    The core uses a sliding window pattern over input rows.
    Three input rows are needed at a time for the 3x3 kernel.
    Vertical border handling uses check=0 (top), 1 (middle), 2 (bottom).
    Horizontal padding is handled inside the kernel.

    Supports stride=1 (same spatial dims) and stride=2 (halved spatial dims).
    Bias is applied in Python after the NPU computation.
    """
    xfr_dtype = bfloat16

    assert kernel_size == 3, "my_conv2d_k3 only supports kernel_size=3"
    assert stride in (1, 2), "Only stride 1 and 2 supported for 3x3 conv"
    assert in_channels % 8 == 0, "in_channels must be a multiple of 8"
    assert out_channels % 8 == 0, "out_channels must be a multiple of 8"
    assert (
        out_channels % num_columns == 0
    ), "out_channels must be divisible by num_columns"
    assert height >= 2, "height must be >= 2 for 3x3 conv"

    if stride == 2:
        assert height % 2 == 0, "height must be even for stride=2"
        assert width % 2 == 0, "width must be even for stride=2"

    # Output spatial dims
    out_h = height if stride == 1 else height // 2
    out_w = width if stride == 1 else width // 2

    # Per-column output channels
    oc_per_col = out_channels // num_columns

    # Sizes for one row of data
    input_row_size = in_channels * width  # [C_in/8, W, 8] flattened
    output_row_size_per_col = oc_per_col * out_w  # per column

    # Weight size per column: [oc_per_col/8, C_in/8, 3, 3, 8, 8]
    weights_per_col = oc_per_col * in_channels * 9  # 3x3 = 9 positions * 64

    # When bias+SiLU is fused, bias is packed at the end of each column's weights
    fused = has_bias and activation == "silu"
    if fused:
        weights_per_col += oc_per_col

    # Total tensor sizes for runtime sequence arguments
    total_input_size = in_channels * height * width
    total_weights_size = weights_per_col * num_columns
    total_output_size = out_channels * out_h * out_w

    # Type definitions for ObjectFIFOs
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_row_size_per_col,), np.dtype[xfr_dtype]]
    weights_ty = np.ndarray[(weights_per_col,), np.dtype[xfr_dtype]]

    # L3 (DDR) tensor types for runtime sequence
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    weights_l3_ty = np.ndarray[(total_weights_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

    if dev == "npu":
        dev_ty = NPU1()
    else:
        dev_ty = NPU2()

    # Kernel declaration - 3x3 conv takes 3 line pointers
    # Select fused bias+SiLU variant when requested
    fused = has_bias and activation == "silu"
    if stride == 1:
        k3_name = "conv2dk3_bf16_bias_silu" if fused else "conv2dk3_bf16"
        conv2dk3_kernel = Kernel(
            k3_name,
            "conv2dk3_bf16.o",
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
            ],
        )
    else:
        k3s2_name = "conv2dk3s2_bf16_bias_silu" if fused else "conv2dk3s2_bf16"
        conv2dk3_kernel = Kernel(
            k3s2_name,
            "conv2dk3_bf16.o",
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
            ],
        )

    # ObjectFIFOs per column
    # Input FIFO needs depth >= 4 for sliding window (3 active + 1 prefetch)
    in_fifos = [
        ObjectFifo(input_row_ty, name=f"in_{i}", depth=4) for i in range(num_columns)
    ]
    wt_fifos = [
        ObjectFifo(weights_ty, name=f"wt_{i}", depth=1) for i in range(num_columns)
    ]
    out_fifos = [
        ObjectFifo(output_row_ty, name=f"out_{i}", depth=2) for i in range(num_columns)
    ]

    if stride == 1:
        # Stride-1 core function using sliding window pattern from bottleneck.
        # Pattern: top (acquire 2), middle (acquire 3, release 1), bottom (acquire 2).
        def core_fn_s1(of_in, of_wt, of_out, kernel_fn):
            y_dim = height
            x_dim = width
            ci = in_channels
            co = oc_per_col

            elem_wt = of_wt.acquire(1)

            # Top row: check=0, window is (padding, row0, row1)
            elems = of_in.acquire(2)
            elem_out = of_out.acquire(1)
            kernel_fn(elems[0], elems[0], elems[1], elem_wt, elem_out, x_dim, ci, co, 0)
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
                )
                of_in.release(1)
                of_out.release(1)

            # Bottom row: check=2, window is (rowH-2, rowH-1, padding)
            elems = of_in.acquire(2)
            elem_out = of_out.acquire(1)
            kernel_fn(elems[0], elems[1], elems[1], elem_wt, elem_out, x_dim, ci, co, 2)
            of_in.release(2)
            of_out.release(1)

            of_wt.release(1)

        core_fn = core_fn_s1
    else:
        # Stride-2 core function.
        # Output height = height // 2.
        # Output row k corresponds to input center y=2*k with padding=1.
        #   k=0: center=0, window=(-1,0,1) -> check=0, lines=(_, row0, row1)
        #   k=1..out_h-1: center=2k, window=(2k-1, 2k, 2k+1) -> check=1
        #
        # Sliding window advances by 2 rows between output rows.
        def core_fn_s2(of_in, of_wt, of_out, kernel_fn):
            x_dim = width
            ci = in_channels
            co = oc_per_col
            oh = out_h

            elem_wt = of_wt.acquire(1)

            # Top row (output row 0): check=0
            # Window: (padding, row0, row1), pass row0 as both line0 and line1
            elems = of_in.acquire(2)
            elem_out = of_out.acquire(1)
            kernel_fn(elems[0], elems[0], elems[1], elem_wt, elem_out, x_dim, ci, co, 0)
            # Release row 0 (we need row 1 for next window)
            of_in.release(1)
            of_out.release(1)

            # Middle rows (output rows 1 to out_h-1): check=1
            # Each needs 3 rows: (2k-1, 2k, 2k+1)
            # After top: we hold row 1. Need rows 1, 2, 3.
            # Acquire(3) -> hold rows 1, 2, 3.
            # Process, release(2) -> hold row 3.
            # Next: acquire(3) -> hold rows 3, 4, 5. Process, release(2).
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
                )
                of_in.release(2)
                of_out.release(1)

            # Release the last held row
            of_in.release(1)
            of_wt.release(1)

        core_fn = core_fn_s2

    # Workers
    workers = [
        Worker(
            core_fn,
            [
                in_fifos[i].cons(),
                wt_fifos[i].cons(),
                out_fifos[i].prod(),
                conv2dk3_kernel,
            ],
        )
        for i in range(num_columns)
    ]

    # Input TAPs: all columns receive the same contiguous input tensor.
    # Hardware constraint: all 4 BD sizes <= 64.
    # Since input is fully contiguous, use linear 4D factorization.
    in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input_size)
    in_taps = [
        TensorAccessPattern(
            (1, total_input_size),
            offset=0,
            sizes=[in_d3, in_d2, in_d1, in_d0],
            strides=[in_d2 * in_d1 * in_d0, in_d1 * in_d0, in_d0, 1],
        )
        for _ in range(num_columns)
    ]

    # Weight TAPs: each column's weights are a contiguous slice.
    # Use linear 4D factorization of weights_per_col.
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

    # Output TAPs: each column drains its own contiguous chunk of the output tensor.
    output_row_total = out_channels * out_w
    if num_columns == 1:
        # Single-column: output is fully contiguous, use linear factorization.
        out_d3, out_d2, out_d1, out_d0 = _factorize_tensor(total_output_size)
        out_taps = [
            TensorAccessPattern(
                (1, total_output_size),
                offset=0,
                sizes=[out_d3, out_d2, out_d1, out_d0],
                strides=[out_d2 * out_d1 * out_d0, out_d1 * out_d0, out_d0, 1],
            )
        ]
    else:
        # Multi-column: column i's rows are interleaved (strided).
        # out_h must be <= 64 for d3 constraint.
        assert out_h <= _BD_WRAP_MAX, (
            f"out_h={out_h} > {_BD_WRAP_MAX} not supported for multi-column k3 conv2d. "
            "Use num_columns=1."
        )
        per_row = output_row_size_per_col
        _, pr_d2, pr_d1, pr_d0 = _factorize_tensor(per_row)
        out_taps = [
            TensorAccessPattern(
                (1, total_output_size),
                offset=i * oc_per_col * out_w,
                sizes=[out_h, pr_d2, pr_d1, pr_d0],
                strides=[output_row_total, pr_d1 * pr_d0, pr_d0, 1],
            )
            for i in range(num_columns)
        ]

    # Runtime sequence
    rt = Runtime()
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (inp, wts, out):
        rt.start(*workers)

        tg = rt.task_group()

        # Fill input FIFOs (all columns get the same input)
        for i in range(num_columns):
            rt.fill(in_fifos[i].prod(), inp, in_taps[i], task_group=tg)

        # Fill weight FIFOs (each column gets its own weights)
        for i in range(num_columns):
            rt.fill(wt_fifos[i].prod(), wts, wt_taps[i], task_group=tg)

        # Drain output FIFOs
        for i in range(num_columns):
            rt.drain(out_fifos[i].cons(), out, out_taps[i], wait=True, task_group=tg)

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
    p.add_argument("--in-channels", required=True, type=int)
    p.add_argument("--out-channels", required=True, type=int)
    p.add_argument("--kernel-size", default=1, type=int)
    p.add_argument("--stride", default=1, type=int)
    p.add_argument("--has-bias", default=0, type=int)
    p.add_argument("--activation", default="none", type=str)
    p.add_argument("--num-columns", default=1, type=int)
    p.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        help="Output file path for the generated MLIR module",
    )

    opts = p.parse_args(sys.argv[1:])

    activation = None if opts.activation == "none" else opts.activation

    design_fn = my_conv2d if opts.kernel_size == 1 else my_conv2d_k3
    module = design_fn(
        opts.device,
        opts.height,
        opts.width,
        opts.in_channels,
        opts.out_channels,
        opts.kernel_size,
        opts.stride,
        bool(opts.has_bias),
        activation,
        opts.num_columns,
    )

    if opts.output_file_path:
        output_file_path = Path(opts.output_file_path)
        with open(output_file_path, "w") as f:
            f.write(str(module))
    else:
        print(module)
