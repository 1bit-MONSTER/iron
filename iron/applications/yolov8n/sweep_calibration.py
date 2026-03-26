#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Per-stage calibration percentile sweep for YOLOv8n int8.

Runs CPU int8 simulation (npu_sim=True) with different per-stage percentile
combinations to find the optimal setting that produces correct detections
(person + bus, conf > 0.25) on bus.jpg.

After CPU sweep, runs the best combo on actual NPU hardware.

Usage:
    source ironenv/bin/activate
    source /scratch/jmelber/mlir-aie/utils/env_setup.sh /scratch/jmelber/mlir-aie /opt/xrt 2>/dev/null
    python3 iron/applications/yolov8n/sweep_calibration.py
"""

import re
import time
import urllib.request
from pathlib import Path

import torch

from iron.applications.yolov8n.postprocess import YOLOv8nPostProcess
from iron.applications.yolov8n.run_int8_cpu import Int8YOLOv8nCPU
from iron.applications.yolov8n.run_pretrained import (
    COCO_NAMES,
    preprocess_image,
)


# -- Percentile combos to sweep -----------------------------------------------

COMBOS = [
    {
        "name": "combo1: aggressive detect_cbs only",
        "backbone": 1.0,
        "neck": 1.0,
        "detect_cbs": 0.95,
        "detect_bare": 1.0,
    },
    {
        "name": "combo2: mild all",
        "backbone": 0.999,
        "neck": 0.999,
        "detect_cbs": 0.97,
        "detect_bare": 0.999,
    },
    {
        "name": "combo3: mild backbone, moderate neck+detect",
        "backbone": 0.999,
        "neck": 0.99,
        "detect_cbs": 0.95,
        "detect_bare": 0.999,
    },
    {
        "name": "combo4: no-clip backbone, moderate neck+detect",
        "backbone": 1.0,
        "neck": 0.99,
        "detect_cbs": 0.95,
        "detect_bare": 1.0,
    },
    {
        "name": "combo5: mild all, moderate neck",
        "backbone": 0.999,
        "neck": 0.997,
        "detect_cbs": 0.97,
        "detect_bare": 0.999,
    },
]


def _get_stage(layer_name):
    """Classify a layer name into its network stage."""
    if layer_name == "input":
        return "input"
    if layer_name.startswith("det."):
        if ".cv3" in layer_name:
            return "detect_bare"
        return "detect_cbs"
    m = re.match(r"l(\d+)", layer_name)
    if m:
        layer_num = int(m.group(1))
        if layer_num <= 9:
            return "backbone"
        return "neck"
    return "backbone"


def make_percentile_fn(combo):
    """Create a percentile function from a combo dict."""
    stage_pct = {
        "input": 1.0,
        "backbone": combo["backbone"],
        "neck": combo["neck"],
        "detect_cbs": combo["detect_cbs"],
        "detect_bare": combo["detect_bare"],
    }

    def fn(layer_name):
        return stage_pct[_get_stage(layer_name)]

    return fn


def analyze_cls_outputs(cls_tensors):
    """Analyze classification output tensors."""
    stats = {}
    for i, (scale, cls) in enumerate(
        zip(["p3", "p4", "p5"], cls_tensors)
    ):
        flat = cls.float().squeeze(0).permute(1, 2, 0).reshape(-1, 80)
        scores = flat.sigmoid()
        max_per_anchor = scores.max(dim=1)[0]
        stats[f"cls_{scale}"] = {
            "range": (cls.min().item(), cls.max().item()),
            "logit_abs_max": cls.abs().max().item(),
            "max_score": max_per_anchor.max().item(),
            "mean_score": max_per_anchor.mean().item(),
            "gt_0.25": (max_per_anchor > 0.25).sum().item(),
            "gt_0.10": (max_per_anchor > 0.10).sum().item(),
        }
    return stats


def run_combo_cpu(runner, img_tensor, combo, pp_25, pp_10):
    """Run a single combo through CPU int8 simulation with npu_sim=True."""
    pct_fn = make_percentile_fn(combo)
    runner.recalibrate_percentiles(pct_fn)

    result = runner.forward_int8(img_tensor, npu_sim=True)

    # Analyze cls outputs
    cls_stats = analyze_cls_outputs(result["cls"])

    # Detections at conf=0.25
    dets_25 = pp_25(result["reg"], result["cls"])
    n_25 = len(dets_25["boxes"])

    # Detections at conf=0.10
    dets_10 = pp_10(result["reg"], result["cls"])
    n_10 = len(dets_10["boxes"])

    return {
        "cls_stats": cls_stats,
        "dets_25": dets_25,
        "n_25": n_25,
        "dets_10": dets_10,
        "n_10": n_10,
        "result": result,
    }


def print_combo_result(combo, res):
    """Pretty-print results for a single combo."""
    print(f"\n{'=' * 70}")
    print(f"  {combo['name']}")
    print(
        f"  backbone={combo['backbone']}  neck={combo['neck']}  "
        f"detect_cbs={combo['detect_cbs']}  detect_bare={combo['detect_bare']}"
    )
    print(f"{'=' * 70}")

    # Cls stats
    for scale in ["cls_p3", "cls_p4", "cls_p5"]:
        s = res["cls_stats"][scale]
        print(
            f"  {scale}: range=[{s['range'][0]:.2f}, {s['range'][1]:.2f}]  "
            f"max_score={s['max_score']:.4f}  "
            f">0.25: {s['gt_0.25']}  >0.10: {s['gt_0.10']}"
        )

    # Detections
    print(f"\n  Detections (conf>0.25): {res['n_25']}")
    if res["n_25"] > 0:
        for i in range(min(10, res["n_25"])):
            box = res["dets_25"]["boxes"][i].tolist()
            score = res["dets_25"]["scores"][i].item()
            label = res["dets_25"]["labels"][i].item()
            name = (
                COCO_NAMES[label]
                if label < len(COCO_NAMES)
                else f"class_{label}"
            )
            print(
                f"    {name}: {score:.3f} at "
                f"[{box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f}]"
            )

    print(f"  Detections (conf>0.10): {res['n_10']}")
    if res["n_10"] > 0:
        for i in range(min(10, res["n_10"])):
            box = res["dets_10"]["boxes"][i].tolist()
            score = res["dets_10"]["scores"][i].item()
            label = res["dets_10"]["labels"][i].item()
            name = (
                COCO_NAMES[label]
                if label < len(COCO_NAMES)
                else f"class_{label}"
            )
            print(
                f"    {name}: {score:.3f} at "
                f"[{box[0]:.0f},{box[1]:.0f},{box[2]:.0f},{box[3]:.0f}]"
            )


def main():
    image_path = Path("test_bus.jpg")
    model_path = "yolov8n.pt"

    if not image_path.exists():
        print(f"Downloading test image to {image_path}...")
        urllib.request.urlretrieve(
            "https://ultralytics.com/images/bus.jpg", str(image_path)
        )

    print("=" * 70)
    print("YOLOv8n INT8 Per-Stage Calibration Sweep (CPU sim, npu_sim=True)")
    print("=" * 70)

    # Load model and calibrate once with p100 (stores all percentile data)
    print("\n[1] Loading model and calibrating (stores percentile data)...")
    t0 = time.time()
    runner = Int8YOLOv8nCPU(model_path)
    img_tensor = preprocess_image(image_path, img_size=640)
    runner.calibrate(img_tensor)  # Default p100, stores percentile data
    print(f"    Setup: {time.time() - t0:.1f}s")

    pp_25 = YOLOv8nPostProcess(conf_thres=0.25, iou_thres=0.45)
    pp_10 = YOLOv8nPostProcess(conf_thres=0.10, iou_thres=0.45)

    # Baseline: p100 everywhere
    print("\n[2] Baseline: p100 everywhere (npu_sim=True)")
    baseline_combo = {
        "name": "baseline: p100 everywhere",
        "backbone": 1.0,
        "neck": 1.0,
        "detect_cbs": 1.0,
        "detect_bare": 1.0,
    }
    baseline_res = run_combo_cpu(runner, img_tensor, baseline_combo, pp_25, pp_10)
    print_combo_result(baseline_combo, baseline_res)

    # Run all combos
    print(f"\n\n[3] Sweeping {len(COMBOS)} combos...")
    results = {}
    for combo in COMBOS:
        t0 = time.time()
        res = run_combo_cpu(runner, img_tensor, combo, pp_25, pp_10)
        elapsed = time.time() - t0
        print_combo_result(combo, res)
        print(f"  Time: {elapsed:.2f}s")
        results[combo["name"]] = (combo, res)

    # Summary table
    print(f"\n\n{'=' * 70}")
    print("SWEEP SUMMARY")
    print(f"{'=' * 70}")
    print(
        f"{'Combo':<50} {'n@0.25':>6} {'n@0.10':>6} "
        f"{'max_cls_score':>13} {'correct?':>8}"
    )
    print("-" * 90)

    all_results = [(baseline_combo, baseline_res)] + [
        (c, results[c["name"]][1]) for c in COMBOS
    ]

    for combo, res in all_results:
        max_score = max(
            res["cls_stats"][f"cls_{s}"]["max_score"]
            for s in ["p3", "p4", "p5"]
        )
        # Check if person (0) or bus (5) detected
        correct = "NO"
        if res["n_25"] > 0:
            labels = res["dets_25"]["labels"].tolist()
            has_person = 0 in labels
            has_bus = 5 in labels
            if has_person and has_bus:
                correct = "YES"
            elif has_person or has_bus:
                correct = "PARTIAL"

        print(
            f"  {combo['name']:<48} {res['n_25']:>6} {res['n_10']:>6} "
            f"{max_score:>13.4f} {correct:>8}"
        )

    # Find best combo
    best = None
    best_score = -1
    for combo, res in all_results:
        if res["n_25"] > 0:
            labels = res["dets_25"]["labels"].tolist()
            has_person = 0 in labels
            has_bus = 5 in labels
            score = 0
            if has_person:
                score += 1
            if has_bus:
                score += 1
            score += res["n_25"] * 0.01  # tie-break on more detections
            if score > best_score:
                best_score = score
                best = combo

    if best:
        print(f"\n  BEST COMBO: {best['name']}")
    else:
        print("\n  No combo produced correct detections at conf>0.25")
        # Fall back to best at conf>0.10
        for combo, res in all_results:
            if res["n_10"] > 0:
                labels = res["dets_10"]["labels"].tolist()
                has_person = 0 in labels
                has_bus = 5 in labels
                if has_person or has_bus:
                    print(
                        f"  At conf>0.10: {combo['name']} has "
                        f"person={has_person} bus={has_bus}"
                    )


if __name__ == "__main__":
    main()
