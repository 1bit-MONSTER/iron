#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Sweep widths to find where vectorized k3 SiLU breaks."""

import sys
import torch
import numpy as np

from iron.common import AIEContext
from iron.operators.conv2d_int8.op import AIEConv2dInt8
from iron.operators.conv2d_int8.reference import conv2d_int8_pade_silu_reference


def test_width(h, w, in_ch=8, out_ch=16, stride=1, shift1=10, shift2=7):
    """Test fused k3 at a specific width. Returns (passed, error_count, total)."""
    torch.manual_seed(42)
    x = torch.randint(-20, 21, (1, in_ch, h, w), dtype=torch.int8)
    wt = torch.randint(-50, 51, (out_ch, in_ch, 3, 3), dtype=torch.int8)
    bias = torch.randint(-500, 501, (out_ch,), dtype=torch.int32)

    ref = conv2d_int8_pade_silu_reference(x, wt, bias, shift1, shift2, stride=stride)

    ctx = AIEContext()
    op = AIEConv2dInt8(
        in_channels=in_ch, out_channels=out_ch,
        kernel_size=3, stride=stride, height=h, width=w,
        fused=True, shift1=shift1, shift2=shift2, context=ctx,
    )
    op.context.compile_all()
    op.context.prepare_runtime()
    npu_out = op.forward(x, wt, bias)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_out.numpy().reshape(-1).astype(np.int32)

    diffs = np.abs(ref_np - npu_np)
    errors = int(np.sum(diffs > 1))
    total = len(ref_np)
    exact = int(np.sum(diffs == 0))

    return (errors == 0, errors, total, exact)


def main():
    # Test widths from 8 to 96 in steps of 8
    widths = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]

    for w in widths:
        h = w  # Square
        vec_iters = w // 8
        try:
            passed, errors, total, exact = test_width(h, w)
            status = "PASS" if passed else "FAIL"
            print(f"  {w:3d}x{h:<3d}  vec_iters={vec_iters:2d}  {status}  "
                  f"exact={exact}/{total}  errors={errors}")
        except Exception as e:
            print(f"  {w:3d}x{h:<3d}  vec_iters={vec_iters:2d}  EXCEPTION: {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
