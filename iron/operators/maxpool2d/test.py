#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import numpy as np
from ml_dtypes import bfloat16

from iron.operators.maxpool2d.op import AIEMaxPool2d, nchw_to_tiled, tiled_to_nchw
from iron.operators.maxpool2d.reference import generate_golden_reference
from iron.common.utils import torch_to_numpy

# Test parameters: (channels, height, width, kernel_size, stride, padding)
regular_params = [
    (8, 8, 8, 5, 1, 2),  # tiny (must be >= kernel_size=5)
    (16, 8, 8, 5, 1, 2),  # small
    (128, 8, 8, 5, 1, 2),  # medium, close to SPPF size
]

extensive_params = [
    (128, 20, 20, 5, 1, 2),  # actual YOLOv8n SPPF size
]


def make_test_name(channels, h, w, k, s, p):
    return f"maxpool2d_{channels}c_{h}h_{w}w_k{k}_s{s}_p{p}"


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
    "channels,height,width,kernel_size,stride,padding",
    all_params,
)
def test_maxpool2d(channels, height, width, kernel_size, stride, padding, aie_context):
    """Test MaxPool2d operator against PyTorch reference.

    MaxPool2d is exact (no floating point accumulation -- just comparisons),
    so we use abs_tol=0.0, rel_tol=0.0 for exact matching.
    """
    # Generate golden reference
    golden_ref = generate_golden_reference(
        channels=channels,
        height=height,
        width=width,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
    )

    # Create operator
    operator = AIEMaxPool2d(
        channels=channels,
        height=height,
        width=width,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        num_aie_columns=1,
        context=aie_context,
    )

    import logging

    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    operator.context.compile_all()
    operator.context.prepare_runtime()

    # Prepare padded input in tiled layout
    input_tiled = operator._pad_input(golden_ref["input"])

    # Write buffers
    out_height = (height + 2 * padding - kernel_size) // stride + 1
    out_width = (width + 2 * padding - kernel_size) // stride + 1
    total_output = channels * out_height * out_width
    original_write = operator.write_buffer
    original_write("output", np.zeros(total_output, dtype=bfloat16))
    original_write("input", input_tiled)

    # Run
    elapsed = operator.run_runlist()
    latency_us = elapsed * 1e6

    # Read and verify output
    output_raw = operator.read_buffer("output", (total_output,), dtype=bfloat16)

    # Convert NPU output from tiled back to NCHW for comparison
    npu_output_nchw = tiled_to_nchw(output_raw.copy(), channels, out_height, out_width)

    # Compare against reference
    expected_output = golden_ref["output"]
    ref_np = torch_to_numpy(expected_output).reshape(-1)
    npu_np = torch_to_numpy(npu_output_nchw).reshape(-1)

    errors = []
    # MaxPool is exact (no accumulation), so use zero tolerance
    rel_tol = 0.0
    abs_tol = 0.0
    for i in range(len(ref_np)):
        a = float(npu_np[i])
        b = float(ref_np[i])
        if a == b:
            continue
        errors.append(i)
        if len(errors) <= 10:
            print(
                f"Mismatch at [{i}]: NPU={a:.6f}, ref={b:.6f}, "
                f"diff={abs(a - b):.6f}"
            )

    # Calculate bandwidth
    padded_height = height + 2 * padding
    padded_width = width + 2 * padding
    input_bytes = channels * padded_height * padded_width * 2  # bf16 = 2 bytes
    output_bytes = channels * out_height * out_width * 2
    total_bytes = input_bytes + output_bytes
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert (
        not errors
    ), f"Test failed with {len(errors)} mismatches out of {len(ref_np)} elements"
