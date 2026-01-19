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
        num_batches=1,
        use_static_weight=False,
        kernel_vector_size=64,
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
        self.num_batches = num_batches
        self.kernel_vector_size = kernel_vector_size
        assert K >= kernel_vector_size and K % kernel_vector_size == 0, "K must be multiple of kernel_vector_size"

        self.xclbin_artifact = None
        self.insts_artifact = None

        SingleMLIRSourceOperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"{self.M}x{self.K}_{self.tile_size_input}tsi_{self.tile_size_output}tso_{self.num_batches}batch_{self.num_aie_columns}col"

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
                self.num_batches,
            ],
            callback_kwargs={
                "kernel_archive": self.get_kernel_archive_name(),
            }
        )
    
    def get_kernel_archive_name(self):
        return f"mv_{self.K}k.a"

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact.new(
                f"mv_{self.K}k.o",
                depends=[
                    SourceArtifact.new(
                        self.context.base_dir / "aie_kernels" / "generic" / "mv.cc"
                    )
                ],
                extra_flags=[
                    f"-DDIM_K={self.K}",
                    f"-DVEC_SIZE={self.kernel_vector_size}",
                ]
            ),
        ]

    def get_arg_spec(self):
        batch_dim = (self.num_batches,) if self.num_batches > 1 else ()
        return [
            AIERuntimeArgSpec("in", batch_dim + (self.M, self.K)),  # matrix
            AIERuntimeArgSpec("in", batch_dim + (self.K,)),  # vector
            AIERuntimeArgSpec("out", batch_dim + (self.M,)),  # output
        ]
