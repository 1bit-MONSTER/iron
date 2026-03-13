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
from iron.operators.conv2d.op import nchw_to_tiled, tiled_to_nchw


class AIEUpsample(AIEOperatorBase):
    """AIE-accelerated nearest-neighbor 2x upsampling.

    Input:  [1, C, H, W]  in bfloat16
    Output: [1, C, 2H, 2W] in bfloat16

    Channels must be a multiple of 8. The operator converts between
    NCHW and tiled [H, C/8, W, 8] layout internally.

    Args:
        channels: Number of channels (must be a multiple of 8).
        height: Input spatial height.
        width: Input spatial width.
        scale_factor: Upsampling scale factor (only 2 is supported).
        num_aie_columns: Number of AIE columns for parallelism.
        context: AIEContext instance.
    """

    def __init__(
        self,
        channels,
        height,
        width,
        scale_factor=2,
        num_aie_columns=1,
        context=None,
        register=True,
    ):
        assert scale_factor == 2, "Only scale_factor=2 is supported"
        assert channels % 8 == 0, f"channels ({channels}) must be a multiple of 8"

        self.channels = channels
        self.height = height
        self.width = width
        self.scale_factor = scale_factor
        self.num_aie_columns = num_aie_columns

        self.out_height = height * scale_factor
        self.out_width = width * scale_factor

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=register)

    def get_artifacts(self, prefix="upsample_"):
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
            f"s{self.scale_factor}_{self.num_aie_columns}col"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_upsample",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.channels,
                self.scale_factor,
                self.num_aie_columns,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    "upsample2x_bf16.o",
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir
                            / "aie_kernels"
                            / "aie2p"
                            / "upsample2x_bf16.cc"
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
        total_input = self.channels * self.height * self.width
        total_output = self.channels * self.out_height * self.out_width

        self.add_buffer("input", total_input)
        self.add_buffer("output", total_output)

        self.add_kernel(
            "upsample",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("upsample", "input", "output")

    def forward(self, x):
        """Run nearest-neighbor 2x upsampling on the NPU.

        Args:
            x: Input tensor of shape [1, C, H, W] in bfloat16.

        Returns:
            Output tensor of shape [1, C, 2H, 2W] in bfloat16.
        """
        if x.dtype != torch.bfloat16:
            raise AIEOperatorConstraintError("AIEUpsample: input must be bfloat16")
        if x.shape[0] != 1:
            raise AIEOperatorConstraintError("AIEUpsample: batch size must be 1")
        if x.shape[1] != self.channels:
            raise AIEOperatorConstraintError(
                f"AIEUpsample: expected {self.channels} channels, " f"got {x.shape[1]}"
            )
        if x.shape[2] != self.height or x.shape[3] != self.width:
            raise AIEOperatorConstraintError(
                f"AIEUpsample: expected spatial dims ({self.height}, {self.width}), "
                f"got ({x.shape[2]}, {x.shape[3]})"
            )

        # Convert input to tiled layout and write to buffer
        input_tiled = nchw_to_tiled(x)
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
