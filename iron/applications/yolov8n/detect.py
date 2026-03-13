# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOv8n detect head: decoupled regression + classification.

The detect head runs independently at each of three scales (P3, P4, P5).
Each scale has two branches:

    Regression branch:
        CBS(3x3, C_in -> 64) -> CBS(3x3, 64 -> 64) -> Conv1x1(64 -> 64)
        Output: [1, 64, H, W]  (4 * reg_max=16 distribution bins)

    Classification branch:
        CBS(3x3, C_in -> 80) -> CBS(3x3, 80 -> 80) -> Conv1x1(80 -> 80)
        Output: [1, 80, H, W]  (80 COCO classes)

Where C_in varies per scale:
    P3: C_in=64  (80x80)
    P4: C_in=128 (40x40)
    P5: C_in=256 (20x20)

The final Conv1x1 in each branch has NO BatchNorm and NO SiLU activation
-- it is a bare convolution with bias. CBS layers handle SiLU internally.
"""

from iron.applications.yolov8n.blocks import CBS, _auto_columns
from iron.operators.conv2d.op import AIEConv2d


class DetectBranch:
    """One branch (regression or classification) of the detect head
    at one scale.

    Structure:
        CBS(3x3, c_in -> c_mid)  [Conv + SiLU]
        CBS(3x3, c_mid -> c_mid) [Conv + SiLU]
        Conv1x1(c_mid -> c_out)  [bare conv with bias, no activation]

    Args:
        c_in: Input channels from the neck feature map.
        c_mid: Intermediate channels (64 for reg, 80 for cls).
        c_out: Output channels (64 for reg, 80 for cls).
        height: Spatial height of the feature map.
        width: Spatial width of the feature map.
        num_aie_columns: Number of AIE columns for parallelism.
        context: AIEContext instance.
    """

    def __init__(
        self,
        c_in,
        c_mid,
        c_out,
        height,
        width,
        num_aie_columns=0,
        context=None,
    ):
        self.c_in = c_in
        self.c_mid = c_mid
        self.c_out = c_out
        self.height = height
        self.width = width

        # CBS layers: Conv3x3 + BN(fused) + SiLU
        self.cv1 = CBS(
            c_in,
            c_mid,
            kernel_size=3,
            stride=1,
            height=height,
            width=width,
            num_aie_columns=num_aie_columns,
            context=context,
        )

        self.cv2 = CBS(
            c_mid,
            c_mid,
            kernel_size=3,
            stride=1,
            height=height,
            width=width,
            num_aie_columns=num_aie_columns,
            context=context,
        )

        # Final 1x1 conv: no BN, no activation (bare conv with bias)
        cv3_cols = _auto_columns(c_mid, c_out, 1) if num_aie_columns == 0 else num_aie_columns
        self.cv3 = AIEConv2d(
            in_channels=c_mid,
            out_channels=c_out,
            kernel_size=1,
            stride=1,
            height=height,
            width=width,
            has_bias=True,
            activation=None,
            num_aie_columns=cv3_cols,
            context=context,
        )

        self.cv3_weight = None
        self.cv3_bias = None

    def load_weights(
        self, cv1_weight, cv1_bias, cv2_weight, cv2_bias, cv3_weight, cv3_bias
    ):
        """Load weights for all three convolutions.

        Args:
            cv1_weight: First CBS weight [c_mid, c_in, 3, 3].
            cv1_bias: First CBS bias [c_mid].
            cv2_weight: Second CBS weight [c_mid, c_mid, 3, 3].
            cv2_bias: Second CBS bias [c_mid].
            cv3_weight: Final 1x1 weight [c_out, c_mid, 1, 1].
            cv3_bias: Final 1x1 bias [c_out].
        """
        self.cv1.load_weights(cv1_weight, cv1_bias)
        self.cv2.load_weights(cv2_weight, cv2_bias)
        self.cv3_weight = cv3_weight
        self.cv3_bias = cv3_bias

    def forward(self, x):
        """Run detect branch.

        Args:
            x: Input tensor [1, c_in, H, W] in bfloat16.

        Returns:
            Output tensor [1, c_out, H, W] in bfloat16.
        """
        x = self.cv1.forward(x)  # Conv3x3 + SiLU
        x = self.cv2.forward(x)  # Conv3x3 + SiLU
        x = self.cv3.forward(
            x, self.cv3_weight, self.cv3_bias
        )  # Conv1x1, no activation
        return x


class YOLOv8nDetect:
    """YOLOv8n Detect Head: decoupled regression + classification.

    Creates six DetectBranch instances (regression + classification
    at each of three scales). Each branch is independently compiled
    and executed.

    Args:
        nc: Number of classes (default 80 for COCO).
        reg_max: DFL regression max bins (default 16, output = 4*reg_max=64).
        context: AIEContext instance.
        num_aie_columns: Number of AIE columns per operator (default 1).
    """

    def __init__(self, nc=80, reg_max=16, context=None, num_aie_columns=1):
        self.nc = nc
        self.reg_max = reg_max
        c_reg = 4 * reg_max  # 64 regression output channels
        c_cls = nc  # 80 classification output channels

        # Intermediate channel widths (from YOLOv8n architecture)
        c2 = 64  # regression intermediate
        c3 = max(nc, 16)  # classification intermediate (80 for COCO)

        # Scale definitions: (c_in, height, width)
        scales = {
            "p3": (64, 80, 80),
            "p4": (128, 40, 40),
            "p5": (256, 20, 20),
        }

        # Regression branches (one per scale)
        self.reg_p3 = DetectBranch(
            scales["p3"][0],
            c2,
            c_reg,
            scales["p3"][1],
            scales["p3"][2],
            num_aie_columns=num_aie_columns,
            context=context,
        )
        self.reg_p4 = DetectBranch(
            scales["p4"][0],
            c2,
            c_reg,
            scales["p4"][1],
            scales["p4"][2],
            num_aie_columns=num_aie_columns,
            context=context,
        )
        self.reg_p5 = DetectBranch(
            scales["p5"][0],
            c2,
            c_reg,
            scales["p5"][1],
            scales["p5"][2],
            num_aie_columns=num_aie_columns,
            context=context,
        )

        # Classification branches (one per scale)
        self.cls_p3 = DetectBranch(
            scales["p3"][0],
            c3,
            c_cls,
            scales["p3"][1],
            scales["p3"][2],
            num_aie_columns=num_aie_columns,
            context=context,
        )
        self.cls_p4 = DetectBranch(
            scales["p4"][0],
            c3,
            c_cls,
            scales["p4"][1],
            scales["p4"][2],
            num_aie_columns=num_aie_columns,
            context=context,
        )
        self.cls_p5 = DetectBranch(
            scales["p5"][0],
            c3,
            c_cls,
            scales["p5"][1],
            scales["p5"][2],
            num_aie_columns=num_aie_columns,
            context=context,
        )

    def load_weights(self, weights):
        """Load all detect head weights from a weight dictionary.

        Args:
            weights: Dictionary mapping branch names to weight tuples.
                Expected keys: 'reg_p3', 'reg_p4', 'reg_p5',
                               'cls_p3', 'cls_p4', 'cls_p5'.
                Each value is a dict with keys:
                    'cv1_weight', 'cv1_bias',
                    'cv2_weight', 'cv2_bias',
                    'cv3_weight', 'cv3_bias'
        """
        for name in ["reg_p3", "reg_p4", "reg_p5", "cls_p3", "cls_p4", "cls_p5"]:
            branch = getattr(self, name)
            w = weights[name]
            branch.load_weights(
                w["cv1_weight"],
                w["cv1_bias"],
                w["cv2_weight"],
                w["cv2_bias"],
                w["cv3_weight"],
                w["cv3_bias"],
            )

    def forward(self, det_p3, det_p4, det_p5):
        """Run detect head on neck outputs.

        Args:
            det_p3: Tensor [1, 64, 80, 80] from neck.
            det_p4: Tensor [1, 128, 40, 40] from neck.
            det_p5: Tensor [1, 256, 20, 20] from neck.

        Returns:
            Dictionary with raw predictions before post-processing:
                'reg': [reg_p3, reg_p4, reg_p5]
                    reg_p3: [1, 64, 80, 80]
                    reg_p4: [1, 64, 40, 40]
                    reg_p5: [1, 64, 20, 20]
                'cls': [cls_p3, cls_p4, cls_p5]
                    cls_p3: [1, 80, 80, 80]
                    cls_p4: [1, 80, 40, 40]
                    cls_p5: [1, 80, 20, 20]
        """
        reg3 = self.reg_p3.forward(det_p3)  # [1, 64, 80, 80]
        cls3 = self.cls_p3.forward(det_p3)  # [1, 80, 80, 80]

        reg4 = self.reg_p4.forward(det_p4)  # [1, 64, 40, 40]
        cls4 = self.cls_p4.forward(det_p4)  # [1, 80, 40, 40]

        reg5 = self.reg_p5.forward(det_p5)  # [1, 64, 20, 20]
        cls5 = self.cls_p5.forward(det_p5)  # [1, 80, 20, 20]

        return {
            "reg": [reg3, reg4, reg5],
            "cls": [cls3, cls4, cls5],
        }
