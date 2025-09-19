# Licensed under the Apache License, Version 2.0 (the License); you may
# not use this file except in compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


# SPDX-FileCopyrightText:	Copyright (c) 2025, Advanced Micro Devices, Inc. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
from pathlib import Path
import numpy as np
import argparse
import sys

from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker
from aie.iron.placers import SequentialPlacer
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_
from aie.helpers.util import np_ndarray_type_get_shape


def my_rms_norm(
    dev, num_elements, num_columns, num_channels, weight_length, trace_size
):
    per_tile_elements = weight_length
    total_cores = num_columns
    n = per_tile_elements * total_cores
    if num_elements % n != 0:
        raise ValueError(
            f"Number of elements ({num_elements}) must be a multiple of {n}."
        )
    N_div_n = num_elements // n
    chunk = num_elements // total_cores
    dtype = bfloat16
    # Define tensor types
    tensor_ty = np.ndarray[(num_elements,), np.dtype[dtype]]
    weights_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]
    tile_ty = np.ndarray[(per_tile_elements,), np.dtype[dtype]]

    # Set fifodepth based on weight_length
    fifodepth = 1 if weight_length > 4096 else 2

    # AIE-array data movement with object fifos
    of_in1s = [
        ObjectFifo(tile_ty, name=f"in1_{i}", depth=fifodepth)
        for i in range(total_cores)
    ]
    of_in2s = ObjectFifo(weights_ty, name=f"in2_weights", depth=fifodepth)
    of_outs = [
        ObjectFifo(tile_ty, name=f"out_{i}", depth=fifodepth)
        for i in range(total_cores)
    ]

    # AIE Core Function declaration
    weighted_rms_norm_kernel = Kernel(
        "weighted_rms_norm", "rms_norm.o", [tile_ty, weights_ty, tile_ty, np.int32]
    )

    # Define a task that will run on a compute tile
    def core_body(of_in1, of_in2, of_out, weighted_rms_norm):
        # Number of sub-vector "tile" iterations
        elem_in2 = of_in2.acquire(1)
        for _ in range_(N_div_n):
            elem_in1 = of_in1.acquire(1)
            elem_out = of_out.acquire(1)
            weighted_rms_norm_kernel(elem_in1, elem_in2, elem_out, per_tile_elements)
            of_in1.release(1)
            of_out.release(1)
        of_in2.release(1)

    # Create a worker to run the task on a compute tile
    my_workers = [
        Worker(
            core_body,
            [
                of_in1s[i].cons(),
                of_in2s.cons(),
                of_outs[i].prod(),
                weighted_rms_norm_kernel,
            ],
        )
        for i in range(total_cores)
    ]

    # Create a TensorAccessPattern for each core
    # to describe the data movement
    # The pattern chops the data in equal chunks
    # and moves them in parallel across the cores.
    taps = [
        TensorAccessPattern(
            (1, num_elements),
            chunk * i,
            [1, 1, 1, chunk],
            [0, 0, 0, 1],
        )
        for i in range(total_cores)
    ]

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(tensor_ty, weights_ty, tensor_ty) as (A, B, C):
        rt.start(*my_workers)
        # Fill the input objectFIFOs with data
        for i in range(total_cores):
            rt.fill(
                of_in1s[i].prod(),
                A,
                taps[i],
            )
        rt.fill(
            of_in2s.prod(),
            B,
        )
        # Drain the output objectFIFOs with data
        tg_out = rt.task_group()
        for i in range(total_cores):
            rt.drain(
                of_outs[i].cons(),
                C,
                taps[i],
                wait=True,
                task_group=tg_out,
            )
        rt.finish_task_group(tg_out)

    # Place program components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt).resolve_program(SequentialPlacer())


p = argparse.ArgumentParser()
## Parse command line arguments

## Device name is required to select the AIE device: npu or npu2
p.add_argument(
    "-d",
    "--dev",
    required=True,
    dest="device",
    help="AIE Device",
    choices=["npu", "npu2"],
)
## Transfer size is required to define the size of the data to be transferred
## It must be a multiple of 1024 and divisible by the number of columns and 2 channels per column
p.add_argument("-l", "--length", required=True, dest="length", help="Transfer size")
## Number of columns is required to define the number of columns to be used
## It must be less than or equal to 4 for npu and 8 for npu2
p.add_argument("-co", "--columns", required=True, dest="cols", help="Number of columns")
## Number of channels is required to define the number of channels to be used
## It must be 1 or 2
p.add_argument(
    "-ch", "--channels", required=True, dest="chans", help="Number of channels"
)
## Weight length
p.add_argument(
    "-wl",
    "--weight-length",
    required=True,
    dest="weight_length",
    help="Weight vector length",
)
## Trace Size
p.add_argument(
    "-ts", "--trace-size", required=True, dest="trace_size", help="Trace size"
)
p.add_argument(
    "--output-file-path",
    "-o",
    type=str,
    help="Output file path for the generated MLIR module",
)

opts = p.parse_args(sys.argv[1:])

if opts.device == "npu":
    dev = NPU1()  # Four columns of NPU1, the maximum available
elif opts.device == "npu2":
    dev = NPU2()  # Eight columns of NPU2, the maximum available
else:
    raise ValueError("[ERROR] Device name {} is unknown".format(opts.device))

length = int(opts.length)
columns = int(opts.cols)
if opts.device == "npu":
    if columns > 4:
        raise ValueError(
            "[ERROR] Device {} cannot allocate more than 4 columns".format(opts.device)
        )
elif opts.device == "npu2":
    if columns > 8:
        raise ValueError(
            "[ERROR] Device {} cannot allocate more than 8 columns".format(opts.device)
        )
channels = int(opts.chans)
if channels < 1 or channels > 2:
    raise ValueError("Number of channels must be 1 or 2")
weight_length = int(opts.weight_length)
# For weighted RMS norm: cores = columns (weights are broadcasted)
total_cores = columns
if (length % (weight_length * total_cores)) != 0:
    print(
        "transfer size ("
        + str(length)
        + ") must be a multiple of weight_length * total_cores ("
        + str(weight_length * total_cores)
        + ")"
    )
    raise ValueError
trace_size = int(opts.trace_size) if opts.trace_size is not None else 0

module = my_rms_norm(dev, length, columns, channels, weight_length, trace_size)

output_file_path = Path(opts.output_file_path)


with open(output_file_path, "w") as f:
    f.write(str(module))
