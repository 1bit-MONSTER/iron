#!/usr/bin/env python3
"""Instrument the forward() call for L2bn to find where time is spent.

Breaks down the forward() call into individual sub-steps and times each one
using time.perf_counter(). This helps identify whether the bottleneck is in
data conversion, buffer writes, NPU execution, or buffer reads.

Usage:
    source /scratch/jmelber/mlir-aie/ironenv/bin/activate
    source /scratch/jmelber/mlir-aie/utils/env_setup.sh /scratch/jmelber/mlir-aie /opt/xrt
    PYTHONPATH="/scratch/jmelber/bug/IRON:$PYTHONPATH" python3 peano_k3_pipelining_bug/instrument_forward.py
"""

import sys
import time
from pathlib import Path

import numpy as np
import torch

from iron.common import (
    AIEContext,
    KernelObjectArtifact,
    LinkedKernelObjectArtifact,
    SourceArtifact,
    XclbinArtifact,
    InstsBinArtifact,
)
from iron.operators.conv2d_int8.op import (
    AIEConv2dInt8,
    nchw_to_tiled_int8,
    tiled_to_nchw_int8,
    weights_to_tiled_int8_k3,
    _compute_k3_fused_streaming,
)

BUG_DIR = Path(__file__).parent

# L2bn layer parameters
IC = 16
OC = 16
H = 160
W = 160
STRIDE = 1
SHIFT1 = 10
SHIFT2 = 128
N_ITERS = 5


def build_op():
    """Build and compile the L2bn operator, return (op, x, wt, bias)."""
    torch.manual_seed(42)
    x = torch.randint(-128, 128, (1, IC, H, W), dtype=torch.int8)
    wt = torch.randint(-128, 128, (OC, IC, 3, 3), dtype=torch.int8)
    bias = torch.randint(-5000, 5001, (OC,), dtype=torch.int32)

    ctx = AIEContext()
    op = AIEConv2dInt8(
        in_channels=IC,
        out_channels=OC,
        kernel_size=3,
        stride=STRIDE,
        height=H,
        width=W,
        fused=True,
        shift1=SHIFT1,
        shift2=SHIFT2,
        silu_variant="split",
        context=ctx,
    )

    # Use the default kernel (not the benchmark's custom kernel overrides)
    xclbin_art, insts_art = op.get_artifacts(prefix="L2bn_instrument_")
    extra_flags = ["-DINT8_ACT", "-ffunction-sections", "-fdata-sections"]
    mac_obj = KernelObjectArtifact.new(
        "conv2dk3_i8_silu_L2bn_inst_mac.o",
        depends=[SourceArtifact.new(BUG_DIR / "conv2dk3_i8_silu_scalar_workaround.cc")],
        extra_flags=extra_flags,
    )
    silu_obj = KernelObjectArtifact.new(
        "silu_postproc_i8_L2bn_inst.o",
        depends=[SourceArtifact.new(BUG_DIR / "silu_postproc_i8.cc")],
        extra_flags=extra_flags,
    )
    kernel_dep = LinkedKernelObjectArtifact.new(
        "conv2dk3_i8_silu.o",
        depends=[mac_obj, silu_obj],
    )
    mlir_dep = xclbin_art.depends[0]
    xclbin_art = XclbinArtifact.new("L2bn_instrument.xclbin", depends=[mlir_dep, kernel_dep])
    insts_art = InstsBinArtifact.new("L2bn_instrument.bin", depends=[mlir_dep])
    op.xclbin_artifact = xclbin_art
    op.insts_artifact = insts_art
    op.add_artifacts([xclbin_art, insts_art])

    ctx.compile_all()
    ctx.prepare_runtime()

    return op, x, wt, bias


