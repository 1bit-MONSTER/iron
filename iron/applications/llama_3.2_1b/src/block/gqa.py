# Copyright (c) Sebastian Raschka under Apache License 2.0.
# Source for "Build a Large Language Model From Scratch"
#   - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Code: https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/standalone-llama32.ipynb
#
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import torch
import torch.nn as nn

from iron.operators import AIERope, AIESoftmax, AIEMHA, AIEGEMM, AIEGEMV
from iron.operators.rope.rope_utils import apply_rope

from torchtune.modules import KVCache

from ..utils import assign


class GroupedQueryAttention(nn.Module):
    def __init__(
        self,
        d_in,
        d_out,
        num_heads,
        num_kv_groups,
        prompt_length=0,
        num_tokens=1,
        dtype=None,
        max_batch_size=1,
        max_seq_len=8192,
        cfg=None,
    ):
        super().__init__()
        assert d_out % num_heads == 0, "d_out must be divisible by num_heads"
        assert (
            num_heads % num_kv_groups == 0
        ), "num_heads must be divisible by num_kv_groups"

        self.cfg = cfg.copy() if cfg is not None else {}

        self.d_out = d_out
        self.num_heads = num_heads
        self.head_dim = d_out // num_heads

        self.num_tokens = num_tokens

        # Weights for Attention layer
        self.W_key = nn.Linear(
            d_in, num_kv_groups * self.head_dim, bias=False, dtype=dtype
        )
        self.W_value = nn.Linear(
            d_in, num_kv_groups * self.head_dim, bias=False, dtype=dtype
        )
        self.W_query = nn.Linear(d_in, d_out, bias=False, dtype=dtype)
        self.out_proj = nn.Linear(d_out, d_out, bias=False, dtype=dtype)

        self.num_kv_groups = num_kv_groups
        self.group_size = num_heads // num_kv_groups

        self.prompt_length = prompt_length

        aie_gemm_config = {
            "num_aie_columns": 8,
            "tile_m": 64,
            "tile_k": 64,
            "tile_n": 64,
            "use_static_weight": False,
        }

        # Initialize KV Cache
        if self.cfg["use_kv_cache"]:
            self.kv_cache = KVCache(
                batch_size=max_batch_size,
                max_seq_len=max_seq_len,
                num_kv_heads=self.num_kv_groups,
                head_dim=self.head_dim,
                dtype=torch.bfloat16,
            )

        # Initialize AIE Regular MHA operator
        if self.cfg["use_aie_regular_mha"]:
            self.aie_softmax = AIESoftmax(
                num_aie_columns=1,
                num_channels=1,
                rows=prompt_length,
                cols=prompt_length,
            )
            M_for_gemm = prompt_length + num_tokens
            
            # Pad dimensions to meet GEMM requirements
            num_aie_rows = 4
            tile_m = aie_gemm_config["tile_m"]
            tile_k = aie_gemm_config["tile_k"]
            tile_n = aie_gemm_config["tile_n"]
            num_cols = aie_gemm_config["num_aie_columns"]
            min_M = tile_m * num_aie_rows
            min_K = tile_k
            min_N = tile_n * num_cols
            
            M_padded = ((M_for_gemm + min_M - 1) // min_M) * min_M
            head_dim_padded = ((self.head_dim + min_K - 1) // min_K) * min_K
            
            self.aie_mha_gemm_qk = AIEGEMM(
                M=M_padded, K=head_dim_padded, N=M_padded, **aie_gemm_config
            )
            self.aie_mha_gemm_pv = AIEGEMM(
                M=M_padded, K=M_padded, N=head_dim_padded, **aie_gemm_config
            )

        # Initialize AIE RoPE operator
        if self.cfg["use_aie_rope"]:
            self.aie_rope_prefill_k = AIERope(
                rows=self.prompt_length * self.num_kv_groups,
                cols=self.head_dim,
                angle_rows=self.prompt_length,
            )
            self.aie_rope_prefill_q = AIERope(
                rows=self.prompt_length * self.num_heads,
                cols=self.head_dim,
                angle_rows=self.prompt_length,
            )
            self.aie_rope_decode_k = AIERope(
                rows=self.num_kv_groups,
                cols=self.head_dim,
                angle_rows=1,
            )
            self.aie_rope_decode_q = AIERope(
                rows=self.num_heads,
                cols=self.head_dim,
                angle_rows=1,
            )

        # Initialize fused AIE MHA operator
        if self.cfg["use_aie_fused_mha"]:
            self.aie_mha = AIEMHA(
                num_heads=num_heads,
                seq_len=prompt_length,
                d=self.head_dim,
                num_KV_heads=0,  # Regular MHA since we feed repeated K/V
                num_of_pipelines=8,
            )

        # Initialize AIE GEMV operators for decode phase (when using KV cache)
        if self.cfg["use_kv_cache"] and self.cfg["use_aie_gqa_gemv"]:

            aie_gemv_config = {
                "num_aie_columns": 8,
                "use_static_weight": True,
            }
            self.aie_query_gemv = AIEGEMV(
                M=d_out,
                K=d_in,
                tile_size_input=1,
                tile_size_output=d_out // 16,
                **aie_gemv_config,
            )
            kv_out_dim = num_kv_groups * self.head_dim
            self.aie_key_gemv = AIEGEMV(
                M=kv_out_dim,
                K=d_in,
                tile_size_input=1,
                tile_size_output=kv_out_dim // 16,
                **aie_gemv_config,
            )
            self.aie_value_gemv = AIEGEMV(
                M=kv_out_dim,
                K=d_in,
                tile_size_input=1,
                tile_size_output=kv_out_dim // 16,
                **aie_gemv_config,
            )
            self.aie_out_proj_gemv = AIEGEMV(
                M=d_out,
                K=d_out,
                tile_size_input=1,
                tile_size_output=d_out // 16,
                **aie_gemv_config,
            )

        # Initialize AIE GEMM operators
        if self.cfg["use_aie_attn_projection_gemm"]:
            if self.cfg["use_kv_cache"]:
                M_for_gemm = self.prompt_length
            else:
                M_for_gemm = self.prompt_length + self.num_tokens

            # GEMMs for projection use weights
            aie_gemm_config["use_static_weight"] = True
            
            # Pad dimensions to meet GEMM requirements
            num_aie_rows = 4
            tile_m = aie_gemm_config["tile_m"]
            tile_k = aie_gemm_config["tile_k"]
            tile_n = aie_gemm_config["tile_n"]
            num_cols = aie_gemm_config["num_aie_columns"]
            min_M = tile_m * num_aie_rows
            min_K = tile_k
            min_N = tile_n * num_cols
            
            M_padded = ((M_for_gemm + min_M - 1) // min_M) * min_M
            d_in_padded = ((d_in + min_K - 1) // min_K) * min_K
            d_out_padded = ((d_out + min_N - 1) // min_N) * min_N
            kv_out_dim = num_kv_groups * self.head_dim
            kv_out_dim_padded = ((kv_out_dim + min_N - 1) // min_N) * min_N
            
            # Query: (batch_size, d_in) @ (d_in, d_out) -> (batch_size, d_out)
            self.aie_query = AIEGEMM(M=M_padded, K=d_in_padded, N=d_out_padded, **aie_gemm_config)
            # Key: (batch_size, d_in) @ (d_in, num_kv_groups * head_dim) -> (batch_size, num_kv_groups * head_dim)
            self.aie_key = AIEGEMM(
                M=M_padded, K=d_in_padded, N=kv_out_dim_padded, **aie_gemm_config
            )
            # Value: same dimensions as key
            self.aie_value = AIEGEMM(
                M=M_padded, K=d_in_padded, N=kv_out_dim_padded, **aie_gemm_config
            )
            # Output projection: (batch_size, d_out) @ (d_out, d_out) -> (batch_size, d_out)
            self.aie_out_proj = AIEGEMM(
                M=M_padded, K=d_out_padded, N=d_out_padded, **aie_gemm_config
            )

    def forward(self, x, mask, angles, input_pos=None):
        b, num_tokens, d_in = x.shape
        is_prefill = input_pos is None
        is_decode = input_pos is not None

        # Step 1.
        # ---
        # Linear projections -- calculate quries, keys and values by multiplying embedding vector (in decode) or matrix (in prefill) with weight matrices

        # Choose between GEMM (prefill) and GEMV (decode) based on KV cache usage
        if self.cfg["use_kv_cache"] and is_decode and self.cfg["use_aie_gqa_gemv"]:
            # Decode phase with KV cache - use GEMV for single token
            # GEMV arg order: [weight_matrix, input_vector, output_vector]
            x_flat = x.reshape(-1)  # Shape: (d_in,) - flatten to 1D for GEMV

            queries_flat = self._copy_and_run(
                self._aie_callables["query_gemv"],
                self._aie_buffers,
                {"query_gemv_weight": None, "query_gemv_in": x_flat, "query_gemv_out": None}
            )
            queries = queries_flat.reshape(b, num_tokens, self.d_out)

            keys_flat = self._copy_and_run(
                self._aie_callables["key_gemv"],
                self._aie_buffers,
                {"key_gemv_weight": None, "key_gemv_in": x_flat, "key_gemv_out": None}
            )
            keys = keys_flat.reshape(b, num_tokens, self.num_kv_groups * self.head_dim)

            values_flat = self._copy_and_run(
                self._aie_callables["value_gemv"],
                self._aie_buffers,
                {"value_gemv_weight": None, "value_gemv_in": x_flat, "value_gemv_out": None}
            )
            values = values_flat.reshape(
                b, num_tokens, self.num_kv_groups * self.head_dim
            )

        elif self.cfg["use_aie_attn_projection_gemm"]:
            # Prefill phase - use GEMM for multiple tokens
            x_flat = x.reshape(-1, d_in)
            input_dtype = x.dtype

            queries_flat = self._copy_and_run(
                self._aie_callables["query"],
                self._aie_buffers,
                {"query_in": x_flat, "query_weight": None, "query_out": None}
            )
            queries = queries_flat.reshape(b, num_tokens, self.d_out)

            keys_flat = self._copy_and_run(
                self._aie_callables["key"],
                self._aie_buffers,
                {"key_in": x_flat, "key_weight": None, "key_out": None}
            )
            keys = keys_flat.reshape(b, num_tokens, self.num_kv_groups * self.head_dim)

            values_flat = self._copy_and_run(
                self._aie_callables["value"],
                self._aie_buffers,
                {"value_in": x_flat, "value_weight": None, "value_out": None}
            )
            values = values_flat.reshape(
                b, num_tokens, self.num_kv_groups * self.head_dim
            )
        else:
            queries = self.W_query(x)
            keys = self.W_key(x)
            values = self.W_value(x)

        # Each attention head gets its own slice of the embedding dimension.
        # For each head, we have query, key and value.
        # In grouped-query attention, the keys and values are shared across groups of heads.
        # Therefore, we have self.num_heads queries, and self.num_kv_groups (== self.num_heads in case of regular attention) keys and values.
        # Each head can be applied independently to its subslice of the embedding dimension.
        keys = keys.view(b, num_tokens, self.num_kv_groups, self.head_dim)
        values = values.view(b, num_tokens, self.num_kv_groups, self.head_dim)
        queries = queries.view(b, num_tokens, self.num_heads, self.head_dim)

        # Step 2.
        # ---
        # Apply positional encoding to keys and queries.
        # The positional embedding is applied independently to each head.
        # It modifies the embedding vectors to encode where in the sequence each token is located.

        # Determine angle slice based on KV cache usage and phase
        if self.cfg["use_kv_cache"] and is_decode:
            # Decode phase with KV cache: use single position
            current_pos = input_pos.item()
            angle_slice = angles[current_pos : current_pos + 1, :]
        else:
            # Prefill phase or no KV cache: use all tokens
            angle_slice = angles[:num_tokens, :]

        # Apply RoPE with AIE
        def apply_rope_and_transpose(aie_op, tensor, num_heads_dim, angle_slice):
            angle_slice = angle_slice.to(dtype=tensor.dtype)
            if self.cfg["use_aie_rope"]:
                # Determine which RoPE operator this is based on num_heads_dim
                if num_heads_dim == self.num_kv_groups:
                    # Keys RoPE
                    op_name = "rope_prefill_k" if is_prefill else "rope_decode_k"
                else:
                    # Queries RoPE
                    op_name = "rope_prefill_q" if is_prefill else "rope_decode_q"
                
                result = self._copy_and_run(
                    self._aie_callables[op_name],
                    self._aie_buffers,
                    {
                        f"{op_name}_in": tensor.view(num_tokens * num_heads_dim, self.head_dim),
                        f"{op_name}_angles": angle_slice,
                        f"{op_name}_out": None
                    }
                )
                result = result.view(
                    b, num_tokens, num_heads_dim, self.head_dim
                ).transpose(1, 2)
            else:
                transposed = (
                    tensor.view(num_tokens, num_heads_dim, self.head_dim)
                    .transpose(0, 1)
                    .contiguous()
                )
                result = apply_rope(
                    transposed.view(1, num_heads_dim, num_tokens, self.head_dim),
                    angle_slice,
                )
            # ref = apply_rope(transposed.view(1, num_heads_dim, num_tokens, self.head_dim), angle_slice)
            # assert torch.allclose(ref, result, atol=0.7, rtol=0.07), "AIE RoPE result does not match reference"
            return result

        keys = apply_rope_and_transpose(
            (
                (self.aie_rope_prefill_k if is_prefill else self.aie_rope_decode_k)
                if self.cfg["use_aie_rope"]
                else None
            ),
            keys,
            self.num_kv_groups,
            angle_slice,
        )
        queries = apply_rope_and_transpose(
            (
                (self.aie_rope_prefill_q if is_prefill else self.aie_rope_decode_q)
                if self.cfg["use_aie_rope"]
                else None
            ),
            queries,
            self.num_heads,
            angle_slice,
        )
        values = values.transpose(1, 2)

        if self.cfg["use_kv_cache"]:
            if is_prefill:
                self.kv_cache.reset()
                self.kv_cache.update(keys, values)
                cached_keys, cached_values = keys, values
            else:
                self.kv_cache.update(keys, values)
                current_seq_len = input_pos.item() + 1
                cached_keys = self.kv_cache.k_cache[:, :, :current_seq_len, :]
                cached_values = self.kv_cache.v_cache[:, :, :current_seq_len, :]

            keys = cached_keys
            values = cached_values

        # Step 3.
        # ---
        # Since the keys and values are shared across groups of heads in grouped-query attention,
        # we now expand (repeat) the same keys and values so that each head has its own keys and values.
        keys = keys.repeat_interleave(self.group_size, dim=1)
        values = values.repeat_interleave(self.group_size, dim=1)

        # Step 4.
        # ---
        # Compute attention scores (indepdentently for each head), apply softmax to get attention weights, then apply those weights to the attention values to get output.
        # Attention scores are the dot-product of queries and keys.

        # Use fused AIE MHA if enabled and conditions are met
        if is_prefill or not self.cfg["use_kv_cache"]:
            if (
                self.cfg["use_aie_fused_mha"]
                and b == 1
                and num_tokens == self.prompt_length
                and self.head_dim == 64
            ):
                # TODO: Doesn't give good output ven with num_kv_groups set to 8 with kv_cache
                # TODO: Doesn't match the output of CPU only when used without kv_cache
                context_vec = self._copy_and_run(
                    self._aie_callables["mha"],
                    self._aie_buffers,
                    {"mha_q": queries, "mha_k": keys, "mha_v": values, "mha_out": None}
                )  # Shape: (num_heads, num_tokens, head_dim)

                # Reshape context_vec to prepare for output projection
                context_vec = context_vec.transpose(0, 1)
                context_vec = context_vec.reshape(b, num_tokens, self.d_out)

            elif self.cfg["use_aie_regular_mha"]:
                # attn_scores = queries @ keys.transpose(2, 3)
                # Compute attention scores for each head separately since AIE GEMM doesn't support batched operations
                attn_scores_list = []
                for head in range(self.num_heads):
                    q_head = queries[:, head, :, :]  # Shape: (b, num_tokens, head_dim)
                    k_head = keys[:, head, :, :]  # Shape: (b, num_tokens, head_dim)

                    # Use 2D tensors directly (remove batch dimension if b=1)
                    q_2d = q_head.squeeze(0)  # Shape: (num_tokens, head_dim)
                    k_2d = k_head.squeeze(0)  # Shape: (num_tokens, head_dim)

                    # Compute Q @ K^T for this head
                    attn_head = self._copy_and_run(
                        self._aie_callables["mha_gemm_qk"],
                        self._aie_buffers,
                        {"mha_gemm_qk_in0": q_2d, "mha_gemm_qk_in1": k_2d.T, "mha_gemm_qk_out": None}
                    )  # Shape: (num_tokens, num_tokens)
                    attn_head = attn_head.unsqueeze(0).unsqueeze(
                        0
                    )  # Add batch and head dimensions
                    attn_scores_list.append(
                        attn_head
                    )  # Shape: (1, 1, num_tokens, num_tokens)

                attn_scores = torch.cat(
                    attn_scores_list, dim=1
                )  # Shape: (b, num_heads, num_tokens, num_tokens)
                attn_scores = attn_scores.masked_fill(mask, -torch.inf)
                scaled_scores = attn_scores / (self.head_dim**0.5)

                # TODO: Make softmax more configurable to run in any scenario
                if (
                    scaled_scores.shape[-1] == self.prompt_length
                    and scaled_scores.shape[-1] % 16 == 0
                ):
                    attn_weights = self._copy_and_run(
                        self._aie_callables["softmax"],
                        self._aie_buffers,
                        {"softmax_in": scaled_scores, "softmax_out": None}
                    )
                else:
                    attn_weights = torch.nn.functional.softmax(scaled_scores, dim=-1)

                # Compute context vector for each head separately using AIE GEMM
                context_vec_list = []
                for head in range(self.num_heads):
                    attn_head = attn_weights[
                        :, head, :, :
                    ]  # Shape: (b, num_tokens, num_tokens)
                    v_head = values[:, head, :, :]  # Shape: (b, num_tokens, head_dim)

                    # Use 2D tensors directly (remove batch dimension if b=1)
                    attn_2d = attn_head.squeeze(0)  # Shape: (num_tokens, num_tokens)
                    v_2d = v_head.squeeze(0)  # Shape: (num_tokens, head_dim)

                    # Compute attn @ V for this head
                    context_head = self._copy_and_run(
                        self._aie_callables["mha_gemm_pv"],
                        self._aie_buffers,
                        {"mha_gemm_pv_in0": attn_2d, "mha_gemm_pv_in1": v_2d, "mha_gemm_pv_out": None}
                    )  # Shape: (num_tokens, head_dim)
                    context_head = context_head.unsqueeze(0).unsqueeze(
                        1
                    )  # Add batch and head dimensions
                    context_vec_list.append(
                        context_head
                    )  # Shape: (1, 1, num_tokens, head_dim)

                context_vec = torch.cat(
                    context_vec_list, dim=1
                )  # Shape: (b, num_heads, num_tokens, head_dim)
                context_vec = context_vec.transpose(
                    1, 2
                )  # Shape: (b, num_tokens, num_heads, head_dim)
                context_vec = context_vec.reshape(b, num_tokens, self.d_out)
            else:

                def my_mha(queries, keys, values):
                    inv_scale = 1 / np.sqrt(values.shape[-1])
                    context_vec = torch.nn.functional.scaled_dot_product_attention(
                        queries,
                        keys,
                        values,
                        dropout_p=0.0,
                        is_causal=True,
                        scale=inv_scale,
                    )
                    return context_vec

                context_vec = my_mha(queries, keys, values)
                context_vec = context_vec.transpose(1, 2)
                context_vec = context_vec.reshape(b, num_tokens, self.d_out)
        else:
            attn_scores = queries @ keys.transpose(2, 3)

            if mask is not None:
                attn_scores = attn_scores.masked_fill(mask, -torch.inf)

            scaled_scores = attn_scores / (self.head_dim**0.5)

            if (
                scaled_scores.shape[-1] == self.prompt_length
                and self.cfg["use_aie_softmax"]
                and scaled_scores.shape[-1] % 16 == 0
            ):
                attn_weights = self._copy_and_run(
                    self._aie_callables["softmax"],
                    self._aie_buffers,
                    {"softmax_in": scaled_scores, "softmax_out": None}
                )
            else:
                attn_weights = torch.nn.functional.softmax(scaled_scores, dim=-1)

            context_vec = (attn_weights @ values).transpose(1, 2)
            context_vec = context_vec.reshape(b, num_tokens, self.d_out)

        # Choose output projection based on phase
        if self.cfg["use_kv_cache"] and is_decode and self.cfg["use_aie_gqa_gemv"]:
            context_vec_flat = context_vec.reshape(-1)  # Shape: (d_out,) - flatten to 1D for GEMV
            output_flat = self._copy_and_run(
                self._aie_callables["out_proj_gemv"],
                self._aie_buffers,
                {"out_proj_gemv_weight": None, "out_proj_gemv_in": context_vec_flat, "out_proj_gemv_out": None}
            )
            context_vec = output_flat.reshape(b, num_tokens, self.d_out)
        elif self.cfg["use_aie_attn_projection_gemm"]:
            context_vec_flat = context_vec.reshape(-1, self.d_out)
            output_flat = self._copy_and_run(
                self._aie_callables["out_proj"],
                self._aie_buffers,
                {"out_proj_in": context_vec_flat, "out_proj_weight": None, "out_proj_out": None}
            )
            context_vec = output_flat.reshape(b, num_tokens, self.d_out)
        else:
            context_vec = self.out_proj(context_vec)

        return context_vec

    def prepare_aie_operators(self):
        """Prepare AIE operators by getting callables and allocating buffers."""
        from iron.common import AIEBuffer
        from ..aie_buffer_manager import copy_and_run
        from iron.common.utils import torch_to_numpy
        
        self._copy_and_run = copy_and_run
        self._aie_callables = {}
        self._aie_buffers = {}
        
        # Query, Key, Value GEMV operators (decode phase)
        # NOTE: GEMV arg order is [weight_matrix(MxK), input_vector(K), output_vector(M)]
        if self.cfg["use_kv_cache"] and self.cfg["use_aie_gqa_gemv"]:
            self._aie_callables["query_gemv"] = self.aie_query_gemv.get_callable()
            arg_spec = self.aie_query_gemv.get_arg_spec()
            self._aie_buffers["query_gemv_weight"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)  # Weight matrix
            self._aie_buffers["query_gemv_in"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)  # Input vector
            self._aie_buffers["query_gemv_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["key_gemv"] = self.aie_key_gemv.get_callable()
            arg_spec = self.aie_key_gemv.get_arg_spec()
            self._aie_buffers["key_gemv_weight"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)  # Weight matrix
            self._aie_buffers["key_gemv_in"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)  # Input vector
            self._aie_buffers["key_gemv_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["value_gemv"] = self.aie_value_gemv.get_callable()
            arg_spec = self.aie_value_gemv.get_arg_spec()
            self._aie_buffers["value_gemv_weight"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)  # Weight matrix
            self._aie_buffers["value_gemv_in"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)  # Input vector
            self._aie_buffers["value_gemv_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["out_proj_gemv"] = self.aie_out_proj_gemv.get_callable()
            arg_spec = self.aie_out_proj_gemv.get_arg_spec()
            self._aie_buffers["out_proj_gemv_weight"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)  # Weight matrix
            self._aie_buffers["out_proj_gemv_in"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)  # Input vector
            self._aie_buffers["out_proj_gemv_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            # Populate weight matrices (arg 0) if they were set before prepare was called
            if hasattr(self, '_pending_weights'):
                self._aie_buffers["query_gemv_weight"].data[:] = torch_to_numpy(self._pending_weights['query'])
                self._aie_buffers["key_gemv_weight"].data[:] = torch_to_numpy(self._pending_weights['key'])
                self._aie_buffers["value_gemv_weight"].data[:] = torch_to_numpy(self._pending_weights['value'])
                self._aie_buffers["out_proj_gemv_weight"].data[:] = torch_to_numpy(self._pending_weights['out_proj'])
        
        # Query, Key, Value, Out Proj GEMM operators (prefill phase)
        if self.cfg["use_aie_attn_projection_gemm"]:
            self._aie_callables["query"] = self.aie_query.get_callable()
            arg_spec = self.aie_query.get_arg_spec()
            self._aie_buffers["query_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["query_weight"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["query_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["key"] = self.aie_key.get_callable()
            arg_spec = self.aie_key.get_arg_spec()
            self._aie_buffers["key_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["key_weight"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["key_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["value"] = self.aie_value.get_callable()
            arg_spec = self.aie_value.get_arg_spec()
            self._aie_buffers["value_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["value_weight"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["value_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["out_proj"] = self.aie_out_proj.get_callable()
            arg_spec = self.aie_out_proj.get_arg_spec()
            self._aie_buffers["out_proj_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["out_proj_weight"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["out_proj_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            # Populate weights if they were set before prepare was called
            # PyTorch weights are (out_features, in_features) but GEMM expects (K, N) = (in_features, out_features)
            # So we need to transpose
            if hasattr(self, '_pending_weights'):
                self._aie_buffers["query_weight"].data[:] = torch_to_numpy(self._pending_weights['query'].T)
                self._aie_buffers["key_weight"].data[:] = torch_to_numpy(self._pending_weights['key'].T)
                self._aie_buffers["value_weight"].data[:] = torch_to_numpy(self._pending_weights['value'].T)
                self._aie_buffers["out_proj_weight"].data[:] = torch_to_numpy(self._pending_weights['out_proj'].T)
        
        # RoPE operators
        if self.cfg["use_aie_rope"]:
            self._aie_callables["rope_prefill_k"] = self.aie_rope_prefill_k.get_callable()
            arg_spec = self.aie_rope_prefill_k.get_arg_spec()
            self._aie_buffers["rope_prefill_k_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["rope_prefill_k_angles"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["rope_prefill_k_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["rope_prefill_q"] = self.aie_rope_prefill_q.get_callable()
            arg_spec = self.aie_rope_prefill_q.get_arg_spec()
            self._aie_buffers["rope_prefill_q_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["rope_prefill_q_angles"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["rope_prefill_q_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["rope_decode_k"] = self.aie_rope_decode_k.get_callable()
            arg_spec = self.aie_rope_decode_k.get_arg_spec()
            self._aie_buffers["rope_decode_k_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["rope_decode_k_angles"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["rope_decode_k_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["rope_decode_q"] = self.aie_rope_decode_q.get_callable()
            arg_spec = self.aie_rope_decode_q.get_arg_spec()
            self._aie_buffers["rope_decode_q_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["rope_decode_q_angles"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["rope_decode_q_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
        
        # Fused MHA operator
        if self.cfg["use_aie_fused_mha"]:
            self._aie_callables["mha"] = self.aie_mha.get_callable()
            arg_spec = self.aie_mha.get_arg_spec()
            self._aie_buffers["mha_q"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["mha_k"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["mha_v"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            self._aie_buffers["mha_out"] = AIEBuffer(shape=arg_spec[3].shape, dtype=arg_spec[3].dtype)
        
        # Regular MHA GEMM operators
        if self.cfg["use_aie_regular_mha"]:
            self._aie_callables["mha_gemm_qk"] = self.aie_mha_gemm_qk.get_callable()
            arg_spec = self.aie_mha_gemm_qk.get_arg_spec()
            self._aie_buffers["mha_gemm_qk_in0"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["mha_gemm_qk_in1"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["mha_gemm_qk_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["mha_gemm_pv"] = self.aie_mha_gemm_pv.get_callable()
            arg_spec = self.aie_mha_gemm_pv.get_arg_spec()
            self._aie_buffers["mha_gemm_pv_in0"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["mha_gemm_pv_in1"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["mha_gemm_pv_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["softmax"] = self.aie_softmax.get_callable()
            arg_spec = self.aie_softmax.get_arg_spec()
            self._aie_buffers["softmax_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["softmax_out"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)

    def assign_weights(self, l, w_query, w_key, w_value, w_out_proj):
        # Store weights to be populated in prepare_aie_operators
        if self.cfg["use_kv_cache"] and self.cfg["use_aie_gqa_gemv"]:
            self._pending_weights = {
                'query': w_query,
                'key': w_key,
                'value': w_value,
                'out_proj': w_out_proj
            }

        if self.cfg["use_aie_attn_projection_gemm"]:
            self._pending_weights = {
                'query': w_query,
                'key': w_key,
                'value': w_value,
                'out_proj': w_out_proj
            }

        self.W_query.weight = assign(
            self.W_query.weight,
            w_query,
            f"model.layers.{l}.self_attn.q_proj.weight",
        )
        self.W_key.weight = assign(
            self.W_key.weight,
            w_key,
            f"model.layers.{l}.self_attn.k_proj.weight",
        )
        self.W_value.weight = assign(
            self.W_value.weight,
            w_value,
            f"model.layers.{l}.self_attn.v_proj.weight",
        )
        self.out_proj.weight = assign(
            self.out_proj.weight,
            w_out_proj,
            f"model.layers.{l}.self_attn.o_proj.weight",
        )
