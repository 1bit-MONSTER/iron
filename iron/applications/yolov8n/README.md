<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# YOLOv8n NPU Implementation

End-to-end YOLOv8n object detection running on the AMD Ryzen AI NPU,
implemented using the IRON operator API. All convolution, pooling, and
upsampling operations execute on NPU hardware in bfloat16; concat,
residual add, channel split, and post-processing run on the host CPU.

## Architecture Overview

### Model Structure

YOLOv8n follows the standard three-stage detection architecture:

```
Input [1,3,640,640]
  |
  | (pad to 8ch)
  v
BACKBONE (layers 0-9)           NECK (layers 10-21)            DETECT HEAD
 L0: Conv3x3 s2  8->16  640     FPN up-path:                   Per scale (P3/P4/P5):
 L1: Conv3x3 s2  16->32 320      L10: Upsample P5 20->40        reg: CBS3x3 -> CBS3x3 -> Conv1x1
 L2: C2f n=1     32->32 160      L11: Concat(up+P4) 384ch       cls: CBS3x3 -> CBS3x3 -> Conv1x1
 L3: Conv3x3 s2  32->64 160      L12: C2f 384->128  40x40
 L4: C2f n=2     64->64 80       L13: Upsample 128  40->80     Output:
 L5: Conv3x3 s2  64->128 80      L14: Concat(up+P3) 192ch        reg: 3x [1,64,H,W]
 L6: C2f n=2     128->128 40     L15: C2f 192->64   80x80        cls: 3x [1,80,H,W]
 L7: Conv3x3 s2  128->256 40   PAN down-path:
 L8: C2f n=1     256->256 20     L16: CBS3x3 s2 64->64  80->40
 L9: SPPF k=5    256->256 20     L17: Concat(+L12) 192ch
                                  L18: C2f 192->128  40x40
Skip connections:                 L19: CBS3x3 s2 128->128 40->20
  P3 = L4 output (64ch, 80x80)   L20: Concat(+P5) 384ch
  P4 = L6 output (128ch, 40x40)  L21: C2f 384->256  20x20
  P5 = L9 output (256ch, 20x20)
```

Three feature scales feed the detect head:

| Scale | Stride | Resolution | Input Channels | Anchors |
|-------|--------|------------|----------------|---------|
| P3    | 8      | 80x80      | 64             | 6400    |
| P4    | 16     | 40x40      | 128            | 1600    |
| P5    | 32     | 20x20      | 256            | 400     |

Total anchors: **8400** across all scales.

### Composite Blocks

All composite blocks are defined in `blocks.py`:

- **CBS** (Conv + BatchNorm + SiLU): The fundamental building block.
  BatchNorm is pre-fused into the conv weight/bias at export time.
  When `activation="silu"` is set, bias and SiLU are fused into the
  AIE kernel, eliminating a DDR round-trip per block.

- **Bottleneck**: Two CBS(3x3) with optional residual shortcut.
  `x -> CBS3x3 -> CBS3x3 -> [+ x] -> out`

- **C2f** (Cross-Stage Partial v2): Pointwise expand, N bottlenecks, pointwise reduce.
  `x -> CBS1x1(c_in -> 2c) -> chunk(2) -> [A, B, BN0...BNn] -> cat -> CBS1x1((2+n)*c -> c_out)`

- **SPPF** (Spatial Pyramid Pooling Fast): Three cascaded 5x5 max pools (stride=1, padding=2)
  producing the same 13x13 receptive field as a single large pool.
  `x -> CBS1x1 -> [identity, MP5, MP5(MP5), MP5(MP5(MP5))] -> cat -> CBS1x1`

- **DetectBranch**: Two CBS(3x3) followed by a bare Conv1x1 (no BN, no SiLU).
  The final conv outputs raw logits for either regression (64ch = 4 * reg_max)
  or classification (80ch = COCO classes).

### Multi-PDI Approach

The NPU has a limited number of hardware contexts (~32). A naive approach
of allocating one hw_context per operator would exhaust this limit for
YOLOv8n's ~70+ operator instances. The solution is **multi-PDI chaining**:

1. Each **unique** operator configuration (identified by op type, channel
   counts, spatial dims, kernel size, stride, and column count) gets one PDI
   with a unique kernel ID (`0x901`, `0x902`, ...).

2. All PDIs are chained into a **single combined xclbin** via the
   `--xclbin-input` flag, which appends each PDI to the previous xclbin.

3. At runtime, all kernels reference the same combined xclbin but each
   has its own instruction stream (`.bin` file).

4. Layers sharing the same configuration (e.g., all bottleneck convs in
   a C2f block with the same channel count and spatial dims) share the
   same PDI. This **deduplication** reduces the number of PDIs from ~70+
   layer instances to ~50 unique configurations.

The multi-PDI pipeline is implemented in `pipeline.py` as `YOLOv8nPipeline`,
which extends `AIEOperatorBase` and manages all sub-operators with
`register=False` to avoid automatic context registration.

### Execution Model

The current implementation uses a **layer-by-layer** execution model:

```
for each layer in model:
    1. Convert input NCHW -> tiled layout [H, C/8, W, 8]
    2. Write input + weights to XRT buffer objects
    3. Execute single kernel via xrt_kernel(opcode, insts, ...)
    4. Read output from buffer, convert tiled -> NCHW
    5. Apply host-side ops (concat, residual add, channel split)
```

Each kernel invocation is a separate `xrt_kernel()` call with
`sync_to_device` before and `sync_from_device` after. Intermediate
activations transit through DDR between layers.

### Data Layout

All operators use the same tiled layout to avoid format conversion overhead:

```
NCHW [N, C, H, W]  <-->  Tiled [H, C/8, W, 8]
```

Channels are grouped in SIMD-friendly chunks of 8 and interleaved with
the spatial width dimension. This enables contiguous vector loads for the
AIE `aie::mmul<4,8,8>` intrinsic.

Weight layouts:
- **1x1 conv**: `[O/8, I/8, 8(ic), 8(oc)]` -- each 8x8 tile is one
  (output_group, input_group) pair.
- **3x3 conv**: `[O/8, I/8, 3, 3, 8(ic), 8(oc)]` -- spatial kernel
  dimensions kept explicit for the sliding-window loop.

## Operator Inventory

### NPU Operators

Three operator types execute on NPU hardware:

| Operator | Kernel Source | Design File | Variants |
|----------|-------------|-------------|----------|
| Conv2d 1x1 | `aie_kernels/aie2p/conv2dk1_bf16.cc` | `iron/operators/conv2d/design.py` (`my_conv2d`) | plain, bias+SiLU |
| Conv2d 3x3 | `aie_kernels/aie2p/conv2dk3_bf16.cc` | `iron/operators/conv2d/design.py` (`my_conv2d_k3`) | s1 plain, s1 bias+SiLU, s2 plain, s2 bias+SiLU |
| MaxPool2d | `aie_kernels/aie2p/maxpool2d_bf16.cc` | `iron/operators/maxpool2d/design.py` | stride-1 with padding |
| Upsample 2x | `aie_kernels/aie2p/upsample2x_bf16.cc` | `iron/operators/upsample/design.py` | nearest-neighbor 2x |

### Layer Configuration Table

Below is the full set of layers in the YOLOv8n model at 640x640 input
resolution. Layers with identical configuration keys share the same PDI.

#### Backbone Layers (L0-L9)

