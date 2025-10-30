# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

### A library to generated C headers with golden values from PyTorch tensors
### Author: Victor Jung
###

import os
from typing import Dict

import torch
import numpy as np
from ml_dtypes import bfloat16
import struct

torch_dtype_map = {
    "bf16": torch.bfloat16,
    "f32": torch.float32,
    "i8": torch.int8,
    "ui8": torch.uint8,
    "i16": torch.int16,
    "i32": torch.int32,
}

# For the binary golden reference value file format, these are the C struct
# definitions we need to match: (packed + little endian)
"""
constexpr uint16_t golden_reference_magic = 0x507D;

struct __attribute__((packed)) GoldenReferenceBufferHeader {
    char name[48];
    uint16_t dtype;
    uint64_t len;  // length of the following data in bytes
};

struct __attribute__((packed)) GoldenReferenceHeader {
    uint16_t magic;
    uint64_t len; // total file length, including this header
    uint16_t nReferences;
};
"""


dtype_enum = {np.dtype(bfloat16): 1, np.dtype("float32"): 2, np.dtype("uint8"): 3}


def export(
    tensor_dict: Dict[str, np.ndarray],
    header_path: str | None = None,
    bin_path: str | None = None,
):
    """Export matrices to binary golden reference file."""
    if header_path:
        export_to_header(tensor_dict, header_path)
    if bin_path:
        export_to_file(tensor_dict, bin_path)


def export_to_file(tensor_dict: Dict[str, np.ndarray], path: str):
    """Export matrices to binary golden reference file."""

    # Create the necessary folders for the path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        tensors_to_file(f, tensor_dict)


def tensors_to_file(f, tensors: Dict[str, np.ndarray]) -> bytes:
    header_fmt = "<HQH"
    total_len = struct.calcsize(header_fmt) + sum(
        encoded_tensor_size(tensor) for tensor in tensors.values()
    )
    header = struct.pack(header_fmt, 0x507D, total_len, len(tensors))
    f.write(header)
    for tensor_name, tensor in tensors.items():
        f.write(tensor_to_bytes(tensor, tensor_name))


tensor_header_fmt = "<48sHQ"


def encoded_tensor_size(array: np.ndarray) -> int:
    data_len = array.dtype.itemsize * array.size
    total_len = struct.calcsize(tensor_header_fmt) + data_len
    return total_len


def tensor_to_bytes(array: np.ndarray, name: str) -> bytes:
    assert len(name) < 48
    data_bytes = array.tobytes()
    header = struct.pack(
        tensor_header_fmt,
        name.encode("ascii"),
        dtype_enum[array.dtype],
        len(data_bytes),
    )
    return header + data_bytes


# Map data types to C++ types
CPP_DTYPE_MAP = {
    np.dtype(bfloat16): "std::bfloat16_t",
    np.dtype("float32"): "float",
    np.dtype("int8"): "int8_t",
    np.dtype("uint8"): "uint8_t",
    np.dtype("int16"): "int16_t",
    np.dtype("int32"): "int32_t",
}

HEADER_STR = """// Generated golden reference values

#ifndef GOLDEN_REFERENCE_H
#define GOLDEN_REFERENCE_H

#include <array>
#include <cstdint>
#include <stdfloat>

namespace golden_reference {{

"""

CLOSING_STR = """} // namespace golden_reference\n#endif // GOLDEN_REFERENCE_H\n"""


def tensor_to_header(array: np.ndarray, cpp_dtype: str, name: str) -> str:

    ret = "\n"
    ret += f"// Array {name} {array.shape} of type {cpp_dtype}\n"
    ret += f"constexpr std::array<{cpp_dtype}, {np.prod(array.shape)}> {name} = {{\n"

    array_flat = (
        array.flatten().astype(np.float32)
        if cpp_dtype == "std::bfloat16_t"
        else array.flatten()
    )

    for i, val in enumerate(array_flat):
        if cpp_dtype == "std::bfloat16_t":
            ret += f"    {cpp_dtype}({float(val):.6f}f)"
        elif cpp_dtype == "float":
            ret += f"    {float(val):.6f}f"
        else:
            ret += f"    {int(val)}"

        if i < len(array_flat) - 1:
            ret += ","
        if (i + 1) % 8 == 0:
            ret += "\n"

    ret += "\n};"
    return ret


def export_to_header(tensor_dict: Dict[str, np.ndarray], header_path: str):
    """Export matrices to C++ header file."""

    header_dir = os.path.dirname(header_path)

    if header_dir and not os.path.exists(header_dir):
        os.makedirs(header_dir, exist_ok=True)

    with open(header_path, "w") as f:
        f.write(HEADER_STR.format())

        for name, tensor in tensor_dict.items():
            cpp_dtype = CPP_DTYPE_MAP[tensor.dtype]
            f.write(tensor_to_header(tensor, cpp_dtype, name))
            f.write("\n\n")

        f.write(CLOSING_STR)


def torch_to_numpy(tensor: torch.Tensor) -> np.ndarray:
    if tensor.dtype == torch.bfloat16:
        float_arr = tensor.float().detach().cpu().numpy()
        return float_arr.astype(bfloat16)
    return tensor.detach().cpu().numpy()
