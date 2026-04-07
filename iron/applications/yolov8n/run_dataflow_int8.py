#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Run YOLOv8n with full dataflow on NPU (int8) — 13 PDIs, 4 AIEContexts.

Architecture:
  - Backbone (L0-L7): dataflow phases on NPU (5 PDIs, 1 shared AIEContext)
  - L8 C2f + L9 SPPF: 2 PDIs, 1 shared AIEContext
  - Neck (L12+L15, L16+L18, L19+L21): 3 fused dataflow PDIs, 1 shared AIEContext
  - Detect (P3, P4, P5): 3 dataflow PDIs, 1 shared AIEContext
  - CPU-only ops between PDIs: upsample, concat, skip pre-fills

13-PDI pipeline (4 AIEContexts):
  Context 1 — Backbone:
    Phase 1:  L0→L1→L2(C2f)→L3  (8→64ch, 640→80)   8 cores, 2 columns
    Phase 2:  L4 C2f n=2         (64→64ch, 80×80)    7 cores, 2 columns
    Phase 3:  L5 CBS             (64→128ch, 80→40)   1 core, OC streaming
    Phase 4:  L6 C2f n=2         (128→128ch, 40×40)  8 cores, 2 columns
    Phase 5:  L7 CBS             (128→256ch, 40→20)  1 core, OC streaming
  Context 2 — L8+L9:
    Phase 6:  L8 C2f n=1         (256→256ch, 20×20)  4 workers, fused SiLU
    Phase 7:  L9 SPPF            (256→256ch, 20×20)  3 workers, maxpool on NPU
  Context 3 — Neck:
    Phase 8:  L12+L15            (384→64ch, 40→80)   fused PDI
    Phase 9:  L16+L18            (64→128ch, 80→40)   fused PDI
    Phase 10: L19+L21            (128→256ch, 40→20)  fused PDI, 2-column
  Context 4 — Detect:
    Phase 11: Detect P3           (64→64+80, 80×80)  6 workers
    Phase 12: Detect P4           (128→64+80, 40×40) 6 workers
    Phase 13: Detect P5           (256→64+80, 20×20) 6 workers

Usage:
    python3 iron/applications/yolov8n/run_dataflow_int8.py [--image PATH]
