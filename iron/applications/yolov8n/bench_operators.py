#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Benchmark YOLOv8n operators on NPU hardware.

Measures compile time and execution latency for representative operator
configurations used in the YOLOv8n architecture.

Note: Full YOLOv8n spatial dimensions (640x640, 320x320, etc.) exceed
the DMA BD size limit of 1023 elements per dimension. This benchmark
uses reduced spatial dimensions that compile successfully while still
exercising the same compute kernels and data paths.
"""

import sys
import time
import logging
import traceback
import torch
import numpy as np
from ml_dtypes import bfloat16

from iron.common import AIEContext
from iron.operators.conv2d.op import AIEConv2d
from iron.operators.maxpool2d.op import AIEMaxPool2d
from iron.operators.upsample.op import AIEUpsample
from iron.applications.yolov8n.blocks import CBS, Bottleneck


# Suppress noisy debug logs during benchmarking
logging.basicConfig(level=logging.WARNING)

NUM_ITERS = 10


def bench_conv2d(in_ch, out_ch, h, w, k, s, num_cols=1):
    """Benchmark a single Conv2d configuration."""
    label = f"Conv2d k{k}s{s} {in_ch}->{out_ch} @ {h}x{w}"
    context = AIEContext(use_runlist=True)
    op = AIEConv2d(
        in_channels=in_ch,
        out_channels=out_ch,
        kernel_size=k,
        stride=s,
        height=h,
        width=w,
        has_bias=False,
        activation=None,
        num_aie_columns=num_cols,
        context=context,
    )

    # Compile
    t0 = time.perf_counter()
    context.compile_all()
    compile_s = time.perf_counter() - t0

    context.prepare_runtime()

    # Generate test data
    x = (torch.rand(1, in_ch, h, w) * 2 - 1).to(torch.bfloat16)
    weight = (torch.randn(out_ch, in_ch, k, k) * 0.1).to(torch.bfloat16)

    # Warmup
    op.forward(x, weight)

    # Timed iterations
    times = []
    for _ in range(NUM_ITERS):
        t0 = time.perf_counter()
        op.forward(x, weight)
        times.append(time.perf_counter() - t0)

    times_us = [t * 1e6 for t in times]
    return label, compile_s, times_us


def bench_maxpool2d(channels, h, w, k, padding=None):
    """Benchmark a MaxPool2d configuration."""
    if padding is None:
        padding = k // 2
    label = f"MaxPool2d k{k} {channels}ch @ {h}x{w}"
    context = AIEContext(use_runlist=True)
    op = AIEMaxPool2d(
        channels=channels,
        height=h,
        width=w,
        kernel_size=k,
        stride=1,
        padding=padding,
        num_aie_columns=1,
        context=context,
    )

    t0 = time.perf_counter()
    context.compile_all()
    compile_s = time.perf_counter() - t0

    context.prepare_runtime()

    x = (torch.rand(1, channels, h, w) * 2 - 1).to(torch.bfloat16)

    # Warmup
    op.forward(x)

    times = []
    for _ in range(NUM_ITERS):
        t0 = time.perf_counter()
        op.forward(x)
        times.append(time.perf_counter() - t0)

    times_us = [t * 1e6 for t in times]
    return label, compile_s, times_us


def bench_upsample(channels, h, w):
    """Benchmark an Upsample configuration."""
    label = f"Upsample 2x {channels}ch @ {h}x{w}"
    context = AIEContext(use_runlist=True)
    op = AIEUpsample(
        channels=channels,
        height=h,
        width=w,
        scale_factor=2,
        num_aie_columns=1,
        context=context,
    )

    t0 = time.perf_counter()
    context.compile_all()
    compile_s = time.perf_counter() - t0

    context.prepare_runtime()

    x = (torch.rand(1, channels, h, w) * 2 - 1).to(torch.bfloat16)

    # Warmup
    op.forward(x)

    times = []
    for _ in range(NUM_ITERS):
        t0 = time.perf_counter()
        op.forward(x)
        times.append(time.perf_counter() - t0)

    times_us = [t * 1e6 for t in times]
    return label, compile_s, times_us


def bench_cbs(in_ch, out_ch, k, s, h, w):
    """Benchmark a CBS (Conv+BN+SiLU) block."""
    label = f"CBS k{k}s{s} {in_ch}->{out_ch} @ {h}x{w}"
    context = AIEContext(use_runlist=True)
    cbs = CBS(
        in_channels=in_ch,
        out_channels=out_ch,
        kernel_size=k,
        stride=s,
        height=h,
        width=w,
        num_aie_columns=0,  # auto
        context=context,
    )

    t0 = time.perf_counter()
    context.compile_all()
    compile_s = time.perf_counter() - t0

    context.prepare_runtime()

    # Generate random weights
    weight = (torch.randn(out_ch, in_ch, k, k) * 0.1).to(torch.bfloat16)
    bias = torch.zeros(out_ch, dtype=torch.bfloat16)
    cbs.load_weights(weight, bias)

    x = (torch.rand(1, in_ch, h, w) * 2 - 1).to(torch.bfloat16)

    # Warmup
    cbs.forward(x)

    times = []
    for _ in range(NUM_ITERS):
        t0 = time.perf_counter()
        cbs.forward(x)
        times.append(time.perf_counter() - t0)

    times_us = [t * 1e6 for t in times]
    return label, compile_s, times_us


def bench_bottleneck(channels, h, w):
    """Benchmark a Bottleneck block (two CBS 3x3)."""
    label = f"Bottleneck {channels}ch @ {h}x{w}"
    context = AIEContext(use_runlist=True)
    bn = Bottleneck(
        channels=channels,
        height=h,
        width=w,
        shortcut=True,
        num_aie_columns=0,  # auto
        context=context,
    )

    t0 = time.perf_counter()
    context.compile_all()
    compile_s = time.perf_counter() - t0

    context.prepare_runtime()

    # Generate random weights for both convolutions
    cv1_w = (torch.randn(channels, channels, 3, 3) * 0.1).to(torch.bfloat16)
    cv1_b = torch.zeros(channels, dtype=torch.bfloat16)
    cv2_w = (torch.randn(channels, channels, 3, 3) * 0.1).to(torch.bfloat16)
    cv2_b = torch.zeros(channels, dtype=torch.bfloat16)
    bn.load_weights(cv1_w, cv1_b, cv2_w, cv2_b)

    x = (torch.rand(1, channels, h, w) * 2 - 1).to(torch.bfloat16)

    # Warmup
    bn.forward(x)

    times = []
    for _ in range(NUM_ITERS):
        t0 = time.perf_counter()
        bn.forward(x)
        times.append(time.perf_counter() - t0)

    times_us = [t * 1e6 for t in times]
    return label, compile_s, times_us


def run_bench(name, fn, *args, **kwargs):
    """Run a benchmark with error handling."""
    try:
        result = fn(*args, **kwargs)
        label, compile_s, times_us = result
        mean_us = np.mean(times_us)
        print(f"    {label}: compile={compile_s:.1f}s, "
              f"exec={mean_us:.1f}us (min={np.min(times_us):.1f})")
        return result
    except Exception as e:
        print(f"    FAILED: {e}")
        traceback.print_exc()
        return None


def format_results(results, skipped):
    """Format results as a markdown table."""
    lines = []
    lines.append("# YOLOv8n Operator Benchmark Results")
    lines.append("")
    lines.append(f"- Iterations per config: {NUM_ITERS} (+ 1 warmup)")
    lines.append("- Timing: wall-clock including layout conversion + DMA sync")
    lines.append("")
    lines.append(
        "| Operator | Compile (s) | Mean (us) | Min (us) | Max (us) |"
    )
    lines.append(
        "|----------|-------------|-----------|----------|----------|"
    )
    for label, compile_s, times_us in results:
        mean_us = np.mean(times_us)
        min_us = np.min(times_us)
        max_us = np.max(times_us)
        lines.append(
            f"| {label} | {compile_s:.1f} | {mean_us:.1f} | "
            f"{min_us:.1f} | {max_us:.1f} |"
        )

    if skipped:
        lines.append("")
        lines.append("## Configs that failed to compile")
        lines.append("")
        lines.append("These YOLOv8n-scale configs exceed the DMA BD size "
                      "limit (1023 elements per dimension) and require "
                      "design-level decomposition:")
        lines.append("")
        for label, reason in skipped:
            lines.append(f"- **{label}**: {reason}")

    lines.append("")
    return "\n".join(lines)


def main():
    results = []
    skipped = []

    # --- Conv2d 1x1 ---
    # Note: Full YOLOv8n sizes (64ch@80x80, 128ch@40x40) exceed DMA BD
    # size limits. We use reduced spatial dims that exercise the same kernel.
    print("=== Conv2d 1x1 ===")
    configs_1x1 = [
        (32, 32, 32, 32),   # C2f-like
        (64, 64, 16, 16),   # medium
        (128, 128, 8, 8),   # large channel count, small spatial
        (32, 64, 16, 16),   # channel expansion
        (64, 32, 16, 16),   # channel reduction
    ]
    for in_ch, out_ch, h, w in configs_1x1:
        print(f"  {in_ch}->{out_ch} @ {h}x{w} ...", flush=True)
        r = run_bench("conv1x1", bench_conv2d, in_ch, out_ch, h, w, k=1, s=1)
        if r:
            results.append(r)

    # --- Conv2d 3x3 stride=1 ---
    print("=== Conv2d 3x3 s1 ===")
    configs_3x3s1 = [
        (16, 16, 8, 8),     # Bottleneck internal
        (32, 32, 8, 8),     # Bottleneck internal
        (16, 16, 16, 16),   # medium spatial
        (32, 32, 16, 16),   # larger
    ]
    for in_ch, out_ch, h, w in configs_3x3s1:
        print(f"  {in_ch}->{out_ch} @ {h}x{w} ...", flush=True)
        r = run_bench("conv3x3s1", bench_conv2d, in_ch, out_ch, h, w, k=3, s=1)
        if r:
            results.append(r)

    # --- Conv2d 3x3 stride=2 ---
    print("=== Conv2d 3x3 s2 ===")
    configs_3x3s2 = [
        (8, 16, 16, 16),    # backbone downsampling
        (16, 32, 8, 8),     # backbone downsampling
        (8, 8, 8, 8),       # minimal downsampling
    ]
    for in_ch, out_ch, h, w in configs_3x3s2:
        print(f"  {in_ch}->{out_ch} @ {h}x{w} ...", flush=True)
        r = run_bench("conv3x3s2", bench_conv2d, in_ch, out_ch, h, w, k=3, s=2)
        if r:
            results.append(r)

    # --- MaxPool2d ---
    print("=== MaxPool2d ===")
    for channels, h, w in [(128, 8, 8), (16, 8, 8)]:
        print(f"  {channels}ch @ {h}x{w} k5 ...", flush=True)
        r = run_bench("maxpool", bench_maxpool2d, channels, h, w, k=5)
        if r:
            results.append(r)

    # --- Upsample ---
    print("=== Upsample ===")
    for channels, h, w in [(128, 8, 8), (32, 8, 8)]:
        print(f"  {channels}ch @ {h}x{w} s2 ...", flush=True)
        r = run_bench("upsample", bench_upsample, channels, h, w)
        if r:
            results.append(r)

    # --- CBS block (fused SiLU) ---
    print("=== CBS (fused SiLU) ===")
    cbs_configs = [
        (16, 16, 3, 1, 8, 8),     # Bottleneck-like
        (32, 32, 1, 1, 16, 16),   # C2f pointwise
    ]
    for in_ch, out_ch, k, s, h, w in cbs_configs:
        print(f"  {in_ch}->{out_ch} k{k}s{s} @ {h}x{w} ...", flush=True)
        r = run_bench("cbs", bench_cbs, in_ch, out_ch, k, s, h, w)
        if r:
            results.append(r)

    # --- Bottleneck block ---
    print("=== Bottleneck ===")
    for channels, h, w in [(16, 8, 8)]:
        print(f"  {channels}ch @ {h}x{w} ...", flush=True)
        r = run_bench("bottleneck", bench_bottleneck, channels, h, w)
        if r:
            results.append(r)

    # Document skipped YOLOv8n-scale configs
    skipped.append(
        ("Conv2d k1 64->64 @ 80x80",
         "row_size=64*80=5120 > 1023")
    )
    skipped.append(
        ("Conv2d k1 128->128 @ 40x40",
         "row_size=128*40=5120 > 1023")
    )
    skipped.append(
        ("Conv2d k3 32->64 @ 160x160",
         "row_size=32*160=5120 > 1023")
    )

    # Format and print results
    report = format_results(results, skipped)
    print("\n" + report)

    # Save results
    import os

    out_path = os.path.join(os.path.dirname(__file__), "benchmark_results.md")
    with open(out_path, "w") as f:
        f.write(report)
    print(f"Results saved to {out_path}")


if __name__ == "__main__":
    main()
