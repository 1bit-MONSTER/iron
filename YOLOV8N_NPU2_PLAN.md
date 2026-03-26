# YOLOv8n on NPU2: Comprehensive Implementation Plan

## Progress Tracker

| Phase | Status | Tests | Notes |
|-------|--------|-------|-------|
| P0: Infrastructure | **DONE** | 12/12 CPU | Layout conversion, BN fusion, weight export |
| P1: Conv2d 1×1 | **DONE** | 50/50 HW | Refactored with `get_artifacts()`, all pass |
| P2: Conv2d 3×3 | **DONE** | (in P1) | Stride-1 and stride-2 pass (scalar kernel) |
| P3.1: MaxPool2d | **DONE** | 15/15 HW | Refactored with `get_artifacts()`, all pass |
| P3.2: Upsample 2× | **DONE** | 15/15 HW | Refactored with `get_artifacts()`, all pass |
| P3.3: Concat | **DONE** | N/A | Host-side `torch.cat()` — no NPU operator needed |
| P4: Composites | **DONE** | 5/5 HW | CBS now uses fused bias+SiLU kernel on-chip |
| P5.1: Neck (FPN+PAN) | **DONE** | 5/5 HW | FPN up, PAN down, auto-column for L1 fit |
| P5.2: Detect Head | **DONE** | 5/5 HW | Reg + Cls branches, bare Conv1×1 final layer |
| P5.3: Full pipeline | **COMPLETE** | Real detections | 5 objects detected on bus.jpg (4 person + 1 bus), matching ultralytics |
| P6.0: Multi-PDI XCLBIN | **DONE** | 5/5 HW | `YOLOv8nPipeline` chains ~52 PDIs, SwiGLU pattern |
| P6.1: SiLU/Bias Fusion | **DONE** | 5/5 HW | Bias packed in weights, Padé tanh approx, CBS verified |
| P6.2: Post-Processing | **DONE** | 110/110 CPU | DFL decode + dist2bbox + NMS, full unit tests |
| P6.3: Documentation | **DONE** | — | README.md (620 lines), all 7 sections |
| P6.4: Benchmarks | **DONE** | 18 configs | k1: 170-640μs, k3 scalar: 4.6-76ms, CBS fused: 4.7ms |
| P7: Dataflow Fusion | TODO | — | Core-to-core bottleneck, depends on P6.1 |

### What Changed (This Session)

**Phase A — `get_artifacts()` Refactoring**
- Added `get_artifacts(prefix=)` to `AIEConv2d`, `AIEMaxPool2d`, `AIEUpsample`
- Added `register=True` kwarg to `AIEOperatorBase.__init__()` and all 3 operator constructors
- All existing operator tests pass unchanged on hardware (80 tests total)

**Phase B — Multi-PDI Pipeline Operator**
- Created `iron/applications/yolov8n/pipeline.py` (~600 lines)
- `YOLOv8nPipeline(AIEOperatorBase)` deduplicates ~52 unique operator configs
- Chains PDIs via `--xclbin-input` + `--xclbin-kernel-id` (SwiGLU pattern)
- Runs kernels individually via `_run_single_kernel()` (not monolithic runlist)
- Construction test passes at 256x256; 640x640 compile test in progress

**Phase C — Post-Processing**
- Created `iron/applications/yolov8n/postprocess.py`
- `YOLOv8nPostProcess`: anchor generation, DFL softmax decode, dist2bbox, sigmoid, NMS
- Manual NMS implementation (no torchvision dependency)
- 110 unit tests pass (anchors, DFL, dist2bbox, NMS, end-to-end)

**Phase E — SiLU/Bias Kernel Fusion**
- Added `conv2dk1_bf16_bias_silu` to `aie_kernels/aie2p/conv2dk1_bf16.cc`
- Added `conv2dk3_bf16_bias_silu` + stride-2 variant to `conv2dk3_bf16.cc`
- Bias packed at end of weight buffer (no extra DMA channel needed)
- SiLU via Padé tanh: `tanh(z) ≈ z(27+z²)/(27+9z²)` (no `expf` on AIE)
- Updated `design.py` to select fused kernel and enlarge weight FIFO
- Updated `op.py` to pack bias per-column into weight buffer
- CBS block verified on hardware with fused SiLU (5/5 pass)

### Active Risks & Blockers (Updated)

1. **DMA BD size limit (1023)** — **RESOLVED.** TAP 4D decomposition with d3≤64, d0 even constraint. `_factorize_tensor()` and `_factorize_3d()` helpers in design.py.

2. **L1 memory overflow for 1×1 convs** — `_auto_columns()` only checked weight size, not total L1 budget (input+weight+output+stack). FIXED by pipeline-runner: updated `_auto_columns` to check full L1 for 1×1 conv.

3. **UNFIXABLE L1 overflow (3 configs)** — Input FIFO alone exceeds 64KB L1:
   - `384→128 k1 40×40` (neck L12 cv1): input_fifo = 61,440B > 64KB
   - `192→64 k1 80×80` (neck L15 cv1): input_fifo = 61,440B > 64KB
   - `512→256 k1 20×20` (SPPF cv2): input+min_weight > 64KB
   **Needs**: MemTile input buffering or width tiling (route input through 512KB MemTile instead of direct to compute tile).

4. **80-channel detect head problem** — cls branches use 80→80 3×3 convs. Weight = 80×80×9×2 = 115KB at cols=1, 57KB at cols=2. No column count fits L1. **Needs**: weight streaming through MemTile, or padding to 88ch (but 88/cols must still be ÷8).

5. **128→256 k3s2 40×40 (bb_l7)** — Even at 8 cols, weight = 32×128×9×2 = 73KB > 40KB. **Needs**: weight streaming.

2. **Pipeline doesn't use fused SiLU yet** — The pipeline creates sub-operators with `activation=None` and applies `F.silu()` in Python. The fused kernel is used by the standalone CBS block class but not by the pipeline's `_run_cbs()`. Integrating fused SiLU into the pipeline requires creating sub-operators with `activation='silu'` and removing the Python-side `F.silu()` call. This is a follow-up optimization.

3. **Backbone/Neck/Detect not re-tested with fused SiLU** — The individual CBS test passes, but the full backbone→neck→detect flow with fused SiLU has not been re-verified. The existing tests in `test_backbone.py` and `test_neck_detect.py` will exercise this path since CBS now defaults to `activation='silu'`.

4. **Weight re-tiling every forward pass** — The pipeline re-converts weights from NCHW to tiled layout on every forward call. For production, weights should be pre-tiled at `load_weights()` time and stored as static data (like SwiGLU does).

5. **3x3 conv scalar kernel is very slow** — Benchmarks show 76ms for 32→32 at 16x16 (scalar). The vectorized kernel exists but has codegen issues with runtime-variable outer loops. Vectorized 3x3 is critical for acceptable inference latency.

### Hardware-Verified YOLOv8n Configs (7/8 backbone pass)

| Config | Cols | HW Status | Notes |
|--------|------|-----------|-------|
| 8→16 k3s2 640×640 | 1 | **PASS** | L0 backbone |
| 16→32 k3s2 320×320 | 1 | **FAIL** | L1 overflow (depth-4 FIFO + weights > 64KB). Needs MemTile input |
| 32→32 k1 160×160 | 1 | **PASS** | L2 cv1 |
| 64→64 k1 80×80 | 1 | **PASS** | L4 cv1 |
| 128→128 k1 40×40 | 2 | **PASS** | L6 cv1 (auto-columns) |
| 16→16 k3s1 160×160 | 1 | **PASS** | L2 bottleneck |
| 32→32 k3s1 80×80 | 1 | **PASS** | L4 bottleneck |
| 64→64 k3s1 40×40 | 2 | **PASS** | L6 bottleneck (auto-columns) |

### Configs Needing MemTile Routing (Phase 7)

| Config | Issue | Solution |
|--------|-------|----------|
| 16→32 k3s2 320×320 | Depth-4 input FIFO (40KB) + weight + output > 64KB | MemTile input buffering |
| 384→128 k1 40×40 | Input FIFO alone = 61KB > 64KB | MemTile input buffering |
| 192→64 k1 80×80 | Input FIFO alone = 61KB > 64KB | MemTile input buffering |
| 512→256 k1 20×20 | Input + min weight > 64KB | MemTile input buffering |
| 80→80 k3 (detect cls) | Weight = 115KB at cols=1, 57KB at cols=2 | Weight streaming via MemTile |
| 128→256 k3s2 40×40 | Weight = 73KB even at 8 cols | Weight streaming via MemTile |

### Phase 7 Solution: MemTile Tiling via `forward()` + `dims_to_stream`

The IRON/mlir-aie framework supports **MemTile-backed ObjectFIFO links** that buffer
large tensors in MemTile (512KB) and stream small chunks to ComputeTile L1 (64KB).

**Pattern** (from GEMM `design.py` and `single_core_iron.py`):
```python
# Instead of: DDR → ComputeTile directly (L1 overflow)
in_fifo = ObjectFifo(large_row_ty, name="in", depth=2)

# Use: DDR → MemTile (full row buffered) → ComputeTile (channel-group chunks)
in_fifo = ObjectFifo(large_row_ty, name="in_L3L2", depth=2)
in_l1 = in_fifo.cons().forward(
    obj_type=small_chunk_ty,            # L1-sized chunk
    name="in_L2L1",
    placement=AnyMemTile,               # Route through MemTile
    dims_to_stream=[(n_cg, cg_size),    # Stream channel groups
                    (width, 8),         # Then spatial positions
                    (1, 1), (1, 1)],    # Pad to 4D
    depth=2,
)
```

**For input buffering** (solves 384→128 k1, 192→64 k1, etc.):
- MemTile holds full input row (e.g., 384×40 = 15360 elements = 30KB)
- `dims_to_stream` decomposes into channel-group chunks (8×40 = 320 elements)
- ComputeTile L1 only needs depth-2 × 320 × 2B = 1.3KB per FIFO

**For weight streaming** (solves 80→80 k3, 128→256 k3):
- MemTile holds full weight tensor
- `dims_to_stream` streams one output-channel-group's weights at a time
- Core processes one OC group per iteration, accumulates partial sums

