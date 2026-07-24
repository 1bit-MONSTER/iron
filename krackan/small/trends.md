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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.10 (-15.93%)</td><td>0.07 <b>(-21.22%)</b></td><td>0.07 (-19.47%)</td><td>0.06 <b>(-21.01%)</b></td><td>0.01 (-15.37%)</td><td>205.30 <b>(+26.57%)</b></td><td>176.06 <b>(+27.06%)</b></td><td>180.00 <b>(+24.22%)</b></td><td>129.30 (+18.95%)</td><td>28.88 <b>(+23.20%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>162.20 (n/a)</td><td>138.56 (n/a)</td><td>144.90 (n/a)</td><td>108.70 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (-13.59%)</td><td>0.07 (-18.80%)</td><td>0.07 <b>(-25.68%)</b></td><td>0.06 (-19.11%)</td><td>0.01 (-4.56%)</td><td>209.50 <b>(+23.60%)</b></td><td>177.54 <b>(+23.55%)</b></td><td>183.80 <b>(+34.55%)</b></td><td>146.90 (+15.76%)</td><td>24.10 <b>(+35.42%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>169.50 (n/a)</td><td>143.70 (n/a)</td><td>136.60 (n/a)</td><td>126.90 (n/a)</td><td>17.80 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (-14.69%)</td><td>0.07 (+1.95%)</td><td>0.08 (+10.58%)</td><td>0.06 (+4.14%)</td><td>0.01 <b>(-32.99%)</b></td><td>209.10 (-3.95%)</td><td>167.66 (-3.14%)</td><td>155.70 (-9.58%)</td><td>152.90 (+17.16%)</td><td>23.83 <b>(-23.05%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>173.10 (n/a)</td><td>172.20 (n/a)</td><td>130.50 (n/a)</td><td>30.96 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (-6.92%)</td><td>0.06 (-0.80%)</td><td>0.07 (-4.03%)</td><td>0.04 (+2.78%)</td><td>0.01 (-13.67%)</td><td>291.30 (-2.71%)</td><td>199.84 (-0.58%)</td><td>188.20 (+4.21%)</td><td>155.60 (+7.38%)</td><td>54.42 (-10.41%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>299.40 (n/a)</td><td>201.00 (n/a)</td><td>180.60 (n/a)</td><td>144.90 (n/a)</td><td>60.75 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (-0.56%)</td><td>0.04 (+8.80%)</td><td>0.04 (+13.28%)</td><td>0.03 (+6.17%)</td><td>0.01 (-10.04%)</td><td>187.50 (-5.78%)</td><td>147.40 (-8.91%)</td><td>139.70 (-11.69%)</td><td>114.50 (+0.62%)</td><td>29.54 (-15.32%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>161.82 (n/a)</td><td>158.20 (n/a)</td><td>113.80 (n/a)</td><td>34.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.04 (+11.78%)</td><td>0.04 (+11.42%)</td><td>0.04 (+11.83%)</td><td>0.03 (+16.07%)</td><td>0.00 (+3.03%)</td><td>157.00 (-13.83%)</td><td>144.88 (-10.36%)</td><td>146.40 (-10.57%)</td><td>124.70 (-10.55%)</td><td>12.44 <b>(-20.87%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>182.20 (n/a)</td><td>161.62 (n/a)</td><td>163.70 (n/a)</td><td>139.40 (n/a)</td><td>15.72 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 <b>(+37.66%)</b></td><td>0.04 (+19.73%)</td><td>0.04 (+16.06%)</td><td>0.03 (+18.97%)</td><td>0.01 <b>(+108.69%)</b></td><td>160.90 (-15.94%)</td><td>136.22 (-15.11%)</td><td>131.20 (-13.85%)</td><td>104.10 <b>(-27.36%)</b></td><td>24.07 <b>(+28.77%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>191.40 (n/a)</td><td>160.46 (n/a)</td><td>152.30 (n/a)</td><td>143.30 (n/a)</td><td>18.69 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.03 <b>(-31.36%)</b></td><td>0.03 (-17.44%)</td><td>0.03 (-9.87%)</td><td>0.03 (-2.54%)</td><td>0.00 <b>(-71.64%)</b></td><td>203.00 (+2.63%)</td><td>183.78 (+17.61%)</td><td>181.90 (+10.98%)</td><td>168.80 <b>(+45.64%)</b></td><td>13.52 <b>(-56.99%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.80 (n/a)</td><td>156.26 (n/a)</td><td>163.90 (n/a)</td><td>115.90 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.04 (+0.24%)</td><td>0.03 (-1.83%)</td><td>0.03 (-9.90%)</td><td>0.03 (+7.17%)</td><td>0.01 (+6.02%)</td><td>191.80 (-6.67%)</td><td>162.36 (+1.87%)</td><td>167.40 (+11.01%)</td><td>134.70 (-0.22%)</td><td>25.29 (-6.49%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.50 (n/a)</td><td>159.38 (n/a)</td><td>150.80 (n/a)</td><td>135.00 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.04 (-12.35%)</td><td>0.03 (-9.72%)</td><td>0.03 (-10.59%)</td><td>0.02 (-15.92%)</td><td>0.00 (-14.53%)</td><td>218.10 (+18.92%)</td><td>178.54 (+10.77%)</td><td>177.00 (+11.88%)</td><td>146.40 (+14.11%)</td><td>25.67 (+16.66%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>183.40 (n/a)</td><td>161.18 (n/a)</td><td>158.20 (n/a)</td><td>128.30 (n/a)</td><td>22.00 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.03 (-9.45%)</td><td>0.03 (-17.09%)</td><td>0.03 (-14.94%)</td><td>0.02 <b>(-25.64%)</b></td><td>0.00 <b>(+109.76%)</b></td><td>237.10 <b>(+34.49%)</b></td><td>197.48 <b>(+22.57%)</b></td><td>182.20 (+17.55%)</td><td>169.40 (+10.43%)</td><td>31.08 <b>(+213.86%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>176.30 (n/a)</td><td>161.12 (n/a)</td><td>155.00 (n/a)</td><td>153.40 (n/a)</td><td>9.90 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.03 (-6.49%)</td><td>0.02 (-12.95%)</td><td>0.02 <b>(-23.57%)</b></td><td>0.02 (-12.22%)</td><td>0.00 (-11.93%)</td><td>320.90 (+13.96%)</td><td>234.24 (+14.74%)</td><td>231.70 <b>(+30.83%)</b></td><td>181.30 (+6.90%)</td><td>53.14 (+11.13%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>281.60 (n/a)</td><td>204.14 (n/a)</td><td>177.10 (n/a)</td><td>169.60 (n/a)</td><td>47.82 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>242.80 (n/a)</td><td>176.76 (n/a)</td><td>182.20 (n/a)</td><td>111.20 (n/a)</td><td>49.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>301.50 (n/a)</td><td>213.94 (n/a)</td><td>195.10 (n/a)</td><td>180.90 (n/a)</td><td>50.26 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>242.30 (n/a)</td><td>206.80 (n/a)</td><td>213.70 (n/a)</td><td>149.70 (n/a)</td><td>36.99 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>244.90 (n/a)</td><td>215.82 (n/a)</td><td>226.90 (n/a)</td><td>182.50 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.10 (n/a)</td><td>159.42 (n/a)</td><td>161.60 (n/a)</td><td>123.80 (n/a)</td><td>25.91 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>170.30 (n/a)</td><td>170.50 (n/a)</td><td>154.50 (n/a)</td><td>13.62 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>194.74 (n/a)</td><td>190.30 (n/a)</td><td>166.00 (n/a)</td><td>23.65 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>193.92 (n/a)</td><td>204.30 (n/a)</td><td>172.50 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>197.70 (n/a)</td><td>159.62 (n/a)</td><td>170.10 (n/a)</td><td>97.40 (n/a)</td><td>38.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>154.12 (n/a)</td><td>151.60 (n/a)</td><td>108.10 (n/a)</td><td>31.06 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.10 (n/a)</td><td>146.42 (n/a)</td><td>156.40 (n/a)</td><td>115.10 (n/a)</td><td>21.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.10 (n/a)</td><td>158.94 (n/a)</td><td>176.00 (n/a)</td><td>117.80 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>366.90 (n/a)</td><td>208.38 (n/a)</td><td>174.70 (n/a)</td><td>136.60 (n/a)</td><td>91.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.30 (n/a)</td><td>180.88 (n/a)</td><td>181.10 (n/a)</td><td>161.60 (n/a)</td><td>16.96 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>177.16 (n/a)</td><td>182.00 (n/a)</td><td>144.40 (n/a)</td><td>21.32 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>216.10 (n/a)</td><td>187.24 (n/a)</td><td>182.00 (n/a)</td><td>167.40 (n/a)</td><td>18.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>4.88 (+1.05%)</td><td>4.30 (+3.88%)</td><td>4.16 (+1.95%)</td><td>4.10 (+12.67%)</td><td>0.32 <b>(-24.39%)</b></td><td>2295.00 (-11.24%)</td><td>2194.82 (-4.12%)</td><td>2258.30 (-1.92%)</td><td>1928.20 (-1.04%)</td><td>150.88 <b>(-33.32%)</b></td><td>1918.52 (+1.05%)</td><td>1692.50 (+3.88%)</td><td>1638.09 (+1.95%)</td><td>1611.95 (+12.67%)</td><td>127.48 <b>(-24.39%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>4.83 (n/a)</td><td>4.14 (n/a)</td><td>4.08 (n/a)</td><td>3.64 (n/a)</td><td>0.43 (n/a)</td><td>2585.70 (n/a)</td><td>2289.20 (n/a)</td><td>2302.50 (n/a)</td><td>1948.50 (n/a)</td><td>226.27 (n/a)</td><td>1898.58 (n/a)</td><td>1629.28 (n/a)</td><td>1606.68 (n/a)</td><td>1430.70 (n/a)</td><td>168.60 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>1.08 (-0.34%)</td><td>0.82 (-13.90%)</td><td>0.77 <b>(-25.52%)</b></td><td>0.72 (-0.64%)</td><td>0.15 (+1.33%)</td><td>306.30 (+0.66%)</td><td>275.06 (+16.18%)</td><td>287.80 <b>(+34.24%)</b></td><td>205.30 (+0.34%)</td><td>41.22 (+0.20%)</td><td>45.97 (-0.34%)</td><td>35.06 (-13.90%)</td><td>32.79 <b>(-25.52%)</b></td><td>30.81 (-0.64%)</td><td>6.28 (+1.33%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.08 (n/a)</td><td>0.95 (n/a)</td><td>1.03 (n/a)</td><td>0.73 (n/a)</td><td>0.15 (n/a)</td><td>304.30 (n/a)</td><td>236.76 (n/a)</td><td>214.40 (n/a)</td><td>204.60 (n/a)</td><td>41.14 (n/a)</td><td>46.12 (n/a)</td><td>40.72 (n/a)</td><td>44.03 (n/a)</td><td>31.01 (n/a)</td><td>6.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>1.18 (-4.82%)</td><td>1.02 (-2.21%)</td><td>1.05 (-8.84%)</td><td>0.83 (+5.00%)</td><td>0.15 <b>(-31.50%)</b></td><td>266.00 (-4.80%)</td><td>220.62 (+0.29%)</td><td>210.40 (+9.64%)</td><td>187.80 (+5.09%)</td><td>32.95 <b>(-31.88%)</b></td><td>50.25 (-4.82%)</td><td>43.51 (-2.21%)</td><td>44.84 (-8.84%)</td><td>35.47 (+5.00%)</td><td>6.23 <b>(-31.50%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.24 (n/a)</td><td>1.04 (n/a)</td><td>1.15 (n/a)</td><td>0.79 (n/a)</td><td>0.21 (n/a)</td><td>279.40 (n/a)</td><td>219.98 (n/a)</td><td>191.90 (n/a)</td><td>178.70 (n/a)</td><td>48.38 (n/a)</td><td>52.80 (n/a)</td><td>44.50 (n/a)</td><td>49.19 (n/a)</td><td>33.78 (n/a)</td><td>9.09 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.52 (+0.14%)</td><td>0.52 (+0.13%)</td><td>0.52 (+0.03%)</td><td>0.52 (+0.42%)</td><td>0.00 <b>(-61.33%)</b></td><td>48666.30 (-0.42%)</td><td>48613.20 (-0.13%)</td><td>48609.40 (-0.03%)</td><td>48552.70 (-0.14%)</td><td>41.80 <b>(-61.56%)</b></td><td>353.84 (+0.14%)</td><td>353.40 (+0.13%)</td><td>353.43 (+0.03%)</td><td>353.01 (+0.42%)</td><td>0.30 <b>(-61.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.00 (n/a)</td><td>48871.80 (n/a)</td><td>48678.42 (n/a)</td><td>48624.50 (n/a)</td><td>48621.10 (n/a)</td><td>108.75 (n/a)</td><td>353.34 (n/a)</td><td>352.93 (n/a)</td><td>353.32 (n/a)</td><td>351.53 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.89 (-0.78%)</td><td>0.89 (-0.84%)</td><td>0.88 (-1.00%)</td><td>0.88 (-0.74%)</td><td>0.00 (-6.08%)</td><td>28581.00 (+0.75%)</td><td>28433.62 (+0.85%)</td><td>28457.80 (+1.01%)</td><td>28256.80 (+0.79%)</td><td>127.86 (-4.66%)</td><td>607.99 (-0.78%)</td><td>604.22 (-0.84%)</td><td>603.70 (-1.00%)</td><td>601.09 (-0.74%)</td><td>2.72 (-6.08%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.00 (n/a)</td><td>28368.30 (n/a)</td><td>28195.36 (n/a)</td><td>28173.30 (n/a)</td><td>28035.80 (n/a)</td><td>134.12 (n/a)</td><td>612.78 (n/a)</td><td>609.33 (n/a)</td><td>609.79 (n/a)</td><td>605.60 (n/a)</td><td>2.90 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>3.31 (+1.10%)</td><td>3.22 (+1.19%)</td><td>3.22 (+1.72%)</td><td>3.15 (+0.89%)</td><td>0.06 (+0.13%)</td><td>7982.80 (-0.88%)</td><td>7828.94 (-1.17%)</td><td>7821.50 (-1.69%)</td><td>7612.00 (-1.09%)</td><td>140.07 (-1.94%)</td><td>2256.95 (+1.10%)</td><td>2194.97 (+1.19%)</td><td>2196.49 (+1.72%)</td><td>2152.10 (+0.89%)</td><td>39.67 (+0.13%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>3.27 (n/a)</td><td>3.18 (n/a)</td><td>3.16 (n/a)</td><td>3.12 (n/a)</td><td>0.06 (n/a)</td><td>8054.00 (n/a)</td><td>7921.82 (n/a)</td><td>7956.00 (n/a)</td><td>7695.90 (n/a)</td><td>142.85 (n/a)</td><td>2232.33 (n/a)</td><td>2169.24 (n/a)</td><td>2159.37 (n/a)</td><td>2133.08 (n/a)</td><td>39.62 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>4.17 (-1.30%)</td><td>3.58 (+6.61%)</td><td>3.73 <b>(+21.37%)</b></td><td>3.03 (+8.66%)</td><td>0.51 (-14.01%)</td><td>2663.10 (-7.97%)</td><td>2291.72 (-6.83%)</td><td>2161.30 (-17.61%)</td><td>1931.10 (+1.32%)</td><td>335.92 (-17.10%)</td><td>1094.70 (-1.30%)</td><td>938.15 (+6.61%)</td><td>978.07 <b>(+21.37%)</b></td><td>793.79 (+8.66%)</td><td>134.40 (-14.01%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>4.23 (n/a)</td><td>3.36 (n/a)</td><td>3.07 (n/a)</td><td>2.79 (n/a)</td><td>0.60 (n/a)</td><td>2893.70 (n/a)</td><td>2459.64 (n/a)</td><td>2623.30 (n/a)</td><td>1906.00 (n/a)</td><td>405.23 (n/a)</td><td>1109.10 (n/a)</td><td>879.94 (n/a)</td><td>805.84 (n/a)</td><td>730.53 (n/a)</td><td>156.30 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.36 <b>(-29.39%)</b></td><td>0.33 <b>(-22.55%)</b></td><td>0.34 (-17.94%)</td><td>0.30 (-14.20%)</td><td>0.03 <b>(-60.49%)</b></td><td>4190.00 (+16.56%)</td><td>3792.34 <b>(+26.68%)</b></td><td>3631.00 <b>(+21.86%)</b></td><td>3432.10 <b>(+41.63%)</b></td><td>355.53 <b>(-33.55%)</b></td><td>19.55 <b>(-29.39%)</b></td><td>17.82 <b>(-22.55%)</b></td><td>18.48 (-17.94%)</td><td>16.02 (-14.20%)</td><td>1.63 <b>(-60.49%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>3594.80 (n/a)</td><td>2993.74 (n/a)</td><td>2979.60 (n/a)</td><td>2423.30 (n/a)</td><td>535.05 (n/a)</td><td>27.69 (n/a)</td><td>23.01 (n/a)</td><td>22.52 (n/a)</td><td>18.67 (n/a)</td><td>4.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>4.89 <b>(-25.89%)</b></td><td>4.61 (-8.82%)</td><td>4.82 (+1.57%)</td><td>3.72 (-1.35%)</td><td>0.50 <b>(-60.62%)</b></td><td>1788.70 (+1.37%)</td><td>1459.64 (+5.49%)</td><td>1378.80 (-1.54%)</td><td>1359.60 <b>(+34.93%)</b></td><td>184.62 <b>(-45.33%)</b></td><td>1511.58 <b>(-25.89%)</b></td><td>1423.64 (-8.82%)</td><td>1490.55 (+1.57%)</td><td>1149.03 (-1.35%)</td><td>154.44 <b>(-60.62%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>6.60 (n/a)</td><td>5.05 (n/a)</td><td>4.75 (n/a)</td><td>3.77 (n/a)</td><td>1.27 (n/a)</td><td>1764.50 (n/a)</td><td>1383.66 (n/a)</td><td>1400.40 (n/a)</td><td>1007.60 (n/a)</td><td>337.68 (n/a)</td><td>2039.66 (n/a)</td><td>1561.31 (n/a)</td><td>1467.54 (n/a)</td><td>1164.78 (n/a)</td><td>392.21 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.26 (+3.49%)</td><td>0.20 (-3.33%)</td><td>0.19 (-2.95%)</td><td>0.14 (-19.03%)</td><td>0.04 <b>(+29.59%)</b></td><td>0.26 (+3.49%)</td><td>0.20 (-3.33%)</td><td>0.18 (-2.95%)</td><td>0.14 (-19.03%)</td><td>0.04 <b>(+29.59%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>13.44 (-0.03%)</td><td>12.73 (+1.79%)</td><td>13.32 (+5.76%)</td><td>10.16 (-7.11%)</td><td>1.44 <b>(+40.07%)</b></td><td>13.43 (-0.03%)</td><td>12.72 (+1.79%)</td><td>13.31 (+5.76%)</td><td>10.15 (-7.11%)</td><td>1.43 <b>(+40.07%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>13.45 (n/a)</td><td>12.50 (n/a)</td><td>12.60 (n/a)</td><td>10.94 (n/a)</td><td>1.02 (n/a)</td><td>13.44 (n/a)</td><td>12.49 (n/a)</td><td>12.59 (n/a)</td><td>10.93 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>25.25 (-2.17%)</td><td>24.56 (-0.78%)</td><td>24.37 (-2.59%)</td><td>24.12 (+1.99%)</td><td>0.50 <b>(-41.74%)</b></td><td>25.24 (-2.17%)</td><td>24.54 (-0.78%)</td><td>24.36 (-2.59%)</td><td>24.11 (+1.99%)</td><td>0.50 <b>(-41.74%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>25.81 (n/a)</td><td>24.75 (n/a)</td><td>25.02 (n/a)</td><td>23.65 (n/a)</td><td>0.86 (n/a)</td><td>25.80 (n/a)</td><td>24.73 (n/a)</td><td>25.00 (n/a)</td><td>23.64 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>44.64 (+4.46%)</td><td>39.58 (-1.76%)</td><td>39.88 (-1.92%)</td><td>34.54 (-6.47%)</td><td>3.69 <b>(+75.40%)</b></td><td>44.61 (+4.46%)</td><td>39.56 (-1.76%)</td><td>39.86 (-1.92%)</td><td>34.52 (-6.47%)</td><td>3.68 <b>(+75.40%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>42.73 (n/a)</td><td>40.29 (n/a)</td><td>40.67 (n/a)</td><td>36.93 (n/a)</td><td>2.10 (n/a)</td><td>42.71 (n/a)</td><td>40.27 (n/a)</td><td>40.64 (n/a)</td><td>36.91 (n/a)</td><td>2.10 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>44.41 (-2.45%)</td><td>42.90 (+4.07%)</td><td>43.54 (-3.66%)</td><td>40.37 <b>(+50.64%)</b></td><td>1.60 <b>(-80.29%)</b></td><td>44.39 (-2.45%)</td><td>42.88 (+4.07%)</td><td>43.51 (-3.66%)</td><td>40.34 <b>(+50.64%)</b></td><td>1.60 <b>(-80.29%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>45.53 (n/a)</td><td>41.22 (n/a)</td><td>45.19 (n/a)</td><td>26.80 (n/a)</td><td>8.11 (n/a)</td><td>45.50 (n/a)</td><td>41.20 (n/a)</td><td>45.16 (n/a)</td><td>26.78 (n/a)</td><td>8.10 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>13.26 (-1.06%)</td><td>12.76 (+2.62%)</td><td>13.22 (+5.26%)</td><td>10.89 (+3.99%)</td><td>1.05 (-10.74%)</td><td>13.25 (-1.06%)</td><td>12.75 (+2.62%)</td><td>13.22 (+5.26%)</td><td>10.88 (+3.99%)</td><td>1.05 (-10.74%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>13.40 (n/a)</td><td>12.43 (n/a)</td><td>12.56 (n/a)</td><td>10.47 (n/a)</td><td>1.17 (n/a)</td><td>13.39 (n/a)</td><td>12.42 (n/a)</td><td>12.56 (n/a)</td><td>10.46 (n/a)</td><td>1.17 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>25.17 (-0.55%)</td><td>24.50 (-1.17%)</td><td>24.22 (-3.17%)</td><td>24.03 (-0.13%)</td><td>0.55 (+10.44%)</td><td>25.16 (-0.55%)</td><td>24.48 (-1.17%)</td><td>24.20 (-3.17%)</td><td>24.01 (-0.13%)</td><td>0.55 (+10.44%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>25.31 (n/a)</td><td>24.79 (n/a)</td><td>25.01 (n/a)</td><td>24.06 (n/a)</td><td>0.50 (n/a)</td><td>25.30 (n/a)</td><td>24.77 (n/a)</td><td>25.00 (n/a)</td><td>24.05 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>42.38 (+0.93%)</td><td>39.51 (-0.73%)</td><td>39.08 (-1.25%)</td><td>36.91 (-0.93%)</td><td>1.99 (+10.43%)</td><td>42.36 (+0.93%)</td><td>39.49 (-0.73%)</td><td>39.05 (-1.25%)</td><td>36.89 (-0.93%)</td><td>1.98 (+10.43%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>41.99 (n/a)</td><td>39.80 (n/a)</td><td>39.57 (n/a)</td><td>37.26 (n/a)</td><td>1.80 (n/a)</td><td>41.97 (n/a)</td><td>39.77 (n/a)</td><td>39.55 (n/a)</td><td>37.24 (n/a)</td><td>1.80 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>46.69 (+2.73%)</td><td>43.75 (+0.71%)</td><td>43.15 (-2.68%)</td><td>42.13 (+2.83%)</td><td>1.73 <b>(-23.70%)</b></td><td>46.66 (+2.73%)</td><td>43.72 (+0.71%)</td><td>43.12 (-2.68%)</td><td>42.11 (+2.83%)</td><td>1.73 <b>(-23.70%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>45.45 (n/a)</td><td>43.44 (n/a)</td><td>44.33 (n/a)</td><td>40.97 (n/a)</td><td>2.27 (n/a)</td><td>45.43 (n/a)</td><td>43.41 (n/a)</td><td>44.31 (n/a)</td><td>40.95 (n/a)</td><td>2.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>10.06 (+9.18%)</td><td>9.32 (+9.29%)</td><td>9.36 (+9.40%)</td><td>8.54 (+6.93%)</td><td>0.54 (+19.61%)</td><td>10.04 (+9.18%)</td><td>9.31 (+9.29%)</td><td>9.35 (+9.40%)</td><td>8.52 (+6.93%)</td><td>0.54 (+19.61%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>9.21 (n/a)</td><td>8.53 (n/a)</td><td>8.56 (n/a)</td><td>7.98 (n/a)</td><td>0.45 (n/a)</td><td>9.19 (n/a)</td><td>8.51 (n/a)</td><td>8.54 (n/a)</td><td>7.97 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.91 (+14.66%)</td><td>0.86 <b>(+24.49%)</b></td><td>0.85 <b>(+31.62%)</b></td><td>0.81 <b>(+32.99%)</b></td><td>0.05 <b>(-39.91%)</b></td><td>0.89 (+14.66%)</td><td>0.84 <b>(+24.49%)</b></td><td>0.83 <b>(+31.62%)</b></td><td>0.79 <b>(+32.99%)</b></td><td>0.05 <b>(-39.91%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.79 (n/a)</td><td>0.69 (n/a)</td><td>0.64 (n/a)</td><td>0.61 (n/a)</td><td>0.08 (n/a)</td><td>0.78 (n/a)</td><td>0.68 (n/a)</td><td>0.63 (n/a)</td><td>0.60 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>1.16 (-5.87%)</td><td>1.05 (+0.67%)</td><td>1.10 (+6.86%)</td><td>0.86 (-1.42%)</td><td>0.13 (-2.98%)</td><td>1.15 (-5.87%)</td><td>1.04 (+0.67%)</td><td>1.09 (+6.86%)</td><td>0.85 (-1.42%)</td><td>0.13 (-2.98%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.23 (n/a)</td><td>1.04 (n/a)</td><td>1.03 (n/a)</td><td>0.88 (n/a)</td><td>0.14 (n/a)</td><td>1.22 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.86 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>17.10 (+11.74%)</td><td>14.77 (+4.42%)</td><td>14.91 (+2.32%)</td><td>12.94 (+12.94%)</td><td>1.56 (+1.65%)</td><td>16.90 (+11.74%)</td><td>14.60 (+4.42%)</td><td>14.74 (+2.32%)</td><td>12.79 (+12.94%)</td><td>1.54 (+1.65%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>15.30 (n/a)</td><td>14.14 (n/a)</td><td>14.58 (n/a)</td><td>11.45 (n/a)</td><td>1.53 (n/a)</td><td>15.12 (n/a)</td><td>13.98 (n/a)</td><td>14.41 (n/a)</td><td>11.32 (n/a)</td><td>1.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>12.54 (-0.89%)</td><td>12.14 (+15.38%)</td><td>12.13 (+5.21%)</td><td>11.76 <b>(+85.87%)</b></td><td>0.33 <b>(-86.79%)</b></td><td>12.32 (-0.89%)</td><td>11.93 (+15.38%)</td><td>11.92 (+5.21%)</td><td>11.55 <b>(+85.87%)</b></td><td>0.32 <b>(-86.79%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>12.65 (n/a)</td><td>10.52 (n/a)</td><td>11.53 (n/a)</td><td>6.33 (n/a)</td><td>2.50 (n/a)</td><td>12.43 (n/a)</td><td>10.34 (n/a)</td><td>11.33 (n/a)</td><td>6.21 (n/a)</td><td>2.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>9.81 <b>(+32.98%)</b></td><td>7.98 (+18.89%)</td><td>7.77 (+15.94%)</td><td>6.81 (+13.34%)</td><td>1.18 <b>(+141.75%)</b></td><td>9.64 <b>(+32.98%)</b></td><td>7.84 (+18.89%)</td><td>7.63 (+15.94%)</td><td>6.70 (+13.34%)</td><td>1.15 <b>(+141.75%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>7.37 (n/a)</td><td>6.71 (n/a)</td><td>6.70 (n/a)</td><td>6.01 (n/a)</td><td>0.49 (n/a)</td><td>7.25 (n/a)</td><td>6.59 (n/a)</td><td>6.58 (n/a)</td><td>5.91 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>7.22 <b>(+31.57%)</b></td><td>6.60 <b>(+32.40%)</b></td><td>6.53 <b>(+31.67%)</b></td><td>6.20 <b>(+41.87%)</b></td><td>0.38 <b>(-24.71%)</b></td><td>7.10 <b>(+31.57%)</b></td><td>6.49 <b>(+32.40%)</b></td><td>6.43 <b>(+31.67%)</b></td><td>6.10 <b>(+41.87%)</b></td><td>0.37 <b>(-24.71%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>5.49 (n/a)</td><td>4.98 (n/a)</td><td>4.96 (n/a)</td><td>4.37 (n/a)</td><td>0.50 (n/a)</td><td>5.40 (n/a)</td><td>4.90 (n/a)</td><td>4.88 (n/a)</td><td>4.30 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>156.24 (n/a)</td><td>146.70 (n/a)</td><td>134.00 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.10 (n/a)</td><td>181.00 (n/a)</td><td>186.00 (n/a)</td><td>117.40 (n/a)</td><td>51.19 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.90 (n/a)</td><td>178.32 (n/a)</td><td>169.00 (n/a)</td><td>153.40 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>171.36 (n/a)</td><td>181.70 (n/a)</td><td>111.50 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.60 (n/a)</td><td>174.46 (n/a)</td><td>182.40 (n/a)</td><td>130.70 (n/a)</td><td>25.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>172.48 (n/a)</td><td>172.70 (n/a)</td><td>132.60 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>187.70 (n/a)</td><td>170.46 (n/a)</td><td>168.80 (n/a)</td><td>152.80 (n/a)</td><td>15.99 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>297.90 (n/a)</td><td>188.52 (n/a)</td><td>171.20 (n/a)</td><td>116.90 (n/a)</td><td>66.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 <b>(+25.94%)</b></td><td>0.06 (+16.55%)</td><td>0.05 (+13.54%)</td><td>0.04 (-6.99%)</td><td>0.01 <b>(+120.54%)</b></td><td>202.10 (+7.50%)</td><td>147.32 (-11.08%)</td><td>149.10 (-11.93%)</td><td>107.80 <b>(-20.62%)</b></td><td>36.58 <b>(+91.14%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>165.68 (n/a)</td><td>169.30 (n/a)</td><td>135.80 (n/a)</td><td>19.14 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (-0.06%)</td><td>0.06 (+17.02%)</td><td>0.07 <b>(+26.62%)</b></td><td>0.06 <b>(+35.36%)</b></td><td>0.00 <b>(-70.24%)</b></td><td>137.20 <b>(-26.12%)</b></td><td>128.40 (-16.46%)</td><td>125.20 <b>(-21.01%)</b></td><td>123.40 (+0.08%)</td><td>5.92 <b>(-77.62%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.70 (n/a)</td><td>153.70 (n/a)</td><td>158.50 (n/a)</td><td>123.30 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 <b>(+23.02%)</b></td><td>0.06 (+10.15%)</td><td>0.06 (+15.44%)</td><td>0.04 (-17.93%)</td><td>0.01 <b>(+310.24%)</b></td><td>195.20 <b>(+21.85%)</b></td><td>143.06 (-6.53%)</td><td>133.30 (-13.39%)</td><td>117.10 (-18.74%)</td><td>30.64 <b>(+317.30%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>160.20 (n/a)</td><td>153.06 (n/a)</td><td>153.90 (n/a)</td><td>144.10 (n/a)</td><td>7.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 <b>(+40.47%)</b></td><td>0.06 <b>(+22.68%)</b></td><td>0.06 (+14.40%)</td><td>0.05 (+9.67%)</td><td>0.01 <b>(+771.07%)</b></td><td>156.40 (-8.80%)</td><td>138.20 (-17.41%)</td><td>145.80 (-12.59%)</td><td>116.10 <b>(-28.82%)</b></td><td>17.35 <b>(+463.16%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>171.50 (n/a)</td><td>167.34 (n/a)</td><td>166.80 (n/a)</td><td>163.10 (n/a)</td><td>3.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (+9.27%)</td><td>0.05 (-2.44%)</td><td>0.06 (+14.00%)</td><td>0.03 <b>(-37.59%)</b></td><td>0.02 <b>(+186.37%)</b></td><td>304.10 <b>(+60.22%)</b></td><td>194.90 <b>(+21.43%)</b></td><td>137.50 (-12.31%)</td><td>117.80 (-8.47%)</td><td>96.90 <b>(+332.66%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>160.50 (n/a)</td><td>156.80 (n/a)</td><td>128.70 (n/a)</td><td>22.40 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 <b>(+40.32%)</b></td><td>0.05 <b>(+35.09%)</b></td><td>0.05 <b>(+22.32%)</b></td><td>0.05 <b>(+74.21%)</b></td><td>0.01 (-10.48%)</td><td>167.30 <b>(-42.59%)</b></td><td>155.32 <b>(-27.74%)</b></td><td>160.60 (-18.27%)</td><td>124.50 <b>(-28.69%)</b></td><td>17.63 <b>(-63.71%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>291.40 (n/a)</td><td>214.96 (n/a)</td><td>196.50 (n/a)</td><td>174.60 (n/a)</td><td>48.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 <b>(+34.10%)</b></td><td>0.05 (+9.33%)</td><td>0.05 (+0.38%)</td><td>0.04 (-3.90%)</td><td>0.01 <b>(+162.95%)</b></td><td>203.70 (+4.09%)</td><td>160.70 (-5.80%)</td><td>165.50 (-0.42%)</td><td>116.80 <b>(-25.46%)</b></td><td>33.33 <b>(+103.44%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.70 (n/a)</td><td>170.60 (n/a)</td><td>166.20 (n/a)</td><td>156.70 (n/a)</td><td>16.38 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 <b>(+26.34%)</b></td><td>0.04 (+8.08%)</td><td>0.04 (+0.76%)</td><td>0.04 (-2.41%)</td><td>0.01 <b>(+223.47%)</b></td><td>220.60 (+2.51%)</td><td>187.74 (-5.66%)</td><td>195.50 (-0.71%)</td><td>145.90 <b>(-20.84%)</b></td><td>29.79 <b>(+160.39%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>215.20 (n/a)</td><td>199.00 (n/a)</td><td>196.90 (n/a)</td><td>184.30 (n/a)</td><td>11.44 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 <b>(+23.15%)</b></td><td>0.04 (-2.73%)</td><td>0.04 (-16.42%)</td><td>0.03 <b>(-20.30%)</b></td><td>0.01 <b>(+619.47%)</b></td><td>248.00 <b>(+25.51%)</b></td><td>203.72 (+7.73%)</td><td>224.30 (+19.69%)</td><td>147.90 (-18.78%)</td><td>47.18 <b>(+631.29%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.60 (n/a)</td><td>189.10 (n/a)</td><td>187.40 (n/a)</td><td>182.10 (n/a)</td><td>6.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (-10.07%)</td><td>0.04 (+9.55%)</td><td>0.04 (+7.60%)</td><td>0.03 <b>(+32.76%)</b></td><td>0.01 <b>(-42.23%)</b></td><td>254.40 <b>(-24.67%)</b></td><td>208.32 (-12.49%)</td><td>207.20 (-7.09%)</td><td>175.40 (+11.15%)</td><td>31.40 <b>(-51.82%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>337.70 (n/a)</td><td>238.04 (n/a)</td><td>223.00 (n/a)</td><td>157.80 (n/a)</td><td>65.17 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 <b>(+20.32%)</b></td><td>0.05 (+13.54%)</td><td>0.05 (+11.31%)</td><td>0.05 (+18.76%)</td><td>0.01 <b>(+20.45%)</b></td><td>178.60 (-15.83%)</td><td>154.54 (-11.92%)</td><td>151.40 (-10.15%)</td><td>131.40 (-16.89%)</td><td>17.81 (-17.22%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>175.46 (n/a)</td><td>168.50 (n/a)</td><td>158.10 (n/a)</td><td>21.52 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (+9.46%)</td><td>0.04 (+14.29%)</td><td>0.04 (+10.71%)</td><td>0.04 <b>(+51.06%)</b></td><td>0.00 <b>(-53.79%)</b></td><td>206.30 <b>(-33.81%)</b></td><td>193.76 (-14.85%)</td><td>194.40 (-9.71%)</td><td>172.30 (-8.64%)</td><td>13.27 <b>(-72.99%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.70 (n/a)</td><td>227.54 (n/a)</td><td>215.30 (n/a)</td><td>188.60 (n/a)</td><td>49.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (+3.29%)</td><td>0.04 (-1.30%)</td><td>0.04 (+6.31%)</td><td>0.02 (-10.18%)</td><td>0.01 <b>(+25.14%)</b></td><td>331.10 (+11.33%)</td><td>214.06 (+4.36%)</td><td>188.10 (-5.90%)</td><td>153.80 (-3.15%)</td><td>72.27 <b>(+32.04%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.40 (n/a)</td><td>205.12 (n/a)</td><td>199.90 (n/a)</td><td>158.80 (n/a)</td><td>54.73 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (+14.30%)</td><td>0.05 (+10.06%)</td><td>0.05 (+7.51%)</td><td>0.05 (+12.01%)</td><td>0.00 (+14.87%)</td><td>169.20 (-10.71%)</td><td>154.30 (-9.13%)</td><td>151.50 (-7.00%)</td><td>137.80 (-12.51%)</td><td>12.18 (-10.02%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.50 (n/a)</td><td>169.80 (n/a)</td><td>162.90 (n/a)</td><td>157.50 (n/a)</td><td>13.54 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (+8.32%)</td><td>0.05 (+2.83%)</td><td>0.05 (+2.58%)</td><td>0.04 (-9.67%)</td><td>0.01 <b>(+68.66%)</b></td><td>219.50 (+10.69%)</td><td>166.44 (-1.20%)</td><td>156.40 (-2.49%)</td><td>141.30 (-7.65%)</td><td>31.24 <b>(+73.88%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>198.30 (n/a)</td><td>168.46 (n/a)</td><td>160.40 (n/a)</td><td>153.00 (n/a)</td><td>17.97 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 <b>(+51.49%)</b></td><td>0.06 <b>(+43.22%)</b></td><td>0.05 <b>(+28.71%)</b></td><td>0.04 <b>(+22.88%)</b></td><td>0.01 <b>(+100.03%)</b></td><td>211.20 (-18.61%)</td><td>147.18 <b>(-28.09%)</b></td><td>149.60 <b>(-22.29%)</b></td><td>105.40 <b>(-34.00%)</b></td><td>40.81 (+6.83%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.50 (n/a)</td><td>204.68 (n/a)</td><td>192.50 (n/a)</td><td>159.70 (n/a)</td><td>38.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (+1.50%)</td><td>0.05 (+12.14%)</td><td>0.05 <b>(+26.96%)</b></td><td>0.04 (+13.70%)</td><td>0.01 (+2.53%)</td><td>225.80 (-12.04%)</td><td>175.58 (-11.09%)</td><td>159.10 <b>(-21.24%)</b></td><td>137.60 (-1.50%)</td><td>41.43 (-9.81%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>256.70 (n/a)</td><td>197.48 (n/a)</td><td>202.00 (n/a)</td><td>139.70 (n/a)</td><td>45.94 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 <b>(+64.76%)</b></td><td>0.05 <b>(+36.18%)</b></td><td>0.05 <b>(+20.36%)</b></td><td>0.04 <b>(+36.71%)</b></td><td>0.01 <b>(+88.76%)</b></td><td>212.20 <b>(-26.85%)</b></td><td>159.54 <b>(-25.46%)</b></td><td>158.40 (-16.94%)</td><td>113.30 <b>(-39.28%)</b></td><td>36.64 (-16.87%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>290.10 (n/a)</td><td>214.04 (n/a)</td><td>190.70 (n/a)</td><td>186.60 (n/a)</td><td>44.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.21 (+0.12%)</td><td>0.21 (-0.00%)</td><td>0.21 (-0.02%)</td><td>0.21 (-0.10%)</td><td>0.00 <b>(+21.65%)</b></td><td>40876.00 (+0.10%)</td><td>40742.86 (+0.00%)</td><td>40798.30 (+0.02%)</td><td>40430.80 (-0.12%)</td><td>179.98 <b>(+21.62%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40833.30 (n/a)</td><td>40741.08 (n/a)</td><td>40788.20 (n/a)</td><td>40478.90 (n/a)</td><td>147.99 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (-0.89%)</td><td>0.05 (-18.68%)</td><td>0.05 <b>(-29.99%)</b></td><td>0.04 (-18.45%)</td><td>0.01 (+12.44%)</td><td>208.80 <b>(+22.61%)</b></td><td>172.50 <b>(+24.73%)</b></td><td>180.70 <b>(+42.85%)</b></td><td>111.60 (+0.90%)</td><td>36.94 <b>(+29.30%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.30 (n/a)</td><td>138.30 (n/a)</td><td>126.50 (n/a)</td><td>110.60 (n/a)</td><td>28.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (-18.90%)</td><td>0.06 (-15.88%)</td><td>0.07 (-19.79%)</td><td>0.04 <b>(-32.10%)</b></td><td>0.02 (-15.35%)</td><td>326.20 <b>(+47.27%)</b></td><td>204.46 <b>(+20.82%)</b></td><td>182.20 <b>(+24.62%)</b></td><td>151.40 <b>(+23.29%)</b></td><td>69.67 <b>(+56.86%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>221.50 (n/a)</td><td>169.22 (n/a)</td><td>146.20 (n/a)</td><td>122.80 (n/a)</td><td>44.42 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (+13.68%)</td><td>0.05 (-1.73%)</td><td>0.05 (-6.68%)</td><td>0.03 <b>(-27.09%)</b></td><td>0.01 <b>(+136.25%)</b></td><td>251.10 <b>(+37.14%)</b></td><td>178.06 (+6.65%)</td><td>182.00 (+7.18%)</td><td>123.50 (-12.04%)</td><td>47.75 <b>(+189.79%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.10 (n/a)</td><td>166.96 (n/a)</td><td>169.80 (n/a)</td><td>140.40 (n/a)</td><td>16.48 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 <b>(-23.45%)</b></td><td>0.05 <b>(-22.67%)</b></td><td>0.05 <b>(-22.74%)</b></td><td>0.05 (-14.97%)</td><td>0.01 <b>(-41.72%)</b></td><td>217.50 (+17.63%)</td><td>192.44 <b>(+27.70%)</b></td><td>200.20 <b>(+29.41%)</b></td><td>154.70 <b>(+30.55%)</b></td><td>23.99 (-10.96%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>184.90 (n/a)</td><td>150.70 (n/a)</td><td>154.70 (n/a)</td><td>118.50 (n/a)</td><td>26.94 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (-3.69%)</td><td>0.05 (+0.92%)</td><td>0.05 (-11.41%)</td><td>0.04 <b>(+32.00%)</b></td><td>0.01 <b>(-26.62%)</b></td><td>208.70 <b>(-24.25%)</b></td><td>166.64 (-5.26%)</td><td>174.80 (+12.85%)</td><td>126.30 (+3.87%)</td><td>32.89 <b>(-45.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>275.50 (n/a)</td><td>175.90 (n/a)</td><td>154.90 (n/a)</td><td>121.60 (n/a)</td><td>60.04 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (-4.33%)</td><td>0.05 (-14.89%)</td><td>0.05 <b>(-20.65%)</b></td><td>0.04 <b>(-23.93%)</b></td><td>0.01 <b>(+89.61%)</b></td><td>242.70 <b>(+31.47%)</b></td><td>203.38 (+19.44%)</td><td>208.00 <b>(+25.98%)</b></td><td>162.20 (+4.51%)</td><td>32.24 <b>(+156.16%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>184.60 (n/a)</td><td>170.28 (n/a)</td><td>165.10 (n/a)</td><td>155.20 (n/a)</td><td>12.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (-4.54%)</td><td>0.05 (-12.59%)</td><td>0.04 (-9.50%)</td><td>0.03 (-10.93%)</td><td>0.01 (-10.62%)</td><td>235.50 (+12.25%)</td><td>186.42 (+13.99%)</td><td>182.60 (+10.47%)</td><td>125.70 (+4.84%)</td><td>41.86 (+4.52%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>163.54 (n/a)</td><td>165.30 (n/a)</td><td>119.90 (n/a)</td><td>40.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 <b>(-23.10%)</b></td><td>0.04 <b>(-27.47%)</b></td><td>0.04 (-15.80%)</td><td>0.03 <b>(-47.10%)</b></td><td>0.01 (+2.41%)</td><td>344.30 <b>(+89.07%)</b></td><td>231.20 <b>(+43.53%)</b></td><td>213.40 (+18.75%)</td><td>156.40 <b>(+30.12%)</b></td><td>70.77 <b>(+151.79%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>161.08 (n/a)</td><td>179.70 (n/a)</td><td>120.20 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 <b>(-20.08%)</b></td><td>0.04 (-18.48%)</td><td>0.04 (-17.03%)</td><td>0.03 <b>(-22.55%)</b></td><td>0.01 (-18.41%)</td><td>236.00 <b>(+29.10%)</b></td><td>191.28 <b>(+22.88%)</b></td><td>199.60 <b>(+20.53%)</b></td><td>145.40 <b>(+25.13%)</b></td><td>35.76 <b>(+30.64%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.80 (n/a)</td><td>155.66 (n/a)</td><td>165.60 (n/a)</td><td>116.20 (n/a)</td><td>27.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 <b>(-24.47%)</b></td><td>0.05 (-5.86%)</td><td>0.05 (+1.20%)</td><td>0.04 (+4.68%)</td><td>0.01 <b>(-52.20%)</b></td><td>218.20 (-4.47%)</td><td>181.88 (+3.15%)</td><td>179.10 (-1.16%)</td><td>159.70 <b>(+32.42%)</b></td><td>23.85 <b>(-38.06%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.40 (n/a)</td><td>176.32 (n/a)</td><td>181.20 (n/a)</td><td>120.60 (n/a)</td><td>38.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (-10.64%)</td><td>0.04 (-17.73%)</td><td>0.04 (-14.19%)</td><td>0.04 <b>(-24.87%)</b></td><td>0.01 <b>(+139.37%)</b></td><td>219.50 <b>(+33.11%)</b></td><td>194.68 <b>(+22.78%)</b></td><td>188.50 (+16.57%)</td><td>168.20 (+11.91%)</td><td>23.12 <b>(+265.13%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>164.90 (n/a)</td><td>158.56 (n/a)</td><td>161.70 (n/a)</td><td>150.30 (n/a)</td><td>6.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (-1.54%)</td><td>0.04 (-19.84%)</td><td>0.04 <b>(-28.98%)</b></td><td>0.03 <b>(-31.80%)</b></td><td>0.01 <b>(+53.16%)</b></td><td>299.70 <b>(+46.62%)</b></td><td>226.84 <b>(+28.30%)</b></td><td>229.50 <b>(+40.80%)</b></td><td>159.70 (+1.53%)</td><td>50.05 <b>(+124.20%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>176.80 (n/a)</td><td>163.00 (n/a)</td><td>157.30 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 <b>(-29.94%)</b></td><td>0.04 <b>(-20.44%)</b></td><td>0.04 <b>(-21.28%)</b></td><td>0.04 (-16.07%)</td><td>0.01 <b>(-41.42%)</b></td><td>231.00 (+19.20%)</td><td>206.48 <b>(+24.31%)</b></td><td>221.30 <b>(+27.04%)</b></td><td>173.50 <b>(+42.68%)</b></td><td>28.82 (+1.00%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>166.10 (n/a)</td><td>174.20 (n/a)</td><td>121.60 (n/a)</td><td>28.54 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (+10.16%)</td><td>0.04 (+0.96%)</td><td>0.04 (-2.43%)</td><td>0.04 (-3.43%)</td><td>0.01 <b>(+44.50%)</b></td><td>227.90 (+3.59%)</td><td>200.14 (-0.22%)</td><td>209.50 (+2.50%)</td><td>161.00 (-9.24%)</td><td>26.37 <b>(+34.48%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>220.00 (n/a)</td><td>200.58 (n/a)</td><td>204.40 (n/a)</td><td>177.40 (n/a)</td><td>19.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 <b>(+23.23%)</b></td><td>0.03 (-16.74%)</td><td>0.03 (-18.79%)</td><td>0.02 <b>(-38.57%)</b></td><td>0.01 <b>(+299.41%)</b></td><td>385.20 <b>(+62.81%)</b></td><td>277.24 <b>(+31.99%)</b></td><td>254.60 <b>(+23.11%)</b></td><td>156.00 (-18.88%)</td><td>90.63 <b>(+427.17%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>236.60 (n/a)</td><td>210.04 (n/a)</td><td>206.80 (n/a)</td><td>192.30 (n/a)</td><td>17.19 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.61 (-7.96%)</td><td>0.56 (+5.11%)</td><td>0.57 (+14.21%)</td><td>0.51 (+9.85%)</td><td>0.04 <b>(-49.17%)</b></td><td>193.10 (-8.96%)</td><td>176.42 (-6.00%)</td><td>173.90 (-12.44%)</td><td>161.80 (+8.66%)</td><td>12.90 <b>(-49.14%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.66 (n/a)</td><td>0.53 (n/a)</td><td>0.50 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>212.10 (n/a)</td><td>187.68 (n/a)</td><td>198.60 (n/a)</td><td>148.90 (n/a)</td><td>25.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.81 (+3.77%)</td><td>0.58 (-6.76%)</td><td>0.54 (-7.88%)</td><td>0.46 (-4.17%)</td><td>0.13 (-7.32%)</td><td>211.90 (+4.38%)</td><td>174.98 (+6.54%)</td><td>181.70 (+8.54%)</td><td>121.80 (-3.64%)</td><td>32.76 (-9.71%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.78 (n/a)</td><td>0.62 (n/a)</td><td>0.59 (n/a)</td><td>0.48 (n/a)</td><td>0.14 (n/a)</td><td>203.00 (n/a)</td><td>164.24 (n/a)</td><td>167.40 (n/a)</td><td>126.40 (n/a)</td><td>36.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.55 (-13.82%)</td><td>0.50 (-9.82%)</td><td>0.49 (-9.05%)</td><td>0.44 (-8.54%)</td><td>0.04 <b>(-30.32%)</b></td><td>224.10 (+9.32%)</td><td>198.96 (+10.45%)</td><td>202.10 (+9.96%)</td><td>179.20 (+15.99%)</td><td>17.84 (-11.67%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.64 (n/a)</td><td>0.55 (n/a)</td><td>0.53 (n/a)</td><td>0.48 (n/a)</td><td>0.06 (n/a)</td><td>205.00 (n/a)</td><td>180.14 (n/a)</td><td>183.80 (n/a)</td><td>154.50 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.76 (-2.02%)</td><td>0.58 (-2.99%)</td><td>0.63 (+14.79%)</td><td>0.32 <b>(-30.73%)</b></td><td>0.17 (+16.45%)</td><td>310.10 <b>(+44.37%)</b></td><td>186.48 (+7.88%)</td><td>156.50 (-12.91%)</td><td>129.80 (+2.04%)</td><td>71.79 <b>(+82.23%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.77 (n/a)</td><td>0.59 (n/a)</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.14 (n/a)</td><td>214.80 (n/a)</td><td>172.86 (n/a)</td><td>179.70 (n/a)</td><td>127.20 (n/a)</td><td>39.39 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.59 <b>(+23.81%)</b></td><td>0.44 (+6.37%)</td><td>0.41 (-0.27%)</td><td>0.34 (-0.59%)</td><td>0.09 <b>(+98.09%)</b></td><td>216.90 (+0.60%)</td><td>173.96 (-3.79%)</td><td>180.60 (+0.28%)</td><td>125.90 (-19.19%)</td><td>34.41 <b>(+56.08%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.47 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.05 (n/a)</td><td>215.60 (n/a)</td><td>180.82 (n/a)</td><td>180.10 (n/a)</td><td>155.80 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.48 (-13.79%)</td><td>0.45 (-3.01%)</td><td>0.46 (+9.46%)</td><td>0.41 (+12.29%)</td><td>0.04 <b>(-58.74%)</b></td><td>181.40 (-10.95%)</td><td>166.38 (+0.82%)</td><td>159.10 (-8.67%)</td><td>154.10 (+16.04%)</td><td>13.51 <b>(-55.37%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.09 (n/a)</td><td>203.70 (n/a)</td><td>165.02 (n/a)</td><td>174.20 (n/a)</td><td>132.80 (n/a)</td><td>30.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.49 (-12.23%)</td><td>0.42 (+4.44%)</td><td>0.43 (+19.24%)</td><td>0.35 (+14.71%)</td><td>0.05 <b>(-45.04%)</b></td><td>208.00 (-12.82%)</td><td>179.22 (-7.04%)</td><td>173.20 (-16.13%)</td><td>149.50 (+13.95%)</td><td>23.35 <b>(-43.62%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.56 (n/a)</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.10 (n/a)</td><td>238.60 (n/a)</td><td>192.80 (n/a)</td><td>206.50 (n/a)</td><td>131.20 (n/a)</td><td>41.42 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.48 (+11.99%)</td><td>0.42 (+19.58%)</td><td>0.47 <b>(+20.64%)</b></td><td>0.24 (-11.54%)</td><td>0.10 <b>(+56.18%)</b></td><td>301.40 (+13.05%)</td><td>185.84 (-12.93%)</td><td>158.10 (-17.09%)</td><td>153.90 (-10.68%)</td><td>64.63 <b>(+57.97%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.43 (n/a)</td><td>0.36 (n/a)</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.06 (n/a)</td><td>266.60 (n/a)</td><td>213.44 (n/a)</td><td>190.70 (n/a)</td><td>172.30 (n/a)</td><td>40.91 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.81 <b>(-32.26%)</b></td><td>0.70 (-4.68%)</td><td>0.76 <b>(+20.75%)</b></td><td>0.50 (-9.32%)</td><td>0.12 <b>(-53.14%)</b></td><td>261.70 (+10.24%)</td><td>191.64 (+0.37%)</td><td>173.00 (-17.19%)</td><td>162.10 <b>(+47.63%)</b></td><td>40.50 (-17.13%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.19 (n/a)</td><td>0.74 (n/a)</td><td>0.63 (n/a)</td><td>0.55 (n/a)</td><td>0.26 (n/a)</td><td>237.40 (n/a)</td><td>190.94 (n/a)</td><td>208.90 (n/a)</td><td>109.80 (n/a)</td><td>48.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.85 <b>(-21.86%)</b></td><td>0.74 (-4.74%)</td><td>0.70 (-3.20%)</td><td>0.67 (+8.94%)</td><td>0.07 <b>(-61.16%)</b></td><td>194.40 (-8.22%)</td><td>178.92 (+1.90%)</td><td>186.10 (+3.33%)</td><td>153.50 <b>(+27.92%)</b></td><td>16.10 <b>(-52.34%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.09 (n/a)</td><td>0.77 (n/a)</td><td>0.73 (n/a)</td><td>0.62 (n/a)</td><td>0.18 (n/a)</td><td>211.80 (n/a)</td><td>175.58 (n/a)</td><td>180.10 (n/a)</td><td>120.00 (n/a)</td><td>33.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.86 <b>(-24.67%)</b></td><td>0.67 (-18.17%)</td><td>0.66 (-16.86%)</td><td>0.53 (-19.42%)</td><td>0.13 <b>(-31.43%)</b></td><td>245.70 <b>(+24.09%)</b></td><td>199.76 <b>(+21.38%)</b></td><td>199.00 <b>(+20.24%)</b></td><td>152.00 <b>(+32.75%)</b></td><td>36.66 (+16.88%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>1.14 (n/a)</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.66 (n/a)</td><td>0.19 (n/a)</td><td>198.00 (n/a)</td><td>164.58 (n/a)</td><td>165.50 (n/a)</td><td>114.50 (n/a)</td><td>31.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.00 (+2.27%)</td><td>0.00 (-0.47%)</td><td>0.00 (+0.00%)</td><td>0.00 (-2.50%)</td><td>0.00 <b>(+40.11%)</b></td><td>1037.49 (+2.04%)</td><td>956.12 (+0.01%)</td><td>947.41 (-0.19%)</td><td>905.60 (-1.89%)</td><td>50.85 <b>(+42.49%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1016.71 (n/a)</td><td>956.02 (n/a)</td><td>949.25 (n/a)</td><td>923.02 (n/a)</td><td>35.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.01 (+2.38%)</td><td>0.01 (-0.25%)</td><td>0.01 (+0.00%)</td><td>0.01 (-1.30%)</td><td>0.00 <b>(+34.37%)</b></td><td>1077.88 (+1.01%)</td><td>1013.20 (+0.27%)</td><td>1010.99 (+0.20%)</td><td>957.36 (-1.85%)</td><td>44.02 <b>(+25.23%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1067.08 (n/a)</td><td>1010.43 (n/a)</td><td>1009.02 (n/a)</td><td>975.38 (n/a)</td><td>35.15 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.98 (+3.29%)</td><td>0.94 (-0.28%)</td><td>0.93 (-1.39%)</td><td>0.93 (-1.36%)</td><td>0.02 <b>(+598.62%)</b></td><td>2261.74 (+1.38%)</td><td>2228.73 (+0.32%)</td><td>2253.53 (+1.41%)</td><td>2140.39 (-3.18%)</td><td>50.60 <b>(+583.64%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.00 (n/a)</td><td>2230.96 (n/a)</td><td>2221.62 (n/a)</td><td>2222.18 (n/a)</td><td>2210.72 (n/a)</td><td>7.40 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>3.65 (+9.51%)</td><td>3.32 <b>(+24.19%)</b></td><td>3.41 <b>(+31.76%)</b></td><td>2.74 (+16.35%)</td><td>0.34 (-10.44%)</td><td>191.40 (-14.05%)</td><td>159.40 (-19.85%)</td><td>153.70 <b>(-24.10%)</b></td><td>143.80 (-8.64%)</td><td>18.44 <b>(-25.95%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>3.33 (n/a)</td><td>2.67 (n/a)</td><td>2.59 (n/a)</td><td>2.35 (n/a)</td><td>0.38 (n/a)</td><td>222.70 (n/a)</td><td>198.88 (n/a)</td><td>202.50 (n/a)</td><td>157.40 (n/a)</td><td>24.91 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>6.46 (+12.75%)</td><td>5.06 (+14.37%)</td><td>5.14 <b>(+21.05%)</b></td><td>4.18 <b>(+20.69%)</b></td><td>0.91 (+5.88%)</td><td>250.70 (-17.15%)</td><td>212.42 (-12.96%)</td><td>204.10 (-17.40%)</td><td>162.40 (-11.31%)</td><td>35.76 <b>(-20.42%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>5.73 (n/a)</td><td>4.42 (n/a)</td><td>4.24 (n/a)</td><td>3.47 (n/a)</td><td>0.86 (n/a)</td><td>302.60 (n/a)</td><td>244.04 (n/a)</td><td>247.10 (n/a)</td><td>183.10 (n/a)</td><td>44.94 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>3.54 (+18.62%)</td><td>3.07 <b>(+20.49%)</b></td><td>3.10 (+13.35%)</td><td>2.66 <b>(+34.06%)</b></td><td>0.37 (-7.98%)</td><td>197.40 <b>(-25.40%)</b></td><td>172.60 (-17.84%)</td><td>169.30 (-11.78%)</td><td>148.20 (-15.70%)</td><td>20.94 <b>(-42.09%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:37:47</td><td>2.98 (n/a)</td><td>2.55 (n/a)</td><td>2.73 (n/a)</td><td>1.98 (n/a)</td><td>0.40 (n/a)</td><td>264.60 (n/a)</td><td>210.08 (n/a)</td><td>191.90 (n/a)</td><td>175.80 (n/a)</td><td>36.16 (n/a)</td>
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
