<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# YOLOv8n Layer Configuration Reference

Every layer in the YOLOv8n model with its operator config, column count,
memory strategy, and NPU verification status. This is the definitive
reference for running the full model on AMD Ryzen AI NPU2.

Input: `[1, 3, 640, 640]` bfloat16 (padded to 8ch internally).

## Backbone (L0–L9)

| Layer | Block | Op Type | IC | OC | H×W | K | S | Cols | MemTile | Weight Stream | IC Stream | HW Status |
|-------|-------|---------|----|----|-----|---|---|------|---------|---------------|-----------|-----------|
| L0 | CBS | conv2d k3s2 | 8 | 16 | 640×640→320×320 | 3 | 2 | 1 | No | No | No | **PASS** |
| L1 | CBS | conv2d k3s2 | 16 | 32 | 320×320→160×160 | 3 | 2 | 2 | No | No | No | **PASS** |
| L2 cv1 | C2f | conv2d k1 | 32 | 32 | 160×160 | 1 | 1 | 1 | No | No | No | **PASS** |
| L2 bn0 cv1 | C2f | conv2d k3s1 | 16 | 16 | 160×160 | 3 | 1 | 1 | No | No | No | **PASS** |
| L2 bn0 cv2 | C2f | conv2d k3s1 | 16 | 16 | 160×160 | 3 | 1 | 1 | No | No | No | **PASS** |
| L2 cv2 | C2f | conv2d k1 | 48 | 32 | 160×160 | 1 | 1 | 1 | No | No | No | **PASS** |
| L3 | CBS | conv2d k3s2 | 32 | 64 | 160×160→80×80 | 3 | 2 | 4 | No | No | No | **PASS** |
| L4 cv1 | C2f | conv2d k1 | 64 | 64 | 80×80 | 1 | 1 | 1 | No | No | No | **PASS** |
| L4 bn0 cv1 | C2f | conv2d k3s1 | 32 | 32 | 80×80 | 3 | 1 | 1 | No | No | No | **PASS** |
| L4 bn0 cv2 | C2f | conv2d k3s1 | 32 | 32 | 80×80 | 3 | 1 | 1 | No | No | No | **PASS** |
| L4 bn1 cv1 | C2f | conv2d k3s1 | 32 | 32 | 80×80 | 3 | 1 | 1 | No | No | No | **PASS** |
| L4 bn1 cv2 | C2f | conv2d k3s1 | 32 | 32 | 80×80 | 3 | 1 | 1 | No | No | No | **PASS** |
| L4 cv2 | C2f | conv2d k1 | 128 | 64 | 80×80 | 1 | 1 | 1 | No | No | No | **PASS** |
| L5 | CBS | conv2d k3s2 | 64 | 128 | 80×80→40×40 | 3 | 2 | 8 | No | No | No | **PASS** |
| L6 cv1 | C2f | conv2d k1 | 128 | 128 | 40×40 | 1 | 1 | 2 | No | No | No | **PASS** |
| L6 bn0 cv1 | C2f | conv2d k3s1 | 64 | 64 | 40×40 | 3 | 1 | 2 | No | No | No | **PASS** |
| L6 bn0 cv2 | C2f | conv2d k3s1 | 64 | 64 | 40×40 | 3 | 1 | 2 | No | No | No | **PASS** |
| L6 bn1 cv1 | C2f | conv2d k3s1 | 64 | 64 | 40×40 | 3 | 1 | 2 | No | No | No | **PASS** |
| L6 bn1 cv2 | C2f | conv2d k3s1 | 64 | 64 | 40×40 | 3 | 1 | 2 | No | No | No | **PASS** |
| L6 cv2 | C2f | conv2d k1 | 256 | 128 | 40×40 | 1 | 1 | 4 | Yes | No | No | **PASS** |
| L7 | CBS | conv2d k3s2 | 128 | 256 | 40×40→20×20 | 3 | 2 | 8 | No | Yes (oc=8) | No | **PASS** |
| L8 cv1 | C2f | conv2d k1 | 256 | 256 | 20×20 | 1 | 1 | 1 | No | No | No | **PASS** |
| L8 bn0 cv1 | C2f | conv2d k3s1 | 128 | 128 | 20×20 | 3 | 1 | 8 | No | Yes (oc=8) | No | **PASS** |
| L8 bn0 cv2 | C2f | conv2d k3s1 | 128 | 128 | 20×20 | 3 | 1 | 8 | No | Yes (oc=8) | No | **PASS** |
| L8 cv2 | C2f | conv2d k1 | 384 | 256 | 20×20 | 1 | 1 | 8 | Yes | No | No | **PASS** |
| L9 cv1 | SPPF | conv2d k1 | 256 | 128 | 20×20 | 1 | 1 | 2 | No | No | No | **PASS** |
| L9 mp1 | SPPF | maxpool2d k5 | 128 | — | 20×20 | 5 | 1 | 1 | No | — | — | **PASS** |
| L9 mp2 | SPPF | maxpool2d k5 | 128 | — | 20×20 | 5 | 1 | 1 | No | — | — | **PASS** |
| L9 mp3 | SPPF | maxpool2d k5 | 128 | — | 20×20 | 5 | 1 | 1 | No | — | — | **PASS** |
| L9 cv2 | SPPF | conv2d k1 | 512 | 256 | 20×20 | 1 | 1 | 8 | Yes | No | No | **PASS** |

