#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Benchmark: mlp_block_decode (fused) vs separate RMSNorm + SwiGLUFusedDecode
#
# Measures latency of both approaches at Llama 3.2 1B dimensions:
#   embedding_dim=2048, hidden_dim=8192

import time
import torch
import numpy as np
from ml_dtypes import bfloat16 as ml_bfloat16

from iron.common import AIEContext
from iron.common.utils import torch_to_numpy
from iron.operators.rms_norm.op import AIERMSNorm
from iron.operators.swiglu_fused_decode.op import AIESwiGLUFusedDecode
from iron.operators.mlp_block_decode.op import AIEMLPBlockDecode
from iron.operators.mlp_block_decode.reference import generate_golden_reference

EMBEDDING_DIM = 2048
HIDDEN_DIM = 8192
WARMUP = 3
ITERS = 20


def bench_separate():
    """Current decode path: standalone RMSNorm + standalone SwiGLUFusedDecode."""
    golden = generate_golden_reference(EMBEDDING_DIM, HIDDEN_DIM)

    ctx = AIEContext()

    # RMSNorm operator (weighted, 1 col, 2 channels)
    rms = AIERMSNorm(
        size=EMBEDDING_DIM,
        num_aie_columns=1,
        num_channels=2,
        tile_size=EMBEDDING_DIM,
        weighted=True,
        context=ctx,
    )
    import torch.nn as nn

    rms.weight = nn.Parameter(golden["norm_weight"].clone())

    # SwiGLU fused decode
    swiglu = AIESwiGLUFusedDecode(
        embedding_dim=EMBEDDING_DIM,
        hidden_dim=HIDDEN_DIM,
        context=ctx,
    )
    swiglu.weights_gate = golden["w_gate"]
    swiglu.weights_up = golden["w_up"]
    swiglu.weights_down = golden["w_down"]

    ctx.compile_all()
    ctx.prepare_runtime()

    x = golden["x"]

    # Warmup
    for _ in range(WARMUP):
        norm_x = rms(x)
        _ = swiglu(norm_x)

    # Benchmark
    latencies = []
    for _ in range(ITERS):
        t0 = time.perf_counter_ns()
        norm_x = rms(x)
        out = swiglu(norm_x)
        t1 = time.perf_counter_ns()
        latencies.append((t1 - t0) / 1e3)  # us

    return latencies


def bench_fused():
    """New fused path: mlp_block_decode (RMSNorm + SwiGLU in one xclbin)."""
    golden = generate_golden_reference(EMBEDDING_DIM, HIDDEN_DIM)

    ctx = AIEContext()

    op = AIEMLPBlockDecode(
        embedding_dim=EMBEDDING_DIM,
        hidden_dim=HIDDEN_DIM,
        context=ctx,
    )
    op.norm_weight = golden["norm_weight"]
    op.weights_gate = golden["w_gate"]
    op.weights_up = golden["w_up"]
    op.weights_down = golden["w_down"]

    ctx.compile_all()
    ctx.prepare_runtime()

    x = golden["x"]

    # Warmup
    for _ in range(WARMUP):
        _ = op(x)

    # Benchmark
    latencies = []
    for _ in range(ITERS):
        t0 = time.perf_counter_ns()
        out = op(x)
        t1 = time.perf_counter_ns()
        latencies.append((t1 - t0) / 1e3)  # us

    return latencies


def print_stats(name, latencies):
    arr = np.array(latencies)
    print(f"  {name}:")
    print(f"    min    = {arr.min():>10.1f} us")
    print(f"    median = {np.median(arr):>10.1f} us")
    print(f"    mean   = {arr.mean():>10.1f} us")
    print(f"    max    = {arr.max():>10.1f} us")
    print(f"    std    = {arr.std():>10.1f} us")
    return np.median(arr)


if __name__ == "__main__":
    print(f"Benchmark: MLP decode block ({EMBEDDING_DIM}x{HIDDEN_DIM})")
    print(f"  Warmup iterations: {WARMUP}")
    print(f"  Measured iterations: {ITERS}")
    print()

    print("Building separate operators (RMSNorm + SwiGLUFusedDecode)...")
    sep_lats = bench_separate()

    print("Building fused operator (MLPBlockDecode)...")
    fused_lats = bench_fused()

    print()
    print("=" * 60)
    print("Results")
    print("=" * 60)
    sep_med = print_stats("Separate (RMSNorm + SwiGLUFusedDecode)", sep_lats)
    fused_med = print_stats("Fused (MLPBlockDecode)", fused_lats)
    print()

    speedup = sep_med / fused_med
    saved = sep_med - fused_med
    print(f"  Speedup: {speedup:.2f}x ({saved:.0f} us saved per call)")
    print(f"  Per-layer savings (16 layers): {saved * 16 / 1000:.1f} ms/token")
