#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.operators.swiglu_fused_decode.op import AIESwiGLUFusedDecode
from iron.operators.swiglu_fused_decode.reference import (
    generate_golden_reference,
)
from iron.common.test_utils import run_test


def generate_test_params(extensive=False):
    params = [
        # (embedding_dim, hidden_dim)
        (2048, 2048),
    ]
    if extensive:
        params += [
            (2048, 8192),
        ]
    names = [f"swiglu_fused_decode_{emb}x{hid}" for emb, hid in params]
    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)

all_params = [
    pytest.param(*params, id=name)
    for params, name in zip(regular_params, regular_names)
] + [
    pytest.param(*params, marks=pytest.mark.extensive, id=name)
    for params, name in zip(extensive_params, extensive_names)
]


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize("embedding_dim,hidden_dim", all_params)
def test_swiglu_fused_decode(embedding_dim, hidden_dim, aie_context):
    golden_ref = generate_golden_reference(
        embedding_dim=embedding_dim, hidden_dim=hidden_dim
    )

    operator = AIESwiGLUFusedDecode(
        embedding_dim=embedding_dim,
        hidden_dim=hidden_dim,
        context=aie_context,
    )
    operator.weights_gate = golden_ref["w_gate"]
    operator.weights_up = golden_ref["w_up"]
    operator.weights_down = golden_ref["w_down"]

    input_buffers = {"input": golden_ref["x"]}
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        input_buffers,
        output_buffers,
        rel_tol=0.35,
        abs_tol=1.0,
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
