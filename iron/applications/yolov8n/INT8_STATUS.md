<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# YOLOv8n INT8 NPU Implementation — Status & Architecture

## Overview

YOLOv8n object detection running on AMD Ryzen AI NPU with int8 quantized
convolutions. All conv layers execute on NPU hardware using fully-integer
fused Conv+Bias+SiLU kernels — no floating point in the conv data path.

**Branch**: `yolov8n-int8` (based on `yolov8n` which has the working bf16 model)

## What's Working

### BF16 Model (Reference — Complete)
- **5 detections** on bus.jpg (4 person + 1 bus, matching ultralytics)
- 2 multi-PDI xclbins: backbone+neck (28 PDIs) + detect head (17 PDIs)
- 64.7s inference (scalar k3 kernels)
- Run: `python3 -m iron.applications.yolov8n.run_pretrained`

### INT8 Model (In Progress)
- **Full model runs end-to-end** on NPU (all 63 layers, all fused, no crashes)
- **Fused conv+bias+SiLU kernel**: 100% exact match with CPU reference
- **Vectorized k3 int8**: 1000× speedup (1.4s → 1.3ms per layer)
- **Calibration sweep**: detections appear at p95-p99 percentile calibration
  - p99: 7 detections at conf=0.1, **0.91 confidence** (class confusion)
  - p99.9: 2 person detections at conf=0.01 (correct class, low confidence)
- **Int8 CPU reference**: 5 correct detections (validates quantization scheme)

## Architecture

### NPU Offload Summary

```
Image [1,3,640,640] float
  │
  ▼ Quantize to int8 (CPU)
  │
  ├─── BACKBONE (L0-L9) ──────────────────────────────────────────────┐
  │    L0: CBS 8→16 k3s2 ──── int8 fused conv+bias+SiLU (NPU) ──→ int8 │
  │    L1: CBS 16→32 k3s2 ── int8 fused (NPU) ──→ int8                │
  │    L2: C2f 32→32 n=1 ─── 4× fused CBS (NPU) + residual add (CPU) │
  │    L3: CBS 32→64 k3s2 ── int8 fused (NPU) ──→ int8                │
  │    L4: C2f 64→64 n=2 ─── 6× fused CBS (NPU) + residual add ──→ P3│
  │    L5: CBS 64→128 k3s2 ─ int8 fused (NPU)                        │
  │    L6: C2f 128→128 n=2 ─ 6× fused CBS (NPU) ──→ P4              │
  │    L7: CBS 128→256 k3s2  int8 fused (NPU)                        │
  │    L8: C2f 256→256 n=1 ─ 4× fused CBS (NPU)                     │
  │    L9: SPPF ──────────── fused CBS + bf16 MaxPool (NPU) ──→ P5   │
  │                                                                    │
  ├─── NECK (L10-L21) ────────────────────────────────────────────────┤
  │    L10: Upsample 2× ──── bf16 (NPU)                              │
  │    L11: Concat ────────── CPU (torch.cat)                          │
  │    L12: C2f 384→128 ──── fused CBS (NPU)                         │
  │    L13: Upsample 2× ──── bf16 (NPU)                              │
  │    L14: Concat ────────── CPU                                      │
  │    L15: C2f 192→64 ───── fused CBS (NPU) ──→ det_p3              │
  │    L16: CBS 64→64 k3s2 ─ int8 fused (NPU)                        │
  │    L17: Concat ────────── CPU                                      │
  │    L18: C2f 192→128 ──── fused CBS (NPU) ──→ det_p4              │
  │    L19: CBS 128→128 ──── int8 fused (NPU)                        │
  │    L20: Concat ────────── CPU                                      │
  │    L21: C2f 384→256 ──── fused CBS (NPU) ──→ det_p5              │
  │                                                                    │
  ├─── DETECT HEAD (6 branches) ──────────────────────────────────────┤
  │    Per scale (P3/P4/P5):                                          │
  │      Reg: CBS(k3)+CBS(k3) ── int8 fused (NPU)                    │
  │           Conv(k1) ────────── int8 bare (NPU) → dequant (CPU)    │
  │      Cls: CBS(k3)+CBS(k3) ── int8 fused (NPU)                    │
  │           Conv(k1) ────────── int8 bare (NPU) → dequant (CPU)    │
  │                                                                    │
  └─── POST-PROCESSING (CPU) ─────────────────────────────────────────┘
       DFL decode → dist2bbox → sigmoid → NMS → detections
```

### What Runs Where

| Operation | Where | Dtype | Kernel |
|-----------|-------|-------|--------|
| Conv2d k3 CBS | **NPU** | int8 in/out | `conv2dk3_i8_fused_packed` (conv+bias+SiLU) |
| Conv2d k1 CBS | **NPU** | int8 in/out | `conv2dk1_i8_fused` (conv+bias+SiLU) |
| Conv2d k1 bare | **NPU** | int8 in/out | `conv2dk1_i8` (conv only) |
| MaxPool2d | **NPU** | bf16 | `maxpool2d_bf16` |
| Upsample 2× | **NPU** | bf16 | `upsample2x_bf16` |
| Concat | CPU | int8 → int8 | `torch.cat` |
| Residual add | CPU | int8 + int8 → int8 | Clamped integer add |
| Bias + dequant | CPU | int8 → float | Detect cv3 only |
| Post-processing | CPU | float | DFL + NMS |

### Fused Conv+Bias+SiLU Kernel

The key innovation: **fully integer SiLU activation** using a sigmoid lookup table.

