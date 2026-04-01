# Peano Pipelining Bug: Vectorized k3 SiLU Hangs at IC <= 16

## Summary

The vectorized 3x3 conv + SiLU kernel hangs (`ERT_CMD_STATE_TIMEOUT`) when
input channels (IC) is 8 or 16, but works correctly at IC >= 32. The hang
only occurs with **split compilation** — SiLU in a separate `.o`, linked
via `ld.lld -r`.

## Quick Start

```bash
# 1. Set up the IRON environment
python3 -m venv ironenv && source ironenv/bin/activate
source /opt/xilinx/xrt/setup.sh  # or wherever XRT is installed
pip install -r requirements.txt

# 2. Verify NPU hardware
xrt-smi examine

# 3. Run safe tests (scalar + vectorized IC>=32)
python3 peano_k3_pipelining_bug/reproduce.py

# 4. Run ALL tests including the ones that hang (will timeout at ~90s)
python3 peano_k3_pipelining_bug/reproduce.py --all

# 5. Run a single hanging test to see the bug
python3 peano_k3_pipelining_bug/reproduce.py --test ic8_vec_HANGS

# 6. Show the full test matrix
python3 peano_k3_pipelining_bug/reproduce.py --list
```

## Test Matrix

| Test                   | IC | OC | HxW      | S | Kernel   | Expected |
|------------------------|----|----|----------|---|----------|----------|
| ic8_scalar_PASS        |  8 | 16 | 640x640  | 2 | scalar   | PASS     |
| ic16s2_scalar_PASS     | 16 | 32 | 320x320  | 2 | scalar   | PASS     |
| ic16s1_scalar_PASS     | 16 | 16 | 160x160  | 1 | scalar   | PASS     |
| ic32_vec_PASS          | 32 | 64 | 160x160  | 2 | **vec**  | PASS     |
| ic64_vec_PASS          | 64 |128 |  80x80   | 2 | **vec**  | PASS     |
| ic8_vec_HANGS          |  8 | 16 | 640x640  | 2 | **vec**  | **HANG** |
| ic16s2_vec_HANGS       | 16 | 32 | 320x320  | 2 | **vec**  | **HANG** |
| ic16s1_vec_HANGS       | 16 | 16 | 160x160  | 1 | **vec**  | **HANG** |

All tests verify NPU output against a CPU reference (Pade tanh SiLU).
The "vec" tests use the bug kernel (`conv2dk3_i8_silu_bug.cc`) which has
the IC guard removed, forcing the vectorized path at all IC values.

## Bug Details

**Symptom**: `ERT_CMD_STATE_TIMEOUT` — NPU hardware never completes.
The core enters an infinite loop in the vectorized MAC+SiLU loop body.

**Trigger conditions** (all must be true):
1. Split compilation: MAC in one `.o`, SiLU (`apply_silu_i8`) in another,
   partial-linked with `ld.lld -r`
2. IC <= 16 (1-2 ic_groups in the inner MAC loop)
3. Vectorized path using `aie::mmul<8,8,8,int8,int8>`

**Does NOT hang when**:
- IC >= 32 (4+ ic_groups) — works correctly with split compilation
- Scalar MAC path (element-by-element C loops) — always works
- Co-compiled SiLU (noinline, same `.cc` file) — works but SiLU is 100x
  slower due to Peano codegen degradation when tanh intrinsics are visible
  alongside MMUL code

## Compilation Commands

The bug kernel is compiled with these exact Peano flags:

```bash
PEANO=/path/to/peano  # typically inside mlir-aie install
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

## Code Structure

The vectorized loop that hangs (simplified from `conv2dk3_i8_silu_bug.cc`):

```cpp
// In conv2dk3_i8_silu_vec_mid_v2():
for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
    for (int vi_base = 0; vi_base < vec_iters; vi_base += MAX_VI) {
        for (int vi = vi_base; vi < vi_end; vi++) {
            MMUL acc = zeros();
            // MAC: at IC=8, this is just 1 iteration per kh row
            for kh in {0,1,2}:
                mac_kh_row_s1<8>(acc, line[kh], weights, ...);
                //              ^^^ only 1 ic_group — trivially fast

            // Extract + extern SiLU (from silu_postproc_i8.o, ~5us)
            store(lo8_buf, acc.to_vector<int8>(shift1));
            store(hi8_buf, acc.to_vector<int8>(shift1 + 8));
            apply_silu_i8(lo8_buf, hi8_buf, bias, ...);  // extern call
            store(output + ..., load(out_buf));
        }
    }
}
```

At IC=8 the loop body is very fast (tiny MAC + fast extern SiLU). Peano
appears to auto-pipeline this loop and generate broken control flow.

## What We Tried

| Approach | Result |
|----------|--------|
| Loop chunking (MAX_VI = 4, 8, 12) | Still hangs |
| `[[clang::optnone]]` on vec functions | Not supported on AIE target |
| Co-compiled SiLU (noinline, same TU) | Works but SiLU is 100x slower |
| Scalar MAC fallback | Works (current workaround) |

## Files

```
peano_k3_pipelining_bug/
├── README.md                       This file
├── reproduce.py                    Test harness (uses IRON operator framework)
├── conv2dk3_i8_silu_bug.cc         MAC kernel with IC guard REMOVED (triggers hang)
└── silu_postproc_i8.cc             SiLU post-processor (separate TU, extern "C")
```

The guarded (working) version of the MAC kernel lives in the main repo at
`aie_kernels/aie2p/conv2dk3_i8_silu_split.cc` with `input_channels > 16`
in the dispatch condition.
