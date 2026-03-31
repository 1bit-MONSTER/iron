# Dataflow NPU Implementation Guide

Reference material distilled from the AMD/Xilinx mlir-aie repository's MobileNetV3, ResNet, and
bottleneck examples (`programming_examples/ml/`). These patterns show how to map entire CNN inference
pipelines onto the NPU using depth-first dataflow, avoiding DDR round-trips between layers.

---

## 1. Core Concepts

### 1.1 Dataflow vs. Sequential Execution

**Sequential (multi-PDI) execution** runs one operator at a time. Each operator:
1. Reads its input from DDR via ShimDMA.
2. Computes on one or more AIE cores.
3. Writes its output back to DDR.
4. The host launches the next operator.

Every layer boundary incurs a DDR read + DDR write. For a 15-layer MobileNet, that is 30 DDR
transfers for intermediate activations alone.

**Dataflow (single-PDI) execution** maps multiple layers simultaneously onto different AIE cores.
Intermediate activations flow directly from the producer core to the consumer core through
ObjectFIFO connections -- they never leave the AIE array. Only the very first input and the
very last output touch DDR. This eliminates all intermediate DDR traffic and keeps the pipeline
busy: while core N processes row R, core N+1 processes row R-1 on the previous layer's output.

Key benefit: **latency and bandwidth** are both dramatically improved because:
- Intermediate data stays in L1 (64KB per core) or L2 (512KB per MemTile).
- Cores run concurrently in a pipelined fashion -- the AIE array is utilized more efficiently.
- DDR bandwidth is reserved for weights and the original input/final output.

### 1.2 How ObjectFIFOs Enable Core-to-Core Data Movement

An ObjectFIFO is a hardware-managed FIFO backed by DMA buffer descriptors. When you write:

```python
act_fifo = object_fifo("act_bn0_bn1", tile_A, tile_B, depth=2, element_type)
```

the compiler configures the DMA engines on both tiles so that:
- tile_A's producer DMA automatically sends completed elements to tile_B.
- tile_B's consumer DMA receives them into local buffers.
- `acquire()` blocks until data is available; `release()` frees the buffer for reuse.
- With `depth=2`, double buffering means the producer can fill buffer slot 1 while the consumer
  reads from slot 0.

For core-to-core dataflow, the ObjectFIFO is the **only** mechanism needed. No explicit DMA
programming, no manual synchronization. The FIFO abstraction handles flow control, back-pressure,
and buffer recycling.

**Sliding window pattern** for 3x3 convolutions: `acquire(3)` returns the current row and its
two neighbors. After processing, `release(1)` slides the window forward by one row. This requires
`depth >= 4` to avoid deadlock (3 acquired + 1 being filled by the producer).

### 1.3 When to Use Dataflow vs. Multi-PDI

| Criterion | Single PDI (Dataflow) | Multi-PDI (Sequential) |
|---|---|---|
| Layer count fits on array | Yes -- all layers mapped to cores | Layers exceed available cores |
| Intermediate activations fit in L1/L2 | Yes | Too large for on-chip storage |
| Weights fit in L1 (static) or can be streamed | Yes | Weights too large even with streaming |
| Need maximum throughput | Yes -- pipeline parallelism | Flexibility more important |
| Development complexity | Higher -- must plan full tile map | Lower -- each op is independent |

**Rule of thumb**: if the total number of concurrent layers times their per-layer L1 budget
(buffers + weights + stack) fits within the available AIE cores and their 64KB each, use dataflow.

---

## 2. Design Patterns from MobileNet

### 2.1 Architecture Overview

MobileNetV3 on the NPU uses a 4-column x 4-row AIE array (Strix: 8 columns x 4 rows of compute
tiles, 8 MemTiles). The design maps 15 bottleneck blocks plus init-conv and post-processing layers
across all 32 compute tiles using three mapping strategies:

- **Bottleneck A** (bn0-bn9): Each bottleneck on a **single core**. Ten bottlenecks chained
  across 10 cores. Each core runs all three layers (1x1 conv, 3x3 dw-conv, 1x1 conv) sequentially
  within its core body, using self-to-self ObjectFIFOs for intermediate results.

- **Bottleneck B** (bn10-bn12): Each bottleneck spread across **3 cores** (one per layer).
  Three bottlenecks chained, using 9 cores total.

- **Bottleneck C** (bn13-bn14): Each bottleneck spread across **5 cores** (partial sum
  splitting with cascade connections). Two bottlenecks using 10 cores.

The data flows: DDR --> InitConv --> bn0 --> bn1 --> ... --> bn9 --> bn10 --> ... --> bn12 -->
bn13 --> bn14 --> PostBlock (AvgPool+FC) --> DDR.

### 2.2 Layer Chaining via ObjectFIFOs

The fundamental pattern is a chain of ObjectFIFOs connecting adjacent layers:

