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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.09 (-16.09%)</td><td>0.08 (-12.22%)</td><td>0.08 <b>(-28.88%)</b></td><td>0.07 (+10.90%)</td><td>0.01 <b>(-59.66%)</b></td><td>176.30 (-9.87%)</td><td>156.42 (+7.77%)</td><td>163.40 <b>(+40.62%)</b></td><td>129.40 (+19.26%)</td><td>18.18 <b>(-58.15%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>195.60 (n/a)</td><td>145.14 (n/a)</td><td>116.20 (n/a)</td><td>108.50 (n/a)</td><td>43.44 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 <b>(-27.81%)</b></td><td>0.07 (-9.48%)</td><td>0.07 (+11.12%)</td><td>0.05 (-6.65%)</td><td>0.01 <b>(-59.01%)</b></td><td>231.90 (+7.11%)</td><td>184.20 (+5.09%)</td><td>177.90 (-10.02%)</td><td>154.60 <b>(+38.53%)</b></td><td>28.63 <b>(-38.59%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>175.28 (n/a)</td><td>197.70 (n/a)</td><td>111.60 (n/a)</td><td>46.62 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.09 (+7.56%)</td><td>0.07 (-4.67%)</td><td>0.06 (-11.82%)</td><td>0.06 (-7.05%)</td><td>0.02 <b>(+60.95%)</b></td><td>215.10 (+7.55%)</td><td>185.70 (+7.42%)</td><td>205.60 (+13.40%)</td><td>131.30 (-7.01%)</td><td>37.63 <b>(+66.62%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>172.88 (n/a)</td><td>181.30 (n/a)</td><td>141.20 (n/a)</td><td>22.58 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 <b>(-21.07%)</b></td><td>0.06 (-17.92%)</td><td>0.05 (-18.09%)</td><td>0.04 <b>(-21.59%)</b></td><td>0.01 (-13.23%)</td><td>290.30 <b>(+27.55%)</b></td><td>227.48 <b>(+23.11%)</b></td><td>231.80 <b>(+22.06%)</b></td><td>159.80 <b>(+26.62%)</b></td><td>55.19 <b>(+45.97%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>227.60 (n/a)</td><td>184.78 (n/a)</td><td>189.90 (n/a)</td><td>126.20 (n/a)</td><td>37.81 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (+5.58%)</td><td>0.03 (-1.08%)</td><td>0.03 (-5.60%)</td><td>0.03 (-7.46%)</td><td>0.01 <b>(+86.62%)</b></td><td>188.40 (+8.03%)</td><td>161.78 (+2.64%)</td><td>167.00 (+5.96%)</td><td>133.90 (-5.30%)</td><td>25.94 <b>(+88.33%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>174.40 (n/a)</td><td>157.62 (n/a)</td><td>157.60 (n/a)</td><td>141.40 (n/a)</td><td>13.78 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.03 <b>(-23.54%)</b></td><td>0.03 <b>(-29.60%)</b></td><td>0.03 <b>(-34.77%)</b></td><td>0.02 <b>(-30.55%)</b></td><td>0.00 (-11.23%)</td><td>252.10 <b>(+43.97%)</b></td><td>206.80 <b>(+42.88%)</b></td><td>208.30 <b>(+53.27%)</b></td><td>165.20 <b>(+30.80%)</b></td><td>31.44 <b>(+64.37%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>175.10 (n/a)</td><td>144.74 (n/a)</td><td>135.90 (n/a)</td><td>126.30 (n/a)</td><td>19.13 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (-18.77%)</td><td>0.03 (-2.80%)</td><td>0.03 (+4.41%)</td><td>0.03 (+5.68%)</td><td>0.00 <b>(-49.23%)</b></td><td>193.30 (-5.38%)</td><td>166.84 (-0.48%)</td><td>169.40 (-4.24%)</td><td>135.30 <b>(+23.11%)</b></td><td>22.24 <b>(-39.94%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>167.64 (n/a)</td><td>176.90 (n/a)</td><td>109.90 (n/a)</td><td>37.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.03 (+19.19%)</td><td>0.03 (+17.30%)</td><td>0.03 (+12.83%)</td><td>0.02 <b>(+22.08%)</b></td><td>0.01 <b>(+34.49%)</b></td><td>251.40 (-18.08%)</td><td>204.12 (-14.18%)</td><td>204.80 (-11.38%)</td><td>155.50 (-16.08%)</td><td>41.39 (-8.15%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>306.90 (n/a)</td><td>237.86 (n/a)</td><td>231.10 (n/a)</td><td>185.30 (n/a)</td><td>45.06 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (+3.29%)</td><td>0.03 (+9.81%)</td><td>0.03 (+3.28%)</td><td>0.02 <b>(+33.45%)</b></td><td>0.01 (-15.22%)</td><td>247.40 <b>(-25.05%)</b></td><td>195.56 (-11.75%)</td><td>199.20 (-3.16%)</td><td>149.50 (-3.17%)</td><td>40.13 <b>(-40.64%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>330.10 (n/a)</td><td>221.60 (n/a)</td><td>205.70 (n/a)</td><td>154.40 (n/a)</td><td>67.60 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (+13.42%)</td><td>0.03 <b>(+21.54%)</b></td><td>0.03 <b>(+28.01%)</b></td><td>0.02 (+9.02%)</td><td>0.01 <b>(+22.74%)</b></td><td>237.30 (-8.27%)</td><td>183.92 (-17.29%)</td><td>175.10 <b>(-21.90%)</b></td><td>146.50 (-11.80%)</td><td>37.41 (-2.01%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.70 (n/a)</td><td>222.38 (n/a)</td><td>224.20 (n/a)</td><td>166.10 (n/a)</td><td>38.18 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (+8.31%)</td><td>0.03 (+3.96%)</td><td>0.03 (+7.83%)</td><td>0.02 (-9.21%)</td><td>0.01 <b>(+58.91%)</b></td><td>259.30 (+10.11%)</td><td>185.42 (-0.87%)</td><td>174.80 (-7.27%)</td><td>140.90 (-7.73%)</td><td>48.88 <b>(+57.17%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.50 (n/a)</td><td>187.04 (n/a)</td><td>188.50 (n/a)</td><td>152.70 (n/a)</td><td>31.10 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (+4.07%)</td><td>0.03 (+11.83%)</td><td>0.03 (+14.44%)</td><td>0.02 (-1.88%)</td><td>0.01 (+5.08%)</td><td>306.90 (+1.89%)</td><td>208.98 (-9.91%)</td><td>204.00 (-12.63%)</td><td>138.80 (-3.94%)</td><td>62.76 (+8.60%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>301.20 (n/a)</td><td>231.98 (n/a)</td><td>233.50 (n/a)</td><td>144.50 (n/a)</td><td>57.79 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>133.40 (n/a)</td><td>122.34 (n/a)</td><td>124.90 (n/a)</td><td>100.00 (n/a)</td><td>13.36 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>144.54 (n/a)</td><td>130.20 (n/a)</td><td>124.20 (n/a)</td><td>26.60 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>153.22 (n/a)</td><td>152.00 (n/a)</td><td>123.00 (n/a)</td><td>27.74 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>163.90 (n/a)</td><td>155.16 (n/a)</td><td>159.10 (n/a)</td><td>137.20 (n/a)</td><td>10.98 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>180.60 (n/a)</td><td>168.36 (n/a)</td><td>170.40 (n/a)</td><td>158.20 (n/a)</td><td>9.96 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.10 (n/a)</td><td>200.44 (n/a)</td><td>206.60 (n/a)</td><td>167.70 (n/a)</td><td>20.69 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>179.54 (n/a)</td><td>178.90 (n/a)</td><td>159.40 (n/a)</td><td>18.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>357.80 (n/a)</td><td>235.54 (n/a)</td><td>230.50 (n/a)</td><td>138.40 (n/a)</td><td>79.33 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>262.20 (n/a)</td><td>191.30 (n/a)</td><td>182.70 (n/a)</td><td>123.10 (n/a)</td><td>51.93 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.80 (n/a)</td><td>173.76 (n/a)</td><td>159.80 (n/a)</td><td>119.10 (n/a)</td><td>48.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>159.10 (n/a)</td><td>147.40 (n/a)</td><td>133.40 (n/a)</td><td>35.22 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.80 (n/a)</td><td>191.16 (n/a)</td><td>188.60 (n/a)</td><td>177.30 (n/a)</td><td>12.29 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>183.88 (n/a)</td><td>194.60 (n/a)</td><td>127.90 (n/a)</td><td>31.90 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>294.10 (n/a)</td><td>232.34 (n/a)</td><td>241.90 (n/a)</td><td>170.40 (n/a)</td><td>51.10 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.00 (n/a)</td><td>194.58 (n/a)</td><td>183.00 (n/a)</td><td>156.20 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>346.20 (n/a)</td><td>241.94 (n/a)</td><td>211.40 (n/a)</td><td>198.30 (n/a)</td><td>62.68 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>4.94 (+0.97%)</td><td>4.41 (+1.03%)</td><td>4.20 (-1.40%)</td><td>4.01 (-4.63%)</td><td>0.42 <b>(+43.90%)</b></td><td>2346.60 (+4.85%)</td><td>2146.64 (-0.65%)</td><td>2240.30 (+1.42%)</td><td>1905.10 (-0.97%)</td><td>199.58 <b>(+49.33%)</b></td><td>1941.82 (+0.97%)</td><td>1735.67 (+1.03%)</td><td>1651.26 (-1.40%)</td><td>1576.47 (-4.63%)</td><td>166.20 <b>(+43.90%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>4.89 (n/a)</td><td>4.37 (n/a)</td><td>4.26 (n/a)</td><td>4.20 (n/a)</td><td>0.29 (n/a)</td><td>2238.00 (n/a)</td><td>2160.62 (n/a)</td><td>2208.90 (n/a)</td><td>1923.70 (n/a)</td><td>133.65 (n/a)</td><td>1923.08 (n/a)</td><td>1717.89 (n/a)</td><td>1674.72 (n/a)</td><td>1652.98 (n/a)</td><td>115.49 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>1.35 <b>(+21.26%)</b></td><td>1.14 <b>(+29.46%)</b></td><td>1.30 <b>(+37.12%)</b></td><td>0.68 (+5.49%)</td><td>0.29 <b>(+35.60%)</b></td><td>326.40 (-5.23%)</td><td>207.14 <b>(-21.29%)</b></td><td>170.20 <b>(-27.08%)</b></td><td>163.80 (-17.52%)</td><td>69.49 (+3.04%)</td><td>57.63 <b>(+21.26%)</b></td><td>48.83 <b>(+29.46%)</b></td><td>55.44 <b>(+37.12%)</b></td><td>28.91 (+5.49%)</td><td>12.34 <b>(+35.60%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>1.11 (n/a)</td><td>0.88 (n/a)</td><td>0.95 (n/a)</td><td>0.64 (n/a)</td><td>0.21 (n/a)</td><td>344.40 (n/a)</td><td>263.16 (n/a)</td><td>233.40 (n/a)</td><td>198.60 (n/a)</td><td>67.44 (n/a)</td><td>47.52 (n/a)</td><td>37.72 (n/a)</td><td>40.43 (n/a)</td><td>27.41 (n/a)</td><td>9.10 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>1.31 (+19.08%)</td><td>1.07 (+19.47%)</td><td>1.20 <b>(+32.21%)</b></td><td>0.65 (-2.41%)</td><td>0.29 <b>(+79.16%)</b></td><td>339.00 (+2.45%)</td><td>221.90 (-12.45%)</td><td>184.00 <b>(-24.37%)</b></td><td>168.50 (-16.04%)</td><td>73.29 <b>(+47.97%)</b></td><td>56.00 (+19.08%)</td><td>45.76 (+19.47%)</td><td>51.29 <b>(+32.21%)</b></td><td>27.83 (-2.41%)</td><td>12.42 <b>(+79.16%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>1.10 (n/a)</td><td>0.90 (n/a)</td><td>0.91 (n/a)</td><td>0.67 (n/a)</td><td>0.16 (n/a)</td><td>330.90 (n/a)</td><td>253.46 (n/a)</td><td>243.30 (n/a)</td><td>200.70 (n/a)</td><td>49.53 (n/a)</td><td>47.03 (n/a)</td><td>38.31 (n/a)</td><td>38.79 (n/a)</td><td>28.52 (n/a)</td><td>6.94 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.52 (+0.82%)</td><td>0.52 (+0.21%)</td><td>0.52 (+0.08%)</td><td>0.52 (+0.06%)</td><td>0.00 <b>(+418.41%)</b></td><td>48668.40 (-0.06%)</td><td>48539.04 (-0.21%)</td><td>48595.00 (-0.08%)</td><td>48211.30 (-0.81%)</td><td>185.70 <b>(+413.10%)</b></td><td>356.35 (+0.82%)</td><td>353.94 (+0.21%)</td><td>353.53 (+0.08%)</td><td>353.00 (+0.06%)</td><td>1.36 <b>(+418.35%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48700.00 (n/a)</td><td>48640.04 (n/a)</td><td>48632.40 (n/a)</td><td>48607.20 (n/a)</td><td>36.19 (n/a)</td><td>353.44 (n/a)</td><td>353.20 (n/a)</td><td>353.26 (n/a)</td><td>352.77 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.88 (-1.34%)</td><td>0.88 (-0.69%)</td><td>0.88 (-0.66%)</td><td>0.87 (-0.70%)</td><td>0.00 <b>(-29.28%)</b></td><td>28863.80 (+0.71%)</td><td>28656.32 (+0.70%)</td><td>28678.50 (+0.66%)</td><td>28511.80 (+1.36%)</td><td>142.64 <b>(-27.75%)</b></td><td>602.55 (-1.34%)</td><td>599.53 (-0.69%)</td><td>599.05 (-0.66%)</td><td>595.20 (-0.70%)</td><td>2.98 <b>(-29.28%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28661.60 (n/a)</td><td>28458.36 (n/a)</td><td>28489.10 (n/a)</td><td>28130.10 (n/a)</td><td>197.41 (n/a)</td><td>610.73 (n/a)</td><td>603.71 (n/a)</td><td>603.03 (n/a)</td><td>599.40 (n/a)</td><td>4.21 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>3.43 (+2.00%)</td><td>3.28 (+0.08%)</td><td>3.31 (+1.28%)</td><td>3.14 (-1.17%)</td><td>0.12 <b>(+49.57%)</b></td><td>8012.50 (+1.19%)</td><td>7687.26 (-0.02%)</td><td>7600.00 (-1.26%)</td><td>7330.00 (-1.96%)</td><td>285.31 <b>(+49.40%)</b></td><td>2343.79 (+2.00%)</td><td>2237.32 (+0.08%)</td><td>2260.51 (+1.28%)</td><td>2144.14 (-1.17%)</td><td>83.03 <b>(+49.57%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>3.37 (n/a)</td><td>3.27 (n/a)</td><td>3.27 (n/a)</td><td>3.18 (n/a)</td><td>0.08 (n/a)</td><td>7918.60 (n/a)</td><td>7688.46 (n/a)</td><td>7697.30 (n/a)</td><td>7476.30 (n/a)</td><td>190.97 (n/a)</td><td>2297.90 (n/a)</td><td>2235.60 (n/a)</td><td>2231.94 (n/a)</td><td>2169.55 (n/a)</td><td>55.51 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>3.85 (-9.33%)</td><td>3.39 (-8.85%)</td><td>3.32 (-13.41%)</td><td>2.92 (+2.07%)</td><td>0.37 <b>(-32.73%)</b></td><td>2760.40 (-2.03%)</td><td>2400.60 (+8.59%)</td><td>2429.40 (+15.49%)</td><td>2093.20 (+10.29%)</td><td>264.75 <b>(-28.38%)</b></td><td>1009.89 (-9.33%)</td><td>889.15 (-8.85%)</td><td>870.16 (-13.41%)</td><td>765.79 (+2.07%)</td><td>97.46 <b>(-32.73%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>4.25 (n/a)</td><td>3.72 (n/a)</td><td>3.83 (n/a)</td><td>2.86 (n/a)</td><td>0.55 (n/a)</td><td>2817.70 (n/a)</td><td>2210.78 (n/a)</td><td>2103.60 (n/a)</td><td>1897.90 (n/a)</td><td>369.67 (n/a)</td><td>1113.83 (n/a)</td><td>975.44 (n/a)</td><td>1004.89 (n/a)</td><td>750.23 (n/a)</td><td>144.87 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.46 (-13.27%)</td><td>0.38 (-1.01%)</td><td>0.34 (-2.03%)</td><td>0.32 (-0.62%)</td><td>0.06 <b>(-28.33%)</b></td><td>3848.80 (+0.62%)</td><td>3367.78 (-0.23%)</td><td>3632.40 (+2.08%)</td><td>2689.60 (+15.29%)</td><td>517.52 (-14.24%)</td><td>24.95 (-13.27%)</td><td>20.34 (-1.01%)</td><td>18.48 (-2.03%)</td><td>17.44 (-0.62%)</td><td>3.34 <b>(-28.33%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.53 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td><td>3825.10 (n/a)</td><td>3375.60 (n/a)</td><td>3558.50 (n/a)</td><td>2332.80 (n/a)</td><td>603.43 (n/a)</td><td>28.77 (n/a)</td><td>20.55 (n/a)</td><td>18.86 (n/a)</td><td>17.54 (n/a)</td><td>4.67 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>6.42 (+6.23%)</td><td>5.02 (+10.75%)</td><td>4.72 (+0.90%)</td><td>3.96 (+19.20%)</td><td>0.92 (-15.19%)</td><td>1678.60 (-16.10%)</td><td>1358.40 (-11.51%)</td><td>1409.90 (-0.89%)</td><td>1036.40 (-5.87%)</td><td>237.03 <b>(-35.04%)</b></td><td>1982.97 (+6.23%)</td><td>1552.03 (+10.75%)</td><td>1457.75 (+0.90%)</td><td>1224.38 (+19.20%)</td><td>283.59 (-15.19%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>6.04 (n/a)</td><td>4.54 (n/a)</td><td>4.68 (n/a)</td><td>3.32 (n/a)</td><td>1.08 (n/a)</td><td>2000.80 (n/a)</td><td>1535.14 (n/a)</td><td>1422.50 (n/a)</td><td>1101.00 (n/a)</td><td>364.86 (n/a)</td><td>1866.76 (n/a)</td><td>1401.41 (n/a)</td><td>1444.76 (n/a)</td><td>1027.18 (n/a)</td><td>334.38 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.27 <b>(+24.00%)</b></td><td>0.23 <b>(+20.48%)</b></td><td>0.22 (+13.55%)</td><td>0.19 (+10.09%)</td><td>0.03 <b>(+84.27%)</b></td><td>0.26 <b>(+24.00%)</b></td><td>0.23 <b>(+20.48%)</b></td><td>0.22 (+13.55%)</td><td>0.19 (+10.09%)</td><td>0.03 <b>(+84.27%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>13.21 (+1.03%)</td><td>12.51 (+0.23%)</td><td>13.01 (+4.16%)</td><td>10.89 (-8.45%)</td><td>0.96 <b>(+121.07%)</b></td><td>13.21 (+1.03%)</td><td>12.51 (+0.23%)</td><td>13.00 (+4.16%)</td><td>10.89 (-8.45%)</td><td>0.96 <b>(+121.07%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>13.08 (n/a)</td><td>12.48 (n/a)</td><td>12.49 (n/a)</td><td>11.90 (n/a)</td><td>0.43 (n/a)</td><td>13.07 (n/a)</td><td>12.48 (n/a)</td><td>12.48 (n/a)</td><td>11.89 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>25.21 (+3.38%)</td><td>24.49 (+2.69%)</td><td>24.67 (+3.18%)</td><td>23.52 (+2.74%)</td><td>0.65 (+13.28%)</td><td>25.19 (+3.38%)</td><td>24.47 (+2.69%)</td><td>24.66 (+3.18%)</td><td>23.50 (+2.74%)</td><td>0.65 (+13.28%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>24.38 (n/a)</td><td>23.85 (n/a)</td><td>23.91 (n/a)</td><td>22.89 (n/a)</td><td>0.58 (n/a)</td><td>24.37 (n/a)</td><td>23.83 (n/a)</td><td>23.90 (n/a)</td><td>22.88 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>42.84 (+3.96%)</td><td>40.12 (+2.62%)</td><td>40.04 (+1.12%)</td><td>36.58 (-1.85%)</td><td>2.41 <b>(+47.00%)</b></td><td>42.82 (+3.96%)</td><td>40.10 (+2.62%)</td><td>40.02 (+1.12%)</td><td>36.56 (-1.85%)</td><td>2.41 <b>(+47.00%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>41.21 (n/a)</td><td>39.10 (n/a)</td><td>39.60 (n/a)</td><td>37.27 (n/a)</td><td>1.64 (n/a)</td><td>41.19 (n/a)</td><td>39.07 (n/a)</td><td>39.57 (n/a)</td><td>37.25 (n/a)</td><td>1.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>45.48 (+6.54%)</td><td>42.99 (+2.32%)</td><td>42.07 (+0.40%)</td><td>40.07 (-3.71%)</td><td>2.34 <b>(+488.23%)</b></td><td>45.45 (+6.54%)</td><td>42.97 (+2.32%)</td><td>42.05 (+0.40%)</td><td>40.05 (-3.71%)</td><td>2.34 <b>(+488.23%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>42.68 (n/a)</td><td>42.02 (n/a)</td><td>41.91 (n/a)</td><td>41.61 (n/a)</td><td>0.40 (n/a)</td><td>42.66 (n/a)</td><td>41.99 (n/a)</td><td>41.88 (n/a)</td><td>41.59 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>13.46 (+2.04%)</td><td>12.55 (+6.98%)</td><td>12.94 (+11.27%)</td><td>10.71 (+1.45%)</td><td>1.10 (+5.16%)</td><td>13.46 (+2.04%)</td><td>12.54 (+6.98%)</td><td>12.93 (+11.27%)</td><td>10.70 (+1.45%)</td><td>1.10 (+5.16%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>13.20 (n/a)</td><td>11.73 (n/a)</td><td>11.63 (n/a)</td><td>10.56 (n/a)</td><td>1.04 (n/a)</td><td>13.19 (n/a)</td><td>11.73 (n/a)</td><td>11.62 (n/a)</td><td>10.55 (n/a)</td><td>1.04 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>24.88 (+1.73%)</td><td>24.30 (+0.47%)</td><td>24.64 (+1.23%)</td><td>23.16 (-2.37%)</td><td>0.69 <b>(+130.38%)</b></td><td>24.87 (+1.73%)</td><td>24.28 (+0.47%)</td><td>24.62 (+1.23%)</td><td>23.14 (-2.37%)</td><td>0.69 <b>(+130.38%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>24.46 (n/a)</td><td>24.18 (n/a)</td><td>24.34 (n/a)</td><td>23.72 (n/a)</td><td>0.30 (n/a)</td><td>24.45 (n/a)</td><td>24.17 (n/a)</td><td>24.32 (n/a)</td><td>23.70 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>42.56 (+2.35%)</td><td>40.39 (+1.23%)</td><td>39.53 (-2.16%)</td><td>38.45 (+5.00%)</td><td>1.80 (-5.40%)</td><td>42.53 (+2.35%)</td><td>40.37 (+1.23%)</td><td>39.51 (-2.16%)</td><td>38.43 (+5.00%)</td><td>1.80 (-5.40%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>41.58 (n/a)</td><td>39.90 (n/a)</td><td>40.40 (n/a)</td><td>36.62 (n/a)</td><td>1.90 (n/a)</td><td>41.56 (n/a)</td><td>39.88 (n/a)</td><td>40.38 (n/a)</td><td>36.60 (n/a)</td><td>1.90 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>45.29 (+0.68%)</td><td>44.22 (+2.46%)</td><td>44.80 (+3.32%)</td><td>42.73 (+4.87%)</td><td>1.09 <b>(-28.60%)</b></td><td>45.26 (+0.68%)</td><td>44.19 (+2.46%)</td><td>44.77 (+3.32%)</td><td>42.70 (+4.87%)</td><td>1.08 <b>(-28.60%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>44.98 (n/a)</td><td>43.15 (n/a)</td><td>43.36 (n/a)</td><td>40.74 (n/a)</td><td>1.52 (n/a)</td><td>44.95 (n/a)</td><td>43.13 (n/a)</td><td>43.33 (n/a)</td><td>40.72 (n/a)</td><td>1.52 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.00 (n/a)</td><td>193.78 (n/a)</td><td>186.70 (n/a)</td><td>155.70 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>285.50 (n/a)</td><td>209.20 (n/a)</td><td>185.50 (n/a)</td><td>178.60 (n/a)</td><td>45.34 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.70 (n/a)</td><td>200.70 (n/a)</td><td>186.90 (n/a)</td><td>185.70 (n/a)</td><td>21.22 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.30 (n/a)</td><td>196.08 (n/a)</td><td>198.10 (n/a)</td><td>158.90 (n/a)</td><td>31.90 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>212.40 (n/a)</td><td>196.50 (n/a)</td><td>199.50 (n/a)</td><td>168.50 (n/a)</td><td>17.22 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>268.60 (n/a)</td><td>202.78 (n/a)</td><td>199.50 (n/a)</td><td>158.60 (n/a)</td><td>44.20 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.10 (n/a)</td><td>197.58 (n/a)</td><td>196.60 (n/a)</td><td>160.90 (n/a)</td><td>31.68 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>265.40 (n/a)</td><td>212.16 (n/a)</td><td>202.50 (n/a)</td><td>186.90 (n/a)</td><td>31.30 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 <b>(+20.06%)</b></td><td>0.05 (+8.20%)</td><td>0.05 (+8.09%)</td><td>0.04 (+9.51%)</td><td>0.01 <b>(+51.02%)</b></td><td>190.40 (-8.68%)</td><td>160.12 (-6.79%)</td><td>154.30 (-7.49%)</td><td>129.10 (-16.71%)</td><td>25.16 (+15.53%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>171.78 (n/a)</td><td>166.80 (n/a)</td><td>155.00 (n/a)</td><td>21.78 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (+17.81%)</td><td>0.04 (+1.66%)</td><td>0.04 (+6.23%)</td><td>0.02 <b>(-35.59%)</b></td><td>0.01 <b>(+137.87%)</b></td><td>378.30 <b>(+55.23%)</b></td><td>230.92 (+6.19%)</td><td>210.10 (-5.87%)</td><td>151.60 (-15.12%)</td><td>86.13 <b>(+237.59%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>243.70 (n/a)</td><td>217.46 (n/a)</td><td>223.20 (n/a)</td><td>178.60 (n/a)</td><td>25.51 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.07 <b>(+31.08%)</b></td><td>0.06 <b>(+25.10%)</b></td><td>0.05 (+18.63%)</td><td>0.04 (+15.65%)</td><td>0.01 <b>(+86.79%)</b></td><td>189.10 (-13.49%)</td><td>153.04 (-18.75%)</td><td>153.40 (-15.71%)</td><td>119.50 <b>(-23.74%)</b></td><td>29.03 <b>(+22.66%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.60 (n/a)</td><td>188.36 (n/a)</td><td>182.00 (n/a)</td><td>156.70 (n/a)</td><td>23.67 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 <b>(+42.96%)</b></td><td>0.06 <b>(+32.02%)</b></td><td>0.05 (+15.15%)</td><td>0.04 <b>(+40.25%)</b></td><td>0.01 <b>(+50.67%)</b></td><td>192.40 <b>(-28.71%)</b></td><td>148.84 <b>(-24.00%)</b></td><td>157.60 (-13.12%)</td><td>107.40 <b>(-30.03%)</b></td><td>32.97 <b>(-27.57%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>269.90 (n/a)</td><td>195.84 (n/a)</td><td>181.40 (n/a)</td><td>153.50 (n/a)</td><td>45.53 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (+15.57%)</td><td>0.04 (+2.40%)</td><td>0.05 (+3.74%)</td><td>0.03 <b>(-25.21%)</b></td><td>0.01 <b>(+279.66%)</b></td><td>280.50 <b>(+33.70%)</b></td><td>194.24 (+1.62%)</td><td>181.90 (-3.65%)</td><td>156.10 (-13.47%)</td><td>49.85 <b>(+350.09%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.80 (n/a)</td><td>191.14 (n/a)</td><td>188.80 (n/a)</td><td>180.40 (n/a)</td><td>11.08 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.07 (+17.24%)</td><td>0.05 (+14.30%)</td><td>0.05 (+14.23%)</td><td>0.04 (+0.44%)</td><td>0.01 <b>(+42.24%)</b></td><td>218.70 (-0.41%)</td><td>171.16 (-11.09%)</td><td>179.10 (-12.46%)</td><td>122.60 (-14.68%)</td><td>36.86 <b>(+20.54%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>192.50 (n/a)</td><td>204.60 (n/a)</td><td>143.70 (n/a)</td><td>30.58 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (+12.14%)</td><td>0.05 (+17.93%)</td><td>0.05 (+15.90%)</td><td>0.05 <b>(+23.09%)</b></td><td>0.00 (-18.25%)</td><td>181.80 (-18.77%)</td><td>167.22 (-15.66%)</td><td>171.10 (-13.67%)</td><td>149.00 (-10.83%)</td><td>13.33 <b>(-41.08%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>223.80 (n/a)</td><td>198.26 (n/a)</td><td>198.20 (n/a)</td><td>167.10 (n/a)</td><td>22.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 <b>(+24.46%)</b></td><td>0.05 <b>(+21.23%)</b></td><td>0.05 (+18.45%)</td><td>0.04 (+9.04%)</td><td>0.01 <b>(+99.28%)</b></td><td>202.50 (-8.25%)</td><td>165.04 (-16.60%)</td><td>166.90 (-15.58%)</td><td>140.80 (-19.68%)</td><td>24.68 <b>(+45.87%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>220.70 (n/a)</td><td>197.88 (n/a)</td><td>197.70 (n/a)</td><td>175.30 (n/a)</td><td>16.92 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.21 (-0.23%)</td><td>0.20 (-0.15%)</td><td>0.21 (-0.07%)</td><td>0.20 (-0.16%)</td><td>0.00 (-18.60%)</td><td>40988.20 (+0.16%)</td><td>40927.74 (+0.15%)</td><td>40913.30 (+0.07%)</td><td>40866.90 (+0.23%)</td><td>51.11 (-18.31%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40922.50 (n/a)</td><td>40867.56 (n/a)</td><td>40883.70 (n/a)</td><td>40772.90 (n/a)</td><td>62.57 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (-11.01%)</td><td>0.05 (+0.30%)</td><td>0.05 (+8.74%)</td><td>0.04 (-4.31%)</td><td>0.01 <b>(-20.98%)</b></td><td>232.00 (+4.50%)</td><td>174.16 (-1.11%)</td><td>164.60 (-8.04%)</td><td>138.50 (+12.42%)</td><td>35.45 (-2.04%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.00 (n/a)</td><td>176.12 (n/a)</td><td>179.00 (n/a)</td><td>123.20 (n/a)</td><td>36.19 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 <b>(-22.81%)</b></td><td>0.07 (+1.70%)</td><td>0.07 (+4.02%)</td><td>0.06 <b>(+23.54%)</b></td><td>0.01 <b>(-67.22%)</b></td><td>195.70 (-19.07%)</td><td>169.64 (-6.48%)</td><td>164.70 (-3.85%)</td><td>157.10 <b>(+29.51%)</b></td><td>16.02 <b>(-65.80%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>241.80 (n/a)</td><td>181.40 (n/a)</td><td>171.30 (n/a)</td><td>121.30 (n/a)</td><td>46.86 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (-15.66%)</td><td>0.05 (-4.10%)</td><td>0.05 (+0.10%)</td><td>0.05 (+0.07%)</td><td>0.00 <b>(-54.86%)</b></td><td>177.80 (-0.06%)</td><td>159.48 (+2.56%)</td><td>162.50 (-0.06%)</td><td>144.60 (+18.52%)</td><td>12.97 <b>(-47.52%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.90 (n/a)</td><td>155.50 (n/a)</td><td>162.60 (n/a)</td><td>122.00 (n/a)</td><td>24.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.07 (+8.51%)</td><td>0.05 (-11.03%)</td><td>0.05 (-12.69%)</td><td>0.03 <b>(-42.95%)</b></td><td>0.02 <b>(+129.27%)</b></td><td>379.40 <b>(+75.32%)</b></td><td>217.40 <b>(+24.87%)</b></td><td>196.60 (+14.50%)</td><td>139.20 (-7.81%)</td><td>95.58 <b>(+275.95%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>174.10 (n/a)</td><td>171.70 (n/a)</td><td>151.00 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (-14.09%)</td><td>0.04 (-12.42%)</td><td>0.05 (-1.89%)</td><td>0.03 <b>(-23.44%)</b></td><td>0.01 (+4.74%)</td><td>260.30 <b>(+30.67%)</b></td><td>195.64 (+15.50%)</td><td>179.90 (+1.93%)</td><td>161.30 (+16.46%)</td><td>38.78 <b>(+65.07%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>169.38 (n/a)</td><td>176.50 (n/a)</td><td>138.50 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 (-10.45%)</td><td>0.06 (-2.16%)</td><td>0.06 (+7.54%)</td><td>0.05 (+2.40%)</td><td>0.01 <b>(-35.41%)</b></td><td>215.60 (-2.36%)</td><td>166.30 (-0.98%)</td><td>167.30 (-7.00%)</td><td>131.90 (+11.69%)</td><td>32.38 <b>(-27.23%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>220.80 (n/a)</td><td>167.94 (n/a)</td><td>179.90 (n/a)</td><td>118.10 (n/a)</td><td>44.50 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 <b>(+25.72%)</b></td><td>0.05 (+13.53%)</td><td>0.05 (+13.34%)</td><td>0.04 <b>(+20.29%)</b></td><td>0.01 <b>(+27.76%)</b></td><td>198.90 (-16.88%)</td><td>161.88 (-11.77%)</td><td>171.30 (-11.75%)</td><td>103.60 <b>(-20.43%)</b></td><td>35.27 (-19.03%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.30 (n/a)</td><td>183.48 (n/a)</td><td>194.10 (n/a)</td><td>130.20 (n/a)</td><td>43.56 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 (+11.79%)</td><td>0.05 (+11.45%)</td><td>0.05 (+14.79%)</td><td>0.04 (+17.91%)</td><td>0.02 (+5.55%)</td><td>243.70 (-15.21%)</td><td>180.72 (-11.37%)</td><td>170.00 (-12.87%)</td><td>114.60 (-10.54%)</td><td>48.57 <b>(-21.03%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>287.40 (n/a)</td><td>203.90 (n/a)</td><td>195.10 (n/a)</td><td>128.10 (n/a)</td><td>61.50 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.07 <b>(+22.29%)</b></td><td>0.05 (-11.50%)</td><td>0.05 (-14.80%)</td><td>0.02 <b>(-50.04%)</b></td><td>0.02 <b>(+203.24%)</b></td><td>367.80 <b>(+100.22%)</b></td><td>204.48 <b>(+29.52%)</b></td><td>174.70 (+17.41%)</td><td>112.70 (-18.27%)</td><td>96.97 <b>(+419.99%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>157.88 (n/a)</td><td>148.80 (n/a)</td><td>137.90 (n/a)</td><td>18.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (+0.94%)</td><td>0.06 (+12.54%)</td><td>0.06 <b>(+20.18%)</b></td><td>0.05 <b>(+29.53%)</b></td><td>0.00 <b>(-61.73%)</b></td><td>174.00 <b>(-22.80%)</b></td><td>162.86 (-12.98%)</td><td>165.10 (-16.78%)</td><td>150.80 (-0.92%)</td><td>9.56 <b>(-69.90%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.40 (n/a)</td><td>187.16 (n/a)</td><td>198.40 (n/a)</td><td>152.20 (n/a)</td><td>31.74 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (-3.21%)</td><td>0.05 (-5.92%)</td><td>0.05 (+8.01%)</td><td>0.03 <b>(-22.22%)</b></td><td>0.01 (+6.91%)</td><td>290.90 <b>(+28.55%)</b></td><td>193.26 (+8.98%)</td><td>180.20 (-7.40%)</td><td>126.70 (+3.34%)</td><td>61.27 <b>(+47.11%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>177.34 (n/a)</td><td>194.60 (n/a)</td><td>122.60 (n/a)</td><td>41.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (+14.73%)</td><td>0.04 (+15.00%)</td><td>0.04 (+3.52%)</td><td>0.04 <b>(+38.67%)</b></td><td>0.01 (+6.55%)</td><td>229.60 <b>(-27.89%)</b></td><td>200.92 (-13.93%)</td><td>217.60 (-3.42%)</td><td>150.10 (-12.83%)</td><td>35.26 <b>(-33.24%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>318.40 (n/a)</td><td>233.44 (n/a)</td><td>225.30 (n/a)</td><td>172.20 (n/a)</td><td>52.81 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (+14.49%)</td><td>0.05 (+15.58%)</td><td>0.05 <b>(+25.50%)</b></td><td>0.03 (-7.73%)</td><td>0.01 <b>(+49.52%)</b></td><td>248.90 (+8.41%)</td><td>167.96 (-11.08%)</td><td>155.70 <b>(-20.32%)</b></td><td>128.90 (-12.67%)</td><td>46.95 <b>(+50.44%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>188.88 (n/a)</td><td>195.40 (n/a)</td><td>147.60 (n/a)</td><td>31.21 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (-12.61%)</td><td>0.04 (-2.87%)</td><td>0.04 (-0.14%)</td><td>0.04 (+10.71%)</td><td>0.00 <b>(-50.80%)</b></td><td>233.90 (-9.66%)</td><td>214.88 (+1.59%)</td><td>210.30 (+0.10%)</td><td>194.10 (+14.45%)</td><td>16.29 <b>(-48.67%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>258.90 (n/a)</td><td>211.52 (n/a)</td><td>210.10 (n/a)</td><td>169.60 (n/a)</td><td>31.73 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (+14.40%)</td><td>0.04 (+2.23%)</td><td>0.04 (-0.51%)</td><td>0.03 (-13.43%)</td><td>0.01 <b>(+86.92%)</b></td><td>305.40 (+15.51%)</td><td>221.06 (+0.49%)</td><td>216.70 (+0.51%)</td><td>168.30 (-12.62%)</td><td>51.22 <b>(+90.67%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>264.40 (n/a)</td><td>219.98 (n/a)</td><td>215.60 (n/a)</td><td>192.60 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.75 (-17.82%)</td><td>0.58 (-8.33%)</td><td>0.48 (-0.76%)</td><td>0.46 (+2.26%)</td><td>0.15 <b>(-32.84%)</b></td><td>213.70 (-2.20%)</td><td>179.38 (+4.49%)</td><td>206.40 (+0.78%)</td><td>131.60 <b>(+21.74%)</b></td><td>43.11 <b>(-20.78%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.91 (n/a)</td><td>0.63 (n/a)</td><td>0.48 (n/a)</td><td>0.45 (n/a)</td><td>0.23 (n/a)</td><td>218.50 (n/a)</td><td>171.68 (n/a)</td><td>204.80 (n/a)</td><td>108.10 (n/a)</td><td>54.42 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.70 <b>(+30.11%)</b></td><td>0.48 (-4.47%)</td><td>0.42 (-16.68%)</td><td>0.36 <b>(-27.12%)</b></td><td>0.15 <b>(+707.21%)</b></td><td>275.10 <b>(+37.21%)</b></td><td>218.84 (+12.13%)</td><td>236.60 (+19.98%)</td><td>140.80 <b>(-23.14%)</b></td><td>60.23 <b>(+775.41%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.54 (n/a)</td><td>0.50 (n/a)</td><td>0.50 (n/a)</td><td>0.49 (n/a)</td><td>0.02 (n/a)</td><td>200.50 (n/a)</td><td>195.16 (n/a)</td><td>197.20 (n/a)</td><td>183.20 (n/a)</td><td>6.88 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.58 <b>(-25.35%)</b></td><td>0.53 (-15.11%)</td><td>0.55 (-9.33%)</td><td>0.43 (-9.65%)</td><td>0.07 <b>(-42.80%)</b></td><td>228.40 (+10.66%)</td><td>189.06 (+16.16%)</td><td>178.10 (+10.28%)</td><td>168.70 <b>(+34.00%)</b></td><td>25.49 (-16.08%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.78 (n/a)</td><td>0.62 (n/a)</td><td>0.61 (n/a)</td><td>0.48 (n/a)</td><td>0.11 (n/a)</td><td>206.40 (n/a)</td><td>162.76 (n/a)</td><td>161.50 (n/a)</td><td>125.90 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.61 (+19.35%)</td><td>0.51 (+9.26%)</td><td>0.51 (+5.81%)</td><td>0.40 (+11.43%)</td><td>0.10 <b>(+63.16%)</b></td><td>246.10 (-10.28%)</td><td>200.22 (-7.08%)</td><td>192.00 (-5.47%)</td><td>161.80 (-16.21%)</td><td>39.73 (+19.21%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.51 (n/a)</td><td>0.46 (n/a)</td><td>0.48 (n/a)</td><td>0.36 (n/a)</td><td>0.06 (n/a)</td><td>274.30 (n/a)</td><td>215.48 (n/a)</td><td>203.10 (n/a)</td><td>193.10 (n/a)</td><td>33.33 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.47 (-3.94%)</td><td>0.44 (+8.92%)</td><td>0.44 (+10.72%)</td><td>0.41 <b>(+25.63%)</b></td><td>0.02 <b>(-62.15%)</b></td><td>177.90 <b>(-20.40%)</b></td><td>167.62 (-9.57%)</td><td>168.60 (-9.69%)</td><td>155.70 (+4.08%)</td><td>8.47 <b>(-68.52%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.06 (n/a)</td><td>223.50 (n/a)</td><td>185.36 (n/a)</td><td>186.70 (n/a)</td><td>149.60 (n/a)</td><td>26.90 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.49 (+6.34%)</td><td>0.43 (+7.93%)</td><td>0.42 (+2.26%)</td><td>0.34 (+2.81%)</td><td>0.06 <b>(+23.16%)</b></td><td>218.10 (-2.72%)</td><td>174.80 (-6.89%)</td><td>175.10 (-2.18%)</td><td>150.60 (-5.93%)</td><td>27.47 (+10.28%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.46 (n/a)</td><td>0.40 (n/a)</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>224.20 (n/a)</td><td>187.74 (n/a)</td><td>179.00 (n/a)</td><td>160.10 (n/a)</td><td>24.91 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.48 (-5.69%)</td><td>0.41 (-3.63%)</td><td>0.41 (-1.30%)</td><td>0.34 (-9.53%)</td><td>0.05 (+5.85%)</td><td>216.40 (+10.52%)</td><td>181.42 (+4.11%)</td><td>182.00 (+1.34%)</td><td>154.60 (+6.04%)</td><td>23.71 <b>(+25.79%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.05 (n/a)</td><td>195.80 (n/a)</td><td>174.26 (n/a)</td><td>179.60 (n/a)</td><td>145.80 (n/a)</td><td>18.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.53 (+6.46%)</td><td>0.39 (+12.13%)</td><td>0.37 (+6.01%)</td><td>0.26 (+8.70%)</td><td>0.12 <b>(+24.17%)</b></td><td>287.90 (-8.02%)</td><td>201.70 (-9.24%)</td><td>200.80 (-5.64%)</td><td>139.10 (-6.08%)</td><td>61.81 (+3.85%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.09 (n/a)</td><td>313.00 (n/a)</td><td>222.24 (n/a)</td><td>212.80 (n/a)</td><td>148.10 (n/a)</td><td>59.52 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.93 (+5.95%)</td><td>0.71 (-6.54%)</td><td>0.72 (-3.39%)</td><td>0.56 (-17.86%)</td><td>0.14 <b>(+75.71%)</b></td><td>234.90 <b>(+21.77%)</b></td><td>190.22 (+9.25%)</td><td>182.80 (+3.45%)</td><td>140.90 (-5.63%)</td><td>35.26 <b>(+100.00%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.88 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.68 (n/a)</td><td>0.08 (n/a)</td><td>192.90 (n/a)</td><td>174.12 (n/a)</td><td>176.70 (n/a)</td><td>149.30 (n/a)</td><td>17.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.78 (-16.75%)</td><td>0.69 (-13.38%)</td><td>0.67 (-13.66%)</td><td>0.60 (-13.72%)</td><td>0.07 (-16.90%)</td><td>217.00 (+15.86%)</td><td>191.54 (+15.41%)</td><td>195.50 (+15.82%)</td><td>167.40 <b>(+20.09%)</b></td><td>20.22 (+16.84%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.94 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.70 (n/a)</td><td>0.09 (n/a)</td><td>187.30 (n/a)</td><td>165.96 (n/a)</td><td>168.80 (n/a)</td><td>139.40 (n/a)</td><td>17.31 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>1.03 (+0.74%)</td><td>0.78 (-5.74%)</td><td>0.72 (-7.35%)</td><td>0.55 (-17.53%)</td><td>0.19 <b>(+42.53%)</b></td><td>236.30 <b>(+21.24%)</b></td><td>176.74 (+9.11%)</td><td>181.60 (+7.97%)</td><td>127.10 (-0.70%)</td><td>43.13 <b>(+70.80%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>1.02 (n/a)</td><td>0.83 (n/a)</td><td>0.78 (n/a)</td><td>0.67 (n/a)</td><td>0.13 (n/a)</td><td>194.90 (n/a)</td><td>161.98 (n/a)</td><td>168.20 (n/a)</td><td>128.00 (n/a)</td><td>25.25 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.00 (+0.00%)</td><td>0.00 (-5.45%)</td><td>0.00 (-8.33%)</td><td>0.00 (+0.00%)</td><td>0.00 (-5.13%)</td><td>4475.59 (-1.78%)</td><td>3994.10 (+4.39%)</td><td>3821.83 (+8.97%)</td><td>3517.56 (+0.54%)</td><td>410.30 (-13.70%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4556.47 (n/a)</td><td>3826.12 (n/a)</td><td>3507.16 (n/a)</td><td>3498.51 (n/a)</td><td>475.41 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.00 (+4.55%)</td><td>0.00 (-5.83%)</td><td>0.00 (-14.29%)</td><td>0.00 (-10.53%)</td><td>0.00 <b>(+152.68%)</b></td><td>4772.10 (+8.54%)</td><td>4236.73 (+5.13%)</td><td>4510.67 (+14.09%)</td><td>3533.78 (-4.83%)</td><td>592.76 <b>(+125.63%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4396.72 (n/a)</td><td>4030.10 (n/a)</td><td>3953.60 (n/a)</td><td>3713.01 (n/a)</td><td>262.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.28 (-1.08%)</td><td>0.18 (-7.24%)</td><td>0.15 (-1.31%)</td><td>0.14 (-7.97%)</td><td>0.06 (-11.55%)</td><td>15396.52 (+8.66%)</td><td>12268.40 (+6.33%)</td><td>13872.79 (+1.37%)</td><td>7618.14 (+1.10%)</td><td>3148.14 (-6.19%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>14169.06 (n/a)</td><td>11537.75 (n/a)</td><td>13685.12 (n/a)</td><td>7535.45 (n/a)</td><td>3355.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>3.10 (n/a)</td><td>2.72 (n/a)</td><td>2.74 (n/a)</td><td>2.18 (n/a)</td><td>0.39 (n/a)</td><td>240.40 (n/a)</td><td>195.82 (n/a)</td><td>191.10 (n/a)</td><td>169.10 (n/a)</td><td>29.54 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>5.51 (n/a)</td><td>5.12 (n/a)</td><td>5.32 (n/a)</td><td>4.29 (n/a)</td><td>0.48 (n/a)</td><td>244.30 (n/a)</td><td>206.60 (n/a)</td><td>197.30 (n/a)</td><td>190.30 (n/a)</td><td>21.62 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>3.43 (n/a)</td><td>2.86 (n/a)</td><td>2.85 (n/a)</td><td>2.29 (n/a)</td><td>0.47 (n/a)</td><td>229.10 (n/a)</td><td>187.10 (n/a)</td><td>183.70 (n/a)</td><td>152.70 (n/a)</td><td>31.23 (n/a)</td>
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
