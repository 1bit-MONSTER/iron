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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (-5.45%)</td><td>0.03 (-8.14%)</td><td>0.03 (-18.29%)</td><td>0.02 (-5.23%)</td><td>0.01 (-13.30%)</td><td>548.80 (+5.52%)</td><td>391.78 (+7.89%)</td><td>367.30 <b>(+22.39%)</b></td><td>298.50 (+5.78%)</td><td>102.19 (-2.15%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.10 (n/a)</td><td>363.14 (n/a)</td><td>300.10 (n/a)</td><td>282.20 (n/a)</td><td>104.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.06 (+17.93%)</td><td>0.03 <b>(-30.86%)</b></td><td>0.03 <b>(-49.14%)</b></td><td>0.02 <b>(-23.46%)</b></td><td>0.02 <b>(+51.65%)</b></td><td>630.00 <b>(+30.65%)</b></td><td>459.98 <b>(+58.06%)</b></td><td>464.90 <b>(+96.58%)</b></td><td>196.10 (-15.22%)</td><td>164.32 <b>(+52.27%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>482.20 (n/a)</td><td>291.02 (n/a)</td><td>236.50 (n/a)</td><td>231.30 (n/a)</td><td>107.91 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 <b>(-32.41%)</b></td><td>0.03 (-14.26%)</td><td>0.03 (-11.97%)</td><td>0.02 (+5.36%)</td><td>0.01 <b>(-57.38%)</b></td><td>513.90 (-5.08%)</td><td>378.54 (+5.85%)</td><td>358.20 (+13.61%)</td><td>304.40 <b>(+47.91%)</b></td><td>84.28 <b>(-41.54%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>541.40 (n/a)</td><td>357.62 (n/a)</td><td>315.30 (n/a)</td><td>205.80 (n/a)</td><td>144.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (+3.68%)</td><td>0.02 (+9.64%)</td><td>0.02 <b>(+30.39%)</b></td><td>0.00 <b>(-71.36%)</b></td><td>0.01 <b>(+36.47%)</b></td><td>1914.50 <b>(+249.11%)</b></td><td>633.92 <b>(+52.97%)</b></td><td>327.10 <b>(-23.32%)</b></td><td>184.80 (-3.55%)</td><td>726.07 <b>(+437.55%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.40 (n/a)</td><td>414.42 (n/a)</td><td>426.60 (n/a)</td><td>191.60 (n/a)</td><td>135.07 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (+0.07%)</td><td>0.02 (+4.18%)</td><td>0.01 (+16.38%)</td><td>0.01 (+9.97%)</td><td>0.01 (-10.46%)</td><td>487.80 (-9.06%)</td><td>363.60 (-7.38%)</td><td>409.30 (-14.07%)</td><td>227.30 (-0.04%)</td><td>122.90 (-17.75%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>536.40 (n/a)</td><td>392.56 (n/a)</td><td>476.30 (n/a)</td><td>227.40 (n/a)</td><td>149.43 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (+2.55%)</td><td>0.02 (+3.81%)</td><td>0.01 (+18.54%)</td><td>0.01 (+9.46%)</td><td>0.00 (-18.12%)</td><td>461.00 (-8.64%)</td><td>351.52 (-8.01%)</td><td>362.90 (-15.64%)</td><td>220.50 (-2.52%)</td><td>90.99 <b>(-29.82%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>504.60 (n/a)</td><td>382.14 (n/a)</td><td>430.20 (n/a)</td><td>226.20 (n/a)</td><td>129.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (-0.41%)</td><td>0.01 <b>(-27.76%)</b></td><td>0.01 <b>(-31.36%)</b></td><td>0.00 <b>(-80.97%)</b></td><td>0.01 <b>(+135.75%)</b></td><td>1921.30 <b>(+425.38%)</b></td><td>690.38 <b>(+132.89%)</b></td><td>439.50 <b>(+45.67%)</b></td><td>225.10 (+0.40%)</td><td>702.52 <b>(+1223.74%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>365.70 (n/a)</td><td>296.44 (n/a)</td><td>301.70 (n/a)</td><td>224.20 (n/a)</td><td>53.07 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 <b>(+27.41%)</b></td><td>0.02 <b>(+31.75%)</b></td><td>0.01 <b>(+41.76%)</b></td><td>0.01 <b>(+239.37%)</b></td><td>0.01 (-8.78%)</td><td>546.50 <b>(-70.53%)</b></td><td>367.54 <b>(-47.65%)</b></td><td>375.70 <b>(-29.46%)</b></td><td>191.00 <b>(-21.50%)</b></td><td>127.04 <b>(-80.77%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1854.70 (n/a)</td><td>702.10 (n/a)</td><td>532.60 (n/a)</td><td>243.30 (n/a)</td><td>660.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 <b>(+77.89%)</b></td><td>0.02 <b>(+46.10%)</b></td><td>0.01 <b>(+34.98%)</b></td><td>0.01 <b>(+60.26%)</b></td><td>0.01 <b>(+84.55%)</b></td><td>543.50 <b>(-37.60%)</b></td><td>384.70 <b>(-30.42%)</b></td><td>362.80 <b>(-25.91%)</b></td><td>209.90 <b>(-43.80%)</b></td><td>132.24 <b>(-34.84%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>871.00 (n/a)</td><td>552.90 (n/a)</td><td>489.70 (n/a)</td><td>373.50 (n/a)</td><td>202.95 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>450.90 (n/a)</td><td>361.68 (n/a)</td><td>398.00 (n/a)</td><td>224.40 (n/a)</td><td>101.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>481.50 (n/a)</td><td>350.12 (n/a)</td><td>328.60 (n/a)</td><td>260.00 (n/a)</td><td>96.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.10 (n/a)</td><td>452.16 (n/a)</td><td>461.90 (n/a)</td><td>326.10 (n/a)</td><td>75.33 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>638.90 (n/a)</td><td>513.56 (n/a)</td><td>568.40 (n/a)</td><td>311.90 (n/a)</td><td>133.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1044.50 (n/a)</td><td>506.30 (n/a)</td><td>459.60 (n/a)</td><td>238.50 (n/a)</td><td>328.75 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>547.20 (n/a)</td><td>418.20 (n/a)</td><td>467.50 (n/a)</td><td>247.50 (n/a)</td><td>116.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.40 (n/a)</td><td>389.94 (n/a)</td><td>404.70 (n/a)</td><td>297.40 (n/a)</td><td>97.07 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.70 (n/a)</td><td>457.08 (n/a)</td><td>469.50 (n/a)</td><td>345.00 (n/a)</td><td>92.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>446.80 (n/a)</td><td>325.70 (n/a)</td><td>314.90 (n/a)</td><td>221.70 (n/a)</td><td>96.26 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>994.20 (n/a)</td><td>623.92 (n/a)</td><td>614.50 (n/a)</td><td>328.70 (n/a)</td><td>245.89 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.50 (n/a)</td><td>382.12 (n/a)</td><td>290.00 (n/a)</td><td>273.70 (n/a)</td><td>137.47 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.60 (n/a)</td><td>454.44 (n/a)</td><td>424.20 (n/a)</td><td>345.30 (n/a)</td><td>108.40 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.50 <b>(-27.60%)</b></td><td>0.38 (-16.71%)</td><td>0.44 (+19.74%)</td><td>0.13 <b>(-62.38%)</b></td><td>0.15 (-2.28%)</td><td>1735.90 <b>(+165.83%)</b></td><td>753.42 <b>(+43.54%)</b></td><td>498.30 (-16.48%)</td><td>439.20 <b>(+38.11%)</b></td><td>552.26 <b>(+283.41%)</b></td><td>21.49 <b>(-27.60%)</b></td><td>16.14 (-16.71%)</td><td>18.94 (+19.74%)</td><td>5.44 <b>(-62.38%)</b></td><td>6.32 (-2.28%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.70 (n/a)</td><td>0.45 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.15 (n/a)</td><td>653.00 (n/a)</td><td>524.90 (n/a)</td><td>596.60 (n/a)</td><td>318.00 (n/a)</td><td>144.04 (n/a)</td><td>29.68 (n/a)</td><td>19.38 (n/a)</td><td>15.82 (n/a)</td><td>14.45 (n/a)</td><td>6.47 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.51 (+16.35%)</td><td>0.41 <b>(+38.51%)</b></td><td>0.44 <b>(+27.23%)</b></td><td>0.29 <b>(+214.48%)</b></td><td>0.10 <b>(-26.71%)</b></td><td>752.90 <b>(-68.20%)</b></td><td>560.30 <b>(-43.81%)</b></td><td>497.40 <b>(-21.40%)</b></td><td>431.30 (-14.05%)</td><td>141.81 <b>(-81.75%)</b></td><td>21.88 (+16.35%)</td><td>17.67 <b>(+38.51%)</b></td><td>18.97 <b>(+27.23%)</b></td><td>12.53 <b>(+214.48%)</b></td><td>4.13 <b>(-26.71%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>0.13 (n/a)</td><td>2367.70 (n/a)</td><td>997.10 (n/a)</td><td>632.80 (n/a)</td><td>501.80 (n/a)</td><td>776.90 (n/a)</td><td>18.81 (n/a)</td><td>12.76 (n/a)</td><td>14.91 (n/a)</td><td>3.99 (n/a)</td><td>5.63 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.31 (-1.08%)</td><td>0.31 (+0.76%)</td><td>0.30 (-0.16%)</td><td>0.30 (+4.37%)</td><td>0.00 <b>(-63.24%)</b></td><td>83218.80 (-4.19%)</td><td>82414.68 (-0.81%)</td><td>82635.90 (+0.16%)</td><td>81333.30 (+1.09%)</td><td>845.99 <b>(-64.52%)</b></td><td>211.23 (-1.08%)</td><td>208.47 (+0.76%)</td><td>207.90 (-0.16%)</td><td>206.44 (+4.37%)</td><td>2.15 <b>(-63.25%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>86854.60 (n/a)</td><td>83088.32 (n/a)</td><td>82506.20 (n/a)</td><td>80455.40 (n/a)</td><td>2384.65 (n/a)</td><td>213.53 (n/a)</td><td>206.90 (n/a)</td><td>208.23 (n/a)</td><td>197.80 (n/a)</td><td>5.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>1.04 (+1.44%)</td><td>1.01 (+2.49%)</td><td>1.01 (+0.43%)</td><td>0.99 (+6.26%)</td><td>0.02 <b>(-56.48%)</b></td><td>25440.40 (-5.89%)</td><td>24916.20 (-2.54%)</td><td>24846.90 (-0.43%)</td><td>24292.50 (-1.42%)</td><td>431.16 <b>(-59.58%)</b></td><td>707.21 (+1.44%)</td><td>689.67 (+2.49%)</td><td>691.43 (+0.43%)</td><td>675.30 (+6.26%)</td><td>11.99 <b>(-56.48%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>1.02 (n/a)</td><td>0.99 (n/a)</td><td>1.01 (n/a)</td><td>0.93 (n/a)</td><td>0.04 (n/a)</td><td>27032.40 (n/a)</td><td>25565.84 (n/a)</td><td>24953.90 (n/a)</td><td>24643.50 (n/a)</td><td>1066.75 (n/a)</td><td>697.14 (n/a)</td><td>672.90 (n/a)</td><td>688.46 (n/a)</td><td>635.53 (n/a)</td><td>27.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>3.45 (+2.35%)</td><td>2.74 (+2.42%)</td><td>2.68 (-3.16%)</td><td>1.95 (+3.27%)</td><td>0.66 (-1.34%)</td><td>4129.30 (-3.16%)</td><td>3086.20 (-2.88%)</td><td>3008.10 (+3.26%)</td><td>2338.80 (-2.29%)</td><td>768.75 (-8.60%)</td><td>903.85 (+2.35%)</td><td>719.16 (+2.42%)</td><td>702.76 (-3.16%)</td><td>511.94 (+3.27%)</td><td>173.49 (-1.34%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>3.37 (n/a)</td><td>2.68 (n/a)</td><td>2.77 (n/a)</td><td>1.89 (n/a)</td><td>0.67 (n/a)</td><td>4264.20 (n/a)</td><td>3177.78 (n/a)</td><td>2913.00 (n/a)</td><td>2393.70 (n/a)</td><td>841.13 (n/a)</td><td>883.10 (n/a)</td><td>702.16 (n/a)</td><td>725.70 (n/a)</td><td>495.74 (n/a)</td><td>175.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.31 <b>(+60.11%)</b></td><td>0.20 (+14.72%)</td><td>0.20 (+6.19%)</td><td>0.13 (-9.63%)</td><td>0.06 <b>(+242.62%)</b></td><td>9429.70 (+10.66%)</td><td>6531.54 (-7.23%)</td><td>6334.90 (-5.83%)</td><td>4050.00 <b>(-37.54%)</b></td><td>1923.07 <b>(+128.81%)</b></td><td>16.57 <b>(+60.11%)</b></td><td>11.05 (+14.72%)</td><td>10.59 (+6.19%)</td><td>7.12 (-9.63%)</td><td>3.44 <b>(+242.62%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>8521.70 (n/a)</td><td>7040.34 (n/a)</td><td>6727.30 (n/a)</td><td>6484.40 (n/a)</td><td>840.47 (n/a)</td><td>10.35 (n/a)</td><td>9.63 (n/a)</td><td>9.98 (n/a)</td><td>7.88 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>3.80 (n/a)</td><td>3.68 (n/a)</td><td>3.73 (n/a)</td><td>3.45 (n/a)</td><td>0.14 (n/a)</td><td>3.80 (n/a)</td><td>3.68 (n/a)</td><td>3.73 (n/a)</td><td>3.44 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>7.59 (+2.39%)</td><td>7.12 (+1.77%)</td><td>7.06 (-1.18%)</td><td>6.62 (+6.58%)</td><td>0.40 (-18.27%)</td><td>7.58 (+2.39%)</td><td>7.11 (+1.77%)</td><td>7.06 (-1.18%)</td><td>6.61 (+6.58%)</td><td>0.40 (-18.27%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>7.41 (n/a)</td><td>6.99 (n/a)</td><td>7.15 (n/a)</td><td>6.21 (n/a)</td><td>0.49 (n/a)</td><td>7.41 (n/a)</td><td>6.99 (n/a)</td><td>7.14 (n/a)</td><td>6.21 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>9.86 <b>(-25.02%)</b></td><td>8.75 (-8.28%)</td><td>8.54 (-2.36%)</td><td>7.70 (+4.81%)</td><td>0.88 <b>(-60.35%)</b></td><td>9.85 <b>(-25.02%)</b></td><td>8.74 (-8.28%)</td><td>8.54 (-2.36%)</td><td>7.69 (+4.81%)</td><td>0.88 <b>(-60.35%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>13.15 (n/a)</td><td>9.54 (n/a)</td><td>8.75 (n/a)</td><td>7.34 (n/a)</td><td>2.21 (n/a)</td><td>13.14 (n/a)</td><td>9.53 (n/a)</td><td>8.74 (n/a)</td><td>7.34 (n/a)</td><td>2.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>3.90 (n/a)</td><td>3.66 (n/a)</td><td>3.68 (n/a)</td><td>3.41 (n/a)</td><td>0.21 (n/a)</td><td>3.89 (n/a)</td><td>3.66 (n/a)</td><td>3.67 (n/a)</td><td>3.41 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>7.56 (+5.68%)</td><td>6.85 (+14.30%)</td><td>6.95 <b>(+20.75%)</b></td><td>5.72 (+6.49%)</td><td>0.72 (+3.26%)</td><td>7.56 (+5.68%)</td><td>6.85 (+14.30%)</td><td>6.95 <b>(+20.75%)</b></td><td>5.72 (+6.49%)</td><td>0.72 (+3.26%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>7.16 (n/a)</td><td>5.99 (n/a)</td><td>5.76 (n/a)</td><td>5.37 (n/a)</td><td>0.69 (n/a)</td><td>7.15 (n/a)</td><td>5.99 (n/a)</td><td>5.75 (n/a)</td><td>5.37 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>14.02 <b>(+42.99%)</b></td><td>10.86 <b>(+28.39%)</b></td><td>9.64 (+18.54%)</td><td>7.65 (-1.04%)</td><td>2.75 <b>(+241.49%)</b></td><td>14.01 <b>(+42.99%)</b></td><td>10.85 <b>(+28.39%)</b></td><td>9.63 (+18.54%)</td><td>7.65 (-1.04%)</td><td>2.75 <b>(+241.49%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>9.80 (n/a)</td><td>8.46 (n/a)</td><td>8.13 (n/a)</td><td>7.73 (n/a)</td><td>0.80 (n/a)</td><td>9.80 (n/a)</td><td>8.45 (n/a)</td><td>8.12 (n/a)</td><td>7.73 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>2.84 (-7.06%)</td><td>1.97 (+3.41%)</td><td>1.94 (-2.37%)</td><td>1.27 (+8.45%)</td><td>0.57 <b>(-26.48%)</b></td><td>2.83 (-7.06%)</td><td>1.96 (+3.41%)</td><td>1.94 (-2.37%)</td><td>1.27 (+8.45%)</td><td>0.57 <b>(-26.48%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>3.05 (n/a)</td><td>1.90 (n/a)</td><td>1.99 (n/a)</td><td>1.17 (n/a)</td><td>0.78 (n/a)</td><td>3.05 (n/a)</td><td>1.90 (n/a)</td><td>1.98 (n/a)</td><td>1.17 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.62 (-4.28%)</td><td>0.41 (+7.74%)</td><td>0.44 <b>(+25.21%)</b></td><td>0.08 (+3.34%)</td><td>0.21 (-0.36%)</td><td>0.61 (-4.28%)</td><td>0.40 (+7.74%)</td><td>0.43 <b>(+25.21%)</b></td><td>0.07 (+3.34%)</td><td>0.21 (-0.36%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.64 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td><td>0.63 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.75 <b>(+42.00%)</b></td><td>0.56 <b>(+39.88%)</b></td><td>0.55 (+15.66%)</td><td>0.39 <b>(+377.42%)</b></td><td>0.15 (-15.19%)</td><td>0.74 <b>(+42.00%)</b></td><td>0.55 <b>(+39.88%)</b></td><td>0.54 (+15.66%)</td><td>0.38 <b>(+377.42%)</b></td><td>0.15 (-15.19%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.52 (n/a)</td><td>0.40 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>0.18 (n/a)</td><td>0.52 (n/a)</td><td>0.39 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>2.37 (-11.53%)</td><td>1.58 (-2.42%)</td><td>1.77 (-7.00%)</td><td>0.82 <b>(+83.18%)</b></td><td>0.72 <b>(-34.98%)</b></td><td>2.33 (-11.53%)</td><td>1.55 (-2.42%)</td><td>1.74 (-7.00%)</td><td>0.81 <b>(+83.18%)</b></td><td>0.71 <b>(-34.98%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>2.68 (n/a)</td><td>1.62 (n/a)</td><td>1.91 (n/a)</td><td>0.45 (n/a)</td><td>1.11 (n/a)</td><td>2.64 (n/a)</td><td>1.59 (n/a)</td><td>1.88 (n/a)</td><td>0.44 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>461.20 (n/a)</td><td>377.00 (n/a)</td><td>405.30 (n/a)</td><td>267.80 (n/a)</td><td>77.83 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>687.80 (n/a)</td><td>533.18 (n/a)</td><td>527.00 (n/a)</td><td>310.20 (n/a)</td><td>142.24 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.70 (n/a)</td><td>419.28 (n/a)</td><td>448.20 (n/a)</td><td>258.50 (n/a)</td><td>128.54 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2064.50 (n/a)</td><td>775.66 (n/a)</td><td>540.30 (n/a)</td><td>211.80 (n/a)</td><td>734.87 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1905.10 (n/a)</td><td>796.12 (n/a)</td><td>563.80 (n/a)</td><td>160.90 (n/a)</td><td>662.90 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.40 (n/a)</td><td>429.54 (n/a)</td><td>470.60 (n/a)</td><td>174.50 (n/a)</td><td>158.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (+9.54%)</td><td>0.02 (+0.65%)</td><td>0.03 (-4.75%)</td><td>0.02 (-0.23%)</td><td>0.01 (+10.93%)</td><td>522.10 (+0.23%)</td><td>365.34 (+0.56%)</td><td>322.60 (+4.98%)</td><td>240.50 (-8.69%)</td><td>124.36 (+5.26%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.90 (n/a)</td><td>363.30 (n/a)</td><td>307.30 (n/a)</td><td>263.40 (n/a)</td><td>118.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (+16.05%)</td><td>0.02 (+1.31%)</td><td>0.03 (-3.84%)</td><td>0.01 (-6.70%)</td><td>0.01 <b>(+40.91%)</b></td><td>549.90 (+7.17%)</td><td>379.36 (+4.20%)</td><td>326.10 (+4.02%)</td><td>236.40 (-13.82%)</td><td>145.51 <b>(+37.23%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.10 (n/a)</td><td>364.06 (n/a)</td><td>313.50 (n/a)</td><td>274.30 (n/a)</td><td>106.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (-8.09%)</td><td>0.03 (+12.46%)</td><td>0.03 <b>(+52.09%)</b></td><td>0.01 (-5.18%)</td><td>0.01 (-10.31%)</td><td>574.10 (+5.46%)</td><td>356.50 (-11.56%)</td><td>292.00 <b>(-34.25%)</b></td><td>249.10 (+8.82%)</td><td>134.18 (+4.81%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.40 (n/a)</td><td>403.10 (n/a)</td><td>444.10 (n/a)</td><td>228.90 (n/a)</td><td>128.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (-16.26%)</td><td>0.02 (-6.59%)</td><td>0.02 (+5.73%)</td><td>0.01 (+10.57%)</td><td>0.01 <b>(-34.12%)</b></td><td>553.60 (-9.56%)</td><td>430.08 (+0.85%)</td><td>442.10 (-5.41%)</td><td>289.50 (+19.43%)</td><td>113.06 <b>(-26.61%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.10 (n/a)</td><td>426.44 (n/a)</td><td>467.40 (n/a)</td><td>242.40 (n/a)</td><td>154.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 <b>(+37.42%)</b></td><td>0.02 <b>(+25.37%)</b></td><td>0.02 (+0.38%)</td><td>0.01 (-1.91%)</td><td>0.01 <b>(+103.37%)</b></td><td>585.80 (+1.95%)</td><td>421.68 (-11.45%)</td><td>504.60 (-0.38%)</td><td>219.20 <b>(-27.22%)</b></td><td>165.18 <b>(+60.41%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.60 (n/a)</td><td>476.20 (n/a)</td><td>506.50 (n/a)</td><td>301.20 (n/a)</td><td>102.97 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 <b>(+79.00%)</b></td><td>0.02 <b>(+32.29%)</b></td><td>0.02 (+16.98%)</td><td>0.01 (-5.37%)</td><td>0.01 <b>(+156.92%)</b></td><td>1065.90 (+5.68%)</td><td>551.72 (-10.78%)</td><td>450.50 (-14.52%)</td><td>265.00 <b>(-44.14%)</b></td><td>322.89 <b>(+45.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1008.60 (n/a)</td><td>618.36 (n/a)</td><td>527.00 (n/a)</td><td>474.40 (n/a)</td><td>221.65 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 <b>(+30.87%)</b></td><td>0.02 <b>(+20.05%)</b></td><td>0.02 <b>(+29.75%)</b></td><td>0.01 (+9.34%)</td><td>0.01 <b>(+27.49%)</b></td><td>584.20 (-8.55%)</td><td>375.06 (-16.06%)</td><td>330.40 <b>(-22.93%)</b></td><td>203.50 <b>(-23.58%)</b></td><td>143.62 (-12.52%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.80 (n/a)</td><td>446.80 (n/a)</td><td>428.70 (n/a)</td><td>266.30 (n/a)</td><td>164.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (-9.76%)</td><td>0.02 <b>(+20.50%)</b></td><td>0.03 <b>(+54.56%)</b></td><td>0.01 (+14.92%)</td><td>0.01 (-11.42%)</td><td>565.50 (-12.97%)</td><td>394.22 (-18.31%)</td><td>311.20 <b>(-35.30%)</b></td><td>300.00 (+10.82%)</td><td>122.46 (-11.37%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.80 (n/a)</td><td>482.60 (n/a)</td><td>481.00 (n/a)</td><td>270.70 (n/a)</td><td>138.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (+14.88%)</td><td>0.02 (-5.43%)</td><td>0.03 (+2.66%)</td><td>0.00 <b>(-73.18%)</b></td><td>0.01 <b>(+79.77%)</b></td><td>1999.60 <b>(+272.92%)</b></td><td>633.60 <b>(+81.43%)</b></td><td>307.90 (-2.59%)</td><td>225.20 (-12.95%)</td><td>764.72 <b>(+577.95%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.20 (n/a)</td><td>349.22 (n/a)</td><td>316.10 (n/a)</td><td>258.70 (n/a)</td><td>112.80 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (-12.10%)</td><td>0.02 <b>(-24.32%)</b></td><td>0.02 <b>(-42.15%)</b></td><td>0.02 (+5.23%)</td><td>0.01 (-10.29%)</td><td>526.70 (-4.98%)</td><td>410.54 <b>(+29.18%)</b></td><td>460.40 <b>(+72.89%)</b></td><td>208.50 (+13.75%)</td><td>122.84 (-13.11%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.30 (n/a)</td><td>317.80 (n/a)</td><td>266.30 (n/a)</td><td>183.30 (n/a)</td><td>141.37 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (-16.84%)</td><td>0.03 (+13.30%)</td><td>0.03 (+0.72%)</td><td>0.03 <b>(+98.92%)</b></td><td>0.00 <b>(-81.56%)</b></td><td>271.80 <b>(-49.72%)</b></td><td>250.72 <b>(-23.37%)</b></td><td>244.00 (-0.73%)</td><td>234.00 <b>(+20.25%)</b></td><td>16.06 <b>(-89.03%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.60 (n/a)</td><td>327.20 (n/a)</td><td>245.80 (n/a)</td><td>194.60 (n/a)</td><td>146.43 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 <b>(+26.71%)</b></td><td>0.02 <b>(+36.82%)</b></td><td>0.03 <b>(+59.70%)</b></td><td>0.01 (+6.03%)</td><td>0.01 <b>(+50.66%)</b></td><td>592.70 (-5.70%)</td><td>368.72 <b>(-24.00%)</b></td><td>288.60 <b>(-37.37%)</b></td><td>249.90 <b>(-21.09%)</b></td><td>147.21 (+4.99%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.50 (n/a)</td><td>485.16 (n/a)</td><td>460.80 (n/a)</td><td>316.70 (n/a)</td><td>140.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 <b>(+64.02%)</b></td><td>0.03 <b>(+88.82%)</b></td><td>0.03 <b>(+112.96%)</b></td><td>0.02 <b>(+47.87%)</b></td><td>0.01 <b>(+102.61%)</b></td><td>397.80 <b>(-32.38%)</b></td><td>271.68 <b>(-46.11%)</b></td><td>243.50 <b>(-53.05%)</b></td><td>233.40 <b>(-39.03%)</b></td><td>70.64 (-14.06%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.30 (n/a)</td><td>504.12 (n/a)</td><td>518.60 (n/a)</td><td>382.80 (n/a)</td><td>82.20 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 <b>(+26.02%)</b></td><td>0.02 <b>(+25.13%)</b></td><td>0.03 <b>(+54.52%)</b></td><td>0.01 (-10.81%)</td><td>0.01 <b>(+81.89%)</b></td><td>606.30 (+12.13%)</td><td>392.52 (-12.26%)</td><td>325.40 <b>(-35.30%)</b></td><td>236.60 <b>(-20.63%)</b></td><td>170.17 <b>(+61.05%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.70 (n/a)</td><td>447.36 (n/a)</td><td>502.90 (n/a)</td><td>298.10 (n/a)</td><td>105.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (+3.30%)</td><td>0.03 (+13.06%)</td><td>0.03 (+5.43%)</td><td>0.02 <b>(+58.75%)</b></td><td>0.01 <b>(-39.90%)</b></td><td>362.50 <b>(-37.02%)</b></td><td>275.24 <b>(-20.19%)</b></td><td>246.30 (-5.16%)</td><td>217.80 (-3.16%)</td><td>58.18 <b>(-61.98%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.60 (n/a)</td><td>344.88 (n/a)</td><td>259.70 (n/a)</td><td>224.90 (n/a)</td><td>153.04 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.05 (+0.29%)</td><td>0.04 (-7.52%)</td><td>0.04 (+4.06%)</td><td>0.02 (-14.63%)</td><td>0.01 <b>(+39.63%)</b></td><td>619.60 (+17.13%)</td><td>398.86 (+16.95%)</td><td>296.90 (-3.88%)</td><td>247.80 (-0.28%)</td><td>175.90 <b>(+59.53%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.00 (n/a)</td><td>341.06 (n/a)</td><td>308.90 (n/a)</td><td>248.50 (n/a)</td><td>110.26 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (+2.07%)</td><td>0.03 (-6.17%)</td><td>0.03 (+2.58%)</td><td>0.02 (-10.30%)</td><td>0.01 <b>(+30.47%)</b></td><td>515.20 (+11.49%)</td><td>339.86 (+10.45%)</td><td>275.80 (-2.51%)</td><td>242.20 (-2.02%)</td><td>118.02 <b>(+34.67%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.10 (n/a)</td><td>307.70 (n/a)</td><td>282.90 (n/a)</td><td>247.20 (n/a)</td><td>87.64 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (+0.53%)</td><td>0.03 (-0.40%)</td><td>0.02 (-18.28%)</td><td>0.02 (+1.93%)</td><td>0.01 (-0.52%)</td><td>549.60 (-1.89%)</td><td>398.28 (-0.63%)</td><td>441.50 <b>(+22.37%)</b></td><td>266.30 (-0.52%)</td><td>126.39 (-10.56%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>560.20 (n/a)</td><td>400.82 (n/a)</td><td>360.80 (n/a)</td><td>267.70 (n/a)</td><td>141.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (+2.22%)</td><td>0.02 <b>(-22.55%)</b></td><td>0.02 <b>(-30.11%)</b></td><td>0.00 <b>(-78.89%)</b></td><td>0.01 <b>(+151.83%)</b></td><td>1862.60 <b>(+373.70%)</b></td><td>633.02 <b>(+117.43%)</b></td><td>399.60 <b>(+43.07%)</b></td><td>241.00 (-2.19%)</td><td>692.33 <b>(+1076.47%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>393.20 (n/a)</td><td>291.14 (n/a)</td><td>279.30 (n/a)</td><td>246.40 (n/a)</td><td>58.85 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.05 (-4.98%)</td><td>0.03 <b>(-31.39%)</b></td><td>0.02 <b>(-49.94%)</b></td><td>0.01 <b>(-30.95%)</b></td><td>0.01 (+13.91%)</td><td>790.70 <b>(+44.84%)</b></td><td>468.74 <b>(+57.20%)</b></td><td>482.30 <b>(+99.71%)</b></td><td>224.10 (+5.21%)</td><td>221.55 <b>(+58.83%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.90 (n/a)</td><td>298.18 (n/a)</td><td>241.50 (n/a)</td><td>213.00 (n/a)</td><td>139.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (-6.35%)</td><td>0.02 <b>(-37.61%)</b></td><td>0.02 <b>(-40.73%)</b></td><td>0.00 <b>(-71.54%)</b></td><td>0.01 <b>(+46.69%)</b></td><td>2452.00 <b>(+251.34%)</b></td><td>1075.02 <b>(+201.01%)</b></td><td>484.20 <b>(+68.71%)</b></td><td>249.10 (+6.77%)</td><td>1016.15 <b>(+429.09%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>697.90 (n/a)</td><td>357.14 (n/a)</td><td>287.00 (n/a)</td><td>233.30 (n/a)</td><td>192.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (+17.17%)</td><td>0.02 (-5.86%)</td><td>0.02 <b>(-21.75%)</b></td><td>0.01 <b>(+21.56%)</b></td><td>0.01 (-4.45%)</td><td>669.30 (-17.74%)</td><td>443.00 (+0.84%)</td><td>383.20 <b>(+27.82%)</b></td><td>249.10 (-14.66%)</td><td>161.49 <b>(-28.84%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>813.60 (n/a)</td><td>439.30 (n/a)</td><td>299.80 (n/a)</td><td>291.90 (n/a)</td><td>226.93 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (+11.35%)</td><td>0.03 <b>(+31.26%)</b></td><td>0.03 <b>(+74.75%)</b></td><td>0.01 (+9.70%)</td><td>0.01 (+16.04%)</td><td>571.80 (-8.83%)</td><td>375.18 <b>(-20.65%)</b></td><td>302.20 <b>(-42.77%)</b></td><td>186.70 (-10.20%)</td><td>182.52 (+11.75%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.20 (n/a)</td><td>472.80 (n/a)</td><td>528.00 (n/a)</td><td>207.90 (n/a)</td><td>163.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (+16.58%)</td><td>0.03 (-1.96%)</td><td>0.02 (-17.81%)</td><td>0.02 (-13.41%)</td><td>0.01 <b>(+36.88%)</b></td><td>612.10 (+15.49%)</td><td>400.14 (+7.32%)</td><td>395.10 <b>(+21.68%)</b></td><td>232.60 (-14.23%)</td><td>151.83 <b>(+34.37%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.00 (n/a)</td><td>372.84 (n/a)</td><td>324.70 (n/a)</td><td>271.20 (n/a)</td><td>112.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 <b>(-22.99%)</b></td><td>0.02 (-16.74%)</td><td>0.01 (-13.45%)</td><td>0.01 (+1.57%)</td><td>0.00 <b>(-47.16%)</b></td><td>672.80 (-1.54%)</td><td>516.46 (+11.92%)</td><td>552.60 (+15.53%)</td><td>369.50 <b>(+29.83%)</b></td><td>118.74 <b>(-29.95%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>683.30 (n/a)</td><td>461.46 (n/a)</td><td>478.30 (n/a)</td><td>284.60 (n/a)</td><td>169.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.33 (-2.23%)</td><td>0.27 <b>(+20.79%)</b></td><td>0.29 <b>(+46.22%)</b></td><td>0.20 <b>(+26.56%)</b></td><td>0.06 <b>(-21.76%)</b></td><td>490.60 <b>(-20.97%)</b></td><td>375.04 <b>(-20.33%)</b></td><td>343.90 <b>(-31.62%)</b></td><td>296.60 (+2.28%)</td><td>85.70 <b>(-37.07%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>620.80 (n/a)</td><td>470.72 (n/a)</td><td>502.90 (n/a)</td><td>290.00 (n/a)</td><td>136.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.32 (-12.65%)</td><td>0.22 (-18.47%)</td><td>0.24 <b>(-21.06%)</b></td><td>0.10 <b>(-35.72%)</b></td><td>0.09 (-4.70%)</td><td>1019.40 <b>(+55.56%)</b></td><td>539.84 <b>(+30.55%)</b></td><td>415.00 <b>(+26.68%)</b></td><td>303.80 (+14.47%)</td><td>286.36 <b>(+74.96%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.30 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>655.30 (n/a)</td><td>413.52 (n/a)</td><td>327.60 (n/a)</td><td>265.40 (n/a)</td><td>163.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.43 <b>(+49.81%)</b></td><td>0.34 <b>(+61.63%)</b></td><td>0.41 <b>(+109.52%)</b></td><td>0.20 (+17.36%)</td><td>0.12 <b>(+140.84%)</b></td><td>498.90 (-14.79%)</td><td>329.34 <b>(-32.96%)</b></td><td>239.50 <b>(-52.26%)</b></td><td>228.10 <b>(-33.27%)</b></td><td>132.07 <b>(+34.99%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>585.50 (n/a)</td><td>491.24 (n/a)</td><td>501.70 (n/a)</td><td>341.80 (n/a)</td><td>97.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.27 (+6.29%)</td><td>0.20 (+13.57%)</td><td>0.16 (+2.89%)</td><td>0.14 (+1.00%)</td><td>0.07 <b>(+36.15%)</b></td><td>522.50 (-0.99%)</td><td>407.14 (-8.81%)</td><td>472.70 (-2.82%)</td><td>268.90 (-5.91%)</td><td>124.15 <b>(+24.71%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>527.70 (n/a)</td><td>446.48 (n/a)</td><td>486.40 (n/a)</td><td>285.80 (n/a)</td><td>99.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.27 (-9.01%)</td><td>0.23 (-5.91%)</td><td>0.24 (-1.47%)</td><td>0.16 (+8.65%)</td><td>0.04 <b>(-24.87%)</b></td><td>464.70 (-7.96%)</td><td>333.12 (+3.40%)</td><td>301.50 (+1.52%)</td><td>277.10 (+9.92%)</td><td>77.95 <b>(-25.55%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>504.90 (n/a)</td><td>322.16 (n/a)</td><td>297.00 (n/a)</td><td>252.10 (n/a)</td><td>104.70 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.30 (-0.50%)</td><td>0.22 (+18.70%)</td><td>0.24 <b>(+60.28%)</b></td><td>0.13 <b>(+33.57%)</b></td><td>0.07 <b>(-23.35%)</b></td><td>579.40 <b>(-25.13%)</b></td><td>372.40 <b>(-23.13%)</b></td><td>309.60 <b>(-37.61%)</b></td><td>244.30 (+0.49%)</td><td>132.31 <b>(-39.23%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>773.90 (n/a)</td><td>484.46 (n/a)</td><td>496.20 (n/a)</td><td>243.10 (n/a)</td><td>217.71 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.51 <b>(+36.58%)</b></td><td>0.29 (+12.47%)</td><td>0.27 (+9.17%)</td><td>0.07 <b>(-66.42%)</b></td><td>0.18 <b>(+175.90%)</b></td><td>1909.80 <b>(+197.75%)</b></td><td>730.40 <b>(+39.61%)</b></td><td>488.40 (-8.38%)</td><td>257.80 <b>(-26.78%)</b></td><td>681.34 <b>(+542.87%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>641.40 (n/a)</td><td>523.18 (n/a)</td><td>533.10 (n/a)</td><td>352.10 (n/a)</td><td>105.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.44 (+4.21%)</td><td>0.29 (+11.89%)</td><td>0.26 (+14.91%)</td><td>0.15 (-8.57%)</td><td>0.14 <b>(+25.28%)</b></td><td>864.60 (+9.37%)</td><td>549.04 (-4.86%)</td><td>513.90 (-12.99%)</td><td>295.30 (-4.06%)</td><td>259.71 <b>(+21.57%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.43 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>790.50 (n/a)</td><td>577.08 (n/a)</td><td>590.60 (n/a)</td><td>307.80 (n/a)</td><td>213.62 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.28 <b>(-33.34%)</b></td><td>0.23 (-20.00%)</td><td>0.25 <b>(-35.57%)</b></td><td>0.17 <b>(+144.70%)</b></td><td>0.05 <b>(-70.04%)</b></td><td>751.80 <b>(-59.13%)</b></td><td>587.76 (-19.04%)</td><td>514.90 <b>(+55.23%)</b></td><td>461.20 <b>(+50.03%)</b></td><td>131.46 <b>(-80.04%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.43 (n/a)</td><td>0.29 (n/a)</td><td>0.40 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1839.60 (n/a)</td><td>725.98 (n/a)</td><td>331.70 (n/a)</td><td>307.40 (n/a)</td><td>658.64 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/strided_copy</summary>


### test_strided_copy[chunked_transfer]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.70 (n/a)</td><td>405.94 (n/a)</td><td>292.40 (n/a)</td><td>269.80 (n/a)</td><td>166.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[contiguous]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>382.40 (n/a)</td><td>297.68 (n/a)</td><td>295.00 (n/a)</td><td>248.20 (n/a)</td><td>52.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1848.50 (n/a)</td><td>631.92 (n/a)</td><td>383.20 (n/a)</td><td>236.50 (n/a)</td><td>686.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.59 (n/a)</td><td>0.47 (n/a)</td><td>0.48 (n/a)</td><td>0.34 (n/a)</td><td>0.09 (n/a)</td><td>388.40 (n/a)</td><td>291.32 (n/a)</td><td>276.80 (n/a)</td><td>224.80 (n/a)</td><td>60.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.52 (n/a)</td><td>0.42 (n/a)</td><td>0.45 (n/a)</td><td>0.27 (n/a)</td><td>0.09 (n/a)</td><td>493.40 (n/a)</td><td>329.84 (n/a)</td><td>294.20 (n/a)</td><td>255.80 (n/a)</td><td>93.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.52 (n/a)</td><td>0.40 (n/a)</td><td>0.48 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>565.50 (n/a)</td><td>374.50 (n/a)</td><td>277.50 (n/a)</td><td>251.90 (n/a)</td><td>153.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.51 (n/a)</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>501.20 (n/a)</td><td>414.54 (n/a)</td><td>486.20 (n/a)</td><td>259.40 (n/a)</td><td>111.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot_last]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.54 (n/a)</td><td>0.45 (n/a)</td><td>0.50 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>610.70 (n/a)</td><td>332.24 (n/a)</td><td>266.10 (n/a)</td><td>245.20 (n/a)</td><td>156.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>738.50 (n/a)</td><td>399.74 (n/a)</td><td>294.90 (n/a)</td><td>212.00 (n/a)</td><td>227.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels_chunked]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>678.10 (n/a)</td><td>381.64 (n/a)</td><td>291.00 (n/a)</td><td>211.20 (n/a)</td><td>203.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]

_No metrics available._


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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-26.32%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-12.71%)</td><td>21328.00 (-5.83%)</td><td>17564.65 <b>(+26.51%)</b></td><td>20945.13 <b>(+34.63%)</b></td><td>7186.63 (+10.45%)</td><td>6067.43 (-11.43%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22648.63 (n/a)</td><td>13884.09 (n/a)</td><td>15557.60 (n/a)</td><td>6506.70 (n/a)</td><td>6850.41 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.00 (+9.09%)</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-54.55%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-0.39%)</td><td>18378.71 (-17.79%)</td><td>13003.58 (+4.39%)</td><td>15364.46 <b>(+101.90%)</b></td><td>6788.75 (-8.56%)</td><td>5259.92 <b>(-24.99%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22356.06 (n/a)</td><td>12456.27 (n/a)</td><td>7609.99 (n/a)</td><td>7424.25 (n/a)</td><td>7012.19 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.16 (+1.89%)</td><td>0.10 (-18.32%)</td><td>0.08 <b>(-36.44%)</b></td><td>0.07 (-1.75%)</td><td>0.04 (+14.37%)</td><td>31196.28 (+1.73%)</td><td>22747.45 <b>(+24.33%)</b></td><td>24986.08 <b>(+57.33%)</b></td><td>13445.52 (-1.82%)</td><td>7382.14 (+5.72%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>30665.29 (n/a)</td><td>18295.30 (n/a)</td><td>15881.58 (n/a)</td><td>13695.18 (n/a)</td><td>6982.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>1.59 (-6.61%)</td><td>0.94 (-14.20%)</td><td>0.80 <b>(-20.15%)</b></td><td>0.64 (-11.82%)</td><td>0.38 (+2.01%)</td><td>821.20 (+13.41%)</td><td>615.92 (+18.63%)</td><td>651.30 <b>(+25.23%)</b></td><td>329.10 (+7.06%)</td><td>180.74 <b>(+20.01%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>1.71 (n/a)</td><td>1.09 (n/a)</td><td>1.01 (n/a)</td><td>0.72 (n/a)</td><td>0.37 (n/a)</td><td>724.10 (n/a)</td><td>519.18 (n/a)</td><td>520.10 (n/a)</td><td>307.40 (n/a)</td><td>150.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>2.44 (+2.64%)</td><td>1.40 (+3.51%)</td><td>1.92 <b>(+40.54%)</b></td><td>0.30 (-1.11%)</td><td>1.03 <b>(+31.90%)</b></td><td>3543.60 (+1.12%)</td><td>1711.78 <b>(+34.44%)</b></td><td>545.60 <b>(-28.85%)</b></td><td>430.00 (-2.56%)</td><td>1666.86 <b>(+31.54%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>2.38 (n/a)</td><td>1.36 (n/a)</td><td>1.37 (n/a)</td><td>0.30 (n/a)</td><td>0.78 (n/a)</td><td>3504.30 (n/a)</td><td>1273.28 (n/a)</td><td>766.80 (n/a)</td><td>441.30 (n/a)</td><td>1267.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>2.03 (+2.25%)</td><td>1.19 (-4.16%)</td><td>1.00 (-1.05%)</td><td>0.88 (+15.60%)</td><td>0.48 (-3.50%)</td><td>595.20 (-13.49%)</td><td>483.08 (+1.79%)</td><td>525.90 (+1.06%)</td><td>258.20 (-2.20%)</td><td>130.43 <b>(-21.75%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:27:50</td><td>1.99 (n/a)</td><td>1.24 (n/a)</td><td>1.01 (n/a)</td><td>0.76 (n/a)</td><td>0.49 (n/a)</td><td>688.00 (n/a)</td><td>474.58 (n/a)</td><td>520.40 (n/a)</td><td>264.00 (n/a)</td><td>166.68 (n/a)</td>
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
