#!/usr/bin/env python3

import torch
import math
from pathlib import Path
import sys
import numpy as np
import ml_dtypes
import llama_inference_harness as harness
import logging
import time

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
from operators.rope.op import AIERope

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
        
        # RoPE operators
        # For queries: (seq_len, num_heads * head_dim) = (seq_len, 2048)
        # For keys: (seq_len, num_kv_groups * head_dim) = (seq_len, 512)
        # angle_rows=1 because all rows use the same angle row (angles are per position)
        self.prefill.rope_queries = AIERope(
            rows=prompt_len * config.n_heads,
            cols=config.head_dim,
            angle_rows=prompt_len,
            context=self.context
        ).compile().get_callable()
        
        self.prefill.rope_keys = AIERope(
            rows=prompt_len * config.n_kv_groups,
            cols=config.head_dim,
            angle_rows=prompt_len,
            context=self.context
        ).compile().get_callable()
        
        self.decode.rope_queries = AIERope(
            rows=1 * config.n_heads,
            cols=config.head_dim,
            angle_rows=1,
            context=self.context
        ).compile().get_callable()
        
        self.decode.rope_keys = AIERope(
            rows=1 * config.n_kv_groups,
            cols=config.head_dim,
            angle_rows=1,
            context=self.context
        ).compile().get_callable()
        
        # Attention projection operators
        # Query projection: (seq_len, emb_dim) -> (seq_len, n_heads * head_dim)
        self.prefill.attn_query = AIEGEMM(
            M=prompt_len,
            K=config.emb_dim,
            N=config.n_heads * config.head_dim,
            num_aie_columns=8,
            tile_m=64,
            tile_k=64,
            tile_n=64,
            b_col_maj=False,
            use_static_weight=True,
            context=self.context
        ).compile().get_callable()
        
        self.decode.attn_query = AIEGEMV(
            M=config.n_heads * config.head_dim,
            K=config.emb_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=config.head_dim // 2,
            context=self.context
        ).compile().get_callable()
        
        # Key projection: (seq_len, emb_dim) -> (seq_len, n_kv_groups * head_dim)
        self.prefill.attn_key = AIEGEMM(
            M=prompt_len,
            K=config.emb_dim,
            N=config.n_kv_groups * config.head_dim,
            num_aie_columns=8,
            tile_m=64,
            tile_k=64,
            tile_n=64,
            b_col_maj=False,
            use_static_weight=True,
            context=self.context
        ).compile().get_callable()
        
        self.decode.attn_key = AIEGEMV(
            M=config.n_kv_groups * config.head_dim,
            K=config.emb_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=config.head_dim // 2,
            context=self.context
        ).compile().get_callable()
        
        # Value projection: (seq_len, emb_dim) -> (seq_len, n_kv_groups * head_dim)
        self.prefill.attn_value = AIEGEMM(
            M=prompt_len,
            K=config.emb_dim,
            N=config.n_kv_groups * config.head_dim,
            num_aie_columns=8,
            tile_m=64,
            tile_k=64,
            tile_n=64,
            b_col_maj=False,
            use_static_weight=True,
            context=self.context
        ).compile().get_callable()
        
        self.decode.attn_value = AIEGEMV(
            M=config.n_kv_groups * config.head_dim,
            K=config.emb_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=config.head_dim // 2,
            context=self.context
        ).compile().get_callable()
        
        # Attention score computation: Q @ K^T per head
        # For prefill: (seq_len, head_dim) @ (head_dim, seq_len) = (seq_len, seq_len) per head
        self.prefill.attn_scores = AIEGEMM(
            M=prompt_len,
            K=config.head_dim,
            N=prompt_len,
            num_aie_columns=8,
            tile_m=64,
            tile_k=64,
            tile_n=64,
            b_col_maj=False,
            use_static_weight=False,
            context=self.context
        ).compile().get_callable()
        
        # For decode: per head, (1, head_dim) @ (head_dim, max_context_len)
        # Use GEMV: (max_context_len, head_dim) @ (head_dim,) = (max_context_len,)
        self.decode.attn_scores = AIEGEMV(
            M=prompt_len,  # max possible context length
            K=config.head_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=prompt_len // 8,
            num_batches=config.n_heads,
            context=self.context
        ).compile().get_callable()
        


