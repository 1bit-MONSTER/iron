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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.08 <b>(-38.12%)</b></td><td>0.07 <b>(-23.21%)</b></td><td>0.06 (-19.19%)</td><td>0.05 (-14.86%)</td><td>0.01 <b>(-59.23%)</b></td><td>225.10 (+17.42%)</td><td>185.76 <b>(+25.94%)</b></td><td>191.40 <b>(+23.80%)</b></td><td>155.90 <b>(+61.55%)</b></td><td>27.44 <b>(-20.16%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>191.70 (n/a)</td><td>147.50 (n/a)</td><td>154.60 (n/a)</td><td>96.50 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.09 (-16.34%)</td><td>0.06 <b>(-23.69%)</b></td><td>0.06 <b>(-32.59%)</b></td><td>0.05 (+9.74%)</td><td>0.02 <b>(-34.22%)</b></td><td>236.80 (-8.89%)</td><td>201.66 <b>(+25.24%)</b></td><td>202.10 <b>(+48.38%)</b></td><td>136.10 (+19.60%)</td><td>40.91 <b>(-30.80%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>259.90 (n/a)</td><td>161.02 (n/a)</td><td>136.20 (n/a)</td><td>113.80 (n/a)</td><td>59.11 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.10 (+1.95%)</td><td>0.06 <b>(-23.87%)</b></td><td>0.05 <b>(-34.41%)</b></td><td>0.04 (-7.99%)</td><td>0.02 (+7.62%)</td><td>344.90 (+8.70%)</td><td>235.42 <b>(+31.80%)</b></td><td>234.60 <b>(+52.44%)</b></td><td>122.90 (-1.92%)</td><td>78.64 (+0.06%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>317.30 (n/a)</td><td>178.62 (n/a)</td><td>153.90 (n/a)</td><td>125.30 (n/a)</td><td>78.60 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 <b>(-40.16%)</b></td><td>0.05 <b>(-38.54%)</b></td><td>0.05 <b>(-36.34%)</b></td><td>0.04 <b>(-42.79%)</b></td><td>0.01 <b>(-29.41%)</b></td><td>331.50 <b>(+74.84%)</b></td><td>259.42 <b>(+63.67%)</b></td><td>245.70 <b>(+57.10%)</b></td><td>225.80 <b>(+67.14%)</b></td><td>41.60 <b>(+110.19%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>158.50 (n/a)</td><td>156.40 (n/a)</td><td>135.10 (n/a)</td><td>19.79 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.03 <b>(-39.34%)</b></td><td>0.03 (-17.35%)</td><td>0.03 (-5.80%)</td><td>0.02 (-1.47%)</td><td>0.00 <b>(-74.53%)</b></td><td>215.60 (+1.51%)</td><td>188.70 (+15.68%)</td><td>179.20 (+6.16%)</td><td>174.70 <b>(+64.81%)</b></td><td>17.01 <b>(-55.23%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>163.12 (n/a)</td><td>168.80 (n/a)</td><td>106.00 (n/a)</td><td>37.99 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (+5.75%)</td><td>0.03 (-4.82%)</td><td>0.03 (-16.81%)</td><td>0.03 (-6.12%)</td><td>0.01 (-2.85%)</td><td>205.10 (+6.55%)</td><td>160.70 (+4.84%)</td><td>163.90 <b>(+20.16%)</b></td><td>120.60 (-5.41%)</td><td>30.97 (-2.01%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.50 (n/a)</td><td>153.28 (n/a)</td><td>136.40 (n/a)</td><td>127.50 (n/a)</td><td>31.60 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (-0.06%)</td><td>0.03 (+3.16%)</td><td>0.03 (+4.98%)</td><td>0.01 <b>(-20.04%)</b></td><td>0.01 (+5.74%)</td><td>364.30 <b>(+25.06%)</b></td><td>216.26 (-0.00%)</td><td>196.10 (-4.76%)</td><td>128.70 (+0.08%)</td><td>89.60 <b>(+35.00%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>291.30 (n/a)</td><td>216.26 (n/a)</td><td>205.90 (n/a)</td><td>128.60 (n/a)</td><td>66.37 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (-10.87%)</td><td>0.03 (+3.58%)</td><td>0.03 (+16.43%)</td><td>0.03 (+8.97%)</td><td>0.00 <b>(-36.79%)</b></td><td>190.70 (-8.23%)</td><td>169.56 (-5.00%)</td><td>167.70 (-14.09%)</td><td>149.60 (+12.23%)</td><td>20.40 <b>(-34.91%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>178.48 (n/a)</td><td>195.20 (n/a)</td><td>133.30 (n/a)</td><td>31.34 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 <b>(+26.47%)</b></td><td>0.03 (+11.67%)</td><td>0.03 (+8.62%)</td><td>0.02 (+7.51%)</td><td>0.01 <b>(+54.68%)</b></td><td>215.50 (-6.99%)</td><td>169.28 (-9.20%)</td><td>163.70 (-7.93%)</td><td>125.00 <b>(-20.94%)</b></td><td>33.90 (+13.43%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.70 (n/a)</td><td>186.44 (n/a)</td><td>177.80 (n/a)</td><td>158.10 (n/a)</td><td>29.89 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.03 (-8.60%)</td><td>0.03 (+2.95%)</td><td>0.03 (-0.16%)</td><td>0.03 (+4.56%)</td><td>0.00 <b>(-27.02%)</b></td><td>201.00 (-4.33%)</td><td>179.76 (-3.75%)</td><td>191.50 (+0.16%)</td><td>152.10 (+9.42%)</td><td>21.90 <b>(-21.67%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.10 (n/a)</td><td>186.76 (n/a)</td><td>191.20 (n/a)</td><td>139.00 (n/a)</td><td>27.97 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.03 (-15.52%)</td><td>0.03 (-9.14%)</td><td>0.03 (-9.27%)</td><td>0.02 (-2.07%)</td><td>0.00 <b>(-32.69%)</b></td><td>219.40 (+2.09%)</td><td>193.14 (+8.38%)</td><td>205.50 (+10.25%)</td><td>153.40 (+18.36%)</td><td>28.81 (-18.16%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>178.20 (n/a)</td><td>186.40 (n/a)</td><td>129.60 (n/a)</td><td>35.21 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.03 (+12.54%)</td><td>0.03 (+19.20%)</td><td>0.02 (+2.40%)</td><td>0.02 <b>(+32.32%)</b></td><td>0.01 (-13.63%)</td><td>297.10 <b>(-24.42%)</b></td><td>218.46 (-19.93%)</td><td>218.50 (-2.32%)</td><td>158.30 (-11.17%)</td><td>52.59 <b>(-44.13%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>393.10 (n/a)</td><td>272.84 (n/a)</td><td>223.70 (n/a)</td><td>178.20 (n/a)</td><td>94.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.80 (n/a)</td><td>168.68 (n/a)</td><td>156.20 (n/a)</td><td>155.00 (n/a)</td><td>24.43 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>162.80 (n/a)</td><td>151.68 (n/a)</td><td>152.60 (n/a)</td><td>136.60 (n/a)</td><td>9.56 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>162.26 (n/a)</td><td>158.80 (n/a)</td><td>143.40 (n/a)</td><td>18.58 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>166.12 (n/a)</td><td>160.30 (n/a)</td><td>135.30 (n/a)</td><td>33.49 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>174.10 (n/a)</td><td>142.08 (n/a)</td><td>141.20 (n/a)</td><td>113.40 (n/a)</td><td>21.66 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>179.22 (n/a)</td><td>173.50 (n/a)</td><td>149.30 (n/a)</td><td>29.00 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>188.82 (n/a)</td><td>187.80 (n/a)</td><td>164.60 (n/a)</td><td>18.79 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>359.00 (n/a)</td><td>241.20 (n/a)</td><td>186.30 (n/a)</td><td>148.60 (n/a)</td><td>100.47 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.50 (n/a)</td><td>183.00 (n/a)</td><td>183.60 (n/a)</td><td>128.70 (n/a)</td><td>43.32 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>317.20 (n/a)</td><td>203.58 (n/a)</td><td>187.10 (n/a)</td><td>146.50 (n/a)</td><td>65.98 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>227.90 (n/a)</td><td>174.54 (n/a)</td><td>201.30 (n/a)</td><td>109.50 (n/a)</td><td>52.73 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>164.80 (n/a)</td><td>168.30 (n/a)</td><td>124.80 (n/a)</td><td>42.72 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>272.40 (n/a)</td><td>202.32 (n/a)</td><td>212.50 (n/a)</td><td>117.90 (n/a)</td><td>58.12 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.40 (n/a)</td><td>205.60 (n/a)</td><td>191.50 (n/a)</td><td>154.10 (n/a)</td><td>54.88 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.30 (n/a)</td><td>194.68 (n/a)</td><td>204.80 (n/a)</td><td>155.20 (n/a)</td><td>36.75 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.40 (n/a)</td><td>194.08 (n/a)</td><td>205.20 (n/a)</td><td>125.70 (n/a)</td><td>48.00 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>4.19 (-7.61%)</td><td>3.79 (-7.03%)</td><td>3.64 (-10.89%)</td><td>3.46 (+0.50%)</td><td>0.32 <b>(-21.79%)</b></td><td>2719.30 (-0.49%)</td><td>2494.36 (+7.23%)</td><td>2586.30 (+12.22%)</td><td>2243.60 (+8.23%)</td><td>208.07 (-17.43%)</td><td>1648.86 (-7.61%)</td><td>1491.57 (-7.03%)</td><td>1430.35 (-10.89%)</td><td>1360.42 (+0.50%)</td><td>127.22 <b>(-21.79%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>4.54 (n/a)</td><td>4.08 (n/a)</td><td>4.08 (n/a)</td><td>3.44 (n/a)</td><td>0.41 (n/a)</td><td>2732.80 (n/a)</td><td>2326.16 (n/a)</td><td>2304.70 (n/a)</td><td>2072.90 (n/a)</td><td>252.00 (n/a)</td><td>1784.65 (n/a)</td><td>1604.38 (n/a)</td><td>1605.12 (n/a)</td><td>1353.71 (n/a)</td><td>162.66 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>1.13 (-11.40%)</td><td>0.96 (-11.29%)</td><td>1.04 (-4.72%)</td><td>0.63 <b>(-30.53%)</b></td><td>0.20 (+16.92%)</td><td>349.90 <b>(+43.93%)</b></td><td>240.20 (+15.44%)</td><td>212.20 (+4.95%)</td><td>194.90 (+12.85%)</td><td>62.84 <b>(+94.15%)</b></td><td>48.43 (-11.40%)</td><td>41.02 (-11.29%)</td><td>44.48 (-4.72%)</td><td>26.97 <b>(-30.53%)</b></td><td>8.35 (+16.92%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>1.28 (n/a)</td><td>1.08 (n/a)</td><td>1.09 (n/a)</td><td>0.91 (n/a)</td><td>0.17 (n/a)</td><td>243.10 (n/a)</td><td>208.08 (n/a)</td><td>202.20 (n/a)</td><td>172.70 (n/a)</td><td>32.37 (n/a)</td><td>54.66 (n/a)</td><td>46.24 (n/a)</td><td>46.68 (n/a)</td><td>38.83 (n/a)</td><td>7.14 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>1.02 (-12.37%)</td><td>0.80 (-11.32%)</td><td>0.84 (+14.79%)</td><td>0.57 <b>(-20.06%)</b></td><td>0.19 <b>(-21.92%)</b></td><td>385.40 <b>(+25.09%)</b></td><td>291.02 (+12.07%)</td><td>262.10 (-12.89%)</td><td>217.10 (+14.14%)</td><td>71.30 (+13.77%)</td><td>43.48 (-12.37%)</td><td>33.96 (-11.32%)</td><td>36.00 (+14.79%)</td><td>24.49 <b>(-20.06%)</b></td><td>7.91 <b>(-21.92%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>1.16 (n/a)</td><td>0.90 (n/a)</td><td>0.74 (n/a)</td><td>0.72 (n/a)</td><td>0.24 (n/a)</td><td>308.10 (n/a)</td><td>259.68 (n/a)</td><td>300.90 (n/a)</td><td>190.20 (n/a)</td><td>62.67 (n/a)</td><td>49.62 (n/a)</td><td>38.30 (n/a)</td><td>31.36 (n/a)</td><td>30.63 (n/a)</td><td>10.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.52 (-0.14%)</td><td>0.52 (-0.01%)</td><td>0.52 (+0.00%)</td><td>0.52 (+0.11%)</td><td>0.00 <b>(-41.08%)</b></td><td>48802.80 (-0.11%)</td><td>48684.34 (+0.01%)</td><td>48654.80 (-0.00%)</td><td>48616.00 (+0.14%)</td><td>72.36 <b>(-41.04%)</b></td><td>353.38 (-0.14%)</td><td>352.88 (-0.01%)</td><td>353.10 (+0.00%)</td><td>352.03 (+0.11%)</td><td>0.52 <b>(-41.08%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48855.70 (n/a)</td><td>48678.68 (n/a)</td><td>48655.50 (n/a)</td><td>48546.90 (n/a)</td><td>122.72 (n/a)</td><td>353.88 (n/a)</td><td>352.93 (n/a)</td><td>353.09 (n/a)</td><td>351.64 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.89 (-0.77%)</td><td>0.88 (-0.51%)</td><td>0.88 (-0.54%)</td><td>0.87 (-0.72%)</td><td>0.01 (-0.49%)</td><td>28896.60 (+0.72%)</td><td>28622.80 (+0.52%)</td><td>28671.20 (+0.54%)</td><td>28407.10 (+0.78%)</td><td>211.00 (+0.82%)</td><td>604.77 (-0.77%)</td><td>600.24 (-0.51%)</td><td>599.20 (-0.54%)</td><td>594.53 (-0.72%)</td><td>4.42 (-0.49%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28688.90 (n/a)</td><td>28476.06 (n/a)</td><td>28516.40 (n/a)</td><td>28188.10 (n/a)</td><td>209.28 (n/a)</td><td>609.47 (n/a)</td><td>603.34 (n/a)</td><td>602.46 (n/a)</td><td>598.83 (n/a)</td><td>4.44 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>3.46 (+6.45%)</td><td>3.28 (+3.90%)</td><td>3.25 (+3.34%)</td><td>3.14 (+1.49%)</td><td>0.12 <b>(+113.13%)</b></td><td>8006.50 (-1.46%)</td><td>7669.62 (-3.68%)</td><td>7741.70 (-3.23%)</td><td>7274.30 (-6.06%)</td><td>275.44 <b>(+97.28%)</b></td><td>2361.74 (+6.45%)</td><td>2242.33 (+3.90%)</td><td>2219.14 (+3.34%)</td><td>2145.73 (+1.49%)</td><td>81.49 <b>(+113.13%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>3.25 (n/a)</td><td>3.16 (n/a)</td><td>3.15 (n/a)</td><td>3.10 (n/a)</td><td>0.06 (n/a)</td><td>8125.50 (n/a)</td><td>7962.46 (n/a)</td><td>8000.50 (n/a)</td><td>7743.40 (n/a)</td><td>139.62 (n/a)</td><td>2218.65 (n/a)</td><td>2158.14 (n/a)</td><td>2147.35 (n/a)</td><td>2114.31 (n/a)</td><td>38.23 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>4.16 (+5.71%)</td><td>3.44 (-2.58%)</td><td>3.55 (-0.69%)</td><td>2.93 (+1.35%)</td><td>0.50 <b>(+25.48%)</b></td><td>2752.90 (-1.33%)</td><td>2383.62 (+3.19%)</td><td>2272.30 (+0.69%)</td><td>1936.30 (-5.39%)</td><td>338.71 (+17.39%)</td><td>1091.76 (+5.71%)</td><td>901.76 (-2.58%)</td><td>930.31 (-0.69%)</td><td>767.90 (+1.35%)</td><td>131.81 <b>(+25.48%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>3.94 (n/a)</td><td>3.53 (n/a)</td><td>3.57 (n/a)</td><td>2.89 (n/a)</td><td>0.40 (n/a)</td><td>2790.00 (n/a)</td><td>2309.92 (n/a)</td><td>2256.70 (n/a)</td><td>2046.70 (n/a)</td><td>288.52 (n/a)</td><td>1032.84 (n/a)</td><td>925.60 (n/a)</td><td>936.73 (n/a)</td><td>757.68 (n/a)</td><td>105.05 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.45 (-10.21%)</td><td>0.36 (-6.29%)</td><td>0.35 (-5.99%)</td><td>0.31 (+0.48%)</td><td>0.06 <b>(-22.82%)</b></td><td>4010.80 (-0.48%)</td><td>3567.18 (+5.86%)</td><td>3582.40 (+6.37%)</td><td>2777.60 (+11.38%)</td><td>491.63 (-12.39%)</td><td>24.16 (-10.21%)</td><td>19.14 (-6.29%)</td><td>18.73 (-5.99%)</td><td>16.73 (+0.48%)</td><td>2.99 <b>(-22.82%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.50 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>4030.20 (n/a)</td><td>3369.80 (n/a)</td><td>3368.00 (n/a)</td><td>2493.90 (n/a)</td><td>561.13 (n/a)</td><td>26.91 (n/a)</td><td>20.42 (n/a)</td><td>19.93 (n/a)</td><td>16.65 (n/a)</td><td>3.87 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>4.83 (-9.73%)</td><td>4.40 (-11.95%)</td><td>4.73 (-5.45%)</td><td>3.79 (-18.77%)</td><td>0.53 <b>(+92.07%)</b></td><td>1756.70 <b>(+23.11%)</b></td><td>1528.78 (+14.68%)</td><td>1406.30 (+5.76%)</td><td>1378.50 (+10.79%)</td><td>191.74 <b>(+161.12%)</b></td><td>1490.90 (-9.73%)</td><td>1360.72 (-11.95%)</td><td>1461.40 (-5.45%)</td><td>1169.90 (-18.77%)</td><td>163.19 <b>(+92.07%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>5.35 (n/a)</td><td>5.00 (n/a)</td><td>5.00 (n/a)</td><td>4.66 (n/a)</td><td>0.27 (n/a)</td><td>1426.90 (n/a)</td><td>1333.12 (n/a)</td><td>1329.70 (n/a)</td><td>1244.30 (n/a)</td><td>73.43 (n/a)</td><td>1651.64 (n/a)</td><td>1545.37 (n/a)</td><td>1545.60 (n/a)</td><td>1440.31 (n/a)</td><td>84.96 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.23 (+9.21%)</td><td>0.20 (+11.24%)</td><td>0.19 (+10.57%)</td><td>0.16 (+3.76%)</td><td>0.03 <b>(+39.80%)</b></td><td>0.23 (+9.21%)</td><td>0.20 (+11.24%)</td><td>0.19 (+10.57%)</td><td>0.16 (+3.76%)</td><td>0.03 <b>(+39.80%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>13.37 (+0.36%)</td><td>12.19 (+3.00%)</td><td>11.97 (+0.45%)</td><td>10.59 (+4.26%)</td><td>1.15 (+1.39%)</td><td>13.36 (+0.36%)</td><td>12.18 (+3.00%)</td><td>11.96 (+0.45%)</td><td>10.58 (+4.26%)</td><td>1.15 (+1.39%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>13.32 (n/a)</td><td>11.83 (n/a)</td><td>11.91 (n/a)</td><td>10.16 (n/a)</td><td>1.13 (n/a)</td><td>13.31 (n/a)</td><td>11.83 (n/a)</td><td>11.90 (n/a)</td><td>10.15 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>24.80 (-1.01%)</td><td>23.89 (+5.75%)</td><td>23.98 (+3.46%)</td><td>22.89 <b>(+29.40%)</b></td><td>0.69 <b>(-75.80%)</b></td><td>24.78 (-1.01%)</td><td>23.88 (+5.75%)</td><td>23.97 (+3.46%)</td><td>22.87 <b>(+29.40%)</b></td><td>0.69 <b>(-75.80%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>25.05 (n/a)</td><td>22.59 (n/a)</td><td>23.18 (n/a)</td><td>17.69 (n/a)</td><td>2.85 (n/a)</td><td>25.04 (n/a)</td><td>22.58 (n/a)</td><td>23.16 (n/a)</td><td>17.68 (n/a)</td><td>2.85 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>42.62 (-1.16%)</td><td>39.90 (+0.44%)</td><td>39.08 (-0.94%)</td><td>38.35 (+1.56%)</td><td>1.71 (-19.10%)</td><td>42.59 (-1.16%)</td><td>39.87 (+0.44%)</td><td>39.05 (-0.94%)</td><td>38.33 (+1.56%)</td><td>1.71 (-19.10%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>43.12 (n/a)</td><td>39.72 (n/a)</td><td>39.45 (n/a)</td><td>37.76 (n/a)</td><td>2.12 (n/a)</td><td>43.09 (n/a)</td><td>39.70 (n/a)</td><td>39.42 (n/a)</td><td>37.74 (n/a)</td><td>2.12 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>44.04 (-2.00%)</td><td>42.83 (+0.04%)</td><td>42.69 (-0.43%)</td><td>41.08 (-0.01%)</td><td>1.16 <b>(-28.16%)</b></td><td>44.01 (-2.00%)</td><td>42.81 (+0.04%)</td><td>42.67 (-0.43%)</td><td>41.06 (-0.01%)</td><td>1.16 <b>(-28.16%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>44.94 (n/a)</td><td>42.82 (n/a)</td><td>42.88 (n/a)</td><td>41.09 (n/a)</td><td>1.61 (n/a)</td><td>44.91 (n/a)</td><td>42.79 (n/a)</td><td>42.85 (n/a)</td><td>41.06 (n/a)</td><td>1.61 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>13.38 (-0.75%)</td><td>12.64 (-1.04%)</td><td>12.76 (-1.09%)</td><td>11.40 (+0.15%)</td><td>0.79 (-8.10%)</td><td>13.37 (-0.75%)</td><td>12.63 (-1.04%)</td><td>12.75 (-1.09%)</td><td>11.39 (+0.15%)</td><td>0.78 (-8.10%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>13.48 (n/a)</td><td>12.77 (n/a)</td><td>12.90 (n/a)</td><td>11.38 (n/a)</td><td>0.85 (n/a)</td><td>13.47 (n/a)</td><td>12.76 (n/a)</td><td>12.89 (n/a)</td><td>11.37 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>24.57 (-1.65%)</td><td>23.93 (+0.31%)</td><td>23.89 (-1.96%)</td><td>23.48 (+11.19%)</td><td>0.40 <b>(-74.47%)</b></td><td>24.55 (-1.65%)</td><td>23.92 (+0.31%)</td><td>23.88 (-1.96%)</td><td>23.47 (+11.19%)</td><td>0.40 <b>(-74.47%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>24.98 (n/a)</td><td>23.86 (n/a)</td><td>24.37 (n/a)</td><td>21.12 (n/a)</td><td>1.58 (n/a)</td><td>24.96 (n/a)</td><td>23.85 (n/a)</td><td>24.35 (n/a)</td><td>21.10 (n/a)</td><td>1.58 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>40.90 (+1.19%)</td><td>39.67 (+1.53%)</td><td>39.55 (+1.37%)</td><td>38.61 (+4.91%)</td><td>0.98 <b>(-33.97%)</b></td><td>40.88 (+1.19%)</td><td>39.65 (+1.53%)</td><td>39.52 (+1.37%)</td><td>38.58 (+4.91%)</td><td>0.98 <b>(-33.97%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>40.42 (n/a)</td><td>39.07 (n/a)</td><td>39.01 (n/a)</td><td>36.80 (n/a)</td><td>1.48 (n/a)</td><td>40.40 (n/a)</td><td>39.05 (n/a)</td><td>38.99 (n/a)</td><td>36.78 (n/a)</td><td>1.48 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>47.34 (+5.18%)</td><td>42.59 (-1.61%)</td><td>42.46 (-3.12%)</td><td>38.97 (-5.88%)</td><td>3.04 <b>(+110.39%)</b></td><td>47.31 (+5.18%)</td><td>42.57 (-1.61%)</td><td>42.43 (-3.12%)</td><td>38.95 (-5.88%)</td><td>3.04 <b>(+110.39%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>45.01 (n/a)</td><td>43.29 (n/a)</td><td>43.82 (n/a)</td><td>41.41 (n/a)</td><td>1.44 (n/a)</td><td>44.98 (n/a)</td><td>43.26 (n/a)</td><td>43.80 (n/a)</td><td>41.38 (n/a)</td><td>1.44 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>9.59 (n/a)</td><td>8.64 (n/a)</td><td>8.75 (n/a)</td><td>7.55 (n/a)</td><td>0.79 (n/a)</td><td>9.57 (n/a)</td><td>8.62 (n/a)</td><td>8.74 (n/a)</td><td>7.53 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.02 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>1.14 (n/a)</td><td>1.01 (n/a)</td><td>0.99 (n/a)</td><td>0.92 (n/a)</td><td>0.09 (n/a)</td><td>1.13 (n/a)</td><td>1.00 (n/a)</td><td>0.98 (n/a)</td><td>0.91 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>16.82 (n/a)</td><td>15.09 (n/a)</td><td>14.42 (n/a)</td><td>13.95 (n/a)</td><td>1.27 (n/a)</td><td>16.62 (n/a)</td><td>14.92 (n/a)</td><td>14.25 (n/a)</td><td>13.78 (n/a)</td><td>1.26 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>12.12 (n/a)</td><td>11.24 (n/a)</td><td>11.55 (n/a)</td><td>10.31 (n/a)</td><td>0.79 (n/a)</td><td>11.91 (n/a)</td><td>11.04 (n/a)</td><td>11.35 (n/a)</td><td>10.13 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>7.77 (n/a)</td><td>6.85 (n/a)</td><td>7.53 (n/a)</td><td>5.02 (n/a)</td><td>1.17 (n/a)</td><td>7.63 (n/a)</td><td>6.73 (n/a)</td><td>7.40 (n/a)</td><td>4.93 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>6.13 (n/a)</td><td>5.37 (n/a)</td><td>5.29 (n/a)</td><td>4.80 (n/a)</td><td>0.48 (n/a)</td><td>6.04 (n/a)</td><td>5.28 (n/a)</td><td>5.20 (n/a)</td><td>4.72 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>161.52 (n/a)</td><td>147.40 (n/a)</td><td>145.60 (n/a)</td><td>22.21 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>291.50 (n/a)</td><td>196.12 (n/a)</td><td>180.20 (n/a)</td><td>142.50 (n/a)</td><td>58.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>188.40 (n/a)</td><td>175.08 (n/a)</td><td>177.00 (n/a)</td><td>161.20 (n/a)</td><td>9.89 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>211.00 (n/a)</td><td>183.48 (n/a)</td><td>178.50 (n/a)</td><td>161.40 (n/a)</td><td>19.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.90 (n/a)</td><td>161.12 (n/a)</td><td>158.70 (n/a)</td><td>129.50 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>222.70 (n/a)</td><td>207.80 (n/a)</td><td>209.20 (n/a)</td><td>184.60 (n/a)</td><td>14.90 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>330.90 (n/a)</td><td>219.06 (n/a)</td><td>200.70 (n/a)</td><td>165.40 (n/a)</td><td>64.53 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>301.60 (n/a)</td><td>274.84 (n/a)</td><td>296.40 (n/a)</td><td>235.60 (n/a)</td><td>33.51 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (-8.29%)</td><td>0.04 (-0.41%)</td><td>0.04 (+4.21%)</td><td>0.04 (-1.10%)</td><td>0.01 (-14.45%)</td><td>233.20 (+1.08%)</td><td>191.38 (-0.20%)</td><td>187.40 (-4.05%)</td><td>159.20 (+9.04%)</td><td>32.88 (-8.00%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>191.76 (n/a)</td><td>195.30 (n/a)</td><td>146.00 (n/a)</td><td>35.73 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (-19.32%)</td><td>0.05 (-8.28%)</td><td>0.05 (-1.60%)</td><td>0.04 (-1.00%)</td><td>0.00 <b>(-53.55%)</b></td><td>197.60 (+1.02%)</td><td>175.94 (+6.68%)</td><td>171.20 (+1.66%)</td><td>155.20 <b>(+23.96%)</b></td><td>17.82 <b>(-42.40%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>164.92 (n/a)</td><td>168.40 (n/a)</td><td>125.20 (n/a)</td><td>30.93 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 <b>(+20.99%)</b></td><td>0.05 (+4.11%)</td><td>0.05 (+3.63%)</td><td>0.04 (-16.72%)</td><td>0.01 <b>(+303.59%)</b></td><td>224.80 <b>(+20.09%)</b></td><td>169.80 (-0.70%)</td><td>161.00 (-3.48%)</td><td>135.40 (-17.34%)</td><td>37.04 <b>(+292.67%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>187.20 (n/a)</td><td>171.00 (n/a)</td><td>166.80 (n/a)</td><td>163.80 (n/a)</td><td>9.43 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (+17.52%)</td><td>0.05 (+10.62%)</td><td>0.05 (+13.61%)</td><td>0.04 (+1.87%)</td><td>0.01 <b>(+59.12%)</b></td><td>190.00 (-1.81%)</td><td>164.22 (-8.59%)</td><td>164.00 (-11.97%)</td><td>125.00 (-14.91%)</td><td>24.99 <b>(+33.10%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>179.66 (n/a)</td><td>186.30 (n/a)</td><td>146.90 (n/a)</td><td>18.78 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (+2.97%)</td><td>0.04 (-12.30%)</td><td>0.04 (-13.17%)</td><td>0.03 <b>(-38.42%)</b></td><td>0.01 <b>(+144.63%)</b></td><td>318.00 <b>(+62.41%)</b></td><td>214.98 <b>(+21.20%)</b></td><td>204.10 (+15.18%)</td><td>152.90 (-2.92%)</td><td>66.29 <b>(+280.16%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.80 (n/a)</td><td>177.38 (n/a)</td><td>177.20 (n/a)</td><td>157.50 (n/a)</td><td>17.44 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (+9.06%)</td><td>0.04 (-1.05%)</td><td>0.04 (-3.95%)</td><td>0.03 (-9.56%)</td><td>0.01 <b>(+64.76%)</b></td><td>242.80 (+10.56%)</td><td>192.18 (+2.87%)</td><td>195.40 (+4.16%)</td><td>150.60 (-8.28%)</td><td>35.93 <b>(+65.85%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>219.60 (n/a)</td><td>186.82 (n/a)</td><td>187.60 (n/a)</td><td>164.20 (n/a)</td><td>21.67 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (-10.99%)</td><td>0.04 (-18.63%)</td><td>0.04 (-17.35%)</td><td>0.03 (-18.56%)</td><td>0.01 (-6.15%)</td><td>235.90 <b>(+22.74%)</b></td><td>195.04 <b>(+23.35%)</b></td><td>195.00 <b>(+21.04%)</b></td><td>151.60 (+12.38%)</td><td>30.26 <b>(+29.43%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>158.12 (n/a)</td><td>161.10 (n/a)</td><td>134.90 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (+4.23%)</td><td>0.04 (+2.39%)</td><td>0.04 (-0.81%)</td><td>0.03 (-9.02%)</td><td>0.01 <b>(+49.12%)</b></td><td>251.20 (+9.93%)</td><td>200.58 (-1.02%)</td><td>202.90 (+0.84%)</td><td>166.10 (-4.04%)</td><td>35.19 <b>(+51.84%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>228.50 (n/a)</td><td>202.64 (n/a)</td><td>201.20 (n/a)</td><td>173.10 (n/a)</td><td>23.17 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 <b>(-33.77%)</b></td><td>0.04 <b>(-22.33%)</b></td><td>0.04 (-13.97%)</td><td>0.03 <b>(-28.71%)</b></td><td>0.01 <b>(-35.37%)</b></td><td>312.40 <b>(+40.28%)</b></td><td>226.56 <b>(+28.51%)</b></td><td>205.90 (+16.26%)</td><td>193.40 <b>(+50.98%)</b></td><td>49.05 <b>(+43.61%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>176.30 (n/a)</td><td>177.10 (n/a)</td><td>128.10 (n/a)</td><td>34.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (-10.95%)</td><td>0.03 <b>(-20.56%)</b></td><td>0.04 (-6.98%)</td><td>0.02 <b>(-36.52%)</b></td><td>0.01 <b>(+61.62%)</b></td><td>364.20 <b>(+57.53%)</b></td><td>273.12 <b>(+32.11%)</b></td><td>230.30 (+7.52%)</td><td>195.30 (+12.31%)</td><td>77.17 <b>(+196.51%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>206.74 (n/a)</td><td>214.20 (n/a)</td><td>173.90 (n/a)</td><td>26.03 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (-7.94%)</td><td>0.05 (+5.84%)</td><td>0.05 (+6.83%)</td><td>0.05 <b>(+24.97%)</b></td><td>0.00 <b>(-52.35%)</b></td><td>168.60 (-19.98%)</td><td>153.82 (-7.33%)</td><td>156.70 (-6.39%)</td><td>141.30 (+8.69%)</td><td>11.91 <b>(-59.51%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.70 (n/a)</td><td>165.98 (n/a)</td><td>167.40 (n/a)</td><td>130.00 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 <b>(-28.25%)</b></td><td>0.04 (-11.05%)</td><td>0.04 (-12.90%)</td><td>0.03 <b>(+27.21%)</b></td><td>0.00 <b>(-76.25%)</b></td><td>246.80 <b>(-21.38%)</b></td><td>219.34 (+3.44%)</td><td>214.00 (+14.81%)</td><td>196.80 <b>(+39.38%)</b></td><td>18.93 <b>(-73.98%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>313.90 (n/a)</td><td>212.04 (n/a)</td><td>186.40 (n/a)</td><td>141.20 (n/a)</td><td>72.76 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (-1.64%)</td><td>0.06 (+19.62%)</td><td>0.06 <b>(+28.38%)</b></td><td>0.05 <b>(+28.85%)</b></td><td>0.01 <b>(-26.45%)</b></td><td>178.50 <b>(-22.39%)</b></td><td>147.14 (-18.37%)</td><td>132.80 <b>(-22.11%)</b></td><td>129.20 (+1.65%)</td><td>22.85 <b>(-42.91%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.00 (n/a)</td><td>180.26 (n/a)</td><td>170.50 (n/a)</td><td>127.10 (n/a)</td><td>40.03 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (-8.85%)</td><td>0.05 (+5.59%)</td><td>0.05 (+4.49%)</td><td>0.05 <b>(+50.93%)</b></td><td>0.01 <b>(-53.39%)</b></td><td>178.00 <b>(-33.76%)</b></td><td>165.16 (-10.04%)</td><td>170.60 (-4.26%)</td><td>135.50 (+9.72%)</td><td>17.36 <b>(-67.18%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>268.70 (n/a)</td><td>183.60 (n/a)</td><td>178.20 (n/a)</td><td>123.50 (n/a)</td><td>52.89 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (-4.10%)</td><td>0.05 (-7.44%)</td><td>0.05 (-9.57%)</td><td>0.04 (-5.88%)</td><td>0.01 (+5.46%)</td><td>193.20 (+6.21%)</td><td>171.10 (+8.29%)</td><td>168.50 (+10.56%)</td><td>141.50 (+4.27%)</td><td>21.12 (+17.15%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.90 (n/a)</td><td>158.00 (n/a)</td><td>152.40 (n/a)</td><td>135.70 (n/a)</td><td>18.03 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 <b>(-24.56%)</b></td><td>0.05 (-4.06%)</td><td>0.05 (-3.61%)</td><td>0.04 <b>(+28.57%)</b></td><td>0.00 <b>(-82.27%)</b></td><td>183.00 <b>(-22.23%)</b></td><td>169.82 (-0.29%)</td><td>167.50 (+3.72%)</td><td>164.50 <b>(+32.55%)</b></td><td>7.62 <b>(-81.94%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.30 (n/a)</td><td>170.32 (n/a)</td><td>161.50 (n/a)</td><td>124.10 (n/a)</td><td>42.18 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (+6.47%)</td><td>0.05 (+0.40%)</td><td>0.04 (-10.13%)</td><td>0.04 (-3.78%)</td><td>0.01 <b>(+65.50%)</b></td><td>199.80 (+3.90%)</td><td>176.06 (+0.58%)</td><td>189.20 (+11.29%)</td><td>146.90 (-6.07%)</td><td>24.02 <b>(+58.18%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>192.30 (n/a)</td><td>175.04 (n/a)</td><td>170.00 (n/a)</td><td>156.40 (n/a)</td><td>15.19 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (-1.71%)</td><td>0.05 (+4.81%)</td><td>0.05 (-1.17%)</td><td>0.04 <b>(+60.58%)</b></td><td>0.00 <b>(-56.94%)</b></td><td>203.10 <b>(-37.72%)</b></td><td>177.92 (-10.72%)</td><td>172.30 (+1.17%)</td><td>154.10 (+1.72%)</td><td>18.52 <b>(-74.19%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>326.10 (n/a)</td><td>199.28 (n/a)</td><td>170.30 (n/a)</td><td>151.50 (n/a)</td><td>71.76 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.21 (+0.05%)</td><td>0.21 (+0.05%)</td><td>0.21 (-0.16%)</td><td>0.21 (+0.35%)</td><td>0.00 <b>(-36.54%)</b></td><td>40906.00 (-0.35%)</td><td>40844.16 (-0.05%)</td><td>40882.50 (+0.16%)</td><td>40753.10 (-0.05%)</td><td>68.98 <b>(-36.80%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>41048.30 (n/a)</td><td>40864.76 (n/a)</td><td>40818.90 (n/a)</td><td>40772.70 (n/a)</td><td>109.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 <b>(+39.78%)</b></td><td>0.05 (+12.62%)</td><td>0.05 (+10.22%)</td><td>0.04 (-6.11%)</td><td>0.01 <b>(+135.89%)</b></td><td>229.20 (+6.51%)</td><td>172.88 (-6.99%)</td><td>175.80 (-9.29%)</td><td>112.30 <b>(-28.43%)</b></td><td>45.39 <b>(+80.48%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>185.88 (n/a)</td><td>193.80 (n/a)</td><td>156.90 (n/a)</td><td>25.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.09 (-5.02%)</td><td>0.07 (-5.43%)</td><td>0.07 (-6.89%)</td><td>0.06 (-11.40%)</td><td>0.01 (+7.00%)</td><td>205.90 (+12.82%)</td><td>171.16 (+6.42%)</td><td>172.80 (+7.40%)</td><td>131.90 (+5.35%)</td><td>28.25 <b>(+28.48%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>182.50 (n/a)</td><td>160.84 (n/a)</td><td>160.90 (n/a)</td><td>125.20 (n/a)</td><td>21.99 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (+12.80%)</td><td>0.05 (+0.54%)</td><td>0.05 (+5.38%)</td><td>0.03 <b>(-24.06%)</b></td><td>0.01 <b>(+66.94%)</b></td><td>254.80 <b>(+31.68%)</b></td><td>177.36 (+3.84%)</td><td>172.10 (-5.13%)</td><td>119.40 (-11.36%)</td><td>51.15 <b>(+92.76%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>170.80 (n/a)</td><td>181.40 (n/a)</td><td>134.70 (n/a)</td><td>26.54 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.08 (-4.57%)</td><td>0.06 (-4.45%)</td><td>0.06 (-2.95%)</td><td>0.05 (-10.51%)</td><td>0.01 (-2.17%)</td><td>199.60 (+11.76%)</td><td>168.08 (+4.91%)</td><td>175.50 (+3.05%)</td><td>121.80 (+4.82%)</td><td>28.74 (+12.15%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>178.60 (n/a)</td><td>160.22 (n/a)</td><td>170.30 (n/a)</td><td>116.20 (n/a)</td><td>25.62 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 <b>(-24.60%)</b></td><td>0.05 (+0.98%)</td><td>0.05 (+14.01%)</td><td>0.04 (+6.63%)</td><td>0.01 <b>(-53.13%)</b></td><td>202.00 (-6.22%)</td><td>169.50 (-4.59%)</td><td>162.30 (-12.32%)</td><td>147.70 <b>(+32.59%)</b></td><td>23.98 <b>(-39.00%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>177.66 (n/a)</td><td>185.10 (n/a)</td><td>111.40 (n/a)</td><td>39.31 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 <b>(-31.54%)</b></td><td>0.06 (-15.22%)</td><td>0.06 (-7.76%)</td><td>0.05 (-12.12%)</td><td>0.01 <b>(-55.86%)</b></td><td>203.60 (+13.81%)</td><td>176.48 (+14.87%)</td><td>179.70 (+8.38%)</td><td>149.40 <b>(+46.04%)</b></td><td>22.80 <b>(-24.14%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>178.90 (n/a)</td><td>153.64 (n/a)</td><td>165.80 (n/a)</td><td>102.30 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (-3.83%)</td><td>0.05 (-2.03%)</td><td>0.04 (-0.46%)</td><td>0.04 (+10.61%)</td><td>0.01 <b>(-27.24%)</b></td><td>212.90 (-9.60%)</td><td>172.26 (-2.11%)</td><td>185.90 (+0.43%)</td><td>118.20 (+3.96%)</td><td>36.27 <b>(-32.78%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>235.50 (n/a)</td><td>175.98 (n/a)</td><td>185.10 (n/a)</td><td>113.70 (n/a)</td><td>53.96 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (+9.02%)</td><td>0.05 (+4.87%)</td><td>0.05 (-5.92%)</td><td>0.03 <b>(-24.44%)</b></td><td>0.02 <b>(+66.52%)</b></td><td>313.00 <b>(+32.35%)</b></td><td>200.48 (+1.56%)</td><td>204.30 (+6.30%)</td><td>132.50 (-8.24%)</td><td>71.41 <b>(+101.12%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>236.50 (n/a)</td><td>197.40 (n/a)</td><td>192.20 (n/a)</td><td>144.40 (n/a)</td><td>35.51 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (+1.61%)</td><td>0.05 (+16.49%)</td><td>0.05 (+16.20%)</td><td>0.05 <b>(+32.74%)</b></td><td>0.00 <b>(-48.53%)</b></td><td>179.00 <b>(-24.63%)</b></td><td>171.44 (-15.98%)</td><td>176.00 (-13.94%)</td><td>147.80 (-1.60%)</td><td>13.29 <b>(-61.90%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.50 (n/a)</td><td>204.04 (n/a)</td><td>204.50 (n/a)</td><td>150.20 (n/a)</td><td>34.87 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 <b>(+27.19%)</b></td><td>0.06 <b>(+22.72%)</b></td><td>0.06 <b>(+32.65%)</b></td><td>0.05 (+9.36%)</td><td>0.01 <b>(+122.81%)</b></td><td>200.40 (-8.58%)</td><td>169.16 (-17.28%)</td><td>157.30 <b>(-24.63%)</b></td><td>139.40 <b>(-21.42%)</b></td><td>27.60 <b>(+66.43%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>219.20 (n/a)</td><td>204.50 (n/a)</td><td>208.70 (n/a)</td><td>177.40 (n/a)</td><td>16.58 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 <b>(+30.01%)</b></td><td>0.05 <b>(+21.02%)</b></td><td>0.04 (+17.10%)</td><td>0.04 (+6.02%)</td><td>0.01 <b>(+110.76%)</b></td><td>225.90 (-5.68%)</td><td>184.34 (-16.41%)</td><td>187.00 (-14.61%)</td><td>154.20 <b>(-23.09%)</b></td><td>27.50 <b>(+51.69%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.50 (n/a)</td><td>220.54 (n/a)</td><td>219.00 (n/a)</td><td>200.50 (n/a)</td><td>18.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (+6.10%)</td><td>0.05 (+13.11%)</td><td>0.05 (+16.02%)</td><td>0.04 <b>(+39.62%)</b></td><td>0.01 <b>(-35.69%)</b></td><td>218.30 <b>(-28.38%)</b></td><td>185.36 (-14.27%)</td><td>181.00 (-13.81%)</td><td>160.70 (-5.80%)</td><td>23.36 <b>(-56.64%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>304.80 (n/a)</td><td>216.22 (n/a)</td><td>210.00 (n/a)</td><td>170.60 (n/a)</td><td>53.86 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 <b>(+39.23%)</b></td><td>0.05 (+16.15%)</td><td>0.04 (+11.35%)</td><td>0.04 (+9.92%)</td><td>0.01 <b>(+105.67%)</b></td><td>215.80 (-9.02%)</td><td>185.88 (-12.28%)</td><td>190.10 (-10.20%)</td><td>132.70 <b>(-28.15%)</b></td><td>32.88 <b>(+30.77%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.20 (n/a)</td><td>211.90 (n/a)</td><td>211.70 (n/a)</td><td>184.70 (n/a)</td><td>25.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 <b>(+32.09%)</b></td><td>0.05 <b>(+21.53%)</b></td><td>0.05 (+16.35%)</td><td>0.04 (+17.40%)</td><td>0.01 <b>(+154.06%)</b></td><td>215.40 (-14.79%)</td><td>186.84 (-16.59%)</td><td>188.90 (-14.06%)</td><td>158.30 <b>(-24.29%)</b></td><td>27.77 <b>(+61.19%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>252.80 (n/a)</td><td>224.00 (n/a)</td><td>219.80 (n/a)</td><td>209.10 (n/a)</td><td>17.23 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (+13.92%)</td><td>0.04 (+1.73%)</td><td>0.04 (-5.77%)</td><td>0.04 (+2.22%)</td><td>0.01 <b>(+66.20%)</b></td><td>223.90 (-2.18%)</td><td>201.68 (-0.60%)</td><td>219.10 (+6.10%)</td><td>157.50 (-12.21%)</td><td>29.55 <b>(+46.27%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>228.90 (n/a)</td><td>202.90 (n/a)</td><td>206.50 (n/a)</td><td>179.40 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.63 (+9.24%)</td><td>0.49 (+2.37%)</td><td>0.51 (+8.71%)</td><td>0.27 <b>(-30.75%)</b></td><td>0.13 <b>(+69.31%)</b></td><td>365.40 <b>(+44.37%)</b></td><td>219.70 (+3.96%)</td><td>192.30 (-7.99%)</td><td>156.20 (-8.44%)</td><td>83.00 <b>(+140.82%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.47 (n/a)</td><td>0.39 (n/a)</td><td>0.08 (n/a)</td><td>253.10 (n/a)</td><td>211.34 (n/a)</td><td>209.00 (n/a)</td><td>170.60 (n/a)</td><td>34.47 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.56 <b>(-25.60%)</b></td><td>0.50 (-16.59%)</td><td>0.52 (-4.93%)</td><td>0.43 (-18.90%)</td><td>0.06 <b>(-39.40%)</b></td><td>227.60 <b>(+23.29%)</b></td><td>198.48 (+19.12%)</td><td>188.90 (+5.18%)</td><td>176.60 <b>(+34.50%)</b></td><td>22.76 (+0.28%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.75 (n/a)</td><td>0.60 (n/a)</td><td>0.55 (n/a)</td><td>0.53 (n/a)</td><td>0.09 (n/a)</td><td>184.60 (n/a)</td><td>166.62 (n/a)</td><td>179.60 (n/a)</td><td>131.30 (n/a)</td><td>22.70 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.62 (-7.87%)</td><td>0.57 (-6.42%)</td><td>0.57 (-9.95%)</td><td>0.51 (-5.81%)</td><td>0.04 <b>(-22.22%)</b></td><td>191.80 (+6.20%)</td><td>173.12 (+6.64%)</td><td>173.20 (+11.03%)</td><td>157.90 (+8.60%)</td><td>13.41 (-11.64%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.68 (n/a)</td><td>0.61 (n/a)</td><td>0.63 (n/a)</td><td>0.54 (n/a)</td><td>0.06 (n/a)</td><td>180.60 (n/a)</td><td>162.34 (n/a)</td><td>156.00 (n/a)</td><td>145.40 (n/a)</td><td>15.18 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.59 (-9.17%)</td><td>0.46 (-10.07%)</td><td>0.40 (-15.77%)</td><td>0.39 (-15.39%)</td><td>0.09 (+11.94%)</td><td>252.40 (+18.16%)</td><td>221.32 (+12.43%)</td><td>244.80 (+18.72%)</td><td>167.10 (+10.08%)</td><td>38.47 <b>(+51.34%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.65 (n/a)</td><td>0.51 (n/a)</td><td>0.48 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>213.60 (n/a)</td><td>196.86 (n/a)</td><td>206.20 (n/a)</td><td>151.80 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.44 (-18.57%)</td><td>0.37 <b>(-22.84%)</b></td><td>0.38 <b>(-22.21%)</b></td><td>0.30 <b>(-29.90%)</b></td><td>0.05 (+1.69%)</td><td>245.20 <b>(+42.64%)</b></td><td>201.66 <b>(+30.46%)</b></td><td>196.60 <b>(+28.58%)</b></td><td>168.00 <b>(+22.81%)</b></td><td>27.85 <b>(+78.61%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.48 (n/a)</td><td>0.43 (n/a)</td><td>0.05 (n/a)</td><td>171.90 (n/a)</td><td>154.58 (n/a)</td><td>152.90 (n/a)</td><td>136.80 (n/a)</td><td>15.59 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.54 (+11.38%)</td><td>0.41 (+4.13%)</td><td>0.36 (-8.24%)</td><td>0.34 (-1.78%)</td><td>0.09 <b>(+69.98%)</b></td><td>217.60 (+1.82%)</td><td>185.78 (-1.67%)</td><td>206.40 (+8.98%)</td><td>136.20 (-10.22%)</td><td>38.09 <b>(+60.84%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.05 (n/a)</td><td>213.70 (n/a)</td><td>188.94 (n/a)</td><td>189.40 (n/a)</td><td>151.70 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.49 (-12.16%)</td><td>0.38 (-14.95%)</td><td>0.35 <b>(-27.79%)</b></td><td>0.33 (+14.81%)</td><td>0.07 <b>(-40.02%)</b></td><td>225.00 (-12.93%)</td><td>197.50 (+13.08%)</td><td>211.00 <b>(+38.45%)</b></td><td>149.10 (+13.90%)</td><td>30.35 <b>(-41.81%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.48 (n/a)</td><td>0.29 (n/a)</td><td>0.11 (n/a)</td><td>258.40 (n/a)</td><td>174.66 (n/a)</td><td>152.40 (n/a)</td><td>130.90 (n/a)</td><td>52.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.44 <b>(-25.03%)</b></td><td>0.34 <b>(-22.29%)</b></td><td>0.30 <b>(-26.40%)</b></td><td>0.30 (-14.45%)</td><td>0.06 <b>(-38.04%)</b></td><td>245.60 (+16.90%)</td><td>224.22 <b>(+26.88%)</b></td><td>242.10 <b>(+35.86%)</b></td><td>167.80 <b>(+33.39%)</b></td><td>33.01 (-4.82%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.59 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.10 (n/a)</td><td>210.10 (n/a)</td><td>176.72 (n/a)</td><td>178.20 (n/a)</td><td>125.80 (n/a)</td><td>34.68 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>1.03 (+3.86%)</td><td>0.79 (+6.18%)</td><td>0.71 (-0.16%)</td><td>0.55 (-8.96%)</td><td>0.21 <b>(+35.70%)</b></td><td>239.20 (+9.83%)</td><td>174.60 (-3.35%)</td><td>184.90 (+0.16%)</td><td>126.90 (-3.72%)</td><td>45.93 <b>(+41.03%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.99 (n/a)</td><td>0.75 (n/a)</td><td>0.71 (n/a)</td><td>0.60 (n/a)</td><td>0.15 (n/a)</td><td>217.80 (n/a)</td><td>180.66 (n/a)</td><td>184.60 (n/a)</td><td>131.80 (n/a)</td><td>32.56 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>1.07 (+18.68%)</td><td>0.75 (+2.77%)</td><td>0.68 (-7.56%)</td><td>0.63 (+5.18%)</td><td>0.18 <b>(+50.62%)</b></td><td>208.40 (-4.93%)</td><td>181.64 (-1.14%)</td><td>191.50 (+8.13%)</td><td>122.70 (-15.73%)</td><td>34.53 (+15.87%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.90 (n/a)</td><td>0.73 (n/a)</td><td>0.74 (n/a)</td><td>0.60 (n/a)</td><td>0.12 (n/a)</td><td>219.20 (n/a)</td><td>183.74 (n/a)</td><td>177.10 (n/a)</td><td>145.60 (n/a)</td><td>29.80 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.69 (-12.18%)</td><td>0.62 (-6.93%)</td><td>0.64 (+4.89%)</td><td>0.50 (-12.10%)</td><td>0.08 <b>(-23.49%)</b></td><td>263.80 (+13.76%)</td><td>214.88 (+6.96%)</td><td>206.30 (-4.67%)</td><td>189.00 (+13.86%)</td><td>30.59 (+0.76%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.79 (n/a)</td><td>0.67 (n/a)</td><td>0.61 (n/a)</td><td>0.57 (n/a)</td><td>0.11 (n/a)</td><td>231.90 (n/a)</td><td>200.90 (n/a)</td><td>216.40 (n/a)</td><td>166.00 (n/a)</td><td>30.36 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.00 (-2.27%)</td><td>0.00 (-3.70%)</td><td>0.00 (-2.33%)</td><td>0.00 (-9.30%)</td><td>0.00 <b>(+274.17%)</b></td><td>1060.23 (+10.69%)</td><td>983.32 (+3.97%)</td><td>969.05 (+2.78%)</td><td>943.14 (+0.20%)</td><td>48.25 <b>(+597.75%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>957.84 (n/a)</td><td>945.73 (n/a)</td><td>942.84 (n/a)</td><td>941.27 (n/a)</td><td>6.92 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.01 (-1.19%)</td><td>0.01 (-0.50%)</td><td>0.01 (+0.00%)</td><td>0.01 (-1.32%)</td><td>0.00 (+5.81%)</td><td>1090.38 (+1.57%)</td><td>1020.62 (+0.39%)</td><td>1002.73 (-0.17%)</td><td>992.37 (+1.66%)</td><td>40.33 (+11.22%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1073.53 (n/a)</td><td>1016.68 (n/a)</td><td>1004.39 (n/a)</td><td>976.21 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.94 (-1.67%)</td><td>0.94 (-0.53%)</td><td>0.94 (-0.67%)</td><td>0.94 (+1.45%)</td><td>0.00 <b>(-78.38%)</b></td><td>2241.43 (-1.43%)</td><td>2234.40 (+0.52%)</td><td>2233.72 (+0.68%)</td><td>2225.34 (+1.69%)</td><td>6.87 <b>(-78.53%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.95 (n/a)</td><td>0.92 (n/a)</td><td>0.01 (n/a)</td><td>2274.04 (n/a)</td><td>2222.86 (n/a)</td><td>2218.69 (n/a)</td><td>2188.25 (n/a)</td><td>32.01 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>3.01 (-9.97%)</td><td>2.70 (-12.36%)</td><td>2.82 (-13.46%)</td><td>2.19 (-13.33%)</td><td>0.34 (-1.92%)</td><td>239.90 (+15.39%)</td><td>196.92 (+14.41%)</td><td>186.10 (+15.59%)</td><td>174.30 (+11.09%)</td><td>26.92 <b>(+25.83%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>3.34 (n/a)</td><td>3.08 (n/a)</td><td>3.26 (n/a)</td><td>2.52 (n/a)</td><td>0.34 (n/a)</td><td>207.90 (n/a)</td><td>172.12 (n/a)</td><td>161.00 (n/a)</td><td>156.90 (n/a)</td><td>21.40 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>6.17 (+3.43%)</td><td>5.10 (-4.14%)</td><td>4.69 (-15.04%)</td><td>4.44 (-6.14%)</td><td>0.80 <b>(+44.89%)</b></td><td>236.40 (+6.53%)</td><td>209.58 (+5.37%)</td><td>223.80 (+17.73%)</td><td>169.90 (-3.30%)</td><td>31.15 <b>(+47.49%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>5.97 (n/a)</td><td>5.32 (n/a)</td><td>5.51 (n/a)</td><td>4.73 (n/a)</td><td>0.56 (n/a)</td><td>221.90 (n/a)</td><td>198.90 (n/a)</td><td>190.10 (n/a)</td><td>175.70 (n/a)</td><td>21.12 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>3.51 (-5.93%)</td><td>2.81 (-13.63%)</td><td>2.76 (-17.35%)</td><td>2.34 (-16.75%)</td><td>0.43 (+4.78%)</td><td>224.30 <b>(+20.14%)</b></td><td>189.64 (+16.27%)</td><td>190.20 <b>(+20.99%)</b></td><td>149.20 (+6.27%)</td><td>26.76 <b>(+28.60%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:35:33</td><td>3.73 (n/a)</td><td>3.26 (n/a)</td><td>3.33 (n/a)</td><td>2.81 (n/a)</td><td>0.41 (n/a)</td><td>186.70 (n/a)</td><td>163.10 (n/a)</td><td>157.20 (n/a)</td><td>140.40 (n/a)</td><td>20.81 (n/a)</td>
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
