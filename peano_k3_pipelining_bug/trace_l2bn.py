#!/usr/bin/env python3
"""Run L2bn with AIE Trace to measure on-chip cycle counts.

Uses the existing compilation infrastructure with trace_size enabled.
After NPU execution, reads the trace buffer and parses event0/event1
timestamps to get per-tile kernel cycle counts.

Usage:
    source /scratch/jmelber/mlir-aie/ironenv/bin/activate
    source /scratch/jmelber/mlir-aie/utils/env_setup.sh /scratch/jmelber/mlir-aie /opt/xrt
    PYTHONPATH="/scratch/jmelber/bug/IRON:$PYTHONPATH" python3 peano_k3_pipelining_bug/trace_l2bn.py
"""

import time
from pathlib import Path

import numpy as np
import torch

from iron.common import (
    AIEContext, KernelObjectArtifact, LinkedKernelObjectArtifact,
    SourceArtifact, XclbinArtifact, InstsBinArtifact,
)
from iron.operators.conv2d_int8.op import AIEConv2dInt8

BUG_DIR = Path(__file__).parent

IC = 16
OC = 16
H = 160
W = 160
STRIDE = 1
SHIFT1 = 10
SHIFT2 = 128
TRACE_SIZE = 16384


def main():
    import pyxrt

    print(f"L2bn Trace Profiling")
    print(f"  IC={IC}, OC={OC}, H={H}, W={W}, stride={STRIDE}")
    print(f"  trace_size={TRACE_SIZE} bytes\n")

    torch.manual_seed(42)
    x = torch.randint(-128, 128, (1, IC, H, W), dtype=torch.int8)
    wt = torch.randint(-128, 128, (OC, IC, 3, 3), dtype=torch.int8)
    bias = torch.randint(-5000, 5001, (OC,), dtype=torch.int32)

    # Build with trace enabled
    ctx = AIEContext()
    op = AIEConv2dInt8(
        in_channels=IC, out_channels=OC, kernel_size=3, stride=STRIDE,
        height=H, width=W, fused=True, shift1=SHIFT1, shift2=SHIFT2,
        silu_variant="split", trace_size=TRACE_SIZE, context=ctx,
    )

    tag = "L2bn_trace"
    xclbin_art, insts_art = op.get_artifacts(prefix=f"{tag}_")
    extra_flags = ["-DINT8_ACT", "-ffunction-sections", "-fdata-sections"]
    mac_obj = KernelObjectArtifact.new(
        f"conv2dk3_i8_silu_{tag}_mac.o",
        depends=[SourceArtifact.new(BUG_DIR / "conv2dk3_i8_silu_scalar_workaround.cc")],
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

    print("Compiling...")
    ctx.compile_all()
    ctx.prepare_runtime()
    print("Compilation done.\n")

    # Allocate trace buffer BO using same XRT device/kernel
    # The trace uses ddr_id=4 which maps to group_id(7)
    # Our kernel args are: opcode, insts, insts_len, input(0), weights(1), output(2)
    # Trace needs arg index 4 => we need dummy arg at index 3
    kernel_name = list(op.xrt_kernels.keys())[0]
    _, xrt_kernel, insts_bo, insts_len = op.xrt_kernels[kernel_name]
    device = ctx.device_manager.device

    # Allocate trace BO at group_id for arg index 4
    # group_id mapping: arg 0 -> group_id(3), arg 1 -> group_id(4), etc.
    # trace ddr_id=4 patches npu_address_patch at arg_idx=4
    try:
        trace_bo = pyxrt.bo(device, TRACE_SIZE,
                            pyxrt.bo.flags.host_only, xrt_kernel.group_id(4))
    except Exception as e:
        print(f"  Could not allocate trace BO at group_id(4): {e}")
        print(f"  Trying group_id(7) directly...")
        trace_bo = pyxrt.bo(device, TRACE_SIZE,
                            pyxrt.bo.flags.host_only, 7)

    # Zero trace buffer and sync
    trace_mv = trace_bo.map()
    np.copyto(np.frombuffer(trace_mv, dtype=np.uint8, count=TRACE_SIZE),
              np.zeros(TRACE_SIZE, dtype=np.uint8))
    trace_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)

    # Warmup (without trace BO)
    print("Warmup run...")
    op.forward(x, wt, bias)
    print("Done.\n")

    # Prepare input data
    from iron.operators.conv2d_int8.op import (
        nchw_to_tiled_int8, tiled_to_nchw_int8,
        weights_to_tiled_int8_k3, _compute_k3_fused_streaming,
    )
    input_tiled = nchw_to_tiled_int8(x)
    zero_row = np.zeros(IC * W, dtype=np.int8)
    input_padded = np.concatenate([zero_row, input_tiled, zero_row])
    op.write_buffer("input", input_padded)

    out_h = op.out_height
    out_w = op.out_width
    n_oc_groups, oc_chunk, tile_height = _compute_k3_fused_streaming(
        IC, OC, W, out_w, H, STRIDE, 1
    )
    weight_tiled = weights_to_tiled_int8_k3(wt)
    wt_per_chunk = oc_chunk * IC * 9
    chunks = []
    oc_per_col = OC
    for g in range(n_oc_groups):
        w_start = g * wt_per_chunk
        w_chunk = weight_tiled[w_start: w_start + wt_per_chunk]
        b_start = g * oc_chunk
        b_chunk = bias[b_start: b_start + oc_chunk]
        b_bytes = b_chunk.numpy().astype(np.int32).view(np.int8)
        chunks.append(np.concatenate([w_chunk, b_bytes]))
    packed = np.concatenate(chunks)
    op.write_buffer("weights", packed)

    total_output = OC * out_h * out_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Re-zero trace buffer
    np.copyto(np.frombuffer(trace_mv, dtype=np.uint8, count=TRACE_SIZE),
              np.zeros(TRACE_SIZE, dtype=np.uint8))
    trace_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)

    # Run with trace BO appended
    print("Running on NPU with trace enabled...")
    bos = [op.buffer_bos[ba] for ba in op.runlist[0][1:]]

    insts_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
    for bo in bos:
        bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)

    # Trace uses arg_idx=4 (npu_address_patch). Our data BOs are args 0-2.
    # We need a dummy BO at arg 3 so trace lands at arg 4.
    dummy_bo = pyxrt.bo(device, 4, pyxrt.bo.flags.host_only,
                        xrt_kernel.group_id(3))

    opcode = 3
    t0 = time.perf_counter()
    run = xrt_kernel(opcode, insts_bo, insts_len, *bos, dummy_bo, trace_bo)
    result = run.wait()
    elapsed = (time.perf_counter() - t0) * 1000
    print(f"  NPU execution: {elapsed:.1f} ms")

    if result != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
        print(f"  ERROR: {result}")
        return

    for bo in bos:
        bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)
    trace_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)

    # Read trace buffer
    trace_data = np.frombuffer(trace_bo.map(), dtype=np.uint32,
                               count=TRACE_SIZE // 4).copy()

    nonzero = np.count_nonzero(trace_data)
    print(f"\nTrace buffer: {nonzero} non-zero words out of {len(trace_data)}")

    if nonzero == 0:
        print("  No trace data captured. Trace may not be configured correctly.")
        print("  Dumping MLIR for inspection...")
        # Find and show the generated MLIR
        import glob
        mlir_files = glob.glob(str(ctx.build_dir / f"{tag}*.mlir"))
        for f in mlir_files:
            print(f"  Found: {f}")
        return

    # Dump raw trace words for analysis
    print(f"\n  Raw trace words (non-zero):")
    for i in range(len(trace_data)):
        if trace_data[i] != 0:
            print(f"    [{i:4d}] 0x{trace_data[i]:08x}")
        if i > 200 and trace_data[i] == 0:
            # Stop after a run of zeros past the first 200
            remaining = np.count_nonzero(trace_data[i:])
            if remaining == 0:
                break

    # Try to parse trace
    print(f"\nParsing trace events...")
    # Read the generated MLIR
    import glob
    mlir_files = glob.glob(str(ctx.build_dir / f"{tag}*.mlir"))
    mlir_module_str = ""
    if mlir_files:
        with open(mlir_files[0]) as f:
            mlir_module_str = f.read()
        print(f"  Using MLIR: {mlir_files[0]}")

    from aie.utils.trace import parse_trace
    try:
        events = parse_trace(trace_data, mlir_module_str)
        print(f"  Parsed {len(events)} trace events\n")

        # Show all events
        for ev in events[:50]:
            print(f"    {ev.get('ph','?'):2s} {ev.get('name','?'):<30s} ts={ev.get('ts',0):>12,}")

        # Extract event0/event1 durations
        event0_ts = []
        event1_ts = []
        for ev in events:
            name = ev.get("name", "")
            ph = ev.get("ph", "")
            ts = ev.get("ts", 0)
            if "EVENT_0" in name and ph == "B":
                event0_ts.append(ts)
            elif "EVENT_0" in name and ph == "E":
                event1_ts.append(ts)  # event0 end = event1

        if event0_ts and event1_ts:
            pairs = list(zip(event0_ts, event1_ts))
            print(f"\n  Kernel invocations ({len(pairs)} pairs):")
            for i, (e0, e1) in enumerate(pairs[:15]):
                dur = e1 - e0
                print(f"    tile {i:3d}: {dur:>10,} cycles  ({dur / 1.3e6:.3f} ms)")
            if len(pairs) > 15:
                print(f"    ... ({len(pairs)} total)")

            total_cycles = sum(e1 - e0 for e0, e1 in pairs)
            print(f"\n  Total kernel cycles: {total_cycles:,}")
            print(f"  Total at 1.3 GHz: {total_cycles / 1.3e6:.3f} ms")
            print(f"  Wall-clock: {elapsed:.1f} ms")
            if total_cycles > 0:
                print(f"  Non-compute overhead: {elapsed - total_cycles / 1.3e6:.1f} ms")
    except Exception as e:
        print(f"  Parse error: {e}")
        import traceback
        traceback.print_exc()

    # Correctness check
    output_flat = op.read_buffer("output", (total_output,), copy=True, dtype=np.int8)
    npu_result = tiled_to_nchw_int8(output_flat, OC, out_h, out_w)

    import torch.nn.functional as F
    acc = F.conv2d(x.int(), wt.int(), stride=STRIDE, padding=1)
    acc = acc + bias.view(1, -1, 1, 1).int()
    fval = acc.float() / float(1 << SHIFT1)
    z = fval * 0.5
    z2 = z * z
    tanh_z = torch.where(z2 > 20.0, torch.sign(z),
                         z * (27.0 + z2) / (27.0 + 9.0 * z2))
    silu = fval * 0.5 * (1.0 + tanh_z)
    ref = torch.clamp(torch.round(silu * SHIFT2 / 256.0), -128, 127).to(torch.int8)

    diff = np.abs(ref.numpy().reshape(-1).astype(np.int32) -
                  npu_result.numpy().reshape(-1).astype(np.int32))
    errors = int(np.sum(diff > 2))
    print(f"\n  Correctness: {errors} errors out of {len(diff)} elements")


if __name__ == "__main__":
    main()
