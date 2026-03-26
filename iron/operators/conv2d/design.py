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
    # reads only wt_chunk_elems valid elements.  Applied to both streaming
    # and non-streaming paths so unfactorizable sizes (e.g. 18448=16×1153
    # where 1153 is prime) are handled transparently.
    (
        wt_chunk_transfer,
        _wt_cd3,
        _wt_cd2,
        _wt_cd1,
        _wt_cd0,
    ) = _factorize_tensor_padded(wt_chunk_elems)

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
        weights_ty = np.ndarray[(wt_chunk_transfer,), np.dtype[xfr_dtype]]
        weights_per_col = wt_chunk_transfer
        total_weights_size = weights_per_col * num_columns

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
        wt_taps = [
            [
                TensorAccessPattern(
                    (1, total_weights_size),
                    offset=i * weights_per_col,
                    sizes=[_wt_cd3, _wt_cd2, _wt_cd1, _wt_cd0],
                    strides=[
                        _wt_cd2 * _wt_cd1 * _wt_cd0,
                        _wt_cd1 * _wt_cd0,
                        _wt_cd0,
                        1,
                    ],
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

    # --- L1 budget decision: OC streaming, IC streaming, or both ---
    # L1 = 65536 bytes.  Budget:
    #   input_fifo  = input_depth * in_channels * width * 2  (bf16, non-IC)
    #   weight_fifo = 1 * (oc_chunk * in_channels * 9 [+ oc_chunk bias]) * 2
    #   output_fifo = 2 * oc_chunk * out_w * 2               (depth=2)
    #   overhead    = 1040  (stack + misc)
    #
    # The k3 sliding window requires 3 rows simultaneously:
    #   depth=4 is preferred (3 active + 1 prefetch for overlap).
    #   depth=3 is the minimum correct depth (no prefetch).
    #
    # Streaming modes:
    #   OC streaming: split oc_per_col into n_oc_groups × oc_chunk
    #   IC streaming: DEPRECATED — see note below.
    #
    # IC streaming NOTE: The previous IC streaming implementation was
    # mathematically broken.  It split in_channels into ic_chunk-wide groups
    # and used a static single-row _ic_accum buffer.  IC group 0 processed
    # all H rows, overwriting _ic_accum for each row; by the time IC group 1
    # started processing row 0, _ic_accum contained row H-1's partial sums.
    # Fixing this requires full-height accumulation (H * oc_chunk * out_w *
    # 4 bytes = up to 1MB for the 80x80 config) which doesn't fit in L1 (64KB).
    # IC streaming is therefore DISABLED in this design.  Large in_channels are
    # handled by reducing oc_chunk (OC streaming) and using depth=3 input FIFO.
    #
    # BD budget: 2 * n_oc_groups + 1 ≤ 16
    k_elems = kernel_size * kernel_size  # 9
    use_weight_streaming = False
    use_ic_streaming = False
    n_oc_groups = 1
    n_ic_groups = 1
    oc_chunk = oc_per_col
    ic_chunk = in_channels
    input_depth = 4  # Default; may be reduced to 3 if needed

    # ShimDMA BD limit per shim tile.
    _MAX_BDS = 16

    # Try to find oc_chunk that fits in L1.  First try with depth=4 (preferred),
    # then depth=3 (minimum correct, no prefetch, same correctness).
    # IC streaming is disabled (see note above).
    found = False

    for try_depth in [4, 3]:
        # The AIE ObjectFIFO allocator uses (depth+1) physical buffers for the
        # sliding window input FIFO.  Budget with (depth+1) × element_size.
        phys_bufs = try_depth + 1
        input_fbs = phys_bufs * in_channels * width * 2
        avail = 65536 - 1040 - input_fbs
        if avail <= 0:
            continue
        # Try largest OC chunk first
        for try_oc in range(oc_per_col, 0, -8):
            if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_elems = try_oc * in_channels * k_elems
            if fused:
                wt_elems += try_oc  # bias packed at end of weight buffer
            wt_bytes = wt_elems * 2
            out_bytes = 2 * try_oc * out_w * 2
            if wt_bytes + out_bytes > avail:
                continue
            n_oc = oc_per_col // try_oc
            # BD budget: n_oc input fills + n_oc weight fills + 1 drain
            bd_estimate = 2 * n_oc + 1
            if bd_estimate <= _MAX_BDS:
                oc_chunk = try_oc
                ic_chunk = in_channels
                n_oc_groups = n_oc
                n_ic_groups = 1
                input_depth = try_depth
                found = True
                break
        if found:
            break

    if not found:
        raise ValueError(
            f"k3 conv2d infeasible even with IC+OC streaming: "
            f"in_channels={in_channels}, oc_per_col={oc_per_col}, width={width}. "
            f"Cannot satisfy L1 budget (64KB) and BD limit (16) simultaneously."
        )

    if oc_chunk < oc_per_col:
        use_weight_streaming = True
        n_oc_groups = oc_per_col // oc_chunk
    if ic_chunk < in_channels:
        use_ic_streaming = True
        n_ic_groups = in_channels // ic_chunk

    # Per-IC-group, per-OC-group weight chunk size (elements).
    # When IC streaming: weights for one (oc_chunk, ic_chunk) sub-block.
    # Bias is only packed in the LAST IC group's weight buffer.
    wt_chunk_elems = oc_chunk * ic_chunk * k_elems
    # Bias is appended to the last IC group's weights only.
    # For IC streaming this means the last-IC-group weight chunk is larger.
    # To keep a uniform FIFO element size we pack bias into ALL IC group
    # chunks (last gets real bias, others get zero bias). The kernel uses
    # ic_group_idx to know whether to apply it.
    if fused:
        wt_chunk_elems += oc_chunk  # bias occupies last oc_chunk elements

    # Transfer size: may be padded up for BD factorization.
    (
        wt_chunk_transfer,
        _wt_cd3,
        _wt_cd2,
        _wt_cd1,
        _wt_cd0,
    ) = _factorize_tensor_padded(wt_chunk_elems)

    # Input FIFO row size: when IC streaming, only ic_chunk channels per row.
    ic_input_row_size = ic_chunk * width  # [ic_chunk/8, W, 8]

    # Output FIFO element size: oc_chunk channels per output row element.
    output_elem_size = oc_chunk * out_w

    # Total tensor sizes for runtime sequence arguments
    total_input_size = in_channels * height * width
    total_output_size = out_channels * out_h * out_w

    # Total weights: n_oc_groups × n_ic_groups × wt_chunk_transfer per column.
    weights_per_col = n_oc_groups * n_ic_groups * wt_chunk_transfer
    total_weights_size = weights_per_col * num_columns

    # Type definitions for ObjectFIFOs
    # Input FIFO: ic_chunk channels per row (may be smaller than in_channels)
    input_row_ty = np.ndarray[(ic_input_row_size,), np.dtype[xfr_dtype]]
    output_row_ty = np.ndarray[(output_elem_size,), np.dtype[xfr_dtype]]
    weights_ty = np.ndarray[(wt_chunk_transfer,), np.dtype[xfr_dtype]]

    # L3 (DDR) tensor types for runtime sequence
    input_l3_ty = np.ndarray[(total_input_size,), np.dtype[xfr_dtype]]
    weights_l3_ty = np.ndarray[(total_weights_size,), np.dtype[xfr_dtype]]
    output_l3_ty = np.ndarray[(total_output_size,), np.dtype[xfr_dtype]]

    if dev == "npu":
        dev_ty = NPU1()
    else:
        dev_ty = NPU2()

    # Kernel declaration - 3x3 conv takes 3 line pointers.
    # When IC streaming is active, use the icstream variant which takes two
    # extra int32 parameters: ic_group_idx and n_ic_groups.
    fused = has_bias and activation == "silu"
    if use_ic_streaming:
        # IC streaming uses two kernel entry points from the same .o:
        #   accum: WITH output pointer — writes bfloat16 partial sums
        #   flush: WITH output pointer — last IC group adds bias + SiLU
        # Both entry points acquire the output FIFO so the drain TAP sees
        # only the final result (released once per row after all IC groups).
        conv2dk3_accum = Kernel(
            "conv2dk3_bf16_accum_icstream",
            "conv2dk3_bf16_icstream.o",
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
                np.int32,  # ic_group_idx
                np.int32,  # n_ic_groups
            ],
        )
        conv2dk3_flush = Kernel(
            "conv2dk3_bf16_flush_icstream",
            "conv2dk3_bf16_icstream.o",
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
                np.int32,  # ic_group_idx
                np.int32,  # n_ic_groups
            ],
        )
    elif stride == 1:
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

    # ObjectFIFOs per column.
    # Input FIFO depth:
    #   Non-IC streaming: depth=4 (3-row sliding window + 1 prefetch slot)
    #   IC streaming: depth = 3 * n_ic_groups (HEIGHT-outer sliding window
    #     needs n_ic_groups elements per spatial row × 3 rows simultaneously)
    in_fifos = [
        ObjectFifo(input_row_ty, name=f"in_{i}", depth=input_depth)
        for i in range(num_columns)
    ]

    # Weight FIFO: one OC-group × IC-group chunk per element.
    wt_fifos = [
        ObjectFifo(weights_ty, name=f"wt_{i}", depth=1)
        for i in range(num_columns)
    ]

    out_fifos = [
        ObjectFifo(output_row_ty, name=f"out_{i}", depth=2) for i in range(num_columns)
    ]

    if use_ic_streaming:
        # IC+OC streaming stride-1 core function.
        #
        # Two kernel entry points (same .o file):
        #   kernel_accum: WITH output pointer — writes bfloat16 partial sums
        #   kernel_flush: WITH output pointer — final IC group adds bias + SiLU
        #
        # HEIGHT-outer, IC-inner execution: for each spatial output row, ALL
        # IC groups are processed before moving to the next row.  This ensures
        # the bfloat16 partial sum stored in the output FIFO element is correct
        # for each row (reset for ic_group_idx==0, accumulated for subsequent).
        #
        # The output FIFO element is acquired ONCE per spatial row, kept
        # through all n_ic_groups kernel calls, then released.  The drain DMA
        # therefore sees one final-result element per row (not intermediate sums).
        #
        # The input FIFO has depth = 3 * n_ic_groups.  For a sliding window
        # at spatial row h, we hold n_ic_groups elements per window position:
        #   elems[0..n_ic-1]         = prev row (h-1), one per IC group
        #   elems[n_ic..2*n_ic-1]    = curr row (h),   one per IC group
        #   elems[2*n_ic..3*n_ic-1]  = next row (h+1), one per IC group
        # For IC group g: line0=elems[g], line1=elems[n_ic+g], line2=elems[2*n_ic+g].

        n_ic = n_ic_groups

        def core_fn_ic(of_in, of_wt, kernel_accum, kernel_flush, of_out):
            y_dim = height
            x_dim = width
            ci = ic_chunk
            co = oc_chunk

            for _ in range_(n_oc_groups):
                # TOP ROW: acquire 2*n_ic input elements (curr + next row batches)
                elems = of_in.acquire(2 * n_ic)
                elem_out = of_out.acquire(1)
                # Process all non-last IC groups (accum)
                for g in range(n_ic - 1):
                    elem_wt = of_wt.acquire(1)
                    kernel_accum(
                        elems[g], elems[g], elems[n_ic + g], elem_wt, elem_out,
                        x_dim, ci, co, 0, g, n_ic,
                    )
                    of_wt.release(1)
                # Last IC group (flush)
                elem_wt = of_wt.acquire(1)
                kernel_flush(
                    elems[n_ic - 1], elems[n_ic - 1], elems[2 * n_ic - 1],
                    elem_wt, elem_out,
                    x_dim, ci, co, 0, n_ic - 1, n_ic,
                )
                of_wt.release(1)
                of_out.release(1)

                # MIDDLE ROWS: acquire n_ic more each iteration to extend window
                for _ in range_(y_dim - 2):
                    elems = of_in.acquire(3 * n_ic)
                    elem_out = of_out.acquire(1)
                    for g in range(n_ic - 1):
                        elem_wt = of_wt.acquire(1)
                        kernel_accum(
                            elems[g], elems[n_ic + g], elems[2 * n_ic + g],
                            elem_wt, elem_out,
                            x_dim, ci, co, 1, g, n_ic,
                        )
                        of_wt.release(1)
                    elem_wt = of_wt.acquire(1)
                    kernel_flush(
                        elems[n_ic - 1], elems[2 * n_ic - 1], elems[3 * n_ic - 1],
                        elem_wt, elem_out,
                        x_dim, ci, co, 1, n_ic - 1, n_ic,
                    )
                    of_wt.release(1)
                    of_out.release(1)
                    of_in.release(n_ic)

                # BOTTOM ROW: hold 2*n_ic elements; release after
                elems = of_in.acquire(2 * n_ic)
                elem_out = of_out.acquire(1)
                for g in range(n_ic - 1):
                    elem_wt = of_wt.acquire(1)
                    kernel_accum(
                        elems[g], elems[n_ic + g], elems[n_ic + g],
                        elem_wt, elem_out,
                        x_dim, ci, co, 2, g, n_ic,
                    )
                    of_wt.release(1)
                elem_wt = of_wt.acquire(1)
                kernel_flush(
                    elems[n_ic - 1], elems[2 * n_ic - 1], elems[2 * n_ic - 1],
                    elem_wt, elem_out,
                    x_dim, ci, co, 2, n_ic - 1, n_ic,
                )
                of_wt.release(1)
                of_out.release(1)
                of_in.release(2 * n_ic)

        core_fn = core_fn_ic
    elif stride == 1:
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
    if use_ic_streaming:
        # IC streaming: two kernel entry points (accum + flush) from the same .o.
        # core_fn_ic signature: (of_in, of_wt, kernel_accum, kernel_flush, of_out)
        workers = [
            Worker(
                core_fn,
                [
                    in_fifos[i].cons(),
                    wt_fifos[i].cons(),
                    conv2dk3_accum,
                    conv2dk3_flush,
                    out_fifos[i].prod(),
                ],
            )
            for i in range(num_columns)
        ]
    else:
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

    # Input TAPs: all columns receive the same input.
    # When IC streaming, each IC group streams ic_chunk channels = [height, ic_chunk*width].
    # The input tensor layout is [C_in/8, H, W, 8] tiled, but we've flattened as
    # [H, C_in/8, W, 8] per row.  So IC groups are contiguous slices:
    #   IC group g: offset = g * ic_chunk * height * width
    if use_ic_streaming:
        # Consolidated input TAP: a SINGLE fill covers ALL IC groups for
        # the full height.  The 4D TAP uses HEIGHT-outer, IC-inner ordering
        # so the FIFO delivers:
        #   row0_IC0, row0_IC1, ..., row0_IC(n-1),
        #   row1_IC0, row1_IC1, ..., row1_IC(n-1),
        #   ...
        # This matches the HEIGHT-outer core body which acquires n_ic elements
        # per spatial row (one per IC group) for the sliding window.
        #
        # 4D TAP: [height, n_ic_groups, ic_d1, ic_d0]
        # Strides: [full_row_stride, ic_chunk*width, ic_d0, 1]
        #
        # In the [H, C/8, W, 8] tiled layout:
        #   Row h, IC group g: offset = h * (C_in/8 * W * 8) + g * (ic_chunk/8 * W * 8)
        #                             = h * full_row_stride + g * ic_chunk * width
        #
        # All OC groups re-stream the same input, so the same TAP is used
        # for all n_oc_groups fills.
        full_row_stride = in_channels * width  # row-to-row stride in tiled layout
        ic_slice_size = ic_chunk * width       # elements per IC group per row

        # Factor ic_slice_size into d1 × d0 (d0 even, both ≤ 1023).
        _D0_MAX = 1023
        _ic_d0 = min(ic_slice_size, _D0_MAX)
        if _ic_d0 % 2 != 0:
            _ic_d0 -= 1
        while _ic_d0 >= 2 and ic_slice_size % _ic_d0 != 0:
            _ic_d0 -= 2
        assert _ic_d0 >= 2, (
            f"Cannot factorize ic_slice_size={ic_slice_size} into valid BD dims"
        )
        _ic_d1 = ic_slice_size // _ic_d0
        assert _ic_d1 <= 1023, (
            f"ic_slice d1={_ic_d1} exceeds 1023 for ic_slice={ic_slice_size}"
        )

        assert n_ic_groups <= _BD_WRAP_MAX, (
            f"n_ic_groups={n_ic_groups} exceeds BD d3 limit {_BD_WRAP_MAX}"
        )
        assert height <= 1023, (
            f"height={height} exceeds BD d2 limit 1023 for IC streaming"
        )

        # Build height-split input TAPs: each TAP covers at most _BD_WRAP_MAX rows.
        # TAP layout: sizes=[chunk_h, n_ic_groups, _ic_d1, _ic_d0]
        # Strides: [full_row_stride, ic_slice, _ic_d0, 1]
        # This gives HEIGHT-outer, IC-inner delivery: for row h in chunk, for IC group g.
        # d3 = chunk_h ≤ _BD_WRAP_MAX ✓; d2 = n_ic_groups ≤ 1023 ✓.
        h_factor = (height + _BD_WRAP_MAX - 1) // _BD_WRAP_MAX
        h_chunk = (height + h_factor - 1) // h_factor  # rows per chunk (≤ _BD_WRAP_MAX)
        in_taps_per_col = []
        for chunk_start in range(0, height, h_chunk):
            chunk_h = min(h_chunk, height - chunk_start)
            assert chunk_h <= _BD_WRAP_MAX, (
                f"IC streaming input chunk_h={chunk_h} > BD d3 limit {_BD_WRAP_MAX}"
            )
            in_taps_per_col.append(
                TensorAccessPattern(
                    (1, total_input_size),
                    offset=chunk_start * full_row_stride,
                    sizes=[chunk_h, n_ic_groups, _ic_d1, _ic_d0],
                    strides=[full_row_stride, ic_chunk * width, _ic_d0, 1],
                )
            )
        in_taps = [
            list(in_taps_per_col) * n_oc_groups
            for _ in range(num_columns)
        ]
    else:
        in_d3, in_d2, in_d1, in_d0 = _factorize_tensor(total_input_size)
        in_taps = [
            [
                TensorAccessPattern(
                    (1, total_input_size),
                    offset=0,
                    sizes=[in_d3, in_d2, in_d1, in_d0],
                    strides=[in_d2 * in_d1 * in_d0, in_d1 * in_d0, in_d0, 1],
                )
            ]
            for _ in range(num_columns)
        ]

    # Weight TAPs.
    wt_taps = []
    if use_ic_streaming:
        # IC streaming (HEIGHT-outer): the weight chunks must be delivered
        # once per spatial row per OC group, repeating the same
        # n_oc_groups * n_ic_groups chunks for every row.
        #
        # Total weight FIFO pushes per column:
        #   height * n_oc_groups * n_ic_groups
        # Each push = wt_chunk_transfer elements.
        #
        # 4D TAP with stride=0 for the height dimension repeats the same
        # n_oc_groups * n_ic_groups * wt_chunk_transfer elements height times:
        #   [height, wt_d3, wt_d2_rest_d1, wt_d0]
        #   strides=[0, wt_d2_rest_d1 * wt_d0, wt_d0, 1]
        #
        # The weight data per column is: weights_per_col =
        #   n_oc_groups * n_ic_groups * wt_chunk_transfer elements.
        # We factorize weights_per_col into (d3, d1*d0) where all dims ≤ BD limits.
        # Then use height as the outermost dimension with stride=0.
        #
        # BD wrap constraints: all sizes ≤ 1023 (sizes[3] / d3 ≤ 64 for outermost).
        # height ≤ 64 constraint only applies when height is the outermost dim
        # with stride != 0.  With stride=0, the outermost dim repeats within
        # the same data region; the hardware BD allows size up to 64 for d3.
        # We factorize height into factors ≤ 64 if needed.
        #
        # Approach: use sizes=[h_factor1, h_factor2, d1, d0] for the weight TAP,
        # where h_factor1 * h_factor2 = height and strides=[0, 0, d0, 1].
        # This repeats the innermost d1*d0 elements height times.
        #
        # Simpler approach: if height ≤ 64, use 4D TAP directly.
        # Otherwise factor height into two dims.
        _D0_MAX = 1023
        _wt_d0 = min(weights_per_col, _D0_MAX)
        if _wt_d0 % 2 != 0:
            _wt_d0 -= 1
        while _wt_d0 >= 2 and weights_per_col % _wt_d0 != 0:
            _wt_d0 -= 2
        assert _wt_d0 >= 2, (
            f"Cannot factorize weights_per_col={weights_per_col} for IC streaming weight TAP"
        )
        _wt_d1 = weights_per_col // _wt_d0
        assert _wt_d1 <= 1023, (
            f"IC streaming wt d1={_wt_d1} exceeds 1023"
        )

        # Factor height into two outer dims (each ≤ _BD_WRAP_MAX=64).
        _h1 = 1
        _h2 = height
        if height > _BD_WRAP_MAX:
            for f in range(2, height + 1):
                if height % f == 0 and f <= _BD_WRAP_MAX and height // f <= _BD_WRAP_MAX:
                    _h1 = f
                    _h2 = height // f
                    break
            assert _h1 * _h2 == height, (
                f"Cannot factor height={height} into two dims ≤ {_BD_WRAP_MAX}"
            )

        for i in range(num_columns):
            wt_taps.append(
                [
                    TensorAccessPattern(
                        (1, total_weights_size),
                        offset=i * weights_per_col,
                        sizes=[_h1, _h2, _wt_d1, _wt_d0],
                        strides=[0, 0, _wt_d0, 1],
                    )
                ]
            )
    else:
        # OC streaming (or no streaming): per-chunk TAPs.
        # Layout: [col][oc_g][ic_g] → offset = col*weights_per_col + (oc_g*n_ic_groups+ic_g)*wt_chunk_transfer
        for i in range(num_columns):
            col_taps = []
            for oc_g in range(n_oc_groups):
                for ic_g in range(n_ic_groups):
                    flat_g = oc_g * n_ic_groups + ic_g
                    col_taps.append(
                        TensorAccessPattern(
                            (1, total_weights_size),
                            offset=i * weights_per_col
                            + flat_g * wt_chunk_transfer,
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

    # Output TAPs: each column drains its own output.
    # With weight streaming, the FIFO produces output in OC-group order:
    #   group0: rows 0..out_h-1 (oc_chunk channels each)
    #   group1: rows 0..out_h-1 (next oc_chunk channels)
    #   ...
    # The TAP must scatter these to the correct positions in DDR.
    output_row_total = out_channels * out_w
    if use_ic_streaming or use_weight_streaming:
        # OC streaming only: [n_oc_groups, out_h, d1, d0] with strided placement.
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

        if use_ic_streaming:
            # IC+OC streaming fills.
            # IC streaming (HEIGHT-outer).
            # Weights: single fill per column with a repeat-height TAP (stride=0
            # on the outermost dim) so the same n_oc_groups*n_ic_groups weight
            # chunks are re-delivered for each spatial row.
            # Inputs: n_oc_groups fills per column, each streaming all height rows
            # of all IC groups in HEIGHT-outer, IC-inner order.
            for i in range(num_columns):
                rt.fill(wt_fifos[i].prod(), wts, wt_taps[i][0], task_group=tg)
                for tap_in in in_taps[i]:
                    rt.fill(in_fifos[i].prod(), inp, tap_in, task_group=tg)
        else:
            # OC streaming (or no streaming): re-stream input once per OC group,
            # then stream all weight chunks, then drain output.
            for _g in range(n_oc_groups):
                for i in range(num_columns):
                    rt.fill(in_fifos[i].prod(), inp, in_taps[i][0], task_group=tg)

            for i in range(num_columns):
                for tap in wt_taps[i]:
                    rt.fill(wt_fifos[i].prod(), wts, tap, task_group=tg)

        # Drain output FIFOs
        for i in range(num_columns):
            rt.drain(
                out_fifos[i].cons(), out, out_taps[i], wait=True, task_group=tg
            )

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