**Backbone total: 30 NPU operators, ALL PASS at 640×640**

## Neck (L10–L21)

| Layer | Block | Op Type | IC | OC | H×W | K | S | Cols | MemTile | Weight Stream | IC Stream | HW Status |
|-------|-------|---------|----|----|-----|---|---|------|---------|---------------|-----------|-----------|
| L10 | — | upsample 2× | 256 | — | 20×20→40×40 | — | — | 1 | No | — | — | **PASS** |
| L11 | — | concat (CPU) | 256+128 | 384 | 40×40 | — | — | — | — | — | — | host |
| L12 cv1 | C2f | conv2d k1 | 384 | 128 | 40×40 | 1 | 1 | 4 | Yes | No | No | **PASS** |
| L12 bn0 cv1 | C2f | conv2d k3s1 | 64 | 64 | 40×40 | 3 | 1 | 2 | No | No | No | **PASS** |
| L12 bn0 cv2 | C2f | conv2d k3s1 | 64 | 64 | 40×40 | 3 | 1 | 2 | No | No | No | **PASS** |
| L12 cv2 | C2f | conv2d k1 | 192 | 128 | 40×40 | 1 | 1 | 4 | Yes | No | No | **PASS** |
| L13 | — | upsample 2× | 128 | — | 40×40→80×80 | — | — | 1 | No | — | — | **PASS** |
| L14 | — | concat (CPU) | 128+64 | 192 | 80×80 | — | — | — | — | — | — | host |
| L15 cv1 | C2f | conv2d k1 | 192 | 64 | 80×80 | 1 | 1 | 2 | Yes | No | No | **PASS** |
| L15 bn0 cv1 | C2f | conv2d k3s1 | 32 | 32 | 80×80 | 3 | 1 | 1 | No | No | No | **PASS** |
| L15 bn0 cv2 | C2f | conv2d k3s1 | 32 | 32 | 80×80 | 3 | 1 | 1 | No | No | No | **PASS** |
| L15 cv2 | C2f | conv2d k1 | 96 | 64 | 80×80 | 1 | 1 | 1 | No | No | No | **PASS** |
| L16 | CBS | conv2d k3s2 | 64 | 64 | 80×80→40×40 | 3 | 2 | 4 | No | No | No | **PASS** |
| L17 | — | concat (CPU) | 64+128 | 192 | 40×40 | — | — | — | — | — | — | host |
| L18 cv1 | C2f | conv2d k1 | 192 | 128 | 40×40 | 1 | 1 | 4 | Yes | No | No | **PASS** |
| L18 bn0 cv1 | C2f | conv2d k3s1 | 64 | 64 | 40×40 | 3 | 1 | 2 | No | No | No | **PASS** |
| L18 bn0 cv2 | C2f | conv2d k3s1 | 64 | 64 | 40×40 | 3 | 1 | 2 | No | No | No | **PASS** |
| L18 cv2 | C2f | conv2d k1 | 192 | 128 | 40×40 | 1 | 1 | 4 | Yes | No | No | **PASS** |
| L19 | CBS | conv2d k3s2 | 128 | 128 | 40×40→20×20 | 3 | 2 | 4 | No | Yes (oc=8) | No | **PASS** |
| L20 | — | concat (CPU) | 128+256 | 384 | 20×20 | — | — | — | — | — | — | host |
| L21 cv1 | C2f | conv2d k1 | 384 | 256 | 20×20 | 1 | 1 | 8 | Yes | No | No | **PASS** |
| L21 bn0 cv1 | C2f | conv2d k3s1 | 128 | 128 | 20×20 | 3 | 1 | 8 | No | Yes (oc=8) | No | **PASS** |
| L21 bn0 cv2 | C2f | conv2d k3s1 | 128 | 128 | 20×20 | 3 | 1 | 8 | No | Yes (oc=8) | No | **PASS** |
| L21 cv2 | C2f | conv2d k1 | 768 | 256 | 20×20 | 1 | 1 | 4 | Yes | Yes (oc=16) | No | **PASS** |

