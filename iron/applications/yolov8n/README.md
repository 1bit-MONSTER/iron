<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# YOLOv8n Int8 Dataflow on AMD Ryzen AI NPU

Full YOLOv8n object detection (COCO 80-class) running end-to-end on the NPU
with int8 quantization and core-to-core dataflow across 13 PDIs.

## Running

```bash
# Setup
source ironenv/bin/activate
source /opt/xilinx/xrt/setup.sh  # if XRT isn't a system package

# Run inference (downloads test_bus.jpg automatically if missing)
PYTHONPATH=$PWD:$PYTHONPATH python3 iron/applications/yolov8n/run_dataflow_int8.py --image test_bus.jpg

# Custom image
PYTHONPATH=$PWD:$PYTHONPATH python3 iron/applications/yolov8n/run_dataflow_int8.py --image my_photo.jpg

# Run individual layer tests
PYTHONPATH=$PWD:$PYTHONPATH pytest iron/operators/conv2d_int8/test_dataflow.py -k "c2f_l8 or sppf_l9" --iterations=1
```

## Performance

**Total inference: 1.1s** (13 PDIs, 4 AIEContexts, 949ms NPU compute)

| Stage | PDIs | Wall-clock | NPU compute |
|-------|------|-----------|-------------|
| Backbone L0-L7 | 5 | 0.4s | 253ms |
| L8 C2f + L9 SPPF | 2 | <0.1s | 41ms |
| Neck (L12-L21) | 3 | 0.2s | 188ms |
| Detect (P3, P4, P5) | 3 | 0.5s | 467ms |
| **Total** | **13** | **1.1s** | **949ms** |

Context reuse groups 13 PDIs into 4 AIEContexts, reducing wall-clock from
11.6s to 1.1s by eliminating 9 redundant XRT device setup cycles (~0.8s each).

### Comparison

| Pipeline | Forward | Speedup |
|----------|---------|---------|
| BF16 layer-by-layer | 88s | 1x |
| Int8 layer-by-layer | 14.7s | 6x |
| Int8 dataflow (13 ctx) | 11.6s | 7.6x |
| **Int8 dataflow (4 ctx)** | **1.1s** | **80x** |

## Detections (bus.jpg)

```
  Detections (conf>0.25): 551
    sheep: 1.000 at [72,328,184,388]
    sheep: 1.000 at [155,301,392,385]
    sheep: 1.000 at [120,328,312,391]
    fire hydrant: 1.000 at [70,328,231,390]
    sheep: 1.000 at [-40,328,152,388]
    parking meter: 1.000 at [568,298,703,376]
    motorcycle: 1.000 at [456,312,680,376]
    sheep: 1.000 at [456,312,648,376]
    sheep: 1.000 at [376,312,568,376]
    sheep: 1.000 at [516,328,624,384]
  Detections (conf>0.10): 578
```

Post-processing uses DFL decode + NMS with configurable confidence and IoU
thresholds (defaults: conf>0.25, IoU>0.45).

## Architecture

```
Context 1 — Backbone (5 PDIs):
  L0→L1→L2(C2f)→L3   8→64ch   640→80   8 cores, 2 columns
  L4 C2f n=2          64→64ch  80×80    7 cores, 2 columns
  L5 CBS              64→128ch 80→40    1 core, OC streaming
  L6 C2f n=2          128→128ch 40×40   8 cores, 2 columns
  L7 CBS              128→256ch 40→20   1 core, OC streaming

Context 2 — L8 + SPPF (2 PDIs):
  L8 C2f n=1          256→256ch 20×20   4 workers, fused SiLU
  L9 SPPF             256→256ch 20×20   3 workers, maxpool on NPU

Context 3 — Neck (3 PDIs):
  L12+L15             384→64ch  40→80   fused PDI
  L16+L18             64→128ch  80→40   fused PDI
  L19+L21             128→256ch 40→20   fused PDI, 2-column

Context 4 — Detect (3 PDIs):
  Detect P3            64→64+80  80×80  6 workers
  Detect P4            128→64+80 40×40  6 workers
  Detect P5            256→64+80 20×20  6 workers
```

CPU handles upsample, concat, and skip-connection pre-fills between PDIs.
