# Copyright (c) Sebastian Raschka under Apache License 2.0.
# Source for "Build a Large Language Model From Scratch"
#   - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Code: https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/standalone-llama32.ipynb
#
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn as nn
from ..utils import assign
from iron.operators import (
    AIEElementwiseMul,
    AIEGEMM,
    AIEGEMV,
    AIESiLU,
    AIESwiGLUPrefill,
    AIESwiGLUDecode,
)
from ml_dtypes import bfloat16


class FeedForward(nn.Module):
    def __init__(
        self,
        cfg,
        prompt_length=0,
        num_tokens=1,
    ):
        super().__init__()
        self.cfg = cfg.copy()

        assert (
            cfg["use_aie_ffn_swiglu"]
            and not (
                cfg["use_aie_ffn_silu"]
                or cfg["use_aie_ffn_gemm"]
                or cfg["use_aie_ffn_mul"]
            )
            or not cfg["use_aie_ffn_swiglu"]
        ), "Cannot mix fused SwiGLU with individual AIE operators."

        self.emb_dim = cfg["emb_dim"]
        self.hidden_dim = cfg["hidden_dim"]

        # Initialize SiLU activation
        if self.cfg["use_aie_ffn_silu"]:
            if self.cfg["use_kv_cache"]:
                max_prefill_size = prompt_length * self.hidden_dim
            else:
                max_prefill_size = (prompt_length + num_tokens) * self.hidden_dim
            self.aie_silu_prefill = AIESiLU(
                size=max_prefill_size,
                num_aie_columns=8,
                num_channels=2,
                tile_size=self.hidden_dim,
            )
            # For decode phase - single token (only when using KV cache)
            if self.cfg["use_kv_cache"]:
                decode_size = self.hidden_dim  # 1 token * emb_dim
                self.aie_silu_decode = AIESiLU(
                    size=decode_size,
                    num_aie_columns=1,
                    num_channels=1,
                    tile_size=self.hidden_dim,
                )
            else:
                # When not using KV cache, use same operator for both phases
                self.aie_silu_decode = self.silu_prefill
        else:
            self.silu = nn.SiLU()

        if self.cfg["use_aie_ffn_swiglu"]:
            self.aie_swiglu_prefill = AIESwiGLUPrefill(
                seq_len=prompt_length,
                embedding_dim=self.emb_dim,
                hidden_dim=self.hidden_dim,
            )
            if self.cfg["use_kv_cache"]:
                self.aie_swiglu_decode = AIESwiGLUDecode(
                    embedding_dim=self.emb_dim, hidden_dim=self.hidden_dim
                )

        if self.cfg["use_aie_ffn_gemm"]:
            if self.cfg["use_kv_cache"]:
                M_prefill = prompt_length
            else:
                M_prefill = prompt_length + num_tokens

            aie_config_prefill = {
                "num_aie_columns": 8,
                "tile_m": 64,
                "tile_k": 64,
                "tile_n": 64,
                "use_static_weight": True,
            }

            # Compute required padding for GEMM dimensions (matching GEMM operator's requirements)
            num_aie_rows = 4
            tile_m = aie_config_prefill["tile_m"]
            tile_k = aie_config_prefill["tile_k"]
            tile_n = aie_config_prefill["tile_n"]
            num_cols = aie_config_prefill["num_aie_columns"]
            
            # Pad to multiples using same formula as GEMM.pad_A/pad_B
            min_M = tile_m * num_aie_rows
            min_K = tile_k
            min_N = tile_n * num_cols
            M_padded = ((M_prefill + min_M - 1) // min_M) * min_M
            emb_dim_padded = ((self.emb_dim + min_K - 1) // min_K) * min_K
            hidden_dim_padded = ((self.hidden_dim + min_N - 1) // min_N) * min_N

            self.fc1 = AIEGEMM(
                M=M_padded, K=emb_dim_padded, N=hidden_dim_padded, **aie_config_prefill
            )
            self.fc2 = AIEGEMM(
                M=M_padded, K=emb_dim_padded, N=hidden_dim_padded, **aie_config_prefill
            )
            self.fc3 = AIEGEMM(
                M=M_padded, K=hidden_dim_padded, N=emb_dim_padded, **aie_config_prefill
            )
        else:
            self.fc1 = nn.Linear(
                cfg["emb_dim"], cfg["hidden_dim"], dtype=cfg["dtype"], bias=False
            )
            self.fc2 = nn.Linear(
                cfg["emb_dim"], cfg["hidden_dim"], dtype=cfg["dtype"], bias=False
            )
            self.fc3 = nn.Linear(
                cfg["hidden_dim"], cfg["emb_dim"], dtype=cfg["dtype"], bias=False
            )

        if self.cfg["use_kv_cache"] and self.cfg["use_aie_ffn_gemv"]:
            aie_gemv_config = {"num_aie_columns": 8}
            # FC1 and FC2: emb_dim -> hidden_dim
            self.aie_fc1_gemv = AIEGEMV(
                M=self.hidden_dim,
                K=self.emb_dim,
                tile_size_input=1,
                tile_size_output=self.hidden_dim // 16,
                **aie_gemv_config,
            )
            self.aie_fc2_gemv = AIEGEMV(
                M=self.hidden_dim,
                K=self.emb_dim,
                tile_size_input=1,
                tile_size_output=self.hidden_dim // 16,
                **aie_gemv_config,
            )
            # FC3: hidden_dim -> emb_dim
            self.aie_fc3_gemv = AIEGEMV(
                M=self.emb_dim,
                K=self.hidden_dim,
                tile_size_input=1,
                tile_size_output=self.emb_dim // 16,
                **aie_gemv_config,
            )

        # Initialize AIE elementwise multiply
        if self.cfg["use_aie_ffn_mul"]:
            if self.cfg["use_kv_cache"]:
                max_prefill_size = prompt_length * self.hidden_dim
            else:
                max_prefill_size = (prompt_length + num_tokens) * self.hidden_dim

            self.aie_mul_prefill = AIEElementwiseMul(
                size=max_prefill_size,
                num_aie_columns=8,
                num_channels=2,
                tile_size=self.hidden_dim,
            )

            # For decode phase - single token (only when using KV cache)
            if self.cfg["use_kv_cache"]:
                decode_size = self.hidden_dim  # 1 token * emb_dim
                self.aie_mul_decode = AIEElementwiseMul(
                    size=decode_size,
                    num_aie_columns=1,
                    num_channels=2,
                    tile_size=self.hidden_dim,
                )
            else:
                # When not using KV cache, use same operator for both phases
                self.aie_mul_decode = self.aie_mul_prefill

    def forward(self, x):
        original_shape = x.shape

        # Check if input is a vector (decode phase) or matrix (prefill phase)
        # Handle 1D: (emb_dim,), 2D: (1, emb_dim), or 3D: (1, 1, emb_dim)
        is_vector = (
            len(x.shape) == 1
            or (len(x.shape) == 2 and x.shape[0] == 1)
            or (len(x.shape) == 3 and x.shape[0] == 1 and x.shape[1] == 1)
        )

        is_prefill = not is_vector or not self.cfg["use_kv_cache"]
        is_decode_with_kv = is_vector and self.cfg["use_kv_cache"]

        if self.cfg["use_aie_ffn_swiglu"]:
            if is_prefill:
                return self._copy_and_run(
                    self._aie_callables["swiglu_prefill"],
                    self._aie_buffers,
                    {"swiglu_prefill_in": x, "swiglu_prefill_out": None}
                )
            else:
                return self._copy_and_run(
                    self._aie_callables["swiglu_decode"],
                    self._aie_buffers,
                    {"swiglu_decode_in": x, "swiglu_decode_out": None}
                )

        if is_decode_with_kv and self.cfg["use_aie_ffn_gemv"]:
            # Flatten to 1D for GEMV
            # GEMV arg order: [weight_matrix, input_vector, output_vector]
            x_flat = x.reshape(-1)
            x_fc1 = self._copy_and_run(
                self._aie_callables["fc1_gemv"],
                self._aie_buffers,
                {"fc1_gemv_weight": None, "fc1_gemv_in": x_flat, "fc1_gemv_out": None}
            )
            x_fc2 = self._copy_and_run(
                self._aie_callables["fc2_gemv"],
                self._aie_buffers,
                {"fc2_gemv_weight": None, "fc2_gemv_in": x_flat, "fc2_gemv_out": None}
            )
        else:
            x_fc1 = self.fc1(x)
            x_fc2 = self.fc2(x)

        if self.cfg["use_aie_ffn_silu"]:
            if is_decode_with_kv:
                x_fc1_silu = self._copy_and_run(
                    self._aie_callables["silu_decode"],
                    self._aie_buffers,
                    {"silu_decode_in": x_fc1, "silu_decode_out": None}
                )
            else:
                x_fc1_silu = self._copy_and_run(
                    self._aie_callables["silu_prefill"],
                    self._aie_buffers,
                    {"silu_prefill_in": x_fc1, "silu_prefill_out": None}
                )
        else:
            x_fc1_silu = self.silu(x_fc1)

        if self.cfg["use_aie_ffn_mul"]:
            if is_decode_with_kv:
                x = self._copy_and_run(
                    self._aie_callables["mul_decode"],
                    self._aie_buffers,
                    {"mul_decode_in0": x_fc1_silu, "mul_decode_in1": x_fc2, "mul_decode_out": None}
                )
            else:
                x = self._copy_and_run(
                    self._aie_callables["mul_prefill"],
                    self._aie_buffers,
                    {"mul_prefill_in0": x_fc1_silu, "mul_prefill_in1": x_fc2, "mul_prefill_out": None}
                )
        else:
            x = x_fc1_silu * x_fc2

        if is_decode_with_kv and self.cfg["use_aie_ffn_gemv"]:
            x_flat = x.reshape(-1)
            result = self._copy_and_run(
                self._aie_callables["fc3_gemv"],
                self._aie_buffers,
                {"fc3_gemv_weight": None, "fc3_gemv_in": x_flat, "fc3_gemv_out": None}
            )
            return result.view(original_shape)
        else:
            return self.fc3(x).view(original_shape)

    def prepare_aie_operators(self):
        """Prepare AIE operators by getting callables and allocating buffers."""
        from iron.common import AIEBuffer
        from ..aie_buffer_manager import copy_and_run
        from iron.common.utils import torch_to_numpy
        
        self._copy_and_run = copy_and_run
        self._aie_callables = {}
        self._aie_buffers = {}
        
        # SwiGLU operators
        if self.cfg["use_aie_ffn_swiglu"]:
            self._aie_callables["swiglu_prefill"] = self.aie_swiglu_prefill.get_callable()
            arg_spec = self.aie_swiglu_prefill.get_arg_spec()
            self._aie_buffers["swiglu_prefill_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["swiglu_prefill_out"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            
            if self.cfg["use_kv_cache"]:
                self._aie_callables["swiglu_decode"] = self.aie_swiglu_decode.get_callable()
                arg_spec = self.aie_swiglu_decode.get_arg_spec()
                self._aie_buffers["swiglu_decode_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
                self._aie_buffers["swiglu_decode_out"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
        
        # GEMV operators (decode phase)
        if self.cfg["use_kv_cache"] and self.cfg["use_aie_ffn_gemv"]:
            self._aie_callables["fc1_gemv"] = self.aie_fc1_gemv.get_callable()
            arg_spec = self.aie_fc1_gemv.get_arg_spec()
            # GEMV arg order: [weight_matrix(MxK), input_vector(K), output_vector(M)]
            self._aie_buffers["fc1_gemv_weight"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["fc1_gemv_in"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["fc1_gemv_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["fc2_gemv"] = self.aie_fc2_gemv.get_callable()
            arg_spec = self.aie_fc2_gemv.get_arg_spec()
            self._aie_buffers["fc2_gemv_weight"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["fc2_gemv_in"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["fc2_gemv_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            self._aie_callables["fc3_gemv"] = self.aie_fc3_gemv.get_callable()
            arg_spec = self.aie_fc3_gemv.get_arg_spec()
            self._aie_buffers["fc3_gemv_weight"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["fc3_gemv_in"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["fc3_gemv_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            # Populate weights if they were set before prepare was called
            if hasattr(self, '_pending_weights'):
                self._aie_buffers["fc1_gemv_weight"].data[:] = torch_to_numpy(self._pending_weights['fc1'])
                self._aie_buffers["fc2_gemv_weight"].data[:] = torch_to_numpy(self._pending_weights['fc2'])
                self._aie_buffers["fc3_gemv_weight"].data[:] = torch_to_numpy(self._pending_weights['fc3'])
        
        # SiLU operators
        if self.cfg["use_aie_ffn_silu"]:
            self._aie_callables["silu_prefill"] = self.aie_silu_prefill.get_callable()
            arg_spec = self.aie_silu_prefill.get_arg_spec()
            self._aie_buffers["silu_prefill_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["silu_prefill_out"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            
            if self.cfg["use_kv_cache"]:
                self._aie_callables["silu_decode"] = self.aie_silu_decode.get_callable()
                arg_spec = self.aie_silu_decode.get_arg_spec()
                self._aie_buffers["silu_decode_in"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
                self._aie_buffers["silu_decode_out"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
        
        # Elementwise multiply operators
        if self.cfg["use_aie_ffn_mul"]:
            self._aie_callables["mul_prefill"] = self.aie_mul_prefill.get_callable()
            arg_spec = self.aie_mul_prefill.get_arg_spec()
            self._aie_buffers["mul_prefill_in0"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
            self._aie_buffers["mul_prefill_in1"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
            self._aie_buffers["mul_prefill_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)
            
            if self.cfg["use_kv_cache"]:
                self._aie_callables["mul_decode"] = self.aie_mul_decode.get_callable()
                arg_spec = self.aie_mul_decode.get_arg_spec()
                self._aie_buffers["mul_decode_in0"] = AIEBuffer(shape=arg_spec[0].shape, dtype=arg_spec[0].dtype)
                self._aie_buffers["mul_decode_in1"] = AIEBuffer(shape=arg_spec[1].shape, dtype=arg_spec[1].dtype)
                self._aie_buffers["mul_decode_out"] = AIEBuffer(shape=arg_spec[2].shape, dtype=arg_spec[2].dtype)

    def assign_weights(self, l, fc1, fc2, fc3):
        if self.cfg["use_kv_cache"] and self.cfg["use_aie_ffn_gemv"]:
            # Store weights to be populated in prepare_aie_operators
            self._pending_weights = {
                'fc1': fc1,
                'fc2': fc2,
                'fc3': fc3
            }

        if self.cfg["use_aie_ffn_swiglu"]:
            self.aie_swiglu_prefill.weights_1 = fc1
            self.aie_swiglu_prefill.weights_2 = fc2
            self.aie_swiglu_prefill.weights_3 = fc3
            if self.cfg["use_kv_cache"]:
                self.aie_swiglu_decode.weights_1 = fc1
                self.aie_swiglu_decode.weights_2 = fc2
                self.aie_swiglu_decode.weights_3 = fc3
            return

        self.fc1.weight = assign(
            self.fc1.weight,
            fc1,
            f"model.layers.{l}.mlp.gate_proj.weight",
        )
        self.fc2.weight = assign(
            self.fc2.weight,
            fc2,
            f"model.layers.{l}.mlp.up_proj.weight",
        )
        self.fc3.weight = assign(
            self.fc3.weight,
            fc3,
            f"model.layers.{l}.mlp.down_proj.weight",
        )
