# AIE API Reference & Kernel Optimization Guide

A comprehensive reference for writing correct, high-performance AIE compute kernels
targeting AMD Ryzen AI NPUs (AIE2 and AIE2+ architectures).

Based on the [AIE API](https://xilinx.github.io/aie_api/) (a C++ header-only library)
and hard-won lessons from the IRON operator kernels in `aie_kernels/aie2p/`.

---

## Table of Contents

1. [Vector Types and Operations](#1-vector-types-and-operations)
2. [Accumulator Types](#2-accumulator-types)
3. [Matrix Multiply-Accumulate (MMUL)](#3-matrix-multiply-accumulate-mmul)
4. [Activation Functions](#4-activation-functions)
5. [Data Layout Patterns](#5-data-layout-patterns)
6. [Performance Optimization](#6-performance-optimization)
7. [Common Pitfalls and Known Bugs](#7-common-pitfalls-and-known-bugs)
8. [Working Code Templates](#8-working-code-templates)
9. [AIE2 vs AIE2+ Differences](#9-aie2-vs-aie2p-differences)
10. [Quick Reference Tables](#10-quick-reference-tables)

---

## 1. Vector Types and Operations

### 1.1 Core Vector Type

```cpp
#include <aie_api/aie.hpp>

aie::vector<T, N>
```

**Supported element types (`T`):**

| Type | Size | Notes |
|------|------|-------|
| `int8` / `int8_t` | 8-bit | Primary quantized type |
| `uint8` / `uint8_t` | 8-bit | Used for LUT indices |
| `int16` / `int16_t` | 16-bit | Intermediate precision |
| `int32` / `int32_t` | 32-bit | Accumulator extraction |
| `bfloat16` | 16-bit | Primary floating-point type |
| `float` | 32-bit | Full precision float |

**Supported vector sizes (`N`):**

Vector sizes must be powers of 2 and fill at least one 256-bit or 512-bit register.
Typical sizes by type:

| Type | Common Sizes | Notes |
|------|-------------|-------|
| `int8` | 16, 32, 64, 128 | 64 = one 512-bit register |
| `int16` | 8, 16, 32, 64 | 32 = one 512-bit register |
| `int32` | 4, 8, 16, 32 | 16 = one 512-bit register |
| `bfloat16` | 8, 16, 32, 64 | 16 = one 256-bit register |
| `float` | 4, 8, 16, 32 | 8 = one 256-bit register |

### 1.2 Load and Store

**Aligned load/store (preferred):**

```cpp
// Load N elements from aligned pointer
aie::vector<T, N> v = aie::load_v<N>(ptr);

// Store N elements to aligned pointer
aie::store_v(ptr, v);
```

**CRITICAL alignment requirements:**
- `aie::load_v<N>` requires the pointer to be aligned to `N * sizeof(T)` bytes.
- For `int8` with N=64: requires 64-byte alignment.
- For `bfloat16` with N=16: requires 32-byte alignment.
- Misaligned loads **silently read from wrong addresses** -- no runtime error.

**Unaligned load (slower, use sparingly):**

```cpp
aie::vector<T, N> v = aie::load_unaligned_v<N>(ptr);
```

**Cast-based load (raw intrinsic pattern):**

```cpp
// Legacy pattern -- still works, faster for some cases
v32bfloat16 input = *(v32bfloat16 *)(ptr + offset);
*(v32bfloat16 *)(out + offset) = output;
```

### 1.3 Vector Construction

```cpp
// Broadcast a scalar to all elements
aie::vector<bfloat16, 16> v = aie::broadcast<bfloat16, 16>(0.5f);

// Zero vector
aie::vector<bfloat16, 16> z = aie::zeros<bfloat16, 16>();

// Concatenate two half-sized vectors into one
aie::vector<int8, 32> lo = ...;
aie::vector<int8, 32> hi = ...;
aie::vector<int8, 64> full = aie::concat(lo, hi);
```

### 1.4 Element Access

```cpp
// Read element (scalar -- avoid in hot loops)
T val = v[index];

// Extract sub-vector
aie::vector<T, N/2> sub = v.extract<N/2>(0);  // first half
aie::vector<T, N/2> sub = v.extract<N/2>(1);  // second half
```

### 1.5 Shuffle Operations

Shuffle operations are essential for convolution kernels that need to create
shifted input views for different kernel window positions.

```cpp
// Shift elements up by `count`, filling vacated positions from `fill`
aie::vector<T, N> result = aie::shuffle_up_fill(v, fill, count);
// Elements: [fill[N-count], ..., fill[N-1], v[0], ..., v[N-count-1]]
// Inserts `count` elements from the END of `fill` at the BEGINNING.

// Shift elements down by `count`, filling vacated positions from `fill`
aie::vector<T, N> result = aie::shuffle_down_fill(v, fill, count);
// Elements: [v[count], ..., v[N-1], fill[0], ..., fill[count-1]]
// Inserts `count` elements from the START of `fill` at the END.
```

**Practical use case -- stride-1 convolution border handling:**

```cpp
// For kw=0 (left neighbor): shift center vector up by one position (8 bytes)
// fill with data from the preceding chunk, or zeros for left border
aie::vector<int8, 64> v_left;
if (vi > 0) {
    v_left = aie::shuffle_up_fill(
        v_center,
        aie::load_v<64>(line_ptr + (x_base - NUM_W) * 8),
        8);  // shift by 8 elements = 1 spatial position * 8 channels
} else {
    v_left = aie::shuffle_up_fill(v_center, zeros_v, 8);
}

// For kw=2 (right neighbor): shift center vector down by one position
aie::vector<int8, 64> v_right;
if (x_base + NUM_W < input_width) {
    v_right = aie::shuffle_down_fill(
        v_center,
        aie::load_v<64>(line_ptr + (x_base + NUM_W) * 8),
        8);
} else {
    v_right = aie::shuffle_down_fill(v_center, zeros_v, 8);
}
```

### 1.6 Filter and Interleave

```cpp
// filter_even: extract even-indexed groups
// From [G0, G1, G2, G3, G4, G5, G6, G7] -> [G0, G2, G4, G6]
aie::vector<int8, 32> evens = aie::filter_even(v64, chunk_size);

// filter_odd: extract odd-indexed groups
// From [G0, G1, G2, G3, G4, G5, G6, G7] -> [G1, G3, G5, G7]
aie::vector<int8, 32> odds = aie::filter_odd(v64, chunk_size);

// interleave_zip: duplicate each element (for upsampling)
// From [A, B] -> lo=[A, A], hi=[B, B]  (with chunk_size=8 for channel groups)
auto [lo, hi] = aie::interleave_zip(v, v, chunk_size);
```

**Use case -- stride-2 convolution gather:**

```cpp
// Extract even/odd spatial positions for stride-2 processing
inline void stride2_gather(
    const aie::vector<int8, 64> &vec_lo,
    const aie::vector<int8, 64> &vec_hi,
    aie::vector<int8, 64> &v_even,
    aie::vector<int8, 64> &v_odd) {
    aie::vector<int8, 32> lo_even = aie::filter_even(vec_lo, 8);
    aie::vector<int8, 32> lo_odd  = aie::filter_odd(vec_lo, 8);
    aie::vector<int8, 32> hi_even = aie::filter_even(vec_hi, 8);
    aie::vector<int8, 32> hi_odd  = aie::filter_odd(vec_hi, 8);
    v_even = aie::concat(lo_even, hi_even);
    v_odd  = aie::concat(lo_odd, hi_odd);
}
```

### 1.7 Elementwise Arithmetic

```cpp
// All return aie::vector or aie::accum depending on types
aie::vector<T, N> c = aie::add(a, b);
aie::vector<T, N> c = aie::sub(a, b);

// mul returns accum when mixing types, vector<T,N> when same type for bf16
auto c = aie::mul(a, b);  // may return accum<accfloat, N>

// Comparison / selection
aie::vector<T, N> c = aie::max(a, b);
aie::vector<T, N> c = aie::min(a, b);

// Reduction
T val = aie::reduce_add(v);
T val = aie::reduce_max(v);
T val = aie::reduce_min(v);
```

### 1.8 Special Math Functions

```cpp
// Square root of each element's reciprocal (fast, hardware-accelerated)
float val = aie::invsqrt(x);

// Inverse (1/x)
float val = aie::inv(x);
aie::vector<bfloat16, N> v = aie::inv(bf16_vec);

// Division (slow -- avoid in hot loops)
float val = aie::div(a, b);

// Float conversion helper
float val = aie::to_float(int_val);

// Square each element and return float
aie::vector<float, N> sq = aie::mul_square(bf16_vec);
```

### 1.9 Iterators

Iterators provide auto-incrementing aligned access. Preferred for sequential
processing in elementwise kernels.

```cpp
// Restrict iterator (tells compiler no aliasing)
auto it_in  = aie::begin_restrict_vector<16>((bfloat16 *)input);
auto it_out = aie::begin_restrict_vector<16>((bfloat16 *)output);

// Const restrict iterator (read-only)
auto it_in = aie::cbegin_restrict_vector<16>((bfloat16 *)input);

// Usage: dereference and increment
aie::vector<bfloat16, 16> v = *it_in++;
*it_out++ = result;
```

**CRITICAL: iterator vector size determines alignment.**
Using `begin_restrict_vector<16>` with `bfloat16` means 32-byte alignment.
The pointer MUST be aligned to `16 * sizeof(bfloat16) = 32` bytes.

---

## 2. Accumulator Types

### 2.1 Core Accumulator Type

```cpp
aie::accum<Tag, N>
```

**Supported accumulator tags:**

| Tag | Bit Width | Use Case |
|-----|-----------|----------|
| `acc32` | 32-bit | int8 x int8 MAC results |
| `acc64` | 64-bit | int16 x int16 MAC results |
| `accfloat` | 32-bit float | bfloat16 MAC results, exp/tanh output |
| `accauto` | Auto-selected | Let compiler choose based on input types |

### 2.2 Accumulator Construction

```cpp
// Zero-initialized accumulator
aie::accum<accfloat, 16> acc = aie::zeros<accfloat, 16>();

// From a vector
aie::accum<accfloat, 8> acc;
acc.from_vector(float_vec, shift);  // shift=0 for floating-point

// From a vector directly (bfloat16 -> accfloat)
aie::accum<accfloat, 16> acc(bf16_vec);
```

### 2.3 Accumulator Extraction

```cpp
// Extract to vector with optional shift (SRS = Shift-Round-Saturate)
aie::vector<int8, 64>     v = acc.to_vector<int8>(shift);    // WORKS correctly
aie::vector<bfloat16, 16> v = acc.to_vector<bfloat16>();     // WORKS correctly
aie::vector<float, 8>     v = acc.to_vector<float>();        // WORKS correctly

// CRITICAL BUG: to_vector<int32>(0) on AIE2p with Peano/LLVM
// produces WRONG element ordering. See Section 7.2 for workaround.
aie::vector<int32, 64> v = acc.to_vector<int32>(0);          // BROKEN ordering
```

### 2.4 Accumulator Arithmetic

```cpp
// Accumulate with multiply
aie::accum<accfloat, 16> acc = aie::mul(a, b);  // initial multiply
acc = aie::add(acc, vec);                         // add vector to accum

// Sub: returns new accum
aie::accum<accfloat, N> diff = aie::sub(acc1, acc2_or_vec);
```

---

## 3. Matrix Multiply-Accumulate (MMUL)

### 3.1 MMUL Template

```cpp
using MMUL = aie::mmul<M, K, N, TypeA, TypeB, AccumTag>;
```

- `M x K`: dimensions of the A matrix tile
- `K x N`: dimensions of the B matrix tile
- `M x N`: dimensions of the output C tile
- `TypeA`, `TypeB`: input element types
- `AccumTag`: accumulator type (default: `accauto`)

### 3.2 Supported MMUL Shapes

**int8 x int8:**

| Shape (M,K,N) | size_A | size_B | size_C | Notes |
|---------------|--------|--------|--------|-------|
| 8, 8, 8 | 64 | 64 | 64 | **Primary shape for AIE2/AIE2+** |

**int16 x int16:**

| Shape (M,K,N) | size_A | size_B | size_C | Notes |
|---------------|--------|--------|--------|-------|
| 4, 4, 8 | 16 | 32 | 32 | Primary shape |

**bfloat16 x bfloat16 (standard):**

| Shape (M,K,N) | size_A | size_B | size_C | Notes |
|---------------|--------|--------|--------|-------|
| 4, 8, 8 | 32 | 64 | 32 | **Standard bf16 mmul** |

**bfloat16 x bfloat16 (with BFP16 emulation):**

| Shape (M,K,N) | size_A | size_B | size_C | Notes |
|---------------|--------|--------|--------|-------|
| 8, 8, 8 | 64 | 64 | 64 | Requires `-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16` |

### 3.3 MMUL Usage Pattern

```cpp
using MMUL = aie::mmul<4, 8, 8, bfloat16, bfloat16>;

// Initialize
MMUL acc;
acc = aie::zeros<accfloat, MMUL::size_C>();

// Or initialize from existing partial results
aie::vector<bfloat16, MMUL::size_C> prev = aie::load_v<MMUL::size_C>(c_ptr);
MMUL acc(prev);

// MAC loop
for (int i = 0; i < K_iters; i++) {
    aie::vector<bfloat16, MMUL::size_A> a = aie::load_v<MMUL::size_A>(a_ptr);
    aie::vector<bfloat16, MMUL::size_B> b = aie::load_v<MMUL::size_B>(b_ptr);
    acc.mac(a, b);
    a_ptr += MMUL::size_A;
    b_ptr += MMUL::size_B;
}

// Extract result
aie::vector<bfloat16, MMUL::size_C> result = acc.to_vector<bfloat16>();
aie::store_v(c_ptr, result);
```

### 3.4 2x2 MMUL Expansion (Optimal Pattern)

The highest-efficiency pattern expands the basic MMUL tile 2x in both M and N
dimensions, computing 4 output tiles (C00, C01, C10, C11) per iteration.
This maximizes accumulator register utilization and instruction-level parallelism.

```cpp
template <typename T_in, typename T_out, unsigned rowA, unsigned colA, unsigned colB,
          unsigned r, unsigned s, unsigned t>
void matmul_vectorized_2x2(const T_in *__restrict pA,
                            const T_in *__restrict pB,
                            T_out *__restrict pC) {
    using MMUL = aie::mmul<r, s, t, T_in, T_in, accauto>;

    for (unsigned z = 0; z < rowA; z += 2)
        chess_prepare_for_pipelining chess_loop_range(4, )
        {
            T_out *pC1 = pC + (z * colB) * MMUL::size_C;
            T_out *pC2 = pC + ((z + 1) * colB) * MMUL::size_C;

            for (unsigned j = 0; j < colB; j += 2) {
                const T_in *pA1 = pA + (z * colA) * MMUL::size_A;
                const T_in *pA2 = pA + ((z + 1) * colA) * MMUL::size_A;
                const T_in *pB1 = pB + j * MMUL::size_B;
                const T_in *pB2 = pB + (j + 1) * MMUL::size_B;

                MMUL C00(aie::load_v<MMUL::size_C>(pC1));
                MMUL C01(aie::load_v<MMUL::size_C>(pC1 + MMUL::size_C));
                MMUL C10(aie::load_v<MMUL::size_C>(pC2));
                MMUL C11(aie::load_v<MMUL::size_C>(pC2 + MMUL::size_C));

                for (unsigned i = 0; i < colA; ++i) {
                    auto A0 = aie::load_v<MMUL::size_A>(pA1); pA1 += MMUL::size_A;
                    auto A1 = aie::load_v<MMUL::size_A>(pA2); pA2 += MMUL::size_A;
                    auto B0 = aie::load_v<MMUL::size_B>(pB1); pB1 += MMUL::size_B * colB;
                    auto B1 = aie::load_v<MMUL::size_B>(pB2); pB2 += MMUL::size_B * colB;

                    C00.mac(A0, B0);
                    C01.mac(A0, B1);
                    C10.mac(A1, B0);
                    C11.mac(A1, B1);
                }

                aie::store_v(pC1, C00.template to_vector<T_out>()); pC1 += MMUL::size_C;
                aie::store_v(pC1, C01.template to_vector<T_out>()); pC1 += MMUL::size_C;
                aie::store_v(pC2, C10.template to_vector<T_out>()); pC2 += MMUL::size_C;
                aie::store_v(pC2, C11.template to_vector<T_out>()); pC2 += MMUL::size_C;
            }
        }
}
```

**Dimension requirements for 2x2 expansion:**

```cpp
static_assert(M % (2 * r) == 0);  // M dimension must be divisible by 2*r
static_assert(K % s == 0);         // K dimension must be divisible by s
static_assert(N % (2 * t) == 0);   // N dimension must be divisible by 2*t
```

### 3.5 MMUL for Convolutions

For 1x1 convolutions, reinterpret the spatial dimension as the M dimension
of the matrix multiply. Process `NUM_W` spatial positions (typically 4 for bf16,
8 for int8) at a time:

```cpp
// Conv 1x1 bf16: treat 4 spatial positions x 8 input channels as mmul A tile
using MMUL = aie::mmul<4, 8, 8, bfloat16, bfloat16>;
// A tile = [4 spatial, 8 IC] = 32 elements
// B tile = [8 IC, 8 OC] = 64 elements (one weight block)
// C tile = [4 spatial, 8 OC] = 32 elements

// Conv 1x1 int8: treat 8 spatial positions x 8 input channels as mmul A tile
using MMUL = aie::mmul<8, 8, 8, int8, int8>;
// A tile = [8 spatial, 8 IC] = 64 elements
// B tile = [8 IC, 8 OC] = 64 elements
// C tile = [8 spatial, 8 OC] = 64 elements
```

### 3.6 MMUL Output Extraction

```cpp
// For bfloat16: no shift needed
aie::vector<bfloat16, MMUL::size_C> result = acc.to_vector<bfloat16>();

// For float output from bf16 inputs:
aie::vector<float, MMUL::size_C> result = acc.to_vector<float>();

// For int8 output from int8 inputs: shift right for quantization
// `scale` = number of right-shift bits (SRS operation)
aie::vector<int8, MMUL::size_C> result = acc.to_vector<int8>(scale);
// This WORKS correctly: hardware SRS with proper element ordering.

// MUST set saturation/rounding BEFORE the to_vector call:
::aie::set_saturation(aie::saturation_mode::saturate);
::aie::set_rounding(aie::rounding_mode::symmetric_inf);
```

---

## 4. Activation Functions

### 4.1 Hardware tanh (AIE2+ Only)

```cpp
// CRITICAL: vector size MUST be >= 16 for bfloat16 on AIE2+
// Vec size 8 produces GARBAGE output (verified experimentally).
aie::vector<bfloat16, 16> result = aie::tanh<bfloat16>(float_vec_16);

// The input MUST be float, output is bfloat16
aie::vector<float, 16> input_f32 = acc.to_vector<float>();  // or cast from bf16
aie::vector<bfloat16, 16> tanh_out = aie::tanh<bfloat16>(input_f32);
```

**WRONG -- will produce garbage:**
```cpp
// DO NOT USE vec size 8 for tanh
aie::vector<bfloat16, 8> BAD = aie::tanh<bfloat16>(float_vec_8);  // BROKEN
```

### 4.2 Hardware exp2 (AIE2+ Only)

```cpp
// Base-2 exponential, input is float, output is bfloat16
aie::vector<bfloat16, N> result = aie::exp2<bfloat16>(float_vec);
```

Used in softmax kernels: `exp(x) = exp2(x * log2(e))`.

### 4.3 LUT-Based tanh (AIE2 -- Legacy)

On AIE2 (non-plus), `aie::tanh` is not available. Use the LUT-based
implementation from `lut_based_ops.h`:

```cpp
#include "lut_based_ops.h"

// Takes v16bfloat16, returns v16bfloat16
aie::vector<bfloat16, 16> result = getTanhBf16(input_bf16);
```

This requires the LUT tables (`tanh_lut_ab`, `tanh_lut_cd`) to be linked.
Uses `aie::linear_approx` with precomputed piecewise-linear tables.

### 4.4 Sigmoid via tanh

Sigmoid is computed as `sigmoid(x) = 0.5 * (1 + tanh(x/2))`:

```cpp
aie::vector<bfloat16, 16> half_v = aie::broadcast<bfloat16, 16>(0.5f);
aie::vector<bfloat16, 16> one_v  = aie::broadcast<bfloat16, 16>(1.0f);

// sigmoid(x) = 0.5 * (1 + tanh(x/2))
auto half_x = aie::mul(input, half_v);
auto tanh_hx = aie::tanh<bfloat16>(half_x.to_vector<float>());
auto one_plus = aie::add(tanh_hx, one_v);
aie::vector<bfloat16, 16> sigmoid = aie::mul(one_plus, half_v);
```

### 4.5 SiLU (Swish) via tanh

SiLU is `silu(x) = x * sigmoid(x) = x * 0.5 * (1 + tanh(x/2))`:

```cpp
// Complete SiLU implementation (AIE2+ vectorized)
aie::vector<bfloat16, 16> half_v = aie::broadcast<bfloat16, 16>(0.5f);
aie::vector<bfloat16, 16> one_v  = aie::broadcast<bfloat16, 16>(1.0f);

auto half_x = aie::mul(input, half_v);
auto tanh_hx = aie::tanh<bfloat16>(half_x.to_vector<float>());
auto one_plus = aie::add(tanh_hx, one_v);
aie::vector<bfloat16, 16> sigmoid = aie::mul(one_plus, half_v);
auto silu_acc = aie::mul(input, sigmoid);
*it_out++ = silu_acc.to_vector<bfloat16>();
```

### 4.6 GELU via tanh

GELU uses the tanh approximation: `gelu(x) = 0.5 * x * (1 + tanh(sqrt(2/pi) * (x + 0.044715 * x^3)))`:

```cpp
const bfloat16 sqrt_2_over_pi = 0.79788456f;
const bfloat16 kBeta = 0.044715f;

auto vs2opi = aie::broadcast<bfloat16, 16>(sqrt_2_over_pi);
auto vBeta  = aie::broadcast<bfloat16, 16>(kBeta);
auto v05    = aie::broadcast<bfloat16, 16>(0.5f);
auto v1     = aie::broadcast<bfloat16, 16>(1.0f);

// x^3
auto x2 = aie::mul(x, x);
auto x3 = aie::mul(x, x2);

// inner = sqrt(2/pi) * (x + beta * x^3)
auto x3_beta = aie::mul(x3, vBeta);
auto inner = aie::add(x, x3_beta);
auto inner_scaled = aie::mul(inner, vs2opi);

// tanh + scale
auto tanh_out = aie::tanh<bfloat16>(inner_scaled.to_vector<float>());
auto one_plus_tanh = aie::add(tanh_out, v1);
auto half_one_plus = aie::mul(v05, one_plus_tanh);
auto result = aie::mul(x, half_one_plus);
```

### 4.7 Scalar Pade tanh (Fallback)

When hardware tanh is not available or for scalar code paths:

```cpp
// Pade rational approximation: tanh(z) ~ z(27+z^2)/(27+9z^2)
// Accurate to ~1e-4 for |z| < 4.5
inline float pade_tanh(float z) {
    float z2 = z * z;
    if (z2 > 20.0f)
        return (z > 0.0f) ? 1.0f : -1.0f;
    return z * (27.0f + z2) / (27.0f + 9.0f * z2);
}
```

**Note:** `bf16 tanh saturates for |x| > 8`. `tanh(x/2)` in bf16 returns
exactly -1.0 or 1.0 for large inputs, meaning `sigmoid(x) = 0` or `1` and
`silu(x) = 0` for x < -8. This is expected behavior.

### 4.8 Integer SiLU via Sigmoid LUT

For fully integer pipelines (int8 convolution + activation), use a 256-entry
uint8 lookup table:

```cpp
// sigmoid_lut[i] = round(sigmoid((i - 128) * 8.0 / 128.0) * 255)
// Maps int8 [-128,127] to uint8 [0,255] representing sigmoid [0.0, 1.0]
static const uint8_t sigmoid_lut[256] __attribute__((aligned(64))) = { ... };

// Usage:
int8_t acc_i8 = srs_to_int8(accumulator, shift1);
uint8_t sig = sigmoid_lut[(int)(acc_i8) + 128];
int32_t silu = (int32_t)acc_i8 * (int32_t)sig;
int8_t out = srs_to_int8(silu, shift2);
```

---

## 5. Data Layout Patterns

### 5.1 Tiled Channel Layout

All convolution and spatial kernels in IRON use a "tiled" layout where channels
are grouped into blocks of 8:

```
[C/8, spatial_dims..., 8]
```

**1D (elementwise):** `[C]` -- flat, no tiling needed.

**2D row (convolution input/output):**
```
[C_in/8, W, 8]
```
Element at channel `c`, position `x`: index = `(c/8) * W * 8 + x * 8 + (c%8)`.

**3D (full feature map):**
```
[H, C/8, W, 8]
```

### 5.2 Weight Layouts

**1x1 convolution weights:**
```
[C_out/8, C_in/8, 8, 8]    // [oc_group, ic_group, ic8, oc8]
```
This matches the MMUL B-tile layout: `[8 IC, 8 OC] = 64 elements per block`.

**3x3 convolution weights:**
```
[C_out/8, C_in/8, 3, 3, 8, 8]    // [oc_group, ic_group, kh, kw, ic8, oc8]
```

Weight layout stride calculations:
```cpp
const int wt_stride_kw = 64;                // 8 * 8
const int wt_stride_kh = 3 * 64;            // 3 * 8 * 8
const int wt_stride_ic = 3 * 3 * 64;        // 3 * 3 * 8 * 8
const int wt_stride_oc = ic_groups * wt_stride_ic;
```

### 5.3 Bias Packing

To avoid an extra DMA channel, bias is packed at the end of the weight buffer:

```cpp
// 1x1 conv: bias starts after OC * IC weight elements
bfloat16 *bias = weights + output_channels * input_channels;

// 3x3 conv: bias starts after OC * IC * 9 weight elements
bfloat16 *bias = weights + output_channels * input_channels * 9;

// For int8 with int32 bias:
int32_t *bias = (int32_t *)(weights_and_bias + output_channels * input_channels);
```

### 5.4 MMUL Tiled Layout

For standalone GEMM (non-convolution), data is pre-tiled into MMUL tile shapes:

```
A: [M/r, K/s, r, s]  -- tiles of size r x s
B: [K/s, N/t, s, t]  -- tiles of size s x t
C: [M/r, N/t, r, t]  -- tiles of size r x t
```

Where r, s, t come from `aie::mmul<r, s, t, ...>`.

For non-row-major B (column-major), use `aie::transpose(v, t, s)` before MAC.

---

## 6. Performance Optimization

### 6.1 Pipeline Pragmas

The portable macro header `aie_kernel_utils.h` provides compiler-agnostic pragmas:

```cpp
// Hint: this loop should be software-pipelined
AIE_PREPARE_FOR_PIPELINING
// Chess: [[chess::prepare_for_pipelining]]
// Peano: (no-op -- Peano auto-pipelines)

// Minimum iteration count hint (helps compiler schedule pipeline)
AIE_LOOP_MIN_ITERATION_COUNT(64)
// Chess: [[chess::min_loop_count(64)]]
// Peano: _Pragma("clang loop min_iteration_count(64)")

// Loop range (min, optional max)
AIE_LOOP_RANGE(4, 32)

// Loop unrolling
AIE_LOOP_UNROLL(4)      // Unroll 4 times
AIE_LOOP_UNROLL_FULL     // Fully unroll

// Flatten nested loop (Chess only, fuses inner loop)
AIE_LOOP_FLATTEN         // chess_flatten_loop

// Initiation interval hint (Peano only)
AIE_TRY_INITIATION_INTERVAL(2)

// Disable pipelining for a specific loop
AIE_NO_PREPARE_FOR_PIPELINING
```

**CRITICAL BUG:** `AIE_PREPARE_FOR_PIPELINING` inside an outer loop whose
trip count depends on a **runtime parameter** (e.g., a `check` variable)
can produce **incorrect codegen** with the Chess compiler. The scalar fallback
runs correctly. Always validate vectorized kernels against the scalar reference.

### 6.2 Saturation and Rounding Modes

Set these BEFORE any to_vector() extraction or arithmetic that should use them:

```cpp
// Saturation: clamp out-of-range values instead of wrapping
::aie::set_saturation(aie::saturation_mode::saturate);
// Options: saturate, none

// Rounding mode for SRS (Shift-Round-Saturate)
::aie::set_rounding(aie::rounding_mode::symmetric_inf);
// Options: floor, ceil, symmetric_inf, symmetric_zero, conv_even,
//          conv_odd, symmetric_inf_even, symmetric_inf_odd

// conv_even (convergent/banker's rounding) -- best for bfloat16 accuracy
::aie::set_rounding(aie::rounding_mode::conv_even);

// symmetric_inf -- best for int8 quantized output
::aie::set_rounding(aie::rounding_mode::symmetric_inf);
```

**Restore defaults when done** to avoid affecting other kernels that share
the same tile:

```cpp
::aie::set_saturation(aie::saturation_mode::none);
::aie::set_rounding(aie::rounding_mode::floor);
```

### 6.3 Pointer Restrict Qualifiers

Always use `__restrict` on kernel arguments to tell the compiler that buffers
do not alias. This enables much better instruction scheduling:

```cpp
void my_kernel(bfloat16 *__restrict input,
               bfloat16 *__restrict weights,
               bfloat16 *__restrict output,
               const int32_t size) {
    // Compiler can freely reorder loads/stores
}
```

For the `restrict` keyword (without underscores), include the AIE header
which provides the definition.

### 6.4 Event Markers for Profiling

```cpp
void my_kernel(...) {
    event0();   // Start marker
    // ... kernel body ...
    event1();   // End marker
}
```

These generate hardware events that can be captured by the trace infrastructure
to measure kernel execution time.

### 6.5 Code Size Considerations

- Each AIE tile has **16KB of instruction memory**.
- Large kernels with many template instantiations can exceed this.
- Use `#ifdef` guards (e.g., `#ifdef i8_i8_ONLY`) to compile only needed variants.
- Mark helper functions `inline` or `static inline`.
- Use macros for multi-variant kernel generation (see `mm.cc`'s `combos(X)` pattern).

### 6.6 Stack-Allocated Scratch Buffers

```cpp
// MUST be aligned for vector access
alignas(64) int32_t scratch[64];
alignas(64) bfloat16 temp[16];

// Or use __attribute__
static float __attribute__((aligned(64))) accum_buf[3200];
```

Static buffers work for scratch space that does not need DMA. They do NOT
show up in the MLIR buffer address map -- verify total L1 usage manually.

### 6.7 Multiple Accumulators for ILP

Using multiple accumulators in the inner loop hides MAC latency:

```cpp
constexpr int NUM_ACC = 4;
MMUL8x8x8 acc_tmp[NUM_ACC];
for (int x = 0; x < NUM_ACC; x++)
    acc_tmp[x] = aie::zeros<acc32, MMUL_MN>();

// Inner loop: load weight once, apply to all accumulators
for (int ic = 0; ic < ic_iters; ic++) {
    aie::vector<int8, 64> in_b = aie::load_v<64>(kernels);
    kernels += 64;
    for (int x = 0; x < NUM_ACC; x++) {
        aie::vector<int8, 64> in_a = aie::load_v<64>(input);
        input += 64;
        acc_tmp[x].mac(in_a, in_b);
    }
    input += stride_adjustment;
}
```

This amortizes the weight load across `NUM_ACC` spatial positions.

---

## 7. Common Pitfalls and Known Bugs

### 7.1 aie::tanh Vector Size Requirement (AIE2+)

**BUG:** `aie::tanh<bfloat16>()` requires vector size >= 16 on AIE2+.
Using size 8 **produces garbage** -- not an error, just wrong results.

```cpp
// WRONG -- garbage output
aie::vector<bfloat16, 8> bad = aie::tanh<bfloat16>(float_vec_8);

// CORRECT -- always use size 16
aie::vector<bfloat16, 16> good = aie::tanh<bfloat16>(float_vec_16);

// If you only need 8 results, pad to 16 and extract:
// (Or restructure your loop to process 16 at a time.)
```

This also applies to `aie::exp2<bfloat16>()` -- always use vectors of size >= 16.

### 7.2 to_vector<int32>(0) Element Ordering Bug (AIE2+ / Peano)

**BUG:** When extracting int32 values from an acc32 accumulator using
`acc.to_vector<int32>(0)` on AIE2+ with the Peano/LLVM compiler, the
element ordering is **wrong**. Elements appear scrambled compared to the
logical accumulator order.

**Workaround:** Extract to `int8` (which works correctly) and then
widen manually, or store to a buffer and re-read element by element:

```cpp
// BROKEN on AIE2p with Peano:
aie::vector<int32, 64> v = acc.to_vector<int32>(0);  // wrong ordering

// WORKAROUND: store accum to buffer, read back per-element
aie::vector<int32, MMUL_MN> acc_i32 = acc_mmul.to_vector<int32>(0);
aie::store_v(acc_buf, acc_i32);
// Now acc_buf[i] may not be in the expected order.
// Process per-element via scalar loops instead.

// ALTERNATIVE: to_vector<int8>(shift) WORKS correctly
aie::vector<int8, 64> v8 = acc.to_vector<int8>(scale);  // correct ordering
```

### 7.3 Misaligned Vector Loads

```cpp
// This silently reads from wrong addresses if ptr is not aligned:
aie::vector<int8, 64> v = aie::load_v<64>(ptr);  // requires 64-byte alignment

// Common cause: stride-based pointer arithmetic
// If stride = input_width * 8 and input_width is not a multiple of 8,
// then ptr + stride is NOT 64-byte aligned for int8 loads of size 64.
```

**Rule:** Always ensure `input_width % 8 == 0` for int8 kernels that use
64-element vector loads. Add a runtime check:

```cpp
if (input_width % 8 == 0) {
    vectorized_path(...);
} else {
    scalar_fallback(...);
}
```

### 7.4 Static Buffer Lifetime with IC Streaming

If using a static buffer to accumulate across multiple kernel invocations
(IC streaming pattern), the buffer **only holds the last row's data**
after processing multiple rows:

```cpp
// BROKEN pattern:
static float __attribute__((aligned(64))) _ic_accum[3200];
// Row 0, IC group 0: writes partial sums for row 0
// Row 1, IC group 0: OVERWRITES with row 1's partial sums
// Row 0, IC group 1: reads row 1's data, not row 0's!
```

**Solution:** Either process all IC groups for one row before moving to the
next, or size the buffer to hold all rows simultaneously.

### 7.5 Float Division on AIE Scalar FPU

Float division is **slow** (~15-20 cycles) on the AIE scalar FPU. Use
`aie::inv()` or `aie::invsqrt()` instead:

```cpp
// SLOW:
float result = a / b;

// FASTER:
float result = a * aie::inv(b);

// For 1/sqrt(x):
float result = aie::invsqrt(x);

// For vector inverse:
aie::vector<bfloat16, N> inv_v = aie::inv(bf16_vec);
```

### 7.6 Compiler Differences: Chess vs Peano/LLVM

| Feature | Chess | Peano/LLVM |
|---------|-------|------------|
| `chess_prepare_for_pipelining` | Native pragma | Ignored (auto-pipelines) |
| `chess_flatten_loop` | Fuses inner loop | Not supported |
| `aie::tanh<bfloat16>` | Available (AIE2+) | Available (AIE2+) |
| `to_vector<int32>(0)` | Correct ordering | **BROKEN ordering** |
| `aie::vector<float, 16>` | Works | **May cause compile error** |
| Loop pipelining control | Fine-grained | Limited |

**float vector size on Peano:** Using `aie::vector<float, 16>` may cause
a compile error with Peano. Use size 8 instead and process in two iterations:

```cpp
// Peano-safe pattern for float vectors:
::aie::vector<float, 8> v = ::aie::broadcast<float, 8>(val);
// Process in chunks of 8, not 16
```

### 7.7 extern "C" Requirement

All kernel entry points MUST be wrapped in `extern "C"` to prevent C++ name
mangling. The MLIR-AIE linker looks up symbols by their C name:

```cpp
extern "C" {

void my_kernel_bf16(bfloat16 *input, bfloat16 *output, int32_t size) {
    my_kernel_impl(input, output, size);
}

} // extern "C"
```

### 7.8 NOCPP Define

Some kernels define `NOCPP` at the top. This disables C++ standard library
features that are not available on the AIE target:

```cpp
#define NOCPP
#include <aie_api/aie.hpp>
```

---

## 8. Working Code Templates

### 8.1 Elementwise bf16 Kernel (Vectorized)

Template for any elementwise operation on bfloat16 data:

```cpp
#include "../aie_kernel_utils.h"
#include <aie_api/aie.hpp>
#include <stdint.h>

using namespace aie;

void my_elementwise_bf16(bfloat16 *restrict input,
                          bfloat16 *restrict output,
                          const int32_t vector_size) {
    event0();

    auto it_in  = aie::begin_restrict_vector<16>((bfloat16 *)input);
    auto it_out = aie::begin_restrict_vector<16>((bfloat16 *)output);

    // Pre-compute constants outside the loop
    aie::vector<bfloat16, 16> const_v = aie::broadcast<bfloat16, 16>(CONSTANT);

    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_MIN_ITERATION_COUNT(64)
    for (int i = 0; i < vector_size; i += 16) {
        aie::vector<bfloat16, 16> x = *it_in++;

        // === YOUR OPERATION HERE ===
        auto result = aie::mul(x, const_v);
        // ===========================

        *it_out++ = result.to_vector<bfloat16>();
    }

    event1();
}

extern "C" {
void my_op_bf16(bfloat16 *restrict input, bfloat16 *restrict output,
                int input_size) {
    my_elementwise_bf16(input, output, input_size);
}
} // extern "C"
```

### 8.2 ReLU (Simplest Vectorized Kernel)

The simplest possible vectorized kernel, using raw vector types:

```cpp
void relu_vectorized_bf16(bfloat16 *restrict a, bfloat16 *restrict c,
                           const int32_t vector_size) {
    event0();
    const int v_factor = 32;
    v32bfloat16 zeroes = broadcast_zero_to_v32bfloat16();
    AIE_PREPARE_FOR_PIPELINING
    AIE_LOOP_RANGE(32, 32)
    for (size_t i = 0; i < vector_size; i += v_factor) {
        v32bfloat16 input = *(v32bfloat16 *)(a + i);
        v32bfloat16 output = max(input, zeroes);
        *(v32bfloat16 *)(c + i) = output;
    }
    event1();
}
```

### 8.3 Reduction Kernel (RMS Norm)

Pattern for kernels that need a full-vector reduction before a second pass:

```cpp
template <typename T, int N>
void rms_norm(const T *restrict input, const T *restrict weights,
              T *restrict output, int32_t cols) {
    event0();
    constexpr float epsilon = 1e-5f;

    // Pass 1: compute sum of squares
    ::aie::vector<float, N> add_res = ::aie::zeros<float, N>();
    int vector_chunks = cols / N;
    for (int i = 0; i < vector_chunks; i++) {
        ::aie::vector<T, N> v = ::aie::load_v<N>(input + i * N);
        ::aie::vector<float, N> sq = ::aie::mul_square(v);
        add_res = ::aie::add(add_res, sq);
    }
    float sum_sq = ::aie::reduce_add(add_res);

    // Compute normalization factor
    float rms = sum_sq / cols + epsilon;
    float inv_rms = aie::invsqrt(rms);
    ::aie::vector<T, N> inv_rms_v = ::aie::broadcast<T, N>((T)inv_rms);

    // Pass 2: normalize and optionally multiply by weights
    for (int i = 0; i < vector_chunks; i++) {
        ::aie::vector<T, N> v = ::aie::load_v<N>(input + i * N);
        ::aie::vector<T, N> norm = ::aie::mul(v, inv_rms_v);
        if (weights) {
            ::aie::vector<T, N> w = ::aie::load_v<N>(weights + i * N);
            norm = ::aie::mul(norm, w);
        }
        ::aie::store_v(output + i * N, norm);
    }
    event1();
}
```

### 8.4 1x1 Convolution (bf16 Vectorized)

```cpp
void conv2dk1_bf16_vectorized(bfloat16 *__restrict input,
                               bfloat16 *__restrict weights,
                               bfloat16 *__restrict output,
                               const int32_t W, const int32_t IC,
                               const int32_t OC) {
    event0();

    using MMUL = aie::mmul<4, 8, 8, bfloat16, bfloat16>;
    const int ic_groups = IC / 8;
    const int oc_groups = OC / 8;
    constexpr int NUM_W = 4;
    const int w_iters = W / NUM_W;
    bfloat16 *__restrict out_ptr = output;

    for (int oc_g = 0; oc_g < oc_groups; oc_g++) {
        for (int wi = 0; wi < w_iters; wi++) {
            MMUL acc;
            acc = aie::zeros<accfloat, MMUL::size_C>();

            bfloat16 *__restrict in_ptr = input + wi * NUM_W * 8;
            bfloat16 *__restrict wt_ptr = weights + oc_g * ic_groups * 64;

            for (int ic_g = 0; ic_g < ic_groups; ic_g++) {
                aie::vector<bfloat16, MMUL::size_A> a =
                    aie::load_v<MMUL::size_A>(in_ptr);
                in_ptr += W * 8;  // next IC group
                aie::vector<bfloat16, MMUL::size_B> b =
                    aie::load_v<MMUL::size_B>(wt_ptr);
                wt_ptr += 64;
                acc.mac(a, b);
            }

            aie::store_v(out_ptr, acc.to_vector<bfloat16>());
            out_ptr += MMUL::size_C;
        }
    }

    event1();
}
```

### 8.5 3x3 Convolution with Border Handling (int8 Vectorized)

This shows the shuffle-based border handling pattern for stride-1:

```cpp
void conv2dk3_i8_vec(int8_t *__restrict line0, int8_t *__restrict line1,
                      int8_t *__restrict line2, int8_t *__restrict weights,
                      int8_t *__restrict output,
                      const int32_t W, const int32_t IC, const int32_t OC,
                      const int32_t check, const int32_t scale) {
    event0();
    using MMUL = aie::mmul<8, 8, 8, int8, int8>;
    constexpr int NUM_W = 8;

    ::aie::set_saturation(aie::saturation_mode::saturate);
    ::aie::set_rounding(aie::rounding_mode::symmetric_inf);

    aie::vector<int8, 64> zeros_v = aie::zeros<int8, 64>();
    int8_t *lines[3] = {line0, line1, line2};
    int kh_start = (check == 0) ? 1 : 0;  // skip line0 if top border
    int kh_end   = (check == 2) ? 2 : 3;  // skip line2 if bottom border

    for (int oc_g = 0; oc_g < OC/8; oc_g++) {
        for (int vi = 0; vi < W / NUM_W; vi++) {
            int x = vi * NUM_W;
            MMUL acc;
            acc = aie::zeros<acc32, MMUL::size_C>();

            for (int kh = kh_start; kh < kh_end; kh++) {
                for (int ic_g = 0; ic_g < IC/8; ic_g++) {
                    int8_t *lp = lines[kh] + ic_g * W * 8;
                    auto v_c = aie::load_v<64>(lp + x * 8);

                    // Left-shifted view (kw=0)
                    auto v_left = (vi > 0)
                        ? aie::shuffle_up_fill(v_c,
                              aie::load_v<64>(lp + (x - NUM_W) * 8), 8)
                        : aie::shuffle_up_fill(v_c, zeros_v, 8);

                    // Right-shifted view (kw=2)
                    auto v_right = (x + NUM_W < W)
                        ? aie::shuffle_down_fill(v_c,
                              aie::load_v<64>(lp + (x + NUM_W) * 8), 8)
                        : aie::shuffle_down_fill(v_c, zeros_v, 8);

                    int8_t *wp = weights + oc_g * (IC/8) * 576
                                + ic_g * 576 + kh * 192;
                    acc.mac(v_left, aie::load_v<64>(wp));
                    acc.mac(v_c,    aie::load_v<64>(wp + 64));
                    acc.mac(v_right, aie::load_v<64>(wp + 128));
                }
            }

            aie::store_v(output + oc_g * W * 8 + x * 8,
                         acc.to_vector<int8>(scale));
        }
    }

    ::aie::set_saturation(aie::saturation_mode::none);
    ::aie::set_rounding(aie::rounding_mode::floor);
    event1();
}
```

### 8.6 Upsampling (Nearest-Neighbor 2x)

```cpp
// bf16 version: simple load + double-store
void upsample2x_bf16(bfloat16 *restrict input, bfloat16 *restrict output,
                       const int32_t W, const int32_t C) {
    event0();
    const int cg = C >> 3;
    const int out_w = W << 1;

    for (int c = 0; c < cg; c++) {
        bfloat16 *in_cg  = input + c * W * 8;
        bfloat16 *out_cg = output + c * out_w * 8;

        AIE_PREPARE_FOR_PIPELINING
        for (int x = 0; x < W; x++) {
            aie::vector<bfloat16, 8> v = aie::load_v<8>(in_cg + x * 8);
            aie::store_v(out_cg + (2 * x) * 8, v);
            aie::store_v(out_cg + (2 * x + 1) * 8, v);
        }
    }
    event1();
}

// int8 version: uses interleave_zip for efficiency
void upsample2x_i8(int8_t *__restrict input, int8_t *__restrict output,
                     const int32_t W, const int32_t C) {
    event0();
    const int cg = C >> 3;
    const int out_w = W << 1;

    for (int c = 0; c < cg; c++) {
        int8_t *in_cg  = input + c * W * 8;
        int8_t *out_cg = output + c * out_w * 8;

        AIE_PREPARE_FOR_PIPELINING
        for (int x = 0; x < W - 1; x += 2) {
            aie::vector<int8, 16> v = aie::load_v<16>(in_cg + x * 8);
            auto [lo, hi] = aie::interleave_zip(v, v, 8);
            aie::store_v(out_cg + (2 * x) * 8, lo);
            aie::store_v(out_cg + (2 * x + 2) * 8, hi);
        }
    }
    event1();
}
```

### 8.7 Softmax (Multi-Pass Pattern)

Three-pass softmax: find max, compute exp, normalize.

```cpp
void softmax_bf16(bfloat16 *restrict input, bfloat16 *restrict output,
                   const int32_t size) {
    event0();
    constexpr int VL = 64;  // large vector for throughput
    const int iters = size / VL;

    // Pass 1: Find max (scaled by log2e for numerical stability)
    aie::vector<bfloat16, VL> log2e_v =
        aie::broadcast<bfloat16, VL>((bfloat16)1.4453125f);
    float max_val = 0;

    auto it1 = aie::cbegin_restrict_vector<VL>((bfloat16 *)input);
    for (int i = 0; i < iters; i++) {
        auto scaled = aie::mul(*it1++, log2e_v);
        float rm = aie::reduce_max(scaled.to_vector<bfloat16>());
        if (rm > max_val) max_val = rm;
    }

    // Pass 2: exp2(scaled - max) and accumulate sum
    auto it2 = aie::cbegin_restrict_vector<VL>((bfloat16 *)input);
    auto it2_out = aie::begin_restrict_vector<VL>((bfloat16 *)output);
    aie::vector<bfloat16, VL> max_v = aie::broadcast<bfloat16, VL>(max_val);
    aie::accum<accfloat, VL> sum_acc = aie::zeros<accfloat, VL>();

    for (int i = 0; i < iters; i++) {
        auto scaled = aie::mul(*it2++, log2e_v);
        auto shifted = aie::sub(scaled, max_v);
        auto exp_v = aie::exp2<bfloat16>(shifted.to_vector<float>());
        sum_acc = aie::add(sum_acc, exp_v);
        *it2_out++ = exp_v;
    }

    // Pass 3: divide by sum
    float total = aie::reduce_add(sum_acc.to_vector<float>());
    bfloat16 inv_total = (bfloat16)aie::inv(total);

    auto it3 = aie::cbegin_restrict_vector<VL>((bfloat16 *)output);
    auto it3_out = aie::begin_restrict_vector<VL>((bfloat16 *)output);
    for (int i = 0; i < iters; i++) {
        auto v = aie::mul(*it3++, inv_total);
        *it3_out++ = v.to_vector<bfloat16>();
    }
    event1();
}
```

### 8.8 Zero-Fill (Utility)

```cpp
template <typename T, int M, int N>
void zero_vectorized(T *__restrict c) {
    constexpr int r = 512 / (sizeof(T) * 8);  // elements per 512-bit store
    static_assert((M * N) % r == 0);
    const aie::vector<T, r> zeros = aie::zeros<T, r>();
    const T *c_end = c + M * N;
    for (; c < c_end; c += r) {
        aie::store_v(c, zeros);
    }
}
```

---

## 9. AIE2 vs AIE2+ Differences

### 9.1 Activation Function Implementations

| Feature | AIE2 | AIE2+ |
|---------|------|-------|
| `aie::tanh<bfloat16>()` | NOT available | Hardware intrinsic (vec >= 16) |
| `aie::exp2<bfloat16>()` | NOT available | Hardware intrinsic |
| tanh implementation | LUT-based `getTanhBf16()` | `aie::tanh<bfloat16>()` |
| SiLU implementation | LUT-based tanh | Hardware tanh |
| LUT tables required | Yes (tanh_lut_ab/cd, exp_ilut/flut) | No |
| `aie::invsqrt()` | Quake III fast inverse sqrt | Hardware intrinsic |

### 9.2 Code Organization Pattern

```
aie_kernels/
  aie2/          <-- AIE2 implementations
    silu.cc      <-- uses getTanhBf16() from lut_based_ops.h
    tanh.cc      <-- uses getTanhBf16()
    lut_based_ops.h  <-- LUT tables and lookup functions
    aie2_math.h  <-- Quake III invsqrt
  aie2p/         <-- AIE2+ implementations
    silu.cc      <-- uses aie::tanh<bfloat16>() hardware intrinsic
    tanh.cc      <-- uses aie::tanh<bfloat16>()
    (no LUT headers needed)
  generic/       <-- Architecture-agnostic implementations
```

### 9.3 MMUL Shape Availability

| Shape | int8 | int16 | bf16 (standard) | bf16 (BFP16 emul) |
|-------|------|-------|-----------------|-------------------|
| 8,8,8 | Both | -- | -- | AIE2+ |
| 4,4,8 | -- | Both | -- | -- |
| 4,8,8 | -- | -- | Both | -- |
| 8,8,8 | -- | -- | -- | AIE2+ |

---

## 10. Quick Reference Tables

### 10.1 Memory Budget

| Memory | Size | Notes |
|--------|------|-------|
| L1 (per core) | 64 KB | ObjectFIFO buffers + stack + static data |
| L1 usable | ~48 KB | With double buffering overhead |
| L2 (MemTile) | 512 KB | Shared, must fit all broadcast/join buffers |
| Instruction memory | 16 KB | Code size limit per tile |
| Stack | ~1 KB | Default, grows into L1 |

### 10.2 DMA Limits

| Resource | Limit | Notes |
|----------|-------|-------|
| Input DMA channels per core | 2 | Each input ObjectFIFO = 1 channel |
| Output DMA channels per core | 2 | Each output ObjectFIFO = 1 channel |
| DMA BD size field | 1023 | Use 4D TAP for larger transfers |
| DMA stride field | ~20 bits | Larger limit than size |

### 10.3 Typical Vector Widths by Operation

| Operation | int8 | bfloat16 | float |
|-----------|------|----------|-------|
| Elementwise | 32-64 | 16-32 | 8 |
| MMUL tile | 64 | 32-64 | -- |
| Reduction | 64 | 16-64 | 8 |
| Softmax | -- | 64 | 64 (accum) |
| tanh/exp2 | -- | 16 (minimum!) | 16 (input) |

### 10.4 Compilation Flags

| Flag | Effect |
|------|--------|
| `-DNOCPP` | Disable C++ stdlib features |
| `-DSCALAR` | Select scalar implementation |
| `-DINT8_ACT` | Enable int8 activation path |
| `-Di8_i8_ONLY` | Compile only int8->int8 GEMM variant |
| `-Dbf16_bf16_ONLY` | Compile only bf16->bf16 GEMM variant |
| `-DB_COL_MAJ` | B matrix in column-major order |
| `-DC_COL_MAJ` | C matrix in column-major order |
| `-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16` | Use BFP16 emulation for bf16 mmul |
| `-DOPT_PERF_ENABLED` | Enable chess_flatten_loop optimizations |
| `-DDIM_M=64 -DDIM_K=64 -DDIM_N=64` | Set GEMM tile dimensions |
| `-DROUND_CONV_EVEN` | Use convergent rounding for bf16 mmul |
| `-DNUM_ACC_COUNT=4` | Number of accumulators for ILP |
| `-DN_ROWS=1` | Number of rows per kernel call |

### 10.5 Tolerance Guidelines

| Kernel Type | rel_tol | abs_tol |
|-------------|---------|---------|
| Standalone elementwise (tanh, sigmoid, relu) | 0.04 | 1e-6 |
| Standalone GEMM/GEMV | 0.04 | 1e-3 |
| Composed (SiLU + GEMV = SwiGLU) | 0.07 | 0.7-1.0 |
| Multi-stage pipeline | 0.1 | 1.0 |
| int8 quantized | -- | Exact match after quantization |

---

## Appendix: Kernel Skeleton Checklist

Before writing a new AIE kernel, verify:

- [ ] Include `<aie_api/aie.hpp>` and `"../aie_kernel_utils.h"`
- [ ] Use `__restrict` on all pointer parameters
- [ ] Wrap entry point in `extern "C" { ... }`
- [ ] Add `event0()` / `event1()` markers
- [ ] Vector size >= 16 for any `aie::tanh` or `aie::exp2` calls
- [ ] All `aie::load_v<N>()` pointers are N*sizeof(T)-byte aligned
- [ ] Set saturation/rounding modes before `to_vector<int8>(shift)`
- [ ] Restore saturation/rounding defaults at function end
- [ ] `AIE_PREPARE_FOR_PIPELINING` only on fixed-trip-count loops
- [ ] Total L1 usage (buffers + stack + statics) fits in 64 KB
- [ ] Code size fits in 16 KB instruction memory
- [ ] SPDX license header present
- [ ] Scalar fallback for untiled/remainder cases
- [ ] Tested against CPU reference with appropriate tolerances
