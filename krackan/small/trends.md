# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


### test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.10 (+4.52%)</td><td>0.08 (+10.50%)</td><td>0.08 (-2.21%)</td><td>0.07 <b>(+34.63%)</b></td><td>0.01 <b>(-33.68%)</b></td><td>180.50 <b>(-25.72%)</b></td><td>153.90 (-13.87%)</td><td>162.30 (+2.27%)</td><td>123.50 (-4.26%)</td><td>25.39 <b>(-53.51%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>243.00 (n/a)</td><td>178.68 (n/a)</td><td>158.70 (n/a)</td><td>129.00 (n/a)</td><td>54.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.10 (+17.67%)</td><td>0.08 (+9.39%)</td><td>0.08 (+4.28%)</td><td>0.06 (-3.26%)</td><td>0.02 <b>(+78.80%)</b></td><td>204.40 (+3.39%)</td><td>159.00 (-5.29%)</td><td>150.20 (-4.09%)</td><td>117.10 (-15.02%)</td><td>42.04 <b>(+54.52%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.70 (n/a)</td><td>167.88 (n/a)</td><td>156.60 (n/a)</td><td>137.80 (n/a)</td><td>27.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.10 <b>(+39.42%)</b></td><td>0.08 <b>(+22.54%)</b></td><td>0.08 (+18.59%)</td><td>0.06 (-2.07%)</td><td>0.02 <b>(+364.50%)</b></td><td>208.10 (+2.11%)</td><td>161.28 (-15.67%)</td><td>160.00 (-15.66%)</td><td>127.00 <b>(-28.25%)</b></td><td>34.12 <b>(+231.74%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>203.80 (n/a)</td><td>191.24 (n/a)</td><td>189.70 (n/a)</td><td>177.00 (n/a)</td><td>10.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.10 <b>(+29.59%)</b></td><td>0.07 (+19.49%)</td><td>0.07 <b>(+25.03%)</b></td><td>0.04 <b>(-26.97%)</b></td><td>0.03 <b>(+166.76%)</b></td><td>307.90 <b>(+36.97%)</b></td><td>187.38 (-7.29%)</td><td>168.30 <b>(-20.05%)</b></td><td>119.70 <b>(-22.87%)</b></td><td>77.06 <b>(+185.29%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.80 (n/a)</td><td>202.12 (n/a)</td><td>210.50 (n/a)</td><td>155.20 (n/a)</td><td>27.01 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


### test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (-13.33%)</td><td>0.03 (-5.78%)</td><td>0.04 (+1.63%)</td><td>0.03 (-17.71%)</td><td>0.00 (-13.13%)</td><td>200.40 <b>(+21.53%)</b></td><td>156.90 (+6.30%)</td><td>149.60 (-1.64%)</td><td>132.90 (+15.36%)</td><td>25.50 <b>(+27.70%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>164.90 (n/a)</td><td>147.60 (n/a)</td><td>152.10 (n/a)</td><td>115.20 (n/a)</td><td>19.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (-5.97%)</td><td>0.04 (+7.91%)</td><td>0.04 (+14.68%)</td><td>0.03 (+17.97%)</td><td>0.00 <b>(-42.89%)</b></td><td>160.80 (-15.23%)</td><td>140.40 (-9.51%)</td><td>144.30 (-12.81%)</td><td>123.00 (+6.31%)</td><td>15.69 <b>(-48.81%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>155.16 (n/a)</td><td>165.50 (n/a)</td><td>115.70 (n/a)</td><td>30.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (+13.48%)</td><td>0.04 (-4.66%)</td><td>0.03 (-10.68%)</td><td>0.03 (-8.55%)</td><td>0.01 <b>(+128.89%)</b></td><td>159.20 (+9.42%)</td><td>143.50 (+6.61%)</td><td>150.80 (+11.95%)</td><td>107.30 (-11.83%)</td><td>20.70 <b>(+113.66%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>145.50 (n/a)</td><td>134.60 (n/a)</td><td>134.70 (n/a)</td><td>121.70 (n/a)</td><td>9.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 <b>(+44.27%)</b></td><td>0.04 (+9.66%)</td><td>0.03 (-1.44%)</td><td>0.03 (-5.27%)</td><td>0.01 <b>(+131.94%)</b></td><td>204.10 (+5.53%)</td><td>154.88 (-3.15%)</td><td>151.90 (+1.47%)</td><td>87.30 <b>(-30.71%)</b></td><td>43.94 <b>(+58.97%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>159.92 (n/a)</td><td>149.70 (n/a)</td><td>126.00 (n/a)</td><td>27.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (-14.03%)</td><td>0.03 (-10.87%)</td><td>0.03 (-1.26%)</td><td>0.02 <b>(-22.11%)</b></td><td>0.01 (-7.39%)</td><td>235.70 <b>(+28.38%)</b></td><td>170.08 (+13.55%)</td><td>156.20 (+1.30%)</td><td>120.90 (+16.36%)</td><td>42.79 <b>(+45.80%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>149.78 (n/a)</td><td>154.20 (n/a)</td><td>103.90 (n/a)</td><td>29.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (+1.28%)</td><td>0.03 (+8.54%)</td><td>0.03 (+17.10%)</td><td>0.03 (+1.99%)</td><td>0.00 (+18.56%)</td><td>192.20 (-1.94%)</td><td>165.22 (-7.48%)</td><td>156.40 (-14.63%)</td><td>144.30 (-1.23%)</td><td>22.49 (+18.44%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>196.00 (n/a)</td><td>178.58 (n/a)</td><td>183.20 (n/a)</td><td>146.10 (n/a)</td><td>18.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (-8.79%)</td><td>0.03 (+1.42%)</td><td>0.03 <b>(+21.68%)</b></td><td>0.03 (+0.62%)</td><td>0.01 <b>(-32.08%)</b></td><td>200.00 (-0.65%)</td><td>168.16 (-3.51%)</td><td>162.00 (-17.81%)</td><td>131.00 (+9.72%)</td><td>26.44 <b>(-28.35%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>174.28 (n/a)</td><td>197.10 (n/a)</td><td>119.40 (n/a)</td><td>36.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 (+4.82%)</td><td>0.03 (+13.55%)</td><td>0.03 <b>(+25.42%)</b></td><td>0.03 (+15.23%)</td><td>0.00 <b>(-36.77%)</b></td><td>207.50 (-13.22%)</td><td>183.80 (-12.92%)</td><td>182.30 <b>(-20.29%)</b></td><td>169.90 (-4.60%)</td><td>15.64 <b>(-47.18%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.10 (n/a)</td><td>211.06 (n/a)</td><td>228.70 (n/a)</td><td>178.10 (n/a)</td><td>29.60 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


### test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>197.50 (n/a)</td><td>146.82 (n/a)</td><td>136.70 (n/a)</td><td>119.50 (n/a)</td><td>32.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>242.10 (n/a)</td><td>177.66 (n/a)</td><td>156.10 (n/a)</td><td>147.80 (n/a)</td><td>40.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>210.60 (n/a)</td><td>169.68 (n/a)</td><td>176.10 (n/a)</td><td>120.00 (n/a)</td><td>34.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>203.50 (n/a)</td><td>187.72 (n/a)</td><td>184.30 (n/a)</td><td>175.80 (n/a)</td><td>11.32 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


### test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>188.30 (n/a)</td><td>167.66 (n/a)</td><td>165.60 (n/a)</td><td>152.70 (n/a)</td><td>14.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>235.50 (n/a)</td><td>159.18 (n/a)</td><td>150.30 (n/a)</td><td>121.40 (n/a)</td><td>46.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>252.10 (n/a)</td><td>203.64 (n/a)</td><td>198.20 (n/a)</td><td>174.30 (n/a)</td><td>29.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>330.20 (n/a)</td><td>255.28 (n/a)</td><td>234.90 (n/a)</td><td>174.10 (n/a)</td><td>62.35 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gelu</summary>


### test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.20 (n/a)</td><td>160.86 (n/a)</td><td>164.20 (n/a)</td><td>139.70 (n/a)</td><td>16.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>158.52 (n/a)</td><td>148.80 (n/a)</td><td>128.20 (n/a)</td><td>29.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>194.30 (n/a)</td><td>182.08 (n/a)</td><td>188.30 (n/a)</td><td>166.30 (n/a)</td><td>12.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>179.46 (n/a)</td><td>189.90 (n/a)</td><td>116.00 (n/a)</td><td>38.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.50 (n/a)</td><td>174.92 (n/a)</td><td>181.10 (n/a)</td><td>144.40 (n/a)</td><td>18.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.40 (n/a)</td><td>194.54 (n/a)</td><td>210.30 (n/a)</td><td>156.50 (n/a)</td><td>30.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.10 (n/a)</td><td>187.86 (n/a)</td><td>175.60 (n/a)</td><td>149.80 (n/a)</td><td>42.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>234.90 (n/a)</td><td>223.44 (n/a)</td><td>230.00 (n/a)</td><td>195.80 (n/a)</td><td>16.02 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemm</summary>