```python
# Init conv output feeds into bn0 input
act_init_bn0 = object_fifo("act_init_bn0", init_tile, bn0_tile, [5, 3], bn0_input_ty)

# bn0 output feeds into bn1 input
act_bn0_bn1 = object_fifo("act_bn0_bn1", bn0_tile, bn1_tile, 2, bn0_output_ty)

# bn1 output feeds into bn2 input
act_bn1_bn2 = object_fifo("act_bn1_bn2", bn1_tile, bn2_tile, 2, bn1_output_ty)

# ... continues for all layers ...

# bn9 output feeds into bn10 input (crossing from Bottleneck-A to Bottleneck-B)
act_bn9_bn10 = object_fifo("act_bn9_bn10", bn8_9_tile, bn10_tile_1, [1, 2], bn8_output_ty)
```

Each ObjectFIFO element is one row of activations: `(width, 1, channels)`. Processing happens
row-by-row, so only a few rows need to be buffered at any time. The depth parameters control
how many elements can be in flight -- typically `[producer_depth, consumer_depth]` where:
- Producer depth controls back-pressure (how many rows the producer can get ahead).
- Consumer depth controls how many rows the consumer can see simultaneously (e.g., 3 for a 3x3
  convolution's sliding window).

**Depth notation**: `[5, 3]` means 5 buffer slots on the producer side (init_tile) and 3 on the
consumer side (bn0_tile). This is critical for sliding window convolutions where the consumer
needs to `acquire(3)` simultaneously.

### 2.3 Single-Core Bottleneck (Bottleneck A Pattern)

When all three layers of a bottleneck fit on one core, intermediate results use **self-to-self
ObjectFIFOs**:

```python
# Self-to-self FIFOs within a single core for intermediate activations
self.of_act_1_2 = object_fifo(
    name + "_act_1_2",
    compute_tile, compute_tile,   # same tile for both producer and consumer
    depth=3,                       # 3 slots for 3x3 sliding window
    element_type=layer1_out_ty
)
self.of_act_2_3 = object_fifo(
    name + "_act_2_3",
    compute_tile, compute_tile,
    depth=1,                       # 1x1 conv only needs current row
    element_type=layer2_out_ty
)
```

The core body runs the three convolution layers in a row-interleaved fashion:

```python
@core(compute_tile)
def core_body():
    for _ in for_(sys.maxsize):  # infinite loop -- hardware runs until reset
        # Layer 1: 1x1 conv (row by row)
        for row in range(H):
            elem_in = act_in.acquire(Consume, 1)
            elem_out = of_act_1_2.acquire(Produce, 1)
            conv2dk1(elem_in, weights_L1, elem_out, W, InC, OutC, scale)
            act_in.release(Consume, 1)
            of_act_1_2.release(Produce, 1)

            # As soon as enough rows accumulated, run Layer 2
            if row >= 1:  # 3x3 conv needs 2+ rows
                rows_2 = of_act_1_2.acquire(Consume, 3)  # sliding window
                out_2 = of_act_2_3.acquire(Produce, 1)
                conv2dk3(rows_2[0], rows_2[1], rows_2[2], weights_L2, out_2, ...)
                of_act_1_2.release(Consume, 1)  # slide window forward
                of_act_2_3.release(Produce, 1)

                # Layer 3: 1x1 conv + skip add
                in_3 = of_act_2_3.acquire(Consume, 1)
                out_3 = act_out.acquire(Produce, 1)
                conv2dk1_skip(in_3, weights_L3, out_3, skip_in, ...)
                of_act_2_3.release(Consume, 1)
                act_out.release(Produce, 1)
```

The actual MobileNet implementation uses `memref_view` to slice a single static weight buffer
into per-layer views, avoiding the need for separate weight FIFOs:

```python
weightsLayer1 = memref_view(weightsAllLayers, [InC * OutC], shift=0)
weightsLayer2 = memref_view(weightsAllLayers, [9 * DwC], shift=InC * OutC)
weightsLayer3 = memref_view(weightsAllLayers, [DwC * OutC], shift=InC * OutC + 9 * DwC)
```

### 2.4 Multi-Core Bottleneck (Bottleneck B Pattern)

When a layer has too many weights for one core, split across three cores (one per conv layer):

```python
# Core 1: 1x1 expansion conv
# Core 2: 3x3 depthwise conv
# Core 3: 1x1 projection conv

# Activation flow: Core1 -> Core2 -> Core3
act_1_2 = object_fifo("act_1_2", core1_tile, core2_tile, [2, 4], layer1_out_ty)
act_2_3 = object_fifo("act_2_3", core2_tile, core3_tile, 2, layer2_out_ty)
```

Bottleneck B in MobileNet maps bn10, bn11, bn12 each across 3 cores (9 cores total), with
inter-bottleneck ObjectFIFOs connecting bn10's last core to bn11's first core, and so on.

### 2.5 Five-Core Split with Cascade (Bottleneck C Pattern)

For very large layers (e.g., 80->960 channel expansion), the 1x1 convolution itself is split
across two cores using the AIE cascade interface:

```python
# Cascade connections for partial-sum accumulation
cascade_flow(bn13_tile_layer1_put, bn13_tile_layer1_get)
cascade_flow(bn13_tile_layer3_put, bn13_tile_layer3_get)
```

The "put" core computes partial sums on half the input channels and sends them via cascade
to the "get" core, which adds its own partial sums and produces the final output. This is
the `InputSplit=2` pattern in MobileNet's Bottleneck C.

### 2.6 Skip Connections via MemTile Buffering

Residual connections require the input to be buffered until the bottleneck's output is ready
for addition. Since the skip path must wait for multiple rows of processing, the data is
buffered in the MemTile's larger L2 memory (512KB):

**IRON API (new style)**:
```python
# Broadcast input to both the first conv and the skip buffer in MemTile
of_inOF_act_L3L2 = ObjectFifo(layer1_in_ty, name="inOF_act_L3L2")
of_skip_buf = of_inOF_act_L3L2.cons(4).forward(
    depth=2, placement=AnyMemTile, name="skip_buf"
)
```

**Legacy API (MobileNet style)**:
```python
# Broadcast to first conv and MemTile for skip buffering
act_B_C = object_fifo(
    "act_B_C",
    bn12_tile,
    [bn13_tile_layer1_put, bn13_tile_layer1_get, MemTile51],
    [2, 2, 2, 6],   # depths: producer=2, consumer0=2, consumer1=2, memtile=6
    input_ty
)
# Link from MemTile to the skip consumer
bn13_skip = object_fifo("bn13_skip", MemTile51, bn13_tile_layer3_get, 2, input_ty)
object_fifo_link(act_B_C, bn13_skip)
```

The key insight: the MemTile depth (6 in this example) must be large enough to buffer all the
rows the skip consumer needs before it can start consuming. For a bottleneck with stride-1, the
consumer processes at about the same rate as the producer, so depth 4-6 suffices. For stride-2,
the consumer produces rows twice as fast as the producer generates them, requiring careful depth
calculation.

---

## 3. Weight Distribution Strategies

### 3.1 Static Weights (Pre-loaded into L1 Buffers)

For layers with small weight tensors that fit in L1, pre-load them as static buffers with
`initial_value`. No DMA streaming needed at runtime:

```python
# Weights baked into the binary as initial buffer contents
wts_array = np.fromfile("bn0_chain.txt", sep=",", dtype=np.int8)
bn0_wts_static = buffer(
    bn0_tile,
    np.ndarray[(weights_size,), np.dtype[np.int8]],
    "bn0_wts_static",
    initial_value=wts_array
)
```

The core accesses these via `memref_view` slicing (no acquire/release needed). This is the
pattern used for Bottleneck A (bn0-bn9) and Bottleneck B (bn10-bn12) in MobileNet.

**Budget**: weights must fit within the core's 64KB L1 alongside activation buffers and stack.
For a bottleneck with InC=80, DwC=184, OutC=80:
- 1x1 weights: 80 * 184 = 14,720 bytes
- 3x3 dw weights: 9 * 184 = 1,656 bytes
- 1x1 weights: 184 * 80 = 14,720 bytes
- Total: ~31KB. Leaves ~33KB for activation double-buffers and stack.

### 3.2 Streamed Weights (via ObjectFIFO from DDR)

When weights are too large for static allocation, stream them from DDR through MemTile:

```python
# DDR -> MemTile -> Core weight streaming
bn13_wts_L3L2_layer1 = object_fifo(
    "bn13_wts_L3L2_layer1",
    ShimTile40,         # from DDR via ShimDMA
    MemTile01,          # buffer in MemTile
    depth=1,
    ty_bneck_13_layer1_wts_full  # full weight tensor type
)
# MemTile -> Core with split for partial weights
bn13_wts_memtile_layer1_put = object_fifo(
    "bn13_wts_memtile_layer1_put",
    MemTile01,
    bn13_tile_layer1_put,
    [1, 1],
    ty_bneck_13_layer1_wts_split  # partial weight type (half of full)
)
bn13_wts_memtile_layer1_get = object_fifo(
    "bn13_wts_memtile_layer1_get",
    MemTile01,
    bn13_tile_layer1_get,
    [1, 1],
    ty_bneck_13_layer1_wts_split
)
# Link: MemTile distributes full tensor to two halves
object_fifo_link(
    bn13_wts_L3L2_layer1,
    [bn13_wts_memtile_layer1_put, bn13_wts_memtile_layer1_get],
    [],
    [0, (InC * OutC) // 2]  # offset for second half
)
# Repeat weights for each row of activations
bn13_wts_memtile_layer1_put.set_repeat_count(num_rows)
bn13_wts_memtile_layer1_get.set_repeat_count(num_rows)
```

The `set_repeat_count()` ensures the weight FIFO automatically re-sends the same weights for each
activation row, without the core needing to re-acquire.

### 3.3 Weight Splitting with ObjectFIFO Split

For the IRON API (bottleneck.py), weights for all three layers are packed into a single DDR
buffer and split in the MemTile:

```python
# Single weight FIFO from DDR
inOF_wts_0_L3L2 = ObjectFifo(weightsAll_ty, depth=1, name="inOF_wts_0_L3L2")

# Split into per-layer weight sub-FIFOs
of_offsets = [0, weightsL1_sz, weightsL1_sz + weightsL2_sz]
wts_L1, wts_L2, wts_L3 = inOF_wts_0_L3L2.cons().split(
    of_offsets,
    obj_types=[weightsLayer1_ty, weightsLayer2_ty, weightsLayer3_ty],
    names=["wts_buf_00", "wts_buf_01", "wts_buf_02"]
)
```

This pattern minimizes ShimDMA channel usage (only one channel for all weights) while delivering
the right weight subset to each core.

### 3.4 Lock-Based Weight Streaming from MemTile

For the post-processing FC layers in MobileNet, weights are stored in MemTile buffers with
explicit lock-based DMA control:

```python
# Pre-loaded MemTile buffer with locks for DMA control
post_L1_wts_prod_lock = lock(MemTile41, lock_id=2, init=0)
post_L1_wts_cons_lock = lock(MemTile41, lock_id=3, init=num_repeats)
post_L1_wts_buff = buffer(
    MemTile41,
    np.ndarray[(wts_size,), np.dtype[np.int8]],
    "post_L1_wts_buff",
    initial_value=wts_array
)

# Custom MemTile DMA program to stream chunks to compute tile
@memtile_dma(MemTile41)
def m(block):
    s0 = dma_start(DMAChannelDir.MM2S, 0, dest=block[1], chain=block[2])
    with block[1]:
        use_lock(post_L1_wts_cons_lock, LockAction.AcquireGreaterEqual)
        dma_bd(post_L1_wts_buff)
        use_lock(post_L1_wts_prod_lock, LockAction.Release)
        next_bd(block[1])  # loop back to re-send
    with block[2]:
        EndOp()
```

The compute tile uses matching locks to synchronize:

```python
use_lock(post_L1_tile_cons_lock, LockAction.AcquireGreaterEqual)
call(kernel_fn, [input, post_L1_tile_buff, output, ...])
use_lock(post_L1_tile_prod_lock, LockAction.Release)
```

---

## 4. Tile Placement Strategies

### 4.1 Snake Pattern for Adjacent Cores

MobileNet uses a snake-like pattern across the 4x8 grid to maximize shared-memory adjacency
between connected cores:

```
Column 0 (bn0-bn2 + init):
  (0,2) init    -- column bottom
  (0,3) bn0     -- data flows UP
  (0,4) bn1
  (0,5) bn2     -- column top

Column 1 (bn3-bn6):
  (1,5) bn10_1  -- column top
  (1,4) bn6     -- data flows DOWN
  (1,3) bn3
  (1,2) bn4_5   -- column bottom (fused bn4+bn5)

Column 2 (bn7-bn9 + bn10/11):
  (2,2) bn11_3
  (2,3) bn7     -- data flows UP again
  (2,4) bn10_2
  (2,5) bn10_3
```

Adjacent cores in the same column share L1 memory banks, enabling zero-latency ObjectFIFO
transfers. The snake pattern ensures that each layer's output core is physically adjacent to the
next layer's input core.

### 4.2 Explicit Placement

In the legacy API, tiles are explicitly assigned:

```python
init_tile = tile(0, 2)
bn0_tile  = tile(0, 3)
bn1_tile  = tile(0, 4)
bn2_tile  = tile(0, 5)
bn3_tile  = tile(1, 3)
# ...
```

In the IRON API, you can either use explicit `Tile(col, row)` placement or let the
`SequentialPlacer` auto-assign:

```python
worker = Worker(fn, args, placement=Tile(0, 3))  # explicit
# or
Program(dev, rt).resolve_program(SequentialPlacer())  # automatic
```

### 4.3 Cross-Column Data Movement

When data must move between columns (e.g., bn2 at (0,5) to bn3 at (1,3)), it routes through the
interconnect fabric. This adds latency compared to same-column transfers, but the ObjectFIFO
abstraction handles it transparently. The depth parameters should be increased (e.g., depth=3-4)
to hide this latency.

### 4.4 MemTile Usage for Buffering

MemTiles (row 1) have 512KB each and serve three purposes in dataflow designs:
1. **Skip connection buffering**: Hold input activations until the skip-add at the end of the block.
2. **Weight staging**: Buffer large weights from DDR before streaming to compute tiles.
3. **Join/split operations**: Merge partial outputs from multiple cores or split inputs for
   distribution.

---

## 5. Memory Budget Planning

### 5.1 L1 Budget Per Core (64KB)

Every compute tile has 64KB of L1. This must hold:
- **Activation input buffers**: double-buffered, so `2 * W * C_in` bytes per row
- **Activation output buffers**: double-buffered, so `2 * W * C_out` bytes per row
- **Intermediate self-to-self FIFO buffers**: for single-core bottlenecks, typically
  `3 * W * C_mid` (3 slots for 3x3 sliding window) + `1 * W * C_mid` (1 slot for 1x1)
- **Static weight buffer**: sum of all layer weights if pre-loaded
- **Stack**: typically 1-2.5KB (`stack_size=0x600` to `0xA00`)

**Example budget for a single-core bottleneck (bn1: InC=16, DwC=64, OutC=24, W=112)**:

| Component | Size |
|---|---|
| Input FIFO (depth=2) | 2 * 112 * 16 = 3,584 |
| 1x1 output FIFO (depth=3, self) | 3 * 112 * 64 = 21,504 |
| 3x3 output FIFO (depth=1, self) | 1 * 112 * 64 = 7,168 |
| Output FIFO (depth=2) | 2 * 112 * 24 = 5,376 |
| Weights (1x1+3x3+1x1) | 16*64 + 9*64 + 64*24 = 2,624 |
| Stack | 1,536 |
| **Total** | **~41.8KB** (fits in 64KB) |

### 5.2 L2 Budget Per MemTile (512KB)

MemTile memory is used for:
- Skip connection buffers (must hold multiple rows)
- Weight staging from DDR
- Activation join/split buffers

**Example**: Skip buffer for a 14x14 feature map with 80 channels:
`6 * 14 * 80 = 6,720 bytes` (6 rows buffered). This is tiny relative to 512KB.

### 5.3 Fusing Layers to Balance the Pipeline

MobileNet fuses adjacent bottlenecks onto single cores when individually they would be too small
to keep the core busy:
- **bn4 + bn5** run on a single core sequentially (bn4_5_tile)
- **bn8 + bn9** run on a single core sequentially (bn8_9_tile)

This trades latency for better core utilization. The combined weights must still fit in L1.

---

## 6. Runtime Sequence for Dataflow Designs

### 6.1 Minimal Host Interaction

In a dataflow design, the host's runtime sequence is remarkably simple:

```python
@runtime_sequence(activationsInL3_ty, weightsInL3_ty, activationsOutL3_ty)
def sequence(inputFromL3, weightsFromL3, outputToL3):
    # 1. Write runtime parameters (scale factors, etc.)
    NpuWriteRTPOp("rtp_init", index=0, value=init_scaleFactor)
    NpuWriteRTPOp("rtp_bn0", index=0, value=bn0_scaleFactor2)
    # ... more RTPs ...

    # 2. Send input activations (single DMA transfer for entire input)
    npu_dma_memcpy_nd(
        metadata="act_in",
        bd_id=0,
        mem=inputFromL3,
        sizes=[1, 1, 1, activationsInSize32b],
    )

    # 3. Send weights to each stage that needs streaming
    npu_dma_memcpy_nd(
        metadata="bn13_wts_L3L2_layer1",
        bd_id=1,
        mem=weightsFromL3,
        offsets=[0, 0, 0, weight_offset],
        sizes=[1, 1, 1, weight_size],
    )

    # 4. Drain the final output
    npu_dma_memcpy_nd(
        metadata="act_out",
        bd_id=3,
        mem=outputToL3,
        sizes=[1, 1, 1, activationsOutSize32b],
    )
    dma_wait("act_out")
```

The cores all run infinite loops (`for _ in for_(sys.maxsize)`) and process data as it arrives.
The host simply provides the input, supplies weights to streaming stages, and waits for the final
output.

### 6.2 IRON API Runtime

With the IRON API, the pattern is similar but uses higher-level abstractions:

```python
rt = Runtime()
with rt.sequence(activationsIn_ty, weightsIn_ty, activationsOut_ty) as (I, W, O):
    # Set runtime parameters
    def set_rtps(rtp_buf):
        rtp_buf[0] = scale_value
    rt.inline_ops(set_rtps, [rtp2])

    # Start all workers (they run their compute loops)
    rt.start(*workers)

    # Fill input and weight FIFOs from DDR
    rt.fill(of_inOF_act_L3L2.prod(), I)
    rt.fill(inOF_wts_0_L3L2.prod(), W)

    # Drain output FIFO to DDR (blocks until complete)
    rt.drain(outOFL2L3.cons(), O, wait=True)
```

### 6.3 Weight Streaming with TensorAccessPattern

For multi-stage weight streaming from a single packed DDR buffer, use TensorAccessPattern
to select the right slice:

```python
from aie.helpers.taplib import TensorAccessPattern

# Send first set of weights (offset 0)
tap = TensorAccessPattern(
    (totalWeights,),
    offset=0,
    sizes=[1, 1, 1, weights_stage1_size],
    strides=[0, 0, 0, 1],
)
rt.fill(wts_fifos[0].prod(), weightsFromL3, tap, placement=Tile(0, 0))

# Send second set of weights (offset after stage 1)
tap = TensorAccessPattern(
    (totalWeights,),
    offset=weights_stage1_size,
    sizes=[1, 1, 1, weights_stage2_size],
    strides=[0, 0, 0, 1],
)
rt.fill(wts_fifos[1].prod(), weightsFromL3, tap, placement=Tile(1, 0))
```

### 6.4 Time-Multiplexing DDR Channels

MobileNet reuses Shim channels by time-multiplexing. The average-pooling output goes through
the Shim, gets read back by a different Shim channel for the FC layer:

```python
# First: drain avg-pool output to DDR scratch space
npu_dma_memcpy_nd(metadata="act_out_post_avgpool_shim", bd_id=1,
    mem=inputFromL3, offsets=[0, 0, 0, activationsOutSize32b], ...)
dma_wait("act_out_post_avgpool_shim")

# Then: feed that DDR region back as input to the FC layer
npu_dma_memcpy_nd(metadata="act_out_post_shim_FC", bd_id=2,
    mem=inputFromL3, offsets=[0, 0, 0, activationsOutSize32b], ...)
```

This is a rare case where data does touch DDR mid-pipeline -- but only for the final FC layer
which has fundamentally different dimensions from the conv pipeline.

---

## 7. Implementation Reference

### 7.1 Complete Single-Core Bottleneck (IRON API)

This is the cleanest pattern, from `bottleneck.py`:

```python
def bottleneck4AIEs():
    # 1. Define types
    tensorLayer1In_ty  = np.ndarray[(W, 1, InC),  np.dtype[np.int8]]
    tensorLayer1Out_ty = np.ndarray[(W, 1, MidC), np.dtype[np.uint8]]
    tensorLayer2Out_ty = np.ndarray[(W, 1, MidC//2), np.dtype[np.uint8]]
    tensorLayer3Out_ty = np.ndarray[(W, 1, OutC), np.dtype[np.uint8]]
    weightsAll_ty      = np.ndarray[(totalWeights,), np.dtype[np.int8]]

    # 2. Define kernels
    conv2dk1 = Kernel("conv2dk1_i8", "conv2dk1.o", [...])
    conv2dk3 = Kernel("conv2dk3_ui8", "conv2dk3.o", [...])
    conv2dk1_skip = Kernel("conv2dk1_skip_i8", "conv2dk1_skip.o", [...])

    # 3. Create ObjectFIFOs for the data pipeline
    of_act_in = ObjectFifo(tensorLayer1In_ty, name="inOF_act_L3L2")

    # Skip connection: forward to MemTile for buffering
    of_skip = of_act_in.cons(4).forward(depth=2, placement=AnyMemTile, name="skip_buf")

    # Weight FIFO (single DDR -> split into 3 sub-FIFOs)
    of_wts = ObjectFifo(weightsAll_ty, depth=1, name="inOF_wts_0_L3L2")
    wts_L1, wts_L2, wts_L3 = of_wts.cons().split(
        [0, wL1_sz, wL1_sz + wL2_sz],
        obj_types=[wL1_ty, wL2_ty, wL3_ty],
        names=["wts_0", "wts_1", "wts_2"]
    )

    # Inter-layer activation FIFOs
    of_act_1_2 = ObjectFifo(tensorLayer1Out_ty, name="act_2_3_5")
    of_act_3_4 = ObjectFifo(tensorLayer2Out_ty, name="act_3_4")
    of_act_5_4 = ObjectFifo(tensorLayer2Out_ty, name="act_5_4")
    of_out     = ObjectFifo(tensorLayer3Out_ty, name="outOFL2L3")

    # 4. Define worker functions
    def worker_conv1(of_wts, of_in, of_out, kernel, rtp, barrier):
        barrier.wait_for_value(1)
        scale = rtp[0]
        w = of_wts.acquire(1)
        for _ in range_(H):
            a = of_in.acquire(1)
            o = of_out.acquire(1)
            kernel(a, w, o, W, InC, MidC, scale)
            of_in.release(1)
            of_out.release(1)
        of_wts.release(1)

    def worker_conv3(of_wts, of_in, of_out, kernel, last_arg):
        w = of_wts.acquire(1)
        # Top row (padding)
        rows = of_in.acquire(2)
        o = of_out.acquire(1)
        kernel(rows[0], rows[0], rows[1], w, o, W, MidC, MidC, 3, 3, 0, scale, last_arg)
        of_out.release(1)
        # Middle rows (sliding window)
        for _ in range_(H - 2):
            rows = of_in.acquire(3)
            o = of_out.acquire(1)
            kernel(rows[0], rows[1], rows[2], w, o, W, MidC, MidC, 3, 3, 1, scale, last_arg)
            of_in.release(1)
            of_out.release(1)
        # Bottom row (padding)
        rows = of_in.acquire(2)
        o = of_out.acquire(1)
        kernel(rows[0], rows[1], rows[1], w, o, W, MidC, MidC, 3, 3, 2, scale, last_arg)
        of_in.release(2)
        of_out.release(1)
        of_wts.release(1)

    # 5. Create workers and place them
    workers = [
        Worker(worker_conv1, [wts_L1.cons(), of_act_in.cons(), of_act_1_2.prod(),
               conv2dk1, rtp2, rtp_barrier]),
        Worker(worker_conv3, [wts_L2.cons(), of_act_1_2.cons(4), of_act_3_4.prod(),
               conv2dk3, 0], placement=Tile(0, 3)),
        Worker(worker_conv3, [wts_L2.cons(), of_act_1_2.cons(4), of_act_5_4.prod(),
               conv2dk3, MidC//2], placement=Tile(0, 5)),
        Worker(worker_conv1_skip, [wts_L3.cons(), of_act_3_4.cons(), of_act_5_4.cons(),
               of_skip.cons(), of_out.prod(), conv2dk1_skip, rtp4, rtp_barrier],
               placement=Tile(0, 4), stack_size=0xA00),
    ]

    # 6. Runtime sequence
    rt = Runtime()
    with rt.sequence(actIn_ty, wtsIn_ty, actOut_ty) as (I, W, O):
        rt.inline_ops(set_rtps, [rtp2, rtp4])
        rt.set_barrier(rtp_barrier, 1)
        rt.start(*workers)
        rt.fill(of_act_in.prod(), I)
        rt.fill(of_wts.prod(), W)
        rt.drain(of_out.cons(), O, wait=True)

    return Program(dev, rt).resolve_program(SequentialPlacer())
```

### 7.2 Multi-Bottleneck Chain (ResNet conv2_x Pattern)

The ResNet example chains three bottleneck blocks across three columns:

```python
# Create per-column FIFOs for each bottleneck stage
act_fifos = []  # Input activation FIFOs (from previous stage or DDR)
for i in range(n_cols):
    act_fifos.append(ObjectFifo(layer1_in_ty[i], name=f"act1_{i}"))
    # Skip connection forwarded through MemTile
    skip_fifos.append(
        act_fifos[-1].cons(4).forward(placement=Tile(i, 1), depth=2, name=f"skip_{i}")
    )

# Output of column i becomes input of column i+1
conv3_out_fifos = [act_fifos[1], act_fifos[2], outOFL2L3]  # chain!

# Workers are created identically per column, just with different FIFOs
for i in range(n_cols):
    Worker(conv1_fn, [wts[i][0].cons(), act_fifos[i].cons(), act2[i].prod(), ...])
    Worker(conv2_fn, [wts[i][1].cons(), act2[i].cons(), act3_1[i].prod(), ...])
    Worker(conv1_skip_fn, [wts[i][2].cons(), act3_1[i].cons(), act3_2[i].cons(),
           conv3_out_fifos[i].prod(), skip_fifos[i].cons(), ...])
    Worker(conv2_fn, [wts[i][1].cons(), act2[i].cons(), act3_2[i].prod(), ...])
```

This is the same bottleneck pattern repeated three times, with the output FIFO of each stage
being the input FIFO of the next. The weight FIFOs use TensorAccessPatterns to index into a
single packed weight buffer.

---

## 8. Adapting for YOLOv8n-Style Architectures

### 8.1 Key Differences from MobileNet

| Aspect | MobileNet V3 | YOLOv8n |
|---|---|---|
| Block type | Inverted bottleneck (expand-dw-project) | C2f block (split-bottleneck-concat) |
| Convolutions | Depthwise separable | Standard 3x3 convolutions |
| Skip connections | Residual add | Concatenation (channel-wise) |
| Output heads | Single classification | 3 detection heads (multi-scale) |
| Data flow | Linear chain | Branching (backbone outputs to neck) |

### 8.2 Mapping C2f Blocks to Dataflow

A C2f block splits channels, processes through bottleneck(s), and concatenates. In dataflow:

1. **Channel Split**: Use ObjectFIFO `split()` to divide input channels into two halves.
   One half passes through, the other goes to the bottleneck sub-block.

2. **Bottleneck Sub-Block**: Map the two 3x3 convolutions onto adjacent cores with inter-core
   ObjectFIFOs, exactly like MobileNet's multi-core pattern.

3. **Concatenation**: Use ObjectFIFO `link()` with offset lists to join multiple producer
   outputs into a single consumer input at the MemTile level:

```python
# Join partial outputs from multiple cores/paths
object_fifo_link(
    [path_a_fifo, path_b_fifo],
    [joined_fifo],
    [0, half_channels * width]  # offsets for concatenation
)
```

### 8.3 Handling Multi-Scale Detection Heads

YOLOv8n has three output heads at different resolutions. In a dataflow design:

- **Option A**: Map all three heads in one PDI, with branching ObjectFIFOs from the backbone.
  Use `object_fifo(src, [dest1, dest2, ...])` to broadcast/split.

- **Option B**: Use separate PDIs for the backbone and each head, if the total exceeds available
  cores. The backbone output goes to DDR, and each head PDI reads from there.

### 8.4 Upsample in Dataflow

YOLOv8n's neck requires upsampling. In a dataflow design, the upsample kernel:
- Acquires 1 input row.
- Produces 2 output rows (for 2x upsample).
- The output ObjectFIFO has 2x the element count, or each element is 2x wider.

The ObjectFIFO `acquire(1)` / `release(1)` on the consumer side, with `acquire(1)` /
`release(1)` on producer but producing 2 rows per input row, works naturally.

### 8.5 Suggested Tile Layout for YOLOv8n

Given a 4-column x 4-row compute array with 3 key resolutions:

```
Column 0-1: Backbone (CBS + C2f blocks, stride-2 convolutions)
  - P3 output (80x80) branches to neck
  - P4 output (40x40) branches to neck
  - P5 output (20x20) feeds into neck

Column 2: Neck (upsample + concatenate + C2f)
  - Upsample P5 -> merge with P4
  - Upsample merged -> merge with P3

Column 3: Detection heads
  - Head at P3 scale (80x80)
  - Head at P4 scale (40x40)
  - Head at P5 scale (20x20)
```

Each transition between columns uses cross-column ObjectFIFOs with adequate depth for
latency hiding.

---

## 9. Common Pitfalls and Solutions

### 9.1 ObjectFIFO Depth Too Small

**Symptom**: Deadlock (ERT_CMD_STATE_TIMEOUT).
**Cause**: Consumer tries to `acquire(N)` but only `depth-1` slots are available (producer has one).
**Fix**: For sliding window `acquire(N)`, set depth >= N+1. For 3x3 conv with `acquire(3)`,
use depth >= 4.

### 9.2 DMA Channel Exhaustion

**Symptom**: `aie.tile op number of input DMA channel exceeded!`
**Cause**: Each compute tile has only 2 input + 2 output DMA channels. Each ObjectFIFO endpoint
consumes one channel.
**Fix**: Combine weight data into a single FIFO and use `memref_view` or `split()`. Use static
buffers instead of streaming for smaller weights.

### 9.3 L1 Overflow

**Symptom**: Compilation error or silent corruption.
**Cause**: Sum of all buffers exceeds 64KB.
**Fix**: Calculate budget carefully. Reduce FIFO depths. Use weight streaming instead of static
buffers. Split across more cores.

### 9.4 Weight-Activation Ordering

**Symptom**: Garbled output.
**Cause**: Core acquires weights and activations in wrong order, or weights are not repeated
correctly.
**Fix**: Always acquire weights first (once, outside the row loop). Use `set_repeat_count()` for
streamed weights. Verify with IRON's `wait_for_value` barrier pattern.

### 9.5 Cross-Block Dimension Mismatch

**Symptom**: Output corruption at block boundaries.
**Cause**: Output type of block N does not match input type of block N+1 (e.g., int8 vs uint8,
or wrong channel count).
**Fix**: Trace the type chain through all ObjectFIFOs. The element type of each connecting
FIFO must match exactly.

### 9.6 Infinite Core Loops

All cores in a dataflow design run `for _ in for_(sys.maxsize)` (legacy) or `for _ in range_(N)`
(IRON). For single-inference designs, `N=1` or `for_(1)` suffices. For continuous inference,
use `sys.maxsize` or `0xFFFFFFFF`. The core blocks on `acquire()` when no data is available and
resumes when new data arrives.

---

## 10. Quick Reference: API Comparison

### Legacy API (aie.dialects)

```python
from aie.dialects.aie import *
from aie.dialects.aiex import *

@device(AIEDevice.npu2)
def device_body():
    t = tile(col, row)
    of = object_fifo("name", src_tile, dst_tile, depth, elem_ty)
    object_fifo_link(of_a, of_b)  # connect FIFOs through MemTile
    buf = buffer(t, ty, "name", initial_value=np_array)

    @core(t)
    def core_body():
        elem = of.acquire(ObjectFifoPort.Consume, 1)
        call(func, [elem, ...])
        of.release(ObjectFifoPort.Consume, 1)

    @runtime_sequence(in_ty, wts_ty, out_ty)
    def sequence(inp, wts, out):
        npu_dma_memcpy_nd(metadata="of_name", mem=inp, sizes=[...])
        dma_wait("of_name")
```

### IRON API (aie.iron)

```python
from aie.iron import Kernel, ObjectFifo, Program, Runtime, Worker, Buffer

kernel = Kernel("func_name", "kernel.o", [arg_types...])
of = ObjectFifo(elem_ty, name="name")
skip = of.cons(N).forward(placement=AnyMemTile, depth=2, name="skip")
wts_a, wts_b = of_wts.cons().split(offsets, obj_types=[...], names=[...])

def worker_fn(of_in, of_out, kern):
    elem = of_in.acquire(1)
    out = of_out.acquire(1)
    kern(elem, out)
    of_in.release(1)
    of_out.release(1)

w = Worker(worker_fn, [of.cons(), of_out.prod(), kernel], placement=Tile(0, 2))

rt = Runtime()
with rt.sequence(in_ty, wts_ty, out_ty) as (I, W, O):
    rt.start(w)
    rt.fill(of.prod(), I)
    rt.drain(of_out.cons(), O, wait=True)

Program(dev, rt).resolve_program(SequentialPlacer())
```

---

## 11. Summary: Building a New Dataflow Design

1. **Enumerate all layers** and their dimensions (H, W, C_in, C_out, kernel_size, stride).

2. **Compute per-layer memory requirements**: weights + activation rows + stack.

3. **Decide mapping**: single-core per block (weights < ~30KB), multi-core per block (weights
   30-64KB), or cascade split (weights > 64KB per layer).

4. **Plan tile placement**: snake pattern for linear chains, branch at MemTiles for parallel paths.

5. **Define ObjectFIFOs**: one per layer-to-layer connection, with depths sized for the consumer's
   acquire pattern (depth >= max_acquire + 1 for sliding windows).

6. **Choose weight strategy**: static buffers for small weights, ObjectFIFO streaming for large
   weights, MemTile pre-load with lock-based DMA for repeated access.

7. **Write core bodies**: infinite loops with acquire-compute-release. Handle pre-amble (first
   row), middle (sliding window), and post-amble (last row) for 3x3 convolutions.

8. **Write runtime sequence**: set RTPs, issue DMA transfers for input/weights/output, wait for
   completion.

9. **Test incrementally**: verify each block standalone before chaining. Use `object_fifo` to DDR
   (ShimTile) to capture intermediate results for debugging.

10. **Optimize**: adjust FIFO depths, fuse under-utilized cores, verify L1 budgets, profile with
    tracing.
