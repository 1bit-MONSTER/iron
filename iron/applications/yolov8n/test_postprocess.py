# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for YOLOv8n post-processing (DFL decode + NMS).

These tests verify pure Python/PyTorch logic -- no NPU hardware required.
"""

import pytest
import torch
import torch.nn.functional as F

from iron.applications.yolov8n.postprocess import YOLOv8nPostProcess


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def postproc():
    """Default post-processor with standard YOLOv8n settings."""
    return YOLOv8nPostProcess(
        nc=80, reg_max=16, strides=[8, 16, 32], img_size=640
    )


@pytest.fixture
def small_postproc():
    """Small post-processor for easier manual verification."""
    return YOLOv8nPostProcess(
        nc=2, reg_max=4, strides=[8], img_size=32, conf_thres=0.3, iou_thres=0.5
    )


# ---------------------------------------------------------------------------
# Anchor generation
# ---------------------------------------------------------------------------


class TestAnchorGeneration:
    def test_total_anchor_count(self, postproc):
        """Total anchors = 80*80 + 40*40 + 20*20 = 8400."""
        assert postproc.anchor_points.shape == (8400, 2)
        assert postproc.stride_tensor.shape == (8400, 1)

    def test_per_scale_grid_sizes(self, postproc):
        """Verify grid sizes for each stride."""
        expected = {8: 80 * 80, 16: 40 * 40, 32: 20 * 20}
        offset = 0
        for stride, count in expected.items():
            strides_slice = postproc.stride_tensor[offset : offset + count]
            assert (strides_slice == stride).all()
            offset += count

    def test_anchor_centers_stride8(self, postproc):
        """First anchor at stride=8 should be at (4.0, 4.0) = 0.5 * 8."""
        first = postproc.anchor_points[0]
        assert torch.allclose(first, torch.tensor([4.0, 4.0]))

    def test_anchor_centers_stride16(self, postproc):
        """First anchor at stride=16 should be at (8.0, 8.0) = 0.5 * 16."""
        p3_count = 80 * 80
        first_p4 = postproc.anchor_points[p3_count]
        assert torch.allclose(first_p4, torch.tensor([8.0, 8.0]))

    def test_anchor_centers_stride32(self, postproc):
        """First anchor at stride=32 should be at (16.0, 16.0) = 0.5 * 32."""
        p3_count = 80 * 80
        p4_count = 40 * 40
        first_p5 = postproc.anchor_points[p3_count + p4_count]
        assert torch.allclose(first_p5, torch.tensor([16.0, 16.0]))

    def test_last_anchor_stride8(self, postproc):
        """Last anchor of P3 (stride=8): center of cell (79, 79) = (79.5*8, 79.5*8)."""
        last_p3 = postproc.anchor_points[80 * 80 - 1]
        expected = torch.tensor([79.5 * 8, 79.5 * 8])
        assert torch.allclose(last_p3, expected)


# ---------------------------------------------------------------------------
# DFL decode
# ---------------------------------------------------------------------------


class TestDFLDecode:
    def test_uniform_distribution(self, postproc):
        """Uniform logits -> softmax gives uniform weights -> expected value = 7.5."""
        n = 10
        reg = torch.zeros(n, 64)  # uniform logits
        dist = postproc._dfl_decode(reg)
        assert dist.shape == (n, 4)
        # E[X] for uniform over {0..15} = 7.5
        assert torch.allclose(dist, torch.full((n, 4), 7.5), atol=1e-5)

    def test_peaked_distribution(self, postproc):
        """One-hot logits at bin k -> decoded distance = k."""
        n = 5
        reg = torch.full((n, 64), -100.0)
        target_bin = 10
        for edge in range(4):
            reg[:, edge * 16 + target_bin] = 100.0
        dist = postproc._dfl_decode(reg)
        assert torch.allclose(dist, torch.full((n, 4), float(target_bin)), atol=1e-4)

    def test_zero_bin_peaked(self, postproc):
        """One-hot at bin 0 -> distance = 0."""
        reg = torch.full((1, 64), -100.0)
        for edge in range(4):
            reg[0, edge * 16 + 0] = 100.0
        dist = postproc._dfl_decode(reg)
        assert torch.allclose(dist, torch.zeros(1, 4), atol=1e-4)

    def test_max_bin_peaked(self, postproc):
        """One-hot at bin 15 -> distance = 15."""
        reg = torch.full((1, 64), -100.0)
        for edge in range(4):
            reg[0, edge * 16 + 15] = 100.0
        dist = postproc._dfl_decode(reg)
        assert torch.allclose(dist, torch.full((1, 4), 15.0), atol=1e-4)

    def test_small_reg_max(self, small_postproc):
        """DFL decode with reg_max=4: uniform -> E[X] = 1.5."""
        reg = torch.zeros(3, 16)  # 4 edges * 4 bins = 16
        dist = small_postproc._dfl_decode(reg)
        assert dist.shape == (3, 4)
        assert torch.allclose(dist, torch.full((3, 4), 1.5), atol=1e-5)


# ---------------------------------------------------------------------------
# dist2bbox
# ---------------------------------------------------------------------------


class TestDist2Bbox:
    def test_symmetric_distances(self, postproc):
        """Symmetric distances around anchor produce centered box."""
        anchors = torch.tensor([[100.0, 100.0]])
        # left=10, top=20, right=10, bottom=20
        distances = torch.tensor([[10.0, 20.0, 10.0, 20.0]])
        boxes = postproc._dist2bbox(distances, anchors)
        expected = torch.tensor([[90.0, 80.0, 110.0, 120.0]])
        assert torch.allclose(boxes, expected)

    def test_zero_distances(self, postproc):
        """Zero distances -> degenerate box at anchor point."""
        anchors = torch.tensor([[50.0, 50.0]])
        distances = torch.zeros(1, 4)
        boxes = postproc._dist2bbox(distances, anchors)
        expected = torch.tensor([[50.0, 50.0, 50.0, 50.0]])
        assert torch.allclose(boxes, expected)

    def test_multiple_anchors(self, postproc):
        """Batch of anchors with different distances."""
        anchors = torch.tensor([[10.0, 10.0], [200.0, 300.0]])
        distances = torch.tensor([[5.0, 5.0, 5.0, 5.0], [50.0, 100.0, 50.0, 100.0]])
        boxes = postproc._dist2bbox(distances, anchors)
        expected = torch.tensor(
            [[5.0, 5.0, 15.0, 15.0], [150.0, 200.0, 250.0, 400.0]]
        )
        assert torch.allclose(boxes, expected)


# ---------------------------------------------------------------------------
# NMS
# ---------------------------------------------------------------------------


class TestNMS:
    def _make_preds(self, postproc, boxes_spec, class_idx, logit_val=5.0):
        """Create fake reg/cls predictions that decode to specified boxes.

        Args:
            postproc: Post-processor instance.
            boxes_spec: List of (x1, y1, x2, y2) target boxes.
            class_idx: Class index for all boxes.
            logit_val: Logit value for the target class (higher = more confident).

        Returns:
            (reg_list, cls_list) matching the detect head output format.
        """
        n_anchors = postproc.anchor_points.shape[0]
        nc = postproc.nc
        reg_max = postproc.reg_max

        # Start with very negative class logits (sigmoid -> ~0 confidence)
        cls_flat = torch.full((n_anchors, nc), -20.0)
        reg_flat = torch.full((n_anchors, 4 * reg_max), -100.0)

        for i, (x1, y1, x2, y2) in enumerate(boxes_spec):
            cx = (x1 + x2) / 2.0
            cy = (y1 + y2) / 2.0

            # Find closest anchor
            dists = ((postproc.anchor_points[:, 0] - cx) ** 2 +
                     (postproc.anchor_points[:, 1] - cy) ** 2)
            anchor_idx = dists.argmin().item()
            ax, ay = postproc.anchor_points[anchor_idx].tolist()
            stride = postproc.stride_tensor[anchor_idx].item()

            # Compute required distances in stride units
            l = (ax - x1) / stride
            t = (ay - y1) / stride
            r = (x2 - ax) / stride
            b = (y2 - ay) / stride

            # Set peaked DFL distribution for each edge
            for edge_idx, dist_val in enumerate([l, t, r, b]):
                dist_val = max(0.0, min(dist_val, reg_max - 1.0))
                # Peak at nearest integer bin
                bin_idx = int(round(dist_val))
                bin_idx = min(bin_idx, reg_max - 1)
                reg_flat[anchor_idx, edge_idx * reg_max + bin_idx] = 100.0

            # Set class logit
            cls_flat[anchor_idx, class_idx] = logit_val

        # Re-shape into per-scale [1, C, H, W] tensors
        reg_list = []
        cls_list = []
        offset = 0
        for stride in postproc.strides:
            h = postproc.img_size // stride
            w = postproc.img_size // stride
            count = h * w

            reg_scale = reg_flat[offset:offset + count].reshape(h, w, 4 * reg_max)
            reg_scale = reg_scale.permute(2, 0, 1).unsqueeze(0)
            reg_list.append(reg_scale)

            cls_scale = cls_flat[offset:offset + count].reshape(h, w, nc)
            cls_scale = cls_scale.permute(2, 0, 1).unsqueeze(0)
            cls_list.append(cls_scale)

            offset += count

        return reg_list, cls_list

    def test_nms_suppresses_overlapping(self, postproc):
        """Two highly overlapping boxes for same class -> only one survives."""
        boxes = [(100, 100, 200, 200), (105, 105, 205, 205)]
        reg_list, cls_list = self._make_preds(postproc, boxes, class_idx=0, logit_val=5.0)

        result = postproc(reg_list, cls_list)
        # NMS should suppress one of the two overlapping boxes
        assert result["boxes"].shape[0] == 1
        assert result["labels"][0].item() == 0

    def test_nms_keeps_separated(self, postproc):
        """Two well-separated boxes -> both survive NMS."""
        boxes = [(50, 50, 100, 100), (400, 400, 500, 500)]
        reg_list, cls_list = self._make_preds(postproc, boxes, class_idx=0, logit_val=5.0)

        result = postproc(reg_list, cls_list)
        assert result["boxes"].shape[0] == 2

    def test_confidence_filter(self, postproc):
        """Low-confidence detections are filtered out."""
        boxes = [(100, 100, 200, 200)]
        # logit=-1.0 -> sigmoid ~0.27 < 0.25 threshold... barely above
        # logit=-2.0 -> sigmoid ~0.12 < 0.25 threshold
        reg_list, cls_list = self._make_preds(postproc, boxes, class_idx=0, logit_val=-2.0)

        result = postproc(reg_list, cls_list)
        assert result["boxes"].shape[0] == 0
        assert result["scores"].shape[0] == 0
        assert result["labels"].shape[0] == 0


# ---------------------------------------------------------------------------
# End-to-end shape tests
# ---------------------------------------------------------------------------


class TestEndToEnd:
    def test_output_shapes_random(self, postproc):
        """Random inputs produce correctly-shaped outputs."""
        reg_list = [
            torch.randn(1, 64, 80, 80),
            torch.randn(1, 64, 40, 40),
            torch.randn(1, 64, 20, 20),
        ]
        cls_list = [
            torch.randn(1, 80, 80, 80),
            torch.randn(1, 80, 40, 40),
            torch.randn(1, 80, 20, 20),
        ]

        result = postproc(reg_list, cls_list)

        assert "boxes" in result
        assert "scores" in result
        assert "labels" in result
        assert result["boxes"].ndim == 2
        assert result["boxes"].shape[1] == 4
        assert result["scores"].ndim == 1
        assert result["labels"].ndim == 1
        n = result["boxes"].shape[0]
        assert result["scores"].shape[0] == n
        assert result["labels"].shape[0] == n

    def test_output_shapes_no_detections(self, postproc):
        """All-negative class logits produce empty output."""
        reg_list = [
            torch.zeros(1, 64, 80, 80),
            torch.zeros(1, 64, 40, 40),
            torch.zeros(1, 64, 20, 20),
        ]
        cls_list = [
            torch.full((1, 80, 80, 80), -10.0),
            torch.full((1, 80, 40, 40), -10.0),
            torch.full((1, 80, 20, 20), -10.0),
        ]

        result = postproc(reg_list, cls_list)
        assert result["boxes"].shape == (0, 4)
        assert result["scores"].shape == (0,)
        assert result["labels"].shape == (0,)

    def test_bfloat16_input(self, postproc):
        """Post-processor handles bfloat16 inputs correctly."""
        reg_list = [
            torch.randn(1, 64, 80, 80).to(torch.bfloat16),
            torch.randn(1, 64, 40, 40).to(torch.bfloat16),
            torch.randn(1, 64, 20, 20).to(torch.bfloat16),
        ]
        cls_list = [
            torch.randn(1, 80, 80, 80).to(torch.bfloat16),
            torch.randn(1, 80, 40, 40).to(torch.bfloat16),
            torch.randn(1, 80, 20, 20).to(torch.bfloat16),
        ]

        result = postproc(reg_list, cls_list)
        assert result["boxes"].dtype == torch.float32
        assert result["scores"].dtype == torch.float32

    def test_scores_bounded(self, postproc):
        """All output scores are in [0, 1] after sigmoid."""
        torch.manual_seed(42)
        reg_list = [
            torch.randn(1, 64, 80, 80),
            torch.randn(1, 64, 40, 40),
            torch.randn(1, 64, 20, 20),
        ]
        cls_list = [
            torch.randn(1, 80, 80, 80) * 3,
            torch.randn(1, 80, 40, 40) * 3,
            torch.randn(1, 80, 20, 20) * 3,
        ]

        result = postproc(reg_list, cls_list)
        if result["scores"].numel() > 0:
            assert (result["scores"] >= 0).all()
            assert (result["scores"] <= 1).all()

    def test_labels_in_range(self, postproc):
        """All output labels are in [0, nc)."""
        torch.manual_seed(123)
        reg_list = [
            torch.randn(1, 64, 80, 80),
            torch.randn(1, 64, 40, 40),
            torch.randn(1, 64, 20, 20),
        ]
        cls_list = [
            torch.randn(1, 80, 80, 80) * 5,
            torch.randn(1, 80, 40, 40) * 5,
            torch.randn(1, 80, 20, 20) * 5,
        ]

        result = postproc(reg_list, cls_list)
        if result["labels"].numel() > 0:
            assert (result["labels"] >= 0).all()
            assert (result["labels"] < postproc.nc).all()
