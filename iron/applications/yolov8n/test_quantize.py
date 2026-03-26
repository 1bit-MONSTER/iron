# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests for int8 quantization utilities."""

import math

import torch
import torch.nn as nn
import torch.nn.functional as F
import pytest

from iron.applications.yolov8n.quantize import (
    Int8Quantizer,
    int8_conv2d_reference,
)


class TestQuantizeRoundtrip:
    """Quantize -> dequantize preserves values within tolerance."""

    def test_basic_roundtrip(self):
        """Roundtrip error should be bounded by scale/2."""
        torch.manual_seed(42)
        x = torch.randn(64, 64) * 5.0

        q = Int8Quantizer()
        x_int8, scale = q.quantize_tensor(x)
        x_recovered = q.dequantize_tensor(x_int8, scale)

        # Max roundtrip error is scale/2 (half a quantization step)
        max_err = (x - x_recovered).abs().max().item()
        assert max_err <= scale / 2 + 1e-6, f"Roundtrip error {max_err} > {scale / 2}"

    def test_roundtrip_small_values(self):
        """Small-magnitude tensors should quantize correctly."""
        torch.manual_seed(7)
        x = torch.randn(32, 32) * 0.01

        x_int8, scale = Int8Quantizer.quantize_tensor(x)
        x_recovered = Int8Quantizer.dequantize_tensor(x_int8, scale)

        max_err = (x - x_recovered).abs().max().item()
        assert max_err <= scale / 2 + 1e-6

    def test_roundtrip_large_values(self):
        """Large-magnitude tensors: absolute error bounded by scale/2."""
        torch.manual_seed(99)
        x = torch.randn(16, 16) * 1000.0

        x_int8, scale = Int8Quantizer.quantize_tensor(x)
        x_recovered = Int8Quantizer.dequantize_tensor(x_int8, scale)

        # Absolute error bounded by half a quantization step
        max_err = (x - x_recovered).abs().max().item()
        assert max_err <= scale / 2 + 1e-3, f"Roundtrip error {max_err} > {scale / 2}"

        # Scale should reflect the tensor magnitude
        assert scale > 1.0, f"Scale {scale} too small for 1000x tensor"

    def test_roundtrip_preserves_sign(self):
        """Signs must be preserved through quantization."""
        x = torch.tensor([-5.0, -1.0, 0.0, 1.0, 5.0])
        x_int8, scale = Int8Quantizer.quantize_tensor(x)
        x_recovered = Int8Quantizer.dequantize_tensor(x_int8, scale)

        assert (x_recovered[0] < 0).item()
        assert (x_recovered[1] < 0).item()
        assert (x_recovered[2] == 0).item()
        assert (x_recovered[3] > 0).item()
        assert (x_recovered[4] > 0).item()

    def test_zero_tensor(self):
        """All-zero tensor should quantize to all zeros with scale=1."""
        x = torch.zeros(8, 8)
        x_int8, scale = Int8Quantizer.quantize_tensor(x)

        assert scale == 1.0
        assert (x_int8 == 0).all()

    def test_explicit_scale(self):
        """Passing an explicit scale should use it instead of computing one."""
        x = torch.tensor([1.0, 2.0, 3.0])
        x_int8, scale = Int8Quantizer.quantize_tensor(x, scale=0.1)

        assert scale == 0.1
        assert x_int8[0].item() == 10  # 1.0 / 0.1 = 10
        assert x_int8[1].item() == 20
        assert x_int8[2].item() == 30

    def test_clamping(self):
        """Values outside [-128, 127] * scale should be clamped."""
        x = torch.tensor([200.0, -200.0])
        x_int8, scale = Int8Quantizer.quantize_tensor(x, scale=1.0)

        assert x_int8[0].item() == 127
        assert x_int8[1].item() == -128

    def test_4d_tensor(self):
        """Quantization should work for conv-shaped [N,C,H,W] tensors."""
        torch.manual_seed(42)
        x = torch.randn(1, 16, 8, 8)
        x_int8, scale = Int8Quantizer.quantize_tensor(x)
        x_recovered = Int8Quantizer.dequantize_tensor(x_int8, scale)

        assert x_int8.shape == (1, 16, 8, 8)
        assert x_int8.dtype == torch.int8
        max_err = (x - x_recovered).abs().max().item()
        assert max_err <= scale / 2 + 1e-6


