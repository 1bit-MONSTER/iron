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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (-16.35%)</td><td>0.06 (-13.68%)</td><td>0.06 (-14.41%)</td><td>0.06 (-8.65%)</td><td>0.01 <b>(-35.89%)</b></td><td>206.10 (+9.45%)</td><td>193.04 (+15.34%)</td><td>198.80 (+16.80%)</td><td>169.30 (+19.56%)</td><td>14.96 (-15.78%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>188.30 (n/a)</td><td>167.36 (n/a)</td><td>170.20 (n/a)</td><td>141.60 (n/a)</td><td>17.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 <b>(-23.61%)</b></td><td>0.07 (-9.11%)</td><td>0.07 (+6.17%)</td><td>0.06 (-2.04%)</td><td>0.01 <b>(-67.64%)</b></td><td>214.50 (+2.09%)</td><td>186.82 (+6.29%)</td><td>184.30 (-5.78%)</td><td>173.00 <b>(+30.86%)</b></td><td>16.59 <b>(-55.99%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>210.10 (n/a)</td><td>175.76 (n/a)</td><td>195.60 (n/a)</td><td>132.20 (n/a)</td><td>37.70 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (-18.23%)</td><td>0.06 (-5.30%)</td><td>0.06 (-0.38%)</td><td>0.05 (+17.67%)</td><td>0.01 <b>(-55.17%)</b></td><td>257.80 (-15.03%)</td><td>216.84 (+0.85%)</td><td>205.20 (+0.39%)</td><td>187.00 <b>(+22.30%)</b></td><td>28.16 <b>(-53.04%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>303.40 (n/a)</td><td>215.02 (n/a)</td><td>204.40 (n/a)</td><td>152.90 (n/a)</td><td>59.96 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (-19.38%)</td><td>0.06 (-14.91%)</td><td>0.06 (-16.79%)</td><td>0.05 (-8.10%)</td><td>0.00 <b>(-65.69%)</b></td><td>235.00 (+8.80%)</td><td>218.58 (+16.56%)</td><td>217.20 <b>(+20.20%)</b></td><td>208.00 <b>(+24.03%)</b></td><td>9.94 <b>(-53.01%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>187.52 (n/a)</td><td>180.70 (n/a)</td><td>167.70 (n/a)</td><td>21.15 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (+9.25%)</td><td>0.04 (+15.57%)</td><td>0.04 <b>(+35.13%)</b></td><td>0.03 (-4.34%)</td><td>0.01 <b>(+33.61%)</b></td><td>203.10 (+4.58%)</td><td>154.40 (-12.25%)</td><td>139.10 <b>(-26.01%)</b></td><td>122.50 (-8.45%)</td><td>32.70 <b>(+30.62%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.20 (n/a)</td><td>175.96 (n/a)</td><td>188.00 (n/a)</td><td>133.80 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (+15.77%)</td><td>0.03 <b>(+21.17%)</b></td><td>0.03 <b>(+22.06%)</b></td><td>0.03 <b>(+29.45%)</b></td><td>0.01 (+1.59%)</td><td>181.50 <b>(-22.73%)</b></td><td>160.16 (-18.34%)</td><td>164.10 (-18.07%)</td><td>116.60 (-13.63%)</td><td>26.44 <b>(-30.65%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>196.14 (n/a)</td><td>200.30 (n/a)</td><td>135.00 (n/a)</td><td>38.12 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (+15.29%)</td><td>0.03 (+13.92%)</td><td>0.04 (+18.05%)</td><td>0.03 (+7.99%)</td><td>0.00 <b>(+29.64%)</b></td><td>184.70 (-7.42%)</td><td>154.18 (-11.83%)</td><td>142.20 (-15.26%)</td><td>131.90 (-13.22%)</td><td>22.95 (+3.00%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>199.50 (n/a)</td><td>174.86 (n/a)</td><td>167.80 (n/a)</td><td>152.00 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (-2.44%)</td><td>0.03 (-7.62%)</td><td>0.03 (-10.29%)</td><td>0.02 (-16.65%)</td><td>0.01 (+11.12%)</td><td>252.60 (+19.94%)</td><td>194.48 (+9.36%)</td><td>189.60 (+11.46%)</td><td>144.30 (+2.56%)</td><td>39.19 <b>(+33.25%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>177.84 (n/a)</td><td>170.10 (n/a)</td><td>140.70 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (+13.26%)</td><td>0.03 (+13.98%)</td><td>0.03 (+8.35%)</td><td>0.02 <b>(+75.11%)</b></td><td>0.00 <b>(-32.89%)</b></td><td>213.40 <b>(-42.88%)</b></td><td>177.64 (-18.19%)</td><td>169.70 (-7.72%)</td><td>147.80 (-11.66%)</td><td>28.99 <b>(-67.08%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>373.60 (n/a)</td><td>217.14 (n/a)</td><td>183.90 (n/a)</td><td>167.30 (n/a)</td><td>88.07 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.03 <b>(-47.81%)</b></td><td>0.03 <b>(-24.18%)</b></td><td>0.03 (+1.59%)</td><td>0.02 (-9.74%)</td><td>0.00 <b>(-79.79%)</b></td><td>239.90 (+10.76%)</td><td>208.92 <b>(+20.18%)</b></td><td>203.50 (-1.60%)</td><td>181.30 <b>(+91.65%)</b></td><td>22.58 <b>(-57.96%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>173.84 (n/a)</td><td>206.80 (n/a)</td><td>94.60 (n/a)</td><td>53.71 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.03 (-2.65%)</td><td>0.03 (-8.62%)</td><td>0.03 (+3.53%)</td><td>0.02 <b>(-33.09%)</b></td><td>0.01 <b>(+38.16%)</b></td><td>315.50 <b>(+49.46%)</b></td><td>212.76 (+13.48%)</td><td>197.40 (-3.38%)</td><td>153.70 (+2.67%)</td><td>60.91 <b>(+120.51%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.10 (n/a)</td><td>187.48 (n/a)</td><td>204.30 (n/a)</td><td>149.70 (n/a)</td><td>27.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.03 (-4.95%)</td><td>0.02 (-4.87%)</td><td>0.02 (-8.36%)</td><td>0.02 (-2.31%)</td><td>0.00 (-8.56%)</td><td>238.50 (+2.36%)</td><td>220.06 (+5.05%)</td><td>226.30 (+9.17%)</td><td>196.90 (+5.18%)</td><td>18.24 (-1.78%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.00 (n/a)</td><td>209.48 (n/a)</td><td>207.30 (n/a)</td><td>187.20 (n/a)</td><td>18.57 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.90 (n/a)</td><td>173.36 (n/a)</td><td>179.30 (n/a)</td><td>145.90 (n/a)</td><td>25.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>374.40 (n/a)</td><td>226.54 (n/a)</td><td>211.20 (n/a)</td><td>148.60 (n/a)</td><td>87.49 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.70 (n/a)</td><td>187.52 (n/a)</td><td>197.70 (n/a)</td><td>146.10 (n/a)</td><td>33.33 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>223.00 (n/a)</td><td>208.92 (n/a)</td><td>211.90 (n/a)</td><td>181.90 (n/a)</td><td>16.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>210.90 (n/a)</td><td>195.16 (n/a)</td><td>195.60 (n/a)</td><td>182.20 (n/a)</td><td>12.09 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.30 (n/a)</td><td>179.24 (n/a)</td><td>186.30 (n/a)</td><td>145.50 (n/a)</td><td>19.49 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.60 (n/a)</td><td>177.28 (n/a)</td><td>159.20 (n/a)</td><td>152.40 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>185.02 (n/a)</td><td>181.60 (n/a)</td><td>161.60 (n/a)</td><td>20.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.30 (n/a)</td><td>181.08 (n/a)</td><td>185.80 (n/a)</td><td>149.10 (n/a)</td><td>25.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>334.80 (n/a)</td><td>209.96 (n/a)</td><td>167.30 (n/a)</td><td>141.70 (n/a)</td><td>79.83 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>172.96 (n/a)</td><td>174.30 (n/a)</td><td>139.50 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.10 (n/a)</td><td>198.24 (n/a)</td><td>205.80 (n/a)</td><td>165.20 (n/a)</td><td>34.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>168.64 (n/a)</td><td>163.50 (n/a)</td><td>133.10 (n/a)</td><td>33.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>277.40 (n/a)</td><td>214.44 (n/a)</td><td>186.60 (n/a)</td><td>157.10 (n/a)</td><td>54.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.40 (n/a)</td><td>194.60 (n/a)</td><td>201.90 (n/a)</td><td>154.40 (n/a)</td><td>27.23 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>292.90 (n/a)</td><td>251.12 (n/a)</td><td>239.50 (n/a)</td><td>221.90 (n/a)</td><td>28.13 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>4.22 (+0.54%)</td><td>4.14 (+2.76%)</td><td>4.17 (+0.19%)</td><td>4.06 (+15.66%)</td><td>0.07 <b>(-76.30%)</b></td><td>2318.60 (-13.54%)</td><td>2271.40 (-3.12%)</td><td>2255.70 (-0.19%)</td><td>2226.70 (-0.54%)</td><td>38.34 <b>(-79.73%)</b></td><td>1661.34 (+0.54%)</td><td>1629.06 (+2.76%)</td><td>1640.03 (+0.19%)</td><td>1595.52 (+15.66%)</td><td>27.41 <b>(-76.29%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>4.20 (n/a)</td><td>4.03 (n/a)</td><td>4.16 (n/a)</td><td>3.51 (n/a)</td><td>0.29 (n/a)</td><td>2681.60 (n/a)</td><td>2344.54 (n/a)</td><td>2260.00 (n/a)</td><td>2238.80 (n/a)</td><td>189.12 (n/a)</td><td>1652.42 (n/a)</td><td>1585.34 (n/a)</td><td>1636.91 (n/a)</td><td>1379.54 (n/a)</td><td>115.64 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>1.01 <b>(-22.64%)</b></td><td>0.92 (-14.96%)</td><td>0.99 (-10.31%)</td><td>0.60 <b>(-22.45%)</b></td><td>0.18 (-11.45%)</td><td>367.50 <b>(+28.95%)</b></td><td>251.42 (+18.71%)</td><td>223.10 (+11.49%)</td><td>218.60 <b>(+29.27%)</b></td><td>65.03 <b>(+45.75%)</b></td><td>43.16 <b>(-22.64%)</b></td><td>39.09 (-14.96%)</td><td>42.30 (-10.31%)</td><td>25.68 <b>(-22.45%)</b></td><td>7.54 (-11.45%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>1.31 (n/a)</td><td>1.08 (n/a)</td><td>1.11 (n/a)</td><td>0.78 (n/a)</td><td>0.20 (n/a)</td><td>285.00 (n/a)</td><td>211.80 (n/a)</td><td>200.10 (n/a)</td><td>169.10 (n/a)</td><td>44.62 (n/a)</td><td>55.79 (n/a)</td><td>45.97 (n/a)</td><td>47.16 (n/a)</td><td>33.11 (n/a)</td><td>8.52 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>1.06 (-6.28%)</td><td>0.82 (-4.25%)</td><td>0.88 (-1.11%)</td><td>0.60 (-10.79%)</td><td>0.20 (+7.44%)</td><td>370.60 (+12.07%)</td><td>281.78 (+5.86%)</td><td>251.90 (+1.12%)</td><td>209.50 (+6.72%)</td><td>71.26 <b>(+28.51%)</b></td><td>45.05 (-6.28%)</td><td>35.19 (-4.25%)</td><td>37.46 (-1.11%)</td><td>25.46 (-10.79%)</td><td>8.46 (+7.44%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>1.13 (n/a)</td><td>0.86 (n/a)</td><td>0.89 (n/a)</td><td>0.67 (n/a)</td><td>0.18 (n/a)</td><td>330.70 (n/a)</td><td>266.18 (n/a)</td><td>249.10 (n/a)</td><td>196.30 (n/a)</td><td>55.45 (n/a)</td><td>48.07 (n/a)</td><td>36.75 (n/a)</td><td>37.88 (n/a)</td><td>28.54 (n/a)</td><td>7.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.52 (-0.68%)</td><td>0.52 (-0.26%)</td><td>0.52 (-0.03%)</td><td>0.52 (-0.21%)</td><td>0.00 <b>(-46.12%)</b></td><td>48846.00 (+0.22%)</td><td>48691.90 (+0.26%)</td><td>48647.20 (+0.03%)</td><td>48620.40 (+0.68%)</td><td>94.55 <b>(-45.61%)</b></td><td>353.35 (-0.68%)</td><td>352.83 (-0.26%)</td><td>353.15 (-0.03%)</td><td>351.71 (-0.21%)</td><td>0.68 <b>(-46.12%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48741.00 (n/a)</td><td>48565.04 (n/a)</td><td>48630.30 (n/a)</td><td>48290.30 (n/a)</td><td>173.85 (n/a)</td><td>355.76 (n/a)</td><td>353.75 (n/a)</td><td>353.28 (n/a)</td><td>352.47 (n/a)</td><td>1.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.90 (+0.80%)</td><td>0.89 (+0.57%)</td><td>0.89 (+0.20%)</td><td>0.89 (+0.97%)</td><td>0.01 (-18.19%)</td><td>28380.80 (-0.96%)</td><td>28180.52 (-0.57%)</td><td>28244.20 (-0.20%)</td><td>27891.40 (-0.79%)</td><td>195.51 (-19.58%)</td><td>615.96 (+0.80%)</td><td>609.66 (+0.57%)</td><td>608.26 (+0.20%)</td><td>605.33 (+0.97%)</td><td>4.25 (-18.19%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28655.50 (n/a)</td><td>28342.74 (n/a)</td><td>28300.50 (n/a)</td><td>28114.40 (n/a)</td><td>243.10 (n/a)</td><td>611.07 (n/a)</td><td>606.18 (n/a)</td><td>607.05 (n/a)</td><td>599.53 (n/a)</td><td>5.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>3.32 (-0.18%)</td><td>3.23 (+1.21%)</td><td>3.22 (+2.03%)</td><td>3.16 (+1.42%)</td><td>0.07 (-16.37%)</td><td>7972.20 (-1.40%)</td><td>7798.12 (-1.22%)</td><td>7820.80 (-1.99%)</td><td>7584.60 (+0.18%)</td><td>169.25 (-17.10%)</td><td>2265.09 (-0.18%)</td><td>2203.91 (+1.21%)</td><td>2196.70 (+2.03%)</td><td>2154.97 (+1.42%)</td><td>48.03 (-16.37%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>3.32 (n/a)</td><td>3.19 (n/a)</td><td>3.15 (n/a)</td><td>3.11 (n/a)</td><td>0.08 (n/a)</td><td>8085.40 (n/a)</td><td>7894.12 (n/a)</td><td>7979.40 (n/a)</td><td>7571.20 (n/a)</td><td>204.17 (n/a)</td><td>2269.12 (n/a)</td><td>2177.48 (n/a)</td><td>2153.03 (n/a)</td><td>2124.81 (n/a)</td><td>57.43 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>4.12 (-0.51%)</td><td>3.52 (+0.29%)</td><td>3.55 (+5.86%)</td><td>2.93 (-8.87%)</td><td>0.42 (+15.49%)</td><td>2751.90 (+9.74%)</td><td>2320.34 (+0.10%)</td><td>2271.40 (-5.54%)</td><td>1957.20 (+0.51%)</td><td>284.56 <b>(+30.68%)</b></td><td>1080.08 (-0.51%)</td><td>921.84 (+0.29%)</td><td>930.66 (+5.86%)</td><td>768.16 (-8.87%)</td><td>111.05 (+15.49%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>4.14 (n/a)</td><td>3.51 (n/a)</td><td>3.35 (n/a)</td><td>3.21 (n/a)</td><td>0.37 (n/a)</td><td>2507.70 (n/a)</td><td>2317.96 (n/a)</td><td>2404.50 (n/a)</td><td>1947.20 (n/a)</td><td>217.75 (n/a)</td><td>1085.64 (n/a)</td><td>919.20 (n/a)</td><td>879.16 (n/a)</td><td>842.97 (n/a)</td><td>96.15 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.35 <b>(-39.79%)</b></td><td>0.33 (-14.78%)</td><td>0.33 (+7.34%)</td><td>0.31 (+14.19%)</td><td>0.01 <b>(-89.19%)</b></td><td>4012.10 (-12.43%)</td><td>3805.94 (+7.45%)</td><td>3806.00 (-6.84%)</td><td>3575.90 <b>(+66.10%)</b></td><td>169.13 <b>(-84.42%)</b></td><td>18.77 <b>(-39.79%)</b></td><td>17.66 (-14.78%)</td><td>17.63 (+7.34%)</td><td>16.73 (+14.19%)</td><td>0.79 <b>(-89.19%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.58 (n/a)</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.14 (n/a)</td><td>4581.50 (n/a)</td><td>3542.06 (n/a)</td><td>4085.50 (n/a)</td><td>2152.90 (n/a)</td><td>1085.25 (n/a)</td><td>31.17 (n/a)</td><td>20.72 (n/a)</td><td>16.43 (n/a)</td><td>14.65 (n/a)</td><td>7.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>6.71 (+4.20%)</td><td>4.90 (+3.22%)</td><td>4.84 (+2.01%)</td><td>3.62 (-0.15%)</td><td>1.13 (+1.70%)</td><td>1838.60 (+0.15%)</td><td>1411.38 (-3.29%)</td><td>1373.40 (-1.98%)</td><td>992.00 (-4.03%)</td><td>302.55 (-4.97%)</td><td>2071.77 (+4.20%)</td><td>1514.35 (+3.22%)</td><td>1496.43 (+2.01%)</td><td>1117.80 (-0.15%)</td><td>348.02 (+1.70%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>6.43 (n/a)</td><td>4.75 (n/a)</td><td>4.75 (n/a)</td><td>3.62 (n/a)</td><td>1.11 (n/a)</td><td>1835.80 (n/a)</td><td>1459.36 (n/a)</td><td>1401.10 (n/a)</td><td>1033.70 (n/a)</td><td>318.36 (n/a)</td><td>1988.19 (n/a)</td><td>1467.08 (n/a)</td><td>1466.90 (n/a)</td><td>1119.53 (n/a)</td><td>342.21 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>13.26 (n/a)</td><td>11.57 (n/a)</td><td>11.20 (n/a)</td><td>10.80 (n/a)</td><td>0.97 (n/a)</td><td>13.25 (n/a)</td><td>11.56 (n/a)</td><td>11.19 (n/a)</td><td>10.79 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>25.00 (-0.42%)</td><td>24.34 (+0.12%)</td><td>24.15 (-2.14%)</td><td>23.62 (+5.06%)</td><td>0.56 <b>(-47.44%)</b></td><td>24.98 (-0.42%)</td><td>24.33 (+0.12%)</td><td>24.14 (-2.14%)</td><td>23.61 (+5.06%)</td><td>0.56 <b>(-47.44%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>25.10 (n/a)</td><td>24.31 (n/a)</td><td>24.68 (n/a)</td><td>22.49 (n/a)</td><td>1.07 (n/a)</td><td>25.09 (n/a)</td><td>24.30 (n/a)</td><td>24.67 (n/a)</td><td>22.47 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>40.13 (-6.43%)</td><td>39.05 (-0.76%)</td><td>39.48 (-2.58%)</td><td>36.97 (+7.85%)</td><td>1.32 <b>(-59.49%)</b></td><td>40.10 (-6.43%)</td><td>39.02 (-0.76%)</td><td>39.46 (-2.58%)</td><td>36.95 (+7.85%)</td><td>1.32 <b>(-59.49%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>42.89 (n/a)</td><td>39.35 (n/a)</td><td>40.53 (n/a)</td><td>34.28 (n/a)</td><td>3.25 (n/a)</td><td>42.86 (n/a)</td><td>39.32 (n/a)</td><td>40.50 (n/a)</td><td>34.26 (n/a)</td><td>3.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>45.55 (+0.27%)</td><td>42.99 (-0.97%)</td><td>42.74 (-4.37%)</td><td>39.77 (+4.39%)</td><td>2.45 (-18.69%)</td><td>45.52 (+0.27%)</td><td>42.96 (-0.97%)</td><td>42.71 (-4.37%)</td><td>39.74 (+4.39%)</td><td>2.45 (-18.69%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>45.43 (n/a)</td><td>43.41 (n/a)</td><td>44.69 (n/a)</td><td>38.10 (n/a)</td><td>3.01 (n/a)</td><td>45.40 (n/a)</td><td>43.38 (n/a)</td><td>44.66 (n/a)</td><td>38.07 (n/a)</td><td>3.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>13.40 (n/a)</td><td>12.54 (n/a)</td><td>13.04 (n/a)</td><td>11.13 (n/a)</td><td>0.97 (n/a)</td><td>13.40 (n/a)</td><td>12.53 (n/a)</td><td>13.03 (n/a)</td><td>11.12 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>24.96 (+1.08%)</td><td>24.27 (+1.73%)</td><td>24.17 (+0.27%)</td><td>23.70 (+7.05%)</td><td>0.57 <b>(-44.15%)</b></td><td>24.95 (+1.08%)</td><td>24.26 (+1.73%)</td><td>24.15 (+0.27%)</td><td>23.69 (+7.05%)</td><td>0.57 <b>(-44.15%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>24.70 (n/a)</td><td>23.86 (n/a)</td><td>24.10 (n/a)</td><td>22.14 (n/a)</td><td>1.02 (n/a)</td><td>24.68 (n/a)</td><td>23.84 (n/a)</td><td>24.09 (n/a)</td><td>22.13 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>42.04 (-2.62%)</td><td>38.88 (+0.18%)</td><td>39.93 (-1.71%)</td><td>32.73 (-4.19%)</td><td>3.58 (-11.62%)</td><td>42.01 (-2.62%)</td><td>38.85 (+0.18%)</td><td>39.91 (-1.71%)</td><td>32.71 (-4.19%)</td><td>3.58 (-11.62%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>43.17 (n/a)</td><td>38.81 (n/a)</td><td>40.63 (n/a)</td><td>34.16 (n/a)</td><td>4.05 (n/a)</td><td>43.14 (n/a)</td><td>38.78 (n/a)</td><td>40.60 (n/a)</td><td>34.14 (n/a)</td><td>4.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>44.93 (-1.53%)</td><td>41.04 (-0.65%)</td><td>42.47 (+1.54%)</td><td>34.07 (+2.05%)</td><td>4.16 (-12.33%)</td><td>44.90 (-1.53%)</td><td>41.01 (-0.65%)</td><td>42.45 (+1.54%)</td><td>34.05 (+2.05%)</td><td>4.15 (-12.33%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>45.63 (n/a)</td><td>41.30 (n/a)</td><td>41.83 (n/a)</td><td>33.39 (n/a)</td><td>4.74 (n/a)</td><td>45.60 (n/a)</td><td>41.28 (n/a)</td><td>41.80 (n/a)</td><td>33.37 (n/a)</td><td>4.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>9.05 (+4.76%)</td><td>8.83 (+6.80%)</td><td>8.87 (+8.87%)</td><td>8.62 (+8.65%)</td><td>0.17 <b>(-43.42%)</b></td><td>9.03 (+4.76%)</td><td>8.81 (+6.80%)</td><td>8.85 (+8.87%)</td><td>8.60 (+8.65%)</td><td>0.17 <b>(-43.42%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>8.64 (n/a)</td><td>8.26 (n/a)</td><td>8.15 (n/a)</td><td>7.93 (n/a)</td><td>0.30 (n/a)</td><td>8.62 (n/a)</td><td>8.25 (n/a)</td><td>8.13 (n/a)</td><td>7.91 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.87 (+2.45%)</td><td>0.78 (+2.92%)</td><td>0.78 (+2.24%)</td><td>0.68 (+1.37%)</td><td>0.07 (+9.50%)</td><td>0.86 (+2.45%)</td><td>0.77 (+2.92%)</td><td>0.76 (+2.24%)</td><td>0.67 (+1.37%)</td><td>0.07 (+9.50%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.85 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.67 (n/a)</td><td>0.07 (n/a)</td><td>0.84 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.66 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>1.06 (-9.32%)</td><td>1.03 (-1.13%)</td><td>1.03 (+0.58%)</td><td>0.97 (+3.13%)</td><td>0.04 <b>(-56.94%)</b></td><td>1.05 (-9.32%)</td><td>1.01 (-1.13%)</td><td>1.02 (+0.58%)</td><td>0.96 (+3.13%)</td><td>0.04 <b>(-56.94%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>1.17 (n/a)</td><td>1.04 (n/a)</td><td>1.02 (n/a)</td><td>0.95 (n/a)</td><td>0.09 (n/a)</td><td>1.16 (n/a)</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>0.93 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>16.09 (-0.45%)</td><td>14.93 (+1.23%)</td><td>14.96 (+1.12%)</td><td>14.02 (+8.60%)</td><td>0.76 <b>(-40.22%)</b></td><td>15.91 (-0.45%)</td><td>14.75 (+1.23%)</td><td>14.79 (+1.12%)</td><td>13.86 (+8.60%)</td><td>0.76 <b>(-40.22%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>16.17 (n/a)</td><td>14.75 (n/a)</td><td>14.80 (n/a)</td><td>12.91 (n/a)</td><td>1.28 (n/a)</td><td>15.98 (n/a)</td><td>14.58 (n/a)</td><td>14.63 (n/a)</td><td>12.76 (n/a)</td><td>1.26 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>11.98 (+1.47%)</td><td>11.37 (+6.12%)</td><td>11.81 (+3.85%)</td><td>9.41 <b>(+27.31%)</b></td><td>1.10 <b>(-41.13%)</b></td><td>11.77 (+1.47%)</td><td>11.17 (+6.12%)</td><td>11.60 (+3.85%)</td><td>9.25 <b>(+27.31%)</b></td><td>1.08 <b>(-41.13%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>11.80 (n/a)</td><td>10.72 (n/a)</td><td>11.37 (n/a)</td><td>7.39 (n/a)</td><td>1.87 (n/a)</td><td>11.60 (n/a)</td><td>10.53 (n/a)</td><td>11.17 (n/a)</td><td>7.26 (n/a)</td><td>1.84 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>9.15 (+14.20%)</td><td>7.77 (+4.42%)</td><td>7.46 (+0.76%)</td><td>6.70 (-2.68%)</td><td>0.92 <b>(+112.71%)</b></td><td>8.99 (+14.20%)</td><td>7.64 (+4.42%)</td><td>7.33 (+0.76%)</td><td>6.58 (-2.68%)</td><td>0.90 <b>(+112.71%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>8.01 (n/a)</td><td>7.44 (n/a)</td><td>7.40 (n/a)</td><td>6.88 (n/a)</td><td>0.43 (n/a)</td><td>7.88 (n/a)</td><td>7.31 (n/a)</td><td>7.28 (n/a)</td><td>6.76 (n/a)</td><td>0.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>6.95 (+3.78%)</td><td>6.02 (+15.54%)</td><td>6.03 <b>(+21.05%)</b></td><td>5.41 <b>(+26.70%)</b></td><td>0.60 <b>(-33.96%)</b></td><td>6.83 (+3.78%)</td><td>5.93 (+15.54%)</td><td>5.93 <b>(+21.05%)</b></td><td>5.32 <b>(+26.70%)</b></td><td>0.59 <b>(-33.96%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>6.69 (n/a)</td><td>5.21 (n/a)</td><td>4.98 (n/a)</td><td>4.27 (n/a)</td><td>0.91 (n/a)</td><td>6.59 (n/a)</td><td>5.13 (n/a)</td><td>4.90 (n/a)</td><td>4.20 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>13.29 (n/a)</td><td>12.73 (n/a)</td><td>12.70 (n/a)</td><td>11.79 (n/a)</td><td>0.62 (n/a)</td><td>13.28 (n/a)</td><td>12.72 (n/a)</td><td>12.69 (n/a)</td><td>11.78 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>13.45 (n/a)</td><td>12.98 (n/a)</td><td>13.04 (n/a)</td><td>12.27 (n/a)</td><td>0.43 (n/a)</td><td>13.45 (n/a)</td><td>12.98 (n/a)</td><td>13.03 (n/a)</td><td>12.27 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>158.68 (n/a)</td><td>147.90 (n/a)</td><td>137.60 (n/a)</td><td>27.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.50 (n/a)</td><td>194.52 (n/a)</td><td>179.00 (n/a)</td><td>149.20 (n/a)</td><td>56.21 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.90 (n/a)</td><td>165.62 (n/a)</td><td>171.00 (n/a)</td><td>142.50 (n/a)</td><td>19.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.00 (n/a)</td><td>189.04 (n/a)</td><td>178.70 (n/a)</td><td>171.20 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>175.04 (n/a)</td><td>181.20 (n/a)</td><td>140.30 (n/a)</td><td>20.31 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.90 (n/a)</td><td>194.88 (n/a)</td><td>190.70 (n/a)</td><td>162.90 (n/a)</td><td>30.48 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>287.80 (n/a)</td><td>211.00 (n/a)</td><td>188.70 (n/a)</td><td>179.70 (n/a)</td><td>44.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>287.00 (n/a)</td><td>219.88 (n/a)</td><td>203.50 (n/a)</td><td>198.70 (n/a)</td><td>37.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.08 (+0.96%)</td><td>0.05 (-7.20%)</td><td>0.05 (-19.48%)</td><td>0.04 (+14.69%)</td><td>0.01 (-3.17%)</td><td>182.70 (-12.83%)</td><td>160.34 (+6.54%)</td><td>174.60 <b>(+24.18%)</b></td><td>103.20 (-0.96%)</td><td>32.73 (-19.42%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>209.60 (n/a)</td><td>150.50 (n/a)</td><td>140.60 (n/a)</td><td>104.20 (n/a)</td><td>40.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (+10.02%)</td><td>0.05 (+10.38%)</td><td>0.05 <b>(+20.14%)</b></td><td>0.03 (-10.73%)</td><td>0.01 <b>(+81.68%)</b></td><td>234.50 (+12.04%)</td><td>174.58 (-7.55%)</td><td>156.30 (-16.73%)</td><td>149.00 (-9.15%)</td><td>36.03 <b>(+82.18%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.30 (n/a)</td><td>188.84 (n/a)</td><td>187.70 (n/a)</td><td>164.00 (n/a)</td><td>19.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (-5.38%)</td><td>0.05 (+18.17%)</td><td>0.06 <b>(+31.73%)</b></td><td>0.05 <b>(+37.03%)</b></td><td>0.01 <b>(-49.13%)</b></td><td>167.70 <b>(-27.02%)</b></td><td>150.60 (-17.83%)</td><td>143.20 <b>(-24.11%)</b></td><td>135.90 (+5.68%)</td><td>15.29 <b>(-59.01%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>183.28 (n/a)</td><td>188.70 (n/a)</td><td>128.60 (n/a)</td><td>37.30 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (-8.65%)</td><td>0.05 (-4.38%)</td><td>0.05 (+9.26%)</td><td>0.03 <b>(-33.08%)</b></td><td>0.01 <b>(+65.77%)</b></td><td>315.60 <b>(+49.43%)</b></td><td>194.98 (+10.48%)</td><td>164.20 (-8.47%)</td><td>156.90 (+9.49%)</td><td>68.10 <b>(+178.27%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>176.48 (n/a)</td><td>179.40 (n/a)</td><td>143.30 (n/a)</td><td>24.47 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 <b>(+60.33%)</b></td><td>0.05 <b>(+44.97%)</b></td><td>0.05 <b>(+36.88%)</b></td><td>0.04 <b>(+61.20%)</b></td><td>0.01 <b>(+57.76%)</b></td><td>187.60 <b>(-37.98%)</b></td><td>162.30 <b>(-31.14%)</b></td><td>167.60 <b>(-26.97%)</b></td><td>121.20 <b>(-37.65%)</b></td><td>25.24 <b>(-40.90%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>302.50 (n/a)</td><td>235.70 (n/a)</td><td>229.50 (n/a)</td><td>194.40 (n/a)</td><td>42.71 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 <b>(+37.34%)</b></td><td>0.05 <b>(+23.13%)</b></td><td>0.05 <b>(+23.92%)</b></td><td>0.04 (+8.83%)</td><td>0.01 <b>(+201.45%)</b></td><td>212.20 (-8.10%)</td><td>169.94 (-16.50%)</td><td>158.20 (-19.33%)</td><td>136.90 <b>(-27.18%)</b></td><td>35.19 <b>(+101.70%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>230.90 (n/a)</td><td>203.52 (n/a)</td><td>196.10 (n/a)</td><td>188.00 (n/a)</td><td>17.45 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (+10.47%)</td><td>0.05 (+15.12%)</td><td>0.05 <b>(+33.25%)</b></td><td>0.04 (+10.13%)</td><td>0.01 <b>(+25.82%)</b></td><td>224.20 (-9.19%)</td><td>184.94 (-12.39%)</td><td>165.90 <b>(-24.97%)</b></td><td>145.40 (-9.46%)</td><td>36.56 (+10.44%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.90 (n/a)</td><td>211.10 (n/a)</td><td>221.10 (n/a)</td><td>160.60 (n/a)</td><td>33.11 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 <b>(+26.52%)</b></td><td>0.05 <b>(+24.48%)</b></td><td>0.05 (+15.21%)</td><td>0.04 <b>(+59.02%)</b></td><td>0.01 <b>(-26.42%)</b></td><td>198.40 <b>(-37.12%)</b></td><td>178.86 <b>(-22.00%)</b></td><td>180.20 (-13.24%)</td><td>146.50 <b>(-20.94%)</b></td><td>20.04 <b>(-63.48%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>315.50 (n/a)</td><td>229.30 (n/a)</td><td>207.70 (n/a)</td><td>185.30 (n/a)</td><td>54.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (+9.33%)</td><td>0.05 (+14.11%)</td><td>0.05 (+13.27%)</td><td>0.04 <b>(+21.22%)</b></td><td>0.00 <b>(-21.79%)</b></td><td>182.80 (-17.47%)</td><td>170.14 (-12.95%)</td><td>178.30 (-11.73%)</td><td>153.50 (-8.52%)</td><td>14.51 <b>(-40.60%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>195.46 (n/a)</td><td>202.00 (n/a)</td><td>167.80 (n/a)</td><td>24.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (+6.91%)</td><td>0.04 (-3.00%)</td><td>0.04 (+8.84%)</td><td>0.03 (-19.70%)</td><td>0.01 <b>(+93.84%)</b></td><td>315.00 <b>(+24.56%)</b></td><td>238.72 (+6.77%)</td><td>214.30 (-8.14%)</td><td>178.80 (-6.49%)</td><td>58.04 <b>(+132.05%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>252.90 (n/a)</td><td>223.58 (n/a)</td><td>233.30 (n/a)</td><td>191.20 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (-4.99%)</td><td>0.05 (-16.71%)</td><td>0.05 <b>(-24.25%)</b></td><td>0.04 (-17.91%)</td><td>0.01 (+19.25%)</td><td>194.70 <b>(+21.84%)</b></td><td>167.06 <b>(+21.45%)</b></td><td>171.70 <b>(+31.98%)</b></td><td>120.30 (+5.25%)</td><td>28.31 <b>(+44.17%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>159.80 (n/a)</td><td>137.56 (n/a)</td><td>130.10 (n/a)</td><td>114.30 (n/a)</td><td>19.63 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (-17.67%)</td><td>0.04 (-13.31%)</td><td>0.04 (-5.77%)</td><td>0.03 (-18.39%)</td><td>0.00 <b>(-24.73%)</b></td><td>256.10 <b>(+22.54%)</b></td><td>220.80 (+15.14%)</td><td>218.00 (+6.13%)</td><td>193.60 <b>(+21.46%)</b></td><td>24.54 (+10.74%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.00 (n/a)</td><td>191.76 (n/a)</td><td>205.40 (n/a)</td><td>159.40 (n/a)</td><td>22.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (+4.77%)</td><td>0.05 (-13.28%)</td><td>0.05 (-12.67%)</td><td>0.03 <b>(-20.46%)</b></td><td>0.01 <b>(+37.32%)</b></td><td>259.80 <b>(+25.69%)</b></td><td>180.32 (+19.77%)</td><td>155.20 (+14.54%)</td><td>122.70 (-4.59%)</td><td>54.68 <b>(+66.89%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.70 (n/a)</td><td>150.56 (n/a)</td><td>135.50 (n/a)</td><td>128.60 (n/a)</td><td>32.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (+9.39%)</td><td>0.06 (+13.90%)</td><td>0.06 (+10.37%)</td><td>0.05 (+17.57%)</td><td>0.01 (-0.42%)</td><td>169.60 (-14.94%)</td><td>144.18 (-12.67%)</td><td>142.80 (-9.39%)</td><td>118.90 (-8.54%)</td><td>21.64 <b>(-23.35%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>165.10 (n/a)</td><td>157.60 (n/a)</td><td>130.00 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (-0.92%)</td><td>0.05 (-2.87%)</td><td>0.05 (-12.92%)</td><td>0.04 (+13.34%)</td><td>0.01 <b>(-30.46%)</b></td><td>193.20 (-11.78%)</td><td>167.22 (+1.31%)</td><td>172.20 (+14.88%)</td><td>139.50 (+0.94%)</td><td>20.05 <b>(-39.22%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>165.06 (n/a)</td><td>149.90 (n/a)</td><td>138.20 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (+8.05%)</td><td>0.05 (+12.12%)</td><td>0.05 (+3.32%)</td><td>0.04 <b>(+69.73%)</b></td><td>0.01 <b>(-35.99%)</b></td><td>211.40 <b>(-41.08%)</b></td><td>173.38 (-17.00%)</td><td>168.10 (-3.22%)</td><td>141.40 (-7.40%)</td><td>27.66 <b>(-67.32%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>358.80 (n/a)</td><td>208.88 (n/a)</td><td>173.70 (n/a)</td><td>152.70 (n/a)</td><td>84.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (+11.24%)</td><td>0.04 (-3.65%)</td><td>0.04 (-3.50%)</td><td>0.04 (-11.26%)</td><td>0.01 <b>(+69.45%)</b></td><td>224.50 (+12.70%)</td><td>192.74 (+5.85%)</td><td>200.60 (+3.67%)</td><td>137.40 (-10.08%)</td><td>34.53 <b>(+66.97%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>182.08 (n/a)</td><td>193.50 (n/a)</td><td>152.80 (n/a)</td><td>20.68 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (+2.21%)</td><td>0.04 (+3.36%)</td><td>0.04 (-2.09%)</td><td>0.04 <b>(+34.90%)</b></td><td>0.01 <b>(-42.35%)</b></td><td>214.30 <b>(-25.87%)</b></td><td>185.72 (-6.53%)</td><td>182.50 (+2.13%)</td><td>156.60 (-2.19%)</td><td>21.43 <b>(-59.29%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>289.10 (n/a)</td><td>198.70 (n/a)</td><td>178.70 (n/a)</td><td>160.10 (n/a)</td><td>52.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.21 (+0.82%)</td><td>0.21 (+0.22%)</td><td>0.21 (+0.00%)</td><td>0.21 (+0.09%)</td><td>0.00 <b>(+233.65%)</b></td><td>40891.30 (-0.09%)</td><td>40753.60 (-0.22%)</td><td>40821.50 (-0.00%)</td><td>40461.90 (-0.81%)</td><td>170.90 <b>(+230.36%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40928.50 (n/a)</td><td>40842.10 (n/a)</td><td>40822.60 (n/a)</td><td>40793.60 (n/a)</td><td>51.73 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (-8.13%)</td><td>0.05 (-15.38%)</td><td>0.05 <b>(-24.32%)</b></td><td>0.03 <b>(-26.50%)</b></td><td>0.01 (+7.55%)</td><td>245.60 <b>(+36.07%)</b></td><td>172.24 <b>(+20.58%)</b></td><td>171.20 <b>(+32.10%)</b></td><td>127.30 (+8.80%)</td><td>45.58 <b>(+61.39%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.50 (n/a)</td><td>142.84 (n/a)</td><td>129.60 (n/a)</td><td>117.00 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.09 (+2.56%)</td><td>0.08 (+9.29%)</td><td>0.08 (+12.58%)</td><td>0.06 (+8.99%)</td><td>0.01 (+2.39%)</td><td>193.70 (-8.24%)</td><td>160.52 (-8.59%)</td><td>151.70 (-11.18%)</td><td>144.30 (-2.50%)</td><td>20.60 (-9.62%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>175.60 (n/a)</td><td>170.80 (n/a)</td><td>148.00 (n/a)</td><td>22.79 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (-3.72%)</td><td>0.05 (-11.64%)</td><td>0.05 (+8.10%)</td><td>0.03 <b>(-39.76%)</b></td><td>0.01 <b>(+55.97%)</b></td><td>291.60 <b>(+66.06%)</b></td><td>188.52 <b>(+20.71%)</b></td><td>159.80 (-7.52%)</td><td>130.60 (+3.82%)</td><td>66.42 <b>(+166.84%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.60 (n/a)</td><td>156.18 (n/a)</td><td>172.80 (n/a)</td><td>125.80 (n/a)</td><td>24.89 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (-0.16%)</td><td>0.05 (+0.92%)</td><td>0.06 (+2.36%)</td><td>0.04 <b>(+45.34%)</b></td><td>0.01 <b>(-29.35%)</b></td><td>256.20 <b>(-31.20%)</b></td><td>194.60 (-7.72%)</td><td>183.30 (-2.29%)</td><td>146.50 (+0.14%)</td><td>42.52 <b>(-53.81%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>372.40 (n/a)</td><td>210.88 (n/a)</td><td>187.60 (n/a)</td><td>146.30 (n/a)</td><td>92.06 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (-18.89%)</td><td>0.05 (-16.38%)</td><td>0.04 (-16.71%)</td><td>0.03 <b>(-26.71%)</b></td><td>0.01 (-4.98%)</td><td>244.10 <b>(+36.44%)</b></td><td>185.94 <b>(+20.77%)</b></td><td>184.30 (+19.99%)</td><td>148.70 <b>(+23.30%)</b></td><td>36.00 <b>(+66.59%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.90 (n/a)</td><td>153.96 (n/a)</td><td>153.60 (n/a)</td><td>120.60 (n/a)</td><td>21.61 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.08 (+2.82%)</td><td>0.06 (-2.16%)</td><td>0.06 (+2.07%)</td><td>0.05 (-2.81%)</td><td>0.01 (-4.38%)</td><td>213.70 (+2.89%)</td><td>170.74 (+1.86%)</td><td>176.40 (-2.05%)</td><td>123.20 (-2.69%)</td><td>33.19 (-4.65%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.70 (n/a)</td><td>167.62 (n/a)</td><td>180.10 (n/a)</td><td>126.60 (n/a)</td><td>34.81 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (-3.41%)</td><td>0.04 (-7.60%)</td><td>0.04 (-7.37%)</td><td>0.04 (-4.29%)</td><td>0.00 (-9.63%)</td><td>206.00 (+4.52%)</td><td>185.34 (+8.11%)</td><td>190.50 (+7.99%)</td><td>155.00 (+3.54%)</td><td>18.85 (-2.91%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>171.44 (n/a)</td><td>176.40 (n/a)</td><td>149.70 (n/a)</td><td>19.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 <b>(+25.60%)</b></td><td>0.05 (+14.89%)</td><td>0.05 (+1.89%)</td><td>0.05 <b>(+21.34%)</b></td><td>0.01 <b>(+61.61%)</b></td><td>194.80 (-17.60%)</td><td>173.56 (-12.40%)</td><td>187.40 (-1.83%)</td><td>142.00 <b>(-20.40%)</b></td><td>23.61 (+4.51%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>236.40 (n/a)</td><td>198.12 (n/a)</td><td>190.90 (n/a)</td><td>178.40 (n/a)</td><td>22.59 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (+2.12%)</td><td>0.04 (-9.80%)</td><td>0.04 (-12.55%)</td><td>0.03 <b>(-21.45%)</b></td><td>0.01 <b>(+23.80%)</b></td><td>260.90 <b>(+27.27%)</b></td><td>197.42 (+12.64%)</td><td>190.90 (+14.31%)</td><td>144.60 (-2.10%)</td><td>41.89 <b>(+51.42%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>175.26 (n/a)</td><td>167.00 (n/a)</td><td>147.70 (n/a)</td><td>27.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 <b>(+22.27%)</b></td><td>0.05 (+11.59%)</td><td>0.06 (+15.42%)</td><td>0.03 (-15.15%)</td><td>0.01 <b>(+120.41%)</b></td><td>282.40 (+17.86%)</td><td>186.60 (-6.00%)</td><td>161.90 (-13.38%)</td><td>145.00 (-18.22%)</td><td>57.27 <b>(+114.75%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.60 (n/a)</td><td>198.52 (n/a)</td><td>186.90 (n/a)</td><td>177.30 (n/a)</td><td>26.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (-10.14%)</td><td>0.04 (-14.77%)</td><td>0.04 (-8.38%)</td><td>0.03 <b>(-30.32%)</b></td><td>0.01 <b>(+55.58%)</b></td><td>271.60 <b>(+43.55%)</b></td><td>208.86 <b>(+20.26%)</b></td><td>192.30 (+9.14%)</td><td>162.70 (+11.29%)</td><td>43.69 <b>(+152.81%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>173.68 (n/a)</td><td>176.20 (n/a)</td><td>146.20 (n/a)</td><td>17.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (-6.64%)</td><td>0.04 (-4.94%)</td><td>0.04 (-5.70%)</td><td>0.03 (-1.92%)</td><td>0.00 (-19.53%)</td><td>258.30 (+1.93%)</td><td>216.28 (+4.79%)</td><td>210.10 (+6.06%)</td><td>194.60 (+7.10%)</td><td>24.50 (-11.99%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.40 (n/a)</td><td>206.40 (n/a)</td><td>198.10 (n/a)</td><td>181.70 (n/a)</td><td>27.83 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (+6.37%)</td><td>0.04 (+1.38%)</td><td>0.04 (-6.25%)</td><td>0.04 <b>(+33.07%)</b></td><td>0.01 <b>(-24.86%)</b></td><td>219.20 <b>(-24.83%)</b></td><td>188.76 (-4.05%)</td><td>184.30 (+6.66%)</td><td>153.10 (-5.96%)</td><td>28.59 <b>(-47.04%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>291.60 (n/a)</td><td>196.72 (n/a)</td><td>172.80 (n/a)</td><td>162.80 (n/a)</td><td>53.97 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (-9.50%)</td><td>0.04 (+2.55%)</td><td>0.04 (+12.87%)</td><td>0.03 (+2.00%)</td><td>0.01 <b>(-30.56%)</b></td><td>251.60 (-1.95%)</td><td>202.24 (-4.14%)</td><td>197.70 (-11.39%)</td><td>161.00 (+10.50%)</td><td>32.79 <b>(-21.91%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>256.60 (n/a)</td><td>210.98 (n/a)</td><td>223.10 (n/a)</td><td>145.70 (n/a)</td><td>41.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (+6.49%)</td><td>0.04 (-4.11%)</td><td>0.04 (+1.01%)</td><td>0.02 <b>(-41.78%)</b></td><td>0.01 <b>(+347.35%)</b></td><td>388.40 <b>(+71.78%)</b></td><td>235.56 (+12.33%)</td><td>208.10 (-1.00%)</td><td>182.50 (-6.12%)</td><td>86.26 <b>(+655.51%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>226.10 (n/a)</td><td>209.70 (n/a)</td><td>210.20 (n/a)</td><td>194.40 (n/a)</td><td>11.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.70 (+1.12%)</td><td>0.53 (-16.22%)</td><td>0.51 <b>(-22.54%)</b></td><td>0.38 <b>(-24.83%)</b></td><td>0.12 <b>(+59.57%)</b></td><td>261.80 <b>(+33.03%)</b></td><td>194.92 <b>(+22.84%)</b></td><td>192.90 <b>(+29.12%)</b></td><td>140.50 (-1.13%)</td><td>45.00 <b>(+105.18%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.69 (n/a)</td><td>0.63 (n/a)</td><td>0.66 (n/a)</td><td>0.50 (n/a)</td><td>0.08 (n/a)</td><td>196.80 (n/a)</td><td>158.68 (n/a)</td><td>149.40 (n/a)</td><td>142.10 (n/a)</td><td>21.93 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.80 <b>(+26.61%)</b></td><td>0.63 (+19.53%)</td><td>0.65 <b>(+31.15%)</b></td><td>0.49 (+9.51%)</td><td>0.11 <b>(+43.13%)</b></td><td>199.40 (-8.66%)</td><td>158.90 (-15.65%)</td><td>150.80 <b>(-23.76%)</b></td><td>123.00 <b>(-21.00%)</b></td><td>28.33 (+4.74%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.63 (n/a)</td><td>0.53 (n/a)</td><td>0.50 (n/a)</td><td>0.45 (n/a)</td><td>0.08 (n/a)</td><td>218.30 (n/a)</td><td>188.38 (n/a)</td><td>197.80 (n/a)</td><td>155.70 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.57 (-12.33%)</td><td>0.48 (-16.07%)</td><td>0.51 (-15.14%)</td><td>0.30 <b>(-37.95%)</b></td><td>0.11 <b>(+39.58%)</b></td><td>330.60 <b>(+61.11%)</b></td><td>218.26 <b>(+24.10%)</b></td><td>193.00 (+17.83%)</td><td>171.50 (+14.03%)</td><td>65.74 <b>(+154.67%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.65 (n/a)</td><td>0.57 (n/a)</td><td>0.60 (n/a)</td><td>0.48 (n/a)</td><td>0.08 (n/a)</td><td>205.20 (n/a)</td><td>175.88 (n/a)</td><td>163.80 (n/a)</td><td>150.40 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.64 (-12.30%)</td><td>0.55 (-0.78%)</td><td>0.52 (-3.00%)</td><td>0.49 (+16.52%)</td><td>0.06 <b>(-50.72%)</b></td><td>200.10 (-14.16%)</td><td>181.50 (-1.99%)</td><td>189.20 (+3.11%)</td><td>153.20 (+14.07%)</td><td>18.48 <b>(-52.14%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.73 (n/a)</td><td>0.55 (n/a)</td><td>0.54 (n/a)</td><td>0.42 (n/a)</td><td>0.12 (n/a)</td><td>233.10 (n/a)</td><td>185.18 (n/a)</td><td>183.50 (n/a)</td><td>134.30 (n/a)</td><td>38.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.54 (-13.53%)</td><td>0.48 (-3.17%)</td><td>0.49 (-10.54%)</td><td>0.38 <b>(+23.56%)</b></td><td>0.06 <b>(-50.49%)</b></td><td>195.30 (-19.06%)</td><td>155.68 (-1.59%)</td><td>149.10 (+11.85%)</td><td>136.80 (+15.64%)</td><td>22.94 <b>(-53.68%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.62 (n/a)</td><td>0.50 (n/a)</td><td>0.55 (n/a)</td><td>0.31 (n/a)</td><td>0.12 (n/a)</td><td>241.30 (n/a)</td><td>158.20 (n/a)</td><td>133.30 (n/a)</td><td>118.30 (n/a)</td><td>49.53 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.50 (-14.44%)</td><td>0.43 (+1.88%)</td><td>0.43 (-2.19%)</td><td>0.36 <b>(+48.01%)</b></td><td>0.05 <b>(-59.83%)</b></td><td>203.00 <b>(-32.45%)</b></td><td>173.24 (-8.60%)</td><td>171.60 (+2.26%)</td><td>146.60 (+16.91%)</td><td>20.09 <b>(-69.72%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.59 (n/a)</td><td>0.42 (n/a)</td><td>0.44 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>300.50 (n/a)</td><td>189.54 (n/a)</td><td>167.80 (n/a)</td><td>125.40 (n/a)</td><td>66.36 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.46 (-19.87%)</td><td>0.41 (-3.60%)</td><td>0.40 (+0.98%)</td><td>0.37 <b>(+32.96%)</b></td><td>0.04 <b>(-64.24%)</b></td><td>200.50 <b>(-24.79%)</b></td><td>183.00 (-1.77%)</td><td>183.70 (-0.97%)</td><td>159.40 <b>(+24.82%)</b></td><td>18.14 <b>(-65.89%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.58 (n/a)</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.12 (n/a)</td><td>266.60 (n/a)</td><td>186.30 (n/a)</td><td>185.50 (n/a)</td><td>127.70 (n/a)</td><td>53.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.48 (-15.68%)</td><td>0.41 (-3.70%)</td><td>0.42 (+16.65%)</td><td>0.32 (-4.46%)</td><td>0.06 <b>(-43.73%)</b></td><td>233.90 (+4.65%)</td><td>182.94 (+0.57%)</td><td>175.20 (-14.29%)</td><td>154.10 (+18.63%)</td><td>31.71 <b>(-28.90%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.57 (n/a)</td><td>0.43 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.11 (n/a)</td><td>223.50 (n/a)</td><td>181.90 (n/a)</td><td>204.40 (n/a)</td><td>129.90 (n/a)</td><td>44.60 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>1.18 <b>(+61.91%)</b></td><td>0.87 <b>(+28.68%)</b></td><td>0.91 <b>(+27.40%)</b></td><td>0.54 (-9.86%)</td><td>0.23 <b>(+262.05%)</b></td><td>244.50 (+10.93%)</td><td>161.30 (-17.59%)</td><td>144.70 <b>(-21.53%)</b></td><td>111.50 <b>(-38.23%)</b></td><td>50.21 <b>(+160.51%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.73 (n/a)</td><td>0.67 (n/a)</td><td>0.71 (n/a)</td><td>0.59 (n/a)</td><td>0.06 (n/a)</td><td>220.40 (n/a)</td><td>195.72 (n/a)</td><td>184.40 (n/a)</td><td>180.50 (n/a)</td><td>19.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.94 (+6.73%)</td><td>0.80 (+1.18%)</td><td>0.81 (+3.93%)</td><td>0.70 (-0.69%)</td><td>0.10 <b>(+48.53%)</b></td><td>187.50 (+0.70%)</td><td>165.66 (-0.56%)</td><td>162.00 (-3.80%)</td><td>140.00 (-6.29%)</td><td>19.80 <b>(+42.37%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.88 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.70 (n/a)</td><td>0.07 (n/a)</td><td>186.20 (n/a)</td><td>166.60 (n/a)</td><td>168.40 (n/a)</td><td>149.40 (n/a)</td><td>13.91 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.89 (+3.67%)</td><td>0.85 (+11.04%)</td><td>0.88 (+15.01%)</td><td>0.75 (+8.13%)</td><td>0.06 (-6.61%)</td><td>174.60 (-7.52%)</td><td>155.50 (-10.02%)</td><td>149.60 (-13.02%)</td><td>147.20 (-3.54%)</td><td>11.35 (-15.71%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.86 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.69 (n/a)</td><td>0.06 (n/a)</td><td>188.80 (n/a)</td><td>172.82 (n/a)</td><td>172.00 (n/a)</td><td>152.60 (n/a)</td><td>13.46 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-2.27%)</td><td>0.00 (+4.88%)</td><td>0.00 <b>(-65.70%)</b></td><td>959.94 (-3.76%)</td><td>951.83 (+0.30%)</td><td>952.30 (+1.19%)</td><td>937.24 (+1.48%)</td><td>8.82 <b>(-69.12%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>997.41 (n/a)</td><td>948.98 (n/a)</td><td>941.07 (n/a)</td><td>923.55 (n/a)</td><td>28.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.01 (-2.41%)</td><td>0.01 (-4.14%)</td><td>0.01 (-1.22%)</td><td>0.01 (-11.11%)</td><td>0.00 <b>(+365.99%)</b></td><td>1137.57 (+12.70%)</td><td>1039.95 (+4.48%)</td><td>1008.51 (+1.38%)</td><td>1005.56 (+2.26%)</td><td>56.44 <b>(+492.58%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1009.34 (n/a)</td><td>995.36 (n/a)</td><td>994.78 (n/a)</td><td>983.33 (n/a)</td><td>9.52 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.94 (-3.41%)</td><td>0.94 (-0.28%)</td><td>0.94 (+0.02%)</td><td>0.94 (+1.81%)</td><td>0.00 <b>(-82.99%)</b></td><td>2240.09 (-1.77%)</td><td>2231.98 (+0.24%)</td><td>2237.30 (-0.01%)</td><td>2219.31 (+3.53%)</td><td>9.46 <b>(-82.75%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.98 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.92 (n/a)</td><td>0.02 (n/a)</td><td>2280.56 (n/a)</td><td>2226.71 (n/a)</td><td>2237.63 (n/a)</td><td>2143.56 (n/a)</td><td>54.85 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.00 (n/a)</td><td>1194.70 (n/a)</td><td>1189.72 (n/a)</td><td>1193.15 (n/a)</td><td>1180.84 (n/a)</td><td>5.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.00 (n/a)</td><td>1423.95 (n/a)</td><td>1405.05 (n/a)</td><td>1406.06 (n/a)</td><td>1388.89 (n/a)</td><td>12.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.01 (n/a)</td><td>1483.66 (n/a)</td><td>1445.36 (n/a)</td><td>1438.13 (n/a)</td><td>1396.89 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>3.39 <b>(+28.45%)</b></td><td>2.62 (+1.74%)</td><td>2.60 (+0.84%)</td><td>1.78 <b>(-29.30%)</b></td><td>0.62 <b>(+1291.21%)</b></td><td>294.10 <b>(+41.46%)</b></td><td>210.16 (+3.25%)</td><td>201.60 (-0.84%)</td><td>154.80 <b>(-22.17%)</b></td><td>54.47 <b>(+1447.69%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>2.64 (n/a)</td><td>2.58 (n/a)</td><td>2.58 (n/a)</td><td>2.52 (n/a)</td><td>0.04 (n/a)</td><td>207.90 (n/a)</td><td>203.54 (n/a)</td><td>203.30 (n/a)</td><td>198.90 (n/a)</td><td>3.52 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>5.69 (+12.02%)</td><td>4.21 (-6.76%)</td><td>4.25 (-3.97%)</td><td>2.64 <b>(-36.56%)</b></td><td>1.13 <b>(+229.99%)</b></td><td>396.60 <b>(+57.63%)</b></td><td>266.00 (+13.98%)</td><td>246.90 (+4.13%)</td><td>184.30 (-10.71%)</td><td>80.77 <b>(+384.37%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>5.08 (n/a)</td><td>4.51 (n/a)</td><td>4.42 (n/a)</td><td>4.17 (n/a)</td><td>0.34 (n/a)</td><td>251.60 (n/a)</td><td>233.38 (n/a)</td><td>237.10 (n/a)</td><td>206.40 (n/a)</td><td>16.68 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>2.95 (+9.05%)</td><td>2.45 (-8.68%)</td><td>2.33 (-13.28%)</td><td>2.22 (-16.64%)</td><td>0.30 <b>(+1427.63%)</b></td><td>236.40 (+19.94%)</td><td>216.50 (+10.72%)</td><td>225.00 (+15.33%)</td><td>177.50 (-8.32%)</td><td>24.23 <b>(+1558.92%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>2.71 (n/a)</td><td>2.68 (n/a)</td><td>2.69 (n/a)</td><td>2.66 (n/a)</td><td>0.02 (n/a)</td><td>197.10 (n/a)</td><td>195.54 (n/a)</td><td>195.10 (n/a)</td><td>193.60 (n/a)</td><td>1.46 (n/a)</td>
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
