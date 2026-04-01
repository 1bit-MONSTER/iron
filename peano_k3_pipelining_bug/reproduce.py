#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reproducer for Peano pipelining bug in k3 fused SiLU at IC <= 16.

Demonstrates that split-compiled vectorized 3x3 conv + SiLU hangs on the
NPU when input channels (IC) is 8 or 16, but works correctly at IC >= 32.

Setup:
    source ironenv/bin/activate  # or your MLIR-AIE virtualenv
    source /path/to/mlir-aie/utils/env_setup.sh /path/to/mlir-aie /opt/xrt

Usage:
    python3 peano_k3_pipelining_bug/reproduce.py              # safe tests only
    python3 peano_k3_pipelining_bug/reproduce.py --list        # show test matrix
    python3 peano_k3_pipelining_bug/reproduce.py --all         # include hanging tests
    python3 peano_k3_pipelining_bug/reproduce.py --test ic8_vec_HANGS  # single test
"""

import argparse
import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

from iron.common import (
    AIEContext,
    KernelObjectArtifact,
    LinkedKernelObjectArtifact,
    SourceArtifact,
)
from iron.operators.conv2d_int8.op import AIEConv2dInt8


# ---------------------------------------------------------------------------
# CPU reference: Pade tanh SiLU (matches the AIE kernel exactly)
# ---------------------------------------------------------------------------

def _pade_tanh(z):
    z2 = z * z
    result = z * (27.0 + z2) / (27.0 + 9.0 * z2)
    return torch.where(z2 > 20.0, torch.sign(z), result)


def reference(x, w, bias, shift1, shift2, stride):
    """CPU golden reference for fused int8 k3 conv + bias + Pade SiLU."""
    acc = F.conv2d(x.int(), w.int(), stride=stride, padding=1)
    acc = acc + bias.view(1, -1, 1, 1).int()
    fval = acc.float() / float(1 << shift1)
    silu = fval * 0.5 * (1.0 + _pade_tanh(fval * 0.5))
    out = torch.clamp(torch.round(silu * float(shift2) / 256.0), -128, 127)
    return out.to(torch.int8)


# ---------------------------------------------------------------------------
# Test configurations
# ---------------------------------------------------------------------------

TESTS = [
    # (name,  IC, OC,   H,   W, stride, use_bug_kernel, will_hang)
    # --- Scalar baseline (always works) ---
    ("ic8_scalar_PASS",       8,  16, 640, 640, 2, False, False),
    ("ic16s2_scalar_PASS",   16,  32, 320, 320, 2, False, False),
    ("ic16s1_scalar_PASS",   16,  16, 160, 160, 1, False, False),
    # --- Vectorized, IC>16 (works) ---
    ("ic32_vec_PASS",        32,  64, 160, 160, 2, True,  False),
    ("ic64_vec_PASS",        64, 128,  80,  80, 2, True,  False),
    # --- Vectorized, IC<=16 (THE BUG — hangs) ---
    ("ic8_vec_HANGS",         8,  16, 640, 640, 2, True,  True),
    ("ic16s2_vec_HANGS",     16,  32, 320, 320, 2, True,  True),
    ("ic16s1_vec_HANGS",     16,  16, 160, 160, 1, True,  True),
]

BUG_DIR = Path(__file__).parent


def build_bug_kernel_artifact(ctx, extra_flags):
    """Build the kernel .o with IC guard removed (triggers the bug)."""
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
    return LinkedKernelObjectArtifact.new(
        "conv2dk3_i8_silu_linked_bug.o",
        depends=[mac_obj, silu_obj],
    )


def run_one(name, ic, oc, h, w, stride, use_bug_kernel, timeout_sec):
    """Run a single test. Returns (status, detail_string)."""
    torch.manual_seed(42)
    shift1, shift2 = 10, 7

    x = torch.randint(-20, 21, (1, ic, h, w), dtype=torch.int8)
    wt = torch.randint(-50, 51, (oc, ic, 3, 3), dtype=torch.int8)
    bias = torch.randint(-500, 501, (oc,), dtype=torch.int32)
    ref = reference(x, wt, bias, shift1, shift2, stride)

    ctx = AIEContext()
    op = AIEConv2dInt8(
        in_channels=ic, out_channels=oc, kernel_size=3, stride=stride,
        height=h, width=w, fused=True, shift1=shift1, shift2=shift2,
        context=ctx,
    )

    if use_bug_kernel:
        # Replace the kernel artifact with the bug version (no IC guard)
        xclbin_art, insts_art = op.get_artifacts(prefix="bug_repro_")
        # Swap kernel dep in xclbin to the bug version
        extra_flags = ["-DINT8_ACT", "-ffunction-sections", "-fdata-sections"]
        bug_kernel = build_bug_kernel_artifact(ctx, extra_flags)
        # Rebuild xclbin with bug kernel
        from iron.common import XclbinArtifact, InstsBinArtifact
        mlir_dep = xclbin_art.depends[0]  # MLIR artifact
        xclbin_art = XclbinArtifact.new(
            xclbin_art.path.name.replace("bug_repro_", "bugvec_"),
            depends=[mlir_dep, bug_kernel],
        )
        insts_art = InstsBinArtifact.new(
            insts_art.path.name.replace("bug_repro_", "bugvec_"),
            depends=[mlir_dep],
        )
        op.xclbin_artifact = xclbin_art
        op.insts_artifact = insts_art
        op.add_artifacts([xclbin_art, insts_art])

    # Compile
    ctx.compile_all()
    ctx.prepare_runtime()

    # Run with timeout
    def alarm_handler(signum, frame):
        raise TimeoutError()

    old = signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout_sec)
    try:
        t0 = time.perf_counter()
        npu = op.forward(x, wt, bias)
        elapsed = (time.perf_counter() - t0) * 1000
        signal.alarm(0)
    except (TimeoutError, RuntimeError) as e:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)
        return "HANG", str(e)
    finally:
        signal.signal(signal.SIGALRM, old)

    # Verify
    diff = np.abs(ref.numpy().reshape(-1).astype(np.int32) -
                  npu.numpy().reshape(-1).astype(np.int32))
    total = len(diff)
    exact = int(np.sum(diff == 0))
    max_diff = int(np.max(diff))
    errors = int(np.sum(diff > 2))

    if errors > 0:
        return "FAIL", (f"exact={100*exact/total:.1f}% max_diff={max_diff} "
                        f"errors={errors}/{total} time={elapsed:.0f}ms")
    return "PASS", (f"exact={100*exact/total:.1f}% max_diff={max_diff} "
                    f"time={elapsed:.0f}ms")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--test", help="Run single test by name")
    parser.add_argument("--all", action="store_true",
                        help="Include tests that will hang")
    parser.add_argument("--list", action="store_true",
                        help="Print test matrix and exit")
    parser.add_argument("--timeout", type=int, default=90,
                        help="Hang detection timeout in seconds (default: 90)")
    args = parser.parse_args()

    if args.list:
        fmt = "{:<25s} {:>3s} {:>3s} {:>9s} {:>2s} {:>10s} {:>8s}"
        print(fmt.format("Name", "IC", "OC", "HxW", "S", "Kernel", "Expect"))
        print("-" * 70)
        for name, ic, oc, h, w, s, bug, hang in TESTS:
            k = "BUG(vec)" if bug else "guarded"
            e = "HANG" if hang else "PASS"
            print(fmt.format(name, str(ic), str(oc),
                             f"{h}x{w}", str(s), k, e))
        return

    # Clean stale artifacts
    subprocess.run(["rm", "-rf"] +
                   [f for f in Path("build").glob("bug*")] +
                   [f for f in Path("build").glob("bugvec_*")],
                   check=False)

    tests = TESTS
    if args.test:
        tests = [t for t in TESTS if t[0] == args.test]
        if not tests:
            print(f"Unknown test: {args.test}")
            print("Available:", [t[0] for t in TESTS])
            sys.exit(1)

    print("=" * 70)
    print("Peano k3 Pipelining Bug Reproducer")
    print("=" * 70)
    print()
    print("Split-compiled vectorized k3 SiLU hangs at IC <= 16.")
    print("Same kernel works at IC >= 32. Scalar fallback works at all IC.")
    print()

    results = []
    for name, ic, oc, h, w, stride, use_bug, will_hang in tests:
        if will_hang and not args.all and not args.test:
            print(f"  [SKIP] {name:<30s} (will hang; use --all)")
            results.append((name, "SKIP"))
            continue

        tag = "BUG-VEC" if use_bug else "GUARDED"
        print(f"  [RUN]  {name:<30s} IC={ic:<3d} {h}x{w} s{stride} [{tag}]",
              end="", flush=True)

        status, detail = run_one(
            name, ic, oc, h, w, stride, use_bug, args.timeout)

        icon = {"PASS": "OK ", "FAIL": "ERR", "HANG": "BUG"}[status]
        print(f"  [{icon}] {detail}")
        results.append((name, status))

    print()
    print("=" * 70)
    hangs = sum(1 for _, s in results if s == "HANG")
    passes = sum(1 for _, s in results if s == "PASS")
    skips = sum(1 for _, s in results if s == "SKIP")
    print(f"Results: {passes} passed, {hangs} hangs (bug), {skips} skipped")
    if hangs:
        print("^^^ The HANG results are the Peano pipelining bug.")
    sys.exit(1 if hangs else 0)


if __name__ == "__main__":
    main()
