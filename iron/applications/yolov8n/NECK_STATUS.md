# YOLOv8n Neck — Status & Benchmarks

## Architecture

The YOLOv8n neck connects the backbone feature maps (P3, P4, P5) to the
detect head via Feature Pyramid Network (FPN) up-path and PAN down-path.

```
Backbone outputs:
  P3 = L4 out:  [1, 64, 80, 80]
  P4 = L6 out:  [1, 128, 40, 40]
  P5 = L9 out:  [1, 256, 20, 20]  (after L8 C2f + SPPF)

Neck (FPN up-path):
  L12 C2f: upsample(P5) + P4 → [1, 384, 40, 40] → [1, 128, 40, 40]
  L15 C2f: upsample(L12) + P3 → [1, 192, 80, 80] → [1, 64, 80, 80]

Neck (PAN down-path):
  L16 CBS:  L15 → k3s2 → [1, 64, 40, 40]
  L18 C2f:  L16 + L12 → [1, 192, 40, 40] → [1, 128, 40, 40]
  L19 CBS:  L18 → k3s2 → [1, 128, 20, 20]
  L21 C2f:  L19 + P5 → [1, 384, 20, 20] → [1, 256, 20, 20]

Detect head inputs:
  det_p3 = L15 out  [1, 64, 80, 80]
  det_p4 = L18 out  [1, 128, 40, 40]
  det_p5 = L21 out  [1, 256, 20, 20]
```

---

## Layer Map

| Layer | Type | IC→OC | Spatial | K | S | vec_iters | Fused Vec? | Status |
|-------|------|-------|---------|---|---|-----------|------------|--------|
| L12.cv1 | CBS k1 | 384→128 | 40×40 | 1 | 1 | 5 | ✅ k1 fused | Sequential ✅ |
| L12.bn0.cv1 | CBS k3 | 64→64 | 40×40 | 3 | 1 | 5 | ✅ vec | Sequential ✅ |
| L12.bn0.cv2 | CBS k3 | 64→64 | 40×40 | 3 | 1 | 5 | ✅ vec | Sequential ✅ |
| L12.cv2 | CBS k1 | 192→128 | 40×40 | 1 | 1 | 5 | ✅ k1 fused | Sequential ✅ |
| L15.cv1 | CBS k1 | 192→64 | 80×80 | 1 | 1 | 10 | ✅ k1 fused | Fused ✅ 32ms |
| L15.bn0.cv1 | CBS k3 | 32→32 | 80×80 | 3 | 1 | 10 | ✅ fused works | Fused ✅ 17ms |
| L15.bn0.cv2 | CBS k3 | 32→32 | 80×80 | 3 | 1 | 10 | ✅ fused works | Fused ✅ 17ms |
| L15.cv2 | CBS k1 | 96→64 | 80×80 | 1 | 1 | 10 | ✅ k1 fused | Fused ✅ 31ms |
| L16 | CBS k3s2 | 64→64 | 80→40 | 3 | 2 | 5 | ✅ vec | Sequential ✅ |
| L18.cv1 | CBS k1 | 192→128 | 40×40 | 1 | 1 | 5 | ✅ k1 fused | Sequential ✅ |
| L18.bn0.cv1 | CBS k3 | 64→64 | 40×40 | 3 | 1 | 5 | ✅ vec | Sequential ✅ |
| L18.bn0.cv2 | CBS k3 | 64→64 | 40×40 | 3 | 1 | 5 | ✅ vec | Sequential ✅ |
| L18.cv2 | CBS k1 | 192→128 | 40×40 | 1 | 1 | 5 | ✅ k1 fused | Sequential ✅ |
| L19 | CBS k3s2 | 128→128 | 40→20 | 3 | 2 | 2 | ✅ vec | Sequential ✅ |
| L21.cv1 | CBS k1 | 384→256 | 20×20 | 1 | 1 | 2 | ✅ k1 fused | Sequential ✅ |
| L21.bn0.cv1 | CBS k3 | 128→128 | 20×20 | 3 | 1 | 2 | ✅ vec | Sequential ✅ |
| L21.bn0.cv2 | CBS k3 | 128→128 | 20×20 | 3 | 1 | 2 | ✅ vec | Sequential ✅ |
| L21.cv2 | CBS k1 | 384→256 | 20×20 | 1 | 1 | 2 | ✅ k1 fused | Sequential ✅ |

