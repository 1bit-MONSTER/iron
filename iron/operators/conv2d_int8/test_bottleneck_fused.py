#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Test for fused bottleneck: two chained 3x3 conv+SiLU via inter-core ObjectFIFO.

Compares NPU output against CPU reference (two sequential conv+SiLU calls).
"""

import pytest
import torch
import numpy as np
from pathlib import Path

from iron.operators.conv2d_int8.op import (
    nchw_to_tiled_int8,
    tiled_to_nchw_int8,
    weights_to_tiled_int8_k3,
)
from iron.operators.conv2d_int8.reference import conv2d_int8_pade_silu_reference
from iron.common import (
    AIEOperatorBase,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEBottleneckFusedInt8(AIEOperatorBase):
    """Fused bottleneck operator: two chained k3 conv+SiLU on NPU.

    Compiles and runs the fused design with inter-core ObjectFIFO.
    """

    def __init__(self, channels, height, width, shift1, shift2, context=None):
        self.channels = channels
        self.height = height
        self.width = width
        self.shift1 = shift1
        self.shift2 = shift2

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=True)

    def set_up_artifacts(self):
        C = self.channels
        H = self.height
        W = self.width
        operator_dir = Path(__file__).parent
        file_name_base = f"bottleneck_fused_{C}ch_{H}h_{W}w_sh{self.shift1}_{self.shift2}"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "bottleneck_fused_design.py",
            callback_fn="my_bottleneck_fused",
            callback_args=[
                self.context.device_manager.device_type,
                H,
                W,
                C,
                self.shift1,
                self.shift2,
                self.shift1,
                self.shift2,
            ],
        )

        kernel_src = "conv2dk3_i8_silu.cc"
        kernel_obj_name = "conv2dk3_i8_silu.o"
        kernel_extra_flags = ["-DINT8_ACT"]

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
                    extra_flags=kernel_extra_flags,
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
        C = self.channels
        H = self.height
        W = self.width

        total_input = C * H * W
        wt_size = C * C * 9 + C * 4  # per conv: weights + packed bias
        total_weights = 2 * wt_size
        total_output = C * H * W

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "bottleneck_fused",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("bottleneck_fused", "input", "weights", "output")


def pack_bottleneck_weights(w1_int8, b1_int32, w2_int8, b2_int32):
    """Pack two conv weight/bias sets into the combined bottleneck weight buffer.

    Layout: [conv1_tiled_weights + conv1_bias_bytes + conv2_tiled_weights + conv2_bias_bytes]
    """
    w1_tiled = weights_to_tiled_int8_k3(w1_int8)
    b1_bytes = b1_int32.numpy().astype(np.int32).view(np.int8)
    w2_tiled = weights_to_tiled_int8_k3(w2_int8)
    b2_bytes = b2_int32.numpy().astype(np.int32).view(np.int8)
    return np.concatenate([w1_tiled, b1_bytes, w2_tiled, b2_bytes])


# Test parameters: (channels, height, width, shift1, shift2)
test_params = [
    pytest.param(8, 8, 8, 10, 7, id="bottleneck_fused_8ch_8x8"),
    pytest.param(16, 8, 8, 10, 7, id="bottleneck_fused_16ch_8x8"),
    pytest.param(32, 8, 8, 12, 7, id="bottleneck_fused_32ch_8x8"),
]


@pytest.mark.parametrize("channels,height,width,shift1,shift2", test_params)
def test_bottleneck_fused(channels, height, width, shift1, shift2, aie_context):
    """Test fused bottleneck against reference (two sequential conv+SiLU)."""
    torch.manual_seed(42)

    C, H, W = channels, height, width

    # Random test data
    x_int8 = torch.randint(-20, 21, (1, C, H, W), dtype=torch.int8)
    w1_int8 = torch.randint(-50, 51, (C, C, 3, 3), dtype=torch.int8)
    b1_int32 = torch.randint(-500, 501, (C,), dtype=torch.int32)
    w2_int8 = torch.randint(-50, 51, (C, C, 3, 3), dtype=torch.int8)
    b2_int32 = torch.randint(-500, 501, (C,), dtype=torch.int32)

    # CPU reference: two sequential conv+SiLU
    inter = conv2d_int8_pade_silu_reference(
        x_int8, w1_int8, b1_int32, shift1, shift2, stride=1
    )
    ref_output = conv2d_int8_pade_silu_reference(
        inter, w2_int8, b2_int32, shift1, shift2, stride=1
    )

    # Create fused operator
    operator = AIEBottleneckFusedInt8(
        channels=C, height=H, width=W, shift1=shift1, shift2=shift2, context=aie_context
    )

    # Compile and prepare
    operator.context.compile_all()
    operator.context.prepare_runtime()

    # Write input
    input_tiled = nchw_to_tiled_int8(x_int8)
    operator.write_buffer("input", input_tiled)

    # Write packed weights (both convs combined)
    packed_weights = pack_bottleneck_weights(w1_int8, b1_int32, w2_int8, b2_int32)
    operator.write_buffer("weights", packed_weights)

    # Clear output
    total_output = C * H * W
    operator.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    operator.run_runlist()

    # Read and verify output
    output_raw = operator.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), C, H, W)

    ref_np = ref_output.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    errors = []
    for i in range(len(ref_np)):
        diff = abs(int(npu_np[i]) - int(ref_np[i]))
        if diff > 2:  # Tolerance: +-2 for fused pipeline (2 conv stages)
            errors.append(i)
            if len(errors) <= 10:
                print(
                    f"Mismatch at [{i}]: NPU={npu_np[i]}, ref={ref_np[i]}, diff={diff}"
                )

    total_elements = len(ref_np)
    exact_match = np.sum(ref_np == npu_np)
    off_by_one = np.sum(np.abs(ref_np - npu_np) <= 1)
    off_by_two = np.sum(np.abs(ref_np - npu_np) <= 2)
    print(f"\nBottleneck fused test {C}ch_{H}h_{W}w:")
    print(f"Exact matches: {exact_match}/{total_elements}")
    print(f"Off-by-one: {off_by_one}/{total_elements}")
    print(f"Off-by-two: {off_by_two}/{total_elements}")
    print(f"Errors (diff > 2): {len(errors)}/{total_elements}")

    assert (
        not errors
    ), f"Fused bottleneck test failed with {len(errors)} mismatches (diff > 2) out of {total_elements}"


if __name__ == "__main__":
    """Quick standalone test for development."""
    from iron.operators.conv2d_int8.bottleneck_fused_design import (
        print_feasibility_report,
    )

    print_feasibility_report()