"""

import argparse
import time
import urllib.request
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

from iron.common import AIEContext
from iron.applications.yolov8n.pipeline_int8 import (
    Int8ConvPipeline,
    PRED_MAP,
    _buf,
    compute_all_shifts,
    lookup_weight,
)
from iron.operators.conv2d_int8.op import (
    nchw_to_tiled_int8,
    tiled_to_nchw_int8,
    weights_to_tiled_int8,
    weights_to_tiled_int8_k3,
)
from iron.applications.yolov8n.postprocess import YOLOv8nPostProcess
from iron.applications.yolov8n.run_int8_cpu import Int8YOLOv8nCPU
from iron.applications.yolov8n.run_pretrained import (
    COCO_NAMES,
    preprocess_image,
)
from iron.applications.yolov8n.run_pretrained_int8 import (
    get_percentile,
)
from iron.applications.yolov8n.pipeline_int8 import compute_fused_shifts


def upsample_tiled_2x(data, channels, height, width):
    """Nearest-neighbor 2x upsample in tiled format [H, C/8, W, 8]."""
    t = data.reshape(height, channels // 8, width, 8)
    t = np.repeat(t, 2, axis=0)  # double rows
    t = np.repeat(t, 2, axis=2)  # double columns
    return t.ravel()


def concat_tiled(a, b, ca, cb, h, w):
    """Channel-concat two tiled buffers: [H, CA/8, W, 8] + [H, CB/8, W, 8]."""
    ta = a.reshape(h, ca // 8, w, 8)
    tb = b.reshape(h, cb // 8, w, 8)
    return np.concatenate([ta, tb], axis=1).ravel()


# Import dataflow operator classes from test_dataflow.py
import sys

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent.parent / "operators" / "conv2d_int8"),
)
from test_dataflow import (
    AIEDataflowBackbonePhase1,
    AIEDataflowC2fL4,
    AIEDataflowC2fL6,
    AIEDataflowC2fL8,
    AIEDataflowSPPFL9,
    AIEDataflowFusedOCStreaming,
    AIEDataflowL12L15,
    AIEDataflowL16L18,
    AIEDataflowL19L21_2col,
    AIEDataflowDetectScale,
    AIEDataflowDetectScale4Col,
    pack_fused_weights_k3,
    _pack_k1_silu_weights,
)


def _prescale_bias(bias_float, w_scale, in_act_scale):
    """Pre-scale float bias to int32 in the accumulator domain.

    bias_int32 = round(bias_float / (w_scale * in_act_scale))
    """
    combined = float(w_scale * in_act_scale)
    if combined == 0:
        combined = 1.0
    return np.round(bias_float.numpy() / combined).astype(np.int32)


def _pack_fused_k3(w_int8, bias_float, w_scale, in_act_scale):
    """Pack k3 weights + pre-scaled bias for fused conv+bias+SiLU."""
    b_int32 = _prescale_bias(bias_float, w_scale, in_act_scale)
    w_tiled = weights_to_tiled_int8_k3(w_int8)
    return np.concatenate([w_tiled, b_int32.view(np.int8)])


def _pack_fused_k1(w_int8, bias_float, w_scale, in_act_scale):
    """Pack k1 weights + pre-scaled bias for fused conv+bias+SiLU."""
    b_int32 = _prescale_bias(bias_float, w_scale, in_act_scale)
    w_tiled = weights_to_tiled_int8(w_int8)
    return np.concatenate([w_tiled, b_int32.view(np.int8)])


def run_backbone_dataflow(
    x_int8,
    int8_weights,
    act_scales,
    shifts,
):
    """Run backbone phases 1-5 using dataflow PDIs.

    Args:
        x_int8: Input tensor [1, 8, 640, 640] int8 (padded 3→8 channels).
        int8_weights: Dict of quantized weight tensors.
        act_scales: Dict of per-layer activation scales.
        shifts: Dict of per-layer shift values.

    Returns:
        Tuple of (p3, p4, p5) tensors — the three backbone feature maps.
        p3: [1, 64, 80, 80]  for detect head scale P3
        p4: [1, 128, 40, 40] for detect head scale P4
        p5: [1, 256, 20, 20] for detect head scale P5
    """
    H, W = x_int8.shape[2], x_int8.shape[3]
    assert H == 640 and W == 640, f"Expected 640x640, got {H}x{W}"

    def get_shift(name):
        """Extract shift1 and shift2 from shifts dict."""
        s = shifts[name]
        if isinstance(s, tuple):
            return s
        return (s, 7)  # default shift2=7

    # ===== Create shared context for all backbone phases =====
    ctx = AIEContext()

    # --- Register all 5 backbone operators on the shared context ---
    l0_s1, l0_s2 = get_shift("l0")
    l1_s1, l1_s2 = get_shift("l1")
    cv1_s1, cv1_s2 = get_shift("l2.cv1")
    bn1_s1, bn1_s2 = get_shift("l2.bn0.cv1")
    bn2_s1, bn2_s2 = get_shift("l2.bn0.cv2")
    cv2_s1, cv2_s2 = get_shift("l2.cv2")
    l3_s1, l3_s2 = get_shift("l3")

    op1 = AIEDataflowBackbonePhase1(
        l0_height=640,
        l0_width=640,
        l0_ic=8,
        l0_oc=16,
        l0_shift1=l0_s1,
        l0_shift2=l0_s2,
        l1_oc=32,
        l1_shift1=l1_s1,
        l1_shift2=l1_s2,
        cv1_shift1=cv1_s1,
        cv1_shift2=cv1_s2,
        bn_cv1_shift1=bn1_s1,
        bn_cv1_shift2=bn1_s2,
        bn_cv2_shift1=bn2_s1,
        bn_cv2_shift2=bn2_s2,
        cv2_shift1=cv2_s1,
        cv2_shift2=cv2_s2,
        l3_oc=64,
        l3_shift1=l3_s1,
        l3_shift2=l3_s2,
        context=ctx,
    )

    p2_scale = shifts.get("l4.cv1", 10)
    if isinstance(p2_scale, tuple):
        p2_scale = p2_scale[0]

    op2 = AIEDataflowC2fL4(
        height=80,
        width=80,
        in_channels=64,
        cv1_scale=p2_scale,
        bn0_cv1_scale=p2_scale,
        bn0_cv2_scale=p2_scale,
        bn1_cv1_scale=p2_scale,
        bn1_cv2_scale=p2_scale,
        cv2_scale=p2_scale,
        context=ctx,
    )

    l5_s1, l5_s2 = get_shift("l5")

    op3 = AIEDataflowFusedOCStreaming(
        height=80,
        width=80,
        in_channels=64,
        out_channels=128,
        shift1=l5_s1,
        shift2=l5_s2,
        context=ctx,
    )

    p4_scale = shifts.get("l6.cv1", 10)
    if isinstance(p4_scale, tuple):
        p4_scale = p4_scale[0]

    op4 = AIEDataflowC2fL6(
        height=40,
        width=40,
        in_channels=128,
        cv1_scale=p4_scale,
        bn0_cv1_scale=p4_scale,
        bn0_cv2_scale=p4_scale,
        bn1_cv1_scale=p4_scale,
        bn1_cv2_scale=p4_scale,
        cv2_scale=p4_scale,
        context=ctx,
    )

    l7_s1, l7_s2 = get_shift("l7")

    op5 = AIEDataflowFusedOCStreaming(
        height=40,
        width=40,
        in_channels=128,
        out_channels=256,
        shift1=l7_s1,
        shift2=l7_s2,
        context=ctx,
    )

    # Compile and prepare all 5 backbone operators at once
    ctx.compile_all()
    ctx.prepare_runtime()

    # Timing accumulators
    t_weight_pack = 0.0
    t_npu = 0.0
    t_buffer_io = 0.0

    # ===== Pre-pack ALL weights before any phase runs =====

    def _pad(data, slot_size):
        pad = np.zeros(slot_size - len(data), dtype=np.int8)
        return np.concatenate([data, pad])

    _t = time.perf_counter()

    # Phase 1 weights
    w0, ws0, b0 = lookup_weight(int8_weights, "l0")
    w1, ws1, b1 = lookup_weight(int8_weights, "l1")
    w_cv1, ws_cv1, b_cv1 = lookup_weight(int8_weights, "l2.cv1")
    w_bn1, ws_bn1, b_bn1 = lookup_weight(int8_weights, "l2.bn0.cv1")
    w_bn2, ws_bn2, b_bn2 = lookup_weight(int8_weights, "l2.bn0.cv2")
    w_cv2, ws_cv2, b_cv2 = lookup_weight(int8_weights, "l2.cv2")
    w3, ws3, b3 = lookup_weight(int8_weights, "l3")

    l0_in_sc = act_scales.get("input", 1.0)
    if l0_in_sc == 0:
        l0_in_sc = 1.0
    l0_out = 256.0 / float(l0_s2) if l0_s2 > 0 else 1.0
    l1_out = 256.0 / float(l1_s2) if l1_s2 > 0 else 1.0
    cv1_out_sc = 256.0 / float(cv1_s2) if cv1_s2 > 0 else 1.0
    bn1_out_sc = 256.0 / float(bn1_s2) if bn1_s2 > 0 else 1.0
    bn2_out_sc = 256.0 / float(bn2_s2) if bn2_s2 > 0 else 1.0
    cv2_out_sc = 256.0 / float(cv2_s2) if cv2_s2 > 0 else 1.0

    tg1_wt_slot = op1._tg1_wt_slot
    c2f_wt_slot = op1._c2f_wt_slot

    tg1_packed = np.concatenate(
        [
            _pad(_pack_fused_k3(w0, b0, ws0, l0_in_sc), tg1_wt_slot),
            _pad(_pack_fused_k3(w1, b1, ws1, l0_out), tg1_wt_slot),
        ]
    )
    c2f_packed = np.concatenate(
        [
            _pad(_pack_fused_k1(w_cv1, b_cv1, ws_cv1, l1_out), c2f_wt_slot),
            _pad(_pack_fused_k3(w_bn1, b_bn1, ws_bn1, cv1_out_sc), c2f_wt_slot),
            _pad(_pack_fused_k3(w_bn2, b_bn2, ws_bn2, bn1_out_sc), c2f_wt_slot),
            _pad(_pack_fused_k1(w_cv2, b_cv2, ws_cv2, cv1_out_sc), c2f_wt_slot),
        ]
    )
    l3_packed = _pack_fused_k3(w3, b3, ws3, cv2_out_sc)

    t_weight_pack += time.perf_counter() - _t

    _t = time.perf_counter()
    op1.write_buffer("weights", np.concatenate([tg1_packed, c2f_packed, l3_packed]))
    t_buffer_io += time.perf_counter() - _t

    _t = time.perf_counter()

    # Phase 2 weights
    w_cv1_p2, _, _ = lookup_weight(int8_weights, "l4.cv1")
    w_bn0cv1, _, _ = lookup_weight(int8_weights, "l4.bn0.cv1")
    w_bn0cv2, _, _ = lookup_weight(int8_weights, "l4.bn0.cv2")
    w_bn1cv1, _, _ = lookup_weight(int8_weights, "l4.bn1.cv1")
    w_bn1cv2, _, _ = lookup_weight(int8_weights, "l4.bn1.cv2")
    w_cv2_p2, _, _ = lookup_weight(int8_weights, "l4.cv2")

    packed_p2 = np.concatenate(
        [
            weights_to_tiled_int8(w_cv1_p2),
            weights_to_tiled_int8_k3(w_bn0cv1),
            weights_to_tiled_int8_k3(w_bn0cv2),
            weights_to_tiled_int8_k3(w_bn1cv1),
            weights_to_tiled_int8_k3(w_bn1cv2),
            weights_to_tiled_int8(w_cv2_p2),
        ]
    )

    t_weight_pack += time.perf_counter() - _t

    _t = time.perf_counter()
    op2.write_buffer("weights", packed_p2)
    t_buffer_io += time.perf_counter() - _t

    _t = time.perf_counter()

    # Phase 3 weights
    w_l5, ws_l5, b_l5 = lookup_weight(int8_weights, "l5")
    l5_in_scale = act_scales.get("l4.cv2", 1.0)
    b_l5_i32 = _prescale_bias(b_l5, ws_l5, l5_in_scale)
    oc_chunk_l5 = op3._oc_chunk
    n_oc_groups_l5 = op3._n_oc_groups
    packed_chunks_l5 = []
    for g in range(n_oc_groups_l5):
        oc_start = g * oc_chunk_l5
        oc_end = oc_start + oc_chunk_l5
        w_chunk = w_l5[oc_start:oc_end]
        b_chunk = b_l5_i32[oc_start:oc_end]
        w_tiled = weights_to_tiled_int8_k3(w_chunk)
        packed_chunks_l5.append(np.concatenate([w_tiled, b_chunk.view(np.int8)]))

    t_weight_pack += time.perf_counter() - _t

    _t = time.perf_counter()
    op3.write_buffer("weights", np.concatenate(packed_chunks_l5))
    t_buffer_io += time.perf_counter() - _t

    _t = time.perf_counter()

    # Phase 4 weights
    w_cv1_p4, _, _ = lookup_weight(int8_weights, "l6.cv1")
    w_bn0cv1_p4, _, _ = lookup_weight(int8_weights, "l6.bn0.cv1")
    w_bn0cv2_p4, _, _ = lookup_weight(int8_weights, "l6.bn0.cv2")
    w_bn1cv1_p4, _, _ = lookup_weight(int8_weights, "l6.bn1.cv1")
    w_bn1cv2_p4, _, _ = lookup_weight(int8_weights, "l6.bn1.cv2")
    w_cv2_p4, _, _ = lookup_weight(int8_weights, "l6.cv2")

    packed_p4 = np.concatenate(
        [
            weights_to_tiled_int8(w_cv1_p4),
            weights_to_tiled_int8_k3(w_bn0cv1_p4),
            weights_to_tiled_int8_k3(w_bn0cv2_p4),
            weights_to_tiled_int8_k3(w_bn1cv1_p4),
            weights_to_tiled_int8_k3(w_bn1cv2_p4),
            weights_to_tiled_int8(w_cv2_p4),
        ]
    )

    t_weight_pack += time.perf_counter() - _t

    _t = time.perf_counter()
    op4.write_buffer("weights", packed_p4)
    t_buffer_io += time.perf_counter() - _t

    _t = time.perf_counter()

    # Phase 5 weights
    w_l7, ws_l7, b_l7 = lookup_weight(int8_weights, "l7")
    l7_in_scale = act_scales.get("l6.cv2", 1.0)
    b_l7_i32 = _prescale_bias(b_l7, ws_l7, l7_in_scale)
    oc_chunk_l7 = op5._oc_chunk
    n_oc_groups_l7 = op5._n_oc_groups
    packed_chunks_l7 = []
    for g in range(n_oc_groups_l7):
        oc_start = g * oc_chunk_l7
        oc_end = oc_start + oc_chunk_l7
        w_chunk = w_l7[oc_start:oc_end]
        b_chunk = b_l7_i32[oc_start:oc_end]
        w_tiled = weights_to_tiled_int8_k3(w_chunk)
        packed_chunks_l7.append(np.concatenate([w_tiled, b_chunk.view(np.int8)]))

    t_weight_pack += time.perf_counter() - _t

    _t = time.perf_counter()
    op5.write_buffer("weights", np.concatenate(packed_chunks_l7))
    t_buffer_io += time.perf_counter() - _t

    # ===== Phase 1: L0→L1→L2(C2f)→L3 =====
    print("  Phase 1: L0→L1→L2→L3 ...", end="", flush=True)

    _t = time.perf_counter()
    op1.write_buffer("input", nchw_to_tiled_int8(x_int8))
    op1.write_buffer("output", np.zeros(op1.buffers["output"], dtype=np.int8))
    t_buffer_io += time.perf_counter() - _t

    t0 = time.perf_counter()
    op1.run_runlist()
    t1 = time.perf_counter()
    t_npu += t1 - t0
    print(f" {1000 * (t1 - t0):.0f}ms")

    _t = time.perf_counter()
    total_output_buf = op1.buffers["output"]
    output_buf = op1.read_buffer("output", (total_output_buf,), dtype=np.int8)
    p1_output = output_buf[: op1._total_output].copy()
    t_buffer_io += time.perf_counter() - _t

    # ===== Phase 2: C2f L4 (64→64, 80×80) =====
    print("  Phase 2: C2f L4 ...", end="", flush=True)

    _t = time.perf_counter()
    op2.write_buffer("input", p1_output)
    p2_total_output = 64 * 80 * 80
    p2_concat_size = 128 * 80 * 80
    p2_output_buf_size = p2_total_output + p2_concat_size
    op2.write_buffer("output", np.zeros(p2_output_buf_size, dtype=np.int8))
    t_buffer_io += time.perf_counter() - _t

    t0 = time.perf_counter()
    op2.run_runlist()
    t1 = time.perf_counter()
    t_npu += t1 - t0
    print(f" {1000 * (t1 - t0):.0f}ms")

    _t = time.perf_counter()
    output_raw_p2 = op2.read_buffer("output", (p2_output_buf_size,), dtype=np.int8)
    p3_tiled = output_raw_p2[:p2_total_output].copy()
    t_buffer_io += time.perf_counter() - _t

    # ===== Phase 3: L5 CBS (64→128, s2, 80→40) =====
    print("  Phase 3: L5 ...", end="", flush=True)

    _t = time.perf_counter()
    op3.write_buffer("input", p3_tiled)
    p3_total_output = 128 * 40 * 40
    op3.write_buffer("output", np.zeros(p3_total_output, dtype=np.int8))
    t_buffer_io += time.perf_counter() - _t

    t0 = time.perf_counter()
    op3.run_runlist()
    t1 = time.perf_counter()
    t_npu += t1 - t0
    print(f" {1000 * (t1 - t0):.0f}ms")

    _t = time.perf_counter()
    p3_output = op3.read_buffer("output", (p3_total_output,), dtype=np.int8).copy()
    t_buffer_io += time.perf_counter() - _t

    # ===== Phase 4: C2f L6 (128→128, 40×40) =====
    print("  Phase 4: C2f L6 ...", end="", flush=True)

    _t = time.perf_counter()
    op4.write_buffer("input", p3_output)
    p4_total_output = 128 * 40 * 40
    p4_concat_size = 256 * 40 * 40
    p4_output_buf_size = p4_total_output + p4_concat_size
    op4.write_buffer("output", np.zeros(p4_output_buf_size, dtype=np.int8))
    t_buffer_io += time.perf_counter() - _t

    t0 = time.perf_counter()
    op4.run_runlist()
    t1 = time.perf_counter()
    t_npu += t1 - t0
    print(f" {1000 * (t1 - t0):.0f}ms")

    _t = time.perf_counter()
    output_raw_p4 = op4.read_buffer("output", (p4_output_buf_size,), dtype=np.int8)
    p4_tiled = output_raw_p4[:p4_total_output].copy()
    t_buffer_io += time.perf_counter() - _t

    # ===== Phase 5: L7 CBS (128→256, s2, 40→20) =====
    print("  Phase 5: L7 ...", end="", flush=True)

    _t = time.perf_counter()
    op5.write_buffer("input", p4_tiled)
    p5_total_output = 256 * 20 * 20
    op5.write_buffer("output", np.zeros(p5_total_output, dtype=np.int8))
    t_buffer_io += time.perf_counter() - _t

    t0 = time.perf_counter()
    op5.run_runlist()
    t1 = time.perf_counter()
    t_npu += t1 - t0
    print(f" {1000 * (t1 - t0):.0f}ms")

    _t = time.perf_counter()
    p5_tiled = op5.read_buffer("output", (p5_total_output,), dtype=np.int8).copy()
    t_buffer_io += time.perf_counter() - _t

    del ctx

    timing = {
        "weight_pack": t_weight_pack,
        "npu": t_npu,
        "cpu_ops": 0.0,
        "buffer_io": t_buffer_io,
    }
    # Return tiled buffers: p3 [64,80,80], p4 [128,40,40], p5 [256,20,20]
    return p3_tiled, p4_tiled, p5_tiled, timing


def run_l8_l9_dataflow(l7_out_tiled, int8_weights, shifts, act_scales):
    """Run L8 C2f + SPPF L9 using a shared AIEContext.

    Args:
        l7_out_tiled: Flat int8 array in tiled [H, C/8, W, 8] format — L7 CBS output.
        int8_weights: Dict of quantized weight tensors.
        shifts: Dict of per-layer shift values.
        act_scales: Dict of per-layer activation scales.

    Returns:
        (l8_out_tiled, p5_tiled): Tiled int8 buffers for L8 and P5 outputs.
    """

    def get_shift(name):
        s = shifts[name]
        if isinstance(s, tuple):
            return s
        return (s, 7)

    # --- Register both operators on shared context ---
    ctx = AIEContext()

    cv1_s1, cv1_s2 = get_shift("l8.cv1")
    bn_cv1_s1, bn_cv1_s2 = get_shift("l8.bn0.cv1")
    bn_cv2_s1, bn_cv2_s2 = get_shift("l8.bn0.cv2")
    l8_cv2_s1, l8_cv2_s2 = get_shift("l8.cv2")

    op_l8 = AIEDataflowC2fL8(
        height=20,
        width=20,
        cv1_s1=cv1_s1,
        cv1_s2=cv1_s2,
        bn_cv1_s1=bn_cv1_s1,
        bn_cv1_s2=bn_cv1_s2,
        bn_cv2_s1=bn_cv2_s1,
        bn_cv2_s2=bn_cv2_s2,
        cv2_s1=l8_cv2_s1,
        cv2_s2=l8_cv2_s2,
        context=ctx,
    )

    l9_cv1_s1, l9_cv1_s2 = get_shift("l9.cv1")
    l9_cv2_s1, l9_cv2_s2 = get_shift("l9.cv2")

    op_l9 = AIEDataflowSPPFL9(
        height=20,
        width=20,
        cv1_s1=l9_cv1_s1,
        cv1_s2=l9_cv1_s2,
        cv2_s1=l9_cv2_s1,
        cv2_s2=l9_cv2_s2,
        context=ctx,
    )

    ctx.compile_all()
    ctx.prepare_runtime()

    # Timing accumulators
    t_weight_pack = 0.0
    t_npu = 0.0
    t_buffer_io = 0.0

    # ===== Pre-pack ALL weights before any phase runs =====

    cv2_oc = 256
    h, w = 20, 20

    _t = time.perf_counter()

    # L8 weights
    w_cv1, ws_cv1_l8, b_cv1 = lookup_weight(int8_weights, "l8.cv1")
    w_bn0cv1, ws_bn0cv1_l8, b_bn0cv1 = lookup_weight(int8_weights, "l8.bn0.cv1")
    w_bn0cv2, ws_bn0cv2_l8, b_bn0cv2 = lookup_weight(int8_weights, "l8.bn0.cv2")
    w_cv2, ws_cv2_l8, b_cv2 = lookup_weight(int8_weights, "l8.cv2")

    l8_in_scale = act_scales.get("l7", 1.0)
    l8_cv1_out = 256.0 / float(cv1_s2) if cv1_s2 > 0 else 1.0
    l8_bn1_out = 256.0 / float(bn_cv1_s2) if bn_cv1_s2 > 0 else 1.0

    b_cv1_i32 = _prescale_bias(b_cv1, ws_cv1_l8, l8_in_scale)
    cv1_oc_chunk = op_l8._cv1_oc_chunk
    cv1_n_oc = op_l8._cv1_n_oc
    cv1_chunks = []
    for g in range(cv1_n_oc):
        ws = w_cv1[g * cv1_oc_chunk : (g + 1) * cv1_oc_chunk]
        bs = b_cv1_i32[g * cv1_oc_chunk : (g + 1) * cv1_oc_chunk]
        cv1_chunks.append(np.concatenate([weights_to_tiled_int8(ws), bs.view(np.int8)]))

    bn_oc_chunk = op_l8._bn_oc_chunk
    bn_n_oc = op_l8._bn_n_oc

    def _pack_k3_oc_i32(wt, b_int32, oc_c, n):
        chunks = []
        for g in range(n):
            ws = wt[g * oc_c : (g + 1) * oc_c]
            bs = b_int32[g * oc_c : (g + 1) * oc_c]
            chunks.append(
                np.concatenate([weights_to_tiled_int8_k3(ws), bs.view(np.int8)])
            )
        return np.concatenate(chunks)

    b_bn0cv1_i32 = _prescale_bias(b_bn0cv1, ws_bn0cv1_l8, l8_cv1_out)
    b_bn0cv2_i32 = _prescale_bias(b_bn0cv2, ws_bn0cv2_l8, l8_bn1_out)
    packed_bn0cv1 = _pack_k3_oc_i32(w_bn0cv1, b_bn0cv1_i32, bn_oc_chunk, bn_n_oc)
    packed_bn0cv2 = _pack_k3_oc_i32(w_bn0cv2, b_bn0cv2_i32, bn_oc_chunk, bn_n_oc)

    b_cv2_i32 = _prescale_bias(b_cv2, ws_cv2_l8, l8_cv1_out)
    cv2_oc_chunk = op_l8._cv2_oc_chunk
    cv2_n_oc = op_l8._cv2_n_oc
    cv2_chunks = []
    for g in range(cv2_n_oc):
        ws = w_cv2[g * cv2_oc_chunk : (g + 1) * cv2_oc_chunk]
        bs = b_cv2_i32[g * cv2_oc_chunk : (g + 1) * cv2_oc_chunk]
        cv2_chunks.append(np.concatenate([weights_to_tiled_int8(ws), bs.view(np.int8)]))

    packed_weights = np.concatenate(
        cv1_chunks + [packed_bn0cv1, packed_bn0cv2] + cv2_chunks
    )

    t_weight_pack += time.perf_counter() - _t

    _t = time.perf_counter()
    op_l8.write_buffer("weights", packed_weights)
    t_buffer_io += time.perf_counter() - _t

    _t = time.perf_counter()

    # L9 weights
    w_cv1_l9, ws_cv1_l9, b_cv1_l9 = lookup_weight(int8_weights, "l9.cv1")
    w_cv2_l9, ws_cv2_l9, b_cv2_l9 = lookup_weight(int8_weights, "l9.cv2")

    l9_in_scale = 256.0 / float(l8_cv2_s2) if l8_cv2_s2 > 0 else 1.0
    l9_cv1_out = 256.0 / float(l9_cv1_s2) if l9_cv1_s2 > 0 else 1.0

    b_cv1_l9_i32 = _prescale_bias(b_cv1_l9, ws_cv1_l9, l9_in_scale)
    packed_cv1 = np.concatenate(
        [weights_to_tiled_int8(w_cv1_l9), b_cv1_l9_i32.view(np.int8)]
    )

    b_cv2_l9_i32 = _prescale_bias(b_cv2_l9, ws_cv2_l9, l9_cv1_out)
    l9_cv2_oc_chunk = op_l9._cv2_oc_chunk
    l9_cv2_n_oc = op_l9._cv2_n_oc
    l9_cv2_chunks = []
    for g in range(l9_cv2_n_oc):
        ws = w_cv2_l9[g * l9_cv2_oc_chunk : (g + 1) * l9_cv2_oc_chunk]
        bs = b_cv2_l9_i32[g * l9_cv2_oc_chunk : (g + 1) * l9_cv2_oc_chunk]
        l9_cv2_chunks.append(
            np.concatenate([weights_to_tiled_int8(ws), bs.view(np.int8)])
        )
    packed_cv2 = np.concatenate(l9_cv2_chunks)

    packed_weights_l9 = np.concatenate([packed_cv1, packed_cv2])

    t_weight_pack += time.perf_counter() - _t

    _t = time.perf_counter()
    op_l9.write_buffer("weights", packed_weights_l9)
    t_buffer_io += time.perf_counter() - _t

    # ===== L8 C2f =====
    print("  L8 C2f ...", end="", flush=True)

    _t = time.perf_counter()
    op_l8.write_buffer("input", l7_out_tiled)
    total_output = cv2_oc * h * w
    output_buf_size = op_l8.buffers["output"]
    op_l8.write_buffer("output", np.zeros(output_buf_size, dtype=np.int8))
    t_buffer_io += time.perf_counter() - _t

    t0 = time.perf_counter()
    op_l8.run_runlist()
    t1 = time.perf_counter()
    t_npu += t1 - t0
    print(f" {1000 * (t1 - t0):.0f}ms")

    _t = time.perf_counter()
    out_flat = op_l8.read_buffer("output", (output_buf_size,), dtype=np.int8)
    l8_out_tiled = out_flat[:total_output].copy()
    t_buffer_io += time.perf_counter() - _t

    # ===== SPPF L9 =====
    print("  SPPF L9 ...", end="", flush=True)

    _t = time.perf_counter()
    op_l9.write_buffer("input", l8_out_tiled)
    output_buf_size_l9 = op_l9.buffers["output"]
    op_l9.write_buffer("output", np.full(output_buf_size_l9, -128, dtype=np.int8))
    t_buffer_io += time.perf_counter() - _t

    t0 = time.perf_counter()
    op_l9.run_runlist()
    t1 = time.perf_counter()
    t_npu += t1 - t0
    print(f" {1000 * (t1 - t0):.0f}ms")

    _t = time.perf_counter()
    l9_cv2_oc = 256
    l9_total_output = l9_cv2_oc * 20 * 20
    out_flat_l9 = op_l9.read_buffer("output", (output_buf_size_l9,), dtype=np.int8)
    p5_tiled = out_flat_l9[:l9_total_output].copy()
    t_buffer_io += time.perf_counter() - _t

    del ctx

    timing = {
        "weight_pack": t_weight_pack,
        "npu": t_npu,
        "cpu_ops": 0.0,
        "buffer_io": t_buffer_io,
    }
    return l8_out_tiled, p5_tiled, timing


def run_neck_dataflow(p3_tiled, p4_tiled, p5_tiled, int8_weights, shifts, act_scales):
    """Run neck (L12+L15, L16+L18, L19+L21) using 3 dataflow PDIs.

    Args:
        p3_tiled: Flat int8 array in tiled format — P3 [64, 80, 80].
        p4_tiled: Flat int8 array in tiled format — P4 [128, 40, 40].
        p5_tiled: Flat int8 array in tiled format — P5 [256, 20, 20].
        int8_weights: Dict of quantized weight tensors.
        shifts: Dict of per-layer shift values (tuples for fused layers).
        act_scales: Dict of per-layer activation scales.

    Returns:
        (det_p3_tiled, det_p4_tiled, det_p5_tiled) — detect head inputs in tiled format.
    """
    from iron.operators.conv2d_int8.dataflow_design import (
        _compute_oc_streaming_params,
    )

    def get_shift(name):
        s = shifts[name]
        if isinstance(s, tuple):
            return s
        return (s, 7)

    # Timing accumulators
    t_weight_pack = 0.0
    t_npu = 0.0
    t_cpu_ops = 0.0
    t_buffer_io = 0.0

    # ===== Register all 3 neck operators on shared context =====
    ctx = AIEContext()

    l12_cv1_s1, l12_cv1_s2 = get_shift("l12.cv1")
    l12_bn_cv1_s1, l12_bn_cv1_s2 = get_shift("l12.bn0.cv1")
    l12_bn_cv2_s1, l12_bn_cv2_s2 = get_shift("l12.bn0.cv2")
    l12_cv2_s1, l12_cv2_s2 = get_shift("l12.cv2")
    l15_cv1_s1, l15_cv1_s2 = get_shift("l15.cv1")
    l15_bn_cv1_s1, l15_bn_cv1_s2 = get_shift("l15.bn0.cv1")
    l15_bn_cv2_s1, l15_bn_cv2_s2 = get_shift("l15.bn0.cv2")
    l15_cv2_s1, l15_cv2_s2 = get_shift("l15.cv2")

    op_n1 = AIEDataflowL12L15(
        l12_h=40,
        l12_w=40,
        s1=l12_cv1_s1,
        s2=l12_cv1_s2,
        l12_cv1_s1=l12_cv1_s1,
        l12_cv1_s2=l12_cv1_s2,
        l12_bn_cv1_s1=l12_bn_cv1_s1,
        l12_bn_cv1_s2=l12_bn_cv1_s2,
        l12_bn_cv2_s1=l12_bn_cv2_s1,
        l12_bn_cv2_s2=l12_bn_cv2_s2,
        l12_cv2_s1=l12_cv2_s1,
        l12_cv2_s2=l12_cv2_s2,
        l15_cv1_s1=l15_cv1_s1,
        l15_cv1_s2=l15_cv1_s2,
        l15_bn_cv1_s1=l15_bn_cv1_s1,
        l15_bn_cv1_s2=l15_bn_cv1_s2,
        l15_bn_cv2_s1=l15_bn_cv2_s1,
        l15_bn_cv2_s2=l15_bn_cv2_s2,
        l15_cv2_s1=l15_cv2_s1,
        l15_cv2_s2=l15_cv2_s2,
        context=ctx,
    )

    l16_s1, l16_s2 = get_shift("l16")
    l18_cv1_s1, l18_cv1_s2 = get_shift("l18.cv1")
    l18_bn_cv1_s1, l18_bn_cv1_s2 = get_shift("l18.bn0.cv1")
    l18_bn_cv2_s1, l18_bn_cv2_s2 = get_shift("l18.bn0.cv2")
    l18_cv2_s1, l18_cv2_s2 = get_shift("l18.cv2")

    op_n2 = AIEDataflowL16L18(
        l16_h=80,
        l16_w=80,
        s1=l16_s1,
        s2=l16_s2,
        l16_s1=l16_s1,
        l16_s2=l16_s2,
        cv1_s1=l18_cv1_s1,
        cv1_s2=l18_cv1_s2,
        bn_cv1_s1=l18_bn_cv1_s1,
        bn_cv1_s2=l18_bn_cv1_s2,
        bn_cv2_s1=l18_bn_cv2_s1,
        bn_cv2_s2=l18_bn_cv2_s2,
        cv2_s1=l18_cv2_s1,
        cv2_s2=l18_cv2_s2,
        context=ctx,
    )

    l19_s1, l19_s2 = get_shift("l19")
    l21_cv1_s1, l21_cv1_s2 = get_shift("l21.cv1")
    l21_bn_cv1_s1, l21_bn_cv1_s2 = get_shift("l21.bn0.cv1")
    l21_bn_cv2_s1, l21_bn_cv2_s2 = get_shift("l21.bn0.cv2")
    l21_cv2_s1, l21_cv2_s2 = get_shift("l21.cv2")

    op_n3 = AIEDataflowL19L21_2col(
        l19_h=40,
        l19_w=40,
        s1=l19_s1,
        s2=l19_s2,
        l19_s1=l19_s1,
        l19_s2=l19_s2,
        cv1_s1=l21_cv1_s1,
        cv1_s2=l21_cv1_s2,
        bn_cv1_s1=l21_bn_cv1_s1,
        bn_cv1_s2=l21_bn_cv1_s2,
        bn_cv2_s1=l21_bn_cv2_s1,
        bn_cv2_s2=l21_bn_cv2_s2,
        cv2_s1=l21_cv2_s1,
        cv2_s2=l21_cv2_s2,
        context=ctx,
    )

    # Compile and prepare all 3 neck operators at once
    ctx.compile_all()
    ctx.prepare_runtime()

    # ===== Pre-pack ALL weights before any phase runs =====

    _t = time.perf_counter()

    h12, w12 = 40, 40
    h15, w15 = 80, 80
    avail = 65536 - 1040 - 2 * 384 * w12
    cv1c = 128
    for oc in range(128, 0, -8):
        if 128 % oc != 0:
            continue
        if oc * 384 + oc * 4 + 2 * oc * w12 <= avail:
            cv1c = oc
            break
    cv1n = 128 // cv1c

    # PDI 1 weights (L12+L15)
    w12c1, ws12c1, b12c1 = lookup_weight(int8_weights, "l12.cv1")
    w12b1, ws12b1, b12b1 = lookup_weight(int8_weights, "l12.bn0.cv1")
    w12b2, ws12b2, b12b2 = lookup_weight(int8_weights, "l12.bn0.cv2")
    w12c2, ws12c2, b12c2 = lookup_weight(int8_weights, "l12.cv2")
    w15c1, ws15c1, b15c1 = lookup_weight(int8_weights, "l15.cv1")
    w15b1, ws15b1, b15b1 = lookup_weight(int8_weights, "l15.bn0.cv1")
    w15b2, ws15b2, b15b2 = lookup_weight(int8_weights, "l15.bn0.cv2")
    w15c2, ws15c2, b15c2 = lookup_weight(int8_weights, "l15.cv2")

    l12_in_scale = act_scales.get("l7", 1.0)
    l12_cv1_out = 256.0 / float(l12_cv1_s2) if l12_cv1_s2 > 0 else 1.0
    l12_bn1_out = 256.0 / float(l12_bn_cv1_s2) if l12_bn_cv1_s2 > 0 else 1.0
    l12_bn2_out = 256.0 / float(l12_bn_cv2_s2) if l12_bn_cv2_s2 > 0 else 1.0
    l12_cv2_out = 256.0 / float(l12_cv2_s2) if l12_cv2_s2 > 0 else 1.0
    l15_cv1_out = 256.0 / float(l15_cv1_s2) if l15_cv1_s2 > 0 else 1.0
    l15_bn1_out = 256.0 / float(l15_bn_cv1_s2) if l15_bn_cv1_s2 > 0 else 1.0
    l15_bn2_out = 256.0 / float(l15_bn_cv2_s2) if l15_bn_cv2_s2 > 0 else 1.0

    b12c1_i32 = _prescale_bias(b12c1, ws12c1, l12_in_scale)
    chunks = []
    for g in range(cv1n):
        ws = w12c1[g * cv1c : (g + 1) * cv1c]
        bs = b12c1_i32[g * cv1c : (g + 1) * cv1c]
        chunks.append(np.concatenate([weights_to_tiled_int8(ws), bs.view(np.int8)]))
    pw_n1 = np.concatenate(
        chunks
        + [
            _pack_fused_k3(w12b1, b12b1, ws12b1, l12_cv1_out),
            _pack_fused_k3(w12b2, b12b2, ws12b2, l12_bn1_out),
            _pack_fused_k1(w12c2, b12c2, ws12c2, l12_cv1_out),
            _pack_fused_k1(w15c1, b15c1, ws15c1, l12_cv2_out),
            _pack_fused_k3(w15b1, b15b1, ws15b1, l15_cv1_out),
            _pack_fused_k3(w15b2, b15b2, ws15b2, l15_bn1_out),
            _pack_fused_k1(w15c2, b15c2, ws15c2, l15_cv1_out),
        ]
    )
    t_weight_pack += time.perf_counter() - _t

    _t = time.perf_counter()
    op_n1.write_buffer("weights", pw_n1)
    t_buffer_io += time.perf_counter() - _t

    _t = time.perf_counter()

    # PDI 2 weights (L16+L18)
    l18_h, l18_w = 40, 40
    oc_chunk_l16, n_oc_l16, _ = _compute_oc_streaming_params(64, 64, 80, 2)
    w_l16, ws_l16, b_l16 = lookup_weight(int8_weights, "l16")
    w18c1, ws18c1, b18c1 = lookup_weight(int8_weights, "l18.cv1")
    w18b1, ws18b1, b18b1 = lookup_weight(int8_weights, "l18.bn0.cv1")
    w18b2, ws18b2, b18b2 = lookup_weight(int8_weights, "l18.bn0.cv2")
    w18c2, ws18c2, b18c2 = lookup_weight(int8_weights, "l18.cv2")

    l15_out_scale = 256.0 / float(l15_cv2_s2) if l15_cv2_s2 > 0 else 1.0
    l16_out_scale = 256.0 / float(l16_s2) if l16_s2 > 0 else 1.0
    l18_cv1_out = 256.0 / float(l18_cv1_s2) if l18_cv1_s2 > 0 else 1.0
    l18_bn1_out = 256.0 / float(l18_bn_cv1_s2) if l18_bn_cv1_s2 > 0 else 1.0

    b_l16_i32 = _prescale_bias(b_l16, ws_l16, l15_out_scale)
    l16_chunks = []
    for g in range(n_oc_l16):
        ws = w_l16[g * oc_chunk_l16 : (g + 1) * oc_chunk_l16]
        bs = b_l16_i32[g * oc_chunk_l16 : (g + 1) * oc_chunk_l16]
        l16_chunks.append(
            np.concatenate([weights_to_tiled_int8_k3(ws), bs.view(np.int8)])
        )
    pw_n2 = np.concatenate(
        l16_chunks
        + [
            _pack_fused_k1(w18c1, b18c1, ws18c1, l16_out_scale),
            _pack_fused_k3(w18b1, b18b1, ws18b1, l18_cv1_out),
            _pack_fused_k3(w18b2, b18b2, ws18b2, l18_bn1_out),
            _pack_fused_k1(w18c2, b18c2, ws18c2, l18_cv1_out),
        ]
    )
    t_weight_pack += time.perf_counter() - _t

    _t = time.perf_counter()
    op_n2.write_buffer("weights", pw_n2)
    t_buffer_io += time.perf_counter() - _t

    _t = time.perf_counter()

    # PDI 3 weights (L19+L21)
    l21_h, l21_w = 20, 20
    l19_oc_chunk, l19_n_oc, _ = _compute_oc_streaming_params(128, 128, 40, 2)
    bn_oc_chunk, bn_n_oc, _ = _compute_oc_streaming_params(128, 128, l21_w, 1)

    w_l19, ws_l19, b_l19 = lookup_weight(int8_weights, "l19")
    w21c1, ws21c1, b21c1 = lookup_weight(int8_weights, "l21.cv1")
    w21b1, ws21b1, b21b1 = lookup_weight(int8_weights, "l21.bn0.cv1")
    w21b2, ws21b2, b21b2 = lookup_weight(int8_weights, "l21.bn0.cv2")
    w21c2, ws21c2, b21c2 = lookup_weight(int8_weights, "l21.cv2")

    l18_cv2_out = 256.0 / float(l18_cv2_s2) if l18_cv2_s2 > 0 else 1.0
    l19_out_scale = 256.0 / float(l19_s2) if l19_s2 > 0 else 1.0
    l21_cv1_out = 256.0 / float(l21_cv1_s2) if l21_cv1_s2 > 0 else 1.0
    l21_bn1_out = 256.0 / float(l21_bn_cv1_s2) if l21_bn_cv1_s2 > 0 else 1.0

    b_l19_i32 = _prescale_bias(b_l19, ws_l19, l18_cv2_out)
    l19_chunks = []
    for g in range(l19_n_oc):
        ws = w_l19[g * l19_oc_chunk : (g + 1) * l19_oc_chunk]
        bs = b_l19_i32[g * l19_oc_chunk : (g + 1) * l19_oc_chunk]
        l19_chunks.append(
            np.concatenate([weights_to_tiled_int8_k3(ws), bs.view(np.int8)])
        )

    b21c1_i32 = _prescale_bias(b21c1, ws21c1, l19_out_scale)
    cv1_oc_chunk_l21 = 64
    cv1_n_oc_l21 = 4
    cv1_chunks = []
    for g in range(cv1_n_oc_l21):
        ws = w21c1[g * cv1_oc_chunk_l21 : (g + 1) * cv1_oc_chunk_l21]
        bs = b21c1_i32[g * cv1_oc_chunk_l21 : (g + 1) * cv1_oc_chunk_l21]
        cv1_chunks.append(np.concatenate([weights_to_tiled_int8(ws), bs.view(np.int8)]))

    def _pack_k3_oc_scaled(wt, b_int32, oc_c, n):
        c = []
        for g in range(n):
            ws = wt[g * oc_c : (g + 1) * oc_c]
            bs = b_int32[g * oc_c : (g + 1) * oc_c]
            c.append(np.concatenate([weights_to_tiled_int8_k3(ws), bs.view(np.int8)]))
        return np.concatenate(c)

    b21b1_i32 = _prescale_bias(b21b1, ws21b1, l21_cv1_out)
    b21b2_i32 = _prescale_bias(b21b2, ws21b2, l21_bn1_out)
    packed_bn0cv1 = _pack_k3_oc_scaled(w21b1, b21b1_i32, bn_oc_chunk, bn_n_oc)
    packed_bn0cv2 = _pack_k3_oc_scaled(w21b2, b21b2_i32, bn_oc_chunk, bn_n_oc)

    b21c2_i32 = _prescale_bias(b21c2, ws21c2, l21_cv1_out)
    cv2_chunks = []
    for g in range(4):
        ws = w21c2[g * 64 : (g + 1) * 64]
        bs = b21c2_i32[g * 64 : (g + 1) * 64]
        cv2_chunks.append(np.concatenate([weights_to_tiled_int8(ws), bs.view(np.int8)]))

    pw_n3 = np.concatenate(
        l19_chunks + cv1_chunks + [packed_bn0cv1, packed_bn0cv2] + cv2_chunks
    )
    t_weight_pack += time.perf_counter() - _t

    _t = time.perf_counter()
    op_n3.write_buffer("weights", pw_n3)
    t_buffer_io += time.perf_counter() - _t

    # ===== PDI 1: L12+L15 (P5+P4 → 64ch 80×80) =====
    print("  Neck PDI 1: L12+L15 ...", end="", flush=True)

    oT_n1 = op_n1.buffers["output"]
    s0 = 64 * h15 * w15
    s1_ = 192 * h12 * w12
    s2_ = 128 * h12 * w12
    s3_ = 192 * h15 * w15
    o3 = s0 + s1_ + s2_
    o4 = o3 + s3_

    _t = time.perf_counter()
    o_buf_n1 = np.zeros(oT_n1, dtype=np.int8)
    # Pre-fill P3 into L15_concat[128:192ch per row]
    for row in range(h15):
        src = row * 64 * w15
        dst = o3 + row * 192 * w15 + 128 * w15
        o_buf_n1[dst : dst + 64 * w15] = p3_tiled[src : src + 64 * w15]
    # Pre-fill P4 into o4[256ch offset per row, stride 384*W]
    for row in range(h12):
        src = row * 128 * w12
        dst = o4 + row * 384 * w12 + 256 * w12
        o_buf_n1[dst : dst + 128 * w12] = p4_tiled[src : src + 128 * w12]
    t_cpu_ops += time.perf_counter() - _t

    _t = time.perf_counter()
    op_n1.write_buffer("input", np.concatenate([p5_tiled, p4_tiled]))
    op_n1.write_buffer("output", o_buf_n1)
    t_buffer_io += time.perf_counter() - _t

    t0 = time.perf_counter()
    op_n1.run_runlist()
    t1 = time.perf_counter()
    t_npu += t1 - t0
    print(f" {1000 * (t1 - t0):.0f}ms")

    _t = time.perf_counter()
    out_n1 = op_n1.read_buffer("output", (oT_n1,), dtype=np.int8)
    det_p3_tiled = out_n1[:s0].copy()
    l12_out_offset = s0 + s1_
    l12_out_tiled = out_n1[l12_out_offset : l12_out_offset + s2_].copy()
    t_buffer_io += time.perf_counter() - _t

    # ===== PDI 2: L16+L18 (64ch 80×80 → 128ch 40×40) =====
    print("  Neck PDI 2: L16+L18 ...", end="", flush=True)

    oT_n2 = op_n2.buffers["output"]
    l18_output_size = 128 * l18_h * l18_w
    concat_offset_n2 = l18_output_size

    _t = time.perf_counter()
    o_buf_n2 = np.zeros(oT_n2, dtype=np.int8)
    for row in range(l18_h):
        src_start = row * 128 * l18_w
        dst_start = concat_offset_n2 + row * 192 * l18_w + 64 * l18_w
        o_buf_n2[dst_start : dst_start + 128 * l18_w] = l12_out_tiled[
            src_start : src_start + 128 * l18_w
        ]
    t_cpu_ops += time.perf_counter() - _t

    _t = time.perf_counter()
    op_n2.write_buffer("input", det_p3_tiled)
    op_n2.write_buffer("output", o_buf_n2)
    t_buffer_io += time.perf_counter() - _t

    t0 = time.perf_counter()
    op_n2.run_runlist()
    t1 = time.perf_counter()
    t_npu += t1 - t0
    print(f" {1000 * (t1 - t0):.0f}ms")

    _t = time.perf_counter()
    out_n2 = op_n2.read_buffer("output", (oT_n2,), dtype=np.int8)
    det_p4_tiled = out_n2[:l18_output_size].copy()
    t_buffer_io += time.perf_counter() - _t

    # ===== PDI 3: L19+L21 (128ch 40×40 → 256ch 20×20) =====
    print("  Neck PDI 3: L19+L21 ...", end="", flush=True)

    oT_n3 = op_n3.buffers["output"]
    l21_output_size = 256 * l21_h * l21_w
    concat_offset_n3 = l21_output_size

    _t = time.perf_counter()
    o_buf_n3 = np.zeros(oT_n3, dtype=np.int8)
    for row in range(l21_h):
        src_start = row * 256 * l21_w
        dst_start = concat_offset_n3 + row * 384 * l21_w + 128 * l21_w
        o_buf_n3[dst_start : dst_start + 256 * l21_w] = p5_tiled[
            src_start : src_start + 256 * l21_w
        ]
    t_cpu_ops += time.perf_counter() - _t

    _t = time.perf_counter()
    op_n3.write_buffer("input", det_p4_tiled)
    op_n3.write_buffer("output", o_buf_n3)
    t_buffer_io += time.perf_counter() - _t

    t0 = time.perf_counter()
    op_n3.run_runlist()
    t1 = time.perf_counter()
    t_npu += t1 - t0
    print(f" {1000 * (t1 - t0):.0f}ms")

    _t = time.perf_counter()
    out_n3 = op_n3.read_buffer("output", (oT_n3,), dtype=np.int8)
    det_p5_tiled = out_n3[:l21_output_size].copy()
    t_buffer_io += time.perf_counter() - _t

    del ctx

    timing = {
        "weight_pack": t_weight_pack,
        "npu": t_npu,
        "cpu_ops": t_cpu_ops,
        "buffer_io": t_buffer_io,
    }
    return det_p3_tiled, det_p4_tiled, det_p5_tiled, timing


def run_detect_dataflow(
    det_p3_tiled, det_p4_tiled, det_p5_tiled, int8_weights, shifts, act_scales
):
    """Run detection head using 3 dataflow PDIs (one per scale).

    Args:
        det_p3_tiled: Flat int8 array in tiled format — detect input for P3 [64, 80, 80].
        det_p4_tiled: Flat int8 array in tiled format — detect input for P4 [128, 40, 40].
        det_p5_tiled: Flat int8 array in tiled format — detect input for P5 [256, 20, 20].
        int8_weights: Dict of quantized weight tensors.
        shifts: Dict of per-layer shift values.
        act_scales: Dict of per-layer activation scales.

    Returns:
        Dict {"reg": [reg_p3, reg_p4, reg_p5], "cls": [cls_p3, cls_p4, cls_p5]}.
        reg tensors: int8 NCHW, cls tensors: int8 NCHW.
    """
    from iron.operators.conv2d_int8.dataflow_design import (
        _compute_oc_streaming_params,
        _compute_oc_streaming_params_k1,
    )

    def get_shift(name):
        s = shifts[name]
        if isinstance(s, tuple):
            return s
        return (s, 7)

    scales = [
        ("p3", det_p3_tiled, 64, 80, 80),
        ("p4", det_p4_tiled, 128, 40, 40),
        ("p5", det_p5_tiled, 256, 20, 20),
    ]

    # --- Register all 3 detect operators on shared context ---
    ctx = AIEContext()
    ops = []
    shift_data = []

    for scale_name, det_input, ic, h, w in scales:
        rcv1_s1, rcv1_s2 = get_shift(f"det.reg_{scale_name}.cv1")
        rcv2_s1, rcv2_s2 = get_shift(f"det.reg_{scale_name}.cv2")
        ccv1_s1, ccv1_s2 = get_shift(f"det.cls_{scale_name}.cv1")
        ccv2_s1, ccv2_s2 = get_shift(f"det.cls_{scale_name}.cv2")

        _, ws_rcv3, _ = lookup_weight(int8_weights, f"det.reg_{scale_name}.cv3")
        rcv3_in_scale = 256.0 / float(rcv2_s2) if rcv2_s2 > 0 else 1.0
        rcv3_out_scale = act_scales.get(f"det.reg_{scale_name}.cv3", 1.0)
        rcv3_s1, rcv3_s2 = compute_fused_shifts(ws_rcv3, rcv3_in_scale, rcv3_out_scale)

        _, ws_ccv3, _ = lookup_weight(int8_weights, f"det.cls_{scale_name}.cv3")
        ccv3_in_scale = 256.0 / float(ccv2_s2) if ccv2_s2 > 0 else 1.0
        ccv3_out_scale = act_scales.get(f"det.cls_{scale_name}.cv3", 1.0)
        ccv3_s1, ccv3_s2 = compute_fused_shifts(ws_ccv3, ccv3_in_scale, ccv3_out_scale)

        # Use 4-column design for P3 (80×80) — 2x speedup
        OpClass = (
            AIEDataflowDetectScale4Col if scale_name == "p3" else AIEDataflowDetectScale
        )
        op_d = OpClass(
            height=h,
            width=w,
            in_channels=ic,
            reg_cv1_s1=rcv1_s1,
            reg_cv1_s2=rcv1_s2,
            reg_cv2_s1=rcv2_s1,
            reg_cv2_s2=rcv2_s2,
            reg_cv3_s1=rcv3_s1,
            reg_cv3_s2=rcv3_s2,
            cls_cv1_s1=ccv1_s1,
            cls_cv1_s2=ccv1_s2,
            cls_cv2_s1=ccv2_s1,
            cls_cv2_s2=ccv2_s2,
            cls_cv3_s1=ccv3_s1,
            cls_cv3_s2=ccv3_s2,
            context=ctx,
        )
        ops.append(op_d)
        shift_data.append(
            (rcv1_s1, rcv1_s2, rcv2_s1, rcv2_s2, ccv1_s1, ccv1_s2, ccv2_s1, ccv2_s2)
        )

    # Compile and prepare all 3 detect operators at once
    ctx.compile_all()
    ctx.prepare_runtime()

    # Timing accumulators
    t_weight_pack = 0.0
    t_npu = 0.0
    t_buffer_io = 0.0

    # ===== Pre-pack ALL weights before any phase runs =====
    _t = time.perf_counter()

    def _pack_oc(wt, b_int32, oc_c, n, k3=True):
        """Pack OC-streamed weight chunks with pre-scaled int32 bias."""
        pack_fn = weights_to_tiled_int8_k3 if k3 else weights_to_tiled_int8
        chunks = []
        for g in range(n):
            ws = wt[g * oc_c : (g + 1) * oc_c]
            bs = b_int32[g * oc_c : (g + 1) * oc_c]
            chunks.append(np.concatenate([pack_fn(ws), bs.view(np.int8)]))
        return np.concatenate(chunks)

    packed_weights_all = []
    for i, (scale_name, det_input, ic, h, w) in enumerate(scales):
        rcv1_s1, rcv1_s2, rcv2_s1, rcv2_s2, ccv1_s1, ccv1_s2, ccv2_s1, ccv2_s2 = (
            shift_data[i]
        )

        reg_mid = 64
        reg_out = 64
        cls_mid = 80
        cls_out = 80

        rcv1_oc, rcv1_n, _ = _compute_oc_streaming_params(ic, reg_mid, w, 1)
        rcv2_oc, rcv2_n, _ = _compute_oc_streaming_params(reg_mid, reg_mid, w, 1)
        rcv3_oc, rcv3_n = _compute_oc_streaming_params_k1(reg_mid, reg_out, w)
        ccv1_oc, ccv1_n, _ = _compute_oc_streaming_params(ic, cls_mid, w, 1)
        ccv2_oc, ccv2_n, _ = _compute_oc_streaming_params(cls_mid, cls_mid, w, 1)
        ccv3_oc, ccv3_n = _compute_oc_streaming_params_k1(cls_mid, cls_out, w)

        det_in_scale = act_scales.get(
            (
                "l15.cv2"
                if scale_name == "p3"
                else "l18.cv2" if scale_name == "p4" else "l21.cv2"
            ),
            1.0,
        )

        w_rcv1, ws_rcv1, b_rcv1 = lookup_weight(
            int8_weights, f"det.reg_{scale_name}.cv1"
        )
        w_rcv2, ws_rcv2, b_rcv2 = lookup_weight(
            int8_weights, f"det.reg_{scale_name}.cv2"
        )
        w_rcv3, ws_rcv3, b_rcv3 = lookup_weight(
            int8_weights, f"det.reg_{scale_name}.cv3"
        )
        w_ccv1, ws_ccv1, b_ccv1 = lookup_weight(
            int8_weights, f"det.cls_{scale_name}.cv1"
        )
        w_ccv2, ws_ccv2, b_ccv2 = lookup_weight(
            int8_weights, f"det.cls_{scale_name}.cv2"
        )
        w_ccv3, ws_ccv3, b_ccv3 = lookup_weight(
            int8_weights, f"det.cls_{scale_name}.cv3"
        )

        b_rcv1_i32 = _prescale_bias(b_rcv1, ws_rcv1, det_in_scale)
        rcv1_out_scale = 256.0 / float(rcv1_s2) if rcv1_s2 > 0 else 1.0
        b_rcv2_i32 = _prescale_bias(b_rcv2, ws_rcv2, rcv1_out_scale)
        b_rcv3_i32 = np.round(b_rcv3.numpy()).astype(np.int32)

        b_ccv1_i32 = _prescale_bias(b_ccv1, ws_ccv1, det_in_scale)
        ccv1_out_scale = 256.0 / float(ccv1_s2) if ccv1_s2 > 0 else 1.0
        b_ccv2_i32 = _prescale_bias(b_ccv2, ws_ccv2, ccv1_out_scale)
        b_ccv3_i32 = np.round(b_ccv3.numpy()).astype(np.int32)

        if scale_name == "p3":
            # 4-col layout: lo/hi splits for cv1/cv2, full for cv3
            reg_oc_per_col = reg_mid // 2  # 32
            cls_oc_per_col = cls_mid // 2  # 40
            packed_weights = np.concatenate(
                [
                    _pack_oc(
                        w_rcv1[:reg_oc_per_col],
                        b_rcv1_i32[:reg_oc_per_col],
                        reg_oc_per_col,
                        1,
                        k3=True,
                    ),
                    _pack_oc(
                        w_rcv1[reg_oc_per_col:],
                        b_rcv1_i32[reg_oc_per_col:],
                        reg_oc_per_col,
                        1,
                        k3=True,
                    ),
                    _pack_oc(
                        w_rcv2[:reg_oc_per_col],
                        b_rcv2_i32[:reg_oc_per_col],
                        reg_oc_per_col,
                        1,
                        k3=True,
                    ),
                    _pack_oc(
                        w_rcv2[reg_oc_per_col:],
                        b_rcv2_i32[reg_oc_per_col:],
                        reg_oc_per_col,
                        1,
                        k3=True,
                    ),
                    _pack_oc(w_rcv3, b_rcv3_i32, rcv3_oc, rcv3_n, k3=False),
                    _pack_oc(
                        w_ccv1[:cls_oc_per_col],
                        b_ccv1_i32[:cls_oc_per_col],
                        cls_oc_per_col,
                        1,
                        k3=True,
                    ),
                    _pack_oc(
                        w_ccv1[cls_oc_per_col:],
                        b_ccv1_i32[cls_oc_per_col:],
                        cls_oc_per_col,
                        1,
                        k3=True,
                    ),
                    _pack_oc(
                        w_ccv2[:cls_oc_per_col],
                        b_ccv2_i32[:cls_oc_per_col],
                        cls_oc_per_col,
                        1,
                        k3=True,
                    ),
                    _pack_oc(
                        w_ccv2[cls_oc_per_col:],
                        b_ccv2_i32[cls_oc_per_col:],
                        cls_oc_per_col,
                        1,
                        k3=True,
                    ),
                    _pack_oc(w_ccv3, b_ccv3_i32, ccv3_oc, ccv3_n, k3=False),
                ]
            )
        else:
            packed_weights = np.concatenate(
                [
                    _pack_oc(w_rcv1, b_rcv1_i32, rcv1_oc, rcv1_n, k3=True),
                    _pack_oc(w_rcv2, b_rcv2_i32, rcv2_oc, rcv2_n, k3=True),
                    _pack_oc(w_rcv3, b_rcv3_i32, rcv3_oc, rcv3_n, k3=False),
                    _pack_oc(w_ccv1, b_ccv1_i32, ccv1_oc, ccv1_n, k3=True),
                    _pack_oc(w_ccv2, b_ccv2_i32, ccv2_oc, ccv2_n, k3=True),
                    _pack_oc(w_ccv3, b_ccv3_i32, ccv3_oc, ccv3_n, k3=False),
                ]
            )
        packed_weights_all.append(packed_weights)

    t_weight_pack += time.perf_counter() - _t

    _t = time.perf_counter()
    for i in range(len(ops)):
        ops[i].write_buffer("weights", packed_weights_all[i])
    t_buffer_io += time.perf_counter() - _t

    # --- Run each scale sequentially ---
    reg_outputs = []
    cls_outputs = []

    for i, (scale_name, det_input, ic, h, w) in enumerate(scales):
        print(f"  Detect {scale_name} ({ic}ch {h}×{w}) ...", end="", flush=True)
        op_d = ops[i]

        reg_out = 64
        cls_out = 80

        _t = time.perf_counter()
        output_buf_size = op_d.buffers["output"]
        op_d.write_buffer("input", det_input)
        op_d.write_buffer("output", np.zeros(output_buf_size, dtype=np.int8))
        t_buffer_io += time.perf_counter() - _t

        t0 = time.perf_counter()
        op_d.run_runlist()
        t1 = time.perf_counter()
        t_npu += t1 - t0
        print(f" {1000 * (t1 - t0):.0f}ms")

        _t = time.perf_counter()
        out_flat = op_d.read_buffer("output", (output_buf_size,), dtype=np.int8)

        reg_size = reg_out * h * w
        cls_size = cls_out * h * w
        reg_tiled = out_flat[:reg_size]
        cls_tiled = out_flat[reg_size : reg_size + cls_size]

        # Convert to NCHW only here — needed for post-processing
        reg_nchw = tiled_to_nchw_int8(reg_tiled, reg_out, h, w)
        cls_nchw = tiled_to_nchw_int8(cls_tiled, cls_out, h, w)
        t_buffer_io += time.perf_counter() - _t

        reg_outputs.append(reg_nchw)
        cls_outputs.append(cls_nchw)

    del ctx
    timing = {
        "weight_pack": t_weight_pack,
        "npu": t_npu,
        "cpu_ops": 0.0,
        "buffer_io": t_buffer_io,
    }
    return {"reg": reg_outputs, "cls": cls_outputs}, timing


def main():
    parser = argparse.ArgumentParser(
        description="YOLOv8n dataflow backbone + sequential neck/detect"
    )
    parser.add_argument("--image", default="test_bus.jpg", help="Path to test image")
    parser.add_argument("--model", default="yolov8n.pt", help="Path to YOLOv8n weights")
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Downloading test image to {image_path}...")
        urllib.request.urlretrieve(
            "https://ultralytics.com/images/bus.jpg", str(image_path)
        )

    print("=" * 70)
    print("YOLOv8n DATAFLOW Backbone + Neck + Detect")
    print("=" * 70)

    # -- Step 1: Load model, quantize, calibrate --
    print("\n[1] Loading model, quantizing weights, calibrating...")
    t0 = time.time()
    runner = Int8YOLOv8nCPU(args.model)
    img_tensor = preprocess_image(image_path, img_size=640)
    runner.calibrate(img_tensor, percentile_fn=get_percentile)
    calib_time = time.time() - t0
    print(f"    Calibration: {calib_time:.1f}s")

    int8_weights = runner.int8_weights
    act_scales = runner.act_scales

    # -- Step 2: Compute per-layer shifts --
    print("\n[2] Computing per-layer shifts...")
    shifts, effective_act_scales = compute_all_shifts(int8_weights, act_scales)
    act_scales = effective_act_scales

    # -- Step 3: Run dataflow backbone (phases 1-5) --
    print(f"\n{'=' * 70}")
    print("Running Dataflow Backbone (Phases 1-5)")
    print(f"{'=' * 70}")

    # Quantize input
    x_pad = F.pad(img_tensor.float(), (0, 0, 0, 0, 0, 5))
    l0_in_scale = act_scales.get("input", 1.0)
    if l0_in_scale == 0:
        l0_in_scale = 1.0
    x_int8 = torch.clamp(torch.round(x_pad / l0_in_scale), -128, 127).to(torch.int8)

    t_backbone = time.time()
    p3_tiled, p4_tiled, l7_tiled, tm_bb = run_backbone_dataflow(
        x_int8, int8_weights, act_scales, shifts
    )
    t_backbone = time.time() - t_backbone
    print(f"\n  Backbone total: {t_backbone:.1f}s")
    print(f"    P3 (L4 out): tiled {len(p3_tiled)} bytes [64, 80, 80]")
    print(f"    P4 (L6 out): tiled {len(p4_tiled)} bytes [128, 40, 40]")
    print(f"    L7 out:      tiled {len(l7_tiled)} bytes [256, 20, 20]")

    # -- Step 4: Dataflow L8 C2f + SPPF L9 (shared context) --
    print(f"\n{'=' * 70}")
    print("Dataflow L8 C2f + SPPF L9 (Phases 6-7)")
    print(f"{'=' * 70}")

    t_l8_l9 = time.time()
    l8_tiled, p5_tiled, tm_l8l9 = run_l8_l9_dataflow(
        l7_tiled, int8_weights, shifts, act_scales
    )
    t_l8_l9 = time.time() - t_l8_l9
    print(f"  L8 output: tiled {len(l8_tiled)} bytes [256, 20, 20]")
    print(f"  P5 output: tiled {len(p5_tiled)} bytes [256, 20, 20]")

    # -- Step 5: Dataflow Neck (3 PDIs) --
    print(f"\n{'=' * 70}")
    print("Dataflow Neck (L12+L15, L16+L18, L19+L21)")
    print(f"{'=' * 70}")

    t_neck = time.time()
    det_p3_tiled, det_p4_tiled, det_p5_tiled, tm_neck = run_neck_dataflow(
        p3_tiled, p4_tiled, p5_tiled, int8_weights, shifts, act_scales
    )
    t_neck = time.time() - t_neck
    print(f"\n  Neck total: {t_neck:.1f}s")
    print(f"    det_p3: tiled {len(det_p3_tiled)} bytes [64, 80, 80]")
    print(f"    det_p4: tiled {len(det_p4_tiled)} bytes [128, 40, 40]")
    print(f"    det_p5: tiled {len(det_p5_tiled)} bytes [256, 20, 20]")

    # -- Step 6: Dataflow Detect (3 PDIs) --
    print(f"\n{'=' * 70}")
    print("Dataflow Detect Head (P3, P4, P5)")
    print(f"{'=' * 70}")

    t_detect = time.time()
    result, tm_det = run_detect_dataflow(
        det_p3_tiled, det_p4_tiled, det_p5_tiled, int8_weights, shifts, act_scales
    )
    t_detect = time.time() - t_detect
    print(f"\n  Detect total: {t_detect:.1f}s")

    # -- Step 7: Post-process --
    print(f"\n{'=' * 70}")
    print("Post-Processing (DFL decode + NMS)")
    print(f"{'=' * 70}")

    pp = YOLOv8nPostProcess(conf_thres=0.25, iou_thres=0.45)
    detections = pp(result["reg"], result["cls"])

    n_boxes = len(detections["boxes"])
    print(f"  Detections (conf>0.25): {n_boxes}")
    if n_boxes > 0:
        for i in range(min(10, n_boxes)):
            box = detections["boxes"][i].tolist()
            score = detections["scores"][i].item()
            label = detections["labels"][i].item()
            name = COCO_NAMES[label] if label < len(COCO_NAMES) else f"class_{label}"
            print(
                f"    {name}: {score:.3f} at "
                f"[{box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f}]"
            )

    # Also try lower threshold
    pp_low = YOLOv8nPostProcess(conf_thres=0.10, iou_thres=0.45)
    dets_low = pp_low(result["reg"], result["cls"])
    n_low = len(dets_low["boxes"])
    print(f"  Detections (conf>0.10): {n_low}")

    # -- Summary --
    print(f"\n{'=' * 70}")
    print("Summary (first run, includes context setup)")
    print(f"{'=' * 70}")
    print(f"  Backbone (dataflow):  {t_backbone:.1f}s")
    print(f"  L8+L9 (dataflow):     {t_l8_l9:.1f}s")
    print(f"  Neck (dataflow):      {t_neck:.1f}s")
    print(f"  Detect (dataflow):    {t_detect:.1f}s")
    t_total = t_backbone + t_l8_l9 + t_neck + t_detect
    print(f"  Total inference:      {t_total:.1f}s")
    print(f"  AIE contexts:         4 (was 13)")
    print(f"  Detections (>0.25):   {n_boxes}")

    # -- Steady-state benchmark: frame in → detections out --
    # Excludes: calibration, shift computation, compilation, weight packing.
    # Includes: input quantize, context setup, buffer I/O, NPU exec, post-process.
    n_warmup = 2
    n_bench = 5
    print(f"\n{'=' * 70}")
    print(f"Steady-State Benchmark ({n_warmup} warmup + {n_bench} timed iterations)")
    print(f"  Timing: frame in (quantize) → detections out (NMS)")
    print(f"  Excludes: calibration, weight quant, shift computation")
    print(f"{'=' * 70}")

    pp_bench = YOLOv8nPostProcess(conf_thres=0.25, iou_thres=0.45)
    latencies = []

    for run_i in range(n_warmup + n_bench):
        t_start = time.perf_counter()

        # --- Frame in: quantize input ---
        x_pad_b = F.pad(img_tensor.float(), (0, 0, 0, 0, 0, 5))
        x_int8_b = torch.clamp(torch.round(x_pad_b / l0_in_scale), -128, 127).to(
            torch.int8
        )

        # --- Backbone (5 phases) ---
        p3_t, p4_t, l7_t, _ = run_backbone_dataflow(
            x_int8_b, int8_weights, act_scales, shifts
        )

        # --- L8 C2f + SPPF L9 ---
        _, p5_t, _ = run_l8_l9_dataflow(l7_t, int8_weights, shifts, act_scales)

        # --- Neck (3 PDIs) ---
        dp3, dp4, dp5, _ = run_neck_dataflow(
            p3_t, p4_t, p5_t, int8_weights, shifts, act_scales
        )

        # --- Detect (3 PDIs) ---
        res, _ = run_detect_dataflow(dp3, dp4, dp5, int8_weights, shifts, act_scales)

        # --- Detections out: post-process ---
        dets = pp_bench(res["reg"], res["cls"])

        t_end = time.perf_counter()
        lat_ms = 1000 * (t_end - t_start)
        n_det = len(dets["boxes"])

        if run_i < n_warmup:
            print(f"  Warmup {run_i + 1}: {lat_ms:.1f} ms  ({n_det} dets)")
        else:
            latencies.append(lat_ms)
            print(f"  Run {run_i - n_warmup + 1}:    {lat_ms:.1f} ms  ({n_det} dets)")

    avg_ms = sum(latencies) / len(latencies)
    min_ms = min(latencies)
    max_ms = max(latencies)
    fps = 1000.0 / avg_ms

    print(f"\n{'=' * 70}")
    print("Results")
    print(f"{'=' * 70}")
    print(f"  Latency (avg):  {avg_ms:.1f} ms")
    print(f"  Latency (min):  {min_ms:.1f} ms")
    print(f"  Latency (max):  {max_ms:.1f} ms")
    print(f"  FPS:            {fps:.2f}")
    print(f"  Detections:     {n_det} (conf>0.25)")


if __name__ == "__main__":
    main()
