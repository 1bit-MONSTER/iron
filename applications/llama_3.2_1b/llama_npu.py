#!/usr/bin/env python3

import torch
import math
from pathlib import Path
import sys
import numpy as np
import ml_dtypes
import llama_inference_harness as harness
import logging

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))

from operators.common.aie_context import AIEContext
from operators.common import (
    AIEBuffer
)
from operators.common.utils import torch_to_numpy, numpy_to_torch
from operators import (
    AIERMSNorm,
    AIEGEMM,
    AIEGEMV,
    AIEElementwiseAdd
)
from operators.elementwise_mul.op import AIEElementwiseMul
from operators.silu.op import AIESiLU

logging.basicConfig(level=logging.DEBUG)


# AIE Operator Configuration
# ##########################################################################

aie_ops = None

class AIEPrefillOperations:
    pass

class AIEDecodeOperations:
    pass

class AIELlamaOperators:
    
    def __init__(self, config, prompt_len):
        self.context = AIEContext()
        self.context.build_dir.mkdir(parents=True, exist_ok=True)

        self.prefill = AIEPrefillOperations()
        self.decode = AIEDecodeOperations()

        # RMS Norm
        self.prefill.rms_norm = AIERMSNorm(
            size=prompt_len * config.emb_dim,
            eps=1e-5,
            num_aie_columns=8,
            num_channels=2,
            tile_size=config.emb_dim,
            context=self.context
        ).compile().get_callable()
        self.decode.rms_norm = AIERMSNorm(
            size=config.emb_dim,
            eps=1e-5,
            num_aie_columns=1,
            num_channels=2,
            tile_size=config.emb_dim,
            context=self.context
        ).compile().get_callable()

        # Residual additions
        self.prefill.residual_add = AIEElementwiseAdd(
            size=prompt_len * config.emb_dim,
            tile_size=config.emb_dim
        ).compile().get_callable()
        self.decode.residual_add = AIEElementwiseAdd(
            size=config.emb_dim,
            tile_size=config.emb_dim // 8
        ).compile().get_callable()

        # Final GEMM
        min_N = 64 * 8 * 4  # tile_n * num_aie_columns * partition_N
        config.padded_vocab_size = (config.vocab_size + min_N - 1) // min_N * min_N
        config.vocab_partitions = 4
        self.prefill.out_head_compilable = AIEGEMM(
            M=prompt_len,
            K=config.emb_dim,
            N=config.padded_vocab_size // config.vocab_partitions,
            num_aie_columns=8,
            tile_m=64,
            tile_k=64,
            tile_n=64,
            b_col_maj=True,
            use_static_weight=True,
            separate_c_tiles=True,
            context=self.context
        ).compile()
        self.prefill.out_head = self.prefill.out_head_compilable.get_callable()
        self.decode.out_head = AIEGEMV(
            M=config.vocab_size,
            K=config.emb_dim,
            num_aie_columns=8,
            use_static_weight=True,
            tile_size_input=4,
            tile_size_output=32,
            context=self.context
        ).compile().get_callable()
        
        # SwiGLU FFN operators
        # Prefill: M=prompt_len, K=emb_dim, N=hidden_dim
        self.prefill.ffn_up_gate = AIEGEMM(
            M=prompt_len,
            K=config.emb_dim,
            N=config.hidden_dim,
            num_aie_columns=8,
            tile_m=64,
            tile_k=64,
            tile_n=64,
            b_col_maj=False,  # exceeds stride dimensions otherwise; just transpose weights
            use_static_weight=True,
            context=self.context
        ).compile().get_callable()
        
        self.prefill.ffn_down = AIEGEMM(
            M=prompt_len,
            K=config.hidden_dim,
            N=config.emb_dim,
            num_aie_columns=8,
            tile_m=64,
            tile_k=64,
            tile_n=64,
            b_col_maj=False,  # exceeds stride dimensions otherwise; just transpose weights
            use_static_weight=True,
            context=self.context
        ).compile().get_callable()
        
        self.prefill.ffn_silu = AIESiLU(
            size=prompt_len * config.hidden_dim,
            tile_size=config.hidden_dim,
            num_aie_columns=8,
            context=self.context
        ).compile().get_callable()
        
        self.prefill.ffn_mul = AIEElementwiseMul(
            size=prompt_len * config.hidden_dim,
            tile_size=config.hidden_dim,
            num_aie_columns=8,
            context=self.context
        ).compile().get_callable()
        
        # Decode: GEMV for M=1
        self.decode.ffn_up_gate = AIEGEMV(
            M=config.hidden_dim,
            K=config.emb_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=config.hidden_dim // 8,
            context=self.context
        ).compile().get_callable()
        
        self.decode.ffn_down = AIEGEMV(
            M=config.emb_dim,
            K=config.hidden_dim,
            num_aie_columns=8,
            tile_size_input=1,
            tile_size_output=config.emb_dim // 8,
            context=self.context
        ).compile().get_callable()
        
        self.decode.ffn_silu = AIESiLU(
            size=config.hidden_dim,
            tile_size=config.hidden_dim // 8,
            num_aie_columns=1,
            context=self.context
        ).compile().get_callable()
        
        self.decode.ffn_mul = AIEElementwiseMul(
            size=config.hidden_dim,
            tile_size=config.hidden_dim // 8,
            num_aie_columns=8,
            context=self.context
        ).compile().get_callable()
        


