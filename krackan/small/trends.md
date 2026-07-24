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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.09 (-5.83%)</td><td>0.07 (-2.63%)</td><td>0.06 (-5.49%)</td><td>0.06 (+3.45%)</td><td>0.01 (-17.59%)</td><td>198.50 (-3.31%)</td><td>179.50 (+1.95%)</td><td>190.40 (+5.78%)</td><td>137.40 (+6.26%)</td><td>24.66 (-14.59%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>176.06 (n/a)</td><td>180.00 (n/a)</td><td>129.30 (n/a)</td><td>28.88 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (-14.04%)</td><td>0.06 (-17.21%)</td><td>0.06 (-14.15%)</td><td>0.05 <b>(-22.70%)</b></td><td>0.01 (-0.53%)</td><td>271.00 <b>(+29.36%)</b></td><td>216.02 <b>(+21.67%)</b></td><td>214.10 (+16.49%)</td><td>170.90 (+16.34%)</td><td>36.52 <b>(+51.51%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>177.54 (n/a)</td><td>183.80 (n/a)</td><td>146.90 (n/a)</td><td>24.10 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (-8.57%)</td><td>0.06 <b>(-20.29%)</b></td><td>0.06 (-19.96%)</td><td>0.04 <b>(-24.30%)</b></td><td>0.01 <b>(+25.27%)</b></td><td>276.20 <b>(+32.09%)</b></td><td>214.00 <b>(+27.64%)</b></td><td>194.50 <b>(+24.92%)</b></td><td>167.20 (+9.35%)</td><td>43.44 <b>(+82.30%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>167.66 (n/a)</td><td>155.70 (n/a)</td><td>152.90 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (-16.16%)</td><td>0.06 (-14.73%)</td><td>0.06 (-14.93%)</td><td>0.04 (-4.01%)</td><td>0.01 <b>(-33.89%)</b></td><td>303.50 (+4.19%)</td><td>229.30 (+14.74%)</td><td>221.20 (+17.53%)</td><td>185.60 (+19.28%)</td><td>45.08 (-17.16%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>291.30 (n/a)</td><td>199.84 (n/a)</td><td>188.20 (n/a)</td><td>155.60 (n/a)</td><td>54.42 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (-17.47%)</td><td>0.03 (-11.11%)</td><td>0.03 (-10.52%)</td><td>0.03 (-4.32%)</td><td>0.00 <b>(-40.90%)</b></td><td>195.90 (+4.48%)</td><td>162.90 (+10.52%)</td><td>156.10 (+11.74%)</td><td>138.70 <b>(+21.14%)</b></td><td>22.11 <b>(-25.14%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>147.40 (n/a)</td><td>139.70 (n/a)</td><td>114.50 (n/a)</td><td>29.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (-10.92%)</td><td>0.03 (-14.43%)</td><td>0.03 (-12.70%)</td><td>0.03 (-18.54%)</td><td>0.00 <b>(+20.23%)</b></td><td>192.70 <b>(+22.74%)</b></td><td>170.38 (+17.60%)</td><td>167.70 (+14.55%)</td><td>140.00 (+12.27%)</td><td>20.88 <b>(+67.80%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>157.00 (n/a)</td><td>144.88 (n/a)</td><td>146.40 (n/a)</td><td>124.70 (n/a)</td><td>12.44 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (-19.55%)</td><td>0.03 (-18.08%)</td><td>0.03 (-15.03%)</td><td>0.02 <b>(-36.63%)</b></td><td>0.01 (-1.28%)</td><td>253.90 <b>(+57.80%)</b></td><td>170.44 <b>(+25.12%)</b></td><td>154.50 (+17.76%)</td><td>129.40 <b>(+24.30%)</b></td><td>48.17 <b>(+100.08%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>160.90 (n/a)</td><td>136.22 (n/a)</td><td>131.20 (n/a)</td><td>104.10 (n/a)</td><td>24.07 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 <b>(+30.07%)</b></td><td>0.03 (+2.14%)</td><td>0.03 (+4.93%)</td><td>0.02 <b>(-41.70%)</b></td><td>0.01 <b>(+338.75%)</b></td><td>348.20 <b>(+71.53%)</b></td><td>199.44 (+8.52%)</td><td>173.30 (-4.73%)</td><td>129.80 <b>(-23.10%)</b></td><td>85.25 <b>(+530.49%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.00 (n/a)</td><td>183.78 (n/a)</td><td>181.90 (n/a)</td><td>168.80 (n/a)</td><td>13.52 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (-6.75%)</td><td>0.03 (-11.92%)</td><td>0.03 (+1.99%)</td><td>0.02 <b>(-21.86%)</b></td><td>0.01 <b>(+20.47%)</b></td><td>245.40 <b>(+27.95%)</b></td><td>188.20 (+15.92%)</td><td>164.10 (-1.97%)</td><td>144.40 (+7.20%)</td><td>43.48 <b>(+71.94%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.80 (n/a)</td><td>162.36 (n/a)</td><td>167.40 (n/a)</td><td>134.70 (n/a)</td><td>25.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (+7.95%)</td><td>0.03 (-13.29%)</td><td>0.02 <b>(-27.26%)</b></td><td>0.02 <b>(-30.42%)</b></td><td>0.01 <b>(+120.27%)</b></td><td>313.40 <b>(+43.70%)</b></td><td>222.90 <b>(+24.85%)</b></td><td>243.30 <b>(+37.46%)</b></td><td>135.60 (-7.38%)</td><td>72.89 <b>(+183.94%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.10 (n/a)</td><td>178.54 (n/a)</td><td>177.00 (n/a)</td><td>146.40 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 <b>(+36.15%)</b></td><td>0.03 (+1.84%)</td><td>0.03 (-6.88%)</td><td>0.02 <b>(-20.83%)</b></td><td>0.01 <b>(+133.96%)</b></td><td>299.50 <b>(+26.32%)</b></td><td>208.02 (+5.34%)</td><td>195.70 (+7.41%)</td><td>124.40 <b>(-26.56%)</b></td><td>67.15 <b>(+116.06%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.10 (n/a)</td><td>197.48 (n/a)</td><td>182.20 (n/a)</td><td>169.40 (n/a)</td><td>31.08 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.03 (-11.94%)</td><td>0.02 (-5.00%)</td><td>0.02 (+3.84%)</td><td>0.02 (-3.23%)</td><td>0.00 (-19.47%)</td><td>331.60 (+3.33%)</td><td>244.56 (+4.41%)</td><td>223.10 (-3.71%)</td><td>205.90 (+13.57%)</td><td>50.55 (-4.87%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>320.90 (n/a)</td><td>234.24 (n/a)</td><td>231.70 (n/a)</td><td>181.30 (n/a)</td><td>53.14 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.10 (n/a)</td><td>166.06 (n/a)</td><td>157.20 (n/a)</td><td>136.20 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>240.20 (n/a)</td><td>187.26 (n/a)</td><td>192.10 (n/a)</td><td>139.30 (n/a)</td><td>38.07 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.10 (n/a)</td><td>175.80 (n/a)</td><td>170.30 (n/a)</td><td>149.30 (n/a)</td><td>21.21 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.90 (n/a)</td><td>191.90 (n/a)</td><td>198.70 (n/a)</td><td>147.70 (n/a)</td><td>32.08 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>215.50 (n/a)</td><td>153.84 (n/a)</td><td>160.20 (n/a)</td><td>109.30 (n/a)</td><td>41.28 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>173.70 (n/a)</td><td>157.72 (n/a)</td><td>160.90 (n/a)</td><td>139.00 (n/a)</td><td>16.32 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>199.60 (n/a)</td><td>185.80 (n/a)</td><td>184.10 (n/a)</td><td>170.60 (n/a)</td><td>12.52 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>179.08 (n/a)</td><td>190.30 (n/a)</td><td>129.00 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.20 (n/a)</td><td>149.32 (n/a)</td><td>145.10 (n/a)</td><td>127.50 (n/a)</td><td>21.05 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.70 (n/a)</td><td>162.32 (n/a)</td><td>171.90 (n/a)</td><td>126.40 (n/a)</td><td>24.44 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>168.30 (n/a)</td><td>178.80 (n/a)</td><td>109.50 (n/a)</td><td>36.11 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.60 (n/a)</td><td>184.70 (n/a)</td><td>172.00 (n/a)</td><td>127.10 (n/a)</td><td>52.23 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.20 (n/a)</td><td>162.90 (n/a)</td><td>171.40 (n/a)</td><td>120.30 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>196.60 (n/a)</td><td>202.60 (n/a)</td><td>155.50 (n/a)</td><td>25.86 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>224.70 (n/a)</td><td>197.86 (n/a)</td><td>194.00 (n/a)</td><td>179.10 (n/a)</td><td>17.05 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.80 (n/a)</td><td>204.88 (n/a)</td><td>210.20 (n/a)</td><td>172.00 (n/a)</td><td>25.02 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>4.24 (-13.09%)</td><td>4.00 (-7.03%)</td><td>4.09 (-1.87%)</td><td>3.49 (-14.79%)</td><td>0.30 (-8.91%)</td><td>2693.20 (+17.35%)</td><td>2362.24 (+7.63%)</td><td>2301.50 (+1.91%)</td><td>2218.80 (+15.07%)</td><td>190.20 <b>(+26.06%)</b></td><td>1667.30 (-13.09%)</td><td>1573.52 (-7.03%)</td><td>1607.38 (-1.87%)</td><td>1373.59 (-14.79%)</td><td>116.12 (-8.91%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>4.88 (n/a)</td><td>4.30 (n/a)</td><td>4.16 (n/a)</td><td>4.10 (n/a)</td><td>0.32 (n/a)</td><td>2295.00 (n/a)</td><td>2194.82 (n/a)</td><td>2258.30 (n/a)</td><td>1928.20 (n/a)</td><td>150.88 (n/a)</td><td>1918.52 (n/a)</td><td>1692.50 (n/a)</td><td>1638.09 (n/a)</td><td>1611.95 (n/a)</td><td>127.48 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>1.09 (+1.36%)</td><td>0.95 (+16.03%)</td><td>0.99 <b>(+28.60%)</b></td><td>0.83 (+14.59%)</td><td>0.11 <b>(-23.10%)</b></td><td>267.30 (-12.73%)</td><td>234.68 (-14.68%)</td><td>223.80 <b>(-22.24%)</b></td><td>202.60 (-1.32%)</td><td>28.22 <b>(-31.54%)</b></td><td>46.59 (+1.36%)</td><td>40.68 (+16.03%)</td><td>42.17 <b>(+28.60%)</b></td><td>35.31 (+14.59%)</td><td>4.83 <b>(-23.10%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>1.08 (n/a)</td><td>0.82 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.15 (n/a)</td><td>306.30 (n/a)</td><td>275.06 (n/a)</td><td>287.80 (n/a)</td><td>205.30 (n/a)</td><td>41.22 (n/a)</td><td>45.97 (n/a)</td><td>35.06 (n/a)</td><td>32.79 (n/a)</td><td>30.81 (n/a)</td><td>6.28 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>1.11 (-5.39%)</td><td>0.93 (-8.38%)</td><td>1.03 (-2.23%)</td><td>0.60 <b>(-28.04%)</b></td><td>0.22 <b>(+53.33%)</b></td><td>369.70 <b>(+38.98%)</b></td><td>250.54 (+13.56%)</td><td>215.30 (+2.33%)</td><td>198.50 (+5.70%)</td><td>72.91 <b>(+121.26%)</b></td><td>47.55 (-5.39%)</td><td>39.86 (-8.38%)</td><td>43.84 (-2.23%)</td><td>25.53 <b>(-28.04%)</b></td><td>9.55 <b>(+53.33%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>1.18 (n/a)</td><td>1.02 (n/a)</td><td>1.05 (n/a)</td><td>0.83 (n/a)</td><td>0.15 (n/a)</td><td>266.00 (n/a)</td><td>220.62 (n/a)</td><td>210.40 (n/a)</td><td>187.80 (n/a)</td><td>32.95 (n/a)</td><td>50.25 (n/a)</td><td>43.51 (n/a)</td><td>44.84 (n/a)</td><td>35.47 (n/a)</td><td>6.23 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.52 (-0.06%)</td><td>0.52 (-0.09%)</td><td>0.52 (-0.05%)</td><td>0.52 (-0.27%)</td><td>0.00 <b>(+97.43%)</b></td><td>48798.10 (+0.27%)</td><td>48657.18 (+0.09%)</td><td>48634.50 (+0.05%)</td><td>48581.00 (+0.06%)</td><td>82.85 <b>(+98.20%)</b></td><td>353.63 (-0.06%)</td><td>353.08 (-0.09%)</td><td>353.24 (-0.05%)</td><td>352.06 (-0.27%)</td><td>0.60 <b>(+97.42%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48666.30 (n/a)</td><td>48613.20 (n/a)</td><td>48609.40 (n/a)</td><td>48552.70 (n/a)</td><td>41.80 (n/a)</td><td>353.84 (n/a)</td><td>353.40 (n/a)</td><td>353.43 (n/a)</td><td>353.01 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.89 (-0.37%)</td><td>0.88 (-0.56%)</td><td>0.88 (-0.84%)</td><td>0.88 (-0.49%)</td><td>0.01 <b>(+29.88%)</b></td><td>28720.40 (+0.49%)</td><td>28594.26 (+0.56%)</td><td>28699.50 (+0.85%)</td><td>28361.50 (+0.37%)</td><td>167.70 <b>(+31.15%)</b></td><td>605.75 (-0.37%)</td><td>600.83 (-0.56%)</td><td>598.61 (-0.84%)</td><td>598.18 (-0.49%)</td><td>3.53 <b>(+29.88%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.00 (n/a)</td><td>28581.00 (n/a)</td><td>28433.62 (n/a)</td><td>28457.80 (n/a)</td><td>28256.80 (n/a)</td><td>127.86 (n/a)</td><td>607.99 (n/a)</td><td>604.22 (n/a)</td><td>603.70 (n/a)</td><td>601.09 (n/a)</td><td>2.72 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>3.33 (+0.70%)</td><td>3.19 (-0.78%)</td><td>3.19 (-0.84%)</td><td>3.09 (-2.04%)</td><td>0.09 <b>(+51.93%)</b></td><td>8149.20 (+2.08%)</td><td>7893.34 (+0.82%)</td><td>7887.90 (+0.85%)</td><td>7559.20 (-0.69%)</td><td>215.29 <b>(+53.70%)</b></td><td>2272.72 (+0.70%)</td><td>2177.81 (-0.78%)</td><td>2177.99 (-0.84%)</td><td>2108.16 (-2.04%)</td><td>60.28 <b>(+51.94%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>3.31 (n/a)</td><td>3.22 (n/a)</td><td>3.22 (n/a)</td><td>3.15 (n/a)</td><td>0.06 (n/a)</td><td>7982.80 (n/a)</td><td>7828.94 (n/a)</td><td>7821.50 (n/a)</td><td>7612.00 (n/a)</td><td>140.07 (n/a)</td><td>2256.95 (n/a)</td><td>2194.97 (n/a)</td><td>2196.49 (n/a)</td><td>2152.10 (n/a)</td><td>39.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>4.08 (-2.31%)</td><td>3.71 (+3.71%)</td><td>3.66 (-1.76%)</td><td>3.42 (+12.87%)</td><td>0.25 <b>(-51.13%)</b></td><td>2359.50 (-11.40%)</td><td>2180.40 (-4.86%)</td><td>2200.10 (+1.80%)</td><td>1976.70 (+2.36%)</td><td>144.34 <b>(-57.03%)</b></td><td>1069.40 (-2.31%)</td><td>972.99 (+3.71%)</td><td>960.82 (-1.76%)</td><td>895.94 (+12.87%)</td><td>65.68 <b>(-51.13%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>4.17 (n/a)</td><td>3.58 (n/a)</td><td>3.73 (n/a)</td><td>3.03 (n/a)</td><td>0.51 (n/a)</td><td>2663.10 (n/a)</td><td>2291.72 (n/a)</td><td>2161.30 (n/a)</td><td>1931.10 (n/a)</td><td>335.92 (n/a)</td><td>1094.70 (n/a)</td><td>938.15 (n/a)</td><td>978.07 (n/a)</td><td>793.79 (n/a)</td><td>134.40 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.34 (-6.70%)</td><td>0.31 (-5.75%)</td><td>0.33 (-4.67%)</td><td>0.27 (-9.26%)</td><td>0.03 (+4.27%)</td><td>4617.80 (+10.21%)</td><td>4030.62 (+6.28%)</td><td>3808.70 (+4.89%)</td><td>3678.60 (+7.18%)</td><td>427.60 <b>(+20.27%)</b></td><td>18.24 (-6.70%)</td><td>16.79 (-5.75%)</td><td>17.62 (-4.67%)</td><td>14.53 (-9.26%)</td><td>1.70 (+4.27%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.03 (n/a)</td><td>4190.00 (n/a)</td><td>3792.34 (n/a)</td><td>3631.00 (n/a)</td><td>3432.10 (n/a)</td><td>355.53 (n/a)</td><td>19.55 (n/a)</td><td>17.82 (n/a)</td><td>18.48 (n/a)</td><td>16.02 (n/a)</td><td>1.63 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>5.99 <b>(+22.43%)</b></td><td>4.32 (-6.14%)</td><td>3.92 (-18.67%)</td><td>3.38 (-9.17%)</td><td>1.06 <b>(+112.71%)</b></td><td>1969.20 (+10.09%)</td><td>1605.74 (+10.01%)</td><td>1695.40 <b>(+22.96%)</b></td><td>1110.60 (-18.31%)</td><td>347.88 <b>(+88.43%)</b></td><td>1850.62 <b>(+22.43%)</b></td><td>1336.18 (-6.14%)</td><td>1212.23 (-18.67%)</td><td>1043.68 (-9.17%)</td><td>328.50 <b>(+112.71%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>4.89 (n/a)</td><td>4.61 (n/a)</td><td>4.82 (n/a)</td><td>3.72 (n/a)</td><td>0.50 (n/a)</td><td>1788.70 (n/a)</td><td>1459.64 (n/a)</td><td>1378.80 (n/a)</td><td>1359.60 (n/a)</td><td>184.62 (n/a)</td><td>1511.58 (n/a)</td><td>1423.64 (n/a)</td><td>1490.55 (n/a)</td><td>1149.03 (n/a)</td><td>154.44 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.28 (+8.61%)</td><td>0.20 (+1.84%)</td><td>0.19 (+0.95%)</td><td>0.15 (+1.88%)</td><td>0.05 <b>(+21.90%)</b></td><td>0.28 (+8.61%)</td><td>0.20 (+1.84%)</td><td>0.18 (+0.95%)</td><td>0.14 (+1.88%)</td><td>0.05 <b>(+21.90%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>13.16 (-2.12%)</td><td>11.85 (-6.86%)</td><td>12.73 (-4.42%)</td><td>10.15 (-0.10%)</td><td>1.42 (-1.15%)</td><td>13.15 (-2.12%)</td><td>11.85 (-6.86%)</td><td>12.73 (-4.42%)</td><td>10.14 (-0.10%)</td><td>1.42 (-1.15%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>13.44 (n/a)</td><td>12.73 (n/a)</td><td>13.32 (n/a)</td><td>10.16 (n/a)</td><td>1.44 (n/a)</td><td>13.43 (n/a)</td><td>12.72 (n/a)</td><td>13.31 (n/a)</td><td>10.15 (n/a)</td><td>1.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>25.71 (+1.82%)</td><td>22.49 (-8.40%)</td><td>24.09 (-1.14%)</td><td>13.49 <b>(-44.08%)</b></td><td>5.08 <b>(+919.58%)</b></td><td>25.70 (+1.82%)</td><td>22.48 (-8.40%)</td><td>24.08 (-1.14%)</td><td>13.48 <b>(-44.08%)</b></td><td>5.08 <b>(+919.58%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>25.25 (n/a)</td><td>24.56 (n/a)</td><td>24.37 (n/a)</td><td>24.12 (n/a)</td><td>0.50 (n/a)</td><td>25.24 (n/a)</td><td>24.54 (n/a)</td><td>24.36 (n/a)</td><td>24.11 (n/a)</td><td>0.50 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>41.41 (-7.22%)</td><td>40.36 (+1.95%)</td><td>40.71 (+2.07%)</td><td>38.65 (+11.90%)</td><td>1.04 <b>(-71.80%)</b></td><td>41.39 (-7.22%)</td><td>40.33 (+1.95%)</td><td>40.68 (+2.07%)</td><td>38.63 (+11.90%)</td><td>1.04 <b>(-71.80%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>44.64 (n/a)</td><td>39.58 (n/a)</td><td>39.88 (n/a)</td><td>34.54 (n/a)</td><td>3.69 (n/a)</td><td>44.61 (n/a)</td><td>39.56 (n/a)</td><td>39.86 (n/a)</td><td>34.52 (n/a)</td><td>3.68 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>45.23 (+1.84%)</td><td>42.71 (-0.46%)</td><td>42.61 (-2.14%)</td><td>40.14 (-0.56%)</td><td>2.12 <b>(+32.61%)</b></td><td>45.20 (+1.84%)</td><td>42.68 (-0.46%)</td><td>42.58 (-2.14%)</td><td>40.11 (-0.56%)</td><td>2.12 <b>(+32.61%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>44.41 (n/a)</td><td>42.90 (n/a)</td><td>43.54 (n/a)</td><td>40.37 (n/a)</td><td>1.60 (n/a)</td><td>44.39 (n/a)</td><td>42.88 (n/a)</td><td>43.51 (n/a)</td><td>40.34 (n/a)</td><td>1.60 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>13.29 (+0.24%)</td><td>12.31 (-3.51%)</td><td>12.64 (-4.45%)</td><td>10.91 (+0.19%)</td><td>0.92 (-12.22%)</td><td>13.28 (+0.24%)</td><td>12.30 (-3.51%)</td><td>12.63 (-4.45%)</td><td>10.90 (+0.19%)</td><td>0.92 (-12.22%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>13.26 (n/a)</td><td>12.76 (n/a)</td><td>13.22 (n/a)</td><td>10.89 (n/a)</td><td>1.05 (n/a)</td><td>13.25 (n/a)</td><td>12.75 (n/a)</td><td>13.22 (n/a)</td><td>10.88 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>24.81 (-1.46%)</td><td>23.93 (-2.31%)</td><td>23.95 (-1.12%)</td><td>22.44 (-6.61%)</td><td>0.93 <b>(+70.83%)</b></td><td>24.79 (-1.46%)</td><td>23.92 (-2.31%)</td><td>23.93 (-1.12%)</td><td>22.43 (-6.61%)</td><td>0.93 <b>(+70.83%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>25.17 (n/a)</td><td>24.50 (n/a)</td><td>24.22 (n/a)</td><td>24.03 (n/a)</td><td>0.55 (n/a)</td><td>25.16 (n/a)</td><td>24.48 (n/a)</td><td>24.20 (n/a)</td><td>24.01 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>39.51 (-6.78%)</td><td>37.87 (-4.15%)</td><td>38.31 (-1.96%)</td><td>35.45 (-3.96%)</td><td>1.71 (-13.92%)</td><td>39.49 (-6.78%)</td><td>37.85 (-4.15%)</td><td>38.29 (-1.96%)</td><td>35.43 (-3.96%)</td><td>1.71 (-13.92%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>42.38 (n/a)</td><td>39.51 (n/a)</td><td>39.08 (n/a)</td><td>36.91 (n/a)</td><td>1.99 (n/a)</td><td>42.36 (n/a)</td><td>39.49 (n/a)</td><td>39.05 (n/a)</td><td>36.89 (n/a)</td><td>1.98 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>44.72 (-4.23%)</td><td>43.36 (-0.88%)</td><td>43.37 (+0.53%)</td><td>41.65 (-1.15%)</td><td>1.14 <b>(-34.30%)</b></td><td>44.69 (-4.23%)</td><td>43.34 (-0.88%)</td><td>43.35 (+0.53%)</td><td>41.62 (-1.15%)</td><td>1.14 <b>(-34.30%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>46.69 (n/a)</td><td>43.75 (n/a)</td><td>43.15 (n/a)</td><td>42.13 (n/a)</td><td>1.73 (n/a)</td><td>46.66 (n/a)</td><td>43.72 (n/a)</td><td>43.12 (n/a)</td><td>42.11 (n/a)</td><td>1.73 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>9.62 (-4.32%)</td><td>8.98 (-3.66%)</td><td>9.25 (-1.25%)</td><td>8.15 (-4.49%)</td><td>0.61 (+13.40%)</td><td>9.60 (-4.32%)</td><td>8.96 (-3.66%)</td><td>9.23 (-1.25%)</td><td>8.14 (-4.49%)</td><td>0.61 (+13.40%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>10.06 (n/a)</td><td>9.32 (n/a)</td><td>9.36 (n/a)</td><td>8.54 (n/a)</td><td>0.54 (n/a)</td><td>10.04 (n/a)</td><td>9.31 (n/a)</td><td>9.35 (n/a)</td><td>8.52 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.86 (-5.51%)</td><td>0.80 (-5.98%)</td><td>0.79 (-6.52%)</td><td>0.78 (-3.77%)</td><td>0.03 <b>(-32.53%)</b></td><td>0.84 (-5.51%)</td><td>0.79 (-5.98%)</td><td>0.78 (-6.52%)</td><td>0.76 (-3.77%)</td><td>0.03 <b>(-32.53%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.91 (n/a)</td><td>0.86 (n/a)</td><td>0.85 (n/a)</td><td>0.81 (n/a)</td><td>0.05 (n/a)</td><td>0.89 (n/a)</td><td>0.84 (n/a)</td><td>0.83 (n/a)</td><td>0.79 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>1.18 (+1.34%)</td><td>1.03 (-1.70%)</td><td>1.07 (-3.38%)</td><td>0.87 (+0.31%)</td><td>0.13 (-5.54%)</td><td>1.16 (+1.34%)</td><td>1.02 (-1.70%)</td><td>1.05 (-3.38%)</td><td>0.86 (+0.31%)</td><td>0.12 (-5.54%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>1.16 (n/a)</td><td>1.05 (n/a)</td><td>1.10 (n/a)</td><td>0.86 (n/a)</td><td>0.13 (n/a)</td><td>1.15 (n/a)</td><td>1.04 (n/a)</td><td>1.09 (n/a)</td><td>0.85 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>16.73 (-2.17%)</td><td>16.12 (+9.19%)</td><td>16.30 (+9.32%)</td><td>15.37 (+18.85%)</td><td>0.57 <b>(-63.25%)</b></td><td>16.53 (-2.17%)</td><td>15.94 (+9.19%)</td><td>16.11 (+9.32%)</td><td>15.20 (+18.85%)</td><td>0.57 <b>(-63.25%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>17.10 (n/a)</td><td>14.77 (n/a)</td><td>14.91 (n/a)</td><td>12.94 (n/a)</td><td>1.56 (n/a)</td><td>16.90 (n/a)</td><td>14.60 (n/a)</td><td>14.74 (n/a)</td><td>12.79 (n/a)</td><td>1.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>12.34 (-1.56%)</td><td>10.98 (-9.60%)</td><td>11.77 (-2.97%)</td><td>7.63 <b>(-35.11%)</b></td><td>1.92 <b>(+480.18%)</b></td><td>12.12 (-1.56%)</td><td>10.78 (-9.60%)</td><td>11.56 (-2.97%)</td><td>7.50 <b>(-35.11%)</b></td><td>1.88 <b>(+480.18%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>12.54 (n/a)</td><td>12.14 (n/a)</td><td>12.13 (n/a)</td><td>11.76 (n/a)</td><td>0.33 (n/a)</td><td>12.32 (n/a)</td><td>11.93 (n/a)</td><td>11.92 (n/a)</td><td>11.55 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>10.60 (+8.14%)</td><td>8.00 (+0.27%)</td><td>7.27 (-6.37%)</td><td>6.27 (-8.04%)</td><td>1.70 <b>(+44.86%)</b></td><td>10.42 (+8.14%)</td><td>7.86 (+0.27%)</td><td>7.15 (-6.37%)</td><td>6.16 (-8.04%)</td><td>1.67 <b>(+44.86%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>9.81 (n/a)</td><td>7.98 (n/a)</td><td>7.77 (n/a)</td><td>6.81 (n/a)</td><td>1.18 (n/a)</td><td>9.64 (n/a)</td><td>7.84 (n/a)</td><td>7.63 (n/a)</td><td>6.70 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>6.64 (-7.96%)</td><td>6.04 (-8.41%)</td><td>6.14 (-6.08%)</td><td>5.58 (-10.01%)</td><td>0.44 (+16.49%)</td><td>6.54 (-7.96%)</td><td>5.95 (-8.41%)</td><td>6.04 (-6.08%)</td><td>5.49 (-10.01%)</td><td>0.43 (+16.49%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>7.22 (n/a)</td><td>6.60 (n/a)</td><td>6.53 (n/a)</td><td>6.20 (n/a)</td><td>0.38 (n/a)</td><td>7.10 (n/a)</td><td>6.49 (n/a)</td><td>6.43 (n/a)</td><td>6.10 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>232.60 (n/a)</td><td>209.94 (n/a)</td><td>209.40 (n/a)</td><td>191.50 (n/a)</td><td>15.65 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>202.36 (n/a)</td><td>211.90 (n/a)</td><td>160.40 (n/a)</td><td>24.62 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.50 (n/a)</td><td>187.46 (n/a)</td><td>188.70 (n/a)</td><td>165.20 (n/a)</td><td>17.55 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.90 (n/a)</td><td>184.46 (n/a)</td><td>174.20 (n/a)</td><td>165.10 (n/a)</td><td>28.62 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.70 (n/a)</td><td>178.70 (n/a)</td><td>175.40 (n/a)</td><td>149.80 (n/a)</td><td>30.49 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>220.50 (n/a)</td><td>184.30 (n/a)</td><td>175.30 (n/a)</td><td>163.40 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>255.90 (n/a)</td><td>202.48 (n/a)</td><td>199.50 (n/a)</td><td>160.00 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>289.20 (n/a)</td><td>243.18 (n/a)</td><td>236.80 (n/a)</td><td>219.70 (n/a)</td><td>26.81 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 <b>(-26.00%)</b></td><td>0.05 (-17.24%)</td><td>0.05 (-13.72%)</td><td>0.04 (+2.18%)</td><td>0.01 <b>(-58.83%)</b></td><td>197.80 (-2.13%)</td><td>171.66 (+16.52%)</td><td>172.80 (+15.90%)</td><td>145.70 <b>(+35.16%)</b></td><td>19.98 <b>(-45.37%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.10 (n/a)</td><td>147.32 (n/a)</td><td>149.10 (n/a)</td><td>107.80 (n/a)</td><td>36.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (-19.46%)</td><td>0.05 <b>(-25.91%)</b></td><td>0.05 <b>(-28.11%)</b></td><td>0.04 <b>(-29.63%)</b></td><td>0.01 <b>(+86.98%)</b></td><td>194.90 <b>(+42.06%)</b></td><td>174.76 <b>(+36.11%)</b></td><td>174.20 <b>(+39.14%)</b></td><td>153.20 <b>(+24.15%)</b></td><td>19.66 <b>(+232.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>137.20 (n/a)</td><td>128.40 (n/a)</td><td>125.20 (n/a)</td><td>123.40 (n/a)</td><td>5.92 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (-12.20%)</td><td>0.05 <b>(-20.68%)</b></td><td>0.05 <b>(-22.70%)</b></td><td>0.04 (-7.77%)</td><td>0.01 (-13.25%)</td><td>211.60 (+8.40%)</td><td>179.84 <b>(+25.71%)</b></td><td>172.40 <b>(+29.33%)</b></td><td>133.40 (+13.92%)</td><td>32.24 (+5.21%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.20 (n/a)</td><td>143.06 (n/a)</td><td>133.30 (n/a)</td><td>117.10 (n/a)</td><td>30.64 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (-7.97%)</td><td>0.05 <b>(-20.05%)</b></td><td>0.05 (-13.50%)</td><td>0.04 <b>(-26.66%)</b></td><td>0.01 <b>(+35.12%)</b></td><td>213.20 <b>(+36.32%)</b></td><td>176.76 <b>(+27.90%)</b></td><td>168.60 (+15.64%)</td><td>126.20 (+8.70%)</td><td>35.32 <b>(+103.58%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>156.40 (n/a)</td><td>138.20 (n/a)</td><td>145.80 (n/a)</td><td>116.10 (n/a)</td><td>17.35 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.08 (+15.23%)</td><td>0.06 (+10.20%)</td><td>0.05 (-14.30%)</td><td>0.04 <b>(+38.46%)</b></td><td>0.02 <b>(-20.42%)</b></td><td>219.70 <b>(-27.75%)</b></td><td>158.22 (-18.82%)</td><td>160.50 (+16.73%)</td><td>102.20 (-13.24%)</td><td>46.92 <b>(-51.57%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>304.10 (n/a)</td><td>194.90 (n/a)</td><td>137.50 (n/a)</td><td>117.80 (n/a)</td><td>96.90 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (-2.22%)</td><td>0.04 (-17.45%)</td><td>0.04 <b>(-25.12%)</b></td><td>0.04 <b>(-24.65%)</b></td><td>0.01 <b>(+65.28%)</b></td><td>222.00 <b>(+32.70%)</b></td><td>194.26 <b>(+25.07%)</b></td><td>214.50 <b>(+33.56%)</b></td><td>127.30 (+2.25%)</td><td>39.75 <b>(+125.44%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>167.30 (n/a)</td><td>155.32 (n/a)</td><td>160.60 (n/a)</td><td>124.50 (n/a)</td><td>17.63 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 <b>(-27.98%)</b></td><td>0.05 (-9.35%)</td><td>0.05 (+0.22%)</td><td>0.04 (+11.22%)</td><td>0.00 <b>(-75.08%)</b></td><td>183.10 (-10.11%)</td><td>171.44 (+6.68%)</td><td>165.20 (-0.18%)</td><td>162.20 <b>(+38.87%)</b></td><td>10.56 <b>(-68.31%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>160.70 (n/a)</td><td>165.50 (n/a)</td><td>116.80 (n/a)</td><td>33.33 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (+10.43%)</td><td>0.05 (+3.29%)</td><td>0.04 (-4.56%)</td><td>0.03 (-6.45%)</td><td>0.01 <b>(+63.64%)</b></td><td>235.80 (+6.89%)</td><td>187.96 (+0.12%)</td><td>204.80 (+4.76%)</td><td>132.10 (-9.46%)</td><td>47.11 <b>(+58.12%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>187.74 (n/a)</td><td>195.50 (n/a)</td><td>145.90 (n/a)</td><td>29.79 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (-19.71%)</td><td>0.04 (-1.24%)</td><td>0.04 (+12.48%)</td><td>0.04 (+19.61%)</td><td>0.00 <b>(-79.15%)</b></td><td>207.30 (-16.41%)</td><td>197.10 (-3.25%)</td><td>199.40 (-11.10%)</td><td>184.20 <b>(+24.54%)</b></td><td>10.29 <b>(-78.18%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.00 (n/a)</td><td>203.72 (n/a)</td><td>224.30 (n/a)</td><td>147.90 (n/a)</td><td>47.18 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 <b>(+26.04%)</b></td><td>0.04 (+0.05%)</td><td>0.04 (-4.29%)</td><td>0.02 <b>(-23.33%)</b></td><td>0.01 <b>(+119.90%)</b></td><td>331.80 <b>(+30.42%)</b></td><td>222.14 (+6.63%)</td><td>216.50 (+4.49%)</td><td>139.20 <b>(-20.64%)</b></td><td>71.91 <b>(+129.02%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.40 (n/a)</td><td>208.32 (n/a)</td><td>207.20 (n/a)</td><td>175.40 (n/a)</td><td>31.40 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (-8.40%)</td><td>0.05 (-15.78%)</td><td>0.05 (-15.22%)</td><td>0.03 <b>(-25.31%)</b></td><td>0.01 <b>(+37.40%)</b></td><td>239.20 <b>(+33.93%)</b></td><td>186.88 <b>(+20.93%)</b></td><td>178.60 (+17.97%)</td><td>143.40 (+9.13%)</td><td>36.00 <b>(+102.07%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.60 (n/a)</td><td>154.54 (n/a)</td><td>151.40 (n/a)</td><td>131.40 (n/a)</td><td>17.81 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 (-14.67%)</td><td>0.04 (-11.34%)</td><td>0.04 (-12.27%)</td><td>0.03 (-13.26%)</td><td>0.00 <b>(-20.27%)</b></td><td>237.90 (+15.32%)</td><td>218.46 (+12.75%)</td><td>221.60 (+13.99%)</td><td>202.00 (+17.24%)</td><td>14.31 (+7.79%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.30 (n/a)</td><td>193.76 (n/a)</td><td>194.40 (n/a)</td><td>172.30 (n/a)</td><td>13.27 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.08 <b>(+49.32%)</b></td><td>0.05 <b>(+29.23%)</b></td><td>0.05 (+10.42%)</td><td>0.04 <b>(+58.94%)</b></td><td>0.02 <b>(+34.28%)</b></td><td>208.30 <b>(-37.09%)</b></td><td>162.26 <b>(-24.20%)</b></td><td>170.30 (-9.46%)</td><td>103.00 <b>(-33.03%)</b></td><td>39.03 <b>(-46.00%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>331.10 (n/a)</td><td>214.06 (n/a)</td><td>188.10 (n/a)</td><td>153.80 (n/a)</td><td>72.27 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (+9.57%)</td><td>0.05 (-6.77%)</td><td>0.05 (-16.62%)</td><td>0.04 (-18.72%)</td><td>0.01 <b>(+149.57%)</b></td><td>208.10 <b>(+22.99%)</b></td><td>170.42 (+10.45%)</td><td>181.70 (+19.93%)</td><td>125.70 (-8.78%)</td><td>33.79 <b>(+177.39%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>169.20 (n/a)</td><td>154.30 (n/a)</td><td>151.50 (n/a)</td><td>137.80 (n/a)</td><td>12.18 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (-9.47%)</td><td>0.04 (-10.96%)</td><td>0.04 (-16.16%)</td><td>0.04 (+7.81%)</td><td>0.00 <b>(-39.58%)</b></td><td>203.60 (-7.24%)</td><td>184.12 (+10.62%)</td><td>186.50 (+19.25%)</td><td>156.10 (+10.47%)</td><td>18.86 <b>(-39.64%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.50 (n/a)</td><td>166.44 (n/a)</td><td>156.40 (n/a)</td><td>141.30 (n/a)</td><td>31.24 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (-17.98%)</td><td>0.05 (-18.35%)</td><td>0.05 (-13.17%)</td><td>0.04 (-0.68%)</td><td>0.01 <b>(-36.40%)</b></td><td>212.60 (+0.66%)</td><td>175.16 (+19.01%)</td><td>172.30 (+15.17%)</td><td>128.50 <b>(+21.92%)</b></td><td>30.93 <b>(-24.23%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>147.18 (n/a)</td><td>149.60 (n/a)</td><td>105.40 (n/a)</td><td>40.81 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 <b>(-25.18%)</b></td><td>0.04 (-15.38%)</td><td>0.04 <b>(-20.47%)</b></td><td>0.04 (+6.02%)</td><td>0.00 <b>(-74.72%)</b></td><td>212.90 (-5.71%)</td><td>199.50 (+13.62%)</td><td>200.10 <b>(+25.77%)</b></td><td>183.90 <b>(+33.65%)</b></td><td>13.21 <b>(-68.11%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.80 (n/a)</td><td>175.58 (n/a)</td><td>159.10 (n/a)</td><td>137.60 (n/a)</td><td>41.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.04 <b>(-38.88%)</b></td><td>0.04 <b>(-26.77%)</b></td><td>0.04 (-16.87%)</td><td>0.03 <b>(-23.45%)</b></td><td>0.01 <b>(-48.65%)</b></td><td>277.20 <b>(+30.63%)</b></td><td>213.92 <b>(+34.09%)</b></td><td>190.60 <b>(+20.33%)</b></td><td>185.40 <b>(+63.64%)</b></td><td>39.79 (+8.60%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>159.54 (n/a)</td><td>158.40 (n/a)</td><td>113.30 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.21 (+0.25%)</td><td>0.21 (-0.01%)</td><td>0.21 (+0.03%)</td><td>0.20 (-0.20%)</td><td>0.00 <b>(+39.02%)</b></td><td>40959.00 (+0.20%)</td><td>40748.26 (+0.01%)</td><td>40787.30 (-0.03%)</td><td>40330.90 (-0.25%)</td><td>250.07 <b>(+38.94%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40876.00 (n/a)</td><td>40742.86 (n/a)</td><td>40798.30 (n/a)</td><td>40430.80 (n/a)</td><td>179.98 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (-17.83%)</td><td>0.05 (+6.63%)</td><td>0.06 <b>(+29.40%)</b></td><td>0.04 (+3.24%)</td><td>0.01 <b>(-32.50%)</b></td><td>202.30 (-3.11%)</td><td>158.46 (-8.14%)</td><td>139.60 <b>(-22.74%)</b></td><td>135.80 <b>(+21.68%)</b></td><td>30.14 (-18.39%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>172.50 (n/a)</td><td>180.70 (n/a)</td><td>111.60 (n/a)</td><td>36.94 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.09 (+6.51%)</td><td>0.06 (-0.29%)</td><td>0.07 (-3.21%)</td><td>0.04 (-1.02%)</td><td>0.02 (+8.02%)</td><td>329.60 (+1.04%)</td><td>206.32 (+0.91%)</td><td>188.30 (+3.35%)</td><td>142.10 (-6.14%)</td><td>71.68 (+2.89%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>326.20 (n/a)</td><td>204.46 (n/a)</td><td>182.20 (n/a)</td><td>151.40 (n/a)</td><td>69.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (-10.27%)</td><td>0.05 (+6.95%)</td><td>0.05 (+9.70%)</td><td>0.05 <b>(+40.47%)</b></td><td>0.01 <b>(-45.60%)</b></td><td>178.70 <b>(-28.83%)</b></td><td>159.64 (-10.34%)</td><td>165.90 (-8.85%)</td><td>137.60 (+11.42%)</td><td>20.34 <b>(-57.41%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.10 (n/a)</td><td>178.06 (n/a)</td><td>182.00 (n/a)</td><td>123.50 (n/a)</td><td>47.75 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.09 <b>(+37.67%)</b></td><td>0.07 <b>(+29.78%)</b></td><td>0.07 <b>(+31.49%)</b></td><td>0.05 (+3.40%)</td><td>0.02 <b>(+107.90%)</b></td><td>210.30 (-3.31%)</td><td>152.52 <b>(-20.74%)</b></td><td>152.30 <b>(-23.93%)</b></td><td>112.40 <b>(-27.34%)</b></td><td>36.30 <b>(+51.32%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>217.50 (n/a)</td><td>192.44 (n/a)</td><td>200.20 (n/a)</td><td>154.70 (n/a)</td><td>23.99 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (-10.90%)</td><td>0.05 (+3.37%)</td><td>0.05 (+8.54%)</td><td>0.05 <b>(+20.99%)</b></td><td>0.00 <b>(-55.85%)</b></td><td>172.50 (-17.35%)</td><td>157.00 (-5.78%)</td><td>161.10 (-7.84%)</td><td>141.70 (+12.19%)</td><td>13.52 <b>(-58.89%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>166.64 (n/a)</td><td>174.80 (n/a)</td><td>126.30 (n/a)</td><td>32.89 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (+16.96%)</td><td>0.06 (+14.92%)</td><td>0.06 <b>(+21.94%)</b></td><td>0.05 (+13.92%)</td><td>0.01 <b>(+24.40%)</b></td><td>213.00 (-12.24%)</td><td>177.66 (-12.65%)</td><td>170.60 (-17.98%)</td><td>138.70 (-14.49%)</td><td>30.85 (-4.31%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>242.70 (n/a)</td><td>203.38 (n/a)</td><td>208.00 (n/a)</td><td>162.20 (n/a)</td><td>32.24 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (-3.42%)</td><td>0.05 (+12.90%)</td><td>0.05 (+10.90%)</td><td>0.04 <b>(+24.36%)</b></td><td>0.01 <b>(-37.45%)</b></td><td>189.40 (-19.58%)</td><td>160.16 (-14.09%)</td><td>164.70 (-9.80%)</td><td>130.10 (+3.50%)</td><td>21.99 <b>(-47.47%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.50 (n/a)</td><td>186.42 (n/a)</td><td>182.60 (n/a)</td><td>125.70 (n/a)</td><td>41.86 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (+11.93%)</td><td>0.06 <b>(+32.69%)</b></td><td>0.06 <b>(+28.61%)</b></td><td>0.05 <b>(+79.14%)</b></td><td>0.01 <b>(-34.65%)</b></td><td>192.20 <b>(-44.18%)</b></td><td>165.26 <b>(-28.52%)</b></td><td>165.90 <b>(-22.26%)</b></td><td>139.70 (-10.68%)</td><td>22.43 <b>(-68.31%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>344.30 (n/a)</td><td>231.20 (n/a)</td><td>213.40 (n/a)</td><td>156.40 (n/a)</td><td>70.77 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (+7.02%)</td><td>0.05 <b>(+22.34%)</b></td><td>0.06 <b>(+35.67%)</b></td><td>0.04 <b>(+25.88%)</b></td><td>0.01 (-19.80%)</td><td>187.50 <b>(-20.55%)</b></td><td>154.02 (-19.48%)</td><td>147.10 <b>(-26.30%)</b></td><td>135.90 (-6.53%)</td><td>21.42 <b>(-40.10%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.00 (n/a)</td><td>191.28 (n/a)</td><td>199.60 (n/a)</td><td>145.40 (n/a)</td><td>35.76 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.07 (+14.89%)</td><td>0.06 (+9.33%)</td><td>0.06 (+10.50%)</td><td>0.05 (+12.12%)</td><td>0.01 (+15.91%)</td><td>194.70 (-10.77%)</td><td>166.50 (-8.46%)</td><td>162.10 (-9.49%)</td><td>139.00 (-12.96%)</td><td>21.78 (-8.67%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>181.88 (n/a)</td><td>179.10 (n/a)</td><td>159.70 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (+19.32%)</td><td>0.05 (+18.17%)</td><td>0.05 (+18.16%)</td><td>0.04 (-0.87%)</td><td>0.01 <b>(+64.21%)</b></td><td>221.50 (+0.91%)</td><td>167.10 (-14.17%)</td><td>159.50 (-15.38%)</td><td>141.00 (-16.17%)</td><td>32.07 <b>(+38.70%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.50 (n/a)</td><td>194.68 (n/a)</td><td>188.50 (n/a)</td><td>168.20 (n/a)</td><td>23.12 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (-4.46%)</td><td>0.05 <b>(+22.65%)</b></td><td>0.05 <b>(+35.70%)</b></td><td>0.04 <b>(+33.82%)</b></td><td>0.01 <b>(-38.42%)</b></td><td>224.00 <b>(-25.26%)</b></td><td>179.90 <b>(-20.69%)</b></td><td>169.10 <b>(-26.32%)</b></td><td>167.20 (+4.70%)</td><td>24.69 <b>(-50.67%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.70 (n/a)</td><td>226.84 (n/a)</td><td>229.50 (n/a)</td><td>159.70 (n/a)</td><td>50.05 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 <b>(+27.24%)</b></td><td>0.05 (+18.72%)</td><td>0.05 <b>(+35.50%)</b></td><td>0.03 (-3.53%)</td><td>0.01 <b>(+88.32%)</b></td><td>239.40 (+3.64%)</td><td>179.26 (-13.18%)</td><td>163.30 <b>(-26.21%)</b></td><td>136.40 <b>(-21.38%)</b></td><td>44.41 <b>(+54.07%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.00 (n/a)</td><td>206.48 (n/a)</td><td>221.30 (n/a)</td><td>173.50 (n/a)</td><td>28.82 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.06 (+14.23%)</td><td>0.05 <b>(+23.41%)</b></td><td>0.05 <b>(+26.37%)</b></td><td>0.05 <b>(+32.19%)</b></td><td>0.00 <b>(-29.79%)</b></td><td>172.40 <b>(-24.35%)</b></td><td>160.54 (-19.79%)</td><td>165.80 <b>(-20.86%)</b></td><td>140.90 (-12.48%)</td><td>12.28 <b>(-53.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.90 (n/a)</td><td>200.14 (n/a)</td><td>209.50 (n/a)</td><td>161.00 (n/a)</td><td>26.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.05 (-13.14%)</td><td>0.04 <b>(+25.74%)</b></td><td>0.04 <b>(+30.13%)</b></td><td>0.03 <b>(+61.70%)</b></td><td>0.00 <b>(-60.00%)</b></td><td>238.20 <b>(-38.16%)</b></td><td>202.02 <b>(-27.13%)</b></td><td>195.70 <b>(-23.13%)</b></td><td>179.60 (+15.13%)</td><td>25.35 <b>(-72.03%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>385.20 (n/a)</td><td>277.24 (n/a)</td><td>254.60 (n/a)</td><td>156.00 (n/a)</td><td>90.63 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.69 (+13.22%)</td><td>0.55 (-0.90%)</td><td>0.52 (-8.61%)</td><td>0.49 (-4.49%)</td><td>0.08 <b>(+103.22%)</b></td><td>202.10 (+4.66%)</td><td>180.10 (+2.09%)</td><td>190.30 (+9.43%)</td><td>142.90 (-11.68%)</td><td>23.99 <b>(+85.93%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.61 (n/a)</td><td>0.56 (n/a)</td><td>0.57 (n/a)</td><td>0.51 (n/a)</td><td>0.04 (n/a)</td><td>193.10 (n/a)</td><td>176.42 (n/a)</td><td>173.90 (n/a)</td><td>161.80 (n/a)</td><td>12.90 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.75 (-6.90%)</td><td>0.59 (+2.24%)</td><td>0.56 (+3.21%)</td><td>0.44 (-5.22%)</td><td>0.12 (-6.38%)</td><td>223.50 (+5.47%)</td><td>171.32 (-2.09%)</td><td>176.00 (-3.14%)</td><td>130.90 (+7.47%)</td><td>36.13 (+10.29%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.81 (n/a)</td><td>0.58 (n/a)</td><td>0.54 (n/a)</td><td>0.46 (n/a)</td><td>0.13 (n/a)</td><td>211.90 (n/a)</td><td>174.98 (n/a)</td><td>181.70 (n/a)</td><td>121.80 (n/a)</td><td>32.76 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.71 <b>(+28.74%)</b></td><td>0.57 (+14.46%)</td><td>0.50 (+2.77%)</td><td>0.46 (+5.93%)</td><td>0.12 <b>(+171.37%)</b></td><td>211.60 (-5.58%)</td><td>178.62 (-10.22%)</td><td>196.70 (-2.67%)</td><td>139.20 <b>(-22.32%)</b></td><td>35.03 <b>(+96.40%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.55 (n/a)</td><td>0.50 (n/a)</td><td>0.49 (n/a)</td><td>0.44 (n/a)</td><td>0.04 (n/a)</td><td>224.10 (n/a)</td><td>198.96 (n/a)</td><td>202.10 (n/a)</td><td>179.20 (n/a)</td><td>17.84 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.53 <b>(-29.92%)</b></td><td>0.47 (-18.95%)</td><td>0.49 <b>(-22.14%)</b></td><td>0.38 (+19.59%)</td><td>0.06 <b>(-62.83%)</b></td><td>259.30 (-16.38%)</td><td>213.44 (+14.46%)</td><td>201.00 <b>(+28.43%)</b></td><td>185.20 <b>(+42.68%)</b></td><td>30.21 <b>(-57.92%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.76 (n/a)</td><td>0.58 (n/a)</td><td>0.63 (n/a)</td><td>0.32 (n/a)</td><td>0.17 (n/a)</td><td>310.10 (n/a)</td><td>186.48 (n/a)</td><td>156.50 (n/a)</td><td>129.80 (n/a)</td><td>71.79 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.53 (-9.13%)</td><td>0.42 (-4.56%)</td><td>0.43 (+4.11%)</td><td>0.31 (-8.58%)</td><td>0.08 (-13.37%)</td><td>237.30 (+9.41%)</td><td>181.80 (+4.51%)</td><td>173.40 (-3.99%)</td><td>138.50 (+10.01%)</td><td>36.90 (+7.24%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.59 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.09 (n/a)</td><td>216.90 (n/a)</td><td>173.96 (n/a)</td><td>180.60 (n/a)</td><td>125.90 (n/a)</td><td>34.41 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.56 (+15.99%)</td><td>0.45 (+1.63%)</td><td>0.46 (-0.54%)</td><td>0.37 (-9.54%)</td><td>0.07 <b>(+111.81%)</b></td><td>200.50 (+10.53%)</td><td>166.44 (+0.04%)</td><td>160.00 (+0.57%)</td><td>132.80 (-13.82%)</td><td>27.27 <b>(+101.84%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.48 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.41 (n/a)</td><td>0.04 (n/a)</td><td>181.40 (n/a)</td><td>166.38 (n/a)</td><td>159.10 (n/a)</td><td>154.10 (n/a)</td><td>13.51 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.50 (+1.95%)</td><td>0.41 (-0.57%)</td><td>0.44 (+4.07%)</td><td>0.31 (-13.82%)</td><td>0.08 <b>(+39.08%)</b></td><td>241.30 (+16.01%)</td><td>183.20 (+2.22%)</td><td>166.40 (-3.93%)</td><td>146.60 (-1.94%)</td><td>37.25 <b>(+59.52%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.05 (n/a)</td><td>208.00 (n/a)</td><td>179.22 (n/a)</td><td>173.20 (n/a)</td><td>149.50 (n/a)</td><td>23.35 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.44 (-7.67%)</td><td>0.38 (-11.05%)</td><td>0.37 <b>(-20.54%)</b></td><td>0.32 <b>(+32.84%)</b></td><td>0.05 <b>(-45.77%)</b></td><td>226.90 <b>(-24.72%)</b></td><td>198.36 (+6.74%)</td><td>198.90 <b>(+25.81%)</b></td><td>166.60 (+8.25%)</td><td>28.38 <b>(-56.09%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.48 (n/a)</td><td>0.42 (n/a)</td><td>0.47 (n/a)</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>301.40 (n/a)</td><td>185.84 (n/a)</td><td>158.10 (n/a)</td><td>153.90 (n/a)</td><td>64.63 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.75 (-7.83%)</td><td>0.68 (-3.95%)</td><td>0.70 (-7.16%)</td><td>0.60 (+18.85%)</td><td>0.07 <b>(-39.78%)</b></td><td>220.20 (-15.86%)</td><td>195.62 (+2.08%)</td><td>186.30 (+7.69%)</td><td>175.80 (+8.45%)</td><td>21.85 <b>(-46.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.81 (n/a)</td><td>0.70 (n/a)</td><td>0.76 (n/a)</td><td>0.50 (n/a)</td><td>0.12 (n/a)</td><td>261.70 (n/a)</td><td>191.64 (n/a)</td><td>173.00 (n/a)</td><td>162.10 (n/a)</td><td>40.50 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.74 (-12.89%)</td><td>0.68 (-8.26%)</td><td>0.68 (-3.83%)</td><td>0.59 (-13.13%)</td><td>0.06 (-15.83%)</td><td>223.80 (+15.12%)</td><td>194.96 (+8.96%)</td><td>193.50 (+3.98%)</td><td>176.20 (+14.79%)</td><td>18.20 (+13.08%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.85 (n/a)</td><td>0.74 (n/a)</td><td>0.70 (n/a)</td><td>0.67 (n/a)</td><td>0.07 (n/a)</td><td>194.40 (n/a)</td><td>178.92 (n/a)</td><td>186.10 (n/a)</td><td>153.50 (n/a)</td><td>16.10 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.78 (-9.66%)</td><td>0.68 (+0.52%)</td><td>0.68 (+3.00%)</td><td>0.49 (-9.04%)</td><td>0.12 (-8.08%)</td><td>270.20 (+9.97%)</td><td>199.00 (-0.38%)</td><td>193.20 (-2.91%)</td><td>168.30 (+10.72%)</td><td>41.60 (+13.48%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.86 (n/a)</td><td>0.67 (n/a)</td><td>0.66 (n/a)</td><td>0.53 (n/a)</td><td>0.13 (n/a)</td><td>245.70 (n/a)</td><td>199.76 (n/a)</td><td>199.00 (n/a)</td><td>152.00 (n/a)</td><td>36.66 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.00 (-2.22%)</td><td>0.00 (+2.35%)</td><td>0.00 (+2.33%)</td><td>0.00 (+7.69%)</td><td>0.00 <b>(-61.15%)</b></td><td>966.46 (-6.85%)</td><td>938.03 (-1.89%)</td><td>933.34 (-1.49%)</td><td>922.85 (+1.90%)</td><td>17.45 <b>(-65.68%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1037.49 (n/a)</td><td>956.12 (n/a)</td><td>947.41 (n/a)</td><td>905.60 (n/a)</td><td>50.85 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.01 (-3.49%)</td><td>0.01 (+0.00%)</td><td>0.01 (+2.47%)</td><td>0.01 (-1.32%)</td><td>0.00 (-3.92%)</td><td>1097.50 (+1.82%)</td><td>1014.38 (+0.12%)</td><td>988.35 (-2.24%)</td><td>985.32 (+2.92%)</td><td>47.82 (+8.63%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1077.88 (n/a)</td><td>1013.20 (n/a)</td><td>1010.99 (n/a)</td><td>957.36 (n/a)</td><td>44.02 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>0.93 (-4.80%)</td><td>0.93 (-1.13%)</td><td>0.93 (+0.02%)</td><td>0.93 (+0.10%)</td><td>0.00 <b>(-92.18%)</b></td><td>2259.63 (-0.09%)</td><td>2253.15 (+1.10%)</td><td>2253.08 (-0.02%)</td><td>2248.18 (+5.04%)</td><td>4.18 <b>(-91.75%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>0.98 (n/a)</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.02 (n/a)</td><td>2261.74 (n/a)</td><td>2228.73 (n/a)</td><td>2253.53 (n/a)</td><td>2140.39 (n/a)</td><td>50.60 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>3.49 (-4.27%)</td><td>2.95 (-11.04%)</td><td>3.05 (-10.54%)</td><td>2.44 (-10.94%)</td><td>0.45 <b>(+30.40%)</b></td><td>214.90 (+12.28%)</td><td>180.84 (+13.45%)</td><td>171.80 (+11.78%)</td><td>150.20 (+4.45%)</td><td>27.87 <b>(+51.13%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>3.65 (n/a)</td><td>3.32 (n/a)</td><td>3.41 (n/a)</td><td>2.74 (n/a)</td><td>0.34 (n/a)</td><td>191.40 (n/a)</td><td>159.40 (n/a)</td><td>153.70 (n/a)</td><td>143.80 (n/a)</td><td>18.44 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>4.83 <b>(-25.13%)</b></td><td>4.52 (-10.72%)</td><td>4.60 (-10.56%)</td><td>4.26 (+1.94%)</td><td>0.25 <b>(-72.87%)</b></td><td>245.90 (-1.91%)</td><td>232.78 (+9.58%)</td><td>228.20 (+11.81%)</td><td>216.90 <b>(+33.56%)</b></td><td>12.72 <b>(-64.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>6.46 (n/a)</td><td>5.06 (n/a)</td><td>5.14 (n/a)</td><td>4.18 (n/a)</td><td>0.91 (n/a)</td><td>250.70 (n/a)</td><td>212.42 (n/a)</td><td>204.10 (n/a)</td><td>162.40 (n/a)</td><td>35.76 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:02:06</td><td>3.26 (-7.86%)</td><td>2.68 (-12.75%)</td><td>2.48 <b>(-20.06%)</b></td><td>2.13 (-19.70%)</td><td>0.49 <b>(+31.35%)</b></td><td>245.80 <b>(+24.52%)</b></td><td>200.68 (+16.27%)</td><td>211.80 <b>(+25.10%)</b></td><td>160.80 (+8.50%)</td><td>35.89 <b>(+71.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 03:11:58</td><td>3.54 (n/a)</td><td>3.07 (n/a)</td><td>3.10 (n/a)</td><td>2.66 (n/a)</td><td>0.37 (n/a)</td><td>197.40 (n/a)</td><td>172.60 (n/a)</td><td>169.30 (n/a)</td><td>148.20 (n/a)</td><td>20.94 (n/a)</td>
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
