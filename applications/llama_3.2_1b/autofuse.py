#!/usr/bin/env python3

import torch
import math
from pathlib import Path
import sys
import numpy as np
import ml_dtypes
import logging
import time
import importlib
from aie import ir
from aie.dialects import aie, aiex, memref
from aie.extras.context import mlir_mod_ctx
import logging
logging.basicConfig(level=logging.DEBUG)

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))

from operators.common.aie_context import AIEContext
from operators.common import AIEOperatorBase, AIEBuffer, SingleMLIRSourceOperator
from operators.common.utils import torch_to_numpy, numpy_to_torch
from operators.common.compilation import SourceArtifact, PythonGeneratedMLIRArtifact
from operators import AIEGEMV
from operators.elementwise_mul.op import AIEElementwiseMul
from operators.silu.op import AIESiLU


emb_dim = 2048
hidden_dim = 8192

# Operator definitions
# ---

gemv_ffn_up_gate_op = AIEGEMV(
    M=hidden_dim,
    K=emb_dim,
    num_aie_columns=1,
    tile_size_input=4,
    tile_size_output=hidden_dim // 8,
)

gemv_ffn_down_op = AIEGEMV(
    M=emb_dim,
    K=hidden_dim,
    num_aie_columns=1,
    tile_size_input=1,
    tile_size_output=emb_dim // 8,
)

silu_ffn_op = AIESiLU(
    size=hidden_dim,
    tile_size=hidden_dim // 8,
    num_aie_columns=1,
)

eltwise_mul_ffn_op = AIEElementwiseMul(
    size=hidden_dim,
    tile_size=hidden_dim // 8,
    num_aie_columns=1,
)


# Buffers
# ---

buf_W_ffn_gate = AIEBuffer.from_torch(torch.randn(hidden_dim, emb_dim, dtype=torch.bfloat16))
buf_W_ffn_up = AIEBuffer.from_torch(torch.randn(hidden_dim, emb_dim, dtype=torch.bfloat16))
buf_W_ffn_down = AIEBuffer.from_torch(torch.randn(emb_dim, hidden_dim, dtype=torch.bfloat16))
buf_x_norm = AIEBuffer.from_torch(torch.randn(emb_dim, dtype=torch.bfloat16))
buf_ffn_gate = AIEBuffer.from_torch(torch.zeros(hidden_dim, dtype=torch.bfloat16))
buf_ffn_up = AIEBuffer.from_torch(torch.zeros(hidden_dim, dtype=torch.bfloat16))
buf_ffn_hidden = AIEBuffer.from_torch(torch.zeros(hidden_dim, dtype=torch.bfloat16))
buf_ffn_output = AIEBuffer.from_torch(torch.zeros(emb_dim, dtype=torch.bfloat16))


# Separate xclbins
# ---

gemv_ffn_up_gate = gemv_ffn_up_gate_op.compile().get_callable()
gemv_ffn_down = gemv_ffn_down_op.compile().get_callable()
silu_ffn = silu_ffn_op.compile().get_callable()
eltwise_mul_ffn = eltwise_mul_ffn_op.compile().get_callable()

def run_separate_xclbins():
    gemv_ffn_up_gate(buf_W_ffn_gate, buf_x_norm, buf_ffn_gate)  # Gate projection
    gemv_ffn_up_gate(buf_W_ffn_up, buf_x_norm, buf_ffn_up)  # Up projection
    silu_ffn(buf_ffn_gate, buf_ffn_gate)  # SiLU activation
    eltwise_mul_ffn(buf_ffn_gate, buf_ffn_up, buf_ffn_hidden)  # Gate application (eltwise mul)
    gemv_ffn_down(buf_W_ffn_down, buf_ffn_hidden, buf_ffn_output)  # Down projection
    return buf_ffn_output.to("cpu").view_as_torch()


# Autofused
# ---

