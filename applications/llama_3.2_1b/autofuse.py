#!/usr/bin/env python3

import torch
import math
from pathlib import Path
import sys
import numpy as np
import ml_dtypes
import logging
import time
logging.basicConfig(level=logging.DEBUG)

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))

from operators.common.context import AIEContext
from operators.common import AIEOperatorBase, AIEBuffer, SingleMLIRSourceOperator
from operators.common.utils import torch_to_numpy, numpy_to_torch
from operators.common.compilation import SourceArtifact, PythonGeneratedMLIRArtifact
from operators.common.fusion import FusedMLIROperator, FusedFullELFCallable
from operators import AIEGEMV
from operators.elementwise_mul.op import AIEElementwiseMul
from operators.silu.op import AIESiLU


emb_dim = 2048
hidden_dim = 8192

# Operator definitions
# ---

gemv_ffn_up_gate_op = AIEGEMV(
    M=hidden_dim,
    K=emb_dim,
    num_aie_columns=8,
    tile_size_input=4,
    tile_size_output=hidden_dim // 8,
)

gemv_ffn_down_op = AIEGEMV(
    M=emb_dim,
    K=hidden_dim,
    num_aie_columns=8,
    tile_size_input=1,
    tile_size_output=emb_dim // 8,
)

silu_ffn_op = AIESiLU(
    size=hidden_dim,
    tile_size=hidden_dim // 8,
    num_aie_columns=8,
)

eltwise_mul_ffn_op = AIEElementwiseMul(
    size=hidden_dim,
    tile_size=hidden_dim // 8,
    num_aie_columns=8,
)


# Buffers
# ---

# Create identity matrix for W_ffn_gate (repeating pattern for hidden_dim x emb_dim)
# Each row i will pick element i % emb_dim from x_norm
W_ffn_gate = torch.zeros(hidden_dim, emb_dim, dtype=torch.bfloat16)
for i in range(hidden_dim):
    W_ffn_gate[i, i % emb_dim] = 1.0

W_ffn_up = torch.randn(hidden_dim, emb_dim, dtype=torch.bfloat16)

W_ffn_down = torch.zeros(emb_dim, hidden_dim, dtype=torch.bfloat16)
for i in range(emb_dim):
    W_ffn_down[i, i] = 1.0

buf_W_ffn_gate = AIEBuffer.from_torch(W_ffn_gate)
buf_W_ffn_up = AIEBuffer.from_torch(W_ffn_up)
buf_W_ffn_down = AIEBuffer.from_torch(W_ffn_down)

# Create x_norm as sequential indices: [0, 1, 2, 3, ..., emb_dim-1]
x_norm = torch.arange(emb_dim, dtype=torch.bfloat16)
buf_x_norm = AIEBuffer.from_torch(x_norm)
buf_ffn_gate = AIEBuffer.from_torch(torch.zeros(hidden_dim, dtype=torch.bfloat16))
buf_ffn_up = AIEBuffer.from_torch(torch.zeros(hidden_dim, dtype=torch.bfloat16))
ffn_hidden = torch.arange(hidden_dim, dtype=torch.bfloat16)
buf_ffn_hidden = AIEBuffer.from_torch(ffn_hidden)
buf_ffn_output = AIEBuffer.from_torch(-1 * torch.arange(emb_dim, dtype=torch.bfloat16)) #torch.zeros(emb_dim, dtype=torch.bfloat16))


# Separate xclbins
# ---

gemv_ffn_up_gate = None
gemv_ffn_down = None
silu_ffn = None
eltwise_mul_ffn = None

def setup_separate_xclbins():
    global gemv_ffn_up_gate, gemv_ffn_down, silu_ffn, eltwise_mul_ffn
    ctx = AIEContext(build_dir="build_separate")
    gemv_ffn_up_gate_op.context = ctx
    gemv_ffn_down_op.context = ctx
    silu_ffn_op.context = ctx
    eltwise_mul_ffn_op.context = ctx
    gemv_ffn_up_gate = gemv_ffn_up_gate_op.compile().get_callable()
    gemv_ffn_down = gemv_ffn_down_op.compile().get_callable()
    silu_ffn = silu_ffn_op.compile().get_callable()
    eltwise_mul_ffn = eltwise_mul_ffn_op.compile().get_callable()

