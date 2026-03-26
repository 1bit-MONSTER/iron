#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Run YOLOv8n with int8 convolutions on NPU (pretrained weights).

Architecture:
  - Int8 conv2d layers run on NPU (int8x int8 MAC -> right-shift -> int8)
  - Dequantization, bias, SiLU, maxpool, upsample, concat run on CPU in float
  - All 63 conv PDIs in one xclbin with one hardware context

Flow per conv layer:
  1. Quantize float input to int8 (CPU)
  2. Run int8 conv on NPU -> int8 output
  3. Dequant: out_float = out_int8 * (2^shift * w_scale * in_act_scale)
  4. Add float bias
  5. SiLU activation (for CBS layers)

Usage:
    python3 iron/applications/yolov8n/run_pretrained_int8.py [--image PATH]
"""

import argparse
import math
import re
import time
import urllib.request
from pathlib import Path

import torch
import torch.nn.functional as F

from iron.common import AIEContext
from iron.applications.yolov8n.pipeline_int8 import (
    Int8ConvPipeline,
    PRED_MAP,
    _buf,
    compute_all_shifts,
    compute_layer_shift,
    lookup_weight,
)
from iron.applications.yolov8n.postprocess import YOLOv8nPostProcess
from iron.applications.yolov8n.run_int8_cpu import Int8YOLOv8nCPU
from iron.applications.yolov8n.run_pretrained import (
    COCO_NAMES,
    preprocess_image,
)


# -- Per-stage calibration percentile ----------------------------------------

# Per-stage percentile map.  Controls how aggressively outlier activations
# are clipped during calibration.  Lower percentile = more clipping = smaller
# scale = better precision for typical values at the cost of clipping outliers.
#
# p100 (1.0) = absolute max (no clipping).  Use for backbone where outliers
# carry real information and the shift is highly sensitive to scale changes.
STAGE_PCT = {
    "input": 1.0,  # Never clip the input image
    "backbone": 1.0,  # L0-L9: backbone is very sensitive to scale changes
    "neck": 1.0,  # L12-L21: moderate sensitivity
    "detect_cbs": 1.0,  # Detect cv1/cv2 (CBS with SiLU)
    "detect_bare": 1.0,  # Detect cv3 (bare conv, final logits)
}


def _get_stage(layer_name):
    """Classify a layer name into its network stage."""
    if layer_name == "input":
        return "input"
    if layer_name.startswith("det."):
        if ".cv3" in layer_name:
            return "detect_bare"
        return "detect_cbs"
    m = re.match(r"l(\d+)", layer_name)
    if m:
        layer_num = int(m.group(1))
        if layer_num <= 9:
            return "backbone"
        return "neck"
    return "backbone"


def get_percentile(layer_name):
    """Return the calibration percentile for a layer."""
    return STAGE_PCT[_get_stage(layer_name)]


# -- Unified Pipeline -------------------------------------------------------


class Int8YOLOv8nPipeline(Int8ConvPipeline):
    """Full YOLOv8n int8 pipeline: all 63 conv PDIs in one xclbin."""

    def __init__(self, shifts, act_scales, int8_weights, context=None):
        self.shifts = shifts
        self.act_scales = act_scales
        self.int8_weights = int8_weights
        super().__init__(context=context)

    def _register_all_layers(self):
        s = self.shifts

        def reg(name, ic, oc, h, w, ks, stride):
            self._register_int8_conv(
                _buf(name), ic, oc, h, w, ks, stride, s[name]
            )

        # ---- BACKBONE ----
        reg("l0", 8, 16, 640, 640, 3, 2)
        reg("l1", 16, 32, 320, 320, 3, 2)

        # L2 C2f (32->32, 160x160, n=1)
        reg("l2.cv1", 32, 32, 160, 160, 1, 1)
        reg("l2.bn0.cv1", 16, 16, 160, 160, 3, 1)
        reg("l2.bn0.cv2", 16, 16, 160, 160, 3, 1)
        reg("l2.cv2", 48, 32, 160, 160, 1, 1)

        reg("l3", 32, 64, 160, 160, 3, 2)

        # L4 C2f (64->64, 80x80, n=2)
        reg("l4.cv1", 64, 64, 80, 80, 1, 1)
        reg("l4.bn0.cv1", 32, 32, 80, 80, 3, 1)
        reg("l4.bn0.cv2", 32, 32, 80, 80, 3, 1)
        reg("l4.bn1.cv1", 32, 32, 80, 80, 3, 1)
        reg("l4.bn1.cv2", 32, 32, 80, 80, 3, 1)
        reg("l4.cv2", 128, 64, 80, 80, 1, 1)

        reg("l5", 64, 128, 80, 80, 3, 2)

        # L6 C2f (128->128, 40x40, n=2)
        reg("l6.cv1", 128, 128, 40, 40, 1, 1)
        reg("l6.bn0.cv1", 64, 64, 40, 40, 3, 1)
        reg("l6.bn0.cv2", 64, 64, 40, 40, 3, 1)
        reg("l6.bn1.cv1", 64, 64, 40, 40, 3, 1)
        reg("l6.bn1.cv2", 64, 64, 40, 40, 3, 1)
        reg("l6.cv2", 256, 128, 40, 40, 1, 1)

        reg("l7", 128, 256, 40, 40, 3, 2)

        # L8 C2f (256->256, 20x20, n=1)
        reg("l8.cv1", 256, 256, 20, 20, 1, 1)
        reg("l8.bn0.cv1", 128, 128, 20, 20, 3, 1)
        reg("l8.bn0.cv2", 128, 128, 20, 20, 3, 1)
        reg("l8.cv2", 384, 256, 20, 20, 1, 1)

        # L9 SPPF (convs only; maxpool on CPU)
        reg("l9.cv1", 256, 128, 20, 20, 1, 1)
        reg("l9.cv2", 512, 256, 20, 20, 1, 1)

        # ---- NECK ----
        # L12 C2f (384->128, 40x40, n=1)
        reg("l12.cv1", 384, 128, 40, 40, 1, 1)
        reg("l12.bn0.cv1", 64, 64, 40, 40, 3, 1)
        reg("l12.bn0.cv2", 64, 64, 40, 40, 3, 1)
        reg("l12.cv2", 192, 128, 40, 40, 1, 1)

        # L15 C2f (192->64, 80x80, n=1)
        reg("l15.cv1", 192, 64, 80, 80, 1, 1)
        reg("l15.bn0.cv1", 32, 32, 80, 80, 3, 1)
        reg("l15.bn0.cv2", 32, 32, 80, 80, 3, 1)
        reg("l15.cv2", 96, 64, 80, 80, 1, 1)

        # L16 CBS (64->64, 80->40, k3s2)
        reg("l16", 64, 64, 80, 80, 3, 2)

        # L18 C2f (192->128, 40x40, n=1)
        reg("l18.cv1", 192, 128, 40, 40, 1, 1)
        reg("l18.bn0.cv1", 64, 64, 40, 40, 3, 1)
        reg("l18.bn0.cv2", 64, 64, 40, 40, 3, 1)
        reg("l18.cv2", 192, 128, 40, 40, 1, 1)

        # L19 CBS (128->128, 40->20, k3s2)
        reg("l19", 128, 128, 40, 40, 3, 2)

        # L21 C2f (384->256, 20x20, n=1)
        reg("l21.cv1", 384, 256, 20, 20, 1, 1)
        reg("l21.bn0.cv1", 128, 128, 20, 20, 3, 1)
        reg("l21.bn0.cv2", 128, 128, 20, 20, 3, 1)
        reg("l21.cv2", 384, 256, 20, 20, 1, 1)

        # ---- DETECT HEAD ----
        for branch in ["reg_p3", "cls_p3"]:
            c_mid = 64 if branch.startswith("reg") else 80
            c_out = 64 if branch.startswith("reg") else 80
            reg(f"det.{branch}.cv1", 64, c_mid, 80, 80, 3, 1)
            reg(f"det.{branch}.cv2", c_mid, c_mid, 80, 80, 3, 1)
            reg(f"det.{branch}.cv3", c_mid, c_out, 80, 80, 1, 1)

        for branch in ["reg_p4", "cls_p4"]:
            c_mid = 64 if branch.startswith("reg") else 80
            c_out = 64 if branch.startswith("reg") else 80
            reg(f"det.{branch}.cv1", 128, c_mid, 40, 40, 3, 1)
            reg(f"det.{branch}.cv2", c_mid, c_mid, 40, 40, 3, 1)
            reg(f"det.{branch}.cv3", c_mid, c_out, 40, 40, 1, 1)

        for branch in ["reg_p5", "cls_p5"]:
            c_mid = 64 if branch.startswith("reg") else 80
            c_out = 64 if branch.startswith("reg") else 80
            reg(f"det.{branch}.cv1", 256, c_mid, 20, 20, 3, 1)
            reg(f"det.{branch}.cv2", c_mid, c_mid, 20, 20, 3, 1)
            reg(f"det.{branch}.cv3", c_mid, c_out, 20, 20, 1, 1)

    def _cbs(self, x, name):
        """Run CBS layer: int8 conv NPU -> dequant -> bias -> SiLU."""
        w, ws, b = lookup_weight(self.int8_weights, name)
        pred = PRED_MAP[name]
        in_scale = self.act_scales.get(pred, 1.0)
        return self.int8_cbs(x, _buf(name), w, ws, b, in_scale)

    def _c2f(self, x, prefix, n_bn, shortcut=True):
        """Run a C2f block."""
        x = self._cbs(x, f"{prefix}.cv1")
        chunks = x.chunk(2, dim=1)
        outputs = [chunks[0], chunks[1]]
        for i in range(n_bn):
            inp = outputs[-1]
            y = self._cbs(inp, f"{prefix}.bn{i}.cv1")
            y = self._cbs(y, f"{prefix}.bn{i}.cv2")
            if shortcut:
                y = y + inp
            outputs.append(y)
        x = torch.cat(outputs, dim=1)
        return self._cbs(x, f"{prefix}.cv2")

    def _detect_branch(self, x, branch_name):
        """Run a detect branch (2x CBS 3x3 + 1x Conv 1x1)."""
        for cv in ["cv1", "cv2"]:
            name = f"det.{branch_name}.{cv}"
            w, ws, b = lookup_weight(self.int8_weights, name)
            pred = PRED_MAP[name]
            in_scale = self.act_scales.get(pred, 1.0)
            x = self.int8_cbs(x, _buf(name), w, ws, b, in_scale)

        # cv3: bare conv (no activation)
        name = f"det.{branch_name}.cv3"
        w, ws, b = lookup_weight(self.int8_weights, name)
        pred = PRED_MAP[name]
        in_scale = self.act_scales.get(pred, 1.0)
        x = self.int8_conv_no_act(x, _buf(name), w, ws, b, in_scale)
        return x

    def forward(self, x):
        """Run full YOLOv8n: backbone + neck + detect.

        Args:
            x: Input [1, 3, 640, 640] float tensor.

        Returns:
            dict with 'reg': [3 tensors], 'cls': [3 tensors].
        """
        x = x.float()
        x = F.pad(x, (0, 0, 0, 0, 0, 5))  # 3ch -> 8ch

        # ---- BACKBONE ----
        x = self._cbs(x, "l0")
        print(f"  L0:  {x.shape}")
        x = self._cbs(x, "l1")
        print(f"  L1:  {x.shape}")
        x = self._c2f(x, "l2", 1)
        print(f"  L2:  {x.shape}")
        x = self._cbs(x, "l3")
        print(f"  L3:  {x.shape}")
        p3 = self._c2f(x, "l4", 2)
        print(f"  L4:  {p3.shape}  [P3]")
        x = self._cbs(p3, "l5")
        print(f"  L5:  {x.shape}")
        p4 = self._c2f(x, "l6", 2)
        print(f"  L6:  {p4.shape}  [P4]")
        x = self._cbs(p4, "l7")
        print(f"  L7:  {x.shape}")
        x = self._c2f(x, "l8", 1)
        print(f"  L8:  {x.shape}")

        # SPPF: convs on NPU, maxpool on CPU
        x = self._cbs(x, "l9.cv1")
        y1 = F.max_pool2d(x, 5, stride=1, padding=2)
        y2 = F.max_pool2d(y1, 5, stride=1, padding=2)
        y3 = F.max_pool2d(y2, 5, stride=1, padding=2)
        x = torch.cat([x, y1, y2, y3], dim=1)
        p5 = self._cbs(x, "l9.cv2")
        print(f"  L9:  {p5.shape}  [P5]")

        # ---- NECK (FPN up-path) ----
        x = F.interpolate(p5, scale_factor=2, mode="nearest")
        x = torch.cat([x, p4], dim=1)
        l12_out = self._c2f(x, "l12", 1, shortcut=False)
        print(f"  L12: {l12_out.shape}")

        x = F.interpolate(l12_out, scale_factor=2, mode="nearest")
        x = torch.cat([x, p3], dim=1)
        det_p3 = self._c2f(x, "l15", 1, shortcut=False)
        print(f"  L15: {det_p3.shape}  [det_p3]")

        # ---- NECK (PAN down-path) ----
        x = self._cbs(det_p3, "l16")
        print(f"  L16: {x.shape}")
        x = torch.cat([x, l12_out], dim=1)
        det_p4 = self._c2f(x, "l18", 1, shortcut=False)
        print(f"  L18: {det_p4.shape}  [det_p4]")

        x = self._cbs(det_p4, "l19")
        print(f"  L19: {x.shape}")
        x = torch.cat([x, p5], dim=1)
        det_p5 = self._c2f(x, "l21", 1, shortcut=False)
        print(f"  L21: {det_p5.shape}  [det_p5]")

        # ---- DETECT HEAD ----
        reg_p3 = self._detect_branch(det_p3, "reg_p3")
        print(f"  reg_p3: {reg_p3.shape}")
        cls_p3 = self._detect_branch(det_p3, "cls_p3")
        print(f"  cls_p3: {cls_p3.shape}")

        reg_p4 = self._detect_branch(det_p4, "reg_p4")
        print(f"  reg_p4: {reg_p4.shape}")
        cls_p4 = self._detect_branch(det_p4, "cls_p4")
        print(f"  cls_p4: {cls_p4.shape}")

        reg_p5 = self._detect_branch(det_p5, "reg_p5")
        print(f"  reg_p5: {reg_p5.shape}")
        cls_p5 = self._detect_branch(det_p5, "cls_p5")
        print(f"  cls_p5: {cls_p5.shape}")

        return {
            "reg": [reg_p3, reg_p4, reg_p5],
            "cls": [cls_p3, cls_p4, cls_p5],
        }


# -- Main -------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Run YOLOv8n with int8 convs on NPU"
    )
    parser.add_argument(
        "--image", default="test_bus.jpg", help="Path to test image"
    )
    parser.add_argument(
        "--model", default="yolov8n.pt", help="Path to YOLOv8n weights"
    )
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Downloading test image to {image_path}...")
        urllib.request.urlretrieve(
            "https://ultralytics.com/images/bus.jpg", str(image_path)
        )

    print("=" * 70)
    print("YOLOv8n INT8 NPU Inference")
    print("=" * 70)

    # -- Step 1: Load model, quantize, calibrate ----------------------------

    print("\n[1] Loading model, quantizing weights, calibrating...")
    t0 = time.time()
    runner = Int8YOLOv8nCPU(args.model)
    img_tensor = preprocess_image(image_path, img_size=640)
    runner.calibrate(img_tensor, percentile_fn=get_percentile)
    calib_time = time.time() - t0
    print(f"    Calibration: {calib_time:.1f}s")

    int8_weights = runner.int8_weights
    act_scales = runner.act_scales

    # -- Step 2: Compute per-layer shifts -----------------------------------

    print("\n[2] Computing per-layer shifts...")
    shifts = compute_all_shifts(int8_weights, act_scales)
    shift_vals = list(shifts.values())
    print(f"    Shift range: [{min(shift_vals)}, {max(shift_vals)}]")
    print(f"    Shift mean: {sum(shift_vals)/len(shift_vals):.1f}")

    # -- Step 3: Build single xclbin with all 63 PDIs ----------------------

    print(f"\n{'=' * 70}")
    print("Building single xclbin (63 PDIs)")
    print(f"{'=' * 70}")

    t0 = time.time()
    ctx = AIEContext(use_runlist=False)
    pipeline = Int8YOLOv8nPipeline(
        shifts, act_scales, int8_weights, context=ctx
    )
    ctx.compile_all()
    ctx.prepare_runtime()
    prep_t = time.time() - t0
    n_pdis = len(pipeline._pdi_map)
    print(f"Ready: {n_pdis} PDIs, compiled+prepared in {prep_t:.1f}s")

    # -- Step 4: Run inference ----------------------------------------------

    print(f"\n{'=' * 70}")
    print("Running inference")
    print(f"{'=' * 70}")

    t0_fwd = time.time()
    result = pipeline.forward(img_tensor)
    fwd_t = time.time() - t0_fwd
    print(f"Forward: {fwd_t:.3f}s")

    # -- Step 5: Post-process -----------------------------------------------

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
            name = (
                COCO_NAMES[label]
                if label < len(COCO_NAMES)
                else f"class_{label}"
            )
            print(
                f"    {name}: {score:.3f} at "
                f"[{box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f}]"
            )

    # Also try lower threshold
    pp_low = YOLOv8nPostProcess(conf_thres=0.10, iou_thres=0.45)
    dets_low = pp_low(result["reg"], result["cls"])
    n_low = len(dets_low["boxes"])
    print(f"  Detections (conf>0.10): {n_low}")

    # -- Step 6: Compare with CPU int8 reference ----------------------------

    print(f"\n{'=' * 70}")
    print("CPU Int8 Reference Comparison")
    print(f"{'=' * 70}")

    cpu_result = runner.forward_int8(img_tensor)
    cpu_detections = pp(cpu_result["reg"], cpu_result["cls"])
    n_cpu = len(cpu_detections["boxes"])
    print(f"  CPU int8 detections (conf>0.25): {n_cpu}")
    if n_cpu > 0:
        for i in range(min(10, n_cpu)):
            box = cpu_detections["boxes"][i].tolist()
            score = cpu_detections["scores"][i].item()
            label = cpu_detections["labels"][i].item()
            name = (
                COCO_NAMES[label]
                if label < len(COCO_NAMES)
                else f"class_{label}"
            )
            print(
                f"    {name}: {score:.3f} at "
                f"[{box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f}]"
            )

    # Feature map comparison
    print(f"\n  NPU vs CPU int8 feature map comparison:")
    for scale_name, npu_reg, npu_cls, cpu_reg, cpu_cls in [
        ("P3", result["reg"][0], result["cls"][0],
         cpu_result["reg"][0], cpu_result["cls"][0]),
        ("P4", result["reg"][1], result["cls"][1],
         cpu_result["reg"][1], cpu_result["cls"][1]),
        ("P5", result["reg"][2], result["cls"][2],
         cpu_result["reg"][2], cpu_result["cls"][2]),
    ]:
        reg_corr = torch.corrcoef(
            torch.stack([
                npu_reg.float().flatten(), cpu_reg.float().flatten()
            ])
        )[0, 1].item()
        cls_corr = torch.corrcoef(
            torch.stack([
                npu_cls.float().flatten(), cpu_cls.float().flatten()
            ])
        )[0, 1].item()
        print(
            f"    {scale_name}: reg_corr={reg_corr:.4f}  "
            f"cls_corr={cls_corr:.4f}"
        )

    # -- Summary ------------------------------------------------------------

    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    print(f"PDIs:      {n_pdis}")
    print(f"Compile:   {prep_t:.1f}s")
    print(f"Forward:   {fwd_t:.3f}s")
    print(f"NPU int8:  {n_boxes} detections (conf>0.25)")
    print(f"CPU int8:  {n_cpu} detections (conf>0.25)")
    print()

    if n_boxes >= 2:
        print("PASS -- NPU int8 produces meaningful detections")
    else:
        print("MARGINAL -- check lower thresholds or calibration")


if __name__ == "__main__":
    main()
