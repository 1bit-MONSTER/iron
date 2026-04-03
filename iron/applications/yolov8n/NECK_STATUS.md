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

---

## Dataflow Pipeline Results

*All designs hardware-verified with exact or near-exact match vs CPU reference.*

### Final Pipeline: 3 PDIs, 657ms

| PDI | Layers | Design | Workers | Cols | TGs | Runtime |
|-----|--------|--------|---------|------|-----|---------|
| 1 | L12 + upsample + L15 | `my_dataflow_l12_l15` | 9 | 4 | 7 | 113ms |
| 2 | L16 + L18 | `my_dataflow_l16_l18` | 5 | 2 | 4 | 46ms |
| 3 | L19 + L21 (2-col) | `my_dataflow_l19_l21_2col` | 8 | 4 | 5 | 498ms |
| **Total** | | | **22** | | **16** | **657ms** |

### Progression

| Stage | PDIs | Runtime | Notes |
|-------|------|---------|-------|
| Layer-by-layer sequential | 18 | 740ms | Baseline per-layer AIEContext |
| Per-block dataflow | 6 | 1110ms | C2f blocks fused, but L21 slow (single-core OC) |
| Combined blocks | 4 | 1110ms | L16+L18 and L19+L21 paired |
| Combined + upsample on NPU | 3 | 1110ms | L12+L15 fused via NPU upsample |
| 2-column k3 parallelism | 3 | **657ms** | L19+L21 k3 layers use 2-col OC streaming |

### Key Techniques Used

| Technique | Where | Effect |
|-----------|-------|--------|
| C2f dataflow (cv1→bn0→cv2 in 1 PDI) | L12, L15, L18 | 3 DDR round-trips eliminated per block |
| OC streaming (weight chunking) | L12.cv1, L19, L21 (all layers) | Large weights fit in 64KB L1 |
| 2-column OC parallelism | L19, L21.bn0 k3 layers | 2× speedup (951→498ms) |
| NPU upsample kernel | L12→L15 boundary | CPU upsample eliminated |
| DDR concat via strided DMA | All C2f blocks | Channel split/join without MemTile |
| Skip connection pre-fill | L12→L18, P5→L21, P3→L15 | Host loads skip data into O buffer |
| Kernel symbol rename (-D) | cv2, L15 kernels | Multiple k1/k3 variants in one PDI |

### Designs Built

| Design Function | File | Lines | Verified |
|----------------|------|-------|----------|
| `my_dataflow_c2f_neck` | `dataflow_design.py` | ~300 | L12(40×40), L15(80×80), L18(40×40) ✅ |
| `my_dataflow_c2f_l21` | `dataflow_design.py` | ~250 | L21(20×20) ✅ |
| `my_dataflow_l16_l18` | `dataflow_design.py` | ~250 | 80×80 ✅ |
| `my_dataflow_l19_l21_2col` | `dataflow_design.py` | ~250 | 40×40 ✅ |
| `my_dataflow_l12_l15` | `dataflow_design.py` | ~300 | 40×40 ✅ |
| `my_dataflow_upsample2x` | `dataflow_design.py` | ~60 | 40×40→80×80 ✅ |

---

## Further Optimization Opportunities

### High Impact

1. **4-column k3 parallelism for L21.bn0** (~150ms → ~75ms each, saves ~150ms)
   - L21.bn0.cv1 and bn0.cv2 currently use 2-col with n_oc_per_col=2
   - 4-col would give n_oc_per_col=1 (no OC loop) — pure streaming
   - Requires FIFO sharing via MemTile broadcast to stay within shim limits

2. **MemTile weight pre-loading** (saves ~5-10ms per PDI)
   - Static weight buffers loaded once, reused across frames
   - Eliminates per-frame weight DMA for repeated inference

3. **Runlist chaining** (saves 3 PDI submission overheads)
   - Batch all 3 neck PDIs into a single runlist submission
   - Reduces host-NPU round-trip latency

### Medium Impact

4. **Core-to-core chaining within L21** (saves DDR round-trips)
   - Currently L21 uses 4 serial task groups (each layer through DDR)
   - cv1→bn0.cv1 could stream if bn0 didn't need OC streaming
   - Would need weight streaming via MemTile to avoid OC re-read

5. **Pipeline L16 output directly into L18.cv1** (saves 1 DDR trip)
   - Currently L16 drains to DDR concat, L18 reads it back
   - Could stream L16→L18.cv1 core-to-core if concat is done at MemTile

### Low Impact (diminishing returns)

6. **2-column for L21.cv1/cv2** (saves ~20ms each = ~40ms)
   - Currently single-core at 39ms each — already fast
   - Hit shim DMA exhaustion with 10 workers; needs FIFO sharing

7. **Fuse all 3 PDIs into 1** (saves 2 PDI overheads)
   - Would need ~22 workers across all 4 columns
   - Shim DMA exhaustion makes this impractical without FIFO sharing

---

## Known Constraints

| Constraint | Impact | Workaround |
|-----------|--------|------------|
| Adjacent tiles share 64KB data memory | bn0 k3 weights (37KB each) can't coexist | Place bn0 cores in separate columns |
| AIE2P program memory ~16KB | k3 fused SiLU kernel is 16.4KB on some configs | Always use 2-col for k3 layers |
| Shim DMA channels limited (~24 total) | 10+ workers exhaust available channels | Keep k1 layers single-column |
| `_factorize_tensor()` repeat_count bug | `d3=64` produces `repeat_count=63` on drains | Use `_sr()` helper for drains |
| IRON `Worker()` without `rt.start()` | Workers silently omitted from MLIR | Always call `rt.start(*workers)` |
