# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from pathlib import Path

from iron.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


def nchw_to_tiled_int8(tensor):
    """Convert [N, C, H, W] int8 tensor to tiled layout [H, C/8, W, 8] flattened.

    Args:
        tensor: PyTorch tensor of shape [N, C, H, W] (N must be 1), int8.

    Returns:
        1D numpy array in int8 with layout [H, C/8, W, 8].
    """
    assert tensor.shape[0] == 1, "Batch size must be 1"
    N, C, H, W = tensor.shape
    assert C % 8 == 0, f"Channels ({C}) must be a multiple of 8"

    t = tensor[0]  # [C, H, W]
    t = t.reshape(C // 8, 8, H, W)  # [C/8, 8, H, W]
    t = t.permute(2, 0, 3, 1)  # [H, C/8, W, 8]
    t = t.contiguous()
    return t.numpy().astype(np.int8).reshape(-1)


def tiled_to_nchw_int8(flat, C, H, W):
    """Convert flat tiled [H, C/8, W, 8] int8 back to [1, C, H, W].

    Args:
        flat: 1D numpy array in int8 of size H * C * W.
        C: Number of channels.
        H: Spatial height.
        W: Spatial width.

    Returns:
        PyTorch tensor of shape [1, C, H, W] in int8.
    """
    t = torch.from_numpy(flat.reshape(H, C // 8, W, 8).copy())
    t = t.permute(1, 3, 0, 2)  # [C/8, 8, H, W]
    t = t.reshape(C, H, W)  # [C, H, W]
    return t.unsqueeze(0).to(torch.int8)  # [1, C, H, W]


def weights_to_tiled_int8(weight):
    """Convert [O, I, 1, 1] int8 weight tensor to tiled [O/8, I/8, 8, 8] flat.

    Within each (O_group, I_group) tile, weights are stored as
    [ic8, oc8] -- input channel varies fastest.

    Args:
        weight: PyTorch tensor of shape [O, I, 1, 1] in int8.

    Returns:
        1D numpy array in int8 with layout [O/8, I/8, 8, 8].
    """
    O, I, kh, kw = weight.shape
    assert kh == 1 and kw == 1, "Only 1x1 kernels supported"
    assert O % 8 == 0, f"Out channels ({O}) must be a multiple of 8"
    assert I % 8 == 0, f"In channels ({I}) must be a multiple of 8"

    w = weight.squeeze(-1).squeeze(-1)  # [O, I]
    w = w.reshape(O // 8, 8, I // 8, 8)  # [O/8, 8, I/8, 8]
    w = w.permute(0, 2, 3, 1)  # [O/8, I/8, 8(ic), 8(oc)]
    w = w.contiguous()
    return w.numpy().astype(np.int8).reshape(-1)


class AIEConv2dInt8(AIEOperatorBase):
    """AIE-accelerated 2D Convolution (1x1 kernel, int8).

    Performs int8 x int8 -> int32 MAC with right-shift requantization
    to produce int8 output. Channels must be multiples of 8.

    Args:
        in_channels: Number of input channels (must be multiple of 8).
        out_channels: Number of output channels (must be multiple of 8).
        kernel_size: Convolution kernel size (only 1 supported).
        stride: Convolution stride (only 1 supported).
        height: Spatial height of input.
        width: Spatial width of input.
        scale: Right-shift bits for int32 -> int8 requantization.
        num_aie_columns: Number of AIE columns (only 1 supported).
        context: AIEContext instance.
    """

    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size=1,
        stride=1,
        height=None,
        width=None,
        scale=10,
        num_aie_columns=1,
        context=None,
    ):
        assert kernel_size == 1, f"Only kernel_size=1 supported, got {kernel_size}"
        assert stride == 1, "Only stride=1 supported"
        assert (
            in_channels % 8 == 0
        ), f"in_channels ({in_channels}) must be a multiple of 8"
        assert (
            out_channels % 8 == 0
        ), f"out_channels ({out_channels}) must be a multiple of 8"
        assert (
            height is not None and width is not None
        ), "height and width must be specified"
        assert num_aie_columns == 1, "Only 1 column supported for int8 conv2d"

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.height = height
        self.width = width
        self.scale = scale
        self.num_aie_columns = num_aie_columns

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"conv2d_int8_{self.in_channels}ic_{self.out_channels}oc_"
            f"{self.height}h_{self.width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_conv2d_int8",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.out_channels,
                self.scale,
            ],
        )

        self.xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    "conv2dk1_i8.o",
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir
                            / "aie_kernels"
                            / "aie2p"
                            / "conv2dk1_i8.cc"
                        )
                    ],
                    extra_flags=["-DINT8_ACT", "-DSCALAR"],
                ),
            ],
        )

        self.insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.add_artifacts([self.xclbin_artifact, self.insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width
        total_weights = self.out_channels * self.in_channels
        total_output = self.out_channels * self.height * self.width

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "conv2d_int8",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("conv2d_int8", "input", "weights", "output")

    def forward(self, x, weight):
        """Run int8 conv2d on the NPU.

        Args:
            x: Input tensor of shape [N, C_in, H, W] in int8.
            weight: Weight tensor [C_out, C_in, 1, 1] in int8.

        Returns:
            Output tensor of shape [N, C_out, H, W] in int8.
        """
        if x.dtype != torch.int8:
            raise AIEOperatorConstraintError("AIEConv2dInt8: input must be int8")
        if x.shape[0] != 1:
            raise AIEOperatorConstraintError("AIEConv2dInt8: batch size must be 1")

        input_tiled = nchw_to_tiled_int8(x)
        self.write_buffer("input", input_tiled)

        weight_tiled = weights_to_tiled_int8(weight)
        self.write_buffer("weights", weight_tiled)

        total_output = self.out_channels * self.height * self.width
        self.write_buffer("output", np.zeros(total_output, dtype=np.int8))

        self.run_runlist()

        output_flat = self.read_buffer(
            "output", (total_output,), copy=True, dtype=np.int8
        )
        return tiled_to_nchw_int8(output_flat, self.out_channels, self.height, self.width)
