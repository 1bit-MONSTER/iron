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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.10 (-4.42%)</td><td>0.07 (-9.21%)</td><td>0.07 (-7.47%)</td><td>0.06 (-8.34%)</td><td>0.01 (-12.44%)</td><td>196.90 (+9.09%)</td><td>168.92 (+9.76%)</td><td>175.40 (+8.07%)</td><td>129.20 (+4.62%)</td><td>24.73 (-2.60%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.50 (n/a)</td><td>153.90 (n/a)</td><td>162.30 (n/a)</td><td>123.50 (n/a)</td><td>25.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.09 (-10.83%)</td><td>0.08 (-5.09%)</td><td>0.08 (-2.27%)</td><td>0.06 (+4.50%)</td><td>0.01 <b>(-33.05%)</b></td><td>195.60 (-4.31%)</td><td>162.86 (+2.43%)</td><td>153.70 (+2.33%)</td><td>131.30 (+12.13%)</td><td>30.60 <b>(-27.20%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>204.40 (n/a)</td><td>159.00 (n/a)</td><td>150.20 (n/a)</td><td>117.10 (n/a)</td><td>42.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 <b>(-26.55%)</b></td><td>0.06 (-19.58%)</td><td>0.06 (-16.15%)</td><td>0.05 (-7.38%)</td><td>0.01 <b>(-59.50%)</b></td><td>224.70 (+7.98%)</td><td>195.30 <b>(+21.09%)</b></td><td>190.80 (+19.25%)</td><td>172.80 <b>(+36.06%)</b></td><td>20.87 <b>(-38.84%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>208.10 (n/a)</td><td>161.28 (n/a)</td><td>160.00 (n/a)</td><td>127.00 (n/a)</td><td>34.12 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 <b>(-21.66%)</b></td><td>0.06 (-14.13%)</td><td>0.06 (-17.22%)</td><td>0.06 <b>(+42.49%)</b></td><td>0.01 <b>(-63.49%)</b></td><td>216.10 <b>(-29.81%)</b></td><td>196.70 (+4.97%)</td><td>203.40 <b>(+20.86%)</b></td><td>152.90 <b>(+27.74%)</b></td><td>25.06 <b>(-67.48%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>307.90 (n/a)</td><td>187.38 (n/a)</td><td>168.30 (n/a)</td><td>119.70 (n/a)</td><td>77.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (-3.10%)</td><td>0.03 (-18.11%)</td><td>0.03 (-12.88%)</td><td>0.01 <b>(-46.01%)</b></td><td>0.01 <b>(+101.25%)</b></td><td>371.10 <b>(+85.18%)</b></td><td>213.94 <b>(+36.35%)</b></td><td>171.80 (+14.84%)</td><td>137.20 (+3.24%)</td><td>95.75 <b>(+275.54%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>200.40 (n/a)</td><td>156.90 (n/a)</td><td>149.60 (n/a)</td><td>132.90 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 <b>(-21.02%)</b></td><td>0.03 <b>(-20.68%)</b></td><td>0.03 <b>(-22.53%)</b></td><td>0.03 (-15.98%)</td><td>0.00 <b>(-29.15%)</b></td><td>191.40 (+19.03%)</td><td>176.58 <b>(+25.77%)</b></td><td>186.30 <b>(+29.11%)</b></td><td>155.70 <b>(+26.59%)</b></td><td>17.05 (+8.67%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>160.80 (n/a)</td><td>140.40 (n/a)</td><td>144.30 (n/a)</td><td>123.00 (n/a)</td><td>15.69 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 <b>(-20.81%)</b></td><td>0.03 (-14.04%)</td><td>0.03 (-12.33%)</td><td>0.03 (-16.04%)</td><td>0.00 <b>(-36.17%)</b></td><td>189.60 (+19.10%)</td><td>165.66 (+15.44%)</td><td>172.00 (+14.06%)</td><td>135.50 <b>(+26.28%)</b></td><td>20.13 (-2.76%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>159.20 (n/a)</td><td>143.50 (n/a)</td><td>150.80 (n/a)</td><td>107.30 (n/a)</td><td>20.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 <b>(-44.41%)</b></td><td>0.03 <b>(-21.91%)</b></td><td>0.03 <b>(-21.76%)</b></td><td>0.02 (-8.18%)</td><td>0.00 <b>(-68.55%)</b></td><td>222.30 (+8.92%)</td><td>185.54 (+19.80%)</td><td>194.10 <b>(+27.78%)</b></td><td>157.10 <b>(+79.95%)</b></td><td>27.53 <b>(-37.35%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.10 (n/a)</td><td>154.88 (n/a)</td><td>151.90 (n/a)</td><td>87.30 (n/a)</td><td>43.94 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (-1.65%)</td><td>0.03 (-0.76%)</td><td>0.03 (-8.89%)</td><td>0.03 (+15.77%)</td><td>0.01 (-16.69%)</td><td>203.60 (-13.62%)</td><td>168.10 (-1.16%)</td><td>171.40 (+9.73%)</td><td>122.90 (+1.65%)</td><td>30.18 <b>(-29.48%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.70 (n/a)</td><td>170.08 (n/a)</td><td>156.20 (n/a)</td><td>120.90 (n/a)</td><td>42.79 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (+10.89%)</td><td>0.03 (-6.99%)</td><td>0.03 (-11.68%)</td><td>0.02 (-14.13%)</td><td>0.01 <b>(+54.36%)</b></td><td>223.80 (+16.44%)</td><td>181.28 (+9.72%)</td><td>177.10 (+13.24%)</td><td>130.10 (-9.84%)</td><td>36.02 <b>(+60.15%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.20 (n/a)</td><td>165.22 (n/a)</td><td>156.40 (n/a)</td><td>144.30 (n/a)</td><td>22.49 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (+1.72%)</td><td>0.03 (-11.47%)</td><td>0.03 <b>(-21.93%)</b></td><td>0.02 (-7.07%)</td><td>0.01 <b>(+32.10%)</b></td><td>215.20 (+7.60%)</td><td>193.16 (+14.87%)</td><td>207.50 <b>(+28.09%)</b></td><td>128.70 (-1.76%)</td><td>36.20 <b>(+36.91%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>168.16 (n/a)</td><td>162.00 (n/a)</td><td>131.00 (n/a)</td><td>26.44 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 <b>(+43.01%)</b></td><td>0.03 (-6.60%)</td><td>0.02 <b>(-21.77%)</b></td><td>0.02 (-13.27%)</td><td>0.01 <b>(+313.92%)</b></td><td>239.30 (+15.33%)</td><td>210.72 (+14.65%)</td><td>233.10 <b>(+27.87%)</b></td><td>118.80 <b>(-30.08%)</b></td><td>51.73 <b>(+230.85%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>207.50 (n/a)</td><td>183.80 (n/a)</td><td>182.30 (n/a)</td><td>169.90 (n/a)</td><td>15.64 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>235.80 (n/a)</td><td>186.28 (n/a)</td><td>182.10 (n/a)</td><td>147.10 (n/a)</td><td>38.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>194.10 (n/a)</td><td>153.10 (n/a)</td><td>149.90 (n/a)</td><td>120.30 (n/a)</td><td>29.15 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>221.30 (n/a)</td><td>158.12 (n/a)</td><td>157.30 (n/a)</td><td>113.90 (n/a)</td><td>39.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>197.08 (n/a)</td><td>203.20 (n/a)</td><td>163.70 (n/a)</td><td>22.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>185.80 (n/a)</td><td>155.86 (n/a)</td><td>152.30 (n/a)</td><td>137.60 (n/a)</td><td>19.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.30 (n/a)</td><td>170.38 (n/a)</td><td>167.60 (n/a)</td><td>139.10 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>187.10 (n/a)</td><td>164.76 (n/a)</td><td>170.80 (n/a)</td><td>120.90 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>305.40 (n/a)</td><td>200.22 (n/a)</td><td>190.10 (n/a)</td><td>125.10 (n/a)</td><td>65.53 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.80 (n/a)</td><td>173.64 (n/a)</td><td>154.20 (n/a)</td><td>142.30 (n/a)</td><td>38.61 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>296.90 (n/a)</td><td>196.18 (n/a)</td><td>185.10 (n/a)</td><td>131.70 (n/a)</td><td>69.04 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.40 (n/a)</td><td>151.32 (n/a)</td><td>141.00 (n/a)</td><td>128.10 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.60 (n/a)</td><td>209.80 (n/a)</td><td>194.90 (n/a)</td><td>147.70 (n/a)</td><td>58.87 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>273.50 (n/a)</td><td>179.30 (n/a)</td><td>156.70 (n/a)</td><td>103.80 (n/a)</td><td>63.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>177.60 (n/a)</td><td>177.80 (n/a)</td><td>143.00 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>173.96 (n/a)</td><td>189.00 (n/a)</td><td>113.90 (n/a)</td><td>49.98 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>315.60 (n/a)</td><td>243.20 (n/a)</td><td>225.90 (n/a)</td><td>191.00 (n/a)</td><td>47.27 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>4.79 (+11.84%)</td><td>4.32 (+15.47%)</td><td>4.22 (+18.13%)</td><td>4.07 <b>(+23.08%)</b></td><td>0.29 <b>(-31.87%)</b></td><td>2309.20 (-18.75%)</td><td>2182.96 (-13.97%)</td><td>2230.30 (-15.35%)</td><td>1964.20 (-10.59%)</td><td>138.35 <b>(-50.30%)</b></td><td>1883.36 (+11.84%)</td><td>1700.40 (+15.47%)</td><td>1658.70 (+18.13%)</td><td>1602.04 <b>(+23.08%)</b></td><td>113.26 <b>(-31.87%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>4.28 (n/a)</td><td>3.74 (n/a)</td><td>3.57 (n/a)</td><td>3.31 (n/a)</td><td>0.42 (n/a)</td><td>2842.20 (n/a)</td><td>2537.34 (n/a)</td><td>2634.70 (n/a)</td><td>2196.90 (n/a)</td><td>278.38 (n/a)</td><td>1683.93 (n/a)</td><td>1472.54 (n/a)</td><td>1404.08 (n/a)</td><td>1301.60 (n/a)</td><td>166.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.35 <b>(+42.02%)</b></td><td>1.11 <b>(+32.59%)</b></td><td>1.03 (+11.38%)</td><td>1.02 <b>(+58.15%)</b></td><td>0.14 (-0.59%)</td><td>216.60 <b>(-36.76%)</b></td><td>202.06 <b>(-25.59%)</b></td><td>214.20 (-10.23%)</td><td>164.30 <b>(-29.58%)</b></td><td>22.20 <b>(-55.14%)</b></td><td>57.45 <b>(+42.02%)</b></td><td>47.22 <b>(+32.59%)</b></td><td>44.05 (+11.38%)</td><td>43.58 <b>(+58.15%)</b></td><td>5.91 (-0.59%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.95 (n/a)</td><td>0.83 (n/a)</td><td>0.93 (n/a)</td><td>0.65 (n/a)</td><td>0.14 (n/a)</td><td>342.50 (n/a)</td><td>271.54 (n/a)</td><td>238.60 (n/a)</td><td>233.30 (n/a)</td><td>49.48 (n/a)</td><td>40.45 (n/a)</td><td>35.62 (n/a)</td><td>39.55 (n/a)</td><td>27.55 (n/a)</td><td>5.94 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.29 (-10.68%)</td><td>1.09 (+12.34%)</td><td>1.10 (+16.64%)</td><td>0.77 (+15.09%)</td><td>0.21 <b>(-31.69%)</b></td><td>288.40 (-13.11%)</td><td>210.24 (-14.53%)</td><td>202.00 (-14.26%)</td><td>172.00 (+11.98%)</td><td>47.30 <b>(-34.55%)</b></td><td>54.87 (-10.68%)</td><td>46.49 (+12.34%)</td><td>46.73 (+16.64%)</td><td>32.72 (+15.09%)</td><td>9.01 <b>(-31.69%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.44 (n/a)</td><td>0.97 (n/a)</td><td>0.94 (n/a)</td><td>0.67 (n/a)</td><td>0.31 (n/a)</td><td>331.90 (n/a)</td><td>245.98 (n/a)</td><td>235.60 (n/a)</td><td>153.60 (n/a)</td><td>72.27 (n/a)</td><td>61.42 (n/a)</td><td>41.38 (n/a)</td><td>40.06 (n/a)</td><td>28.43 (n/a)</td><td>13.19 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.52 (-0.42%)</td><td>0.52 (-0.14%)</td><td>0.52 (-0.07%)</td><td>0.52 (+0.02%)</td><td>0.00 <b>(-39.96%)</b></td><td>48672.10 (-0.02%)</td><td>48529.98 (+0.14%)</td><td>48474.50 (+0.07%)</td><td>48454.00 (+0.42%)</td><td>93.07 <b>(-39.73%)</b></td><td>354.56 (-0.42%)</td><td>354.01 (-0.14%)</td><td>354.41 (-0.07%)</td><td>352.97 (+0.02%)</td><td>0.68 <b>(-39.96%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48682.60 (n/a)</td><td>48463.86 (n/a)</td><td>48442.10 (n/a)</td><td>48251.30 (n/a)</td><td>154.42 (n/a)</td><td>356.05 (n/a)</td><td>354.49 (n/a)</td><td>354.65 (n/a)</td><td>352.90 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.91 (-0.85%)</td><td>0.90 (+0.41%)</td><td>0.90 (+1.57%)</td><td>0.89 (+0.67%)</td><td>0.01 <b>(-41.80%)</b></td><td>28280.30 (-0.67%)</td><td>28017.84 (-0.42%)</td><td>27931.50 (-1.54%)</td><td>27747.40 (+0.86%)</td><td>238.53 <b>(-41.64%)</b></td><td>619.15 (-0.85%)</td><td>613.21 (+0.41%)</td><td>615.07 (+1.57%)</td><td>607.48 (+0.67%)</td><td>5.21 <b>(-41.80%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28470.20 (n/a)</td><td>28136.12 (n/a)</td><td>28369.00 (n/a)</td><td>27511.30 (n/a)</td><td>408.70 (n/a)</td><td>624.47 (n/a)</td><td>610.70 (n/a)</td><td>605.59 (n/a)</td><td>603.43 (n/a)</td><td>8.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>3.46 (+6.10%)</td><td>3.28 (+3.89%)</td><td>3.33 (+5.05%)</td><td>3.06 (-0.37%)</td><td>0.16 <b>(+105.63%)</b></td><td>8213.40 (+0.37%)</td><td>7685.64 (-3.60%)</td><td>7550.90 (-4.81%)</td><td>7273.00 (-5.75%)</td><td>385.03 <b>(+94.18%)</b></td><td>2362.13 (+6.10%)</td><td>2239.74 (+3.89%)</td><td>2275.20 (+5.05%)</td><td>2091.69 (-0.37%)</td><td>110.47 <b>(+105.63%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>3.26 (n/a)</td><td>3.16 (n/a)</td><td>3.17 (n/a)</td><td>3.08 (n/a)</td><td>0.08 (n/a)</td><td>8182.90 (n/a)</td><td>7972.88 (n/a)</td><td>7932.40 (n/a)</td><td>7716.40 (n/a)</td><td>198.29 (n/a)</td><td>2226.40 (n/a)</td><td>2155.85 (n/a)</td><td>2165.78 (n/a)</td><td>2099.47 (n/a)</td><td>53.72 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>4.18 (-0.05%)</td><td>3.69 (-4.04%)</td><td>3.87 (+1.41%)</td><td>2.96 (-17.57%)</td><td>0.47 <b>(+101.54%)</b></td><td>2727.00 <b>(+21.31%)</b></td><td>2214.94 (+5.40%)</td><td>2082.00 (-1.39%)</td><td>1929.90 (+0.06%)</td><td>309.71 <b>(+149.95%)</b></td><td>1095.38 (-0.05%)</td><td>967.97 (-4.04%)</td><td>1015.32 (+1.41%)</td><td>775.17 (-17.57%)</td><td>121.95 <b>(+101.54%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>4.18 (n/a)</td><td>3.85 (n/a)</td><td>3.82 (n/a)</td><td>3.59 (n/a)</td><td>0.23 (n/a)</td><td>2247.90 (n/a)</td><td>2101.46 (n/a)</td><td>2111.30 (n/a)</td><td>1928.80 (n/a)</td><td>123.91 (n/a)</td><td>1095.97 (n/a)</td><td>1008.77 (n/a)</td><td>1001.22 (n/a)</td><td>940.39 (n/a)</td><td>60.51 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.51 <b>(+48.58%)</b></td><td>0.45 <b>(+43.35%)</b></td><td>0.49 <b>(+52.81%)</b></td><td>0.28 (-2.85%)</td><td>0.10 <b>(+297.71%)</b></td><td>4481.30 (+2.94%)</td><td>2897.20 <b>(-26.69%)</b></td><td>2521.40 <b>(-34.56%)</b></td><td>2465.40 <b>(-32.69%)</b></td><td>886.11 <b>(+180.34%)</b></td><td>27.22 <b>(+48.58%)</b></td><td>24.46 <b>(+43.35%)</b></td><td>26.62 <b>(+52.81%)</b></td><td>14.98 (-2.85%)</td><td>5.32 <b>(+297.71%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.02 (n/a)</td><td>4353.40 (n/a)</td><td>3952.24 (n/a)</td><td>3852.90 (n/a)</td><td>3662.90 (n/a)</td><td>316.08 (n/a)</td><td>18.32 (n/a)</td><td>17.07 (n/a)</td><td>17.42 (n/a)</td><td>15.42 (n/a)</td><td>1.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>5.23 (+5.43%)</td><td>4.70 (+13.62%)</td><td>4.79 <b>(+27.89%)</b></td><td>3.71 (+10.27%)</td><td>0.58 <b>(-23.04%)</b></td><td>1790.60 (-9.32%)</td><td>1435.16 (-13.01%)</td><td>1389.50 <b>(-21.81%)</b></td><td>1271.10 (-5.16%)</td><td>204.62 <b>(-29.23%)</b></td><td>1616.82 (+5.43%)</td><td>1452.44 (+13.62%)</td><td>1479.11 <b>(+27.89%)</b></td><td>1147.76 (+10.27%)</td><td>179.51 <b>(-23.04%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>4.96 (n/a)</td><td>4.14 (n/a)</td><td>3.74 (n/a)</td><td>3.37 (n/a)</td><td>0.75 (n/a)</td><td>1974.60 (n/a)</td><td>1649.88 (n/a)</td><td>1777.00 (n/a)</td><td>1340.20 (n/a)</td><td>289.15 (n/a)</td><td>1533.51 (n/a)</td><td>1278.28 (n/a)</td><td>1156.54 (n/a)</td><td>1040.82 (n/a)</td><td>233.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>13.18 (n/a)</td><td>12.17 (n/a)</td><td>12.35 (n/a)</td><td>10.75 (n/a)</td><td>1.08 (n/a)</td><td>13.17 (n/a)</td><td>12.16 (n/a)</td><td>12.34 (n/a)</td><td>10.75 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>24.62 (-1.52%)</td><td>23.69 (-1.13%)</td><td>23.82 (-1.67%)</td><td>21.85 (-2.10%)</td><td>1.09 (+10.44%)</td><td>24.60 (-1.52%)</td><td>23.68 (-1.13%)</td><td>23.80 (-1.67%)</td><td>21.84 (-2.10%)</td><td>1.09 (+10.44%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>25.00 (n/a)</td><td>23.96 (n/a)</td><td>24.22 (n/a)</td><td>22.32 (n/a)</td><td>0.99 (n/a)</td><td>24.98 (n/a)</td><td>23.95 (n/a)</td><td>24.21 (n/a)</td><td>22.31 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>39.70 (-6.82%)</td><td>38.16 (-4.32%)</td><td>38.71 (-1.01%)</td><td>34.96 (-8.42%)</td><td>1.87 (+7.02%)</td><td>39.68 (-6.82%)</td><td>38.14 (-4.32%)</td><td>38.69 (-1.01%)</td><td>34.94 (-8.42%)</td><td>1.87 (+7.02%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>42.61 (n/a)</td><td>39.88 (n/a)</td><td>39.11 (n/a)</td><td>38.18 (n/a)</td><td>1.75 (n/a)</td><td>42.58 (n/a)</td><td>39.86 (n/a)</td><td>39.08 (n/a)</td><td>38.15 (n/a)</td><td>1.75 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>45.66 (+3.62%)</td><td>42.91 (+13.14%)</td><td>43.95 (+12.65%)</td><td>39.37 <b>(+56.37%)</b></td><td>2.85 <b>(-62.65%)</b></td><td>45.63 (+3.62%)</td><td>42.89 (+13.14%)</td><td>43.92 (+12.65%)</td><td>39.35 <b>(+56.37%)</b></td><td>2.85 <b>(-62.65%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>44.06 (n/a)</td><td>37.93 (n/a)</td><td>39.01 (n/a)</td><td>25.18 (n/a)</td><td>7.63 (n/a)</td><td>44.04 (n/a)</td><td>37.91 (n/a)</td><td>38.99 (n/a)</td><td>25.16 (n/a)</td><td>7.63 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>13.11 (n/a)</td><td>12.20 (n/a)</td><td>12.35 (n/a)</td><td>10.70 (n/a)</td><td>0.90 (n/a)</td><td>13.10 (n/a)</td><td>12.19 (n/a)</td><td>12.34 (n/a)</td><td>10.70 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>24.83 (-1.51%)</td><td>22.97 (-6.04%)</td><td>24.18 (+0.26%)</td><td>18.04 <b>(-24.32%)</b></td><td>2.81 <b>(+333.28%)</b></td><td>24.81 (-1.51%)</td><td>22.96 (-6.04%)</td><td>24.17 (+0.26%)</td><td>18.03 <b>(-24.32%)</b></td><td>2.81 <b>(+333.28%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>25.21 (n/a)</td><td>24.45 (n/a)</td><td>24.12 (n/a)</td><td>23.83 (n/a)</td><td>0.65 (n/a)</td><td>25.19 (n/a)</td><td>24.43 (n/a)</td><td>24.10 (n/a)</td><td>23.82 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>42.24 (+2.36%)</td><td>39.41 (+5.32%)</td><td>39.47 (+0.74%)</td><td>37.44 (+14.26%)</td><td>2.02 <b>(-45.69%)</b></td><td>42.22 (+2.36%)</td><td>39.38 (+5.32%)</td><td>39.44 (+0.74%)</td><td>37.42 (+14.26%)</td><td>2.01 <b>(-45.69%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>41.27 (n/a)</td><td>37.41 (n/a)</td><td>39.18 (n/a)</td><td>32.77 (n/a)</td><td>3.71 (n/a)</td><td>41.25 (n/a)</td><td>37.39 (n/a)</td><td>39.15 (n/a)</td><td>32.75 (n/a)</td><td>3.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>44.67 (+4.87%)</td><td>42.67 (+6.97%)</td><td>43.25 (+8.22%)</td><td>38.61 (+5.36%)</td><td>2.35 (+3.26%)</td><td>44.64 (+4.87%)</td><td>42.64 (+6.97%)</td><td>43.22 (+8.22%)</td><td>38.59 (+5.36%)</td><td>2.35 (+3.26%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>42.59 (n/a)</td><td>39.89 (n/a)</td><td>39.96 (n/a)</td><td>36.65 (n/a)</td><td>2.27 (n/a)</td><td>42.56 (n/a)</td><td>39.87 (n/a)</td><td>39.94 (n/a)</td><td>36.62 (n/a)</td><td>2.27 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>9.08 (-4.34%)</td><td>8.65 (-4.47%)</td><td>8.78 (-2.92%)</td><td>8.16 (-4.03%)</td><td>0.45 (+9.39%)</td><td>9.06 (-4.34%)</td><td>8.63 (-4.47%)</td><td>8.76 (-2.92%)</td><td>8.14 (-4.03%)</td><td>0.45 (+9.39%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>9.49 (n/a)</td><td>9.06 (n/a)</td><td>9.05 (n/a)</td><td>8.50 (n/a)</td><td>0.41 (n/a)</td><td>9.47 (n/a)</td><td>9.04 (n/a)</td><td>9.03 (n/a)</td><td>8.48 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.00 (+3.12%)</td><td>0.89 (-3.74%)</td><td>0.92 (+0.41%)</td><td>0.77 (-14.60%)</td><td>0.09 <b>(+158.93%)</b></td><td>0.98 (+3.12%)</td><td>0.88 (-3.74%)</td><td>0.91 (+0.41%)</td><td>0.75 (-14.60%)</td><td>0.09 <b>(+158.93%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.97 (n/a)</td><td>0.93 (n/a)</td><td>0.92 (n/a)</td><td>0.90 (n/a)</td><td>0.03 (n/a)</td><td>0.95 (n/a)</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.36 (+1.36%)</td><td>1.17 (-3.46%)</td><td>1.14 (-7.96%)</td><td>1.04 (+1.14%)</td><td>0.13 (-8.19%)</td><td>1.35 (+1.36%)</td><td>1.16 (-3.46%)</td><td>1.13 (-7.96%)</td><td>1.02 (+1.14%)</td><td>0.12 (-8.19%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.34 (n/a)</td><td>1.22 (n/a)</td><td>1.24 (n/a)</td><td>1.02 (n/a)</td><td>0.14 (n/a)</td><td>1.33 (n/a)</td><td>1.20 (n/a)</td><td>1.23 (n/a)</td><td>1.01 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>17.83 (-4.33%)</td><td>15.59 (-12.67%)</td><td>14.72 (-17.22%)</td><td>14.43 (-15.09%)</td><td>1.44 <b>(+136.40%)</b></td><td>17.63 (-4.33%)</td><td>15.40 (-12.67%)</td><td>14.55 (-17.22%)</td><td>14.26 (-15.09%)</td><td>1.42 <b>(+136.40%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>18.64 (n/a)</td><td>17.85 (n/a)</td><td>17.79 (n/a)</td><td>17.00 (n/a)</td><td>0.61 (n/a)</td><td>18.43 (n/a)</td><td>17.64 (n/a)</td><td>17.58 (n/a)</td><td>16.80 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>13.47 (-3.77%)</td><td>13.18 (-3.57%)</td><td>13.29 (-2.96%)</td><td>12.53 (-5.53%)</td><td>0.38 (+16.66%)</td><td>13.24 (-3.77%)</td><td>12.95 (-3.57%)</td><td>13.06 (-2.96%)</td><td>12.31 (-5.53%)</td><td>0.37 (+16.66%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>14.00 (n/a)</td><td>13.67 (n/a)</td><td>13.69 (n/a)</td><td>13.26 (n/a)</td><td>0.32 (n/a)</td><td>13.75 (n/a)</td><td>13.43 (n/a)</td><td>13.45 (n/a)</td><td>13.03 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>8.15 (-16.95%)</td><td>7.36 (-10.94%)</td><td>7.46 (-5.41%)</td><td>6.45 (-14.99%)</td><td>0.63 <b>(-29.00%)</b></td><td>8.01 (-16.95%)</td><td>7.24 (-10.94%)</td><td>7.33 (-5.41%)</td><td>6.34 (-14.99%)</td><td>0.62 <b>(-29.00%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>9.81 (n/a)</td><td>8.27 (n/a)</td><td>7.88 (n/a)</td><td>7.59 (n/a)</td><td>0.89 (n/a)</td><td>9.64 (n/a)</td><td>8.12 (n/a)</td><td>7.75 (n/a)</td><td>7.46 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>6.04 (-2.10%)</td><td>5.22 (-9.01%)</td><td>5.56 (-2.29%)</td><td>4.43 (-14.32%)</td><td>0.73 <b>(+64.73%)</b></td><td>5.95 (-2.10%)</td><td>5.13 (-9.01%)</td><td>5.47 (-2.29%)</td><td>4.36 (-14.32%)</td><td>0.72 <b>(+64.73%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>6.17 (n/a)</td><td>5.73 (n/a)</td><td>5.69 (n/a)</td><td>5.17 (n/a)</td><td>0.44 (n/a)</td><td>6.08 (n/a)</td><td>5.64 (n/a)</td><td>5.59 (n/a)</td><td>5.08 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>13.31 (n/a)</td><td>11.72 (n/a)</td><td>11.21 (n/a)</td><td>10.78 (n/a)</td><td>1.01 (n/a)</td><td>13.30 (n/a)</td><td>11.72 (n/a)</td><td>11.20 (n/a)</td><td>10.78 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>13.43 (n/a)</td><td>12.63 (n/a)</td><td>12.91 (n/a)</td><td>11.01 (n/a)</td><td>0.97 (n/a)</td><td>13.42 (n/a)</td><td>12.63 (n/a)</td><td>12.90 (n/a)</td><td>11.00 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.20 (n/a)</td><td>185.24 (n/a)</td><td>192.20 (n/a)</td><td>159.60 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>293.50 (n/a)</td><td>171.88 (n/a)</td><td>156.80 (n/a)</td><td>96.80 (n/a)</td><td>75.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.10 (n/a)</td><td>171.26 (n/a)</td><td>187.50 (n/a)</td><td>134.20 (n/a)</td><td>32.07 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>164.12 (n/a)</td><td>167.30 (n/a)</td><td>128.50 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>181.90 (n/a)</td><td>197.90 (n/a)</td><td>144.80 (n/a)</td><td>26.19 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>221.50 (n/a)</td><td>196.44 (n/a)</td><td>196.60 (n/a)</td><td>169.40 (n/a)</td><td>19.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>168.32 (n/a)</td><td>188.80 (n/a)</td><td>123.70 (n/a)</td><td>35.31 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>222.20 (n/a)</td><td>194.48 (n/a)</td><td>182.00 (n/a)</td><td>176.80 (n/a)</td><td>20.44 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (+12.82%)</td><td>0.06 <b>(+23.20%)</b></td><td>0.06 <b>(+27.32%)</b></td><td>0.04 (+19.41%)</td><td>0.01 (+13.42%)</td><td>190.70 (-16.25%)</td><td>149.20 (-18.96%)</td><td>134.70 <b>(-21.46%)</b></td><td>129.30 (-11.32%)</td><td>26.55 (-17.91%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>184.10 (n/a)</td><td>171.50 (n/a)</td><td>145.80 (n/a)</td><td>32.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 <b>(+48.09%)</b></td><td>0.06 <b>(+37.44%)</b></td><td>0.06 <b>(+44.90%)</b></td><td>0.04 (+0.91%)</td><td>0.01 <b>(+344.74%)</b></td><td>199.40 (-0.94%)</td><td>144.04 <b>(-24.44%)</b></td><td>132.80 <b>(-30.98%)</b></td><td>116.20 <b>(-32.48%)</b></td><td>34.83 <b>(+191.81%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>201.30 (n/a)</td><td>190.62 (n/a)</td><td>192.40 (n/a)</td><td>172.10 (n/a)</td><td>11.93 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (+5.10%)</td><td>0.05 (+6.84%)</td><td>0.05 (+17.37%)</td><td>0.04 (-5.62%)</td><td>0.01 (+15.08%)</td><td>214.40 (+5.98%)</td><td>168.80 (-5.84%)</td><td>162.60 (-14.82%)</td><td>133.70 (-4.84%)</td><td>29.20 (+19.26%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>179.26 (n/a)</td><td>190.90 (n/a)</td><td>140.50 (n/a)</td><td>24.48 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (+1.73%)</td><td>0.05 (+0.63%)</td><td>0.05 (+0.30%)</td><td>0.04 (-7.22%)</td><td>0.01 <b>(+25.51%)</b></td><td>190.20 (+7.76%)</td><td>156.52 (+1.02%)</td><td>169.10 (-0.29%)</td><td>115.00 (-1.71%)</td><td>34.55 <b>(+30.63%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.50 (n/a)</td><td>154.94 (n/a)</td><td>169.60 (n/a)</td><td>117.00 (n/a)</td><td>26.45 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (-2.53%)</td><td>0.05 (+1.47%)</td><td>0.05 (-0.59%)</td><td>0.04 <b>(+52.78%)</b></td><td>0.01 <b>(-47.17%)</b></td><td>189.40 <b>(-34.55%)</b></td><td>164.96 (-7.76%)</td><td>163.50 (+0.62%)</td><td>132.10 (+2.64%)</td><td>22.24 <b>(-65.66%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>289.40 (n/a)</td><td>178.84 (n/a)</td><td>162.50 (n/a)</td><td>128.70 (n/a)</td><td>64.78 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (+13.83%)</td><td>0.05 (+3.75%)</td><td>0.04 (+5.60%)</td><td>0.03 (-1.44%)</td><td>0.01 <b>(+44.90%)</b></td><td>237.60 (+1.45%)</td><td>189.68 (-1.74%)</td><td>183.20 (-5.32%)</td><td>131.70 (-12.14%)</td><td>41.29 <b>(+29.76%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.20 (n/a)</td><td>193.04 (n/a)</td><td>193.50 (n/a)</td><td>149.90 (n/a)</td><td>31.82 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 <b>(+47.82%)</b></td><td>0.05 <b>(+34.62%)</b></td><td>0.06 <b>(+36.66%)</b></td><td>0.04 <b>(+22.53%)</b></td><td>0.01 <b>(+81.35%)</b></td><td>193.80 (-18.37%)</td><td>154.86 <b>(-24.73%)</b></td><td>147.80 <b>(-26.80%)</b></td><td>116.00 <b>(-32.36%)</b></td><td>29.86 (-1.62%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>205.74 (n/a)</td><td>201.90 (n/a)</td><td>171.50 (n/a)</td><td>30.35 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (+9.27%)</td><td>0.05 (+9.33%)</td><td>0.04 (+7.56%)</td><td>0.04 (+13.23%)</td><td>0.01 (+14.63%)</td><td>230.60 (-11.68%)</td><td>181.16 (-8.41%)</td><td>184.50 (-7.01%)</td><td>138.80 (-8.50%)</td><td>36.50 (-9.61%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.10 (n/a)</td><td>197.80 (n/a)</td><td>198.40 (n/a)</td><td>151.70 (n/a)</td><td>40.39 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (+6.94%)</td><td>0.05 (+0.82%)</td><td>0.04 (-0.04%)</td><td>0.03 (-19.85%)</td><td>0.01 <b>(+82.13%)</b></td><td>250.70 <b>(+24.73%)</b></td><td>182.16 (+2.56%)</td><td>185.30 (+0.05%)</td><td>139.20 (-6.45%)</td><td>45.05 <b>(+107.58%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.00 (n/a)</td><td>177.62 (n/a)</td><td>185.20 (n/a)</td><td>148.80 (n/a)</td><td>21.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (+3.40%)</td><td>0.04 (-1.14%)</td><td>0.04 (+6.68%)</td><td>0.03 (-12.58%)</td><td>0.01 <b>(+120.18%)</b></td><td>268.40 (+14.41%)</td><td>216.40 (+3.42%)</td><td>195.40 (-6.24%)</td><td>180.90 (-3.31%)</td><td>40.95 <b>(+142.70%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>234.60 (n/a)</td><td>209.24 (n/a)</td><td>208.40 (n/a)</td><td>187.10 (n/a)</td><td>16.87 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (+12.13%)</td><td>0.05 (+12.34%)</td><td>0.05 (+5.64%)</td><td>0.05 (+15.35%)</td><td>0.01 (-5.01%)</td><td>171.60 (-13.29%)</td><td>156.02 (-11.29%)</td><td>163.30 (-5.33%)</td><td>136.60 (-10.78%)</td><td>14.86 <b>(-28.04%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>175.88 (n/a)</td><td>172.50 (n/a)</td><td>153.10 (n/a)</td><td>20.64 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (-2.95%)</td><td>0.04 (+10.07%)</td><td>0.04 (-1.15%)</td><td>0.04 <b>(+55.12%)</b></td><td>0.01 <b>(-38.83%)</b></td><td>221.50 <b>(-35.54%)</b></td><td>198.22 (-13.50%)</td><td>214.60 (+1.18%)</td><td>158.20 (+3.06%)</td><td>27.76 <b>(-60.26%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>343.60 (n/a)</td><td>229.16 (n/a)</td><td>212.10 (n/a)</td><td>153.50 (n/a)</td><td>69.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 <b>(-32.63%)</b></td><td>0.05 (-5.61%)</td><td>0.05 (+7.23%)</td><td>0.05 (+11.05%)</td><td>0.00 <b>(-86.34%)</b></td><td>171.80 (-9.96%)</td><td>163.60 (+1.41%)</td><td>162.50 (-6.72%)</td><td>155.40 <b>(+48.42%)</b></td><td>6.38 <b>(-80.78%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>161.32 (n/a)</td><td>174.20 (n/a)</td><td>104.70 (n/a)</td><td>33.21 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (-16.09%)</td><td>0.05 (-1.96%)</td><td>0.05 (+8.24%)</td><td>0.04 (-9.26%)</td><td>0.01 <b>(-27.68%)</b></td><td>200.40 (+10.23%)</td><td>162.94 (+0.52%)</td><td>162.50 (-7.62%)</td><td>120.50 (+19.19%)</td><td>33.67 (-1.54%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>181.80 (n/a)</td><td>162.10 (n/a)</td><td>175.90 (n/a)</td><td>101.10 (n/a)</td><td>34.20 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (+16.22%)</td><td>0.05 (+6.26%)</td><td>0.05 (-8.63%)</td><td>0.04 (+12.23%)</td><td>0.01 <b>(+25.02%)</b></td><td>185.40 (-10.91%)</td><td>162.42 (-5.58%)</td><td>171.30 (+9.46%)</td><td>130.40 (-13.93%)</td><td>24.14 (-2.95%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>172.02 (n/a)</td><td>156.50 (n/a)</td><td>151.50 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (-18.91%)</td><td>0.05 (+2.20%)</td><td>0.05 (+7.13%)</td><td>0.04 (+18.29%)</td><td>0.01 <b>(-56.50%)</b></td><td>193.10 (-15.49%)</td><td>164.96 (-6.30%)</td><td>155.20 (-6.62%)</td><td>148.30 <b>(+23.28%)</b></td><td>19.63 <b>(-55.96%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.50 (n/a)</td><td>176.06 (n/a)</td><td>166.20 (n/a)</td><td>120.30 (n/a)</td><td>44.57 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (-0.49%)</td><td>0.05 (+4.79%)</td><td>0.05 (-1.68%)</td><td>0.04 <b>(+29.52%)</b></td><td>0.00 <b>(-43.58%)</b></td><td>206.70 <b>(-22.79%)</b></td><td>183.52 (-6.92%)</td><td>179.10 (+1.70%)</td><td>162.40 (+0.50%)</td><td>18.81 <b>(-56.45%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>267.70 (n/a)</td><td>197.16 (n/a)</td><td>176.10 (n/a)</td><td>161.60 (n/a)</td><td>43.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (-14.20%)</td><td>0.04 (-8.12%)</td><td>0.05 (+7.33%)</td><td>0.03 (-12.67%)</td><td>0.01 (+3.06%)</td><td>249.40 (+14.51%)</td><td>191.32 (+9.76%)</td><td>165.50 (-6.81%)</td><td>162.40 (+16.50%)</td><td>39.17 <b>(+33.98%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.80 (n/a)</td><td>174.30 (n/a)</td><td>177.60 (n/a)</td><td>139.40 (n/a)</td><td>29.24 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.18 (-0.88%)</td><td>0.18 (-0.13%)</td><td>0.18 (+0.04%)</td><td>0.18 (+0.29%)</td><td>0.00 <b>(-83.57%)</b></td><td>47469.90 (-0.29%)</td><td>47422.38 (+0.13%)</td><td>47420.30 (-0.04%)</td><td>47369.50 (+0.89%)</td><td>40.93 <b>(-83.45%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47609.20 (n/a)</td><td>47363.16 (n/a)</td><td>47439.30 (n/a)</td><td>46950.80 (n/a)</td><td>247.34 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.19 (-4.74%)</td><td>0.16 (+4.81%)</td><td>0.16 (+12.17%)</td><td>0.14 (+0.85%)</td><td>0.02 (-18.00%)</td><td>181.30 (-0.82%)</td><td>152.26 (-5.33%)</td><td>157.80 (-10.85%)</td><td>128.30 (+4.91%)</td><td>21.86 (-17.15%)</td>
</tr>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.31 (-2.90%)</td><td>0.27 (-4.20%)</td><td>0.25 (-11.59%)</td><td>0.24 (-1.51%)</td><td>0.03 (+7.42%)</td><td>170.70 (+1.55%)</td><td>152.58 (+4.59%)</td><td>162.70 (+13.14%)</td><td>130.50 (+3.00%)</td><td>18.15 (+11.39%)</td>
</tr>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (-8.05%)</td><td>0.03 (+5.23%)</td><td>0.03 (+6.41%)</td><td>0.03 <b>(+23.22%)</b></td><td>0.00 <b>(-65.35%)</b></td><td>160.50 (-18.82%)</td><td>147.82 (-6.68%)</td><td>147.30 (-6.06%)</td><td>139.60 (+8.81%)</td><td>7.88 <b>(-69.43%)</b></td>
</tr>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (-3.37%)</td><td>0.05 (+6.45%)</td><td>0.05 (+7.17%)</td><td>0.05 <b>(+23.73%)</b></td><td>0.01 <b>(-29.65%)</b></td><td>175.70 (-19.18%)</td><td>155.50 (-7.51%)</td><td>150.70 (-6.69%)</td><td>134.80 (+3.45%)</td><td>18.76 <b>(-40.74%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>168.12 (n/a)</td><td>161.50 (n/a)</td><td>130.30 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.10 <b>(+20.75%)</b></td><td>0.08 (+11.85%)</td><td>0.09 (+16.59%)</td><td>0.07 (+7.25%)</td><td>0.02 <b>(+75.00%)</b></td><td>186.40 (-6.75%)</td><td>152.26 (-8.99%)</td><td>142.60 (-14.25%)</td><td>119.30 (-17.21%)</td><td>29.92 <b>(+38.85%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>167.30 (n/a)</td><td>166.30 (n/a)</td><td>144.10 (n/a)</td><td>21.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 <b>(+47.82%)</b></td><td>0.06 (+13.22%)</td><td>0.05 (+9.89%)</td><td>0.03 <b>(-36.35%)</b></td><td>0.02 <b>(+304.37%)</b></td><td>306.10 <b>(+57.14%)</b></td><td>169.88 (+0.85%)</td><td>150.30 (-9.02%)</td><td>100.50 <b>(-32.32%)</b></td><td>80.53 <b>(+348.37%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>168.44 (n/a)</td><td>165.20 (n/a)</td><td>148.50 (n/a)</td><td>17.96 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (+9.93%)</td><td>0.06 (+7.25%)</td><td>0.06 (+0.19%)</td><td>0.05 <b>(+27.21%)</b></td><td>0.01 (-3.20%)</td><td>210.20 <b>(-21.36%)</b></td><td>174.86 (-7.98%)</td><td>177.20 (-0.17%)</td><td>136.10 (-9.02%)</td><td>30.03 <b>(-33.75%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>267.30 (n/a)</td><td>190.02 (n/a)</td><td>177.50 (n/a)</td><td>149.60 (n/a)</td><td>45.32 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (-5.66%)</td><td>0.05 (+2.62%)</td><td>0.06 <b>(+20.41%)</b></td><td>0.04 (-7.65%)</td><td>0.01 (-6.63%)</td><td>198.10 (+8.31%)</td><td>156.52 (-2.59%)</td><td>147.60 (-16.94%)</td><td>129.10 (+5.99%)</td><td>28.61 (+5.59%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.90 (n/a)</td><td>160.68 (n/a)</td><td>177.70 (n/a)</td><td>121.80 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 <b>(+30.08%)</b></td><td>0.06 (+1.64%)</td><td>0.05 (-9.49%)</td><td>0.05 (-4.29%)</td><td>0.02 <b>(+107.65%)</b></td><td>214.40 (+4.48%)</td><td>182.58 (+1.38%)</td><td>191.40 (+10.44%)</td><td>121.30 <b>(-23.13%)</b></td><td>37.75 <b>(+62.50%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>180.10 (n/a)</td><td>173.30 (n/a)</td><td>157.80 (n/a)</td><td>23.23 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (+3.02%)</td><td>0.05 (+1.18%)</td><td>0.04 (-8.77%)</td><td>0.04 <b>(+26.73%)</b></td><td>0.01 (+1.45%)</td><td>214.50 <b>(-21.11%)</b></td><td>173.52 (-2.56%)</td><td>187.70 (+9.64%)</td><td>123.70 (-2.98%)</td><td>42.42 <b>(-24.61%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>271.90 (n/a)</td><td>178.08 (n/a)</td><td>171.20 (n/a)</td><td>127.50 (n/a)</td><td>56.26 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (+5.25%)</td><td>0.05 (-2.14%)</td><td>0.05 (-14.40%)</td><td>0.04 (+11.73%)</td><td>0.01 (+3.61%)</td><td>207.60 (-10.48%)</td><td>173.78 (+1.67%)</td><td>185.60 (+16.80%)</td><td>120.10 (-4.98%)</td><td>32.86 (-16.89%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>170.92 (n/a)</td><td>158.90 (n/a)</td><td>126.40 (n/a)</td><td>39.54 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (+17.42%)</td><td>0.05 (+4.75%)</td><td>0.05 (+9.38%)</td><td>0.04 (-1.08%)</td><td>0.01 <b>(+66.74%)</b></td><td>191.50 (+1.11%)</td><td>158.48 (-3.27%)</td><td>151.40 (-8.57%)</td><td>123.90 (-14.85%)</td><td>26.16 <b>(+45.90%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>163.84 (n/a)</td><td>165.60 (n/a)</td><td>145.50 (n/a)</td><td>17.93 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 <b>(+24.92%)</b></td><td>0.06 (+14.35%)</td><td>0.06 (+14.65%)</td><td>0.05 (-4.91%)</td><td>0.01 <b>(+98.15%)</b></td><td>204.70 (+5.14%)</td><td>153.84 (-10.09%)</td><td>154.40 (-12.82%)</td><td>113.10 (-19.96%)</td><td>34.79 <b>(+68.06%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>171.10 (n/a)</td><td>177.10 (n/a)</td><td>141.30 (n/a)</td><td>20.70 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (-10.24%)</td><td>0.05 (+7.71%)</td><td>0.05 (+6.94%)</td><td>0.04 <b>(+28.67%)</b></td><td>0.01 <b>(-42.77%)</b></td><td>223.60 <b>(-22.28%)</b></td><td>176.88 (-10.49%)</td><td>165.60 (-6.49%)</td><td>163.50 (+11.45%)</td><td>26.16 <b>(-51.85%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>287.70 (n/a)</td><td>197.62 (n/a)</td><td>177.10 (n/a)</td><td>146.70 (n/a)</td><td>54.33 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (-1.08%)</td><td>0.04 (+2.09%)</td><td>0.05 (+4.48%)</td><td>0.02 (-4.40%)</td><td>0.01 (+4.56%)</td><td>367.10 (+4.59%)</td><td>219.18 (-0.85%)</td><td>191.00 (-4.26%)</td><td>158.50 (+1.08%)</td><td>85.80 (+10.57%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>351.00 (n/a)</td><td>221.06 (n/a)</td><td>199.50 (n/a)</td><td>156.80 (n/a)</td><td>77.60 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (-4.40%)</td><td>0.05 (-2.15%)</td><td>0.05 (-5.67%)</td><td>0.05 (+10.74%)</td><td>0.01 <b>(-34.45%)</b></td><td>164.90 (-9.69%)</td><td>153.38 (+1.19%)</td><td>157.40 (+5.99%)</td><td>130.30 (+4.66%)</td><td>13.33 <b>(-39.69%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>151.58 (n/a)</td><td>148.50 (n/a)</td><td>124.50 (n/a)</td><td>22.10 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (+8.13%)</td><td>0.05 (+1.75%)</td><td>0.05 (+7.95%)</td><td>0.03 <b>(-30.87%)</b></td><td>0.01 <b>(+181.43%)</b></td><td>309.70 <b>(+44.65%)</b></td><td>198.46 (+3.92%)</td><td>170.60 (-7.33%)</td><td>159.40 (-7.54%)</td><td>63.54 <b>(+281.07%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>214.10 (n/a)</td><td>190.98 (n/a)</td><td>184.10 (n/a)</td><td>172.40 (n/a)</td><td>16.68 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (+1.27%)</td><td>0.04 (+7.33%)</td><td>0.05 (+8.68%)</td><td>0.04 (-0.95%)</td><td>0.01 (+11.61%)</td><td>231.60 (+0.96%)</td><td>185.86 (-6.58%)</td><td>174.60 (-8.01%)</td><td>170.80 (-1.21%)</td><td>25.69 (+12.06%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>229.40 (n/a)</td><td>198.96 (n/a)</td><td>189.80 (n/a)</td><td>172.90 (n/a)</td><td>22.92 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.58 <b>(-25.00%)</b></td><td>0.46 <b>(-31.02%)</b></td><td>0.50 <b>(-20.25%)</b></td><td>0.26 <b>(-56.27%)</b></td><td>0.13 <b>(+77.78%)</b></td><td>376.80 <b>(+128.64%)</b></td><td>234.78 <b>(+56.27%)</b></td><td>197.20 <b>(+25.45%)</b></td><td>168.70 <b>(+33.36%)</b></td><td>85.04 <b>(+456.38%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.78 (n/a)</td><td>0.66 (n/a)</td><td>0.63 (n/a)</td><td>0.60 (n/a)</td><td>0.07 (n/a)</td><td>164.80 (n/a)</td><td>150.24 (n/a)</td><td>157.20 (n/a)</td><td>126.50 (n/a)</td><td>15.29 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.77 (-1.49%)</td><td>0.65 (-4.91%)</td><td>0.71 (+6.28%)</td><td>0.52 (-1.93%)</td><td>0.12 (+10.07%)</td><td>190.70 (+1.98%)</td><td>156.76 (+5.93%)</td><td>139.20 (-5.88%)</td><td>127.60 (+1.51%)</td><td>30.24 <b>(+20.09%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.78 (n/a)</td><td>0.68 (n/a)</td><td>0.66 (n/a)</td><td>0.53 (n/a)</td><td>0.11 (n/a)</td><td>187.00 (n/a)</td><td>147.98 (n/a)</td><td>147.90 (n/a)</td><td>125.70 (n/a)</td><td>25.18 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.93 <b>(+44.11%)</b></td><td>0.58 (+13.43%)</td><td>0.48 (-4.87%)</td><td>0.46 (+9.27%)</td><td>0.20 <b>(+144.61%)</b></td><td>212.20 (-8.50%)</td><td>180.48 (-7.09%)</td><td>205.40 (+5.12%)</td><td>105.20 <b>(-30.61%)</b></td><td>45.67 <b>(+58.27%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.65 (n/a)</td><td>0.52 (n/a)</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.08 (n/a)</td><td>231.90 (n/a)</td><td>194.26 (n/a)</td><td>195.40 (n/a)</td><td>151.60 (n/a)</td><td>28.85 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.63 <b>(-20.86%)</b></td><td>0.57 (+2.46%)</td><td>0.59 (+7.75%)</td><td>0.50 <b>(+63.01%)</b></td><td>0.06 <b>(-65.54%)</b></td><td>196.80 <b>(-38.65%)</b></td><td>175.64 (-10.76%)</td><td>167.70 (-7.19%)</td><td>155.80 <b>(+26.36%)</b></td><td>19.73 <b>(-73.73%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.80 (n/a)</td><td>0.55 (n/a)</td><td>0.54 (n/a)</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>320.80 (n/a)</td><td>196.82 (n/a)</td><td>180.70 (n/a)</td><td>123.30 (n/a)</td><td>75.08 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.58 (-3.57%)</td><td>0.54 (-0.06%)</td><td>0.55 (-4.98%)</td><td>0.50 <b>(+35.51%)</b></td><td>0.03 <b>(-68.92%)</b></td><td>146.40 <b>(-26.17%)</b></td><td>136.28 (-2.99%)</td><td>134.30 (+5.25%)</td><td>126.40 (+3.69%)</td><td>7.59 <b>(-76.64%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.60 (n/a)</td><td>0.54 (n/a)</td><td>0.58 (n/a)</td><td>0.37 (n/a)</td><td>0.10 (n/a)</td><td>198.30 (n/a)</td><td>140.48 (n/a)</td><td>127.60 (n/a)</td><td>121.90 (n/a)</td><td>32.50 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.58 (+1.62%)</td><td>0.53 (+9.46%)</td><td>0.57 (+17.36%)</td><td>0.34 (-15.61%)</td><td>0.11 <b>(+64.81%)</b></td><td>220.00 (+18.47%)</td><td>146.48 (-5.67%)</td><td>128.60 (-14.78%)</td><td>126.10 (-1.64%)</td><td>41.15 <b>(+94.13%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.07 (n/a)</td><td>185.70 (n/a)</td><td>155.28 (n/a)</td><td>150.90 (n/a)</td><td>128.20 (n/a)</td><td>21.20 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.63 <b>(+26.45%)</b></td><td>0.49 (+14.70%)</td><td>0.51 (+14.38%)</td><td>0.26 <b>(-23.06%)</b></td><td>0.14 <b>(+99.97%)</b></td><td>284.80 <b>(+29.99%)</b></td><td>166.66 (-6.28%)</td><td>144.60 (-12.52%)</td><td>117.10 <b>(-20.88%)</b></td><td>67.50 <b>(+118.88%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.45 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>219.10 (n/a)</td><td>177.82 (n/a)</td><td>165.30 (n/a)</td><td>148.00 (n/a)</td><td>30.84 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.58 <b>(+39.70%)</b></td><td>0.48 <b>(+24.90%)</b></td><td>0.47 (+18.60%)</td><td>0.39 (+11.93%)</td><td>0.07 <b>(+156.80%)</b></td><td>190.40 (-10.65%)</td><td>156.20 (-18.81%)</td><td>157.50 (-15.69%)</td><td>127.10 <b>(-28.43%)</b></td><td>23.85 <b>(+63.81%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.03 (n/a)</td><td>213.10 (n/a)</td><td>192.38 (n/a)</td><td>186.80 (n/a)</td><td>177.60 (n/a)</td><td>14.56 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.18 (+3.50%)</td><td>0.98 (+16.89%)</td><td>0.97 <b>(+23.42%)</b></td><td>0.86 <b>(+42.43%)</b></td><td>0.12 <b>(-47.71%)</b></td><td>152.60 <b>(-29.81%)</b></td><td>135.86 (-18.76%)</td><td>135.10 (-18.96%)</td><td>111.50 (-3.38%)</td><td>15.99 <b>(-65.19%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.14 (n/a)</td><td>0.84 (n/a)</td><td>0.79 (n/a)</td><td>0.60 (n/a)</td><td>0.24 (n/a)</td><td>217.40 (n/a)</td><td>167.24 (n/a)</td><td>166.70 (n/a)</td><td>115.40 (n/a)</td><td>45.95 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.06 (+4.53%)</td><td>0.80 <b>(+24.92%)</b></td><td>0.79 <b>(+34.79%)</b></td><td>0.48 <b>(+33.12%)</b></td><td>0.22 (-8.31%)</td><td>271.80 <b>(-24.88%)</b></td><td>175.98 <b>(-22.80%)</b></td><td>165.00 <b>(-25.81%)</b></td><td>123.30 (-4.34%)</td><td>57.60 <b>(-31.90%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.02 (n/a)</td><td>0.64 (n/a)</td><td>0.59 (n/a)</td><td>0.36 (n/a)</td><td>0.24 (n/a)</td><td>361.80 (n/a)</td><td>227.96 (n/a)</td><td>222.40 (n/a)</td><td>128.90 (n/a)</td><td>84.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.01 (-7.20%)</td><td>0.77 (-8.97%)</td><td>0.78 (-5.31%)</td><td>0.36 <b>(-41.19%)</b></td><td>0.25 <b>(+24.58%)</b></td><td>361.10 <b>(+70.01%)</b></td><td>194.50 (+19.65%)</td><td>167.10 (+5.56%)</td><td>130.00 (+7.71%)</td><td>95.05 <b>(+141.99%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.09 (n/a)</td><td>0.85 (n/a)</td><td>0.83 (n/a)</td><td>0.62 (n/a)</td><td>0.20 (n/a)</td><td>212.40 (n/a)</td><td>162.56 (n/a)</td><td>158.30 (n/a)</td><td>120.70 (n/a)</td><td>39.28 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (-2.03%)</td><td>0.03 (+11.95%)</td><td>0.02 (+8.82%)</td><td>0.02 (+10.56%)</td><td>0.00 (-11.34%)</td><td>188.20 (-9.56%)</td><td>156.94 (-11.48%)</td><td>165.00 (-8.13%)</td><td>128.50 (+2.07%)</td><td>26.22 (-19.70%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>177.30 (n/a)</td><td>179.60 (n/a)</td><td>125.90 (n/a)</td><td>32.66 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (+12.47%)</td><td>0.03 (+19.08%)</td><td>0.03 (+15.06%)</td><td>0.02 <b>(+38.28%)</b></td><td>0.00 <b>(-20.10%)</b></td><td>168.60 <b>(-27.67%)</b></td><td>149.22 (-17.25%)</td><td>148.10 (-13.09%)</td><td>129.30 (-11.13%)</td><td>16.82 <b>(-49.28%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.10 (n/a)</td><td>180.32 (n/a)</td><td>170.40 (n/a)</td><td>145.50 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (+6.93%)</td><td>0.02 (+10.88%)</td><td>0.02 (+6.80%)</td><td>0.02 <b>(+35.59%)</b></td><td>0.00 <b>(-34.19%)</b></td><td>187.70 <b>(-26.25%)</b></td><td>170.82 (-11.82%)</td><td>177.80 (-6.37%)</td><td>146.10 (-6.47%)</td><td>19.02 <b>(-53.12%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>254.50 (n/a)</td><td>193.72 (n/a)</td><td>189.90 (n/a)</td><td>156.20 (n/a)</td><td>40.58 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.97 (+3.85%)</td><td>0.74 (-7.64%)</td><td>0.74 (-7.00%)</td><td>0.56 (-10.96%)</td><td>0.15 <b>(+29.33%)</b></td><td>235.40 (+12.31%)</td><td>185.06 (+9.78%)</td><td>179.10 (+7.57%)</td><td>136.10 (-3.68%)</td><td>36.27 <b>(+37.59%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.93 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.63 (n/a)</td><td>0.12 (n/a)</td><td>209.60 (n/a)</td><td>168.58 (n/a)</td><td>166.50 (n/a)</td><td>141.30 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.82 <b>(-21.39%)</b></td><td>0.71 (-14.67%)</td><td>0.75 (-4.28%)</td><td>0.61 (-11.64%)</td><td>0.10 <b>(-32.91%)</b></td><td>217.70 (+13.15%)</td><td>188.02 (+16.31%)</td><td>177.00 (+4.42%)</td><td>160.20 <b>(+27.14%)</b></td><td>26.14 (-0.08%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.05 (n/a)</td><td>0.84 (n/a)</td><td>0.78 (n/a)</td><td>0.69 (n/a)</td><td>0.14 (n/a)</td><td>192.40 (n/a)</td><td>161.66 (n/a)</td><td>169.50 (n/a)</td><td>126.00 (n/a)</td><td>26.16 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.97 (-5.02%)</td><td>0.82 (+3.71%)</td><td>0.82 (+7.97%)</td><td>0.73 (+7.71%)</td><td>0.09 <b>(-30.20%)</b></td><td>181.60 (-7.16%)</td><td>161.92 (-4.51%)</td><td>161.00 (-7.36%)</td><td>136.00 (+5.26%)</td><td>17.14 <b>(-29.83%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.02 (n/a)</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.68 (n/a)</td><td>0.13 (n/a)</td><td>195.60 (n/a)</td><td>169.56 (n/a)</td><td>173.80 (n/a)</td><td>129.20 (n/a)</td><td>24.43 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.09 (+5.65%)</td><td>0.95 (+15.50%)</td><td>0.99 <b>(+24.44%)</b></td><td>0.72 (-0.10%)</td><td>0.14 (+15.59%)</td><td>182.50 (+0.11%)</td><td>141.42 (-12.97%)</td><td>134.10 (-19.60%)</td><td>121.10 (-5.39%)</td><td>23.89 (+17.25%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.03 (n/a)</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.72 (n/a)</td><td>0.12 (n/a)</td><td>182.30 (n/a)</td><td>162.50 (n/a)</td><td>166.80 (n/a)</td><td>128.00 (n/a)</td><td>20.38 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.99 (-7.79%)</td><td>0.75 (-5.31%)</td><td>0.75 (+6.19%)</td><td>0.61 (-8.91%)</td><td>0.16 (-7.27%)</td><td>217.30 (+9.75%)</td><td>182.28 (+5.76%)</td><td>176.70 (-5.86%)</td><td>133.30 (+8.46%)</td><td>35.51 (+13.81%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>1.07 (n/a)</td><td>0.79 (n/a)</td><td>0.70 (n/a)</td><td>0.67 (n/a)</td><td>0.17 (n/a)</td><td>198.00 (n/a)</td><td>172.36 (n/a)</td><td>187.70 (n/a)</td><td>122.90 (n/a)</td><td>31.20 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (-8.59%)</td><td>0.03 (+0.98%)</td><td>0.02 (-1.22%)</td><td>0.02 <b>(+20.64%)</b></td><td>0.00 <b>(-49.15%)</b></td><td>172.20 (-17.13%)</td><td>159.02 (-2.95%)</td><td>164.00 (+1.23%)</td><td>139.30 (+9.43%)</td><td>13.83 <b>(-53.98%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.80 (n/a)</td><td>163.86 (n/a)</td><td>162.00 (n/a)</td><td>127.30 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (-5.46%)</td><td>0.02 (+7.11%)</td><td>0.02 (+11.38%)</td><td>0.02 <b>(+27.85%)</b></td><td>0.00 <b>(-69.83%)</b></td><td>183.00 <b>(-21.79%)</b></td><td>169.86 (-10.04%)</td><td>169.10 (-10.24%)</td><td>154.40 (+5.75%)</td><td>10.44 <b>(-74.96%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.00 (n/a)</td><td>188.82 (n/a)</td><td>188.40 (n/a)</td><td>146.00 (n/a)</td><td>41.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.00 (+2.22%)</td><td>0.00 (+0.47%)</td><td>0.00 (+0.00%)</td><td>0.00 (+2.56%)</td><td>0.00 (-5.83%)</td><td>1034.55 (-0.49%)</td><td>961.28 (+0.13%)</td><td>954.57 (+0.57%)</td><td>900.03 (-0.60%)</td><td>48.72 (-3.50%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1039.69 (n/a)</td><td>960.02 (n/a)</td><td>949.20 (n/a)</td><td>905.49 (n/a)</td><td>50.49 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.01 (-3.57%)</td><td>0.01 (-3.48%)</td><td>0.01 (-2.50%)</td><td>0.01 (-5.26%)</td><td>0.00 (+4.74%)</td><td>1131.70 (+4.74%)</td><td>1057.76 (+3.69%)</td><td>1052.13 (+2.33%)</td><td>1008.85 (+3.32%)</td><td>45.34 (+8.32%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1080.50 (n/a)</td><td>1020.15 (n/a)</td><td>1028.21 (n/a)</td><td>976.42 (n/a)</td><td>41.86 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.99 (+3.08%)</td><td>0.95 (-0.53%)</td><td>0.94 (-1.69%)</td><td>0.94 (-1.77%)</td><td>0.02 <b>(+612.06%)</b></td><td>2235.74 (+1.80%)</td><td>2199.88 (+0.58%)</td><td>2223.65 (+1.72%)</td><td>2114.71 (-2.99%)</td><td>49.94 <b>(+600.54%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.00 (n/a)</td><td>2196.29 (n/a)</td><td>2187.22 (n/a)</td><td>2186.03 (n/a)</td><td>2179.83 (n/a)</td><td>7.13 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.39 (-1.31%)</td><td>0.38 (-1.46%)</td><td>0.38 (-1.64%)</td><td>0.37 (-2.23%)</td><td>0.01 <b>(+24.62%)</b></td><td>1406.59 (+2.28%)</td><td>1378.10 (+1.50%)</td><td>1387.76 (+1.67%)</td><td>1338.84 (+1.32%)</td><td>29.01 <b>(+29.38%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1375.26 (n/a)</td><td>1357.79 (n/a)</td><td>1364.91 (n/a)</td><td>1321.38 (n/a)</td><td>22.43 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.26 (+2.97%)</td><td>0.25 (-1.46%)</td><td>0.25 (-0.36%)</td><td>0.22 (-11.90%)</td><td>0.02 <b>(+281.65%)</b></td><td>2424.73 (+13.50%)</td><td>2128.13 (+1.95%)</td><td>2083.03 (+0.35%)</td><td>1988.28 (-2.89%)</td><td>172.47 <b>(+326.16%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.00 (n/a)</td><td>2136.25 (n/a)</td><td>2087.49 (n/a)</td><td>2075.67 (n/a)</td><td>2047.51 (n/a)</td><td>40.47 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.37 (-1.07%)</td><td>0.37 (-1.22%)</td><td>0.37 (-1.24%)</td><td>0.36 (-1.20%)</td><td>0.00 (-1.28%)</td><td>1452.53 (+1.20%)</td><td>1433.38 (+1.23%)</td><td>1433.58 (+1.27%)</td><td>1412.70 (+1.08%)</td><td>14.67 (+0.16%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.00 (n/a)</td><td>1435.28 (n/a)</td><td>1416.03 (n/a)</td><td>1415.66 (n/a)</td><td>1397.62 (n/a)</td><td>14.65 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>3.31 (-0.36%)</td><td>2.77 (-6.94%)</td><td>2.66 (-7.55%)</td><td>2.44 (-6.56%)</td><td>0.34 (+6.31%)</td><td>214.60 (+6.98%)</td><td>191.08 (+7.65%)</td><td>197.00 (+8.18%)</td><td>158.60 (+0.32%)</td><td>21.64 (+15.62%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>3.32 (n/a)</td><td>2.98 (n/a)</td><td>2.88 (n/a)</td><td>2.61 (n/a)</td><td>0.32 (n/a)</td><td>200.60 (n/a)</td><td>177.50 (n/a)</td><td>182.10 (n/a)</td><td>158.10 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>6.18 (+5.69%)</td><td>5.14 (-1.34%)</td><td>4.96 (-3.10%)</td><td>4.17 (-8.27%)</td><td>0.87 <b>(+75.43%)</b></td><td>251.20 (+9.03%)</td><td>208.84 (+2.97%)</td><td>211.40 (+3.22%)</td><td>169.70 (-5.35%)</td><td>35.04 <b>(+79.29%)</b></td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>5.85 (n/a)</td><td>5.21 (n/a)</td><td>5.12 (n/a)</td><td>4.55 (n/a)</td><td>0.50 (n/a)</td><td>230.40 (n/a)</td><td>202.82 (n/a)</td><td>204.80 (n/a)</td><td>179.30 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>3.32 (+4.99%)</td><td>3.04 (+6.23%)</td><td>2.97 (+0.35%)</td><td>2.66 (+2.53%)</td><td>0.27 (+8.02%)</td><td>197.10 (-2.47%)</td><td>173.42 (-5.84%)</td><td>176.30 (-0.34%)</td><td>157.70 (-4.77%)</td><td>15.96 (-2.43%)</td>
</tr>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:09:18</td><td>3.17 (n/a)</td><td>2.86 (n/a)</td><td>2.96 (n/a)</td><td>2.59 (n/a)</td><td>0.25 (n/a)</td><td>202.10 (n/a)</td><td>184.18 (n/a)</td><td>176.90 (n/a)</td><td>165.60 (n/a)</td><td>16.36 (n/a)</td>
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
