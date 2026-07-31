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
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 167.08 | ✅ | 420.68 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 146.52 | ✅ | 444.76 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 181.46 | ✅ | 354.10 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 204.38 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 186.76 | ✅ | 316.24 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 172.42 | ✅ | 340.38 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 168.82 | ✅ | 323.84 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 169.80 | ✅ | 455.02 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 163.88 | ✅ | 645.36 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 159.38 | ✅ | 357.66 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 176.78 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 219.28 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 191.62 | ✅ | 412.76 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 182.60 | ✅ | 465.28 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 185.40 | ✅ | 470.56 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 205.90 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 157.02 | ✅ | 275.00 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 154.14 | ✅ | 311.08 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 207.14 | ✅ | 349.66 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 195.94 | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 155.44 | ✅ | 380.32 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 166.02 | ✅ | 406.40 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 172.84 | ✅ | 371.80 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 166.44 | ✅ | 374.30 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 167.24 | ✅ | 458.00 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 203.66 | ✅ | 453.72 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 180.62 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 198.78 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1] | ✅ | 2218.30 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 255.28 | ✅ | 481.18 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 241.60 | ✅ | 968.62 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 48607.94 | ✅ | 82955.38 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 28386.06 | ✅ | 24888.94 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 7763.48 | - | - |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1] | ✅ | 2178.38 | ✅ | 4986.06 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4] | ✅ | 3856.08 | ✅ | 5997.28 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1] | ✅ | 1368.88 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.21 | ✅ | 0.09 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 13.23 | ✅ | 3.63 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 24.30 | ✅ | 6.18 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 39.10 | ✅ | 8.49 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 42.93 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.67 | ✅ | 3.68 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 24.45 | ✅ | 6.01 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 39.51 | ✅ | 8.59 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 40.95 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 8.74 | ✅ | 1.77 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 0.80 | ✅ | 0.27 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 1.17 | ✅ | 0.62 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 15.25 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 11.86 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 7.30 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 6.02 | ✅ | 2.14 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.17 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 12.77 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.60 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 187.36 | ✅ | 912.72 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 178.90 | ✅ | 340.96 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 172.80 | ✅ | 407.08 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 185.12 | ✅ | 393.36 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 171.66 | ✅ | 1180.90 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 217.50 | ✅ | 478.44 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 210.98 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 224.78 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 186.02 | ✅ | 351.74 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 182.94 | ✅ | 399.26 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 176.62 | ✅ | 434.78 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 224.38 | ✅ | 321.22 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 194.94 | ✅ | 699.36 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 186.36 | ✅ | 456.78 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 187.70 | ✅ | 439.08 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 213.06 | ✅ | 604.96 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 249.78 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 251.22 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 168.12 | ✅ | 360.26 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 210.24 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 192.10 | ✅ | 379.36 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 175.76 | ✅ | 514.04 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 163.18 | ✅ | 587.00 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 181.56 | ✅ | 521.62 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 195.96 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 188.92 | ✅ | 470.18 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 40836.80 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 161.40 | ✅ | 319.56 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 165.90 | ✅ | 334.74 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 169.80 | ✅ | 294.52 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 177.26 | ✅ | 453.64 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 182.94 | ✅ | 425.04 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 186.20 | ✅ | 428.68 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 184.40 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 210.40 | - | - |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 165.18 | ✅ | 344.28 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 160.04 | ✅ | 330.42 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 180.68 | ✅ | 401.52 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 175.50 | ✅ | 550.98 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 168.38 | ✅ | 365.28 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 193.84 | ✅ | 352.34 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 175.02 | ✅ | 586.94 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 186.30 | ✅ | 504.48 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 178.96 | ✅ | 380.16 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 178.58 | ✅ | 615.98 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 170.92 | ✅ | 464.22 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 194.82 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 197.18 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 194.44 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 255.32 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 195.06 | ✅ | 302.48 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 177.40 | ✅ | 435.68 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 168.42 | ✅ | 577.30 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 179.14 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 167.52 | ✅ | 336.22 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 164.16 | ✅ | 374.20 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 169.02 | ✅ | 437.02 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 185.52 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 163.28 | ✅ | 320.84 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 191.30 | ✅ | 687.72 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 192.34 | ✅ | 390.20 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 172.98 | ✅ | 539.86 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 163.18 | ✅ | 663.02 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 192.06 | ✅ | 501.98 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 186.68 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 237.96 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 185.56 | ✅ | 413.94 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 165.44 | ✅ | 362.20 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 174.40 | ✅ | 384.44 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 194.92 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 175.62 | ✅ | 460.02 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 176.08 | ✅ | 442.70 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 184.74 | ✅ | 785.22 |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 982.05 | ✅ | 13935.32 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1020.83 | ✅ | 12485.75 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False] | ✅ | 2253.67 | ✅ | 21642.72 |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 166.96 | ✅ | 324.14 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 210.72 | ✅ | 438.50 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 191.34 | ✅ | 467.38 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 194.30 | ✅ | 398.36 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 180.78 | ✅ | 445.90 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 226.04 | ✅ | 532.30 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 205.74 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 253.74 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 171.22 | ✅ | 402.62 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 219.36 | ✅ | 1116.82 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 187.84 | ✅ | 484.90 |

