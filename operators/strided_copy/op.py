# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from operators.common import (
    SingleMLIRSourceOperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEStridedCopy(SingleMLIRSourceOperator):
    """AIE-accelerated General Matrix-Vector/Vector-Matrix Multiplication layer"""

    def __init__(
        self,
        input_sizes,
        input_strides,
        input_offset,
        output_sizes,
        output_strides,
        output_offset,
        input_buffer_size,
        output_buffer_size,
        dtype=bfloat16,
        transfer_size=None,
        num_aie_channels=1,
        context=None,
        **kwargs,
    ):
        assert len(input_sizes) == len(input_strides)
        assert len(output_sizes) == len(output_strides)
        self.input_sizes = input_sizes
        self.input_strides = input_strides
        self.input_offset = input_offset
        self.output_sizes = output_sizes
        self.output_strides = output_strides
        self.output_offset = output_offset
        self.input_buffer_size = input_buffer_size
        self.output_buffer_size = output_buffer_size
        self.dtype = dtype
        self.transfer_size = transfer_size
        self.num_aie_channels = num_aie_channels
        self.kwargs = kwargs
        SingleMLIRSourceOperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"strided_copy_{'x'.join(map(str, self.input_sizes))}sz_{'x'.join(map(str, self.input_strides))}st_{self.input_offset}off_to_{'x'.join(map(str, self.output_sizes))}sz_{'x'.join(map(str, self.output_strides))}st_{self.output_offset}off_{self.transfer_size if self.transfer_size is not None else 'auto'}tr_{self.num_aie_channels}ch"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent

        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="strided_copy",
            callback_args=[
                self.context.device_manager.device_type,
                self.dtype,
                self.input_buffer_size,
                self.input_sizes,
                self.input_strides,
                self.input_offset,
                self.output_buffer_size,
                self.output_sizes,
                self.output_strides,
                self.output_offset,
                self.transfer_size,
                self.num_aie_channels,
            ],
            callback_kwargs=self.kwargs,
        )

    def get_kernel_artifacts(self):
        return []

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", self.input_buffer_size),  # matrix
            AIERuntimeArgSpec("out", self.output_buffer_size),  # output
        ]