class FusedMLIROperator(SingleMLIRSourceOperator):
    def __init__(self, name, runlist, input_args, output_args, *args, **kwargs):
        assert all(
            isinstance(op, SingleMLIRSourceOperator) and all(isinstance(buf, str) for buf in bufs) 
            for op, *bufs in runlist
        )
        # Runlist is a list of operators and names for their buffer arguments.
        # Shapes for the named buffer arguments are derived from the operator's argument specification.
        # To pass data between operators, use the same buffer name in multiple operators.
        # If the same buffer name is used in multiple operators, the required buffer shapes must match for each operator.
        self.runlist = runlist
        self.name = name
        self.input_args = input_args
        self.output_args = output_args
        self.args = {}
        self.input_buffer_size = 0
        self.output_buffer_size = 0
        self.scratch_buffer_size = 0
        self.buffer_map = {}  # Maps buffer name -> {'type': 'input'|'output'|'scratch', 'offset': int, 'size': int}
        self.populate_args()
        AIEOperatorBase.__init__(self, *args, **kwargs)
    
    def populate_args(self):
        for op, *bufs in self.runlist:
            args_specs = op.get_arg_spec()
            assert len(args_specs) == len(bufs), "Number of buffers must match operator argument specification"
            for i, buf_name in enumerate(bufs):
                args_spec = args_specs[i]
                if buf_name not in self.args:
                    self.args[buf_name] = args_spec
                else:
                    assert np.prod(self.args[buf_name].shape) == np.prod(args_spec.shape), f"Buffer {buf_name} has conflicting sizes between operators"
        for arg in self.input_args:
            assert arg in self.args, f"Input argument {arg} not found in runlist buffers"
        for arg in self.output_args:
            assert arg in self.args, f"Output argument {arg} not found in runlist buffers"
        
        # Calculate buffer sizes for input, output, and scratch buffers
        # Scratch buffers are those that are neither input nor output
        scratch_args = [arg for arg in self.args if arg not in self.input_args and arg not in self.output_args]

        # Build the buffer map with offsets and sizes for each buffer type
        self.input_buffer_size = self._calculate_buffer_size('input', self.input_args)
        self.output_buffer_size = self._calculate_buffer_size('output', self.output_args)
        self.scratch_buffer_size = self._calculate_buffer_size('scratch', scratch_args)
    
    def _calculate_buffer_size(self, buffer_type, args_list):
        """Calculate total buffer size and populate buffer_map for a given buffer type."""
        offset = 0
        for arg in args_list:
            arg_spec = self.args[arg]
            size_bytes = int(np.prod(arg_spec.shape) * np.dtype(arg_spec.dtype).itemsize)
            self.buffer_map[arg] = {
                'type': buffer_type,
                'offset': offset,
                'size': size_bytes
            }
            offset += size_bytes
        return offset
    
    def get_operator_name(self):
        return self.name
    
    def get_kernel_artifacts(self):
        kernel_artifacts = []
        for op, *bufs in self.runlist:
            kernel_artifacts.extend(op.get_kernel_artifacts())
        return kernel_artifacts
    
    @staticmethod
    def get_child_mlir_module(artifact):
        assert isinstance(artifact, PythonGeneratedMLIRArtifact)
        # Import the Python source file
        spec = importlib.util.spec_from_file_location(
            Path(artifact.import_path).name, artifact.import_path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # We only initiate an MLIR context if requested; otherwise, it is expected that the callback creates the context
        if artifact.requires_context:
            raise NotImplementedError("Not handled, make your operator return a ctx.module")
        callback_function = getattr(module, artifact.callback_fn)
        mlir_module = callback_function(
            *artifact.callback_args, **artifact.callback_kwargs
        )
        return mlir_module
    
    def get_mlir_artifact(self):
        device_mlir_strings = {}  # op -> device str
        device_ty = None
        # FIXME: The proper way for this would be to create a new type of artifact (FusedMLIRArtifact) and a new compilation rule that does what this function steps _only if_ the fused MLIR file doesn't exist yet.
        # As it stands, we're regenerating it on each run.
        for runlist_op, *bufs in self.runlist:
            if runlist_op in device_mlir_strings:
                continue
            artifact = runlist_op.get_mlir_artifact()
            mlir_module = self.get_child_mlir_module(artifact)
            for op in mlir_module.body.operations:
                if not isinstance(op, aie.DeviceOp):
                    continue
                if device_ty is None:
                    device_ty = op.device
                # else:
                #     assert device_ty == op.device, "All operators in a fused operator must target the same type of AIE"
                device_mlir_strings[runlist_op] = str(op)
        
        device_names = {}  # op -> str
        sequence_arg_types = {}  # op -> list of expected arg types
        with mlir_mod_ctx() as ctx:
            for i, (runlist_op, device_str) in enumerate(device_mlir_strings.items()):
                dev_op = aie.DeviceOp.parse(device_str)
                device_names[runlist_op] = f"dev{i}"
                dev_op.sym_name = ir.StringAttr.get(device_names[runlist_op])
                
                # Extract the runtime sequence argument types
                # Look for aie.runtime_sequence operations
                found_sequence = False
                for nested_op in dev_op.body_region.blocks[0].operations:
                    op_name = nested_op.operation.name
                    if op_name == 'aie.runtime_sequence':
                        # Found the runtime sequence - need to extract argument types
                        # The runtime_sequence contains a region with the actual function
                        if hasattr(nested_op, 'body') and hasattr(nested_op.body, 'blocks'):
                            # Look for the entry block which has the arguments
                            if len(nested_op.body.blocks) > 0:
                                entry_block = nested_op.body.blocks[0]
                                # Extract argument types from the block arguments
                                arg_types = [entry_block.arguments[i].type for i in range(len(entry_block.arguments))]
                                sequence_arg_types[runlist_op] = arg_types
                                found_sequence = True
                                break
                
                if not found_sequence:
                    raise RuntimeError(f"Could not find runtime sequence or extract argument types for operator {runlist_op}")
                
                ctx.module.body.append(dev_op)
            @aie.device(device_ty)
            def main():
                # Argument 0 is the input buffer, argument 1 is the output buffer, argument 2 is scratch space for intermediate values.
                # All buffers are bf16, so convert byte sizes to element counts
                bf16_itemsize = 2
                @aiex.runtime_sequence(
                    np.ndarray[(self.input_buffer_size // bf16_itemsize,), np.dtype[ml_dtypes.bfloat16]],
                    np.ndarray[(self.output_buffer_size // bf16_itemsize,), np.dtype[ml_dtypes.bfloat16]],
                    np.ndarray[(self.scratch_buffer_size // bf16_itemsize,), np.dtype[ml_dtypes.bfloat16]],
                )
                def sequence(input_buf, output_buf, scratch_buf):
                    # Map buffer type to the appropriate consolidated buffer argument
                    consolidated_buffers = {
                        'input': input_buf,
                        'output': output_buf,
                        'scratch': scratch_buf
                    }
                    
                    for runlist_op, *bufs in self.runlist:
                        configure_sym_ref_attr = ir.FlatSymbolRefAttr.get(device_names[runlist_op])
                        configure_op = aiex.ConfigureOp(configure_sym_ref_attr)
                        configure_body = configure_op.body.blocks.append()
                        with ir.InsertionPoint(configure_body):
                            # Get the expected argument types for this operator's sequence
                            expected_arg_types = sequence_arg_types.get(runlist_op, [])
                            
                            # Generate subviews and reinterpret_casts for each buffer argument
                            buffer_ssa_values = []
                            bf16_itemsize = 2
                            expected_arg_types = sequence_arg_types.get(runlist_op, None)
                            
                            if expected_arg_types is None:
                                raise RuntimeError(f"No runtime sequence argument types found for operator {runlist_op}")
                            
                            for idx, buf_name in enumerate(bufs):
                                buf_info = self.buffer_map[buf_name]
                                buf_spec = self.args[buf_name]
                                
                                # Get the consolidated buffer this belongs to (already bf16)
                                consolidated_buf = consolidated_buffers[buf_info['type']]
                                
                                # Convert byte offsets/sizes to bf16 element offsets/sizes
                                offset_elements = buf_info['offset'] // bf16_itemsize
                                size_elements = buf_info['size'] // bf16_itemsize
                                
                                # Create subview from the bf16 buffer
                                subview = memref.subview(
                                    consolidated_buf,
                                    [offset_elements],
                                    [size_elements],
                                    [1]
                                )
                                
                                # Get target shape from the expected argument type
                                if idx >= len(expected_arg_types):
                                    raise RuntimeError(f"No expected type for argument {idx} (buffer {buf_name}) of operator {runlist_op}")
                                
                                target_type = expected_arg_types[idx]
                                expected_memref = ir.MemRefType(target_type)
                                target_shape = [expected_memref.shape[i] for i in range(expected_memref.rank)]
                                
                                # Verify the size matches
                                expected_size = np.prod(target_shape)
                                if expected_size != size_elements:
                                    raise ValueError(f"Size mismatch for buffer {buf_name}: expected {expected_size} elements, got {size_elements}")
                                
                                # Build strides (assuming row-major layout)
                                strides = []
                                stride = 1
                                for dim in reversed(target_shape):
                                    strides.insert(0, stride)
                                    stride *= dim
                                
                                # Build the result memref type with target shape (bf16)
                                result_type = ir.MemRefType.get(target_shape, ir.BF16Type.get())
                                
                                # Reinterpret_cast to reset offset to 0 and reshape
                                reinterpreted = memref.reinterpret_cast(
                                    result=result_type,
                                    source=subview,
                                    offsets=[],
                                    sizes=[],
                                    strides=[],
                                    static_offsets=[0],
                                    static_sizes=target_shape,
                                    static_strides=strides
                                )
                                
                                buffer_ssa_values.append(reinterpreted)
                            
                            # Run the sequence with the prepared buffers
                            sequence_sym_ref_attr = ir.FlatSymbolRefAttr.get("sequence")
                            run_op = aiex.RunOp(sequence_sym_ref_attr, buffer_ssa_values)
            
            filename = self.get_operator_name() + "_fused.mlir"
            with open(filename, "w") as f:
                f.write(str(ctx.module))
        src_artifact = SourceArtifact.new(Path(filename))
        src_artifact.fake_available = True
        return src_artifact


    def get_arg_spec(self):
        pass

class FusedFullELFCallable:
    def __init__(self, op):
        self.op = op
    
    def __call__(self, *kwargs):
        assert all(kw in self.op.args for kw in kwargs), "at least one unknown argument passed"
        assert all(kw in kwargs for kw in self.op.input_args), "not all input arguments passed"
        assert all(kw in kwargs for kw in self.op.output_args), "not all output arguments passed"


swiglu_fused_op = FusedMLIROperator(
    "swiglu",
    [
        (gemv_ffn_up_gate_op, "W_ffn_gate", "x_norm", "inter_ffn_gate"),
        (gemv_ffn_up_gate_op, "W_ffn_up", "x_norm", "inter_ffn_up"),
        (silu_ffn_op, "inter_ffn_gate", "inter_ffn_gate"),
        (eltwise_mul_ffn_op, "inter_ffn_gate", "inter_ffn_up", "inter_ffn_hidden"),
        (gemv_ffn_down_op, "W_ffn_down", "inter_ffn_hidden", "ffn_output"),
    ],
    input_args=[
        "x_norm",
        "W_ffn_gate",
        "W_ffn_up",
        "W_ffn_down"
    ],
    output_args=[
        "ffn_output"
    ]
)
swiglu_fused = swiglu_fused_op.compile().get_callable()

def run_autofused():
    swiglu_fused()

# CPU
# ---

def run_cpu():
    x_norm = buf_x_norm.view_as_torch()
    W_ffn_gate = buf_W_ffn_gate.view_as_torch()
    W_ffn_up = buf_W_ffn_up.view_as_torch()
    W_ffn_down = buf_W_ffn_down.view_as_torch()

    ffn_gate = torch.matmul(W_ffn_gate, x_norm)
    ffn_up = torch.matmul(W_ffn_up, x_norm)
    ffn_gate = torch.nn.functional.silu(ffn_gate)
    ffn_hidden = ffn_gate * ffn_up
    ffn_output = torch.matmul(W_ffn_down, ffn_hidden)

    return ffn_output


# Main
# ---

print(run_autofused())
print(run_separate_xclbins())
print(run_cpu())
