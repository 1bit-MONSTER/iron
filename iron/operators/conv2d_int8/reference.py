# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import math

import numpy as np
import torch
import torch.nn.functional as F


def conv2d_int8_reference(x_int8, weight_int8, scale, stride=1, padding=0):
    """CPU reference for int8 convolution with requantization.

    Performs int8 x int8 -> int32 MAC, then right-shifts with rounding
    and saturates to [-128, 127].

    Args:
        x_int8: Input tensor [N, C_in, H, W] in int8.
        weight_int8: Weight tensor [C_out, C_in, K, K] in int8.
        scale: Right-shift bits for int32 -> int8 requantization.
        stride: Convolution stride (default 1).
        padding: Convolution padding (default 0).

    Returns:
        Output tensor [N, C_out, H_out, W_out] in int8.
    """
    # int8 x int8 -> int32 convolution
    out_int32 = F.conv2d(
        x_int8.int(), weight_int8.int(), stride=stride, padding=padding
    )
    # Right-shift with rounding, saturate to int8 range
    out_int8 = torch.clamp((out_int32 + (1 << (scale - 1))) >> scale, -128, 127).to(
        torch.int8
    )
    return out_int8


def _build_sigmoid_lut():
    """Build the 256-entry sigmoid LUT matching the kernel's hardcoded table.

    For index i in [0, 255], int8 value = i - 128,
    real value x = (i - 128) * 8.0 / 128.0 (range [-8, +8]).
    Entry = round(sigmoid(x) * 255).
    """
    lut = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        x = (i - 128) * 8.0 / 128.0
        lut[i] = int(round(1.0 / (1.0 + math.exp(-x)) * 255))
    return lut


_SIGMOID_LUT = _build_sigmoid_lut()


def _srs_i8(val, shift):
    """Right-shift with rounding and saturate to int8 (tensor version)."""
    rounded = (val + (1 << (shift - 1))) >> shift
    return torch.clamp(rounded, -128, 127)


def conv2d_int8_fused_reference(
    x_int8, weight_int8, bias_int32, shift1, shift2, stride=1
):
    """CPU reference for fused int8 conv + bias + SiLU.

    Replicates the exact integer pipeline of conv2dk3_i8_fused_packed:
      1. int8 x int8 -> int32 convolution (padding=1)
      2. Add pre-scaled int32 bias
      3. srs(acc, shift1) -> int8 for LUT index
      4. Sigmoid LUT lookup -> uint8
      5. acc_i8 * sigmoid -> int32
      6. srs(product, shift2) -> int8 output

    Args:
        x_int8: Input [N, C_in, H, W] int8.
        weight_int8: Weights [C_out, C_in, 3, 3] int8.
        bias_int32: Bias [C_out] int32, pre-scaled.
        shift1: Acc -> int8 shift for LUT index.
        shift2: SiLU product -> int8 output shift.
        stride: Convolution stride (1 or 2).

    Returns:
        Output [N, C_out, H_out, W_out] int8.
    """
    # 1. int8 conv -> int32
    out_int32 = F.conv2d(x_int8.int(), weight_int8.int(), stride=stride, padding=1)

    # 2. Add bias
    out_int32 = out_int32 + bias_int32.view(1, -1, 1, 1).int()

    # 3. Shift to int8 for LUT
    acc_i8 = _srs_i8(out_int32, shift1)

    # 4. Sigmoid LUT lookup
    lut_indices = (acc_i8 + 128).clamp(0, 255).long()
    lut_torch = torch.from_numpy(_SIGMOID_LUT.astype(np.int64))
    sig = lut_torch[lut_indices]

    # 5. SiLU = acc_i8 * sigmoid
    silu = acc_i8 * sig

    # 6. Shift product to output int8
    out_i8 = _srs_i8(silu, shift2)

    return out_i8.to(torch.int8)


def conv2d_int8_fused_silu_reference(
    x_int8, weight_int8, bias_int32, shift1, shift2, stride=1, padding=0
):
    """CPU reference for fused int8 conv + bias + SiLU using float tanh.

    Uses continuous SiLU via tanh instead of LUT-based sigmoid:
      1. int8 x int8 -> int32 convolution
      2. Add pre-scaled int32 bias
      3. Dequantize: float_val = acc * 2^(-shift1)
      4. SiLU(x) = x * 0.5 * (1 + tanh(x/2))
      5. Requantize: int8 out = clamp(round(silu * 2^shift2), -128, 127)

    Args:
        x_int8: Input [N, C_in, H, W] int8.
        weight_int8: Weights [C_out, C_in, K, K] int8.
        bias_int32: Bias [C_out] int32, pre-scaled.
        shift1: Dequantization shift (acc -> float scale = 2^(-shift1)).
        shift2: Requantization shift (float -> int8 scale = 2^shift2).
        stride: Convolution stride (default 1).
        padding: Convolution padding (default 0).

    Returns:
        Output [N, C_out, H_out, W_out] int8.
    """
    # 1. int8 conv -> int32
    out_int32 = F.conv2d(
        x_int8.int(), weight_int8.int(), stride=stride, padding=padding
    )

    # 2. Add bias
    out_int32 = out_int32 + bias_int32.view(1, -1, 1, 1).int()

    # 3. Dequantize to float
    scale_in = 1.0 / (1 << shift1)
    out_float = out_int32.float() * scale_in

    # 4. SiLU via tanh: silu(x) = x * 0.5 * (1 + tanh(x/2))
    silu_out = out_float * 0.5 * (1.0 + torch.tanh(out_float * 0.5))

    # 5. Requantize to int8 (shift2 is fixed-point 8.8: scale = shift2/256)
    scale_out = float(shift2) / 256.0
    out_i8 = torch.clamp(torch.round(silu_out * scale_out), -128, 127)

    return out_i8.to(torch.int8)


