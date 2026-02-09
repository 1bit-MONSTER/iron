# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Buffer management and execution helper for AIE operators."""

from iron.common import AIEBuffer
from iron.common.utils import torch_to_numpy
from ml_dtypes import bfloat16
import torch
import numpy as np


def copy_and_run(callable_op, buffers, data_map, output_shape=None):
    """Copy data into buffers and execute the AIE operator callable.
    
    Args:
        callable_op: The callable obtained from operator.get_callable()
        buffers: Dict of {name: AIEBuffer} - pre-allocated buffers
        data_map: Dict mapping buffer names to data sources:
                  - For inputs: {name: torch.Tensor} - data to copy into buffer
                  - For weights: {name: None} - pre-populated weight buffer
                  - For outputs: {name: None} - buffer will receive output (must be last None)
        output_shape: Optional tuple specifying the expected output shape.
                     If not provided, attempts to infer from input shape.
                  
    Returns:
        torch.Tensor or Dict - output tensors from output buffer(s)
    """
    # Prepare arguments for the callable
    args = []
    none_names = []
    input_shape = None
    
    for name, data in data_map.items():
        if name not in buffers:
            raise KeyError(f"Buffer '{name}' not found in buffer dict")
        
        buf = buffers[name]
        
        if data is not None:
            # Input buffer - copy data in
            if isinstance(data, torch.Tensor):
                # Save input shape for potential output reshaping
                if input_shape is None:
                    input_shape = data.shape
                
                data_np = torch_to_numpy(data)
                # Ensure data shape matches buffer shape or can be reshaped
                buf_size = int(np.prod(buf.shape))
                if data_np.size != buf_size:
                    data_np = data_np.reshape(buf.shape)
                buf.from_np(data_np)
        else:
            # None means either: pre-populated weight buffer or output buffer
            # Track all None entries in order
            none_names.append(name)
        
        # Always append the buffer
        args.append(buf)
    
    # Execute the operator
    callable_op(*args)
    
    # Return output - assume last None is the output buffer
    if len(none_names) >= 1:
        output_name = none_names[-1]
        output = buffers[output_name].view_as_torch()
        
        # Reshape output if shape is provided
        if output_shape is not None:
            output = output.reshape(output_shape)
        elif input_shape is not None and len(input_shape) >= 3:
            # Try to infer output shape from input shape
            # Preserve batch (dim 0) and sequence length (dim 1)
            batch_size = input_shape[0]
            seq_len = input_shape[1]
            # Compute remaining dimensions from buffer size
            remaining_size = output.numel() // (batch_size * seq_len)
            output = output.reshape(batch_size, seq_len, remaining_size)
        
        return output
    else:
        return None


def allocate_buffers_for_operator(operator, prefix=""):
    """Allocate input and output buffers for an operator based on its arg spec.
    
    Args:
        operator: AIE operator with get_arg_spec() method
        prefix: Optional prefix for buffer names
        
    Returns:
        Dict of {name: AIEBuffer}
    """
    buffers = {}
    arg_spec = operator.get_arg_spec()
    
    for i, spec in enumerate(arg_spec):
        name = f"{prefix}{spec.direction}_{i}"
        buffers[name] = AIEBuffer(shape=spec.shape, dtype=spec.dtype)
    
    return buffers