def instrumented_forward(op, x, wt, bias):
    """Run forward() with per-step timing, returning dict of step times in ms."""
    timings = {}

    # -- Step 1: nchw_to_tiled_int8 --
    t0 = time.perf_counter()
    input_tiled = nchw_to_tiled_int8(x)
    t1 = time.perf_counter()
    timings["nchw_to_tiled_int8"] = (t1 - t0) * 1000

    out_h = op.out_height
    out_w = op.out_width

    # -- Step 2: zero-padding (stride-1 specific) --
    t0 = time.perf_counter()
    zero_row = np.zeros(op.in_channels * op.width, dtype=np.int8)
    input_tiled = np.concatenate([zero_row, input_tiled, zero_row])
    t1 = time.perf_counter()
    timings["zero_padding"] = (t1 - t0) * 1000

    # -- Step 3: write_buffer("input") --
    t0 = time.perf_counter()
    op.write_buffer("input", input_tiled)
    t1 = time.perf_counter()
    timings["write_buffer_input"] = (t1 - t0) * 1000

    # -- Step 4: weights_to_tiled_int8_k3 + bias packing --
    t0 = time.perf_counter()
    n_oc_groups, oc_chunk, tile_height = _compute_k3_fused_streaming(
        op.in_channels, op.out_channels, op.width, out_w,
        op.height, op.stride, op.num_aie_columns,
    )
    oc_per_col = op.out_channels // op.num_aie_columns
    weight_tiled = weights_to_tiled_int8_k3(wt)
    wt_per_chunk = oc_chunk * op.in_channels * 9
    chunks = []
    for col in range(op.num_aie_columns):
        col_wt_base = col * oc_per_col * op.in_channels * 9
        col_bias_base = col * oc_per_col
        for g in range(n_oc_groups):
            w_start = col_wt_base + g * wt_per_chunk
            w_chunk = weight_tiled[w_start : w_start + wt_per_chunk]
            b_start = col_bias_base + g * oc_chunk
            b_chunk = bias[b_start : b_start + oc_chunk]
            b_bytes = b_chunk.numpy().astype(np.int32).view(np.int8)
            chunks.append(np.concatenate([w_chunk, b_bytes]))
    packed = np.concatenate(chunks)
    t1 = time.perf_counter()
    timings["weight_tiling_and_bias_pack"] = (t1 - t0) * 1000

    # -- Step 5: write_buffer("weights") --
    t0 = time.perf_counter()
    op.write_buffer("weights", packed)
    t1 = time.perf_counter()
    timings["write_buffer_weights"] = (t1 - t0) * 1000

    # -- Step 6: write_buffer("output") (zeroing) --
    t0 = time.perf_counter()
    total_output = op.out_channels * out_h * out_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))
    t1 = time.perf_counter()
    timings["write_buffer_output_zero"] = (t1 - t0) * 1000

    # -- Step 7: run_runlist() broken into sub-phases --
    # Replicate the logic from aie_base.py run_runlist() with per-phase timing
    import pyxrt

    kernel_name, *buffer_args = op.runlist[0]
    context_rt, xrt_kernel, insts_bo, insts_len = op.xrt_kernels[kernel_name]
    bos = [op.buffer_bos[ba] for ba in buffer_args]

    # 7a: sync instructions BO to device
    t0 = time.perf_counter()
    insts_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
    t1 = time.perf_counter()
    timings["run_sync_insts_to_dev"] = (t1 - t0) * 1000

    # 7b: sync data BOs to device
    t0 = time.perf_counter()
    for bo in bos:
        bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
    t1 = time.perf_counter()
    timings["run_sync_data_to_dev"] = (t1 - t0) * 1000

    # 7c: kernel launch
    t0 = time.perf_counter()
    opcode = 3
    run = xrt_kernel(opcode, insts_bo, insts_len, *bos)
    t1 = time.perf_counter()
    timings["run_kernel_launch"] = (t1 - t0) * 1000

    # 7d: wait for completion
    t0 = time.perf_counter()
    result = run.wait()
    t1 = time.perf_counter()
    timings["run_wait"] = (t1 - t0) * 1000

    if result != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
        raise RuntimeError(f"Kernel did not complete: {result}")

    # 7e: sync data BOs from device
    t0 = time.perf_counter()
    for bo in bos:
        bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)
    t1 = time.perf_counter()
    timings["run_sync_data_from_dev"] = (t1 - t0) * 1000

    # -- Step 8: read_buffer("output") --
    t0 = time.perf_counter()
    output_flat = op.read_buffer("output", (total_output,), copy=True, dtype=np.int8)
    t1 = time.perf_counter()
    timings["read_buffer_output"] = (t1 - t0) * 1000

    # -- Step 9: tiled_to_nchw_int8 conversion --
    t0 = time.perf_counter()
    result = tiled_to_nchw_int8(output_flat, op.out_channels, out_h, out_w)
    t1 = time.perf_counter()
    timings["tiled_to_nchw_int8"] = (t1 - t0) * 1000

    return timings, result


def main():
    print(f"L2bn Instrumented Forward")
    print(f"  IC={IC}, OC={OC}, H={H}, W={W}, stride={STRIDE}")
    print(f"  fused=True, shift1={SHIFT1}, shift2={SHIFT2}")
    print()

    print("Building and compiling operator...")
    op, x, wt, bias = build_op()
    print("Compilation done.\n")

    # Warmup run (full forward)
    print("Warmup run (full forward)...")
    t0 = time.perf_counter()
    op.forward(x, wt, bias)
    warmup_ms = (time.perf_counter() - t0) * 1000
    print(f"  Warmup: {warmup_ms:.1f} ms\n")

    # Instrumented runs
    print(f"Running {N_ITERS} instrumented iterations...\n")

    all_timings = []
    for i in range(N_ITERS):
        t_total_start = time.perf_counter()
        timings, result = instrumented_forward(op, x, wt, bias)
        t_total_end = time.perf_counter()
        timings["_total_instrumented"] = (t_total_end - t_total_start) * 1000
        all_timings.append(timings)

        print(f"--- Iteration {i+1} ---")
        for step, ms in timings.items():
            if step.startswith("_"):
                continue
            print(f"  {step:<35s} {ms:8.2f} ms")
        print(f"  {'TOTAL (sum of steps)':<35s} {sum(v for k,v in timings.items() if not k.startswith('_')):8.2f} ms")
        print(f"  {'TOTAL (wall clock)':<35s} {timings['_total_instrumented']:8.2f} ms")
        print()

    # Summary: averages across iterations
    print("=" * 60)
    print("AVERAGE across iterations:")
    print("=" * 60)
    steps = [k for k in all_timings[0] if not k.startswith("_")]
    for step in steps:
        vals = [t[step] for t in all_timings]
        avg = sum(vals) / len(vals)
        mn = min(vals)
        mx = max(vals)
        print(f"  {step:<35s}  avg={avg:8.2f}  min={mn:8.2f}  max={mx:8.2f} ms")

    total_vals = [sum(t[k] for k in steps) for t in all_timings]
    print(f"  {'TOTAL (sum of steps)':<35s}  avg={sum(total_vals)/len(total_vals):8.2f}  "
          f"min={min(total_vals):8.2f}  max={max(total_vals):8.2f} ms")
    wall_vals = [t["_total_instrumented"] for t in all_timings]
    print(f"  {'TOTAL (wall clock)':<35s}  avg={sum(wall_vals)/len(wall_vals):8.2f}  "
          f"min={min(wall_vals):8.2f}  max={max(wall_vals):8.2f} ms")


if __name__ == "__main__":
    main()
