#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""L1: YOLOv8n first downsample — k3 stride-2, IC=16 OC=32, 320x320 -> 160x160.

Default (vectorized): HANGS — demonstrates the Peano pipelining bug.
With --scalar:         PASSES — scalar MAC workaround, correct but slow.

Run:
    python3 peano_k3_pipelining_bug/test_L1_k3s2_16ic_32oc_320.py            # HANGS
    python3 peano_k3_pipelining_bug/test_L1_k3s2_16ic_32oc_320.py --scalar   # PASSES
"""

import argparse
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
IC, OC, H, W, STRIDE = 16, 32, 320, 320, 2
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
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--scalar", action="store_true",
                        help="Use scalar MAC workaround (IC>16 guard)")
    args = parser.parse_args()

    kernel_cc = ("conv2dk3_i8_silu_scalar_workaround.cc" if args.scalar
                 else "conv2dk3_i8_silu_bug.cc")
    tag = "scalar" if args.scalar else "bug"
    mode = "SCALAR WORKAROUND" if args.scalar else "VECTORIZED (expect hang)"

    torch.manual_seed(42)
    x = torch.randint(-20, 21, (1, IC, H, W), dtype=torch.int8)
    wt = torch.randint(-50, 51, (OC, IC, 3, 3), dtype=torch.int8)
    bias = torch.randint(-500, 501, (OC,), dtype=torch.int32)
    ref = golden_reference(x, wt, bias)

    print(f"L1: k3s2 IC={IC} OC={OC} {H}x{W} -> {H//2}x{W//2}  [{mode}]")

    ctx = AIEContext()
    op = AIEConv2dInt8(
        in_channels=IC, out_channels=OC, kernel_size=3, stride=STRIDE,
        height=H, width=W, fused=True, shift1=SHIFT1, shift2=SHIFT2,
        silu_variant="split", context=ctx,
    )

    xclbin_art, insts_art = op.get_artifacts(prefix=f"L1_{tag}_")
    extra_flags = ["-DINT8_ACT", "-ffunction-sections", "-fdata-sections"]
    mac_obj = KernelObjectArtifact.new(
        f"conv2dk3_i8_silu_L1_{tag}.o",
        depends=[SourceArtifact.new(BUG_DIR / kernel_cc)],
        extra_flags=extra_flags,
    )
    silu_obj = KernelObjectArtifact.new(
        f"silu_postproc_i8_L1_{tag}.o",
        depends=[SourceArtifact.new(BUG_DIR / "silu_postproc_i8.cc")],
        extra_flags=extra_flags,
    )
    kernel_dep = LinkedKernelObjectArtifact.new(
        f"conv2dk3_i8_silu_L1_{tag}_linked.o", depends=[mac_obj, silu_obj],
    )
    mlir_dep = xclbin_art.depends[0]
    xclbin_art = XclbinArtifact.new(f"L1_{tag}.xclbin", depends=[mlir_dep, kernel_dep])
    insts_art = InstsBinArtifact.new(f"L1_{tag}.bin", depends=[mlir_dep])
    op.xclbin_artifact = xclbin_art
    op.insts_artifact = insts_art
    op.add_artifacts([xclbin_art, insts_art])

    print(f"  Compiling...")
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
        print(f"  Re-run with --scalar to verify the workaround passes.")
        sys.exit(1)
    finally:
        signal.signal(signal.SIGALRM, old)

    diff = np.abs(ref.numpy().reshape(-1).astype(np.int32) -
                  npu.numpy().reshape(-1).astype(np.int32))
    total = len(diff)
    exact_pct = 100 * np.sum(diff == 0) / total
    max_diff = int(np.max(diff))
    errors = int(np.sum(diff > 2))
    print(f"  exact={exact_pct:.1f}% max_diff={max_diff} errors={errors}/{total} "
          f"time={elapsed:.0f}ms")
    if errors > 0:
        print("  FAIL")
        sys.exit(1)
    print(f"  PASS")


if __name__ == "__main__":
    main()
