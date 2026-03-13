# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOv8n neck: FPN up-path + PAN down-path.

The neck takes three skip connection feature maps from the backbone
(P3, P4, P5) and produces three multi-scale feature maps for the
detect head:
    det_p3: 80x80x64   (stride 8)
    det_p4: 40x40x128  (stride 16)
    det_p5: 20x20x256  (stride 32)

Architecture (layers 10-21):
    FPN up-path:
        L10: Upsample 2x (20x20x256 -> 40x40x256)
        L11: Concat       (40x40x256 + P4=40x40x128 -> 40x40x384)
        L12: C2f           (384->128, 40x40, n=1, shortcut=False)
        L13: Upsample 2x  (40x40x128 -> 80x80x128)
        L14: Concat        (80x80x128 + P3=80x80x64 -> 80x80x192)
        L15: C2f           (192->64, 80x80, n=1, shortcut=False)

    PAN down-path:
        L16: CBS 3x3 s2   (80x80x64 -> 40x40x64)
        L17: Concat        (40x40x64 + L12=40x40x128 -> 40x40x192)
        L18: C2f           (192->128, 40x40, n=1, shortcut=False)
        L19: CBS 3x3 s2   (40x40x128 -> 20x20x128)
        L20: Concat        (20x20x128 + P5=20x20x256 -> 20x20x384)
        L21: C2f           (384->256, 20x20, n=1, shortcut=False)

Concat operations are host-side torch.cat() between NPU calls.
"""

import torch

from iron.applications.yolov8n.blocks import CBS, C2f
from iron.operators.upsample.op import AIEUpsample


class YOLOv8nNeck:
    """YOLOv8n Neck: FPN up-path + PAN down-path.

    Takes backbone skip connections {p3, p4, p5} and produces three
    multi-scale feature maps for the detect head.

    All operators are pre-instantiated with known spatial dimensions
    from the YOLOv8n architecture. The context must not have
    ``prepare_runtime()`` called before all operators are created.

    Args:
        context: AIEContext instance. All operators register with this
            context for joint compilation and runtime setup.
        num_aie_columns: Number of AIE columns per operator (default 1).
    """

    def __init__(self, context=None, num_aie_columns=1):
        cols = num_aie_columns

        # ----- FPN up-path -----

        # L10: Upsample 2x (20x20x256 -> 40x40x256)
        self.up1 = AIEUpsample(
            channels=256,
            height=20,
            width=20,
            scale_factor=2,
            num_aie_columns=cols,
            context=context,
        )

        # L12: C2f (384->128, 40x40, n=1, shortcut=False)
        self.l12 = C2f(
            384,
            128,
            n_bottlenecks=1,
            height=40,
            width=40,
            shortcut=False,
            num_aie_columns=cols,
            context=context,
        )

        # L13: Upsample 2x (40x40x128 -> 80x80x128)
        self.up2 = AIEUpsample(
            channels=128,
            height=40,
            width=40,
            scale_factor=2,
            num_aie_columns=cols,
            context=context,
        )

        # L15: C2f (192->64, 80x80, n=1, shortcut=False)
        self.l15 = C2f(
            192,
            64,
            n_bottlenecks=1,
            height=80,
            width=80,
            shortcut=False,
            num_aie_columns=cols,
            context=context,
        )

        # ----- PAN down-path -----

        # L16: CBS 3x3 s2 (64->64, 80x80 -> 40x40)
        self.l16 = CBS(
            64,
            64,
            kernel_size=3,
            stride=2,
            height=80,
            width=80,
            num_aie_columns=cols,
            context=context,
        )

        # L18: C2f (192->128, 40x40, n=1, shortcut=False)
        self.l18 = C2f(
            192,
            128,
            n_bottlenecks=1,
            height=40,
            width=40,
            shortcut=False,
            num_aie_columns=cols,
            context=context,
        )

        # L19: CBS 3x3 s2 (128->128, 40x40 -> 20x20)
        self.l19 = CBS(
            128,
            128,
            kernel_size=3,
            stride=2,
            height=40,
            width=40,
            num_aie_columns=cols,
            context=context,
        )

        # L21: C2f (384->256, 20x20, n=1, shortcut=False)
        self.l21 = C2f(
            384,
            256,
            n_bottlenecks=1,
            height=20,
            width=20,
            shortcut=False,
            num_aie_columns=cols,
            context=context,
        )

    def load_weights(self, weights):
        """Load all neck weights from a weight dictionary.

        Args:
            weights: Dictionary mapping layer names to weight dictionaries.
                Expected keys:
                    'l12', 'l15', 'l18', 'l21' (C2f):
                        {'cv1_weight': Tensor, 'cv1_bias': Tensor,
                         'bottlenecks': [(cv1_w, cv1_b, cv2_w, cv2_b), ...],
                         'cv2_weight': Tensor, 'cv2_bias': Tensor}
                    'l16', 'l19' (CBS):
                        {'weight': Tensor, 'bias': Tensor}
                Upsample layers (up1, up2) have no weights.
        """
        # CBS layers
        for name in ["l16", "l19"]:
            layer = getattr(self, name)
            w = weights[name]
            layer.load_weights(w["weight"], w["bias"])

        # C2f layers
        for name in ["l12", "l15", "l18", "l21"]:
            layer = getattr(self, name)
            w = weights[name]
            layer.load_weights(
                w["cv1_weight"],
                w["cv1_bias"],
                w["bottlenecks"],
                w["cv2_weight"],
                w["cv2_bias"],
            )

    def forward(self, p3, p4, p5):
        """Run neck on backbone skip connections.

        Args:
            p3: Tensor [1, 64, 80, 80] from backbone L4.
            p4: Tensor [1, 128, 40, 40] from backbone L6.
            p5: Tensor [1, 256, 20, 20] from backbone L9.

        Returns:
            Tuple of (det_p3, det_p4, det_p5):
                det_p3: [1, 64, 80, 80]
                det_p4: [1, 128, 40, 40]
                det_p5: [1, 256, 20, 20]
        """
        # ----- FPN up-path -----

        # L10: Upsample P5 (20x20 -> 40x40)
        x = self.up1.forward(p5)  # [1, 256, 40, 40]

        # L11: Concat with P4
        x = torch.cat([x, p4], dim=1)  # [1, 384, 40, 40]

        # L12: C2f
        l12_out = self.l12.forward(x)  # [1, 128, 40, 40]

        # L13: Upsample (40x40 -> 80x80)
        x = self.up2.forward(l12_out)  # [1, 128, 80, 80]

        # L14: Concat with P3
        x = torch.cat([x, p3], dim=1)  # [1, 192, 80, 80]

        # L15: C2f -> det_p3
        det_p3 = self.l15.forward(x)  # [1, 64, 80, 80]

        # ----- PAN down-path -----

        # L16: CBS 3x3 s2
        x = self.l16.forward(det_p3)  # [1, 64, 40, 40]

        # L17: Concat with L12 output
        x = torch.cat([x, l12_out], dim=1)  # [1, 192, 40, 40]

        # L18: C2f -> det_p4
        det_p4 = self.l18.forward(x)  # [1, 128, 40, 40]

        # L19: CBS 3x3 s2
        x = self.l19.forward(det_p4)  # [1, 128, 20, 20]

        # L20: Concat with P5
        x = torch.cat([x, p5], dim=1)  # [1, 384, 20, 20]

        # L21: C2f -> det_p5
        det_p5 = self.l21.forward(x)  # [1, 256, 20, 20]

        return det_p3, det_p4, det_p5
