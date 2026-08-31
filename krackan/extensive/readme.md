
# IRON

Tested on `2026_08_31_16_13_51` at commit `a279467`.

<details>
<summary>iron/operators/axpy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>139.80</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>152.96</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>169.46</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>147.74</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0]</td><td>✅ 5/5</td><td>189.72</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]</td><td>✅ 5/5</td><td>145.98</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0]</td><td>✅ 5/5</td><td>180.18</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0]</td><td>✅ 5/5</td><td>174.70</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>158.92</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>159.74</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>157.88</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>146.36</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>163.08</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>184.58</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0]</td><td>✅ 5/5</td><td>184.76</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0]</td><td>✅ 5/5</td><td>157.86</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0]</td><td>✅ 5/5</td><td>174.12</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>154.74</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>178.72</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>186.46</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>168.76</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>157.28</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>210.54</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>178.74</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0]</td><td>✅ 5/5</td><td>146.16</td><td>0.34</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0]</td><td>✅ 5/5</td><td>179.58</td><td>0.28</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0]</td><td>✅ 5/5</td><td>167.40</td><td>0.30</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>156.26</td><td>0.33</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>157.84</td><td>0.32</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>154.76</td><td>0.32</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>168.98</td><td>0.30</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>183.80</td><td>0.27</td><td>n/a</td></tr>
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
        <tr><td>test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>164.78</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>150.88</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>168.62</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>177.12</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>166.52</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>169.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>196.20</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32]</td><td>✅ 5/5</td><td>238.70</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>188.18</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>190.26</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>184.16</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>194.06</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>176.12</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>236.58</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>229.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>248.82</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>178.14</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>179.04</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>172.06</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>172.96</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>176.74</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>198.76</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>161.60</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>194.42</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32]</td><td>✅ 5/5</td><td>155.18</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>156.66</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>194.92</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>205.44</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>179.66</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>187.92</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>199.36</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>236.22</td><td>0.09</td><td>n/a</td></tr>
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
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024]</td><td>✅ 5/5</td><td>184.84</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512]</td><td>✅ 5/5</td><td>200.88</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 5/5</td><td>189.56</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128]</td><td>✅ 5/5</td><td>175.10</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>171.18</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>150.52</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>168.32</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256]</td><td>✅ 5/5</td><td>218.38</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 5/5</td><td>181.14</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048]</td><td>✅ 5/5</td><td>181.46</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024]</td><td>✅ 5/5</td><td>204.92</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512]</td><td>✅ 5/5</td><td>193.30</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192]</td><td>✅ 5/5</td><td>182.30</td><td>0.28</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096]</td><td>✅ 5/5</td><td>159.92</td><td>0.32</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048]</td><td>✅ 5/5</td><td>198.90</td><td>0.25</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024]</td><td>✅ 5/5</td><td>222.96</td><td>0.23</td><td>n/a</td></tr>
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
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024]</td><td>✅ 5/5</td><td>173.44</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512]</td><td>✅ 5/5</td><td>172.88</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 5/5</td><td>190.60</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128]</td><td>✅ 5/5</td><td>203.90</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>163.46</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>174.22</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>179.02</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256]</td><td>✅ 5/5</td><td>187.80</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 5/5</td><td>166.54</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048]</td><td>✅ 5/5</td><td>170.58</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024]</td><td>✅ 5/5</td><td>185.64</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512]</td><td>✅ 5/5</td><td>211.32</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096]</td><td>✅ 5/5</td><td>179.66</td><td>0.28</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048]</td><td>✅ 5/5</td><td>174.20</td><td>0.29</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024]</td><td>✅ 5/5</td><td>194.66</td><td>0.26</td><td>n/a</td></tr>
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
        <tr><td>test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>147.22</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>148.04</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>160.68</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>188.86</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>196.30</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>196.70</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>176.64</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>220.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>172.86</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>168.84</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>175.40</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>206.92</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>186.42</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>195.48</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>188.48</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>221.44</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>163.10</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>164.46</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>222.76</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>180.98</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>188.68</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>192.68</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>187.94</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>212.44</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 5/5</td><td>163.18</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>144.94</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>167.74</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>184.86</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>160.62</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>164.70</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>168.00</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>209.64</td><td>0.16</td><td>n/a</td></tr>
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
        <tr><td>test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>2323.88</td><td>4.07</td><td>1600.97</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>254.92</td><td>0.91</td><td>38.62</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>267.84</td><td>0.87</td><td>36.93</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>48479.12</td><td>0.52</td><td>354.38</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>119035.94</td><td>0.21</td><td>144.33</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>28226.70</td><td>0.89</td><td>608.67</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>7238.22</td><td>3.48</td><td>2375.25</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>8675.10</td><td>2.91</td><td>1986.12</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>7849.24</td><td>3.21</td><td>2189.79</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>96066.40</td><td>0.79</td><td>715.33</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>103347.40</td><td>0.73</td><td>664.94</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>108347.34</td><td>0.70</td><td>634.26</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1234.00</td><td>7.24</td><td>435.82</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1571.28</td><td>5.80</td><td>349.40</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1339.58</td><td>6.66</td><td>401.44</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>4307.40</td><td>8.10</td><td>498.91</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>4646.00</td><td>7.51</td><td>462.82</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>4969.70</td><td>7.02</td><td>432.63</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>95450.80</td><td>0.79</td><td>719.95</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>102591.10</td><td>0.74</td><td>669.84</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>107293.72</td><td>0.70</td><td>640.48</td></tr>
        <tr><td>test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>2483.22</td><td>3.27</td><td>856.85</td></tr>
        <tr><td>test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4]</td><td>✅ 5/5</td><td>3863.72</td><td>0.32</td><td>17.44</td></tr>
        <tr><td>test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>1685.30</td><td>4.04</td><td>1249.75</td></tr>
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
        <tr><td>test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 5/5</td><td>n/a</td><td>0.21</td><td>0.20</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>✅ 5/5</td><td>n/a</td><td>11.00</td><td>10.99</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>24.28</td><td>24.26</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512]</td><td>✅ 5/5</td><td>n/a</td><td>40.01</td><td>39.99</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256]</td><td>✅ 5/5</td><td>n/a</td><td>42.90</td><td>42.87</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>12.30</td><td>12.29</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>23.83</td><td>23.82</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>40.32</td><td>40.30</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>42.88</td><td>42.86</td></tr>
        <tr><td>test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2]</td><td>✅ 5/5</td><td>n/a</td><td>8.51</td><td>8.49</td></tr>
        <tr><td>test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2]</td><td>✅ 5/5</td><td>n/a</td><td>0.84</td><td>0.83</td></tr>
        <tr><td>test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]</td><td>✅ 5/5</td><td>n/a</td><td>1.21</td><td>1.20</td></tr>
        <tr><td>test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100]</td><td>✅ 5/5</td><td>n/a</td><td>16.66</td><td>16.47</td></tr>
        <tr><td>test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192]</td><td>✅ 5/5</td><td>n/a</td><td>13.53</td><td>13.29</td></tr>
        <tr><td>test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32]</td><td>✅ 5/5</td><td>n/a</td><td>8.53</td><td>8.39</td></tr>
        <tr><td>test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8]</td><td>✅ 5/5</td><td>n/a</td><td>5.33</td><td>5.25</td></tr>
        <tr><td>test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 5/5</td><td>n/a</td><td>0.17</td><td>0.17</td></tr>
        <tr><td>test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>✅ 5/5</td><td>n/a</td><td>11.93</td><td>11.92</td></tr>
        <tr><td>test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>11.99</td><td>11.98</td></tr>
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
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>193.00</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>195.84</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>188.70</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>179.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>190.56</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>229.26</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>173.80</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>223.22</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>202.92</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>178.46</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>139.42</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>210.76</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>190.84</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>187.50</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>223.52</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>267.08</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>183.46</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>193.42</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>186.30</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>165.58</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>194.94</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>216.24</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>223.78</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>239.16</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 5/5</td><td>192.70</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>175.94</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>193.88</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>220.02</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>220.16</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>241.08</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>205.16</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>246.54</td><td>0.14</td><td>n/a</td></tr>
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
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>150.74</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>166.18</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>156.18</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>177.82</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>182.52</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>189.74</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>200.80</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01]</td><td>✅ 5/5</td><td>186.78</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>169.98</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1]</td><td>✅ 5/5</td><td>169.04</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25]</td><td>✅ 5/5</td><td>199.84</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>174.60</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>169.68</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>199.04</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>172.02</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>173.38</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>207.26</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>208.20</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>183.16</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>157.00</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>183.42</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>184.72</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>177.26</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>189.38</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>192.76</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>227.14</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>189.22</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>168.66</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>158.38</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>149.62</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>208.00</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>190.42</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>217.78</td><td>0.16</td><td>n/a</td></tr>
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
        <tr><td>test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>168.14</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>163.64</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64]</td><td>✅ 5/5</td><td>196.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64]</td><td>✅ 5/5</td><td>203.80</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>159.58</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>162.18</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>185.12</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>172.84</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>208.20</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>176.76</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>157.50</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>175.78</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>197.44</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128]</td><td>✅ 5/5</td><td>167.08</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>191.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128]</td><td>✅ 5/5</td><td>177.74</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>188.12</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>154.38</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>234.52</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128]</td><td>✅ 5/5</td><td>219.70</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>191.60</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>189.26</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>180.92</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>216.46</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>160.68</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>162.00</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>210.10</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>163.36</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>207.16</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>186.72</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>204.72</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>185.42</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>143.92</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>168.34</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>214.36</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>184.40</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>168.58</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>187.84</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>172.84</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>176.26</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>187.32</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>188.38</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>178.66</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>191.30</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>173.14</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>167.62</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>179.20</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>172.62</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192]</td><td>✅ 5/5</td><td>215.92</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192]</td><td>✅ 5/5</td><td>175.74</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>225.74</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>192.26</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>160.04</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>169.96</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>159.94</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>166.42</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>186.18</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>200.14</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>180.40</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>193.06</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>215.70</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>180.56</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>169.24</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>170.96</td><td>0.20</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/mha</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0]</td><td>✅ 5/5</td><td>47376.88</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]</td><td>✅ 5/5</td><td>47396.56</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2]</td><td>✅ 5/5</td><td>374367.42</td><td>0.11</td><td>n/a</td></tr>
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
        <tr><td>test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>166.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>160.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>178.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>150.50</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>166.08</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>183.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>173.56</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>250.94</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>150.04</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>155.26</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>165.18</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>151.90</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>195.66</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>195.84</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>165.08</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>229.26</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>175.42</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>157.64</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>150.88</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>160.94</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>158.08</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>184.64</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>171.06</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>210.60</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>173.16</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>155.28</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>167.72</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>169.54</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>207.76</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>197.46</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>227.56</td><td>0.14</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/repeat</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]</td><td>✅ 5/5</td><td>172.40</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None]</td><td>✅ 5/5</td><td>192.38</td><td>0.27</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64]</td><td>✅ 5/5</td><td>917.64</td><td>11.84</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]</td><td>✅ 5/5</td><td>156.12</td><td>0.27</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]</td><td>✅ 5/5</td><td>161.68</td><td>0.03</td><td>n/a</td></tr>
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
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>148.34</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>186.00</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>144.94</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>177.64</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>145.66</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>169.54</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>164.52</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>189.70</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>174.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>165.12</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>174.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True]</td><td>✅ 5/5</td><td>209.24</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>177.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True]</td><td>✅ 5/5</td><td>220.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False]</td><td>✅ 5/5</td><td>198.88</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>158.28</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>165.12</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>204.20</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>177.46</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>187.34</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>181.70</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>169.90</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>190.14</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>152.88</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>197.98</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>183.22</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>260.32</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>173.50</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>224.42</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>207.66</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>158.78</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>179.72</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>149.84</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>166.38</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>154.38</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>173.64</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>205.34</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>206.66</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>165.46</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>186.68</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>165.62</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>194.12</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>165.02</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>200.28</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>230.46</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False]</td><td>✅ 5/5</td><td>199.04</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>184.92</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>203.58</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>178.04</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>169.54</td><td>0.25</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>166.18</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>158.30</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>206.78</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>179.38</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>176.86</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>167.30</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>190.36</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>196.70</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>255.86</td><td>0.13</td><td>n/a</td></tr>
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
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>193.92</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>198.62</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>175.00</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>167.04</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>161.94</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>166.26</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>193.04</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>187.40</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>184.78</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>172.86</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>169.14</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>166.90</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>196.52</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>152.86</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>230.10</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>211.46</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>176.04</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>178.52</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>188.98</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>177.18</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>189.70</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>172.42</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>191.34</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>185.30</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>173.50</td><td>0.59</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>187.24</td><td>0.53</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>159.68</td><td>0.64</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>205.86</td><td>0.49</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>195.74</td><td>0.38</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>203.06</td><td>0.37</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>185.60</td><td>0.43</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>192.84</td><td>0.39</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>190.42</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>183.82</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>163.14</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>170.96</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>187.64</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>158.70</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>190.92</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>199.70</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>157.38</td><td>0.27</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>170.00</td><td>0.25</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>170.42</td><td>0.25</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>159.60</td><td>0.26</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>193.88</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>159.52</td><td>0.27</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>192.24</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>173.80</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>184.22</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>165.64</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>174.28</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>171.80</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>182.04</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>170.04</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>193.40</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1]</td><td>✅ 5/5</td><td>202.64</td><td>0.19</td><td>n/a</td></tr>
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
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>154.34</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>171.86</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>157.76</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>160.66</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>176.14</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>166.52</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>212.24</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>296.34</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>169.72</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>173.90</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>162.28</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>179.32</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>170.88</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>171.26</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>186.56</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>228.36</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>165.32</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>157.18</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>154.78</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>154.78</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>160.56</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>186.96</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>169.28</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>225.90</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>189.28</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>179.54</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>171.34</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>216.80</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>190.32</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>207.10</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>236.76</td><td>0.15</td><td>n/a</td></tr>
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
        <tr><td>test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>155.86</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>207.44</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>192.20</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>210.18</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>169.56</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>205.08</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>171.70</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>200.96</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>194.88</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>160.80</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>180.60</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>172.70</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>173.60</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>167.60</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>178.34</td><td>0.19</td><td>n/a</td></tr>
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
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>188.32</td><td>0.71</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>185.32</td><td>0.72</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>197.16</td><td>0.68</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/strided_copy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_strided_copy[chunked_transfer]</td><td>✅ 5/5</td><td>179.22</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[contiguous]</td><td>✅ 5/5</td><td>175.64</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[four_channels]</td><td>✅ 5/5</td><td>176.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_llama_full]</td><td>✅ 5/5</td><td>154.44</td><td>13.80</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot0]</td><td>✅ 5/5</td><td>162.00</td><td>0.85</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5]</td><td>✅ 5/5</td><td>201.48</td><td>0.72</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_four_channels]</td><td>✅ 5/5</td><td>178.70</td><td>0.78</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_two_channels]</td><td>✅ 5/5</td><td>181.28</td><td>0.74</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot_last]</td><td>✅ 5/5</td><td>155.80</td><td>0.86</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels]</td><td>✅ 5/5</td><td>190.72</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels_chunked]</td><td>✅ 5/5</td><td>189.94</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
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
        <tr><td>test_swiglu_decode[embedding_dim_1024-hidden_dim_3584]</td><td>✅ 5/5</td><td>984.59</td><td>0.00</td><td>n/a</td></tr>
        <tr><td>test_swiglu_decode[embedding_dim_2048-hidden_dim_2048]</td><td>✅ 5/5</td><td>1049.10</td><td>0.01</td><td>n/a</td></tr>
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
        <tr><td>test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False]</td><td>✅ 5/5</td><td>2201.27</td><td>0.95</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/swiglu_prefill_stream</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_swiglu_prefill_stream[k_1]</td><td>✅ 5/5</td><td>1328.44</td><td>0.39</td><td>n/a</td></tr>
        <tr><td>test_swiglu_prefill_stream[k_2]</td><td>✅ 5/5</td><td>2021.31</td><td>0.26</td><td>n/a</td></tr>
        <tr><td>test_swiglu_prefill_stream[k_5]</td><td>✅ 5/5</td><td>1427.77</td><td>0.37</td><td>n/a</td></tr>
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
        <tr><td>test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>149.50</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>158.90</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>158.70</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>170.08</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>180.98</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>189.32</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]</td><td>✅ 5/5</td><td>192.62</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]</td><td>✅ 5/5</td><td>244.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>225.58</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>170.28</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>174.12</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>201.40</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>188.40</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>212.06</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>223.48</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>227.88</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>176.50</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>178.22</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>196.26</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>203.68</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>182.26</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>209.72</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>171.54</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>220.52</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>174.28</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>174.94</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>164.66</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>179.06</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>180.78</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>191.18</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>218.20</td><td>0.15</td><td>n/a</td></tr>
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
        <tr><td>test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>233.50</td><td>4.75</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>197.48</td><td>5.36</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>229.86</td><td>4.65</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>215.44</td><td>4.93</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>250.08</td><td>8.42</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>263.74</td><td>8.05</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>270.96</td><td>7.85</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>257.94</td><td>8.25</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>271.18</td><td>8.07</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>261.02</td><td>8.09</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>375.98</td><td>11.30</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>343.92</td><td>12.26</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>359.08</td><td>11.85</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>302.38</td><td>14.06</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>323.26</td><td>13.23</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>320.78</td><td>13.32</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>296.88</td><td>14.27</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>359.12</td><td>12.05</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>202.84</td><td>2.62</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2]</td><td>✅ 5/5</td><td>197.24</td><td>5.36</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4]</td><td>✅ 5/5</td><td>277.12</td><td>7.61</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>183.28</td><td>2.90</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>148.62</td><td>0.23</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>163.80</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>138.08</td><td>0.48</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>150.26</td><td>0.45</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>153.18</td><td>0.44</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>157.78</td><td>0.87</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>181.44</td><td>0.73</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>163.78</td><td>0.81</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>177.04</td><td>0.75</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>156.60</td><td>0.11</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

