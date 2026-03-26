#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import numpy as np
import logging

from iron.operators.maxpool2d_int8.op import AIEMaxPool2dInt8
from iron.operators.maxpool2d_int8.reference import generate_golden_reference
from iron.operators.conv2d_int8.op import nchw_to_tiled_int8, tiled_to_nchw_int8

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
    return f"maxpool2d_int8_{channels}c_{h}h_{w}w_k{k}_s{s}_p{p}"


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
def test_maxpool2d_int8(
    channels, height, width, kernel_size, stride, padding, aie_context
):
    """Test int8 MaxPool2d operator against PyTorch reference.

    MaxPool2d is exact (no accumulation — just comparisons),
    so we use zero tolerance for exact matching.
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
    operator = AIEMaxPool2dInt8(
        channels=channels,
        height=height,
        width=width,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        num_aie_columns=1,
        context=aie_context,
    )

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
    operator.write_buffer("output", np.zeros(total_output, dtype=np.int8))
    operator.write_buffer("input", input_tiled)

    # Run
    elapsed = operator.run_runlist()
    latency_us = elapsed * 1e6

    # Read and verify output
    output_raw = operator.read_buffer("output", (total_output,), dtype=np.int8)

    # Convert NPU output from tiled back to NCHW for comparison
    npu_output_nchw = tiled_to_nchw_int8(output_raw.copy(), channels, out_height, out_width)

    # Compare against reference
    expected_output = golden_ref["output"]
    ref_np = expected_output.numpy().reshape(-1)
    npu_np = npu_output_nchw.numpy().reshape(-1)

    errors = []
    # MaxPool is exact (no accumulation), so use zero tolerance
    for i in range(len(ref_np)):
        if int(npu_np[i]) != int(ref_np[i]):
            errors.append(i)
            if len(errors) <= 10:
                print(
                    f"Mismatch at [{i}]: NPU={int(npu_np[i])}, ref={int(ref_np[i])}"
                )

    # Calculate bandwidth (int8 = 1 byte per element)
    padded_height = height + 2 * padding
    padded_width = width + 2 * padding
    input_bytes = channels * padded_height * padded_width  # int8 = 1 byte
    output_bytes = channels * out_height * out_width
    total_bytes = input_bytes + output_bytes
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert (
        not errors
    ), f"Test failed with {len(errors)} mismatches out of {len(ref_np)} elements"
