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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.09 (+0.45%)</td><td>0.07 (+3.66%)</td><td>0.07 (+8.30%)</td><td>0.06 (-0.96%)</td><td>0.01 (+1.63%)</td><td>200.40 (+0.96%)</td><td>173.32 (-3.44%)</td><td>175.80 (-7.67%)</td><td>136.70 (-0.51%)</td><td>25.79 (+4.55%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>179.50 (n/a)</td><td>190.40 (n/a)</td><td>137.40 (n/a)</td><td>24.66 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.08 (+15.69%)</td><td>0.07 <b>(+23.58%)</b></td><td>0.07 <b>(+29.78%)</b></td><td>0.06 <b>(+28.27%)</b></td><td>0.01 (+8.28%)</td><td>211.30 <b>(-22.03%)</b></td><td>174.04 (-19.43%)</td><td>165.00 <b>(-22.93%)</b></td><td>147.70 (-13.58%)</td><td>26.56 <b>(-27.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>271.00 (n/a)</td><td>216.02 (n/a)</td><td>214.10 (n/a)</td><td>170.90 (n/a)</td><td>36.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.09 <b>(+20.28%)</b></td><td>0.06 (+7.50%)</td><td>0.07 (+4.70%)</td><td>0.03 <b>(-33.39%)</b></td><td>0.02 <b>(+86.26%)</b></td><td>414.60 <b>(+50.11%)</b></td><td>221.10 (+3.32%)</td><td>185.80 (-4.47%)</td><td>139.00 (-16.87%)</td><td>109.94 <b>(+153.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>276.20 (n/a)</td><td>214.00 (n/a)</td><td>194.50 (n/a)</td><td>167.20 (n/a)</td><td>43.44 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.08 <b>(+21.17%)</b></td><td>0.06 (+15.16%)</td><td>0.06 (+11.72%)</td><td>0.05 <b>(+27.00%)</b></td><td>0.01 (+11.64%)</td><td>239.00 <b>(-21.25%)</b></td><td>197.92 (-13.69%)</td><td>198.00 (-10.49%)</td><td>153.20 (-17.46%)</td><td>31.44 <b>(-30.26%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>303.50 (n/a)</td><td>229.30 (n/a)</td><td>221.20 (n/a)</td><td>185.60 (n/a)</td><td>45.08 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 <b>(+20.06%)</b></td><td>0.03 (+1.12%)</td><td>0.03 (-10.01%)</td><td>0.03 (+2.45%)</td><td>0.01 <b>(+68.38%)</b></td><td>191.30 (-2.35%)</td><td>163.82 (+0.56%)</td><td>173.50 (+11.15%)</td><td>115.50 (-16.73%)</td><td>28.82 <b>(+30.33%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>195.90 (n/a)</td><td>162.90 (n/a)</td><td>156.10 (n/a)</td><td>138.70 (n/a)</td><td>22.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.03 (-8.05%)</td><td>0.03 (-8.72%)</td><td>0.03 (-6.45%)</td><td>0.02 <b>(-20.31%)</b></td><td>0.00 (+14.87%)</td><td>241.80 <b>(+25.48%)</b></td><td>188.58 (+10.68%)</td><td>179.20 (+6.86%)</td><td>152.30 (+8.79%)</td><td>33.32 <b>(+59.61%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.70 (n/a)</td><td>170.38 (n/a)</td><td>167.70 (n/a)</td><td>140.00 (n/a)</td><td>20.88 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.03 <b>(-20.64%)</b></td><td>0.03 (-14.02%)</td><td>0.03 (-18.18%)</td><td>0.02 <b>(+20.32%)</b></td><td>0.00 <b>(-62.36%)</b></td><td>211.00 (-16.90%)</td><td>189.76 (+11.34%)</td><td>188.80 <b>(+22.20%)</b></td><td>163.10 <b>(+26.04%)</b></td><td>17.66 <b>(-63.34%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>253.90 (n/a)</td><td>170.44 (n/a)</td><td>154.50 (n/a)</td><td>129.40 (n/a)</td><td>48.17 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.04 (-11.10%)</td><td>0.03 (+4.82%)</td><td>0.03 (-2.87%)</td><td>0.03 <b>(+78.40%)</b></td><td>0.00 <b>(-57.59%)</b></td><td>195.20 <b>(-43.94%)</b></td><td>173.00 (-13.26%)</td><td>178.40 (+2.94%)</td><td>146.00 (+12.48%)</td><td>20.88 <b>(-75.51%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>348.20 (n/a)</td><td>199.44 (n/a)</td><td>173.30 (n/a)</td><td>129.80 (n/a)</td><td>85.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.03 (-5.28%)</td><td>0.03 (-0.27%)</td><td>0.03 (-15.77%)</td><td>0.03 (+18.54%)</td><td>0.00 <b>(-35.70%)</b></td><td>207.10 (-15.61%)</td><td>183.90 (-2.28%)</td><td>194.80 (+18.71%)</td><td>152.50 (+5.61%)</td><td>24.47 <b>(-43.72%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>245.40 (n/a)</td><td>188.20 (n/a)</td><td>164.10 (n/a)</td><td>144.40 (n/a)</td><td>43.48 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.04 (-1.98%)</td><td>0.03 (+4.00%)</td><td>0.02 (+13.61%)</td><td>0.02 <b>(+40.60%)</b></td><td>0.01 <b>(-32.99%)</b></td><td>222.90 <b>(-28.88%)</b></td><td>201.34 (-9.67%)</td><td>214.20 (-11.96%)</td><td>138.30 (+1.99%)</td><td>35.64 <b>(-51.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>313.40 (n/a)</td><td>222.90 (n/a)</td><td>243.30 (n/a)</td><td>135.60 (n/a)</td><td>72.89 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.03 <b>(-25.36%)</b></td><td>0.03 (-8.25%)</td><td>0.03 (+5.56%)</td><td>0.02 (-9.55%)</td><td>0.01 <b>(-33.33%)</b></td><td>331.10 (+10.55%)</td><td>220.64 (+6.07%)</td><td>185.40 (-5.26%)</td><td>166.70 <b>(+34.00%)</b></td><td>67.38 (+0.34%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>299.50 (n/a)</td><td>208.02 (n/a)</td><td>195.70 (n/a)</td><td>124.40 (n/a)</td><td>67.15 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.02 (-7.35%)</td><td>0.02 (-4.95%)</td><td>0.02 (-4.65%)</td><td>0.02 (+6.27%)</td><td>0.00 (-18.95%)</td><td>312.00 (-5.91%)</td><td>254.72 (+4.15%)</td><td>234.00 (+4.89%)</td><td>222.30 (+7.97%)</td><td>39.89 <b>(-21.08%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>331.60 (n/a)</td><td>244.56 (n/a)</td><td>223.10 (n/a)</td><td>205.90 (n/a)</td><td>50.55 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>170.10 (n/a)</td><td>168.00 (n/a)</td><td>151.20 (n/a)</td><td>19.82 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.80 (n/a)</td><td>194.76 (n/a)</td><td>182.50 (n/a)</td><td>167.30 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>194.30 (n/a)</td><td>178.76 (n/a)</td><td>187.90 (n/a)</td><td>148.00 (n/a)</td><td>18.57 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.50 (n/a)</td><td>190.54 (n/a)</td><td>194.10 (n/a)</td><td>140.50 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>163.40 (n/a)</td><td>139.86 (n/a)</td><td>136.50 (n/a)</td><td>108.70 (n/a)</td><td>21.33 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>218.70 (n/a)</td><td>165.00 (n/a)</td><td>153.30 (n/a)</td><td>130.60 (n/a)</td><td>36.89 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.80 (n/a)</td><td>165.94 (n/a)</td><td>149.00 (n/a)</td><td>135.70 (n/a)</td><td>39.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>194.00 (n/a)</td><td>176.82 (n/a)</td><td>182.70 (n/a)</td><td>139.40 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.50 (n/a)</td><td>153.74 (n/a)</td><td>152.80 (n/a)</td><td>126.90 (n/a)</td><td>27.23 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>224.40 (n/a)</td><td>183.88 (n/a)</td><td>208.80 (n/a)</td><td>99.40 (n/a)</td><td>52.38 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.30 (n/a)</td><td>155.50 (n/a)</td><td>160.30 (n/a)</td><td>126.00 (n/a)</td><td>17.18 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.10 (n/a)</td><td>163.56 (n/a)</td><td>168.30 (n/a)</td><td>143.00 (n/a)</td><td>17.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>174.10 (n/a)</td><td>161.98 (n/a)</td><td>171.90 (n/a)</td><td>145.40 (n/a)</td><td>14.71 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>177.36 (n/a)</td><td>175.00 (n/a)</td><td>152.50 (n/a)</td><td>21.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>171.66 (n/a)</td><td>169.40 (n/a)</td><td>146.50 (n/a)</td><td>24.12 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>187.40 (n/a)</td><td>191.90 (n/a)</td><td>162.40 (n/a)</td><td>24.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>4.84 (+14.13%)</td><td>4.18 (+4.61%)</td><td>4.20 (+2.69%)</td><td>3.55 (+1.57%)</td><td>0.51 <b>(+71.19%)</b></td><td>2651.70 (-1.54%)</td><td>2274.06 (-3.73%)</td><td>2241.30 (-2.62%)</td><td>1944.10 (-12.38%)</td><td>277.51 <b>(+45.91%)</b></td><td>1902.90 (+14.13%)</td><td>1646.11 (+4.61%)</td><td>1650.56 (+2.69%)</td><td>1395.12 (+1.57%)</td><td>198.78 <b>(+71.19%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>4.24 (n/a)</td><td>4.00 (n/a)</td><td>4.09 (n/a)</td><td>3.49 (n/a)</td><td>0.30 (n/a)</td><td>2693.20 (n/a)</td><td>2362.24 (n/a)</td><td>2301.50 (n/a)</td><td>2218.80 (n/a)</td><td>190.20 (n/a)</td><td>1667.30 (n/a)</td><td>1573.52 (n/a)</td><td>1607.38 (n/a)</td><td>1373.59 (n/a)</td><td>116.12 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>1.13 (+3.50%)</td><td>0.87 (-8.53%)</td><td>0.82 (-16.64%)</td><td>0.64 <b>(-22.20%)</b></td><td>0.19 <b>(+67.46%)</b></td><td>343.60 <b>(+28.54%)</b></td><td>263.44 (+12.25%)</td><td>268.50 (+19.97%)</td><td>195.70 (-3.41%)</td><td>57.18 <b>(+102.63%)</b></td><td>48.22 (+3.50%)</td><td>37.21 (-8.53%)</td><td>35.15 (-16.64%)</td><td>27.47 <b>(-22.20%)</b></td><td>8.09 <b>(+67.46%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>1.09 (n/a)</td><td>0.95 (n/a)</td><td>0.99 (n/a)</td><td>0.83 (n/a)</td><td>0.11 (n/a)</td><td>267.30 (n/a)</td><td>234.68 (n/a)</td><td>223.80 (n/a)</td><td>202.60 (n/a)</td><td>28.22 (n/a)</td><td>46.59 (n/a)</td><td>40.68 (n/a)</td><td>42.17 (n/a)</td><td>35.31 (n/a)</td><td>4.83 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>1.16 (+4.13%)</td><td>0.99 (+5.75%)</td><td>1.08 (+4.78%)</td><td>0.72 (+19.97%)</td><td>0.20 (-10.49%)</td><td>308.20 (-16.64%)</td><td>232.28 (-7.29%)</td><td>205.40 (-4.60%)</td><td>190.60 (-3.98%)</td><td>52.17 <b>(-28.45%)</b></td><td>49.51 (+4.13%)</td><td>42.16 (+5.75%)</td><td>45.94 (+4.78%)</td><td>30.62 (+19.97%)</td><td>8.54 (-10.49%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>1.11 (n/a)</td><td>0.93 (n/a)</td><td>1.03 (n/a)</td><td>0.60 (n/a)</td><td>0.22 (n/a)</td><td>369.70 (n/a)</td><td>250.54 (n/a)</td><td>215.30 (n/a)</td><td>198.50 (n/a)</td><td>72.91 (n/a)</td><td>47.55 (n/a)</td><td>39.86 (n/a)</td><td>43.84 (n/a)</td><td>25.53 (n/a)</td><td>9.55 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.52 (+0.50%)</td><td>0.52 (+0.21%)</td><td>0.52 (+0.07%)</td><td>0.52 (+0.34%)</td><td>0.00 <b>(+48.07%)</b></td><td>48632.50 (-0.34%)</td><td>48555.66 (-0.21%)</td><td>48600.50 (-0.07%)</td><td>48339.50 (-0.50%)</td><td>121.57 <b>(+46.74%)</b></td><td>355.40 (+0.50%)</td><td>353.82 (+0.21%)</td><td>353.49 (+0.07%)</td><td>353.26 (+0.34%)</td><td>0.89 <b>(+48.07%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48798.10 (n/a)</td><td>48657.18 (n/a)</td><td>48634.50 (n/a)</td><td>48581.00 (n/a)</td><td>82.85 (n/a)</td><td>353.63 (n/a)</td><td>353.08 (n/a)</td><td>353.24 (n/a)</td><td>352.06 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.89 (+0.53%)</td><td>0.89 (+0.73%)</td><td>0.89 (+1.11%)</td><td>0.88 (+0.58%)</td><td>0.00 (-13.40%)</td><td>28555.00 (-0.58%)</td><td>28386.32 (-0.73%)</td><td>28384.30 (-1.10%)</td><td>28213.40 (-0.52%)</td><td>143.51 (-14.42%)</td><td>608.93 (+0.53%)</td><td>605.23 (+0.73%)</td><td>605.26 (+1.11%)</td><td>601.64 (+0.58%)</td><td>3.06 (-13.40%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28720.40 (n/a)</td><td>28594.26 (n/a)</td><td>28699.50 (n/a)</td><td>28361.50 (n/a)</td><td>167.70 (n/a)</td><td>605.75 (n/a)</td><td>600.83 (n/a)</td><td>598.61 (n/a)</td><td>598.18 (n/a)</td><td>3.53 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>3.31 (-0.64%)</td><td>3.24 (+1.44%)</td><td>3.19 (+0.07%)</td><td>3.19 (+3.22%)</td><td>0.06 <b>(-28.55%)</b></td><td>7895.30 (-3.12%)</td><td>7779.08 (-1.45%)</td><td>7882.70 (-0.07%)</td><td>7607.90 (+0.64%)</td><td>150.60 <b>(-30.05%)</b></td><td>2258.15 (-0.64%)</td><td>2209.14 (+1.44%)</td><td>2179.44 (+0.07%)</td><td>2175.97 (+3.22%)</td><td>43.07 <b>(-28.55%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>3.33 (n/a)</td><td>3.19 (n/a)</td><td>3.19 (n/a)</td><td>3.09 (n/a)</td><td>0.09 (n/a)</td><td>8149.20 (n/a)</td><td>7893.34 (n/a)</td><td>7887.90 (n/a)</td><td>7559.20 (n/a)</td><td>215.29 (n/a)</td><td>2272.72 (n/a)</td><td>2177.81 (n/a)</td><td>2177.99 (n/a)</td><td>2108.16 (n/a)</td><td>60.28 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>3.66 (-10.24%)</td><td>3.19 (-14.00%)</td><td>2.98 (-18.61%)</td><td>2.84 (-16.73%)</td><td>0.38 <b>(+50.92%)</b></td><td>2833.70 <b>(+20.10%)</b></td><td>2553.76 (+17.12%)</td><td>2703.20 <b>(+22.87%)</b></td><td>2202.30 (+11.41%)</td><td>290.93 <b>(+101.55%)</b></td><td>959.87 (-10.24%)</td><td>836.80 (-14.00%)</td><td>782.01 (-18.61%)</td><td>746.01 (-16.73%)</td><td>99.12 <b>(+50.92%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>4.08 (n/a)</td><td>3.71 (n/a)</td><td>3.66 (n/a)</td><td>3.42 (n/a)</td><td>0.25 (n/a)</td><td>2359.50 (n/a)</td><td>2180.40 (n/a)</td><td>2200.10 (n/a)</td><td>1976.70 (n/a)</td><td>144.34 (n/a)</td><td>1069.40 (n/a)</td><td>972.99 (n/a)</td><td>960.82 (n/a)</td><td>895.94 (n/a)</td><td>65.68 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.57 <b>(+68.89%)</b></td><td>0.43 <b>(+37.09%)</b></td><td>0.34 (+3.91%)</td><td>0.34 <b>(+24.54%)</b></td><td>0.12 <b>(+286.85%)</b></td><td>3707.80 (-19.71%)</td><td>3098.46 <b>(-23.13%)</b></td><td>3665.30 (-3.77%)</td><td>2178.20 <b>(-40.79%)</b></td><td>801.73 <b>(+87.49%)</b></td><td>30.81 <b>(+68.89%)</b></td><td>23.02 <b>(+37.09%)</b></td><td>18.31 (+3.91%)</td><td>18.10 <b>(+24.54%)</b></td><td>6.59 <b>(+286.85%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>4617.80 (n/a)</td><td>4030.62 (n/a)</td><td>3808.70 (n/a)</td><td>3678.60 (n/a)</td><td>427.60 (n/a)</td><td>18.24 (n/a)</td><td>16.79 (n/a)</td><td>17.62 (n/a)</td><td>14.53 (n/a)</td><td>1.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>6.13 (+2.29%)</td><td>4.28 (-1.04%)</td><td>3.58 (-8.77%)</td><td>3.51 (+3.86%)</td><td>1.13 (+6.24%)</td><td>1896.00 (-3.72%)</td><td>1628.84 (+1.44%)</td><td>1858.30 (+9.61%)</td><td>1085.70 (-2.24%)</td><td>356.27 (+2.41%)</td><td>1892.92 (+2.29%)</td><td>1322.29 (-1.04%)</td><td>1105.96 (-8.77%)</td><td>1083.99 (+3.86%)</td><td>349.01 (+6.24%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>5.99 (n/a)</td><td>4.32 (n/a)</td><td>3.92 (n/a)</td><td>3.38 (n/a)</td><td>1.06 (n/a)</td><td>1969.20 (n/a)</td><td>1605.74 (n/a)</td><td>1695.40 (n/a)</td><td>1110.60 (n/a)</td><td>347.88 (n/a)</td><td>1850.62 (n/a)</td><td>1336.18 (n/a)</td><td>1212.23 (n/a)</td><td>1043.68 (n/a)</td><td>328.50 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.22 <b>(-23.35%)</b></td><td>0.18 (-11.37%)</td><td>0.17 (-8.62%)</td><td>0.15 (+1.66%)</td><td>0.03 <b>(-51.49%)</b></td><td>0.21 <b>(-23.35%)</b></td><td>0.18 (-11.37%)</td><td>0.17 (-8.62%)</td><td>0.15 (+1.66%)</td><td>0.03 <b>(-51.49%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>13.04 (-0.90%)</td><td>12.82 (+8.20%)</td><td>12.97 (+1.82%)</td><td>12.36 <b>(+21.78%)</b></td><td>0.28 <b>(-80.28%)</b></td><td>13.03 (-0.90%)</td><td>12.82 (+8.20%)</td><td>12.96 (+1.82%)</td><td>12.35 <b>(+21.78%)</b></td><td>0.28 <b>(-80.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>13.16 (n/a)</td><td>11.85 (n/a)</td><td>12.73 (n/a)</td><td>10.15 (n/a)</td><td>1.42 (n/a)</td><td>13.15 (n/a)</td><td>11.85 (n/a)</td><td>12.73 (n/a)</td><td>10.14 (n/a)</td><td>1.42 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>24.34 (-5.32%)</td><td>23.81 (+5.83%)</td><td>23.88 (-0.86%)</td><td>23.37 <b>(+73.21%)</b></td><td>0.40 <b>(-92.15%)</b></td><td>24.33 (-5.32%)</td><td>23.79 (+5.83%)</td><td>23.87 (-0.86%)</td><td>23.35 <b>(+73.21%)</b></td><td>0.40 <b>(-92.15%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>25.71 (n/a)</td><td>22.49 (n/a)</td><td>24.09 (n/a)</td><td>13.49 (n/a)</td><td>5.08 (n/a)</td><td>25.70 (n/a)</td><td>22.48 (n/a)</td><td>24.08 (n/a)</td><td>13.48 (n/a)</td><td>5.08 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>40.35 (-2.56%)</td><td>39.71 (-1.59%)</td><td>39.49 (-3.00%)</td><td>39.42 (+1.99%)</td><td>0.40 <b>(-61.50%)</b></td><td>40.33 (-2.56%)</td><td>39.69 (-1.59%)</td><td>39.46 (-3.00%)</td><td>39.40 (+1.99%)</td><td>0.40 <b>(-61.50%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>41.41 (n/a)</td><td>40.36 (n/a)</td><td>40.71 (n/a)</td><td>38.65 (n/a)</td><td>1.04 (n/a)</td><td>41.39 (n/a)</td><td>40.33 (n/a)</td><td>40.68 (n/a)</td><td>38.63 (n/a)</td><td>1.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>44.38 (-1.88%)</td><td>42.26 (-1.05%)</td><td>44.09 (+3.48%)</td><td>37.05 (-7.70%)</td><td>3.16 <b>(+49.06%)</b></td><td>44.35 (-1.88%)</td><td>42.23 (-1.05%)</td><td>44.06 (+3.48%)</td><td>37.02 (-7.70%)</td><td>3.16 <b>(+49.06%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>45.23 (n/a)</td><td>42.71 (n/a)</td><td>42.61 (n/a)</td><td>40.14 (n/a)</td><td>2.12 (n/a)</td><td>45.20 (n/a)</td><td>42.68 (n/a)</td><td>42.58 (n/a)</td><td>40.11 (n/a)</td><td>2.12 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>12.94 (-2.63%)</td><td>12.12 (-1.51%)</td><td>12.21 (-3.33%)</td><td>10.80 (-0.97%)</td><td>0.82 (-10.99%)</td><td>12.94 (-2.63%)</td><td>12.12 (-1.51%)</td><td>12.21 (-3.33%)</td><td>10.79 (-0.97%)</td><td>0.82 (-10.99%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>13.29 (n/a)</td><td>12.31 (n/a)</td><td>12.64 (n/a)</td><td>10.91 (n/a)</td><td>0.92 (n/a)</td><td>13.28 (n/a)</td><td>12.30 (n/a)</td><td>12.63 (n/a)</td><td>10.90 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>24.54 (-1.08%)</td><td>23.80 (-0.57%)</td><td>23.78 (-0.68%)</td><td>22.94 (+2.23%)</td><td>0.57 <b>(-38.70%)</b></td><td>24.52 (-1.08%)</td><td>23.78 (-0.57%)</td><td>23.77 (-0.68%)</td><td>22.93 (+2.23%)</td><td>0.57 <b>(-38.70%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>24.81 (n/a)</td><td>23.93 (n/a)</td><td>23.95 (n/a)</td><td>22.44 (n/a)</td><td>0.93 (n/a)</td><td>24.79 (n/a)</td><td>23.92 (n/a)</td><td>23.93 (n/a)</td><td>22.43 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>41.47 (+4.95%)</td><td>38.57 (+1.85%)</td><td>39.81 (+3.91%)</td><td>32.23 (-9.07%)</td><td>3.64 <b>(+112.74%)</b></td><td>41.44 (+4.95%)</td><td>38.55 (+1.85%)</td><td>39.78 (+3.91%)</td><td>32.21 (-9.07%)</td><td>3.63 <b>(+112.74%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>39.51 (n/a)</td><td>37.87 (n/a)</td><td>38.31 (n/a)</td><td>35.45 (n/a)</td><td>1.71 (n/a)</td><td>39.49 (n/a)</td><td>37.85 (n/a)</td><td>38.29 (n/a)</td><td>35.43 (n/a)</td><td>1.71 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>44.72 (+0.02%)</td><td>42.27 (-2.52%)</td><td>43.24 (-0.31%)</td><td>39.85 (-4.31%)</td><td>2.20 <b>(+92.85%)</b></td><td>44.70 (+0.02%)</td><td>42.24 (-2.52%)</td><td>43.21 (-0.31%)</td><td>39.83 (-4.31%)</td><td>2.20 <b>(+92.85%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>44.72 (n/a)</td><td>43.36 (n/a)</td><td>43.37 (n/a)</td><td>41.65 (n/a)</td><td>1.14 (n/a)</td><td>44.69 (n/a)</td><td>43.34 (n/a)</td><td>43.35 (n/a)</td><td>41.62 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>9.61 (-0.15%)</td><td>8.60 (-4.23%)</td><td>8.40 (-9.14%)</td><td>7.77 (-4.66%)</td><td>0.70 (+13.96%)</td><td>9.59 (-0.15%)</td><td>8.59 (-4.23%)</td><td>8.39 (-9.14%)</td><td>7.76 (-4.66%)</td><td>0.69 (+13.96%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>9.62 (n/a)</td><td>8.98 (n/a)</td><td>9.25 (n/a)</td><td>8.15 (n/a)</td><td>0.61 (n/a)</td><td>9.60 (n/a)</td><td>8.96 (n/a)</td><td>9.23 (n/a)</td><td>8.14 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.94 (+9.92%)</td><td>0.77 (-3.96%)</td><td>0.73 (-8.12%)</td><td>0.69 (-11.37%)</td><td>0.10 <b>(+196.85%)</b></td><td>0.93 (+9.92%)</td><td>0.76 (-3.96%)</td><td>0.72 (-8.12%)</td><td>0.68 (-11.37%)</td><td>0.10 <b>(+196.85%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.86 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.03 (n/a)</td><td>0.84 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>1.28 (+9.11%)</td><td>1.10 (+6.97%)</td><td>1.08 (+1.42%)</td><td>0.89 (+2.50%)</td><td>0.15 (+18.26%)</td><td>1.27 (+9.11%)</td><td>1.09 (+6.97%)</td><td>1.07 (+1.42%)</td><td>0.88 (+2.50%)</td><td>0.15 (+18.26%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>1.18 (n/a)</td><td>1.03 (n/a)</td><td>1.07 (n/a)</td><td>0.87 (n/a)</td><td>0.13 (n/a)</td><td>1.16 (n/a)</td><td>1.02 (n/a)</td><td>1.05 (n/a)</td><td>0.86 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>15.57 (-6.90%)</td><td>14.90 (-7.61%)</td><td>14.66 (-10.06%)</td><td>14.35 (-6.65%)</td><td>0.56 (-2.28%)</td><td>15.39 (-6.90%)</td><td>14.72 (-7.61%)</td><td>14.49 (-10.06%)</td><td>14.19 (-6.65%)</td><td>0.55 (-2.28%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>16.73 (n/a)</td><td>16.12 (n/a)</td><td>16.30 (n/a)</td><td>15.37 (n/a)</td><td>0.57 (n/a)</td><td>16.53 (n/a)</td><td>15.94 (n/a)</td><td>16.11 (n/a)</td><td>15.20 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>12.07 (-2.18%)</td><td>11.76 (+7.17%)</td><td>11.65 (-1.04%)</td><td>11.53 <b>(+51.10%)</b></td><td>0.23 <b>(-87.95%)</b></td><td>11.86 (-2.18%)</td><td>11.56 (+7.17%)</td><td>11.44 (-1.04%)</td><td>11.33 <b>(+51.10%)</b></td><td>0.23 <b>(-87.95%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>12.34 (n/a)</td><td>10.98 (n/a)</td><td>11.77 (n/a)</td><td>7.63 (n/a)</td><td>1.92 (n/a)</td><td>12.12 (n/a)</td><td>10.78 (n/a)</td><td>11.56 (n/a)</td><td>7.50 (n/a)</td><td>1.88 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>8.32 <b>(-21.51%)</b></td><td>7.43 (-7.10%)</td><td>7.40 (+1.78%)</td><td>6.53 (+4.23%)</td><td>0.82 <b>(-51.94%)</b></td><td>8.18 <b>(-21.51%)</b></td><td>7.30 (-7.10%)</td><td>7.27 (+1.78%)</td><td>6.42 (+4.23%)</td><td>0.80 <b>(-51.94%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>10.60 (n/a)</td><td>8.00 (n/a)</td><td>7.27 (n/a)</td><td>6.27 (n/a)</td><td>1.70 (n/a)</td><td>10.42 (n/a)</td><td>7.86 (n/a)</td><td>7.15 (n/a)</td><td>6.16 (n/a)</td><td>1.67 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>7.07 (+6.45%)</td><td>5.35 (-11.46%)</td><td>4.94 (-19.54%)</td><td>4.05 <b>(-27.33%)</b></td><td>1.15 <b>(+160.08%)</b></td><td>6.96 (+6.45%)</td><td>5.26 (-11.46%)</td><td>4.86 (-19.54%)</td><td>3.99 <b>(-27.33%)</b></td><td>1.13 <b>(+160.08%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>6.64 (n/a)</td><td>6.04 (n/a)</td><td>6.14 (n/a)</td><td>5.58 (n/a)</td><td>0.44 (n/a)</td><td>6.54 (n/a)</td><td>5.95 (n/a)</td><td>6.04 (n/a)</td><td>5.49 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.10 (n/a)</td><td>190.76 (n/a)</td><td>196.10 (n/a)</td><td>135.10 (n/a)</td><td>33.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>178.02 (n/a)</td><td>159.10 (n/a)</td><td>125.60 (n/a)</td><td>45.06 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>155.78 (n/a)</td><td>141.50 (n/a)</td><td>129.70 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>168.52 (n/a)</td><td>163.90 (n/a)</td><td>136.10 (n/a)</td><td>29.75 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>179.60 (n/a)</td><td>169.42 (n/a)</td><td>173.30 (n/a)</td><td>148.90 (n/a)</td><td>12.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.90 (n/a)</td><td>193.38 (n/a)</td><td>189.50 (n/a)</td><td>163.90 (n/a)</td><td>24.83 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.10 (n/a)</td><td>188.28 (n/a)</td><td>198.50 (n/a)</td><td>152.30 (n/a)</td><td>28.76 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>264.50 (n/a)</td><td>225.06 (n/a)</td><td>240.80 (n/a)</td><td>186.50 (n/a)</td><td>34.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 <b>(+22.56%)</b></td><td>0.06 <b>(+24.17%)</b></td><td>0.06 <b>(+34.37%)</b></td><td>0.05 (+13.91%)</td><td>0.01 <b>(+51.39%)</b></td><td>173.60 (-12.23%)</td><td>139.24 (-18.89%)</td><td>128.60 <b>(-25.58%)</b></td><td>118.90 (-18.39%)</td><td>21.93 (+9.74%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.80 (n/a)</td><td>171.66 (n/a)</td><td>172.80 (n/a)</td><td>145.70 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (+14.80%)</td><td>0.05 (+0.78%)</td><td>0.05 (+12.31%)</td><td>0.03 <b>(-24.85%)</b></td><td>0.01 <b>(+121.45%)</b></td><td>259.40 <b>(+33.09%)</b></td><td>181.60 (+3.91%)</td><td>155.10 (-10.96%)</td><td>133.50 (-12.86%)</td><td>50.85 <b>(+158.65%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>174.76 (n/a)</td><td>174.20 (n/a)</td><td>153.20 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (+1.92%)</td><td>0.05 (+12.77%)</td><td>0.05 (+13.52%)</td><td>0.04 (+0.59%)</td><td>0.01 (-4.79%)</td><td>210.40 (-0.57%)</td><td>159.04 (-11.57%)</td><td>151.90 (-11.89%)</td><td>130.90 (-1.87%)</td><td>30.47 (-5.49%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>179.84 (n/a)</td><td>172.40 (n/a)</td><td>133.40 (n/a)</td><td>32.24 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (-5.81%)</td><td>0.05 (+2.38%)</td><td>0.05 (+9.27%)</td><td>0.04 (-7.37%)</td><td>0.01 (-5.50%)</td><td>230.20 (+7.97%)</td><td>172.82 (-2.23%)</td><td>154.30 (-8.48%)</td><td>133.90 (+6.10%)</td><td>38.43 (+8.79%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.20 (n/a)</td><td>176.76 (n/a)</td><td>168.60 (n/a)</td><td>126.20 (n/a)</td><td>35.32 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 <b>(-20.96%)</b></td><td>0.05 (-7.43%)</td><td>0.05 (+0.55%)</td><td>0.04 (+0.44%)</td><td>0.01 <b>(-34.17%)</b></td><td>218.70 (-0.46%)</td><td>165.32 (+4.49%)</td><td>159.60 (-0.56%)</td><td>129.40 <b>(+26.61%)</b></td><td>38.16 (-18.67%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>219.70 (n/a)</td><td>158.22 (n/a)</td><td>160.50 (n/a)</td><td>102.20 (n/a)</td><td>46.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (+0.83%)</td><td>0.06 <b>(+29.61%)</b></td><td>0.06 <b>(+45.52%)</b></td><td>0.05 <b>(+44.82%)</b></td><td>0.00 <b>(-59.88%)</b></td><td>153.30 <b>(-30.95%)</b></td><td>144.14 <b>(-25.80%)</b></td><td>147.40 <b>(-31.28%)</b></td><td>126.20 (-0.86%)</td><td>11.02 <b>(-72.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.00 (n/a)</td><td>194.26 (n/a)</td><td>214.50 (n/a)</td><td>127.30 (n/a)</td><td>39.75 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 <b>(+24.47%)</b></td><td>0.05 (+10.78%)</td><td>0.05 (+5.82%)</td><td>0.05 (+5.19%)</td><td>0.01 <b>(+105.57%)</b></td><td>174.10 (-4.92%)</td><td>155.76 (-9.15%)</td><td>156.10 (-5.51%)</td><td>130.30 (-19.67%)</td><td>16.21 <b>(+53.47%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>183.10 (n/a)</td><td>171.44 (n/a)</td><td>165.20 (n/a)</td><td>162.20 (n/a)</td><td>10.56 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (-5.77%)</td><td>0.05 (+3.38%)</td><td>0.05 <b>(+23.71%)</b></td><td>0.03 (+0.08%)</td><td>0.01 <b>(-29.26%)</b></td><td>235.60 (-0.08%)</td><td>177.32 (-5.66%)</td><td>165.50 (-19.19%)</td><td>140.20 (+6.13%)</td><td>36.45 <b>(-22.62%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.80 (n/a)</td><td>187.96 (n/a)</td><td>204.80 (n/a)</td><td>132.10 (n/a)</td><td>47.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 <b>(+31.53%)</b></td><td>0.05 (+18.30%)</td><td>0.05 <b>(+20.20%)</b></td><td>0.04 (-0.01%)</td><td>0.01 <b>(+207.46%)</b></td><td>207.40 (+0.05%)</td><td>168.92 (-14.30%)</td><td>165.90 (-16.80%)</td><td>140.00 <b>(-24.00%)</b></td><td>24.42 <b>(+137.26%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>207.30 (n/a)</td><td>197.10 (n/a)</td><td>199.40 (n/a)</td><td>184.20 (n/a)</td><td>10.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 <b>(-20.42%)</b></td><td>0.04 (+8.16%)</td><td>0.05 <b>(+20.42%)</b></td><td>0.04 <b>(+42.33%)</b></td><td>0.00 <b>(-62.37%)</b></td><td>233.10 <b>(-29.75%)</b></td><td>191.32 (-13.87%)</td><td>179.80 (-16.95%)</td><td>174.90 <b>(+25.65%)</b></td><td>24.11 <b>(-66.47%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>331.80 (n/a)</td><td>222.14 (n/a)</td><td>216.50 (n/a)</td><td>139.20 (n/a)</td><td>71.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 (+17.23%)</td><td>0.05 (+13.73%)</td><td>0.05 (+3.65%)</td><td>0.04 (+4.05%)</td><td>0.01 <b>(+62.88%)</b></td><td>229.90 (-3.89%)</td><td>169.42 (-9.34%)</td><td>172.30 (-3.53%)</td><td>122.40 (-14.64%)</td><td>45.86 <b>(+27.39%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.20 (n/a)</td><td>186.88 (n/a)</td><td>178.60 (n/a)</td><td>143.40 (n/a)</td><td>36.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 <b>(+23.45%)</b></td><td>0.04 (+16.27%)</td><td>0.04 (+19.91%)</td><td>0.04 (+3.89%)</td><td>0.01 <b>(+113.41%)</b></td><td>229.00 (-3.74%)</td><td>189.56 (-13.23%)</td><td>184.80 (-16.61%)</td><td>163.60 (-19.01%)</td><td>24.39 <b>(+70.51%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.90 (n/a)</td><td>218.46 (n/a)</td><td>221.60 (n/a)</td><td>202.00 (n/a)</td><td>14.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (-18.78%)</td><td>0.05 (+0.52%)</td><td>0.05 (+13.30%)</td><td>0.05 (+19.67%)</td><td>0.01 <b>(-54.52%)</b></td><td>174.10 (-16.42%)</td><td>154.60 (-4.72%)</td><td>150.30 (-11.74%)</td><td>126.80 <b>(+23.11%)</b></td><td>19.26 <b>(-50.64%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>208.30 (n/a)</td><td>162.26 (n/a)</td><td>170.30 (n/a)</td><td>103.00 (n/a)</td><td>39.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (-4.78%)</td><td>0.05 (+9.35%)</td><td>0.06 <b>(+26.69%)</b></td><td>0.04 (+4.64%)</td><td>0.01 <b>(-20.56%)</b></td><td>198.90 (-4.42%)</td><td>153.98 (-9.65%)</td><td>143.40 <b>(-21.08%)</b></td><td>132.10 (+5.09%)</td><td>27.32 (-19.15%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>170.42 (n/a)</td><td>181.70 (n/a)</td><td>125.70 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (+9.18%)</td><td>0.05 (+12.68%)</td><td>0.05 (+15.44%)</td><td>0.04 (+9.09%)</td><td>0.01 <b>(+27.25%)</b></td><td>186.60 (-8.35%)</td><td>163.92 (-10.97%)</td><td>161.60 (-13.35%)</td><td>142.90 (-8.46%)</td><td>20.22 (+7.22%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>203.60 (n/a)</td><td>184.12 (n/a)</td><td>186.50 (n/a)</td><td>156.10 (n/a)</td><td>18.86 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (-9.86%)</td><td>0.05 (+0.02%)</td><td>0.05 (+14.31%)</td><td>0.02 <b>(-41.71%)</b></td><td>0.01 <b>(+55.01%)</b></td><td>364.70 <b>(+71.54%)</b></td><td>193.70 (+10.58%)</td><td>150.70 (-12.54%)</td><td>142.60 (+10.97%)</td><td>96.14 <b>(+210.88%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>175.16 (n/a)</td><td>172.30 (n/a)</td><td>128.50 (n/a)</td><td>30.93 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (+18.25%)</td><td>0.05 (+10.68%)</td><td>0.05 (+12.29%)</td><td>0.04 (+4.13%)</td><td>0.01 <b>(+89.11%)</b></td><td>204.50 (-3.95%)</td><td>181.50 (-9.02%)</td><td>178.20 (-10.94%)</td><td>155.60 (-15.39%)</td><td>20.38 <b>(+54.27%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>212.90 (n/a)</td><td>199.50 (n/a)</td><td>200.10 (n/a)</td><td>183.90 (n/a)</td><td>13.21 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (+19.86%)</td><td>0.05 <b>(+22.69%)</b></td><td>0.05 (+14.30%)</td><td>0.04 <b>(+44.38%)</b></td><td>0.00 <b>(-39.03%)</b></td><td>192.00 <b>(-30.74%)</b></td><td>171.04 <b>(-20.04%)</b></td><td>166.70 (-12.54%)</td><td>154.70 (-16.56%)</td><td>14.32 <b>(-64.01%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>277.20 (n/a)</td><td>213.92 (n/a)</td><td>190.60 (n/a)</td><td>185.40 (n/a)</td><td>39.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.21 (-0.15%)</td><td>0.21 (+0.23%)</td><td>0.21 (+0.04%)</td><td>0.21 (+0.22%)</td><td>0.00 (-4.06%)</td><td>40867.10 (-0.22%)</td><td>40655.64 (-0.23%)</td><td>40770.20 (-0.04%)</td><td>40389.60 (+0.15%)</td><td>239.80 (-4.11%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40959.00 (n/a)</td><td>40748.26 (n/a)</td><td>40787.30 (n/a)</td><td>40330.90 (n/a)</td><td>250.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (-2.12%)</td><td>0.05 (-9.27%)</td><td>0.05 <b>(-20.98%)</b></td><td>0.04 (-11.07%)</td><td>0.01 (-6.03%)</td><td>227.50 (+12.46%)</td><td>174.84 (+10.34%)</td><td>176.70 <b>(+26.58%)</b></td><td>138.80 (+2.21%)</td><td>33.58 (+11.41%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>158.46 (n/a)</td><td>139.60 (n/a)</td><td>135.80 (n/a)</td><td>30.14 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.09 (-0.61%)</td><td>0.07 (+3.12%)</td><td>0.06 (-2.14%)</td><td>0.05 <b>(+39.87%)</b></td><td>0.01 <b>(-27.33%)</b></td><td>235.60 <b>(-28.52%)</b></td><td>190.66 (-7.59%)</td><td>192.40 (+2.18%)</td><td>143.00 (+0.63%)</td><td>34.61 <b>(-51.72%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>329.60 (n/a)</td><td>206.32 (n/a)</td><td>188.30 (n/a)</td><td>142.10 (n/a)</td><td>71.68 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (-1.22%)</td><td>0.05 (-6.99%)</td><td>0.05 (-3.98%)</td><td>0.04 <b>(-20.77%)</b></td><td>0.01 <b>(+20.75%)</b></td><td>225.60 <b>(+26.25%)</b></td><td>173.68 (+8.79%)</td><td>172.70 (+4.10%)</td><td>139.30 (+1.24%)</td><td>32.32 <b>(+58.92%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.70 (n/a)</td><td>159.64 (n/a)</td><td>165.90 (n/a)</td><td>137.60 (n/a)</td><td>20.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 <b>(-28.63%)</b></td><td>0.06 <b>(-20.45%)</b></td><td>0.06 (-14.66%)</td><td>0.04 (-8.37%)</td><td>0.01 <b>(-47.78%)</b></td><td>229.50 (+9.13%)</td><td>187.16 <b>(+22.71%)</b></td><td>178.40 (+17.14%)</td><td>157.50 <b>(+40.12%)</b></td><td>28.64 <b>(-21.08%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>152.52 (n/a)</td><td>152.30 (n/a)</td><td>112.40 (n/a)</td><td>36.30 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (+11.72%)</td><td>0.05 (-8.34%)</td><td>0.04 (-12.98%)</td><td>0.04 (-14.78%)</td><td>0.01 <b>(+118.11%)</b></td><td>202.40 (+17.33%)</td><td>175.42 (+11.73%)</td><td>185.10 (+14.90%)</td><td>126.90 (-10.44%)</td><td>31.30 <b>(+131.48%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>172.50 (n/a)</td><td>157.00 (n/a)</td><td>161.10 (n/a)</td><td>141.70 (n/a)</td><td>13.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 (+0.14%)</td><td>0.05 (-8.72%)</td><td>0.05 (-19.26%)</td><td>0.05 (-3.50%)</td><td>0.01 (+9.08%)</td><td>220.80 (+3.66%)</td><td>195.54 (+10.06%)</td><td>211.30 <b>(+23.86%)</b></td><td>138.50 (-0.14%)</td><td>33.43 (+8.37%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>177.66 (n/a)</td><td>170.60 (n/a)</td><td>138.70 (n/a)</td><td>30.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (-6.47%)</td><td>0.04 (-16.41%)</td><td>0.04 <b>(-22.16%)</b></td><td>0.03 (-19.92%)</td><td>0.01 <b>(+31.23%)</b></td><td>236.50 <b>(+24.87%)</b></td><td>195.38 <b>(+21.99%)</b></td><td>211.50 <b>(+28.42%)</b></td><td>139.10 (+6.92%)</td><td>38.21 <b>(+73.78%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>160.16 (n/a)</td><td>164.70 (n/a)</td><td>130.10 (n/a)</td><td>21.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.07 (+6.52%)</td><td>0.05 (-12.71%)</td><td>0.04 <b>(-23.30%)</b></td><td>0.04 <b>(-20.93%)</b></td><td>0.01 <b>(+69.76%)</b></td><td>243.10 <b>(+26.48%)</b></td><td>195.96 (+18.58%)</td><td>216.40 <b>(+30.44%)</b></td><td>131.20 (-6.08%)</td><td>44.73 <b>(+99.47%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>165.26 (n/a)</td><td>165.90 (n/a)</td><td>139.70 (n/a)</td><td>22.43 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 <b>(-22.80%)</b></td><td>0.04 <b>(-23.77%)</b></td><td>0.04 <b>(-27.62%)</b></td><td>0.03 <b>(-20.51%)</b></td><td>0.00 <b>(-32.83%)</b></td><td>235.90 <b>(+25.81%)</b></td><td>201.30 <b>(+30.70%)</b></td><td>203.30 <b>(+38.21%)</b></td><td>176.00 <b>(+29.51%)</b></td><td>23.48 (+9.61%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>154.02 (n/a)</td><td>147.10 (n/a)</td><td>135.90 (n/a)</td><td>21.42 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (-16.37%)</td><td>0.05 (-14.79%)</td><td>0.05 (-18.04%)</td><td>0.04 (-8.62%)</td><td>0.00 <b>(-36.14%)</b></td><td>213.00 (+9.40%)</td><td>194.14 (+16.60%)</td><td>197.80 <b>(+22.02%)</b></td><td>166.20 (+19.57%)</td><td>17.90 (-17.83%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>166.50 (n/a)</td><td>162.10 (n/a)</td><td>139.00 (n/a)</td><td>21.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.06 (+3.42%)</td><td>0.05 (-9.95%)</td><td>0.04 (-13.76%)</td><td>0.04 (+2.72%)</td><td>0.01 (+8.60%)</td><td>215.60 (-2.66%)</td><td>185.94 (+11.27%)</td><td>185.00 (+15.99%)</td><td>136.30 (-3.33%)</td><td>32.10 (+0.08%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>167.10 (n/a)</td><td>159.50 (n/a)</td><td>141.00 (n/a)</td><td>32.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (-4.26%)</td><td>0.04 (-19.95%)</td><td>0.04 (-18.35%)</td><td>0.03 <b>(-34.42%)</b></td><td>0.01 <b>(+70.40%)</b></td><td>341.50 <b>(+52.46%)</b></td><td>234.94 <b>(+30.59%)</b></td><td>207.10 <b>(+22.47%)</b></td><td>174.60 (+4.43%)</td><td>67.26 <b>(+172.47%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.00 (n/a)</td><td>179.90 (n/a)</td><td>169.10 (n/a)</td><td>167.20 (n/a)</td><td>24.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 <b>(-21.66%)</b></td><td>0.04 (-18.00%)</td><td>0.04 (-16.72%)</td><td>0.03 <b>(-20.96%)</b></td><td>0.01 <b>(-32.34%)</b></td><td>302.90 <b>(+26.52%)</b></td><td>216.32 <b>(+20.67%)</b></td><td>196.20 <b>(+20.15%)</b></td><td>174.10 <b>(+27.64%)</b></td><td>50.48 (+13.68%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.40 (n/a)</td><td>179.26 (n/a)</td><td>163.30 (n/a)</td><td>136.40 (n/a)</td><td>44.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.05 (-18.64%)</td><td>0.04 (-19.33%)</td><td>0.04 (-19.97%)</td><td>0.04 <b>(-23.73%)</b></td><td>0.00 (+10.49%)</td><td>226.00 <b>(+31.09%)</b></td><td>199.94 <b>(+24.54%)</b></td><td>207.10 <b>(+24.91%)</b></td><td>173.20 <b>(+22.92%)</b></td><td>21.82 <b>(+77.67%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>172.40 (n/a)</td><td>160.54 (n/a)</td><td>165.80 (n/a)</td><td>140.90 (n/a)</td><td>12.28 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.04 (-15.68%)</td><td>0.04 (-13.08%)</td><td>0.04 (-15.46%)</td><td>0.03 (-1.50%)</td><td>0.00 <b>(-64.56%)</b></td><td>241.80 (+1.51%)</td><td>230.04 (+13.87%)</td><td>231.40 (+18.24%)</td><td>213.00 (+18.60%)</td><td>10.92 <b>(-56.93%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>238.20 (n/a)</td><td>202.02 (n/a)</td><td>195.70 (n/a)</td><td>179.60 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.74 (+7.25%)</td><td>0.63 (+14.24%)</td><td>0.64 <b>(+23.41%)</b></td><td>0.54 (+11.64%)</td><td>0.07 (-13.75%)</td><td>181.10 (-10.39%)</td><td>156.74 (-12.97%)</td><td>154.20 (-18.97%)</td><td>133.30 (-6.72%)</td><td>17.36 <b>(-27.63%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.69 (n/a)</td><td>0.55 (n/a)</td><td>0.52 (n/a)</td><td>0.49 (n/a)</td><td>0.08 (n/a)</td><td>202.10 (n/a)</td><td>180.10 (n/a)</td><td>190.30 (n/a)</td><td>142.90 (n/a)</td><td>23.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.71 (-5.39%)</td><td>0.65 (+8.71%)</td><td>0.68 <b>(+21.19%)</b></td><td>0.51 (+16.26%)</td><td>0.08 <b>(-35.91%)</b></td><td>192.30 (-13.96%)</td><td>154.30 (-9.93%)</td><td>145.20 (-17.50%)</td><td>138.30 (+5.65%)</td><td>21.80 <b>(-39.66%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.75 (n/a)</td><td>0.59 (n/a)</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.12 (n/a)</td><td>223.50 (n/a)</td><td>171.32 (n/a)</td><td>176.00 (n/a)</td><td>130.90 (n/a)</td><td>36.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.72 (+1.79%)</td><td>0.54 (-4.54%)</td><td>0.51 (+1.24%)</td><td>0.42 (-9.65%)</td><td>0.12 (+1.98%)</td><td>234.10 (+10.63%)</td><td>187.92 (+5.21%)</td><td>194.30 (-1.22%)</td><td>136.80 (-1.72%)</td><td>39.38 (+12.41%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.71 (n/a)</td><td>0.57 (n/a)</td><td>0.50 (n/a)</td><td>0.46 (n/a)</td><td>0.12 (n/a)</td><td>211.60 (n/a)</td><td>178.62 (n/a)</td><td>196.70 (n/a)</td><td>139.20 (n/a)</td><td>35.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.98 <b>(+84.74%)</b></td><td>0.64 <b>(+36.61%)</b></td><td>0.56 (+14.80%)</td><td>0.47 <b>(+24.34%)</b></td><td>0.20 <b>(+221.97%)</b></td><td>208.50 (-19.59%)</td><td>163.60 <b>(-23.35%)</b></td><td>175.10 (-12.89%)</td><td>100.30 <b>(-45.84%)</b></td><td>39.71 <b>(+31.46%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.53 (n/a)</td><td>0.47 (n/a)</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>0.06 (n/a)</td><td>259.30 (n/a)</td><td>213.44 (n/a)</td><td>201.00 (n/a)</td><td>185.20 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.51 (-4.92%)</td><td>0.42 (+0.34%)</td><td>0.43 (+2.18%)</td><td>0.34 (+7.96%)</td><td>0.06 <b>(-20.80%)</b></td><td>219.80 (-7.37%)</td><td>179.02 (-1.53%)</td><td>169.70 (-2.13%)</td><td>145.70 (+5.20%)</td><td>28.44 <b>(-22.95%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.53 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>237.30 (n/a)</td><td>181.80 (n/a)</td><td>173.40 (n/a)</td><td>138.50 (n/a)</td><td>36.90 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.50 (-9.77%)</td><td>0.40 (-10.95%)</td><td>0.38 (-17.83%)</td><td>0.33 (-10.13%)</td><td>0.08 (+0.47%)</td><td>223.10 (+11.27%)</td><td>187.86 (+12.87%)</td><td>194.70 <b>(+21.69%)</b></td><td>147.20 (+10.84%)</td><td>33.44 <b>(+22.62%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.37 (n/a)</td><td>0.07 (n/a)</td><td>200.50 (n/a)</td><td>166.44 (n/a)</td><td>160.00 (n/a)</td><td>132.80 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.60 (+19.14%)</td><td>0.45 (+7.69%)</td><td>0.42 (-4.24%)</td><td>0.34 (+12.12%)</td><td>0.10 <b>(+26.14%)</b></td><td>215.20 (-10.82%)</td><td>170.84 (-6.75%)</td><td>173.80 (+4.45%)</td><td>123.10 (-16.03%)</td><td>33.90 (-8.99%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.50 (n/a)</td><td>0.41 (n/a)</td><td>0.44 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>241.30 (n/a)</td><td>183.20 (n/a)</td><td>166.40 (n/a)</td><td>146.60 (n/a)</td><td>37.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.52 (+16.67%)</td><td>0.38 (-0.08%)</td><td>0.40 (+8.87%)</td><td>0.24 <b>(-25.22%)</b></td><td>0.12 <b>(+114.08%)</b></td><td>303.40 <b>(+33.72%)</b></td><td>212.52 (+7.14%)</td><td>182.70 (-8.14%)</td><td>142.80 (-14.29%)</td><td>70.59 <b>(+148.76%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.44 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>226.90 (n/a)</td><td>198.36 (n/a)</td><td>198.90 (n/a)</td><td>166.60 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.88 (+17.91%)</td><td>0.75 (+10.37%)</td><td>0.71 (+1.58%)</td><td>0.64 (+8.25%)</td><td>0.09 <b>(+23.64%)</b></td><td>203.40 (-7.63%)</td><td>177.54 (-9.24%)</td><td>183.40 (-1.56%)</td><td>149.10 (-15.19%)</td><td>20.82 (-4.74%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.75 (n/a)</td><td>0.68 (n/a)</td><td>0.70 (n/a)</td><td>0.60 (n/a)</td><td>0.07 (n/a)</td><td>220.20 (n/a)</td><td>195.62 (n/a)</td><td>186.30 (n/a)</td><td>175.80 (n/a)</td><td>21.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.85 (+14.14%)</td><td>0.71 (+4.82%)</td><td>0.79 (+16.90%)</td><td>0.36 <b>(-38.47%)</b></td><td>0.20 <b>(+233.67%)</b></td><td>363.80 <b>(+62.56%)</b></td><td>204.82 (+5.06%)</td><td>165.50 (-14.47%)</td><td>154.40 (-12.37%)</td><td>89.39 <b>(+391.12%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.74 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.59 (n/a)</td><td>0.06 (n/a)</td><td>223.80 (n/a)</td><td>194.96 (n/a)</td><td>193.50 (n/a)</td><td>176.20 (n/a)</td><td>18.20 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.88 (+12.33%)</td><td>0.73 (+7.68%)</td><td>0.71 (+4.82%)</td><td>0.54 (+12.24%)</td><td>0.13 (+6.35%)</td><td>240.70 (-10.92%)</td><td>184.20 (-7.44%)</td><td>184.30 (-4.61%)</td><td>149.80 (-10.99%)</td><td>35.09 (-15.66%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.78 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.49 (n/a)</td><td>0.12 (n/a)</td><td>270.20 (n/a)</td><td>199.00 (n/a)</td><td>193.20 (n/a)</td><td>168.30 (n/a)</td><td>41.60 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.00 (+2.27%)</td><td>0.00 (-2.75%)</td><td>0.00 (-4.55%)</td><td>0.00 (-4.76%)</td><td>0.00 <b>(+103.10%)</b></td><td>1012.65 (+4.78%)</td><td>963.88 (+2.76%)</td><td>973.94 (+4.35%)</td><td>911.51 (-1.23%)</td><td>37.67 <b>(+115.91%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>966.46 (n/a)</td><td>938.03 (n/a)</td><td>933.34 (n/a)</td><td>922.85 (n/a)</td><td>17.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.01 (+2.41%)</td><td>0.01 (-0.49%)</td><td>0.01 (-2.41%)</td><td>0.01 (+0.00%)</td><td>0.00 (+3.28%)</td><td>1085.17 (-1.12%)</td><td>1014.36 (-0.00%)</td><td>1008.94 (+2.08%)</td><td>960.10 (-2.56%)</td><td>44.87 (-6.17%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1097.50 (n/a)</td><td>1014.38 (n/a)</td><td>988.35 (n/a)</td><td>985.32 (n/a)</td><td>47.82 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>0.93 (+0.08%)</td><td>0.93 (-0.31%)</td><td>0.93 (-0.38%)</td><td>0.92 (-0.61%)</td><td>0.00 <b>(+179.94%)</b></td><td>2273.63 (+0.62%)</td><td>2260.12 (+0.31%)</td><td>2261.67 (+0.38%)</td><td>2246.55 (-0.07%)</td><td>11.72 <b>(+180.50%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.00 (n/a)</td><td>2259.63 (n/a)</td><td>2253.15 (n/a)</td><td>2253.08 (n/a)</td><td>2248.18 (n/a)</td><td>4.18 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>3.21 (-8.14%)</td><td>2.48 (-16.00%)</td><td>2.46 (-19.28%)</td><td>1.72 <b>(-29.32%)</b></td><td>0.53 (+18.66%)</td><td>304.00 <b>(+41.46%)</b></td><td>219.86 <b>(+21.58%)</b></td><td>212.80 <b>(+23.86%)</b></td><td>163.50 (+8.85%)</td><td>51.64 <b>(+85.24%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>3.49 (n/a)</td><td>2.95 (n/a)</td><td>3.05 (n/a)</td><td>2.44 (n/a)</td><td>0.45 (n/a)</td><td>214.90 (n/a)</td><td>180.84 (n/a)</td><td>171.80 (n/a)</td><td>150.20 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>6.06 <b>(+25.32%)</b></td><td>4.84 (+7.29%)</td><td>4.76 (+3.66%)</td><td>3.74 (-12.30%)</td><td>0.85 <b>(+245.32%)</b></td><td>280.40 (+14.03%)</td><td>221.94 (-4.66%)</td><td>220.10 (-3.55%)</td><td>173.10 <b>(-20.19%)</b></td><td>39.56 <b>(+211.04%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>4.83 (n/a)</td><td>4.52 (n/a)</td><td>4.60 (n/a)</td><td>4.26 (n/a)</td><td>0.25 (n/a)</td><td>245.90 (n/a)</td><td>232.78 (n/a)</td><td>228.20 (n/a)</td><td>216.90 (n/a)</td><td>12.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 20:53:59</td><td>3.59 (+10.20%)</td><td>2.97 (+10.77%)</td><td>2.81 (+13.69%)</td><td>2.29 (+7.20%)</td><td>0.53 (+7.86%)</td><td>229.30 (-6.71%)</td><td>181.14 (-9.74%)</td><td>186.30 (-12.04%)</td><td>145.90 (-9.27%)</td><td>33.19 (-7.53%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>3.26 (n/a)</td><td>2.68 (n/a)</td><td>2.48 (n/a)</td><td>2.13 (n/a)</td><td>0.49 (n/a)</td><td>245.80 (n/a)</td><td>200.68 (n/a)</td><td>211.80 (n/a)</td><td>160.80 (n/a)</td><td>35.89 (n/a)</td>
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
