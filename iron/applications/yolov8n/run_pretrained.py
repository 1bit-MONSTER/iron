#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Run YOLOv8n with real pretrained weights on a test image using the NPU.

Loads ultralytics YOLOv8n pretrained weights (COCO), fuses Conv+BN, maps
them to our pipeline's weight format, preprocesses a test image, runs
inference through the 2-xclbin NPU pipeline, post-processes detections,
and compares results against ultralytics CPU inference.

Usage:
    python3 iron/applications/yolov8n/run_pretrained.py [--image PATH]
"""

import argparse
import gc
import time
import urllib.request
from pathlib import Path

import cv2
import torch
import torch.nn.functional as F

from iron.applications.yolov8n.model_prep import fuse_conv_bn
from iron.applications.yolov8n.postprocess import YOLOv8nPostProcess
from iron.applications.yolov8n.run_full_model import (
    BackboneNeckPipeline,
    DetectHeadPipeline,
    cleanup_xrt,
)
from iron.common import AIEContext

# COCO 80 class names
COCO_NAMES = [
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "couch",
    "potted plant",
    "bed",
    "dining table",
    "toilet",
    "tv",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]


# ── Weight Extraction ────────────────────────────────────────────────────────


def _fuse_cbs(module):
    """Fuse a Conv+BN module (ultralytics Conv class) into weight+bias.

    Args:
        module: ultralytics Conv module with .conv and .bn attributes.

    Returns:
        (weight_bf16, bias_bf16) tuple.
    """
    w, b = fuse_conv_bn(module.conv, module.bn)
    return w.to(torch.bfloat16), b.to(torch.bfloat16)


def _extract_cbs_weights(module):
    """Extract CBS (Conv+BN+SiLU) weights into pipeline format."""
    w, b = _fuse_cbs(module)
    return {"weight": w, "bias": b}


def _extract_c2f_weights(c2f_module):
    """Extract C2f block weights into pipeline format.

    Maps ultralytics C2f structure to our weight dict format:
        cv1_weight, cv1_bias: pointwise expand
        bottlenecks: list of (cv1_w, cv1_b, cv2_w, cv2_b) tuples
        cv2_weight, cv2_bias: pointwise reduce
    """
    cv1_w, cv1_b = _fuse_cbs(c2f_module.cv1)
    cv2_w, cv2_b = _fuse_cbs(c2f_module.cv2)

    bottlenecks = []
    for bn in c2f_module.m:
        bn_cv1_w, bn_cv1_b = _fuse_cbs(bn.cv1)
        bn_cv2_w, bn_cv2_b = _fuse_cbs(bn.cv2)
        bottlenecks.append((bn_cv1_w, bn_cv1_b, bn_cv2_w, bn_cv2_b))

    return {
        "cv1_weight": cv1_w,
        "cv1_bias": cv1_b,
        "bottlenecks": bottlenecks,
        "cv2_weight": cv2_w,
        "cv2_bias": cv2_b,
    }


def _extract_sppf_weights(sppf_module):
    """Extract SPPF block weights into pipeline format."""
    cv1_w, cv1_b = _fuse_cbs(sppf_module.cv1)
    cv2_w, cv2_b = _fuse_cbs(sppf_module.cv2)
    return {
        "cv1_weight": cv1_w,
        "cv1_bias": cv1_b,
        "cv2_weight": cv2_w,
        "cv2_bias": cv2_b,
    }


def _extract_detect_branch_weights(det_module, branch_attr, scale_idx):
    """Extract detect branch weights.

    Args:
        det_module: ultralytics Detect module.
        branch_attr: 'cv2' for regression, 'cv3' for classification.
        scale_idx: 0=P3, 1=P4, 2=P5.

    Returns:
        Weight dict with cv1_weight/bias, cv2_weight/bias, cv3_weight/bias.
    """
    seq = getattr(det_module, branch_attr)[scale_idx]

    # seq[0] and seq[1] are Conv+BN+SiLU modules
    cv1_w, cv1_b = _fuse_cbs(seq[0])
    cv2_w, cv2_b = _fuse_cbs(seq[1])

    # seq[2] is a bare nn.Conv2d (no BN, no activation)
    cv3_w = seq[2].weight.to(torch.bfloat16)
    cv3_b = seq[2].bias.to(torch.bfloat16)

    return {
        "cv1_weight": cv1_w,
        "cv1_bias": cv1_b,
        "cv2_weight": cv2_w,
        "cv2_bias": cv2_b,
        "cv3_weight": cv3_w,
        "cv3_bias": cv3_b,
    }


def extract_pretrained_weights(model_path="yolov8n.pt"):
    """Load ultralytics YOLOv8n and extract all weights in pipeline format.

    Maps the ultralytics module hierarchy to our pipeline's weight dictionary:
        backbone: {l0..l9}
        neck:     {l12, l15, l16, l18, l19, l21}
        detect:   {reg_p3..p5, cls_p3..p5}

    Args:
        model_path: Path to YOLOv8n weights file.

    Returns:
        Weight dictionary compatible with pipeline.load_weights().
    """
    from ultralytics import YOLO

    model = YOLO(model_path)
    m = model.model.model  # Sequential of modules

    # ---- Backbone (L0-L9) ----
    backbone = {}

    # L0: Conv(3->16, k3, s2) -- pad input channels 3->8
    l0_w, l0_b = _fuse_cbs(m[0])
    # Pad weight from [16, 3, 3, 3] to [16, 8, 3, 3]
    l0_w = F.pad(l0_w.float(), (0, 0, 0, 0, 0, 5)).to(torch.bfloat16)
    backbone["l0"] = {"weight": l0_w, "bias": l0_b}

    # L1: Conv(16->32, k3, s2)
    backbone["l1"] = _extract_cbs_weights(m[1])

    # L2: C2f(32->32, n=1)
    backbone["l2"] = _extract_c2f_weights(m[2])

    # L3: Conv(32->64, k3, s2)
    backbone["l3"] = _extract_cbs_weights(m[3])

    # L4: C2f(64->64, n=2)
    backbone["l4"] = _extract_c2f_weights(m[4])

    # L5: Conv(64->128, k3, s2)
    backbone["l5"] = _extract_cbs_weights(m[5])

    # L6: C2f(128->128, n=2)
    backbone["l6"] = _extract_c2f_weights(m[6])

    # L7: Conv(128->256, k3, s2)
    backbone["l7"] = _extract_cbs_weights(m[7])

    # L8: C2f(256->256, n=1)
    backbone["l8"] = _extract_c2f_weights(m[8])

    # L9: SPPF(256->256, k=5)
    backbone["l9"] = _extract_sppf_weights(m[9])

    # ---- Neck (L12-L21) ----
    # L10=Upsample, L11=Concat (no weights)
    neck = {}

    # L12: C2f(384->128, n=1)
    neck["l12"] = _extract_c2f_weights(m[12])

    # L13=Upsample, L14=Concat (no weights)

    # L15: C2f(192->64, n=1)
    neck["l15"] = _extract_c2f_weights(m[15])

    # L16: Conv(64->64, k3, s2)
    neck["l16"] = _extract_cbs_weights(m[16])

    # L17=Concat (no weights)

    # L18: C2f(192->128, n=1)
    neck["l18"] = _extract_c2f_weights(m[18])

    # L19: Conv(128->128, k3, s2)
    neck["l19"] = _extract_cbs_weights(m[19])

    # L20=Concat (no weights)

    # L21: C2f(384->256, n=1)
    neck["l21"] = _extract_c2f_weights(m[21])

    # ---- Detect Head (L22) ----
    det = m[22]  # Detect module
    detect = {}

    # Regression branches (cv2): P3=idx0, P4=idx1, P5=idx2
    detect["reg_p3"] = _extract_detect_branch_weights(det, "cv2", 0)
    detect["reg_p4"] = _extract_detect_branch_weights(det, "cv2", 1)
    detect["reg_p5"] = _extract_detect_branch_weights(det, "cv2", 2)

    # Classification branches (cv3): P3=idx0, P4=idx1, P5=idx2
    detect["cls_p3"] = _extract_detect_branch_weights(det, "cv3", 0)
    detect["cls_p4"] = _extract_detect_branch_weights(det, "cv3", 1)
    detect["cls_p5"] = _extract_detect_branch_weights(det, "cv3", 2)

    return {"backbone": backbone, "neck": neck, "detect": detect}


# ── Image Preprocessing ──────────────────────────────────────────────────────


def preprocess_image(image_path, img_size=640):
    """Preprocess an image for YOLOv8n inference.

    Resizes to img_size x img_size, converts BGR->RGB, normalizes to [0,1],
    and converts to bfloat16 tensor.

    Args:
        image_path: Path to input image.
        img_size: Target size (square).

    Returns:
        bfloat16 tensor [1, 3, img_size, img_size].
    """
    img = cv2.imread(str(image_path))
    if img is None:
        raise FileNotFoundError(f"Cannot read image: {image_path}")

    img = cv2.resize(img, (img_size, img_size))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # HWC -> CHW, normalize to [0,1], add batch dim
    img_tensor = torch.from_numpy(img).permute(2, 0, 1).unsqueeze(0).float() / 255.0
    return img_tensor.to(torch.bfloat16)


# ── Ultralytics Reference ────────────────────────────────────────────────────


def run_ultralytics_reference(image_path, model_path="yolov8n.pt"):
    """Run ultralytics CPU inference for comparison.

    Args:
        image_path: Path to input image.
        model_path: Path to model weights.

    Returns:
        List of (class_name, confidence, [x1,y1,x2,y2]) tuples.
    """
    from ultralytics import YOLO

    model = YOLO(model_path)
    results = model(str(image_path), imgsz=640, verbose=False)
    detections = []
    for box in results[0].boxes:
        cls_id = int(box.cls.item())
        conf = box.conf.item()
        xyxy = box.xyxy[0].tolist()
        name = model.names[cls_id]
        detections.append((name, conf, xyxy))
    return detections


# ── CPU Reference (same preprocessing) ───────────────────────────────────────


def run_cpu_reference(img_tensor, weights):
    """Run YOLOv8n through CPU convolution using the same fused weights.

    This validates that our weight extraction produces correct results
    independent of the NPU pipeline. Uses torch.nn.functional.conv2d
    with the same fused weights.

    Args:
        img_tensor: Input [1, 3, H, W] bfloat16 tensor.
        weights: Weight dict from extract_pretrained_weights().

    Returns:
        dict with 'reg': [3 tensors], 'cls': [3 tensors].
    """

    def conv_silu(x, w, b, stride=1):
        kH = w.shape[2]
        pad = kH // 2
        out = F.conv2d(x.float(), w.float(), b.float(), stride=stride, padding=pad)
        return F.silu(out).to(torch.bfloat16)

    def conv_no_act(x, w, b, stride=1):
        kH = w.shape[2]
        pad = kH // 2
        out = F.conv2d(x.float(), w.float(), b.float(), stride=stride, padding=pad)
        return out.to(torch.bfloat16)

    def run_c2f(x, wts, shortcut=True):
        x = conv_silu(x, wts["cv1_weight"], wts["cv1_bias"])
        chunks = x.chunk(2, dim=1)
        outputs = [chunks[0], chunks[1]]
        for w1, b1, w2, b2 in wts["bottlenecks"]:
            inp = outputs[-1]
            y = conv_silu(inp, w1, b1)
            y = conv_silu(y, w2, b2)
            if shortcut:
                y = y + inp
            outputs.append(y)
        x = torch.cat(outputs, dim=1)
        return conv_silu(x, wts["cv2_weight"], wts["cv2_bias"])

    def run_sppf(x, wts):
        x = conv_silu(x, wts["cv1_weight"], wts["cv1_bias"])
        y1 = F.max_pool2d(x.float(), 5, stride=1, padding=2).to(torch.bfloat16)
        y2 = F.max_pool2d(y1.float(), 5, stride=1, padding=2).to(torch.bfloat16)
        y3 = F.max_pool2d(y2.float(), 5, stride=1, padding=2).to(torch.bfloat16)
        x = torch.cat([x, y1, y2, y3], dim=1)
        return conv_silu(x, wts["cv2_weight"], wts["cv2_bias"])

    def run_detect_branch(x, wts):
        x = conv_silu(x, wts["cv1_weight"], wts["cv1_bias"])
        x = conv_silu(x, wts["cv2_weight"], wts["cv2_bias"])
        x = conv_no_act(x, wts["cv3_weight"], wts["cv3_bias"])
        return x

    bb = weights["backbone"]
    nk = weights["neck"]
    dt = weights["detect"]

    # Pad 3ch -> 8ch
    x = F.pad(img_tensor, (0, 0, 0, 0, 0, 5))

    # Backbone
    x = conv_silu(x, bb["l0"]["weight"], bb["l0"]["bias"], stride=2)
    x = conv_silu(x, bb["l1"]["weight"], bb["l1"]["bias"], stride=2)
    x = run_c2f(x, bb["l2"])
    x = conv_silu(x, bb["l3"]["weight"], bb["l3"]["bias"], stride=2)
    p3 = run_c2f(x, bb["l4"])
    x = conv_silu(p3, bb["l5"]["weight"], bb["l5"]["bias"], stride=2)
    p4 = run_c2f(x, bb["l6"])
    x = conv_silu(p4, bb["l7"]["weight"], bb["l7"]["bias"], stride=2)
    x = run_c2f(x, bb["l8"])
    p5 = run_sppf(x, bb["l9"])

    # Neck FPN up-path
    x = F.interpolate(p5.float(), scale_factor=2, mode="nearest").to(torch.bfloat16)
    x = torch.cat([x, p4], dim=1)
    l12_out = run_c2f(x, nk["l12"], shortcut=False)
    x = F.interpolate(l12_out.float(), scale_factor=2, mode="nearest").to(
        torch.bfloat16
    )
    x = torch.cat([x, p3], dim=1)
    det_p3 = run_c2f(x, nk["l15"], shortcut=False)

    # Neck PAN down-path
    x = conv_silu(det_p3, nk["l16"]["weight"], nk["l16"]["bias"], stride=2)
    x = torch.cat([x, l12_out], dim=1)
    det_p4 = run_c2f(x, nk["l18"], shortcut=False)
    x = conv_silu(det_p4, nk["l19"]["weight"], nk["l19"]["bias"], stride=2)
    x = torch.cat([x, p5], dim=1)
    det_p5 = run_c2f(x, nk["l21"], shortcut=False)

    # Detect head
    reg_p3 = run_detect_branch(det_p3, dt["reg_p3"])
    cls_p3 = run_detect_branch(det_p3, dt["cls_p3"])
    reg_p4 = run_detect_branch(det_p4, dt["reg_p4"])
    cls_p4 = run_detect_branch(det_p4, dt["cls_p4"])
    reg_p5 = run_detect_branch(det_p5, dt["reg_p5"])
    cls_p5 = run_detect_branch(det_p5, dt["cls_p5"])

    return {
        "reg": [reg_p3, reg_p4, reg_p5],
        "cls": [cls_p3, cls_p4, cls_p5],
    }


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run YOLOv8n with pretrained weights on NPU"
    )
    parser.add_argument(
        "--image",
        default="test_bus.jpg",
        help="Path to test image (default: test_bus.jpg, auto-downloaded)",
    )
    parser.add_argument(
        "--model",
        default="yolov8n.pt",
        help="Path to YOLOv8n weights (default: yolov8n.pt, auto-downloaded)",
    )
    parser.add_argument(
        "--cpu-only",
        action="store_true",
        help="Run CPU reference only (skip NPU pipeline)",
    )
    args = parser.parse_args()

    # Download test image if needed
    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Downloading test image to {image_path}...")
        urllib.request.urlretrieve(
            "https://ultralytics.com/images/bus.jpg", str(image_path)
        )

    H, W = 640, 640

    print("=" * 70)
    print("YOLOv8n Pretrained Inference")
    print("=" * 70)

    # ── Step 1: Extract pretrained weights ────────────────────────────────
    print("\n[1] Extracting pretrained weights from ultralytics YOLOv8n...")
    t0 = time.time()
    weights = extract_pretrained_weights(args.model)
    print(f"    Weight extraction: {time.time() - t0:.1f}s")

    # Print weight shapes for verification
    bb = weights["backbone"]
    print(f"    L0 weight: {bb['l0']['weight'].shape} (padded 3->8 input channels)")
    print(f"    L1 weight: {bb['l1']['weight'].shape}")
    print(f"    L9 SPPF cv1: {bb['l9']['cv1_weight'].shape}")
    dt = weights["detect"]
    print(f"    det reg_p3 cv1: {dt['reg_p3']['cv1_weight'].shape}")
    print(f"    det cls_p3 cv3: {dt['cls_p3']['cv3_weight'].shape}")

    # ── Step 2: Preprocess image ──────────────────────────────────────────
    print(f"\n[2] Preprocessing image: {image_path}")
    img_tensor = preprocess_image(image_path, img_size=H)
    print(f"    Input tensor: {img_tensor.shape} {img_tensor.dtype}")
    print(
        f"    Value range: [{img_tensor.float().min():.3f}, {img_tensor.float().max():.3f}]"
    )

    # ── Step 3: CPU reference with same weights ───────────────────────────
    print("\n[3] Running CPU reference (fused weights, bf16)...")
    t0 = time.time()
    cpu_result = run_cpu_reference(img_tensor, weights)
    cpu_time = time.time() - t0
    print(f"    CPU forward: {cpu_time:.3f}s")

    pp = YOLOv8nPostProcess(conf_thres=0.25, iou_thres=0.45)
    cpu_detections = pp(cpu_result["reg"], cpu_result["cls"])
    n_cpu = len(cpu_detections["boxes"])
    print(f"    CPU detections: {n_cpu}")
    if n_cpu > 0:
        for i in range(min(10, n_cpu)):
            box = cpu_detections["boxes"][i].tolist()
            score = cpu_detections["scores"][i].item()
            label = cpu_detections["labels"][i].item()
            name = COCO_NAMES[label] if label < len(COCO_NAMES) else f"class_{label}"
            print(
                f"      {name}: {score:.3f} at "
                f"[{box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f}]"
            )

    if args.cpu_only:
        print("\n[CPU-only mode] Skipping NPU pipeline.")

        # Run ultralytics reference for comparison
        print("\n[4] Running ultralytics reference (native pipeline)...")
        ultra_dets = run_ultralytics_reference(image_path, args.model)
        print(f"    Ultralytics detections: {len(ultra_dets)}")
        for name, conf, xyxy in ultra_dets[:10]:
            print(
                f"      {name}: {conf:.3f} at "
                f"[{xyxy[0]:.0f},{xyxy[1]:.0f},{xyxy[2]:.0f},{xyxy[3]:.0f}]"
            )

        print("\n" + "=" * 70)
        print("DONE (CPU-only mode)")
        raise SystemExit(0)

    # ── Step 4: NPU Pipeline — Backbone + Neck ───────────────────────────
    print(f"\n[4] NPU Pipeline: Backbone + Neck (XCLBIN 1)")
    print(f"    {'─' * 60}")

    t0 = time.time()
    ctx1 = AIEContext()
    bb_neck = BackboneNeckPipeline(img_height=H, img_width=W, context=ctx1)
    ctx1.compile_all()
    bb_neck.load_weights(weights)
    ctx1.prepare_runtime()
    prep1_t = time.time() - t0

    n_pdis_1 = len(bb_neck._pdi_map)
    print(f"    Ready: {n_pdis_1} PDIs, compiled+prepared in {prep1_t:.1f}s")

    t0_fwd1 = time.time()
    det_p3, det_p4, det_p5 = bb_neck.forward(img_tensor)
    fwd1_t = time.time() - t0_fwd1

    bb_neck_pass = True
    for name, tensor, exp in [
        ("det_p3", det_p3, (1, 64, 80, 80)),
        ("det_p4", det_p4, (1, 128, 40, 40)),
        ("det_p5", det_p5, (1, 256, 20, 20)),
    ]:
        ok = tensor.shape == exp and torch.isfinite(tensor).all().item()
        if not ok:
            bb_neck_pass = False
        print(
            f"    {name}: {tensor.shape} "
            f"finite={torch.isfinite(tensor).all().item()} "
            f"{'PASS' if ok else 'FAIL'}"
        )

    print(
        f"    Backbone+Neck forward: {fwd1_t:.3f}s "
        f"{'PASS' if bb_neck_pass else 'FAIL'}"
    )

    if not bb_neck_pass:
        print("ABORTING -- backbone+neck failed")
        raise SystemExit(1)

    del bb_neck, ctx1
    cleanup_xrt()

    # ── Step 5: NPU Pipeline — Detect Head ────────────────────────────────
    print(f"\n[5] NPU Pipeline: Detect Head (XCLBIN 2)")
    print(f"    {'─' * 60}")

    t0 = time.time()
    ctx2 = AIEContext()
    detect = DetectHeadPipeline(img_height=H, img_width=W, context=ctx2)
    ctx2.compile_all()
    detect.load_weights(weights)
    ctx2.prepare_runtime()
    prep2_t = time.time() - t0

    n_pdis_2 = len(detect._pdi_map)
    print(f"    Ready: {n_pdis_2} PDIs, compiled+prepared in {prep2_t:.1f}s")

    t0_fwd2 = time.time()
    det_result = detect.forward(det_p3, det_p4, det_p5)
    fwd2_t = time.time() - t0_fwd2

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
        print(
            f"    {name}: {tensor.shape} "
            f"finite={torch.isfinite(tensor).all().item()} "
            f"{'PASS' if ok else 'FAIL'}"
        )

    print(
        f"    Detect head forward: {fwd2_t:.3f}s "
        f"{'PASS' if detect_pass else 'FAIL'}"
    )

    if not detect_pass:
        print("ABORTING -- detect head failed")
        raise SystemExit(1)

    del detect, ctx2
    cleanup_xrt()

    # ── Step 6: Post-Processing ───────────────────────────────────────────
    print(f"\n[6] Post-Processing (DFL decode + NMS)")
    print(f"    {'─' * 60}")

    t0_pp = time.time()
    npu_detections = pp(reg_list, cls_list)
    pp_t = time.time() - t0_pp

    n_npu = len(npu_detections["boxes"])
    print(f"    NPU detections (conf>0.25): {n_npu}")
    if n_npu > 0:
        for i in range(min(10, n_npu)):
            box = npu_detections["boxes"][i].tolist()
            score = npu_detections["scores"][i].item()
            label = npu_detections["labels"][i].item()
            name = COCO_NAMES[label] if label < len(COCO_NAMES) else f"class_{label}"
            print(
                f"      {name}: {score:.3f} at "
                f"[{box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f}]"
            )

    # Also try lower confidence threshold to see if NPU outputs contain signals
    pp_low = YOLOv8nPostProcess(conf_thres=0.10, iou_thres=0.45)
    npu_dets_low = pp_low(reg_list, cls_list)
    n_npu_low = len(npu_dets_low["boxes"])
    print(f"    NPU detections (conf>0.10): {n_npu_low}")
    if n_npu_low > 0:
        for i in range(min(10, n_npu_low)):
            box = npu_dets_low["boxes"][i].tolist()
            score = npu_dets_low["scores"][i].item()
            label = npu_dets_low["labels"][i].item()
            name = COCO_NAMES[label] if label < len(COCO_NAMES) else f"class_{label}"
            print(
                f"      {name}: {score:.3f} at "
                f"[{box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f}]"
            )

    # Score distribution diagnostics
    cls_flat_all = torch.cat(
        [c.float().squeeze(0).permute(1, 2, 0).reshape(-1, 80) for c in cls_list],
        dim=0,
    )
    max_scores_all = cls_flat_all.sigmoid().max(dim=1)[0]
    print(
        f"    NPU cls score stats: max={max_scores_all.max():.4f} "
        f"mean={max_scores_all.mean():.4f} "
        f">0.25: {(max_scores_all > 0.25).sum().item()} "
        f">0.10: {(max_scores_all > 0.10).sum().item()}"
    )

    print(f"    Post-processing: {pp_t:.4f}s")

    # ── Step 7: Ultralytics Reference ─────────────────────────────────────
    print(f"\n[7] Ultralytics Reference (native CPU pipeline)")
    print(f"    {'─' * 60}")

    ultra_dets = run_ultralytics_reference(image_path, args.model)
    print(f"    Ultralytics detections: {len(ultra_dets)}")
    for name, conf, xyxy in ultra_dets[:10]:
        print(
            f"      {name}: {conf:.3f} at "
            f"[{xyxy[0]:.0f},{xyxy[1]:.0f},{xyxy[2]:.0f},{xyxy[3]:.0f}]"
        )

    # ── Summary ───────────────────────────────────────────────────────────
    total_fwd = fwd1_t + fwd2_t

    print(f"\n{'=' * 70}")
    print("RESULTS COMPARISON")
    print(f"{'=' * 70}")
    print(f"Ultralytics (float32 CPU):     {len(ultra_dets)} detections")
    print(f"CPU reference (fused bf16):    {n_cpu} detections")
    print(f"NPU pipeline  (fused bf16):    {n_npu} detections")
    print()
    print(f"NPU Timing:")
    print(
        f"  XCLBIN 1 (BB+Neck):  {n_pdis_1} PDIs  "
        f"prep={prep1_t:.1f}s  fwd={fwd1_t:.3f}s"
    )
    print(
        f"  XCLBIN 2 (Detect):   {n_pdis_2} PDIs  "
        f"prep={prep2_t:.1f}s  fwd={fwd2_t:.3f}s"
    )
    print(f"  Post-processing:     {pp_t:.4f}s")
    print(f"  Total forward:       {total_fwd:.3f}s")
    print()

    # Show NPU vs CPU feature map agreement
    print("NPU vs CPU feature map agreement (max abs diff):")
    for scale_name, npu_reg, npu_cls, cpu_reg, cpu_cls in zip(
        ["P3", "P4", "P5"],
        reg_list,
        cls_list,
        cpu_result["reg"],
        cpu_result["cls"],
    ):
        reg_diff = (npu_reg.float() - cpu_reg.float()).abs().max().item()
        cls_diff = (npu_cls.float() - cpu_cls.float()).abs().max().item()
        print(f"  {scale_name}: reg_diff={reg_diff:.4f}  cls_diff={cls_diff:.4f}")

    print()
    all_pass = bb_neck_pass and detect_pass
    if all_pass:
        print("ALL PASS -- YOLOv8n pretrained inference on NPU completed successfully")
    else:
        print("FAIL -- see errors above")
        raise SystemExit(1)
