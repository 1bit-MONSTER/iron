#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Diagnostic script for mlp_block_decode mismatch.
#
# Isolates whether the bug lives in:
#   Stage A: AIERMSNorm (does it produce correct x_normed?)
#   Stage B: AIESwiGLUFusedDecode fed x_normed  (does it produce correct output?)
#
# Each stage is run as a standalone operator with its own fresh AIEContext,
# using the same seeds / data as the mlp_block_decode test.
#
# Run:
#   source ironenv/bin/activate && source /opt/xilinx/xrt/setup.sh
#   python3 /scratch/jmelber/IRON/debug_mlp_block.py

import sys
import torch
import numpy as np
from ml_dtypes import bfloat16

# ---------------------------------------------------------------------------
# Path setup — run from repo root so relative imports resolve
# ---------------------------------------------------------------------------
import os
os.chdir("/scratch/jmelber/IRON")
sys.path.insert(0, "/scratch/jmelber/IRON")

from iron.common import AIEContext
from iron.common.test_utils import nearly_equal
from iron.common.utils import torch_to_numpy

from iron.operators.mlp_block_decode.reference import generate_golden_reference
from iron.operators.rms_norm.op import AIERMSNorm
from iron.operators.swiglu_fused_decode.op import AIESwiGLUFusedDecode

# ---------------------------------------------------------------------------
# Parameters — must match the mlp_block_decode test
# ---------------------------------------------------------------------------
EMBEDDING_DIM = 2048
HIDDEN_DIM = 2048
NUM_AIE_COLUMNS = 4

# Tolerances used by the test
REL_TOL = 0.30
ABS_TOL = 1.0

# RMSNorm config that matches what mlp_block_decode embeds:
#   single column (1 col), 2 channels, tile_size = embedding_dim
#   (the MLP block runs a single-tile weighted RMSNorm over the full vector)
RMS_NUM_COLS = 1
RMS_NUM_CHANNELS = 2
RMS_TILE_SIZE = EMBEDDING_DIM // RMS_NUM_COLS  # = 2048

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def sep(title):
    print()
    print("=" * 70)
    print(f"  {title}")
    print("=" * 70)


def count_mismatches(actual_np, expected_np, rel_tol, abs_tol, label, max_print=10):
    assert len(actual_np) == len(expected_np), "length mismatch"
    errors = []
    for i in range(len(actual_np)):
        if not nearly_equal(float(actual_np[i]), float(expected_np[i]), rel_tol, abs_tol):
            errors.append(i)
            if len(errors) <= max_print:
                print(
                    f"  [{label}] mismatch [{i}]: "
                    f"expected {float(expected_np[i]):.4f}, "
                    f"got {float(actual_np[i]):.4f}, "
                    f"diff {abs(float(actual_np[i]) - float(expected_np[i])):.4f}"
                )
    return errors


# ---------------------------------------------------------------------------
# Step 1: Build the golden reference (same seed / dtype as the test)
# ---------------------------------------------------------------------------
sep("Step 1: Build golden reference (mlp_block_decode)")

golden = generate_golden_reference(
    embedding_dim=EMBEDDING_DIM,
    hidden_dim=HIDDEN_DIM,
)

x           = golden["x"]            # (embedding_dim,) bf16
norm_weight = golden["norm_weight"]  # (embedding_dim,) bf16
w_gate      = golden["w_gate"]       # (hidden_dim, embedding_dim) bf16
w_up        = golden["w_up"]         # (hidden_dim, embedding_dim) bf16
w_down      = golden["w_down"]       # (embedding_dim, hidden_dim) bf16
x_normed_ref = golden["x_normed"]   # (embedding_dim,) bf16  — RMSNorm output
output_ref  = golden["output"]       # (embedding_dim,) bf16  — final MLP output

print(f"x          : shape={x.shape}, dtype={x.dtype}")
print(f"norm_weight: shape={norm_weight.shape}, dtype={norm_weight.dtype}")
print(f"x_normed   : shape={x_normed_ref.shape}, dtype={x_normed_ref.dtype}")
print(f"output_ref : shape={output_ref.shape}, dtype={output_ref.dtype}")
print(f"x[:5]          = {x[:5].tolist()}")
print(f"x_normed_ref[:5] = {x_normed_ref[:5].tolist()}")
print(f"output_ref[:5] = {output_ref[:5].tolist()}")


