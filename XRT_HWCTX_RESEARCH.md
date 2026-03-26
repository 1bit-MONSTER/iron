# XRT / xdna-driver Hardware Context & PDI Limits Research

## Executive Summary

The `CONFIG_HWCTX EINVAL` error when loading 44 PDIs is caused by **`MAX_NUM_CUS = 32`** — the firmware message protocol limits each hardware context to **32 CUs (PDIs) maximum**. This is a firmware protocol limit, not a driver or xclbin format limit.

- **29 PDIs works** because 29 ≤ 32
- **44 PDIs fails** because 44 > 32

## Key Limits Found

### 1. MAX CUs per Hardware Context: **32**

**Source**: `xdna-driver/src/driver/amdxdna/aie2_msg_priv.h:351`
```c
#define MAX_NUM_CUS    32
```

The firmware message `config_cu_req` has a fixed-size array:
```c
struct config_cu_req {
    u32 num_cus;
    u32 cfgs[MAX_NUM_CUS];   // Only 32 slots!
};
```

When `ctx->cus->num_cus > MAX_NUM_CUS`, the driver returns `-EINVAL`:
```c
// aie2_message.c:884
if (ctx->cus->num_cus > MAX_NUM_CUS) {
    XDNA_DBG(xdna, "Exceed maximum CU %d", MAX_NUM_CUS);
    return -EINVAL;
}
```

**This is the exact cause of the CONFIG_HWCTX EINVAL error.**

Each kernel in the xclbin maps to one CU. Each CU has one PDI. So xclbin kernels = CUs = PDIs, and the limit is 32.

### 2. MAX Hardware Contexts (per chip)

| NPU Generation | Chip | Device ID | `hwctx_limit` | `ctx_limit` |
|---|---|---|---|---|
| NPU1 | Phoenix | 0x1502 | **6** | 6 |
| NPU4 | Strix Point | 0x17f0 rev 10 | **16** | 32 |
| NPU5 | Strix Halo | 0x17f0 rev 11 | **16** | 32 |
| NPU6 | Krackan | 0x17f0 rev 20 | **16** | 32 |
| NPU3 | (UMQ, VE2 driver) | 0x17f1 | **255** | 255 |

**Source**: `npu1_regs.c:82`, `npu4_family.h:82`, `ve2_regs.c:11`

- `hwctx_limit`: Max **concurrent** hardware contexts the NPU firmware can schedule simultaneously
- `ctx_limit`: Max **virtual** contexts — contexts beyond `hwctx_limit` are time-shared via the partition runqueue (context switching)

**Our system**: `RyzenAI-npu4` (Strix Point, 0x17f0 rev 10) → **16 concurrent hw contexts, 32 virtual contexts**

### 3. MAX PDI IDs System-wide: **255**

**Source**: `aie2_msg_priv.h:615`
```c
#define AIE2_MAX_PDI_ID    255
```

PDI IDs are allocated globally across ALL contexts using `ida_alloc_range(&xdna->pdi_ida, 0, AIE2_MAX_PDI_ID, GFP_KERNEL)`. This means:
- Across all hw_contexts combined, at most 256 PDIs (IDs 0-255) can be registered
- Each CU in each context consumes one PDI ID
- If you have 16 contexts × 32 CUs each = 512 potential PDIs, but only 256 IDs available

### 4. Partition & Context Scheduling

The NPU4 family uses `temporal_only = 1`, meaning all contexts share all columns via temporal multiplexing (context switching). The partition system divides `hwctx_limit` across partitions:

```c
// aie2_ctx_runqueue.c:583
part->max_hwctx = rq->hwctx_limit / rq->num_parts;
```

With `temporal_only`, there's typically one partition using all columns.

## How CUs Map to PDIs

The XRT shim parses the xclbin to extract CUs:

```cpp
// shim/hwctx.cpp:23-38
for (const auto& k : xclbin.get_kernels()) {
    for (const auto& cu : k.get_cus()) {
        m_cus.push_back({
            .m_name = cu.get_name(),
            .m_func = props.functional,
            .m_pdi = get_pdi(aie_partition, props.kernel_id)
        });
    }
}
```

