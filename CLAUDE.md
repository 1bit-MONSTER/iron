# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

IRON is a Python API for programming AMD Ryzen AI NPUs (Neural Processing Units). It wraps the MLIR-AIE dialect to enable writing high-performance ML operators targeting NPU hardware. The project includes 22 pre-built operators and a Llama 3.2 1B inference application.

## Common Commands

### Setup
```bash
python3 -m venv ironenv && source ironenv/bin/activate
source /opt/xilinx/xrt/setup.sh
pip install -r requirements.txt
```

### Testing
```bash
# Run quick test suite (smoke tests only)
pytest iron/operators/ -m "not extensive"

# Run full test suite (all parameter sweeps)
pytest iron/operators/

# Run a single operator's tests
pytest iron/operators/gemm/test.py

# Run a single test function
pytest iron/operators/gemm/test.py::test_gemm

# Run application tests
pytest iron/applications/

# Run all tests
pytest
```

### Linting & Formatting
```bash
# Python formatting (black, default 88-char line width)
black --check .        # check
black .                # fix

# C++ formatting (clang-format, LLVM-based, 120-char column limit)
python scripts/clang-format-wrapper.py --check   # check
python scripts/clang-format-wrapper.py --fix     # fix

# License compliance (SPDX headers required on all files)
reuse lint
```

## Definition of Done

An operator or feature is **not done** until it:
1. **Compiles** — MLIR generation, kernel .o, xclbin, and instruction .bin all build without errors
2. **Runs on hardware** — Executes on the NPU without hangs, timeouts, or ERT_CMD_STATE errors
3. **Passes verification** — Output matches the CPU golden reference within specified tolerances

Code that only generates MLIR or only compiles is not a deliverable. The bar is a passing `pytest` that exercises the full pipeline: compile → load → execute → verify. No exceptions.

## Architecture

### Operator Pattern
Every operator in `iron/operators/<name>/` follows a 4-file convention:
- **`op.py`** — Python operator class (extends `AIEOperatorBase`), the user-facing API
- **`design.py`** — NPU hardware design using MLIR-AIE DSL (tile mapping, data movement, kernel binding)
- **`reference.py`** — CPU reference implementation for golden-value testing
- **`test.py`** — Parametrized pytest tests comparing NPU output against the reference

### Core Infrastructure (`iron/common/`)
- **`aie_base.py`** — `AIEOperatorBase` abstract class: kernel/buffer registration, runlist execution, buffer I/O
- **`aie_context.py`** — `AIEContext` singleton orchestrating operator lifecycle: compilation, runtime prep, device management
- **`compilation.py`** — Artifact-based build system with dependency tracking and caching (singleton per absolute path). Key classes: `SourceArtifact`, `XclbinArtifact`, `InstsBinArtifact`, `KernelObjectArtifact`
- **`aie_device_manager.py`** — XRT runtime integration for hardware device management
- **`test_utils.py`** — `run_test()` and `verify_buffer()` helpers used by all operator tests

### AIE Kernels (`aie_kernels/`)
Low-level C/C++ compute kernels organized by hardware generation:
- `generic/` — Architecture-agnostic implementations
- `aie2/` — AIE2 optimized
- `aie2p/` — AIE2+ optimized

### Applications (`iron/applications/`)
End-to-end applications (e.g., Llama 3.2 1B) that compose multiple operators.

### Key Dependencies
- **mlir-aie** — MLIR dialect bindings (`from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker`)
- **llvm-aie (Peano)** — Low-level compiler backend
- **XRT** — Xilinx Runtime for hardware execution (loaded via `source /opt/xilinx/xrt/setup.sh`)
- **torch, numpy, ml_dtypes** — Data types and tensor operations (primary dtype: `bfloat16`)

## CI

Three CI pipelines run on GitHub Actions:
1. **ci-lint** (every push/PR) — black, clang-format, reuse lint
2. **small** (PRs + devel/main) — quick operator tests (`-m "not extensive"`)
3. **extensive** (daily + manual) — full parameter sweep tests

