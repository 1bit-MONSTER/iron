#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOv8n layer inventory benchmark.

Tests every unique (IC, OC, H, W, KS, stride, fused) configuration from the
YOLOv8n model at actual YOLO dimensions.  Each test creates an AIEConv2dInt8
operator, compiles once, runs a warmup, then performs N timed iterations
reusing the same HW context.

Run by group:

    pytest test_layer_benchmark.py -v -s -k "k3s2"      --iterations=10
    pytest test_layer_benchmark.py -v -s -k "k3s1"      --iterations=10
    pytest test_layer_benchmark.py -v -s -k "k1_fused"   --iterations=10
    pytest test_layer_benchmark.py -v -s -k "k1_nonfused" --iterations=10
"""

import statistics
import time

import numpy as np
import pytest
import torch

from iron.operators.conv2d_int8.op import AIEConv2dInt8
from iron.operators.conv2d_int8.reference import (
    conv2d_int8_pade_silu_reference,
    conv2d_int8_reference,
)


# ── helpers ──────────────────────────────────────────────────────────────────


def _run_and_verify(operator, x_int8, w_int8, bias_int32, ref_output, max_tol,
                    label, iterations):
    """Compile once, warmup, then time *iterations* runs on the same HW context.

    Args:
        operator: An AIEConv2dInt8 instance (not yet compiled).
        x_int8: Input tensor [1, IC, H, W] int8.
        w_int8: Weight tensor [OC, IC, K, K] int8.
        bias_int32: Bias tensor [OC] int32, or None for non-fused.
        ref_output: CPU reference tensor [1, OC, OH, OW] int8.
        max_tol: Maximum allowed element-wise absolute difference.
        label: Human-readable name for printing.
        iterations: Number of timed iterations (after warmup).
    """
    # ── compile + load (once) ──
    operator.context.compile_all()
    operator.context.prepare_runtime()

    # ── warmup run (verify correctness, discard timing) ──
    npu_output = operator.forward(x_int8, w_int8, bias_int32)

    ref_np = ref_output.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff))
    total = len(ref_np)
    exact = int(np.sum(diff == 0))
    off_by_one = int(np.sum(diff == 1))
    errors = int(np.sum(diff > max_tol))

    # ── timed iterations (same HW context, same xrt::run path) ──
    times_ms = []
    for _ in range(iterations):
        t0 = time.perf_counter()
        operator.forward(x_int8, w_int8, bias_int32)
        t1 = time.perf_counter()
        times_ms.append((t1 - t0) * 1000.0)

    # ── report ──
    t_min = min(times_ms)
    t_med = statistics.median(times_ms)
    t_mean = statistics.mean(times_ms)
    t_max = max(times_ms)

    print(f"\n{label}:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Off-by-one: {off_by_one}/{total}")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>{max_tol}): {errors}/{total}")
    print(f"  NPU time ({iterations} iters): "
          f"min={t_min:.2f} med={t_med:.2f} mean={t_mean:.2f} max={t_max:.2f} ms")

    assert errors == 0, (
        f"{label}: {errors} elements exceed tolerance {max_tol} "
        f"(max_diff={max_diff}, total={total})"
    )


# ── Test 1: k3 stride-2 fused CBS (downsample) ──────────────────────────────

k3s2_params = [
    # (IC, OC, H, W, stride) — all fused (SiLU)
    pytest.param(8, 16, 640, 640, 2, id="L0_k3s2_8ic_16oc_640"),
    pytest.param(16, 32, 320, 320, 2, id="L1_k3s2_16ic_32oc_320"),
    pytest.param(32, 64, 160, 160, 2, id="L3_k3s2_32ic_64oc_160"),
    pytest.param(64, 128, 80, 80, 2, id="L5_k3s2_64ic_128oc_80"),
    pytest.param(128, 256, 40, 40, 2, id="L7_k3s2_128ic_256oc_40"),
    pytest.param(64, 64, 80, 80, 2, id="L16_k3s2_64ic_64oc_80"),
    pytest.param(128, 128, 40, 40, 2, id="L19_k3s2_128ic_128oc_40"),
]


@pytest.mark.internal_iterations
@pytest.mark.parametrize("ic,oc,h,w,stride", k3s2_params)
def test_k3s2_fused(ic, oc, h, w, stride, aie_context, request):
    """k3 stride-2 fused conv+bias+SiLU at YOLO dimensions."""
    iterations = request.config.getoption("--iterations")
    torch.manual_seed(42)
    shift1, shift2 = 10, 7

    x = torch.randint(-20, 21, (1, ic, h, w), dtype=torch.int8)
    wt = torch.randint(-50, 51, (oc, ic, 3, 3), dtype=torch.int8)
    bias = torch.randint(-500, 501, (oc,), dtype=torch.int32)

    ref = conv2d_int8_pade_silu_reference(x, wt, bias, shift1, shift2, stride=stride)

    op = AIEConv2dInt8(
        in_channels=ic,
        out_channels=oc,
        kernel_size=3,
        stride=stride,
        height=h,
        width=w,
        fused=True,
        shift1=shift1,
        shift2=shift2,
        context=aie_context,
    )

    _run_and_verify(op, x, wt, bias, ref, max_tol=2,
                    label=f"k3s2 {ic}->{oc} {h}x{w}", iterations=iterations)


# ── Test 2: k3 stride-1 fused CBS ───────────────────────────────────────────

k3s1_params = [
    # (IC, OC, H, W, stride)
    pytest.param(16, 16, 160, 160, 1, id="L2bn_k3s1_16ic_16oc_160"),
    pytest.param(32, 32, 80, 80, 1, id="L4bn_k3s1_32ic_32oc_80"),
    pytest.param(64, 64, 40, 40, 1, id="L6bn_k3s1_64ic_64oc_40"),
    pytest.param(128, 128, 20, 20, 1, id="L8bn_k3s1_128ic_128oc_20"),
    pytest.param(64, 64, 80, 80, 1, id="det_reg_p3_k3s1_64ic_64oc_80"),
    pytest.param(64, 80, 80, 80, 1, id="det_cls_p3cv1_k3s1_64ic_80oc_80"),
    pytest.param(80, 80, 80, 80, 1, id="det_cls_p3cv2_k3s1_80ic_80oc_80"),
    pytest.param(128, 64, 40, 40, 1, id="det_reg_p4cv1_k3s1_128ic_64oc_40"),
    pytest.param(128, 80, 40, 40, 1, id="det_cls_p4cv1_k3s1_128ic_80oc_40"),
    pytest.param(80, 80, 40, 40, 1, id="det_cls_p4cv2_k3s1_80ic_80oc_40"),
    pytest.param(256, 64, 20, 20, 1, id="det_reg_p5cv1_k3s1_256ic_64oc_20"),
    pytest.param(256, 80, 20, 20, 1, id="det_cls_p5cv1_k3s1_256ic_80oc_20"),
    pytest.param(80, 80, 20, 20, 1, id="det_cls_p5cv2_k3s1_80ic_80oc_20"),
]


@pytest.mark.internal_iterations
@pytest.mark.parametrize("ic,oc,h,w,stride", k3s1_params)
def test_k3s1_fused(ic, oc, h, w, stride, aie_context, request):
    """k3 stride-1 fused conv+bias+SiLU at YOLO dimensions."""
    iterations = request.config.getoption("--iterations")
    torch.manual_seed(42)
    shift1, shift2 = 10, 7

    x = torch.randint(-20, 21, (1, ic, h, w), dtype=torch.int8)
    wt = torch.randint(-50, 51, (oc, ic, 3, 3), dtype=torch.int8)
    bias = torch.randint(-500, 501, (oc,), dtype=torch.int32)

    ref = conv2d_int8_pade_silu_reference(x, wt, bias, shift1, shift2, stride=stride)

    op = AIEConv2dInt8(
        in_channels=ic,
        out_channels=oc,
        kernel_size=3,
        stride=stride,
        height=h,
        width=w,
        fused=True,
        shift1=shift1,
        shift2=shift2,
        context=aie_context,
    )

    _run_and_verify(op, x, wt, bias, ref, max_tol=2,
                    label=f"k3s1 {ic}->{oc} {h}x{w}", iterations=iterations)


# ── Test 3: k1 fused CBS (1×1 conv + SiLU) ──────────────────────────────────

k1_fused_params = [
    # (IC, OC, H, W)
    pytest.param(32, 32, 160, 160, id="L2cv1_k1f_32ic_32oc_160"),
    pytest.param(48, 32, 160, 160, id="L2cv2_k1f_48ic_32oc_160"),
    pytest.param(64, 64, 80, 80, id="L4cv1_k1f_64ic_64oc_80"),
    pytest.param(128, 64, 80, 80, id="L4cv2_k1f_128ic_64oc_80"),
    pytest.param(128, 128, 40, 40, id="L6cv1_k1f_128ic_128oc_40"),
    pytest.param(256, 128, 40, 40, id="L6cv2_k1f_256ic_128oc_40"),
    pytest.param(256, 256, 20, 20, id="L8cv1_k1f_256ic_256oc_20"),
    pytest.param(384, 256, 20, 20, id="L8cv2_k1f_384ic_256oc_20"),
    pytest.param(256, 128, 20, 20, id="L9cv1_k1f_256ic_128oc_20"),
    pytest.param(512, 256, 20, 20, id="L9cv2_k1f_512ic_256oc_20"),
    pytest.param(384, 128, 40, 40, id="L12cv1_k1f_384ic_128oc_40"),
    pytest.param(192, 128, 40, 40, id="L12cv2_k1f_192ic_128oc_40"),
    pytest.param(192, 64, 80, 80, id="L15cv1_k1f_192ic_64oc_80"),
    pytest.param(96, 64, 80, 80, id="L15cv2_k1f_96ic_64oc_80"),
    pytest.param(384, 256, 20, 20, id="L21cv1_k1f_384ic_256oc_20"),
]


@pytest.mark.internal_iterations
@pytest.mark.parametrize("ic,oc,h,w", k1_fused_params)
def test_k1_fused(ic, oc, h, w, aie_context, request):
    """k1 fused conv+bias+SiLU at YOLO dimensions."""
    iterations = request.config.getoption("--iterations")
    torch.manual_seed(42)
    shift1, shift2 = 10, 7

    x = torch.randint(-20, 21, (1, ic, h, w), dtype=torch.int8)
    wt = torch.randint(-50, 51, (oc, ic, 1, 1), dtype=torch.int8)
    bias = torch.randint(-500, 501, (oc,), dtype=torch.int32)

    ref = conv2d_int8_pade_silu_reference(
        x, wt, bias, shift1, shift2, stride=1, padding=0
    )

    op = AIEConv2dInt8(
        in_channels=ic,
        out_channels=oc,
        kernel_size=1,
        stride=1,
        height=h,
        width=w,
        fused=True,
        shift1=shift1,
        shift2=shift2,
        context=aie_context,
    )

    _run_and_verify(op, x, wt, bias, ref, max_tol=2,
                    label=f"k1f {ic}->{oc} {h}x{w}", iterations=iterations)


# ── Test 4: k1 non-fused (detect head bare conv) ────────────────────────────

k1_nonfused_params = [
    # (IC, OC, H, W)
    pytest.param(64, 64, 80, 80, id="det_reg_p3cv3_k1_64ic_64oc_80"),
    pytest.param(80, 80, 80, 80, id="det_cls_p3cv3_k1_80ic_80oc_80"),
    pytest.param(64, 64, 40, 40, id="det_reg_p4cv3_k1_64ic_64oc_40"),
    pytest.param(80, 80, 40, 40, id="det_cls_p4cv3_k1_80ic_80oc_40"),
    pytest.param(64, 64, 20, 20, id="det_reg_p5cv3_k1_64ic_64oc_20"),
    pytest.param(80, 80, 20, 20, id="det_cls_p5cv3_k1_80ic_80oc_20"),
]


@pytest.mark.internal_iterations
@pytest.mark.parametrize("ic,oc,h,w", k1_nonfused_params)
def test_k1_nonfused(ic, oc, h, w, aie_context, request):
    """k1 non-fused conv (detect head) at YOLO dimensions."""
    iterations = request.config.getoption("--iterations")
    torch.manual_seed(42)
    scale = 10

    x = torch.randint(-20, 21, (1, ic, h, w), dtype=torch.int8)
    wt = torch.randint(-50, 51, (oc, ic, 1, 1), dtype=torch.int8)

    ref = conv2d_int8_reference(x, wt, scale, stride=1, padding=0)

    op = AIEConv2dInt8(
        in_channels=ic,
        out_channels=oc,
        kernel_size=1,
        stride=1,
        height=h,
        width=w,
        scale=scale,
        context=aie_context,
    )

    _run_and_verify(op, x, wt, None, ref, max_tol=1,
                    label=f"k1 {ic}->{oc} {h}x{w}", iterations=iterations)