### test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>4.28 (-1.09%)</td><td>3.74 (-5.69%)</td><td>3.57 (-14.35%)</td><td>3.31 (-5.70%)</td><td>0.42 (+17.82%)</td><td>2842.20 (+6.04%)</td><td>2537.34 (+6.37%)</td><td>2634.70 (+16.75%)</td><td>2196.90 (+1.11%)</td><td>278.38 <b>(+24.87%)</b></td><td>1683.93 (-1.09%)</td><td>1472.54 (-5.69%)</td><td>1404.08 (-14.35%)</td><td>1301.60 (-5.70%)</td><td>166.24 (+17.82%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>4.33 (n/a)</td><td>3.97 (n/a)</td><td>4.17 (n/a)</td><td>3.51 (n/a)</td><td>0.36 (n/a)</td><td>2680.20 (n/a)</td><td>2385.42 (n/a)</td><td>2256.70 (n/a)</td><td>2172.80 (n/a)</td><td>222.94 (n/a)</td><td>1702.55 (n/a)</td><td>1561.37 (n/a)</td><td>1639.27 (n/a)</td><td>1380.29 (n/a)</td><td>141.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.95 (-17.33%)</td><td>0.83 (-10.78%)</td><td>0.93 (-11.90%)</td><td>0.65 (-2.89%)</td><td>0.14 <b>(-40.10%)</b></td><td>342.50 (+2.98%)</td><td>271.54 (+8.67%)</td><td>238.60 (+13.51%)</td><td>233.30 <b>(+20.94%)</b></td><td>49.48 <b>(-27.15%)</b></td><td>40.45 (-17.33%)</td><td>35.62 (-10.78%)</td><td>39.55 (-11.90%)</td><td>27.55 (-2.89%)</td><td>5.94 <b>(-40.10%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.15 (n/a)</td><td>0.94 (n/a)</td><td>1.05 (n/a)</td><td>0.67 (n/a)</td><td>0.23 (n/a)</td><td>332.60 (n/a)</td><td>249.88 (n/a)</td><td>210.20 (n/a)</td><td>192.90 (n/a)</td><td>67.92 (n/a)</td><td>48.93 (n/a)</td><td>39.92 (n/a)</td><td>44.89 (n/a)</td><td>28.37 (n/a)</td><td>9.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.44 (+6.79%)</td><td>0.97 (-0.83%)</td><td>0.94 (-10.44%)</td><td>0.67 (-3.88%)</td><td>0.31 (+9.40%)</td><td>331.90 (+4.01%)</td><td>245.98 (+1.44%)</td><td>235.60 (+11.66%)</td><td>153.60 (-6.40%)</td><td>72.27 (+0.80%)</td><td>61.42 (+6.80%)</td><td>41.38 (-0.83%)</td><td>40.06 (-10.44%)</td><td>28.43 (-3.88%)</td><td>13.19 (+9.40%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.35 (n/a)</td><td>0.98 (n/a)</td><td>1.05 (n/a)</td><td>0.69 (n/a)</td><td>0.28 (n/a)</td><td>319.10 (n/a)</td><td>242.50 (n/a)</td><td>211.00 (n/a)</td><td>164.10 (n/a)</td><td>71.69 (n/a)</td><td>57.52 (n/a)</td><td>41.73 (n/a)</td><td>44.73 (n/a)</td><td>29.58 (n/a)</td><td>12.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.52 (+0.39%)</td><td>0.52 (+0.08%)</td><td>0.52 (+0.09%)</td><td>0.52 (-0.11%)</td><td>0.00 <b>(+102.83%)</b></td><td>48682.60 (+0.11%)</td><td>48463.86 (-0.08%)</td><td>48442.10 (-0.09%)</td><td>48251.30 (-0.39%)</td><td>154.42 <b>(+102.29%)</b></td><td>356.05 (+0.39%)</td><td>354.49 (+0.08%)</td><td>354.65 (+0.09%)</td><td>352.90 (-0.11%)</td><td>1.13 <b>(+102.83%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48627.60 (n/a)</td><td>48503.70 (n/a)</td><td>48483.60 (n/a)</td><td>48440.80 (n/a)</td><td>76.34 (n/a)</td><td>354.66 (n/a)</td><td>354.20 (n/a)</td><td>354.34 (n/a)</td><td>353.29 (n/a)</td><td>0.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.91 (+2.12%)</td><td>0.89 (+0.44%)</td><td>0.89 (-0.38%)</td><td>0.88 (-0.01%)</td><td>0.01 <b>(+195.53%)</b></td><td>28470.20 (+0.01%)</td><td>28136.12 (-0.43%)</td><td>28369.00 (+0.38%)</td><td>27511.30 (-2.07%)</td><td>408.70 <b>(+189.46%)</b></td><td>624.47 (+2.12%)</td><td>610.70 (+0.44%)</td><td>605.59 (-0.38%)</td><td>603.43 (-0.01%)</td><td>8.96 <b>(+195.53%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.00 (n/a)</td><td>28467.90 (n/a)</td><td>28256.22 (n/a)</td><td>28262.40 (n/a)</td><td>28094.00 (n/a)</td><td>141.19 (n/a)</td><td>611.51 (n/a)</td><td>608.02 (n/a)</td><td>607.87 (n/a)</td><td>603.48 (n/a)</td><td>3.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>3.26 (-2.16%)</td><td>3.16 (-2.77%)</td><td>3.17 (-2.23%)</td><td>3.08 (-3.33%)</td><td>0.08 <b>(+27.55%)</b></td><td>8182.90 (+3.44%)</td><td>7972.88 (+2.87%)</td><td>7932.40 (+2.28%)</td><td>7716.40 (+2.21%)</td><td>198.29 <b>(+35.31%)</b></td><td>2226.40 (-2.16%)</td><td>2155.85 (-2.77%)</td><td>2165.78 (-2.23%)</td><td>2099.47 (-3.33%)</td><td>53.72 <b>(+27.55%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>3.33 (n/a)</td><td>3.25 (n/a)</td><td>3.24 (n/a)</td><td>3.18 (n/a)</td><td>0.06 (n/a)</td><td>7910.60 (n/a)</td><td>7750.22 (n/a)</td><td>7755.80 (n/a)</td><td>7549.80 (n/a)</td><td>146.54 (n/a)</td><td>2275.55 (n/a)</td><td>2217.34 (n/a)</td><td>2215.10 (n/a)</td><td>2171.76 (n/a)</td><td>42.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>4.18 (-1.25%)</td><td>3.85 (+5.66%)</td><td>3.82 (+5.21%)</td><td>3.59 (+18.57%)</td><td>0.23 <b>(-46.24%)</b></td><td>2247.90 (-15.66%)</td><td>2101.46 (-6.17%)</td><td>2111.30 (-4.95%)</td><td>1928.80 (+1.26%)</td><td>123.91 <b>(-54.65%)</b></td><td>1095.97 (-1.25%)</td><td>1008.77 (+5.66%)</td><td>1001.22 (+5.21%)</td><td>940.39 (+18.57%)</td><td>60.51 <b>(-46.24%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>4.23 (n/a)</td><td>3.64 (n/a)</td><td>3.63 (n/a)</td><td>3.02 (n/a)</td><td>0.43 (n/a)</td><td>2665.30 (n/a)</td><td>2239.66 (n/a)</td><td>2221.30 (n/a)</td><td>1904.80 (n/a)</td><td>273.25 (n/a)</td><td>1109.81 (n/a)</td><td>954.77 (n/a)</td><td>951.66 (n/a)</td><td>793.12 (n/a)</td><td>112.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.34 (-5.61%)</td><td>0.32 (-1.96%)</td><td>0.32 (+0.92%)</td><td>0.29 (+0.02%)</td><td>0.02 (-15.33%)</td><td>4353.40 (-0.02%)</td><td>3952.24 (+1.83%)</td><td>3852.90 (-0.91%)</td><td>3662.90 (+5.94%)</td><td>316.08 (-10.55%)</td><td>18.32 (-5.61%)</td><td>17.07 (-1.96%)</td><td>17.42 (+0.92%)</td><td>15.42 (+0.02%)</td><td>1.34 (-15.33%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.03 (n/a)</td><td>4354.30 (n/a)</td><td>3881.08 (n/a)</td><td>3888.10 (n/a)</td><td>3457.50 (n/a)</td><td>353.37 (n/a)</td><td>19.41 (n/a)</td><td>17.41 (n/a)</td><td>17.26 (n/a)</td><td>15.41 (n/a)</td><td>1.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>4.96 (-0.05%)</td><td>4.14 (+2.00%)</td><td>3.74 (+0.16%)</td><td>3.37 (-1.62%)</td><td>0.75 (+5.51%)</td><td>1974.60 (+1.65%)</td><td>1649.88 (-1.76%)</td><td>1777.00 (-0.16%)</td><td>1340.20 (+0.05%)</td><td>289.15 (+2.99%)</td><td>1533.51 (-0.05%)</td><td>1278.28 (+2.00%)</td><td>1156.54 (+0.16%)</td><td>1040.82 (-1.62%)</td><td>233.24 (+5.51%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>4.97 (n/a)</td><td>4.06 (n/a)</td><td>3.74 (n/a)</td><td>3.42 (n/a)</td><td>0.72 (n/a)</td><td>1942.60 (n/a)</td><td>1679.38 (n/a)</td><td>1779.80 (n/a)</td><td>1339.50 (n/a)</td><td>280.77 (n/a)</td><td>1534.27 (n/a)</td><td>1253.27 (n/a)</td><td>1154.72 (n/a)</td><td>1057.98 (n/a)</td><td>221.05 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemv</summary>