def _pade_tanh(z):
    """Padé [3/2] approximation to tanh, matching the AIE kernel.

    tanh(z) ≈ z * (27 + z²) / (27 + 9*z²)   for |z²| ≤ 20
    tanh(z) = sign(z)                          for |z²| > 20
    """
    z2 = z * z
    result = z * (27.0 + z2) / (27.0 + 9.0 * z2)
    # Saturate where |z| is large
    result = torch.where(z2 > 20.0, torch.sign(z), result)
    return result


def conv2d_int8_pade_silu_reference(
    x_int8, weight_int8, bias_int32, shift1, shift2, stride=1, padding=1
):
    """CPU reference for fused int8 conv + bias + SiLU using Padé tanh.

    Matches the exact pipeline of conv2dk3_i8_silu:
      1. int8 x int8 -> int32 convolution (padding=1)
      2. Add pre-scaled int32 bias
      3. Dequantize: float_val = acc / 2^shift1
      4. SiLU(x) = x * 0.5 * (1 + tanh_pade(x/2))
      5. Requantize: clamp(round(silu * 2^shift2), -128, 127)

    Args:
        x_int8: Input [N, C_in, H, W] int8.
        weight_int8: Weights [C_out, C_in, 3, 3] int8.
        bias_int32: Bias [C_out] int32, pre-scaled.
        shift1: Dequantization shift (acc / 2^shift1).
        shift2: Requantization shift (silu * 2^shift2).
        stride: Convolution stride (1 or 2).
        padding: Convolution padding (default 1).

    Returns:
        Output [N, C_out, H_out, W_out] int8.
    """
    # 1. int8 conv -> int32
    out_int32 = F.conv2d(
        x_int8.int(), weight_int8.int(), stride=stride, padding=padding
    )

    # 2. Add bias
    out_int32 = out_int32 + bias_int32.view(1, -1, 1, 1).int()

    # 3. Dequantize to float
    out_float = out_int32.float() / float(1 << shift1)

    # 4. SiLU via Padé tanh: silu(x) = x * 0.5 * (1 + tanh_pade(x/2))
    silu_out = out_float * 0.5 * (1.0 + _pade_tanh(out_float * 0.5))

    # 5. Requantize to int8 (shift2 is fixed-point 8.8: scale = shift2/256)
    scale_out = float(shift2) / 256.0
    out_i8 = torch.clamp(torch.round(silu_out * scale_out), -128, 127)

    return out_i8.to(torch.int8)


def conv2d_int8_split_silu_reference(
    x_int8, weight_int8, bias_int32, conv_scale, shift1, shift2,
    stride=1, padding=1
):
    """CPU reference for split conv -> bias+SiLU pipeline.

    Models the two-core dataflow:
      Core 0 (conv): int8 conv -> int32 acc -> srs(acc, conv_scale) -> int8
      Core 1 (bias_silu):
        1. Dequantize: float val = (float)conv_i8
        2. Add bias:   val += bias_int32 * 2^(-shift1)
        3. SiLU(x) = x * 0.5 * (1 + tanh_pade(x/2))
        4. Requantize:  int8 = clamp(round(silu * shift2/256), -128, 127)

    The key difference from the fused reference: the int8 clipping after
    conv_scale introduces quantization error that the bias+SiLU kernel
    operates on. For well-chosen conv_scale, this error is negligible
    because SiLU saturates for large values.

    Args:
        x_int8: Input [N, C_in, H, W] int8.
        weight_int8: Weights [C_out, C_in, K, K] int8.
        bias_int32: Bias [C_out] int32, pre-scaled.
        conv_scale: Right-shift for conv accumulator -> int8 (Core 0).
        shift1: Dequantization shift for bias scaling in Core 1.
        shift2: Requantization shift for SiLU output (8.8 fixed-point).
        stride: Convolution stride (1 or 2).
        padding: Convolution padding (default 1).

    Returns:
        Output [N, C_out, H_out, W_out] int8.
    """
    # Core 0: int8 conv -> srs -> int8
    out_int32 = F.conv2d(
        x_int8.int(), weight_int8.int(), stride=stride, padding=padding
    )
    conv_i8 = torch.clamp(
        (out_int32 + (1 << (conv_scale - 1))) >> conv_scale, -128, 127
    ).to(torch.int8)

    # Core 1: dequant + bias + SiLU + requant
    dequant = 1.0 / float(1 << shift1)
    val_float = conv_i8.float() + bias_int32.view(1, -1, 1, 1).float() * dequant

    # SiLU via Pade tanh
    silu_out = val_float * 0.5 * (1.0 + _pade_tanh(val_float * 0.5))

    # Requantize
    scale_out_val = float(shift2) / 256.0
    out_i8 = torch.clamp(torch.round(silu_out * scale_out_val), -128, 127)

    return out_i8.to(torch.int8)
