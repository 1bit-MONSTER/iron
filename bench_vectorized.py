# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import torch
import numpy as np
from iron.common import AIEContext
from iron.operators.conv2d_int8.op import AIEConv2dInt8
from iron.operators.conv2d_int8.reference import conv2d_int8_reference

configs = [
    (32, 32, 160, 160),
    (64, 64, 80, 80),
    (128, 128, 40, 40),
]

for ic, oc, h, w in configs:
    can_vec = w % 32 == 0 and ic >= 24
    mode = "VECTORIZED" if can_vec else "SCALAR"
    print(f"\n=== {ic}->{oc} k1 {h}x{w} ({mode}) ===")
    ctx = AIEContext()
    op = AIEConv2dInt8(ic, oc, 1, 1, h, w, scale=10, context=ctx)
    ctx.compile_all()
    ctx.prepare_runtime()

    x = torch.randint(-20, 20, (1, ic, h, w), dtype=torch.int8)
    wt = torch.randint(-50, 50, (oc, ic, 1, 1), dtype=torch.int8)

    # Correctness check
    npu_out = op.forward(x, wt)
    ref_out = conv2d_int8_reference(x, wt, scale=10)
    max_diff = (npu_out.float() - ref_out.float()).abs().max().item()
    print(f"  Correctness: max_diff={max_diff:.1f} (pass={max_diff <= 1.0})")

    # Warmup
    op.forward(x, wt)

    # Benchmark
    times = []
    for _ in range(10):
        t0 = time.perf_counter()
        op.forward(x, wt)
        times.append(time.perf_counter() - t0)
    mean_us = sum(times) / len(times) * 1e6
    min_us = min(times) * 1e6
    print(f"  Timing: mean={mean_us:.0f}us min={min_us:.0f}us")
