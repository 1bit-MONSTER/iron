#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import numpy as np
import logging
from ml_dtypes import bfloat16

from iron.operators.upsample.op import AIEUpsample
from iron.operators.upsample.reference import generate_golden_reference
from iron.operators.conv2d.op import nchw_to_tiled, tiled_to_nchw
from iron.common.utils import torch_to_numpy

# Test parameters: (channels, height, width, scale_factor)
regular_params = [
    (8, 4, 4, 2),  # tiny
    (16, 4, 4, 2),  # small
    (32, 8, 8, 2),  # medium
]

extensive_params = [
    (128, 20, 20, 2),  # YOLOv8n SPPF output -> neck
    (256, 20, 20, 2),  # YOLOv8n P5 upsample
]


def make_test_name(channels, height, width, scale_factor):
    return f"upsample_{channels}c_{height}h_{width}w_s{scale_factor}"


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
def test_upsample(channels, height, width, scale_factor, aie_context):
    """Test nearest-neighbor 2x upsampling operator against PyTorch reference.

    Upsample is a pure data movement operation, so we use exact comparison
    (zero tolerance). The test converts data to tiled layout to match the
    NPU's internal format.
    """
    # Generate golden reference in NCHW format
    golden_ref = generate_golden_reference(
        channels=channels,
        height=height,
        width=width,
        scale_factor=scale_factor,
    )

    out_height = height * scale_factor
    out_width = width * scale_factor

    # Create operator
    operator = AIEUpsample(
        channels=channels,
        height=height,
        width=width,
        scale_factor=scale_factor,
        num_aie_columns=1,
        context=aie_context,
    )

    # Convert to tiled layout for NPU
    input_tiled = nchw_to_tiled(golden_ref["input"])
    output_tiled_expected = nchw_to_tiled(golden_ref["output"])

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
    operator.write_buffer("output", np.zeros(total_output, dtype=bfloat16))
    operator.write_buffer("input", input_tiled)

    # Run
    elapsed = operator.run_runlist()
    latency_us = elapsed * 1e6

    # Read output
    output_raw = operator.read_buffer("output", (total_output,), dtype=bfloat16)

    # Convert NPU output from tiled back to NCHW for comparison
    npu_output_nchw = tiled_to_nchw(output_raw.copy(), channels, out_height, out_width)

    # Compare against reference (exact match -- upsample is pure data duplication)
    ref_np = torch_to_numpy(golden_ref["output"]).reshape(-1)
    npu_np = torch_to_numpy(npu_output_nchw).reshape(-1)

    errors = []
    for i in range(len(ref_np)):
        if float(npu_np[i]) != float(ref_np[i]):
            errors.append(i)
            if len(errors) <= 10:
                print(
                    f"Mismatch at [{i}]: NPU={float(npu_np[i]):.6f}, "
                    f"ref={float(ref_np[i]):.6f}"
                )

    # Calculate bandwidth
    input_bytes = channels * height * width * 2  # bf16 = 2 bytes
    output_bytes = channels * out_height * out_width * 2
    total_bytes = input_bytes + output_bytes
    bandwidth_gbps = total_bytes / (latency_us * 1e-6) / 1e9

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert (
        not errors
    ), f"Test failed with {len(errors)} mismatches out of {len(ref_np)} elements"
