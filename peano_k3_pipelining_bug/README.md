# Peano Pipelining Bug: Vectorized k3 SiLU Hangs at IC <= 16

## Summary

The vectorized 3x3 conv + SiLU kernel hangs (`ERT_CMD_STATE_TIMEOUT`) when
input channels (IC) is 8 or 16, but works correctly at IC >= 32. The hang
only occurs with **split compilation** — SiLU in a separate `.o`, linked
via `ld.lld -r`.

## Packed-Element Tiling (New)

The stride-1 path now uses **packed-element tiling**: each ObjectFIFO element
contains T+2 input rows / T output rows in a single contiguous buffer. The
input is zero-padded (1 row above + below), eliminating TOP/BOTTOM boundary
handling — all kernel calls use MIDDLE (check=1). This is mathematically
identical because `weight * 0 = 0`.

### Architecture

```
DDR (zero-padded input) ──→ Shim DMA ──→ ObjectFIFO (depth=2) ──→ Core
                                          [T+2 rows per element]
```

For L2bn (IC=16, OC=16, H=160, W=160, stride=1):
- **T=4**: 40 tiles, each 15360 bytes input / 10240 bytes output
- L1 budget: 54608 / 65536 bytes (fits)
- DDR overlap: 48% read overhead from 2-row overlap between tiles

### Performance Results

| Config | Time | Speedup | Status |
|--------|------|---------|--------|
| 1 column (baseline) | 1803 ms | 1.0x | PASS |
| 1 col + MemTile relay | 1802 ms | 1.0x | PASS |
| 1 col + MemTile join (2 shim DMAs) | 1802 ms | 1.0x | PASS |
| **2 columns (OC split)** | **902 ms** | **2.0x** | **PASS** |

### Performance Analysis

Instrumentation of `forward()` revealed **`run.wait()` accounts for 99.9%
of wall-clock time** (1801 ms out of 1803 ms). All host-side operations
(data conversion, buffer writes, XRT sync) total < 2 ms.

AIE Trace captured ~7800 cycles per vector iteration, estimating ~50M total
kernel cycles (~38 ms at 1.3 GHz). The remaining ~1760 ms is the core
**stalled on lock acquire** waiting for DMA transfers — the design is
DDR-bandwidth-bound.

**Multi-column is the only strategy that helps** because each column brings
independent shim DMA channels, genuinely doubling aggregate DDR bandwidth.
MemTile relay and MemTile join (2 shim DMAs → 1 core) do NOT help because
the single MemTile→Core DMA channel remains the bottleneck.

### Strategies Tested

| Strategy | Approach | Result | Why |
|----------|----------|--------|-----|
| Packed-element tiling | T+2 rows per FIFO element, zero-padded input | Correct, no speedup | Reduces DMA ops (160→40) but same bandwidth |
| MemTile relay (forward) | DDR→MemTile(depth=8)→Core(depth=2) | No improvement | Hides latency but bandwidth unchanged |
| MemTile join (2 shim DMAs) | 2 shim columns → join at MemTile → 1 core | No improvement | Bottleneck is MemTile→Core, not DDR→MemTile |
| **Multi-column (2 cols)** | OC split across 2 cores, each with own DMAs | **2x speedup** | Doubles both compute and DMA bandwidth |

## Setup

```bash
# From the IRON repo root:
source /scratch/jmelber/mlir-aie/ironenv/bin/activate
source /scratch/jmelber/mlir-aie/utils/env_setup.sh /scratch/jmelber/mlir-aie /opt/xrt

# Verify:
xrt-smi examine
python3 -c "from iron.operators.conv2d_int8.op import AIEConv2dInt8; print('OK')"
```

## Running the Benchmark

```bash
PYTHONPATH="/path/to/IRON:$PYTHONPATH"

# All layers (L0 stride-2, L1 stride-2, L2bn stride-1):
python3 peano_k3_pipelining_bug/benchmark.py --iters 5

# Single layer:
python3 peano_k3_pipelining_bug/benchmark.py --layer L2bn --iters 5

# Instrumented timing breakdown:
python3 peano_k3_pipelining_bug/instrument_forward.py

# AIE Trace profiling:
python3 peano_k3_pipelining_bug/trace_l2bn.py
```

## Running the Tests

Each test compiles the kernel, runs on the NPU, and verifies against a CPU
Pade-tanh SiLU golden reference.

```bash
python3 peano_k3_pipelining_bug/test_L0_k3s2_8ic_16oc_640.py
python3 peano_k3_pipelining_bug/test_L1_k3s2_16ic_32oc_320.py
python3 peano_k3_pipelining_bug/test_L2bn_k3s1_16ic_16oc_160.py
```

## Affected Layers

| Layer | Config              | IC | Stride | Output Size | Tiling | Status |
|-------|---------------------|----|--------|-------------|--------|--------|
| L0    | k3s2 8->16 640x640  |  8 | 2      | 320x320     | Per-row sliding window | PASS |
| L1    | k3s2 16->32 320x320 | 16 | 2      | 160x160     | Per-row sliding window | PASS |
| L2bn  | k3s1 16->16 160x160 | 16 | 1      | 160x160     | Packed-element T=4 | PASS |

Stride-2 layers keep the original per-row sliding window (3-line-pointer kernel).
Stride-1 layers use packed-element tiling with zero-padded input.

## Kernel Interface

### Stride-1 (packed-element, new)

```c
void conv2dk3_i8_silu(
    int8_t *input,              // (num_tiles * (tile_height+2)) rows contiguous
    int8_t *weights_and_bias,   // OC*IC*9 weights + OC*4 bias bytes
    int8_t *output,             // (num_tiles * tile_height) rows contiguous
    int32_t input_width,
    int32_t input_channels,
    int32_t output_channels,
    int32_t tile_height,        // T output rows per tile
    int32_t num_tiles,          // tiles per element (1 normal, 2 for join)
    int32_t shift1,
    int32_t shift2);
```

### Stride-2 (unchanged)

```c
void conv2dk3s2_i8_silu(
    int8_t *line0, int8_t *line1, int8_t *line2,
    int8_t *weights_and_bias, int8_t *output,
    int32_t input_width, int32_t input_channels,
    int32_t output_channels, int32_t check,
    int32_t shift1, int32_t shift2);
```

## Files

```
peano_k3_pipelining_bug/
├── README.md                                   This file
├── benchmark.py                                Vec vs scalar benchmark
├── instrument_forward.py                       Per-step timing breakdown
├── trace_l2bn.py                               AIE Trace cycle counting
├── conv2dk3_i8_silu_scalar_workaround.cc       Vectorized MAC (IC guard removed)
├── conv2dk3_i8_silu_force_scalar.cc            Force scalar MAC for comparison
├── silu_postproc_i8.cc                         SiLU in separate TU
├── test_L0_k3s2_8ic_16oc_640.py                L0 stride-2 test
├── test_L1_k3s2_16ic_32oc_320.py               L1 stride-2 test
└── test_L2bn_k3s1_16ic_16oc_160.py             L2bn stride-1 test

iron/operators/conv2d_int8/
├── op.py                                       Operator (solver, forward)
└── design.py                                   MLIR design (ObjectFIFO, TAPs)

aie_kernels/aie2p/
└── conv2dk3_i8_silu_split.cc                   Production kernel
```
