#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import torch
import numpy as np

from iron.operators.conv2d_int8.op import (
    AIEConv2dInt8,
    nchw_to_tiled_int8,
    tiled_to_nchw_int8,
    weights_to_tiled_int8,
)
from iron.operators.conv2d_int8.reference import (
    conv2d_int8_reference,
    conv2d_int8_fused_reference,
)

# Test parameters: (in_channels, out_channels, height, width)
regular_params = [
    (8, 8, 4, 4),
    (16, 16, 8, 8),
    (32, 32, 16, 16),
    (64, 64, 8, 8),
]


def make_test_name(in_ch, out_ch, h, w):
    return f"conv2d_int8_{in_ch}ic_{out_ch}oc_{h}h_{w}w"


all_params = [
    pytest.param(
        *p,
        id=make_test_name(*p),
    )
    for p in regular_params
]


@pytest.mark.parametrize(
    "in_channels,out_channels,height,width",
    all_params,
)
def test_conv2d_int8(in_channels, out_channels, height, width, aie_context):
    """Test int8 conv2d operator against CPU reference.

    Uses random int8 inputs and weights, computes the reference output
    using int32 accumulation + right-shift requantization, then runs the
    same on the NPU and compares. Should be exact match or +-1 due to
    rounding.
    """
    scale = 10
    torch.manual_seed(42)

    # Random int8 inputs and weights
    x_int8 = torch.randint(-20, 21, (1, in_channels, height, width), dtype=torch.int8)
    w_int8 = torch.randint(-50, 81, (out_channels, in_channels, 1, 1), dtype=torch.int8)

    # CPU reference
    ref_output = conv2d_int8_reference(x_int8, w_int8, scale)

    # Create operator
    operator = AIEConv2dInt8(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=1,
        stride=1,
        height=height,
        width=width,
        scale=scale,
        context=aie_context,
    )

    # Compile and prepare
    operator.context.compile_all()
    operator.context.prepare_runtime()

    # Write buffers
    input_tiled = nchw_to_tiled_int8(x_int8)
    weight_tiled = weights_to_tiled_int8(w_int8)
    total_output = out_channels * height * width

    operator.write_buffer("input", input_tiled)
    operator.write_buffer("weights", weight_tiled)
    operator.write_buffer("output", np.zeros(total_output, dtype=np.int8))

    # Run on NPU
    operator.run_runlist()

    # Read and verify output
    output_raw = operator.read_buffer("output", (total_output,), dtype=np.int8)
    npu_output = tiled_to_nchw_int8(output_raw.copy(), out_channels, height, width)

    # Compare: int8 should be exact or +-1 due to rounding
    ref_np = ref_output.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    errors = []
    for i in range(len(ref_np)):
        diff = abs(int(npu_np[i]) - int(ref_np[i]))
        if diff > 1:
            errors.append(i)
            if len(errors) <= 10:
                print(
                    f"Mismatch at [{i}]: NPU={npu_np[i]}, ref={ref_np[i]}, "
                    f"diff={diff}"
                )

    total_elements = len(ref_np)
    exact_match = np.sum(ref_np == npu_np)
    off_by_one = np.sum(np.abs(ref_np - npu_np) == 1)
    print(f"\nExact matches: {exact_match}/{total_elements}")
    print(f"Off-by-one: {off_by_one}/{total_elements}")
    print(f"Errors (diff > 1): {len(errors)}/{total_elements}")

    assert (
        not errors
    ), f"Test failed with {len(errors)} mismatches (diff > 1) out of {total_elements}"


# Fused test parameters: (in_channels, out_channels, height, width, stride, shift1, shift2)
fused_params = [
    (8, 16, 8, 8, 1, 10, 7),
    (8, 16, 8, 8, 2, 10, 7),
    (16, 32, 8, 8, 1, 11, 7),
    (32, 32, 8, 8, 1, 12, 7),
]


def make_fused_test_name(ic, oc, h, w, s, s1, s2):
    return f"conv2d_int8_fused_{ic}ic_{oc}oc_{h}h_{w}w_s{s}"


all_fused_params = [
    pytest.param(
        *p,
        id=make_fused_test_name(*p),
    )
    for p in fused_params
]


@pytest.mark.parametrize(
    "in_channels,out_channels,height,width,stride,shift1,shift2",
    all_fused_params,
)
def test_conv2d_int8_fused(
    in_channels, out_channels, height, width, stride, shift1, shift2, aie_context
):
    """Test fused int8 conv + bias + SiLU operator against CPU reference.

    Uses the packed-bias kernel (bias appended to weight buffer).
    Verifies the full integer SiLU pipeline: conv -> bias -> shift ->
    LUT lookup -> multiply -> shift -> int8 output.
    """
    torch.manual_seed(42)

    x_int8 = torch.randint(-20, 21, (1, in_channels, height, width), dtype=torch.int8)
    w_int8 = torch.randint(-50, 51, (out_channels, in_channels, 3, 3), dtype=torch.int8)
    bias_int32 = torch.randint(-500, 501, (out_channels,), dtype=torch.int32)

    # CPU reference
    ref_output = conv2d_int8_fused_reference(
        x_int8, w_int8, bias_int32, shift1, shift2, stride=stride
    )

    # Create fused operator
    operator = AIEConv2dInt8(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=3,
        stride=stride,
        height=height,
        width=width,
        fused=True,
        shift1=shift1,
        shift2=shift2,
        context=aie_context,
    )

    # Compile and run
    operator.context.compile_all()
    operator.context.prepare_runtime()

    npu_output = operator.forward(x_int8, w_int8, bias_int32)

    # Compare with tolerance (int8 pipeline may have +-1 rounding differences)
    out_h = height if stride == 1 else height // 2
    out_w = width if stride == 1 else width // 2
    ref_np = ref_output.numpy().reshape(-1).astype(np.int32)
    npu_np = npu_output.numpy().reshape(-1).astype(np.int32)

    errors = []
    for i in range(len(ref_np)):
        diff = abs(int(npu_np[i]) - int(ref_np[i]))
        if diff > 1:
            errors.append(i)
            if len(errors) <= 10:
                print(
                    f"Mismatch at [{i}]: NPU={npu_np[i]}, ref={ref_np[i]}, "
                    f"diff={diff}"
                )

    total_elements = len(ref_np)
    exact_match = np.sum(ref_np == npu_np)
    off_by_one = np.sum(np.abs(ref_np - npu_np) == 1)
    print(f"\nFused test {in_channels}ic_{out_channels}oc_s{stride}:")
    print(f"Exact matches: {exact_match}/{total_elements}")
    print(f"Off-by-one: {off_by_one}/{total_elements}")
    print(f"Errors (diff > 1): {len(errors)}/{total_elements}")

    assert (
        not errors
    ), f"Fused test failed with {len(errors)} mismatches (diff > 1) out of {total_elements}"
