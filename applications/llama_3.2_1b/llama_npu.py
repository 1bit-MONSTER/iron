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

from operators.common.context import AIEContext
from operators.common import (
    AIEBuffer
)
from operators.common.utils import torch_to_numpy, numpy_to_torch
from operators.common.base import PatchableSingleXclbinCallable
from operators import (
    AIERMSNorm,
    AIEGEMM,
    AIEGEMV,
    AIEElementwiseAdd
)
from operators.elementwise_mul.op import AIEElementwiseMul
from operators.silu.op import AIESiLU
from operators.rope.op import AIERope
from operators.strided_copy.op import AIEStridedCopy
from operators.repeat.op import AIERepeat
from operators.softmax.op import AIESoftmax
from operators.transpose.op import AIETranspose

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
        self.prefill.gemv_out_head_compilable = AIEGEMM(
            M=prompt_len,
            K=config.emb_dim,
            N=config.padded_vocab_size // config.vocab_partitions,
            num_aie_columns=8,
            tile_m=64,
            tile_k=64,
            tile_n=64,
            b_col_maj=True,
            separate_c_tiles=True,
            context=self.context
        ).compile()
        self.prefill.out_head = self.prefill.gemv_out_head_compilable.get_callable()
        self.decode.gemv_out_head = AIEGEMV(
            M=config.vocab_size,
            K=config.emb_dim,
            num_aie_columns=8,
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
            context=self.context
        ).compile().get_callable()
        
        self.prefill.ffn_silu = AIESiLU(
            size=prompt_len * config.hidden_dim,
            tile_size=config.hidden_dim,
            num_aie_columns=8,
            context=self.context
        ).compile().get_callable()
        
        self.prefill.eltwise_mul_ffn = AIEElementwiseMul(
            size=prompt_len * config.hidden_dim,
            tile_size=config.hidden_dim,
            num_aie_columns=8,
            context=self.context
        ).compile().get_callable()
        
        # Decode: GEMV for M=1
        self.decode.gemv_ffn_up_gate = AIEGEMV(
            M=config.hidden_dim,
            K=config.emb_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=config.hidden_dim // 8,
            context=self.context
        ).compile().get_callable()
        
        self.decode.gemv_ffn_down = AIEGEMV(
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
        
        self.decode.eltwise_mul_ffn = AIEElementwiseMul(
            size=config.hidden_dim,
            tile_size=config.hidden_dim // 8,
            num_aie_columns=8,
            context=self.context
        ).compile().get_callable()
        
        # Attention score scaling operators
        # FIXME: Using elementwise mul is very wasteful (of bandwidth) here since it's the same scalar factor for all values; need a kernel that allows scalar multiplication of a vector
        self.prefill.attn_scale = AIEElementwiseMul(
            size=config.n_heads * prompt_len * prompt_len,
            tile_size=prompt_len,
            num_aie_columns=8,
            context=self.context
        ).compile().get_callable()
        
        self.decode.attn_scale = AIEElementwiseMul(
            size=config.n_heads * prompt_len,
            tile_size=prompt_len // 8,
            num_aie_columns=8,
            context=self.context
        ).compile().get_callable()
        
        # Softmax operators for attention weights
        # Prefill uses CPU softmax to reduce NPU operator count
        
        self.decode.softmax_compilable = AIESoftmax(
            rows=config.n_heads,
            cols=prompt_len,
            num_aie_columns=1,
            num_channels=1,
            rtp_vector_size=prompt_len,  # Compile with max size
            context=self.context
        ).compile()
        
        self.decode.softmax = PatchableSingleXclbinCallable(
            xclbin_path=self.decode.softmax_compilable.xclbin_artifact.filename,
            kernel_name=self.decode.softmax_compilable.xclbin_artifact.kernel_name,
            insts_bin_path=self.decode.softmax_compilable.insts_artifact.filename,
            args_spec=self.decode.softmax_compilable.get_arg_spec()
        )
        
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
        
        # Strided copy operators for cache update (transpose and concatenate)
        # Keys: transpose from (1, n_kv_groups, head_dim) to (n_kv_groups, 1, head_dim) and write to cache
        self.decode.strided_copy_cache_compilable = AIEStridedCopy(
            input_sizes=(config.n_kv_groups, 1, config.head_dim),
            input_strides=(config.head_dim, config.n_kv_groups * config.head_dim, 1),
            input_offset=0,
            output_sizes=(1, config.n_kv_groups, 1, config.head_dim),
            output_strides=(0, prompt_len * config.head_dim, config.head_dim, 1),
            output_offset=0,  # Will be patched at runtime based on cached_prompt_len
            input_buffer_size=1 * config.n_kv_groups * config.head_dim,
            output_buffer_size=config.n_kv_groups * prompt_len * config.head_dim,
            num_aie_channels=1,
            context=self.context
        ).compile()
        
        # Create patchable callable for runtime offset updates
        self.decode.strided_copy_cache = PatchableSingleXclbinCallable(
            xclbin_path=self.decode.strided_copy_cache_compilable.xclbin_artifact.filename,
            kernel_name=self.decode.strided_copy_cache_compilable.xclbin_artifact.kernel_name,
            insts_bin_path=self.decode.strided_copy_cache_compilable.insts_artifact.filename,
            args_spec=self.decode.strided_copy_cache_compilable.get_arg_spec()
        )

        # Repeat interleave for keys: (n_kv_groups, context_len, head_dim) -> (n_heads, context_len, head_dim)
        # Compile with max context length, then patch at runtime for actual context_len
        self.decode.attn_repeat_interleave = AIERepeat(
            rows=config.n_kv_groups,
            cols=prompt_len * config.head_dim,  # Max context length
            repeat=config.n_heads // config.n_kv_groups,
            transfer_size=config.head_dim,
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
            context=self.context
        ).compile().get_callable()
        
        self.decode.gemv_attn_query = AIEGEMV(
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
            context=self.context
        ).compile().get_callable()
        
        self.decode.gemv_attn_key_value = AIEGEMV(
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
            context=self.context
        ).compile().get_callable()
        
        # For decode: per head, (1, head_dim) @ (head_dim, max_context_len)
        # Use GEMV: (max_context_len, head_dim) @ (head_dim,) = (max_context_len,)
        self.decode.gemv_attn_scores = AIEGEMV(
            M=prompt_len,  # max possible context length
            K=config.head_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=prompt_len // 8,
            num_batches=config.n_heads,
            context=self.context
        ).compile().get_callable()
        
        # Transpose values from (max_context_len, head_dim) to (head_dim, max_context_len) per head
        self.decode.transpose_values = AIETranspose(
            M=prompt_len,
            N=config.head_dim,
            num_aie_columns=2,
            num_channels=1,
            m=256,
            n=32,
            s=8,
            context=self.context
        ).compile().get_callable()
        
        # GEMV for attention context: (head_dim, max_context_len) @ (max_context_len,) = (head_dim,) per head
        self.decode.gemv_attn_context = AIEGEMV(
            M=config.head_dim,
            K=prompt_len,  # max possible context length
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=4,
            num_batches=config.n_heads,
            context=self.context
        ).compile().get_callable()
        
        # Output projection: (n_heads * head_dim,) @ (emb_dim, n_heads * head_dim)^T -> (emb_dim,)
        self.decode.gemv_attn_output = AIEGEMV(
            M=config.emb_dim,
            K=config.n_heads * config.head_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=config.emb_dim // 8,
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
        # Attention buffers: queries and keys serve as both projection output and RoPE input/output
        self.queries = AIEBuffer(shape=(prompt_len * n_heads, head_dim), dtype=ml_dtypes.bfloat16)
        self.keys = AIEBuffer(shape=(prompt_len * n_kv_groups, head_dim), dtype=ml_dtypes.bfloat16)
        self.values = AIEBuffer(shape=(prompt_len, n_kv_groups * head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_angles = AIEBuffer(shape=(prompt_len, head_dim), dtype=ml_dtypes.bfloat16)
        # Attention score computation buffers (per-head) - parent buffers with subbuffers
        # Parent buffer for all heads' queries: (n_heads, prompt_len, head_dim) stored contiguously
        self.attn_scores_queries_all = AIEBuffer(shape=(n_heads * prompt_len, head_dim), dtype=ml_dtypes.bfloat16)
        self.attn_scores_queries_per_head = [
            self.attn_scores_queries_all.subbuffer(
                length=prompt_len * head_dim,
                offset=h * prompt_len * head_dim,
                shape=(prompt_len, head_dim)
            )
            for h in range(n_heads)
        ]
        # Parent buffer for all KV groups' keys: (n_kv_groups, head_dim, prompt_len) stored contiguously
        self.attn_scores_keys_all = AIEBuffer(shape=(n_kv_groups * head_dim, prompt_len), dtype=ml_dtypes.bfloat16)
        self.attn_scores_keys_per_kv_group = [
            self.attn_scores_keys_all.subbuffer(
                length=head_dim * prompt_len,
                offset=g * head_dim * prompt_len,
                shape=(head_dim, prompt_len)
            )
            for g in range(n_kv_groups)
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
        # Attention score scaling buffer (pre-initialized with 1/sqrt(head_dim))
        scale_factor = 1.0 / math.sqrt(head_dim)
        self.attn_scale_factor = AIEBuffer(shape=(n_heads * prompt_len, prompt_len), dtype=ml_dtypes.bfloat16)
        self.attn_scale_factor.view_as_torch()[:] = scale_factor
        self.attn_scale_factor.to("npu")
        # Attention weights buffer (output of softmax)
        self.attn_weights = AIEBuffer(shape=(n_heads * prompt_len, prompt_len), dtype=ml_dtypes.bfloat16)

class AIEDecodeBuffers:
    def __init__(self, emb_dim, hidden_dim, n_heads, n_kv_groups, head_dim, max_context_len):
        self.x = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        self.x_norm = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        self.attn_output = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_output = AIEBuffer(shape=(1, emb_dim), dtype=ml_dtypes.bfloat16)
        # SwiGLU intermediate buffers
        self.ffn_gate = AIEBuffer(shape=(1, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_up = AIEBuffer(shape=(1, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_hidden = AIEBuffer(shape=(1, hidden_dim), dtype=ml_dtypes.bfloat16)
        # Attention buffers: queries and keys serve as both projection output and RoPE input/output
        self.queries = AIEBuffer(shape=(1 * n_heads, head_dim), dtype=ml_dtypes.bfloat16)
        self.keys = AIEBuffer(shape=(1 * n_kv_groups, head_dim), dtype=ml_dtypes.bfloat16)
        self.values = AIEBuffer(shape=(1, n_kv_groups * head_dim), dtype=ml_dtypes.bfloat16)
        self.rope_angles = AIEBuffer(shape=(1, head_dim), dtype=ml_dtypes.bfloat16)
        # Attention score computation buffers (batched)
        self.attn_scores_keys = AIEBuffer(shape=(n_heads, max_context_len, head_dim), dtype=ml_dtypes.bfloat16)
        self.attn_scores_values = AIEBuffer(shape=(n_heads, max_context_len, head_dim), dtype=ml_dtypes.bfloat16)
        self.attn_scores_values_transposed = AIEBuffer(shape=(n_heads, head_dim, max_context_len), dtype=ml_dtypes.bfloat16)
        # Create per-head subbuffers for transpose operations (to avoid allocating in hot path)
        self.attn_scores_values_per_head = [
            self.attn_scores_values.subbuffer(
                length=max_context_len * head_dim,
                offset=h * max_context_len * head_dim,
                shape=(max_context_len, head_dim)
            )
            for h in range(n_heads)
        ]
        self.attn_scores_values_transposed_per_head = [
            self.attn_scores_values_transposed.subbuffer(
                length=head_dim * max_context_len,
                offset=h * head_dim * max_context_len,
                shape=(head_dim, max_context_len)
            )
            for h in range(n_heads)
        ]
        self.attn_context = AIEBuffer(shape=(n_heads, head_dim), dtype=ml_dtypes.bfloat16)
        self.attn_context_concat = AIEBuffer(shape=(n_heads * head_dim,), dtype=ml_dtypes.bfloat16)
        self.attn_scores = AIEBuffer(shape=(n_heads, max_context_len), dtype=ml_dtypes.bfloat16)
        # Attention score scaling buffer (pre-initialized with 1/sqrt(head_dim))
        scale_factor = 1.0 / math.sqrt(head_dim)
        self.attn_scale_factor = AIEBuffer(shape=(n_heads, max_context_len), dtype=ml_dtypes.bfloat16)
        self.attn_scale_factor.view_as_torch()[:] = scale_factor
        self.attn_scale_factor.to("npu")
        self.attn_weights = AIEBuffer(shape=(n_heads, max_context_len), dtype=ml_dtypes.bfloat16)

class AIELlamaBuffers:
    def __init__(self, config, prompt_len):
        # Vector of the current token(s) being processed through the pipeline
        self.prefill = AIEPrefillBuffers(prompt_len, config.emb_dim, config.hidden_dim, config.n_heads, config.n_kv_groups, config.head_dim)
        self.decode = AIEDecodeBuffers(config.emb_dim, config.hidden_dim, config.n_heads, config.n_kv_groups, config.head_dim, prompt_len)

        # Per-layer KV cache buffers on NPU (used by strided copy for transpose and concatenate)
        self.keys_cache = [
            AIEBuffer(shape=(config.n_kv_groups, prompt_len, config.head_dim), dtype=ml_dtypes.bfloat16)
            for _ in range(config.n_layers)
        ]
        self.values_cache = [
            AIEBuffer(shape=(config.n_kv_groups, prompt_len, config.head_dim), dtype=ml_dtypes.bfloat16)
            for _ in range(config.n_layers)
        ]

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
        self.W_attn_output_decode = []
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
            self.W_attn_output_decode.append(
                AIEBuffer.from_torch(config.weights[f'model.layers.{layer_idx}.self_attn.o_proj.weight']).to("npu")
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
        W_out_head_parts = aie_ops.prefill.gemv_out_head_compilable.partition_B(
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


# Prefill
# ##########################################################################

def grouped_query_attention_forward_prefill(
    config,
    x, 
    keys_cache,
    values_cache,
    layer_idx,
    mask=None,
):
    batch, seq_len, emb_dim = x.shape
    num_preceding_tokens = keys_cache.shape[2]

    # Step 1: Linear projections
    aie_ops.prefill.attn_query(aie_buffers.prefill.x_norm, aie_buffers.W_attn_query_prefill[layer_idx], aie_buffers.prefill.queries)
    aie_ops.prefill.attn_key(aie_buffers.prefill.x_norm, aie_buffers.W_attn_key_prefill[layer_idx], aie_buffers.prefill.keys)
    aie_ops.prefill.attn_value(aie_buffers.prefill.x_norm, aie_buffers.W_attn_value_prefill[layer_idx], aie_buffers.prefill.values)
    
    # Step 2: Apply RoPE to queries and keys
    aie_ops.prefill.rope_queries(aie_buffers.prefill.queries, aie_buffers.prefill.rope_angles, aie_buffers.prefill.queries)
    aie_ops.prefill.rope_keys(aie_buffers.prefill.keys, aie_buffers.prefill.rope_angles, aie_buffers.prefill.keys)
    
    # Read results from NPU
    queries = aie_buffers.prefill.queries.to("cpu").view_as_torch()[:seq_len * config.n_heads, :]
    keys = aie_buffers.prefill.keys.to("cpu").view_as_torch()[:seq_len * config.n_kv_groups, :]
    values = aie_buffers.prefill.values.to("cpu").view_as_torch()[:seq_len, :]  # (seq_len, n_kv_groups * head_dim)
    queries = queries.view(batch, seq_len, config.n_heads, config.head_dim)
    keys = keys.unsqueeze(0).view(batch, seq_len, config.n_kv_groups, config.head_dim)
    values = values.unsqueeze(0).view(batch, seq_len, config.n_kv_groups, config.head_dim) # (batch, seq_len, num_kv_groups, head_dim)

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
    group_size = config.n_heads // config.n_kv_groups
    values = values.repeat_interleave(group_size, dim=1)
    context_len = keys.shape[2]
    
    # Step 6: Compute attention scores using NPU (per-head)
    # (batch, num_heads, seq_len, head_dim) @ (batch, num_heads, head_dim, context_len)
    # -> (batch, num_heads, seq_len, context_len)
    
    queries_buf = aie_buffers.prefill.attn_scores_queries_all.view_as_torch().view(
        config.n_heads, -1, config.head_dim
    )
    queries_buf[:, :seq_len, :] = queries.squeeze(0)[:, :seq_len, :] # (num_heads, seq_len, head_dim)
    keys_buf = aie_buffers.prefill.attn_scores_keys_all.view_as_torch().view(
        config.n_kv_groups, config.head_dim, -1
    )
    keys_buf[:, :, :context_len] = keys.squeeze(0).transpose(-2, -1) # (num_kv_groups, head_dim, context_len)
    
    # Transfer parent buffers to NPU once
    aie_buffers.prefill.attn_scores_queries_all.to("npu")
    aie_buffers.prefill.attn_scores_keys_all.to("npu")
    aie_buffers.prefill.attn_scores.to("npu")
    
    # Execute GEMM for each head using sub-buffers
    for h in range(config.n_heads):
        kv_group = h // group_size
        aie_ops.prefill.attn_scores(
            aie_buffers.prefill.attn_scores_queries_per_head[h],
            aie_buffers.prefill.attn_scores_keys_per_kv_group[kv_group],
            aie_buffers.prefill.attn_scores_per_head[h]
        )
    
    # Read back all results at once from parent buffer and apply scaling on NPU
    aie_ops.prefill.attn_scale(aie_buffers.prefill.attn_scores, aie_buffers.prefill.attn_scale_factor, aie_buffers.prefill.attn_scores)
    aie_buffers.prefill.attn_scores.to("cpu")
    # Buffer is (n_heads * max_seq_len, max_seq_len), view as (n_heads, max_seq_len, max_seq_len) then slice
    max_seq_len = aie_buffers.prefill.attn_scores.shape[0] // config.n_heads
    scores = aie_buffers.prefill.attn_scores.view_as_torch().view(config.n_heads, max_seq_len, max_seq_len).unsqueeze(0)[:, :, :seq_len, :context_len]
    
    # Step 7: Apply mask
    # This ensures causality, so that tokens in the future cannot attend to tokens in the past.
    if mask is not None:
        scores = scores.masked_fill(mask, float('-inf'))
    
    # Step 8: Apply softmax on CPU
    scores = torch.softmax(scores.to(torch.float32), dim=-1).to(torch.bfloat16)
    attention_weights = scores
    
    # Step 9: Compute attention output
    # (batch, num_heads, seq_len, seq_len) @ (batch, num_heads, seq_len, head_dim)
    # -> (batch, num_heads, seq_len, head_dim)
    context = torch.matmul(attention_weights, values)
    
    # Step 10: Concatenate heads and project
    # (batch, seq_len, num_heads, head_dim) -> (batch, seq_len, num_heads * head_dim)
    context = context.transpose(1, 2).contiguous().view(batch, seq_len, -1)
    
    output = torch.nn.functional.linear(context, config.weights[f'model.layers.{layer_idx}.self_attn.o_proj.weight'])
    
    return output, keys_cache, values_cache


def swiglu_ffn_forward_prefill(layer_idx):
    # Step 1: Gate projection
    aie_ops.prefill.ffn_up_gate(aie_buffers.prefill.x_norm, aie_buffers.W_ffn_gate_prefill[layer_idx], aie_buffers.prefill.ffn_gate)
    
    # Step 2: Up projection
    aie_ops.prefill.ffn_up_gate(aie_buffers.prefill.x_norm, aie_buffers.W_ffn_up_prefill[layer_idx], aie_buffers.prefill.ffn_up)
    
    # Step 3: Apply SiLU activation
    aie_ops.prefill.ffn_silu(aie_buffers.prefill.ffn_gate, aie_buffers.prefill.ffn_gate)
    
    # Step 4: Element-wise multiplication
    aie_ops.prefill.eltwise_mul_ffn(aie_buffers.prefill.ffn_gate, aie_buffers.prefill.ffn_up, aie_buffers.prefill.ffn_hidden)
    
    # Step 5: Down projection
    aie_ops.prefill.ffn_down(aie_buffers.prefill.ffn_hidden, aie_buffers.W_ffn_down_prefill[layer_idx], aie_buffers.prefill.ffn_output)


def transformer_block_forward_prefill(
    config,
    seq_len,
    layer_idx,
    attn_keys_cache,
    attn_values_cache,
    attn_mask
):
    # Step 1: RMS normalization
    aie_ops.prefill.rms_norm(aie_buffers.prefill.x, aie_buffers.W_norm1[layer_idx], aie_buffers.prefill.x_norm)
    aie_buffers.prefill.x_norm.to("cpu")
    x_norm = aie_buffers.prefill.x_norm.view_as_torch().unsqueeze(0)[:, :seq_len, :]

    # Step 2: Attention
    attn_output, attn_keys, attn_values = grouped_query_attention_forward_prefill(
        config,
        x_norm,
        attn_keys_cache,
        attn_values_cache,
        layer_idx,
        attn_mask,
    )
    
    # Step 3: Residual
    aie_buffers.prefill.attn_output.view_as_torch().unsqueeze(0)[0, :seq_len, :] = attn_output
    aie_ops.prefill.residual_add(aie_buffers.prefill.x, aie_buffers.prefill.attn_output, aie_buffers.prefill.x)
    x = aie_buffers.prefill.x.to("cpu").view_as_torch().unsqueeze(0)[:, :seq_len, :]
    
    # Step 4: Post-norm
    aie_buffers.prefill.x.view_as_torch().unsqueeze(0)[0, :seq_len, :] = x
    aie_ops.prefill.rms_norm(aie_buffers.prefill.x, aie_buffers.W_norm2[layer_idx], aie_buffers.prefill.x_norm)
    aie_buffers.prefill.x_norm.to("cpu")
    x_norm = aie_buffers.prefill.x_norm.view_as_torch().unsqueeze(0)[:, :seq_len, :]
    
    # Step 5: Feed-forward network
    swiglu_ffn_forward_prefill(layer_idx)
    
    # Step 6: Residual
    aie_ops.prefill.residual_add(aie_buffers.prefill.x, aie_buffers.prefill.ffn_output, aie_buffers.prefill.x)
    
    return attn_keys, attn_values


def llama_forward_pass_prefill(
    config,
    state
):
    batch, seq_len = state.token_ids.shape
    
    # Step 1: RoPE angles
    num_preceding_tokens = state.attn_keys_caches[0].shape[2]
    angles_slice = config.angles[num_preceding_tokens : num_preceding_tokens + seq_len]
    aie_buffers.prefill.rope_angles.view_as_torch()[:seq_len, :] = angles_slice

    # Step 2: Token embedding
    tok_emb_weight = config.weights['model.embed_tokens.weight']
    x = torch.nn.functional.embedding(state.token_ids, tok_emb_weight)
    attn_mask = torch.triu(
        torch.ones(seq_len, seq_len, device=x.device, dtype=torch.bool),
        diagonal=1
    )
    aie_buffers.prefill.x.view_as_torch().unsqueeze(0)[0, :seq_len, :] = x

    # Step 3: Transformer blocks
    for layer_idx in range(config.n_layers):
        state.attn_keys_caches[layer_idx], state.attn_values_caches[layer_idx] = transformer_block_forward_prefill(
            config,
            seq_len,
            layer_idx,
            state.attn_keys_caches[layer_idx],
            state.attn_values_caches[layer_idx],
            attn_mask=attn_mask,
        )

    # Step 4: Final normalization
    aie_ops.prefill.rms_norm(aie_buffers.prefill.x, aie_buffers.W_final_norm, aie_buffers.prefill.x)
    
    # Step 5: Output projection
    for i in range(config.vocab_partitions):
        aie_ops.prefill.out_head(aie_buffers.prefill.x, aie_buffers.W_out_head_parts[i], aie_buffers.prefill.logits_parts[i])
    aie_buffers.prefill.logits.to("cpu")
    logits_padded_partitioned = aie_buffers.prefill.logits.view_as_torch()
    logits_padded = logits_padded_partitioned.transpose(0, 1).contiguous().view(-1, config.padded_vocab_size)
    logits = logits_padded.unsqueeze(0)[:,:seq_len,:config.vocab_size]

    # Step 6: Initialize per-layer NPU cache buffers with current cache state for decode phase
    for layer_idx in range(config.n_layers):
        cache_len = state.attn_keys_caches[layer_idx].shape[2]
        aie_buffers.keys_cache[layer_idx].view_as_torch()[:, :cache_len, :] = state.attn_keys_caches[layer_idx].squeeze(0)
        aie_buffers.values_cache[layer_idx].view_as_torch()[:, :cache_len, :] = state.attn_values_caches[layer_idx].squeeze(0)
        aie_buffers.keys_cache[layer_idx].to("npu")
        aie_buffers.values_cache[layer_idx].to("npu")

    return logits, state


# Decode
# ##########################################################################

def patch_operators_for_decode(config, num_preceding_tokens):
    context_len = num_preceding_tokens + 1
    
    # Patch strided copy operator for cache offset
    output_offset = num_preceding_tokens * config.head_dim
    offset_val = output_offset * 2  # Multiply by 2 for bfloat16 byte offset
    strided_copy_patches = {
        39: (offset_val, 0xFFFFFFFF),
        56: (offset_val, 0xFFFFFFFF),
    }
    aie_ops.decode.strided_copy_cache.patch(strided_copy_patches)
    
    # Patch softmax operator for actual context length
    softmax_patches = {8: (context_len, 0xFFFFFFFF)}
    aie_ops.decode.softmax.patch(softmax_patches)


def llama_forward_pass_decode(config, state):
    batch, seq_len = state.token_ids.shape
    assert seq_len == 1 

    patch_operators_for_decode(config, state.num_preceding_tokens)

    # Step 1: Prefill RoPE angle look-up tables
    angles_slice = config.angles[state.num_preceding_tokens : state.num_preceding_tokens + seq_len]
    aie_buffers.decode.rope_angles.view_as_torch()[:] = angles_slice

    # Step 2: Token embedding (on CPU)
    tok_emb_weight = config.weights['model.embed_tokens.weight']
    x = torch.nn.functional.embedding(state.token_ids, tok_emb_weight)
    aie_buffers.decode.x.view_as_torch().unsqueeze(0)[0, :seq_len, :] = x

    # Step 3: Transformer blocks
    for layer_idx in range(config.n_layers):
        transformer_block_forward_decode(
            config,
            state.num_preceding_tokens,
            layer_idx,
        )
    aie_ops.decode.rms_norm(aie_buffers.decode.x, aie_buffers.W_final_norm, aie_buffers.decode.x) # Step 4: Final normalization
    aie_ops.decode.gemv_out_head(aie_buffers.W_out_head, aie_buffers.decode.x, aie_buffers.decode.logits)  # Step 5: Output projection

    # Read outputs from NPU to CPU
    aie_buffers.decode.logits.to("cpu")
    logits = aie_buffers.decode.logits.view_as_torch().view(1, 1, config.vocab_size)

    return logits, state


def transformer_block_forward_decode(config, num_preceding_tokens, layer_idx):
    aie_ops.decode.rms_norm(aie_buffers.decode.x, aie_buffers.W_norm1[layer_idx], aie_buffers.decode.x_norm) # Step 1: RMS normalization
    grouped_query_attention_forward_decode(config, num_preceding_tokens, layer_idx) # Step 2: Attention; results stored in attn_output
    aie_ops.decode.residual_add(aie_buffers.decode.x, aie_buffers.decode.attn_output, aie_buffers.decode.x) # Step 3: Residual
    aie_ops.decode.rms_norm(aie_buffers.decode.x, aie_buffers.W_norm2[layer_idx], aie_buffers.decode.x_norm) # Step 4: Post-norm
    swiglu_ffn_forward_decode(layer_idx) # Step 5: Feed-forward network
    aie_ops.decode.residual_add(aie_buffers.decode.x, aie_buffers.decode.ffn_output, aie_buffers.decode.x) # Step 6: Residual


def grouped_query_attention_forward_decode(config, num_preceding_tokens, layer_idx):
    context_len = num_preceding_tokens + 1
    group_size = config.n_heads // config.n_kv_groups

    # Step 1: Linear projections - write directly to queries/keys/values buffers
    aie_ops.decode.gemv_attn_query(aie_buffers.W_attn_query_decode[layer_idx], aie_buffers.decode.x_norm, aie_buffers.decode.queries)
    aie_ops.decode.gemv_attn_key_value(aie_buffers.W_attn_key_decode[layer_idx], aie_buffers.decode.x_norm, aie_buffers.decode.keys)
    aie_ops.decode.gemv_attn_key_value(aie_buffers.W_attn_value_decode[layer_idx], aie_buffers.decode.x_norm, aie_buffers.decode.values)
    
    # Step 2: Apply RoPE - use same buffers for input and output
    aie_ops.decode.rope_queries(aie_buffers.decode.queries, aie_buffers.decode.rope_angles, aie_buffers.decode.queries)
    aie_ops.decode.rope_keys(aie_buffers.decode.keys, aie_buffers.decode.rope_angles, aie_buffers.decode.keys)
    
    # Step 3: Update cache using strided copy on NPU (transpose and concatenate)
    # Cache is already on NPU from prefill initialization or previous decode iteration
    # Transpose and append new keys/values to this layer's cache on NPU
    aie_ops.decode.strided_copy_cache(aie_buffers.decode.keys, aie_buffers.keys_cache[layer_idx])
    aie_ops.decode.strided_copy_cache(aie_buffers.decode.values, aie_buffers.values_cache[layer_idx])
    
    # Step 4: Repeat keys and values for grouped attention using AIERepeat on NPU
    aie_ops.decode.attn_repeat_interleave(aie_buffers.keys_cache[layer_idx], aie_buffers.decode.attn_scores_keys)
    aie_ops.decode.attn_repeat_interleave(aie_buffers.values_cache[layer_idx], aie_buffers.decode.attn_scores_values)
    
    # Step 5: Compute attention scores
    # Copy repeated keys from keys_repeated buffer to attn_scores_keys for GEMV
    aie_ops.decode.gemv_attn_scores(aie_buffers.decode.attn_scores_keys, aie_buffers.decode.queries, aie_buffers.decode.attn_scores)
    aie_ops.decode.attn_scale(aie_buffers.decode.attn_scores, aie_buffers.decode.attn_scale_factor, aie_buffers.decode.attn_scores)
    
    # Step 7: Softmax on NPU (patched once at beginning of decode pass)
    aie_ops.decode.softmax(aie_buffers.decode.attn_scores, aie_buffers.decode.attn_weights)
    
    # Step 8: Compute attention output on NPU
    # Transpose values: (max_context_len, head_dim) -> (head_dim, max_context_len) for each head
    for h in range(config.n_heads):
        aie_ops.decode.transpose_values(
            aie_buffers.decode.attn_scores_values_per_head[h],
            aie_buffers.decode.attn_scores_values_transposed_per_head[h]
        )
    # GEMV: (n_heads, head_dim, max_context_len) @ (n_heads, max_context_len) -> (n_heads, head_dim)
    aie_ops.decode.gemv_attn_context(aie_buffers.decode.attn_scores_values_transposed, aie_buffers.decode.attn_weights, aie_buffers.decode.attn_context)
    
    # Step 9: Project on NPU: (emb_dim, n_heads * head_dim) @ (n_heads * head_dim,) -> (emb_dim,)
    aie_ops.decode.gemv_attn_output(aie_buffers.W_attn_output_decode[layer_idx], aie_buffers.decode.attn_context, aie_buffers.decode.attn_output)


def swiglu_ffn_forward_decode(layer_idx):
    aie_ops.decode.gemv_ffn_up_gate(aie_buffers.W_ffn_gate_decode[layer_idx], aie_buffers.decode.x_norm, aie_buffers.decode.ffn_gate)  # Gate projection
    aie_ops.decode.gemv_ffn_up_gate(aie_buffers.W_ffn_up_decode[layer_idx], aie_buffers.decode.x_norm, aie_buffers.decode.ffn_up)  # Up projection
    aie_ops.decode.ffn_silu(aie_buffers.decode.ffn_gate, aie_buffers.decode.ffn_gate)  # SiLU activation
    aie_ops.decode.eltwise_mul_ffn(aie_buffers.decode.ffn_gate, aie_buffers.decode.ffn_up, aie_buffers.decode.ffn_hidden)  # Gate application (eltwise mul)
    aie_ops.decode.gemv_ffn_down(aie_buffers.W_ffn_down_decode[layer_idx], aie_buffers.decode.ffn_hidden, aie_buffers.decode.ffn_output)  # Down projection


# Main
# ##########################################################################

def llama_forward_pass(
    config,
    state
):
    batch, seq_len = state.token_ids.shape
    if seq_len > 1:
        ret = llama_forward_pass_prefill(config, state)
        state.num_preceding_tokens = state.token_ids.shape[1]
        return ret
    else:
        ret = llama_forward_pass_decode(config, state)
        state.num_preceding_tokens += 1
        return ret


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
