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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.08 (-7.91%)</td><td>0.07 (-6.42%)</td><td>0.07 (-3.27%)</td><td>0.05 (-14.17%)</td><td>0.01 (-7.37%)</td><td>233.50 (+16.52%)</td><td>185.56 (+7.06%)</td><td>181.80 (+3.41%)</td><td>148.50 (+8.63%)</td><td>30.53 (+18.39%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>173.32 (n/a)</td><td>175.80 (n/a)</td><td>136.70 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.08 (-9.24%)</td><td>0.07 (-5.36%)</td><td>0.07 (-10.93%)</td><td>0.06 (+11.25%)</td><td>0.00 <b>(-58.59%)</b></td><td>189.90 (-10.13%)</td><td>181.18 (+4.10%)</td><td>185.20 (+12.24%)</td><td>162.80 (+10.22%)</td><td>10.74 <b>(-59.55%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>174.04 (n/a)</td><td>165.00 (n/a)</td><td>147.70 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 <b>(-30.39%)</b></td><td>0.06 (-8.14%)</td><td>0.06 (-12.35%)</td><td>0.06 <b>(+90.56%)</b></td><td>0.00 <b>(-90.11%)</b></td><td>217.60 <b>(-47.52%)</b></td><td>210.26 (-4.90%)</td><td>212.00 (+14.10%)</td><td>199.80 <b>(+43.74%)</b></td><td>7.42 <b>(-93.25%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>414.60 (n/a)</td><td>221.10 (n/a)</td><td>185.80 (n/a)</td><td>139.00 (n/a)</td><td>109.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (-10.47%)</td><td>0.06 (+0.84%)</td><td>0.06 (+1.52%)</td><td>0.06 (+10.64%)</td><td>0.01 <b>(-38.22%)</b></td><td>216.00 (-9.62%)</td><td>193.76 (-2.10%)</td><td>195.00 (-1.52%)</td><td>171.10 (+11.68%)</td><td>19.86 <b>(-36.83%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>239.00 (n/a)</td><td>197.92 (n/a)</td><td>198.00 (n/a)</td><td>153.20 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (-6.54%)</td><td>0.04 (+8.53%)</td><td>0.03 (+13.75%)</td><td>0.03 (+10.86%)</td><td>0.01 <b>(-23.30%)</b></td><td>172.50 (-9.83%)</td><td>149.08 (-9.00%)</td><td>152.50 (-12.10%)</td><td>123.60 (+7.01%)</td><td>22.15 <b>(-23.14%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>163.82 (n/a)</td><td>173.50 (n/a)</td><td>115.50 (n/a)</td><td>28.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 <b>(+50.79%)</b></td><td>0.04 <b>(+38.27%)</b></td><td>0.04 <b>(+20.58%)</b></td><td>0.03 <b>(+34.84%)</b></td><td>0.01 <b>(+131.74%)</b></td><td>179.30 <b>(-25.85%)</b></td><td>141.24 <b>(-25.10%)</b></td><td>148.70 (-17.02%)</td><td>101.00 <b>(-33.68%)</b></td><td>36.59 (+9.80%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.80 (n/a)</td><td>188.58 (n/a)</td><td>179.20 (n/a)</td><td>152.30 (n/a)</td><td>33.32 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (+9.49%)</td><td>0.03 (+12.37%)</td><td>0.03 (+12.49%)</td><td>0.03 (+6.52%)</td><td>0.00 <b>(+39.22%)</b></td><td>198.10 (-6.11%)</td><td>169.66 (-10.59%)</td><td>167.80 (-11.12%)</td><td>148.90 (-8.71%)</td><td>21.03 (+19.11%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.00 (n/a)</td><td>189.76 (n/a)</td><td>188.80 (n/a)</td><td>163.10 (n/a)</td><td>17.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (+9.13%)</td><td>0.03 (+12.57%)</td><td>0.04 <b>(+20.97%)</b></td><td>0.03 (+11.80%)</td><td>0.00 (-0.56%)</td><td>174.60 (-10.55%)</td><td>153.36 (-11.35%)</td><td>147.50 (-17.32%)</td><td>133.80 (-8.36%)</td><td>17.23 (-17.51%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>195.20 (n/a)</td><td>173.00 (n/a)</td><td>178.40 (n/a)</td><td>146.00 (n/a)</td><td>20.88 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 <b>(+21.50%)</b></td><td>0.03 (+14.64%)</td><td>0.03 (+14.52%)</td><td>0.03 (+18.87%)</td><td>0.00 <b>(+20.40%)</b></td><td>174.20 (-15.89%)</td><td>160.38 (-12.79%)</td><td>170.10 (-12.68%)</td><td>125.50 (-17.70%)</td><td>20.03 (-18.17%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>207.10 (n/a)</td><td>183.90 (n/a)</td><td>194.80 (n/a)</td><td>152.50 (n/a)</td><td>24.47 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (+8.38%)</td><td>0.03 (+20.00%)</td><td>0.03 <b>(+23.28%)</b></td><td>0.03 <b>(+21.13%)</b></td><td>0.01 (-15.12%)</td><td>184.00 (-17.45%)</td><td>165.36 (-17.87%)</td><td>173.70 (-18.91%)</td><td>127.60 (-7.74%)</td><td>23.43 <b>(-34.26%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.90 (n/a)</td><td>201.34 (n/a)</td><td>214.20 (n/a)</td><td>138.30 (n/a)</td><td>35.64 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (+14.81%)</td><td>0.03 <b>(+25.80%)</b></td><td>0.03 (+11.71%)</td><td>0.03 <b>(+69.90%)</b></td><td>0.00 <b>(-44.26%)</b></td><td>194.90 <b>(-41.14%)</b></td><td>166.52 <b>(-24.53%)</b></td><td>165.90 (-10.52%)</td><td>145.20 (-12.90%)</td><td>19.04 <b>(-71.74%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>331.10 (n/a)</td><td>220.64 (n/a)</td><td>185.40 (n/a)</td><td>166.70 (n/a)</td><td>67.38 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.03 <b>(+27.91%)</b></td><td>0.02 (+15.60%)</td><td>0.02 (+7.09%)</td><td>0.02 (+1.20%)</td><td>0.00 <b>(+57.21%)</b></td><td>308.30 (-1.19%)</td><td>224.22 (-11.97%)</td><td>218.50 (-6.62%)</td><td>173.80 <b>(-21.82%)</b></td><td>50.69 <b>(+27.07%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>312.00 (n/a)</td><td>254.72 (n/a)</td><td>234.00 (n/a)</td><td>222.30 (n/a)</td><td>39.89 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>204.20 (n/a)</td><td>164.96 (n/a)</td><td>167.10 (n/a)</td><td>116.10 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>219.50 (n/a)</td><td>203.90 (n/a)</td><td>202.30 (n/a)</td><td>185.80 (n/a)</td><td>13.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>204.00 (n/a)</td><td>176.84 (n/a)</td><td>171.30 (n/a)</td><td>149.60 (n/a)</td><td>21.88 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>323.00 (n/a)</td><td>221.90 (n/a)</td><td>210.30 (n/a)</td><td>164.90 (n/a)</td><td>60.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>191.80 (n/a)</td><td>161.74 (n/a)</td><td>175.30 (n/a)</td><td>123.30 (n/a)</td><td>32.61 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.70 (n/a)</td><td>161.82 (n/a)</td><td>141.90 (n/a)</td><td>128.90 (n/a)</td><td>39.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.40 (n/a)</td><td>176.78 (n/a)</td><td>187.30 (n/a)</td><td>127.70 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>303.10 (n/a)</td><td>222.68 (n/a)</td><td>188.50 (n/a)</td><td>175.40 (n/a)</td><td>59.61 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>176.94 (n/a)</td><td>175.10 (n/a)</td><td>147.40 (n/a)</td><td>25.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.70 (n/a)</td><td>176.00 (n/a)</td><td>162.30 (n/a)</td><td>145.90 (n/a)</td><td>41.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>179.20 (n/a)</td><td>176.50 (n/a)</td><td>143.20 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>194.80 (n/a)</td><td>181.24 (n/a)</td><td>180.80 (n/a)</td><td>167.10 (n/a)</td><td>10.05 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>173.10 (n/a)</td><td>163.06 (n/a)</td><td>163.30 (n/a)</td><td>147.50 (n/a)</td><td>10.11 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>182.90 (n/a)</td><td>175.22 (n/a)</td><td>178.60 (n/a)</td><td>161.80 (n/a)</td><td>9.15 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.00 (n/a)</td><td>188.46 (n/a)</td><td>189.90 (n/a)</td><td>164.30 (n/a)</td><td>16.46 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>302.80 (n/a)</td><td>231.14 (n/a)</td><td>205.40 (n/a)</td><td>199.10 (n/a)</td><td>43.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>4.95 (+2.36%)</td><td>3.90 (-6.89%)</td><td>3.50 (-16.47%)</td><td>3.44 (-3.09%)</td><td>0.66 <b>(+30.69%)</b></td><td>2736.30 (+3.19%)</td><td>2463.82 (+8.34%)</td><td>2683.30 (+19.72%)</td><td>1899.20 (-2.31%)</td><td>370.89 <b>(+33.65%)</b></td><td>1947.90 (+2.36%)</td><td>1532.65 (-6.89%)</td><td>1378.66 (-16.47%)</td><td>1351.98 (-3.09%)</td><td>259.78 <b>(+30.69%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>4.84 (n/a)</td><td>4.18 (n/a)</td><td>4.20 (n/a)</td><td>3.55 (n/a)</td><td>0.51 (n/a)</td><td>2651.70 (n/a)</td><td>2274.06 (n/a)</td><td>2241.30 (n/a)</td><td>1944.10 (n/a)</td><td>277.51 (n/a)</td><td>1902.90 (n/a)</td><td>1646.11 (n/a)</td><td>1650.56 (n/a)</td><td>1395.12 (n/a)</td><td>198.78 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>1.19 (+5.46%)</td><td>0.86 (-1.70%)</td><td>0.71 (-14.35%)</td><td>0.64 (-0.82%)</td><td>0.26 <b>(+39.73%)</b></td><td>346.40 (+0.81%)</td><td>277.04 (+5.16%)</td><td>313.40 (+16.72%)</td><td>185.60 (-5.16%)</td><td>77.21 <b>(+35.03%)</b></td><td>50.85 (+5.46%)</td><td>36.58 (-1.70%)</td><td>30.11 (-14.35%)</td><td>27.25 (-0.82%)</td><td>11.30 <b>(+39.73%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>1.13 (n/a)</td><td>0.87 (n/a)</td><td>0.82 (n/a)</td><td>0.64 (n/a)</td><td>0.19 (n/a)</td><td>343.60 (n/a)</td><td>263.44 (n/a)</td><td>268.50 (n/a)</td><td>195.70 (n/a)</td><td>57.18 (n/a)</td><td>48.22 (n/a)</td><td>37.21 (n/a)</td><td>35.15 (n/a)</td><td>27.47 (n/a)</td><td>8.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>1.27 (+9.81%)</td><td>0.95 (-3.91%)</td><td>1.02 (-5.43%)</td><td>0.66 (-8.07%)</td><td>0.28 <b>(+37.38%)</b></td><td>335.20 (+8.76%)</td><td>250.54 (+7.86%)</td><td>217.20 (+5.74%)</td><td>173.60 (-8.92%)</td><td>76.50 <b>(+46.65%)</b></td><td>54.37 (+9.81%)</td><td>40.51 (-3.91%)</td><td>43.44 (-5.43%)</td><td>28.15 (-8.07%)</td><td>11.74 <b>(+37.38%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>1.16 (n/a)</td><td>0.99 (n/a)</td><td>1.08 (n/a)</td><td>0.72 (n/a)</td><td>0.20 (n/a)</td><td>308.20 (n/a)</td><td>232.28 (n/a)</td><td>205.40 (n/a)</td><td>190.60 (n/a)</td><td>52.17 (n/a)</td><td>49.51 (n/a)</td><td>42.16 (n/a)</td><td>45.94 (n/a)</td><td>30.62 (n/a)</td><td>8.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.52 (+0.10%)</td><td>0.52 (-0.02%)</td><td>0.52 (-0.06%)</td><td>0.52 (-0.04%)</td><td>0.00 <b>(+27.21%)</b></td><td>48650.60 (+0.04%)</td><td>48566.26 (+0.02%)</td><td>48631.40 (+0.06%)</td><td>48290.40 (-0.10%)</td><td>154.51 <b>(+27.09%)</b></td><td>355.76 (+0.10%)</td><td>353.74 (-0.02%)</td><td>353.27 (-0.06%)</td><td>353.13 (-0.04%)</td><td>1.13 <b>(+27.21%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48632.50 (n/a)</td><td>48555.66 (n/a)</td><td>48600.50 (n/a)</td><td>48339.50 (n/a)</td><td>121.57 (n/a)</td><td>355.40 (n/a)</td><td>353.82 (n/a)</td><td>353.49 (n/a)</td><td>353.26 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.89 (+0.05%)</td><td>0.89 (-0.13%)</td><td>0.89 (+0.33%)</td><td>0.88 (-0.64%)</td><td>0.01 <b>(+85.41%)</b></td><td>28739.40 (+0.65%)</td><td>28423.34 (+0.13%)</td><td>28289.80 (-0.33%)</td><td>28200.10 (-0.05%)</td><td>267.62 <b>(+86.48%)</b></td><td>609.21 (+0.05%)</td><td>604.47 (-0.13%)</td><td>607.28 (+0.33%)</td><td>597.78 (-0.64%)</td><td>5.67 <b>(+85.41%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.00 (n/a)</td><td>28555.00 (n/a)</td><td>28386.32 (n/a)</td><td>28384.30 (n/a)</td><td>28213.40 (n/a)</td><td>143.51 (n/a)</td><td>608.93 (n/a)</td><td>605.23 (n/a)</td><td>605.26 (n/a)</td><td>601.64 (n/a)</td><td>3.06 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>3.33 (+0.71%)</td><td>3.25 (+0.30%)</td><td>3.30 (+3.37%)</td><td>3.12 (-2.08%)</td><td>0.09 <b>(+49.39%)</b></td><td>8062.80 (+2.12%)</td><td>7758.50 (-0.26%)</td><td>7625.70 (-3.26%)</td><td>7554.00 (-0.71%)</td><td>228.02 <b>(+51.41%)</b></td><td>2274.28 (+0.71%)</td><td>2215.85 (+0.30%)</td><td>2252.90 (+3.37%)</td><td>2130.76 (-2.08%)</td><td>64.34 <b>(+49.39%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>3.31 (n/a)</td><td>3.24 (n/a)</td><td>3.19 (n/a)</td><td>3.19 (n/a)</td><td>0.06 (n/a)</td><td>7895.30 (n/a)</td><td>7779.08 (n/a)</td><td>7882.70 (n/a)</td><td>7607.90 (n/a)</td><td>150.60 (n/a)</td><td>2258.15 (n/a)</td><td>2209.14 (n/a)</td><td>2179.44 (n/a)</td><td>2175.97 (n/a)</td><td>43.07 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>4.10 (+12.07%)</td><td>3.47 (+8.83%)</td><td>3.24 (+8.50%)</td><td>3.08 (+8.28%)</td><td>0.45 (+18.28%)</td><td>2617.00 (-7.65%)</td><td>2350.70 (-7.95%)</td><td>2491.50 (-7.83%)</td><td>1965.10 (-10.77%)</td><td>286.02 (-1.69%)</td><td>1075.75 (+12.07%)</td><td>910.67 (+8.83%)</td><td>848.45 (+8.50%)</td><td>807.78 (+8.28%)</td><td>117.24 (+18.28%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>3.66 (n/a)</td><td>3.19 (n/a)</td><td>2.98 (n/a)</td><td>2.84 (n/a)</td><td>0.38 (n/a)</td><td>2833.70 (n/a)</td><td>2553.76 (n/a)</td><td>2703.20 (n/a)</td><td>2202.30 (n/a)</td><td>290.93 (n/a)</td><td>959.87 (n/a)</td><td>836.80 (n/a)</td><td>782.01 (n/a)</td><td>746.01 (n/a)</td><td>99.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.51 (-10.64%)</td><td>0.37 (-14.41%)</td><td>0.34 (+0.62%)</td><td>0.28 (-17.72%)</td><td>0.09 <b>(-27.14%)</b></td><td>4506.10 <b>(+21.53%)</b></td><td>3551.74 (+14.63%)</td><td>3642.70 (-0.62%)</td><td>2437.50 (+11.90%)</td><td>763.49 (-4.77%)</td><td>27.53 (-10.64%)</td><td>19.70 (-14.41%)</td><td>18.42 (+0.62%)</td><td>14.89 (-17.72%)</td><td>4.80 <b>(-27.14%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.57 (n/a)</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>3707.80 (n/a)</td><td>3098.46 (n/a)</td><td>3665.30 (n/a)</td><td>2178.20 (n/a)</td><td>801.73 (n/a)</td><td>30.81 (n/a)</td><td>23.02 (n/a)</td><td>18.31 (n/a)</td><td>18.10 (n/a)</td><td>6.59 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>6.26 (+2.20%)</td><td>4.57 (+6.83%)</td><td>4.69 <b>(+30.91%)</b></td><td>3.34 (-4.67%)</td><td>1.12 (-0.44%)</td><td>1988.90 (+4.90%)</td><td>1524.12 (-6.43%)</td><td>1419.50 <b>(-23.61%)</b></td><td>1062.30 (-2.16%)</td><td>359.03 (+0.77%)</td><td>1934.60 (+2.20%)</td><td>1412.60 (+6.83%)</td><td>1447.81 <b>(+30.91%)</b></td><td>1033.33 (-4.67%)</td><td>347.48 (-0.44%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>6.13 (n/a)</td><td>4.28 (n/a)</td><td>3.58 (n/a)</td><td>3.51 (n/a)</td><td>1.13 (n/a)</td><td>1896.00 (n/a)</td><td>1628.84 (n/a)</td><td>1858.30 (n/a)</td><td>1085.70 (n/a)</td><td>356.27 (n/a)</td><td>1892.92 (n/a)</td><td>1322.29 (n/a)</td><td>1105.96 (n/a)</td><td>1083.99 (n/a)</td><td>349.01 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>13.29 (n/a)</td><td>12.49 (n/a)</td><td>13.03 (n/a)</td><td>10.96 (n/a)</td><td>1.02 (n/a)</td><td>13.28 (n/a)</td><td>12.49 (n/a)</td><td>13.02 (n/a)</td><td>10.95 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>24.88 (+2.20%)</td><td>23.80 (-0.02%)</td><td>23.92 (+0.14%)</td><td>23.01 (-1.55%)</td><td>0.77 <b>(+94.17%)</b></td><td>24.86 (+2.20%)</td><td>23.79 (-0.02%)</td><td>23.90 (+0.14%)</td><td>22.99 (-1.55%)</td><td>0.77 <b>(+94.17%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>24.34 (n/a)</td><td>23.81 (n/a)</td><td>23.88 (n/a)</td><td>23.37 (n/a)</td><td>0.40 (n/a)</td><td>24.33 (n/a)</td><td>23.79 (n/a)</td><td>23.87 (n/a)</td><td>23.35 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>41.32 (+2.40%)</td><td>37.37 (-5.89%)</td><td>38.24 (-3.17%)</td><td>30.83 <b>(-21.80%)</b></td><td>4.12 <b>(+929.23%)</b></td><td>41.30 (+2.40%)</td><td>37.35 (-5.89%)</td><td>38.21 (-3.17%)</td><td>30.81 <b>(-21.80%)</b></td><td>4.12 <b>(+929.23%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>40.35 (n/a)</td><td>39.71 (n/a)</td><td>39.49 (n/a)</td><td>39.42 (n/a)</td><td>0.40 (n/a)</td><td>40.33 (n/a)</td><td>39.69 (n/a)</td><td>39.46 (n/a)</td><td>39.40 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>43.44 (-2.11%)</td><td>40.80 (-3.45%)</td><td>41.44 (-6.00%)</td><td>35.91 (-3.08%)</td><td>2.92 (-7.53%)</td><td>43.42 (-2.11%)</td><td>40.78 (-3.45%)</td><td>41.42 (-6.00%)</td><td>35.88 (-3.08%)</td><td>2.92 (-7.53%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>44.38 (n/a)</td><td>42.26 (n/a)</td><td>44.09 (n/a)</td><td>37.05 (n/a)</td><td>3.16 (n/a)</td><td>44.35 (n/a)</td><td>42.23 (n/a)</td><td>44.06 (n/a)</td><td>37.02 (n/a)</td><td>3.16 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>13.30 (n/a)</td><td>12.06 (n/a)</td><td>12.52 (n/a)</td><td>10.47 (n/a)</td><td>1.25 (n/a)</td><td>13.29 (n/a)</td><td>12.05 (n/a)</td><td>12.51 (n/a)</td><td>10.47 (n/a)</td><td>1.25 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>24.24 (-1.22%)</td><td>23.91 (+0.46%)</td><td>24.10 (+1.34%)</td><td>23.37 (+1.85%)</td><td>0.37 <b>(-34.65%)</b></td><td>24.22 (-1.22%)</td><td>23.89 (+0.46%)</td><td>24.09 (+1.34%)</td><td>23.35 (+1.85%)</td><td>0.37 <b>(-34.65%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>24.54 (n/a)</td><td>23.80 (n/a)</td><td>23.78 (n/a)</td><td>22.94 (n/a)</td><td>0.57 (n/a)</td><td>24.52 (n/a)</td><td>23.78 (n/a)</td><td>23.77 (n/a)</td><td>22.93 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>39.55 (-4.63%)</td><td>37.67 (-2.34%)</td><td>38.35 (-3.67%)</td><td>33.65 (+4.40%)</td><td>2.38 <b>(-34.50%)</b></td><td>39.52 (-4.63%)</td><td>37.65 (-2.34%)</td><td>38.32 (-3.67%)</td><td>33.63 (+4.40%)</td><td>2.38 <b>(-34.50%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>41.47 (n/a)</td><td>38.57 (n/a)</td><td>39.81 (n/a)</td><td>32.23 (n/a)</td><td>3.64 (n/a)</td><td>41.44 (n/a)</td><td>38.55 (n/a)</td><td>39.78 (n/a)</td><td>32.21 (n/a)</td><td>3.63 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>47.89 (+7.09%)</td><td>42.19 (-0.20%)</td><td>42.36 (-2.03%)</td><td>37.12 (-6.87%)</td><td>3.93 <b>(+78.93%)</b></td><td>47.86 (+7.09%)</td><td>42.16 (-0.20%)</td><td>42.34 (-2.03%)</td><td>37.09 (-6.87%)</td><td>3.93 <b>(+78.93%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>44.72 (n/a)</td><td>42.27 (n/a)</td><td>43.24 (n/a)</td><td>39.85 (n/a)</td><td>2.20 (n/a)</td><td>44.70 (n/a)</td><td>42.24 (n/a)</td><td>43.21 (n/a)</td><td>39.83 (n/a)</td><td>2.20 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>9.74 (+1.37%)</td><td>9.27 (+7.76%)</td><td>9.03 (+7.44%)</td><td>8.94 (+14.98%)</td><td>0.40 <b>(-42.48%)</b></td><td>9.72 (+1.37%)</td><td>9.25 (+7.76%)</td><td>9.01 (+7.44%)</td><td>8.92 (+14.98%)</td><td>0.40 <b>(-42.48%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>9.61 (n/a)</td><td>8.60 (n/a)</td><td>8.40 (n/a)</td><td>7.77 (n/a)</td><td>0.70 (n/a)</td><td>9.59 (n/a)</td><td>8.59 (n/a)</td><td>8.39 (n/a)</td><td>7.76 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.84 (-11.31%)</td><td>0.78 (+0.61%)</td><td>0.77 (+6.08%)</td><td>0.72 (+5.18%)</td><td>0.04 <b>(-56.77%)</b></td><td>0.82 (-11.31%)</td><td>0.76 (+0.61%)</td><td>0.76 (+6.08%)</td><td>0.71 (+5.18%)</td><td>0.04 <b>(-56.77%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.94 (n/a)</td><td>0.77 (n/a)</td><td>0.73 (n/a)</td><td>0.69 (n/a)</td><td>0.10 (n/a)</td><td>0.93 (n/a)</td><td>0.76 (n/a)</td><td>0.72 (n/a)</td><td>0.68 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>1.29 (+0.18%)</td><td>1.11 (+0.63%)</td><td>1.14 (+4.94%)</td><td>0.88 (-0.68%)</td><td>0.17 (+11.19%)</td><td>1.27 (+0.18%)</td><td>1.10 (+0.63%)</td><td>1.12 (+4.94%)</td><td>0.87 (-0.68%)</td><td>0.16 (+11.19%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>1.28 (n/a)</td><td>1.10 (n/a)</td><td>1.08 (n/a)</td><td>0.89 (n/a)</td><td>0.15 (n/a)</td><td>1.27 (n/a)</td><td>1.09 (n/a)</td><td>1.07 (n/a)</td><td>0.88 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>17.58 (+12.92%)</td><td>15.90 (+6.72%)</td><td>15.34 (+4.64%)</td><td>14.26 (-0.61%)</td><td>1.35 <b>(+141.81%)</b></td><td>17.38 (+12.92%)</td><td>15.71 (+6.72%)</td><td>15.17 (+4.64%)</td><td>14.10 (-0.61%)</td><td>1.34 <b>(+141.81%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>15.57 (n/a)</td><td>14.90 (n/a)</td><td>14.66 (n/a)</td><td>14.35 (n/a)</td><td>0.56 (n/a)</td><td>15.39 (n/a)</td><td>14.72 (n/a)</td><td>14.49 (n/a)</td><td>14.19 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>12.84 (+6.36%)</td><td>12.07 (+2.62%)</td><td>11.95 (+2.58%)</td><td>11.60 (+0.62%)</td><td>0.46 <b>(+100.72%)</b></td><td>12.62 (+6.36%)</td><td>11.86 (+2.62%)</td><td>11.74 (+2.58%)</td><td>11.40 (+0.62%)</td><td>0.46 <b>(+100.72%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>12.07 (n/a)</td><td>11.76 (n/a)</td><td>11.65 (n/a)</td><td>11.53 (n/a)</td><td>0.23 (n/a)</td><td>11.86 (n/a)</td><td>11.56 (n/a)</td><td>11.44 (n/a)</td><td>11.33 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>8.13 (-2.27%)</td><td>7.76 (+4.47%)</td><td>7.96 (+7.57%)</td><td>7.31 (+11.88%)</td><td>0.38 <b>(-53.67%)</b></td><td>7.99 (-2.27%)</td><td>7.63 (+4.47%)</td><td>7.82 (+7.57%)</td><td>7.18 (+11.88%)</td><td>0.37 <b>(-53.67%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>8.32 (n/a)</td><td>7.43 (n/a)</td><td>7.40 (n/a)</td><td>6.53 (n/a)</td><td>0.82 (n/a)</td><td>8.18 (n/a)</td><td>7.30 (n/a)</td><td>7.27 (n/a)</td><td>6.42 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>5.92 (-16.33%)</td><td>5.79 (+8.31%)</td><td>5.78 (+17.04%)</td><td>5.59 <b>(+38.00%)</b></td><td>0.13 <b>(-88.47%)</b></td><td>5.82 (-16.33%)</td><td>5.70 (+8.31%)</td><td>5.69 (+17.04%)</td><td>5.50 <b>(+38.00%)</b></td><td>0.13 <b>(-88.47%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>7.07 (n/a)</td><td>5.35 (n/a)</td><td>4.94 (n/a)</td><td>4.05 (n/a)</td><td>1.15 (n/a)</td><td>6.96 (n/a)</td><td>5.26 (n/a)</td><td>4.86 (n/a)</td><td>3.99 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>13.37 (n/a)</td><td>12.77 (n/a)</td><td>13.33 (n/a)</td><td>11.52 (n/a)</td><td>0.83 (n/a)</td><td>13.36 (n/a)</td><td>12.76 (n/a)</td><td>13.32 (n/a)</td><td>11.52 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>13.58 (n/a)</td><td>12.75 (n/a)</td><td>13.29 (n/a)</td><td>10.91 (n/a)</td><td>1.09 (n/a)</td><td>13.57 (n/a)</td><td>12.74 (n/a)</td><td>13.28 (n/a)</td><td>10.90 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.40 (n/a)</td><td>170.86 (n/a)</td><td>166.60 (n/a)</td><td>157.60 (n/a)</td><td>14.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.60 (n/a)</td><td>168.26 (n/a)</td><td>166.20 (n/a)</td><td>137.30 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>283.20 (n/a)</td><td>184.26 (n/a)</td><td>164.70 (n/a)</td><td>144.70 (n/a)</td><td>56.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.50 (n/a)</td><td>158.04 (n/a)</td><td>157.60 (n/a)</td><td>136.40 (n/a)</td><td>22.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.60 (n/a)</td><td>194.62 (n/a)</td><td>184.90 (n/a)</td><td>135.90 (n/a)</td><td>44.53 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.10 (n/a)</td><td>155.92 (n/a)</td><td>153.10 (n/a)</td><td>124.60 (n/a)</td><td>24.32 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>185.78 (n/a)</td><td>190.60 (n/a)</td><td>135.20 (n/a)</td><td>37.71 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.10 (n/a)</td><td>204.52 (n/a)</td><td>195.00 (n/a)</td><td>192.70 (n/a)</td><td>16.90 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (-5.31%)</td><td>0.05 <b>(-20.23%)</b></td><td>0.05 <b>(-26.84%)</b></td><td>0.03 <b>(-29.93%)</b></td><td>0.01 <b>(+35.30%)</b></td><td>247.80 <b>(+42.74%)</b></td><td>179.84 <b>(+29.16%)</b></td><td>175.80 <b>(+36.70%)</b></td><td>125.60 (+5.63%)</td><td>44.43 <b>(+102.63%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.60 (n/a)</td><td>139.24 (n/a)</td><td>128.60 (n/a)</td><td>118.90 (n/a)</td><td>21.93 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (+13.29%)</td><td>0.05 (+3.60%)</td><td>0.04 (-15.17%)</td><td>0.04 <b>(+26.03%)</b></td><td>0.01 (+0.16%)</td><td>205.80 <b>(-20.66%)</b></td><td>172.16 (-5.20%)</td><td>182.80 (+17.86%)</td><td>117.80 (-11.76%)</td><td>34.09 <b>(-32.96%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.40 (n/a)</td><td>181.60 (n/a)</td><td>155.10 (n/a)</td><td>133.50 (n/a)</td><td>50.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (-15.43%)</td><td>0.04 (-16.33%)</td><td>0.05 (-15.88%)</td><td>0.03 (-15.74%)</td><td>0.01 (-5.17%)</td><td>249.70 (+18.68%)</td><td>191.16 <b>(+20.20%)</b></td><td>180.60 (+18.89%)</td><td>154.80 (+18.26%)</td><td>39.00 <b>(+28.00%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>159.04 (n/a)</td><td>151.90 (n/a)</td><td>130.90 (n/a)</td><td>30.47 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (-17.07%)</td><td>0.04 <b>(-21.16%)</b></td><td>0.04 <b>(-29.68%)</b></td><td>0.03 (-17.65%)</td><td>0.01 (-10.76%)</td><td>279.60 <b>(+21.46%)</b></td><td>220.48 <b>(+27.58%)</b></td><td>219.40 <b>(+42.19%)</b></td><td>161.50 <b>(+20.61%)</b></td><td>49.71 <b>(+29.37%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>172.82 (n/a)</td><td>154.30 (n/a)</td><td>133.90 (n/a)</td><td>38.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (-7.51%)</td><td>0.05 (-11.75%)</td><td>0.05 (-10.37%)</td><td>0.03 (-7.74%)</td><td>0.01 <b>(-21.09%)</b></td><td>237.00 (+8.37%)</td><td>185.44 (+12.17%)</td><td>178.10 (+11.59%)</td><td>139.90 (+8.11%)</td><td>36.38 (-4.69%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>165.32 (n/a)</td><td>159.60 (n/a)</td><td>129.40 (n/a)</td><td>38.16 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (-17.28%)</td><td>0.05 <b>(-20.99%)</b></td><td>0.04 <b>(-23.36%)</b></td><td>0.04 <b>(-27.19%)</b></td><td>0.01 <b>(+33.78%)</b></td><td>210.50 <b>(+37.31%)</b></td><td>184.22 <b>(+27.81%)</b></td><td>192.30 <b>(+30.46%)</b></td><td>152.60 <b>(+20.92%)</b></td><td>24.41 <b>(+121.48%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>153.30 (n/a)</td><td>144.14 (n/a)</td><td>147.40 (n/a)</td><td>126.20 (n/a)</td><td>11.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (-19.18%)</td><td>0.04 <b>(-25.66%)</b></td><td>0.04 <b>(-23.45%)</b></td><td>0.03 <b>(-42.50%)</b></td><td>0.01 <b>(+48.41%)</b></td><td>302.80 <b>(+73.92%)</b></td><td>217.00 <b>(+39.32%)</b></td><td>203.90 <b>(+30.62%)</b></td><td>161.30 <b>(+23.79%)</b></td><td>53.79 <b>(+231.84%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.10 (n/a)</td><td>155.76 (n/a)</td><td>156.10 (n/a)</td><td>130.30 (n/a)</td><td>16.21 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (-11.13%)</td><td>0.04 (-16.19%)</td><td>0.04 (-19.43%)</td><td>0.03 <b>(-24.34%)</b></td><td>0.01 (+11.64%)</td><td>311.40 <b>(+32.17%)</b></td><td>216.78 <b>(+22.25%)</b></td><td>205.50 <b>(+24.17%)</b></td><td>157.70 (+12.48%)</td><td>59.90 <b>(+64.33%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.60 (n/a)</td><td>177.32 (n/a)</td><td>165.50 (n/a)</td><td>140.20 (n/a)</td><td>36.45 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (-16.51%)</td><td>0.04 (-16.68%)</td><td>0.04 (-19.03%)</td><td>0.03 (-13.07%)</td><td>0.01 (-19.67%)</td><td>238.50 (+15.00%)</td><td>202.32 (+19.77%)</td><td>204.90 <b>(+23.51%)</b></td><td>167.70 (+19.79%)</td><td>26.50 (+8.50%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.40 (n/a)</td><td>168.92 (n/a)</td><td>165.90 (n/a)</td><td>140.00 (n/a)</td><td>24.42 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (+1.10%)</td><td>0.04 (-8.13%)</td><td>0.04 (-12.82%)</td><td>0.03 (-0.75%)</td><td>0.00 (-0.60%)</td><td>234.90 (+0.77%)</td><td>208.18 (+8.81%)</td><td>206.20 (+14.68%)</td><td>173.00 (-1.09%)</td><td>23.40 (-2.95%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.10 (n/a)</td><td>191.32 (n/a)</td><td>179.80 (n/a)</td><td>174.90 (n/a)</td><td>24.11 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (-11.72%)</td><td>0.05 (+5.10%)</td><td>0.06 <b>(+20.28%)</b></td><td>0.05 <b>(+30.78%)</b></td><td>0.01 <b>(-55.58%)</b></td><td>175.80 <b>(-23.53%)</b></td><td>153.54 (-9.37%)</td><td>143.20 (-16.89%)</td><td>138.60 (+13.24%)</td><td>18.34 <b>(-60.01%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>169.42 (n/a)</td><td>172.30 (n/a)</td><td>122.40 (n/a)</td><td>45.86 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 <b>(-21.50%)</b></td><td>0.04 (-14.38%)</td><td>0.04 (-15.82%)</td><td>0.03 (-2.59%)</td><td>0.00 <b>(-67.54%)</b></td><td>235.10 (+2.66%)</td><td>219.04 (+15.55%)</td><td>219.50 (+18.78%)</td><td>208.40 <b>(+27.38%)</b></td><td>10.22 <b>(-58.12%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.00 (n/a)</td><td>189.56 (n/a)</td><td>184.80 (n/a)</td><td>163.60 (n/a)</td><td>24.39 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (-12.08%)</td><td>0.05 (-6.75%)</td><td>0.06 (+1.61%)</td><td>0.04 <b>(-25.45%)</b></td><td>0.01 <b>(+28.94%)</b></td><td>233.50 <b>(+34.12%)</b></td><td>169.08 (+9.37%)</td><td>148.00 (-1.53%)</td><td>144.20 (+13.72%)</td><td>37.68 <b>(+95.61%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.10 (n/a)</td><td>154.60 (n/a)</td><td>150.30 (n/a)</td><td>126.80 (n/a)</td><td>19.26 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (+8.19%)</td><td>0.05 (-2.25%)</td><td>0.05 (-5.37%)</td><td>0.04 (+5.26%)</td><td>0.01 (+10.65%)</td><td>189.00 (-4.98%)</td><td>157.80 (+2.48%)</td><td>151.60 (+5.72%)</td><td>122.10 (-7.57%)</td><td>26.62 (-2.59%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>153.98 (n/a)</td><td>143.40 (n/a)</td><td>132.10 (n/a)</td><td>27.32 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 <b>(+20.79%)</b></td><td>0.06 (+16.69%)</td><td>0.06 (+17.26%)</td><td>0.05 (+17.47%)</td><td>0.01 (+12.07%)</td><td>158.90 (-14.84%)</td><td>140.28 (-14.42%)</td><td>137.80 (-14.73%)</td><td>118.30 (-17.21%)</td><td>16.04 <b>(-20.65%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.60 (n/a)</td><td>163.92 (n/a)</td><td>161.60 (n/a)</td><td>142.90 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (+1.00%)</td><td>0.05 (+11.60%)</td><td>0.05 (-5.12%)</td><td>0.05 <b>(+125.30%)</b></td><td>0.00 <b>(-76.63%)</b></td><td>161.90 <b>(-55.61%)</b></td><td>153.08 <b>(-20.97%)</b></td><td>158.80 (+5.37%)</td><td>141.10 (-1.05%)</td><td>9.62 <b>(-90.00%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>364.70 (n/a)</td><td>193.70 (n/a)</td><td>150.70 (n/a)</td><td>142.60 (n/a)</td><td>96.14 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (-0.61%)</td><td>0.05 (+3.45%)</td><td>0.05 (+10.83%)</td><td>0.04 (-6.94%)</td><td>0.01 <b>(+29.11%)</b></td><td>219.80 (+7.48%)</td><td>176.76 (-2.61%)</td><td>160.70 (-9.82%)</td><td>156.50 (+0.58%)</td><td>27.73 <b>(+36.01%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>181.50 (n/a)</td><td>178.20 (n/a)</td><td>155.60 (n/a)</td><td>20.38 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.08 <b>(+41.68%)</b></td><td>0.05 (+7.71%)</td><td>0.05 (+9.40%)</td><td>0.03 <b>(-31.69%)</b></td><td>0.02 <b>(+401.24%)</b></td><td>281.10 <b>(+46.41%)</b></td><td>180.00 (+5.24%)</td><td>152.40 (-8.58%)</td><td>109.20 <b>(-29.41%)</b></td><td>74.34 <b>(+419.07%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>192.00 (n/a)</td><td>171.04 (n/a)</td><td>166.70 (n/a)</td><td>154.70 (n/a)</td><td>14.32 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.21 (-1.06%)</td><td>0.21 (-0.49%)</td><td>0.21 (-0.20%)</td><td>0.21 (-0.08%)</td><td>0.00 <b>(-87.36%)</b></td><td>40898.00 (+0.08%)</td><td>40855.52 (+0.49%)</td><td>40849.90 (+0.20%)</td><td>40823.40 (+1.07%)</td><td>30.68 <b>(-87.21%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40867.10 (n/a)</td><td>40655.64 (n/a)</td><td>40770.20 (n/a)</td><td>40389.60 (n/a)</td><td>239.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (+1.77%)</td><td>0.05 (+2.77%)</td><td>0.05 (+5.61%)</td><td>0.04 (+10.60%)</td><td>0.01 (+7.32%)</td><td>205.70 (-9.58%)</td><td>170.24 (-2.63%)</td><td>167.30 (-5.32%)</td><td>136.40 (-1.73%)</td><td>31.86 (-5.13%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.50 (n/a)</td><td>174.84 (n/a)</td><td>176.70 (n/a)</td><td>138.80 (n/a)</td><td>33.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.09 (+5.03%)</td><td>0.07 (+1.87%)</td><td>0.07 (+4.82%)</td><td>0.05 (+0.93%)</td><td>0.01 (+10.79%)</td><td>233.50 (-0.89%)</td><td>187.92 (-1.44%)</td><td>183.50 (-4.63%)</td><td>136.20 (-4.76%)</td><td>35.94 (+3.84%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>235.60 (n/a)</td><td>190.66 (n/a)</td><td>192.40 (n/a)</td><td>143.00 (n/a)</td><td>34.61 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (+7.20%)</td><td>0.05 (+7.69%)</td><td>0.05 (+8.04%)</td><td>0.04 (+16.70%)</td><td>0.01 (+3.14%)</td><td>193.30 (-14.32%)</td><td>160.66 (-7.50%)</td><td>159.90 (-7.41%)</td><td>130.00 (-6.68%)</td><td>26.10 (-19.24%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.60 (n/a)</td><td>173.68 (n/a)</td><td>172.70 (n/a)</td><td>139.30 (n/a)</td><td>32.32 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (+5.97%)</td><td>0.06 (+0.73%)</td><td>0.05 (-11.57%)</td><td>0.05 (+4.05%)</td><td>0.01 <b>(+29.04%)</b></td><td>220.60 (-3.88%)</td><td>187.40 (+0.13%)</td><td>201.80 (+13.12%)</td><td>148.60 (-5.65%)</td><td>32.91 (+14.91%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.50 (n/a)</td><td>187.16 (n/a)</td><td>178.40 (n/a)</td><td>157.50 (n/a)</td><td>28.64 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (-6.38%)</td><td>0.05 (+0.80%)</td><td>0.04 (-1.98%)</td><td>0.04 (+0.74%)</td><td>0.01 (-5.25%)</td><td>201.00 (-0.69%)</td><td>173.86 (-0.89%)</td><td>188.80 (+2.00%)</td><td>135.50 (+6.78%)</td><td>31.74 (+1.38%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>175.42 (n/a)</td><td>185.10 (n/a)</td><td>126.90 (n/a)</td><td>31.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (-12.01%)</td><td>0.05 (-6.28%)</td><td>0.05 (+2.34%)</td><td>0.04 (-16.20%)</td><td>0.01 (-0.03%)</td><td>263.40 (+19.29%)</td><td>211.06 (+7.94%)</td><td>206.40 (-2.32%)</td><td>157.40 (+13.65%)</td><td>47.17 <b>(+41.09%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>220.80 (n/a)</td><td>195.54 (n/a)</td><td>211.30 (n/a)</td><td>138.50 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (+0.02%)</td><td>0.04 (+1.18%)</td><td>0.04 (+11.67%)</td><td>0.03 (-10.81%)</td><td>0.01 (+7.76%)</td><td>265.20 (+12.14%)</td><td>195.16 (-0.11%)</td><td>189.40 (-10.45%)</td><td>139.10 (+0.00%)</td><td>47.14 <b>(+23.36%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.50 (n/a)</td><td>195.38 (n/a)</td><td>211.50 (n/a)</td><td>139.10 (n/a)</td><td>38.21 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (-19.42%)</td><td>0.05 (-1.46%)</td><td>0.05 (+15.46%)</td><td>0.04 (-0.23%)</td><td>0.01 <b>(-46.61%)</b></td><td>243.70 (+0.25%)</td><td>192.84 (-1.59%)</td><td>187.40 (-13.40%)</td><td>162.80 <b>(+24.09%)</b></td><td>30.84 <b>(-31.06%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>243.10 (n/a)</td><td>195.96 (n/a)</td><td>216.40 (n/a)</td><td>131.20 (n/a)</td><td>44.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 <b>(+22.29%)</b></td><td>0.05 (+14.57%)</td><td>0.05 (+18.72%)</td><td>0.04 (+5.78%)</td><td>0.01 <b>(+63.11%)</b></td><td>223.00 (-5.47%)</td><td>177.66 (-11.74%)</td><td>171.20 (-15.79%)</td><td>143.90 (-18.24%)</td><td>30.04 <b>(+27.94%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>235.90 (n/a)</td><td>201.30 (n/a)</td><td>203.30 (n/a)</td><td>176.00 (n/a)</td><td>23.48 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.08 <b>(+50.76%)</b></td><td>0.06 (+16.30%)</td><td>0.05 (+7.25%)</td><td>0.04 (-8.66%)</td><td>0.02 <b>(+258.31%)</b></td><td>233.20 (+9.48%)</td><td>176.40 (-9.14%)</td><td>184.40 (-6.77%)</td><td>110.20 <b>(-33.69%)</b></td><td>45.31 <b>(+153.14%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.00 (n/a)</td><td>194.14 (n/a)</td><td>197.80 (n/a)</td><td>166.20 (n/a)</td><td>17.90 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (-8.66%)</td><td>0.05 (+2.43%)</td><td>0.04 (+1.33%)</td><td>0.04 (+0.89%)</td><td>0.01 (-19.79%)</td><td>213.70 (-0.88%)</td><td>180.04 (-3.17%)</td><td>182.60 (-1.30%)</td><td>149.30 (+9.54%)</td><td>27.57 (-14.10%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>185.94 (n/a)</td><td>185.00 (n/a)</td><td>136.30 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 <b>(+25.96%)</b></td><td>0.05 (+17.45%)</td><td>0.05 (+7.08%)</td><td>0.04 <b>(+39.10%)</b></td><td>0.01 (+4.67%)</td><td>245.50 <b>(-28.11%)</b></td><td>195.52 (-16.78%)</td><td>193.40 (-6.62%)</td><td>138.60 <b>(-20.62%)</b></td><td>38.39 <b>(-42.93%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>341.50 (n/a)</td><td>234.94 (n/a)</td><td>207.10 (n/a)</td><td>174.60 (n/a)</td><td>67.26 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (+4.49%)</td><td>0.04 (+10.09%)</td><td>0.04 (+3.21%)</td><td>0.04 <b>(+38.46%)</b></td><td>0.00 <b>(-33.74%)</b></td><td>218.80 <b>(-27.76%)</b></td><td>191.56 (-11.45%)</td><td>190.10 (-3.11%)</td><td>166.60 (-4.31%)</td><td>22.19 <b>(-56.04%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>302.90 (n/a)</td><td>216.32 (n/a)</td><td>196.20 (n/a)</td><td>174.10 (n/a)</td><td>50.48 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.08 <b>(+50.66%)</b></td><td>0.05 (+6.75%)</td><td>0.04 (-7.30%)</td><td>0.04 (-1.90%)</td><td>0.02 <b>(+231.71%)</b></td><td>230.40 (+1.95%)</td><td>198.80 (-0.57%)</td><td>223.40 (+7.87%)</td><td>115.00 <b>(-33.60%)</b></td><td>48.32 <b>(+121.45%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>226.00 (n/a)</td><td>199.94 (n/a)</td><td>207.10 (n/a)</td><td>173.20 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (+13.57%)</td><td>0.04 (+6.71%)</td><td>0.04 (+6.12%)</td><td>0.04 (+4.79%)</td><td>0.00 <b>(+88.01%)</b></td><td>230.80 (-4.55%)</td><td>216.40 (-5.93%)</td><td>218.10 (-5.75%)</td><td>187.60 (-11.92%)</td><td>17.17 <b>(+57.28%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>241.80 (n/a)</td><td>230.04 (n/a)</td><td>231.40 (n/a)</td><td>213.00 (n/a)</td><td>10.92 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.68 (-8.09%)</td><td>0.58 (-8.99%)</td><td>0.59 (-6.76%)</td><td>0.47 (-13.28%)</td><td>0.10 <b>(+37.74%)</b></td><td>208.80 (+15.30%)</td><td>174.62 (+11.41%)</td><td>165.30 (+7.20%)</td><td>145.00 (+8.78%)</td><td>30.46 <b>(+75.46%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.74 (n/a)</td><td>0.63 (n/a)</td><td>0.64 (n/a)</td><td>0.54 (n/a)</td><td>0.07 (n/a)</td><td>181.10 (n/a)</td><td>156.74 (n/a)</td><td>154.20 (n/a)</td><td>133.30 (n/a)</td><td>17.36 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.84 (+17.63%)</td><td>0.57 (-11.65%)</td><td>0.53 <b>(-21.58%)</b></td><td>0.44 (-14.65%)</td><td>0.15 <b>(+96.60%)</b></td><td>225.30 (+17.16%)</td><td>180.68 (+17.10%)</td><td>185.20 <b>(+27.55%)</b></td><td>117.60 (-14.97%)</td><td>39.59 <b>(+81.64%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.71 (n/a)</td><td>0.65 (n/a)</td><td>0.68 (n/a)</td><td>0.51 (n/a)</td><td>0.08 (n/a)</td><td>192.30 (n/a)</td><td>154.30 (n/a)</td><td>145.20 (n/a)</td><td>138.30 (n/a)</td><td>21.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.79 (+10.55%)</td><td>0.59 (+8.09%)</td><td>0.57 (+13.20%)</td><td>0.44 (+5.93%)</td><td>0.13 (+9.57%)</td><td>221.00 (-5.60%)</td><td>173.92 (-7.45%)</td><td>171.60 (-11.68%)</td><td>123.70 (-9.58%)</td><td>36.63 (-6.97%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.72 (n/a)</td><td>0.54 (n/a)</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.12 (n/a)</td><td>234.10 (n/a)</td><td>187.92 (n/a)</td><td>194.30 (n/a)</td><td>136.80 (n/a)</td><td>39.38 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.63 <b>(-35.31%)</b></td><td>0.50 <b>(-21.30%)</b></td><td>0.48 (-13.96%)</td><td>0.40 (-14.80%)</td><td>0.11 <b>(-45.94%)</b></td><td>244.80 (+17.41%)</td><td>202.76 <b>(+23.94%)</b></td><td>203.50 (+16.22%)</td><td>155.00 <b>(+54.54%)</b></td><td>42.21 (+6.29%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.98 (n/a)</td><td>0.64 (n/a)</td><td>0.56 (n/a)</td><td>0.47 (n/a)</td><td>0.20 (n/a)</td><td>208.50 (n/a)</td><td>163.60 (n/a)</td><td>175.10 (n/a)</td><td>100.30 (n/a)</td><td>39.71 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.47 (-7.93%)</td><td>0.41 (-2.43%)</td><td>0.41 (-6.54%)</td><td>0.37 (+9.37%)</td><td>0.04 <b>(-45.16%)</b></td><td>200.90 (-8.60%)</td><td>180.92 (+1.06%)</td><td>181.60 (+7.01%)</td><td>158.20 (+8.58%)</td><td>15.18 <b>(-46.62%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.06 (n/a)</td><td>219.80 (n/a)</td><td>179.02 (n/a)</td><td>169.70 (n/a)</td><td>145.70 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.42 (-16.64%)</td><td>0.38 (-4.99%)</td><td>0.40 (+5.38%)</td><td>0.34 (+2.73%)</td><td>0.03 <b>(-55.27%)</b></td><td>217.20 (-2.64%)</td><td>193.74 (+3.13%)</td><td>184.80 (-5.08%)</td><td>176.60 (+19.97%)</td><td>17.52 <b>(-47.61%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>223.10 (n/a)</td><td>187.86 (n/a)</td><td>194.70 (n/a)</td><td>147.20 (n/a)</td><td>33.44 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.43 <b>(-27.81%)</b></td><td>0.41 (-8.09%)</td><td>0.42 (-1.60%)</td><td>0.37 (+7.19%)</td><td>0.03 <b>(-73.49%)</b></td><td>200.80 (-6.69%)</td><td>180.22 (+5.49%)</td><td>176.60 (+1.61%)</td><td>170.50 <b>(+38.51%)</b></td><td>11.98 <b>(-64.66%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.60 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>215.20 (n/a)</td><td>170.84 (n/a)</td><td>173.80 (n/a)</td><td>123.10 (n/a)</td><td>33.90 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.58 (+11.59%)</td><td>0.41 (+8.68%)</td><td>0.33 (-17.88%)</td><td>0.32 <b>(+32.79%)</b></td><td>0.12 (+1.66%)</td><td>228.50 <b>(-24.69%)</b></td><td>191.00 (-10.13%)</td><td>222.50 <b>(+21.78%)</b></td><td>128.00 (-10.36%)</td><td>48.99 <b>(-30.60%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.52 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>303.40 (n/a)</td><td>212.52 (n/a)</td><td>182.70 (n/a)</td><td>142.80 (n/a)</td><td>70.59 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.80 (-8.81%)</td><td>0.72 (-3.18%)</td><td>0.72 (+1.07%)</td><td>0.65 (+1.29%)</td><td>0.06 <b>(-35.27%)</b></td><td>200.80 (-1.28%)</td><td>182.26 (+2.66%)</td><td>181.50 (-1.04%)</td><td>163.50 (+9.66%)</td><td>14.73 <b>(-29.25%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.88 (n/a)</td><td>0.75 (n/a)</td><td>0.71 (n/a)</td><td>0.64 (n/a)</td><td>0.09 (n/a)</td><td>203.40 (n/a)</td><td>177.54 (n/a)</td><td>183.40 (n/a)</td><td>149.10 (n/a)</td><td>20.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.85 (+0.08%)</td><td>0.72 (+1.37%)</td><td>0.79 (+0.07%)</td><td>0.53 <b>(+47.83%)</b></td><td>0.14 <b>(-29.66%)</b></td><td>246.10 <b>(-32.35%)</b></td><td>188.62 (-7.91%)</td><td>165.40 (-0.06%)</td><td>154.30 (-0.06%)</td><td>40.53 <b>(-54.66%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.85 (n/a)</td><td>0.71 (n/a)</td><td>0.79 (n/a)</td><td>0.36 (n/a)</td><td>0.20 (n/a)</td><td>363.80 (n/a)</td><td>204.82 (n/a)</td><td>165.50 (n/a)</td><td>154.40 (n/a)</td><td>89.39 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.84 (-4.14%)</td><td>0.72 (-1.39%)</td><td>0.75 (+5.41%)</td><td>0.45 (-16.87%)</td><td>0.16 <b>(+24.08%)</b></td><td>289.50 <b>(+20.27%)</b></td><td>191.54 (+3.98%)</td><td>174.90 (-5.10%)</td><td>156.30 (+4.34%)</td><td>55.60 <b>(+58.46%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.88 (n/a)</td><td>0.73 (n/a)</td><td>0.71 (n/a)</td><td>0.54 (n/a)</td><td>0.13 (n/a)</td><td>240.70 (n/a)</td><td>184.20 (n/a)</td><td>184.30 (n/a)</td><td>149.80 (n/a)</td><td>35.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.00 (+2.22%)</td><td>0.00 (+3.77%)</td><td>0.00 (+4.76%)</td><td>0.00 (+5.00%)</td><td>0.00 (-12.96%)</td><td>969.52 (-4.26%)</td><td>929.70 (-3.55%)</td><td>930.40 (-4.47%)</td><td>897.28 (-1.56%)</td><td>30.00 <b>(-20.36%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1012.65 (n/a)</td><td>963.88 (n/a)</td><td>973.94 (n/a)</td><td>911.51 (n/a)</td><td>37.67 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.01 (+0.00%)</td><td>0.01 (+1.49%)</td><td>0.01 (+0.00%)</td><td>0.01 (+6.67%)</td><td>0.00 <b>(-46.24%)</b></td><td>1022.96 (-5.73%)</td><td>1002.36 (-1.18%)</td><td>1011.75 (+0.28%)</td><td>963.76 (+0.38%)</td><td>23.20 <b>(-48.29%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1085.17 (n/a)</td><td>1014.36 (n/a)</td><td>1008.94 (n/a)</td><td>960.10 (n/a)</td><td>44.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.95 (+1.52%)</td><td>0.94 (+1.44%)</td><td>0.94 (+1.28%)</td><td>0.94 (+1.47%)</td><td>0.01 (+9.38%)</td><td>2240.51 (-1.46%)</td><td>2228.10 (-1.42%)</td><td>2232.86 (-1.27%)</td><td>2212.98 (-1.49%)</td><td>12.40 (+5.81%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.92 (n/a)</td><td>0.00 (n/a)</td><td>2273.63 (n/a)</td><td>2260.12 (n/a)</td><td>2261.67 (n/a)</td><td>2246.55 (n/a)</td><td>11.72 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>3.32 (+3.54%)</td><td>2.77 (+11.58%)</td><td>2.64 (+7.20%)</td><td>2.37 <b>(+37.67%)</b></td><td>0.40 <b>(-24.92%)</b></td><td>220.80 <b>(-27.37%)</b></td><td>192.34 (-12.52%)</td><td>198.50 (-6.72%)</td><td>157.90 (-3.43%)</td><td>26.41 <b>(-48.85%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>3.21 (n/a)</td><td>2.48 (n/a)</td><td>2.46 (n/a)</td><td>1.72 (n/a)</td><td>0.53 (n/a)</td><td>304.00 (n/a)</td><td>219.86 (n/a)</td><td>212.80 (n/a)</td><td>163.50 (n/a)</td><td>51.64 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>5.23 (-13.64%)</td><td>4.73 (-2.27%)</td><td>4.71 (-1.19%)</td><td>4.23 (+13.04%)</td><td>0.45 <b>(-47.27%)</b></td><td>248.10 (-11.52%)</td><td>223.10 (+0.52%)</td><td>222.80 (+1.23%)</td><td>200.40 (+15.77%)</td><td>21.24 <b>(-46.30%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>6.06 (n/a)</td><td>4.84 (n/a)</td><td>4.76 (n/a)</td><td>3.74 (n/a)</td><td>0.85 (n/a)</td><td>280.40 (n/a)</td><td>221.94 (n/a)</td><td>220.10 (n/a)</td><td>173.10 (n/a)</td><td>39.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>2.79 <b>(-22.31%)</b></td><td>2.63 (-11.49%)</td><td>2.67 (-5.00%)</td><td>2.32 (+1.47%)</td><td>0.18 <b>(-65.87%)</b></td><td>226.00 (-1.44%)</td><td>200.22 (+10.53%)</td><td>196.10 (+5.26%)</td><td>187.80 <b>(+28.72%)</b></td><td>14.84 <b>(-55.29%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>3.59 (n/a)</td><td>2.97 (n/a)</td><td>2.81 (n/a)</td><td>2.29 (n/a)</td><td>0.53 (n/a)</td><td>229.30 (n/a)</td><td>181.14 (n/a)</td><td>186.30 (n/a)</td><td>145.90 (n/a)</td><td>33.19 (n/a)</td>
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
