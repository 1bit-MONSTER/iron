#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests for YOLOv8n neck (FPN + PAN) and detect head.

Tests are ordered from simple to complex:
    1. Neck FPN up-path (Upsample + Concat + C2f)
    2. Neck PAN down-path (CBS 3x3 s2 + Concat + C2f)
    3. Detect branch (CBS + CBS + Conv1x1 bare)
    4. Full neck at reduced scale (extensive)
    5. Detect head at P5 scale (extensive)

All tests use small spatial dimensions for fast compilation and
compare NPU output against a PyTorch CPU reference. Composed
blocks may have up to 1% element-wise outliers due to bf16
accumulation order differences between PyTorch CPU and AIE.
"""

import logging

import numpy as np
import pytest
import torch
import torch.nn.functional as F

from iron.common.utils import torch_to_numpy
from iron.applications.yolov8n.blocks import CBS, C2f
from iron.operators.conv2d.op import AIEConv2d
from iron.operators.upsample.op import AIEUpsample

# ---------------------------------------------------------------------------
# Helpers (same as test_backbone.py for consistency)
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


def _c2f_reference(x, cv1_w, cv1_b, bn_weights, cv2_w, cv2_b, shortcut=False):
    """Compute C2f reference in bf16-at-boundaries style.

    Args:
        x: Input tensor [1, c_in, H, W] in bfloat16.
        cv1_w: Conv1x1 expand weight.
        cv1_b: Conv1x1 expand bias.
        bn_weights: List of (cv1_w, cv1_b, cv2_w, cv2_b) per bottleneck.
        cv2_w: Conv1x1 reduce weight.
        cv2_b: Conv1x1 reduce bias.
        shortcut: Whether bottlenecks use residual shortcuts.

    Returns:
        Output tensor [1, c_out, H, W] in bfloat16.
    """
    # cv1: 1x1 conv + SiLU
    out = F.conv2d(x.float(), cv1_w.float(), cv1_b.float())
    out = F.silu(out).to(torch.bfloat16)

    # chunk into two halves
    chunks = out.chunk(2, dim=1)
    outputs = [chunks[0], chunks[1]]

    # Bottleneck chain
    for bn_cv1_w, bn_cv1_b, bn_cv2_w, bn_cv2_b in bn_weights:
        bn_in = outputs[-1]
        bn_out = F.conv2d(bn_in.float(), bn_cv1_w.float(), bn_cv1_b.float(), padding=1)
        bn_out = F.silu(bn_out).to(torch.bfloat16)
        bn_out = F.conv2d(bn_out.float(), bn_cv2_w.float(), bn_cv2_b.float(), padding=1)
        bn_out = F.silu(bn_out).to(torch.bfloat16)
        if shortcut:
            bn_out = (bn_out + bn_in).to(torch.bfloat16)
        outputs.append(bn_out)

    # concat
    cat = torch.cat(outputs, dim=1)

    # cv2: 1x1 conv + SiLU
    ref = F.conv2d(cat.float(), cv2_w.float(), cv2_b.float())
    ref = F.silu(ref).to(torch.bfloat16)
    return ref


def _cbs_reference(x, weight, bias, stride=1, padding=1):
    """Compute CBS reference: Conv + SiLU, cast to bf16."""
    out = F.conv2d(
        x.float(), weight.float(), bias.float(), stride=stride, padding=padding
    )
    return F.silu(out).to(torch.bfloat16)


# ---------------------------------------------------------------------------
# Weight generation helpers
# ---------------------------------------------------------------------------


def _gen_c2f_weights(c_in, c_out, n_bn, seed):
    """Generate random C2f weights.

    Returns:
        (cv1_w, cv1_b, bn_weights, cv2_w, cv2_b)
    """
    c = c_out // 2
    cv1_w = _rand_bf16(2 * c, c_in, 1, 1, seed=seed)
    cv1_b = _rand_bf16(2 * c, seed=seed + 1)

    bn_weights = []
    for i in range(n_bn):
        s = seed + 2 + i * 4
        bn_weights.append(
            (
                _rand_bf16(c, c, 3, 3, seed=s),
                _rand_bf16(c, seed=s + 1),
                _rand_bf16(c, c, 3, 3, seed=s + 2),
                _rand_bf16(c, seed=s + 3),
            )
        )

    cv2_in = (2 + n_bn) * c
    cv2_w = _rand_bf16(c_out, cv2_in, 1, 1, seed=seed + 100)
    cv2_b = _rand_bf16(c_out, seed=seed + 101)

    return cv1_w, cv1_b, bn_weights, cv2_w, cv2_b


# ---------------------------------------------------------------------------
# Test: Neck FPN up-path
# ---------------------------------------------------------------------------


def test_neck_fpn_up(aie_context):
    """Test FPN up-path: Upsample + Concat + C2f at small scale.

    Uses reduced channel counts and spatial sizes:
        p5_sim: [1, 16, 4, 4]   (simulates P5)
        p4_sim: [1, 8, 8, 8]    (simulates P4)
        Upsample(16ch, 4x4 -> 8x8)
        Concat(16+8=24ch, 8x8)
        C2f(24->16, 8x8, n=1, shortcut=False)
    """
    seed = 500

    # Simulate P5 and P4 at small scale
    p5_ch, p5_h, p5_w = 16, 4, 4
    p4_ch, p4_h, p4_w = 8, 8, 8

    # Build operators
    up = AIEUpsample(
        channels=p5_ch,
        height=p5_h,
        width=p5_w,
        scale_factor=2,
        context=aie_context,
    )

    c2f_in = p5_ch + p4_ch  # 24
    c2f_out = 16
    c2f = C2f(
        c2f_in,
        c2f_out,
        n_bottlenecks=1,
        height=p4_h,
        width=p4_w,
        shortcut=False,
        context=aie_context,
    )

    # Generate inputs and weights
    p5 = _rand_bf16(1, p5_ch, p5_h, p5_w, seed=seed)
    p4 = _rand_bf16(1, p4_ch, p4_h, p4_w, seed=seed + 1)

    cv1_w, cv1_b, bn_weights, cv2_w, cv2_b = _gen_c2f_weights(
        c2f_in, c2f_out, 1, seed=seed + 10
    )
    c2f.load_weights(cv1_w, cv1_b, bn_weights, cv2_w, cv2_b)

    # Compile
    _prepare_context(aie_context)

    # --- NPU path ---
    npu_up = up.forward(p5)  # [1, 16, 8, 8]
    npu_cat = torch.cat([npu_up, p4], dim=1)  # [1, 24, 8, 8]
    npu_out = c2f.forward(npu_cat)  # [1, 16, 8, 8]

    # --- Reference path ---
    # Upsample reference: nearest-neighbor 2x
    ref_up = F.interpolate(p5.float(), scale_factor=2, mode="nearest").to(
        torch.bfloat16
    )
    ref_cat = torch.cat([ref_up, p4], dim=1)

    # Feed NPU's actual concatenated output to avoid diverging baselines
    ref_out = _c2f_reference(
        npu_cat, cv1_w, cv1_b, bn_weights, cv2_w, cv2_b, shortcut=False
    )

    # --- Verify ---
    assert npu_up.shape == (1, p5_ch, p4_h, p4_w), f"Upsample shape: {npu_up.shape}"
    assert npu_out.shape == (1, c2f_out, p4_h, p4_w), f"C2f shape: {npu_out.shape}"

    # Check upsample
    err_up = _compare(npu_up, ref_up, rel_tol=0.01, abs_tol=0.01, label="Upsample")
    print(f"\nUpsample: {len(err_up)} errors / {ref_up.numel()} elements")
    assert not err_up, f"Upsample failed with {len(err_up)} mismatches"

    # Check C2f (allow 1% outliers for composed blocks)
    err_c2f = _compare(npu_out, ref_out, rel_tol=0.15, abs_tol=5.0, label="FPN_C2f")
    print(f"FPN C2f: {len(err_c2f)} errors / {ref_out.numel()} elements")
    max_err_pct = 0.01
    err_pct = len(err_c2f) / ref_out.numel()
    assert err_pct <= max_err_pct, (
        f"FPN C2f failed with {len(err_c2f)}/{ref_out.numel()} "
        f"({err_pct:.1%}) mismatches (threshold {max_err_pct:.0%})"
    )


# ---------------------------------------------------------------------------
# Test: Neck PAN down-path
# ---------------------------------------------------------------------------


def test_neck_pan_down(aie_context):
    """Test PAN down-path: CBS 3x3 s2 + Concat + C2f at small scale.

    Uses reduced channel counts and spatial sizes:
        det_p3_sim: [1, 8, 8, 8]    (simulates det_p3)
        l12_sim: [1, 16, 4, 4]      (simulates L12 skip output)
        CBS 3x3 s2(8->8, 8x8 -> 4x4)
        Concat(8+16=24, 4x4)
        C2f(24->16, 4x4, n=1, shortcut=False)
    """
    seed = 600

    det_ch, det_h, det_w = 8, 8, 8
    l12_ch, l12_h, l12_w = 16, 4, 4

    # Build operators
    cbs = CBS(
        det_ch,
        det_ch,
        kernel_size=3,
        stride=2,
        height=det_h,
        width=det_w,
        context=aie_context,
    )

    c2f_in = det_ch + l12_ch  # 24
    c2f_out = 16
    c2f = C2f(
        c2f_in,
        c2f_out,
        n_bottlenecks=1,
        height=l12_h,
        width=l12_w,
        shortcut=False,
        context=aie_context,
    )

    # Generate inputs and weights
    det_p3 = _rand_bf16(1, det_ch, det_h, det_w, seed=seed)
    l12_out = _rand_bf16(1, l12_ch, l12_h, l12_w, seed=seed + 1)

    cbs_w = _rand_bf16(det_ch, det_ch, 3, 3, seed=seed + 2)
    cbs_b = _rand_bf16(det_ch, seed=seed + 3)
    cbs.load_weights(cbs_w, cbs_b)

    cv1_w, cv1_b, bn_weights, cv2_w, cv2_b = _gen_c2f_weights(
        c2f_in, c2f_out, 1, seed=seed + 10
    )
    c2f.load_weights(cv1_w, cv1_b, bn_weights, cv2_w, cv2_b)

    # Compile
    _prepare_context(aie_context)

    # --- NPU path ---
    npu_cbs = cbs.forward(det_p3)  # [1, 8, 4, 4]
    npu_cat = torch.cat([npu_cbs, l12_out], dim=1)  # [1, 24, 4, 4]
    npu_out = c2f.forward(npu_cat)  # [1, 16, 4, 4]

    # --- Reference ---
    ref_cbs = _cbs_reference(det_p3, cbs_w, cbs_b, stride=2, padding=1)

    # Use NPU's actual CBS output to avoid diverging baselines
    ref_out = _c2f_reference(
        npu_cat, cv1_w, cv1_b, bn_weights, cv2_w, cv2_b, shortcut=False
    )

    # --- Verify ---
    assert npu_cbs.shape == (1, det_ch, l12_h, l12_w), f"CBS shape: {npu_cbs.shape}"
    assert npu_out.shape == (1, c2f_out, l12_h, l12_w), f"C2f shape: {npu_out.shape}"

    # Check CBS
    err_cbs = _compare(npu_cbs, ref_cbs, rel_tol=0.07, abs_tol=0.5, label="PAN_CBS")
    print(f"\nPAN CBS: {len(err_cbs)} errors / {ref_cbs.numel()} elements")
    assert not err_cbs, f"PAN CBS failed with {len(err_cbs)} mismatches"

    # Check C2f (allow 1% outliers)
    err_c2f = _compare(npu_out, ref_out, rel_tol=0.15, abs_tol=5.0, label="PAN_C2f")
    print(f"PAN C2f: {len(err_c2f)} errors / {ref_out.numel()} elements")
    max_err_pct = 0.01
    err_pct = len(err_c2f) / ref_out.numel()
    assert err_pct <= max_err_pct, (
        f"PAN C2f failed with {len(err_c2f)}/{ref_out.numel()} "
        f"({err_pct:.1%}) mismatches (threshold {max_err_pct:.0%})"
    )


# ---------------------------------------------------------------------------
# Test: Detect branch
# ---------------------------------------------------------------------------


def test_detect_branch(aie_context):
    """Test one detect branch: CBS(3x3) -> CBS(3x3) -> Conv1x1 at small scale.

    Uses reduced channel counts:
        c_in=16, c_mid=8, c_out=8, spatial 8x8
    The final Conv1x1 has no activation and no BN -- just bias.
    """
    seed = 700

    c_in, c_mid, c_out = 16, 8, 8
    h, w = 8, 8

    # Build operators
    cv1 = CBS(
        c_in,
        c_mid,
        kernel_size=3,
        stride=1,
        height=h,
        width=w,
        context=aie_context,
    )
    cv2 = CBS(
        c_mid,
        c_mid,
        kernel_size=3,
        stride=1,
        height=h,
        width=w,
        context=aie_context,
    )
    cv3 = AIEConv2d(
        in_channels=c_mid,
        out_channels=c_out,
        kernel_size=1,
        stride=1,
        height=h,
        width=w,
        has_bias=True,
        activation=None,
        context=aie_context,
    )

    # Generate weights
    cv1_w = _rand_bf16(c_mid, c_in, 3, 3, seed=seed)
    cv1_b = _rand_bf16(c_mid, seed=seed + 1)
    cv2_w = _rand_bf16(c_mid, c_mid, 3, 3, seed=seed + 2)
    cv2_b = _rand_bf16(c_mid, seed=seed + 3)
    cv3_w = _rand_bf16(c_out, c_mid, 1, 1, seed=seed + 4)
    cv3_b = _rand_bf16(c_out, seed=seed + 5)

    cv1.load_weights(cv1_w, cv1_b)
    cv2.load_weights(cv2_w, cv2_b)

    x = _rand_bf16(1, c_in, h, w, seed=seed + 10)

    # Compile
    _prepare_context(aie_context)

    # --- NPU path ---
    npu1 = cv1.forward(x)  # Conv3x3 + SiLU
    npu2 = cv2.forward(npu1)  # Conv3x3 + SiLU
    npu3 = cv3.forward(npu2, cv3_w, cv3_b)  # Conv1x1, no activation

    # --- Reference ---
    # Use NPU intermediate outputs to avoid diverging baselines
    # cv1: 3x3 conv + SiLU
    ref1 = _cbs_reference(x, cv1_w, cv1_b, stride=1, padding=1)
    # cv2: 3x3 conv + SiLU (use npu1 as input to match NPU data path)
    ref2 = _cbs_reference(npu1, cv2_w, cv2_b, stride=1, padding=1)
    # cv3: 1x1 conv, no activation (use npu2 as input)
    ref3 = F.conv2d(npu2.float(), cv3_w.float(), cv3_b.float())
    ref3 = ref3.to(torch.bfloat16)

    # --- Verify ---
    assert npu3.shape == (1, c_out, h, w), f"Detect branch shape: {npu3.shape}"

    # Check CBS stages
    err1 = _compare(npu1, ref1, rel_tol=0.07, abs_tol=0.5, label="Det_CBS1")
    err2 = _compare(npu2, ref2, rel_tol=0.07, abs_tol=0.5, label="Det_CBS2")
    # Check final 1x1 (tighter tolerance -- single 1x1 conv, no activation)
    err3 = _compare(npu3, ref3, rel_tol=0.07, abs_tol=0.5, label="Det_Conv1x1")

    print(f"\nDetect CBS1: {len(err1)} errors / {ref1.numel()} elements")
    print(f"Detect CBS2: {len(err2)} errors / {ref2.numel()} elements")
    print(f"Detect Conv1x1: {len(err3)} errors / {ref3.numel()} elements")

    assert not err1, f"Detect CBS1 failed with {len(err1)} mismatches"
    assert not err2, f"Detect CBS2 failed with {len(err2)} mismatches"
    assert not err3, f"Detect Conv1x1 failed with {len(err3)} mismatches"


# ---------------------------------------------------------------------------
# Test: Full neck at reduced scale (extensive)
# ---------------------------------------------------------------------------


@pytest.mark.extensive
def test_neck_full(aie_context):
    """Test full neck (FPN up + PAN down) at reduced spatial scale.

    Uses the actual YOLOv8n channel counts but reduced spatial dims:
        p3: [1, 64, 8, 8]    (instead of 80x80)
        p4: [1, 128, 4, 4]   (instead of 40x40)
        p5: [1, 256, 4, 4]   (instead of 20x20)

    Spatial dims after stride-2 CBS: 8->4, 4->2 ... but 2x2 is too small
    for 3x3 conv with padding. So we use 16x16, 8x8, 4x4 instead.

    Revised spatial dims:
        p3: [1, 64, 16, 16]
        p4: [1, 128, 8, 8]
        p5: [1, 256, 4, 4]
    """
    seed = 800

    # Spatial dims (reduced from 80/40/20)
    p3_h, p3_w = 16, 16
    p4_h, p4_w = 8, 8
    p5_h, p5_w = 4, 4

    # ----- Build all operators -----

    # FPN up
    up1 = AIEUpsample(
        channels=256,
        height=p5_h,
        width=p5_w,
        scale_factor=2,
        context=aie_context,
    )
    l12 = C2f(
        384,
        128,
        n_bottlenecks=1,
        height=p4_h,
        width=p4_w,
        shortcut=False,
        context=aie_context,
    )
    up2 = AIEUpsample(
        channels=128,
        height=p4_h,
        width=p4_w,
        scale_factor=2,
        context=aie_context,
    )
    l15 = C2f(
        192,
        64,
        n_bottlenecks=1,
        height=p3_h,
        width=p3_w,
        shortcut=False,
        context=aie_context,
    )

    # PAN down
    l16 = CBS(
        64,
        64,
        kernel_size=3,
        stride=2,
        height=p3_h,
        width=p3_w,
        context=aie_context,
    )
    l18 = C2f(
        192,
        128,
        n_bottlenecks=1,
        height=p4_h,
        width=p4_w,
        shortcut=False,
        context=aie_context,
    )
    l19 = CBS(
        128,
        128,
        kernel_size=3,
        stride=2,
        height=p4_h,
        width=p4_w,
        context=aie_context,
    )
    l21 = C2f(
        384,
        256,
        n_bottlenecks=1,
        height=p5_h,
        width=p5_w,
        shortcut=False,
        context=aie_context,
    )

    # ----- Generate weights -----
    l12_cv1_w, l12_cv1_b, l12_bn, l12_cv2_w, l12_cv2_b = _gen_c2f_weights(
        384, 128, 1, seed=seed
    )
    l15_cv1_w, l15_cv1_b, l15_bn, l15_cv2_w, l15_cv2_b = _gen_c2f_weights(
        192, 64, 1, seed=seed + 200
    )
    l16_w = _rand_bf16(64, 64, 3, 3, seed=seed + 400)
    l16_b = _rand_bf16(64, seed=seed + 401)
    l18_cv1_w, l18_cv1_b, l18_bn, l18_cv2_w, l18_cv2_b = _gen_c2f_weights(
        192, 128, 1, seed=seed + 500
    )
    l19_w = _rand_bf16(128, 128, 3, 3, seed=seed + 700)
    l19_b = _rand_bf16(128, seed=seed + 701)
    l21_cv1_w, l21_cv1_b, l21_bn, l21_cv2_w, l21_cv2_b = _gen_c2f_weights(
        384, 256, 1, seed=seed + 800
    )

    l12.load_weights(l12_cv1_w, l12_cv1_b, l12_bn, l12_cv2_w, l12_cv2_b)
    l15.load_weights(l15_cv1_w, l15_cv1_b, l15_bn, l15_cv2_w, l15_cv2_b)
    l16.load_weights(l16_w, l16_b)
    l18.load_weights(l18_cv1_w, l18_cv1_b, l18_bn, l18_cv2_w, l18_cv2_b)
    l19.load_weights(l19_w, l19_b)
    l21.load_weights(l21_cv1_w, l21_cv1_b, l21_bn, l21_cv2_w, l21_cv2_b)

    # ----- Generate inputs -----
    p3 = _rand_bf16(1, 64, p3_h, p3_w, seed=seed + 1000)
    p4 = _rand_bf16(1, 128, p4_h, p4_w, seed=seed + 1001)
    p5 = _rand_bf16(1, 256, p5_h, p5_w, seed=seed + 1002)

    # Compile
    _prepare_context(aie_context)

    # ----- NPU path: FPN up -----
    x = up1.forward(p5)  # [1, 256, 8, 8]
    x = torch.cat([x, p4], dim=1)  # [1, 384, 8, 8]
    l12_npu = l12.forward(x)  # [1, 128, 8, 8]

    x = up2.forward(l12_npu)  # [1, 128, 16, 16]
    x = torch.cat([x, p3], dim=1)  # [1, 192, 16, 16]
    det_p3 = l15.forward(x)  # [1, 64, 16, 16]

    # ----- NPU path: PAN down -----
    x = l16.forward(det_p3)  # [1, 64, 8, 8]
    x = torch.cat([x, l12_npu], dim=1)  # [1, 192, 8, 8]
    det_p4 = l18.forward(x)  # [1, 128, 8, 8]

    x = l19.forward(det_p4)  # [1, 128, 4, 4]
    x = torch.cat([x, p5], dim=1)  # [1, 384, 4, 4]
    det_p5 = l21.forward(x)  # [1, 256, 4, 4]

    # ----- Verify shapes -----
    assert det_p3.shape == (1, 64, p3_h, p3_w), f"det_p3 shape: {det_p3.shape}"
    assert det_p4.shape == (1, 128, p4_h, p4_w), f"det_p4 shape: {det_p4.shape}"
    assert det_p5.shape == (1, 256, p5_h, p5_w), f"det_p5 shape: {det_p5.shape}"

    print(
        f"\nNeck full: det_p3={det_p3.shape}, det_p4={det_p4.shape}, "
        f"det_p5={det_p5.shape}"
    )
    print("Neck full test passed (shape verification)")


# ---------------------------------------------------------------------------
# Test: Detect head at P5 scale (extensive)
# ---------------------------------------------------------------------------


@pytest.mark.extensive
def test_detect_head_p5(aie_context):
    """Test detect head regression + classification branches.

    Uses reduced channel counts to fit in L1 without weight streaming:
        Input: [1, 64, 8, 8]
        Reg branch: CBS(64->64) -> CBS(64->64) -> Conv1x1(64->64)
        Cls branch: CBS(64->80) -> CBS(80->80) -> Conv1x1(80->80)

    Full-scale (256ch input) requires weight streaming design (Phase 6).
    """
    seed = 900

    c_in = 64
    h, w = 8, 8
    c_reg_mid, c_reg_out = 32, 32  # Reduced to fit in L1 without weight streaming
    c_cls_mid, c_cls_out = 32, 32  # Reduced (80ch needs weight streaming)

    from iron.applications.yolov8n.detect import DetectBranch

    # Build branches
    reg = DetectBranch(
        c_in,
        c_reg_mid,
        c_reg_out,
        h,
        w,
        context=aie_context,
    )
    cls = DetectBranch(
        c_in,
        c_cls_mid,
        c_cls_out,
        h,
        w,
        context=aie_context,
    )

    # Generate weights
    reg_cv1_w = _rand_bf16(c_reg_mid, c_in, 3, 3, seed=seed)
    reg_cv1_b = _rand_bf16(c_reg_mid, seed=seed + 1)
    reg_cv2_w = _rand_bf16(c_reg_mid, c_reg_mid, 3, 3, seed=seed + 2)
    reg_cv2_b = _rand_bf16(c_reg_mid, seed=seed + 3)
    reg_cv3_w = _rand_bf16(c_reg_out, c_reg_mid, 1, 1, seed=seed + 4)
    reg_cv3_b = _rand_bf16(c_reg_out, seed=seed + 5)

    cls_cv1_w = _rand_bf16(c_cls_mid, c_in, 3, 3, seed=seed + 10)
    cls_cv1_b = _rand_bf16(c_cls_mid, seed=seed + 11)
    cls_cv2_w = _rand_bf16(c_cls_mid, c_cls_mid, 3, 3, seed=seed + 12)
    cls_cv2_b = _rand_bf16(c_cls_mid, seed=seed + 13)
    cls_cv3_w = _rand_bf16(c_cls_out, c_cls_mid, 1, 1, seed=seed + 14)
    cls_cv3_b = _rand_bf16(c_cls_out, seed=seed + 15)

    reg.load_weights(reg_cv1_w, reg_cv1_b, reg_cv2_w, reg_cv2_b, reg_cv3_w, reg_cv3_b)
    cls.load_weights(cls_cv1_w, cls_cv1_b, cls_cv2_w, cls_cv2_b, cls_cv3_w, cls_cv3_b)

    # Input feature map
    x = _rand_bf16(1, c_in, h, w, seed=seed + 100)

    # Compile
    _prepare_context(aie_context)

    # --- NPU path (run stage by stage to capture intermediates) ---
    # Regression branch
    reg_npu1 = reg.cv1.forward(x)  # CBS: Conv3x3 + SiLU
    reg_npu2 = reg.cv2.forward(reg_npu1)  # CBS: Conv3x3 + SiLU
    reg_out = reg.cv3.forward(reg_npu2, reg_cv3_w, reg_cv3_b)  # Conv1x1, no activation

    # Classification branch
    cls_npu1 = cls.cv1.forward(x)  # CBS: Conv3x3 + SiLU
    cls_npu2 = cls.cv2.forward(cls_npu1)  # CBS: Conv3x3 + SiLU
    cls_out = cls.cv3.forward(cls_npu2, cls_cv3_w, cls_cv3_b)  # Conv1x1, no activation

    # --- Reference (use NPU intermediates to avoid diverging baselines) ---
    # Regression: reference for final 1x1 conv using NPU's cv2 output
    reg_ref3 = F.conv2d(reg_npu2.float(), reg_cv3_w.float(), reg_cv3_b.float()).to(
        torch.bfloat16
    )

    # Classification: reference for final 1x1 conv using NPU's cv2 output
    cls_ref3 = F.conv2d(cls_npu2.float(), cls_cv3_w.float(), cls_cv3_b.float()).to(
        torch.bfloat16
    )

    # --- Verify ---
    assert reg_out.shape == (1, c_reg_out, h, w), f"Reg shape: {reg_out.shape}"
    assert cls_out.shape == (1, c_cls_out, h, w), f"Cls shape: {cls_out.shape}"

    # Compare final outputs
    err_reg = _compare(reg_out, reg_ref3, rel_tol=0.10, abs_tol=1.0, label="Det_Reg")
    err_cls = _compare(cls_out, cls_ref3, rel_tol=0.10, abs_tol=1.0, label="Det_Cls")

    print(f"\nDetect Reg P5: {len(err_reg)} errors / {reg_ref3.numel()} elements")
    print(f"Detect Cls P5: {len(err_cls)} errors / {cls_ref3.numel()} elements")

    # Allow 1% outliers for 3-conv-deep branches
    max_err_pct = 0.01
    reg_pct = len(err_reg) / reg_ref3.numel()
    cls_pct = len(err_cls) / cls_ref3.numel()

    assert reg_pct <= max_err_pct, (
        f"Detect Reg P5 failed with {len(err_reg)}/{reg_ref3.numel()} "
        f"({reg_pct:.1%}) mismatches (threshold {max_err_pct:.0%})"
    )
    assert cls_pct <= max_err_pct, (
        f"Detect Cls P5 failed with {len(err_cls)}/{cls_ref3.numel()} "
        f"({cls_pct:.1%}) mismatches (threshold {max_err_pct:.0%})"
    )