# Allocate buffers shared with NPU
# ##########################################################################

aie_buffers = None

class AIEPrefillBuffers:
    def __init__(self, prompt_len, emb_dim, hidden_dim, n_heads, n_kv_groups, head_dim):
        self.x = AIEBuffer(shape=(prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        self.x_norm = AIEBuffer(shape=(prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        self.attn_output = AIEBuffer(shape=(prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_output = AIEBuffer(shape=(prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        # SwiGLU intermediate buffers
        self.ffn_gate = AIEBuffer(shape=(prompt_len, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_up = AIEBuffer(shape=(prompt_len, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_hidden = AIEBuffer(shape=(prompt_len, hidden_dim), dtype=ml_dtypes.bfloat16)
        # RoPE buffers
        self.rope_queries_in = AIEBuffer(shape=(prompt_len * n_heads, head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_queries_out = AIEBuffer(shape=(prompt_len * n_heads, head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_keys_in = AIEBuffer(shape=(prompt_len * n_kv_groups, head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_keys_out = AIEBuffer(shape=(prompt_len * n_kv_groups, head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_angles_queries = AIEBuffer(shape=(prompt_len, head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_angles_keys = AIEBuffer(shape=(prompt_len, head_dim), dtype=ml_dtypes.bfloat16)
        # Attention projection buffers
        self.attn_queries = AIEBuffer(shape=(prompt_len, n_heads * head_dim), dtype=ml_dtypes.bfloat16)
        self.attn_keys = AIEBuffer(shape=(prompt_len, n_kv_groups * head_dim), dtype=ml_dtypes.bfloat16)
        self.attn_values = AIEBuffer(shape=(prompt_len, n_kv_groups * head_dim), dtype=ml_dtypes.bfloat16)
        # Attention score computation buffers (per-head) - parent buffer with subbuffers
        self.attn_scores_queries_per_head = [
            AIEBuffer(shape=(prompt_len, head_dim), dtype=ml_dtypes.bfloat16)
            for h in range(n_heads)
        ]
        self.attn_scores_keys_per_head = [
            AIEBuffer(shape=(head_dim, prompt_len), dtype=ml_dtypes.bfloat16)
            for h in range(n_heads)
        ]
        # Parent buffer for all heads' scores: (n_heads * prompt_len, prompt_len)
        self.attn_scores = AIEBuffer(shape=(n_heads * prompt_len, prompt_len), dtype=ml_dtypes.bfloat16)
        self.attn_scores_per_head = [
            self.attn_scores.subbuffer(
                length=prompt_len * prompt_len,
                offset=h * prompt_len * prompt_len,
                shape=(prompt_len, prompt_len)
            )
            for h in range(n_heads)
        ]

class AIEDecodeBuffers:
    def __init__(self, emb_dim, hidden_dim, n_heads, n_kv_groups, head_dim):
        self.x = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        self.x_norm = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        self.attn_output = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_output = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        # SwiGLU intermediate buffers
        self.ffn_gate = AIEBuffer(shape=(1, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_up = AIEBuffer(shape=(1, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_hidden = AIEBuffer(shape=(1, hidden_dim), dtype=ml_dtypes.bfloat16)
        # RoPE buffers
        self.rope_queries_in = AIEBuffer(shape=(1 * n_heads, head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_queries_out = AIEBuffer(shape=(1 * n_heads, head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_keys_in = AIEBuffer(shape=(1 * n_kv_groups, head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_keys_out = AIEBuffer(shape=(1 * n_kv_groups, head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_angles_queries = AIEBuffer(shape=(1, head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_angles_keys = AIEBuffer(shape=(1, head_dim), dtype=ml_dtypes.bfloat16)
        # Attention projection buffers
        self.attn_queries = AIEBuffer(shape=(1, n_heads * head_dim), dtype=ml_dtypes.bfloat16)
        self.attn_keys = AIEBuffer(shape=(1, n_kv_groups * head_dim), dtype=ml_dtypes.bfloat16)
        self.attn_values = AIEBuffer(shape=(1, n_kv_groups * head_dim), dtype=ml_dtypes.bfloat16)
        # Attention score computation buffers (batched)
        # Batched GEMV expects: (num_batches, M, K) @ (num_batches, K, 1) = (num_batches, M, 1)
        self.attn_scores_keys = AIEBuffer(shape=(n_heads, emb_dim, head_dim), dtype=ml_dtypes.bfloat16)  # Max context length
        self.attn_scores_queries = AIEBuffer(shape=(n_heads, head_dim, 1), dtype=ml_dtypes.bfloat16)
        self.attn_scores = AIEBuffer(shape=(n_heads, emb_dim, 1), dtype=ml_dtypes.bfloat16)

class AIELlamaBuffers:
    def __init__(self, config, prompt_len):
        # Vector of the current token(s) being processed through the pipeline
        self.prefill = AIEPrefillBuffers(prompt_len, config.emb_dim, config.hidden_dim, config.n_heads, config.n_kv_groups, config.head_dim)
        self.decode = AIEDecodeBuffers(config.emb_dim, config.hidden_dim, config.n_heads, config.n_kv_groups, config.head_dim)

        # Transformer block layer-wise RMS norm
        self.W_norm1 = []
        self.W_norm2 = []
        # Attention projection weights
        self.W_attn_query_prefill = []
        self.W_attn_query_decode = []
        self.W_attn_key_prefill = []
        self.W_attn_key_decode = []
        self.W_attn_value_prefill = []
        self.W_attn_value_decode = []
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
            self.W_attn_query_decode.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.self_attn.q_proj.weight']).to("npu")
            )
            self.W_attn_query_prefill.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.self_attn.q_proj.weight'].T).to("npu")
            )
            self.W_attn_key_decode.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.self_attn.k_proj.weight']).to("npu")
            )
            self.W_attn_key_prefill.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.self_attn.k_proj.weight'].T).to("npu")
            )
            self.W_attn_value_decode.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.self_attn.v_proj.weight']).to("npu")
            )
            self.W_attn_value_prefill.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.self_attn.v_proj.weight'].T).to("npu")
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

def rope_forward(x, angles, num_preceding_tokens, is_query):
    """Rotary positional embedding using NPU"""
    # x: (batch, seq_len, num_heads_or_groups, head_dim)
    # angles: (context_length, head_dim) - full angle table
    batch, seq_len, num_heads_or_groups, head_dim = x.shape
    
    # Select prefill or decode buffers
    if seq_len > 1:
        ops = aie_ops.prefill
        bufs = aie_buffers.prefill
    else:
        ops = aie_ops.decode
        bufs = aie_buffers.decode
    
    # Select appropriate buffers and operator based on query/key
    if is_query:
        rope_op = ops.rope_queries
        buf_in = bufs.rope_queries_in
        buf_out = bufs.rope_queries_out
        buf_angles = bufs.rope_angles_queries
    else:
        rope_op = ops.rope_keys
        buf_in = bufs.rope_keys_in
        buf_out = bufs.rope_keys_out
        buf_angles = bufs.rope_angles_keys
    
    # Reshape x to (seq_len * num_heads_or_groups, head_dim) for NPU
    x_reshaped = x.view(batch * seq_len * num_heads_or_groups, head_dim)
    
    # Get the relevant angles slice and repeat for each head/group
    angles_slice = angles[num_preceding_tokens : num_preceding_tokens + seq_len]  # (seq_len, head_dim)
    # Repeat angles for each head/group: (seq_len, head_dim) -> (seq_len * num_heads_or_groups, head_dim)
    angles_repeated = angles_slice.repeat_interleave(num_heads_or_groups, dim=0)
    
    # Copy to NPU buffers
    buf_in.view_as_torch()[:seq_len * num_heads_or_groups, :] = x_reshaped[:seq_len * num_heads_or_groups]
    buf_angles.view_as_torch()[:seq_len, :] = angles_slice
    
    buf_in.to("npu")
    buf_angles.to("npu")
    buf_out.to("npu")
    
    # Execute RoPE on NPU
    rope_op(buf_in, buf_angles, buf_out)
    
    buf_out.to("cpu")
    
    # Read result and reshape back
    result = buf_out.view_as_torch()[:seq_len * num_heads_or_groups, :].clone()
    result = result.view(batch, seq_len, num_heads_or_groups, head_dim)
    
    return result

def grouped_query_attention_forward(
    x, 
    keys_cache,
    values_cache,
    W_query, W_key, W_value, W_out,
    angles,
    layer_idx,
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

    # Select prefill or decode operations and buffers
    if seq_len > 1:
        ops = aie_ops.prefill
        bufs = aie_buffers.prefill
        W_attn_query = aie_buffers.W_attn_query_prefill[layer_idx]
        W_attn_key = aie_buffers.W_attn_key_prefill[layer_idx]
        W_attn_value = aie_buffers.W_attn_value_prefill[layer_idx]
    else:
        ops = aie_ops.decode
        bufs = aie_buffers.decode
        W_attn_query = aie_buffers.W_attn_query_decode[layer_idx]
        W_attn_key = aie_buffers.W_attn_key_decode[layer_idx]
        W_attn_value = aie_buffers.W_attn_value_decode[layer_idx]

    # Step 1: Linear projections
    # This multiplication produces queries, keys and values for all tokens in the sequence.
    # The weight matrix is such that multiple queries, keys and values are generated for each token.
    # For each token, each head corresponds to one query.
    # In particular, each token gets `num_heads` queries and `num_kv_groups` keys/values (keys/values shared for multiple queries).
    # Due to the structure of the matmul, all queries, keys and values are contiguous for each token.
    # Note that during the decode phase, seq_len=1, and we are only calculating the projections for the most recent token -- the keys and values of previous tokens will be concatenated in step 4.
    
    # Query projection using NPU - write directly to RoPE input buffer to avoid CPU round-trip
    bufs.x_norm.to("npu")
    bufs.rope_queries_in.to("npu")
    if seq_len > 1:
        # Project and write to rope buffer with appropriate view
        rope_queries_in_view = bufs.rope_queries_in.view((bufs.rope_queries_in.shape[0] // num_heads, num_heads * head_dim))
        ops.attn_query(bufs.x_norm, W_attn_query, rope_queries_in_view)
    else:
        # ropes_queries_in is (num_heads, head_dim)
        # GEMV expects: (1, M, K) @ (1, K, 1) = (1, M, 1)
        W_attn_query_view = W_attn_query.view((1, W_attn_query.shape[0], W_attn_query.shape[1]))
        x_norm_view = bufs.x_norm.view((1, bufs.x_norm.shape[1], 1))
        rope_queries_in_view = bufs.rope_queries_in.view((1, bufs.rope_queries_in.shape[0] * bufs.rope_queries_in.shape[1], 1))
        ops.attn_query(W_attn_query_view, x_norm_view, rope_queries_in_view)
    
    # Key projection using NPU - write directly to RoPE input buffer to avoid CPU round-trip
    bufs.rope_keys_in.to("npu")
    if seq_len > 1:
        # Project and write to rope buffer with appropriate view
        rope_keys_in_view = bufs.rope_keys_in.view((bufs.rope_keys_in.shape[0] // num_kv_groups, num_kv_groups * head_dim))
        ops.attn_key(bufs.x_norm, W_attn_key, rope_keys_in_view)
    else:
        # GEMV expects: (1, M, K) @ (1, K, 1) = (1, M, 1)
        x_norm_view = bufs.x_norm.view((1, bufs.x_norm.shape[1], 1))
        rope_keys_in_view = bufs.rope_keys_in.view((1, bufs.rope_keys_in.shape[0] * bufs.rope_keys_in.shape[1], 1))
        W_attn_key_view = W_attn_key.view((1, W_attn_key.shape[0], W_attn_key.shape[1]))
        ops.attn_key(W_attn_key_view, x_norm_view, rope_keys_in_view)
    
    # Value projection using NPU
    bufs.attn_values.to("npu")
    if seq_len > 1:
        # Project to values buffer with appropriate view
        ops.attn_value(bufs.x_norm, W_attn_value, bufs.attn_values)
    else:
        # GEMV expects: (1, M, K) @ (1, K, 1) = (1, M, 1)
        x_norm_view = bufs.x_norm.view((1, bufs.x_norm.shape[1], 1))
        attn_values_view = bufs.attn_values.view((1, bufs.attn_values.shape[1], 1))
        W_attn_value_view = W_attn_value.view((1, W_attn_value.shape[0], W_attn_value.shape[1]))
        ops.attn_value(W_attn_value_view, x_norm_view, attn_values_view)
    
    # Read values result from NPU
    bufs.attn_values.to("cpu")
    values = bufs.attn_values.view_as_torch()[:seq_len, :].clone()
    values = values.unsqueeze(0)  # (batch, seq_len, n_kv_groups * head_dim)
    values = values.view(batch, seq_len, num_kv_groups, head_dim) # (batch, seq_len, num_kv_groups, head_dim)
    
    # Step 2: Apply RoPE to queries (already in rope_queries_in buffer on NPU)
    # Get the relevant angles slice
    num_preceding_tokens = keys_cache.shape[2]
    angles_slice = angles[num_preceding_tokens : num_preceding_tokens + seq_len]  # (seq_len, head_dim)
    bufs.rope_angles_queries.view_as_torch()[:seq_len, :] = angles_slice
    bufs.rope_angles_queries.to("npu")
    bufs.rope_queries_out.to("npu")
    
    # Execute RoPE on NPU (data already there from query projection)
    ops.rope_queries(bufs.rope_queries_in, bufs.rope_angles_queries, bufs.rope_queries_out)
    
    # Read queries result from NPU
    bufs.rope_queries_out.to("cpu")
    queries = bufs.rope_queries_out.view_as_torch()[:seq_len * num_heads, :].clone()
    queries = queries.view(batch, seq_len, num_heads, head_dim)
    
    # Apply RoPE to keys (already in rope_keys_in buffer on NPU)
    bufs.rope_angles_keys.view_as_torch()[:seq_len, :] = angles_slice
    bufs.rope_angles_keys.to("npu")
    bufs.rope_keys_out.to("npu")
    
    # Execute RoPE on NPU (data already there from key projection)
    ops.rope_keys(bufs.rope_keys_in, bufs.rope_angles_keys, bufs.rope_keys_out)
    
    # Read keys result from NPU
    bufs.rope_keys_out.to("cpu")
    keys = bufs.rope_keys_out.view_as_torch()[:seq_len * num_kv_groups, :].clone()
    keys = keys.view(batch, seq_len, num_kv_groups, head_dim)

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
    context_len = keys.shape[2]
    
    # Step 6: Compute attention scores using NPU (per-head)
    # (batch, num_heads, seq_len, head_dim) @ (batch, num_heads, head_dim, context_len)
    # -> (batch, num_heads, seq_len, context_len)
    queries_per_head = queries.squeeze(0)  # (num_heads, seq_len, head_dim)
    keys_per_head = keys.squeeze(0).transpose(-2, -1)  # (num_heads, head_dim, context_len)
    
    if seq_len > 1:
        # Prefill: use GEMM per head
        for h in range(num_heads):
            # Copy data for this head
            bufs.attn_scores_queries_per_head[h].view_as_torch()[:context_len, :] = queries_per_head[h, :, :]
            bufs.attn_scores_keys_per_head[h].view_as_torch()[:, :context_len] = keys_per_head[h, :, :context_len]
            
            # Transfer to NPU
            bufs.attn_scores_queries_per_head[h].to("npu")
            bufs.attn_scores_keys_per_head[h].to("npu")
            bufs.attn_scores_per_head[h].to("npu")
            
            # Execute GEMM for this head
            ops.attn_scores(
                bufs.attn_scores_queries_per_head[h],
                bufs.attn_scores_keys_per_head[h],
                bufs.attn_scores_per_head[h]
            )
        
        # Read back all results at once from parent buffer
        bufs.attn_scores.to("cpu")
        # Buffer is (n_heads * max_seq_len, max_seq_len), view as (n_heads, max_seq_len, max_seq_len) then slice
        max_seq_len = bufs.attn_scores.shape[0] // num_heads
        scores = bufs.attn_scores.view_as_torch().view(num_heads, max_seq_len, max_seq_len).unsqueeze(0)[:, :, :seq_len, :context_len]
    else:
        # Decode: batched GEMV with all heads at once
        keys_transposed = keys_per_head.transpose(-2, -1)  # (num_heads, context_len, head_dim)
        
        # Copy all heads' data to batched buffers
        # Keys: (num_heads, context_len, head_dim)
        bufs.attn_scores_keys.view_as_torch()[:, :context_len, :] = keys_transposed[:, :context_len, :]
        # Queries: (num_heads, head_dim, 1) - reshape from (num_heads, 1, head_dim)
        bufs.attn_scores_queries.view_as_torch()[:, :, 0] = queries_per_head[:, 0, :]
        
        # Transfer to NPU
        bufs.attn_scores_keys.to("npu")
        bufs.attn_scores_queries.to("npu")
        bufs.attn_scores.to("npu")
        
        # Execute batched GEMV: (num_heads, context_len, head_dim) @ (num_heads, head_dim, 1) = (num_heads, context_len, 1)
        t_aie_start = time.perf_counter()
        ops.attn_scores(bufs.attn_scores_keys, bufs.attn_scores_queries, bufs.attn_scores)
        t_aie = time.perf_counter() - t_aie_start
        # Reference:
        t_cpu_start = time.perf_counter()
        ref = bufs.attn_scores_keys.to("cpu").view_as_torch() @ bufs.attn_scores_queries.to("cpu").view_as_torch()
        t_cpu = time.perf_counter() - t_cpu_start
        
        # Read back result
        bufs.attn_scores.to("cpu")
        # Result is (num_heads, max_context_len, 1), reshape to (batch, num_heads, 1, context_len)
        scores = bufs.attn_scores.view_as_torch()[:, :context_len, 0].unsqueeze(0).unsqueeze(2)
    
    # Apply scaling
    scores = scores / math.sqrt(head_dim)
    
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
        # GEMV expects: (1, M, K) @ (1, K, 1) = (1, M, 1)
        x_norm_view = bufs.x_norm.view((1, bufs.x_norm.shape[1], 1))
        ffn_gate_view = bufs.ffn_gate.view((1, bufs.ffn_gate.shape[1], 1))
        W_ffn_gate_view = W_ffn_gate.view((1, W_ffn_gate.shape[0], W_ffn_gate.shape[1]))
        ops.ffn_up_gate(W_ffn_gate_view, x_norm_view, ffn_gate_view)
    
    # Step 2: Up projection: (batch, seq_len, embedding_dim) -> (batch, seq_len, swiglu_hidden_dim)
    bufs.ffn_up.to("npu")
    if seq_len > 1:
        ops.ffn_up_gate(bufs.x_norm, W_ffn_up, bufs.ffn_up)
    else:
        # GEMV expects: (1, M, K) @ (1, K, 1) = (1, M, 1)
        x_norm_view = bufs.x_norm.view((1, bufs.x_norm.shape[1], 1))
        ffn_up_view = bufs.ffn_up.view((1, bufs.ffn_up.shape[1], 1))
        W_ffn_up_view = W_ffn_up.view((1, W_ffn_up.shape[0], W_ffn_up.shape[1]))
        ops.ffn_up_gate(W_ffn_up_view, x_norm_view, ffn_up_view)
    
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
        # GEMV expects: (1, M, K) @ (1, K, 1) = (1, M, 1)
        ffn_hidden_view = bufs.ffn_hidden.view((1, bufs.ffn_hidden.shape[1], 1))
        ffn_output_view = bufs.ffn_output.view((1, bufs.ffn_output.shape[1], 1))
        W_ffn_down_view = W_ffn_down.view((1, W_ffn_down.shape[0], W_ffn_down.shape[1]))
        ops.ffn_down(W_ffn_down_view, ffn_hidden_view, ffn_output_view)


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
        layer_idx,
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
        # GEMV expects: (1, M, K) @ (1, K, 1) = (1, M, 1)
        x_view = bufs.x.view((1, config.emb_dim, 1))
        logits_view = bufs.logits.view((1, config.vocab_size, 1))
        W_out_head_view = aie_buffers.W_out_head.view((1, aie_buffers.W_out_head.shape[0], aie_buffers.W_out_head.shape[1]))
        ops.out_head(W_out_head_view, x_view, logits_view)
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
