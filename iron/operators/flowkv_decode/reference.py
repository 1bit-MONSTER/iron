# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16


def interleave_kv_cache(k_cache, v_cache):
    """Interleave K and V cache rows for the FlowKV DMA pattern.

    Input shapes:
        k_cache: (num_kv_heads, seq_len, head_dim)
        v_cache: (num_kv_heads, seq_len, head_dim)

    Output shape: (num_kv_heads, seq_len, 2, head_dim) flattened.

    For each KV head and position, K row comes first, then V row.
    This layout allows the DMA to stream K and V separately using
    strided access patterns (stride = 2 * head_dim).
    """
    num_kv_heads, seq_len, head_dim = k_cache.shape
    interleaved = torch.empty(num_kv_heads, seq_len, 2, head_dim, dtype=k_cache.dtype)
    interleaved[:, :, 0, :] = k_cache
    interleaved[:, :, 1, :] = v_cache
    return interleaved.reshape(-1)


def generate_golden_reference(
    num_heads=32,
    num_kv_heads=8,
    head_dim=64,
    seq_len=128,
    seed=42,
):
    """Generate golden reference data for FlowKV decode attention.

    Computes standard scaled dot-product attention for a single decode step
    (one query position attending over the full KV cache):

        O[h] = softmax(Q[h] @ K[kv_h]^T / sqrt(d)) @ V[kv_h]

    where h is the query head index and kv_h = h // group_size is the
    corresponding KV head.

    Parameters:
        num_heads:    Total number of query heads (32 for Llama 3.2 1B)
        num_kv_heads: Number of KV heads (8 for Llama 3.2 1B)
        head_dim:     Dimension per head (64 for Llama 3.2 1B)
        seq_len:      Current sequence length (number of KV cache positions)
        seed:         Random seed for reproducibility

    Returns:
        dict with:
            Q:        (num_heads, head_dim)           -- query vectors
            K_cache:  (num_kv_heads, seq_len, head_dim) -- K cache
            V_cache:  (num_kv_heads, seq_len, head_dim) -- V cache
            KV_interleaved: (num_kv_heads * seq_len * 2 * head_dim,)
            O:        (num_heads, head_dim)           -- reference output
    """
    torch.manual_seed(seed)
    np.random.seed(seed)

    group_size = num_heads // num_kv_heads

    # Use small value range to keep bf16 precision reasonable
    val_range = 2

    # Generate inputs in bf16 for hardware-accurate reference
    Q = torch.randn(num_heads, head_dim, dtype=torch.bfloat16) * val_range
    K_cache = (
        torch.randn(num_kv_heads, seq_len, head_dim, dtype=torch.bfloat16) * val_range
    )
    V_cache = (
        torch.randn(num_kv_heads, seq_len, head_dim, dtype=torch.bfloat16) * val_range
    )

    # Compute reference attention output in float32 for precision
    Q_f32 = Q.float()
    K_f32 = K_cache.float()
    V_f32 = V_cache.float()

    inv_sqrt_d = 1.0 / np.sqrt(head_dim)

    O = torch.zeros(num_heads, head_dim, dtype=torch.float32)

    for kv_h in range(num_kv_heads):
        k = K_f32[kv_h]  # (seq_len, head_dim)
        v = V_f32[kv_h]  # (seq_len, head_dim)

        for g in range(group_size):
            h = kv_h * group_size + g
            q = Q_f32[h]  # (head_dim,)

            # Attention scores: (seq_len,)
            scores = (q @ k.T) * inv_sqrt_d

            # Softmax
            attn_weights = torch.nn.functional.softmax(scores, dim=-1)

            # Weighted sum: (head_dim,)
            O[h] = attn_weights @ v

    O_bf16 = O.to(torch.bfloat16)

    # Create interleaved KV cache for the design's DDR layout
    kv_interleaved = interleave_kv_cache(K_cache, V_cache)

    return {
        "Q": Q,
        "K_cache": K_cache,
        "V_cache": V_cache,
        "KV_interleaved": kv_interleaved,
        "O": O_bf16,
    }
