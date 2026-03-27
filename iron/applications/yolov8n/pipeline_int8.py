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
    _compute_k3_fused_streaming,
    _compute_k1_silu_streaming,
    nchw_to_tiled_int8,
    tiled_to_nchw_int8,
    weights_to_tiled_int8,
    weights_to_tiled_int8_k3,
)
from iron.applications.yolov8n.quantize import Int8Quantizer


def _auto_columns_int8(
    in_channels, out_channels, kernel_size, width, stride=1, fused=False
):
    """Choose num_aie_columns for int8 conv2d to maximize parallelism.

    Int8 elements are 1 byte (vs 2 for bf16). Per-core output channels
    must be a multiple of 8. Tries largest column count first [4, 2, 1]
    to maximize core utilization, falling back to fewer columns when
    constraints aren't met.

    For k1: input depth=2 (MemTile forwarded), weight depth=1, output depth=2.
    For k3: input depth=3-4 (sliding window, phys_bufs=depth+1), OC streaming.

    When fused=True, weight buffer includes 4 bytes of int32 bias per OC.
    """
    _L1 = 65536
    _OH = 1040
    _BD_WRAP_MAX = 64
    k_elems = kernel_size * kernel_size
    out_w = width // stride if stride > 1 else width
    bias_bytes_per_oc = 4 if fused else 0

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
                wt_bytes = try_oc * in_channels + try_oc * bias_bytes_per_oc
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
                    wt_bytes = (
                        try_oc * in_channels * k_elems + try_oc * bias_bytes_per_oc
                    )
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

    def __init__(self, context=None, preprocessor=None):
        self._pdi_map = {}  # layer_name -> {sub_op, xclbin, insts, kernel_name}
        self._layer_map = {}  # layer_name -> pdi_key (same as layer_name)
        self._kernel_id_counter = 0x901
        self._group_xclbins = []  # combined xclbin per group
        self._shifts = {}  # layer_name -> shift value
        self._weights_prepared = False
        self._weights_synced = False  # True after load_static_weights()
        self._layer_cache = {}  # buf_name -> {tiled_weights, in_act_scale, ...}
        self._preprocessor = preprocessor
        self._prof = {}  # profiling: name -> total_seconds
        self._prof_n = {}  # profiling: name -> count
        self._chains = {}  # chain_name -> {layers, bos, runlist}

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
        fused=False,
        shift1=None,
        shift2=None,
    ):
        """Register an int8 conv layer with its own PDI.

        Args:
            fused: If True, use fused conv+bias+SiLU kernel.
            shift1: Dequant shift (acc -> float). Required if fused.
            shift2: Requant shift (SiLU -> int8). Required if fused.
        """
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
            fused=fused,
            shift1=shift1,
            shift2=shift2,
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
            out_sz = sub_op.out_channels * sub_op.out_height * sub_op.out_width

            # Fused weight buffer includes packed int32 bias per OC chunk
            if sub_op.fused and sub_op.kernel_size == 3:
                n_oc_groups, oc_chunk = _compute_k3_fused_streaming(
                    sub_op.in_channels,
                    sub_op.out_channels,
                    sub_op.width,
                    sub_op.out_width,
                    sub_op.num_aie_columns,
                )
                wt_chunk = oc_chunk * sub_op.in_channels * 9 + oc_chunk * 4
                w_sz = n_oc_groups * wt_chunk * sub_op.num_aie_columns
            elif sub_op.fused and sub_op.kernel_size == 1:
                n_oc_groups, oc_chunk = _compute_k1_silu_streaming(
                    sub_op.in_channels,
                    sub_op.out_channels,
                    sub_op.width,
                    sub_op.num_aie_columns,
                )
                wt_chunk = oc_chunk * sub_op.in_channels + oc_chunk * 4
                w_sz = n_oc_groups * wt_chunk * sub_op.num_aie_columns
            elif sub_op.kernel_size == 3:
                w_sz = sub_op.out_channels * sub_op.in_channels * 9
            else:
                w_sz = sub_op.out_channels * sub_op.in_channels

            self.add_buffer(f"{lname}_input", in_sz, dtype=np.int8)
            # When a preprocessor is available and the layer is NOT fused,
            # register weight data as static — this gives each layer a
            # dedicated BO that is written once during prepare_runtime()
            # and never touched again during inference.
            # Fused layers have packed bias in the weight buffer, which
            # the preprocessor doesn't compute, so they use regular BOs.
            if self._preprocessor is not None and not getattr(sub_op, "fused", False):
                static_w = self._preprocessor.get_static_weight_data(lname)
                self.add_buffer(
                    f"{lname}_weights", w_sz, dtype=np.int8, static_data=static_w
                )
            else:
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

        Call after prepare_runtime(). When a preprocessor is available,
        uses pre-computed data directly (weight tiling already done).
        Otherwise, tiles weights inline.

        For fused layers, packs int32 bias after weights in the buffer
        so the NPU kernel handles bias+SiLU+requant entirely on-chip.
        """
        if self._preprocessor is not None:
            for dot_name in PRED_MAP:
                buf_name = _buf(dot_name)
                if buf_name not in self._pdi_map:
                    continue
                entry = self._pdi_map[buf_name]
                sub_op = entry["sub_op"]
                if getattr(sub_op, "fused", False):
                    # Fused layers need packed weights+bias — fall through
                    # to the inline packing path below.
                    w_int8, w_scale, bias = lookup_weight(self.int8_weights, dot_name)
                    pred = PRED_MAP[dot_name]
                    in_act_scale = self._preprocessor.act_scales.get(pred, 1.0)
                    if in_act_scale == 0:
                        in_act_scale = 1.0
                    tiled_w = self._pack_fused_weights(
                        sub_op, w_int8, w_scale, bias, in_act_scale
                    )
                    self._layer_cache[buf_name] = {
                        "tiled_weights": tiled_w,
                        "in_act_scale": in_act_scale,
                    }
                else:
                    self._layer_cache[buf_name] = self._preprocessor.get_layer_data(
                        buf_name
                    )
            self._weights_prepared = True
            return

        for dot_name in PRED_MAP:
            buf_name = _buf(dot_name)
            if buf_name not in self._pdi_map:
                continue

            entry = self._pdi_map[buf_name]
            sub_op = entry["sub_op"]

            w_int8, w_scale, bias = lookup_weight(self.int8_weights, dot_name)

            # Pre-compute per-layer constants
            pred = PRED_MAP[dot_name]
            in_act_scale = self.act_scales.get(pred, 1.0)
            if in_act_scale == 0:
                in_act_scale = 1.0
            shift = self._shifts[buf_name]
            dequant_scale = float((2**shift) * w_scale * in_act_scale)

            if sub_op.fused:
                # Pack weights + int32 bias for fused conv+bias+SiLU kernel
                tiled_w = self._pack_fused_weights(
                    sub_op, w_int8, w_scale, bias, in_act_scale
                )
                self._layer_cache[buf_name] = {
                    "tiled_weights": tiled_w,
                    "in_act_scale": in_act_scale,
                }
            else:
                # Non-fused: just tile weights
                if sub_op.kernel_size == 3:
                    tiled_w = weights_to_tiled_int8_k3(w_int8)
                else:
                    tiled_w = weights_to_tiled_int8(w_int8)

                self._layer_cache[buf_name] = {
                    "tiled_weights": tiled_w,
                    "in_act_scale": in_act_scale,
                    "dequant_scale": dequant_scale,
                    "bias_view": bias.view(1, -1, 1, 1),
                }

        self._weights_prepared = True

    def load_static_weights(self):
        """Sync all static weight BOs to device once.

        Call after prepare_runtime(). After this, weight BOs are never
        re-written or re-synced during inference, saving one write_buffer
        + sync per layer per forward pass.
        """
        if self._preprocessor is None:
            return
        for lname in self._layer_map:
            wbuf = f"{lname}_weights"
            if wbuf in self.buffer_static_data:
                self.buffer_bos[wbuf].sync(
                    pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE
                )
        self._weights_synced = True

    # -- Runlist chain infrastructure -------------------------------------------

    def setup_chain(self, chain_name, layer_names):
        """Set up a runlist chain with ping-pong activation BOs.

        Uses minimal BOs following production inference patterns:
        - 2 activation BOs (ping-pong: layer N reads A/writes B,
          layer N+1 reads B/writes A)
        - 1 weight BO per layer (pre-filled at setup time)

        All layers must be in the same xclbin group (same hw_context).
        The runlist executes all kernels in one NPU submission. Between
        kernels, activations flow through shared BOs on-device with no
        host involvement.

        Args:
            chain_name: Identifier for this chain.
            layer_names: Ordered list of buffer-safe layer names to chain.
        """
        assert self._weights_prepared, "Call prepare_weights() first"

        # Verify all layers are in the same xclbin group
        groups = set(self._pdi_map[ln]["group_idx"] for ln in layer_names)
        assert len(groups) == 1, f"Chain layers must be in same group: {groups}"

        device = self.context.device_manager.device
        page_sz = 4096

        def align(sz):
            return (sz + page_sz - 1) // page_sz * page_sz

        # Get hw_context from first layer's kernel
        first_kname = self._pdi_map[layer_names[0]]["kernel_name"]
        context = self.xrt_kernels[first_kname][0]

        # Compute max activation size for ping-pong BOs
        max_act_sz = 0
        for lname in layer_names:
            max_act_sz = max(
                max_act_sz,
                self.buffers[f"{lname}_input"],
                self.buffers[f"{lname}_output"],
            )

        # Allocate 2 ping-pong activation BOs (sized to max activation)
        act_bo_a = pyxrt.bo(device, align(max_act_sz), pyxrt.bo.host_only, 0x10000)
        act_bo_b = pyxrt.bo(device, align(max_act_sz), pyxrt.bo.host_only, 0x10000)

        # Allocate per-layer weight BOs, pre-fill and sync
        weight_bos = {}
        for lname in layer_names:
            w_sz = self.buffers[f"{lname}_weights"]
            w_bo = pyxrt.bo(device, align(w_sz), pyxrt.bo.host_only, 0x10000)
            cache = self._layer_cache[lname]
            w_data = cache["tiled_weights"]
            mv = w_bo.map()
            dst = np.frombuffer(mv, dtype=np.uint8, count=w_bo.size())
            src = w_data.ravel().view(np.uint8)
            np.copyto(dst[: src.size], src, casting="no")
            w_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
            weight_bos[lname] = w_bo

        # Pre-sync instruction BOs
        for lname in layer_names:
            kname = self._pdi_map[lname]["kernel_name"]
            _, _, insts_bo, _ = self.xrt_kernels[kname]
            insts_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)

        # Build runlist with ping-pong activation pattern
        runlist = pyxrt.runlist(context)
        for i, lname in enumerate(layer_names):
            kname = self._pdi_map[lname]["kernel_name"]
            _, xrt_kernel, insts_bo, insts_len = self.xrt_kernels[kname]

            # Ping-pong: even layers read A/write B, odd layers read B/write A
            if i % 2 == 0:
                in_bo, out_bo = act_bo_a, act_bo_b
            else:
                in_bo, out_bo = act_bo_b, act_bo_a

            run = pyxrt.run(xrt_kernel)
            run.set_arg(0, 3)  # opcode
            run.set_arg(1, insts_bo)
            run.set_arg(2, insts_len)
            run.set_arg(3, in_bo)
            run.set_arg(4, weight_bos[lname])
            run.set_arg(5, out_bo)
            runlist.add(run)

        # Determine which BO holds first input and last output
        n = len(layer_names)
        last_output_bo = act_bo_b if (n - 1) % 2 == 0 else act_bo_a

        self._chains[chain_name] = {
            "layers": layer_names,
            "act_bo_a": act_bo_a,
            "act_bo_b": act_bo_b,
            "weight_bos": weight_bos,
            "runlist": runlist,
            "first_input_bo": act_bo_a,  # always starts with A
            "last_output_bo": last_output_bo,
        }

    def run_chain(self, chain_name, x_int8):
        """Execute a chain via runlist: single NPU submission.

        Writes tiled int8 input to BO_A, executes the runlist (all kernels
        in one NPU submission with ping-pong activation flow), reads tiled
        output from the last layer's output BO.

        Args:
            chain_name: Chain identifier from setup_chain().
            x_int8: Int8 input tensor [1, C, H, W] (NCHW).

        Returns:
            Int8 output tensor [1, C_out, H_out, W_out] (NCHW).
        """
        chain = self._chains[chain_name]
        layers = chain["layers"]

        # Tile input and write to BO_A (first layer always reads from A)
        t0 = _time.perf_counter()
        input_tiled = nchw_to_tiled_int8(x_int8)
        in_bo = chain["first_input_bo"]
        mv = in_bo.map()
        dst = np.frombuffer(mv, dtype=np.uint8, count=in_bo.size())
        src = input_tiled.ravel().view(np.uint8)
        np.copyto(dst[: src.size], src, casting="no")
        in_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        self._prof_add("chain_tile+write", _time.perf_counter() - t0)

        # Execute runlist (single NPU submission, all kernels sequentially)
        t0 = _time.perf_counter()
        chain["runlist"].execute()
        chain["runlist"].wait()
        self._prof_add("chain_kernel", _time.perf_counter() - t0)

        # Read output from last layer's output BO
        last_lname = layers[-1]
        sub_op = self._pdi_map[last_lname]["sub_op"]
        oh, ow = sub_op.out_height, sub_op.out_width
        total_output = sub_op.out_channels * oh * ow

        t0 = _time.perf_counter()
        out_bo = chain["last_output_bo"]
        out_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)
        mv = out_bo.map()
        output_flat = np.frombuffer(mv, dtype=np.int8, count=total_output).copy()
        out_int8 = tiled_to_nchw_int8(output_flat, sub_op.out_channels, oh, ow)
        self._prof_add("chain_read+untile", _time.perf_counter() - t0)

        return out_int8

    def benchmark_chain(self, chain_name, x_int8, n_iter=20, warmup=5):
        """Benchmark a chain: measure runlist vs per-layer execution time.

        Args:
            chain_name: Chain identifier from setup_chain().
            x_int8: Int8 input tensor [1, C, H, W] (NCHW).
            n_iter: Number of timed iterations.
            warmup: Number of warmup iterations.

        Returns:
            Dict with timing statistics.
        """
        chain = self._chains[chain_name]
        layers = chain["layers"]

        # Pre-tile input once and write to BO_A
        input_tiled = nchw_to_tiled_int8(x_int8)
        in_bo = chain["first_input_bo"]
        mv = in_bo.map()
        dst = np.frombuffer(mv, dtype=np.uint8, count=in_bo.size())
        src = input_tiled.ravel().view(np.uint8)
        np.copyto(dst[: src.size], src, casting="no")
        in_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)

        # Warmup
        for _ in range(warmup):
            chain["runlist"].execute()
            chain["runlist"].wait()

        # Timed iterations (kernel execution only, no host I/O)
        times = []
        for _ in range(n_iter):
            t0 = _time.perf_counter()
            chain["runlist"].execute()
            chain["runlist"].wait()
            times.append(_time.perf_counter() - t0)

        times_ms = [t * 1000 for t in times]
        avg = sum(times_ms) / len(times_ms)
        mn = min(times_ms)
        mx = max(times_ms)

        # Per-layer individual execution for comparison (same BOs, same data)
        per_layer_times = []
        for _ in range(n_iter):
            # Re-write input for fair comparison
            in_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
            total = 0.0
            for i, lname in enumerate(layers):
                kname = self._pdi_map[lname]["kernel_name"]
                _, xrt_kernel, insts_bo, insts_len = self.xrt_kernels[kname]

                # Use same ping-pong pattern as the runlist
                if i % 2 == 0:
                    in_b, out_b = chain["act_bo_a"], chain["act_bo_b"]
                else:
                    in_b, out_b = chain["act_bo_b"], chain["act_bo_a"]
                w_b = chain["weight_bos"][lname]

                insts_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
                in_b.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
                t0 = _time.perf_counter()
                r = xrt_kernel(3, insts_bo, insts_len, in_b, w_b, out_b)
                r.wait()
                total += _time.perf_counter() - t0
                out_b.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)
            per_layer_times.append(total * 1000)

        per_layer_avg = sum(per_layer_times) / len(per_layer_times)

        return {
            "chain": chain_name,
            "n_layers": len(layers),
            "runlist_avg_ms": avg,
            "runlist_min_ms": mn,
            "runlist_max_ms": mx,
            "per_layer_avg_ms": per_layer_avg,
            "speedup": per_layer_avg / avg if avg > 0 else 0,
        }

    def _pack_fused_weights(self, sub_op, w_int8, w_scale, bias_float, in_act_scale):
        """Pack tiled weights + int32 bias for fused conv+bias+SiLU kernel.

        Bias is pre-scaled to the accumulator domain:
            bias_int32 = round(bias_float / (in_act_scale * w_scale))

        Layout per OC chunk per column:
            [weights: oc_chunk * IC * K*K bytes] [bias: oc_chunk * 4 bytes]
        """
        combined_scale = float(in_act_scale * w_scale)
        if combined_scale == 0:
            combined_scale = 1.0
        bias_int32 = np.round(bias_float.numpy() / combined_scale).astype(np.int32)

        if sub_op.kernel_size == 3:
            n_oc_groups, oc_chunk = _compute_k3_fused_streaming(
                sub_op.in_channels,
                sub_op.out_channels,
                sub_op.width,
                sub_op.out_width,
                sub_op.num_aie_columns,
            )
            weight_tiled = weights_to_tiled_int8_k3(w_int8)
            wt_per_chunk = oc_chunk * sub_op.in_channels * 9
        else:
            n_oc_groups, oc_chunk = _compute_k1_silu_streaming(
                sub_op.in_channels,
                sub_op.out_channels,
                sub_op.width,
                sub_op.num_aie_columns,
            )
            weight_tiled = weights_to_tiled_int8(w_int8)
            wt_per_chunk = oc_chunk * sub_op.in_channels

        oc_per_col = sub_op.out_channels // sub_op.num_aie_columns
        chunks = []
        for col in range(sub_op.num_aie_columns):
            col_wt_base = (
                col
                * oc_per_col
                * (sub_op.in_channels * (9 if sub_op.kernel_size == 3 else 1))
            )
            col_bias_base = col * oc_per_col
            for g in range(n_oc_groups):
                w_start = col_wt_base + g * wt_per_chunk
                w_chunk = weight_tiled[w_start : w_start + wt_per_chunk]
                b_start = col_bias_base + g * oc_chunk
                b_chunk = bias_int32[b_start : b_start + oc_chunk]
                b_bytes = b_chunk.view(np.int8)
                chunks.append(np.concatenate([w_chunk, b_bytes]))

        return np.concatenate(chunks)

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
        If static weights are loaded, also skips weight sync TO_DEVICE.
        """
        context, xrt_kernel, insts_bo, insts_len = self.xrt_kernels[kernel_name]
        insts_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        in_bo = self.buffer_bos[input_buf]
        w_bo = self.buffer_bos[weights_buf]
        out_bo = self.buffer_bos[output_buf]
        in_bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        if not self._weights_synced:
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
        if not self._weights_synced:
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

    def int8_cbs_fused_fast(self, x, layer_name):
        """Fused CBS: input -> NPU conv+bias+SiLU -> int8 output.

        The fused kernel handles bias addition, SiLU activation, and
        requantization entirely on-chip. No Python post-processing needed.

        Args:
            x: Input tensor, int8 (skip quantize) or float (quantize first).
            layer_name: Pipeline layer identifier.

        Returns:
            Int8 output tensor [1, C_out, H_out, W_out].
        """
        cache = self._layer_cache[layer_name]
        entry = self._pdi_map[layer_name]
        sub_op = entry["sub_op"]

        t0 = _time.perf_counter()
        if x.dtype == torch.int8:
            x_int8 = x
        else:
            x_int8 = torch.clamp(
                torch.round(x.float() / cache["in_act_scale"]), -128, 127
            ).to(torch.int8)
        self._prof_add("quantize", _time.perf_counter() - t0)

        t0 = _time.perf_counter()
        input_tiled = nchw_to_tiled_int8(x_int8)
        self.write_buffer(f"{layer_name}_input", input_tiled)
        if not self._weights_synced:
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

        # No dequant/bias/SiLU — kernel handles everything!
        return out_int8

    def int8_conv_no_act_fast(self, x, layer_name):
        """Fast conv without activation: pre-tiled weights, fewer syncs."""
        cache = self._layer_cache[layer_name]
        entry = self._pdi_map[layer_name]
        sub_op = entry["sub_op"]

        t0 = _time.perf_counter()
        if x.dtype == torch.int8:
            x_int8 = x
        else:
            x_int8 = torch.clamp(
                torch.round(x.float() / cache["in_act_scale"]), -128, 127
            ).to(torch.int8)
        self._prof_add("quantize", _time.perf_counter() - t0)

        t0 = _time.perf_counter()
        input_tiled = nchw_to_tiled_int8(x_int8)
        self.write_buffer(f"{layer_name}_input", input_tiled)
        if not self._weights_synced:
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


