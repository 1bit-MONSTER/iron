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
<summary>(unknown)</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128 | ✅ | 0.22 | - | - |
| M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1 | ✅ | 2213.46 | - | - |
| M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1 | ✅ | 252.28 | - | - |
| M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1 | ✅ | 242.72 | - | - |
| M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 49207.44 | - | - |
| M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 28745.08 | - | - |
| M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 7659.88 | - | - |
| M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048 | ✅ | 12.61 | - | - |
| M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024 | ✅ | 24.54 | - | - |
| M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512 | ✅ | 40.37 | - | - |
| M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256 | ✅ | 44.19 | - | - |
| M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8 | ✅ | 201.78 | - | - |
| M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8 | ✅ | 176.92 | - | - |
| M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1 | ✅ | 2248.58 | - | - |
| M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4 | ✅ | 3229.16 | - | - |
| M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024 | ✅ | 13.00 | - | - |
| M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024 | ✅ | 24.50 | - | - |
| M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024 | ✅ | 40.20 | - | - |
| M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024 | ✅ | 43.19 | - | - |
| M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1 | ✅ | 1472.76 | - | - |
| embedding_dim_1024-hidden_dim_3584 | ✅ | 3804.21 | - | - |
| embedding_dim_2048-hidden_dim_2048 | ✅ | 4127.10 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048 | ✅ | 165.14 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32 | ✅ | 154.72 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False | ✅ | 168.44 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True | ✅ | 186.26 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024 | ✅ | 166.30 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32 | ✅ | 162.44 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False | ✅ | 153.28 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True | ✅ | 164.00 | - | - |
| input_length_2048-num_aie_columns_1-tile_size_2048 | ✅ | 157.65 | - | - |
| input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0 | ✅ | 181.44 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024 | ✅ | 177.46 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32 | ✅ | 187.46 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False | ✅ | 183.86 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True | ✅ | 188.10 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512 | ✅ | 180.86 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32 | ✅ | 170.32 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False | ✅ | 188.84 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True | ✅ | 203.38 | - | - |
| input_length_2048-num_aie_columns_2-tile_size_1024 | ✅ | 148.79 | - | - |
| input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0 | ✅ | 218.20 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512 | ✅ | 177.71 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32 | ✅ | 153.26 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False | ✅ | 176.10 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True | ✅ | 198.32 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256 | ✅ | 196.21 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32 | ✅ | 183.64 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False | ✅ | 192.72 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True | ✅ | 225.84 | - | - |
| input_length_2048-num_aie_columns_4-tile_size_512 | ✅ | 164.60 | - | - |
| input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0 | ✅ | 223.86 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256 | ✅ | 207.66 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32 | ✅ | 169.90 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False | ✅ | 210.80 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True | ✅ | 210.98 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128 | ✅ | 231.52 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32 | ✅ | 229.22 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False | ✅ | 224.94 | - | - |
| input_length_2048-num_aie_columns_8-tile_size_256 | ✅ | 212.18 | - | - |
| input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0 | ✅ | 247.78 | - | - |
| input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048 | ✅ | 183.26 | - | - |
| input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128 | ✅ | 228.56 | - | - |
| input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024 | ✅ | 158.42 | - | - |
| input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024 | ✅ | 184.74 | - | - |
| input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512 | ✅ | 205.50 | - | - |
| input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512 | ✅ | 195.54 | - | - |
| input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256 | ✅ | 195.28 | - | - |
| input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256 | ✅ | 198.00 | - | - |
| input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024 | ✅ | 206.60 | - | - |
| input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048 | ✅ | 195.20 | - | - |
| input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512 | ✅ | 194.84 | - | - |
| rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0 | ✅ | 164.04 | - | - |
| rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0 | ✅ | 189.20 | - | - |
| rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0 | ✅ | 205.88 | - | - |
| rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0 | ✅ | 193.08 | - | - |
| rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0 | ✅ | 171.92 | - | - |
| rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0 | ✅ | 172.14 | - | - |
| rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0 | ✅ | 186.72 | - | - |
| rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0 | ✅ | 180.92 | - | - |
| seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0 | ✅ | 40715.44 | - | - |
| seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False | ✅ | 11728.07 | - | - |

