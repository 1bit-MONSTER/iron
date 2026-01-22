import numpy as np
import ml_dtypes
import pyxrt
from . import compilation as comp
from .base import AIEOperatorBase, SingleMLIRSourceOperator, AIEBuffer
from .device_manager import AIEDeviceManager

# Fused Operator
# ##########################################################################


class FusedMLIROperator(AIEOperatorBase):
    """Operator that fuses multiple SingleMLIRSourceOperators into one."""
    
    def __init__(self, name, runlist, input_args, output_args, *args, **kwargs):
        assert all(
            isinstance(op, SingleMLIRSourceOperator) and all(isinstance(buf, str) for buf in bufs)
            for op, *bufs in runlist
        )
        self.runlist = runlist
        self.name = name
        self.input_args = input_args
        self.output_args = output_args
        self.kernel_archive = "kernels.a"
        super().__init__(*args, **kwargs)
    
    def get_operator_name(self):
        return self.name
    
    def get_kernel_artifacts(self):
        """Collect all kernel artifacts from child operators."""
        kernel_artifacts = []
        unique_ops = set(op for op, *_ in self.runlist)
        for idx, op in enumerate(unique_ops):
            objs = op.get_kernel_artifacts()
            for obj in objs:
                obj.prefix_symbols = f"op{idx}_"
            kernel_artifacts.extend(objs)
        return kernel_artifacts
    
    def get_mlir_artifact(self):
        # Build operator_mlir_map: {op_name -> PythonGeneratedMLIRArtifact}
        operator_mlir_map = {}
        mlir_dependencies = []
        comp_runlist = []
        op_names = {} # op -> op_name

        unique_operators = set(op for op, *_ in self.runlist)
        for idx, op in enumerate(unique_operators):
            mlir_artifact = op.get_mlir_artifact()
            if len(op.get_kernel_artifacts()) > 0:
                # FIXME: currently hard-coding that the design will accept this argument as an input if it uses kernels
                # Also not handling name collisions of kernels with the same name
                mlir_artifact.callback_kwargs["kernel_archive"] = self.kernel_archive
                mlir_artifact.callback_kwargs["func_prefix"] = f"op{idx}_"
            op_name = f"op{idx}_{op.__class__.__name__}"
            op_names[op] = op_name
            operator_mlir_map[op_name] = mlir_artifact
        
        for op, *bufs in self.runlist:
            comp_runlist.append((op_names[op], *bufs))
        
        # Calculate buffer layout: {buffer_name -> (type, offset, length)}
        self.subbuffer_layout, self.buffer_sizes = self._calculate_buffer_layout()
        
        filename = self.get_operator_name() + "_fused.mlir"
        fused_artifact = comp.FusedMLIRSource(
            filename,
            operator_mlir_map=operator_mlir_map,
            runlist=comp_runlist,
            subbuffer_layout=self.subbuffer_layout,
            buffer_sizes=self.buffer_sizes
        )
        
        return fused_artifact
    
    def _calculate_buffer_layout(self):
        args = {}
        
        # Collect all buffer specs from operators
        for op, *bufs in self.runlist:
            args_specs = op.get_arg_spec()
            assert len(args_specs) == len(bufs), "Number of buffers must match operator argument specification"
            for i, buf_name in enumerate(bufs):
                args_spec = args_specs[i]
                if buf_name not in args:
                    args[buf_name] = args_spec
                else:
                    assert np.prod(args[buf_name].shape) == np.prod(args_spec.shape), f"Buffer {buf_name} has conflicting sizes between operators"
        
        # Verify all input/output args are present
        for arg in self.input_args:
            assert arg in args, f"Input argument {arg} not found in runlist buffers"
        for arg in self.output_args:
            assert arg in args, f"Output argument {arg} not found in runlist buffers"
        
        # Determine buffer types
        subbuffer_layout = {}
        
        def add_buffers(buffer_type, args_list):
            offset = 0
            for arg in args_list:
                arg_spec = args[arg]
                length = int(np.prod(arg_spec.shape) * np.dtype(arg_spec.dtype).itemsize)
                subbuffer_layout[arg] = (buffer_type, offset, length)
                offset += length
            return offset # == total length
        
        input_buffer_size = add_buffers('input', self.input_args)
        output_buffer_size = add_buffers('output', self.output_args)
        scratch_args = [arg for arg in args if arg not in self.input_args and arg not in self.output_args]
        scratch_buffer_size = add_buffers('scratch', scratch_args)
        
        buffer_sizes = (input_buffer_size, output_buffer_size, scratch_buffer_size)
        return subbuffer_layout, buffer_sizes
    
    def set_up_artifacts(self):
        operator_name = self.get_operator_name()
        mlir_artifact = self.get_mlir_artifact()
        kernel_objects = self.get_kernel_artifacts()
        kernel_dep = [comp.KernelArchiveArtifact(
            self.kernel_archive,
            dependencies=kernel_objects,
        )] if kernel_objects else []
        full_elf_artifact = comp.FullElfArtifact(
            f"{operator_name}.elf",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact] + kernel_dep,
        )
        self.add_artifacts([full_elf_artifact])
    
    def get_arg_spec(self):
        pass
    
    def get_callable(self):
        """Return a callable for the fused operator (stub for now)."""
        return FusedFullELFCallable(self)


