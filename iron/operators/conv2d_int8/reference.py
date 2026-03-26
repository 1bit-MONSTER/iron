# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

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
    out_int8 = torch.clamp(
        (out_int32 + (1 << (scale - 1))) >> scale, -128, 127
    ).to(torch.int8)
    return out_int8