**Key API**: `ObjectFifoHandle.forward(placement=AnyMemTile, dims_to_stream=...)`
- `dims_to_stream`: list of 4 `(iterations, stride)` tuples for MemTile DMA
- Acts like TAPs but for MemTile→ComputeTile transfers
- `dims_from_stream`: inverse for ComputeTile→MemTile (output path)

### Benchmark Results (Small-Scale, Scalar Kernels)

| Operator | Config | Exec Time |
|----------|--------|-----------|
| Conv2d 1×1 | 32→32 @ 32×32 | 322μs |
| Conv2d 1×1 | 64→64 @ 16×16 | 217μs |
| Conv2d 1×1 | 128→128 @ 8×8 | 245μs |
| Conv2d 3×3 s1 | 16→16 @ 8×8 | 4.6ms |
| Conv2d 3×3 s1 | 32→32 @ 8×8 | 18ms |
| Conv2d 3×3 s1 | 16→16 @ 16×16 | 19ms |
| Conv2d 3×3 s1 | 32→32 @ 16×16 | 76ms |
| Conv2d 3×3 s2 | 8→16 @ 16×16 | 2.3ms |
| MaxPool2d k5 | 128ch @ 8×8 | 3.9ms |
| Upsample 2× | 128ch @ 8×8 | 165μs |
| CBS (fused SiLU) | 16→16 k3 @ 8×8 | 4.6ms |
| Bottleneck | 16ch @ 8×8 | 9.3ms |

Full results: `iron/applications/yolov8n/benchmark_results.md`

### Lessons Learned During Implementation
- **`AIE_PREPARE_FOR_PIPELINING` + runtime-variable outer loop = bad codegen.** The Chess compiler generates incorrect code when pipelining an inner loop whose outer loop has a runtime-variable trip count. Use scalar kernels as a safe baseline.
- **`acquire(N)` with N≥5 may deadlock.** The sliding window `acquire(5)` + `release(1)` pattern caused FIFO deadlocks. Workaround: send input strips (kernel_size rows concatenated) as single FIFO elements with strided DMA.
- **DMA BD size fields limited to 1023.** Use all 4 TAP dimensions to decompose large transfers. Stride fields have larger limits (~20 bits).
- **Large FIFO elements exhaust L1.** 5-row strips of 128ch×24w = 30KB × 2 (double-buffer) = 60KB > 64KB L1. Must tile channels across cores for large layers.
- **aiecc flag `--aie-generate-npu` was renamed to `--aie-generate-npu-insts`.** Old flag silently ignored.

## Getting to End-to-End Today — Action Items

### Critical Path (in order)

1. **Implement multi-PDI XCLBIN chaining (P6.0a)** — ~2 hours
   - Create a single operator class that chains all conv/maxpool/upsample
     variants into 1-2 shared XCLBINs using `xclbin_input`
   - Follow the `swiglu_decode/op.py` pattern (lines 56-82)
   - This eliminates the 32-context exhaustion blocker

2. **Wire up full backbone+neck+detect pipeline** — ~1 hour
   - `backbone.py` + `neck.py` + `detect.py` already exist and work individually
   - Create `inference.py` that chains all three
   - Use random weights first (verify shapes flow correctly)

3. **Load real YOLOv8n weights** — ~30 min
   - `model_prep.py:export_yolov8n_weights()` already implemented
   - `pip install ultralytics` → export → load into pipeline

4. **Run on a test image** — ~30 min
   - Preprocess: resize to 640×640, normalize, convert to bf16
   - Run through pipeline
   - Post-process: DFL decode, NMS (on CPU)
   - Visualize detections

### Known Blockers & Workarounds

| Blocker | Impact | Workaround |
|---------|--------|------------|
| NPU context exhaustion (32 limit) | Can't run all layers in one session | Multi-PDI XCLBIN (P6.0) or run layers in batches |
| 80ch classification conv exceeds L1 | Detect cls branch at full scale | Use 64ch for testing, or pad to 88ch, or weight streaming (P6.1) |
| 640×640 input → 320×320 early layers | Large activation bandwidth | Start at 160×160 input to test pipeline, scale up later |
| 3×3 scalar kernel is slow | Performance, not correctness | Acceptable for first end-to-end; optimize in P6.2 |

### Debugging Checklist

If a layer fails with **ERT_CMD_STATE_TIMEOUT**:
- FIFO deadlock: check acquire/release counts match DMA fill/drain counts
- Generate MLIR directly: `python3 -c "from ...design import my_conv2d; print(my_conv2d(...))"`
- Count: total DMA elements sent = total core acquires; total core releases = total FIFO drain

If a layer fails with **L1 overflow** (`allocated buffers exceeded available memory`):
- Check `_auto_columns()` returned correct column count
- Verify `rm -rf build/<artifact_name>*` to force recompilation with new columns
- Weight size per core = `C_in × (C_out/cols) × K × K × 2` must be < 40KB

If a layer fails with **DRM_IOCTL_AMDXDNA_CREATE_HWCTX**:
- Hardware context exhaustion — too many unique XCLBINs loaded
- Workaround: run tests individually (`pytest -k test_name`)
- Fix: implement multi-PDI XCLBIN chaining (P6.0)

If a layer produces **numerical mismatches**:
- Check tolerance: composed blocks need `rel_tol=0.15, abs_tol=5.0`
- Ensure reference uses bf16 at every layer boundary (not float32 accumulation)
- Use NPU output from layer N as reference input to layer N+1 (cascade test pattern)
- For >1% element-wise outliers, check kernel correctness with scalar fallback

### Files Overview

```
iron/operators/                          # Low-level NPU operators (DONE)
  conv2d/{op,design,reference,test}.py   # 1×1 and 3×3, stride 1+2
  maxpool2d/{op,design,reference,test}.py # 5×5 stride 1, strip-based
  upsample/{op,design,reference,test}.py  # 2× nearest neighbor

iron/applications/yolov8n/               # YOLOv8n application
  model_prep.py                          # BN fusion, layout utils, weight export (DONE)
  blocks.py                              # CBS, Bottleneck, C2f, SPPF composites (DONE)
  backbone.py                            # Backbone L0-L9 pipeline (DONE)
  neck.py                                # FPN up + PAN down pipeline (DONE)
  detect.py                              # Detect head reg+cls branches (DONE)
  inference.py                           # Full pipeline (TODO — wire up)
  test_model_prep.py                     # 12 CPU tests (PASS)
  test_backbone.py                       # 5 HW tests (PASS)
  test_neck_detect.py                    # 5 HW tests (PASS)

aie_kernels/aie2p/                       # AIE compute kernels (DONE)
  conv2dk1_bf16.cc                       # 1×1 conv (vectorized mmul<4,8,8>)
  conv2dk3_bf16.cc                       # 3×3 conv (scalar, stride 1+2)
  maxpool2d_bf16.cc                      # 5×5 maxpool (strip-based scalar)
  upsample2x_bf16.cc                     # 2× nearest (vectorized load/store)
```

### Quick Test Commands

```bash
# Setup
source /scratch/jmelber/mlir-aie/ironenv/bin/activate
source /scratch/jmelber/mlir-aie/utils/env_setup.sh /scratch/jmelber/mlir-aie /opt/xrt

# Run all operator tests (non-extensive)
pytest iron/operators/conv2d/test.py iron/operators/maxpool2d/test.py iron/operators/upsample/test.py -m "not extensive" --iterations=1 -v

# Run composite block tests (run individually to avoid context exhaustion)
pytest iron/applications/yolov8n/test_backbone.py -k "test_cbs_block" --iterations=1 -v
pytest iron/applications/yolov8n/test_backbone.py -k "test_bottleneck" --iterations=1 -v
pytest iron/applications/yolov8n/test_backbone.py -k "test_c2f" --iterations=1 -v
pytest iron/applications/yolov8n/test_backbone.py -k "test_backbone_l0_l2" --iterations=1 -v

# Run neck + detect tests (individually)
pytest iron/applications/yolov8n/test_neck_detect.py -k "test_neck_fpn_up" --iterations=1 -v
pytest iron/applications/yolov8n/test_neck_detect.py -k "test_neck_pan_down" --iterations=1 -v
pytest iron/applications/yolov8n/test_neck_detect.py -k "test_detect_branch" --iterations=1 -v
pytest iron/applications/yolov8n/test_neck_detect.py -k "test_neck_full" --iterations=1 -v
pytest iron/applications/yolov8n/test_neck_detect.py -k "test_detect_head_p5" --iterations=1 -v

# Clean and rebuild a specific operator
rm -rf build/<operator_name>*
pytest iron/operators/<name>/test.py -k "<test_name>" --iterations=1 -v -s
```

---

## Executive Summary

This document lays out a phased plan to implement YOLOv8n (nano) object detection
on AMD Ryzen AI NPU2 (AIE2+, Strix) using the IRON framework. The approach is
**layer-by-layer**: build parameterized operators for each CNN primitive, validate
them individually across all required shapes, then stitch them into a full inference
pipeline.

YOLOv8n has 3.16M parameters, 8.9 GFLOPs, and requires only **7 distinct operator
types** (with BN fused into Conv). The NPU2 provides 32 compute cores across 8
columns with 64KB L1 each, 8 memtiles with 512KB L2 each, and hardware support for
int8/bf16 MAC operations at high throughput.

---

## 1. Hardware Budget: NPU2 (AIE2+)

```
Row 5: C C C C C C C C   ← 32 compute tiles (64KB L1 each)
Row 4: C C C C C C C C
Row 3: C C C C C C C C
Row 2: C C C C C C C C
Row 1: M M M M M M M M   ← 8 memory tiles (512KB L2 each)
Row 0: S S S S S S S S   ← 8 shim DMA tiles (DDR interface)
       0 1 2 3 4 5 6 7
```

| Resource            | Per Tile    | Total       |
|---------------------|-------------|-------------|
| Compute cores       | 1           | 32          |
| L1 memory           | 64 KB       | 2 MB        |
| L2 (MemTile)        | 512 KB      | 4 MB        |
| DMA channels/core   | 2 in + 2 out| 128         |
| DMA BDs/core        | 16          | 512         |
| DMA BDs/memtile     | 48          | 384         |
| Locks/core          | 16          | 512         |
| Locks/memtile       | 64          | 512         |