class TestShiftComputation:
    """Verify shift values for known scale combinations."""

    def test_identity_scales(self):
        """When all scales are 1.0, combined = 1.0, shift = 0."""
        shift = Int8Quantizer.compute_shift(1.0, 1.0, 1.0)
        assert shift == 0

    def test_power_of_two_combined(self):
        """When combined scale is a power of 2, shift is exact."""
        # combined = w * a / o = 0.5 * 0.5 / 1.0 = 0.25
        # 1/combined = 4 = 2^2, shift = 2
        shift = Int8Quantizer.compute_shift(0.5, 0.5, 1.0)
        assert shift == 2

    def test_shift_increases_with_smaller_combined(self):
        """Smaller combined scale -> larger shift."""
        s1 = Int8Quantizer.compute_shift(0.1, 0.1, 1.0)
        s2 = Int8Quantizer.compute_shift(0.01, 0.01, 1.0)
        assert s2 > s1

    def test_shift_clamp_lower(self):
        """Shift should be clamped to 0 minimum."""
        # combined = 10*10/1 = 100, log2(1/100) ≈ -6.6, rounds to -7 -> clamp to 0
        shift = Int8Quantizer.compute_shift(10.0, 10.0, 1.0)
        assert shift == 0

    def test_shift_clamp_upper(self):
        """Shift should be clamped to 31 maximum."""
        # combined = 1e-20, 1/combined is huge, log2 >> 31
        shift = Int8Quantizer.compute_shift(1e-10, 1e-10, 1.0)
        assert shift == 31

    def test_known_shift_values(self):
        """Verify shift for realistic YOLOv8n-like scales."""
        # Typical: w_scale ≈ 0.02, a_scale ≈ 0.1, o_scale ≈ 0.05
        # combined = 0.02 * 0.1 / 0.05 = 0.04
        # 1/0.04 = 25, log2(25) ≈ 4.64, round to 5
        shift = Int8Quantizer.compute_shift(0.02, 0.1, 0.05)
        assert shift == 5

    def test_shift_symmetry(self):
        """Swapping weight and activation scales should give same shift."""
        s1 = Int8Quantizer.compute_shift(0.03, 0.07, 0.1)
        s2 = Int8Quantizer.compute_shift(0.07, 0.03, 0.1)
        assert s1 == s2


class TestWeightQuantization:
    """Quantize conv weights and verify range/properties."""

    def test_int8_range(self):
        """All quantized weights should be in [-128, 127]."""
        torch.manual_seed(42)
        w = torch.randn(32, 16, 3, 3)

        w_int8, scale = Int8Quantizer.quantize_tensor(w)

        assert w_int8.dtype == torch.int8
        assert w_int8.min().item() >= -128
        assert w_int8.max().item() <= 127

    def test_scale_is_positive(self):
        """Scale should always be positive."""
        torch.manual_seed(42)
        for _ in range(10):
            w = torch.randn(16, 8, 3, 3)
            _, scale = Int8Quantizer.quantize_tensor(w)
            assert scale > 0

    def test_max_maps_to_127(self):
        """The max absolute value should map to ±127."""
        torch.manual_seed(42)
        w = torch.randn(16, 8, 1, 1)
        w_int8, scale = Int8Quantizer.quantize_tensor(w)

        # The element with max abs should map to ±127
        max_abs_idx = w.abs().argmax()
        max_int8 = w_int8.flatten()[max_abs_idx].item()
        assert abs(max_int8) == 127

    def test_quantize_conv_layer(self):
        """quantize_conv_layer should store scale and return int8 weights."""
        torch.manual_seed(42)
        q = Int8Quantizer()
        w = torch.randn(32, 16, 3, 3)
        b = torch.randn(32)

        result = q.quantize_conv_layer(w, b, "test_layer")

        assert result["weight"].dtype == torch.int8
        assert result["bias"].dtype == torch.float32
        assert result["weight_scale"] > 0
        assert "test_layer" in q.weight_scales
        assert q.weight_scales["test_layer"] == result["weight_scale"]

    def test_various_kernel_sizes(self):
        """Quantization should work for 1x1 and 3x3 kernels."""
        torch.manual_seed(42)
        for kH, kW in [(1, 1), (3, 3)]:
            w = torch.randn(32, 16, kH, kW)
            w_int8, scale = Int8Quantizer.quantize_tensor(w)
            assert w_int8.shape == (32, 16, kH, kW)
            assert w_int8.dtype == torch.int8


