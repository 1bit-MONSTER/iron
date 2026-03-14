# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
from pathlib import Path
import numpy as np
import argparse
import sys

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2, AnyMemTile
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


def _factorize_tensor_padded(
    total: int,
) -> tuple[int, int, int, int, int]:
    """Factor total elements into BD dims, padding if necessary.

    When the exact total is not BD-factorizable (e.g. contains a prime
    factor > 1023), pad up to the smallest factorizable value.

    Returns (padded_total, d3, d2, d1, d0) with d3*d2*d1*d0 == padded_total
    and padded_total >= total.
    """
    try:
        d3, d2, d1, d0 = _factorize_tensor(total)
        return (total, d3, d2, d1, d0)
    except ValueError:
        pass
    # Search upward in steps of 2 (must stay even for bf16 alignment)
    for padded in range(total + 2, total + 1024, 2):
        try:
            d3, d2, d1, d0 = _factorize_tensor(padded)
            return (padded, d3, d2, d1, d0)
        except ValueError:
            continue
    raise ValueError(
        f"Cannot find BD-factorizable padded size near total={total}"
    )


def _factorize_3d(total: int) -> tuple[int, int, int]:
    """Factor total into three BD dims (d2, d1, d0).

    Same constraints as _factorize_tensor but uses only 3 dimensions,
    leaving d3 free for the caller (e.g. for height in strided output TAPs).

    Returns (d2, d1, d0) with d2*d1*d0 == total.
    """
    _D0_MAX = 1023
    _D12_MAX = 1023

    # Find largest even d0 that divides total
    d0 = min(total, _D0_MAX)
    if d0 % 2 != 0:
        d0 -= 1
    while d0 >= 2:
        if total % d0 == 0:
            rest = total // d0
            # Split rest into d1 * d2
            d1 = min(rest, _D12_MAX)
            while d1 > 1 and rest % d1 != 0:
                d1 -= 1
            d2 = rest // d1
            if d2 <= _D12_MAX:
                return (d2, d1, d0)
        d0 -= 2

    raise ValueError(
        f"Cannot factorize total={total} into 3 valid BD dims "
        f"(d0 even and <={_D0_MAX}, d1,d2<={_D12_MAX})"
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

    if dev == "npu":
        dev_ty = NPU1()
    else:
        dev_ty = NPU2()

    # --- L1 budget check ---
    # Determine whether to route input through MemTile (depth=1 at L1)
    # and whether to stream weights through MemTile in OC-group chunks.
    # Phases:
    #   1. Direct DDR→L1 for both input (depth=2) and weights: cheapest.
    #   2. MemTile input (depth=1 at L1) + direct weights: saves input L1.
    #   3. MemTile input + MemTile weight streaming: for very large configs.
    use_memtile = False
    use_weight_streaming = False
    n_oc_groups = 1
    oc_chunk = oc_per_col

    # Phase 1: try without MemTile
    input_fbs = 2 * input_row_size * 2  # depth=2
    wt_fbs = weights_per_col * 2
    out_fbs = 2 * output_row_size_per_col * 2  # depth=2
    total_l1 = input_fbs + wt_fbs + out_fbs + 1040
    if total_l1 > 65536:
        # Phase 2: MemTile input routing (depth=1 at L1)
        use_memtile = True
        mt_input_fbs = 1 * input_row_size * 2
        mt_total = mt_input_fbs + wt_fbs + out_fbs + 1040
        if mt_total > 65536:
            # Phase 3: MemTile input + weight streaming
            # ShimDMA BD limit: n_oc_groups*2 + 1 <= 16.
            _MAX_BDS = 16
            avail = 65536 - 1040 - mt_input_fbs
            for try_oc in range(oc_per_col, 0, -8):
                if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                    continue
                wt_elems = try_oc * in_channels
                if fused_bias_silu:
                    wt_elems += try_oc
                wt_bytes = wt_elems * 2
                out_bytes = 2 * try_oc * width * 2
                if wt_bytes + out_bytes <= avail:
                    n_groups = oc_per_col // try_oc
                    if n_groups * 2 + 1 <= _MAX_BDS:
                        oc_chunk = try_oc
                        break
            if oc_chunk < oc_per_col:
                use_weight_streaming = True
                n_oc_groups = oc_per_col // oc_chunk

    # Per-OC-group weight chunk size (elements)
    wt_chunk_elems = oc_chunk * in_channels
    if fused_bias_silu:
        wt_chunk_elems += oc_chunk

    # Transfer size: may be padded up for BD factorization.
    # Padding is harmless — extra elements go into the FIFO but the kernel
    # reads only wt_chunk_elems valid elements.
    if use_weight_streaming:
        (
            wt_chunk_transfer,
            _wt_cd3,
            _wt_cd2,
            _wt_cd1,
            _wt_cd0,
        ) = _factorize_tensor_padded(wt_chunk_elems)
    else:
        wt_chunk_transfer = wt_chunk_elems

    # Output FIFO element size
    output_elem_size = oc_chunk * width

    # Type definitions for ObjectFIFOs — use padded transfer size for FIFO
    # element so the DMA can write the full padded chunk.
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_elem_size,), np.dtype[xfr_dtype]]
    if use_weight_streaming:
        weights_ty = np.ndarray[(wt_chunk_transfer,), np.dtype[xfr_dtype]]
        weights_per_col = n_oc_groups * wt_chunk_transfer
        total_weights_size = weights_per_col * num_columns
    else:
        weights_ty = np.ndarray[(weights_per_col,), np.dtype[xfr_dtype]]

    # L3 (DDR) tensor types for runtime sequence
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    weights_l3_ty = np.ndarray[(total_weights_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

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
    if use_memtile:
        # Route input through MemTile: DDR → MemTile (depth=2) → L1 (depth=1)
        in_l3_fifos = [
            ObjectFifo(input_row_ty, name=f"in_l3_{i}", depth=2)
            for i in range(num_columns)
        ]
        in_fifos = [
            in_l3_fifos[i].cons().forward(
                obj_type=input_row_ty,
                name=f"in_{i}",
                placement=AnyMemTile,
                depth=1,
            )
            for i in range(num_columns)
        ]
    else:
        in_l3_fifos = None
        in_fifos = [
            ObjectFifo(input_row_ty, name=f"in_{i}", depth=2)
            for i in range(num_columns)
        ]
    # Weight FIFO: direct DDR → L1.  When streaming, the FIFO element is one
    # OC-group chunk.  Multiple fill() calls deliver successive chunks.
    wt_fifos = [
        ObjectFifo(weights_ty, name=f"wt_{i}", depth=1)
        for i in range(num_columns)
    ]
    out_fifos = [
        ObjectFifo(output_row_ty, name=f"out_{i}", depth=2) for i in range(num_columns)
    ]

    # Core function: loop over OC groups (n_oc_groups times),
    # each group acquires a weight chunk and processes all rows.
    def core_fn(of_in, of_wt, of_out, kernel_fn):
        y_dim = height
        x_dim = width
        ci = in_channels
        co = oc_chunk

        for _ in range_(n_oc_groups):
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

    # Weight TAPs: each column's weights are a contiguous slice.
    # When streaming, use pre-computed padded BD dims from above.
    if use_weight_streaming:
        wt_taps = []
        for i in range(num_columns):
            col_taps = []
            for g in range(n_oc_groups):
                col_taps.append(
                    TensorAccessPattern(
                        (1, total_weights_size),
                        offset=i * weights_per_col + g * wt_chunk_transfer,
                        sizes=[_wt_cd3, _wt_cd2, _wt_cd1, _wt_cd0],
                        strides=[
                            _wt_cd2 * _wt_cd1 * _wt_cd0,
                            _wt_cd1 * _wt_cd0,
                            _wt_cd0,
                            1,
                        ],
                    )
                )
            wt_taps.append(col_taps)
    else:
        wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(weights_per_col)
        wt_taps = [
            [
                TensorAccessPattern(
                    (1, total_weights_size),
                    offset=i * weights_per_col,
                    sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                    strides=[wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1],
                )
            ]
            for i in range(num_columns)
        ]

    # Output TAPs
    output_row_total = out_channels * width
    if use_weight_streaming:
        # Streaming: [n_oc_groups, height, d1, d0] with strided placement.
        per_elem = output_elem_size  # oc_chunk * width
        pe_d0 = min(per_elem, 1023)
        if pe_d0 % 2 != 0:
            pe_d0 -= 1
        while pe_d0 >= 2 and per_elem % pe_d0 != 0:
            pe_d0 -= 2
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
                strides=[out_d2 * out_d1 * out_d0, out_d1 * out_d0, out_d0, 1],
            )
        ]
    else:
        per_row = output_row_size_per_col  # oc_per_col * width
        if height <= _BD_WRAP_MAX:
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
            h_outer = min(height, _BD_WRAP_MAX)
            while h_outer >= 1 and (
                height % h_outer != 0 or height // h_outer > 1023
            ):
                h_outer -= 1
            assert h_outer >= 1, (
                f"Cannot split height={height} into valid BD dims"
            )
            h_inner = height // h_outer
            _D0_MAX = 1023
            d0 = min(per_row, _D0_MAX)
            if d0 % 2 != 0:
                d0 -= 1
            while d0 >= 2 and per_row % d0 != 0:
                d0 -= 2
            assert d0 >= 2, (
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
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (inp, wts, out):
        rt.start(*workers)

        tg = rt.task_group()

        # Fill input FIFOs.  When weight streaming, re-stream input for each
        # OC group.  When using MemTile input, fill the L3 FIFOs.
        fill_in_fifos = in_l3_fifos if use_memtile else in_fifos
        for _g in range(n_oc_groups):
            for i in range(num_columns):
                rt.fill(fill_in_fifos[i].prod(), inp, in_taps[i], task_group=tg)

        # Fill weight FIFOs.  When streaming, one fill per OC group per column.
        for i in range(num_columns):
            for tap in wt_taps[i]:
                rt.fill(wt_fifos[i].prod(), wts, tap, task_group=tg)

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

    # --- L1 budget check: determine if weight streaming is needed ---
    # L1 = 65536 bytes.  Budget:
    #   input_fifo  = input_depth * input_row_size * 2  (bf16)
    #   weight_fifo = 1 * weight_chunk * 2              (depth=1 from MemTile)
    #   output_fifo = 2 * oc_chunk * out_w * 2          (depth=2)
    #   overhead    = 1040  (stack + misc)
    #
    # When all weights fit in L1 alongside input/output FIFOs, no streaming
    # is needed.  Otherwise, stream weights through MemTile in OC-group
    # chunks of size oc_chunk.
    k_elems = kernel_size * kernel_size  # 9
    use_weight_streaming = False
    n_oc_groups = 1
    oc_chunk = oc_per_col
    # Sliding window acquire(3) forces depth=4 (3 active + 1 prefetch).
    # The MLIR-AIE framework automatically upgrades depth to
    # max(depth, max_acquire + 1), so depth=3 is ineffective for k3.
    input_depth = 4

    # ShimDMA BD limit: each fill/drain uses 1 BD.  With weight streaming,
    # the runtime issues n_oc_groups input fills + n_oc_groups weight fills
    # + 1 output drain per column.  NPU2 ShimDMA has 16 BDs per tile.
    _MAX_BDS = 16

    input_fbs = input_depth * input_row_size * 2
    avail = 65536 - 1040 - input_fbs
    if avail > 0:
        for try_oc in range(oc_per_col, 0, -8):
            if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_elems = try_oc * in_channels * k_elems
            if fused:
                wt_elems += try_oc
            wt_bytes = wt_elems * 2
            out_bytes = 2 * try_oc * out_w * 2
            if wt_bytes + out_bytes <= avail:
                n_groups = oc_per_col // try_oc
                if n_groups * 2 + 1 <= _MAX_BDS:
                    oc_chunk = try_oc
                    break

    if oc_chunk < oc_per_col:
        use_weight_streaming = True
        n_oc_groups = oc_per_col // oc_chunk

    # Per-OC-group weight chunk size (elements)
    wt_chunk_elems = oc_chunk * in_channels * k_elems
    if fused:
        wt_chunk_elems += oc_chunk

    # Transfer size: may be padded up for BD factorization.
    if use_weight_streaming:
        (
            wt_chunk_transfer,
            _wt_cd3,
            _wt_cd2,
            _wt_cd1,
            _wt_cd0,
        ) = _factorize_tensor_padded(wt_chunk_elems)
    else:
        wt_chunk_transfer = wt_chunk_elems

    # Output FIFO element size: oc_chunk channels per element when streaming,
    # full oc_per_col when not streaming.
    output_elem_size = oc_chunk * out_w

    # Total tensor sizes for runtime sequence arguments
    total_input_size = in_channels * height * width
    total_output_size = out_channels * out_h * out_w

    # Type definitions for ObjectFIFOs — use padded transfer size for FIFO
    input_row_ty = np.ndarray[(input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_elem_size,), np.dtype[xfr_dtype]]
    if use_weight_streaming:
        weights_ty = np.ndarray[(wt_chunk_transfer,), np.dtype[xfr_dtype]]
        weights_per_col = n_oc_groups * wt_chunk_transfer
        total_weights_size = weights_per_col * num_columns
    else:
        weights_ty = np.ndarray[(weights_per_col,), np.dtype[xfr_dtype]]
        total_weights_size = weights_per_col * num_columns

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
    # Input FIFO: depth=input_depth for sliding window (3 active + prefetch).
    # When weight streaming needs tighter L1, input_depth may be 3 instead of 4.
    in_fifos = [
        ObjectFifo(input_row_ty, name=f"in_{i}", depth=input_depth)
        for i in range(num_columns)
    ]

    # Weight FIFO: direct DDR → L1.  When streaming, the FIFO element is one
    # OC-group chunk (wt_chunk_elems).  Multiple fill() calls in the runtime
    # sequence deliver successive OC-group chunks.
    wt_fifos = [
        ObjectFifo(weights_ty, name=f"wt_{i}", depth=1)
        for i in range(num_columns)
    ]

    out_fifos = [
        ObjectFifo(output_row_ty, name=f"out_{i}", depth=2) for i in range(num_columns)
    ]

    if stride == 1:
        # Stride-1 core function using sliding window pattern.
        # Pattern: top (acquire 2), middle (acquire 3, release 1), bottom (acquire 2).
        # When weight streaming: outer loop over n_oc_groups, each doing a full
        # sliding window pass.  Input is re-streamed for each OC group.
        def core_fn_s1(of_in, of_wt, of_out, kernel_fn):
            y_dim = height
            x_dim = width
            ci = in_channels
            co = oc_chunk

            for _ in range_(n_oc_groups):
                elem_wt = of_wt.acquire(1)

                # Top row: check=0, window is (padding, row0, row1)
                elems = of_in.acquire(2)
                elem_out = of_out.acquire(1)
                kernel_fn(
                    elems[0], elems[0], elems[1], elem_wt, elem_out, x_dim, ci, co, 0
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
                    )
                    of_in.release(1)
                    of_out.release(1)

                # Bottom row: check=2, window is (rowH-2, rowH-1, padding)
                elems = of_in.acquire(2)
                elem_out = of_out.acquire(1)
                kernel_fn(
                    elems[0], elems[1], elems[1], elem_wt, elem_out, x_dim, ci, co, 2
                )
                of_in.release(2)
                of_out.release(1)

                of_wt.release(1)

        core_fn = core_fn_s1
    else:
        # Stride-2 core function.
        # Output height = height // 2.
        # Sliding window advances by 2 rows between output rows.
        # When weight streaming: outer loop over n_oc_groups.
        def core_fn_s2(of_in, of_wt, of_out, kernel_fn):
            x_dim = width
            ci = in_channels
            co = oc_chunk
            oh = out_h

            for _ in range_(n_oc_groups):
                elem_wt = of_wt.acquire(1)

                # Top row (output row 0): check=0
                elems = of_in.acquire(2)
                elem_out = of_out.acquire(1)
                kernel_fn(
                    elems[0], elems[0], elems[1], elem_wt, elem_out, x_dim, ci, co, 0
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
    # When streaming, use pre-computed padded BD dims from above.
    if use_weight_streaming:
        wt_taps = []
        for i in range(num_columns):
            col_taps = []
            for g in range(n_oc_groups):
                col_taps.append(
                    TensorAccessPattern(
                        (1, total_weights_size),
                        offset=i * weights_per_col + g * wt_chunk_transfer,
                        sizes=[_wt_cd3, _wt_cd2, _wt_cd1, _wt_cd0],
                        strides=[
                            _wt_cd2 * _wt_cd1 * _wt_cd0,
                            _wt_cd1 * _wt_cd0,
                            _wt_cd0,
                            1,
                        ],
                    )
                )
            wt_taps.append(col_taps)
    else:
        wt_d3, wt_d2, wt_d1, wt_d0 = _factorize_tensor(weights_per_col)
        wt_taps = [
            [
                TensorAccessPattern(
                    (1, total_weights_size),
                    offset=i * weights_per_col,
                    sizes=[wt_d3, wt_d2, wt_d1, wt_d0],
                    strides=[wt_d2 * wt_d1 * wt_d0, wt_d1 * wt_d0, wt_d0, 1],
                )
            ]
            for i in range(num_columns)
        ]

    # Output TAPs: each column drains its own output.
    # With weight streaming, the FIFO produces output in OC-group order:
    #   group0: rows 0..out_h-1 (oc_chunk channels each)
    #   group1: rows 0..out_h-1 (next oc_chunk channels)
    #   ...
    # The TAP must scatter these to the correct positions in DDR.
    output_row_total = out_channels * out_w
    if use_weight_streaming:
        # Streaming: [n_oc_groups, out_h, d1, d0] with strided placement.
        per_elem = output_elem_size  # oc_chunk * out_w
        pe_d0 = min(per_elem, 1023)
        if pe_d0 % 2 != 0:
            pe_d0 -= 1
        while pe_d0 >= 2 and per_elem % pe_d0 != 0:
            pe_d0 -= 2
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
        # Multi-column without streaming: column i's rows are interleaved.
        per_row = output_row_size_per_col  # oc_per_col * out_w
        if out_h <= _BD_WRAP_MAX:
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
            h_outer = min(out_h, _BD_WRAP_MAX)
            while h_outer >= 1 and (
                out_h % h_outer != 0 or out_h // h_outer > 1023
            ):
                h_outer -= 1
            assert h_outer >= 1, (
                f"Cannot split out_h={out_h} into valid BD dims"
            )
            h_inner = out_h // h_outer
            _D0_MAX = 1023
            d0 = min(per_row, _D0_MAX)
            if d0 % 2 != 0:
                d0 -= 1
            while d0 >= 2 and per_row % d0 != 0:
                d0 -= 2
            assert d0 >= 2, (
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
    with rt.sequence(input_l3_ty, weights_l3_ty, output_l3_ty) as (inp, wts, out):
        rt.start(*workers)

        tg = rt.task_group()

        # Fill input FIFOs.  When weight streaming, re-stream input for each
        # OC group (the core processes all rows per OC group).
        for _g in range(n_oc_groups):
            for i in range(num_columns):
                rt.fill(in_fifos[i].prod(), inp, in_taps[i], task_group=tg)

        # Fill weight FIFOs.  When streaming, one fill per OC group per column.
        for i in range(num_columns):
            for tap in wt_taps[i]:
                rt.fill(wt_fifos[i].prod(), wts, tap, task_group=tg)

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
