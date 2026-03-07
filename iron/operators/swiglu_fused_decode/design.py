# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from pathlib import Path
from ml_dtypes import bfloat16
import argparse

import aie.dialects.index as index
from aie.dialects.aie import *
from aie.dialects.aiex import *
from aie.helpers.dialects.scf import _for as range_
from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2

"""
Fused SwiGLU decode design: 3-stage tile pipeline with on-chip reduction.

Computes: output = Wdown @ (silu(Wgate @ x) * (Wup @ x))

Stage 1 (per column): Dual-GEMV + SiLU + Mul
  - Reads interleaved Wgate/Wup rows from DDR, x vector from DDR
  - Computes silu(Wgate_partial @ x) * (Wup_partial @ x)
  - Outputs intermediate chunk via inter-tile ObjectFIFO (ON-CHIP)

Stage 2 (per column): Down-projection GEMV
  - Reads intermediate chunk from stage 1 via on-chip ObjectFIFO
  - Reads Wdown column-slice from DDR
  - Computes partial GEMV: Wdown_slice @ intermediate_chunk
  - Outputs partial result to MemTile via ObjectFIFO (ON-CHIP)

Stage 3 (single tile): Reduction
  - Reads concatenated partials from all columns via MemTile join
  - Sums them element-wise to produce the final output
  - Writes final result to DDR

The reduction eliminates host-side partial summation and reduces
DDR output traffic from 4*embedding_dim to 1*embedding_dim.

Runtime.sequence args:
  - arg0: all weights packed [interleaved_gate_up | down_col0 | down_col1 | ...]
  - arg1: input vector x
  - arg2: output (embedding_dim elements, fully reduced)
"""