def compute_fused_shifts(w_scale, in_act_scale, out_act_scale):
    """Compute shift1/shift2 for fused conv+bias+SiLU kernel.

    The fused kernel pipeline:
      1. MAC: acc = sum(x_int8 * w_int8) -> int32
      2. Add int32 bias (pre-scaled to accumulator domain)
      3. Dequant: float_val = acc * 2^(-shift1)
      4. SiLU(float_val)
      5. Requant: int8 = clamp(round(silu * 2^shift2), -128, 127)

    shift1 maps the accumulator to actual float values:
        shift1 = round(log2(1 / (in_act_scale * w_scale)))

    shift2 maps the SiLU output to int8 at the output activation scale:
        shift2 = round(log2(1 / out_act_scale))

    Args:
        w_scale: Per-tensor weight scale.
        in_act_scale: Input activation scale.
        out_act_scale: Output activation scale (post-SiLU, from calibration).

    Returns:
        (shift1, shift2) tuple, each clamped to [1, 31].
    """
    combined = w_scale * in_act_scale
    if combined == 0:
        shift1 = 10
    else:
        shift1 = round(math.log2(max(1.0 / combined, 1.0)))
    shift1 = max(1, min(31, shift1))

    if out_act_scale == 0:
        shift2 = 10
    else:
        shift2 = round(math.log2(max(1.0 / out_act_scale, 1.0)))
    shift2 = max(1, min(31, shift2))

    return shift1, shift2


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