# ---------------------------------------------------------------------------
# Step 2: Run standalone AIERMSNorm with the exact same x and norm_weight
# ---------------------------------------------------------------------------
sep("Step 2: AIERMSNorm standalone — does it produce correct x_normed?")

rms_context = AIEContext()

rms_op = AIERMSNorm(
    size=EMBEDDING_DIM,
    num_aie_columns=RMS_NUM_COLS,
    num_channels=RMS_NUM_CHANNELS,
    tile_size=RMS_TILE_SIZE,
    weighted=True,
    context=rms_context,
)

# Assign the exact norm_weight from the golden reference.
# NOTE: AIERMSNorm.weight must be set BEFORE compile/prepare_runtime because
# the weight is baked into the static_data buffer during set_up_runtime().
import torch.nn as nn
rms_op.weight = nn.Parameter(norm_weight.clone())

print("Compiling AIERMSNorm...")
rms_context.compile_all()
rms_context.prepare_runtime()

# Write input; output buffer is zeroed by write_buffer call
from ml_dtypes import bfloat16 as ml_bfloat16
rms_op.write_buffer("input1", torch_to_numpy(x))
rms_op.write_buffer("output", np.zeros(EMBEDDING_DIM, dtype=ml_bfloat16))

rms_op.run_runlist()

x_normed_aie = rms_op.read_buffer_as_torch("output", shape=(EMBEDDING_DIM,), dtype=ml_bfloat16)

print(f"AIE x_normed[:5]  = {x_normed_aie[:5].tolist()}")
print(f"Ref x_normed[:5]  = {x_normed_ref[:5].tolist()}")

rms_errors = count_mismatches(
    torch_to_numpy(x_normed_aie).reshape(-1),
    torch_to_numpy(x_normed_ref).reshape(-1),
    rel_tol=0.04,  # tight: standalone rms_norm tolerance
    abs_tol=1e-6,
    label="rms_norm",
)

if rms_errors:
    print(f"\nRMSNorm has {len(rms_errors)}/{EMBEDDING_DIM} mismatches vs reference.")
else:
    print(f"\nRMSNorm PASSED — AIE output matches reference exactly (tol=0.04/1e-6).")


# ---------------------------------------------------------------------------
# Step 3: Run AIESwiGLUFusedDecode with the REFERENCE x_normed
#         (bypasses any RMSNorm error to check SwiGLU in isolation)
# ---------------------------------------------------------------------------
sep("Step 3a: AIESwiGLUFusedDecode with REFERENCE x_normed — SwiGLU isolation test")

swiglu_ref_context = AIEContext()

swiglu_ref_op = AIESwiGLUFusedDecode(
    embedding_dim=EMBEDDING_DIM,
    hidden_dim=HIDDEN_DIM,
    num_aie_columns=NUM_AIE_COLUMNS,
    context=swiglu_ref_context,
)
swiglu_ref_op.weights_gate = w_gate
swiglu_ref_op.weights_up   = w_up
swiglu_ref_op.weights_down = w_down

print("Compiling AIESwiGLUFusedDecode (reference x_normed path)...")
swiglu_ref_context.compile_all()
swiglu_ref_context.prepare_runtime()

# Write x_normed from the GOLDEN REFERENCE (not the AIE output)
swiglu_ref_op.write_buffer("input", torch_to_numpy(x_normed_ref))
swiglu_ref_op.run_runlist()

partials_ref = swiglu_ref_op.read_buffer_as_torch(
    "output_partials",
    (NUM_AIE_COLUMNS, EMBEDDING_DIM),
)
output_aie_ref_path = partials_ref.sum(dim=0)

print(f"AIE output (ref x_normed)[:5]  = {output_aie_ref_path[:5].tolist()}")
print(f"Ref output[:5]                 = {output_ref[:5].tolist()}")

swiglu_ref_errors = count_mismatches(
    torch_to_numpy(output_aie_ref_path).reshape(-1),
    torch_to_numpy(output_ref).reshape(-1),
    rel_tol=REL_TOL,
    abs_tol=ABS_TOL,
    label="swiglu(ref_x_normed)",
)

if swiglu_ref_errors:
    print(
        f"\nSwiGLU(ref x_normed) has {len(swiglu_ref_errors)}/{EMBEDDING_DIM} mismatches. "
        f"BUG IS IN THE SWIGLU STAGE (not RMSNorm handoff)."
    )