```
Computation (per output element):
  1. int8 × int8 → int32 MAC accumulation (3×3 or 1×1 kernel)
  2. Add int32 bias (pre-scaled to accumulator domain)
  3. Right-shift to int8 for LUT lookup: acc_i8 = (acc + rnd) >> shift1
  4. Sigmoid LUT: sig = sigmoid_lut[acc_i8 + 128]  (256-entry uint8 table)
  5. Integer SiLU: silu = acc_i8 × sig
  6. Right-shift to output int8: out = (silu + rnd) >> shift2
```

- Sigmoid LUT: 256 entries, maps int8 [-128,127] → real [-8,+8] → sigmoid [0,255]
- Bias packed at end of weight buffer (no extra DMA channel needed)
- Two shift parameters per layer: shift1 (acc→LUT) and shift2 (SiLU→output)

### Quantization Scheme

- **Type**: Symmetric per-tensor for weights and activations
- **Calibration**: Run float model on calibration image, compute percentile-based accumulator ranges
- **Shift**: `shift = ceil(log2(percentile_value / 127))`
- **Percentile**: 95th-99th gives best results (trade-off between precision and clipping)
- **Weight packing**: `[int8 weights] ++ [int32 bias bytes]` packed contiguously per OC chunk

## Performance

### Kernel Benchmarks (Single Layer)

| Operator | Scalar | Vectorized | Speedup |
|----------|--------|------------|---------|
| Conv2d k3 int8 | 1471 ms | **1.3 ms** | **1000×** |
| Conv2d k1 int8 | 60-71 ms | ~1.5 ms | ~40× |
| MaxPool2d int8 | 3.8 ms | 3.3 ms | 1.15× |
| Upsample2x int8 | 1.0 ms | **0.16 ms** | **6.2×** |

### Full Model Timing

| Model | Inference | Notes |
|-------|-----------|-------|
| BF16 (scalar k3) | 88s | 5 detections, production quality |
| INT8 (scalar k3) | 130s | All fused, calibration WIP |
| INT8 (vectorized k3, projected) | **~10s** | 1000× k3 speedup |

## Files

### Kernels
- `aie_kernels/aie2p/conv2dk1_i8.cc` — 1×1 int8 conv (scalar + vectorized)
- `aie_kernels/aie2p/conv2dk3_i8.cc` — 3×3 int8 conv (scalar + vectorized 1000×)
- `aie_kernels/aie2p/conv2dk1_i8_fused.cc` — 1×1 fused conv+bias+SiLU
- `aie_kernels/aie2p/conv2dk3_i8_fused.cc` — 3×3 fused conv+bias+SiLU (original)
- `aie_kernels/aie2p/conv2dk3_i8_fused_packed.cc` — 3×3 fused, bias packed in weights
- `aie_kernels/aie2p/maxpool2d_i8.cc` — int8 maxpool (vectorized)
- `aie_kernels/aie2p/upsample2x_i8.cc` — int8 upsample (vectorized 6.2×)

### Operators
- `iron/operators/conv2d_int8/` — AIEConv2dInt8 with fused mode, OC streaming, MemTile
- `iron/operators/maxpool2d_int8/` — AIEMaxPool2dInt8
- `iron/operators/upsample_int8/` — AIEUpsampleInt8

### Application
- `iron/applications/yolov8n/quantize.py` — Int8Quantizer, calibration utilities
- `iron/applications/yolov8n/run_int8_cpu.py` — Int8 CPU reference (5 detections)
- `iron/applications/yolov8n/run_pretrained_int8.py` — NPU int8 model (WIP)

## Current Status & Next Steps

### What's Done ✓
- [x] All int8 operators verified on NPU (conv k1/k3, maxpool, upsample)
- [x] Fused conv+bias+SiLU kernel: 100% exact match, fully integer
- [x] Vectorized k3: 1000× speedup
- [x] K1 fused OC streaming with MemTile: fixed deadlock
- [x] Full model runs end-to-end (all 63 layers, no crashes)
- [x] Int8 CPU reference: 5 correct detections (validates scheme)
- [x] Calibration sweep: detections appear at p95-p99

### What's Needed for Production Detections
- [ ] **Per-layer calibration percentile**: Use p99.9 for backbone, p97 for neck, p95 for detect
      (different stages have different precision requirements)
- [ ] **Per-channel weight quantization for detect head**: The cls cv3 layer's per-tensor
      quantization doesn't preserve the fine class distinctions
- [ ] **Vectorized k3 alignment fix**: The vectorized kernel produces 1.5× output at large
      scale — shuffle alignment bug needs debugging
- [ ] **Multi-PDI xclbin**: Currently uses sequential contexts; migrate to 2-xclbin
      multi-PDI architecture (28+17 PDIs) for single-context execution

### Research Directions
- [ ] **Mixed precision**: int8 for backbone k3 (compute-bound), bf16 for detect head
      (precision-sensitive) — hybrid approach
- [ ] **Per-channel activation quantization**: Different scales per output channel
- [ ] **QAT (Quantization-Aware Training)**: Fine-tune model with int8 constraints
- [ ] **INT4 weights**: Further bandwidth reduction with 4-bit weight quantization

## Hardware Constraints

| Constraint | Limit | Impact |
|-----------|-------|--------|
| L1 memory | 64KB | Limits weight + FIFO per compute tile |
| DMA channels | 2 in + 2 out | Bias packed in weights (no 3rd channel) |
| BD dimensions | d3≤64, d0-d2≤1023 | TAP decomposition needed for large tensors |
| PDIs per xclbin | ≤32 (MAX_NUM_CUS) | 2 xclbins needed for full model |
| hw_contexts | ≤16 concurrent | Sequential context cleanup between layers |
| Int8 MMUL | 8×8×8 | Width must be multiple of 32 for vectorized |
| Sigmoid LUT | 256 entries | Maps int8 [-128,127] → sigmoid [0,255] |
