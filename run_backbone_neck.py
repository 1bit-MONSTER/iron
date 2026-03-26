#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Run full YOLOv8n backbone + neck (L0-L21) end-to-end on NPU at 640x640.

Uses 2 AIEContexts:
  - Context 1: Backbone L0-L9 (30 operators, ~20 unique xclbins)
  - Context 2: Neck L10-L21 (20 operators + 4 host concats)

Each context's operators share hw_context deduplication via the HostRuntime
cache, keeping total unique hw_contexts manageable.
"""

import torch
import torch.nn.functional as F
import time
import gc
from iron.common import AIEContext
from iron.applications.yolov8n.blocks import CBS, C2f, SPPF
from iron.operators.upsample.op import AIEUpsample
from aie.utils import DefaultNPURuntime

torch.manual_seed(42)


def cleanup_xrt():
    """Release all XRT hw_contexts to avoid driver exhaustion."""
    DefaultNPURuntime._context_cache.clear()
    DefaultNPURuntime._insts_cache.clear()
    gc.collect()


# ── Context 1: Backbone L0-L9 ──────────────────────────────────────────────
print("=== Context 1: Backbone L0-L9 ===")
t0_compile = time.time()

ctx1 = AIEContext()

l0 = CBS(8, 16, 3, 2, 640, 640, context=ctx1)
l1 = CBS(16, 32, 3, 2, 320, 320, context=ctx1)
l2 = C2f(32, 32, 1, 160, 160, context=ctx1)
l3 = CBS(32, 64, 3, 2, 160, 160, context=ctx1)
l4 = C2f(64, 64, 2, 80, 80, context=ctx1)
l5 = CBS(64, 128, 3, 2, 80, 80, context=ctx1)
l6 = C2f(128, 128, 2, 40, 40, context=ctx1)
l7 = CBS(128, 256, 3, 2, 40, 40, context=ctx1)
l8 = C2f(256, 256, 1, 20, 20, context=ctx1)
l9 = SPPF(256, 256, 20, 20, kernel_size=5, context=ctx1)

ctx1.compile_all()

# Load weights
l0.load_weights(torch.randn(16, 8, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(16, dtype=torch.bfloat16) * 0.01)
l1.load_weights(torch.randn(32, 16, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(32, dtype=torch.bfloat16) * 0.01)

c2 = 32 // 2
l2.load_weights(
    torch.randn(2 * c2, 32, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(2 * c2, dtype=torch.bfloat16) * 0.01,
    [(torch.randn(c2, c2, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c2, dtype=torch.bfloat16) * 0.01,
      torch.randn(c2, c2, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c2, dtype=torch.bfloat16) * 0.01) for _ in range(1)],
    torch.randn(32, 3 * c2, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(32, dtype=torch.bfloat16) * 0.01)

l3.load_weights(torch.randn(64, 32, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(64, dtype=torch.bfloat16) * 0.01)

c4 = 64 // 2
l4.load_weights(
    torch.randn(2 * c4, 64, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(2 * c4, dtype=torch.bfloat16) * 0.01,
    [(torch.randn(c4, c4, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c4, dtype=torch.bfloat16) * 0.01,
      torch.randn(c4, c4, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c4, dtype=torch.bfloat16) * 0.01) for _ in range(2)],
    torch.randn(64, 4 * c4, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(64, dtype=torch.bfloat16) * 0.01)

l5.load_weights(torch.randn(128, 64, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(128, dtype=torch.bfloat16) * 0.01)

c6 = 128 // 2
l6.load_weights(
    torch.randn(2 * c6, 128, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(2 * c6, dtype=torch.bfloat16) * 0.01,
    [(torch.randn(c6, c6, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c6, dtype=torch.bfloat16) * 0.01,
      torch.randn(c6, c6, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c6, dtype=torch.bfloat16) * 0.01) for _ in range(2)],
    torch.randn(128, 4 * c6, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(128, dtype=torch.bfloat16) * 0.01)

l7.load_weights(torch.randn(256, 128, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(256, dtype=torch.bfloat16) * 0.01)

c8 = 256 // 2
l8.load_weights(
    torch.randn(2 * c8, 256, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(2 * c8, dtype=torch.bfloat16) * 0.01,
    [(torch.randn(c8, c8, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c8, dtype=torch.bfloat16) * 0.01,
      torch.randn(c8, c8, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c8, dtype=torch.bfloat16) * 0.01) for _ in range(1)],
    torch.randn(256, 3 * c8, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(256, dtype=torch.bfloat16) * 0.01)

c9_ = 256 // 2
l9.load_weights(
    torch.randn(c9_, 256, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(c9_, dtype=torch.bfloat16) * 0.01,
    torch.randn(256, c9_ * 4, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(256, dtype=torch.bfloat16) * 0.01)

ctx1.prepare_runtime()
compile_time_1 = time.time() - t0_compile
print(f"Context 1 compiled + prepared in {compile_time_1:.1f}s")

# Forward pass backbone
print("\nRunning backbone L0-L9...")
t0_fwd = time.time()

x = F.pad(torch.randn(1, 3, 640, 640, dtype=torch.bfloat16), (0, 0, 0, 0, 0, 5))
x = l0.forward(x);  print(f"L0:  {x.shape}")
x = l1.forward(x);  print(f"L1:  {x.shape}")
x = l2.forward(x);  print(f"L2:  {x.shape}")
x = l3.forward(x);  print(f"L3:  {x.shape}")
p3 = l4.forward(x); print(f"L4:  {p3.shape}  [P3]")
x = l5.forward(p3); print(f"L5:  {x.shape}")
p4 = l6.forward(x); print(f"L6:  {p4.shape}  [P4]")
x = l7.forward(p4); print(f"L7:  {x.shape}")
x = l8.forward(x);  print(f"L8:  {x.shape}")
p5 = l9.forward(x); print(f"L9:  {p5.shape}  [P5]")

fwd_time_1 = time.time() - t0_fwd
print(f"Backbone forward: {fwd_time_1:.3f}s")

# Clean up Context 1 before Context 2
del l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, ctx1
cleanup_xrt()

# ── Context 2: Neck L10-L21 ────────────────────────────────────────────────
print("\n=== Context 2: Neck L10-L21 ===")
t0_compile = time.time()

ctx2 = AIEContext()

up1 = AIEUpsample(256, 20, 20, scale_factor=2, context=ctx2)
l12 = C2f(384, 128, 1, 40, 40, shortcut=False, context=ctx2)
up2 = AIEUpsample(128, 40, 40, scale_factor=2, context=ctx2)
l15 = C2f(192, 64, 1, 80, 80, shortcut=False, context=ctx2)
l16 = CBS(64, 64, 3, 2, 80, 80, context=ctx2)
l18 = C2f(192, 128, 1, 40, 40, shortcut=False, context=ctx2)
l19 = CBS(128, 128, 3, 2, 40, 40, context=ctx2)
l21 = C2f(384, 256, 1, 20, 20, shortcut=False, context=ctx2)

ctx2.compile_all()

# Load weights
c12 = 128 // 2
l12.load_weights(
    torch.randn(2 * c12, 384, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(2 * c12, dtype=torch.bfloat16) * 0.01,
    [(torch.randn(c12, c12, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c12, dtype=torch.bfloat16) * 0.01,
      torch.randn(c12, c12, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c12, dtype=torch.bfloat16) * 0.01) for _ in range(1)],
    torch.randn(128, 3 * c12, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(128, dtype=torch.bfloat16) * 0.01)

c15 = 64 // 2
l15.load_weights(
    torch.randn(2 * c15, 192, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(2 * c15, dtype=torch.bfloat16) * 0.01,
    [(torch.randn(c15, c15, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c15, dtype=torch.bfloat16) * 0.01,
      torch.randn(c15, c15, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c15, dtype=torch.bfloat16) * 0.01) for _ in range(1)],
    torch.randn(64, 3 * c15, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(64, dtype=torch.bfloat16) * 0.01)

l16.load_weights(torch.randn(64, 64, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(64, dtype=torch.bfloat16) * 0.01)

c18 = 128 // 2
l18.load_weights(
    torch.randn(2 * c18, 192, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(2 * c18, dtype=torch.bfloat16) * 0.01,
    [(torch.randn(c18, c18, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c18, dtype=torch.bfloat16) * 0.01,
      torch.randn(c18, c18, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c18, dtype=torch.bfloat16) * 0.01) for _ in range(1)],
    torch.randn(128, 3 * c18, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(128, dtype=torch.bfloat16) * 0.01)

l19.load_weights(torch.randn(128, 128, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(128, dtype=torch.bfloat16) * 0.01)

c21 = 256 // 2
l21.load_weights(
    torch.randn(2 * c21, 384, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(2 * c21, dtype=torch.bfloat16) * 0.01,
    [(torch.randn(c21, c21, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c21, dtype=torch.bfloat16) * 0.01,
      torch.randn(c21, c21, 3, 3, dtype=torch.bfloat16) * 0.01, torch.randn(c21, dtype=torch.bfloat16) * 0.01) for _ in range(1)],
    torch.randn(256, 3 * c21, 1, 1, dtype=torch.bfloat16) * 0.01, torch.randn(256, dtype=torch.bfloat16) * 0.01)

ctx2.prepare_runtime()
compile_time_2 = time.time() - t0_compile
print(f"Context 2 compiled + prepared in {compile_time_2:.1f}s")

# Forward pass neck
print("\nRunning neck L10-L21...")
t0_fwd = time.time()

# FPN up-path
x = up1.forward(p5);           print(f"L10: {x.shape}")
x = torch.cat([x, p4], dim=1); print(f"L11: {x.shape} (concat)")
l12_out = l12.forward(x);      print(f"L12: {l12_out.shape}")
x = up2.forward(l12_out);      print(f"L13: {x.shape}")
x = torch.cat([x, p3], dim=1); print(f"L14: {x.shape} (concat)")
det_p3 = l15.forward(x);       print(f"L15: {det_p3.shape}  [det_p3]")

# PAN down-path
x = l16.forward(det_p3);            print(f"L16: {x.shape}")
x = torch.cat([x, l12_out], dim=1); print(f"L17: {x.shape} (concat)")
det_p4 = l18.forward(x);            print(f"L18: {det_p4.shape}  [det_p4]")
x = l19.forward(det_p4);            print(f"L19: {x.shape}")
x = torch.cat([x, p5], dim=1);      print(f"L20: {x.shape} (concat)")
det_p5 = l21.forward(x);            print(f"L21: {det_p5.shape}  [det_p5]")

fwd_time_2 = time.time() - t0_fwd
print(f"Neck forward: {fwd_time_2:.3f}s")

# Verify
print(f"\n=== Results ===")
print(f"Compile time: {compile_time_1 + compile_time_2:.1f}s total ({compile_time_1:.1f}s backbone + {compile_time_2:.1f}s neck)")
print(f"Forward time: {fwd_time_1 + fwd_time_2:.3f}s total ({fwd_time_1:.3f}s backbone + {fwd_time_2:.3f}s neck)")
print()
for name, t in [("det_p3", det_p3), ("det_p4", det_p4), ("det_p5", det_p5)]:
    print(f"{name}: {t.shape} finite={torch.isfinite(t).all()}")

assert det_p3.shape == (1, 64, 80, 80)
assert det_p4.shape == (1, 128, 40, 40)
assert det_p5.shape == (1, 256, 20, 20)
assert torch.isfinite(det_p3).all()
assert torch.isfinite(det_p4).all()
assert torch.isfinite(det_p5).all()

print("\nBACKBONE + NECK L0-L21 ALL PASS ON NPU")
