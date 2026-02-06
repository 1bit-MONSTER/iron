#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
from pathlib import Path
import time
import torch

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.softmax.op import AIESoftmax
from operators.common import AIEBuffer

max_context_len = 2048
prompt_len = 8
n_heads = 32

softmax_op = (
    AIESoftmax(rows=n_heads, cols=max_context_len, rtp_vector_size=prompt_len)
    .compile()
    .get_callable()
)

inp = AIEBuffer((n_heads, max_context_len))
out = AIEBuffer((n_heads, max_context_len))

inp.view_as_torch()[:] = torch.randn(n_heads, max_context_len)
out.view_as_torch()[:] = torch.zeros(n_heads, max_context_len)

t_cpu_start = time.perf_counter()
out_ref = inp.view_as_torch()[:, :prompt_len].softmax(dim=-1)
t_cpu = time.perf_counter() - t_cpu_start

inp.to("npu")
out.to("npu")
t_aie_start = time.perf_counter()
softmax_op(inp, out)
t_aie = time.perf_counter() - t_aie_start
out.to("cpu")

print(out_ref)
print(t_cpu)
aie_out = out.view_as_torch()[:, :prompt_len]
print(aie_out)
print(t_aie)

# Check which elements differ
diff = torch.abs(out_ref - aie_out)
max_diff = diff.max()
print(f"Max diff: {max_diff}")
print(f"Number of mismatches (> 1e-2): {(diff > 1e-2).sum()}")

# Find first mismatch
mismatches = torch.where(diff > 1e-2)
if len(mismatches[0]) > 0:
    for i in range(min(10, len(mismatches[0]))):
        h, s = mismatches[0][i], mismatches[1][i]
        print(
            f"Mismatch at head={h}, seq={s}: ref={out_ref[h,s]}, aie={aie_out[h,s]}, diff={diff[h,s]}"
        )

assert torch.allclose(out_ref, aie_out, atol=1e-2, rtol=1e-2)