Each xclbin kernel with a unique `kernel_id` maps to one CU, which has one PDI (partial device image). The `config_cu` message sends all CU configs to firmware in one message, limited to `MAX_NUM_CUS = 32`.

## Configuration Options

### Module Parameters (can be set at load time or via sysfs)

| Parameter | Description | Current Value | File |
|---|---|---|---|
| `hwctx_limit` | Override max hw contexts (0 = use default) | 0 (default=16) | `/sys/module/amdxdna/parameters/aie2_max_col` |
| `context_limit` | Override max virtual contexts | 0 (default=32) | N/A |

**Cannot override `MAX_NUM_CUS`** — it's a compile-time constant in the firmware message protocol. Changing it requires recompiling the driver AND matching firmware.

### How to Check Current Limits
```bash
# Module parameters
cat /sys/module/amdxdna/parameters/aie2_max_col
cat /sys/module/amdxdna/parameters/force_cmdlist

# System info
xrt-smi examine  # Shows NPU variant and firmware version

# Kernel debug messages (if enabled)
dmesg | grep -i "hwctx_limit\|context_limit\|Maximum limit"
```

## Implications for YOLOv8n Full Model

### The Problem
- Full YOLOv8n has 68+ operators
- Even with multi-PDI xclbins, we need more than 32 CUs per context
- 44 PDIs in one xclbin fails because 44 > 32

### Solutions

1. **Multiple hw_contexts** (current approach): Split into ≤32 CUs per context
   - We have 16 concurrent hw_contexts available
   - Each can hold up to 32 CUs
   - Total: 16 × 32 = 512 CUs (limited to 256 by PDI ID space)
   - **Caveat**: Context switching overhead between hw_contexts

2. **Runlist execution** (if supported): Submit multi-context runlists
   - Some NPU4 firmware versions support `force_cmdlist` mode
   - Allows chaining multiple contexts in one execution

3. **CU reuse via `cu_func`**: Multiple kernels can share the same PDI
   - If operators use the same column layout, they can share a PDI
   - Different `cu_func` values select different entry points within the same PDI
   - This requires the xclbin to be structured with shared PDIs

4. **Reduce operator count**: Fuse operations to get under 32 per context
   - Combine conv+bn+relu into single fused operators
   - Group sequential operations that use the same tile layout

## Source Code References

| File | Key Contents |
|---|---|
| `aie2_msg_priv.h:351` | `MAX_NUM_CUS = 32` definition |
| `aie2_msg_priv.h:615` | `AIE2_MAX_PDI_ID = 255` definition |
| `aie2_message.c:868-928` | `aie2_config_cu()` — the EINVAL check |
| `aie2_message.c:1595-1684` | `aie2_register_pdis()` — PDI registration |
| `aie2_ctx_runqueue.c:1191-1250` | `aie2_rq_init()` — hwctx_limit initialization |
| `npu4_family.h:82-83` | NPU4 hwctx_limit=16, ctx_limit=32 |
| `npu1_regs.c:82-83` | NPU1 hwctx_limit=6, ctx_limit=6 |
| `shim/hwctx.cpp:15-45` | xclbin → CU parsing |
| `shim/kmq/hwctx.cpp:24-57` | CU config → CONFIG_HWCTX ioctl |
| `amdxdna_ctx.c:200-261` | `config_hwctx_ioctl()` — IOCTL entry point |

## Summary Table

| Limit | Value | Scope | Configurable? |
|---|---|---|---|
| CUs per hw_context | **32** | Per context | No (firmware protocol) |
| PDI IDs system-wide | **256** (0-255) | Global | No (firmware protocol) |
| Concurrent hw_contexts (NPU4) | **16** | Per device | Yes (module param) |
| Virtual contexts (NPU4) | **32** | Per device | Yes (module param) |
| Concurrent hw_contexts (NPU1) | **6** | Per device | Yes (module param) |
