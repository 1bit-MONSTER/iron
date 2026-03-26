#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Benchmark int8 3x3 conv2d kernel on NPU.

Measures NPU execution time for scalar vs vectorized kernel implementations.
Run this script twice: once with scalar wrapper, once with vectorized wrapper.
Pass --label scalar or --label vectorized to tag the output.
"""

import argparse
import time

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


CONFIGS = [
    # (in_channels, out_channels, height, width)
    (16, 16, 160, 160),
    (32, 32, 80, 80),
    (64, 64, 40, 40),
]

SCALE = 10
WARMUP_ITERS = 5
BENCH_ITERS = 50


def benchmark_config(ic, oc, h, w, verify=True):
    """Benchmark a single conv2d k3s1 configuration.

    Returns (avg_ms, verified_ok).
    """
    ctx = AIEContext()
    op = AIEConv2dInt8(
        in_channels=ic,
        out_channels=oc,
        kernel_size=3,
        stride=1,
        height=h,
        width=w,
        scale=SCALE,
        context=ctx,
    )
    ctx.compile_all()
    ctx.prepare_runtime()

    torch.manual_seed(42)
    x = torch.randint(-20, 21, (1, ic, h, w), dtype=torch.int8)
    wt = torch.randint(-50, 81, (oc, ic, 3, 3), dtype=torch.int8)

    input_tiled = nchw_to_tiled_int8(x)
    weight_tiled = weights_to_tiled_int8_k3(wt)
    total_output = oc * h * w

    op.write_buffer("input", input_tiled)
    op.write_buffer("weights", weight_tiled)
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Warmup
    for _ in range(WARMUP_ITERS):
        op.run_runlist()

    # Benchmark
    start = time.perf_counter()
    for _ in range(BENCH_ITERS):
        op.run_runlist()
    elapsed = time.perf_counter() - start
    avg_ms = (elapsed / BENCH_ITERS) * 1000

    # Verify correctness
    verified_ok = True
    if verify:
        output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
        npu_out = tiled_to_nchw_int8(output_raw.copy(), oc, h, w)
        ref_out = conv2d_int8_reference(x, wt, SCALE, stride=1, padding=1)

        ref_np = ref_out.numpy().reshape(-1).astype(np.int32)
        npu_np = npu_out.numpy().reshape(-1).astype(np.int32)
        max_diff = int(np.max(np.abs(ref_np - npu_np)))
        n_errors = int(np.sum(np.abs(ref_np - npu_np) > 1))
        verified_ok = n_errors == 0
        if not verified_ok:
            print(f"  VERIFY FAIL: {n_errors} mismatches (max_diff={max_diff})")
            # Print first 20 mismatches with NCHW coordinates
            diffs = np.abs(ref_np - npu_np)
            mismatch_idx = np.where(diffs > 1)[0]
            N_show = min(20, len(mismatch_idx))
            # npu_out is [1, oc, h, w]
            for mi in range(N_show):
                flat_idx = mismatch_idx[mi]
                # NCHW coordinates: flat_idx = c * h * w + y * w + x_pos
                c_idx = flat_idx // (h * w)
                rem = flat_idx % (h * w)
                y_idx = rem // w
                x_idx = rem % w
                # Which zone? left=0, interior=1..W-2, right=W-1
                zone = "LEFT" if x_idx == 0 else ("RIGHT" if x_idx == w - 1 else "INTERIOR")
                print(
                    f"    [{flat_idx}] c={c_idx} y={y_idx} x={x_idx} "
                    f"({zone}): NPU={npu_np[flat_idx]} ref={ref_np[flat_idx]} "
                    f"diff={diffs[flat_idx]}"
                )
        else:
            exact = int(np.sum(ref_np == npu_np))
            print(
                f"  VERIFY OK: exact={exact}/{len(ref_np)}, "
                f"max_diff={max_diff}"
            )

    return avg_ms, verified_ok


def main():
    parser = argparse.ArgumentParser(description="Benchmark int8 k3 conv2d")
    parser.add_argument(
        "--label",
        default="unknown",
        help="Label for this run (e.g. 'scalar' or 'vectorized')",
    )
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"Int8 3x3 Conv2d Benchmark — {args.label}")
    print(f"{'='*60}")
    print(f"Warmup: {WARMUP_ITERS} iters, Benchmark: {BENCH_ITERS} iters\n")

    results = []
    for ic, oc, h, w in CONFIGS:
        tag = f"{ic}→{oc} k3s1 {h}×{w}"
        print(f"Config: {tag}")
        avg_ms, ok = benchmark_config(ic, oc, h, w)
        status = "PASS" if ok else "FAIL"
        print(f"  Time: {avg_ms:.3f} ms  [{status}]\n")
        results.append((tag, avg_ms, ok))

    print(f"\n{'='*60}")
    print(f"Summary — {args.label}")
    print(f"{'='*60}")
    for tag, avg_ms, ok in results:
        status = "PASS" if ok else "FAIL"
        print(f"  {tag:30s}  {avg_ms:8.3f} ms  [{status}]")
    print()


if __name__ == "__main__":
    main()
