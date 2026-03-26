# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from iron.common import AIEContext
from iron.operators.conv2d_int8.op import AIEConv2dInt8
from iron.operators.conv2d_int8.reference import conv2d_int8_reference

torch.manual_seed(42)

ic, oc, h, w = 32, 32, 1, 160  # Just 1 row to isolate
scale = 10

print(f"Config: {ic}->{oc} k1 {h}x{w}, scale={scale}")

ctx = AIEContext()
op = AIEConv2dInt8(ic, oc, 1, 1, h, w, scale=scale, context=ctx)
ctx.compile_all()
ctx.prepare_runtime()

# Use same value range as original benchmark
x = torch.randint(-20, 20, (1, ic, h, w), dtype=torch.int8)
wt = torch.randint(-50, 50, (oc, ic, 1, 1), dtype=torch.int8)

npu_out = op.forward(x, wt)
ref_out = conv2d_int8_reference(x, wt, scale=scale)

diff = (npu_out.float() - ref_out.float()).abs()
print(f"Max diff: {diff.max().item()}")
print(f"Mean diff: {diff.mean().item():.3f}")
print(f"Num mismatches (>1): {(diff > 1).sum().item()} / {diff.numel()}")

# Show per-OC-group max errors
for oc_g in range(oc // 8):
    sl = npu_out[0, oc_g*8:(oc_g+1)*8, :, :]
    sl_ref = ref_out[0, oc_g*8:(oc_g+1)*8, :, :]
    d = (sl.float() - sl_ref.float()).abs()
    print(f"  OC group {oc_g}: max_diff={d.max().item():.1f}")

# Show first few large mismatches
if diff.max().item() > 1:
    indices = torch.where(diff > 10)
    print(f"\nMismatches > 10:")
    for i in range(min(20, len(indices[0]))):
        n, c, y, x_idx = [idx[i].item() for idx in indices]
        print(f"  [{n},{c},{y},{x_idx}] npu={npu_out[n,c,y,x_idx].item()} ref={ref_out[n,c,y,x_idx].item()}")
