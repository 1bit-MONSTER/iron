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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 (+5.42%)</td><td>0.03 (-11.72%)</td><td>0.03 (-8.44%)</td><td>0.02 (-6.20%)</td><td>0.01 (-3.70%)</td><td>506.10 (+6.61%)</td><td>425.46 (+12.67%)</td><td>475.90 (+9.20%)</td><td>246.80 (-5.15%)</td><td>104.44 (-3.16%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>474.70 (n/a)</td><td>377.62 (n/a)</td><td>435.80 (n/a)</td><td>260.20 (n/a)</td><td>107.84 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.06 <b>(+42.62%)</b></td><td>0.03 (+6.71%)</td><td>0.02 (-17.95%)</td><td>0.01 <b>(-72.19%)</b></td><td>0.02 <b>(+166.44%)</b></td><td>1899.30 <b>(+259.58%)</b></td><td>684.72 <b>(+61.80%)</b></td><td>525.20 <b>(+21.86%)</b></td><td>190.60 <b>(-29.87%)</b></td><td>696.23 <b>(+641.51%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.20 (n/a)</td><td>423.18 (n/a)</td><td>431.00 (n/a)</td><td>271.80 (n/a)</td><td>93.89 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.06 (+19.49%)</td><td>0.04 <b>(+21.28%)</b></td><td>0.04 <b>(+37.53%)</b></td><td>0.02 <b>(+20.80%)</b></td><td>0.01 <b>(+32.69%)</b></td><td>548.60 (-17.20%)</td><td>375.98 (-15.00%)</td><td>333.00 <b>(-27.29%)</b></td><td>214.90 (-16.32%)</td><td>146.73 (-1.78%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>662.60 (n/a)</td><td>442.32 (n/a)</td><td>458.00 (n/a)</td><td>256.80 (n/a)</td><td>149.40 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (-18.22%)</td><td>0.02 (+4.00%)</td><td>0.02 <b>(+32.29%)</b></td><td>0.01 (+1.16%)</td><td>0.01 (-16.59%)</td><td>481.80 (-1.15%)</td><td>338.30 (-5.15%)</td><td>276.00 <b>(-24.40%)</b></td><td>233.30 <b>(+22.27%)</b></td><td>123.72 (+1.82%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>487.40 (n/a)</td><td>356.68 (n/a)</td><td>365.10 (n/a)</td><td>190.80 (n/a)</td><td>121.51 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (+11.27%)</td><td>0.02 (+16.48%)</td><td>0.02 <b>(+45.51%)</b></td><td>0.01 (-4.34%)</td><td>0.01 <b>(+29.03%)</b></td><td>642.00 (+4.53%)</td><td>349.44 (-9.00%)</td><td>238.40 <b>(-31.28%)</b></td><td>217.10 (-10.14%)</td><td>182.10 (+19.75%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.20 (n/a)</td><td>383.98 (n/a)</td><td>346.90 (n/a)</td><td>241.60 (n/a)</td><td>152.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (+9.99%)</td><td>0.02 (+5.49%)</td><td>0.02 (+5.42%)</td><td>0.01 (-15.08%)</td><td>0.01 <b>(+28.12%)</b></td><td>507.60 (+17.75%)</td><td>323.20 (-1.65%)</td><td>253.50 (-5.13%)</td><td>233.50 (-9.11%)</td><td>120.72 <b>(+30.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>431.10 (n/a)</td><td>328.62 (n/a)</td><td>267.20 (n/a)</td><td>256.90 (n/a)</td><td>92.31 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 <b>(+39.17%)</b></td><td>0.02 <b>(+72.63%)</b></td><td>0.02 <b>(+96.15%)</b></td><td>0.01 <b>(+61.44%)</b></td><td>0.01 <b>(+21.59%)</b></td><td>465.60 <b>(-38.05%)</b></td><td>288.84 <b>(-43.60%)</b></td><td>247.60 <b>(-49.02%)</b></td><td>209.60 <b>(-28.15%)</b></td><td>101.64 <b>(-41.71%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>751.60 (n/a)</td><td>512.10 (n/a)</td><td>485.70 (n/a)</td><td>291.70 (n/a)</td><td>174.36 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (+1.47%)</td><td>0.01 (-1.61%)</td><td>0.01 (-6.54%)</td><td>0.01 (-10.60%)</td><td>0.01 (+17.54%)</td><td>588.20 (+11.87%)</td><td>431.08 (+6.28%)</td><td>472.30 (+6.98%)</td><td>242.90 (-1.46%)</td><td>166.79 <b>(+27.08%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>525.80 (n/a)</td><td>405.60 (n/a)</td><td>441.50 (n/a)</td><td>246.50 (n/a)</td><td>131.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (+7.10%)</td><td>0.01 (-0.88%)</td><td>0.01 (-14.58%)</td><td>0.01 (+16.34%)</td><td>0.00 (-6.36%)</td><td>593.60 (-14.05%)</td><td>468.48 (-2.16%)</td><td>495.30 (+17.06%)</td><td>285.40 (-6.64%)</td><td>133.84 <b>(-24.36%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>690.60 (n/a)</td><td>478.84 (n/a)</td><td>423.10 (n/a)</td><td>305.70 (n/a)</td><td>176.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>458.80 (n/a)</td><td>321.24 (n/a)</td><td>293.80 (n/a)</td><td>228.40 (n/a)</td><td>96.45 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.00 (n/a)</td><td>401.18 (n/a)</td><td>477.80 (n/a)</td><td>244.40 (n/a)</td><td>140.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.30 (n/a)</td><td>347.42 (n/a)</td><td>300.50 (n/a)</td><td>248.50 (n/a)</td><td>103.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>618.30 (n/a)</td><td>424.04 (n/a)</td><td>397.60 (n/a)</td><td>233.30 (n/a)</td><td>169.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>507.80 (n/a)</td><td>303.16 (n/a)</td><td>269.20 (n/a)</td><td>144.60 (n/a)</td><td>132.86 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>627.80 (n/a)</td><td>456.60 (n/a)</td><td>545.80 (n/a)</td><td>258.20 (n/a)</td><td>173.72 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>489.40 (n/a)</td><td>316.02 (n/a)</td><td>292.80 (n/a)</td><td>152.60 (n/a)</td><td>132.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.70 (n/a)</td><td>467.16 (n/a)</td><td>439.50 (n/a)</td><td>359.00 (n/a)</td><td>99.60 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.20 (n/a)</td><td>437.16 (n/a)</td><td>532.70 (n/a)</td><td>204.00 (n/a)</td><td>205.92 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1065.20 (n/a)</td><td>478.54 (n/a)</td><td>310.10 (n/a)</td><td>237.20 (n/a)</td><td>348.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1940.50 (n/a)</td><td>703.96 (n/a)</td><td>480.00 (n/a)</td><td>267.40 (n/a)</td><td>702.42 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1061.50 (n/a)</td><td>549.76 (n/a)</td><td>471.10 (n/a)</td><td>284.20 (n/a)</td><td>299.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.58 <b>(+32.10%)</b></td><td>0.41 (+15.02%)</td><td>0.47 (+9.52%)</td><td>0.13 (+3.71%)</td><td>0.18 <b>(+34.48%)</b></td><td>1731.80 (-3.58%)</td><td>725.36 (-7.60%)</td><td>475.50 (-8.68%)</td><td>384.40 <b>(-24.30%)</b></td><td>570.25 (+0.71%)</td><td>24.55 <b>(+32.10%)</b></td><td>17.59 (+15.02%)</td><td>19.85 (+9.52%)</td><td>5.45 (+3.71%)</td><td>7.68 <b>(+34.48%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.44 (n/a)</td><td>0.36 (n/a)</td><td>0.42 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>1796.10 (n/a)</td><td>785.02 (n/a)</td><td>520.70 (n/a)</td><td>507.80 (n/a)</td><td>566.25 (n/a)</td><td>18.59 (n/a)</td><td>15.29 (n/a)</td><td>18.12 (n/a)</td><td>5.25 (n/a)</td><td>5.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.86 <b>(+76.13%)</b></td><td>0.41 (-6.05%)</td><td>0.35 <b>(-26.42%)</b></td><td>0.12 <b>(-63.59%)</b></td><td>0.32 <b>(+316.47%)</b></td><td>1900.90 <b>(+174.66%)</b></td><td>986.50 <b>(+86.90%)</b></td><td>630.40 <b>(+35.92%)</b></td><td>256.00 <b>(-43.22%)</b></td><td>781.81 <b>(+641.93%)</b></td><td>36.86 <b>(+76.13%)</b></td><td>17.28 (-6.05%)</td><td>14.97 <b>(-26.42%)</b></td><td>4.96 <b>(-63.59%)</b></td><td>13.51 <b>(+316.47%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.49 (n/a)</td><td>0.43 (n/a)</td><td>0.48 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>692.10 (n/a)</td><td>527.82 (n/a)</td><td>463.80 (n/a)</td><td>450.90 (n/a)</td><td>105.38 (n/a)</td><td>20.93 (n/a)</td><td>18.39 (n/a)</td><td>20.35 (n/a)</td><td>13.64 (n/a)</td><td>3.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.31 (-0.58%)</td><td>0.31 (+0.76%)</td><td>0.31 (+0.27%)</td><td>0.30 (+4.01%)</td><td>0.00 <b>(-64.01%)</b></td><td>83500.60 (-3.86%)</td><td>82118.76 (-0.81%)</td><td>81739.00 (-0.27%)</td><td>81519.50 (+0.58%)</td><td>836.05 <b>(-65.24%)</b></td><td>210.75 (-0.58%)</td><td>209.22 (+0.76%)</td><td>210.18 (+0.27%)</td><td>205.75 (+4.01%)</td><td>2.11 <b>(-64.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>86849.40 (n/a)</td><td>82789.18 (n/a)</td><td>81963.50 (n/a)</td><td>81046.90 (n/a)</td><td>2405.44 (n/a)</td><td>211.97 (n/a)</td><td>207.65 (n/a)</td><td>209.60 (n/a)</td><td>197.81 (n/a)</td><td>5.86 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>1.05 (+1.09%)</td><td>1.02 (-0.44%)</td><td>1.01 (-0.02%)</td><td>0.99 (-1.66%)</td><td>0.02 <b>(+67.01%)</b></td><td>25318.30 (+1.68%)</td><td>24789.32 (+0.46%)</td><td>24852.20 (+0.02%)</td><td>24080.60 (-1.08%)</td><td>461.73 <b>(+67.62%)</b></td><td>713.43 (+1.09%)</td><td>693.23 (-0.44%)</td><td>691.28 (-0.02%)</td><td>678.56 (-1.66%)</td><td>13.04 <b>(+67.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>0.01 (n/a)</td><td>24898.80 (n/a)</td><td>24674.80 (n/a)</td><td>24848.10 (n/a)</td><td>24343.70 (n/a)</td><td>275.46 (n/a)</td><td>705.72 (n/a)</td><td>696.32 (n/a)</td><td>691.40 (n/a)</td><td>689.99 (n/a)</td><td>7.81 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>4.10 (+0.92%)</td><td>2.55 (+4.09%)</td><td>2.12 (+0.53%)</td><td>1.58 (-16.76%)</td><td>1.13 <b>(+23.77%)</b></td><td>5106.20 <b>(+20.13%)</b></td><td>3663.16 (+2.94%)</td><td>3796.80 (-0.53%)</td><td>1966.10 (-0.91%)</td><td>1452.53 <b>(+60.11%)</b></td><td>1075.19 (+0.92%)</td><td>668.58 (+4.09%)</td><td>556.77 (+0.53%)</td><td>413.99 (-16.76%)</td><td>295.03 <b>(+23.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>4.06 (n/a)</td><td>2.45 (n/a)</td><td>2.11 (n/a)</td><td>1.90 (n/a)</td><td>0.91 (n/a)</td><td>4250.40 (n/a)</td><td>3558.62 (n/a)</td><td>3817.10 (n/a)</td><td>1984.20 (n/a)</td><td>907.20 (n/a)</td><td>1065.38 (n/a)</td><td>642.29 (n/a)</td><td>553.81 (n/a)</td><td>497.34 (n/a)</td><td>238.37 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.23 (-3.41%)</td><td>0.21 (-3.99%)</td><td>0.20 (-5.30%)</td><td>0.18 (-7.15%)</td><td>0.02 (+14.90%)</td><td>6731.20 (+7.70%)</td><td>6089.84 (+4.36%)</td><td>6217.10 (+5.60%)</td><td>5361.80 (+3.53%)</td><td>533.52 <b>(+28.31%)</b></td><td>12.52 (-3.41%)</td><td>11.09 (-3.99%)</td><td>10.79 (-5.30%)</td><td>9.97 (-7.15%)</td><td>1.00 (+14.90%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>6250.20 (n/a)</td><td>5835.22 (n/a)</td><td>5887.50 (n/a)</td><td>5179.10 (n/a)</td><td>415.79 (n/a)</td><td>12.96 (n/a)</td><td>11.55 (n/a)</td><td>11.40 (n/a)</td><td>10.74 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>3.86 (n/a)</td><td>3.62 (n/a)</td><td>3.65 (n/a)</td><td>3.36 (n/a)</td><td>0.23 (n/a)</td><td>3.86 (n/a)</td><td>3.62 (n/a)</td><td>3.65 (n/a)</td><td>3.36 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>7.01 (-6.53%)</td><td>6.42 (+1.16%)</td><td>6.67 (+15.41%)</td><td>5.48 (-2.42%)</td><td>0.66 <b>(-23.75%)</b></td><td>7.00 (-6.53%)</td><td>6.41 (+1.16%)</td><td>6.67 (+15.41%)</td><td>5.48 (-2.42%)</td><td>0.66 <b>(-23.75%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>7.50 (n/a)</td><td>6.34 (n/a)</td><td>5.78 (n/a)</td><td>5.62 (n/a)</td><td>0.87 (n/a)</td><td>7.49 (n/a)</td><td>6.34 (n/a)</td><td>5.78 (n/a)</td><td>5.61 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>12.77 (-8.10%)</td><td>10.19 (+4.81%)</td><td>11.22 <b>(+32.24%)</b></td><td>7.66 (+3.31%)</td><td>2.22 (-14.39%)</td><td>12.76 (-8.10%)</td><td>10.19 (+4.81%)</td><td>11.22 <b>(+32.24%)</b></td><td>7.65 (+3.31%)</td><td>2.22 (-14.39%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>13.90 (n/a)</td><td>9.73 (n/a)</td><td>8.49 (n/a)</td><td>7.41 (n/a)</td><td>2.60 (n/a)</td><td>13.89 (n/a)</td><td>9.72 (n/a)</td><td>8.48 (n/a)</td><td>7.41 (n/a)</td><td>2.60 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>3.82 (n/a)</td><td>3.63 (n/a)</td><td>3.65 (n/a)</td><td>3.37 (n/a)</td><td>0.17 (n/a)</td><td>3.81 (n/a)</td><td>3.63 (n/a)</td><td>3.65 (n/a)</td><td>3.37 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>7.37 (+2.34%)</td><td>6.32 (+2.24%)</td><td>6.12 (+1.92%)</td><td>5.23 (-4.57%)</td><td>0.86 <b>(+22.77%)</b></td><td>7.36 (+2.34%)</td><td>6.32 (+2.24%)</td><td>6.11 (+1.92%)</td><td>5.22 (-4.57%)</td><td>0.86 <b>(+22.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>7.20 (n/a)</td><td>6.19 (n/a)</td><td>6.00 (n/a)</td><td>5.48 (n/a)</td><td>0.70 (n/a)</td><td>7.20 (n/a)</td><td>6.18 (n/a)</td><td>6.00 (n/a)</td><td>5.47 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>13.27 <b>(+55.78%)</b></td><td>9.92 <b>(+20.05%)</b></td><td>9.85 <b>(+20.25%)</b></td><td>5.81 <b>(-27.48%)</b></td><td>3.17 <b>(+1267.79%)</b></td><td>13.27 <b>(+55.78%)</b></td><td>9.91 <b>(+20.05%)</b></td><td>9.85 <b>(+20.25%)</b></td><td>5.81 <b>(-27.48%)</b></td><td>3.17 <b>(+1267.79%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>8.52 (n/a)</td><td>8.26 (n/a)</td><td>8.19 (n/a)</td><td>8.01 (n/a)</td><td>0.23 (n/a)</td><td>8.52 (n/a)</td><td>8.26 (n/a)</td><td>8.19 (n/a)</td><td>8.01 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>3.10 (-1.60%)</td><td>2.86 (+9.93%)</td><td>2.80 (-6.16%)</td><td>2.63 <b>(+48.78%)</b></td><td>0.21 <b>(-66.90%)</b></td><td>3.09 (-1.60%)</td><td>2.85 (+9.93%)</td><td>2.79 (-6.16%)</td><td>2.62 <b>(+48.78%)</b></td><td>0.21 <b>(-66.90%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>3.15 (n/a)</td><td>2.60 (n/a)</td><td>2.98 (n/a)</td><td>1.77 (n/a)</td><td>0.64 (n/a)</td><td>3.14 (n/a)</td><td>2.59 (n/a)</td><td>2.98 (n/a)</td><td>1.76 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.41 <b>(-21.12%)</b></td><td>0.21 <b>(-28.88%)</b></td><td>0.13 <b>(-60.99%)</b></td><td>0.07 (-0.30%)</td><td>0.16 <b>(-23.81%)</b></td><td>0.40 <b>(-21.12%)</b></td><td>0.21 <b>(-28.88%)</b></td><td>0.12 <b>(-60.99%)</b></td><td>0.07 (-0.30%)</td><td>0.16 <b>(-23.81%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.52 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>0.22 (n/a)</td><td>0.51 (n/a)</td><td>0.29 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.64 (-8.81%)</td><td>0.45 (-0.92%)</td><td>0.44 (-16.05%)</td><td>0.29 <b>(+282.59%)</b></td><td>0.14 <b>(-45.08%)</b></td><td>0.63 (-8.81%)</td><td>0.44 (-0.92%)</td><td>0.43 (-16.05%)</td><td>0.28 <b>(+282.59%)</b></td><td>0.13 <b>(-45.08%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.70 (n/a)</td><td>0.45 (n/a)</td><td>0.52 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td><td>0.69 (n/a)</td><td>0.45 (n/a)</td><td>0.51 (n/a)</td><td>0.07 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>2.35 (-13.63%)</td><td>1.52 (-7.16%)</td><td>2.08 (+10.37%)</td><td>0.43 (-6.31%)</td><td>0.99 (-12.04%)</td><td>2.32 (-13.63%)</td><td>1.49 (-7.16%)</td><td>2.05 (+10.37%)</td><td>0.42 (-6.31%)</td><td>0.97 (-12.04%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>2.72 (n/a)</td><td>1.63 (n/a)</td><td>1.89 (n/a)</td><td>0.46 (n/a)</td><td>1.12 (n/a)</td><td>2.68 (n/a)</td><td>1.61 (n/a)</td><td>1.86 (n/a)</td><td>0.45 (n/a)</td><td>1.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]

_No metrics available._


### test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]

_No metrics available._


### test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]

_No metrics available._


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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>581.20 (n/a)</td><td>465.48 (n/a)</td><td>466.50 (n/a)</td><td>325.10 (n/a)</td><td>91.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.80 (n/a)</td><td>481.02 (n/a)</td><td>513.50 (n/a)</td><td>302.00 (n/a)</td><td>113.83 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1097.20 (n/a)</td><td>508.68 (n/a)</td><td>370.40 (n/a)</td><td>266.20 (n/a)</td><td>341.84 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>972.40 (n/a)</td><td>590.78 (n/a)</td><td>494.20 (n/a)</td><td>455.50 (n/a)</td><td>215.73 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>678.30 (n/a)</td><td>532.30 (n/a)</td><td>506.00 (n/a)</td><td>438.30 (n/a)</td><td>102.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>629.00 (n/a)</td><td>453.20 (n/a)</td><td>550.20 (n/a)</td><td>184.70 (n/a)</td><td>188.13 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (+14.00%)</td><td>0.03 (+15.47%)</td><td>0.02 <b>(+28.00%)</b></td><td>0.01 (+13.26%)</td><td>0.01 (+5.61%)</td><td>548.60 (-11.72%)</td><td>359.66 (-15.01%)</td><td>349.40 <b>(-21.89%)</b></td><td>202.40 (-12.31%)</td><td>134.30 (-17.58%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.40 (n/a)</td><td>423.20 (n/a)</td><td>447.30 (n/a)</td><td>230.80 (n/a)</td><td>162.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 <b>(+47.44%)</b></td><td>0.03 <b>(+27.60%)</b></td><td>0.03 (+16.09%)</td><td>0.02 (+8.80%)</td><td>0.01 <b>(+48.91%)</b></td><td>493.80 (-8.10%)</td><td>304.36 (-19.75%)</td><td>268.90 (-13.87%)</td><td>179.50 <b>(-32.19%)</b></td><td>116.36 (-6.92%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.30 (n/a)</td><td>379.28 (n/a)</td><td>312.20 (n/a)</td><td>264.70 (n/a)</td><td>125.02 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 <b>(+26.14%)</b></td><td>0.03 (+10.32%)</td><td>0.03 (-1.07%)</td><td>0.02 (-14.96%)</td><td>0.01 <b>(+42.18%)</b></td><td>511.10 (+17.60%)</td><td>316.36 (-5.69%)</td><td>295.30 (+1.10%)</td><td>201.60 <b>(-20.75%)</b></td><td>115.83 <b>(+34.80%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>434.60 (n/a)</td><td>335.44 (n/a)</td><td>292.10 (n/a)</td><td>254.40 (n/a)</td><td>85.93 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (+17.58%)</td><td>0.02 (+6.63%)</td><td>0.02 (+0.78%)</td><td>0.01 <b>(-43.47%)</b></td><td>0.01 <b>(+38.79%)</b></td><td>1084.10 <b>(+76.88%)</b></td><td>510.84 (+14.70%)</td><td>522.70 (-0.78%)</td><td>203.70 (-14.91%)</td><td>357.03 <b>(+92.14%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.90 (n/a)</td><td>445.38 (n/a)</td><td>526.80 (n/a)</td><td>239.40 (n/a)</td><td>185.81 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (+15.84%)</td><td>0.02 <b>(+22.65%)</b></td><td>0.03 <b>(+67.72%)</b></td><td>0.01 (-17.37%)</td><td>0.01 <b>(+66.81%)</b></td><td>697.30 <b>(+21.02%)</b></td><td>398.44 (-7.43%)</td><td>268.40 <b>(-40.38%)</b></td><td>227.10 (-13.68%)</td><td>208.34 <b>(+82.48%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.20 (n/a)</td><td>430.40 (n/a)</td><td>450.20 (n/a)</td><td>263.10 (n/a)</td><td>114.17 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (-11.59%)</td><td>0.02 (+8.56%)</td><td>0.02 (+12.49%)</td><td>0.01 <b>(+31.28%)</b></td><td>0.01 (-19.19%)</td><td>613.50 <b>(-23.83%)</b></td><td>443.60 (-13.16%)</td><td>469.60 (-11.09%)</td><td>245.90 (+13.11%)</td><td>161.71 <b>(-23.59%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>805.40 (n/a)</td><td>510.84 (n/a)</td><td>528.20 (n/a)</td><td>217.40 (n/a)</td><td>211.62 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 <b>(+25.79%)</b></td><td>0.03 <b>(+30.28%)</b></td><td>0.03 <b>(+86.00%)</b></td><td>0.01 (-15.13%)</td><td>0.01 <b>(+49.79%)</b></td><td>611.50 (+17.82%)</td><td>353.80 (-16.57%)</td><td>263.80 <b>(-46.24%)</b></td><td>193.40 <b>(-20.48%)</b></td><td>171.72 <b>(+40.19%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.00 (n/a)</td><td>424.08 (n/a)</td><td>490.70 (n/a)</td><td>243.20 (n/a)</td><td>122.49 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (+3.58%)</td><td>0.02 (+0.47%)</td><td>0.02 <b>(-28.21%)</b></td><td>0.02 <b>(+307.55%)</b></td><td>0.01 <b>(-44.61%)</b></td><td>541.80 <b>(-75.46%)</b></td><td>450.36 <b>(-39.65%)</b></td><td>463.10 <b>(+39.28%)</b></td><td>285.80 (-3.45%)</td><td>101.49 <b>(-87.69%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2208.10 (n/a)</td><td>746.28 (n/a)</td><td>332.50 (n/a)</td><td>296.00 (n/a)</td><td>824.24 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (-1.34%)</td><td>0.03 (-7.52%)</td><td>0.03 (-9.42%)</td><td>0.02 (+13.05%)</td><td>0.01 (-2.65%)</td><td>522.00 (-11.54%)</td><td>340.00 (+5.85%)</td><td>268.90 (+10.39%)</td><td>240.80 (+1.35%)</td><td>127.22 (-16.46%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.10 (n/a)</td><td>321.20 (n/a)</td><td>243.60 (n/a)</td><td>237.60 (n/a)</td><td>152.28 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (-0.87%)</td><td>0.03 (+16.80%)</td><td>0.03 (+3.76%)</td><td>0.02 <b>(+21.15%)</b></td><td>0.01 <b>(-27.51%)</b></td><td>422.40 (-17.47%)</td><td>283.56 (-19.82%)</td><td>259.00 (-3.65%)</td><td>228.20 (+0.88%)</td><td>80.03 <b>(-42.02%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.80 (n/a)</td><td>353.66 (n/a)</td><td>268.80 (n/a)</td><td>226.20 (n/a)</td><td>138.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (+12.83%)</td><td>0.02 (-13.96%)</td><td>0.03 (-19.66%)</td><td>0.01 <b>(-58.68%)</b></td><td>0.01 <b>(+35.65%)</b></td><td>1077.10 <b>(+142.04%)</b></td><td>464.60 <b>(+46.36%)</b></td><td>295.30 <b>(+24.49%)</b></td><td>202.90 (-11.36%)</td><td>355.87 <b>(+207.32%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>445.00 (n/a)</td><td>317.44 (n/a)</td><td>237.20 (n/a)</td><td>228.90 (n/a)</td><td>115.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (-1.37%)</td><td>0.02 <b>(-26.67%)</b></td><td>0.01 <b>(-29.58%)</b></td><td>0.00 <b>(-67.77%)</b></td><td>0.01 <b>(+39.22%)</b></td><td>1893.10 <b>(+210.29%)</b></td><td>834.60 <b>(+97.16%)</b></td><td>582.80 <b>(+42.01%)</b></td><td>233.70 (+1.39%)</td><td>651.35 <b>(+357.89%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.10 (n/a)</td><td>423.32 (n/a)</td><td>410.40 (n/a)</td><td>230.50 (n/a)</td><td>142.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 <b>(-44.50%)</b></td><td>0.02 (-15.55%)</td><td>0.02 (+9.17%)</td><td>0.01 (+1.54%)</td><td>0.00 <b>(-63.32%)</b></td><td>626.30 (-1.51%)</td><td>495.60 (+6.07%)</td><td>433.00 (-8.42%)</td><td>373.40 <b>(+80.21%)</b></td><td>120.19 <b>(-27.15%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>635.90 (n/a)</td><td>467.22 (n/a)</td><td>472.80 (n/a)</td><td>207.20 (n/a)</td><td>164.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (-8.98%)</td><td>0.02 (+7.48%)</td><td>0.03 <b>(+50.31%)</b></td><td>0.01 (-5.35%)</td><td>0.01 (-1.51%)</td><td>579.50 (+5.65%)</td><td>384.60 (-4.68%)</td><td>290.20 <b>(-33.49%)</b></td><td>240.80 (+9.85%)</td><td>154.96 <b>(+25.26%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.50 (n/a)</td><td>403.50 (n/a)</td><td>436.30 (n/a)</td><td>219.20 (n/a)</td><td>123.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (-6.41%)</td><td>0.03 (-7.96%)</td><td>0.03 (-0.09%)</td><td>0.02 <b>(-40.52%)</b></td><td>0.01 <b>(+122.05%)</b></td><td>492.50 <b>(+68.15%)</b></td><td>308.50 (+15.02%)</td><td>268.80 (+0.11%)</td><td>251.40 (+6.84%)</td><td>103.16 <b>(+306.71%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>292.90 (n/a)</td><td>268.22 (n/a)</td><td>268.50 (n/a)</td><td>235.30 (n/a)</td><td>25.36 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.06 <b>(+37.23%)</b></td><td>0.04 (+13.47%)</td><td>0.03 (-17.44%)</td><td>0.02 (+4.27%)</td><td>0.02 <b>(+72.57%)</b></td><td>531.90 (-4.09%)</td><td>395.74 (-5.95%)</td><td>472.40 <b>(+21.13%)</b></td><td>218.60 <b>(-27.13%)</b></td><td>143.99 (+18.80%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>554.60 (n/a)</td><td>420.78 (n/a)</td><td>390.00 (n/a)</td><td>300.00 (n/a)</td><td>121.20 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (+13.09%)</td><td>0.03 (-11.96%)</td><td>0.02 <b>(-30.41%)</b></td><td>0.02 (-18.41%)</td><td>0.01 <b>(+63.39%)</b></td><td>543.20 <b>(+22.56%)</b></td><td>365.48 <b>(+21.44%)</b></td><td>390.80 <b>(+43.68%)</b></td><td>217.00 (-11.61%)</td><td>131.32 <b>(+63.24%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>443.20 (n/a)</td><td>300.96 (n/a)</td><td>272.00 (n/a)</td><td>245.50 (n/a)</td><td>80.45 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 (+16.84%)</td><td>0.03 (+13.44%)</td><td>0.02 (+12.47%)</td><td>0.02 (+12.45%)</td><td>0.01 (+15.88%)</td><td>512.00 (-11.06%)</td><td>381.24 (-11.49%)</td><td>450.70 (-11.09%)</td><td>226.10 (-14.42%)</td><td>133.42 (-10.31%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.70 (n/a)</td><td>430.74 (n/a)</td><td>506.90 (n/a)</td><td>264.20 (n/a)</td><td>148.77 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (+17.54%)</td><td>0.03 <b>(+23.24%)</b></td><td>0.03 <b>(+50.13%)</b></td><td>0.01 (-10.67%)</td><td>0.01 (+6.24%)</td><td>626.80 (+11.95%)</td><td>332.20 (-17.70%)</td><td>270.20 <b>(-33.40%)</b></td><td>200.40 (-14.94%)</td><td>168.35 (+8.85%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.90 (n/a)</td><td>403.64 (n/a)</td><td>405.70 (n/a)</td><td>235.60 (n/a)</td><td>154.67 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.06 <b>(+63.77%)</b></td><td>0.03 (-0.35%)</td><td>0.03 (-6.53%)</td><td>0.00 <b>(-81.84%)</b></td><td>0.02 <b>(+326.79%)</b></td><td>2053.00 <b>(+450.55%)</b></td><td>636.96 <b>(+102.84%)</b></td><td>304.60 (+6.99%)</td><td>167.20 <b>(-38.93%)</b></td><td>796.31 <b>(+1552.39%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>372.90 (n/a)</td><td>314.02 (n/a)</td><td>284.70 (n/a)</td><td>273.80 (n/a)</td><td>48.19 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (+8.53%)</td><td>0.03 <b>(+23.61%)</b></td><td>0.03 <b>(+54.93%)</b></td><td>0.01 (-6.42%)</td><td>0.01 (+13.71%)</td><td>604.40 (+6.86%)</td><td>325.14 (-16.31%)</td><td>276.10 <b>(-35.46%)</b></td><td>228.10 (-7.84%)</td><td>158.39 <b>(+21.29%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.60 (n/a)</td><td>388.52 (n/a)</td><td>427.80 (n/a)</td><td>247.50 (n/a)</td><td>130.59 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (+9.19%)</td><td>0.02 <b>(-22.44%)</b></td><td>0.02 <b>(-49.72%)</b></td><td>0.01 (-1.60%)</td><td>0.01 (+4.74%)</td><td>661.10 (+1.61%)</td><td>494.54 <b>(+28.79%)</b></td><td>549.40 <b>(+98.91%)</b></td><td>239.50 (-8.41%)</td><td>162.63 (-4.19%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.60 (n/a)</td><td>384.00 (n/a)</td><td>276.20 (n/a)</td><td>261.50 (n/a)</td><td>169.73 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (-1.37%)</td><td>0.02 (+15.13%)</td><td>0.02 <b>(+21.02%)</b></td><td>0.01 <b>(+20.72%)</b></td><td>0.01 (-13.49%)</td><td>651.20 (-17.16%)</td><td>408.58 (-17.06%)</td><td>391.20 (-17.36%)</td><td>239.00 (+1.40%)</td><td>152.89 <b>(-23.29%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>786.10 (n/a)</td><td>492.62 (n/a)</td><td>473.40 (n/a)</td><td>235.70 (n/a)</td><td>199.31 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (-15.52%)</td><td>0.02 <b>(-22.94%)</b></td><td>0.02 <b>(-32.85%)</b></td><td>0.02 <b>(-28.08%)</b></td><td>0.01 (-8.18%)</td><td>591.60 <b>(+39.04%)</b></td><td>436.22 <b>(+31.76%)</b></td><td>433.20 <b>(+48.92%)</b></td><td>286.10 (+18.37%)</td><td>123.63 <b>(+43.08%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>425.50 (n/a)</td><td>331.08 (n/a)</td><td>290.90 (n/a)</td><td>241.70 (n/a)</td><td>86.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (-0.80%)</td><td>0.02 (+14.58%)</td><td>0.02 <b>(+25.63%)</b></td><td>0.02 <b>(+170.13%)</b></td><td>0.00 <b>(-53.52%)</b></td><td>476.30 <b>(-62.98%)</b></td><td>394.58 <b>(-32.45%)</b></td><td>375.30 <b>(-20.40%)</b></td><td>294.40 (+0.79%)</td><td>73.06 <b>(-82.16%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1286.60 (n/a)</td><td>584.14 (n/a)</td><td>471.50 (n/a)</td><td>292.10 (n/a)</td><td>409.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.33 (-5.08%)</td><td>0.23 (-0.19%)</td><td>0.21 (-5.72%)</td><td>0.18 (+15.27%)</td><td>0.06 <b>(-28.71%)</b></td><td>559.30 (-13.25%)</td><td>440.66 (-5.58%)</td><td>467.60 (+6.06%)</td><td>293.50 (+5.35%)</td><td>98.80 <b>(-39.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.35 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>644.70 (n/a)</td><td>466.70 (n/a)</td><td>440.90 (n/a)</td><td>278.60 (n/a)</td><td>164.44 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.42 (+8.72%)</td><td>0.25 (-13.79%)</td><td>0.22 <b>(-38.47%)</b></td><td>0.19 (+10.64%)</td><td>0.09 (-9.38%)</td><td>514.40 (-9.61%)</td><td>421.32 (+11.08%)</td><td>451.10 <b>(+62.50%)</b></td><td>234.50 (-8.04%)</td><td>107.87 <b>(-29.97%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.35 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>569.10 (n/a)</td><td>379.28 (n/a)</td><td>277.60 (n/a)</td><td>255.00 (n/a)</td><td>154.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.39 (+17.42%)</td><td>0.25 (+1.92%)</td><td>0.23 (-2.15%)</td><td>0.17 (-7.44%)</td><td>0.09 <b>(+48.22%)</b></td><td>589.80 (+8.04%)</td><td>430.22 (+1.86%)</td><td>430.10 (+2.21%)</td><td>249.80 (-14.83%)</td><td>122.67 <b>(+31.78%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>545.90 (n/a)</td><td>422.38 (n/a)</td><td>420.80 (n/a)</td><td>293.30 (n/a)</td><td>93.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.27 (+1.48%)</td><td>0.17 (-13.65%)</td><td>0.14 <b>(-31.22%)</b></td><td>0.14 (+15.24%)</td><td>0.05 (-12.41%)</td><td>540.90 (-13.23%)</td><td>455.42 (+12.52%)</td><td>511.20 <b>(+45.35%)</b></td><td>277.40 (-1.46%)</td><td>111.26 <b>(-23.32%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>623.40 (n/a)</td><td>404.74 (n/a)</td><td>351.70 (n/a)</td><td>281.50 (n/a)</td><td>145.10 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.27 (-10.81%)</td><td>0.17 (-18.24%)</td><td>0.16 <b>(-34.88%)</b></td><td>0.10 (+17.57%)</td><td>0.06 <b>(-32.81%)</b></td><td>709.20 (-14.94%)</td><td>467.30 (+9.01%)</td><td>463.10 <b>(+53.55%)</b></td><td>274.00 (+12.11%)</td><td>157.83 <b>(-36.21%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>833.80 (n/a)</td><td>428.66 (n/a)</td><td>301.60 (n/a)</td><td>244.40 (n/a)</td><td>247.40 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.30 (-1.73%)</td><td>0.21 (+5.08%)</td><td>0.21 <b>(+30.97%)</b></td><td>0.12 (-1.15%)</td><td>0.08 (+9.80%)</td><td>598.20 (+1.15%)</td><td>409.36 (-1.59%)</td><td>354.70 <b>(-23.65%)</b></td><td>243.00 (+1.76%)</td><td>169.50 <b>(+20.97%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>591.40 (n/a)</td><td>415.98 (n/a)</td><td>464.60 (n/a)</td><td>238.80 (n/a)</td><td>140.12 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.48 <b>(+22.87%)</b></td><td>0.31 <b>(+24.02%)</b></td><td>0.28 (+19.22%)</td><td>0.17 <b>(+40.93%)</b></td><td>0.14 <b>(+37.40%)</b></td><td>782.20 <b>(-29.05%)</b></td><td>493.20 (-18.59%)</td><td>465.20 (-16.12%)</td><td>271.70 (-18.60%)</td><td>220.29 <b>(-25.81%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.39 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>1102.40 (n/a)</td><td>605.84 (n/a)</td><td>554.60 (n/a)</td><td>333.80 (n/a)</td><td>296.91 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.57 <b>(+46.09%)</b></td><td>0.38 <b>(+50.65%)</b></td><td>0.44 <b>(+72.69%)</b></td><td>0.19 <b>(+88.28%)</b></td><td>0.17 <b>(+61.96%)</b></td><td>694.90 <b>(-46.89%)</b></td><td>416.64 <b>(-34.23%)</b></td><td>295.60 <b>(-42.10%)</b></td><td>228.70 <b>(-31.55%)</b></td><td>212.69 <b>(-44.88%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.39 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>1308.40 (n/a)</td><td>633.50 (n/a)</td><td>510.50 (n/a)</td><td>334.10 (n/a)</td><td>385.89 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.52 (-3.83%)</td><td>0.30 (-10.30%)</td><td>0.26 (-12.32%)</td><td>0.23 (-11.44%)</td><td>0.12 (+4.71%)</td><td>569.40 (+12.91%)</td><td>476.32 (+13.55%)</td><td>506.90 (+14.06%)</td><td>253.10 (+3.99%)</td><td>128.54 (+19.95%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.54 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>504.30 (n/a)</td><td>419.48 (n/a)</td><td>444.40 (n/a)</td><td>243.40 (n/a)</td><td>107.16 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.00 <b>(+40.00%)</b></td><td>0.00 <b>(+28.57%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+59.04%)</b></td><td>24241.21 (+8.47%)</td><td>15120.02 (-13.58%)</td><td>16192.69 (-14.87%)</td><td>6113.36 <b>(-24.51%)</b></td><td>7296.29 <b>(+24.44%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22348.53 (n/a)</td><td>17495.56 (n/a)</td><td>19021.22 (n/a)</td><td>8097.78 (n/a)</td><td>5863.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.00 (+18.18%)</td><td>0.00 <b>(+46.43%)</b></td><td>0.00 <b>(+75.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+34.00%)</b></td><td>18560.02 (-15.72%)</td><td>12039.50 <b>(-30.46%)</b></td><td>11797.07 <b>(-39.09%)</b></td><td>6365.53 (-17.82%)</td><td>5452.57 (-2.33%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22022.94 (n/a)</td><td>17313.57 (n/a)</td><td>19368.61 (n/a)</td><td>7745.44 (n/a)</td><td>5582.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.14 (-9.73%)</td><td>0.12 (+18.47%)</td><td>0.13 <b>(+54.37%)</b></td><td>0.07 (-13.28%)</td><td>0.03 (-5.48%)</td><td>30016.64 (+15.35%)</td><td>19180.16 (-14.80%)</td><td>15810.96 <b>(-35.22%)</b></td><td>15492.53 (+10.79%)</td><td>6204.13 <b>(+24.93%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>26022.77 (n/a)</td><td>22512.56 (n/a)</td><td>24405.59 (n/a)</td><td>13984.24 (n/a)</td><td>4966.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>1.54 (-4.03%)</td><td>1.41 <b>(+36.23%)</b></td><td>1.48 <b>(+43.41%)</b></td><td>1.07 <b>(+57.17%)</b></td><td>0.19 <b>(-47.63%)</b></td><td>489.70 <b>(-36.37%)</b></td><td>379.94 <b>(-31.88%)</b></td><td>354.60 <b>(-30.27%)</b></td><td>341.30 (+4.18%)</td><td>62.23 <b>(-65.45%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>1.60 (n/a)</td><td>1.03 (n/a)</td><td>1.03 (n/a)</td><td>0.68 (n/a)</td><td>0.37 (n/a)</td><td>769.60 (n/a)</td><td>557.78 (n/a)</td><td>508.50 (n/a)</td><td>327.60 (n/a)</td><td>180.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>2.38 (-6.78%)</td><td>1.78 <b>(+22.97%)</b></td><td>1.62 (+15.69%)</td><td>1.26 <b>(+299.05%)</b></td><td>0.53 <b>(-33.09%)</b></td><td>833.00 <b>(-74.94%)</b></td><td>632.72 <b>(-46.46%)</b></td><td>648.20 (-13.56%)</td><td>440.80 (+7.28%)</td><td>182.33 <b>(-84.88%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>2.55 (n/a)</td><td>1.45 (n/a)</td><td>1.40 (n/a)</td><td>0.32 (n/a)</td><td>0.80 (n/a)</td><td>3324.20 (n/a)</td><td>1181.76 (n/a)</td><td>749.90 (n/a)</td><td>410.90 (n/a)</td><td>1206.24 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>1.66 (+1.86%)</td><td>1.29 <b>(+24.93%)</b></td><td>1.39 <b>(+38.03%)</b></td><td>0.87 <b>(+42.56%)</b></td><td>0.39 (+5.09%)</td><td>601.20 <b>(-29.85%)</b></td><td>439.92 <b>(-21.24%)</b></td><td>376.10 <b>(-27.55%)</b></td><td>316.60 (-1.83%)</td><td>142.89 <b>(-25.94%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:06:45</td><td>1.63 (n/a)</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>0.61 (n/a)</td><td>0.37 (n/a)</td><td>857.00 (n/a)</td><td>558.58 (n/a)</td><td>519.10 (n/a)</td><td>322.50 (n/a)</td><td>192.93 (n/a)</td>
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
