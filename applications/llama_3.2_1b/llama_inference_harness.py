#!/usr/bin/env python3
"""
Inference harness -- all the necessary code _other_ than the actual model (forward pass).
Exposes a 'harness' function that can be called with a 'forward_pass' function that implements the model.
The 'harness' function does the following:
1. Load and set up model weights, tokenizer, and RoPE angle look-up table.
2. Tokenize the provided input prompt.
3. Run the generation loop to produce new tokens; this calls the provided forward_pass function. Decode and print each generated token.
"""

import torch
import math
import sys
import time

import safetensors.torch
import tiktoken, tiktoken.load


# Configuration
# ##########################################################################

class LlamaConfig:
    """Fixed model configuration for Llama 3.2 1B"""

    # Model architecture
    vocab_size = 128256
    emb_dim = 2048
    n_layers = 16
    n_heads = 32
    n_kv_groups = 8
    head_dim = emb_dim // n_heads  # 64
    hidden_dim = 8192
    
    # RoPE
    rope_base = 500000.0
    context_length = 131072
    
    # Generation
    temperature = 0.7
    top_k = 50

    # Tokenization 
    special_tokens = {
        "<|begin_of_text|>": 128000,
        "<|end_of_text|>": 128001,
        "<|start_header_id|>": 128006,
        "<|end_header_id|>": 128007,
        "<|eot_id|>": 128009,
    }
    special_tokens.update({
        f"<|reserved_{i}|>": i
        for i in list(range(128002, 128006)) + list(range(128009, 128256))
    })


# Utilities
# ##########################################################################

def compute_rope_angles(head_dim, context_length, rope_base=500000.0):
    """Compute RoPE (Rotary Position Embedding) angles."""
    # Precompute the frequency tensor
    inv_freq = 1.0 / (rope_base ** (torch.arange(0, head_dim, 2).float() / head_dim))
    position = torch.arange(context_length).float()
    freqs = torch.outer(position, inv_freq)
    
    cos = torch.cos(freqs)
    sin = torch.sin(freqs)
    
    # Interleave cos and sin - create angles buffer
    angles = torch.empty(context_length, head_dim)
    angles[:, ::2] = cos
    angles[:, 1::2] = sin
    return angles


def get_tokenizer(tokenizer_path, config):
    mergeable = tiktoken.load.load_tiktoken_bpe(tokenizer_path)
    return tiktoken.Encoding(
        name="llama3.2-1b",
        pat_str=r"(?i:'s|'t|'re|'ve|'m|'ll|'d)"
        r"|[^\r\n\p{L}\p{N}]?\p{L}+"
        r"|\p{N}{1,3}"
        r"| ?[^\s\p{L}\p{N}]+[\r\n]*"
        r"|\s*[\r\n]+"
        r"|\s+(?!\S)"
        r"|\s+",
        mergeable_ranks=mergeable,
        special_tokens=config.special_tokens,
    )


# Generation loop
# ##########################################################################

def generate_token(
    config,
    weights,
    angles,
    forward_pass,
    token_ids,
    attn_keys_caches=None,
    attn_values_caches=None,
):
    generated_tokens = []
    
    # Step 1: Forward pass
    logits, attn_keys_caches, attn_values_caches = forward_pass(
        config,
        weights,
        angles,
        token_ids,
        attn_keys_caches,
        attn_values_caches
    )
    
    # Step 2: Get logits for last token
    last_token_logits = logits[:, -1, :]  # (batch, vocab_size)
    
    # Step 3: Temperature scaling
    if config.temperature > 0:
        last_token_logits = last_token_logits / config.temperature
    
    # Step 4: Top-k filtering
    if config.top_k is not None:
        top_logits, top_indices = torch.topk(last_token_logits, config.top_k)
        min_val = top_logits[:, -1:]
        last_token_logits = torch.where(
            last_token_logits < min_val,
            torch.tensor(float('-inf')),
            last_token_logits
        )
    
    # Step 5: Sample
    probs = torch.nn.functional.softmax(last_token_logits, dim=-1)
    next_token = torch.multinomial(probs, num_samples=1)

    return next_token.item(), attn_keys_caches, attn_values_caches