## Code Conventions

- All files require SPDX license headers:
  ```
  SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
  SPDX-License-Identifier: Apache-2.0
  ```
- PR target branch is `devel`
- C++ style: LLVM-based, 120-char columns, 4-space indent, Linux brace style
- Python style: black defaults (88-char lines)
- Test metrics are collected via `conftest.py` into CSV format for regression tracking

## AIE Development Tips

### Hardware Constraints
- **AIE tile L1 memory: 64 KB.** ObjectFIFO buffers, stack, and static data all share this. Budget carefully when designing multi-FIFO operators. Use `dequant/design.py` as a reference: 16384 bf16 elements (32 KB) is half of L1.
- **DMA channels per compute tile: 2 input + 2 output.** Each ObjectFIFO consumer or producer counts as one channel. A design with 3 input FIFOs per tile will fail with `'aie.tile' op number of input DMA channel exceeded!`. Plan FIFO count around this limit.
- **One `.o` binary per Worker.** MLIR-AIE enforces `ValueError: Currently, only one binary per works is supported`. If you need functions from multiple source files, combine them into a single `.cc` file.
- **ShimDMA channels are limited.** The `SequentialPlacer` will fail with `Failed to find a tile matching column N` if the total FIFO count across columns exceeds available shim resources. Reduce `num_aie_columns` if this happens.

### Kernel Development
- **AIE2 vs AIE2+ tanh:** AIE2 (`aie_kernels/aie2/`) uses LUT-based `getTanhBf16()` from `lut_based_ops.h`. AIE2+ (`aie_kernels/aie2p/`) uses hardware `aie::tanh<bfloat16>(float_vec)`. Always implement both variants.
- **Static buffers need alignment.** If a kernel uses `aie::load_v<N>()` or `aie::begin_restrict_vector<N>()` on static arrays, add `__attribute__((aligned(64)))`. Misaligned vector access reads from wrong addresses silently.
- **bf16 tanh saturates for |x| > 8.** `tanh(x/2)` in bf16 returns exactly -1.0 or 1.0, making `sigmoid(x) = 0` or `1`. This means `silu(x) = 0` for x < -8. This is expected — match tolerances to the standalone SiLU operator (`abs_tol=1.0` for composed operators).
- **Static kernel buffers work** for scratch space that doesn't need DMA. Use them to hold intermediate results between kernel phases within the same core body. They avoid ObjectFIFO overhead but don't show up in the MLIR buffer address map — verify no overlap by checking total L1 usage.
- **`matvec_vectorized` uses `r=64` SIMD lanes** with `aie::mac` + `aie::reduce_add`. The inner loop requires `k >= 2*r = 128` for pipelining (see `AIE_LOOP_MIN_ITERATION_COUNT(2)`).

### Design Patterns
- **Composing operators in SwiGLU-style pipelines:** Use `get_artifacts(prefix=)` to create uniquely-named artifacts. Chain xclbins via `xclbin.xclbin_input` and `xclbin.depends`. Assign unique kernel IDs (`--xclbin-kernel-id=0x90N`).
- **Pre-interleaving weights for shared FIFOs:** When a single A FIFO must carry data from two DDR buffers (e.g., W1 and W2 for dual-GEMV), pre-interleave in Python at setup time. The core body consumes tiles in FIFO order — structure the interleaving to match. Use a `phase` parameter in the kernel to select the destination buffer.
- **Two `rt.fill()` calls to the same FIFO in a `task_group` have NO ordering guarantee.** The task_group only controls await/free bookkeeping. If you need ordered fills, either pre-interleave in DDR or use separate FIFOs (subject to DMA channel limits).

