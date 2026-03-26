# YOLOv8n BF16 → INT8 Conversion Plan

## Context

YOLOv8n runs on AMD Ryzen AI NPU with bfloat16 and produces correct detections (4 persons + 1 bus on bus.jpg, matching ultralytics reference). The goal: convert to int8 for faster inference. Int8 uses 8×8×8 MMUL (vs 4×8×8 for bf16), halves memory bandwidth, and YOLOv8n is designed to be quantization-tolerant.

**Existing int8 infrastructure**:
- `mlir-aie/aie_kernels/aie2p/conv2dk1_i8.cc` — 1×1 int8 conv kernel (production-ready)
- `mlir-aie/programming_examples/ml/conv2d/` — working int8 conv2d example with test
- Same `[H, C/8, W, 8]` tiling layout as bf16
- Per-tensor symmetric quantization: int8×int8→int32→right-shift→int8
- **No 3×3 int8 kernel exists** — must be created
- **No bias or activation** in int8 kernel — applied in Python between layers

**Quantization scheme**: Right-shift by `scale` bits (power-of-2), saturate to [-128, 127].

## Phases

### Phase 1: Int8 Conv2d 1×1 Operator

**Goal**: Create `AIEConv2dInt8` operator for 1×1 convolutions with int8 weights and activations.

**Files to create/modify**:
- `aie_kernels/aie2p/conv2dk1_i8.cc` — copy from `mlir-aie/aie_kernels/aie2p/conv2dk1_i8.cc`
- `aie_kernels/aie2p/conv2dk1_i8.h` — copy header
- `iron/operators/conv2d_int8/__init__.py`
- `iron/operators/conv2d_int8/op.py` — `AIEConv2dInt8(AIEOperatorBase)` with int8 dtype
- `iron/operators/conv2d_int8/design.py` — MLIR design with int8 element types
- `iron/operators/conv2d_int8/reference.py` — CPU int8 reference
- `iron/operators/conv2d_int8/test.py` — hardware verification tests

**Key differences from bf16**:
- Element size: 1 byte (int8) vs 2 bytes (bf16)
- Scale parameter: 7th kernel arg (right-shift bits)
- No bias, no activation
- Width must be multiple of 32 for vectorized kernel

### Phase 2: Int8 Conv2d 3×3 Kernel

**Goal**: Create `conv2dk3_i8.cc` for 3×3 convolutions with int8.

**Files**:
- `aie_kernels/aie2p/conv2dk3_i8.cc` — new kernel (scalar + vectorized)
  - Stride-1 and stride-2 variants
  - Border handling: check=0/1/2 (top/middle/bottom)
  - Weight layout: `[OC/8, IC/8, 3, 3, 8, 8]`
  - Accumulation: int32 MAC → right-shift → saturate to int8

### Phase 3: Quantization Utilities (parallel with 1+2)

**Goal**: Float32 → int8 weight conversion with optimal scale computation.

**Files**:
- `iron/applications/yolov8n/quantize.py`:
  - `quantize_weight_per_tensor(float_weight) → (int8_weight, scale_shift)`
  - `quantize_activation(float_tensor, act_scale) → int8_tensor`
  - `dequantize_output(int8_tensor, out_scale) → float_tensor`
  - `compute_scale(weight, activation_range) → shift_bits`

**Scheme**: Per-tensor symmetric. `w_int8 = round(w_float / w_scale)`, `y_int8 = (y_int32 >> combined_shift)`

### Phase 4: Int8 YOLOv8n Blocks

**Goal**: Int8 versions of CBS, C2f, SPPF, DetectBranch.

**Inter-layer data flow**:
```
int8_input → NPU conv (int8×int8→int8) → dequant to float → SiLU → requant to int8 → next layer
```

**Files**: `iron/applications/yolov8n/blocks_int8.py`

### Phase 5: Full Model Int8 Inference

**Goal**: Run YOLOv8n with int8 weights on bus.jpg. Same objects as bf16.

**Files**: `iron/applications/yolov8n/run_pretrained_int8.py`

## Team Assignment

| Agent | Phase | Focus | Parallel? |
|-------|-------|-------|-----------|
| Agent 1 | 1 | Int8 1×1 conv operator | Yes |
| Agent 2 | 2 | Int8 3×3 conv kernel | Yes |
| Agent 3 | 3 | Quantization utilities | Yes |
| Lead | 4+5 | Int8 blocks + integration | After 1-3 |

## Key Constraints

- **Width multiple of 32** for vectorized int8 kernel. YOLOv8n P5 (20×20) and P4 (40×40) are NOT multiples of 32 — need scalar fallback or padding
- **No bias/SiLU in int8 kernel** — applied in float between layers
- **Scale per-tensor** — right-shift by N bits ≈ divide by 2^N
- **MaxPool/Upsample**: Keep as bf16 (simple data movement)

## Definition of Done

- [ ] Conv2d int8 1×1 passes HW verification at YOLOv8n sizes
- [ ] Conv2d int8 3×3 passes HW verification at YOLOv8n sizes
- [ ] Full YOLOv8n with int8 weights detects objects on bus.jpg
- [ ] Performance comparison: int8 vs bf16 inference time
