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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.11 (+9.47%)</td><td>0.09 (+4.60%)</td><td>0.11 (+19.74%)</td><td>0.06 (-12.58%)</td><td>0.02 <b>(+100.90%)</b></td><td>195.60 (+14.39%)</td><td>145.14 (+0.62%)</td><td>116.20 (-16.46%)</td><td>108.50 (-8.67%)</td><td>43.44 <b>(+113.30%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>171.00 (n/a)</td><td>144.24 (n/a)</td><td>139.10 (n/a)</td><td>118.80 (n/a)</td><td>20.37 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.11 <b>(+26.88%)</b></td><td>0.07 (-1.10%)</td><td>0.06 <b>(-20.49%)</b></td><td>0.06 (-3.73%)</td><td>0.02 <b>(+108.59%)</b></td><td>216.50 (+3.89%)</td><td>175.28 (+6.10%)</td><td>197.70 <b>(+25.76%)</b></td><td>111.60 <b>(-21.19%)</b></td><td>46.62 <b>(+73.36%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>208.40 (n/a)</td><td>165.20 (n/a)</td><td>157.20 (n/a)</td><td>141.60 (n/a)</td><td>26.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.09 (-16.78%)</td><td>0.07 (-4.23%)</td><td>0.07 (-8.44%)</td><td>0.06 (+15.09%)</td><td>0.01 <b>(-52.77%)</b></td><td>200.00 (-13.12%)</td><td>172.88 (-0.40%)</td><td>181.30 (+9.22%)</td><td>141.20 <b>(+20.17%)</b></td><td>22.58 <b>(-52.15%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>230.20 (n/a)</td><td>173.58 (n/a)</td><td>166.00 (n/a)</td><td>117.50 (n/a)</td><td>47.20 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.10 (+18.83%)</td><td>0.07 (+19.79%)</td><td>0.06 (+18.68%)</td><td>0.05 <b>(+29.06%)</b></td><td>0.02 (+12.81%)</td><td>227.60 <b>(-22.51%)</b></td><td>184.78 (-17.16%)</td><td>189.90 (-15.75%)</td><td>126.20 (-15.81%)</td><td>37.81 <b>(-26.93%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>293.70 (n/a)</td><td>223.06 (n/a)</td><td>225.40 (n/a)</td><td>149.90 (n/a)</td><td>51.74 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.04 (-11.34%)</td><td>0.03 (+4.54%)</td><td>0.03 (+9.53%)</td><td>0.03 (+12.43%)</td><td>0.00 <b>(-49.42%)</b></td><td>174.40 (-11.02%)</td><td>157.62 (-5.91%)</td><td>157.60 (-8.69%)</td><td>141.40 (+12.76%)</td><td>13.78 <b>(-47.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>167.52 (n/a)</td><td>172.60 (n/a)</td><td>125.40 (n/a)</td><td>26.23 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.04 (-12.49%)</td><td>0.04 (+2.71%)</td><td>0.04 <b>(+24.28%)</b></td><td>0.03 <b>(+33.55%)</b></td><td>0.00 <b>(-59.46%)</b></td><td>175.10 <b>(-25.11%)</b></td><td>144.74 (-9.01%)</td><td>135.90 (-19.54%)</td><td>126.30 (+14.30%)</td><td>19.13 <b>(-62.54%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.80 (n/a)</td><td>159.08 (n/a)</td><td>168.90 (n/a)</td><td>110.50 (n/a)</td><td>51.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (+8.21%)</td><td>0.03 (-7.56%)</td><td>0.03 (-8.26%)</td><td>0.03 (-9.51%)</td><td>0.01 <b>(+27.61%)</b></td><td>204.30 (+10.55%)</td><td>167.64 (+10.22%)</td><td>176.90 (+9.00%)</td><td>109.90 (-7.57%)</td><td>37.03 <b>(+30.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>152.10 (n/a)</td><td>162.30 (n/a)</td><td>118.90 (n/a)</td><td>28.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.03 <b>(-25.03%)</b></td><td>0.02 <b>(-25.69%)</b></td><td>0.02 <b>(-23.24%)</b></td><td>0.02 <b>(-25.89%)</b></td><td>0.00 <b>(-26.43%)</b></td><td>306.90 <b>(+34.90%)</b></td><td>237.86 <b>(+34.51%)</b></td><td>231.10 <b>(+30.27%)</b></td><td>185.30 <b>(+33.41%)</b></td><td>45.06 <b>(+33.51%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.50 (n/a)</td><td>176.84 (n/a)</td><td>177.40 (n/a)</td><td>138.90 (n/a)</td><td>33.75 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.03 <b>(-22.50%)</b></td><td>0.03 <b>(-32.20%)</b></td><td>0.03 <b>(-35.24%)</b></td><td>0.02 <b>(-47.05%)</b></td><td>0.01 <b>(+24.61%)</b></td><td>330.10 <b>(+88.84%)</b></td><td>221.60 <b>(+54.71%)</b></td><td>205.70 <b>(+54.43%)</b></td><td>154.40 <b>(+28.99%)</b></td><td>67.60 <b>(+207.44%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>174.80 (n/a)</td><td>143.24 (n/a)</td><td>133.20 (n/a)</td><td>119.70 (n/a)</td><td>21.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.03 (-9.53%)</td><td>0.02 <b>(-21.64%)</b></td><td>0.02 <b>(-29.11%)</b></td><td>0.02 (-17.88%)</td><td>0.00 (-1.21%)</td><td>258.70 <b>(+21.80%)</b></td><td>222.38 <b>(+28.45%)</b></td><td>224.20 <b>(+41.10%)</b></td><td>166.10 (+10.51%)</td><td>38.18 <b>(+36.22%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.40 (n/a)</td><td>173.12 (n/a)</td><td>158.90 (n/a)</td><td>150.30 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.03 (-19.02%)</td><td>0.03 (-3.91%)</td><td>0.03 (+3.64%)</td><td>0.02 (-5.57%)</td><td>0.00 <b>(-43.30%)</b></td><td>235.50 (+5.94%)</td><td>187.04 (+1.17%)</td><td>188.50 (-3.53%)</td><td>152.70 <b>(+23.54%)</b></td><td>31.10 <b>(-26.43%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.30 (n/a)</td><td>184.88 (n/a)</td><td>195.40 (n/a)</td><td>123.60 (n/a)</td><td>42.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.04 <b>(+23.87%)</b></td><td>0.02 (-5.72%)</td><td>0.02 (-11.49%)</td><td>0.02 (-13.86%)</td><td>0.01 <b>(+109.70%)</b></td><td>301.20 (+16.11%)</td><td>231.98 (+10.90%)</td><td>233.50 (+13.02%)</td><td>144.50 (-19.27%)</td><td>57.79 <b>(+86.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>259.40 (n/a)</td><td>209.18 (n/a)</td><td>206.60 (n/a)</td><td>179.00 (n/a)</td><td>31.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>177.62 (n/a)</td><td>170.70 (n/a)</td><td>158.70 (n/a)</td><td>23.54 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>177.04 (n/a)</td><td>174.50 (n/a)</td><td>145.20 (n/a)</td><td>24.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>239.60 (n/a)</td><td>193.66 (n/a)</td><td>192.60 (n/a)</td><td>156.30 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>178.16 (n/a)</td><td>185.90 (n/a)</td><td>143.20 (n/a)</td><td>28.17 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.80 (n/a)</td><td>176.66 (n/a)</td><td>188.40 (n/a)</td><td>144.10 (n/a)</td><td>20.08 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>184.42 (n/a)</td><td>186.80 (n/a)</td><td>139.30 (n/a)</td><td>29.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>235.30 (n/a)</td><td>193.56 (n/a)</td><td>192.60 (n/a)</td><td>160.70 (n/a)</td><td>26.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>237.20 (n/a)</td><td>213.40 (n/a)</td><td>215.50 (n/a)</td><td>179.40 (n/a)</td><td>21.04 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.90 (n/a)</td><td>144.34 (n/a)</td><td>148.40 (n/a)</td><td>110.00 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.50 (n/a)</td><td>170.54 (n/a)</td><td>164.20 (n/a)</td><td>143.30 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.80 (n/a)</td><td>162.80 (n/a)</td><td>171.40 (n/a)</td><td>137.60 (n/a)</td><td>22.98 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>164.30 (n/a)</td><td>167.70 (n/a)</td><td>126.80 (n/a)</td><td>24.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>323.80 (n/a)</td><td>188.14 (n/a)</td><td>147.10 (n/a)</td><td>124.40 (n/a)</td><td>80.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.50 (n/a)</td><td>170.06 (n/a)</td><td>164.80 (n/a)</td><td>155.70 (n/a)</td><td>18.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>183.36 (n/a)</td><td>177.70 (n/a)</td><td>148.40 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.00 (n/a)</td><td>191.50 (n/a)</td><td>201.80 (n/a)</td><td>134.20 (n/a)</td><td>49.41 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>4.89 (-2.05%)</td><td>4.37 (+2.90%)</td><td>4.26 (+5.32%)</td><td>4.20 (+5.98%)</td><td>0.29 <b>(-31.19%)</b></td><td>2238.00 (-5.65%)</td><td>2160.62 (-3.20%)</td><td>2208.90 (-5.05%)</td><td>1923.70 (+2.10%)</td><td>133.65 <b>(-33.34%)</b></td><td>1923.08 (-2.05%)</td><td>1717.89 (+2.90%)</td><td>1674.72 (+5.32%)</td><td>1652.98 (+5.98%)</td><td>115.49 <b>(-31.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>4.99 (n/a)</td><td>4.24 (n/a)</td><td>4.04 (n/a)</td><td>3.96 (n/a)</td><td>0.43 (n/a)</td><td>2371.90 (n/a)</td><td>2232.02 (n/a)</td><td>2326.50 (n/a)</td><td>1884.20 (n/a)</td><td>200.51 (n/a)</td><td>1963.40 (n/a)</td><td>1669.47 (n/a)</td><td>1590.09 (n/a)</td><td>1559.66 (n/a)</td><td>167.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>1.11 <b>(-28.36%)</b></td><td>0.88 (-4.92%)</td><td>0.95 <b>(+23.02%)</b></td><td>0.64 (-0.24%)</td><td>0.21 <b>(-43.78%)</b></td><td>344.40 (+0.26%)</td><td>263.16 (-0.60%)</td><td>233.40 (-18.70%)</td><td>198.60 <b>(+39.56%)</b></td><td>67.44 <b>(-20.21%)</b></td><td>47.52 <b>(-28.36%)</b></td><td>37.72 (-4.92%)</td><td>40.43 <b>(+23.02%)</b></td><td>27.41 (-0.24%)</td><td>9.10 <b>(-43.78%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>1.55 (n/a)</td><td>0.93 (n/a)</td><td>0.77 (n/a)</td><td>0.64 (n/a)</td><td>0.38 (n/a)</td><td>343.50 (n/a)</td><td>264.76 (n/a)</td><td>287.10 (n/a)</td><td>142.30 (n/a)</td><td>84.51 (n/a)</td><td>66.33 (n/a)</td><td>39.67 (n/a)</td><td>32.87 (n/a)</td><td>27.47 (n/a)</td><td>16.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>1.10 (+11.32%)</td><td>0.90 (+7.55%)</td><td>0.91 (+4.05%)</td><td>0.67 (+0.90%)</td><td>0.16 <b>(+28.21%)</b></td><td>330.90 (-0.87%)</td><td>253.46 (-6.18%)</td><td>243.30 (-3.87%)</td><td>200.70 (-10.16%)</td><td>49.53 (+14.66%)</td><td>47.03 (+11.32%)</td><td>38.31 (+7.55%)</td><td>38.79 (+4.05%)</td><td>28.52 (+0.90%)</td><td>6.94 <b>(+28.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.99 (n/a)</td><td>0.83 (n/a)</td><td>0.87 (n/a)</td><td>0.66 (n/a)</td><td>0.13 (n/a)</td><td>333.80 (n/a)</td><td>270.16 (n/a)</td><td>253.10 (n/a)</td><td>223.40 (n/a)</td><td>43.20 (n/a)</td><td>42.24 (n/a)</td><td>35.62 (n/a)</td><td>37.28 (n/a)</td><td>28.27 (n/a)</td><td>5.41 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.52 (-0.68%)</td><td>0.52 (-0.14%)</td><td>0.52 (-0.01%)</td><td>0.52 (-0.06%)</td><td>0.00 <b>(-78.49%)</b></td><td>48700.00 (+0.06%)</td><td>48640.04 (+0.14%)</td><td>48632.40 (+0.01%)</td><td>48607.20 (+0.69%)</td><td>36.19 <b>(-78.30%)</b></td><td>353.44 (-0.68%)</td><td>353.20 (-0.14%)</td><td>353.26 (-0.01%)</td><td>352.77 (-0.06%)</td><td>0.26 <b>(-78.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48670.60 (n/a)</td><td>48570.74 (n/a)</td><td>48627.00 (n/a)</td><td>48274.70 (n/a)</td><td>166.79 (n/a)</td><td>355.88 (n/a)</td><td>353.71 (n/a)</td><td>353.30 (n/a)</td><td>352.98 (n/a)</td><td>1.22 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.89 (+0.51%)</td><td>0.88 (+0.45%)</td><td>0.88 (+0.39%)</td><td>0.88 (+0.95%)</td><td>0.01 (-17.99%)</td><td>28661.60 (-0.94%)</td><td>28458.36 (-0.45%)</td><td>28489.10 (-0.39%)</td><td>28130.10 (-0.51%)</td><td>197.41 (-19.31%)</td><td>610.73 (+0.51%)</td><td>603.71 (+0.45%)</td><td>603.03 (+0.39%)</td><td>599.40 (+0.95%)</td><td>4.21 (-17.99%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28932.90 (n/a)</td><td>28586.36 (n/a)</td><td>28600.70 (n/a)</td><td>28274.00 (n/a)</td><td>244.64 (n/a)</td><td>607.62 (n/a)</td><td>601.02 (n/a)</td><td>600.68 (n/a)</td><td>593.78 (n/a)</td><td>5.14 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>3.37 (+2.85%)</td><td>3.27 (+3.47%)</td><td>3.27 (+3.49%)</td><td>3.18 (+3.03%)</td><td>0.08 (+18.84%)</td><td>7918.60 (-2.94%)</td><td>7688.46 (-3.34%)</td><td>7697.30 (-3.37%)</td><td>7476.30 (-2.78%)</td><td>190.97 (+12.34%)</td><td>2297.90 (+2.85%)</td><td>2235.60 (+3.47%)</td><td>2231.94 (+3.49%)</td><td>2169.55 (+3.03%)</td><td>55.51 (+18.84%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>3.27 (n/a)</td><td>3.16 (n/a)</td><td>3.16 (n/a)</td><td>3.08 (n/a)</td><td>0.07 (n/a)</td><td>8158.20 (n/a)</td><td>7954.42 (n/a)</td><td>7966.10 (n/a)</td><td>7689.80 (n/a)</td><td>169.99 (n/a)</td><td>2234.13 (n/a)</td><td>2160.59 (n/a)</td><td>2156.62 (n/a)</td><td>2105.84 (n/a)</td><td>46.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>4.25 (-2.30%)</td><td>3.72 (-1.98%)</td><td>3.83 (+3.49%)</td><td>2.86 (-9.90%)</td><td>0.55 (+17.29%)</td><td>2817.70 (+10.99%)</td><td>2210.78 (+2.76%)</td><td>2103.60 (-3.38%)</td><td>1897.90 (+2.35%)</td><td>369.67 <b>(+35.56%)</b></td><td>1113.83 (-2.30%)</td><td>975.44 (-1.98%)</td><td>1004.89 (+3.49%)</td><td>750.23 (-9.90%)</td><td>144.87 (+17.29%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>4.35 (n/a)</td><td>3.79 (n/a)</td><td>3.70 (n/a)</td><td>3.18 (n/a)</td><td>0.47 (n/a)</td><td>2538.80 (n/a)</td><td>2151.30 (n/a)</td><td>2177.10 (n/a)</td><td>1854.30 (n/a)</td><td>272.71 (n/a)</td><td>1140.03 (n/a)</td><td>995.10 (n/a)</td><td>970.97 (n/a)</td><td>832.66 (n/a)</td><td>123.51 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.53 <b>(+50.27%)</b></td><td>0.38 <b>(+20.58%)</b></td><td>0.35 (+7.48%)</td><td>0.33 (+19.57%)</td><td>0.09 <b>(+169.76%)</b></td><td>3825.10 (-16.37%)</td><td>3375.60 (-15.02%)</td><td>3558.50 (-6.96%)</td><td>2332.80 <b>(-33.45%)</b></td><td>603.43 <b>(+45.03%)</b></td><td>28.77 <b>(+50.27%)</b></td><td>20.55 <b>(+20.58%)</b></td><td>18.86 (+7.48%)</td><td>17.54 (+19.57%)</td><td>4.67 <b>(+169.76%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>4573.70 (n/a)</td><td>3972.46 (n/a)</td><td>3824.60 (n/a)</td><td>3505.50 (n/a)</td><td>416.07 (n/a)</td><td>19.14 (n/a)</td><td>17.04 (n/a)</td><td>17.55 (n/a)</td><td>14.67 (n/a)</td><td>1.73 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>6.04 (-8.03%)</td><td>4.54 (-0.93%)</td><td>4.68 (+4.36%)</td><td>3.32 (-7.15%)</td><td>1.08 (-10.22%)</td><td>2000.80 (+7.70%)</td><td>1535.14 (+0.76%)</td><td>1422.50 (-4.18%)</td><td>1101.00 (+8.73%)</td><td>364.86 (+6.83%)</td><td>1866.76 (-8.03%)</td><td>1401.41 (-0.93%)</td><td>1444.76 (+4.36%)</td><td>1027.18 (-7.15%)</td><td>334.38 (-10.22%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>6.57 (n/a)</td><td>4.58 (n/a)</td><td>4.48 (n/a)</td><td>3.58 (n/a)</td><td>1.21 (n/a)</td><td>1857.80 (n/a)</td><td>1523.60 (n/a)</td><td>1484.60 (n/a)</td><td>1012.60 (n/a)</td><td>341.54 (n/a)</td><td>2029.68 (n/a)</td><td>1414.56 (n/a)</td><td>1384.37 (n/a)</td><td>1106.25 (n/a)</td><td>372.43 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.21 (-0.05%)</td><td>0.19 (-1.25%)</td><td>0.19 (-3.07%)</td><td>0.18 (+15.12%)</td><td>0.02 <b>(-35.07%)</b></td><td>0.21 (-0.05%)</td><td>0.19 (-1.25%)</td><td>0.19 (-3.07%)</td><td>0.17 (+15.12%)</td><td>0.02 <b>(-35.07%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>13.08 (-2.39%)</td><td>12.48 (-5.64%)</td><td>12.49 (-5.56%)</td><td>11.90 (-8.90%)</td><td>0.43 <b>(+218.13%)</b></td><td>13.07 (-2.39%)</td><td>12.48 (-5.64%)</td><td>12.48 (-5.56%)</td><td>11.89 (-8.90%)</td><td>0.43 <b>(+218.13%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>13.40 (n/a)</td><td>13.23 (n/a)</td><td>13.22 (n/a)</td><td>13.06 (n/a)</td><td>0.14 (n/a)</td><td>13.39 (n/a)</td><td>13.22 (n/a)</td><td>13.21 (n/a)</td><td>13.05 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>24.38 (-3.79%)</td><td>23.85 (-4.37%)</td><td>23.91 (-4.35%)</td><td>22.89 (-6.36%)</td><td>0.58 <b>(+57.43%)</b></td><td>24.37 (-3.79%)</td><td>23.83 (-4.37%)</td><td>23.90 (-4.35%)</td><td>22.88 (-6.36%)</td><td>0.58 <b>(+57.43%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>25.34 (n/a)</td><td>24.94 (n/a)</td><td>25.00 (n/a)</td><td>24.45 (n/a)</td><td>0.37 (n/a)</td><td>25.33 (n/a)</td><td>24.92 (n/a)</td><td>24.98 (n/a)</td><td>24.43 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>41.21 (-7.87%)</td><td>39.10 (-6.17%)</td><td>39.60 (-5.12%)</td><td>37.27 (-4.39%)</td><td>1.64 <b>(-20.37%)</b></td><td>41.19 (-7.87%)</td><td>39.07 (-6.17%)</td><td>39.57 (-5.12%)</td><td>37.25 (-4.39%)</td><td>1.64 <b>(-20.37%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>44.73 (n/a)</td><td>41.67 (n/a)</td><td>41.73 (n/a)</td><td>38.99 (n/a)</td><td>2.06 (n/a)</td><td>44.70 (n/a)</td><td>41.65 (n/a)</td><td>41.71 (n/a)</td><td>38.96 (n/a)</td><td>2.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>42.68 (-3.88%)</td><td>42.02 (-1.65%)</td><td>41.91 (-1.93%)</td><td>41.61 (+2.91%)</td><td>0.40 <b>(-73.36%)</b></td><td>42.66 (-3.88%)</td><td>41.99 (-1.65%)</td><td>41.88 (-1.93%)</td><td>41.59 (+2.91%)</td><td>0.40 <b>(-73.36%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>44.41 (n/a)</td><td>42.73 (n/a)</td><td>42.73 (n/a)</td><td>40.44 (n/a)</td><td>1.49 (n/a)</td><td>44.38 (n/a)</td><td>42.70 (n/a)</td><td>42.71 (n/a)</td><td>40.41 (n/a)</td><td>1.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>13.20 (-0.72%)</td><td>11.73 (-9.82%)</td><td>11.63 (-12.20%)</td><td>10.56 (-13.14%)</td><td>1.04 <b>(+115.78%)</b></td><td>13.19 (-0.72%)</td><td>11.73 (-9.82%)</td><td>11.62 (-12.20%)</td><td>10.55 (-13.14%)</td><td>1.04 <b>(+115.78%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>13.29 (n/a)</td><td>13.01 (n/a)</td><td>13.24 (n/a)</td><td>12.15 (n/a)</td><td>0.48 (n/a)</td><td>13.28 (n/a)</td><td>13.00 (n/a)</td><td>13.23 (n/a)</td><td>12.14 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>24.46 (-1.08%)</td><td>24.18 (-0.75%)</td><td>24.34 (+0.07%)</td><td>23.72 (-1.85%)</td><td>0.30 <b>(+31.81%)</b></td><td>24.45 (-1.08%)</td><td>24.17 (-0.75%)</td><td>24.32 (+0.07%)</td><td>23.70 (-1.85%)</td><td>0.30 <b>(+31.81%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>24.73 (n/a)</td><td>24.37 (n/a)</td><td>24.32 (n/a)</td><td>24.16 (n/a)</td><td>0.23 (n/a)</td><td>24.71 (n/a)</td><td>24.35 (n/a)</td><td>24.30 (n/a)</td><td>24.15 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>41.58 (-2.15%)</td><td>39.90 (-1.27%)</td><td>40.40 (+1.52%)</td><td>36.62 (-5.80%)</td><td>1.90 <b>(+34.20%)</b></td><td>41.56 (-2.15%)</td><td>39.88 (-1.27%)</td><td>40.38 (+1.52%)</td><td>36.60 (-5.80%)</td><td>1.90 <b>(+34.20%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>42.49 (n/a)</td><td>40.41 (n/a)</td><td>39.80 (n/a)</td><td>38.87 (n/a)</td><td>1.42 (n/a)</td><td>42.47 (n/a)</td><td>40.39 (n/a)</td><td>39.77 (n/a)</td><td>38.85 (n/a)</td><td>1.42 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>44.98 (+2.68%)</td><td>43.15 (+2.89%)</td><td>43.36 (-0.74%)</td><td>40.74 (+7.88%)</td><td>1.52 <b>(-43.12%)</b></td><td>44.95 (+2.68%)</td><td>43.13 (+2.89%)</td><td>43.33 (-0.74%)</td><td>40.72 (+7.88%)</td><td>1.52 <b>(-43.12%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>43.81 (n/a)</td><td>41.94 (n/a)</td><td>43.68 (n/a)</td><td>37.77 (n/a)</td><td>2.67 (n/a)</td><td>43.78 (n/a)</td><td>41.91 (n/a)</td><td>43.65 (n/a)</td><td>37.75 (n/a)</td><td>2.67 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>269.30 (n/a)</td><td>185.38 (n/a)</td><td>177.80 (n/a)</td><td>109.80 (n/a)</td><td>58.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.60 (n/a)</td><td>175.36 (n/a)</td><td>172.90 (n/a)</td><td>129.90 (n/a)</td><td>37.30 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.80 (n/a)</td><td>169.40 (n/a)</td><td>175.60 (n/a)</td><td>125.70 (n/a)</td><td>26.67 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.50 (n/a)</td><td>172.36 (n/a)</td><td>178.90 (n/a)</td><td>147.60 (n/a)</td><td>20.64 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.80 (n/a)</td><td>189.10 (n/a)</td><td>178.30 (n/a)</td><td>161.00 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.00 (n/a)</td><td>205.88 (n/a)</td><td>203.20 (n/a)</td><td>163.80 (n/a)</td><td>33.59 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.50 (n/a)</td><td>201.28 (n/a)</td><td>197.00 (n/a)</td><td>172.80 (n/a)</td><td>24.16 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.20 (n/a)</td><td>219.22 (n/a)</td><td>225.00 (n/a)</td><td>176.50 (n/a)</td><td>28.83 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 <b>(-26.35%)</b></td><td>0.05 (-7.78%)</td><td>0.05 (-1.32%)</td><td>0.04 (-4.99%)</td><td>0.01 <b>(-53.68%)</b></td><td>208.50 (+5.25%)</td><td>171.78 (+5.84%)</td><td>166.80 (+1.34%)</td><td>155.00 <b>(+35.85%)</b></td><td>21.78 <b>(-31.88%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>162.30 (n/a)</td><td>164.60 (n/a)</td><td>114.10 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (-7.42%)</td><td>0.04 <b>(+20.45%)</b></td><td>0.04 <b>(+36.63%)</b></td><td>0.03 <b>(+31.16%)</b></td><td>0.00 <b>(-52.03%)</b></td><td>243.70 <b>(-23.75%)</b></td><td>217.46 <b>(-20.86%)</b></td><td>223.20 <b>(-26.82%)</b></td><td>178.60 (+8.05%)</td><td>25.51 <b>(-59.54%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>319.60 (n/a)</td><td>274.78 (n/a)</td><td>305.00 (n/a)</td><td>165.30 (n/a)</td><td>63.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (-13.35%)</td><td>0.04 (-15.62%)</td><td>0.05 (-14.27%)</td><td>0.04 (-14.11%)</td><td>0.01 (-9.34%)</td><td>218.60 (+16.40%)</td><td>188.36 (+18.64%)</td><td>182.00 (+16.67%)</td><td>156.70 (+15.39%)</td><td>23.67 <b>(+21.22%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>158.76 (n/a)</td><td>156.00 (n/a)</td><td>135.80 (n/a)</td><td>19.52 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 <b>(-24.26%)</b></td><td>0.04 <b>(-22.86%)</b></td><td>0.05 (-13.17%)</td><td>0.03 <b>(-33.18%)</b></td><td>0.01 (-19.05%)</td><td>269.90 <b>(+49.69%)</b></td><td>195.84 <b>(+30.82%)</b></td><td>181.40 (+15.10%)</td><td>153.50 <b>(+31.99%)</b></td><td>45.53 <b>(+65.17%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.30 (n/a)</td><td>149.70 (n/a)</td><td>157.60 (n/a)</td><td>116.30 (n/a)</td><td>27.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 <b>(-38.71%)</b></td><td>0.04 (-18.08%)</td><td>0.04 (-10.61%)</td><td>0.04 (-10.87%)</td><td>0.00 <b>(-80.69%)</b></td><td>209.80 (+12.19%)</td><td>191.14 (+18.24%)</td><td>188.80 (+11.91%)</td><td>180.40 <b>(+63.26%)</b></td><td>11.08 <b>(-62.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.00 (n/a)</td><td>161.66 (n/a)</td><td>168.70 (n/a)</td><td>110.50 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (-17.36%)</td><td>0.04 (-13.89%)</td><td>0.04 (-7.97%)</td><td>0.04 (+6.95%)</td><td>0.01 <b>(-46.22%)</b></td><td>219.60 (-6.51%)</td><td>192.50 (+11.07%)</td><td>204.60 (+8.66%)</td><td>143.70 <b>(+20.96%)</b></td><td>30.58 <b>(-37.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>173.32 (n/a)</td><td>188.30 (n/a)</td><td>118.80 (n/a)</td><td>48.92 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (-15.01%)</td><td>0.04 (-2.48%)</td><td>0.04 (-2.22%)</td><td>0.04 (+3.98%)</td><td>0.00 <b>(-44.44%)</b></td><td>223.80 (-3.82%)</td><td>198.26 (+0.59%)</td><td>198.20 (+2.27%)</td><td>167.10 (+17.68%)</td><td>22.63 <b>(-36.04%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.70 (n/a)</td><td>197.10 (n/a)</td><td>193.80 (n/a)</td><td>142.00 (n/a)</td><td>35.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 <b>(-23.26%)</b></td><td>0.04 (-17.08%)</td><td>0.04 (-11.17%)</td><td>0.04 (-5.05%)</td><td>0.00 <b>(-62.72%)</b></td><td>220.70 (+5.30%)</td><td>197.88 (+17.77%)</td><td>197.70 (+12.52%)</td><td>175.30 <b>(+30.33%)</b></td><td>16.92 <b>(-47.09%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>168.02 (n/a)</td><td>175.70 (n/a)</td><td>134.50 (n/a)</td><td>31.97 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.21 (+0.05%)</td><td>0.21 (-0.06%)</td><td>0.21 (-0.10%)</td><td>0.20 (-0.10%)</td><td>0.00 <b>(+79.29%)</b></td><td>40922.50 (+0.10%)</td><td>40867.56 (+0.06%)</td><td>40883.70 (+0.10%)</td><td>40772.90 (-0.05%)</td><td>62.57 <b>(+79.44%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40882.90 (n/a)</td><td>40842.88 (n/a)</td><td>40843.80 (n/a)</td><td>40791.90 (n/a)</td><td>34.87 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (+1.93%)</td><td>0.05 (-0.83%)</td><td>0.05 (-4.21%)</td><td>0.04 (+0.40%)</td><td>0.01 (+0.92%)</td><td>222.00 (-0.40%)</td><td>176.12 (+0.71%)</td><td>179.00 (+4.43%)</td><td>123.20 (-1.91%)</td><td>36.19 (-4.01%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.90 (n/a)</td><td>174.88 (n/a)</td><td>171.40 (n/a)</td><td>125.60 (n/a)</td><td>37.70 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.10 (+0.89%)</td><td>0.07 (-13.29%)</td><td>0.07 (-11.17%)</td><td>0.05 <b>(-27.92%)</b></td><td>0.02 <b>(+74.71%)</b></td><td>241.80 <b>(+38.73%)</b></td><td>181.40 <b>(+20.37%)</b></td><td>171.30 (+12.55%)</td><td>121.30 (-0.90%)</td><td>46.86 <b>(+144.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>174.30 (n/a)</td><td>150.70 (n/a)</td><td>152.20 (n/a)</td><td>122.40 (n/a)</td><td>19.14 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (-10.69%)</td><td>0.05 (-10.93%)</td><td>0.05 <b>(-22.41%)</b></td><td>0.05 (+5.43%)</td><td>0.01 <b>(-35.01%)</b></td><td>177.90 (-5.17%)</td><td>155.50 (+9.40%)</td><td>162.60 <b>(+28.84%)</b></td><td>122.00 (+12.03%)</td><td>24.71 <b>(-30.65%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.60 (n/a)</td><td>142.14 (n/a)</td><td>126.20 (n/a)</td><td>108.90 (n/a)</td><td>35.64 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (-4.19%)</td><td>0.06 (+8.01%)</td><td>0.06 (+7.38%)</td><td>0.05 <b>(+32.51%)</b></td><td>0.01 <b>(-38.84%)</b></td><td>216.40 <b>(-24.55%)</b></td><td>174.10 (-10.72%)</td><td>171.70 (-6.84%)</td><td>151.00 (+4.35%)</td><td>25.42 <b>(-53.17%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>286.80 (n/a)</td><td>195.00 (n/a)</td><td>184.30 (n/a)</td><td>144.70 (n/a)</td><td>54.29 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (-8.69%)</td><td>0.05 (-7.37%)</td><td>0.05 (-8.48%)</td><td>0.04 (+2.06%)</td><td>0.01 <b>(-34.52%)</b></td><td>199.20 (-2.06%)</td><td>169.38 (+6.07%)</td><td>176.50 (+9.29%)</td><td>138.50 (+9.49%)</td><td>23.49 <b>(-28.13%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>159.68 (n/a)</td><td>161.50 (n/a)</td><td>126.50 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.09 (+0.98%)</td><td>0.06 (+10.72%)</td><td>0.06 (-3.25%)</td><td>0.05 <b>(+31.60%)</b></td><td>0.02 (-3.29%)</td><td>220.80 <b>(-23.99%)</b></td><td>167.94 (-11.92%)</td><td>179.90 (+3.33%)</td><td>118.10 (-0.92%)</td><td>44.50 <b>(-30.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>290.50 (n/a)</td><td>190.66 (n/a)</td><td>174.10 (n/a)</td><td>119.20 (n/a)</td><td>64.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (-8.27%)</td><td>0.05 (-9.95%)</td><td>0.04 (-14.02%)</td><td>0.03 (-8.94%)</td><td>0.01 (+1.07%)</td><td>239.30 (+9.82%)</td><td>183.48 (+11.97%)</td><td>194.10 (+16.30%)</td><td>130.20 (+9.05%)</td><td>43.56 (+19.14%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>163.86 (n/a)</td><td>166.90 (n/a)</td><td>119.40 (n/a)</td><td>36.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 (+17.20%)</td><td>0.05 (-14.36%)</td><td>0.05 (-19.11%)</td><td>0.03 <b>(-35.95%)</b></td><td>0.02 <b>(+255.94%)</b></td><td>287.40 <b>(+56.11%)</b></td><td>203.90 <b>(+25.43%)</b></td><td>195.10 <b>(+23.64%)</b></td><td>128.10 (-14.71%)</td><td>61.50 <b>(+368.05%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>184.10 (n/a)</td><td>162.56 (n/a)</td><td>157.80 (n/a)</td><td>150.20 (n/a)</td><td>13.14 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (-12.47%)</td><td>0.05 (-3.08%)</td><td>0.06 (+3.04%)</td><td>0.04 (+15.57%)</td><td>0.01 <b>(-43.10%)</b></td><td>183.70 (-13.51%)</td><td>157.88 (+0.83%)</td><td>148.80 (-2.94%)</td><td>137.90 (+14.25%)</td><td>18.65 <b>(-45.12%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>156.58 (n/a)</td><td>153.30 (n/a)</td><td>120.70 (n/a)</td><td>33.98 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (-18.46%)</td><td>0.05 (-10.43%)</td><td>0.05 (-12.35%)</td><td>0.04 (-15.48%)</td><td>0.01 (-14.35%)</td><td>225.40 (+18.32%)</td><td>187.16 (+11.82%)</td><td>198.40 (+14.09%)</td><td>152.20 <b>(+22.64%)</b></td><td>31.74 <b>(+25.47%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>190.50 (n/a)</td><td>167.38 (n/a)</td><td>173.90 (n/a)</td><td>124.10 (n/a)</td><td>25.30 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.07 <b>(+44.70%)</b></td><td>0.05 (+9.36%)</td><td>0.04 (-7.48%)</td><td>0.04 (-13.55%)</td><td>0.01 <b>(+472.49%)</b></td><td>226.30 (+15.70%)</td><td>177.34 (-4.18%)</td><td>194.60 (+8.05%)</td><td>122.60 <b>(-30.93%)</b></td><td>41.65 <b>(+352.07%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.60 (n/a)</td><td>185.08 (n/a)</td><td>180.10 (n/a)</td><td>177.50 (n/a)</td><td>9.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (-10.53%)</td><td>0.04 (-5.47%)</td><td>0.04 (-6.89%)</td><td>0.03 (-8.52%)</td><td>0.01 <b>(-23.27%)</b></td><td>318.40 (+9.30%)</td><td>233.44 (+4.20%)</td><td>225.30 (+7.39%)</td><td>172.20 (+11.75%)</td><td>52.81 (-6.33%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>291.30 (n/a)</td><td>224.02 (n/a)</td><td>209.80 (n/a)</td><td>154.10 (n/a)</td><td>56.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.06 (-6.69%)</td><td>0.04 (-13.31%)</td><td>0.04 (-15.90%)</td><td>0.04 <b>(-23.40%)</b></td><td>0.01 <b>(+41.74%)</b></td><td>229.60 <b>(+30.53%)</b></td><td>188.88 (+17.03%)</td><td>195.40 (+18.93%)</td><td>147.60 (+7.11%)</td><td>31.21 <b>(+95.09%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.90 (n/a)</td><td>161.40 (n/a)</td><td>164.30 (n/a)</td><td>137.80 (n/a)</td><td>16.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.05 (-8.33%)</td><td>0.04 (-13.12%)</td><td>0.04 (-12.35%)</td><td>0.03 (-14.83%)</td><td>0.01 (-13.48%)</td><td>258.90 (+17.41%)</td><td>211.52 (+15.04%)</td><td>210.10 (+14.12%)</td><td>169.60 (+9.07%)</td><td>31.73 (+13.22%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>183.86 (n/a)</td><td>184.10 (n/a)</td><td>155.50 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.04 (-16.55%)</td><td>0.04 (-4.11%)</td><td>0.04 (-0.21%)</td><td>0.03 (+9.35%)</td><td>0.00 <b>(-48.20%)</b></td><td>264.40 (-8.54%)</td><td>219.98 (+1.74%)</td><td>215.60 (+0.19%)</td><td>192.60 (+19.85%)</td><td>26.86 <b>(-42.63%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>289.10 (n/a)</td><td>216.22 (n/a)</td><td>215.20 (n/a)</td><td>160.70 (n/a)</td><td>46.82 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.91 <b>(+30.21%)</b></td><td>0.63 (+13.64%)</td><td>0.48 (-7.52%)</td><td>0.45 (+2.38%)</td><td>0.23 <b>(+98.30%)</b></td><td>218.50 (-2.32%)</td><td>171.68 (-6.36%)</td><td>204.80 (+8.13%)</td><td>108.10 <b>(-23.22%)</b></td><td>54.42 <b>(+50.08%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.70 (n/a)</td><td>0.55 (n/a)</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.11 (n/a)</td><td>223.70 (n/a)</td><td>183.34 (n/a)</td><td>189.40 (n/a)</td><td>140.80 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.54 (-16.11%)</td><td>0.50 (-6.59%)</td><td>0.50 (-11.16%)</td><td>0.49 (+10.30%)</td><td>0.02 <b>(-76.76%)</b></td><td>200.50 (-9.32%)</td><td>195.16 (+5.26%)</td><td>197.20 (+12.56%)</td><td>183.20 (+19.19%)</td><td>6.88 <b>(-75.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.64 (n/a)</td><td>0.54 (n/a)</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.08 (n/a)</td><td>221.10 (n/a)</td><td>185.40 (n/a)</td><td>175.20 (n/a)</td><td>153.70 (n/a)</td><td>27.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.78 <b>(+26.90%)</b></td><td>0.62 (+19.51%)</td><td>0.61 <b>(+20.93%)</b></td><td>0.48 (+7.65%)</td><td>0.11 <b>(+70.09%)</b></td><td>206.40 (-7.11%)</td><td>162.76 (-15.11%)</td><td>161.50 (-17.31%)</td><td>125.90 <b>(-21.21%)</b></td><td>30.37 <b>(+25.23%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.62 (n/a)</td><td>0.52 (n/a)</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.07 (n/a)</td><td>222.20 (n/a)</td><td>191.72 (n/a)</td><td>195.30 (n/a)</td><td>159.80 (n/a)</td><td>24.25 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.51 (-11.49%)</td><td>0.46 (-5.26%)</td><td>0.48 (+3.86%)</td><td>0.36 (-15.70%)</td><td>0.06 (+1.18%)</td><td>274.30 (+18.64%)</td><td>215.48 (+6.05%)</td><td>203.10 (-3.74%)</td><td>193.10 (+12.99%)</td><td>33.33 <b>(+40.07%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.58 (n/a)</td><td>0.49 (n/a)</td><td>0.47 (n/a)</td><td>0.43 (n/a)</td><td>0.06 (n/a)</td><td>231.20 (n/a)</td><td>203.18 (n/a)</td><td>211.00 (n/a)</td><td>170.90 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.49 (-19.33%)</td><td>0.40 <b>(-20.18%)</b></td><td>0.39 <b>(-20.44%)</b></td><td>0.33 (-11.52%)</td><td>0.06 <b>(-38.19%)</b></td><td>223.50 (+12.99%)</td><td>185.36 <b>(+23.49%)</b></td><td>186.70 <b>(+25.72%)</b></td><td>149.60 <b>(+23.94%)</b></td><td>26.90 (-13.00%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.61 (n/a)</td><td>0.51 (n/a)</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.10 (n/a)</td><td>197.80 (n/a)</td><td>150.10 (n/a)</td><td>148.50 (n/a)</td><td>120.70 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.46 (-19.79%)</td><td>0.40 (-16.03%)</td><td>0.41 (-5.77%)</td><td>0.33 (-14.69%)</td><td>0.05 <b>(-41.31%)</b></td><td>224.20 (+17.26%)</td><td>187.74 (+17.63%)</td><td>179.00 (+6.11%)</td><td>160.10 <b>(+24.69%)</b></td><td>24.91 (-11.15%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.57 (n/a)</td><td>0.47 (n/a)</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.09 (n/a)</td><td>191.20 (n/a)</td><td>159.60 (n/a)</td><td>168.70 (n/a)</td><td>128.40 (n/a)</td><td>28.04 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.51 (-3.07%)</td><td>0.43 (-1.39%)</td><td>0.41 (-2.20%)</td><td>0.38 (+4.29%)</td><td>0.05 <b>(-29.74%)</b></td><td>195.80 (-4.11%)</td><td>174.26 (+0.32%)</td><td>179.60 (+2.22%)</td><td>145.80 (+3.18%)</td><td>18.85 <b>(-31.61%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.07 (n/a)</td><td>204.20 (n/a)</td><td>173.70 (n/a)</td><td>175.70 (n/a)</td><td>141.30 (n/a)</td><td>27.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.50 (+10.34%)</td><td>0.35 (-9.07%)</td><td>0.35 (-2.24%)</td><td>0.24 <b>(-29.91%)</b></td><td>0.09 <b>(+68.60%)</b></td><td>313.00 <b>(+42.66%)</b></td><td>222.24 (+14.56%)</td><td>212.80 (+2.26%)</td><td>148.10 (-9.36%)</td><td>59.52 <b>(+120.29%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.45 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.06 (n/a)</td><td>219.40 (n/a)</td><td>194.00 (n/a)</td><td>208.10 (n/a)</td><td>163.40 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.88 (-6.40%)</td><td>0.76 (-6.69%)</td><td>0.74 (-10.72%)</td><td>0.68 (-0.32%)</td><td>0.08 <b>(-27.78%)</b></td><td>192.90 (+0.31%)</td><td>174.12 (+6.44%)</td><td>176.70 (+12.05%)</td><td>149.30 (+6.87%)</td><td>17.63 <b>(-22.91%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.94 (n/a)</td><td>0.81 (n/a)</td><td>0.83 (n/a)</td><td>0.68 (n/a)</td><td>0.11 (n/a)</td><td>192.30 (n/a)</td><td>163.58 (n/a)</td><td>157.70 (n/a)</td><td>139.70 (n/a)</td><td>22.87 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.94 (-15.79%)</td><td>0.80 (+2.27%)</td><td>0.78 (+15.30%)</td><td>0.70 (+10.80%)</td><td>0.09 <b>(-55.65%)</b></td><td>187.30 (-9.73%)</td><td>165.96 (-5.47%)</td><td>168.80 (-13.26%)</td><td>139.40 (+18.84%)</td><td>17.31 <b>(-52.58%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>1.12 (n/a)</td><td>0.78 (n/a)</td><td>0.67 (n/a)</td><td>0.63 (n/a)</td><td>0.20 (n/a)</td><td>207.50 (n/a)</td><td>175.56 (n/a)</td><td>194.60 (n/a)</td><td>117.30 (n/a)</td><td>36.50 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>1.02 (-11.80%)</td><td>0.83 (-2.36%)</td><td>0.78 (-7.66%)</td><td>0.67 (+11.64%)</td><td>0.13 <b>(-38.88%)</b></td><td>194.90 (-10.43%)</td><td>161.98 (-0.88%)</td><td>168.20 (+8.24%)</td><td>128.00 (+13.37%)</td><td>25.25 <b>(-39.08%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>1.16 (n/a)</td><td>0.85 (n/a)</td><td>0.84 (n/a)</td><td>0.60 (n/a)</td><td>0.22 (n/a)</td><td>217.60 (n/a)</td><td>163.42 (n/a)</td><td>155.40 (n/a)</td><td>112.90 (n/a)</td><td>41.45 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.00 (+9.09%)</td><td>0.00 (+19.57%)</td><td>0.00 <b>(+33.33%)</b></td><td>0.00 (+12.50%)</td><td>0.00 <b>(+29.10%)</b></td><td>4556.47 (-11.83%)</td><td>3826.12 (-13.66%)</td><td>3507.16 <b>(-21.94%)</b></td><td>3498.51 (-2.18%)</td><td>475.41 (-17.07%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>5168.09 (n/a)</td><td>4431.69 (n/a)</td><td>4492.92 (n/a)</td><td>3576.64 (n/a)</td><td>573.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.00 (+0.00%)</td><td>0.00 (+3.00%)</td><td>0.00 (+5.00%)</td><td>0.00 (+5.56%)</td><td>0.00 <b>(-27.89%)</b></td><td>4396.72 (-3.41%)</td><td>4030.10 (-2.90%)</td><td>3953.60 (-4.10%)</td><td>3713.01 (-2.47%)</td><td>262.71 (-15.65%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4552.05 (n/a)</td><td>4150.54 (n/a)</td><td>4122.63 (n/a)</td><td>3806.88 (n/a)</td><td>311.43 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>0.28 (+1.35%)</td><td>0.20 (-18.31%)</td><td>0.15 <b>(-37.95%)</b></td><td>0.15 <b>(-21.98%)</b></td><td>0.06 <b>(+106.69%)</b></td><td>14169.06 <b>(+28.16%)</b></td><td>11537.75 <b>(+30.49%)</b></td><td>13685.12 <b>(+61.10%)</b></td><td>7535.45 (-1.32%)</td><td>3355.70 <b>(+158.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>11055.95 (n/a)</td><td>8841.86 (n/a)</td><td>8494.64 (n/a)</td><td>7636.48 (n/a)</td><td>1298.01 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