| Layer | Block | Type | In Ch | Out Ch | Size | KS | Stride | Notes |
|-------|-------|------|-------|--------|------|----|--------|-------|
| bb_l0 | CBS | Conv3x3+SiLU | 8 | 16 | 640x640 | 3 | 2 | RGB padded to 8ch |
| bb_l1 | CBS | Conv3x3+SiLU | 16 | 32 | 320x320 | 3 | 2 | |
| bb_l2_cv1 | C2f | Conv1x1+SiLU | 32 | 32 | 160x160 | 1 | 1 | |
| bb_l2_bn0_cv1 | C2f/BN | Conv3x3+SiLU | 16 | 16 | 160x160 | 3 | 1 | |
| bb_l2_bn0_cv2 | C2f/BN | Conv3x3+SiLU | 16 | 16 | 160x160 | 3 | 1 | Shares PDI with cv1 |
| bb_l2_cv2 | C2f | Conv1x1+SiLU | 48 | 32 | 160x160 | 1 | 1 | |
| bb_l3 | CBS | Conv3x3+SiLU | 32 | 64 | 160x160 | 3 | 2 | |
| bb_l4_cv1 | C2f | Conv1x1+SiLU | 64 | 64 | 80x80 | 1 | 1 | |
| bb_l4_bn{0,1}_cv{1,2} | C2f/BN | Conv3x3+SiLU | 32 | 32 | 80x80 | 3 | 1 | 4 layers, 1 PDI |
| bb_l4_cv2 | C2f | Conv1x1+SiLU | 128 | 64 | 80x80 | 1 | 1 | |
| bb_l5 | CBS | Conv3x3+SiLU | 64 | 128 | 80x80 | 3 | 2 | |
| bb_l6_cv1 | C2f | Conv1x1+SiLU | 128 | 128 | 40x40 | 1 | 1 | |
| bb_l6_bn{0,1}_cv{1,2} | C2f/BN | Conv3x3+SiLU | 64 | 64 | 40x40 | 3 | 1 | 4 layers, 1 PDI |
| bb_l6_cv2 | C2f | Conv1x1+SiLU | 256 | 128 | 40x40 | 1 | 1 | |
| bb_l7 | CBS | Conv3x3+SiLU | 128 | 256 | 40x40 | 3 | 2 | |
| bb_l8_cv1 | C2f | Conv1x1+SiLU | 256 | 256 | 20x20 | 1 | 1 | |
| bb_l8_bn0_cv{1,2} | C2f/BN | Conv3x3+SiLU | 128 | 128 | 20x20 | 3 | 1 | 2 layers, 1 PDI |
| bb_l8_cv2 | C2f | Conv1x1+SiLU | 384 | 256 | 20x20 | 1 | 1 | |
| bb_l9_cv1 | SPPF | Conv1x1+SiLU | 256 | 128 | 20x20 | 1 | 1 | |
| bb_l9_mp{1,2,3} | SPPF | MaxPool | 128 | 128 | 20x20 | 5 | 1 | 3 instances, 1 PDI |
| bb_l9_cv2 | SPPF | Conv1x1+SiLU | 512 | 256 | 20x20 | 1 | 1 | |

#### Neck Layers (L10-L21)

| Layer | Block | Type | In Ch | Out Ch | Size | KS | Stride | Notes |
|-------|-------|------|-------|--------|------|----|--------|-------|
| nk_up1 | - | Upsample 2x | 256 | 256 | 20x20->40x40 | - | - | |
| nk_l12_cv1 | C2f | Conv1x1+SiLU | 384 | 128 | 40x40 | 1 | 1 | |
| nk_l12_bn0_cv{1,2} | C2f/BN | Conv3x3+SiLU | 64 | 64 | 40x40 | 3 | 1 | Shares PDI with bb_l6 BNs |
| nk_l12_cv2 | C2f | Conv1x1+SiLU | 192 | 128 | 40x40 | 1 | 1 | |
| nk_up2 | - | Upsample 2x | 128 | 128 | 40x40->80x80 | - | - | |
| nk_l15_cv1 | C2f | Conv1x1+SiLU | 192 | 64 | 80x80 | 1 | 1 | |
| nk_l15_bn0_cv{1,2} | C2f/BN | Conv3x3+SiLU | 32 | 32 | 80x80 | 3 | 1 | Shares PDI with bb_l4 BNs |
| nk_l15_cv2 | C2f | Conv1x1+SiLU | 96 | 64 | 80x80 | 1 | 1 | |
| nk_l16 | CBS | Conv3x3+SiLU | 64 | 64 | 80x80 | 3 | 2 | |
| nk_l18_cv1 | C2f | Conv1x1+SiLU | 192 | 128 | 40x40 | 1 | 1 | Shares PDI with nk_l12_cv2 |
| nk_l18_bn0_cv{1,2} | C2f/BN | Conv3x3+SiLU | 64 | 64 | 40x40 | 3 | 1 | Shares PDI with bb_l6 BNs |
| nk_l18_cv2 | C2f | Conv1x1+SiLU | 192 | 128 | 40x40 | 1 | 1 | Shares PDI with nk_l18_cv1 |
| nk_l19 | CBS | Conv3x3+SiLU | 128 | 128 | 40x40 | 3 | 2 | |
| nk_l21_cv1 | C2f | Conv1x1+SiLU | 384 | 256 | 20x20 | 1 | 1 | Shares PDI with bb_l8_cv2 |
| nk_l21_bn0_cv{1,2} | C2f/BN | Conv3x3+SiLU | 128 | 128 | 20x20 | 3 | 1 | Shares PDI with bb_l8 BNs |
| nk_l21_cv2 | C2f | Conv1x1+SiLU | 384 | 256 | 20x20 | 1 | 1 | Shares PDI with nk_l21_cv1 |

