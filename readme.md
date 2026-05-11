# IRON - CI Summary

## Examples

<details>
<summary>(unknown)</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| llama_3.2_1b_prompt_1024_tokens_1 | ✅ | - | - | - |
| llama_3.2_1b_prompt_1024_tokens_40 | ✅ | - | - | - |
| llama_3.2_1b_prompt_13_tokens_1 | ✅ | - | - | - |
| llama_3.2_1b_prompt_13_tokens_40 | ✅ | - | - | - |

</details>

## Small

<details>
<summary>(unknown)</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128 | ✅ | 0.22 | ✅ | 0.10 |
| M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1 | ✅ | 2213.46 | - | - |
| M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1 | ✅ | 252.28 | ✅ | 787.42 |
| M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1 | ✅ | 242.72 | ✅ | 506.06 |
| M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 49207.44 | ✅ | 82375.28 |
| M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 28745.08 | ✅ | 24175.22 |
| M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 7659.88 | - | - |
| M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048 | ✅ | 12.61 | ✅ | 3.62 |
| M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024 | ✅ | 24.54 | ✅ | 5.88 |
| M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512 | ✅ | 40.37 | ✅ | 10.58 |
| M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256 | ✅ | 44.19 | - | - |
| M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8 | ✅ | 201.78 | ✅ | 550.18 |
| M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8 | ✅ | 176.92 | ✅ | 457.80 |
| M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1 | ✅ | 2248.58 | ✅ | 3594.94 |
| M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4 | ✅ | 3229.16 | ✅ | 5978.60 |
| M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024 | ✅ | 13.00 | ✅ | 3.52 |
| M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024 | ✅ | 24.50 | ✅ | 6.86 |
| M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024 | ✅ | 40.20 | ✅ | 9.94 |
| M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024 | ✅ | 43.19 | - | - |
| M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1 | ✅ | 1472.76 | - | - |
| embedding_dim_1024-hidden_dim_3584 | ✅ | 3804.21 | ✅ | 13431.05 |
| embedding_dim_2048-hidden_dim_2048 | ✅ | 4127.10 | ✅ | 10368.19 |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048 | ✅ | 165.14 | ✅ | 481.52 |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32 | ✅ | 154.72 | ✅ | 382.28 |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False | ✅ | 168.44 | ✅ | 470.28 |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True | ✅ | 186.26 | ✅ | 466.00 |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024 | ✅ | 166.30 | ✅ | 477.52 |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32 | ✅ | 162.44 | ✅ | 407.04 |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False | ✅ | 153.28 | ✅ | 450.08 |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True | ✅ | 164.00 | ✅ | 439.54 |
| input_length_2048-num_aie_columns_1-tile_size_2048 | ✅ | 157.65 | ✅ | 579.21 |
| input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0 | ✅ | 181.44 | ✅ | 333.74 |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024 | ✅ | 177.46 | ✅ | 381.50 |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32 | ✅ | 187.46 | ✅ | 372.62 |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False | ✅ | 183.86 | ✅ | 445.38 |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True | ✅ | 188.10 | ✅ | 424.60 |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512 | ✅ | 180.86 | ✅ | 369.38 |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32 | ✅ | 170.32 | ✅ | 408.00 |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False | ✅ | 188.84 | ✅ | 412.20 |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True | ✅ | 203.38 | ✅ | 488.02 |
| input_length_2048-num_aie_columns_2-tile_size_1024 | ✅ | 148.79 | ✅ | 544.90 |
| input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0 | ✅ | 218.20 | ✅ | 323.66 |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512 | ✅ | 177.71 | ✅ | 509.59 |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32 | ✅ | 153.26 | ✅ | 382.24 |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False | ✅ | 176.10 | ✅ | 422.84 |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True | ✅ | 198.32 | ✅ | 430.86 |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256 | ✅ | 196.21 | ✅ | 455.08 |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32 | ✅ | 183.64 | ✅ | 381.08 |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False | ✅ | 192.72 | ✅ | 492.90 |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True | ✅ | 225.84 | - | - |
| input_length_2048-num_aie_columns_4-tile_size_512 | ✅ | 164.60 | ✅ | 408.91 |
| input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0 | ✅ | 223.86 | ✅ | 298.74 |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256 | ✅ | 207.66 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32 | ✅ | 169.90 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False | ✅ | 210.80 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True | ✅ | 210.98 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128 | ✅ | 231.52 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32 | ✅ | 229.22 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False | ✅ | 224.94 | - | - |
| input_length_2048-num_aie_columns_8-tile_size_256 | ✅ | 212.18 | - | - |
| input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0 | ✅ | 247.78 | - | - |
| input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048 | ✅ | 183.26 | ✅ | 311.22 |
| input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128 | ✅ | 228.56 | - | - |
| input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024 | ✅ | 158.42 | ✅ | 360.58 |
| input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024 | ✅ | 184.74 | ✅ | 293.24 |
| input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512 | ✅ | 205.50 | ✅ | 379.70 |
| input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512 | ✅ | 195.54 | ✅ | 777.80 |
| input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256 | ✅ | 195.28 | - | - |
| input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256 | ✅ | 198.00 | ✅ | 423.46 |
| input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024 | ✅ | 206.60 | ✅ | 364.74 |
| input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048 | ✅ | 195.20 | ✅ | 400.94 |
| input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512 | ✅ | 194.84 | ✅ | 472.84 |
| rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0 | ✅ | 164.04 | ✅ | 404.04 |
| rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0 | ✅ | 189.20 | ✅ | 334.48 |
| rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0 | ✅ | 205.88 | ✅ | 382.02 |
| rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0 | ✅ | 193.08 | - | - |
| rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0 | ✅ | 171.92 | ✅ | 669.22 |
| rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0 | ✅ | 172.14 | ✅ | 331.02 |
| rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0 | ✅ | 186.72 | ✅ | 586.12 |
| rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0 | ✅ | 180.92 | - | - |
| seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0 | ✅ | 40715.44 | - | - |
| seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False | ✅ | 11728.07 | ✅ | 25291.80 |