**Key AIE2+ compute capabilities:**
- **bf16 mmul**: `aie::mmul<4,8,8,bfloat16>` or `<8,8,8>` → 128 or 256 MACs/cycle
- **int8 mmul**: `aie::mmul<8,8,8,int8>` → 512 MACs/cycle (highest throughput)
- **Vector width**: 512-bit datapath (64 x int8, 32 x bf16, 16 x float32)
- **Hardware SiLU**: AIE2+ has `aie::tanh` + `aie::inv` for sigmoid; compose for SiLU
- **4D strided DMA**: Hardware address generator supports 4D nested strides

**PDI/XCLBIN reconfiguration**: Loading a new column configuration takes ~50-200μs
per reconfiguration event (column-granular via partial reconfiguration). This is
significant when switching dataflow layouts between layers.

---

## 2. YOLOv8n Architecture (640×640 Input)

### 2.1 Model Parameters

| Parameter           | Value       |
|---------------------|-------------|
| Input               | 640×640×3   |
| width_multiple      | 0.25        |
| depth_multiple      | 0.33        |
| Parameters          | 3,157,200   |
| GFLOPs              | 8.9         |
| Output              | [1, 84, 8400] |
| Classes (COCO)      | 80          |

### 2.2 Channel Scaling (nano)

| Base channels | Scaled (×0.25) |
|---------------|----------------|
| 64            | **16**         |
| 128           | **32**         |
| 256           | **64**         |
| 512           | **128**        |
| 1024          | **256**        |

### 2.3 Complete Layer-by-Layer

```
INPUT:     640 × 640 ×   3
─────────── BACKBONE ───────────
L0  Conv3×3 s2:  320 × 320 ×  16   (P1/2)
L1  Conv3×3 s2:  160 × 160 ×  32   (P2/4)
L2  C2f(n=1):    160 × 160 ×  32   (shortcut=True)
L3  Conv3×3 s2:   80 ×  80 ×  64   (P3/8)   ──── skip to L14
L4  C2f(n=2):     80 ×  80 ×  64   (shortcut=True) ── skip to L14
L5  Conv3×3 s2:   40 ×  40 × 128   (P4/16)  ──── skip to L11
L6  C2f(n=2):     40 ×  40 × 128   (shortcut=True) ── skip to L11
L7  Conv3×3 s2:   20 ×  20 × 256   (P5/32)
L8  C2f(n=1):     20 ×  20 × 256   (shortcut=True)
L9  SPPF(k=5):    20 ×  20 × 256            ──── skip to L20
─────────── NECK (FPN UP) ───────────
L10 Upsample 2×:  40 ×  40 × 256
L11 Concat:        40 ×  40 × 384   (L10 + L6)
L12 C2f(n=1):      40 ×  40 × 128   (no shortcut) ── skip to L17
L13 Upsample 2×:   80 ×  80 × 128
L14 Concat:         80 ×  80 × 192   (L13 + L4)
L15 C2f(n=1):      80 ×  80 ×  64   (no shortcut) → Detect P3
─────────── NECK (PAN DOWN) ───────────
L16 Conv3×3 s2:    40 ×  40 ×  64
L17 Concat:         40 ×  40 × 192   (L16 + L12)
L18 C2f(n=1):      40 ×  40 × 128   (no shortcut) → Detect P4
L19 Conv3×3 s2:    20 ×  20 × 128
L20 Concat:         20 ×  20 × 384   (L19 + L9)
L21 C2f(n=1):      20 ×  20 × 256   (no shortcut) → Detect P5
─────────── DETECT HEAD ───────────
L22 Detect:  3-scale decoupled head → [1, 84, 8400]
```

### 2.4 C2f Internal Structure

```
Input(c_in) → Conv1×1(c_in → 2c) → chunk → Part_A(c) + Part_B(c)
                                              │              │
                                              │    Bottleneck_1(c→c)
                                              │         │
                                              │    Bottleneck_n(c→c)
                                              │         │    │
                                    Concat([A, B, BN1...BNn]) = (2+n)×c
                                              │
                                    Conv1×1((2+n)×c → c_out)
                                              │
                                         Output(c_out)
```

Each Bottleneck: `Conv3×3(c→c) → Conv3×3(c→c) [+ residual if shortcut=True]`

### 2.5 SPPF Structure

```
Input(256) → Conv1×1(256→128) → [identity, MP5×5, MP5×5, MP5×5]
                                         │
                                  Concat(128×4=512)
                                         │
                                  Conv1×1(512→256) → Output(256)
```

### 2.6 Detect Head (Per Scale)

```
Feature(C_in) ─┬─ Reg: Conv3×3(C_in→64) → Conv3×3(64→64) → Conv1×1(64→64) → DFL
               └─ Cls: Conv3×3(C_in→80) → Conv3×3(80→80) → Conv1×1(80→80)
```

### 2.7 All Required Primitive Operations

| # | Operation       | Kernel | Stride | Pad | Instances |
|---|-----------------|--------|--------|-----|-----------|
| 1 | Conv2d+BN+SiLU  | 3×3    | 2      | 1   | 7         |
| 2 | Conv2d+BN+SiLU  | 3×3    | 1      | 1   | ~22       |
| 3 | Conv2d+BN+SiLU  | 1×1    | 1      | 0   | ~18       |
| 4 | Conv2d (bare)   | 1×1    | 1      | 0   | 7         |
| 5 | MaxPool2d       | 5×5    | 1      | 2   | 3         |
| 6 | Upsample        | 2×     | —      | —   | 2         |
| 7 | Concat          | —      | —      | —   | 4         |
| 8 | Elementwise Add | —      | —      | —   | ~8        |
| 9 | SiLU            | —      | —      | —   | (fused)   |

---

## 3. Data Type and Quantization Strategy

### 3.1 Primary: INT8 Quantized Inference

INT8 is the target for production deployment:
- **4× throughput** vs bf16 on AIE2+ (512 vs 128 MACs/cycle)
- **4× memory savings** (weights + activations)
- Matches the mlir-aie conv2d reference kernels (all int8)
- YOLOv8n INT8 model is ~2MB, fits entirely in MemTile L2 budget (4MB)

**Quantization approach**: Post-training quantization (PTQ) using PyTorch's
quantization toolkit or Ultralytics export. Fuse Conv+BN+ReLU/SiLU at export time.

For SiLU in INT8: Approximate with a piecewise linear or LUT. The saturation
behavior of SiLU in int8 range (-128..127) is well-bounded. Alternatively, use
bf16 for the activation portion only (mixed-precision).

### 3.2 Development: BF16

For initial development and debugging, use bf16 throughout:
- Simpler to validate correctness against PyTorch reference
- No quantization calibration needed
- Existing IRON SiLU operator works directly
- `aie::mmul<4,8,8,bfloat16>` provides adequate throughput for prototyping

### 3.3 BatchNorm Fusion

For inference, BatchNorm is **always folded into Conv weights**:
```
W_fused = W * (gamma / sqrt(running_var + eps))
b_fused = beta - running_mean * gamma / sqrt(running_var + eps)
```
This is a standard offline transformation. The fused Conv2d then has bias=True.

---

## 4. Data Layout

### 4.1 Activation Layout: `Y{C/8}X{C8}` (Channel-last with 8-wide grouping)

This is the proven layout from the mlir-aie conv2d examples:
```
Memory order: [y][c_group][x][c_sub]
  where c_group = C/8, c_sub = 8
```

**Why this layout:**
- Aligns with AIE SIMD width (8 elements for int8 mmul)
- Enables efficient vector loads: `aie::load_v<8>()` gets 8 channels at once
- Compatible with 4D strided DMA: one BD can tile across height/width/channels
- Same layout used in proven conv2d, conv3d, and ResNet examples

### 4.2 Weight Layout: `{O/8}{I/8}YX{I8}{O8}`

```
Memory order: [o_group][i_group][ky][kx][i_sub][o_sub]
  where o_group = O/8, i_group = I/8, i_sub = 8, o_sub = 8
```

This puts the inner dimensions at the SIMD width for direct mmul feeding.

### 4.3 Layout Conversion

Provide Python utilities for NCHW ↔ Y{C/8}X{C8} conversion at model load time.
During inference, all data stays in the tiled layout.

---

## 5. Operator Implementation Plan

### 5.1 Operator Inventory

We need 6 new IRON operators (plus leverage 2 existing ones):

| # | Operator         | New/Existing | Priority | Complexity |
|---|-----------------|--------------|----------|------------|
| 1 | Conv2d 1×1      | **New**      | P0       | Medium     |
| 2 | Conv2d 3×3 s1   | **New**      | P0       | High       |
| 3 | Conv2d 3×3 s2   | **New**      | P0       | High       |
| 4 | MaxPool2d 5×5   | **New**      | P1       | Medium     |
| 5 | Upsample 2×     | **New**      | P1       | Low        |
| 6 | Concat (chan)    | **New**      | P1       | Low-Med    |
| 7 | SiLU            | Existing     | —        | Done       |
| 8 | Elementwise Add | Existing     | —        | Done       |

### 5.2 Conv2d Operator Design (The Core)

This is the most critical and complex operator. Following the IRON 4-file pattern:

#### `iron/operators/conv2d/op.py` — AIEConv2d

```python
class AIEConv2d(AIEOperatorBase):
    def __init__(self,
                 in_channels,      # Input channels
                 out_channels,     # Output channels
                 kernel_size,      # 1 or 3
                 stride=1,         # 1 or 2
                 height=None,      # Feature map height
                 width=None,       # Feature map width
                 has_bias=True,    # Bias (from fused BN)
                 activation=None,  # None, 'silu', 'relu'
                 num_cores=4,      # AIE cores to use
                 ):
```

**Parameterization axes:**
- `kernel_size ∈ {1, 3}` — different kernel implementations
- `stride ∈ {1, 2}` — stride-2 halves spatial dimensions
- `activation ∈ {None, 'silu'}` — fused activation avoids extra DDR round-trip
- Channel/spatial dims — drive tiling decisions

