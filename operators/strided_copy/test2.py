#!/usr/bin/env python3

import sys
from pathlib import Path
import time
import torch
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.strided_copy.op import AIEStridedCopy
from operators.common import AIEBuffer

max_prompt_len = 2048
cached_prompt_len = 9
prompt_len = 7
head_dim = 64
num_heads = 32

transpose_concat = AIEStridedCopy(
    input_sizes=(num_heads, prompt_len, head_dim,),
    input_strides=(head_dim, num_heads * head_dim, 1,),
    input_offset=0,
    output_sizes=(1, num_heads, prompt_len, head_dim,),
    output_strides=(0, max_prompt_len * head_dim, head_dim, 1,),
    output_offset=cached_prompt_len * head_dim,
    input_buffer_size=prompt_len * num_heads * head_dim,
    output_buffer_size=num_heads * max_prompt_len * head_dim,
    num_aie_channels=4
).compile().get_callable()

value_cache = AIEBuffer((num_heads, max_prompt_len, head_dim))
value = AIEBuffer((prompt_len, num_heads, head_dim))

value_cache.view_as_torch()[:, :cached_prompt_len, :] = torch.randn(num_heads, cached_prompt_len, head_dim)
value.view_as_torch()[:prompt_len, :, :] = torch.randn(prompt_len, num_heads, head_dim)

t_cpu_start = time.perf_counter()
value_transposed = value.view_as_torch().transpose(0, 1)
out_ref = torch.cat([value_cache.view_as_torch()[:, :cached_prompt_len, :], value_transposed], dim=1)
t_cpu = time.perf_counter() - t_cpu_start

value_cache.to("npu")
value.to("npu")
t_aie_start = time.perf_counter()
transpose_concat(value, value_cache)
t_aie = time.perf_counter() - t_aie_start
value_cache.to("cpu")

print(out_ref)
print(t_cpu)
aie_out = value_cache.view_as_torch()[:, :(cached_prompt_len + prompt_len), :]
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
        h, s, d = mismatches[0][i], mismatches[1][i], mismatches[2][i]
        print(f"Mismatch at head={h}, seq={s}, dim={d}: ref={out_ref[h,s,d]}, aie={aie_out[h,s,d]}, diff={diff[h,s,d]}")

assert torch.allclose(out_ref, aie_out, atol=1e-2, rtol=1e-2)

