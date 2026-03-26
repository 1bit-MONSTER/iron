#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Run full YOLOv8n model end-to-end on NPU at 640x640.

Uses sequential AIEContexts with XRT cache cleanup between stages:
  - Context 1: Backbone L0-L9  (10 layers, ~30 operators)
  - Context 2: Neck L10-L21    (8 NPU layers + 4 host concats + 2 upsamples)
  - Context 3+: Detect head     (6 branches — TBD)
  - Post-processing             (DFL decode + NMS — TBD)

Each context is compiled, run, then cleaned up before the next to avoid
driver hw_context exhaustion.
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


def run_backbone(x):
    """Run backbone L0-L9 on NPU.

    Args:
        x: Input tensor [1, 8, 640, 640] in bfloat16 (3ch padded to 8ch).

    Returns:
        (p3, p4, p5) feature maps:
            p3: [1,  64, 80, 80]
            p4: [1, 128, 40, 40]
            p5: [1, 256, 20, 20]
    """
    print("=== Context 1: Backbone L0-L9 ===")
    t0 = time.time()

    ctx = AIEContext()

    l0 = CBS(8, 16, 3, 2, 640, 640, context=ctx)
    l1 = CBS(16, 32, 3, 2, 320, 320, context=ctx)
    l2 = C2f(32, 32, 1, 160, 160, context=ctx)
    l3 = CBS(32, 64, 3, 2, 160, 160, context=ctx)
    l4 = C2f(64, 64, 2, 80, 80, context=ctx)
    l5 = CBS(64, 128, 3, 2, 80, 80, context=ctx)
    l6 = C2f(128, 128, 2, 40, 40, context=ctx)
    l7 = CBS(128, 256, 3, 2, 40, 40, context=ctx)
    l8 = C2f(256, 256, 1, 20, 20, context=ctx)
    l9 = SPPF(256, 256, 20, 20, kernel_size=5, context=ctx)

    ctx.compile_all()

    # Load random weights (scaled small to keep outputs finite)
    l0.load_weights(
        torch.randn(16, 8, 3, 3, dtype=torch.bfloat16) * 0.01,
        torch.randn(16, dtype=torch.bfloat16) * 0.01,
    )
    l1.load_weights(
        torch.randn(32, 16, 3, 3, dtype=torch.bfloat16) * 0.01,
        torch.randn(32, dtype=torch.bfloat16) * 0.01,
    )

    c2 = 32 // 2
    l2.load_weights(
        torch.randn(2 * c2, 32, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(2 * c2, dtype=torch.bfloat16) * 0.01,
        [
            (
                torch.randn(c2, c2, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c2, dtype=torch.bfloat16) * 0.01,
                torch.randn(c2, c2, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c2, dtype=torch.bfloat16) * 0.01,
            )
            for _ in range(1)
        ],
        torch.randn(32, 3 * c2, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(32, dtype=torch.bfloat16) * 0.01,
    )

    l3.load_weights(
        torch.randn(64, 32, 3, 3, dtype=torch.bfloat16) * 0.01,
        torch.randn(64, dtype=torch.bfloat16) * 0.01,
    )

    c4 = 64 // 2
    l4.load_weights(
        torch.randn(2 * c4, 64, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(2 * c4, dtype=torch.bfloat16) * 0.01,
        [
            (
                torch.randn(c4, c4, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c4, dtype=torch.bfloat16) * 0.01,
                torch.randn(c4, c4, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c4, dtype=torch.bfloat16) * 0.01,
            )
            for _ in range(2)
        ],
        torch.randn(64, 4 * c4, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(64, dtype=torch.bfloat16) * 0.01,
    )

    l5.load_weights(
        torch.randn(128, 64, 3, 3, dtype=torch.bfloat16) * 0.01,
        torch.randn(128, dtype=torch.bfloat16) * 0.01,
    )

    c6 = 128 // 2
    l6.load_weights(
        torch.randn(2 * c6, 128, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(2 * c6, dtype=torch.bfloat16) * 0.01,
        [
            (
                torch.randn(c6, c6, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c6, dtype=torch.bfloat16) * 0.01,
                torch.randn(c6, c6, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c6, dtype=torch.bfloat16) * 0.01,
            )
            for _ in range(2)
        ],
        torch.randn(128, 4 * c6, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(128, dtype=torch.bfloat16) * 0.01,
    )

    l7.load_weights(
        torch.randn(256, 128, 3, 3, dtype=torch.bfloat16) * 0.01,
        torch.randn(256, dtype=torch.bfloat16) * 0.01,
    )

    c8 = 256 // 2
    l8.load_weights(
        torch.randn(2 * c8, 256, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(2 * c8, dtype=torch.bfloat16) * 0.01,
        [
            (
                torch.randn(c8, c8, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c8, dtype=torch.bfloat16) * 0.01,
                torch.randn(c8, c8, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c8, dtype=torch.bfloat16) * 0.01,
            )
            for _ in range(1)
        ],
        torch.randn(256, 3 * c8, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(256, dtype=torch.bfloat16) * 0.01,
    )

    c9_ = 256 // 2
    l9.load_weights(
        torch.randn(c9_, 256, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(c9_, dtype=torch.bfloat16) * 0.01,
        torch.randn(256, c9_ * 4, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(256, dtype=torch.bfloat16) * 0.01,
    )

    ctx.prepare_runtime()
    compile_t = time.time() - t0
    print(f"Backbone compiled + prepared in {compile_t:.1f}s")

    # Forward pass
    print("\nRunning backbone L0-L9...")
    t0_fwd = time.time()

    x = l0.forward(x)
    print(f"  L0:  {x.shape}")
    x = l1.forward(x)
    print(f"  L1:  {x.shape}")
    x = l2.forward(x)
    print(f"  L2:  {x.shape}")
    x = l3.forward(x)
    print(f"  L3:  {x.shape}")
    p3 = l4.forward(x)
    print(f"  L4:  {p3.shape}  [P3]")
    x = l5.forward(p3)
    print(f"  L5:  {x.shape}")
    p4 = l6.forward(x)
    print(f"  L6:  {p4.shape}  [P4]")
    x = l7.forward(p4)
    print(f"  L7:  {x.shape}")
    x = l8.forward(x)
    print(f"  L8:  {x.shape}")
    p5 = l9.forward(x)
    print(f"  L9:  {p5.shape}  [P5]")

    fwd_t = time.time() - t0_fwd
    print(f"Backbone forward: {fwd_t:.3f}s")

    # Verify
    assert p3.shape == (1, 64, 80, 80), f"P3 shape mismatch: {p3.shape}"
    assert p4.shape == (1, 128, 40, 40), f"P4 shape mismatch: {p4.shape}"
    assert p5.shape == (1, 256, 20, 20), f"P5 shape mismatch: {p5.shape}"
    assert torch.isfinite(p3).all(), "P3 has non-finite values"
    assert torch.isfinite(p4).all(), "P4 has non-finite values"
    assert torch.isfinite(p5).all(), "P5 has non-finite values"
    print("Backbone PASS")

    # Cleanup
    del l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, ctx
    cleanup_xrt()

    return p3, p4, p5, compile_t, fwd_t


def run_neck(p3, p4, p5):
    """Run neck L10-L21 on NPU.

    Args:
        p3: [1,  64, 80, 80] from backbone.
        p4: [1, 128, 40, 40] from backbone.
        p5: [1, 256, 20, 20] from backbone.

    Returns:
        (det_p3, det_p4, det_p5) detection feature maps:
            det_p3: [1,  64, 80, 80]
            det_p4: [1, 128, 40, 40]
            det_p5: [1, 256, 20, 20]
    """
    print("\n=== Context 2: Neck L10-L21 ===")
    t0 = time.time()

    ctx = AIEContext()

    up1 = AIEUpsample(256, 20, 20, scale_factor=2, context=ctx)
    l12 = C2f(384, 128, 1, 40, 40, shortcut=False, context=ctx)
    up2 = AIEUpsample(128, 40, 40, scale_factor=2, context=ctx)
    l15 = C2f(192, 64, 1, 80, 80, shortcut=False, context=ctx)
    l16 = CBS(64, 64, 3, 2, 80, 80, context=ctx)
    l18 = C2f(192, 128, 1, 40, 40, shortcut=False, context=ctx)
    l19 = CBS(128, 128, 3, 2, 40, 40, context=ctx)
    l21 = C2f(384, 256, 1, 20, 20, shortcut=False, context=ctx)

    ctx.compile_all()

    # Load weights
    c12 = 128 // 2
    l12.load_weights(
        torch.randn(2 * c12, 384, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(2 * c12, dtype=torch.bfloat16) * 0.01,
        [
            (
                torch.randn(c12, c12, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c12, dtype=torch.bfloat16) * 0.01,
                torch.randn(c12, c12, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c12, dtype=torch.bfloat16) * 0.01,
            )
            for _ in range(1)
        ],
        torch.randn(128, 3 * c12, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(128, dtype=torch.bfloat16) * 0.01,
    )

    c15 = 64 // 2
    l15.load_weights(
        torch.randn(2 * c15, 192, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(2 * c15, dtype=torch.bfloat16) * 0.01,
        [
            (
                torch.randn(c15, c15, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c15, dtype=torch.bfloat16) * 0.01,
                torch.randn(c15, c15, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c15, dtype=torch.bfloat16) * 0.01,
            )
            for _ in range(1)
        ],
        torch.randn(64, 3 * c15, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(64, dtype=torch.bfloat16) * 0.01,
    )

    l16.load_weights(
        torch.randn(64, 64, 3, 3, dtype=torch.bfloat16) * 0.01,
        torch.randn(64, dtype=torch.bfloat16) * 0.01,
    )

    c18 = 128 // 2
    l18.load_weights(
        torch.randn(2 * c18, 192, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(2 * c18, dtype=torch.bfloat16) * 0.01,
        [
            (
                torch.randn(c18, c18, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c18, dtype=torch.bfloat16) * 0.01,
                torch.randn(c18, c18, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c18, dtype=torch.bfloat16) * 0.01,
            )
            for _ in range(1)
        ],
        torch.randn(128, 3 * c18, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(128, dtype=torch.bfloat16) * 0.01,
    )

    l19.load_weights(
        torch.randn(128, 128, 3, 3, dtype=torch.bfloat16) * 0.01,
        torch.randn(128, dtype=torch.bfloat16) * 0.01,
    )

    c21 = 256 // 2
    l21.load_weights(
        torch.randn(2 * c21, 384, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(2 * c21, dtype=torch.bfloat16) * 0.01,
        [
            (
                torch.randn(c21, c21, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c21, dtype=torch.bfloat16) * 0.01,
                torch.randn(c21, c21, 3, 3, dtype=torch.bfloat16) * 0.01,
                torch.randn(c21, dtype=torch.bfloat16) * 0.01,
            )
            for _ in range(1)
        ],
        torch.randn(256, 3 * c21, 1, 1, dtype=torch.bfloat16) * 0.01,
        torch.randn(256, dtype=torch.bfloat16) * 0.01,
    )

    ctx.prepare_runtime()
    compile_t = time.time() - t0
    print(f"Neck compiled + prepared in {compile_t:.1f}s")

    # Forward pass
    print("\nRunning neck L10-L21...")
    t0_fwd = time.time()

    # FPN up-path
    x = up1.forward(p5)
    print(f"  L10: {x.shape}  (upsample)")
    x = torch.cat([x, p4], dim=1)
    print(f"  L11: {x.shape}  (concat)")
    l12_out = l12.forward(x)
    print(f"  L12: {l12_out.shape}")
    x = up2.forward(l12_out)
    print(f"  L13: {x.shape}  (upsample)")
    x = torch.cat([x, p3], dim=1)
    print(f"  L14: {x.shape}  (concat)")
    det_p3 = l15.forward(x)
    print(f"  L15: {det_p3.shape}  [det_p3]")

    # PAN down-path
    x = l16.forward(det_p3)
    print(f"  L16: {x.shape}")
    x = torch.cat([x, l12_out], dim=1)
    print(f"  L17: {x.shape}  (concat)")
    det_p4 = l18.forward(x)
    print(f"  L18: {det_p4.shape}  [det_p4]")
    x = l19.forward(det_p4)
    print(f"  L19: {x.shape}")
    x = torch.cat([x, p5], dim=1)
    print(f"  L20: {x.shape}  (concat)")
    det_p5 = l21.forward(x)
    print(f"  L21: {det_p5.shape}  [det_p5]")

    fwd_t = time.time() - t0_fwd
    print(f"Neck forward: {fwd_t:.3f}s")

    # Verify
    assert det_p3.shape == (1, 64, 80, 80), f"det_p3 shape mismatch: {det_p3.shape}"
    assert det_p4.shape == (1, 128, 40, 40), f"det_p4 shape mismatch: {det_p4.shape}"
    assert det_p5.shape == (1, 256, 20, 20), f"det_p5 shape mismatch: {det_p5.shape}"
    assert torch.isfinite(det_p3).all(), "det_p3 has non-finite values"
    assert torch.isfinite(det_p4).all(), "det_p4 has non-finite values"
    assert torch.isfinite(det_p5).all(), "det_p5 has non-finite values"
    print("Neck PASS")

    # Cleanup
    del up1, l12, up2, l15, l16, l18, l19, l21, ctx
    cleanup_xrt()

    return det_p3, det_p4, det_p5, compile_t, fwd_t


# ── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("YOLOv8n Full Model — NPU End-to-End")
    print("=" * 60)

    total_t0 = time.time()

    # Prepare input: 3ch RGB padded to 8ch
    x_input = F.pad(
        torch.randn(1, 3, 640, 640, dtype=torch.bfloat16),
        (0, 0, 0, 0, 0, 5),
    )
    print(f"Input: {x_input.shape} (3ch padded to 8ch)\n")

    # Stage 1: Backbone
    p3, p4, p5, bb_compile, bb_fwd = run_backbone(x_input)

    # Stage 2: Neck
    det_p3, det_p4, det_p5, neck_compile, neck_fwd = run_neck(p3, p4, p5)

    # TODO: Stage 3 — Detect head (6 branches)
    # TODO: Stage 4 — Post-processing (DFL decode + NMS)

    # Summary
    total_t = time.time() - total_t0
    total_compile = bb_compile + neck_compile
    total_fwd = bb_fwd + neck_fwd

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Compile time: {total_compile:.1f}s  (backbone {bb_compile:.1f}s + neck {neck_compile:.1f}s)")
    print(f"Forward time: {total_fwd:.3f}s  (backbone {bb_fwd:.3f}s + neck {neck_fwd:.3f}s)")
    print(f"Total wall time: {total_t:.1f}s")
    print()
    for name, t in [("det_p3", det_p3), ("det_p4", det_p4), ("det_p5", det_p5)]:
        print(f"  {name}: {t.shape}  finite={torch.isfinite(t).all()}")
    print()
    print("BACKBONE + NECK (L0-L21) ALL PASS ON NPU")