</details>

## Extensive

<details>
<summary>(unknown)</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128 | ✅ | 0.23 | - | - |
| M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1 | ✅ | 2286.18 | - | - |
| M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1 | ✅ | 225.60 | - | - |
| M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1 | ✅ | 265.04 | - | - |
| M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 49254.10 | - | - |
| M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1 | ✅ | 117437.50 | - | - |
| M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 28578.32 | - | - |
| M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1 | ✅ | 7346.18 | - | - |
| M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1 | ✅ | 8800.48 | - | - |
| M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 7324.10 | - | - |
| M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 97753.04 | - | - |
| M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 102750.68 | - | - |
| M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 109569.54 | - | - |
| M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 1333.92 | - | - |
| M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 1316.64 | - | - |
| M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 1550.24 | - | - |
| M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 4522.72 | - | - |
| M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 4692.70 | - | - |
| M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 4840.40 | - | - |
| M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 97011.96 | - | - |
| M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 102054.88 | - | - |
| M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1 | ✅ | 108364.70 | - | - |
| M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048 | ✅ | 13.00 | - | - |
| M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024 | ✅ | 24.17 | - | - |
| M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512 | ✅ | 40.30 | - | - |
| M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256 | ✅ | 41.22 | - | - |
| M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8 | ✅ | 232.70 | - | - |
| M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8 | ✅ | 239.64 | - | - |
| M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8 | ✅ | 237.14 | - | - |
| M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8 | ✅ | 218.94 | - | - |
| M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8 | ✅ | 261.74 | - | - |
| M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8 | ✅ | 253.30 | - | - |
| M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8 | ✅ | 260.16 | - | - |
| M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8 | ✅ | 269.04 | - | - |
| M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8 | ✅ | 273.16 | - | - |
| M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8 | ✅ | 253.48 | - | - |
| M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8 | ✅ | 383.30 | - | - |
| M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8 | ✅ | 349.96 | - | - |
| M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8 | ✅ | 376.46 | - | - |
| M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8 | ✅ | 343.00 | - | - |
| M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8 | ✅ | 391.54 | - | - |
| M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8 | ✅ | 352.92 | - | - |
| M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8 | ✅ | 338.16 | - | - |
| M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8 | ✅ | 369.08 | - | - |
| M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8 | ✅ | 210.80 | - | - |
| M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8 | ✅ | 192.22 | - | - |
| M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1 | ✅ | 2280.26 | - | - |
| M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4 | ✅ | 3489.58 | - | - |
| M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8 | ✅ | 177.16 | - | - |
| M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8 | ✅ | 209.72 | - | - |
| M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8 | ✅ | 180.10 | - | - |
| M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8 | ✅ | 180.10 | - | - |
| M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8 | ✅ | 177.42 | - | - |
| M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8 | ✅ | 175.48 | - | - |
| M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8 | ✅ | 175.30 | - | - |
| M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8 | ✅ | 189.56 | - | - |
| M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8 | ✅ | 176.02 | - | - |
| M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8 | ✅ | 171.18 | - | - |
| M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024 | ✅ | 12.36 | - | - |
| M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024 | ✅ | 23.77 | - | - |
| M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024 | ✅ | 40.78 | - | - |
| M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024 | ✅ | 42.63 | - | - |
| M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1 | ✅ | 1485.16 | - | - |
| embedding_dim_1024-hidden_dim_3584 | ✅ | 3924.16 | - | - |
| embedding_dim_2048-hidden_dim_2048 | ✅ | 3787.08 | - | - |
| input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024 | ✅ | 167.19 | - | - |
| input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32 | ✅ | 170.66 | - | - |
| input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False | ✅ | 174.66 | - | - |
| input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True | ✅ | 168.82 | - | - |
| input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512 | ✅ | 169.08 | - | - |
| input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32 | ✅ | 155.20 | - | - |
| input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False | ✅ | 183.14 | - | - |
| input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True | ✅ | 171.06 | - | - |
| input_length_1024-num_aie_columns_1-tile_size_1024 | ✅ | 154.68 | - | - |
| input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0 | ✅ | 218.00 | - | - |
| input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0 | ✅ | 148.84 | - | - |
| input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512 | ✅ | 175.57 | - | - |
| input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32 | ✅ | 146.36 | - | - |
| input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False | ✅ | 184.00 | - | - |
| input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True | ✅ | 183.30 | - | - |
| input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256 | ✅ | 176.58 | - | - |
| input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32 | ✅ | 161.68 | - | - |
| input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False | ✅ | 196.56 | - | - |
| input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True | ✅ | 185.54 | - | - |
| input_length_1024-num_aie_columns_2-tile_size_512 | ✅ | 166.68 | - | - |
| input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0 | ✅ | 171.12 | - | - |
| input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0 | ✅ | 193.32 | - | - |
| input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256 | ✅ | 173.42 | - | - |
| input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32 | ✅ | 147.48 | - | - |
| input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False | ✅ | 164.68 | - | - |
| input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True | ✅ | 154.10 | - | - |
| input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128 | ✅ | 193.95 | - | - |
| input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32 | ✅ | 180.80 | - | - |
| input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False | ✅ | 192.28 | - | - |
| input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True | ✅ | 184.84 | - | - |
| input_length_1024-num_aie_columns_4-tile_size_256 | ✅ | 172.55 | - | - |
| input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0 | ✅ | 163.84 | - | - |
| input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0 | ✅ | 185.60 | - | - |
| input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128 | ✅ | 194.54 | - | - |
| input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32 | ✅ | 176.20 | - | - |
| input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False | ✅ | 173.50 | - | - |
| input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True | ✅ | 213.16 | - | - |
| input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64 | ✅ | 226.09 | - | - |
| input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32 | ✅ | 225.10 | - | - |
| input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False | ✅ | 231.26 | - | - |
| input_length_1024-num_aie_columns_8-tile_size_128 | ✅ | 181.22 | - | - |
| input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0 | ✅ | 166.82 | - | - |
| input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0 | ✅ | 221.22 | - | - |
| input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024 | ✅ | 162.02 | - | - |
| input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024 | ✅ | 155.56 | - | - |
| input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64 | ✅ | 193.84 | - | - |
| input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64 | ✅ | 168.16 | - | - |
| input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512 | ✅ | 160.78 | - | - |
| input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512 | ✅ | 172.24 | - | - |
| input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512 | ✅ | 161.84 | - | - |
| input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512 | ✅ | 159.56 | - | - |
| input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256 | ✅ | 170.02 | - | - |
| input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256 | ✅ | 174.38 | - | - |
| input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256 | ✅ | 150.64 | - | - |
| input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256 | ✅ | 156.32 | - | - |
| input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128 | ✅ | 181.86 | - | - |
| input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128 | ✅ | 172.70 | - | - |
| input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128 | ✅ | 192.38 | - | - |
| input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128 | ✅ | 185.18 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048 | ✅ | 183.22 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32 | ✅ | 174.52 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False | ✅ | 163.34 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True | ✅ | 170.50 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024 | ✅ | 176.10 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32 | ✅ | 160.92 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False | ✅ | 194.12 | - | - |
| input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True | ✅ | 168.94 | - | - |
| input_length_2048-num_aie_columns_1-tile_size_2048 | ✅ | 168.89 | - | - |
| input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0 | ✅ | 154.72 | - | - |
| input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0 | ✅ | 153.66 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024 | ✅ | 175.27 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32 | ✅ | 186.78 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False | ✅ | 154.70 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True | ✅ | 202.72 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512 | ✅ | 179.70 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32 | ✅ | 197.98 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False | ✅ | 169.98 | - | - |
| input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True | ✅ | 174.82 | - | - |
| input_length_2048-num_aie_columns_2-tile_size_1024 | ✅ | 172.32 | - | - |
| input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0 | ✅ | 175.02 | - | - |
| input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0 | ✅ | 207.66 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512 | ✅ | 183.93 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32 | ✅ | 194.34 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False | ✅ | 176.38 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True | ✅ | 213.04 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256 | ✅ | 198.82 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32 | ✅ | 198.36 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False | ✅ | 183.20 | - | - |
| input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True | ✅ | 264.68 | - | - |
| input_length_2048-num_aie_columns_4-tile_size_512 | ✅ | 169.67 | - | - |
| input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0 | ✅ | 146.56 | - | - |
| input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0 | ✅ | 170.16 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256 | ✅ | 188.84 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32 | ✅ | 200.28 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False | ✅ | 197.82 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True | ✅ | 252.94 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128 | ✅ | 228.94 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32 | ✅ | 220.46 | - | - |
| input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False | ✅ | 226.48 | - | - |
| input_length_2048-num_aie_columns_8-tile_size_256 | ✅ | 188.73 | - | - |
| input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0 | ✅ | 197.40 | - | - |
| input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0 | ✅ | 204.26 | - | - |
| input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048 | ✅ | 147.06 | - | - |
| input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048 | ✅ | 144.16 | - | - |
| input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128 | ✅ | 230.28 | - | - |
| input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128 | ✅ | 181.56 | - | - |
| input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024 | ✅ | 168.10 | - | - |
| input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024 | ✅ | 153.74 | - | - |
| input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024 | ✅ | 151.92 | - | - |
| input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024 | ✅ | 164.58 | - | - |
| input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512 | ✅ | 200.20 | - | - |
| input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512 | ✅ | 150.48 | - | - |
| input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512 | ✅ | 168.46 | - | - |
| input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512 | ✅ | 184.82 | - | - |
| input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256 | ✅ | 193.30 | - | - |
| input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256 | ✅ | 164.78 | - | - |
| input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256 | ✅ | 183.26 | - | - |
| input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256 | ✅ | 173.66 | - | - |
| input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024 | ✅ | 152.14 | - | - |
| input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048 | ✅ | 176.28 | - | - |
| input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512 | ✅ | 175.90 | - | - |
| input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096 | ✅ | 171.84 | - | - |
| input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32 | ✅ | 144.54 | - | - |
| input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False | ✅ | 160.02 | - | - |
| input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True | ✅ | 189.90 | - | - |
| input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048 | ✅ | 179.17 | - | - |
| input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32 | ✅ | 163.04 | - | - |
| input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False | ✅ | 166.16 | - | - |
| input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True | ✅ | 187.62 | - | - |
| input_length_4096-num_aie_columns_1-tile_size_4096 | ✅ | 171.55 | - | - |
| input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0 | ✅ | 244.00 | - | - |
| input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0 | ✅ | 152.62 | - | - |
| input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048 | ✅ | 174.90 | - | - |
| input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32 | ✅ | 164.88 | - | - |
| input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False | ✅ | 170.22 | - | - |
| input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True | ✅ | 177.94 | - | - |
| input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024 | ✅ | 192.18 | - | - |
| input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32 | ✅ | 158.12 | - | - |
| input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False | ✅ | 180.14 | - | - |
| input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True | ✅ | 191.78 | - | - |
| input_length_4096-num_aie_columns_2-tile_size_2048 | ✅ | 188.09 | - | - |
| input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0 | ✅ | 164.16 | - | - |
| input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0 | ✅ | 169.96 | - | - |
| input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024 | ✅ | 176.41 | - | - |
| input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32 | ✅ | 197.46 | - | - |
| input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False | ✅ | 149.16 | - | - |
| input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True | ✅ | 191.54 | - | - |
| input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512 | ✅ | 187.46 | - | - |
| input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32 | ✅ | 193.88 | - | - |
| input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False | ✅ | 198.26 | - | - |
| input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True | ✅ | 242.86 | - | - |
| input_length_4096-num_aie_columns_4-tile_size_1024 | ✅ | 181.28 | - | - |
| input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0 | ✅ | 204.56 | - | - |
| input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0 | ✅ | 183.44 | - | - |
| input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512 | ✅ | 192.84 | - | - |
| input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32 | ✅ | 180.78 | - | - |
| input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False | ✅ | 159.98 | - | - |
| input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True | ✅ | 220.66 | - | - |
| input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256 | ✅ | 235.49 | - | - |
| input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32 | ✅ | 235.72 | - | - |
| input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False | ✅ | 226.06 | - | - |
| input_length_4096-num_aie_columns_8-tile_size_512 | ✅ | 197.05 | - | - |
| input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0 | ✅ | 216.30 | - | - |
| input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0 | ✅ | 187.06 | - | - |
| input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096 | ✅ | 133.24 | - | - |
| input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096 | ✅ | 168.36 | - | - |
| input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256 | ✅ | 219.14 | - | - |
| input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256 | ✅ | 196.86 | - | - |
| input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048 | ✅ | 148.04 | - | - |
| input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048 | ✅ | 138.02 | - | - |
| input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048 | ✅ | 167.94 | - | - |
| input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048 | ✅ | 150.66 | - | - |
| input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024 | ✅ | 176.18 | - | - |
| input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024 | ✅ | 166.52 | - | - |
| input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024 | ✅ | 159.58 | - | - |
| input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024 | ✅ | 140.86 | - | - |
| input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512 | ✅ | 167.40 | - | - |
| input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512 | ✅ | 155.18 | - | - |
| input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512 | ✅ | 200.82 | - | - |
| input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512 | ✅ | 153.46 | - | - |
| input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192 | ✅ | 204.85 | - | - |
| input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32 | ✅ | 187.52 | - | - |
| input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False | ✅ | 197.38 | - | - |
| input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096 | ✅ | 179.95 | - | - |
| input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32 | ✅ | 182.36 | - | - |
| input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False | ✅ | 173.74 | - | - |
| input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True | ✅ | 207.96 | - | - |
| input_length_8192-num_aie_columns_1-tile_size_8192 | ✅ | 170.06 | - | - |
| input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0 | ✅ | 175.96 | - | - |
| input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0 | ✅ | 165.68 | - | - |
| input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096 | ✅ | 177.45 | - | - |
| input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32 | ✅ | 212.72 | - | - |
| input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False | ✅ | 201.32 | - | - |
| input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True | ✅ | 179.12 | - | - |
| input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048 | ✅ | 175.88 | - | - |
| input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32 | ✅ | 180.66 | - | - |
| input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False | ✅ | 192.10 | - | - |
| input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True | ✅ | 204.42 | - | - |
| input_length_8192-num_aie_columns_2-tile_size_4096 | ✅ | 157.64 | - | - |
| input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0 | ✅ | 165.94 | - | - |
| input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0 | ✅ | 178.18 | - | - |
| input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048 | ✅ | 172.76 | - | - |
| input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32 | ✅ | 175.66 | - | - |
| input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False | ✅ | 179.76 | - | - |
| input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True | ✅ | 204.48 | - | - |
| input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024 | ✅ | 203.79 | - | - |
| input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32 | ✅ | 204.48 | - | - |
| input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False | ✅ | 193.70 | - | - |
| input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True | ✅ | 261.48 | - | - |
| input_length_8192-num_aie_columns_4-tile_size_2048 | ✅ | 156.48 | - | - |
| input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0 | ✅ | 181.26 | - | - |
| input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0 | ✅ | 196.32 | - | - |
| input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024 | ✅ | 186.94 | - | - |
| input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32 | ✅ | 184.08 | - | - |
| input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False | ✅ | 194.24 | - | - |
| input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True | ✅ | 213.52 | - | - |
| input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512 | ✅ | 223.67 | - | - |
| input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32 | ✅ | 229.84 | - | - |
| input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False | ✅ | 231.54 | - | - |
| input_length_8192-num_aie_columns_8-tile_size_1024 | ✅ | 191.88 | - | - |
| input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0 | ✅ | 236.46 | - | - |
| input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0 | ✅ | 228.72 | - | - |
| input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192 | ✅ | 164.66 | - | - |
| input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192 | ✅ | 128.50 | - | - |
| input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512 | ✅ | 206.00 | - | - |
| input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512 | ✅ | 196.78 | - | - |
| input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096 | ✅ | 146.64 | - | - |
| input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096 | ✅ | 162.60 | - | - |
| input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096 | ✅ | 167.46 | - | - |
| input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096 | ✅ | 157.14 | - | - |
| input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048 | ✅ | 181.30 | - | - |
| input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048 | ✅ | 152.00 | - | - |
| input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048 | ✅ | 168.36 | - | - |
| input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048 | ✅ | 169.16 | - | - |
| input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024 | ✅ | 212.64 | - | - |
| input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024 | ✅ | 181.48 | - | - |
| input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024 | ✅ | 162.10 | - | - |
| input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024 | ✅ | 173.06 | - | - |
| rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0 | ✅ | 175.34 | - | - |
| rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1 | ✅ | 226.36 | - | - |
| rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0 | ✅ | 164.76 | - | - |
| rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1 | ✅ | 173.64 | - | - |
| rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0 | ✅ | 167.72 | - | - |
| rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1 | ✅ | 188.86 | - | - |
| rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0 | ✅ | 188.70 | - | - |
| rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1 | ✅ | 215.80 | - | - |
| rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0 | ✅ | 171.10 | - | - |
| rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1 | ✅ | 171.66 | - | - |
| rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0 | ✅ | 162.04 | - | - |
| rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1 | ✅ | 153.26 | - | - |
| rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0 | ✅ | 167.22 | - | - |
| rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1 | ✅ | 170.10 | - | - |
| rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0 | ✅ | 186.42 | - | - |
| rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1 | ✅ | 209.90 | - | - |
| rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0 | ✅ | 172.34 | - | - |
| rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1 | ✅ | 160.48 | - | - |
| rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0 | ✅ | 179.52 | - | - |
| rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1 | ✅ | 186.64 | - | - |
| rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0 | ✅ | 225.98 | - | - |
| rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1 | ✅ | 190.24 | - | - |
| rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0 | ✅ | 187.86 | - | - |
| rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1 | ✅ | 194.40 | - | - |
| rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0 | ✅ | 174.40 | - | - |
| rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0 | ✅ | 175.80 | - | - |
| rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0 | ✅ | 208.68 | - | - |
| rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0 | ✅ | 205.54 | - | - |
| rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0 | ✅ | 169.92 | - | - |
| rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0 | ✅ | 170.94 | - | - |
| rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0 | ✅ | 180.58 | - | - |
| rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0 | ✅ | 212.54 | - | - |
| rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0 | ✅ | 149.74 | - | - |
| rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1 | ✅ | 186.74 | - | - |
| rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0 | ✅ | 190.30 | - | - |
| rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1 | ✅ | 181.38 | - | - |
| rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0 | ✅ | 180.48 | - | - |
| rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1 | ✅ | 184.12 | - | - |
| rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0 | ✅ | 256.34 | - | - |
| rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1 | ✅ | 213.74 | - | - |
| rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0 | ✅ | 186.06 | - | - |
| rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1 | ✅ | 159.80 | - | - |
| rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0 | ✅ | 182.30 | - | - |
| rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1 | ✅ | 205.94 | - | - |
| rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0 | ✅ | 174.98 | - | - |
| rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1 | ✅ | 182.86 | - | - |
| rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0 | ✅ | 246.90 | - | - |
| rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1 | ✅ | 221.84 | - | - |
| rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0 | ✅ | 217.28 | - | - |
| rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1 | ✅ | 174.96 | - | - |
| rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0 | ✅ | 186.86 | - | - |
| rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1 | ✅ | 156.72 | - | - |
| rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0 | ✅ | 179.10 | - | - |
| rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1 | ✅ | 172.22 | - | - |
| rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0 | ✅ | 213.04 | - | - |
| rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1 | ✅ | 215.70 | - | - |
| seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0 | ✅ | 40636.28 | - | - |
| seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0 | ✅ | 40593.88 | - | - |
| seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2 | ✅ | 320082.52 | - | - |
| seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False | ✅ | 9816.38 | - | - |