#### `iron/operators/conv2d/design.py` — Hardware Design

**Tiling strategy (following ResNet example patterns):**

For a conv with input `[H, W, C_in]` and output `[H', W', C_out]`:

1. **Spatial tiling**: Process one row (or row-strip) at a time
   - Row tile = `[1, W, C_in]` for 1×1; `[3, W, C_in]` for 3×3 (needs 3 rows)
   - Fits in L1: `W × C_in × 8 bytes` per row (bf16, double-buffered)

2. **Output channel tiling**: Split `C_out` across cores
   - Each core produces `C_out / num_cores` output channels
   - Weights for that channel slice loaded per core

3. **Input channel accumulation**: Loop over `C_in` groups within each core
   - Inner mmul loop: `aie::mmul<r,s,t>` accumulates partial sums

**Memory budget check (worst case: L0, 320×320×16→320×320×16, 3×3 s1):**
- Input tile (3 rows): 3 × 320 × 16 = 15,360 bytes (bf16) × 2 (double-buf) = 30 KB
- Output tile (1 row): 1 × 320 × 4 = 1,280 bytes × 2 = 2.5 KB  (4 ch/core)
- Weights (per core): 3 × 3 × 16 × 4 = 576 bytes
- Total per core: ~33 KB ✓ (fits in 48KB usable L1)

**For deeper layers (L7, 40×40×128→20×20×256, 3×3 s2):**
- Input tile (3 rows): 3 × 40 × 128 = 15,360 bytes × 2 = 30 KB
- Output tile (1 row): 1 × 20 × 32 = 640 bytes × 2 = 1.3 KB (32 ch/core for 8 cores)
- Weights (per core): 3 × 3 × 128 × 32 = 36,864 bytes → **Too large for L1!**

**Solution for large weight layers**: Stream weights from MemTile via ObjectFIFO.
Don't preload all weights — stream weight tiles as needed:
- Weight tile size: `3 × 3 × C_in_group × C_out_group` where groups are SIMD-sized (8)
- Weight FIFO depth=2 for double-buffering
- MemTile holds the full weight partition for one core column

#### `iron/operators/conv2d/reference.py` — Golden Reference

```python
def conv2d_reference(input, weight, bias, stride, padding, activation):
    # Use torch.nn.functional.conv2d for golden values
    out = F.conv2d(input, weight, bias, stride=stride, padding=padding)
    if activation == 'silu':
        out = F.silu(out)
    return out
```

#### Kernel Implementations

Following the aie2/aie2p split pattern:

**`aie_kernels/aie2p/conv2dk1.cc`** — 1×1 convolution kernel
- Pure pointwise operation: each output pixel is a dot product over channels
- Use `aie::mmul<4,8,8,bfloat16>` for bf16 or `<8,8,8,int8>` for int8
- Stride-2 variant: skip every other input pixel in x and y

**`aie_kernels/aie2p/conv2dk3.cc`** — 3×3 convolution kernel
- Sliding window: accumulate 9 mmul products per output pixel
- Load 3 rows of input, slide across width
- For stride-2: output every other pixel position

**`aie_kernels/aie2p/conv2dk3_silu.cc`** — 3×3 + fused SiLU
- Same as conv2dk3 but applies `x * sigmoid(x)` after accumulation
- Uses hardware `aie::tanh` for sigmoid: `sigmoid(x) = 0.5 * (1 + tanh(x/2))`

### 5.3 MaxPool2d Operator

```
iron/operators/maxpool2d/
  ├── op.py          # AIEMaxPool2d(kernel_size, stride, padding, H, W, C)
  ├── design.py      # Simple: 1 core per channel group
  ├── reference.py   # torch.nn.functional.max_pool2d
  └── test.py        # Parametrized tests
```

**Implementation**: Row-based sliding window with `aie::reduce_max()`.
For 5×5 s1 p2: load 5 rows, slide 5-wide window, take max across the 25 elements.
Each output pixel requires comparing 25 values — no mmul needed, pure comparison.

**Memory**: Lightweight. 5 rows × W × C_group fits easily in L1.

### 5.4 Upsample 2× (Nearest Neighbor) Operator

```
iron/operators/upsample/
  ├── op.py          # AIEUpsample(scale_factor, H, W, C)
  ├── design.py      # Duplicate-in-place via DMA or simple core logic
  ├── reference.py   # torch.nn.functional.interpolate
  └── test.py
```

**Implementation options:**
1. **DMA-only**: Use 4D strided DMA to read each pixel once, write it to 4
   output locations (2×2 replication). No compute core needed — pure data movement.
2. **Core-based**: Simple kernel that reads a row and writes each element twice
   to two output rows. Trivial vectorization.

Option 1 is preferred if the DMA BD count permits it. Option 2 is the fallback.

### 5.5 Concat (Channel Dimension) Operator

```
iron/operators/concat/
  ├── op.py          # AIEConcat(tensors_info, dim=1)
  ├── design.py
  ├── reference.py   # torch.cat(tensors, dim=1)
  └── test.py
```

**Implementation**: In the `Y{C/8}X{C8}` layout, channel concatenation means
interleaving channel groups. Two approaches:

1. **Host-side (zero-copy)**: If both tensors are contiguous in DDR, simply pass
   both buffer pointers to the next operator's DMA sequence. The next layer's
   input FIFO reads from two DDR regions with appropriate strides. **No compute
   or copy needed.**

2. **DMA-based**: Use two DMA sequences that fill the same MemTile buffer at
   different channel offsets. The downstream core sees a unified activation tensor.

Option 1 is strongly preferred — it eliminates an entire operator from the critical
path.

### 5.6 Leveraging Existing Operators

**SiLU** (`iron/operators/silu/`): Already implemented for both AIE2 and AIE2+.
For fused Conv+SiLU, inline the SiLU logic into the conv kernel. For standalone
use (if needed), use as-is.

**Elementwise Add** (`iron/operators/elementwise_add/`): Already implemented.
Used for residual/skip connections in Bottleneck blocks. May need a shape-aware
wrapper for the tiled layout, but the core kernel is ready.

---

## 6. Tiling and Dataflow Strategies

### 6.1 Per-Layer Tiling Analysis

The challenge: early layers have large spatial dimensions but few channels; deep
layers have small spatial dimensions but many channels. The tiling strategy must
adapt.

| Layer Group    | Spatial | Channels | Bottleneck    | Strategy                  |
|----------------|---------|----------|---------------|---------------------------|
| L0-L2          | 320-160 | 16-32    | Activation BW | Row-by-row, all ch/core   |
| L3-L4          | 80      | 64       | Balanced      | Row-by-row, ch-split      |
| L5-L6          | 40      | 128      | Weights       | Row-by-row, stream wts    |
| L7-L9          | 20      | 256      | Weights       | Full map, stream wts      |
| L10-L15 (neck) | 40-80   | 64-384   | Varies        | Adaptive per layer        |
| L16-L21 (PAN)  | 20-40   | 128-384  | Weights       | Row-by-row, stream wts    |
| Detect head    | 20-80   | 64-256   | Moderate      | Per-scale processing      |

### 6.2 Core Allocation Strategies

**Strategy A: Spatial Parallelism (early layers)**
- Split the spatial dimension across cores
- Each core processes a horizontal strip of the feature map
- Good when channels are few and spatial dimensions are large
- Example: L0 (320×320×16) → 8 cores, each handles 40 rows

**Strategy B: Output Channel Parallelism (deep layers)**
- Split output channels across cores
- Each core computes all spatial positions for its channel slice
- Good when channels are many and spatial dimensions are small
- Example: L7 (40×40×128→20×20×256) → 8 cores, each produces 32 output channels

**Strategy C: Hybrid (mid layers)**
- Split both spatially and across channels
- 2×4 grid: 2 spatial partitions × 4 channel partitions
- Example: L5 (80×80×64→40×40×128) → 4 channel groups × 2 spatial strips

### 6.3 Depth-First vs Layer-by-Layer Execution

**Layer-by-Layer** (initial approach):
- Each layer runs as a separate XCLBIN invocation
- Activations round-trip through DDR between layers
- Simple to implement and debug
- Reconfiguration overhead: ~100-200μs per layer × 22 layers ≈ 2-4ms overhead

**Depth-First Pipelining** (optimization target):
- Chain multiple layers in a single XCLBIN
- Activations flow core-to-core via ObjectFIFO (no DDR round-trip)
- Following the ResNet conv2_x example: 3 bottleneck blocks in one design
- Dramatically reduces DDR bandwidth pressure

**Recommended phasing:**
1. Start layer-by-layer for correctness
2. Fuse Conv+BN+SiLU within each operator (trivial, just kernel fusion)
3. Fuse consecutive Conv+C2f blocks (medium complexity)
4. Eventually: full backbone or full neck as single XCLBIN (advanced)

### 6.4 Activation Memory Between Layers

For layer-by-layer execution, the host must manage intermediate activation buffers
in DDR. Peak memory:

```
L0 output:  320 × 320 × 16 × 2B = 3.28 MB (bf16)
L1 output:  160 × 160 × 32 × 2B = 1.64 MB
L3 output:   80 ×  80 × 64 × 2B = 819 KB
...
```

**Total DDR budget for activations**: ~8-10 MB (double-buffered ping-pong).
This is well within typical system DDR availability.

For the **skip connections** (L4→L14, L6→L11, L9→L20), the backbone activation
must be retained in DDR until the neck layer consumes it. This means we need
simultaneous storage for:
- L4 output: 80×80×64 = 819 KB
- L6 output: 40×40×128 = 410 KB
- L9 output: 20×20×256 = 205 KB
- Current layer input + output

Total: ~6-8 MB concurrent activation storage. Manageable.

---

## 7. Phased Implementation Plan

### Phase 0: Infrastructure & Model Preparation (1-2 weeks)

- [ ] **P0.1**: Export YOLOv8n with fused BN from PyTorch
  - Use `ultralytics` to export with BN folded into Conv weights+bias
  - Extract all weight tensors in the fused form
  - Save as numpy/safetensors with proper naming

