# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn.functional as F


def generate_golden_reference(
    in_channels,
    out_channels,
    height,
    width,
    kernel_size=1,
    stride=1,
    has_bias=True,
    activation=None,
    dtype="bf16",
    seed=42,
):
    """Generate input, weights, bias, and expected output for conv2d.

    All tensors are in standard PyTorch NCHW format. Layout conversion
    to tiled format happens in op.py.

    Args:
        in_channels: Number of input channels.
        out_channels: Number of output channels.
        height: Spatial height.
        width: Spatial width.
        kernel_size: Convolution kernel size (only 1 supported).
        stride: Convolution stride.
        has_bias: Whether to include a bias term.
        activation: Optional activation ('silu' or None).
        dtype: Data type string ('bf16').
        seed: Random seed for reproducibility.

    Returns:
        dict with keys: input, weight, bias (or None), output.
        All tensors are bfloat16.
    """
    torch.manual_seed(seed)
    val_range = 2

    assert kernel_size in (1, 3), f"kernel_size must be 1 or 3, got {kernel_size}"

    # Generate random input in [-val_range, val_range]
    input_tensor = (
        torch.rand(1, in_channels, height, width, dtype=torch.bfloat16) * 2 * val_range
        - val_range
    )

    # Generate random weights
    weight = (
        torch.rand(
            out_channels, in_channels, kernel_size, kernel_size, dtype=torch.bfloat16
        )
        * 2
        * val_range
        - val_range
    )

    # Generate random bias
    bias = None
    if has_bias:
        bias = (
            torch.rand(out_channels, dtype=torch.bfloat16) * 2 * val_range - val_range
        )

    # Compute reference output using PyTorch
    # padding=0 for 1x1, padding=1 for 3x3 (same spatial dims at stride=1)
    padding = kernel_size // 2
    output = F.conv2d(input_tensor, weight, bias, stride=stride, padding=padding)

    if activation == "silu":
        output = F.silu(output)

    return {
        "input": input_tensor,
        "weight": weight,
        "bias": bias,
        "output": output,
    }