### test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>13.51 (n/a)</td><td>11.66 (n/a)</td><td>11.66 (n/a)</td><td>10.31 (n/a)</td><td>1.18 (n/a)</td><td>13.50 (n/a)</td><td>11.65 (n/a)</td><td>11.66 (n/a)</td><td>10.31 (n/a)</td><td>1.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>25.00 (+1.76%)</td><td>23.96 (-0.88%)</td><td>24.22 (-0.28%)</td><td>22.32 (-5.03%)</td><td>0.99 <b>(+147.06%)</b></td><td>24.98 (+1.76%)</td><td>23.95 (-0.88%)</td><td>24.21 (-0.28%)</td><td>22.31 (-5.03%)</td><td>0.99 <b>(+147.06%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>24.57 (n/a)</td><td>24.18 (n/a)</td><td>24.29 (n/a)</td><td>23.50 (n/a)</td><td>0.40 (n/a)</td><td>24.55 (n/a)</td><td>24.16 (n/a)</td><td>24.27 (n/a)</td><td>23.49 (n/a)</td><td>0.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>42.61 (+5.39%)</td><td>39.88 (+1.61%)</td><td>39.11 (-0.90%)</td><td>38.18 (+1.65%)</td><td>1.75 <b>(+64.24%)</b></td><td>42.58 (+5.39%)</td><td>39.86 (+1.61%)</td><td>39.08 (-0.90%)</td><td>38.15 (+1.65%)</td><td>1.75 <b>(+64.24%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>40.43 (n/a)</td><td>39.25 (n/a)</td><td>39.46 (n/a)</td><td>37.55 (n/a)</td><td>1.07 (n/a)</td><td>40.40 (n/a)</td><td>39.23 (n/a)</td><td>39.44 (n/a)</td><td>37.53 (n/a)</td><td>1.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>44.06 (+1.18%)</td><td>37.93 (-9.56%)</td><td>39.01 (-9.27%)</td><td>25.18 <b>(-36.10%)</b></td><td>7.63 <b>(+320.22%)</b></td><td>44.04 (+1.18%)</td><td>37.91 (-9.56%)</td><td>38.99 (-9.27%)</td><td>25.16 <b>(-36.10%)</b></td><td>7.63 <b>(+320.22%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>43.55 (n/a)</td><td>41.94 (n/a)</td><td>43.00 (n/a)</td><td>39.40 (n/a)</td><td>1.82 (n/a)</td><td>43.52 (n/a)</td><td>41.91 (n/a)</td><td>42.97 (n/a)</td><td>39.38 (n/a)</td><td>1.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>13.16 (n/a)</td><td>12.26 (n/a)</td><td>12.23 (n/a)</td><td>10.69 (n/a)</td><td>1.01 (n/a)</td><td>13.15 (n/a)</td><td>12.25 (n/a)</td><td>12.22 (n/a)</td><td>10.69 (n/a)</td><td>1.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>25.21 (+2.01%)</td><td>24.45 (+1.08%)</td><td>24.12 (-0.00%)</td><td>23.83 (+0.60%)</td><td>0.65 <b>(+62.91%)</b></td><td>25.19 (+2.01%)</td><td>24.43 (+1.08%)</td><td>24.10 (-0.00%)</td><td>23.82 (+0.60%)</td><td>0.65 <b>(+62.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>24.71 (n/a)</td><td>24.19 (n/a)</td><td>24.12 (n/a)</td><td>23.69 (n/a)</td><td>0.40 (n/a)</td><td>24.70 (n/a)</td><td>24.17 (n/a)</td><td>24.11 (n/a)</td><td>23.68 (n/a)</td><td>0.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>41.27 (-2.90%)</td><td>37.41 (-6.34%)</td><td>39.18 (-0.75%)</td><td>32.77 (-13.36%)</td><td>3.71 <b>(+105.93%)</b></td><td>41.25 (-2.90%)</td><td>37.39 (-6.34%)</td><td>39.15 (-0.75%)</td><td>32.75 (-13.36%)</td><td>3.71 <b>(+105.93%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>42.51 (n/a)</td><td>39.95 (n/a)</td><td>39.47 (n/a)</td><td>37.82 (n/a)</td><td>1.80 (n/a)</td><td>42.48 (n/a)</td><td>39.92 (n/a)</td><td>39.45 (n/a)</td><td>37.80 (n/a)</td><td>1.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>42.59 (-6.22%)</td><td>39.89 (+1.34%)</td><td>39.96 (-0.99%)</td><td>36.65 <b>(+22.36%)</b></td><td>2.27 <b>(-61.74%)</b></td><td>42.56 (-6.22%)</td><td>39.87 (+1.34%)</td><td>39.94 (-0.99%)</td><td>36.62 <b>(+22.36%)</b></td><td>2.27 <b>(-61.74%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>45.42 (n/a)</td><td>39.36 (n/a)</td><td>40.36 (n/a)</td><td>29.95 (n/a)</td><td>5.94 (n/a)</td><td>45.39 (n/a)</td><td>39.34 (n/a)</td><td>40.34 (n/a)</td><td>29.93 (n/a)</td><td>5.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>9.49 (+1.80%)</td><td>9.06 (+1.31%)</td><td>9.05 (+0.57%)</td><td>8.50 (+1.22%)</td><td>0.41 <b>(+20.78%)</b></td><td>9.47 (+1.80%)</td><td>9.04 (+1.31%)</td><td>9.03 (+0.57%)</td><td>8.48 (+1.22%)</td><td>0.41 <b>(+20.78%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>9.32 (n/a)</td><td>8.94 (n/a)</td><td>9.00 (n/a)</td><td>8.40 (n/a)</td><td>0.34 (n/a)</td><td>9.30 (n/a)</td><td>8.92 (n/a)</td><td>8.98 (n/a)</td><td>8.38 (n/a)</td><td>0.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.97 (-4.51%)</td><td>0.93 (+0.15%)</td><td>0.92 (-2.70%)</td><td>0.90 (+11.78%)</td><td>0.03 <b>(-61.52%)</b></td><td>0.95 (-4.52%)</td><td>0.91 (+0.15%)</td><td>0.90 (-2.70%)</td><td>0.88 (+11.78%)</td><td>0.03 <b>(-61.52%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.01 (n/a)</td><td>0.93 (n/a)</td><td>0.94 (n/a)</td><td>0.80 (n/a)</td><td>0.09 (n/a)</td><td>1.00 (n/a)</td><td>0.91 (n/a)</td><td>0.93 (n/a)</td><td>0.79 (n/a)</td><td>0.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.34 (-5.68%)</td><td>1.22 (+1.54%)</td><td>1.24 (+12.87%)</td><td>1.02 (-3.01%)</td><td>0.14 <b>(-20.46%)</b></td><td>1.33 (-5.68%)</td><td>1.20 (+1.54%)</td><td>1.23 (+12.87%)</td><td>1.01 (-3.01%)</td><td>0.13 <b>(-20.46%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.42 (n/a)</td><td>1.20 (n/a)</td><td>1.10 (n/a)</td><td>1.06 (n/a)</td><td>0.17 (n/a)</td><td>1.41 (n/a)</td><td>1.18 (n/a)</td><td>1.09 (n/a)</td><td>1.04 (n/a)</td><td>0.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>18.64 (+5.57%)</td><td>17.85 (+15.33%)</td><td>17.79 (+9.04%)</td><td>17.00 <b>(+29.69%)</b></td><td>0.61 <b>(-71.69%)</b></td><td>18.43 (+5.57%)</td><td>17.64 (+15.33%)</td><td>17.58 (+9.04%)</td><td>16.80 <b>(+29.69%)</b></td><td>0.60 <b>(-71.69%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>17.66 (n/a)</td><td>15.47 (n/a)</td><td>16.31 (n/a)</td><td>13.11 (n/a)</td><td>2.15 (n/a)</td><td>17.45 (n/a)</td><td>15.30 (n/a)</td><td>16.12 (n/a)</td><td>12.95 (n/a)</td><td>2.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>14.00 (-2.60%)</td><td>13.67 (-0.70%)</td><td>13.69 (+0.48%)</td><td>13.26 (-1.49%)</td><td>0.32 (-9.91%)</td><td>13.75 (-2.60%)</td><td>13.43 (-0.70%)</td><td>13.45 (+0.48%)</td><td>13.03 (-1.49%)</td><td>0.32 (-9.90%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>14.37 (n/a)</td><td>13.77 (n/a)</td><td>13.63 (n/a)</td><td>13.46 (n/a)</td><td>0.36 (n/a)</td><td>14.12 (n/a)</td><td>13.53 (n/a)</td><td>13.39 (n/a)</td><td>13.23 (n/a)</td><td>0.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>9.81 <b>(+22.90%)</b></td><td>8.27 (+17.03%)</td><td>7.88 (+5.82%)</td><td>7.59 <b>(+46.39%)</b></td><td>0.89 (-19.84%)</td><td>9.64 <b>(+22.90%)</b></td><td>8.12 (+17.03%)</td><td>7.75 (+5.82%)</td><td>7.46 <b>(+46.39%)</b></td><td>0.88 (-19.84%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>7.98 (n/a)</td><td>7.06 (n/a)</td><td>7.45 (n/a)</td><td>5.19 (n/a)</td><td>1.11 (n/a)</td><td>7.84 (n/a)</td><td>6.94 (n/a)</td><td>7.32 (n/a)</td><td>5.10 (n/a)</td><td>1.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>6.17 (+0.99%)</td><td>5.73 (-0.14%)</td><td>5.69 (+0.27%)</td><td>5.17 (-6.76%)</td><td>0.44 <b>(+93.59%)</b></td><td>6.08 (+0.99%)</td><td>5.64 (-0.14%)</td><td>5.59 (+0.27%)</td><td>5.08 (-6.76%)</td><td>0.43 <b>(+93.59%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>6.11 (n/a)</td><td>5.74 (n/a)</td><td>5.67 (n/a)</td><td>5.54 (n/a)</td><td>0.23 (n/a)</td><td>6.02 (n/a)</td><td>5.65 (n/a)</td><td>5.58 (n/a)</td><td>5.45 (n/a)</td><td>0.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>13.50 (n/a)</td><td>12.32 (n/a)</td><td>12.58 (n/a)</td><td>9.99 (n/a)</td><td>1.40 (n/a)</td><td>13.49 (n/a)</td><td>12.31 (n/a)</td><td>12.57 (n/a)</td><td>9.98 (n/a)</td><td>1.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>13.49 (n/a)</td><td>12.60 (n/a)</td><td>13.22 (n/a)</td><td>10.12 (n/a)</td><td>1.40 (n/a)</td><td>13.48 (n/a)</td><td>12.59 (n/a)</td><td>13.21 (n/a)</td><td>10.12 (n/a)</td><td>1.40 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/layer_norm</summary>