- [ ] **P0.2**: Layout conversion utilities
  - `nchw_to_tiled(tensor, group_size=8)` → Y{C/8}X{C8} format
  - `tiled_to_nchw(tensor, C, group_size=8)` → standard NCHW
  - Weight reordering: PyTorch `[O,I,H,W]` → `{O/8}{I/8}HW{I8}{O8}`
  - Unit tests for round-trip conversion

- [ ] **P0.3**: Reference implementation
  - Full YOLOv8n inference in PyTorch (CPU)
  - Dump intermediate activations at every layer boundary (golden values)
  - Use `torch.manual_seed(42)` for reproducible inputs

- [ ] **P0.4**: Test harness
  - Parametrized test framework for conv2d: sweep over all (C_in, C_out, H, W, k, s)
    combinations that appear in YOLOv8n
  - Tolerance ladder: standalone conv uses `rel_tol=0.02, abs_tol=1e-4` (tighter
    than composed operators)

### Phase 1: Conv2d 1×1 Operator (2-3 weeks)

- [ ] **P1.1**: AIE kernel — `conv2dk1_bf16.cc`
  - Pointwise convolution using `aie::mmul<4,8,8,bfloat16>`
  - Input: `[tile_h, tile_w, c_in_group, 8]`, Output: `[tile_h, tile_w, c_out_group, 8]`
  - Weights: `[c_out_group, c_in_group, 8, 8]`
  - Inner loop accumulates over `c_in_group`, outer loop over spatial positions
  - Bias addition after accumulation
  - Optional fused SiLU

- [ ] **P1.2**: Design — ObjectFIFO topology
  - DDR → ShimDMA → MemTile (activation broadcast) → Cores (channel-parallel)
  - DDR → ShimDMA → MemTile (weight split) → Cores
  - Cores → MemTile (join) → ShimDMA → DDR

- [ ] **P1.3**: Op wrapper — `AIEConv2d(kernel_size=1, ...)`
  - Implement `set_up_artifacts()`, `set_up_runtime()`, `forward()`
  - Handle padding to SIMD-aligned channel counts
  - Weight layout transformation on first call (cached)

- [ ] **P1.4**: Validate against all YOLOv8n 1×1 conv shapes:
  | Location | c_in | c_out | H×W     |
  |----------|------|-------|---------|
  | C2f cv1  | 32   | 32    | 160×160 |
  | C2f cv1  | 64   | 64    | 80×80   |
  | C2f cv1  | 128  | 128   | 40×40   |
  | C2f cv1  | 256  | 256   | 20×20   |
  | C2f cv1  | 384  | 128   | 40×40   |
  | C2f cv1  | 192  | 64    | 80×80   |
  | C2f cv2  | 48   | 32    | 160×160 |
  | C2f cv2  | 128  | 64    | 80×80   |
  | C2f cv2  | 256  | 128   | 40×40   |
  | C2f cv2  | 384  | 256   | 20×20   |
  | C2f cv2  | 192  | 128   | 40×40   |
  | C2f cv2  | 96   | 64    | 80×80   |
  | SPPF cv1 | 256  | 128   | 20×20   |
  | SPPF cv2 | 512  | 256   | 20×20   |
  | Det reg  | 64   | 64    | 80×80   |
  | Det reg  | 64   | 64    | 40×40   |
  | Det reg  | 64   | 64    | 20×20   |
  | Det cls  | 80   | 80    | 80×80   |
  | Det cls  | 80   | 80    | 40×40   |
  | Det cls  | 80   | 80    | 20×20   |

### Phase 2: Conv2d 3×3 Operator (2-3 weeks)

- [ ] **P2.1**: AIE kernel — `conv2dk3_bf16.cc`
  - 3×3 sliding window convolution
  - Requires 3 input rows buffered simultaneously
  - 9 mmul accumulations per output pixel
  - Two variants: stride=1 (same spatial) and stride=2 (halve spatial)
  - Padding: zero-pad borders (first/last row, first/last column)

- [ ] **P2.2**: Design — row-streaming architecture
  - Input FIFO: depth=4 (3 active rows + 1 prefetch)
  - Weight FIFO: streamed from MemTile per output channel group
  - Handle stride-2 by only writing every other output row/column

- [ ] **P2.3**: Fused Conv3×3+SiLU variant
  - After accumulation + bias, apply SiLU in-register
  - Avoids separate activation pass through DDR

- [ ] **P2.4**: Validate against all YOLOv8n 3×3 conv shapes:
  | Location      | c_in | c_out | H×W     | stride |
  |---------------|------|-------|---------|--------|
  | Backbone L0   | 3    | 16    | 640→320 | 2      |
  | Backbone L1   | 16   | 32    | 320→160 | 2      |
  | Backbone L3   | 32   | 64    | 160→80  | 2      |
  | Backbone L5   | 64   | 128   | 80→40   | 2      |
  | Backbone L7   | 128  | 256   | 40→20   | 2      |
  | Bottleneck    | 16   | 16    | 160×160 | 1      |
  | Bottleneck    | 32   | 32    | 80×80   | 1      |
  | Bottleneck    | 64   | 64    | 40×40   | 1      |
  | Bottleneck    | 128  | 128   | 20×20   | 1      |
  | Neck L16      | 64   | 64    | 80→40   | 2      |
  | Neck L19      | 128  | 128   | 40→20   | 2      |
  | Det reg       | 64   | 64    | 80×80   | 1      |
  | Det reg       | 128  | 64    | 40×40   | 1      |
  | Det reg       | 256  | 64    | 20×20   | 1      |
  | Det cls       | 64   | 80    | 80×80   | 1      |
  | Det cls       | 128  | 80    | 40×40   | 1      |
  | Det cls       | 256  | 80    | 20×20   | 1      |

  Special case: L0 has `c_in=3` (RGB) which doesn't divide by 8. Pad to 8 channels.

### Phase 3: Auxiliary Operators (1-2 weeks)

- [x] **P3.1**: MaxPool2d 5×5 — **DONE** (3/3 tests pass on hardware)
  - Strip-based design: 5 rows concatenated as one FIFO element
  - Scalar kernel processes strip → 1 output row
  - 4D TAP decomposition for large channel counts (>1023 BD size limit)
  - Known limitation: 128ch×20×20 extensive test exceeds L1 (needs multi-core tiling)

- [x] **P3.2**: Upsample 2× nearest — **DONE** (3/3 tests pass on hardware)
  - Core-based: kernel duplicates pixels horizontally, design loop handles vertical
  - Per input row: kernel called twice to produce 2 identical output rows
  - Pure data movement (no arithmetic)

- [ ] **P3.3**: Concat (channel dimension)
  - Implement as host-side zero-copy DDR pointer management
  - In `Y{C/8}X{C8}` layout, concatenated tensors can be fed to the next
    operator via two DMA fill sequences targeting the same input FIFO
  - Four instances with varying channel combinations

### Phase 4: Composite Module Testing (2-3 weeks)

- [ ] **P4.1**: CBS block (Conv+BN+SiLU)
  - Verify fused Conv+SiLU produces same output as separate Conv → SiLU
  - Test all 7 backbone downsample configurations

- [ ] **P4.2**: Bottleneck block
  - Chain: Conv3×3+SiLU → Conv3×3+SiLU → Add (residual)
  - Two approaches:
    - **Layer-by-layer**: 3 separate operator invocations + DDR round-trips
    - **Fused**: Single XCLBIN with 3 cores in pipeline (like ResNet example)
  - Test with and without shortcut

- [ ] **P4.3**: C2f block
  - Orchestration logic: Conv1×1 → chunk → Bottleneck(s) → concat → Conv1×1
  - This is the most complex composite — multiple data paths with fan-out/fan-in
  - Start with layer-by-layer, then explore fusion opportunities

- [ ] **P4.4**: SPPF block
  - Chain: Conv1×1 → MaxPool → MaxPool → MaxPool → Concat → Conv1×1
  - Only one instance (20×20×256), relatively cheap
  - MaxPool chain is sequential (each feeds next)

- [ ] **P4.5**: Detect head (per scale)
  - Two parallel branches: regression + classification
  - Can run branches on separate column groups simultaneously
  - Final DFL is a simple 1×1 conv (can run on CPU for simplicity)

### Phase 5: End-to-End Integration (2-3 weeks)

- [ ] **P5.1**: Layer-by-layer pipeline
  - Python orchestrator that calls operators sequentially
  - Manages DDR activation buffers between layers
  - Handles skip connections (retain activations for neck)
  - Profile total latency: compute + reconfiguration overhead

- [ ] **P5.2**: Post-processing
  - Decode box predictions (DFL + dist2bbox)
  - Non-maximum suppression (NMS) — run on CPU
  - Class probability thresholding

- [ ] **P5.3**: End-to-end accuracy validation
  - Run on COCO validation images
  - Compare mAP against PyTorch reference
  - Verify detection quality is within tolerance

- [ ] **P5.4**: Latency profiling and bottleneck analysis
  - Measure per-layer NPU execution time
  - Measure XCLBIN reconfiguration overhead per transition
  - Measure DDR bandwidth utilization
  - Identify the critical path

### Phase 6: Multi-PDI XCLBIN & Context Management (NEXT — pick up here)

> **STATUS: RESEARCHED, READY TO IMPLEMENT**
> This is the critical blocker for full-scale YOLOv8n end-to-end inference.
> Without it, running all ~20 unique operator configurations exhausts the
> NPU2's 32 hardware context limit.

#### Background

Each unique XCLBIN gets its own XRT `hw_context`. NPU2 supports 32 concurrent
contexts system-wide. With ~20 unique operator configurations (different channel
counts / spatial sizes), we hit the limit when running backbone+neck+detect in
one session.

#### Solution: Chain PDIs into Shared XCLBINs

IRON already supports this via `XclbinArtifact.xclbin_input` — used by
`swiglu_decode` to merge two kernels into one XCLBIN.

