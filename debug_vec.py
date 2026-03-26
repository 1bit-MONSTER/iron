# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Debug vectorized conv2dk1_i8 - compare scalar and vectorized outputs."""

import torch
import numpy as np
from iron.common import AIEContext
from iron.operators.conv2d_int8.op import AIEConv2dInt8
from iron.operators.conv2d_int8.reference import conv2d_int8_reference

torch.manual_seed(42)

ic, oc, h, w = 32, 32, 32, 32  # 32x32 spatial, width=32 (divisible by 32)
scale = 10

print(f"Config: {ic}->{oc} k1 {h}x{w}, scale={scale}")
print(f"can_vectorize: width%32={w%32}, IC>16: {ic>=24}")

# Build and run
ctx = AIEContext()
op = AIEConv2dInt8(ic, oc, 1, 1, h, w, scale=scale, context=ctx)
ctx.compile_all()
ctx.prepare_runtime()

# Simple test input: small values
x = torch.randint(-5, 5, (1, ic, h, w), dtype=torch.int8)
wt = torch.randint(-3, 3, (oc, ic, 1, 1), dtype=torch.int8)

npu_out = op.forward(x, wt)
ref_out = conv2d_int8_reference(x, wt, scale=scale)

diff = (npu_out.float() - ref_out.float()).abs()
print(f"Max diff: {diff.max().item()}")
print(f"Mean diff: {diff.mean().item():.3f}")
print(f"Num mismatches: {(diff > 1).sum().item()} / {diff.numel()}")

# Show first few mismatches
if diff.max().item() > 1:
    indices = torch.where(diff > 1)
    for i in range(min(10, len(indices[0]))):
        n, c, y, x_idx = [idx[i].item() for idx in indices]
        print(f"  [{n},{c},{y},{x_idx}] npu={npu_out[n,c,y,x_idx].item()} ref={ref_out[n,c,y,x_idx].item()} diff={diff[n,c,y,x_idx].item()}")