### test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.60 (n/a)</td><td>192.46 (n/a)</td><td>189.40 (n/a)</td><td>153.30 (n/a)</td><td>34.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>283.90 (n/a)</td><td>174.50 (n/a)</td><td>156.40 (n/a)</td><td>113.90 (n/a)</td><td>64.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>234.90 (n/a)</td><td>173.62 (n/a)</td><td>184.70 (n/a)</td><td>110.30 (n/a)</td><td>58.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>165.10 (n/a)</td><td>165.00 (n/a)</td><td>127.80 (n/a)</td><td>32.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>242.50 (n/a)</td><td>177.06 (n/a)</td><td>192.50 (n/a)</td><td>109.20 (n/a)</td><td>52.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>290.30 (n/a)</td><td>198.28 (n/a)</td><td>215.80 (n/a)</td><td>122.40 (n/a)</td><td>68.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>323.00 (n/a)</td><td>222.90 (n/a)</td><td>205.00 (n/a)</td><td>182.70 (n/a)</td><td>57.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>337.50 (n/a)</td><td>289.10 (n/a)</td><td>320.10 (n/a)</td><td>206.00 (n/a)</td><td>57.35 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (+7.47%)</td><td>0.05 (-3.19%)</td><td>0.05 (+2.89%)</td><td>0.04 (-16.34%)</td><td>0.01 <b>(+103.12%)</b></td><td>227.70 (+19.53%)</td><td>184.10 (+5.28%)</td><td>171.50 (-2.78%)</td><td>145.80 (-6.96%)</td><td>32.34 <b>(+128.09%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.50 (n/a)</td><td>174.86 (n/a)</td><td>176.40 (n/a)</td><td>156.70 (n/a)</td><td>14.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (-6.72%)</td><td>0.04 (-4.40%)</td><td>0.04 (-7.83%)</td><td>0.04 (+13.80%)</td><td>0.00 <b>(-53.22%)</b></td><td>201.30 (-12.10%)</td><td>190.62 (+3.29%)</td><td>192.40 (+8.46%)</td><td>172.10 (+7.16%)</td><td>11.93 <b>(-56.18%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.00 (n/a)</td><td>184.54 (n/a)</td><td>177.40 (n/a)</td><td>160.60 (n/a)</td><td>27.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (+2.82%)</td><td>0.05 (-0.79%)</td><td>0.04 (-7.03%)</td><td>0.04 (+1.24%)</td><td>0.01 (+4.78%)</td><td>202.30 (-1.27%)</td><td>179.26 (+0.86%)</td><td>190.90 (+7.61%)</td><td>140.50 (-2.70%)</td><td>24.48 (-1.88%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>177.74 (n/a)</td><td>177.40 (n/a)</td><td>144.40 (n/a)</td><td>24.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 <b>(+31.24%)</b></td><td>0.05 (+18.18%)</td><td>0.05 (+4.70%)</td><td>0.05 (+16.26%)</td><td>0.01 <b>(+89.35%)</b></td><td>176.50 (-13.99%)</td><td>154.94 (-14.08%)</td><td>169.60 (-4.45%)</td><td>117.00 <b>(-23.78%)</b></td><td>26.45 <b>(+25.11%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>180.34 (n/a)</td><td>177.50 (n/a)</td><td>153.50 (n/a)</td><td>21.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 <b>(+26.02%)</b></td><td>0.05 (+18.20%)</td><td>0.05 <b>(+25.22%)</b></td><td>0.03 <b>(-20.49%)</b></td><td>0.01 <b>(+143.19%)</b></td><td>289.40 <b>(+25.77%)</b></td><td>178.84 (-9.46%)</td><td>162.50 <b>(-20.15%)</b></td><td>128.70 <b>(-20.65%)</b></td><td>64.78 <b>(+151.78%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>197.52 (n/a)</td><td>203.50 (n/a)</td><td>162.20 (n/a)</td><td>25.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (+14.61%)</td><td>0.04 (+1.09%)</td><td>0.04 (-3.24%)</td><td>0.03 (-1.27%)</td><td>0.01 <b>(+45.41%)</b></td><td>234.20 (+1.30%)</td><td>193.04 (-0.04%)</td><td>193.50 (+3.37%)</td><td>149.90 (-12.75%)</td><td>31.82 <b>(+28.76%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>193.12 (n/a)</td><td>187.20 (n/a)</td><td>171.80 (n/a)</td><td>24.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (-14.05%)</td><td>0.04 (-4.60%)</td><td>0.04 (+1.53%)</td><td>0.03 (-2.67%)</td><td>0.01 <b>(-23.89%)</b></td><td>237.40 (+2.73%)</td><td>205.74 (+4.15%)</td><td>201.90 (-1.51%)</td><td>171.50 (+16.35%)</td><td>30.35 (-4.92%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>197.54 (n/a)</td><td>205.00 (n/a)</td><td>147.40 (n/a)</td><td>31.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (+13.58%)</td><td>0.04 (+15.72%)</td><td>0.04 (+12.09%)</td><td>0.03 <b>(+21.05%)</b></td><td>0.01 (+5.53%)</td><td>261.10 (-17.40%)</td><td>197.80 (-14.23%)</td><td>198.40 (-10.79%)</td><td>151.70 (-11.96%)</td><td>40.39 <b>(-24.02%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.10 (n/a)</td><td>230.62 (n/a)</td><td>222.40 (n/a)</td><td>172.30 (n/a)</td><td>53.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (-5.02%)</td><td>0.05 (+3.76%)</td><td>0.04 (-10.62%)</td><td>0.04 <b>(+67.62%)</b></td><td>0.01 <b>(-58.34%)</b></td><td>201.00 <b>(-40.32%)</b></td><td>177.62 (-12.22%)</td><td>185.20 (+11.90%)</td><td>148.80 (+5.23%)</td><td>21.70 <b>(-73.53%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>336.80 (n/a)</td><td>202.34 (n/a)</td><td>165.50 (n/a)</td><td>141.40 (n/a)</td><td>82.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (+1.85%)</td><td>0.04 (+5.97%)</td><td>0.04 (+8.82%)</td><td>0.03 (+12.93%)</td><td>0.00 <b>(-30.96%)</b></td><td>234.60 (-11.44%)</td><td>209.24 (-6.30%)</td><td>208.40 (-8.11%)</td><td>187.10 (-1.78%)</td><td>16.87 <b>(-39.86%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>264.90 (n/a)</td><td>223.32 (n/a)</td><td>226.80 (n/a)</td><td>190.50 (n/a)</td><td>28.06 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


