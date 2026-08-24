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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.11 <b>(+44.80%)</b></td><td>0.08 (+11.63%)</td><td>0.07 (-5.19%)</td><td>0.06 (+15.22%)</td><td>0.02 <b>(+141.70%)</b></td><td>195.10 (-13.17%)</td><td>168.76 (-7.90%)</td><td>186.90 (+5.47%)</td><td>114.50 <b>(-30.94%)</b></td><td>33.51 <b>(+41.02%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>183.24 (n/a)</td><td>177.20 (n/a)</td><td>165.80 (n/a)</td><td>23.76 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.12 <b>(+72.44%)</b></td><td>0.08 <b>(+26.02%)</b></td><td>0.07 (+11.59%)</td><td>0.06 (+16.83%)</td><td>0.02 <b>(+282.82%)</b></td><td>190.00 (-14.38%)</td><td>159.80 (-16.98%)</td><td>170.20 (-10.42%)</td><td>100.70 <b>(-42.03%)</b></td><td>35.80 <b>(+85.41%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>192.48 (n/a)</td><td>190.00 (n/a)</td><td>173.70 (n/a)</td><td>19.31 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.09 (+1.86%)</td><td>0.07 (-4.27%)</td><td>0.06 (-10.08%)</td><td>0.05 (-0.93%)</td><td>0.01 (+10.61%)</td><td>238.60 (+0.93%)</td><td>192.62 (+4.99%)</td><td>198.50 (+11.20%)</td><td>139.70 (-1.83%)</td><td>37.59 (+6.98%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.40 (n/a)</td><td>183.46 (n/a)</td><td>178.50 (n/a)</td><td>142.30 (n/a)</td><td>35.14 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.10 <b>(+26.76%)</b></td><td>0.07 (+12.66%)</td><td>0.07 (+12.41%)</td><td>0.06 (+1.67%)</td><td>0.01 <b>(+95.76%)</b></td><td>216.40 (-1.64%)</td><td>178.66 (-9.45%)</td><td>177.70 (-11.06%)</td><td>128.10 <b>(-21.12%)</b></td><td>32.57 <b>(+49.78%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>197.30 (n/a)</td><td>199.80 (n/a)</td><td>162.40 (n/a)</td><td>21.75 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.04 (+17.96%)</td><td>0.03 (+4.02%)</td><td>0.03 (+6.31%)</td><td>0.03 (-8.87%)</td><td>0.01 <b>(+140.66%)</b></td><td>207.00 (+9.76%)</td><td>169.70 (-2.20%)</td><td>167.50 (-5.90%)</td><td>135.70 (-15.24%)</td><td>27.47 <b>(+126.96%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>188.60 (n/a)</td><td>173.52 (n/a)</td><td>178.00 (n/a)</td><td>160.10 (n/a)</td><td>12.10 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.04 (-3.57%)</td><td>0.03 (+11.81%)</td><td>0.04 <b>(+29.77%)</b></td><td>0.03 (-4.62%)</td><td>0.01 (-0.59%)</td><td>209.40 (+4.86%)</td><td>157.28 (-10.30%)</td><td>141.40 <b>(-22.90%)</b></td><td>132.30 (+3.76%)</td><td>31.82 (+11.34%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.70 (n/a)</td><td>175.34 (n/a)</td><td>183.40 (n/a)</td><td>127.50 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.03 (+2.27%)</td><td>0.03 (+6.02%)</td><td>0.03 (+8.31%)</td><td>0.03 (+0.62%)</td><td>0.00 (-6.18%)</td><td>190.90 (-0.62%)</td><td>164.06 (-5.78%)</td><td>158.90 (-7.67%)</td><td>154.70 (-2.27%)</td><td>15.14 (-7.35%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.10 (n/a)</td><td>174.12 (n/a)</td><td>172.10 (n/a)</td><td>158.30 (n/a)</td><td>16.34 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.03 (+0.08%)</td><td>0.03 (-4.47%)</td><td>0.03 (-0.08%)</td><td>0.03 (-12.12%)</td><td>0.00 <b>(+82.55%)</b></td><td>205.50 (+13.79%)</td><td>180.96 (+5.44%)</td><td>174.50 (+0.11%)</td><td>160.80 (-0.06%)</td><td>20.27 <b>(+108.55%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>180.60 (n/a)</td><td>171.62 (n/a)</td><td>174.30 (n/a)</td><td>160.90 (n/a)</td><td>9.72 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.04 (-12.05%)</td><td>0.03 (-12.21%)</td><td>0.03 (-12.34%)</td><td>0.03 (-12.14%)</td><td>0.00 (-7.15%)</td><td>193.30 (+13.84%)</td><td>168.98 (+13.99%)</td><td>167.70 (+14.08%)</td><td>149.20 (+13.72%)</td><td>16.61 (+19.58%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>169.80 (n/a)</td><td>148.24 (n/a)</td><td>147.00 (n/a)</td><td>131.20 (n/a)</td><td>13.89 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.03 (+5.80%)</td><td>0.03 (+5.41%)</td><td>0.03 (+9.47%)</td><td>0.02 (+9.07%)</td><td>0.00 (-10.08%)</td><td>235.80 (-8.32%)</td><td>191.04 (-5.89%)</td><td>193.50 (-8.64%)</td><td>152.30 (-5.46%)</td><td>30.76 <b>(-20.54%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>257.20 (n/a)</td><td>203.00 (n/a)</td><td>211.80 (n/a)</td><td>161.10 (n/a)</td><td>38.71 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.03 (-1.77%)</td><td>0.03 (+3.10%)</td><td>0.03 (+2.92%)</td><td>0.03 (+5.67%)</td><td>0.00 <b>(-25.95%)</b></td><td>198.10 (-5.40%)</td><td>182.18 (-3.44%)</td><td>182.60 (-2.82%)</td><td>161.40 (+1.77%)</td><td>14.13 <b>(-28.54%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>209.40 (n/a)</td><td>188.68 (n/a)</td><td>187.90 (n/a)</td><td>158.60 (n/a)</td><td>19.78 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.03 <b>(+24.21%)</b></td><td>0.03 (+10.97%)</td><td>0.02 (+5.00%)</td><td>0.02 (+2.85%)</td><td>0.00 <b>(+222.16%)</b></td><td>226.70 (-2.79%)</td><td>201.02 (-8.69%)</td><td>211.30 (-4.78%)</td><td>165.60 (-19.49%)</td><td>26.88 <b>(+153.20%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.20 (n/a)</td><td>220.14 (n/a)</td><td>221.90 (n/a)</td><td>205.70 (n/a)</td><td>10.61 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>178.30 (n/a)</td><td>143.54 (n/a)</td><td>139.70 (n/a)</td><td>118.10 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>175.10 (n/a)</td><td>150.80 (n/a)</td><td>152.70 (n/a)</td><td>122.10 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>371.30 (n/a)</td><td>206.82 (n/a)</td><td>166.50 (n/a)</td><td>139.70 (n/a)</td><td>94.04 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>295.60 (n/a)</td><td>199.32 (n/a)</td><td>191.80 (n/a)</td><td>149.10 (n/a)</td><td>57.30 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>210.50 (n/a)</td><td>172.06 (n/a)</td><td>174.10 (n/a)</td><td>116.50 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>183.72 (n/a)</td><td>193.60 (n/a)</td><td>149.90 (n/a)</td><td>21.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>176.86 (n/a)</td><td>185.90 (n/a)</td><td>139.60 (n/a)</td><td>21.94 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>214.90 (n/a)</td><td>191.18 (n/a)</td><td>189.20 (n/a)</td><td>176.20 (n/a)</td><td>14.58 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.60 (n/a)</td><td>154.82 (n/a)</td><td>158.30 (n/a)</td><td>126.30 (n/a)</td><td>17.56 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.50 (n/a)</td><td>179.04 (n/a)</td><td>175.90 (n/a)</td><td>170.00 (n/a)</td><td>9.71 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>172.18 (n/a)</td><td>179.90 (n/a)</td><td>123.40 (n/a)</td><td>31.39 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>266.00 (n/a)</td><td>182.86 (n/a)</td><td>159.30 (n/a)</td><td>145.30 (n/a)</td><td>50.66 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.70 (n/a)</td><td>208.80 (n/a)</td><td>192.60 (n/a)</td><td>179.50 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.20 (n/a)</td><td>180.50 (n/a)</td><td>177.60 (n/a)</td><td>165.80 (n/a)</td><td>12.92 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.30 (n/a)</td><td>192.10 (n/a)</td><td>201.90 (n/a)</td><td>150.80 (n/a)</td><td>26.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>324.20 (n/a)</td><td>233.54 (n/a)</td><td>205.60 (n/a)</td><td>200.90 (n/a)</td><td>52.54 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>4.37 (-2.72%)</td><td>3.87 (-1.19%)</td><td>3.76 (-9.18%)</td><td>3.52 (+8.69%)</td><td>0.37 <b>(-28.88%)</b></td><td>2671.20 (-7.99%)</td><td>2449.88 (+0.41%)</td><td>2499.00 (+10.11%)</td><td>2153.90 (+2.80%)</td><td>231.06 <b>(-32.76%)</b></td><td>1717.55 (-2.72%)</td><td>1521.14 (-1.19%)</td><td>1480.33 (-9.18%)</td><td>1384.92 (+8.69%)</td><td>147.43 <b>(-28.88%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>4.49 (n/a)</td><td>3.91 (n/a)</td><td>4.14 (n/a)</td><td>3.24 (n/a)</td><td>0.53 (n/a)</td><td>2903.30 (n/a)</td><td>2439.84 (n/a)</td><td>2269.50 (n/a)</td><td>2095.20 (n/a)</td><td>343.62 (n/a)</td><td>1765.61 (n/a)</td><td>1539.52 (n/a)</td><td>1630.02 (n/a)</td><td>1274.21 (n/a)</td><td>207.28 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>1.04 (-8.78%)</td><td>0.97 (+2.40%)</td><td>0.97 (-0.48%)</td><td>0.88 <b>(+32.72%)</b></td><td>0.07 <b>(-60.05%)</b></td><td>250.30 <b>(-24.65%)</b></td><td>229.54 (-5.02%)</td><td>227.90 (+0.49%)</td><td>212.70 (+9.64%)</td><td>16.46 <b>(-68.73%)</b></td><td>44.37 (-8.78%)</td><td>41.28 (+2.40%)</td><td>41.41 (-0.48%)</td><td>37.71 <b>(+32.72%)</b></td><td>2.93 <b>(-60.05%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>1.14 (n/a)</td><td>0.94 (n/a)</td><td>0.98 (n/a)</td><td>0.67 (n/a)</td><td>0.17 (n/a)</td><td>332.20 (n/a)</td><td>241.66 (n/a)</td><td>226.80 (n/a)</td><td>194.00 (n/a)</td><td>52.65 (n/a)</td><td>48.64 (n/a)</td><td>40.32 (n/a)</td><td>41.61 (n/a)</td><td>28.41 (n/a)</td><td>7.34 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>1.16 (-7.71%)</td><td>0.88 (-12.53%)</td><td>0.93 (-13.35%)</td><td>0.65 (+7.33%)</td><td>0.22 (-14.66%)</td><td>340.70 (-6.84%)</td><td>264.48 (+12.53%)</td><td>239.00 (+15.40%)</td><td>189.90 (+8.39%)</td><td>68.81 (-11.23%)</td><td>49.70 (-7.71%)</td><td>37.66 (-12.53%)</td><td>39.49 (-13.35%)</td><td>27.70 (+7.33%)</td><td>9.56 (-14.66%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>1.26 (n/a)</td><td>1.01 (n/a)</td><td>1.07 (n/a)</td><td>0.60 (n/a)</td><td>0.26 (n/a)</td><td>365.70 (n/a)</td><td>235.04 (n/a)</td><td>207.10 (n/a)</td><td>175.20 (n/a)</td><td>77.52 (n/a)</td><td>53.86 (n/a)</td><td>43.05 (n/a)</td><td>45.57 (n/a)</td><td>25.81 (n/a)</td><td>11.21 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.52 (+0.02%)</td><td>0.52 (-0.07%)</td><td>0.52 (-0.01%)</td><td>0.52 (-0.31%)</td><td>0.00 <b>(+602.63%)</b></td><td>48808.00 (+0.32%)</td><td>48676.00 (+0.07%)</td><td>48648.30 (+0.01%)</td><td>48622.50 (-0.02%)</td><td>74.78 <b>(+606.32%)</b></td><td>353.33 (+0.02%)</td><td>352.94 (-0.07%)</td><td>353.14 (-0.01%)</td><td>351.99 (-0.31%)</td><td>0.54 <b>(+602.74%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48654.40 (n/a)</td><td>48643.34 (n/a)</td><td>48642.70 (n/a)</td><td>48631.20 (n/a)</td><td>10.59 (n/a)</td><td>353.27 (n/a)</td><td>353.18 (n/a)</td><td>353.19 (n/a)</td><td>353.10 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.90 (+0.85%)</td><td>0.89 (+0.20%)</td><td>0.88 (-0.27%)</td><td>0.88 (+0.39%)</td><td>0.01 <b>(+30.29%)</b></td><td>28667.40 (-0.38%)</td><td>28401.98 (-0.19%)</td><td>28455.40 (+0.27%)</td><td>28106.10 (-0.84%)</td><td>233.14 <b>(+28.53%)</b></td><td>611.25 (+0.85%)</td><td>604.92 (+0.20%)</td><td>603.75 (-0.27%)</td><td>599.28 (+0.39%)</td><td>4.97 <b>(+30.29%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28778.00 (n/a)</td><td>28457.10 (n/a)</td><td>28378.30 (n/a)</td><td>28345.10 (n/a)</td><td>181.39 (n/a)</td><td>606.10 (n/a)</td><td>603.73 (n/a)</td><td>605.39 (n/a)</td><td>596.98 (n/a)</td><td>3.82 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>3.33 (+3.27%)</td><td>3.22 (+0.78%)</td><td>3.17 (-1.20%)</td><td>3.11 (-0.78%)</td><td>0.10 <b>(+168.17%)</b></td><td>8086.90 (+0.78%)</td><td>7831.54 (-0.72%)</td><td>7951.10 (+1.21%)</td><td>7565.50 (-3.17%)</td><td>232.94 <b>(+160.66%)</b></td><td>2270.83 (+3.27%)</td><td>2195.25 (+0.78%)</td><td>2160.70 (-1.20%)</td><td>2124.40 (-0.78%)</td><td>65.73 <b>(+168.17%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>3.22 (n/a)</td><td>3.19 (n/a)</td><td>3.20 (n/a)</td><td>3.14 (n/a)</td><td>0.04 (n/a)</td><td>8024.00 (n/a)</td><td>7888.04 (n/a)</td><td>7856.00 (n/a)</td><td>7813.00 (n/a)</td><td>89.36 (n/a)</td><td>2198.88 (n/a)</td><td>2178.18 (n/a)</td><td>2186.85 (n/a)</td><td>2141.05 (n/a)</td><td>24.51 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>4.27 (+15.83%)</td><td>3.71 (+8.35%)</td><td>3.71 (+4.54%)</td><td>2.92 (-4.64%)</td><td>0.52 <b>(+75.29%)</b></td><td>2761.30 (+4.86%)</td><td>2210.72 (-6.67%)</td><td>2171.90 (-4.34%)</td><td>1888.70 (-13.67%)</td><td>341.39 <b>(+60.68%)</b></td><td>1119.25 (+15.83%)</td><td>973.05 (+8.35%)</td><td>973.32 (+4.54%)</td><td>765.57 (-4.64%)</td><td>137.16 <b>(+75.29%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>3.68 (n/a)</td><td>3.42 (n/a)</td><td>3.55 (n/a)</td><td>3.06 (n/a)</td><td>0.30 (n/a)</td><td>2633.20 (n/a)</td><td>2368.76 (n/a)</td><td>2270.50 (n/a)</td><td>2187.70 (n/a)</td><td>212.46 (n/a)</td><td>966.28 (n/a)</td><td>898.03 (n/a)</td><td>931.03 (n/a)</td><td>802.80 (n/a)</td><td>78.25 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.50 (-3.84%)</td><td>0.35 (-15.56%)</td><td>0.32 (-7.94%)</td><td>0.28 <b>(-20.12%)</b></td><td>0.09 (+2.21%)</td><td>4509.80 <b>(+25.19%)</b></td><td>3737.72 (+19.45%)</td><td>3837.90 (+8.62%)</td><td>2465.80 (+3.99%)</td><td>767.80 <b>(+24.10%)</b></td><td>27.22 (-3.84%)</td><td>18.75 (-15.56%)</td><td>17.49 (-7.94%)</td><td>14.88 <b>(-20.12%)</b></td><td>4.87 (+2.21%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>3602.40 (n/a)</td><td>3129.02 (n/a)</td><td>3533.30 (n/a)</td><td>2371.20 (n/a)</td><td>618.71 (n/a)</td><td>28.30 (n/a)</td><td>22.20 (n/a)</td><td>18.99 (n/a)</td><td>18.63 (n/a)</td><td>4.77 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>4.89 <b>(-23.87%)</b></td><td>4.70 (-14.94%)</td><td>4.75 (-4.73%)</td><td>4.49 (-8.82%)</td><td>0.15 <b>(-80.28%)</b></td><td>1482.20 (+9.67%)</td><td>1416.90 (+15.87%)</td><td>1401.20 (+4.97%)</td><td>1360.60 <b>(+31.36%)</b></td><td>46.89 <b>(-71.53%)</b></td><td>1510.52 <b>(-23.87%)</b></td><td>1451.77 (-14.94%)</td><td>1466.77 (-4.73%)</td><td>1386.60 (-8.82%)</td><td>47.69 <b>(-80.28%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>6.42 (n/a)</td><td>5.52 (n/a)</td><td>4.98 (n/a)</td><td>4.92 (n/a)</td><td>0.78 (n/a)</td><td>1351.50 (n/a)</td><td>1222.82 (n/a)</td><td>1334.90 (n/a)</td><td>1035.80 (n/a)</td><td>164.69 (n/a)</td><td>1984.19 (n/a)</td><td>1706.77 (n/a)</td><td>1539.58 (n/a)</td><td>1520.74 (n/a)</td><td>241.79 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>13.22 (n/a)</td><td>12.13 (n/a)</td><td>12.31 (n/a)</td><td>10.66 (n/a)</td><td>1.02 (n/a)</td><td>13.21 (n/a)</td><td>12.12 (n/a)</td><td>12.30 (n/a)</td><td>10.65 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>25.24 (+0.45%)</td><td>24.73 (+2.15%)</td><td>24.69 (+3.16%)</td><td>24.17 (+4.54%)</td><td>0.40 <b>(-54.47%)</b></td><td>25.23 (+0.45%)</td><td>24.71 (+2.15%)</td><td>24.68 (+3.16%)</td><td>24.15 (+4.54%)</td><td>0.40 <b>(-54.47%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>25.13 (n/a)</td><td>24.21 (n/a)</td><td>23.94 (n/a)</td><td>23.12 (n/a)</td><td>0.88 (n/a)</td><td>25.11 (n/a)</td><td>24.19 (n/a)</td><td>23.92 (n/a)</td><td>23.10 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>41.24 (+2.78%)</td><td>39.78 (+4.30%)</td><td>39.96 (+2.51%)</td><td>38.57 (+11.31%)</td><td>1.09 <b>(-51.00%)</b></td><td>41.22 (+2.78%)</td><td>39.76 (+4.30%)</td><td>39.93 (+2.51%)</td><td>38.55 (+11.31%)</td><td>1.08 <b>(-51.00%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>40.13 (n/a)</td><td>38.14 (n/a)</td><td>38.98 (n/a)</td><td>34.65 (n/a)</td><td>2.22 (n/a)</td><td>40.10 (n/a)</td><td>38.12 (n/a)</td><td>38.95 (n/a)</td><td>34.63 (n/a)</td><td>2.21 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>45.74 (+0.40%)</td><td>43.95 (+4.25%)</td><td>43.25 (+2.54%)</td><td>42.74 (+10.70%)</td><td>1.27 <b>(-50.02%)</b></td><td>45.71 (+0.40%)</td><td>43.92 (+4.25%)</td><td>43.22 (+2.54%)</td><td>42.72 (+10.70%)</td><td>1.27 <b>(-50.02%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>45.56 (n/a)</td><td>42.16 (n/a)</td><td>42.18 (n/a)</td><td>38.61 (n/a)</td><td>2.54 (n/a)</td><td>45.53 (n/a)</td><td>42.14 (n/a)</td><td>42.15 (n/a)</td><td>38.59 (n/a)</td><td>2.54 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>13.56 (n/a)</td><td>12.72 (n/a)</td><td>13.25 (n/a)</td><td>10.71 (n/a)</td><td>1.16 (n/a)</td><td>13.55 (n/a)</td><td>12.71 (n/a)</td><td>13.24 (n/a)</td><td>10.71 (n/a)</td><td>1.16 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>25.22 (+2.45%)</td><td>24.82 (+5.14%)</td><td>24.93 (+5.83%)</td><td>24.27 (+8.19%)</td><td>0.40 <b>(-55.11%)</b></td><td>25.20 (+2.45%)</td><td>24.81 (+5.14%)</td><td>24.92 (+5.83%)</td><td>24.26 (+8.19%)</td><td>0.40 <b>(-55.11%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>24.61 (n/a)</td><td>23.61 (n/a)</td><td>23.56 (n/a)</td><td>22.43 (n/a)</td><td>0.89 (n/a)</td><td>24.60 (n/a)</td><td>23.60 (n/a)</td><td>23.55 (n/a)</td><td>22.42 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>40.51 (-2.16%)</td><td>39.29 (+0.52%)</td><td>39.57 (+0.40%)</td><td>36.67 (-0.54%)</td><td>1.56 (-7.72%)</td><td>40.49 (-2.16%)</td><td>39.27 (+0.52%)</td><td>39.55 (+0.40%)</td><td>36.65 (-0.54%)</td><td>1.56 (-7.72%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>41.41 (n/a)</td><td>39.09 (n/a)</td><td>39.41 (n/a)</td><td>36.87 (n/a)</td><td>1.69 (n/a)</td><td>41.38 (n/a)</td><td>39.07 (n/a)</td><td>39.39 (n/a)</td><td>36.85 (n/a)</td><td>1.69 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>44.88 (-0.35%)</td><td>42.71 (-1.74%)</td><td>42.26 (-2.38%)</td><td>39.35 (-6.38%)</td><td>2.30 <b>(+101.46%)</b></td><td>44.85 (-0.35%)</td><td>42.68 (-1.74%)</td><td>42.23 (-2.38%)</td><td>39.33 (-6.38%)</td><td>2.30 <b>(+101.46%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>45.04 (n/a)</td><td>43.46 (n/a)</td><td>43.29 (n/a)</td><td>42.03 (n/a)</td><td>1.14 (n/a)</td><td>45.01 (n/a)</td><td>43.44 (n/a)</td><td>43.26 (n/a)</td><td>42.01 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>9.84 (+7.68%)</td><td>9.10 (+3.07%)</td><td>9.07 (+4.37%)</td><td>8.48 (-1.31%)</td><td>0.52 <b>(+106.34%)</b></td><td>9.82 (+7.68%)</td><td>9.08 (+3.07%)</td><td>9.05 (+4.37%)</td><td>8.46 (-1.31%)</td><td>0.52 <b>(+106.34%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>9.14 (n/a)</td><td>8.83 (n/a)</td><td>8.69 (n/a)</td><td>8.59 (n/a)</td><td>0.25 (n/a)</td><td>9.12 (n/a)</td><td>8.81 (n/a)</td><td>8.67 (n/a)</td><td>8.57 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.88 (+10.52%)</td><td>0.83 (+7.07%)</td><td>0.83 (+6.83%)</td><td>0.78 (+3.81%)</td><td>0.05 <b>(+108.90%)</b></td><td>0.87 (+10.52%)</td><td>0.82 (+7.07%)</td><td>0.81 (+6.83%)</td><td>0.77 (+3.81%)</td><td>0.05 <b>(+108.90%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.02 (n/a)</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>1.31 (+8.74%)</td><td>1.26 (+15.85%)</td><td>1.29 (+19.47%)</td><td>1.15 (+16.38%)</td><td>0.07 <b>(-23.98%)</b></td><td>1.30 (+8.74%)</td><td>1.24 (+15.85%)</td><td>1.27 (+19.47%)</td><td>1.14 (+16.38%)</td><td>0.07 <b>(-23.98%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>1.21 (n/a)</td><td>1.09 (n/a)</td><td>1.08 (n/a)</td><td>0.99 (n/a)</td><td>0.09 (n/a)</td><td>1.19 (n/a)</td><td>1.07 (n/a)</td><td>1.07 (n/a)</td><td>0.98 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>16.46 (+0.79%)</td><td>15.19 (-1.68%)</td><td>15.16 (-2.62%)</td><td>14.54 (+0.48%)</td><td>0.78 (+13.96%)</td><td>16.27 (+0.79%)</td><td>15.02 (-1.68%)</td><td>14.99 (-2.62%)</td><td>14.37 (+0.48%)</td><td>0.77 (+13.96%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>16.33 (n/a)</td><td>15.45 (n/a)</td><td>15.57 (n/a)</td><td>14.47 (n/a)</td><td>0.69 (n/a)</td><td>16.14 (n/a)</td><td>15.28 (n/a)</td><td>15.39 (n/a)</td><td>14.31 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>12.27 (+1.72%)</td><td>11.89 (-0.09%)</td><td>11.69 (-2.89%)</td><td>11.62 (+0.74%)</td><td>0.32 <b>(+38.55%)</b></td><td>12.06 (+1.72%)</td><td>11.68 (-0.09%)</td><td>11.49 (-2.89%)</td><td>11.41 (+0.74%)</td><td>0.31 <b>(+38.55%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>12.06 (n/a)</td><td>11.90 (n/a)</td><td>12.04 (n/a)</td><td>11.53 (n/a)</td><td>0.23 (n/a)</td><td>11.85 (n/a)</td><td>11.69 (n/a)</td><td>11.83 (n/a)</td><td>11.33 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>10.08 (+13.95%)</td><td>8.70 (+6.15%)</td><td>8.58 (+3.96%)</td><td>7.72 (+5.72%)</td><td>0.88 <b>(+42.35%)</b></td><td>9.91 (+13.95%)</td><td>8.55 (+6.15%)</td><td>8.43 (+3.96%)</td><td>7.58 (+5.72%)</td><td>0.86 <b>(+42.35%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>8.85 (n/a)</td><td>8.19 (n/a)</td><td>8.25 (n/a)</td><td>7.30 (n/a)</td><td>0.62 (n/a)</td><td>8.69 (n/a)</td><td>8.05 (n/a)</td><td>8.11 (n/a)</td><td>7.17 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>7.05 (+7.56%)</td><td>6.66 (+8.29%)</td><td>6.61 (+6.71%)</td><td>6.15 (+10.53%)</td><td>0.35 (-17.69%)</td><td>6.93 (+7.56%)</td><td>6.55 (+8.29%)</td><td>6.51 (+6.71%)</td><td>6.05 (+10.53%)</td><td>0.34 (-17.69%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>6.55 (n/a)</td><td>6.15 (n/a)</td><td>6.20 (n/a)</td><td>5.56 (n/a)</td><td>0.42 (n/a)</td><td>6.45 (n/a)</td><td>6.05 (n/a)</td><td>6.10 (n/a)</td><td>5.47 (n/a)</td><td>0.42 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>13.50 (n/a)</td><td>13.11 (n/a)</td><td>13.48 (n/a)</td><td>11.60 (n/a)</td><td>0.84 (n/a)</td><td>13.49 (n/a)</td><td>13.10 (n/a)</td><td>13.47 (n/a)</td><td>11.59 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>13.51 (n/a)</td><td>13.15 (n/a)</td><td>13.39 (n/a)</td><td>12.65 (n/a)</td><td>0.42 (n/a)</td><td>13.50 (n/a)</td><td>13.14 (n/a)</td><td>13.38 (n/a)</td><td>12.64 (n/a)</td><td>0.42 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.30 (n/a)</td><td>155.96 (n/a)</td><td>157.90 (n/a)</td><td>130.00 (n/a)</td><td>15.58 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.60 (n/a)</td><td>151.58 (n/a)</td><td>156.80 (n/a)</td><td>122.40 (n/a)</td><td>21.05 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.50 (n/a)</td><td>172.16 (n/a)</td><td>168.30 (n/a)</td><td>133.20 (n/a)</td><td>38.24 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>163.30 (n/a)</td><td>143.70 (n/a)</td><td>138.30 (n/a)</td><td>41.78 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>176.84 (n/a)</td><td>163.90 (n/a)</td><td>139.90 (n/a)</td><td>30.65 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.20 (n/a)</td><td>173.32 (n/a)</td><td>178.10 (n/a)</td><td>145.10 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.40 (n/a)</td><td>188.84 (n/a)</td><td>186.30 (n/a)</td><td>153.70 (n/a)</td><td>43.65 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>294.40 (n/a)</td><td>211.48 (n/a)</td><td>195.10 (n/a)</td><td>170.60 (n/a)</td><td>50.89 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 <b>(+31.90%)</b></td><td>0.06 <b>(+28.02%)</b></td><td>0.06 <b>(+38.60%)</b></td><td>0.05 (+18.36%)</td><td>0.01 <b>(+57.11%)</b></td><td>170.50 (-15.51%)</td><td>143.98 <b>(-21.31%)</b></td><td>142.60 <b>(-27.87%)</b></td><td>118.00 <b>(-24.21%)</b></td><td>23.01 (+0.90%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>182.96 (n/a)</td><td>197.70 (n/a)</td><td>155.70 (n/a)</td><td>22.80 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (+16.67%)</td><td>0.06 (+13.54%)</td><td>0.06 (+15.23%)</td><td>0.05 (+17.55%)</td><td>0.01 <b>(+27.23%)</b></td><td>176.80 (-14.92%)</td><td>146.04 (-11.56%)</td><td>132.10 (-13.21%)</td><td>123.00 (-14.29%)</td><td>25.85 (-5.39%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>165.12 (n/a)</td><td>152.20 (n/a)</td><td>143.50 (n/a)</td><td>27.32 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 <b>(+35.96%)</b></td><td>0.05 <b>(+36.93%)</b></td><td>0.05 <b>(+43.56%)</b></td><td>0.05 <b>(+34.49%)</b></td><td>0.01 <b>(+25.88%)</b></td><td>169.90 <b>(-25.65%)</b></td><td>151.26 <b>(-27.10%)</b></td><td>151.90 <b>(-30.32%)</b></td><td>126.80 <b>(-26.45%)</b></td><td>16.95 <b>(-32.08%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.50 (n/a)</td><td>207.48 (n/a)</td><td>218.00 (n/a)</td><td>172.40 (n/a)</td><td>24.96 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (+19.31%)</td><td>0.05 <b>(+23.83%)</b></td><td>0.06 <b>(+22.91%)</b></td><td>0.04 <b>(+72.01%)</b></td><td>0.01 <b>(-23.10%)</b></td><td>208.90 <b>(-41.84%)</b></td><td>162.14 <b>(-23.98%)</b></td><td>145.70 (-18.65%)</td><td>138.40 (-16.22%)</td><td>29.90 <b>(-63.75%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>359.20 (n/a)</td><td>213.28 (n/a)</td><td>179.10 (n/a)</td><td>165.20 (n/a)</td><td>82.49 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (+6.37%)</td><td>0.05 (+7.59%)</td><td>0.06 (+8.31%)</td><td>0.04 (+9.58%)</td><td>0.01 (+16.00%)</td><td>184.20 (-8.72%)</td><td>156.60 (-6.86%)</td><td>148.60 (-7.64%)</td><td>136.70 (-5.98%)</td><td>21.52 (-1.72%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>168.14 (n/a)</td><td>160.90 (n/a)</td><td>145.40 (n/a)</td><td>21.89 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (-6.75%)</td><td>0.05 (+1.83%)</td><td>0.05 (-7.31%)</td><td>0.04 (+13.91%)</td><td>0.01 <b>(-37.55%)</b></td><td>201.90 (-12.18%)</td><td>172.00 (-4.64%)</td><td>173.80 (+7.88%)</td><td>141.70 (+7.27%)</td><td>24.33 <b>(-43.82%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>180.36 (n/a)</td><td>161.10 (n/a)</td><td>132.10 (n/a)</td><td>43.30 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 <b>(+41.67%)</b></td><td>0.06 <b>(+33.82%)</b></td><td>0.06 <b>(+36.93%)</b></td><td>0.04 (+11.81%)</td><td>0.01 <b>(+220.68%)</b></td><td>187.60 (-10.54%)</td><td>151.62 <b>(-24.11%)</b></td><td>147.90 <b>(-27.00%)</b></td><td>127.50 <b>(-29.44%)</b></td><td>23.60 <b>(+105.07%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.70 (n/a)</td><td>199.80 (n/a)</td><td>202.60 (n/a)</td><td>180.70 (n/a)</td><td>11.51 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (-18.93%)</td><td>0.05 (+2.23%)</td><td>0.05 (+7.40%)</td><td>0.04 (+2.71%)</td><td>0.01 <b>(-42.61%)</b></td><td>226.50 (-2.62%)</td><td>179.00 (-4.46%)</td><td>177.00 (-6.89%)</td><td>155.20 <b>(+23.37%)</b></td><td>28.41 <b>(-26.70%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.60 (n/a)</td><td>187.36 (n/a)</td><td>190.10 (n/a)</td><td>125.80 (n/a)</td><td>38.77 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 <b>(+41.73%)</b></td><td>0.05 (+19.50%)</td><td>0.05 <b>(+21.40%)</b></td><td>0.03 (-9.86%)</td><td>0.02 <b>(+106.15%)</b></td><td>267.40 (+10.95%)</td><td>179.28 (-11.75%)</td><td>165.30 (-17.60%)</td><td>112.60 <b>(-29.45%)</b></td><td>57.10 <b>(+59.02%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.00 (n/a)</td><td>203.16 (n/a)</td><td>200.60 (n/a)</td><td>159.60 (n/a)</td><td>35.91 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.04 (+12.56%)</td><td>0.04 (+10.40%)</td><td>0.04 (+12.57%)</td><td>0.02 (-2.15%)</td><td>0.01 <b>(+45.46%)</b></td><td>328.10 (+2.21%)</td><td>227.90 (-7.73%)</td><td>211.10 (-11.15%)</td><td>193.30 (-11.17%)</td><td>56.77 <b>(+33.12%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>321.00 (n/a)</td><td>246.98 (n/a)</td><td>237.60 (n/a)</td><td>217.60 (n/a)</td><td>42.64 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (+2.74%)</td><td>0.05 (+1.18%)</td><td>0.05 (-4.58%)</td><td>0.04 (+1.86%)</td><td>0.01 (+4.72%)</td><td>186.40 (-1.84%)</td><td>168.12 (-1.14%)</td><td>169.80 (+4.81%)</td><td>148.20 (-2.63%)</td><td>17.60 (-1.70%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.90 (n/a)</td><td>170.06 (n/a)</td><td>162.00 (n/a)</td><td>152.20 (n/a)</td><td>17.91 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (-2.69%)</td><td>0.04 (+2.87%)</td><td>0.04 (-0.72%)</td><td>0.04 (+17.65%)</td><td>0.01 <b>(-25.14%)</b></td><td>211.60 (-14.99%)</td><td>193.48 (-3.93%)</td><td>207.90 (+0.73%)</td><td>159.90 (+2.76%)</td><td>22.99 <b>(-33.19%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.90 (n/a)</td><td>201.40 (n/a)</td><td>206.40 (n/a)</td><td>155.60 (n/a)</td><td>34.41 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (-7.84%)</td><td>0.05 (+2.58%)</td><td>0.05 (+0.03%)</td><td>0.04 <b>(+22.11%)</b></td><td>0.01 <b>(-48.37%)</b></td><td>187.50 (-18.09%)</td><td>160.86 (-5.52%)</td><td>162.60 (-0.06%)</td><td>137.80 (+8.50%)</td><td>18.13 <b>(-54.26%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.90 (n/a)</td><td>170.26 (n/a)</td><td>162.70 (n/a)</td><td>127.00 (n/a)</td><td>39.64 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (+13.11%)</td><td>0.05 (+4.49%)</td><td>0.05 (+0.08%)</td><td>0.04 (+5.42%)</td><td>0.01 (+18.40%)</td><td>188.50 (-5.18%)</td><td>159.66 (-3.89%)</td><td>173.80 (-0.11%)</td><td>117.50 (-11.59%)</td><td>28.53 (-0.19%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>166.12 (n/a)</td><td>174.00 (n/a)</td><td>132.90 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (-17.10%)</td><td>0.05 (-9.48%)</td><td>0.05 (-6.66%)</td><td>0.04 (-3.49%)</td><td>0.00 <b>(-54.58%)</b></td><td>190.60 (+3.64%)</td><td>177.14 (+9.47%)</td><td>176.90 (+7.15%)</td><td>161.40 <b>(+20.63%)</b></td><td>11.25 <b>(-42.82%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>161.82 (n/a)</td><td>165.10 (n/a)</td><td>133.80 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (-6.65%)</td><td>0.05 (+17.26%)</td><td>0.05 <b>(+21.42%)</b></td><td>0.04 <b>(+42.88%)</b></td><td>0.01 <b>(-47.86%)</b></td><td>214.60 <b>(-30.01%)</b></td><td>172.78 <b>(-20.51%)</b></td><td>164.10 (-17.66%)</td><td>148.70 (+7.13%)</td><td>27.29 <b>(-62.00%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>306.60 (n/a)</td><td>217.36 (n/a)</td><td>199.30 (n/a)</td><td>138.80 (n/a)</td><td>71.83 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (-4.73%)</td><td>0.05 (+6.05%)</td><td>0.04 (+6.37%)</td><td>0.03 (+3.30%)</td><td>0.01 (-12.71%)</td><td>237.10 (-3.18%)</td><td>184.74 (-6.38%)</td><td>184.90 (-6.00%)</td><td>156.00 (+4.91%)</td><td>33.06 (-12.40%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.90 (n/a)</td><td>197.34 (n/a)</td><td>196.70 (n/a)</td><td>148.70 (n/a)</td><td>37.74 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 <b>(+21.77%)</b></td><td>0.05 <b>(+31.22%)</b></td><td>0.05 (+16.52%)</td><td>0.04 <b>(+62.20%)</b></td><td>0.01 <b>(-39.00%)</b></td><td>203.80 <b>(-38.35%)</b></td><td>166.50 <b>(-27.28%)</b></td><td>162.20 (-14.23%)</td><td>148.00 (-17.91%)</td><td>21.70 <b>(-67.32%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>330.60 (n/a)</td><td>228.96 (n/a)</td><td>189.10 (n/a)</td><td>180.30 (n/a)</td><td>66.40 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.18 (-13.56%)</td><td>0.18 (-13.72%)</td><td>0.18 (-13.73%)</td><td>0.18 (-13.88%)</td><td>0.00 <b>(+27.45%)</b></td><td>47502.00 (+16.12%)</td><td>47333.36 (+15.90%)</td><td>47376.40 (+15.91%)</td><td>47039.70 (+15.69%)</td><td>174.68 <b>(+71.09%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40908.50 (n/a)</td><td>40840.72 (n/a)</td><td>40872.90 (n/a)</td><td>40660.30 (n/a)</td><td>102.10 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (-18.87%)</td><td>0.05 (-1.84%)</td><td>0.05 (+2.12%)</td><td>0.04 (+3.87%)</td><td>0.01 <b>(-49.52%)</b></td><td>194.70 (-3.71%)</td><td>173.24 (-0.24%)</td><td>180.70 (-2.11%)</td><td>153.20 <b>(+23.25%)</b></td><td>18.40 <b>(-40.04%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>173.66 (n/a)</td><td>184.60 (n/a)</td><td>124.30 (n/a)</td><td>30.69 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.09 <b>(+36.79%)</b></td><td>0.08 (+16.19%)</td><td>0.08 (+13.76%)</td><td>0.06 (-1.28%)</td><td>0.01 <b>(+188.71%)</b></td><td>220.60 (+1.29%)</td><td>168.10 (-11.92%)</td><td>162.70 (-12.10%)</td><td>132.80 <b>(-26.91%)</b></td><td>32.73 <b>(+116.20%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>217.80 (n/a)</td><td>190.84 (n/a)</td><td>185.10 (n/a)</td><td>181.70 (n/a)</td><td>15.14 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 <b>(+24.14%)</b></td><td>0.05 <b>(+32.13%)</b></td><td>0.05 <b>(+39.56%)</b></td><td>0.04 <b>(+72.90%)</b></td><td>0.01 (-11.47%)</td><td>212.90 <b>(-42.15%)</b></td><td>159.50 <b>(-28.61%)</b></td><td>151.50 <b>(-28.33%)</b></td><td>119.90 (-19.48%)</td><td>34.15 <b>(-59.95%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>368.00 (n/a)</td><td>223.42 (n/a)</td><td>211.40 (n/a)</td><td>148.90 (n/a)</td><td>85.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.08 (+18.89%)</td><td>0.06 (+12.08%)</td><td>0.06 (+6.63%)</td><td>0.04 (+3.02%)</td><td>0.02 <b>(+37.54%)</b></td><td>231.50 (-2.94%)</td><td>171.18 (-9.36%)</td><td>168.60 (-6.23%)</td><td>122.40 (-15.88%)</td><td>41.90 (+11.05%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>238.50 (n/a)</td><td>188.86 (n/a)</td><td>179.80 (n/a)</td><td>145.50 (n/a)</td><td>37.73 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (+13.38%)</td><td>0.05 (+5.23%)</td><td>0.05 (+12.42%)</td><td>0.03 <b>(-30.29%)</b></td><td>0.01 <b>(+166.06%)</b></td><td>294.80 <b>(+43.45%)</b></td><td>182.48 (+1.10%)</td><td>160.20 (-11.05%)</td><td>142.60 (-11.76%)</td><td>63.28 <b>(+256.44%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.50 (n/a)</td><td>180.50 (n/a)</td><td>180.10 (n/a)</td><td>161.60 (n/a)</td><td>17.75 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.10 <b>(+55.88%)</b></td><td>0.07 <b>(+27.31%)</b></td><td>0.06 (+12.11%)</td><td>0.04 (-0.79%)</td><td>0.02 <b>(+186.28%)</b></td><td>232.70 (+0.82%)</td><td>160.80 (-15.84%)</td><td>169.80 (-10.82%)</td><td>102.60 <b>(-35.88%)</b></td><td>51.99 <b>(+81.56%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>191.06 (n/a)</td><td>190.40 (n/a)</td><td>160.00 (n/a)</td><td>28.63 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 <b>(+27.93%)</b></td><td>0.05 (+12.80%)</td><td>0.05 (+13.38%)</td><td>0.04 (-1.35%)</td><td>0.01 <b>(+183.36%)</b></td><td>196.30 (+1.34%)</td><td>164.24 (-9.78%)</td><td>164.80 (-11.82%)</td><td>129.80 <b>(-21.85%)</b></td><td>26.13 <b>(+124.18%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>193.70 (n/a)</td><td>182.04 (n/a)</td><td>186.90 (n/a)</td><td>166.10 (n/a)</td><td>11.66 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (+3.01%)</td><td>0.05 (-1.21%)</td><td>0.05 (-3.10%)</td><td>0.04 (-5.87%)</td><td>0.01 <b>(+33.54%)</b></td><td>207.10 (+6.26%)</td><td>184.42 (+1.61%)</td><td>186.00 (+3.22%)</td><td>157.10 (-2.90%)</td><td>18.67 <b>(+35.11%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>194.90 (n/a)</td><td>181.50 (n/a)</td><td>180.20 (n/a)</td><td>161.80 (n/a)</td><td>13.82 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 <b>(+22.90%)</b></td><td>0.05 (+18.13%)</td><td>0.05 <b>(+27.61%)</b></td><td>0.04 (+11.77%)</td><td>0.01 <b>(+37.11%)</b></td><td>211.70 (-10.56%)</td><td>174.12 (-14.50%)</td><td>168.10 <b>(-21.63%)</b></td><td>129.20 (-18.64%)</td><td>36.27 (+2.23%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.70 (n/a)</td><td>203.64 (n/a)</td><td>214.50 (n/a)</td><td>158.80 (n/a)</td><td>35.48 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (+12.69%)</td><td>0.06 <b>(+20.91%)</b></td><td>0.06 <b>(+29.07%)</b></td><td>0.05 <b>(+26.76%)</b></td><td>0.01 <b>(-20.55%)</b></td><td>174.80 <b>(-21.12%)</b></td><td>156.94 (-18.26%)</td><td>156.30 <b>(-22.55%)</b></td><td>132.70 (-11.30%)</td><td>16.47 <b>(-44.36%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>192.00 (n/a)</td><td>201.80 (n/a)</td><td>149.60 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 <b>(+34.54%)</b></td><td>0.05 <b>(+24.19%)</b></td><td>0.05 <b>(+20.50%)</b></td><td>0.04 <b>(+37.64%)</b></td><td>0.01 <b>(+37.64%)</b></td><td>229.80 <b>(-27.35%)</b></td><td>173.42 (-19.50%)</td><td>159.00 (-17.01%)</td><td>122.20 <b>(-25.67%)</b></td><td>43.04 <b>(-27.60%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.30 (n/a)</td><td>215.44 (n/a)</td><td>191.60 (n/a)</td><td>164.40 (n/a)</td><td>59.45 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (-0.10%)</td><td>0.05 (+10.08%)</td><td>0.05 (+3.20%)</td><td>0.04 <b>(+29.59%)</b></td><td>0.00 <b>(-43.43%)</b></td><td>222.20 <b>(-22.85%)</b></td><td>191.20 (-11.12%)</td><td>190.50 (-3.10%)</td><td>176.30 (+0.11%)</td><td>18.71 <b>(-57.42%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>288.00 (n/a)</td><td>215.12 (n/a)</td><td>196.60 (n/a)</td><td>176.10 (n/a)</td><td>43.94 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 <b>(+25.42%)</b></td><td>0.04 (+14.72%)</td><td>0.05 (+17.26%)</td><td>0.03 (-4.36%)</td><td>0.01 <b>(+66.36%)</b></td><td>266.10 (+4.56%)</td><td>191.82 (-10.77%)</td><td>173.40 (-14.75%)</td><td>148.10 <b>(-20.25%)</b></td><td>46.39 <b>(+42.24%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.50 (n/a)</td><td>214.98 (n/a)</td><td>203.40 (n/a)</td><td>185.70 (n/a)</td><td>32.61 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (+13.02%)</td><td>0.05 (+11.64%)</td><td>0.05 (+16.19%)</td><td>0.04 (+1.80%)</td><td>0.00 <b>(+130.69%)</b></td><td>205.60 (-1.77%)</td><td>178.94 (-10.04%)</td><td>173.10 (-13.97%)</td><td>167.80 (-11.54%)</td><td>15.71 <b>(+102.01%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.30 (n/a)</td><td>198.90 (n/a)</td><td>201.20 (n/a)</td><td>189.70 (n/a)</td><td>7.78 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.04 (+2.63%)</td><td>0.04 (-0.63%)</td><td>0.04 (+0.73%)</td><td>0.03 (+1.03%)</td><td>0.00 <b>(+28.18%)</b></td><td>255.50 (-1.01%)</td><td>224.74 (+1.17%)</td><td>218.40 (-0.73%)</td><td>190.70 (-2.60%)</td><td>29.57 <b>(+25.97%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>258.10 (n/a)</td><td>222.14 (n/a)</td><td>220.00 (n/a)</td><td>195.80 (n/a)</td><td>23.47 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.64 (-15.43%)</td><td>0.53 (-12.35%)</td><td>0.53 (-9.61%)</td><td>0.41 (+4.33%)</td><td>0.10 <b>(-32.03%)</b></td><td>239.50 (-4.16%)</td><td>191.34 (+11.24%)</td><td>185.90 (+10.65%)</td><td>152.70 (+18.28%)</td><td>36.84 <b>(-23.37%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.76 (n/a)</td><td>0.60 (n/a)</td><td>0.59 (n/a)</td><td>0.39 (n/a)</td><td>0.15 (n/a)</td><td>249.90 (n/a)</td><td>172.00 (n/a)</td><td>168.00 (n/a)</td><td>129.10 (n/a)</td><td>48.08 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.74 (+2.27%)</td><td>0.62 (+8.59%)</td><td>0.60 (+4.72%)</td><td>0.46 (+17.51%)</td><td>0.11 (-11.94%)</td><td>213.00 (-14.87%)</td><td>163.30 (-9.34%)</td><td>163.20 (-4.51%)</td><td>132.50 (-2.21%)</td><td>31.92 <b>(-28.11%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.73 (n/a)</td><td>0.57 (n/a)</td><td>0.58 (n/a)</td><td>0.39 (n/a)</td><td>0.13 (n/a)</td><td>250.20 (n/a)</td><td>180.12 (n/a)</td><td>170.90 (n/a)</td><td>135.50 (n/a)</td><td>44.41 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.61 <b>(-21.87%)</b></td><td>0.49 (-8.40%)</td><td>0.50 (-2.40%)</td><td>0.35 (-13.81%)</td><td>0.12 <b>(-20.16%)</b></td><td>277.10 (+15.99%)</td><td>208.82 (+8.94%)</td><td>196.30 (+2.45%)</td><td>160.80 <b>(+28.03%)</b></td><td>51.62 (+18.89%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.78 (n/a)</td><td>0.54 (n/a)</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.15 (n/a)</td><td>238.90 (n/a)</td><td>191.68 (n/a)</td><td>191.60 (n/a)</td><td>125.60 (n/a)</td><td>43.42 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.66 (-14.14%)</td><td>0.53 (-11.23%)</td><td>0.59 (-2.64%)</td><td>0.33 <b>(-30.40%)</b></td><td>0.13 (+18.53%)</td><td>300.70 <b>(+43.67%)</b></td><td>198.08 (+16.85%)</td><td>166.60 (+2.71%)</td><td>149.60 (+16.51%)</td><td>61.80 <b>(+102.33%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.77 (n/a)</td><td>0.60 (n/a)</td><td>0.61 (n/a)</td><td>0.47 (n/a)</td><td>0.11 (n/a)</td><td>209.30 (n/a)</td><td>169.52 (n/a)</td><td>162.20 (n/a)</td><td>128.40 (n/a)</td><td>30.54 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.55 (-7.03%)</td><td>0.44 (-13.14%)</td><td>0.41 <b>(-21.64%)</b></td><td>0.34 (-15.62%)</td><td>0.09 (+19.32%)</td><td>217.30 (+18.55%)</td><td>171.50 (+16.70%)</td><td>178.30 <b>(+27.63%)</b></td><td>133.60 (+7.57%)</td><td>34.01 <b>(+47.16%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.59 (n/a)</td><td>0.51 (n/a)</td><td>0.53 (n/a)</td><td>0.40 (n/a)</td><td>0.07 (n/a)</td><td>183.30 (n/a)</td><td>146.96 (n/a)</td><td>139.70 (n/a)</td><td>124.20 (n/a)</td><td>23.11 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.56 (-11.86%)</td><td>0.49 (-0.39%)</td><td>0.49 (+13.28%)</td><td>0.43 (+2.38%)</td><td>0.05 <b>(-50.37%)</b></td><td>171.00 (-2.34%)</td><td>150.42 (-1.70%)</td><td>150.90 (-11.70%)</td><td>131.70 (+13.44%)</td><td>14.80 <b>(-46.09%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.63 (n/a)</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.10 (n/a)</td><td>175.10 (n/a)</td><td>153.02 (n/a)</td><td>170.90 (n/a)</td><td>116.10 (n/a)</td><td>27.46 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.58 <b>(+21.76%)</b></td><td>0.43 (+4.81%)</td><td>0.37 (-9.66%)</td><td>0.31 (-12.09%)</td><td>0.12 <b>(+118.71%)</b></td><td>241.30 (+13.77%)</td><td>182.38 (-0.16%)</td><td>201.80 (+10.70%)</td><td>126.30 (-17.88%)</td><td>47.98 <b>(+98.34%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.05 (n/a)</td><td>212.10 (n/a)</td><td>182.68 (n/a)</td><td>182.30 (n/a)</td><td>153.80 (n/a)</td><td>24.19 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.51 (-7.57%)</td><td>0.41 (-5.10%)</td><td>0.42 (+2.86%)</td><td>0.27 <b>(-21.35%)</b></td><td>0.09 (-4.55%)</td><td>275.00 <b>(+27.14%)</b></td><td>187.26 (+6.52%)</td><td>176.00 (-2.76%)</td><td>144.30 (+8.17%)</td><td>52.02 <b>(+35.45%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>216.30 (n/a)</td><td>175.80 (n/a)</td><td>181.00 (n/a)</td><td>133.40 (n/a)</td><td>38.40 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>1.02 (-1.96%)</td><td>0.88 (+12.03%)</td><td>0.89 (+14.46%)</td><td>0.76 (+17.65%)</td><td>0.10 <b>(-32.63%)</b></td><td>172.10 (-15.01%)</td><td>149.82 (-12.17%)</td><td>147.20 (-12.64%)</td><td>128.50 (+1.98%)</td><td>17.61 <b>(-40.74%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>1.04 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.65 (n/a)</td><td>0.15 (n/a)</td><td>202.50 (n/a)</td><td>170.58 (n/a)</td><td>168.50 (n/a)</td><td>126.00 (n/a)</td><td>29.71 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>1.03 (+5.01%)</td><td>0.94 (+19.59%)</td><td>0.93 <b>(+21.80%)</b></td><td>0.86 <b>(+32.59%)</b></td><td>0.06 <b>(-47.18%)</b></td><td>153.20 <b>(-24.57%)</b></td><td>140.04 (-17.57%)</td><td>140.90 (-17.89%)</td><td>127.10 (-4.79%)</td><td>9.55 <b>(-61.28%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.98 (n/a)</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.65 (n/a)</td><td>0.12 (n/a)</td><td>203.10 (n/a)</td><td>169.88 (n/a)</td><td>171.60 (n/a)</td><td>133.50 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.94 <b>(+22.56%)</b></td><td>0.86 <b>(+39.89%)</b></td><td>0.91 <b>(+38.86%)</b></td><td>0.72 <b>(+92.03%)</b></td><td>0.09 <b>(-37.36%)</b></td><td>183.00 <b>(-47.91%)</b></td><td>154.26 <b>(-32.09%)</b></td><td>144.20 <b>(-27.97%)</b></td><td>139.80 (-18.39%)</td><td>18.07 <b>(-74.77%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.77 (n/a)</td><td>0.61 (n/a)</td><td>0.65 (n/a)</td><td>0.37 (n/a)</td><td>0.15 (n/a)</td><td>351.30 (n/a)</td><td>227.14 (n/a)</td><td>200.20 (n/a)</td><td>171.30 (n/a)</td><td>71.60 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.00 (-2.27%)</td><td>0.00 (-1.84%)</td><td>0.00 (-2.27%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-38.76%)</b></td><td>978.24 (+1.14%)</td><td>958.55 (+1.63%)</td><td>952.80 (+1.28%)</td><td>945.83 (+2.34%)</td><td>14.76 (-9.20%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>967.19 (n/a)</td><td>943.19 (n/a)</td><td>940.74 (n/a)</td><td>924.24 (n/a)</td><td>16.26 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.01 (+1.23%)</td><td>0.01 (-0.50%)</td><td>0.01 (-1.23%)</td><td>0.01 (-2.50%)</td><td>0.00 <b>(+226.60%)</b></td><td>1045.21 (+1.91%)</td><td>1018.48 (+0.19%)</td><td>1019.57 (+0.61%)</td><td>994.24 (-1.29%)</td><td>21.18 <b>(+166.81%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1025.59 (n/a)</td><td>1016.55 (n/a)</td><td>1013.35 (n/a)</td><td>1007.22 (n/a)</td><td>7.94 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.97 (-0.33%)</td><td>0.96 (-0.73%)</td><td>0.96 (-1.12%)</td><td>0.95 (-0.76%)</td><td>0.01 <b>(+26.85%)</b></td><td>2209.86 (+0.77%)</td><td>2192.65 (+0.74%)</td><td>2195.13 (+1.13%)</td><td>2168.81 (+0.33%)</td><td>16.70 <b>(+27.95%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.01 (n/a)</td><td>2192.96 (n/a)</td><td>2176.57 (n/a)</td><td>2170.60 (n/a)</td><td>2161.57 (n/a)</td><td>13.05 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.40 (-9.88%)</td><td>0.39 (-10.38%)</td><td>0.39 (-10.20%)</td><td>0.38 (-11.26%)</td><td>0.01 <b>(+39.04%)</b></td><td>1374.32 (+12.69%)</td><td>1345.59 (+11.60%)</td><td>1344.77 (+11.38%)</td><td>1315.76 (+10.98%)</td><td>23.37 <b>(+74.02%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.00 (n/a)</td><td>1219.59 (n/a)</td><td>1205.76 (n/a)</td><td>1207.37 (n/a)</td><td>1185.61 (n/a)</td><td>13.43 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.27 <b>(-30.16%)</b></td><td>0.26 <b>(-31.18%)</b></td><td>0.25 <b>(-31.85%)</b></td><td>0.25 <b>(-31.04%)</b></td><td>0.01 (-11.18%)</td><td>2105.81 <b>(+45.02%)</b></td><td>2054.01 <b>(+45.33%)</b></td><td>2071.67 <b>(+46.76%)</b></td><td>1972.63 <b>(+43.21%)</b></td><td>50.27 <b>(+82.94%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1452.04 (n/a)</td><td>1413.30 (n/a)</td><td>1411.56 (n/a)</td><td>1377.40 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.37 (-0.67%)</td><td>0.37 (+0.95%)</td><td>0.37 (+1.70%)</td><td>0.37 (+2.87%)</td><td>0.00 <b>(-55.53%)</b></td><td>1434.79 (-2.78%)</td><td>1418.00 (-0.97%)</td><td>1412.31 (-1.69%)</td><td>1404.09 (+0.67%)</td><td>13.16 <b>(-56.52%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1475.86 (n/a)</td><td>1431.88 (n/a)</td><td>1436.53 (n/a)</td><td>1394.77 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>2.98 <b>(+23.91%)</b></td><td>2.30 (+4.78%)</td><td>2.27 (+5.43%)</td><td>1.62 <b>(-21.64%)</b></td><td>0.52 <b>(+281.20%)</b></td><td>323.60 <b>(+27.60%)</b></td><td>237.76 (-0.69%)</td><td>231.20 (-5.13%)</td><td>176.10 (-19.29%)</td><td>56.52 <b>(+295.72%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>2.40 (n/a)</td><td>2.20 (n/a)</td><td>2.15 (n/a)</td><td>2.07 (n/a)</td><td>0.14 (n/a)</td><td>253.60 (n/a)</td><td>239.40 (n/a)</td><td>243.70 (n/a)</td><td>218.20 (n/a)</td><td>14.28 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>4.66 (-11.16%)</td><td>4.41 (-5.25%)</td><td>4.56 (-5.54%)</td><td>3.92 (-3.03%)</td><td>0.31 <b>(-45.58%)</b></td><td>267.60 (+3.12%)</td><td>238.76 (+4.70%)</td><td>230.10 (+5.89%)</td><td>225.10 (+12.55%)</td><td>17.63 <b>(-37.77%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>5.24 (n/a)</td><td>4.65 (n/a)</td><td>4.82 (n/a)</td><td>4.04 (n/a)</td><td>0.56 (n/a)</td><td>259.50 (n/a)</td><td>228.04 (n/a)</td><td>217.30 (n/a)</td><td>200.00 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>2.84 (-8.96%)</td><td>2.50 (-4.06%)</td><td>2.59 (-2.66%)</td><td>1.80 (-14.45%)</td><td>0.41 (+7.61%)</td><td>291.80 (+16.86%)</td><td>215.08 (+5.19%)</td><td>202.30 (+2.74%)</td><td>184.90 (+9.86%)</td><td>43.64 <b>(+41.39%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>3.12 (n/a)</td><td>2.61 (n/a)</td><td>2.66 (n/a)</td><td>2.10 (n/a)</td><td>0.38 (n/a)</td><td>249.70 (n/a)</td><td>204.46 (n/a)</td><td>196.90 (n/a)</td><td>168.30 (n/a)</td><td>30.86 (n/a)</td>
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
