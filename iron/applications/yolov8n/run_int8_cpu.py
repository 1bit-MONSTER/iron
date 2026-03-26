#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Verify YOLOv8n int8 quantization on CPU.

Runs the full YOLOv8n model with int8 quantized weights and activations
on CPU to verify that int8 quantization preserves enough signal for
object detection before committing to NPU implementation.

Two-pass approach:
  1. Calibration pass: run float model, record activation scales per layer
  2. Int8 pass: quantize everything, simulate int8 MAC + right-shift

Usage:
    python3 iron/applications/yolov8n/run_int8_cpu.py [--image PATH]
"""

import argparse
import time
import urllib.request
from pathlib import Path

import torch
import torch.nn.functional as F

from iron.applications.yolov8n.model_prep import fuse_conv_bn
from iron.applications.yolov8n.postprocess import YOLOv8nPostProcess
from iron.applications.yolov8n.quantize import Int8Quantizer
from iron.applications.yolov8n.run_pretrained import (
    COCO_NAMES,
    preprocess_image,
    run_ultralytics_reference,
)


class Int8YOLOv8nCPU:
    """Full YOLOv8n inference in int8 on CPU.

    Two-phase execution:
      1. calibrate(): run float model to determine activation scales
      2. forward_int8(): run with int8 weights and quantized activations
    """

    def __init__(self, model_path="yolov8n.pt"):
        from ultralytics import YOLO

        self.model = YOLO(model_path)
        self.m = self.model.model.model  # Sequential of modules
        self.quantizer = Int8Quantizer()

        # Fuse all Conv+BN and store float weights
        self.float_weights = {}
        self._fuse_all()

        # Quantize weights to int8
        self.int8_weights = self.quantizer.quantize_yolov8n_weights(self.model)

        # Activation scales filled during calibration
        self.act_scales = {}

    def _fuse_all(self):
        """Fuse Conv+BN for all layers, store float weights."""
        m = self.m

        def fuse(module, name):
            w, b = fuse_conv_bn(module.conv, module.bn)
            self.float_weights[name] = (w.float(), b.float())

        def fuse_c2f(c2f, prefix):
            fuse(c2f.cv1, f"{prefix}.cv1")
            for i, bn in enumerate(c2f.m):
                fuse(bn.cv1, f"{prefix}.bn{i}.cv1")
                fuse(bn.cv2, f"{prefix}.bn{i}.cv2")
            fuse(c2f.cv2, f"{prefix}.cv2")

        # Backbone
        fuse(m[0], "l0")
        # Pad L0 weights from [16, 3, 3, 3] to [16, 8, 3, 3]
        w0, b0 = self.float_weights["l0"]
        w0_padded = F.pad(w0, (0, 0, 0, 0, 0, 5))
        self.float_weights["l0"] = (w0_padded, b0)
        fuse(m[1], "l1")
        fuse_c2f(m[2], "l2")
        fuse(m[3], "l3")
        fuse_c2f(m[4], "l4")
        fuse(m[5], "l5")
        fuse_c2f(m[6], "l6")
        fuse(m[7], "l7")
        fuse_c2f(m[8], "l8")
        fuse(m[9].cv1, "l9.cv1")
        fuse(m[9].cv2, "l9.cv2")

        # Neck
        fuse_c2f(m[12], "l12")
        fuse_c2f(m[15], "l15")
        fuse(m[16], "l16")
        fuse_c2f(m[18], "l18")
        fuse(m[19], "l19")
        fuse_c2f(m[21], "l21")

        # Detect head - CBS layers
        det = m[22]
        for branch_attr, prefix in [("cv2", "reg"), ("cv3", "cls")]:
            for scale_idx, scale_name in enumerate(["p3", "p4", "p5"]):
                seq = getattr(det, branch_attr)[scale_idx]
                fuse(seq[0], f"det.{prefix}_{scale_name}.cv1")
                fuse(seq[1], f"det.{prefix}_{scale_name}.cv2")
                # seq[2] is bare Conv2d (no BN)
                w = seq[2].weight.float()
                b = seq[2].bias.float()
                self.float_weights[f"det.{prefix}_{scale_name}.cv3"] = (w, b)

    def calibrate(self, img_tensor):
        """Run float model forward, record activation scales at each layer output.

        Args:
            img_tensor: [1, 3, H, W] bfloat16 tensor (same as normal inference).

        Returns:
            dict of intermediate feature maps (for debugging).
        """
        x = img_tensor.float()

        def conv_silu(x, name, stride=1):
            w, b = self.float_weights[name]
            kH = w.shape[2]
            out = F.conv2d(x, w, b, stride=stride, padding=kH // 2)
            out = F.silu(out)
            self.act_scales[name] = out.abs().max().item() / 127.0
            return out

        def conv_no_act(x, name, stride=1):
            w, b = self.float_weights[name]
            kH = w.shape[2]
            out = F.conv2d(x, w, b, stride=stride, padding=kH // 2)
            self.act_scales[name] = out.abs().max().item() / 127.0
            return out

        def run_c2f(x, prefix, shortcut=True):
            x = conv_silu(x, f"{prefix}.cv1")
            chunks = x.chunk(2, dim=1)
            outputs = [chunks[0], chunks[1]]
            for i in range(len([k for k in self.float_weights if k.startswith(f"{prefix}.bn") and k.endswith(".cv1")])):
                inp = outputs[-1]
                y = conv_silu(inp, f"{prefix}.bn{i}.cv1")
                y = conv_silu(y, f"{prefix}.bn{i}.cv2")
                if shortcut:
                    y = y + inp
                outputs.append(y)
            cat = torch.cat(outputs, dim=1)
            return conv_silu(cat, f"{prefix}.cv2")

        # Record input scale
        x_padded = F.pad(x, (0, 0, 0, 0, 0, 5))
        self.act_scales["input"] = x_padded.abs().max().item() / 127.0

        # Backbone
        x = conv_silu(x_padded, "l0", stride=2)
        x = conv_silu(x, "l1", stride=2)
        x = run_c2f(x, "l2")
        x = conv_silu(x, "l3", stride=2)
        p3 = run_c2f(x, "l4")
        x = conv_silu(p3, "l5", stride=2)
        p4 = run_c2f(x, "l6")
        x = conv_silu(p4, "l7", stride=2)
        x = run_c2f(x, "l8")

        # SPPF
        x = conv_silu(x, "l9.cv1")
        y1 = F.max_pool2d(x, 5, stride=1, padding=2)
        y2 = F.max_pool2d(y1, 5, stride=1, padding=2)
        y3 = F.max_pool2d(y2, 5, stride=1, padding=2)
        x = torch.cat([x, y1, y2, y3], dim=1)
        p5 = conv_silu(x, "l9.cv2")

        # Neck FPN up
        x = F.interpolate(p5, scale_factor=2, mode="nearest")
        x = torch.cat([x, p4], dim=1)
        l12_out = run_c2f(x, "l12", shortcut=False)
        x = F.interpolate(l12_out, scale_factor=2, mode="nearest")
        x = torch.cat([x, p3], dim=1)
        det_p3 = run_c2f(x, "l15", shortcut=False)

        # Neck PAN down
        x = conv_silu(det_p3, "l16", stride=2)
        x = torch.cat([x, l12_out], dim=1)
        det_p4 = run_c2f(x, "l18", shortcut=False)
        x = conv_silu(det_p4, "l19", stride=2)
        x = torch.cat([x, p5], dim=1)
        det_p5 = run_c2f(x, "l21", shortcut=False)

        # Detect head
        def run_det_branch(x, prefix):
            x = conv_silu(x, f"det.{prefix}.cv1")
            x = conv_silu(x, f"det.{prefix}.cv2")
            x = conv_no_act(x, f"det.{prefix}.cv3")
            return x

        results = {}
        for prefix, feat in [
            ("reg_p3", det_p3), ("cls_p3", det_p3),
            ("reg_p4", det_p4), ("cls_p4", det_p4),
            ("reg_p5", det_p5), ("cls_p5", det_p5),
        ]:
            results[prefix] = run_det_branch(feat, prefix)

        print(f"    Calibrated {len(self.act_scales)} activation scales")
        return results

    def forward_int8(self, img_tensor):
        """Run int8-simulated forward pass.

        For each conv layer:
          1. Quantize input to int8
          2. int8 × int8 MAC → int32
          3. Dequantize int32 result to float (using w_scale * act_scale)
          4. Add float bias
          5. Apply activation (SiLU or none)
          6. The float output becomes input to next layer

        This is the "fake quantization" approach — we simulate int8 arithmetic
        but keep intermediate float precision for bias/activation/concat/upsample.

        Args:
            img_tensor: [1, 3, H, W] bfloat16 tensor.

        Returns:
            dict with 'reg': [3 tensors], 'cls': [3 tensors].
        """

        def get_int8_weight(layer_name):
            """Look up int8 weight and scale from the quantized weight dict."""
            # Map layer names to the weight dict structure
            return self._lookup_weight(layer_name)

        def int8_cbs(x_float, layer_name, stride=1):
            """CBS layer: int8 conv → dequant → bias → SiLU."""
            w_int8, w_scale, bias = get_int8_weight(layer_name)
            kH = w_int8.shape[2]
            pad = kH // 2

            # Quantize activation to int8
            act_scale = self.act_scales.get(
                self._prev_layer_name(layer_name),
                x_float.abs().max().item() / 127.0,
            )
            if act_scale == 0:
                act_scale = 1.0
            x_int8 = torch.clamp(
                torch.round(x_float / act_scale), -128, 127
            ).to(torch.int8)

            # int8 × int8 MAC → int32
            out_int32 = F.conv2d(
                x_int8.float(), w_int8.float(),
                bias=None, stride=stride, padding=pad,
            ).to(torch.int32)

            # Dequantize: int32 * (w_scale * act_scale)
            combined_scale = w_scale * act_scale
            out_float = out_int32.float() * combined_scale

            # Add bias in float domain
            out_float = out_float + bias.view(1, -1, 1, 1)

            # SiLU activation
            out_float = F.silu(out_float)
            return out_float

        def int8_conv_no_act(x_float, layer_name, stride=1):
            """Conv without activation: int8 conv → dequant → bias."""
            w_int8, w_scale, bias = get_int8_weight(layer_name)
            kH = w_int8.shape[2]
            pad = kH // 2

            act_scale = self.act_scales.get(
                self._prev_layer_name(layer_name),
                x_float.abs().max().item() / 127.0,
            )
            if act_scale == 0:
                act_scale = 1.0
            x_int8 = torch.clamp(
                torch.round(x_float / act_scale), -128, 127
            ).to(torch.int8)

            out_int32 = F.conv2d(
                x_int8.float(), w_int8.float(),
                bias=None, stride=stride, padding=pad,
            ).to(torch.int32)

            combined_scale = w_scale * act_scale
            out_float = out_int32.float() * combined_scale
            out_float = out_float + bias.view(1, -1, 1, 1)
            return out_float

        def run_c2f_int8(x, prefix, shortcut=True):
            x = int8_cbs(x, f"{prefix}.cv1")
            chunks = x.chunk(2, dim=1)
            outputs = [chunks[0], chunks[1]]
            n_bottlenecks = len([k for k in self.float_weights if k.startswith(f"{prefix}.bn") and k.endswith(".cv1")])
            for i in range(n_bottlenecks):
                inp = outputs[-1]
                y = int8_cbs(inp, f"{prefix}.bn{i}.cv1")
                y = int8_cbs(y, f"{prefix}.bn{i}.cv2")
                if shortcut:
                    y = y + inp
                outputs.append(y)
            cat = torch.cat(outputs, dim=1)
            return int8_cbs(cat, f"{prefix}.cv2")

        # Forward pass
        x = img_tensor.float()
        x_padded = F.pad(x, (0, 0, 0, 0, 0, 5))

        # Backbone
        x = int8_cbs(x_padded, "l0", stride=2)
        x = int8_cbs(x, "l1", stride=2)
        x = run_c2f_int8(x, "l2")
        x = int8_cbs(x, "l3", stride=2)
        p3 = run_c2f_int8(x, "l4")
        x = int8_cbs(p3, "l5", stride=2)
        p4 = run_c2f_int8(x, "l6")
        x = int8_cbs(p4, "l7", stride=2)
        x = run_c2f_int8(x, "l8")

        # SPPF (maxpool in float, conv in int8)
        x = int8_cbs(x, "l9.cv1")
        y1 = F.max_pool2d(x, 5, stride=1, padding=2)
        y2 = F.max_pool2d(y1, 5, stride=1, padding=2)
        y3 = F.max_pool2d(y2, 5, stride=1, padding=2)
        x = torch.cat([x, y1, y2, y3], dim=1)
        p5 = int8_cbs(x, "l9.cv2")

        # Neck FPN up-path
        x = F.interpolate(p5, scale_factor=2, mode="nearest")
        x = torch.cat([x, p4], dim=1)
        l12_out = run_c2f_int8(x, "l12", shortcut=False)
        x = F.interpolate(l12_out, scale_factor=2, mode="nearest")
        x = torch.cat([x, p3], dim=1)
        det_p3 = run_c2f_int8(x, "l15", shortcut=False)

        # Neck PAN down-path
        x = int8_cbs(det_p3, "l16", stride=2)
        x = torch.cat([x, l12_out], dim=1)
        det_p4 = run_c2f_int8(x, "l18", shortcut=False)
        x = int8_cbs(det_p4, "l19", stride=2)
        x = torch.cat([x, p5], dim=1)
        det_p5 = run_c2f_int8(x, "l21", shortcut=False)

        # Detect head
        def run_det_branch_int8(x, prefix):
            x = int8_cbs(x, f"det.{prefix}.cv1")
            x = int8_cbs(x, f"det.{prefix}.cv2")
            x = int8_conv_no_act(x, f"det.{prefix}.cv3")
            return x

        reg_p3 = run_det_branch_int8(det_p3, "reg_p3")
        cls_p3 = run_det_branch_int8(det_p3, "cls_p3")
        reg_p4 = run_det_branch_int8(det_p4, "reg_p4")
        cls_p4 = run_det_branch_int8(det_p4, "cls_p4")
        reg_p5 = run_det_branch_int8(det_p5, "reg_p5")
        cls_p5 = run_det_branch_int8(det_p5, "cls_p5")

        return {
            "reg": [reg_p3, reg_p4, reg_p5],
            "cls": [cls_p3, cls_p4, cls_p5],
        }

    def _lookup_weight(self, layer_name):
        """Look up int8 weight, scale, and float bias for a layer.

        Returns:
            (weight_int8, weight_scale, bias_float) tuple.
        """
        wts = self.int8_weights

        # Direct CBS layers
        cbs_map = {
            "l0": ("backbone", "l0"),
            "l1": ("backbone", "l1"),
            "l3": ("backbone", "l3"),
            "l5": ("backbone", "l5"),
            "l7": ("backbone", "l7"),
            "l16": ("neck", "l16"),
            "l19": ("neck", "l19"),
        }
        if layer_name in cbs_map:
            section, key = cbs_map[layer_name]
            d = wts[section][key]
            return d["weight"], d["weight_scale"], d["bias"]

        # SPPF layers
        if layer_name == "l9.cv1":
            d = wts["backbone"]["l9"]
            return d["cv1_weight"], d["cv1_scale"], d["cv1_bias"]
        if layer_name == "l9.cv2":
            d = wts["backbone"]["l9"]
            return d["cv2_weight"], d["cv2_scale"], d["cv2_bias"]

        # C2f layers: l2, l4, l6, l8, l12, l15, l18, l21
        c2f_layers = {
            "l2": ("backbone", "l2"),
            "l4": ("backbone", "l4"),
            "l6": ("backbone", "l6"),
            "l8": ("backbone", "l8"),
            "l12": ("neck", "l12"),
            "l15": ("neck", "l15"),
            "l18": ("neck", "l18"),
            "l21": ("neck", "l21"),
        }
        for c2f_prefix, (section, key) in c2f_layers.items():
            d = wts[section][key]
            if layer_name == f"{c2f_prefix}.cv1":
                return d["cv1_weight"], d["cv1_scale"], d["cv1_bias"]
            if layer_name == f"{c2f_prefix}.cv2":
                return d["cv2_weight"], d["cv2_scale"], d["cv2_bias"]
            # Bottleneck layers
            for i, bn_data in enumerate(d["bottlenecks"]):
                w1, b1, w2, b2, s1, s2 = bn_data
                if layer_name == f"{c2f_prefix}.bn{i}.cv1":
                    return w1, s1, b1
                if layer_name == f"{c2f_prefix}.bn{i}.cv2":
                    return w2, s2, b2

        # Detect head layers
        det_branches = ["reg_p3", "reg_p4", "reg_p5", "cls_p3", "cls_p4", "cls_p5"]
        for branch in det_branches:
            d = wts["detect"][branch]
            if layer_name == f"det.{branch}.cv1":
                return d["cv1_weight"], d["cv1_scale"], d["cv1_bias"]
            if layer_name == f"det.{branch}.cv2":
                return d["cv2_weight"], d["cv2_scale"], d["cv2_bias"]
            if layer_name == f"det.{branch}.cv3":
                return d["cv3_weight"], d["cv3_scale"], d["cv3_bias"]

        raise KeyError(f"Unknown layer: {layer_name}")

    def _prev_layer_name(self, layer_name):
        """Get the layer name whose output feeds into this layer.

        Used to look up activation scale for quantizing the input to this layer.
        For the first layer, returns 'input'.
        """
        # Build a simple predecessor map based on the network topology
        pred = {
            "l0": "input",
            "l1": "l0",
            "l2.cv1": "l1",
            "l3": "l2.cv2",
            "l4.cv1": "l3",
            "l5": "l4.cv2",
            "l6.cv1": "l5",
            "l7": "l6.cv2",
            "l8.cv1": "l7",
            "l9.cv1": "l8.cv2",
            "l9.cv2": "l9.cv1",  # After concat, use cv1's scale as approx
            "l16": "l15.cv2",
            "l19": "l18.cv2",
        }

        if layer_name in pred:
            return pred[layer_name]

        # For C2f internal layers, use the previous internal layer
        for c2f_prefix in ["l2", "l4", "l6", "l8", "l12", "l15", "l18", "l21"]:
            if layer_name == f"{c2f_prefix}.cv2":
                return f"{c2f_prefix}.cv1"  # Approximation: concat output ~ cv1 scale
            if layer_name.startswith(f"{c2f_prefix}.bn"):
                # bn0.cv1 input is from cv1 output (second chunk)
                # bn0.cv2 input is from bn0.cv1 output
                if layer_name.endswith(".cv1"):
                    parts = layer_name.split(".")
                    bn_idx = int(parts[1].replace("bn", ""))
                    if bn_idx == 0:
                        return f"{c2f_prefix}.cv1"
                    else:
                        return f"{c2f_prefix}.bn{bn_idx - 1}.cv2"
                elif layer_name.endswith(".cv2"):
                    parts = layer_name.split(".")
                    bn_name = parts[1]
                    return f"{c2f_prefix}.{bn_name}.cv1"

        # Detect head predecessors
        for branch in ["reg_p3", "cls_p3", "reg_p4", "cls_p4", "reg_p5", "cls_p5"]:
            if layer_name == f"det.{branch}.cv1":
                # Input is from neck feature map
                if "p3" in branch:
                    return "l15.cv2"
                elif "p4" in branch:
                    return "l18.cv2"
                else:
                    return "l21.cv2"
            if layer_name == f"det.{branch}.cv2":
                return f"det.{branch}.cv1"
            if layer_name == f"det.{branch}.cv3":
                return f"det.{branch}.cv2"

        # Neck C2f input predecessors
        if layer_name == "l12.cv1":
            return "l9.cv2"  # After concat with p4, approximate
        if layer_name == "l15.cv1":
            return "l12.cv2"  # After concat with p3, approximate
        if layer_name == "l18.cv1":
            return "l16"  # After concat with l12_out, approximate
        if layer_name == "l21.cv1":
            return "l19"  # After concat with p5, approximate

        # Fallback: use the layer name itself (will trigger dynamic scale computation)
        return layer_name


def main():
    parser = argparse.ArgumentParser(
        description="Verify YOLOv8n int8 quantization on CPU"
    )
    parser.add_argument("--image", default="test_bus.jpg", help="Path to test image")
    parser.add_argument("--model", default="yolov8n.pt", help="Path to YOLOv8n weights")
    args = parser.parse_args()

    # Download test image if needed
    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Downloading test image to {image_path}...")
        urllib.request.urlretrieve(
            "https://ultralytics.com/images/bus.jpg", str(image_path)
        )

    print("=" * 70)
    print("YOLOv8n INT8 CPU Verification")
    print("=" * 70)

    # Step 1: Load model and quantize weights
    print("\n[1] Loading model and quantizing weights...")
    t0 = time.time()
    runner = Int8YOLOv8nCPU(args.model)
    print(f"    Weight quantization: {time.time() - t0:.1f}s")
    print(f"    Quantized {len(runner.quantizer.weight_scales)} weight tensors")

    # Print weight scale stats
    w_scales = list(runner.quantizer.weight_scales.values())
    print(f"    Weight scale range: [{min(w_scales):.6f}, {max(w_scales):.6f}]")

    # Step 2: Preprocess image
    print(f"\n[2] Preprocessing image: {image_path}")
    img_tensor = preprocess_image(image_path, img_size=640)
    print(f"    Input tensor: {img_tensor.shape} {img_tensor.dtype}")

    # Step 3: Calibration pass (float model)
    print("\n[3] Calibration pass (float model to determine activation scales)...")
    t0 = time.time()
    float_result = runner.calibrate(img_tensor)
    print(f"    Calibration: {time.time() - t0:.2f}s")

    # Post-process float calibration result for comparison
    pp = YOLOv8nPostProcess(conf_thres=0.25, iou_thres=0.45)
    reg_float = [
        float_result["reg_p3"].unsqueeze(0) if float_result["reg_p3"].dim() == 3 else float_result["reg_p3"],
        float_result["reg_p4"].unsqueeze(0) if float_result["reg_p4"].dim() == 3 else float_result["reg_p4"],
        float_result["reg_p5"].unsqueeze(0) if float_result["reg_p5"].dim() == 3 else float_result["reg_p5"],
    ]
    cls_float = [
        float_result["cls_p3"].unsqueeze(0) if float_result["cls_p3"].dim() == 3 else float_result["cls_p3"],
        float_result["cls_p4"].unsqueeze(0) if float_result["cls_p4"].dim() == 3 else float_result["cls_p4"],
        float_result["cls_p5"].unsqueeze(0) if float_result["cls_p5"].dim() == 3 else float_result["cls_p5"],
    ]
    float_detections = pp(reg_float, cls_float)
    n_float = len(float_detections["boxes"])
    print(f"    Float (fused weights) detections: {n_float}")
    if n_float > 0:
        for i in range(min(10, n_float)):
            box = float_detections["boxes"][i].tolist()
            score = float_detections["scores"][i].item()
            label = float_detections["labels"][i].item()
            name = COCO_NAMES[label] if label < len(COCO_NAMES) else f"class_{label}"
            print(f"      {name}: {score:.3f} at [{box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f}]")

    # Print activation scale stats
    act_scales = list(runner.act_scales.values())
    print(f"\n    Activation scales: {len(act_scales)} layers")
    print(f"    Act scale range: [{min(act_scales):.6f}, {max(act_scales):.6f}]")

    # Step 4: Int8 forward pass
    print("\n[4] Int8 forward pass (quantized weights + quantized activations)...")
    t0 = time.time()
    int8_result = runner.forward_int8(img_tensor)
    int8_time = time.time() - t0
    print(f"    Int8 forward: {int8_time:.2f}s")

    # Verify output shapes and finiteness
    for name, tensor in [
        ("reg_p3", int8_result["reg"][0]),
        ("cls_p3", int8_result["cls"][0]),
        ("reg_p4", int8_result["reg"][1]),
        ("cls_p4", int8_result["cls"][1]),
        ("reg_p5", int8_result["reg"][2]),
        ("cls_p5", int8_result["cls"][2]),
    ]:
        finite = torch.isfinite(tensor).all().item()
        print(f"    {name}: {tensor.shape} finite={finite} range=[{tensor.min():.2f}, {tensor.max():.2f}]")

    # Step 5: Post-process int8 results
    print("\n[5] Post-processing int8 results (DFL + NMS)...")
    int8_detections = pp(int8_result["reg"], int8_result["cls"])
    n_int8 = len(int8_detections["boxes"])
    print(f"    Int8 detections (conf>0.25): {n_int8}")
    if n_int8 > 0:
        for i in range(min(10, n_int8)):
            box = int8_detections["boxes"][i].tolist()
            score = int8_detections["scores"][i].item()
            label = int8_detections["labels"][i].item()
            name = COCO_NAMES[label] if label < len(COCO_NAMES) else f"class_{label}"
            print(f"      {name}: {score:.3f} at [{box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f}]")

    # Try lower confidence threshold
    pp_low = YOLOv8nPostProcess(conf_thres=0.10, iou_thres=0.45)
    int8_dets_low = pp_low(int8_result["reg"], int8_result["cls"])
    n_int8_low = len(int8_dets_low["boxes"])
    print(f"    Int8 detections (conf>0.10): {n_int8_low}")
    if n_int8_low > 0:
        for i in range(min(10, n_int8_low)):
            box = int8_dets_low["boxes"][i].tolist()
            score = int8_dets_low["scores"][i].item()
            label = int8_dets_low["labels"][i].item()
            name = COCO_NAMES[label] if label < len(COCO_NAMES) else f"class_{label}"
            print(f"      {name}: {score:.3f} at [{box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f}]")

    # Score distribution diagnostics
    cls_flat = torch.cat(
        [c.float().squeeze(0).permute(1, 2, 0).reshape(-1, 80) for c in int8_result["cls"]],
        dim=0,
    )
    max_scores = cls_flat.sigmoid().max(dim=1)[0]
    print(f"\n    Int8 cls score stats:")
    print(f"      max={max_scores.max():.4f}")
    print(f"      mean={max_scores.mean():.4f}")
    print(f"      >0.25: {(max_scores > 0.25).sum().item()}")
    print(f"      >0.10: {(max_scores > 0.10).sum().item()}")
    print(f"      >0.05: {(max_scores > 0.05).sum().item()}")

    # Step 6: Ultralytics reference
    print("\n[6] Ultralytics reference (native float32 CPU)...")
    ultra_dets = run_ultralytics_reference(image_path, args.model)
    print(f"    Ultralytics detections: {len(ultra_dets)}")
    for name, conf, xyxy in ultra_dets[:10]:
        print(f"      {name}: {conf:.3f} at [{xyxy[0]:.0f},{xyxy[1]:.0f},{xyxy[2]:.0f},{xyxy[3]:.0f}]")

    # Step 7: Int8 vs Float feature map comparison
    print("\n[7] Int8 vs Float feature map comparison:")
    for scale_name, int8_reg, int8_cls, float_reg_name, float_cls_name in [
        ("P3", int8_result["reg"][0], int8_result["cls"][0], "reg_p3", "cls_p3"),
        ("P4", int8_result["reg"][1], int8_result["cls"][1], "reg_p4", "cls_p4"),
        ("P5", int8_result["reg"][2], int8_result["cls"][2], "reg_p5", "cls_p5"),
    ]:
        float_reg = float_result[float_reg_name]
        float_cls = float_result[float_cls_name]
        reg_diff = (int8_reg.float() - float_reg.float()).abs().max().item()
        cls_diff = (int8_cls.float() - float_cls.float()).abs().max().item()
        reg_corr = torch.corrcoef(
            torch.stack([int8_reg.float().flatten(), float_reg.float().flatten()])
        )[0, 1].item()
        cls_corr = torch.corrcoef(
            torch.stack([int8_cls.float().flatten(), float_cls.float().flatten()])
        )[0, 1].item()
        print(f"    {scale_name}: reg_diff={reg_diff:.4f} reg_corr={reg_corr:.4f}  "
              f"cls_diff={cls_diff:.4f} cls_corr={cls_corr:.4f}")

    # Summary
    print(f"\n{'=' * 70}")
    print("RESULTS COMPARISON")
    print(f"{'=' * 70}")
    print(f"Ultralytics (float32 CPU):     {len(ultra_dets)} detections")
    print(f"Float (fused weights, f32):    {n_float} detections")
    print(f"Int8 simulation (CPU):         {n_int8} detections (conf>0.25)")
    print(f"Int8 simulation (CPU):         {n_int8_low} detections (conf>0.10)")
    print()

    if n_int8 >= 2:
        print("PASS: Int8 quantization preserves enough signal for detection")
        print("      Proceed with NPU int8 implementation")
    elif n_int8_low >= 2:
        print("MARGINAL: Int8 detections exist but at lower confidence")
        print("          Consider per-channel quantization or adjusted scales")
    else:
        print("FAIL: Int8 quantization destroys too much signal")
        print("      Need to investigate: per-channel scales, mixed precision, etc.")


if __name__ == "__main__":
    main()
