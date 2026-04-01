# Peano Pipelining Bug: Vectorized k3 SiLU Hangs at IC <= 16

## Summary

The vectorized 3x3 conv + SiLU kernel hangs (`ERT_CMD_STATE_TIMEOUT`) when
input channels (IC) is 8 or 16, but works correctly at IC >= 32. The hang
only occurs with **split compilation** — SiLU in a separate `.o`, linked
via `ld.lld -r`.

## Setup

```bash
# From the IRON repo root:
python3 -m venv ironenv && source ironenv/bin/activate
pip install -r requirements.txt
source /opt/xlinx/xrt/setup.sh

# Verify:
xrt-smi examine
python3 -c "from iron.operators.conv2d_int8.op import AIEConv2dInt8; print('OK')"
```

## Running the Tests

Each test is a standalone script for one affected YOLOv8n layer.
Each compiles the kernel, runs on the NPU, and verifies against a CPU
Pade-tanh SiLU golden reference.

By default, tests use the **vectorized** kernel (no IC guard) and will
**hang** to demonstrate the bug. Pass `--scalar` to use the scalar MAC
workaround, which runs correctly but slowly.

```bash
# --- Demonstrate the bug (HANGS, timeout ~90s) ---
python3 peano_k3_pipelining_bug/test_L0_k3s2_8ic_16oc_640.py
python3 peano_k3_pipelining_bug/test_L1_k3s2_16ic_32oc_320.py
python3 peano_k3_pipelining_bug/test_L2bn_k3s1_16ic_16oc_160.py

# --- Verify scalar workaround (PASSES, but slow) ---
python3 peano_k3_pipelining_bug/test_L0_k3s2_8ic_16oc_640.py --scalar
python3 peano_k3_pipelining_bug/test_L1_k3s2_16ic_32oc_320.py --scalar
python3 peano_k3_pipelining_bug/test_L2bn_k3s1_16ic_16oc_160.py --scalar
```

The two kernel variants:
- `conv2dk3_i8_silu_bug.cc` — vectorized dispatch for all IC (**hangs** at IC<=16)
- `conv2dk3_i8_silu_scalar_workaround.cc` — adds `input_channels > 16` guard (**passes**)

## Affected Layers

| Layer | Config              | IC | ic_groups | Output Size | Status    |
|-------|---------------------|----|-----------|-------------|-----------|
| L0    | k3s2 8->16 640x640  |  8 | 1         | 320x320     | **HANGS** |
| L1    | k3s2 16->32 320x320 | 16 | 2         | 160x160     | **HANGS** |
| L2bn  | k3s1 16->16 160x160 | 16 | 2         | 160x160     | **HANGS** |

These are the first three conv layers of the YOLOv8n backbone. All
subsequent layers have IC >= 32 and work correctly with the same kernel.

## Bug Details

**Symptom**: `ERT_CMD_STATE_TIMEOUT` — NPU core enters infinite loop.

**Trigger conditions** (all required):
1. Split compilation: MAC in `conv2dk3_i8_silu_bug.cc`, SiLU in
   `silu_postproc_i8.cc`, partial-linked with `ld.lld -r`
2. IC <= 16 (1-2 ic_groups in the inner MAC loop)
3. Vectorized path using `aie::mmul<8,8,8,int8,int8>`

**Does NOT hang when**:
- IC >= 32 (4+ ic_groups) — same kernel, same compilation, works fine
- Scalar MAC path — always correct
- Co-compiled SiLU (noinline, same `.cc` file) — works but SiLU runs
  100x slower due to Peano codegen degradation with tanh intrinsics

## Compilation Commands

```bash
PEANO=/path/to/peano  # inside mlir-aie install
MLIR_AIE=/path/to/mlir-aie

# 1. Compile MAC kernel (declares extern "C" apply_silu_i8)
$PEANO/bin/clang++ -O2 -std=c++20 --target=aie2p-none-unknown-elf \
    -Wno-parentheses -Wno-attributes -Wno-macro-redefined \
    -Wno-empty-body -Wno-missing-template-arg-list-after-template-kw \
    -I$MLIR_AIE/include \
    -DINT8_ACT -ffunction-sections -fdata-sections \
    -c conv2dk3_i8_silu_bug.cc -o conv2dk3_i8_silu_bug.o

# 2. Compile SiLU post-processor (defines extern "C" apply_silu_i8)
$PEANO/bin/clang++ -O2 -std=c++20 --target=aie2p-none-unknown-elf \
    -Wno-parentheses -Wno-attributes -Wno-macro-redefined \
    -Wno-empty-body -Wno-missing-template-arg-list-after-template-kw \
    -I$MLIR_AIE/include \
    -DINT8_ACT -ffunction-sections -fdata-sections \
    -c silu_postproc_i8.cc -o silu_postproc_i8.o

# 3. Partial-link into single relocatable .o
$PEANO/bin/ld.lld -r conv2dk3_i8_silu_bug.o silu_postproc_i8.o \
    -o conv2dk3_i8_silu.o
```

## Key Code Path

The vectorized loop that hangs (from `conv2dk3_i8_silu_bug.cc`):

```cpp
void conv2dk3_i8_silu_vec_mid_v2(...) {
    constexpr int NUM_W = 8;
    const int vec_iters = input_width / NUM_W;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int vi = 0; vi < vec_iters; vi++) {
            MMUL acc = zeros();

            // At IC=8: only 1 ic_group per kh row — trivially fast
            for (int ic_g = 0; ic_g < ic_groups; ic_g++) {  // 1 iteration!
                acc.mac(input_vec, weight_vec);
            }
            // ... repeat for kh=0,1,2 ...

            // Extern SiLU call (~5us, from silu_postproc_i8.o)
            apply_silu_i8(lo8_buf, hi8_buf, bias, oc_g, out_buf, ...);
        }
    }
}
```

## What We Tried

| Approach | Result |
|----------|--------|
| Loop chunking (MAX_VI = 4, 8, 12) | Still hangs |
| Co-compiled SiLU (noinline, same TU) | Works but 100x slower SiLU |
| Scalar MAC fallback | Works (current workaround, 50-100x slower) |

## Files

```
peano_k3_pipelining_bug/
├── README.md                                   This file
├── conv2dk3_i8_silu_bug.cc                     MAC kernel, IC guard REMOVED (HANGS)
├── conv2dk3_i8_silu_scalar_workaround.cc       MAC kernel, IC>16 guard (PASSES)
├── silu_postproc_i8.cc                         SiLU in separate TU (shared by both)
├── test_L0_k3s2_8ic_16oc_640.py                L0 test (--scalar for workaround)
├── test_L1_k3s2_16ic_32oc_320.py               L1 test (--scalar for workaround)
└── test_L2bn_k3s1_16ic_16oc_160.py             L2bn test (--scalar for workaround)
```
