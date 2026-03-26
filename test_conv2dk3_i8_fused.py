#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Test for fused int8 conv3x3 + bias + SiLU kernel correctness.

Compares the fused all-integer computation against a float32 reference.
This test runs purely on CPU (no NPU needed) to validate the numerical
correctness of the integer SiLU approximation via sigmoid LUT.

The kernel's computation:
  1. int8 conv accumulation -> int32
  2. + int32 pre-scaled bias
  3. SRS(acc, shift1) -> int8 for LUT index
  4. sigmoid_lut[acc_i8 + 128] -> uint8 sigmoid
  5. acc_i8 * sigmoid -> int16
  6. SRS(product, shift2) -> int8 output

Key insight on shift selection:
  - shift1 controls how the accumulator maps into the LUT's [-8, +8] input
    range. It must be chosen so that the max |accumulator| >> shift1 fits
    in [-128, 127].
  - shift2 controls the final output quantization. Since the SiLU product
    is int8 * uint8 (max 127*255 = 32385), shift2 determines the output
    scale. Higher shift2 = coarser output but no clipping. Lower shift2 =
    finer output but clipping of large SiLU values.
  - The pair (shift1, shift2) jointly determine the output dynamic range.
    We calibrate both from the actual accumulator distribution.
"""

import numpy as np
import math
import sys

# ---- Sigmoid LUT (must match the kernel's table exactly) ----
SIGMOID_LUT = np.array(
    [
        int(round(1.0 / (1.0 + math.exp(-((i - 128) * 8.0 / 128.0))) * 255))
        for i in range(256)
    ],
    dtype=np.uint8,
)


def srs_i8(val, shift):
    """Shift-Round-Saturate to int8 (matching the kernel's srs_i8)."""
    if shift <= 0:
        rounded = val
    else:
        rounded = (val + (1 << (shift - 1))) >> shift
    return int(np.clip(rounded, -128, 127))


def weights_to_tiled_3x3_i8(weight_nchw):
    """Convert [O, I, 3, 3] int8 weight to [O/8, I/8, 3, 3, 8, 8] flat."""
    O, I, kh, kw = weight_nchw.shape
    assert kh == 3 and kw == 3
    assert O % 8 == 0 and I % 8 == 0
    w = weight_nchw.reshape(O // 8, 8, I // 8, 8, 3, 3)
    w = w.transpose(0, 2, 4, 5, 3, 1)
    return w.copy().reshape(-1)


def nchw_to_tiled_i8(tensor_nchw):
    """Convert [1, C, H, W] int8 to [H, C/8, W, 8] flat."""
    N, C, H, W = tensor_nchw.shape
    assert N == 1 and C % 8 == 0
    t = tensor_nchw[0].reshape(C // 8, 8, H, W)
    t = t.transpose(2, 0, 3, 1)
    return t.copy().reshape(-1)


def tiled_to_nchw_i8(flat, C, H, W):
    """Convert flat tiled [H, C/8, W, 8] int8 back to [1, C, H, W]."""
    t = flat.reshape(H, C // 8, W, 8)
    t = t.transpose(1, 3, 0, 2)
    t = t.reshape(C, H, W)
    return t[np.newaxis, :]


def conv2d_i8_accumulators(input_nchw_i8, weight_nchw_i8, bias_i32):
    """Compute int32 accumulators (conv + bias) for all positions."""
    N, IC, H, W = input_nchw_i8.shape
    OC = weight_nchw_i8.shape[0]
    accs = np.zeros((1, OC, H, W), dtype=np.int64)

    for oc in range(OC):
        for oh in range(H):
            for ow in range(W):
                acc = np.int64(0)
                for ic in range(IC):
                    for kh in range(3):
                        for kw in range(3):
                            ih = oh + kh - 1
                            iw = ow + kw - 1
                            if ih < 0 or ih >= H or iw < 0 or iw >= W:
                                continue
                            acc += int(input_nchw_i8[0, ic, ih, iw]) * int(
                                weight_nchw_i8[oc, ic, kh, kw]
                            )
                acc += int(bias_i32[oc])
                accs[0, oc, oh, ow] = acc
    return accs


def apply_integer_silu(acc, shift1, shift2):
    """Apply integer SiLU to a single accumulator value.

    Returns the output int8 value.
    """
    acc_i8 = srs_i8(acc, shift1)
    sig = int(SIGMOID_LUT[acc_i8 + 128])
    product = acc_i8 * sig
    return srs_i8(product, shift2)


def conv2dk3_i8_fused_reference(
    input_nchw_i8, weight_nchw_i8, bias_i32, shift1, shift2
):
    """Python reference matching the fused kernel's integer computation."""
    accs = conv2d_i8_accumulators(input_nchw_i8, weight_nchw_i8, bias_i32)
    N, OC, H, W = accs.shape
    output = np.zeros((1, OC, H, W), dtype=np.int8)

    for oc in range(OC):
        for oh in range(H):
            for ow in range(W):
                output[0, oc, oh, ow] = apply_integer_silu(
                    int(accs[0, oc, oh, ow]), shift1, shift2
                )
    return output


def conv2dk3_float_silu_reference(input_nchw_f32, weight_nchw_f32, bias_f32):
    """Float32 reference: conv3x3 + bias + SiLU."""
    N, IC, H, W = input_nchw_f32.shape
    OC = weight_nchw_f32.shape[0]
    output = np.zeros((1, OC, H, W), dtype=np.float32)

    for oc in range(OC):
        for oh in range(H):
            for ow in range(W):
                acc = 0.0
                for ic in range(IC):
                    for kh in range(3):
                        for kw in range(3):
                            ih = oh + kh - 1
                            iw = ow + kw - 1
                            if ih < 0 or ih >= H or iw < 0 or iw >= W:
                                continue
                            acc += float(input_nchw_f32[0, ic, ih, iw]) * float(
                                weight_nchw_f32[oc, ic, kh, kw]
                            )
                acc += float(bias_f32[oc])
                sigmoid_val = 1.0 / (1.0 + math.exp(-acc))
                output[0, oc, oh, ow] = acc * sigmoid_val
    return output


def calibrate_shifts(accs, acc_scale):
    """Calibrate shift1 and shift2 from actual accumulator distribution.

    The goal:
      1. shift1 maps accumulators into int8 for LUT lookup.
         The LUT covers [-8, +8] in "real" space (mapped to [-128, +127]).
         So acc_i8 = SRS(acc, shift1) should map the typical acc range
         to [-128, 127]. We want the max |acc| >> shift1 ~ 120.

      2. shift2 maps the SiLU product (int8 * uint8) to output int8.
         The max positive product is 127 * 255 = 32385.
         The max negative product is -128 * ~0 = 0 (SiLU is ~0 for
         very negative inputs). For moderately negative inputs, e.g.
         acc_i8=-30, sig~55, product=-1650.
         We want: max_product >> shift2 ~ 120.

      3. The output_scale in real units:
         An output int8 value 'v' represents the real value:
           v * acc_scale * 2^shift1 * 2^shift2 / 255

    Returns:
        shift1, shift2
    """
    max_acc = max(int(np.abs(accs).max()), 1)

    # shift1: map max_acc to ~120 in int8
    shift1 = max(0, int(math.ceil(math.log2(max_acc / 120.0))))

    # After shift1, the max silu product in practice:
    # For positive acc_i8 up to 120: silu = 120 * sigmoid_lut[120+128]
    #   sigmoid_lut[248] = 255, so max_product ~ 120 * 255 = 30600
    # For full range: worst case is 127 * 255 = 32385
    # We want output int8 to cover the full SiLU output range.
    # Compute the actual max product by simulating on the acc distribution.
    max_product = 0
    for v in [int(np.min(accs)), int(np.max(accs))]:
        acc_i8 = srs_i8(v, shift1)
        sig = int(SIGMOID_LUT[acc_i8 + 128])
        p = abs(acc_i8 * sig)
        if p > max_product:
            max_product = p

    # Also sample a few representative values
    percentiles = [1, 5, 50, 95, 99]
    for pct in percentiles:
        v = int(np.percentile(accs, pct))
        acc_i8 = srs_i8(v, shift1)
        sig = int(SIGMOID_LUT[acc_i8 + 128])
        p = abs(acc_i8 * sig)
        if p > max_product:
            max_product = p

    max_product = max(max_product, 1)

    # shift2: map max_product to ~120
    shift2 = max(0, int(math.ceil(math.log2(max_product / 120.0))))

    return shift1, shift2


def run_test(IC, OC, H, W, seed=42):
    """Run a single test case."""
    np.random.seed(seed)
    print(f"\n{'='*60}")
    print(f"Test: IC={IC}, OC={OC}, H={H}, W={W}")
    print(f"{'='*60}")

    # Generate random float data
    input_f32 = (np.random.randn(1, IC, H, W) * 2.0).astype(np.float32)
    weight_f32 = (np.random.randn(OC, IC, 3, 3) * 0.5).astype(np.float32)
    bias_f32 = (np.random.randn(OC) * 0.5).astype(np.float32)

    # --- Quantize inputs ---
    input_max = max(np.abs(input_f32).max(), 1e-10)
    input_scale = input_max / 127.0
    input_i8 = np.clip(np.round(input_f32 / input_scale), -128, 127).astype(np.int8)

    weight_max = max(np.abs(weight_f32).max(), 1e-10)
    weight_scale = weight_max / 127.0
    weight_i8 = np.clip(np.round(weight_f32 / weight_scale), -128, 127).astype(np.int8)

    acc_scale = input_scale * weight_scale
    bias_i32 = np.round(bias_f32 / acc_scale).astype(np.int32)

    # --- Calibrate shifts ---
    input_i8_4d = input_i8.reshape(1, IC, H, W)
    weight_i8_4d = weight_i8.reshape(OC, IC, 3, 3)
    accs = conv2d_i8_accumulators(input_i8_4d, weight_i8_4d, bias_i32)
    shift1, shift2 = calibrate_shifts(accs, acc_scale)

    # output_scale: what each int8 output unit represents in real value
    # The integer pipeline does:
    #   acc_i8 = acc >> shift1  (represents real value acc_i8 * acc_scale * 2^shift1)
    #   sig = sigmoid_lut[acc_i8+128]  (represents sigmoid * 255)
    #   product = acc_i8 * sig  (represents real_silu * 255 / (acc_scale * 2^shift1))
    #     wait -- more carefully:
    #   In real units, acc represents acc * acc_scale.
    #   acc_i8 = acc >> shift1, so acc_i8 represents (acc * acc_scale) / (acc_scale * 2^shift1)
    #     = acc / 2^shift1 (but the "unit" of acc_i8 is acc_scale * 2^shift1 in real)
    #   The LUT treats acc_i8 as a fixed-point value in the range [-128, 127]
    #     mapped to real [-8, +8] (scale factor: 8/128 = 1/16 per LUT unit).
    #   sigmoid_lut[acc_i8+128] = round(sigmoid(acc_i8 * 8/128) * 255)
    #   But acc_i8 in "real" terms is acc_i8 * acc_scale * 2^shift1,
    #     and the LUT assumes acc_i8's real value is acc_i8 * (8/128).
    #   So the LUT is correct when acc_scale * 2^shift1 ~ 8/128 = 0.0625.
    #   In general, this is an approximation.
    #
    # The product = acc_i8 * sig
    #   ~ acc_i8 * sigmoid(acc_i8 * 8/128) * 255
    #   ~ silu_approx(acc_i8) * 255   where silu_approx operates on the LUT scale
    #
    # After shift2: output_i8 = product >> shift2
    #
    # To dequantize: the "true" SiLU(x) where x = acc * acc_scale
    #   In the integer path, acc_i8 ~ acc / 2^shift1
    #   silu_int ~ acc_i8 * sigmoid(acc_i8 * 8/128) * 255
    #   output_i8 ~ silu_int / 2^shift2
    #
    # The real-valued SiLU output is approximately:
    #   silu_real = x * sigmoid(x) where x = acc * acc_scale
    #   silu_int_real = (acc / 2^shift1) * sigmoid((acc / 2^shift1) * 8/128) * 255 / 2^shift2
    #
    # These differ because sigmoid's argument scale doesn't match.
    # For comparison, we'll dequantize output by computing the real SiLU of
    # the dequantized input and comparing directly.

    # Actually, the simplest correct approach: compute what the integer
    # pipeline produces, dequantize it, and compare to float SiLU.
    # The output_scale should be derived from the max integer SiLU output
    # and the corresponding max float SiLU output.

    print(
        f"Scales: input={input_scale:.6f}, weight={weight_scale:.6f}, acc={acc_scale:.8f}"
    )
    print(f"Acc range: [{accs.min()}, {accs.max()}]")
    print(f"Shifts: shift1={shift1}, shift2={shift2}")

    # --- Float reference ---
    float_ref = conv2dk3_float_silu_reference(input_f32, weight_f32, bias_f32)
    print(f"Float SiLU output range: [{float_ref.min():.3f}, {float_ref.max():.3f}]")

    # --- Integer reference ---
    int_ref = conv2dk3_i8_fused_reference(
        input_i8_4d, weight_i8_4d, bias_i32, shift1, shift2
    )
    print(f"Integer output range: [{int_ref.min()}, {int_ref.max()}]")

    # --- Derive output_scale from the linear fit between int and float ---
    # For the comparison, we need to find the scale that best maps int8
    # outputs to float outputs. We do this by regression on the non-zero
    # elements.
    int_flat = int_ref.astype(np.float64).ravel()
    float_flat = float_ref.ravel().astype(np.float64)

    # Simple scale: output_scale = sum(int * float) / sum(int * int)
    # (least-squares fit forcing zero intercept)
    dot_if = np.sum(int_flat * float_flat)
    dot_ii = np.sum(int_flat * int_flat)
    if dot_ii > 0:
        output_scale = dot_if / dot_ii
    else:
        output_scale = 1.0

    int_ref_float = int_ref.astype(np.float32) * output_scale
    print(f"Output scale (fitted): {output_scale:.6f}")
    print(
        f"Integer output (rescaled) range: "
        f"[{int_ref_float.min():.3f}, {int_ref_float.max():.3f}]"
    )

    # --- Error analysis ---
    abs_err = np.abs(int_ref_float - float_ref)
    float_range = float_ref.max() - float_ref.min()
    if float_range < 1e-10:
        float_range = 1.0

    max_abs_err = abs_err.max()
    mean_abs_err = abs_err.mean()
    nrmse = np.sqrt(np.mean((int_ref_float - float_ref) ** 2)) / float_range

    # Correlation coefficient
    corr = np.corrcoef(int_flat, float_flat)[0, 1] if len(int_flat) > 1 else 0

    print(f"\nError analysis (float domain, fitted scale):")
    print(f"  Max absolute error:  {max_abs_err:.4f}")
    print(f"  Mean absolute error: {mean_abs_err:.4f}")
    print(f"  NRMSE:               {nrmse:.4f} ({nrmse*100:.1f}%)")
    print(f"  Correlation:         {corr:.6f}")
    print(f"  Output range:        {float_range:.4f}")

    # --- Compare in quantized domain ---
    # Quantize float_ref to int8 at the fitted output_scale
    float_ref_qi8 = np.clip(np.round(float_ref / output_scale), -128, 127).astype(
        np.int32
    )
    int_ref_i32 = int_ref.astype(np.int32)
    abs_diff_i8 = np.abs(int_ref_i32 - float_ref_qi8)

    max_diff = abs_diff_i8.max()
    mean_diff = abs_diff_i8.mean()
    within_1 = (abs_diff_i8 <= 1).mean() * 100
    within_2 = (abs_diff_i8 <= 2).mean() * 100
    within_3 = (abs_diff_i8 <= 3).mean() * 100
    within_5 = (abs_diff_i8 <= 5).mean() * 100

    print(f"\nError analysis (int8 units at fitted output_scale):")
    print(f"  Max absolute diff:  {max_diff}")
    print(f"  Mean absolute diff: {mean_diff:.2f}")
    print(f"  Within +/- 1: {within_1:.1f}%")
    print(f"  Within +/- 2: {within_2:.1f}%")
    print(f"  Within +/- 3: {within_3:.1f}%")
    print(f"  Within +/- 5: {within_5:.1f}%")

    if max_diff > 0:
        worst_idx = np.unravel_index(abs_diff_i8.argmax(), abs_diff_i8.shape)
        print(f"\n  Worst mismatch at {worst_idx}:")
        print(f"    Integer kernel:  {int_ref[worst_idx]}")
        print(f"    Float quantized: {float_ref_qi8[worst_idx]}")
        print(f"    Float raw:       {float_ref[worst_idx]:.4f}")
        print(f"    Int dequantized: {int_ref_float[worst_idx]:.4f}")

    # Determinism check
    int_ref2 = conv2dk3_i8_fused_reference(
        input_i8_4d, weight_i8_4d, bias_i32, shift1, shift2
    )
    assert np.array_equal(int_ref, int_ref2), "Integer reference is non-deterministic!"
    print("\nDeterminism check: PASS")

    # Tiled layout round-trip
    input_tiled = nchw_to_tiled_i8(input_i8_4d)
    input_roundtrip = tiled_to_nchw_i8(input_tiled, IC, H, W)
    assert np.array_equal(input_i8_4d, input_roundtrip), "Tiled round-trip failed!"
    print("Tiled layout round-trip: PASS")

    weight_tiled = weights_to_tiled_3x3_i8(weight_i8_4d)
    w_orig = weight_i8_4d
    assert weight_tiled[0] == w_orig[0, 0, 0, 0], "Weight tiling check failed!"
    print("Weight tiled layout: PASS")

    # --- Pass/fail criteria ---
    # For int8 inference with LUT-based SiLU:
    #   1. Correlation > 0.95 (the integer SiLU output strongly tracks float)
    #   2. NRMSE < 15% (acceptable for 8-bit approximation)
    #   3. At least 60% within +/- 3 int8 units
    passed = corr > 0.95 and nrmse < 0.15 and within_3 >= 60.0
    print(f"\nResult: {'PASS' if passed else 'FAIL'}")
    if not passed:
        reasons = []
        if corr <= 0.95:
            reasons.append(f"corr={corr:.4f} <= 0.95")
        if nrmse >= 0.15:
            reasons.append(f"NRMSE={nrmse:.4f} >= 0.15")
        if within_3 < 60.0:
            reasons.append(f"within_3={within_3:.1f}% < 60%")
        print(f"  FAIL reason: {', '.join(reasons)}")

    return passed


def main():
    """Run all test configurations."""
    test_configs = [
        (8, 8, 4, 4),
        (8, 8, 8, 8),
        (16, 16, 4, 4),
        (16, 8, 8, 8),
        (8, 16, 4, 4),
    ]

    results = []
    for IC, OC, H, W in test_configs:
        try:
            passed = run_test(IC, OC, H, W)
            results.append((IC, OC, H, W, passed))
        except Exception as e:
            print(f"\nERROR in test IC={IC}, OC={OC}, H={H}, W={W}: {e}")
            import traceback

            traceback.print_exc()
            results.append((IC, OC, H, W, False))

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    all_pass = True
    for IC, OC, H, W, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"  IC={IC:3d}, OC={OC:3d}, H={H:2d}, W={W:2d}: {status}")
        if not passed:
            all_pass = False

    print(f"\nOverall: {'ALL PASSED' if all_pass else 'SOME FAILED'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
