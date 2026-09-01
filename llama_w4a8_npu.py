#!/usr/bin/env python3
"""Full-model W4A8 llama prefill on XDNA2 (part 30 follow-up).

NPU does the 7 heavy GEMMs per layer (attn q/k/v/o + ffn gate/up/down) as
asymmetric i8xi4 with INT4-packed weights (per-output-neuron scales) and
INT8 activations (per-tensor scale). Host does everything else (embedding,
rmsnorm, RoPE, attention scores/softmax/value, SiLU, residual, lm_head) in
bf16 — the small matmuls (scores: K=64, value: K=seq) don't justify NPU
dispatch overhead.

Validates against the bf16 CPU reference (llama_cpu.llama_forward_pass):
logits correlation, top-k, and greedy text.

Usage (iron-venv python):
  cd ~/amd-oss/iron
  PYTHONPATH=/usr/lib/python3/dist-packages \
    ~/amd-oss/iron-venv/bin/python llama_w4a8_npu.py "The capital of France is"
"""
import os
import sys
import math
import time

sys.path.insert(0, "/home/bcloud/amd-oss/iron")
sys.path.insert(0, "/home/bcloud/amd-oss/iron/iron/applications/llama_3.2_1b")

import numpy as np
import torch
import safetensors.torch as st

from iron.common.context import AIEContext
from iron.operators import GEMM
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

import llama_cpu
import llama_inference_harness as harness

WT = "/home/bcloud/llama3.2-1b/model.safetensors"
M_PAD = 256  # i8xi4 GEMM constraint: M % (tile_m*4) == 0
M_PAD_SEQ = 256  # padded sequence length (attention GEMM-free, host side)

CONFIG = dict(
    emb_dim=2048, hidden_dim=8192, n_heads=32, n_kv_groups=8,
    head_dim=64, n_layers=16, vocab_size=128256,
)


class NPU_W4A8_GEMM:
    """Compiled i8xi4 GEMM for one (K, N) shape. Each weight gets its own
    buffer set via bind(); the compiled op is shared (compile once per shape,
    buffers are per-weight — the B-binding overwrite bug made every op in a
    shape group use the last-bound weights)."""

    def __init__(self, K, N, build_dir="/tmp/w4a8-prefill"):
        self.K, self.N = K, N
        assert N % 2 == 0 and N % 512 == 0 and K % 16 == 0
        ctx = AIEContext(build_dir=build_dir)
        self.op = (
            GEMM(M=M_PAD, K=K, N=N, tile_m=64, tile_k=64, tile_n=64,
                 num_aie_columns=8, dtype_in="i8", dtype_out="i32",
                 dtype_b="i4", context=ctx)
            .compile()
            .get_callable()
        )

    def bind(self, B_ref, s_w):
        """Return a callable bound to this weight's own buffers."""
        return _Bound(self, B_ref, s_w)


