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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.09 (-19.90%)</td><td>0.07 (-2.98%)</td><td>0.07 (+7.46%)</td><td>0.07 (+0.97%)</td><td>0.01 <b>(-55.55%)</b></td><td>188.30 (-0.95%)</td><td>167.36 (+0.17%)</td><td>170.20 (-6.94%)</td><td>141.60 <b>(+24.87%)</b></td><td>17.76 <b>(-45.25%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>190.10 (n/a)</td><td>167.08 (n/a)</td><td>182.90 (n/a)</td><td>113.40 (n/a)</td><td>32.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.09 (-5.81%)</td><td>0.07 (-14.74%)</td><td>0.06 <b>(-26.67%)</b></td><td>0.06 (-12.07%)</td><td>0.02 <b>(+39.70%)</b></td><td>210.10 (+13.69%)</td><td>175.76 (+19.96%)</td><td>195.60 <b>(+36.31%)</b></td><td>132.20 (+6.18%)</td><td>37.70 <b>(+63.21%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>146.52 (n/a)</td><td>143.50 (n/a)</td><td>124.50 (n/a)</td><td>23.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.08 (-19.96%)</td><td>0.06 (-14.25%)</td><td>0.06 (-7.03%)</td><td>0.04 <b>(-29.37%)</b></td><td>0.02 (-10.99%)</td><td>303.40 <b>(+41.58%)</b></td><td>215.02 (+18.49%)</td><td>204.40 (+7.52%)</td><td>152.90 <b>(+24.92%)</b></td><td>59.96 <b>(+56.81%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>214.30 (n/a)</td><td>181.46 (n/a)</td><td>190.10 (n/a)</td><td>122.40 (n/a)</td><td>38.24 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 <b>(-25.05%)</b></td><td>0.07 (+2.11%)</td><td>0.07 (+11.44%)</td><td>0.06 <b>(+37.36%)</b></td><td>0.01 <b>(-64.91%)</b></td><td>216.00 <b>(-27.17%)</b></td><td>187.52 (-8.25%)</td><td>180.70 (-10.28%)</td><td>167.70 <b>(+33.41%)</b></td><td>21.15 <b>(-65.48%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>296.60 (n/a)</td><td>204.38 (n/a)</td><td>201.40 (n/a)</td><td>125.70 (n/a)</td><td>61.28 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (-0.67%)</td><td>0.03 (+3.98%)</td><td>0.03 (+0.62%)</td><td>0.03 (+17.56%)</td><td>0.01 <b>(-24.81%)</b></td><td>194.20 (-14.97%)</td><td>175.96 (-5.78%)</td><td>188.00 (-0.58%)</td><td>133.80 (+0.68%)</td><td>25.03 <b>(-37.05%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.40 (n/a)</td><td>186.76 (n/a)</td><td>189.10 (n/a)</td><td>132.90 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 <b>(+20.89%)</b></td><td>0.03 (-9.00%)</td><td>0.03 (-15.10%)</td><td>0.02 <b>(-21.93%)</b></td><td>0.01 <b>(+321.31%)</b></td><td>234.90 <b>(+28.08%)</b></td><td>196.14 (+13.76%)</td><td>200.30 (+17.75%)</td><td>135.00 (-17.28%)</td><td>38.12 <b>(+331.69%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>183.40 (n/a)</td><td>172.42 (n/a)</td><td>170.10 (n/a)</td><td>163.20 (n/a)</td><td>8.83 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.03 <b>(-23.39%)</b></td><td>0.03 (-7.07%)</td><td>0.03 (-2.51%)</td><td>0.03 (+18.99%)</td><td>0.00 <b>(-53.56%)</b></td><td>199.50 (-15.96%)</td><td>174.86 (+3.58%)</td><td>167.80 (+2.57%)</td><td>152.00 <b>(+30.47%)</b></td><td>22.28 <b>(-48.69%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>168.82 (n/a)</td><td>163.60 (n/a)</td><td>116.50 (n/a)</td><td>43.42 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (-0.23%)</td><td>0.03 (-4.01%)</td><td>0.03 (-1.81%)</td><td>0.02 (-3.43%)</td><td>0.01 (+11.18%)</td><td>210.60 (+3.59%)</td><td>177.84 (+4.73%)</td><td>170.10 (+1.86%)</td><td>140.70 (+0.21%)</td><td>29.41 (+17.99%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.30 (n/a)</td><td>169.80 (n/a)</td><td>167.00 (n/a)</td><td>140.40 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.03 <b>(-20.89%)</b></td><td>0.03 <b>(-20.23%)</b></td><td>0.03 <b>(-20.17%)</b></td><td>0.01 <b>(-42.94%)</b></td><td>0.01 (+7.30%)</td><td>373.60 <b>(+75.23%)</b></td><td>217.14 <b>(+32.50%)</b></td><td>183.90 <b>(+25.27%)</b></td><td>167.30 <b>(+26.36%)</b></td><td>88.07 <b>(+146.94%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.20 (n/a)</td><td>163.88 (n/a)</td><td>146.80 (n/a)</td><td>132.40 (n/a)</td><td>35.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 <b>(+43.02%)</b></td><td>0.03 (-1.15%)</td><td>0.03 <b>(-32.81%)</b></td><td>0.02 (-10.70%)</td><td>0.01 <b>(+124.29%)</b></td><td>216.60 (+12.00%)</td><td>173.84 (+9.07%)</td><td>206.80 <b>(+48.88%)</b></td><td>94.60 <b>(-30.08%)</b></td><td>53.71 <b>(+78.49%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>159.38 (n/a)</td><td>138.90 (n/a)</td><td>135.30 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (-15.07%)</td><td>0.03 (-7.70%)</td><td>0.03 (-12.95%)</td><td>0.02 (+5.59%)</td><td>0.00 <b>(-36.05%)</b></td><td>211.10 (-5.29%)</td><td>187.48 (+6.05%)</td><td>204.30 (+14.84%)</td><td>149.70 (+17.78%)</td><td>27.62 <b>(-27.95%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.90 (n/a)</td><td>176.78 (n/a)</td><td>177.90 (n/a)</td><td>127.10 (n/a)</td><td>38.34 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.03 (-2.78%)</td><td>0.03 (+4.31%)</td><td>0.03 (+8.46%)</td><td>0.02 (+2.15%)</td><td>0.00 <b>(-20.10%)</b></td><td>233.00 (-2.14%)</td><td>209.48 (-4.47%)</td><td>207.30 (-7.83%)</td><td>187.20 (+2.86%)</td><td>18.57 (-19.11%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.10 (n/a)</td><td>219.28 (n/a)</td><td>224.90 (n/a)</td><td>182.00 (n/a)</td><td>22.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>244.00 (n/a)</td><td>185.10 (n/a)</td><td>169.30 (n/a)</td><td>117.80 (n/a)</td><td>53.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.70 (n/a)</td><td>192.22 (n/a)</td><td>200.00 (n/a)</td><td>156.60 (n/a)</td><td>29.19 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>289.80 (n/a)</td><td>224.30 (n/a)</td><td>209.50 (n/a)</td><td>200.10 (n/a)</td><td>37.07 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>293.60 (n/a)</td><td>217.28 (n/a)</td><td>211.70 (n/a)</td><td>172.20 (n/a)</td><td>48.00 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>196.80 (n/a)</td><td>194.70 (n/a)</td><td>165.60 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.60 (n/a)</td><td>197.32 (n/a)</td><td>188.60 (n/a)</td><td>167.00 (n/a)</td><td>27.25 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>221.30 (n/a)</td><td>196.56 (n/a)</td><td>195.10 (n/a)</td><td>182.00 (n/a)</td><td>15.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>241.20 (n/a)</td><td>210.42 (n/a)</td><td>213.40 (n/a)</td><td>176.00 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.60 (n/a)</td><td>208.34 (n/a)</td><td>233.40 (n/a)</td><td>124.20 (n/a)</td><td>54.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.60 (n/a)</td><td>179.40 (n/a)</td><td>174.50 (n/a)</td><td>135.40 (n/a)</td><td>34.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>330.80 (n/a)</td><td>210.28 (n/a)</td><td>182.80 (n/a)</td><td>128.40 (n/a)</td><td>77.35 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.70 (n/a)</td><td>197.56 (n/a)</td><td>183.00 (n/a)</td><td>153.80 (n/a)</td><td>56.77 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>164.16 (n/a)</td><td>160.50 (n/a)</td><td>129.20 (n/a)</td><td>31.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.40 (n/a)</td><td>185.46 (n/a)</td><td>187.60 (n/a)</td><td>154.80 (n/a)</td><td>31.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>188.24 (n/a)</td><td>193.70 (n/a)</td><td>138.30 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>291.20 (n/a)</td><td>242.54 (n/a)</td><td>231.40 (n/a)</td><td>196.70 (n/a)</td><td>41.49 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>4.20 (-13.21%)</td><td>4.03 (-5.41%)</td><td>4.16 (-0.21%)</td><td>3.51 (-10.98%)</td><td>0.29 (-15.43%)</td><td>2681.60 (+12.33%)</td><td>2344.54 (+5.69%)</td><td>2260.00 (+0.21%)</td><td>2238.80 (+15.23%)</td><td>189.12 (+11.75%)</td><td>1652.42 (-13.21%)</td><td>1585.34 (-5.41%)</td><td>1636.91 (-0.21%)</td><td>1379.54 (-10.98%)</td><td>115.64 (-15.43%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>4.84 (n/a)</td><td>4.26 (n/a)</td><td>4.17 (n/a)</td><td>3.94 (n/a)</td><td>0.35 (n/a)</td><td>2387.20 (n/a)</td><td>2218.30 (n/a)</td><td>2255.30 (n/a)</td><td>1942.90 (n/a)</td><td>169.23 (n/a)</td><td>1904.00 (n/a)</td><td>1675.98 (n/a)</td><td>1640.30 (n/a)</td><td>1549.67 (n/a)</td><td>136.74 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>1.31 (+6.08%)</td><td>1.08 (+14.76%)</td><td>1.11 (+9.03%)</td><td>0.78 <b>(+25.46%)</b></td><td>0.20 <b>(-29.02%)</b></td><td>285.00 <b>(-20.30%)</b></td><td>211.80 (-17.03%)</td><td>200.10 (-8.30%)</td><td>169.10 (-5.74%)</td><td>44.62 <b>(-46.15%)</b></td><td>55.79 (+6.08%)</td><td>45.97 (+14.76%)</td><td>47.16 (+9.03%)</td><td>33.11 <b>(+25.46%)</b></td><td>8.52 <b>(-29.02%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>1.23 (n/a)</td><td>0.94 (n/a)</td><td>1.01 (n/a)</td><td>0.62 (n/a)</td><td>0.28 (n/a)</td><td>357.60 (n/a)</td><td>255.28 (n/a)</td><td>218.20 (n/a)</td><td>179.40 (n/a)</td><td>82.85 (n/a)</td><td>52.60 (n/a)</td><td>40.06 (n/a)</td><td>43.25 (n/a)</td><td>26.39 (n/a)</td><td>12.00 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>1.13 <b>(-29.10%)</b></td><td>0.86 (-15.17%)</td><td>0.89 (-7.35%)</td><td>0.67 (-0.33%)</td><td>0.18 <b>(-51.34%)</b></td><td>330.70 (+0.33%)</td><td>266.18 (+10.17%)</td><td>249.10 (+7.93%)</td><td>196.30 <b>(+41.02%)</b></td><td>55.45 <b>(-32.33%)</b></td><td>48.07 <b>(-29.10%)</b></td><td>36.75 (-15.17%)</td><td>37.88 (-7.35%)</td><td>28.54 (-0.33%)</td><td>7.87 <b>(-51.34%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>1.59 (n/a)</td><td>1.02 (n/a)</td><td>0.96 (n/a)</td><td>0.67 (n/a)</td><td>0.38 (n/a)</td><td>329.60 (n/a)</td><td>241.60 (n/a)</td><td>230.80 (n/a)</td><td>139.20 (n/a)</td><td>81.94 (n/a)</td><td>67.80 (n/a)</td><td>43.32 (n/a)</td><td>40.88 (n/a)</td><td>28.64 (n/a)</td><td>16.18 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.52 (+0.22%)</td><td>0.52 (+0.09%)</td><td>0.52 (+0.01%)</td><td>0.52 (+0.03%)</td><td>0.00 <b>(+33.49%)</b></td><td>48741.00 (-0.03%)</td><td>48565.04 (-0.09%)</td><td>48630.30 (-0.01%)</td><td>48290.30 (-0.22%)</td><td>173.85 <b>(+33.19%)</b></td><td>355.76 (+0.22%)</td><td>353.75 (+0.09%)</td><td>353.28 (+0.01%)</td><td>352.47 (+0.03%)</td><td>1.27 <b>(+33.50%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48756.80 (n/a)</td><td>48607.94 (n/a)</td><td>48633.80 (n/a)</td><td>48398.00 (n/a)</td><td>130.53 (n/a)</td><td>354.97 (n/a)</td><td>353.44 (n/a)</td><td>353.25 (n/a)</td><td>352.36 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.90 (-0.16%)</td><td>0.89 (+0.15%)</td><td>0.89 (+0.59%)</td><td>0.88 (-0.18%)</td><td>0.01 (+18.60%)</td><td>28655.50 (+0.18%)</td><td>28342.74 (-0.15%)</td><td>28300.50 (-0.58%)</td><td>28114.40 (+0.16%)</td><td>243.10 (+18.99%)</td><td>611.07 (-0.16%)</td><td>606.18 (+0.15%)</td><td>607.05 (+0.59%)</td><td>599.53 (-0.18%)</td><td>5.19 (+18.60%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28603.70 (n/a)</td><td>28386.06 (n/a)</td><td>28466.40 (n/a)</td><td>28070.60 (n/a)</td><td>204.31 (n/a)</td><td>612.02 (n/a)</td><td>605.25 (n/a)</td><td>603.51 (n/a)</td><td>600.62 (n/a)</td><td>4.38 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>3.32 (-0.77%)</td><td>3.19 (-1.65%)</td><td>3.15 (-1.44%)</td><td>3.11 (-1.82%)</td><td>0.08 (+3.97%)</td><td>8085.40 (+1.86%)</td><td>7894.12 (+1.68%)</td><td>7979.40 (+1.46%)</td><td>7571.20 (+0.78%)</td><td>204.17 (+6.45%)</td><td>2269.12 (-0.77%)</td><td>2177.48 (-1.65%)</td><td>2153.03 (-1.44%)</td><td>2124.81 (-1.82%)</td><td>57.43 (+3.96%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>3.35 (n/a)</td><td>3.24 (n/a)</td><td>3.20 (n/a)</td><td>3.17 (n/a)</td><td>0.08 (n/a)</td><td>7937.90 (n/a)</td><td>7763.48 (n/a)</td><td>7864.20 (n/a)</td><td>7512.80 (n/a)</td><td>191.79 (n/a)</td><td>2286.75 (n/a)</td><td>2214.00 (n/a)</td><td>2184.56 (n/a)</td><td>2164.28 (n/a)</td><td>55.24 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>4.14 (+0.40%)</td><td>3.51 (-6.25%)</td><td>3.35 (-10.09%)</td><td>3.21 (+3.12%)</td><td>0.37 (-10.42%)</td><td>2507.70 (-3.03%)</td><td>2317.96 (+6.41%)</td><td>2404.50 (+11.23%)</td><td>1947.20 (-0.40%)</td><td>217.75 (-14.81%)</td><td>1085.64 (+0.40%)</td><td>919.20 (-6.25%)</td><td>879.16 (-10.09%)</td><td>842.97 (+3.12%)</td><td>96.15 (-10.42%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>4.12 (n/a)</td><td>3.74 (n/a)</td><td>3.73 (n/a)</td><td>3.12 (n/a)</td><td>0.41 (n/a)</td><td>2586.00 (n/a)</td><td>2178.38 (n/a)</td><td>2161.80 (n/a)</td><td>1955.00 (n/a)</td><td>255.62 (n/a)</td><td>1081.28 (n/a)</td><td>980.45 (n/a)</td><td>977.85 (n/a)</td><td>817.44 (n/a)</td><td>107.34 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.58 <b>(+57.07%)</b></td><td>0.38 (+18.53%)</td><td>0.30 (-3.94%)</td><td>0.27 (-11.12%)</td><td>0.14 <b>(+428.56%)</b></td><td>4581.50 (+12.52%)</td><td>3542.06 (-8.14%)</td><td>4085.50 (+4.11%)</td><td>2152.90 <b>(-36.33%)</b></td><td>1085.25 <b>(+283.55%)</b></td><td>31.17 <b>(+57.07%)</b></td><td>20.72 (+18.53%)</td><td>16.43 (-3.94%)</td><td>14.65 (-11.12%)</td><td>7.32 <b>(+428.56%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.03 (n/a)</td><td>4071.80 (n/a)</td><td>3856.08 (n/a)</td><td>3924.40 (n/a)</td><td>3381.50 (n/a)</td><td>282.95 (n/a)</td><td>19.85 (n/a)</td><td>17.48 (n/a)</td><td>17.10 (n/a)</td><td>16.48 (n/a)</td><td>1.39 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>6.43 (+6.98%)</td><td>4.75 (-3.66%)</td><td>4.75 (-1.61%)</td><td>3.62 (-12.49%)</td><td>1.11 <b>(+63.71%)</b></td><td>1835.80 (+14.27%)</td><td>1459.36 (+6.61%)</td><td>1401.10 (+1.64%)</td><td>1033.70 (-6.53%)</td><td>318.36 <b>(+79.44%)</b></td><td>1988.19 (+6.98%)</td><td>1467.08 (-3.66%)</td><td>1466.90 (-1.61%)</td><td>1119.53 (-12.49%)</td><td>342.21 <b>(+63.71%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>6.01 (n/a)</td><td>4.93 (n/a)</td><td>4.83 (n/a)</td><td>4.14 (n/a)</td><td>0.68 (n/a)</td><td>1606.60 (n/a)</td><td>1368.88 (n/a)</td><td>1378.50 (n/a)</td><td>1105.90 (n/a)</td><td>177.42 (n/a)</td><td>1858.40 (n/a)</td><td>1522.85 (n/a)</td><td>1490.87 (n/a)</td><td>1279.26 (n/a)</td><td>209.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>13.35 (n/a)</td><td>13.13 (n/a)</td><td>13.26 (n/a)</td><td>12.47 (n/a)</td><td>0.37 (n/a)</td><td>13.34 (n/a)</td><td>13.13 (n/a)</td><td>13.25 (n/a)</td><td>12.46 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>25.10 (-0.71%)</td><td>24.31 (+0.06%)</td><td>24.68 (+0.07%)</td><td>22.49 (+0.33%)</td><td>1.07 (-4.70%)</td><td>25.09 (-0.71%)</td><td>24.30 (+0.06%)</td><td>24.67 (+0.07%)</td><td>22.47 (+0.33%)</td><td>1.07 (-4.70%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>25.28 (n/a)</td><td>24.30 (n/a)</td><td>24.66 (n/a)</td><td>22.41 (n/a)</td><td>1.12 (n/a)</td><td>25.27 (n/a)</td><td>24.28 (n/a)</td><td>24.65 (n/a)</td><td>22.40 (n/a)</td><td>1.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>42.89 (+1.80%)</td><td>39.35 (+0.63%)</td><td>40.53 (+0.97%)</td><td>34.28 (+2.90%)</td><td>3.25 (-3.67%)</td><td>42.86 (+1.80%)</td><td>39.32 (+0.63%)</td><td>40.50 (+0.97%)</td><td>34.26 (+2.90%)</td><td>3.25 (-3.67%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>42.13 (n/a)</td><td>39.10 (n/a)</td><td>40.14 (n/a)</td><td>33.32 (n/a)</td><td>3.37 (n/a)</td><td>42.10 (n/a)</td><td>39.08 (n/a)</td><td>40.11 (n/a)</td><td>33.30 (n/a)</td><td>3.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>45.43 (-2.67%)</td><td>43.41 (+1.11%)</td><td>44.69 (+3.10%)</td><td>38.10 (+1.26%)</td><td>3.01 (-8.94%)</td><td>45.40 (-2.67%)</td><td>43.38 (+1.11%)</td><td>44.66 (+3.10%)</td><td>38.07 (+1.26%)</td><td>3.01 (-8.94%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>46.67 (n/a)</td><td>42.93 (n/a)</td><td>43.35 (n/a)</td><td>37.62 (n/a)</td><td>3.31 (n/a)</td><td>46.64 (n/a)</td><td>42.90 (n/a)</td><td>43.32 (n/a)</td><td>37.60 (n/a)</td><td>3.30 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>13.26 (n/a)</td><td>12.34 (n/a)</td><td>12.30 (n/a)</td><td>11.23 (n/a)</td><td>0.80 (n/a)</td><td>13.25 (n/a)</td><td>12.33 (n/a)</td><td>12.30 (n/a)</td><td>11.23 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>24.70 (-1.89%)</td><td>23.86 (-2.41%)</td><td>24.10 (-2.90%)</td><td>22.14 (-1.78%)</td><td>1.02 (-5.91%)</td><td>24.68 (-1.89%)</td><td>23.84 (-2.41%)</td><td>24.09 (-2.90%)</td><td>22.13 (-1.78%)</td><td>1.01 (-5.91%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>25.17 (n/a)</td><td>24.45 (n/a)</td><td>24.82 (n/a)</td><td>22.54 (n/a)</td><td>1.08 (n/a)</td><td>25.16 (n/a)</td><td>24.43 (n/a)</td><td>24.81 (n/a)</td><td>22.53 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>43.17 (+3.38%)</td><td>38.81 (-1.78%)</td><td>40.63 (+1.07%)</td><td>34.16 (+0.25%)</td><td>4.05 <b>(+28.08%)</b></td><td>43.14 (+3.38%)</td><td>38.78 (-1.78%)</td><td>40.60 (+1.07%)</td><td>34.14 (+0.25%)</td><td>4.05 <b>(+28.08%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>41.76 (n/a)</td><td>39.51 (n/a)</td><td>40.20 (n/a)</td><td>34.07 (n/a)</td><td>3.16 (n/a)</td><td>41.73 (n/a)</td><td>39.49 (n/a)</td><td>40.17 (n/a)</td><td>34.05 (n/a)</td><td>3.16 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>45.63 (-0.75%)</td><td>41.30 (+0.87%)</td><td>41.83 (-3.99%)</td><td>33.39 <b>(+24.16%)</b></td><td>4.74 <b>(-40.50%)</b></td><td>45.60 (-0.75%)</td><td>41.28 (+0.87%)</td><td>41.80 (-3.99%)</td><td>33.37 <b>(+24.16%)</b></td><td>4.74 <b>(-40.50%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>45.97 (n/a)</td><td>40.95 (n/a)</td><td>43.57 (n/a)</td><td>26.89 (n/a)</td><td>7.97 (n/a)</td><td>45.94 (n/a)</td><td>40.92 (n/a)</td><td>43.54 (n/a)</td><td>26.87 (n/a)</td><td>7.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>8.64 (-9.66%)</td><td>8.26 (-5.46%)</td><td>8.15 (-4.21%)</td><td>7.93 (-2.93%)</td><td>0.30 <b>(-47.54%)</b></td><td>8.62 (-9.66%)</td><td>8.25 (-5.46%)</td><td>8.13 (-4.21%)</td><td>7.91 (-2.93%)</td><td>0.30 <b>(-47.54%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>9.56 (n/a)</td><td>8.74 (n/a)</td><td>8.51 (n/a)</td><td>8.17 (n/a)</td><td>0.58 (n/a)</td><td>9.54 (n/a)</td><td>8.72 (n/a)</td><td>8.49 (n/a)</td><td>8.15 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.85 (-3.40%)</td><td>0.76 (-5.52%)</td><td>0.76 (-4.12%)</td><td>0.67 (-10.11%)</td><td>0.07 (+17.06%)</td><td>0.84 (-3.40%)</td><td>0.75 (-5.52%)</td><td>0.75 (-4.12%)</td><td>0.66 (-10.11%)</td><td>0.07 (+17.06%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.88 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.74 (n/a)</td><td>0.06 (n/a)</td><td>0.87 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.73 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>1.17 (-8.99%)</td><td>1.04 (-11.25%)</td><td>1.02 (-10.12%)</td><td>0.95 (-12.32%)</td><td>0.09 (-4.87%)</td><td>1.16 (-8.99%)</td><td>1.03 (-11.25%)</td><td>1.01 (-10.12%)</td><td>0.93 (-12.32%)</td><td>0.09 (-4.87%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>1.29 (n/a)</td><td>1.17 (n/a)</td><td>1.14 (n/a)</td><td>1.08 (n/a)</td><td>0.09 (n/a)</td><td>1.28 (n/a)</td><td>1.16 (n/a)</td><td>1.12 (n/a)</td><td>1.07 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>16.17 (-8.31%)</td><td>14.75 (-3.31%)</td><td>14.80 (+0.89%)</td><td>12.91 (-5.49%)</td><td>1.28 (-15.58%)</td><td>15.98 (-8.31%)</td><td>14.58 (-3.31%)</td><td>14.63 (+0.89%)</td><td>12.76 (-5.49%)</td><td>1.26 (-15.58%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>17.63 (n/a)</td><td>15.25 (n/a)</td><td>14.67 (n/a)</td><td>13.66 (n/a)</td><td>1.52 (n/a)</td><td>17.43 (n/a)</td><td>15.07 (n/a)</td><td>14.50 (n/a)</td><td>13.50 (n/a)</td><td>1.50 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>11.80 (-4.91%)</td><td>10.72 (-9.63%)</td><td>11.37 (-2.83%)</td><td>7.39 <b>(-36.57%)</b></td><td>1.87 <b>(+491.55%)</b></td><td>11.60 (-4.91%)</td><td>10.53 (-9.63%)</td><td>11.17 (-2.83%)</td><td>7.26 <b>(-36.57%)</b></td><td>1.84 <b>(+491.55%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>12.41 (n/a)</td><td>11.86 (n/a)</td><td>11.70 (n/a)</td><td>11.65 (n/a)</td><td>0.32 (n/a)</td><td>12.19 (n/a)</td><td>11.65 (n/a)</td><td>11.50 (n/a)</td><td>11.45 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>8.01 (-1.35%)</td><td>7.44 (+1.92%)</td><td>7.40 (+1.84%)</td><td>6.88 (+4.51%)</td><td>0.43 <b>(-32.10%)</b></td><td>7.88 (-1.35%)</td><td>7.31 (+1.92%)</td><td>7.28 (+1.84%)</td><td>6.76 (+4.51%)</td><td>0.42 <b>(-32.10%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>8.12 (n/a)</td><td>7.30 (n/a)</td><td>7.27 (n/a)</td><td>6.58 (n/a)</td><td>0.64 (n/a)</td><td>7.98 (n/a)</td><td>7.18 (n/a)</td><td>7.15 (n/a)</td><td>6.47 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>6.69 (+0.52%)</td><td>5.21 (-13.40%)</td><td>4.98 (-16.97%)</td><td>4.27 <b>(-21.24%)</b></td><td>0.91 <b>(+101.79%)</b></td><td>6.59 (+0.52%)</td><td>5.13 (-13.40%)</td><td>4.90 (-16.97%)</td><td>4.20 <b>(-21.24%)</b></td><td>0.90 <b>(+101.79%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>6.66 (n/a)</td><td>6.02 (n/a)</td><td>6.00 (n/a)</td><td>5.42 (n/a)</td><td>0.45 (n/a)</td><td>6.55 (n/a)</td><td>5.92 (n/a)</td><td>5.90 (n/a)</td><td>5.33 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>13.39 (n/a)</td><td>12.68 (n/a)</td><td>13.09 (n/a)</td><td>10.92 (n/a)</td><td>1.00 (n/a)</td><td>13.38 (n/a)</td><td>12.67 (n/a)</td><td>13.08 (n/a)</td><td>10.91 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>13.22 (n/a)</td><td>12.37 (n/a)</td><td>12.55 (n/a)</td><td>10.99 (n/a)</td><td>0.85 (n/a)</td><td>13.21 (n/a)</td><td>12.36 (n/a)</td><td>12.54 (n/a)</td><td>10.98 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>271.60 (n/a)</td><td>210.68 (n/a)</td><td>212.00 (n/a)</td><td>144.70 (n/a)</td><td>48.72 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.40 (n/a)</td><td>197.20 (n/a)</td><td>195.80 (n/a)</td><td>164.20 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>214.70 (n/a)</td><td>192.96 (n/a)</td><td>198.40 (n/a)</td><td>172.70 (n/a)</td><td>17.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>189.64 (n/a)</td><td>190.70 (n/a)</td><td>158.40 (n/a)</td><td>22.40 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.00 (n/a)</td><td>189.78 (n/a)</td><td>186.40 (n/a)</td><td>181.70 (n/a)</td><td>9.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>277.30 (n/a)</td><td>212.68 (n/a)</td><td>200.60 (n/a)</td><td>181.00 (n/a)</td><td>38.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>300.40 (n/a)</td><td>221.06 (n/a)</td><td>205.20 (n/a)</td><td>193.50 (n/a)</td><td>45.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>325.80 (n/a)</td><td>248.06 (n/a)</td><td>234.40 (n/a)</td><td>182.30 (n/a)</td><td>55.18 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.08 <b>(+29.79%)</b></td><td>0.06 <b>(+27.70%)</b></td><td>0.06 <b>(+40.42%)</b></td><td>0.04 (-1.21%)</td><td>0.02 <b>(+73.45%)</b></td><td>209.60 (+1.26%)</td><td>150.50 (-19.09%)</td><td>140.60 <b>(-28.77%)</b></td><td>104.20 <b>(-22.99%)</b></td><td>40.62 <b>(+40.86%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>186.02 (n/a)</td><td>197.40 (n/a)</td><td>135.30 (n/a)</td><td>28.84 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (-3.06%)</td><td>0.04 (-3.44%)</td><td>0.04 (-0.21%)</td><td>0.04 (+1.01%)</td><td>0.00 (-17.27%)</td><td>209.30 (-0.99%)</td><td>188.84 (+3.23%)</td><td>187.70 (+0.21%)</td><td>164.00 (+3.21%)</td><td>19.77 (-12.60%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>182.94 (n/a)</td><td>187.30 (n/a)</td><td>158.90 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (+6.98%)</td><td>0.05 (-1.84%)</td><td>0.04 (-4.07%)</td><td>0.04 (-9.63%)</td><td>0.01 <b>(+39.58%)</b></td><td>229.80 (+10.64%)</td><td>183.28 (+3.77%)</td><td>188.70 (+4.25%)</td><td>128.60 (-6.47%)</td><td>37.30 <b>(+43.03%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.70 (n/a)</td><td>176.62 (n/a)</td><td>181.00 (n/a)</td><td>137.50 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 <b>(+20.50%)</b></td><td>0.05 <b>(+23.65%)</b></td><td>0.05 (+17.84%)</td><td>0.04 <b>(+52.92%)</b></td><td>0.01 (-17.26%)</td><td>211.20 <b>(-34.59%)</b></td><td>176.48 <b>(-21.35%)</b></td><td>179.40 (-15.14%)</td><td>143.30 (-17.02%)</td><td>24.47 <b>(-57.50%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>322.90 (n/a)</td><td>224.38 (n/a)</td><td>211.40 (n/a)</td><td>172.70 (n/a)</td><td>57.58 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (-19.09%)</td><td>0.04 (-16.80%)</td><td>0.04 (-11.06%)</td><td>0.03 <b>(-25.08%)</b></td><td>0.01 (-10.61%)</td><td>302.50 <b>(+33.50%)</b></td><td>235.70 <b>(+20.91%)</b></td><td>229.50 (+12.44%)</td><td>194.40 <b>(+23.59%)</b></td><td>42.71 <b>(+48.78%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.60 (n/a)</td><td>194.94 (n/a)</td><td>204.10 (n/a)</td><td>157.30 (n/a)</td><td>28.71 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (-15.46%)</td><td>0.04 (-9.25%)</td><td>0.04 (-3.28%)</td><td>0.04 (-7.83%)</td><td>0.00 <b>(-45.62%)</b></td><td>230.90 (+8.45%)</td><td>203.52 (+9.21%)</td><td>196.10 (+3.43%)</td><td>188.00 (+18.24%)</td><td>17.45 <b>(-29.60%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>186.36 (n/a)</td><td>189.60 (n/a)</td><td>159.00 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (+2.50%)</td><td>0.04 (-10.11%)</td><td>0.04 (-17.74%)</td><td>0.03 (-10.13%)</td><td>0.01 <b>(+36.52%)</b></td><td>246.90 (+11.27%)</td><td>211.10 (+12.47%)</td><td>221.10 <b>(+21.55%)</b></td><td>160.60 (-2.43%)</td><td>33.11 <b>(+44.96%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>187.70 (n/a)</td><td>181.90 (n/a)</td><td>164.60 (n/a)</td><td>22.84 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (-2.97%)</td><td>0.04 (-4.27%)</td><td>0.04 (+3.94%)</td><td>0.03 <b>(-22.53%)</b></td><td>0.01 <b>(+70.53%)</b></td><td>315.50 <b>(+29.09%)</b></td><td>229.30 (+7.62%)</td><td>207.70 (-3.75%)</td><td>185.30 (+3.06%)</td><td>54.87 <b>(+125.08%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>244.40 (n/a)</td><td>213.06 (n/a)</td><td>215.80 (n/a)</td><td>179.80 (n/a)</td><td>24.38 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (+4.66%)</td><td>0.04 <b>(+22.42%)</b></td><td>0.04 (+12.61%)</td><td>0.04 <b>(+47.78%)</b></td><td>0.01 <b>(-39.71%)</b></td><td>221.50 <b>(-32.35%)</b></td><td>195.46 <b>(-21.75%)</b></td><td>202.00 (-11.21%)</td><td>167.80 (-4.50%)</td><td>24.44 <b>(-62.79%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>327.40 (n/a)</td><td>249.78 (n/a)</td><td>227.50 (n/a)</td><td>175.70 (n/a)</td><td>65.68 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (+11.98%)</td><td>0.04 (+11.13%)</td><td>0.04 (+2.98%)</td><td>0.03 <b>(+28.30%)</b></td><td>0.00 (-16.27%)</td><td>252.90 <b>(-22.06%)</b></td><td>223.58 (-11.00%)</td><td>233.30 (-2.87%)</td><td>191.20 (-10.65%)</td><td>25.01 <b>(-43.10%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>324.50 (n/a)</td><td>251.22 (n/a)</td><td>240.20 (n/a)</td><td>214.00 (n/a)</td><td>43.95 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (+17.24%)</td><td>0.06 <b>(+20.30%)</b></td><td>0.06 <b>(+33.48%)</b></td><td>0.05 <b>(+25.10%)</b></td><td>0.01 (-15.57%)</td><td>159.80 <b>(-20.06%)</b></td><td>137.56 (-18.18%)</td><td>130.10 <b>(-25.06%)</b></td><td>114.30 (-14.70%)</td><td>19.63 <b>(-40.31%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>168.12 (n/a)</td><td>173.60 (n/a)</td><td>134.00 (n/a)</td><td>32.89 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (+19.44%)</td><td>0.04 (+10.26%)</td><td>0.04 (+2.88%)</td><td>0.04 (+13.75%)</td><td>0.01 <b>(+64.28%)</b></td><td>209.00 (-12.07%)</td><td>191.76 (-8.79%)</td><td>205.40 (-2.79%)</td><td>159.40 (-16.28%)</td><td>22.16 <b>(+22.23%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.70 (n/a)</td><td>210.24 (n/a)</td><td>211.30 (n/a)</td><td>190.40 (n/a)</td><td>18.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 <b>(+21.72%)</b></td><td>0.06 <b>(+28.27%)</b></td><td>0.06 <b>(+39.59%)</b></td><td>0.04 <b>(+21.78%)</b></td><td>0.01 <b>(+34.07%)</b></td><td>206.70 (-17.88%)</td><td>150.56 <b>(-21.62%)</b></td><td>135.50 <b>(-28.38%)</b></td><td>128.60 (-17.83%)</td><td>32.77 (-10.49%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.70 (n/a)</td><td>192.10 (n/a)</td><td>189.20 (n/a)</td><td>156.50 (n/a)</td><td>36.61 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (+3.04%)</td><td>0.05 (+6.74%)</td><td>0.05 (+16.21%)</td><td>0.04 (+2.62%)</td><td>0.01 (+7.10%)</td><td>199.40 (-2.54%)</td><td>165.10 (-6.07%)</td><td>157.60 (-13.93%)</td><td>130.00 (-2.99%)</td><td>28.23 (+5.27%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>175.76 (n/a)</td><td>183.10 (n/a)</td><td>134.00 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (-1.02%)</td><td>0.05 (-0.57%)</td><td>0.05 (-2.33%)</td><td>0.04 (-11.41%)</td><td>0.01 (+6.35%)</td><td>219.00 (+12.89%)</td><td>165.06 (+1.15%)</td><td>149.90 (+2.39%)</td><td>138.20 (+1.02%)</td><td>32.99 (+18.96%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.00 (n/a)</td><td>163.18 (n/a)</td><td>146.40 (n/a)</td><td>136.80 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (+1.42%)</td><td>0.04 (-5.61%)</td><td>0.05 (+3.26%)</td><td>0.02 <b>(-41.59%)</b></td><td>0.01 <b>(+137.96%)</b></td><td>358.80 <b>(+71.18%)</b></td><td>208.88 (+15.05%)</td><td>173.70 (-3.18%)</td><td>152.70 (-1.42%)</td><td>84.65 <b>(+331.45%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.60 (n/a)</td><td>181.56 (n/a)</td><td>179.40 (n/a)</td><td>154.90 (n/a)</td><td>19.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (+13.03%)</td><td>0.05 (+7.95%)</td><td>0.04 (+4.10%)</td><td>0.04 (+11.80%)</td><td>0.01 <b>(+31.38%)</b></td><td>199.20 (-10.55%)</td><td>182.08 (-7.08%)</td><td>193.50 (-3.97%)</td><td>152.80 (-11.52%)</td><td>20.68 (+5.61%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>222.70 (n/a)</td><td>195.96 (n/a)</td><td>201.50 (n/a)</td><td>172.70 (n/a)</td><td>19.58 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (+11.16%)</td><td>0.04 (-0.78%)</td><td>0.05 (+5.03%)</td><td>0.03 <b>(-30.55%)</b></td><td>0.01 <b>(+271.06%)</b></td><td>289.10 <b>(+43.97%)</b></td><td>198.70 (+5.18%)</td><td>178.70 (-4.79%)</td><td>160.10 (-10.06%)</td><td>52.65 <b>(+393.10%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>200.80 (n/a)</td><td>188.92 (n/a)</td><td>187.70 (n/a)</td><td>178.00 (n/a)</td><td>10.68 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.21 (-0.16%)</td><td>0.21 (-0.01%)</td><td>0.21 (+0.03%)</td><td>0.20 (-0.06%)</td><td>0.00 <b>(-30.15%)</b></td><td>40928.50 (+0.06%)</td><td>40842.10 (+0.01%)</td><td>40822.60 (-0.03%)</td><td>40793.60 (+0.16%)</td><td>51.73 <b>(-30.00%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40905.80 (n/a)</td><td>40836.80 (n/a)</td><td>40836.10 (n/a)</td><td>40727.10 (n/a)</td><td>73.91 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (-5.28%)</td><td>0.06 (+12.64%)</td><td>0.06 <b>(+35.89%)</b></td><td>0.05 <b>(+20.34%)</b></td><td>0.01 <b>(-24.12%)</b></td><td>180.50 (-16.90%)</td><td>142.84 (-13.52%)</td><td>129.60 <b>(-26.41%)</b></td><td>117.00 (+5.60%)</td><td>28.24 <b>(-32.25%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>165.18 (n/a)</td><td>176.10 (n/a)</td><td>110.80 (n/a)</td><td>41.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.08 <b>(-24.85%)</b></td><td>0.07 (-11.78%)</td><td>0.07 (-4.55%)</td><td>0.06 (+1.72%)</td><td>0.01 <b>(-54.74%)</b></td><td>211.10 (-1.68%)</td><td>175.60 (+9.72%)</td><td>170.80 (+4.79%)</td><td>148.00 <b>(+33.09%)</b></td><td>22.79 <b>(-39.43%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>214.70 (n/a)</td><td>160.04 (n/a)</td><td>163.00 (n/a)</td><td>111.20 (n/a)</td><td>37.63 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 <b>(+23.49%)</b></td><td>0.05 (+16.52%)</td><td>0.05 (+9.36%)</td><td>0.05 <b>(+20.88%)</b></td><td>0.01 <b>(+45.50%)</b></td><td>175.60 (-17.29%)</td><td>156.18 (-13.56%)</td><td>172.80 (-8.52%)</td><td>125.80 (-19.00%)</td><td>24.89 (+1.68%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>180.68 (n/a)</td><td>188.90 (n/a)</td><td>155.30 (n/a)</td><td>24.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 (-5.40%)</td><td>0.05 (-9.88%)</td><td>0.05 (-12.71%)</td><td>0.03 <b>(-40.64%)</b></td><td>0.02 <b>(+46.70%)</b></td><td>372.40 <b>(+68.43%)</b></td><td>210.88 <b>(+20.16%)</b></td><td>187.60 (+14.53%)</td><td>146.30 (+5.71%)</td><td>92.06 <b>(+174.56%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>175.50 (n/a)</td><td>163.80 (n/a)</td><td>138.40 (n/a)</td><td>33.53 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.07 <b>(+27.92%)</b></td><td>0.05 (+9.63%)</td><td>0.05 (+2.33%)</td><td>0.05 (+18.88%)</td><td>0.01 <b>(+35.45%)</b></td><td>178.90 (-15.89%)</td><td>153.96 (-8.56%)</td><td>153.60 (-2.23%)</td><td>120.60 <b>(-21.84%)</b></td><td>21.61 (-13.71%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>168.38 (n/a)</td><td>157.10 (n/a)</td><td>154.30 (n/a)</td><td>25.04 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.08 <b>(+41.21%)</b></td><td>0.06 (+18.37%)</td><td>0.06 (+0.92%)</td><td>0.05 (+16.58%)</td><td>0.01 <b>(+118.65%)</b></td><td>207.70 (-14.21%)</td><td>167.62 (-13.53%)</td><td>180.10 (-0.88%)</td><td>126.60 <b>(-29.19%)</b></td><td>34.81 <b>(+28.55%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>242.10 (n/a)</td><td>193.84 (n/a)</td><td>181.70 (n/a)</td><td>178.80 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (-2.34%)</td><td>0.05 (+1.59%)</td><td>0.05 (+2.08%)</td><td>0.04 (+2.29%)</td><td>0.01 (-17.11%)</td><td>197.10 (-2.28%)</td><td>171.44 (-2.05%)</td><td>176.40 (-2.05%)</td><td>149.70 (+2.39%)</td><td>19.41 (-17.80%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>175.02 (n/a)</td><td>180.10 (n/a)</td><td>146.20 (n/a)</td><td>23.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (-10.54%)</td><td>0.05 (-6.60%)</td><td>0.05 (-7.11%)</td><td>0.04 (-7.39%)</td><td>0.00 <b>(-31.22%)</b></td><td>236.40 (+7.99%)</td><td>198.12 (+6.34%)</td><td>190.90 (+7.67%)</td><td>178.40 (+11.78%)</td><td>22.59 (-15.92%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.90 (n/a)</td><td>186.30 (n/a)</td><td>177.30 (n/a)</td><td>159.60 (n/a)</td><td>26.87 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (-3.75%)</td><td>0.05 (+1.98%)</td><td>0.05 (+10.02%)</td><td>0.04 (+5.37%)</td><td>0.01 (-4.24%)</td><td>205.00 (-5.09%)</td><td>175.26 (-2.07%)</td><td>167.00 (-9.09%)</td><td>147.70 (+3.94%)</td><td>27.67 (-2.87%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>178.96 (n/a)</td><td>183.70 (n/a)</td><td>142.10 (n/a)</td><td>28.49 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 <b>(-29.66%)</b></td><td>0.05 (-13.99%)</td><td>0.05 (+6.55%)</td><td>0.04 (-3.40%)</td><td>0.01 <b>(-61.35%)</b></td><td>239.60 (+3.50%)</td><td>198.52 (+11.17%)</td><td>186.90 (-6.13%)</td><td>177.30 <b>(+42.18%)</b></td><td>26.67 <b>(-42.13%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>178.58 (n/a)</td><td>199.10 (n/a)</td><td>124.70 (n/a)</td><td>46.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (+1.26%)</td><td>0.05 (-1.99%)</td><td>0.05 (-9.58%)</td><td>0.04 (+5.18%)</td><td>0.01 (-14.62%)</td><td>189.20 (-4.92%)</td><td>173.68 (+1.61%)</td><td>176.20 (+10.61%)</td><td>146.20 (-1.22%)</td><td>17.28 <b>(-21.17%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>170.92 (n/a)</td><td>159.30 (n/a)</td><td>148.00 (n/a)</td><td>21.92 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (-14.59%)</td><td>0.04 (-6.74%)</td><td>0.04 (+6.07%)</td><td>0.03 (-7.79%)</td><td>0.01 <b>(-37.65%)</b></td><td>253.40 (+8.48%)</td><td>206.40 (+5.94%)</td><td>198.10 (-5.71%)</td><td>181.70 (+17.07%)</td><td>27.83 (-17.25%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.60 (n/a)</td><td>194.82 (n/a)</td><td>210.10 (n/a)</td><td>155.20 (n/a)</td><td>33.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.05 (-9.36%)</td><td>0.04 (+1.38%)</td><td>0.05 (+17.71%)</td><td>0.03 (-13.43%)</td><td>0.01 (+0.23%)</td><td>291.60 (+15.49%)</td><td>196.72 (-0.23%)</td><td>172.80 (-15.04%)</td><td>162.80 (+10.30%)</td><td>53.97 <b>(+32.46%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.50 (n/a)</td><td>197.18 (n/a)</td><td>203.40 (n/a)</td><td>147.60 (n/a)</td><td>40.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.06 (+10.12%)</td><td>0.04 (-6.38%)</td><td>0.04 (-6.78%)</td><td>0.03 (-13.60%)</td><td>0.01 <b>(+29.93%)</b></td><td>256.60 (+15.74%)</td><td>210.98 (+8.51%)</td><td>223.10 (+7.26%)</td><td>145.70 (-9.22%)</td><td>41.99 <b>(+33.81%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.70 (n/a)</td><td>194.44 (n/a)</td><td>208.00 (n/a)</td><td>160.50 (n/a)</td><td>31.38 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.04 (-8.01%)</td><td>0.04 (+14.60%)</td><td>0.04 (+14.17%)</td><td>0.04 <b>(+51.68%)</b></td><td>0.00 <b>(-77.37%)</b></td><td>226.10 <b>(-34.08%)</b></td><td>209.70 (-17.87%)</td><td>210.20 (-12.38%)</td><td>194.40 (+8.72%)</td><td>11.42 <b>(-84.03%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>343.00 (n/a)</td><td>255.32 (n/a)</td><td>239.90 (n/a)</td><td>178.80 (n/a)</td><td>71.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.69 (-2.92%)</td><td>0.63 (+11.27%)</td><td>0.66 (+5.19%)</td><td>0.50 <b>(+73.26%)</b></td><td>0.08 <b>(-57.45%)</b></td><td>196.80 <b>(-42.27%)</b></td><td>158.68 (-18.65%)</td><td>149.40 (-4.96%)</td><td>142.10 (+2.97%)</td><td>21.93 <b>(-74.22%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.71 (n/a)</td><td>0.56 (n/a)</td><td>0.63 (n/a)</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>340.90 (n/a)</td><td>195.06 (n/a)</td><td>157.20 (n/a)</td><td>138.00 (n/a)</td><td>85.07 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.63 (+1.06%)</td><td>0.53 (-4.94%)</td><td>0.50 (-9.91%)</td><td>0.45 (-6.37%)</td><td>0.08 <b>(+44.79%)</b></td><td>218.30 (+6.80%)</td><td>188.38 (+6.19%)</td><td>197.80 (+11.00%)</td><td>155.70 (-1.08%)</td><td>27.05 <b>(+50.93%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.62 (n/a)</td><td>0.56 (n/a)</td><td>0.55 (n/a)</td><td>0.48 (n/a)</td><td>0.05 (n/a)</td><td>204.40 (n/a)</td><td>177.40 (n/a)</td><td>178.20 (n/a)</td><td>157.40 (n/a)</td><td>17.92 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.65 (-7.04%)</td><td>0.57 (-4.72%)</td><td>0.60 (+4.12%)</td><td>0.48 (-3.26%)</td><td>0.08 (-18.32%)</td><td>205.20 (+3.38%)</td><td>175.88 (+4.43%)</td><td>163.80 (-3.99%)</td><td>150.40 (+7.58%)</td><td>25.81 (-5.82%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.70 (n/a)</td><td>0.60 (n/a)</td><td>0.58 (n/a)</td><td>0.50 (n/a)</td><td>0.10 (n/a)</td><td>198.50 (n/a)</td><td>168.42 (n/a)</td><td>170.60 (n/a)</td><td>139.80 (n/a)</td><td>27.41 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.73 (+6.27%)</td><td>0.55 (-1.01%)</td><td>0.54 (-0.79%)</td><td>0.42 (-13.37%)</td><td>0.12 <b>(+56.77%)</b></td><td>233.10 (+15.40%)</td><td>185.18 (+3.37%)</td><td>183.50 (+0.82%)</td><td>134.30 (-5.95%)</td><td>38.62 <b>(+75.11%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.69 (n/a)</td><td>0.56 (n/a)</td><td>0.54 (n/a)</td><td>0.49 (n/a)</td><td>0.08 (n/a)</td><td>202.00 (n/a)</td><td>179.14 (n/a)</td><td>182.00 (n/a)</td><td>142.80 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.62 (+19.32%)</td><td>0.50 (+9.08%)</td><td>0.55 (+10.05%)</td><td>0.31 (-4.05%)</td><td>0.12 <b>(+46.56%)</b></td><td>241.30 (+4.23%)</td><td>158.20 (-5.56%)</td><td>133.30 (-9.13%)</td><td>118.30 (-16.16%)</td><td>49.53 <b>(+31.02%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.52 (n/a)</td><td>0.46 (n/a)</td><td>0.50 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>231.50 (n/a)</td><td>167.52 (n/a)</td><td>146.70 (n/a)</td><td>141.10 (n/a)</td><td>37.80 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.59 (+4.40%)</td><td>0.42 (-9.93%)</td><td>0.44 (-10.69%)</td><td>0.25 <b>(-20.68%)</b></td><td>0.12 <b>(+29.58%)</b></td><td>300.50 <b>(+26.10%)</b></td><td>189.54 (+15.46%)</td><td>167.80 (+11.94%)</td><td>125.40 (-4.27%)</td><td>66.36 <b>(+56.08%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.56 (n/a)</td><td>0.47 (n/a)</td><td>0.49 (n/a)</td><td>0.31 (n/a)</td><td>0.10 (n/a)</td><td>238.30 (n/a)</td><td>164.16 (n/a)</td><td>149.90 (n/a)</td><td>131.00 (n/a)</td><td>42.52 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.58 (+12.21%)</td><td>0.42 (-4.27%)</td><td>0.40 (-10.03%)</td><td>0.28 <b>(-29.16%)</b></td><td>0.12 <b>(+141.27%)</b></td><td>266.60 <b>(+41.21%)</b></td><td>186.30 (+10.22%)</td><td>185.50 (+11.14%)</td><td>127.70 (-10.89%)</td><td>53.19 <b>(+205.04%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.51 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.05 (n/a)</td><td>188.80 (n/a)</td><td>169.02 (n/a)</td><td>166.90 (n/a)</td><td>143.30 (n/a)</td><td>17.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.57 (+11.58%)</td><td>0.43 (+4.22%)</td><td>0.36 (-2.54%)</td><td>0.33 (-2.24%)</td><td>0.11 <b>(+36.11%)</b></td><td>223.50 (+2.29%)</td><td>181.90 (-1.95%)</td><td>204.40 (+2.61%)</td><td>129.90 (-10.35%)</td><td>44.60 <b>(+24.32%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>218.50 (n/a)</td><td>185.52 (n/a)</td><td>199.20 (n/a)</td><td>144.90 (n/a)</td><td>35.87 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.73 (-7.94%)</td><td>0.67 (-9.78%)</td><td>0.71 (-5.47%)</td><td>0.59 (-14.34%)</td><td>0.06 <b>(+72.23%)</b></td><td>220.40 (+16.74%)</td><td>195.72 (+11.45%)</td><td>184.40 (+5.79%)</td><td>180.50 (+8.60%)</td><td>19.27 <b>(+116.44%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.79 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.69 (n/a)</td><td>0.04 (n/a)</td><td>188.80 (n/a)</td><td>175.62 (n/a)</td><td>174.30 (n/a)</td><td>166.20 (n/a)</td><td>8.90 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.88 (-1.63%)</td><td>0.79 (+5.34%)</td><td>0.78 (+5.72%)</td><td>0.70 (+3.35%)</td><td>0.07 <b>(-21.12%)</b></td><td>186.20 (-3.22%)</td><td>166.60 (-5.38%)</td><td>168.40 (-5.39%)</td><td>149.40 (+1.63%)</td><td>13.91 <b>(-21.28%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.89 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.68 (n/a)</td><td>0.08 (n/a)</td><td>192.40 (n/a)</td><td>176.08 (n/a)</td><td>178.00 (n/a)</td><td>147.00 (n/a)</td><td>17.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.86 (-1.98%)</td><td>0.76 (+6.13%)</td><td>0.76 (+11.57%)</td><td>0.69 (+7.71%)</td><td>0.06 <b>(-34.24%)</b></td><td>188.80 (-7.13%)</td><td>172.82 (-6.45%)</td><td>172.00 (-10.37%)</td><td>152.60 (+2.01%)</td><td>13.46 <b>(-37.47%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.88 (n/a)</td><td>0.72 (n/a)</td><td>0.68 (n/a)</td><td>0.64 (n/a)</td><td>0.09 (n/a)</td><td>203.30 (n/a)</td><td>184.74 (n/a)</td><td>191.90 (n/a)</td><td>149.60 (n/a)</td><td>21.53 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.00 (+2.33%)</td><td>0.00 (+3.35%)</td><td>0.00 (+2.33%)</td><td>0.00 (+2.50%)</td><td>0.00 <b>(-20.65%)</b></td><td>997.41 (-2.92%)</td><td>948.98 (-3.37%)</td><td>941.07 (-1.42%)</td><td>923.55 (-2.80%)</td><td>28.55 <b>(-30.28%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1027.44 (n/a)</td><td>982.05 (n/a)</td><td>954.62 (n/a)</td><td>950.15 (n/a)</td><td>40.94 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.01 (-2.35%)</td><td>0.01 (+1.99%)</td><td>0.01 (+0.00%)</td><td>0.01 (+10.96%)</td><td>0.00 <b>(-81.43%)</b></td><td>1009.34 (-10.10%)</td><td>995.36 (-2.49%)</td><td>994.78 (-0.94%)</td><td>983.33 (+2.22%)</td><td>9.52 <b>(-84.23%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1122.74 (n/a)</td><td>1020.83 (n/a)</td><td>1004.23 (n/a)</td><td>961.96 (n/a)</td><td>60.40 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>0.98 (+3.97%)</td><td>0.94 (+1.26%)</td><td>0.94 (+0.85%)</td><td>0.92 (-0.17%)</td><td>0.02 <b>(+169.82%)</b></td><td>2280.56 (+0.17%)</td><td>2226.71 (-1.20%)</td><td>2237.63 (-0.84%)</td><td>2143.56 (-3.82%)</td><td>54.85 <b>(+159.71%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.92 (n/a)</td><td>0.01 (n/a)</td><td>2276.66 (n/a)</td><td>2253.67 (n/a)</td><td>2256.59 (n/a)</td><td>2228.69 (n/a)</td><td>21.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>2.64 <b>(-20.78%)</b></td><td>2.58 (-16.36%)</td><td>2.58 (-15.56%)</td><td>2.52 (-6.04%)</td><td>0.04 <b>(-82.44%)</b></td><td>207.90 (+6.40%)</td><td>203.54 (+18.88%)</td><td>203.30 (+18.40%)</td><td>198.90 <b>(+26.21%)</b></td><td>3.52 <b>(-76.58%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>3.33 (n/a)</td><td>3.08 (n/a)</td><td>3.05 (n/a)</td><td>2.68 (n/a)</td><td>0.26 (n/a)</td><td>195.40 (n/a)</td><td>171.22 (n/a)</td><td>171.70 (n/a)</td><td>157.60 (n/a)</td><td>15.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>5.08 (-17.71%)</td><td>4.51 (-7.40%)</td><td>4.42 (-3.10%)</td><td>4.17 (+0.49%)</td><td>0.34 <b>(-57.06%)</b></td><td>251.60 (-0.51%)</td><td>233.38 (+6.39%)</td><td>237.10 (+3.22%)</td><td>206.40 <b>(+21.48%)</b></td><td>16.68 <b>(-47.91%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>6.17 (n/a)</td><td>4.87 (n/a)</td><td>4.56 (n/a)</td><td>4.15 (n/a)</td><td>0.80 (n/a)</td><td>252.90 (n/a)</td><td>219.36 (n/a)</td><td>229.70 (n/a)</td><td>169.90 (n/a)</td><td>32.01 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:41:42</td><td>2.71 (-13.41%)</td><td>2.68 (-4.63%)</td><td>2.69 (-6.22%)</td><td>2.66 (+9.21%)</td><td>0.02 <b>(-92.52%)</b></td><td>197.10 (-8.41%)</td><td>195.54 (+4.10%)</td><td>195.10 (+6.61%)</td><td>193.60 (+15.51%)</td><td>1.46 <b>(-92.06%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>3.13 (n/a)</td><td>2.81 (n/a)</td><td>2.87 (n/a)</td><td>2.44 (n/a)</td><td>0.27 (n/a)</td><td>215.20 (n/a)</td><td>187.84 (n/a)</td><td>183.00 (n/a)</td><td>167.60 (n/a)</td><td>18.40 (n/a)</td>
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