#### Detect Head Layers

Each scale has a regression branch (c_mid=64, c_out=64) and a
classification branch (c_mid=80, c_out=80):

| Layer | Branch | Type | In Ch | Out Ch | Size | KS | Notes |
|-------|--------|------|-------|--------|------|----|-------|
| det_reg_p3_cv{1,2} | Reg P3 | CBS 3x3+SiLU | 64 | 64 | 80x80 | 3 | |
| det_reg_p3_cv3 | Reg P3 | Conv1x1 (bare) | 64 | 64 | 80x80 | 1 | No activation |
| det_cls_p3_cv{1,2} | Cls P3 | CBS 3x3+SiLU | 80 | 80 | 80x80 | 3 | 80ch: no 8-div issue for k3 |
| det_cls_p3_cv3 | Cls P3 | Conv1x1 (bare) | 80 | 80 | 80x80 | 1 | No activation |
| det_reg_p4_cv{1,2} | Reg P4 | CBS 3x3+SiLU | 64 | 64 | 40x40 | 3 | cv1 in=128 |
| det_reg_p4_cv3 | Reg P4 | Conv1x1 (bare) | 64 | 64 | 40x40 | 1 | |
| det_cls_p4_cv{1,2} | Cls P4 | CBS 3x3+SiLU | 80 | 80 | 40x40 | 3 | cv1 in=128 |
| det_cls_p4_cv3 | Cls P4 | Conv1x1 (bare) | 80 | 80 | 40x40 | 1 | |
| det_reg_p5_cv{1,2} | Reg P5 | CBS 3x3+SiLU | 64 | 64 | 20x20 | 3 | cv1 in=256 |
| det_reg_p5_cv3 | Reg P5 | Conv1x1 (bare) | 64 | 64 | 20x20 | 1 | |
| det_cls_p5_cv{1,2} | Cls P5 | CBS 3x3+SiLU | 80 | 80 | 20x20 | 3 | cv1 in=256 |
| det_cls_p5_cv3 | Cls P5 | Conv1x1 (bare) | 80 | 80 | 20x20 | 1 | |

### Host-Side Operations

The following operations execute on the CPU between NPU kernel invocations:

| Operation | Where Used | Description |
|-----------|-----------|-------------|
| Channel concat | C2f output, SPPF output, Neck concat layers | `torch.cat(tensors, dim=1)` |
| Channel split | C2f after cv1 | `tensor.chunk(2, dim=1)` |
| Residual add | Bottleneck shortcut | `y + x` elementwise |
| Padding | Input (3ch->8ch), MaxPool (-inf pad) | `F.pad()` |
| Layout conversion | Every layer boundary | `nchw_to_tiled()` / `tiled_to_nchw()` |

### Auto-Column Selection

The `_auto_columns()` function in `blocks.py` automatically selects the
number of AIE columns (1, 2, 4, or 8) for each operator based on L1
memory constraints:

```python
# Per-core weight must fit in ~40KB (of 64KB L1 total)
# Per-core output channels must be a multiple of 8
for cols in [1, 2, 4, 8]:
    per_core_oc = out_channels // cols
    per_core_weight_bytes = in_channels * per_core_oc * k_elems * 2
    if per_core_oc % 8 == 0 and per_core_weight_bytes <= 40KB:
        return cols
```