### test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (+15.62%)</td><td>0.05 (+13.41%)</td><td>0.05 (+18.86%)</td><td>0.04 (+4.15%)</td><td>0.01 <b>(+97.66%)</b></td><td>197.90 (-3.98%)</td><td>175.88 (-11.14%)</td><td>172.50 (-15.85%)</td><td>153.10 (-13.50%)</td><td>20.64 <b>(+66.68%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.10 (n/a)</td><td>197.94 (n/a)</td><td>205.00 (n/a)</td><td>177.00 (n/a)</td><td>12.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (+19.59%)</td><td>0.04 (-1.39%)</td><td>0.04 (+4.04%)</td><td>0.02 <b>(-29.04%)</b></td><td>0.01 <b>(+109.26%)</b></td><td>343.60 <b>(+40.94%)</b></td><td>229.16 (+6.95%)</td><td>212.10 (-3.90%)</td><td>153.50 (-16.39%)</td><td>69.84 <b>(+157.40%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.80 (n/a)</td><td>214.26 (n/a)</td><td>220.70 (n/a)</td><td>183.60 (n/a)</td><td>27.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.08 <b>(+33.32%)</b></td><td>0.05 (+12.32%)</td><td>0.05 (-1.24%)</td><td>0.04 <b>(+20.95%)</b></td><td>0.01 <b>(+73.55%)</b></td><td>190.80 (-17.33%)</td><td>161.32 (-9.26%)</td><td>174.20 (+1.22%)</td><td>104.70 <b>(-25.00%)</b></td><td>33.21 (+0.43%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>177.78 (n/a)</td><td>172.10 (n/a)</td><td>139.60 (n/a)</td><td>33.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.08 <b>(+32.52%)</b></td><td>0.05 (+15.97%)</td><td>0.05 (+0.58%)</td><td>0.05 <b>(+57.31%)</b></td><td>0.02 (+8.21%)</td><td>181.80 <b>(-36.46%)</b></td><td>162.10 (-16.87%)</td><td>175.90 (-0.57%)</td><td>101.10 <b>(-24.55%)</b></td><td>34.20 <b>(-48.09%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>286.10 (n/a)</td><td>195.00 (n/a)</td><td>176.90 (n/a)</td><td>134.00 (n/a)</td><td>65.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (-2.92%)</td><td>0.05 (-0.24%)</td><td>0.05 (+7.88%)</td><td>0.04 (-3.38%)</td><td>0.01 <b>(+21.19%)</b></td><td>208.10 (+3.48%)</td><td>172.02 (+0.80%)</td><td>156.50 (-7.29%)</td><td>151.50 (+2.99%)</td><td>24.88 <b>(+26.90%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.10 (n/a)</td><td>170.66 (n/a)</td><td>168.80 (n/a)</td><td>147.10 (n/a)</td><td>19.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 <b>(+23.31%)</b></td><td>0.05 (+3.78%)</td><td>0.05 (+7.77%)</td><td>0.04 (-16.03%)</td><td>0.01 <b>(+154.32%)</b></td><td>228.50 (+19.13%)</td><td>176.06 (+0.84%)</td><td>166.20 (-7.20%)</td><td>120.30 (-18.88%)</td><td>44.57 <b>(+151.54%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.80 (n/a)</td><td>174.60 (n/a)</td><td>179.10 (n/a)</td><td>148.30 (n/a)</td><td>17.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (+1.29%)</td><td>0.04 (+3.12%)</td><td>0.05 (+9.26%)</td><td>0.03 (-8.53%)</td><td>0.01 <b>(+28.76%)</b></td><td>267.70 (+9.31%)</td><td>197.16 (-1.59%)</td><td>176.10 (-8.47%)</td><td>161.60 (-1.28%)</td><td>43.18 <b>(+39.61%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.90 (n/a)</td><td>200.34 (n/a)</td><td>192.40 (n/a)</td><td>163.70 (n/a)</td><td>30.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 <b>(+26.37%)</b></td><td>0.05 (+15.61%)</td><td>0.05 (+12.57%)</td><td>0.04 (+1.24%)</td><td>0.01 <b>(+113.99%)</b></td><td>217.80 (-1.22%)</td><td>174.30 (-12.13%)</td><td>177.60 (-11.16%)</td><td>139.40 <b>(-20.84%)</b></td><td>29.24 <b>(+67.97%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>220.50 (n/a)</td><td>198.36 (n/a)</td><td>199.90 (n/a)</td><td>176.10 (n/a)</td><td>17.40 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mha</summary>


### test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.18 (+0.04%)</td><td>0.18 (-0.16%)</td><td>0.18 (-0.18%)</td><td>0.18 (-0.46%)</td><td>0.00 <b>(+37.25%)</b></td><td>47609.20 (+0.46%)</td><td>47363.16 (+0.16%)</td><td>47439.30 (+0.18%)</td><td>46950.80 (-0.04%)</td><td>247.34 <b>(+37.75%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47391.30 (n/a)</td><td>47287.48 (n/a)</td><td>47356.10 (n/a)</td><td>46967.50 (n/a)</td><td>179.57 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/repeat</summary>


### test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word]

_No metrics available._


