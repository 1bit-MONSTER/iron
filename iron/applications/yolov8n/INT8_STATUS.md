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
- **5 correct detections** on bus.jpg: 4 person + 1 bus (matches bf16!)
- **Confidence HIGHER than bf16**: 0.885 vs 0.844
- **Fused conv+bias+SiLU kernel**: 100% exact match, fully integer, no float
- **Vectorized k3 int8**: 1000-5000× speedup (1.4ms per bottleneck layer)
- **p100 calibration**: no clipping (backbone too sensitive to percentile clipping)
- **Forward: 29.4s** (dominated by scalar k1 + stride-2)
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

### Per-Layer Timing: BF16 vs INT8 (Scalar)

| Config | BF16 (ms) | INT8 scalar (ms) | INT8 vec (ms) |
|--------|-----------|-------------------|---------------|
| 8→16 k3s2 640×640 (L0) | 4,875 | 2,980 | ~5 (projected) |
| 16→32 k3s2 320×320 (L1) | 2,211 | 2,956 | ~3 |
| 32→32 k3s1 80×80 (bn) | 2,081 | 1,461 | ~1.3 |
| 64→64 k1 80×80 (cv1) | 2.6 | 64 | ~1.5 |
| 128→128 k3s1 40×40 (bn) | 1,976 | 5,775 | ~1.3 |

**Key finding**: Scalar int8 is NOT faster than bf16 (bf16 uses vectorized mmul).
The vectorized int8 k3 kernel (1000× speedup) is critical for int8 to beat bf16.

### Full Model Timing (Final)

| Model | Forward | Detections | Notes |
|-------|---------|-----------|-------|
| BF16 (scalar k3) | 88s | 5 | Production bf16 baseline |
| INT8 (scalar k3) | 130s | 5 | All fused, p100 calibration |
| INT8 (all vectorized, LUT SiLU) | 10.4s | 4 | LUT accuracy loss at P5 |
| **INT8 (all vectorized, Padé tanh)** | **14.7s** | **5** | **6× faster than bf16, all correct** |

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

## Current Status

### What's Done ✓
- [x] 5/5 correct detections on bus.jpg (person+bus, 0.85-0.90 confidence)
- [x] 14.7s forward (6× faster than bf16)
- [x] All int8 operators vectorized (k1 175×, k3s1 1000×, k3s2 635×)
- [x] Fused conv+bias+SiLU with Padé tanh (no LUT, continuous function)
- [x] All 63 layers run on NPU with correct results
- [x] p100 calibration (no percentile clipping needed)
- [x] Multi-PDI pipeline classes (2 xclbins, 45+18 PDIs)

## Performance Optimization Opportunities

### Current Bottlenecks (14.7s forward)

The 14.7s is dominated by **XRT context overhead**, not compute:
- **~63 AIEContext create/compile/prepare/destroy cycles** at ~100-200ms each = ~10s overhead
- Actual NPU kernel compute: ~1-2s total (all vectorized)
- DMA transfer time: ~2-3s (640×640 int8 data movement)

### 1. Multi-PDI Xclbin (Eliminate Context Overhead) — **Biggest Win**

**Current**: 63 separate AIEContext instances, each creating/destroying a hw_context.
**Target**: 2 xclbins (backbone+neck: ≤32 PDIs, detect: ≤32 PDIs), 2 hw_contexts total.
**Savings**: ~10s → ~0.2s context overhead. **Projected: ~4-5s forward.**

Pipeline classes already exist (`pipeline_int8.py`), need hardware verification.

### 2. Multi-Column Designs (Use All Cores) — **Not Currently Used**

**Current**: All int8 operators use `num_aie_columns=1` (single core per layer).
**Available**: NPU2 has 4 compute columns × 5 rows = 20 compute tiles.
**Opportunity**: For large layers (L0 640×640), split output channels across 4 columns:
- Each column processes `OC/4` output channels in parallel
- 4× throughput per layer
- Requires multi-column ObjectFIFO design (proven in bf16 `_auto_columns`)

**Impact**: k3s2 L0 (6.2ms) → ~1.5ms with 4 columns. Similar for other large configs.