## Fused Bias+SiLU Kernel

### Motivation

In a standard CBS block, the computation is:

```
NPU: y = conv(x, W)     -- DDR write
CPU: y = y + bias        -- DDR read + write
CPU: y = SiLU(y)         -- DDR read + write
NPU: next_conv(y, ...)   -- DDR read
```

This requires **3 DDR round-trips** for bias and SiLU. By fusing
bias addition and SiLU into the convolution kernel, the entire CBS
block executes in a single NPU invocation:

```
NPU: y = SiLU(conv(x, W) + bias)  -- single DDR write
```

### Bias Packing

Bias values are packed at the end of the weight buffer to avoid using
an additional DMA channel (AIE compute tiles have only 2 input + 2
output DMA channels):

```
Weight buffer layout (per column):
  [column_weights (oc_per_col * ic * k_elems) | column_bias (oc_per_col)]

Full buffer:
  [col0_weights | col0_bias | col1_weights | col1_bias | ...]
```

The kernel derives the bias pointer from the weight pointer:
```c
// For 1x1 conv:
bfloat16 *bias = weights + output_channels * input_channels;

// For 3x3 conv:
bfloat16 *bias = weights + output_channels * input_channels * 9;
```

This packing is performed in `AIEConv2d.forward()` (in `op.py`):
```python
for col in range(self.num_aie_columns):
    parts.append(weight_tiled[col_start : col_start + wt_per_col])
    parts.append(bias_np[col * bias_per_col : (col+1) * bias_per_col])
weight_tiled = np.concatenate(parts)
```

### SiLU Approximation

AIE2+ cores lack a hardware `exp()` instruction. SiLU is computed using
a rational Pade approximation for tanh:

```
SiLU(x) = x * sigmoid(x)
         = x * 0.5 * (1 + tanh(x/2))
```

The tanh approximation:
```c
// Padé approximant: tanh(z) ≈ z*(27 + z²) / (27 + 9*z²)
// Accurate for |z| < 4.5 (covers the sigmoid transition region)
float z = val * 0.5f;
float z2 = z * z;
float tanh_z = (z2 > 20.0f)
    ? (z > 0 ? 1.0f : -1.0f)          // saturation for large |z|
    : z * (27.0f + z2) / (27.0f + 9.0f * z2);  // Padé rational approx
float silu_val = val * 0.5f * (1.0f + tanh_z);
```

The saturation guard (`z2 > 20.0f`) handles large inputs where
`tanh(z) -> ±1`. For bf16, `tanh(x/2)` saturates for `|x| > ~8`,
making `sigmoid(x) = 0` or `1`. This is expected behavior and matches
the standalone SiLU operator tolerances.

### Kernel Variants

Six kernel entry points are provided across the two source files:

| Entry Point | Source | Description |
|-------------|--------|-------------|
| `conv2dk1_bf16` | `conv2dk1_bf16.cc` | 1x1 conv, vectorized (mmul<4,8,8>) |
| `conv2dk1_bf16_bias_silu` | `conv2dk1_bf16.cc` | 1x1 conv + bias + SiLU (scalar) |
| `conv2dk3_bf16` | `conv2dk3_bf16.cc` | 3x3 conv stride-1 (scalar fallback at borders) |
| `conv2dk3s2_bf16` | `conv2dk3_bf16.cc` | 3x3 conv stride-2 (vectorized) |
| `conv2dk3_bf16_bias_silu` | `conv2dk3_bf16.cc` | 3x3 s1 + bias + SiLU (scalar) |
| `conv2dk3s2_bf16_bias_silu` | `conv2dk3_bf16.cc` | 3x3 s2 + bias + SiLU (scalar) |

The vectorized `mmul<4,8,8>` path processes 4 spatial positions x 8
channels per MAC instruction. Border pixels (left/right columns) fall
back to scalar computation for correct zero-padding.

## Post-Processing Pipeline

Post-processing is implemented in `postprocess.py` as pure PyTorch
operations on the CPU. It converts raw detect head outputs into final
bounding box predictions.