# Allocate buffers shared with NPU
# ##########################################################################

aie_buffers = None

class AIEPrefillBuffers:
    def __init__(self, prompt_len, emb_dim, hidden_dim):
        self.x = AIEBuffer(shape=(prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        self.x_norm = AIEBuffer(shape=(prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        self.attn_output = AIEBuffer(shape=(prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_output = AIEBuffer(shape=(prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        # SwiGLU intermediate buffers
        self.ffn_gate = AIEBuffer(shape=(prompt_len, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_up = AIEBuffer(shape=(prompt_len, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_hidden = AIEBuffer(shape=(prompt_len, hidden_dim), dtype=ml_dtypes.bfloat16)

class AIEDecodeBuffers:
    def __init__(self, emb_dim, hidden_dim):
        self.x = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        self.x_norm = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        self.attn_output = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_output = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        # SwiGLU intermediate buffers
        self.ffn_gate = AIEBuffer(shape=(1, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_up = AIEBuffer(shape=(1, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_hidden = AIEBuffer(shape=(1, hidden_dim), dtype=ml_dtypes.bfloat16)

class AIELlamaBuffers:
    def __init__(self, config, prompt_len):
        # Vector of the current token(s) being processed through the pipeline
        self.prefill = AIEPrefillBuffers(prompt_len, config.emb_dim, config.hidden_dim)
        self.decode = AIEDecodeBuffers(config.emb_dim, config.hidden_dim)

        # Transformer block layer-wise RMS norm
        self.W_norm1 = []
        self.W_norm2 = []
        # SwiGLU FFN weights
        self.W_ffn_gate_prefill = []
        self.W_ffn_up_prefill = []
        self.W_ffn_down_prefill = []
        self.W_ffn_gate_decode = []
        self.W_ffn_up_decode = []
        self.W_ffn_down_decode = []
        for layer_idx in range(config.n_layers):
            self.W_norm1.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.input_layernorm.weight']).to("npu")
            )
            self.W_norm2.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.post_attention_layernorm.weight']).to("npu")
            )
            self.W_ffn_gate_decode.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.mlp.gate_proj.weight']).to("npu")
            )
            self.W_ffn_up_decode.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.mlp.up_proj.weight']).to("npu")
            )
            self.W_ffn_down_decode.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.mlp.down_proj.weight']).to("npu")
            )
            self.W_ffn_gate_prefill.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.mlp.gate_proj.weight'].T).to("npu")
            )
            self.W_ffn_up_prefill.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.mlp.up_proj.weight'].T).to("npu")
            )
            self.W_ffn_down_prefill.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.mlp.down_proj.weight'].T).to("npu")
            )

        # Final RMS norm weights
        self.W_final_norm = AIEBuffer.from_torch(config.weights['model.norm.weight']).to("npu")
        # Final linear layer
        self.W_out_head = AIEBuffer.from_torch(config.weights['model.embed_tokens.weight']).to("npu")  # unpadded/unpartitioned, used by GEMV
        W_out_head_parts = aie_ops.prefill.out_head_compilable.partition_B(
            torch_to_numpy(config.weights['model.embed_tokens.weight']), 
            config.vocab_partitions
        )
        self.W_out_head_parts = [
            AIEBuffer.from_np(W_out_head_part).to("npu") 
            for W_out_head_part in W_out_head_parts
        ] # partitioned, padded parts of weight, used by GEMM
        self.prefill.logits = AIEBuffer(shape=(config.vocab_partitions, prompt_len, config.padded_vocab_size // config.vocab_partitions)).to("npu")
        self.prefill.logits_parts = [
            self.prefill.logits.subbuffer(
                length=prompt_len * (config.padded_vocab_size // config.vocab_partitions),
                offset=i * prompt_len * (config.padded_vocab_size // config.vocab_partitions),
                shape=(prompt_len, config.padded_vocab_size // config.vocab_partitions),
            )
            for i in range(config.vocab_partitions)
        ]
        self.decode.logits = AIEBuffer(shape=(config.vocab_size,))


# Operators
# ##########################################################################

def rope_forward(x, angles):
    """Rotary positional embedding using precomputed angles"""
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
    # (The same cosine and sine values are used across batch and heads.)
    cos = cos.unsqueeze(0).unsqueeze(2)
    sin = sin.unsqueeze(0).unsqueeze(2)
    
    # Rotate: [x1*cos - x2*sin, x1*sin + x2*cos]
    rotated = torch.empty_like(x)
    rotated[..., : head_dim // 2] = x1 * cos - x2 * sin
    rotated[..., head_dim // 2 :] = x1 * sin + x2 * cos
    
    return rotated


def rms_norm_forward(x, weight, eps=1e-5):
    """Root Mean Square Layer Normalization"""
    # x: (batch, seq_len, dim)
    variance = x.pow(2).mean(-1, keepdim=True)
    x = x * torch.rsqrt(variance + eps)
    return weight * x


def grouped_query_attention_forward(
    x, 
    keys_cache,
    values_cache,
    W_query, W_key, W_value, W_out,
    angles,
    mask=None,
    num_heads=32,
    num_kv_groups=8,
):
    batch, seq_len, d_in = x.shape
    assert W_query.shape[0] >= num_heads and W_query.shape[0] % num_heads == 0
    head_dim = W_query.shape[0] // num_heads
    assert W_key.shape[0] == num_kv_groups * head_dim
    assert W_value.shape[0] == num_kv_groups * head_dim
    num_preceding_tokens = keys_cache.shape[2]
    assert keys_cache.shape == (batch, num_kv_groups, num_preceding_tokens, head_dim)
    assert values_cache.shape == (batch, num_kv_groups, num_preceding_tokens, head_dim)

    # Step 1: Linear projections
    # This multiplication produces queries, keys and values for all tokens in the sequence.
    # The weight matrix is such that multiple queries, keys and values are generated for each token.
    # For each token, each head corresponds to one query.
    # In particular, each token gets `num_heads` queries and `num_kv_groups` keys/values (keys/values shared for multiple queries).
    # Due to the structure of the matmul, all queries, keys and values are contiguous for each token.
    # Note that during the decode phase, seq_len=1, and we are only calculating the projections for the most recent token -- the keys and values of previous tokens will be concatenated in step 4.
    queries = torch.nn.functional.linear(x, W_query)              # (batch, seq_len, num_heads * head_dim)
    keys = torch.nn.functional.linear(x, W_key)                   # (batch, seq_len, num_kv_groups * head_dim)
    values = torch.nn.functional.linear(x, W_value)               # (batch, seq_len, num_kv_groups * head_dim)
    queries = queries.view(batch, seq_len, num_heads, head_dim)   # (batch, seq_len, num_heads, head_dim)
    keys = keys.view(batch, seq_len, num_kv_groups, head_dim)     # (batch, seq_len, num_kv_groups, head_dim)
    values = values.view(batch, seq_len, num_kv_groups, head_dim) # (batch, seq_len, num_kv_groups, head_dim)
    
    # Step 2: Apply RoPE
    queries = rope_forward(queries, angles[num_preceding_tokens : num_preceding_tokens + seq_len])
    keys = rope_forward(keys, angles[num_preceding_tokens : num_preceding_tokens + seq_len])

    # Step 3: Transpose for attention computation
    # As a result of the attention projections, the queries, keys and values for each head are interspersed with each other.
    # Transpose so that heads are consecutive for attention computation: 
    # (batch, seq_len, num_heads, head_dim) -> (batch, num_heads, seq_len, head_dim)
    queries = queries.transpose(1, 2)  # (batch, num_heads, seq_len, head_dim)
    keys = keys.transpose(1, 2)        # (batch, num_kv_groups, seq_len, head_dim)
    values = values.transpose(1, 2)    # (batch, num_kv_groups, seq_len, head_dim)

    # Step 4: Combine newly computed keys/values for most recent token with cache; these values are used as the updated cache and will be returned to use in the next iteration.
    keys_cache = torch.cat([keys_cache, keys], dim=2)
    values_cache = torch.cat([values_cache, values], dim=2)
    keys = keys_cache
    values = values_cache
    
    # Step 5: Repeat keys and values for grouped attention -- multiple queries get the same key/value
    group_size = num_heads // num_kv_groups
    keys = keys.repeat_interleave(group_size, dim=1)
    values = values.repeat_interleave(group_size, dim=1)
    
    # Step 6: Compute attention scores
    # (batch, num_heads, seq_len, head_dim) @ (batch, num_heads, head_dim, seq_len)
    # -> (batch, num_heads, seq_len, seq_len)
    # Entry at row i, column j, indicates how much token i's query attends to token j's key.
    scores = torch.matmul(queries, keys.transpose(-2, -1)) / math.sqrt(head_dim)
    
    # Step 7: Apply mask
    # This ensures causality, so that tokens in the future cannot attend to tokens in the past.
    if mask is not None:
        scores = scores.masked_fill(mask, float('-inf'))
    
    # Step 8: Apply softmax to squeeze scores into probabilities (0, 1)
    attention_weights = torch.nn.functional.softmax(scores, dim=-1)
    
    # Step 9: Compute attention output
    # (batch, num_heads, seq_len, seq_len) @ (batch, num_heads, seq_len, head_dim)
    # -> (batch, num_heads, seq_len, head_dim)
    context = torch.matmul(attention_weights, values)
    
    # Step 10: Concatenate heads and project
    # (batch, seq_len, num_heads, head_dim) -> (batch, seq_len, num_heads * head_dim)
    context = context.transpose(1, 2).contiguous().view(batch, seq_len, -1)
    
    output = torch.nn.functional.linear(context, W_out)
    
    return output, keys_cache, values_cache


def swiglu_ffn_forward(seq_len, layer_idx):
    # Select prefill or decode operations and buffers
    if seq_len > 1:
        ops = aie_ops.prefill
        bufs = aie_buffers.prefill
        W_ffn_gate = aie_buffers.W_ffn_gate_prefill[layer_idx]
        W_ffn_up = aie_buffers.W_ffn_up_prefill[layer_idx]
        W_ffn_down = aie_buffers.W_ffn_down_prefill[layer_idx]
    else:
        ops = aie_ops.decode
        bufs = aie_buffers.decode
        W_ffn_gate = aie_buffers.W_ffn_gate_decode[layer_idx]
        W_ffn_up = aie_buffers.W_ffn_up_decode[layer_idx]
        W_ffn_down = aie_buffers.W_ffn_down_decode[layer_idx]
    
    # Step 1: Gate projection: (batch, seq_len, embedding_dim) -> (batch, seq_len, swiglu_hidden_dim)
    bufs.x_norm.to("npu")
    bufs.ffn_gate.to("npu")
    if seq_len > 1:
        ops.ffn_up_gate(bufs.x_norm, W_ffn_gate, bufs.ffn_gate)
    else:
        x_norm_view = bufs.x_norm.view(np.prod(bufs.x_norm.shape))
        ffn_gate_view = bufs.ffn_gate.view(np.prod(bufs.ffn_gate.shape))
        ops.ffn_up_gate(W_ffn_gate, x_norm_view, ffn_gate_view)
    
    # Step 2: Up projection: (batch, seq_len, embedding_dim) -> (batch, seq_len, swiglu_hidden_dim)
    bufs.ffn_up.to("npu")
    if seq_len > 1:
        ops.ffn_up_gate(bufs.x_norm, W_ffn_up, bufs.ffn_up)
    else:
        x_norm_view = bufs.x_norm.view(np.prod(bufs.x_norm.shape))
        ffn_up_view = bufs.ffn_up.view(np.prod(bufs.ffn_up.shape))
        ops.ffn_up_gate(W_ffn_up, x_norm_view, ffn_up_view)
    
    # Step 3: Apply SiLU activation to gate
    ffn_gate_view = bufs.ffn_gate.view(np.prod(bufs.ffn_gate.shape))
    ops.ffn_silu(ffn_gate_view, ffn_gate_view)
    
    # Step 4: Element-wise multiplication (apply the 'gating')
    bufs.ffn_hidden.to("npu")
    ffn_up_view = bufs.ffn_up.view(np.prod(bufs.ffn_up.shape))
    ffn_hidden_view = bufs.ffn_hidden.view(np.prod(bufs.ffn_hidden.shape))
    ops.ffn_mul(ffn_gate_view, ffn_up_view, ffn_hidden_view)
    
    # Step 5: Down projection: (batch, seq_len, swiglu_hidden_dim) -> (batch, seq_len, embedding_dim)
    bufs.ffn_output.to("npu")
    if seq_len > 1:
        ops.ffn_down(bufs.ffn_hidden, W_ffn_down, bufs.ffn_output)
    else:
        ffn_output_view = bufs.ffn_output.view(np.prod(bufs.ffn_output.shape))
        ops.ffn_down(W_ffn_down, ffn_hidden_view, ffn_output_view)


def transformer_block_forward(
    seq_len,
    layer_idx,
    attn_keys_cache,
    attn_values_cache,
    num_heads,
    num_kv_groups,
    W_norm1,
    W_attn_query,
    W_attn_key,
    W_attn_value,
    W_attn_out,
    W_norm2,
    rope_angles,
    attn_mask
):
    # Select prefill or decode operations and buffers
    if seq_len > 1:
        ops = aie_ops.prefill
        bufs = aie_buffers.prefill
    else:
        ops = aie_ops.decode
        bufs = aie_buffers.decode
    
    # Step 1: RMS normalization
    bufs.x.to("npu")
    bufs.x_norm.to("npu")
    ops.rms_norm(bufs.x, W_norm1, bufs.x_norm)
    bufs.x_norm.to("cpu")
    x_norm = bufs.x_norm.view_as_torch().unsqueeze(0)[:, :seq_len, :]

    # Step 2: Attention
    attn_output, attn_keys, attn_values = grouped_query_attention_forward(
        x_norm,
        attn_keys_cache,
        attn_values_cache,
        W_attn_query, W_attn_key, W_attn_value, W_attn_out,
        rope_angles,
        attn_mask,
        num_heads,
        num_kv_groups,
    )
    
    # Step 3: Residual
    bufs.attn_output.view_as_torch().unsqueeze(0)[0, :seq_len, :] = attn_output
    bufs.attn_output.to("npu")
    x_view = bufs.x.view(np.prod(bufs.x.shape))
    attn_output_view = bufs.attn_output.view(np.prod(bufs.attn_output.shape))
    ops.residual_add(x_view, attn_output_view, x_view)
    x = bufs.x.to("cpu").view_as_torch().unsqueeze(0)[:, :seq_len, :]
    
    # Step 4: Post-norm
    bufs.x.view_as_torch().unsqueeze(0)[0, :seq_len, :] = x
    bufs.x.to("npu")
    bufs.x_norm.to("npu")
    ops.rms_norm(bufs.x, W_norm2, bufs.x_norm)
    bufs.x_norm.to("cpu")
    x_norm = bufs.x_norm.view_as_torch().unsqueeze(0)[:, :seq_len, :]
    
    # Step 5: fully-connected feed-forward network
    swiglu_ffn_forward(seq_len, layer_idx)
    
    # Step 6: Residual
    ffn_output_view = bufs.ffn_output.view(np.prod(bufs.ffn_output.shape))
    ops.residual_add(x_view, ffn_output_view, x_view)
    
    return attn_keys, attn_values


def llama_forward_pass(
    config,
    state
):
    batch, seq_len = state.token_ids.shape

    # Select prefill or decode operations and buffers
    if seq_len > 1:
        ops = aie_ops.prefill
        bufs = aie_buffers.prefill
    else:
        ops = aie_ops.decode
        bufs = aie_buffers.decode

    tok_emb_weight = config.weights['model.embed_tokens.weight']
    x = torch.nn.functional.embedding(state.token_ids, tok_emb_weight)  # (batch, seq_len, emb_dim)
    attn_mask = torch.triu(
        torch.ones(seq_len, seq_len, device=x.device, dtype=torch.bool),
        diagonal=1
    )
    bufs.x.view_as_torch().unsqueeze(0)[0, :seq_len, :] = x

    # Step 3: Apply transformer blocks
    for layer_idx in range(config.n_layers):
        state.attn_keys_caches[layer_idx], state.attn_values_caches[layer_idx] = transformer_block_forward(
            seq_len,
            layer_idx,
            state.attn_keys_caches[layer_idx],
            state.attn_values_caches[layer_idx],
            config.n_heads,
            config.n_kv_groups,
            W_norm1=aie_buffers.W_norm1[layer_idx],
            W_attn_query=config.weights[f'model.layers.{layer_idx}.self_attn.q_proj.weight'],
            W_attn_key=config.weights[f'model.layers.{layer_idx}.self_attn.k_proj.weight'],
            W_attn_value=config.weights[f'model.layers.{layer_idx}.self_attn.v_proj.weight'],
            W_attn_out=config.weights[f'model.layers.{layer_idx}.self_attn.o_proj.weight'],
            W_norm2=aie_buffers.W_norm2[layer_idx],
            rope_angles=config.angles,
            attn_mask=attn_mask,
        )

    
    # Step 4: Final normalization
    bufs.x.to("npu")
    ops.rms_norm(bufs.x, aie_buffers.W_final_norm, bufs.x)
    
    # Step 5: Output projection (check for tied embeddings)
    if seq_len > 1:
        # Since vocab size is a very large dimension unsupported by the AIE GEMM, we have to execute the GEMM in multiple partitions and reassemble the output.
        # Reference:
        # bufs.x.to("cpu")
        # x = bufs.x.view_as_torch().unsqueeze(0)[:, :seq_len, :]
        # logits_ref = torch.nn.functional.linear(x, config.weights['model.embed_tokens.weight'])  # (batch, seq_len, vocab_size)
        # assert (logits - logits_ref).max() < 0.5
        bufs.x.to("npu")
        bufs.logits.to("npu")
        for i in range(config.vocab_partitions):
            ops.out_head(bufs.x, aie_buffers.W_out_head_parts[i], bufs.logits_parts[i])
        bufs.logits.to("cpu")
        logits_padded_partitioned = bufs.logits.view_as_torch()  # (vocab_partitions, padded_seq_len, padded_vocab_size // vocab_partitions)
        logits_padded = logits_padded_partitioned.transpose(0, 1).contiguous().view(-1, config.padded_vocab_size)  # (padded_seq_len, padded_vocab_size)
        logits = logits_padded.unsqueeze(0)[:,:seq_len,:config.vocab_size]  # (batch, seq_len, vocab_size)
    else:
        # Step 5: Output projection
        # Reference:
        # x = bufs.x.view_as_torch().unsqueeze(0)
        # logits = torch.nn.functional.linear(config.weights['model.embed_tokens.weight'])  # (batch, seq_len, vocab_size)
        bufs.logits.to("npu")
        ops.out_head(aie_buffers.W_out_head, bufs.x.view((config.emb_dim,)), bufs.logits)
        bufs.logits.to("cpu")
        logits = bufs.logits.view_as_torch().view(1, 1, config.vocab_size)

    return logits, state


# Main
# ##########################################################################

def main():
    global aie_ops, aie_buffers
    max_seq_len = 2048
    prompt = "The capital of France is "
    #with open('prompt.txt', 'r') as f:
    #    prompt = f.read()
    #prompt = prompt[:max_seq_len]

    config, state = harness.init(prompt=prompt)

    aie_ops = AIELlamaOperators(config, max_seq_len)
    aie_buffers = AIELlamaBuffers(config, max_seq_len)

    print(prompt, end='', flush=True)
    harness.generate(config, state, llama_forward_pass, use_kv_cache=True)

if __name__ == "__main__":
    main()