</details>

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0] | - | - | ✅ | 374.10 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0] | - | - | ✅ | 332.44 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0] | - | - | ✅ | 443.88 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0] | - | - | ✅ | 378.42 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0] | - | - | ✅ | 811.42 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | - | - | ✅ | 344.70 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0] | - | - | ✅ | 314.64 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | - | - | ✅ | 632.02 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0] | - | - | ✅ | 280.12 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | - | - | ✅ | 374.24 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0] | - | - | ✅ | 337.26 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | - | - | ✅ | 369.20 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0] | - | - | ✅ | 352.28 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 310.26 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0] | - | - | ✅ | 624.34 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0] | - | - | ✅ | 388.58 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0] | - | - | ✅ | 377.76 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0] | - | - | ✅ | 613.66 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0] | - | - | ✅ | 309.00 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0] | - | - | ✅ | 402.88 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0] | - | - | ✅ | 317.58 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 326.54 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0] | - | - | ✅ | 420.40 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0] | - | - | ✅ | 724.58 |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32] | - | - | ✅ | 301.04 |
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32] | - | - | ✅ | 843.90 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32] | - | - | ✅ | 359.16 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32] | - | - | ✅ | 373.36 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32] | - | - | ✅ | 373.54 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32] | - | - | ✅ | 451.04 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | - | - | ✅ | 389.44 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | - | - | ✅ | 435.76 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | - | - | ✅ | 487.74 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | - | - | ✅ | 584.44 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | - | - | ✅ | 447.92 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | - | - | ✅ | 437.56 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32] | - | - | ✅ | 403.98 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32] | - | - | ✅ | 425.88 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32] | - | - | ✅ | 416.16 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32] | - | - | ✅ | 472.22 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32] | - | - | ✅ | 392.62 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32] | - | - | ✅ | 474.26 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32] | - | - | ✅ | 355.76 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32] | - | - | ✅ | 439.44 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32] | - | - | ✅ | 496.94 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32] | - | - | ✅ | 455.04 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32] | - | - | ✅ | 328.60 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32] | - | - | ✅ | 431.00 |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024] | - | - | ✅ | 410.98 |
| test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512] | - | - | ✅ | 452.98 |
| test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256] | - | - | ✅ | 414.76 |
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | - | - | ✅ | 721.84 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | - | - | ✅ | 858.02 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | - | - | ✅ | 580.18 |
| test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096] | - | - | ✅ | 444.54 |
| test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048] | - | - | ✅ | 512.64 |
| test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024] | - | - | ✅ | 568.18 |
| test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192] | - | - | ✅ | 488.86 |
| test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096] | - | - | ✅ | 467.28 |
| test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048] | - | - | ✅ | 480.52 |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024] | - | - | ✅ | 410.50 |
| test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512] | - | - | ✅ | 451.96 |
| test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256] | - | - | ✅ | 475.36 |
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | - | - | ✅ | 266.88 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | - | - | ✅ | 422.76 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | - | - | ✅ | 299.26 |
| test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096] | - | - | ✅ | 395.72 |
| test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048] | - | - | ✅ | 390.20 |
| test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024] | - | - | ✅ | 558.30 |
| test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096] | - | - | ✅ | 349.10 |
| test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048] | - | - | ✅ | 515.52 |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | - | - | ✅ | 270.20 |
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | - | - | ✅ | 315.30 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | - | - | ✅ | 309.20 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | - | - | ✅ | 432.02 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | - | - | ✅ | 369.60 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 308.68 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 437.92 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | - | - | ✅ | 395.12 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 362.64 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 540.88 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 563.60 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 454.36 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 685.44 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | - | - | ✅ | 327.06 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | - | - | ✅ | 394.64 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | - | - | ✅ | 386.10 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | - | - | ✅ | 324.34 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | - | - | ✅ | 455.04 |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | - | - | ✅ | 256.58 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | - | - | ✅ | 335.04 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | - | - | ✅ | 385.16 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | - | - | ✅ | 459.78 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | - | - | ✅ | 554.16 |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1] | - | - | ✅ | 615.24 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1] | - | - | ✅ | 476.22 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 82931.28 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 25718.46 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 95662.44 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 99334.16 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 97266.42 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 2860.54 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 2478.58 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 3066.20 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 6936.00 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 7471.12 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 6249.30 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 98672.68 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 99763.34 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 95368.28 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1] | - | - | ✅ | 3669.86 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4] | - | - | ✅ | 5777.88 |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | - | - | ✅ | 0.08 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | - | - | ✅ | 3.57 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | - | - | ✅ | 6.29 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | - | - | ✅ | 11.59 |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | - | - | ✅ | 3.78 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | - | - | ✅ | 6.14 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | - | - | ✅ | 9.53 |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | - | - | ✅ | 350.60 |
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | - | - | ✅ | 411.06 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | - | - | ✅ | 364.22 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | - | - | ✅ | 410.02 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | - | - | ✅ | 388.32 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 426.92 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 305.34 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | - | - | ✅ | 445.36 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 385.30 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 388.30 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 258.08 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 514.20 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 320.52 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | - | - | ✅ | 446.32 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | - | - | ✅ | 402.96 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | - | - | ✅ | 418.44 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | - | - | ✅ | 470.98 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | - | - | ✅ | 722.70 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | - | - | ✅ | 438.58 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | - | - | ✅ | 415.02 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | - | - | ✅ | 726.06 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | - | - | ✅ | 463.32 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | - | - | ✅ | 640.34 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | - | - | ✅ | 651.40 |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024] | - | - | ✅ | 370.10 |
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024] | - | - | ✅ | 462.20 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512] | - | - | ✅ | 413.36 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512] | - | - | ✅ | 269.86 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512] | - | - | ✅ | 362.08 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512] | - | - | ✅ | 267.50 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256] | - | - | ✅ | 363.30 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256] | - | - | ✅ | 521.52 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256] | - | - | ✅ | 389.72 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256] | - | - | ✅ | 480.78 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128] | - | - | ✅ | 452.02 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128] | - | - | ✅ | 415.44 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | - | - | ✅ | 383.84 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048] | - | - | ✅ | 380.36 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | - | - | ✅ | 438.62 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024] | - | - | ✅ | 299.84 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | - | - | ✅ | 790.44 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024] | - | - | ✅ | 653.56 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | - | - | ✅ | 691.02 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512] | - | - | ✅ | 469.22 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | - | - | ✅ | 574.72 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512] | - | - | ✅ | 567.06 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | - | - | ✅ | 451.70 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256] | - | - | ✅ | 389.98 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096] | - | - | ✅ | 315.64 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096] | - | - | ✅ | 384.82 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048] | - | - | ✅ | 308.82 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048] | - | - | ✅ | 417.42 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048] | - | - | ✅ | 372.44 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048] | - | - | ✅ | 297.50 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024] | - | - | ✅ | 393.28 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024] | - | - | ✅ | 800.14 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024] | - | - | ✅ | 444.82 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024] | - | - | ✅ | 363.00 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512] | - | - | ✅ | 399.18 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512] | - | - | ✅ | 761.38 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192] | - | - | ✅ | 403.74 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192] | - | - | ✅ | 350.62 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096] | - | - | ✅ | 282.86 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096] | - | - | ✅ | 381.50 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096] | - | - | ✅ | 463.88 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096] | - | - | ✅ | 369.72 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048] | - | - | ✅ | 343.92 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048] | - | - | ✅ | 366.06 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048] | - | - | ✅ | 480.12 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048] | - | - | ✅ | 477.54 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024] | - | - | ✅ | 803.96 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024] | - | - | ✅ | 365.46 |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | - | - | ✅ | 336.88 |
| test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | - | - | ✅ | 451.26 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | - | - | ✅ | 385.26 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | - | - | ✅ | 404.20 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | - | - | ✅ | 480.96 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 456.82 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 309.78 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | - | - | ✅ | 245.48 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 359.06 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 444.26 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 512.70 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 448.94 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 311.40 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | - | - | ✅ | 465.40 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | - | - | ✅ | 353.66 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | - | - | ✅ | 624.14 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | - | - | ✅ | 357.34 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | - | - | ✅ | 631.88 |
| test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | - | - | ✅ | 388.66 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | - | - | ✅ | 451.58 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | - | - | ✅ | 430.62 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | - | - | ✅ | 391.20 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | - | - | ✅ | 484.66 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False] | - | - | ✅ | 387.46 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True] | - | - | ✅ | 593.38 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False] | - | - | ✅ | 510.16 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True] | - | - | ✅ | 664.46 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False] | - | - | ✅ | 396.66 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True] | - | - | ✅ | 413.46 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False] | - | - | ✅ | 484.62 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True] | - | - | ✅ | 351.86 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False] | - | - | ✅ | 423.46 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | - | - | ✅ | 347.94 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False] | - | - | ✅ | 425.28 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | - | - | ✅ | 430.88 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | - | - | ✅ | 343.54 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | - | - | ✅ | 351.98 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | - | - | ✅ | 481.20 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | - | - | ✅ | 409.12 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | - | - | ✅ | 523.68 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | - | - | ✅ | 419.92 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | - | - | ✅ | 500.00 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | - | - | ✅ | 412.50 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | - | - | ✅ | 372.86 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | - | - | ✅ | 416.68 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False] | - | - | ✅ | 316.32 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | - | - | ✅ | 396.20 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False] | - | - | ✅ | 297.30 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True] | - | - | ✅ | 457.08 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False] | - | - | ✅ | 832.96 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True] | - | - | ✅ | 382.04 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False] | - | - | ✅ | 316.30 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True] | - | - | ✅ | 370.58 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False] | - | - | ✅ | 402.08 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True] | - | - | ✅ | 383.86 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False] | - | - | ✅ | 411.92 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False] | - | - | ✅ | 397.46 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False] | - | - | ✅ | 290.78 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 733.74 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False] | - | - | ✅ | 395.02 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True] | - | - | ✅ | 378.46 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False] | - | - | ✅ | 457.54 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True] | - | - | ✅ | 418.00 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False] | - | - | ✅ | 517.58 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True] | - | - | ✅ | 380.80 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False] | - | - | ✅ | 742.72 |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0] | - | - | ✅ | 300.10 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1] | - | - | ✅ | 630.30 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0] | - | - | ✅ | 431.88 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1] | - | - | ✅ | 321.74 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0] | - | - | ✅ | 471.20 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1] | - | - | ✅ | 610.36 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0] | - | - | ✅ | 389.94 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1] | - | - | ✅ | 283.02 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0] | - | - | ✅ | 331.48 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1] | - | - | ✅ | 353.88 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0] | - | - | ✅ | 389.46 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1] | - | - | ✅ | 464.32 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0] | - | - | ✅ | 783.52 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1] | - | - | ✅ | 390.96 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0] | - | - | ✅ | 289.78 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1] | - | - | ✅ | 518.36 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 352.80 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1] | - | - | ✅ | 427.54 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | - | - | ✅ | 399.82 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | - | - | ✅ | 354.84 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | - | - | ✅ | 421.16 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | - | - | ✅ | 398.44 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | - | - | ✅ | 364.06 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 357.50 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0] | - | - | ✅ | 334.38 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1] | - | - | ✅ | 414.64 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0] | - | - | ✅ | 778.42 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1] | - | - | ✅ | 355.50 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0] | - | - | ✅ | 366.46 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1] | - | - | ✅ | 344.20 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0] | - | - | ✅ | 377.22 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1] | - | - | ✅ | 393.80 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0] | - | - | ✅ | 393.92 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1] | - | - | ✅ | 348.10 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0] | - | - | ✅ | 395.50 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1] | - | - | ✅ | 411.02 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0] | - | - | ✅ | 443.08 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1] | - | - | ✅ | 328.92 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0] | - | - | ✅ | 356.58 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1] | - | - | ✅ | 463.60 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 356.66 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1] | - | - | ✅ | 860.12 |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | - | - | ✅ | 439.24 |
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | - | - | ✅ | 408.64 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | - | - | ✅ | 731.14 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | - | - | ✅ | 309.04 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | - | - | ✅ | 429.36 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 865.56 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 283.60 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | - | - | ✅ | 271.30 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 281.98 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 428.94 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 482.36 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 494.70 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 724.60 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | - | - | ✅ | 439.06 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | - | - | ✅ | 344.22 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | - | - | ✅ | 455.62 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | - | - | ✅ | 252.54 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | - | - | ✅ | 476.56 |
| test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | - | - | ✅ | 383.62 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | - | - | ✅ | 435.22 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | - | - | ✅ | 417.38 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | - | - | ✅ | 382.34 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | - | - | ✅ | 493.94 |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | - | - | ✅ | 654.04 |
| test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | - | - | ✅ | 325.52 |
| test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | - | - | ✅ | 447.40 |
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 365.16 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 442.30 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 320.78 |
| test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 321.84 |
| test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | - | - | ✅ | 518.96 |
| test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | - | - | ✅ | 506.74 |
| test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | - | - | ✅ | 433.92 |
| test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | - | - | ✅ | 491.36 |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | - | - | ✅ | 392.54 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | - | - | ✅ | 402.38 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 1042.16 |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | - | - | ✅ | 13293.57 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | - | - | ✅ | 15432.11 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False] | - | - | ✅ | 22495.50 |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | - | - | ✅ | 345.60 |
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | - | - | ✅ | 454.74 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | - | - | ✅ | 443.90 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | - | - | ✅ | 437.90 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | - | - | ✅ | 435.38 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | - | - | ✅ | 405.68 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | - | - | ✅ | 401.32 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | - | - | ✅ | 412.72 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | - | - | ✅ | 438.86 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | - | - | ✅ | 581.74 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | - | - | ✅ | 339.54 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | - | - | ✅ | 624.32 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | - | - | ✅ | 371.02 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | - | - | ✅ | 399.36 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | - | - | ✅ | 424.74 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | - | - | ✅ | 643.08 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | - | - | ✅ | 456.22 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | - | - | ✅ | 404.08 |
| test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | - | - | ✅ | 444.14 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | - | - | ✅ | 489.74 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | - | - | ✅ | 375.76 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | - | - | ✅ | 392.02 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | - | - | ✅ | 404.76 |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8] | - | - | ✅ | 600.30 |
| test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8] | - | - | ✅ | 991.08 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8] | - | - | ✅ | 557.56 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8] | - | - | ✅ | 449.62 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8] | - | - | ✅ | 1763.64 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8] | - | - | ✅ | 1761.00 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8] | - | - | ✅ | 1210.34 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8] | - | - | ✅ | 1274.68 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8] | - | - | ✅ | 882.34 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8] | - | - | ✅ | 936.00 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8] | - | - | ✅ | 1670.92 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8] | - | - | ✅ | 1960.18 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8] | - | - | ✅ | 1264.14 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8] | - | - | ✅ | 746.58 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8] | - | - | ✅ | 1122.06 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8] | - | - | ✅ | 793.22 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8] | - | - | ✅ | 1011.36 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8] | - | - | ✅ | 679.58 |
| test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8] | - | - | ✅ | 446.70 |
| test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8] | - | - | ✅ | 724.06 |
| test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8] | - | - | ✅ | 452.68 |
| test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8] | - | - | ✅ | 420.00 |
| test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8] | - | - | ✅ | 494.16 |
| test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8] | - | - | ✅ | 491.76 |
| test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8] | - | - | ✅ | 817.66 |
| test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8] | - | - | ✅ | 775.14 |
| test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8] | - | - | ✅ | 502.90 |

</details>