class TestInt8ConvReference:
    """Int8 conv matches float conv within quantization error."""

    def test_1x1_conv_accuracy(self):
        """Int8 1x1 conv should approximate float conv."""
        torch.manual_seed(42)
        O, I, H, W = 16, 8, 4, 4

        # Float reference
        w_float = torch.randn(O, I, 1, 1) * 0.1
        x_float = torch.randn(1, I, H, W) * 0.5
        b_float = torch.randn(O) * 0.01

        float_out = F.conv2d(x_float, w_float, b_float)

        # Quantize inputs
        x_int8, x_scale = Int8Quantizer.quantize_tensor(x_float)
        w_int8, w_scale = Int8Quantizer.quantize_tensor(w_float)

        # Int8 MAC (no bias in int domain)
        int32_out = int8_conv2d_reference(x_int8, w_int8, b_float)

        # Dequantize: int32_out * (w_scale * x_scale) + bias
        deq_out = int32_out.float() * (w_scale * x_scale) + b_float.view(1, -1, 1, 1)

        # Check correlation (should be high even if absolute values differ slightly)
        flat_float = float_out.flatten()
        flat_deq = deq_out.flatten()
        correlation = torch.corrcoef(torch.stack([flat_float, flat_deq]))[0, 1].item()
        assert correlation > 0.95, f"Correlation {correlation} too low"

    def test_3x3_conv_accuracy(self):
        """Int8 3x3 conv should approximate float conv."""
        torch.manual_seed(42)
        O, I, H, W = 16, 8, 8, 8

        w_float = torch.randn(O, I, 3, 3) * 0.1
        x_float = torch.randn(1, I, H, W) * 0.5
        b_float = torch.randn(O) * 0.01

        float_out = F.conv2d(x_float, w_float, b_float, padding=1)

        x_int8, x_scale = Int8Quantizer.quantize_tensor(x_float)
        w_int8, w_scale = Int8Quantizer.quantize_tensor(w_float)

        int32_out = int8_conv2d_reference(x_int8, w_int8, b_float, padding=1)
        deq_out = int32_out.float() * (w_scale * x_scale) + b_float.view(1, -1, 1, 1)

        flat_float = float_out.flatten()
        flat_deq = deq_out.flatten()
        correlation = torch.corrcoef(torch.stack([flat_float, flat_deq]))[0, 1].item()
        assert correlation > 0.95, f"Correlation {correlation} too low"

    def test_int8_output_dtype(self):
        """int8_conv2d_reference should return int32."""
        torch.manual_seed(42)
        x = torch.randint(-10, 10, (1, 4, 4, 4), dtype=torch.int8)
        w = torch.randint(-5, 5, (8, 4, 1, 1), dtype=torch.int8)
        b = torch.zeros(8)

        out = int8_conv2d_reference(x, w, b)
        assert out.dtype == torch.int32


class TestActivationQuantization:
    """Test activation quantization with scale tracking."""

    def test_calibration_stores_scale(self):
        """calibration=True should record the scale."""
        q = Int8Quantizer()
        x = torch.randn(1, 16, 8, 8)

        x_int8, scale = q.quantize_activation(x, "layer0", calibration=True)

        assert "layer0" in q.act_scales
        assert q.act_scales["layer0"] == scale

    def test_stored_scale_reused(self):
        """With calibration=False and stored scale, should reuse it."""
        q = Int8Quantizer()
        x1 = torch.randn(1, 16, 8, 8) * 2.0
        x2 = torch.randn(1, 16, 8, 8) * 10.0  # Much larger range

        # Calibrate on x1
        _, scale1 = q.quantize_activation(x1, "layer0", calibration=True)

        # Use stored scale on x2 (calibration=False)
        _, scale2 = q.quantize_activation(x2, "layer0", calibration=False)

        assert scale2 == scale1  # Should reuse calibrated scale

    def test_recalibration_updates_scale(self):
        """With calibration=True, should update the stored scale."""
        q = Int8Quantizer()
        x1 = torch.randn(1, 16, 8, 8) * 1.0
        x2 = torch.randn(1, 16, 8, 8) * 100.0

        q.quantize_activation(x1, "layer0", calibration=True)
        scale1 = q.act_scales["layer0"]

        q.quantize_activation(x2, "layer0", calibration=True)
        scale2 = q.act_scales["layer0"]

        assert scale2 > scale1  # Larger tensor -> larger scale


class TestGetLayerShift:
    """Test get_layer_shift with stored scales."""

    def test_returns_shift_with_all_scales(self):
        """Should return a valid shift when all scales are available."""
        q = Int8Quantizer()
        q.weight_scales["conv1"] = 0.02
        q.act_scales["conv1"] = 0.1
        q.act_scales["conv2"] = 0.05

        shift = q.get_layer_shift("conv1", "conv2")
        assert shift is not None
        assert 0 <= shift <= 31

    def test_returns_none_with_missing_scales(self):
        """Should return None when any scale is missing."""
        q = Int8Quantizer()
        q.weight_scales["conv1"] = 0.02

        assert q.get_layer_shift("conv1", "conv2") is None
