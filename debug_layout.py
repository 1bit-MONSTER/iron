# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compare our weight/input tiling with upstream DataShaper."""

import torch
import numpy as np
from aie.utils.ml import DataShaper
from iron.operators.conv2d_int8.op import (
    nchw_to_tiled_int8,
    weights_to_tiled_int8,
    tiled_to_nchw_int8,
)

ds = DataShaper()

# Test weight layout
for ic, oc in [(8, 8), (16, 16), (24, 24), (32, 32)]:
    wt = torch.arange(oc * ic, dtype=torch.int8).reshape(oc, ic, 1, 1)

    # Our method
    ours = weights_to_tiled_int8(wt)

    # Upstream DataShaper
    wt_np = wt.data.numpy().astype(np.int8)
    upstream = ds.reorder_mat(wt_np, "OIYXI8O8", "OIYX")
    upstream_flat = np.concatenate((upstream), axis=None).astype(np.int8)

    match = np.array_equal(ours, upstream_flat)
    if not match:
        diff_indices = np.where(ours != upstream_flat)[0]
        print(f"IC={ic:2d} OC={oc:2d}: MISMATCH at {len(diff_indices)} positions")
        for i in diff_indices[:10]:
            print(f"  [{i}] ours={ours[i]} upstream={upstream_flat[i]}")
    else:
        print(f"IC={ic:2d} OC={oc:2d}: weights match ✓")

# Test input layout
print()
for ic, w in [(8, 32), (16, 32), (24, 32), (32, 32)]:
    h = 1
    x = torch.arange(ic * h * w, dtype=torch.int8).reshape(1, ic, h, w)

    # Our method
    ours = nchw_to_tiled_int8(x)

    # Upstream DataShaper
    x_np = x.squeeze().data.numpy().astype(np.int8)
    upstream = ds.reorder_mat(x_np, "YCXC8", "CYX")
    upstream_flat = upstream.flatten().astype(np.int8)

    match = np.array_equal(ours, upstream_flat)
    if not match:
        diff_indices = np.where(ours != upstream_flat)[0]
        print(f"IC={ic:2d} W={w:3d}: input MISMATCH at {len(diff_indices)} positions")
        for i in diff_indices[:10]:
            print(f"  [{i}] ours={ours[i]} upstream={upstream_flat[i]}")
    else:
        print(f"IC={ic:2d} W={w:3d}: inputs match ✓")
