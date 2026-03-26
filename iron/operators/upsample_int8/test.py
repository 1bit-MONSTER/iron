#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import numpy as np
import logging

from iron.operators.upsample_int8.op import AIEUpsampleInt8
from iron.operators.upsample_int8.reference import generate_golden_reference
from iron.operators.conv2d_int8.op import nchw_to_tiled_int8, tiled_to_nchw_int8

# Test parameters: (channels, height, width, scale_factor)
regular_params = [
    (8, 4, 4, 2),  # tiny
    (16, 4, 4, 2),  # small
    (32, 8, 8, 2),  # medium
]

extensive_params = [
    (128, 20, 20, 2),  # YOLOv8n SPPF output -> neck
]


def make_test_name(channels, height, width, scale_factor):
    return f"upsample_int8_{channels}c_{height}h_{width}w_s{scale_factor}"


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
    "channels,height,width,scale_factor",
    all_params,
)
def test_upsample_int8(channels, height, width, scale_factor, aie_context):
    """Test int8 nearest-neighbor 2x upsampling operator against PyTorch reference.

    Upsample is a pure data movement operation, so we use exact comparison
    (zero tolerance).
    """
    # Generate golden reference
    golden_ref = generate_golden_reference(
        channels=channels,
        height=height,
        width=width,
        scale_factor=scale_factor,
    )

    out_height = height * scale_factor
    out_width = width * scale_factor

    # Create operator
    operator = AIEUpsampleInt8(
        channels=channels,
        height=height,
        width=width,
        scale_factor=scale_factor,
        num_aie_columns=1,
        context=aie_context,
    )

    # Convert to tiled layout for NPU
    input_tiled = nchw_to_tiled_int8(golden_ref["input"])

    # Build operator and prepare runtime
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    operator.context.compile_all()
    operator.context.prepare_runtime()

    # Warmup
    operator.run_runlist()

    # Write input buffer in tiled format and zero output
    total_output = channels * out_height * out_width
    operator.write_buffer("output", np.zeros(total_output, dtype=np.int8))
    operator.write_buffer("input", input_tiled)

    # Run
    elapsed = operator.run_runlist()
    latency_us = elapsed * 1e6

    # Read output
    output_raw = operator.read_buffer("output", (total_output,), dtype=np.int8)

    # Convert NPU output from tiled back to NCHW for comparison
    npu_output_nchw = tiled_to_nchw_int8(
        output_raw.copy(), channels, out_height, out_width
    )

    # Compare against reference (exact match — upsample is pure data duplication)
    ref_np = golden_ref["output"].numpy().reshape(-1)
    npu_np = npu_output_nchw.numpy().reshape(-1)

    errors = []
    for i in range(len(ref_np)):
        if int(npu_np[i]) != int(ref_np[i]):
            errors.append(i)
            if len(errors) <= 10:
                print(
                    f"Mismatch at [{i}]: NPU={int(npu_np[i])}, ref={int(ref_np[i])}"
                )

    # Calculate bandwidth (int8 = 1 byte per element)
    input_bytes = channels * height * width  # int8 = 1 byte
    output_bytes = channels * out_height * out_width
    total_bytes = input_bytes + output_bytes
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert (
        not errors
    ), f"Test failed with {len(errors)} mismatches out of {len(ref_np)} elements"