**How it works:**
```python
# Kernel A: compile normally with a unique kernel ID
k1_xclbin = XclbinArtifact.new("yolo_conv.xclbin", depends=[mlir_a, kernel_obj],
    extra_flags=["--xclbin-kernel-id=0x901", "--xclbin-instance-name=conv_k3_16ic"],
    kernel_name="conv_k3_16ic")

# Kernel B: chain into A's xclbin
k2_xclbin = XclbinArtifact.new("yolo_conv_v2.xclbin", depends=[mlir_b, kernel_obj],
    extra_flags=["--xclbin-kernel-id=0x902", "--xclbin-instance-name=conv_k1_32ic"],
    xclbin_input=k1_xclbin,   # ← merge into k1's xclbin
    kernel_name="conv_k1_32ic")
k2_xclbin.depends += [k1_xclbin]

# At runtime: both kernels share ONE hw_context
self.add_kernel("k1", combined_xclbin, "conv_k3_16ic", k1_insts)
self.add_kernel("k2", combined_xclbin, "conv_k1_32ic", k2_insts)
self.add_to_runlist("k1", "input", "weights_1", "output")
# ... later ...
self.add_to_runlist("k2", "input", "weights_2", "output")
```

**Key files:**
- `iron/common/compilation.py:119-127` — `XclbinArtifact` with `xclbin_input`
- `iron/common/compilation.py:376-379` — `--xclbin-input=` flag generation
- `iron/common/aie_context.py:173-187` — runlist construction (asserts same context)
- `iron/operators/swiglu_decode/op.py:56-82` — working example of multi-kernel chaining

#### Implementation Plan

- [ ] **P6.0a**: Create `AIEYOLOv8nPipeline` mega-operator class
  - Single `AIEOperatorBase` subclass that registers ALL conv/maxpool/upsample
    kernel variants into one shared XCLBIN via `xclbin_input` chaining
  - Each variant gets a unique `--xclbin-kernel-id` (0x901, 0x902, ...)
  - At runtime, select kernel by name and swap instruction buffers per layer
  - **Result: 1 hw_context for the entire model instead of 20+**

- [ ] **P6.0b**: Update `blocks.py` to use the mega-operator
  - CBS/C2f/Bottleneck forward() calls select the correct kernel by name
  - Weights written to shared buffers, kernel selected by `add_to_runlist()`
  - Runlist rebuilt per layer invocation (or use separate runlists per layer)

- [ ] **P6.0c**: Verify full backbone+neck+detect in one session
  - All 22 layers execute sequentially using 1-3 XCLBINs total
  - No `DRM_IOCTL_AMDXDNA_CREATE_HWCTX` errors

#### Grouping Strategy

| Mega-XCLBIN | Kernel IDs | Contains |
|-------------|------------|----------|
| `yolo_conv.xclbin` | 0x901-0x910 | All Conv2d variants (1×1/3×3, various C_in/C_out/H/W) |
| `yolo_aux.xclbin` | 0x920-0x925 | MaxPool2d + Upsample variants |

Or even simpler: one `yolo_all.xclbin` with every operator. The XCLBIN file
grows but compilation is cached — only the chaining step runs after initial build.

### Phase 6: Further Optimization

- [ ] **P6.1**: Weight streaming for large convolutions
  - 3×3 convs with >64 input channels × >40 output channels exceed L1
  - Stream weight tiles from MemTile via ObjectFIFO (depth=2)
  - Enables 80-channel classification branch at full scale
  - Reference: existing GEMV operator streams weights per output group

- [ ] **P6.2**: Vectorized 3×3 conv kernel
  - Current scalar kernel works but is slow
  - Fix the `AIE_PREPARE_FOR_PIPELINING` issue by restructuring the loop
  - Target: move `kh` loop inside the pipelined region with fixed trip count
  - Separate top/middle/bottom kernel functions with compile-time `kh` range

- [ ] **P6.3**: INT8 quantization
  - Implement int8 conv kernels using `aie::mmul<8,8,8,int8>` (4× throughput)
  - Add quantization scale handling (per-channel or per-tensor)
  - LUT-based SiLU for int8 (256-entry lookup table)
  - Calibrate using representative COCO images
  - Validate mAP degradation is acceptable (target: <1% mAP drop)

- [ ] **P6.4**: Depth-first layer fusion
  - Following ResNet conv2_x example: chain entire C2f block as pipeline
  - Core mapping: each conv in the C2f gets a dedicated core row
  - Inter-core ObjectFIFOs carry activations without DDR round-trip
  - Target specific bottleneck: backbone L5→L6 or neck stages

---

## 8. Detailed Core Mapping Examples

### 8.1 Conv3×3 s2 (L7: 40×40×128 → 20×20×256)

Using 8 columns, 4 rows = 32 cores:
```
Strategy: Output channel parallelism
- 8 columns × 32 output channels each = 256 total output channels
- Each core in a column handles a spatial strip

Column 0:           Column 1:         ...  Column 7:
Core(0,2): rows 0-4  Core(1,2): rows 0-4     Core(7,2): rows 0-4
Core(0,3): rows 5-9  Core(1,3): rows 5-9     Core(7,3): rows 5-9
Core(0,4): rows10-14  Core(1,4): rows10-14    Core(7,4): rows10-14
Core(0,5): rows15-19  Core(1,5): rows15-19    Core(7,5): rows15-19
   ↓ 32 ch out          ↓ 32 ch out             ↓ 32 ch out

MemTile(0,1): Input broadcast + weight partition for col 0
MemTile(1,1): Input broadcast + weight partition for col 1
...
```

Weight per column: 3×3×128×32 × 2B = 72 KB → fits in MemTile (512 KB)
Input per MemTile: 40×40×128 × 2B = 400 KB → fits in MemTile
Per-core input strip: 5 rows × 40 × 128 × 2B = 50 KB → needs streaming to L1

### 8.2 Conv1×1 (C2f cv2 L8: 384→256, 20×20)

```
Strategy: Channel parallelism, full spatial in each core
- 8 columns × 32 output channels = 256
- 20×20 spatial fits in L1: 20×20×32 × 2B = 25 KB per core output
- Input: 20×20×384 × 2B = 300 KB → stream from MemTile in channel groups

Each core:
  for c_in_group in range(384 / 8):
    load input_tile[20×20×8]        # from input FIFO
    load weight_tile[8×32]          # from weight FIFO
    accumulate: mmul(input, weight)
  add bias, apply activation
  write output[20×20×32]            # to output FIFO
```

### 8.3 Bottleneck Block (Fused, 3-Core Pipeline)

```
Core A (row 2): Conv3×3+SiLU
Core B (row 3): Conv3×3+SiLU
Core C (row 4): Elementwise Add (residual)

ObjectFIFO topology:
DDR → Shim → MemTile → FIFO_in → Core_A
                         ↓ (skip path: FIFO_skip → Core_C)
                  Core_A → FIFO_ab → Core_B
                                       ↓
                              Core_B → FIFO_bc → Core_C
                                                   ↓
                                        Core_C → FIFO_out → MemTile → Shim → DDR
```

This avoids two DDR round-trips compared to running each conv separately.

---

## 9. Risk Analysis and Mitigations

### 9.1 Reconfiguration Overhead

**Risk**: 22 XCLBIN loads at ~100-200μs each = 2-4ms overhead, potentially
dominating total inference time for a small model.

**Mitigations**:
- Layer fusion reduces reconfig count (Phase 6.1)
- Use `partial reconfiguration` to only reconfigure changed columns
- Pre-load next XCLBIN while current layer executes (if hardware supports)
- Amortize over batch of images

### 9.2 Early Layer Bandwidth Bottleneck

**Risk**: L0 processes 640×640×3→320×320×16 — the activation volume is 1.2M pixels.
DDR bandwidth may be the bottleneck, not compute.

**Mitigations**:
- Maximize spatial parallelism (all 32 cores working on different regions)
- Minimize DDR touches: fuse L0+L1+L2 to keep 320×320×16 intermediate on-chip
- Use DMA burst mode (512B bursts) for maximum bandwidth

### 9.3 Weight Streaming for Large Layers

**Risk**: L7's weights (128×256×3×3 = 295K params) don't fit in a single MemTile.
Need weight streaming which adds DMA scheduling complexity.

**Mitigations**:
- Split weights across multiple MemTiles (8 available)
- Pipeline weight loading with computation (load next group while computing current)
- INT8 quantization cuts weight size by 2× (147K × 1B = 147 KB fits in one MemTile)

### 9.4 C2f Complexity

**Risk**: C2f has a complex dataflow graph (split + multiple bottlenecks + concat).
Implementing this as a fused XCLBIN is architecturally challenging.

**Mitigations**:
- Start with layer-by-layer (each internal conv is a separate invocation)
- The C2f hidden channels are small in YOLOv8n (16-128), so DDR round-trips
  involve modest data volumes
- Fuse only if profiling shows C2f is the bottleneck

### 9.5 3-Channel RGB Input

**Risk**: L0 has 3 input channels, which doesn't align with the 8-channel group
size in the tiled layout.

**Mitigations**:
- Pad input to 8 channels (3 real + 5 zero) — wastes 62.5% bandwidth on L0 input
- Or: use a specialized 3-channel kernel for L0 only
- L0 is a single layer; the overhead is bounded and one-time

### 9.6 SiLU in INT8

**Risk**: SiLU is nonlinear and loses precision in INT8 range.

**Mitigations**:
- LUT-based SiLU: 256-entry lookup table, computed offline
- Piecewise linear approximation (4 segments sufficient for int8 range)
- Mixed precision: run conv in INT8, dequant to bf16 for SiLU, requant to INT8

---

## 10. Directory Structure

```
iron/operators/
  conv2d/
    op.py             # AIEConv2d — parameterized conv2d operator
    design.py         # Hardware design with configurable tiling
    reference.py      # PyTorch F.conv2d golden reference
    test.py           # Parametrized tests over all YOLOv8n shapes
  maxpool2d/
    op.py             # AIEMaxPool2d
    design.py
    reference.py
    test.py
  upsample/
    op.py             # AIEUpsample (nearest 2×)
    design.py
    reference.py
    test.py
  concat/
    op.py             # AIEConcat (channel dimension)
    design.py
    reference.py
    test.py

aie_kernels/
  aie2p/
    conv2dk1_bf16.cc  # 1×1 conv kernel (bf16)
    conv2dk3_bf16.cc  # 3×3 conv kernel (bf16)
    conv2dk1_i8.cc    # 1×1 conv kernel (int8)
    conv2dk3_i8.cc    # 3×3 conv kernel (int8)
    maxpool2d.cc      # MaxPool kernel
    upsample_nearest.cc  # Nearest-neighbor upsample

iron/applications/
  yolov8n/
    inference.py      # End-to-end inference pipeline
    model_prep.py     # Weight export & layout conversion
    postprocess.py    # NMS, box decoding
    test.py           # Accuracy validation
    configs/
      yolov8n.yaml    # Model configuration
    weights/
      yolov8n_fused.safetensors  # Fused BN weights
```

