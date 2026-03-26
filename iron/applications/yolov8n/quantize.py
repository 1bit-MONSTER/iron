# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Symmetric per-tensor int8 quantization utilities for YOLOv8n NPU inference.

The NPU int8 kernel performs MAC in int32 and requantizes via right-shift:

    output_int32 = sum(input_int8 * weight_int8)
    output_int8  = (output_int32 + rounding) >> shift

The shift encodes the combined scale ratio:

    shift = round(log2(1 / (weight_scale * act_scale / output_scale)))

This module provides:
- Per-tensor symmetric quantization/dequantization
- Shift computation for the NPU requantization step
- Full YOLOv8n weight quantization from ultralytics models
- Calibration-based activation scale determination
"""

import math

import torch
import torch.nn.functional as F


class Int8Quantizer:
    """Symmetric per-tensor int8 quantization for YOLOv8n."""

    def __init__(self):
        self.weight_scales = {}  # layer_name -> float scale
        self.act_scales = {}  # layer_name -> float scale

    @staticmethod
    def quantize_tensor(tensor_float, scale=None):
        """Quantize a float tensor to int8 using symmetric per-tensor scaling.

        Args:
            tensor_float: Float tensor to quantize.
            scale: Scale factor. If None, derived from tensor's max absolute value.

        Returns:
            (int8_tensor, scale_factor) tuple.
        """
        if scale is None:
            max_abs = tensor_float.abs().max().item()
            scale = max_abs / 127.0 if max_abs != 0 else 1.0
        int8_tensor = torch.clamp(torch.round(tensor_float / scale), -128, 127).to(
            torch.int8
        )
        return int8_tensor, scale

    @staticmethod
    def dequantize_tensor(int8_tensor, scale):
        """Dequantize an int8 tensor back to float.

        Args:
            int8_tensor: Int8 tensor.
            scale: Scale factor used during quantization.

        Returns:
            Float tensor.
        """
        return int8_tensor.float() * scale

    @staticmethod
    def compute_shift(weight_scale, act_scale, output_scale):
        """Compute right-shift bits for the NPU requantization kernel.

        The kernel does: output_int8 = (int32_mac + rounding) >> shift

        The combined float scale is weight_scale * act_scale, and the output
        needs to be in output_scale units, so:

            int32_mac * (w_scale * a_scale) / o_scale ≈ result * 2^(-shift)
            shift = round(log2(o_scale / (w_scale * a_scale)))

        Args:
            weight_scale: Per-tensor weight scale factor.
            act_scale: Per-tensor activation scale factor.
            output_scale: Per-tensor output scale factor.

        Returns:
            Shift value clamped to [0, 31].
        """
        combined = weight_scale * act_scale / output_scale
        shift = round(math.log2(1.0 / combined))
        return max(0, min(31, shift))

    def quantize_conv_layer(self, weight_float, bias_float, layer_name):
        """Quantize a single conv layer's weights and bias.

        Weights are quantized to int8. Bias is kept in int32 (standard practice:
        bias_scale = weight_scale * act_scale, quantized bias is int32).

        Args:
            weight_float: Float weight tensor [O, I, kH, kW].
            bias_float: Float bias tensor [O].
            layer_name: Name for scale tracking.

        Returns:
            dict with 'weight' (int8), 'bias' (float32), 'weight_scale' (float).
        """
        weight_int8, w_scale = self.quantize_tensor(weight_float.float())
        self.weight_scales[layer_name] = w_scale
        return {
            "weight": weight_int8,
            "bias": bias_float.float(),
            "weight_scale": w_scale,
        }

    def quantize_yolov8n_weights(self, ultralytics_model):
        """Quantize all YOLOv8n weights from an ultralytics model.

        Walks the model, fuses Conv+BN, and quantizes each layer to int8.
        Returns a weight dict with the same structure as
        ``run_pretrained.extract_pretrained_weights`` but with int8 weights
        and scale metadata.

        Args:
            ultralytics_model: An ultralytics YOLO model instance.

        Returns:
            dict with 'backbone', 'neck', 'detect' sub-dicts, each layer
            containing 'weight' (int8), 'bias' (float32), 'weight_scale'.
        """
        from iron.applications.yolov8n.model_prep import fuse_conv_bn

        m = ultralytics_model.model.model  # Sequential of modules

        def _fuse_and_quantize(module, name):
            w, b = fuse_conv_bn(module.conv, module.bn)
            return self.quantize_conv_layer(w, b, name)

        def _quantize_c2f(c2f_module, prefix):
            result = {}
            cv1_q = _fuse_and_quantize(c2f_module.cv1, f"{prefix}.cv1")
            result["cv1_weight"] = cv1_q["weight"]
            result["cv1_bias"] = cv1_q["bias"]
            result["cv1_scale"] = cv1_q["weight_scale"]

            bottlenecks = []
            for i, bn in enumerate(c2f_module.m):
                bn_cv1 = _fuse_and_quantize(bn.cv1, f"{prefix}.bn{i}.cv1")
                bn_cv2 = _fuse_and_quantize(bn.cv2, f"{prefix}.bn{i}.cv2")
                bottlenecks.append(
                    (
                        bn_cv1["weight"],
                        bn_cv1["bias"],
                        bn_cv2["weight"],
                        bn_cv2["bias"],
                        bn_cv1["weight_scale"],
                        bn_cv2["weight_scale"],
                    )
                )
            result["bottlenecks"] = bottlenecks

            cv2_q = _fuse_and_quantize(c2f_module.cv2, f"{prefix}.cv2")
            result["cv2_weight"] = cv2_q["weight"]
            result["cv2_bias"] = cv2_q["bias"]
            result["cv2_scale"] = cv2_q["weight_scale"]
            return result

        def _quantize_sppf(sppf_module, prefix):
            cv1_q = _fuse_and_quantize(sppf_module.cv1, f"{prefix}.cv1")
            cv2_q = _fuse_and_quantize(sppf_module.cv2, f"{prefix}.cv2")
            return {
                "cv1_weight": cv1_q["weight"],
                "cv1_bias": cv1_q["bias"],
                "cv1_scale": cv1_q["weight_scale"],
                "cv2_weight": cv2_q["weight"],
                "cv2_bias": cv2_q["bias"],
                "cv2_scale": cv2_q["weight_scale"],
            }

        def _quantize_detect_branch(det_module, branch_attr, scale_idx, prefix):
            seq = getattr(det_module, branch_attr)[scale_idx]
            cv1_q = _fuse_and_quantize(seq[0], f"{prefix}.cv1")
            cv2_q = _fuse_and_quantize(seq[1], f"{prefix}.cv2")
            # seq[2] is bare nn.Conv2d (no BN)
            cv3_q = self.quantize_conv_layer(
                seq[2].weight, seq[2].bias, f"{prefix}.cv3"
            )
            return {
                "cv1_weight": cv1_q["weight"],
                "cv1_bias": cv1_q["bias"],
                "cv1_scale": cv1_q["weight_scale"],
                "cv2_weight": cv2_q["weight"],
                "cv2_bias": cv2_q["bias"],
                "cv2_scale": cv2_q["weight_scale"],
                "cv3_weight": cv3_q["weight"],
                "cv3_bias": cv3_q["bias"],
                "cv3_scale": cv3_q["weight_scale"],
            }

        # ---- Backbone ----
        backbone = {}

        l0_q = _fuse_and_quantize(m[0], "backbone.l0")
        # Pad input channels 3 -> 8
        l0_w_float = self.dequantize_tensor(l0_q["weight"], l0_q["weight_scale"])
        l0_w_padded = F.pad(l0_w_float, (0, 0, 0, 0, 0, 5))
        l0_w_int8, l0_scale = self.quantize_tensor(l0_w_padded)
        self.weight_scales["backbone.l0"] = l0_scale
        backbone["l0"] = {
            "weight": l0_w_int8,
            "bias": l0_q["bias"],
            "weight_scale": l0_scale,
        }

        backbone["l1"] = _fuse_and_quantize(m[1], "backbone.l1")
        backbone["l2"] = _quantize_c2f(m[2], "backbone.l2")
        backbone["l3"] = _fuse_and_quantize(m[3], "backbone.l3")
        backbone["l4"] = _quantize_c2f(m[4], "backbone.l4")
        backbone["l5"] = _fuse_and_quantize(m[5], "backbone.l5")
        backbone["l6"] = _quantize_c2f(m[6], "backbone.l6")
        backbone["l7"] = _fuse_and_quantize(m[7], "backbone.l7")
        backbone["l8"] = _quantize_c2f(m[8], "backbone.l8")
        backbone["l9"] = _quantize_sppf(m[9], "backbone.l9")

        # ---- Neck ----
        neck = {}
        neck["l12"] = _quantize_c2f(m[12], "neck.l12")
        neck["l15"] = _quantize_c2f(m[15], "neck.l15")
        neck["l16"] = _fuse_and_quantize(m[16], "neck.l16")
        neck["l18"] = _quantize_c2f(m[18], "neck.l18")
        neck["l19"] = _fuse_and_quantize(m[19], "neck.l19")
        neck["l21"] = _quantize_c2f(m[21], "neck.l21")

        # ---- Detect ----
        det = m[22]
        detect = {}
        detect["reg_p3"] = _quantize_detect_branch(det, "cv2", 0, "detect.reg_p3")
        detect["reg_p4"] = _quantize_detect_branch(det, "cv2", 1, "detect.reg_p4")
        detect["reg_p5"] = _quantize_detect_branch(det, "cv2", 2, "detect.reg_p5")
        detect["cls_p3"] = _quantize_detect_branch(det, "cv3", 0, "detect.cls_p3")
        detect["cls_p4"] = _quantize_detect_branch(det, "cv3", 1, "detect.cls_p4")
        detect["cls_p5"] = _quantize_detect_branch(det, "cv3", 2, "detect.cls_p5")

        return {"backbone": backbone, "neck": neck, "detect": detect}

    def quantize_activation(self, x_float, layer_name, calibration=True):
        """Quantize an activation tensor for a specific layer.

        During calibration (first pass), records the scale. On subsequent calls,
        uses the stored scale for consistent quantization.

        Args:
            x_float: Float activation tensor.
            layer_name: Layer identifier for scale lookup/storage.
            calibration: If True, (re-)compute and store the scale.

        Returns:
            (int8_tensor, scale_factor) tuple.
        """
        if calibration or layer_name not in self.act_scales:
            max_abs = x_float.abs().max().item()
            scale = max_abs / 127.0 if max_abs != 0 else 1.0
            self.act_scales[layer_name] = scale
        else:
            scale = self.act_scales[layer_name]

        return self.quantize_tensor(x_float, scale=scale)

    def get_layer_shift(self, layer_name, output_layer_name):
        """Compute the right-shift for a layer given stored scales.

        Args:
            layer_name: Layer whose weight_scale and act_scale to use.
            output_layer_name: Layer whose act_scale is the output scale.

        Returns:
            Shift value, or None if scales are not available.
        """
        w_scale = self.weight_scales.get(layer_name)
        a_scale = self.act_scales.get(layer_name)
        o_scale = self.act_scales.get(output_layer_name)
        if w_scale is None or a_scale is None or o_scale is None:
            return None
        return self.compute_shift(w_scale, a_scale, o_scale)


def calibrate_scales(model, sample_inputs, n_samples=10):
    """Run the float model on sample inputs to determine activation scales.

    Hooks into every Conv2d layer to record the max absolute activation value,
    then computes the optimal per-tensor quantization scale for each layer.

    Args:
        model: An ultralytics YOLO model (or any nn.Module).
        sample_inputs: Iterable of input tensors [1, 3, H, W].
        n_samples: Max number of samples to process.

    Returns:
        dict mapping layer_name -> scale (float).
    """
    act_max = {}
    hooks = []

    def _make_hook(name):
        def hook_fn(module, input, output):
            with torch.no_grad():
                val = output.abs().max().item()
                if name in act_max:
                    act_max[name] = max(act_max[name], val)
                else:
                    act_max[name] = val

        return hook_fn

    # Register hooks on all Conv2d layers
    pytorch_model = model.model if hasattr(model, "model") else model
    for name, module in pytorch_model.named_modules():
        if isinstance(module, torch.nn.Conv2d):
            hooks.append(module.register_forward_hook(_make_hook(name)))

    # Run forward passes
    pytorch_model.eval()
    with torch.no_grad():
        for i, inp in enumerate(sample_inputs):
            if i >= n_samples:
                break
            pytorch_model(inp)

    # Remove hooks
    for h in hooks:
        h.remove()

    # Convert max values to scales
    scales = {}
    for name, max_val in act_max.items():
        scales[name] = max_val / 127.0 if max_val != 0 else 1.0

    return scales


def int8_conv2d_reference(input_int8, weight_int8, bias_float, stride=1, padding=0):
    """Reference int8 convolution mimicking NPU behavior.

    Performs MAC in int32 (matching NPU accumulation), returns int32 result
    before requantization. The caller applies the shift.

    Args:
        input_int8: Int8 input tensor [N, C, H, W].
        weight_int8: Int8 weight tensor [O, I, kH, kW].
        bias_float: Float32 bias tensor [O].
        stride: Conv stride.
        padding: Conv padding.

    Returns:
        Int32 tensor of accumulated MAC results (before shift).
    """
    # Simulate int8 MAC in int32 using float (torch doesn't natively support int8 conv)
    out = F.conv2d(
        input_int8.float(),
        weight_int8.float(),
        bias=None,
        stride=stride,
        padding=padding,
    )
    # Add bias scaled to int32 accumulator domain (bias is in float, caller handles)
    return out.to(torch.int32)
