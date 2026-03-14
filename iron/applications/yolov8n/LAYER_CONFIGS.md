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

## Compilation Flags

All designs require these aiecc flags (set in `iron/common/compilation.py`):
- `--no-unified`: Prevents multi-column linker symbol collision
- `--aie-generate-npu-insts`: Generates instruction binary (NOT `--aie-generate-npu`)
- `--aie-generate-xclbin`: Generates hardware binary

## Data Layout

All operators use tiled layout `[H, C/8, W, 8]` for activations:
- Input: NCHW → tiled in `op.py:nchw_to_tiled()`
- Output: tiled → NCHW in `op.py:tiled_to_nchw()`
- Weights k1: `[OC/8, IC/8, 8, 8]` via `weights_to_tiled()`
- Weights k3: `[OC/8, IC/8, 3, 3, 8, 8]` via `weights_to_tiled_3x3()`
- Fused SiLU: bias `[OC]` appended after tiled weights per column
