#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Debug attn_block_decode phase by phase.
#
# Runs each phase as a standalone operator, then compares against the fused
# design's output at each stage.
#
# Phases:
#   1. RMSNorm:       x -> norm_x
#   2. QKV GEMV:      norm_x -> Q, K, V
#   3. FlowKV:        Q + KV_cache -> attn_out
#   4. Output GEMV:   attn_out -> proj_out
#   5. Residual Add:  x + proj_out -> output

import sys
import os
import torch
import torch.nn as nn
import numpy as np
from ml_dtypes import bfloat16 as ml_bf16

os.chdir("/scratch/jmelber/IRON")
sys.path.insert(0, "/scratch/jmelber/IRON")

from iron.common import AIEContext
from iron.common.test_utils import nearly_equal
from iron.common.utils import torch_to_numpy
from iron.operators.rms_norm.op import AIERMSNorm
from iron.operators.gemv.op import AIEGEMV
from iron.operators.flowkv_decode.op import AIEFlowKVDecode, pack_q_with_angles
from iron.operators.flowkv_decode.reference import interleave_kv_cache
from iron.operators.elementwise_add.op import AIEElementwiseAdd
from iron.operators.attn_block_decode.reference import generate_golden_reference

EMB = 2048
NH = 32
NKV = 8
HD = 64
SL = 128
GS = NH // NKV  # 4
Q_DIM = NH * HD  # 2048
KV_DIM = NKV * HD  # 512


def sep(title):
    print()
    print("=" * 70)
    print(f"  {title}")
    print("=" * 70)


def check(name, actual, expected, rel_tol=0.04, abs_tol=1e-6, max_print=5):
    a = torch_to_numpy(actual.flatten()).reshape(-1)
    e = torch_to_numpy(expected.flatten()).reshape(-1)
    assert len(a) == len(e), f"length mismatch: {len(a)} vs {len(e)}"
    errs = []
    for i in range(len(a)):
        if not nearly_equal(float(a[i]), float(e[i]), rel_tol, abs_tol):
            errs.append(i)
            if len(errs) <= max_print:
                print(
                    f"  [{name}][{i}]: expected {float(e[i]):.4f}, "
                    f"got {float(a[i]):.4f}, diff {abs(float(a[i])-float(e[i])):.4f}"
                )
    status = "PASS" if not errs else f"FAIL ({len(errs)}/{len(a)})"
    print(f"  {name}: {status} (tol={rel_tol}/{abs_tol})")
    return errs


# =========================================================================
sep("Step 0: Generate golden reference")
golden = generate_golden_reference(EMB, NH, NKV, HD, SL)
x = golden["x"]
norm_w = golden["norm_weight"]
w_q, w_k, w_v, w_o = golden["w_q"], golden["w_k"], golden["w_v"], golden["w_o"]
x_normed_ref = golden["x_normed"]
q_ref = golden["q"]  # (NH, HD) unrotated
Q_rot_ref = golden["Q_rotated"]  # (NH, HD) rotated
K_cache = golden["K_cache"]  # (NKV, SL, HD)
V_cache = golden["V_cache"]  # (NKV, SL, HD)
q_angles = golden["q_angles"]
attn_out_ref = golden["attn_out"]  # (NH, HD)
proj_out_ref = golden["proj_out"]  # (EMB,)
output_ref = golden["output"]  # (EMB,)

print(f"x[:3] = {x[:3].tolist()}")
print(f"x_normed[:3] = {x_normed_ref[:3].tolist()}")
print(f"output[:3] = {output_ref[:3].tolist()}")


# =========================================================================
sep("Step 1: Standalone RMSNorm")
ctx1 = AIEContext()
rms = AIERMSNorm(
    size=EMB, num_aie_columns=1, num_channels=2,
    tile_size=EMB, weighted=True, context=ctx1,
)
rms.weight = nn.Parameter(norm_w.clone())
ctx1.compile_all()
ctx1.prepare_runtime()

norm_x_aie = rms(x)
check("RMSNorm", norm_x_aie, x_normed_ref, rel_tol=0.04, abs_tol=1e-6)


# =========================================================================
sep("Step 2: Standalone QKV GEMV (3 separate)")
ctx2 = AIEContext()

q_gemv = AIEGEMV(
    M=Q_DIM, K=EMB, tile_size_input=4, tile_size_output=Q_DIM // 8,
    num_aie_columns=8, is_mv=False, use_static_weight=True, context=ctx2,
)
q_gemv.weight = w_q

k_gemv = AIEGEMV(
    M=KV_DIM, K=EMB, tile_size_input=4, tile_size_output=KV_DIM // 8,
    num_aie_columns=8, is_mv=False, use_static_weight=True, context=ctx2,
)
k_gemv.weight = w_k

v_gemv = AIEGEMV(
    M=KV_DIM, K=EMB, tile_size_input=4, tile_size_output=KV_DIM // 8,
    num_aie_columns=8, is_mv=False, use_static_weight=True, context=ctx2,
)
v_gemv.weight = w_v