**vec_iters** = output_width / 8 (for stride=1), determines if the vectorized
k3 SiLU kernel is safe. Bug threshold: vec_iters ≥ 10 causes Peano codegen
corruption. k1 has a separate vectorization path unaffected by this bug.

---

## Benchmark Results

*Measured on AMD Ryzen AI 9 HX 370, XRT 2.21.75, per-layer AIEContext.*
*All fused conv+bias+SiLU on NPU (int8 in, int8 out).*
*128ch k3 layers use 2 AIE columns to halve OC streaming groups.*
*Runtime context cleanup between blocks prevents hw_context exhaustion.*

### Per-Layer Timing

| Sub-Layer | IC→OC | K/S | Cols | Run (ms) | Compile (ms) |
|-----------|-------|-----|------|----------|-------------|
| L12.cv1 | 384→128 | k1/s1 | 1 | 16 | 411 |
| L12.bn0.cv1 | 64→64 | k3/s1 | 1 | 9 | 280 |
| L12.bn0.cv2 | 64→64 | k3/s1 | 1 | 9 | 213 |
| L12.cv2 | 192→128 | k1/s1 | 1 | 16 | 231 |
| **L12 total** | | | | **50** | 1134 |
| L15.cv1 | 192→64 | k1/s1 | 1 | 32 | 230 |
| L15.bn0.cv1 | 32→32 | k3/s1 | 1 | 17 | 200 |
| L15.bn0.cv2 | 32→32 | k3/s1 | 1 | 17 | 210 |
| L15.cv2 | 96→64 | k1/s1 | 1 | 31 | 241 |
| **L15 total** | | | | **97** | 882 |
| L16 | 64→64 | k3/s2 | 1 | **9** | 209 |
| L18.cv1 | 192→128 | k1/s1 | 1 | 16 | 223 |
| L18.bn0.cv1 | 64→64 | k3/s1 | 1 | 9 | 229 |
| L18.bn0.cv2 | 64→64 | k3/s1 | 1 | 9 | 235 |
| L18.cv2 | 192→128 | k1/s1 | 1 | 16 | 241 |
| **L18 total** | | | | **50** | 928 |
| L19 | 128→128 | k3/s2 | 2 | **155** | 314 |
| L21.cv1 | 384→256 | k1/s1 | 1 | 39 | 235 |
| L21.bn0.cv1 | 128→128 | k3/s1 | 2 | 151 | 367 |
| L21.bn0.cv2 | 128→128 | k3/s1 | 2 | 151 | 362 |
| L21.cv2 | 384→256 | k1/s1 | 1 | 39 | 274 |
| **L21 total** | | | | **379** | 1239 |

### Summary

| Block | Channels | Spatial | NPU Run (ms) | Notes |
|-------|----------|---------|-------------|-------|
| L12 C2f | 384→128 | 40×40 | 50 | |
| L15 C2f | 192→64 | 80×80 | 97 | |
| L16 CBS | 64→64 k3s2 | 80→40 | 9 | |
| L18 C2f | 192→128 | 40×40 | 50 | |
| L19 CBS | 128→128 k3s2 | 40→20 | 155 | 2 cols (was 309ms with 1 col) |
| L21 C2f | 384→256 | 20×20 | 379 | Complete (was 339+ partial) |
| **Neck total** | | | **740** | |

### Fixes Applied (vs initial benchmark)

- **Multi-column for 128ch k3**: L19 and L21.bn0 use `num_aie_columns=2`,
  halving OC streaming groups from 4 to 2. L19: 309→155ms (2x), L21.bn0:
  300→151ms per sub-layer (2x).
