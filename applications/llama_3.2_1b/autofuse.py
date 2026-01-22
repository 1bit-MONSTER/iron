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
    num_aie_columns=1,
    tile_size_input=4,
    tile_size_output=hidden_dim // 8,
)

gemv_ffn_down_op = AIEGEMV(
    M=emb_dim,
    K=hidden_dim,
    num_aie_columns=1,
    tile_size_input=1,
    tile_size_output=emb_dim // 8,
)

silu_ffn_op = AIESiLU(
    size=hidden_dim,
    tile_size=hidden_dim // 8,
    num_aie_columns=1,
)

eltwise_mul_ffn_op = AIEElementwiseMul(
    size=hidden_dim,
    tile_size=hidden_dim // 8,
    num_aie_columns=1,
)


# Buffers
# ---

buf_W_ffn_gate = AIEBuffer.from_torch(torch.randn(hidden_dim, emb_dim, dtype=torch.bfloat16))
buf_W_ffn_up = AIEBuffer.from_torch(torch.randn(hidden_dim, emb_dim, dtype=torch.bfloat16))
buf_W_ffn_down = AIEBuffer.from_torch(torch.randn(emb_dim, hidden_dim, dtype=torch.bfloat16))
buf_x_norm = AIEBuffer.from_torch(torch.randn(emb_dim, dtype=torch.bfloat16))
buf_ffn_gate = AIEBuffer.from_torch(torch.zeros(hidden_dim, dtype=torch.bfloat16))
buf_ffn_up = AIEBuffer.from_torch(torch.zeros(hidden_dim, dtype=torch.bfloat16))
buf_ffn_hidden = AIEBuffer.from_torch(torch.zeros(hidden_dim, dtype=torch.bfloat16))
buf_ffn_output = AIEBuffer.from_torch(torch.zeros(emb_dim, dtype=torch.bfloat16))


# Separate xclbins
# ---

gemv_ffn_up_gate = None
gemv_ffn_down = None
silu_ffn = None
eltwise_mul_ffn = None

def setup_separate_xclbins():
    global gemv_ffn_up_gate, gemv_ffn_down, silu_ffn, eltwise_mul_ffn
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
    global swiglu_fused_op, swiglu_fused
    swiglu_fused_op = FusedMLIROperator(
        "swiglu",
        [
            (gemv_ffn_up_gate_op, "W_ffn_gate", "x_norm", "inter_ffn_gate"),
            (gemv_ffn_up_gate_op, "W_ffn_up", "x_norm", "inter_ffn_up"),
            (silu_ffn_op, "inter_ffn_gate", "inter_ffn_gate"),
            (eltwise_mul_ffn_op, "inter_ffn_gate", "inter_ffn_up", "inter_ffn_hidden"),
            (gemv_ffn_down_op, "W_ffn_down", "inter_ffn_hidden", "ffn_output"),
        ],
        input_args=[
            "x_norm",
            "W_ffn_gate",
            "W_ffn_up",
            "W_ffn_down"
        ],
        output_args=[
            "ffn_output"
        ]
    )
    swiglu_fused = swiglu_fused_op.compile().get_callable()

def run_autofused():
    swiglu_fused.get_buffer("x_norm").view_as_torch()[:] = buf_x_norm.view_as_torch()
    swiglu_fused.get_buffer("W_ffn_gate").view_as_torch()[:] = buf_W_ffn_gate.view_as_torch()
    swiglu_fused.get_buffer("W_ffn_up").view_as_torch()[:] = buf_W_ffn_up.view_as_torch()
    swiglu_fused.get_buffer("W_ffn_down").view_as_torch()[:] = buf_W_ffn_down.view_as_torch()
    swiglu_fused.get_buffer("ffn_output").view_as_torch()[:] = buf_ffn_output.view_as_torch()
    swiglu_fused()
    return swiglu_fused.get_buffer("ffn_output").view_as_torch()

# CPU
# ---

def run_cpu():
    x_norm = buf_x_norm.view_as_torch()
    W_ffn_gate = buf_W_ffn_gate.view_as_torch()
    W_ffn_up = buf_W_ffn_up.view_as_torch()
    W_ffn_down = buf_W_ffn_down.view_as_torch()

    ffn_gate = torch.matmul(W_ffn_gate, x_norm)
    ffn_up = torch.matmul(W_ffn_up, x_norm)
    ffn_gate = torch.nn.functional.silu(ffn_gate)
    ffn_hidden = ffn_gate * ffn_up
    ffn_output = torch.matmul(W_ffn_down, ffn_hidden)

    return ffn_output


# Main
# ---

setup_autofused()
print(run_autofused())
setup_separate_xclbins()
print(run_separate_xclbins())
print(run_cpu())
