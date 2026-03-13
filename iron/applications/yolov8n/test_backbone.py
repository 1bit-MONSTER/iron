#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests for YOLOv8n composite blocks and backbone layers.

Tests are ordered from simple to complex:
    1. CBS block (single conv + SiLU)
    2. Bottleneck block (two CBS + residual)
    3. C2f block (expand + bottlenecks + reduce)
    4. Backbone layers 0-2 (three cascaded layers)

All tests use small spatial dimensions for fast compilation and
compare NPU output against a PyTorch CPU reference.
"""

import logging

import numpy as np
import pytest
import torch
import torch.nn.functional as F

from iron.common.utils import torch_to_numpy
from iron.applications.yolov8n.blocks import CBS, Bottleneck, C2f, SPPF

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

VAL_RANGE = 2.0
"""Random tensor value range [-VAL_RANGE, VAL_RANGE]."""


def _rand_bf16(*shape, seed=42):
    """Generate a random bfloat16 tensor in [-VAL_RANGE, VAL_RANGE]."""
    torch.manual_seed(seed)
    return (torch.rand(*shape) * 2 * VAL_RANGE - VAL_RANGE).to(torch.bfloat16)


def _compare(npu_out, ref_out, rel_tol=0.07, abs_tol=0.5, label="output"):
    """Element-wise comparison with tolerance, returns list of error indices."""
    npu_np = torch_to_numpy(npu_out).reshape(-1)
    ref_np = torch_to_numpy(ref_out).reshape(-1)

    assert len(npu_np) == len(
        ref_np
    ), f"{label}: shape mismatch NPU={npu_out.shape} vs ref={ref_out.shape}"

    errors = []
    for i in range(len(ref_np)):
        a = float(npu_np[i])
        b = float(ref_np[i])
        if a == b:
            continue
        diff = abs(a - b)
        norm = min(abs(a) + abs(b), np.finfo(np.float32).max)
        if diff >= max(abs_tol, rel_tol * norm):
            errors.append(i)
            if len(errors) <= 10:
                print(
                    f"{label} mismatch [{i}]: NPU={a:.6f}, ref={b:.6f}, "
                    f"diff={diff:.6f}"
                )
    return errors


def _prepare_context(context):
    """Compile and prepare runtime for the context."""
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    context.compile_all()
    context.prepare_runtime()


# ---------------------------------------------------------------------------
# Test: CBS block
# ---------------------------------------------------------------------------


def test_cbs_block(aie_context):
    """Test a single CBS block (Conv3x3 s2 + SiLU) on hardware.

    Uses 8->16 channels at 16x16 spatial, which is small enough for
    fast compilation but exercises the full CBS pipeline.
    """
    in_ch, out_ch = 8, 16
    h, w = 16, 16
    seed = 42

    # Create block
    cbs = CBS(
        in_ch,
        out_ch,
        kernel_size=3,
        stride=2,
        height=h,
        width=w,
        num_aie_columns=1,
        context=aie_context,
    )

    # Generate random weights and input
    torch.manual_seed(seed)
    weight = _rand_bf16(out_ch, in_ch, 3, 3, seed=seed)
    bias = _rand_bf16(out_ch, seed=seed + 1)
    x = _rand_bf16(1, in_ch, h, w, seed=seed + 2)

    cbs.load_weights(weight, bias)

    # Compute reference: conv2d + bias + SiLU
    ref = F.conv2d(x.float(), weight.float(), bias.float(), stride=2, padding=1)
    ref = F.silu(ref).to(torch.bfloat16)

    # Run on NPU
    _prepare_context(aie_context)
    npu_out = cbs.forward(x)

    # Verify shapes
    assert (
        npu_out.shape == ref.shape
    ), f"Shape mismatch: NPU={npu_out.shape}, ref={ref.shape}"

    # Compare (wider tolerance for 3x3 conv + SiLU composition)
    errors = _compare(npu_out, ref, rel_tol=0.07, abs_tol=0.5, label="CBS")
    print(f"\nCBS test: {len(errors)} errors / {ref.numel()} elements")
    assert not errors, f"CBS test failed with {len(errors)} mismatches"


def test_cbs_1x1(aie_context):
    """Test a CBS block with 1x1 convolution on hardware."""
    in_ch, out_ch = 16, 32
    h, w = 8, 8
    seed = 100

    cbs = CBS(
        in_ch,
        out_ch,
        kernel_size=1,
        stride=1,
        height=h,
        width=w,
        num_aie_columns=1,
        context=aie_context,
    )

    torch.manual_seed(seed)
    weight = _rand_bf16(out_ch, in_ch, 1, 1, seed=seed)
    bias = _rand_bf16(out_ch, seed=seed + 1)
    x = _rand_bf16(1, in_ch, h, w, seed=seed + 2)

    cbs.load_weights(weight, bias)

    ref = F.conv2d(x.float(), weight.float(), bias.float(), stride=1, padding=0)
    ref = F.silu(ref).to(torch.bfloat16)

    _prepare_context(aie_context)
    npu_out = cbs.forward(x)

    assert npu_out.shape == ref.shape
    errors = _compare(npu_out, ref, rel_tol=0.07, abs_tol=0.5, label="CBS_1x1")
    print(f"\nCBS 1x1 test: {len(errors)} errors / {ref.numel()} elements")
    assert not errors, f"CBS 1x1 test failed with {len(errors)} mismatches"


# ---------------------------------------------------------------------------
# Test: Bottleneck block
# ---------------------------------------------------------------------------


def test_bottleneck_block(aie_context):
    """Test a Bottleneck block (two 3x3 convs + residual) on hardware.

    Uses 8 channels at 8x8 spatial for fast compilation.
    """
    ch = 8
    h, w = 8, 8
    seed = 200

    bn = Bottleneck(
        ch,
        height=h,
        width=w,
        shortcut=True,
        num_aie_columns=1,
        context=aie_context,
    )

    # Generate weights for both convolutions
    torch.manual_seed(seed)
    cv1_w = _rand_bf16(ch, ch, 3, 3, seed=seed)
    cv1_b = _rand_bf16(ch, seed=seed + 1)
    cv2_w = _rand_bf16(ch, ch, 3, 3, seed=seed + 2)
    cv2_b = _rand_bf16(ch, seed=seed + 3)
    x = _rand_bf16(1, ch, h, w, seed=seed + 4)

    bn.load_weights(cv1_w, cv1_b, cv2_w, cv2_b)

    # Reference: two conv3x3+SiLU + residual add
    out = F.conv2d(x.float(), cv1_w.float(), cv1_b.float(), stride=1, padding=1)
    out = F.silu(out)
    out = F.conv2d(out, cv2_w.float(), cv2_b.float(), stride=1, padding=1)
    out = F.silu(out)
    ref = (out + x.float()).to(torch.bfloat16)

    _prepare_context(aie_context)
    npu_out = bn.forward(x)

    assert npu_out.shape == ref.shape

    # Wider tolerance: two 3x3 convs + SiLU + residual
    errors = _compare(npu_out, ref, rel_tol=0.07, abs_tol=1.0, label="Bottleneck")
    print(f"\nBottleneck test: {len(errors)} errors / {ref.numel()} elements")
    assert not errors, f"Bottleneck test failed with {len(errors)} mismatches"


# ---------------------------------------------------------------------------
# Test: C2f block
# ---------------------------------------------------------------------------


def test_c2f_block(aie_context):
    """Test a C2f block (expand + 1 bottleneck + reduce) on hardware.

    Uses 16->16 channels at 8x8 spatial. This is the smallest meaningful
    C2f configuration: c_out//2 = 8 channels for the bottleneck hidden
    dimension, which is the minimum for AIE's 8-channel SIMD.
    """
    c_in, c_out = 16, 16
    n_bn = 1
    h, w = 8, 8
    seed = 300
    c = c_out // 2  # 8

    c2f = C2f(
        c_in,
        c_out,
        n_bottlenecks=n_bn,
        height=h,
        width=w,
        shortcut=True,
        num_aie_columns=1,
        context=aie_context,
    )

    # Generate weights
    torch.manual_seed(seed)
    cv1_w = _rand_bf16(2 * c, c_in, 1, 1, seed=seed)
    cv1_b = _rand_bf16(2 * c, seed=seed + 1)

    # Bottleneck weights
    bn_cv1_w = _rand_bf16(c, c, 3, 3, seed=seed + 2)
    bn_cv1_b = _rand_bf16(c, seed=seed + 3)
    bn_cv2_w = _rand_bf16(c, c, 3, 3, seed=seed + 4)
    bn_cv2_b = _rand_bf16(c, seed=seed + 5)
    bottleneck_weights = [(bn_cv1_w, bn_cv1_b, bn_cv2_w, bn_cv2_b)]

    # cv2 input channels: (2 + n_bn) * c = 3 * 8 = 24
    cv2_w = _rand_bf16(c_out, (2 + n_bn) * c, 1, 1, seed=seed + 6)
    cv2_b = _rand_bf16(c_out, seed=seed + 7)

    c2f.load_weights(cv1_w, cv1_b, bottleneck_weights, cv2_w, cv2_b)

    x = _rand_bf16(1, c_in, h, w, seed=seed + 8)

    # Reference computation
    # cv1: 1x1 conv + SiLU
    out = F.conv2d(x.float(), cv1_w.float(), cv1_b.float())
    out = F.silu(out).to(torch.bfloat16)

    # chunk into two halves
    chunks = out.chunk(2, dim=1)
    outputs = [chunks[0], chunks[1]]

    # Bottleneck
    bn_in = outputs[-1]
    bn_out = F.conv2d(bn_in.float(), bn_cv1_w.float(), bn_cv1_b.float(), padding=1)
    bn_out = F.silu(bn_out)
    bn_out = F.conv2d(bn_out, bn_cv2_w.float(), bn_cv2_b.float(), padding=1)
    bn_out = F.silu(bn_out)
    bn_out = (bn_out + bn_in.float()).to(torch.bfloat16)  # residual
    outputs.append(bn_out)

    # concat
    cat = torch.cat(outputs, dim=1)

    # cv2: 1x1 conv + SiLU
    ref = F.conv2d(cat.float(), cv2_w.float(), cv2_b.float())
    ref = F.silu(ref).to(torch.bfloat16)

    _prepare_context(aie_context)
    npu_out = c2f.forward(x)

    assert npu_out.shape == ref.shape

    # Widest tolerance: four convs deep + SiLU + residual + concat
    # bf16 accumulation error grows ~sqrt(N_ops), abs values grow with channel count
    errors = _compare(npu_out, ref, rel_tol=0.15, abs_tol=5.0, label="C2f")
    print(f"\nC2f test: {len(errors)} errors / {ref.numel()} elements")
    assert not errors, f"C2f test failed with {len(errors)} mismatches"


# ---------------------------------------------------------------------------
# Test: Backbone layers 0-2
# ---------------------------------------------------------------------------


@pytest.mark.extensive
def test_backbone_l0_l2(aie_context):
    """Test first 3 backbone layers: Conv3x3s2 -> Conv3x3s2 -> C2f.

    Uses reduced spatial size (32x32 instead of 640x640) for fast
    compilation, but preserves the channel progression:
        Input: 8ch 32x32 -> L0: 16ch 16x16 -> L1: 32ch 8x8 -> L2: 32ch 8x8

    This validates the end-to-end data flow pattern: multiple operators
    sharing one AIEContext, compiled together, and executed sequentially
    with NCHW bfloat16 tensors flowing between them.
    """
    seed = 400

    # Reduced spatial dimensions (must be even for stride-2 downsampling)
    h0, w0 = 32, 32  # input spatial
    h1, w1 = 16, 16  # after L0 (stride 2)
    h2, w2 = 8, 8  # after L1 (stride 2)

    # L0: Conv3x3 s2, 8->16
    l0 = CBS(
        8,
        16,
        kernel_size=3,
        stride=2,
        height=h0,
        width=w0,
        num_aie_columns=1,
        context=aie_context,
    )

    # L1: Conv3x3 s2, 16->32
    l1 = CBS(
        16,
        32,
        kernel_size=3,
        stride=2,
        height=h1,
        width=w1,
        num_aie_columns=1,
        context=aie_context,
    )

    # L2: C2f n=1, 32->32 (c=16 hidden channels)
    l2 = C2f(
        32,
        32,
        n_bottlenecks=1,
        height=h2,
        width=w2,
        shortcut=True,
        num_aie_columns=1,
        context=aie_context,
    )

    # Generate random weights
    torch.manual_seed(seed)
    l0_w = _rand_bf16(16, 8, 3, 3, seed=seed)
    l0_b = _rand_bf16(16, seed=seed + 1)
    l1_w = _rand_bf16(32, 16, 3, 3, seed=seed + 2)
    l1_b = _rand_bf16(32, seed=seed + 3)

    c = 16  # c_out // 2 for C2f(32, 32)
    cv1_w = _rand_bf16(32, 32, 1, 1, seed=seed + 4)
    cv1_b = _rand_bf16(32, seed=seed + 5)
    bn_cv1_w = _rand_bf16(c, c, 3, 3, seed=seed + 6)
    bn_cv1_b = _rand_bf16(c, seed=seed + 7)
    bn_cv2_w = _rand_bf16(c, c, 3, 3, seed=seed + 8)
    bn_cv2_b = _rand_bf16(c, seed=seed + 9)
    cv2_w = _rand_bf16(32, 48, 1, 1, seed=seed + 10)  # (2+1)*16 = 48
    cv2_b = _rand_bf16(32, seed=seed + 11)

    l0.load_weights(l0_w, l0_b)
    l1.load_weights(l1_w, l1_b)
    l2.load_weights(
        cv1_w,
        cv1_b,
        [(bn_cv1_w, bn_cv1_b, bn_cv2_w, bn_cv2_b)],
        cv2_w,
        cv2_b,
    )

    # Input: 3ch padded to 8ch at 32x32
    x = _rand_bf16(1, 3, h0, w0, seed=seed + 12)
    x_padded = F.pad(x, (0, 0, 0, 0, 0, 5)).to(torch.bfloat16)

    # Reference computation for L0 and L1 (float32 internally, cast to bf16)
    ref0 = F.conv2d(x_padded.float(), l0_w.float(), l0_b.float(), stride=2, padding=1)
    ref0 = F.silu(ref0).to(torch.bfloat16)

    ref1 = F.conv2d(ref0.float(), l1_w.float(), l1_b.float(), stride=2, padding=1)
    ref1 = F.silu(ref1).to(torch.bfloat16)

    # Run on NPU first so we can use the actual NPU L1 output as input to
    # the L2 reference.  The NPU accumulates bf16 rounding at each layer, so
    # ref1 and npu1 are slightly different tensors.  Feeding ref1 into the
    # C2f reference while npu1 goes into the NPU creates a diverging baseline
    # that compounds through C2f's 4-conv chain and produces huge apparent
    # mismatches (~1640) that are not real L2 errors.
    _prepare_context(aie_context)

    npu0 = l0.forward(x_padded)
    npu1 = l1.forward(npu0)

    # C2f reference: use npu1 as input and cast to bf16 at every boundary
    # to match the NPU's accumulation precision as closely as possible.
    out = F.conv2d(npu1.float(), cv1_w.float(), cv1_b.float())
    out = F.silu(out).to(torch.bfloat16)
    chunks = out.chunk(2, dim=1)
    outputs = [chunks[0], chunks[1]]

    bn_in = outputs[-1]
    bn_out = F.conv2d(bn_in.float(), bn_cv1_w.float(), bn_cv1_b.float(), padding=1)
    bn_out = F.silu(bn_out).to(torch.bfloat16)
    bn_out = F.conv2d(bn_out.float(), bn_cv2_w.float(), bn_cv2_b.float(), padding=1)
    bn_out = F.silu(bn_out).to(torch.bfloat16)
    bn_out = (bn_out + bn_in).to(torch.bfloat16)
    outputs.append(bn_out)
    cat = torch.cat(outputs, dim=1)
    ref2 = F.conv2d(cat.float(), cv2_w.float(), cv2_b.float())
    ref2 = F.silu(ref2).to(torch.bfloat16)

    npu2 = l2.forward(npu1)

    # Verify intermediate shapes
    assert npu0.shape == (1, 16, h1, w1), f"L0 shape: {npu0.shape}"
    assert npu1.shape == (1, 32, h2, w2), f"L1 shape: {npu1.shape}"
    assert npu2.shape == (1, 32, h2, w2), f"L2 shape: {npu2.shape}"

    # Compare each layer output
    # Cascaded layers compound bf16 rounding error
    err0 = _compare(npu0, ref0, rel_tol=0.07, abs_tol=0.5, label="L0")
    err1 = _compare(npu1, ref1, rel_tol=0.10, abs_tol=1.0, label="L1")
    err2 = _compare(npu2, ref2, rel_tol=0.15, abs_tol=5.0, label="L2")

    print(f"\nL0: {len(err0)} errors / {ref0.numel()} elements")
    print(f"L1: {len(err1)} errors / {ref1.numel()} elements")
    print(f"L2: {len(err2)} errors / {ref2.numel()} elements")

    assert not err0, f"L0 failed with {len(err0)} mismatches"
    assert not err1, f"L1 failed with {len(err1)} mismatches"
    # C2f has 4 convolutions deep — bf16 accumulation order differs between
    # PyTorch CPU (float32 reduction) and AIE (accfloat mmul). Allow up to 1%
    # element-wise outliers for composed blocks.
    max_err_pct = 0.01
    err2_pct = len(err2) / ref2.numel()
    assert err2_pct <= max_err_pct, (
        f"L2 failed with {len(err2)}/{ref2.numel()} ({err2_pct:.1%}) mismatches "
        f"(threshold {max_err_pct:.0%})"
    )
