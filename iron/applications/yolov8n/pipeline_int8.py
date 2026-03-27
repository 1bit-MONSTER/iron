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
import time as _time

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


def _auto_columns_int8(in_channels, out_channels, kernel_size, width, stride=1):
    """Choose num_aie_columns for int8 conv2d to maximize parallelism.

    Int8 elements are 1 byte (vs 2 for bf16). Per-core output channels
    must be a multiple of 8. Tries largest column count first [4, 2, 1]
    to maximize core utilization, falling back to fewer columns when
    constraints aren't met.

    For k1: input depth=2 (MemTile forwarded), weight depth=1, output depth=2.
    For k3: input depth=3-4 (sliding window, phys_bufs=depth+1), OC streaming.
    """
    _L1 = 65536
    _OH = 1040
    _BD_WRAP_MAX = 64
    k_elems = kernel_size * kernel_size
    out_w = width // stride if stride > 1 else width

    # Try largest column count first for max parallelism
    for cols in [4, 2, 1]:
        oc_per_col = out_channels // cols if out_channels % cols == 0 else -1
        if oc_per_col < 8 or oc_per_col % 8 != 0:
            continue

        if kernel_size == 1:
            # k1: input depth=2, weight=1, output depth=2 (all 1 byte)
            input_bytes = 2 * in_channels * width
            avail = _L1 - _OH - input_bytes
            if avail <= 0:
                continue
            # Try full oc_per_col first, then OC streaming
            for try_oc in range(oc_per_col, 0, -8):
                if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                    continue
                wt_bytes = try_oc * in_channels
                out_bytes = 2 * try_oc * width
                if wt_bytes + out_bytes <= avail:
                    n_oc = oc_per_col // try_oc
                    if n_oc <= _BD_WRAP_MAX:
                        return cols
                    break
        else:
            # k3: sliding window input, OC streaming
            for try_depth in [4, 3]:
                phys_bufs = try_depth + 1
                input_bytes = phys_bufs * in_channels * width
                avail = _L1 - _OH - input_bytes
                if avail <= 0:
                    continue
                for try_oc in range(oc_per_col, 0, -8):
                    if oc_per_col % try_oc != 0 or try_oc % 8 != 0:
                        continue
                    wt_bytes = try_oc * in_channels * k_elems
                    out_bytes = 2 * try_oc * out_w
                    if wt_bytes + out_bytes <= avail:
                        n_oc = oc_per_col // try_oc
                        if n_oc <= _BD_WRAP_MAX:
                            return cols
                        break

    raise ValueError(
        f"No feasible int8 NPU mapping: IC={in_channels}, "
        f"OC={out_channels}, K={kernel_size}, W={width}, S={stride}"
    )


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
        self._weights_prepared = False
        self._layer_cache = {}  # buf_name -> {tiled_weights, in_act_scale, ...}
        self._prof = {}  # profiling: name -> total_seconds
        self._prof_n = {}  # profiling: name -> count

        super().__init__(context=context)

    def _next_kernel_id(self):
        kid = self._kernel_id_counter
        self._kernel_id_counter += 1
        return kid

    def _register_int8_conv(
        self,
        layer_name,
        in_ch,
        out_ch,
        h,
        w,
        ks,
        stride,
        shift,
        num_aie_columns=1,
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
            num_aie_columns=num_aie_columns,
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
            out_sz = sub_op.out_channels * sub_op.out_height * sub_op.out_width
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

    # -- Profiling helpers -----------------------------------------------------

    def _prof_add(self, name, elapsed):
        self._prof[name] = self._prof.get(name, 0.0) + elapsed
        self._prof_n[name] = self._prof_n.get(name, 0) + 1

    def reset_profile(self):
        self._prof.clear()
        self._prof_n.clear()

    def print_profile(self):
        total = sum(self._prof.values())
        if total == 0:
            print("No profiling data collected.")
            return
        print(f"\nForward pass profile ({total*1000:.0f}ms total):")
        for name in sorted(self._prof, key=lambda k: -self._prof[k]):
            ms = self._prof[name] * 1000
            n = self._prof_n[name]
            pct = ms / (total * 1000) * 100
            print(
                f"  {name:25s}: {ms:8.1f}ms ({pct:4.1f}%) "
                f"[{n:3d} calls, {ms/n:.2f}ms avg]"
            )

    # -- Weight pre-computation ------------------------------------------------

    def prepare_weights(self):
        """Pre-tile all weights and cache per-layer constants.

        Call after prepare_runtime(). Pre-tiles weight tensors so the
        forward pass skips weight tiling, output zero-fills, and reduces
        BO syncs from 8 to 5 per kernel call.
        """
        for dot_name in PRED_MAP:
            buf_name = _buf(dot_name)
            if buf_name not in self._pdi_map:
                continue

            entry = self._pdi_map[buf_name]
            sub_op = entry["sub_op"]

            w_int8, w_scale, bias = lookup_weight(self.int8_weights, dot_name)

            # Pre-tile weights once (saves ~50ms per forward)
            if sub_op.kernel_size == 3:
                tiled_w = weights_to_tiled_int8_k3(w_int8)
            else:
                tiled_w = weights_to_tiled_int8(w_int8)

            # Pre-compute per-layer constants
            pred = PRED_MAP[dot_name]
            in_act_scale = self.act_scales.get(pred, 1.0)
            if in_act_scale == 0:
                in_act_scale = 1.0
            shift = self._shifts[buf_name]
            dequant_scale = float((2**shift) * w_scale * in_act_scale)

            self._layer_cache[buf_name] = {
                "tiled_weights": tiled_w,
                "in_act_scale": in_act_scale,
                "dequant_scale": dequant_scale,
                "bias_view": bias.view(1, -1, 1, 1),
            }

        self._weights_prepared = True

    # -- Optimized kernel execution --------------------------------------------

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
            raise RuntimeError(f"Kernel {kernel_name} failed: {result}")
        for bo in bos:
            bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)

    def _run_kernel_fast(self, kernel_name, input_buf, weights_buf, output_buf):
        """Execute kernel with minimal BO syncs.

        Skips: output sync TO_DEVICE (write-only), input/weights sync
        FROM_DEVICE (read-only from host perspective).
        """
        context, xrt_kernel, insts_bo, insts_len = self.xrt_kernels[kernel_name]
        insts_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        in_bo = self.buffer_bos[input_buf]
        w_bo = self.buffer_bos[weights_buf]
        out_bo = self.buffer_bos[output_buf]
        in_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        w_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        opcode = 3
        run = xrt_kernel(opcode, insts_bo, insts_len, in_bo, w_bo, out_bo)
        result = run.wait()
        if result != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
            raise RuntimeError(f"Kernel {kernel_name} failed: {result}")
        out_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)

    # -- Fast-path CBS / conv methods ------------------------------------------

    def int8_cbs_fast(self, x_float, layer_name):
        """Fast CBS: pre-tiled weights, no output zero-fill, fewer syncs."""
        cache = self._layer_cache[layer_name]
        entry = self._pdi_map[layer_name]
        sub_op = entry["sub_op"]

        t0 = _time.perf_counter()
        x_int8 = torch.clamp(
            torch.round(x_float / cache["in_act_scale"]), -128, 127
        ).to(torch.int8)
        self._prof_add("quantize", _time.perf_counter() - t0)

        t0 = _time.perf_counter()
        input_tiled = nchw_to_tiled_int8(x_int8)
        self.write_buffer(f"{layer_name}_input", input_tiled)
        self.write_buffer(f"{layer_name}_weights", cache["tiled_weights"])
        self._prof_add("tile+write", _time.perf_counter() - t0)

        t0 = _time.perf_counter()
        self._run_kernel_fast(
            entry["kernel_name"],
            f"{layer_name}_input",
            f"{layer_name}_weights",
            f"{layer_name}_output",
        )
        self._prof_add("kernel", _time.perf_counter() - t0)

        t0 = _time.perf_counter()
        oh, ow = sub_op.out_height, sub_op.out_width
        total_output = sub_op.out_channels * oh * ow
        output_flat = self.read_buffer(
            f"{layer_name}_output", (total_output,), copy=True, dtype=np.int8
        )
        out_int8 = tiled_to_nchw_int8(output_flat, sub_op.out_channels, oh, ow)
        self._prof_add("read+untile", _time.perf_counter() - t0)

        t0 = _time.perf_counter()
        out_float = out_int8.float() * cache["dequant_scale"]
        out_float = out_float + cache["bias_view"]
        out_float = F.silu(out_float)
        self._prof_add("dequant+bias+silu", _time.perf_counter() - t0)

        return out_float

    def int8_conv_no_act_fast(self, x_float, layer_name):
        """Fast conv without activation: pre-tiled weights, fewer syncs."""
        cache = self._layer_cache[layer_name]
        entry = self._pdi_map[layer_name]
        sub_op = entry["sub_op"]

        t0 = _time.perf_counter()
        x_int8 = torch.clamp(
            torch.round(x_float / cache["in_act_scale"]), -128, 127
        ).to(torch.int8)
        self._prof_add("quantize", _time.perf_counter() - t0)

        t0 = _time.perf_counter()
        input_tiled = nchw_to_tiled_int8(x_int8)
        self.write_buffer(f"{layer_name}_input", input_tiled)
        self.write_buffer(f"{layer_name}_weights", cache["tiled_weights"])
        self._prof_add("tile+write", _time.perf_counter() - t0)

        t0 = _time.perf_counter()
        self._run_kernel_fast(
            entry["kernel_name"],
            f"{layer_name}_input",
            f"{layer_name}_weights",
            f"{layer_name}_output",
        )
        self._prof_add("kernel", _time.perf_counter() - t0)

        t0 = _time.perf_counter()
        oh, ow = sub_op.out_height, sub_op.out_width
        total_output = sub_op.out_channels * oh * ow
        output_flat = self.read_buffer(
            f"{layer_name}_output", (total_output,), copy=True, dtype=np.int8
        )
        out_int8 = tiled_to_nchw_int8(output_flat, sub_op.out_channels, oh, ow)
        self._prof_add("read+untile", _time.perf_counter() - t0)

        t0 = _time.perf_counter()
        out_float = out_int8.float() * cache["dequant_scale"]
        out_float = out_float + cache["bias_view"]
        self._prof_add("dequant+bias", _time.perf_counter() - t0)

        return out_float

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
        self.write_buffer(f"{layer_name}_output", np.zeros(total_output, dtype=np.int8))

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
        x_int8 = torch.clamp(torch.round(x_float / in_act_scale), -128, 127).to(
            torch.int8
        )

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
        x_int8 = torch.clamp(torch.round(x_float / in_act_scale), -128, 127).to(
            torch.int8
        )

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


