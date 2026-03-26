# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Test vectorized conv2dk1_i8 with different heights and value ranges."""

import torch
from iron.common import AIEContext
from iron.operators.conv2d_int8.op import AIEConv2dInt8
from iron.operators.conv2d_int8.reference import conv2d_int8_reference

torch.manual_seed(42)

ic, oc, w, scale = 32, 32, 32, 10

for h in [2, 4, 8, 32]:
    ctx = AIEContext()
    op = AIEConv2dInt8(ic, oc, 1, 1, h, w, scale=scale, context=ctx)
    ctx.compile_all()
    ctx.prepare_runtime()

    x = torch.randint(-20, 20, (1, ic, h, w), dtype=torch.int8)
    wt = torch.randint(-50, 50, (oc, ic, 1, 1), dtype=torch.int8)

    npu_out = op.forward(x, wt)
    ref_out = conv2d_int8_reference(x, wt, scale=scale)

    diff = (npu_out.float() - ref_out.float()).abs()
    print(f"H={h:3d} IC={ic} OC={oc} W={w}: max_diff={diff.max().item():.1f} bad(>1)={((diff > 1).sum().item())}/{diff.numel()}")