</details>

## Extensive

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0] | ✅ | 166.38 | ✅ | 397.96 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0] | ✅ | 158.36 | ✅ | 427.02 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0] | ✅ | 160.12 | ✅ | 347.82 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0] | ✅ | 154.42 | ✅ | 360.80 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0] | ✅ | 177.18 | ✅ | 458.36 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | ✅ | 173.88 | ✅ | 284.30 |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0] | ✅ | 186.06 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0] | ✅ | 190.92 | - | - |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0] | ✅ | 165.62 | ✅ | 229.44 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 155.30 | ✅ | 343.84 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0] | ✅ | 155.70 | ✅ | 401.00 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 197.28 | ✅ | 384.28 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0] | ✅ | 162.78 | ✅ | 384.98 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 157.08 | ✅ | 735.36 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0] | ✅ | 174.38 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 223.50 | - | - |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0] | ✅ | 166.34 | ✅ | 319.82 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | ✅ | 168.50 | ✅ | 328.40 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0] | ✅ | 179.78 | ✅ | 646.34 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0] | ✅ | 180.66 | ✅ | 449.74 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0] | ✅ | 185.08 | ✅ | 521.44 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0] | ✅ | 202.58 | ✅ | 338.20 |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0] | ✅ | 176.24 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0] | ✅ | 200.42 | - | - |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0] | ✅ | 146.50 | ✅ | 319.62 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0] | ✅ | 154.56 | ✅ | 303.34 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0] | ✅ | 184.32 | ✅ | 320.88 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0] | ✅ | 170.70 | ✅ | 664.44 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0] | ✅ | 179.96 | ✅ | 480.34 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0] | ✅ | 178.54 | ✅ | 423.82 |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0] | ✅ | 188.30 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0] | ✅ | 209.72 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32] | ✅ | 144.34 | ✅ | 308.58 |
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32] | ✅ | 161.40 | ✅ | 479.98 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32] | ✅ | 154.24 | ✅ | 345.48 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32] | ✅ | 165.00 | ✅ | 376.02 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32] | ✅ | 161.84 | ✅ | 763.66 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32] | ✅ | 179.00 | ✅ | 410.42 |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32] | ✅ | 174.76 | - | - |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32] | ✅ | 269.14 | - | - |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 159.72 | ✅ | 362.12 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 172.42 | ✅ | 298.66 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 162.26 | ✅ | 254.28 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 174.82 | ✅ | 742.18 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 168.18 | ✅ | 514.10 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 176.28 | ✅ | 587.54 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 176.24 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 200.74 | - | - |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32] | ✅ | 150.16 | ✅ | 334.90 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32] | ✅ | 151.68 | ✅ | 426.72 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32] | ✅ | 145.54 | ✅ | 429.32 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32] | ✅ | 138.84 | ✅ | 460.86 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32] | ✅ | 130.64 | ✅ | 815.94 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32] | ✅ | 151.74 | ✅ | 691.70 |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32] | ✅ | 166.56 | - | - |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32] | ✅ | 191.44 | - | - |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32] | ✅ | 144.40 | ✅ | 454.88 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32] | ✅ | 154.06 | ✅ | 327.26 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32] | ✅ | 169.42 | ✅ | 824.02 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32] | ✅ | 189.98 | ✅ | 386.08 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32] | ✅ | 161.12 | ✅ | 410.70 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32] | ✅ | 171.48 | ✅ | 441.42 |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32] | ✅ | 161.68 | - | - |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32] | ✅ | 199.24 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 169.04 | ✅ | 348.94 |
| test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 166.74 | ✅ | 431.18 |
| test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 186.66 | ✅ | 549.26 |
| test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 221.54 | - | - |
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 186.26 | ✅ | 385.68 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 189.34 | ✅ | 386.64 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 177.12 | ✅ | 432.66 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 187.02 | - | - |
| test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 194.64 | ✅ | 390.82 |
| test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 189.58 | ✅ | 445.52 |
| test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 209.88 | ✅ | 661.06 |
| test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 205.48 | - | - |
| test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192] | ✅ | 183.96 | ✅ | 412.88 |
| test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 191.16 | ✅ | 427.18 |
| test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 193.32 | ✅ | 459.14 |
| test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 196.78 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 194.08 | ✅ | 370.20 |
| test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 170.86 | ✅ | 440.30 |
| test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 183.46 | ✅ | 391.56 |
| test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 205.34 | - | - |
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 172.06 | ✅ | 377.94 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 173.66 | ✅ | 312.56 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 172.92 | ✅ | 311.94 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 181.32 | - | - |
| test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 153.32 | ✅ | 287.66 |
| test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 173.92 | ✅ | 378.72 |
| test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 184.86 | ✅ | 394.64 |
| test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 199.30 | - | - |
| test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 184.30 | ✅ | 330.56 |
| test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 170.14 | ✅ | 337.86 |
| test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 215.56 | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 148.78 | ✅ | 259.82 |
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 183.70 | ✅ | 287.44 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 161.04 | ✅ | 491.52 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 166.48 | ✅ | 818.12 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 165.52 | ✅ | 376.72 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 177.60 | ✅ | 507.98 |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 169.84 | - | - |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 190.50 | - | - |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 157.34 | ✅ | 349.62 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 198.08 | ✅ | 687.72 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 178.88 | ✅ | 774.18 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 173.06 | ✅ | 475.06 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 214.66 | ✅ | 394.98 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 222.64 | ✅ | 468.34 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 166.84 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 229.08 | - | - |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 162.76 | ✅ | 324.74 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 171.90 | ✅ | 545.66 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 164.26 | ✅ | 411.14 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 156.20 | ✅ | 342.58 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 168.30 | ✅ | 393.82 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 183.16 | ✅ | 468.20 |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 188.14 | - | - |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 189.58 | - | - |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | - | - | ✅ | 337.78 |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 162.12 | ✅ | 758.88 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 172.98 | ✅ | 346.32 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 167.82 | ✅ | 453.68 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 153.82 | ✅ | 366.00 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 169.70 | ✅ | 456.20 |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 206.58 | - | - |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 208.42 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1] | ✅ | 2219.16 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 201.72 | ✅ | 460.38 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 202.62 | ✅ | 532.06 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 48709.56 | ✅ | 81709.36 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1] | ✅ | 117809.10 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 28381.98 | ✅ | 24723.36 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1] | ✅ | 7453.58 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1] | ✅ | 8919.30 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 7898.20 | - | - |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 96500.66 | ✅ | 94128.12 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 103726.50 | ✅ | 100273.96 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 108698.66 | ✅ | 94860.02 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1298.46 | ✅ | 2279.14 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1430.68 | ✅ | 3433.54 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1452.64 | ✅ | 2265.78 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4586.20 | ✅ | 7852.72 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4613.84 | ✅ | 7123.04 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4871.06 | ✅ | 6715.78 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 95747.94 | ✅ | 99461.72 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 102918.70 | ✅ | 100277.20 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 107849.78 | ✅ | 94023.98 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1] | ✅ | 2201.48 | ✅ | 3065.24 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4] | ✅ | 3513.42 | ✅ | 5874.48 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1] | ✅ | 1412.56 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.18 | ✅ | 0.08 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 13.17 | ✅ | 3.60 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 24.16 | ✅ | 6.04 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 39.06 | ✅ | 10.25 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 44.21 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.66 | ✅ | 3.73 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 24.46 | ✅ | 6.40 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 40.61 | ✅ | 9.47 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 43.37 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 8.78 | ✅ | 1.96 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 0.83 | ✅ | 0.29 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 0.86 | ✅ | 0.62 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 14.36 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 12.10 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 7.19 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 5.78 | ✅ | 1.46 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.23 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 12.86 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.12 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 158.62 | ✅ | 359.36 |
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 171.12 | ✅ | 462.12 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 168.34 | ✅ | 522.20 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 179.28 | ✅ | 511.60 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 159.20 | ✅ | 406.82 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 184.84 | ✅ | 510.80 |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 207.92 | - | - |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 205.72 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 194.84 | ✅ | 355.38 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 182.08 | ✅ | 375.90 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 195.36 | ✅ | 412.82 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 187.76 | ✅ | 525.80 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 181.14 | ✅ | 404.72 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 201.50 | ✅ | 524.44 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 196.66 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 222.48 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 204.92 | ✅ | 409.70 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 188.90 | ✅ | 371.44 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 190.42 | ✅ | 781.84 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 189.56 | ✅ | 488.02 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 166.80 | ✅ | 538.94 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 204.40 | ✅ | 471.26 |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 196.28 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 215.92 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 182.18 | ✅ | 377.82 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 175.48 | ✅ | 603.22 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 173.82 | ✅ | 662.44 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 155.12 | ✅ | 422.42 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 197.90 | ✅ | 498.72 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 216.50 | ✅ | 506.38 |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 233.54 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 232.52 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 165.12 | ✅ | 299.40 |
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 164.84 | ✅ | 327.48 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 174.00 | ✅ | 462.28 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 197.74 | ✅ | 390.18 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 168.92 | ✅ | 370.76 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 177.04 | ✅ | 360.78 |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01] | ✅ | 210.12 | - | - |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01] | ✅ | 191.58 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 157.56 | ✅ | 342.56 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 175.26 | ✅ | 394.40 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 145.30 | ✅ | 293.74 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 160.08 | ✅ | 293.10 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 180.22 | ✅ | 298.38 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 197.94 | ✅ | 411.80 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 181.88 | ✅ | 301.84 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 191.18 | ✅ | 389.48 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 177.40 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 211.20 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 168.66 | ✅ | 406.66 |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 168.66 | ✅ | 389.48 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 179.58 | ✅ | 331.60 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 171.20 | ✅ | 438.46 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 163.88 | ✅ | 474.18 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 184.26 | ✅ | 368.22 |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 199.02 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 210.70 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 169.54 | ✅ | 464.08 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 167.48 | ✅ | 383.24 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 151.60 | ✅ | 485.88 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 182.76 | ✅ | 419.96 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 193.90 | ✅ | 475.00 |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 196.56 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 217.88 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024] | ✅ | 155.34 | ✅ | 626.88 |
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024] | ✅ | 156.62 | ✅ | 414.46 |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64] | ✅ | 220.74 | - | - |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64] | ✅ | 198.38 | - | - |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512] | ✅ | 152.90 | ✅ | 357.46 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512] | ✅ | 158.62 | ✅ | 690.62 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512] | ✅ | 175.90 | ✅ | 441.54 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512] | ✅ | 169.10 | ✅ | 752.30 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256] | ✅ | 174.50 | ✅ | 840.96 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256] | ✅ | 167.52 | ✅ | 367.76 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256] | ✅ | 210.96 | ✅ | 732.44 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256] | ✅ | 161.08 | ✅ | 301.24 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128] | ✅ | 172.68 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128] | ✅ | 182.94 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128] | ✅ | 182.08 | ✅ | 466.50 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128] | ✅ | 184.82 | ✅ | 304.58 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 174.72 | ✅ | 374.20 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048] | ✅ | 169.96 | ✅ | 280.80 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 233.66 | - | - |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128] | ✅ | 191.58 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 152.68 | ✅ | 295.84 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024] | ✅ | 161.30 | ✅ | 420.40 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 154.06 | ✅ | 351.42 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024] | ✅ | 161.58 | ✅ | 364.22 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 171.46 | ✅ | 471.14 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512] | ✅ | 164.92 | ✅ | 381.78 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 159.20 | ✅ | 470.52 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512] | ✅ | 169.56 | ✅ | 393.40 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 209.80 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256] | ✅ | 158.80 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 165.46 | ✅ | 450.68 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256] | ✅ | 146.56 | ✅ | 484.20 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096] | ✅ | 177.10 | ✅ | 412.98 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096] | ✅ | 174.38 | ✅ | 443.36 |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256] | ✅ | 178.68 | - | - |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256] | ✅ | 188.66 | - | - |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048] | ✅ | 171.72 | ✅ | 422.40 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048] | ✅ | 203.18 | ✅ | 435.18 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048] | ✅ | 156.42 | ✅ | 358.04 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048] | ✅ | 143.88 | ✅ | 383.88 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024] | ✅ | 160.74 | ✅ | 462.24 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024] | ✅ | 204.30 | ✅ | 372.62 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024] | ✅ | 161.32 | ✅ | 338.22 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024] | ✅ | 153.64 | ✅ | 362.32 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512] | ✅ | 184.92 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512] | ✅ | 160.20 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512] | ✅ | 166.60 | ✅ | 541.64 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512] | ✅ | 180.40 | ✅ | 425.12 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192] | ✅ | 154.52 | ✅ | 445.50 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192] | ✅ | 152.88 | ✅ | 351.68 |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512] | ✅ | 209.56 | - | - |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512] | ✅ | 195.48 | - | - |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096] | ✅ | 161.96 | ✅ | 380.12 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096] | ✅ | 163.06 | ✅ | 390.24 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096] | ✅ | 168.18 | ✅ | 424.56 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096] | ✅ | 155.90 | ✅ | 417.10 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048] | ✅ | 176.74 | ✅ | 628.16 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048] | ✅ | 144.90 | ✅ | 430.72 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048] | ✅ | 164.26 | ✅ | 325.44 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048] | ✅ | 170.84 | ✅ | 428.04 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024] | ✅ | 178.52 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024] | ✅ | 188.42 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024] | ✅ | 210.46 | ✅ | 433.26 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024] | ✅ | 179.66 | ✅ | 638.70 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0] | ✅ | 40732.90 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 40726.96 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | 321718.26 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 150.04 | ✅ | 317.86 |
| test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 188.46 | ✅ | 312.62 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 176.94 | ✅ | 253.06 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 210.74 | ✅ | 408.76 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 161.68 | ✅ | 343.94 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 188.26 | ✅ | 397.72 |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 192.08 | - | - |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 247.98 | - | - |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 166.44 | ✅ | 273.90 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 178.84 | ✅ | 351.46 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 167.30 | ✅ | 279.42 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 174.20 | ✅ | 494.22 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 182.52 | ✅ | 360.24 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 189.26 | ✅ | 481.32 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 190.40 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 211.38 | - | - |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 168.26 | ✅ | 317.54 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 168.34 | ✅ | 566.70 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 187.32 | ✅ | 469.90 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 196.52 | ✅ | 623.60 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 183.22 | ✅ | 697.10 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 173.78 | ✅ | 481.12 |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 206.32 | - | - |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 217.90 | - | - |
| test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 166.52 | ✅ | 401.30 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 170.80 | ✅ | 399.34 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 162.94 | ✅ | 540.02 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 152.96 | ✅ | 367.28 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 181.16 | ✅ | 407.86 |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 202.90 | - | - |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 211.26 | - | - |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False] | ✅ | 218.60 | ✅ | 448.78 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True] | ✅ | 200.44 | ✅ | 584.40 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False] | ✅ | 173.98 | ✅ | 487.64 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True] | ✅ | 169.78 | ✅ | 540.76 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False] | ✅ | 173.84 | ✅ | 383.94 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True] | ✅ | 145.82 | ✅ | 396.04 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False] | ✅ | 166.84 | ✅ | 424.38 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True] | ✅ | 189.80 | ✅ | 475.98 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False] | ✅ | 220.00 | ✅ | 455.58 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | ✅ | 185.72 | ✅ | 516.36 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False] | ✅ | 193.68 | ✅ | 587.86 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True] | ✅ | 189.00 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False] | ✅ | 194.24 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 223.20 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False] | ✅ | 204.30 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 164.32 | ✅ | 401.20 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 226.14 | ✅ | 599.86 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 164.06 | ✅ | 451.68 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 172.34 | ✅ | 370.44 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 162.22 | ✅ | 342.34 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 162.16 | ✅ | 507.64 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 172.44 | ✅ | 504.10 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 179.08 | ✅ | 445.76 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 171.94 | ✅ | 725.56 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 180.70 | ✅ | 427.70 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 200.02 | ✅ | 520.90 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 170.90 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 186.74 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 194.46 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 208.84 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False] | ✅ | 171.82 | ✅ | 355.80 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 167.98 | ✅ | 374.16 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False] | ✅ | 154.64 | ✅ | 375.00 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True] | ✅ | 165.70 | ✅ | 410.72 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False] | ✅ | 202.76 | ✅ | 367.90 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True] | ✅ | 198.76 | ✅ | 654.76 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False] | ✅ | 164.94 | ✅ | 304.36 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True] | ✅ | 181.10 | ✅ | 509.92 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False] | ✅ | 179.36 | ✅ | 290.84 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True] | ✅ | 166.74 | ✅ | 470.16 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False] | ✅ | 197.30 | ✅ | 403.98 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True] | ✅ | 212.14 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False] | ✅ | 168.60 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True] | ✅ | 184.74 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False] | ✅ | 237.64 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False] | ✅ | 189.38 | ✅ | 344.96 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False] | ✅ | 171.32 | ✅ | 489.54 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True] | ✅ | 174.62 | ✅ | 548.44 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False] | ✅ | 213.38 | ✅ | 405.80 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True] | ✅ | 189.80 | ✅ | 750.08 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False] | ✅ | 209.80 | ✅ | 452.94 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True] | ✅ | 182.66 | ✅ | 590.86 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False] | ✅ | 186.46 | ✅ | 692.72 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True] | ✅ | 195.86 | ✅ | 521.92 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False] | ✅ | 188.26 | ✅ | 392.92 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True] | ✅ | 199.20 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False] | ✅ | 183.18 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True] | ✅ | 195.48 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False] | ✅ | 214.02 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 146.82 | ✅ | 461.96 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 170.60 | ✅ | 711.36 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 174.36 | ✅ | 420.90 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 185.54 | ✅ | 499.94 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 143.26 | ✅ | 696.26 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 177.56 | ✅ | 463.48 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 187.80 | - | - |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 156.58 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 148.82 | ✅ | 434.52 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 162.34 | ✅ | 343.38 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 161.70 | ✅ | 415.94 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 173.16 | ✅ | 471.02 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 164.92 | ✅ | 410.30 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 157.78 | ✅ | 468.50 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 178.90 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 191.66 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 173.58 | ✅ | 437.84 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 153.48 | ✅ | 354.36 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 142.90 | ✅ | 365.76 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 186.82 | ✅ | 441.50 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 166.78 | ✅ | 444.60 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 164.10 | ✅ | 512.10 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 193.98 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 187.58 | - | - |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 153.14 | ✅ | 379.38 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 159.70 | ✅ | 471.90 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 158.72 | ✅ | 387.92 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 150.08 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 190.98 | ✅ | 348.30 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 178.64 | ✅ | 483.78 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 142.00 | ✅ | 464.18 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 195.20 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 166.70 | ✅ | 428.40 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 192.02 | ✅ | 475.20 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 157.90 | ✅ | 455.48 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 159.88 | ✅ | 394.82 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 177.30 | ✅ | 414.22 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 176.18 | ✅ | 430.26 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 183.82 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 178.82 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 186.14 | ✅ | 415.98 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 157.22 | ✅ | 405.88 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 178.34 | ✅ | 414.54 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 165.60 | ✅ | 414.80 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 152.44 | ✅ | 431.32 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 190.56 | ✅ | 491.08 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 180.38 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 165.68 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 145.56 | ✅ | 415.48 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 171.24 | ✅ | 392.16 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 186.64 | ✅ | 387.64 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 168.42 | ✅ | 390.80 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 167.24 | ✅ | 471.28 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 168.28 | ✅ | 614.74 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 177.02 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 175.86 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 176.66 | ✅ | 264.10 |
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 170.64 | ✅ | 359.32 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 170.68 | ✅ | 475.40 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 174.58 | ✅ | 348.24 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 178.44 | ✅ | 816.32 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 167.22 | ✅ | 684.00 |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 203.78 | - | - |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 200.88 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 154.98 | ✅ | 449.82 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 166.40 | ✅ | 451.08 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 171.84 | ✅ | 813.26 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 193.02 | ✅ | 343.46 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 190.88 | ✅ | 308.24 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 206.88 | ✅ | 420.88 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 179.46 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 218.54 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 163.22 | ✅ | 290.24 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 201.42 | ✅ | 322.38 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 184.68 | ✅ | 319.16 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 204.86 | ✅ | 425.34 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 175.68 | ✅ | 250.58 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 207.82 | ✅ | 421.94 |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 202.42 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 206.06 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 170.06 | ✅ | 735.16 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 185.76 | ✅ | 555.10 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 166.52 | ✅ | 347.64 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 183.64 | ✅ | 444.78 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 187.94 | ✅ | 603.98 |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 172.80 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 212.42 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 175.44 | ✅ | 341.16 |
| test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 143.10 | ✅ | 414.22 |
| test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 144.66 | ✅ | 499.04 |
| test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 201.14 | - | - |
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 166.70 | ✅ | 371.30 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 163.78 | ✅ | 430.64 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 162.02 | ✅ | 324.60 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 244.60 | - | - |
| test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 190.14 | ✅ | 736.02 |
| test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 165.76 | ✅ | 349.62 |
| test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 178.82 | ✅ | 432.94 |
| test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 163.78 | - | - |
| test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 193.94 | ✅ | 452.90 |
| test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 160.62 | ✅ | 407.10 |
| test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 178.88 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 169.00 | ✅ | 441.64 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 166.18 | ✅ | 421.74 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 184.60 | ✅ | 450.98 |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 940.64 | ✅ | 10073.45 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1004.56 | ✅ | 11396.32 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False] | ✅ | 2238.75 | ✅ | 21057.45 |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 178.12 | ✅ | 504.50 |
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 187.76 | ✅ | 414.40 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 138.54 | ✅ | 319.14 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 181.52 | ✅ | 440.30 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 160.80 | ✅ | 348.56 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 193.02 | ✅ | 406.44 |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 233.10 | - | - |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 200.64 | - | - |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 167.18 | ✅ | 295.88 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 176.14 | ✅ | 264.20 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 149.58 | ✅ | 443.30 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 185.46 | ✅ | 446.14 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 185.08 | ✅ | 785.56 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 214.62 | ✅ | 511.88 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 191.36 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 212.88 | - | - |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 162.40 | ✅ | 382.82 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 165.22 | ✅ | 464.00 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 185.42 | ✅ | 636.60 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 178.16 | ✅ | 353.86 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 195.88 | ✅ | 291.10 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 194.20 | ✅ | 437.96 |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 209.50 | - | - |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 237.78 | - | - |
| test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 188.12 | ✅ | 375.80 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 179.76 | ✅ | 528.14 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 191.88 | ✅ | 463.22 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 214.96 | ✅ | 447.92 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 182.66 | ✅ | 559.40 |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 212.92 | - | - |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 251.04 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 257.58 | ✅ | 545.06 |
| test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 216.76 | ✅ | 569.26 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 233.86 | ✅ | 568.58 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 211.80 | ✅ | 743.34 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 278.46 | ✅ | 1234.08 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 262.68 | ✅ | 764.28 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 268.30 | ✅ | 651.04 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 247.68 | ✅ | 722.82 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 257.52 | ✅ | 2092.66 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 256.96 | ✅ | 1134.54 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 382.62 | ✅ | 982.94 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 366.88 | ✅ | 1621.22 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 364.12 | ✅ | 699.88 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 322.98 | ✅ | 643.46 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 320.26 | ✅ | 662.86 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 332.18 | ✅ | 1124.96 |
| test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 305.10 | - | - |
| test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 337.76 | - | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 200.30 | ✅ | 463.78 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 220.54 | ✅ | 461.06 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4] | ✅ | 296.08 | ✅ | 648.58 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 184.88 | ✅ | 398.72 |
| test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 180.00 | ✅ | 359.74 |
| test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 169.04 | ✅ | 387.60 |
| test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 176.56 | ✅ | 292.00 |
| test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 188.58 | ✅ | 538.12 |
| test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 166.22 | ✅ | 412.40 |
| test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 161.34 | ✅ | 400.80 |
| test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 203.36 | ✅ | 351.26 |
| test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 160.78 | ✅ | 466.26 |
| test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 201.74 | - | - |
| test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 187.54 | ✅ | 342.90 |

</details>

