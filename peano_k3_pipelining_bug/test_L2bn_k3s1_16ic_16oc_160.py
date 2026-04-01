#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""L2bn: YOLOv8n C2f bottleneck — k3 stride-1, IC=16 OC=16, 160x160.

EXPECTED: HANG (ERT_CMD_STATE_TIMEOUT) with vectorized split-SiLU kernel.

Same IC=16 / 2 ic_groups as L1, but stride-1 instead of stride-2.
Demonstrates the bug is not stride-specific.

Run:
    python3 peano_k3_pipelining_bug/test_L2bn_k3s1_16ic_16oc_160.py
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
IC, OC, H, W, STRIDE = 16, 16, 160, 160, 1
SHIFT1, SHIFT2 = 10, 7
TIMEOUT = 90


def golden_reference(x, w, bias):
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

    print(f"L2bn: k3s1 IC={IC} OC={OC} {H}x{W} -> {H}x{W}")
    print(f"  Reference output: {ref.shape}, range [{ref.min()}, {ref.max()}]")

    ctx = AIEContext()
    op = AIEConv2dInt8(
        in_channels=IC, out_channels=OC, kernel_size=3, stride=STRIDE,
        height=H, width=W, fused=True, shift1=SHIFT1, shift2=SHIFT2,
        silu_variant="split", context=ctx,
    )

    xclbin_art, insts_art = op.get_artifacts(prefix="L2bn_bug_")
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
        "conv2dk3_i8_silu_L2bn_bug.o", depends=[mac_obj, silu_obj],
    )
    mlir_dep = xclbin_art.depends[0]
    xclbin_art = XclbinArtifact.new("L2bn_bug.xclbin", depends=[mlir_dep, kernel_dep])
    insts_art = InstsBinArtifact.new("L2bn_bug.bin", depends=[mlir_dep])
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

    diff = np.abs(ref.numpy().reshape(-1).astype(np.int32) -
                  npu.numpy().reshape(-1).astype(np.int32))
    print(f"  PASS (unexpected!): exact={100*np.sum(diff==0)/len(diff):.1f}% "
          f"max_diff={np.max(diff)} time={elapsed:.0f}ms")


if __name__ == "__main__":
    main()