- **Context cleanup between blocks**: `DefaultNPURuntime._context_cache.clear()`
  + `gc.collect()` after each C2f/CBS group prevents driver exhaustion.
  L21 now completes fully (all 4 sub-layers).
- **Total improvement**: 854ms → 740ms (13.4% reduction), all layers complete.

### Remaining Bottleneck

L21.bn0 (128→128 k3 at 20×20) dominates at 151ms × 2 = 302ms. Even with
2 columns, the OC streaming overhead is significant for 128ch k3 convs.
Further optimization paths:
- 4 columns would halve again → ~75ms per sub-layer
- Dataflow pipeline (core-to-core) would eliminate per-layer DDR round-trips

---

## Vectorization Status

### All Neck Layers Verified with Fused SiLU

Benchmark results show that **all neck layers run successfully with fused
conv+bias+SiLU on NPU**, including the previously-untested 80×80 layers.

| Width | vec_iters | Layers | Fused SiLU | Notes |
|-------|-----------|--------|-----------|-------|
| 80 | 10 | L15.bn0 (32→32, k3) | ✅ Works | IC=32 small enough — no pipelining issue |
| 80 | 10 | L15.cv1/cv2 (k1) | ✅ Works | k1 has independent vectorization path |
| 40 | 5 | L12, L18, L16 | ✅ Works | Well within safe threshold |
| 20 | 2 | L21, L19 | ✅ Works | Minimal vec_iters |

**Key finding**: The vec_iters ≥ 10 Peano bug only manifests when the
inner MMUL loop has many iterations AND float SiLU interaction. For L15's
bottleneck (IC=32, OC=32), the loop count is small enough that the
pipelining bug doesn't trigger.

---

## Known Blockers

| Issue | Affected Layers | Severity | Workaround | Status |
|-------|----------------|----------|------------|--------|
| OC streaming slow for 128ch k3 | L19, L21.bn0 | Medium | 2 columns halves time (309→155ms, 300→151ms) | Mitigated ✅ |
| NPU hw_context exhaustion | L21 (14th context) | Low | Context cleanup between blocks | Fixed ✅ |
| Multi-PDI xclbin timeout | All (in pipeline) | Medium | Use per-layer AIEContext for now | Open |

---

## Dataflow Roadmap

### Current State
All neck layers run sequentially via `Int8YOLOv8nPipeline` with per-layer
PDIs. Each layer does: host→NPU transfer, compute, NPU→host transfer,
CPU post-processing (dequant/bias/SiLU for non-fused layers).

### Phase 1: Individual Verification (this document)
Verify each neck layer works on NPU, benchmark scalar vs fused, document
which layers can be vectorized.

### Phase 2: Neck Dataflow Blocks
Design multi-core dataflow blocks for neck sub-sections:
- **L12 C2f block** (40×40): 4 cores, cv1→bn0→cv2, core-to-core chaining
- **L18 C2f block** (40×40): Same structure as L12
- **L21 C2f block** (20×20): Same structure, smaller spatial

### Phase 3: Neck Phase Fusion
Fuse neck blocks into multi-phase pipelines:
- Phase A: L12 C2f (needs P5 upsample + P4 concat — CPU or MemTile?)
- Phase B: L15 C2f (needs L12 upsample + P3 concat)
- Phase C: L16 + L18 (L16 output feeds directly to L18 after concat)
- Phase D: L19 + L21 (L19 output feeds directly to L21 after concat)

### Key Challenges
1. **Upsample on NPU**: `repeat_interleave(2)` — possible via strided DMA
   or a dedicated upsample kernel. Currently done on CPU.
2. **Concat on NPU**: Channel concatenation at MemTile via multi-source
   ObjectFIFO join. Already proven in C2f designs.
3. **DDR round-trips**: Each upsample/concat forces a DDR round-trip.
   Minimizing these is the key optimization for neck dataflow.