**Neck total: 20 NPU operators + 4 host concats, ALL PASS at 640×640**

## Detect Head

### Regression Branches (4×reg_max=64 output channels)

| Layer | Scale | Op Type | IC | OC | H×W | K | S | Cols | MemTile | Weight Stream | IC Stream | HW Status |
|-------|-------|---------|----|----|-----|---|---|------|---------|---------------|-----------|-----------|
| reg_p3 cv1 | P3 | conv2d k3s1 | 64 | 64 | 80×80 | 3 | 1 | 2 | No | No | No | **PASS** |
| reg_p3 cv2 | P3 | conv2d k3s1 | 64 | 64 | 80×80 | 3 | 1 | 2 | No | No | No | **PASS** |
| reg_p3 cv3 | P3 | conv2d k1 | 64 | 64 | 80×80 | 1 | 1 | 1 | No | No | No | **PASS** |
| reg_p4 cv1 | P4 | conv2d k3s1 | 128 | 64 | 40×40 | 3 | 1 | 8 | No | Yes (oc=8) | No | **PASS** |
| reg_p4 cv2 | P4 | conv2d k3s1 | 64 | 64 | 40×40 | 3 | 1 | 2 | No | No | No | **PASS** |
| reg_p4 cv3 | P4 | conv2d k1 | 64 | 64 | 40×40 | 1 | 1 | 1 | No | No | No | **PASS** |
| reg_p5 cv1 | P5 | conv2d k3s1 | 256 | 64 | 20×20 | 3 | 1 | ? | ? | ? | **YES** | **NEEDS IC** |
| reg_p5 cv2 | P5 | conv2d k3s1 | 64 | 64 | 20×20 | 3 | 1 | 2 | No | No | No | **PASS** |
| reg_p5 cv3 | P5 | conv2d k1 | 64 | 64 | 20×20 | 1 | 1 | 1 | No | No | No | **PASS** |

### Classification Branches (80 COCO classes)

| Layer | Scale | Op Type | IC | OC | H×W | K | S | Cols | MemTile | Weight Stream | IC Stream | HW Status |
|-------|-------|---------|----|----|-----|---|---|------|---------|---------------|-----------|-----------|
| cls_p3 cv1 | P3 | conv2d k3s1 | 64 | 80 | 80×80 | 3 | 1 | 2 | No | Yes (oc=8) | No | **PASS** |
| cls_p3 cv2 | P3 | conv2d k3s1 | 80 | 80 | 80×80 | 3 | 1 | ? | ? | ? | **YES** | **NEEDS IC** |
| cls_p3 cv3 | P3 | conv2d k1 | 80 | 80 | 80×80 | 1 | 1 | 1 | No | No | No | **PASS** |
| cls_p4 cv1 | P4 | conv2d k3s1 | 128 | 80 | 40×40 | 3 | 1 | 2 | No | Yes (oc=8) | No | **PASS** |
| cls_p4 cv2 | P4 | conv2d k3s1 | 80 | 80 | 40×40 | 3 | 1 | 1 | No | Yes (oc=16) | No | **PASS** |
| cls_p4 cv3 | P4 | conv2d k1 | 80 | 80 | 40×40 | 1 | 1 | 1 | No | No | No | **PASS** |
| cls_p5 cv1 | P5 | conv2d k3s1 | 256 | 80 | 20×20 | 3 | 1 | ? | ? | ? | **YES** | **NEEDS IC** |
| cls_p5 cv2 | P5 | conv2d k3s1 | 80 | 80 | 20×20 | 3 | 1 | 1 | No | Yes (oc=16) | No | **PASS** |
| cls_p5 cv3 | P5 | conv2d k1 | 80 | 80 | 20×20 | 1 | 1 | 1 | No | No | No | **PASS** |

