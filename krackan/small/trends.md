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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.13 <b>(+40.70%)</b></td><td>0.09 (+11.46%)</td><td>0.08 (+3.66%)</td><td>0.06 (-5.86%)</td><td>0.02 <b>(+170.43%)</b></td><td>191.70 (+6.20%)</td><td>147.50 (-6.56%)</td><td>154.60 (-3.56%)</td><td>96.50 <b>(-28.89%)</b></td><td>34.37 <b>(+96.32%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.50 (n/a)</td><td>157.86 (n/a)</td><td>160.30 (n/a)</td><td>135.70 (n/a)</td><td>17.51 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.11 <b>(+49.93%)</b></td><td>0.08 <b>(+29.19%)</b></td><td>0.09 <b>(+36.32%)</b></td><td>0.05 (-12.74%)</td><td>0.02 <b>(+198.92%)</b></td><td>259.90 (+14.59%)</td><td>161.02 (-16.73%)</td><td>136.20 <b>(-26.66%)</b></td><td>113.80 <b>(-33.33%)</b></td><td>59.11 <b>(+136.88%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.80 (n/a)</td><td>193.38 (n/a)</td><td>185.70 (n/a)</td><td>170.70 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.10 (-4.89%)</td><td>0.08 (+3.13%)</td><td>0.08 (+8.00%)</td><td>0.04 <b>(-23.01%)</b></td><td>0.02 (+17.50%)</td><td>317.30 <b>(+29.88%)</b></td><td>178.62 (+2.30%)</td><td>153.90 (-7.40%)</td><td>125.30 (+5.21%)</td><td>78.60 <b>(+71.39%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>244.30 (n/a)</td><td>174.60 (n/a)</td><td>166.20 (n/a)</td><td>119.10 (n/a)</td><td>45.86 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.09 (+4.11%)</td><td>0.08 <b>(+24.58%)</b></td><td>0.08 <b>(+25.73%)</b></td><td>0.06 <b>(+40.33%)</b></td><td>0.01 <b>(-38.39%)</b></td><td>189.60 <b>(-28.75%)</b></td><td>158.50 <b>(-22.19%)</b></td><td>156.40 <b>(-20.49%)</b></td><td>135.10 (-3.98%)</td><td>19.79 <b>(-56.33%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>266.10 (n/a)</td><td>203.70 (n/a)</td><td>196.70 (n/a)</td><td>140.70 (n/a)</td><td>45.32 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (+7.50%)</td><td>0.03 (-9.25%)</td><td>0.03 (-19.11%)</td><td>0.02 (-19.01%)</td><td>0.01 <b>(+48.59%)</b></td><td>212.40 <b>(+23.49%)</b></td><td>163.12 (+13.40%)</td><td>168.80 <b>(+23.57%)</b></td><td>106.00 (-6.94%)</td><td>37.99 <b>(+60.03%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>172.00 (n/a)</td><td>143.84 (n/a)</td><td>136.60 (n/a)</td><td>113.90 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 <b>(-26.23%)</b></td><td>0.04 (-8.18%)</td><td>0.04 (+12.81%)</td><td>0.03 (-15.61%)</td><td>0.01 <b>(-31.06%)</b></td><td>192.50 (+18.53%)</td><td>153.28 (+7.93%)</td><td>136.40 (-11.31%)</td><td>127.50 <b>(+35.49%)</b></td><td>31.60 (+11.97%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>162.40 (n/a)</td><td>142.02 (n/a)</td><td>153.80 (n/a)</td><td>94.10 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (-8.57%)</td><td>0.03 <b>(-29.40%)</b></td><td>0.03 <b>(-26.83%)</b></td><td>0.02 <b>(-44.55%)</b></td><td>0.01 <b>(+57.70%)</b></td><td>291.30 <b>(+80.37%)</b></td><td>216.26 <b>(+51.53%)</b></td><td>205.90 <b>(+36.72%)</b></td><td>128.60 (+9.35%)</td><td>66.37 <b>(+214.59%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>161.50 (n/a)</td><td>142.72 (n/a)</td><td>150.60 (n/a)</td><td>117.60 (n/a)</td><td>21.10 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (-3.75%)</td><td>0.03 (-1.81%)</td><td>0.03 (-7.76%)</td><td>0.03 (-1.69%)</td><td>0.01 (+0.03%)</td><td>207.80 (+1.71%)</td><td>178.48 (+2.07%)</td><td>195.20 (+8.38%)</td><td>133.30 (+3.90%)</td><td>31.34 (+9.27%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>174.86 (n/a)</td><td>180.10 (n/a)</td><td>128.30 (n/a)</td><td>28.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.03 (-10.78%)</td><td>0.03 (-1.33%)</td><td>0.03 (-0.54%)</td><td>0.02 (+2.56%)</td><td>0.00 <b>(-24.76%)</b></td><td>231.70 (-2.52%)</td><td>186.44 (+0.18%)</td><td>177.80 (+0.51%)</td><td>158.10 (+12.05%)</td><td>29.89 (-18.20%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>186.10 (n/a)</td><td>176.90 (n/a)</td><td>141.10 (n/a)</td><td>36.54 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 <b>(+28.17%)</b></td><td>0.03 (+4.16%)</td><td>0.03 (-1.70%)</td><td>0.02 (-3.49%)</td><td>0.01 <b>(+217.90%)</b></td><td>210.10 (+3.60%)</td><td>186.76 (-2.16%)</td><td>191.20 (+1.76%)</td><td>139.00 <b>(-22.00%)</b></td><td>27.97 <b>(+146.99%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>202.80 (n/a)</td><td>190.88 (n/a)</td><td>187.90 (n/a)</td><td>178.20 (n/a)</td><td>11.32 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (-11.91%)</td><td>0.03 (-2.46%)</td><td>0.03 (-1.97%)</td><td>0.02 (-5.90%)</td><td>0.01 <b>(-20.97%)</b></td><td>214.90 (+6.28%)</td><td>178.20 (+1.47%)</td><td>186.40 (+1.97%)</td><td>129.60 (+13.49%)</td><td>35.21 (-2.51%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>175.62 (n/a)</td><td>182.80 (n/a)</td><td>114.20 (n/a)</td><td>36.12 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.03 <b>(+21.88%)</b></td><td>0.02 (-8.70%)</td><td>0.02 (+0.02%)</td><td>0.01 <b>(-38.17%)</b></td><td>0.01 <b>(+568.76%)</b></td><td>393.10 <b>(+61.70%)</b></td><td>272.84 (+19.83%)</td><td>223.70 (-0.04%)</td><td>178.20 (-17.92%)</td><td>94.13 <b>(+817.06%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>243.10 (n/a)</td><td>227.68 (n/a)</td><td>223.80 (n/a)</td><td>217.10 (n/a)</td><td>10.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>234.60 (n/a)</td><td>188.04 (n/a)</td><td>195.20 (n/a)</td><td>130.00 (n/a)</td><td>40.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>203.38 (n/a)</td><td>199.30 (n/a)</td><td>169.50 (n/a)</td><td>24.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.10 (n/a)</td><td>191.42 (n/a)</td><td>203.90 (n/a)</td><td>157.10 (n/a)</td><td>29.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>255.30 (n/a)</td><td>215.20 (n/a)</td><td>218.10 (n/a)</td><td>183.10 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>286.00 (n/a)</td><td>192.06 (n/a)</td><td>167.00 (n/a)</td><td>161.30 (n/a)</td><td>53.29 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>290.00 (n/a)</td><td>192.72 (n/a)</td><td>166.60 (n/a)</td><td>151.30 (n/a)</td><td>57.06 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.30 (n/a)</td><td>191.92 (n/a)</td><td>198.80 (n/a)</td><td>141.40 (n/a)</td><td>33.66 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>188.02 (n/a)</td><td>184.70 (n/a)</td><td>168.80 (n/a)</td><td>20.50 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.50 (n/a)</td><td>152.90 (n/a)</td><td>152.90 (n/a)</td><td>115.20 (n/a)</td><td>29.14 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.50 (n/a)</td><td>167.72 (n/a)</td><td>162.10 (n/a)</td><td>117.60 (n/a)</td><td>41.93 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>159.90 (n/a)</td><td>153.90 (n/a)</td><td>135.80 (n/a)</td><td>20.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.00 (n/a)</td><td>173.80 (n/a)</td><td>174.40 (n/a)</td><td>128.70 (n/a)</td><td>35.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>167.76 (n/a)</td><td>162.40 (n/a)</td><td>146.70 (n/a)</td><td>21.90 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.80 (n/a)</td><td>170.80 (n/a)</td><td>148.50 (n/a)</td><td>134.90 (n/a)</td><td>38.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.50 (n/a)</td><td>171.32 (n/a)</td><td>175.40 (n/a)</td><td>143.30 (n/a)</td><td>19.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.40 (n/a)</td><td>196.90 (n/a)</td><td>196.30 (n/a)</td><td>147.60 (n/a)</td><td>34.84 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>4.54 (+9.93%)</td><td>4.08 (+0.17%)</td><td>4.08 (-0.09%)</td><td>3.44 (-13.00%)</td><td>0.41 <b>(+501.94%)</b></td><td>2732.80 (+14.94%)</td><td>2326.16 (+0.69%)</td><td>2304.70 (+0.09%)</td><td>2072.90 (-9.03%)</td><td>252.00 <b>(+535.46%)</b></td><td>1784.65 (+9.93%)</td><td>1604.38 (+0.17%)</td><td>1605.12 (-0.09%)</td><td>1353.71 (-13.00%)</td><td>162.66 <b>(+501.93%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>4.13 (n/a)</td><td>4.07 (n/a)</td><td>4.08 (n/a)</td><td>3.96 (n/a)</td><td>0.07 (n/a)</td><td>2377.60 (n/a)</td><td>2310.12 (n/a)</td><td>2302.60 (n/a)</td><td>2278.70 (n/a)</td><td>39.66 (n/a)</td><td>1623.43 (n/a)</td><td>1601.73 (n/a)</td><td>1606.61 (n/a)</td><td>1555.90 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>1.28 (-4.74%)</td><td>1.08 (+14.31%)</td><td>1.09 (+10.11%)</td><td>0.91 <b>(+33.62%)</b></td><td>0.17 <b>(-37.31%)</b></td><td>243.10 <b>(-25.15%)</b></td><td>208.08 (-16.08%)</td><td>202.20 (-9.16%)</td><td>172.70 (+4.98%)</td><td>32.37 <b>(-51.36%)</b></td><td>54.66 (-4.74%)</td><td>46.24 (+14.31%)</td><td>46.68 (+10.11%)</td><td>38.83 <b>(+33.62%)</b></td><td>7.14 <b>(-37.31%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>1.34 (n/a)</td><td>0.95 (n/a)</td><td>0.99 (n/a)</td><td>0.68 (n/a)</td><td>0.27 (n/a)</td><td>324.80 (n/a)</td><td>247.96 (n/a)</td><td>222.60 (n/a)</td><td>164.50 (n/a)</td><td>66.55 (n/a)</td><td>57.38 (n/a)</td><td>40.46 (n/a)</td><td>42.39 (n/a)</td><td>29.06 (n/a)</td><td>11.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>1.16 (-14.82%)</td><td>0.90 (-16.21%)</td><td>0.74 <b>(-38.46%)</b></td><td>0.72 (+18.47%)</td><td>0.24 (-19.45%)</td><td>308.10 (-15.59%)</td><td>259.68 (+15.84%)</td><td>300.90 <b>(+62.47%)</b></td><td>190.20 (+17.41%)</td><td>62.67 <b>(-23.70%)</b></td><td>49.62 (-14.82%)</td><td>38.30 (-16.21%)</td><td>31.36 <b>(-38.46%)</b></td><td>30.63 (+18.47%)</td><td>10.13 (-19.45%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>1.37 (n/a)</td><td>1.07 (n/a)</td><td>1.19 (n/a)</td><td>0.61 (n/a)</td><td>0.29 (n/a)</td><td>365.00 (n/a)</td><td>224.18 (n/a)</td><td>185.20 (n/a)</td><td>162.00 (n/a)</td><td>82.13 (n/a)</td><td>58.25 (n/a)</td><td>45.71 (n/a)</td><td>50.96 (n/a)</td><td>25.86 (n/a)</td><td>12.57 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.52 (+0.14%)</td><td>0.52 (-0.10%)</td><td>0.52 (-0.07%)</td><td>0.52 (-0.42%)</td><td>0.00 <b>(+626.91%)</b></td><td>48855.70 (+0.43%)</td><td>48678.68 (+0.10%)</td><td>48655.50 (+0.07%)</td><td>48546.90 (-0.14%)</td><td>122.72 <b>(+629.80%)</b></td><td>353.88 (+0.14%)</td><td>352.93 (-0.10%)</td><td>353.09 (-0.07%)</td><td>351.64 (-0.42%)</td><td>0.89 <b>(+626.93%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48648.30 (n/a)</td><td>48629.88 (n/a)</td><td>48619.90 (n/a)</td><td>48613.70 (n/a)</td><td>16.82 (n/a)</td><td>353.40 (n/a)</td><td>353.28 (n/a)</td><td>353.35 (n/a)</td><td>353.14 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.89 (+0.26%)</td><td>0.88 (+0.22%)</td><td>0.88 (+0.28%)</td><td>0.88 (+0.40%)</td><td>0.01 (-0.06%)</td><td>28688.90 (-0.40%)</td><td>28476.06 (-0.22%)</td><td>28516.40 (-0.28%)</td><td>28188.10 (-0.25%)</td><td>209.28 (-0.63%)</td><td>609.47 (+0.26%)</td><td>603.34 (+0.22%)</td><td>602.46 (+0.28%)</td><td>598.83 (+0.40%)</td><td>4.44 (-0.06%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28803.80 (n/a)</td><td>28539.90 (n/a)</td><td>28597.40 (n/a)</td><td>28260.10 (n/a)</td><td>210.60 (n/a)</td><td>607.92 (n/a)</td><td>601.99 (n/a)</td><td>600.75 (n/a)</td><td>596.44 (n/a)</td><td>4.45 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>3.25 (-2.21%)</td><td>3.16 (-1.91%)</td><td>3.15 (-1.46%)</td><td>3.10 (-0.38%)</td><td>0.06 <b>(-39.79%)</b></td><td>8125.50 (+0.38%)</td><td>7962.46 (+1.90%)</td><td>8000.50 (+1.48%)</td><td>7743.40 (+2.26%)</td><td>139.62 <b>(-38.02%)</b></td><td>2218.65 (-2.21%)</td><td>2158.14 (-1.91%)</td><td>2147.35 (-1.46%)</td><td>2114.31 (-0.38%)</td><td>38.23 <b>(-39.79%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>3.32 (n/a)</td><td>3.22 (n/a)</td><td>3.19 (n/a)</td><td>3.11 (n/a)</td><td>0.09 (n/a)</td><td>8094.50 (n/a)</td><td>7813.80 (n/a)</td><td>7883.70 (n/a)</td><td>7572.10 (n/a)</td><td>225.26 (n/a)</td><td>2268.84 (n/a)</td><td>2200.13 (n/a)</td><td>2179.17 (n/a)</td><td>2122.40 (n/a)</td><td>63.50 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>3.94 (+0.28%)</td><td>3.53 (+2.54%)</td><td>3.57 (+0.63%)</td><td>2.89 (-4.55%)</td><td>0.40 (+4.09%)</td><td>2790.00 (+4.77%)</td><td>2309.92 (-2.36%)</td><td>2256.70 (-0.63%)</td><td>2046.70 (-0.28%)</td><td>288.52 (+8.36%)</td><td>1032.84 (+0.28%)</td><td>925.60 (+2.54%)</td><td>936.73 (+0.63%)</td><td>757.68 (-4.55%)</td><td>105.05 (+4.09%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>3.93 (n/a)</td><td>3.44 (n/a)</td><td>3.55 (n/a)</td><td>3.03 (n/a)</td><td>0.38 (n/a)</td><td>2663.00 (n/a)</td><td>2365.70 (n/a)</td><td>2271.00 (n/a)</td><td>2052.50 (n/a)</td><td>266.26 (n/a)</td><td>1029.92 (n/a)</td><td>902.64 (n/a)</td><td>930.82 (n/a)</td><td>793.82 (n/a)</td><td>100.92 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.50 (-3.42%)</td><td>0.38 (-6.98%)</td><td>0.37 (+0.84%)</td><td>0.31 (-4.37%)</td><td>0.07 <b>(-22.99%)</b></td><td>4030.20 (+4.57%)</td><td>3369.80 (+5.91%)</td><td>3368.00 (-0.83%)</td><td>2493.90 (+3.54%)</td><td>561.13 (-18.38%)</td><td>26.91 (-3.42%)</td><td>20.42 (-6.98%)</td><td>19.93 (+0.84%)</td><td>16.65 (-4.37%)</td><td>3.87 <b>(-22.99%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.52 (n/a)</td><td>0.41 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>3854.10 (n/a)</td><td>3181.74 (n/a)</td><td>3396.30 (n/a)</td><td>2408.60 (n/a)</td><td>687.47 (n/a)</td><td>27.86 (n/a)</td><td>21.96 (n/a)</td><td>19.76 (n/a)</td><td>17.41 (n/a)</td><td>5.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>5.35 (-12.36%)</td><td>5.00 (+9.29%)</td><td>5.00 (+3.26%)</td><td>4.66 <b>(+40.39%)</b></td><td>0.27 <b>(-75.20%)</b></td><td>1426.90 <b>(-28.77%)</b></td><td>1333.12 (-12.55%)</td><td>1329.70 (-3.16%)</td><td>1244.30 (+14.10%)</td><td>73.43 <b>(-80.27%)</b></td><td>1651.64 (-12.36%)</td><td>1545.37 (+9.29%)</td><td>1545.60 (+3.26%)</td><td>1440.31 <b>(+40.39%)</b></td><td>84.96 <b>(-75.20%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>6.10 (n/a)</td><td>4.58 (n/a)</td><td>4.84 (n/a)</td><td>3.32 (n/a)</td><td>1.11 (n/a)</td><td>2003.30 (n/a)</td><td>1524.52 (n/a)</td><td>1373.10 (n/a)</td><td>1090.50 (n/a)</td><td>372.16 (n/a)</td><td>1884.65 (n/a)</td><td>1414.00 (n/a)</td><td>1496.77 (n/a)</td><td>1025.91 (n/a)</td><td>342.56 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.21 (-8.31%)</td><td>0.18 (-13.12%)</td><td>0.17 (-12.79%)</td><td>0.15 <b>(-21.69%)</b></td><td>0.02 <b>(+44.32%)</b></td><td>0.21 (-8.31%)</td><td>0.18 (-13.12%)</td><td>0.17 (-12.79%)</td><td>0.15 <b>(-21.69%)</b></td><td>0.02 <b>(+44.32%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>13.32 (+0.02%)</td><td>11.83 (-7.44%)</td><td>11.91 (-10.14%)</td><td>10.16 (-6.52%)</td><td>1.13 (+5.35%)</td><td>13.31 (+0.02%)</td><td>11.83 (-7.44%)</td><td>11.90 (-10.14%)</td><td>10.15 (-6.52%)</td><td>1.13 (+5.35%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>13.32 (n/a)</td><td>12.79 (n/a)</td><td>13.26 (n/a)</td><td>10.86 (n/a)</td><td>1.08 (n/a)</td><td>13.31 (n/a)</td><td>12.78 (n/a)</td><td>13.25 (n/a)</td><td>10.86 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>25.05 (-1.17%)</td><td>22.59 (-8.45%)</td><td>23.18 (-5.53%)</td><td>17.69 <b>(-26.98%)</b></td><td>2.85 <b>(+483.62%)</b></td><td>25.04 (-1.17%)</td><td>22.58 (-8.45%)</td><td>23.16 (-5.53%)</td><td>17.68 <b>(-26.98%)</b></td><td>2.85 <b>(+483.63%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>25.35 (n/a)</td><td>24.68 (n/a)</td><td>24.54 (n/a)</td><td>24.22 (n/a)</td><td>0.49 (n/a)</td><td>25.33 (n/a)</td><td>24.66 (n/a)</td><td>24.52 (n/a)</td><td>24.20 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>43.12 (-2.98%)</td><td>39.72 (-3.12%)</td><td>39.45 (-4.41%)</td><td>37.76 (+2.12%)</td><td>2.12 <b>(-23.48%)</b></td><td>43.09 (-2.98%)</td><td>39.70 (-3.12%)</td><td>39.42 (-4.41%)</td><td>37.74 (+2.12%)</td><td>2.12 <b>(-23.48%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>44.44 (n/a)</td><td>41.00 (n/a)</td><td>41.27 (n/a)</td><td>36.98 (n/a)</td><td>2.77 (n/a)</td><td>44.42 (n/a)</td><td>40.98 (n/a)</td><td>41.24 (n/a)</td><td>36.96 (n/a)</td><td>2.77 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>44.94 (-1.38%)</td><td>42.82 (-1.55%)</td><td>42.88 (+0.01%)</td><td>41.09 (-3.71%)</td><td>1.61 <b>(+31.07%)</b></td><td>44.91 (-1.38%)</td><td>42.79 (-1.55%)</td><td>42.85 (+0.01%)</td><td>41.06 (-3.71%)</td><td>1.61 <b>(+31.07%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>45.57 (n/a)</td><td>43.49 (n/a)</td><td>42.87 (n/a)</td><td>42.67 (n/a)</td><td>1.23 (n/a)</td><td>45.54 (n/a)</td><td>43.46 (n/a)</td><td>42.85 (n/a)</td><td>42.64 (n/a)</td><td>1.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>13.48 (+1.37%)</td><td>12.77 (+0.36%)</td><td>12.90 (-2.44%)</td><td>11.38 (-4.18%)</td><td>0.85 (+18.88%)</td><td>13.47 (+1.37%)</td><td>12.76 (+0.36%)</td><td>12.89 (-2.44%)</td><td>11.37 (-4.18%)</td><td>0.85 (+18.88%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>13.30 (n/a)</td><td>12.73 (n/a)</td><td>13.22 (n/a)</td><td>11.88 (n/a)</td><td>0.72 (n/a)</td><td>13.29 (n/a)</td><td>12.72 (n/a)</td><td>13.21 (n/a)</td><td>11.87 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>24.98 (-0.78%)</td><td>23.86 (-3.67%)</td><td>24.37 (-1.63%)</td><td>21.12 (-12.78%)</td><td>1.58 <b>(+315.71%)</b></td><td>24.96 (-0.78%)</td><td>23.85 (-3.67%)</td><td>24.35 (-1.63%)</td><td>21.10 (-12.78%)</td><td>1.58 <b>(+315.71%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>25.17 (n/a)</td><td>24.77 (n/a)</td><td>24.77 (n/a)</td><td>24.21 (n/a)</td><td>0.38 (n/a)</td><td>25.16 (n/a)</td><td>24.75 (n/a)</td><td>24.76 (n/a)</td><td>24.20 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>40.42 (-2.34%)</td><td>39.07 (-2.02%)</td><td>39.01 (-2.02%)</td><td>36.80 (-3.72%)</td><td>1.48 (+7.23%)</td><td>40.40 (-2.34%)</td><td>39.05 (-2.02%)</td><td>38.99 (-2.02%)</td><td>36.78 (-3.72%)</td><td>1.48 (+7.23%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>41.39 (n/a)</td><td>39.88 (n/a)</td><td>39.82 (n/a)</td><td>38.22 (n/a)</td><td>1.38 (n/a)</td><td>41.36 (n/a)</td><td>39.85 (n/a)</td><td>39.79 (n/a)</td><td>38.20 (n/a)</td><td>1.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>45.01 (+5.55%)</td><td>43.29 (+2.53%)</td><td>43.82 (+3.37%)</td><td>41.41 (-0.05%)</td><td>1.44 <b>(+208.16%)</b></td><td>44.98 (+5.55%)</td><td>43.26 (+2.53%)</td><td>43.80 (+3.37%)</td><td>41.38 (-0.05%)</td><td>1.44 <b>(+208.16%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>42.64 (n/a)</td><td>42.22 (n/a)</td><td>42.39 (n/a)</td><td>41.43 (n/a)</td><td>0.47 (n/a)</td><td>42.62 (n/a)</td><td>42.19 (n/a)</td><td>42.37 (n/a)</td><td>41.41 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>183.70 (n/a)</td><td>173.24 (n/a)</td><td>174.60 (n/a)</td><td>164.80 (n/a)</td><td>7.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>158.74 (n/a)</td><td>146.90 (n/a)</td><td>129.00 (n/a)</td><td>30.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>172.70 (n/a)</td><td>174.10 (n/a)</td><td>119.90 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>175.56 (n/a)</td><td>168.20 (n/a)</td><td>156.50 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>164.82 (n/a)</td><td>160.60 (n/a)</td><td>132.20 (n/a)</td><td>26.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>317.00 (n/a)</td><td>217.32 (n/a)</td><td>204.60 (n/a)</td><td>169.10 (n/a)</td><td>57.63 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>304.70 (n/a)</td><td>208.42 (n/a)</td><td>200.20 (n/a)</td><td>152.70 (n/a)</td><td>57.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>275.10 (n/a)</td><td>236.76 (n/a)</td><td>233.30 (n/a)</td><td>199.80 (n/a)</td><td>37.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (-1.65%)</td><td>0.04 (+3.92%)</td><td>0.04 (-3.30%)</td><td>0.04 <b>(+66.74%)</b></td><td>0.01 <b>(-34.34%)</b></td><td>230.70 <b>(-40.02%)</b></td><td>191.76 (-11.45%)</td><td>195.30 (+3.39%)</td><td>146.00 (+1.74%)</td><td>35.73 <b>(-62.79%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>384.60 (n/a)</td><td>216.56 (n/a)</td><td>188.90 (n/a)</td><td>143.50 (n/a)</td><td>96.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (+14.58%)</td><td>0.05 (+4.71%)</td><td>0.05 (+1.93%)</td><td>0.04 (+4.84%)</td><td>0.01 <b>(+53.08%)</b></td><td>195.60 (-4.59%)</td><td>164.92 (-3.07%)</td><td>168.40 (-1.92%)</td><td>125.20 (-12.75%)</td><td>30.93 <b>(+30.24%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>170.14 (n/a)</td><td>171.70 (n/a)</td><td>143.50 (n/a)</td><td>23.75 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 <b>(-26.65%)</b></td><td>0.05 (+1.73%)</td><td>0.05 (+10.37%)</td><td>0.04 <b>(+20.61%)</b></td><td>0.00 <b>(-80.84%)</b></td><td>187.20 (-17.09%)</td><td>171.00 (-6.61%)</td><td>166.80 (-9.40%)</td><td>163.80 <b>(+36.27%)</b></td><td>9.43 <b>(-78.46%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.80 (n/a)</td><td>183.10 (n/a)</td><td>184.10 (n/a)</td><td>120.20 (n/a)</td><td>43.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (-11.59%)</td><td>0.05 (-5.23%)</td><td>0.04 (-9.69%)</td><td>0.04 <b>(+26.71%)</b></td><td>0.01 <b>(-48.55%)</b></td><td>193.50 <b>(-21.08%)</b></td><td>179.66 (+2.13%)</td><td>186.30 (+10.76%)</td><td>146.90 (+13.09%)</td><td>18.78 <b>(-56.08%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.20 (n/a)</td><td>175.92 (n/a)</td><td>168.20 (n/a)</td><td>129.90 (n/a)</td><td>42.76 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (-16.75%)</td><td>0.05 (-10.30%)</td><td>0.05 (-9.29%)</td><td>0.04 (-9.30%)</td><td>0.00 <b>(-29.89%)</b></td><td>195.80 (+10.25%)</td><td>177.38 (+11.03%)</td><td>177.20 (+10.20%)</td><td>157.50 <b>(+20.14%)</b></td><td>17.44 (-6.47%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.60 (n/a)</td><td>159.76 (n/a)</td><td>160.80 (n/a)</td><td>131.10 (n/a)</td><td>18.65 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (-9.99%)</td><td>0.04 (-8.43%)</td><td>0.04 (-8.28%)</td><td>0.04 (-2.67%)</td><td>0.00 <b>(-29.45%)</b></td><td>219.60 (+2.76%)</td><td>186.82 (+8.38%)</td><td>187.60 (+9.01%)</td><td>164.20 (+11.10%)</td><td>21.67 (-18.63%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>172.38 (n/a)</td><td>172.10 (n/a)</td><td>147.80 (n/a)</td><td>26.63 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (+8.92%)</td><td>0.05 (+13.96%)</td><td>0.05 (+13.54%)</td><td>0.04 (+10.05%)</td><td>0.01 (+19.46%)</td><td>192.20 (-9.13%)</td><td>158.12 (-12.02%)</td><td>161.10 (-11.92%)</td><td>134.90 (-8.17%)</td><td>23.38 (-1.26%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>179.72 (n/a)</td><td>182.90 (n/a)</td><td>146.90 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (-4.08%)</td><td>0.04 (-6.97%)</td><td>0.04 (-5.36%)</td><td>0.04 (-13.27%)</td><td>0.00 <b>(+44.03%)</b></td><td>228.50 (+15.29%)</td><td>202.64 (+8.16%)</td><td>201.20 (+5.67%)</td><td>173.10 (+4.21%)</td><td>23.17 <b>(+74.86%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>198.20 (n/a)</td><td>187.36 (n/a)</td><td>190.40 (n/a)</td><td>166.10 (n/a)</td><td>13.25 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (-10.03%)</td><td>0.05 (+5.70%)</td><td>0.05 (+9.39%)</td><td>0.04 (+11.61%)</td><td>0.01 <b>(-32.70%)</b></td><td>222.70 (-10.38%)</td><td>176.30 (-8.64%)</td><td>177.10 (-8.62%)</td><td>128.10 (+11.20%)</td><td>34.15 <b>(-30.37%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.50 (n/a)</td><td>192.98 (n/a)</td><td>193.80 (n/a)</td><td>115.20 (n/a)</td><td>49.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (-2.68%)</td><td>0.04 (-0.83%)</td><td>0.04 (-3.69%)</td><td>0.04 (+9.34%)</td><td>0.01 (-11.84%)</td><td>231.20 (-8.54%)</td><td>206.74 (+0.37%)</td><td>214.20 (+3.83%)</td><td>173.90 (+2.72%)</td><td>26.03 (-16.78%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.80 (n/a)</td><td>205.98 (n/a)</td><td>206.30 (n/a)</td><td>169.30 (n/a)</td><td>31.27 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (-2.75%)</td><td>0.05 (-1.23%)</td><td>0.05 (-4.46%)</td><td>0.04 (-0.82%)</td><td>0.01 (-9.70%)</td><td>210.70 (+0.81%)</td><td>165.98 (+0.79%)</td><td>167.40 (+4.69%)</td><td>130.00 (+2.77%)</td><td>29.43 (-6.08%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.00 (n/a)</td><td>164.68 (n/a)</td><td>159.90 (n/a)</td><td>126.50 (n/a)</td><td>31.33 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 <b>(+22.80%)</b></td><td>0.04 (-0.99%)</td><td>0.04 (+4.69%)</td><td>0.03 <b>(-34.86%)</b></td><td>0.01 <b>(+384.01%)</b></td><td>313.90 <b>(+53.50%)</b></td><td>212.04 (+10.07%)</td><td>186.40 (-4.46%)</td><td>141.20 (-18.57%)</td><td>72.76 <b>(+515.26%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.50 (n/a)</td><td>192.64 (n/a)</td><td>195.10 (n/a)</td><td>173.40 (n/a)</td><td>11.83 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (+8.62%)</td><td>0.05 (-4.48%)</td><td>0.05 (-3.87%)</td><td>0.04 (-13.78%)</td><td>0.01 <b>(+59.20%)</b></td><td>230.00 (+15.99%)</td><td>180.26 (+7.48%)</td><td>170.50 (+4.03%)</td><td>127.10 (-7.90%)</td><td>40.03 <b>(+69.79%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.30 (n/a)</td><td>167.72 (n/a)</td><td>163.90 (n/a)</td><td>138.00 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (-4.89%)</td><td>0.05 (-9.66%)</td><td>0.05 (-5.75%)</td><td>0.03 <b>(-33.67%)</b></td><td>0.01 <b>(+31.42%)</b></td><td>268.70 <b>(+50.79%)</b></td><td>183.60 (+15.08%)</td><td>178.20 (+6.07%)</td><td>123.50 (+5.11%)</td><td>52.89 <b>(+119.62%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.20 (n/a)</td><td>159.54 (n/a)</td><td>168.00 (n/a)</td><td>117.50 (n/a)</td><td>24.08 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (+3.57%)</td><td>0.05 (+10.48%)</td><td>0.05 (+6.22%)</td><td>0.05 <b>(+113.12%)</b></td><td>0.01 <b>(-60.91%)</b></td><td>181.90 <b>(-53.07%)</b></td><td>158.00 <b>(-20.81%)</b></td><td>152.40 (-5.81%)</td><td>135.70 (-3.49%)</td><td>18.03 <b>(-82.94%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>387.60 (n/a)</td><td>199.52 (n/a)</td><td>161.80 (n/a)</td><td>140.60 (n/a)</td><td>105.69 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (+5.44%)</td><td>0.05 (-6.65%)</td><td>0.05 (-0.83%)</td><td>0.03 <b>(-30.51%)</b></td><td>0.01 <b>(+125.77%)</b></td><td>235.30 <b>(+43.91%)</b></td><td>170.32 (+11.42%)</td><td>161.50 (+0.87%)</td><td>124.10 (-5.12%)</td><td>42.18 <b>(+213.81%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>163.50 (n/a)</td><td>152.86 (n/a)</td><td>160.10 (n/a)</td><td>130.80 (n/a)</td><td>13.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (-13.52%)</td><td>0.05 (-2.07%)</td><td>0.05 (+4.22%)</td><td>0.04 (+12.65%)</td><td>0.00 <b>(-57.35%)</b></td><td>192.30 (-11.22%)</td><td>175.04 (-0.43%)</td><td>170.00 (-4.06%)</td><td>156.40 (+15.68%)</td><td>15.19 <b>(-55.60%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>175.80 (n/a)</td><td>177.20 (n/a)</td><td>135.20 (n/a)</td><td>34.20 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (-11.04%)</td><td>0.04 (-2.33%)</td><td>0.05 (+10.26%)</td><td>0.03 (-14.52%)</td><td>0.01 (-9.22%)</td><td>326.10 (+16.97%)</td><td>199.28 (+3.46%)</td><td>170.30 (-9.32%)</td><td>151.50 (+12.39%)</td><td>71.76 <b>(+27.00%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>278.80 (n/a)</td><td>192.62 (n/a)</td><td>187.80 (n/a)</td><td>134.80 (n/a)</td><td>56.50 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.21 (+0.21%)</td><td>0.21 (+0.15%)</td><td>0.21 (+0.30%)</td><td>0.20 (-0.21%)</td><td>0.00 <b>(+162.02%)</b></td><td>41048.30 (+0.21%)</td><td>40864.76 (-0.15%)</td><td>40818.90 (-0.30%)</td><td>40772.70 (-0.21%)</td><td>109.15 <b>(+161.97%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40961.20 (n/a)</td><td>40924.92 (n/a)</td><td>40941.50 (n/a)</td><td>40859.60 (n/a)</td><td>41.66 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (-19.86%)</td><td>0.04 (-3.86%)</td><td>0.04 (-1.17%)</td><td>0.04 (+2.69%)</td><td>0.01 <b>(-44.21%)</b></td><td>215.20 (-2.58%)</td><td>185.88 (+1.61%)</td><td>193.80 (+1.20%)</td><td>156.90 <b>(+24.72%)</b></td><td>25.15 <b>(-31.41%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.90 (n/a)</td><td>182.94 (n/a)</td><td>191.50 (n/a)</td><td>125.80 (n/a)</td><td>36.66 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.10 (+12.00%)</td><td>0.08 (+8.11%)</td><td>0.08 (+9.86%)</td><td>0.07 (+16.52%)</td><td>0.01 (+11.05%)</td><td>182.50 (-14.16%)</td><td>160.84 (-7.63%)</td><td>160.90 (-8.99%)</td><td>125.20 (-10.76%)</td><td>21.99 (-16.52%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>174.12 (n/a)</td><td>176.80 (n/a)</td><td>140.30 (n/a)</td><td>26.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (-6.78%)</td><td>0.05 (-1.21%)</td><td>0.05 (+3.84%)</td><td>0.04 (+16.24%)</td><td>0.01 <b>(-35.81%)</b></td><td>193.50 (-13.96%)</td><td>170.80 (-1.81%)</td><td>181.40 (-3.66%)</td><td>134.70 (+7.25%)</td><td>26.54 <b>(-37.78%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>173.94 (n/a)</td><td>188.30 (n/a)</td><td>125.60 (n/a)</td><td>42.65 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.09 <b>(+55.66%)</b></td><td>0.07 <b>(+30.57%)</b></td><td>0.06 (+19.69%)</td><td>0.06 <b>(+35.90%)</b></td><td>0.01 <b>(+115.38%)</b></td><td>178.60 <b>(-26.41%)</b></td><td>160.22 <b>(-22.37%)</b></td><td>170.30 (-16.48%)</td><td>116.20 <b>(-35.77%)</b></td><td>25.62 (+0.83%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>242.70 (n/a)</td><td>206.40 (n/a)</td><td>203.90 (n/a)</td><td>180.90 (n/a)</td><td>25.41 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (+2.17%)</td><td>0.05 (-10.07%)</td><td>0.04 (-12.84%)</td><td>0.04 (-13.44%)</td><td>0.01 <b>(+30.43%)</b></td><td>215.40 (+15.50%)</td><td>177.66 (+13.90%)</td><td>185.10 (+14.76%)</td><td>111.40 (-2.11%)</td><td>39.31 <b>(+42.61%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.50 (n/a)</td><td>155.98 (n/a)</td><td>161.30 (n/a)</td><td>113.80 (n/a)</td><td>27.57 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.10 <b>(+47.22%)</b></td><td>0.07 (+18.93%)</td><td>0.06 (-5.14%)</td><td>0.06 <b>(+99.21%)</b></td><td>0.02 (+5.22%)</td><td>178.90 <b>(-49.80%)</b></td><td>153.64 <b>(-21.60%)</b></td><td>165.80 (+5.47%)</td><td>102.30 <b>(-32.03%)</b></td><td>30.06 <b>(-66.52%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>356.40 (n/a)</td><td>195.96 (n/a)</td><td>157.20 (n/a)</td><td>150.50 (n/a)</td><td>89.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (+19.15%)</td><td>0.05 (+7.05%)</td><td>0.04 (-3.91%)</td><td>0.03 (-6.88%)</td><td>0.02 <b>(+87.83%)</b></td><td>235.50 (+7.39%)</td><td>175.98 (-1.17%)</td><td>185.10 (+4.11%)</td><td>113.70 (-16.03%)</td><td>53.96 <b>(+68.82%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.30 (n/a)</td><td>178.06 (n/a)</td><td>177.80 (n/a)</td><td>135.40 (n/a)</td><td>31.96 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (-12.68%)</td><td>0.05 (-8.51%)</td><td>0.05 (-2.93%)</td><td>0.04 (-3.02%)</td><td>0.01 <b>(-21.62%)</b></td><td>236.50 (+3.14%)</td><td>197.40 (+8.27%)</td><td>192.20 (+3.06%)</td><td>144.40 (+14.51%)</td><td>35.51 (-5.00%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>182.32 (n/a)</td><td>186.50 (n/a)</td><td>126.10 (n/a)</td><td>37.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (-12.34%)</td><td>0.04 (-7.32%)</td><td>0.04 (-0.52%)</td><td>0.03 (-5.48%)</td><td>0.01 <b>(-23.50%)</b></td><td>237.50 (+5.79%)</td><td>204.04 (+6.76%)</td><td>204.50 (+0.49%)</td><td>150.20 (+14.13%)</td><td>34.87 (-7.02%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.50 (n/a)</td><td>191.12 (n/a)</td><td>203.50 (n/a)</td><td>131.60 (n/a)</td><td>37.51 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (-17.82%)</td><td>0.05 (-13.24%)</td><td>0.04 (-14.33%)</td><td>0.04 (-5.09%)</td><td>0.00 <b>(-46.76%)</b></td><td>219.20 (+5.38%)</td><td>204.50 (+14.12%)</td><td>208.70 (+16.72%)</td><td>177.40 <b>(+21.67%)</b></td><td>16.58 <b>(-32.33%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>179.20 (n/a)</td><td>178.80 (n/a)</td><td>145.80 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 <b>(-22.21%)</b></td><td>0.04 (-14.56%)</td><td>0.04 (-13.46%)</td><td>0.03 (-2.61%)</td><td>0.00 <b>(-55.94%)</b></td><td>239.50 (+2.70%)</td><td>220.54 (+15.28%)</td><td>219.00 (+15.51%)</td><td>200.50 <b>(+28.61%)</b></td><td>18.13 <b>(-41.18%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.20 (n/a)</td><td>191.30 (n/a)</td><td>189.60 (n/a)</td><td>155.90 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (+11.33%)</td><td>0.04 (-1.87%)</td><td>0.04 (-3.32%)</td><td>0.03 <b>(-27.30%)</b></td><td>0.01 <b>(+241.43%)</b></td><td>304.80 <b>(+37.55%)</b></td><td>216.22 (+6.05%)</td><td>210.00 (+3.45%)</td><td>170.60 (-10.16%)</td><td>53.86 <b>(+323.46%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>221.60 (n/a)</td><td>203.88 (n/a)</td><td>203.00 (n/a)</td><td>189.90 (n/a)</td><td>12.72 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (-6.80%)</td><td>0.04 (-10.61%)</td><td>0.04 (-11.03%)</td><td>0.03 (-16.18%)</td><td>0.00 <b>(+86.90%)</b></td><td>237.20 (+19.26%)</td><td>211.90 (+12.87%)</td><td>211.70 (+12.43%)</td><td>184.70 (+7.32%)</td><td>25.15 <b>(+141.01%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>198.90 (n/a)</td><td>187.74 (n/a)</td><td>188.30 (n/a)</td><td>172.10 (n/a)</td><td>10.43 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 <b>(-21.26%)</b></td><td>0.04 (-16.86%)</td><td>0.04 <b>(-20.27%)</b></td><td>0.03 (-11.50%)</td><td>0.00 <b>(-52.87%)</b></td><td>252.80 (+12.96%)</td><td>224.00 (+19.14%)</td><td>219.80 <b>(+25.39%)</b></td><td>209.10 <b>(+26.96%)</b></td><td>17.23 <b>(-31.82%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.80 (n/a)</td><td>188.02 (n/a)</td><td>175.30 (n/a)</td><td>164.70 (n/a)</td><td>25.27 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (-4.22%)</td><td>0.04 (-1.57%)</td><td>0.04 (-1.38%)</td><td>0.04 (+8.33%)</td><td>0.00 <b>(-28.97%)</b></td><td>228.90 (-7.70%)</td><td>202.90 (+0.74%)</td><td>206.50 (+1.42%)</td><td>179.40 (+4.36%)</td><td>20.20 <b>(-32.17%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.00 (n/a)</td><td>201.40 (n/a)</td><td>203.60 (n/a)</td><td>171.90 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.58 <b>(-20.91%)</b></td><td>0.48 <b>(-25.75%)</b></td><td>0.47 <b>(-29.89%)</b></td><td>0.39 <b>(-29.37%)</b></td><td>0.08 (-6.51%)</td><td>253.10 <b>(+41.63%)</b></td><td>211.34 <b>(+35.65%)</b></td><td>209.00 <b>(+42.56%)</b></td><td>170.60 <b>(+26.37%)</b></td><td>34.47 <b>(+64.54%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.73 (n/a)</td><td>0.64 (n/a)</td><td>0.67 (n/a)</td><td>0.55 (n/a)</td><td>0.08 (n/a)</td><td>178.70 (n/a)</td><td>155.80 (n/a)</td><td>146.60 (n/a)</td><td>135.00 (n/a)</td><td>20.95 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.75 (+14.19%)</td><td>0.60 (+1.64%)</td><td>0.55 (-5.83%)</td><td>0.53 (+6.16%)</td><td>0.09 <b>(+38.89%)</b></td><td>184.60 (-5.77%)</td><td>166.62 (-0.99%)</td><td>179.60 (+6.15%)</td><td>131.30 (-12.47%)</td><td>22.70 (+17.57%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.66 (n/a)</td><td>0.59 (n/a)</td><td>0.58 (n/a)</td><td>0.50 (n/a)</td><td>0.07 (n/a)</td><td>195.90 (n/a)</td><td>168.28 (n/a)</td><td>169.20 (n/a)</td><td>150.00 (n/a)</td><td>19.31 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.68 (-10.50%)</td><td>0.61 (+1.69%)</td><td>0.63 (+13.16%)</td><td>0.54 (+7.16%)</td><td>0.06 <b>(-42.45%)</b></td><td>180.60 (-6.71%)</td><td>162.34 (-2.88%)</td><td>156.00 (-11.61%)</td><td>145.40 (+11.67%)</td><td>15.18 <b>(-38.34%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.76 (n/a)</td><td>0.60 (n/a)</td><td>0.56 (n/a)</td><td>0.51 (n/a)</td><td>0.10 (n/a)</td><td>193.60 (n/a)</td><td>167.16 (n/a)</td><td>176.50 (n/a)</td><td>130.20 (n/a)</td><td>24.62 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.65 (+5.25%)</td><td>0.51 (-4.27%)</td><td>0.48 (-8.11%)</td><td>0.46 (-4.39%)</td><td>0.08 <b>(+44.97%)</b></td><td>213.60 (+4.60%)</td><td>196.86 (+5.32%)</td><td>206.20 (+8.81%)</td><td>151.80 (-5.01%)</td><td>25.42 <b>(+41.10%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.62 (n/a)</td><td>0.53 (n/a)</td><td>0.52 (n/a)</td><td>0.48 (n/a)</td><td>0.05 (n/a)</td><td>204.20 (n/a)</td><td>186.92 (n/a)</td><td>189.50 (n/a)</td><td>159.80 (n/a)</td><td>18.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.54 (+12.88%)</td><td>0.48 (+16.27%)</td><td>0.48 (+16.94%)</td><td>0.43 (+16.82%)</td><td>0.05 (+18.14%)</td><td>171.90 (-14.39%)</td><td>154.58 (-13.94%)</td><td>152.90 (-14.49%)</td><td>136.80 (-11.40%)</td><td>15.59 (-8.76%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.37 (n/a)</td><td>0.04 (n/a)</td><td>200.80 (n/a)</td><td>179.62 (n/a)</td><td>178.80 (n/a)</td><td>154.40 (n/a)</td><td>17.09 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.49 (-5.74%)</td><td>0.40 (-14.19%)</td><td>0.39 (-13.42%)</td><td>0.34 <b>(-21.40%)</b></td><td>0.05 <b>(+72.94%)</b></td><td>213.70 <b>(+27.20%)</b></td><td>188.94 (+17.75%)</td><td>189.40 (+15.49%)</td><td>151.70 (+6.08%)</td><td>23.68 <b>(+130.78%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.52 (n/a)</td><td>0.46 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>0.03 (n/a)</td><td>168.00 (n/a)</td><td>160.46 (n/a)</td><td>164.00 (n/a)</td><td>143.00 (n/a)</td><td>10.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.56 (+2.64%)</td><td>0.45 (+0.73%)</td><td>0.48 (+9.80%)</td><td>0.29 (-17.68%)</td><td>0.11 <b>(+56.08%)</b></td><td>258.40 <b>(+21.49%)</b></td><td>174.66 (+3.25%)</td><td>152.40 (-8.91%)</td><td>130.90 (-2.60%)</td><td>52.15 <b>(+84.43%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.55 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.07 (n/a)</td><td>212.70 (n/a)</td><td>169.16 (n/a)</td><td>167.30 (n/a)</td><td>134.40 (n/a)</td><td>28.28 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.59 (+11.42%)</td><td>0.43 (+5.67%)</td><td>0.41 (+1.59%)</td><td>0.35 (+4.94%)</td><td>0.10 <b>(+31.32%)</b></td><td>210.10 (-4.72%)</td><td>176.72 (-4.26%)</td><td>178.20 (-1.55%)</td><td>125.80 (-10.27%)</td><td>34.68 (+14.99%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>220.50 (n/a)</td><td>184.58 (n/a)</td><td>181.00 (n/a)</td><td>140.20 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.99 (+18.55%)</td><td>0.75 (+0.18%)</td><td>0.71 (-5.10%)</td><td>0.60 (-4.16%)</td><td>0.15 <b>(+86.79%)</b></td><td>217.80 (+4.36%)</td><td>180.66 (+1.78%)</td><td>184.60 (+5.37%)</td><td>131.80 (-15.62%)</td><td>32.56 <b>(+60.17%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.84 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.63 (n/a)</td><td>0.08 (n/a)</td><td>208.70 (n/a)</td><td>177.50 (n/a)</td><td>175.20 (n/a)</td><td>156.20 (n/a)</td><td>20.33 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.90 (-4.84%)</td><td>0.73 (-1.04%)</td><td>0.74 (+5.03%)</td><td>0.60 (+9.10%)</td><td>0.12 <b>(-28.79%)</b></td><td>219.20 (-8.36%)</td><td>183.74 (-1.07%)</td><td>177.10 (-4.78%)</td><td>145.60 (+5.05%)</td><td>29.80 <b>(-29.77%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.95 (n/a)</td><td>0.74 (n/a)</td><td>0.70 (n/a)</td><td>0.55 (n/a)</td><td>0.17 (n/a)</td><td>239.20 (n/a)</td><td>185.72 (n/a)</td><td>186.00 (n/a)</td><td>138.60 (n/a)</td><td>42.43 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.79 (+6.65%)</td><td>0.67 (+4.84%)</td><td>0.61 (-0.94%)</td><td>0.57 (+13.01%)</td><td>0.11 (+11.01%)</td><td>231.90 (-11.49%)</td><td>200.90 (-4.57%)</td><td>216.40 (+0.98%)</td><td>166.00 (-6.21%)</td><td>30.36 (-9.19%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.74 (n/a)</td><td>0.63 (n/a)</td><td>0.61 (n/a)</td><td>0.50 (n/a)</td><td>0.09 (n/a)</td><td>262.00 (n/a)</td><td>210.52 (n/a)</td><td>214.30 (n/a)</td><td>177.00 (n/a)</td><td>33.43 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.00 (+2.33%)</td><td>0.00 (+2.86%)</td><td>0.00 (+0.00%)</td><td>0.00 (+13.16%)</td><td>0.00 <b>(-80.00%)</b></td><td>957.84 (-11.23%)</td><td>945.73 (-3.37%)</td><td>942.84 (-1.04%)</td><td>941.27 (-0.96%)</td><td>6.92 <b>(-87.70%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1079.03 (n/a)</td><td>978.73 (n/a)</td><td>952.71 (n/a)</td><td>950.43 (n/a)</td><td>56.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.01 (+2.44%)</td><td>0.01 (+1.25%)</td><td>0.01 (+1.23%)</td><td>0.01 (-1.30%)</td><td>0.00 <b>(+39.91%)</b></td><td>1073.53 (+0.95%)</td><td>1016.68 (-0.86%)</td><td>1004.39 (-0.86%)</td><td>976.21 (-2.12%)</td><td>36.26 <b>(+33.17%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1063.48 (n/a)</td><td>1025.53 (n/a)</td><td>1013.10 (n/a)</td><td>997.32 (n/a)</td><td>27.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.96 (+0.67%)</td><td>0.94 (-0.68%)</td><td>0.95 (-0.58%)</td><td>0.92 (-2.53%)</td><td>0.01 <b>(+455.08%)</b></td><td>2274.04 (+2.59%)</td><td>2222.86 (+0.70%)</td><td>2218.69 (+0.58%)</td><td>2188.25 (-0.66%)</td><td>32.01 <b>(+467.36%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.00 (n/a)</td><td>2216.53 (n/a)</td><td>2207.36 (n/a)</td><td>2205.81 (n/a)</td><td>2202.82 (n/a)</td><td>5.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>3.34 (+9.18%)</td><td>3.08 (+11.07%)</td><td>3.26 <b>(+22.75%)</b></td><td>2.52 (-2.26%)</td><td>0.34 <b>(+57.47%)</b></td><td>207.90 (+2.31%)</td><td>172.12 (-9.40%)</td><td>161.00 (-18.56%)</td><td>156.90 (-8.41%)</td><td>21.40 <b>(+47.75%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>3.06 (n/a)</td><td>2.77 (n/a)</td><td>2.65 (n/a)</td><td>2.58 (n/a)</td><td>0.22 (n/a)</td><td>203.20 (n/a)</td><td>189.98 (n/a)</td><td>197.70 (n/a)</td><td>171.30 (n/a)</td><td>14.48 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>5.97 (-4.30%)</td><td>5.32 (+18.02%)</td><td>5.51 <b>(+28.18%)</b></td><td>4.73 <b>(+30.16%)</b></td><td>0.56 <b>(-45.08%)</b></td><td>221.90 <b>(-23.16%)</b></td><td>198.90 (-17.35%)</td><td>190.10 <b>(-21.99%)</b></td><td>175.70 (+4.52%)</td><td>21.12 <b>(-53.08%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>6.24 (n/a)</td><td>4.51 (n/a)</td><td>4.30 (n/a)</td><td>3.63 (n/a)</td><td>1.01 (n/a)</td><td>288.80 (n/a)</td><td>240.64 (n/a)</td><td>243.70 (n/a)</td><td>168.10 (n/a)</td><td>45.00 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>3.73 <b>(+23.90%)</b></td><td>3.26 <b>(+27.93%)</b></td><td>3.33 <b>(+34.88%)</b></td><td>2.81 <b>(+25.21%)</b></td><td>0.41 <b>(+38.93%)</b></td><td>186.70 <b>(-20.15%)</b></td><td>163.10 <b>(-21.60%)</b></td><td>157.20 <b>(-25.88%)</b></td><td>140.40 (-19.26%)</td><td>20.81 (-7.93%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>3.01 (n/a)</td><td>2.55 (n/a)</td><td>2.47 (n/a)</td><td>2.24 (n/a)</td><td>0.29 (n/a)</td><td>233.80 (n/a)</td><td>208.04 (n/a)</td><td>212.10 (n/a)</td><td>173.90 (n/a)</td><td>22.60 (n/a)</td>
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
