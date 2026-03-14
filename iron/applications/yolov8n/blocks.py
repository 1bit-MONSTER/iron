# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOv8n composite blocks: CBS, Bottleneck, C2f, SPPF.

These blocks compose existing IRON operators in layer-by-layer fashion.
All data stays in NCHW bfloat16 format between blocks -- layout conversion
happens inside each operator's forward() method.

Each block requires spatial dimensions (height, width) at construction
time because the underlying AIEConv2d/AIEMaxPool2d operators must be
compiled for specific spatial sizes. Pre-compute these from the YOLOv8n
architecture table before building blocks.
"""

import torch
import torch.nn.functional as F

from iron.operators.conv2d.op import AIEConv2d
from iron.operators.maxpool2d.op import AIEMaxPool2d
from iron.common import AIEOperatorConstraintError


def _auto_columns(in_channels, out_channels, kernel_size, width=None, stride=1):
    """Choose num_aie_columns to fit all buffers in L1 (64KB).

    Checks total L1 usage including all FIFO buffers on the compute tile.
    Per-core output channels must be a multiple of 8.

    For 1x1 conv: input depth=2, output depth=2, weight depth=1.
    For 3x3 conv: input depth=4 (sliding window), output depth=2, weight depth=1.

    Args:
        in_channels: Number of input channels.
        out_channels: Number of output channels.
        kernel_size: Convolution kernel size (1 or 3).
        width: Spatial width (enables full L1 check).
        stride: Convolution stride (1 or 2).
    """
    L1_SIZE = 65536
    OVERHEAD = 1040  # stack (1024) + misc (16)
    k_elems = kernel_size * kernel_size
    max_weight = 40 * 1024
    # Try columns: 1, 2, 4, 8 — pick smallest that fits
    for cols in [1, 2, 4, 8]:
        per_core_oc = out_channels // cols if out_channels % cols == 0 else -1
        if per_core_oc < 8 or per_core_oc % 8 != 0:
            continue
        per_core_weight = in_channels * per_core_oc * k_elems * 2
        if width is not None:
            out_w = width // stride if stride > 1 else width
            input_depth = 4 if kernel_size == 3 else 2
            input_bytes = input_depth * in_channels * width * 2
            output_bytes = 2 * per_core_oc * out_w * 2
            total_l1 = OVERHEAD + input_bytes + per_core_weight + output_bytes
            if total_l1 <= L1_SIZE:
                return cols
        else:
            # Unknown width: weight-only check as fallback.
            if per_core_weight <= max_weight:
                return cols
    # Second pass: try with MemTile input routing (L1 input depth=1 instead
    # of 2).  The design.py will route input through MemTile automatically
    # when direct routing overflows L1.
    if kernel_size == 1 and width is not None:
        for cols in [1, 2, 4, 8]:
            per_core_oc = out_channels // cols if out_channels % cols == 0 else -1
            if per_core_oc < 8 or per_core_oc % 8 != 0:
                continue
            per_core_weight = in_channels * per_core_oc * k_elems * 2
            # MemTile routing reduces L1 input depth from 2 to 1
            input_bytes = 1 * in_channels * width * 2
            output_bytes = 2 * per_core_oc * width * 2
            total_l1 = OVERHEAD + input_bytes + per_core_weight + output_bytes
            if total_l1 <= L1_SIZE:
                return cols
    # Third pass: weight streaming via multiple DDR fills per OC group.
    # design.py will automatically stream weights in OC-group chunks.
    # Find smallest column count where the largest possible oc_chunk fits
    # in L1 alongside input/output FIFOs AND n_oc_groups stays within
    # the ShimDMA BD limit (16 BDs per tile).
    MAX_BDS_PER_TILE = 16
    if width is not None:
        for cols in [1, 2, 4, 8]:
            per_core_oc = out_channels // cols if out_channels % cols == 0 else -1
            if per_core_oc < 8 or per_core_oc % 8 != 0:
                continue
            out_w = width // stride if stride > 1 else width
            # Input depth: k1 with MemTile=1, k3=4.
            # k3 sliding window uses acquire(3) which forces depth=4
            # (3 active + 1 prefetch) in the MLIR-AIE framework.
            if kernel_size == 1:
                input_bytes = 1 * in_channels * width * 2
            else:
                input_bytes = 4 * in_channels * width * 2
            avail = L1_SIZE - OVERHEAD - input_bytes
            if avail <= 0:
                continue
            # Try largest oc_chunk first to minimize n_oc_groups
            for try_oc in range(per_core_oc, 0, -8):
                if per_core_oc % try_oc != 0 or try_oc % 8 != 0:
                    continue
                wt_bytes = try_oc * in_channels * k_elems * 2
                out_bytes = 2 * try_oc * out_w * 2
                if wt_bytes + out_bytes <= avail:
                    n_groups = per_core_oc // try_oc
                    # BD count: n_groups input + n_groups weight + 1 output
                    if n_groups * 2 + 1 <= MAX_BDS_PER_TILE:
                        return cols
                    break  # larger oc_chunk won't help, try more columns
    raise AIEOperatorConstraintError(
        f"No feasible NPU mapping: in_channels={in_channels}, "
        f"out_channels={out_channels}, kernel_size={kernel_size}, "
        f"width={width}, stride={stride}. "
        f"Even at 8 columns, weight chunk ({8 * in_channels * k_elems * 2} bytes) "
        f"does not fit in L1 alongside input FIFO "
        f"({'4' if kernel_size == 3 else '1'}*{in_channels}*{width}*2 = "
        f"{(4 if kernel_size == 3 else 1) * in_channels * width * 2} bytes). "
        f"This layer requires IC streaming (not yet implemented)."
    )


class CBS:
    """Conv + BatchNorm + SiLU (BN fused into conv weights+bias).

    This is the fundamental building block of YOLOv8n. Each CBS wraps
    a single AIEConv2d operator with SiLU activation applied in Python
    after the NPU returns the convolution result.

    Args:
        in_channels: Input channels (must be multiple of 8).
        out_channels: Output channels (must be multiple of 8).
        kernel_size: Convolution kernel size (1 or 3).
        stride: Convolution stride (1 or 2; 2 only for kernel_size=3).
        height: Spatial height of the input.
        width: Spatial width of the input.
        num_aie_columns: Number of AIE columns (0=auto based on L1 fit).
        context: AIEContext instance (all operators in a pipeline must
            share the same context so they can be compiled together).
    """

    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        stride=1,
        height=None,
        width=None,
        num_aie_columns=0,
        context=None,
    ):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.height = height
        self.width = width
        self.cpu_fallback = False

        # Compute output spatial dims
        if kernel_size == 3 and stride == 2:
            self.out_height = height // 2
            self.out_width = width // 2
        else:
            self.out_height = height
            self.out_width = width

        if num_aie_columns == 0:
            try:
                num_aie_columns = _auto_columns(
                    in_channels, out_channels, kernel_size, width, stride
                )
            except AIEOperatorConstraintError:
                # Layer is infeasible on NPU (input FIFO alone exceeds L1).
                # Fall back to CPU execution via PyTorch.
                self.cpu_fallback = True
                self.conv = None
                self.weight = None
                self.bias = None
                return

        # Create the underlying AIEConv2d operator with fused bias+SiLU.
        # The kernel applies bias and SiLU on-chip, eliminating the DDR
        # round-trip for these operations.
        self.conv = AIEConv2d(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            stride=stride,
            height=height,
            width=width,
            has_bias=True,
            activation="silu",
            num_aie_columns=num_aie_columns,
            context=context,
        )

        self.weight = None
        self.bias = None

    def load_weights(self, weight, bias):
        """Load fused Conv+BN weights and bias.

        Args:
            weight: Tensor [out_channels, in_channels, kH, kW] in any
                float dtype (will be converted to bfloat16).
            bias: Tensor [out_channels] in any float dtype (will be
                converted to bfloat16).
        """
        self.weight = weight.to(torch.bfloat16)
        self.bias = bias.to(torch.bfloat16)

    def forward(self, x):
        """Run Conv + Bias + SiLU on the NPU (or CPU fallback).

        Args:
            x: Input tensor [1, C_in, H, W] in bfloat16.

        Returns:
            Output tensor [1, C_out, H_out, W_out] in bfloat16.
        """
        if self.cpu_fallback:
            # Layer exceeds NPU L1 budget; run on CPU via PyTorch.
            padding = self.kernel_size // 2
            out = F.conv2d(
                x.float(),
                self.weight.float(),
                self.bias.float(),
                stride=self.stride,
                padding=padding,
            )
            out = F.silu(out)
            return out.to(torch.bfloat16)
        return self.conv.forward(x, self.weight, self.bias)


class Bottleneck:
    """Two 3x3 convolutions with optional residual shortcut.

    Standard YOLOv8n bottleneck block:
        x -> Conv3x3+SiLU -> Conv3x3+SiLU -> [+ residual] -> out

    Both convolutions preserve spatial dimensions (stride=1) and
    channel count.

    Args:
        channels: Number of input/output channels (must be multiple of 8).
        height: Spatial height.
        width: Spatial width.
        shortcut: Whether to add a residual connection (default True).
        num_aie_columns: Number of AIE columns for parallelism.
        context: AIEContext instance.
    """

    def __init__(
        self,
        channels,
        height,
        width,
        shortcut=True,
        num_aie_columns=0,
        context=None,
    ):
        self.channels = channels
        self.height = height
        self.width = width
        self.shortcut = shortcut

        self.cv1 = CBS(
            channels,
            channels,
            kernel_size=3,
            stride=1,
            height=height,
            width=width,
            num_aie_columns=num_aie_columns,
            context=context,
        )
        self.cv2 = CBS(
            channels,
            channels,
            kernel_size=3,
            stride=1,
            height=height,
            width=width,
            num_aie_columns=num_aie_columns,
            context=context,
        )

    def load_weights(self, cv1_weight, cv1_bias, cv2_weight, cv2_bias):
        """Load weights for both convolutions.

        Args:
            cv1_weight: First conv weight [C, C, 3, 3].
            cv1_bias: First conv bias [C].
            cv2_weight: Second conv weight [C, C, 3, 3].
            cv2_bias: Second conv bias [C].
        """
        self.cv1.load_weights(cv1_weight, cv1_bias)
        self.cv2.load_weights(cv2_weight, cv2_bias)

    def forward(self, x):
        """Run bottleneck.

        Args:
            x: Input tensor [1, C, H, W] in bfloat16.

        Returns:
            Output tensor [1, C, H, W] in bfloat16.
        """
        out = self.cv1.forward(x)
        out = self.cv2.forward(out)
        if self.shortcut:
            out = out + x  # elementwise add in Python
        return out


class C2f:
    """Cross-Stage Partial with 2 convolutions and N bottlenecks.

    YOLOv8n C2f structure:
        Input(c_in) -> Conv1x1(c_in -> 2*c) -> chunk(2) ->
            Part_A(c) + Part_B(c)
                            |
                    Bottleneck_1(c -> c)
                            |
                    Bottleneck_n(c -> c)
                            |
            Concat([A, B, BN1...BNn]) = (2+n)*c
                            |
            Conv1x1((2+n)*c -> c_out)
                            |
            Output(c_out)

    Args:
        c_in: Input channels.
        c_out: Output channels.
        n_bottlenecks: Number of bottleneck blocks.
        height: Spatial height (preserved through the block).
        width: Spatial width (preserved through the block).
        shortcut: Whether bottleneck blocks use residual shortcuts.
        num_aie_columns: Number of AIE columns.
        context: AIEContext instance.
    """

    def __init__(
        self,
        c_in,
        c_out,
        n_bottlenecks,
        height,
        width,
        shortcut=True,
        num_aie_columns=0,
        context=None,
    ):
        c = c_out // 2  # hidden channels

        self.c_in = c_in
        self.c_out = c_out
        self.c = c
        self.n_bottlenecks = n_bottlenecks
        self.height = height
        self.width = width

        # cv1: pointwise expand c_in -> 2*c
        self.cv1 = CBS(
            c_in,
            2 * c,
            kernel_size=1,
            stride=1,
            height=height,
            width=width,
            num_aie_columns=num_aie_columns,
            context=context,
        )

        # N bottleneck blocks, all operating on c channels
        self.bottlenecks = [
            Bottleneck(
                c,
                height,
                width,
                shortcut=shortcut,
                num_aie_columns=num_aie_columns,
                context=context,
            )
            for _ in range(n_bottlenecks)
        ]

        # cv2: pointwise reduce (2+n)*c -> c_out
        self.cv2 = CBS(
            (2 + n_bottlenecks) * c,
            c_out,
            kernel_size=1,
            stride=1,
            height=height,
            width=width,
            num_aie_columns=num_aie_columns,
            context=context,
        )

    def load_weights(
        self, cv1_weight, cv1_bias, bottleneck_weights, cv2_weight, cv2_bias
    ):
        """Load weights for the entire C2f block.

        Args:
            cv1_weight: Conv1x1 expand weight [2*c, c_in, 1, 1].
            cv1_bias: Conv1x1 expand bias [2*c].
            bottleneck_weights: List of (cv1_w, cv1_b, cv2_w, cv2_b) tuples,
                one per bottleneck.
            cv2_weight: Conv1x1 reduce weight [c_out, (2+n)*c, 1, 1].
            cv2_bias: Conv1x1 reduce bias [c_out].
        """
        self.cv1.load_weights(cv1_weight, cv1_bias)
        for bn, (w1, b1, w2, b2) in zip(self.bottlenecks, bottleneck_weights):
            bn.load_weights(w1, b1, w2, b2)
        self.cv2.load_weights(cv2_weight, cv2_bias)

    def forward(self, x):
        """Run C2f block.

        Args:
            x: Input tensor [1, c_in, H, W] in bfloat16.

        Returns:
            Output tensor [1, c_out, H, W] in bfloat16.
        """
        # Pointwise expand and split
        x = self.cv1.forward(x)
        chunks = x.chunk(2, dim=1)  # split channels in half (Python)
        outputs = [chunks[0], chunks[1]]

        # Run bottleneck chain -- each feeds from the previous output
        for bn in self.bottlenecks:
            outputs.append(bn.forward(outputs[-1]))

        # Concat all branches along channel dimension
        x = torch.cat(outputs, dim=1)

        # Pointwise reduce
        return self.cv2.forward(x)


class SPPF:
    """Spatial Pyramid Pooling -- Fast.

    SPPF structure:
        Input(c_in) -> Conv1x1(c_in -> c_) -> [identity, MP5, MP5, MP5]
                                                    |
                                             Concat(c_ * 4)
                                                    |
                                             Conv1x1(c_*4 -> c_out)
                                                    |
                                               Output(c_out)

    Three cascaded 5x5 max pools with stride=1 and padding=2 produce the
    same receptive field as a single 13x13 pool (5 + 5 + 5 - 2 = 13).

    Args:
        c_in: Input channels.
        c_out: Output channels.
        height: Spatial height (preserved by stride-1 pooling with padding).
        width: Spatial width (preserved).
        kernel_size: Max pool kernel size (default 5).
        num_aie_columns: Number of AIE columns.
        context: AIEContext instance.
    """

    def __init__(
        self,
        c_in,
        c_out,
        height,
        width,
        kernel_size=5,
        num_aie_columns=0,
        context=None,
    ):
        c_ = c_in // 2  # hidden channels

        self.c_in = c_in
        self.c_out = c_out
        self.c_ = c_
        self.height = height
        self.width = width

        # cv1: pointwise reduce c_in -> c_
        self.cv1 = CBS(
            c_in,
            c_,
            kernel_size=1,
            stride=1,
            height=height,
            width=width,
            num_aie_columns=num_aie_columns,
            context=context,
        )

        # Three MaxPool2d instances -- all share the same spatial dims
        # and channel count but need separate operator instances since
        # they may be compiled with different artifact names.
        padding = kernel_size // 2
        self.mp1 = AIEMaxPool2d(
            channels=c_,
            height=height,
            width=width,
            kernel_size=kernel_size,
            stride=1,
            padding=padding,
            num_aie_columns=num_aie_columns,
            context=context,
        )
        self.mp2 = AIEMaxPool2d(
            channels=c_,
            height=height,
            width=width,
            kernel_size=kernel_size,
            stride=1,
            padding=padding,
            num_aie_columns=num_aie_columns,
            context=context,
        )
        self.mp3 = AIEMaxPool2d(
            channels=c_,
            height=height,
            width=width,
            kernel_size=kernel_size,
            stride=1,
            padding=padding,
            num_aie_columns=num_aie_columns,
            context=context,
        )

        # cv2: pointwise expand c_*4 -> c_out
        self.cv2 = CBS(
            c_ * 4,
            c_out,
            kernel_size=1,
            stride=1,
            height=height,
            width=width,
            num_aie_columns=num_aie_columns,
            context=context,
        )

    def load_weights(self, cv1_weight, cv1_bias, cv2_weight, cv2_bias):
        """Load weights for SPPF conv layers (max pool has no weights).

        Args:
            cv1_weight: First conv weight [c_, c_in, 1, 1].
            cv1_bias: First conv bias [c_].
            cv2_weight: Second conv weight [c_out, c_*4, 1, 1].
            cv2_bias: Second conv bias [c_out].
        """
        self.cv1.load_weights(cv1_weight, cv1_bias)
        self.cv2.load_weights(cv2_weight, cv2_bias)

    def forward(self, x):
        """Run SPPF block.

        Args:
            x: Input tensor [1, c_in, H, W] in bfloat16.

        Returns:
            Output tensor [1, c_out, H, W] in bfloat16.
        """
        x = self.cv1.forward(x)
        y1 = self.mp1.forward(x)
        y2 = self.mp2.forward(y1)
        y3 = self.mp3.forward(y2)
        x = torch.cat([x, y1, y2, y3], dim=1)  # concat in Python
        return self.cv2.forward(x)