### Pipeline Steps

```
Detect Head Output
  reg: 3x [1, 64, H_i, W_i]     (4 * 16 DFL bins per anchor)
  cls: 3x [1, 80, H_i, W_i]     (80 class logits per anchor)
       |
  1. Flatten across scales
       reg_flat: [8400, 64]
       cls_flat: [8400, 80]
       |
  2. DFL Decode (Distribution Focal Loss)
       [8400, 64] -> reshape [8400, 4, 16]
       -> softmax(dim=-1) -> dot([0..15])
       -> distances [8400, 4]  (left, top, right, bottom in stride units)
       |
  3. Scale to pixel coordinates
       distances *= stride_tensor  (8, 16, or 32 per anchor)
       |
  4. dist2bbox
       x1 = anchor_cx - left
       y1 = anchor_cy - top
       x2 = anchor_cx + right
       y2 = anchor_cy + bottom
       -> boxes [8400, 4]  (x1, y1, x2, y2 in pixels)
       |
  5. Sigmoid class scores
       scores = sigmoid(cls_flat)  -> [8400, 80]
       max_score, max_label = scores.max(dim=1)
       |
  6. Confidence filter
       keep = max_score > conf_thres (default 0.25)
       |
  7. Per-class NMS
       Offset boxes by class_id * img_size to prevent cross-class suppression
       Greedy IoU-based NMS with iou_thres (default 0.45)
       |
  Final Output:
    boxes:  [N, 4]  (x1, y1, x2, y2 in pixel coordinates)
    scores: [N]     (confidence scores in [0, 1])
    labels: [N]     (class indices in [0, 80))
```

### Anchor Generation

Anchor points are pre-computed as a grid of cell centers for each scale:

```python
# For each stride (8, 16, 32):
grid = meshgrid(arange(H), arange(W)) + 0.5   # cell centers
anchor_points = grid * stride                   # pixel coordinates
```

At 640x640:
- Stride 8:  80x80 grid = 6400 anchors, first at (4.0, 4.0)
- Stride 16: 40x40 grid = 1600 anchors, first at (8.0, 8.0)
- Stride 32: 20x20 grid = 400 anchors, first at (16.0, 16.0)

### DFL Decode

Distribution Focal Loss represents each box edge as a discrete
probability distribution over `reg_max=16` bins (values 0-15 in stride
units). The expected distance is:

```
distance = sum(softmax(logits[0:16]) * [0, 1, 2, ..., 15])
```

This allows the network to predict multi-modal distributions for
ambiguous boundaries rather than a single regression target.

## Weight Preparation

### BN Fusion

BatchNorm parameters are fused into conv weights at export time
(`model_prep.py:fuse_conv_bn`):

```
scale = gamma / sqrt(var + eps)
W_fused = W * scale[:, None, None, None]
b_fused = (b - mu) * scale + beta
```

This eliminates the BN layer entirely, replacing `Conv + BN` with a
single `Conv(weight=W_fused, bias=b_fused)`.

### Weight Export

```python
from iron.applications.yolov8n.model_prep import export_yolov8n_weights

# Requires: pip install ultralytics
weights = export_yolov8n_weights(output_dir="weights")
# Saves to weights/yolov8n_fused_weights.pt
```

## Build & Run

### Environment Setup

```bash
# Activate IRON environment
source /opt/xilinx/xrt/setup.sh
source ironenv/bin/activate

# Verify NPU is available
xrt-smi examine
```

### Running Tests

```bash
# Post-processing unit tests (no NPU required)
pytest iron/applications/yolov8n/test_postprocess.py -v

# Pipeline construction test (no compilation)
pytest iron/applications/yolov8n/test_pipeline.py::test_pipeline_construction -v

# Full pipeline test (requires NPU, compiles ~50 PDIs)
pytest iron/applications/yolov8n/test_pipeline.py::test_pipeline_shapes -v -m extensive

# All application tests
pytest iron/applications/yolov8n/ -v
```

### Programmatic Usage

