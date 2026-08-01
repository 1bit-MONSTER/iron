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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.07 (-1.17%)</td><td>0.07 (+3.24%)</td><td>0.07 (+8.87%)</td><td>0.06 (-3.37%)</td><td>0.01 (+11.45%)</td><td>213.30 (+3.49%)</td><td>187.28 (-2.98%)</td><td>182.60 (-8.15%)</td><td>171.30 (+1.18%)</td><td>17.46 (+16.73%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>206.10 (n/a)</td><td>193.04 (n/a)</td><td>198.80 (n/a)</td><td>169.30 (n/a)</td><td>14.96 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.09 <b>(+25.39%)</b></td><td>0.07 (+12.59%)</td><td>0.07 (+5.06%)</td><td>0.07 (+17.23%)</td><td>0.01 <b>(+63.99%)</b></td><td>183.00 (-14.69%)</td><td>166.72 (-10.76%)</td><td>175.40 (-4.83%)</td><td>138.00 <b>(-20.23%)</b></td><td>18.26 (+10.08%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>186.82 (n/a)</td><td>184.30 (n/a)</td><td>173.00 (n/a)</td><td>16.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.08 <b>(+24.69%)</b></td><td>0.07 (+18.57%)</td><td>0.06 (+7.10%)</td><td>0.05 (+13.47%)</td><td>0.01 <b>(+55.96%)</b></td><td>227.20 (-11.87%)</td><td>184.46 (-14.93%)</td><td>191.60 (-6.63%)</td><td>150.00 (-19.79%)</td><td>30.44 (+8.09%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>257.80 (n/a)</td><td>216.84 (n/a)</td><td>205.20 (n/a)</td><td>187.00 (n/a)</td><td>28.16 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.07 (+17.67%)</td><td>0.06 (+6.33%)</td><td>0.06 (+6.91%)</td><td>0.05 (-4.43%)</td><td>0.01 <b>(+189.02%)</b></td><td>245.90 (+4.64%)</td><td>207.66 (-5.00%)</td><td>203.10 (-6.49%)</td><td>176.80 (-15.00%)</td><td>25.48 <b>(+156.30%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>235.00 (n/a)</td><td>218.58 (n/a)</td><td>217.20 (n/a)</td><td>208.00 (n/a)</td><td>9.94 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (-15.85%)</td><td>0.03 (-6.27%)</td><td>0.03 (-8.03%)</td><td>0.02 (-3.96%)</td><td>0.00 <b>(-31.21%)</b></td><td>211.40 (+4.09%)</td><td>162.52 (+5.26%)</td><td>151.30 (+8.77%)</td><td>145.60 (+18.86%)</td><td>27.83 (-14.89%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>154.40 (n/a)</td><td>139.10 (n/a)</td><td>122.50 (n/a)</td><td>32.70 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (+16.12%)</td><td>0.04 <b>(+20.07%)</b></td><td>0.04 (+19.90%)</td><td>0.03 (+12.06%)</td><td>0.01 (+14.75%)</td><td>161.90 (-10.80%)</td><td>133.40 (-16.71%)</td><td>136.90 (-16.58%)</td><td>100.40 (-13.89%)</td><td>23.19 (-12.27%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>181.50 (n/a)</td><td>160.16 (n/a)</td><td>164.10 (n/a)</td><td>116.60 (n/a)</td><td>26.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (+4.47%)</td><td>0.03 (-10.97%)</td><td>0.03 <b>(-25.75%)</b></td><td>0.03 (-7.58%)</td><td>0.01 <b>(+32.43%)</b></td><td>199.90 (+8.23%)</td><td>175.52 (+13.84%)</td><td>191.40 <b>(+34.60%)</b></td><td>126.20 (-4.32%)</td><td>31.51 <b>(+37.31%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>184.70 (n/a)</td><td>154.18 (n/a)</td><td>142.20 (n/a)</td><td>131.90 (n/a)</td><td>22.95 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (+4.77%)</td><td>0.03 (+5.55%)</td><td>0.03 (-6.04%)</td><td>0.03 <b>(+23.29%)</b></td><td>0.01 (-3.00%)</td><td>204.90 (-18.88%)</td><td>182.80 (-6.01%)</td><td>201.80 (+6.43%)</td><td>137.70 (-4.57%)</td><td>30.06 <b>(-23.30%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.60 (n/a)</td><td>194.48 (n/a)</td><td>189.60 (n/a)</td><td>144.30 (n/a)</td><td>39.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (+9.49%)</td><td>0.03 (+0.10%)</td><td>0.03 (-9.64%)</td><td>0.03 (+9.71%)</td><td>0.00 (+3.84%)</td><td>194.50 (-8.86%)</td><td>177.02 (-0.35%)</td><td>187.80 (+10.67%)</td><td>135.00 (-8.66%)</td><td>24.58 (-15.22%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.40 (n/a)</td><td>177.64 (n/a)</td><td>169.70 (n/a)</td><td>147.80 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.03 (+13.85%)</td><td>0.03 (+10.11%)</td><td>0.03 (+5.85%)</td><td>0.03 (+17.67%)</td><td>0.00 (+6.91%)</td><td>203.90 (-15.01%)</td><td>189.46 (-9.31%)</td><td>192.30 (-5.50%)</td><td>159.30 (-12.13%)</td><td>17.63 <b>(-21.94%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.90 (n/a)</td><td>208.92 (n/a)</td><td>203.50 (n/a)</td><td>181.30 (n/a)</td><td>22.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.03 (+1.05%)</td><td>0.03 (+11.95%)</td><td>0.03 (+9.18%)</td><td>0.02 <b>(+39.45%)</b></td><td>0.00 <b>(-33.63%)</b></td><td>226.20 <b>(-28.30%)</b></td><td>183.00 (-13.99%)</td><td>180.80 (-8.41%)</td><td>152.20 (-0.98%)</td><td>27.62 <b>(-54.65%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>315.50 (n/a)</td><td>212.76 (n/a)</td><td>197.40 (n/a)</td><td>153.70 (n/a)</td><td>60.91 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.03 (+7.08%)</td><td>0.02 (+0.17%)</td><td>0.02 (+3.39%)</td><td>0.02 (-6.49%)</td><td>0.00 <b>(+41.91%)</b></td><td>255.10 (+6.96%)</td><td>220.90 (+0.38%)</td><td>218.80 (-3.31%)</td><td>183.90 (-6.60%)</td><td>25.59 <b>(+40.26%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.50 (n/a)</td><td>220.06 (n/a)</td><td>226.30 (n/a)</td><td>196.90 (n/a)</td><td>18.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.90 (n/a)</td><td>177.20 (n/a)</td><td>186.00 (n/a)</td><td>130.80 (n/a)</td><td>31.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>200.60 (n/a)</td><td>173.10 (n/a)</td><td>183.10 (n/a)</td><td>123.60 (n/a)</td><td>29.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>281.20 (n/a)</td><td>212.16 (n/a)</td><td>218.30 (n/a)</td><td>141.80 (n/a)</td><td>52.83 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>235.40 (n/a)</td><td>193.80 (n/a)</td><td>200.00 (n/a)</td><td>159.90 (n/a)</td><td>32.04 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>179.58 (n/a)</td><td>171.60 (n/a)</td><td>157.70 (n/a)</td><td>19.92 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>178.50 (n/a)</td><td>178.30 (n/a)</td><td>162.50 (n/a)</td><td>16.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>190.72 (n/a)</td><td>195.70 (n/a)</td><td>147.10 (n/a)</td><td>32.49 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>332.80 (n/a)</td><td>220.76 (n/a)</td><td>208.80 (n/a)</td><td>163.20 (n/a)</td><td>67.67 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.30 (n/a)</td><td>184.30 (n/a)</td><td>186.10 (n/a)</td><td>122.70 (n/a)</td><td>37.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.10 (n/a)</td><td>177.28 (n/a)</td><td>175.30 (n/a)</td><td>143.20 (n/a)</td><td>23.84 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>188.62 (n/a)</td><td>196.40 (n/a)</td><td>164.50 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>275.10 (n/a)</td><td>207.82 (n/a)</td><td>188.20 (n/a)</td><td>177.10 (n/a)</td><td>41.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.20 (n/a)</td><td>204.32 (n/a)</td><td>186.60 (n/a)</td><td>174.80 (n/a)</td><td>31.95 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.20 (n/a)</td><td>193.70 (n/a)</td><td>188.00 (n/a)</td><td>155.80 (n/a)</td><td>30.41 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.20 (n/a)</td><td>187.46 (n/a)</td><td>180.40 (n/a)</td><td>163.50 (n/a)</td><td>21.02 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>254.10 (n/a)</td><td>231.76 (n/a)</td><td>246.10 (n/a)</td><td>186.30 (n/a)</td><td>28.26 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>4.48 (+5.99%)</td><td>3.98 (-3.94%)</td><td>4.02 (-3.63%)</td><td>3.38 (-16.57%)</td><td>0.41 <b>(+494.78%)</b></td><td>2779.20 (+19.87%)</td><td>2385.64 (+5.03%)</td><td>2340.50 (+3.76%)</td><td>2100.90 (-5.65%)</td><td>259.11 <b>(+575.77%)</b></td><td>1760.88 (+5.99%)</td><td>1564.79 (-3.94%)</td><td>1580.56 (-3.63%)</td><td>1331.09 (-16.57%)</td><td>163.04 <b>(+494.77%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>4.22 (n/a)</td><td>4.14 (n/a)</td><td>4.17 (n/a)</td><td>4.06 (n/a)</td><td>0.07 (n/a)</td><td>2318.60 (n/a)</td><td>2271.40 (n/a)</td><td>2255.70 (n/a)</td><td>2226.70 (n/a)</td><td>38.34 (n/a)</td><td>1661.34 (n/a)</td><td>1629.06 (n/a)</td><td>1640.03 (n/a)</td><td>1595.52 (n/a)</td><td>27.41 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>1.17 (+15.54%)</td><td>0.91 (-0.52%)</td><td>0.92 (-7.16%)</td><td>0.67 (+12.10%)</td><td>0.18 (-0.42%)</td><td>327.90 (-10.78%)</td><td>250.20 (-0.49%)</td><td>240.30 (+7.71%)</td><td>189.20 (-13.45%)</td><td>49.92 <b>(-23.24%)</b></td><td>49.87 (+15.54%)</td><td>38.89 (-0.52%)</td><td>39.27 (-7.16%)</td><td>28.78 (+12.10%)</td><td>7.51 (-0.42%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>1.01 (n/a)</td><td>0.92 (n/a)</td><td>0.99 (n/a)</td><td>0.60 (n/a)</td><td>0.18 (n/a)</td><td>367.50 (n/a)</td><td>251.42 (n/a)</td><td>223.10 (n/a)</td><td>218.60 (n/a)</td><td>65.03 (n/a)</td><td>43.16 (n/a)</td><td>39.09 (n/a)</td><td>42.30 (n/a)</td><td>25.68 (n/a)</td><td>7.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>1.24 (+17.43%)</td><td>1.02 <b>(+23.87%)</b></td><td>1.12 <b>(+27.46%)</b></td><td>0.63 (+5.10%)</td><td>0.26 <b>(+30.93%)</b></td><td>352.70 (-4.83%)</td><td>231.20 (-17.95%)</td><td>197.70 <b>(-21.52%)</b></td><td>178.40 (-14.84%)</td><td>73.26 (+2.81%)</td><td>52.90 (+17.43%)</td><td>43.59 <b>(+23.87%)</b></td><td>47.74 <b>(+27.46%)</b></td><td>26.76 (+5.10%)</td><td>11.08 <b>(+30.93%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>1.06 (n/a)</td><td>0.82 (n/a)</td><td>0.88 (n/a)</td><td>0.60 (n/a)</td><td>0.20 (n/a)</td><td>370.60 (n/a)</td><td>281.78 (n/a)</td><td>251.90 (n/a)</td><td>209.50 (n/a)</td><td>71.26 (n/a)</td><td>45.05 (n/a)</td><td>35.19 (n/a)</td><td>37.46 (n/a)</td><td>25.46 (n/a)</td><td>8.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.52 (-0.02%)</td><td>0.52 (+0.06%)</td><td>0.52 (-0.01%)</td><td>0.52 (+0.28%)</td><td>0.00 <b>(-65.46%)</b></td><td>48708.10 (-0.28%)</td><td>48660.46 (-0.06%)</td><td>48652.40 (+0.01%)</td><td>48628.80 (+0.02%)</td><td>32.56 <b>(-65.56%)</b></td><td>353.29 (-0.02%)</td><td>353.06 (+0.06%)</td><td>353.11 (-0.01%)</td><td>352.71 (+0.28%)</td><td>0.24 <b>(-65.46%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48846.00 (n/a)</td><td>48691.90 (n/a)</td><td>48647.20 (n/a)</td><td>48620.40 (n/a)</td><td>94.55 (n/a)</td><td>353.35 (n/a)</td><td>352.83 (n/a)</td><td>353.15 (n/a)</td><td>351.71 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.90 (-0.20%)</td><td>0.89 (-0.13%)</td><td>0.89 (-0.09%)</td><td>0.88 (-0.56%)</td><td>0.01 <b>(+23.32%)</b></td><td>28541.20 (+0.57%)</td><td>28216.58 (+0.13%)</td><td>28268.60 (+0.09%)</td><td>27947.70 (+0.20%)</td><td>242.83 <b>(+24.20%)</b></td><td>614.71 (-0.20%)</td><td>608.89 (-0.13%)</td><td>607.74 (-0.09%)</td><td>601.93 (-0.56%)</td><td>5.23 <b>(+23.32%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28380.80 (n/a)</td><td>28180.52 (n/a)</td><td>28244.20 (n/a)</td><td>27891.40 (n/a)</td><td>195.51 (n/a)</td><td>615.96 (n/a)</td><td>609.66 (n/a)</td><td>608.26 (n/a)</td><td>605.33 (n/a)</td><td>4.25 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>3.34 (+0.81%)</td><td>3.26 (+1.07%)</td><td>3.29 (+2.40%)</td><td>3.15 (-0.12%)</td><td>0.08 (+9.38%)</td><td>7982.20 (+0.13%)</td><td>7715.78 (-1.06%)</td><td>7637.80 (-2.34%)</td><td>7523.60 (-0.80%)</td><td>183.90 (+8.66%)</td><td>2283.46 (+0.81%)</td><td>2227.60 (+1.07%)</td><td>2249.32 (+2.40%)</td><td>2152.28 (-0.12%)</td><td>52.54 (+9.39%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>3.32 (n/a)</td><td>3.23 (n/a)</td><td>3.22 (n/a)</td><td>3.16 (n/a)</td><td>0.07 (n/a)</td><td>7972.20 (n/a)</td><td>7798.12 (n/a)</td><td>7820.80 (n/a)</td><td>7584.60 (n/a)</td><td>169.25 (n/a)</td><td>2265.09 (n/a)</td><td>2203.91 (n/a)</td><td>2196.70 (n/a)</td><td>2154.97 (n/a)</td><td>48.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>3.93 (-4.60%)</td><td>3.56 (+1.27%)</td><td>3.66 (+3.11%)</td><td>3.03 (+3.55%)</td><td>0.33 <b>(-21.97%)</b></td><td>2657.50 (-3.43%)</td><td>2281.20 (-1.69%)</td><td>2202.80 (-3.02%)</td><td>2051.50 (+4.82%)</td><td>227.65 <b>(-20.00%)</b></td><td>1030.43 (-4.60%)</td><td>933.56 (+1.27%)</td><td>959.64 (+3.11%)</td><td>795.46 (+3.55%)</td><td>86.65 <b>(-21.97%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>4.12 (n/a)</td><td>3.52 (n/a)</td><td>3.55 (n/a)</td><td>2.93 (n/a)</td><td>0.42 (n/a)</td><td>2751.90 (n/a)</td><td>2320.34 (n/a)</td><td>2271.40 (n/a)</td><td>1957.20 (n/a)</td><td>284.56 (n/a)</td><td>1080.08 (n/a)</td><td>921.84 (n/a)</td><td>930.66 (n/a)</td><td>768.16 (n/a)</td><td>111.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.45 <b>(+28.21%)</b></td><td>0.34 (+4.60%)</td><td>0.32 (-1.74%)</td><td>0.29 (-7.82%)</td><td>0.06 <b>(+333.49%)</b></td><td>4352.30 (+8.48%)</td><td>3722.90 (-2.18%)</td><td>3873.20 (+1.77%)</td><td>2789.00 <b>(-22.01%)</b></td><td>611.60 <b>(+261.61%)</b></td><td>24.06 <b>(+28.21%)</b></td><td>18.47 (+4.60%)</td><td>17.33 (-1.74%)</td><td>15.42 (-7.82%)</td><td>3.43 <b>(+333.49%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.01 (n/a)</td><td>4012.10 (n/a)</td><td>3805.94 (n/a)</td><td>3806.00 (n/a)</td><td>3575.90 (n/a)</td><td>169.13 (n/a)</td><td>18.77 (n/a)</td><td>17.66 (n/a)</td><td>17.63 (n/a)</td><td>16.73 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>5.46 (-18.57%)</td><td>4.04 (-17.64%)</td><td>3.50 <b>(-27.69%)</b></td><td>3.16 (-12.52%)</td><td>0.99 (-11.77%)</td><td>2101.90 (+14.32%)</td><td>1722.70 <b>(+22.06%)</b></td><td>1899.20 <b>(+38.28%)</b></td><td>1218.30 <b>(+22.81%)</b></td><td>382.96 <b>(+26.58%)</b></td><td>1686.98 (-18.57%)</td><td>1247.29 (-17.64%)</td><td>1082.13 <b>(-27.69%)</b></td><td>977.81 (-12.52%)</td><td>307.06 (-11.77%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>6.71 (n/a)</td><td>4.90 (n/a)</td><td>4.84 (n/a)</td><td>3.62 (n/a)</td><td>1.13 (n/a)</td><td>1838.60 (n/a)</td><td>1411.38 (n/a)</td><td>1373.40 (n/a)</td><td>992.00 (n/a)</td><td>302.55 (n/a)</td><td>2071.77 (n/a)</td><td>1514.35 (n/a)</td><td>1496.43 (n/a)</td><td>1117.80 (n/a)</td><td>348.02 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>13.39 (n/a)</td><td>12.28 (n/a)</td><td>11.73 (n/a)</td><td>11.23 (n/a)</td><td>1.01 (n/a)</td><td>13.39 (n/a)</td><td>12.28 (n/a)</td><td>11.73 (n/a)</td><td>11.22 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>24.63 (-1.48%)</td><td>24.20 (-0.58%)</td><td>24.16 (+0.02%)</td><td>23.64 (+0.07%)</td><td>0.40 <b>(-29.30%)</b></td><td>24.61 (-1.48%)</td><td>24.19 (-0.58%)</td><td>24.14 (+0.02%)</td><td>23.63 (+0.07%)</td><td>0.40 <b>(-29.30%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>25.00 (n/a)</td><td>24.34 (n/a)</td><td>24.15 (n/a)</td><td>23.62 (n/a)</td><td>0.56 (n/a)</td><td>24.98 (n/a)</td><td>24.33 (n/a)</td><td>24.14 (n/a)</td><td>23.61 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>40.79 (+1.66%)</td><td>39.63 (+1.49%)</td><td>39.79 (+0.77%)</td><td>37.48 (+1.37%)</td><td>1.27 (-3.39%)</td><td>40.77 (+1.66%)</td><td>39.61 (+1.49%)</td><td>39.76 (+0.77%)</td><td>37.46 (+1.37%)</td><td>1.27 (-3.39%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>40.13 (n/a)</td><td>39.05 (n/a)</td><td>39.48 (n/a)</td><td>36.97 (n/a)</td><td>1.32 (n/a)</td><td>40.10 (n/a)</td><td>39.02 (n/a)</td><td>39.46 (n/a)</td><td>36.95 (n/a)</td><td>1.32 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>43.58 (-4.33%)</td><td>42.62 (-0.85%)</td><td>42.76 (+0.05%)</td><td>41.74 (+4.96%)</td><td>0.83 <b>(-66.24%)</b></td><td>43.55 (-4.33%)</td><td>42.60 (-0.85%)</td><td>42.74 (+0.05%)</td><td>41.71 (+4.96%)</td><td>0.83 <b>(-66.24%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>45.55 (n/a)</td><td>42.99 (n/a)</td><td>42.74 (n/a)</td><td>39.77 (n/a)</td><td>2.45 (n/a)</td><td>45.52 (n/a)</td><td>42.96 (n/a)</td><td>42.71 (n/a)</td><td>39.74 (n/a)</td><td>2.45 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>13.17 (n/a)</td><td>12.48 (n/a)</td><td>12.35 (n/a)</td><td>11.64 (n/a)</td><td>0.67 (n/a)</td><td>13.16 (n/a)</td><td>12.47 (n/a)</td><td>12.35 (n/a)</td><td>11.63 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>24.94 (-0.11%)</td><td>23.97 (-1.26%)</td><td>23.85 (-1.31%)</td><td>23.07 (-2.64%)</td><td>0.68 (+19.36%)</td><td>24.92 (-0.11%)</td><td>23.95 (-1.26%)</td><td>23.83 (-1.31%)</td><td>23.06 (-2.64%)</td><td>0.68 (+19.36%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>24.96 (n/a)</td><td>24.27 (n/a)</td><td>24.17 (n/a)</td><td>23.70 (n/a)</td><td>0.57 (n/a)</td><td>24.95 (n/a)</td><td>24.26 (n/a)</td><td>24.15 (n/a)</td><td>23.69 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>43.23 (+2.84%)</td><td>39.68 (+2.07%)</td><td>38.98 (-2.39%)</td><td>38.19 (+16.67%)</td><td>2.03 <b>(-43.33%)</b></td><td>43.21 (+2.84%)</td><td>39.66 (+2.07%)</td><td>38.95 (-2.39%)</td><td>38.16 (+16.67%)</td><td>2.03 <b>(-43.33%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>42.04 (n/a)</td><td>38.88 (n/a)</td><td>39.93 (n/a)</td><td>32.73 (n/a)</td><td>3.58 (n/a)</td><td>42.01 (n/a)</td><td>38.85 (n/a)</td><td>39.91 (n/a)</td><td>32.71 (n/a)</td><td>3.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>44.33 (-1.34%)</td><td>42.36 (+3.23%)</td><td>42.51 (+0.08%)</td><td>40.36 (+18.46%)</td><td>1.88 <b>(-54.73%)</b></td><td>44.30 (-1.34%)</td><td>42.34 (+3.23%)</td><td>42.48 (+0.08%)</td><td>40.33 (+18.46%)</td><td>1.88 <b>(-54.73%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>44.93 (n/a)</td><td>41.04 (n/a)</td><td>42.47 (n/a)</td><td>34.07 (n/a)</td><td>4.16 (n/a)</td><td>44.90 (n/a)</td><td>41.01 (n/a)</td><td>42.45 (n/a)</td><td>34.05 (n/a)</td><td>4.15 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>9.90 (+9.46%)</td><td>8.80 (-0.32%)</td><td>8.78 (-1.03%)</td><td>8.19 (-4.97%)</td><td>0.69 <b>(+306.80%)</b></td><td>9.88 (+9.46%)</td><td>8.78 (-0.32%)</td><td>8.76 (-1.03%)</td><td>8.17 (-4.97%)</td><td>0.69 <b>(+306.80%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>9.05 (n/a)</td><td>8.83 (n/a)</td><td>8.87 (n/a)</td><td>8.62 (n/a)</td><td>0.17 (n/a)</td><td>9.03 (n/a)</td><td>8.81 (n/a)</td><td>8.85 (n/a)</td><td>8.60 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.92 (+5.04%)</td><td>0.81 (+3.73%)</td><td>0.77 (-0.55%)</td><td>0.71 (+4.63%)</td><td>0.09 (+18.14%)</td><td>0.90 (+5.04%)</td><td>0.80 (+3.73%)</td><td>0.76 (-0.55%)</td><td>0.70 (+4.63%)</td><td>0.09 (+18.14%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.87 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.68 (n/a)</td><td>0.07 (n/a)</td><td>0.86 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.67 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>1.26 (+18.31%)</td><td>1.07 (+4.50%)</td><td>0.97 (-5.13%)</td><td>0.94 (-3.75%)</td><td>0.16 <b>(+314.33%)</b></td><td>1.25 (+18.31%)</td><td>1.06 (+4.50%)</td><td>0.96 (-5.13%)</td><td>0.93 (-3.75%)</td><td>0.16 <b>(+314.33%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>1.06 (n/a)</td><td>1.03 (n/a)</td><td>1.03 (n/a)</td><td>0.97 (n/a)</td><td>0.04 (n/a)</td><td>1.05 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td><td>0.96 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>16.22 (+0.79%)</td><td>14.82 (-0.75%)</td><td>14.62 (-2.28%)</td><td>13.66 (-2.53%)</td><td>0.95 <b>(+24.02%)</b></td><td>16.03 (+0.79%)</td><td>14.64 (-0.75%)</td><td>14.45 (-2.28%)</td><td>13.51 (-2.53%)</td><td>0.94 <b>(+24.02%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>16.09 (n/a)</td><td>14.93 (n/a)</td><td>14.96 (n/a)</td><td>14.02 (n/a)</td><td>0.76 (n/a)</td><td>15.91 (n/a)</td><td>14.75 (n/a)</td><td>14.79 (n/a)</td><td>13.86 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>11.88 (-0.84%)</td><td>11.46 (+0.72%)</td><td>11.71 (-0.86%)</td><td>10.31 (+9.60%)</td><td>0.65 <b>(-40.76%)</b></td><td>11.67 (-0.84%)</td><td>11.26 (+0.72%)</td><td>11.50 (-0.86%)</td><td>10.13 (+9.60%)</td><td>0.64 <b>(-40.76%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>11.98 (n/a)</td><td>11.37 (n/a)</td><td>11.81 (n/a)</td><td>9.41 (n/a)</td><td>1.10 (n/a)</td><td>11.77 (n/a)</td><td>11.17 (n/a)</td><td>11.60 (n/a)</td><td>9.25 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>8.40 (-8.23%)</td><td>7.30 (-6.12%)</td><td>7.34 (-1.66%)</td><td>6.04 (-9.75%)</td><td>0.98 (+6.85%)</td><td>8.25 (-8.23%)</td><td>7.17 (-6.12%)</td><td>7.21 (-1.66%)</td><td>5.94 (-9.75%)</td><td>0.97 (+6.85%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>9.15 (n/a)</td><td>7.77 (n/a)</td><td>7.46 (n/a)</td><td>6.70 (n/a)</td><td>0.92 (n/a)</td><td>8.99 (n/a)</td><td>7.64 (n/a)</td><td>7.33 (n/a)</td><td>6.58 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>6.80 (-2.13%)</td><td>5.49 (-8.91%)</td><td>5.34 (-11.46%)</td><td>4.75 (-12.13%)</td><td>0.83 <b>(+38.64%)</b></td><td>6.69 (-2.13%)</td><td>5.40 (-8.91%)</td><td>5.25 (-11.46%)</td><td>4.68 (-12.13%)</td><td>0.82 <b>(+38.64%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>6.95 (n/a)</td><td>6.02 (n/a)</td><td>6.03 (n/a)</td><td>5.41 (n/a)</td><td>0.60 (n/a)</td><td>6.83 (n/a)</td><td>5.93 (n/a)</td><td>5.93 (n/a)</td><td>5.32 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>13.39 (n/a)</td><td>12.44 (n/a)</td><td>12.51 (n/a)</td><td>11.69 (n/a)</td><td>0.68 (n/a)</td><td>13.38 (n/a)</td><td>12.43 (n/a)</td><td>12.50 (n/a)</td><td>11.68 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>13.24 (n/a)</td><td>11.66 (n/a)</td><td>11.65 (n/a)</td><td>10.69 (n/a)</td><td>1.00 (n/a)</td><td>13.23 (n/a)</td><td>11.66 (n/a)</td><td>11.65 (n/a)</td><td>10.68 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>175.90 (n/a)</td><td>165.96 (n/a)</td><td>166.50 (n/a)</td><td>155.50 (n/a)</td><td>9.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.80 (n/a)</td><td>179.88 (n/a)</td><td>182.90 (n/a)</td><td>131.00 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.50 (n/a)</td><td>199.22 (n/a)</td><td>197.60 (n/a)</td><td>177.00 (n/a)</td><td>23.23 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>187.50 (n/a)</td><td>187.00 (n/a)</td><td>153.60 (n/a)</td><td>26.98 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.80 (n/a)</td><td>186.34 (n/a)</td><td>194.20 (n/a)</td><td>155.70 (n/a)</td><td>28.20 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.60 (n/a)</td><td>199.12 (n/a)</td><td>192.30 (n/a)</td><td>168.10 (n/a)</td><td>29.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>223.80 (n/a)</td><td>197.54 (n/a)</td><td>197.80 (n/a)</td><td>174.10 (n/a)</td><td>21.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.60 (n/a)</td><td>208.16 (n/a)</td><td>213.30 (n/a)</td><td>179.40 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 <b>(-20.18%)</b></td><td>0.06 (+9.18%)</td><td>0.06 <b>(+27.29%)</b></td><td>0.05 (+9.37%)</td><td>0.01 <b>(-62.64%)</b></td><td>167.10 (-8.54%)</td><td>141.44 (-11.79%)</td><td>137.20 <b>(-21.42%)</b></td><td>129.30 <b>(+25.29%)</b></td><td>14.75 <b>(-54.92%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.70 (n/a)</td><td>160.34 (n/a)</td><td>174.60 (n/a)</td><td>103.20 (n/a)</td><td>32.73 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.07 <b>(+21.39%)</b></td><td>0.04 (-8.56%)</td><td>0.04 <b>(-21.58%)</b></td><td>0.02 <b>(-38.14%)</b></td><td>0.02 <b>(+105.96%)</b></td><td>379.00 <b>(+61.62%)</b></td><td>215.16 <b>(+23.24%)</b></td><td>199.20 <b>(+27.45%)</b></td><td>122.80 (-17.58%)</td><td>100.32 <b>(+178.47%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.50 (n/a)</td><td>174.58 (n/a)</td><td>156.30 (n/a)</td><td>149.00 (n/a)</td><td>36.03 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (-0.50%)</td><td>0.05 (-17.63%)</td><td>0.04 <b>(-28.19%)</b></td><td>0.03 <b>(-32.90%)</b></td><td>0.01 <b>(+94.41%)</b></td><td>249.90 <b>(+49.02%)</b></td><td>189.30 <b>(+25.70%)</b></td><td>199.40 <b>(+39.25%)</b></td><td>136.60 (+0.52%)</td><td>43.32 <b>(+183.35%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>167.70 (n/a)</td><td>150.60 (n/a)</td><td>143.20 (n/a)</td><td>135.90 (n/a)</td><td>15.29 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (+1.82%)</td><td>0.04 (-8.60%)</td><td>0.04 (-14.64%)</td><td>0.02 (-10.09%)</td><td>0.01 (+0.50%)</td><td>351.00 (+11.22%)</td><td>215.26 (+10.40%)</td><td>192.40 (+17.17%)</td><td>154.10 (-1.78%)</td><td>78.04 (+14.60%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>315.60 (n/a)</td><td>194.98 (n/a)</td><td>164.20 (n/a)</td><td>156.90 (n/a)</td><td>68.10 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (-12.97%)</td><td>0.05 (-2.60%)</td><td>0.05 (-1.25%)</td><td>0.04 (+1.19%)</td><td>0.01 <b>(-41.22%)</b></td><td>185.40 (-1.17%)</td><td>164.40 (+1.29%)</td><td>169.80 (+1.31%)</td><td>139.30 (+14.93%)</td><td>17.15 <b>(-32.05%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.60 (n/a)</td><td>162.30 (n/a)</td><td>167.60 (n/a)</td><td>121.20 (n/a)</td><td>25.24 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 <b>(-24.91%)</b></td><td>0.04 (-13.46%)</td><td>0.04 (-16.00%)</td><td>0.04 (+5.32%)</td><td>0.00 <b>(-83.67%)</b></td><td>201.50 (-5.04%)</td><td>190.16 (+11.90%)</td><td>188.30 (+19.03%)</td><td>182.30 <b>(+33.16%)</b></td><td>7.29 <b>(-79.28%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>169.94 (n/a)</td><td>158.20 (n/a)</td><td>136.90 (n/a)</td><td>35.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (-11.94%)</td><td>0.04 (-11.75%)</td><td>0.04 (-11.88%)</td><td>0.02 <b>(-33.91%)</b></td><td>0.01 (+9.52%)</td><td>339.30 <b>(+51.34%)</b></td><td>216.38 (+17.00%)</td><td>188.30 (+13.50%)</td><td>165.10 (+13.55%)</td><td>69.93 <b>(+91.27%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>184.94 (n/a)</td><td>165.90 (n/a)</td><td>145.40 (n/a)</td><td>36.56 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 <b>(-23.02%)</b></td><td>0.04 (-13.34%)</td><td>0.04 (-9.17%)</td><td>0.03 (-16.40%)</td><td>0.00 <b>(-41.70%)</b></td><td>237.40 (+19.66%)</td><td>205.36 (+14.82%)</td><td>198.40 (+10.10%)</td><td>190.30 <b>(+29.90%)</b></td><td>18.73 (-6.54%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.40 (n/a)</td><td>178.86 (n/a)</td><td>180.20 (n/a)</td><td>146.50 (n/a)</td><td>20.04 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (-4.75%)</td><td>0.04 (-9.63%)</td><td>0.04 (-8.03%)</td><td>0.04 (-17.30%)</td><td>0.01 <b>(+22.24%)</b></td><td>221.00 <b>(+20.90%)</b></td><td>189.28 (+11.25%)</td><td>193.90 (+8.75%)</td><td>161.20 (+5.02%)</td><td>22.54 <b>(+55.30%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>182.80 (n/a)</td><td>170.14 (n/a)</td><td>178.30 (n/a)</td><td>153.50 (n/a)</td><td>14.51 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (-7.93%)</td><td>0.04 (+3.51%)</td><td>0.04 (+2.43%)</td><td>0.03 (-0.78%)</td><td>0.01 <b>(-21.79%)</b></td><td>317.50 (+0.79%)</td><td>227.42 (-4.73%)</td><td>209.20 (-2.38%)</td><td>194.20 (+8.61%)</td><td>50.75 (-12.57%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>315.00 (n/a)</td><td>238.72 (n/a)</td><td>214.30 (n/a)</td><td>178.80 (n/a)</td><td>58.04 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (-13.78%)</td><td>0.05 (-2.92%)</td><td>0.05 (-4.47%)</td><td>0.04 (-5.31%)</td><td>0.01 <b>(-20.31%)</b></td><td>205.60 (+5.60%)</td><td>171.08 (+2.41%)</td><td>179.70 (+4.66%)</td><td>139.50 (+15.96%)</td><td>27.97 (-1.17%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>167.06 (n/a)</td><td>171.70 (n/a)</td><td>120.30 (n/a)</td><td>28.31 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 <b>(+44.50%)</b></td><td>0.04 (+12.55%)</td><td>0.04 (+10.89%)</td><td>0.03 (+1.41%)</td><td>0.01 <b>(+189.08%)</b></td><td>252.50 (-1.41%)</td><td>205.04 (-7.14%)</td><td>196.60 (-9.82%)</td><td>134.00 <b>(-30.79%)</b></td><td>49.40 <b>(+101.33%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>256.10 (n/a)</td><td>220.80 (n/a)</td><td>218.00 (n/a)</td><td>193.60 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 <b>(-24.14%)</b></td><td>0.04 (-13.45%)</td><td>0.04 (-18.34%)</td><td>0.03 (+3.99%)</td><td>0.01 <b>(-53.26%)</b></td><td>249.90 (-3.81%)</td><td>198.32 (+9.98%)</td><td>190.10 <b>(+22.49%)</b></td><td>161.80 <b>(+31.87%)</b></td><td>32.38 <b>(-40.78%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.80 (n/a)</td><td>180.32 (n/a)</td><td>155.20 (n/a)</td><td>122.70 (n/a)</td><td>54.68 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (-7.18%)</td><td>0.05 (-7.94%)</td><td>0.05 (-9.02%)</td><td>0.05 (-6.76%)</td><td>0.01 (-10.88%)</td><td>181.90 (+7.25%)</td><td>156.36 (+8.45%)</td><td>156.90 (+9.87%)</td><td>128.10 (+7.74%)</td><td>22.26 (+2.87%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.60 (n/a)</td><td>144.18 (n/a)</td><td>142.80 (n/a)</td><td>118.90 (n/a)</td><td>21.64 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.07 (+16.57%)</td><td>0.05 (+5.56%)</td><td>0.05 (+3.68%)</td><td>0.04 (-2.09%)</td><td>0.01 <b>(+69.15%)</b></td><td>197.30 (+2.12%)</td><td>161.18 (-3.61%)</td><td>166.00 (-3.60%)</td><td>119.60 (-14.27%)</td><td>29.56 <b>(+47.43%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>167.22 (n/a)</td><td>172.20 (n/a)</td><td>139.50 (n/a)</td><td>20.05 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (-13.72%)</td><td>0.04 (-7.40%)</td><td>0.04 (-7.84%)</td><td>0.04 (+2.65%)</td><td>0.00 <b>(-41.47%)</b></td><td>205.90 (-2.60%)</td><td>184.98 (+6.69%)</td><td>182.40 (+8.51%)</td><td>163.80 (+15.84%)</td><td>18.35 <b>(-33.66%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>173.38 (n/a)</td><td>168.10 (n/a)</td><td>141.40 (n/a)</td><td>27.66 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (-19.93%)</td><td>0.04 (+0.20%)</td><td>0.04 (+8.74%)</td><td>0.04 (+6.90%)</td><td>0.00 <b>(-65.47%)</b></td><td>210.00 (-6.46%)</td><td>187.34 (-2.80%)</td><td>184.40 (-8.08%)</td><td>171.50 <b>(+24.82%)</b></td><td>14.36 <b>(-58.41%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.50 (n/a)</td><td>192.74 (n/a)</td><td>200.60 (n/a)</td><td>137.40 (n/a)</td><td>34.53 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (-8.66%)</td><td>0.04 (-5.77%)</td><td>0.04 (-4.03%)</td><td>0.03 (-10.86%)</td><td>0.01 (+1.38%)</td><td>240.40 (+12.18%)</td><td>197.72 (+6.46%)</td><td>190.20 (+4.22%)</td><td>171.50 (+9.51%)</td><td>27.00 <b>(+25.98%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>185.72 (n/a)</td><td>182.50 (n/a)</td><td>156.60 (n/a)</td><td>21.43 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.21 (+0.11%)</td><td>0.21 (-0.03%)</td><td>0.21 (-0.05%)</td><td>0.21 (-0.02%)</td><td>0.00 (+17.75%)</td><td>40898.10 (+0.02%)</td><td>40766.32 (+0.03%)</td><td>40842.20 (+0.05%)</td><td>40417.80 (-0.11%)</td><td>201.12 (+17.68%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40891.30 (n/a)</td><td>40753.60 (n/a)</td><td>40821.50 (n/a)</td><td>40461.90 (n/a)</td><td>170.90 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 <b>(-23.40%)</b></td><td>0.04 (-12.07%)</td><td>0.04 (-7.63%)</td><td>0.04 (+11.06%)</td><td>0.01 <b>(-56.28%)</b></td><td>221.10 (-9.98%)</td><td>188.48 (+9.43%)</td><td>185.40 (+8.29%)</td><td>166.20 <b>(+30.56%)</b></td><td>22.87 <b>(-49.83%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.60 (n/a)</td><td>172.24 (n/a)</td><td>171.20 (n/a)</td><td>127.30 (n/a)</td><td>45.58 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.09 (+10.20%)</td><td>0.07 (-9.72%)</td><td>0.07 (-18.37%)</td><td>0.06 (-3.91%)</td><td>0.01 <b>(+50.59%)</b></td><td>201.50 (+4.03%)</td><td>180.14 (+12.22%)</td><td>185.80 <b>(+22.48%)</b></td><td>131.00 (-9.22%)</td><td>28.78 <b>(+39.71%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>160.52 (n/a)</td><td>151.70 (n/a)</td><td>144.30 (n/a)</td><td>20.60 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 <b>(-26.51%)</b></td><td>0.04 (-13.18%)</td><td>0.04 (-19.12%)</td><td>0.03 <b>(+21.88%)</b></td><td>0.00 <b>(-68.21%)</b></td><td>239.20 (-17.97%)</td><td>201.22 (+6.74%)</td><td>197.60 <b>(+23.65%)</b></td><td>177.70 <b>(+36.06%)</b></td><td>23.73 <b>(-64.28%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>291.60 (n/a)</td><td>188.52 (n/a)</td><td>159.80 (n/a)</td><td>130.60 (n/a)</td><td>66.42 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.08 (+9.44%)</td><td>0.06 (+8.00%)</td><td>0.05 (-3.92%)</td><td>0.04 (+10.84%)</td><td>0.01 (+11.21%)</td><td>231.20 (-9.76%)</td><td>180.20 (-7.40%)</td><td>190.80 (+4.09%)</td><td>133.90 (-8.60%)</td><td>38.06 (-10.50%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>256.20 (n/a)</td><td>194.60 (n/a)</td><td>183.30 (n/a)</td><td>146.50 (n/a)</td><td>42.52 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (-0.18%)</td><td>0.05 (+0.67%)</td><td>0.04 (-2.75%)</td><td>0.04 (+15.09%)</td><td>0.01 (-3.42%)</td><td>212.10 (-13.11%)</td><td>183.76 (-1.17%)</td><td>189.60 (+2.88%)</td><td>149.00 (+0.20%)</td><td>29.94 (-16.82%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.10 (n/a)</td><td>185.94 (n/a)</td><td>184.30 (n/a)</td><td>148.70 (n/a)</td><td>36.00 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.07 (-17.53%)</td><td>0.06 (-2.20%)</td><td>0.06 (+3.20%)</td><td>0.05 (+10.11%)</td><td>0.01 <b>(-45.16%)</b></td><td>194.10 (-9.17%)</td><td>170.80 (+0.04%)</td><td>170.90 (-3.12%)</td><td>149.30 <b>(+21.19%)</b></td><td>20.41 <b>(-38.52%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>170.74 (n/a)</td><td>176.40 (n/a)</td><td>123.20 (n/a)</td><td>33.19 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 <b>(+20.24%)</b></td><td>0.04 (-1.58%)</td><td>0.04 (-10.12%)</td><td>0.04 (-6.93%)</td><td>0.01 <b>(+125.33%)</b></td><td>221.30 (+7.43%)</td><td>194.22 (+4.79%)</td><td>211.90 (+11.23%)</td><td>128.90 (-16.84%)</td><td>37.71 <b>(+100.09%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.00 (n/a)</td><td>185.34 (n/a)</td><td>190.50 (n/a)</td><td>155.00 (n/a)</td><td>18.85 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (-4.55%)</td><td>0.05 (-13.54%)</td><td>0.04 (-13.87%)</td><td>0.04 (-17.53%)</td><td>0.01 <b>(+24.26%)</b></td><td>236.20 <b>(+21.25%)</b></td><td>203.78 (+17.41%)</td><td>217.50 (+16.06%)</td><td>148.80 (+4.79%)</td><td>37.49 <b>(+58.79%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>173.56 (n/a)</td><td>187.40 (n/a)</td><td>142.00 (n/a)</td><td>23.61 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (-1.65%)</td><td>0.04 (+4.48%)</td><td>0.04 (+2.78%)</td><td>0.04 (+15.17%)</td><td>0.01 (-18.10%)</td><td>226.60 (-13.15%)</td><td>186.30 (-5.63%)</td><td>185.80 (-2.67%)</td><td>147.00 (+1.66%)</td><td>30.14 <b>(-28.05%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.90 (n/a)</td><td>197.42 (n/a)</td><td>190.90 (n/a)</td><td>144.60 (n/a)</td><td>41.89 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (-17.06%)</td><td>0.04 (-17.73%)</td><td>0.04 <b>(-22.05%)</b></td><td>0.03 (-10.32%)</td><td>0.01 <b>(-31.28%)</b></td><td>314.90 (+11.51%)</td><td>222.20 (+19.08%)</td><td>207.70 <b>(+28.29%)</b></td><td>174.90 <b>(+20.62%)</b></td><td>54.76 (-4.38%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>282.40 (n/a)</td><td>186.60 (n/a)</td><td>161.90 (n/a)</td><td>145.00 (n/a)</td><td>57.27 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (-2.94%)</td><td>0.04 (+6.98%)</td><td>0.04 (+5.01%)</td><td>0.04 <b>(+27.03%)</b></td><td>0.00 <b>(-45.32%)</b></td><td>213.80 <b>(-21.28%)</b></td><td>190.40 (-8.84%)</td><td>183.10 (-4.78%)</td><td>167.60 (+3.01%)</td><td>19.40 <b>(-55.61%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>271.60 (n/a)</td><td>208.86 (n/a)</td><td>192.30 (n/a)</td><td>162.70 (n/a)</td><td>43.69 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (+3.63%)</td><td>0.04 (-5.25%)</td><td>0.04 (+1.45%)</td><td>0.03 (-14.90%)</td><td>0.01 <b>(+91.94%)</b></td><td>303.50 (+17.50%)</td><td>234.76 (+8.54%)</td><td>207.10 (-1.43%)</td><td>187.80 (-3.49%)</td><td>52.23 <b>(+113.23%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>258.30 (n/a)</td><td>216.28 (n/a)</td><td>210.10 (n/a)</td><td>194.60 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (+5.40%)</td><td>0.04 (-5.74%)</td><td>0.04 (-4.55%)</td><td>0.02 <b>(-33.16%)</b></td><td>0.01 <b>(+72.76%)</b></td><td>327.90 <b>(+49.59%)</b></td><td>211.96 (+12.29%)</td><td>193.10 (+4.77%)</td><td>145.20 (-5.16%)</td><td>70.67 <b>(+147.21%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.20 (n/a)</td><td>188.76 (n/a)</td><td>184.30 (n/a)</td><td>153.10 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 <b>(-24.02%)</b></td><td>0.04 (-17.12%)</td><td>0.04 (-8.54%)</td><td>0.02 <b>(-28.35%)</b></td><td>0.01 (-1.23%)</td><td>351.10 <b>(+39.55%)</b></td><td>248.02 <b>(+22.64%)</b></td><td>216.20 (+9.36%)</td><td>211.90 <b>(+31.61%)</b></td><td>59.40 <b>(+81.17%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.60 (n/a)</td><td>202.24 (n/a)</td><td>197.70 (n/a)</td><td>161.00 (n/a)</td><td>32.79 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (-15.60%)</td><td>0.04 (-2.14%)</td><td>0.04 (-7.02%)</td><td>0.04 <b>(+69.66%)</b></td><td>0.00 <b>(-92.01%)</b></td><td>228.90 <b>(-41.07%)</b></td><td>223.00 (-5.33%)</td><td>223.80 (+7.54%)</td><td>216.20 (+18.47%)</td><td>4.60 <b>(-94.66%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>388.40 (n/a)</td><td>235.56 (n/a)</td><td>208.10 (n/a)</td><td>182.50 (n/a)</td><td>86.26 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.63 (-9.90%)</td><td>0.54 (+2.10%)</td><td>0.53 (+4.00%)</td><td>0.45 (+18.94%)</td><td>0.08 <b>(-35.65%)</b></td><td>220.10 (-15.93%)</td><td>186.16 (-4.49%)</td><td>185.50 (-3.84%)</td><td>156.00 (+11.03%)</td><td>26.85 <b>(-40.34%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.70 (n/a)</td><td>0.53 (n/a)</td><td>0.51 (n/a)</td><td>0.38 (n/a)</td><td>0.12 (n/a)</td><td>261.80 (n/a)</td><td>194.92 (n/a)</td><td>192.90 (n/a)</td><td>140.50 (n/a)</td><td>45.00 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.66 (-17.04%)</td><td>0.54 (-15.02%)</td><td>0.54 (-16.42%)</td><td>0.45 (-9.23%)</td><td>0.08 <b>(-28.85%)</b></td><td>219.70 (+10.18%)</td><td>185.46 (+16.71%)</td><td>180.50 (+19.69%)</td><td>148.30 <b>(+20.57%)</b></td><td>26.50 (-6.47%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.80 (n/a)</td><td>0.63 (n/a)</td><td>0.65 (n/a)</td><td>0.49 (n/a)</td><td>0.11 (n/a)</td><td>199.40 (n/a)</td><td>158.90 (n/a)</td><td>150.80 (n/a)</td><td>123.00 (n/a)</td><td>28.33 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.83 <b>(+45.23%)</b></td><td>0.59 <b>(+23.90%)</b></td><td>0.54 (+5.88%)</td><td>0.48 <b>(+61.65%)</b></td><td>0.14 <b>(+23.58%)</b></td><td>204.50 <b>(-38.14%)</b></td><td>172.36 <b>(-21.03%)</b></td><td>182.30 (-5.54%)</td><td>118.10 <b>(-31.14%)</b></td><td>32.58 <b>(-50.44%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.57 (n/a)</td><td>0.48 (n/a)</td><td>0.51 (n/a)</td><td>0.30 (n/a)</td><td>0.11 (n/a)</td><td>330.60 (n/a)</td><td>218.26 (n/a)</td><td>193.00 (n/a)</td><td>171.50 (n/a)</td><td>65.74 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.69 (+7.93%)</td><td>0.53 (-2.77%)</td><td>0.48 (-7.04%)</td><td>0.36 <b>(-27.35%)</b></td><td>0.15 <b>(+144.94%)</b></td><td>275.40 <b>(+37.63%)</b></td><td>197.02 (+8.55%)</td><td>203.50 (+7.56%)</td><td>141.90 (-7.38%)</td><td>55.47 <b>(+200.12%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.64 (n/a)</td><td>0.55 (n/a)</td><td>0.52 (n/a)</td><td>0.49 (n/a)</td><td>0.06 (n/a)</td><td>200.10 (n/a)</td><td>181.50 (n/a)</td><td>189.20 (n/a)</td><td>153.20 (n/a)</td><td>18.48 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.44 (-18.14%)</td><td>0.35 <b>(-27.79%)</b></td><td>0.33 <b>(-34.15%)</b></td><td>0.31 (-18.41%)</td><td>0.05 (-11.56%)</td><td>239.30 <b>(+22.53%)</b></td><td>215.94 <b>(+38.71%)</b></td><td>226.30 <b>(+51.78%)</b></td><td>167.10 <b>(+22.15%)</b></td><td>28.97 <b>(+26.28%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>0.06 (n/a)</td><td>195.30 (n/a)</td><td>155.68 (n/a)</td><td>149.10 (n/a)</td><td>136.80 (n/a)</td><td>22.94 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.56 (+12.27%)</td><td>0.43 (+0.96%)</td><td>0.40 (-7.17%)</td><td>0.40 (+9.42%)</td><td>0.07 <b>(+47.01%)</b></td><td>185.50 (-8.62%)</td><td>172.98 (-0.15%)</td><td>184.80 (+7.69%)</td><td>130.60 (-10.91%)</td><td>23.83 (+18.62%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.36 (n/a)</td><td>0.05 (n/a)</td><td>203.00 (n/a)</td><td>173.24 (n/a)</td><td>171.60 (n/a)</td><td>146.60 (n/a)</td><td>20.09 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.54 (+17.58%)</td><td>0.46 (+14.44%)</td><td>0.45 (+11.32%)</td><td>0.39 (+5.53%)</td><td>0.06 <b>(+56.56%)</b></td><td>190.00 (-5.24%)</td><td>161.08 (-11.98%)</td><td>165.00 (-10.18%)</td><td>135.60 (-14.93%)</td><td>22.24 <b>(+22.58%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.46 (n/a)</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.37 (n/a)</td><td>0.04 (n/a)</td><td>200.50 (n/a)</td><td>183.00 (n/a)</td><td>183.70 (n/a)</td><td>159.40 (n/a)</td><td>18.14 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.52 (+8.69%)</td><td>0.40 (-3.69%)</td><td>0.37 (-13.17%)</td><td>0.35 (+12.14%)</td><td>0.07 (+9.23%)</td><td>208.60 (-10.82%)</td><td>189.82 (+3.76%)</td><td>201.80 (+15.18%)</td><td>141.80 (-7.98%)</td><td>27.78 (-12.38%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>233.90 (n/a)</td><td>182.94 (n/a)</td><td>175.20 (n/a)</td><td>154.10 (n/a)</td><td>31.71 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.84 <b>(-28.82%)</b></td><td>0.72 (-16.92%)</td><td>0.70 <b>(-23.00%)</b></td><td>0.66 <b>(+22.80%)</b></td><td>0.08 <b>(-67.38%)</b></td><td>199.10 (-18.57%)</td><td>183.20 (+13.58%)</td><td>187.90 <b>(+29.85%)</b></td><td>156.60 <b>(+40.45%)</b></td><td>18.15 <b>(-63.85%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>1.18 (n/a)</td><td>0.87 (n/a)</td><td>0.91 (n/a)</td><td>0.54 (n/a)</td><td>0.23 (n/a)</td><td>244.50 (n/a)</td><td>161.30 (n/a)</td><td>144.70 (n/a)</td><td>111.50 (n/a)</td><td>50.21 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.88 (-6.33%)</td><td>0.76 (-4.91%)</td><td>0.74 (-9.11%)</td><td>0.72 (+3.13%)</td><td>0.07 <b>(-33.16%)</b></td><td>181.80 (-3.04%)</td><td>173.12 (+4.50%)</td><td>178.30 (+10.06%)</td><td>149.50 (+6.79%)</td><td>13.32 <b>(-32.76%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.94 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.70 (n/a)</td><td>0.10 (n/a)</td><td>187.50 (n/a)</td><td>165.66 (n/a)</td><td>162.00 (n/a)</td><td>140.00 (n/a)</td><td>19.80 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.91 (+1.96%)</td><td>0.74 (-12.47%)</td><td>0.75 (-14.26%)</td><td>0.61 (-19.16%)</td><td>0.12 <b>(+115.15%)</b></td><td>216.00 <b>(+23.71%)</b></td><td>180.92 (+16.35%)</td><td>174.40 (+16.58%)</td><td>144.30 (-1.97%)</td><td>30.08 <b>(+165.10%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.89 (n/a)</td><td>0.85 (n/a)</td><td>0.88 (n/a)</td><td>0.75 (n/a)</td><td>0.06 (n/a)</td><td>174.60 (n/a)</td><td>155.50 (n/a)</td><td>149.60 (n/a)</td><td>147.20 (n/a)</td><td>11.35 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.00 (-2.27%)</td><td>0.00 (-3.24%)</td><td>0.00 (+0.00%)</td><td>0.00 (-13.95%)</td><td>0.00 <b>(+500.00%)</b></td><td>1096.81 (+14.26%)</td><td>976.00 (+2.54%)</td><td>947.00 (-0.56%)</td><td>942.33 (+0.54%)</td><td>67.61 <b>(+666.82%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>959.94 (n/a)</td><td>951.83 (n/a)</td><td>952.30 (n/a)</td><td>937.24 (n/a)</td><td>8.82 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.01 (+1.23%)</td><td>0.01 (+1.02%)</td><td>0.01 (+0.00%)</td><td>0.01 (+1.39%)</td><td>0.00 (-3.01%)</td><td>1114.90 (-1.99%)</td><td>1028.83 (-1.07%)</td><td>1010.57 (+0.20%)</td><td>995.35 (-1.02%)</td><td>49.16 (-12.90%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1137.57 (n/a)</td><td>1039.95 (n/a)</td><td>1008.51 (n/a)</td><td>1005.56 (n/a)</td><td>56.44 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.97 (+2.95%)</td><td>0.94 (+0.40%)</td><td>0.94 (+0.16%)</td><td>0.93 (-0.73%)</td><td>0.02 <b>(+324.12%)</b></td><td>2256.37 (+0.73%)</td><td>2223.61 (-0.37%)</td><td>2233.70 (-0.16%)</td><td>2155.66 (-2.87%)</td><td>39.20 <b>(+314.33%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.00 (n/a)</td><td>2240.09 (n/a)</td><td>2231.98 (n/a)</td><td>2237.30 (n/a)</td><td>2219.31 (n/a)</td><td>9.46 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.46 (+3.42%)</td><td>0.45 (+1.54%)</td><td>0.44 (+0.96%)</td><td>0.44 (+0.80%)</td><td>0.01 <b>(+222.64%)</b></td><td>1185.47 (-0.77%)</td><td>1171.91 (-1.50%)</td><td>1181.98 (-0.94%)</td><td>1141.65 (-3.32%)</td><td>18.50 <b>(+210.95%)</b></td>
</tr>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.38 (+0.66%)</td><td>0.37 (-0.43%)</td><td>0.37 (-0.80%)</td><td>0.37 (-0.57%)</td><td>0.01 <b>(+57.22%)</b></td><td>1432.28 (+0.58%)</td><td>1411.41 (+0.45%)</td><td>1417.51 (+0.81%)</td><td>1379.55 (-0.67%)</td><td>19.99 <b>(+57.54%)</b></td>
</tr>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.36 (-3.22%)</td><td>0.36 (-1.18%)</td><td>0.36 (-1.92%)</td><td>0.36 (+0.48%)</td><td>0.00 <b>(-63.19%)</b></td><td>1476.40 (-0.49%)</td><td>1462.02 (+1.15%)</td><td>1466.24 (+1.95%)</td><td>1443.67 (+3.35%)</td><td>13.48 <b>(-62.58%)</b></td>
</tr>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>3.44 (+1.49%)</td><td>3.03 (+15.52%)</td><td>3.11 (+19.74%)</td><td>2.58 <b>(+44.79%)</b></td><td>0.35 <b>(-44.48%)</b></td><td>203.10 <b>(-30.94%)</b></td><td>175.02 (-16.72%)</td><td>168.40 (-16.47%)</td><td>152.60 (-1.42%)</td><td>20.58 <b>(-62.22%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>3.39 (n/a)</td><td>2.62 (n/a)</td><td>2.60 (n/a)</td><td>1.78 (n/a)</td><td>0.62 (n/a)</td><td>294.10 (n/a)</td><td>210.16 (n/a)</td><td>201.60 (n/a)</td><td>154.80 (n/a)</td><td>54.47 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>5.61 (-1.49%)</td><td>4.69 (+11.36%)</td><td>4.49 (+5.74%)</td><td>4.39 <b>(+65.98%)</b></td><td>0.52 <b>(-54.21%)</b></td><td>239.00 <b>(-39.74%)</b></td><td>225.74 (-15.14%)</td><td>233.50 (-5.43%)</td><td>187.10 (+1.52%)</td><td>21.73 <b>(-73.09%)</b></td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>5.69 (n/a)</td><td>4.21 (n/a)</td><td>4.25 (n/a)</td><td>2.64 (n/a)</td><td>1.13 (n/a)</td><td>396.60 (n/a)</td><td>266.00 (n/a)</td><td>246.90 (n/a)</td><td>184.30 (n/a)</td><td>80.77 (n/a)</td>
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
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>3.88 <b>(+31.25%)</b></td><td>3.08 <b>(+25.65%)</b></td><td>2.95 <b>(+26.58%)</b></td><td>2.72 <b>(+22.77%)</b></td><td>0.47 <b>(+54.84%)</b></td><td>192.60 (-18.53%)</td><td>173.20 <b>(-20.00%)</b></td><td>177.70 <b>(-21.02%)</b></td><td>135.20 <b>(-23.83%)</b></td><td>23.12 (-4.58%)</td>
</tr>
<tr>
<td><code>65c00d6</code> — 2026-08-01 00:39:19</td><td>2.95 (n/a)</td><td>2.45 (n/a)</td><td>2.33 (n/a)</td><td>2.22 (n/a)</td><td>0.30 (n/a)</td><td>236.40 (n/a)</td><td>216.50 (n/a)</td><td>225.00 (n/a)</td><td>177.50 (n/a)</td><td>24.23 (n/a)</td>
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