---

## 11. Testing Strategy

### 11.1 Unit Tests (Per Operator)

Each operator gets parametrized tests sweeping all YOLOv8n shapes:

```python
@pytest.mark.parametrize("c_in,c_out,h,w,k,s", [
    (3, 16, 640, 640, 3, 2),    # L0
    (16, 32, 320, 320, 3, 2),   # L1
    (32, 64, 160, 160, 3, 2),   # L3
    # ... all shapes from Phase 1.4 and 2.4 tables
])
def test_conv2d(c_in, c_out, h, w, k, s):
    op = AIEConv2d(c_in, c_out, k, s, h, w)
    input_data = torch.randn(1, c_in, h, w).to(torch.bfloat16)
    # ... run_test pattern
```

### 11.2 Integration Tests (Composite Modules)

```python
def test_bottleneck_block():
    """Conv3×3+SiLU → Conv3×3+SiLU → Add"""

def test_c2f_block():
    """Conv1×1 → chunk → Bottleneck(s) → concat → Conv1×1"""

def test_sppf_block():
    """Conv1×1 → MaxPool³ → Concat → Conv1×1"""

def test_detect_head_p3():
    """Regression + Classification branches at P3 scale"""
```

### 11.3 End-to-End Tests

```python
def test_yolov8n_backbone():
    """Full backbone: layers 0-9, compare all intermediate activations"""

def test_yolov8n_full():
    """Full model inference, compare output tensor [1, 84, 8400]"""

def test_yolov8n_coco_map():
    """Run on COCO val2017, verify mAP within tolerance of PyTorch baseline"""
```

### 11.4 Tolerance Ladder

| Test Level          | rel_tol | abs_tol | Rationale                    |
|---------------------|---------|---------|------------------------------|
| Single conv (bf16)  | 0.02    | 1e-4    | Minimal accumulation error   |
| Conv+SiLU fused     | 0.04    | 1e-3    | SiLU approximation adds error|
| Bottleneck block    | 0.05    | 0.01    | 2 convs + add               |
| C2f block           | 0.07    | 0.05    | Multiple bottlenecks         |
| Full backbone       | 0.10    | 0.1     | 10 layers of accumulation    |
| Full model (bf16)   | 0.15    | 0.5     | 22 layers + detect head      |
| Full model (int8)   | —       | —       | Validate via mAP, not tensor |

---

## 12. Performance Targets

### 12.1 Compute Analysis

YOLOv8n: 8.9 GFLOPs = 8.9 billion multiply-accumulate operations.

**NPU2 theoretical peak (bf16)**:
- 32 cores × 128 MACs/cycle × ~1.3 GHz ≈ 5.3 TMAC/s = 5,300 GMAC/s
- At 100% utilization: 8.9G / 5,300G = **1.7 μs** (unreachable theoretical minimum)

**NPU2 theoretical peak (int8)**:
- 32 cores × 512 MACs/cycle × ~1.3 GHz ≈ 21.3 TMAC/s
- At 100% utilization: 8.9G / 21,300G = **0.4 μs** (unreachable)

**Realistic targets** (accounting for memory bandwidth, DMA overhead, utilization):
- **Layer-by-layer bf16**: 5-15 ms (10-30% utilization, dominated by reconfig + DDR BW)
- **Fused bf16**: 2-5 ms (20-50% utilization)
- **Fused int8**: 1-3 ms (target for production)

### 12.2 Bandwidth Analysis

Total activation data moved per inference (layer-by-layer, bf16):
```
Sum of all layer input+output volumes ≈ 15 MB
DDR bandwidth (typical): ~30 GB/s
Minimum transfer time: 15 MB / 30 GB/s ≈ 0.5 ms
```

With skip connections (data read twice): ~20 MB total → ~0.7 ms minimum.

This means **DDR bandwidth is NOT the primary bottleneck** for YOLOv8n, even in
layer-by-layer mode. Reconfiguration overhead and compute utilization matter more.

### 12.3 Reconfiguration Analysis

```
22 layers × ~150 μs/reconfig = 3.3 ms reconfiguration overhead
With fusion to ~8 XCLBINs: 8 × 150 μs = 1.2 ms
```

**This is the key optimization lever.** Reducing XCLBIN count through layer fusion
can save 2+ ms, which may be larger than the compute time itself.

---

## 13. Milestone Summary

| Milestone | Deliverable | Timeline |
|-----------|-------------|----------|
| M0 | Infrastructure, model export, reference impl | Weeks 1-2 |
| M1 | Conv2d 1×1 operator, validated on all shapes | Weeks 3-5 |
| M2 | Conv2d 3×3 operator (s1 + s2), validated | Weeks 5-7 |
| M3 | MaxPool, Upsample, Concat operators | Weeks 7-8 |
| M4 | Composite blocks (Bottleneck, C2f, SPPF, Detect) | Weeks 8-11 |
| M5 | End-to-end YOLOv8n inference (layer-by-layer) | Weeks 11-13 |
| M6 | Layer fusion + INT8 + performance optimization | Weeks 13-17 |

---

## 14. Open Questions and Future Decisions

1. **BF16 vs INT8 first?** Plan starts with bf16 for easier debugging, but if
   performance requirements are strict, going INT8 from the start avoids rework.

2. **Which layers to fuse first?** Profiling in Phase 5 will reveal the bottleneck
   layers. Likely candidates: backbone downsample stages (L0-L2) and neck.

3. **Batch processing?** Running multiple images through the same XCLBIN amortizes
   reconfiguration cost. Need to decide batch size vs latency tradeoff.

4. **Pre/post-processing on NPU?** Image resize, letterboxing, NMS could
   potentially run on NPU cores, but the benefit is marginal for YOLOv8n.

5. **Partial reconfiguration granularity?** If the hardware supports column-level
   partial reconfig, we can overlap reconfig of unused columns with compute on
   active columns.