### 3. Layer Fusion (Core-to-Core Dataflow) — **Eliminates DDR Round-Trips**

**Current**: Each conv layer does: DDR → L1 → compute → L1 → DDR → next layer.
**Target**: Chain adjacent convs within a single MLIR design:
- Bottleneck: conv3x3(Core0) → ObjectFIFO → conv3x3(Core1) → DDR
- Keeps activations on-chip between the two 3×3 convs
- Eliminates 1 DDR read + 1 DDR write per bottleneck

**Impact**: ~50% fewer DDR transfers for bottleneck pairs. C2f blocks have 2-4 bottlenecks each.

### 4. Shared PDI with Multiple TXN Binaries — **Eliminate Reconfiguration**

**Current**: Each unique `(IC, OC, H, W, K, S)` config gets its own PDI with its own
instruction binary (.bin). Layers sharing the same spatial dimensions but different
weights require separate PDIs because weights are baked into the DMA configuration.

**Target**: Parameterize PDIs so the same hardware configuration can run with different
weights by swapping only the TXN (instruction) binary:
- One PDI per `(IC_group, OC_group, K, S)` template (ignoring spatial dims)
- Multiple TXN binaries per PDI for different `(H, W)` spatial configurations
- Weights loaded via runtime fill() — already the case, just need shared PDI

**Impact**: Reduce 63 PDIs → ~15 template PDIs. Faster xclbin loading, smaller binary.
Could fit entire model in 1 xclbin (15 < 32 MAX_NUM_CUS).

### 5. Vectorized k1 NUM_ACC=4 (Compiler Bug Workaround) — **2× k1 Speedup**

**Current**: k1 uses NUM_ACC=1 (VEC1) due to Peano LLVM codegen bug with NUM_ACC=4.
**Target**: Fix or work around the compiler bug to enable NUM_ACC=4.
**Impact**: k1 0.4ms → ~0.1ms per layer (4× MMUL throughput per cycle).

### 6. Static Weight Preloading — **Eliminate Per-Layer Weight DMA**

**Current**: Weights are written to XRT buffers and DMA'd to L1 on every forward() call.
**Target**: Pre-load weights into MemTile or L1 as static data during `prepare_runtime()`.
Subsequent forward() calls skip weight DMA entirely.
**Impact**: Saves ~1-2s of weight transfer time across 63 layers.

### 7. INT4 Weight Quantization — **Halve Weight Bandwidth**

**Current**: INT8 weights (1 byte per element).
**Target**: INT4 weights (0.5 bytes per element) with int8 activations.
- Halves weight DMA bandwidth
- Requires weight unpacking in kernel (int4 → int8 before MMUL)
- Accuracy impact: needs QAT or careful calibration

### Projected Performance with Optimizations

| Optimization | Savings | Projected |
|-------------|---------|-----------|
| Current (all vectorized) | — | 14.7s |
| + Multi-PDI (2 xclbins) | -10s | **~4.5s** |
| + Multi-column (4 cols) | -1.5s | **~3s** |
| + Layer fusion | -0.5s | **~2.5s** |
| + Static weights | -0.5s | **~2s** |
| + Shared PDI (1 xclbin) | -0.3s | **~1.7s** |

## Hardware Constraints

| Constraint | Limit | Impact |
|-----------|-------|--------|
| L1 memory | 64KB | Limits weight + FIFO per compute tile |
| DMA channels | 2 in + 2 out | Bias packed in weights (no 3rd channel) |
| BD dimensions | d3≤64, d0-d2≤1023 | TAP decomposition needed for large tensors |
| PDIs per xclbin | ≤32 (MAX_NUM_CUS) | 2 xclbins needed for full model |
| hw_contexts | ≤16 concurrent | Sequential context cleanup between layers |
| Compute columns | 4 | Multi-column for parallelism (not yet used for int8) |
| Int8 MMUL | 8×8×8 | Width % 8 == 0 for VEC1, % 32 for VEC4 |
| Padé tanh | Rational approx | tanh(z) ≈ z(27+z²)/(27+9z²), accurate to ±0.003 |
