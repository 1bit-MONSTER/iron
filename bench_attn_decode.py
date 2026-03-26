#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Benchmark: Attention block decode — separate operators
#
# Measures the full decode attention block as individual operator calls,
# matching the current Llama decode path:
#   RMSNorm → QKV GEMV (3x or fused) → RoPE → FlowKV → Output GEMV → Residual Add
#
# The attn_block_decode fused design exceeds ShimDMA limits with
# SequentialPlacer (it can't reuse channels across task_groups), so
# we benchmark the separate path and report kernel-launch overhead
# that fusion would eliminate.

import time
import torch
import numpy as np
from ml_dtypes import bfloat16 as ml_bfloat16

from iron.common import AIEContext
from iron.common.utils import torch_to_numpy
from iron.operators.rms_norm.op import AIERMSNorm
from iron.operators.gemv.op import AIEGEMV
from iron.operators.flowkv_decode.op import AIEFlowKVDecode
from iron.operators.flowkv_decode.op import pack_q_with_angles
from iron.operators.flowkv_decode.reference import interleave_kv_cache
from iron.operators.elementwise_add.op import AIEElementwiseAdd
from iron.operators.attn_block_decode.reference import (
    generate_golden_reference,
    apply_rope_two_halves,
    make_rope_angles_interleaved,
)

EMBEDDING_DIM = 2048
NUM_HEADS = 32
NUM_KV_HEADS = 8
HEAD_DIM = 64
SEQ_LEN = 128
WARMUP = 3
ITERS = 20

Q_DIM = NUM_HEADS * HEAD_DIM       # 2048
KV_DIM = NUM_KV_HEADS * HEAD_DIM   # 512
GROUP_SIZE = NUM_HEADS // NUM_KV_HEADS  # 4


def bench_separate():
    """Current decode attention: separate AIE operators."""
    golden = generate_golden_reference(
        EMBEDDING_DIM, NUM_HEADS, NUM_KV_HEADS, HEAD_DIM, SEQ_LEN
    )

    ctx = AIEContext()

    # 1. RMSNorm
    import torch.nn as nn
    rms = AIERMSNorm(
        size=EMBEDDING_DIM, num_aie_columns=1, num_channels=2,
        tile_size=EMBEDDING_DIM, weighted=True, context=ctx,
    )
    rms.weight = nn.Parameter(golden["norm_weight"].clone())

    # 2. Q projection GEMV
    q_gemv = AIEGEMV(
        M=Q_DIM, K=EMBEDDING_DIM,
        tile_size_input=4, tile_size_output=Q_DIM // 8,
        num_aie_columns=8, is_mv=False, use_static_weight=True,
        context=ctx,
    )
    q_gemv.weight = golden["w_q"]

    # 3. K projection GEMV
    k_gemv = AIEGEMV(
        M=KV_DIM, K=EMBEDDING_DIM,
        tile_size_input=4, tile_size_output=KV_DIM // 8,
        num_aie_columns=8, is_mv=False, use_static_weight=True,
        context=ctx,
    )
    k_gemv.weight = golden["w_k"]

    # 4. V projection GEMV
    v_gemv = AIEGEMV(
        M=KV_DIM, K=EMBEDDING_DIM,
        tile_size_input=4, tile_size_output=KV_DIM // 8,
        num_aie_columns=8, is_mv=False, use_static_weight=True,
        context=ctx,
    )
    v_gemv.weight = golden["w_v"]

    # 5. FlowKV attention (seq_len must be divisible by chunk_size)
    flowkv_seq_len = SEQ_LEN  # Use cache length without the new token for benchmark
    flowkv = AIEFlowKVDecode(
        num_heads=NUM_HEADS, num_kv_heads=NUM_KV_HEADS,
        head_dim=HEAD_DIM, seq_len=flowkv_seq_len,
        chunk_size=32, num_cols=4, context=ctx,
    )

    # 6. Output projection GEMV
    o_gemv = AIEGEMV(
        M=EMBEDDING_DIM, K=Q_DIM,
        tile_size_input=4, tile_size_output=EMBEDDING_DIM // 8,
        num_aie_columns=8, is_mv=False, use_static_weight=True,
        context=ctx,
    )
    o_gemv.weight = golden["w_o"]

    # 7. Residual add
    add_op = AIEElementwiseAdd(
        size=EMBEDDING_DIM, num_aie_columns=1, num_channels=2,
        tile_size=EMBEDDING_DIM, context=ctx,
    )

    print("  Compiling 7 operators...")
    ctx.compile_all()
    ctx.prepare_runtime()
    print("  Ready.")

    x = golden["x"]
    q_angles = golden["q_angles"]

    # Precompute RoPE angles
    half_dim = HEAD_DIM // 2
    inv_freq = 1.0 / (10000.0 ** (torch.arange(0, HEAD_DIM, 2, dtype=torch.float32) / HEAD_DIM))
    new_pos = SEQ_LEN
    new_cos = torch.cos(torch.tensor([new_pos], dtype=torch.float32) * inv_freq).squeeze(0)
    new_sin = torch.sin(torch.tensor([new_pos], dtype=torch.float32) * inv_freq).squeeze(0)

    # Precompute KV cache (use original cache without new token for FlowKV benchmark)
    kv_cache_updated = golden["K_cache"]  # (num_kv_heads, SEQ_LEN, head_dim)
    vv_cache_updated = golden["V_cache"]  # (num_kv_heads, SEQ_LEN, head_dim)

    def run_one():
        # 1. RMSNorm
        norm_x = rms(x)

        # 2-4. QKV projections
        x_flat = norm_x.reshape(1, -1)
        q_flat = q_gemv(x_flat).reshape(NUM_HEADS, HEAD_DIM)
        k_flat = k_gemv(x_flat).reshape(NUM_KV_HEADS, HEAD_DIM)
        v_flat = v_gemv(x_flat).reshape(NUM_KV_HEADS, HEAD_DIM)

        # 5. RoPE (CPU — matches current Llama path)
        q_rot = apply_rope_two_halves(q_flat.float(), new_cos, new_sin).to(torch.bfloat16)

        # 6. FlowKV attention (includes fused RoPE on Q, but we pass pre-rotated)
        # For fair benchmark, call FlowKV with the full KV cache
        attn_out = flowkv(q_flat, kv_cache_updated, vv_cache_updated, q_angles)
        attn_out_flat = attn_out.reshape(1, -1)

        # 7. Output projection
        proj_out = o_gemv(attn_out_flat).reshape(-1)

        # 8. Residual add
        out = add_op(proj_out, x)
        return out

    # Warmup
    for _ in range(WARMUP):
        run_one()

    # Benchmark
    latencies = []
    component_times = {"rms": [], "q_gemv": [], "k_gemv": [], "v_gemv": [],
                       "flowkv": [], "o_gemv": [], "add": []}
    for _ in range(ITERS):
        t_total_0 = time.perf_counter_ns()

        t0 = time.perf_counter_ns()
        norm_x = rms(x)
        t1 = time.perf_counter_ns()
        component_times["rms"].append((t1 - t0) / 1e3)

        x_flat = norm_x.reshape(1, -1)

        t0 = time.perf_counter_ns()
        q_flat = q_gemv(x_flat).reshape(NUM_HEADS, HEAD_DIM)
        t1 = time.perf_counter_ns()
        component_times["q_gemv"].append((t1 - t0) / 1e3)

        t0 = time.perf_counter_ns()
        k_flat = k_gemv(x_flat).reshape(NUM_KV_HEADS, HEAD_DIM)
        t1 = time.perf_counter_ns()
        component_times["k_gemv"].append((t1 - t0) / 1e3)

        t0 = time.perf_counter_ns()
        v_flat = v_gemv(x_flat).reshape(NUM_KV_HEADS, HEAD_DIM)
        t1 = time.perf_counter_ns()
        component_times["v_gemv"].append((t1 - t0) / 1e3)

        t0 = time.perf_counter_ns()
        attn_out = flowkv(q_flat, kv_cache_updated, vv_cache_updated, q_angles)
        t1 = time.perf_counter_ns()
        component_times["flowkv"].append((t1 - t0) / 1e3)

        attn_out_flat = attn_out.reshape(1, -1)

        t0 = time.perf_counter_ns()
        proj_out = o_gemv(attn_out_flat).reshape(-1)
        t1 = time.perf_counter_ns()
        component_times["o_gemv"].append((t1 - t0) / 1e3)

        t0 = time.perf_counter_ns()
        out = add_op(proj_out, x)
        t1 = time.perf_counter_ns()
        component_times["add"].append((t1 - t0) / 1e3)

        t_total_1 = time.perf_counter_ns()
        latencies.append((t_total_1 - t_total_0) / 1e3)

    return latencies, component_times


