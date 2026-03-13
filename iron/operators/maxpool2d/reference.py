# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn.functional as F


def generate_golden_reference(
    channels, height, width, kernel_size=5, stride=1, padding=2, seed=42
):
    """Generate input and expected output for MaxPool2d.

    All tensors are in standard PyTorch NCHW format (batch=1). Layout
    conversion to tiled format happens in op.py.

    Args:
        channels: Number of channels (must be a multiple of 8).
        height: Spatial height of input.
        width: Spatial width of input.
        kernel_size: Pooling window size.
        stride: Pooling stride.
        padding: Amount of padding on each side.
        seed: Random seed for reproducibility.

    Returns:
        dict with keys: input, output. All tensors are bfloat16.
    """
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = (
        torch.rand(1, channels, height, width, dtype=torch.bfloat16) * 2 * val_range
        - val_range
    )
    # Compute in float32 for exact reference, then cast back to bf16
    output_tensor = F.max_pool2d(
        input_tensor.float(),
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
    ).to(torch.bfloat16)
    return {"input": input_tensor, "output": output_tensor}
