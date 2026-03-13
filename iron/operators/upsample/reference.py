# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn.functional as F


def generate_golden_reference(channels, height, width, scale_factor=2, seed=42):
    """Generate input and expected output for nearest-neighbor 2x upsampling.

    Args:
        channels: Number of channels (must be a multiple of 8).
        height: Input spatial height.
        width: Input spatial width.
        scale_factor: Upsampling scale factor (only 2 is supported).
        seed: Random seed for reproducibility.

    Returns:
        dict with keys: input [1, C, H, W], output [1, C, 2H, 2W].
        All tensors are bfloat16.
    """
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = (
        torch.rand(1, channels, height, width, dtype=torch.bfloat16) * val_range * 2
        - val_range
    )
    # Compute in float32 then cast back to avoid any precision issues
    output_tensor = F.interpolate(
        input_tensor.float(), scale_factor=scale_factor, mode="nearest"
    ).to(torch.bfloat16)
    return {"input": input_tensor, "output": output_tensor}
