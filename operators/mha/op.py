# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from operators.common import (
    SingleMLIRSourceOperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEMHA(SingleMLIRSourceOperator):

    def __init__(
        self,
        num_heads: int,
        seq_len: int,
        d: int,
        num_KV_heads: int,
        num_of_pipelines: int = 1,
        context=None,
    ):
        self.num_heads = num_heads
        self.seq_len = seq_len
        self.d = d
        self.B_q = 64
        self.B_kv = 64
        self.num_KV_heads = num_KV_heads
        self.num_of_pipelines = num_of_pipelines
        assert d == 64, "Only d=64 is supported in this version"
        
        SingleMLIRSourceOperator.__init__(self, context=context)

    def get_operator_name(self):
        kv_heads = self.num_KV_heads if self.num_KV_heads > 0 else self.num_heads
        return f"mha_{self.num_heads}h_{kv_heads}kv_{self.seq_len}s_{self.d}d"

    def get_kernel_archive_name(self):
        return "mha_kernels.a"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        return PythonGeneratedMLIRArtifact.new(
            f"{self.get_operator_name()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="fused_mha",
            callback_kwargs={
                "heads": self.num_heads,
                "S_q": self.seq_len,
                "S_kv": self.seq_len,
                "d": self.d,
                "B_q": self.B_q,
                "B_kv": self.B_kv,
                "num_KV_heads": self.num_KV_heads,
                "number_of_pipelines": self.num_of_pipelines,
                "emulate_bf16_mmul_with_bfp16": True,
                "trace_size": 0,
                "verbose": False,
            },
        )

    def get_kernel_artifacts(self):
        # Define source files
        mm_source = self.context.base_dir / "aie_kernels" / "aie2p" / "mm.cc"
        softmax_source = self.context.base_dir / "aie_kernels" / "aie2p" / "softmax.cc"
        mha_source = self.context.base_dir / "aie_kernels" / "aie2p" / "mha.cc"
        passthrough_source = self.context.base_dir / "aie_kernels" / "generic" / "passThrough.cc"

        # Compile mm.cc (col-major)
        mm_defines_rowmaj = [
            "-Dbf16_bf16_ONLY",
            f"-DDIM_M={self.B_q}",
            f"-DDIM_K={self.d}",
            f"-DDIM_N={self.B_kv}",
            "-DROUND_CONV_EVEN",
            "-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16",
        ]
        mm_defines_colmaj = mm_defines_rowmaj + [
            "-DB_COL_MAJ",
        ]
        mm_rename_symbols = {
            "matmul_bf16_bf16": "matmul_bf16_bf16_rowmaj",
            "matmul_scalar_bf16_bf16": "matmul_scalar_bf16_bf16_rowmaj",
            "zero_bf16": "zero_bf16_rowmaj",
            "zero_scalar_bf16": "zero_scalar_bf16_rowmaj",
        }

        return [
            KernelObjectArtifact.new(
                f"mha_mm.o",
                extra_flags=mm_defines_colmaj,
                depends=[SourceArtifact.new(mm_source)],
            ),
            KernelObjectArtifact.new(
                f"mha_mm_rowmaj.o",
                extra_flags=mm_defines_rowmaj,
                depends=[SourceArtifact.new(mm_source)],
                rename_symbols=mm_rename_symbols,
            ),
            KernelObjectArtifact.new(
                "mha_softmax.o",
                depends=[SourceArtifact.new(softmax_source)],
            ),
            KernelObjectArtifact.new(
                "mha_mha.o", depends=[SourceArtifact.new(mha_source)]
            ),
            KernelObjectArtifact.new(
                "mha_passThrough.o",
                extra_flags=["-DBIT_WIDTH=16"],
                depends=[SourceArtifact.new(passthrough_source)],
            ),
        ]

    def _calculate_seq_padding(self, seq_len, num_pipeline=1):
        return ((seq_len + 63 * num_pipeline) // (64 * num_pipeline)) * (
            64 * num_pipeline
        )

    def get_arg_spec(self):
        S_pad = self._calculate_seq_padding(self.seq_len, self.num_of_pipelines)
        buffer_size = self.num_heads * self.d * S_pad
        return [
            AIERuntimeArgSpec("in", (buffer_size,)),  # Q
            AIERuntimeArgSpec("in", (buffer_size,)),  # K
            AIERuntimeArgSpec("in", (buffer_size,)),  # V
            AIERuntimeArgSpec("out", (buffer_size,)), # O
        ]
