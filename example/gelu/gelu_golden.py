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
        description="Generate PyTorch golden reference for GeLU activation function."
    )
    parser.add_argument(
        "--dtype",
        type=str,
        choices=["bf16", "f32"],
        default="bf16",
        help="IO data type",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="golden_reference.h",
        help="Output header file path",
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    # Function-specific argument(s)
    parser.add_argument("--input_length", type=int, default=42, help="Input length")

    args = parser.parse_args()
    torch.manual_seed(args.seed)

    # Generate golden inputs
    val_range = 4
    A = torch.rand(args.input_length, dtype=torch.float32) * val_range

    # Generate golden outputs
    B = torch.nn.functional.gelu(A)

    export_to_header(
        tensor_dict={"A": torch_to_numpy(A), "B": torch_to_numpy(B)},
        dtype=args.dtype,
        header_path=args.output,
        name="GeLU",
    )


if __name__ == "__main__":
    main()
