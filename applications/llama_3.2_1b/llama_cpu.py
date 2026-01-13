#!/usr/bin/env python3

import torch
import math
from llama_inference_harness import harness

# Operators
# ##########################################################################

def apply_rope(x, angles):
    """Apply RoPE to input tensor x using precomputed angles."""
    # x: (batch, seq_len, num_heads, head_dim) after view and before transpose
    # angles: (context_length, head_dim)
    _, seq_len, _, head_dim = x.shape
    angles_slice = angles[:seq_len]  # (seq_len, head_dim)
    
    # Split into even and odd dimensions
    x1 = x[..., : head_dim // 2]  # (batch, seq_len, num_heads, head_dim//2)
    x2 = x[..., head_dim // 2 :]  # (batch, seq_len, num_heads, head_dim//2)
    
    # Get cos and sin from angles
    cos = angles_slice[:, ::2]  # (seq_len, head_dim//2)
    sin = angles_slice[:, 1::2]  # (seq_len, head_dim//2)
    
    # Reshape for broadcasting: (1, seq_len, 1, head_dim//2)
    cos = cos.unsqueeze(0).unsqueeze(2)
    sin = sin.unsqueeze(0).unsqueeze(2)
    
    # Rotate: [x1*cos - x2*sin, x1*sin + x2*cos]
    rotated = torch.empty_like(x)
    rotated[..., : head_dim // 2] = x1 * cos - x2 * sin
    rotated[..., head_dim // 2 :] = x1 * sin + x2 * cos
    
    return rotated


def rms_norm_forward(x, weight, eps=1e-5):
    """RMSNorm: Root Mean Square Layer Normalization."""
    # x: (batch, seq_len, dim)
    variance = x.pow(2).mean(-1, keepdim=True)
    x = x * torch.rsqrt(variance + eps)
    return weight * x


def grouped_query_attention_forward(
    x, 
    W_query, W_key, W_value, W_out,
    angles,
    mask=None,
    num_heads=32,
    num_kv_groups=8,
    kv_cache=None,
    input_pos=None,
):
    """
    Grouped Query Attention forward pass.
    
    Steps:
    1. Linear projections (Q, K, V)
    2. Reshape for multi-head
    3. Apply RoPE to Q and K
    4. Repeat K and V for grouped attention
    5. Compute attention scores (Q @ K^T / sqrt(d))
    6. Apply mask and softmax
    7. Compute attention output (scores @ V)
    8. Concatenate heads and project
    """
    batch, seq_len, d_in = x.shape
    head_dim = W_query.shape[0] // num_heads
    
    # Step 1: Linear projections
    queries = torch.nn.functional.linear(x, W_query)  # (batch, seq_len, d_out)
    keys = torch.nn.functional.linear(x, W_key)       # (batch, seq_len, num_kv_groups * head_dim)
    values = torch.nn.functional.linear(x, W_value)   # (batch, seq_len, num_kv_groups * head_dim)
    
    # Step 2: Reshape for multi-head
    queries = queries.view(batch, seq_len, num_heads, head_dim)
    keys = keys.view(batch, seq_len, num_kv_groups, head_dim)
    values = values.view(batch, seq_len, num_kv_groups, head_dim)
    
    # Step 3: Apply RoPE
    queries = apply_rope(queries, angles)
    keys = apply_rope(keys, angles)
    
    # Transpose for attention computation: (batch, num_heads, seq_len, head_dim)
    queries = queries.transpose(1, 2)
    keys = keys.transpose(1, 2)
    values = values.transpose(1, 2)
    
    # Step 4: Repeat K and V for grouped attention
    group_size = num_heads // num_kv_groups
    keys = keys.repeat_interleave(group_size, dim=1)
    values = values.repeat_interleave(group_size, dim=1)
    
    # Step 5: Compute attention scores
    # (batch, num_heads, seq_len, head_dim) @ (batch, num_heads, head_dim, seq_len)
    # -> (batch, num_heads, seq_len, seq_len)
    scores = torch.matmul(queries, keys.transpose(-2, -1)) / math.sqrt(head_dim)
    
    # Step 6: Apply mask and softmax
    if mask is not None:
        scores = scores.masked_fill(mask, float('-inf'))
    
    attention_weights = torch.nn.functional.softmax(scores, dim=-1)
    
    # Step 7: Compute attention output
    # (batch, num_heads, seq_len, seq_len) @ (batch, num_heads, seq_len, head_dim)
    # -> (batch, num_heads, seq_len, head_dim)
    context = torch.matmul(attention_weights, values)
    
    # Step 8: Concatenate heads and project
    # (batch, seq_len, num_heads, head_dim) -> (batch, seq_len, num_heads * head_dim)
    context = context.transpose(1, 2).contiguous().view(batch, seq_len, -1)
    
    output = torch.nn.functional.linear(context, W_out)
    
    return output


def swiglu_ffn_forward(x, fc1_weight, fc2_weight, fc3_weight):
    """
    SwiGLU Feed-Forward Network.
    
    SwiGLU: x -> (SiLU(fc1(x)) * fc2(x)) -> fc3
    where SiLU(x) = x * sigmoid(x)
    
    Steps:
    1. Two parallel linear projections (gate and up)
    2. Apply SiLU to gate
    3. Element-wise multiplication
    4. Down projection
    """
    # Step 1: Parallel projections
    gate = torch.nn.functional.linear(x, fc1_weight)  # gate projection
    up = torch.nn.functional.linear(x, fc2_weight)    # up projection
    
    # Step 2: Apply SiLU activation
    gate_activated = torch.nn.functional.silu(gate)
    
    # Step 3: Element-wise multiplication
    hidden = gate_activated * up
    
    # Step 4: Down projection
    output = torch.nn.functional.linear(hidden, fc3_weight)
    
    return output


def transformer_block_forward(
    x,
    weights,
    layer_idx,
    angles,
    mask,
    num_heads,
    num_kv_groups,
):
    """
    Transformer block forward pass.
    
    Steps:
    1. Pre-norm (RMSNorm)
    2. Grouped Query Attention
    3. Residual connection
    4. Post-norm (RMSNorm)
    5. Feed-Forward Network
    6. Residual connection
    """
    # Step 1: Pre-norm
    norm1_weight = weights[f'model.layers.{layer_idx}.input_layernorm.weight']
    x_norm = rms_norm_forward(x, norm1_weight)
    
    # Step 2: Attention
    attn_W_query = weights[f'model.layers.{layer_idx}.self_attn.q_proj.weight']
    attn_W_key = weights[f'model.layers.{layer_idx}.self_attn.k_proj.weight']
    attn_W_value = weights[f'model.layers.{layer_idx}.self_attn.v_proj.weight']
    attn_W_out = weights[f'model.layers.{layer_idx}.self_attn.o_proj.weight']
    
    attn_output = grouped_query_attention_forward(
        x_norm,
        attn_W_query, attn_W_key, attn_W_value, attn_W_out,
        angles,
        mask,
        num_heads,
        num_kv_groups,
    )
    
    # Step 3: Residual
    x = x + attn_output
    
    # Step 4: Post-norm
    norm2_weight = weights[f'model.layers.{layer_idx}.post_attention_layernorm.weight']
    x_norm = rms_norm_forward(x, norm2_weight)
    
    # Step 5: FFN
    ffn_fc1 = weights[f'model.layers.{layer_idx}.mlp.gate_proj.weight']
    ffn_fc2 = weights[f'model.layers.{layer_idx}.mlp.up_proj.weight']
    ffn_fc3 = weights[f'model.layers.{layer_idx}.mlp.down_proj.weight']
    
    ffn_output = swiglu_ffn_forward(x_norm, ffn_fc1, ffn_fc2, ffn_fc3)
    
    # Step 6: Residual
    x = x + ffn_output
    
    return x


def llama_forward_pass(
    input_ids,
    weights,
    angles,
    config,
):
    """
    Complete Llama model forward pass.
    
    Args:
        input_ids: (batch, seq_len) token indices
        weights: Dict of model weights from safetensors
        angles: Precomputed RoPE angles
        config: LlamaConfig with model hyperparameters
    
    Returns:
        logits: (batch, seq_len, vocab_size)
    """
    batch, seq_len = input_ids.shape
    
    # Step 1: Token embedding
    tok_emb_weight = weights['model.embed_tokens.weight']
    x = torch.nn.functional.embedding(input_ids, tok_emb_weight)  # (batch, seq_len, emb_dim)
    
    # Step 2: Create causal mask
    mask = torch.triu(
        torch.ones(seq_len, seq_len, device=x.device, dtype=torch.bool),
        diagonal=1
    )
    
    # Step 3: Apply transformer blocks
    for layer_idx in range(config.n_layers):
        x = transformer_block_forward(
            x,
            weights,
            layer_idx,
            angles,
            mask,
            config.n_heads,
            config.n_kv_groups,
        )
    
    # Step 4: Final normalization
    final_norm_weight = weights['model.norm.weight']
    x = rms_norm_forward(x, final_norm_weight)
    
    # Step 5: Output projection (check for tied embeddings)
    if 'lm_head.weight' in weights:
        lm_head_weight = weights['lm_head.weight']
    else:
        lm_head_weight = weights['model.embed_tokens.weight']
    
    logits = torch.nn.functional.linear(x, lm_head_weight)  # (batch, seq_len, vocab_size)
    
    return logits


# Main
# ##########################################################################

def main():
    harness(llama_forward_pass)

if __name__ == "__main__":
    main()