def compute_all_shifts(int8_weights, act_scales, fused=True):
    """Compute per-layer shift values from calibration data.

    When fused=True, returns (shift1, shift2) tuples for layers with
    activation (CBS). Non-activation layers (detect cv3) get single shifts.

    Args:
        int8_weights: Weight dict from quantizer.
        act_scales: Dict of layer_name -> float activation scale.
        fused: If True, compute fused (shift1, shift2) for activation layers.

    Returns:
        Dict of layer_name -> shift (int) or (shift1, shift2) tuple.
    """
    # Detect cv3 layers (bare conv, no activation) — always use single shift
    _no_act_layers = {
        name for name in PRED_MAP if name.endswith(".cv3")
    }

    shifts = {}
    for layer_name in PRED_MAP:
        w_int8, w_scale, _ = lookup_weight(int8_weights, layer_name)
        pred = PRED_MAP[layer_name]
        in_act_scale = act_scales.get(pred, 1.0)
        out_act_scale = act_scales.get(layer_name, 1.0)

        if fused and layer_name not in _no_act_layers:
            shifts[layer_name] = compute_fused_shifts(
                w_scale, in_act_scale, out_act_scale
            )
        else:
            shifts[layer_name] = compute_layer_shift(
                w_scale, in_act_scale, out_act_scale
            )
    return shifts