### test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>182.80 (n/a)</td><td>160.84 (n/a)</td><td>177.00 (n/a)</td><td>122.30 (n/a)</td><td>26.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>168.10 (n/a)</td><td>145.88 (n/a)</td><td>143.80 (n/a)</td><td>126.70 (n/a)</td><td>16.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.70 (n/a)</td><td>158.40 (n/a)</td><td>156.80 (n/a)</td><td>128.30 (n/a)</td><td>25.78 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (-6.43%)</td><td>0.05 (-19.25%)</td><td>0.05 (-19.73%)</td><td>0.04 <b>(-24.64%)</b></td><td>0.01 <b>(+29.74%)</b></td><td>217.40 <b>(+32.64%)</b></td><td>168.12 <b>(+25.74%)</b></td><td>161.50 <b>(+24.52%)</b></td><td>130.30 (+6.89%)</td><td>31.66 <b>(+83.25%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>163.90 (n/a)</td><td>133.70 (n/a)</td><td>129.70 (n/a)</td><td>121.90 (n/a)</td><td>17.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.09 (-17.81%)</td><td>0.07 (-12.23%)</td><td>0.07 (-15.61%)</td><td>0.06 (+12.32%)</td><td>0.01 <b>(-52.75%)</b></td><td>199.90 (-10.96%)</td><td>167.30 (+9.58%)</td><td>166.30 (+18.53%)</td><td>144.10 <b>(+21.71%)</b></td><td>21.55 <b>(-49.58%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>224.50 (n/a)</td><td>152.68 (n/a)</td><td>140.30 (n/a)</td><td>118.40 (n/a)</td><td>42.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 <b>(-20.74%)</b></td><td>0.05 (-15.12%)</td><td>0.05 (-12.30%)</td><td>0.04 (-10.06%)</td><td>0.01 <b>(-38.18%)</b></td><td>194.80 (+11.19%)</td><td>168.44 (+16.94%)</td><td>165.20 (+14.01%)</td><td>148.50 <b>(+26.17%)</b></td><td>17.96 (-13.22%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.20 (n/a)</td><td>144.04 (n/a)</td><td>144.90 (n/a)</td><td>117.70 (n/a)</td><td>20.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (-13.87%)</td><td>0.06 (-17.76%)</td><td>0.06 (-10.68%)</td><td>0.04 <b>(-33.88%)</b></td><td>0.01 (+9.51%)</td><td>267.30 <b>(+51.19%)</b></td><td>190.02 <b>(+24.10%)</b></td><td>177.50 (+11.92%)</td><td>149.60 (+16.06%)</td><td>45.32 <b>(+104.23%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>176.80 (n/a)</td><td>153.12 (n/a)</td><td>158.60 (n/a)</td><td>128.90 (n/a)</td><td>22.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (-4.93%)</td><td>0.05 (-3.02%)</td><td>0.05 (-7.96%)</td><td>0.04 (-1.20%)</td><td>0.01 (-1.83%)</td><td>182.90 (+1.22%)</td><td>160.68 (+3.29%)</td><td>177.70 (+8.62%)</td><td>121.80 (+5.18%)</td><td>27.09 (+8.69%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.70 (n/a)</td><td>155.56 (n/a)</td><td>163.60 (n/a)</td><td>115.80 (n/a)</td><td>24.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (-14.85%)</td><td>0.06 (-16.75%)</td><td>0.06 (-15.35%)</td><td>0.05 (-18.03%)</td><td>0.01 <b>(+32.27%)</b></td><td>205.20 <b>(+22.00%)</b></td><td>180.10 <b>(+21.07%)</b></td><td>173.30 (+18.13%)</td><td>157.80 (+17.41%)</td><td>23.23 <b>(+89.70%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>168.20 (n/a)</td><td>148.76 (n/a)</td><td>146.70 (n/a)</td><td>134.40 (n/a)</td><td>12.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (-2.00%)</td><td>0.05 (-6.31%)</td><td>0.05 (-9.85%)</td><td>0.03 <b>(-23.68%)</b></td><td>0.01 <b>(+36.72%)</b></td><td>271.90 <b>(+31.04%)</b></td><td>178.08 (+11.05%)</td><td>171.20 (+10.88%)</td><td>127.50 (+2.08%)</td><td>56.26 <b>(+85.41%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>160.36 (n/a)</td><td>154.40 (n/a)</td><td>124.90 (n/a)</td><td>30.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (+0.17%)</td><td>0.06 (-10.08%)</td><td>0.06 (-1.98%)</td><td>0.04 <b>(-26.43%)</b></td><td>0.01 <b>(+64.45%)</b></td><td>231.90 <b>(+35.93%)</b></td><td>170.92 (+14.51%)</td><td>158.90 (+2.06%)</td><td>126.40 (-0.16%)</td><td>39.54 <b>(+128.60%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.60 (n/a)</td><td>149.26 (n/a)</td><td>155.70 (n/a)</td><td>126.60 (n/a)</td><td>17.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (+0.47%)</td><td>0.05 (-7.37%)</td><td>0.05 (-9.75%)</td><td>0.04 (-16.01%)</td><td>0.01 <b>(+205.95%)</b></td><td>189.40 (+19.04%)</td><td>163.84 (+8.89%)</td><td>165.60 (+10.84%)</td><td>145.50 (-0.48%)</td><td>17.93 <b>(+255.36%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>159.10 (n/a)</td><td>150.46 (n/a)</td><td>149.40 (n/a)</td><td>146.20 (n/a)</td><td>5.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (+0.89%)</td><td>0.05 (-1.08%)</td><td>0.05 (-3.50%)</td><td>0.05 (+8.51%)</td><td>0.01 <b>(-22.22%)</b></td><td>194.70 (-7.81%)</td><td>171.10 (+0.13%)</td><td>177.10 (+3.63%)</td><td>141.30 (-0.84%)</td><td>20.70 <b>(-27.95%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>170.88 (n/a)</td><td>170.90 (n/a)</td><td>142.50 (n/a)</td><td>28.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (-16.59%)</td><td>0.04 <b>(-21.10%)</b></td><td>0.05 (-16.32%)</td><td>0.03 <b>(-42.02%)</b></td><td>0.01 <b>(+39.48%)</b></td><td>287.70 <b>(+72.48%)</b></td><td>197.62 <b>(+31.71%)</b></td><td>177.10 (+19.50%)</td><td>146.70 (+19.85%)</td><td>54.33 <b>(+196.70%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>166.80 (n/a)</td><td>150.04 (n/a)</td><td>148.20 (n/a)</td><td>122.40 (n/a)</td><td>18.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (-0.43%)</td><td>0.04 (-16.93%)</td><td>0.04 (-17.36%)</td><td>0.02 <b>(-45.58%)</b></td><td>0.01 <b>(+204.84%)</b></td><td>351.00 <b>(+83.77%)</b></td><td>221.06 <b>(+29.78%)</b></td><td>199.50 <b>(+20.98%)</b></td><td>156.80 (+0.45%)</td><td>77.60 <b>(+471.38%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>191.00 (n/a)</td><td>170.34 (n/a)</td><td>164.90 (n/a)</td><td>156.10 (n/a)</td><td>13.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (+3.64%)</td><td>0.05 (+0.64%)</td><td>0.06 (-3.16%)</td><td>0.04 (+5.11%)</td><td>0.01 (-13.27%)</td><td>182.60 (-4.90%)</td><td>151.58 (-1.37%)</td><td>148.50 (+3.27%)</td><td>124.50 (-3.56%)</td><td>22.10 (-19.37%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.00 (n/a)</td><td>153.68 (n/a)</td><td>143.80 (n/a)</td><td>129.10 (n/a)</td><td>27.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (-11.77%)</td><td>0.05 (-8.13%)</td><td>0.05 (-6.25%)</td><td>0.04 (+3.03%)</td><td>0.00 <b>(-46.77%)</b></td><td>214.10 (-2.95%)</td><td>190.98 (+7.47%)</td><td>184.10 (+6.66%)</td><td>172.40 (+13.35%)</td><td>16.68 <b>(-40.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>177.70 (n/a)</td><td>172.60 (n/a)</td><td>152.10 (n/a)</td><td>28.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (-0.94%)</td><td>0.04 (+2.05%)</td><td>0.04 (+6.92%)</td><td>0.04 (+13.68%)</td><td>0.00 <b>(-28.72%)</b></td><td>229.40 (-12.04%)</td><td>198.96 (-3.17%)</td><td>189.80 (-6.46%)</td><td>172.90 (+0.93%)</td><td>22.92 <b>(-35.80%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.80 (n/a)</td><td>205.48 (n/a)</td><td>202.90 (n/a)</td><td>171.30 (n/a)</td><td>35.70 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.78 (+7.08%)</td><td>0.66 (+19.60%)</td><td>0.63 (+15.74%)</td><td>0.60 <b>(+32.64%)</b></td><td>0.07 <b>(-34.48%)</b></td><td>164.80 <b>(-24.61%)</b></td><td>150.24 (-18.11%)</td><td>157.20 (-13.63%)</td><td>126.50 (-6.64%)</td><td>15.29 <b>(-54.54%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.73 (n/a)</td><td>0.55 (n/a)</td><td>0.54 (n/a)</td><td>0.45 (n/a)</td><td>0.11 (n/a)</td><td>218.60 (n/a)</td><td>183.46 (n/a)</td><td>182.00 (n/a)</td><td>135.50 (n/a)</td><td>33.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.78 (+13.10%)</td><td>0.68 <b>(+24.84%)</b></td><td>0.66 <b>(+27.08%)</b></td><td>0.53 (+18.11%)</td><td>0.11 (+17.15%)</td><td>187.00 (-15.35%)</td><td>147.98 (-19.86%)</td><td>147.90 <b>(-21.33%)</b></td><td>125.70 (-11.60%)</td><td>25.18 (-12.06%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.69 (n/a)</td><td>0.54 (n/a)</td><td>0.52 (n/a)</td><td>0.45 (n/a)</td><td>0.09 (n/a)</td><td>220.90 (n/a)</td><td>184.66 (n/a)</td><td>188.00 (n/a)</td><td>142.20 (n/a)</td><td>28.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.65 (+4.37%)</td><td>0.52 (-6.32%)</td><td>0.50 (-7.89%)</td><td>0.42 (-10.33%)</td><td>0.08 <b>(+39.83%)</b></td><td>231.90 (+11.54%)</td><td>194.26 (+7.78%)</td><td>195.40 (+8.56%)</td><td>151.60 (-4.23%)</td><td>28.85 <b>(+47.05%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.62 (n/a)</td><td>0.55 (n/a)</td><td>0.55 (n/a)</td><td>0.47 (n/a)</td><td>0.06 (n/a)</td><td>207.90 (n/a)</td><td>180.24 (n/a)</td><td>180.00 (n/a)</td><td>158.30 (n/a)</td><td>19.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.80 <b>(+40.86%)</b></td><td>0.55 <b>(+23.98%)</b></td><td>0.54 <b>(+31.98%)</b></td><td>0.31 (+7.94%)</td><td>0.18 <b>(+53.96%)</b></td><td>320.80 (-7.36%)</td><td>196.82 (-16.33%)</td><td>180.70 <b>(-24.23%)</b></td><td>123.30 <b>(-28.97%)</b></td><td>75.08 (+7.62%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.57 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.12 (n/a)</td><td>346.30 (n/a)</td><td>235.24 (n/a)</td><td>238.50 (n/a)</td><td>173.60 (n/a)</td><td>69.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.60 <b>(+30.78%)</b></td><td>0.54 <b>(+32.02%)</b></td><td>0.58 <b>(+42.73%)</b></td><td>0.37 (+7.90%)</td><td>0.10 <b>(+94.43%)</b></td><td>198.30 (-7.34%)</td><td>140.48 <b>(-22.62%)</b></td><td>127.60 <b>(-29.97%)</b></td><td>121.90 <b>(-23.53%)</b></td><td>32.50 <b>(+43.32%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.46 (n/a)</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.05 (n/a)</td><td>214.00 (n/a)</td><td>181.54 (n/a)</td><td>182.20 (n/a)</td><td>159.40 (n/a)</td><td>22.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.58 (-4.13%)</td><td>0.48 (+1.99%)</td><td>0.49 (+10.66%)</td><td>0.40 (-1.76%)</td><td>0.07 (-17.39%)</td><td>185.70 (+1.81%)</td><td>155.28 (-2.49%)</td><td>150.90 (-9.64%)</td><td>128.20 (+4.31%)</td><td>21.20 (-11.38%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.60 (n/a)</td><td>0.47 (n/a)</td><td>0.44 (n/a)</td><td>0.40 (n/a)</td><td>0.08 (n/a)</td><td>182.40 (n/a)</td><td>159.24 (n/a)</td><td>167.00 (n/a)</td><td>122.90 (n/a)</td><td>23.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.50 (-2.29%)</td><td>0.42 (+7.68%)</td><td>0.45 (+9.78%)</td><td>0.34 <b>(+30.77%)</b></td><td>0.07 <b>(-29.06%)</b></td><td>219.10 <b>(-23.53%)</b></td><td>177.82 (-10.25%)</td><td>165.30 (-8.93%)</td><td>148.00 (+2.28%)</td><td>30.84 <b>(-44.97%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.41 (n/a)</td><td>0.26 (n/a)</td><td>0.10 (n/a)</td><td>286.50 (n/a)</td><td>198.12 (n/a)</td><td>181.50 (n/a)</td><td>144.70 (n/a)</td><td>56.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.42 (-14.24%)</td><td>0.38 (+4.41%)</td><td>0.39 (+5.34%)</td><td>0.35 (+15.46%)</td><td>0.03 <b>(-61.87%)</b></td><td>213.10 (-13.41%)</td><td>192.38 (-6.64%)</td><td>186.80 (-5.03%)</td><td>177.60 (+16.61%)</td><td>14.56 <b>(-62.07%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.48 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>246.10 (n/a)</td><td>206.06 (n/a)</td><td>196.70 (n/a)</td><td>152.30 (n/a)</td><td>38.39 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/softmax</summary>


