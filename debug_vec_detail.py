# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Detailed element-level debug of vectorized conv2dk1_i8."""

import torch
import numpy as np
from iron.common import AIEContext
from iron.operators.conv2d_int8.op import AIEConv2dInt8, nchw_to_tiled_int8, tiled_to_nchw_int8, weights_to_tiled_int8

torch.manual_seed(0)

# Minimal config: 8 IC, 8 OC, 1 row, 32 width
ic, oc, h, w = 16, 8, 1, 32
scale = 10

print(f"Config: {ic}->{oc} k1 {h}x{w}, scale={scale}")

ctx = AIEContext()
op = AIEConv2dInt8(ic, oc, 1, 1, h, w, scale=scale, context=ctx)
ctx.compile_all()
ctx.prepare_runtime()

# Use identity-like inputs for easy manual verification
x = torch.zeros((1, ic, h, w), dtype=torch.int8)
wt = torch.zeros((oc, ic, 1, 1), dtype=torch.int8)

# Set x[0, 0, 0, 0] = 1, all weights for oc=0 channel ic=0 = 1
# Expected output: oc=0, pos 0 should be 1 >> 10 = 0
# Actually let's use larger values so we can see the shift result
x[0, 0, 0, :] = 100  # Channel 0, all spatial positions = 100
wt[0, 0, 0, 0] = 10   # Weight oc=0, ic=0 = 10
# Expected: output[0,0,0,:] = (100 * 10 + round) >> 10 = (1000+512)>>10 = 1

npu_out = op.forward(x, wt)
print(f"Test 1 - single channel, single weight:")
print(f"  Expected: all spatial positions of oc=0 should be ~1")
print(f"  NPU output oc=0: {npu_out[0, 0, 0, :].tolist()}")
print(f"  NPU output oc=1: {npu_out[0, 1, 0, :].tolist()}")

# Test 2: Multiple IC accumulation
x2 = torch.zeros((1, ic, h, w), dtype=torch.int8)
wt2 = torch.zeros((oc, ic, 1, 1), dtype=torch.int8)
for i in range(ic):
    x2[0, i, 0, :] = 10
    wt2[0, i, 0, 0] = 10
# Expected: output[0,0,0,:] = (IC * 10 * 10 + round) >> 10 = (16*100+512)>>10 = (2112)>>10 = 2

npu_out2 = op.forward(x2, wt2)
print(f"\nTest 2 - all IC channels contribute:")
print(f"  Expected: all spatial positions of oc=0 should be ~{(ic * 100 + 512) >> 10}")
print(f"  NPU output oc=0: {npu_out2[0, 0, 0, :].tolist()}")

# Test 3: Random data, compare tiled representations
x3 = torch.randint(-20, 20, (1, ic, h, w), dtype=torch.int8)
wt3 = torch.randint(-50, 50, (oc, ic, 1, 1), dtype=torch.int8)
npu_out3 = op.forward(x3, wt3)

# Manual reference in tiled layout
in_tiled = nchw_to_tiled_int8(x3)   # [H, IC/8, W, 8]
wt_tiled = weights_to_tiled_int8(wt3)  # [OC/8, IC/8, 8(ic), 8(oc)]

# Compute reference in tiled format
out_ref = np.zeros(oc * w, dtype=np.int32)
for oc_g in range(oc // 8):
    for x_pos in range(w):
        for oc8 in range(8):
            acc = 0
            for ic_g in range(ic // 8):
                for ic8 in range(8):
                    in_val = in_tiled[ic_g * w * 8 + x_pos * 8 + ic8]
                    wt_val = wt_tiled[oc_g * (ic // 8) * 64 + ic_g * 64 + ic8 * 8 + oc8]
                    acc += int(in_val) * int(wt_val)
            srs = (acc + (1 << (scale - 1))) >> scale
            srs = max(-128, min(127, srs))
            out_ref[oc_g * w * 8 + x_pos * 8 + oc8] = srs

# Convert NPU output to tiled
npu_tiled = nchw_to_tiled_int8(npu_out3)

diff = np.abs(out_ref.astype(np.int16) - npu_tiled.astype(np.int16))
print(f"\nTest 3 - Random data, tiled-domain comparison:")
print(f"  Max diff: {diff.max()}")
print(f"  Mismatches > 1: {(diff > 1).sum()} / {len(diff)}")
if diff.max() > 1:
    bad = np.where(diff > 1)[0][:20]
    for b in bad:
        oc_g = b // (w * 8)
        rem = b % (w * 8)
        x_pos = rem // 8
        oc8 = rem % 8
        print(f"    tiled[{b}] (oc_g={oc_g}, w={x_pos}, oc8={oc8}): npu={npu_tiled[b]} ref={out_ref[b]}")
