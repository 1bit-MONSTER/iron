# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests for layout conversion utilities (no hardware needed)."""

import torch
import torch.nn as nn
import torch.nn.functional as F
import pytest

from iron.applications.yolov8n.model_prep import (
    fuse_conv_bn,
    nchw_to_tiled,
    tiled_to_nchw,
    weights_to_tiled_1x1,
    weights_to_tiled_3x3,
)


def test_nchw_tiled_roundtrip():
    """Verify NCHW -> tiled -> NCHW is identity."""
    torch.manual_seed(42)
    C, H, W = 32, 16, 16
    x = torch.randn(1, C, H, W)

    tiled = nchw_to_tiled(x, group_size=8)

    # Check tiled shape
    assert tiled.shape == (H, C // 8, W, 8)

    # Roundtrip
    recovered = tiled_to_nchw(tiled, C, H, W, group_size=8)
    assert recovered.shape == (1, C, H, W)
    assert torch.allclose(x, recovered), "Roundtrip mismatch"


def test_nchw_tiled_roundtrip_padded():
    """Verify roundtrip works when channels aren't a multiple of 8."""
    torch.manual_seed(123)
    C, H, W = 3, 8, 8  # 3 channels (e.g., RGB input)
    x = torch.randn(1, C, H, W)

    tiled = nchw_to_tiled(x, group_size=8)

    # Channels padded from 3 to 8
    C_padded = 8
    assert tiled.shape == (H, C_padded // 8, W, 8)

    # Roundtrip should recover original 3 channels
    recovered = tiled_to_nchw(tiled, C, H, W, group_size=8)
    assert recovered.shape == (1, C, H, W)
    assert torch.allclose(x, recovered), "Padded roundtrip mismatch"


def test_nchw_tiled_roundtrip_various_channels():
    """Verify roundtrip for several channel counts used in YOLOv8n."""
    torch.manual_seed(7)
    for C in [3, 16, 32, 64, 128, 192, 256, 384]:
        H, W = 4, 4
        x = torch.randn(1, C, H, W)
        tiled = nchw_to_tiled(x, group_size=8)
        recovered = tiled_to_nchw(tiled, C, H, W, group_size=8)
        assert torch.allclose(x, recovered), f"Roundtrip failed for C={C}"


def test_nchw_tiled_3d_input():
    """Verify nchw_to_tiled accepts [C, H, W] input without batch dim."""
    torch.manual_seed(99)
    C, H, W = 16, 4, 4
    x_3d = torch.randn(C, H, W)
    x_4d = x_3d.unsqueeze(0)

    tiled_3d = nchw_to_tiled(x_3d, group_size=8)
    tiled_4d = nchw_to_tiled(x_4d, group_size=8)

    assert torch.allclose(
        tiled_3d, tiled_4d
    ), "3D and 4D input should give same tiled output"


def test_nchw_tiled_element_check():
    """Verify specific element positions are correct in tiled layout.

    For a tensor with C=16, H=2, W=2, group_size=8:
      tiled[y, cg, x, ci] = original[cg*8 + ci, y, x]
    """
    torch.manual_seed(0)
    C, H, W = 16, 2, 2
    x = torch.randn(1, C, H, W)

    tiled = nchw_to_tiled(x, group_size=8)
    # tiled shape: [2, 2, 2, 8]

    for y in range(H):
        for cg in range(C // 8):
            for xi in range(W):
                for ci in range(8):
                    expected = x[0, cg * 8 + ci, y, xi]
                    actual = tiled[y, cg, xi, ci]
                    assert (
                        expected == actual
                    ), f"Mismatch at y={y}, cg={cg}, x={xi}, ci={ci}"


def test_weights_1x1_tiled():
    """Verify 1x1 weight tiling produces correct layout.

    For weight[o, i, 1, 1], the tiled layout should satisfy:
      tiled[o//g, i//g, i%g, o%g] = weight[o, i, 0, 0]
    """
    torch.manual_seed(42)
    O, I = 32, 16
    w = torch.randn(O, I, 1, 1)

    tiled = weights_to_tiled_1x1(w, group_size=8)
    assert tiled.shape == (O // 8, I // 8, 8, 8)

    for o in range(O):
        for i in range(I):
            expected = w[o, i, 0, 0]
            actual = tiled[o // 8, i // 8, i % 8, o % 8]
            assert expected == actual, f"Mismatch at o={o}, i={i}"


def test_weights_1x1_tiled_padded():
    """Verify 1x1 weight tiling with channels that need padding."""
    torch.manual_seed(55)
    O, I = 5, 3  # Both need padding to 8
    w = torch.randn(O, I, 1, 1)

    tiled = weights_to_tiled_1x1(w, group_size=8)
    assert tiled.shape == (1, 1, 8, 8)  # Both padded to 8

    # Original elements should be preserved
    for o in range(O):
        for i in range(I):
            expected = w[o, i, 0, 0]
            actual = tiled[o // 8, i // 8, i % 8, o % 8]
            assert expected == actual, f"Mismatch at o={o}, i={i}"

    # Padded elements should be zero
    for o in range(O, 8):
        for i in range(I):
            actual = tiled[0, 0, i % 8, o % 8]
            assert actual == 0.0, f"Padded o={o}, i={i} should be zero"


def test_weights_3x3_tiled():
    """Verify 3x3 weight tiling produces correct layout.

    For weight[o, i, kh, kw], the tiled layout should satisfy:
      tiled[o//g, i//g, kh, kw, i%g, o%g] = weight[o, i, kh, kw]
    """
    torch.manual_seed(42)
    O, I = 16, 8
    w = torch.randn(O, I, 3, 3)

    tiled = weights_to_tiled_3x3(w, group_size=8)
    assert tiled.shape == (O // 8, I // 8, 3, 3, 8, 8)

    for o in range(O):
        for i in range(I):
            for kh in range(3):
                for kw in range(3):
                    expected = w[o, i, kh, kw]
                    actual = tiled[o // 8, i // 8, kh, kw, i % 8, o % 8]
                    assert (
                        expected == actual
                    ), f"Mismatch at o={o}, i={i}, kh={kh}, kw={kw}"


def test_weights_3x3_tiled_padded():
    """Verify 3x3 weight tiling with non-multiple-of-8 channels."""
    torch.manual_seed(77)
    O, I = 16, 3  # Input channels = 3 (first conv layer in YOLOv8n)
    w = torch.randn(O, I, 3, 3)

    tiled = weights_to_tiled_3x3(w, group_size=8)
    assert tiled.shape == (O // 8, 1, 3, 3, 8, 8)  # I padded to 8

    # Original elements preserved
    for o in range(O):
        for i in range(I):
            for kh in range(3):
                for kw in range(3):
                    expected = w[o, i, kh, kw]
                    actual = tiled[o // 8, i // 8, kh, kw, i % 8, o % 8]
                    assert (
                        expected == actual
                    ), f"Mismatch at o={o}, i={i}, kh={kh}, kw={kw}"


def test_fuse_conv_bn():
    """Verify BN fusion matches separate Conv+BN forward pass."""
    torch.manual_seed(42)

    # Create Conv2d + BatchNorm2d
    conv = nn.Conv2d(16, 32, 3, padding=1, bias=False)
    bn = nn.BatchNorm2d(32)

    # Put BN in eval mode and set non-trivial running stats
    bn.eval()
    # Simulate trained BN by setting running stats
    bn.running_mean.copy_(torch.randn(32) * 0.5)
    bn.running_var.copy_(torch.rand(32) * 2.0 + 0.1)
    bn.weight.data.copy_(torch.randn(32) * 0.8 + 1.0)
    bn.bias.data.copy_(torch.randn(32) * 0.3)

    # Run separate Conv + BN
    x = torch.randn(1, 16, 8, 8)
    with torch.no_grad():
        conv_out = conv(x)
        bn_out = bn(conv_out)

    # Run fused
    w_fused, b_fused = fuse_conv_bn(conv, bn)
    with torch.no_grad():
        fused_out = F.conv2d(x, w_fused, b_fused, padding=1)

    assert torch.allclose(
        bn_out, fused_out, atol=1e-5
    ), f"Max diff: {(bn_out - fused_out).abs().max()}"


def test_fuse_conv_bn_with_bias():
    """Verify BN fusion works when Conv has a bias."""
    torch.manual_seed(42)

    conv = nn.Conv2d(8, 16, 1, bias=True)
    bn = nn.BatchNorm2d(16)
    bn.eval()
    bn.running_mean.copy_(torch.randn(16))
    bn.running_var.copy_(torch.rand(16) + 0.1)

    x = torch.randn(1, 8, 4, 4)
    with torch.no_grad():
        expected = bn(conv(x))

    w_fused, b_fused = fuse_conv_bn(conv, bn)
    with torch.no_grad():
        actual = F.conv2d(x, w_fused, b_fused)

    assert torch.allclose(
        expected, actual, atol=1e-5
    ), f"Max diff: {(expected - actual).abs().max()}"


def test_fuse_conv_bn_shapes():
    """Verify fused weight/bias have correct shapes for various configs."""
    for O, I, k in [(16, 3, 3), (32, 16, 3), (64, 32, 1), (128, 64, 1)]:
        conv = nn.Conv2d(I, O, k, bias=False)
        bn = nn.BatchNorm2d(O)
        bn.eval()
        w, b = fuse_conv_bn(conv, bn)
        assert w.shape == (O, I, k, k), f"Weight shape mismatch for ({O},{I},{k})"
        assert b.shape == (O,), f"Bias shape mismatch for ({O},{I},{k})"
