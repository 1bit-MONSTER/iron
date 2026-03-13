<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# NPU Data Movement Guide

A comprehensive reference for designing MLIR-AIE operators in the IRON framework.
Covers the NPU memory hierarchy, ObjectFIFO API, TensorAccessPatterns (TAPs),
MemTile routing, multi-column designs, and common pitfalls.

---

## Table of Contents

1. [NPU Memory Hierarchy](#1-npu-memory-hierarchy)
2. [ObjectFIFO Basics](#2-objectfifo-basics)
3. [TensorAccessPatterns (TAPs)](#3-tensoraccesspatterns-taps)
4. [MemTile Routing](#4-memtile-routing)
5. [Data Tiling Through MemTile](#5-data-tiling-through-memtile)
6. [Multi-Column Designs](#6-multi-column-designs)
7. [Common Patterns and Pitfalls](#7-common-patterns-and-pitfalls)
8. [Design Checklist](#8-design-checklist)

---

## 1. NPU Memory Hierarchy

The AMD Ryzen AI NPU (AIE-ML / AIE2) has a three-level memory hierarchy.
Data moves from host DDR through ShimDMA tiles, optionally through MemTiles,
and into ComputeTile local memory. Understanding each level's capacity,
bandwidth, and DMA channel limits is essential for correct designs.

### 1.1 Tile Layout (NPU2)

```
Row 5: C C C C  (ComputeTiles — 64 KB L1 each, 2 DMA in + 2 DMA out)
Row 4: C C C C
Row 3: C C C C
Row 2: C C C C
Row 1: M M M M  (MemTiles  — 512 KB L2 each, 6 DMA in + 6 DMA out)
Row 0: S S S S  (ShimTiles — DDR interface, 2 DMA in + 2 DMA out)
       Col 0-3   (up to 8 columns on NPU2)
```

### 1.2 Memory Levels

| Level | Location | Capacity | DMA Channels | Role |
|-------|----------|----------|--------------|------|
| **L3 (DDR)** | Host memory | GBs | N/A | Input/output buffers, weights |
| **ShimDMA** | Row 0 | N/A (pass-through) | 2 in + 2 out per tile | DDR ↔ AIE array gateway |
| **L2 (MemTile)** | Row 1 | 512 KB per tile | 6 in + 6 out per tile | Shared buffer, broadcast/join hub |
| **L1 (ComputeTile)** | Rows 2–5 | 64 KB per tile | 2 in + 2 out per tile | Local compute scratchpad |

### 1.3 Data Flow

```
DDR (Host)
    │
    ▼  ShimDMA (npu_dma_memcpy_nd / rt.fill / rt.drain)
Row 0: ShimTile
    │
    ▼  ObjectFIFO (automatic DMA)
Row 1: MemTile (optional — forward / split / join)
    │
    ▼  ObjectFIFO (automatic DMA)
Row 2+: ComputeTile (kernel execution)
```

Data can skip the MemTile and flow directly from ShimDMA to ComputeTile
(e.g., `conv2d` does this). MemTile is used when you need broadcasting,
fan-out distribution, fan-in merging, or larger buffering than L1 allows.

### 1.4 DMA Channel Budget

Each ObjectFIFO endpoint (producer or consumer placed on a tile) consumes
one DMA channel on that tile. Exceeding the limit causes a placement error.

| Tile Type | Input Channels | Output Channels | ObjectFIFO Limit |
|-----------|---------------|-----------------|------------------|
| ComputeTile | 2 | 2 | Max 2 input FIFOs + 2 output FIFOs |
| MemTile | 6 | 6 | Max 6 input FIFOs + 6 output FIFOs |
| ShimTile | 2 | 2 | Max 2 input FIFOs + 2 output FIFOs |

**Common error when exceeded:**
```
'aie.tile' op number of input DMA channel exceeded!
```

### 1.5 Buffer Descriptors (BDs)

Each ShimDMA has 16 Buffer Descriptors. Each `rt.fill()` or `rt.drain()`
call uses one BD. Reuse BDs after synchronization via `dma_wait()` or
`rt.finish_task_group()`.

**BD dimension constraints:**

| Field | Max Value | Notes |
|-------|-----------|-------|
| d3 (wrap/repeat) | 64 | Outermost dimension |
| d2 (size) | 1023 | Middle dimensions |
| d1 (size) | 1023 | Middle dimensions |
| d0 (size) | 1023 | Innermost; must be **even** for bf16 |
| Strides | ~2^20 | ~1M elements |

---

## 2. ObjectFIFO Basics

ObjectFIFO is the primary data movement abstraction in IRON/MLIR-AIE.
It represents a synchronized circular buffer between a producer tile and
one or more consumer tiles. The runtime automatically configures DMAs,
locks, and AXI stream routing.

### 2.1 Creating an ObjectFIFO

```python
from aie.iron import ObjectFifo
import numpy as np
from ml_dtypes import bfloat16

# Define the buffer element type
line_type = np.ndarray[(1024,), np.dtype[bfloat16]]

# Create a FIFO with depth 2 (double-buffering)
of_data = ObjectFifo(line_type, name="data", depth=2)
```

**Constructor parameters:**

```python
ObjectFifo(
    obj_type,                    # np.ndarray type: shape + dtype
    depth=2,                     # Circular buffer depth (default: 2)
    name=None,                   # Human-readable name (auto-generated if None)
    dims_to_stream=None,         # Producer DMA layout transform [(size, stride), ...]
    dims_from_stream_per_cons=None,  # Default consumer DMA layout transform
    plio=False,                  # PLIO mode (rare)
)
```

### 2.2 Producer and Consumer Handles

Each ObjectFIFO has exactly **one producer** and **one or more consumers**.
Handles are obtained via `.prod()` and `.cons()`:

```python
# Producer handle (singleton — multiple calls return same handle)
prod_handle = of_data.prod()

# Consumer handles (each call creates a NEW consumer)
cons_handle_1 = of_data.cons()
cons_handle_2 = of_data.cons()  # Second consumer → broadcast
```

**Per-endpoint depth override:**
```python
prod_handle = of_data.prod(depth=3)      # Producer gets 3 buffers
cons_handle = of_data.cons(depth=4)      # This consumer gets 4 buffers
```

### 2.3 Acquire / Release

Inside a Worker's core function, use `acquire()` to get buffer access and
`release()` to signal completion:

```python
def core_fn(of_in, of_out, kernel_fn):
    for _ in range_(N):
        # Acquire one input and one output buffer
        elem_in = of_in.acquire(1)
        elem_out = of_out.acquire(1)

        # Call the AIE kernel
        kernel_fn(elem_in, elem_out, size)

        # Release buffers for DMA reuse
        of_in.release(1)
        of_out.release(1)
```

**Key rules:**
- `acquire(N)` blocks until N buffers are available from the other endpoint
- `release(N)` frees N buffers (oldest first)
- `N` must be ≤ FIFO depth
- Unreleased objects persist across acquire calls (sliding window)

### 2.4 Sliding Window Pattern

Acquire more than you release to implement a sliding window:

```python
# 3x3 conv sliding window: depth=3, acquire(3), release(1)
of_rows = ObjectFifo(row_type, name="rows", depth=3)

def conv3x3_core(of_in, of_out, kernel_fn):
    for _ in range_(height - 2):
        rows = of_in.acquire(3)       # Get 3 consecutive rows
        out = of_out.acquire(1)
        kernel_fn(rows[0], rows[1], rows[2], out)
        of_in.release(1)              # Release oldest row (slide by 1)
        of_out.release(1)
```

**Warning:** `acquire(N)` with N ≥ 5 may deadlock. Prefer the "strip" pattern
(Section 7.1) for large kernel sizes.

### 2.5 Connecting to Workers

```python
from aie.iron import Kernel, Worker

# Load kernel binary
my_kernel = Kernel("process_data", "kernel.o", [line_type, line_type, np.int32])

# Create worker with FIFO handles
worker = Worker(
    core_fn,
    fn_args=[of_data.cons(), of_out.prod(), my_kernel],
)
```

### 2.6 Runtime Sequence (Host ↔ AIE)

The Runtime fills FIFOs from host buffers and drains results back:

```python
from aie.iron import Runtime

rt = Runtime()
with rt.sequence(input_type, weights_type, output_type) as (inp, wts, out):
    rt.start(worker)

    # Fill input FIFO from host DDR
    rt.fill(of_data.prod(), inp)

    # Drain output FIFO to host DDR
    rt.drain(of_out.cons(), out, wait=True)
```

**Task groups** manage BD reuse for iterative designs:

```python
tg = rt.task_group()
for tile_idx in range(n_tiles):
    rt.fill(of_in.prod(), inp, tap=in_taps[tile_idx], task_group=tg)
    rt.drain(of_out.cons(), out, tap=out_taps[tile_idx], wait=True, task_group=tg)
rt.finish_task_group(tg)
```

---

## 3. TensorAccessPatterns (TAPs)

TAPs describe how to tile, stride, and offset into host DDR buffers when
issuing DMA transfers via `rt.fill()` and `rt.drain()`. They enable a
single DMA command to transfer complex multi-dimensional slices.

### 3.1 TAP Structure

A TAP specifies a 4D nested loop over a tensor:

```python
from aie.helpers.taplib import TensorAccessPattern

tap = TensorAccessPattern(
    tensor_dims=(1, total_size),     # Shape of the full DDR tensor
    offset=start_offset,             # Starting element offset
    sizes=[d3, d2, d1, d0],          # Iteration counts per dimension
    strides=[s3, s2, s1, s0],        # Element strides per dimension
)
```

**Equivalent nested loop:**
```
for i3 in range(d3):                          # Outermost
    for i2 in range(d2):
        for i1 in range(d1):
            for i0 in range(d0):              # Innermost
                addr = offset + i3*s3 + i2*s2 + i1*s1 + i0*s0
                transfer element at addr
```

**Total elements transferred:** `d3 × d2 × d1 × d0`

### 3.2 BD Dimension Constraints

| Dimension | Max Size | Notes |
|-----------|----------|-------|
| d3 | 64 | Outermost wrap; often used for height or batch |
| d2 | 1023 | |
| d1 | 1023 | |
| d0 | 1023 | Must be **even** for bf16 (2-byte elements) |
| Strides | ~2^20 | Large strides are fine |

### 3.3 Linear Transfer (Simple Case)

Transfer N contiguous elements:

```python
tap = TensorAccessPattern(
    (1, N),
    offset=0,
    sizes=[1, 1, 1, N],        # All in d0
    strides=[0, 0, 0, 1],      # Contiguous
)
```

### 3.4 Strided Row Transfer (2D Slice)

Transfer `height` rows of `width` elements from a matrix with `row_stride`:

```python
# Matrix is [H, W] in DDR; transfer a tile of [tile_h, tile_w] at (row_off, col_off)
tap = TensorAccessPattern(
    (1, H * W),
    offset=row_off * W + col_off,
    sizes=[1, 1, tile_h, tile_w],
    strides=[0, 0, W, 1],          # Stride by full row width
)
```

### 3.5 TAP Factorization for Large Tensors

When any dimension exceeds BD limits (d3 > 64, d0-d2 > 1023), decompose:

```python
def _factorize_tensor(total: int) -> tuple[int, int, int, int]:
    """Factor total elements into (d3, d2, d1, d0) within BD constraints."""
    _D0_MAX = 1023
    _D12_MAX = 1023
    _BD_WRAP_MAX = 64     # d3 constraint

    d3 = min(total, _BD_WRAP_MAX)
    while d3 >= 1:
        if total % d3 == 0:
            rest = total // d3
            d0 = _find_even_d0(rest)    # Must be even for bf16
            if d0 is not None:
                rest2 = rest // d0
                d1 = min(rest2, _D12_MAX)
                while d1 > 1 and rest2 % d1 != 0:
                    d1 -= 1
                d2 = rest2 // d1
                if d2 <= _D12_MAX:
                    return (d3, d2, d1, d0)
        d3 -= 1
    raise ValueError(f"Cannot factorize {total}")
```

*From `iron/operators/conv2d/design.py`*

### 3.6 Channel-Group Decomposition

For operators with large channel counts (e.g., pooling with C=128),
a single row may exceed d0=1023. Decompose using channel groups:

```python
# MaxPool2d: input strip = kernel_size rows × channels × padded_width
# Decompose: [out_height, kernel_size, n_channel_groups, cg_row_size]
cg_size = 8                              # Channel group size
n_cg = channels // cg_size
cg_row_size = padded_width * cg_size     # Must be ≤ 1023

in_tap = TensorAccessPattern(
    (1, total_input_size),
    offset=0,
    sizes=[out_height, kernel_size, n_cg, cg_row_size],
    strides=[
        row_elems * stride,     # Next output row's input start
        row_elems,              # Next row within strip
        cg_row_size,            # Next channel group
        1,                      # Contiguous within group
    ],
)
```

*From `iron/operators/maxpool2d/design.py`*

### 3.7 Multi-Column Strided Output

When output channels are split across columns, each column's output
occupies a strided slice of the DDR output buffer:

```python
# Column i writes oc_per_col channels; total output row = out_channels × width
output_row_total = out_channels * width

out_tap = TensorAccessPattern(
    (1, total_output_size),
    offset=col_idx * oc_per_col * width,      # Column offset
    sizes=[height, d2, d1, d0],                # Factorized per-column output
    strides=[output_row_total, d1 * d0, d0, 1],  # Stride by full row
)
```

*From `iron/operators/conv2d/design.py`*

### 3.8 Using TAPs with Runtime

```python
rt = Runtime()
with rt.sequence(A_ty, W_ty, C_ty) as (A, W, C):
    rt.start(*workers)

    tg = rt.task_group()

    # Fill with TAP — transfers a tiled slice of A
    rt.fill(of_in.prod(), A, tap=input_tap, task_group=tg)

    # Drain with TAP — writes output to strided DDR location
    rt.drain(of_out.cons(), C, tap=output_tap, wait=True, task_group=tg)

    rt.finish_task_group(tg)
```

### 3.9 TAP Legalization

Some TAPs exceed MemTile BD dimension limits. Linearize them:

```python
def legalize_tap(tap, max_dim_size=1023):
    """Flatten TAP dimensions that exceed hardware limits."""
    sizes = tap._sizes
    if all(s <= max_dim_size for s in sizes):
        return tap
    # Linearize to contiguous 1D
    total = math.prod(sizes)
    tap._sizes = [1, 1, 1, total]
    tap._strides = [0, 0, 0, 1]
    return tap
```

*From `iron/operators/mha/design.py`*

---

## 4. MemTile Routing

The MemTile (L2, 512 KB) acts as a data routing hub between ShimDMA and
ComputeTiles. Three routing operations are supported: **forward**, **split**,
and **join**. All operate at the DMA level — no compute core is used.

### 4.1 Forward (Pass-Through)

Buffers data through MemTile without modification. Use for:
- Adding buffering between DDR and compute tiles
- Enabling `dims_to_stream` layout transformation at the MemTile level
- Skip connections

```python
of_in = ObjectFifo(data_type, name="in", depth=2)

# Forward through any MemTile
of_forwarded = of_in.cons().forward(
    placement=AnyMemTile,        # Auto-select MemTile
    name="forwarded",
    depth=2,
)

# Consumer cores read from the forwarded FIFO
worker = Worker(core_fn, [of_forwarded.cons(), ...])
```

**With layout transformation:**
```python
# Forward + re-tile data at MemTile for microkernel consumption
of_retiled = of_in.cons().forward(
    name="retiled",
    dims_to_stream=[
        (k // s, s * n),    # K-dimension tiling
        (n // t, t),        # N-dimension tiling
        (s, n),             # Inner K block
        (t, 1),             # Inner N block
    ],
    placement=Tile(col, 1),  # Specific MemTile column
)
```

*From `iron/operators/gemm/design.py` — Matrix B forwarding*

**Bypass pattern (DMA-only copy, no kernel):**
```python
# mem_copy operator: forward = pure DMA copy without compute core
if bypass:
    of_outs = [of_ins[i].cons().forward() for i in range(num_cores)]
    # No Worker needed
```

*From `iron/operators/mem_copy/design.py`*

### 4.2 Split (Fan-Out Distribution)

Splits a single large FIFO into N smaller FIFOs at specified offsets.
The MemTile DMA distributes data to multiple compute tiles.

```python
of_in = ObjectFifo(large_type, name="weights_all", depth=1)

# Split into 3 weight FIFOs at byte offsets
of_w1, of_w2, of_w3 = of_in.cons().split(
    offsets=[0, w1_size, w1_size + w2_size],
    obj_types=[w1_type, w2_type, w3_type],
    names=["wts_layer1", "wts_layer2", "wts_layer3"],
    placement=AnyMemTile,
)
```

**With per-output dims_to_stream:**
```python
# GEMM: split matrix A across row tiles, each with 4D access pattern
n_rows = 4
dims = [
    [(m // r, r * k), (k // s, s), (r, k), (s, 1)]
] * n_rows  # Same pattern for each row tile

a_fifos = of_A.cons().split(
    offsets=[m * k * i for i in range(n_rows)],
    obj_types=[A_l1_type] * n_rows,
    names=[f"A_L2L1_{row}" for row in range(n_rows)],
    dims_to_stream=dims,
    placement=Tile(col, 1),
)
```

*From `iron/operators/gemm/design.py`*

### 4.3 Join (Fan-In Merging)

Merges N smaller FIFOs into a single large FIFO at specified offsets.
The MemTile DMA collects data from multiple compute tiles.

```python
of_out = ObjectFifo(large_type, name="output", depth=2)

# Join from 4 cores at offsets
c_fifos = of_out.prod().join(
    offsets=[chunk_size * i for i in range(4)],
    obj_types=[chunk_type] * 4,
    names=[f"C_core{i}" for i in range(4)],
    placement=Tile(col, 1),
)

# Each core produces to its join FIFO
for i in range(4):
    worker = Worker(core_fn, [in_fifos[i].cons(), c_fifos[i].prod(), ...])
```

*From `iron/operators/gemm/design.py`*

### 4.4 MemTile DMA Advantages

| Feature | MemTile | ComputeTile |
|---------|---------|-------------|
| DMA channels | 6 in + 6 out | 2 in + 2 out |
| TAP dimensions | **4D** | 3D |
| Memory | 512 KB | 64 KB |
| Compute | None | Full core |

The MemTile's 6+6 DMA channels allow complex fan-out/fan-in patterns
that would exhaust ComputeTile's 2+2 channels.

### 4.5 MemTile L2 Budget

All MemTile FIFOs share the 512 KB:

```
L2 Budget (512 KB):
  Input broadcast buffer (depth=2):  buf_size × 2
  Weight split buffers (depth=1):    total_weights × 1
  Output join buffer (depth=2):      out_size × 2
  ─────────────────────────────────
  Total must be ≤ 512 KB
```

---

## 5. Data Tiling Through MemTile

The most powerful data movement pattern uses MemTile as a tiling engine:
large DDR tensors are buffered in L2 and re-tiled via `dims_to_stream`
into small chunks for L1 consumption.

### 5.1 Three-Level Hierarchy Pattern

```
DDR [M × K matrix]
    │
    ▼  rt.fill() with TAP (selects tile block)
ShimDMA → MemTile [L2 buffer: n_rows × m × k]
    │
    ▼  split() + dims_to_stream (re-tiles for microkernel)
ComputeTile [L1: m × k per core]
```

### 5.2 GEMM Example: Matrix A Distribution

From `iron/operators/gemm/design.py`:

```python
# Types
A_l2_ty = np.ndarray[(n_aie_rows * m * k,), np.dtype[bfloat16]]  # L2 buffer
A_l1_ty = np.ndarray[(m, k), np.dtype[bfloat16]]                  # L1 per core

# L3 → L2: large chunk from DDR to MemTile
A_l3l2 = ObjectFifo(A_l2_ty, name="A_L3L2", depth=2)

# L2 → L1: split across row cores with vectorized access pattern
A_l2l1_fifos = A_l3l2.cons().split(
    offsets=[m * k * row for row in range(n_aie_rows)],
    obj_types=[A_l1_ty] * n_aie_rows,
    names=[f"A_L2L1_{row}" for row in range(n_aie_rows)],
    dims_to_stream=[
        # 4D vectorized: [m/r blocks, k/s blocks, r rows, s cols]
        [(m // r, r * k), (k // s, s), (r, k), (s, 1)]
    ] * n_aie_rows,
    placement=Tile(col, 1),  # MemTile
)
```

### 5.3 GEMM Example: Matrix B Broadcast

```python
# L3 → L2
B_l3l2 = ObjectFifo(B_l2_ty, name="B_L3L2", depth=2)

# L2 → all rows via forward (broadcast — all row cores read same B tile)
B_l2l1 = B_l3l2.cons().forward(
    obj_type=B_l1_ty,
    name="B_L2L1",
    dims_to_stream=[
        (k // s, s * n), (n // t, t), (s, n), (t, 1)
    ],
    placement=Tile(col, 1),
)

# All row workers consume same B data
for row in range(n_aie_rows):
    Worker(core_fn, [A_l2l1_fifos[row].cons(), B_l2l1.cons(), ...])
```

### 5.4 GEMM Example: Output Join

```python
# Per-column output: join row cores' results at MemTile
C_l2l3 = ObjectFifo(C_l2_ty, name="C_L2L3", depth=2,
                     dims_to_stream=C_dims)

C_l1l2_fifos = C_l2l3.prod().join(
    offsets=[m * n * row for row in range(n_aie_rows)],
    obj_types=[C_l1_ty] * n_aie_rows,
    names=[f"C_L1L2_{row}" for row in range(n_aie_rows)],
    placement=Tile(col, 1),
)
```

### 5.5 MHA Example: Multi-Pipeline Split/Join

From `iron/operators/mha/design.py`:

```python
# Input Q: split across parallel pipelines at MemTile
inQ = ObjectFifo(
    np.ndarray[(n_pipelines * B_q, d), np.dtype[bfloat16]],
    name="inQ",
)
memQ = inQ.cons().split(
    offsets=[B_q * d * i for i in range(n_pipelines)],
    obj_types=[q_type] * n_pipelines,
    names=[f"memQ{i}" for i in range(n_pipelines)],
    dims_to_stream=[(B_q // r, r * d), (d // s, s), (r, d), (s, 1)],
    depths=[2] * n_pipelines,
    placement=Tile(col=6, row=1),
)

# Input K: broadcast via forward (all pipelines share same K)
inK = ObjectFifo(k_type, name="inK", depth=2)
memK = inK.cons().forward(
    name="memK",
    dims_to_stream=[(B_kv // t, t * d), (d // s, s), (t, d), (s, 1)],
    placement=Tile(col=3, row=1),
    depth=2,
)

# Output O: join pipeline results
memO = ObjectFifo(
    np.ndarray[(n_pipelines * B_q, d), np.dtype[bfloat16]],
    name="memO",
)
outO = memO.prod().join(
    offsets=[B_q * d * i for i in range(n_pipelines)],
    obj_types=[q_type] * n_pipelines,
    names=[f"outO{i}" for i in range(n_pipelines)],
    placement=Tile(col=6, row=1),
)
```

### 5.6 When to Use MemTile vs Direct Routing

| Criterion | Use MemTile | Skip MemTile |
|-----------|-------------|--------------|
| Multi-core fan-out/fan-in | Yes (split/join) | N/A |
| Data re-tiling needed | Yes (dims_to_stream) | Simple linear |
| L1 too small for ping-pong | Yes (buffer in L2) | L1 sufficient |
| Single core, simple I/O | No | Yes (direct ShimDMA → core) |
| Weight loading (small, once) | No | Yes (depth=1, direct) |

**Example: Conv2d uses direct routing (no MemTile):**
```python
# Direct ShimDMA → ComputeTile — no MemTile needed
in_fifos = [ObjectFifo(input_row_ty, name=f"in_{i}", depth=2)
            for i in range(num_columns)]
wt_fifos = [ObjectFifo(weights_ty, name=f"wt_{i}", depth=1)
            for i in range(num_columns)]
```

*From `iron/operators/conv2d/design.py`*

---

## 6. Multi-Column Designs

Multi-column designs distribute work across columns of the NPU array.
Each column typically processes a subset of output channels.

### 6.1 Output Channel Tiling

Split output channels across `num_columns` columns:

```python
oc_per_col = out_channels // num_columns
# Each column processes oc_per_col channels
```

**Constraint:** `oc_per_col` must be a multiple of the kernel's vector width
(typically 8 for bf16). This means `out_channels / num_columns` must divide
evenly by 8.

**Known limitation:** 80 output channels cannot be multi-column tiled:
- 80/2 = 40 (not multiple of 8)
- 80/4 = 20 (not multiple of 8)
- 80/8 = 10 (not multiple of 8)

Solution: pad to 88 channels or use weight streaming.

### 6.2 Input Broadcasting

All columns typically receive the same input data. Use broadcast (multiple
consumers on same ObjectFIFO) or separate fills:

```python
# Option A: separate FIFOs per column, filled from same DDR buffer
for col in range(num_columns):
    rt.fill(of_in[col].prod(), input_buf, tap=input_tap, task_group=tg)

# Option B: single FIFO with multiple consumers (broadcast)
of_in = ObjectFifo(input_type, name="input")
workers = [Worker(fn, [of_in.cons(), ...]) for col in range(num_columns)]
```

### 6.3 Weight Distribution

Each column gets its own weight slice:

```python
for col in range(num_columns):
    wt_tap = TensorAccessPattern(
        (1, total_weight_size),
        offset=col * weights_per_col,
        sizes=[1, 1, 1, weights_per_col],
        strides=[0, 0, 0, 1],
    )
    rt.fill(wt_fifos[col].prod(), weights_buf, tap=wt_tap, task_group=tg)
```

### 6.4 Strided Output Collection

Multi-column outputs are interleaved in DDR. Column `i` writes its
`oc_per_col` channels at an offset within each row:

```python
# DDR layout: [height, out_channels, width] with channels from all columns
for col in range(num_columns):
    out_tap = TensorAccessPattern(
        (1, total_output_size),
        offset=col * oc_per_col * width,
        sizes=[height, d2, d1, d0],
        strides=[out_channels * width, d1 * d0, d0, 1],
    )
    rt.drain(out_fifos[col].cons(), output_buf, tap=out_tap,
             wait=True, task_group=tg)
```

### 6.5 Auto-Column Selection

Use `num_aie_columns=0` for automatic selection based on L1 budget:

```python
def _auto_columns(out_channels, in_channels, kernel_size, max_weight_kb=40):
    """Find smallest column count where per-core weights fit in L1."""
    for n_cols in [1, 2, 4, 8]:
        oc_per_col = out_channels // n_cols
        if oc_per_col % 8 != 0:
            continue
        weight_bytes = oc_per_col * in_channels * kernel_size**2 * 2  # bf16
        if weight_bytes <= max_weight_kb * 1024:
            return n_cols
    raise ValueError("Cannot fit weights in L1")
```

---

## 7. Common Patterns and Pitfalls

### 7.1 Strip Pattern for Pooling/Large Kernels

Instead of `acquire(kernel_size)` which risks deadlock for large kernels,
send `kernel_size` contiguous rows as a single FIFO element:

```python
# Strip = kernel_size rows concatenated
strip_size = channels * padded_width * kernel_size
strip_type = np.ndarray[(strip_size,), np.dtype[bfloat16]]

in_fifo = ObjectFifo(strip_type, name="in", depth=2)

# Core acquires one strip (all kernel_size rows at once)
def core_fn(of_in, of_out, kernel_fn):
    for _ in range_(out_height):
        elem_in = of_in.acquire(1)     # One strip
        elem_out = of_out.acquire(1)
        kernel_fn(elem_in, elem_out, out_width, channels, padded_width)
        of_in.release(1)
        of_out.release(1)
```

*From `iron/operators/maxpool2d/design.py`*

### 7.2 Weight Loading (Load-Once Pattern)

Weights are loaded once before processing all rows. Use `depth=1`:

```python
wt_fifo = ObjectFifo(weights_type, name="weights", depth=1)

def core_fn(of_in, of_wt, of_out, kernel_fn):
    elem_wt = of_wt.acquire(1)         # Acquire weights once

    for _ in range_(height):
        elem_in = of_in.acquire(1)
        elem_out = of_out.acquire(1)
        kernel_fn(elem_in, elem_wt, elem_out, ...)
        of_in.release(1)
        of_out.release(1)

    of_wt.release(1)                    # Release weights at end
```

*From `iron/operators/conv2d/design.py`*

### 7.3 L1 Memory Budget Calculation

Every FIFO buffer and static allocation must fit in 64 KB:

```
L1 Budget (64 KB total):
  Input FIFO:   element_size × depth     (e.g., 8KB × 2 = 16KB)
  Weight FIFO:  weight_size × depth      (e.g., 16KB × 1 = 16KB)
  Output FIFO:  element_size × depth     (e.g., 8KB × 2 = 16KB)
  Static bufs:  scratch arrays           (e.g., 4KB)
  Stack:        ~1 KB
  ─────────────────────────────────────
  Total ≤ 64 KB (aim for ≤ 48KB for safety)
```

**Double-buffered strip budget:**
```
strip_size × 2 (input double-buffer)
+ output_row × 2 (output double-buffer)
+ stack (1 KB)
≤ 64 KB
```

If too tight, reduce depth to 1 (sacrificing throughput):

```python
strip_bytes = strip_size * 2    # bf16 = 2 bytes
in_depth = 1 if strip_bytes > 16384 else 2
```

### 7.4 Conv2d Sliding Window (3x3, stride=1)

```python
def core_fn_s1(of_in, of_wt, of_out, kernel_fn):
    elem_wt = of_wt.acquire(1)

    # First row: top padding (row0 used as padding), row0, row1
    elems = of_in.acquire(2)
    elem_out = of_out.acquire(1)
    kernel_fn(elems[0], elems[0], elems[1], elem_wt, elem_out, ..., check=0)
    of_out.release(1)

    # Middle rows: row[i-1], row[i], row[i+1]
    for _ in range_(height - 2):
        elems = of_in.acquire(3)        # Sliding window of 3
        elem_out = of_out.acquire(1)
        kernel_fn(elems[0], elems[1], elems[2], elem_wt, elem_out, ..., check=1)
        of_in.release(1)                # Release oldest row
        of_out.release(1)

    # Last row: row[H-2], row[H-1], bottom padding (row[H-1] reused)
    elems = of_in.acquire(2)
    elem_out = of_out.acquire(1)
    kernel_fn(elems[0], elems[1], elems[1], elem_wt, elem_out, ..., check=2)
    of_in.release(2)
    of_out.release(1)

    of_wt.release(1)
```

*From `iron/operators/conv2d/design.py`*

### 7.5 Fill/Drain Ordering

**Two `rt.fill()` calls to the same FIFO in a `task_group` have NO ordering
guarantee.** The task_group only controls BD await/free bookkeeping.

If you need ordered data, either:
1. Pre-interleave data in DDR before filling
2. Use separate FIFOs (subject to DMA channel limits)

### 7.6 ERT_CMD_STATE_TIMEOUT Debugging

This error means the design deadlocked. Common causes:

| Cause | Fix |
|-------|-----|
| Core waiting on FIFO that DMA never fills | Verify fill/drain count matches acquire/release count |
| DMA misconfiguration (wrong strides/sizes) | Inspect generated MLIR, check TAP arithmetic |
| Stale build artifacts | `rm -rf build/<operator>_*` and rebuild |
| Design never terminates | Ensure core loop has finite iterations |

### 7.7 Stale Build Artifacts

The build system caches `.xclbin` and `.bin` by filename. Always clean
when changing kernels or designs:

```bash
rm -rf build/<operator>_*
```

### 7.8 dims_to_stream Explained

`dims_to_stream` specifies how the DMA reads data from a buffer into the
AXI stream. It's a list of `(size, stride)` tuples forming a nested loop:

```python
# Example: 4D access for a [M, K] matrix tiled as [M/r, K/s, r, s]
dims_to_stream = [
    (M // r, r * K),     # Outer: iterate M/r tile blocks, stride r*K
    (K // s, s),          # Middle: iterate K/s tile blocks, stride s
    (r, K),               # Inner: iterate r rows, stride K (full row width)
    (s, 1),               # Innermost: s contiguous elements
]
```

**Key distinction:**
- `dims_to_stream` on ObjectFifo constructor: applied at the **producer** side
- `dims_to_stream` on `forward()`/`split()`: applied at the **MemTile** output
- `dims_from_stream` on `.cons()`: applied at the **consumer** side

### 7.9 NPU Hardware Context Limits

Each unique XCLBIN gets its own hardware context. NPU2 supports ~32
concurrent contexts system-wide.

**Symptom:** `DRM_IOCTL_AMDXDNA_CREATE_HWCTX` errors in pytest.

**Solutions:**
- Run tests individually: `pytest -k test_name`
- Chain operators into shared XCLBINs via `xclbin.xclbin_input`
- Limit concurrent `aie_context` instances

### 7.10 Static Buffer Alignment

AIE vector operations require 64-byte alignment:

```cpp
// In AIE kernel C++ code:
static bfloat16 scratch[4096] __attribute__((aligned(64)));

// Misaligned buffers cause silent wrong results with:
// aie::load_v<N>() and aie::begin_restrict_vector<N>()
```

---

## 8. Design Checklist

Use this checklist when designing a new IRON operator.

### Phase 1: Requirements

- [ ] **Determine tensor shapes**: input, weights (if any), output
- [ ] **Choose data type**: bfloat16, int8, float32
- [ ] **Identify compute pattern**: elementwise, reduction, sliding window, matrix multiply
- [ ] **Check reference implementation**: write CPU golden reference in `reference.py`

### Phase 2: Memory Planning

- [ ] **Calculate per-core data sizes** (input tile, weight tile, output tile)
- [ ] **L1 budget check**: `input×depth + weights×depth + output×depth + stack(1KB) ≤ 64KB`
- [ ] **Determine number of columns**: auto-select or manual based on L1 budget
- [ ] **Check oc_per_col % 8 == 0** for multi-column designs
- [ ] **L2 budget check** (if using MemTile): all FIFO buffers ≤ 512 KB

### Phase 3: DMA Channel Planning

- [ ] **Count FIFOs per compute tile**: ≤ 2 input + ≤ 2 output
- [ ] **Count FIFOs per MemTile** (if used): ≤ 6 input + ≤ 6 output
- [ ] **Count FIFOs per ShimTile**: ≤ 2 input + ≤ 2 output

### Phase 4: ObjectFIFO Design

- [ ] **Choose FIFO depth**: 2 for double-buffering, 1 for weights, 3+ for sliding window
- [ ] **Choose routing**: direct (ShimDMA → core) or MemTile (forward/split/join)
- [ ] **Design dims_to_stream** if microkernel needs re-tiled layout
- [ ] **Design TAPs** for `rt.fill()` and `rt.drain()`
- [ ] **Check BD constraints**: d3 ≤ 64, d0-d2 ≤ 1023, d0 even for bf16
- [ ] **Factorize** any dimension exceeding BD limits

### Phase 5: Core Function

- [ ] **Write core body**: acquire/release pattern matches fill/drain count
- [ ] **Handle edge cases**: padding for conv (first/last row), partial tiles
- [ ] **Verify acquire(N) ≤ depth** for all FIFOs
- [ ] **Ensure finite termination**: all loops have bounded iteration counts

### Phase 6: Runtime Sequence

- [ ] **Use task_group** if issuing multiple fill/drain calls
- [ ] **Set wait=True** on final drain to synchronize
- [ ] **Call rt.finish_task_group()** to free BDs
- [ ] **Set RTPs** (runtime parameters) before starting computation

### Phase 7: Testing

- [ ] **Clean build**: `rm -rf build/<operator>_*`
- [ ] **Verify reference separately**: check golden values at failing indices
- [ ] **Run on hardware**: full compile → load → execute → verify pipeline
- [ ] **Check tolerances**: standalone ops use `rel_tol=0.04`, composed ops up to `abs_tol=1.0`
- [ ] **Inspect MLIR** if debugging: `print(my_design('npu2', ...))`

---

## Appendix A: API Quick Reference

### ObjectFifo

| Method | Returns | Description |
|--------|---------|-------------|
| `ObjectFifo(type, depth, name)` | ObjectFifo | Create FIFO |
| `.prod(depth=None)` | Handle | Get producer (singleton) |
| `.cons(depth=None, dims_from_stream=None)` | Handle | Get consumer (new each call) |

### ObjectFifoHandle

| Method | Returns | Description |
|--------|---------|-------------|
| `.acquire(N)` | list | Acquire N buffers |
| `.release(N)` | None | Release N buffers |
| `.forward(placement, ...)` | ObjectFifo | Pass-through copy (consumer only) |
| `.split(offsets, ...)` | list[ObjectFifo] | Fan-out distribution (consumer only) |
| `.join(offsets, ...)` | list[ObjectFifo] | Fan-in merge (producer only) |

### Runtime

| Method | Description |
|--------|-------------|
| `rt.fill(prod, buf, tap=None, task_group=None)` | DDR → FIFO |
| `rt.drain(cons, buf, tap=None, wait=False, task_group=None)` | FIFO → DDR |
| `rt.start(*workers)` | Start compute workers |
| `rt.task_group()` | Create BD reuse group |
| `rt.finish_task_group(tg)` | Free BDs in group |

### TensorAccessPattern

```python
TensorAccessPattern(
    tensor_dims=(1, total),
    offset=0,
    sizes=[d3, d2, d1, d0],      # d3≤64, d0-d2≤1023, d0 even for bf16
    strides=[s3, s2, s1, s0],     # Element strides (~2^20 max)
)
```

## Appendix B: Placement Types

```python
from aie.iron import Tile, AnyMemTile, AnyShimTile, AnyComputeTile

Tile(col, row)       # Explicit tile at (col, row)
AnyMemTile           # Auto-select MemTile (row 1)
AnyShimTile          # Auto-select ShimTile (row 0)
AnyComputeTile       # Auto-select ComputeTile (rows 2+)
```
