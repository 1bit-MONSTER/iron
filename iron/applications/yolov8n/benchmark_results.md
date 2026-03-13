# YOLOv8n Operator Benchmark Results

- Iterations per config: 10 (+ 1 warmup)
- Timing: wall-clock including layout conversion + DMA sync

| Operator | Compile (s) | Mean (us) | Min (us) | Max (us) |
|----------|-------------|-----------|----------|----------|
| Conv2d k1s1 32->32 @ 32x32 | 0.7 | 346.0 | 322.5 | 399.8 |
| Conv2d k1s1 64->64 @ 16x16 | 0.6 | 240.3 | 217.1 | 262.4 |
| Conv2d k1s1 128->128 @ 8x8 | 0.6 | 325.0 | 244.7 | 638.9 |
| Conv2d k1s1 32->64 @ 16x16 | 0.6 | 255.9 | 206.7 | 476.0 |
| Conv2d k1s1 64->32 @ 16x16 | 0.6 | 192.3 | 171.3 | 216.5 |
| Conv2d k3s1 16->16 @ 8x8 | 0.6 | 4678.1 | 4646.0 | 4718.7 |
| Conv2d k3s1 32->32 @ 8x8 | 0.7 | 18341.3 | 18059.3 | 18511.1 |
| Conv2d k3s1 16->16 @ 16x16 | 0.7 | 19498.2 | 19294.3 | 19719.1 |
| Conv2d k3s1 32->32 @ 16x16 | 0.7 | 76163.0 | 75954.6 | 76449.2 |
| Conv2d k3s2 8->16 @ 16x16 | 0.7 | 2330.3 | 2294.7 | 2382.6 |
| Conv2d k3s2 16->32 @ 8x8 | 0.6 | 2263.9 | 2153.0 | 2490.1 |
| Conv2d k3s2 8->8 @ 8x8 | 0.6 | 371.5 | 363.1 | 406.6 |
| MaxPool2d k5 128ch @ 8x8 | 2.9 | 3906.5 | 3865.7 | 3979.9 |
| MaxPool2d k5 16ch @ 8x8 | 0.6 | 596.4 | 578.9 | 667.4 |
| Upsample 2x 128ch @ 8x8 | 0.6 | 190.0 | 164.5 | 224.3 |
| Upsample 2x 32ch @ 8x8 | 0.6 | 128.3 | 113.6 | 207.6 |
| CBS k3s1 16->16 @ 8x8 | 0.0 | 4767.0 | 4640.5 | 4934.9 |
| Bottleneck 16ch @ 8x8 | 0.0 | 9448.4 | 9284.1 | 9731.3 |

## Configs that failed to compile

These YOLOv8n-scale configs exceed the DMA BD size limit (1023 elements per dimension) and require design-level decomposition:

- **Conv2d k1 64->64 @ 80x80**: row_size=64*80=5120 > 1023
- **Conv2d k1 128->128 @ 40x40**: row_size=128*40=5120 > 1023
- **Conv2d k3 32->64 @ 160x160**: row_size=32*160=5120 > 1023
