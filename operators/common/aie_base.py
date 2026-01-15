# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import os
from pathlib import Path
from abc import ABC, abstractmethod
import logging
import time
import torch
from ml_dtypes import bfloat16

import aie.utils.config
from . import compilation as comp
from .aie_context import AIEContext
from .aie_device_manager import AIEDeviceManager, pyxrt
from .utils import numpy_to_torch, torch_to_numpy
from .compilation import (
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEOperatorBase(ABC):
    """Base class for AIE-accelerated operations"""

    def __init__(self, context=None):
        self.artifacts = (
            []
        )  # CompilationArtifact objects are uniqued within the context
        if context is None:
            context = self.get_default_context()
        context.register_operator(self)
        self.context = context

    @abstractmethod
    def set_up_artifacts(self):
        """
        Subclasses should overwrite this method to set up their required dependenices and runtime runlist, kernels and buffers with calls to add_artifacts(), add_kernel(), add_buffer(), and add_to_runlist().
        Note: This method should only *describe* the required artifacts and runtime buffers, and not yet do any computation or compilation.
        Compilation will be handled automatically based on the provided description.
        """
        pass
    
    @abstractmethod
    def get_arg_spec(self):
        pass

    @abstractmethod
    def get_callable(self):
        pass

    @classmethod
    def get_default_context(cls):
        """One global 'default' context if none is specified"""
        if not hasattr(AIEOperatorBase, "_default_context"):
            AIEOperatorBase._default_context = AIEContext()
        return AIEOperatorBase._default_context

    def compile(self, dry_run=None):
        """
        Set up the operator and compile any necessary artifacts.
        Subclasses are expected to overwrite set_up(); they may register any artifacts that they need to be compiled there.
        """
        context = self.context
        self.set_up_artifacts()
        self._move_artifact_paths()
        work_list = comp.get_work_list(self.artifacts)
        compilation_rules = [
            comp.GenerateMLIRFromPythonCompilationRule(dry_run=dry_run),
            comp.PeanoCompilationRule(
                context.peano_dir, context.mlir_aie_dir, dry_run=dry_run
            ),
            comp.ArchiveCompilationRule(context.peano_dir, dry_run=dry_run),
            comp.AieccCompilationRule(
                context.build_dir,
                context.peano_dir,
                context.mlir_aie_dir,
                dry_run=dry_run,
            ),
        ]
        if work_list:
            logging.info(
                f"Compiling {len(work_list)} new artifacts for AIE operator {self.__class__.__name__}: {', '.join(str(artifact.path.name) for artifact in work_list)}"
            )
        comp.compile(compilation_rules, work_list)
        return self

    def add_artifacts(self, artifacts):
        self.artifacts.extend(artifacts)

    def _move_artifact_paths(self):
        """Make all artifacts paths point into the build directory (source artifacts into the ironclad source directory). This doesn't phyisically move files; this function is called before artifact generation."""
        context = self.context
        todo = self.artifacts.copy()
        while todo:
            artifact = todo[0]
            todo.pop(0)
            if isinstance(artifact, comp.SourceArtifact):
                artifact.set_path(context.base_dir / artifact.path)
            else:
                artifact.set_path(context.build_dir / artifact.path)
            todo.extend(artifact.depends)


def sync_to_device(bos):
    for bo in bos:
        bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)


def sync_from_device(bos):
    for bo in bos:
        bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)


def execute_runlist(runlist):
    runlist.execute()
    runlist.wait()


class SingleMLIRSourceOperator(AIEOperatorBase, ABC):
    """Base class for AIE-accelerated operations"""
    def __init__(self, *args, **kwargs):
        AIEOperatorBase.__init__(self, *args, **kwargs)

    @abstractmethod
    def get_operator_name(self):
        pass
    
    @abstractmethod
    def get_mlir_artifact(self):
        pass
    
    @abstractmethod
    def get_kernel_artifacts(self):
        pass
    
    def get_kernel_archive_name(self):
        return self.get_operator_name() + ".a"
    
    def get_artifacts(self):
        operator_name = self.get_operator_name()
        mlir_artifact = self.get_mlir_artifact()
        kernel_deps = self.get_kernel_artifacts()
        xclbin_artifact = XclbinArtifact.new(
            f"{operator_name}.xclbin",
            depends=[
                mlir_artifact,
                KernelArchiveArtifact.new(
                    self.get_kernel_archive_name(),
                    depends=kernel_deps,
                ),
            ],
        )
        insts_artifact = InstsBinArtifact.new(
            f"{operator_name}.bin", depends=[mlir_artifact]
        )
        return xclbin_artifact, insts_artifact
    
    def set_up_artifacts(self):
        xclbin_artifact, insts_artifact = self.get_artifacts()
        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])
    
    
    def get_callable(self):
        return SingleXclbinCallable(
            xclbin_path=self.xclbin_artifact.path,
            kernel_name=self.xclbin_artifact.kernel_name,
            insts_bin_path=self.insts_artifact.path,
            args_spec=self.get_arg_spec()
        )
    
