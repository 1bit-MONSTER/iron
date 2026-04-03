# YOLOv8n NPU Dataflow Pipeline — Status & Plan

## Executive Summary

Building YOLOv8n object detection on AMD Ryzen AI NPU using dataflow execution.
Target: 60 FPS (16.7ms per frame). Current best: Phase 1 backbone at 10.8s (640×640).

The pipeline is being built layer-by-layer with hardware verification after each addition.

---

## 1. Kernel Inventory

### Fused Conv + SiLU Kernels (on-chip activation, no Python overhead)

| Kernel | File | Vectorized | Width Limit | SiLU Method |
|--------|------|-----------|-------------|-------------|
| `conv2dk3_i8_silu` (s1) | `conv2dk3_i8_silu.cc` | Yes (top/mid/bot) | ≤96 | Vec-16 `aie::tanh<bfloat16>()` via two-pass |
| `conv2dk3s2_i8_silu` (s2) | `conv2dk3_i8_silu.cc` | Yes | ≤96 | Vec-16 `aie::tanh<bfloat16>()` via two-pass |
| `conv2dk1_i8_silu` | `conv2dk1_i8_silu.cc` | Yes | Any (width%8==0) | Vec-16 `aie::tanh<bfloat16>()` |
| Scalar fallback (all) | Same files | No | Any | Padé rational tanh |

**Key constraints:**
- `aie::tanh<bfloat16>()` requires vector size ≥ 16 (size 8 = garbage)
- `to_vector<int32>(0)` has wrong element ordering on AIE2p — ONLY `to_vector<int8>(shift)` via SRS is correct
- Three separate functions (top/mid/bot) eliminate runtime `check` that causes Peano codegen corruption
- Width ≤96 threshold due to MMUL software pipelining bug at larger vec_iters

### Non-Fused Conv Kernels (fast, exact)

| Kernel | File | Status |
|--------|------|--------|
| `conv2dk3_i8` (s1) | `conv2dk3_i8.cc` | Vectorized MMUL, all sizes |
| `conv2dk3s2_i8` (s2) | `conv2dk3_i8.cc` | Vectorized MMUL, all sizes |
| `conv2dk1_i8` | `conv2dk1_i8.cc` | Vectorized MMUL, all sizes |

### Utility Kernels

| Kernel | File | Purpose |
|--------|------|---------|
| `add_i8` | `add_i8.cc` | Saturating int8 add (residual connections) |
| `bias_silu_i8` | `bias_silu_i8.cc` | Standalone bias+SiLU (split-TU approach) |
| `passthrough_i8` | `passthrough_i8.cc` | Data routing (split→join bridge) |
| `conv2dk3_i8_silu_fwd` | `conv2dk3_i8_silu_fwd.cc` | K3 SiLU + passthrough (combined .o for MLIR) |

---

## 2. Dataflow Designs — What's Built & Verified

### Building Blocks (all hardware-verified, 100% exact match)

| Design | Layers | Cores | Fused SiLU | Max Size Tested |
|--------|--------|-------|------------|-----------------|
| `my_dataflow_l0` | L0 alone | 1 | No | 640×640 ✅ |
| `my_dataflow_l0_l1` | L0→L1 chain | 2 | No | 640×640 ✅ (1.37x speedup) |
| `my_dataflow_l0_l1_l2cv1` | L0→L1→L2.cv1 | 3 | No | 640×640 ✅ (3.5ms) |
| `my_dataflow_conv_silu` | Conv→SiLU 2-core | 2 | Split SiLU | 32×32 ✅ |
| `my_dataflow_spine_fused` | L0→L1→L3→L5 | 4 | Yes | 640×640 ✅ |
| `my_dataflow_spine_5layer` | L0→L1→L3→L5→L7 | 5 | Yes + OC streaming | 64×64 ✅ (YOLO channels) |
| `my_dataflow_c2f_l2_simple` | C2f L2 (32ch split) | 4 | No | 32×32 ✅ |
| `my_dataflow_c2f_l2_full` | C2f L2 (48ch concat) | 5 | Yes | 160×160 ✅ |
| `my_dataflow_fused_oc_streaming` | Single layer OC stream | 1 | Yes | 80×80 ✅ |
| `my_dataflow_c2f_l4` | C2f L4 (n=2, 128ch) | 8 | No | 80×80 ✅ |
| `my_dataflow_c2f_l6` | C2f L6 (n=2, 128ch) | 8 | No | 40×40 ✅ |
| `my_dataflow_backbone_phase1` | L0→L1→L2→L3 | 8 | Mixed | 640×640 ✅ (10.8s) |

