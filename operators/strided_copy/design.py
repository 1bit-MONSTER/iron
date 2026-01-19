# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
#from aie.extras.context import mlir_mod_ctx
#from aie.ir import StridedLayoutAttr, ShapedType
#from aie.dialects.aie import *
#from aie.dialects.aiex import *
from aie.dialects.aiex import TensorAccessPattern
from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer


"""
Strided copy design

This can be useful for data layout manipulation and data copying such as:
input[0, :, 0] -> output[:, 0, 0]
"""
def strided_copy(dev, dtype, input_buffer_size, input_sizes, input_strides, input_offset, output_buffer_size, output_sizes, output_strides, output_offset, transfer_size=None, num_aie_channels=1):
    assert input_sizes[0] % num_aie_channels == 0, "Highest dimension of input_sizes must be divisible by num_aie_channels"
    assert output_sizes[0] % num_aie_channels == 0, "Highest dimension of output_sizes must be divisible by num_aie_channels"

    if transfer_size is None:
        transfer_size = int(np.prod(input_sizes))
    assert np.prod(input_sizes) % transfer_size == 0
    transfer_ty = np.ndarray[(transfer_size,), np.dtype[dtype],]
    
    inp_ty = np.ndarray[(int(input_buffer_size),), np.dtype[dtype],]
    out_ty = np.ndarray[(int(output_buffer_size),), np.dtype[dtype],]

    input_taps = [
        TensorAccessPattern(
            tensor_dims=(int(input_buffer_size),),
            offset=input_offset + c * (input_sizes[0] // num_aie_channels) * input_strides[0],
            sizes=[input_sizes[0] // num_aie_channels, *input_sizes[1:]],
            strides=list(input_strides),
        ) 
        for c in range(num_aie_channels)
    ]

    output_taps = [
        TensorAccessPattern(
            tensor_dims=(int(output_buffer_size),),
            offset=output_offset + c * (output_sizes[0] // num_aie_channels) * output_strides[0],
            sizes=[output_sizes[0] // num_aie_channels, *output_sizes[1:]],
            strides=list(output_strides),
        )
        for c in range(num_aie_channels)
    ]

    # Use smaller FIFOs for the transfer amount
    fifos_in = [ObjectFifo(transfer_ty, name=f"fifo_in_{c}", depth=2) for c in range(num_aie_channels)]
    fifos_out = [fifos_in[c].cons().forward(name=f"fifo_out_{c}", depth=2) for c in range(num_aie_channels)]

    rt = Runtime()
    with rt.sequence(inp_ty, out_ty) as (inp, out):
        tg = rt.task_group()
        for c in range(num_aie_channels):
            rt.fill(fifos_in[c].prod(), inp, input_taps[c], task_group=tg)
            rt.drain(fifos_out[c].cons(), out, output_taps[c], task_group=tg, wait=True)
        rt.finish_task_group(tg)

    return Program(dev, rt).resolve_program(SequentialPlacer())
