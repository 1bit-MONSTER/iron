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
    
    # Sampling
    dtype = torch.float32

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
):
    generated_tokens = []
    
    # Step 1: Forward pass
    logits = forward_pass(
        token_ids,
        weights,
        angles,
        config,
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

    return next_token.item()


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
    token_ids = [config.special_tokens["<|begin_of_text|>"]]
    token_ids += tokenizer.encode(prompt)
    assert len(token_ids) + num_tokens <= config.context_length, "Prompt + new tokens to generate too long (exceed context)"
    token_ids = torch.tensor([token_ids], dtype=torch.long)
    
    # Generate tokens
    print(prompt, end='', flush=True)
    for _ in range(num_tokens):
        next_token = generate_token(config, weights, angles, forward_pass, token_ids)
        token_ids = torch.cat([token_ids, torch.tensor([[next_token]])], dim=1)

        token_text = tokenizer.decode([next_token])
        print(token_text, end='', flush=True)


if __name__ == "__main__":
    main()

