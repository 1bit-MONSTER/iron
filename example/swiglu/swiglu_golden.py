# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import sys
import argparse

import torch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)

from golden_model_lib import export_to_header, torch_to_numpy


def main():
    parser = argparse.ArgumentParser(
        description="Generate PyTorch golden reference for SwiGLU"
    )
    parser.add_argument(
        "--output", required=True, type=str, help="Output header file path"
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--dim", type=int, default=256, help="Embedding dimension")

    args = parser.parse_args()
    torch.manual_seed(args.seed)

    # Generate golden inputs, N: out features, K: in features, M: sequence length
    val_range = 4
    inp = torch.randn(args.dim, dtype=torch.bfloat16) * val_range
    W1 = torch.randn(args.dim, args.dim, dtype=torch.bfloat16) * val_range
    bias1 = torch.randn(args.dim, dtype=torch.bfloat16) * val_range
    W2 = torch.randn(args.dim, args.dim, dtype=torch.bfloat16) * val_range
    bias2 = torch.randn(args.dim, dtype=torch.bfloat16) * val_range

    # Generate golden outputs
    left = W1 @ inp  # + bias1
    left_swished = torch.nn.functional.silu(left)
    right = W2 @ inp  # + bias2
    result = left_swished * right

    export_to_header(
        tensor_dict={
            name: torch_to_numpy(vars()[name].float())
            for name in [
                "inp",
                "W1",
                "bias1",
                "W2",
                "bias2",
                "left",
                "left_swished",
                "right",
                "result",
            ]
        },
        dtype="bf16",
        header_path=args.output,
        name="SwiGLU",
    )


if __name__ == "__main__":
    main()