### Multi-Phase Chained Tests

| Test | Phases | Layers | Status |
|------|--------|--------|--------|
| `test_dataflow_backbone_p1_p2` | P1→P2 | L0→L3 + C2f L4 | 64×64 ✅ |
| `test_dataflow_backbone_p1_through_p5` | P1→P5 | L0→L7 (full backbone) | 64×64 (new) |

### Key Techniques Proven

| Technique | Status | Where Used |
|-----------|--------|------------|
| Core-to-core ObjectFIFO | ✅ Working | All multi-core chains |
| MemTile weight split | ✅ Working | Spine, C2f blocks |
| Channel split at MemTile | ✅ Working | C2f cv1→halves |
| Channel join at MemTile | ✅ Working | C2f concat→cv2 |
| 48ch concat [h1\|h2\|bn0] | ✅ Working | C2f L2 full |
| Neighboring tile (no DMA) | ✅ Working | C2f bn inter |
| OC streaming (weight chunks) | ✅ Working | L5 (64→128), L7 (128→256) |
| Stride-0 DMA repeat | ✅ Working | Input re-streaming for OC groups |
| Strided output drain | ✅ Working | OC chunk interleaving |
| Residual add (int8) | ✅ Working | C2f bottleneck skip |
| Phase-based execution | ✅ Working | Backbone Phase 1 |
| Multi-phase DDR chaining | ✅ Working | P1→P2, P1→P5 |

---

## 3. YOLOv8n Backbone Layer Map

