# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOv8n post-processing: DFL decode + anchor-free bbox conversion + NMS.

Converts raw detect head outputs (reg + cls per scale) into final bounding
box predictions with class labels and confidence scores.

Pipeline:
    1. Flatten reg/cls tensors across 3 scales into [N_anchors, C] format
    2. Generate anchor grid points for each scale (strides 8, 16, 32)
    3. DFL decode: softmax over 16 bins per box edge -> expected distance
    4. dist2bbox: convert (left, top, right, bottom) distances to (x1, y1, x2, y2)
    5. Sigmoid on class logits to get confidence scores
    6. NMS to remove duplicate detections
"""

import torch
import torch.nn.functional as F


class YOLOv8nPostProcess:
    """Post-processor for YOLOv8n detect head outputs.

    Args:
        nc: Number of classes (default 80 for COCO).
        reg_max: Number of DFL distribution bins per box edge (default 16).
        strides: Feature map strides for each scale level.
        img_size: Input image size (assumes square).
        conf_thres: Confidence threshold for filtering detections.
        iou_thres: IoU threshold for NMS.
    """

    def __init__(
        self,
        nc=80,
        reg_max=16,
        strides=None,
        img_size=640,
        conf_thres=0.25,
        iou_thres=0.45,
    ):
        if strides is None:
            strides = [8, 16, 32]
        self.nc = nc
        self.reg_max = reg_max
        self.strides = strides
        self.img_size = img_size
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres

        # Pre-compute DFL projection vector: [0, 1, ..., reg_max-1]
        self.dfl_proj = torch.arange(reg_max, dtype=torch.float32)

        # Pre-compute anchor points and stride tensor
        self.anchor_points, self.stride_tensor = self._make_anchors()

    def _make_anchors(self):
        """Generate anchor center points and corresponding stride tensor.

        For each scale, creates a grid of (cx, cy) anchor centers at the
        center of each cell (offset by 0.5), in units of pixels.

        Returns:
            anchor_points: Tensor [N_total, 2] of (cx, cy) in pixel coords.
            stride_tensor: Tensor [N_total, 1] of stride per anchor.
        """
        anchor_points = []
        stride_tensor = []

        for stride in self.strides:
            h = self.img_size // stride
            w = self.img_size // stride
            # Grid of cell centers
            sy, sx = torch.meshgrid(
                torch.arange(h, dtype=torch.float32),
                torch.arange(w, dtype=torch.float32),
                indexing="ij",
            )
            # Offset to cell center and scale to pixel coordinates
            grid = torch.stack((sx, sy), dim=-1).reshape(-1, 2) + 0.5
            anchor_points.append(grid * stride)
            stride_tensor.append(torch.full((h * w, 1), stride, dtype=torch.float32))

        return torch.cat(anchor_points, dim=0), torch.cat(stride_tensor, dim=0)

    def _flatten_preds(self, pred_list):
        """Flatten [1, C, H, W] predictions across scales to [N, C].

        Args:
            pred_list: List of 3 tensors, one per scale:
                [1, C, H_i, W_i] for i in {P3, P4, P5}.

        Returns:
            Tensor [N_total, C] where N_total = sum(H_i * W_i).
        """
        flat = []
        for pred in pred_list:
            # [1, C, H, W] -> [H*W, C]
            b, c, h, w = pred.shape
            flat.append(pred.squeeze(0).permute(1, 2, 0).reshape(-1, c))
        return torch.cat(flat, dim=0)

    def _dfl_decode(self, reg_flat):
        """Apply Distribution Focal Loss decode to regression predictions.

        Takes raw regression logits [N, 4*reg_max] and produces expected
        distances [N, 4] via softmax over each group of reg_max bins.

        Args:
            reg_flat: Tensor [N, 4 * reg_max] of raw regression logits.

        Returns:
            Tensor [N, 4] of decoded distances (left, top, right, bottom)
            in stride units.
        """
        n = reg_flat.shape[0]
        # Reshape to [N, 4, reg_max] - one distribution per box edge
        reg = reg_flat.reshape(n, 4, self.reg_max)
        # Softmax over bins, then dot product with [0..reg_max-1]
        weights = F.softmax(reg, dim=-1)
        return (weights * self.dfl_proj.to(reg.device)).sum(dim=-1)

    def _dist2bbox(self, distances, anchor_points):
        """Convert distance predictions to bounding boxes.

        Args:
            distances: Tensor [N, 4] of (left, top, right, bottom) in pixels.
            anchor_points: Tensor [N, 2] of (cx, cy) anchor centers in pixels.

        Returns:
            Tensor [N, 4] of (x1, y1, x2, y2) bounding boxes in pixels.
        """
        lt = distances[:, :2]  # left, top
        rb = distances[:, 2:]  # right, bottom
        x1y1 = anchor_points - lt
        x2y2 = anchor_points + rb
        return torch.cat([x1y1, x2y2], dim=-1)

    @staticmethod
    def _nms(boxes, scores, iou_thres):
        """Greedy Non-Maximum Suppression.

        Args:
            boxes: Tensor [N, 4] of (x1, y1, x2, y2).
            scores: Tensor [N] of confidence scores.
            iou_thres: IoU threshold for suppression.

        Returns:
            Tensor of indices to keep, sorted by descending score.
        """
        x1 = boxes[:, 0]
        y1 = boxes[:, 1]
        x2 = boxes[:, 2]
        y2 = boxes[:, 3]
        areas = (x2 - x1) * (y2 - y1)

        order = scores.argsort(descending=True)
        keep = []

        while order.numel() > 0:
            i = order[0].item()
            keep.append(i)

            if order.numel() == 1:
                break

            rest = order[1:]
            xx1 = torch.clamp(x1[rest], min=x1[i].item())
            yy1 = torch.clamp(y1[rest], min=y1[i].item())
            xx2 = torch.clamp(x2[rest], max=x2[i].item())
            yy2 = torch.clamp(y2[rest], max=y2[i].item())

            inter = torch.clamp(xx2 - xx1, min=0) * torch.clamp(yy2 - yy1, min=0)
            union = areas[i] + areas[rest] - inter
            iou = inter / union

            remaining = (iou <= iou_thres).nonzero(as_tuple=True)[0]
            order = rest[remaining]

        return torch.tensor(keep, dtype=torch.long)

    def __call__(self, reg_list, cls_list):
        """Run full post-processing pipeline.

        Args:
            reg_list: List of 3 regression tensors from detect head:
                [1, 64, 80, 80], [1, 64, 40, 40], [1, 64, 20, 20].
            cls_list: List of 3 classification tensors from detect head:
                [1, 80, 80, 80], [1, 80, 40, 40], [1, 80, 20, 20].

        Returns:
            Dictionary with:
                'boxes': Tensor [N, 4] of (x1, y1, x2, y2) in pixel coords.
                'scores': Tensor [N] of confidence scores.
                'labels': Tensor [N] of class indices (int64).
            Where N is the number of detections after NMS. Returns empty
            tensors if no detections pass the confidence threshold.
        """
        # Ensure float32 for post-processing math
        reg_list = [r.float() for r in reg_list]
        cls_list = [c.float() for c in cls_list]

        # 1. Flatten across scales: [N_total, C]
        reg_flat = self._flatten_preds(reg_list)  # [N, 64]
        cls_flat = self._flatten_preds(cls_list)  # [N, 80]

        # 2. DFL decode: [N, 64] -> [N, 4] distances in stride units
        dist = self._dfl_decode(reg_flat)

        # 3. Scale distances to pixel coordinates
        anchors = self.anchor_points.to(dist.device)
        strides = self.stride_tensor.to(dist.device)
        dist_pixels = dist * strides

        # 4. dist2bbox: distances -> (x1, y1, x2, y2) boxes
        boxes = self._dist2bbox(dist_pixels, anchors)

        # 5. Sigmoid class scores
        scores = cls_flat.sigmoid()

        # 6. Confidence filter: max class score > threshold
        max_scores, max_labels = scores.max(dim=1)
        keep_mask = max_scores > self.conf_thres

        if not keep_mask.any():
            return {
                "boxes": torch.empty((0, 4), dtype=torch.float32),
                "scores": torch.empty((0,), dtype=torch.float32),
                "labels": torch.empty((0,), dtype=torch.int64),
            }

        boxes = boxes[keep_mask]
        max_scores = max_scores[keep_mask]
        max_labels = max_labels[keep_mask]

        # 7. NMS per class (offset trick: shift boxes by class to avoid
        # cross-class suppression)
        class_offsets = max_labels.float() * self.img_size
        boxes_for_nms = boxes + class_offsets.unsqueeze(1)
        nms_keep = self._nms(boxes_for_nms, max_scores, self.iou_thres)

        return {
            "boxes": boxes[nms_keep],
            "scores": max_scores[nms_keep],
            "labels": max_labels[nms_keep],
        }