# -- Predecessor map for activation scale lookup ----------------------------

# Maps each layer name to the layer whose output feeds into it.
# Used to look up the input activation scale for quantizing the input.
PRED_MAP = {
    "l0": "input",
    "l1": "l0",
    "l2.cv1": "l1",
    "l2.bn0.cv1": "l2.cv1",
    "l2.bn0.cv2": "l2.bn0.cv1",
    "l2.cv2": "l2.cv1",
    "l3": "l2.cv2",
    "l4.cv1": "l3",
    "l4.bn0.cv1": "l4.cv1",
    "l4.bn0.cv2": "l4.bn0.cv1",
    "l4.bn1.cv1": "l4.bn0.cv2",
    "l4.bn1.cv2": "l4.bn1.cv1",
    "l4.cv2": "l4.cv1",
    "l5": "l4.cv2",
    "l6.cv1": "l5",
    "l6.bn0.cv1": "l6.cv1",
    "l6.bn0.cv2": "l6.bn0.cv1",
    "l6.bn1.cv1": "l6.bn0.cv2",
    "l6.bn1.cv2": "l6.bn1.cv1",
    "l6.cv2": "l6.cv1",
    "l7": "l6.cv2",
    "l8.cv1": "l7",
    "l8.bn0.cv1": "l8.cv1",
    "l8.bn0.cv2": "l8.bn0.cv1",
    "l8.cv2": "l8.cv1",
    "l9.cv1": "l8.cv2",
    "l9.cv2": "l9.cv1",
    # Neck
    "l12.cv1": "l9.cv2",
    "l12.bn0.cv1": "l12.cv1",
    "l12.bn0.cv2": "l12.bn0.cv1",
    "l12.cv2": "l12.cv1",
    "l15.cv1": "l12.cv2",
    "l15.bn0.cv1": "l15.cv1",
    "l15.bn0.cv2": "l15.bn0.cv1",
    "l15.cv2": "l15.cv1",
    "l16": "l15.cv2",
    "l18.cv1": "l16",
    "l18.bn0.cv1": "l18.cv1",
    "l18.bn0.cv2": "l18.bn0.cv1",
    "l18.cv2": "l18.cv1",
    "l19": "l18.cv2",
    "l21.cv1": "l19",
    "l21.bn0.cv1": "l21.cv1",
    "l21.bn0.cv2": "l21.bn0.cv1",
    "l21.cv2": "l21.cv1",
    # Detect head
    "det.reg_p3.cv1": "l15.cv2",
    "det.reg_p3.cv2": "det.reg_p3.cv1",
    "det.reg_p3.cv3": "det.reg_p3.cv2",
    "det.cls_p3.cv1": "l15.cv2",
    "det.cls_p3.cv2": "det.cls_p3.cv1",
    "det.cls_p3.cv3": "det.cls_p3.cv2",
    "det.reg_p4.cv1": "l18.cv2",
    "det.reg_p4.cv2": "det.reg_p4.cv1",
    "det.reg_p4.cv3": "det.reg_p4.cv2",
    "det.cls_p4.cv1": "l18.cv2",
    "det.cls_p4.cv2": "det.cls_p4.cv1",
    "det.cls_p4.cv3": "det.cls_p4.cv2",
    "det.reg_p5.cv1": "l21.cv2",
    "det.reg_p5.cv2": "det.reg_p5.cv1",
    "det.reg_p5.cv3": "det.reg_p5.cv2",
    "det.cls_p5.cv1": "l21.cv2",
    "det.cls_p5.cv2": "det.cls_p5.cv1",
    "det.cls_p5.cv3": "det.cls_p5.cv2",
}