</details>

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | - | - | ✅ | 394.04 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | - | - | ✅ | 358.30 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | - | - | ✅ | 431.70 |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | - | - | ✅ | 370.26 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | - | - | ✅ | 401.06 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | - | - | ✅ | 380.92 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | - | - | ✅ | 488.34 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | - | - | ✅ | 343.44 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | - | - | ✅ | 443.82 |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | - | - | ✅ | 412.80 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | - | - | ✅ | 681.16 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | - | - | ✅ | 887.68 |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | - | - | ✅ | 354.28 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | - | - | ✅ | 651.12 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | - | - | ✅ | 434.56 |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 322.18 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | - | - | ✅ | 252.44 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 361.50 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 497.86 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 307.82 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 407.50 |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1] | - | - | ✅ | 628.94 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1] | - | - | ✅ | 766.82 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 82225.06 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 25420.24 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 3307.84 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4] | - | - | ✅ | 6139.54 |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | - | - | ✅ | 0.07 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | - | - | ✅ | 3.59 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | - | - | ✅ | 7.13 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | - | - | ✅ | 10.45 |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | - | - | ✅ | 3.52 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | - | - | ✅ | 6.66 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | - | - | ✅ | 10.73 |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 374.78 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | - | - | ✅ | 238.76 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 332.94 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 374.42 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 372.46 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 757.68 |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | - | - | ✅ | 416.26 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | - | - | ✅ | 423.44 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | - | - | ✅ | 418.16 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | - | - | ✅ | 428.74 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | - | - | ✅ | 316.60 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | - | - | ✅ | 484.62 |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 320.66 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | - | - | ✅ | 319.60 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 417.16 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 344.50 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 415.18 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 390.88 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | - | - | ✅ | 369.66 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | - | - | ✅ | 489.52 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | - | - | ✅ | 505.44 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | - | - | ✅ | 379.18 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | - | - | ✅ | 822.84 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | - | - | ✅ | 371.56 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | - | - | ✅ | 828.60 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | - | - | ✅ | 408.44 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | - | - | ✅ | 436.22 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | - | - | ✅ | 492.22 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | - | - | ✅ | 531.76 |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | - | - | ✅ | 437.96 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | - | - | ✅ | 504.90 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | - | - | ✅ | 502.68 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | - | - | ✅ | 745.78 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | - | - | ✅ | 346.24 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 425.06 |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 271.08 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | - | - | ✅ | 491.20 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 334.90 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 694.18 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 903.94 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 551.70 |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 331.54 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 442.48 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 540.60 |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | - | - | ✅ | 480.06 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | - | - | ✅ | 441.52 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 326.66 |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | - | - | ✅ | 15364.62 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | - | - | ✅ | 16117.52 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False] | - | - | ✅ | 21805.69 |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 426.70 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | - | - | ✅ | 441.14 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 472.94 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 362.14 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 368.20 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 467.24 |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8] | - | - | ✅ | 984.96 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8] | - | - | ✅ | 505.64 |

</details>

