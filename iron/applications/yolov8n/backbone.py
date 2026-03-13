# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOv8n backbone: layers 0-9.

The backbone extracts multi-scale features from a 640x640 input image.
It produces three feature maps at different resolutions for the
detection neck:
    P3: 80x80x64   (stride 8)
    P4: 40x40x128  (stride 16)
    P5: 20x20x256  (stride 32)

All operators are pre-instantiated with known spatial dimensions from
the YOLOv8n architecture. Data flows through layer-by-layer NPU
invocations with NCHW bfloat16 tensors passed between layers via DDR.
"""

import torch
import torch.nn.functional as F

from iron.applications.yolov8n.blocks import CBS, C2f, SPPF


class YOLOv8nBackbone:
    """YOLOv8n backbone (layers 0-9).

    Pre-instantiates all operators for the fixed 640x640 input size.
    Each operator is compiled for its exact spatial dimensions. The
    context must not have ``prepare_runtime()`` called before all
    operators are created.

    Spatial dimension trace through the backbone:
        L0: Conv3x3 s2   (8,16)   640x640  -> 320x320
        L1: Conv3x3 s2   (16,32)  320x320  -> 160x160
        L2: C2f n=1      (32,32)  160x160  -> 160x160
        L3: Conv3x3 s2   (32,64)  160x160  -> 80x80
        L4: C2f n=2      (64,64)  80x80    -> 80x80    [P3 skip]
        L5: Conv3x3 s2   (64,128) 80x80    -> 40x40
        L6: C2f n=2      (128,128)40x40    -> 40x40    [P4 skip]
        L7: Conv3x3 s2   (128,256)40x40    -> 20x20
        L8: C2f n=1      (256,256)20x20    -> 20x20
        L9: SPPF k=5     (256,256)20x20    -> 20x20    [P5 skip]

    Args:
        context: AIEContext instance. All operators register with this
            context for joint compilation and runtime setup.
        num_aie_columns: Number of AIE columns per operator (default 1).
    """

    def __init__(self, context=None, num_aie_columns=1):
        cols = num_aie_columns

        # L0: Conv3x3 s2, 8->16, 640->320
        # NOTE: Input image is RGB (3ch) padded to 8ch before this layer.
        self.l0 = CBS(
            8,
            16,
            kernel_size=3,
            stride=2,
            height=640,
            width=640,
            num_aie_columns=cols,
            context=context,
        )

        # L1: Conv3x3 s2, 16->32, 320->160
        self.l1 = CBS(
            16,
            32,
            kernel_size=3,
            stride=2,
            height=320,
            width=320,
            num_aie_columns=cols,
            context=context,
        )

        # L2: C2f n=1, 32->32, 160x160, shortcut=True
        self.l2 = C2f(
            32,
            32,
            n_bottlenecks=1,
            height=160,
            width=160,
            shortcut=True,
            num_aie_columns=cols,
            context=context,
        )

        # L3: Conv3x3 s2, 32->64, 160->80
        self.l3 = CBS(
            32,
            64,
            kernel_size=3,
            stride=2,
            height=160,
            width=160,
            num_aie_columns=cols,
            context=context,
        )

        # L4: C2f n=2, 64->64, 80x80, shortcut=True
        self.l4 = C2f(
            64,
            64,
            n_bottlenecks=2,
            height=80,
            width=80,
            shortcut=True,
            num_aie_columns=cols,
            context=context,
        )

        # L5: Conv3x3 s2, 64->128, 80->40
        self.l5 = CBS(
            64,
            128,
            kernel_size=3,
            stride=2,
            height=80,
            width=80,
            num_aie_columns=cols,
            context=context,
        )

        # L6: C2f n=2, 128->128, 40x40, shortcut=True
        self.l6 = C2f(
            128,
            128,
            n_bottlenecks=2,
            height=40,
            width=40,
            shortcut=True,
            num_aie_columns=cols,
            context=context,
        )

        # L7: Conv3x3 s2, 128->256, 40->20
        self.l7 = CBS(
            128,
            256,
            kernel_size=3,
            stride=2,
            height=40,
            width=40,
            num_aie_columns=cols,
            context=context,
        )

        # L8: C2f n=1, 256->256, 20x20, shortcut=True
        self.l8 = C2f(
            256,
            256,
            n_bottlenecks=1,
            height=20,
            width=20,
            shortcut=True,
            num_aie_columns=cols,
            context=context,
        )

        # L9: SPPF k=5, 256->256, 20x20
        self.l9 = SPPF(
            256,
            256,
            height=20,
            width=20,
            kernel_size=5,
            num_aie_columns=cols,
            context=context,
        )

    def load_weights(self, weights):
        """Load all backbone weights from a weight dictionary.

        Args:
            weights: Dictionary mapping layer names to weight dictionaries.
                Expected keys: 'l0' through 'l9', each containing the
                appropriate weight/bias tensors for its block type.

                For CBS layers (l0, l1, l3, l5, l7):
                    {'weight': Tensor, 'bias': Tensor}
                For C2f layers (l2, l4, l6, l8):
                    {'cv1_weight': Tensor, 'cv1_bias': Tensor,
                     'bottlenecks': [(cv1_w, cv1_b, cv2_w, cv2_b), ...],
                     'cv2_weight': Tensor, 'cv2_bias': Tensor}
                For SPPF (l9):
                    {'cv1_weight': Tensor, 'cv1_bias': Tensor,
                     'cv2_weight': Tensor, 'cv2_bias': Tensor}
        """
        # CBS layers
        for name in ["l0", "l1", "l3", "l5", "l7"]:
            layer = getattr(self, name)
            w = weights[name]
            layer.load_weights(w["weight"], w["bias"])

        # C2f layers
        for name in ["l2", "l4", "l6", "l8"]:
            layer = getattr(self, name)
            w = weights[name]
            layer.load_weights(
                w["cv1_weight"],
                w["cv1_bias"],
                w["bottlenecks"],
                w["cv2_weight"],
                w["cv2_bias"],
            )

        # SPPF
        w = weights["l9"]
        self.l9.load_weights(
            w["cv1_weight"],
            w["cv1_bias"],
            w["cv2_weight"],
            w["cv2_bias"],
        )

    def forward(self, x):
        """Run backbone on a 640x640 input image.

        Args:
            x: Input tensor [1, 3, 640, 640] in bfloat16.

        Returns:
            Dictionary with skip connection feature maps:
                'p3': [1, 64, 80, 80]   (layer 4 output)
                'p4': [1, 128, 40, 40]  (layer 6 output)
                'p5': [1, 256, 20, 20]  (layer 9 output)
        """
        # Pad RGB (3ch) to 8 channels for AIE alignment
        # F.pad order: (W_left, W_right, H_top, H_bot, C_front, C_back)
        x = F.pad(x, (0, 0, 0, 0, 0, 5))  # [1, 8, 640, 640]

        x = self.l0.forward(x)  # [1, 16, 320, 320]
        x = self.l1.forward(x)  # [1, 32, 160, 160]
        x = self.l2.forward(x)  # [1, 32, 160, 160]
        x = self.l3.forward(x)  # [1, 64, 80, 80]
        p3 = self.l4.forward(x)  # [1, 64, 80, 80]   -> skip to neck L14

        x = self.l5.forward(p3)  # [1, 128, 40, 40]
        p4 = self.l6.forward(x)  # [1, 128, 40, 40]  -> skip to neck L11

        x = self.l7.forward(p4)  # [1, 256, 20, 20]
        x = self.l8.forward(x)  # [1, 256, 20, 20]
        p5 = self.l9.forward(x)  # [1, 256, 20, 20]  -> skip to neck L20

        return {"p3": p3, "p4": p4, "p5": p5}