class _Bound:
    def __init__(self, gemm, B_ref, s_w):
        self.gemm = gemm
        q4 = np.rint(B_ref / s_w).clip(-8, 7).astype(np.int8)
        self.B = XRTTensor((gemm.K, gemm.N // 2), dtype=np.int8)
        self.B.numpy()[:] = GEMM.pack_i4(q4)
        self.A = XRTTensor((M_PAD, gemm.K), dtype=np.int8)
        self.C = XRTTensor((M_PAD, gemm.N), dtype=np.int32)
        self.s_w = s_w.astype(np.float64)
        self._warmed = False

    def __call__(self, x, real_m):
        xf = x.float().numpy().reshape(M_PAD, -1)  # drop batch dim if present
        # Per-token (per-row) activation scale: each input row quantized with
        # its own s_x (Q8_0-style). Naive per-tensor scales lose too much over
        # 16 layers (corr ~0.55-0.75); per-row holds up much better.
        sx = np.max(np.abs(xf[:real_m]), axis=1, keepdims=True) / 127.0
        q8 = np.zeros_like(xf, dtype=np.int8)
        q8[:real_m] = np.rint(xf[:real_m] / sx).clip(-127, 127).astype(np.int8)
        self.A.numpy()[:] = q8
        res = self.gemm.op(self.A, self.B, self.C)
        _ = res.npu_time  # force the dispatch to complete before reading C
        c = self.C.to_torch().numpy().astype(np.float64)
        sx_full = np.zeros((M_PAD, 1), dtype=np.float64)
        sx_full[:real_m, 0] = sx[:, 0]
        out = c * sx_full * self.s_w[None, :]
        if not self._warmed:
            # XRT first-dispatch flake (iron 5582ca1): the first call after
            # other kernels on the same device can return a stale C readback.
            # Re-run once (same buffers) and keep the second result.
            self._warmed = True
            return self(x, real_m)
        return torch.from_numpy(out.astype(np.float32)).to(torch.bfloat16)


def quantize_weight(W):
    """W: torch [out, in] bf16 -> (B_ref [in, out] f32, s_w [out] f32)."""
    B_ref = W.float().t().numpy()
    s_w = np.max(np.abs(B_ref), axis=0) / 8.0
    s_w = np.maximum(s_w, 1e-8).astype(np.float32)
    return B_ref, s_w


def build_npu_layers(weights, build_dir):
    """Return per-layer dict of NPU W4A8 GEMMs (cache by K,N)."""
    pool = {}

    def get(K, N):
        key = (K, N)
        if key not in pool:
            pool[key] = NPU_W4A8_GEMM(K, N, build_dir)
        return pool[key]

    layers = []
    for i in range(CONFIG["n_layers"]):
        L = {}
        for name, (Wkey, K, N) in {
            "q": (f"model.layers.{i}.self_attn.q_proj.weight", CONFIG["emb_dim"], CONFIG["emb_dim"]),
            "k": (f"model.layers.{i}.self_attn.k_proj.weight", CONFIG["emb_dim"], CONFIG["n_kv_groups"] * CONFIG["head_dim"]),
            "v": (f"model.layers.{i}.self_attn.v_proj.weight", CONFIG["emb_dim"], CONFIG["n_kv_groups"] * CONFIG["head_dim"]),
            "o": (f"model.layers.{i}.self_attn.o_proj.weight", CONFIG["emb_dim"], CONFIG["emb_dim"]),
            "gate": (f"model.layers.{i}.mlp.gate_proj.weight", CONFIG["emb_dim"], CONFIG["hidden_dim"]),
            "up": (f"model.layers.{i}.mlp.up_proj.weight", CONFIG["emb_dim"], CONFIG["hidden_dim"]),
            "down": (f"model.layers.{i}.mlp.down_proj.weight", CONFIG["hidden_dim"], CONFIG["emb_dim"]),
        }.items():
            B_ref, s_w = quantize_weight(weights[Wkey])
            L[name] = get(K, N).bind(B_ref, s_w)  # per-weight buffers
        layers.append(L)
    print(f"[w4a8] built {len(pool)} compiled NPU GEMM shapes ({len(layers)} layers)", flush=True)
    return layers


def forward_w4a8_npu(layers, weights, token_ids, rope_angles, build_dir):
    """token_ids: [1, seq] int64. Returns logits bf16 [1, seq, vocab] (padded seq)."""
    seq = token_ids.shape[1]
    assert seq <= M_PAD
    batch = 1
    emb = weights["model.embed_tokens.weight"]
    x = torch.nn.functional.embedding(token_ids, emb)  # [1, seq, emb]
    x = torch.nn.functional.pad(x, (0, 0, 0, M_PAD - seq))  # [1, M_PAD, emb]

    mask = torch.triu(torch.ones(M_PAD, M_PAD, dtype=torch.bool), diagonal=1)
    if seq < M_PAD:
        mask[:, seq:] = True
        mask[seq:, :] = True

    for i in range(CONFIG["n_layers"]):
        L = layers[i]
        x_norm = llama_cpu.rms_norm_forward(
            x, weights[f"model.layers.{i}.input_layernorm.weight"])
        # projections on NPU (W4A8)
        q = L["q"](x_norm, seq).view(batch, M_PAD, CONFIG["n_heads"], CONFIG["head_dim"])
        k = L["k"](x_norm, seq).view(batch, M_PAD, CONFIG["n_kv_groups"], CONFIG["head_dim"])
        v = L["v"](x_norm, seq).view(batch, M_PAD, CONFIG["n_kv_groups"], CONFIG["head_dim"])
        q = llama_cpu.rope_forward(q, rope_angles[:M_PAD])
        k = llama_cpu.rope_forward(k, rope_angles[:M_PAD])
        q = q.transpose(1, 2)  # [b, H, M, hd]
        k = k.transpose(1, 2)  # [b, G, M, hd]
        v = v.transpose(1, 2)
        gsz = CONFIG["n_heads"] // CONFIG["n_kv_groups"]
        k = k.repeat_interleave(gsz, dim=1)
        v = v.repeat_interleave(gsz, dim=1)
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(CONFIG["head_dim"])
        scores = scores.masked_fill(mask, float("-inf"))
        scores[:, :, seq:, :] = 0.0  # padded query rows: finite (uniform), zeroed below
        aw = torch.nn.functional.softmax(scores, dim=-1)
        aw[:, :, seq:, :] = 0.0  # padded query rows attend to nothing
        ctx_out = torch.matmul(aw, v).transpose(1, 2).contiguous().view(
            batch, M_PAD, -1)
        attn_out = L["o"](ctx_out, seq)  # NPU
        x = x + attn_out
        x_norm = llama_cpu.rms_norm_forward(
            x, weights[f"model.layers.{i}.post_attention_layernorm.weight"])
        gate = L["gate"](x_norm, seq)  # NPU
        up = L["up"](x_norm, seq)  # NPU
        hidden = torch.nn.functional.silu(gate) * up
        ffn_out = L["down"](hidden, seq)  # NPU
        x = x + ffn_out
        if i in (0, 1, 5):
            print(f"[w4a8] layer {i}: x[0,{seq-1},:4] = "
                  f"{x[0, seq-1, :4].float().tolist()}", flush=True)

    x = llama_cpu.rms_norm_forward(x, weights["model.norm.weight"])
    logits = torch.nn.functional.linear(x, emb)  # host, tied lm_head
    return logits


def main():
    prompt = sys.argv[1] if len(sys.argv) > 1 else "The capital of France is"
    build_dir = sys.argv[2] if len(sys.argv) > 2 else "/tmp/w4a8-prefill"

    weights = st.load_file(WT)
    for k, v in weights.items():
        weights[k] = v.to(torch.bfloat16)

    tok_path = "/home/bcloud/llama3.2-1b/original/tokenizer.model"
    config, state = harness.init(WT, tok_path, prompt=prompt)
    token_ids = state.token_ids  # torch [1, seq]
    seq = token_ids.shape[1]
    rope_angles = harness.compute_rope_angles(
        CONFIG["head_dim"], M_PAD + 16, rope_base=500000.0)

    # bf16 CPU reference
    t0 = time.time()
    ref_logits, _ = llama_cpu.llama_forward_pass(config, state)
    t_ref = time.time() - t0

    # W4A8 NPU
    layers = build_npu_layers(weights, build_dir)
    t0 = time.time()
    logits = forward_w4a8_npu(layers, weights, token_ids, rope_angles, build_dir)
    t_npu = time.time() - t0

    # compare at the last REAL token
    ref_last = ref_logits[0, seq - 1].float()
    npu_last = logits[0, seq - 1].float()
    corr = float(torch.corrcoef(torch.stack([ref_last, npu_last]))[0, 1])
    diff = (npu_last - ref_last).abs()
    print(f"\nprompt: '{prompt}' ({seq} tokens, padded {M_PAD})")
    print(f"bf16 ref : {t_ref:.2f}s cpu | W4A8 NPU: {t_npu:.2f}s (GEMM-heavy path)")
    print(f"logits corr : {corr:.6f}")
    print(f"max |dlogit| : {diff.max():.4f}")
    print(f"top1 : ref {ref_last.argmax().item():>6}  npu {npu_last.argmax().item():>6}  "
          f"{'OK' if ref_last.argmax()==npu_last.argmax() else 'MISMATCH'}")
    rk, nk = torch.topk(ref_last, 5).indices.tolist(), torch.topk(npu_last, 5).indices.tolist()
    print(f"top5 ref: {rk}")
    print(f"top5 npu: {nk}")
    print(f"overlap  : {len(set(rk) & set(nk))}/5")

    # greedy continuation (host-side, W4A8 logits)
    print("\ngreedy (npu logits):")
    gen = token_ids.clone()
    ids = []
    for _ in range(8):
        lg = forward_w4a8_npu(layers, weights, gen, rope_angles, build_dir)
        nxt = lg[0, gen.shape[1] - 1].argmax().item()
        ids.append(nxt)
        gen = torch.cat([gen, torch.tensor([[nxt]])], dim=1)
        if nxt == 2:
            break
    print(f"W4A8 greedy token ids: {ids} (2=EOS)")


if __name__ == "__main__":
    main()
