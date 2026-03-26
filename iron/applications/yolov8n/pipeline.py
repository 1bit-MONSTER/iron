# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""YOLOv8n Multi-PDI Pipeline Operator.

Chains all YOLOv8n operator configurations into a single multi-PDI xclbin,
using 1 hardware context for the entire model. This avoids exhausting the
NPU's hw_context limit (~32) which was the bottleneck with per-operator
context allocation.

The approach follows the SwiGLU multi-PDI pattern: each unique operator
configuration gets its own PDI (xclbin partition) with a unique kernel ID.
All PDIs are merged into one combined xclbin via aiecc's --xclbin-input
chaining. At runtime, all kernels reference the same combined xclbin but
each uses its own instruction stream.
"""

import torch
import torch.nn.functional as F
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from iron.common import AIEOperatorBase
from iron.common.aie_device_manager import pyxrt
from iron.operators.conv2d.op import (
    AIEConv2d,
    nchw_to_tiled,
    tiled_to_nchw,
    weights_to_tiled,
    weights_to_tiled_3x3,
)
from iron.operators.maxpool2d.op import AIEMaxPool2d
from iron.operators.upsample.op import AIEUpsample
from iron.applications.yolov8n.blocks import _auto_columns


def _conv_key(in_ch, out_ch, h, w, kernel_size, stride, num_cols, activation=None):
    """Unique key for a conv2d configuration."""
    return (
        "conv2d",
        in_ch,
        out_ch,
        h,
        w,
        kernel_size,
        stride,
        num_cols,
        activation,
    )


def _pool_key(channels, h, w, kernel_size, stride, padding, num_cols):
    """Unique key for a maxpool2d configuration."""
    return ("maxpool2d", channels, h, w, kernel_size, stride, padding, num_cols)


def _upsample_key(channels, h, w, scale_factor, num_cols):
    """Unique key for an upsample configuration."""
    return ("upsample", channels, h, w, scale_factor, num_cols)


class YOLOv8nPipeline(AIEOperatorBase):
    """YOLOv8n full model as a single multi-PDI operator.

    Merges all ~52 unique operator configurations into one xclbin with
    one hardware context. Each layer is mapped to its unique PDI by
    config key, and layers sharing the same config share the same PDI
    (but have separate instruction streams only if dimensions differ).

    Args:
        img_height: Input image height (default 640).
        img_width: Input image width (default 640).
        nc: Number of classes (default 80 for COCO).
        reg_max: DFL regression max bins (default 16).
        context: AIEContext instance.
    """

    def __init__(
        self,
        img_height=640,
        img_width=640,
        nc=80,
        reg_max=16,
        context=None,
    ):
        self.img_height = img_height
        self.img_width = img_width
        self.nc = nc
        self.reg_max = reg_max

        # These will be populated by set_up_artifacts
        self.combined_xclbin = None
        self._pdi_map = {}  # config_key -> (xclbin_artifact, insts_artifact, sub_op)
        self._layer_map = {}  # layer_name -> config_key
        self._kernel_id_counter = 0x901

        # Weight storage (set by load_weights)
        self._weights = {}

        super().__init__(context=context)

    def _next_kernel_id(self):
        kid = self._kernel_id_counter
        self._kernel_id_counter += 1
        return kid

    def _register_conv(
        self, layer_name, in_ch, out_ch, h, w, kernel_size, stride, num_cols,
        activation=None,
    ):
        """Register a conv2d config; deduplicate by config key."""
        if num_cols == 0:
            num_cols = _auto_columns(in_ch, out_ch, kernel_size, w, stride)
        key = _conv_key(in_ch, out_ch, h, w, kernel_size, stride, num_cols, activation)
        self._layer_map[layer_name] = key

        if key not in self._pdi_map:
            sub_op = AIEConv2d(
                in_channels=in_ch,
                out_channels=out_ch,
                kernel_size=kernel_size,
                stride=stride,
                height=h,
                width=w,
                has_bias=True,
                activation=activation,
                num_aie_columns=num_cols,
                context=self.context,
                register=False,
            )
            self._pdi_map[key] = {"sub_op": sub_op, "xclbin": None, "insts": None}

    def _register_pool(
        self, layer_name, channels, h, w, kernel_size, stride, padding, num_cols
    ):
        """Register a maxpool2d config; deduplicate by config key."""
        key = _pool_key(channels, h, w, kernel_size, stride, padding, num_cols)
        self._layer_map[layer_name] = key

        if key not in self._pdi_map:
            sub_op = AIEMaxPool2d(
                channels=channels,
                height=h,
                width=w,
                kernel_size=kernel_size,
                stride=stride,
                padding=padding,
                num_aie_columns=num_cols,
                context=self.context,
                register=False,
            )
            self._pdi_map[key] = {"sub_op": sub_op, "xclbin": None, "insts": None}

    def _register_upsample(self, layer_name, channels, h, w, scale_factor, num_cols):
        """Register an upsample config; deduplicate by config key."""
        key = _upsample_key(channels, h, w, scale_factor, num_cols)
        self._layer_map[layer_name] = key

        if key not in self._pdi_map:
            sub_op = AIEUpsample(
                channels=channels,
                height=h,
                width=w,
                scale_factor=scale_factor,
                num_aie_columns=num_cols,
                context=self.context,
                register=False,
            )
            self._pdi_map[key] = {"sub_op": sub_op, "xclbin": None, "insts": None}

    def _register_cbs(self, name, in_ch, out_ch, ks, stride, h, w, cols):
        """Register a CBS block (conv2d with fused bias+SiLU)."""
        self._register_conv(name, in_ch, out_ch, h, w, ks, stride, cols,
                            activation="silu")

    def _register_bottleneck(self, name, channels, h, w, cols):
        """Register a Bottleneck block (two 3x3 convs)."""
        self._register_cbs(f"{name}_cv1", channels, channels, 3, 1, h, w, cols)
        self._register_cbs(f"{name}_cv2", channels, channels, 3, 1, h, w, cols)

    def _register_c2f(self, name, c_in, c_out, n_bn, h, w, cols):
        """Register a C2f block."""
        c = c_out // 2
        self._register_cbs(f"{name}_cv1", c_in, 2 * c, 1, 1, h, w, cols)
        for i in range(n_bn):
            self._register_bottleneck(f"{name}_bn{i}", c, h, w, cols)
        cv2_in = (2 + n_bn) * c
        self._register_cbs(f"{name}_cv2", cv2_in, c_out, 1, 1, h, w, cols)

    def _register_sppf(self, name, c_in, c_out, h, w, ks, cols):
        """Register an SPPF block."""
        c_ = c_in // 2
        padding = ks // 2
        self._register_cbs(f"{name}_cv1", c_in, c_, 1, 1, h, w, cols)
        # Three maxpool instances share config
        self._register_pool(f"{name}_mp1", c_, h, w, ks, 1, padding, cols)
        self._register_pool(f"{name}_mp2", c_, h, w, ks, 1, padding, cols)
        self._register_pool(f"{name}_mp3", c_, h, w, ks, 1, padding, cols)
        self._register_cbs(f"{name}_cv2", c_ * 4, c_out, 1, 1, h, w, cols)

    def _register_detect_branch(self, name, c_in, c_mid, c_out, h, w, cols):
        """Register a DetectBranch (2x CBS 3x3 + 1x bare Conv1x1)."""
        self._register_cbs(f"{name}_cv1", c_in, c_mid, 3, 1, h, w, cols)
        self._register_cbs(f"{name}_cv2", c_mid, c_mid, 3, 1, h, w, cols)
        cv3_cols = _auto_columns(c_mid, c_out, 1, w) if cols == 0 else cols
        self._register_conv(f"{name}_cv3", c_mid, c_out, h, w, 1, 1, cv3_cols)

    def _register_all_layers(self):
        """Register all unique operator configs for the full YOLOv8n model."""
        H, W = self.img_height, self.img_width
        cols = 0  # auto

        # ---- BACKBONE ----
        # L0: Conv3x3s2, 8->16, HxW -> H/2 x W/2
        self._register_cbs("bb_l0", 8, 16, 3, 2, H, W, cols)
        h2, w2 = H // 2, W // 2  # 320x320

        # L1: Conv3x3s2, 16->32, H/2 -> H/4
        self._register_cbs("bb_l1", 16, 32, 3, 2, h2, w2, cols)
        h4, w4 = h2 // 2, w2 // 2  # 160x160

        # L2: C2f n=1, 32->32, 160x160
        self._register_c2f("bb_l2", 32, 32, 1, h4, w4, cols)

        # L3: Conv3x3s2, 32->64, 160->80
        self._register_cbs("bb_l3", 32, 64, 3, 2, h4, w4, cols)
        h8, w8 = h4 // 2, w4 // 2  # 80x80

        # L4: C2f n=2, 64->64, 80x80
        self._register_c2f("bb_l4", 64, 64, 2, h8, w8, cols)

        # L5: Conv3x3s2, 64->128, 80->40
        self._register_cbs("bb_l5", 64, 128, 3, 2, h8, w8, cols)
        h16, w16 = h8 // 2, w8 // 2  # 40x40

        # L6: C2f n=2, 128->128, 40x40
        self._register_c2f("bb_l6", 128, 128, 2, h16, w16, cols)

        # L7: Conv3x3s2, 128->256, 40->20
        self._register_cbs("bb_l7", 128, 256, 3, 2, h16, w16, cols)
        h32, w32 = h16 // 2, w16 // 2  # 20x20

        # L8: C2f n=1, 256->256, 20x20
        self._register_c2f("bb_l8", 256, 256, 1, h32, w32, cols)

        # L9: SPPF k=5, 256->256, 20x20
        self._register_sppf("bb_l9", 256, 256, h32, w32, 5, cols)

        # ---- NECK (FPN up-path) ----
        # L10: Upsample 2x, 256ch, 20x20 -> 40x40
        self._register_upsample("nk_up1", 256, h32, w32, 2, cols)

        # L12: C2f (384->128, 40x40, n=1)
        self._register_c2f("nk_l12", 384, 128, 1, h16, w16, cols)

        # L13: Upsample 2x, 128ch, 40x40 -> 80x80
        self._register_upsample("nk_up2", 128, h16, w16, 2, cols)

        # L15: C2f (192->64, 80x80, n=1)
        self._register_c2f("nk_l15", 192, 64, 1, h8, w8, cols)

        # ---- NECK (PAN down-path) ----
        # L16: CBS 3x3s2, 64->64, 80->40
        self._register_cbs("nk_l16", 64, 64, 3, 2, h8, w8, cols)

        # L18: C2f (192->128, 40x40, n=1)
        self._register_c2f("nk_l18", 192, 128, 1, h16, w16, cols)

        # L19: CBS 3x3s2, 128->128, 40->20
        self._register_cbs("nk_l19", 128, 128, 3, 2, h16, w16, cols)

        # L21: C2f (384->256, 20x20, n=1)
        self._register_c2f("nk_l21", 384, 256, 1, h32, w32, cols)

        # ---- DETECT HEAD ----
        c_reg = 4 * self.reg_max  # 64
        c_cls = self.nc  # 80
        c2 = 64  # reg intermediate
        c3 = max(self.nc, 16)  # cls intermediate (80)

        # P3 scale (80x80, input 64ch)
        self._register_detect_branch("det_reg_p3", 64, c2, c_reg, h8, w8, cols)
        self._register_detect_branch("det_cls_p3", 64, c3, c_cls, h8, w8, cols)

        # P4 scale (40x40, input 128ch)
        self._register_detect_branch("det_reg_p4", 128, c2, c_reg, h16, w16, cols)
        self._register_detect_branch("det_cls_p4", 128, c3, c_cls, h16, w16, cols)

        # P5 scale (20x20, input 256ch)
        self._register_detect_branch("det_reg_p5", 256, c2, c_reg, h32, w32, cols)
        self._register_detect_branch("det_cls_p5", 256, c3, c_cls, h32, w32, cols)

    def set_up_artifacts(self):
        # Register all unique layer configs
        self._register_all_layers()

        # Build multi-PDI xclbin chain
        artifacts = []
        prev_xclbin = None
        pdi_keys = list(self._pdi_map.keys())

        for i, key in enumerate(pdi_keys):
            entry = self._pdi_map[key]
            sub_op = entry["sub_op"]
            kid = self._next_kernel_id()

            prefix = f"yolov8n_pdi{i:03d}_"
            xclbin, insts = sub_op.get_artifacts(prefix=prefix)

            kernel_name = f"yolov8n_k{i:03d}"
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

            artifacts.append(insts)
            prev_xclbin = xclbin

        artifacts.append(prev_xclbin)
        self.combined_xclbin = prev_xclbin
        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        # Register kernels for each unique PDI.
        # All kernels reference combined_xclbin but each has its own insts.
        for key, entry in self._pdi_map.items():
            self.add_kernel(
                entry["kernel_name"],
                self.combined_xclbin,
                entry["xclbin"].kernel_name,
                entry["insts"],
            )

        # Create per-layer buffers. We do NOT use add_to_runlist because
        # this operator executes kernels individually via _run_single_kernel
        # (writing activations between layers in Python). The monolithic
        # runlist pattern doesn't apply to a multi-layer pipeline.
        self._setup_layer_buffers()

    def _get_layer_entry(self, layer_name):
        """Get the PDI entry for a layer name."""
        key = self._layer_map[layer_name]
        return self._pdi_map[key]

    def _setup_layer_buffers(self):
        """Create all buffers needed for the pipeline.

        Each layer gets uniquely-named input/output (and weight for conv)
        buffers. The context's buffer pooling reuses same-sized BOs across
        layers that don't conflict.
        """
        for lname, key in self._layer_map.items():
            op_type = key[0]
            entry = self._pdi_map[key]
            sub_op = entry["sub_op"]

            if op_type == "conv2d":
                in_sz = sub_op.in_channels * sub_op.height * sub_op.width
                if sub_op.kernel_size == 1:
                    w_sz = sub_op.out_channels * sub_op.in_channels
                else:
                    w_sz = sub_op.out_channels * sub_op.in_channels * 9
                # Fused bias+SiLU packs bias into weight buffer
                if sub_op._fused_bias_silu:
                    w_sz += sub_op.out_channels
                out_sz = sub_op.out_channels * sub_op.out_height * sub_op.out_width
                self.add_buffer(f"{lname}_input", in_sz)
                self.add_buffer(f"{lname}_weights", w_sz)
                self.add_buffer(f"{lname}_output", out_sz)

            elif op_type == "maxpool2d":
                in_sz = sub_op.channels * sub_op.padded_height * sub_op.padded_width
                out_sz = sub_op.channels * sub_op.out_height * sub_op.out_width
                self.add_buffer(f"{lname}_input", in_sz)
                self.add_buffer(f"{lname}_output", out_sz)

            elif op_type == "upsample":
                in_sz = sub_op.channels * sub_op.height * sub_op.width
                out_sz = sub_op.channels * sub_op.out_height * sub_op.out_width
                self.add_buffer(f"{lname}_input", in_sz)
                self.add_buffer(f"{lname}_output", out_sz)

    def _run_conv(self, layer_name, x, weight, bias=None):
        """Run a single conv2d layer through the pipeline.

        When the sub-operator has fused bias+SiLU (activation='silu'),
        bias is packed into the weight buffer and applied on-chip.
        Otherwise, bias is applied in Python after the NPU returns.
        """
        entry = self._get_layer_entry(layer_name)
        sub_op = entry["sub_op"]

        # Convert input to tiled layout
        input_tiled = nchw_to_tiled(x)
        self.write_buffer(f"{layer_name}_input", input_tiled)

        # Convert and write weights
        if sub_op.kernel_size == 1:
            weight_tiled = weights_to_tiled(weight)
        else:
            weight_tiled = weights_to_tiled_3x3(weight)

        # Pack bias into weight buffer when fused bias+SiLU
        if sub_op._fused_bias_silu and bias is not None:
            from iron.common.utils import torch_to_numpy
            bias_np = torch_to_numpy(bias.to(torch.bfloat16)).ravel()
            oc_per_col = sub_op.out_channels // sub_op.num_aie_columns
            k_elems = sub_op.kernel_size * sub_op.kernel_size
            wt_per_col = oc_per_col * sub_op.in_channels * k_elems
            bias_per_col = oc_per_col
            parts = []
            for col in range(sub_op.num_aie_columns):
                wt_start = col * wt_per_col
                parts.append(weight_tiled[wt_start : wt_start + wt_per_col])
                b_start = col * bias_per_col
                parts.append(bias_np[b_start : b_start + bias_per_col])
            weight_tiled = np.concatenate(parts)

        self.write_buffer(f"{layer_name}_weights", weight_tiled)

        # Zero output
        oh, ow = sub_op.out_height, sub_op.out_width
        total_output = sub_op.out_channels * oh * ow
        self.write_buffer(f"{layer_name}_output", np.zeros(total_output, dtype=bfloat16))

        # Run this single kernel
        kernel_name = entry["kernel_name"]
        self._run_single_kernel(
            kernel_name,
            f"{layer_name}_input",
            f"{layer_name}_weights",
            f"{layer_name}_output",
        )

        # Read output
        output_flat = self.read_buffer(
            f"{layer_name}_output", (total_output,), copy=True, dtype=bfloat16
        )
        result = tiled_to_nchw(output_flat, sub_op.out_channels, oh, ow)

        if sub_op._fused_bias_silu:
            # Bias and SiLU already applied on-chip
            pass
        else:
            # Apply bias in Python (non-fused path)
            if bias is not None:
                result = result + bias.reshape(1, -1, 1, 1)

        return result

    def _run_cbs(self, layer_name, x, weight, bias):
        """Run a CBS layer (conv + bias + SiLU fused on-chip)."""
        return self._run_conv(layer_name, x, weight, bias)

    def _run_pool(self, layer_name, x):
        """Run a maxpool2d layer."""
        entry = self._get_layer_entry(layer_name)
        sub_op = entry["sub_op"]

        # Pad input with -inf
        x_padded = torch.nn.functional.pad(
            x.float(),
            (sub_op.padding, sub_op.padding, sub_op.padding, sub_op.padding),
            mode="constant",
            value=float("-inf"),
        ).to(torch.bfloat16)

        input_tiled = nchw_to_tiled(x_padded)
        self.write_buffer(f"{layer_name}_input", input_tiled)

        total_output = sub_op.channels * sub_op.out_height * sub_op.out_width
        self.write_buffer(
            f"{layer_name}_output", np.zeros(total_output, dtype=bfloat16)
        )

        kernel_name = entry["kernel_name"]
        self._run_single_kernel(
            kernel_name, f"{layer_name}_input", f"{layer_name}_output"
        )

        output_flat = self.read_buffer(
            f"{layer_name}_output", (total_output,), copy=True, dtype=bfloat16
        )
        return tiled_to_nchw(
            output_flat, sub_op.channels, sub_op.out_height, sub_op.out_width
        )

    def _run_upsample(self, layer_name, x):
        """Run an upsample layer."""
        entry = self._get_layer_entry(layer_name)
        sub_op = entry["sub_op"]

        input_tiled = nchw_to_tiled(x)
        self.write_buffer(f"{layer_name}_input", input_tiled)

        total_output = sub_op.channels * sub_op.out_height * sub_op.out_width
        self.write_buffer(
            f"{layer_name}_output", np.zeros(total_output, dtype=bfloat16)
        )

        kernel_name = entry["kernel_name"]
        self._run_single_kernel(
            kernel_name, f"{layer_name}_input", f"{layer_name}_output"
        )

        output_flat = self.read_buffer(
            f"{layer_name}_output", (total_output,), copy=True, dtype=bfloat16
        )
        return tiled_to_nchw(
            output_flat, sub_op.channels, sub_op.out_height, sub_op.out_width
        )

    def _run_single_kernel(self, kernel_name, *buffer_names):
        """Execute a single kernel invocation."""
        context, xrt_kernel, insts_bo, insts_len = self.xrt_kernels[kernel_name]
        insts_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        bos = [self.buffer_bos[bn] for bn in buffer_names]
        for bo in bos:
            bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        opcode = 3
        run = xrt_kernel(opcode, insts_bo, insts_len, *bos)
        result = run.wait()
        if result != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
            raise RuntimeError(
                f"Kernel {kernel_name} did not complete correctly: {result}"
            )
        for bo in bos:
            bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)

    def _run_c2f(self, name, x, weights, shortcut=True):
        """Run a C2f block through the pipeline.

        Args:
            name: Layer name prefix.
            x: Input tensor [1, C_in, H, W].
            weights: Weight dict with cv1, bottlenecks, cv2 entries.
            shortcut: Whether bottlenecks use residual connections.
        """
        x = self._run_cbs(f"{name}_cv1", x, weights["cv1_weight"], weights["cv1_bias"])
        chunks = x.chunk(2, dim=1)
        outputs = [chunks[0], chunks[1]]

        for i, (w1, b1, w2, b2) in enumerate(weights["bottlenecks"]):
            inp = outputs[-1]
            y = self._run_cbs(f"{name}_bn{i}_cv1", inp, w1, b1)
            y = self._run_cbs(f"{name}_bn{i}_cv2", y, w2, b2)
            if shortcut:
                y = y + inp
            outputs.append(y)

        x = torch.cat(outputs, dim=1)
        return self._run_cbs(f"{name}_cv2", x, weights["cv2_weight"], weights["cv2_bias"])

    def _run_sppf(self, name, x, weights):
        """Run SPPF block."""
        x = self._run_cbs(f"{name}_cv1", x, weights["cv1_weight"], weights["cv1_bias"])
        y1 = self._run_pool(f"{name}_mp1", x)
        y2 = self._run_pool(f"{name}_mp2", y1)
        y3 = self._run_pool(f"{name}_mp3", y2)
        x = torch.cat([x, y1, y2, y3], dim=1)
        return self._run_cbs(f"{name}_cv2", x, weights["cv2_weight"], weights["cv2_bias"])

    def _run_detect_branch(self, name, x, weights):
        """Run a DetectBranch (2x CBS 3x3 + 1x bare Conv1x1)."""
        x = self._run_cbs(f"{name}_cv1", x, weights["cv1_weight"], weights["cv1_bias"])
        x = self._run_cbs(f"{name}_cv2", x, weights["cv2_weight"], weights["cv2_bias"])
        x = self._run_conv(f"{name}_cv3", x, weights["cv3_weight"], weights["cv3_bias"])
        return x

    def load_weights(self, weights):
        """Load all model weights.

        Args:
            weights: Dictionary with keys for each section:
                'backbone': dict from YOLOv8nBackbone.load_weights format
                'neck': dict from YOLOv8nNeck.load_weights format
                'detect': dict from YOLOv8nDetect.load_weights format
        """
        self._weights = weights

    def forward(self, x):
        """Run the full YOLOv8n model.

        Args:
            x: Input tensor [1, 3, H, W] in bfloat16.

        Returns:
            Dictionary with raw predictions:
                'reg': [reg_p3, reg_p4, reg_p5]
                'cls': [cls_p3, cls_p4, cls_p5]
        """
        if not self._weights:
            raise RuntimeError("Call load_weights() before forward()")

        bb = self._weights.get("backbone", {})
        nk = self._weights.get("neck", {})
        dt = self._weights.get("detect", {})

        # Pad RGB (3ch) to 8 channels
        x = F.pad(x, (0, 0, 0, 0, 0, 5))

        # ---- BACKBONE ----
        x = self._run_cbs("bb_l0", x, bb["l0"]["weight"], bb["l0"]["bias"])
        x = self._run_cbs("bb_l1", x, bb["l1"]["weight"], bb["l1"]["bias"])
        x = self._run_c2f("bb_l2", x, bb["l2"])
        x = self._run_cbs("bb_l3", x, bb["l3"]["weight"], bb["l3"]["bias"])
        p3 = self._run_c2f("bb_l4", x, bb["l4"])
        x = self._run_cbs("bb_l5", p3, bb["l5"]["weight"], bb["l5"]["bias"])
        p4 = self._run_c2f("bb_l6", x, bb["l6"])
        x = self._run_cbs("bb_l7", p4, bb["l7"]["weight"], bb["l7"]["bias"])
        x = self._run_c2f("bb_l8", x, bb["l8"])
        p5 = self._run_sppf("bb_l9", x, bb["l9"])

        # ---- NECK (FPN up-path) ----
        x = self._run_upsample("nk_up1", p5)
        x = torch.cat([x, p4], dim=1)
        l12_out = self._run_c2f("nk_l12", x, nk["l12"], shortcut=False)

        x = self._run_upsample("nk_up2", l12_out)
        x = torch.cat([x, p3], dim=1)
        det_p3 = self._run_c2f("nk_l15", x, nk["l15"], shortcut=False)

        # ---- NECK (PAN down-path) ----
        x = self._run_cbs("nk_l16", det_p3, nk["l16"]["weight"], nk["l16"]["bias"])
        x = torch.cat([x, l12_out], dim=1)
        det_p4 = self._run_c2f("nk_l18", x, nk["l18"], shortcut=False)

        x = self._run_cbs("nk_l19", det_p4, nk["l19"]["weight"], nk["l19"]["bias"])
        x = torch.cat([x, p5], dim=1)
        det_p5 = self._run_c2f("nk_l21", x, nk["l21"], shortcut=False)

        # ---- DETECT HEAD ----
        reg3 = self._run_detect_branch("det_reg_p3", det_p3, dt["reg_p3"])
        cls3 = self._run_detect_branch("det_cls_p3", det_p3, dt["cls_p3"])

        reg4 = self._run_detect_branch("det_reg_p4", det_p4, dt["reg_p4"])
        cls4 = self._run_detect_branch("det_cls_p4", det_p4, dt["cls_p4"])

        reg5 = self._run_detect_branch("det_reg_p5", det_p5, dt["reg_p5"])
        cls5 = self._run_detect_branch("det_cls_p5", det_p5, dt["cls_p5"])

        return {
            "reg": [reg3, reg4, reg5],
            "cls": [cls3, cls4, cls5],
        }
