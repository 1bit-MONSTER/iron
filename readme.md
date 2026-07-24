# IRON - CI Summary

## Examples

<details>
<summary>iron/applications/llama_3.2_1b</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_1] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_40] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_1] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_40] | ✅ | - | - | - |

</details>

## Small

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 179.50 | ✅ | 370.00 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 216.02 | ✅ | 319.92 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 214.00 | ✅ | 469.02 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 229.30 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 162.90 | ✅ | 357.46 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 170.38 | ✅ | 419.80 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 170.44 | ✅ | 530.28 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 199.44 | ✅ | 492.68 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 188.20 | ✅ | 495.18 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 222.90 | ✅ | 644.72 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 208.02 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 244.56 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 166.06 | ✅ | 375.74 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 187.26 | ✅ | 461.76 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 175.80 | ✅ | 417.48 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 191.90 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 153.84 | ✅ | 435.94 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 157.72 | ✅ | 709.50 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 185.80 | ✅ | 448.34 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 179.08 | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 149.32 | ✅ | 410.84 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 162.32 | ✅ | 373.02 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 168.30 | ✅ | 368.92 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 184.70 | ✅ | 413.12 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 162.90 | ✅ | 410.34 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 196.60 | ✅ | 788.32 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 197.86 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 204.88 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1] | ✅ | 2362.24 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 234.68 | ✅ | 917.74 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 250.54 | ✅ | 616.14 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 48657.18 | ✅ | 83136.20 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 28594.26 | ✅ | 24937.52 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 7893.34 | - | - |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1] | ✅ | 2180.40 | ✅ | 4671.68 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4] | ✅ | 4030.62 | ✅ | 6039.82 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1] | ✅ | 1605.74 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.20 | ✅ | 0.11 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 11.85 | ✅ | 3.64 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 22.49 | ✅ | 6.13 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 40.36 | ✅ | 10.57 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 42.71 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.31 | ✅ | 3.77 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 23.93 | ✅ | 6.09 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 37.87 | ✅ | 10.91 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 43.36 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 8.98 | ✅ | 1.84 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 0.80 | ✅ | 0.28 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 1.03 | ✅ | 0.46 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 16.12 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 10.98 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 8.00 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 6.04 | ✅ | 1.21 |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 209.94 | ✅ | 336.28 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 202.36 | ✅ | 372.80 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 187.46 | ✅ | 486.84 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 184.46 | ✅ | 395.40 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 178.70 | ✅ | 450.02 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 184.30 | ✅ | 410.78 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 202.48 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 243.18 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 171.66 | ✅ | 466.86 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 174.76 | ✅ | 287.56 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 179.84 | ✅ | 952.52 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 176.76 | ✅ | 430.98 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 158.22 | ✅ | 514.26 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 194.26 | ✅ | 600.86 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 171.44 | ✅ | 394.90 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 187.96 | ✅ | 484.36 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 197.10 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 222.14 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 186.88 | ✅ | 736.60 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 218.46 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 162.26 | ✅ | 458.40 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 170.42 | ✅ | 823.10 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 184.12 | ✅ | 421.74 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 175.16 | ✅ | 531.10 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 199.50 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 213.92 | ✅ | 501.62 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 40748.26 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 163.36 | ✅ | 381.90 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 200.76 | ✅ | 364.22 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 196.34 | ✅ | 329.06 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 197.98 | ✅ | 378.12 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 201.76 | ✅ | 402.54 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 191.16 | ✅ | 438.68 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 187.88 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 199.76 | - | - |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 158.46 | ✅ | 270.44 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 206.32 | ✅ | 475.48 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 159.64 | ✅ | 353.28 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 152.52 | ✅ | 471.52 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 157.00 | ✅ | 340.08 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 177.66 | ✅ | 391.82 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 160.16 | ✅ | 360.52 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 165.26 | ✅ | 460.44 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 154.02 | ✅ | 429.38 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 166.50 | ✅ | 419.96 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 167.10 | ✅ | 511.12 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 179.90 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 179.26 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 160.54 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 202.02 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 180.10 | ✅ | 394.28 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 171.32 | ✅ | 352.82 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 178.62 | ✅ | 443.40 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 213.44 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 181.80 | ✅ | 395.92 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 166.44 | ✅ | 441.64 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 183.20 | ✅ | 493.34 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 198.36 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 194.32 | ✅ | 388.78 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 197.78 | ✅ | 428.38 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 209.72 | ✅ | 392.40 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 204.98 | ✅ | 409.26 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 206.58 | ✅ | 379.54 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 232.74 | ✅ | 549.26 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 206.46 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 279.74 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 200.98 | ✅ | 444.86 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 198.02 | ✅ | 556.62 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 191.12 | ✅ | 705.64 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 212.56 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 195.62 | ✅ | 439.66 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 194.96 | ✅ | 696.50 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 199.00 | ✅ | 796.98 |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 938.03 | ✅ | 15216.24 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1014.38 | ✅ | 10899.98 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False] | ✅ | 2253.15 | ✅ | 22850.01 |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 148.44 | ✅ | 371.98 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 146.92 | ✅ | 445.58 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 154.52 | ✅ | 420.14 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 145.28 | ✅ | 416.58 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 152.58 | ✅ | 436.64 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 186.28 | ✅ | 532.08 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 169.60 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 224.48 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 180.84 | ✅ | 571.60 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 232.78 | ✅ | 1221.64 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 200.68 | ✅ | 669.66 |

