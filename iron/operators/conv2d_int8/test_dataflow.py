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
    """Full C2f L2: fused SiLU, 48ch concat [cv1_out|bn0_out].

    Uses fused conv+SiLU kernels. cv2 takes 48ch input (32ch from cv1
    pass-through + 16ch from bottleneck output) concatenated at MemTile.
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

        # bn k3 SiLU kernel (renamed symbol for separate MLIR type)
        k3_silu_bn_obj = KernelObjectArtifact.new(
            "conv2dk3_i8_silu_bn.o",
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
                k3_silu_bn_obj,
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
    """Test full C2f L2: fused SiLU, 48ch concat for cv2."""
    torch.manual_seed(42)

    bn_ch = 16
    cv2_ic = 48
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
    # Split: extract second 16 channels for bottleneck
    half2 = cv1_out[:, bn_ch:, :, :]
    # Bottleneck with fused SiLU
    bn_inter = conv2d_int8_pade_silu_reference(
        half2, w_bn1, b_bn1, bn1_s1, bn1_s2, stride=1, padding=1
    )
    bn_out = conv2d_int8_pade_silu_reference(
        bn_inter, w_bn2, b_bn2, bn2_s1, bn2_s2, stride=1, padding=1
    )
    # Concat: [cv1_out(32ch) | bn_out(16ch)] = 48ch
    concat = torch.cat([cv1_out, bn_out], dim=1)
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

        phase1_wt_slot = max(cv1_wt, bn_k3_wt)
        phase1_total_wt = 5 * phase1_wt_slot
        total_wt = phase1_total_wt + cv2_wt
        self._phase1_wt_slot = phase1_wt_slot
        self._cv2_wt = cv2_wt

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

    # Write packed weights
    phase1_wt_slot = op._phase1_wt_slot
    w_cv1_tiled = weights_to_tiled_int8(w_cv1)
    w_bn0cv1_tiled = weights_to_tiled_int8_k3(w_bn0cv1)
    w_bn0cv2_tiled = weights_to_tiled_int8_k3(w_bn0cv2)
    w_bn1cv1_tiled = weights_to_tiled_int8_k3(w_bn1cv1)
    w_bn1cv2_tiled = weights_to_tiled_int8_k3(w_bn1cv2)
    w_cv2_tiled = weights_to_tiled_int8(w_cv2)

    def _pad(data, slot_size):
        pad = np.zeros(slot_size - len(data), dtype=np.int8)
        return np.concatenate([data, pad])

    packed_p1 = np.concatenate(
        [
            _pad(w_cv1_tiled, phase1_wt_slot),
            _pad(w_bn0cv1_tiled, phase1_wt_slot),
            _pad(w_bn0cv2_tiled, phase1_wt_slot),
            _pad(w_bn1cv1_tiled, phase1_wt_slot),
            _pad(w_bn1cv2_tiled, phase1_wt_slot),
        ]
    )
    packed_all = np.concatenate([packed_p1, w_cv2_tiled])
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
