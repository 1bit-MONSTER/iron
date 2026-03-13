# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from iron.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from iron.common.utils import torch_to_numpy, numpy_to_torch


def nchw_to_tiled(tensor):
    """Convert [N, C, H, W] tensor to tiled layout [H, C/8, W, 8] flattened.

    The tiled layout groups channels in chunks of 8 and interleaves
    them with spatial positions. This matches the data layout expected
    by the AIE conv2dk1_bf16 kernel.

    Args:
        tensor: PyTorch tensor of shape [N, C, H, W] (N must be 1).

    Returns:
        1D numpy array in bfloat16 with layout [H, C/8, W, 8].
    """
    assert tensor.shape[0] == 1, "Batch size must be 1"
    N, C, H, W = tensor.shape
    assert C % 8 == 0, f"Channels ({C}) must be a multiple of 8"

    # Reshape to [H, C/8, 8, W] then transpose last two dims to [H, C/8, W, 8]
    t = tensor[0]  # [C, H, W]
    t = t.reshape(C // 8, 8, H, W)  # [C/8, 8, H, W]
    t = t.permute(2, 0, 3, 1)  # [H, C/8, W, 8]
    t = t.contiguous()
    return torch_to_numpy(t).reshape(-1)


def tiled_to_nchw(flat, C, H, W):
    """Convert flat tiled [H, C/8, W, 8] back to [1, C, H, W].

    Args:
        flat: 1D numpy array in bfloat16 of size H * C * W.
        C: Number of channels.
        H: Spatial height.
        W: Spatial width.

    Returns:
        PyTorch tensor of shape [1, C, H, W] in bfloat16.
    """
    t = numpy_to_torch(flat.reshape(H, C // 8, W, 8))
    t = t.permute(1, 3, 0, 2)  # [C/8, 8, H, W]
    t = t.reshape(C, H, W)  # [C, H, W]
    return t.unsqueeze(0)  # [1, C, H, W]


def weights_to_tiled(weight):
    """Convert [O, I, 1, 1] weight tensor to tiled [O/8, I/8, 8, 8] flat.

    The tiled weight layout groups both input and output channels in
    chunks of 8. Within each (O_group, I_group) tile, weights are
    stored as [ic8, oc8] -- i.e., input channel varies fastest.

    Args:
        weight: PyTorch tensor of shape [O, I, 1, 1].

    Returns:
        1D numpy array in bfloat16 with layout [O/8, I/8, 8, 8].
    """
    O, I, kh, kw = weight.shape
    assert kh == 1 and kw == 1, "Only 1x1 kernels supported"
    assert O % 8 == 0, f"Out channels ({O}) must be a multiple of 8"
    assert I % 8 == 0, f"In channels ({I}) must be a multiple of 8"

    # weight is [O, I] for 1x1 conv
    w = weight.squeeze(-1).squeeze(-1)  # [O, I]
    w = w.reshape(O // 8, 8, I // 8, 8)  # [O/8, 8, I/8, 8]
    w = w.permute(0, 2, 3, 1)  # [O/8, I/8, 8(ic), 8(oc)]
    w = w.contiguous()
    return torch_to_numpy(w).reshape(-1)


def weights_to_tiled_3x3(weight):
    """Convert [O, I, 3, 3] weight tensor to tiled [O/8, I/8, 3, 3, 8, 8] flat.

    The tiled weight layout for 3x3 conv groups both input and output channels
    in chunks of 8 and keeps the spatial kernel dimensions explicit.
    Within each (O_group, I_group, ky, kx) position, weights are stored as
    [ic8, oc8] -- i.e., input channel varies fastest (same as 1x1).

    This matches the layout expected by the AIE conv2dk3_bf16 kernel and
    the existing conv2dk3_i8 kernel in mlir-aie programming examples.

    Args:
        weight: PyTorch tensor of shape [O, I, 3, 3].

    Returns:
        1D numpy array in bfloat16 with layout [O/8, I/8, 3, 3, 8, 8].
    """
    O, I, kh, kw = weight.shape
    assert kh == 3 and kw == 3, f"Expected 3x3 kernel, got {kh}x{kw}"
    assert O % 8 == 0, f"Out channels ({O}) must be a multiple of 8"
    assert I % 8 == 0, f"In channels ({I}) must be a multiple of 8"

    # weight: [O, I, 3, 3]
    # Reshape to [O/8, 8, I/8, 8, 3, 3]
    w = weight.reshape(O // 8, 8, I // 8, 8, 3, 3)
    # Permute to [O/8, I/8, 3, 3, 8(ic), 8(oc)]
    w = w.permute(0, 2, 4, 5, 3, 1)
    w = w.contiguous()
    return torch_to_numpy(w).reshape(-1)


class AIEConv2d(AIEOperatorBase):
    """AIE-accelerated 2D Convolution (1x1 and 3x3 kernels, bfloat16).

    Supports 1x1 and 3x3 convolutions with optional bias and activation.
    Channels must be multiples of 8. Input is expected in NCHW format
    and is converted to tiled layout internally.

    For 3x3 kernels, stride 1 and stride 2 are supported. Border handling
    (vertical padding) is done in the AIE kernel via the check parameter.
    Horizontal zero-padding is also handled by the kernel.

    Args:
        in_channels: Number of input channels (must be multiple of 8).
        out_channels: Number of output channels (must be multiple of 8).
        kernel_size: Convolution kernel size (1 or 3).
        stride: Convolution stride (1 for all; 1 or 2 for kernel_size=3).
        height: Spatial height of input.
        width: Spatial width of input (must be multiple of 4 for vectorization).
        has_bias: Whether to include bias.
        activation: Optional activation function ('silu' or None).
        num_aie_columns: Number of AIE columns for parallelism.
        context: AIEContext instance.
    """

    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size=1,
        stride=1,
        height=None,
        width=None,
        has_bias=True,
        activation=None,
        num_aie_columns=1,
        context=None,
        register=True,
    ):
        assert kernel_size in (1, 3), f"kernel_size must be 1 or 3, got {kernel_size}"
        if kernel_size == 1:
            assert stride == 1, "Only stride=1 supported for 1x1 conv"
        else:
            assert stride in (1, 2), "Only stride 1 or 2 supported for 3x3 conv"
        assert (
            in_channels % 8 == 0
        ), f"in_channels ({in_channels}) must be a multiple of 8"
        assert (
            out_channels % 8 == 0
        ), f"out_channels ({out_channels}) must be a multiple of 8"
        assert (
            height is not None and width is not None
        ), "height and width must be specified"
        assert (
            width % 4 == 0
        ), f"width ({width}) must be a multiple of 4 for vectorized kernel"
        assert out_channels % num_aie_columns == 0, (
            f"out_channels ({out_channels}) must be divisible by "
            f"num_aie_columns ({num_aie_columns})"
        )
        if kernel_size == 3 and stride == 2:
            assert height % 2 == 0, f"height ({height}) must be even for stride=2"
            assert width % 2 == 0, f"width ({width}) must be even for stride=2"

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.height = height
        self.width = width
        self.has_bias = has_bias
        self.activation = activation
        self.num_aie_columns = num_aie_columns

        # Store bias separately (applied in Python after conv)
        self.bias = None

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=register)

    def get_artifacts(self, prefix="conv2d_"):
        """Create compilation artifacts without registering them.

        Args:
            prefix: Prefix for artifact file names (allows multiple
                independent compilations of the same operator config).

        Returns:
            Tuple of (xclbin_artifact, insts_artifact).
        """
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"{prefix}{self.in_channels}ic_{self.out_channels}oc_"
            f"{self.height}h_{self.width}w_"
            f"k{self.kernel_size}_s{self.stride}_"
            f"{self.num_aie_columns}col"
        )

        # Select design function and kernel source based on kernel_size
        if self.kernel_size == 1:
            design_callback = "my_conv2d"
            kernel_obj_name = "conv2dk1_bf16.o"
            kernel_src_name = "conv2dk1_bf16.cc"
        else:
            design_callback = "my_conv2d_k3"
            kernel_obj_name = "conv2dk3_bf16.o"
            kernel_src_name = "conv2dk3_bf16.cc"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn=design_callback,
            callback_args=[
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.out_channels,
                self.kernel_size,
                self.stride,
                self.has_bias,
                self.activation,
                self.num_aie_columns,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    kernel_obj_name,
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir
                            / "aie_kernels"
                            / "aie2p"
                            / kernel_src_name
                        )
                    ],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        return (xclbin_artifact, insts_artifact)

    def set_up_artifacts(self):
        xclbin_artifact, insts_artifact = self.get_artifacts()
        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    @property
    def out_height(self):
        """Output spatial height."""
        if self.kernel_size == 3 and self.stride == 2:
            return self.height // 2
        return self.height

    @property
    def out_width(self):
        """Output spatial width."""
        if self.kernel_size == 3 and self.stride == 2:
            return self.width // 2
        return self.width

    @property
    def _fused_bias_silu(self):
        """Whether bias+SiLU is fused into the kernel."""
        return self.has_bias and self.activation == "silu"

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width

        if self.kernel_size == 1:
            total_weights = self.out_channels * self.in_channels
        else:
            # 3x3: [O/8, I/8, 3, 3, 8, 8] = O * I * 9
            total_weights = self.out_channels * self.in_channels * 9

        # When bias+SiLU is fused, bias is packed at the end of weights
        if self._fused_bias_silu:
            total_weights += self.out_channels

        total_output = self.out_channels * self.out_height * self.out_width

        self.add_buffer("input", total_input)
        self.add_buffer("weights", total_weights)
        self.add_buffer("output", total_output)

        self.add_kernel(
            "conv2d",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("conv2d", "input", "weights", "output")

    def forward(self, x, weight=None, bias=None):
        """Run conv2d on the NPU.

        Args:
            x: Input tensor of shape [N, C_in, H, W] in bfloat16.
            weight: Optional weight tensor [C_out, C_in, kH, kW] in bfloat16.
                If None, weights must have been previously written.
            bias: Optional bias tensor [C_out] in bfloat16.
                If None and has_bias was True, bias must have been set.

        Returns:
            Output tensor of shape [N, C_out, H_out, W_out] in bfloat16.
        """
        if x.dtype != torch.bfloat16:
            raise AIEOperatorConstraintError("AIEConv2d: input must be bfloat16")
        if x.shape[0] != 1:
            raise AIEOperatorConstraintError("AIEConv2d: batch size must be 1")
        if x.shape[1] != self.in_channels:
            raise AIEOperatorConstraintError(
                f"AIEConv2d: expected {self.in_channels} input channels, "
                f"got {x.shape[1]}"
            )
        if x.shape[2] != self.height or x.shape[3] != self.width:
            raise AIEOperatorConstraintError(
                f"AIEConv2d: expected spatial dims ({self.height}, {self.width}), "
                f"got ({x.shape[2]}, {x.shape[3]})"
            )

        # Convert input to tiled layout and write to buffer
        input_tiled = nchw_to_tiled(x)
        self.write_buffer("input", input_tiled)

        # Convert and write weights (+ packed bias when fused)
        if weight is not None:
            if self.kernel_size == 1:
                weight_tiled = weights_to_tiled(weight)
            else:
                weight_tiled = weights_to_tiled_3x3(weight)

            if self._fused_bias_silu:
                # Pack bias after each column's weights for the fused kernel.
                # Layout: [col0_wt, col0_bias, col1_wt, col1_bias, ...]
                b = bias if bias is not None else self.bias
                if b is None:
                    raise AIEOperatorConstraintError(
                        "AIEConv2d: fused bias+SiLU requires bias"
                    )
                bias_np = torch_to_numpy(b.to(torch.bfloat16)).ravel()
                oc_per_col = self.out_channels // self.num_aie_columns
                k_elems = self.kernel_size * self.kernel_size
                wt_per_col = oc_per_col * self.in_channels * k_elems
                bias_per_col = oc_per_col
                parts = []
                for col in range(self.num_aie_columns):
                    wt_start = col * wt_per_col
                    parts.append(weight_tiled[wt_start : wt_start + wt_per_col])
                    b_start = col * bias_per_col
                    parts.append(bias_np[b_start : b_start + bias_per_col])
                weight_tiled = np.concatenate(parts)

            self.write_buffer("weights", weight_tiled)

        # Zero the output buffer
        oh, ow = self.out_height, self.out_width
        total_output = self.out_channels * oh * ow
        self.write_buffer("output", np.zeros(total_output, dtype=bfloat16))

        # Run on NPU
        self.run_runlist()

        # Read output and convert back to NCHW
        output_flat = self.read_buffer(
            "output", (total_output,), copy=True, dtype=bfloat16
        )
        result = tiled_to_nchw(output_flat, self.out_channels, oh, ow)

        if self._fused_bias_silu:
            # Bias and SiLU were applied by the kernel -- nothing to do
            pass
        else:
            # Apply bias in Python (not fused into kernel)
            if bias is not None:
                result = result + bias.reshape(1, -1, 1, 1)
            elif self.bias is not None:
                result = result + self.bias.reshape(1, -1, 1, 1)

            # Apply activation
            if self.activation == "silu":
                result = torch.nn.functional.silu(result)

        return result