### test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.14 <b>(+39.03%)</b></td><td>0.84 <b>(+24.62%)</b></td><td>0.79 (+11.08%)</td><td>0.60 <b>(+29.99%)</b></td><td>0.24 <b>(+66.54%)</b></td><td>217.40 <b>(-23.04%)</b></td><td>167.24 (-17.96%)</td><td>166.70 (-9.99%)</td><td>115.40 <b>(-28.05%)</b></td><td>45.95 (-7.28%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.82 (n/a)</td><td>0.67 (n/a)</td><td>0.71 (n/a)</td><td>0.46 (n/a)</td><td>0.14 (n/a)</td><td>282.50 (n/a)</td><td>203.84 (n/a)</td><td>185.20 (n/a)</td><td>160.40 (n/a)</td><td>49.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.02 (+3.85%)</td><td>0.64 (-4.99%)</td><td>0.59 (-16.36%)</td><td>0.36 (-3.22%)</td><td>0.24 (+2.49%)</td><td>361.80 (+3.31%)</td><td>227.96 (+5.13%)</td><td>222.40 (+19.57%)</td><td>128.90 (-3.66%)</td><td>84.58 (-0.52%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.98 (n/a)</td><td>0.67 (n/a)</td><td>0.70 (n/a)</td><td>0.37 (n/a)</td><td>0.23 (n/a)</td><td>350.20 (n/a)</td><td>216.84 (n/a)</td><td>186.00 (n/a)</td><td>133.80 (n/a)</td><td>85.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.09 <b>(+21.68%)</b></td><td>0.85 (+15.10%)</td><td>0.83 (+11.29%)</td><td>0.62 (+2.83%)</td><td>0.20 <b>(+62.00%)</b></td><td>212.40 (-2.75%)</td><td>162.56 (-11.03%)</td><td>158.30 (-10.11%)</td><td>120.70 (-17.78%)</td><td>39.28 <b>(+26.18%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.89 (n/a)</td><td>0.73 (n/a)</td><td>0.74 (n/a)</td><td>0.60 (n/a)</td><td>0.12 (n/a)</td><td>218.40 (n/a)</td><td>182.72 (n/a)</td><td>176.10 (n/a)</td><td>146.80 (n/a)</td><td>31.13 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/strided_copy</summary>


### test_strided_copy[chunked_transfer]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 (-8.95%)</td><td>0.02 (+1.28%)</td><td>0.02 (+13.91%)</td><td>0.02 (+2.41%)</td><td>0.01 <b>(-26.37%)</b></td><td>208.10 (-2.35%)</td><td>177.30 (-3.48%)</td><td>179.60 (-12.18%)</td><td>125.90 (+9.76%)</td><td>32.66 <b>(-21.40%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>183.70 (n/a)</td><td>204.50 (n/a)</td><td>114.70 (n/a)</td><td>41.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[contiguous]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 <b>(-26.05%)</b></td><td>0.02 (-4.42%)</td><td>0.02 (+2.46%)</td><td>0.02 (+15.83%)</td><td>0.00 <b>(-54.29%)</b></td><td>233.10 (-13.67%)</td><td>180.32 (-2.10%)</td><td>170.40 (-2.41%)</td><td>145.50 <b>(+35.22%)</b></td><td>33.16 <b>(-44.60%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>270.00 (n/a)</td><td>184.18 (n/a)</td><td>174.60 (n/a)</td><td>107.60 (n/a)</td><td>59.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 <b>(-22.22%)</b></td><td>0.02 (-12.38%)</td><td>0.02 (-6.70%)</td><td>0.02 (-14.47%)</td><td>0.00 <b>(-22.72%)</b></td><td>254.50 (+16.90%)</td><td>193.72 (+13.74%)</td><td>189.90 (+7.17%)</td><td>156.20 <b>(+28.56%)</b></td><td>40.58 (+15.90%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>170.32 (n/a)</td><td>177.20 (n/a)</td><td>121.50 (n/a)</td><td>35.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.93 (+8.17%)</td><td>0.80 (+3.78%)</td><td>0.79 (-3.07%)</td><td>0.63 (+18.76%)</td><td>0.12 (-14.61%)</td><td>209.60 (-15.79%)</td><td>168.58 (-5.04%)</td><td>166.50 (+3.16%)</td><td>141.30 (-7.59%)</td><td>26.36 <b>(-34.69%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.86 (n/a)</td><td>0.77 (n/a)</td><td>0.82 (n/a)</td><td>0.53 (n/a)</td><td>0.14 (n/a)</td><td>248.90 (n/a)</td><td>177.52 (n/a)</td><td>161.40 (n/a)</td><td>152.90 (n/a)</td><td>40.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.05 (-4.21%)</td><td>0.84 (-14.18%)</td><td>0.78 (-19.39%)</td><td>0.69 (-12.41%)</td><td>0.14 (+14.37%)</td><td>192.40 (+14.18%)</td><td>161.66 (+17.45%)</td><td>169.50 <b>(+24.08%)</b></td><td>126.00 (+4.39%)</td><td>26.16 <b>(+35.61%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.09 (n/a)</td><td>0.97 (n/a)</td><td>0.97 (n/a)</td><td>0.78 (n/a)</td><td>0.13 (n/a)</td><td>168.50 (n/a)</td><td>137.64 (n/a)</td><td>136.60 (n/a)</td><td>120.70 (n/a)</td><td>19.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.02 (-2.31%)</td><td>0.79 (-1.02%)</td><td>0.76 (-8.96%)</td><td>0.68 (+19.07%)</td><td>0.13 <b>(-27.67%)</b></td><td>195.60 (-16.05%)</td><td>169.56 (-1.46%)</td><td>173.80 (+9.79%)</td><td>129.20 (+2.38%)</td><td>24.43 <b>(-41.01%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.05 (n/a)</td><td>0.80 (n/a)</td><td>0.83 (n/a)</td><td>0.57 (n/a)</td><td>0.18 (n/a)</td><td>233.00 (n/a)</td><td>172.08 (n/a)</td><td>158.30 (n/a)</td><td>126.20 (n/a)</td><td>41.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.03 (-14.19%)</td><td>0.82 (-6.66%)</td><td>0.79 (-1.54%)</td><td>0.72 (-4.94%)</td><td>0.12 <b>(-35.54%)</b></td><td>182.30 (+5.19%)</td><td>162.50 (+5.59%)</td><td>166.80 (+1.52%)</td><td>128.00 (+16.58%)</td><td>20.38 <b>(-23.09%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.20 (n/a)</td><td>0.88 (n/a)</td><td>0.80 (n/a)</td><td>0.76 (n/a)</td><td>0.19 (n/a)</td><td>173.30 (n/a)</td><td>153.90 (n/a)</td><td>164.30 (n/a)</td><td>109.80 (n/a)</td><td>26.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot_last]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.07 (-3.75%)</td><td>0.79 (-14.64%)</td><td>0.70 <b>(-30.54%)</b></td><td>0.67 (-9.54%)</td><td>0.17 (-1.42%)</td><td>198.00 (+10.55%)</td><td>172.36 (+17.41%)</td><td>187.70 <b>(+44.05%)</b></td><td>122.90 (+3.89%)</td><td>31.20 (+8.95%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.12 (n/a)</td><td>0.93 (n/a)</td><td>1.01 (n/a)</td><td>0.74 (n/a)</td><td>0.17 (n/a)</td><td>179.10 (n/a)</td><td>146.80 (n/a)</td><td>130.30 (n/a)</td><td>118.30 (n/a)</td><td>28.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 (-5.88%)</td><td>0.03 (-4.61%)</td><td>0.03 (+1.91%)</td><td>0.02 (-12.15%)</td><td>0.00 (-1.10%)</td><td>207.80 (+13.86%)</td><td>163.86 (+5.27%)</td><td>162.00 (-1.88%)</td><td>127.30 (+6.17%)</td><td>30.06 <b>(+21.38%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.50 (n/a)</td><td>155.66 (n/a)</td><td>165.10 (n/a)</td><td>119.90 (n/a)</td><td>24.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels_chunked]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 (-14.47%)</td><td>0.02 (-11.12%)</td><td>0.02 (-10.10%)</td><td>0.02 (-18.44%)</td><td>0.01 (+8.74%)</td><td>234.00 <b>(+22.64%)</b></td><td>188.82 (+14.34%)</td><td>188.40 (+11.28%)</td><td>146.00 (+16.89%)</td><td>41.71 <b>(+54.08%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.80 (n/a)</td><td>165.14 (n/a)</td><td>169.30 (n/a)</td><td>124.90 (n/a)</td><td>27.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]