</details>

## Extensive

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0] | ✅ | 179.52 | ✅ | 323.84 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0] | ✅ | 153.62 | ✅ | 405.54 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0] | ✅ | 166.88 | ✅ | 423.26 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0] | ✅ | 170.00 | ✅ | 391.80 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0] | ✅ | 173.34 | ✅ | 469.14 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | ✅ | 165.46 | ✅ | 383.48 |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0] | ✅ | 199.10 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0] | ✅ | 202.68 | - | - |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0] | ✅ | 170.84 | ✅ | 315.46 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 158.32 | ✅ | 241.44 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0] | ✅ | 170.18 | ✅ | 420.14 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 160.94 | ✅ | 278.82 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0] | ✅ | 192.38 | ✅ | 378.98 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 174.18 | ✅ | 423.36 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0] | ✅ | 200.78 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 186.28 | - | - |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0] | ✅ | 189.20 | ✅ | 330.10 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | ✅ | 172.56 | ✅ | 656.00 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0] | ✅ | 185.98 | ✅ | 352.76 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0] | ✅ | 193.38 | ✅ | 373.30 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0] | ✅ | 178.20 | ✅ | 384.14 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0] | ✅ | 187.56 | ✅ | 381.72 |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0] | ✅ | 189.14 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0] | ✅ | 219.12 | - | - |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0] | ✅ | 159.30 | ✅ | 405.48 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0] | ✅ | 168.46 | ✅ | 466.82 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0] | ✅ | 167.26 | ✅ | 344.70 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0] | ✅ | 189.02 | ✅ | 602.94 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0] | ✅ | 191.60 | ✅ | 370.78 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0] | ✅ | 179.16 | ✅ | 464.06 |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0] | ✅ | 211.22 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0] | ✅ | 205.42 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32] | ✅ | 155.14 | ✅ | 400.08 |
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32] | ✅ | 142.04 | ✅ | 382.02 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32] | ✅ | 156.90 | ✅ | 403.72 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32] | ✅ | 211.70 | ✅ | 393.32 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32] | ✅ | 167.26 | ✅ | 350.24 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32] | ✅ | 172.76 | ✅ | 469.46 |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32] | ✅ | 195.96 | - | - |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32] | ✅ | 203.46 | - | - |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 167.84 | ✅ | 349.58 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 151.06 | ✅ | 351.40 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 173.56 | ✅ | 259.34 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 191.06 | ✅ | 420.98 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 167.08 | ✅ | 741.52 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 185.44 | ✅ | 472.74 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 186.80 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 236.92 | - | - |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32] | ✅ | 160.30 | ✅ | 865.16 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32] | ✅ | 169.28 | ✅ | 484.22 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32] | ✅ | 181.18 | ✅ | 348.88 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32] | ✅ | 169.88 | ✅ | 384.68 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32] | ✅ | 192.10 | ✅ | 482.68 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32] | ✅ | 223.90 | ✅ | 603.42 |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32] | ✅ | 170.46 | - | - |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32] | ✅ | 232.74 | - | - |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32] | ✅ | 161.64 | ✅ | 417.98 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32] | ✅ | 166.78 | ✅ | 418.26 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32] | ✅ | 160.32 | ✅ | 715.34 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32] | ✅ | 190.34 | ✅ | 311.70 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32] | ✅ | 172.44 | ✅ | 485.06 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32] | ✅ | 194.08 | ✅ | 873.96 |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32] | ✅ | 192.68 | - | - |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32] | ✅ | 199.64 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 161.72 | ✅ | 411.24 |
| test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 161.66 | ✅ | 420.74 |
| test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 165.44 | ✅ | 408.74 |
| test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 179.92 | - | - |
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 175.52 | ✅ | 368.20 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 171.02 | ✅ | 388.72 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 172.16 | ✅ | 488.90 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 189.54 | - | - |
| test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 166.70 | ✅ | 406.22 |
| test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 188.54 | ✅ | 562.66 |
| test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 189.58 | ✅ | 373.38 |
| test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 181.26 | - | - |
| test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192] | ✅ | 209.44 | ✅ | 326.58 |
| test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 172.58 | ✅ | 418.18 |
| test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 151.90 | ✅ | 493.44 |
| test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 205.94 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 171.38 | ✅ | 431.24 |
| test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 197.38 | ✅ | 601.46 |
| test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 181.16 | ✅ | 683.46 |
| test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 195.00 | - | - |
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 161.22 | ✅ | 516.18 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 181.00 | ✅ | 478.56 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 198.58 | ✅ | 450.78 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 241.20 | - | - |
| test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 178.06 | ✅ | 682.52 |
| test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 185.22 | ✅ | 478.48 |
| test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 197.38 | ✅ | 596.64 |
| test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 225.94 | - | - |
| test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 193.86 | ✅ | 372.78 |
| test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 198.48 | ✅ | 451.74 |
| test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 183.50 | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 197.92 | ✅ | 351.16 |
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 167.72 | ✅ | 407.92 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 156.78 | ✅ | 342.24 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 174.54 | ✅ | 574.50 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 166.06 | ✅ | 434.36 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 182.82 | ✅ | 394.38 |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 173.82 | - | - |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 195.66 | - | - |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 154.06 | ✅ | 705.28 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 158.28 | ✅ | 384.78 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 150.32 | ✅ | 409.58 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 166.14 | ✅ | 325.50 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 155.26 | ✅ | 344.34 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 173.24 | ✅ | 418.56 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 177.36 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 188.22 | - | - |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 164.10 | ✅ | 328.76 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 151.38 | ✅ | 457.46 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 166.02 | ✅ | 355.20 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 170.28 | ✅ | 438.64 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 162.50 | ✅ | 308.38 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 173.34 | ✅ | 453.00 |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 173.08 | - | - |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 219.22 | - | - |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 170.58 | ✅ | 447.40 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 161.52 | ✅ | 572.98 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 170.26 | ✅ | 441.88 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 163.50 | ✅ | 449.52 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 193.72 | ✅ | 452.52 |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 197.28 | - | - |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 201.90 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1] | ✅ | 2332.68 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 245.76 | ✅ | 770.86 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 213.64 | ✅ | 729.12 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 48679.28 | ✅ | 82732.08 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1] | ✅ | 118350.20 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 28259.88 | ✅ | 24868.90 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1] | ✅ | 7334.38 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1] | ✅ | 8897.32 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 7732.38 | - | - |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 96466.54 | ✅ | 93766.82 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 103586.80 | ✅ | 97660.06 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 108550.08 | ✅ | 95469.16 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1281.34 | ✅ | 2291.38 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1405.22 | ✅ | 2622.36 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1516.32 | ✅ | 2523.90 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4511.80 | ✅ | 7064.50 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4612.26 | ✅ | 7881.62 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4771.02 | ✅ | 6074.06 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 95765.88 | ✅ | 99236.74 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 102914.40 | ✅ | 98919.30 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 107843.24 | ✅ | 95503.48 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1] | ✅ | 2217.42 | ✅ | 4426.12 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4] | ✅ | 3849.40 | ✅ | 6190.44 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1] | ✅ | 1453.18 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.19 | ✅ | 0.12 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 12.19 | ✅ | 3.54 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 23.44 | ✅ | 6.64 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 40.00 | ✅ | 9.97 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 43.69 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.60 | ✅ | 3.71 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 23.78 | ✅ | 7.15 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 40.17 | ✅ | 11.19 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 43.84 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 8.84 | ✅ | 2.01 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 0.81 | ✅ | 0.27 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 1.15 | ✅ | 0.55 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 14.94 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 11.14 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 8.22 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 5.49 | ✅ | 1.67 |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 188.36 | ✅ | 390.26 |
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 172.90 | ✅ | 423.56 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 184.76 | ✅ | 364.36 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 177.04 | ✅ | 438.06 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 170.62 | ✅ | 363.76 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 196.60 | ✅ | 810.92 |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 231.84 | - | - |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 229.02 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 165.78 | ✅ | 405.78 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 171.26 | ✅ | 394.72 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 188.24 | ✅ | 417.86 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 209.76 | ✅ | 411.44 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 184.94 | ✅ | 442.70 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 211.42 | ✅ | 494.82 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 178.34 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 235.30 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 180.38 | ✅ | 368.36 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 188.30 | ✅ | 469.16 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 174.32 | ✅ | 367.92 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 184.26 | ✅ | 352.36 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 183.68 | ✅ | 428.20 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 231.22 | ✅ | 443.78 |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 211.20 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 306.36 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 197.48 | ✅ | 394.50 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 179.20 | ✅ | 450.94 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 198.72 | ✅ | 457.88 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 192.62 | ✅ | 475.76 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 166.48 | ✅ | 424.64 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 213.16 | ✅ | 433.56 |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 199.44 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 269.62 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 188.44 | ✅ | 340.18 |
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 153.66 | ✅ | 330.78 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 172.92 | ✅ | 352.54 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 153.88 | ✅ | 356.72 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 161.94 | ✅ | 418.58 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 168.98 | ✅ | 435.90 |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01] | ✅ | 199.20 | - | - |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01] | ✅ | 203.28 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 154.52 | ✅ | 352.98 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 161.24 | ✅ | 444.64 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 180.02 | ✅ | 411.00 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 172.58 | ✅ | 318.48 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 144.60 | ✅ | 396.44 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 195.72 | ✅ | 394.26 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 163.14 | ✅ | 393.50 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 173.70 | ✅ | 830.30 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 171.70 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 236.72 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 145.96 | ✅ | 419.80 |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 163.34 | ✅ | 303.96 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 196.78 | ✅ | 791.34 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 161.70 | ✅ | 351.64 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 188.18 | ✅ | 361.50 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 195.72 | ✅ | 417.48 |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 177.20 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 209.86 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 153.48 | ✅ | 517.54 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 162.30 | ✅ | 432.68 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 158.44 | ✅ | 492.96 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 157.14 | ✅ | 375.46 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 178.08 | ✅ | 750.24 |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 170.68 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 193.18 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024] | ✅ | 177.96 | ✅ | 395.90 |
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024] | ✅ | 160.74 | ✅ | 316.50 |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64] | ✅ | 223.86 | - | - |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64] | ✅ | 209.14 | - | - |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512] | ✅ | 168.64 | ✅ | 432.98 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512] | ✅ | 172.88 | ✅ | 371.48 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512] | ✅ | 179.74 | ✅ | 267.20 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512] | ✅ | 175.24 | ✅ | 268.36 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256] | ✅ | 198.40 | ✅ | 393.42 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256] | ✅ | 157.64 | ✅ | 382.06 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256] | ✅ | 166.08 | ✅ | 270.30 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256] | ✅ | 182.74 | ✅ | 365.62 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128] | ✅ | 177.58 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128] | ✅ | 170.18 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128] | ✅ | 173.10 | ✅ | 443.76 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128] | ✅ | 199.92 | ✅ | 516.00 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 172.70 | ✅ | 306.56 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048] | ✅ | 182.38 | ✅ | 288.96 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 207.18 | - | - |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128] | ✅ | 211.30 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 161.70 | ✅ | 473.00 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024] | ✅ | 163.06 | ✅ | 366.36 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 186.90 | ✅ | 303.20 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024] | ✅ | 162.28 | ✅ | 348.96 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 154.30 | ✅ | 384.56 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512] | ✅ | 137.22 | ✅ | 375.72 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 164.38 | ✅ | 399.82 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512] | ✅ | 169.36 | ✅ | 417.42 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 165.96 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256] | ✅ | 169.74 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 159.48 | ✅ | 355.48 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256] | ✅ | 173.22 | ✅ | 409.08 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096] | ✅ | 171.88 | ✅ | 396.34 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096] | ✅ | 169.00 | ✅ | 436.52 |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256] | ✅ | 224.08 | - | - |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256] | ✅ | 186.18 | - | - |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048] | ✅ | 148.60 | ✅ | 305.28 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048] | ✅ | 137.22 | ✅ | 376.24 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048] | ✅ | 173.68 | ✅ | 345.78 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048] | ✅ | 138.54 | ✅ | 405.04 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024] | ✅ | 186.10 | ✅ | 382.00 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024] | ✅ | 168.80 | ✅ | 346.98 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024] | ✅ | 159.68 | ✅ | 412.62 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024] | ✅ | 146.76 | ✅ | 334.66 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512] | ✅ | 181.82 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512] | ✅ | 172.38 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512] | ✅ | 159.62 | ✅ | 424.84 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512] | ✅ | 169.86 | ✅ | 357.50 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192] | ✅ | 143.22 | ✅ | 345.98 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192] | ✅ | 173.56 | ✅ | 396.42 |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512] | ✅ | 235.34 | - | - |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512] | ✅ | 200.08 | - | - |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096] | ✅ | 158.00 | ✅ | 406.90 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096] | ✅ | 162.34 | ✅ | 412.00 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096] | ✅ | 152.96 | ✅ | 334.42 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096] | ✅ | 176.98 | ✅ | 384.64 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048] | ✅ | 172.22 | ✅ | 507.04 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048] | ✅ | 168.74 | ✅ | 490.98 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048] | ✅ | 176.86 | ✅ | 441.36 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048] | ✅ | 166.24 | ✅ | 446.00 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024] | ✅ | 195.92 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024] | ✅ | 177.16 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024] | ✅ | 184.96 | ✅ | 428.10 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024] | ✅ | 182.96 | ✅ | 424.26 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0] | ✅ | 40746.78 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 40851.58 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | 321699.70 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 172.44 | ✅ | 379.12 |
| test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 162.94 | ✅ | 429.62 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 147.60 | ✅ | 415.90 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 193.20 | ✅ | 410.62 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 173.06 | ✅ | 374.88 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 198.72 | ✅ | 442.48 |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 168.46 | - | - |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 209.40 | - | - |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 137.56 | ✅ | 293.58 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 178.80 | ✅ | 471.14 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 189.60 | ✅ | 889.52 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 155.18 | ✅ | 405.80 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 191.72 | ✅ | 472.26 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 187.80 | ✅ | 380.18 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 201.58 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 213.22 | - | - |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 189.06 | ✅ | 311.74 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 202.60 | ✅ | 813.06 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 157.50 | ✅ | 285.98 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 162.40 | ✅ | 491.30 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 182.70 | ✅ | 442.92 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 198.32 | ✅ | 491.50 |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 172.74 | - | - |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 224.46 | - | - |
| test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 203.94 | ✅ | 398.68 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 207.18 | ✅ | 540.96 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 180.24 | ✅ | 469.50 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 183.88 | ✅ | 903.30 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 191.14 | ✅ | 430.50 |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 184.62 | - | - |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 204.84 | - | - |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False] | ✅ | 159.62 | ✅ | 362.78 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True] | ✅ | 147.22 | ✅ | 454.32 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False] | ✅ | 171.10 | ✅ | 400.78 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True] | ✅ | 169.06 | ✅ | 507.28 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False] | ✅ | 164.06 | ✅ | 710.36 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True] | ✅ | 167.18 | ✅ | 611.06 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False] | ✅ | 174.58 | ✅ | 509.58 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True] | ✅ | 172.20 | ✅ | 408.50 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False] | ✅ | 183.78 | ✅ | 438.86 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | ✅ | 163.86 | ✅ | 537.60 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False] | ✅ | 210.80 | ✅ | 748.28 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True] | ✅ | 195.64 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False] | ✅ | 164.12 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 194.00 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False] | ✅ | 212.04 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 155.94 | ✅ | 458.64 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 171.76 | ✅ | 470.76 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 168.08 | ✅ | 340.46 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 196.92 | ✅ | 484.74 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 180.16 | ✅ | 824.90 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 204.16 | ✅ | 538.26 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 182.36 | ✅ | 389.58 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 202.56 | ✅ | 436.96 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 198.16 | ✅ | 401.76 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 194.96 | ✅ | 458.28 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 179.52 | ✅ | 731.80 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 244.88 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 186.10 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 202.76 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 216.78 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False] | ✅ | 171.62 | ✅ | 337.22 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 184.50 | ✅ | 341.92 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False] | ✅ | 185.34 | ✅ | 418.02 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True] | ✅ | 181.54 | ✅ | 441.04 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False] | ✅ | 173.92 | ✅ | 562.92 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True] | ✅ | 190.48 | ✅ | 451.22 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False] | ✅ | 158.36 | ✅ | 732.34 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True] | ✅ | 183.22 | ✅ | 427.28 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False] | ✅ | 153.50 | ✅ | 702.80 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True] | ✅ | 187.82 | ✅ | 393.52 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False] | ✅ | 148.66 | ✅ | 414.20 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True] | ✅ | 189.50 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False] | ✅ | 153.54 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True] | ✅ | 186.44 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False] | ✅ | 180.56 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False] | ✅ | 158.24 | ✅ | 762.76 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False] | ✅ | 158.90 | ✅ | 463.14 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True] | ✅ | 179.96 | ✅ | 461.54 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False] | ✅ | 200.70 | ✅ | 434.68 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True] | ✅ | 186.72 | ✅ | 895.34 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False] | ✅ | 180.22 | ✅ | 354.90 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True] | ✅ | 172.20 | ✅ | 457.38 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False] | ✅ | 163.84 | ✅ | 417.28 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True] | ✅ | 206.88 | ✅ | 479.64 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False] | ✅ | 169.32 | ✅ | 497.62 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True] | ✅ | 194.92 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False] | ✅ | 209.62 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True] | ✅ | 222.56 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False] | ✅ | 177.98 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 150.38 | ✅ | 428.32 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 168.40 | ✅ | 337.22 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 153.80 | ✅ | 356.62 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 153.84 | ✅ | 521.74 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 175.24 | ✅ | 348.56 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 173.66 | ✅ | 373.74 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 204.98 | - | - |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 198.98 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 160.32 | ✅ | 482.30 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 203.02 | ✅ | 410.98 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 157.70 | ✅ | 273.64 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 177.06 | ✅ | 340.92 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 205.02 | ✅ | 421.74 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 159.50 | ✅ | 464.86 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 191.14 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 172.14 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 160.18 | ✅ | 365.78 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 180.42 | ✅ | 374.94 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 153.00 | ✅ | 753.40 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 175.78 | ✅ | 464.66 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 149.26 | ✅ | 654.18 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 169.66 | ✅ | 334.46 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 179.34 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 196.96 | - | - |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 199.96 | ✅ | 400.94 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 189.96 | ✅ | 244.34 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 170.14 | ✅ | 435.78 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 207.28 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 220.70 | ✅ | 429.96 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 165.96 | ✅ | 479.64 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 160.96 | ✅ | 538.36 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 196.54 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 187.32 | ✅ | 457.22 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 188.32 | ✅ | 407.46 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 150.30 | ✅ | 380.90 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 186.38 | ✅ | 691.74 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 218.70 | ✅ | 394.30 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 203.92 | ✅ | 460.78 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 179.50 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 158.80 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 207.90 | ✅ | 356.62 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 173.02 | ✅ | 423.70 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 161.46 | ✅ | 521.12 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 141.92 | ✅ | 397.04 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 198.80 | ✅ | 372.34 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 170.24 | ✅ | 358.64 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 149.68 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 178.04 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 199.40 | ✅ | 484.88 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 182.34 | ✅ | 416.76 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 221.38 | ✅ | 598.90 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 211.46 | ✅ | 345.84 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 202.10 | ✅ | 479.08 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 192.28 | ✅ | 527.54 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 171.46 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 173.48 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 151.56 | ✅ | 397.30 |
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 198.56 | ✅ | 363.28 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 161.10 | ✅ | 323.04 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 155.88 | ✅ | 386.66 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 225.68 | ✅ | 349.74 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 195.48 | ✅ | 379.72 |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 188.38 | - | - |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 218.22 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 170.96 | ✅ | 499.98 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 172.46 | ✅ | 353.90 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 173.32 | ✅ | 826.48 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 192.00 | ✅ | 426.02 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 221.42 | ✅ | 497.98 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 181.42 | ✅ | 423.42 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 187.84 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 192.86 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 175.20 | ✅ | 407.46 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 202.86 | ✅ | 318.30 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 185.42 | ✅ | 303.94 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 177.72 | ✅ | 361.42 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 205.46 | ✅ | 419.26 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 199.40 | ✅ | 486.48 |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 178.18 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 218.10 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 175.20 | ✅ | 514.02 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 205.30 | ✅ | 360.86 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 205.58 | ✅ | 338.80 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 199.78 | ✅ | 772.56 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 194.86 | ✅ | 976.56 |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 187.90 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 185.28 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 174.76 | ✅ | 294.48 |
| test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 157.42 | ✅ | 455.72 |
| test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 179.54 | ✅ | 355.42 |
| test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 203.30 | - | - |
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 191.86 | ✅ | 307.02 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 174.10 | ✅ | 375.10 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 182.84 | ✅ | 419.70 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 191.72 | - | - |
| test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 190.28 | ✅ | 387.58 |
| test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 192.26 | ✅ | 514.18 |
| test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 196.82 | ✅ | 387.80 |
| test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 211.04 | - | - |
| test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 156.68 | ✅ | 750.46 |
| test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 182.38 | ✅ | 423.30 |
| test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 188.96 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 168.76 | ✅ | 594.80 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 196.76 | ✅ | 450.72 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 182.68 | ✅ | 406.38 |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 953.07 | ✅ | 14717.90 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1026.35 | ✅ | 14257.78 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False] | ✅ | 2228.92 | ✅ | 24416.13 |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 164.18 | ✅ | 776.30 |
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 216.82 | ✅ | 783.66 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 172.74 | ✅ | 360.66 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 203.70 | ✅ | 408.10 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 191.86 | ✅ | 618.74 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 192.52 | ✅ | 413.62 |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 217.10 | - | - |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 233.80 | - | - |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 162.44 | ✅ | 325.34 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 176.04 | ✅ | 324.94 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 178.82 | ✅ | 337.74 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 175.76 | ✅ | 415.20 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 178.02 | ✅ | 498.30 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 190.42 | ✅ | 443.00 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 183.90 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 202.38 | - | - |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 166.84 | ✅ | 404.90 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 203.32 | ✅ | 427.92 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 162.76 | ✅ | 485.52 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 166.48 | ✅ | 523.74 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 190.06 | ✅ | 465.60 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 198.64 | ✅ | 434.02 |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 192.36 | - | - |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 212.18 | - | - |
| test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 162.32 | ✅ | 455.48 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 187.26 | ✅ | 586.08 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 171.46 | ✅ | 373.22 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 164.32 | ✅ | 817.12 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 194.78 | ✅ | 508.32 |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 175.48 | - | - |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 220.58 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 247.28 | ✅ | 1624.68 |
| test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 222.66 | ✅ | 1287.82 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 222.54 | ✅ | 1712.76 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 219.10 | ✅ | 597.14 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 257.44 | ✅ | 1027.36 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 277.22 | ✅ | 722.16 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 280.88 | ✅ | 1229.28 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 242.12 | ✅ | 611.10 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 248.90 | ✅ | 1213.90 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 246.68 | ✅ | 535.60 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 349.60 | ✅ | 1530.32 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 367.80 | ✅ | 972.34 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 350.94 | ✅ | 1486.44 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 315.76 | ✅ | 1223.72 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 314.24 | ✅ | 731.44 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 330.80 | ✅ | 612.94 |
| test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 332.32 | - | - |
| test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 317.38 | - | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 198.74 | ✅ | 1100.52 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 229.62 | ✅ | 2367.16 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4] | ✅ | 261.28 | ✅ | 1255.22 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 186.08 | ✅ | 595.84 |
| test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 164.08 | ✅ | 387.88 |
| test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 166.08 | ✅ | 682.44 |
| test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 188.16 | ✅ | 498.50 |
| test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 177.06 | ✅ | 447.08 |
| test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 187.54 | ✅ | 487.92 |
| test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 167.76 | ✅ | 437.68 |
| test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 164.46 | ✅ | 362.30 |
| test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 194.68 | ✅ | 418.88 |
| test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 159.98 | - | - |
| test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 153.70 | ✅ | 678.00 |

</details>

