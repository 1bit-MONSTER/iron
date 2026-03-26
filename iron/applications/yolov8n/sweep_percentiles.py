#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Sweep per-stage calibration percentiles for int8 YOLOv8n.

Runs the full model on CPU with NPU shift simulation to find the
percentile combination that produces correct detections (person + bus
at conf > 0.25) on bus.jpg.

Usage:
    python3 iron/applications/yolov8n/sweep_percentiles.py [--image PATH]
"""

import argparse
import re
import time
import urllib.request
from itertools import product
from pathlib import Path

import torch

from iron.applications.yolov8n.postprocess import YOLOv8nPostProcess
from iron.applications.yolov8n.run_int8_cpu import Int8YOLOv8nCPU
from iron.applications.yolov8n.run_pretrained import COCO_NAMES, preprocess_image


# -- Per-stage percentile logic -----------------------------------------------


def get_stage(layer_name):
    """Classify a layer into its network stage."""
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


def make_percentile_fn(backbone, neck, detect_cbs, detect_bare):
    """Create a percentile function from per-stage values."""
    stage_pcts = {
        "input": 1.0,  # never clip the input image
        "backbone": backbone,
        "neck": neck,
        "detect_cbs": detect_cbs,
        "detect_bare": detect_bare,
    }

    def fn(layer_name):
        return stage_pcts[get_stage(layer_name)]

    return fn


# -- Main sweep ---------------------------------------------------------------


def run_sweep(runner, img_tensor):
    """Try all percentile combos and report detection results."""

    pp = YOLOv8nPostProcess(conf_thres=0.25, iou_thres=0.45)
    pp_low = YOLOv8nPostProcess(conf_thres=0.10, iou_thres=0.45)

    # Percentile grid
    backbone_opts = [0.999, 0.997, 0.995]
    neck_opts = [0.999, 0.997, 0.995, 0.99]
    detect_cbs_opts = [0.99, 0.97, 0.95, 0.93]
    detect_bare_opts = [0.999, 0.997, 0.995, 0.99]

    n_combos = (
        len(backbone_opts)
        * len(neck_opts)
        * len(detect_cbs_opts)
        * len(detect_bare_opts)
    )
    print(f"Sweeping {n_combos} combinations...")
    print()

    header = (
        f"{'BB':>6s} {'NECK':>6s} {'DCBS':>6s} {'DBAR':>6s} | "
        f"{'nDet':>4s} {'nLow':>4s} {'person':>7s} {'bus':>7s} {'classes'}"
    )
    print(header)
    print("-" * len(header) + "----------")

    winners = []

    for bb, nk, dcbs, dbar in product(
        backbone_opts, neck_opts, detect_cbs_opts, detect_bare_opts
    ):
        pfn = make_percentile_fn(bb, nk, dcbs, dbar)
        runner.recalibrate_percentiles(pfn)

        result = runner.forward_int8(img_tensor, npu_sim=True)

        dets = pp(result["reg"], result["cls"])
        dets_low = pp_low(result["reg"], result["cls"])
        n_det = len(dets["boxes"])
        n_low = len(dets_low["boxes"])

        # Extract class names and scores
        classes = []
        person_conf = 0.0
        bus_conf = 0.0
        for i in range(min(15, n_det)):
            label = dets["labels"][i].item()
            score = dets["scores"][i].item()
            name = COCO_NAMES[label] if label < len(COCO_NAMES) else f"cls{label}"
            classes.append(name)
            if name == "person" and score > person_conf:
                person_conf = score
            if name == "bus" and score > bus_conf:
                bus_conf = score

        class_str = ",".join(classes[:8]) if classes else "-"
        print(
            f"{bb:6.3f} {nk:6.3f} {dcbs:6.3f} {dbar:6.3f} | "
            f"{n_det:4d} {n_low:4d} {person_conf:7.3f} {bus_conf:7.3f} {class_str}"
        )

        # Check for winner: person + bus at conf > 0.25, not too many FPs
        has_person = person_conf > 0.25
        has_bus = bus_conf > 0.25
        reasonable_count = 1 <= n_det <= 20

        if has_person and has_bus and reasonable_count:
            winners.append(
                {
                    "backbone": bb,
                    "neck": nk,
                    "detect_cbs": dcbs,
                    "detect_bare": dbar,
                    "n_det": n_det,
                    "person_conf": person_conf,
                    "bus_conf": bus_conf,
                    "classes": classes,
                }
            )

    print()
    print("=" * 70)
    if winners:
        print(f"WINNERS ({len(winners)} combos with person + bus at conf>0.25):")
        for w in sorted(winners, key=lambda x: -(x["person_conf"] + x["bus_conf"])):
            print(
                f"  BB={w['backbone']:.3f} NECK={w['neck']:.3f} "
                f"DCBS={w['detect_cbs']:.3f} DBAR={w['detect_bare']:.3f} "
                f"| {w['n_det']} dets, person={w['person_conf']:.3f} "
                f"bus={w['bus_conf']:.3f} | {','.join(w['classes'][:8])}"
            )
    else:
        print("NO WINNERS found. Showing best combos by person+bus confidence:")
        # Show combos with any detections
        print("Try broader search or adjust thresholds.")

    return winners


def main():
    parser = argparse.ArgumentParser(
        description="Sweep per-stage calibration percentiles"
    )
    parser.add_argument("--image", default="test_bus.jpg", help="Path to test image")
    parser.add_argument(
        "--model", default="yolov8n.pt", help="Path to YOLOv8n weights"
    )
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Downloading test image to {image_path}...")
        urllib.request.urlretrieve(
            "https://ultralytics.com/images/bus.jpg", str(image_path)
        )

    print("=" * 70)
    print("Per-Stage Percentile Sweep for Int8 YOLOv8n")
    print("=" * 70)

    # Load model and calibrate (once, stores all percentile data)
    print("\n[1] Loading model and calibrating (stores percentile data)...")
    t0 = time.time()
    runner = Int8YOLOv8nCPU(args.model)
    img_tensor = preprocess_image(image_path, img_size=640)
    runner.calibrate(img_tensor)  # p100 by default, stores all percentiles
    print(f"    Setup: {time.time() - t0:.1f}s")

    # Run the sweep
    print("\n[2] Running sweep (CPU NPU simulation)...")
    t0 = time.time()
    winners = run_sweep(runner, img_tensor)
    print(f"    Sweep: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