def _buf(name):
    """Convert dot-notation layer name to buffer-safe underscore name."""
    return name.replace(".", "_")


def lookup_weight(int8_weights, layer_name):
    """Look up int8 weight, scale, and float bias for a layer.

    Args:
        int8_weights: Weight dict from Int8Quantizer.quantize_yolov8n_weights().
        layer_name: Layer name in calibration convention (e.g., "l2.cv1").

    Returns:
        (weight_int8, weight_scale, bias_float) tuple.
    """
    wts = int8_weights

    # Direct CBS layers
    cbs_map = {
        "l0": ("backbone", "l0"),
        "l1": ("backbone", "l1"),
        "l3": ("backbone", "l3"),
        "l5": ("backbone", "l5"),
        "l7": ("backbone", "l7"),
        "l16": ("neck", "l16"),
        "l19": ("neck", "l19"),
    }
    if layer_name in cbs_map:
        section, key = cbs_map[layer_name]
        d = wts[section][key]
        return d["weight"], d["weight_scale"], d["bias"]

    # SPPF
    if layer_name == "l9.cv1":
        d = wts["backbone"]["l9"]
        return d["cv1_weight"], d["cv1_scale"], d["cv1_bias"]
    if layer_name == "l9.cv2":
        d = wts["backbone"]["l9"]
        return d["cv2_weight"], d["cv2_scale"], d["cv2_bias"]

    # C2f layers
    c2f_layers = {
        "l2": ("backbone", "l2"),
        "l4": ("backbone", "l4"),
        "l6": ("backbone", "l6"),
        "l8": ("backbone", "l8"),
        "l12": ("neck", "l12"),
        "l15": ("neck", "l15"),
        "l18": ("neck", "l18"),
        "l21": ("neck", "l21"),
    }
    for c2f_prefix, (section, key) in c2f_layers.items():
        d = wts[section][key]
        if layer_name == f"{c2f_prefix}.cv1":
            return d["cv1_weight"], d["cv1_scale"], d["cv1_bias"]
        if layer_name == f"{c2f_prefix}.cv2":
            return d["cv2_weight"], d["cv2_scale"], d["cv2_bias"]
        for i, bn_data in enumerate(d["bottlenecks"]):
            w1, b1, w2, b2, s1, s2 = bn_data
            if layer_name == f"{c2f_prefix}.bn{i}.cv1":
                return w1, s1, b1
            if layer_name == f"{c2f_prefix}.bn{i}.cv2":
                return w2, s2, b2

    # Detect head
    for branch in ["reg_p3", "reg_p4", "reg_p5", "cls_p3", "cls_p4", "cls_p5"]:
        d = wts["detect"][branch]
        if layer_name == f"det.{branch}.cv1":
            return d["cv1_weight"], d["cv1_scale"], d["cv1_bias"]
        if layer_name == f"det.{branch}.cv2":
            return d["cv2_weight"], d["cv2_scale"], d["cv2_bias"]
        if layer_name == f"det.{branch}.cv3":
            return d["cv3_weight"], d["cv3_scale"], d["cv3_bias"]

    raise KeyError(f"Unknown layer: {layer_name}")


