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

        # Compute oc_chunk, ic_chunk, and padded transfer size.
        # (must match design.py logic)
        self._oc_chunk = self._compute_oc_chunk()
        self._ic_chunk = self._compute_ic_chunk()
        self._wt_chunk_transfer = self._compute_wt_chunk_transfer()

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
        fused_suffix = "_fused" if self._fused_bias_silu else ""
        bias_suffix = "_bias" if self.has_bias and not self._fused_bias_silu else ""
        file_name_base = (
            f"{prefix}{self.in_channels}ic_{self.out_channels}oc_"
            f"{self.height}h_{self.width}w_"
            f"k{self.kernel_size}_s{self.stride}_"
            f"{self.num_aie_columns}col{fused_suffix}{bias_suffix}"
        )

        # Select design function and kernel source based on kernel_size
        if self.kernel_size == 1:
            design_callback = "my_conv2d"
            kernel_obj_name = "conv2dk1_bf16.o"
            kernel_src_name = "conv2dk1_bf16.cc"
        elif self._ic_chunk < self.in_channels:
            # IC streaming uses separate .o to avoid _ic_accum overhead
            design_callback = "my_conv2d_k3"
            kernel_obj_name = "conv2dk3_bf16_icstream.o"
            kernel_src_name = "conv2dk3_bf16_icstream.cc"
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

    def _compute_oc_chunk(self):
        """Compute per-core OC chunk size, matching design.py L1 budget logic.

        When weights don't fit in L1 alongside input/output FIFOs, the design
        streams weights in smaller OC-group chunks.  This method replicates
        that decision so forward() can pack the DDR weight buffer to match
        the TAP offsets used by the runtime sequence.
        """
        L1_SIZE = 65536
        OVERHEAD = 1040
        MAX_BDS = 16
        IC_ACCUM_STATIC_BYTES = 12800  # _ic_accum in icstream .o
        oc_per_col = self.out_channels // self.num_aie_columns
        k_elems = self.kernel_size * self.kernel_size
        fused = self._fused_bias_silu
        out_w = self.width // self.stride if self.stride > 1 else self.width

        # Compute weights_per_col (elements, not bytes)
        wpc = oc_per_col * self.in_channels * k_elems
        if fused:
            wpc += oc_per_col

        if self.kernel_size == 1:
            # k1: Phase 1 (depth=2), Phase 2 (MemTile depth=1), Phase 3 (streaming)
            input_fbs_p1 = 2 * self.in_channels * self.width * 2
            wt_fbs = wpc * 2
            out_fbs = 2 * oc_per_col * out_w * 2
            if input_fbs_p1 + wt_fbs + out_fbs + OVERHEAD <= L1_SIZE:
                return oc_per_col
            mt_input_fbs = 1 * self.in_channels * self.width * 2
            if mt_input_fbs + wt_fbs + out_fbs + OVERHEAD <= L1_SIZE:
                return oc_per_col
            # Phase 3: k1 weight streaming through MemTile
            avail = L1_SIZE - OVERHEAD - mt_input_fbs
            if avail > 0:
                for try_oc in range(oc_per_col, 0, -8):
                    if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                        continue
                    wt_elems = try_oc * self.in_channels * k_elems
                    if fused:
                        wt_elems += try_oc
                    wt_bytes = wt_elems * 2
                    out_bytes = 2 * try_oc * out_w * 2
                    if wt_bytes + out_bytes <= avail:
                        return try_oc
            raise AIEOperatorConstraintError(
                f"AIEConv2d k1 infeasible: in_channels={self.in_channels}, "
                f"oc_per_col={oc_per_col}, width={self.width}, avail={avail} bytes."
            )
        else:
            # k3: Try full IC, then IC streaming (ic_chunk splits).
            # Mirror design.py's nested (ic_chunk, oc_chunk) search.
            for try_ic in ([self.in_channels] + [
                c for c in [64, 32, 16]
                if c < self.in_channels and self.in_channels % c == 0 and c % 8 == 0
            ]):
                is_ic_streaming = try_ic < self.in_channels
                input_fbs = 4 * try_ic * self.width * 2
                ic_accum_cost = IC_ACCUM_STATIC_BYTES if is_ic_streaming else 0
                avail = L1_SIZE - OVERHEAD - input_fbs - ic_accum_cost
                if avail <= 0:
                    continue
                for try_oc in range(oc_per_col, 0, -8):
                    if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                        continue
                    wt_elems = try_oc * try_ic * k_elems
                    if fused:
                        wt_elems += try_oc
                    wt_bytes = wt_elems * 2
                    out_bytes = 2 * try_oc * out_w * 2
                    if wt_bytes + out_bytes > avail:
                        continue
                    n_oc = oc_per_col // try_oc
                    n_ic = self.in_channels // try_ic
                    bd_estimate = n_oc * (n_ic + 1) + 1
                    if bd_estimate <= MAX_BDS:
                        return try_oc  # store oc_chunk; ic_chunk via _compute_ic_chunk
            raise AIEOperatorConstraintError(
                f"AIEConv2d k3 infeasible even with IC+OC streaming: "
                f"in_channels={self.in_channels}, oc_per_col={oc_per_col}, "
                f"width={self.width}. Cannot satisfy L1+BD constraints."
            )

    def _compute_ic_chunk(self):
        """Compute IC streaming chunk size (mirrors design.py search logic).

        Returns in_channels when IC streaming is not needed.
        """
        if self.kernel_size == 1:
            return self.in_channels  # k1 never uses IC streaming

        L1_SIZE = 65536
        OVERHEAD = 1040
        MAX_BDS = 16
        IC_ACCUM_STATIC_BYTES = 12800
        oc_per_col = self.out_channels // self.num_aie_columns
        k_elems = self.kernel_size * self.kernel_size
        fused = self._fused_bias_silu
        out_w = self.width // self.stride if self.stride > 1 else self.width

        for try_ic in ([self.in_channels] + [
            c for c in [64, 32, 16]
            if c < self.in_channels and self.in_channels % c == 0 and c % 8 == 0
        ]):
            is_ic_streaming = try_ic < self.in_channels
            input_fbs = 4 * try_ic * self.width * 2
            ic_accum_cost = IC_ACCUM_STATIC_BYTES if is_ic_streaming else 0
            avail = L1_SIZE - OVERHEAD - input_fbs - ic_accum_cost
            if avail <= 0:
                continue
            for try_oc in range(oc_per_col, 0, -8):
                if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                    continue
                wt_elems = try_oc * try_ic * k_elems
                if fused:
                    wt_elems += try_oc
                wt_bytes = wt_elems * 2
                out_bytes = 2 * try_oc * out_w * 2
                if wt_bytes + out_bytes > avail:
                    continue
                n_oc = oc_per_col // try_oc
                n_ic = self.in_channels // try_ic
                bd_estimate = n_oc * (n_ic + 1) + 1
                if bd_estimate <= MAX_BDS:
                    return try_ic
        return self.in_channels  # fallback (design.py will raise)

    def _compute_wt_chunk_transfer(self):
        """Compute padded weight chunk transfer size for BD factorization.

        Weight chunk = oc_chunk × ic_chunk × k_elems [+ oc_chunk bias].
        Must match design.py's _factorize_tensor_padded() behavior.
        """
        oc_chunk = self._oc_chunk
        ic_chunk = self._ic_chunk
        k_elems = self.kernel_size * self.kernel_size

        wt_chunk_elems = oc_chunk * ic_chunk * k_elems
        if self._fused_bias_silu:
            wt_chunk_elems += oc_chunk

        from iron.operators.conv2d.design import _factorize_tensor_padded

        padded, _, _, _, _ = _factorize_tensor_padded(wt_chunk_elems)
        return padded

    def set_up_runtime(self):
        total_input = self.in_channels * self.height * self.width

        oc_per_col = self.out_channels // self.num_aie_columns
        oc_chunk = self._oc_chunk
        ic_chunk = self._ic_chunk
        n_oc_groups = oc_per_col // oc_chunk
        n_ic_groups = self.in_channels // ic_chunk

        # Per-column weight buffer: n_oc_groups × n_ic_groups chunks.
        weights_per_col = n_oc_groups * n_ic_groups * self._wt_chunk_transfer
        total_weights = weights_per_col * self.num_aie_columns

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
                # Pack weights for IC+OC streaming.
                # DDR layout: [col][oc_g][ic_g] → each chunk = wt_chunk_transfer.
                # Each chunk holds: oc_chunk × ic_chunk × k_elems weights + oc_chunk bias.
                # Bias is appended to EVERY IC group chunk (last IC group uses real bias,
                # others use zero bias — the kernel selects based on ic_group_idx).
                b = bias if bias is not None else self.bias
                if b is None:
                    raise AIEOperatorConstraintError(
                        "AIEConv2d: fused bias+SiLU requires bias"
                    )
                bias_np = torch_to_numpy(b.to(torch.bfloat16)).ravel()
                oc_per_col = self.out_channels // self.num_aie_columns
                oc_chunk = self._oc_chunk
                ic_chunk = self._ic_chunk
                k_elems = self.kernel_size * self.kernel_size
                n_oc_groups = oc_per_col // oc_chunk
                n_ic_groups = self.in_channels // ic_chunk
                wt_per_chunk = oc_chunk * ic_chunk * k_elems  # without bias
                wt_chunk_elems = wt_per_chunk + oc_chunk       # with bias
                wt_chunk_transfer = self._wt_chunk_transfer
                pad = wt_chunk_transfer - wt_chunk_elems
                parts = []
                for col in range(self.num_aie_columns):
                    col_oc_base = col * oc_per_col
                    for oc_g in range(n_oc_groups):
                        oc_start_in_col = oc_g * oc_chunk
                        for ic_g in range(n_ic_groups):
                            # Weight slice: [oc_g_channels, ic_g_channels, k, k]
                            # weight_tiled layout: [oc_per_col/8, in_channels/8, k, k, 8, 8]
                            # We need to extract [oc_chunk, ic_chunk, k, k] sub-block.
                            # weight_tiled is [n_cols * oc_per_col * in_channels * k_elems]
                            # For col=i: offset = i * oc_per_col * in_channels * k_elems
                            # Within col: [oc_g, ic_g] block (oc×ic groups of 64).
                            # Tiled layout: [oc_per_col, in_channels, k_elems] in 8x8 tiles.
                            # We want oc_chunk×ic_chunk×k_elems contiguous from tiled buffer.
                            # Since tiling groups oc by 8 and ic by 8, and oc_chunk%8==0
                            # and ic_chunk%8==0, each (oc_g, ic_g) block IS contiguous.
                            col_offset = col * oc_per_col * self.in_channels * k_elems
                            # In tiled layout [oc_per_col/8, ic/8, k, k, 8, 8],
                            # oc_group g occupies rows [g*oc_chunk/8 .. (g+1)*oc_chunk/8).
                            # ic_group h occupies cols [h*ic_chunk/8 .. (h+1)*ic_chunk/8).
                            # stride per oc_group = ic/8 * k_elems * 64
                            ic_per_8 = self.in_channels // 8
                            oc_g_stride = ic_per_8 * k_elems * 64
                            ic_chunk_8 = ic_chunk // 8
                            oc_chunk_8 = oc_chunk // 8
                            wt_start = (col_offset
                                        + oc_g * oc_chunk_8 * oc_g_stride
                                        + ic_g * ic_chunk_8 * k_elems * 64)
                            # Each oc_chunk_8 row covers ic_per_8*k_elems*64 elements,
                            # but we only want ic_chunk_8 cols.  Extract row by row.
                            wt_block_parts = []
                            for ocr in range(oc_chunk_8):
                                row_start = (col_offset
                                             + (oc_g * oc_chunk_8 + ocr) * oc_g_stride
                                             + ic_g * ic_chunk_8 * k_elems * 64)
                                row_len = ic_chunk_8 * k_elems * 64
                                wt_block_parts.append(
                                    weight_tiled[row_start: row_start + row_len]
                                )
                            wt_chunk = np.concatenate(wt_block_parts)
                            parts.append(wt_chunk)
                            # Bias: real bias for last IC group, zeros otherwise
                            bias_oc_start = col_oc_base + oc_g * oc_chunk
                            if ic_g == n_ic_groups - 1:
                                parts.append(bias_np[bias_oc_start: bias_oc_start + oc_chunk])
                            else:
                                parts.append(np.zeros(oc_chunk, dtype=bfloat16))
                            if pad > 0:
                                parts.append(np.zeros(pad, dtype=bfloat16))
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
