#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Run full YOLOv8n model end-to-end on NPU at 640x640.

Uses 2 multi-PDI xclbins with sequential hw_contexts:
  - XCLBIN 1: Backbone+Neck (L0-L21) — 28 unique PDIs, 1 hw_context
  - XCLBIN 2: Detect Head (6 branches) — ~17 unique PDIs, 1 hw_context
  - Post-processing: DFL decode + NMS (CPU)

Each xclbin merges all its operators into a single combined xclbin via
PDI chaining. XRT cache is cleaned between stages to free hw_contexts.
"""

import torch
import torch.nn.functional as F
import time
import gc

from iron.common import AIEContext
from iron.applications.yolov8n.pipeline import YOLOv8nPipeline
from iron.applications.yolov8n.postprocess import YOLOv8nPostProcess
from aie.utils import DefaultNPURuntime


def cleanup_xrt():
    """Release all XRT hw_contexts to avoid driver exhaustion."""
    DefaultNPURuntime._context_cache.clear()
    DefaultNPURuntime._insts_cache.clear()
    gc.collect()


# ── XCLBIN 1: Backbone + Neck ───────────────────────────────────────────────


class BackboneNeckPipeline(YOLOv8nPipeline):
    """Multi-PDI pipeline for backbone (L0-L9) + neck (L10-L21).

    28 unique PDIs in one combined xclbin, 50 layer mappings.
    """

    def _register_all_layers(self):
        H, W = self.img_height, self.img_width
        cols = 0

        # Backbone
        self._register_cbs("bb_l0", 8, 16, 3, 2, H, W, cols)
        h2, w2 = H // 2, W // 2
        self._register_cbs("bb_l1", 16, 32, 3, 2, h2, w2, cols)
        h4, w4 = h2 // 2, w2 // 2
        self._register_c2f("bb_l2", 32, 32, 1, h4, w4, cols)
        self._register_cbs("bb_l3", 32, 64, 3, 2, h4, w4, cols)
        h8, w8 = h4 // 2, w4 // 2
        self._register_c2f("bb_l4", 64, 64, 2, h8, w8, cols)
        self._register_cbs("bb_l5", 64, 128, 3, 2, h8, w8, cols)
        h16, w16 = h8 // 2, w8 // 2
        self._register_c2f("bb_l6", 128, 128, 2, h16, w16, cols)
        self._register_cbs("bb_l7", 128, 256, 3, 2, h16, w16, cols)
        h32, w32 = h16 // 2, w16 // 2
        self._register_c2f("bb_l8", 256, 256, 1, h32, w32, cols)
        self._register_sppf("bb_l9", 256, 256, h32, w32, 5, cols)

        # Neck (FPN up-path)
        self._register_upsample("nk_up1", 256, h32, w32, 2, cols)
        self._register_c2f("nk_l12", 384, 128, 1, h16, w16, cols)
        self._register_upsample("nk_up2", 128, h16, w16, 2, cols)
        self._register_c2f("nk_l15", 192, 64, 1, h8, w8, cols)

        # Neck (PAN down-path)
        self._register_cbs("nk_l16", 64, 64, 3, 2, h8, w8, cols)
        self._register_c2f("nk_l18", 192, 128, 1, h16, w16, cols)
        self._register_cbs("nk_l19", 128, 128, 3, 2, h16, w16, cols)
        self._register_c2f("nk_l21", 384, 256, 1, h32, w32, cols)

    def forward(self, x):
        """Run backbone + neck.

        Args:
            x: Input [1, 3, H, W] in bfloat16.

        Returns:
            (det_p3, det_p4, det_p5) feature maps.
        """
        bb = self._weights["backbone"]
        nk = self._weights["neck"]

        x = F.pad(x, (0, 0, 0, 0, 0, 5))

        # Backbone
        x = self._run_cbs("bb_l0", x, bb["l0"]["weight"], bb["l0"]["bias"])
        print(f"  L0:  {x.shape}")
        x = self._run_cbs("bb_l1", x, bb["l1"]["weight"], bb["l1"]["bias"])
        print(f"  L1:  {x.shape}")
        x = self._run_c2f("bb_l2", x, bb["l2"])
        print(f"  L2:  {x.shape}")
        x = self._run_cbs("bb_l3", x, bb["l3"]["weight"], bb["l3"]["bias"])
        print(f"  L3:  {x.shape}")
        p3 = self._run_c2f("bb_l4", x, bb["l4"])
        print(f"  L4:  {p3.shape}  [P3]")
        x = self._run_cbs("bb_l5", p3, bb["l5"]["weight"], bb["l5"]["bias"])
        print(f"  L5:  {x.shape}")
        p4 = self._run_c2f("bb_l6", x, bb["l6"])
        print(f"  L6:  {p4.shape}  [P4]")
        x = self._run_cbs("bb_l7", p4, bb["l7"]["weight"], bb["l7"]["bias"])
        print(f"  L7:  {x.shape}")
        x = self._run_c2f("bb_l8", x, bb["l8"])
        print(f"  L8:  {x.shape}")
        p5 = self._run_sppf("bb_l9", x, bb["l9"])
        print(f"  L9:  {p5.shape}  [P5]")

        # Neck (FPN up-path)
        x = self._run_upsample("nk_up1", p5)
        print(f"  L10: {x.shape}  (upsample)")
        x = torch.cat([x, p4], dim=1)
        print(f"  L11: {x.shape}  (concat)")
        l12_out = self._run_c2f("nk_l12", x, nk["l12"], shortcut=False)
        print(f"  L12: {l12_out.shape}")
        x = self._run_upsample("nk_up2", l12_out)
        print(f"  L13: {x.shape}  (upsample)")
        x = torch.cat([x, p3], dim=1)
        print(f"  L14: {x.shape}  (concat)")
        det_p3 = self._run_c2f("nk_l15", x, nk["l15"], shortcut=False)
        print(f"  L15: {det_p3.shape}  [det_p3]")

        # Neck (PAN down-path)
        x = self._run_cbs("nk_l16", det_p3, nk["l16"]["weight"], nk["l16"]["bias"])
        print(f"  L16: {x.shape}")
        x = torch.cat([x, l12_out], dim=1)
        print(f"  L17: {x.shape}  (concat)")
        det_p4 = self._run_c2f("nk_l18", x, nk["l18"], shortcut=False)
        print(f"  L18: {det_p4.shape}  [det_p4]")
        x = self._run_cbs("nk_l19", det_p4, nk["l19"]["weight"], nk["l19"]["bias"])
        print(f"  L19: {x.shape}")
        x = torch.cat([x, p5], dim=1)
        print(f"  L20: {x.shape}  (concat)")
        det_p5 = self._run_c2f("nk_l21", x, nk["l21"], shortcut=False)
        print(f"  L21: {det_p5.shape}  [det_p5]")

        return det_p3, det_p4, det_p5


# ── XCLBIN 2: Detect Head ───────────────────────────────────────────────────


class DetectHeadPipeline(YOLOv8nPipeline):
    """Multi-PDI pipeline for detect head (6 branches).

    ~17 unique PDIs in one combined xclbin.
    """

    def _register_all_layers(self):
        H, W = self.img_height, self.img_width
        cols = 0
        h8, w8 = H // 8, W // 8      # 80x80
        h16, w16 = H // 16, W // 16   # 40x40
        h32, w32 = H // 32, W // 32   # 20x20

        c_reg = 4 * self.reg_max  # 64
        c_cls = self.nc            # 80
        c2 = 64                    # reg intermediate
        c3 = max(self.nc, 16)      # cls intermediate (80)

        self._register_detect_branch("det_reg_p3", 64, c2, c_reg, h8, w8, cols)
        self._register_detect_branch("det_cls_p3", 64, c3, c_cls, h8, w8, cols)
        self._register_detect_branch("det_reg_p4", 128, c2, c_reg, h16, w16, cols)
        self._register_detect_branch("det_cls_p4", 128, c3, c_cls, h16, w16, cols)
        self._register_detect_branch("det_reg_p5", 256, c2, c_reg, h32, w32, cols)
        self._register_detect_branch("det_cls_p5", 256, c3, c_cls, h32, w32, cols)

    def forward(self, det_p3, det_p4, det_p5):
        """Run detect head on neck outputs.

        Args:
            det_p3: [1, 64, 80, 80] from neck.
            det_p4: [1, 128, 40, 40] from neck.
            det_p5: [1, 256, 20, 20] from neck.

        Returns:
            dict with 'reg': [reg_p3, reg_p4, reg_p5],
                       'cls': [cls_p3, cls_p4, cls_p5]
        """
        dt = self._weights["detect"]

        reg_p3 = self._run_detect_branch("det_reg_p3", det_p3, dt["reg_p3"])
        print(f"  reg_p3: {reg_p3.shape}")
        cls_p3 = self._run_detect_branch("det_cls_p3", det_p3, dt["cls_p3"])
        print(f"  cls_p3: {cls_p3.shape}")

        reg_p4 = self._run_detect_branch("det_reg_p4", det_p4, dt["reg_p4"])
        print(f"  reg_p4: {reg_p4.shape}")
        cls_p4 = self._run_detect_branch("det_cls_p4", det_p4, dt["cls_p4"])
        print(f"  cls_p4: {cls_p4.shape}")

        reg_p5 = self._run_detect_branch("det_reg_p5", det_p5, dt["reg_p5"])
        print(f"  reg_p5: {reg_p5.shape}")
        cls_p5 = self._run_detect_branch("det_cls_p5", det_p5, dt["cls_p5"])
        print(f"  cls_p5: {cls_p5.shape}")

        return {
            "reg": [reg_p3, reg_p4, reg_p5],
            "cls": [cls_p3, cls_p4, cls_p5],
        }


# ── Weight Generation ────────────────────────────────────────────────────────


def _make_random_cbs_weights(in_ch, out_ch, kernel_size):
    return {
        "weight": torch.randn(out_ch, in_ch, kernel_size, kernel_size, dtype=torch.bfloat16) * 0.01,
        "bias": torch.randn(out_ch, dtype=torch.bfloat16) * 0.01,
    }


def _make_random_bottleneck_weights(channels, n=1):
    return [
        (
            torch.randn(channels, channels, 3, 3, dtype=torch.bfloat16) * 0.01,
            torch.randn(channels, dtype=torch.bfloat16) * 0.01,
            torch.randn(channels, channels, 3, 3, dtype=torch.bfloat16) * 0.01,
            torch.randn(channels, dtype=torch.bfloat16) * 0.01,
        )
        for _ in range(n)
    ]


def _make_random_c2f_weights(c_in, c_out, n_bottlenecks):
    c = c_out // 2
    return {
        "cv1_weight": torch.randn(2 * c, c_in, 1, 1, dtype=torch.bfloat16) * 0.01,
        "cv1_bias": torch.randn(2 * c, dtype=torch.bfloat16) * 0.01,
        "bottlenecks": _make_random_bottleneck_weights(c, n_bottlenecks),
        "cv2_weight": torch.randn(c_out, (2 + n_bottlenecks) * c, 1, 1, dtype=torch.bfloat16) * 0.01,
        "cv2_bias": torch.randn(c_out, dtype=torch.bfloat16) * 0.01,
    }


def _make_random_sppf_weights(c_in, c_out):
    c_ = c_in // 2
    return {
        "cv1_weight": torch.randn(c_, c_in, 1, 1, dtype=torch.bfloat16) * 0.01,
        "cv1_bias": torch.randn(c_, dtype=torch.bfloat16) * 0.01,
        "cv2_weight": torch.randn(c_out, c_ * 4, 1, 1, dtype=torch.bfloat16) * 0.01,
        "cv2_bias": torch.randn(c_out, dtype=torch.bfloat16) * 0.01,
    }


def _make_random_detect_branch_weights(c_in, c_mid, c_out):
    return {
        "cv1_weight": torch.randn(c_mid, c_in, 3, 3, dtype=torch.bfloat16) * 0.01,
        "cv1_bias": torch.randn(c_mid, dtype=torch.bfloat16) * 0.01,
        "cv2_weight": torch.randn(c_mid, c_mid, 3, 3, dtype=torch.bfloat16) * 0.01,
        "cv2_bias": torch.randn(c_mid, dtype=torch.bfloat16) * 0.01,
        "cv3_weight": torch.randn(c_out, c_mid, 1, 1, dtype=torch.bfloat16) * 0.01,
        "cv3_bias": torch.randn(c_out, dtype=torch.bfloat16) * 0.01,
    }


def make_all_weights(nc=80, reg_max=16):
    """Generate random weights for full YOLOv8n model."""
    backbone = {
        "l0": _make_random_cbs_weights(8, 16, 3),
        "l1": _make_random_cbs_weights(16, 32, 3),
        "l2": _make_random_c2f_weights(32, 32, 1),
        "l3": _make_random_cbs_weights(32, 64, 3),
        "l4": _make_random_c2f_weights(64, 64, 2),
        "l5": _make_random_cbs_weights(64, 128, 3),
        "l6": _make_random_c2f_weights(128, 128, 2),
        "l7": _make_random_cbs_weights(128, 256, 3),
        "l8": _make_random_c2f_weights(256, 256, 1),
        "l9": _make_random_sppf_weights(256, 256),
    }
    neck = {
        "l12": _make_random_c2f_weights(384, 128, 1),
        "l15": _make_random_c2f_weights(192, 64, 1),
        "l16": _make_random_cbs_weights(64, 64, 3),
        "l18": _make_random_c2f_weights(192, 128, 1),
        "l19": _make_random_cbs_weights(128, 128, 3),
        "l21": _make_random_c2f_weights(384, 256, 1),
    }
    c_reg = 4 * reg_max
    c_cls = nc
    c2 = 64
    c3 = max(nc, 16)
    detect = {
        "reg_p3": _make_random_detect_branch_weights(64, c2, c_reg),
        "reg_p4": _make_random_detect_branch_weights(128, c2, c_reg),
        "reg_p5": _make_random_detect_branch_weights(256, c2, c_reg),
        "cls_p3": _make_random_detect_branch_weights(64, c3, c_cls),
        "cls_p4": _make_random_detect_branch_weights(128, c3, c_cls),
        "cls_p5": _make_random_detect_branch_weights(256, c3, c_cls),
    }
    return {"backbone": backbone, "neck": neck, "detect": detect}


# ── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    torch.manual_seed(42)
    H, W = 640, 640

    print("=" * 60)
    print("YOLOv8n Full Model — 2 Multi-PDI XCLBINs on NPU")
    print("=" * 60)

    total_t0 = time.time()

    # Generate all weights upfront
    print("\nGenerating random weights...")
    weights = make_all_weights()

    x = torch.randn(1, 3, H, W, dtype=torch.bfloat16)
    print(f"Input: {x.shape}")

    # ── XCLBIN 1: Backbone + Neck ────────────────────────────────────────

    print(f"\n{'─' * 60}")
    print("XCLBIN 1: Backbone + Neck (L0-L21)")
    print(f"{'─' * 60}")

    t0 = time.time()
    ctx1 = AIEContext()
    bb_neck = BackboneNeckPipeline(img_height=H, img_width=W, context=ctx1)
    ctx1.compile_all()
    bb_neck.load_weights(weights)
    ctx1.prepare_runtime()
    prep1_t = time.time() - t0

    n_pdis_1 = len(bb_neck._pdi_map)
    print(f"Ready: {n_pdis_1} PDIs, compiled+prepared in {prep1_t:.1f}s\n")

    t0_fwd1 = time.time()
    det_p3, det_p4, det_p5 = bb_neck.forward(x)
    fwd1_t = time.time() - t0_fwd1

    # Verify backbone+neck outputs
    bb_neck_pass = True
    for name, tensor, exp in [
        ("det_p3", det_p3, (1, 64, 80, 80)),
        ("det_p4", det_p4, (1, 128, 40, 40)),
        ("det_p5", det_p5, (1, 256, 20, 20)),
    ]:
        ok = tensor.shape == exp and torch.isfinite(tensor).all().item()
        if not ok:
            bb_neck_pass = False
        print(f"  {name}: {tensor.shape} finite={torch.isfinite(tensor).all().item()} {'PASS' if ok else 'FAIL'}")

    print(f"\nBackbone+Neck forward: {fwd1_t:.3f}s  {'PASS' if bb_neck_pass else 'FAIL'}")

    if not bb_neck_pass:
        print("ABORTING — backbone+neck failed")
        raise SystemExit(1)

    # Clean up XCLBIN 1 hw_context
    del bb_neck, ctx1
    cleanup_xrt()

    # ── XCLBIN 2: Detect Head ────────────────────────────────────────────

    print(f"\n{'─' * 60}")
    print("XCLBIN 2: Detect Head (6 branches)")
    print(f"{'─' * 60}")

    t0 = time.time()
    ctx2 = AIEContext()
    detect = DetectHeadPipeline(img_height=H, img_width=W, context=ctx2)
    ctx2.compile_all()
    detect.load_weights(weights)
    ctx2.prepare_runtime()
    prep2_t = time.time() - t0

    n_pdis_2 = len(detect._pdi_map)
    print(f"Ready: {n_pdis_2} PDIs, compiled+prepared in {prep2_t:.1f}s\n")

    t0_fwd2 = time.time()
    det_result = detect.forward(det_p3, det_p4, det_p5)
    fwd2_t = time.time() - t0_fwd2

    # Verify detect outputs
    reg_list = det_result["reg"]
    cls_list = det_result["cls"]

    detect_pass = True
    for name, tensor, exp in [
        ("reg_p3", reg_list[0], (1, 64, 80, 80)),
        ("cls_p3", cls_list[0], (1, 80, 80, 80)),
        ("reg_p4", reg_list[1], (1, 64, 40, 40)),
        ("cls_p4", cls_list[1], (1, 80, 40, 40)),
        ("reg_p5", reg_list[2], (1, 64, 20, 20)),
        ("cls_p5", cls_list[2], (1, 80, 20, 20)),
    ]:
        ok = tensor.shape == exp and torch.isfinite(tensor).all().item()
        if not ok:
            detect_pass = False
        print(f"  {name}: {tensor.shape} finite={torch.isfinite(tensor).all().item()} {'PASS' if ok else 'FAIL'}")

    print(f"\nDetect head forward: {fwd2_t:.3f}s  {'PASS' if detect_pass else 'FAIL'}")

    if not detect_pass:
        print("ABORTING — detect head failed")
        raise SystemExit(1)

    # Clean up XCLBIN 2 hw_context
    del detect, ctx2
    cleanup_xrt()

    # ── Post-Processing (CPU) ────────────────────────────────────────────

    print(f"\n{'─' * 60}")
    print("Post-Processing (DFL decode + NMS)")
    print(f"{'─' * 60}")

    t0_pp = time.time()
    pp = YOLOv8nPostProcess(conf_thres=0.25, iou_thres=0.45)
    detections = pp(reg_list, cls_list)
    pp_t = time.time() - t0_pp

    n_boxes = len(detections["boxes"])
    print(f"  Detections: {n_boxes} boxes")
    if n_boxes > 0:
        print(f"  Top score: {detections['scores'][0]:.4f}")
        print(f"  Top box: {detections['boxes'][0].tolist()}")
        print(f"  Top label: {detections['labels'][0].item()}")
    print(f"  Post-processing: {pp_t:.4f}s")

    # ── Summary ──────────────────────────────────────────────────────────

    total_t = time.time() - total_t0
    total_fwd = fwd1_t + fwd2_t

    print(f"\n{'=' * 60}")
    print("FULL MODEL SUMMARY")
    print(f"{'=' * 60}")
    print(f"XCLBIN 1 (BB+Neck):  {n_pdis_1} PDIs  prep={prep1_t:.1f}s  fwd={fwd1_t:.3f}s")
    print(f"XCLBIN 2 (Detect):   {n_pdis_2} PDIs  prep={prep2_t:.1f}s  fwd={fwd2_t:.3f}s")
    print(f"Post-processing:     {pp_t:.4f}s")
    print(f"Total forward:       {total_fwd:.3f}s")
    print(f"Total wall time:     {total_t:.1f}s")
    print(f"Detections:          {n_boxes} boxes")
    print()

    all_pass = bb_neck_pass and detect_pass
    if all_pass:
        print("ALL PASS — FULL YOLOv8n MODEL ON NPU")
        print("  2 xclbins, 2 hw_contexts, L0-L21 + detect + post-processing")
    else:
        print("FAIL — see errors above")
        raise SystemExit(1)