def my_swiglu_fused_decode(
    dev,
    cols,
    embedding_dim,
    hidden_dim,
    m_input_stage1,
    m_output_stage1=None,
    m_input_stage2=1,
    m_output_stage2=None,
):
    """Generate the fused SwiGLU decode MLIR design.

    Args:
        dev: Device type ("npu" or "npu2")
        cols: Number of AIE columns (4)
        embedding_dim: Input/output dimension (2048 for Llama 3.2 1B)
        hidden_dim: Intermediate dimension (8192 for Llama 3.2 1B)
        m_input_stage1: Tile size for stage1 weight rows per GEMV call
        m_output_stage1: Tile size for stage1 SiLU+Mul output chunk.
                         Defaults to hidden_dim // cols (full column slice).
        m_input_stage2: Tile size for stage2 weight rows per GEMV call
        m_output_stage2: Tile size for stage2 output chunk.
                         Defaults to embedding_dim (full output in one chunk).
    """
    inter_dim_per_col = hidden_dim // cols

    if m_output_stage1 is None:
        m_output_stage1 = inter_dim_per_col
    if m_output_stage2 is None:
        m_output_stage2 = embedding_dim

    # Stage 1 assertions
    assert m_output_stage1 % m_input_stage1 == 0
    assert m_output_stage1 >= m_input_stage1
    assert m_output_stage1 <= inter_dim_per_col
    assert inter_dim_per_col % m_output_stage1 == 0
    assert inter_dim_per_col % m_input_stage1 == 0

    # Stage 2 assertions
    assert m_output_stage2 % m_input_stage2 == 0
    assert m_output_stage2 >= m_input_stage2
    assert m_output_stage2 <= embedding_dim
    assert embedding_dim % m_output_stage2 == 0
    assert embedding_dim % m_input_stage2 == 0

    # Reduction chunk must be 16-aligned for vectorized add
    assert m_output_stage2 % 16 == 0

    assert hidden_dim % cols == 0

    dtype_in = np.dtype[bfloat16]
    dtype_out = np.dtype[bfloat16]

    dev_ty = NPU1() if dev == "npu" else NPU2()

    # --- L1 tile types ---

    # Stage 1: dual-GEMV weight tile and input vector
    L1_A1_ty = np.ndarray[(m_input_stage1, embedding_dim), dtype_in]
    L1_B_ty = np.ndarray[(embedding_dim,), dtype_in]

    # Inter-stage: intermediate vector chunk (on-chip transfer)
    L1_inter_ty = np.ndarray[(m_output_stage1,), dtype_out]

    # Stage 2: down-projection weight tile and output chunk
    L1_A2_ty = np.ndarray[(m_input_stage2, inter_dim_per_col), dtype_in]
    L1_C_ty = np.ndarray[(m_output_stage2,), dtype_out]

    # Reduction: concatenated partials from all columns and final output
    L1_concat_ty = np.ndarray[(cols * m_output_stage2,), dtype_out]
    L1_out_ty = np.ndarray[(m_output_stage2,), dtype_out]

    # --- L3 (DDR) buffer types ---

    # All weights packed: interleaved gate+up (2*hidden_dim rows x embedding_dim cols)
    # followed by down weights sliced per column (cols * embedding_dim x inter_dim_per_col)
    total_weight_elems = (
        2 * hidden_dim * embedding_dim + cols * embedding_dim * inter_dim_per_col
    )
    L3_W_ty = np.ndarray[(total_weight_elems,), dtype_in]
    L3_B_ty = np.ndarray[(embedding_dim,), dtype_in]
    L3_C_ty = np.ndarray[(embedding_dim,), dtype_out]

    # --- Kernel declarations ---

    # Stage 1: GEMV to static buffer (phase selects left/right)
    stage1_matvec = Kernel(
        "swiglu_fused_dual_gemv_bf16",
        "swiglu_fused.o",
        [np.int32, np.int32, np.int32, L1_A1_ty, L1_B_ty, np.int32],
    )

    # Stage 1: SiLU+Mul from static buffers to inter-tile FIFO
    stage1_silu_mul = Kernel(
        "swiglu_fused_silu_mul_bf16",
        "swiglu_fused.o",
        [L1_inter_ty, np.int32],
    )

    # Stage 2: Down-projection GEMV
    stage2_matvec = Kernel(
        "swiglu_fused_down_gemv_bf16",
        "swiglu_fused.o",
        [np.int32, np.int32, np.int32, L1_A2_ty, L1_inter_ty, L1_C_ty],
    )

    # Stage 3: Reduction kernel
    reduce_fn = Kernel(
        "swiglu_fused_reduce_bf16",
        "swiglu_fused.o",
        [L1_concat_ty, L1_out_ty, np.int32, np.int32],
    )

    # --- ObjectFIFOs ---

    # Stage 1 input FIFOs (2 per column: weights + vector)
    A1_fifos = [ObjectFifo(L1_A1_ty, name=f"A1_{i}", depth=2) for i in range(cols)]
    B_fifos = [ObjectFifo(L1_B_ty, name=f"B_{i}", depth=1) for i in range(cols)]

    # Inter-stage FIFO: connects stage 1 output to stage 2 input (ON-CHIP)
    # depth=2 allows stage 1 to produce next chunk while stage 2 consumes
    inter_fifos = [
        ObjectFifo(L1_inter_ty, name=f"inter_{i}", depth=2) for i in range(cols)
    ]

    # Stage 2 input FIFO (down weights from DDR)
    A2_fifos = [ObjectFifo(L1_A2_ty, name=f"A2_{i}", depth=2) for i in range(cols)]

    # --- MemTile join for reduction ---
    # Create a concatenated FIFO that joins partials from all columns.
    # The MemTile DMA concatenates cols partial chunks (each m_output_stage2)
    # into a single buffer (cols * m_output_stage2 elements).
    concat_fifo = ObjectFifo(L1_concat_ty, name="concat", depth=2)

    # join() creates per-column sub-FIFOs whose consumers feed into the
    # MemTile link. The producers of these sub-FIFOs are the stage2 Workers.
    C_fifos = concat_fifo.prod().join(
        offsets=[i * m_output_stage2 for i in range(cols)],
        obj_types=[L1_C_ty] * cols,
        names=[f"C_{i}" for i in range(cols)],
        depths=[2] * cols,
    )

    # Output FIFO: reduction tile -> DDR
    out_fifo = ObjectFifo(L1_out_ty, name="out", depth=2)

    # --- Core bodies ---

    def stage1_core_body(A1_fifo, B_fifo, inter_fifo, matvec_fn, silu_mul_fn):
        """Stage 1: Dual-GEMV + SiLU + Mul, output to inter-tile FIFO."""
        for _ in range_(0xFFFFFFFF):
            b = B_fifo.acquire(1)
            for i_idx in range_(inter_dim_per_col // m_output_stage1):
                # Phase 1: Wgate rows -> left_buf (phase=0)
                for j_idx in range_(m_output_stage1 // m_input_stage1):
                    j_i32 = index.casts(T.i32(), j_idx)
                    row_offset = j_i32 * m_input_stage1
                    a = A1_fifo.acquire(1)
                    matvec_fn(
                        m_input_stage1,
                        embedding_dim,
                        row_offset,
                        a,
                        b,
                        0,
                    )
                    A1_fifo.release(1)
                # Phase 2: Wup rows -> right_buf (phase=1)
                for j_idx in range_(m_output_stage1 // m_input_stage1):
                    j_i32 = index.casts(T.i32(), j_idx)
                    row_offset = j_i32 * m_input_stage1
                    a = A1_fifo.acquire(1)
                    matvec_fn(
                        m_input_stage1,
                        embedding_dim,
                        row_offset,
                        a,
                        b,
                        1,
                    )
                    A1_fifo.release(1)
                # Phase 3: silu(left_buf) * right_buf -> inter FIFO
                inter = inter_fifo.acquire(1)
                silu_mul_fn(inter, m_output_stage1)
                inter_fifo.release(1)
            B_fifo.release(1)

    def stage2_core_body(A2_fifo, inter_fifo, C_fifo, matvec_fn):
        """Stage 2: Down-projection GEMV, output to per-column C FIFO."""
        for _ in range_(0xFFFFFFFF):
            inter = inter_fifo.acquire(1)
            for i_idx in range_(embedding_dim // m_output_stage2):
                c = C_fifo.acquire(1)
                for j_idx in range_(m_output_stage2 // m_input_stage2):
                    j_i32 = index.casts(T.i32(), j_idx)
                    row_offset = j_i32 * m_input_stage2
                    a = A2_fifo.acquire(1)
                    matvec_fn(
                        m_input_stage2,
                        inter_dim_per_col,
                        row_offset,
                        a,
                        inter,
                        c,
                    )
                    A2_fifo.release(1)
                C_fifo.release(1)
            inter_fifo.release(1)

    def reduce_core_body(concat_in, out_fifo, reduce_kernel):
        """Stage 3: Sum concatenated partials and write final output."""
        for _ in range_(0xFFFFFFFF):
            for _ in range_(embedding_dim // m_output_stage2):
                partials = concat_in.acquire(1)
                out = out_fifo.acquire(1)
                reduce_kernel(partials, out, m_output_stage2, cols)
                out_fifo.release(1)
                concat_in.release(1)

    # --- Workers ---

    stage1_workers = [
        Worker(
            stage1_core_body,
            [
                A1_fifos[i].cons(),
                B_fifos[i].cons(),
                inter_fifos[i].prod(),
                stage1_matvec,
                stage1_silu_mul,
            ],
        )
        for i in range(cols)
    ]

    stage2_workers = [
        Worker(
            stage2_core_body,
            [
                A2_fifos[i].cons(),
                inter_fifos[i].cons(),
                C_fifos[i].prod(),
                stage2_matvec,
            ],
        )
        for i in range(cols)
    ]

    reduce_worker = Worker(
        reduce_core_body,
        [concat_fifo.cons(), out_fifo.prod(), reduce_fn],
    )

    # --- TensorAccessPatterns ---

    # Offset into the packed weight buffer where down weights start
    down_weights_offset = 2 * hidden_dim * embedding_dim
    rows_per_col = hidden_dim // cols

    # Stage 1: interleaved gate+up weights per column
    A1_taps = [
        TensorAccessPattern(
            tensor_dims=(total_weight_elems,),
            offset=col * 2 * rows_per_col * embedding_dim,
            sizes=[1, 1, 1, 2 * rows_per_col * embedding_dim],
            strides=[0, 0, 0, 1],
        )
        for col in range(cols)
    ]

    # Stage 2: down weights per column
    A2_taps = [
        TensorAccessPattern(
            tensor_dims=(total_weight_elems,),
            offset=down_weights_offset + col * embedding_dim * inter_dim_per_col,
            sizes=[1, 1, 1, embedding_dim * inter_dim_per_col],
            strides=[0, 0, 0, 1],
        )
        for col in range(cols)
    ]

    # --- Runtime sequence ---

    rt = Runtime()
    with rt.sequence(L3_W_ty, L3_B_ty, L3_C_ty) as (W, B, C):
        rt.start(*stage1_workers, *stage2_workers, reduce_worker)
        tg = rt.task_group()
        for i in range(cols):
            rt.fill(A1_fifos[i].prod(), W, A1_taps[i], task_group=tg)
            rt.fill(B_fifos[i].prod(), B, task_group=tg)
            rt.fill(A2_fifos[i].prod(), W, A2_taps[i], task_group=tg)
        rt.drain(out_fifo.cons(), C, task_group=tg, wait=True)
        rt.finish_task_group(tg)

    return Program(dev_ty, rt).resolve_program(SequentialPlacer())


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        prog="AIE Fused SwiGLU Decode Design",
    )
    argparser.add_argument("--dev", type=str, choices=["npu", "npu2"], default="npu")
    argparser.add_argument("--embedding-dim", type=int, required=True)
    argparser.add_argument("--hidden-dim", type=int, required=True)
    argparser.add_argument(
        "--m-input-stage1",
        type=int,
        required=True,
        dest="m_input_stage1",
    )
    argparser.add_argument(
        "--m-output-stage1",
        type=int,
        default=None,
        dest="m_output_stage1",
    )
    argparser.add_argument(
        "--m-input-stage2",
        type=int,
        default=1,
        dest="m_input_stage2",
    )
    argparser.add_argument(
        "--m-output-stage2",
        type=int,
        default=None,
        dest="m_output_stage2",
    )
    argparser.add_argument("--cols", type=int, required=True)
    argparser.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        help="Output file path for the generated MLIR module",
    )
    args = argparser.parse_args()
    module = my_swiglu_fused_decode(
        args.dev,
        args.cols,
        args.embedding_dim,
        args.hidden_dim,
        args.m_input_stage1,
        args.m_output_stage1,
        args.m_input_stage2,
        args.m_output_stage2,
    )

    output_file_path = Path(args.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