def compute_all_shifts(int8_weights, act_scales):
    """Compute per-layer right-shift values from calibration data.

    Args:
        int8_weights: Weight dict from quantizer.
        act_scales: Dict of layer_name -> float activation scale.

    Returns:
        Dict of layer_name -> shift (int).
    """
    shifts = {}
    for layer_name in PRED_MAP:
        w_int8, w_scale, _ = lookup_weight(int8_weights, layer_name)
        pred = PRED_MAP[layer_name]
        in_act_scale = act_scales.get(pred, 1.0)
        out_act_scale = act_scales.get(layer_name, 1.0)
        shift = compute_layer_shift(w_scale, in_act_scale, out_act_scale)
        shifts[layer_name] = shift
    return shifts


# -- 2-XCLBIN Split Pipelines ----------------------------------------------


class Int8BackboneNeckPipeline(Int8ConvPipeline):
    """Multi-PDI pipeline for int8 backbone (L0-L9) + neck (L10-L21).

    45 unique PDIs across 2 xclbin groups (32 + 13), 1 hw_context.
    Convolutions run on NPU in int8. MaxPool, upsample, concat,
    dequantization, bias, and SiLU run on CPU in float.
    """

    def __init__(self, shifts, act_scales, int8_weights, context=None):
        self.shifts = shifts
        self.act_scales = act_scales
        self.int8_weights = int8_weights
        super().__init__(context=context)

    def _register_all_layers(self):
        s = self.shifts

        def reg(name, ic, oc, h, w, ks, stride):
            cols = _auto_columns_int8(ic, oc, ks, w, stride)
            self._register_int8_conv(
                _buf(name),
                ic,
                oc,
                h,
                w,
                ks,
                stride,
                s[name],
                num_aie_columns=cols,
            )

        # ---- BACKBONE ----
        reg("l0", 8, 16, 640, 640, 3, 2)
        reg("l1", 16, 32, 320, 320, 3, 2)

        # L2 C2f (32->32, 160x160, n=1)
        reg("l2.cv1", 32, 32, 160, 160, 1, 1)
        reg("l2.bn0.cv1", 16, 16, 160, 160, 3, 1)
        reg("l2.bn0.cv2", 16, 16, 160, 160, 3, 1)
        reg("l2.cv2", 48, 32, 160, 160, 1, 1)

        reg("l3", 32, 64, 160, 160, 3, 2)

        # L4 C2f (64->64, 80x80, n=2)
        reg("l4.cv1", 64, 64, 80, 80, 1, 1)
        reg("l4.bn0.cv1", 32, 32, 80, 80, 3, 1)
        reg("l4.bn0.cv2", 32, 32, 80, 80, 3, 1)
        reg("l4.bn1.cv1", 32, 32, 80, 80, 3, 1)
        reg("l4.bn1.cv2", 32, 32, 80, 80, 3, 1)
        reg("l4.cv2", 128, 64, 80, 80, 1, 1)

        reg("l5", 64, 128, 80, 80, 3, 2)

        # L6 C2f (128->128, 40x40, n=2)
        reg("l6.cv1", 128, 128, 40, 40, 1, 1)
        reg("l6.bn0.cv1", 64, 64, 40, 40, 3, 1)
        reg("l6.bn0.cv2", 64, 64, 40, 40, 3, 1)
        reg("l6.bn1.cv1", 64, 64, 40, 40, 3, 1)
        reg("l6.bn1.cv2", 64, 64, 40, 40, 3, 1)
        reg("l6.cv2", 256, 128, 40, 40, 1, 1)

        reg("l7", 128, 256, 40, 40, 3, 2)

        # L8 C2f (256->256, 20x20, n=1)
        reg("l8.cv1", 256, 256, 20, 20, 1, 1)
        reg("l8.bn0.cv1", 128, 128, 20, 20, 3, 1)
        reg("l8.bn0.cv2", 128, 128, 20, 20, 3, 1)
        reg("l8.cv2", 384, 256, 20, 20, 1, 1)

        # L9 SPPF (convs only; maxpool on CPU)
        reg("l9.cv1", 256, 128, 20, 20, 1, 1)
        reg("l9.cv2", 512, 256, 20, 20, 1, 1)

        # ---- NECK ----
        # L12 C2f (384->128, 40x40, n=1)
        reg("l12.cv1", 384, 128, 40, 40, 1, 1)
        reg("l12.bn0.cv1", 64, 64, 40, 40, 3, 1)
        reg("l12.bn0.cv2", 64, 64, 40, 40, 3, 1)
        reg("l12.cv2", 192, 128, 40, 40, 1, 1)

        # L15 C2f (192->64, 80x80, n=1)
        reg("l15.cv1", 192, 64, 80, 80, 1, 1)
        reg("l15.bn0.cv1", 32, 32, 80, 80, 3, 1)
        reg("l15.bn0.cv2", 32, 32, 80, 80, 3, 1)
        reg("l15.cv2", 96, 64, 80, 80, 1, 1)

        # L16 CBS (64->64, 80->40, k3s2)
        reg("l16", 64, 64, 80, 80, 3, 2)

        # L18 C2f (192->128, 40x40, n=1)
        reg("l18.cv1", 192, 128, 40, 40, 1, 1)
        reg("l18.bn0.cv1", 64, 64, 40, 40, 3, 1)
        reg("l18.bn0.cv2", 64, 64, 40, 40, 3, 1)
        reg("l18.cv2", 192, 128, 40, 40, 1, 1)

        # L19 CBS (128->128, 40->20, k3s2)
        reg("l19", 128, 128, 40, 40, 3, 2)

        # L21 C2f (384->256, 20x20, n=1)
        reg("l21.cv1", 384, 256, 20, 20, 1, 1)
        reg("l21.bn0.cv1", 128, 128, 20, 20, 3, 1)
        reg("l21.bn0.cv2", 128, 128, 20, 20, 3, 1)
        reg("l21.cv2", 384, 256, 20, 20, 1, 1)

    def _cbs(self, x, name):
        """CBS: quantize -> int8 conv NPU -> dequant -> bias -> SiLU."""
        if self._weights_prepared:
            return self.int8_cbs_fast(x, _buf(name))
        w, ws, b = lookup_weight(self.int8_weights, name)
        pred = PRED_MAP[name]
        in_scale = self.act_scales.get(pred, 1.0)
        return self.int8_cbs(x, _buf(name), w, ws, b, in_scale)

    def _c2f(self, x, prefix, n_bn, shortcut=True):
        """Run a C2f block."""
        x = self._cbs(x, f"{prefix}.cv1")
        chunks = x.chunk(2, dim=1)
        outputs = [chunks[0], chunks[1]]
        for i in range(n_bn):
            inp = outputs[-1]
            y = self._cbs(inp, f"{prefix}.bn{i}.cv1")
            y = self._cbs(y, f"{prefix}.bn{i}.cv2")
            if shortcut:
                y = y + inp
            outputs.append(y)
        x = torch.cat(outputs, dim=1)
        return self._cbs(x, f"{prefix}.cv2")

    def forward(self, x):
        """Run backbone + neck.

        Args:
            x: Input [1, 3, 640, 640] float tensor.

        Returns:
            (det_p3, det_p4, det_p5) float feature maps.
        """
        x = x.float()
        x = F.pad(x, (0, 0, 0, 0, 0, 5))  # 3ch -> 8ch

        # ---- BACKBONE ----
        x = self._cbs(x, "l0")
        print(f"  L0:  {x.shape}")
        x = self._cbs(x, "l1")
        print(f"  L1:  {x.shape}")
        x = self._c2f(x, "l2", 1)
        print(f"  L2:  {x.shape}")
        x = self._cbs(x, "l3")
        print(f"  L3:  {x.shape}")
        p3 = self._c2f(x, "l4", 2)
        print(f"  L4:  {p3.shape}  [P3]")
        x = self._cbs(p3, "l5")
        print(f"  L5:  {x.shape}")
        p4 = self._c2f(x, "l6", 2)
        print(f"  L6:  {p4.shape}  [P4]")
        x = self._cbs(p4, "l7")
        print(f"  L7:  {x.shape}")
        x = self._c2f(x, "l8", 1)
        print(f"  L8:  {x.shape}")

        # SPPF: convs on NPU, maxpool on CPU
        x = self._cbs(x, "l9.cv1")
        y1 = F.max_pool2d(x, 5, stride=1, padding=2)
        y2 = F.max_pool2d(y1, 5, stride=1, padding=2)
        y3 = F.max_pool2d(y2, 5, stride=1, padding=2)
        x = torch.cat([x, y1, y2, y3], dim=1)
        p5 = self._cbs(x, "l9.cv2")
        print(f"  L9:  {p5.shape}  [P5]")

        # ---- NECK (FPN up-path) ----
        x = F.interpolate(p5, scale_factor=2, mode="nearest")
        x = torch.cat([x, p4], dim=1)
        l12_out = self._c2f(x, "l12", 1, shortcut=False)
        print(f"  L12: {l12_out.shape}")

        x = F.interpolate(l12_out, scale_factor=2, mode="nearest")
        x = torch.cat([x, p3], dim=1)
        det_p3 = self._c2f(x, "l15", 1, shortcut=False)
        print(f"  L15: {det_p3.shape}  [det_p3]")

        # ---- NECK (PAN down-path) ----
        x = self._cbs(det_p3, "l16")
        print(f"  L16: {x.shape}")
        x = torch.cat([x, l12_out], dim=1)
        det_p4 = self._c2f(x, "l18", 1, shortcut=False)
        print(f"  L18: {det_p4.shape}  [det_p4]")

        x = self._cbs(det_p4, "l19")
        print(f"  L19: {x.shape}")
        x = torch.cat([x, p5], dim=1)
        det_p5 = self._c2f(x, "l21", 1, shortcut=False)
        print(f"  L21: {det_p5.shape}  [det_p5]")

        return det_p3, det_p4, det_p5