```
Layer   Type     IC→OC   Spatial    Kernel          Dataflow Status
─────   ────     ─────   ───────    ──────          ───────────────
L0      CBS k3s2  8→16   640→320   conv2dk3s2_silu  Phase 1 ✅ (scalar SiLU, width>96)
L1      CBS k3s2 16→32   320→160   conv2dk3s2_silu  Phase 1 ✅ (scalar SiLU, width>96)
L2.cv1  CBS k1   32→32   160×160   conv2dk1_silu    Phase 1 ✅ (vectorized)
L2.bn0.cv1 CBS k3 16→16  160×160   conv2dk3_silu    Phase 1 ✅ (scalar, width>96)
L2.bn0.cv2 CBS k3 16→16  160×160   conv2dk3_silu    Phase 1 ✅ (scalar, width>96)
L2.cv2  CBS k1   48→32   160×160   conv2dk1_silu    Phase 1 ✅ (vectorized)
L3      CBS k3s2 32→64   160→80    conv2dk3s2_silu  Phase 1 ✅ (vectorized, w=80≤96)
─── Phase 1 complete: 8 cores, 2 columns, 10.8s at 640×640 ───

L4.cv1  CBS k1   64→64   80×80     conv2dk1         Phase 2 ✅ (my_dataflow_c2f_l4)
L4.bn0  Bottleneck 32ch  80×80     conv2dk3+add     Phase 2 ✅
L4.bn1  Bottleneck 32ch  80×80     conv2dk3+add     Phase 2 ✅
L4.cv2  CBS k1  128→64   80×80     conv2dk1         Phase 2 ✅
─── Phase 2: L4 C2f n=2, 7 cores, 2 columns ───

L5      CBS k3s2 64→128  80→40     conv2dk3s2_silu  Phase 3 ✅ (OC streaming, oc_chunk=32)
─── Phase 3: L5 downsample, 1 core, OC streaming ───

L6.cv1  CBS k1  128→128  40×40     conv2dk1         Phase 4 ✅ (my_dataflow_c2f_l6)
L6.bn0  Bottleneck 64ch  40×40     conv2dk3+add     Phase 4 ✅
L6.bn1  Bottleneck 64ch  40×40     conv2dk3+add     Phase 4 ✅
L6.cv2  CBS k1  256→128  40×40     conv2dk1         Phase 4 ✅
─── Phase 4: L6 C2f n=2, 8 cores, 2 columns ───

L7      CBS k3s2 128→256 40→20     conv2dk3s2_silu  Phase 5 ✅ (OC streaming, oc_chunk=32)
─── Phase 5: L7 downsample, 1 core, OC streaming ───

L8.cv1  CBS k1  256→256  20×20     conv2dk1         Phase 6 TODO
L8.bn0  Bottleneck 128ch 20×20     conv2dk3+add     Phase 6 TODO
L8.cv2  CBS k1  384→256  20×20     conv2dk1         Phase 6 TODO
L9.cv1  CBS k1  256→128  20×20     conv2dk1         Phase 6 TODO
L9.cv2  CBS k1  512→256  20×20     conv2dk1         Phase 6 TODO
─── Phase 6: L8 C2f + SPPF (future) ───

NECK (all verified with fused SiLU, per-layer NPU context):
L12.cv1 CBS k1  384→128  40×40     conv2dk1_silu    Fused ✅ 16ms (1 col)
L12.bn0 Bottleneck 64ch  40×40     conv2dk3_silu    Fused ✅ 18ms (1 col)
L12.cv2 CBS k1  192→128  40×40     conv2dk1_silu    Fused ✅ 16ms (1 col)
L15.cv1 CBS k1  192→64   80×80     conv2dk1_silu    Fused ✅ 32ms (1 col)
L15.bn0 Bottleneck 32ch  80×80     conv2dk3_silu    Fused ✅ 34ms (1 col)
L15.cv2 CBS k1   96→64   80×80     conv2dk1_silu    Fused ✅ 31ms (1 col)
L16     CBS k3s2 64→64   80→40     conv2dk3s2_silu  Fused ✅ 9ms  (1 col)
L18.cv1 CBS k1  192→128  40×40     conv2dk1_silu    Fused ✅ 16ms (1 col)
L18.bn0 Bottleneck 64ch  40×40     conv2dk3_silu    Fused ✅ 18ms (1 col)
L18.cv2 CBS k1  192→128  40×40     conv2dk1_silu    Fused ✅ 16ms (1 col)
L19     CBS k3s2 128→128 40→20     conv2dk3s2_silu  Fused ✅ 155ms (2 col)
L21.cv1 CBS k1  384→256  20×20     conv2dk1_silu    Fused ✅ 39ms (1 col)
L21.bn0 Bottleneck 128ch 20×20     conv2dk3_silu    Fused ✅ 302ms (2 col, 151ms×2)
L21.cv2 CBS k1  384→256  20×20     conv2dk1_silu    Fused ✅ 39ms (1 col)
─── Neck: all layers verified, 740ms total (was 854ms) ───
```

### SiLU Vectorization Coverage

| Width | Vectorized? | Layers at this width |
|-------|------------|---------------------|
| 640 | ❌ Scalar (>96) | L0 input |
| 320 | ❌ Scalar (>96) | L0→L1 |
| 160 | ❌ Scalar (>96) | L1→L2, L2 internal, L3 input |
| 80 | ✅ Vectorized (≤96) | L3→L4, L4 internal, L5 input |
| 40 | ✅ Vectorized (≤96) | L5→L6, L6 internal, L7 input |
| 20 | ✅ Vectorized (≤96) | L7→L8, L8 internal, L9 |

**Bottleneck**: L0/L1/L2/L3 at widths 160-640 use scalar SiLU (~4s per layer).
Extending the vec threshold to width≤320 would make L1/L2/L3 vectorized.

---

## 4. Performance

| Configuration | Forward Time | Per-Layer Avg | Notes |
|--------------|-------------|---------------|-------|
| Non-fused sequential (63 PDIs) | 14.7s | ~230ms | Python SiLU = 10s overhead |
| Fused sequential (scalar SiLU) | 101s | 1607ms | Scalar Padé too slow |
| Fused sequential (vec k3 enabled) | 16.4s | 260ms | L0/L1 still scalar |
| Phase 1 dataflow (L0→L1→L2→L3) | 10.8s | — | 8 cores, core-to-core |
| L0→L1 dataflow (non-fused) | 5.76s | — | 1.37x vs sequential |

### What dominates the 10.8s Phase 1 time

- L0 (8→16, 640→320): ~4.3s (scalar SiLU on 1.6M output elements)
- L1 (16→32, 320→160): ~3.5s (scalar SiLU on 819K output elements)
- L2 C2f (160×160): ~2s (scalar SiLU on internal k3 layers)
- L3 (32→64, 160→80): ~0.5s (vectorized SiLU at width=80)

