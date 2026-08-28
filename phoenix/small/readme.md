
# IRON

Tested on `2026_08_28_20_14_14` at commit `9b92482`.

<details>
<summary>iron/operators/axpy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>409.44</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>530.82</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>435.10</td><td>0.03</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/dequant</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>356.32</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>426.56</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>416.94</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>359.72</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>560.50</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>665.28</td><td>0.01</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>387.02</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>474.26</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>499.86</td><td>0.03</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>329.90</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>447.38</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>439.86</td><td>0.03</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gelu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>372.20</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>408.14</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>409.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>396.64</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>297.38</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>446.02</td><td>0.02</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gemm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>531.24</td><td>0.43</td><td>18.46</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>515.74</td><td>0.47</td><td>20.17</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>82653.04</td><td>0.30</td><td>208.01</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>25265.40</td><td>1.00</td><td>680.30</td></tr>
        <tr><td>test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>4309.28</td><td>1.91</td><td>499.76</td></tr>
        <tr><td>test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4]</td><td>✅ 5/5</td><td>6194.88</td><td>0.21</td><td>11.17</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gemv</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 5/5</td><td>n/a</td><td>0.10</td><td>0.10</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>✅ 5/5</td><td>n/a</td><td>3.68</td><td>3.68</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>7.19</td><td>7.19</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512]</td><td>✅ 5/5</td><td>n/a</td><td>9.77</td><td>9.77</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>3.65</td><td>3.65</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>6.92</td><td>6.92</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>10.57</td><td>10.56</td></tr>
        <tr><td>test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2]</td><td>✅ 5/5</td><td>n/a</td><td>1.89</td><td>1.89</td></tr>
        <tr><td>test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2]</td><td>✅ 5/5</td><td>n/a</td><td>0.44</td><td>0.43</td></tr>
        <tr><td>test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]</td><td>✅ 5/5</td><td>n/a</td><td>0.46</td><td>0.45</td></tr>
        <tr><td>test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8]</td><td>✅ 5/5</td><td>n/a</td><td>1.23</td><td>1.21</td></tr>
        <tr><td>test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/layer_norm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>357.14</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>691.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>384.80</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>380.92</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>419.44</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>410.54</td><td>0.02</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>464.46</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1]</td><td>✅ 5/5</td><td>807.16</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25]</td><td>✅ 5/5</td><td>301.46</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>382.84</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>371.04</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>414.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>333.16</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>778.52</td><td>0.01</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/mem_copy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>240.74</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>304.30</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>801.28</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>395.36</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>344.58</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>503.56</td><td>0.02</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/relu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>358.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>443.12</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>418.74</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>399.24</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>620.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>431.54</td><td>0.02</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/rms_norm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>311.82</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>411.24</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>409.70</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>641.72</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>503.50</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>541.72</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>345.16</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>493.60</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>450.18</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>616.10</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>487.26</td><td>0.02</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/rope</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>400.38</td><td>0.26</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>546.76</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>474.36</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>406.06</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>649.96</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>518.46</td><td>0.16</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/sigmoid</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>509.26</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>506.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>325.24</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>333.72</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>374.88</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>522.20</td><td>0.02</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/silu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>310.42</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>318.20</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>292.14</td><td>0.03</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/softmax</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>375.60</td><td>0.37</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>452.26</td><td>0.34</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>443.76</td><td>0.33</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_swiglu_decode[embedding_dim_1024-hidden_dim_3584]</td><td>✅ 5/5</td><td>17921.90</td><td>0.00</td><td>n/a</td></tr>
        <tr><td>test_swiglu_decode[embedding_dim_2048-hidden_dim_2048]</td><td>✅ 5/5</td><td>17402.61</td><td>0.00</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False]</td><td>✅ 5/5</td><td>24018.04</td><td>0.09</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/tanh</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>390.14</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>445.74</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>446.96</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>537.78</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>476.58</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>450.40</td><td>0.02</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/transpose</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>419.74</td><td>1.32</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2]</td><td>✅ 5/5</td><td>1052.42</td><td>1.82</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>468.96</td><td>1.22</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