else:
    print(
        f"\nSwiGLU(ref x_normed) PASSED ({REL_TOL}/{ABS_TOL} tol). "
        f"SwiGLU stage is correct when fed reference-normalized input."
    )


# ---------------------------------------------------------------------------
# Step 4: Run AIESwiGLUFusedDecode with the AIE x_normed
#         (end-to-end chained, mirrors what mlp_block_decode does)
# ---------------------------------------------------------------------------
sep("Step 3b: AIESwiGLUFusedDecode with AIE x_normed — end-to-end chain")

swiglu_aie_context = AIEContext()

swiglu_aie_op = AIESwiGLUFusedDecode(
    embedding_dim=EMBEDDING_DIM,
    hidden_dim=HIDDEN_DIM,
    num_aie_columns=NUM_AIE_COLUMNS,
    context=swiglu_aie_context,
)
swiglu_aie_op.weights_gate = w_gate
swiglu_aie_op.weights_up   = w_up
swiglu_aie_op.weights_down = w_down

print("Compiling AIESwiGLUFusedDecode (AIE x_normed path)...")
swiglu_aie_context.compile_all()
swiglu_aie_context.prepare_runtime()

# Write x_normed from the AIE RMSNorm output
swiglu_aie_op.write_buffer("input", torch_to_numpy(x_normed_aie))
swiglu_aie_op.run_runlist()

partials_aie = swiglu_aie_op.read_buffer_as_torch(
    "output_partials",
    (NUM_AIE_COLUMNS, EMBEDDING_DIM),
)
output_aie_chained = partials_aie.sum(dim=0)

print(f"AIE output (chained)[:5] = {output_aie_chained[:5].tolist()}")
print(f"Ref output[:5]           = {output_ref[:5].tolist()}")

chained_errors = count_mismatches(
    torch_to_numpy(output_aie_chained).reshape(-1),
    torch_to_numpy(output_ref).reshape(-1),
    rel_tol=REL_TOL,
    abs_tol=ABS_TOL,
    label="swiglu(aie_x_normed)",
)

if chained_errors:
    print(
        f"\nChained pipeline has {len(chained_errors)}/{EMBEDDING_DIM} mismatches vs reference."
    )
else:
    print(f"\nChained pipeline PASSED ({REL_TOL}/{ABS_TOL} tol).")


# ---------------------------------------------------------------------------
# Step 5: Summary and diagnosis
# ---------------------------------------------------------------------------
sep("Step 4: Diagnosis Summary")

print(f"  RMSNorm standalone errors      : {len(rms_errors)}/{EMBEDDING_DIM}")
print(f"  SwiGLU(ref x_normed) errors    : {len(swiglu_ref_errors)}/{EMBEDDING_DIM}")
print(f"  SwiGLU(AIE x_normed) errors    : {len(chained_errors)}/{EMBEDDING_DIM}")
print()

if len(rms_errors) == 0 and len(swiglu_ref_errors) == 0 and len(chained_errors) == 0:
    print("CONCLUSION: All stages pass in isolation AND when chained.")
    print("  The mlp_block_decode mismatch is likely in the fused design's")
    print("  buffer handoff (TG1 drain -> TG2 fill of the same DDR buffer)")
    print("  or in how the fused kernel packs/offsets the weights_all buffer.")
elif len(rms_errors) > 0:
    print("CONCLUSION: RMSNorm itself is producing wrong output.")
    print("  Fix the RMSNorm AIE kernel or its weight layout before investigating SwiGLU.")
elif len(swiglu_ref_errors) > 0:
    print("CONCLUSION: SwiGLU has a bug independent of RMSNorm output.")
    print("  The SwiGLU stage produces wrong answers even when given the correct")
    print("  normalized input. Investigate swiglu_fused kernel / weight packing.")
elif len(chained_errors) > 0 and len(rms_errors) == 0 and len(swiglu_ref_errors) == 0:
    print("CONCLUSION: Both stages are correct in isolation but the RMSNorm")
    print("  output (x_normed_aie) differs enough from the reference that it")
    print("  causes out-of-tolerance errors after SwiGLU amplifies the delta.")
    print("  Check rms_norm tolerance and whether the fused design reads the")
    print("  same normalized vector that rms_norm wrote.")
else:
    print("CONCLUSION: Inconclusive. Review the per-stage error counts above.")

print()
print("Script complete.")