### Testing & Debugging
- **Always `rm -rf build/<operator>_*` when changing kernels or designs.** The build system caches `.xclbin` and `.bin` artifacts by filename. Stale artifacts cause confusing failures including `ERT_CMD_STATE_TIMEOUT` hangs.
- **Verify the reference separately.** Before debugging hardware mismatches, check that the Python reference produces correct values at the failing indices. Use `torch.manual_seed` for reproducibility.
- **Isolate components.** If a fused operator fails, test each component standalone first (e.g., test GEMV alone with the same data, test SiLU+Mul alone). The standard GEMV test at `iron/operators/gemv/test.py` is a reliable baseline.
- **Tolerance ladder for composed operators:** Standalone elementwise ops use `rel_tol=0.04, abs_tol=1e-6`. Multi-kernel pipelines (SwiGLU) use `rel_tol=0.07, abs_tol=0.7` to `1.0` because bf16 rounding errors accumulate through GEMV + activation + multiply.
- **`ERT_CMD_STATE_TIMEOUT`** usually means the core body is deadlocked waiting on a FIFO acquire that will never be filled (DMA misconfiguration) or the design doesn't terminate. Check that fill/drain counts match the core body's acquire/release counts.
- **XRT may be a system package** (no `/opt/xilinx/xrt/setup.sh`). If `pyxrt` isn't found in a venv, symlink it: `ln -s /usr/lib/python3/dist-packages/pyxrt.*.so ironenv/lib/python3.12/site-packages/`
- **Inspect generated MLIR** by calling the design function directly: `python3 -c "from iron.operators.foo.design import my_foo; print(my_foo('npu2', ...))"`. Check ObjectFIFO declarations, tile assignments, and DMA channel usage before running on hardware.
- **aiecc flag for NPU instruction generation is `--aie-generate-npu-insts`** (NOT the old `--aie-generate-npu`). The C++ aiecc silently ignores the old flag via LLVM `cl::opt`, returns exit code 0 with "Compilation completed successfully", but never writes the `.bin` file. If `.bin` files aren't being generated despite successful compilation, check this flag in `iron/common/compilation.py`.
- **`AIE_PREPARE_FOR_PIPELINING` + runtime-variable outer loop = incorrect codegen.** If an inner loop with `[[chess::prepare_for_pipelining]]` sits inside an outer loop whose trip count depends on a runtime parameter (e.g., `check`), the Chess compiler generates incorrect hardware code. The scalar implementation runs correctly. Always validate vectorized kernels against the scalar fallback.
- **DMA BD size fields are limited to 1023.** Use 4D TAP dimensions to decompose large transfers. Each TAP dimension size must be ≤ 1023. Stride fields have larger limits (~20 bits). For conv/pooling with large channel counts, decompose rows as `[n_channel_groups, channel_group_row_size]`.
- **Sliding window `acquire(N)` with N≥5 may deadlock.** A safer pattern for large kernel pooling: send `kernel_size` contiguous rows as a single FIFO element (a "strip") using strided DMA, then the core does `acquire(1)` per output row. This avoids the complex acquire/release bookkeeping.
- **L1 budget with double-buffered strip FIFOs:** strip_size × 2 (double-buffer) + output_row × 2 + stack (1KB) must fit in 64KB. For 128ch×24w×5rows = 30KB per strip, double-buffered = 60KB — dangerously close. Tile channels across cores for large layers.
- **80 output channels can't be multi-column tiled.** 80/N must be a multiple of 8 for the per-core channel count, but 80/2=40, 80/4=20, 80/8=10 — none are multiples of 8. For 3×3 convs with 80 output channels and large input channels, weights exceed L1. Requires weight streaming through MemTile or padding to 88ch.
- **Auto-column selection via `_auto_columns()`**: Use `num_aie_columns=0` in block constructors (CBS, C2f, Bottleneck, DetectBranch) to auto-select the smallest column count where per-core weight fits in 40KB and per-core output channels are a multiple of 8. Always pass 0 (auto) unless you have a specific reason.
- **NPU hardware context exhaustion:** Running many tests in one pytest session causes `DRM_IOCTL_AMDXDNA_CREATE_HWCTX` errors. Each `aie_context` opens separate hardware contexts. Run extensive tests individually (`-k test_name`) or limit concurrent contexts.
