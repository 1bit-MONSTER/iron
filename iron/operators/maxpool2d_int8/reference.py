# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn.functional as F


def generate_golden_reference(
    channels, height, width, kernel_size=5, stride=1, padding=2, seed=42
):
    """Generate input and expected output for int8 MaxPool2d.

    Args:
        channels: Number of channels (must be a multiple of 8).
        height: Spatial height of input.
        width: Spatial width of input.
        kernel_size: Pooling window size.
        stride: Pooling stride.
        padding: Amount of padding on each side.
        seed: Random seed for reproducibility.

    Returns:
        dict with keys: input, output. All tensors are int8.
    """
    torch.manual_seed(seed)
    input_tensor = torch.randint(
        -128, 128, (1, channels, height, width), dtype=torch.int8
    )
    # MaxPool2d requires float input in PyTorch, compute in float32 then cast
    output_tensor = F.max_pool2d(
        input_tensor.float(),
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
    ).to(torch.int8)
    return {"input": input_tensor, "output": output_tensor}