ctx2.compile_all()
ctx2.prepare_runtime()

# Feed reference norm_x (isolate QKV from RMSNorm errors)
x_flat = x_normed_ref.reshape(1, -1)
q_aie = q_gemv(x_flat).reshape(NH, HD)
k_aie = k_gemv(x_flat).reshape(NKV, HD)
v_aie = v_gemv(x_flat).reshape(NKV, HD)

q_ref_flat = (w_q @ x_normed_ref).reshape(NH, HD)
check("Q GEMV", q_aie, q_ref_flat, rel_tol=0.07, abs_tol=0.7)
check("K GEMV", k_aie, golden["k_new"], rel_tol=0.07, abs_tol=0.7)
check("V GEMV", v_aie, golden["v_new"], rel_tol=0.07, abs_tol=0.7)


# =========================================================================
sep("Step 3: Standalone FlowKV")
ctx3 = AIEContext()
flowkv = AIEFlowKVDecode(
    num_heads=NH, num_kv_heads=NKV, head_dim=HD,
    seq_len=SL, chunk_size=32, num_cols=4, context=ctx3,
)
ctx3.compile_all()
ctx3.prepare_runtime()

# Feed reference Q (unrotated — FlowKV applies RoPE internally)
attn_aie = flowkv(q_ref, K_cache, V_cache, q_angles)
check("FlowKV", attn_aie, attn_out_ref, rel_tol=0.07, abs_tol=0.7)


# =========================================================================
sep("Step 4: Standalone Output GEMV")
ctx4 = AIEContext()
o_gemv = AIEGEMV(
    M=EMB, K=Q_DIM, tile_size_input=4, tile_size_output=EMB // 8,
    num_aie_columns=8, is_mv=False, use_static_weight=True, context=ctx4,
)
o_gemv.weight = w_o
ctx4.compile_all()
ctx4.prepare_runtime()

# Feed reference attn_out (isolate OProj from FlowKV errors)
attn_flat = attn_out_ref.reshape(1, -1)
proj_aie = o_gemv(attn_flat).reshape(-1)
check("OProj GEMV", proj_aie, proj_out_ref, rel_tol=0.07, abs_tol=0.7)


# =========================================================================
sep("Step 5: Standalone Residual Add")
ctx5 = AIEContext()
add_op = AIEElementwiseAdd(
    size=EMB, num_aie_columns=1, num_channels=2,
    tile_size=EMB, context=ctx5,
)
ctx5.compile_all()
ctx5.prepare_runtime()

# Feed reference proj_out
out_aie = add_op(proj_out_ref, x)
check("Residual Add", out_aie, output_ref, rel_tol=0.04, abs_tol=1e-6)


# =========================================================================
sep("Step 6: Chained standalone (RMS -> Q GEMV -> FlowKV -> O GEMV -> Add)")
# Use each standalone operator's actual output as input to the next
norm_x_chain = rms(x)

q_chain = q_gemv(norm_x_chain.reshape(1, -1)).reshape(NH, HD)
# k_chain and v_chain are unused by FlowKV (it reads from KV cache)

attn_chain = flowkv(q_chain, K_cache, V_cache, q_angles)
proj_chain = o_gemv(attn_chain.reshape(1, -1)).reshape(-1)
out_chain = add_op(proj_chain, x)

print("Chained standalone vs reference:")
check("Chained output", out_chain, output_ref, rel_tol=0.30, abs_tol=1.0)
check("Chained output (wide)", out_chain, output_ref, rel_tol=0.90, abs_tol=100.0)


# =========================================================================
sep("Step 7: Fused attn_block_decode")
from iron.operators.attn_block_decode.op import AIEAttnBlockDecode

ctx7 = AIEContext()
fused = AIEAttnBlockDecode(
    embedding_dim=EMB, num_heads=NH, num_kv_heads=NKV,
    head_dim=HD, seq_len=SL, context=ctx7,
)
fused.norm_weight = norm_w
fused.w_q = w_q
fused.w_k = w_k
fused.w_v = w_v
fused.w_o = w_o

ctx7.compile_all()
ctx7.prepare_runtime()

out_fused = fused.forward(x, K_cache, V_cache, q_angles)

print("Fused vs reference:")
check("Fused output", out_fused, output_ref, rel_tol=0.30, abs_tol=1.0)
check("Fused output (wide)", out_fused, output_ref, rel_tol=0.90, abs_tol=100.0)

print()
print("Fused vs chained standalone:")
check("Fused vs chain", out_fused, out_chain, rel_tol=0.30, abs_tol=1.0)
check("Fused vs chain (wide)", out_fused, out_chain, rel_tol=0.90, abs_tol=100.0)

# =========================================================================
sep("Summary")
print("If standalone phases all PASS but fused FAILS:")
print("  -> Bug is in the fused design's data flow between phases")
print("If chained standalone also FAILS:")
print("  -> Error amplification through the pipeline (expected for bf16)")
print("If fused matches chained but both differ from reference:")
print("  -> Normal bf16 accumulation error, widen tolerance")