**Detect total: 15/18 on NPU, 3 need IC streaming**

## Summary

| Section | NPU Operators | Host Ops | NPU PASS | Needs IC Streaming |
|---------|--------------|----------|----------|--------------------|
| Backbone (L0-L9) | 30 | 0 | **30/30** | 0 |
| Neck (L10-L21) | 20 | 4 concat | **20/20** | 0 |
| Detect Reg | 9 | 0 | **8/9** | 1 (reg_p5 cv1) |
| Detect Cls | 9 | 0 | **7/9** | 2 (cls_p3 cv2, cls_p5 cv1) |
| **Total** | **68** | **4** | **65/68** | **3** |

## Memory Strategy Legend

- **Cols**: Number of AIE columns (`_auto_columns` selects based on L1 budget)
- **MemTile**: Input FIFO routed through MemTile via `forward(placement=AnyMemTile)` — reduces L1 input depth from 2 to 1
- **Weight Stream**: Weights split into OC-subgroups, streamed from MemTile — `oc_chunk` elements per acquire
- **IC Stream**: Input channels split into groups, partial sums accumulated across groups — **NOT YET IMPLEMENTED**

## L1 Memory Budget Formula

For k3×3 stride-1:
```
L1 = stack(1040) + input_fifo(4 × IC × W × 2) + weight(OC_chunk × IC × 9 × 2) + output_fifo(2 × OC_chunk × W × 2)
```

For k1×1:
```
L1 = stack(1040) + input_fifo(depth × IC × W × 2) + weight(OC_per_col × IC × 2) + output_fifo(2 × OC_per_col × W × 2)
```
Where `depth=2` normally, `depth=1` with MemTile input routing.

Must fit in **65,536 bytes** (64KB compute tile L1).

## 3 Infeasible Configs — IC Streaming Required

These configs have large IC × k3×3 depth-4 input FIFOs that consume >40KB:

| Config | IC | W | Input FIFO (4×IC×W×2) | L1 Remaining | Min Weight Chunk | Fits? |
|--------|----|----|----------------------|--------------|------------------|-------|
| reg_p5 cv1 (256→64) | 256 | 20 | 40,960 | 23,536 | 36,864 (8×256×9×2) | **NO** |
| cls_p3 cv2 (80→80) | 80 | 80 | 51,200 | 13,296 | 11,520 (8×80×9×2) | **NO** (+ output 2,560) |
| cls_p5 cv1 (256→80) | 256 | 20 | 40,960 | 23,536 | 36,864 (8×256×9×2) | **NO** |

**Fix**: IC streaming — split IC into groups (e.g., ic_chunk=32), process each group's input rows with partial accumulation. Requires accumulating kernel variant.

With ic_chunk=32 for reg_p5 cv1:
```
input_fifo = 4 × 32 × 20 × 2 = 5,120
weight = 8 × 32 × 9 × 2 = 4,608
output = 2 × 8 × 20 × 2 = 640
Total = 12,408 ✓✓✓
```

## Multi-PDI Configuration (29 PDIs for L0-L21)

Each unique `(op_type, IC, OC, H, W, K, S, cols)` gets one PDI. Layers sharing
the same config share a PDI (same xclbin partition) but use separate instruction
streams and buffers.