_No metrics available._


</details>


<details>
<summary>iron/operators/swiglu_decode</summary>


### test_swiglu_decode[embedding_dim_1024-hidden_dim_3584]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.00 (+0.00%)</td><td>0.00 (-1.84%)</td><td>0.00 (-2.27%)</td><td>0.00 (-7.14%)</td><td>0.00 <b>(+71.59%)</b></td><td>1039.69 (+5.73%)</td><td>960.02 (+1.89%)</td><td>949.20 (+1.72%)</td><td>905.49 (+0.47%)</td><td>50.49 <b>(+46.85%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>983.35 (n/a)</td><td>942.25 (n/a)</td><td>933.12 (n/a)</td><td>901.27 (n/a)</td><td>34.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_decode[embedding_dim_2048-hidden_dim_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.01 (+0.00%)</td><td>0.01 (+1.77%)</td><td>0.01 (+1.27%)</td><td>0.01 (+1.33%)</td><td>0.00 (-0.96%)</td><td>1080.50 (-1.05%)</td><td>1020.15 (-1.57%)</td><td>1028.21 (-0.88%)</td><td>976.42 (+0.63%)</td><td>41.86 (-3.98%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1092.01 (n/a)</td><td>1036.47 (n/a)</td><td>1037.39 (n/a)</td><td>970.26 (n/a)</td><td>43.59 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/swiglu_prefill</summary>


### test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.96 (-1.68%)</td><td>0.96 (-0.48%)</td><td>0.96 (-0.57%)</td><td>0.95 (+1.05%)</td><td>0.00 <b>(-73.94%)</b></td><td>2196.29 (-1.03%)</td><td>2187.22 (+0.47%)</td><td>2186.03 (+0.57%)</td><td>2179.83 (+1.71%)</td><td>7.13 <b>(-73.80%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2219.24 (n/a)</td><td>2176.91 (n/a)</td><td>2173.66 (n/a)</td><td>2143.18 (n/a)</td><td>27.21 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/swiglu_prefill_stream</summary>


### test_swiglu_prefill_stream[k_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.40 (+0.30%)</td><td>0.39 (-0.92%)</td><td>0.38 (-1.46%)</td><td>0.38 (-0.03%)</td><td>0.01 (+11.67%)</td><td>1375.26 (+0.01%)</td><td>1357.79 (+0.92%)</td><td>1364.91 (+1.47%)</td><td>1321.38 (-0.30%)</td><td>22.43 (+10.99%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1375.17 (n/a)</td><td>1345.35 (n/a)</td><td>1345.14 (n/a)</td><td>1325.32 (n/a)</td><td>20.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill_stream[k_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.26 (+0.23%)</td><td>0.25 (+1.17%)</td><td>0.25 (+0.72%)</td><td>0.25 (+2.08%)</td><td>0.00 <b>(-30.75%)</b></td><td>2136.25 (-2.05%)</td><td>2087.49 (-1.18%)</td><td>2075.67 (-0.71%)</td><td>2047.51 (-0.22%)</td><td>40.47 <b>(-32.34%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.01 (n/a)</td><td>2180.90 (n/a)</td><td>2112.50 (n/a)</td><td>2090.43 (n/a)</td><td>2052.10 (n/a)</td><td>59.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill_stream[k_5]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.38 (-2.24%)</td><td>0.37 (+0.86%)</td><td>0.37 (+1.73%)</td><td>0.37 (+1.22%)</td><td>0.00 <b>(-59.28%)</b></td><td>1435.28 (-1.20%)</td><td>1416.03 (-0.90%)</td><td>1415.66 (-1.71%)</td><td>1397.62 (+2.27%)</td><td>14.65 <b>(-58.44%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1452.66 (n/a)</td><td>1428.87 (n/a)</td><td>1440.23 (n/a)</td><td>1366.55 (n/a)</td><td>35.24 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>3.32 (-8.02%)</td><td>2.98 (+3.42%)</td><td>2.88 (+3.48%)</td><td>2.61 (+5.75%)</td><td>0.32 <b>(-25.79%)</b></td><td>200.60 (-5.42%)</td><td>177.50 (-3.93%)</td><td>182.10 (-3.34%)</td><td>158.10 (+8.73%)</td><td>18.71 <b>(-22.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>3.61 (n/a)</td><td>2.88 (n/a)</td><td>2.78 (n/a)</td><td>2.47 (n/a)</td><td>0.43 (n/a)</td><td>212.10 (n/a)</td><td>184.76 (n/a)</td><td>188.40 (n/a)</td><td>145.40 (n/a)</td><td>24.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>5.85 (+18.69%)</td><td>5.21 (+12.75%)</td><td>5.12 (+9.54%)</td><td>4.55 (+5.46%)</td><td>0.50 <b>(+95.83%)</b></td><td>230.40 (-5.19%)</td><td>202.82 (-10.87%)</td><td>204.80 (-8.73%)</td><td>179.30 (-15.74%)</td><td>19.55 <b>(+55.58%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>4.93 (n/a)</td><td>4.62 (n/a)</td><td>4.67 (n/a)</td><td>4.31 (n/a)</td><td>0.25 (n/a)</td><td>243.00 (n/a)</td><td>227.56 (n/a)</td><td>224.40 (n/a)</td><td>212.80 (n/a)</td><td>12.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>3.72 <b>(+20.32%)</b></td><td>3.12 (+16.02%)</td><td>3.04 (+6.32%)</td><td>2.73 <b>(+32.06%)</b></td><td>0.43 (+8.15%)</td><td>192.20 <b>(-24.30%)</b></td><td>170.32 (-14.26%)</td><td>172.50 (-5.94%)</td><td>141.00 (-16.86%)</td><td>22.57 <b>(-32.31%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>3.09 (n/a)</td><td>2.69 (n/a)</td><td>2.86 (n/a)</td><td>2.07 (n/a)</td><td>0.40 (n/a)</td><td>253.90 (n/a)</td><td>198.64 (n/a)</td><td>183.40 (n/a)</td><td>169.60 (n/a)</td><td>33.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>3.17 <b>(-32.60%)</b></td><td>2.86 (-13.50%)</td><td>2.96 (+8.00%)</td><td>2.59 (+14.34%)</td><td>0.25 <b>(-75.81%)</b></td><td>202.10 (-12.55%)</td><td>184.18 (+7.92%)</td><td>176.90 (-7.43%)</td><td>165.60 <b>(+48.39%)</b></td><td>16.36 <b>(-67.12%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>4.70 (n/a)</td><td>3.31 (n/a)</td><td>2.74 (n/a)</td><td>2.27 (n/a)</td><td>1.04 (n/a)</td><td>231.10 (n/a)</td><td>170.66 (n/a)</td><td>191.10 (n/a)</td><td>111.60 (n/a)</td><td>49.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>4.36 (+7.95%)</td><td>3.26 (+13.04%)</td><td>3.33 <b>(+22.37%)</b></td><td>2.38 (+18.97%)</td><td>0.79 (-14.92%)</td><td>220.70 (-15.96%)</td><td>168.40 (-14.68%)</td><td>157.40 (-18.28%)</td><td>120.30 (-7.39%)</td><td>40.78 <b>(-34.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>4.04 (n/a)</td><td>2.89 (n/a)</td><td>2.72 (n/a)</td><td>2.00 (n/a)</td><td>0.93 (n/a)</td><td>262.60 (n/a)</td><td>197.38 (n/a)</td><td>192.60 (n/a)</td><td>129.90 (n/a)</td><td>62.14 (n/a)</td>
</tr>
</tbody>
</table>


</details>
