#!/usr/bin/env python3
"""INT8 GEMM on the XDNA2 NPU via patched IRON GEMM (dtype_in="i8").

Builds a 2048x2048x2048 i8->i32 GEMM across all 8 NPU columns (32 AIE
tiles), verifies against an exact numpy int32 reference, and reports
achieved INT8 TOPS from the NPU's own cycle counter.

Usage:
  PYTHONPATH=/usr/lib/python3/dist-packages python run_int8_gemm.py [M K N]
"""
import sys
import time
import numpy as np

sys.path.insert(0, "/home/bcloud/amd-oss/iron")

from iron.common.context import AIEContext
from iron.operators import GEMM
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

M, K, N = 2048, 2048, 2048
if len(sys.argv) > 3:
    M, K, N = map(int, sys.argv[1:4])

TM = TK = TN = 64
COLS = 8

rng = np.random.default_rng(0)
A_np = rng.integers(-8, 8, size=(M, K), dtype=np.int8)
B_np = rng.integers(-8, 8, size=(K, N), dtype=np.int8)

# Exact CPU reference (int32 accumulation, no rounding).
ref = A_np.astype(np.int32) @ B_np.astype(np.int32)

ctx = AIEContext()
ctx.build_dir.mkdir(parents=True, exist_ok=True)
print(f"[int8-gemm] M={M} K={K} N={N} tiles=({TM},{TK},{TN}) cols={COLS} dtype=i8->i32")

op = (
    GEMM(
        M=M, K=K, N=N,
        tile_m=TM, tile_k=TK, tile_n=TN,
        num_aie_columns=COLS,
        dtype_in="i8",
        dtype_out="i32",
        context=ctx,
    )
    .compile()
    .get_callable()
)

A = XRTTensor((M, K), dtype=np.int8)
B = XRTTensor((K, N), dtype=np.int8)
C = XRTTensor((M, N), dtype=np.int32)
A.numpy()[:] = A_np
B.numpy()[:] = B_np

# Warm-up + timing (npu_time comes from the AIE event counter).
res = op(A, B, C)
t_warm = res.npu_time

t0 = time.perf_counter()
res = op(A, B, C)
t_host = time.perf_counter() - t0
t_npu = res.npu_time

C_np = C.to_torch().numpy()  # syncs device -> host

n_ops = 2 * M * K * N
t_npu_s = t_npu * 1e-9
print(f"[int8-gemm] warm npu_time={t_warm} ns")
print(f"[int8-gemm] host wall  = {t_host*1e3:.2f} ms  ({n_ops/t_host/1e12:.2f} TOPS incl. copies)")
print(f"[int8-gemm] npu_time   = {t_npu_s*1e3:.3f} ms  ({n_ops/t_npu_s/1e12:.2f} TOPS pure compute)")

exact = np.array_equal(C_np, ref)
max_abs = int(np.abs(C_np.astype(np.int64) - ref.astype(np.int64)).max()) if not exact else 0
n_bad = int(np.count_nonzero(C_np != ref)) if not exact else 0
print(f"[int8-gemm] exact match: {exact}  (max_abs_err={max_abs}, bad_elems={n_bad}/{C_np.size})")
print(f"[int8-gemm] C[0,:4]={C_np[0,:4].tolist()}  ref[0,:4]={ref[0,:4].tolist()}")