class Int8DetectHeadPipeline(Int8ConvPipeline):
    """Multi-PDI pipeline for int8 detect head (6 branches).

    18 PDIs in one xclbin group, 1 hw_context.
    CBS layers (cv1, cv2) use int8 conv + dequant + bias + SiLU.
    Bare conv layers (cv3) use int8 conv + dequant + bias (no activation).
    """

    def __init__(self, shifts, act_scales, int8_weights, context=None):
        self.shifts = shifts
        self.act_scales = act_scales
        self.int8_weights = int8_weights
        super().__init__(context=context)

    def _register_all_layers(self):
        s = self.shifts

        def reg(name, ic, oc, h, w, ks, stride):
            cols = _auto_columns_int8(ic, oc, ks, w, stride)
            self._register_int8_conv(
                _buf(name),
                ic,
                oc,
                h,
                w,
                ks,
                stride,
                s[name],
                num_aie_columns=cols,
            )

        for branch in ["reg_p3", "cls_p3"]:
            c_mid = 64 if branch.startswith("reg") else 80
            c_out = 64 if branch.startswith("reg") else 80
            reg(f"det.{branch}.cv1", 64, c_mid, 80, 80, 3, 1)
            reg(f"det.{branch}.cv2", c_mid, c_mid, 80, 80, 3, 1)
            reg(f"det.{branch}.cv3", c_mid, c_out, 80, 80, 1, 1)

        for branch in ["reg_p4", "cls_p4"]:
            c_mid = 64 if branch.startswith("reg") else 80
            c_out = 64 if branch.startswith("reg") else 80
            reg(f"det.{branch}.cv1", 128, c_mid, 40, 40, 3, 1)
            reg(f"det.{branch}.cv2", c_mid, c_mid, 40, 40, 3, 1)
            reg(f"det.{branch}.cv3", c_mid, c_out, 40, 40, 1, 1)

        for branch in ["reg_p5", "cls_p5"]:
            c_mid = 64 if branch.startswith("reg") else 80
            c_out = 64 if branch.startswith("reg") else 80
            reg(f"det.{branch}.cv1", 256, c_mid, 20, 20, 3, 1)
            reg(f"det.{branch}.cv2", c_mid, c_mid, 20, 20, 3, 1)
            reg(f"det.{branch}.cv3", c_mid, c_out, 20, 20, 1, 1)

    def _detect_branch(self, x, branch_name):
        """Run a detect branch (2x CBS 3x3 + 1x Conv 1x1)."""
        if self._weights_prepared:
            for cv in ["cv1", "cv2"]:
                x = self.int8_cbs_fast(x, _buf(f"det.{branch_name}.{cv}"))
            return self.int8_conv_no_act_fast(x, _buf(f"det.{branch_name}.cv3"))
        for cv in ["cv1", "cv2"]:
            name = f"det.{branch_name}.{cv}"
            w, ws, b = lookup_weight(self.int8_weights, name)
            pred = PRED_MAP[name]
            in_scale = self.act_scales.get(pred, 1.0)
            x = self.int8_cbs(x, _buf(name), w, ws, b, in_scale)

        # cv3: bare conv (no activation)
        name = f"det.{branch_name}.cv3"
        w, ws, b = lookup_weight(self.int8_weights, name)
        pred = PRED_MAP[name]
        in_scale = self.act_scales.get(pred, 1.0)
        x = self.int8_conv_no_act(x, _buf(name), w, ws, b, in_scale)
        return x

    def forward(self, det_p3, det_p4, det_p5):
        """Run detect head on neck outputs.

        Args:
            det_p3: [1, 64, 80, 80] float from neck.
            det_p4: [1, 128, 40, 40] float from neck.
            det_p5: [1, 256, 20, 20] float from neck.

        Returns:
            dict with 'reg': [reg_p3, reg_p4, reg_p5],
                       'cls': [cls_p3, cls_p4, cls_p5]
        """
        reg_p3 = self._detect_branch(det_p3, "reg_p3")
        print(f"  reg_p3: {reg_p3.shape}")
        cls_p3 = self._detect_branch(det_p3, "cls_p3")
        print(f"  cls_p3: {cls_p3.shape}")

        reg_p4 = self._detect_branch(det_p4, "reg_p4")
        print(f"  reg_p4: {reg_p4.shape}")
        cls_p4 = self._detect_branch(det_p4, "cls_p4")
        print(f"  cls_p4: {cls_p4.shape}")

        reg_p5 = self._detect_branch(det_p5, "reg_p5")
        print(f"  reg_p5: {reg_p5.shape}")
        cls_p5 = self._detect_branch(det_p5, "cls_p5")
        print(f"  cls_p5: {cls_p5.shape}")

        return {
            "reg": [reg_p3, reg_p4, reg_p5],
            "cls": [cls_p3, cls_p4, cls_p5],
        }