class FullELFCallable:
    def __init__(self, op, device_name="main", sequence_name="sequence", device_manager=None):
        self.device_manager = device_manager or AIEDeviceManager()
        self.xrt_elf = pyxrt.elf(op.artifacts[0].filename)
        self.xrt_module = pyxrt.module(self.xrt_elf)
        self.xrt_context = pyxrt.hw_context(self.device_manager.device, self.xrt_elf)
        self.xrt_kernel = pyxrt.ext.kernel(self.xrt_context, f"{device_name}:{sequence_name}")
    
    def __call__(self, *args):
        run = pyxrt.run(self.xrt_kernel)
        for i, arg in enumerate(args):
            assert isinstance(arg, pyxrt.bo), f"Argument {i} is not a pyxrt.bo"
            run.set_arg(i, arg)
        run.start()
        ret_code = run.wait()
        if ret_code != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
            raise RuntimeError(f"Kernel execution failed with return code {retcode}")

class FusedFullELFCallable(FullELFCallable):
    def __init__(self, op, device_manager=None):
        super().__init__(op, device_manager=device_manager)

        self.subbuffer_layout = op.subbuffer_layout
        self.buffer_sizes = op.buffer_sizes
        
        input_buffer_size, output_buffer_size, scratch_buffer_size = self.buffer_sizes
        itemsize = np.dtype(ml_dtypes.bfloat16).itemsize
        
        self.input_buffer = AIEBuffer(
            shape=(max(input_buffer_size, itemsize) // itemsize,),
            dtype=ml_dtypes.bfloat16
        ) 
        
        self.output_buffer = AIEBuffer(
            shape=(max(output_buffer_size, itemsize) // itemsize,),
            dtype=ml_dtypes.bfloat16
        ) 
        
        self.scratch_buffer = AIEBuffer(
            shape=(max(scratch_buffer_size, itemsize) // itemsize,),
            dtype=ml_dtypes.bfloat16
        ) 
        
        self._buffer_cache = {}
    
    def get_buffer(self, buffer_name):
        # Return cached buffer if already allocated
        if buffer_name in self._buffer_cache:
            return self._buffer_cache[buffer_name]
        
        # Look up buffer information
        if buffer_name not in self.subbuffer_layout:
            raise KeyError(f"Buffer '{buffer_name}' not found in buffer layout")
        
        buf_type, offset, length = self.subbuffer_layout[buffer_name]
        
        # Select the appropriate main buffer
        if buf_type == 'input':
            main_buffer = self.input_buffer
        elif buf_type == 'output':
            main_buffer = self.output_buffer
        elif buf_type == 'scratch':
            main_buffer = self.scratch_buffer
        else:
            raise ValueError(f"Unknown buffer type '{buf_type}' for buffer '{buffer_name}'")
        
        if main_buffer is None:
            raise RuntimeError(f"Main buffer for type '{buf_type}' is not allocated")
        
        # Convert byte offset/length to element offset/length
        bf16_itemsize = np.dtype(ml_dtypes.bfloat16).itemsize
        offset_elements = offset // bf16_itemsize
        length_elements = length // bf16_itemsize
        
        # Create subbuffer with appropriate shape
        # For now, use 1D shape; could be enhanced to use actual buffer shapes
        sub_buffer = main_buffer.subbuffer(
            length=length_elements,
            offset=offset_elements,
            shape=(length_elements,),
            dtype=ml_dtypes.bfloat16
        )
        
        # Cache and return
        self._buffer_cache[buffer_name] = sub_buffer
        return sub_buffer
    
    def __call__(self):
        self.input_buffer.to("npu")
        self.output_buffer.to("npu")
        self.scratch_buffer.to("npu")
        super().__call__(
            self.input_buffer.bo if self.input_buffer else None,
            self.output_buffer.bo if self.output_buffer else None,
            self.scratch_buffer.bo if self.scratch_buffer else None,
        )
