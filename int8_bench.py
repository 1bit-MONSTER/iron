#!/usr/bin/env python3
"""NPU INT8 GEMM benchmark sweep: TOPS + bit-exactness at multiple shapes.

Usage:
  PYTHONPATH=/usr/lib/python3/dist-packages python int8_bench.py
"""
import sys
import time
import numpy as np

sys.path.insert(0, "/home/bcloud/amd-oss/iron")

from iron.common.context import AIEContext
from iron.operators import GEMM
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

SHAPES = [
    (1024, 512, 1024),
    (2048, 512, 2048),
    (2048, 2048, 2048),
    (2048, 2048, 8192),
]

rng = np.random.default_rng(0)

for M, K, N in SHAPES:
    ctx = AIEContext()
    ctx.build_dir.mkdir(parents=True, exist_ok=True)
    print(f"=== INT8 GEMM {M}x{K}x{N} ===", flush=True)
    A_np = rng.integers(-8, 8, size=(M, K), dtype=np.int8)
    B_np = rng.integers(-8, 8, size=(K, N), dtype=np.int8)
    t0 = time.perf_counter()
    ref = A_np.astype(np.int32) @ B_np.astype(np.int32)
    t_ref = time.perf_counter() - t0

    op = (
        GEMM(M=M, K=K, N=N, tile_m=64, tile_k=64, tile_n=64,
             num_aie_columns=8, dtype_in="i8", dtype_out="i32",
             context=ctx)
        .compile()
        .get_callable()
    )
    A = XRTTensor((M, K), dtype=np.int8)
    B = XRTTensor((K, N), dtype=np.int8)
    C = XRTTensor((M, N), dtype=np.int32)
    A.numpy()[:] = A_np
    B.numpy()[:] = B_np

    res = op(A, B, C)  # warm
    res = op(A, B, C)
    C_np = C.to_torch().numpy()

    exact = bool(np.array_equal(C_np, ref))
    n_ops = 2 * M * K * N
    t_npu = res.npu_time * 1e-9
    print(f"  exact: {exact}  npu: {t_npu*1e3:.2f} ms  {n_ops/t_npu/1e12:.2f} TOPS"
          f"  (CPU ref {t_ref:.2f} s)", flush=True)
