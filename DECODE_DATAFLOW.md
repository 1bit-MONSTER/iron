# Decode Dataflow Design for Llama 3.2 1B on AMD AI Engine NPU

A comprehensive plan for a high-performance, token-in / token-out dataflow decode
architecture that eliminates unnecessary DDR round-trips by keeping activations on-chip
and streaming weights through the compute array.

## Table of Contents

1. [First Principles](#1-first-principles)
2. [Hardware Budget](#2-hardware-budget)
3. [The Fundamental Bottleneck](#3-the-fundamental-bottleneck)
4. [Current Architecture and Its Costs](#4-current-architecture-and-its-costs)
5. [Target Architecture: The Decode Mega-Operator](#5-target-architecture-the-decode-mega-operator)
6. [Phase 1: Fused Projection Engine](#6-phase-1-fused-projection-engine)
7. [Phase 2: On-Chip Attention (FlowKV)](#7-phase-2-on-chip-attention-flowkv)
8. [Phase 3: Fused MLP (SwiGLU) Engine](#8-phase-3-fused-mlp-swiglu-engine)
9. [Phase 4: Full Layer Dataflow](#9-phase-4-full-layer-dataflow)
10. [Phase 5: INT4 Weight Quantization (FusedDQP)](#10-phase-5-int4-weight-quantization-fuseddqp)
11. [Tile Mapping](#11-tile-mapping)
12. [Data Movement Discipline](#12-data-movement-discipline)
13. [Performance Model](#13-performance-model)
14. [Implementation Roadmap](#14-implementation-roadmap)
15. [References and Inspiration](#15-references-and-inspiration)

---

## 1. First Principles

### The Goal

**One token in, one token out. No wasted trips to DDR.**

During autoregressive decode, each generated token flows through all 16 transformer
layers sequentially. Each layer consists of two sub-blocks:

```
Token → RMSNorm → Attention(QKV proj → RoPE → GQA → Output proj) → Residual Add
      → RMSNorm → MLP(Gate proj → Up proj → SiLU·Mul → Down proj)  → Residual Add → Token
```

The activation vector is small -- 2048 bfloat16 values = **4 KB**. This easily fits in a
single tile's 64 KB L1 memory. There is no computational reason for it to ever touch DDR
between operations within a layer. The only data that *must* stream from DDR are:

1. **Weights** -- ~116 MB per layer at bf16, ~29 MB at INT4
2. **KV cache** -- grows with sequence length, lives in DDR

Everything else should stay on-chip.

### Design Philosophy

| Principle | Rationale |
|---|---|
| **Bandwidth is the bottleneck, not compute** | A 2048×8192 GEMV requires 33.6 MFLOP but loads 32 MB of weights. At 25 TFLOPS peak, compute takes 1.3 µs. At 50 GB/s DDR bandwidth, loading takes 640 µs. The ratio is 500:1. |
| **Every DDR byte must earn its keep** | Each byte loaded from DDR should contribute to a MAC operation. Materializing intermediate activations in DDR is pure waste. |
| **Fuse vertically, parallelize horizontally** | Fuse sequential operations that share activations (vertical). Distribute independent weight rows across columns (horizontal). |
| **The NPU IS a persistent kernel** | Workers run in infinite loops. ObjectFIFOs are hardware producer-consumer queues. This is the mega-kernel that GPU programmers dream of -- we just need to use it. |
| **Stream weights, hold activations** | Activations are reused (the input vector is read by every weight row). Weights are used once per token. Therefore: hold activations stationary in L1, stream weights through. |

---

## 2. Hardware Budget

### XDNA 2 (Strix Point / NPU2) -- Primary Target

| Resource | Per Unit | Total |
|---|---|---|
| Compute tiles | 4 rows × 8 columns | **32 tiles** |
| L1 data memory | 64 KB per tile | **2 MB total** |
| L1 program memory | 16 KB per tile | 512 KB total |
| Memory tiles (L2) | 512 KB each, 8 total | **4 MB total** |
| Shim/Interface tiles | 1 per column | **8 shim tiles** |
| Shim DMA channels | 2 S2MM + 2 MM2S per shim | **32 total** |
| MemTile DMA channels | 6 S2MM + 6 MM2S per memtile | **96 total** |
| Compute tile DMA | 2 S2MM + 2 MM2S per tile | **128 total** |
| bf16 MAC/cycle/tile | 128 FMA (256 FLOP) | 8192 FMA across array |
| Clock frequency | ~1.3-1.8 GHz | |
| DDR bandwidth | 50-80 GB/s (platform dependent) | |

### XDNA 1 (Phoenix/Hawk -- NPU1) -- Secondary Target

| Resource | Per Unit | Total |
|---|---|---|
| Compute tiles | 4 rows × 4 columns | **16 tiles** |
| L1/L2/Shim | Same per-unit specs | Half the total |

### Llama 3.2 1B Model Dimensions

| Parameter | Value | Notes |
|---|---|---|
| Layers | 16 | |
| Hidden dim (`d_model`) | 2048 | Activation vector = 4 KB at bf16 |
| FFN intermediate dim | 8192 | 4× model dim |
| Attention heads | 32 | |
| KV heads (GQA) | 8 | 4:1 grouping ratio |
| Head dim (`d_head`) | 64 | = 2048/32 |
| Vocabulary | 128,256 | |
| Context length | 131,072 | |
| RoPE base | 500,000 | |

### Per-Layer Weight Inventory

| Weight Matrix | Dimensions | bf16 Size | INT4 Size |
|---|---|---|---|
| Wq (query proj) | 2048 × 2048 | 8 MB | 2 MB |
| Wk (key proj) | 2048 × 512 | 2 MB | 0.5 MB |
| Wv (value proj) | 2048 × 512 | 2 MB | 0.5 MB |
| Wo (output proj) | 2048 × 2048 | 8 MB | 2 MB |
| Wgate (SwiGLU gate) | 2048 × 8192 | 32 MB | 8 MB |
| Wup (SwiGLU up) | 2048 × 8192 | 32 MB | 8 MB |
| Wdown (SwiGLU down) | 8192 × 2048 | 32 MB | 8 MB |
| RMSNorm (×2) | 2048 each | ~8 KB | ~8 KB |
| **Layer total** | | **~116 MB** | **~29 MB** |
| **16-layer total** | | **~1.86 GB** | **~464 MB** |

---

## 3. The Fundamental Bottleneck

### Decode is DDR-Bandwidth-Bound

For a single decode token, every weight in every layer must be loaded from DDR exactly
once (there is no reuse across tokens in batch-1 decode). This makes the theoretical
minimum token latency:

| Precision | Weight Traffic/Token | @ 50 GB/s | @ 80 GB/s |
|---|---|---|---|
| bf16 | 1.86 GB | 37.2 ms (27 tok/s) | 23.3 ms (43 tok/s) |
| INT4 | 464 MB | 9.3 ms (108 tok/s) | 5.8 ms (172 tok/s) |

At longer sequences, KV cache traffic adds to this. For context length L with 8 KV heads
and d_head=64:

```
KV cache traffic per layer = 2 × L × 8 × 64 × 2 bytes = 2048 × L bytes
KV cache traffic (16 layers) = 32,768 × L bytes
At L=4096: 128 MB additional per token
```

### Implication

**Every optimization must be measured in DDR bytes saved, not FLOPS gained.**

The entire design should be viewed as a weight-streaming pipeline where:
- DDR continuously feeds weight data through the shim → memtile → compute tile path
- Activations never touch DDR between operations within a layer
- Compute tiles perform fused multiply-accumulate as weight data streams through
- The only time activations return to DDR is between transformer layers (and even this
  is optional with careful design)

---

## 4. Current Architecture and Its Costs

### Current Decode Per-Layer Execution

The current IRON implementation executes decode as **10 separate operator invocations**
per transformer layer, each with its own kernel launch, DDR buffer sync, and
completion wait:

```
Step  Operator              Weight Traffic    Activation DDR Traffic
─────────────────────────────────────────────────────────────────────
 1    RMSNorm (input)       8 KB (γ)         4 KB read + 4 KB write
 2    GEMV: Q projection    8 MB (Wq)        4 KB read + 4 KB write
 3    GEMV: K projection    2 MB (Wk)        4 KB read + 1 KB write
 4    GEMV: V projection    2 MB (Wv)        4 KB read + 1 KB write
 5    RoPE (Q, K)           ~2 KB (LUT)      5 KB read + 5 KB write
 6    GQA attention         KV cache         ~10 KB read + 4 KB write
 7    GEMV: Output proj     8 MB (Wo)        4 KB read + 4 KB write
 8    Residual add          —                8 KB read + 4 KB write
 9    RMSNorm (post-attn)   8 KB (γ)         4 KB read + 4 KB write
10a   GEMV: Gate proj       32 MB (Wgate)    4 KB read + 16 KB write
10b   GEMV: Up proj         32 MB (Wup)      4 KB read + 16 KB write
10c   SiLU·Mul              —                32 KB read + 16 KB write
10d   GEMV: Down proj       32 MB (Wdown)    16 KB read + 4 KB write
11    Residual add          —                8 KB read + 4 KB write
─────────────────────────────────────────────────────────────────────
      TOTAL                 ~116 MB          ~152 KB wasted DDR I/O
```

### Where Time is Wasted

1. **Activation DDR round-trips**: The 4 KB activation vector is written to DDR after
   every operation and re-read by the next. Over 12+ operations per layer × 16 layers,
   this is ~192 unnecessary DDR transfers per token.

2. **Kernel launch overhead**: Each `run_runlist()` call involves XRT kernel invocation,
   DMA sync, and completion polling. At ~50-100 µs per launch, 12 launches × 16 layers
   = ~10-20 ms of pure overhead per token.

3. **Separate SwiGLU stages**: Gate and Up projections load the same 4 KB input vector
   from DDR independently. The intermediate 16 KB vectors (gate and up outputs) also
   round-trip through DDR before the SiLU·Mul fusion.

4. **No weight streaming overlap**: Each GEMV waits for the previous one to fully
   complete before starting its weight load. There is no pipelining between operators.

### What the Current WIP (swiglu-fusion branch) Addresses

The `dual_gemv_silu_mul` operator on this branch fuses steps 10a+10b+10c into a single
kernel invocation by interleaving Wgate and Wup rows in DDR and streaming them through
a single input FIFO. This eliminates the intermediate DDR traffic for the gate/up
vectors. However, it still operates as an isolated operator -- the activation arrives
from DDR and the result goes back to DDR.

---

## 5. Target Architecture: The Decode Mega-Operator

### Vision: One Design, One Token, One Layer

Instead of 10+ separate operators per layer, the target is a **single NPU design** that
processes one complete transformer layer per invocation:

```
                              ┌─────────────────────────────────────────┐
                              │         TRANSFORMER LAYER DESIGN        │
                              │                                         │
   Token (4KB) ──DDR──►       │  RMSNorm ──► QKV Proj ──► RoPE         │
                              │                  │                      │
                              │            Attn (FlowKV) ◄── KV Cache   │
                              │                  │           (DDR)      │
   Weights ────DDR──►         │            Output Proj                  │
   (streamed)                 │                  │                      │
                              │            Residual Add                 │
                              │                  │                      │
                              │            RMSNorm                      │
                              │                  │                      │
                              │  ┌──► Gate Proj ──► SiLU ──┐           │
                              │  │                          ├──► Mul    │
                              │  └──► Up Proj ──────────────┘    │     │
                              │                              Down Proj  │
                              │                                  │     │
                              │                           Residual Add  │
                              │                                  │     │
                              └──────────────────────────────────┼─────┘
                                                                 │
   Token (4KB) ◄──DDR──                                   Output Token
```

**Data that touches DDR:**
- Token in (4 KB) -- once at layer start
- Token out (4 KB) -- once at layer end
- Weights (~116 MB at bf16, ~29 MB at INT4) -- streamed continuously
- KV cache (variable) -- streamed for attention

**Data that stays on-chip:**
- All intermediate activations (norm outputs, projections, attention scores, MLP intermediates)

### Incremental Path to Get There

This cannot be built in one step. The plan follows five phases, each delivering
measurable value and building toward the full vision:

| Phase | Scope | DDR Savings | Key Innovation |
|---|---|---|---|
| 1 | Fused QKV Projection | 3× fewer input vector loads | Weight concatenation + split output |
| 2 | On-chip Attention (FlowKV) | Eliminate Q/K/V DDR write + attn DDR read | 2-CT pipeline with online softmax |
| 3 | Fused MLP (complete SwiGLU) | Eliminate 4 intermediate DDR transfers | Dual-GEMV + SiLU·Mul + Down proj chain |
| 4 | Full Layer Dataflow | Eliminate ALL intermediate DDR traffic | RMSNorm → Proj → Attn → MLP chain |
| 5 | INT4 Quantization (FusedDQP) | 4× reduction in weight traffic | Fused dequant-GEMV kernel |

---

## 6. Phase 1: Fused Projection Engine

### Problem

The current decode runs Q, K, V, and output projections as **4 separate GEMV
invocations**. Each one:
1. Loads the 4 KB activation vector from DDR
2. Streams its weight matrix from DDR
3. Writes its output vector back to DDR

The activation vector is loaded 4 times when it only needs to be loaded once.

### Design: `fused_qkv_proj`

**Concept**: Concatenate Wq, Wk, Wv row-wise into a single weight matrix. Run one
GEMV that produces the concatenated [Q, K, V] output. The host-side op splits the
output vector into Q, K, V segments.

```
Concatenated weight matrix:

    ┌─── Wq rows (2048 × 2048) ───┐
    │                              │
    ├─── Wk rows (512 × 2048) ────┤
    │                              │
    └─── Wv rows (512 × 2048) ────┘

    Total: 2560 × 2048 (at bf16: 10 MB streamed once, vector loaded once)
```

**Tile mapping**: Distribute the 2560 output rows across all available columns.
Each column processes 2560/N_cols rows, receiving the same input vector via broadcast
and streaming its portion of the concatenated weight matrix.

**ObjectFIFO structure per column**:
- `of_weights` (depth=2): Streams weight rows from DDR, double-buffered
- `of_input` (depth=1): Holds input vector, loaded once at start
- `of_output` (depth=2): Drains output rows to DDR

**Benefit**: Eliminates 3 redundant 4 KB vector loads and 3 kernel launch overheads.

### Alternatively: Interleaved Q/K/V Weights

For better cache locality and simpler output splitting, interleave Q/K/V weight rows
in a pattern that produces outputs aligned to per-column boundaries:

```
Column 0: [Wq rows 0..255, Wk rows 0..63, Wv rows 0..63]
Column 1: [Wq rows 256..511, Wk rows 64..127, Wv rows 64..127]
...
```

This way each column's output naturally separates into Q, K, V segments without
post-processing.

---

## 7. Phase 2: On-Chip Attention (FlowKV)

### Problem

After QKV projection, the current flow writes Q, K, V to DDR, applies RoPE on the
CPU/separate operator, updates the KV cache in DDR, then reads everything back for
attention computation. During decode, attention is a 1-query operation against the
full KV cache -- inherently streaming.

### Design: FlowKV Decode (2-Tile Pipeline per KV Head)

Inspired by the FastFlowLM paper's FlowKV design, but cleaner by leveraging IRON's
ObjectFIFO abstraction directly.

**Architecture**: 4 KV head groups × 2 tiles per group = **8 tiles** (2 columns)

```
Per KV head group (handles 4 query heads with shared K, V):

  ┌──────────────────────────────────────────────────────┐
  │  CT0: Score Tile                                     │
  │                                                      │
  │  Inputs:  Q vector (4 heads × 64 = 256 bf16)       │
  │           K chunk (Lc × 64 bf16) -- streamed from   │
  │           KV cache in DDR                            │
  │                                                      │
  │  Compute: For each K chunk c:                        │
  │    S_c = Q · K_c^T / sqrt(64)       (dot products)  │
  │    m_new = max(m_old, max(S_c))     (running max)   │
  │    F_c = exp(S_c - m_new)           (safe exp)      │
  │    C_c = exp(m_old - m_new)         (correction)    │
  │    l = C_c · l_old + sum(F_c)       (denominator)   │
  │                                                      │
  │  Outputs: F_c, C_c, l → CT1 via ObjectFIFO         │
  └──────────────────────┬───────────────────────────────┘
                         │ on-chip (no DDR)
  ┌──────────────────────▼───────────────────────────────┐
  │  CT1: Value Tile                                     │
  │                                                      │
  │  Inputs:  F_c, C_c, l from CT0 (on-chip FIFO)      │
  │           V chunk (Lc × 64 bf16) -- streamed from   │
  │           KV cache in DDR                            │
  │                                                      │
  │  Compute: For each chunk c:                          │
  │    Y = C_c · Y_old + F_c · V_c     (accumulate)    │
  │                                                      │
  │  Final:   O = Y / l                 (normalize)     │
  │                                                      │
  │  Output:  O (4 heads × 64 = 256 bf16) → DDR or     │
  │           directly to output projection FIFO         │
  └──────────────────────────────────────────────────────┘
```

**Key properties**:
- Online softmax: exact FlashAttention semantics, single streaming pass over KV cache
- Intermediates (F_c, C_c, l) pass tile-to-tile via ObjectFIFO, never touch DDR
- K and V chunks double-buffered: depth=2 FIFOs overlap DMA with compute
- Each KV head group processes independently -- natural column parallelism
- Works for any sequence length (just stream more KV chunks)

**Chunk size selection**: With d_head=64, each K chunk of Lc positions is
Lc × 64 × 2 = 128·Lc bytes. At Lc=64, each chunk is 8 KB. The score tile needs
space for Q (512 bytes for 4 heads), one K chunk (8 KB), scores (Lc × 4 × 2 = 512 bytes),
and softmax state (~64 bytes). Total: ~9 KB, well within 64 KB L1.

### RoPE Integration

RoPE rotation can be fused directly into the score tile kernel. When Q arrives and each
K chunk arrives, apply RoPE rotation in-register before the dot product. The rotation
coefficients (sin/cos LUT for the current position) are tiny (~256 bytes) and can be
loaded once into a static buffer.

This eliminates RoPE as a separate operator entirely.

---

## 8. Phase 3: Fused MLP (SwiGLU) Engine

### Problem

The SwiGLU MLP consists of:
1. Gate projection: Wgate × x → gate (2048 → 8192)
2. Up projection: Wup × x → up (2048 → 8192)
3. Activation: SiLU(gate) · up → intermediate (8192)
4. Down projection: Wdown × intermediate → output (8192 → 2048)

Currently, steps 1-3 are being fused in `dual_gemv_silu_mul` (WIP on this branch), but
step 4 (down projection) remains separate. This means the 8192-element intermediate
vector (16 KB) is written to DDR and re-read.

### Design: Complete SwiGLU Fusion

**Strategy**: Chain the dual-GEMV-SiLU-Mul output directly into a down-projection
GEMV, all within one NPU design.

**Two-stage tile pipeline** using all available columns:

```
Stage 1: Gate+Up+SiLU·Mul (rows 2-3 of each column)
──────────────────────────────────────────────────────
  Row 2 Tile: Dual-GEMV core
    - Input: x vector (4 KB, held in L1)
    - Streams: Interleaved Wgate/Wup rows from DDR
    - Output: SiLU(gate_partial) · up_partial → ObjectFIFO to Row 3

  Each column produces M_ffn/N_cols elements of the 8192-dim intermediate

Stage 2: Down projection (row 3-4 of each column)
──────────────────────────────────────────────────────
  Row 3 Tile: Down-GEMV accumulator
    - Input: intermediate chunk from Row 2 via ObjectFIFO (ON-CHIP)
    - Streams: Wdown rows from DDR (each row is 8192 bf16 = 16 KB)
    - Accumulates: partial output vector (2048 elements)
    - Output: partial output → drain to DDR
```

**The key insight**: The 8192-element intermediate vector never touches DDR.
Each column produces its slice of the intermediate, and the down-projection tile
in the same column immediately consumes it via an ObjectFIFO link.

**Challenge**: The down projection has K=8192, meaning each weight row is 16 KB at bf16
(or 4 KB at INT4). A single tile can hold ~3 weight rows at bf16 in L1 with
double-buffering. This is fine for streaming -- the tile processes one row at a time.

However, the down projection's output dimension is 2048, and each column only has access
to `8192/N_cols` elements of the intermediate vector. This means each column computes a
**partial dot product** for each output row, and these partials must be reduced.

**Reduction options**:
1. **Cascade chain** across rows: Accumulate partial products along the row, with each
   tile forwarding its partial sum to the next via the cascade interconnect.
2. **DDR reduction**: Each column writes its partial output; the host sums them.
   (Simple but adds DDR traffic.)
3. **MemTile reduction**: Route partial outputs through memory tiles for accumulation.

Option 1 (cascade) is the cleanest for the full dataflow design. Each column contributes
its partial sum to a cascade chain that produces the final output at the last tile.

---

## 9. Phase 4: Full Layer Dataflow

### The Prize: Zero Intermediate DDR Traffic

By chaining Phases 1-3, one complete transformer layer runs as a single NPU design:

```
DDR ──► x (4KB)                                                    DDR
         │                                                           ▲
    ┌────▼─────┐                                                     │
    │ RMSNorm  │ (1 tile, row 2, col 0)                             │
    │ + γ wts  │                                                     │
    └────┬─────┘                                                     │
         │ ObjectFIFO (on-chip)                                      │
    ┌────▼──────────────────────────────────┐                        │
    │  Fused QKV Projection (16 tiles)      │◄── Wq,Wk,Wv from DDR │
    │  4 cols × 4 rows, weight streaming    │                        │
    └────┬──────────┬───────────┬───────────┘                        │
         │Q         │K          │V                                   │
         │(on-chip) │(on-chip)  │(on-chip)                          │
    ┌────▼──────────▼───────────▼───────────┐                        │
    │  FlowKV Attention (8 tiles)           │◄── KV cache from DDR  │
    │  4 KV groups × 2 tiles each           │──► KV cache to DDR    │
    │  Online softmax, no attn matrix DDR   │                        │
    └────┬──────────────────────────────────┘                        │
         │ attn_output (on-chip)                                     │
    ┌────▼──────────────────────────────────┐                        │
    │  Output Projection (8 tiles)          │◄── Wo from DDR        │
    │  Weight streaming GEMV                │                        │
    └────┬──────────────────────────────────┘                        │
         │ (on-chip)                                                 │
    ┌────▼─────┐                                                     │
    │ Residual │ + original x                                        │
    │   Add    │ (x held in memtile from layer start)               │
    └────┬─────┘                                                     │
         │ (on-chip)                                                 │
    ┌────▼─────┐                                                     │
    │ RMSNorm  │                                                     │
    └────┬─────┘                                                     │
         │ (on-chip)                                                 │
    ┌────▼──────────────────────────────────┐                        │
    │  Fused SwiGLU MLP                     │◄── Wgate,Wup,Wdown    │
    │  Dual-GEMV + SiLU·Mul + Down proj     │    from DDR           │
    │  Intermediate never leaves tile       │                        │
    └────┬──────────────────────────────────┘                        │
         │ (on-chip)                                                 │
    ┌────▼─────┐                                                     │
    │ Residual │ + post-attention x                                  │
    │   Add    │ (held in memtile)                                  │
    └────┬─────┘                                                     │
         │                                                           │
         └──────────────────────────────────────────────► x' (4KB) ──┘
```

### Activation Flow Budget

| Stage | Input Size | Output Size | On-chip? |
|---|---|---|---|
| Token in | 4 KB | — | DDR → L1 (once) |
| RMSNorm | 4 KB | 4 KB | L1 → L1 via FIFO |
| QKV Projection | 4 KB | 5 KB (Q:4KB + K:1KB + V:1KB) | L1 → L1 via FIFO |
| RoPE | ~5 KB | ~5 KB | In-register (fused into attention) |
| FlowKV Attention | 5 KB + KV cache | 4 KB | L1 → L1 via FIFO (KV cache from DDR) |
| Output Projection | 4 KB | 4 KB | L1 → L1 via FIFO |
| Residual Add | 4 KB + 4 KB | 4 KB | L1 (x from memtile) |
| RMSNorm | 4 KB | 4 KB | L1 → L1 via FIFO |
| SwiGLU MLP | 4 KB | 4 KB | L1 → L1 (16 KB intermediate on-chip) |
| Residual Add | 4 KB + 4 KB | 4 KB | L1 (x from memtile) |
| Token out | — | 4 KB | L1 → DDR (once) |

**Total DDR activation traffic: 8 KB** (4 KB in + 4 KB out) vs. current ~152 KB.

### Residual Connection Strategy

The residual connections require the *original* input to be available after the
attention/MLP sub-block completes. Two approaches:

1. **MemTile stash**: Copy the input activation to a memory tile (512 KB available)
   at layer start. After the sub-block completes, read it back for the add. Cost: one
   4 KB L1→L2 write and one 4 KB L2→L1 read per residual. No DDR involved.

2. **Dedicated tile buffer**: Assign one tile's L1 as a "residual buffer" that holds
   the input activation while the pipeline processes. The residual add tile reads
   from this neighbor via the direct load path (512 bits/cycle).

Option 1 is more practical since it doesn't consume a compute tile.

---

## 10. Phase 5: INT4 Weight Quantization (FusedDQP)

### Motivation

INT4 quantization reduces weight traffic by 4× -- this is the single highest-impact
optimization for decode throughput.

### Quantization Format: Q4-Block Aligned

Inspired by FastFlowLM's Q4NX but simplified for IRON:

```
Block layout (group_size=32):

  ┌───────────────────────────────────────┐
  │  32 × K_tile INT4 weights             │  (32 × K_tile / 2 bytes)
  │  K_tile/32 bf16 scales                │  (K_tile/32 × 2 bytes)
  │  K_tile/32 bf16 zero-points           │  (K_tile/32 × 2 bytes)
  └───────────────────────────────────────┘

  Dequantization: w_bf16 = scale * (w_int4 - zero_point)
```

**Tile size K_tile**: Choose K_tile to align with the tile's natural processing width.
For bf16 GEMV with `aie::mmul<4,8,8>`, K_tile=256 is natural (matches the existing
microkernel's reduction dimension granularity).

### Fused Dequant-GEMV Kernel

The GEMV kernel dequantizes weight sub-blocks in-register before the MAC:

```cpp
// Pseudocode for fused dequant-GEMV inner loop
for (int k_block = 0; k_block < K; k_block += 32) {
    // Load 32 INT4 weights (16 bytes) from FIFO
    auto w_int4 = fifo_weights.acquire();

    // Load scale and zero-point for this group
    auto scale = scales[k_block / 32];
    auto zp = zero_points[k_block / 32];

    // Dequantize to bf16 in vector registers
    auto w_bf16 = scale * (convert_int4_to_bf16(w_int4) - zp);

    // Multiply-accumulate with activation vector
    acc += w_bf16 * x[k_block : k_block + 32];

    fifo_weights.release();
}
```

**Bandwidth saving**: For a 2048×8192 GEMV:
- bf16: 32 MB weight traffic
- INT4: 8 MB weight traffic + ~128 KB metadata = ~8.1 MB
- **3.9× reduction in DDR bandwidth**

### INT4 Weight Packing

Pack two INT4 weights into one byte. The kernel unpacks using shift+mask:

```cpp
int8_t packed = weight_buffer[i];
int4_t w0 = packed & 0x0F;
int4_t w1 = (packed >> 4) & 0x0F;
```

This is a simple, architecture-independent operation that adds negligible compute cost.

---

## 11. Tile Mapping

### Full Layer Design: Tile Allocation (NPU2, 8 columns × 4 rows)

```
         Col 0      Col 1      Col 2      Col 3      Col 4      Col 5      Col 6      Col 7
       ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
Row 4  │ Proj    │ Proj    │ Proj    │ Proj    │ Proj    │ Proj    │ Proj    │ Proj    │
       │ GEMV-0  │ GEMV-1  │ GEMV-2  │ GEMV-3  │ GEMV-4  │ GEMV-5  │ GEMV-6  │ GEMV-7  │
       ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
Row 3  │ Attn    │ Attn    │ Attn    │ Attn    │ MLP     │ MLP     │ MLP     │ MLP     │
       │ Score-0 │ Score-1 │ Score-2 │ Score-3 │ DualGV-4│ DualGV-5│ DualGV-6│ DualGV-7│
       ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
Row 2  │ Attn    │ Attn    │ Attn    │ Attn    │ MLP     │ MLP     │ MLP     │ MLP     │
       │ Value-0 │ Value-1 │ Value-2 │ Value-3 │ DownPr-4│ DownPr-5│ DownPr-6│ DownPr-7│
       ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
Row 1  │ Norm+   │ Norm+   │ OutProj │ OutProj │ OutProj │ OutProj │ Residual│ Residual│
       │ RoPE    │ Add     │  GEMV-0 │  GEMV-1 │  GEMV-2 │  GEMV-3 │ +Norm   │ +Add    │
       ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
MemTile│  MT-0   │  MT-1   │  MT-2   │  MT-3   │  MT-4   │  MT-5   │  MT-6   │  MT-7   │
       │ Residual│ Weight  │ Weight  │ Weight  │ Weight  │ Weight  │ Weight  │ Residual│
       │ stash   │ staging │ staging │ staging │ staging │ staging │ staging │ stash   │
       ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
Shim   │  Shim-0 │  Shim-1 │  Shim-2 │  Shim-3 │  Shim-4 │  Shim-5 │  Shim-6 │  Shim-7 │
       │ DDR I/O │ DDR I/O │ DDR I/O │ DDR I/O │ DDR I/O │ DDR I/O │ DDR I/O │ DDR I/O │
       └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

**Allocation summary**:
- **Row 4 (8 tiles)**: Projection GEMV engine -- handles QKV projection (Phase 1),
  MLP gate/up projections (Phase 3), and output projection. Time-multiplexed across
  these roles within a single layer execution.
- **Rows 2-3, Cols 0-3 (8 tiles)**: FlowKV attention -- 4 KV groups × 2 tiles each
- **Rows 2-3, Cols 4-7 (8 tiles)**: SwiGLU MLP -- dual-GEMV + down projection
- **Row 1 (8 tiles)**: Utility -- RMSNorm, RoPE, residual add, output projection
- **MemTiles**: Residual activation stash + weight staging

### Time-Multiplexing Strategy

The 32 tiles process a layer in **temporal phases**, reusing tiles across roles:

```
Time →

Phase A: Input Norm + QKV Projection
  Row 4:   Stream Wq/Wk/Wv, compute QKV projection (all 8 cols)
  Row 1:   RMSNorm produces normalized input → Row 4 via FIFO

Phase B: Attention + Output Projection
  Cols 0-3: FlowKV attention (rows 2-3)
  Cols 4-7: Output projection (row 4, time-shared)

Phase C: Post-Attention Norm + SwiGLU MLP
  Row 4:   Stream Wgate/Wup, compute gate+up projection (all 8 cols)
  Row 1:   RMSNorm + residual add
  Rows 2-3 cols 4-7: Down projection (consumes intermediate from row 4)

Phase D: Final Residual Add + Output
  Row 1:   Add MLP output to residual, produce final token
```

This time-multiplexing means that while only 32 tiles exist, each phase uses them at
~100% utilization for its specific task. The key is that **activations pass between
phases via on-chip FIFOs**, never DDR.

---

## 12. Data Movement Discipline

### The Five Commandments

1. **Activations stay on-chip.** The 4 KB activation vector enters from DDR once at
   layer start and exits once at layer end. Between operations, it moves tile-to-tile
   via ObjectFIFOs through L1 or via L2 memtile staging.

2. **Weights stream, never load.** Weights flow DDR → Shim → MemTile → Compute Tile
   through double-buffered FIFOs. No weight data is ever "loaded" into L2 for later
   use -- it passes through on its way to the compute tile.

3. **Double-buffer everything.** Every ObjectFIFO carrying streamed data uses depth≥2.
   While the kernel processes buffer A, DMA fills buffer B. This hides the full DMA
   transfer latency when compute time ≥ transfer time.

4. **Broadcast shared inputs.** The activation vector is broadcast to all columns via
   multicast ObjectFIFO. Each column receives a copy without independent DMA channels.

5. **Reduce on-chip when possible.** Partial results from column-parallel GEMVs are
   reduced via cascade chain or memtile routing, not DDR round-trips.

### ObjectFIFO Depth Strategy

| Data Type | FIFO Depth | Rationale |
|---|---|---|
| Weight rows (DDR→L1) | 2 | Double-buffer: overlap DMA with compute |
| Activation (tile→tile) | 1 | Small, produced/consumed synchronously |
| FlowKV intermediates | 2 | Pipeline CT0→CT1, overlap scoring with value weighting |
| KV cache chunks (DDR→L1) | 2 | Double-buffer: overlap DMA with attention compute |
| Down proj intermediate | 2 | Pipeline dual-GEMV output into down-proj input |

### DMA Channel Budget

Each shim tile has 2 S2MM (DDR→NPU) + 2 MM2S (NPU→DDR) channels.
For 8 shim tiles: 16 input + 16 output channels total.

Per-phase DMA allocation:

| Phase | Input Channels (S2MM) | Output Channels (MM2S) |
|---|---|---|
| QKV Projection | 8 (weight rows, 1/col) + 1 (input vector broadcast) | 8 (QKV outputs, 1/col) |
| Attention | 8 (K/V cache chunks, 2/KV group) | 4 (attn outputs) + 4 (KV cache writes) |
| MLP | 8 (weight rows) + 1 (input broadcast) | 8 (partial outputs) |

This fits within the 16+16 channel budget for each phase. With time-multiplexing,
channels are reassigned between phases.

---

## 13. Performance Model

### Theoretical Token Latency

#### bf16 Weights (Current Precision)

```
Weight traffic per token:
  16 layers × 116 MB/layer = 1,856 MB

KV cache traffic per token (at seq_len=1024):
  16 layers × 2 × 1024 × 8 × 64 × 2 bytes = 32 MB

Total DDR traffic: ~1,888 MB

At 50 GB/s DDR bandwidth:
  1,888 MB / 50 GB/s = 37.8 ms → 26 tokens/second

At 80 GB/s DDR bandwidth:
  1,888 MB / 80 GB/s = 23.6 ms → 42 tokens/second
```

#### INT4 Weights (Phase 5)

```
Weight traffic per token:
  16 layers × 29 MB/layer = 464 MB
  + metadata (scales, zero-points): ~14 MB
  Total: ~478 MB

KV cache traffic (at seq_len=1024): 32 MB

Total DDR traffic: ~510 MB

At 50 GB/s: 510 / 50 = 10.2 ms → 98 tokens/second
At 80 GB/s: 510 / 80 = 6.4 ms  → 157 tokens/second
```

#### Overhead Budget

| Source | Estimate | Notes |
|---|---|---|
| Kernel launch (1 per layer) | 50 µs × 16 = 0.8 ms | Single design per layer |
| DDR activation I/O | 8 KB × 16 / 50 GB/s ≈ 0 | Negligible |
| On-chip FIFO overhead | ~10 µs per layer | Lock acquire/release |
| Host-side processing | ~1 ms total | Sampling, KV cache management |
| **Total overhead** | **~2 ms** | |

#### Comparison

| Configuration | Tok/s (50 GB/s) | Tok/s (80 GB/s) | vs. Current |
|---|---|---|---|
| Current (12 ops/layer, bf16) | ~15-20 | ~25-30 | baseline |
| Full layer fusion, bf16 | ~26 | ~42 | ~1.5-2× |
| Full layer fusion, INT4 | ~90 | ~140 | ~5-7× |
| INT4 + KV cache INT8 | ~95 | ~150 | ~5-8× |

### Where Does Time Go?

At INT4 with full fusion (target state), per-layer breakdown:

| Operation | Weight Traffic | Time @ 50 GB/s | % of Layer |
|---|---|---|---|
| QKV Projection | 2.5 MB | 50 µs | 8% |
| Attention (KV cache) | 2 MB @ L=1024 | 40 µs | 6% |
| Output Projection | 2 MB | 40 µs | 6% |
| Gate+Up Projection | 16 MB | 320 µs | 50% |
| Down Projection | 8 MB | 160 µs | 25% |
| Everything else | ~0 | ~20 µs | 3% |
| **Total per layer** | **~30.5 MB** | **~630 µs** | |
| **16 layers** | **~488 MB** | **~10.1 ms** | **~99 tok/s** |

The MLP (gate+up+down) dominates at 75% of layer time. This confirms that
SwiGLU fusion and weight quantization are the highest-impact optimizations.

---

## 14. Implementation Roadmap

### Phase 1: Fused QKV Projection (Foundation)
**Scope**: New operator `fused_qkv_proj_decode`
**Files**:
  - `iron/operators/fused_qkv_proj/op.py`
  - `iron/operators/fused_qkv_proj/design.py`
  - `iron/operators/fused_qkv_proj/reference.py`
  - `iron/operators/fused_qkv_proj/test.py`

**Key work**:
- Concatenate Wq, Wk, Wv into single weight buffer
- GEMV design with broadcast input, column-parallel weight streaming
- Output splitting into Q, K, V segments
- Validate against separate Q/K/V GEMV outputs

**Risk**: Low. This is a straightforward extension of the existing GEMV pattern.

### Phase 2: FlowKV Decode Attention
**Scope**: New operator `flowkv_decode`
**Files**:
  - `iron/operators/flowkv_decode/op.py`
  - `iron/operators/flowkv_decode/design.py`
  - `iron/operators/flowkv_decode/reference.py`
  - `iron/operators/flowkv_decode/test.py`
  - `aie_kernels/aie2/flowkv_score.cc`
  - `aie_kernels/aie2/flowkv_value.cc`
  - (and aie2p variants)

**Key work**:
- 2-tile pipeline design (score tile + value tile) per KV head group
- Online softmax kernel (streaming, single-pass)
- KV cache chunk streaming with double buffering
- Fused RoPE within score kernel
- GQA: 4 query heads per KV group
- Validate against existing CPU attention implementation

**Risk**: Medium. Online softmax requires careful numerical implementation. The
2-tile pipeline is a new pattern for this codebase but well-established in
FastFlowLM.

### Phase 3: Complete SwiGLU Fusion
**Scope**: Extend `dual_gemv_silu_mul` to include down projection
**Files**:
  - `iron/operators/swiglu_fused_decode/op.py`
  - `iron/operators/swiglu_fused_decode/design.py`
  - `iron/operators/swiglu_fused_decode/reference.py`
  - `iron/operators/swiglu_fused_decode/test.py`
  - `aie_kernels/aie2/swiglu_fused.cc` (extended kernel)

**Key work**:
- Fix current `dual_gemv_silu_mul` WIP (debug static buffer issue)
- Extend design to chain output into down-projection tiles via ObjectFIFO
- Column-parallel intermediate → down-proj reduction strategy
- Validate end-to-end: input → SwiGLU output matches reference

**Risk**: Medium-High. The two-stage pipeline with on-chip intermediate passing
is the most complex dataflow in the design. The cascade/reduction for the down
projection across columns needs careful design.

**Prerequisite**: Fix the `dual_gemv_silu_mul` bug first (13 zero output elements).

### Phase 4: Full Layer Integration
**Scope**: New mega-operator `transformer_layer_decode`
**Files**:
  - `iron/operators/transformer_layer_decode/op.py`
  - `iron/operators/transformer_layer_decode/design.py`
  - `iron/operators/transformer_layer_decode/reference.py`
  - `iron/operators/transformer_layer_decode/test.py`

**Key work**:
- Compose Phase 1-3 designs into a single NPU program
- Time-multiplexed tile usage across attention and MLP phases
- MemTile-based residual stashing
- End-to-end validation: single token through one transformer layer
- Integration with `TransformerBlock.forward()` in the Llama application

**Risk**: High. This is the most architecturally complex design. Tile placement,
DMA channel allocation, and FIFO routing must be carefully managed to fit within
hardware constraints. The time-multiplexing pattern may require runtime sequence
support that needs validation with the toolchain.

### Phase 5: INT4 Quantization
**Scope**: Fused dequant-GEMV kernel + quantization tooling
**Files**:
  - `aie_kernels/aie2/fused_dequant_gemv.cc`
  - `aie_kernels/aie2p/fused_dequant_gemv.cc`
  - `iron/common/quantization.py` (weight packing utilities)
  - Updates to all GEMV-based operators to support INT4 mode

**Key work**:
- INT4 weight packing (2 weights per byte)
- Scale/zero-point metadata format
- Fused dequant kernel: unpack INT4, dequant to bf16, MAC in one loop
- Quantization-aware weight preparation script
- Accuracy validation against bf16 reference

**Risk**: Medium. The kernel is straightforward. The quantization accuracy must
be validated carefully -- perplexity regression testing against the bf16 baseline.

### Milestone Dependencies

```
Phase 1 (QKV Fusion) ──────────────────────────────────────┐
                                                            ├──► Phase 4
Phase 2 (FlowKV Attention) ────────────────────────────────┤    (Full Layer)
                                                            │
Phase 3 (SwiGLU Complete) ─────────────────────────────────┘
         ▲
         │
    Fix dual_gemv_silu_mul WIP bug

Phase 5 (INT4 Quantization) ─── independent, can proceed in parallel
```

---

## 15. References and Inspiration

### Primary Paper
- **"Mapping Gemma3 onto an Edge Dataflow Architecture"** (arXiv:2602.06063)
  - FusedDQP: Fused dequantization + projection -- the key decode optimization
  - FlowKV: 2-CT pipelined attention with online softmax
  - Q4NX: Block-aligned INT4 quantization format
  - Tile allocation: 16 CTs for projections, 8 CTs for attention, 1 CT each for
    nonlinear ops
  - Performance: 18.2 tok/s for Gemma3-4B, up to 41.1 tok/s for 1B on XDNA2
  - Power: 4.5W total system power (NPU + CPU overhead)

### GPU Techniques Adapted for NPU
- **FlashAttention** (Dao et al.): Online softmax with tiled KV processing --
  maps to FlowKV's 2-tile pipeline
- **FlashDecoding** (Dao et al.): Split-K parallelism across KV sequence --
  maps to multi-column KV chunk distribution
- **Persistent Kernels** (CUTLASS): Workers that never exit, processing work as
  it arrives -- this IS the NPU's native execution model
- **Stream-K** (Osama et al.): Uniform work distribution across compute units --
  maps to column-parallel GEMV with balanced row distribution
- **Mirage Persistent Kernel** (MPK): Mega-kernelizing entire inference into one
  kernel with dataflow dependencies -- the goal of Phase 4
- **Deep Kernel Fusion for Transformers** (arXiv:2602.11808): Gate+Up+SiLU+Mul
  fusion for SwiGLU -- implemented as `dual_gemv_silu_mul`

### Quantization References
- **AWQ** (MLSys 2024 Best Paper): Activation-aware weight quantization
- **GPTQ**: Row-wise post-training quantization
- **KVQuant** (NeurIPS 2024): 3-bit KV cache with <0.1 PPL loss
- **Marlin kernels**: Fused dequant-GEMM achieving 10.9× speedup over baseline

### MLIR-AIE Patterns Used
- **Cascade design** (`programming_examples/basic/matrix_multiplication/cascade/`):
  Accumulator chain through tile rows for partial sum reduction
- **Whole array design** (`programming_examples/basic/matrix_multiplication/whole_array/`):
  Full 8×4 tile utilization with broadcast/distribute
- **ObjectFIFO link** for multi-level staging (shim → memtile → compute)
- **Double-buffering** via `depth=2` ObjectFIFOs throughout
- **TensorAccessPattern** for strided DMA addressing of weight matrices

### NPU Architecture
- XDNA 2: 32 CTs (8×4), 64 KB L1/tile, 512 KB L2/memtile, ~1.3-1.8 GHz
- DDR bandwidth: 50-80 GB/s (platform dependent)
- bf16: 128 FMA/cycle/tile (256 FLOP)
- INT8: 256 MAC/cycle/tile
- Cascade chain between adjacent tiles for low-latency reduction
- Multicast ObjectFIFOs for broadcast patterns

---

*This document defines the target architecture for high-performance Llama 3.2 1B
decode on AMD AI Engine NPU. Each phase is independently valuable and testable.
The ultimate goal -- one design per layer, zero intermediate DDR traffic, INT4
weight streaming -- would achieve ~100 tokens/second on XDNA 2 hardware.*

---

## 16. Measured Bandwidth & Performance Projections

### 16.1 Measured DDR Bandwidth (Strix Point)

Aggregate NPU↔DDR bandwidth measured via mlir-aie memcpy benchmark:

```
$ python3 memcpy.py
Latency: 0.002609 seconds (2608.72 µs)
Effective Bandwidth: 51.45 GB/s
```

This measures the round-trip (read from DDR + write to DDR). For decode, which is
~99% reads (streaming weights, reading KV cache), the relevant bound is the
read-only share of that bus:

| Metric | Value |
|---|---|
| Measured R+W bandwidth | 51.45 GB/s |
| Estimated read-only bandwidth | **~25.7 GB/s** (= R+W / 2) |
| Overhead (kernel launch + host) | ~2 ms per token |

### 16.2 Traffic Model

**Fixed cost (per token, independent of sequence length):**

| Precision | Bytes/weight | 16-layer weight traffic |
|---|---|---|
| bf16 | 2.0 | 1,856 MB |
| bfp16 | 1.125 | 1,044 MB |
| INT4 (+metadata) | ~0.5 | 478 MB |

**Variable cost (scales with sequence length L):**

```
KV cache read per token = 16 layers × 2 (K+V) × L × 8 heads × 64 × 2 bytes
                        = 32,768 × L bytes = 32 KB × L

At bf16 KV:  32 KB × L
At INT8 KV:  16 KB × L
```

### 16.3 AIE2P Considerations

Per the AIE2P Architecture Specification v1.4, all on-chip datapaths are doubled
vs AIE2 (2x MACs/cycle, 2x DMA throughput, 2x stream switch width, 2x memory bank
width). Decode remains DDR-bandwidth-bound regardless -- the compute-to-bandwidth
ratio is 35-500:1 depending on operation.

**bfp16 (Block Floating Point)** is natively supported on AIE2P with 512
multiplies/cycle (8x bf16). Format: 8-bit mantissa per element + 8-bit shared
exponent per block of 8 elements. The hardware decompresses bfp16 on load with
zero kernel overhead, making it a practical middle ground between bf16 and INT4.

**Hardware tanh** is available on AIE2P via the vector non-linear unit, eliminating
LUT overhead for SiLU computation.

### 16.4 Strix Point Projections (25.7 GB/s Read)

All times include 2 ms overhead. KV cache at bf16 unless noted.

#### bf16 Weights

| Seq Len | Weights (MB) | KV Read (MB) | Total Read (MB) | Time (ms) | Tok/s |
|---|---|---|---|---|---|
| 128 | 1,856 | 4 | 1,860 | 74.4 | **13.4** |
| 512 | 1,856 | 16 | 1,872 | 74.8 | **13.4** |
| 1,024 | 1,856 | 32 | 1,888 | 75.5 | **13.2** |
| 2,048 | 1,856 | 64 | 1,920 | 76.7 | **13.0** |
| 4,096 | 1,856 | 128 | 1,984 | 79.2 | **12.6** |
| 8,192 | 1,856 | 256 | 2,112 | 84.2 | **11.9** |
| 16,384 | 1,856 | 512 | 2,368 | 94.1 | **10.6** |
| 32,768 | 1,856 | 1,024 | 2,880 | 114.1 | **8.8** |

#### bfp16 Weights (AIE2P native)

| Seq Len | Weights (MB) | KV Read (MB) | Total Read (MB) | Time (ms) | Tok/s |
|---|---|---|---|---|---|
| 128 | 1,044 | 4 | 1,048 | 42.8 | **23.4** |
| 512 | 1,044 | 16 | 1,060 | 43.2 | **23.1** |
| 1,024 | 1,044 | 32 | 1,076 | 43.9 | **22.8** |
| 2,048 | 1,044 | 64 | 1,108 | 45.1 | **22.2** |
| 4,096 | 1,044 | 128 | 1,172 | 47.6 | **21.0** |
| 8,192 | 1,044 | 256 | 1,300 | 52.6 | **19.0** |
| 16,384 | 1,044 | 512 | 1,556 | 62.5 | **16.0** |
| 32,768 | 1,044 | 1,024 | 2,068 | 82.4 | **12.1** |

#### INT4 Weights

| Seq Len | Weights (MB) | KV Read (MB) | Total Read (MB) | Time (ms) | Tok/s |
|---|---|---|---|---|---|
| 128 | 478 | 4 | 482 | 20.8 | **48.1** |
| 512 | 478 | 16 | 494 | 21.2 | **47.1** |
| 1,024 | 478 | 32 | 510 | 21.8 | **45.8** |
| 2,048 | 478 | 64 | 542 | 23.1 | **43.3** |
| 4,096 | 478 | 128 | 606 | 25.6 | **39.1** |
| 8,192 | 478 | 256 | 734 | 30.6 | **32.7** |
| 16,384 | 478 | 512 | 990 | 40.5 | **24.7** |
| 32,768 | 478 | 1,024 | 1,502 | 60.5 | **16.5** |

#### INT4 Weights + INT8 KV Cache

| Seq Len | Weights (MB) | KV Read (MB) | Total Read (MB) | Time (ms) | Tok/s |
|---|---|---|---|---|---|
| 128 | 478 | 2 | 480 | 20.7 | **48.3** |
| 512 | 478 | 8 | 486 | 20.9 | **47.8** |
| 1,024 | 478 | 16 | 494 | 21.2 | **47.1** |
| 2,048 | 478 | 32 | 510 | 21.8 | **45.8** |
| 4,096 | 478 | 64 | 542 | 23.1 | **43.3** |
| 8,192 | 478 | 128 | 606 | 25.6 | **39.1** |
| 16,384 | 478 | 256 | 734 | 30.6 | **32.7** |
| 32,768 | 478 | 512 | 990 | 40.5 | **24.7** |

### 16.5 Krackan Projections (51.4 GB/s Read)

Krackan uses the same AIE2P NPU but a different NOC in the SOC, theoretically
doubling the NPU's DDR bandwidth to ~51.4 GB/s read.

| Config | Seq 128 | Seq 1K | Seq 4K | Seq 8K | Seq 16K | Seq 32K |
|---|---|---|---|---|---|---|
| **bf16** | 38.2 / **26.2** | 38.7 / **25.8** | 40.6 / **24.6** | 43.1 / **23.2** | 48.0 / **20.8** | 58.0 / **17.2** |
| **bfp16** | 22.3 / **44.8** | 22.9 / **43.6** | 24.8 / **40.3** | 27.3 / **36.6** | 32.3 / **31.0** | 42.3 / **23.7** |
| **INT4** | 11.4 / **87.9** | 12.0 / **83.6** | 13.8 / **72.5** | 16.3 / **61.5** | 21.2 / **47.2** | 31.2 / **32.0** |
| **INT4+INT8 KV** | 11.3 / **88.2** | 11.6 / **86.1** | 12.5 / **79.8** | 13.8 / **72.5** | 16.3 / **61.5** | 21.2 / **47.2** |

*(Format: time ms / tok/s)*

### 16.6 Strix vs Krackan Comparison (Seq 1K)

| Config | Strix (25.7 GB/s) | Krackan (51.4 GB/s) | Speedup |
|---|---|---|---|
| bf16 | 13.2 tok/s | 25.8 tok/s | 1.95x |
| bfp16 | 22.8 tok/s | 43.6 tok/s | 1.91x |
| INT4 | 45.8 tok/s | 83.6 tok/s | 1.83x |
| INT4+INT8 KV | 47.1 tok/s | 86.1 tok/s | 1.83x |

Speedup is <2x because the fixed 2 ms overhead becomes a larger fraction of total
time at higher bandwidths.

### 16.7 KV Cache Crossover Points

The sequence length where KV cache traffic equals weight traffic (beyond this
point, KV cache dominates latency):

| Weight Precision | KV Format | Crossover Seq Len |
|---|---|---|
| bf16 | bf16 | ~58,000 |
| bfp16 | bf16 | ~32,600 |
| INT4 | bf16 | ~15,300 |
| INT4 | INT8 | ~30,600 |

These crossover points are bandwidth-independent (same on Strix and Krackan).

### 16.8 Key Takeaways

1. **Decode is DDR-read-bandwidth-bound at every precision.** Compute utilization
   is <1% even on AIE2. AIE2P's 2x MACs make compute even more irrelevant.

2. **INT4 is the single highest-impact optimization.** On Strix it takes decode
   from ~13 tok/s to ~46 tok/s (3.5x). On Krackan, from ~26 to ~84 tok/s (3.2x).

3. **bfp16 is the best effort-to-payoff ratio on AIE2P.** 1.78x bandwidth
   reduction with zero dequant kernel work -- the hardware decompresses on load.
   Gets to ~23 tok/s on Strix, ~44 on Krackan.

4. **KV cache quantization only matters past ~4K context with INT4 weights.** With
   bf16/bfp16 weights, the weight traffic so dominates that KV cache is noise at
   all practical sequence lengths.

5. **Krackan with INT4 achieves ~84 tok/s** at typical decode lengths -- genuine
   real-time conversational LLM speed from a laptop NPU. With INT8 KV cache, it
   sustains >60 tok/s out to 8K context.

6. **The 100 tok/s target** requires Krackan + INT4 + short context (<512), or
   further optimizations (INT3, structured pruning with hardware sparsity
   compression, or speculative decoding).

---

## 17. SOTA Comparison: FastFlowLM (FLM)

### 17.1 Published SOTA Numbers

FastFlowLM Llama 3.2 1B decode performance measured on **Krackan** (AMD Ryzen AI 7
350, Kraken Point, 32 GB DRAM). Performance is comparable to other Kraken Point
systems.

| Seq Len | 1K | 2K | 4K | 8K | 16K | 32K | 64K | 128K |
|---|---|---|---|---|---|---|---|---|
| **Tok/s** | 64.5 | 62.2 | 58.9 | 53.9 | 45.5 | 35.0 | 24.1 | 13.6 |
| Time (ms) | 15.50 | 16.08 | 16.98 | 18.55 | 21.98 | 28.57 | 41.49 | 73.53 |

### 17.2 Reverse-Engineering the SOTA Operating Point

The incremental cost per 1K positions of KV cache is remarkably consistent at
~0.41 ms/1K across the curve, revealing the underlying configuration. Fitting
`Time(L) = W/B + C×L/B + overhead` to the measured data:

| Parameter | Fitted Value |
|---|---|
| Effective read bandwidth | **~40 GB/s** |
| Weight precision | **INT4** (~478 MB per token) |
| KV cache format | **INT8** (~16 KB per position) |
| Fixed overhead | **~3.1 ms** |

**Model verification** across all sequence lengths:

| Seq Len | Predicted (ms) | Actual (ms) | Error |
|---|---|---|---|
| 1K | 15.47 | 15.50 | 0.0% |
| 2K | 15.89 | 16.08 | -1.2% |
| 4K | 16.73 | 16.98 | -1.5% |
| 8K | 18.41 | 18.55 | -0.8% |
| 16K | 21.76 | 21.98 | -1.0% |
| 32K | 28.47 | 28.57 | -0.4% |
| 64K | 41.89 | 41.49 | +1.0% |
| 128K | 68.74 | 73.53 | -6.5% |

The model fits within ~1.5% up to 64K context. The 6.5% deviation at 128K likely
reflects additional overhead at extreme context lengths (cache management, TLB
pressure, or sub-linear bandwidth scaling).

### 17.3 Bandwidth Calibration

**Critical clarification**: FLM was measured on **Krackan**, which has a different
NOC that theoretically doubles NPU memory bandwidth vs Strix. This means the ~40
GB/s effective read bandwidth demonstrated by FLM is a **Krackan** number, not a
Strix number.

Our Strix memcpy benchmark measured 51.45 GB/s R+W. However, the memcpy metric
(round-trip DMA throughput) does not directly predict decode read bandwidth. The
relationship between memcpy R+W and sustained unidirectional read throughput
depends on NOC topology, DDR controller scheduling, and access patterns.

**Calibrated read bandwidths:**

| Platform | Read BW | Basis |
|---|---|---|
| Krackan | **~40 GB/s** | Validated against FLM (model fits <1.5% error) |
| Strix | **~20 GB/s** | Estimated as ~half of Krackan (half the NOC BW) |

```
Krackan (FLM-validated):  ~40 GB/s effective read
Strix (projected):        ~20 GB/s effective read (half NOC bandwidth)
Strix memcpy (measured):  51.45 GB/s R+W (different metric, not directly comparable)
```

Note: The Strix ~20 GB/s read estimate supersedes the earlier memcpy-derived
25.7 GB/s estimate in Section 16.4. The memcpy R+W / 2 heuristic overestimated
Strix decode bandwidth because the memcpy benchmark exercises a different
(bidirectional) data path than the read-dominated decode workload.

### 17.4 Krackan Projections (40 GB/s Read -- FLM-Validated)

Using the FLM-calibrated bandwidth. Overhead = 3 ms. These projections are
validated against FLM's published numbers for the INT4+INT8 KV configuration.

#### bf16 Weights

| Seq Len | Weights (MB) | KV Read (MB) | Total (MB) | Time (ms) | Tok/s |
|---|---|---|---|---|---|
| 1K | 1,856 | 32 | 1,888 | 50.2 | **19.9** |
| 4K | 1,856 | 128 | 1,984 | 52.6 | **19.0** |
| 8K | 1,856 | 256 | 2,112 | 55.8 | **17.9** |
| 16K | 1,856 | 512 | 2,368 | 62.2 | **16.1** |
| 32K | 1,856 | 1,024 | 2,880 | 75.0 | **13.3** |
| 64K | 1,856 | 2,048 | 3,904 | 100.6 | **9.9** |

#### bfp16 Weights (AIE2P native, zero dequant overhead)

| Seq Len | Weights (MB) | KV Read (MB) | Total (MB) | Time (ms) | Tok/s |
|---|---|---|---|---|---|
| 1K | 1,044 | 32 | 1,076 | 29.9 | **33.4** |
| 4K | 1,044 | 128 | 1,172 | 32.3 | **31.0** |
| 8K | 1,044 | 256 | 1,300 | 35.5 | **28.2** |
| 16K | 1,044 | 512 | 1,556 | 41.9 | **23.9** |
| 32K | 1,044 | 1,024 | 2,068 | 54.7 | **18.3** |
| 64K | 1,044 | 2,048 | 3,092 | 80.3 | **12.5** |

#### INT4 Weights (bf16 KV)

| Seq Len | Weights (MB) | KV Read (MB) | Total (MB) | Time (ms) | Tok/s |
|---|---|---|---|---|---|
| 1K | 478 | 32 | 510 | 15.8 | **63.5** |
| 4K | 478 | 128 | 606 | 18.2 | **55.1** |
| 8K | 478 | 256 | 734 | 21.4 | **46.8** |
| 16K | 478 | 512 | 990 | 27.8 | **36.0** |
| 32K | 478 | 1,024 | 1,502 | 40.6 | **24.7** |
| 64K | 478 | 2,048 | 2,526 | 66.2 | **15.1** |

#### INT4 Weights + INT8 KV Cache

| Seq Len | Weights (MB) | KV Read (MB) | Total (MB) | Time (ms) | Tok/s |
|---|---|---|---|---|---|
| 1K | 478 | 16 | 494 | 15.4 | **65.1** |
| 4K | 478 | 64 | 542 | 16.6 | **60.4** |
| 8K | 478 | 128 | 606 | 18.2 | **55.1** |
| 16K | 478 | 256 | 734 | 21.4 | **46.8** |
| 32K | 478 | 512 | 990 | 27.8 | **36.0** |
| 64K | 478 | 1,024 | 1,502 | 40.6 | **24.7** |

**Validation against FLM** (INT4+INT8 KV):

| Seq Len | Our Model | FLM Actual | Error |
|---|---|---|---|
| 1K | 65.1 tok/s | 64.5 tok/s | +0.9% |
| 4K | 60.4 tok/s | 58.9 tok/s | +2.5% |
| 8K | 55.1 tok/s | 53.9 tok/s | +2.2% |
| 16K | 46.8 tok/s | 45.5 tok/s | +2.9% |
| 32K | 36.0 tok/s | 35.0 tok/s | +2.9% |
| 64K | 24.7 tok/s | 24.1 tok/s | +2.5% |

Model tracks FLM within ~3% across all practical sequence lengths.

### 17.5 Strix Projections (20 GB/s Read -- Estimated)

Strix has approximately half the NOC bandwidth to the NPU. These projections
use 20 GB/s read bandwidth and 3 ms overhead. Note: these supersede the
memcpy-derived estimates in Section 16.4.

| Config | Seq 1K | Seq 4K | Seq 8K | Seq 16K | Seq 32K | Seq 64K |
|---|---|---|---|---|---|---|
| bf16 | **10.3** | 9.8 | 9.2 | 8.2 | 6.8 | 5.0 |
| bfp16 | **17.6** | 16.2 | 14.7 | 12.4 | 9.4 | 6.6 |
| INT4 | **35.1** | 30.0 | 25.2 | 19.0 | 12.8 | 8.2 |
| INT4+INT8 KV | **36.1** | 33.2 | 30.0 | 25.2 | 19.0 | 12.8 |

*(Values are tok/s.)*

### 17.6 Competitive Analysis

**At typical decode context (Seq 1K):**

| Implementation | Platform | Read BW | Config | Tok/s |
|---|---|---|---|---|
| **SOTA (FLM)** | **Krackan** | **40 GB/s** | **INT4+INT8 KV** | **64.5** |
| This work (projected) | Krackan | 40 GB/s | INT4+INT8 KV | **~65** |
| This work (projected) | Krackan | 40 GB/s | INT4 (bf16 KV) | **~64** |
| This work (projected) | Krackan | 40 GB/s | bfp16 (no dequant) | **~33** |
| This work (projected) | Krackan | 40 GB/s | bf16 | **~20** |
| This work (projected) | Strix | 20 GB/s | INT4+INT8 KV | **~36** |
| This work (projected) | Strix | 20 GB/s | bfp16 (no dequant) | **~18** |

**Key findings:**

1. **Our model validates against SOTA.** The INT4+INT8 KV projection matches FLM
   within 3% across all sequence lengths, confirming the bandwidth-bound analysis
   is correct. The entire performance curve is explained by a simple linear model:
   `Time = weights/BW + KV_traffic/BW + 3.1 ms`.

2. **Strix is significantly bandwidth-constrained.** At ~20 GB/s read (half the
   Krackan NOC), Strix INT4+INT8 KV tops out at ~36 tok/s -- roughly half of
   FLM's Krackan numbers. This is below the 60 tok/s conversational threshold
   at any precision.

3. **bfp16 on Krackan delivers ~33 tok/s with zero dequant effort.** This exceeds
   conversational speed (30 tok/s) without writing any quantization kernels. On
   Strix, bfp16 reaches only ~18 tok/s -- usable but not fast.

4. **INT4 on Krackan matches FLM.** Our traffic model shows that with full layer
   fusion (Phase 4) and INT4 quantization (Phase 5), we can match FLM's
   performance on Krackan. The remaining variable is overhead (~3 ms), which
   requires efficient single-design-per-layer execution.

5. **KV cache format matters more at short context than expected.** On Krackan,
   the difference between INT4 with bf16 KV (63.5 tok/s @ 1K) and INT4 with
   INT8 KV (65.1 tok/s @ 1K) is only 2.5%. The gap widens at longer contexts:
   at 32K, it's 24.7 vs 36.0 tok/s (46% improvement from INT8 KV).

6. **The Strix-to-Krackan jump is the largest single performance lever.** The 2x
   NOC bandwidth improvement delivers a consistent ~1.8x speedup across all
   configurations and sequence lengths (slightly less than 2x due to fixed
   overhead). This is a hardware improvement -- no software changes needed.

7. **Long-context on Strix is challenging.** At 16K context, even INT4+INT8 KV
   on Strix delivers only ~25 tok/s. For long-context applications, Krackan
   (46.8 tok/s @ 16K) or aggressive KV compression (INT4 KV) is required.