def harness(
    forward_pass,
    weights_path="/scratch/roesti/models/llama3.2-1b/model.safetensors",
    tokenizer_path="/scratch/roesti/models/llama3.2-1b/tokenizer.model",
    prompt="The capital of France is ",
    num_tokens=100
):

    seed = 1608560892
    torch.manual_seed(seed)

    config = LlamaConfig()
    
    # Load model weights and tokenizer
    weights = safetensors.torch.load_file(weights_path)
    tokenizer = get_tokenizer(tokenizer_path, config)

    # Compute RoPE angle look-up table
    angles = compute_rope_angles(
        config.head_dim,
        config.context_length,
        config.rope_base
    )
    
    # Tokenize prompt
    prompt_token_ids = [config.special_tokens["<|begin_of_text|>"]]
    prompt_token_ids += tokenizer.encode(prompt)
    assert len(prompt_token_ids) + num_tokens <= config.context_length, "Prompt + new tokens to generate too long (exceed context)"
    prompt_token_ids = torch.tensor([prompt_token_ids], dtype=torch.long)

    # Set up KV cache -- initially empty
    # This is what passes information from previous tokens to the current token during generation
    attn_keys_caches = [torch.empty(1, config.n_kv_groups, 0, config.head_dim, dtype=weights["model.layers.0.self_attn.k_proj.weight"].dtype) for _ in range(config.n_layers)] # (batch_size, n_kv_groups, seq_len, head_dim)
    attn_values_caches = [torch.empty(1, config.n_kv_groups, 0, config.head_dim, dtype=weights["model.layers.0.self_attn.v_proj.weight"].dtype) for _ in range(config.n_layers)] # (batch_size, n_kv_groups, seq_len, head_dim)

    # Generate tokens
    # First token (prefill)
    n_tokens_generated = 0
    t_prefill_start = time.perf_counter()
    first_token, attn_keys_caches, attn_values_caches = generate_token(config, weights, angles, forward_pass, prompt_token_ids, attn_keys_caches, attn_values_caches)
    token_text = tokenizer.decode([first_token])
    n_tokens_generated  += 1
    print(prompt, end='', flush=True)
    print(token_text, end='', flush=True)
    t_prefill_stop = time.perf_counter()

    # Remaining tokens (decode)
    last_token = torch.tensor([[first_token]])
    t_decode_start = time.perf_counter()
    for _ in range(num_tokens-1):
        next_token, attn_keys_caches, attn_values_caches = generate_token(config, weights, angles, forward_pass, last_token, attn_keys_caches, attn_values_caches)
        token_text = tokenizer.decode([next_token])
        n_tokens_generated += 1
        print(token_text, end='', flush=True)
        last_token = torch.tensor([[next_token]])
    t_decode_end = time.perf_counter()

    t_prefill = t_prefill_stop - t_prefill_start
    t_decode = t_decode_end - t_decode_start
    sys.stderr.write("\n\n=== Performance Statistics ===\n")
    sys.stderr.write(f"[Prefill] Time to first token:   {t_prefill:7.3f} s\n")
    sys.stderr.write(f"[Decode]  Time per token (mean): {t_decode / (n_tokens_generated - 1):7.3f} s\n")
    sys.stderr.write(f"[Decode]  Tokens per second:     {(n_tokens_generated - 1) / t_decode:7.3f}\n")
    sys.stderr.write(f"[Total]   Time per token (mean): {(t_prefill + t_decode) / n_tokens_generated:7.3f} s\n")
    sys.stderr.write(f"[Total]   Tokens per second:     {n_tokens_generated / (t_prefill + t_decode):7.3f}\n")


if __name__ == "__main__":
    main()