def run_separate_xclbins():
    gemv_ffn_up_gate(buf_W_ffn_gate, buf_x_norm, buf_ffn_gate)  # Gate projection
    gemv_ffn_up_gate(buf_W_ffn_up, buf_x_norm, buf_ffn_up)  # Up projection
    silu_ffn(buf_ffn_gate, buf_ffn_gate)  # SiLU activation
    eltwise_mul_ffn(buf_ffn_gate, buf_ffn_up, buf_ffn_hidden)  # Gate application (eltwise mul)
    gemv_ffn_down(buf_W_ffn_down, buf_ffn_hidden, buf_ffn_output)  # Down projection
    return buf_ffn_output.to("cpu").view_as_torch()


# Autofused
# ---

def setup_autofused():
    ctx = AIEContext(build_dir="build_autofused")
    gemv_ffn_up_gate_op.context = ctx
    gemv_ffn_down_op.context = ctx
    silu_ffn_op.context = ctx
    eltwise_mul_ffn_op.context = ctx
    global swiglu_fused_op, swiglu_fused
    swiglu_fused_op = FusedMLIROperator(
        "swiglu",
        [
            (gemv_ffn_up_gate_op, "W_ffn_gate", "x_norm", "ffn_gate"),
            (gemv_ffn_up_gate_op, "W_ffn_up", "x_norm", "ffn_up"),
            (silu_ffn_op, "ffn_gate", "ffn_gate"),
            (eltwise_mul_ffn_op, "ffn_gate", "ffn_up", "ffn_hidden"),
            (gemv_ffn_down_op, "W_ffn_down", "ffn_hidden", "ffn_output"),
        ],
        input_args=[
            "x_norm",
            "W_ffn_gate",
            "W_ffn_up",
            "W_ffn_down"
        ],
        output_args=[
            "ffn_output"
        ],
    )
    swiglu_fused_op.context = ctx
    swiglu_fused = swiglu_fused_op.compile().get_callable()

    swiglu_fused.get_buffer("x_norm").view_as_torch()[:] = x_norm.flatten()
    swiglu_fused.get_buffer("W_ffn_gate").view_as_torch()[:] = W_ffn_gate.flatten()
    swiglu_fused.get_buffer("W_ffn_up").view_as_torch()[:] = W_ffn_up.flatten()
    swiglu_fused.get_buffer("W_ffn_down").view_as_torch()[:] = W_ffn_down.flatten()

def run_autofused():
    swiglu_fused()
    return swiglu_fused.get_buffer("ffn_output").to("cpu").view_as_torch()

# CPU
# ---

def run_cpu():
    ffn_gate = torch.matmul(W_ffn_gate, x_norm)
    ffn_up = torch.matmul(W_ffn_up, x_norm)
    ffn_gate = torch.nn.functional.silu(ffn_gate)
    ffn_hidden = ffn_gate * ffn_up
    ffn_output = torch.matmul(W_ffn_down, ffn_hidden)
    return ffn_output


# Main
# ---

iters=100

setup_autofused()
t_autofused_start = time.time()
for _ in range(iters):
    res_npu = run_autofused()
t_autofused = time.time() - t_autofused_start

setup_separate_xclbins()
t_separate_start = time.time()
for _ in range(iters):
    res_npu_s = run_separate_xclbins()
t_separate = time.time() - t_separate_start

t_cpu_start = time.time()
for _ in range(iters):
    res_cpu = run_cpu()
t_cpu = time.time() - t_cpu_start

print(res_npu_s)
print(res_npu)
print(res_cpu)


print(f"Separate xclbins time: {t_separate/iters:.6f} seconds")
print(f"Autofused time:        {t_autofused/iters:.6f} seconds")
print(f"CPU time:              {t_cpu/iters:.6f} seconds")
assert(torch.allclose(res_npu[-1], res_cpu[-1], atol=0.7, rtol=0.07))
