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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.11 <b>(+43.35%)</b></td><td>0.09 <b>(+35.03%)</b></td><td>0.08 <b>(+32.05%)</b></td><td>0.08 <b>(+38.81%)</b></td><td>0.02 <b>(+67.39%)</b></td><td>162.20 <b>(-27.94%)</b></td><td>138.56 <b>(-25.41%)</b></td><td>144.90 <b>(-24.29%)</b></td><td>108.70 <b>(-30.28%)</b></td><td>23.44 (-14.58%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.10 (n/a)</td><td>185.76 (n/a)</td><td>191.40 (n/a)</td><td>155.90 (n/a)</td><td>27.44 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.10 (+7.18%)</td><td>0.09 <b>(+36.33%)</b></td><td>0.09 <b>(+47.93%)</b></td><td>0.07 <b>(+39.75%)</b></td><td>0.01 <b>(-35.48%)</b></td><td>169.50 <b>(-28.42%)</b></td><td>143.70 <b>(-28.74%)</b></td><td>136.60 <b>(-32.41%)</b></td><td>126.90 (-6.76%)</td><td>17.80 <b>(-56.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>236.80 (n/a)</td><td>201.66 (n/a)</td><td>202.10 (n/a)</td><td>136.10 (n/a)</td><td>40.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.09 (-5.81%)</td><td>0.07 <b>(+24.99%)</b></td><td>0.07 <b>(+36.26%)</b></td><td>0.06 <b>(+58.38%)</b></td><td>0.01 <b>(-44.29%)</b></td><td>217.70 <b>(-36.88%)</b></td><td>173.10 <b>(-26.47%)</b></td><td>172.20 <b>(-26.60%)</b></td><td>130.50 (+6.18%)</td><td>30.96 <b>(-60.63%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>344.90 (n/a)</td><td>235.42 (n/a)</td><td>234.60 (n/a)</td><td>122.90 (n/a)</td><td>78.64 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.08 <b>(+55.87%)</b></td><td>0.07 <b>(+35.06%)</b></td><td>0.07 <b>(+36.07%)</b></td><td>0.04 (+10.72%)</td><td>0.02 <b>(+154.19%)</b></td><td>299.40 (-9.68%)</td><td>201.00 <b>(-22.52%)</b></td><td>180.60 <b>(-26.50%)</b></td><td>144.90 <b>(-35.83%)</b></td><td>60.75 <b>(+46.03%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>331.50 (n/a)</td><td>259.42 (n/a)</td><td>245.70 (n/a)</td><td>225.80 (n/a)</td><td>41.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 <b>(+53.52%)</b></td><td>0.03 <b>(+20.72%)</b></td><td>0.03 (+13.25%)</td><td>0.03 (+8.31%)</td><td>0.01 <b>(+236.65%)</b></td><td>199.00 (-7.70%)</td><td>161.82 (-14.24%)</td><td>158.20 (-11.72%)</td><td>113.80 <b>(-34.86%)</b></td><td>34.89 <b>(+105.15%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.60 (n/a)</td><td>188.70 (n/a)</td><td>179.20 (n/a)</td><td>174.70 (n/a)</td><td>17.01 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (-13.52%)</td><td>0.03 (-2.78%)</td><td>0.03 (+0.13%)</td><td>0.03 (+12.54%)</td><td>0.00 <b>(-50.59%)</b></td><td>182.20 (-11.17%)</td><td>161.62 (+0.57%)</td><td>163.70 (-0.12%)</td><td>139.40 (+15.59%)</td><td>15.72 <b>(-49.23%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>160.70 (n/a)</td><td>163.90 (n/a)</td><td>120.60 (n/a)</td><td>30.97 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (-10.20%)</td><td>0.03 <b>(+21.10%)</b></td><td>0.03 <b>(+28.74%)</b></td><td>0.03 <b>(+90.33%)</b></td><td>0.00 <b>(-63.62%)</b></td><td>191.40 <b>(-47.46%)</b></td><td>160.46 <b>(-25.80%)</b></td><td>152.30 <b>(-22.34%)</b></td><td>143.30 (+11.34%)</td><td>18.69 <b>(-79.14%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>364.30 (n/a)</td><td>216.26 (n/a)</td><td>196.10 (n/a)</td><td>128.70 (n/a)</td><td>89.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 <b>(+29.09%)</b></td><td>0.03 (+10.94%)</td><td>0.03 (+2.29%)</td><td>0.03 (-3.63%)</td><td>0.01 <b>(+94.57%)</b></td><td>197.80 (+3.72%)</td><td>156.26 (-7.84%)</td><td>163.90 (-2.27%)</td><td>115.90 <b>(-22.53%)</b></td><td>31.44 <b>(+54.10%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.70 (n/a)</td><td>169.56 (n/a)</td><td>167.70 (n/a)</td><td>149.60 (n/a)</td><td>20.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (-7.38%)</td><td>0.03 (+4.83%)</td><td>0.03 (+8.55%)</td><td>0.03 (+4.86%)</td><td>0.00 <b>(-25.32%)</b></td><td>205.50 (-4.64%)</td><td>159.38 (-5.85%)</td><td>150.80 (-7.88%)</td><td>135.00 (+8.00%)</td><td>27.05 <b>(-20.22%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>169.28 (n/a)</td><td>163.70 (n/a)</td><td>125.00 (n/a)</td><td>33.90 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (+18.57%)</td><td>0.03 (+11.94%)</td><td>0.03 <b>(+21.01%)</b></td><td>0.03 (+9.59%)</td><td>0.00 <b>(+29.85%)</b></td><td>183.40 (-8.76%)</td><td>161.18 (-10.34%)</td><td>158.20 (-17.39%)</td><td>128.30 (-15.65%)</td><td>22.00 (+0.45%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.00 (n/a)</td><td>179.76 (n/a)</td><td>191.50 (n/a)</td><td>152.10 (n/a)</td><td>21.90 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.03 (+0.02%)</td><td>0.03 (+17.92%)</td><td>0.03 <b>(+32.60%)</b></td><td>0.03 <b>(+24.44%)</b></td><td>0.00 <b>(-56.67%)</b></td><td>176.30 (-19.64%)</td><td>161.12 (-16.58%)</td><td>155.00 <b>(-24.57%)</b></td><td>153.40 (+0.00%)</td><td>9.90 <b>(-65.63%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.40 (n/a)</td><td>193.14 (n/a)</td><td>205.50 (n/a)</td><td>153.40 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.03 (-6.63%)</td><td>0.03 (+6.26%)</td><td>0.03 <b>(+23.38%)</b></td><td>0.02 (+5.49%)</td><td>0.01 (-9.27%)</td><td>281.60 (-5.22%)</td><td>204.14 (-6.55%)</td><td>177.10 (-18.95%)</td><td>169.60 (+7.14%)</td><td>47.82 (-9.07%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>297.10 (n/a)</td><td>218.46 (n/a)</td><td>218.50 (n/a)</td><td>158.30 (n/a)</td><td>52.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>176.30 (n/a)</td><td>149.68 (n/a)</td><td>139.00 (n/a)</td><td>135.30 (n/a)</td><td>17.87 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>260.60 (n/a)</td><td>173.26 (n/a)</td><td>156.70 (n/a)</td><td>133.00 (n/a)</td><td>50.06 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>169.16 (n/a)</td><td>169.90 (n/a)</td><td>134.40 (n/a)</td><td>34.77 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>185.10 (n/a)</td><td>179.54 (n/a)</td><td>179.00 (n/a)</td><td>172.90 (n/a)</td><td>4.88 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>169.74 (n/a)</td><td>159.50 (n/a)</td><td>128.20 (n/a)</td><td>35.33 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.20 (n/a)</td><td>191.28 (n/a)</td><td>193.20 (n/a)</td><td>149.10 (n/a)</td><td>28.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>255.20 (n/a)</td><td>190.82 (n/a)</td><td>173.70 (n/a)</td><td>165.10 (n/a)</td><td>36.87 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.00 (n/a)</td><td>192.72 (n/a)</td><td>197.70 (n/a)</td><td>165.30 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>176.14 (n/a)</td><td>180.20 (n/a)</td><td>118.00 (n/a)</td><td>38.64 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>310.90 (n/a)</td><td>204.12 (n/a)</td><td>173.80 (n/a)</td><td>155.00 (n/a)</td><td>64.28 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>177.84 (n/a)</td><td>184.40 (n/a)</td><td>125.40 (n/a)</td><td>31.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.50 (n/a)</td><td>200.92 (n/a)</td><td>200.40 (n/a)</td><td>146.30 (n/a)</td><td>41.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.60 (n/a)</td><td>196.04 (n/a)</td><td>187.70 (n/a)</td><td>163.30 (n/a)</td><td>28.05 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>198.14 (n/a)</td><td>191.90 (n/a)</td><td>171.30 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>238.50 (n/a)</td><td>224.58 (n/a)</td><td>234.10 (n/a)</td><td>190.40 (n/a)</td><td>20.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>372.50 (n/a)</td><td>246.00 (n/a)</td><td>211.00 (n/a)</td><td>187.10 (n/a)</td><td>75.19 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>4.83 (+15.15%)</td><td>4.14 (+9.23%)</td><td>4.08 (+12.33%)</td><td>3.64 (+5.17%)</td><td>0.43 <b>(+32.53%)</b></td><td>2585.70 (-4.91%)</td><td>2289.20 (-8.22%)</td><td>2302.50 (-10.97%)</td><td>1948.50 (-13.15%)</td><td>226.27 (+8.75%)</td><td>1898.58 (+15.15%)</td><td>1629.28 (+9.23%)</td><td>1606.68 (+12.33%)</td><td>1430.70 (+5.17%)</td><td>168.60 <b>(+32.53%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>4.19 (n/a)</td><td>3.79 (n/a)</td><td>3.64 (n/a)</td><td>3.46 (n/a)</td><td>0.32 (n/a)</td><td>2719.30 (n/a)</td><td>2494.36 (n/a)</td><td>2586.30 (n/a)</td><td>2243.60 (n/a)</td><td>208.07 (n/a)</td><td>1648.86 (n/a)</td><td>1491.57 (n/a)</td><td>1430.35 (n/a)</td><td>1360.42 (n/a)</td><td>127.22 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.08 (-4.76%)</td><td>0.95 (-0.75%)</td><td>1.03 (-1.01%)</td><td>0.73 (+14.96%)</td><td>0.15 <b>(-25.78%)</b></td><td>304.30 (-13.03%)</td><td>236.76 (-1.43%)</td><td>214.40 (+1.04%)</td><td>204.60 (+4.98%)</td><td>41.14 <b>(-34.54%)</b></td><td>46.12 (-4.76%)</td><td>40.72 (-0.75%)</td><td>44.03 (-1.01%)</td><td>31.01 (+14.96%)</td><td>6.20 <b>(-25.78%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>1.13 (n/a)</td><td>0.96 (n/a)</td><td>1.04 (n/a)</td><td>0.63 (n/a)</td><td>0.20 (n/a)</td><td>349.90 (n/a)</td><td>240.20 (n/a)</td><td>212.20 (n/a)</td><td>194.90 (n/a)</td><td>62.84 (n/a)</td><td>48.43 (n/a)</td><td>41.02 (n/a)</td><td>44.48 (n/a)</td><td>26.97 (n/a)</td><td>8.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.24 <b>(+21.44%)</b></td><td>1.04 <b>(+31.01%)</b></td><td>1.15 <b>(+36.64%)</b></td><td>0.79 <b>(+37.96%)</b></td><td>0.21 (+14.96%)</td><td>279.40 <b>(-27.50%)</b></td><td>219.98 <b>(-24.41%)</b></td><td>191.90 <b>(-26.78%)</b></td><td>178.70 (-17.69%)</td><td>48.38 <b>(-32.15%)</b></td><td>52.80 <b>(+21.44%)</b></td><td>44.50 <b>(+31.01%)</b></td><td>49.19 <b>(+36.64%)</b></td><td>33.78 <b>(+37.96%)</b></td><td>9.09 (+14.96%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>1.02 (n/a)</td><td>0.80 (n/a)</td><td>0.84 (n/a)</td><td>0.57 (n/a)</td><td>0.19 (n/a)</td><td>385.40 (n/a)</td><td>291.02 (n/a)</td><td>262.10 (n/a)</td><td>217.10 (n/a)</td><td>71.30 (n/a)</td><td>43.48 (n/a)</td><td>33.96 (n/a)</td><td>36.00 (n/a)</td><td>24.49 (n/a)</td><td>7.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.52 (-0.01%)</td><td>0.52 (+0.01%)</td><td>0.52 (+0.06%)</td><td>0.51 (-0.14%)</td><td>0.00 <b>(+50.06%)</b></td><td>48871.80 (+0.14%)</td><td>48678.42 (-0.01%)</td><td>48624.50 (-0.06%)</td><td>48621.10 (+0.01%)</td><td>108.75 <b>(+50.29%)</b></td><td>353.34 (-0.01%)</td><td>352.93 (+0.01%)</td><td>353.32 (+0.06%)</td><td>351.53 (-0.14%)</td><td>0.79 <b>(+50.07%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48802.80 (n/a)</td><td>48684.34 (n/a)</td><td>48654.80 (n/a)</td><td>48616.00 (n/a)</td><td>72.36 (n/a)</td><td>353.38 (n/a)</td><td>352.88 (n/a)</td><td>353.10 (n/a)</td><td>352.03 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.90 (+1.32%)</td><td>0.89 (+1.51%)</td><td>0.89 (+1.77%)</td><td>0.89 (+1.86%)</td><td>0.00 <b>(-34.51%)</b></td><td>28368.30 (-1.83%)</td><td>28195.36 (-1.49%)</td><td>28173.30 (-1.74%)</td><td>28035.80 (-1.31%)</td><td>134.12 <b>(-36.44%)</b></td><td>612.78 (+1.32%)</td><td>609.33 (+1.51%)</td><td>609.79 (+1.77%)</td><td>605.60 (+1.86%)</td><td>2.90 <b>(-34.51%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28896.60 (n/a)</td><td>28622.80 (n/a)</td><td>28671.20 (n/a)</td><td>28407.10 (n/a)</td><td>211.00 (n/a)</td><td>604.77 (n/a)</td><td>600.24 (n/a)</td><td>599.20 (n/a)</td><td>594.53 (n/a)</td><td>4.42 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>3.27 (-5.48%)</td><td>3.18 (-3.26%)</td><td>3.16 (-2.69%)</td><td>3.12 (-0.59%)</td><td>0.06 <b>(-51.37%)</b></td><td>8054.00 (+0.59%)</td><td>7921.82 (+3.29%)</td><td>7956.00 (+2.77%)</td><td>7695.90 (+5.80%)</td><td>142.85 <b>(-48.14%)</b></td><td>2232.33 (-5.48%)</td><td>2169.24 (-3.26%)</td><td>2159.37 (-2.69%)</td><td>2133.08 (-0.59%)</td><td>39.62 <b>(-51.37%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>3.46 (n/a)</td><td>3.28 (n/a)</td><td>3.25 (n/a)</td><td>3.14 (n/a)</td><td>0.12 (n/a)</td><td>8006.50 (n/a)</td><td>7669.62 (n/a)</td><td>7741.70 (n/a)</td><td>7274.30 (n/a)</td><td>275.44 (n/a)</td><td>2361.74 (n/a)</td><td>2242.33 (n/a)</td><td>2219.14 (n/a)</td><td>2145.73 (n/a)</td><td>81.49 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>4.23 (+1.59%)</td><td>3.36 (-2.42%)</td><td>3.07 (-13.38%)</td><td>2.79 (-4.87%)</td><td>0.60 (+18.57%)</td><td>2893.70 (+5.11%)</td><td>2459.64 (+3.19%)</td><td>2623.30 (+15.45%)</td><td>1906.00 (-1.56%)</td><td>405.23 (+19.64%)</td><td>1109.10 (+1.59%)</td><td>879.94 (-2.42%)</td><td>805.84 (-13.38%)</td><td>730.53 (-4.87%)</td><td>156.30 (+18.57%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>4.16 (n/a)</td><td>3.44 (n/a)</td><td>3.55 (n/a)</td><td>2.93 (n/a)</td><td>0.50 (n/a)</td><td>2752.90 (n/a)</td><td>2383.62 (n/a)</td><td>2272.30 (n/a)</td><td>1936.30 (n/a)</td><td>338.71 (n/a)</td><td>1091.76 (n/a)</td><td>901.76 (n/a)</td><td>930.31 (n/a)</td><td>767.90 (n/a)</td><td>131.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.51 (+14.62%)</td><td>0.43 <b>(+20.19%)</b></td><td>0.42 <b>(+20.23%)</b></td><td>0.35 (+11.57%)</td><td>0.08 <b>(+38.34%)</b></td><td>3594.80 (-10.37%)</td><td>2993.74 (-16.08%)</td><td>2979.60 (-16.83%)</td><td>2423.30 (-12.76%)</td><td>535.05 (+8.83%)</td><td>27.69 (+14.62%)</td><td>23.01 <b>(+20.19%)</b></td><td>22.52 <b>(+20.23%)</b></td><td>18.67 (+11.57%)</td><td>4.13 <b>(+38.34%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.45 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.06 (n/a)</td><td>4010.80 (n/a)</td><td>3567.18 (n/a)</td><td>3582.40 (n/a)</td><td>2777.60 (n/a)</td><td>491.63 (n/a)</td><td>24.16 (n/a)</td><td>19.14 (n/a)</td><td>18.73 (n/a)</td><td>16.73 (n/a)</td><td>2.99 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>6.60 <b>(+36.81%)</b></td><td>5.05 (+14.74%)</td><td>4.75 (+0.42%)</td><td>3.77 (-0.44%)</td><td>1.27 <b>(+140.35%)</b></td><td>1764.50 (+0.44%)</td><td>1383.66 (-9.49%)</td><td>1400.40 (-0.42%)</td><td>1007.60 <b>(-26.91%)</b></td><td>337.68 <b>(+76.11%)</b></td><td>2039.66 <b>(+36.81%)</b></td><td>1561.31 (+14.74%)</td><td>1467.54 (+0.42%)</td><td>1164.78 (-0.44%)</td><td>392.21 <b>(+140.35%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>4.83 (n/a)</td><td>4.40 (n/a)</td><td>4.73 (n/a)</td><td>3.79 (n/a)</td><td>0.53 (n/a)</td><td>1756.70 (n/a)</td><td>1528.78 (n/a)</td><td>1406.30 (n/a)</td><td>1378.50 (n/a)</td><td>191.74 (n/a)</td><td>1490.90 (n/a)</td><td>1360.72 (n/a)</td><td>1461.40 (n/a)</td><td>1169.90 (n/a)</td><td>163.19 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.25 (+7.72%)</td><td>0.21 (+3.88%)</td><td>0.19 (+0.45%)</td><td>0.18 (+10.87%)</td><td>0.03 (+5.93%)</td><td>0.25 (+7.72%)</td><td>0.20 (+3.88%)</td><td>0.19 (+0.45%)</td><td>0.17 (+10.87%)</td><td>0.03 (+5.93%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>13.45 (+0.59%)</td><td>12.50 (+2.57%)</td><td>12.60 (+5.28%)</td><td>10.94 (+3.30%)</td><td>1.02 (-10.78%)</td><td>13.44 (+0.59%)</td><td>12.49 (+2.57%)</td><td>12.59 (+5.28%)</td><td>10.93 (+3.30%)</td><td>1.02 (-10.78%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>13.37 (n/a)</td><td>12.19 (n/a)</td><td>11.97 (n/a)</td><td>10.59 (n/a)</td><td>1.15 (n/a)</td><td>13.36 (n/a)</td><td>12.18 (n/a)</td><td>11.96 (n/a)</td><td>10.58 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>25.81 (+4.08%)</td><td>24.75 (+3.60%)</td><td>25.02 (+4.33%)</td><td>23.65 (+3.36%)</td><td>0.86 <b>(+23.99%)</b></td><td>25.80 (+4.08%)</td><td>24.73 (+3.60%)</td><td>25.00 (+4.33%)</td><td>23.64 (+3.36%)</td><td>0.85 <b>(+23.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>24.80 (n/a)</td><td>23.89 (n/a)</td><td>23.98 (n/a)</td><td>22.89 (n/a)</td><td>0.69 (n/a)</td><td>24.78 (n/a)</td><td>23.88 (n/a)</td><td>23.97 (n/a)</td><td>22.87 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>42.73 (+0.26%)</td><td>40.29 (+0.99%)</td><td>40.67 (+4.06%)</td><td>36.93 (-3.71%)</td><td>2.10 <b>(+22.61%)</b></td><td>42.71 (+0.26%)</td><td>40.27 (+0.99%)</td><td>40.64 (+4.06%)</td><td>36.91 (-3.71%)</td><td>2.10 <b>(+22.61%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>42.62 (n/a)</td><td>39.90 (n/a)</td><td>39.08 (n/a)</td><td>38.35 (n/a)</td><td>1.71 (n/a)</td><td>42.59 (n/a)</td><td>39.87 (n/a)</td><td>39.05 (n/a)</td><td>38.33 (n/a)</td><td>1.71 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>45.53 (+3.38%)</td><td>41.22 (-3.75%)</td><td>45.19 (+5.85%)</td><td>26.80 <b>(-34.77%)</b></td><td>8.11 <b>(+599.32%)</b></td><td>45.50 (+3.38%)</td><td>41.20 (-3.75%)</td><td>45.16 (+5.85%)</td><td>26.78 <b>(-34.77%)</b></td><td>8.10 <b>(+599.32%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>44.04 (n/a)</td><td>42.83 (n/a)</td><td>42.69 (n/a)</td><td>41.08 (n/a)</td><td>1.16 (n/a)</td><td>44.01 (n/a)</td><td>42.81 (n/a)</td><td>42.67 (n/a)</td><td>41.06 (n/a)</td><td>1.16 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>13.40 (+0.18%)</td><td>12.43 (-1.64%)</td><td>12.56 (-1.52%)</td><td>10.47 (-8.16%)</td><td>1.17 <b>(+49.24%)</b></td><td>13.39 (+0.18%)</td><td>12.42 (-1.64%)</td><td>12.56 (-1.52%)</td><td>10.46 (-8.16%)</td><td>1.17 <b>(+49.24%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>13.38 (n/a)</td><td>12.64 (n/a)</td><td>12.76 (n/a)</td><td>11.40 (n/a)</td><td>0.79 (n/a)</td><td>13.37 (n/a)</td><td>12.63 (n/a)</td><td>12.75 (n/a)</td><td>11.39 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>25.31 (+3.04%)</td><td>24.79 (+3.56%)</td><td>25.01 (+4.69%)</td><td>24.06 (+2.47%)</td><td>0.50 <b>(+22.74%)</b></td><td>25.30 (+3.04%)</td><td>24.77 (+3.56%)</td><td>25.00 (+4.69%)</td><td>24.05 (+2.47%)</td><td>0.49 <b>(+22.74%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>24.57 (n/a)</td><td>23.93 (n/a)</td><td>23.89 (n/a)</td><td>23.48 (n/a)</td><td>0.40 (n/a)</td><td>24.55 (n/a)</td><td>23.92 (n/a)</td><td>23.88 (n/a)</td><td>23.47 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>41.99 (+2.67%)</td><td>39.80 (+0.32%)</td><td>39.57 (+0.06%)</td><td>37.26 (-3.49%)</td><td>1.80 <b>(+84.21%)</b></td><td>41.97 (+2.67%)</td><td>39.77 (+0.32%)</td><td>39.55 (+0.06%)</td><td>37.24 (-3.49%)</td><td>1.80 <b>(+84.21%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>40.90 (n/a)</td><td>39.67 (n/a)</td><td>39.55 (n/a)</td><td>38.61 (n/a)</td><td>0.98 (n/a)</td><td>40.88 (n/a)</td><td>39.65 (n/a)</td><td>39.52 (n/a)</td><td>38.58 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>45.45 (-3.99%)</td><td>43.44 (+1.99%)</td><td>44.33 (+4.41%)</td><td>40.97 (+5.13%)</td><td>2.27 <b>(-25.17%)</b></td><td>45.43 (-3.99%)</td><td>43.41 (+1.99%)</td><td>44.31 (+4.41%)</td><td>40.95 (+5.13%)</td><td>2.27 <b>(-25.17%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>47.34 (n/a)</td><td>42.59 (n/a)</td><td>42.46 (n/a)</td><td>38.97 (n/a)</td><td>3.04 (n/a)</td><td>47.31 (n/a)</td><td>42.57 (n/a)</td><td>42.43 (n/a)</td><td>38.95 (n/a)</td><td>3.04 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>9.21 (-3.99%)</td><td>8.53 (-1.26%)</td><td>8.56 (-2.20%)</td><td>7.98 (+5.77%)</td><td>0.45 <b>(-42.96%)</b></td><td>9.19 (-3.99%)</td><td>8.51 (-1.26%)</td><td>8.54 (-2.20%)</td><td>7.97 (+5.77%)</td><td>0.45 <b>(-42.96%)</b></td>
</tr>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.79 (-2.06%)</td><td>0.69 (-12.84%)</td><td>0.64 (-18.99%)</td><td>0.61 (-19.94%)</td><td>0.08 <b>(+285.68%)</b></td><td>0.78 (-2.06%)</td><td>0.68 (-12.84%)</td><td>0.63 (-18.99%)</td><td>0.60 (-19.94%)</td><td>0.08 <b>(+285.68%)</b></td>
</tr>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.23 (+8.15%)</td><td>1.04 (+3.30%)</td><td>1.03 (+4.62%)</td><td>0.88 (-4.59%)</td><td>0.14 <b>(+50.56%)</b></td><td>1.22 (+8.15%)</td><td>1.03 (+3.30%)</td><td>1.02 (+4.62%)</td><td>0.86 (-4.59%)</td><td>0.14 <b>(+50.56%)</b></td>
</tr>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>15.30 (-9.02%)</td><td>14.14 (-6.32%)</td><td>14.58 (+1.08%)</td><td>11.45 (-17.87%)</td><td>1.53 <b>(+20.60%)</b></td><td>15.12 (-9.02%)</td><td>13.98 (-6.32%)</td><td>14.41 (+1.08%)</td><td>11.32 (-17.87%)</td><td>1.51 <b>(+20.60%)</b></td>
</tr>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>12.65 (+4.35%)</td><td>10.52 (-6.38%)</td><td>11.53 (-0.22%)</td><td>6.33 <b>(-38.63%)</b></td><td>2.50 <b>(+214.33%)</b></td><td>12.43 (+4.35%)</td><td>10.34 (-6.38%)</td><td>11.33 (-0.22%)</td><td>6.21 <b>(-38.63%)</b></td><td>2.45 <b>(+214.33%)</b></td>
</tr>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>7.37 (-5.05%)</td><td>6.71 (-2.11%)</td><td>6.70 (-11.04%)</td><td>6.01 (+19.84%)</td><td>0.49 <b>(-58.51%)</b></td><td>7.25 (-5.05%)</td><td>6.59 (-2.11%)</td><td>6.58 (-11.04%)</td><td>5.91 (+19.84%)</td><td>0.48 <b>(-58.51%)</b></td>
</tr>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>5.49 (-10.58%)</td><td>4.98 (-7.19%)</td><td>4.96 (-6.16%)</td><td>4.37 (-9.04%)</td><td>0.50 (+3.83%)</td><td>5.40 (-10.58%)</td><td>4.90 (-7.19%)</td><td>4.88 (-6.16%)</td><td>4.30 (-9.04%)</td><td>0.49 (+3.83%)</td>
</tr>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.90 (n/a)</td><td>167.86 (n/a)</td><td>187.00 (n/a)</td><td>131.60 (n/a)</td><td>28.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.70 (n/a)</td><td>185.90 (n/a)</td><td>181.20 (n/a)</td><td>159.60 (n/a)</td><td>21.44 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.30 (n/a)</td><td>166.12 (n/a)</td><td>170.50 (n/a)</td><td>138.20 (n/a)</td><td>17.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>187.02 (n/a)</td><td>197.00 (n/a)</td><td>128.40 (n/a)</td><td>39.23 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.20 (n/a)</td><td>196.28 (n/a)</td><td>187.10 (n/a)</td><td>166.30 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.20 (n/a)</td><td>190.60 (n/a)</td><td>177.90 (n/a)</td><td>155.40 (n/a)</td><td>32.12 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>223.00 (n/a)</td><td>203.08 (n/a)</td><td>210.60 (n/a)</td><td>179.60 (n/a)</td><td>20.33 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.30 (n/a)</td><td>190.42 (n/a)</td><td>177.30 (n/a)</td><td>170.20 (n/a)</td><td>23.63 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (+17.20%)</td><td>0.05 (+14.16%)</td><td>0.05 (+10.71%)</td><td>0.04 <b>(+24.08%)</b></td><td>0.01 (-15.15%)</td><td>188.00 (-19.38%)</td><td>165.68 (-13.43%)</td><td>169.30 (-9.66%)</td><td>135.80 (-14.70%)</td><td>19.14 <b>(-41.79%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.20 (n/a)</td><td>191.38 (n/a)</td><td>187.40 (n/a)</td><td>159.20 (n/a)</td><td>32.88 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 <b>(+25.81%)</b></td><td>0.05 (+16.35%)</td><td>0.05 (+7.99%)</td><td>0.04 (+6.41%)</td><td>0.01 <b>(+103.66%)</b></td><td>185.70 (-6.02%)</td><td>153.70 (-12.64%)</td><td>158.50 (-7.42%)</td><td>123.30 <b>(-20.55%)</b></td><td>26.46 <b>(+48.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.60 (n/a)</td><td>175.94 (n/a)</td><td>171.20 (n/a)</td><td>155.20 (n/a)</td><td>17.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (-6.04%)</td><td>0.05 (+7.28%)</td><td>0.05 (+4.63%)</td><td>0.05 <b>(+40.33%)</b></td><td>0.00 <b>(-74.35%)</b></td><td>160.20 <b>(-28.74%)</b></td><td>153.06 (-9.86%)</td><td>153.90 (-4.41%)</td><td>144.10 (+6.43%)</td><td>7.34 <b>(-80.18%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.80 (n/a)</td><td>169.80 (n/a)</td><td>161.00 (n/a)</td><td>135.40 (n/a)</td><td>37.04 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 <b>(-23.33%)</b></td><td>0.05 (-3.88%)</td><td>0.05 (-1.73%)</td><td>0.05 (+10.77%)</td><td>0.00 <b>(-89.68%)</b></td><td>171.50 (-9.74%)</td><td>167.34 (+1.90%)</td><td>166.80 (+1.71%)</td><td>163.10 <b>(+30.48%)</b></td><td>3.08 <b>(-87.67%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>164.22 (n/a)</td><td>164.00 (n/a)</td><td>125.00 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (+18.80%)</td><td>0.05 <b>(+27.09%)</b></td><td>0.05 <b>(+30.19%)</b></td><td>0.04 <b>(+67.53%)</b></td><td>0.01 <b>(-32.72%)</b></td><td>189.80 <b>(-40.31%)</b></td><td>160.50 <b>(-25.34%)</b></td><td>156.80 <b>(-23.17%)</b></td><td>128.70 (-15.83%)</td><td>22.40 <b>(-66.22%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>318.00 (n/a)</td><td>214.98 (n/a)</td><td>204.10 (n/a)</td><td>152.90 (n/a)</td><td>66.29 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (-13.76%)</td><td>0.04 (-9.84%)</td><td>0.04 (-0.55%)</td><td>0.03 (-16.67%)</td><td>0.01 (-2.98%)</td><td>291.40 <b>(+20.02%)</b></td><td>214.96 (+11.85%)</td><td>196.50 (+0.56%)</td><td>174.60 (+15.94%)</td><td>48.59 <b>(+35.21%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.80 (n/a)</td><td>192.18 (n/a)</td><td>195.40 (n/a)</td><td>150.60 (n/a)</td><td>35.93 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (-3.27%)</td><td>0.05 (+12.79%)</td><td>0.05 (+17.32%)</td><td>0.04 <b>(+20.54%)</b></td><td>0.00 <b>(-37.44%)</b></td><td>195.70 (-17.04%)</td><td>170.60 (-12.53%)</td><td>166.20 (-14.77%)</td><td>156.70 (+3.36%)</td><td>16.38 <b>(-45.85%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.90 (n/a)</td><td>195.04 (n/a)</td><td>195.00 (n/a)</td><td>151.60 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (-9.86%)</td><td>0.04 (-1.33%)</td><td>0.04 (+3.01%)</td><td>0.04 (+16.71%)</td><td>0.00 <b>(-66.68%)</b></td><td>215.20 (-14.33%)</td><td>199.00 (-0.79%)</td><td>196.90 (-2.96%)</td><td>184.30 (+10.96%)</td><td>11.44 <b>(-67.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.20 (n/a)</td><td>200.58 (n/a)</td><td>202.90 (n/a)</td><td>166.10 (n/a)</td><td>35.19 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (+6.19%)</td><td>0.04 (+16.32%)</td><td>0.04 (+9.85%)</td><td>0.04 <b>(+58.05%)</b></td><td>0.00 <b>(-77.28%)</b></td><td>197.60 <b>(-36.75%)</b></td><td>189.10 (-16.53%)</td><td>187.40 (-8.98%)</td><td>182.10 (-5.84%)</td><td>6.45 <b>(-86.85%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>312.40 (n/a)</td><td>226.56 (n/a)</td><td>205.90 (n/a)</td><td>193.40 (n/a)</td><td>49.05 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 <b>(+23.81%)</b></td><td>0.04 (+14.51%)</td><td>0.04 (+3.28%)</td><td>0.02 (+7.84%)</td><td>0.01 (+17.90%)</td><td>337.70 (-7.28%)</td><td>238.04 (-12.84%)</td><td>223.00 (-3.17%)</td><td>157.80 (-19.20%)</td><td>65.17 (-15.55%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>364.20 (n/a)</td><td>273.12 (n/a)</td><td>230.30 (n/a)</td><td>195.30 (n/a)</td><td>77.17 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (-10.64%)</td><td>0.05 (-11.82%)</td><td>0.05 (-7.01%)</td><td>0.04 <b>(-20.52%)</b></td><td>0.01 <b>(+23.81%)</b></td><td>212.20 <b>(+25.86%)</b></td><td>175.46 (+14.07%)</td><td>168.50 (+7.53%)</td><td>158.10 (+11.89%)</td><td>21.52 <b>(+80.62%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>168.60 (n/a)</td><td>153.82 (n/a)</td><td>156.70 (n/a)</td><td>141.30 (n/a)</td><td>11.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (+4.31%)</td><td>0.04 (-1.15%)</td><td>0.04 (-0.60%)</td><td>0.03 <b>(-20.84%)</b></td><td>0.01 <b>(+109.62%)</b></td><td>311.70 <b>(+26.30%)</b></td><td>227.54 (+3.74%)</td><td>215.30 (+0.61%)</td><td>188.60 (-4.17%)</td><td>49.13 <b>(+159.52%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>246.80 (n/a)</td><td>219.34 (n/a)</td><td>214.00 (n/a)</td><td>196.80 (n/a)</td><td>18.93 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (-18.68%)</td><td>0.04 <b>(-26.14%)</b></td><td>0.04 <b>(-33.58%)</b></td><td>0.03 <b>(-39.96%)</b></td><td>0.01 (+12.44%)</td><td>297.40 <b>(+66.61%)</b></td><td>205.12 <b>(+39.40%)</b></td><td>199.90 <b>(+50.53%)</b></td><td>158.80 <b>(+22.91%)</b></td><td>54.73 <b>(+139.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.50 (n/a)</td><td>147.14 (n/a)</td><td>132.80 (n/a)</td><td>129.20 (n/a)</td><td>22.85 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (-13.96%)</td><td>0.05 (-3.23%)</td><td>0.05 (+4.74%)</td><td>0.04 (-6.05%)</td><td>0.00 <b>(-37.63%)</b></td><td>189.50 (+6.46%)</td><td>169.80 (+2.81%)</td><td>162.90 (-4.51%)</td><td>157.50 (+16.24%)</td><td>13.54 <b>(-21.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.00 (n/a)</td><td>165.16 (n/a)</td><td>170.60 (n/a)</td><td>135.50 (n/a)</td><td>17.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (-7.51%)</td><td>0.05 (+1.12%)</td><td>0.05 (+5.05%)</td><td>0.04 (-2.54%)</td><td>0.00 <b>(-23.54%)</b></td><td>198.30 (+2.64%)</td><td>168.46 (-1.54%)</td><td>160.40 (-4.81%)</td><td>153.00 (+8.13%)</td><td>17.97 (-14.93%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>171.10 (n/a)</td><td>168.50 (n/a)</td><td>141.50 (n/a)</td><td>21.12 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (+3.01%)</td><td>0.04 (-14.87%)</td><td>0.04 (-12.99%)</td><td>0.03 <b>(-29.46%)</b></td><td>0.01 <b>(+261.57%)</b></td><td>259.50 <b>(+41.80%)</b></td><td>204.68 <b>(+20.53%)</b></td><td>192.50 (+14.93%)</td><td>159.70 (-2.92%)</td><td>38.20 <b>(+401.66%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>183.00 (n/a)</td><td>169.82 (n/a)</td><td>167.50 (n/a)</td><td>164.50 (n/a)</td><td>7.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (+5.13%)</td><td>0.04 (-8.14%)</td><td>0.04 (-6.35%)</td><td>0.03 <b>(-22.16%)</b></td><td>0.01 <b>(+56.59%)</b></td><td>256.70 <b>(+28.48%)</b></td><td>197.48 (+12.17%)</td><td>202.00 (+6.77%)</td><td>139.70 (-4.90%)</td><td>45.94 <b>(+91.22%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>176.06 (n/a)</td><td>189.20 (n/a)</td><td>146.90 (n/a)</td><td>24.02 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (-17.43%)</td><td>0.04 (-15.23%)</td><td>0.04 (-9.64%)</td><td>0.03 <b>(-29.99%)</b></td><td>0.01 <b>(+37.62%)</b></td><td>290.10 <b>(+42.84%)</b></td><td>214.04 <b>(+20.30%)</b></td><td>190.70 (+10.68%)</td><td>186.60 <b>(+21.09%)</b></td><td>44.08 <b>(+138.04%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>203.10 (n/a)</td><td>177.92 (n/a)</td><td>172.30 (n/a)</td><td>154.10 (n/a)</td><td>18.52 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.21 (+0.68%)</td><td>0.21 (+0.25%)</td><td>0.21 (+0.23%)</td><td>0.21 (+0.18%)</td><td>0.00 <b>(+116.48%)</b></td><td>40833.30 (-0.18%)</td><td>40741.08 (-0.25%)</td><td>40788.20 (-0.23%)</td><td>40478.90 (-0.67%)</td><td>147.99 <b>(+114.52%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40906.00 (n/a)</td><td>40844.16 (n/a)</td><td>40882.50 (n/a)</td><td>40753.10 (n/a)</td><td>68.98 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (+1.47%)</td><td>0.06 <b>(+21.50%)</b></td><td>0.06 <b>(+39.00%)</b></td><td>0.05 <b>(+34.56%)</b></td><td>0.01 (-17.29%)</td><td>170.30 <b>(-25.70%)</b></td><td>138.30 <b>(-20.00%)</b></td><td>126.50 <b>(-28.04%)</b></td><td>110.60 (-1.51%)</td><td>28.57 <b>(-37.06%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.20 (n/a)</td><td>172.88 (n/a)</td><td>175.80 (n/a)</td><td>112.30 (n/a)</td><td>45.39 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.10 (+7.39%)</td><td>0.08 (+4.28%)</td><td>0.08 (+18.22%)</td><td>0.06 (-7.03%)</td><td>0.02 <b>(+48.94%)</b></td><td>221.50 (+7.58%)</td><td>169.22 (-1.13%)</td><td>146.20 (-15.39%)</td><td>122.80 (-6.90%)</td><td>44.42 <b>(+57.20%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.90 (n/a)</td><td>171.16 (n/a)</td><td>172.80 (n/a)</td><td>131.90 (n/a)</td><td>28.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (-14.94%)</td><td>0.05 (+0.49%)</td><td>0.05 (+1.36%)</td><td>0.04 <b>(+39.19%)</b></td><td>0.01 <b>(-61.16%)</b></td><td>183.10 <b>(-28.14%)</b></td><td>166.96 (-5.86%)</td><td>169.80 (-1.34%)</td><td>140.40 (+17.59%)</td><td>16.48 <b>(-67.79%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.80 (n/a)</td><td>177.36 (n/a)</td><td>172.10 (n/a)</td><td>119.40 (n/a)</td><td>51.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.09 (+2.80%)</td><td>0.07 (+11.38%)</td><td>0.07 (+13.46%)</td><td>0.06 (+7.93%)</td><td>0.01 (+1.18%)</td><td>184.90 (-7.36%)</td><td>150.70 (-10.34%)</td><td>154.70 (-11.85%)</td><td>118.50 (-2.71%)</td><td>26.94 (-6.25%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>199.60 (n/a)</td><td>168.08 (n/a)</td><td>175.50 (n/a)</td><td>121.80 (n/a)</td><td>28.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 <b>(+21.42%)</b></td><td>0.05 (+2.51%)</td><td>0.05 (+4.80%)</td><td>0.03 <b>(-26.68%)</b></td><td>0.01 <b>(+112.15%)</b></td><td>275.50 <b>(+36.39%)</b></td><td>175.90 (+3.78%)</td><td>154.90 (-4.56%)</td><td>121.60 (-17.67%)</td><td>60.04 <b>(+150.36%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>169.50 (n/a)</td><td>162.30 (n/a)</td><td>147.70 (n/a)</td><td>23.98 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (-3.76%)</td><td>0.06 (+2.69%)</td><td>0.06 (+8.87%)</td><td>0.06 (+10.27%)</td><td>0.00 <b>(-42.47%)</b></td><td>184.60 (-9.33%)</td><td>170.28 (-3.51%)</td><td>165.10 (-8.12%)</td><td>155.20 (+3.88%)</td><td>12.59 <b>(-44.80%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>176.48 (n/a)</td><td>179.70 (n/a)</td><td>149.40 (n/a)</td><td>22.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (-1.47%)</td><td>0.05 (+6.22%)</td><td>0.05 (+12.51%)</td><td>0.04 (+1.49%)</td><td>0.01 (+8.84%)</td><td>209.80 (-1.46%)</td><td>163.54 (-5.06%)</td><td>165.30 (-11.08%)</td><td>119.90 (+1.44%)</td><td>40.05 (+10.42%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>172.26 (n/a)</td><td>185.90 (n/a)</td><td>118.20 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.08 (+10.16%)</td><td>0.06 (+16.67%)</td><td>0.05 (+13.67%)</td><td>0.05 <b>(+71.82%)</b></td><td>0.01 <b>(-28.44%)</b></td><td>182.10 <b>(-41.82%)</b></td><td>161.08 (-19.65%)</td><td>179.70 (-12.04%)</td><td>120.20 (-9.28%)</td><td>28.11 <b>(-60.64%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>313.00 (n/a)</td><td>200.48 (n/a)</td><td>204.30 (n/a)</td><td>132.50 (n/a)</td><td>71.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 <b>(+27.16%)</b></td><td>0.05 (+12.61%)</td><td>0.05 (+6.29%)</td><td>0.04 (-2.10%)</td><td>0.01 <b>(+155.08%)</b></td><td>182.80 (+2.12%)</td><td>155.66 (-9.20%)</td><td>165.60 (-5.91%)</td><td>116.20 <b>(-21.38%)</b></td><td>27.37 <b>(+106.04%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>179.00 (n/a)</td><td>171.44 (n/a)</td><td>176.00 (n/a)</td><td>147.80 (n/a)</td><td>13.29 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.08 (+15.61%)</td><td>0.05 (-1.96%)</td><td>0.05 (-13.20%)</td><td>0.04 (-12.26%)</td><td>0.01 <b>(+50.66%)</b></td><td>228.40 (+13.97%)</td><td>176.32 (+4.23%)</td><td>181.20 (+15.19%)</td><td>120.60 (-13.49%)</td><td>38.51 <b>(+39.54%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>169.16 (n/a)</td><td>157.30 (n/a)</td><td>139.40 (n/a)</td><td>27.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (+2.56%)</td><td>0.05 (+14.43%)</td><td>0.05 (+15.64%)</td><td>0.05 <b>(+36.95%)</b></td><td>0.00 <b>(-67.57%)</b></td><td>164.90 <b>(-27.00%)</b></td><td>158.56 (-13.99%)</td><td>161.70 (-13.53%)</td><td>150.30 (-2.53%)</td><td>6.33 <b>(-76.97%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>184.34 (n/a)</td><td>187.00 (n/a)</td><td>154.20 (n/a)</td><td>27.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (+2.21%)</td><td>0.05 (+4.85%)</td><td>0.05 (+11.05%)</td><td>0.04 (+6.82%)</td><td>0.01 (+4.02%)</td><td>204.40 (-6.37%)</td><td>176.80 (-4.62%)</td><td>163.00 (-9.94%)</td><td>157.30 (-2.12%)</td><td>22.32 (-4.43%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.30 (n/a)</td><td>185.36 (n/a)</td><td>181.00 (n/a)</td><td>160.70 (n/a)</td><td>23.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (+9.11%)</td><td>0.05 (+11.61%)</td><td>0.05 (+9.10%)</td><td>0.04 (+11.34%)</td><td>0.01 (+5.06%)</td><td>193.80 (-10.19%)</td><td>166.10 (-10.64%)</td><td>174.20 (-8.36%)</td><td>121.60 (-8.36%)</td><td>28.54 (-13.23%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.80 (n/a)</td><td>185.88 (n/a)</td><td>190.10 (n/a)</td><td>132.70 (n/a)</td><td>32.88 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (-10.72%)</td><td>0.04 (-7.79%)</td><td>0.04 (-7.57%)</td><td>0.04 (-2.13%)</td><td>0.00 <b>(-38.82%)</b></td><td>220.00 (+2.14%)</td><td>200.58 (+7.35%)</td><td>204.40 (+8.21%)</td><td>177.40 (+12.07%)</td><td>19.61 <b>(-29.38%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>186.84 (n/a)</td><td>188.90 (n/a)</td><td>158.30 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (-18.08%)</td><td>0.04 (-5.31%)</td><td>0.04 (+5.97%)</td><td>0.03 (-5.35%)</td><td>0.00 <b>(-54.34%)</b></td><td>236.60 (+5.67%)</td><td>210.04 (+4.15%)</td><td>206.80 (-5.61%)</td><td>192.30 <b>(+22.10%)</b></td><td>17.19 <b>(-41.82%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.90 (n/a)</td><td>201.68 (n/a)</td><td>219.10 (n/a)</td><td>157.50 (n/a)</td><td>29.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.66 (+4.88%)</td><td>0.53 (+9.42%)</td><td>0.50 (-3.16%)</td><td>0.46 <b>(+72.28%)</b></td><td>0.08 <b>(-39.79%)</b></td><td>212.10 <b>(-41.95%)</b></td><td>187.68 (-14.57%)</td><td>198.60 (+3.28%)</td><td>148.90 (-4.67%)</td><td>25.37 <b>(-69.44%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.63 (n/a)</td><td>0.49 (n/a)</td><td>0.51 (n/a)</td><td>0.27 (n/a)</td><td>0.13 (n/a)</td><td>365.40 (n/a)</td><td>219.70 (n/a)</td><td>192.30 (n/a)</td><td>156.20 (n/a)</td><td>83.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.78 <b>(+39.66%)</b></td><td>0.62 <b>(+24.59%)</b></td><td>0.59 (+12.90%)</td><td>0.48 (+12.10%)</td><td>0.14 <b>(+154.87%)</b></td><td>203.00 (-10.81%)</td><td>164.24 (-17.25%)</td><td>167.40 (-11.38%)</td><td>126.40 <b>(-28.43%)</b></td><td>36.28 <b>(+59.37%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.56 (n/a)</td><td>0.50 (n/a)</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.06 (n/a)</td><td>227.60 (n/a)</td><td>198.48 (n/a)</td><td>188.90 (n/a)</td><td>176.60 (n/a)</td><td>22.76 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.64 (+2.22%)</td><td>0.55 (-3.36%)</td><td>0.53 (-5.78%)</td><td>0.48 (-6.44%)</td><td>0.06 <b>(+44.48%)</b></td><td>205.00 (+6.88%)</td><td>180.14 (+4.05%)</td><td>183.80 (+6.12%)</td><td>154.50 (-2.15%)</td><td>20.19 <b>(+50.54%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.62 (n/a)</td><td>0.57 (n/a)</td><td>0.57 (n/a)</td><td>0.51 (n/a)</td><td>0.04 (n/a)</td><td>191.80 (n/a)</td><td>173.12 (n/a)</td><td>173.20 (n/a)</td><td>157.90 (n/a)</td><td>13.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.77 <b>(+31.43%)</b></td><td>0.59 <b>(+30.27%)</b></td><td>0.55 <b>(+36.25%)</b></td><td>0.46 (+17.51%)</td><td>0.14 <b>(+61.57%)</b></td><td>214.80 (-14.90%)</td><td>172.86 <b>(-21.90%)</b></td><td>179.70 <b>(-26.59%)</b></td><td>127.20 <b>(-23.88%)</b></td><td>39.39 (+2.39%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.59 (n/a)</td><td>0.46 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.09 (n/a)</td><td>252.40 (n/a)</td><td>221.32 (n/a)</td><td>244.80 (n/a)</td><td>167.10 (n/a)</td><td>38.47 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.47 (+7.79%)</td><td>0.41 (+11.14%)</td><td>0.41 (+9.15%)</td><td>0.34 (+13.73%)</td><td>0.05 (-3.08%)</td><td>215.60 (-12.07%)</td><td>180.82 (-10.33%)</td><td>180.10 (-8.39%)</td><td>155.80 (-7.26%)</td><td>22.05 <b>(-20.83%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.44 (n/a)</td><td>0.37 (n/a)</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.05 (n/a)</td><td>245.20 (n/a)</td><td>201.66 (n/a)</td><td>196.60 (n/a)</td><td>168.00 (n/a)</td><td>27.85 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.56 (+2.58%)</td><td>0.46 (+11.46%)</td><td>0.42 (+18.49%)</td><td>0.36 (+6.81%)</td><td>0.09 (-8.03%)</td><td>203.70 (-6.39%)</td><td>165.02 (-11.17%)</td><td>174.20 (-15.60%)</td><td>132.80 (-2.50%)</td><td>30.27 <b>(-20.53%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.54 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.09 (n/a)</td><td>217.60 (n/a)</td><td>185.78 (n/a)</td><td>206.40 (n/a)</td><td>136.20 (n/a)</td><td>38.09 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.56 (+13.62%)</td><td>0.40 (+4.65%)</td><td>0.36 (+2.17%)</td><td>0.31 (-5.68%)</td><td>0.10 <b>(+47.60%)</b></td><td>238.60 (+6.04%)</td><td>192.80 (-2.38%)</td><td>206.50 (-2.13%)</td><td>131.20 (-12.01%)</td><td>41.42 <b>(+36.48%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>225.00 (n/a)</td><td>197.50 (n/a)</td><td>211.00 (n/a)</td><td>149.10 (n/a)</td><td>30.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.43 (-2.59%)</td><td>0.36 (+5.82%)</td><td>0.39 <b>(+26.96%)</b></td><td>0.28 (-7.88%)</td><td>0.06 (+8.79%)</td><td>266.60 (+8.55%)</td><td>213.44 (-4.81%)</td><td>190.70 <b>(-21.23%)</b></td><td>172.30 (+2.68%)</td><td>40.91 <b>(+23.94%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.44 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.06 (n/a)</td><td>245.60 (n/a)</td><td>224.22 (n/a)</td><td>242.10 (n/a)</td><td>167.80 (n/a)</td><td>33.01 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.19 (+15.60%)</td><td>0.74 (-6.85%)</td><td>0.63 (-11.46%)</td><td>0.55 (+0.79%)</td><td>0.26 <b>(+26.20%)</b></td><td>237.40 (-0.75%)</td><td>190.94 (+9.36%)</td><td>208.90 (+12.98%)</td><td>109.80 (-13.48%)</td><td>48.87 (+6.41%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>1.03 (n/a)</td><td>0.79 (n/a)</td><td>0.71 (n/a)</td><td>0.55 (n/a)</td><td>0.21 (n/a)</td><td>239.20 (n/a)</td><td>174.60 (n/a)</td><td>184.90 (n/a)</td><td>126.90 (n/a)</td><td>45.93 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.09 (+2.27%)</td><td>0.77 (+3.38%)</td><td>0.73 (+6.34%)</td><td>0.62 (-1.59%)</td><td>0.18 (+0.86%)</td><td>211.80 (+1.63%)</td><td>175.58 (-3.34%)</td><td>180.10 (-5.95%)</td><td>120.00 (-2.20%)</td><td>33.77 (-2.20%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>1.07 (n/a)</td><td>0.75 (n/a)</td><td>0.68 (n/a)</td><td>0.63 (n/a)</td><td>0.18 (n/a)</td><td>208.40 (n/a)</td><td>181.64 (n/a)</td><td>191.50 (n/a)</td><td>122.70 (n/a)</td><td>34.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.14 <b>(+65.07%)</b></td><td>0.82 <b>(+33.20%)</b></td><td>0.79 <b>(+24.67%)</b></td><td>0.66 <b>(+33.22%)</b></td><td>0.19 <b>(+133.42%)</b></td><td>198.00 <b>(-24.94%)</b></td><td>164.58 <b>(-23.41%)</b></td><td>165.50 (-19.78%)</td><td>114.50 <b>(-39.42%)</b></td><td>31.37 (+2.54%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.69 (n/a)</td><td>0.62 (n/a)</td><td>0.64 (n/a)</td><td>0.50 (n/a)</td><td>0.08 (n/a)</td><td>263.80 (n/a)</td><td>214.88 (n/a)</td><td>206.30 (n/a)</td><td>189.00 (n/a)</td><td>30.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.00 (+2.33%)</td><td>0.00 (+2.88%)</td><td>0.00 (+2.38%)</td><td>0.00 (+2.56%)</td><td>0.00 (-1.80%)</td><td>1016.71 (-4.10%)</td><td>956.02 (-2.78%)</td><td>949.25 (-2.04%)</td><td>923.02 (-2.13%)</td><td>35.68 <b>(-26.05%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1060.23 (n/a)</td><td>983.32 (n/a)</td><td>969.05 (n/a)</td><td>943.14 (n/a)</td><td>48.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.01 (+1.20%)</td><td>0.01 (+1.00%)</td><td>0.01 (-1.22%)</td><td>0.01 (+2.67%)</td><td>0.00 (-16.39%)</td><td>1067.08 (-2.14%)</td><td>1010.43 (-1.00%)</td><td>1009.02 (+0.63%)</td><td>975.38 (-1.71%)</td><td>35.15 (-12.84%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1090.38 (n/a)</td><td>1020.62 (n/a)</td><td>1002.73 (n/a)</td><td>992.37 (n/a)</td><td>40.33 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.95 (+0.66%)</td><td>0.94 (+0.57%)</td><td>0.94 (+0.51%)</td><td>0.94 (+0.47%)</td><td>0.00 (+8.00%)</td><td>2230.96 (-0.47%)</td><td>2221.62 (-0.57%)</td><td>2222.18 (-0.52%)</td><td>2210.72 (-0.66%)</td><td>7.40 (+7.70%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.00 (n/a)</td><td>2241.43 (n/a)</td><td>2234.40 (n/a)</td><td>2233.72 (n/a)</td><td>2225.34 (n/a)</td><td>6.87 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>3.33 (+10.70%)</td><td>2.67 (-0.93%)</td><td>2.59 (-8.09%)</td><td>2.35 (+7.71%)</td><td>0.38 (+13.45%)</td><td>222.70 (-7.17%)</td><td>198.88 (+1.00%)</td><td>202.50 (+8.81%)</td><td>157.40 (-9.70%)</td><td>24.91 (-7.49%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>3.01 (n/a)</td><td>2.70 (n/a)</td><td>2.82 (n/a)</td><td>2.19 (n/a)</td><td>0.34 (n/a)</td><td>239.90 (n/a)</td><td>196.92 (n/a)</td><td>186.10 (n/a)</td><td>174.30 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>5.73 (-7.23%)</td><td>4.42 (-13.28%)</td><td>4.24 (-9.41%)</td><td>3.47 <b>(-21.87%)</b></td><td>0.86 (+6.82%)</td><td>302.60 <b>(+28.00%)</b></td><td>244.04 (+16.44%)</td><td>247.10 (+10.41%)</td><td>183.10 (+7.77%)</td><td>44.94 <b>(+44.28%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>6.17 (n/a)</td><td>5.10 (n/a)</td><td>4.69 (n/a)</td><td>4.44 (n/a)</td><td>0.80 (n/a)</td><td>236.40 (n/a)</td><td>209.58 (n/a)</td><td>223.80 (n/a)</td><td>169.90 (n/a)</td><td>31.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>2.98 (-15.10%)</td><td>2.55 (-9.29%)</td><td>2.73 (-0.86%)</td><td>1.98 (-15.23%)</td><td>0.40 (-5.74%)</td><td>264.60 (+17.97%)</td><td>210.08 (+10.78%)</td><td>191.90 (+0.89%)</td><td>175.80 (+17.83%)</td><td>36.16 <b>(+35.11%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:33:27</td><td>3.51 (n/a)</td><td>2.81 (n/a)</td><td>2.76 (n/a)</td><td>2.34 (n/a)</td><td>0.43 (n/a)</td><td>224.30 (n/a)</td><td>189.64 (n/a)</td><td>190.20 (n/a)</td><td>149.20 (n/a)</td><td>26.76 (n/a)</td>
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
