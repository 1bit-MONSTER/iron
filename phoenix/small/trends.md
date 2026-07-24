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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.05 (+1.03%)</td><td>0.04 (+6.05%)</td><td>0.04 <b>(+64.98%)</b></td><td>0.02 (+3.51%)</td><td>0.01 (-6.35%)</td><td>581.70 (-3.39%)</td><td>394.14 (-6.47%)</td><td>309.80 <b>(-39.39%)</b></td><td>224.00 (-1.02%)</td><td>173.73 (+1.97%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>602.10 (n/a)</td><td>421.40 (n/a)</td><td>511.10 (n/a)</td><td>226.30 (n/a)</td><td>170.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 <b>(+29.58%)</b></td><td>0.03 (+9.88%)</td><td>0.03 (+2.95%)</td><td>0.02 (-4.28%)</td><td>0.01 <b>(+67.72%)</b></td><td>632.00 (+4.46%)</td><td>466.24 (-4.82%)</td><td>464.50 (-2.86%)</td><td>275.60 <b>(-22.84%)</b></td><td>141.45 <b>(+30.90%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>605.00 (n/a)</td><td>489.86 (n/a)</td><td>478.20 (n/a)</td><td>357.20 (n/a)</td><td>108.07 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (-15.46%)</td><td>0.03 <b>(-33.02%)</b></td><td>0.02 <b>(-51.72%)</b></td><td>0.02 (-12.66%)</td><td>0.01 <b>(-31.67%)</b></td><td>601.50 (+14.51%)</td><td>514.14 <b>(+42.47%)</b></td><td>544.00 <b>(+107.16%)</b></td><td>291.50 (+18.26%)</td><td>127.54 (-12.26%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.30 (n/a)</td><td>360.88 (n/a)</td><td>262.60 (n/a)</td><td>246.50 (n/a)</td><td>145.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 (-16.78%)</td><td>0.02 (-8.31%)</td><td>0.02 (-19.43%)</td><td>0.02 <b>(+24.20%)</b></td><td>0.00 <b>(-60.70%)</b></td><td>341.60 (-19.49%)</td><td>295.42 (-1.13%)</td><td>304.40 <b>(+24.14%)</b></td><td>232.80 <b>(+20.19%)</b></td><td>40.72 <b>(-64.73%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>424.30 (n/a)</td><td>298.80 (n/a)</td><td>245.20 (n/a)</td><td>193.70 (n/a)</td><td>115.47 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 (-4.38%)</td><td>0.02 (+6.42%)</td><td>0.02 (+9.73%)</td><td>0.01 (+1.06%)</td><td>0.01 (-15.53%)</td><td>578.70 (-1.06%)</td><td>328.56 (-11.20%)</td><td>244.10 (-8.88%)</td><td>210.00 (+4.58%)</td><td>152.22 (-17.63%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.90 (n/a)</td><td>370.02 (n/a)</td><td>267.90 (n/a)</td><td>200.80 (n/a)</td><td>184.80 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 (+6.33%)</td><td>0.02 (+7.58%)</td><td>0.02 (+18.87%)</td><td>0.01 (-13.76%)</td><td>0.01 <b>(+26.09%)</b></td><td>623.30 (+15.94%)</td><td>375.72 (-0.19%)</td><td>267.10 (-15.87%)</td><td>214.40 (-5.96%)</td><td>191.33 <b>(+29.77%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>537.60 (n/a)</td><td>376.44 (n/a)</td><td>317.50 (n/a)</td><td>228.00 (n/a)</td><td>147.44 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 (+15.58%)</td><td>0.01 (-6.59%)</td><td>0.01 (-12.07%)</td><td>0.01 (-8.34%)</td><td>0.01 <b>(+41.98%)</b></td><td>523.30 (+9.09%)</td><td>417.88 (+11.49%)</td><td>458.20 (+13.75%)</td><td>221.20 (-13.49%)</td><td>116.48 <b>(+27.08%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>479.70 (n/a)</td><td>374.80 (n/a)</td><td>402.80 (n/a)</td><td>255.70 (n/a)</td><td>91.66 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (+5.33%)</td><td>0.02 <b>(+33.82%)</b></td><td>0.02 <b>(+74.81%)</b></td><td>0.01 <b>(+20.16%)</b></td><td>0.01 (+9.66%)</td><td>666.80 (-16.79%)</td><td>362.06 <b>(-24.15%)</b></td><td>275.50 <b>(-42.79%)</b></td><td>189.00 (-5.03%)</td><td>199.78 (-7.59%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>801.30 (n/a)</td><td>477.32 (n/a)</td><td>481.60 (n/a)</td><td>199.00 (n/a)</td><td>216.19 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 <b>(-32.91%)</b></td><td>0.02 (+5.84%)</td><td>0.02 (+10.30%)</td><td>0.02 <b>(+58.89%)</b></td><td>0.00 <b>(-81.67%)</b></td><td>336.20 <b>(-37.06%)</b></td><td>305.02 (-18.25%)</td><td>305.10 (-9.36%)</td><td>271.10 <b>(+49.04%)</b></td><td>24.34 <b>(-83.34%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>534.20 (n/a)</td><td>373.10 (n/a)</td><td>336.60 (n/a)</td><td>181.90 (n/a)</td><td>146.14 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2050.80 (n/a)</td><td>763.24 (n/a)</td><td>496.40 (n/a)</td><td>254.40 (n/a)</td><td>727.88 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>536.10 (n/a)</td><td>408.76 (n/a)</td><td>451.90 (n/a)</td><td>195.10 (n/a)</td><td>144.92 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>561.10 (n/a)</td><td>390.08 (n/a)</td><td>434.90 (n/a)</td><td>231.80 (n/a)</td><td>142.11 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.10 (n/a)</td><td>323.60 (n/a)</td><td>274.10 (n/a)</td><td>233.90 (n/a)</td><td>125.52 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.90 (n/a)</td><td>316.48 (n/a)</td><td>262.90 (n/a)</td><td>248.10 (n/a)</td><td>115.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>780.50 (n/a)</td><td>401.48 (n/a)</td><td>316.00 (n/a)</td><td>273.40 (n/a)</td><td>214.14 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.70 (n/a)</td><td>336.50 (n/a)</td><td>282.90 (n/a)</td><td>221.30 (n/a)</td><td>130.66 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.50 (n/a)</td><td>390.10 (n/a)</td><td>460.50 (n/a)</td><td>210.20 (n/a)</td><td>147.51 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.10 (n/a)</td><td>354.42 (n/a)</td><td>326.10 (n/a)</td><td>221.70 (n/a)</td><td>142.49 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1380.80 (n/a)</td><td>580.94 (n/a)</td><td>439.40 (n/a)</td><td>290.30 (n/a)</td><td>453.00 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.20 (n/a)</td><td>403.38 (n/a)</td><td>425.50 (n/a)</td><td>246.90 (n/a)</td><td>101.28 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>485.70 (n/a)</td><td>383.08 (n/a)</td><td>371.40 (n/a)</td><td>255.40 (n/a)</td><td>86.28 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemm</summary>


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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.61 <b>(+35.09%)</b></td><td>0.49 <b>(+37.85%)</b></td><td>0.44 (+8.39%)</td><td>0.38 <b>(+193.03%)</b></td><td>0.10 <b>(-28.41%)</b></td><td>585.00 <b>(-65.88%)</b></td><td>467.78 <b>(-40.09%)</b></td><td>498.50 (-7.74%)</td><td>364.70 <b>(-25.98%)</b></td><td>90.28 <b>(-82.85%)</b></td><td>25.87 <b>(+35.09%)</b></td><td>20.80 <b>(+37.85%)</b></td><td>18.93 (+8.39%)</td><td>16.13 <b>(+193.03%)</b></td><td>4.09 <b>(-28.41%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.45 (n/a)</td><td>0.35 (n/a)</td><td>0.41 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>1714.30 (n/a)</td><td>780.78 (n/a)</td><td>540.30 (n/a)</td><td>492.70 (n/a)</td><td>526.30 (n/a)</td><td>19.15 (n/a)</td><td>15.09 (n/a)</td><td>17.47 (n/a)</td><td>5.50 (n/a)</td><td>5.71 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.50 (+9.54%)</td><td>0.44 (+12.54%)</td><td>0.47 <b>(+20.58%)</b></td><td>0.35 (+1.40%)</td><td>0.06 <b>(+41.52%)</b></td><td>628.00 (-1.38%)</td><td>512.92 (-10.48%)</td><td>472.60 (-17.07%)</td><td>442.40 (-8.73%)</td><td>76.76 <b>(+27.99%)</b></td><td>21.33 (+9.54%)</td><td>18.71 (+12.54%)</td><td>19.97 <b>(+20.58%)</b></td><td>15.03 (+1.40%)</td><td>2.60 <b>(+41.52%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.04 (n/a)</td><td>636.80 (n/a)</td><td>572.98 (n/a)</td><td>569.90 (n/a)</td><td>484.70 (n/a)</td><td>59.97 (n/a)</td><td>19.47 (n/a)</td><td>16.62 (n/a)</td><td>16.56 (n/a)</td><td>14.82 (n/a)</td><td>1.83 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.31 (+0.36%)</td><td>0.31 (+0.28%)</td><td>0.31 (+0.67%)</td><td>0.30 (+0.48%)</td><td>0.00 (+8.75%)</td><td>82902.30 (-0.48%)</td><td>82161.88 (-0.28%)</td><td>81887.00 (-0.67%)</td><td>81532.80 (-0.36%)</td><td>635.48 (+7.95%)</td><td>210.71 (+0.36%)</td><td>209.11 (+0.28%)</td><td>209.80 (+0.67%)</td><td>207.23 (+0.48%)</td><td>1.61 (+8.75%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83298.60 (n/a)</td><td>82394.82 (n/a)</td><td>82438.00 (n/a)</td><td>81830.00 (n/a)</td><td>588.70 (n/a)</td><td>209.95 (n/a)</td><td>208.52 (n/a)</td><td>208.40 (n/a)</td><td>206.24 (n/a)</td><td>1.48 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>1.07 (+4.13%)</td><td>1.03 (+0.89%)</td><td>1.02 (+0.36%)</td><td>1.00 (-0.69%)</td><td>0.02 <b>(+291.98%)</b></td><td>25150.90 (+0.69%)</td><td>24528.92 (-0.84%)</td><td>24628.10 (-0.36%)</td><td>23594.10 (-3.97%)</td><td>577.48 <b>(+277.00%)</b></td><td>728.14 (+4.13%)</td><td>700.71 (+0.89%)</td><td>697.57 (+0.36%)</td><td>683.07 (-0.69%)</td><td>16.79 <b>(+291.98%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>0.01 (n/a)</td><td>24977.70 (n/a)</td><td>24735.92 (n/a)</td><td>24717.00 (n/a)</td><td>24568.50 (n/a)</td><td>153.18 (n/a)</td><td>699.27 (n/a)</td><td>694.55 (n/a)</td><td>695.06 (n/a)</td><td>687.81 (n/a)</td><td>4.28 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>2.78 <b>(-28.27%)</b></td><td>2.01 (-0.19%)</td><td>2.08 <b>(+34.31%)</b></td><td>1.36 <b>(+26.20%)</b></td><td>0.54 <b>(-51.75%)</b></td><td>5941.10 <b>(-20.76%)</b></td><td>4259.74 (-12.37%)</td><td>3882.70 <b>(-25.54%)</b></td><td>2900.40 <b>(+39.40%)</b></td><td>1161.30 <b>(-43.58%)</b></td><td>728.83 <b>(-28.27%)</b></td><td>526.19 (-0.19%)</td><td>544.45 <b>(+34.31%)</b></td><td>355.81 <b>(+26.20%)</b></td><td>141.04 <b>(-51.75%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>3.87 (n/a)</td><td>2.01 (n/a)</td><td>1.55 (n/a)</td><td>1.08 (n/a)</td><td>1.11 (n/a)</td><td>7497.60 (n/a)</td><td>4861.04 (n/a)</td><td>5214.70 (n/a)</td><td>2080.60 (n/a)</td><td>2058.45 (n/a)</td><td>1016.01 (n/a)</td><td>527.19 (n/a)</td><td>405.38 (n/a)</td><td>281.95 (n/a)</td><td>292.28 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.23 (+14.68%)</td><td>0.21 (+12.36%)</td><td>0.20 (+4.42%)</td><td>0.19 <b>(+20.96%)</b></td><td>0.02 (+1.00%)</td><td>6502.90 (-17.33%)</td><td>6024.82 (-11.18%)</td><td>6250.90 (-4.24%)</td><td>5434.40 (-12.80%)</td><td>496.30 <b>(-27.30%)</b></td><td>12.35 (+14.68%)</td><td>11.20 (+12.36%)</td><td>10.74 (+4.42%)</td><td>10.32 <b>(+20.96%)</b></td><td>0.95 (+1.00%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>7866.10 (n/a)</td><td>6782.86 (n/a)</td><td>6527.50 (n/a)</td><td>6232.00 (n/a)</td><td>682.70 (n/a)</td><td>10.77 (n/a)</td><td>9.97 (n/a)</td><td>10.28 (n/a)</td><td>8.53 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.12 (-16.71%)</td><td>0.08 <b>(-22.52%)</b></td><td>0.09 (-17.63%)</td><td>0.02 <b>(-70.89%)</b></td><td>0.04 (+18.40%)</td><td>0.11 (-16.71%)</td><td>0.08 <b>(-22.52%)</b></td><td>0.09 (-17.63%)</td><td>0.02 <b>(-70.89%)</b></td><td>0.04 (+18.40%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>3.86 (+4.19%)</td><td>3.70 (+3.22%)</td><td>3.79 (+4.43%)</td><td>3.41 (+1.30%)</td><td>0.19 <b>(+32.12%)</b></td><td>3.86 (+4.19%)</td><td>3.70 (+3.22%)</td><td>3.79 (+4.43%)</td><td>3.41 (+1.30%)</td><td>0.19 <b>(+32.12%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>3.71 (n/a)</td><td>3.58 (n/a)</td><td>3.63 (n/a)</td><td>3.37 (n/a)</td><td>0.14 (n/a)</td><td>3.71 (n/a)</td><td>3.58 (n/a)</td><td>3.63 (n/a)</td><td>3.37 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>7.60 (+9.48%)</td><td>6.42 (-0.80%)</td><td>6.68 (+1.51%)</td><td>4.83 (-14.96%)</td><td>1.19 <b>(+152.04%)</b></td><td>7.59 (+9.48%)</td><td>6.42 (-0.80%)</td><td>6.68 (+1.51%)</td><td>4.83 (-14.96%)</td><td>1.18 <b>(+152.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>6.94 (n/a)</td><td>6.48 (n/a)</td><td>6.58 (n/a)</td><td>5.68 (n/a)</td><td>0.47 (n/a)</td><td>6.94 (n/a)</td><td>6.47 (n/a)</td><td>6.58 (n/a)</td><td>5.68 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>13.70 (-2.53%)</td><td>9.77 (-4.14%)</td><td>8.22 (-16.87%)</td><td>7.96 (-4.59%)</td><td>2.48 (+6.96%)</td><td>13.69 (-2.53%)</td><td>9.77 (-4.14%)</td><td>8.22 (-16.87%)</td><td>7.96 (-4.59%)</td><td>2.48 (+6.96%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>14.05 (n/a)</td><td>10.19 (n/a)</td><td>9.89 (n/a)</td><td>8.35 (n/a)</td><td>2.32 (n/a)</td><td>14.04 (n/a)</td><td>10.19 (n/a)</td><td>9.89 (n/a)</td><td>8.34 (n/a)</td><td>2.32 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>3.93 (+4.15%)</td><td>3.79 (+2.52%)</td><td>3.88 (+4.96%)</td><td>3.53 (-3.46%)</td><td>0.16 <b>(+223.01%)</b></td><td>3.93 (+4.15%)</td><td>3.79 (+2.52%)</td><td>3.88 (+4.96%)</td><td>3.53 (-3.46%)</td><td>0.16 <b>(+223.01%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>3.78 (n/a)</td><td>3.70 (n/a)</td><td>3.70 (n/a)</td><td>3.65 (n/a)</td><td>0.05 (n/a)</td><td>3.77 (n/a)</td><td>3.70 (n/a)</td><td>3.69 (n/a)</td><td>3.65 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>7.55 (-1.73%)</td><td>6.30 (+1.60%)</td><td>6.64 (+12.32%)</td><td>4.84 (-1.46%)</td><td>1.08 (-1.39%)</td><td>7.54 (-1.73%)</td><td>6.30 (+1.60%)</td><td>6.63 (+12.32%)</td><td>4.84 (-1.46%)</td><td>1.08 (-1.39%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>7.68 (n/a)</td><td>6.20 (n/a)</td><td>5.91 (n/a)</td><td>4.91 (n/a)</td><td>1.09 (n/a)</td><td>7.67 (n/a)</td><td>6.20 (n/a)</td><td>5.91 (n/a)</td><td>4.91 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>13.34 (+19.81%)</td><td>9.23 (+3.41%)</td><td>8.57 (+1.25%)</td><td>7.17 (-3.15%)</td><td>2.41 <b>(+56.39%)</b></td><td>13.33 (+19.81%)</td><td>9.22 (+3.41%)</td><td>8.56 (+1.25%)</td><td>7.16 (-3.15%)</td><td>2.41 <b>(+56.39%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>11.14 (n/a)</td><td>8.92 (n/a)</td><td>8.46 (n/a)</td><td>7.40 (n/a)</td><td>1.54 (n/a)</td><td>11.13 (n/a)</td><td>8.92 (n/a)</td><td>8.46 (n/a)</td><td>7.39 (n/a)</td><td>1.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>3.13 (+12.92%)</td><td>2.25 (-7.02%)</td><td>2.81 (+4.73%)</td><td>1.10 (-11.51%)</td><td>1.02 <b>(+55.30%)</b></td><td>3.12 (+12.92%)</td><td>2.24 (-7.02%)</td><td>2.80 (+4.73%)</td><td>1.10 (-11.51%)</td><td>1.02 <b>(+55.30%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>2.77 (n/a)</td><td>2.41 (n/a)</td><td>2.68 (n/a)</td><td>1.24 (n/a)</td><td>0.66 (n/a)</td><td>2.76 (n/a)</td><td>2.41 (n/a)</td><td>2.68 (n/a)</td><td>1.24 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.45 <b>(+38.08%)</b></td><td>0.32 <b>(+24.89%)</b></td><td>0.38 <b>(+25.54%)</b></td><td>0.08 (-1.12%)</td><td>0.15 <b>(+39.58%)</b></td><td>0.45 <b>(+38.08%)</b></td><td>0.32 <b>(+24.89%)</b></td><td>0.38 <b>(+25.54%)</b></td><td>0.07 (-1.12%)</td><td>0.14 <b>(+39.58%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.73 (+16.81%)</td><td>0.61 <b>(+21.14%)</b></td><td>0.63 <b>(+20.38%)</b></td><td>0.35 (+16.20%)</td><td>0.15 (+16.59%)</td><td>0.72 (+16.81%)</td><td>0.60 <b>(+21.14%)</b></td><td>0.63 <b>(+20.38%)</b></td><td>0.34 (+16.20%)</td><td>0.15 (+16.59%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.62 (n/a)</td><td>0.50 (n/a)</td><td>0.53 (n/a)</td><td>0.30 (n/a)</td><td>0.13 (n/a)</td><td>0.62 (n/a)</td><td>0.49 (n/a)</td><td>0.52 (n/a)</td><td>0.29 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>2.41 (+13.81%)</td><td>1.60 (+18.35%)</td><td>2.17 <b>(+31.07%)</b></td><td>0.42 (-4.98%)</td><td>0.98 (+15.86%)</td><td>2.37 (+13.81%)</td><td>1.57 (+18.35%)</td><td>2.14 <b>(+31.07%)</b></td><td>0.41 (-4.98%)</td><td>0.96 (+15.86%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>2.11 (n/a)</td><td>1.35 (n/a)</td><td>1.66 (n/a)</td><td>0.44 (n/a)</td><td>0.85 (n/a)</td><td>2.08 (n/a)</td><td>1.33 (n/a)</td><td>1.63 (n/a)</td><td>0.43 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.00 (n/a)</td><td>446.72 (n/a)</td><td>450.50 (n/a)</td><td>297.50 (n/a)</td><td>122.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.20 (n/a)</td><td>473.42 (n/a)</td><td>486.10 (n/a)</td><td>270.00 (n/a)</td><td>142.45 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>484.00 (n/a)</td><td>375.46 (n/a)</td><td>437.10 (n/a)</td><td>239.00 (n/a)</td><td>112.84 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.50 (n/a)</td><td>482.82 (n/a)</td><td>548.30 (n/a)</td><td>275.50 (n/a)</td><td>144.55 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>492.20 (n/a)</td><td>444.46 (n/a)</td><td>457.20 (n/a)</td><td>367.70 (n/a)</td><td>50.87 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.50 (n/a)</td><td>422.92 (n/a)</td><td>487.10 (n/a)</td><td>263.00 (n/a)</td><td>105.44 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (-3.52%)</td><td>0.03 (+13.06%)</td><td>0.03 (+11.66%)</td><td>0.01 <b>(+210.34%)</b></td><td>0.01 <b>(-26.19%)</b></td><td>634.40 <b>(-67.78%)</b></td><td>383.26 <b>(-45.44%)</b></td><td>250.40 (-10.44%)</td><td>241.00 (+3.66%)</td><td>190.33 <b>(-74.47%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1968.70 (n/a)</td><td>702.40 (n/a)</td><td>279.60 (n/a)</td><td>232.50 (n/a)</td><td>745.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (+8.62%)</td><td>0.02 (-5.94%)</td><td>0.03 <b>(+33.42%)</b></td><td>0.00 <b>(-75.27%)</b></td><td>0.01 <b>(+116.92%)</b></td><td>1903.20 <b>(+304.33%)</b></td><td>645.76 <b>(+92.88%)</b></td><td>248.70 <b>(-25.05%)</b></td><td>220.20 (-7.94%)</td><td>722.10 <b>(+686.34%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>470.70 (n/a)</td><td>334.80 (n/a)</td><td>331.80 (n/a)</td><td>239.20 (n/a)</td><td>91.83 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 <b>(-31.20%)</b></td><td>0.02 (-13.19%)</td><td>0.03 (-0.53%)</td><td>0.00 <b>(-72.02%)</b></td><td>0.01 (-13.87%)</td><td>1886.10 <b>(+257.35%)</b></td><td>605.90 <b>(+75.23%)</b></td><td>314.20 (+0.54%)</td><td>224.10 <b>(+45.33%)</b></td><td>718.19 <b>(+375.98%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>527.80 (n/a)</td><td>345.78 (n/a)</td><td>312.50 (n/a)</td><td>154.20 (n/a)</td><td>150.89 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (-1.05%)</td><td>0.03 (+16.92%)</td><td>0.03 <b>(+27.34%)</b></td><td>0.02 <b>(+49.33%)</b></td><td>0.01 <b>(-39.46%)</b></td><td>429.70 <b>(-33.03%)</b></td><td>309.42 <b>(-24.49%)</b></td><td>295.20 <b>(-21.47%)</b></td><td>226.60 (+1.07%)</td><td>77.57 <b>(-58.08%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>641.60 (n/a)</td><td>409.80 (n/a)</td><td>375.90 (n/a)</td><td>224.20 (n/a)</td><td>185.06 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (-2.48%)</td><td>0.02 (-18.59%)</td><td>0.02 (-19.15%)</td><td>0.01 <b>(-55.00%)</b></td><td>0.01 <b>(+30.17%)</b></td><td>1117.60 <b>(+122.23%)</b></td><td>561.34 <b>(+45.70%)</b></td><td>472.70 <b>(+23.68%)</b></td><td>232.90 (+2.55%)</td><td>330.75 <b>(+212.66%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.90 (n/a)</td><td>385.26 (n/a)</td><td>382.20 (n/a)</td><td>227.10 (n/a)</td><td>105.79 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (+1.74%)</td><td>0.02 (+5.85%)</td><td>0.03 <b>(+44.37%)</b></td><td>0.01 <b>(-21.96%)</b></td><td>0.01 <b>(+34.67%)</b></td><td>610.00 <b>(+28.15%)</b></td><td>398.68 (+3.29%)</td><td>303.20 <b>(-30.74%)</b></td><td>235.10 (-1.67%)</td><td>182.06 <b>(+76.00%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.00 (n/a)</td><td>385.98 (n/a)</td><td>437.80 (n/a)</td><td>239.10 (n/a)</td><td>103.44 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (-19.44%)</td><td>0.02 (+18.79%)</td><td>0.02 <b>(+43.12%)</b></td><td>0.01 <b>(+188.51%)</b></td><td>0.01 <b>(-37.95%)</b></td><td>657.30 <b>(-65.34%)</b></td><td>435.48 <b>(-42.01%)</b></td><td>366.70 <b>(-30.13%)</b></td><td>246.20 <b>(+24.16%)</b></td><td>177.49 <b>(-73.14%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1896.40 (n/a)</td><td>750.90 (n/a)</td><td>524.80 (n/a)</td><td>198.30 (n/a)</td><td>660.81 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 <b>(+40.00%)</b></td><td>0.02 (+15.28%)</td><td>0.02 (-3.80%)</td><td>0.02 <b>(+44.39%)</b></td><td>0.01 <b>(+33.90%)</b></td><td>516.30 <b>(-30.74%)</b></td><td>426.02 (-14.19%)</td><td>463.30 (+3.97%)</td><td>249.50 <b>(-28.57%)</b></td><td>103.31 <b>(-36.79%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>745.40 (n/a)</td><td>496.46 (n/a)</td><td>445.60 (n/a)</td><td>349.30 (n/a)</td><td>163.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (-3.18%)</td><td>0.03 (-4.37%)</td><td>0.03 (-19.61%)</td><td>0.02 (+18.88%)</td><td>0.01 <b>(-29.70%)</b></td><td>469.40 (-15.89%)</td><td>348.68 (-4.02%)</td><td>317.30 <b>(+24.38%)</b></td><td>241.10 (+3.30%)</td><td>104.84 <b>(-37.36%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.10 (n/a)</td><td>363.28 (n/a)</td><td>255.10 (n/a)</td><td>233.40 (n/a)</td><td>167.36 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (+0.11%)</td><td>0.02 (+1.12%)</td><td>0.03 <b>(+57.43%)</b></td><td>0.00 <b>(-78.31%)</b></td><td>0.01 <b>(+34.79%)</b></td><td>2438.50 <b>(+360.96%)</b></td><td>731.64 <b>(+84.19%)</b></td><td>292.20 <b>(-36.49%)</b></td><td>230.70 (-0.13%)</td><td>958.58 <b>(+549.97%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.00 (n/a)</td><td>397.22 (n/a)</td><td>460.10 (n/a)</td><td>231.00 (n/a)</td><td>147.48 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (-10.06%)</td><td>0.02 <b>(-32.78%)</b></td><td>0.02 <b>(-39.01%)</b></td><td>0.01 <b>(-39.02%)</b></td><td>0.01 <b>(+55.86%)</b></td><td>597.60 <b>(+64.00%)</b></td><td>452.66 <b>(+57.03%)</b></td><td>462.10 <b>(+63.98%)</b></td><td>264.80 (+11.17%)</td><td>120.21 <b>(+159.17%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>364.40 (n/a)</td><td>288.26 (n/a)</td><td>281.80 (n/a)</td><td>238.20 (n/a)</td><td>46.38 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.02 <b>(-46.64%)</b></td><td>0.02 <b>(-23.59%)</b></td><td>0.02 (-0.53%)</td><td>0.01 (+1.53%)</td><td>0.00 <b>(-73.03%)</b></td><td>623.90 (-1.52%)</td><td>488.90 (+10.89%)</td><td>482.80 (+0.54%)</td><td>402.60 <b>(+87.43%)</b></td><td>92.31 <b>(-52.52%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.50 (n/a)</td><td>440.88 (n/a)</td><td>480.20 (n/a)</td><td>214.80 (n/a)</td><td>194.42 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (+15.37%)</td><td>0.02 <b>(-20.27%)</b></td><td>0.02 <b>(-32.84%)</b></td><td>0.01 <b>(-34.40%)</b></td><td>0.01 <b>(+66.29%)</b></td><td>734.40 <b>(+52.43%)</b></td><td>469.14 <b>(+40.18%)</b></td><td>477.20 <b>(+48.89%)</b></td><td>228.20 (-13.33%)</td><td>194.56 <b>(+117.35%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.80 (n/a)</td><td>334.68 (n/a)</td><td>320.50 (n/a)</td><td>263.30 (n/a)</td><td>89.51 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (-2.54%)</td><td>0.02 (-14.68%)</td><td>0.02 <b>(-34.49%)</b></td><td>0.01 (-6.65%)</td><td>0.01 (-5.01%)</td><td>583.10 (+7.13%)</td><td>425.88 (+17.04%)</td><td>483.40 <b>(+52.64%)</b></td><td>252.50 (+2.60%)</td><td>135.21 (+4.06%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.30 (n/a)</td><td>363.88 (n/a)</td><td>316.70 (n/a)</td><td>246.10 (n/a)</td><td>129.93 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (+3.02%)</td><td>0.03 (-6.56%)</td><td>0.03 (-0.33%)</td><td>0.01 (-13.13%)</td><td>0.01 <b>(+30.92%)</b></td><td>619.30 (+15.13%)</td><td>388.94 (+16.86%)</td><td>295.10 (+0.34%)</td><td>226.60 (-2.91%)</td><td>190.29 <b>(+50.99%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.90 (n/a)</td><td>332.82 (n/a)</td><td>294.10 (n/a)</td><td>233.40 (n/a)</td><td>126.03 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.05 (-5.72%)</td><td>0.03 <b>(-30.80%)</b></td><td>0.02 <b>(-50.79%)</b></td><td>0.01 <b>(-72.32%)</b></td><td>0.02 <b>(+59.14%)</b></td><td>1900.70 <b>(+261.21%)</b></td><td>695.12 <b>(+129.67%)</b></td><td>519.60 <b>(+103.21%)</b></td><td>228.90 (+6.07%)</td><td>692.13 <b>(+447.55%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.20 (n/a)</td><td>302.66 (n/a)</td><td>255.70 (n/a)</td><td>215.80 (n/a)</td><td>126.41 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (+10.37%)</td><td>0.02 <b>(+21.62%)</b></td><td>0.03 <b>(+71.69%)</b></td><td>0.00 <b>(-66.75%)</b></td><td>0.01 <b>(+71.26%)</b></td><td>2017.20 <b>(+200.76%)</b></td><td>680.36 <b>(+36.40%)</b></td><td>314.40 <b>(-41.76%)</b></td><td>240.50 (-9.38%)</td><td>759.87 <b>(+382.20%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>670.70 (n/a)</td><td>498.78 (n/a)</td><td>539.80 (n/a)</td><td>265.40 (n/a)</td><td>157.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (+3.69%)</td><td>0.02 <b>(-36.95%)</b></td><td>0.02 <b>(-53.86%)</b></td><td>0.01 <b>(-69.72%)</b></td><td>0.01 <b>(+23.62%)</b></td><td>1920.60 <b>(+230.28%)</b></td><td>791.14 <b>(+117.71%)</b></td><td>569.80 <b>(+116.74%)</b></td><td>236.20 (-3.55%)</td><td>654.98 <b>(+325.07%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>581.50 (n/a)</td><td>363.40 (n/a)</td><td>262.90 (n/a)</td><td>244.90 (n/a)</td><td>154.09 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 <b>(+43.37%)</b></td><td>0.02 <b>(+20.30%)</b></td><td>0.02 (+18.03%)</td><td>0.02 (-0.32%)</td><td>0.01 <b>(+69.27%)</b></td><td>535.20 (+0.32%)</td><td>389.24 (-11.08%)</td><td>439.10 (-15.28%)</td><td>210.70 <b>(-30.25%)</b></td><td>146.94 <b>(+20.21%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.50 (n/a)</td><td>437.76 (n/a)</td><td>518.30 (n/a)</td><td>302.10 (n/a)</td><td>122.24 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (+0.09%)</td><td>0.03 (+2.85%)</td><td>0.03 (-10.17%)</td><td>0.02 <b>(+33.68%)</b></td><td>0.01 (-15.18%)</td><td>600.50 <b>(-25.20%)</b></td><td>380.78 (-11.25%)</td><td>321.20 (+11.33%)</td><td>231.20 (-0.09%)</td><td>153.31 <b>(-36.36%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>802.80 (n/a)</td><td>429.06 (n/a)</td><td>288.50 (n/a)</td><td>231.40 (n/a)</td><td>240.92 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (-0.69%)</td><td>0.02 <b>(-22.90%)</b></td><td>0.02 <b>(-38.48%)</b></td><td>0.01 <b>(-57.93%)</b></td><td>0.01 <b>(+33.42%)</b></td><td>1275.30 <b>(+137.71%)</b></td><td>606.56 <b>(+59.60%)</b></td><td>519.00 <b>(+62.54%)</b></td><td>258.60 (+0.66%)</td><td>402.49 <b>(+212.30%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.50 (n/a)</td><td>380.06 (n/a)</td><td>319.30 (n/a)</td><td>256.90 (n/a)</td><td>128.88 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (+3.13%)</td><td>0.02 (-8.95%)</td><td>0.02 <b>(-23.18%)</b></td><td>0.01 (-17.52%)</td><td>0.01 (-4.20%)</td><td>672.30 <b>(+21.24%)</b></td><td>412.40 (+10.69%)</td><td>382.20 <b>(+30.13%)</b></td><td>258.90 (-3.07%)</td><td>157.68 (+18.99%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>554.50 (n/a)</td><td>372.58 (n/a)</td><td>293.70 (n/a)</td><td>267.10 (n/a)</td><td>132.52 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.04 (+11.01%)</td><td>0.03 (+17.13%)</td><td>0.03 <b>(+37.96%)</b></td><td>0.02 <b>(+22.60%)</b></td><td>0.01 (+8.95%)</td><td>520.40 (-18.43%)</td><td>346.64 (-15.37%)</td><td>302.30 <b>(-27.51%)</b></td><td>216.80 (-9.93%)</td><td>131.64 (-16.79%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.00 (n/a)</td><td>409.60 (n/a)</td><td>417.00 (n/a)</td><td>240.70 (n/a)</td><td>158.21 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (-4.25%)</td><td>0.02 (+1.36%)</td><td>0.02 (+1.48%)</td><td>0.02 (-2.97%)</td><td>0.01 (-3.40%)</td><td>555.10 (+3.08%)</td><td>401.42 (-1.34%)</td><td>404.80 (-1.46%)</td><td>288.60 (+4.45%)</td><td>105.69 (+3.21%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.50 (n/a)</td><td>406.88 (n/a)</td><td>410.80 (n/a)</td><td>276.30 (n/a)</td><td>102.40 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.03 (+0.92%)</td><td>0.02 <b>(+21.99%)</b></td><td>0.02 <b>(+35.03%)</b></td><td>0.01 (+4.45%)</td><td>0.01 (-7.42%)</td><td>643.30 (-4.26%)</td><td>438.70 (-18.98%)</td><td>419.20 <b>(-25.95%)</b></td><td>317.70 (-0.90%)</td><td>127.52 (-9.88%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>671.90 (n/a)</td><td>541.48 (n/a)</td><td>566.10 (n/a)</td><td>320.60 (n/a)</td><td>141.50 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.43 <b>(+35.86%)</b></td><td>0.28 (+3.03%)</td><td>0.21 <b>(-25.53%)</b></td><td>0.16 (-18.17%)</td><td>0.12 <b>(+157.81%)</b></td><td>602.30 <b>(+22.20%)</b></td><td>412.18 (+9.73%)</td><td>476.00 <b>(+34.27%)</b></td><td>231.20 <b>(-26.39%)</b></td><td>164.70 <b>(+121.17%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>492.90 (n/a)</td><td>375.62 (n/a)</td><td>354.50 (n/a)</td><td>314.10 (n/a)</td><td>74.47 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.38 (+9.78%)</td><td>0.21 (-2.49%)</td><td>0.17 (-8.26%)</td><td>0.05 <b>(-67.25%)</b></td><td>0.15 <b>(+103.15%)</b></td><td>1935.40 <b>(+205.36%)</b></td><td>829.18 <b>(+69.19%)</b></td><td>568.80 (+9.01%)</td><td>259.10 (-8.90%)</td><td>708.61 <b>(+440.52%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>633.80 (n/a)</td><td>490.08 (n/a)</td><td>521.80 (n/a)</td><td>284.40 (n/a)</td><td>131.10 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.39 (-9.25%)</td><td>0.23 (-3.72%)</td><td>0.18 (-4.54%)</td><td>0.15 (-13.08%)</td><td>0.10 (-8.57%)</td><td>640.40 (+15.06%)</td><td>490.34 (+4.85%)</td><td>551.30 (+4.75%)</td><td>252.40 (+10.22%)</td><td>166.49 <b>(+21.33%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.43 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>556.60 (n/a)</td><td>467.66 (n/a)</td><td>526.30 (n/a)</td><td>229.00 (n/a)</td><td>137.22 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.26 (+9.36%)</td><td>0.19 <b>(+27.01%)</b></td><td>0.16 <b>(+23.80%)</b></td><td>0.14 <b>(+33.63%)</b></td><td>0.06 (+7.18%)</td><td>508.80 <b>(-25.18%)</b></td><td>408.00 <b>(-22.11%)</b></td><td>458.20 (-19.22%)</td><td>280.40 (-8.55%)</td><td>107.00 <b>(-22.61%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>680.00 (n/a)</td><td>523.82 (n/a)</td><td>567.20 (n/a)</td><td>306.60 (n/a)</td><td>138.26 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.30 (+6.62%)</td><td>0.20 (+15.01%)</td><td>0.18 <b>(+29.54%)</b></td><td>0.12 (-5.70%)</td><td>0.07 (+15.29%)</td><td>590.50 (+6.05%)</td><td>404.50 (-11.39%)</td><td>414.20 <b>(-22.80%)</b></td><td>249.00 (-6.18%)</td><td>141.10 (+8.12%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>556.80 (n/a)</td><td>456.48 (n/a)</td><td>536.50 (n/a)</td><td>265.40 (n/a)</td><td>130.50 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.27 (-2.27%)</td><td>0.15 (-5.07%)</td><td>0.14 (-2.52%)</td><td>0.04 <b>(-60.65%)</b></td><td>0.08 <b>(+26.15%)</b></td><td>1741.40 <b>(+154.14%)</b></td><td>706.96 <b>(+38.83%)</b></td><td>524.20 (+2.58%)</td><td>275.20 (+2.34%)</td><td>591.18 <b>(+284.51%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>685.20 (n/a)</td><td>509.24 (n/a)</td><td>511.00 (n/a)</td><td>268.90 (n/a)</td><td>153.75 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.29 <b>(-33.18%)</b></td><td>0.25 (-10.11%)</td><td>0.24 (+0.09%)</td><td>0.20 (-3.67%)</td><td>0.04 <b>(-59.90%)</b></td><td>647.90 (+3.81%)</td><td>529.96 (+5.36%)</td><td>537.20 (-0.09%)</td><td>446.80 <b>(+49.68%)</b></td><td>82.24 <b>(-38.66%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.44 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>624.10 (n/a)</td><td>503.02 (n/a)</td><td>537.70 (n/a)</td><td>298.50 (n/a)</td><td>134.08 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.58 <b>(+41.48%)</b></td><td>0.33 <b>(+28.88%)</b></td><td>0.28 (+11.39%)</td><td>0.26 <b>(+105.13%)</b></td><td>0.14 <b>(+35.88%)</b></td><td>508.40 <b>(-51.25%)</b></td><td>430.68 <b>(-26.25%)</b></td><td>466.60 (-10.23%)</td><td>225.80 <b>(-29.33%)</b></td><td>116.03 <b>(-57.32%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.41 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>1042.80 (n/a)</td><td>583.94 (n/a)</td><td>519.80 (n/a)</td><td>319.50 (n/a)</td><td>271.84 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.26 <b>(-38.85%)</b></td><td>0.21 <b>(-37.80%)</b></td><td>0.23 <b>(-25.94%)</b></td><td>0.12 <b>(-56.16%)</b></td><td>0.05 (-13.40%)</td><td>1056.10 <b>(+128.05%)</b></td><td>671.00 <b>(+67.92%)</b></td><td>581.10 <b>(+35.01%)</b></td><td>510.70 <b>(+63.53%)</b></td><td>223.12 <b>(+232.29%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.06 (n/a)</td><td>463.10 (n/a)</td><td>399.60 (n/a)</td><td>430.40 (n/a)</td><td>312.30 (n/a)</td><td>67.15 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-20.00%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-7.56%)</td><td>22467.92 (+6.92%)</td><td>16698.71 <b>(+27.43%)</b></td><td>16773.64 <b>(+26.29%)</b></td><td>6248.54 (+0.83%)</td><td>6463.07 (-0.52%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21012.89 (n/a)</td><td>13104.67 (n/a)</td><td>13281.81 (n/a)</td><td>6197.35 (n/a)</td><td>6496.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.00 <b>(-61.54%)</b></td><td>0.00 <b>(-47.62%)</b></td><td>0.00 <b>(-60.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-86.83%)</b></td><td>22354.73 (-2.85%)</td><td>19287.32 <b>(+45.54%)</b></td><td>18602.01 <b>(+134.65%)</b></td><td>16075.85 <b>(+149.55%)</b></td><td>2501.18 <b>(-69.79%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23010.60 (n/a)</td><td>13252.01 (n/a)</td><td>7927.55 (n/a)</td><td>6441.89 (n/a)</td><td>8280.10 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>0.16 (+5.95%)</td><td>0.10 (-11.58%)</td><td>0.08 <b>(-33.44%)</b></td><td>0.08 (+3.07%)</td><td>0.03 (+8.84%)</td><td>27172.73 (-2.91%)</td><td>21913.98 (+13.53%)</td><td>24912.62 <b>(+50.23%)</b></td><td>13093.31 (-5.58%)</td><td>5720.16 (-2.60%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>27986.88 (n/a)</td><td>19303.07 (n/a)</td><td>16582.76 (n/a)</td><td>13866.77 (n/a)</td><td>5872.92 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>1.60 <b>(-33.83%)</b></td><td>0.86 <b>(-33.18%)</b></td><td>0.78 <b>(-23.52%)</b></td><td>0.28 <b>(-51.40%)</b></td><td>0.49 <b>(-29.93%)</b></td><td>1886.20 <b>(+105.78%)</b></td><td>847.50 <b>(+66.64%)</b></td><td>674.20 <b>(+30.76%)</b></td><td>326.70 <b>(+51.11%)</b></td><td>609.95 <b>(+133.71%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>2.43 (n/a)</td><td>1.29 (n/a)</td><td>1.02 (n/a)</td><td>0.57 (n/a)</td><td>0.70 (n/a)</td><td>916.60 (n/a)</td><td>508.58 (n/a)</td><td>515.60 (n/a)</td><td>216.20 (n/a)</td><td>260.98 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>2.65 <b>(+57.02%)</b></td><td>2.11 <b>(+98.70%)</b></td><td>2.19 <b>(+65.55%)</b></td><td>1.38 <b>(+360.22%)</b></td><td>0.55 <b>(-20.66%)</b></td><td>757.70 <b>(-78.27%)</b></td><td>529.86 <b>(-69.53%)</b></td><td>477.80 <b>(-39.60%)</b></td><td>395.00 <b>(-36.31%)</b></td><td>153.97 <b>(-89.40%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>1.69 (n/a)</td><td>1.06 (n/a)</td><td>1.33 (n/a)</td><td>0.30 (n/a)</td><td>0.69 (n/a)</td><td>3487.00 (n/a)</td><td>1738.86 (n/a)</td><td>791.00 (n/a)</td><td>620.20 (n/a)</td><td>1452.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.58 (-2.67%)</td><td>1.21 (+5.65%)</td><td>1.29 <b>(+41.89%)</b></td><td>0.66 <b>(-20.05%)</b></td><td>0.38 (-2.53%)</td><td>792.90 <b>(+25.08%)</b></td><td>479.12 (-3.80%)</td><td>406.80 <b>(-29.52%)</b></td><td>331.10 (+2.76%)</td><td>189.18 <b>(+26.62%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>1.63 (n/a)</td><td>1.14 (n/a)</td><td>0.91 (n/a)</td><td>0.83 (n/a)</td><td>0.38 (n/a)</td><td>633.90 (n/a)</td><td>498.02 (n/a)</td><td>577.20 (n/a)</td><td>322.20 (n/a)</td><td>149.40 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:20:01</td><td>1.94 (+13.97%)</td><td>1.25 (+5.92%)</td><td>1.19 <b>(+29.36%)</b></td><td>0.70 (-17.35%)</td><td>0.45 (+14.33%)</td><td>748.60 <b>(+21.00%)</b></td><td>468.72 (-3.24%)</td><td>439.70 <b>(-22.70%)</b></td><td>270.30 (-12.24%)</td><td>175.91 <b>(+22.29%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>1.70 (n/a)</td><td>1.18 (n/a)</td><td>0.92 (n/a)</td><td>0.85 (n/a)</td><td>0.39 (n/a)</td><td>618.70 (n/a)</td><td>484.44 (n/a)</td><td>568.80 (n/a)</td><td>308.00 (n/a)</td><td>143.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.75 (-15.44%)</td><td>1.32 (-0.50%)</td><td>1.36 <b>(+22.47%)</b></td><td>0.77 (-19.20%)</td><td>0.36 <b>(-21.75%)</b></td><td>678.10 <b>(+23.76%)</b></td><td>430.02 (-0.09%)</td><td>385.10 (-18.34%)</td><td>300.10 (+18.29%)</td><td>146.96 (+19.46%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>2.07 (n/a)</td><td>1.32 (n/a)</td><td>1.11 (n/a)</td><td>0.96 (n/a)</td><td>0.46 (n/a)</td><td>547.90 (n/a)</td><td>430.40 (n/a)</td><td>471.60 (n/a)</td><td>253.70 (n/a)</td><td>123.02 (n/a)</td>
</tr>
</tbody>
</table>


</details>
