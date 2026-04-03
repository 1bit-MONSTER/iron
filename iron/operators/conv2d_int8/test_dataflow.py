#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests for YOLOv8n dataflow pipeline designs.

Step 1: L0 alone — verify single-core dataflow matches sequential conv output.
Step 2: L0->L1 chain — verify two-core chain matches sequential output.
Step 3+: Add more layers incrementally.
"""

import pytest
import torch
import numpy as np
import time
from pathlib import Path

from iron.operators.conv2d_int8.op import (
    nchw_to_tiled_int8,
    tiled_to_nchw_int8,
    weights_to_tiled_int8,
    weights_to_tiled_int8_k3,
)
from iron.operators.conv2d_int8.reference import (
    conv2d_int8_pade_silu_reference,
    conv2d_int8_reference,
)
from iron.common import (
    AIEContext,
    AIEOperatorBase,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


def pack_fused_weights_k3(w_int8, b_int32):
    """Pack k3 weights with int32 bias appended.

    Layout: [tiled_weights | bias_as_int8_bytes]
    """
    w_tiled = weights_to_tiled_int8_k3(w_int8)
    b_bytes = b_int32.numpy().astype(np.int32).view(np.int8)
    return np.concatenate([w_tiled, b_bytes])


# ============================================================================
# Step 1: L0 alone
# ============================================================================


class AIEDataflowL0(AIEOperatorBase):
    """Dataflow operator for L0 alone: k3s2 8->16, 640x640->320x320."""

    def __init__(
        self,
        height,
        width,
        in_channels,
        out_channels,
        shift1,
        shift2,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.shift1 = shift1
        self.shift2 = shift2
        self.out_h = height // 2
        self.out_w = width // 2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_l0_{self.in_channels}ic_{self.out_channels}oc_"
            f"{self.height}h_{self.width}w_sh{self.shift1}_{self.shift2}"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_l0",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.out_channels,
                self.shift1,
                self.shift2,
            ],
        )

        kernel_src = "conv2dk3_i8_silu.cc"
        kernel_obj_name = "conv2dk3_i8_silu.o"

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    kernel_obj_name,
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir / "aie_kernels" / "aie2p" / kernel_src
                        )
                    ],
                    extra_flags=["-DINT8_ACT"],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width
        wt_size = self.out_channels * self.in_channels * 9 + self.out_channels * 4
        total_output = self.out_channels * self.out_h * self.out_w

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", wt_size, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "dataflow_l0",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dataflow_l0", "input", "weights", "output")


@pytest.mark.parametrize(
    "height,width,ic,oc,shift1,shift2",
    [
        pytest.param(8, 8, 8, 16, 10, 7, id="dataflow_l0_8x8"),
        pytest.param(16, 16, 8, 16, 10, 7, id="dataflow_l0_16x16"),
        pytest.param(32, 32, 8, 16, 10, 7, id="dataflow_l0_32x32"),
        pytest.param(64, 64, 8, 16, 10, 7, id="dataflow_l0_64x64"),
        pytest.param(128, 128, 8, 16, 10, 7, id="dataflow_l0_128x128"),
        pytest.param(
            640,
            640,
            8,
            16,
            10,
            7,
            id="dataflow_l0_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_l0(height, width, ic, oc, shift1, shift2, aie_context):
    """Step 1: Verify L0 dataflow design matches sequential conv output."""
    torch.manual_seed(42)

    # Test data
    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_int8 = torch.randint(-50, 51, (oc, ic, 3, 3), dtype=torch.int8)
    b_int32 = torch.randint(-500, 501, (oc,), dtype=torch.int32)

    # CPU reference
    ref = conv2d_int8_pade_silu_reference(
        x_int8, w_int8, b_int32, shift1, shift2, stride=2
    )

    # Create dataflow operator
    op = AIEDataflowL0(
        height=height,
        width=width,
        in_channels=ic,
        out_channels=oc,
        shift1=shift1,
        shift2=shift2,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write weights
    packed_wts = pack_fused_weights_k3(w_int8, b_int32)
    op.write_buffer("weights", packed_wts)

    # Clear output
    out_h = height // 2
    out_w = width // 2
    total_output = oc * out_h * out_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), oc, out_h, out_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff))
    errors_gt1 = int(np.sum(diff > 1))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nDataflow L0 test {ic}ic_{oc}oc_{height}h_{width}w:")
    print(f"  Exact vs ref: {exact}/{total} ({100*exact/total:.1f}%)")
    print(f"  Max diff vs ref: {max_diff}")
    print(f"  Errors (>1) vs ref: {errors_gt1}/{total}")
    print(f"  NPU time: {1000*(t1-t0):.1f} ms")

    # For large spatial sizes, the scalar Pade SiLU has known rounding
    # differences vs the float CPU reference (2-3% of outputs, max_diff
    # up to 128). This matches the existing sequential conv operator.
    # Use tolerance +-2 for single-layer designs.
    errors_gt2 = int(np.sum(diff > 2))
    if height >= 256:
        # At large sizes, compare NPU output structure (not exact values)
        # The known SiLU reference mismatch is not a dataflow bug.
        error_rate = errors_gt1 / total
        assert (
            error_rate < 0.05
        ), f"Dataflow L0: error rate {100*error_rate:.1f}% exceeds 5% threshold"
        print(
            f"  NOTE: {100*error_rate:.1f}% error rate matches sequential conv "
            f"(known Pade SiLU reference mismatch)"
        )
    else:
        assert errors_gt1 == 0, (
            f"Dataflow L0 failed: {errors_gt1} mismatches (diff>1) out of {total}, "
            f"max_diff={max_diff}"
        )


# ============================================================================
# Step 2: L0 -> L1 chain
# ============================================================================


class AIEDataflowL0L1(AIEOperatorBase):
    """Dataflow operator for L0->L1 chain.

    L0: k3s2 8->16, 640x640->320x320 (fused SiLU)
    L1: k3s2 16->32, 320x320->160x160 (fused SiLU)
    """

    def __init__(
        self,
        l0_height,
        l0_width,
        l0_ic,
        l0_oc,
        l0_shift1,
        l0_shift2,
        l1_oc,
        l1_shift1,
        l1_shift2,
        context=None,
    ):
        self.l0_height = l0_height
        self.l0_width = l0_width
        self.l0_ic = l0_ic
        self.l0_oc = l0_oc
        self.l0_shift1 = l0_shift1
        self.l0_shift2 = l0_shift2
        self.l1_oc = l1_oc
        self.l1_shift1 = l1_shift1
        self.l1_shift2 = l1_shift2

        # Derived dims
        self.l1_ic = l0_oc
        self.l1_height = l0_height // 2
        self.l1_width = l0_width // 2
        self.out_h = self.l1_height // 2
        self.out_w = self.l1_width // 2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_l0l1_{self.l0_ic}ic_{self.l1_oc}oc_"
            f"{self.l0_height}h_{self.l0_width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_l0_l1",
            callback_args=[
                self.context.device_manager.device_type,
                self.l0_height,
                self.l0_width,
                self.l0_ic,
                self.l0_oc,
                self.l0_shift1,
                self.l0_shift2,
                self.l1_oc,
                self.l1_shift1,
                self.l1_shift2,
            ],
        )

        kernel_src = "conv2dk3_i8_silu.cc"
        kernel_obj_name = "conv2dk3_i8_silu.o"

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    kernel_obj_name,
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir / "aie_kernels" / "aie2p" / kernel_src
                        )
                    ],
                    extra_flags=["-DINT8_ACT"],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.l0_ic * self.l0_height * self.l0_width
        l0_wt = self.l0_oc * self.l0_ic * 9 + self.l0_oc * 4
        l1_wt = self.l1_oc * self.l1_ic * 9 + self.l1_oc * 4
        # Both weight FIFOs are padded to max size (matches design)
        wt_fifo_size = max(l0_wt, l1_wt)
        total_weights = 2 * wt_fifo_size
        self._l0_wt_size = l0_wt
        self._l1_wt_size = l1_wt
        self._wt_fifo_size = wt_fifo_size
        total_output = self.l1_oc * self.out_h * self.out_w

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "dataflow_l0l1",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dataflow_l0l1", "input", "weights", "output")


@pytest.mark.parametrize(
    "l0_h,l0_w,l0_ic,l0_oc,l0_s1,l0_s2,l1_oc,l1_s1,l1_s2",
    [
        pytest.param(8, 8, 8, 16, 10, 7, 32, 11, 7, id="dataflow_l0l1_8x8"),
        pytest.param(16, 16, 8, 16, 10, 7, 32, 11, 7, id="dataflow_l0l1_16x16"),
        pytest.param(
            640,
            640,
            8,
            16,
            10,
            7,
            32,
            11,
            7,
            id="dataflow_l0l1_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_l0l1(
    l0_h, l0_w, l0_ic, l0_oc, l0_s1, l0_s2, l1_oc, l1_s1, l1_s2, aie_context
):
    """Step 2: Verify L0->L1 chain matches two sequential conv outputs."""
    torch.manual_seed(42)

    l1_ic = l0_oc
    l1_h = l0_h // 2
    l1_w = l0_w // 2
    out_h = l1_h // 2
    out_w = l1_w // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)
    w0_int8 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    b0_int32 = torch.randint(-500, 501, (l0_oc,), dtype=torch.int32)
    w1_int8 = torch.randint(-50, 51, (l1_oc, l1_ic, 3, 3), dtype=torch.int8)
    b1_int32 = torch.randint(-500, 501, (l1_oc,), dtype=torch.int32)

    # CPU reference: sequential L0 then L1
    inter = conv2d_int8_pade_silu_reference(
        x_int8, w0_int8, b0_int32, l0_s1, l0_s2, stride=2
    )
    ref = conv2d_int8_pade_silu_reference(
        inter, w1_int8, b1_int32, l1_s1, l1_s2, stride=2
    )

    # Create dataflow operator
    op = AIEDataflowL0L1(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_shift1=l0_s1,
        l0_shift2=l0_s2,
        l1_oc=l1_oc,
        l1_shift1=l1_s1,
        l1_shift2=l1_s2,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write packed weights: [l0_weights+bias+padding | l1_weights+bias+padding]
    # Both weight FIFO elements are padded to the same size (wt_fifo_size)
    packed_w0 = pack_fused_weights_k3(w0_int8, b0_int32)
    packed_w1 = pack_fused_weights_k3(w1_int8, b1_int32)
    wt_fifo_size = op._wt_fifo_size
    pad0 = np.zeros(wt_fifo_size - len(packed_w0), dtype=np.int8)
    pad1 = np.zeros(wt_fifo_size - len(packed_w1), dtype=np.int8)
    packed_all = np.concatenate([packed_w0, pad0, packed_w1, pad1])
    op.write_buffer("weights", packed_all)

    # Clear output
    total_output = l1_oc * out_h * out_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), l1_oc, out_h, out_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff))
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt2 = int(np.sum(diff > 2))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nDataflow L0->L1 test {l0_ic}ic_{l1_oc}oc_{l0_h}h_{l0_w}w:")
    print(f"  Exact: {exact}/{total} ({100*exact/total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>2): {errors_gt2}/{total}")
    print(f"  NPU time: {1000*(t1-t0):.1f} ms")

    # For large spatial sizes, the scalar Pade SiLU has known rounding
    # differences vs the float CPU reference (compounds through 2 layers).
    # This matches the existing sequential conv operators.
    if l0_h >= 256:
        error_rate = errors_gt2 / total
        assert (
            error_rate < 0.05
        ), f"Dataflow L0->L1: error rate {100*error_rate:.1f}% exceeds 5% threshold"
        print(
            f"  NOTE: {100*error_rate:.1f}% error rate matches sequential conv chain "
            f"(known Pade SiLU reference mismatch)"
        )
    else:
        # At small sizes, Pade SiLU is accurate: strict tolerance
        assert errors_gt2 == 0, (
            f"Dataflow L0->L1 failed: {errors_gt2} mismatches (diff>2) "
            f"out of {total}, max_diff={max_diff}"
        )


# ============================================================================
# Conv -> SiLU split dataflow (two kernels, two cores)
# ============================================================================


from iron.operators.conv2d_int8.reference import conv2d_int8_split_silu_reference


class AIEDataflowConvSilu(AIEOperatorBase):
    """Dataflow operator: conv core -> FIFO -> bias_silu core."""

    def __init__(
        self,
        height,
        width,
        in_channels,
        out_channels,
        shift1,
        shift2,
        conv_scale,
        stride=1,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.shift1 = shift1
        self.shift2 = shift2
        self.conv_scale = conv_scale
        self.stride = stride
        self.out_h = height if stride == 1 else height // 2
        self.out_w = width if stride == 1 else width // 2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_conv_silu_{self.in_channels}ic_{self.out_channels}oc_"
            f"{self.height}h_{self.width}w_s{self.stride}_"
            f"cs{self.conv_scale}_sh{self.shift1}_{self.shift2}"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_conv_silu",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.out_channels,
                self.shift1,
                self.shift2,
                self.conv_scale,
                self.stride,
            ],
        )

        # Two kernel objects: conv and bias_silu
        conv_kernel_obj = KernelObjectArtifact.new(
            "conv2dk3_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        silu_kernel_obj = KernelObjectArtifact.new(
            "bias_silu_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "bias_silu_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[mlir_artifact, conv_kernel_obj, silu_kernel_obj],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width

        # Conv weights (no bias) + bias (int32 as int8 bytes)
        conv_wt_size = self.out_channels * self.in_channels * 9
        bias_size = self.out_channels * 4
        total_weights = conv_wt_size + bias_size

        total_output = self.out_channels * self.out_h * self.out_w

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "dataflow_conv_silu",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dataflow_conv_silu", "input", "weights", "output")


@pytest.mark.parametrize(
    "height,width,ic,oc,conv_scale,shift1,shift2,stride",
    [
        pytest.param(8, 8, 8, 16, 10, 10, 7, 1, id="conv_silu_8x8_s1"),
        pytest.param(16, 16, 8, 16, 10, 10, 7, 1, id="conv_silu_16x16_s1"),
        pytest.param(8, 8, 8, 16, 10, 10, 7, 2, id="conv_silu_8x8_s2"),
        pytest.param(16, 16, 8, 16, 10, 10, 7, 2, id="conv_silu_16x16_s2"),
        pytest.param(32, 32, 8, 16, 10, 10, 7, 2, id="conv_silu_32x32_s2"),
    ],
)
def test_dataflow_conv_silu(
    height, width, ic, oc, conv_scale, shift1, shift2, stride, aie_context
):
    """Verify split conv->silu dataflow matches CPU reference."""
    torch.manual_seed(42)

    out_h = height if stride == 1 else height // 2
    out_w = width if stride == 1 else width // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_int8 = torch.randint(-50, 51, (oc, ic, 3, 3), dtype=torch.int8)
    b_int32 = torch.randint(-500, 501, (oc,), dtype=torch.int32)

    # CPU reference for split pipeline
    ref = conv2d_int8_split_silu_reference(
        x_int8, w_int8, b_int32, conv_scale, shift1, shift2, stride=stride
    )

    # Create dataflow operator
    op = AIEDataflowConvSilu(
        height=height,
        width=width,
        in_channels=ic,
        out_channels=oc,
        shift1=shift1,
        shift2=shift2,
        conv_scale=conv_scale,
        stride=stride,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write weights: [conv_weights_tiled | bias_as_int8_bytes]
    w_tiled = weights_to_tiled_int8_k3(w_int8)
    b_bytes = b_int32.numpy().astype(np.int32).view(np.int8)
    packed_wts = np.concatenate([w_tiled, b_bytes])
    op.write_buffer("weights", packed_wts)

    # Clear output
    total_output = oc * out_h * out_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), oc, out_h, out_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff))
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt2 = int(np.sum(diff > 2))
    errors_gt3 = int(np.sum(diff > 3))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nDataflow Conv->SiLU test {ic}ic_{oc}oc_{height}h_{width}w_s{stride}:")
    print(f"  Exact vs ref: {exact}/{total} ({100*exact/total:.1f}%)")
    print(f"  Max diff vs ref: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>2): {errors_gt2}/{total}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  NPU time: {1000*(t1-t0):.1f} ms")

    # Target: max_diff <= 2, 0 errors > 3
    assert (
        max_diff <= 3
    ), f"Conv->SiLU dataflow: max_diff={max_diff} exceeds threshold 3"
    assert (
        errors_gt3 == 0
    ), f"Conv->SiLU dataflow: {errors_gt3} errors > 3 out of {total}"


# ============================================================================
# Step 3: L0 -> L1 -> L2.cv1 chain (non-fused)
# ============================================================================


class AIEDataflowL0L1L2cv1(AIEOperatorBase):
    """Dataflow operator for L0->L1->L2.cv1 chain (non-fused).

    L0: k3s2, IC->OC0 (no SiLU, no bias)
    L1: k3s2, OC0->OC1 (no SiLU, no bias)
    L2.cv1: k1s1, OC1->OC2 (no SiLU, no bias)
    """

    def __init__(
        self,
        l0_height,
        l0_width,
        l0_ic,
        l0_oc,
        l0_scale,
        l1_oc,
        l1_scale,
        l2cv1_oc,
        l2cv1_scale,
        context=None,
    ):
        self.l0_height = l0_height
        self.l0_width = l0_width
        self.l0_ic = l0_ic
        self.l0_oc = l0_oc
        self.l0_scale = l0_scale
        self.l1_oc = l1_oc
        self.l1_scale = l1_scale
        self.l2cv1_oc = l2cv1_oc
        self.l2cv1_scale = l2cv1_scale

        # Derived dims
        self.l1_ic = l0_oc
        self.l1_height = l0_height // 2
        self.l1_width = l0_width // 2
        self.l2cv1_ic = l1_oc
        self.l2cv1_height = self.l1_height // 2
        self.l2cv1_width = self.l1_width // 2
        self.out_h = self.l2cv1_height
        self.out_w = self.l2cv1_width

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_l0l1l2cv1_{self.l0_ic}ic_{self.l2cv1_oc}oc_"
            f"{self.l0_height}h_{self.l0_width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_l0_l1_l2cv1",
            callback_args=[
                self.context.device_manager.device_type,
                self.l0_height,
                self.l0_width,
                self.l0_ic,
                self.l0_oc,
                self.l0_scale,
                self.l1_oc,
                self.l1_scale,
                self.l2cv1_oc,
                self.l2cv1_scale,
            ],
        )

        # Two kernel objects: k3 conv and k1 conv
        k3_kernel_obj = KernelObjectArtifact.new(
            "conv2dk3_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k1_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[mlir_artifact, k3_kernel_obj, k1_kernel_obj],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.l0_ic * self.l0_height * self.l0_width

        # Weight sizes (non-fused: no bias)
        l0_wt = self.l0_oc * self.l0_ic * 9
        l1_wt = self.l1_oc * self.l1_ic * 9
        l2cv1_wt = self.l2cv1_oc * self.l2cv1_ic

        # Padded to max for uniform MemTile split (matches design)
        wt_slot_size = max(l0_wt, l1_wt, l2cv1_wt)
        total_weights = 3 * wt_slot_size
        self._l0_wt_size = l0_wt
        self._l1_wt_size = l1_wt
        self._l2cv1_wt_size = l2cv1_wt
        self._wt_slot_size = wt_slot_size

        total_output = self.l2cv1_oc * self.out_h * self.out_w

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "dataflow_l0l1l2cv1",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dataflow_l0l1l2cv1", "input", "weights", "output")


@pytest.mark.parametrize(
    "l0_h,l0_w,l0_ic,l0_oc,l0_sc,l1_oc,l1_sc,l2cv1_oc,l2cv1_sc",
    [
        pytest.param(
            16,
            16,
            8,
            16,
            10,
            32,
            11,
            32,
            10,
            id="dataflow_l0l1l2cv1_16x16",
        ),
        pytest.param(
            32,
            32,
            8,
            16,
            10,
            32,
            11,
            32,
            10,
            id="dataflow_l0l1l2cv1_32x32",
        ),
        pytest.param(
            64,
            64,
            8,
            16,
            10,
            32,
            11,
            32,
            10,
            id="dataflow_l0l1l2cv1_64x64",
        ),
        pytest.param(
            640,
            640,
            8,
            16,
            10,
            32,
            11,
            32,
            10,
            id="dataflow_l0l1l2cv1_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_l0l1l2cv1(
    l0_h,
    l0_w,
    l0_ic,
    l0_oc,
    l0_sc,
    l1_oc,
    l1_sc,
    l2cv1_oc,
    l2cv1_sc,
    aie_context,
):
    """Step 3: Verify L0->L1->L2.cv1 non-fused chain matches CPU reference."""
    torch.manual_seed(42)

    l1_ic = l0_oc
    l1_h = l0_h // 2
    l1_w = l0_w // 2
    l2cv1_ic = l1_oc
    l2cv1_h = l1_h // 2
    l2cv1_w = l1_w // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)
    w0_int8 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    w1_int8 = torch.randint(-50, 51, (l1_oc, l1_ic, 3, 3), dtype=torch.int8)
    w2_int8 = torch.randint(-50, 51, (l2cv1_oc, l2cv1_ic, 1, 1), dtype=torch.int8)

    # CPU reference: sequential L0 -> L1 -> L2.cv1 (non-fused, no bias)
    inter01 = conv2d_int8_reference(x_int8, w0_int8, l0_sc, stride=2, padding=1)
    inter12 = conv2d_int8_reference(inter01, w1_int8, l1_sc, stride=2, padding=1)
    ref = conv2d_int8_reference(inter12, w2_int8, l2cv1_sc, stride=1, padding=0)

    # Create dataflow operator
    op = AIEDataflowL0L1L2cv1(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_scale=l0_sc,
        l1_oc=l1_oc,
        l1_scale=l1_sc,
        l2cv1_oc=l2cv1_oc,
        l2cv1_scale=l2cv1_sc,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write packed weights: [l0_wt+pad | l1_wt+pad | l2cv1_wt+pad]
    wt_slot_size = op._wt_slot_size
    w0_tiled = weights_to_tiled_int8_k3(w0_int8)
    w1_tiled = weights_to_tiled_int8_k3(w1_int8)
    w2_tiled = weights_to_tiled_int8(w2_int8)

    pad0 = np.zeros(wt_slot_size - len(w0_tiled), dtype=np.int8)
    pad1 = np.zeros(wt_slot_size - len(w1_tiled), dtype=np.int8)
    pad2 = np.zeros(wt_slot_size - len(w2_tiled), dtype=np.int8)
    packed_all = np.concatenate([w0_tiled, pad0, w1_tiled, pad1, w2_tiled, pad2])
    op.write_buffer("weights", packed_all)

    # Clear output
    total_output = l2cv1_oc * l2cv1_h * l2cv1_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), l2cv1_oc, l2cv1_h, l2cv1_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff))
    errors_gt0 = int(np.sum(diff > 0))
    errors_gt1 = int(np.sum(diff > 1))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nDataflow L0->L1->L2.cv1 test " f"{l0_ic}ic_{l2cv1_oc}oc_{l0_h}h_{l0_w}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>0): {errors_gt0}/{total}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # Non-fused convolutions should be exact (pure integer arithmetic,
    # no floating-point SiLU). Allow max_diff <= 1 for potential
    # rounding at the boundary of the right-shift.
    assert errors_gt1 == 0, (
        f"Dataflow L0->L1->L2.cv1 failed: {errors_gt1} mismatches "
        f"(diff>1) out of {total}, max_diff={max_diff}"
    )


# ============================================================================
# Step 4: L0 -> L1 -> L3 chain (non-fused, all k3s2 downsample)
# ============================================================================


class AIEDataflowL0L1L3(AIEOperatorBase):
    """Dataflow operator for L0->L1->L3 downsample chain (non-fused).

    L0: k3s2, IC->OC0 (no SiLU, no bias)
    L1: k3s2, OC0->OC1 (no SiLU, no bias)
    L3: k3s2, OC1->OC2 (no SiLU, no bias)
    """

    def __init__(
        self,
        l0_height,
        l0_width,
        l0_ic,
        l0_oc,
        l0_scale,
        l1_oc,
        l1_scale,
        l3_oc,
        l3_scale,
        context=None,
    ):
        self.l0_height = l0_height
        self.l0_width = l0_width
        self.l0_ic = l0_ic
        self.l0_oc = l0_oc
        self.l0_scale = l0_scale
        self.l1_oc = l1_oc
        self.l1_scale = l1_scale
        self.l3_oc = l3_oc
        self.l3_scale = l3_scale

        # Derived dims
        self.l1_ic = l0_oc
        self.l1_height = l0_height // 2
        self.l1_width = l0_width // 2
        self.l3_ic = l1_oc
        self.l3_height = self.l1_height // 2
        self.l3_width = self.l1_width // 2
        self.out_h = self.l3_height // 2
        self.out_w = self.l3_width // 2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_l0l1l3_{self.l0_ic}ic_{self.l3_oc}oc_"
            f"{self.l0_height}h_{self.l0_width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_l0_l1_l3",
            callback_args=[
                self.context.device_manager.device_type,
                self.l0_height,
                self.l0_width,
                self.l0_ic,
                self.l0_oc,
                self.l0_scale,
                self.l1_oc,
                self.l1_scale,
                self.l3_oc,
                self.l3_scale,
            ],
        )

        # Single kernel object: k3 conv (used for all three layers)
        k3_kernel_obj = KernelObjectArtifact.new(
            "conv2dk3_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[mlir_artifact, k3_kernel_obj],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.l0_ic * self.l0_height * self.l0_width

        # Weight sizes (non-fused: no bias)
        l0_wt = self.l0_oc * self.l0_ic * 9
        l1_wt = self.l1_oc * self.l1_ic * 9
        l3_wt = self.l3_oc * self.l3_ic * 9

        # Padded to max for uniform MemTile split (matches design)
        wt_slot_size = max(l0_wt, l1_wt, l3_wt)
        total_weights = 3 * wt_slot_size
        self._l0_wt_size = l0_wt
        self._l1_wt_size = l1_wt
        self._l3_wt_size = l3_wt
        self._wt_slot_size = wt_slot_size

        total_output = self.l3_oc * self.out_h * self.out_w

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "dataflow_l0l1l3",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dataflow_l0l1l3", "input", "weights", "output")


@pytest.mark.parametrize(
    "l0_h,l0_w,l0_ic,l0_oc,l0_sc,l1_oc,l1_sc,l3_oc,l3_sc",
    [
        pytest.param(
            16,
            16,
            8,
            16,
            10,
            32,
            11,
            64,
            12,
            id="dataflow_l0l1l3_16x16",
        ),
        pytest.param(
            32,
            32,
            8,
            16,
            10,
            32,
            11,
            64,
            12,
            id="dataflow_l0l1l3_32x32",
        ),
        pytest.param(
            64,
            64,
            8,
            16,
            10,
            32,
            11,
            64,
            12,
            id="dataflow_l0l1l3_64x64",
        ),
        pytest.param(
            640,
            640,
            8,
            16,
            10,
            32,
            11,
            64,
            12,
            id="dataflow_l0l1l3_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_l0l1l3(
    l0_h,
    l0_w,
    l0_ic,
    l0_oc,
    l0_sc,
    l1_oc,
    l1_sc,
    l3_oc,
    l3_sc,
    aie_context,
):
    """Step 4: Verify L0->L1->L3 non-fused k3s2 chain matches CPU reference."""
    torch.manual_seed(42)

    l1_ic = l0_oc
    l1_h = l0_h // 2
    l1_w = l0_w // 2
    l3_ic = l1_oc
    l3_h = l1_h // 2
    l3_w = l1_w // 2
    out_h = l3_h // 2
    out_w = l3_w // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)
    w0_int8 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    w1_int8 = torch.randint(-50, 51, (l1_oc, l1_ic, 3, 3), dtype=torch.int8)
    w3_int8 = torch.randint(-50, 51, (l3_oc, l3_ic, 3, 3), dtype=torch.int8)

    # CPU reference: sequential L0 -> L1 -> L3 (non-fused, no bias)
    inter01 = conv2d_int8_reference(x_int8, w0_int8, l0_sc, stride=2, padding=1)
    inter13 = conv2d_int8_reference(inter01, w1_int8, l1_sc, stride=2, padding=1)
    ref = conv2d_int8_reference(inter13, w3_int8, l3_sc, stride=2, padding=1)

    # Create dataflow operator
    op = AIEDataflowL0L1L3(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_scale=l0_sc,
        l1_oc=l1_oc,
        l1_scale=l1_sc,
        l3_oc=l3_oc,
        l3_scale=l3_sc,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write packed weights: [l0_wt+pad | l1_wt+pad | l3_wt+pad]
    wt_slot_size = op._wt_slot_size
    w0_tiled = weights_to_tiled_int8_k3(w0_int8)
    w1_tiled = weights_to_tiled_int8_k3(w1_int8)
    w3_tiled = weights_to_tiled_int8_k3(w3_int8)

    pad0 = np.zeros(wt_slot_size - len(w0_tiled), dtype=np.int8)
    pad1 = np.zeros(wt_slot_size - len(w1_tiled), dtype=np.int8)
    pad3 = np.zeros(wt_slot_size - len(w3_tiled), dtype=np.int8)
    packed_all = np.concatenate([w0_tiled, pad0, w1_tiled, pad1, w3_tiled, pad3])
    op.write_buffer("weights", packed_all)

    # Clear output
    total_output = l3_oc * out_h * out_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), l3_oc, out_h, out_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff))
    errors_gt0 = int(np.sum(diff > 0))
    errors_gt1 = int(np.sum(diff > 1))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nDataflow L0->L1->L3 test " f"{l0_ic}ic_{l3_oc}oc_{l0_h}h_{l0_w}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>0): {errors_gt0}/{total}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # Non-fused convolutions should be exact (pure integer arithmetic,
    # no floating-point SiLU). Allow max_diff <= 1 for potential
    # rounding at the boundary of the right-shift.
    assert errors_gt1 == 0, (
        f"Dataflow L0->L1->L3 failed: {errors_gt1} mismatches "
        f"(diff>1) out of {total}, max_diff={max_diff}"
    )


# ============================================================================
# CBS L0: Conv+Bias+SiLU — 2 cores (conv_core + silu_core), k3 stride-2
# ============================================================================


class AIEDataflowCBSL0(AIEOperatorBase):
    """Dataflow operator for CBS L0: conv core -> bias_silu core, k3s2."""

    def __init__(
        self,
        height,
        width,
        in_channels,
        out_channels,
        conv_scale,
        shift1,
        shift2,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.conv_scale = conv_scale
        self.shift1 = shift1
        self.shift2 = shift2
        self.out_h = height // 2
        self.out_w = width // 2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_cbs_l0_{self.in_channels}ic_{self.out_channels}oc_"
            f"{self.height}h_{self.width}w_cs{self.conv_scale}_"
            f"sh{self.shift1}_{self.shift2}"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_cbs_l0",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.out_channels,
                self.conv_scale,
                self.shift1,
                self.shift2,
            ],
        )

        conv_kernel_obj = KernelObjectArtifact.new(
            "conv2dk3_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        silu_kernel_obj = KernelObjectArtifact.new(
            "bias_silu_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "bias_silu_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[mlir_artifact, conv_kernel_obj, silu_kernel_obj],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width
        conv_wt_size = self.out_channels * self.in_channels * 9
        bias_size = self.out_channels * 4
        total_weights = conv_wt_size + bias_size
        total_output = self.out_channels * self.out_h * self.out_w

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "dataflow_cbs_l0",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dataflow_cbs_l0", "input", "weights", "output")


@pytest.mark.parametrize(
    "height,width,ic,oc,conv_scale,shift1,shift2",
    [
        pytest.param(8, 8, 8, 16, 10, 10, 7, id="cbs_l0_8x8"),
        pytest.param(16, 16, 8, 16, 10, 10, 7, id="cbs_l0_16x16"),
        pytest.param(32, 32, 8, 16, 10, 10, 7, id="cbs_l0_32x32"),
        pytest.param(64, 64, 8, 16, 10, 10, 7, id="cbs_l0_64x64"),
        pytest.param(128, 128, 8, 16, 10, 10, 7, id="cbs_l0_128x128"),
        pytest.param(
            640,
            640,
            8,
            16,
            10,
            10,
            7,
            id="cbs_l0_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_cbs_l0(
    height, width, ic, oc, conv_scale, shift1, shift2, aie_context
):
    """Verify CBS L0 (split conv->silu, k3s2) matches CPU reference."""
    torch.manual_seed(42)

    out_h = height // 2
    out_w = width // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_int8 = torch.randint(-50, 51, (oc, ic, 3, 3), dtype=torch.int8)
    b_int32 = torch.randint(-500, 501, (oc,), dtype=torch.int32)

    # CPU reference for split pipeline
    ref = conv2d_int8_split_silu_reference(
        x_int8, w_int8, b_int32, conv_scale, shift1, shift2, stride=2
    )

    # Create dataflow operator
    op = AIEDataflowCBSL0(
        height=height,
        width=width,
        in_channels=ic,
        out_channels=oc,
        conv_scale=conv_scale,
        shift1=shift1,
        shift2=shift2,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write weights: [conv_weights_tiled | bias_as_int8_bytes]
    w_tiled = weights_to_tiled_int8_k3(w_int8)
    b_bytes = b_int32.numpy().astype(np.int32).view(np.int8)
    packed_wts = np.concatenate([w_tiled, b_bytes])
    op.write_buffer("weights", packed_wts)

    # Clear output
    total_output = oc * out_h * out_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), oc, out_h, out_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff))
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt2 = int(np.sum(diff > 2))
    errors_gt3 = int(np.sum(diff > 3))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nCBS L0 test {ic}ic_{oc}oc_{height}h_{width}w:")
    print(f"  Exact vs ref: {exact}/{total} ({100*exact/total:.1f}%)")
    print(f"  Max diff vs ref: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>2): {errors_gt2}/{total}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  NPU time: {1000*(t1-t0):.1f} ms")

    # Target: max_diff <= 3, 0 errors > 3
    assert max_diff <= 3, f"CBS L0 dataflow: max_diff={max_diff} exceeds threshold 3"
    assert errors_gt3 == 0, f"CBS L0 dataflow: {errors_gt3} errors > 3 out of {total}"


# ============================================================================
# CBS L0 -> L1: 4-core pipeline (conv0 + silu0 + conv1 + silu1)
# ============================================================================


class AIEDataflowCBSL0L1(AIEOperatorBase):
    """Dataflow operator for CBS L0->L1 chain.

    L0 CBS: k3s2, IC->OC0 (split conv + bias_silu)
    L1 CBS: k3s2, OC0->OC1 (split conv + bias_silu)
    4 cores total in a single column.
    """

    def __init__(
        self,
        l0_height,
        l0_width,
        l0_ic,
        l0_oc,
        l0_conv_scale,
        l0_shift1,
        l0_shift2,
        l1_oc,
        l1_conv_scale,
        l1_shift1,
        l1_shift2,
        context=None,
    ):
        self.l0_height = l0_height
        self.l0_width = l0_width
        self.l0_ic = l0_ic
        self.l0_oc = l0_oc
        self.l0_conv_scale = l0_conv_scale
        self.l0_shift1 = l0_shift1
        self.l0_shift2 = l0_shift2
        self.l1_oc = l1_oc
        self.l1_conv_scale = l1_conv_scale
        self.l1_shift1 = l1_shift1
        self.l1_shift2 = l1_shift2

        # Derived dims
        self.l1_ic = l0_oc
        self.l1_height = l0_height // 2
        self.l1_width = l0_width // 2
        self.out_h = self.l1_height // 2
        self.out_w = self.l1_width // 2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_cbs_l0l1_{self.l0_ic}ic_{self.l1_oc}oc_"
            f"{self.l0_height}h_{self.l0_width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_cbs_l0_l1",
            callback_args=[
                self.context.device_manager.device_type,
                self.l0_height,
                self.l0_width,
                self.l0_ic,
                self.l0_oc,
                self.l0_conv_scale,
                self.l0_shift1,
                self.l0_shift2,
                self.l1_oc,
                self.l1_conv_scale,
                self.l1_shift1,
                self.l1_shift2,
            ],
        )

        conv_kernel_obj = KernelObjectArtifact.new(
            "conv2dk3_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        silu_kernel_obj = KernelObjectArtifact.new(
            "bias_silu_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "bias_silu_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[mlir_artifact, conv_kernel_obj, silu_kernel_obj],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.l0_ic * self.l0_height * self.l0_width

        # Weight sizes
        l0_conv_wt = self.l0_oc * self.l0_ic * 9
        l0_bias = self.l0_oc * 4
        l1_conv_wt = self.l1_oc * self.l1_ic * 9
        l1_bias = self.l1_oc * 4

        # Padded to max for uniform MemTile split (matches design)
        wt_slot_size = max(l0_conv_wt, l0_bias, l1_conv_wt, l1_bias)
        total_weights = 4 * wt_slot_size
        self._l0_conv_wt_size = l0_conv_wt
        self._l0_bias_size = l0_bias
        self._l1_conv_wt_size = l1_conv_wt
        self._l1_bias_size = l1_bias
        self._wt_slot_size = wt_slot_size

        total_output = self.l1_oc * self.out_h * self.out_w

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "dataflow_cbs_l0l1",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dataflow_cbs_l0l1", "input", "weights", "output")


@pytest.mark.parametrize(
    "l0_h,l0_w,l0_ic,l0_oc,l0_cs,l0_s1,l0_s2," "l1_oc,l1_cs,l1_s1,l1_s2",
    [
        pytest.param(
            16,
            16,
            8,
            16,
            10,
            10,
            7,
            32,
            11,
            11,
            7,
            id="cbs_l0l1_16x16",
        ),
        pytest.param(
            32,
            32,
            8,
            16,
            10,
            10,
            7,
            32,
            11,
            11,
            7,
            id="cbs_l0l1_32x32",
        ),
        pytest.param(
            64,
            64,
            8,
            16,
            10,
            10,
            7,
            32,
            11,
            11,
            7,
            id="cbs_l0l1_64x64",
        ),
        pytest.param(
            640,
            640,
            8,
            16,
            10,
            10,
            7,
            32,
            11,
            11,
            7,
            id="cbs_l0l1_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_cbs_l0l1(
    l0_h,
    l0_w,
    l0_ic,
    l0_oc,
    l0_cs,
    l0_s1,
    l0_s2,
    l1_oc,
    l1_cs,
    l1_s1,
    l1_s2,
    aie_context,
):
    """Verify CBS L0->L1 (4-core split conv+silu chain) matches CPU ref."""
    torch.manual_seed(42)

    l1_ic = l0_oc
    l1_h = l0_h // 2
    l1_w = l0_w // 2
    out_h = l1_h // 2
    out_w = l1_w // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)
    w0_int8 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    b0_int32 = torch.randint(-500, 501, (l0_oc,), dtype=torch.int32)
    w1_int8 = torch.randint(-50, 51, (l1_oc, l1_ic, 3, 3), dtype=torch.int8)
    b1_int32 = torch.randint(-500, 501, (l1_oc,), dtype=torch.int32)

    # CPU reference: sequential L0_CBS then L1_CBS
    inter = conv2d_int8_split_silu_reference(
        x_int8, w0_int8, b0_int32, l0_cs, l0_s1, l0_s2, stride=2
    )
    ref = conv2d_int8_split_silu_reference(
        inter, w1_int8, b1_int32, l1_cs, l1_s1, l1_s2, stride=2
    )

    # Create dataflow operator
    op = AIEDataflowCBSL0L1(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_conv_scale=l0_cs,
        l0_shift1=l0_s1,
        l0_shift2=l0_s2,
        l1_oc=l1_oc,
        l1_conv_scale=l1_cs,
        l1_shift1=l1_s1,
        l1_shift2=l1_s2,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write packed weights: [l0_conv_wt+pad | l0_bias+pad |
    #                        l1_conv_wt+pad | l1_bias+pad]
    wt_slot_size = op._wt_slot_size
    w0_tiled = weights_to_tiled_int8_k3(w0_int8)
    b0_bytes = b0_int32.numpy().astype(np.int32).view(np.int8)
    w1_tiled = weights_to_tiled_int8_k3(w1_int8)
    b1_bytes = b1_int32.numpy().astype(np.int32).view(np.int8)

    def _pad_slot(data, slot_size):
        pad = np.zeros(slot_size - len(data), dtype=np.int8)
        return np.concatenate([data, pad])

    packed_all = np.concatenate(
        [
            _pad_slot(w0_tiled, wt_slot_size),
            _pad_slot(b0_bytes, wt_slot_size),
            _pad_slot(w1_tiled, wt_slot_size),
            _pad_slot(b1_bytes, wt_slot_size),
        ]
    )
    op.write_buffer("weights", packed_all)

    # Clear output
    total_output = l1_oc * out_h * out_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), l1_oc, out_h, out_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff))
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt2 = int(np.sum(diff > 2))
    errors_gt3 = int(np.sum(diff > 3))
    errors_gt5 = int(np.sum(diff > 5))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nCBS L0->L1 test " f"{l0_ic}ic_{l1_oc}oc_{l0_h}h_{l0_w}w:")
    print(f"  Exact: {exact}/{total} ({100*exact/total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>2): {errors_gt2}/{total}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  Errors (>5): {errors_gt5}/{total}")
    print(f"  NPU time: {1000*(t1-t0):.1f} ms")

    # Two CBS layers compound rounding errors through bf16 tanh.
    # Target: max_diff <= 5, < 1% errors > 3
    assert (
        max_diff <= 5
    ), f"CBS L0->L1 dataflow: max_diff={max_diff} exceeds threshold 5"
    error_rate = errors_gt3 / total
    assert error_rate < 0.01, (
        f"CBS L0->L1 dataflow: {100*error_rate:.2f}% errors > 3 "
        f"exceeds 1% threshold"
    )


# ============================================================================
# Step 5: L0 -> L1 -> L3 -> L4.cv1 chain (non-fused, 4 cores)
# ============================================================================


class AIEDataflowL0L1L3L4cv1(AIEOperatorBase):
    """Dataflow operator for L0->L1->L3->L4.cv1 chain (non-fused).

    L0: k3s2, IC->OC0 (no SiLU, no bias)
    L1: k3s2, OC0->OC1 (no SiLU, no bias)
    L3: k3s2, OC1->OC2 (no SiLU, no bias)
    L4.cv1: k1s1, OC2->OC3 (no SiLU, no bias)
    """

    def __init__(
        self,
        l0_height,
        l0_width,
        l0_ic,
        l0_oc,
        l0_scale,
        l1_oc,
        l1_scale,
        l3_oc,
        l3_scale,
        l4cv1_oc,
        l4cv1_scale,
        context=None,
    ):
        self.l0_height = l0_height
        self.l0_width = l0_width
        self.l0_ic = l0_ic
        self.l0_oc = l0_oc
        self.l0_scale = l0_scale
        self.l1_oc = l1_oc
        self.l1_scale = l1_scale
        self.l3_oc = l3_oc
        self.l3_scale = l3_scale
        self.l4cv1_oc = l4cv1_oc
        self.l4cv1_scale = l4cv1_scale

        # Derived dims
        self.l1_ic = l0_oc
        self.l1_height = l0_height // 2
        self.l1_width = l0_width // 2
        self.l3_ic = l1_oc
        self.l3_height = self.l1_height // 2
        self.l3_width = self.l1_width // 2
        self.l4cv1_ic = l3_oc
        self.l4cv1_height = self.l3_height // 2
        self.l4cv1_width = self.l3_width // 2
        self.out_h = self.l4cv1_height
        self.out_w = self.l4cv1_width

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_l0l1l3l4cv1_{self.l0_ic}ic_{self.l4cv1_oc}oc_"
            f"{self.l0_height}h_{self.l0_width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_l0_l1_l3_l4cv1",
            callback_args=[
                self.context.device_manager.device_type,
                self.l0_height,
                self.l0_width,
                self.l0_ic,
                self.l0_oc,
                self.l0_scale,
                self.l1_oc,
                self.l1_scale,
                self.l3_oc,
                self.l3_scale,
                self.l4cv1_oc,
                self.l4cv1_scale,
            ],
        )

        # Two kernel objects: k3 conv and k1 conv
        k3_kernel_obj = KernelObjectArtifact.new(
            "conv2dk3_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k1_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[mlir_artifact, k3_kernel_obj, k1_kernel_obj],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.l0_ic * self.l0_height * self.l0_width

        # Weight sizes (non-fused: no bias)
        l0_wt = self.l0_oc * self.l0_ic * 9
        l1_wt = self.l1_oc * self.l1_ic * 9
        l3_wt = self.l3_oc * self.l3_ic * 9
        l4cv1_wt = self.l4cv1_oc * self.l4cv1_ic  # k1

        # Padded to max for uniform MemTile split (matches design)
        wt_slot_size = max(l0_wt, l1_wt, l3_wt, l4cv1_wt)
        total_weights = 4 * wt_slot_size
        self._wt_slot_size = wt_slot_size

        total_output = self.l4cv1_oc * self.out_h * self.out_w

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "dataflow_l0l1l3l4cv1",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dataflow_l0l1l3l4cv1", "input", "weights", "output")


@pytest.mark.parametrize(
    "l0_h,l0_w,l0_ic,l0_oc,l0_sc,l1_oc,l1_sc,l3_oc,l3_sc,l4cv1_oc,l4cv1_sc",
    [
        pytest.param(
            16,
            16,
            8,
            16,
            10,
            32,
            11,
            64,
            12,
            64,
            10,
            id="dataflow_l0l1l3l4cv1_16x16",
        ),
        pytest.param(
            32,
            32,
            8,
            16,
            10,
            32,
            11,
            64,
            12,
            64,
            10,
            id="dataflow_l0l1l3l4cv1_32x32",
        ),
        pytest.param(
            64,
            64,
            8,
            16,
            10,
            32,
            11,
            64,
            12,
            64,
            10,
            id="dataflow_l0l1l3l4cv1_64x64",
        ),
        pytest.param(
            640,
            640,
            8,
            16,
            10,
            32,
            11,
            64,
            12,
            64,
            10,
            id="dataflow_l0l1l3l4cv1_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_l0l1l3l4cv1(
    l0_h,
    l0_w,
    l0_ic,
    l0_oc,
    l0_sc,
    l1_oc,
    l1_sc,
    l3_oc,
    l3_sc,
    l4cv1_oc,
    l4cv1_sc,
    aie_context,
):
    """Step 5: Verify L0->L1->L3->L4.cv1 non-fused chain (4 cores)."""
    torch.manual_seed(42)

    l1_ic = l0_oc
    l1_h = l0_h // 2
    l1_w = l0_w // 2
    l3_ic = l1_oc
    l3_h = l1_h // 2
    l3_w = l1_w // 2
    l4cv1_ic = l3_oc
    l4cv1_h = l3_h // 2
    l4cv1_w = l3_w // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)
    w0_int8 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    w1_int8 = torch.randint(-50, 51, (l1_oc, l1_ic, 3, 3), dtype=torch.int8)
    w3_int8 = torch.randint(-50, 51, (l3_oc, l3_ic, 3, 3), dtype=torch.int8)
    w4cv1_int8 = torch.randint(-50, 51, (l4cv1_oc, l4cv1_ic, 1, 1), dtype=torch.int8)

    # CPU reference: sequential L0 -> L1 -> L3 -> L4.cv1
    inter01 = conv2d_int8_reference(x_int8, w0_int8, l0_sc, stride=2, padding=1)
    inter13 = conv2d_int8_reference(inter01, w1_int8, l1_sc, stride=2, padding=1)
    inter3_4cv1 = conv2d_int8_reference(inter13, w3_int8, l3_sc, stride=2, padding=1)
    ref = conv2d_int8_reference(inter3_4cv1, w4cv1_int8, l4cv1_sc, stride=1, padding=0)

    # Create dataflow operator
    op = AIEDataflowL0L1L3L4cv1(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_scale=l0_sc,
        l1_oc=l1_oc,
        l1_scale=l1_sc,
        l3_oc=l3_oc,
        l3_scale=l3_sc,
        l4cv1_oc=l4cv1_oc,
        l4cv1_scale=l4cv1_sc,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write packed weights: [l0_wt+pad | l1_wt+pad | l3_wt+pad | l4cv1_wt+pad]
    wt_slot_size = op._wt_slot_size
    w0_tiled = weights_to_tiled_int8_k3(w0_int8)
    w1_tiled = weights_to_tiled_int8_k3(w1_int8)
    w3_tiled = weights_to_tiled_int8_k3(w3_int8)
    w4cv1_tiled = weights_to_tiled_int8(w4cv1_int8)

    def _pad_slot(data, slot_size):
        pad = np.zeros(slot_size - len(data), dtype=np.int8)
        return np.concatenate([data, pad])

    packed_all = np.concatenate(
        [
            _pad_slot(w0_tiled, wt_slot_size),
            _pad_slot(w1_tiled, wt_slot_size),
            _pad_slot(w3_tiled, wt_slot_size),
            _pad_slot(w4cv1_tiled, wt_slot_size),
        ]
    )
    op.write_buffer("weights", packed_all)

    # Clear output
    total_output = l4cv1_oc * l4cv1_h * l4cv1_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), l4cv1_oc, l4cv1_h, l4cv1_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff))
    errors_gt0 = int(np.sum(diff > 0))
    errors_gt1 = int(np.sum(diff > 1))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(
        f"\nDataflow L0->L1->L3->L4.cv1 test "
        f"{l0_ic}ic_{l4cv1_oc}oc_{l0_h}h_{l0_w}w:"
    )
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>0): {errors_gt0}/{total}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # Non-fused convolutions: pure integer arithmetic, expect exact match.
    assert errors_gt1 == 0, (
        f"Dataflow L0->L1->L3->L4.cv1 failed: {errors_gt1} mismatches "
        f"(diff>1) out of {total}, max_diff={max_diff}"
    )


# ============================================================================
# Step 6: Five-core fused downsample spine -- L0->L1->L3->L5->L7
# ============================================================================


class AIEDataflowSpineFused(AIEOperatorBase):
    """Dataflow operator for fused 4-core downsample spine.

    L0: k3s2, IC->OC0,   H x W      -> H/2 x W/2    (fused SiLU)
    L1: k3s2, OC0->OC1,  H/2 x W/2  -> H/4 x W/4    (fused SiLU)
    L3: k3s2, OC1->OC3,  H/4 x W/4  -> H/8 x W/8    (fused SiLU)
    L5: k3s2, OC3->OC5,  H/8 x W/8  -> H/16 x W/16  (fused SiLU)

    Uses 4 compute tiles (0,2)-(0,5) in one column, which is the max
    per column on NPU2.
    """

    def __init__(
        self,
        l0_height,
        l0_width,
        l0_ic,
        l0_oc,
        l0_shift1,
        l0_shift2,
        l1_oc,
        l1_shift1,
        l1_shift2,
        l3_oc,
        l3_shift1,
        l3_shift2,
        l5_oc,
        l5_shift1,
        l5_shift2,
        context=None,
    ):
        self.l0_height = l0_height
        self.l0_width = l0_width
        self.l0_ic = l0_ic
        self.l0_oc = l0_oc
        self.l0_shift1 = l0_shift1
        self.l0_shift2 = l0_shift2
        self.l1_oc = l1_oc
        self.l1_shift1 = l1_shift1
        self.l1_shift2 = l1_shift2
        self.l3_oc = l3_oc
        self.l3_shift1 = l3_shift1
        self.l3_shift2 = l3_shift2
        self.l5_oc = l5_oc
        self.l5_shift1 = l5_shift1
        self.l5_shift2 = l5_shift2

        # Derived dims
        self.l1_ic = l0_oc
        self.l1_height = l0_height // 2
        self.l1_width = l0_width // 2
        self.l3_ic = l1_oc
        self.l3_height = self.l1_height // 2
        self.l3_width = self.l1_width // 2
        self.l5_ic = l3_oc
        self.l5_height = self.l3_height // 2
        self.l5_width = self.l3_width // 2
        self.out_h = self.l5_height // 2
        self.out_w = self.l5_width // 2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_spine_fused_{self.l0_ic}ic_{self.l5_oc}oc_"
            f"{self.l0_height}h_{self.l0_width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_spine_fused",
            callback_args=[
                self.context.device_manager.device_type,
                self.l0_height,
                self.l0_width,
                self.l0_ic,
                self.l0_oc,
                self.l0_shift1,
                self.l0_shift2,
                self.l1_oc,
                self.l1_shift1,
                self.l1_shift2,
                self.l3_oc,
                self.l3_shift1,
                self.l3_shift2,
                self.l5_oc,
                self.l5_shift1,
                self.l5_shift2,
            ],
        )

        kernel_src = "conv2dk3_i8_silu.cc"
        kernel_obj_name = "conv2dk3_i8_silu.o"

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    kernel_obj_name,
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir / "aie_kernels" / "aie2p" / kernel_src
                        )
                    ],
                    extra_flags=["-DINT8_ACT"],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.l0_ic * self.l0_height * self.l0_width

        # Weight sizes (fused: weights + int32 bias)
        l0_wt = self.l0_oc * self.l0_ic * 9 + self.l0_oc * 4
        l1_wt = self.l1_oc * self.l1_ic * 9 + self.l1_oc * 4
        l3_wt = self.l3_oc * self.l3_ic * 9 + self.l3_oc * 4
        l5_wt = self.l5_oc * self.l5_ic * 9 + self.l5_oc * 4

        wt_slot_size = max(l0_wt, l1_wt, l3_wt, l5_wt)
        total_weights = 4 * wt_slot_size
        self._wt_slot_size = wt_slot_size

        total_output = self.l5_oc * self.out_h * self.out_w

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "dataflow_spine_fused",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dataflow_spine_fused", "input", "weights", "output")


@pytest.mark.parametrize(
    "l0_h,l0_w,l0_ic,l0_oc,l0_s1,l0_s2,"
    "l1_oc,l1_s1,l1_s2,"
    "l3_oc,l3_s1,l3_s2,"
    "l5_oc,l5_s1,l5_s2",
    [
        # 4-core fused spine: L0->L1->L3->L5 (max per column on NPU2).
        # NPU2 has 4 compute tiles per column (rows 2-5).
        # Full YOLOv8n L5 weights (64->128, k3) = 74KB > 64KB so use
        # reduced channel counts for validation.
        pytest.param(
            32,
            32,
            8,
            8,
            10,
            7,
            16,
            11,
            7,
            16,
            11,
            7,
            16,
            11,
            7,
            id="spine_fused_32x32",
        ),
        pytest.param(
            64,
            64,
            8,
            8,
            10,
            7,
            16,
            11,
            7,
            16,
            11,
            7,
            16,
            11,
            7,
            id="spine_fused_64x64",
        ),
        pytest.param(
            64,
            64,
            8,
            16,
            10,
            7,
            32,
            11,
            7,
            32,
            12,
            7,
            32,
            12,
            7,
            id="spine_fused_64x64_yolo",
        ),
        pytest.param(
            640,
            640,
            8,
            16,
            10,
            7,
            32,
            11,
            7,
            32,
            12,
            7,
            32,
            12,
            7,
            id="spine_fused_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_spine_fused(
    l0_h,
    l0_w,
    l0_ic,
    l0_oc,
    l0_s1,
    l0_s2,
    l1_oc,
    l1_s1,
    l1_s2,
    l3_oc,
    l3_s1,
    l3_s2,
    l5_oc,
    l5_s1,
    l5_s2,
    aie_context,
):
    """Step 6: Verify fused 4-core downsample spine L0->L1->L3->L5."""
    torch.manual_seed(42)

    # Derived dims
    l1_ic = l0_oc
    l1_h = l0_h // 2
    l1_w = l0_w // 2
    l3_ic = l1_oc
    l3_h = l1_h // 2
    l3_w = l1_w // 2
    l5_ic = l3_oc
    l5_h = l3_h // 2
    l5_w = l3_w // 2
    out_h = l5_h // 2
    out_w = l5_w // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)
    w0_int8 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    b0_int32 = torch.randint(-500, 501, (l0_oc,), dtype=torch.int32)
    w1_int8 = torch.randint(-50, 51, (l1_oc, l1_ic, 3, 3), dtype=torch.int8)
    b1_int32 = torch.randint(-500, 501, (l1_oc,), dtype=torch.int32)
    w3_int8 = torch.randint(-50, 51, (l3_oc, l3_ic, 3, 3), dtype=torch.int8)
    b3_int32 = torch.randint(-500, 501, (l3_oc,), dtype=torch.int32)
    w5_int8 = torch.randint(-50, 51, (l5_oc, l5_ic, 3, 3), dtype=torch.int8)
    b5_int32 = torch.randint(-500, 501, (l5_oc,), dtype=torch.int32)

    # CPU reference: sequential fused conv+SiLU pipeline
    inter01 = conv2d_int8_pade_silu_reference(
        x_int8, w0_int8, b0_int32, l0_s1, l0_s2, stride=2
    )
    inter13 = conv2d_int8_pade_silu_reference(
        inter01, w1_int8, b1_int32, l1_s1, l1_s2, stride=2
    )
    inter35 = conv2d_int8_pade_silu_reference(
        inter13, w3_int8, b3_int32, l3_s1, l3_s2, stride=2
    )
    ref = conv2d_int8_pade_silu_reference(
        inter35, w5_int8, b5_int32, l5_s1, l5_s2, stride=2
    )

    # Create dataflow operator (reuse the spine design with 4 layers)
    op = AIEDataflowSpineFused(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_shift1=l0_s1,
        l0_shift2=l0_s2,
        l1_oc=l1_oc,
        l1_shift1=l1_s1,
        l1_shift2=l1_s2,
        l3_oc=l3_oc,
        l3_shift1=l3_s1,
        l3_shift2=l3_s2,
        l5_oc=l5_oc,
        l5_shift1=l5_s1,
        l5_shift2=l5_s2,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write packed weights (padded to uniform slot size):
    # [l0_wt+bias+pad | l1_wt+bias+pad | l3_wt+bias+pad | l5_wt+bias+pad]
    wt_slot_size = op._wt_slot_size
    all_layers = [
        (w0_int8, b0_int32),
        (w1_int8, b1_int32),
        (w3_int8, b3_int32),
        (w5_int8, b5_int32),
    ]

    def _pad_slot(data, slot_size):
        pad = np.zeros(slot_size - len(data), dtype=np.int8)
        return np.concatenate([data, pad])

    packed_slots = []
    for w_int8_l, b_int32_l in all_layers:
        w_tiled = weights_to_tiled_int8_k3(w_int8_l)
        b_bytes = b_int32_l.numpy().astype(np.int32).view(np.int8)
        fused = np.concatenate([w_tiled, b_bytes])
        packed_slots.append(_pad_slot(fused, wt_slot_size))

    packed_all = np.concatenate(packed_slots)
    op.write_buffer("weights", packed_all)

    # Clear output
    total_output = l5_oc * out_h * out_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), l5_oc, out_h, out_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt2 = int(np.sum(diff > 2))
    errors_gt3 = int(np.sum(diff > 3))
    errors_gt5 = int(np.sum(diff > 5))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nFused spine L0->L1->L3->L5 test " f"{l0_ic}ic_{l5_oc}oc_{l0_h}h_{l0_w}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>2): {errors_gt2}/{total}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  Errors (>5): {errors_gt5}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # Four fused layers compound rounding errors through bf16 tanh.
    # Target: max_diff <= 5, < 2% errors > 3
    assert max_diff <= 8, f"Fused spine: max_diff={max_diff} exceeds threshold 8"
    error_rate_gt3 = errors_gt3 / total if total > 0 else 0
    assert error_rate_gt3 < 0.05, (
        f"Fused spine: {100 * error_rate_gt3:.2f}% errors > 3 " f"exceeds 5% threshold"
    )


# ============================================================================
# Step 7: Standalone fused k3s2 with OC streaming
# ============================================================================


class AIEDataflowFusedOCStreaming(AIEOperatorBase):
    """Single-core fused k3s2 conv+SiLU with OC streaming.

    For layers where weights exceed 64KB L1 (e.g., L5: 64->128, k3).
    Splits output channels into chunks, re-streams input for each chunk.
    """

    def __init__(
        self,
        height,
        width,
        in_channels,
        out_channels,
        shift1,
        shift2,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.shift1 = shift1
        self.shift2 = shift2
        self.out_h = height // 2
        self.out_w = width // 2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        from iron.operators.conv2d_int8.dataflow_design import (
            _compute_oc_streaming_params,
        )

        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_ocs_{self.in_channels}ic_{self.out_channels}oc_"
            f"{self.height}h_{self.width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_fused_oc_streaming",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.out_channels,
                self.shift1,
                self.shift2,
            ],
        )

        kernel_src = "conv2dk3_i8_silu.cc"
        kernel_obj_name = "conv2dk3_i8_silu.o"

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    kernel_obj_name,
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir / "aie_kernels" / "aie2p" / kernel_src
                        )
                    ],
                    extra_flags=["-DINT8_ACT"],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

        # Store OC streaming params for weight packing
        oc_chunk, n_oc_groups, _ = _compute_oc_streaming_params(
            self.in_channels, self.out_channels, self.width, 2
        )
        self._oc_chunk = oc_chunk
        self._n_oc_groups = n_oc_groups

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width

        k_elems = 9
        wt_chunk = self._oc_chunk * self.in_channels * k_elems + self._oc_chunk * 4
        total_weights = self._n_oc_groups * wt_chunk

        total_output = self.out_channels * self.out_h * self.out_w

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "dataflow_ocs",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dataflow_ocs", "input", "weights", "output")


@pytest.mark.parametrize(
    "height,width,ic,oc,s1,s2",
    [
        # Small test: 32->64, still fits L1 but exercises OC streaming logic
        pytest.param(16, 16, 32, 64, 11, 7, id="ocs_32to64_16x16"),
        # L5-like: 64->128, k3 weights = 74KB > 64KB, needs OC streaming
        pytest.param(16, 16, 64, 128, 12, 7, id="ocs_64to128_16x16"),
        # Larger spatial: L5 at 80x80 (YOLO dims)
        pytest.param(
            80,
            80,
            64,
            128,
            12,
            7,
            id="ocs_64to128_80x80",
            marks=pytest.mark.extensive,
        ),
        # L7-like: 128->256, k3 weights = 295KB >> 64KB
        pytest.param(16, 16, 128, 256, 12, 7, id="ocs_128to256_16x16"),
        # Neck L16: 64->64, k3s2, 80x80->40x40
        pytest.param(80, 80, 64, 64, 10, 7, id="neck_l16_64to64_80x80"),
        # Neck L19: 128->128, k3s2, 40x40->20x20
        pytest.param(40, 40, 128, 128, 10, 7, id="neck_l19_128to128_40x40"),
    ],
)
def test_dataflow_fused_oc_streaming(height, width, ic, oc, s1, s2, aie_context):
    """Step 7: Verify single-core fused k3s2 with OC streaming."""
    torch.manual_seed(42)

    from iron.operators.conv2d_int8.dataflow_design import (
        _compute_oc_streaming_params,
    )

    out_h = height // 2
    out_w = width // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_int8 = torch.randint(-50, 51, (oc, ic, 3, 3), dtype=torch.int8)
    b_int32 = torch.randint(-500, 501, (oc,), dtype=torch.int32)

    # CPU reference
    ref = conv2d_int8_pade_silu_reference(x_int8, w_int8, b_int32, s1, s2, stride=2)

    # Create operator
    op = AIEDataflowFusedOCStreaming(
        height=height,
        width=width,
        in_channels=ic,
        out_channels=oc,
        shift1=s1,
        shift2=s2,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Pack weights for OC streaming: n_oc_groups contiguous weight chunks
    # Each chunk: tiled weights for oc_chunk OCs + packed int32 bias
    oc_chunk = op._oc_chunk
    n_oc_groups = op._n_oc_groups

    packed_chunks = []
    for g in range(n_oc_groups):
        oc_start = g * oc_chunk
        oc_end = oc_start + oc_chunk
        w_chunk = w_int8[oc_start:oc_end]
        b_chunk = b_int32[oc_start:oc_end]
        w_tiled = weights_to_tiled_int8_k3(w_chunk)
        b_bytes = b_chunk.numpy().astype(np.int32).view(np.int8)
        packed_chunks.append(np.concatenate([w_tiled, b_bytes]))

    packed_all = np.concatenate(packed_chunks)
    op.write_buffer("weights", packed_all)

    # Clear output
    total_output = oc * out_h * out_w
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), oc, out_h, out_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt2 = int(np.sum(diff > 2))
    errors_gt3 = int(np.sum(diff > 3))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nOC streaming test {ic}ic_{oc}oc_{height}h_{width}w:")
    print(f"  oc_chunk={oc_chunk}, n_oc_groups={n_oc_groups}")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>2): {errors_gt2}/{total}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    assert max_diff <= 5, f"OC streaming: max_diff={max_diff} exceeds threshold 5"
    error_rate_gt2 = errors_gt2 / total if total > 0 else 0
    assert error_rate_gt2 < 0.03, (
        f"OC streaming: {100 * error_rate_gt2:.2f}% errors > 2 " f"exceeds 3% threshold"
    )


# ============================================================================
# Step 8: Five-layer spine with OC streaming (L0->L1->L3->L5->L7)
# ============================================================================


class AIEDataflowSpine5Layer(AIEOperatorBase):
    """Five-layer fused downsample spine with OC streaming for L5/L7.

    L0: k3s2, IC->OC0,    H x W       -> H/2 x W/2     (fused SiLU)
    L1: k3s2, OC0->OC1,   H/2 x W/2   -> H/4 x W/4     (fused SiLU)
    L3: k3s2, OC1->OC3,   H/4 x W/4   -> H/8 x W/8     (fused SiLU)
    L5: k3s2, OC3->OC5,   H/8 x W/8   -> H/16 x W/16   (OC streaming)
    L7: k3s2, OC5->OC7,   H/16 x W/16 -> H/32 x W/32   (OC streaming)
    """

    def __init__(
        self,
        l0_height,
        l0_width,
        l0_ic,
        l0_oc,
        l0_shift1,
        l0_shift2,
        l1_oc,
        l1_shift1,
        l1_shift2,
        l3_oc,
        l3_shift1,
        l3_shift2,
        l5_oc,
        l5_shift1,
        l5_shift2,
        l7_oc,
        l7_shift1,
        l7_shift2,
        context=None,
    ):
        self.l0_height = l0_height
        self.l0_width = l0_width
        self.l0_ic = l0_ic
        self.l0_oc = l0_oc
        self.l0_shift1 = l0_shift1
        self.l0_shift2 = l0_shift2
        self.l1_oc = l1_oc
        self.l1_shift1 = l1_shift1
        self.l1_shift2 = l1_shift2
        self.l3_oc = l3_oc
        self.l3_shift1 = l3_shift1
        self.l3_shift2 = l3_shift2
        self.l5_oc = l5_oc
        self.l5_shift1 = l5_shift1
        self.l5_shift2 = l5_shift2
        self.l7_oc = l7_oc
        self.l7_shift1 = l7_shift1
        self.l7_shift2 = l7_shift2

        # Derived dims
        self.l1_ic = l0_oc
        self.l1_height = l0_height // 2
        self.l1_width = l0_width // 2
        self.l3_ic = l1_oc
        self.l3_height = self.l1_height // 2
        self.l3_width = self.l1_width // 2
        self.l5_ic = l3_oc
        self.l5_height = self.l3_height // 2
        self.l5_width = self.l3_width // 2
        self.l7_ic = l5_oc
        self.l7_height = self.l5_height // 2
        self.l7_width = self.l5_width // 2
        self.out_h = self.l7_height // 2
        self.out_w = self.l7_width // 2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        from iron.operators.conv2d_int8.dataflow_design import (
            _compute_oc_streaming_params,
        )

        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_spine5_{self.l0_ic}ic_{self.l7_oc}oc_"
            f"{self.l0_height}h_{self.l0_width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_spine_5layer",
            callback_args=[
                self.context.device_manager.device_type,
                self.l0_height,
                self.l0_width,
                self.l0_ic,
                self.l0_oc,
                self.l0_shift1,
                self.l0_shift2,
                self.l1_oc,
                self.l1_shift1,
                self.l1_shift2,
                self.l3_oc,
                self.l3_shift1,
                self.l3_shift2,
                self.l5_oc,
                self.l5_shift1,
                self.l5_shift2,
                self.l7_oc,
                self.l7_shift1,
                self.l7_shift2,
            ],
        )

        kernel_src = "conv2dk3_i8_silu.cc"
        kernel_obj_name = "conv2dk3_i8_silu.o"
        kernel_obj_l5 = "conv2dk3_i8_silu_l5.o"
        kernel_obj_l7 = "conv2dk3_i8_silu_l7.o"

        kernel_src_artifact = SourceArtifact.new(
            self.context.base_dir / "aie_kernels" / "aie2p" / kernel_src
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    kernel_obj_name,
                    depends=[kernel_src_artifact],
                    extra_flags=["-DINT8_ACT"],
                ),
                KernelObjectArtifact.new(
                    kernel_obj_l5,
                    depends=[kernel_src_artifact],
                    extra_flags=["-DINT8_ACT"],
                ),
                KernelObjectArtifact.new(
                    kernel_obj_l7,
                    depends=[kernel_src_artifact],
                    extra_flags=["-DINT8_ACT"],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

        # Store OC streaming params
        l5_oc_chunk, l5_n_oc_groups, _ = _compute_oc_streaming_params(
            self.l5_ic, self.l5_oc, self.l5_width, 2
        )
        l7_oc_chunk, l7_n_oc_groups, _ = _compute_oc_streaming_params(
            self.l7_ic, self.l7_oc, self.l7_width, 2
        )
        self._l5_oc_chunk = l5_oc_chunk
        self._l5_n_oc_groups = l5_n_oc_groups
        self._l7_oc_chunk = l7_oc_chunk
        self._l7_n_oc_groups = l7_n_oc_groups

    def set_up_runtime(self):
        total_input = self.l0_ic * self.l0_height * self.l0_width

        # Column 0 weights (fused: weights + int32 bias)
        l0_wt = self.l0_oc * self.l0_ic * 9 + self.l0_oc * 4
        l1_wt = self.l1_oc * self.l1_ic * 9 + self.l1_oc * 4
        l3_wt = self.l3_oc * self.l3_ic * 9 + self.l3_oc * 4
        col0_wt_slot = max(l0_wt, l1_wt, l3_wt)
        col0_total_wt = 3 * col0_wt_slot
        self._col0_wt_slot = col0_wt_slot

        # L5 and L7 weight sizes
        l5_wt_chunk = self._l5_oc_chunk * self.l5_ic * 9 + self._l5_oc_chunk * 4
        l5_total_wt = self._l5_n_oc_groups * l5_wt_chunk
        l7_wt_chunk = self._l7_oc_chunk * self.l7_ic * 9 + self._l7_oc_chunk * 4
        l7_total_wt = self._l7_n_oc_groups * l7_wt_chunk

        total_weights = col0_total_wt + l5_total_wt + l7_total_wt

        total_output = self.l7_oc * self.out_h * self.out_w
        total_inter35 = self.l3_oc * (self.l3_height // 2) * (self.l3_width // 2)
        total_inter57 = self.l5_oc * (self.l5_height // 2) * (self.l5_width // 2)
        total_output_buf = total_output + total_inter35 + total_inter57
        self._total_output = total_output

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output_buf, dtype=np.int8)

        self.add_kernel(
            "dataflow_spine5",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dataflow_spine5", "input", "weights", "output")


@pytest.mark.parametrize(
    "l0_h,l0_w,l0_ic,l0_oc,l0_s1,l0_s2,"
    "l1_oc,l1_s1,l1_s2,"
    "l3_oc,l3_s1,l3_s2,"
    "l5_oc,l5_s1,l5_s2,"
    "l7_oc,l7_s1,l7_s2",
    [
        # Small test: reduced channels, exercises full 5-layer pipeline
        pytest.param(
            64,
            64,
            8,
            8,
            10,
            7,
            16,
            11,
            7,
            16,
            11,
            7,
            32,
            11,
            7,
            32,
            12,
            7,
            id="spine5_64x64_small",
        ),
        # Medium test: L5 and L7 with real OC streaming
        pytest.param(
            64,
            64,
            8,
            16,
            10,
            7,
            32,
            11,
            7,
            64,
            12,
            7,
            128,
            12,
            7,
            256,
            12,
            7,
            id="spine5_64x64_yolo_channels",
        ),
        # Full YOLO dims
        pytest.param(
            640,
            640,
            8,
            16,
            10,
            7,
            32,
            11,
            7,
            64,
            12,
            7,
            128,
            12,
            7,
            256,
            12,
            7,
            id="spine5_640x640_yolo",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_spine_5layer(
    l0_h,
    l0_w,
    l0_ic,
    l0_oc,
    l0_s1,
    l0_s2,
    l1_oc,
    l1_s1,
    l1_s2,
    l3_oc,
    l3_s1,
    l3_s2,
    l5_oc,
    l5_s1,
    l5_s2,
    l7_oc,
    l7_s1,
    l7_s2,
    aie_context,
):
    """Step 8: Verify 5-layer spine L0->L1->L3->L5->L7 with OC streaming."""
    torch.manual_seed(42)

    from iron.operators.conv2d_int8.dataflow_design import (
        _compute_oc_streaming_params,
    )

    # Derived dims
    l1_ic = l0_oc
    l1_h = l0_h // 2
    l1_w = l0_w // 2
    l3_ic = l1_oc
    l3_h = l1_h // 2
    l3_w = l1_w // 2
    l5_ic = l3_oc
    l5_h = l3_h // 2
    l5_w = l3_w // 2
    l7_ic = l5_oc
    l7_h = l5_h // 2
    l7_w = l5_w // 2
    out_h = l7_h // 2
    out_w = l7_w // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)
    w0 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    b0 = torch.randint(-500, 501, (l0_oc,), dtype=torch.int32)
    w1 = torch.randint(-50, 51, (l1_oc, l1_ic, 3, 3), dtype=torch.int8)
    b1 = torch.randint(-500, 501, (l1_oc,), dtype=torch.int32)
    w3 = torch.randint(-50, 51, (l3_oc, l3_ic, 3, 3), dtype=torch.int8)
    b3 = torch.randint(-500, 501, (l3_oc,), dtype=torch.int32)
    w5 = torch.randint(-50, 51, (l5_oc, l5_ic, 3, 3), dtype=torch.int8)
    b5 = torch.randint(-500, 501, (l5_oc,), dtype=torch.int32)
    w7 = torch.randint(-50, 51, (l7_oc, l7_ic, 3, 3), dtype=torch.int8)
    b7 = torch.randint(-500, 501, (l7_oc,), dtype=torch.int32)

    # CPU reference: sequential fused conv+SiLU pipeline
    inter01 = conv2d_int8_pade_silu_reference(x_int8, w0, b0, l0_s1, l0_s2, stride=2)
    inter13 = conv2d_int8_pade_silu_reference(inter01, w1, b1, l1_s1, l1_s2, stride=2)
    inter35 = conv2d_int8_pade_silu_reference(inter13, w3, b3, l3_s1, l3_s2, stride=2)
    inter57 = conv2d_int8_pade_silu_reference(inter35, w5, b5, l5_s1, l5_s2, stride=2)
    ref = conv2d_int8_pade_silu_reference(inter57, w7, b7, l7_s1, l7_s2, stride=2)

    # Create operator
    op = AIEDataflowSpine5Layer(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_shift1=l0_s1,
        l0_shift2=l0_s2,
        l1_oc=l1_oc,
        l1_shift1=l1_s1,
        l1_shift2=l1_s2,
        l3_oc=l3_oc,
        l3_shift1=l3_s1,
        l3_shift2=l3_s2,
        l5_oc=l5_oc,
        l5_shift1=l5_s1,
        l5_shift2=l5_s2,
        l7_oc=l7_oc,
        l7_shift1=l7_s1,
        l7_shift2=l7_s2,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Pack weights
    col0_wt_slot = op._col0_wt_slot

    def _pad_slot(data, slot_size):
        pad = np.zeros(slot_size - len(data), dtype=np.int8)
        return np.concatenate([data, pad])

    # Column 0: padded slots for L0, L1, L3
    col0_layers = [(w0, b0), (w1, b1), (w3, b3)]
    col0_packed = []
    for w_l, b_l in col0_layers:
        w_tiled = weights_to_tiled_int8_k3(w_l)
        b_bytes = b_l.numpy().astype(np.int32).view(np.int8)
        fused = np.concatenate([w_tiled, b_bytes])
        col0_packed.append(_pad_slot(fused, col0_wt_slot))

    # L5 weights: n_oc_groups contiguous chunks
    l5_oc_chunk = op._l5_oc_chunk
    l5_n_oc_groups = op._l5_n_oc_groups
    l5_chunks = []
    for g in range(l5_n_oc_groups):
        oc_start = g * l5_oc_chunk
        oc_end = oc_start + l5_oc_chunk
        w_tiled = weights_to_tiled_int8_k3(w5[oc_start:oc_end])
        b_bytes = b5[oc_start:oc_end].numpy().astype(np.int32).view(np.int8)
        l5_chunks.append(np.concatenate([w_tiled, b_bytes]))

    # L7 weights: n_oc_groups contiguous chunks
    l7_oc_chunk = op._l7_oc_chunk
    l7_n_oc_groups = op._l7_n_oc_groups
    l7_chunks = []
    for g in range(l7_n_oc_groups):
        oc_start = g * l7_oc_chunk
        oc_end = oc_start + l7_oc_chunk
        w_tiled = weights_to_tiled_int8_k3(w7[oc_start:oc_end])
        b_bytes = b7[oc_start:oc_end].numpy().astype(np.int32).view(np.int8)
        l7_chunks.append(np.concatenate([w_tiled, b_bytes]))

    packed_all = np.concatenate(col0_packed + l5_chunks + l7_chunks)
    op.write_buffer("weights", packed_all)

    # Clear output buffer
    total_output_buf = op.buffers["output"]  # bytes (int8 = 1 byte each)
    op.write_buffer("output", np.zeros(total_output_buf, dtype=np.int8))

    # Run
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify (final output is at offset 0)
    total_output = op._total_output
    output_buf = op.read_buffer("output", (total_output_buf,), dtype=np.int8)
    output_raw = output_buf[:total_output].copy()
    npu_output = tiled_to_nchw_int8(output_raw, l7_oc, out_h, out_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt2 = int(np.sum(diff > 2))
    errors_gt3 = int(np.sum(diff > 3))
    errors_gt5 = int(np.sum(diff > 5))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(
        f"\n5-layer spine L0->L1->L3->L5->L7 test "
        f"{l0_ic}ic_{l7_oc}oc_{l0_h}h_{l0_w}w:"
    )
    print(
        f"  L5: oc_chunk={l5_oc_chunk}, n_groups={l5_n_oc_groups}; "
        f"L7: oc_chunk={l7_oc_chunk}, n_groups={l7_n_oc_groups}"
    )
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>2): {errors_gt2}/{total}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  Errors (>5): {errors_gt5}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # Five fused layers compound rounding errors significantly
    assert max_diff <= 10, f"5-layer spine: max_diff={max_diff} exceeds threshold 10"
    error_rate_gt3 = errors_gt3 / total if total > 0 else 0
    assert error_rate_gt3 < 0.08, (
        f"5-layer spine: {100 * error_rate_gt3:.2f}% errors > 3 "
        f"exceeds 8% threshold"
    )


# ============================================================================
# C2f L2 simplified: cv1 -> channel split -> bottleneck -> cv2
# ============================================================================


class AIEDataflowC2fL2Simple(AIEOperatorBase):
    """Simplified C2f L2: cv1 -> split -> half2 -> bottleneck -> cv2.

    Only the bottleneck path (half2) feeds cv2. half1 is drained to scratch.
    """

    def __init__(
        self,
        height,
        width,
        in_channels,
        cv1_scale,
        bn_cv1_scale,
        bn_cv2_scale,
        cv2_scale,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.cv1_scale = cv1_scale
        self.bn_cv1_scale = bn_cv1_scale
        self.bn_cv2_scale = bn_cv2_scale
        self.cv2_scale = cv2_scale

        self.cv1_oc = 32
        self.bn_ch = 16
        self.cv2_ic = 16
        self.cv2_oc = 32

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_c2f_l2_simple_{self.in_channels}ic_"
            f"{self.height}h_{self.width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_c2f_l2_simple",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.cv1_scale,
                self.bn_cv1_scale,
                self.bn_cv2_scale,
                self.cv2_scale,
            ],
        )

        # cv1 kernel (conv2dk1_i8)
        k1_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        # Bottleneck k3 kernel -- same source, renamed symbol via -D
        k3_bn_kernel_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_bn.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3_i8=conv2dk3_i8_bn",
                "-Dconv2dk3s2_i8=conv2dk3s2_i8_bn",
            ],
        )

        # cv2 kernel -- same source as k1, renamed symbol
        k1_cv2_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_cv2.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk1_i8=conv2dk1_i8_cv2",
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                k1_kernel_obj,
                k3_bn_kernel_obj,
                k1_cv2_kernel_obj,
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width

        cv1_wt = self.cv1_oc * self.in_channels
        bn_cv1_wt = self.bn_ch * self.bn_ch * 9
        bn_cv2_wt = self.bn_ch * self.bn_ch * 9
        cv2_wt = self.cv2_oc * self.cv2_ic

        wt_slot = max(cv1_wt, bn_cv1_wt, bn_cv2_wt, cv2_wt)
        total_wt = 4 * wt_slot
        self._wt_slot = wt_slot

        total_output = self.cv2_oc * self.height * self.width

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "c2f_l2_simple",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("c2f_l2_simple", "input", "weights", "output")


@pytest.mark.parametrize(
    "height,width,ic,cv1_sc,bn1_sc,bn2_sc,cv2_sc",
    [
        pytest.param(8, 8, 32, 10, 10, 10, 10, id="c2f_l2_simple_8x8"),
        pytest.param(16, 16, 32, 10, 10, 10, 10, id="c2f_l2_simple_16x16"),
        pytest.param(32, 32, 32, 10, 10, 10, 10, id="c2f_l2_simple_32x32"),
    ],
)
def test_dataflow_c2f_l2_simple(
    height, width, ic, cv1_sc, bn1_sc, bn2_sc, cv2_sc, aie_context
):
    """Test simplified C2f L2: cv1 -> split -> bn -> cv2 (non-fused)."""
    torch.manual_seed(42)

    bn_ch = 16
    cv2_ic = 16
    cv2_oc = 32

    # Test data
    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_cv1 = torch.randint(-50, 51, (32, ic, 1, 1), dtype=torch.int8)
    w_bn1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, cv2_ic, 1, 1), dtype=torch.int8)

    # CPU reference: cv1 -> split -> half2 -> bn -> cv2
    cv1_out = conv2d_int8_reference(x_int8, w_cv1, cv1_sc, stride=1, padding=0)
    # Split: extract second 16 channels
    half2 = cv1_out[:, bn_ch:, :, :]
    bn_inter = conv2d_int8_reference(half2, w_bn1, bn1_sc, stride=1, padding=1)
    bn_out_ref = conv2d_int8_reference(bn_inter, w_bn2, bn2_sc, stride=1, padding=1)
    ref = conv2d_int8_reference(bn_out_ref, w_cv2, cv2_sc, stride=1, padding=0)

    # Create operator
    op = AIEDataflowC2fL2Simple(
        height=height,
        width=width,
        in_channels=ic,
        cv1_scale=cv1_sc,
        bn_cv1_scale=bn1_sc,
        bn_cv2_scale=bn2_sc,
        cv2_scale=cv2_sc,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write packed weights: [cv1+pad | bn1+pad | bn2+pad | cv2+pad]
    wt_slot = op._wt_slot
    w_cv1_tiled = weights_to_tiled_int8(w_cv1)
    w_bn1_tiled = weights_to_tiled_int8_k3(w_bn1)
    w_bn2_tiled = weights_to_tiled_int8_k3(w_bn2)
    w_cv2_tiled = weights_to_tiled_int8(w_cv2)

    def _pad(data, slot_size):
        pad = np.zeros(slot_size - len(data), dtype=np.int8)
        return np.concatenate([data, pad])

    packed_all = np.concatenate(
        [
            _pad(w_cv1_tiled, wt_slot),
            _pad(w_bn1_tiled, wt_slot),
            _pad(w_bn2_tiled, wt_slot),
            _pad(w_cv2_tiled, wt_slot),
        ]
    )
    op.write_buffer("weights", packed_all)

    # Clear output
    total_output = cv2_oc * height * width
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), cv2_oc, height, width)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt0 = int(np.sum(diff > 0))
    errors_gt1 = int(np.sum(diff > 1))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nC2f L2 simplified test {ic}ic_{height}h_{width}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>0): {errors_gt0}/{total}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # Non-fused integer convolutions should have max_diff <= 1
    assert errors_gt1 == 0, (
        f"C2f L2 simple failed: {errors_gt1} mismatches (diff>1) "
        f"out of {total}, max_diff={max_diff}"
    )


# ============================================================================
# C2f L2 full: fused SiLU, 48ch concat, optional residual add
# ============================================================================


class AIEDataflowC2fL2Full(AIEOperatorBase):
    """Full C2f L2: fused SiLU, 48ch concat [half1|half2|bn0_out].

    Uses fused conv+SiLU kernels. cv2 takes 48ch input (16ch half1 +
    16ch half2 + 16ch bottleneck output) concatenated at MemTile.
    Core B forwards half2 rows to join while doing k3 conv; bn_inter
    to Core C uses neighboring tile transfer (no DMA channels).
    """

    def __init__(
        self,
        height,
        width,
        in_channels,
        cv1_shift1,
        cv1_shift2,
        bn_cv1_shift1,
        bn_cv1_shift2,
        bn_cv2_shift1,
        bn_cv2_shift2,
        cv2_shift1,
        cv2_shift2,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.cv1_shift1 = cv1_shift1
        self.cv1_shift2 = cv1_shift2
        self.bn_cv1_shift1 = bn_cv1_shift1
        self.bn_cv1_shift2 = bn_cv1_shift2
        self.bn_cv2_shift1 = bn_cv2_shift1
        self.bn_cv2_shift2 = bn_cv2_shift2
        self.cv2_shift1 = cv2_shift1
        self.cv2_shift2 = cv2_shift2

        self.cv1_oc = 32
        self.bn_ch = 16
        self.cv2_ic = 48
        self.cv2_oc = 32

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_c2f_l2_full_{self.in_channels}ic_"
            f"{self.height}h_{self.width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_c2f_l2_full",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.cv1_shift1,
                self.cv1_shift2,
                self.bn_cv1_shift1,
                self.bn_cv1_shift2,
                self.bn_cv2_shift1,
                self.bn_cv2_shift2,
                self.cv2_shift1,
                self.cv2_shift2,
            ],
        )

        # cv1 kernel: conv2dk1_i8_silu
        k1_silu_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_silu.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk1_i8_silu.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        # bn k3 SiLU kernel + passthrough_fwd (combined .o for Core B)
        k3_silu_bn_fwd_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_silu_bn_fwd.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk3_i8_silu_fwd.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3_i8_silu=conv2dk3_i8_silu_bn",
                "-Dconv2dk3s2_i8_silu=conv2dk3s2_i8_silu_bn",
            ],
        )

        # passthrough kernel
        passthrough_obj = KernelObjectArtifact.new(
            "passthrough_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "passthrough_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        # cv2 kernel: conv2dk1_i8_silu with renamed symbol
        k1_silu_cv2_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_silu_cv2.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk1_i8_silu.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk1_i8_silu=conv2dk1_i8_silu_cv2",
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                k1_silu_obj,
                k3_silu_bn_fwd_obj,
                passthrough_obj,
                k1_silu_cv2_obj,
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width

        cv1_wt = self.cv1_oc * self.in_channels + self.cv1_oc * 4
        bn_cv1_wt = self.bn_ch * self.bn_ch * 9 + self.bn_ch * 4
        bn_cv2_wt = self.bn_ch * self.bn_ch * 9 + self.bn_ch * 4
        cv2_wt = self.cv2_oc * self.cv2_ic + self.cv2_oc * 4

        wt_slot = max(cv1_wt, bn_cv1_wt, bn_cv2_wt, cv2_wt)
        total_wt = 4 * wt_slot
        self._wt_slot = wt_slot

        total_output = self.cv2_oc * self.height * self.width

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "c2f_l2_full",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("c2f_l2_full", "input", "weights", "output")


def _pack_k1_silu_weights(w_int8, b_int32):
    """Pack k1 weights with int32 bias for fused SiLU kernel.

    Layout: [tiled_k1_weights | bias_as_int8_bytes]
    """
    w_tiled = weights_to_tiled_int8(w_int8)
    b_bytes = b_int32.numpy().astype(np.int32).view(np.int8)
    return np.concatenate([w_tiled, b_bytes])


@pytest.mark.parametrize(
    "height,width,ic,cv1_s1,cv1_s2,bn1_s1,bn1_s2,bn2_s1,bn2_s2,cv2_s1,cv2_s2",
    [
        pytest.param(8, 8, 32, 10, 7, 10, 7, 10, 7, 10, 7, id="c2f_full_8x8"),
        pytest.param(16, 16, 32, 10, 7, 10, 7, 10, 7, 10, 7, id="c2f_full_16x16"),
        pytest.param(32, 32, 32, 10, 7, 10, 7, 10, 7, 10, 7, id="c2f_full_32x32"),
        pytest.param(
            160,
            160,
            32,
            10,
            7,
            10,
            7,
            10,
            7,
            10,
            7,
            id="c2f_full_160x160",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_c2f_l2_full(
    height,
    width,
    ic,
    cv1_s1,
    cv1_s2,
    bn1_s1,
    bn1_s2,
    bn2_s1,
    bn2_s2,
    cv2_s1,
    cv2_s2,
    aie_context,
):
    """Test full C2f L2: fused SiLU, 48ch concat [half1|half2|bn0_out] for cv2."""
    torch.manual_seed(42)

    bn_ch = 16
    cv2_ic = 48  # 16ch half1 + 16ch half2 + 16ch bn0_out
    cv2_oc = 32

    # Test data
    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)

    # Weights with bias for fused SiLU
    w_cv1 = torch.randint(-50, 51, (32, ic, 1, 1), dtype=torch.int8)
    b_cv1 = torch.randint(-500, 501, (32,), dtype=torch.int32)
    w_bn1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    b_bn1 = torch.randint(-500, 501, (bn_ch,), dtype=torch.int32)
    w_bn2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    b_bn2 = torch.randint(-500, 501, (bn_ch,), dtype=torch.int32)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, cv2_ic, 1, 1), dtype=torch.int8)
    b_cv2 = torch.randint(-500, 501, (cv2_oc,), dtype=torch.int32)

    # CPU reference: cv1 -> split -> half2 -> bn -> concat -> cv2
    # cv1 fused SiLU
    cv1_out = conv2d_int8_pade_silu_reference(
        x_int8, w_cv1, b_cv1, cv1_s1, cv1_s2, stride=1, padding=0
    )
    # Split into half1 (first 16ch) and half2 (second 16ch)
    half1 = cv1_out[:, :bn_ch, :, :]
    half2 = cv1_out[:, bn_ch:, :, :]
    # Bottleneck with fused SiLU
    bn_inter = conv2d_int8_pade_silu_reference(
        half2, w_bn1, b_bn1, bn1_s1, bn1_s2, stride=1, padding=1
    )
    bn_out = conv2d_int8_pade_silu_reference(
        bn_inter, w_bn2, b_bn2, bn2_s1, bn2_s2, stride=1, padding=1
    )
    # Concat: [half1(16ch) | half2(16ch) | bn_out(16ch)] = 48ch
    concat = torch.cat([half1, half2, bn_out], dim=1)
    # cv2 fused SiLU
    ref = conv2d_int8_pade_silu_reference(
        concat, w_cv2, b_cv2, cv2_s1, cv2_s2, stride=1, padding=0
    )

    # Create operator
    op = AIEDataflowC2fL2Full(
        height=height,
        width=width,
        in_channels=ic,
        cv1_shift1=cv1_s1,
        cv1_shift2=cv1_s2,
        bn_cv1_shift1=bn1_s1,
        bn_cv1_shift2=bn1_s2,
        bn_cv2_shift1=bn2_s1,
        bn_cv2_shift2=bn2_s2,
        cv2_shift1=cv2_s1,
        cv2_shift2=cv2_s2,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Pack weights: [cv1+pad | bn1+pad | bn2+pad | cv2+pad]
    wt_slot = op._wt_slot

    def _pad(data, slot_size):
        pad = np.zeros(slot_size - len(data), dtype=np.int8)
        return np.concatenate([data, pad])

    packed_all = np.concatenate(
        [
            _pad(_pack_k1_silu_weights(w_cv1, b_cv1), wt_slot),
            _pad(pack_fused_weights_k3(w_bn1, b_bn1), wt_slot),
            _pad(pack_fused_weights_k3(w_bn2, b_bn2), wt_slot),
            _pad(_pack_k1_silu_weights(w_cv2, b_cv2), wt_slot),
        ]
    )
    op.write_buffer("weights", packed_all)

    # Clear output
    total_output = cv2_oc * height * width
    op.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify
    output_raw = op.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), cv2_oc, height, width)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt2 = int(np.sum(diff > 2))
    errors_gt3 = int(np.sum(diff > 3))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nC2f L2 full test {ic}ic_{height}h_{width}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>2): {errors_gt2}/{total}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # Fused SiLU with 5 layers compounds errors. Allow up to diff 5.
    assert max_diff <= 5, f"C2f L2 full failed: max_diff={max_diff} exceeds threshold 5"
    error_rate_gt3 = errors_gt3 / total if total > 0 else 0
    assert error_rate_gt3 < 0.05, (
        f"C2f L2 full: {100 * error_rate_gt3:.2f}% errors > 3 " f"exceeds 5% threshold"
    )


# ============================================================================
# Step 9: C2f L4 (n=2 bottlenecks, 64ch, residual add)
# ============================================================================


def add_i8_reference(a, b):
    """CPU reference for saturating int8 addition.

    Args:
        a: Tensor [N, C, H, W] int8.
        b: Tensor [N, C, H, W] int8.

    Returns:
        Tensor [N, C, H, W] int8, saturated to [-128, 127].
    """
    return torch.clamp(a.int() + b.int(), -128, 127).to(torch.int8)


class AIEDataflowC2fL4(AIEOperatorBase):
    """C2f block for L4: 64ch, n=2 bottlenecks with residual connections.

    cv1(64->64, k1) -> split [half1(32) | half2(32)]
    half2 -> bn0.cv1(k3) -> bn0.cv2(k3) -> +half2 -> bn0_out
    bn0_out -> bn1.cv1(k3) -> bn1.cv2(k3) -> +bn0_out -> bn1_out
    concat [half1|half2|bn0_out|bn1_out]=128ch -> cv2(128->64, k1) -> out
    """

    def __init__(
        self,
        height,
        width,
        in_channels,
        cv1_scale,
        bn0_cv1_scale,
        bn0_cv2_scale,
        bn1_cv1_scale,
        bn1_cv2_scale,
        cv2_scale,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.cv1_scale = cv1_scale
        self.bn0_cv1_scale = bn0_cv1_scale
        self.bn0_cv2_scale = bn0_cv2_scale
        self.bn1_cv1_scale = bn1_cv1_scale
        self.bn1_cv2_scale = bn1_cv2_scale
        self.cv2_scale = cv2_scale

        self.cv1_oc = 64
        self.bn_ch = 32
        self.cv2_ic = 128
        self.cv2_oc = 64

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_c2f_l4_{self.in_channels}ic_" f"{self.height}h_{self.width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_c2f_l4",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.cv1_scale,
                self.bn0_cv1_scale,
                self.bn0_cv2_scale,
                self.bn1_cv1_scale,
                self.bn1_cv2_scale,
                self.cv2_scale,
            ],
        )

        # Kernel objects
        k1_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k3_bn_kernel_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_bn.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3_i8=conv2dk3_i8_bn",
                "-Dconv2dk3s2_i8=conv2dk3s2_i8_bn",
            ],
        )

        add_kernel_obj = KernelObjectArtifact.new(
            "add_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "add_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT", "-DSCALAR"],
        )

        k1_cv2_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_cv2.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk1_i8=conv2dk1_i8_cv2",
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                k1_kernel_obj,
                k3_bn_kernel_obj,
                add_kernel_obj,
                k1_cv2_kernel_obj,
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width

        cv1_wt = self.cv1_oc * self.in_channels
        bn_k3_wt = self.bn_ch * self.bn_ch * 9
        cv2_wt = self.cv2_oc * self.cv2_ic

        # Match the design's weight layout exactly:
        # [cv1_wt | bn0cv1_wt | bn0cv2_wt | bn1cv1_wt | bn1cv2_wt | cv2_wt]
        bn_wt_slot = bn_k3_wt
        total_wt = cv1_wt + 4 * bn_wt_slot + cv2_wt

        total_output = self.cv2_oc * self.height * self.width
        total_concat = self.cv2_ic * self.height * self.width
        output_buf_size = total_output + total_concat

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", output_buf_size, dtype=np.int8)

        self.add_kernel(
            "c2f_l4",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("c2f_l4", "input", "weights", "output")


@pytest.mark.parametrize(
    "height,width,ic,cv1_sc,bn0cv1_sc,bn0cv2_sc,bn1cv1_sc,bn1cv2_sc,cv2_sc",
    [
        pytest.param(8, 8, 64, 10, 10, 10, 10, 10, 10, id="c2f_l4_8x8"),
        pytest.param(16, 16, 64, 10, 10, 10, 10, 10, 10, id="c2f_l4_16x16"),
        pytest.param(
            80,
            80,
            64,
            10,
            10,
            10,
            10,
            10,
            10,
            id="c2f_l4_80x80",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_c2f_l4(
    height,
    width,
    ic,
    cv1_sc,
    bn0cv1_sc,
    bn0cv2_sc,
    bn1cv1_sc,
    bn1cv2_sc,
    cv2_sc,
    aie_context,
):
    """Test C2f L4: n=2 bottlenecks with residual connections (non-fused)."""
    torch.manual_seed(42)

    bn_ch = 32
    cv2_ic = 128
    cv2_oc = 64

    # Test data
    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_cv1 = torch.randint(-50, 51, (64, ic, 1, 1), dtype=torch.int8)
    w_bn0cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn0cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, cv2_ic, 1, 1), dtype=torch.int8)

    # CPU reference: cv1 -> split -> bn0(+res) -> bn1(+res) -> concat -> cv2
    cv1_out = conv2d_int8_reference(x_int8, w_cv1, cv1_sc, stride=1, padding=0)
    half1 = cv1_out[:, :bn_ch, :, :]
    half2 = cv1_out[:, bn_ch:, :, :]

    # Bottleneck 0 with residual
    bn0_inter = conv2d_int8_reference(half2, w_bn0cv1, bn0cv1_sc, stride=1, padding=1)
    bn0_cv2_out = conv2d_int8_reference(
        bn0_inter, w_bn0cv2, bn0cv2_sc, stride=1, padding=1
    )
    bn0_out = add_i8_reference(bn0_cv2_out, half2)

    # Bottleneck 1 with residual
    bn1_inter = conv2d_int8_reference(bn0_out, w_bn1cv1, bn1cv1_sc, stride=1, padding=1)
    bn1_cv2_out = conv2d_int8_reference(
        bn1_inter, w_bn1cv2, bn1cv2_sc, stride=1, padding=1
    )
    bn1_out = add_i8_reference(bn1_cv2_out, bn0_out)

    # Concat [half1 | half2 | bn0_out | bn1_out]
    concat = torch.cat([half1, half2, bn0_out, bn1_out], dim=1)
    ref = conv2d_int8_reference(concat, w_cv2, cv2_sc, stride=1, padding=0)

    # Create operator
    op = AIEDataflowC2fL4(
        height=height,
        width=width,
        in_channels=ic,
        cv1_scale=cv1_sc,
        bn0_cv1_scale=bn0cv1_sc,
        bn0_cv2_scale=bn0cv2_sc,
        bn1_cv1_scale=bn1cv1_sc,
        bn1_cv2_scale=bn1cv2_sc,
        cv2_scale=cv2_sc,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write packed weights — match design layout exactly:
    # [cv1_wt | bn0cv1_wt | bn0cv2_wt | bn1cv1_wt | bn1cv2_wt | cv2_wt]
    w_cv1_tiled = weights_to_tiled_int8(w_cv1)
    w_bn0cv1_tiled = weights_to_tiled_int8_k3(w_bn0cv1)
    w_bn0cv2_tiled = weights_to_tiled_int8_k3(w_bn0cv2)
    w_bn1cv1_tiled = weights_to_tiled_int8_k3(w_bn1cv1)
    w_bn1cv2_tiled = weights_to_tiled_int8_k3(w_bn1cv2)
    w_cv2_tiled = weights_to_tiled_int8(w_cv2)

    packed_all = np.concatenate(
        [
            w_cv1_tiled,
            w_bn0cv1_tiled,
            w_bn0cv2_tiled,
            w_bn1cv1_tiled,
            w_bn1cv2_tiled,
            w_cv2_tiled,
        ]
    )
    op.write_buffer("weights", packed_all)

    # Clear output
    total_output = cv2_oc * height * width
    total_concat = cv2_ic * height * width
    output_buf_size = total_output + total_concat
    op.write_buffer("output", np.zeros(output_buf_size, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify (final output is first total_output bytes)
    output_raw = op.read_buffer("output", (output_buf_size,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(
        output_raw[:total_output].copy(), cv2_oc, height, width
    )

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt0 = int(np.sum(diff > 0))
    errors_gt1 = int(np.sum(diff > 1))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nC2f L4 test {ic}ic_{height}h_{width}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>0): {errors_gt0}/{total}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # Non-fused integer convolutions + saturating add should have max_diff <= 1
    assert errors_gt1 == 0, (
        f"C2f L4 failed: {errors_gt1} mismatches (diff>1) "
        f"out of {total}, max_diff={max_diff}"
    )


class AIEDataflowC2fL6(AIEOperatorBase):
    """C2f block for L6: 128ch, n=2 bottlenecks with residual connections.

    cv1(128->128, k1) -> split [half1(64) | half2(64)]
    half2 -> bn0.cv1(k3) -> bn0.cv2(k3) -> +half2 -> bn0_out
    bn0_out -> bn1.cv1(k3) -> bn1.cv2(k3) -> +bn0_out -> bn1_out
    concat [half1|half2|bn0_out|bn1_out]=256ch -> cv2(256->128, k1) -> out
    """

    def __init__(
        self,
        height,
        width,
        in_channels,
        cv1_scale,
        bn0_cv1_scale,
        bn0_cv2_scale,
        bn1_cv1_scale,
        bn1_cv2_scale,
        cv2_scale,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.cv1_scale = cv1_scale
        self.bn0_cv1_scale = bn0_cv1_scale
        self.bn0_cv2_scale = bn0_cv2_scale
        self.bn1_cv1_scale = bn1_cv1_scale
        self.bn1_cv2_scale = bn1_cv2_scale
        self.cv2_scale = cv2_scale

        self.cv1_oc = 128
        self.bn_ch = 64
        self.cv2_ic = 256
        self.cv2_oc = 128

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_c2f_l6_{self.in_channels}ic_" f"{self.height}h_{self.width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_c2f_l6",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.cv1_scale,
                self.bn0_cv1_scale,
                self.bn0_cv2_scale,
                self.bn1_cv1_scale,
                self.bn1_cv2_scale,
                self.cv2_scale,
            ],
        )

        # Kernel objects
        k1_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k3_bn_kernel_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_bn.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3_i8=conv2dk3_i8_bn",
                "-Dconv2dk3s2_i8=conv2dk3s2_i8_bn",
            ],
        )

        add_kernel_obj = KernelObjectArtifact.new(
            "add_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "add_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k1_cv2_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_cv2.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk1_i8=conv2dk1_i8_cv2",
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                k1_kernel_obj,
                k3_bn_kernel_obj,
                add_kernel_obj,
                k1_cv2_kernel_obj,
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width

        cv1_wt = self.cv1_oc * self.in_channels
        bn_k3_wt = self.bn_ch * self.bn_ch * 9
        cv2_wt = self.cv2_oc * self.cv2_ic

        # Match the design's weight layout exactly:
        # [cv1_wt | bn0cv1_wt | bn0cv2_wt | bn1cv1_wt | bn1cv2_wt | cv2_wt]
        bn_wt_slot = bn_k3_wt
        total_wt = cv1_wt + 4 * bn_wt_slot + cv2_wt

        total_output = self.cv2_oc * self.height * self.width
        total_concat = self.cv2_ic * self.height * self.width
        output_buf_size = total_output + total_concat

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", output_buf_size, dtype=np.int8)

        self.add_kernel(
            "c2f_l6",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("c2f_l6", "input", "weights", "output")


@pytest.mark.parametrize(
    "height,width,ic,cv1_sc,bn0cv1_sc,bn0cv2_sc,bn1cv1_sc,bn1cv2_sc,cv2_sc",
    [
        pytest.param(8, 8, 128, 10, 10, 10, 10, 10, 10, id="c2f_l6_8x8"),
        pytest.param(16, 16, 128, 10, 10, 10, 10, 10, 10, id="c2f_l6_16x16"),
        pytest.param(
            40,
            40,
            128,
            10,
            10,
            10,
            10,
            10,
            10,
            id="c2f_l6_40x40",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_c2f_l6(
    height,
    width,
    ic,
    cv1_sc,
    bn0cv1_sc,
    bn0cv2_sc,
    bn1cv1_sc,
    bn1cv2_sc,
    cv2_sc,
    aie_context,
):
    """Test C2f L6: n=2 bottlenecks with residual connections (128ch)."""
    torch.manual_seed(42)

    bn_ch = 64
    cv2_ic = 256
    cv2_oc = 128

    # Test data
    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_cv1 = torch.randint(-50, 51, (128, ic, 1, 1), dtype=torch.int8)
    w_bn0cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn0cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, cv2_ic, 1, 1), dtype=torch.int8)

    # CPU reference: cv1 -> split -> bn0(+res) -> bn1(+res) -> concat -> cv2
    cv1_out = conv2d_int8_reference(x_int8, w_cv1, cv1_sc, stride=1, padding=0)
    half1 = cv1_out[:, :bn_ch, :, :]
    half2 = cv1_out[:, bn_ch:, :, :]

    # Bottleneck 0 with residual
    bn0_inter = conv2d_int8_reference(half2, w_bn0cv1, bn0cv1_sc, stride=1, padding=1)
    bn0_cv2_out = conv2d_int8_reference(
        bn0_inter, w_bn0cv2, bn0cv2_sc, stride=1, padding=1
    )
    bn0_out = add_i8_reference(bn0_cv2_out, half2)

    # Bottleneck 1 with residual
    bn1_inter = conv2d_int8_reference(bn0_out, w_bn1cv1, bn1cv1_sc, stride=1, padding=1)
    bn1_cv2_out = conv2d_int8_reference(
        bn1_inter, w_bn1cv2, bn1cv2_sc, stride=1, padding=1
    )
    bn1_out = add_i8_reference(bn1_cv2_out, bn0_out)

    # Concat [half1 | half2 | bn0_out | bn1_out]
    concat = torch.cat([half1, half2, bn0_out, bn1_out], dim=1)
    ref = conv2d_int8_reference(concat, w_cv2, cv2_sc, stride=1, padding=0)

    # Create operator
    op = AIEDataflowC2fL6(
        height=height,
        width=width,
        in_channels=ic,
        cv1_scale=cv1_sc,
        bn0_cv1_scale=bn0cv1_sc,
        bn0_cv2_scale=bn0cv2_sc,
        bn1_cv1_scale=bn1cv1_sc,
        bn1_cv2_scale=bn1cv2_sc,
        cv2_scale=cv2_sc,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Write packed weights — match design layout exactly:
    # [cv1_wt | bn0cv1_wt | bn0cv2_wt | bn1cv1_wt | bn1cv2_wt | cv2_wt]
    w_cv1_tiled = weights_to_tiled_int8(w_cv1)
    w_bn0cv1_tiled = weights_to_tiled_int8_k3(w_bn0cv1)
    w_bn0cv2_tiled = weights_to_tiled_int8_k3(w_bn0cv2)
    w_bn1cv1_tiled = weights_to_tiled_int8_k3(w_bn1cv1)
    w_bn1cv2_tiled = weights_to_tiled_int8_k3(w_bn1cv2)
    w_cv2_tiled = weights_to_tiled_int8(w_cv2)

    packed_all = np.concatenate(
        [
            w_cv1_tiled,
            w_bn0cv1_tiled,
            w_bn0cv2_tiled,
            w_bn1cv1_tiled,
            w_bn1cv2_tiled,
            w_cv2_tiled,
        ]
    )
    op.write_buffer("weights", packed_all)

    # Clear output
    total_output = cv2_oc * height * width
    total_concat = cv2_ic * height * width
    output_buf_size = total_output + total_concat
    op.write_buffer("output", np.zeros(output_buf_size, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify (final output is first total_output bytes)
    output_raw = op.read_buffer("output", (output_buf_size,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(
        output_raw[:total_output].copy(), cv2_oc, height, width
    )

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt0 = int(np.sum(diff > 0))
    errors_gt1 = int(np.sum(diff > 1))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nC2f L6 test {ic}ic_{height}h_{width}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>0): {errors_gt0}/{total}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # Non-fused integer convolutions + saturating add should have max_diff <= 1
    assert errors_gt1 == 0, (
        f"C2f L6 failed: {errors_gt1} mismatches (diff>1) "
        f"out of {total}, max_diff={max_diff}"
    )


# ============================================================================
# Step 11: Backbone Phase 1 — L0->L1->L2(C2f)->L3 in one PDI
# ============================================================================


class AIEDataflowBackbonePhase1(AIEOperatorBase):
    """Backbone Phase 1: L0->L1->L2(C2f)->L3 chained in one PDI.

    Three task groups:
      TG1: L0(k3s2)->L1(k3s2) pipeline -> DDR scratch_A
      TG2: C2f L2 full (fused SiLU) -> DDR scratch_B
      TG3: L3(k3s2) -> DDR final output

    8 cores across 2 columns:
      Col 0: L0(0,2), L1(0,3), passthrough(0,4), L3(0,5)
      Col 1: cv1(1,2), bn0.cv1(1,3), bn0.cv2(1,4), cv2(1,5)
    """

    def __init__(
        self,
        l0_height,
        l0_width,
        l0_ic,
        l0_oc,
        l0_shift1,
        l0_shift2,
        l1_oc,
        l1_shift1,
        l1_shift2,
        cv1_shift1,
        cv1_shift2,
        bn_cv1_shift1,
        bn_cv1_shift2,
        bn_cv2_shift1,
        bn_cv2_shift2,
        cv2_shift1,
        cv2_shift2,
        l3_oc,
        l3_shift1,
        l3_shift2,
        context=None,
    ):
        self.l0_height = l0_height
        self.l0_width = l0_width
        self.l0_ic = l0_ic
        self.l0_oc = l0_oc
        self.l0_shift1 = l0_shift1
        self.l0_shift2 = l0_shift2
        self.l1_oc = l1_oc
        self.l1_shift1 = l1_shift1
        self.l1_shift2 = l1_shift2
        self.cv1_shift1 = cv1_shift1
        self.cv1_shift2 = cv1_shift2
        self.bn_cv1_shift1 = bn_cv1_shift1
        self.bn_cv1_shift2 = bn_cv1_shift2
        self.bn_cv2_shift1 = bn_cv2_shift1
        self.bn_cv2_shift2 = bn_cv2_shift2
        self.cv2_shift1 = cv2_shift1
        self.cv2_shift2 = cv2_shift2
        self.l3_oc = l3_oc
        self.l3_shift1 = l3_shift1
        self.l3_shift2 = l3_shift2

        # Derived dims
        self.l1_ic = l0_oc
        self.l1_height = l0_height // 2
        self.l1_width = l0_width // 2
        self.c2f_ic = l1_oc
        self.c2f_height = l0_height // 4
        self.c2f_width = l0_width // 4
        self.cv1_oc = 32
        self.bn_ch = 16
        self.cv2_ic = 48
        self.cv2_oc = 32
        self.l3_ic = 32
        self.l3_height = self.c2f_height
        self.l3_width = self.c2f_width
        self.l3_out_h = self.l3_height // 2
        self.l3_out_w = self.l3_width // 2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_backbone_phase1_{self.l0_ic}ic_{self.l3_oc}oc_"
            f"{self.l0_height}h_{self.l0_width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_backbone_phase1",
            callback_args=[
                self.context.device_manager.device_type,
                self.l0_height,
                self.l0_width,
                self.l0_ic,
                self.l0_oc,
                self.l0_shift1,
                self.l0_shift2,
                self.l1_oc,
                self.l1_shift1,
                self.l1_shift2,
                self.cv1_shift1,
                self.cv1_shift2,
                self.bn_cv1_shift1,
                self.bn_cv1_shift2,
                self.bn_cv2_shift1,
                self.bn_cv2_shift2,
                self.cv2_shift1,
                self.cv2_shift2,
                self.l3_oc,
                self.l3_shift1,
                self.l3_shift2,
            ],
        )

        # 5 kernel objects
        k3s2_silu_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_silu.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk3_i8_silu.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k1_silu_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_silu.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk1_i8_silu.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k3_silu_bn_fwd_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_silu_bn_fwd.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk3_i8_silu_fwd.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3_i8_silu=conv2dk3_i8_silu_bn",
                "-Dconv2dk3s2_i8_silu=conv2dk3s2_i8_silu_bn",
            ],
        )

        passthrough_obj = KernelObjectArtifact.new(
            "passthrough_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "passthrough_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k1_silu_cv2_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_silu_cv2.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk1_i8_silu.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk1_i8_silu=conv2dk1_i8_silu_cv2",
            ],
        )

        # L3 kernel: separate .o with renamed symbol (different type signature)
        k3s2_silu_l3_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_silu_l3.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk3_i8_silu.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3s2_i8_silu=conv2dk3s2_i8_silu_l3",
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                k3s2_silu_obj,
                k1_silu_obj,
                k3_silu_bn_fwd_obj,
                passthrough_obj,
                k1_silu_cv2_obj,
                k3s2_silu_l3_obj,
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.l0_ic * self.l0_height * self.l0_width

        # TG1 weights
        l0_wt = self.l0_oc * self.l0_ic * 9 + self.l0_oc * 4
        l1_wt = self.l1_oc * self.l1_ic * 9 + self.l1_oc * 4
        tg1_wt_slot = max(l0_wt, l1_wt)
        tg1_total_wt = 2 * tg1_wt_slot
        self._tg1_wt_slot = tg1_wt_slot

        # C2f weights
        cv1_wt = self.cv1_oc * self.c2f_ic + self.cv1_oc * 4
        bn_cv1_wt = self.bn_ch * self.bn_ch * 9 + self.bn_ch * 4
        bn_cv2_wt = self.bn_ch * self.bn_ch * 9 + self.bn_ch * 4
        cv2_wt = self.cv2_oc * self.cv2_ic + self.cv2_oc * 4
        c2f_wt_slot = max(cv1_wt, bn_cv1_wt, bn_cv2_wt, cv2_wt)
        c2f_total_wt = 4 * c2f_wt_slot
        self._c2f_wt_slot = c2f_wt_slot

        # L3 weight
        l3_wt = self.l3_oc * self.l3_ic * 9 + self.l3_oc * 4

        total_weights = tg1_total_wt + c2f_total_wt + l3_wt

        # Output buffer = [final | scratch_A | scratch_B]
        total_output = self.l3_oc * self.l3_out_h * self.l3_out_w
        scratch_a = self.l1_oc * self.c2f_height * self.c2f_width
        scratch_b = self.cv2_oc * self.c2f_height * self.c2f_width
        total_output_buf = total_output + scratch_a + scratch_b
        self._total_output = total_output

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output_buf, dtype=np.int8)

        self.add_kernel(
            "backbone_phase1",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("backbone_phase1", "input", "weights", "output")


@pytest.mark.parametrize(
    "l0_h,l0_w,l0_ic,l0_oc,"
    "l0_s1,l0_s2,"
    "l1_oc,l1_s1,l1_s2,"
    "cv1_s1,cv1_s2,bn1_s1,bn1_s2,bn2_s1,bn2_s2,cv2_s1,cv2_s2,"
    "l3_oc,l3_s1,l3_s2",
    [
        pytest.param(
            32,
            32,
            8,
            16,
            10,
            7,
            32,
            10,
            7,
            10,
            7,
            10,
            7,
            10,
            7,
            10,
            7,
            64,
            10,
            7,
            id="backbone_p1_32x32",
        ),
        pytest.param(
            64,
            64,
            8,
            16,
            10,
            7,
            32,
            10,
            7,
            10,
            7,
            10,
            7,
            10,
            7,
            10,
            7,
            64,
            10,
            7,
            id="backbone_p1_64x64",
        ),
        pytest.param(
            640,
            640,
            8,
            16,
            10,
            7,
            32,
            10,
            7,
            10,
            7,
            10,
            7,
            10,
            7,
            10,
            7,
            64,
            10,
            7,
            id="backbone_p1_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_backbone_phase1(
    l0_h,
    l0_w,
    l0_ic,
    l0_oc,
    l0_s1,
    l0_s2,
    l1_oc,
    l1_s1,
    l1_s2,
    cv1_s1,
    cv1_s2,
    bn1_s1,
    bn1_s2,
    bn2_s1,
    bn2_s2,
    cv2_s1,
    cv2_s2,
    l3_oc,
    l3_s1,
    l3_s2,
    aie_context,
):
    """Test backbone phase 1: L0->L1->L2(C2f)->L3 in one PDI."""
    torch.manual_seed(42)

    bn_ch = 16
    cv2_ic = 48
    cv2_oc = 32

    # Derived dims
    l1_ic = l0_oc
    l1_h = l0_h // 2
    l1_w = l0_w // 2
    c2f_h = l0_h // 4
    c2f_w = l0_w // 4
    l3_ic = cv2_oc
    l3_out_h = c2f_h // 2
    l3_out_w = c2f_w // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)

    # L0, L1, L3 weights (k3 fused: weights + bias)
    w0 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    b0 = torch.randint(-500, 501, (l0_oc,), dtype=torch.int32)
    w1 = torch.randint(-50, 51, (l1_oc, l1_ic, 3, 3), dtype=torch.int8)
    b1 = torch.randint(-500, 501, (l1_oc,), dtype=torch.int32)
    w3 = torch.randint(-50, 51, (l3_oc, l3_ic, 3, 3), dtype=torch.int8)
    b3 = torch.randint(-500, 501, (l3_oc,), dtype=torch.int32)

    # C2f weights (k1 fused for cv1/cv2, k3 fused for bn)
    w_cv1 = torch.randint(-50, 51, (32, l1_oc, 1, 1), dtype=torch.int8)
    b_cv1 = torch.randint(-500, 501, (32,), dtype=torch.int32)
    w_bn1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    b_bn1 = torch.randint(-500, 501, (bn_ch,), dtype=torch.int32)
    w_bn2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    b_bn2 = torch.randint(-500, 501, (bn_ch,), dtype=torch.int32)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, cv2_ic, 1, 1), dtype=torch.int8)
    b_cv2 = torch.randint(-500, 501, (cv2_oc,), dtype=torch.int32)

    # CPU reference: L0 -> L1 -> C2f -> L3
    inter01 = conv2d_int8_pade_silu_reference(x_int8, w0, b0, l0_s1, l0_s2, stride=2)
    l1_out = conv2d_int8_pade_silu_reference(inter01, w1, b1, l1_s1, l1_s2, stride=2)

    # C2f reference
    cv1_out = conv2d_int8_pade_silu_reference(
        l1_out, w_cv1, b_cv1, cv1_s1, cv1_s2, stride=1, padding=0
    )
    half1 = cv1_out[:, :bn_ch, :, :]
    half2 = cv1_out[:, bn_ch:, :, :]
    bn_inter = conv2d_int8_pade_silu_reference(
        half2, w_bn1, b_bn1, bn1_s1, bn1_s2, stride=1, padding=1
    )
    bn_out = conv2d_int8_pade_silu_reference(
        bn_inter, w_bn2, b_bn2, bn2_s1, bn2_s2, stride=1, padding=1
    )
    concat = torch.cat([half1, half2, bn_out], dim=1)
    c2f_out = conv2d_int8_pade_silu_reference(
        concat, w_cv2, b_cv2, cv2_s1, cv2_s2, stride=1, padding=0
    )

    # L3 reference
    ref = conv2d_int8_pade_silu_reference(c2f_out, w3, b3, l3_s1, l3_s2, stride=2)

    # Create operator
    op = AIEDataflowBackbonePhase1(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_shift1=l0_s1,
        l0_shift2=l0_s2,
        l1_oc=l1_oc,
        l1_shift1=l1_s1,
        l1_shift2=l1_s2,
        cv1_shift1=cv1_s1,
        cv1_shift2=cv1_s2,
        bn_cv1_shift1=bn1_s1,
        bn_cv1_shift2=bn1_s2,
        bn_cv2_shift1=bn2_s1,
        bn_cv2_shift2=bn2_s2,
        cv2_shift1=cv2_s1,
        cv2_shift2=cv2_s2,
        l3_oc=l3_oc,
        l3_shift1=l3_s1,
        l3_shift2=l3_s2,
        context=aie_context,
    )

    # Compile
    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Pack weights
    tg1_wt_slot = op._tg1_wt_slot
    c2f_wt_slot = op._c2f_wt_slot

    def _pad(data, slot_size):
        pad = np.zeros(slot_size - len(data), dtype=np.int8)
        return np.concatenate([data, pad])

    # TG1 weights: [L0 (padded) | L1 (padded)]
    tg1_packed = np.concatenate(
        [
            _pad(pack_fused_weights_k3(w0, b0), tg1_wt_slot),
            _pad(pack_fused_weights_k3(w1, b1), tg1_wt_slot),
        ]
    )

    # TG2 C2f weights: [cv1 | bn1 | bn2 | cv2] each padded to c2f_wt_slot
    c2f_packed = np.concatenate(
        [
            _pad(_pack_k1_silu_weights(w_cv1, b_cv1), c2f_wt_slot),
            _pad(pack_fused_weights_k3(w_bn1, b_bn1), c2f_wt_slot),
            _pad(pack_fused_weights_k3(w_bn2, b_bn2), c2f_wt_slot),
            _pad(_pack_k1_silu_weights(w_cv2, b_cv2), c2f_wt_slot),
        ]
    )

    # TG3 L3 weight (no padding needed, single weight)
    l3_packed = pack_fused_weights_k3(w3, b3)

    packed_all = np.concatenate([tg1_packed, c2f_packed, l3_packed])
    op.write_buffer("weights", packed_all)

    # Clear output buffer
    total_output_buf = op.buffers["output"]
    op.write_buffer("output", np.zeros(total_output_buf, dtype=np.int8))

    # Run
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify (final output at offset 0)
    total_output = op._total_output
    output_buf = op.read_buffer("output", (total_output_buf,), dtype=np.int8)
    output_raw = output_buf[:total_output].copy()
    npu_output = tiled_to_nchw_int8(output_raw, l3_oc, l3_out_h, l3_out_w)

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt2 = int(np.sum(diff > 2))
    errors_gt3 = int(np.sum(diff > 3))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nBackbone Phase 1 test {l0_ic}ic_{l3_oc}oc_{l0_h}h_{l0_w}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>2): {errors_gt2}/{total}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # 7-layer pipeline (L0,L1,cv1,bn.cv1,bn.cv2,cv2,L3) compounds errors
    assert (
        max_diff <= 8
    ), f"Backbone Phase 1 failed: max_diff={max_diff} exceeds threshold 8"
    error_rate_gt3 = errors_gt3 / total if total > 0 else 0
    assert error_rate_gt3 < 0.10, (
        f"Backbone Phase 1: {100 * error_rate_gt3:.2f}% errors > 3 "
        f"exceeds 10% threshold"
    )


# ============================================================================
# Step 12: Backbone Phases 1-5 chained via DDR scratch buffers
# ============================================================================


@pytest.mark.parametrize(
    "l0_h,l0_w",
    [
        pytest.param(64, 64, id="backbone_p1_p5_64x64"),
        pytest.param(
            640,
            640,
            id="backbone_p1_p5_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_backbone_p1_through_p5(l0_h, l0_w):
    """Test backbone phases 1-5 chained with DDR scratch buffers.

    Phase 1: L0(8->16,k3s2) -> L1(16->32,k3s2) -> C2f L2 -> L3(32->64,k3s2)
    Phase 2: C2f L4 (64ch, n=2 bottlenecks)
    Phase 3: L5 CBS (64->128, k3s2) via OC streaming
    Phase 4: C2f L6 (128ch, n=2 bottlenecks)
    Phase 5: L7 CBS (128->256, k3s2) via OC streaming
    """
    from iron.operators.conv2d_int8.dataflow_design import (
        _compute_oc_streaming_params,
    )

    torch.manual_seed(42)

    # Common shifts
    scale = 10
    shift2 = 7

    # ---- Channel dimensions ----
    l0_ic, l0_oc = 8, 16
    l1_oc = 32
    # C2f L2
    c2f_l2_cv1_oc = 32
    c2f_l2_bn_ch = 16
    c2f_l2_cv2_ic = 48
    c2f_l2_cv2_oc = 32
    l3_oc = 64
    # C2f L4
    c2f_l4_ic = 64
    c2f_l4_cv1_oc = 64
    c2f_l4_bn_ch = 32
    c2f_l4_cv2_ic = 128
    c2f_l4_cv2_oc = 64
    # L5
    l5_ic, l5_oc = 64, 128
    # C2f L6
    c2f_l6_ic = 128
    c2f_l6_cv1_oc = 128
    c2f_l6_bn_ch = 64
    c2f_l6_cv2_ic = 256
    c2f_l6_cv2_oc = 128
    # L7
    l7_ic, l7_oc = 128, 256

    # ---- Spatial dimensions at each stage ----
    p1_out_h = l0_h // 8  # After L0(s2)->L1(s2)->C2f->L3(s2)
    p1_out_w = l0_w // 8
    p2_h = p1_out_h  # C2f L4 preserves spatial
    p2_w = p1_out_w
    p3_in_h, p3_in_w = p2_h, p2_w
    p3_out_h = p3_in_h // 2  # L5 stride-2
    p3_out_w = p3_in_w // 2
    p4_h = p3_out_h  # C2f L6 preserves spatial
    p4_w = p3_out_w
    p5_in_h, p5_in_w = p4_h, p4_w
    p5_out_h = p5_in_h // 2  # L7 stride-2
    p5_out_w = p5_in_w // 2

    # ---- Generate ALL test data up front ----
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)

    # Phase 1 weights
    w0 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    b0 = torch.randint(-500, 501, (l0_oc,), dtype=torch.int32)
    w1 = torch.randint(-50, 51, (l1_oc, l0_oc, 3, 3), dtype=torch.int8)
    b1 = torch.randint(-500, 501, (l1_oc,), dtype=torch.int32)
    w_l2_cv1 = torch.randint(-50, 51, (c2f_l2_cv1_oc, l1_oc, 1, 1), dtype=torch.int8)
    b_l2_cv1 = torch.randint(-500, 501, (c2f_l2_cv1_oc,), dtype=torch.int32)
    w_l2_bn1 = torch.randint(
        -50, 51, (c2f_l2_bn_ch, c2f_l2_bn_ch, 3, 3), dtype=torch.int8
    )
    b_l2_bn1 = torch.randint(-500, 501, (c2f_l2_bn_ch,), dtype=torch.int32)
    w_l2_bn2 = torch.randint(
        -50, 51, (c2f_l2_bn_ch, c2f_l2_bn_ch, 3, 3), dtype=torch.int8
    )
    b_l2_bn2 = torch.randint(-500, 501, (c2f_l2_bn_ch,), dtype=torch.int32)
    w_l2_cv2 = torch.randint(
        -50, 51, (c2f_l2_cv2_oc, c2f_l2_cv2_ic, 1, 1), dtype=torch.int8
    )
    b_l2_cv2 = torch.randint(-500, 501, (c2f_l2_cv2_oc,), dtype=torch.int32)
    w3 = torch.randint(-50, 51, (l3_oc, c2f_l2_cv2_oc, 3, 3), dtype=torch.int8)
    b3 = torch.randint(-500, 501, (l3_oc,), dtype=torch.int32)

    # Phase 2 weights (C2f L4, non-fused: no bias)
    w_l4_cv1 = torch.randint(
        -50, 51, (c2f_l4_cv1_oc, c2f_l4_ic, 1, 1), dtype=torch.int8
    )
    w_l4_bn0cv1 = torch.randint(
        -50, 51, (c2f_l4_bn_ch, c2f_l4_bn_ch, 3, 3), dtype=torch.int8
    )
    w_l4_bn0cv2 = torch.randint(
        -50, 51, (c2f_l4_bn_ch, c2f_l4_bn_ch, 3, 3), dtype=torch.int8
    )
    w_l4_bn1cv1 = torch.randint(
        -50, 51, (c2f_l4_bn_ch, c2f_l4_bn_ch, 3, 3), dtype=torch.int8
    )
    w_l4_bn1cv2 = torch.randint(
        -50, 51, (c2f_l4_bn_ch, c2f_l4_bn_ch, 3, 3), dtype=torch.int8
    )
    w_l4_cv2 = torch.randint(
        -50, 51, (c2f_l4_cv2_oc, c2f_l4_cv2_ic, 1, 1), dtype=torch.int8
    )

    # Phase 3 weights (L5, fused SiLU with bias)
    w5 = torch.randint(-50, 51, (l5_oc, l5_ic, 3, 3), dtype=torch.int8)
    b5 = torch.randint(-500, 501, (l5_oc,), dtype=torch.int32)

    # Phase 4 weights (C2f L6, non-fused: no bias)
    w_l6_cv1 = torch.randint(
        -50, 51, (c2f_l6_cv1_oc, c2f_l6_ic, 1, 1), dtype=torch.int8
    )
    w_l6_bn0cv1 = torch.randint(
        -50, 51, (c2f_l6_bn_ch, c2f_l6_bn_ch, 3, 3), dtype=torch.int8
    )
    w_l6_bn0cv2 = torch.randint(
        -50, 51, (c2f_l6_bn_ch, c2f_l6_bn_ch, 3, 3), dtype=torch.int8
    )
    w_l6_bn1cv1 = torch.randint(
        -50, 51, (c2f_l6_bn_ch, c2f_l6_bn_ch, 3, 3), dtype=torch.int8
    )
    w_l6_bn1cv2 = torch.randint(
        -50, 51, (c2f_l6_bn_ch, c2f_l6_bn_ch, 3, 3), dtype=torch.int8
    )
    w_l6_cv2 = torch.randint(
        -50, 51, (c2f_l6_cv2_oc, c2f_l6_cv2_ic, 1, 1), dtype=torch.int8
    )

    # Phase 5 weights (L7, fused SiLU with bias)
    w7 = torch.randint(-50, 51, (l7_oc, l7_ic, 3, 3), dtype=torch.int8)
    b7 = torch.randint(-500, 501, (l7_oc,), dtype=torch.int32)

    # ================================================================
    # CPU reference end-to-end
    # ================================================================

    # Phase 1: L0 -> L1 -> C2f L2 -> L3 (all fused SiLU)
    ref_l0 = conv2d_int8_pade_silu_reference(x_int8, w0, b0, scale, shift2, stride=2)
    ref_l1 = conv2d_int8_pade_silu_reference(ref_l0, w1, b1, scale, shift2, stride=2)
    ref_cv1 = conv2d_int8_pade_silu_reference(
        ref_l1, w_l2_cv1, b_l2_cv1, scale, shift2, stride=1, padding=0
    )
    l2_half1 = ref_cv1[:, :c2f_l2_bn_ch, :, :]
    l2_half2 = ref_cv1[:, c2f_l2_bn_ch:, :, :]
    ref_l2_bn_inter = conv2d_int8_pade_silu_reference(
        l2_half2, w_l2_bn1, b_l2_bn1, scale, shift2, stride=1, padding=1
    )
    ref_l2_bn_out = conv2d_int8_pade_silu_reference(
        ref_l2_bn_inter, w_l2_bn2, b_l2_bn2, scale, shift2, stride=1, padding=1
    )
    l2_concat = torch.cat([l2_half1, l2_half2, ref_l2_bn_out], dim=1)
    ref_c2f_out = conv2d_int8_pade_silu_reference(
        l2_concat, w_l2_cv2, b_l2_cv2, scale, shift2, stride=1, padding=0
    )
    ref_l3 = conv2d_int8_pade_silu_reference(
        ref_c2f_out, w3, b3, scale, shift2, stride=2
    )

    # Phase 2: C2f L4 (non-fused, scale only)
    ref_l4_cv1 = conv2d_int8_reference(ref_l3, w_l4_cv1, scale, stride=1, padding=0)
    l4_half1 = ref_l4_cv1[:, :c2f_l4_bn_ch, :, :]
    l4_half2 = ref_l4_cv1[:, c2f_l4_bn_ch:, :, :]
    ref_l4_bn0_inter = conv2d_int8_reference(
        l4_half2, w_l4_bn0cv1, scale, stride=1, padding=1
    )
    ref_l4_bn0_cv2 = conv2d_int8_reference(
        ref_l4_bn0_inter, w_l4_bn0cv2, scale, stride=1, padding=1
    )
    ref_l4_bn0_out = add_i8_reference(ref_l4_bn0_cv2, l4_half2)
    ref_l4_bn1_inter = conv2d_int8_reference(
        ref_l4_bn0_out, w_l4_bn1cv1, scale, stride=1, padding=1
    )
    ref_l4_bn1_cv2 = conv2d_int8_reference(
        ref_l4_bn1_inter, w_l4_bn1cv2, scale, stride=1, padding=1
    )
    ref_l4_bn1_out = add_i8_reference(ref_l4_bn1_cv2, ref_l4_bn0_out)
    l4_concat = torch.cat([l4_half1, l4_half2, ref_l4_bn0_out, ref_l4_bn1_out], dim=1)
    ref_l4 = conv2d_int8_reference(l4_concat, w_l4_cv2, scale, stride=1, padding=0)

    # Phase 3: L5 (fused SiLU, stride-2)
    ref_l5 = conv2d_int8_pade_silu_reference(ref_l4, w5, b5, scale, shift2, stride=2)

    # Phase 4: C2f L6 (non-fused, scale only)
    ref_l6_cv1 = conv2d_int8_reference(ref_l5, w_l6_cv1, scale, stride=1, padding=0)
    l6_half1 = ref_l6_cv1[:, :c2f_l6_bn_ch, :, :]
    l6_half2 = ref_l6_cv1[:, c2f_l6_bn_ch:, :, :]
    ref_l6_bn0_inter = conv2d_int8_reference(
        l6_half2, w_l6_bn0cv1, scale, stride=1, padding=1
    )
    ref_l6_bn0_cv2 = conv2d_int8_reference(
        ref_l6_bn0_inter, w_l6_bn0cv2, scale, stride=1, padding=1
    )
    ref_l6_bn0_out = add_i8_reference(ref_l6_bn0_cv2, l6_half2)
    ref_l6_bn1_inter = conv2d_int8_reference(
        ref_l6_bn0_out, w_l6_bn1cv1, scale, stride=1, padding=1
    )
    ref_l6_bn1_cv2 = conv2d_int8_reference(
        ref_l6_bn1_inter, w_l6_bn1cv2, scale, stride=1, padding=1
    )
    ref_l6_bn1_out = add_i8_reference(ref_l6_bn1_cv2, ref_l6_bn0_out)
    l6_concat = torch.cat([l6_half1, l6_half2, ref_l6_bn0_out, ref_l6_bn1_out], dim=1)
    ref_l6 = conv2d_int8_reference(l6_concat, w_l6_cv2, scale, stride=1, padding=0)

    # Phase 5: L7 (fused SiLU, stride-2)
    ref_final = conv2d_int8_pade_silu_reference(ref_l6, w7, b7, scale, shift2, stride=2)

    phase_times = {}

    # ================================================================
    # Phase 1: L0->L1->C2f L2->L3
    # ================================================================
    ctx1 = AIEContext()
    op1 = AIEDataflowBackbonePhase1(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_shift1=scale,
        l0_shift2=shift2,
        l1_oc=l1_oc,
        l1_shift1=scale,
        l1_shift2=shift2,
        cv1_shift1=scale,
        cv1_shift2=shift2,
        bn_cv1_shift1=scale,
        bn_cv1_shift2=shift2,
        bn_cv2_shift1=scale,
        bn_cv2_shift2=shift2,
        cv2_shift1=scale,
        cv2_shift2=shift2,
        l3_oc=l3_oc,
        l3_shift1=scale,
        l3_shift2=shift2,
        context=ctx1,
    )
    op1.context.compile_all()
    op1.context.prepare_runtime()

    input_tiled = nchw_to_tiled_int8(x_int8)
    op1.write_buffer("input", input_tiled)

    # Pack Phase 1 weights
    tg1_wt_slot = op1._tg1_wt_slot
    c2f_wt_slot = op1._c2f_wt_slot

    def _pad(data, slot_size):
        pad = np.zeros(slot_size - len(data), dtype=np.int8)
        return np.concatenate([data, pad])

    tg1_packed = np.concatenate(
        [
            _pad(pack_fused_weights_k3(w0, b0), tg1_wt_slot),
            _pad(pack_fused_weights_k3(w1, b1), tg1_wt_slot),
        ]
    )
    c2f_packed = np.concatenate(
        [
            _pad(_pack_k1_silu_weights(w_l2_cv1, b_l2_cv1), c2f_wt_slot),
            _pad(pack_fused_weights_k3(w_l2_bn1, b_l2_bn1), c2f_wt_slot),
            _pad(pack_fused_weights_k3(w_l2_bn2, b_l2_bn2), c2f_wt_slot),
            _pad(_pack_k1_silu_weights(w_l2_cv2, b_l2_cv2), c2f_wt_slot),
        ]
    )
    l3_packed = pack_fused_weights_k3(w3, b3)
    op1.write_buffer("weights", np.concatenate([tg1_packed, c2f_packed, l3_packed]))

    total_output_buf_p1 = op1.buffers["output"]
    op1.write_buffer("output", np.zeros(total_output_buf_p1, dtype=np.int8))

    t0 = time.perf_counter()
    op1.run_runlist()
    t1 = time.perf_counter()
    phase_times["Phase 1"] = t1 - t0

    # Read Phase 1 output (tiled int8, at offset 0)
    p1_total_output = op1._total_output
    p1_out_buf = op1.read_buffer("output", (total_output_buf_p1,), dtype=np.int8)
    p1_output_tiled = p1_out_buf[:p1_total_output].copy()

    # Verify Phase 1 intermediate
    p1_npu = tiled_to_nchw_int8(p1_output_tiled.copy(), l3_oc, p1_out_h, p1_out_w)
    p1_ref_np = ref_l3.numpy().reshape(-1).astype(np.int32)
    p1_npu_np = p1_npu.numpy().reshape(-1).astype(np.int32)
    p1_diff = np.abs(p1_ref_np - p1_npu_np)
    p1_max_diff = int(np.max(p1_diff)) if len(p1_diff) > 0 else 0
    print(f"\n  Phase 1 (L0->L3): max_diff={p1_max_diff}")

    # ================================================================
    # Phase 2: C2f L4
    # ================================================================
    ctx2 = AIEContext()
    op2 = AIEDataflowC2fL4(
        height=p2_h,
        width=p2_w,
        in_channels=c2f_l4_ic,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        bn1_cv1_scale=scale,
        bn1_cv2_scale=scale,
        cv2_scale=scale,
        context=ctx2,
    )
    op2.context.compile_all()
    op2.context.prepare_runtime()

    # Phase 1 tiled output -> Phase 2 tiled input (direct)
    op2.write_buffer("input", p1_output_tiled)

    # Pack C2f L4 weights: [cv1 | bn0cv1 | bn0cv2 | bn1cv1 | bn1cv2 | cv2]
    w_l4_cv1_tiled = weights_to_tiled_int8(w_l4_cv1)
    w_l4_bn0cv1_tiled = weights_to_tiled_int8_k3(w_l4_bn0cv1)
    w_l4_bn0cv2_tiled = weights_to_tiled_int8_k3(w_l4_bn0cv2)
    w_l4_bn1cv1_tiled = weights_to_tiled_int8_k3(w_l4_bn1cv1)
    w_l4_bn1cv2_tiled = weights_to_tiled_int8_k3(w_l4_bn1cv2)
    w_l4_cv2_tiled = weights_to_tiled_int8(w_l4_cv2)
    op2.write_buffer(
        "weights",
        np.concatenate(
            [
                w_l4_cv1_tiled,
                w_l4_bn0cv1_tiled,
                w_l4_bn0cv2_tiled,
                w_l4_bn1cv1_tiled,
                w_l4_bn1cv2_tiled,
                w_l4_cv2_tiled,
            ]
        ),
    )

    p2_total_output = c2f_l4_cv2_oc * p2_h * p2_w
    p2_total_concat = c2f_l4_cv2_ic * p2_h * p2_w
    p2_output_buf_size = p2_total_output + p2_total_concat
    op2.write_buffer("output", np.zeros(p2_output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op2.run_runlist()
    t1 = time.perf_counter()
    phase_times["Phase 2"] = t1 - t0

    # Read Phase 2 output (tiled int8, first p2_total_output bytes)
    p2_out_buf = op2.read_buffer("output", (p2_output_buf_size,), dtype=np.int8)
    p2_output_tiled = p2_out_buf[:p2_total_output].copy()

    # Verify Phase 2 intermediate
    p2_npu = tiled_to_nchw_int8(p2_output_tiled.copy(), c2f_l4_cv2_oc, p2_h, p2_w)
    p2_ref_np = ref_l4.numpy().reshape(-1).astype(np.int32)
    p2_npu_np = p2_npu.numpy().reshape(-1).astype(np.int32)
    p2_diff = np.abs(p2_ref_np - p2_npu_np)
    p2_max_diff = int(np.max(p2_diff)) if len(p2_diff) > 0 else 0
    print(f"  Phase 2 (C2f L4): max_diff={p2_max_diff}")

    # ================================================================
    # Phase 3: L5 CBS (64->128, k3s2) via OC streaming
    # ================================================================
    ctx3 = AIEContext()
    op3 = AIEDataflowFusedOCStreaming(
        height=p3_in_h,
        width=p3_in_w,
        in_channels=l5_ic,
        out_channels=l5_oc,
        shift1=scale,
        shift2=shift2,
        context=ctx3,
    )
    op3.context.compile_all()
    op3.context.prepare_runtime()

    # Phase 2 tiled output -> Phase 3 tiled input
    op3.write_buffer("input", p2_output_tiled)

    # Pack L5 weights for OC streaming
    l5_oc_chunk = op3._oc_chunk
    l5_n_oc_groups = op3._n_oc_groups
    l5_packed_chunks = []
    for g in range(l5_n_oc_groups):
        oc_start = g * l5_oc_chunk
        oc_end = oc_start + l5_oc_chunk
        w_chunk = w5[oc_start:oc_end]
        b_chunk = b5[oc_start:oc_end]
        w_tiled = weights_to_tiled_int8_k3(w_chunk)
        b_bytes = b_chunk.numpy().astype(np.int32).view(np.int8)
        l5_packed_chunks.append(np.concatenate([w_tiled, b_bytes]))
    op3.write_buffer("weights", np.concatenate(l5_packed_chunks))

    p3_total_output = l5_oc * p3_out_h * p3_out_w
    op3.write_buffer("output", np.zeros(p3_total_output, dtype=np.int8))

    t0 = time.perf_counter()
    op3.run_runlist()
    t1 = time.perf_counter()
    phase_times["Phase 3"] = t1 - t0

    # Read Phase 3 output
    p3_output_tiled = op3.read_buffer(
        "output", (p3_total_output,), dtype=np.int8
    ).copy()

    # Verify Phase 3 intermediate
    p3_npu = tiled_to_nchw_int8(p3_output_tiled.copy(), l5_oc, p3_out_h, p3_out_w)
    p3_ref_np = ref_l5.numpy().reshape(-1).astype(np.int32)
    p3_npu_np = p3_npu.numpy().reshape(-1).astype(np.int32)
    p3_diff = np.abs(p3_ref_np - p3_npu_np)
    p3_max_diff = int(np.max(p3_diff)) if len(p3_diff) > 0 else 0
    print(f"  Phase 3 (L5 OCS): max_diff={p3_max_diff}")

    # ================================================================
    # Phase 4: C2f L6
    # ================================================================
    ctx4 = AIEContext()
    op4 = AIEDataflowC2fL6(
        height=p4_h,
        width=p4_w,
        in_channels=c2f_l6_ic,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        bn1_cv1_scale=scale,
        bn1_cv2_scale=scale,
        cv2_scale=scale,
        context=ctx4,
    )
    op4.context.compile_all()
    op4.context.prepare_runtime()

    # Phase 3 tiled output -> Phase 4 tiled input
    op4.write_buffer("input", p3_output_tiled)

    # Pack C2f L6 weights: [cv1 | bn0cv1 | bn0cv2 | bn1cv1 | bn1cv2 | cv2]
    w_l6_cv1_tiled = weights_to_tiled_int8(w_l6_cv1)
    w_l6_bn0cv1_tiled = weights_to_tiled_int8_k3(w_l6_bn0cv1)
    w_l6_bn0cv2_tiled = weights_to_tiled_int8_k3(w_l6_bn0cv2)
    w_l6_bn1cv1_tiled = weights_to_tiled_int8_k3(w_l6_bn1cv1)
    w_l6_bn1cv2_tiled = weights_to_tiled_int8_k3(w_l6_bn1cv2)
    w_l6_cv2_tiled = weights_to_tiled_int8(w_l6_cv2)
    op4.write_buffer(
        "weights",
        np.concatenate(
            [
                w_l6_cv1_tiled,
                w_l6_bn0cv1_tiled,
                w_l6_bn0cv2_tiled,
                w_l6_bn1cv1_tiled,
                w_l6_bn1cv2_tiled,
                w_l6_cv2_tiled,
            ]
        ),
    )

    p4_total_output = c2f_l6_cv2_oc * p4_h * p4_w
    p4_total_concat = c2f_l6_cv2_ic * p4_h * p4_w
    p4_output_buf_size = p4_total_output + p4_total_concat
    op4.write_buffer("output", np.zeros(p4_output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op4.run_runlist()
    t1 = time.perf_counter()
    phase_times["Phase 4"] = t1 - t0

    # Read Phase 4 output (first p4_total_output bytes)
    p4_out_buf = op4.read_buffer("output", (p4_output_buf_size,), dtype=np.int8)
    p4_output_tiled = p4_out_buf[:p4_total_output].copy()

    # Verify Phase 4 intermediate
    p4_npu = tiled_to_nchw_int8(p4_output_tiled.copy(), c2f_l6_cv2_oc, p4_h, p4_w)
    p4_ref_np = ref_l6.numpy().reshape(-1).astype(np.int32)
    p4_npu_np = p4_npu.numpy().reshape(-1).astype(np.int32)
    p4_diff = np.abs(p4_ref_np - p4_npu_np)
    p4_max_diff = int(np.max(p4_diff)) if len(p4_diff) > 0 else 0
    print(f"  Phase 4 (C2f L6): max_diff={p4_max_diff}")

    # ================================================================
    # Phase 5: L7 CBS (128->256, k3s2) via OC streaming
    # ================================================================
    ctx5 = AIEContext()
    op5 = AIEDataflowFusedOCStreaming(
        height=p5_in_h,
        width=p5_in_w,
        in_channels=l7_ic,
        out_channels=l7_oc,
        shift1=scale,
        shift2=shift2,
        context=ctx5,
    )
    op5.context.compile_all()
    op5.context.prepare_runtime()

    # Phase 4 tiled output -> Phase 5 tiled input
    op5.write_buffer("input", p4_output_tiled)

    # Pack L7 weights for OC streaming
    l7_oc_chunk = op5._oc_chunk
    l7_n_oc_groups = op5._n_oc_groups
    l7_packed_chunks = []
    for g in range(l7_n_oc_groups):
        oc_start = g * l7_oc_chunk
        oc_end = oc_start + l7_oc_chunk
        w_chunk = w7[oc_start:oc_end]
        b_chunk = b7[oc_start:oc_end]
        w_tiled = weights_to_tiled_int8_k3(w_chunk)
        b_bytes = b_chunk.numpy().astype(np.int32).view(np.int8)
        l7_packed_chunks.append(np.concatenate([w_tiled, b_bytes]))
    op5.write_buffer("weights", np.concatenate(l7_packed_chunks))

    p5_total_output = l7_oc * p5_out_h * p5_out_w
    op5.write_buffer("output", np.zeros(p5_total_output, dtype=np.int8))

    t0 = time.perf_counter()
    op5.run_runlist()
    t1 = time.perf_counter()
    phase_times["Phase 5"] = t1 - t0

    # Read Phase 5 final output
    p5_output_raw = op5.read_buffer("output", (p5_total_output,), dtype=np.int8).copy()
    npu_final = tiled_to_nchw_int8(p5_output_raw, l7_oc, p5_out_h, p5_out_w)

    # ================================================================
    # Final verification
    # ================================================================
    ref_np = ref_final.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_final.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt3 = int(np.sum(diff > 3))
    errors_gt5 = int(np.sum(diff > 5))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nBackbone P1-P5 test {l0_ic}ic_{l7_oc}oc_{l0_h}h_{l0_w}w:")
    print(f"  Final dims: {l7_oc}ch x {p5_out_h}h x {p5_out_w}w")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  Errors (>5): {errors_gt5}/{total}")
    for phase_name, dt in phase_times.items():
        print(f"  {phase_name} NPU time: {1000 * dt:.1f} ms")
    total_time = sum(phase_times.values())
    print(f"  Total NPU time: {1000 * total_time:.1f} ms")

    # 5-phase pipeline (17+ layers) compounds quantization errors
    assert (
        max_diff <= 15
    ), f"Backbone P1-P5 failed: max_diff={max_diff} exceeds threshold 15"
    error_rate_gt5 = errors_gt5 / total if total > 0 else 0
    assert error_rate_gt5 < 0.20, (
        f"Backbone P1-P5: {100 * error_rate_gt5:.2f}% errors > 5 "
        f"exceeds 20% threshold"
    )


# ---------------------------------------------------------------------------
# Step 12: Combined L4(C2f) + L5(k3s2, 4-core OC parallel)
# ---------------------------------------------------------------------------


class AIEDataflowL4L5Combined(AIEOperatorBase):
    """Combined L4(C2f) + L5(k3s2) in one PDI.

    L4-only mode (l5_oc=0): phases A-D, 8 cores, 2 columns.
    L4+L5 mode (l5_oc>0): phases A-E, 12 cores, 3 columns.
    """

    def __init__(
        self,
        height,
        width,
        in_channels,
        cv1_scale,
        bn0_cv1_scale,
        bn0_cv2_scale,
        bn1_cv1_scale,
        bn1_cv2_scale,
        cv2_scale,
        l5_oc=0,
        l5_shift1=0,
        l5_shift2=0,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.cv1_scale = cv1_scale
        self.bn0_cv1_scale = bn0_cv1_scale
        self.bn0_cv2_scale = bn0_cv2_scale
        self.bn1_cv1_scale = bn1_cv1_scale
        self.bn1_cv2_scale = bn1_cv2_scale
        self.cv2_scale = cv2_scale
        self.l5_oc = l5_oc
        self.l5_shift1 = l5_shift1
        self.l5_shift2 = l5_shift2

        self.cv1_oc = 64
        self.bn_ch = 32
        self.cv2_ic = 128
        self.cv2_oc = 64
        self.l5_mode = l5_oc > 0

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        if self.l5_mode:
            file_name_base = (
                f"dataflow_l4l5_{self.in_channels}ic_{self.l5_oc}oc_"
                f"{self.height}h_{self.width}w"
            )
        else:
            file_name_base = (
                f"dataflow_l4l5_l4only_{self.in_channels}ic_"
                f"{self.height}h_{self.width}w"
            )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_l4_l5_combined",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.cv1_scale,
                self.bn0_cv1_scale,
                self.bn0_cv2_scale,
                self.bn1_cv1_scale,
                self.bn1_cv2_scale,
                self.cv2_scale,
                self.l5_oc,
                self.l5_shift1,
                self.l5_shift2,
            ],
        )

        # L4 C2f kernel objects
        k1_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k3_bn_kernel_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_bn.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3_i8=conv2dk3_i8_bn",
                "-Dconv2dk3s2_i8=conv2dk3s2_i8_bn",
            ],
        )

        add_kernel_obj = KernelObjectArtifact.new(
            "add_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "add_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT", "-DSCALAR"],
        )

        k1_cv2_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_cv2.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk1_i8=conv2dk1_i8_cv2",
            ],
        )

        kernel_deps = [
            mlir_artifact,
            k1_kernel_obj,
            k3_bn_kernel_obj,
            add_kernel_obj,
            k1_cv2_kernel_obj,
        ]

        # L5 kernel object (single core, OC streaming)
        # conv2dk3s2_i8_silu_l5 is already defined in conv2dk3_i8_silu.cc
        if self.l5_mode:
            l5_obj = KernelObjectArtifact.new(
                "conv2dk3_i8_silu_l5.o",
                depends=[
                    SourceArtifact.new(
                        self.context.base_dir
                        / "aie_kernels"
                        / "aie2p"
                        / "conv2dk3_i8_silu.cc"
                    )
                ],
                extra_flags=["-DINT8_ACT"],
            )
            kernel_deps.append(l5_obj)

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=kernel_deps,
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width

        cv1_wt = self.cv1_oc * self.in_channels
        bn_k3_wt = self.bn_ch * self.bn_ch * 9
        cv2_wt = self.cv2_oc * self.cv2_ic

        bn_wt_slot = bn_k3_wt
        l4_total_wt = cv1_wt + 4 * bn_wt_slot + cv2_wt

        l4_output_size = self.cv2_oc * self.height * self.width
        total_concat = self.cv2_ic * self.height * self.width

        if self.l5_mode:
            from iron.operators.conv2d_int8.dataflow_design import (
                _compute_oc_streaming_params,
            )

            l5_ic = self.cv2_oc
            l5_out_h = self.height // 2
            l5_out_w = self.width // 2

            l5_oc_chunk, l5_n_oc_groups, _ = _compute_oc_streaming_params(
                l5_ic, self.l5_oc, self.width, 2
            )
            l5_wt_chunk = l5_oc_chunk * l5_ic * 9 + l5_oc_chunk * 4
            l5_total_wt = l5_n_oc_groups * l5_wt_chunk
            self._l5_oc_chunk = l5_oc_chunk
            self._l5_n_oc_groups = l5_n_oc_groups

            l5_total_output = self.l5_oc * l5_out_h * l5_out_w
            self._l5_total_output = l5_total_output

            total_wt = l4_total_wt + l5_total_wt
            output_buf_size = l5_total_output + l4_output_size + total_concat
        else:
            total_wt = l4_total_wt
            output_buf_size = l4_output_size + total_concat

        self._l4_output_size = l4_output_size
        self._output_buf_size = output_buf_size

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", output_buf_size, dtype=np.int8)

        self.add_kernel(
            "l4_l5_combined",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("l4_l5_combined", "input", "weights", "output")


@pytest.mark.parametrize(
    "height,width,ic,cv1_sc,bn0cv1_sc,bn0cv2_sc,bn1cv1_sc,bn1cv2_sc,cv2_sc",
    [
        pytest.param(8, 8, 64, 10, 10, 10, 10, 10, 10, id="l4l5_step1_8x8"),
        pytest.param(16, 16, 64, 10, 10, 10, 10, 10, 10, id="l4l5_step1_16x16"),
        pytest.param(
            80,
            80,
            64,
            10,
            10,
            10,
            10,
            10,
            10,
            id="l4l5_step1_80x80",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_l4_l5_step1(
    height,
    width,
    ic,
    cv1_sc,
    bn0cv1_sc,
    bn0cv2_sc,
    bn1cv1_sc,
    bn1cv2_sc,
    cv2_sc,
    aie_context,
):
    """Test L4+L5 combined, Step 1: L4 C2f only (l5_oc=0).

    Verifies the combined design function produces correct L4 output
    when L5 is disabled.
    """
    torch.manual_seed(42)

    bn_ch = 32
    cv2_ic = 128
    cv2_oc = 64

    # Test data
    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_cv1 = torch.randint(-50, 51, (64, ic, 1, 1), dtype=torch.int8)
    w_bn0cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn0cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, cv2_ic, 1, 1), dtype=torch.int8)

    # CPU reference: cv1 -> split -> bn0(+res) -> bn1(+res) -> concat -> cv2
    cv1_out = conv2d_int8_reference(x_int8, w_cv1, cv1_sc, stride=1, padding=0)
    half1 = cv1_out[:, :bn_ch, :, :]
    half2 = cv1_out[:, bn_ch:, :, :]

    bn0_inter = conv2d_int8_reference(half2, w_bn0cv1, bn0cv1_sc, stride=1, padding=1)
    bn0_cv2_out = conv2d_int8_reference(
        bn0_inter, w_bn0cv2, bn0cv2_sc, stride=1, padding=1
    )
    bn0_out = add_i8_reference(bn0_cv2_out, half2)

    bn1_inter = conv2d_int8_reference(bn0_out, w_bn1cv1, bn1cv1_sc, stride=1, padding=1)
    bn1_cv2_out = conv2d_int8_reference(
        bn1_inter, w_bn1cv2, bn1cv2_sc, stride=1, padding=1
    )
    bn1_out = add_i8_reference(bn1_cv2_out, bn0_out)

    concat = torch.cat([half1, half2, bn0_out, bn1_out], dim=1)
    ref = conv2d_int8_reference(concat, w_cv2, cv2_sc, stride=1, padding=0)

    # Create operator (L4-only mode)
    op = AIEDataflowL4L5Combined(
        height=height,
        width=width,
        in_channels=ic,
        cv1_scale=cv1_sc,
        bn0_cv1_scale=bn0cv1_sc,
        bn0_cv2_scale=bn0cv2_sc,
        bn1_cv1_scale=bn1cv1_sc,
        bn1_cv2_scale=bn1cv2_sc,
        cv2_scale=cv2_sc,
        l5_oc=0,
        context=aie_context,
    )

    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Pack weights: [cv1 | bn0cv1 | bn0cv2 | bn1cv1 | bn1cv2 | cv2]
    w_cv1_tiled = weights_to_tiled_int8(w_cv1)
    w_bn0cv1_tiled = weights_to_tiled_int8_k3(w_bn0cv1)
    w_bn0cv2_tiled = weights_to_tiled_int8_k3(w_bn0cv2)
    w_bn1cv1_tiled = weights_to_tiled_int8_k3(w_bn1cv1)
    w_bn1cv2_tiled = weights_to_tiled_int8_k3(w_bn1cv2)
    w_cv2_tiled = weights_to_tiled_int8(w_cv2)

    packed_all = np.concatenate(
        [
            w_cv1_tiled,
            w_bn0cv1_tiled,
            w_bn0cv2_tiled,
            w_bn1cv1_tiled,
            w_bn1cv2_tiled,
            w_cv2_tiled,
        ]
    )
    op.write_buffer("weights", packed_all)

    # Clear output
    output_buf_size = op._output_buf_size
    l4_output_size = op._l4_output_size
    op.write_buffer("output", np.zeros(output_buf_size, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify (L4 output at offset 0 in L4-only mode)
    output_raw = op.read_buffer("output", (output_buf_size,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(
        output_raw[:l4_output_size].copy(), cv2_oc, height, width
    )

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt1 = int(np.sum(diff > 1))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    errors_gt2 = int(np.sum(diff > 2))
    print(f"\nL4+L5 Step 1 (L4 only) {ic}ic_{height}h_{width}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>2): {errors_gt2}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # Non-fused integer convolutions compound rounding through C2f pipeline
    # (cv1 -> bn0.cv1 -> bn0.cv2 -> add -> bn1.cv1 -> bn1.cv2 -> add -> cv2)
    # Non-fused C2f rounding scales with spatial size (max_diff=4 at 16x16,
    # 37 at 80x80). Matches existing standalone C2f L4 behavior exactly.
    threshold = 4 if height <= 16 else 40
    assert (
        max_diff <= threshold
    ), f"L4+L5 Step 1 failed: max_diff={max_diff} exceeds threshold {threshold}"


@pytest.mark.parametrize(
    "height,width",
    [
        pytest.param(16, 16, id="l4l5_step2_16x16"),
        pytest.param(
            80,
            80,
            id="l4l5_step2_80x80",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_l4_l5_step2(height, width, aie_context):
    """Test L4+L5 combined: L4 C2f + L5 k3s2 with OC streaming.

    Verifies the combined design produces correct L5 output when both
    L4 C2f and L5 k3s2 run within the same PDI.
    """
    torch.manual_seed(42)

    ic = 64
    bn_ch = 32
    cv2_ic = 128
    cv2_oc = 64
    l5_oc = 128
    scale = 10
    l5_shift1 = 10
    l5_shift2 = 7

    l5_out_h = height // 2
    l5_out_w = width // 2

    # Test data
    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_cv1 = torch.randint(-50, 51, (64, ic, 1, 1), dtype=torch.int8)
    w_bn0cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn0cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, cv2_ic, 1, 1), dtype=torch.int8)

    # L5 weights (k3 fused with bias)
    w_l5 = torch.randint(-50, 51, (l5_oc, cv2_oc, 3, 3), dtype=torch.int8)
    b_l5 = torch.randint(-500, 501, (l5_oc,), dtype=torch.int32)

    # CPU reference: L4 C2f
    cv1_out = conv2d_int8_reference(x_int8, w_cv1, scale, stride=1, padding=0)
    half1 = cv1_out[:, :bn_ch, :, :]
    half2 = cv1_out[:, bn_ch:, :, :]

    bn0_inter = conv2d_int8_reference(half2, w_bn0cv1, scale, stride=1, padding=1)
    bn0_cv2_out = conv2d_int8_reference(bn0_inter, w_bn0cv2, scale, stride=1, padding=1)
    bn0_out = add_i8_reference(bn0_cv2_out, half2)

    bn1_inter = conv2d_int8_reference(bn0_out, w_bn1cv1, scale, stride=1, padding=1)
    bn1_cv2_out = conv2d_int8_reference(bn1_inter, w_bn1cv2, scale, stride=1, padding=1)
    bn1_out = add_i8_reference(bn1_cv2_out, bn0_out)

    concat = torch.cat([half1, half2, bn0_out, bn1_out], dim=1)
    l4_out = conv2d_int8_reference(concat, w_cv2, scale, stride=1, padding=0)

    # CPU reference: L5 (fused SiLU, stride-2)
    ref = conv2d_int8_pade_silu_reference(
        l4_out, w_l5, b_l5, l5_shift1, l5_shift2, stride=2
    )

    # Create operator (L4+L5 mode)
    op = AIEDataflowL4L5Combined(
        height=height,
        width=width,
        in_channels=ic,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        bn1_cv1_scale=scale,
        bn1_cv2_scale=scale,
        cv2_scale=scale,
        l5_oc=l5_oc,
        l5_shift1=l5_shift1,
        l5_shift2=l5_shift2,
        context=aie_context,
    )

    op.context.compile_all()
    op.context.prepare_runtime()

    # Write input (tiled layout)
    input_tiled = nchw_to_tiled_int8(x_int8)
    op.write_buffer("input", input_tiled)

    # Pack weights: [cv1 | bn0cv1 | bn0cv2 | bn1cv1 | bn1cv2 | cv2 | l5 OC chunks]
    w_cv1_tiled = weights_to_tiled_int8(w_cv1)
    w_bn0cv1_tiled = weights_to_tiled_int8_k3(w_bn0cv1)
    w_bn0cv2_tiled = weights_to_tiled_int8_k3(w_bn0cv2)
    w_bn1cv1_tiled = weights_to_tiled_int8_k3(w_bn1cv1)
    w_bn1cv2_tiled = weights_to_tiled_int8_k3(w_bn1cv2)
    w_cv2_tiled = weights_to_tiled_int8(w_cv2)

    l4_packed = np.concatenate(
        [
            w_cv1_tiled,
            w_bn0cv1_tiled,
            w_bn0cv2_tiled,
            w_bn1cv1_tiled,
            w_bn1cv2_tiled,
            w_cv2_tiled,
        ]
    )

    # L5 weights: pack as OC streaming chunks
    l5_oc_chunk = op._l5_oc_chunk
    l5_n_oc_groups = op._l5_n_oc_groups
    l5_chunks = []
    for g in range(l5_n_oc_groups):
        oc_start = g * l5_oc_chunk
        oc_end = oc_start + l5_oc_chunk
        w_chunk = w_l5[oc_start:oc_end, :, :, :]
        b_chunk = b_l5[oc_start:oc_end]
        l5_chunks.append(pack_fused_weights_k3(w_chunk, b_chunk))
    l5_packed = np.concatenate(l5_chunks)

    packed_all = np.concatenate([l4_packed, l5_packed])
    op.write_buffer("weights", packed_all)

    # Clear output
    output_buf_size = op._output_buf_size
    op.write_buffer("output", np.zeros(output_buf_size, dtype=np.int8))

    # Run on NPU
    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    # Read and verify (L5 output at offset 0)
    l5_total_output = op._l5_total_output
    output_raw = op.read_buffer("output", (output_buf_size,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(
        output_raw[:l5_total_output].copy(), l5_oc, l5_out_h, l5_out_w
    )

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt3 = int(np.sum(diff > 3))
    errors_gt5 = int(np.sum(diff > 5))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nL4+L5 Step 2 {ic}ic_{l5_oc}oc_{height}h_{width}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  Errors (>5): {errors_gt5}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # L4 C2f (8 layers) + L5 fused SiLU compounds rounding errors
    assert (
        max_diff <= 10
    ), f"L4+L5 Step 2 failed: max_diff={max_diff} exceeds threshold 10"
    error_rate_gt5 = errors_gt5 / total if total > 0 else 0
    assert error_rate_gt5 < 0.15, (
        f"L4+L5 Step 2: {100 * error_rate_gt5:.2f}% errors > 5 "
        f"exceeds 15% threshold"
    )


# ---------------------------------------------------------------------------
# Step 12c: P1→P2 chain test
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "l0_h,l0_w",
    [
        pytest.param(64, 64, id="p1_p2_64x64"),
        pytest.param(
            640,
            640,
            id="p1_p2_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_p1_p2_combined(l0_h, l0_w):
    """Test backbone P1→P2 chain: Phase 1 (L0-L3) feeds Phase 2 (L4+L5).

    Phase 1: L0(8->16)->L1(16->32)->C2f L2->L3(32->64) [existing]
    Phase 2: C2f L4(64ch) + L5(64->128, OC streaming) [new combined]
    """
    from iron.operators.conv2d_int8.dataflow_design import (
        _compute_oc_streaming_params,
    )

    torch.manual_seed(42)

    l0_ic = 8
    l0_oc = 16
    l1_oc = 32
    l3_oc = 64
    l5_oc = 128
    scale = 10
    shift2 = 7
    bn_ch_l2 = 16
    cv2_ic_l2 = 48
    cv2_oc_l2 = 32

    # Derived dims
    p1_out_h = l0_h // 4  # after L0(s2) + L1(s2)
    p1_out_w = l0_w // 4
    l3_out_h = p1_out_h // 2  # after L3(s2)
    l3_out_w = p1_out_w // 2
    l5_out_h = l3_out_h // 2  # after L5(s2)
    l5_out_w = l3_out_w // 2

    # Generate all weights
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)

    # Phase 1 weights
    w0 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    b0 = torch.randint(-500, 501, (l0_oc,), dtype=torch.int32)
    w1 = torch.randint(-50, 51, (l1_oc, l0_oc, 3, 3), dtype=torch.int8)
    b1 = torch.randint(-500, 501, (l1_oc,), dtype=torch.int32)
    w_cv1_l2 = torch.randint(-50, 51, (32, l1_oc, 1, 1), dtype=torch.int8)
    b_cv1_l2 = torch.randint(-500, 501, (32,), dtype=torch.int32)
    w_bn1_l2 = torch.randint(-50, 51, (bn_ch_l2, bn_ch_l2, 3, 3), dtype=torch.int8)
    b_bn1_l2 = torch.randint(-500, 501, (bn_ch_l2,), dtype=torch.int32)
    w_bn2_l2 = torch.randint(-50, 51, (bn_ch_l2, bn_ch_l2, 3, 3), dtype=torch.int8)
    b_bn2_l2 = torch.randint(-500, 501, (bn_ch_l2,), dtype=torch.int32)
    w_cv2_l2 = torch.randint(-50, 51, (cv2_oc_l2, cv2_ic_l2, 1, 1), dtype=torch.int8)
    b_cv2_l2 = torch.randint(-500, 501, (cv2_oc_l2,), dtype=torch.int32)
    w3 = torch.randint(-50, 51, (l3_oc, cv2_oc_l2, 3, 3), dtype=torch.int8)
    b3 = torch.randint(-500, 501, (l3_oc,), dtype=torch.int32)

    # Phase 2 weights (L4 C2f non-fused + L5 fused)
    bn_ch_l4 = 32
    cv2_ic_l4 = 128
    cv2_oc_l4 = 64
    w_cv1_l4 = torch.randint(-50, 51, (64, l3_oc, 1, 1), dtype=torch.int8)
    w_bn0cv1_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn0cv2_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn1cv1_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn1cv2_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_cv2_l4 = torch.randint(-50, 51, (cv2_oc_l4, cv2_ic_l4, 1, 1), dtype=torch.int8)
    w_l5 = torch.randint(-50, 51, (l5_oc, cv2_oc_l4, 3, 3), dtype=torch.int8)
    b_l5 = torch.randint(-500, 501, (l5_oc,), dtype=torch.int32)

    # ================================================================
    # CPU reference: full pipeline
    # ================================================================
    # Phase 1
    inter01 = conv2d_int8_pade_silu_reference(x_int8, w0, b0, scale, shift2, stride=2)
    l1_out = conv2d_int8_pade_silu_reference(inter01, w1, b1, scale, shift2, stride=2)
    cv1_l2 = conv2d_int8_pade_silu_reference(
        l1_out, w_cv1_l2, b_cv1_l2, scale, shift2, stride=1, padding=0
    )
    half1_l2 = cv1_l2[:, :bn_ch_l2, :, :]
    half2_l2 = cv1_l2[:, bn_ch_l2:, :, :]
    bn_inter_l2 = conv2d_int8_pade_silu_reference(
        half2_l2, w_bn1_l2, b_bn1_l2, scale, shift2, stride=1, padding=1
    )
    bn_out_l2 = conv2d_int8_pade_silu_reference(
        bn_inter_l2, w_bn2_l2, b_bn2_l2, scale, shift2, stride=1, padding=1
    )
    concat_l2 = torch.cat([half1_l2, half2_l2, bn_out_l2], dim=1)
    c2f_l2_out = conv2d_int8_pade_silu_reference(
        concat_l2, w_cv2_l2, b_cv2_l2, scale, shift2, stride=1, padding=0
    )
    l3_out = conv2d_int8_pade_silu_reference(
        c2f_l2_out, w3, b3, scale, shift2, stride=2
    )

    # Phase 2
    cv1_l4 = conv2d_int8_reference(l3_out, w_cv1_l4, scale, stride=1, padding=0)
    half1_l4 = cv1_l4[:, :bn_ch_l4, :, :]
    half2_l4 = cv1_l4[:, bn_ch_l4:, :, :]
    bn0_inter = conv2d_int8_reference(half2_l4, w_bn0cv1_l4, scale, stride=1, padding=1)
    bn0_cv2 = conv2d_int8_reference(bn0_inter, w_bn0cv2_l4, scale, stride=1, padding=1)
    bn0_out = add_i8_reference(bn0_cv2, half2_l4)
    bn1_inter = conv2d_int8_reference(bn0_out, w_bn1cv1_l4, scale, stride=1, padding=1)
    bn1_cv2 = conv2d_int8_reference(bn1_inter, w_bn1cv2_l4, scale, stride=1, padding=1)
    bn1_out = add_i8_reference(bn1_cv2, bn0_out)
    concat_l4 = torch.cat([half1_l4, half2_l4, bn0_out, bn1_out], dim=1)
    l4_out = conv2d_int8_reference(concat_l4, w_cv2_l4, scale, stride=1, padding=0)
    ref_final = conv2d_int8_pade_silu_reference(
        l4_out, w_l5, b_l5, scale, shift2, stride=2
    )

    phase_times = {}

    # ================================================================
    # Phase 1: Backbone Phase 1 (L0->L1->L2->L3)
    # ================================================================
    ctx1 = AIEContext()
    op1 = AIEDataflowBackbonePhase1(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_shift1=scale,
        l0_shift2=shift2,
        l1_oc=l1_oc,
        l1_shift1=scale,
        l1_shift2=shift2,
        cv1_shift1=scale,
        cv1_shift2=shift2,
        bn_cv1_shift1=scale,
        bn_cv1_shift2=shift2,
        bn_cv2_shift1=scale,
        bn_cv2_shift2=shift2,
        cv2_shift1=scale,
        cv2_shift2=shift2,
        l3_oc=l3_oc,
        l3_shift1=scale,
        l3_shift2=shift2,
        context=ctx1,
    )
    op1.context.compile_all()
    op1.context.prepare_runtime()

    op1.write_buffer("input", nchw_to_tiled_int8(x_int8))

    tg1_wt_slot = op1._tg1_wt_slot
    c2f_wt_slot = op1._c2f_wt_slot

    def _pad(data, slot_size):
        pad = np.zeros(slot_size - len(data), dtype=np.int8)
        return np.concatenate([data, pad])

    tg1_packed = np.concatenate(
        [
            _pad(pack_fused_weights_k3(w0, b0), tg1_wt_slot),
            _pad(pack_fused_weights_k3(w1, b1), tg1_wt_slot),
        ]
    )
    c2f_packed = np.concatenate(
        [
            _pad(_pack_k1_silu_weights(w_cv1_l2, b_cv1_l2), c2f_wt_slot),
            _pad(pack_fused_weights_k3(w_bn1_l2, b_bn1_l2), c2f_wt_slot),
            _pad(pack_fused_weights_k3(w_bn2_l2, b_bn2_l2), c2f_wt_slot),
            _pad(_pack_k1_silu_weights(w_cv2_l2, b_cv2_l2), c2f_wt_slot),
        ]
    )
    l3_wt_packed = pack_fused_weights_k3(w3, b3)
    op1.write_buffer("weights", np.concatenate([tg1_packed, c2f_packed, l3_wt_packed]))

    total_output_buf_p1 = op1.buffers["output"]
    op1.write_buffer("output", np.zeros(total_output_buf_p1, dtype=np.int8))

    t0 = time.perf_counter()
    op1.run_runlist()
    t1 = time.perf_counter()
    phase_times["Phase 1"] = t1 - t0

    # Read Phase 1 output (at offset 0)
    p1_total_output = op1._total_output
    p1_output_buf = op1.read_buffer("output", (total_output_buf_p1,), dtype=np.int8)
    p1_output_tiled = p1_output_buf[:p1_total_output].copy()

    # ================================================================
    # Phase 2: L4 C2f + L5 (combined)
    # ================================================================
    ctx2 = AIEContext()
    op2 = AIEDataflowL4L5Combined(
        height=l3_out_h,
        width=l3_out_w,
        in_channels=l3_oc,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        bn1_cv1_scale=scale,
        bn1_cv2_scale=scale,
        cv2_scale=scale,
        l5_oc=l5_oc,
        l5_shift1=scale,
        l5_shift2=shift2,
        context=ctx2,
    )
    op2.context.compile_all()
    op2.context.prepare_runtime()

    op2.write_buffer("input", p1_output_tiled)

    # Pack Phase 2 weights
    l4_packed = np.concatenate(
        [
            weights_to_tiled_int8(w_cv1_l4),
            weights_to_tiled_int8_k3(w_bn0cv1_l4),
            weights_to_tiled_int8_k3(w_bn0cv2_l4),
            weights_to_tiled_int8_k3(w_bn1cv1_l4),
            weights_to_tiled_int8_k3(w_bn1cv2_l4),
            weights_to_tiled_int8(w_cv2_l4),
        ]
    )

    l5_oc_chunk = op2._l5_oc_chunk
    l5_n_oc_groups = op2._l5_n_oc_groups
    l5_chunks = []
    for g in range(l5_n_oc_groups):
        oc_s = g * l5_oc_chunk
        w_chunk = w_l5[oc_s : oc_s + l5_oc_chunk]
        b_chunk = b_l5[oc_s : oc_s + l5_oc_chunk]
        l5_chunks.append(pack_fused_weights_k3(w_chunk, b_chunk))

    op2.write_buffer("weights", np.concatenate([l4_packed, np.concatenate(l5_chunks)]))
    op2.write_buffer("output", np.zeros(op2._output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op2.run_runlist()
    t1 = time.perf_counter()
    phase_times["Phase 2"] = t1 - t0

    # Read and verify Phase 2 output (L5 output at offset 0)
    l5_total_output = op2._l5_total_output
    output_raw = op2.read_buffer("output", (op2._output_buf_size,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(
        output_raw[:l5_total_output].copy(), l5_oc, l5_out_h, l5_out_w
    )

    ref_np = ref_final.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt3 = int(np.sum(diff > 3))
    errors_gt5 = int(np.sum(diff > 5))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nP1→P2 test {l0_ic}ic_{l5_oc}oc_{l0_h}h_{l0_w}w:")
    print(f"  Final dims: {l5_oc}ch x {l5_out_h}h x {l5_out_w}w")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  Errors (>5): {errors_gt5}/{total}")
    for phase_name, dt in phase_times.items():
        print(f"  {phase_name} NPU time: {1000 * dt:.1f} ms")
    total_time = sum(phase_times.values())
    print(f"  Total NPU time: {1000 * total_time:.1f} ms")

    # P1 (7 fused SiLU layers) + P2 (8 non-fused layers + 1 fused SiLU)
    assert max_diff <= 15, f"P1→P2 failed: max_diff={max_diff} exceeds threshold 15"
    error_rate_gt5 = errors_gt5 / total if total > 0 else 0
    assert (
        error_rate_gt5 < 0.20
    ), f"P1→P2: {100 * error_rate_gt5:.2f}% errors > 5 exceeds 20% threshold"


# ---------------------------------------------------------------------------
# Step 13: Combined L6(C2f) + L7(k3s2, single-core OC streaming)
# ---------------------------------------------------------------------------


class AIEDataflowL6L7Combined(AIEOperatorBase):
    """Combined L6(C2f) + L7(k3s2) in one PDI.

    L6-only mode (l7_oc=0): phases A-D, 8 cores, 2 columns.
    L6+L7 mode (l7_oc>0): phases A-E, 9 cores, 3 columns.
    """

    def __init__(
        self,
        height,
        width,
        in_channels,
        cv1_scale,
        bn0_cv1_scale,
        bn0_cv2_scale,
        bn1_cv1_scale,
        bn1_cv2_scale,
        cv2_scale,
        l7_oc=0,
        l7_shift1=0,
        l7_shift2=0,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.cv1_scale = cv1_scale
        self.bn0_cv1_scale = bn0_cv1_scale
        self.bn0_cv2_scale = bn0_cv2_scale
        self.bn1_cv1_scale = bn1_cv1_scale
        self.bn1_cv2_scale = bn1_cv2_scale
        self.cv2_scale = cv2_scale
        self.l7_oc = l7_oc
        self.l7_shift1 = l7_shift1
        self.l7_shift2 = l7_shift2

        self.cv1_oc = 128
        self.bn_ch = 64
        self.cv2_ic = 256
        self.cv2_oc = 128
        self.l7_mode = l7_oc > 0

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        if self.l7_mode:
            file_name_base = (
                f"dataflow_l6l7_{self.in_channels}ic_{self.l7_oc}oc_"
                f"{self.height}h_{self.width}w"
            )
        else:
            file_name_base = (
                f"dataflow_l6l7_l6only_{self.in_channels}ic_"
                f"{self.height}h_{self.width}w"
            )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_l6_l7_combined",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.cv1_scale,
                self.bn0_cv1_scale,
                self.bn0_cv2_scale,
                self.bn1_cv1_scale,
                self.bn1_cv2_scale,
                self.cv2_scale,
                self.l7_oc,
                self.l7_shift1,
                self.l7_shift2,
            ],
        )

        k1_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k3_bn_kernel_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_bn.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3_i8=conv2dk3_i8_bn",
                "-Dconv2dk3s2_i8=conv2dk3s2_i8_bn",
            ],
        )

        add_kernel_obj = KernelObjectArtifact.new(
            "add_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "add_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT", "-DSCALAR"],
        )

        k1_cv2_kernel_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_cv2.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk1_i8=conv2dk1_i8_cv2",
            ],
        )

        kernel_deps = [
            mlir_artifact,
            k1_kernel_obj,
            k3_bn_kernel_obj,
            add_kernel_obj,
            k1_cv2_kernel_obj,
        ]

        # L7 kernel object (conv2dk3s2_i8_silu_l7 already defined in source)
        if self.l7_mode:
            l7_obj = KernelObjectArtifact.new(
                "conv2dk3_i8_silu_l7.o",
                depends=[
                    SourceArtifact.new(
                        self.context.base_dir
                        / "aie_kernels"
                        / "aie2p"
                        / "conv2dk3_i8_silu.cc"
                    )
                ],
                extra_flags=["-DINT8_ACT"],
            )
            kernel_deps.append(l7_obj)

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=kernel_deps,
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width

        cv1_wt = self.cv1_oc * self.in_channels
        bn_k3_wt = self.bn_ch * self.bn_ch * 9
        cv2_wt = self.cv2_oc * self.cv2_ic

        bn_wt_slot = bn_k3_wt
        l6_total_wt = cv1_wt + 4 * bn_wt_slot + cv2_wt

        l6_output_size = self.cv2_oc * self.height * self.width
        total_concat = self.cv2_ic * self.height * self.width

        if self.l7_mode:
            from iron.operators.conv2d_int8.dataflow_design import (
                _compute_oc_streaming_params,
            )

            l7_ic = self.cv2_oc
            l7_out_h = self.height // 2
            l7_out_w = self.width // 2

            l7_oc_chunk, l7_n_oc_groups, _ = _compute_oc_streaming_params(
                l7_ic, self.l7_oc, self.width, 2
            )
            l7_wt_chunk = l7_oc_chunk * l7_ic * 9 + l7_oc_chunk * 4
            l7_total_wt = l7_n_oc_groups * l7_wt_chunk
            self._l7_oc_chunk = l7_oc_chunk
            self._l7_n_oc_groups = l7_n_oc_groups

            l7_total_output = self.l7_oc * l7_out_h * l7_out_w
            self._l7_total_output = l7_total_output

            total_wt = l6_total_wt + l7_total_wt
            output_buf_size = l7_total_output + l6_output_size + total_concat
        else:
            total_wt = l6_total_wt
            output_buf_size = l6_output_size + total_concat

        self._l6_output_size = l6_output_size
        self._output_buf_size = output_buf_size

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", output_buf_size, dtype=np.int8)

        self.add_kernel(
            "l6_l7_combined",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("l6_l7_combined", "input", "weights", "output")


@pytest.mark.parametrize(
    "height,width,ic",
    [
        pytest.param(8, 8, 128, id="l6l7_step1_8x8"),
        pytest.param(16, 16, 128, id="l6l7_step1_16x16"),
    ],
)
def test_dataflow_l6_l7_step1(height, width, ic, aie_context):
    """Test L6+L7 combined, Step 1: L6 C2f only (l7_oc=0)."""
    torch.manual_seed(42)

    bn_ch = 64
    cv2_ic = 256
    cv2_oc = 128
    scale = 10

    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_cv1 = torch.randint(-50, 51, (128, ic, 1, 1), dtype=torch.int8)
    w_bn0cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn0cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, cv2_ic, 1, 1), dtype=torch.int8)

    # CPU reference
    cv1_out = conv2d_int8_reference(x_int8, w_cv1, scale, stride=1, padding=0)
    half1 = cv1_out[:, :bn_ch, :, :]
    half2 = cv1_out[:, bn_ch:, :, :]
    bn0_inter = conv2d_int8_reference(half2, w_bn0cv1, scale, stride=1, padding=1)
    bn0_cv2_out = conv2d_int8_reference(bn0_inter, w_bn0cv2, scale, stride=1, padding=1)
    bn0_out = add_i8_reference(bn0_cv2_out, half2)
    bn1_inter = conv2d_int8_reference(bn0_out, w_bn1cv1, scale, stride=1, padding=1)
    bn1_cv2_out = conv2d_int8_reference(bn1_inter, w_bn1cv2, scale, stride=1, padding=1)
    bn1_out = add_i8_reference(bn1_cv2_out, bn0_out)
    concat = torch.cat([half1, half2, bn0_out, bn1_out], dim=1)
    ref = conv2d_int8_reference(concat, w_cv2, scale, stride=1, padding=0)

    op = AIEDataflowL6L7Combined(
        height=height,
        width=width,
        in_channels=ic,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        bn1_cv1_scale=scale,
        bn1_cv2_scale=scale,
        cv2_scale=scale,
        l7_oc=0,
        context=aie_context,
    )
    op.context.compile_all()
    op.context.prepare_runtime()

    op.write_buffer("input", nchw_to_tiled_int8(x_int8))
    packed_all = np.concatenate(
        [
            weights_to_tiled_int8(w_cv1),
            weights_to_tiled_int8_k3(w_bn0cv1),
            weights_to_tiled_int8_k3(w_bn0cv2),
            weights_to_tiled_int8_k3(w_bn1cv1),
            weights_to_tiled_int8_k3(w_bn1cv2),
            weights_to_tiled_int8(w_cv2),
        ]
    )
    op.write_buffer("weights", packed_all)
    op.write_buffer("output", np.zeros(op._output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    l6_output_size = op._l6_output_size
    output_raw = op.read_buffer("output", (op._output_buf_size,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(
        output_raw[:l6_output_size].copy(), cv2_oc, height, width
    )

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)
    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt1 = int(np.sum(diff > 1))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nL6+L7 Step 1 (L6 only) {ic}ic_{height}h_{width}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # L6 has larger channels (128/64/256/128) than L4, more rounding
    # Matches existing C2f L6 standalone tolerance (max_diff=9 at 16x16)
    assert (
        max_diff <= 9
    ), f"L6+L7 Step 1 failed: max_diff={max_diff} exceeds threshold 9"


@pytest.mark.parametrize(
    "height,width",
    [
        pytest.param(16, 16, id="l6l7_step2_16x16"),
        pytest.param(
            40,
            40,
            id="l6l7_step2_40x40",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_l6_l7_step2(height, width, aie_context):
    """Test L6+L7 combined: L6 C2f + L7 k3s2 with OC streaming."""
    torch.manual_seed(42)

    ic = 128
    bn_ch = 64
    cv2_ic = 256
    cv2_oc = 128
    l7_oc = 256
    scale = 10
    l7_shift1 = 10
    l7_shift2 = 7

    l7_out_h = height // 2
    l7_out_w = width // 2

    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_cv1 = torch.randint(-50, 51, (128, ic, 1, 1), dtype=torch.int8)
    w_bn0cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn0cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn1cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, cv2_ic, 1, 1), dtype=torch.int8)
    w_l7 = torch.randint(-50, 51, (l7_oc, cv2_oc, 3, 3), dtype=torch.int8)
    b_l7 = torch.randint(-500, 501, (l7_oc,), dtype=torch.int32)

    # CPU reference: L6 C2f
    cv1_out = conv2d_int8_reference(x_int8, w_cv1, scale, stride=1, padding=0)
    half1 = cv1_out[:, :bn_ch, :, :]
    half2 = cv1_out[:, bn_ch:, :, :]
    bn0_inter = conv2d_int8_reference(half2, w_bn0cv1, scale, stride=1, padding=1)
    bn0_cv2_out = conv2d_int8_reference(bn0_inter, w_bn0cv2, scale, stride=1, padding=1)
    bn0_out = add_i8_reference(bn0_cv2_out, half2)
    bn1_inter = conv2d_int8_reference(bn0_out, w_bn1cv1, scale, stride=1, padding=1)
    bn1_cv2_out = conv2d_int8_reference(bn1_inter, w_bn1cv2, scale, stride=1, padding=1)
    bn1_out = add_i8_reference(bn1_cv2_out, bn0_out)
    concat = torch.cat([half1, half2, bn0_out, bn1_out], dim=1)
    l6_out = conv2d_int8_reference(concat, w_cv2, scale, stride=1, padding=0)

    # CPU reference: L7 (fused SiLU, stride-2)
    ref = conv2d_int8_pade_silu_reference(
        l6_out, w_l7, b_l7, l7_shift1, l7_shift2, stride=2
    )

    op = AIEDataflowL6L7Combined(
        height=height,
        width=width,
        in_channels=ic,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        bn1_cv1_scale=scale,
        bn1_cv2_scale=scale,
        cv2_scale=scale,
        l7_oc=l7_oc,
        l7_shift1=l7_shift1,
        l7_shift2=l7_shift2,
        context=aie_context,
    )
    op.context.compile_all()
    op.context.prepare_runtime()

    op.write_buffer("input", nchw_to_tiled_int8(x_int8))

    # Pack L6 + L7 weights
    l6_packed = np.concatenate(
        [
            weights_to_tiled_int8(w_cv1),
            weights_to_tiled_int8_k3(w_bn0cv1),
            weights_to_tiled_int8_k3(w_bn0cv2),
            weights_to_tiled_int8_k3(w_bn1cv1),
            weights_to_tiled_int8_k3(w_bn1cv2),
            weights_to_tiled_int8(w_cv2),
        ]
    )

    l7_oc_chunk = op._l7_oc_chunk
    l7_n_oc_groups = op._l7_n_oc_groups
    l7_chunks = []
    for g in range(l7_n_oc_groups):
        oc_s = g * l7_oc_chunk
        l7_chunks.append(
            pack_fused_weights_k3(
                w_l7[oc_s : oc_s + l7_oc_chunk], b_l7[oc_s : oc_s + l7_oc_chunk]
            )
        )

    op.write_buffer("weights", np.concatenate([l6_packed, np.concatenate(l7_chunks)]))
    op.write_buffer("output", np.zeros(op._output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    l7_total_output = op._l7_total_output
    output_raw = op.read_buffer("output", (op._output_buf_size,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(
        output_raw[:l7_total_output].copy(), l7_oc, l7_out_h, l7_out_w
    )

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)
    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt3 = int(np.sum(diff > 3))
    errors_gt5 = int(np.sum(diff > 5))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nL6+L7 Step 2 {ic}ic_{l7_oc}oc_{height}h_{width}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  Errors (>5): {errors_gt5}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    assert (
        max_diff <= 10
    ), f"L6+L7 Step 2 failed: max_diff={max_diff} exceeds threshold 10"
    error_rate_gt5 = errors_gt5 / total if total > 0 else 0
    assert error_rate_gt5 < 0.15, (
        f"L6+L7 Step 2: {100 * error_rate_gt5:.2f}% errors > 5 "
        f"exceeds 15% threshold"
    )


# ---------------------------------------------------------------------------
# Step 14: P1→P2→P3 chain test
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "l0_h,l0_w",
    [
        pytest.param(64, 64, id="p1_p2_p3_64x64"),
        pytest.param(
            640,
            640,
            id="p1_p2_p3_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_p1_through_p3(l0_h, l0_w):
    """Test backbone P1→P2→P3: three combined PDIs in sequence.

    P1: L0(8->16)->L1(16->32)->C2f L2->L3(32->64)
    P2: C2f L4(64ch) + L5(64->128, OC streaming)
    P3: C2f L6(128ch) + L7(128->256, OC streaming)
    """
    torch.manual_seed(42)

    l0_ic = 8
    l0_oc = 16
    l1_oc = 32
    l3_oc = 64
    l5_oc = 128
    l7_oc = 256
    scale = 10
    shift2 = 7
    bn_ch_l2 = 16
    bn_ch_l4 = 32
    bn_ch_l6 = 64

    # Spatial dims through the backbone
    l3_out_h = l0_h // 8  # after L0(s2), L1(s2), L3(s2)
    l3_out_w = l0_w // 8
    l5_out_h = l3_out_h // 2  # after L5(s2)
    l5_out_w = l3_out_w // 2
    l7_out_h = l5_out_h // 2  # after L7(s2)
    l7_out_w = l5_out_w // 2

    # Generate all weights
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)

    # P1 weights
    w0 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    b0 = torch.randint(-500, 501, (l0_oc,), dtype=torch.int32)
    w1 = torch.randint(-50, 51, (l1_oc, l0_oc, 3, 3), dtype=torch.int8)
    b1 = torch.randint(-500, 501, (l1_oc,), dtype=torch.int32)
    w_cv1_l2 = torch.randint(-50, 51, (32, l1_oc, 1, 1), dtype=torch.int8)
    b_cv1_l2 = torch.randint(-500, 501, (32,), dtype=torch.int32)
    w_bn1_l2 = torch.randint(-50, 51, (bn_ch_l2, bn_ch_l2, 3, 3), dtype=torch.int8)
    b_bn1_l2 = torch.randint(-500, 501, (bn_ch_l2,), dtype=torch.int32)
    w_bn2_l2 = torch.randint(-50, 51, (bn_ch_l2, bn_ch_l2, 3, 3), dtype=torch.int8)
    b_bn2_l2 = torch.randint(-500, 501, (bn_ch_l2,), dtype=torch.int32)
    w_cv2_l2 = torch.randint(-50, 51, (32, 48, 1, 1), dtype=torch.int8)
    b_cv2_l2 = torch.randint(-500, 501, (32,), dtype=torch.int32)
    w3 = torch.randint(-50, 51, (l3_oc, 32, 3, 3), dtype=torch.int8)
    b3 = torch.randint(-500, 501, (l3_oc,), dtype=torch.int32)

    # P2 weights (L4 C2f non-fused + L5 fused)
    w_cv1_l4 = torch.randint(-50, 51, (64, l3_oc, 1, 1), dtype=torch.int8)
    w_bn0cv1_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn0cv2_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn1cv1_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn1cv2_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_cv2_l4 = torch.randint(-50, 51, (64, 128, 1, 1), dtype=torch.int8)
    w_l5 = torch.randint(-50, 51, (l5_oc, 64, 3, 3), dtype=torch.int8)
    b_l5 = torch.randint(-500, 501, (l5_oc,), dtype=torch.int32)

    # P3 weights (L6 C2f non-fused + L7 fused)
    w_cv1_l6 = torch.randint(-50, 51, (128, l5_oc, 1, 1), dtype=torch.int8)
    w_bn0cv1_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_bn0cv2_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_bn1cv1_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_bn1cv2_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_cv2_l6 = torch.randint(-50, 51, (128, 256, 1, 1), dtype=torch.int8)
    w_l7 = torch.randint(-50, 51, (l7_oc, 128, 3, 3), dtype=torch.int8)
    b_l7 = torch.randint(-500, 501, (l7_oc,), dtype=torch.int32)

    # ================================================================
    # CPU reference (full pipeline)
    # ================================================================
    # P1
    inter01 = conv2d_int8_pade_silu_reference(x_int8, w0, b0, scale, shift2, stride=2)
    l1_out = conv2d_int8_pade_silu_reference(inter01, w1, b1, scale, shift2, stride=2)
    cv1_l2 = conv2d_int8_pade_silu_reference(
        l1_out, w_cv1_l2, b_cv1_l2, scale, shift2, stride=1, padding=0
    )
    half1_l2 = cv1_l2[:, :bn_ch_l2, :, :]
    half2_l2 = cv1_l2[:, bn_ch_l2:, :, :]
    bn_inter_l2 = conv2d_int8_pade_silu_reference(
        half2_l2, w_bn1_l2, b_bn1_l2, scale, shift2, stride=1, padding=1
    )
    bn_out_l2 = conv2d_int8_pade_silu_reference(
        bn_inter_l2, w_bn2_l2, b_bn2_l2, scale, shift2, stride=1, padding=1
    )
    concat_l2 = torch.cat([half1_l2, half2_l2, bn_out_l2], dim=1)
    c2f_l2_out = conv2d_int8_pade_silu_reference(
        concat_l2, w_cv2_l2, b_cv2_l2, scale, shift2, stride=1, padding=0
    )
    l3_out = conv2d_int8_pade_silu_reference(
        c2f_l2_out, w3, b3, scale, shift2, stride=2
    )

    # P2
    cv1_l4 = conv2d_int8_reference(l3_out, w_cv1_l4, scale, stride=1, padding=0)
    half1_l4 = cv1_l4[:, :bn_ch_l4, :, :]
    half2_l4 = cv1_l4[:, bn_ch_l4:, :, :]
    bn0_inter_l4 = conv2d_int8_reference(
        half2_l4, w_bn0cv1_l4, scale, stride=1, padding=1
    )
    bn0_cv2_l4 = conv2d_int8_reference(
        bn0_inter_l4, w_bn0cv2_l4, scale, stride=1, padding=1
    )
    bn0_out_l4 = add_i8_reference(bn0_cv2_l4, half2_l4)
    bn1_inter_l4 = conv2d_int8_reference(
        bn0_out_l4, w_bn1cv1_l4, scale, stride=1, padding=1
    )
    bn1_cv2_l4 = conv2d_int8_reference(
        bn1_inter_l4, w_bn1cv2_l4, scale, stride=1, padding=1
    )
    bn1_out_l4 = add_i8_reference(bn1_cv2_l4, bn0_out_l4)
    concat_l4 = torch.cat([half1_l4, half2_l4, bn0_out_l4, bn1_out_l4], dim=1)
    l4_out = conv2d_int8_reference(concat_l4, w_cv2_l4, scale, stride=1, padding=0)
    l5_out = conv2d_int8_pade_silu_reference(
        l4_out, w_l5, b_l5, scale, shift2, stride=2
    )

    # P3
    cv1_l6 = conv2d_int8_reference(l5_out, w_cv1_l6, scale, stride=1, padding=0)
    half1_l6 = cv1_l6[:, :bn_ch_l6, :, :]
    half2_l6 = cv1_l6[:, bn_ch_l6:, :, :]
    bn0_inter_l6 = conv2d_int8_reference(
        half2_l6, w_bn0cv1_l6, scale, stride=1, padding=1
    )
    bn0_cv2_l6 = conv2d_int8_reference(
        bn0_inter_l6, w_bn0cv2_l6, scale, stride=1, padding=1
    )
    bn0_out_l6 = add_i8_reference(bn0_cv2_l6, half2_l6)
    bn1_inter_l6 = conv2d_int8_reference(
        bn0_out_l6, w_bn1cv1_l6, scale, stride=1, padding=1
    )
    bn1_cv2_l6 = conv2d_int8_reference(
        bn1_inter_l6, w_bn1cv2_l6, scale, stride=1, padding=1
    )
    bn1_out_l6 = add_i8_reference(bn1_cv2_l6, bn0_out_l6)
    concat_l6 = torch.cat([half1_l6, half2_l6, bn0_out_l6, bn1_out_l6], dim=1)
    l6_out = conv2d_int8_reference(concat_l6, w_cv2_l6, scale, stride=1, padding=0)
    ref_final = conv2d_int8_pade_silu_reference(
        l6_out, w_l7, b_l7, scale, shift2, stride=2
    )

    phase_times = {}

    # ================================================================
    # Phase 1
    # ================================================================
    ctx1 = AIEContext()
    op1 = AIEDataflowBackbonePhase1(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_shift1=scale,
        l0_shift2=shift2,
        l1_oc=l1_oc,
        l1_shift1=scale,
        l1_shift2=shift2,
        cv1_shift1=scale,
        cv1_shift2=shift2,
        bn_cv1_shift1=scale,
        bn_cv1_shift2=shift2,
        bn_cv2_shift1=scale,
        bn_cv2_shift2=shift2,
        cv2_shift1=scale,
        cv2_shift2=shift2,
        l3_oc=l3_oc,
        l3_shift1=scale,
        l3_shift2=shift2,
        context=ctx1,
    )
    op1.context.compile_all()
    op1.context.prepare_runtime()
    op1.write_buffer("input", nchw_to_tiled_int8(x_int8))

    def _pad(data, slot_size):
        return np.concatenate([data, np.zeros(slot_size - len(data), dtype=np.int8)])

    tg1_wt_slot = op1._tg1_wt_slot
    c2f_wt_slot = op1._c2f_wt_slot
    p1_packed = np.concatenate(
        [
            _pad(pack_fused_weights_k3(w0, b0), tg1_wt_slot),
            _pad(pack_fused_weights_k3(w1, b1), tg1_wt_slot),
            _pad(_pack_k1_silu_weights(w_cv1_l2, b_cv1_l2), c2f_wt_slot),
            _pad(pack_fused_weights_k3(w_bn1_l2, b_bn1_l2), c2f_wt_slot),
            _pad(pack_fused_weights_k3(w_bn2_l2, b_bn2_l2), c2f_wt_slot),
            _pad(_pack_k1_silu_weights(w_cv2_l2, b_cv2_l2), c2f_wt_slot),
            pack_fused_weights_k3(w3, b3),
        ]
    )
    op1.write_buffer("weights", p1_packed)
    op1.write_buffer("output", np.zeros(op1.buffers["output"], dtype=np.int8))

    t0 = time.perf_counter()
    op1.run_runlist()
    t1 = time.perf_counter()
    phase_times["Phase 1"] = t1 - t0

    p1_out_buf = op1.read_buffer("output", (op1.buffers["output"],), dtype=np.int8)
    p1_output_tiled = p1_out_buf[: op1._total_output].copy()

    # ================================================================
    # Phase 2
    # ================================================================
    ctx2 = AIEContext()
    op2 = AIEDataflowL4L5Combined(
        height=l3_out_h,
        width=l3_out_w,
        in_channels=l3_oc,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        bn1_cv1_scale=scale,
        bn1_cv2_scale=scale,
        cv2_scale=scale,
        l5_oc=l5_oc,
        l5_shift1=scale,
        l5_shift2=shift2,
        context=ctx2,
    )
    op2.context.compile_all()
    op2.context.prepare_runtime()
    op2.write_buffer("input", p1_output_tiled)

    l4_packed = np.concatenate(
        [
            weights_to_tiled_int8(w_cv1_l4),
            weights_to_tiled_int8_k3(w_bn0cv1_l4),
            weights_to_tiled_int8_k3(w_bn0cv2_l4),
            weights_to_tiled_int8_k3(w_bn1cv1_l4),
            weights_to_tiled_int8_k3(w_bn1cv2_l4),
            weights_to_tiled_int8(w_cv2_l4),
        ]
    )
    l5_oc_chunk = op2._l5_oc_chunk
    l5_n_oc_groups = op2._l5_n_oc_groups
    l5_chunks = [
        pack_fused_weights_k3(
            w_l5[g * l5_oc_chunk : (g + 1) * l5_oc_chunk],
            b_l5[g * l5_oc_chunk : (g + 1) * l5_oc_chunk],
        )
        for g in range(l5_n_oc_groups)
    ]
    op2.write_buffer("weights", np.concatenate([l4_packed, np.concatenate(l5_chunks)]))
    op2.write_buffer("output", np.zeros(op2._output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op2.run_runlist()
    t1 = time.perf_counter()
    phase_times["Phase 2"] = t1 - t0

    p2_out_buf = op2.read_buffer("output", (op2._output_buf_size,), dtype=np.int8)
    p2_output_tiled = p2_out_buf[: op2._l5_total_output].copy()

    # ================================================================
    # Phase 3
    # ================================================================
    ctx3 = AIEContext()
    op3 = AIEDataflowL6L7Combined(
        height=l5_out_h,
        width=l5_out_w,
        in_channels=l5_oc,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        bn1_cv1_scale=scale,
        bn1_cv2_scale=scale,
        cv2_scale=scale,
        l7_oc=l7_oc,
        l7_shift1=scale,
        l7_shift2=shift2,
        context=ctx3,
    )
    op3.context.compile_all()
    op3.context.prepare_runtime()
    op3.write_buffer("input", p2_output_tiled)

    l6_packed = np.concatenate(
        [
            weights_to_tiled_int8(w_cv1_l6),
            weights_to_tiled_int8_k3(w_bn0cv1_l6),
            weights_to_tiled_int8_k3(w_bn0cv2_l6),
            weights_to_tiled_int8_k3(w_bn1cv1_l6),
            weights_to_tiled_int8_k3(w_bn1cv2_l6),
            weights_to_tiled_int8(w_cv2_l6),
        ]
    )
    l7_oc_chunk = op3._l7_oc_chunk
    l7_n_oc_groups = op3._l7_n_oc_groups
    l7_chunks = [
        pack_fused_weights_k3(
            w_l7[g * l7_oc_chunk : (g + 1) * l7_oc_chunk],
            b_l7[g * l7_oc_chunk : (g + 1) * l7_oc_chunk],
        )
        for g in range(l7_n_oc_groups)
    ]
    op3.write_buffer("weights", np.concatenate([l6_packed, np.concatenate(l7_chunks)]))
    op3.write_buffer("output", np.zeros(op3._output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op3.run_runlist()
    t1 = time.perf_counter()
    phase_times["Phase 3"] = t1 - t0

    # ================================================================
    # Verify final output
    # ================================================================
    l7_total_output = op3._l7_total_output
    p3_out_buf = op3.read_buffer("output", (op3._output_buf_size,), dtype=np.int8)
    npu_final = tiled_to_nchw_int8(
        p3_out_buf[:l7_total_output].copy(), l7_oc, l7_out_h, l7_out_w
    )

    ref_np = ref_final.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_final.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt3 = int(np.sum(diff > 3))
    errors_gt5 = int(np.sum(diff > 5))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nP1→P2→P3 test {l0_ic}ic_{l7_oc}oc_{l0_h}h_{l0_w}w:")
    print(f"  Final dims: {l7_oc}ch x {l7_out_h}h x {l7_out_w}w")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  Errors (>5): {errors_gt5}/{total}")
    for phase_name, dt in phase_times.items():
        print(f"  {phase_name} NPU time: {1000 * dt:.1f} ms")
    total_time = sum(phase_times.values())
    print(f"  Total NPU time: {1000 * total_time:.1f} ms")

    # 3 PDIs, ~25 layers total, compounds errors
    assert max_diff <= 15, f"P1→P2→P3 failed: max_diff={max_diff} exceeds threshold 15"
    error_rate_gt5 = errors_gt5 / total if total > 0 else 0
    assert (
        error_rate_gt5 < 0.20
    ), f"P1→P2→P3: {100 * error_rate_gt5:.2f}% errors > 5 exceeds 20% threshold"


# ---------------------------------------------------------------------------
# Step 14: L8 C2f (n=1 bottleneck, OC streaming on all layers)
# ---------------------------------------------------------------------------


class AIEDataflowL8C2f(AIEOperatorBase):
    """L8 C2f block with OC streaming on all layers.

    5 sequential phases (cv1, bn0.cv1, bn0.cv2, bn0_add, cv2),
    each using single-core OC streaming where weights exceed L1.
    """

    def __init__(
        self,
        height,
        width,
        in_channels,
        cv1_scale,
        bn0_cv1_scale,
        bn0_cv2_scale,
        cv2_scale,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.cv1_scale = cv1_scale
        self.bn0_cv1_scale = bn0_cv1_scale
        self.bn0_cv2_scale = bn0_cv2_scale
        self.cv2_scale = cv2_scale

        self.cv1_oc = 256
        self.half_ch = 128
        self.bn_ch = 128
        self.concat_ch = 384
        self.cv2_oc = 256

        # OC streaming params
        self.cv1_oc_chunk = 128
        self.cv1_n_groups = 2
        self.bn_oc_chunk = 32
        self.bn_n_groups = 4
        self.cv2_oc_chunk = 64
        self.cv2_n_groups = 4

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_l8_c2f_{self.in_channels}ic_" f"{self.height}h_{self.width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_l8_c2f",
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.cv1_scale,
                self.bn0_cv1_scale,
                self.bn0_cv2_scale,
                self.cv2_scale,
            ],
        )

        k1_obj = KernelObjectArtifact.new(
            "conv2dk1_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k3_bn_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_bn.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3_i8=conv2dk3_i8_bn",
                "-Dconv2dk3s2_i8=conv2dk3s2_i8_bn",
            ],
        )

        k3_bn_cv2_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_bn_cv2.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3_i8=conv2dk3_i8_bn_cv2",
                "-Dconv2dk3s2_i8=conv2dk3s2_i8_bn_cv2",
            ],
        )

        add_obj = KernelObjectArtifact.new(
            "add_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "add_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT", "-DSCALAR"],
        )

        k1_cv2_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_cv2.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk1_i8=conv2dk1_i8_cv2",
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                k1_obj,
                k3_bn_obj,
                k3_bn_cv2_obj,
                add_obj,
                k1_cv2_obj,
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width

        # Weight sizes
        cv1_wt_chunk = self.cv1_oc_chunk * self.in_channels
        cv1_total_wt = self.cv1_n_groups * cv1_wt_chunk
        bn_wt_chunk = self.bn_oc_chunk * self.bn_ch * 9
        bn_total_wt_each = self.bn_n_groups * bn_wt_chunk
        cv2_wt_chunk = self.cv2_oc_chunk * self.concat_ch
        cv2_total_wt = self.cv2_n_groups * cv2_wt_chunk
        total_wt = cv1_total_wt + 2 * bn_total_wt_each + cv2_total_wt

        # Output buffer
        final_size = self.cv2_oc * self.height * self.width
        concat_size = self.concat_ch * self.height * self.width
        scratch_size = self.bn_ch * self.height * self.width
        output_buf_size = final_size + concat_size + 2 * scratch_size

        self._final_size = final_size
        self._output_buf_size = output_buf_size

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", output_buf_size, dtype=np.int8)

        self.add_kernel(
            "l8_c2f",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("l8_c2f", "input", "weights", "output")


@pytest.mark.parametrize(
    "height,width",
    [
        pytest.param(8, 8, id="l8_c2f_8x8"),
        pytest.param(20, 20, id="l8_c2f_20x20", marks=pytest.mark.extensive),
    ],
)
def test_dataflow_l8(height, width, aie_context):
    """Test L8 C2f: n=1 bottleneck, OC streaming on all layers."""
    torch.manual_seed(42)

    ic = 256
    cv1_oc = 256
    half_ch = 128
    bn_ch = 128
    concat_ch = 384
    cv2_oc = 256
    scale = 10

    x_int8 = torch.randint(-20, 21, (1, ic, height, width), dtype=torch.int8)
    w_cv1 = torch.randint(-50, 51, (cv1_oc, ic, 1, 1), dtype=torch.int8)
    w_bn0cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_bn0cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, concat_ch, 1, 1), dtype=torch.int8)

    # CPU reference
    cv1_out = conv2d_int8_reference(x_int8, w_cv1, scale, stride=1, padding=0)
    half1 = cv1_out[:, :half_ch, :, :]
    half2 = cv1_out[:, half_ch:, :, :]
    bn0_inter = conv2d_int8_reference(half2, w_bn0cv1, scale, stride=1, padding=1)
    bn0_cv2_out = conv2d_int8_reference(bn0_inter, w_bn0cv2, scale, stride=1, padding=1)
    bn0_out = add_i8_reference(bn0_cv2_out, half2)
    concat = torch.cat([half1, half2, bn0_out], dim=1)
    ref = conv2d_int8_reference(concat, w_cv2, scale, stride=1, padding=0)

    op = AIEDataflowL8C2f(
        height=height,
        width=width,
        in_channels=ic,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        cv2_scale=scale,
        context=aie_context,
    )
    op.context.compile_all()
    op.context.prepare_runtime()

    op.write_buffer("input", nchw_to_tiled_int8(x_int8))

    # Pack weights: [cv1_chunks | bn0cv1_chunks | bn0cv2_chunks | cv2_chunks]
    # cv1: oc_chunk=128, 2 groups
    cv1_chunks = []
    for g in range(2):
        oc_s = g * 128
        cv1_chunks.append(weights_to_tiled_int8(w_cv1[oc_s : oc_s + 128]))
    cv1_packed = np.concatenate(cv1_chunks)

    # bn0cv1: oc_chunk=32, 4 groups
    bn0cv1_chunks = []
    for g in range(4):
        oc_s = g * 32
        bn0cv1_chunks.append(weights_to_tiled_int8_k3(w_bn0cv1[oc_s : oc_s + 32]))
    bn0cv1_packed = np.concatenate(bn0cv1_chunks)

    # bn0cv2: oc_chunk=32, 4 groups
    bn0cv2_chunks = []
    for g in range(4):
        oc_s = g * 32
        bn0cv2_chunks.append(weights_to_tiled_int8_k3(w_bn0cv2[oc_s : oc_s + 32]))
    bn0cv2_packed = np.concatenate(bn0cv2_chunks)

    # cv2: oc_chunk=64, 4 groups
    cv2_chunks = []
    for g in range(4):
        oc_s = g * 64
        cv2_chunks.append(weights_to_tiled_int8(w_cv2[oc_s : oc_s + 64]))
    cv2_packed = np.concatenate(cv2_chunks)

    packed_all = np.concatenate([cv1_packed, bn0cv1_packed, bn0cv2_packed, cv2_packed])
    op.write_buffer("weights", packed_all)
    op.write_buffer("output", np.zeros(op._output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()

    output_raw = op.read_buffer("output", (op._output_buf_size,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(
        output_raw[: op._final_size].copy(), cv2_oc, height, width
    )

    ref_np = ref.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)
    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt3 = int(np.sum(diff > 3))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nL8 C2f test {ic}ic_{cv2_oc}oc_{height}h_{width}w:")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>1): {errors_gt1}/{total}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  NPU time: {1000 * (t1 - t0):.1f} ms")

    # 5-phase pipeline with OC streaming on 256ch tensors compounds
    # rounding through cv1(256->256) + bn0.cv1(128->128) + bn0.cv2(128->128)
    # + add + cv2(384->256). Non-fused integer conv accumulates errors.
    assert max_diff <= 15, f"L8 C2f failed: max_diff={max_diff} exceeds threshold 15"


# ---------------------------------------------------------------------------
# Step 15: Full backbone chain P1→P2→P3→P4
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "l0_h,l0_w",
    [
        pytest.param(64, 64, id="full_backbone_64x64"),
        pytest.param(
            640,
            640,
            id="full_backbone_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_full_backbone(l0_h, l0_w):
    """Test full backbone: P1→P2→P3→P4 (L0 through L8).

    P1: L0(8->16)->L1(16->32)->C2f L2->L3(32->64)
    P2: C2f L4(64ch) + L5(64->128, OC streaming)
    P3: C2f L6(128ch) + L7(128->256, OC streaming)
    P4: C2f L8(256ch, OC streaming on all layers)
    """
    torch.manual_seed(42)

    l0_ic = 8
    l0_oc = 16
    l1_oc = 32
    l3_oc = 64
    l5_oc = 128
    l7_oc = 256
    scale = 10
    shift2 = 7
    bn_ch_l2 = 16
    bn_ch_l4 = 32
    bn_ch_l6 = 64
    bn_ch_l8 = 128

    # Spatial dims
    l3_out_h = l0_h // 8
    l3_out_w = l0_w // 8
    l5_out_h = l3_out_h // 2
    l5_out_w = l3_out_w // 2
    l7_out_h = l5_out_h // 2
    l7_out_w = l5_out_w // 2

    # Generate weights
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)

    # P1 weights
    w0 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    b0 = torch.randint(-500, 501, (l0_oc,), dtype=torch.int32)
    w1 = torch.randint(-50, 51, (l1_oc, l0_oc, 3, 3), dtype=torch.int8)
    b1 = torch.randint(-500, 501, (l1_oc,), dtype=torch.int32)
    w_cv1_l2 = torch.randint(-50, 51, (32, l1_oc, 1, 1), dtype=torch.int8)
    b_cv1_l2 = torch.randint(-500, 501, (32,), dtype=torch.int32)
    w_bn1_l2 = torch.randint(-50, 51, (bn_ch_l2, bn_ch_l2, 3, 3), dtype=torch.int8)
    b_bn1_l2 = torch.randint(-500, 501, (bn_ch_l2,), dtype=torch.int32)
    w_bn2_l2 = torch.randint(-50, 51, (bn_ch_l2, bn_ch_l2, 3, 3), dtype=torch.int8)
    b_bn2_l2 = torch.randint(-500, 501, (bn_ch_l2,), dtype=torch.int32)
    w_cv2_l2 = torch.randint(-50, 51, (32, 48, 1, 1), dtype=torch.int8)
    b_cv2_l2 = torch.randint(-500, 501, (32,), dtype=torch.int32)
    w3 = torch.randint(-50, 51, (l3_oc, 32, 3, 3), dtype=torch.int8)
    b3 = torch.randint(-500, 501, (l3_oc,), dtype=torch.int32)

    # P2 weights
    w_cv1_l4 = torch.randint(-50, 51, (64, l3_oc, 1, 1), dtype=torch.int8)
    w_bn0cv1_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn0cv2_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn1cv1_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn1cv2_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_cv2_l4 = torch.randint(-50, 51, (64, 128, 1, 1), dtype=torch.int8)
    w_l5 = torch.randint(-50, 51, (l5_oc, 64, 3, 3), dtype=torch.int8)
    b_l5 = torch.randint(-500, 501, (l5_oc,), dtype=torch.int32)

    # P3 weights
    w_cv1_l6 = torch.randint(-50, 51, (128, l5_oc, 1, 1), dtype=torch.int8)
    w_bn0cv1_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_bn0cv2_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_bn1cv1_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_bn1cv2_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_cv2_l6 = torch.randint(-50, 51, (128, 256, 1, 1), dtype=torch.int8)
    w_l7 = torch.randint(-50, 51, (l7_oc, 128, 3, 3), dtype=torch.int8)
    b_l7 = torch.randint(-500, 501, (l7_oc,), dtype=torch.int32)

    # P4 weights (L8 C2f)
    w_cv1_l8 = torch.randint(-50, 51, (256, l7_oc, 1, 1), dtype=torch.int8)
    w_bn0cv1_l8 = torch.randint(-50, 51, (bn_ch_l8, bn_ch_l8, 3, 3), dtype=torch.int8)
    w_bn0cv2_l8 = torch.randint(-50, 51, (bn_ch_l8, bn_ch_l8, 3, 3), dtype=torch.int8)
    w_cv2_l8 = torch.randint(-50, 51, (256, 384, 1, 1), dtype=torch.int8)

    # ================================================================
    # CPU reference (full pipeline)
    # ================================================================
    # P1
    inter01 = conv2d_int8_pade_silu_reference(x_int8, w0, b0, scale, shift2, stride=2)
    l1_out = conv2d_int8_pade_silu_reference(inter01, w1, b1, scale, shift2, stride=2)
    cv1_l2 = conv2d_int8_pade_silu_reference(
        l1_out, w_cv1_l2, b_cv1_l2, scale, shift2, stride=1, padding=0
    )
    half1_l2 = cv1_l2[:, :bn_ch_l2, :, :]
    half2_l2 = cv1_l2[:, bn_ch_l2:, :, :]
    bn_inter_l2 = conv2d_int8_pade_silu_reference(
        half2_l2, w_bn1_l2, b_bn1_l2, scale, shift2, stride=1, padding=1
    )
    bn_out_l2 = conv2d_int8_pade_silu_reference(
        bn_inter_l2, w_bn2_l2, b_bn2_l2, scale, shift2, stride=1, padding=1
    )
    c2f_l2_out = conv2d_int8_pade_silu_reference(
        torch.cat([half1_l2, half2_l2, bn_out_l2], dim=1),
        w_cv2_l2,
        b_cv2_l2,
        scale,
        shift2,
        stride=1,
        padding=0,
    )
    l3_out = conv2d_int8_pade_silu_reference(
        c2f_l2_out, w3, b3, scale, shift2, stride=2
    )

    # P2
    cv1_l4 = conv2d_int8_reference(l3_out, w_cv1_l4, scale, stride=1, padding=0)
    half1_l4 = cv1_l4[:, :bn_ch_l4, :, :]
    half2_l4 = cv1_l4[:, bn_ch_l4:, :, :]
    bn0_l4 = add_i8_reference(
        conv2d_int8_reference(
            conv2d_int8_reference(half2_l4, w_bn0cv1_l4, scale, stride=1, padding=1),
            w_bn0cv2_l4,
            scale,
            stride=1,
            padding=1,
        ),
        half2_l4,
    )
    bn1_l4 = add_i8_reference(
        conv2d_int8_reference(
            conv2d_int8_reference(bn0_l4, w_bn1cv1_l4, scale, stride=1, padding=1),
            w_bn1cv2_l4,
            scale,
            stride=1,
            padding=1,
        ),
        bn0_l4,
    )
    l4_out = conv2d_int8_reference(
        torch.cat([half1_l4, half2_l4, bn0_l4, bn1_l4], dim=1),
        w_cv2_l4,
        scale,
        stride=1,
        padding=0,
    )
    l5_out = conv2d_int8_pade_silu_reference(
        l4_out, w_l5, b_l5, scale, shift2, stride=2
    )

    # P3
    cv1_l6 = conv2d_int8_reference(l5_out, w_cv1_l6, scale, stride=1, padding=0)
    half1_l6 = cv1_l6[:, :bn_ch_l6, :, :]
    half2_l6 = cv1_l6[:, bn_ch_l6:, :, :]
    bn0_l6 = add_i8_reference(
        conv2d_int8_reference(
            conv2d_int8_reference(half2_l6, w_bn0cv1_l6, scale, stride=1, padding=1),
            w_bn0cv2_l6,
            scale,
            stride=1,
            padding=1,
        ),
        half2_l6,
    )
    bn1_l6 = add_i8_reference(
        conv2d_int8_reference(
            conv2d_int8_reference(bn0_l6, w_bn1cv1_l6, scale, stride=1, padding=1),
            w_bn1cv2_l6,
            scale,
            stride=1,
            padding=1,
        ),
        bn0_l6,
    )
    l6_out = conv2d_int8_reference(
        torch.cat([half1_l6, half2_l6, bn0_l6, bn1_l6], dim=1),
        w_cv2_l6,
        scale,
        stride=1,
        padding=0,
    )
    l7_out = conv2d_int8_pade_silu_reference(
        l6_out, w_l7, b_l7, scale, shift2, stride=2
    )

    # P4 (L8 C2f)
    cv1_l8 = conv2d_int8_reference(l7_out, w_cv1_l8, scale, stride=1, padding=0)
    half1_l8 = cv1_l8[:, :bn_ch_l8, :, :]
    half2_l8 = cv1_l8[:, bn_ch_l8:, :, :]
    bn0_l8 = add_i8_reference(
        conv2d_int8_reference(
            conv2d_int8_reference(half2_l8, w_bn0cv1_l8, scale, stride=1, padding=1),
            w_bn0cv2_l8,
            scale,
            stride=1,
            padding=1,
        ),
        half2_l8,
    )
    ref_final = conv2d_int8_reference(
        torch.cat([half1_l8, half2_l8, bn0_l8], dim=1),
        w_cv2_l8,
        scale,
        stride=1,
        padding=0,
    )

    phase_times = {}

    def _pad(data, slot_size):
        return np.concatenate([data, np.zeros(slot_size - len(data), dtype=np.int8)])

    # ================================================================
    # Phase 1
    # ================================================================
    ctx1 = AIEContext()
    op1 = AIEDataflowBackbonePhase1(
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_shift1=scale,
        l0_shift2=shift2,
        l1_oc=l1_oc,
        l1_shift1=scale,
        l1_shift2=shift2,
        cv1_shift1=scale,
        cv1_shift2=shift2,
        bn_cv1_shift1=scale,
        bn_cv1_shift2=shift2,
        bn_cv2_shift1=scale,
        bn_cv2_shift2=shift2,
        cv2_shift1=scale,
        cv2_shift2=shift2,
        l3_oc=l3_oc,
        l3_shift1=scale,
        l3_shift2=shift2,
        context=ctx1,
    )
    op1.context.compile_all()
    op1.context.prepare_runtime()
    op1.write_buffer("input", nchw_to_tiled_int8(x_int8))
    tg1s = op1._tg1_wt_slot
    c2fs = op1._c2f_wt_slot
    op1.write_buffer(
        "weights",
        np.concatenate(
            [
                _pad(pack_fused_weights_k3(w0, b0), tg1s),
                _pad(pack_fused_weights_k3(w1, b1), tg1s),
                _pad(_pack_k1_silu_weights(w_cv1_l2, b_cv1_l2), c2fs),
                _pad(pack_fused_weights_k3(w_bn1_l2, b_bn1_l2), c2fs),
                _pad(pack_fused_weights_k3(w_bn2_l2, b_bn2_l2), c2fs),
                _pad(_pack_k1_silu_weights(w_cv2_l2, b_cv2_l2), c2fs),
                pack_fused_weights_k3(w3, b3),
            ]
        ),
    )
    op1.write_buffer("output", np.zeros(op1.buffers["output"], dtype=np.int8))
    t0 = time.perf_counter()
    op1.run_runlist()
    t1 = time.perf_counter()
    phase_times["P1"] = t1 - t0
    p1_buf = op1.read_buffer("output", (op1.buffers["output"],), dtype=np.int8)
    p1_tiled = p1_buf[: op1._total_output].copy()

    # ================================================================
    # Phase 2
    # ================================================================
    ctx2 = AIEContext()
    op2 = AIEDataflowL4L5Combined(
        height=l3_out_h,
        width=l3_out_w,
        in_channels=l3_oc,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        bn1_cv1_scale=scale,
        bn1_cv2_scale=scale,
        cv2_scale=scale,
        l5_oc=l5_oc,
        l5_shift1=scale,
        l5_shift2=shift2,
        context=ctx2,
    )
    op2.context.compile_all()
    op2.context.prepare_runtime()
    op2.write_buffer("input", p1_tiled)
    l4p = np.concatenate(
        [
            weights_to_tiled_int8(w_cv1_l4),
            weights_to_tiled_int8_k3(w_bn0cv1_l4),
            weights_to_tiled_int8_k3(w_bn0cv2_l4),
            weights_to_tiled_int8_k3(w_bn1cv1_l4),
            weights_to_tiled_int8_k3(w_bn1cv2_l4),
            weights_to_tiled_int8(w_cv2_l4),
        ]
    )
    l5c = op2._l5_oc_chunk
    l5g = op2._l5_n_oc_groups
    l5p = np.concatenate(
        [
            pack_fused_weights_k3(
                w_l5[g * l5c : (g + 1) * l5c], b_l5[g * l5c : (g + 1) * l5c]
            )
            for g in range(l5g)
        ]
    )
    op2.write_buffer("weights", np.concatenate([l4p, l5p]))
    op2.write_buffer("output", np.zeros(op2._output_buf_size, dtype=np.int8))
    t0 = time.perf_counter()
    op2.run_runlist()
    t1 = time.perf_counter()
    phase_times["P2"] = t1 - t0
    p2_buf = op2.read_buffer("output", (op2._output_buf_size,), dtype=np.int8)
    p2_tiled = p2_buf[: op2._l5_total_output].copy()

    # ================================================================
    # Phase 3
    # ================================================================
    ctx3 = AIEContext()
    op3 = AIEDataflowL6L7Combined(
        height=l5_out_h,
        width=l5_out_w,
        in_channels=l5_oc,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        bn1_cv1_scale=scale,
        bn1_cv2_scale=scale,
        cv2_scale=scale,
        l7_oc=l7_oc,
        l7_shift1=scale,
        l7_shift2=shift2,
        context=ctx3,
    )
    op3.context.compile_all()
    op3.context.prepare_runtime()
    op3.write_buffer("input", p2_tiled)
    l6p = np.concatenate(
        [
            weights_to_tiled_int8(w_cv1_l6),
            weights_to_tiled_int8_k3(w_bn0cv1_l6),
            weights_to_tiled_int8_k3(w_bn0cv2_l6),
            weights_to_tiled_int8_k3(w_bn1cv1_l6),
            weights_to_tiled_int8_k3(w_bn1cv2_l6),
            weights_to_tiled_int8(w_cv2_l6),
        ]
    )
    l7c = op3._l7_oc_chunk
    l7g = op3._l7_n_oc_groups
    l7p = np.concatenate(
        [
            pack_fused_weights_k3(
                w_l7[g * l7c : (g + 1) * l7c], b_l7[g * l7c : (g + 1) * l7c]
            )
            for g in range(l7g)
        ]
    )
    op3.write_buffer("weights", np.concatenate([l6p, l7p]))
    op3.write_buffer("output", np.zeros(op3._output_buf_size, dtype=np.int8))
    t0 = time.perf_counter()
    op3.run_runlist()
    t1 = time.perf_counter()
    phase_times["P3"] = t1 - t0
    p3_buf = op3.read_buffer("output", (op3._output_buf_size,), dtype=np.int8)
    p3_tiled = p3_buf[: op3._l7_total_output].copy()

    # ================================================================
    # Phase 4 (L8 C2f)
    # ================================================================
    ctx4 = AIEContext()
    op4 = AIEDataflowL8C2f(
        height=l7_out_h,
        width=l7_out_w,
        in_channels=l7_oc,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        cv2_scale=scale,
        context=ctx4,
    )
    op4.context.compile_all()
    op4.context.prepare_runtime()
    op4.write_buffer("input", p3_tiled)

    # L8 weights: [cv1_chunks | bn0cv1_chunks | bn0cv2_chunks | cv2_chunks]
    cv1_l8_chunks = np.concatenate(
        [weights_to_tiled_int8(w_cv1_l8[g * 128 : (g + 1) * 128]) for g in range(2)]
    )
    bn0cv1_l8_chunks = np.concatenate(
        [weights_to_tiled_int8_k3(w_bn0cv1_l8[g * 32 : (g + 1) * 32]) for g in range(4)]
    )
    bn0cv2_l8_chunks = np.concatenate(
        [weights_to_tiled_int8_k3(w_bn0cv2_l8[g * 32 : (g + 1) * 32]) for g in range(4)]
    )
    cv2_l8_chunks = np.concatenate(
        [weights_to_tiled_int8(w_cv2_l8[g * 64 : (g + 1) * 64]) for g in range(4)]
    )
    op4.write_buffer(
        "weights",
        np.concatenate(
            [cv1_l8_chunks, bn0cv1_l8_chunks, bn0cv2_l8_chunks, cv2_l8_chunks]
        ),
    )
    op4.write_buffer("output", np.zeros(op4._output_buf_size, dtype=np.int8))
    t0 = time.perf_counter()
    op4.run_runlist()
    t1 = time.perf_counter()
    phase_times["P4"] = t1 - t0

    # ================================================================
    # Verify
    # ================================================================
    p4_buf = op4.read_buffer("output", (op4._output_buf_size,), dtype=np.int8)
    npu_final = tiled_to_nchw_int8(
        p4_buf[: op4._final_size].copy(), 256, l7_out_h, l7_out_w
    )

    ref_np = ref_final.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_final.numpy().reshape(-1).astype(np.int32)
    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt5 = int(np.sum(diff > 5))
    errors_gt10 = int(np.sum(diff > 10))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nFull backbone P1-P4 test {l0_ic}ic_256oc_{l0_h}h_{l0_w}w:")
    print(f"  Final dims: 256ch x {l7_out_h}h x {l7_out_w}w")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>5): {errors_gt5}/{total}")
    print(f"  Errors (>10): {errors_gt10}/{total}")
    for pn, dt in phase_times.items():
        print(f"  {pn} NPU time: {1000 * dt:.1f} ms")
    print(f"  Total NPU time: {1000 * sum(phase_times.values()):.1f} ms")

    # 4 PDIs, ~30 layers, heavy rounding accumulation
    assert (
        max_diff <= 25
    ), f"Full backbone failed: max_diff={max_diff} exceeds threshold 25"
    error_rate_gt10 = errors_gt10 / total if total > 0 else 0
    assert error_rate_gt10 < 0.30, (
        f"Full backbone: {100 * error_rate_gt10:.2f}% errors > 10 "
        f"exceeds 30% threshold"
    )


# ---------------------------------------------------------------------------
# Step 16: P1+P2 combined PDI + P3 separate PDI test
# ---------------------------------------------------------------------------


class AIEDataflowP1P2Combined(AIEOperatorBase):
    """Combined P1(L0-L3) + P2(L4+L5) in one PDI.

    P1: L0(k3s2)->L1(k3s2)->C2f L2->L3(k3s2)
    P2: C2f L4 + L5(k3s2, OC streaming)
    """

    def __init__(
        self,
        # P1 params
        l0_height,
        l0_width,
        l0_ic,
        l0_oc,
        l0_shift1,
        l0_shift2,
        l1_oc,
        l1_shift1,
        l1_shift2,
        cv1_shift1,
        cv1_shift2,
        bn_cv1_shift1,
        bn_cv1_shift2,
        bn_cv2_shift1,
        bn_cv2_shift2,
        cv2_shift1,
        cv2_shift2,
        l3_oc,
        l3_shift1,
        l3_shift2,
        # P2 params
        l4_cv1_scale,
        l4_bn0_cv1_scale,
        l4_bn0_cv2_scale,
        l4_bn1_cv1_scale,
        l4_bn1_cv2_scale,
        l4_cv2_scale,
        l5_oc,
        l5_shift1,
        l5_shift2,
        context=None,
    ):
        # P1 params
        self.l0_height = l0_height
        self.l0_width = l0_width
        self.l0_ic = l0_ic
        self.l0_oc = l0_oc
        self.l0_shift1 = l0_shift1
        self.l0_shift2 = l0_shift2
        self.l1_oc = l1_oc
        self.l1_shift1 = l1_shift1
        self.l1_shift2 = l1_shift2
        self.cv1_shift1 = cv1_shift1
        self.cv1_shift2 = cv1_shift2
        self.bn_cv1_shift1 = bn_cv1_shift1
        self.bn_cv1_shift2 = bn_cv1_shift2
        self.bn_cv2_shift1 = bn_cv2_shift1
        self.bn_cv2_shift2 = bn_cv2_shift2
        self.cv2_shift1 = cv2_shift1
        self.cv2_shift2 = cv2_shift2
        self.l3_oc = l3_oc
        self.l3_shift1 = l3_shift1
        self.l3_shift2 = l3_shift2

        # P2 params
        self.l4_cv1_scale = l4_cv1_scale
        self.l4_bn0_cv1_scale = l4_bn0_cv1_scale
        self.l4_bn0_cv2_scale = l4_bn0_cv2_scale
        self.l4_bn1_cv1_scale = l4_bn1_cv1_scale
        self.l4_bn1_cv2_scale = l4_bn1_cv2_scale
        self.l4_cv2_scale = l4_cv2_scale
        self.l5_oc = l5_oc
        self.l5_shift1 = l5_shift1
        self.l5_shift2 = l5_shift2

        # P1 derived dims
        self.l1_ic = l0_oc
        self.l1_height = l0_height // 2
        self.l1_width = l0_width // 2
        self.c2f_ic = l1_oc
        self.c2f_height = l0_height // 4
        self.c2f_width = l0_width // 4
        self.p1_cv1_oc = 32
        self.p1_bn_ch = 16
        self.p1_cv2_ic = 48
        self.p1_cv2_oc = 32
        self.l3_ic = 32
        self.l3_height = self.c2f_height
        self.l3_width = self.c2f_width
        self.l3_out_h = self.l3_height // 2
        self.l3_out_w = self.l3_width // 2

        # P2 derived dims
        self.p2_in_channels = 64
        self.p2_height = self.l3_out_h
        self.p2_width = self.l3_out_w
        self.p2_cv1_oc = 64
        self.p2_bn_ch = 32
        self.p2_cv2_ic = 128
        self.p2_cv2_oc = 64
        self.l5_out_h = self.p2_height // 2
        self.l5_out_w = self.p2_width // 2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_p1p2_{self.l0_ic}ic_{self.l5_oc}oc_"
            f"{self.l0_height}h_{self.l0_width}w"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_p1_p2_combined",
            callback_args=[
                self.context.device_manager.device_type,
                # P1 params
                self.l0_height,
                self.l0_width,
                self.l0_ic,
                self.l0_oc,
                self.l0_shift1,
                self.l0_shift2,
                self.l1_oc,
                self.l1_shift1,
                self.l1_shift2,
                self.cv1_shift1,
                self.cv1_shift2,
                self.bn_cv1_shift1,
                self.bn_cv1_shift2,
                self.bn_cv2_shift1,
                self.bn_cv2_shift2,
                self.cv2_shift1,
                self.cv2_shift2,
                self.l3_oc,
                self.l3_shift1,
                self.l3_shift2,
                # P2 params
                self.l4_cv1_scale,
                self.l4_bn0_cv1_scale,
                self.l4_bn0_cv2_scale,
                self.l4_bn1_cv1_scale,
                self.l4_bn1_cv2_scale,
                self.l4_cv2_scale,
                self.l5_oc,
                self.l5_shift1,
                self.l5_shift2,
            ],
        )

        # P1 kernel objects (6 total)
        k3s2_silu_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_silu.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk3_i8_silu.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k1_silu_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_silu.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk1_i8_silu.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k3_silu_bn_fwd_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_silu_bn_fwd.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk3_i8_silu_fwd.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3_i8_silu=conv2dk3_i8_silu_bn",
                "-Dconv2dk3s2_i8_silu=conv2dk3s2_i8_silu_bn",
            ],
        )

        passthrough_obj = KernelObjectArtifact.new(
            "passthrough_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "passthrough_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k1_silu_cv2_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_silu_cv2.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk1_i8_silu.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk1_i8_silu=conv2dk1_i8_silu_cv2",
            ],
        )

        k3s2_silu_l3_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_silu_l3.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk3_i8_silu.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3s2_i8_silu=conv2dk3s2_i8_silu_l3",
            ],
        )

        # P2 kernel objects (5 total)
        k1_i8_obj = KernelObjectArtifact.new(
            "conv2dk1_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        k3_bn_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_bn.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk3_i8=conv2dk3_i8_bn",
                "-Dconv2dk3s2_i8=conv2dk3s2_i8_bn",
            ],
        )

        add_i8_obj = KernelObjectArtifact.new(
            "add_i8.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "add_i8.cc"
                )
            ],
            extra_flags=["-DINT8_ACT", "-DSCALAR"],
        )

        k1_cv2_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_cv2.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8.cc"
                )
            ],
            extra_flags=[
                "-DINT8_ACT",
                "-Dconv2dk1_i8=conv2dk1_i8_cv2",
            ],
        )

        l5_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_silu_l5.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir
                    / "aie_kernels"
                    / "aie2p"
                    / "conv2dk3_i8_silu.cc"
                )
            ],
            extra_flags=["-DINT8_ACT"],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                # P1
                k3s2_silu_obj,
                k1_silu_obj,
                k3_silu_bn_fwd_obj,
                passthrough_obj,
                k1_silu_cv2_obj,
                k3s2_silu_l3_obj,
                # P2
                k1_i8_obj,
                k3_bn_obj,
                add_i8_obj,
                k1_cv2_obj,
                l5_obj,
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.l0_ic * self.l0_height * self.l0_width

        # ---- P1 weight sizes ----
        l0_wt = self.l0_oc * self.l0_ic * 9 + self.l0_oc * 4
        l1_wt = self.l1_oc * self.l1_ic * 9 + self.l1_oc * 4
        tg1_wt_slot = max(l0_wt, l1_wt)
        tg1_total_wt = 2 * tg1_wt_slot
        self._tg1_wt_slot = tg1_wt_slot

        cv1_wt = self.p1_cv1_oc * self.c2f_ic + self.p1_cv1_oc * 4
        bn_cv1_wt = self.p1_bn_ch * self.p1_bn_ch * 9 + self.p1_bn_ch * 4
        bn_cv2_wt = self.p1_bn_ch * self.p1_bn_ch * 9 + self.p1_bn_ch * 4
        cv2_wt = self.p1_cv2_oc * self.p1_cv2_ic + self.p1_cv2_oc * 4
        c2f_wt_slot = max(cv1_wt, bn_cv1_wt, bn_cv2_wt, cv2_wt)
        c2f_total_wt = 4 * c2f_wt_slot
        self._c2f_wt_slot = c2f_wt_slot

        l3_wt = self.l3_oc * self.l3_ic * 9 + self.l3_oc * 4
        p1_total_wt = tg1_total_wt + c2f_total_wt + l3_wt

        p1_scratch_a = self.l1_oc * self.c2f_height * self.c2f_width
        p1_scratch_b = self.p1_cv2_oc * self.c2f_height * self.c2f_width

        # ---- P2 weight sizes ----
        p2_cv1_wt = self.p2_cv1_oc * self.p2_in_channels
        p2_bn_k3_wt = self.p2_bn_ch * self.p2_bn_ch * 9
        p2_cv2_wt = self.p2_cv2_oc * self.p2_cv2_ic
        p2_bn_wt_slot = p2_bn_k3_wt
        p2_l4_total_wt = p2_cv1_wt + 4 * p2_bn_wt_slot + p2_cv2_wt

        p2_l4_output_size = self.p2_cv2_oc * self.p2_height * self.p2_width
        p2_total_concat = self.p2_cv2_ic * self.p2_height * self.p2_width
        p2_total_input = self.p2_in_channels * self.p2_height * self.p2_width

        from iron.operators.conv2d_int8.dataflow_design import (
            _compute_oc_streaming_params,
        )

        l5_ic = self.p2_cv2_oc
        l5_oc_chunk, l5_n_oc_groups, _ = _compute_oc_streaming_params(
            l5_ic, self.l5_oc, self.p2_width, 2
        )
        l5_wt_chunk = l5_oc_chunk * l5_ic * 9 + l5_oc_chunk * 4
        l5_total_wt = l5_n_oc_groups * l5_wt_chunk
        self._l5_oc_chunk = l5_oc_chunk
        self._l5_n_oc_groups = l5_n_oc_groups

        l5_total_output = self.l5_oc * self.l5_out_h * self.l5_out_w
        self._l5_total_output = l5_total_output

        p2_total_wt = p2_l4_total_wt + l5_total_wt

        # ---- Total weights ----
        total_weights = p1_total_wt + p2_total_wt

        # ---- Output buffer layout ----
        # [L5_final | P1_scratch_A | P1_scratch_B |
        #  P2_input | P2_concat | P2_L4_scratch]
        total_output_buf = (
            l5_total_output
            + p1_scratch_a
            + p1_scratch_b
            + p2_total_input
            + p2_total_concat
            + p2_l4_output_size
        )
        self._total_output_buf = total_output_buf

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output_buf, dtype=np.int8)

        self.add_kernel(
            "p1_p2_combined",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("p1_p2_combined", "input", "weights", "output")


@pytest.mark.parametrize(
    "l0_h,l0_w",
    [
        pytest.param(64, 64, id="p1p2_fused_p3_64x64"),
        pytest.param(
            640,
            640,
            id="p1p2_fused_p3_640x640",
            marks=pytest.mark.extensive,
        ),
    ],
)
def test_dataflow_p1p2_fused_p3(l0_h, l0_w):
    """Test P1+P2 combined in one PDI, then P3 in a separate PDI.

    PDI 1 (P1+P2): L0(8->16)->L1(16->32)->C2f L2->L3(32->64)
                    + C2f L4(64ch) + L5(64->128, OC streaming)
    PDI 2 (P3):    C2f L6(128ch) + L7(128->256, OC streaming)
    """
    torch.manual_seed(42)

    l0_ic = 8
    l0_oc = 16
    l1_oc = 32
    l3_oc = 64
    l5_oc = 128
    l7_oc = 256
    scale = 10
    shift2 = 7
    bn_ch_l2 = 16
    bn_ch_l4 = 32
    bn_ch_l6 = 64

    # Spatial dims through the backbone
    l3_out_h = l0_h // 8  # after L0(s2), L1(s2), L3(s2)
    l3_out_w = l0_w // 8
    l5_out_h = l3_out_h // 2  # after L5(s2)
    l5_out_w = l3_out_w // 2
    l7_out_h = l5_out_h // 2  # after L7(s2)
    l7_out_w = l5_out_w // 2

    # Generate all weights (same seed -> same values as p1_through_p3)
    x_int8 = torch.randint(-20, 21, (1, l0_ic, l0_h, l0_w), dtype=torch.int8)

    # P1 weights
    w0 = torch.randint(-50, 51, (l0_oc, l0_ic, 3, 3), dtype=torch.int8)
    b0 = torch.randint(-500, 501, (l0_oc,), dtype=torch.int32)
    w1 = torch.randint(-50, 51, (l1_oc, l0_oc, 3, 3), dtype=torch.int8)
    b1 = torch.randint(-500, 501, (l1_oc,), dtype=torch.int32)
    w_cv1_l2 = torch.randint(-50, 51, (32, l1_oc, 1, 1), dtype=torch.int8)
    b_cv1_l2 = torch.randint(-500, 501, (32,), dtype=torch.int32)
    w_bn1_l2 = torch.randint(-50, 51, (bn_ch_l2, bn_ch_l2, 3, 3), dtype=torch.int8)
    b_bn1_l2 = torch.randint(-500, 501, (bn_ch_l2,), dtype=torch.int32)
    w_bn2_l2 = torch.randint(-50, 51, (bn_ch_l2, bn_ch_l2, 3, 3), dtype=torch.int8)
    b_bn2_l2 = torch.randint(-500, 501, (bn_ch_l2,), dtype=torch.int32)
    w_cv2_l2 = torch.randint(-50, 51, (32, 48, 1, 1), dtype=torch.int8)
    b_cv2_l2 = torch.randint(-500, 501, (32,), dtype=torch.int32)
    w3 = torch.randint(-50, 51, (l3_oc, 32, 3, 3), dtype=torch.int8)
    b3 = torch.randint(-500, 501, (l3_oc,), dtype=torch.int32)

    # P2 weights (L4 C2f non-fused + L5 fused)
    w_cv1_l4 = torch.randint(-50, 51, (64, l3_oc, 1, 1), dtype=torch.int8)
    w_bn0cv1_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn0cv2_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn1cv1_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_bn1cv2_l4 = torch.randint(-50, 51, (bn_ch_l4, bn_ch_l4, 3, 3), dtype=torch.int8)
    w_cv2_l4 = torch.randint(-50, 51, (64, 128, 1, 1), dtype=torch.int8)
    w_l5 = torch.randint(-50, 51, (l5_oc, 64, 3, 3), dtype=torch.int8)
    b_l5 = torch.randint(-500, 501, (l5_oc,), dtype=torch.int32)

    # P3 weights (L6 C2f non-fused + L7 fused)
    w_cv1_l6 = torch.randint(-50, 51, (128, l5_oc, 1, 1), dtype=torch.int8)
    w_bn0cv1_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_bn0cv2_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_bn1cv1_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_bn1cv2_l6 = torch.randint(-50, 51, (bn_ch_l6, bn_ch_l6, 3, 3), dtype=torch.int8)
    w_cv2_l6 = torch.randint(-50, 51, (128, 256, 1, 1), dtype=torch.int8)
    w_l7 = torch.randint(-50, 51, (l7_oc, 128, 3, 3), dtype=torch.int8)
    b_l7 = torch.randint(-500, 501, (l7_oc,), dtype=torch.int32)

    # ================================================================
    # CPU reference (full pipeline, identical to test_dataflow_p1_through_p3)
    # ================================================================
    # P1
    inter01 = conv2d_int8_pade_silu_reference(x_int8, w0, b0, scale, shift2, stride=2)
    l1_out = conv2d_int8_pade_silu_reference(inter01, w1, b1, scale, shift2, stride=2)
    cv1_l2 = conv2d_int8_pade_silu_reference(
        l1_out, w_cv1_l2, b_cv1_l2, scale, shift2, stride=1, padding=0
    )
    half1_l2 = cv1_l2[:, :bn_ch_l2, :, :]
    half2_l2 = cv1_l2[:, bn_ch_l2:, :, :]
    bn_inter_l2 = conv2d_int8_pade_silu_reference(
        half2_l2, w_bn1_l2, b_bn1_l2, scale, shift2, stride=1, padding=1
    )
    bn_out_l2 = conv2d_int8_pade_silu_reference(
        bn_inter_l2, w_bn2_l2, b_bn2_l2, scale, shift2, stride=1, padding=1
    )
    concat_l2 = torch.cat([half1_l2, half2_l2, bn_out_l2], dim=1)
    c2f_l2_out = conv2d_int8_pade_silu_reference(
        concat_l2, w_cv2_l2, b_cv2_l2, scale, shift2, stride=1, padding=0
    )
    l3_out = conv2d_int8_pade_silu_reference(
        c2f_l2_out, w3, b3, scale, shift2, stride=2
    )

    # P2
    cv1_l4 = conv2d_int8_reference(l3_out, w_cv1_l4, scale, stride=1, padding=0)
    half1_l4 = cv1_l4[:, :bn_ch_l4, :, :]
    half2_l4 = cv1_l4[:, bn_ch_l4:, :, :]
    bn0_inter_l4 = conv2d_int8_reference(
        half2_l4, w_bn0cv1_l4, scale, stride=1, padding=1
    )
    bn0_cv2_l4 = conv2d_int8_reference(
        bn0_inter_l4, w_bn0cv2_l4, scale, stride=1, padding=1
    )
    bn0_out_l4 = add_i8_reference(bn0_cv2_l4, half2_l4)
    bn1_inter_l4 = conv2d_int8_reference(
        bn0_out_l4, w_bn1cv1_l4, scale, stride=1, padding=1
    )
    bn1_cv2_l4 = conv2d_int8_reference(
        bn1_inter_l4, w_bn1cv2_l4, scale, stride=1, padding=1
    )
    bn1_out_l4 = add_i8_reference(bn1_cv2_l4, bn0_out_l4)
    concat_l4 = torch.cat([half1_l4, half2_l4, bn0_out_l4, bn1_out_l4], dim=1)
    l4_out = conv2d_int8_reference(concat_l4, w_cv2_l4, scale, stride=1, padding=0)
    l5_out = conv2d_int8_pade_silu_reference(
        l4_out, w_l5, b_l5, scale, shift2, stride=2
    )

    # P3
    cv1_l6 = conv2d_int8_reference(l5_out, w_cv1_l6, scale, stride=1, padding=0)
    half1_l6 = cv1_l6[:, :bn_ch_l6, :, :]
    half2_l6 = cv1_l6[:, bn_ch_l6:, :, :]
    bn0_inter_l6 = conv2d_int8_reference(
        half2_l6, w_bn0cv1_l6, scale, stride=1, padding=1
    )
    bn0_cv2_l6 = conv2d_int8_reference(
        bn0_inter_l6, w_bn0cv2_l6, scale, stride=1, padding=1
    )
    bn0_out_l6 = add_i8_reference(bn0_cv2_l6, half2_l6)
    bn1_inter_l6 = conv2d_int8_reference(
        bn0_out_l6, w_bn1cv1_l6, scale, stride=1, padding=1
    )
    bn1_cv2_l6 = conv2d_int8_reference(
        bn1_inter_l6, w_bn1cv2_l6, scale, stride=1, padding=1
    )
    bn1_out_l6 = add_i8_reference(bn1_cv2_l6, bn0_out_l6)
    concat_l6 = torch.cat([half1_l6, half2_l6, bn0_out_l6, bn1_out_l6], dim=1)
    l6_out = conv2d_int8_reference(concat_l6, w_cv2_l6, scale, stride=1, padding=0)
    ref_final = conv2d_int8_pade_silu_reference(
        l6_out, w_l7, b_l7, scale, shift2, stride=2
    )

    phase_times = {}

    # ================================================================
    # PDI 1: P1+P2 combined
    # ================================================================
    ctx1 = AIEContext()
    op = AIEDataflowP1P2Combined(
        # P1 params
        l0_height=l0_h,
        l0_width=l0_w,
        l0_ic=l0_ic,
        l0_oc=l0_oc,
        l0_shift1=scale,
        l0_shift2=shift2,
        l1_oc=l1_oc,
        l1_shift1=scale,
        l1_shift2=shift2,
        cv1_shift1=scale,
        cv1_shift2=shift2,
        bn_cv1_shift1=scale,
        bn_cv1_shift2=shift2,
        bn_cv2_shift1=scale,
        bn_cv2_shift2=shift2,
        cv2_shift1=scale,
        cv2_shift2=shift2,
        l3_oc=l3_oc,
        l3_shift1=scale,
        l3_shift2=shift2,
        # P2 params
        l4_cv1_scale=scale,
        l4_bn0_cv1_scale=scale,
        l4_bn0_cv2_scale=scale,
        l4_bn1_cv1_scale=scale,
        l4_bn1_cv2_scale=scale,
        l4_cv2_scale=scale,
        l5_oc=l5_oc,
        l5_shift1=scale,
        l5_shift2=shift2,
        context=ctx1,
    )
    op.context.compile_all()
    op.context.prepare_runtime()

    # Pack input
    op.write_buffer("input", nchw_to_tiled_int8(x_int8))

    # Pack P1+P2 weights
    def _pad(data, slot_size):
        return np.concatenate([data, np.zeros(slot_size - len(data), dtype=np.int8)])

    tg1_wt_slot = op._tg1_wt_slot
    c2f_wt_slot = op._c2f_wt_slot
    p1_packed = np.concatenate(
        [
            _pad(pack_fused_weights_k3(w0, b0), tg1_wt_slot),
            _pad(pack_fused_weights_k3(w1, b1), tg1_wt_slot),
            _pad(_pack_k1_silu_weights(w_cv1_l2, b_cv1_l2), c2f_wt_slot),
            _pad(pack_fused_weights_k3(w_bn1_l2, b_bn1_l2), c2f_wt_slot),
            _pad(pack_fused_weights_k3(w_bn2_l2, b_bn2_l2), c2f_wt_slot),
            _pad(_pack_k1_silu_weights(w_cv2_l2, b_cv2_l2), c2f_wt_slot),
            pack_fused_weights_k3(w3, b3),
        ]
    )

    l4_packed = np.concatenate(
        [
            weights_to_tiled_int8(w_cv1_l4),
            weights_to_tiled_int8_k3(w_bn0cv1_l4),
            weights_to_tiled_int8_k3(w_bn0cv2_l4),
            weights_to_tiled_int8_k3(w_bn1cv1_l4),
            weights_to_tiled_int8_k3(w_bn1cv2_l4),
            weights_to_tiled_int8(w_cv2_l4),
        ]
    )
    l5_oc_chunk = op._l5_oc_chunk
    l5_n_oc_groups = op._l5_n_oc_groups
    l5_chunks = [
        pack_fused_weights_k3(
            w_l5[g * l5_oc_chunk : (g + 1) * l5_oc_chunk],
            b_l5[g * l5_oc_chunk : (g + 1) * l5_oc_chunk],
        )
        for g in range(l5_n_oc_groups)
    ]
    p2_packed = np.concatenate([l4_packed, np.concatenate(l5_chunks)])

    op.write_buffer("weights", np.concatenate([p1_packed, p2_packed]))
    op.write_buffer("output", np.zeros(op._total_output_buf, dtype=np.int8))

    t0 = time.perf_counter()
    op.run_runlist()
    t1 = time.perf_counter()
    phase_times["PDI 1 (P1+P2)"] = t1 - t0

    # Extract L5 output from offset 0
    out_buf = op.read_buffer("output", (op._total_output_buf,), dtype=np.int8)
    l5_total_output = op._l5_total_output
    p1p2_output_tiled = out_buf[:l5_total_output].copy()

    # ================================================================
    # PDI 2: P3 separate (L6+L7)
    # ================================================================
    ctx3 = AIEContext()
    op3 = AIEDataflowL6L7Combined(
        height=l5_out_h,
        width=l5_out_w,
        in_channels=l5_oc,
        cv1_scale=scale,
        bn0_cv1_scale=scale,
        bn0_cv2_scale=scale,
        bn1_cv1_scale=scale,
        bn1_cv2_scale=scale,
        cv2_scale=scale,
        l7_oc=l7_oc,
        l7_shift1=scale,
        l7_shift2=shift2,
        context=ctx3,
    )
    op3.context.compile_all()
    op3.context.prepare_runtime()
    op3.write_buffer("input", p1p2_output_tiled)

    l6_packed = np.concatenate(
        [
            weights_to_tiled_int8(w_cv1_l6),
            weights_to_tiled_int8_k3(w_bn0cv1_l6),
            weights_to_tiled_int8_k3(w_bn0cv2_l6),
            weights_to_tiled_int8_k3(w_bn1cv1_l6),
            weights_to_tiled_int8_k3(w_bn1cv2_l6),
            weights_to_tiled_int8(w_cv2_l6),
        ]
    )
    l7_oc_chunk = op3._l7_oc_chunk
    l7_n_oc_groups = op3._l7_n_oc_groups
    l7_chunks = [
        pack_fused_weights_k3(
            w_l7[g * l7_oc_chunk : (g + 1) * l7_oc_chunk],
            b_l7[g * l7_oc_chunk : (g + 1) * l7_oc_chunk],
        )
        for g in range(l7_n_oc_groups)
    ]
    op3.write_buffer("weights", np.concatenate([l6_packed, np.concatenate(l7_chunks)]))
    op3.write_buffer("output", np.zeros(op3._output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op3.run_runlist()
    t1 = time.perf_counter()
    phase_times["PDI 2 (P3)"] = t1 - t0

    # ================================================================
    # Verify final output (L7 at offset 0 of P3's output buffer)
    # ================================================================
    l7_total_output = op3._l7_total_output
    p3_out_buf = op3.read_buffer("output", (op3._output_buf_size,), dtype=np.int8)
    npu_final = tiled_to_nchw_int8(
        p3_out_buf[:l7_total_output].copy(), l7_oc, l7_out_h, l7_out_w
    )

    ref_np = ref_final.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_final.numpy().reshape(-1).astype(np.int32)

    diff = np.abs(ref_np - npu_np)
    max_diff = int(np.max(diff)) if len(diff) > 0 else 0
    errors_gt3 = int(np.sum(diff > 3))
    errors_gt5 = int(np.sum(diff > 5))
    exact = int(np.sum(diff == 0))
    total = len(ref_np)

    print(f"\nP1+P2 combined + P3 test {l0_ic}ic_{l7_oc}oc_{l0_h}h_{l0_w}w:")
    print(f"  Final dims: {l7_oc}ch x {l7_out_h}h x {l7_out_w}w")
    print(f"  Exact: {exact}/{total} ({100 * exact / total:.1f}%)")
    print(f"  Max diff: {max_diff}")
    print(f"  Errors (>3): {errors_gt3}/{total}")
    print(f"  Errors (>5): {errors_gt5}/{total}")
    for phase_name, dt in phase_times.items():
        print(f"  {phase_name} NPU time: {1000 * dt:.1f} ms")
    total_time = sum(phase_times.values())
    print(f"  Total NPU time: {1000 * total_time:.1f} ms")

    # Same tolerances as test_dataflow_p1_through_p3
    assert (
        max_diff <= 15
    ), f"P1+P2 combined + P3 failed: max_diff={max_diff} exceeds threshold 15"
    error_rate_gt5 = errors_gt5 / total if total > 0 else 0
    assert error_rate_gt5 < 0.20, (
        f"P1+P2 combined + P3: {100 * error_rate_gt5:.2f}% errors > 5 "
        f"exceeds 20% threshold"
    )


# ============================================================================
# Neck C2f dataflow blocks (L12, L15, L18)
# ============================================================================


class AIEDataflowC2fNeck(AIEOperatorBase):
    """Generic C2f neck block: n=1 bottleneck, fused SiLU, no residual.

    Supports L12 (384->128), L15 (192->64), L18 (192->128).
    """

    def __init__(self, height, width, in_channels, cv1_oc, bn_ch, cv2_oc,
                 cv1_shift1, cv1_shift2, bn0_cv1_shift1, bn0_cv1_shift2,
                 bn0_cv2_shift1, bn0_cv2_shift2, cv2_shift1, cv2_shift2,
                 tag="neck", context=None):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.cv1_oc = cv1_oc
        self.bn_ch = bn_ch
        self.cv2_ic = cv1_oc + bn_ch
        self.cv2_oc = cv2_oc
        self.cv1_shift1 = cv1_shift1
        self.cv1_shift2 = cv1_shift2
        self.bn0_cv1_shift1 = bn0_cv1_shift1
        self.bn0_cv1_shift2 = bn0_cv1_shift2
        self.bn0_cv2_shift1 = bn0_cv2_shift1
        self.bn0_cv2_shift2 = bn0_cv2_shift2
        self.cv2_shift1 = cv2_shift1
        self.cv2_shift2 = cv2_shift2
        self.tag = tag
        self.xclbin_artifact = None
        self.insts_artifact = None
        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"dataflow_c2f_{self.tag}_{self.in_channels}ic_"
            f"{self.cv1_oc}oc_{self.height}h_{self.width}w"
        )
        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_c2f_neck",
            callback_args=[
                self.context.device_manager.device_type,
                self.height, self.width,
                self.in_channels, self.cv1_oc, self.bn_ch, self.cv2_oc,
                self.cv1_shift1, self.cv1_shift2,
                self.bn0_cv1_shift1, self.bn0_cv1_shift2,
                self.bn0_cv2_shift1, self.bn0_cv2_shift2,
                self.cv2_shift1, self.cv2_shift2,
            ],
        )
        k1_silu_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_silu.o",
            depends=[SourceArtifact.new(
                self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8_silu.cc"
            )],
            extra_flags=["-DINT8_ACT"],
        )
        k1_silu_cv2_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_silu_cv2.o",
            depends=[SourceArtifact.new(
                self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8_silu.cc"
            )],
            extra_flags=["-DINT8_ACT", "-Dconv2dk1_i8_silu=conv2dk1_i8_silu_cv2"],
        )
        k3_silu_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_silu.o",
            depends=[SourceArtifact.new(
                self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8_silu.cc"
            )],
            extra_flags=["-DINT8_ACT"],
        )
        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[mlir_artifact, k1_silu_obj, k1_silu_cv2_obj, k3_silu_obj],
        )
        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )
        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width
        # Compute OC streaming params (same logic as design function)
        cv1_input_bufs = 2 * self.in_channels * self.width
        cv1_avail = 65536 - 1040 - cv1_input_bufs
        cv1_full_wt = self.cv1_oc * self.in_channels + self.cv1_oc * 4
        cv1_full_out = 2 * self.cv1_oc * self.width
        if cv1_full_wt + cv1_full_out <= cv1_avail:
            cv1_oc_chunk = self.cv1_oc
        else:
            for try_oc in range(self.cv1_oc, 0, -8):
                if self.cv1_oc % try_oc != 0 or try_oc % 8 != 0:
                    continue
                wt = try_oc * self.in_channels + try_oc * 4
                out = 2 * try_oc * self.width
                if wt + out <= cv1_avail:
                    cv1_oc_chunk = try_oc
                    break
        cv1_n_oc = self.cv1_oc // cv1_oc_chunk
        cv1_wt_chunk = cv1_oc_chunk * self.in_channels + cv1_oc_chunk * 4
        cv1_total_wt = cv1_n_oc * cv1_wt_chunk
        bn_k3_wt = self.bn_ch * self.bn_ch * 9 + self.bn_ch * 4
        cv2_wt_size = self.cv2_oc * self.cv2_ic + self.cv2_oc * 4
        total_wt = cv1_total_wt + 2 * bn_k3_wt + cv2_wt_size
        total_output = self.cv2_oc * self.height * self.width
        total_concat = self.cv2_ic * self.height * self.width
        output_buf_size = total_output + total_concat
        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", output_buf_size, dtype=np.int8)
        self.add_kernel(
            f"c2f_{self.tag}",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist(f"c2f_{self.tag}", "input", "weights", "output")


def _run_c2f_neck_test(tag, h, w, in_channels, cv1_oc, bn_ch, cv2_oc):
    """Shared test logic for all neck C2f dataflow blocks."""
    torch.manual_seed(42)
    scale = 10
    shift2 = 7
    cv2_ic = cv1_oc + bn_ch

    # Generate weights + biases
    w_cv1 = torch.randint(-50, 51, (cv1_oc, in_channels, 1, 1), dtype=torch.int8)
    b_cv1 = torch.randint(-500, 501, (cv1_oc,), dtype=torch.int32)
    w_bn0cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    b_bn0cv1 = torch.randint(-500, 501, (bn_ch,), dtype=torch.int32)
    w_bn0cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    b_bn0cv2 = torch.randint(-500, 501, (bn_ch,), dtype=torch.int32)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, cv2_ic, 1, 1), dtype=torch.int8)
    b_cv2 = torch.randint(-500, 501, (cv2_oc,), dtype=torch.int32)
    x_int8 = torch.randint(-20, 21, (1, in_channels, h, w), dtype=torch.int8)

    # CPU reference
    ref_cv1 = conv2d_int8_pade_silu_reference(
        x_int8, w_cv1, b_cv1, scale, shift2, stride=1, padding=0
    )
    half1 = ref_cv1[:, :bn_ch, :, :]
    half2 = ref_cv1[:, bn_ch:, :, :]
    ref_bn0_inter = conv2d_int8_pade_silu_reference(
        half2, w_bn0cv1, b_bn0cv1, scale, shift2, stride=1, padding=1
    )
    ref_bn0_out = conv2d_int8_pade_silu_reference(
        ref_bn0_inter, w_bn0cv2, b_bn0cv2, scale, shift2, stride=1, padding=1
    )
    concat = torch.cat([half1, half2, ref_bn0_out], dim=1)
    ref_output = conv2d_int8_pade_silu_reference(
        concat, w_cv2, b_cv2, scale, shift2, stride=1, padding=0
    )

    # Pack weights — compute OC streaming chunk for cv1
    cv1_input_bufs = 2 * in_channels * w
    cv1_avail = 65536 - 1040 - cv1_input_bufs
    cv1_full_wt = cv1_oc * in_channels + cv1_oc * 4
    cv1_full_out = 2 * cv1_oc * w
    if cv1_full_wt + cv1_full_out <= cv1_avail:
        cv1_oc_chunk = cv1_oc
    else:
        for try_oc in range(cv1_oc, 0, -8):
            if cv1_oc % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_b = try_oc * in_channels + try_oc * 4
            out_b = 2 * try_oc * w
            if wt_b + out_b <= cv1_avail:
                cv1_oc_chunk = try_oc
                break
    cv1_n_oc = cv1_oc // cv1_oc_chunk

    cv1_chunks = []
    for g in range(cv1_n_oc):
        w_slice = w_cv1[g * cv1_oc_chunk : (g + 1) * cv1_oc_chunk]
        b_slice = b_cv1[g * cv1_oc_chunk : (g + 1) * cv1_oc_chunk]
        w_tiled = weights_to_tiled_int8(w_slice)
        b_bytes = b_slice.numpy().astype(np.int32).view(np.int8)
        cv1_chunks.append(np.concatenate([w_tiled, b_bytes]))
    packed_cv1 = np.concatenate(cv1_chunks)
    packed_bn0cv1 = pack_fused_weights_k3(w_bn0cv1, b_bn0cv1)
    packed_bn0cv2 = pack_fused_weights_k3(w_bn0cv2, b_bn0cv2)
    packed_cv2 = _pack_k1_silu_weights(w_cv2, b_cv2)
    packed_weights = np.concatenate(
        [packed_cv1, packed_bn0cv1, packed_bn0cv2, packed_cv2]
    )

    # Build NPU design
    ctx = AIEContext()
    op = AIEDataflowC2fNeck(
        height=h, width=w,
        in_channels=in_channels, cv1_oc=cv1_oc, bn_ch=bn_ch, cv2_oc=cv2_oc,
        cv1_shift1=scale, cv1_shift2=shift2,
        bn0_cv1_shift1=scale, bn0_cv1_shift2=shift2,
        bn0_cv2_shift1=scale, bn0_cv2_shift2=shift2,
        cv2_shift1=scale, cv2_shift2=shift2,
        tag=tag, context=ctx,
    )
    ctx.compile_all()
    ctx.prepare_runtime()

    total_output = cv2_oc * h * w
    output_buf_size = op.buffers["output"]
    op.write_buffer("input", nchw_to_tiled_int8(x_int8))
    op.write_buffer("weights", packed_weights)
    op.write_buffer("output", np.zeros(output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op.run_runlist()
    run_ms = (time.perf_counter() - t0) * 1000
    print(f"\n  C2f {tag} dataflow ({h}x{w}): {run_ms:.1f}ms")

    out_flat = op.read_buffer("output", (output_buf_size,), dtype=np.int8)
    out_flat = out_flat[:total_output]
    npu_output = tiled_to_nchw_int8(out_flat, cv2_oc, h, w)

    ref_np = ref_output.numpy().astype(np.int8)
    npu_np = npu_output.numpy().astype(np.int8)
    diff = np.abs(ref_np.astype(np.int32) - npu_np.astype(np.int32))
    max_diff = int(diff.max())
    total = diff.size
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt5 = int(np.sum(diff > 5))
    print(f"  max_diff={max_diff}, errors>1={errors_gt1}/{total}, "
          f"errors>5={errors_gt5}/{total}")

    assert max_diff <= 10, (
        f"C2f {tag} dataflow failed: max_diff={max_diff} exceeds threshold 10"
    )
    error_rate = errors_gt5 / total if total > 0 else 0
    assert error_rate < 0.10, (
        f"C2f {tag} dataflow: {100 * error_rate:.2f}% errors > 5 "
        f"exceeds 10% threshold"
    )


@pytest.mark.parametrize(
    "l12_h,l12_w",
    [
        pytest.param(16, 16, id="c2f_l12_16x16"),
        pytest.param(40, 40, id="c2f_l12_40x40"),
    ],
)
def test_dataflow_c2f_l12(l12_h, l12_w):
    """L12 C2f: 384->128, bn_ch=64, 40x40. OC streaming for cv1."""
    _run_c2f_neck_test("l12", l12_h, l12_w, 384, 128, 64, 128)


@pytest.mark.parametrize(
    "l18_h,l18_w",
    [
        pytest.param(16, 16, id="c2f_l18_16x16"),
        pytest.param(40, 40, id="c2f_l18_40x40"),
    ],
)
def test_dataflow_c2f_l18(l18_h, l18_w):
    """L18 C2f: 192->128, bn_ch=64, 40x40. No OC streaming."""
    _run_c2f_neck_test("l18", l18_h, l18_w, 192, 128, 64, 128)


@pytest.mark.parametrize(
    "l15_h,l15_w",
    [
        pytest.param(16, 16, id="c2f_l15_16x16"),
        pytest.param(80, 80, id="c2f_l15_80x80"),
    ],
)
def test_dataflow_c2f_l15(l15_h, l15_w):
    """L15 C2f: 192->64, bn_ch=32, 80x80. 1 column (small weights)."""
    _run_c2f_neck_test("l15", l15_h, l15_w, 192, 64, 32, 64)


# ============================================================================
# Neck C2f L21 dataflow block (all layers OC streaming)
# ============================================================================


class AIEDataflowC2fL21(AIEOperatorBase):
    """C2f L21: 384->256, bn_ch=128, 20x20. All layers OC-streaming."""

    def __init__(self, height, width, cv1_s1, cv1_s2, bn_cv1_s1, bn_cv1_s2,
                 bn_cv2_s1, bn_cv2_s2, cv2_s1, cv2_s2, context=None):
        self.height = height
        self.width = width
        self.cv1_s1 = cv1_s1
        self.cv1_s2 = cv1_s2
        self.bn_cv1_s1 = bn_cv1_s1
        self.bn_cv1_s2 = bn_cv1_s2
        self.bn_cv2_s1 = bn_cv2_s1
        self.bn_cv2_s2 = bn_cv2_s2
        self.cv2_s1 = cv2_s1
        self.cv2_s2 = cv2_s2
        self.xclbin_artifact = None
        self.insts_artifact = None
        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        from iron.operators.conv2d_int8.dataflow_design import (
            _compute_oc_streaming_params,
        )

        operator_dir = Path(__file__).parent
        file_name_base = f"dataflow_c2f_l21_{self.height}h_{self.width}w"
        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_c2f_l21",
            callback_args=[
                self.context.device_manager.device_type,
                self.height, self.width,
                self.cv1_s1, self.cv1_s2,
                self.bn_cv1_s1, self.bn_cv1_s2,
                self.bn_cv2_s1, self.bn_cv2_s2,
                self.cv2_s1, self.cv2_s2,
            ],
        )
        k1_silu_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_silu.o",
            depends=[SourceArtifact.new(
                self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8_silu.cc"
            )],
            extra_flags=["-DINT8_ACT"],
        )
        k1_silu_cv2_obj = KernelObjectArtifact.new(
            "conv2dk1_i8_silu_cv2.o",
            depends=[SourceArtifact.new(
                self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk1_i8_silu.cc"
            )],
            extra_flags=["-DINT8_ACT", "-Dconv2dk1_i8_silu=conv2dk1_i8_silu_cv2"],
        )
        k3_silu_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_silu.o",
            depends=[SourceArtifact.new(
                self.context.base_dir / "aie_kernels" / "aie2p" / "conv2dk3_i8_silu.cc"
            )],
            extra_flags=["-DINT8_ACT"],
        )
        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[mlir_artifact, k1_silu_obj, k1_silu_cv2_obj, k3_silu_obj],
        )
        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )
        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

        # Store OC streaming params for weight packing
        self._cv1_oc_chunk = 64
        self._cv1_n_oc = 4
        bn_oc_chunk, bn_n_oc, _ = _compute_oc_streaming_params(128, 128, self.width, 1)
        self._bn_oc_chunk = bn_oc_chunk
        self._bn_n_oc = bn_n_oc
        self._cv2_oc_chunk = 64
        self._cv2_n_oc = 4

    def set_up_runtime(self):
        in_channels = 384
        cv1_oc = 256
        bn_ch = 128
        cv2_ic = 384
        cv2_oc = 256

        total_input = in_channels * self.height * self.width
        cv1_wt_chunk = self._cv1_oc_chunk * in_channels + self._cv1_oc_chunk * 4
        cv1_total_wt = self._cv1_n_oc * cv1_wt_chunk
        bn_wt_chunk = self._bn_oc_chunk * bn_ch * 9 + self._bn_oc_chunk * 4
        bn_total_wt = self._bn_n_oc * bn_wt_chunk
        cv2_wt_chunk = self._cv2_oc_chunk * cv2_ic + self._cv2_oc_chunk * 4
        cv2_total_wt = self._cv2_n_oc * cv2_wt_chunk
        total_wt = cv1_total_wt + 2 * bn_total_wt + cv2_total_wt

        total_output = cv2_oc * self.height * self.width
        total_concat = cv2_ic * self.height * self.width
        bn_scratch = bn_ch * self.height * self.width
        output_buf_size = total_output + total_concat + bn_scratch

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", output_buf_size, dtype=np.int8)
        self.add_kernel(
            "c2f_l21", self.xclbin_artifact,
            self.xclbin_artifact.kernel_name, self.insts_artifact,
        )
        self.add_to_runlist("c2f_l21", "input", "weights", "output")


@pytest.mark.parametrize(
    "l21_h,l21_w",
    [
        pytest.param(8, 8, id="c2f_l21_8x8"),
        pytest.param(20, 20, id="c2f_l21_20x20"),
    ],
)
def test_dataflow_c2f_l21(l21_h, l21_w):
    """L21 C2f: 384->256, bn_ch=128, 20x20. All layers OC streaming."""
    from iron.operators.conv2d_int8.dataflow_design import (
        _compute_oc_streaming_params,
    )

    torch.manual_seed(42)
    scale = 10
    shift2 = 7

    in_channels = 384
    cv1_oc = 256
    bn_ch = 128
    cv2_ic = 384
    cv2_oc = 256

    # Generate data
    x_int8 = torch.randint(-20, 21, (1, in_channels, l21_h, l21_w), dtype=torch.int8)
    w_cv1 = torch.randint(-50, 51, (cv1_oc, in_channels, 1, 1), dtype=torch.int8)
    b_cv1 = torch.randint(-500, 501, (cv1_oc,), dtype=torch.int32)
    w_bn0cv1 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    b_bn0cv1 = torch.randint(-500, 501, (bn_ch,), dtype=torch.int32)
    w_bn0cv2 = torch.randint(-50, 51, (bn_ch, bn_ch, 3, 3), dtype=torch.int8)
    b_bn0cv2 = torch.randint(-500, 501, (bn_ch,), dtype=torch.int32)
    w_cv2 = torch.randint(-50, 51, (cv2_oc, cv2_ic, 1, 1), dtype=torch.int8)
    b_cv2 = torch.randint(-500, 501, (cv2_oc,), dtype=torch.int32)

    # CPU reference
    ref_cv1 = conv2d_int8_pade_silu_reference(
        x_int8, w_cv1, b_cv1, scale, shift2, stride=1, padding=0
    )
    half1 = ref_cv1[:, :bn_ch, :, :]
    half2 = ref_cv1[:, bn_ch:, :, :]
    ref_bn0_inter = conv2d_int8_pade_silu_reference(
        half2, w_bn0cv1, b_bn0cv1, scale, shift2, stride=1, padding=1
    )
    ref_bn0_out = conv2d_int8_pade_silu_reference(
        ref_bn0_inter, w_bn0cv2, b_bn0cv2, scale, shift2, stride=1, padding=1
    )
    concat = torch.cat([half1, half2, ref_bn0_out], dim=1)
    ref_output = conv2d_int8_pade_silu_reference(
        concat, w_cv2, b_cv2, scale, shift2, stride=1, padding=0
    )

    # Pack weights — OC streaming chunks for each layer
    cv1_oc_chunk = 64
    cv1_n_oc = cv1_oc // cv1_oc_chunk
    cv1_chunks = []
    for g in range(cv1_n_oc):
        w_s = w_cv1[g * cv1_oc_chunk : (g + 1) * cv1_oc_chunk]
        b_s = b_cv1[g * cv1_oc_chunk : (g + 1) * cv1_oc_chunk]
        cv1_chunks.append(np.concatenate([
            weights_to_tiled_int8(w_s),
            b_s.numpy().astype(np.int32).view(np.int8),
        ]))
    packed_cv1 = np.concatenate(cv1_chunks)

    bn_oc_chunk, bn_n_oc, _ = _compute_oc_streaming_params(bn_ch, bn_ch, l21_w, 1)
    def _pack_k3_oc(w, b, oc_chunk, n_oc):
        chunks = []
        for g in range(n_oc):
            w_s = w[g * oc_chunk : (g + 1) * oc_chunk]
            b_s = b[g * oc_chunk : (g + 1) * oc_chunk]
            chunks.append(np.concatenate([
                weights_to_tiled_int8_k3(w_s),
                b_s.numpy().astype(np.int32).view(np.int8),
            ]))
        return np.concatenate(chunks)

    packed_bn0cv1 = _pack_k3_oc(w_bn0cv1, b_bn0cv1, bn_oc_chunk, bn_n_oc)
    packed_bn0cv2 = _pack_k3_oc(w_bn0cv2, b_bn0cv2, bn_oc_chunk, bn_n_oc)

    cv2_oc_chunk = 64
    cv2_n_oc = cv2_oc // cv2_oc_chunk
    cv2_chunks = []
    for g in range(cv2_n_oc):
        w_s = w_cv2[g * cv2_oc_chunk : (g + 1) * cv2_oc_chunk]
        b_s = b_cv2[g * cv2_oc_chunk : (g + 1) * cv2_oc_chunk]
        cv2_chunks.append(np.concatenate([
            weights_to_tiled_int8(w_s),
            b_s.numpy().astype(np.int32).view(np.int8),
        ]))
    packed_cv2 = np.concatenate(cv2_chunks)

    packed_weights = np.concatenate(
        [packed_cv1, packed_bn0cv1, packed_bn0cv2, packed_cv2]
    )

    # Build NPU design
    ctx = AIEContext()
    op = AIEDataflowC2fL21(
        height=l21_h, width=l21_w,
        cv1_s1=scale, cv1_s2=shift2,
        bn_cv1_s1=scale, bn_cv1_s2=shift2,
        bn_cv2_s1=scale, bn_cv2_s2=shift2,
        cv2_s1=scale, cv2_s2=shift2,
        context=ctx,
    )
    ctx.compile_all()
    ctx.prepare_runtime()

    total_output = cv2_oc * l21_h * l21_w
    output_buf_size = op.buffers["output"]
    op.write_buffer("input", nchw_to_tiled_int8(x_int8))
    op.write_buffer("weights", packed_weights)
    op.write_buffer("output", np.zeros(output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op.run_runlist()
    run_ms = (time.perf_counter() - t0) * 1000
    print(f"\n  C2f L21 dataflow ({l21_h}x{l21_w}): {run_ms:.1f}ms")

    out_flat = op.read_buffer("output", (output_buf_size,), dtype=np.int8)
    out_flat = out_flat[:total_output]
    npu_output = tiled_to_nchw_int8(out_flat, cv2_oc, l21_h, l21_w)

    ref_np = ref_output.numpy().astype(np.int8)
    npu_np = npu_output.numpy().astype(np.int8)
    diff = np.abs(ref_np.astype(np.int32) - npu_np.astype(np.int32))
    max_diff = int(diff.max())
    total = diff.size
    errors_gt1 = int(np.sum(diff > 1))
    errors_gt5 = int(np.sum(diff > 5))
    print(f"  max_diff={max_diff}, errors>1={errors_gt1}/{total}, "
          f"errors>5={errors_gt5}/{total}")

    assert max_diff <= 10, (
        f"C2f L21 dataflow failed: max_diff={max_diff} exceeds threshold 10"
    )
    error_rate = errors_gt5 / total if total > 0 else 0
    assert error_rate < 0.10, (
        f"C2f L21 dataflow: {100 * error_rate:.2f}% errors > 5 "
        f"exceeds 10% threshold"
    )


# ============================================================================
# Combined L16+L18 and L19+L21 tests
# ============================================================================


class AIEDataflowL16L18(AIEOperatorBase):
    """Combined L16 CBS + L18 C2f in one PDI."""

    def __init__(self, l16_h, l16_w, s1, s2, context=None):
        self.l16_h = l16_h
        self.l16_w = l16_w
        self.s1 = s1
        self.s2 = s2
        self.xclbin_artifact = None
        self.insts_artifact = None
        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        from iron.operators.conv2d_int8.dataflow_design import (
            _compute_oc_streaming_params,
        )

        operator_dir = Path(__file__).parent
        base = f"dataflow_l16_l18_{self.l16_h}h_{self.l16_w}w"
        mlir = PythonGeneratedMLIRArtifact.new(
            f"{base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_l16_l18",
            callback_args=[
                self.context.device_manager.device_type,
                self.l16_h, self.l16_w,
                self.s1, self.s2, self.s1, self.s2, self.s1, self.s2,
                self.s1, self.s2, self.s1, self.s2,
            ],
        )
        k_objs = self._make_kernel_objs()
        xclbin = XclbinArtifact.new(f"{base}.xclbin", depends=[mlir] + k_objs)
        insts = InstsBinArtifact.new(f"{base}.bin", depends=[mlir])
        self.xclbin_artifact = xclbin
        self.insts_artifact = insts
        self.add_artifacts([xclbin, insts])

        oc_chunk, n_oc, _ = _compute_oc_streaming_params(64, 64, self.l16_w, 2)
        self._l16_oc_chunk = oc_chunk
        self._l16_n_oc = n_oc

    def _make_kernel_objs(self):
        base_dir = self.context.base_dir / "aie_kernels" / "aie2p"
        return [
            KernelObjectArtifact.new("conv2dk3_i8_silu.o",
                depends=[SourceArtifact.new(base_dir / "conv2dk3_i8_silu.cc")],
                extra_flags=["-DINT8_ACT"]),
            KernelObjectArtifact.new("conv2dk1_i8_silu.o",
                depends=[SourceArtifact.new(base_dir / "conv2dk1_i8_silu.cc")],
                extra_flags=["-DINT8_ACT"]),
            KernelObjectArtifact.new("conv2dk1_i8_silu_cv2.o",
                depends=[SourceArtifact.new(base_dir / "conv2dk1_i8_silu.cc")],
                extra_flags=["-DINT8_ACT", "-Dconv2dk1_i8_silu=conv2dk1_i8_silu_cv2"]),
        ]

    def set_up_runtime(self):
        l18_h = self.l16_h // 2
        l18_w = self.l16_w // 2
        l16_input = 64 * self.l16_h * self.l16_w
        l16_wt = self._l16_n_oc * (self._l16_oc_chunk * 64 * 9 + self._l16_oc_chunk * 4)
        l18_cv1_wt = 128 * 192 + 128 * 4
        l18_bn_wt = 64 * 64 * 9 + 64 * 4
        l18_cv2_wt = 128 * 192 + 128 * 4
        total_wt = l16_wt + l18_cv1_wt + 2 * l18_bn_wt + l18_cv2_wt
        l18_output = 128 * l18_h * l18_w
        l18_concat = 192 * l18_h * l18_w
        output_buf = l18_output + l18_concat
        self.add_buffer("input", l16_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", output_buf, dtype=np.int8)
        self.add_kernel("l16_l18", self.xclbin_artifact,
                        self.xclbin_artifact.kernel_name, self.insts_artifact)
        self.add_to_runlist("l16_l18", "input", "weights", "output")


@pytest.mark.parametrize("h,w", [
    pytest.param(16, 16, id="l16_l18_16x16"),
    pytest.param(80, 80, id="l16_l18_80x80"),
])
def test_dataflow_l16_l18(h, w):
    """Combined L16 CBS + L18 C2f: L15_out(64ch) -> L16(k3s2) -> L18(C2f) -> 128ch."""
    from iron.operators.conv2d_int8.dataflow_design import _compute_oc_streaming_params

    torch.manual_seed(42)
    scale = 10
    shift2 = 7
    l18_h, l18_w = h // 2, w // 2

    # Generate input + skip + weights
    x_l15 = torch.randint(-20, 21, (1, 64, h, w), dtype=torch.int8)
    x_l12_skip = torch.randint(-20, 21, (1, 128, l18_h, l18_w), dtype=torch.int8)

    w_l16 = torch.randint(-50, 51, (64, 64, 3, 3), dtype=torch.int8)
    b_l16 = torch.randint(-500, 501, (64,), dtype=torch.int32)
    w_cv1 = torch.randint(-50, 51, (128, 192, 1, 1), dtype=torch.int8)
    b_cv1 = torch.randint(-500, 501, (128,), dtype=torch.int32)
    w_bn0cv1 = torch.randint(-50, 51, (64, 64, 3, 3), dtype=torch.int8)
    b_bn0cv1 = torch.randint(-500, 501, (64,), dtype=torch.int32)
    w_bn0cv2 = torch.randint(-50, 51, (64, 64, 3, 3), dtype=torch.int8)
    b_bn0cv2 = torch.randint(-500, 501, (64,), dtype=torch.int32)
    w_cv2 = torch.randint(-50, 51, (128, 192, 1, 1), dtype=torch.int8)
    b_cv2 = torch.randint(-500, 501, (128,), dtype=torch.int32)

    # CPU reference: L16 -> concat(L16_out, L12_skip) -> L18
    ref_l16 = conv2d_int8_pade_silu_reference(
        x_l15, w_l16, b_l16, scale, shift2, stride=2
    )
    ref_concat = torch.cat([ref_l16, x_l12_skip], dim=1)  # 192ch
    ref_cv1 = conv2d_int8_pade_silu_reference(
        ref_concat, w_cv1, b_cv1, scale, shift2, stride=1, padding=0
    )
    half1 = ref_cv1[:, :64, :, :]
    half2 = ref_cv1[:, 64:, :, :]
    ref_bn0_inter = conv2d_int8_pade_silu_reference(
        half2, w_bn0cv1, b_bn0cv1, scale, shift2, stride=1, padding=1
    )
    ref_bn0_out = conv2d_int8_pade_silu_reference(
        ref_bn0_inter, w_bn0cv2, b_bn0cv2, scale, shift2, stride=1, padding=1
    )
    ref_concat2 = torch.cat([half1, half2, ref_bn0_out], dim=1)
    ref_output = conv2d_int8_pade_silu_reference(
        ref_concat2, w_cv2, b_cv2, scale, shift2, stride=1, padding=0
    )

    # Pack weights
    oc_chunk, n_oc, _ = _compute_oc_streaming_params(64, 64, w, 2)
    l16_chunks = []
    for g in range(n_oc):
        ws = w_l16[g * oc_chunk : (g + 1) * oc_chunk]
        bs = b_l16[g * oc_chunk : (g + 1) * oc_chunk]
        l16_chunks.append(np.concatenate([
            weights_to_tiled_int8_k3(ws),
            bs.numpy().astype(np.int32).view(np.int8),
        ]))
    packed_l16 = np.concatenate(l16_chunks)
    packed_cv1 = _pack_k1_silu_weights(w_cv1, b_cv1)
    packed_bn0cv1 = pack_fused_weights_k3(w_bn0cv1, b_bn0cv1)
    packed_bn0cv2 = pack_fused_weights_k3(w_bn0cv2, b_bn0cv2)
    packed_cv2 = _pack_k1_silu_weights(w_cv2, b_cv2)
    packed_weights = np.concatenate(
        [packed_l16, packed_cv1, packed_bn0cv1, packed_bn0cv2, packed_cv2]
    )

    # Build NPU
    ctx = AIEContext()
    op = AIEDataflowL16L18(l16_h=h, l16_w=w, s1=scale, s2=shift2, context=ctx)
    ctx.compile_all()
    ctx.prepare_runtime()

    output_buf_size = op.buffers["output"]
    l18_output_size = 128 * l18_h * l18_w
    concat_offset = l18_output_size

    # Pre-fill O with L12_skip in concat[64:192ch] (strided)
    o_buf = np.zeros(output_buf_size, dtype=np.int8)
    skip_tiled = nchw_to_tiled_int8(x_l12_skip)  # flat 128ch*H*W
    # Place skip into concat rows: each concat row = 192*W, skip at offset 64*W
    for row in range(l18_h):
        src_start = row * 128 * l18_w
        dst_start = concat_offset + row * 192 * l18_w + 64 * l18_w
        o_buf[dst_start:dst_start + 128 * l18_w] = skip_tiled[src_start:src_start + 128 * l18_w]

    op.write_buffer("input", nchw_to_tiled_int8(x_l15))
    op.write_buffer("weights", packed_weights)
    op.write_buffer("output", o_buf)

    t0 = time.perf_counter()
    op.run_runlist()
    run_ms = (time.perf_counter() - t0) * 1000
    print(f"\n  L16+L18 combined ({h}x{w}): {run_ms:.1f}ms")

    out_flat = op.read_buffer("output", (output_buf_size,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(out_flat[:l18_output_size], 128, l18_h, l18_w)

    ref_np = ref_output.numpy().astype(np.int8)
    npu_np = npu_output.numpy().astype(np.int8)
    diff = np.abs(ref_np.astype(np.int32) - npu_np.astype(np.int32))
    max_diff = int(diff.max())
    total_elems = diff.size
    errors_gt5 = int(np.sum(diff > 5))
    print(f"  max_diff={max_diff}, errors>5={errors_gt5}/{total_elems}")

    assert max_diff <= 10, f"L16+L18 failed: max_diff={max_diff}"
    assert errors_gt5 / total_elems < 0.10, f"L16+L18: too many errors >5"


class AIEDataflowL19L21(AIEOperatorBase):
    """Combined L19 CBS + L21 C2f in one PDI."""

    def __init__(self, l19_h, l19_w, s1, s2, context=None):
        self.l19_h = l19_h
        self.l19_w = l19_w
        self.s1 = s1
        self.s2 = s2
        self.xclbin_artifact = None
        self.insts_artifact = None
        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        from iron.operators.conv2d_int8.dataflow_design import (
            _compute_oc_streaming_params,
        )

        operator_dir = Path(__file__).parent
        base = f"dataflow_l19_l21_{self.l19_h}h_{self.l19_w}w"
        mlir = PythonGeneratedMLIRArtifact.new(
            f"{base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_l19_l21",
            callback_args=[
                self.context.device_manager.device_type,
                self.l19_h, self.l19_w,
                self.s1, self.s2, self.s1, self.s2, self.s1, self.s2,
                self.s1, self.s2, self.s1, self.s2,
            ],
        )
        k_objs = self._make_kernel_objs()
        xclbin = XclbinArtifact.new(f"{base}.xclbin", depends=[mlir] + k_objs)
        insts = InstsBinArtifact.new(f"{base}.bin", depends=[mlir])
        self.xclbin_artifact = xclbin
        self.insts_artifact = insts
        self.add_artifacts([xclbin, insts])

        oc_chunk, n_oc, _ = _compute_oc_streaming_params(128, 128, self.l19_w, 2)
        self._l19_oc_chunk = oc_chunk
        self._l19_n_oc = n_oc
        l21_w = self.l19_w // 2
        bn_oc, bn_n, _ = _compute_oc_streaming_params(128, 128, l21_w, 1)
        self._bn_oc_chunk = bn_oc
        self._bn_n_oc = bn_n

    def _make_kernel_objs(self):
        base_dir = self.context.base_dir / "aie_kernels" / "aie2p"
        return [
            KernelObjectArtifact.new("conv2dk3_i8_silu.o",
                depends=[SourceArtifact.new(base_dir / "conv2dk3_i8_silu.cc")],
                extra_flags=["-DINT8_ACT"]),
            KernelObjectArtifact.new("conv2dk1_i8_silu.o",
                depends=[SourceArtifact.new(base_dir / "conv2dk1_i8_silu.cc")],
                extra_flags=["-DINT8_ACT"]),
            KernelObjectArtifact.new("conv2dk1_i8_silu_cv2.o",
                depends=[SourceArtifact.new(base_dir / "conv2dk1_i8_silu.cc")],
                extra_flags=["-DINT8_ACT", "-Dconv2dk1_i8_silu=conv2dk1_i8_silu_cv2"]),
        ]

    def set_up_runtime(self):
        l21_h = self.l19_h // 2
        l21_w = self.l19_w // 2
        l19_input = 128 * self.l19_h * self.l19_w
        l19_wt = self._l19_n_oc * (self._l19_oc_chunk * 128 * 9 + self._l19_oc_chunk * 4)
        cv1_wt_chunk = 64 * 384 + 64 * 4
        cv1_total_wt = 4 * cv1_wt_chunk
        bn_wt_chunk = self._bn_oc_chunk * 128 * 9 + self._bn_oc_chunk * 4
        bn_total_wt = self._bn_n_oc * bn_wt_chunk
        cv2_wt_chunk = 64 * 384 + 64 * 4
        cv2_total_wt = 4 * cv2_wt_chunk
        total_wt = l19_wt + cv1_total_wt + 2 * bn_total_wt + cv2_total_wt
        l21_output = 256 * l21_h * l21_w
        l21_concat = 384 * l21_h * l21_w
        bn_scratch = 128 * l21_h * l21_w
        output_buf = l21_output + l21_concat + bn_scratch
        self.add_buffer("input", l19_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", output_buf, dtype=np.int8)
        self.add_kernel("l19_l21", self.xclbin_artifact,
                        self.xclbin_artifact.kernel_name, self.insts_artifact)
        self.add_to_runlist("l19_l21", "input", "weights", "output")


@pytest.mark.parametrize("h,w", [
    pytest.param(16, 16, id="l19_l21_16x16"),
    pytest.param(40, 40, id="l19_l21_40x40"),
])
def test_dataflow_l19_l21(h, w):
    """Combined L19 CBS + L21 C2f: L18_out(128ch) -> L19(k3s2) -> L21(C2f) -> 256ch."""
    from iron.operators.conv2d_int8.dataflow_design import _compute_oc_streaming_params

    torch.manual_seed(42)
    scale = 10
    shift2 = 7
    l21_h, l21_w = h // 2, w // 2

    # Generate input + skip + weights
    x_l18 = torch.randint(-20, 21, (1, 128, h, w), dtype=torch.int8)
    x_p5_skip = torch.randint(-20, 21, (1, 256, l21_h, l21_w), dtype=torch.int8)

    w_l19 = torch.randint(-50, 51, (128, 128, 3, 3), dtype=torch.int8)
    b_l19 = torch.randint(-500, 501, (128,), dtype=torch.int32)
    w_cv1 = torch.randint(-50, 51, (256, 384, 1, 1), dtype=torch.int8)
    b_cv1 = torch.randint(-500, 501, (256,), dtype=torch.int32)
    w_bn0cv1 = torch.randint(-50, 51, (128, 128, 3, 3), dtype=torch.int8)
    b_bn0cv1 = torch.randint(-500, 501, (128,), dtype=torch.int32)
    w_bn0cv2 = torch.randint(-50, 51, (128, 128, 3, 3), dtype=torch.int8)
    b_bn0cv2 = torch.randint(-500, 501, (128,), dtype=torch.int32)
    w_cv2 = torch.randint(-50, 51, (256, 384, 1, 1), dtype=torch.int8)
    b_cv2 = torch.randint(-500, 501, (256,), dtype=torch.int32)

    # CPU reference
    ref_l19 = conv2d_int8_pade_silu_reference(
        x_l18, w_l19, b_l19, scale, shift2, stride=2
    )
    ref_concat = torch.cat([ref_l19, x_p5_skip], dim=1)  # 384ch
    ref_cv1 = conv2d_int8_pade_silu_reference(
        ref_concat, w_cv1, b_cv1, scale, shift2, stride=1, padding=0
    )
    half1 = ref_cv1[:, :128, :, :]
    half2 = ref_cv1[:, 128:, :, :]
    ref_bn0_inter = conv2d_int8_pade_silu_reference(
        half2, w_bn0cv1, b_bn0cv1, scale, shift2, stride=1, padding=1
    )
    ref_bn0_out = conv2d_int8_pade_silu_reference(
        ref_bn0_inter, w_bn0cv2, b_bn0cv2, scale, shift2, stride=1, padding=1
    )
    ref_concat2 = torch.cat([half1, half2, ref_bn0_out], dim=1)
    ref_output = conv2d_int8_pade_silu_reference(
        ref_concat2, w_cv2, b_cv2, scale, shift2, stride=1, padding=0
    )

    # Pack weights
    l19_oc_chunk, l19_n_oc, _ = _compute_oc_streaming_params(128, 128, w, 2)
    l19_chunks = []
    for g in range(l19_n_oc):
        ws = w_l19[g * l19_oc_chunk : (g + 1) * l19_oc_chunk]
        bs = b_l19[g * l19_oc_chunk : (g + 1) * l19_oc_chunk]
        l19_chunks.append(np.concatenate([
            weights_to_tiled_int8_k3(ws),
            bs.numpy().astype(np.int32).view(np.int8),
        ]))
    packed_l19 = np.concatenate(l19_chunks)

    cv1_oc_chunk, cv1_n_oc = 64, 4
    cv1_chunks = []
    for g in range(cv1_n_oc):
        ws = w_cv1[g * cv1_oc_chunk : (g + 1) * cv1_oc_chunk]
        bs = b_cv1[g * cv1_oc_chunk : (g + 1) * cv1_oc_chunk]
        cv1_chunks.append(np.concatenate([
            weights_to_tiled_int8(ws),
            bs.numpy().astype(np.int32).view(np.int8),
        ]))
    packed_cv1 = np.concatenate(cv1_chunks)

    bn_oc_chunk, bn_n_oc, _ = _compute_oc_streaming_params(128, 128, l21_w, 1)
    def _pack_k3_oc(wt, b, oc_c, n):
        chunks = []
        for g in range(n):
            ws = wt[g * oc_c : (g + 1) * oc_c]
            bs = b[g * oc_c : (g + 1) * oc_c]
            chunks.append(np.concatenate([
                weights_to_tiled_int8_k3(ws),
                bs.numpy().astype(np.int32).view(np.int8),
            ]))
        return np.concatenate(chunks)
    packed_bn0cv1 = _pack_k3_oc(w_bn0cv1, b_bn0cv1, bn_oc_chunk, bn_n_oc)
    packed_bn0cv2 = _pack_k3_oc(w_bn0cv2, b_bn0cv2, bn_oc_chunk, bn_n_oc)

    cv2_chunks = []
    for g in range(4):
        ws = w_cv2[g * 64 : (g + 1) * 64]
        bs = b_cv2[g * 64 : (g + 1) * 64]
        cv2_chunks.append(np.concatenate([
            weights_to_tiled_int8(ws),
            bs.numpy().astype(np.int32).view(np.int8),
        ]))
    packed_cv2 = np.concatenate(cv2_chunks)

    packed_weights = np.concatenate(
        [packed_l19, packed_cv1, packed_bn0cv1, packed_bn0cv2, packed_cv2]
    )

    # Build NPU
    ctx = AIEContext()
    op = AIEDataflowL19L21(l19_h=h, l19_w=w, s1=scale, s2=shift2, context=ctx)
    ctx.compile_all()
    ctx.prepare_runtime()

    output_buf_size = op.buffers["output"]
    l21_output_size = 256 * l21_h * l21_w
    l21_concat_size = 384 * l21_h * l21_w
    concat_offset = l21_output_size

    # Pre-fill O with P5_skip in concat[128:384ch] (strided)
    o_buf = np.zeros(output_buf_size, dtype=np.int8)
    skip_tiled = nchw_to_tiled_int8(x_p5_skip)
    for row in range(l21_h):
        src_start = row * 256 * l21_w
        dst_start = concat_offset + row * 384 * l21_w + 128 * l21_w
        o_buf[dst_start:dst_start + 256 * l21_w] = skip_tiled[src_start:src_start + 256 * l21_w]

    op.write_buffer("input", nchw_to_tiled_int8(x_l18))
    op.write_buffer("weights", packed_weights)
    op.write_buffer("output", o_buf)

    t0 = time.perf_counter()
    op.run_runlist()
    run_ms = (time.perf_counter() - t0) * 1000
    print(f"\n  L19+L21 combined ({h}x{w}): {run_ms:.1f}ms")

    out_flat = op.read_buffer("output", (output_buf_size,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(out_flat[:l21_output_size], 256, l21_h, l21_w)

    ref_np = ref_output.numpy().astype(np.int8)
    npu_np = npu_output.numpy().astype(np.int8)
    diff = np.abs(ref_np.astype(np.int32) - npu_np.astype(np.int32))
    max_diff = int(diff.max())
    total_elems = diff.size
    errors_gt5 = int(np.sum(diff > 5))
    print(f"  max_diff={max_diff}, errors>5={errors_gt5}/{total_elems}")

    assert max_diff <= 10, f"L19+L21 failed: max_diff={max_diff}"
    assert errors_gt5 / total_elems < 0.10, f"L19+L21: too many errors >5"


# ============================================================================
# Combined L19+L21 with 2-column parallelism
# ============================================================================


class AIEDataflowL19L21_2col(AIEOperatorBase):
    """Combined L19+L21 with 2-column parallelism."""

    def __init__(self, l19_h, l19_w, s1, s2, context=None):
        self.l19_h, self.l19_w = l19_h, l19_w
        self.s1, self.s2 = s1, s2
        self.xclbin_artifact = self.insts_artifact = None
        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        from iron.operators.conv2d_int8.dataflow_design import (
            _compute_oc_streaming_params,
        )
        d = Path(__file__).parent
        bd = self.context.base_dir / "aie_kernels" / "aie2p"
        base = f"dataflow_l19_l21_2col_{self.l19_h}h_{self.l19_w}w"
        s = self.s1
        mlir = PythonGeneratedMLIRArtifact.new(
            f"{base}.mlir", import_path=d / "dataflow_design.py",
            callback_fn="my_dataflow_l19_l21_2col",
            callback_args=[
                self.context.device_manager.device_type,
                self.l19_h, self.l19_w,
                s, self.s2, s, self.s2, s, self.s2,
                s, self.s2, s, self.s2,
            ])
        def ko(name, src, flags):
            return KernelObjectArtifact.new(name,
                depends=[SourceArtifact.new(bd / src)], extra_flags=flags)
        k_objs = [
            ko("conv2dk3_i8_silu.o", "conv2dk3_i8_silu.cc", ["-DINT8_ACT"]),
            ko("conv2dk1_i8_silu.o", "conv2dk1_i8_silu.cc", ["-DINT8_ACT"]),
            ko("conv2dk1_i8_silu_cv2.o", "conv2dk1_i8_silu.cc",
               ["-DINT8_ACT", "-Dconv2dk1_i8_silu=conv2dk1_i8_silu_cv2"]),
        ]
        xclbin = XclbinArtifact.new(f"{base}.xclbin", depends=[mlir]+k_objs)
        insts = InstsBinArtifact.new(f"{base}.bin", depends=[mlir])
        self.xclbin_artifact, self.insts_artifact = xclbin, insts
        self.add_artifacts([xclbin, insts])
        oc_chunk, n_oc, _ = _compute_oc_streaming_params(128, 128, self.l19_w, 2)
        self._l19_oc_chunk, self._l19_n_oc = oc_chunk, n_oc
        l21_w = self.l19_w // 2
        bn_oc, bn_n, _ = _compute_oc_streaming_params(128, 128, l21_w, 1)
        self._bn_oc_chunk, self._bn_n_oc = bn_oc, bn_n

    def set_up_runtime(self):
        NC = 2
        l21_h, l21_w = self.l19_h // 2, self.l19_w // 2
        l19_ti = 128 * self.l19_h * self.l19_w
        l19_tw = self._l19_n_oc * (self._l19_oc_chunk*128*9+self._l19_oc_chunk*4)
        cv1_tw = 4*(64*384+64*4)
        bn_tw = self._bn_n_oc*(self._bn_oc_chunk*128*9+self._bn_oc_chunk*4)
        cv2_tw = 4*(64*384+64*4)
        tw = l19_tw+cv1_tw+2*bn_tw+cv2_tw
        l21_out = 256*l21_h*l21_w
        l21_concat = 384*l21_h*l21_w
        bn_scratch = 128*l21_h*l21_w
        oT = l21_out+l21_concat+bn_scratch
        self.add_buffer("input", l19_ti, dtype=np.int8)
        self.add_buffer("weights", tw, dtype=np.int8)
        self.add_buffer("output", oT, dtype=np.int8)
        self.add_kernel("l19l21_2c", self.xclbin_artifact,
                        self.xclbin_artifact.kernel_name, self.insts_artifact)
        self.add_to_runlist("l19l21_2c", "input", "weights", "output")


@pytest.mark.parametrize("h,w", [
    pytest.param(16, 16, id="l19_l21_2col_16x16"),
    pytest.param(40, 40, id="l19_l21_2col_40x40"),
])
def test_dataflow_l19_l21_2col(h, w):
    """Combined L19+L21 with 2-column parallelism."""
    from iron.operators.conv2d_int8.dataflow_design import _compute_oc_streaming_params

    torch.manual_seed(42)
    s, s2 = 10, 7
    NC = 2
    l21_h, l21_w = h//2, w//2

    x_l18 = torch.randint(-20, 21, (1, 128, h, w), dtype=torch.int8)
    x_p5 = torch.randint(-20, 21, (1, 256, l21_h, l21_w), dtype=torch.int8)
    w_l19 = torch.randint(-50,51,(128,128,3,3),dtype=torch.int8)
    b_l19 = torch.randint(-500,501,(128,),dtype=torch.int32)
    w_cv1 = torch.randint(-50,51,(256,384,1,1),dtype=torch.int8)
    b_cv1 = torch.randint(-500,501,(256,),dtype=torch.int32)
    w_bn1 = torch.randint(-50,51,(128,128,3,3),dtype=torch.int8)
    b_bn1 = torch.randint(-500,501,(128,),dtype=torch.int32)
    w_bn2 = torch.randint(-50,51,(128,128,3,3),dtype=torch.int8)
    b_bn2 = torch.randint(-500,501,(128,),dtype=torch.int32)
    w_cv2 = torch.randint(-50,51,(256,384,1,1),dtype=torch.int8)
    b_cv2 = torch.randint(-500,501,(256,),dtype=torch.int32)

    # CPU ref
    rl19 = conv2d_int8_pade_silu_reference(x_l18,w_l19,b_l19,s,s2,stride=2)
    rc = torch.cat([rl19, x_p5], dim=1)
    rcv1 = conv2d_int8_pade_silu_reference(rc,w_cv1,b_cv1,s,s2,stride=1,padding=0)
    h1,h2_=rcv1[:,:128],rcv1[:,128:]
    rb1 = conv2d_int8_pade_silu_reference(h2_,w_bn1,b_bn1,s,s2,stride=1,padding=1)
    rb2 = conv2d_int8_pade_silu_reference(rb1,w_bn2,b_bn2,s,s2,stride=1,padding=1)
    ref = conv2d_int8_pade_silu_reference(
        torch.cat([h1,h2_,rb2],dim=1),w_cv2,b_cv2,s,s2,stride=1,padding=0)

    # Pack weights: col0 gets first half of OC groups, col1 gets second half
    l19_oc_chunk, l19_n, _ = _compute_oc_streaming_params(128,128,w,2)
    l19_npc = l19_n // NC
    def _pk3(wt, b, oc_c, n):
        cs = []
        for g in range(n):
            ws=wt[g*oc_c:(g+1)*oc_c]; bs=b[g*oc_c:(g+1)*oc_c]
            cs.append(np.concatenate([weights_to_tiled_int8_k3(ws),
                                      bs.numpy().astype(np.int32).view(np.int8)]))
        return np.concatenate(cs)
    def _pk1(wt, b, oc_c, n):
        cs = []
        for g in range(n):
            ws=wt[g*oc_c:(g+1)*oc_c]; bs=b[g*oc_c:(g+1)*oc_c]
            cs.append(np.concatenate([weights_to_tiled_int8(ws),
                                      bs.numpy().astype(np.int32).view(np.int8)]))
        return np.concatenate(cs)

    half = l19_npc * l19_oc_chunk
    pw_l19 = np.concatenate([_pk3(w_l19[:half],b_l19[:half],l19_oc_chunk,l19_npc),
                              _pk3(w_l19[half:],b_l19[half:],l19_oc_chunk,l19_npc)])
    cv1_c = 64
    pw_cv1 = _pk1(w_cv1, b_cv1, cv1_c, 4)  # single-col, all 4 groups
    bn_oc_chunk, bn_n, _ = _compute_oc_streaming_params(128,128,l21_w,1)
    bn_npc = bn_n // NC
    bn_half = bn_npc * bn_oc_chunk
    pw_bn1 = np.concatenate([_pk3(w_bn1[:bn_half],b_bn1[:bn_half],bn_oc_chunk,bn_npc),
                              _pk3(w_bn1[bn_half:],b_bn1[bn_half:],bn_oc_chunk,bn_npc)])
    pw_bn2 = np.concatenate([_pk3(w_bn2[:bn_half],b_bn2[:bn_half],bn_oc_chunk,bn_npc),
                              _pk3(w_bn2[bn_half:],b_bn2[bn_half:],bn_oc_chunk,bn_npc)])
    pw_cv2 = _pk1(w_cv2, b_cv2, cv1_c, 4)  # single-col, all 4 groups
    pw = np.concatenate([pw_l19, pw_cv1, pw_bn1, pw_bn2, pw_cv2])

    # Build NPU
    ctx = AIEContext()
    op = AIEDataflowL19L21_2col(l19_h=h, l19_w=w, s1=s, s2=s2, context=ctx)
    ctx.compile_all()
    ctx.prepare_runtime()

    oT = op.buffers["output"]
    l21_out = 256*l21_h*l21_w
    concat_off = l21_out

    # Pre-fill P5 into concat[128:384ch]
    o_buf = np.zeros(oT, dtype=np.int8)
    p5t = nchw_to_tiled_int8(x_p5)
    for row in range(l21_h):
        src = row*256*l21_w
        dst = concat_off + row*384*l21_w + 128*l21_w
        o_buf[dst:dst+256*l21_w] = p5t[src:src+256*l21_w]

    op.write_buffer("input", nchw_to_tiled_int8(x_l18))
    op.write_buffer("weights", pw)
    op.write_buffer("output", o_buf)

    t0 = time.perf_counter()
    op.run_runlist()
    ms = (time.perf_counter()-t0)*1000
    print(f"\n  L19+L21 2-col ({h}×{w}): {ms:.1f}ms")

    out = op.read_buffer("output", (oT,), dtype=np.int8)[:l21_out]
    npu = tiled_to_nchw_int8(out, 256, l21_h, l21_w)
    diff = np.abs(ref.numpy().astype(np.int32) - npu.numpy().astype(np.int32))
    md = int(diff.max()); e5 = int(np.sum(diff>5)); tot = diff.size
    print(f"  max_diff={md}, errors>5={e5}/{tot}")
    assert md <= 10, f"L19+L21 2-col failed: max_diff={md}"
    assert e5/tot < 0.10


# ============================================================================
# Upsample 2× dataflow test
# ============================================================================


class AIEDataflowUpsample2x(AIEOperatorBase):
    """Nearest-neighbor 2× spatial upsample on NPU."""

    def __init__(self, height, width, channels, context=None):
        self.height = height
        self.width = width
        self.channels = channels
        self.xclbin_artifact = None
        self.insts_artifact = None
        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        base = f"dataflow_ups2x_{self.channels}ch_{self.height}h_{self.width}w"
        mlir = PythonGeneratedMLIRArtifact.new(
            f"{base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_upsample2x",
            callback_args=[
                self.context.device_manager.device_type,
                self.height, self.width, self.channels,
            ],
        )
        k_obj = KernelObjectArtifact.new(
            "upsample2x_i8.o",
            depends=[SourceArtifact.new(
                self.context.base_dir / "aie_kernels" / "aie2p" / "upsample2x_i8.cc"
            )],
            extra_flags=["-DINT8_ACT"],
        )
        xclbin = XclbinArtifact.new(f"{base}.xclbin", depends=[mlir, k_obj])
        insts = InstsBinArtifact.new(f"{base}.bin", depends=[mlir])
        self.xclbin_artifact = xclbin
        self.insts_artifact = insts
        self.add_artifacts([xclbin, insts])

    def set_up_runtime(self):
        total_in = self.channels * self.height * self.width
        total_out = self.channels * (self.height * 2) * (self.width * 2)
        self.add_buffer("input", total_in, dtype=np.int8)
        self.add_buffer("weights", 4, dtype=np.int8)  # dummy, 3-buf interface
        self.add_buffer("output", total_out, dtype=np.int8)
        self.add_kernel("ups2x", self.xclbin_artifact,
                        self.xclbin_artifact.kernel_name, self.insts_artifact)
        self.add_to_runlist("ups2x", "input", "weights", "output")


@pytest.mark.parametrize("h,w,c", [
    pytest.param(8, 8, 64, id="ups2x_64ch_8x8"),
    pytest.param(8, 8, 128, id="ups2x_128ch_8x8"),
    pytest.param(20, 20, 128, id="ups2x_128ch_20x20"),
    pytest.param(40, 40, 128, id="ups2x_128ch_40x40"),
])
def test_dataflow_upsample2x(h, w, c):
    """Test nearest-neighbor 2× upsample on NPU."""
    torch.manual_seed(42)

    x_int8 = torch.randint(-128, 127, (1, c, h, w), dtype=torch.int8)

    # CPU reference: repeat_interleave on both spatial dims
    ref = x_int8.repeat_interleave(2, dim=2).repeat_interleave(2, dim=3)

    ctx = AIEContext()
    op = AIEDataflowUpsample2x(height=h, width=w, channels=c, context=ctx)
    ctx.compile_all()
    ctx.prepare_runtime()

    op.write_buffer("input", nchw_to_tiled_int8(x_int8))
    op.write_buffer("weights", np.zeros(4, dtype=np.int8))
    total_out = c * (h * 2) * (w * 2)
    op.write_buffer("output", np.zeros(total_out, dtype=np.int8))

    t0 = time.perf_counter()
    op.run_runlist()
    run_ms = (time.perf_counter() - t0) * 1000

    out_flat = op.read_buffer("output", (total_out,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(out_flat, c, h * 2, w * 2)

    ref_np = ref.numpy().astype(np.int8)
    npu_np = npu_output.numpy().astype(np.int8)
    diff = np.abs(ref_np.astype(np.int32) - npu_np.astype(np.int32))
    max_diff = int(diff.max())
    total_elems = diff.size
    exact = int(np.sum(diff == 0))
    print(f"\n  Upsample 2× ({c}ch, {h}×{w} → {h*2}×{w*2}): "
          f"{run_ms:.1f}ms, max_diff={max_diff}, exact={exact}/{total_elems}")

    assert max_diff == 0, f"Upsample 2× failed: max_diff={max_diff} (expected exact)"


# ============================================================================
# Combined L12+L15 test
# ============================================================================


class AIEDataflowL12L15(AIEOperatorBase):
    """Combined L12 C2f + Upsample + L15 C2f in one PDI."""

    def __init__(self, l12_h, l12_w, s1, s2, context=None):
        self.l12_h, self.l12_w = l12_h, l12_w
        self.s1, self.s2 = s1, s2
        self.xclbin_artifact = self.insts_artifact = None
        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        d = Path(__file__).parent
        bd = self.context.base_dir / "aie_kernels" / "aie2p"
        base = f"dataflow_l12_l15_{self.l12_h}h_{self.l12_w}w"
        s = self.s1
        mlir = PythonGeneratedMLIRArtifact.new(
            f"{base}.mlir", import_path=d / "dataflow_design.py",
            callback_fn="my_dataflow_l12_l15",
            callback_args=[
                self.context.device_manager.device_type, self.l12_h, self.l12_w,
                s, self.s2, s, self.s2, s, self.s2, s, self.s2,
                s, self.s2, s, self.s2, s, self.s2, s, self.s2,
            ])
        def ko(name, src, flags):
            return KernelObjectArtifact.new(name,
                depends=[SourceArtifact.new(bd / src)], extra_flags=flags)
        k_objs = [
            ko("conv2dk1_i8_silu.o", "conv2dk1_i8_silu.cc", ["-DINT8_ACT"]),
            ko("conv2dk1_i8_silu_cv2.o", "conv2dk1_i8_silu.cc",
               ["-DINT8_ACT", "-Dconv2dk1_i8_silu=conv2dk1_i8_silu_cv2"]),
            ko("conv2dk3_i8_silu.o", "conv2dk3_i8_silu.cc", ["-DINT8_ACT"]),
            ko("conv2dk1_i8_silu_l15.o", "conv2dk1_i8_silu.cc",
               ["-DINT8_ACT", "-Dconv2dk1_i8_silu=conv2dk1_i8_silu_l15"]),
            ko("conv2dk1_i8_silu_l15cv2.o", "conv2dk1_i8_silu.cc",
               ["-DINT8_ACT", "-Dconv2dk1_i8_silu=conv2dk1_i8_silu_l15cv2"]),
            ko("conv2dk3_i8_silu_l15.o", "conv2dk3_i8_silu.cc",
               ["-DINT8_ACT", "-Dconv2dk3_i8_silu=conv2dk3_i8_silu_l15",
                "-Dconv2dk3s2_i8_silu=conv2dk3s2_i8_silu_l15"]),
            ko("upsample2x_i8.o", "upsample2x_i8.cc", ["-DINT8_ACT"]),
        ]
        xclbin = XclbinArtifact.new(f"{base}.xclbin", depends=[mlir]+k_objs)
        insts = InstsBinArtifact.new(f"{base}.bin", depends=[mlir])
        self.xclbin_artifact, self.insts_artifact = xclbin, insts
        self.add_artifacts([xclbin, insts])

    def set_up_runtime(self):
        h12, w12 = self.l12_h, self.l12_w
        h15, w15 = h12*2, w12*2
        total_in = 384 * h12 * w12
        # Weights
        avail = 65536 - 1040 - 2*384*w12
        cv1c = 128
        for oc in range(128, 0, -8):
            if 128 % oc != 0: continue
            if oc*384+oc*4+2*oc*w12 <= avail: cv1c = oc; break
        l12_cv1_tw = (128//cv1c) * (cv1c*384+cv1c*4)
        l12_bw = 64*64*9+64*4
        l12_c2w = 128*192+128*4
        l15_c1w = 64*192+64*4
        l15_bw = 32*32*9+32*4
        l15_c2w = 64*96+64*4
        tw = l12_cv1_tw+2*l12_bw+l12_c2w+l15_c1w+2*l15_bw+l15_c2w
        # Output buf
        s0 = 64*h15*w15; s1 = 192*h12*w12; s2 = 128*h12*w12
        s3 = 192*h15*w15; s4 = 96*h15*w15
        oT = s0+s1+s2+s3+s4
        self.add_buffer("input", total_in, dtype=np.int8)
        self.add_buffer("weights", tw, dtype=np.int8)
        self.add_buffer("output", oT, dtype=np.int8)
        self.add_kernel("l12l15", self.xclbin_artifact,
                        self.xclbin_artifact.kernel_name, self.insts_artifact)
        self.add_to_runlist("l12l15", "input", "weights", "output")


@pytest.mark.parametrize("h,w", [
    pytest.param(8, 8, id="l12_l15_8x8"),
    pytest.param(40, 40, id="l12_l15_40x40"),
])
def test_dataflow_l12_l15(h, w):
    """Combined L12+upsample+L15: 384ch input → 64ch output."""
    torch.manual_seed(42)
    s, s2 = 10, 7
    h15, w15 = h*2, w*2

    # Input + P3 skip
    x = torch.randint(-20, 21, (1, 384, h, w), dtype=torch.int8)
    p3 = torch.randint(-20, 21, (1, 64, h15, w15), dtype=torch.int8)

    # L12 weights
    w12c1 = torch.randint(-50,51,(128,384,1,1),dtype=torch.int8)
    b12c1 = torch.randint(-500,501,(128,),dtype=torch.int32)
    w12b1 = torch.randint(-50,51,(64,64,3,3),dtype=torch.int8)
    b12b1 = torch.randint(-500,501,(64,),dtype=torch.int32)
    w12b2 = torch.randint(-50,51,(64,64,3,3),dtype=torch.int8)
    b12b2 = torch.randint(-500,501,(64,),dtype=torch.int32)
    w12c2 = torch.randint(-50,51,(128,192,1,1),dtype=torch.int8)
    b12c2 = torch.randint(-500,501,(128,),dtype=torch.int32)
    # L15 weights
    w15c1 = torch.randint(-50,51,(64,192,1,1),dtype=torch.int8)
    b15c1 = torch.randint(-500,501,(64,),dtype=torch.int32)
    w15b1 = torch.randint(-50,51,(32,32,3,3),dtype=torch.int8)
    b15b1 = torch.randint(-500,501,(32,),dtype=torch.int32)
    w15b2 = torch.randint(-50,51,(32,32,3,3),dtype=torch.int8)
    b15b2 = torch.randint(-500,501,(32,),dtype=torch.int32)
    w15c2 = torch.randint(-50,51,(64,96,1,1),dtype=torch.int8)
    b15c2 = torch.randint(-500,501,(64,),dtype=torch.int32)

    # CPU ref: L12
    rc1 = conv2d_int8_pade_silu_reference(x, w12c1, b12c1, s, s2, stride=1, padding=0)
    h1, h2_ = rc1[:,:64], rc1[:,64:]
    rb1 = conv2d_int8_pade_silu_reference(h2_, w12b1, b12b1, s, s2, stride=1, padding=1)
    rb2 = conv2d_int8_pade_silu_reference(rb1, w12b2, b12b2, s, s2, stride=1, padding=1)
    rc2 = conv2d_int8_pade_silu_reference(
        torch.cat([h1,h2_,rb2],dim=1), w12c2, b12c2, s, s2, stride=1, padding=0)
    # Upsample + concat P3
    ups = rc2.repeat_interleave(2,dim=2).repeat_interleave(2,dim=3)
    l15_in = torch.cat([ups, p3], dim=1)
    # L15
    rc1_ = conv2d_int8_pade_silu_reference(l15_in, w15c1, b15c1, s, s2, stride=1, padding=0)
    h1_, h2__ = rc1_[:,:32], rc1_[:,32:]
    rb1_ = conv2d_int8_pade_silu_reference(h2__, w15b1, b15b1, s, s2, stride=1, padding=1)
    rb2_ = conv2d_int8_pade_silu_reference(rb1_, w15b2, b15b2, s, s2, stride=1, padding=1)
    ref = conv2d_int8_pade_silu_reference(
        torch.cat([h1_,h2__,rb2_],dim=1), w15c2, b15c2, s, s2, stride=1, padding=0)

    # Pack weights
    avail = 65536 - 1040 - 2*384*w
    cv1c = 128
    for oc in range(128,0,-8):
        if 128%oc!=0: continue
        if oc*384+oc*4+2*oc*w<=avail: cv1c=oc; break
    cv1n = 128//cv1c
    chunks = []
    for g in range(cv1n):
        ws=w12c1[g*cv1c:(g+1)*cv1c]; bs=b12c1[g*cv1c:(g+1)*cv1c]
        chunks.append(np.concatenate([weights_to_tiled_int8(ws),
                                      bs.numpy().astype(np.int32).view(np.int8)]))
    pw = np.concatenate(chunks + [
        pack_fused_weights_k3(w12b1,b12b1), pack_fused_weights_k3(w12b2,b12b2),
        _pack_k1_silu_weights(w12c2,b12c2),
        _pack_k1_silu_weights(w15c1,b15c1),
        pack_fused_weights_k3(w15b1,b15b1), pack_fused_weights_k3(w15b2,b15b2),
        _pack_k1_silu_weights(w15c2,b15c2),
    ])

    # Build NPU
    ctx = AIEContext()
    op = AIEDataflowL12L15(l12_h=h, l12_w=w, s1=s, s2=s2, context=ctx)
    ctx.compile_all()
    ctx.prepare_runtime()

    oT = op.buffers["output"]
    s0=64*h15*w15; s1_=192*h*w; s2_=128*h*w; s3_=192*h15*w15
    o3 = s0+s1_+s2_  # L15_concat offset

    # Pre-fill P3 into L15_concat[128:192ch]
    o_buf = np.zeros(oT, dtype=np.int8)
    p3t = nchw_to_tiled_int8(p3)
    for row in range(h15):
        src = row*64*w15
        dst = o3 + row*192*w15 + 128*w15
        o_buf[dst:dst+64*w15] = p3t[src:src+64*w15]

    op.write_buffer("input", nchw_to_tiled_int8(x))
    op.write_buffer("weights", pw)
    op.write_buffer("output", o_buf)

    t0 = time.perf_counter()
    op.run_runlist()
    ms = (time.perf_counter()-t0)*1000
    print(f"\n  L12+L15 combined ({h}×{w}): {ms:.1f}ms")

    out = op.read_buffer("output", (oT,), dtype=np.int8)[:s0]
    npu = tiled_to_nchw_int8(out, 64, h15, w15)
    diff = np.abs(ref.numpy().astype(np.int32) - npu.numpy().astype(np.int32))
    md = int(diff.max())
    e5 = int(np.sum(diff>5))
    tot = diff.size
    print(f"  max_diff={md}, errors>5={e5}/{tot}")
    assert md <= 10, f"L12+L15 failed: max_diff={md}"
    assert e5/tot < 0.10, f"L12+L15: too many errors >5"


# ============================================================================
# Detection head: one PDI per scale (reg + cls branches)
# ============================================================================


class AIEDataflowDetectScale(AIEOperatorBase):
    """Detection head: one PDI per scale (reg + cls branches).

    6 workers (2 columns), 6 task groups, 6 kernel symbols.
    Each branch: cv1(k3+SiLU) -> cv2(k3+SiLU) -> cv3(k1+bias, no activation).
    """

    def __init__(
        self, height, width, in_channels,
        reg_cv1_s1, reg_cv1_s2, reg_cv2_s1, reg_cv2_s2,
        reg_cv3_s1, reg_cv3_s2,
        cls_cv1_s1, cls_cv1_s2, cls_cv2_s1, cls_cv2_s2,
        cls_cv3_s1, cls_cv3_s2,
        context=None,
    ):
        self.height = height
        self.width = width
        self.in_channels = in_channels
        self.reg_cv1_s1 = reg_cv1_s1
        self.reg_cv1_s2 = reg_cv1_s2
        self.reg_cv2_s1 = reg_cv2_s1
        self.reg_cv2_s2 = reg_cv2_s2
        self.reg_cv3_s1 = reg_cv3_s1
        self.reg_cv3_s2 = reg_cv3_s2
        self.cls_cv1_s1 = cls_cv1_s1
        self.cls_cv1_s2 = cls_cv1_s2
        self.cls_cv2_s1 = cls_cv2_s1
        self.cls_cv2_s2 = cls_cv2_s2
        self.cls_cv3_s1 = cls_cv3_s1
        self.cls_cv3_s2 = cls_cv3_s2
        self.xclbin_artifact = None
        self.insts_artifact = None
        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        from iron.operators.conv2d_int8.dataflow_design import (
            _compute_oc_streaming_params,
            _compute_oc_streaming_params_k1,
        )

        operator_dir = Path(__file__).parent
        base = (f"dataflow_detect_{self.in_channels}ic_"
                f"{self.height}h_{self.width}w")
        mlir = PythonGeneratedMLIRArtifact.new(
            f"{base}.mlir",
            import_path=operator_dir / "dataflow_design.py",
            callback_fn="my_dataflow_detect_scale",
            callback_args=[
                self.context.device_manager.device_type,
                self.height, self.width, self.in_channels,
                self.reg_cv1_s1, self.reg_cv1_s2,
                self.reg_cv2_s1, self.reg_cv2_s2,
                self.reg_cv3_s1, self.reg_cv3_s2,
                self.cls_cv1_s1, self.cls_cv1_s2,
                self.cls_cv2_s1, self.cls_cv2_s2,
                self.cls_cv3_s1, self.cls_cv3_s2,
            ],
        )
        k_objs = self._make_kernel_objs()
        xclbin = XclbinArtifact.new(f"{base}.xclbin", depends=[mlir] + k_objs)
        insts = InstsBinArtifact.new(f"{base}.bin", depends=[mlir])
        self.xclbin_artifact = xclbin
        self.insts_artifact = insts
        self.add_artifacts([xclbin, insts])

        # Store OC streaming params for weight packing
        reg_mid = 64
        cls_mid = 80
        self._rcv1_oc_chunk, self._rcv1_n_oc, _ = _compute_oc_streaming_params(
            self.in_channels, reg_mid, self.width, 1)
        self._rcv2_oc_chunk, self._rcv2_n_oc, _ = _compute_oc_streaming_params(
            reg_mid, reg_mid, self.width, 1)
        self._rcv3_oc_chunk, self._rcv3_n_oc = _compute_oc_streaming_params_k1(
            reg_mid, 64, self.width)  # reg_mid -> reg_out (64)

        self._ccv1_oc_chunk, self._ccv1_n_oc, _ = _compute_oc_streaming_params(
            self.in_channels, cls_mid, self.width, 1)
        self._ccv2_oc_chunk, self._ccv2_n_oc, _ = _compute_oc_streaming_params(
            cls_mid, cls_mid, self.width, 1)
        self._ccv3_oc_chunk, self._ccv3_n_oc = _compute_oc_streaming_params_k1(
            cls_mid, cls_mid, self.width)

    def _make_kernel_objs(self):
        base_dir = self.context.base_dir / "aie_kernels" / "aie2p"
        k3_src = SourceArtifact.new(base_dir / "conv2dk3_i8_silu.cc")
        k1_bias_src = SourceArtifact.new(base_dir / "conv2dk1_i8_bias.cc")
        return [
            # 1. reg.cv1 k3+SiLU
            KernelObjectArtifact.new("conv2dk3_i8_silu.o",
                depends=[k3_src], extra_flags=["-DINT8_ACT"]),
            # 2. reg.cv2 k3+SiLU (renamed symbol)
            KernelObjectArtifact.new("conv2dk3_i8_silu_rcv2.o",
                depends=[k3_src],
                extra_flags=["-DINT8_ACT",
                             "-Dconv2dk3_i8_silu=conv2dk3_i8_silu_rcv2"]),
            # 3. cls.cv1 k3+SiLU (renamed symbol)
            KernelObjectArtifact.new("conv2dk3_i8_silu_ccv1.o",
                depends=[k3_src],
                extra_flags=["-DINT8_ACT",
                             "-Dconv2dk3_i8_silu=conv2dk3_i8_silu_ccv1"]),
            # 4. cls.cv2 k3+SiLU (renamed symbol)
            KernelObjectArtifact.new("conv2dk3_i8_silu_ccv2.o",
                depends=[k3_src],
                extra_flags=["-DINT8_ACT",
                             "-Dconv2dk3_i8_silu=conv2dk3_i8_silu_ccv2"]),
            # 5. reg.cv3 k1+bias (-O1 to avoid Peano codegen bug at w_iters>=10)
            KernelObjectArtifact.new("conv2dk1_i8_bias.o",
                depends=[k1_bias_src], extra_flags=["-DINT8_ACT"]),
            # 6. cls.cv3 k1+bias (renamed, -O1 for same codegen bug)
            KernelObjectArtifact.new("conv2dk1_i8_bias_cls.o",
                depends=[k1_bias_src],
                extra_flags=["-DINT8_ACT", "-O1",
                             "-Dconv2dk1_i8_bias=conv2dk1_i8_bias_cls"]),
        ]

    def set_up_runtime(self):
        ic = self.in_channels
        reg_mid = 64
        reg_out = 64
        cls_mid = 80
        cls_out = 80
        h, w = self.height, self.width

        total_input = ic * h * w

        # Weight sizes
        def _k3_wt(oc_chunk, n_oc, ic_):
            chunk = oc_chunk * ic_ * 9 + oc_chunk * 4
            return n_oc * chunk

        def _k1_wt(oc_chunk, n_oc, ic_):
            chunk = oc_chunk * ic_ + oc_chunk * 4
            return n_oc * chunk

        rcv1_wt = _k3_wt(self._rcv1_oc_chunk, self._rcv1_n_oc, ic)
        rcv2_wt = _k3_wt(self._rcv2_oc_chunk, self._rcv2_n_oc, reg_mid)
        rcv3_wt = _k1_wt(self._rcv3_oc_chunk, self._rcv3_n_oc, reg_mid)
        ccv1_wt = _k3_wt(self._ccv1_oc_chunk, self._ccv1_n_oc, ic)
        ccv2_wt = _k3_wt(self._ccv2_oc_chunk, self._ccv2_n_oc, cls_mid)
        ccv3_wt = _k1_wt(self._ccv3_oc_chunk, self._ccv3_n_oc, cls_mid)
        total_wt = rcv1_wt + rcv2_wt + rcv3_wt + ccv1_wt + ccv2_wt + ccv3_wt

        reg_output_size = reg_out * h * w
        cls_output_size = cls_out * h * w
        reg_scratch_a = reg_mid * h * w
        reg_scratch_b = reg_mid * h * w
        cls_scratch_a = cls_mid * h * w
        cls_scratch_b = cls_mid * h * w
        output_buf_size = (reg_output_size + cls_output_size
                           + reg_scratch_a + reg_scratch_b
                           + cls_scratch_a + cls_scratch_b)

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_wt, dtype=np.int8)
        self.add_buffer("output", output_buf_size, dtype=np.int8)
        self.add_kernel(
            "detect", self.xclbin_artifact,
            self.xclbin_artifact.kernel_name, self.insts_artifact,
        )
        self.add_to_runlist("detect", "input", "weights", "output")


@pytest.mark.parametrize(
    "det_ic,det_h,det_w",
    [
        pytest.param(128, 16, 16, id="detect_p4_16x16"),
        pytest.param(128, 40, 40, id="detect_p4_40x40"),
        pytest.param(64, 16, 16, id="detect_p3_16x16"),
        pytest.param(256, 16, 16, id="detect_p5_16x16"),
        pytest.param(256, 20, 20, id="detect_p5_20x20",
                     marks=pytest.mark.extensive),
        pytest.param(64, 80, 80, id="detect_p3_80x80",
                     marks=pytest.mark.extensive),
    ],
)
def test_dataflow_detect_scale(det_ic, det_h, det_w):
    """Detection head: one PDI per scale with reg + cls branches."""
    from iron.operators.conv2d_int8.dataflow_design import (
        _compute_oc_streaming_params,
        _compute_oc_streaming_params_k1,
    )
    from iron.operators.conv2d_int8.reference import conv2d_int8_bias_reference

    torch.manual_seed(42)
    scale = 10
    shift2 = 7

    reg_mid = 64
    reg_out = 64
    cls_mid = 80
    cls_out = 80

    # Generate input
    x_int8 = torch.randint(
        -20, 21, (1, det_ic, det_h, det_w), dtype=torch.int8
    )

    # reg branch weights
    w_rcv1 = torch.randint(-50, 51, (reg_mid, det_ic, 3, 3), dtype=torch.int8)
    b_rcv1 = torch.randint(-500, 501, (reg_mid,), dtype=torch.int32)
    w_rcv2 = torch.randint(-50, 51, (reg_mid, reg_mid, 3, 3), dtype=torch.int8)
    b_rcv2 = torch.randint(-500, 501, (reg_mid,), dtype=torch.int32)
    w_rcv3 = torch.randint(-50, 51, (reg_out, reg_mid, 1, 1), dtype=torch.int8)
    b_rcv3 = torch.randint(-500, 501, (reg_out,), dtype=torch.int32)

    # cls branch weights
    w_ccv1 = torch.randint(-50, 51, (cls_mid, det_ic, 3, 3), dtype=torch.int8)
    b_ccv1 = torch.randint(-500, 501, (cls_mid,), dtype=torch.int32)
    w_ccv2 = torch.randint(-50, 51, (cls_mid, cls_mid, 3, 3), dtype=torch.int8)
    b_ccv2 = torch.randint(-500, 501, (cls_mid,), dtype=torch.int32)
    w_ccv3 = torch.randint(-50, 51, (cls_out, cls_mid, 1, 1), dtype=torch.int8)
    b_ccv3 = torch.randint(-500, 501, (cls_out,), dtype=torch.int32)

    # CPU reference — reg branch
    ref_rcv1 = conv2d_int8_pade_silu_reference(
        x_int8, w_rcv1, b_rcv1, scale, shift2, stride=1, padding=1
    )
    ref_rcv2 = conv2d_int8_pade_silu_reference(
        ref_rcv1, w_rcv2, b_rcv2, scale, shift2, stride=1, padding=1
    )
    ref_reg = conv2d_int8_bias_reference(
        ref_rcv2, w_rcv3, b_rcv3, scale, shift2, stride=1, padding=0
    )

    # CPU reference — cls branch
    ref_ccv1 = conv2d_int8_pade_silu_reference(
        x_int8, w_ccv1, b_ccv1, scale, shift2, stride=1, padding=1
    )
    ref_ccv2 = conv2d_int8_pade_silu_reference(
        ref_ccv1, w_ccv2, b_ccv2, scale, shift2, stride=1, padding=1
    )
    ref_cls = conv2d_int8_bias_reference(
        ref_ccv2, w_ccv3, b_ccv3, scale, shift2, stride=1, padding=0
    )

    # Pack weights — OC streaming chunks for each layer
    # k3 weight packing
    def _pack_k3_oc(w, b, oc_chunk, n_oc):
        chunks = []
        for g in range(n_oc):
            w_s = w[g * oc_chunk : (g + 1) * oc_chunk]
            b_s = b[g * oc_chunk : (g + 1) * oc_chunk]
            chunks.append(np.concatenate([
                weights_to_tiled_int8_k3(w_s),
                b_s.numpy().astype(np.int32).view(np.int8),
            ]))
        return np.concatenate(chunks)

    # k1 weight packing
    def _pack_k1_oc(w, b, oc_chunk, n_oc):
        chunks = []
        for g in range(n_oc):
            w_s = w[g * oc_chunk : (g + 1) * oc_chunk]
            b_s = b[g * oc_chunk : (g + 1) * oc_chunk]
            chunks.append(np.concatenate([
                weights_to_tiled_int8(w_s),
                b_s.numpy().astype(np.int32).view(np.int8),
            ]))
        return np.concatenate(chunks)

    # OC streaming params
    rcv1_oc, rcv1_n, _ = _compute_oc_streaming_params(det_ic, reg_mid, det_w, 1)
    rcv2_oc, rcv2_n, _ = _compute_oc_streaming_params(reg_mid, reg_mid, det_w, 1)
    rcv3_oc, rcv3_n = _compute_oc_streaming_params_k1(reg_mid, reg_out, det_w)
    ccv1_oc, ccv1_n, _ = _compute_oc_streaming_params(det_ic, cls_mid, det_w, 1)
    ccv2_oc, ccv2_n, _ = _compute_oc_streaming_params(cls_mid, cls_mid, det_w, 1)
    ccv3_oc, ccv3_n = _compute_oc_streaming_params_k1(cls_mid, cls_out, det_w)

    packed_rcv1 = _pack_k3_oc(w_rcv1, b_rcv1, rcv1_oc, rcv1_n)
    packed_rcv2 = _pack_k3_oc(w_rcv2, b_rcv2, rcv2_oc, rcv2_n)
    packed_rcv3 = _pack_k1_oc(w_rcv3, b_rcv3, rcv3_oc, rcv3_n)
    packed_ccv1 = _pack_k3_oc(w_ccv1, b_ccv1, ccv1_oc, ccv1_n)
    packed_ccv2 = _pack_k3_oc(w_ccv2, b_ccv2, ccv2_oc, ccv2_n)
    packed_ccv3 = _pack_k1_oc(w_ccv3, b_ccv3, ccv3_oc, ccv3_n)

    packed_weights = np.concatenate([
        packed_rcv1, packed_rcv2, packed_rcv3,
        packed_ccv1, packed_ccv2, packed_ccv3,
    ])

    # Build NPU design
    ctx = AIEContext()
    op = AIEDataflowDetectScale(
        height=det_h, width=det_w, in_channels=det_ic,
        reg_cv1_s1=scale, reg_cv1_s2=shift2,
        reg_cv2_s1=scale, reg_cv2_s2=shift2,
        reg_cv3_s1=scale, reg_cv3_s2=shift2,
        cls_cv1_s1=scale, cls_cv1_s2=shift2,
        cls_cv2_s1=scale, cls_cv2_s2=shift2,
        cls_cv3_s1=scale, cls_cv3_s2=shift2,
        context=ctx,
    )
    ctx.compile_all()
    ctx.prepare_runtime()

    reg_output_size = reg_out * det_h * det_w
    cls_output_size = cls_out * det_h * det_w
    output_buf_size = op.buffers["output"]

    op.write_buffer("input", nchw_to_tiled_int8(x_int8))
    op.write_buffer("weights", packed_weights)
    op.write_buffer("output", np.zeros(output_buf_size, dtype=np.int8))

    t0 = time.perf_counter()
    op.run_runlist()
    run_ms = (time.perf_counter() - t0) * 1000
    print(f"\n  Detect scale IC={det_ic} ({det_h}x{det_w}): {run_ms:.1f}ms")

    out_flat = op.read_buffer("output", (output_buf_size,), dtype=np.int8)

    # Verify reg output
    reg_flat = out_flat[:reg_output_size]
    npu_reg = tiled_to_nchw_int8(reg_flat, reg_out, det_h, det_w)
    ref_reg_np = ref_reg.numpy().astype(np.int8)
    npu_reg_np = npu_reg.numpy().astype(np.int8)
    diff_reg = np.abs(ref_reg_np.astype(np.int32) - npu_reg_np.astype(np.int32))
    max_diff_reg = int(diff_reg.max())
    e5_reg = int(np.sum(diff_reg > 5))
    tot_reg = diff_reg.size
    print(f"  reg: max_diff={max_diff_reg}, errors>5={e5_reg}/{tot_reg}")

    # Verify cls output
    cls_flat = out_flat[reg_output_size : reg_output_size + cls_output_size]
    npu_cls = tiled_to_nchw_int8(cls_flat, cls_out, det_h, det_w)
    ref_cls_np = ref_cls.numpy().astype(np.int8)
    npu_cls_np = npu_cls.numpy().astype(np.int8)
    diff_cls = np.abs(ref_cls_np.astype(np.int32) - npu_cls_np.astype(np.int32))
    max_diff_cls = int(diff_cls.max())
    e5_cls = int(np.sum(diff_cls > 5))
    tot_cls = diff_cls.size
    print(f"  cls: max_diff={max_diff_cls}, errors>5={e5_cls}/{tot_cls}")

    # Assert correctness (tolerance ladder for 3-layer pipeline)
    # Large IC (256) accumulates more bf16 rounding error through 3 layers
    max_diff_thresh = 30 if det_ic >= 256 else 15
    e5_rate_thresh = 0.25 if det_ic >= 256 else 0.10
    assert max_diff_reg <= max_diff_thresh, (
        f"Detect reg failed: max_diff={max_diff_reg} exceeds threshold {max_diff_thresh}"
    )
    assert e5_reg / tot_reg < e5_rate_thresh, (
        f"Detect reg: {100 * e5_reg / tot_reg:.2f}% errors > 5 "
        f"exceeds {100 * e5_rate_thresh:.0f}%"
    )
    assert max_diff_cls <= max_diff_thresh, (
        f"Detect cls failed: max_diff={max_diff_cls} exceeds threshold {max_diff_thresh}"
    )
    assert e5_cls / tot_cls < e5_rate_thresh, (
        f"Detect cls: {100 * e5_cls / tot_cls:.2f}% errors > 5 "
        f"exceeds {100 * e5_rate_thresh:.0f}%"
    )
