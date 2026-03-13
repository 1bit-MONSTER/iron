# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOv8n model preparation: weight export, BN fusion, layout conversion."""

import torch
import torch.nn.functional as F
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path


def fuse_conv_bn(conv, bn):
    """Fuse Conv2d and BatchNorm2d into a single Conv2d with bias.

    Standard BN fusion: given Conv weight W and bias b, and BN parameters
    gamma, beta, running_mean (mu), running_var (var), eps:

        scale = gamma / sqrt(var + eps)
        W_fused = W * scale[:, None, None, None]
        b_fused = (b - mu) * scale + beta

    Returns (fused_weight, fused_bias) as torch tensors.
    """
    w = conv.weight  # [O, I, kH, kW]
    if conv.bias is not None:
        b = conv.bias
    else:
        b = torch.zeros(w.shape[0])

    gamma = bn.weight  # [O]
    beta = bn.bias  # [O]
    mu = bn.running_mean  # [O]
    var = bn.running_var  # [O]
    eps = bn.eps

    scale = gamma / torch.sqrt(var + eps)
    w_fused = w * scale.reshape(-1, 1, 1, 1)
    b_fused = (b - mu) * scale + beta

    return w_fused, b_fused


def nchw_to_tiled(tensor, group_size=8):
    """Convert NCHW tensor to Y{C/g}X{Cg} tiled layout.

    This layout groups channels into SIMD-friendly chunks of ``group_size``
    and interleaves them with the spatial W dimension so that each row
    can be loaded as a contiguous vector.

    Args:
        tensor: [N, C, H, W] or [C, H, W] torch tensor
        group_size: channel group size (default 8 for AIE SIMD)

    Returns:
        torch tensor in tiled layout [H, C_padded//g, W, g]
    """
    if tensor.dim() == 4:
        tensor = tensor.squeeze(0)  # Remove batch dim
    C, H, W = tensor.shape

    # Pad channels to multiple of group_size
    pad_c = (group_size - C % group_size) % group_size
    if pad_c > 0:
        tensor = F.pad(tensor, (0, 0, 0, 0, 0, pad_c))
        C = C + pad_c

    # Reshape: [C, H, W] -> [C//g, g, H, W] -> [H, C//g, W, g]
    t = tensor.reshape(C // group_size, group_size, H, W)
    t = t.permute(2, 0, 3, 1)  # [H, C//g, W, g]
    t = t.contiguous()

    return t


def tiled_to_nchw(tiled, C, H, W, group_size=8):
    """Convert Y{C/g}X{Cg} tiled layout back to NCHW.

    Inverse of ``nchw_to_tiled``.

    Args:
        tiled: tensor in [H, C_padded//g, W, g] layout
        C: original (unpadded) channel count
        H, W: spatial dimensions
        group_size: channel group size

    Returns:
        torch tensor [1, C, H, W]
    """
    C_padded = ((C + group_size - 1) // group_size) * group_size
    t = tiled.reshape(H, C_padded // group_size, W, group_size)
    t = t.permute(1, 3, 0, 2)  # [C//g, g, H, W]
    t = t.reshape(C_padded, H, W)
    t = t[:C, :, :]  # Remove padding
    return t.unsqueeze(0)  # Add batch dim


def weights_to_tiled_1x1(weight, group_size=8):
    """Convert 1x1 conv weight [O, I, 1, 1] to {O/g}{I/g}{Ig}{Og} layout.

    This layout tiles both output and input channels into groups and
    arranges them so that the inner dimensions are contiguous SIMD
    vectors: the innermost ``Og`` dimension runs across the output
    channel group and ``Ig`` across the input channel group.

    Args:
        weight: [O, I, 1, 1] torch tensor
        group_size: channel group size (default 8)

    Returns:
        torch tensor in [O_p//g, I_p//g, g, g] layout
    """
    O, I, kH, kW = weight.shape
    assert kH == 1 and kW == 1, "Only 1x1 convolutions supported"

    # Pad channels to multiples of group_size
    pad_o = (group_size - O % group_size) % group_size
    pad_i = (group_size - I % group_size) % group_size
    if pad_o > 0 or pad_i > 0:
        weight = F.pad(weight, (0, 0, 0, 0, 0, pad_i, 0, pad_o))

    O_p, I_p = weight.shape[0], weight.shape[1]

    # [O, I, 1, 1] -> [O, I] -> [O/g, g_o, I/g, g_i] -> [O/g, I/g, g_i, g_o]
    w = weight.squeeze(-1).squeeze(-1)  # [O, I]
    w = w.reshape(O_p // group_size, group_size, I_p // group_size, group_size)
    w = w.permute(0, 2, 3, 1)  # [O/g, I/g, Ig, Og]
    w = w.contiguous()

    return w


def weights_to_tiled_3x3(weight, group_size=8):
    """Convert 3x3 conv weight [O, I, 3, 3] to tiled layout.

    Layout: {O/g}{I/g}{kH}{kW}{Ig}{Og}

    The spatial kernel dimensions (3x3) are kept in the middle so that
    the kernel loop can iterate over (kH, kW) while doing vectorized
    loads of the (Ig, Og) channel groups.

    Args:
        weight: [O, I, 3, 3] torch tensor
        group_size: channel group size (default 8)

    Returns:
        torch tensor in [O_p//g, I_p//g, 3, 3, g, g] layout
    """
    O, I, kH, kW = weight.shape
    assert kH == 3 and kW == 3, "Only 3x3 convolutions supported"

    pad_o = (group_size - O % group_size) % group_size
    pad_i = (group_size - I % group_size) % group_size
    if pad_o > 0 or pad_i > 0:
        weight = F.pad(weight, (0, 0, 0, 0, 0, pad_i, 0, pad_o))

    O_p, I_p = weight.shape[0], weight.shape[1]

    # [O, I, 3, 3]
    # -> [O/g, g_o, I/g, g_i, 3, 3]
    # -> [O/g, I/g, 3, 3, g_i, g_o]
    w = weight.reshape(
        O_p // group_size, group_size, I_p // group_size, group_size, kH, kW
    )
    w = w.permute(0, 2, 4, 5, 3, 1)  # [O/g, I/g, kH, kW, Ig, Og]
    w = w.contiguous()

    return w


def export_yolov8n_weights(output_dir="weights"):
    """Export YOLOv8n weights with fused BN in tiled layout.

    Requires: pip install ultralytics
    """
    try:
        from ultralytics import YOLO
    except ImportError:
        raise ImportError("Install ultralytics: pip install ultralytics")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    model = YOLO("yolov8n.pt")
    pytorch_model = model.model

    # Walk through model and fuse Conv+BN pairs
    layer_weights = {}
    for name, module in pytorch_model.named_modules():
        if hasattr(module, "conv") and hasattr(module, "bn"):
            w_fused, b_fused = fuse_conv_bn(module.conv, module.bn)
            layer_weights[name] = {
                "weight": w_fused.to(torch.bfloat16),
                "bias": b_fused.to(torch.float32),  # bias stays float32
                "kernel_size": module.conv.kernel_size,
                "stride": module.conv.stride,
                "in_channels": module.conv.in_channels,
                "out_channels": module.conv.out_channels,
            }

    # Save weights
    torch.save(layer_weights, output_dir / "yolov8n_fused_weights.pt")
    print(f"Exported {len(layer_weights)} fused conv layers to {output_dir}")
    return layer_weights


class YOLOv8nReference:
    """CPU reference implementation for layer-by-layer validation."""

    def __init__(self, weights_path=None):
        self.weights = None
        if weights_path:
            self.weights = torch.load(weights_path)

    def conv_bn_silu(self, x, weight, bias, stride=1, padding=None):
        """Fused Conv+BN+SiLU reference (BN already folded into weight/bias)."""
        kH = weight.shape[2]
        if padding is None:
            padding = kH // 2
        out = F.conv2d(x.float(), weight.float(), bias, stride=stride, padding=padding)
        out = F.silu(out)
        return out.to(torch.bfloat16)

    def conv_bn(self, x, weight, bias, stride=1, padding=None):
        """Fused Conv+BN reference without activation."""
        kH = weight.shape[2]
        if padding is None:
            padding = kH // 2
        out = F.conv2d(x.float(), weight.float(), bias, stride=stride, padding=padding)
        return out.to(torch.bfloat16)
