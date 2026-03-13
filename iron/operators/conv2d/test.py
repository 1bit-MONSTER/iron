#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import numpy as np
from ml_dtypes import bfloat16

from iron.operators.conv2d.op import (
    AIEConv2d,
    nchw_to_tiled,
    tiled_to_nchw,
    weights_to_tiled,
    weights_to_tiled_3x3,
)
from iron.operators.conv2d.reference import generate_golden_reference
from iron.common.test_utils import run_test
from iron.common.utils import torch_to_numpy

# Test parameters: (in_channels, out_channels, height, width, kernel_size, stride)
regular_params = [
    # 1x1 conv: tiny test cases for fast validation
    (8, 8, 4, 4, 1, 1),
    (16, 16, 4, 4, 1, 1),
    (32, 32, 8, 8, 1, 1),
    # 1x1 conv: small C2f-like shapes
    (64, 64, 8, 8, 1, 1),
    (32, 32, 16, 16, 1, 1),
    # 3x3 conv stride=1: Bottleneck internal convs
    (16, 16, 8, 8, 3, 1),
    (8, 8, 16, 16, 3, 1),
    (16, 16, 16, 16, 3, 1),
    # 3x3 conv stride=2: backbone downsampling
    (8, 8, 8, 8, 3, 2),
    (8, 16, 8, 8, 3, 2),
]

extensive_params = [
    # 1x1 conv: larger YOLOv8n-like shapes
    (32, 32, 32, 32, 1, 1),
    (64, 64, 16, 16, 1, 1),
    (128, 128, 8, 8, 1, 1),
    (32, 64, 16, 16, 1, 1),
    (64, 32, 16, 16, 1, 1),
    # 3x3 conv stride=1: larger shapes
    (32, 32, 16, 16, 3, 1),
    (32, 32, 32, 32, 3, 1),
    # 3x3 conv stride=2: larger downsampling
    (16, 32, 16, 16, 3, 2),
    (32, 64, 16, 16, 3, 2),
]


def make_test_name(in_ch, out_ch, h, w, k, s):
    return f"conv2d_{in_ch}ic_{out_ch}oc_{h}h_{w}w_k{k}_s{s}"


all_params = [
    pytest.param(
        *p,
        id=make_test_name(*p),
    )
    for p in regular_params
] + [
    pytest.param(
        *p,
        marks=pytest.mark.extensive,
        id=make_test_name(*p),
    )
    for p in extensive_params
]


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "in_channels,out_channels,height,width,kernel_size,stride",
    all_params,
)
def test_conv2d(
    in_channels, out_channels, height, width, kernel_size, stride, aie_context
):
    """Test conv2d operator against PyTorch reference.

    The test generates random input and weights, computes the reference
    output using PyTorch F.conv2d, then runs the same computation on
    the NPU and compares results.

    Bias is applied in Python after the NPU computation,
    so we test without bias to isolate the NPU kernel correctness.
    """
    # Generate golden reference (without bias for NPU kernel validation)
    golden_ref = generate_golden_reference(
        in_channels=in_channels,
        out_channels=out_channels,
        height=height,
        width=width,
        kernel_size=kernel_size,
        stride=stride,
        has_bias=False,
        activation=None,
    )

    # Create operator
    operator = AIEConv2d(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        height=height,
        width=width,
        has_bias=False,
        activation=None,
        num_aie_columns=1,
        context=aie_context,
    )

    # Prepare input and weight buffers in tiled layout
    input_tiled = nchw_to_tiled(golden_ref["input"])
    if kernel_size == 1:
        weight_tiled = weights_to_tiled(golden_ref["weight"])
    else:
        weight_tiled = weights_to_tiled_3x3(golden_ref["weight"])

    # Prepare expected output in tiled layout for comparison
    expected_output_torch = golden_ref["output"]
    out_h = expected_output_torch.shape[2]
    out_w = expected_output_torch.shape[3]

    # Build operator and prepare runtime
    import logging

    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    operator.context.compile_all()
    operator.context.prepare_runtime()

    # Write buffers in tiled format
    original_write = operator.write_buffer
    total_output = out_channels * out_h * out_w
    original_write("output", np.zeros(total_output, dtype=bfloat16))
    original_write("input", input_tiled)
    original_write("weights", weight_tiled)

    # Warmup
    operator.run_runlist()

    # Clear and re-write for timed run
    original_write("output", np.zeros(total_output, dtype=bfloat16))
    original_write("input", input_tiled)
    original_write("weights", weight_tiled)

    # Run
    elapsed = operator.run_runlist()
    latency_us = elapsed * 1e6

    # Read and verify output
    output_raw = operator.read_buffer("output", (total_output,), dtype=bfloat16)

    # Convert NPU output from tiled back to NCHW for comparison
    npu_output_nchw = tiled_to_nchw(output_raw.copy(), out_channels, out_h, out_w)

    # Compare against reference
    ref_np = torch_to_numpy(expected_output_torch).reshape(-1)
    npu_np = torch_to_numpy(npu_output_nchw).reshape(-1)

    errors = []
    # 3x3 conv accumulates more products per output element, so
    # bfloat16 rounding errors are larger. Use wider tolerances.
    if kernel_size == 3:
        rel_tol = 0.07
        abs_tol = 0.5
    else:
        rel_tol = 0.04
        abs_tol = 1e-4
    for i in range(len(ref_np)):
        a = float(npu_np[i])
        b = float(ref_np[i])
        if a == b:
            continue
        diff = abs(a - b)
        norm = min(abs(a) + abs(b), np.finfo(np.float32).max)
        if diff >= max(abs_tol, rel_tol * norm):
            errors.append(i)
            if len(errors) <= 10:
                print(
                    f"Mismatch at [{i}]: NPU={a:.6f}, ref={b:.6f}, " f"diff={diff:.6f}"
                )

    # Calculate bandwidth
    input_bytes = in_channels * height * width * 2  # bf16 = 2 bytes
    weight_bytes = out_channels * in_channels * kernel_size * kernel_size * 2
    output_bytes = out_channels * out_h * out_w * 2
    total_bytes = input_bytes + weight_bytes + output_bytes
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert (
        not errors
    ), f"Test failed with {len(errors)} mismatches out of {len(ref_np)} elements"
