# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
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


def nchw_to_tiled_int8(tensor):
    """Convert [N, C, H, W] int8 tensor to tiled layout [H, C/8, W, 8] flattened.

    Args:
        tensor: PyTorch tensor of shape [N, C, H, W] (N must be 1), int8.

    Returns:
        1D numpy array in int8 with layout [H, C/8, W, 8].
    """
    assert tensor.shape[0] == 1, "Batch size must be 1"
    N, C, H, W = tensor.shape
    assert C % 8 == 0, f"Channels ({C}) must be a multiple of 8"

    t = tensor[0]  # [C, H, W]
    t = t.reshape(C // 8, 8, H, W)  # [C/8, 8, H, W]
    t = t.permute(2, 0, 3, 1)  # [H, C/8, W, 8]
    t = t.contiguous()
    return t.numpy().astype(np.int8).reshape(-1)


def tiled_to_nchw_int8(flat, C, H, W):
    """Convert flat tiled [H, C/8, W, 8] int8 back to [1, C, H, W].

    Args:
        flat: 1D numpy array in int8 of size H * C * W.
        C: Number of channels.
        H: Spatial height.
        W: Spatial width.

    Returns:
        PyTorch tensor of shape [1, C, H, W] in int8.
    """
    t = torch.from_numpy(flat.reshape(H, C // 8, W, 8).copy())
    t = t.permute(1, 3, 0, 2)  # [C/8, 8, H, W]
    t = t.reshape(C, H, W)  # [C, H, W]
    return t.unsqueeze(0).to(torch.int8)  # [1, C, H, W]


def weights_to_tiled_int8(weight):
    """Convert [O, I, 1, 1] int8 weight tensor to tiled [O/8, I/8, 8, 8] flat.

    Within each (O_group, I_group) tile, weights are stored as
    [ic8, oc8] -- input channel varies fastest.

    Args:
        weight: PyTorch tensor of shape [O, I, 1, 1] in int8.

    Returns:
        1D numpy array in int8 with layout [O/8, I/8, 8, 8].
    """
    O, I, kh, kw = weight.shape
    assert kh == 1 and kw == 1, "Only 1x1 kernels supported"
    assert O % 8 == 0, f"Out channels ({O}) must be a multiple of 8"
    assert I % 8 == 0, f"In channels ({I}) must be a multiple of 8"

    w = weight.squeeze(-1).squeeze(-1)  # [O, I]
    w = w.reshape(O // 8, 8, I // 8, 8)  # [O/8, 8, I/8, 8]
    w = w.permute(0, 2, 3, 1)  # [O/8, I/8, 8(ic), 8(oc)]
    w = w.contiguous()
    return w.numpy().astype(np.int8).reshape(-1)


def weights_to_tiled_int8_k3(weight):
    """Convert [O, I, 3, 3] int8 weight tensor to tiled [O/8, I/8, 3, 3, 8, 8] flat.

    Within each (O_group, I_group, kh, kw) tile, weights are stored as
    [ic8, oc8] -- input channel varies fastest.

    Args:
        weight: PyTorch tensor of shape [O, I, 3, 3] in int8.

    Returns:
        1D numpy array in int8 with layout [O/8, I/8, 3, 3, 8, 8].
    """
    O, I, kh, kw = weight.shape
    assert kh == 3 and kw == 3, "Only 3x3 kernels supported"
    assert O % 8 == 0, f"Out channels ({O}) must be a multiple of 8"
    assert I % 8 == 0, f"In channels ({I}) must be a multiple of 8"

    # [O, I, 3, 3] -> [O/8, 8, I/8, 8, 3, 3]
    w = weight.reshape(O // 8, 8, I // 8, 8, 3, 3)
    # -> [O/8, I/8, 3, 3, 8(ic), 8(oc)]
    w = w.permute(0, 2, 4, 5, 3, 1)
    w = w.contiguous()
    return w.numpy().astype(np.int8).reshape(-1)


def _compute_k3_fused_streaming(in_channels, out_channels, width, out_w):
    """Compute OC streaming params for fused k3 conv (bias packed in weights).

    Must match the L1 budget logic in my_conv2d_int8_k3_fused() exactly.

    Returns:
        (n_oc_groups, oc_chunk)
    """
    input_row_size = in_channels * width
    _BD_WRAP_MAX = 64

    for try_depth in [4, 3]:
        phys_bufs = try_depth + 1
        input_fbs = phys_bufs * input_row_size
        avail = 65536 - 1040 - input_fbs
        if avail <= 0:
            continue
        for try_oc in range(out_channels, 0, -8):
            if out_channels % try_oc != 0 or try_oc % 8 != 0:
                continue
            wt_bytes = try_oc * in_channels * 9 + try_oc * 4
            out_bytes = 2 * try_oc * out_w
            if wt_bytes + out_bytes > avail:
                continue
            n_oc = out_channels // try_oc
            if n_oc > _BD_WRAP_MAX:
                continue
            return (n_oc, try_oc)

    raise ValueError(
        f"k3 fused int8 conv2d infeasible: "
        f"IC={in_channels}, OC={out_channels}, W={width}"
    )


class AIEConv2dInt8(AIEOperatorBase):
    """AIE-accelerated 2D Convolution (int8).

    Performs int8 x int8 -> int32 MAC with right-shift requantization
    to produce int8 output. Channels must be multiples of 8.

    When fused=True (kernel_size=3 only), performs conv + bias + SiLU
    using a fully integer pipeline with sigmoid LUT lookup. Bias is
    packed at the end of the weight buffer to avoid a 3rd DMA channel.

    Args:
        in_channels: Number of input channels (must be multiple of 8).
        out_channels: Number of output channels (must be multiple of 8).
        kernel_size: Convolution kernel size (1 or 3).
        stride: Convolution stride.
        height: Spatial height of input.
        width: Spatial width of input.
        scale: Right-shift bits for int32 -> int8 requantization (non-fused).
        fused: If True, use fused conv+bias+SiLU kernel (k3 only).
        shift1: Acc -> int8 shift for LUT lookup (required if fused=True).
        shift2: SiLU product -> int8 shift (required if fused=True).
        num_aie_columns: Number of AIE columns (only 1 supported).
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
        scale=10,
        fused=False,
        shift1=None,
        shift2=None,
        num_aie_columns=1,
        context=None,
        register=True,
    ):
        assert kernel_size in (1, 3), f"kernel_size must be 1 or 3, got {kernel_size}"
        if kernel_size == 1:
            assert stride == 1, "Only stride=1 supported for 1x1 conv"
        else:
            assert stride in (1, 2), "Only stride 1 or 2 supported for 3x3 conv"
        if fused:
            assert kernel_size in (1, 3), "fused mode supported for kernel_size=1 and 3"
            assert (
                shift1 is not None and shift2 is not None
            ), "shift1 and shift2 required for fused mode"
        assert (
            in_channels % 8 == 0
        ), f"in_channels ({in_channels}) must be a multiple of 8"
        assert (
            out_channels % 8 == 0
        ), f"out_channels ({out_channels}) must be a multiple of 8"
        assert (
            height is not None and width is not None
        ), "height and width must be specified"
        assert num_aie_columns == 1, "Only 1 column supported for int8 conv2d"

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.height = height
        self.width = width
        self.scale = scale
        self.fused = fused
        self.shift1 = shift1
        self.shift2 = shift2
        self.num_aie_columns = num_aie_columns

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context, register=register)

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

    def get_artifacts(self, prefix="conv2d_int8_"):
        """Create compilation artifacts without registering them.

        Args:
            prefix: Prefix for artifact file names (allows multiple
                independent compilations of the same operator config).

        Returns:
            Tuple of (xclbin_artifact, insts_artifact).
        """
        operator_dir = Path(__file__).parent

        if self.fused and self.kernel_size == 3:
            file_name_base = (
                f"{prefix}{self.in_channels}ic_{self.out_channels}oc_"
                f"{self.height}h_{self.width}w_k3s{self.stride}"
                f"_fused_sh{self.shift1}_{self.shift2}"
            )
            callback_fn = "my_conv2d_int8_k3_fused"
            callback_args = [
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.out_channels,
                self.shift1,
                self.shift2,
                self.stride,
            ]
            kernel_obj_name = "conv2dk3_i8_fused_packed.o"
            kernel_src = "conv2dk3_i8_fused_packed.cc"
            kernel_extra_flags = ["-DINT8_ACT"]
        elif self.kernel_size == 3:
            file_name_base = (
                f"{prefix}{self.in_channels}ic_{self.out_channels}oc_"
                f"{self.height}h_{self.width}w_k3s{self.stride}"
                f"_sc{self.scale}"
            )
            callback_fn = "my_conv2d_int8_k3"
            callback_args = [
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.out_channels,
                self.scale,
                self.stride,
            ]
            kernel_obj_name = "conv2dk3_i8.o"
            kernel_src = "conv2dk3_i8.cc"
            kernel_extra_flags = ["-DINT8_ACT"]
        elif self.fused and self.kernel_size == 1:
            file_name_base = (
                f"{prefix}{self.in_channels}ic_{self.out_channels}oc_"
                f"{self.height}h_{self.width}w_k1"
                f"_fused_sh{self.shift1}_{self.shift2}"
            )
            callback_fn = "my_conv2d_int8_fused"
            callback_args = [
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.out_channels,
                self.shift1,
                self.shift2,
            ]
            kernel_obj_name = "conv2dk1_i8_fused.o"
            kernel_src = "conv2dk1_i8_fused.cc"
            kernel_extra_flags = ["-DINT8_ACT"]
        else:
            file_name_base = (
                f"{prefix}{self.in_channels}ic_{self.out_channels}oc_"
                f"{self.height}h_{self.width}w_sc{self.scale}"
            )
            callback_fn = "my_conv2d_int8"
            kernel_src = "conv2dk1_i8.cc"
            # Vectorized path: width must be multiple of 32 (MMUL_M*NUM_ACC)
            # and in_channels >= 24 (IC/8 > 2 for pipeline min iterations)
            use_vectorized = self.width % 32 == 0 and self.in_channels >= 24
            if use_vectorized:
                kernel_obj_name = "conv2dk1_i8_vec.o"
                kernel_extra_flags = ["-DINT8_ACT"]
            else:
                kernel_obj_name = "conv2dk1_i8.o"
                kernel_extra_flags = ["-DINT8_ACT", "-DSCALAR"]
            callback_args = [
                self.context.device_manager.device_type,
                self.height,
                self.width,
                self.in_channels,
                self.out_channels,
                self.scale,
            ]

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn=callback_fn,
            callback_args=callback_args,
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    kernel_obj_name,
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir / "aie_kernels" / "aie2p" / kernel_src
                        )
                    ],
                    extra_flags=kernel_extra_flags,
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

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width
        out_h = self.out_height
        out_w = self.out_width

        if self.fused and self.kernel_size == 3:
            # Packed weight buffer: weights + bias per OC chunk
            n_oc_groups, oc_chunk = _compute_k3_fused_streaming(
                self.in_channels, self.out_channels, self.width, out_w
            )
            wt_chunk_elems = oc_chunk * self.in_channels * 9 + oc_chunk * 4
            total_weights = n_oc_groups * wt_chunk_elems
        elif self.kernel_size == 3:
            total_weights = self.out_channels * self.in_channels * 9
        else:
            total_weights = self.out_channels * self.in_channels

        total_output = self.out_channels * out_h * out_w

        self.add_buffer("input", total_input, dtype=np.int8)
        self.add_buffer("weights", total_weights, dtype=np.int8)
        self.add_buffer("output", total_output, dtype=np.int8)

        self.add_kernel(
            "conv2d_int8",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("conv2d_int8", "input", "weights", "output")

    def forward(self, x, weight, bias=None):
        """Run int8 conv2d on the NPU.

        Args:
            x: Input tensor of shape [N, C_in, H, W] in int8.
            weight: Weight tensor [C_out, C_in, K, K] in int8.
            bias: (optional) Bias tensor [C_out] in int32. Required if fused.

        Returns:
            Output tensor of shape [N, C_out, H_out, W_out] in int8.
        """
        if x.dtype != torch.int8:
            raise AIEOperatorConstraintError("AIEConv2dInt8: input must be int8")
        if x.shape[0] != 1:
            raise AIEOperatorConstraintError("AIEConv2dInt8: batch size must be 1")
        if self.fused and bias is None:
            raise AIEOperatorConstraintError(
                "AIEConv2dInt8: bias required for fused mode"
            )

        input_tiled = nchw_to_tiled_int8(x)
        self.write_buffer("input", input_tiled)

        out_h = self.out_height
        out_w = self.out_width

        if self.fused and self.kernel_size == 3:
            # Pack weights with interleaved bias per OC chunk
            n_oc_groups, oc_chunk = _compute_k3_fused_streaming(
                self.in_channels, self.out_channels, self.width, out_w
            )
            weight_tiled = weights_to_tiled_int8_k3(weight)
            wt_per_chunk = oc_chunk * self.in_channels * 9
            chunks = []
            for g in range(n_oc_groups):
                w_chunk = weight_tiled[g * wt_per_chunk : (g + 1) * wt_per_chunk]
                b_chunk = bias[g * oc_chunk : (g + 1) * oc_chunk]
                b_bytes = b_chunk.numpy().astype(np.int32).view(np.int8)
                chunks.append(np.concatenate([w_chunk, b_bytes]))
            packed = np.concatenate(chunks)
            self.write_buffer("weights", packed)
        elif self.kernel_size == 3:
            weight_tiled = weights_to_tiled_int8_k3(weight)
            self.write_buffer("weights", weight_tiled)
        else:
            weight_tiled = weights_to_tiled_int8(weight)
            self.write_buffer("weights", weight_tiled)

        total_output = self.out_channels * out_h * out_w
        self.write_buffer("output", np.zeros(total_output, dtype=np.int8))

        self.run_runlist()

        output_flat = self.read_buffer(
            "output", (total_output,), copy=True, dtype=np.int8
        )
        return tiled_to_nchw_int8(output_flat, self.out_channels, out_h, out_w)