# -- 2-XCLBIN Split Pipelines ----------------------------------------------


class Int8BackboneNeckPipeline(Int8ConvPipeline):
    """Multi-PDI pipeline for int8 backbone (L0-L9) + neck (L10-L21).

    45 unique PDIs across 2 xclbin groups (32 + 13), 1 hw_context.
    Convolutions run on NPU in int8. MaxPool, upsample, concat,
    dequantization, bias, and SiLU run on CPU in float.
    """

    def __init__(
        self, shifts, act_scales, int8_weights, context=None, preprocessor=None
    ):
        self.shifts = shifts
        self.act_scales = act_scales
        self.int8_weights = int8_weights
        super().__init__(context=context, preprocessor=preprocessor)

    def _fused_shifts(self, name):
        """Compute shift1/shift2 for a fused CBS layer."""
        _, w_scale, _ = lookup_weight(self.int8_weights, name)
        pred = PRED_MAP[name]
        in_act_scale = self.act_scales.get(pred, 1.0)
        if in_act_scale == 0:
            in_act_scale = 1.0
        out_act_scale = self.act_scales.get(name, 1.0)
        if out_act_scale == 0:
            out_act_scale = 1.0
        return compute_fused_shifts(w_scale, in_act_scale, out_act_scale)

    def _register_all_layers(self):
        s = self.shifts

        def reg(name, ic, oc, h, w, ks, stride, fused=False):
            cols = _auto_columns_int8(ic, oc, ks, w, stride, fused=fused)
            shift1, shift2 = None, None
            if fused:
                shift1, shift2 = self._fused_shifts(name)
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
                fused=fused,
                shift1=shift1,
                shift2=shift2,
            )

        # All backbone+neck layers are CBS — use fused conv+bias+SiLU
        _F = True

        # ---- BACKBONE ----
        reg("l0", 8, 16, 640, 640, 3, 2, fused=_F)
        reg("l1", 16, 32, 320, 320, 3, 2, fused=_F)

        # L2 C2f (32->32, 160x160, n=1)
        reg("l2.cv1", 32, 32, 160, 160, 1, 1, fused=_F)
        reg("l2.bn0.cv1", 16, 16, 160, 160, 3, 1, fused=_F)
        reg("l2.bn0.cv2", 16, 16, 160, 160, 3, 1, fused=_F)
        reg("l2.cv2", 48, 32, 160, 160, 1, 1, fused=_F)

        reg("l3", 32, 64, 160, 160, 3, 2, fused=_F)

        # L4 C2f (64->64, 80x80, n=2)
        reg("l4.cv1", 64, 64, 80, 80, 1, 1, fused=_F)
        reg("l4.bn0.cv1", 32, 32, 80, 80, 3, 1, fused=_F)
        reg("l4.bn0.cv2", 32, 32, 80, 80, 3, 1, fused=_F)
        reg("l4.bn1.cv1", 32, 32, 80, 80, 3, 1, fused=_F)
        reg("l4.bn1.cv2", 32, 32, 80, 80, 3, 1, fused=_F)
        reg("l4.cv2", 128, 64, 80, 80, 1, 1, fused=_F)

        reg("l5", 64, 128, 80, 80, 3, 2, fused=_F)

        # L6 C2f (128->128, 40x40, n=2)
        reg("l6.cv1", 128, 128, 40, 40, 1, 1, fused=_F)
        reg("l6.bn0.cv1", 64, 64, 40, 40, 3, 1, fused=_F)
        reg("l6.bn0.cv2", 64, 64, 40, 40, 3, 1, fused=_F)
        reg("l6.bn1.cv1", 64, 64, 40, 40, 3, 1, fused=_F)
        reg("l6.bn1.cv2", 64, 64, 40, 40, 3, 1, fused=_F)
        reg("l6.cv2", 256, 128, 40, 40, 1, 1, fused=_F)

        reg("l7", 128, 256, 40, 40, 3, 2, fused=_F)

        # L8 C2f (256->256, 20x20, n=1)
        reg("l8.cv1", 256, 256, 20, 20, 1, 1, fused=_F)
        reg("l8.bn0.cv1", 128, 128, 20, 20, 3, 1, fused=_F)
        reg("l8.bn0.cv2", 128, 128, 20, 20, 3, 1, fused=_F)
        reg("l8.cv2", 384, 256, 20, 20, 1, 1, fused=_F)

        # L9 SPPF (convs only; maxpool on CPU)
        reg("l9.cv1", 256, 128, 20, 20, 1, 1, fused=_F)
        reg("l9.cv2", 512, 256, 20, 20, 1, 1, fused=_F)

        # ---- NECK ----
        # L12 C2f (384->128, 40x40, n=1)
        reg("l12.cv1", 384, 128, 40, 40, 1, 1, fused=_F)
        reg("l12.bn0.cv1", 64, 64, 40, 40, 3, 1, fused=_F)
        reg("l12.bn0.cv2", 64, 64, 40, 40, 3, 1, fused=_F)
        reg("l12.cv2", 192, 128, 40, 40, 1, 1, fused=_F)

        # L15 C2f (192->64, 80x80, n=1)
        reg("l15.cv1", 192, 64, 80, 80, 1, 1, fused=_F)
        reg("l15.bn0.cv1", 32, 32, 80, 80, 3, 1, fused=_F)
        reg("l15.bn0.cv2", 32, 32, 80, 80, 3, 1, fused=_F)
        reg("l15.cv2", 96, 64, 80, 80, 1, 1, fused=_F)

        # L16 CBS (64->64, 80->40, k3s2)
        reg("l16", 64, 64, 80, 80, 3, 2, fused=_F)

        # L18 C2f (192->128, 40x40, n=1)
        reg("l18.cv1", 192, 128, 40, 40, 1, 1, fused=_F)
        reg("l18.bn0.cv1", 64, 64, 40, 40, 3, 1, fused=_F)
        reg("l18.bn0.cv2", 64, 64, 40, 40, 3, 1, fused=_F)
        reg("l18.cv2", 192, 128, 40, 40, 1, 1, fused=_F)

        # L19 CBS (128->128, 40->20, k3s2)
        reg("l19", 128, 128, 40, 40, 3, 2, fused=_F)

        # L21 C2f (384->256, 20x20, n=1)
        reg("l21.cv1", 384, 256, 20, 20, 1, 1, fused=_F)
        reg("l21.bn0.cv1", 128, 128, 20, 20, 3, 1, fused=_F)
        reg("l21.bn0.cv2", 128, 128, 20, 20, 3, 1, fused=_F)
        reg("l21.cv2", 384, 256, 20, 20, 1, 1, fused=_F)

    def _cbs(self, x, name):
        """CBS: fused conv+bias+SiLU on NPU (int8 in, int8 out)."""
        buf = _buf(name)
        if self._weights_prepared:
            entry = self._pdi_map[buf]
            if entry["sub_op"].fused:
                return self.int8_cbs_fused_fast(x, buf)
            return self.int8_cbs_fast(x, buf)
        w, ws, b = lookup_weight(self.int8_weights, name)
        pred = PRED_MAP[name]
        in_scale = self.act_scales.get(pred, 1.0)
        return self.int8_cbs(x, buf, w, ws, b, in_scale)

    def _c2f(self, x, prefix, n_bn, shortcut=True):
        """Run a C2f block. Operates in int8 when fused CBS is active."""
        x = self._cbs(x, f"{prefix}.cv1")
        chunks = x.chunk(2, dim=1)
        outputs = [chunks[0], chunks[1]]
        for i in range(n_bn):
            inp = outputs[-1]
            y = self._cbs(inp, f"{prefix}.bn{i}.cv1")
            y = self._cbs(y, f"{prefix}.bn{i}.cv2")
            if shortcut:
                if y.dtype == torch.int8:
                    y = (y.int() + inp.int()).clamp(-128, 127).to(torch.int8)
                else:
                    y = y + inp
            outputs.append(y)
        x = torch.cat(outputs, dim=1)
        return self._cbs(x, f"{prefix}.cv2")

    def forward(self, x):
        """Run backbone + neck.

        With fused CBS kernels, data flows as int8 between layers.
        Non-CBS ops (concat, upsample, maxpool, residual add) operate
        directly on int8 tensors — no Python dequant/SiLU needed.

        Args:
            x: Input [1, 3, 640, 640] float tensor.

        Returns:
            (det_p3, det_p4, det_p5) int8 feature maps (or float if
            fused is not active).
        """
        x = x.float()
        x = F.pad(x, (0, 0, 0, 0, 0, 5))  # 3ch -> 8ch

        # ---- BACKBONE ----
        x = self._cbs(x, "l0")
        print(f"  L0:  {x.shape} {x.dtype}")
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

        # SPPF: convs on NPU, maxpool on CPU (int8-safe)
        x = self._cbs(x, "l9.cv1")
        if x.dtype == torch.int8:
            # MaxPool on int8: cast to float (lossless), pool, cast back
            y1 = F.max_pool2d(x.float(), 5, stride=1, padding=2).to(torch.int8)
            y2 = F.max_pool2d(y1.float(), 5, stride=1, padding=2).to(torch.int8)
            y3 = F.max_pool2d(y2.float(), 5, stride=1, padding=2).to(torch.int8)
        else:
            y1 = F.max_pool2d(x, 5, stride=1, padding=2)
            y2 = F.max_pool2d(y1, 5, stride=1, padding=2)
            y3 = F.max_pool2d(y2, 5, stride=1, padding=2)
        x = torch.cat([x, y1, y2, y3], dim=1)
        p5 = self._cbs(x, "l9.cv2")
        print(f"  L9:  {p5.shape}  [P5]")

        # ---- NECK (FPN up-path) ----
        if p5.dtype == torch.int8:
            # Nearest 2x upsample on int8: just duplicate pixels
            x = p5.repeat_interleave(2, dim=2).repeat_interleave(2, dim=3)
        else:
            x = F.interpolate(p5, scale_factor=2, mode="nearest")
        x = torch.cat([x, p4], dim=1)
        l12_out = self._c2f(x, "l12", 1, shortcut=False)
        print(f"  L12: {l12_out.shape}")

        if l12_out.dtype == torch.int8:
            x = l12_out.repeat_interleave(2, dim=2).repeat_interleave(2, dim=3)
        else:
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

    def __init__(
        self, shifts, act_scales, int8_weights, context=None, preprocessor=None
    ):
        self.shifts = shifts
        self.act_scales = act_scales
        self.int8_weights = int8_weights
        super().__init__(context=context, preprocessor=preprocessor)

    def _fused_shifts(self, name):
        """Compute shift1/shift2 for a fused CBS layer."""
        _, w_scale, _ = lookup_weight(self.int8_weights, name)
        pred = PRED_MAP[name]
        in_act_scale = self.act_scales.get(pred, 1.0)
        if in_act_scale == 0:
            in_act_scale = 1.0
        out_act_scale = self.act_scales.get(name, 1.0)
        if out_act_scale == 0:
            out_act_scale = 1.0
        return compute_fused_shifts(w_scale, in_act_scale, out_act_scale)

    def _register_all_layers(self):
        s = self.shifts

        def reg(name, ic, oc, h, w, ks, stride, fused=False):
            cols = _auto_columns_int8(ic, oc, ks, w, stride, fused=fused)
            shift1, shift2 = None, None
            if fused:
                shift1, shift2 = self._fused_shifts(name)
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
                fused=fused,
                shift1=shift1,
                shift2=shift2,
            )

        # cv1/cv2 are CBS (fused SiLU), cv3 is bare conv (no activation)
        for branch in ["reg_p3", "cls_p3"]:
            c_mid = 64 if branch.startswith("reg") else 80
            c_out = 64 if branch.startswith("reg") else 80
            reg(f"det.{branch}.cv1", 64, c_mid, 80, 80, 3, 1, fused=True)
            reg(f"det.{branch}.cv2", c_mid, c_mid, 80, 80, 3, 1, fused=True)
            reg(f"det.{branch}.cv3", c_mid, c_out, 80, 80, 1, 1)

        for branch in ["reg_p4", "cls_p4"]:
            c_mid = 64 if branch.startswith("reg") else 80
            c_out = 64 if branch.startswith("reg") else 80
            reg(f"det.{branch}.cv1", 128, c_mid, 40, 40, 3, 1, fused=True)
            reg(f"det.{branch}.cv2", c_mid, c_mid, 40, 40, 3, 1, fused=True)
            reg(f"det.{branch}.cv3", c_mid, c_out, 40, 40, 1, 1)

        for branch in ["reg_p5", "cls_p5"]:
            c_mid = 64 if branch.startswith("reg") else 80
            c_out = 64 if branch.startswith("reg") else 80
            reg(f"det.{branch}.cv1", 256, c_mid, 20, 20, 3, 1, fused=True)
            reg(f"det.{branch}.cv2", c_mid, c_mid, 20, 20, 3, 1, fused=True)
            reg(f"det.{branch}.cv3", c_mid, c_out, 20, 20, 1, 1)

    def _detect_branch(self, x, branch_name):
        """Run a detect branch (2x CBS 3x3 + 1x Conv 1x1).

        cv1/cv2 use fused conv+bias+SiLU (int8 in/out).
        cv3 is bare conv (no activation) → returns float.
        """
        if self._weights_prepared:
            for cv in ["cv1", "cv2"]:
                buf = _buf(f"det.{branch_name}.{cv}")
                entry = self._pdi_map[buf]
                if entry["sub_op"].fused:
                    x = self.int8_cbs_fused_fast(x, buf)
                else:
                    x = self.int8_cbs_fast(x, buf)
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
