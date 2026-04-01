#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""L0: YOLOv8n stem — k3 stride-2, IC=8 OC=16, 640x640 -> 320x320.

EXPECTED: HANG (ERT_CMD_STATE_TIMEOUT) with vectorized split-SiLU kernel.

This is the first layer of YOLOv8n. IC=8 means only 1 ic_group in the
MMUL inner loop, making the loop body trivially fast. Peano generates
broken pipelining code for this case when SiLU is split-compiled.

Run:
    python3 peano_k3_pipelining_bug/test_L0_k3s2_8ic_16oc_640.py
"""

import signal
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

from iron.common import (
    AIEContext, KernelObjectArtifact, LinkedKernelObjectArtifact,
    SourceArtifact, XclbinArtifact, InstsBinArtifact,
)
from iron.operators.conv2d_int8.op import AIEConv2dInt8

BUG_DIR = Path(__file__).parent

# --- Layer parameters ---
IC, OC, H, W, STRIDE = 8, 16, 640, 640, 2
SHIFT1, SHIFT2 = 10, 7
TIMEOUT = 90


def golden_reference(x, w, bias):
    """CPU golden: fused int8 k3 conv + bias + Pade SiLU."""
    acc = F.conv2d(x.int(), w.int(), stride=STRIDE, padding=1)
    acc = acc + bias.view(1, -1, 1, 1).int()
    fval = acc.float() / float(1 << SHIFT1)
    z = fval * 0.5
    z2 = z * z
    tanh_z = torch.where(z2 > 20.0, torch.sign(z),
                         z * (27.0 + z2) / (27.0 + 9.0 * z2))
    silu = fval * 0.5 * (1.0 + tanh_z)
    return torch.clamp(torch.round(silu * SHIFT2 / 256.0), -128, 127).to(torch.int8)


def main():
    torch.manual_seed(42)
    x = torch.randint(-20, 21, (1, IC, H, W), dtype=torch.int8)
    wt = torch.randint(-50, 51, (OC, IC, 3, 3), dtype=torch.int8)
    bias = torch.randint(-500, 501, (OC,), dtype=torch.int32)
    ref = golden_reference(x, wt, bias)

    print(f"L0: k3s2 IC={IC} OC={OC} {H}x{W} -> {H//2}x{W//2}")
    print(f"  Reference output: {ref.shape}, range [{ref.min()}, {ref.max()}]")

    # Build operator with split-compiled bug kernel (no IC guard)
    ctx = AIEContext()
    op = AIEConv2dInt8(
        in_channels=IC, out_channels=OC, kernel_size=3, stride=STRIDE,
        height=H, width=W, fused=True, shift1=SHIFT1, shift2=SHIFT2,
        silu_variant="split", context=ctx,
    )

    xclbin_art, insts_art = op.get_artifacts(prefix="L0_bug_")
    extra_flags = ["-DINT8_ACT", "-ffunction-sections", "-fdata-sections"]
    mac_obj = KernelObjectArtifact.new(
        "conv2dk3_i8_silu_bug.o",
        depends=[SourceArtifact.new(BUG_DIR / "conv2dk3_i8_silu_bug.cc")],
        extra_flags=extra_flags,
    )
    silu_obj = KernelObjectArtifact.new(
        "silu_postproc_i8_bug.o",
        depends=[SourceArtifact.new(BUG_DIR / "silu_postproc_i8.cc")],
        extra_flags=extra_flags,
    )
    kernel_dep = LinkedKernelObjectArtifact.new(
        "conv2dk3_i8_silu_L0_bug.o", depends=[mac_obj, silu_obj],
    )
    mlir_dep = xclbin_art.depends[0]
    xclbin_art = XclbinArtifact.new("L0_bug.xclbin", depends=[mlir_dep, kernel_dep])
    insts_art = InstsBinArtifact.new("L0_bug.bin", depends=[mlir_dep])
    op.xclbin_artifact = xclbin_art
    op.insts_artifact = insts_art
    op.add_artifacts([xclbin_art, insts_art])

    print("  Compiling (split SiLU, vectorized, no IC guard)...")
    ctx.compile_all()
    ctx.prepare_runtime()

    print(f"  Running on NPU (timeout={TIMEOUT}s)...")
    old = signal.signal(signal.SIGALRM, lambda s, f: (_ for _ in ()).throw(TimeoutError()))
    signal.alarm(TIMEOUT)
    try:
        t0 = time.perf_counter()
        npu = op.forward(x, wt, bias)
        elapsed = (time.perf_counter() - t0) * 1000
        signal.alarm(0)
    except (TimeoutError, RuntimeError) as e:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)
        print(f"\n  *** HANG: {e}")
        print(f"  This confirms the Peano pipelining bug at IC={IC}.")
        sys.exit(1)
    finally:
        signal.signal(signal.SIGALRM, old)

    # If we get here, it didn't hang (unexpected)
    diff = np.abs(ref.numpy().reshape(-1).astype(np.int32) -
                  npu.numpy().reshape(-1).astype(np.int32))
    print(f"  PASS (unexpected!): exact={100*np.sum(diff==0)/len(diff):.1f}% "
          f"max_diff={np.max(diff)} time={elapsed:.0f}ms")


if __name__ == "__main__":
    main()