```python
from iron.common import AIEContext
from iron.applications.yolov8n.pipeline import YOLOv8nPipeline
from iron.applications.yolov8n.postprocess import YOLOv8nPostProcess

# Create context and pipeline
ctx = AIEContext()
pipeline = YOLOv8nPipeline(img_height=640, img_width=640, context=ctx)

# Compile all operators (builds ~50 unique PDIs into one xclbin)
ctx.compile_all()

# Load pre-exported weights (with fused BatchNorm)
weights = make_or_load_weights()  # dict with backbone/neck/detect keys
pipeline.load_weights(weights)

# Prepare XRT runtime
ctx.prepare_runtime()

# Run inference
import torch
x = torch.randn(1, 3, 640, 640, dtype=torch.bfloat16)
raw = pipeline.forward(x)

# Post-process: DFL decode + NMS
postproc = YOLOv8nPostProcess(nc=80, reg_max=16, img_size=640)
detections = postproc(raw["reg"], raw["cls"])
# detections = {"boxes": [N,4], "scores": [N], "labels": [N]}
```

### Running with Pretrained Weights (Real Object Detection)

Detect objects in an image using pretrained YOLOv8n weights on the NPU:

```bash
# Prerequisites
pip install ultralytics opencv-python

# Environment
source ~/.bashrc
source ironenv/bin/activate
source /scratch/jmelber/mlir-aie/utils/env_setup.sh /scratch/jmelber/mlir-aie /opt/xrt

# Run on the classic YOLO test image
python3 -m iron.applications.yolov8n.run_pretrained --image test_bus.jpg
```

**Example output (bus.jpg):**
```
NPU DETECTIONS: 5
  person: 0.848 [41, 236, 190, 537]
  person: 0.840 [529, 230, 640, 519]
  bus:    0.835 [7, 136, 637, 442]
  person: 0.803 [176, 240, 272, 509]
  person: 0.430 [-1, 324, 58, 516]
```

**How it works:**
1. Loads ultralytics YOLOv8n pretrained weights (COCO, 80 classes)
2. Fuses Conv+BatchNorm into single weight+bias per layer
3. Converts weights to bfloat16, pads L0 from 3→8 input channels
4. Runs backbone (L0-L9) → neck (L10-L21) → detect head (6 branches) on NPU
5. Post-processes with DFL decode + dist2bbox + NMS
6. Each block runs in its own AIEContext with XRT cache cleanup between blocks

**Performance (unoptimized, scalar k3 kernels):**
- Inference: ~88s (dominated by scalar 3×3 conv — vectorized would be ~10× faster)
- Compilation: ~0s (cached after first run)
- Post-processing: <0.01s

**Accuracy:**
- Matches ultralytics CPU reference: same objects detected (4 person + 1 bus)
- Per-layer NPU vs CPU correlation: >0.999 through all backbone layers
- Confidence scores within ~5% of float32 reference

### Running the Full Model (Random Weights)

For testing the pipeline without pretrained weights:

```bash
python3 -m iron.applications.yolov8n.run_full_model
```

This uses 2 multi-PDI xclbins (backbone+neck: 28 PDIs, detect: 17 PDIs)
with random weights. Verifies all shapes and finite values.

## File Structure

