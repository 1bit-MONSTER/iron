# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Sweep IC/OC to find where vectorized conv2dk1_i8 breaks."""

import torch
import numpy as np
from iron.common import AIEContext
from iron.operators.conv2d_int8.op import AIEConv2dInt8
from iron.operators.conv2d_int8.reference import conv2d_int8_reference

torch.manual_seed(42)

configs = [
    (8, 8),
    (16, 8),
    (16, 16),
    (24, 8),
    (24, 16),
    (24, 24),
    (32, 8),
    (32, 16),
    (32, 32),
]

h, w, scale = 1, 32, 10

for ic, oc in configs:
    ctx = AIEContext()
    op = AIEConv2dInt8(ic, oc, 1, 1, h, w, scale=scale, context=ctx)
    ctx.compile_all()
    ctx.prepare_runtime()

    x = torch.randint(-20, 20, (1, ic, h, w), dtype=torch.int8)
    wt = torch.randint(-50, 50, (oc, ic, 1, 1), dtype=torch.int8)

    npu_out = op.forward(x, wt)
    ref_out = conv2d_int8_reference(x, wt, scale=scale)

    diff = (npu_out.float() - ref_out.float()).abs()
    print(f"IC={ic:3d} OC={oc:3d}: max_diff={diff.max().item():.1f} bad={((diff > 1).sum().item())}/{diff.numel()}")
