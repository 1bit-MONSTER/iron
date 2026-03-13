# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
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
from iron.common.utils import torch_to_numpy, numpy_to_torch


def nchw_to_tiled(tensor):
    """Convert [N, C, H, W] tensor to tiled layout [H, C/8, W, 8] flattened.

    Args:
        tensor: PyTorch tensor of shape [N, C, H, W] (N must be 1).

    Returns:
        1D numpy array in bfloat16 with layout [H, C/8, W, 8].
    """
    assert tensor.shape[0] == 1, "Batch size must be 1"
    N, C, H, W = tensor.shape
    assert C % 8 == 0, f"Channels ({C}) must be a multiple of 8"

    t = tensor[0]  # [C, H, W]
    t = t.reshape(C // 8, 8, H, W)  # [C/8, 8, H, W]
    t = t.permute(2, 0, 3, 1)  # [H, C/8, W, 8]
    t = t.contiguous()
    return torch_to_numpy(t).reshape(-1)


def tiled_to_nchw(flat, C, H, W):
    """Convert flat tiled [H, C/8, W, 8] back to [1, C, H, W].

    Args:
        flat: 1D numpy array in bfloat16 of size H * C * W.
        C: Number of channels.
        H: Spatial height.
        W: Spatial width.

    Returns:
        PyTorch tensor of shape [1, C, H, W] in bfloat16.
    """
    t = numpy_to_torch(flat.reshape(H, C // 8, W, 8))
    t = t.permute(1, 3, 0, 2)  # [C/8, 8, H, W]
    t = t.reshape(C, H, W)  # [C, H, W]
    return t.unsqueeze(0)  # [1, C, H, W]


class AIEMaxPool2d(AIEOperatorBase):
    """AIE-accelerated MaxPool2d for bfloat16.

    Supports configurable kernel_size, stride, and padding.
    Input is pre-padded with -inf in Python before sending to the NPU,
    so the AIE kernel always operates on valid data.

    Data layout: tiled [H, C/8, W, 8] (same as conv2d).

    Args:
        channels: Number of channels (must be a multiple of 8).
        height: Spatial height of input.
        width: Spatial width of input (must be >= kernel_size).
        kernel_size: Pooling window size (default 5).
        stride: Pooling stride (default 1).
        padding: Padding on each side (default 2).
        num_aie_columns: Number of AIE columns for parallelism.
        context: AIEContext instance.
    """

    def __init__(
        self,
        channels,
        height,
        width,
        kernel_size=5,
        stride=1,
        padding=2,
        num_aie_columns=1,
        context=None,
        register=True,
    ):
        assert channels % 8 == 0, f"channels ({channels}) must be a multiple of 8"
        assert (
            width >= kernel_size
        ), f"width ({width}) must be >= kernel_size ({kernel_size})"
        assert stride == 1, "Only stride=1 is supported currently"

        self.channels = channels
        self.height = height
        self.width = width
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.num_aie_columns = num_aie_columns

        # Padded input dimensions
        self.padded_height = height + 2 * padding
        self.padded_width = width + 2 * padding

        # Output dimensions (stride=1, so output = input size)
        self.out_height = (height + 2 * padding - kernel_size) // stride + 1
        self.out_width = (width + 2 * padding - kernel_size) // stride + 1

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=register)

    def get_artifacts(self, prefix="maxpool2d_"):
        """Create compilation artifacts without registering them.

        Args:
            prefix: Prefix for artifact file names (allows multiple
                independent compilations of the same operator config).

        Returns:
            Tuple of (xclbin_artifact, insts_artifact).
        """
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"{prefix}{self.channels}c_{self.height}h_{self.width}w_"
            f"k{self.kernel_size}_s{self.stride}_p{self.padding}_"
            f"{self.num_aie_columns}col"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_maxpool2d",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.channels,
                self.kernel_size,
                self.stride,
                self.padding,
                self.num_aie_columns,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    "maxpool2d_bf16.o",
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir
                            / "aie_kernels"
                            / "aie2p"
                            / "maxpool2d_bf16.cc"
                        )
                    ],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        return (xclbin_artifact, insts_artifact)

    def set_up_artifacts(self):
        xclbin_artifact, insts_artifact = self.get_artifacts()
        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        # Input is pre-padded: padded_height * padded_width * channels
        total_input = self.channels * self.padded_height * self.padded_width
        # Output: out_height * out_width * channels
        total_output = self.channels * self.out_height * self.out_width

        self.add_buffer("input", total_input)
        self.add_buffer("output", total_output)

        self.add_kernel(
            "maxpool2d",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("maxpool2d", "input", "output")

    def _pad_input(self, x):
        """Pad input tensor with -inf for max pooling, then convert to tiled layout.

        Args:
            x: Input tensor [1, C, H, W] in bfloat16.

        Returns:
            1D numpy array in bfloat16 with padded tiled layout
            [H_padded, C/8, W_padded, 8].
        """
        # Pad with -inf (use large negative for bf16: -3.3895e+38)
        # F.pad order: (left, right, top, bottom)
        x_padded = torch.nn.functional.pad(
            x.float(),
            (self.padding, self.padding, self.padding, self.padding),
            mode="constant",
            value=float("-inf"),
        ).to(torch.bfloat16)
        return nchw_to_tiled(x_padded)

    def forward(self, x):
        """Run MaxPool2d on the NPU.

        Args:
            x: Input tensor of shape [1, C, H, W] in bfloat16.

        Returns:
            Output tensor of shape [1, C, H_out, W_out] in bfloat16.
        """
        if x.dtype != torch.bfloat16:
            raise AIEOperatorConstraintError("AIEMaxPool2d: input must be bfloat16")
        if x.shape[0] != 1:
            raise AIEOperatorConstraintError("AIEMaxPool2d: batch size must be 1")
        if x.shape[1] != self.channels:
            raise AIEOperatorConstraintError(
                f"AIEMaxPool2d: expected {self.channels} channels, " f"got {x.shape[1]}"
            )
        if x.shape[2] != self.height or x.shape[3] != self.width:
            raise AIEOperatorConstraintError(
                f"AIEMaxPool2d: expected spatial dims ({self.height}, {self.width}), "
                f"got ({x.shape[2]}, {x.shape[3]})"
            )

        # Pad input with -inf and convert to tiled layout
        input_tiled = self._pad_input(x)
        self.write_buffer("input", input_tiled)

        # Zero the output buffer
        total_output = self.channels * self.out_height * self.out_width
        self.write_buffer("output", np.zeros(total_output, dtype=bfloat16))

        # Run on NPU
        self.run_runlist()

        # Read output and convert back to NCHW
        output_flat = self.read_buffer(
            "output", (total_output,), copy=True, dtype=bfloat16
        )
        result = tiled_to_nchw(
            output_flat, self.channels, self.out_height, self.out_width
        )

        return result
