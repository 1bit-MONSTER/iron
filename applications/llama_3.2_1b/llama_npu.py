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
from operators.common.aie_base import PatchableSingleXclbinCallable
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
from operators.mha.op import AIEMHA

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
        # Replaced by Fused MHA
        # self.prefill.attn_scale = AIEElementwiseMul(
        #     size=config.n_heads * prompt_len * prompt_len,
        #     tile_size=prompt_len,
        #     num_aie_columns=8,
        #     context=self.context
        # ).compile().get_callable()

        # Fused MHA
        self.prefill.mha_compilable = AIEMHA(
            num_heads=config.n_heads,
            seq_len=prompt_len,
            d=config.head_dim,
            num_KV_heads=config.n_kv_groups,
            num_of_pipelines=8,
            context=self.context
        ).compile()
        self.prefill.mha = self.prefill.mha_compilable.get_callable()
        
        self.decode.attn_scale = AIEElementwiseMul(
            size=config.n_heads * prompt_len,
            tile_size=prompt_len // 8,
            num_aie_columns=8,
            context=self.context
        ).compile().get_callable()
        
        # Softmax operators for attention weights
        # Replaced by Fused MHA
        # self.prefill.softmax_compilable = AIESoftmax(
        #     rows=config.n_heads * prompt_len,
        #     cols=prompt_len,
        #     num_aie_columns=8,
        #     num_channels=1,
        #     rtp_vector_size=prompt_len,  # Compile with max size
        #     context=self.context
        # ).compile()
        
        # self.prefill.softmax = PatchableSingleXclbinCallable(
        #     xclbin_path=self.prefill.softmax_compilable.xclbin_artifact.path,
        #     kernel_name=self.prefill.softmax_compilable.xclbin_artifact.kernel_name,
        #     insts_bin_path=self.prefill.softmax_compilable.insts_artifact.path,
        #     args_spec=self.prefill.softmax_compilable.get_arg_spec()
        # )
        
        self.decode.softmax_compilable = AIESoftmax(
            rows=config.n_heads,
            cols=prompt_len,
            num_aie_columns=1,
            num_channels=1,
            rtp_vector_size=prompt_len,  # Compile with max size
            context=self.context
        ).compile()
        
        self.decode.softmax = PatchableSingleXclbinCallable(
            xclbin_path=self.decode.softmax_compilable.xclbin_artifact.path,
            kernel_name=self.decode.softmax_compilable.xclbin_artifact.kernel_name,
            insts_bin_path=self.decode.softmax_compilable.insts_artifact.path,
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
            xclbin_path=self.decode.strided_copy_cache_compilable.xclbin_artifact.path,
            kernel_name=self.decode.strided_copy_cache_compilable.xclbin_artifact.kernel_name,
            insts_bin_path=self.decode.strided_copy_cache_compilable.insts_artifact.path,
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
        
        self.decode.gemv_attn_key = AIEGEMV(
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
        
        self.decode.gemv_attn_value = AIEGEMV(
            M=config.n_kv_groups * config.head_dim,
            K=config.emb_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=config.head_dim // 2,
            context=self.context
        ).compile().get_callable()
        
        # Attention score computation: Q @ K^T per head
        # For prefill: (seq_len, head_dim) @ (head_dim, seq_len) = (seq_len, seq_len) per head
        # Replaced by Fused MHA
        # self.prefill.attn_scores = AIEGEMM(
        #     M=prompt_len,
        #     K=config.head_dim,
        #     N=prompt_len,
        #     num_aie_columns=8,
        #     tile_m=64,
        #     tile_k=64,
        #     tile_n=64,
        #     b_col_maj=False,
        #     context=self.context
        # ).compile().get_callable()
        
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
        # Replaced by Fused MHA buffers
        # Parent buffer for all heads' queries: (n_heads, prompt_len, head_dim) stored contiguously
        # self.attn_scores_queries_all = AIEBuffer(shape=(n_heads * prompt_len, head_dim), dtype=ml_dtypes.bfloat16)
        # self.attn_scores_queries_per_head = [
        #     self.attn_scores_queries_all.subbuffer(
        #         length=prompt_len * head_dim,
        #         offset=h * prompt_len * head_dim,
        #         shape=(prompt_len, head_dim)
        #     )
        #     for h in range(n_heads)
        # ]
        # # Parent buffer for all KV groups' keys: (n_kv_groups, head_dim, prompt_len) stored contiguously
        # self.attn_scores_keys_all = AIEBuffer(shape=(n_kv_groups * head_dim, prompt_len), dtype=ml_dtypes.bfloat16)
        # self.attn_scores_keys_per_kv_group = [
        #     self.attn_scores_keys_all.subbuffer(
        #         length=head_dim * prompt_len,
        #         offset=g * head_dim * prompt_len,
        #         shape=(head_dim, prompt_len)
        #     )
        #     for g in range(n_kv_groups)
        # ]
        # # Parent buffer for all heads' scores: (n_heads * prompt_len, prompt_len)
        # self.attn_scores = AIEBuffer(shape=(n_heads * prompt_len, prompt_len), dtype=ml_dtypes.bfloat16)
        # self.attn_scores_per_head = [
        #     self.attn_scores.subbuffer(
        #         length=prompt_len * prompt_len,
        #         offset=h * prompt_len * prompt_len,
        #         shape=(prompt_len, prompt_len)
        #     )
        #     for h in range(n_heads)
        # ]
        # # Attention score scaling buffer (pre-initialized with 1/sqrt(head_dim))
        # scale_factor = 1.0 / math.sqrt(head_dim)
        # self.attn_scale_factor = AIEBuffer(shape=(n_heads * prompt_len, prompt_len), dtype=ml_dtypes.bfloat16)
        # self.attn_scale_factor.view_as_torch()[:] = scale_factor
        # self.attn_scale_factor.to("npu")
        # # Attention weights buffer (output of softmax)
        # self.attn_weights = AIEBuffer(shape=(n_heads * prompt_len, prompt_len), dtype=ml_dtypes.bfloat16)

        # MHA buffers
        # Calculate padded sequence length (assuming num_of_pipelines=8)
        num_pipelines = 8
        S_pad = ((prompt_len + 63 * num_pipelines) // (64 * num_pipelines)) * (64 * num_pipelines)
        
        self.mha_q = AIEBuffer(shape=(n_heads * S_pad * head_dim,), dtype=ml_dtypes.bfloat16)
        self.mha_k = AIEBuffer(shape=(n_kv_groups * S_pad * head_dim,), dtype=ml_dtypes.bfloat16)
        self.mha_v = AIEBuffer(shape=(n_kv_groups * S_pad * head_dim,), dtype=ml_dtypes.bfloat16)
        self.mha_o = AIEBuffer(shape=(n_heads * S_pad * head_dim,), dtype=ml_dtypes.bfloat16)

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


# Operators
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
    # Since we padded x, the outputs are also padded (max_seq_len)
    max_seq_len = aie_buffers.prefill.queries.shape[0] // config.n_heads
    
    queries = aie_buffers.prefill.queries.to("cpu").view_as_torch()
    keys = aie_buffers.prefill.keys.to("cpu").view_as_torch()
    values = aie_buffers.prefill.values.to("cpu").view_as_torch()
    
    queries = queries.view(batch, max_seq_len, config.n_heads, config.head_dim)
    keys = keys.unsqueeze(0).view(batch, max_seq_len, config.n_kv_groups, config.head_dim)
    values = values.unsqueeze(0).view(batch, max_seq_len, config.n_kv_groups, config.head_dim)

    # Step 3: Transpose for attention computation
    queries = queries.transpose(1, 2)  # (batch, num_heads, max_seq_len, head_dim)
    keys = keys.transpose(1, 2)        # (batch, num_kv_groups, max_seq_len, head_dim)
    values = values.transpose(1, 2)    # (batch, num_kv_groups, max_seq_len, head_dim)

    # Step 4: Update cache
    # We only want to cache the valid tokens, not padding
    keys_valid = keys[:, :, :seq_len, :]
    values_valid = values[:, :, :seq_len, :]
    keys_cache = torch.cat([keys_cache, keys_valid], dim=2)
    values_cache = torch.cat([values_cache, values_valid], dim=2)
    
    # For MHA, we use the padded keys/values (assuming padding is zero/masked)
    # But wait, MHA expects full context.
    # If this is first prefill, keys/values are just what we computed.
    # If we have previous cache (e.g. chunked prefill), we need to concat.
    # Assuming single prefill pass for now as per harness.
    
    # Step 5: Repeat keys and values
    # Fused MHA handles GQA internally, so we don't need to repeat keys/values on CPU
    # group_size = config.n_heads // config.n_kv_groups
    # values = values.repeat_interleave(group_size, dim=1)
    # keys = keys.repeat_interleave(group_size, dim=1)

    # Step 6: Compute attention output using Fused MHA on NPU
    q_in = queries.squeeze(0)
    k_in = keys.squeeze(0)
    v_in = values.squeeze(0)
    
    # Write to buffers (already padded size)
    aie_buffers.prefill.mha_q.view_as_torch()[:] = q_in.flatten()
    aie_buffers.prefill.mha_k.view_as_torch()[:] = k_in.flatten()
    aie_buffers.prefill.mha_v.view_as_torch()[:] = v_in.flatten()
    
    aie_buffers.prefill.mha_q.to("npu")
    aie_buffers.prefill.mha_k.to("npu")
    aie_buffers.prefill.mha_v.to("npu")
    
    # Call MHA
    aie_ops.prefill.mha(
        aie_buffers.prefill.mha_q,
        aie_buffers.prefill.mha_k,
        aie_buffers.prefill.mha_v,
        aie_buffers.prefill.mha_o
    )
    
    # Read output
    aie_buffers.prefill.mha_o.to("cpu")
    context_vec_flat = aie_buffers.prefill.mha_o.view_as_torch()
    
    # Reshape to (num_heads, S_pad, head_dim)
    # S_pad is max_seq_len here
    context_vec = context_vec_flat.view(config.n_heads, max_seq_len, config.head_dim)
    
    # Slice back to original length
    # context_vec is (num_heads, max_seq_len, head_dim)
    # We keep it padded for subsequent layers
    context = context_vec.unsqueeze(0) # (1, num_heads, max_seq_len, head_dim)
    
    # Step 10: Concatenate heads and project
    # (batch, max_seq_len, num_heads, head_dim) -> (batch, max_seq_len, num_heads * head_dim)
    context = context.transpose(1, 2).contiguous().view(batch, max_seq_len, -1)
    
    # Output projection runs on padded input
    # We need to write to aie_buffers.prefill.attn_output which is used for residual
    # But torch.nn.functional.linear is CPU.
    # Wait, we should use NPU for output projection if possible?
    # llama_npu.py doesn't seem to have prefill.out_proj operator?
    # Ah, it returns `output` and then:
    # aie_buffers.prefill.attn_output.view_as_torch().unsqueeze(0)[0, :seq_len, :] = attn_output
    
    # So we compute output on CPU using torch.linear
    output = torch.nn.functional.linear(context, config.weights[f'model.layers.{layer_idx}.self_attn.o_proj.weight'])
    
    # Slice output to valid length for return (or keep padded?)
    # transformer_block_forward_prefill expects to write to attn_output buffer.
    # If we return padded output, we should write padded output.
    
    return output, keys_cache, values_cache


def grouped_query_attention_forward_decode(
    config,
    x, 
    num_preceding_tokens,
    layer_idx,
    mask=None,
):
    batch, seq_len, emb_dim = x.shape

    # Step 1: Linear projections - write directly to queries/keys/values buffers
    aie_ops.decode.gemv_attn_query(aie_buffers.W_attn_query_decode[layer_idx], aie_buffers.decode.x_norm, aie_buffers.decode.queries)
    aie_ops.decode.gemv_attn_key(aie_buffers.W_attn_key_decode[layer_idx], aie_buffers.decode.x_norm, aie_buffers.decode.keys)
    aie_ops.decode.gemv_attn_value(aie_buffers.W_attn_value_decode[layer_idx], aie_buffers.decode.x_norm, aie_buffers.decode.values)
    
    # Step 2: Apply RoPE - use same buffers for input and output
    aie_ops.decode.rope_queries(aie_buffers.decode.queries, aie_buffers.decode.rope_angles, aie_buffers.decode.queries)
    aie_ops.decode.rope_keys(aie_buffers.decode.keys, aie_buffers.decode.rope_angles, aie_buffers.decode.keys)
    
    # Read results from NPU for CPU reference computation
    aie_buffers.decode.queries.to("cpu")
    queries = aie_buffers.decode.queries.view_as_torch()[:seq_len * config.n_heads, :]
    # Since seq_len=1, the transpose is just a reinterpretation of the shape; no actual data movement needed
    queries = queries.view(batch, config.n_heads, 1, config.head_dim)
    
    # Step 3: Update cache using strided copy on NPU (transpose and concatenate)
    # Cache is already on NPU from prefill initialization or previous decode iteration
    context_len = num_preceding_tokens + seq_len
    
    # Transpose and append new keys/values to this layer's cache on NPU
    aie_ops.decode.strided_copy_cache(aie_buffers.decode.keys, aie_buffers.keys_cache[layer_idx])
    aie_ops.decode.strided_copy_cache(aie_buffers.decode.values, aie_buffers.values_cache[layer_idx])
    
    # Step 4: Repeat keys and values for grouped attention using AIERepeat on NPU
    group_size = config.n_heads // config.n_kv_groups
    aie_ops.decode.attn_repeat_interleave(aie_buffers.keys_cache[layer_idx], aie_buffers.decode.attn_scores_keys)
    aie_ops.decode.attn_repeat_interleave(aie_buffers.values_cache[layer_idx], aie_buffers.decode.attn_scores_values)
    
    # Step 5: Compute attention scores
    # Copy repeated keys from keys_repeated buffer to attn_scores_keys for GEMV
    aie_ops.decode.gemv_attn_scores(aie_buffers.decode.attn_scores_keys, aie_buffers.decode.queries, aie_buffers.decode.attn_scores)
    # Apply scaling on NPU
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
    
    # Read context from NPU
    aie_buffers.decode.attn_context.to("cpu")
    context = aie_buffers.decode.attn_context.view_as_torch().unsqueeze(1)  # (n_heads, 1, head_dim)
    
    # Step 9: Concatenate heads and project
    # (n_heads, 1, head_dim) -> (n_heads, head_dim, 1) -> (1, 1, n_heads * head_dim)
    context = context.transpose(1, 2).contiguous().view(batch, seq_len, -1)
    # (1, 1, n_heads * head_dim) @ (emb_dim, n_heads * head_dim)^T -> (1, 1, emb_dim)
    output = torch.nn.functional.linear(context, config.weights[f'model.layers.{layer_idx}.self_attn.o_proj.weight'])
    
    return output, None, None


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


def swiglu_ffn_forward_decode(layer_idx):
    # Step 1: Gate projection
    aie_ops.decode.gemv_ffn_up_gate(aie_buffers.W_ffn_gate_decode[layer_idx], aie_buffers.decode.x_norm, aie_buffers.decode.ffn_gate)
    
    # Step 2: Up projection
    aie_ops.decode.gemv_ffn_up_gate(aie_buffers.W_ffn_up_decode[layer_idx], aie_buffers.decode.x_norm, aie_buffers.decode.ffn_up)
    
    # Step 3: Apply SiLU activation
    aie_ops.decode.ffn_silu(aie_buffers.decode.ffn_gate, aie_buffers.decode.ffn_gate)
    
    # Step 4: Element-wise multiplication
    aie_ops.decode.eltwise_mul_ffn(aie_buffers.decode.ffn_gate, aie_buffers.decode.ffn_up, aie_buffers.decode.ffn_hidden)
    
    # Step 5: Down projection
    aie_ops.decode.gemv_ffn_down(aie_buffers.W_ffn_down_decode[layer_idx], aie_buffers.decode.ffn_hidden, aie_buffers.decode.ffn_output)


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
    # attn_output is padded (max_seq_len)
    aie_buffers.prefill.attn_output.view_as_torch()[:] = attn_output.squeeze(0)
    aie_ops.prefill.residual_add(aie_buffers.prefill.x, aie_buffers.prefill.attn_output, aie_buffers.prefill.x)
    # x is updated in place on NPU (padded)
    
    # Step 4: Post-norm
    aie_ops.prefill.rms_norm(aie_buffers.prefill.x, aie_buffers.W_norm2[layer_idx], aie_buffers.prefill.x_norm)
    aie_buffers.prefill.x_norm.to("cpu")
    x_norm = aie_buffers.prefill.x_norm.view_as_torch().unsqueeze(0) # Padded
    
    # Step 5: Feed-forward network
    swiglu_ffn_forward_prefill(layer_idx)
    
    # Step 6: Residual
    aie_ops.prefill.residual_add(aie_buffers.prefill.x, aie_buffers.prefill.ffn_output, aie_buffers.prefill.x)
    
    return attn_keys, attn_values


def transformer_block_forward_decode(
    config,
    seq_len,
    num_preceding_tokens,
    layer_idx,
    attn_mask
):
    # Step 1: RMS normalization
    aie_ops.decode.rms_norm(aie_buffers.decode.x, aie_buffers.W_norm1[layer_idx], aie_buffers.decode.x_norm)
    aie_buffers.decode.x_norm.to("cpu")
    x_norm = aie_buffers.decode.x_norm.view_as_torch().unsqueeze(0)[:, :seq_len, :]

    # Step 2: Attention
    attn_output, attn_keys, attn_values = grouped_query_attention_forward_decode(
        config,
        x_norm,
        num_preceding_tokens,
        layer_idx,
        attn_mask,
    )
    
    # Step 3: Residual
    aie_buffers.decode.attn_output.view_as_torch().unsqueeze(0)[0, :seq_len, :] = attn_output
    aie_ops.decode.residual_add(aie_buffers.decode.x, aie_buffers.decode.attn_output, aie_buffers.decode.x)
    x = aie_buffers.decode.x.to("cpu").view_as_torch().unsqueeze(0)[:, :seq_len, :]
    
    # Step 4: Post-norm
    aie_buffers.decode.x.view_as_torch().unsqueeze(0)[0, :seq_len, :] = x
    aie_ops.decode.rms_norm(aie_buffers.decode.x, aie_buffers.W_norm2[layer_idx], aie_buffers.decode.x_norm)
    aie_buffers.decode.x_norm.to("cpu")
    x_norm = aie_buffers.decode.x_norm.view_as_torch().unsqueeze(0)[:, :seq_len, :]
    
    # Step 5: Feed-forward network
    swiglu_ffn_forward_decode(layer_idx)
    
    # Step 6: Residual
    aie_ops.decode.residual_add(aie_buffers.decode.x, aie_buffers.decode.ffn_output, aie_buffers.decode.x)
    
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
    
    # Patch softmax operator once for this prefill pass with the context length
    # Replaced by Fused MHA
    # context_len = num_preceding_tokens + seq_len
    # softmax_patches = {8: (context_len, 0xFFFFFFFF)}
    # aie_ops.prefill.softmax.patch(softmax_patches)

    # Step 2: Token embedding
    tok_emb_weight = config.weights['model.embed_tokens.weight']
    x = torch.nn.functional.embedding(state.token_ids, tok_emb_weight)
    attn_mask = torch.triu(
        torch.ones(seq_len, seq_len, device=x.device, dtype=torch.bool),
        diagonal=1
    )
    
    # Pad x to max_seq_len (prompt_len) to run fully on NPU
    max_seq_len = aie_buffers.prefill.x.shape[0]
    if seq_len < max_seq_len:
        pad_len = max_seq_len - seq_len
        x_padded = torch.nn.functional.pad(x, (0, 0, 0, pad_len))
    else:
        x_padded = x
        
    aie_buffers.prefill.x.view_as_torch()[:] = x_padded.squeeze(0)

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
    # logits_padded_partitioned shape: (partitions, max_seq_len, vocab_part)
    logits_padded = logits_padded_partitioned.transpose(0, 1).contiguous().view(-1, config.padded_vocab_size)
    # Slice to valid seq_len
    logits = logits_padded.unsqueeze(0)[:,:seq_len,:config.vocab_size]

    # Step 6: Initialize per-layer NPU cache buffers with current cache state for decode phase
    for layer_idx in range(config.n_layers):
        cache_len = state.attn_keys_caches[layer_idx].shape[2]
        aie_buffers.keys_cache[layer_idx].view_as_torch()[:, :cache_len, :] = state.attn_keys_caches[layer_idx].squeeze(0)
        aie_buffers.values_cache[layer_idx].view_as_torch()[:, :cache_len, :] = state.attn_values_caches[layer_idx].squeeze(0)
        aie_buffers.keys_cache[layer_idx].to("npu")
        aie_buffers.values_cache[layer_idx].to("npu")

    return logits, state


def llama_forward_pass_decode(
    config,
    state,
):
    batch, seq_len = state.token_ids.shape

    # Patch operators once for all layers with current context length
    num_preceding_tokens = state.num_preceding_tokens
    context_len = num_preceding_tokens + seq_len
    
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

    # Step 1: RoPE angles
    angles_slice = config.angles[num_preceding_tokens : num_preceding_tokens + seq_len]
    aie_buffers.decode.rope_angles.view_as_torch()[:] = angles_slice

    # Step 2: Token embedding
    tok_emb_weight = config.weights['model.embed_tokens.weight']
    x = torch.nn.functional.embedding(state.token_ids, tok_emb_weight)
    attn_mask = torch.triu(
        torch.ones(seq_len, seq_len, device=x.device, dtype=torch.bool),
        diagonal=1
    )
    aie_buffers.decode.x.view_as_torch().unsqueeze(0)[0, :seq_len, :] = x

    # Step 3: Transformer blocks
    for layer_idx in range(config.n_layers):
        state.attn_keys_caches[layer_idx], state.attn_values_caches[layer_idx] = transformer_block_forward_decode(
            config,
            seq_len,
            num_preceding_tokens,
            layer_idx,
            attn_mask=attn_mask,
        )

    # Step 4: Final normalization
    aie_ops.decode.rms_norm(aie_buffers.decode.x, aie_buffers.W_final_norm, aie_buffers.decode.x)
    
    # Step 5: Output projection
    aie_ops.decode.gemv_out_head(aie_buffers.W_out_head, aie_buffers.decode.x, aie_buffers.decode.logits)
    aie_buffers.decode.logits.to("cpu")
    logits = aie_buffers.decode.logits.view_as_torch().view(1, 1, config.vocab_size)

    return logits, state


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