**If L0/L1/L2 were vectorized**: Phase 1 could drop to ~1-2s.

---

## 5. Next Steps (Priority Order)

### Immediate (agents working now)

| Task | Agent | Status |
|------|-------|--------|
| Extend vec threshold to width≤320 | kernel-vectorizer | In progress |
| Wire Phase 1→5 backbone test | backbone-designer | ✅ Done |
| L6 C2f design (128ch, n=2) | c2f-expert | ✅ Done |

### Short-term (this week)

1. ~~**Wire Phase 1→2→3→4→5** with DDR scratch buffers~~ ✅ Done
2. **L8 C2f + L9 SPPF** designs (Phase 6)
3. **End-to-end backbone test** with real YOLOv8n weights
4. **Neck + detect head** (upsample, concat, 6 detect branches)

### Medium-term (60 FPS path)

1. **Vectorize all widths** — push threshold to 640 or use chunk-based processing
2. **Reduce phase boundaries** — merge adjacent phases to eliminate DDR round-trips
3. **Multi-column parallelism** — use all 8 columns for pipeline stages
4. **Weight pre-loading** — static weight buffers, zero per-frame overhead
5. **Runlist chains** — batch all phases in one NPU submission

### Architecture target

```
Single PDI (all 8 columns):
  Col 0-1: L0→L1 (core-to-core, fused SiLU)
  Col 2-3: L2 C2f (split/join at MemTile)
  Col 4:   L3 downsample
  Col 5-6: L4 C2f (2 bottlenecks)
  Col 7:   L5 downsample (OC streaming)

  → DDR handoff →

  Second PDI:
  Col 0-1: L6 C2f
  Col 2:   L7 downsample (OC streaming)
  Col 3-4: L8 C2f
  Col 5-6: L9 SPPF
  Col 7:   Neck start
```

---

## 6. Known Issues & Workarounds

| Issue | Root Cause | Workaround |
|-------|-----------|------------|
| `to_vector<int32>(0)` wrong ordering | Raw bitcast, no SRS depermutation | Use `to_vector<int8>(shift)` only |
| `aie::tanh<bf16>()` vec size 8 = garbage | HW intrinsic needs ≥16 | Always use vec-16 |
| Peano codegen with runtime `check` | Auto-pipelining corrupts MMUL | Three separate functions (top/mid/bot) |
| MMUL + float SiLU register overlap | Peano -O2 register allocation | Two-pass: MMUL loop → SiLU loop |
| Vec k3 SiLU width>96 fails | Second MMUL pipelining bug | Width threshold, scalar fallback |
| ObjectFifo single-link constraint | One split/forward per FIFO | Passthrough kernel as bridge |
| MemTile 6 DMA output limit | Hardware limit | Distribute across MemTiles |
| L1 64KB limit for large weights | L5: 74KB, L7: 296KB | OC streaming (chunk weights) |

---

## 7. File Inventory

```
aie_kernels/aie2p/
  conv2dk3_i8_silu.cc          # Fused k3 SiLU (3-fn vec + scalar)
  conv2dk3_i8_silu_fwd.cc      # K3 SiLU + passthrough combined
  conv2dk1_i8_silu.cc          # Fused k1 SiLU (vec-16)
  bias_silu_i8.cc              # Standalone bias+SiLU (split-TU)
  add_i8.cc                    # Saturating int8 add
  elem_add_i8.cc               # Element-wise int8 add
  passthrough_i8.cc            # Identity kernel for routing

iron/operators/conv2d_int8/
  dataflow_design.py           # 16 dataflow design functions (~6000 lines)
  test_dataflow.py             # 16 test functions (~5000 lines)
  design.py                    # Sequential single-layer designs
  op.py                        # AIEConv2dInt8 operator class
  reference.py                 # CPU reference implementations

iron/applications/yolov8n/
  pipeline_int8.py             # Sequential 63-PDI pipeline
  run_pretrained_int8.py       # End-to-end inference script

Skill guides (in ~/.claude/):
  AIE_KERNEL_OPTIMIZATION.md   # 1449 lines, AIE API + bugs
  NPU_DATAFLOW_GUIDE.md        # 960 lines, dataflow patterns
```