```
iron/applications/yolov8n/
├── __init__.py
├── README.md              # This file
├── LAYER_CONFIGS.md       # All 68 operator configs with PDI map
├── pipeline.py            # YOLOv8nPipeline: multi-PDI full model
├── blocks.py              # CBS, Bottleneck, C2f, SPPF blocks
├── backbone.py            # YOLOv8nBackbone (layers 0-9)
├── neck.py                # YOLOv8nNeck (FPN + PAN, layers 10-21)
├── detect.py              # YOLOv8nDetect, DetectBranch (head)
├── postprocess.py         # YOLOv8nPostProcess (DFL + NMS)
├── model_prep.py          # BN fusion, weight export, layout utils
├── run_full_model.py      # Full model with random weights (2 xclbins)
├── run_pretrained.py      # Pretrained weights on real images
├── bench_operators.py     # Operator benchmarking script
├── benchmark_results.md   # Benchmark results table
├── test_pipeline.py       # Multi-PDI pipeline tests
├── test_backbone.py       # Backbone-only tests
├── test_neck_detect.py    # Neck + detect head tests
├── test_postprocess.py    # Post-processing unit tests (CPU only)
└── test_model_prep.py     # Weight preparation tests

iron/operators/
├── conv2d/
│   ├── op.py              # AIEConv2d operator (1x1, 3x3)
│   └── design.py          # MLIR-AIE ObjectFIFO designs
├── maxpool2d/
│   └── op.py              # AIEMaxPool2d operator
└── upsample/
    └── op.py              # AIEUpsample operator (2x nearest)

aie_kernels/aie2p/
├── conv2dk1_bf16.cc       # 1x1 conv: vectorized + bias+SiLU scalar
├── conv2dk3_bf16.cc       # 3x3 conv: s1/s2, vectorized + bias+SiLU
├── maxpool2d_bf16.cc      # Max pooling kernel
└── upsample2x_bf16.cc    # Nearest-neighbor 2x upsample kernel
```

## Known Constraints

### Hardware

- **Input size**: Designed for 640x640. Smaller sizes may hit the DMA BD
  1023-element dimension limit in TAP decomposition. Each TAP dimension
  `size` field must be <= 1023.

- **Channel alignment**: All channel counts must be multiples of 8
  (AIE SIMD width). The input image (3 channels) is padded to 8.

- **80 output channels**: Cannot be multi-column tiled for 3x3 convs.
  80/N is never a multiple of 8 for N > 1 (80/2=40, 80/4=20, 80/8=10).
  The classification detect branches (80ch intermediate) run single-column.

- **L1 memory**: 64KB per AIE tile. Weight buffers, input/output FIFOs
  (double-buffered), and stack all share this space. The `_auto_columns`
  function budgets 40KB for weights to leave room for FIFOs.

- **DMA channels**: 2 input + 2 output per compute tile. Conv2d uses
  3 channels (input, weights, output) which fits with the weight FIFO
  using depth=1 (loaded once, not streamed).

### Software

- **Batch size**: Only batch=1 is supported. This is inherent to the
  NPU's single-image processing model.

- **Compilation time**: Building ~50 unique PDIs takes significant time
  on first run. Artifacts are cached in the build directory; subsequent
  runs skip compilation for unchanged configs.

- **NPU context exhaustion**: Running many tests in a single pytest
  session can exhaust NPU hardware contexts. Run extensive tests
  individually with `-k test_name`.

- **SiLU fused kernels are scalar**: The `bias_silu` kernel variants
  currently use scalar implementations. The base convolution kernels
  (`conv2dk1_bf16`, `conv2dk3_bf16`) have vectorized paths using
  `aie::mmul<4,8,8>`.

## Future Work

### Phase F: Dataflow Fusion

The current layer-by-layer execution model writes every intermediate
activation to DDR. Dataflow fusion would connect producer and consumer
cores via core-to-core ObjectFIFOs through L1/L2 memory, eliminating
DDR round-trips for intermediate results.

Priority candidates for fusion:
- CBS blocks (conv + bias + SiLU already fused in kernel)
- Bottleneck pairs within C2f blocks (two 3x3 convs)
- Sequential CBS + MaxPool in SPPF

### Vectorized SiLU Kernels

The fused bias+SiLU kernel variants currently use scalar
implementations. Vectorizing these using AIE2+ `aie::tanh<bfloat16>()`
hardware instructions (available on AIE2+ but not AIE2) would
significantly improve throughput for CBS blocks, which dominate the
model's compute.

### Weight Pre-Tiling

Currently, weight layout conversion (`weights_to_tiled`,
`weights_to_tiled_3x3`) happens at runtime in Python before each
inference. Pre-converting and saving weights in tiled layout at export
time would eliminate this per-inference overhead.

### End-to-End Image Pipeline

Current input is a pre-processed `[1, 3, 640, 640]` bfloat16 tensor.
A complete pipeline would add:
- Image decode and resize to 640x640
- Letterbox padding for non-square images
- Normalization (0-255 -> 0-1)
- Output coordinate rescaling to original image dimensions
