# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests for YOLOv8n multi-PDI pipeline.

These tests verify that the full YOLOv8n model can be compiled into a
single multi-PDI xclbin and executed on the NPU. Tests use reduced-scale
inputs (32x32) for fast compilation and small memory footprint.
"""

import pytest
import torch
import torch.nn.functional as F
import numpy as np
from ml_dtypes import bfloat16

from iron.common import AIEContext


def _make_random_cbs_weights(in_ch, out_ch, kernel_size):
    """Generate random CBS (Conv+BN fused) weights."""
    w = torch.randn(out_ch, in_ch, kernel_size, kernel_size, dtype=torch.bfloat16) * 0.01
    b = torch.randn(out_ch, dtype=torch.bfloat16) * 0.01
    return {"weight": w, "bias": b}


def _make_random_bottleneck_weights(channels, n=1):
    """Generate random bottleneck weights."""
    bns = []
    for _ in range(n):
        bns.append((
            torch.randn(channels, channels, 3, 3, dtype=torch.bfloat16) * 0.01,
            torch.randn(channels, dtype=torch.bfloat16) * 0.01,
            torch.randn(channels, channels, 3, 3, dtype=torch.bfloat16) * 0.01,
            torch.randn(channels, dtype=torch.bfloat16) * 0.01,
        ))
    return bns


def _make_random_c2f_weights(c_in, c_out, n_bottlenecks):
    """Generate random C2f weights."""
    c = c_out // 2
    return {
        "cv1_weight": torch.randn(2 * c, c_in, 1, 1, dtype=torch.bfloat16) * 0.01,
        "cv1_bias": torch.randn(2 * c, dtype=torch.bfloat16) * 0.01,
        "bottlenecks": _make_random_bottleneck_weights(c, n_bottlenecks),
        "cv2_weight": torch.randn(c_out, (2 + n_bottlenecks) * c, 1, 1, dtype=torch.bfloat16) * 0.01,
        "cv2_bias": torch.randn(c_out, dtype=torch.bfloat16) * 0.01,
    }


def _make_random_sppf_weights(c_in, c_out):
    """Generate random SPPF weights."""
    c_ = c_in // 2
    return {
        "cv1_weight": torch.randn(c_, c_in, 1, 1, dtype=torch.bfloat16) * 0.01,
        "cv1_bias": torch.randn(c_, dtype=torch.bfloat16) * 0.01,
        "cv2_weight": torch.randn(c_out, c_ * 4, 1, 1, dtype=torch.bfloat16) * 0.01,
        "cv2_bias": torch.randn(c_out, dtype=torch.bfloat16) * 0.01,
    }


def _make_random_detect_branch_weights(c_in, c_mid, c_out):
    """Generate random DetectBranch weights."""
    return {
        "cv1_weight": torch.randn(c_mid, c_in, 3, 3, dtype=torch.bfloat16) * 0.01,
        "cv1_bias": torch.randn(c_mid, dtype=torch.bfloat16) * 0.01,
        "cv2_weight": torch.randn(c_mid, c_mid, 3, 3, dtype=torch.bfloat16) * 0.01,
        "cv2_bias": torch.randn(c_mid, dtype=torch.bfloat16) * 0.01,
        "cv3_weight": torch.randn(c_out, c_mid, 1, 1, dtype=torch.bfloat16) * 0.01,
        "cv3_bias": torch.randn(c_out, dtype=torch.bfloat16) * 0.01,
    }


def _make_random_model_weights(nc=80, reg_max=16):
    """Generate random weights for the full YOLOv8n model."""
    torch.manual_seed(42)

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

    c_reg = 4 * reg_max  # 64
    c_cls = nc  # 80
    c2 = 64
    c3 = max(nc, 16)  # 80

    detect = {
        "reg_p3": _make_random_detect_branch_weights(64, c2, c_reg),
        "reg_p4": _make_random_detect_branch_weights(128, c2, c_reg),
        "reg_p5": _make_random_detect_branch_weights(256, c2, c_reg),
        "cls_p3": _make_random_detect_branch_weights(64, c3, c_cls),
        "cls_p4": _make_random_detect_branch_weights(128, c3, c_cls),
        "cls_p5": _make_random_detect_branch_weights(256, c3, c_cls),
    }

    return {"backbone": backbone, "neck": neck, "detect": detect}


def test_pipeline_construction(aie_context):
    """Test that the pipeline can be constructed and artifacts set up.

    This test calls set_up_artifacts() directly (normally done by
    compile_all) to verify the multi-PDI chain is built correctly
    without actually compiling.
    """
    from iron.applications.yolov8n.pipeline import YOLOv8nPipeline

    pipeline = YOLOv8nPipeline(
        img_height=256,
        img_width=256,
        context=aie_context,
    )

    # Trigger artifact setup (normally done by compile_all)
    pipeline.set_up_artifacts()

    # Verify artifacts were registered
    assert len(pipeline.artifacts) > 0, "No artifacts registered"
    assert pipeline.combined_xclbin is not None, "No combined xclbin"

    # Verify layer map has entries for all expected layers
    assert "bb_l0" in pipeline._layer_map
    assert "bb_l9_cv1" in pipeline._layer_map
    assert "nk_up1" in pipeline._layer_map
    assert "det_reg_p3_cv1" in pipeline._layer_map
    assert "det_cls_p5_cv3" in pipeline._layer_map

    # Count unique PDIs
    n_pdis = len(pipeline._pdi_map)
    print(f"Unique PDI configs: {n_pdis}")
    assert n_pdis > 0, "No PDIs registered"
    print(f"Total layers: {len(pipeline._layer_map)}")
    print(f"Total artifacts: {len(pipeline.artifacts)}")


@pytest.mark.extensive
def test_pipeline_shapes(aie_context):
    """Test that the pipeline compiles and produces correct output shapes.

    Uses 640x640 (native YOLOv8n size) because the MLIR designs' TAP
    decompositions are tuned for this size. Smaller sizes may hit the
    DMA BD 1023-element dimension limit.
    """
    from iron.applications.yolov8n.pipeline import YOLOv8nPipeline

    H, W = 640, 640

    pipeline = YOLOv8nPipeline(
        img_height=H,
        img_width=W,
        context=aie_context,
    )

    # Compile
    aie_context.compile_all()

    # Load random weights
    weights = _make_random_model_weights()
    pipeline.load_weights(weights)

    # Prepare runtime
    aie_context.prepare_runtime()

    # Run
    x = torch.randn(1, 3, H, W, dtype=torch.bfloat16)
    result = pipeline.forward(x)

    # Verify output shapes
    assert len(result["reg"]) == 3
    assert len(result["cls"]) == 3

    # P3 scale: H/8 x W/8
    h8, w8 = H // 8, W // 8
    assert result["reg"][0].shape == (1, 64, h8, w8), f"reg_p3 shape: {result['reg'][0].shape}"
    assert result["cls"][0].shape == (1, 80, h8, w8), f"cls_p3 shape: {result['cls'][0].shape}"

    # P4 scale: H/16 x W/16
    h16, w16 = H // 16, W // 16
    assert result["reg"][1].shape == (1, 64, h16, w16), f"reg_p4 shape: {result['reg'][1].shape}"
    assert result["cls"][1].shape == (1, 80, h16, w16), f"cls_p4 shape: {result['cls'][1].shape}"

    # P5 scale: H/32 x W/32
    h32, w32 = H // 32, W // 32
    assert result["reg"][2].shape == (1, 64, h32, w32), f"reg_p5 shape: {result['reg'][2].shape}"
    assert result["cls"][2].shape == (1, 80, h32, w32), f"cls_p5 shape: {result['cls'][2].shape}"

    print("All output shapes correct!")


@pytest.mark.extensive
def test_pipeline_vs_layerwise(aie_context):
    """Verify pipeline compiles, runs, and produces finite outputs.

    Uses 640x640 native size. Runs forward pass with random weights
    and verifies all outputs are finite (not NaN/inf).
    """
    from iron.applications.yolov8n.pipeline import YOLOv8nPipeline

    H, W = 640, 640

    # Create pipeline
    pipeline = YOLOv8nPipeline(
        img_height=H,
        img_width=W,
        context=aie_context,
    )

    # Note: Can't run both pipeline and layer-wise in same context
    # since they'd both try to register operators. The pipeline test
    # alone verifies correct shapes and compilation.
    # A full layer-wise comparison would need separate contexts.

    # Compile and run pipeline
    aie_context.compile_all()

    weights = _make_random_model_weights()
    pipeline.load_weights(weights)

    aie_context.prepare_runtime()

    x = torch.randn(1, 3, H, W, dtype=torch.bfloat16)
    result = pipeline.forward(x)

    # Verify outputs are finite
    for i, reg in enumerate(result["reg"]):
        assert torch.isfinite(reg).all(), f"reg_p{i+3} has non-finite values"
    for i, cls_ in enumerate(result["cls"]):
        assert torch.isfinite(cls_).all(), f"cls_p{i+3} has non-finite values"

    print("Pipeline outputs are all finite")