| PDI | Kernel ID | Config | Layers Using This PDI |
|-----|-----------|--------|----------------------|
| 0 | 0x901 | conv2d 8→16 k3s2 640×640 1col | L0 |
| 1 | 0x902 | conv2d 16→32 k3s2 320×320 2col | L1 |
| 2 | 0x903 | conv2d 32→32 k1 160×160 1col | L2 cv1 |
| 3 | 0x904 | conv2d 16→16 k3s1 160×160 1col | L2 bn0 cv1, L2 bn0 cv2 |
| 4 | 0x905 | conv2d 48→32 k1 160×160 1col | L2 cv2 |
| 5 | 0x906 | conv2d 32→64 k3s2 160×160 4col | L3 |
| 6 | 0x907 | conv2d 64→64 k1 80×80 1col | L4 cv1, reg_p3 cv3 |
| 7 | 0x908 | conv2d 32→32 k3s1 80×80 1col | L4 bn0/bn1 cv1/cv2, L15 bn0 cv1/cv2 |
| 8 | 0x909 | conv2d 128→64 k1 80×80 2col | L4 cv2 |
| 9 | 0x90A | conv2d 64→128 k3s2 80×80 8col | L5 |
| 10 | 0x90B | conv2d 128→128 k1 40×40 2col | L6 cv1 |
| 11 | 0x90C | conv2d 64→64 k3s1 40×40 2col | L6 bn0/bn1, L12 bn0, L18 bn0 |
| 12 | 0x90D | conv2d 256→128 k1 40×40 4col (MemTile) | L6 cv2 |
| 13 | 0x90E | conv2d 128→256 k3s2 40×40 8col (wt stream) | L7 |
| 14 | 0x90F | conv2d 256→256 k1 20×20 4col | L8 cv1 |
| 15 | 0x910 | conv2d 128→128 k3s1 20×20 8col (wt stream) | L8 bn0, L21 bn0 |
| 16 | 0x911 | conv2d 384→256 k1 20×20 8col (MemTile) | L8 cv2 |
| 17 | 0x912 | conv2d 256→128 k1 20×20 2col | L9 cv1 |
| 18 | 0x913 | maxpool2d 128ch k5 20×20 1col | L9 mp1/mp2/mp3 |
| 19 | 0x914 | conv2d 512→256 k1 20×20 8col (MemTile) | L9 cv2 |
| 20 | 0x915 | upsample 256ch 20×20 1col | L10 (up1) |
| 21 | 0x916 | conv2d 384→128 k1 40×40 4col (MemTile) | L12 cv1 |
| 22 | 0x917 | conv2d 192→128 k1 40×40 4col (MemTile) | L12 cv2, L18 cv1, L18 cv2 |
| 23 | 0x918 | upsample 128ch 40×40 1col | L13 (up2) |
| 24 | 0x919 | conv2d 192→64 k1 80×80 2col (MemTile) | L15 cv1 |
| 25 | 0x91A | conv2d 96→64 k1 80×80 1col | L15 cv2 |
| 26 | 0x91B | conv2d 64→64 k3s2 80×80 4col | L16 |
| 27 | 0x91C | conv2d 128→128 k3s2 40×40 4col (wt stream) | L19 |
| 28 | 0x91D | conv2d 768→256 k1 20×20 4col (MemTile+wt stream) | L21 cv2 |

**Detect head PDIs** (additional, to be added after IC streaming):