def print_stats(name, latencies):
    arr = np.array(latencies)
    print(f"  {name}:")
    print(f"    min    = {arr.min():>10.1f} us")
    print(f"    median = {np.median(arr):>10.1f} us")
    print(f"    mean   = {arr.mean():>10.1f} us")
    print(f"    max    = {arr.max():>10.1f} us")
    return np.median(arr)


if __name__ == "__main__":
    print(f"Benchmark: Attention decode block")
    print(f"  {EMBEDDING_DIM}d, {NUM_HEADS}h, {NUM_KV_HEADS}kv, {HEAD_DIM}hd, {SEQ_LEN}sl")
    print(f"  Warmup: {WARMUP}, Measured: {ITERS}")
    print()

    print("Separate operators (RMSNorm + 3×GEMV + FlowKV + GEMV + Add):")
    sep_lats, comp_times = bench_separate()

    print()
    print("=" * 60)
    print("Results — Separate Attention Decode Block")
    print("=" * 60)
    total_med = print_stats("Total", sep_lats)
    print()
    print("  Component breakdown (median, us):")
    for name, times in comp_times.items():
        med = np.median(times)
        print(f"    {name:>10s}: {med:>8.1f} us")
    print()

    # Estimate kernel-launch overhead that fusion would save
    # Each kernel launch has overhead (~75 us based on mlp_block benchmark)
    num_ops = 7  # rms, q, k, v, flowkv, o, add
    overhead_per_launch = 75  # us estimate
    total_overhead = num_ops * overhead_per_launch
    print(f"  Kernel launches: {num_ops}")
    print(f"  Est. launch overhead: ~{overhead_per_launch} us/launch × {num_ops} = ~{total_overhead} us")
    print(f"  Est. fused savings: ~{total_overhead} us → ~{total_med - total_overhead:.0f} us fused target")
    print(f"  Per-layer savings (16 layers): ~{total_overhead * 16 / 1000:.1f} ms/token")
    print()
    print("  NOTE: attn_block_decode fused design exceeds ShimDMA limits with")
    print("  SequentialPlacer (can't reuse channels across task_groups).")
    print("  Needs MLIR-AIE placer support or split into 2-3 smaller fusions.")
