#!/usr/bin/env python3
"""Repeat 2048^3 INT8 GEMM 5x in one process, report best/mean TOPS."""
import sys
import numpy as np

sys.path.insert(0, "/home/bcloud/amd-oss/iron")

from iron.common.context import AIEContext
from iron.operators import GEMM
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

M, K, N = 2048, 2048, 2048
rng = np.random.default_rng(0)
A_np = rng.integers(-8, 8, size=(M, K), dtype=np.int8)
B_np = rng.integers(-8, 8, size=(K, N), dtype=np.int8)
ref = A_np.astype(np.int32) @ B_np.astype(np.int32)

ctx = AIEContext()
ctx.build_dir.mkdir(parents=True, exist_ok=True)
op = (
    GEMM(M=M, K=K, N=N, tile_m=64, tile_k=64, tile_n=64, num_aie_columns=8,
         dtype_in="i8", dtype_out="i32", context=ctx)
    .compile()
    .get_callable()
)
A = XRTTensor((M, K), dtype=np.int8)
B = XRTTensor((K, N), dtype=np.int8)
C = XRTTensor((M, N), dtype=np.int32)
A.numpy()[:] = A_np
B.numpy()[:] = B_np

op(A, B, C)  # warm
times = []
for _ in range(5):
    res = op(A, B, C)
    times.append(res.npu_time * 1e-9)
C_np = C.to_torch().numpy()
n_ops = 2 * M * K * N
t = np.array(times)
print(f"runs_ms={np.round(t*1e3,2).tolist()}")
print(f"best={n_ops/t.min()/1e12:.2f} TOPS  mean={n_ops/t.mean()/1e12:.2f} TOPS  exact={np.array_equal(C_np, ref)}")