## Extensive

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0] | ✅ | 179.32 | ✅ | 374.10 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0] | ✅ | 175.98 | ✅ | 332.44 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0] | ✅ | 185.88 | ✅ | 443.88 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0] | ✅ | 165.82 | ✅ | 378.42 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0] | ✅ | 198.88 | ✅ | 811.42 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | ✅ | 210.36 | ✅ | 344.70 |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0] | ✅ | 233.34 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0] | ✅ | 197.04 | - | - |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0] | ✅ | 166.94 | ✅ | 314.64 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 179.68 | ✅ | 632.02 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0] | ✅ | 190.86 | ✅ | 280.12 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 175.12 | ✅ | 374.24 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0] | ✅ | 188.66 | ✅ | 337.26 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 213.12 | ✅ | 369.20 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0] | ✅ | 236.96 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 240.66 | - | - |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0] | ✅ | 220.12 | ✅ | 352.28 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | ✅ | 186.40 | ✅ | 310.26 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0] | ✅ | 182.10 | ✅ | 624.34 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0] | ✅ | 180.32 | ✅ | 388.58 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0] | ✅ | 193.34 | ✅ | 377.76 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0] | ✅ | 173.48 | ✅ | 613.66 |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0] | ✅ | 189.06 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0] | ✅ | 199.00 | - | - |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0] | ✅ | 227.52 | ✅ | 309.00 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0] | ✅ | 184.74 | ✅ | 402.88 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0] | ✅ | 170.58 | ✅ | 317.58 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0] | ✅ | 175.54 | ✅ | 326.54 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0] | ✅ | 215.64 | ✅ | 420.40 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0] | ✅ | 168.84 | ✅ | 724.58 |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0] | ✅ | 193.38 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0] | ✅ | 190.32 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32] | ✅ | 147.92 | ✅ | 301.04 |
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32] | ✅ | 164.86 | ✅ | 843.90 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32] | ✅ | 185.64 | ✅ | 359.16 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32] | ✅ | 171.96 | ✅ | 373.36 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32] | ✅ | 167.68 | ✅ | 373.54 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32] | ✅ | 196.14 | ✅ | 451.04 |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32] | ✅ | 153.94 | - | - |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32] | ✅ | 188.70 | - | - |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 148.38 | ✅ | 389.44 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 180.90 | ✅ | 435.76 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 186.34 | ✅ | 487.74 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 190.40 | ✅ | 584.44 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 165.76 | ✅ | 447.92 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 185.74 | ✅ | 437.56 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 214.62 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 217.98 | - | - |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32] | ✅ | 179.36 | ✅ | 403.98 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32] | ✅ | 171.46 | ✅ | 425.88 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32] | ✅ | 198.70 | ✅ | 416.16 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32] | ✅ | 170.94 | ✅ | 472.22 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32] | ✅ | 172.30 | ✅ | 392.62 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32] | ✅ | 167.38 | ✅ | 474.26 |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32] | ✅ | 171.88 | - | - |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32] | ✅ | 208.56 | - | - |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32] | ✅ | 208.80 | ✅ | 355.76 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32] | ✅ | 166.26 | ✅ | 439.44 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32] | ✅ | 177.24 | ✅ | 496.94 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32] | ✅ | 171.50 | ✅ | 455.04 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32] | ✅ | 178.10 | ✅ | 328.60 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32] | ✅ | 197.34 | ✅ | 431.00 |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32] | ✅ | 177.28 | - | - |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32] | ✅ | 244.18 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 157.24 | ✅ | 410.98 |
| test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 154.10 | ✅ | 452.98 |
| test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 156.80 | ✅ | 414.76 |
| test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 167.28 | - | - |
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 170.00 | ✅ | 721.84 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 137.04 | ✅ | 858.02 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 173.76 | ✅ | 580.18 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 193.46 | - | - |
| test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 181.88 | ✅ | 444.54 |
| test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 168.48 | ✅ | 512.64 |
| test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 238.40 | ✅ | 568.18 |
| test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 204.96 | - | - |
| test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192] | ✅ | 147.48 | ✅ | 488.86 |
| test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 146.86 | ✅ | 467.28 |
| test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 156.50 | ✅ | 480.52 |
| test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 173.18 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 173.28 | ✅ | 410.50 |
| test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 151.04 | ✅ | 451.96 |
| test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 155.72 | ✅ | 475.36 |
| test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 205.84 | - | - |
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 162.78 | ✅ | 266.88 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 144.08 | ✅ | 422.76 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 171.80 | ✅ | 299.26 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 196.76 | - | - |
| test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 174.34 | ✅ | 395.72 |
| test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 181.88 | ✅ | 390.20 |
| test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 171.24 | ✅ | 558.30 |
| test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 196.80 | - | - |
| test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 171.90 | ✅ | 349.10 |
| test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 184.04 | ✅ | 515.52 |
| test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 195.96 | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 168.30 | ✅ | 270.20 |
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 164.32 | ✅ | 315.30 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 151.66 | ✅ | 309.20 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 173.12 | ✅ | 432.02 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 172.62 | ✅ | 369.60 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 165.30 | ✅ | 308.68 |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 169.88 | - | - |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 233.88 | - | - |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 155.26 | ✅ | 437.92 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 198.94 | ✅ | 395.12 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 159.96 | ✅ | 362.64 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 165.24 | ✅ | 540.88 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 180.14 | ✅ | 563.60 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 184.10 | ✅ | 454.36 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 186.20 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 213.74 | - | - |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 184.60 | ✅ | 685.44 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 154.40 | ✅ | 327.06 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 156.58 | ✅ | 394.64 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 162.32 | ✅ | 386.10 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 160.78 | ✅ | 324.34 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 213.20 | ✅ | 455.04 |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 194.18 | - | - |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 220.96 | - | - |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 170.58 | ✅ | 256.58 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 170.84 | ✅ | 335.04 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 174.54 | ✅ | 385.16 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 158.00 | ✅ | 459.78 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 161.44 | ✅ | 554.16 |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 162.58 | - | - |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 196.62 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1] | ✅ | 2227.74 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 289.04 | ✅ | 615.24 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 193.84 | ✅ | 476.22 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 48871.12 | ✅ | 82931.28 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1] | ✅ | 118677.06 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 28634.28 | ✅ | 25718.46 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1] | ✅ | 7584.74 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1] | ✅ | 8874.26 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 7773.30 | - | - |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 96801.62 | ✅ | 95662.44 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 103096.22 | ✅ | 99334.16 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 109585.58 | ✅ | 97266.42 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1252.00 | ✅ | 2860.54 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1317.82 | ✅ | 2478.58 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1410.66 | ✅ | 3066.20 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4415.02 | ✅ | 6936.00 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4609.26 | ✅ | 7471.12 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4784.00 | ✅ | 6249.30 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 96045.32 | ✅ | 98672.68 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 102298.80 | ✅ | 99763.34 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 108241.50 | ✅ | 95368.28 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1] | ✅ | 2268.62 | ✅ | 3669.86 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4] | ✅ | 3018.56 | ✅ | 5777.88 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1] | ✅ | 1388.34 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.25 | ✅ | 0.08 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 12.98 | ✅ | 3.57 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 23.07 | ✅ | 6.29 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 39.40 | ✅ | 11.59 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 42.43 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.99 | ✅ | 3.78 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 24.16 | ✅ | 6.14 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 39.98 | ✅ | 9.53 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 42.24 | - | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 169.32 | ✅ | 350.60 |
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 179.58 | ✅ | 411.06 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 143.42 | ✅ | 364.22 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 173.48 | ✅ | 410.02 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 176.32 | ✅ | 388.32 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 173.08 | ✅ | 426.92 |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 193.46 | - | - |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 221.32 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 139.16 | ✅ | 305.34 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 155.32 | ✅ | 445.36 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 153.64 | ✅ | 385.30 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 179.62 | ✅ | 388.30 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 159.38 | ✅ | 258.08 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 175.80 | ✅ | 514.20 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 172.54 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 213.06 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 180.22 | ✅ | 320.52 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 179.76 | ✅ | 446.32 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 186.32 | ✅ | 402.96 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 168.40 | ✅ | 418.44 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 204.54 | ✅ | 470.98 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 181.30 | ✅ | 722.70 |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 184.26 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 226.04 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 186.48 | ✅ | 438.58 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 174.18 | ✅ | 415.02 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 171.54 | ✅ | 726.06 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 184.18 | ✅ | 463.32 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 188.06 | ✅ | 640.34 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 203.56 | ✅ | 651.40 |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 182.58 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 249.80 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024] | ✅ | 132.08 | ✅ | 370.10 |
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024] | ✅ | 134.84 | ✅ | 462.20 |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64] | ✅ | 191.08 | - | - |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64] | ✅ | 204.64 | - | - |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512] | ✅ | 154.34 | ✅ | 413.36 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512] | ✅ | 167.86 | ✅ | 269.86 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512] | ✅ | 165.16 | ✅ | 362.08 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512] | ✅ | 162.24 | ✅ | 267.50 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256] | ✅ | 194.22 | ✅ | 363.30 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256] | ✅ | 168.80 | ✅ | 521.52 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256] | ✅ | 177.52 | ✅ | 389.72 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256] | ✅ | 166.96 | ✅ | 480.78 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128] | ✅ | 205.54 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128] | ✅ | 173.78 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128] | ✅ | 209.16 | ✅ | 452.02 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128] | ✅ | 183.96 | ✅ | 415.44 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 158.84 | ✅ | 383.84 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048] | ✅ | 166.56 | ✅ | 380.36 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 235.96 | - | - |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128] | ✅ | 235.30 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 154.16 | ✅ | 438.62 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024] | ✅ | 172.36 | ✅ | 299.84 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 153.76 | ✅ | 790.44 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024] | ✅ | 164.74 | ✅ | 653.56 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 165.66 | ✅ | 691.02 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512] | ✅ | 164.04 | ✅ | 469.22 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 176.90 | ✅ | 574.72 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512] | ✅ | 165.02 | ✅ | 567.06 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 177.52 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256] | ✅ | 173.74 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 174.32 | ✅ | 451.70 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256] | ✅ | 172.00 | ✅ | 389.98 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096] | ✅ | 163.30 | ✅ | 315.64 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096] | ✅ | 164.48 | ✅ | 384.82 |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256] | ✅ | 204.54 | - | - |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256] | ✅ | 212.54 | - | - |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048] | ✅ | 209.82 | ✅ | 308.82 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048] | ✅ | 157.82 | ✅ | 417.42 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048] | ✅ | 152.14 | ✅ | 372.44 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048] | ✅ | 161.66 | ✅ | 297.50 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024] | ✅ | 179.50 | ✅ | 393.28 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024] | ✅ | 179.04 | ✅ | 800.14 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024] | ✅ | 175.12 | ✅ | 444.82 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024] | ✅ | 149.12 | ✅ | 363.00 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512] | ✅ | 162.28 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512] | ✅ | 156.28 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512] | ✅ | 174.42 | ✅ | 399.18 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512] | ✅ | 145.52 | ✅ | 761.38 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192] | ✅ | 152.20 | ✅ | 403.74 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192] | ✅ | 145.92 | ✅ | 350.62 |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512] | ✅ | 222.70 | - | - |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512] | ✅ | 176.86 | - | - |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096] | ✅ | 138.46 | ✅ | 282.86 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096] | ✅ | 155.36 | ✅ | 381.50 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096] | ✅ | 152.20 | ✅ | 463.88 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096] | ✅ | 145.44 | ✅ | 369.72 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048] | ✅ | 172.92 | ✅ | 343.92 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048] | ✅ | 155.00 | ✅ | 366.06 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048] | ✅ | 165.14 | ✅ | 480.12 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048] | ✅ | 146.20 | ✅ | 477.54 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024] | ✅ | 191.88 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024] | ✅ | 156.74 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024] | ✅ | 163.32 | ✅ | 803.96 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024] | ✅ | 140.96 | ✅ | 365.46 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0] | ✅ | 40592.98 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 40766.28 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | 320029.26 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 182.84 | ✅ | 336.88 |
| test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 186.06 | ✅ | 451.26 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 220.66 | ✅ | 385.26 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 182.78 | ✅ | 404.20 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 183.60 | ✅ | 480.96 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 238.94 | ✅ | 456.82 |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 197.30 | - | - |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 268.98 | - | - |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 151.76 | ✅ | 309.78 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 169.30 | ✅ | 245.48 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 161.06 | ✅ | 359.06 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 189.94 | ✅ | 444.26 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 176.84 | ✅ | 512.70 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 170.12 | ✅ | 448.94 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 202.72 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 247.58 | - | - |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 187.58 | ✅ | 311.40 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 172.10 | ✅ | 465.40 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 170.16 | ✅ | 353.66 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 199.62 | ✅ | 624.14 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 161.28 | ✅ | 357.34 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 193.40 | ✅ | 631.88 |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 236.44 | - | - |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 219.68 | - | - |
| test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 169.14 | ✅ | 388.66 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 171.90 | ✅ | 451.58 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 193.10 | ✅ | 430.62 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 222.94 | ✅ | 391.20 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 192.94 | ✅ | 484.66 |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 201.20 | - | - |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 274.30 | - | - |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False] | ✅ | 188.42 | ✅ | 387.46 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True] | ✅ | 170.10 | ✅ | 593.38 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False] | ✅ | 170.46 | ✅ | 510.16 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True] | ✅ | 232.96 | ✅ | 664.46 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False] | ✅ | 174.94 | ✅ | 396.66 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True] | ✅ | 155.90 | ✅ | 413.46 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False] | ✅ | 185.30 | ✅ | 484.62 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True] | ✅ | 161.60 | ✅ | 351.86 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False] | ✅ | 183.70 | ✅ | 423.46 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | ✅ | 166.32 | ✅ | 347.94 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False] | ✅ | 228.00 | ✅ | 425.28 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True] | ✅ | 189.16 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False] | ✅ | 211.66 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 194.36 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False] | ✅ | 236.96 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 171.34 | ✅ | 430.88 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 149.42 | ✅ | 343.54 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 216.96 | ✅ | 351.98 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 174.64 | ✅ | 481.20 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 166.80 | ✅ | 409.12 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 190.54 | ✅ | 523.68 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 173.72 | ✅ | 419.92 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 196.74 | ✅ | 500.00 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 201.18 | ✅ | 412.50 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 156.88 | ✅ | 372.86 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 188.96 | ✅ | 416.68 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 256.98 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 241.10 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 206.00 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 273.36 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False] | ✅ | 193.16 | ✅ | 316.32 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 168.92 | ✅ | 396.20 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False] | ✅ | 150.10 | ✅ | 297.30 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True] | ✅ | 139.46 | ✅ | 457.08 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False] | ✅ | 183.40 | ✅ | 832.96 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True] | ✅ | 184.52 | ✅ | 382.04 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False] | ✅ | 194.78 | ✅ | 316.30 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True] | ✅ | 218.80 | ✅ | 370.58 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False] | ✅ | 192.60 | ✅ | 402.08 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True] | ✅ | 194.36 | ✅ | 383.86 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False] | ✅ | 167.82 | ✅ | 411.92 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True] | ✅ | 219.86 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False] | ✅ | 198.18 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True] | ✅ | 189.00 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False] | ✅ | 218.52 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False] | ✅ | 177.12 | ✅ | 397.46 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False] | ✅ | 160.04 | ✅ | 290.78 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True] | ✅ | 181.18 | ✅ | 733.74 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False] | ✅ | 181.72 | ✅ | 395.02 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True] | ✅ | 186.76 | ✅ | 378.46 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False] | ✅ | 191.72 | ✅ | 457.54 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True] | ✅ | 169.58 | ✅ | 418.00 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False] | ✅ | 174.96 | ✅ | 517.58 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True] | ✅ | 194.60 | ✅ | 380.80 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False] | ✅ | 199.36 | ✅ | 742.72 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True] | ✅ | 183.66 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False] | ✅ | 181.44 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True] | ✅ | 271.72 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False] | ✅ | 227.28 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 163.20 | ✅ | 300.10 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 175.08 | ✅ | 630.30 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 168.80 | ✅ | 431.88 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 189.34 | ✅ | 321.74 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 170.08 | ✅ | 471.20 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 189.64 | ✅ | 610.36 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 162.92 | - | - |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 185.86 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 160.08 | ✅ | 389.94 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 209.00 | ✅ | 283.02 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 214.26 | ✅ | 331.48 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 176.60 | ✅ | 353.88 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 183.32 | ✅ | 389.46 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 193.52 | ✅ | 464.32 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 167.36 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 167.52 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 150.40 | ✅ | 783.52 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 146.60 | ✅ | 390.96 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 177.70 | ✅ | 289.78 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 183.42 | ✅ | 518.36 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 188.70 | ✅ | 352.80 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 206.60 | ✅ | 427.54 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 150.34 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 187.90 | - | - |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 186.40 | ✅ | 399.82 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 190.24 | ✅ | 354.84 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 186.78 | ✅ | 421.16 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 188.12 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 161.38 | ✅ | 398.44 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 155.18 | ✅ | 364.06 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 249.24 | ✅ | 357.50 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 187.48 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 191.98 | ✅ | 334.38 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 225.90 | ✅ | 414.64 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 168.98 | ✅ | 778.42 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 176.44 | ✅ | 355.50 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 165.34 | ✅ | 366.46 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 162.28 | ✅ | 344.20 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 191.32 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 185.48 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 203.76 | ✅ | 377.22 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 188.06 | ✅ | 393.80 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 181.08 | ✅ | 393.92 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 165.74 | ✅ | 348.10 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 177.22 | ✅ | 395.50 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 189.26 | ✅ | 411.02 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 186.34 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 184.14 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 183.80 | ✅ | 443.08 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 185.04 | ✅ | 328.92 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 168.18 | ✅ | 356.58 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 158.62 | ✅ | 463.60 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 190.38 | ✅ | 356.66 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 178.60 | ✅ | 860.12 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 176.86 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 182.82 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 178.58 | ✅ | 439.24 |
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 175.04 | ✅ | 408.64 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 193.66 | ✅ | 731.14 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 215.24 | ✅ | 309.04 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 185.96 | ✅ | 429.36 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 199.24 | ✅ | 865.56 |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 206.50 | - | - |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 212.78 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 186.16 | ✅ | 283.60 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 166.04 | ✅ | 271.30 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 182.48 | ✅ | 281.98 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 222.68 | ✅ | 428.94 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 185.52 | ✅ | 482.36 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 197.00 | ✅ | 494.70 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 223.82 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 251.18 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 192.16 | ✅ | 724.60 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 201.26 | ✅ | 439.06 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 178.18 | ✅ | 344.22 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 204.46 | ✅ | 455.62 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 178.22 | ✅ | 252.54 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 231.02 | ✅ | 476.56 |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 202.20 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 219.58 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 174.02 | ✅ | 383.62 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 182.48 | ✅ | 435.22 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 190.42 | ✅ | 417.38 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 208.78 | ✅ | 382.34 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 188.54 | ✅ | 493.94 |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 227.00 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 251.56 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 197.68 | ✅ | 654.04 |
| test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 140.78 | ✅ | 325.52 |
| test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 158.02 | ✅ | 447.40 |
| test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 198.34 | - | - |
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 159.20 | ✅ | 365.16 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 154.18 | ✅ | 442.30 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 212.00 | ✅ | 320.78 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 158.46 | - | - |
| test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 162.14 | ✅ | 321.84 |
| test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 169.04 | ✅ | 518.96 |
| test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 189.60 | ✅ | 506.74 |
| test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 231.12 | - | - |
| test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 172.22 | ✅ | 433.92 |
| test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 173.12 | ✅ | 491.36 |
| test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 190.52 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 185.12 | ✅ | 392.54 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 166.18 | ✅ | 402.38 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 187.48 | ✅ | 1042.16 |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 3982.62 | ✅ | 13293.57 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 3760.00 | ✅ | 15432.11 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False] | ✅ | 10576.83 | ✅ | 22495.50 |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 167.78 | ✅ | 345.60 |
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 149.96 | ✅ | 454.74 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 166.28 | ✅ | 443.90 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 169.94 | ✅ | 437.90 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 166.64 | ✅ | 435.38 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 178.12 | ✅ | 405.68 |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 171.00 | - | - |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 201.40 | - | - |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 165.34 | ✅ | 401.32 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 173.22 | ✅ | 412.72 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 181.52 | ✅ | 438.86 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 161.50 | ✅ | 581.74 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 183.86 | ✅ | 339.54 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 171.84 | ✅ | 624.32 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 183.66 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 219.98 | - | - |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 168.58 | ✅ | 371.02 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 185.54 | ✅ | 399.36 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 169.52 | ✅ | 424.74 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 171.72 | ✅ | 643.08 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 191.20 | ✅ | 456.22 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 219.46 | ✅ | 404.08 |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 207.90 | - | - |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 264.92 | - | - |
| test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 160.20 | ✅ | 444.14 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 179.94 | ✅ | 489.74 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 180.26 | ✅ | 375.76 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 179.22 | ✅ | 392.02 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 178.52 | ✅ | 404.76 |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 149.94 | - | - |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 205.92 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8] | ✅ | 220.30 | ✅ | 600.30 |
| test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8] | ✅ | 225.64 | ✅ | 991.08 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8] | ✅ | 232.04 | ✅ | 557.56 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8] | ✅ | 222.00 | ✅ | 449.62 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8] | ✅ | 257.26 | ✅ | 1763.64 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8] | ✅ | 266.96 | ✅ | 1761.00 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8] | ✅ | 272.08 | ✅ | 1210.34 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8] | ✅ | 262.32 | ✅ | 1274.68 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8] | ✅ | 254.36 | ✅ | 882.34 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8] | ✅ | 257.60 | ✅ | 936.00 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8] | ✅ | 379.08 | ✅ | 1670.92 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8] | ✅ | 371.38 | ✅ | 1960.18 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8] | ✅ | 372.44 | ✅ | 1264.14 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8] | ✅ | 324.52 | ✅ | 746.58 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8] | ✅ | 344.00 | ✅ | 1122.06 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8] | ✅ | 334.24 | ✅ | 793.22 |
| test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8] | ✅ | 333.10 | - | - |
| test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8] | ✅ | 337.00 | - | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8] | ✅ | 194.96 | ✅ | 1011.36 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8] | ✅ | 160.64 | ✅ | 679.58 |
| test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8] | ✅ | 170.32 | ✅ | 446.70 |
| test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8] | ✅ | 183.62 | ✅ | 724.06 |
| test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8] | ✅ | 187.52 | ✅ | 452.68 |
| test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8] | ✅ | 157.96 | ✅ | 420.00 |
| test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8] | ✅ | 201.88 | ✅ | 494.16 |
| test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8] | ✅ | 222.52 | ✅ | 491.76 |
| test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8] | ✅ | 196.76 | ✅ | 817.66 |
| test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8] | ✅ | 187.02 | ✅ | 775.14 |
| test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8] | ✅ | 241.44 | - | - |
| test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8] | ✅ | 173.40 | ✅ | 502.90 |

</details>

