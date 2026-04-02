#!/usr/bin/env python3
"""Benchmark vectorized vs scalar k3 conv+SiLU kernels across all three layers.

Compiles each kernel variant once, then runs N iterations to measure
steady-state per-invocation time on the NPU.

Usage:
    python3 peano_k3_pipelining_bug/benchmark.py
    python3 peano_k3_pipelining_bug/benchmark.py --iters 10
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
TIMEOUT = 90

LAYERS = [
    {"name": "L0",   "IC": 8,  "OC": 16, "H": 640, "W": 640, "stride": 2, "shift1": 10, "shift2": 128},
    {"name": "L1",   "IC": 16, "OC": 32, "H": 320, "W": 320, "stride": 2, "shift1": 10, "shift2": 128},
    {"name": "L2bn", "IC": 16, "OC": 16, "H": 160, "W": 160, "stride": 1, "shift1": 10, "shift2": 128},
]

KERNELS = {
    "vec":    "conv2dk3_i8_silu_scalar_workaround.cc",  # IC guard removed, vectorized
    "scalar": "conv2dk3_i8_silu_force_scalar.cc",       # always scalar
}


def golden_reference(x, w, bias, stride, shift1, shift2):
    acc = F.conv2d(x.int(), w.int(), stride=stride, padding=1)
    acc = acc + bias.view(1, -1, 1, 1).int()
    fval = acc.float() / float(1 << shift1)
    z = fval * 0.5
    z2 = z * z
    tanh_z = torch.where(z2 > 20.0, torch.sign(z),
                         z * (27.0 + z2) / (27.0 + 9.0 * z2))
    silu = fval * 0.5 * (1.0 + tanh_z)
    return torch.clamp(torch.round(silu * shift2 / 256.0), -128, 127).to(torch.int8)


def build_and_run(layer, kernel_tag, kernel_cc, n_iters):
    IC, OC = layer["IC"], layer["OC"]
    H, W, S = layer["H"], layer["W"], layer["stride"]
    shift1, shift2 = layer["shift1"], layer["shift2"]
    name = layer["name"]

    torch.manual_seed(42)
    x = torch.randint(-128, 128, (1, IC, H, W), dtype=torch.int8)
    wt = torch.randint(-128, 128, (OC, IC, 3, 3), dtype=torch.int8)
    bias = torch.randint(-5000, 5001, (OC,), dtype=torch.int32)
    ref = golden_reference(x, wt, bias, S, shift1, shift2)

    tag = f"{name}_{kernel_tag}"
    ctx = AIEContext()
    op = AIEConv2dInt8(
        in_channels=IC, out_channels=OC, kernel_size=3, stride=S,
        height=H, width=W, fused=True, shift1=shift1, shift2=shift2,
        silu_variant="split", context=ctx,
    )

    xclbin_art, insts_art = op.get_artifacts(prefix=f"{tag}_")
    extra_flags = ["-DINT8_ACT", "-ffunction-sections", "-fdata-sections"]
    mac_obj = KernelObjectArtifact.new(
        f"conv2dk3_i8_silu_{tag}_mac.o",
        depends=[SourceArtifact.new(BUG_DIR / kernel_cc)],
        extra_flags=extra_flags,
    )
    silu_obj = KernelObjectArtifact.new(
        f"silu_postproc_i8_{tag}.o",
        depends=[SourceArtifact.new(BUG_DIR / "silu_postproc_i8.cc")],
        extra_flags=extra_flags,
    )
    kernel_dep = LinkedKernelObjectArtifact.new(
        "conv2dk3_i8_silu.o", depends=[mac_obj, silu_obj],
    )
    mlir_dep = xclbin_art.depends[0]
    xclbin_art = XclbinArtifact.new(f"{tag}.xclbin", depends=[mlir_dep, kernel_dep])
    insts_art = InstsBinArtifact.new(f"{tag}.bin", depends=[mlir_dep])
    op.xclbin_artifact = xclbin_art
    op.insts_artifact = insts_art
    op.add_artifacts([xclbin_art, insts_art])

    ctx.compile_all()
    ctx.prepare_runtime()

    # Warmup
    op.forward(x, wt, bias)

    # Timed runs
    times = []
    for i in range(n_iters):
        old_handler = signal.signal(signal.SIGALRM,
                                     lambda s, f: (_ for _ in ()).throw(TimeoutError()))
        signal.alarm(TIMEOUT)
        try:
            t0 = time.perf_counter()
            npu = op.forward(x, wt, bias)
            elapsed = (time.perf_counter() - t0) * 1000
            signal.alarm(0)
            times.append(elapsed)
        except (TimeoutError, RuntimeError) as e:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)
            return None, None, str(e)
        finally:
            signal.signal(signal.SIGALRM, old_handler)

    # Correctness check on last run
    diff = np.abs(ref.numpy().reshape(-1).astype(np.int32) -
                  npu.numpy().reshape(-1).astype(np.int32))
    errors = int(np.sum(diff > 2))
    max_diff = int(np.max(diff))

    return times, (errors, max_diff, len(diff)), None


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--iters", type=int, default=5,
                        help="Number of timed iterations per config (default: 5)")
    parser.add_argument("--layer", type=str, default=None,
                        help="Run only this layer (L0, L1, L2bn)")
    args = parser.parse_args()

    layers = LAYERS
    if args.layer:
        layers = [l for l in LAYERS if l["name"] == args.layer]
        if not layers:
            print(f"Unknown layer: {args.layer}. Choose from: {[l['name'] for l in LAYERS]}")
            sys.exit(1)

    print(f"{'Layer':<6} {'IC':>3} {'OC':>3} {'Size':>10} {'Kernel':<8} "
          f"{'Min':>8} {'Avg':>8} {'Max':>8}  {'Errors':>8}  {'Status'}")
    print("-" * 85)

    results = {}
    for layer in layers:
        name = layer["name"]
        IC, OC, H, W, S = layer["IC"], layer["OC"], layer["H"], layer["W"], layer["stride"]
        oH, oW = H // S, W // S
        size_str = f"{H}x{W}"

        for ktag, kfile in KERNELS.items():
            label = f"{name}"
            sys.stdout.write(f"{label:<6} {IC:>3} {OC:>3} {size_str:>10} {ktag:<8} ")
            sys.stdout.flush()

            times, check, err = build_and_run(layer, ktag, kfile, args.iters)
            if err:
                print(f"{'HANG':>8} {'':>8} {'':>8}  {'':>8}  {err}")
                continue

            t_min = min(times)
            t_avg = sum(times) / len(times)
            t_max = max(times)
            errors, max_diff, total = check
            status = "PASS" if errors == 0 else f"FAIL (max_diff={max_diff})"
            errs_str = f"{errors}/{total}"

            print(f"{t_min:>7.0f}ms {t_avg:>7.0f}ms {t_max:>7.0f}ms  {errs_str:>8}  {status}")
            results[(name, ktag)] = t_avg

    # Summary
    print()
    print("Speedup (vec / scalar):")
    for layer in layers:
        name = layer["name"]
        vec = results.get((name, "vec"))
        scalar = results.get((name, "scalar"))
        if vec and scalar:
            speedup = scalar / vec
            print(f"  {name}: {speedup:.2f}x  (vec={vec:.0f}ms, scalar={scalar:.0f}ms)")


if __name__ == "__main__":
    main()
