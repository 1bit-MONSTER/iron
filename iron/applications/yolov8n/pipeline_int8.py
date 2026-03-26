# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Int8 multi-PDI pipeline for YOLOv8n on NPU.

Only int8 convolutions run on NPU. All other operations (maxpool, upsample,
concat, bias addition, SiLU activation, dequantization) run on CPU in float.

All 63 conv PDIs are merged into a single xclbin with one hardware context,
following the same pattern as the bf16 pipeline (pipeline.py).

Each conv layer gets its own PDI with a calibrated right-shift value
computed from calibration data. Between NPU conv calls, the CPU handles:
  int8 output → dequant to float → add bias → SiLU → float input for next layer
"""

import math

import numpy as np
import torch
import torch.nn.functional as F

from iron.common import AIEOperatorBase
from iron.common.aie_device_manager import pyxrt
from iron.operators.conv2d_int8.op import (
    AIEConv2dInt8,
    nchw_to_tiled_int8,
    tiled_to_nchw_int8,
    weights_to_tiled_int8,
    weights_to_tiled_int8_k3,
)
from iron.applications.yolov8n.quantize import Int8Quantizer


class Int8ConvPipeline(AIEOperatorBase):
    """Base multi-PDI pipeline for int8 conv2d layers on NPU.

    Each conv layer gets its own PDI (no deduplication) with a calibrated
    right-shift value. The shift is baked into the AIE core binary at
    compile time. Between conv layers, CPU handles dequant/bias/SiLU.

    Subclasses implement _register_all_layers() to define which conv layers
    belong to this pipeline stage, and forward() for the execution flow.
    """

    # NPU driver limits PDIs per hw_context to 32.
    _MAX_PDIS_PER_XCLBIN = 32

    def __init__(self, context=None):
        self._pdi_map = {}  # layer_name -> {sub_op, xclbin, insts, kernel_name}
        self._layer_map = {}  # layer_name -> pdi_key (same as layer_name)
        self._kernel_id_counter = 0x901
        self._group_xclbins = []  # combined xclbin per group
        self._shifts = {}  # layer_name -> shift value

        super().__init__(context=context)

    def _next_kernel_id(self):
        kid = self._kernel_id_counter
        self._kernel_id_counter += 1
        return kid

    def _register_int8_conv(
        self, layer_name, in_ch, out_ch, h, w, ks, stride, shift
    ):
        """Register an int8 conv layer with its own PDI."""
        self._layer_map[layer_name] = layer_name
        self._shifts[layer_name] = shift
        sub_op = AIEConv2dInt8(
            in_channels=in_ch,
            out_channels=out_ch,
            kernel_size=ks,
            stride=stride,
            height=h,
            width=w,
            scale=shift,
            context=self.context,
            register=False,
        )
        self._pdi_map[layer_name] = {"sub_op": sub_op}

    def set_up_artifacts(self):
        self._register_all_layers()

        pdi_items = list(self._pdi_map.items())
        max_per = self._MAX_PDIS_PER_XCLBIN
        n_groups = (len(pdi_items) + max_per - 1) // max_per

        artifacts = []
        self._group_xclbins = []
        pdi_idx = 0

        for g_idx in range(n_groups):
            start = g_idx * max_per
            end = min(start + max_per, len(pdi_items))
            group = pdi_items[start:end]

            prev_xclbin = None
            for key, entry in group:
                sub_op = entry["sub_op"]
                kid = self._next_kernel_id()
                prefix = f"yolov8n_i8_{pdi_idx:03d}_"
                xclbin, insts = sub_op.get_artifacts(prefix=prefix)

                kernel_name = f"yolov8n_i8_k{pdi_idx:03d}"
                xclbin.extra_flags += [
                    f"--xclbin-instance-name={kernel_name}",
                    f"--xclbin-kernel-id={kid:#x}",
                ]
                xclbin.kernel_name = kernel_name

                if prev_xclbin is not None:
                    xclbin.xclbin_input = prev_xclbin
                    xclbin.depends += [prev_xclbin]

                entry["xclbin"] = xclbin
                entry["insts"] = insts
                entry["kernel_name"] = kernel_name
                entry["group_idx"] = g_idx
                artifacts.append(insts)
                prev_xclbin = xclbin
                pdi_idx += 1

            artifacts.append(prev_xclbin)
            self._group_xclbins.append(prev_xclbin)

        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        for key, entry in self._pdi_map.items():
            group_xclbin = self._group_xclbins[entry["group_idx"]]
            self.add_kernel(
                entry["kernel_name"],
                group_xclbin,
                entry["xclbin"].kernel_name,
                entry["insts"],
            )
        self._setup_layer_buffers()

    def _setup_layer_buffers(self):
        for lname in self._layer_map:
            entry = self._pdi_map[lname]
            sub_op = entry["sub_op"]
            in_sz = sub_op.in_channels * sub_op.height * sub_op.width
            k_sq = sub_op.kernel_size**2
            w_sz = sub_op.out_channels * sub_op.in_channels * k_sq
            out_sz = (
                sub_op.out_channels * sub_op.out_height * sub_op.out_width
            )
            self.add_buffer(f"{lname}_input", in_sz, dtype=np.int8)
            self.add_buffer(f"{lname}_weights", w_sz, dtype=np.int8)
            self.add_buffer(f"{lname}_output", out_sz, dtype=np.int8)
            # Register in the runlist so the buffer pool allocator knows
            # which buffers are used together and must not share a BO.
            self.add_to_runlist(
                entry["kernel_name"],
                f"{lname}_input",
                f"{lname}_weights",
                f"{lname}_output",
            )

    def _run_single_kernel(self, kernel_name, *buffer_names):
        """Execute a single kernel invocation."""
        context, xrt_kernel, insts_bo, insts_len = self.xrt_kernels[
            kernel_name
        ]
        insts_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        bos = [self.buffer_bos[bn] for bn in buffer_names]
        for bo in bos:
            bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        opcode = 3
        run = xrt_kernel(opcode, insts_bo, insts_len, *bos)
        result = run.wait()
        if result != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
            raise RuntimeError(f"Kernel {kernel_name} failed: {result}")
        for bo in bos:
            bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)

    def run_int8_conv(self, layer_name, x_int8, weight_int8):
        """Run int8 conv on NPU, return int8 output tensor."""
        entry = self._pdi_map[layer_name]
        sub_op = entry["sub_op"]

        input_tiled = nchw_to_tiled_int8(x_int8)
        self.write_buffer(f"{layer_name}_input", input_tiled)

        if sub_op.kernel_size == 3:
            weight_tiled = weights_to_tiled_int8_k3(weight_int8)
        else:
            weight_tiled = weights_to_tiled_int8(weight_int8)
        self.write_buffer(f"{layer_name}_weights", weight_tiled)

        oh, ow = sub_op.out_height, sub_op.out_width
        total_output = sub_op.out_channels * oh * ow
        self.write_buffer(
            f"{layer_name}_output", np.zeros(total_output, dtype=np.int8)
        )

        self._run_single_kernel(
            entry["kernel_name"],
            f"{layer_name}_input",
            f"{layer_name}_weights",
            f"{layer_name}_output",
        )

        output_flat = self.read_buffer(
            f"{layer_name}_output", (total_output,), copy=True, dtype=np.int8
        )
        return tiled_to_nchw_int8(output_flat, sub_op.out_channels, oh, ow)

    def int8_cbs(self, x_float, layer_name, w_int8, w_scale, bias, in_act_scale):
        """CBS: quantize input → int8 conv NPU → dequant → bias → SiLU.

        Args:
            x_float: Float input tensor [1, C, H, W].
            layer_name: Pipeline layer identifier.
            w_int8: Int8 weight tensor [O, I, K, K].
            w_scale: Weight quantization scale (float).
            bias: Float bias tensor [O].
            in_act_scale: Input activation scale (from calibration).

        Returns:
            Float output tensor after dequant + bias + SiLU.
        """
        if in_act_scale == 0:
            in_act_scale = 1.0
        x_int8 = torch.clamp(
            torch.round(x_float / in_act_scale), -128, 127
        ).to(torch.int8)

        out_int8 = self.run_int8_conv(layer_name, x_int8, w_int8)

        shift = self._shifts[layer_name]
        dequant_scale = (2**shift) * w_scale * in_act_scale
        out_float = out_int8.float() * dequant_scale
        out_float = out_float + bias.view(1, -1, 1, 1)
        out_float = F.silu(out_float)
        return out_float

    def int8_conv_no_act(
        self, x_float, layer_name, w_int8, w_scale, bias, in_act_scale
    ):
        """Conv without activation: quantize → int8 conv NPU → dequant → bias.

        Same as int8_cbs but without the SiLU activation.
        """
        if in_act_scale == 0:
            in_act_scale = 1.0
        x_int8 = torch.clamp(
            torch.round(x_float / in_act_scale), -128, 127
        ).to(torch.int8)

        out_int8 = self.run_int8_conv(layer_name, x_int8, w_int8)

        shift = self._shifts[layer_name]
        dequant_scale = (2**shift) * w_scale * in_act_scale
        out_float = out_int8.float() * dequant_scale
        out_float = out_float + bias.view(1, -1, 1, 1)
        return out_float

    def _register_all_layers(self):
        raise NotImplementedError


def compute_layer_shift(w_scale, in_act_scale, out_act_scale):
    """Compute right-shift for NPU requantization.

    shift = round(log2(out_act_scale / (w_scale * in_act_scale)))

    This maps the int32 MAC accumulator range to int8 such that
    the int8 output, when dequantized, approximates the float result.

    Args:
        w_scale: Per-tensor weight scale.
        in_act_scale: Input activation scale.
        out_act_scale: Output activation scale (from calibration).

    Returns:
        Shift value clamped to [1, 31].
    """
    combined = w_scale * in_act_scale
    if combined == 0 or out_act_scale == 0:
        return 10  # safe default
    ratio = out_act_scale / combined
    shift = round(math.log2(max(ratio, 1.0)))
    return max(1, min(31, shift))