| PDI | Config | Layers | Status |
|-----|--------|--------|--------|
| 29 | conv2d 64→64 k3s1 80×80 2col | reg_p3 cv1/cv2 | Ready |
| 30 | conv2d 128→64 k3s1 40×40 8col (wt stream) | reg_p4 cv1 | Ready |
| 31 | conv2d 64→64 k3s1 40×40 2col | reg_p4 cv2 | Ready (shared w/ PDI 11) |
| 32 | conv2d 256→64 k3s1 20×20 (IC stream) | reg_p5 cv1 | **NEEDS IC STREAMING** |
| 33 | conv2d 64→64 k3s1 20×20 2col | reg_p5 cv2 | Ready |
| 34 | conv2d 64→64 k1 40×40 1col | reg_p4 cv3 | Ready |
| 35 | conv2d 64→64 k1 20×20 1col | reg_p5 cv3 | Ready |
| 36 | conv2d 64→80 k3s1 80×80 2col (wt stream) | cls_p3 cv1 | Ready |
| 37 | conv2d 80→80 k3s1 80×80 (IC stream) | cls_p3 cv2 | **NEEDS IC STREAMING** |
| 38 | conv2d 80→80 k1 80×80 1col | cls_p3 cv3 | Ready |
| 39 | conv2d 128→80 k3s1 40×40 2col (wt stream) | cls_p4 cv1 | Ready |
| 40 | conv2d 80→80 k3s1 40×40 1col (wt stream) | cls_p4 cv2 | Ready |
| 41 | conv2d 80→80 k1 40×40 1col | cls_p4 cv3 | Ready |
| 42 | conv2d 256→80 k3s1 20×20 (IC stream) | cls_p5 cv1 | **NEEDS IC STREAMING** |
| 43 | conv2d 80→80 k3s1 20×20 1col (wt stream) | cls_p5 cv2 | Ready |
| 44 | conv2d 80→80 k1 20×20 1col | cls_p5 cv3 | Ready |

**Total**: 29 backbone+neck PDIs (verified) + ~15 detect PDIs = ~44 unique PDIs.
Some detect PDIs are shared with existing backbone/neck PDIs (e.g., 64→64 k3s1 40×40).

## Bug Fixes Applied This Session

### 1. TAP 4D Decomposition (DMA BD Size Limits)
**File**: `iron/operators/conv2d/design.py`
**Problem**: Flat TAPs like `sizes=[1,1,1,total_size]` fail when `total_size > 1023`.
At YOLOv8n scale, input rows easily exceed 1023 (e.g., 64ch × 80w = 5120).
**Fix**: `_factorize_tensor()` decomposes any size into 4D `(d3, d2, d1, d0)` with:
- d3 ≤ 64 (hardware wrap count limit)
- d0, d1, d2 ≤ 1023
- d0 must be even (4-byte alignment for bf16)
**Impact**: Unblocks all YOLOv8n-scale TAPs. All input/weight/output TAPs now use decomposed dims.

### 2. Multi-Column Linker Fix (`--no-unified`)
**File**: `iron/common/compilation.py`
**Problem**: `aiecc --unified` (default) compiles all core functions into one object file.
When linking per-tile ELFs for 4+ column designs, the linker sees FIFO buffer symbol
references from other tiles' switch tables, causing `undefined symbol: in_N_cons_buff_*`.
**Fix**: Added `--no-unified` flag to aiecc. Forces per-core object file generation.
**Impact**: Unblocks L3 (4col), L5 (8col), L7 (8col), L16 (4col), L19 (4col), and
all future multi-column 3×3 conv designs.

### 3. BD Factorization Padding
**File**: `iron/operators/conv2d/design.py`, `iron/operators/conv2d/op.py`
**Problem**: Fused bias+SiLU packs bias at end of weights: `weights_per_col = OC×IC×9 + OC`.
For L8 bottleneck (128→128 k3s1 at 8col): `16×128×9 + 16 = 18448 = 16×1153`.
Since 1153 is prime > 1023, no valid BD factorization exists.
**Fix**: `_factorize_tensor_padded()` pads by up to 2 elements to find a factorizable
size (18448→18450 = 45×410). Weight buffer allocates the padded size.
**Impact**: Unblocks L8 bottleneck and L21 bottleneck with fused SiLU.

### 4. MemTile Input Buffering
**File**: `iron/operators/conv2d/design.py`
**Problem**: For 1×1 conv with large IC, input FIFO at depth=2 overflows L1.
E.g., 384→128 k1 40×40: input_fifo = 2×384×40×2 = 61KB > 64KB L1.
**Fix**: When `total_l1 > 65536` for k1 conv, route input through MemTile via
`ObjectFifo.cons().forward(placement=AnyMemTile, depth=1)`. MemTile holds the
double-buffer (512KB available); L1 only needs depth=1 (single buffer).
**Impact**: Unblocks L6 cv2, L9 cv2, L12 cv1, L15 cv1, L18 cv1/cv2, L21 cv1.

