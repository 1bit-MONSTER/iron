#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Standalone test for vectorized k3 fused SiLU dispatch.

Tests conv2dk3_i8_silu_vec_{top,mid,bot} at multiple sizes to verify
the three-function vectorized approach with MMUL + tanh SiLU.
"""

import sys
import torch
import numpy as np

from iron.common import AIEContext
from iron.operators.conv2d_int8.op import AIEConv2dInt8
from iron.operators.conv2d_int8.reference import conv2d_int8_pade_silu_reference


def test_fused_k3_silu(in_ch, out_ch, h, w, stride, shift1, shift2):
    """Test fused k3 conv+bias+SiLU at a given size."""
    print(f"\n{'='*60}")
    print(f"Testing: {in_ch}ic x {out_ch}oc @ {h}x{w}, stride={stride}")
    print(f"  shift1={shift1}, shift2={shift2}")
    print(f"  Vectorized path: width%8={w%8} -> {'YES' if w%8==0 else 'NO (scalar)'}")
    print(f"{'='*60}")

    torch.manual_seed(42)
    x_int8 = torch.randint(-20, 21, (1, in_ch, h, w), dtype=torch.int8)
    w_int8 = torch.randint(-50, 51, (out_ch, in_ch, 3, 3), dtype=torch.int8)
    bias_int32 = torch.randint(-500, 501, (out_ch,), dtype=torch.int32)

    # CPU reference
    ref_output = conv2d_int8_pade_silu_reference(
        x_int8, w_int8, bias_int32, shift1, shift2, stride=stride
    )

    # Create operator with fresh context
    ctx = AIEContext()
    op = AIEConv2dInt8(
        in_channels=in_ch,
        out_channels=out_ch,
        kernel_size=3,
        stride=stride,
        height=h,
        width=w,
        fused=True,
        shift1=shift1,
        shift2=shift2,
        context=ctx,
    )

    # Compile
    print("  Compiling...")
    op.context.compile_all()
    op.context.prepare_runtime()

    # Run
    print("  Running on NPU...")
    npu_output = op.forward(x_int8, w_int8, bias_int32)

    # Verify
    ref_np = ref_output.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    errors = []
    for i in range(len(ref_np)):
        diff = abs(int(npu_np[i]) - int(ref_np[i]))
        if diff > 1:
            errors.append((i, int(npu_np[i]), int(ref_np[i]), diff))
            if len(errors) <= 10:
                print(
                    f"  MISMATCH at [{i}]: NPU={npu_np[i]}, ref={ref_np[i]}, diff={diff}"
                )

    total = len(ref_np)
    exact = int(np.sum(ref_np == npu_np))
    off1 = int(np.sum(np.abs(ref_np - npu_np) == 1))
    print(f"  Results: exact={exact}/{total}, off-by-1={off1}/{total}, errors={len(errors)}/{total}")

    if errors:
        print(f"  FAILED: {len(errors)} mismatches (diff > 1)")
        return False
    else:
        print(f"  PASSED")
        return True


def main():
    # Test matrix: (in_ch, out_ch, h, w, stride, shift1, shift2)
    tests = [
        # Original 8x8 tests (baseline)
        (8, 16, 8, 8, 1, 10, 7),
        (8, 16, 8, 8, 2, 10, 7),
        # 32x32 (larger spatial, vectorized path)
        (8, 16, 32, 32, 1, 10, 7),
        # 80x80 (non-power-of-2 but %8==0)
        (8, 16, 80, 80, 1, 10, 7),
        # 160x160 (large spatial)
        (8, 16, 160, 160, 1, 10, 7),
    ]

    passed = 0
    failed = 0
    for t in tests:
        try:
            if test_fused_k3_silu(*t):
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  EXCEPTION: {e}")
            import traceback
            traceback.print_exc()
            failed += 1

    print(f"\n{'='*60}")
    print(f"SUMMARY: {passed} passed, {failed} failed out of {len(tests)}")
    print(f"{'='*60}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
