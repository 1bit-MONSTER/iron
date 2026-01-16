# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from operators.common import (
    SingleMLIRSourceOperator,
    AIERuntimeArgSpec,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from operators.common.utils import torch_to_numpy


class AIEGEMV(SingleMLIRSourceOperator):
    """AIE-accelerated General Matrix-Vector/Vector-Matrix Multiplication layer"""

    def __init__(
        self,
        M,
        K,
        num_aie_columns=1,
        tile_size_input=2,
        tile_size_output=None,
        is_mv=True,
        use_static_weight=False,
        context=None,
    ):
        if tile_size_output is None:
            tile_size_output = tile_size_input

        assert (
            tile_size_output % tile_size_input == 0
            and tile_size_output >= tile_size_input
        ), "tile_size_output must be a multiple of tile_size_input"
        self.M = M  # matrix rows
        self.K = K  # matrix columns, vector rows
        self.num_aie_columns = num_aie_columns
        self.tile_size_input = tile_size_input
        self.tile_size_output = tile_size_output

        self.xclbin_artifact = None
        self.insts_artifact = None

        SingleMLIRSourceOperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"{self.M}x{self.K}_{self.tile_size_input}tsi_{self.tile_size_output}tso_{self.num_aie_columns}col"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent

        return PythonGeneratedMLIRArtifact.new(
            f"{self.get_operator_name()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_matvec",
            callback_args=[
                self.context.device_manager.device_type,
                self.num_aie_columns,
                self.M,
                self.K,
                self.tile_size_input,
                self.tile_size_output,
            ],
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact.new(
                f"mv.o",
                depends=[
                    SourceArtifact.new(
                        self.context.base_dir / "aie_kernels" / "generic" / "mv.cc"
                    )
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec((self.M, self.K)),  # matrix
            AIERuntimeArgSpec((self.K,)),  # vector
            AIERuntimeArgSpec((self.M,)),  # output
        ]