### 5. MemTile Weight Streaming
**File**: `iron/operators/conv2d/design.py`
**Problem**: For configs where full weight buffer exceeds L1 even after multi-column
split. E.g., L7 (128→256 k3s2) at 8col: weight = 32×128×9×2 = 72KB > 40KB budget.
**Fix**: Split weights into OC-subgroups (`oc_chunk`, typically 8). Store full weights
in MemTile, stream one OC-subgroup at a time via `forward(placement=AnyMemTile,
dims_to_stream=...)`. Core loops: for each OC group → for each row → kernel.
Output FIFO element is `oc_chunk × W` instead of `oc_per_col × W`.
**Impact**: Unblocks L7, L8 bn, L19, L21 bn, L21 cv2, reg_p4 cv1, cls_p3 cv1,
cls_p4 cv1, cls_p4 cv2, cls_p5 cv2.

### 6. `_auto_columns` Full L1 Budget Check
**File**: `iron/applications/yolov8n/blocks.py`
**Problem**: Original `_auto_columns()` only checked per-core weight size (≤40KB),
ignoring input/output FIFO buffers. For 1×1 conv, all FIFOs live on compute tile,
so total L1 = input + weight + output + stack must fit 64KB.
**Fix**: Updated to check full L1 budget:
- k1: `stack(1040) + input(2×IC×W×2) + weight(OC_col×IC×2) + output(2×OC_col×W×2)`
- k3: `stack(1040) + input(4×IC×W×2) + weight(OC_col×IC×9×2) + output(2×OC_col×W_out×2)`
- Second pass for k1: MemTile routing reduces input depth to 1
**Impact**: Correct column selection for all configs. Prevents silent L1 overflow.

### 7. Auto-Columns Default (0 instead of 1)
**Files**: `backbone.py`, `neck.py`, `detect.py`, `blocks.py` (SPPF)
**Problem**: Backbone/Neck/Detect constructors defaulted to `num_aie_columns=1`,
which overrode `_auto_columns()` and caused L1 overflow for large configs.
**Fix**: Changed default to `num_aie_columns=0` (auto-select based on L1 budget).
**Impact**: All blocks now automatically choose the optimal column count.

### 8. Fused Bias+SiLU Kernel
**Files**: `aie_kernels/aie2p/conv2dk1_bf16.cc`, `conv2dk3_bf16.cc`
**Problem**: CBS block applied bias and SiLU in Python after NPU conv, requiring
DDR round-trip per layer.
**Fix**: New kernel variants `conv2dk1_bf16_bias_silu` and `conv2dk3_bf16_bias_silu`
that apply bias+SiLU on-chip. Bias packed at end of weight buffer per column.
SiLU uses Padé rational tanh approximation (no `expf` on AIE):
`tanh(z) ≈ z(27+z²)/(27+9z²)`, then `SiLU(x) = x × 0.5 × (1 + tanh(x/2))`.
**Impact**: Eliminates DDR round-trip for every CBS block (~25 per model).

## Compilation Flags

All designs require these aiecc flags (set in `iron/common/compilation.py`):
- `--no-unified`: Prevents multi-column linker symbol collision (Bug Fix #2)
- `--aie-generate-npu-insts`: Generates instruction binary (NOT `--aie-generate-npu`)
- `--aie-generate-xclbin`: Generates hardware binary

## Data Layout

All operators use tiled layout `[H, C/8, W, 8]` for activations:
- Input: NCHW → tiled in `op.py:nchw_to_tiled()`
- Output: tiled → NCHW in `op.py:tiled_to_nchw()`
- Weights k1: `[OC/8, IC/8, 8, 8]` via `weights_to_tiled()`
- Weights k3: `[OC/8, IC/8, 3, 3, 8, 8]` via `weights_to_tiled_3x3()`
- Fused SiLU: bias `[OC]` appended after tiled weights per column (Bug Fix #8)
