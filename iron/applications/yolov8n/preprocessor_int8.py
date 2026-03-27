# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One-time preprocessing for int8 YOLOv8n inference on NPU.

Consolidates all expensive one-time work that should NOT repeat per frame:
- BN fusion + int8 weight quantization
- Calibration (float forward pass for activation scales)
- Shift computation (per-layer requantization shifts)
- Weight tiling (layout transform to AIE-friendly format)
- Pre-computation of per-layer inference constants

Usage:
    from iron.applications.yolov8n.preprocessor_int8 import Int8ModelPreprocessor
    from iron.applications.yolov8n.run_pretrained_int8 import Int8YOLOv8nPipeline
    from iron.common import AIEContext

    # One-time setup (~5-10s):
    preprocessor = Int8ModelPreprocessor("yolov8n.pt", calibration_image)

    ctx = AIEContext(use_runlist=False)
    pipeline = Int8YOLOv8nPipeline(preprocessor, context=ctx)
    ctx.compile_all()
    ctx.prepare_runtime()
    pipeline.prepare_weights()
    pipeline.load_static_weights()

    # Per-frame inference (no preprocessing overhead):
    x = preprocessor.preprocess_image(frame)
    result = pipeline.forward(x)
"""

import time

import numpy as np
import torch
import torch.nn.functional as F

from iron.applications.yolov8n.pipeline_int8 import (
    PRED_MAP,
    _buf,
    compute_all_shifts,
    lookup_weight,
)
from iron.operators.conv2d_int8.op import (
    weights_to_tiled_int8,
    weights_to_tiled_int8_k3,
)


class Int8ModelPreprocessor:
    """One-time preprocessing for int8 YOLOv8n — run once, reuse for every frame.

    Performs all expensive preprocessing steps exactly once:
    1. Fuses Conv+BN across the entire model
    2. Quantizes all weights to int8
    3. Runs a calibration forward pass to determine activation scales
    4. Computes per-layer right-shift values for NPU requantization
    5. Pre-tiles all weights to AIE layout
    6. Pre-computes per-layer inference constants (dequant scales, bias views)

    The resulting data is consumed by Int8YOLOv8nPipeline (or its subclasses)
    to set up static weight BOs and skip per-frame weight processing.
    """

    def __init__(self, model_path, calibration_image, percentile_fn=None):
        """
        Args:
            model_path: Path to ultralytics YOLOv8n weights (e.g., "yolov8n.pt").
            calibration_image: [1, 3, 640, 640] tensor for calibration forward pass.
            percentile_fn: Optional callable(layer_name) -> float percentile in (0, 1].
                Controls clipping aggressiveness per layer during calibration.
                If None, uses absolute max (percentile=1.0).
        """
        t0 = time.time()

        # 1. Load model, fuse BN, quantize weights to int8
        from iron.applications.yolov8n.run_int8_cpu import Int8YOLOv8nCPU

        runner = Int8YOLOv8nCPU(model_path)
        self._int8_weights = runner.int8_weights

        # 2. Calibrate via float forward pass to determine activation scales
        runner.calibrate(calibration_image, percentile_fn=percentile_fn)
        self._act_scales = dict(runner.act_scales)

        # 3. Compute per-layer shift values (fused returns (shifts, eff_scales))
        result = compute_all_shifts(self._int8_weights, self._act_scales)
        if isinstance(result, tuple):
            self._shifts, self._act_scales = result
        else:
            self._shifts = result

        # 4. Pre-tile all weights and pre-compute inference constants
        self._layer_data = {}
        self._total_weight_bytes = 0
        self._prepare_all_layers()

        self.setup_time = time.time() - t0

    @property
    def shifts(self):
        """Per-layer right-shift values for NPU requantization."""
        return self._shifts

    @property
    def act_scales(self):
        """Per-layer activation scales from calibration."""
        return self._act_scales

    @property
    def int8_weights(self):
        """Quantized int8 weight dict (backbone/neck/detect structure)."""
        return self._int8_weights

    def _prepare_all_layers(self):
        """Pre-tile weights and pre-compute inference constants for all layers."""
        for dot_name in PRED_MAP:
            buf_name = _buf(dot_name)
            w_int8, w_scale, bias = lookup_weight(self._int8_weights, dot_name)

            kernel_size = w_int8.shape[2]
            if kernel_size == 3:
                tiled_w = weights_to_tiled_int8_k3(w_int8)
            else:
                tiled_w = weights_to_tiled_int8(w_int8)

            pred = PRED_MAP[dot_name]
            in_act_scale = self._act_scales.get(pred, 1.0)
            if in_act_scale == 0:
                in_act_scale = 1.0

            shift = self._shifts[dot_name]
            dequant_scale = float((2**shift) * w_scale * in_act_scale)

            self._layer_data[buf_name] = {
                "tiled_weights": tiled_w,
                "in_act_scale": in_act_scale,
                "dequant_scale": dequant_scale,
                "bias_view": bias.view(1, -1, 1, 1),
            }
            self._total_weight_bytes += tiled_w.nbytes

    def get_layer_data(self, buf_name):
        """Return pre-computed inference constants for a layer.

        Args:
            buf_name: Buffer-safe layer name (underscores, e.g., "l2_cv1").

        Returns:
            dict with keys: tiled_weights, in_act_scale, dequant_scale, bias_view.
        """
        return self._layer_data[buf_name]

    def get_static_weight_data(self, buf_name):
        """Return pre-tiled weight data as numpy int8 array for static BO.

        Args:
            buf_name: Buffer-safe layer name (underscores, e.g., "l2_cv1").

        Returns:
            1D numpy int8 array ready for XRT BO write.
        """
        return self._layer_data[buf_name]["tiled_weights"]

    def preprocess_image(self, image_tensor):
        """Per-frame preprocessing: pad 3 -> 8 channels.

        This is the ONLY per-frame work needed. Everything else was
        pre-computed during __init__.

        Args:
            image_tensor: [1, 3, 640, 640] input tensor (any dtype).

        Returns:
            [1, 8, 640, 640] float32 tensor with 5 zero-padded channels.
        """
        return F.pad(image_tensor.float(), (0, 0, 0, 0, 0, 5))

    def summary(self):
        """Print preprocessing summary."""
        n_layers = len(self._layer_data)
        shifts = list(self._shifts.values())
        print("Int8ModelPreprocessor:")
        print(f"  Layers:      {n_layers}")
        print(
            f"  Shifts:      [{min(shifts)}, {max(shifts)}] "
            f"(mean={sum(shifts) / len(shifts):.1f})"
        )
        print(f"  Weight data: {self._total_weight_bytes / 1024:.0f} KB")
        print(f"  Setup time:  {self.setup_time:.1f}s")
