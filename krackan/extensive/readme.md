
# IRON

Tested on `2026_07_09_23_33_58` at commit `17769b8`.

<details>
<summary>iron/operators/axpy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>165.24</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>183.68</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>187.28</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>182.40</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0]</td><td>✅ 5/5</td><td>175.52</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]</td><td>✅ 5/5</td><td>198.94</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0]</td><td>✅ 5/5</td><td>202.68</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0]</td><td>✅ 5/5</td><td>180.50</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>149.58</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>167.98</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>160.84</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>157.46</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>150.82</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>192.30</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0]</td><td>✅ 5/5</td><td>166.60</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0]</td><td>✅ 5/5</td><td>183.18</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0]</td><td>✅ 5/5</td><td>198.90</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>173.04</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>205.92</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>161.82</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>165.56</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>181.60</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>195.46</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>182.86</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0]</td><td>✅ 5/5</td><td>174.90</td><td>0.28</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0]</td><td>✅ 5/5</td><td>159.98</td><td>0.32</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0]</td><td>✅ 5/5</td><td>152.20</td><td>0.33</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>161.42</td><td>0.31</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>167.16</td><td>0.30</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>164.50</td><td>0.31</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>198.54</td><td>0.25</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>192.88</td><td>0.26</td><td>n/a</td></tr>
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
        <tr><td>test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>155.58</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>174.12</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>161.70</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>159.78</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>182.78</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>177.30</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>203.14</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32]</td><td>✅ 5/5</td><td>218.06</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>157.92</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>184.08</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>162.76</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>182.78</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>187.90</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>197.64</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>231.58</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>215.60</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>185.68</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>176.54</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>167.70</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>209.02</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>188.78</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>186.76</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>159.28</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>225.80</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32]</td><td>✅ 5/5</td><td>157.84</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>177.36</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>147.90</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>167.18</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>187.22</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>186.44</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>181.36</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>222.76</td><td>0.10</td><td>n/a</td></tr>
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
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024]</td><td>✅ 5/5</td><td>159.22</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512]</td><td>✅ 5/5</td><td>176.22</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 5/5</td><td>243.92</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128]</td><td>✅ 5/5</td><td>211.16</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>189.18</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>170.62</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>169.58</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256]</td><td>✅ 5/5</td><td>207.00</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 5/5</td><td>155.40</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048]</td><td>✅ 5/5</td><td>170.32</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024]</td><td>✅ 5/5</td><td>176.10</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512]</td><td>✅ 5/5</td><td>176.40</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192]</td><td>✅ 5/5</td><td>214.70</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096]</td><td>✅ 5/5</td><td>179.70</td><td>0.28</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048]</td><td>✅ 5/5</td><td>173.26</td><td>0.29</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024]</td><td>✅ 5/5</td><td>201.86</td><td>0.26</td><td>n/a</td></tr>
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
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024]</td><td>✅ 5/5</td><td>140.06</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512]</td><td>✅ 5/5</td><td>189.08</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 5/5</td><td>150.18</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128]</td><td>✅ 5/5</td><td>183.82</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>149.12</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>154.42</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>200.42</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256]</td><td>✅ 5/5</td><td>182.42</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 5/5</td><td>158.28</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048]</td><td>✅ 5/5</td><td>151.48</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024]</td><td>✅ 5/5</td><td>188.64</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512]</td><td>✅ 5/5</td><td>185.16</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096]</td><td>✅ 5/5</td><td>165.48</td><td>0.31</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048]</td><td>✅ 5/5</td><td>141.18</td><td>0.36</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024]</td><td>✅ 5/5</td><td>162.26</td><td>0.30</td><td>n/a</td></tr>
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
        <tr><td>test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>175.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>204.44</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>200.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>171.30</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>179.56</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>178.14</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>191.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>216.50</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>157.64</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>167.08</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>169.08</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>163.20</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>167.06</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>236.30</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>189.92</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>247.50</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>198.74</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>186.46</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>182.44</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>186.26</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>199.26</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>188.66</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>221.30</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>235.14</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>204.16</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>184.24</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>194.82</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>191.64</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>205.24</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>203.38</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>256.50</td><td>0.13</td><td>n/a</td></tr>
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
        <tr><td>test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>2339.42</td><td>4.09</td><td>1608.36</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>237.40</td><td>0.94</td><td>40.25</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>238.10</td><td>0.98</td><td>41.95</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>48641.44</td><td>0.52</td><td>353.19</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>118282.30</td><td>0.21</td><td>145.25</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>28301.36</td><td>0.89</td><td>607.11</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>7349.78</td><td>3.43</td><td>2339.00</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>8994.48</td><td>2.80</td><td>1910.87</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>7908.20</td><td>3.18</td><td>2173.36</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>96464.64</td><td>0.78</td><td>712.38</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>103715.18</td><td>0.73</td><td>662.58</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>109385.24</td><td>0.69</td><td>628.23</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1216.50</td><td>7.33</td><td>441.69</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1325.56</td><td>6.73</td><td>405.60</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1528.22</td><td>6.02</td><td>362.66</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>4531.40</td><td>7.71</td><td>474.75</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>4636.86</td><td>7.52</td><td>463.36</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>4791.40</td><td>7.30</td><td>449.76</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>95803.78</td><td>0.79</td><td>717.29</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>102836.82</td><td>0.73</td><td>668.24</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>108113.32</td><td>0.70</td><td>635.63</td></tr>
        <tr><td>test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>2148.68</td><td>3.80</td><td>997.51</td></tr>
        <tr><td>test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4]</td><td>✅ 5/5</td><td>3652.48</td><td>0.34</td><td>18.45</td></tr>
        <tr><td>test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1415.08</td><td>4.71</td><td>1454.06</td></tr>
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
        <tr><td>test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 5/5</td><td>n/a</td><td>0.19</td><td>0.19</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>✅ 5/5</td><td>n/a</td><td>12.96</td><td>12.95</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>24.47</td><td>24.46</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512]</td><td>✅ 5/5</td><td>n/a</td><td>39.79</td><td>39.76</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256]</td><td>✅ 5/5</td><td>n/a</td><td>42.76</td><td>42.73</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>12.44</td><td>12.43</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>23.68</td><td>23.67</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>39.58</td><td>39.56</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>44.12</td><td>44.09</td></tr>
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
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>170.50</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>161.08</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>204.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>168.28</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>146.94</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>190.32</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>192.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>235.50</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>166.28</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>158.90</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>165.64</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>168.34</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>158.30</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>199.76</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>159.46</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>202.56</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>179.56</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>184.70</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>176.14</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>184.50</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>199.74</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>190.72</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>169.92</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>199.10</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 5/5</td><td>181.10</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>172.28</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>178.14</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>170.12</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>175.40</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>174.34</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>167.98</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>188.26</td><td>0.18</td><td>n/a</td></tr>
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
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>189.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>186.18</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>190.28</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>188.66</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>173.98</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>204.62</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>175.84</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01]</td><td>✅ 5/5</td><td>251.50</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>173.50</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1]</td><td>✅ 5/5</td><td>174.62</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25]</td><td>✅ 5/5</td><td>168.84</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>257.00</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>167.24</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>193.54</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>177.58</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>178.82</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>176.18</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>213.08</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>168.72</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>173.20</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>181.34</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>181.46</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>173.38</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>171.76</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>176.50</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>221.98</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>188.26</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>168.24</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>178.18</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>174.88</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>230.02</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>189.76</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>256.40</td><td>0.13</td><td>n/a</td></tr>
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
        <tr><td>test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>178.16</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>173.92</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64]</td><td>✅ 5/5</td><td>222.20</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64]</td><td>✅ 5/5</td><td>205.62</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>173.42</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>164.84</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>191.08</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>161.90</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>188.22</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>170.20</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>195.20</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>165.80</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>199.72</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128]</td><td>✅ 5/5</td><td>171.28</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>177.10</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128]</td><td>✅ 5/5</td><td>174.78</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>157.50</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>151.90</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>229.12</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128]</td><td>✅ 5/5</td><td>210.88</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>171.08</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>139.58</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>146.94</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>148.72</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>163.70</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>151.88</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>158.50</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>159.00</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>183.60</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>161.52</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>197.00</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>192.18</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>165.52</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>170.30</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>205.96</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>201.34</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>157.78</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>150.48</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>159.88</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>146.10</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>177.72</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>173.52</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>163.90</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>173.34</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>182.56</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>173.82</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>174.50</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>170.06</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192]</td><td>✅ 5/5</td><td>170.52</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192]</td><td>✅ 5/5</td><td>149.62</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>235.42</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>189.30</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>172.84</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>169.64</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>168.90</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>155.58</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>156.08</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>159.04</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>165.28</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>154.44</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>164.58</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>178.80</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>172.88</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>188.64</td><td>0.18</td><td>n/a</td></tr>
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
        <tr><td>test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>157.72</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>163.22</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>154.04</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>152.88</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>174.82</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>171.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>185.46</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>238.60</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>182.84</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>212.54</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>196.20</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>187.10</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>164.54</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>206.68</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>190.62</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>207.70</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>147.02</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>166.68</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>151.84</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>160.08</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>188.44</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>179.94</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>169.10</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>174.76</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>143.52</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>167.64</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>157.76</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>171.40</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>174.04</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>168.84</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>212.06</td><td>0.16</td><td>n/a</td></tr>
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
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>165.96</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>168.02</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>182.56</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>172.82</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>159.54</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>135.02</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>181.44</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>166.16</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>175.36</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>158.90</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>176.88</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True]</td><td>✅ 5/5</td><td>202.96</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>185.52</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True]</td><td>✅ 5/5</td><td>198.26</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False]</td><td>✅ 5/5</td><td>231.98</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>163.60</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>165.48</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>160.12</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>189.50</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>166.62</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>165.22</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>191.26</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>177.76</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>177.92</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>162.56</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>175.94</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>214.14</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>181.34</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>173.70</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>199.04</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>158.54</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>156.30</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>167.40</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>145.78</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>168.30</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>172.48</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>169.24</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>141.78</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>234.68</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>165.12</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>178.20</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>176.48</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>187.68</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>192.32</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>196.72</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False]</td><td>✅ 5/5</td><td>166.26</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>144.02</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>187.50</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>171.30</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>176.42</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>171.34</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>178.36</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>180.48</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>191.98</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>175.20</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>191.46</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>186.92</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>225.56</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>230.40</td><td>0.16</td><td>n/a</td></tr>
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
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>141.32</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>161.38</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>175.78</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>216.96</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>180.32</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>166.08</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>166.20</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>219.24</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>149.14</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>167.86</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>164.08</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>168.56</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>181.10</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>151.82</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>192.84</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>184.86</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>162.30</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>184.02</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>191.56</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>181.50</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>175.10</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>191.82</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>198.48</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>174.08</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>177.84</td><td>0.58</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>166.52</td><td>0.60</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>169.16</td><td>0.59</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>173.74</td><td>0.59</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>185.06</td><td>0.45</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>168.36</td><td>0.46</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>170.22</td><td>0.44</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>179.58</td><td>0.43</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>171.12</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>173.86</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>169.62</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>175.02</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>176.80</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>180.24</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>165.16</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>187.44</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>170.26</td><td>0.25</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>204.18</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>178.40</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>160.40</td><td>0.26</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>186.42</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>171.52</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>169.18</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>156.54</td><td>0.28</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>176.22</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>176.02</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>185.78</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>173.14</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>167.22</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>182.78</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>206.54</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>166.08</td><td>0.21</td><td>n/a</td></tr>
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
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>159.70</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>149.50</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>168.64</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>178.22</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>184.36</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>183.18</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>211.08</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>248.86</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>171.78</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>184.34</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>200.42</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>195.00</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>190.64</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>205.30</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>210.20</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>219.18</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>161.88</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>170.78</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>175.04</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>175.54</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>162.02</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>176.24</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>184.54</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>207.42</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>168.70</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>172.52</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>172.84</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>166.20</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>210.68</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>209.70</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>215.14</td><td>0.15</td><td>n/a</td></tr>
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
        <tr><td>test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>189.94</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>165.12</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>161.66</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>160.14</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>153.74</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>195.06</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>156.54</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>172.08</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>151.08</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>147.14</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>174.32</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>194.14</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>197.70</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>187.74</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>223.26</td><td>0.16</td><td>n/a</td></tr>
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
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>156.06</td><td>0.85</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>188.68</td><td>0.70</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>173.30</td><td>0.78</td><td>n/a</td></tr>
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
        <tr><td>test_swiglu_decode[embedding_dim_1024-hidden_dim_3584]</td><td>✅ 5/5</td><td>959.47</td><td>0.00</td><td>n/a</td></tr>
        <tr><td>test_swiglu_decode[embedding_dim_2048-hidden_dim_2048]</td><td>✅ 5/5</td><td>1016.00</td><td>0.01</td><td>n/a</td></tr>
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
        <tr><td>test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False]</td><td>✅ 5/5</td><td>2216.23</td><td>0.95</td><td>n/a</td></tr>
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
        <tr><td>test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>186.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>171.42</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>170.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>168.50</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>175.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>187.98</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>197.52</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>224.74</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>197.62</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>190.94</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>162.72</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>171.82</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>194.24</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>180.90</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>209.86</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>234.32</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>195.42</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>181.52</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>177.96</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>197.24</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>173.14</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>181.56</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>187.88</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>235.98</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>205.54</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>151.40</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>159.70</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>176.82</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>230.86</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>208.54</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>232.12</td><td>0.15</td><td>n/a</td></tr>
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
        <tr><td>test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>221.82</td><td>4.78</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>224.00</td><td>4.72</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>223.62</td><td>4.82</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>216.18</td><td>4.89</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>264.72</td><td>7.95</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>272.62</td><td>7.75</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>270.48</td><td>7.82</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>241.58</td><td>8.71</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>270.10</td><td>7.92</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>234.00</td><td>9.10</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>388.58</td><td>10.86</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>387.68</td><td>10.94</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>387.26</td><td>10.87</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>332.94</td><td>12.73</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>327.80</td><td>12.95</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>325.10</td><td>13.09</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>319.72</td><td>13.22</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>350.32</td><td>12.22</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>164.22</td><td>3.22</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2]</td><td>✅ 5/5</td><td>237.50</td><td>4.49</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4]</td><td>✅ 5/5</td><td>265.96</td><td>7.96</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>177.04</td><td>3.03</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>163.18</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>175.62</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>177.96</td><td>0.38</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>182.64</td><td>0.36</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>169.88</td><td>0.39</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>159.70</td><td>0.84</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>167.78</td><td>0.79</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>174.02</td><td>0.76</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>187.40</td><td>0.73</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>150.60</td><td>0.11</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