6. **Weight caching across frames?** If weights don't change between inferences
   (they don't), can we keep XCLBIN loaded and just swap activation buffers?
   This would eliminate reconfiguration overhead entirely for same-layer reruns.

---

## Appendix A: Complete C2f Channel Breakdown

| Layer | c_in | c_out | c (hidden) | n | cv1: in→out | Bottleneck convs | cv2: in→out | shortcut |
|-------|------|-------|------------|---|-------------|------------------|-------------|----------|
| 2     | 32   | 32    | 16         | 1 | 32→32       | 16→16, 16→16     | 48→32       | Yes      |
| 4     | 64   | 64    | 32         | 2 | 64→64       | 32→32 ×4         | 128→64      | Yes      |
| 6     | 128  | 128   | 64         | 2 | 128→128     | 64→64 ×4         | 256→128     | Yes      |
| 8     | 256  | 256   | 128        | 1 | 256→256     | 128→128, 128→128 | 384→256     | Yes      |
| 12    | 384  | 128   | 64         | 1 | 384→128     | 64→64, 64→64     | 192→128     | No       |
| 15    | 192  | 64    | 32         | 1 | 192→64      | 32→32, 32→32     | 96→64       | No       |
| 18    | 192  | 128   | 64         | 1 | 192→128     | 64→64, 64→64     | 192→128     | No       |
| 21    | 384  | 256   | 128        | 1 | 384→256     | 128→128, 128→128 | 384→256     | No       |

## Appendix B: All Unique Conv2d Invocations

Sorted by compute volume (FLOPs):

| # | c_in | c_out | k  | s | H_in | W_in | FLOPs (M) | Count |
|---|------|-------|----|---|------|------|-----------|-------|
| 1 | 3    | 16    | 3  | 2 | 640  | 640  | 4.4       | 1     |
| 2 | 16   | 32    | 3  | 2 | 320  | 320  | 47.2      | 1     |
| 3 | 32   | 64    | 3  | 2 | 160  | 160  | 75.5      | 1     |
| 4 | 64   | 128   | 3  | 2 | 80   | 80   | 75.5      | 1     |
| 5 | 128  | 256   | 3  | 2 | 40   | 40   | 75.5      | 1     |
| 6 | 64   | 64    | 3  | 2 | 80   | 80   | 37.7      | 1     |
| 7 | 128  | 128   | 3  | 2 | 40   | 40   | 37.7      | 1     |
| 8 | 32   | 32    | 1  | 1 | 160  | 160  | 26.2      | 1     |
| 9 | 64   | 64    | 1  | 1 | 80   | 80   | 26.2      | 1     |
| 10| 128  | 128   | 1  | 1 | 40   | 40   | 26.2      | 1     |
| 11| 256  | 256   | 1  | 1 | 20   | 20   | 26.2      | 1     |
| 12| 16   | 16    | 3  | 1 | 160  | 160  | 18.9      | 2     |
| 13| 32   | 32    | 3  | 1 | 80   | 80   | 18.9      | 4     |
| 14| 64   | 64    | 3  | 1 | 40   | 40   | 18.9      | 4     |
| 15| 128  | 128   | 3  | 1 | 20   | 20   | 18.9      | 2     |
| 16| 48   | 32    | 1  | 1 | 160  | 160  | 39.3      | 1     |
| 17| 128  | 64    | 1  | 1 | 80   | 80   | 52.4      | 1     |
| 18| 256  | 128   | 1  | 1 | 40   | 40   | 52.4      | 1     |
| 19| 384  | 256   | 1  | 1 | 20   | 20   | 39.3      | 2     |
| 20| 384  | 128   | 1  | 1 | 40   | 40   | 78.6      | 1     |
| 21| 192  | 64    | 1  | 1 | 80   | 80   | 78.6      | 1     |
| 22| 192  | 128   | 1  | 1 | 40   | 40   | 39.3      | 1     |
| 23| 96   | 64    | 1  | 1 | 80   | 80   | 39.3      | 1     |
| 24| 512  | 256   | 1  | 1 | 20   | 20   | 52.4      | 1     |
| 25| 256  | 128   | 1  | 1 | 20   | 20   | 13.1      | 1     |

## Appendix C: Reference Implementation Sources

- [Ultralytics YOLOv8 YAML](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/models/v8/yolov8.yaml)
- [YOLOv8 Documentation](https://docs.ultralytics.com/models/yolov8/)
- [MLIR-AIE Conv2d Examples](https://github.com/Xilinx/mlir-aie/tree/main/programming_examples/ml/conv2d)
- [MLIR-AIE ResNet Example](https://github.com/Xilinx/mlir-aie/tree/main/programming_examples/ml/resnet)
- [AIE2P Architecture Specification v1.4](internal)
- [IRON Framework](https://github.com/nod-ai/IRON)

## Appendix D: Session Progress Log

### Git History (branch: yolov8n, based on devel)
```
f5ecbc1 Conv2d: MemTile input buffering + weight streaming for YOLOv8n-scale configs
b76e786 YOLOv8n end-to-end NPU implementation: operators, pipeline, kernels, docs
```

### Files Created (40 files, ~12,000 lines)

**Operators:**
- `iron/operators/conv2d/{op,design,reference,test}.py` — Conv2d 1×1/3×3 with TAP decomposition, MemTile routing, fused bias+SiLU, weight streaming
- `iron/operators/maxpool2d/{op,design,reference,test}.py` — MaxPool2d k5 with strip-based design
- `iron/operators/upsample/{op,design,reference,test}.py` — Nearest 2× upsample

**AIE Kernels:**
- `aie_kernels/aie2p/conv2dk1_bf16.cc` — 1×1 conv scalar+vectorized, bias+SiLU fused variant
- `aie_kernels/aie2p/conv2dk3_bf16.cc` — 3×3 conv s1/s2 scalar+vectorized, bias+SiLU fused variants
- `aie_kernels/aie2p/maxpool2d_bf16.cc` — 5×5 max pooling
- `aie_kernels/aie2p/upsample2x_bf16.cc` — 2× nearest upsample

**YOLOv8n Application:**
- `iron/applications/yolov8n/blocks.py` — CBS, Bottleneck, C2f, SPPF with auto-column L1 budget
- `iron/applications/yolov8n/backbone.py` — Layers L0-L9
- `iron/applications/yolov8n/neck.py` — FPN up-path + PAN down-path (L10-L21)
- `iron/applications/yolov8n/detect.py` — Decoupled reg+cls head (6 branches)
- `iron/applications/yolov8n/pipeline.py` — Multi-PDI pipeline operator (~52 PDIs in one xclbin)
- `iron/applications/yolov8n/postprocess.py` — DFL decode + dist2bbox + NMS
- `iron/applications/yolov8n/model_prep.py` — BN fusion, weight export, tiled layout utils
- `iron/applications/yolov8n/test_*.py` — Tests for all components

**Documentation:**
- `iron/applications/yolov8n/README.md` — 620-line architecture guide
- `NPU_DATA_MOVEMENT_GUIDE.md` — 1106-line NPU data movement reference
- `iron/applications/yolov8n/benchmark_results.md` — 18-config operator benchmarks

**Infrastructure:**
- `iron/common/aie_base.py` — `register=True` kwarg for sub-operator creation
- `iron/common/compilation.py` — Minor fix

### Hardware Verification Summary

| Component | Tests | Status |
|-----------|-------|--------|
| Conv2d operator (all variants) | 50/50 | **PASS** on NPU |
| MaxPool2d operator | 15/15 | **PASS** on NPU |
| Upsample operator | 15/15 | **PASS** on NPU |
| CBS block (fused bias+SiLU) | 5/5 | **PASS** on NPU |
| Post-processing (DFL+NMS) | 110/110 | **PASS** (CPU) |
| Pipeline construction (256×256) | 5/5 | **PASS** |
| YOLOv8n-scale Conv2d (TAP fix) | 11/13 | **PASS** on NPU |
| YOLOv8n-scale Conv2d (MemTile) | 11/11 | **PASS** on NPU |
| Full 640×640 compile audit | 37/47 | Compile OK; 10 use weight streaming |
| **Layer-by-layer 640×640** | **IN PROGRESS** | Agent running L0→L1→...→L9 |

### Key Technical Achievements

1. **Multi-PDI xclbin chaining** — 52 unique operator configs merged into one xclbin via `--xclbin-input` + `--xclbin-kernel-id` (SwiGLU pattern)
2. **Fused bias+SiLU kernel** — Bias packed at end of weight buffer, Padé tanh approx (no expf on AIE), eliminates DDR round-trip per CBS block
3. **TAP 4D decomposition** — `_factorize_tensor()` handles DMA BD d3≤64, d0-d2≤1023, d0 even constraints
4. **MemTile input buffering** — `forward(placement=AnyMemTile)` for configs where input FIFO overflows L1
5. **MemTile weight streaming** — OC-subgroup chunks streamed from MemTile, core loops over chunks
6. **Auto-column L1 budget** — `_auto_columns()` checks full L1 (input+weight+output+stack) for all conv types

### Multi-PDI Verification Results

**Backbone L0-L9 multi-PDI**: PASS (20 PDIs, 1 context, 23.8s forward)
**Backbone+Neck L0-L21 multi-PDI**: PASS (29 PDIs, 1 context, 33.1s forward, 34.2s compile)

All 29 unique operator configs compiled into a single xclbin via `--xclbin-input` chaining.
Each PDI has a unique `--xclbin-kernel-id` (0x901-0x91D). Runtime uses 1 hw_context.
Forward pass feeds data sequentially through all layers via `_run_kernel()` per layer.

### Pickup Point — What's Left

#### 1. IC Streaming (in progress — `ic-streaming` agent task #6)
3 detect head configs need input-channel streaming to fit L1:
- `reg_p5 cv1` (256→64 k3s1 20×20): input FIFO 41KB + min weight 37KB > 64KB
- `cls_p3 cv2` (80→80 k3s1 80×80): input FIFO 51KB > 64KB alone
- `cls_p5 cv1` (256→80 k3s1 20×20): input FIFO 41KB + min weight 37KB > 64KB

**Implementation status:**
- `aie_kernels/aie2p/conv2dk3_bf16_icstream.cc` — accumulating kernel (DONE, 169 lines)
- `iron/operators/conv2d/design.py` — IC streaming path in `my_conv2d_k3` (DONE, 34 refs)
- `iron/operators/conv2d/op.py` — `_compute_ic_chunk()`, weight packing (DONE, 29 refs)
- `iron/applications/yolov8n/blocks.py` — `_auto_columns` IC streaming budget (DONE)
- Hardware verification: IN PROGRESS (aiecc compiling reg_p5 cv1)

**To resume:** Check if `ic-streaming` agent completed task #6. If not, run:
```bash
source ~/.bashrc; source ironenv/bin/activate && source /scratch/jmelber/mlir-aie/utils/env_setup.sh /scratch/jmelber/mlir-aie /opt/xrt
python3 -c "
import torch; from iron.common import AIEContext; from iron.applications.yolov8n.blocks import CBS
for ic,oc,h,w in [(256,64,20,20),(80,80,80,80),(256,80,20,20)]:
    ctx=AIEContext(); cbs=CBS(ic,oc,3,1,h,w,context=ctx); ctx.compile_all()
    cbs.load_weights(torch.randn(oc,ic,3,3,dtype=torch.bfloat16)*0.01,torch.randn(oc,dtype=torch.bfloat16)*0.01)
    ctx.prepare_runtime(); out=cbs.forward(torch.randn(1,ic,h,w,dtype=torch.bfloat16))
    print(f'{ic}->{oc} {h}x{w}: {out.shape} finite={torch.isfinite(out).all()}')
"
```

#### 2. Detect Head Multi-PDI (after IC streaming)
Once IC streaming works, add detect head layers to the multi-PDI pipeline:
- 6 DetectBranch instances (reg×3 + cls×3)
- Each has 3 convs: CBS(k3)+CBS(k3)+Conv(k1)
- ~18 additional PDIs (many shared with backbone/neck)
- Extend the `FullPipe` class with detect layers

#### 3. Full Model End-to-End
Chain L0-L21 + detect head + postprocess:
```python
det_p3, det_p4, det_p5 = pipe.forward(image)
postproc = YOLOv8nPostProcess()
detections = postproc(
    [det_reg_p3, det_reg_p4, det_reg_p5],
    [det_cls_p3, det_cls_p4, det_cls_p5]
)
```

#### 4. Real Weights (optional, after e2e works)
Load pretrained YOLOv8n weights via `model_prep.py`:
```python
from iron.applications.yolov8n.model_prep import export_yolov8n_weights
weights = export_yolov8n_weights()  # requires: pip install ultralytics
```

### Git Log (branch: yolov8n)
```
eaff4cb Fix k1 weight streaming in _compute_oc_chunk, verify L0-L21 multi-PDI
1f02c54 Multi-PDI backbone verified on NPU: 20 PDIs, 1 hw_context, 640x640
73b9ec5 LAYER_CONFIGS.md: add comprehensive bug fixes section
9e90630 Add LAYER_CONFIGS.md: complete YOLOv8n operator reference
db7c759 Update plan: backbone+neck 100% NPU verified at 640x640
9f41927 Fix SPPF auto-columns default (was 1, now 0)
d7132ff Default to auto-columns, add CPU fallback for infeasible configs
35bda75 Fix BD factorization for unfactorizable weight sizes (L8 bottleneck)
04eba65 Fix multi-column k3 linker bug: add --no-unified to aiecc
0f33753 Update YOLOV8N_NPU2_PLAN.md with comprehensive session progress log
f5ecbc1 Conv2d: MemTile input buffering + weight streaming for YOLOv8n-scale configs
b76e786 YOLOv8n end-to-end NPU implementation: operators, pipeline, kernels, docs
```