class AIERuntimeArgSpec:
    def __init__(self, shape, dtype=bfloat16):
        self.shape = shape
        self.dtype = dtype

class AIEBuffer:
    def __init__(self, shape, dtype=bfloat16, bo=None, device_manager=None):
        size = np.prod(shape) * np.dtype(dtype).itemsize
        self.shape = shape
        self.dtype = dtype
        self.bo = bo
        self.on = "cpu"
        self.device_manager = device_manager or AIEDeviceManager()
        if not self.bo:
            self.bo = pyxrt.bo(
                self.device_manager.device,
                size,
                pyxrt.bo.host_only,
                0x10000,
            )
    
    def subbuffer(self, length, offset, shape, dtype=None):
        if dtype is None:
            dtype = self.dtype
        assert np.prod(shape) == length
        itemsize = np.dtype(dtype).itemsize
        assert offset >= 0 
        assert offset * itemsize <= np.prod(self.shape) * np.dtype(self.dtype).itemsize
        assert length * itemsize + offset * itemsize <= np.prod(self.shape) * np.dtype(self.dtype).itemsize
        sub_bo = pyxrt.bo(
            self.bo, # parent bo 
            length * itemsize, # size
            offset * itemsize, # offset
        )
        return AIEBuffer(shape=shape, dtype=dtype, bo=sub_bo, device_manager=self.device_manager)

    def view_as_np(self):
        self.to("cpu")
        # Create a byte accessible memory view of the buffer object
        mv = self.bo.map()
        # Interpret the buffer as a 1-dimensional array then change its view to the expected shape
        return np.frombuffer(mv, dtype=self.dtype, count=np.prod(self.shape)).reshape(self.shape)

    def view_as_torch(self):
        return numpy_to_torch(self.view_as_np())
    
    def to(self, dest):
        if dest == "npu":
            if self.on != "npu":
                self.bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
                self.on = "npu"
        elif dest == "cpu":
            if self.on != "cpu":
                self.bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)
                self.on = "cpu"
        else:
            raise RuntimeError(f"Unknown destination for AIEBuffer.to(): {dest}")
        return self
    
    @staticmethod
    def from_np(buffer):
        shape = buffer.shape
        dtype = buffer.dtype
        size = np.prod(shape) * np.dtype(dtype).itemsize
        aie_buffer = AIEBuffer(shape=shape, dtype=dtype)
        aie_buffer.view_as_np()[:] = buffer
        aie_buffer.to("npu")
        return aie_buffer
    
    @staticmethod
    def from_torch(tensor):
        return AIEBuffer.from_np(torch_to_numpy(tensor))

class SingleXclbinCallable:
    def __init__(self, xclbin_path, kernel_name, insts_bin_path, args_spec, device_manager=None):
        self.device_manager = device_manager or AIEDeviceManager()
        self.context, self.xrt_kernel = self.device_manager.get_context_and_kernel(
            str(xclbin_path), kernel_name
        )
        with open(str(insts_bin_path), "rb") as f:
            instructions = np.frombuffer(f.read(), dtype=np.uint32)
        insts_bo = pyxrt.bo(
            self.device_manager.device,
            instructions.nbytes,
            pyxrt.bo.cacheable,
            self.xrt_kernel.group_id(1),
        )
        insts_bo.write(instructions.view(np.uint8), 0)
        self.insts_buffer = AIEBuffer(shape=(len(instructions),), dtype=np.uint32, bo=insts_bo)
        self.insts_buffer.to("npu")
        self.args_spec = args_spec
    
    def __call__(self, *buffers):
        assert len(buffers) == len(self.args_spec)
        assert all(
            buffers[i].shape == self.args_spec[i].shape and buffers[i].dtype == self.args_spec[i].dtype
            for i in range(len(buffers))
        ), "Input buffer shapes or dtypes do not match expected argument specification."
        self.insts_buffer.to("npu")
        for buffer in buffers:
            buffer.to("npu")
        opcode = 3
        bos = [buffer.bo for buffer in buffers]
        run = self.xrt_kernel(opcode, self.insts_buffer.bo, self.insts_buffer.shape[0], *bos)
        for buffer in buffers:
            buffer.to("cpu") 

