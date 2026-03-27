#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Standalone test: vectorized k3 stride-2 accuracy at L7 scale (128->256, 40->20).

Run:
    python3 test_k3s2_accuracy.py

Compares NPU output against Python reference for the non-fused k3s2 conv.
"""

import sys
import numpy as np
import torch

from iron.common import AIEContext
from iron.operators.conv2d_int8.op import (
    AIEConv2dInt8,
    nchw_to_tiled_int8,
    tiled_to_nchw_int8,
    weights_to_tiled_int8_k3,
)
from iron.operators.conv2d_int8.reference import conv2d_int8_reference


def test_k3s2_config(in_channels, out_channels, height, width, scale):
    """Test non-fused k3 stride-2 conv at given config."""
    stride = 2
    out_h = height // 2
    out_w = width // 2

    print(f"\n{'='*70}")
    print(f"Testing k3s2: {in_channels}ic -> {out_channels}oc, "
          f"{height}x{width} -> {out_h}x{out_w}, scale={scale}")
    print(f"{'='*70}")

    torch.manual_seed(42)

    # Create random int8 inputs and weights
    x_int8 = torch.randint(-20, 21, (1, in_channels, height, width), dtype=torch.int8)
    w_int8 = torch.randint(-50, 51, (out_channels, in_channels, 3, 3), dtype=torch.int8)

    # CPU reference (stride=2, padding=1)
    ref_output = conv2d_int8_reference(x_int8, w_int8, scale, stride=stride, padding=1)
    print(f"Reference shape: {ref_output.shape}")

    # Create operator
    ctx = AIEContext()
    operator = AIEConv2dInt8(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=3,
        stride=stride,
        height=height,
        width=width,
        scale=scale,
        fused=False,
        context=ctx,
    )

    # Compile and prepare
    print("Compiling...")
    operator.context.compile_all()
    operator.context.prepare_runtime()

    # Run on NPU
    print("Running on NPU...")
    npu_output = operator.forward(x_int8, w_int8)
    print(f"NPU output shape: {npu_output.shape}")

    # Compare element-by-element
    ref_np = ref_output.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diffs = np.abs(ref_np - npu_np)
    exact = np.sum(diffs == 0)
    off_by_one = np.sum(diffs == 1)
    errors = np.sum(diffs > 1)
    total = len(ref_np)

    print(f"\nResults ({total} elements):")
    print(f"  Exact match:   {exact}/{total} ({100*exact/total:.1f}%)")
    print(f"  Off-by-one:    {off_by_one}/{total} ({100*off_by_one/total:.1f}%)")
    print(f"  Errors (>1):   {errors}/{total} ({100*errors/total:.1f}%)")
    print(f"  Max diff:      {diffs.max()}")
    print(f"  Mean abs diff: {diffs.mean():.4f}")

    if errors > 0:
        # Show first 20 errors
        error_indices = np.where(diffs > 1)[0]
        print(f"\nFirst {min(20, len(error_indices))} errors:")
        for idx in error_indices[:20]:
            oc_g = idx // (out_h * out_w * 8)
            rem = idx % (out_h * out_w * 8)
            x_pos = (rem // 8) % out_w
            y_pos = (rem // 8) // out_w
            oc8 = rem % 8
            print(f"  [{idx}] NPU={npu_np[idx]:4d}, ref={ref_np[idx]:4d}, "
                  f"diff={diffs[idx]:3d} (oc_g={oc_g}, y={y_pos}, x={x_pos}, oc8={oc8})")

        # Correlation analysis
        corr = np.corrcoef(ref_np.astype(float), npu_np.astype(float))[0, 1]
        print(f"\n  Correlation: {corr:.4f}")

    return errors == 0


if __name__ == "__main__":
    configs = [
        # (in_ch, out_ch, h, w, scale)
        # Small config (existing test size, should pass)
        (8, 16, 8, 8, 10),
        # Medium config
        (32, 64, 16, 16, 10),
        # L7 config (the problematic one)
        (128, 256, 40, 40, 10),
    ]

    # If argument given, run specific configs
    if len(sys.argv) > 1 and sys.argv[1] == "l7":
        configs = [(128, 256, 40, 40, 10)]
    elif len(sys.argv) > 1 and sys.argv[1] == "sweep":
        configs = [
            (8, 16, 8, 8, 10),       # ic_groups=1, vec_iters=0 (scalar only)
            (8, 16, 16, 16, 10),      # ic_groups=1, vec_iters=1
            (16, 16, 16, 16, 10),     # ic_groups=2
            (32, 32, 16, 16, 10),     # ic_groups=4
            (64, 64, 24, 24, 10),     # ic_groups=8, ow=12, vec_iters=1
            (64, 64, 40, 40, 10),     # ic_groups=8, ow=20, vec_iters=2
            (128, 128, 40, 40, 10),   # ic_groups=16, ow=20
            (128, 256, 40, 40, 10),   # L7
        ]

    results = []
    for cfg in configs:
        try:
            passed = test_k3s2_config(*cfg)
            results.append((cfg, passed))
        except Exception as e:
            print(f"\nERROR for config {cfg}: {e}")
            import traceback
            traceback.print_exc()
            results.append((cfg, False))

    print(f"\n{'='*70}")
    print("Summary:")
    for cfg, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"  {cfg[0]}ic->{cfg[1]}oc {cfg[2]}x{cfg[3]} s2: {status}")
