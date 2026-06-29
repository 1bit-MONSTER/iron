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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.05 (+6.67%)</td><td>0.04 (+7.41%)</td><td>0.03 (-6.58%)</td><td>0.03 <b>(+28.95%)</b></td><td>0.01 <b>(-25.01%)</b></td><td>456.40 <b>(-22.45%)</b></td><td>348.90 (-11.44%)</td><td>352.70 (+7.04%)</td><td>256.10 (-6.26%)</td><td>73.17 <b>(-45.81%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>588.50 (n/a)</td><td>393.98 (n/a)</td><td>329.50 (n/a)</td><td>273.20 (n/a)</td><td>135.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 <b>(-20.54%)</b></td><td>0.02 <b>(-20.67%)</b></td><td>0.03 (+9.06%)</td><td>0.01 <b>(-60.51%)</b></td><td>0.01 (+7.02%)</td><td>1339.30 <b>(+153.27%)</b></td><td>630.14 <b>(+48.47%)</b></td><td>445.30 (-8.32%)</td><td>341.80 <b>(+25.85%)</b></td><td>411.31 <b>(+249.42%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.80 (n/a)</td><td>424.42 (n/a)</td><td>485.70 (n/a)</td><td>271.60 (n/a)</td><td>117.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (-18.84%)</td><td>0.02 (+1.87%)</td><td>0.02 <b>(+28.40%)</b></td><td>0.01 <b>(-50.51%)</b></td><td>0.01 (+13.65%)</td><td>2171.60 <b>(+102.07%)</b></td><td>836.08 <b>(+24.32%)</b></td><td>509.50 <b>(-22.12%)</b></td><td>472.70 <b>(+23.20%)</b></td><td>746.98 <b>(+195.37%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1074.70 (n/a)</td><td>672.54 (n/a)</td><td>654.20 (n/a)</td><td>383.70 (n/a)</td><td>252.90 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 <b>(+55.84%)</b></td><td>0.02 <b>(+25.28%)</b></td><td>0.02 (+9.82%)</td><td>0.01 (-1.69%)</td><td>0.01 <b>(+108.08%)</b></td><td>493.50 (+1.73%)</td><td>293.02 (-14.71%)</td><td>272.80 (-8.91%)</td><td>185.70 <b>(-35.83%)</b></td><td>118.12 <b>(+42.90%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>485.10 (n/a)</td><td>343.56 (n/a)</td><td>299.50 (n/a)</td><td>289.40 (n/a)</td><td>82.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 <b>(+75.25%)</b></td><td>0.01 (+12.87%)</td><td>0.01 <b>(-24.11%)</b></td><td>0.00 (+12.99%)</td><td>0.01 <b>(+82.39%)</b></td><td>1072.20 (-11.49%)</td><td>557.28 (-4.11%)</td><td>501.40 <b>(+31.77%)</b></td><td>165.10 <b>(-42.93%)</b></td><td>326.36 (-15.45%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1211.40 (n/a)</td><td>581.16 (n/a)</td><td>380.50 (n/a)</td><td>289.30 (n/a)</td><td>385.98 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 <b>(+110.32%)</b></td><td>0.03 <b>(+131.11%)</b></td><td>0.02 <b>(+149.24%)</b></td><td>0.02 <b>(+324.19%)</b></td><td>0.01 <b>(+38.03%)</b></td><td>264.10 <b>(-76.43%)</b></td><td>217.50 <b>(-63.34%)</b></td><td>235.00 <b>(-59.88%)</b></td><td>138.00 <b>(-52.45%)</b></td><td>51.17 <b>(-84.39%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1120.30 (n/a)</td><td>593.36 (n/a)</td><td>585.70 (n/a)</td><td>290.20 (n/a)</td><td>327.86 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 <b>(+51.77%)</b></td><td>0.02 <b>(+49.92%)</b></td><td>0.02 (+17.06%)</td><td>0.02 <b>(+217.12%)</b></td><td>0.01 (-6.79%)</td><td>334.80 <b>(-68.46%)</b></td><td>245.52 <b>(-47.73%)</b></td><td>224.10 (-14.56%)</td><td>164.10 <b>(-34.12%)</b></td><td>74.79 <b>(-78.67%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1061.60 (n/a)</td><td>469.68 (n/a)</td><td>262.30 (n/a)</td><td>249.10 (n/a)</td><td>350.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.02 (-5.19%)</td><td>0.02 (+5.36%)</td><td>0.02 <b>(+57.54%)</b></td><td>0.01 (-14.05%)</td><td>0.01 (+3.29%)</td><td>596.80 (+16.36%)</td><td>395.14 (-2.45%)</td><td>305.80 <b>(-36.53%)</b></td><td>254.10 (+5.48%)</td><td>161.38 <b>(+25.83%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>512.90 (n/a)</td><td>405.06 (n/a)</td><td>481.80 (n/a)</td><td>240.90 (n/a)</td><td>128.25 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.01 <b>(-53.47%)</b></td><td>0.01 <b>(-43.50%)</b></td><td>0.01 (-18.76%)</td><td>0.00 <b>(-69.59%)</b></td><td>0.00 <b>(-39.32%)</b></td><td>1854.70 <b>(+228.85%)</b></td><td>892.66 <b>(+97.03%)</b></td><td>637.50 <b>(+23.09%)</b></td><td>615.60 <b>(+114.94%)</b></td><td>539.55 <b>(+334.95%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>564.00 (n/a)</td><td>453.06 (n/a)</td><td>517.90 (n/a)</td><td>286.40 (n/a)</td><td>124.05 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>624.50 (n/a)</td><td>480.32 (n/a)</td><td>453.10 (n/a)</td><td>290.20 (n/a)</td><td>138.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>629.80 (n/a)</td><td>493.46 (n/a)</td><td>537.60 (n/a)</td><td>230.60 (n/a)</td><td>153.42 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.60 (n/a)</td><td>388.84 (n/a)</td><td>462.90 (n/a)</td><td>230.40 (n/a)</td><td>128.30 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.30 (n/a)</td><td>317.56 (n/a)</td><td>272.10 (n/a)</td><td>246.00 (n/a)</td><td>121.28 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>659.50 (n/a)</td><td>494.72 (n/a)</td><td>477.10 (n/a)</td><td>305.10 (n/a)</td><td>131.84 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.60 (n/a)</td><td>406.32 (n/a)</td><td>467.30 (n/a)</td><td>245.20 (n/a)</td><td>104.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.10 (n/a)</td><td>347.60 (n/a)</td><td>247.60 (n/a)</td><td>165.80 (n/a)</td><td>183.10 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1855.30 (n/a)</td><td>733.76 (n/a)</td><td>536.90 (n/a)</td><td>212.30 (n/a)</td><td>643.38 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.20 (n/a)</td><td>311.16 (n/a)</td><td>256.50 (n/a)</td><td>220.20 (n/a)</td><td>126.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.70 (n/a)</td><td>495.60 (n/a)</td><td>563.10 (n/a)</td><td>280.40 (n/a)</td><td>124.98 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.70 (n/a)</td><td>373.70 (n/a)</td><td>326.90 (n/a)</td><td>240.60 (n/a)</td><td>130.46 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>437.60 (n/a)</td><td>352.34 (n/a)</td><td>359.30 (n/a)</td><td>242.20 (n/a)</td><td>85.42 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.65 <b>(+22.36%)</b></td><td>0.43 (-7.04%)</td><td>0.38 <b>(-23.13%)</b></td><td>0.35 (+6.63%)</td><td>0.12 <b>(+54.56%)</b></td><td>631.70 (-6.22%)</td><td>539.58 (+9.79%)</td><td>588.20 <b>(+30.08%)</b></td><td>342.20 (-18.27%)</td><td>115.76 (+11.08%)</td><td>27.58 <b>(+22.36%)</b></td><td>18.38 (-7.04%)</td><td>16.04 <b>(-23.13%)</b></td><td>14.94 (+6.63%)</td><td>5.23 <b>(+54.56%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.53 (n/a)</td><td>0.46 (n/a)</td><td>0.49 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>673.60 (n/a)</td><td>491.46 (n/a)</td><td>452.20 (n/a)</td><td>418.70 (n/a)</td><td>104.22 (n/a)</td><td>22.54 (n/a)</td><td>19.77 (n/a)</td><td>20.87 (n/a)</td><td>14.01 (n/a)</td><td>3.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.54 (+16.49%)</td><td>0.44 <b>(+24.60%)</b></td><td>0.43 (+0.34%)</td><td>0.36 <b>(+297.73%)</b></td><td>0.08 <b>(-46.27%)</b></td><td>620.60 <b>(-74.86%)</b></td><td>511.02 <b>(-44.09%)</b></td><td>517.20 (-0.35%)</td><td>406.60 (-14.15%)</td><td>93.06 <b>(-89.30%)</b></td><td>23.21 (+16.49%)</td><td>18.98 <b>(+24.60%)</b></td><td>18.25 (+0.34%)</td><td>15.21 <b>(+297.73%)</b></td><td>3.51 <b>(-46.27%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.47 (n/a)</td><td>0.36 (n/a)</td><td>0.43 (n/a)</td><td>0.09 (n/a)</td><td>0.15 (n/a)</td><td>2468.50 (n/a)</td><td>914.00 (n/a)</td><td>519.00 (n/a)</td><td>473.60 (n/a)</td><td>870.07 (n/a)</td><td>19.93 (n/a)</td><td>15.23 (n/a)</td><td>18.18 (n/a)</td><td>3.82 (n/a)</td><td>6.54 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.31 (-0.42%)</td><td>0.31 (+1.74%)</td><td>0.31 (+2.51%)</td><td>0.30 (+1.50%)</td><td>0.01 <b>(-24.23%)</b></td><td>84687.50 (-1.47%)</td><td>82190.72 (-1.73%)</td><td>81670.10 (-2.45%)</td><td>80980.40 (+0.42%)</td><td>1515.67 <b>(-24.86%)</b></td><td>212.15 (-0.42%)</td><td>209.08 (+1.74%)</td><td>210.36 (+2.51%)</td><td>202.86 (+1.50%)</td><td>3.79 <b>(-24.23%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85954.00 (n/a)</td><td>83637.32 (n/a)</td><td>83724.00 (n/a)</td><td>80641.80 (n/a)</td><td>2017.03 (n/a)</td><td>213.04 (n/a)</td><td>205.51 (n/a)</td><td>205.20 (n/a)</td><td>199.87 (n/a)</td><td>5.01 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>1.02 (-0.92%)</td><td>0.98 (-4.21%)</td><td>1.01 (-1.53%)</td><td>0.91 (-11.25%)</td><td>0.05 <b>(+1781.95%)</b></td><td>27693.90 (+12.68%)</td><td>25659.76 (+4.60%)</td><td>24928.50 (+1.56%)</td><td>24658.50 (+0.93%)</td><td>1291.06 <b>(+2036.04%)</b></td><td>696.71 (-0.92%)</td><td>670.84 (-4.21%)</td><td>689.16 (-1.53%)</td><td>620.35 (-11.25%)</td><td>32.54 <b>(+1781.79%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.03 (n/a)</td><td>1.03 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.00 (n/a)</td><td>24577.70 (n/a)</td><td>24532.28 (n/a)</td><td>24546.30 (n/a)</td><td>24430.80 (n/a)</td><td>60.44 (n/a)</td><td>703.20 (n/a)</td><td>700.30 (n/a)</td><td>699.90 (n/a)</td><td>699.00 (n/a)</td><td>1.73 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>2.27 <b>(-40.21%)</b></td><td>1.74 <b>(-40.99%)</b></td><td>1.61 <b>(-54.01%)</b></td><td>1.33 (-11.32%)</td><td>0.41 <b>(-61.18%)</b></td><td>6051.30 (+12.76%)</td><td>4847.08 <b>(+54.43%)</b></td><td>5008.50 <b>(+117.46%)</b></td><td>3549.20 <b>(+67.23%)</b></td><td>1085.54 <b>(-23.56%)</b></td><td>595.60 <b>(-40.21%)</b></td><td>455.16 <b>(-40.99%)</b></td><td>422.07 <b>(-54.01%)</b></td><td>349.34 (-11.32%)</td><td>107.05 <b>(-61.18%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>3.80 (n/a)</td><td>2.94 (n/a)</td><td>3.50 (n/a)</td><td>1.50 (n/a)</td><td>1.05 (n/a)</td><td>5366.40 (n/a)</td><td>3138.64 (n/a)</td><td>2303.20 (n/a)</td><td>2122.30 (n/a)</td><td>1420.14 (n/a)</td><td>996.08 (n/a)</td><td>771.31 (n/a)</td><td>917.81 (n/a)</td><td>393.92 (n/a)</td><td>275.75 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.29 (-11.40%)</td><td>0.22 (-2.67%)</td><td>0.21 (+0.29%)</td><td>0.18 (+0.39%)</td><td>0.04 <b>(-30.64%)</b></td><td>6986.90 (-0.39%)</td><td>5806.54 (+0.28%)</td><td>6022.80 (-0.29%)</td><td>4302.00 (+12.87%)</td><td>1018.41 <b>(-24.56%)</b></td><td>15.60 (-11.40%)</td><td>11.88 (-2.67%)</td><td>11.14 (+0.29%)</td><td>9.60 (+0.39%)</td><td>2.32 <b>(-30.64%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>7014.20 (n/a)</td><td>5790.04 (n/a)</td><td>6040.20 (n/a)</td><td>3811.60 (n/a)</td><td>1350.01 (n/a)</td><td>17.61 (n/a)</td><td>12.20 (n/a)</td><td>11.11 (n/a)</td><td>9.57 (n/a)</td><td>3.34 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.13 (-10.28%)</td><td>0.07 <b>(-26.72%)</b></td><td>0.07 <b>(-33.49%)</b></td><td>0.04 <b>(-29.83%)</b></td><td>0.03 (-14.17%)</td><td>0.13 (-10.28%)</td><td>0.07 <b>(-26.72%)</b></td><td>0.07 <b>(-33.49%)</b></td><td>0.04 <b>(-29.83%)</b></td><td>0.03 (-14.17%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>3.76 (+0.68%)</td><td>3.59 (-0.36%)</td><td>3.70 (+2.44%)</td><td>3.38 (+0.17%)</td><td>0.18 <b>(+24.19%)</b></td><td>3.75 (+0.68%)</td><td>3.59 (-0.36%)</td><td>3.70 (+2.44%)</td><td>3.38 (+0.17%)</td><td>0.18 <b>(+24.19%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>3.73 (n/a)</td><td>3.61 (n/a)</td><td>3.61 (n/a)</td><td>3.38 (n/a)</td><td>0.14 (n/a)</td><td>3.73 (n/a)</td><td>3.61 (n/a)</td><td>3.61 (n/a)</td><td>3.37 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>7.35 (-1.78%)</td><td>6.24 (-11.03%)</td><td>5.87 (-17.64%)</td><td>5.59 (-14.34%)</td><td>0.79 <b>(+78.21%)</b></td><td>7.35 (-1.78%)</td><td>6.23 (-11.03%)</td><td>5.86 (-17.64%)</td><td>5.59 (-14.34%)</td><td>0.79 <b>(+78.21%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>7.49 (n/a)</td><td>7.01 (n/a)</td><td>7.12 (n/a)</td><td>6.53 (n/a)</td><td>0.44 (n/a)</td><td>7.48 (n/a)</td><td>7.01 (n/a)</td><td>7.12 (n/a)</td><td>6.52 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>12.77 (-8.67%)</td><td>9.45 (-9.58%)</td><td>8.36 (-14.22%)</td><td>8.06 (+11.13%)</td><td>2.01 <b>(-34.77%)</b></td><td>12.76 (-8.67%)</td><td>9.44 (-9.58%)</td><td>8.36 (-14.22%)</td><td>8.05 (+11.13%)</td><td>2.01 <b>(-34.77%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>13.98 (n/a)</td><td>10.45 (n/a)</td><td>9.75 (n/a)</td><td>7.25 (n/a)</td><td>3.08 (n/a)</td><td>13.97 (n/a)</td><td>10.44 (n/a)</td><td>9.74 (n/a)</td><td>7.24 (n/a)</td><td>3.08 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>3.82 (-2.57%)</td><td>3.72 (+0.95%)</td><td>3.81 (+1.25%)</td><td>3.43 (+2.76%)</td><td>0.17 <b>(-34.62%)</b></td><td>3.82 (-2.57%)</td><td>3.72 (+0.95%)</td><td>3.81 (+1.25%)</td><td>3.43 (+2.76%)</td><td>0.17 <b>(-34.62%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>3.92 (n/a)</td><td>3.69 (n/a)</td><td>3.76 (n/a)</td><td>3.34 (n/a)</td><td>0.25 (n/a)</td><td>3.92 (n/a)</td><td>3.68 (n/a)</td><td>3.76 (n/a)</td><td>3.34 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>6.74 (-10.56%)</td><td>6.31 (-9.31%)</td><td>6.71 (-1.75%)</td><td>5.62 (-9.31%)</td><td>0.57 (-0.55%)</td><td>6.73 (-10.56%)</td><td>6.30 (-9.31%)</td><td>6.71 (-1.75%)</td><td>5.62 (-9.31%)</td><td>0.57 (-0.55%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>7.53 (n/a)</td><td>6.96 (n/a)</td><td>6.83 (n/a)</td><td>6.20 (n/a)</td><td>0.57 (n/a)</td><td>7.53 (n/a)</td><td>6.95 (n/a)</td><td>6.83 (n/a)</td><td>6.19 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>14.04 <b>(+29.62%)</b></td><td>10.51 <b>(+21.62%)</b></td><td>8.52 (+5.04%)</td><td>8.11 (+1.34%)</td><td>2.95 <b>(+140.85%)</b></td><td>14.03 <b>(+29.62%)</b></td><td>10.50 <b>(+21.62%)</b></td><td>8.51 (+5.04%)</td><td>8.10 (+1.34%)</td><td>2.95 <b>(+140.85%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>10.83 (n/a)</td><td>8.64 (n/a)</td><td>8.11 (n/a)</td><td>8.00 (n/a)</td><td>1.23 (n/a)</td><td>10.82 (n/a)</td><td>8.64 (n/a)</td><td>8.10 (n/a)</td><td>8.00 (n/a)</td><td>1.22 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.60 (n/a)</td><td>462.76 (n/a)</td><td>444.50 (n/a)</td><td>380.70 (n/a)</td><td>83.81 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>836.00 (n/a)</td><td>536.84 (n/a)</td><td>526.90 (n/a)</td><td>281.70 (n/a)</td><td>205.08 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.20 (n/a)</td><td>494.88 (n/a)</td><td>497.20 (n/a)</td><td>287.40 (n/a)</td><td>145.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>974.00 (n/a)</td><td>513.26 (n/a)</td><td>464.80 (n/a)</td><td>244.70 (n/a)</td><td>292.49 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.90 (n/a)</td><td>495.20 (n/a)</td><td>531.70 (n/a)</td><td>288.10 (n/a)</td><td>127.75 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.70 (n/a)</td><td>466.66 (n/a)</td><td>492.80 (n/a)</td><td>288.50 (n/a)</td><td>120.86 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (-9.38%)</td><td>0.02 (-11.93%)</td><td>0.03 (-7.61%)</td><td>0.01 <b>(-24.30%)</b></td><td>0.01 (+18.48%)</td><td>663.90 <b>(+32.09%)</b></td><td>399.80 (+18.73%)</td><td>322.10 (+8.23%)</td><td>294.50 (+10.34%)</td><td>156.72 <b>(+64.01%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.60 (n/a)</td><td>336.74 (n/a)</td><td>297.60 (n/a)</td><td>266.90 (n/a)</td><td>95.55 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (-3.93%)</td><td>0.02 (-13.99%)</td><td>0.03 (+1.61%)</td><td>0.00 <b>(-74.70%)</b></td><td>0.01 <b>(+53.70%)</b></td><td>1880.50 <b>(+295.31%)</b></td><td>626.76 <b>(+90.47%)</b></td><td>294.30 (-1.60%)</td><td>236.10 (+4.10%)</td><td>705.97 <b>(+578.63%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>475.70 (n/a)</td><td>329.06 (n/a)</td><td>299.10 (n/a)</td><td>226.80 (n/a)</td><td>104.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (+4.27%)</td><td>0.02 <b>(-21.50%)</b></td><td>0.01 <b>(-48.78%)</b></td><td>0.00 <b>(-70.05%)</b></td><td>0.01 <b>(+52.78%)</b></td><td>1946.90 <b>(+233.89%)</b></td><td>757.54 <b>(+90.97%)</b></td><td>580.50 <b>(+95.26%)</b></td><td>266.30 (-4.11%)</td><td>692.98 <b>(+359.26%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.10 (n/a)</td><td>396.68 (n/a)</td><td>297.30 (n/a)</td><td>277.70 (n/a)</td><td>150.89 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (-11.13%)</td><td>0.02 (-8.88%)</td><td>0.02 (+7.05%)</td><td>0.02 <b>(+29.50%)</b></td><td>0.01 <b>(-46.41%)</b></td><td>522.10 <b>(-22.78%)</b></td><td>436.90 (-4.45%)</td><td>476.00 (-6.59%)</td><td>274.00 (+12.53%)</td><td>96.55 <b>(-52.31%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>676.10 (n/a)</td><td>457.24 (n/a)</td><td>509.60 (n/a)</td><td>243.50 (n/a)</td><td>202.44 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 <b>(+44.15%)</b></td><td>0.02 (+17.08%)</td><td>0.02 (+1.04%)</td><td>0.01 (+0.91%)</td><td>0.01 <b>(+88.58%)</b></td><td>624.70 (-0.89%)</td><td>458.58 (-8.97%)</td><td>474.90 (-1.02%)</td><td>233.50 <b>(-30.63%)</b></td><td>152.11 <b>(+20.44%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>630.30 (n/a)</td><td>503.78 (n/a)</td><td>479.80 (n/a)</td><td>336.60 (n/a)</td><td>126.30 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 <b>(+36.16%)</b></td><td>0.02 (+18.57%)</td><td>0.01 (+2.74%)</td><td>0.01 <b>(+30.58%)</b></td><td>0.01 <b>(+60.78%)</b></td><td>636.40 <b>(-23.43%)</b></td><td>511.74 (-13.99%)</td><td>560.80 (-2.67%)</td><td>309.50 <b>(-26.55%)</b></td><td>130.97 (-12.66%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>831.10 (n/a)</td><td>594.98 (n/a)</td><td>576.20 (n/a)</td><td>421.40 (n/a)</td><td>149.95 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.05 <b>(+48.45%)</b></td><td>0.03 <b>(+23.83%)</b></td><td>0.03 (-5.68%)</td><td>0.02 <b>(+129.44%)</b></td><td>0.01 (+17.95%)</td><td>489.40 <b>(-56.42%)</b></td><td>349.14 <b>(-31.14%)</b></td><td>323.70 (+5.99%)</td><td>176.60 <b>(-32.62%)</b></td><td>126.69 <b>(-65.08%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1122.90 (n/a)</td><td>507.02 (n/a)</td><td>305.40 (n/a)</td><td>262.10 (n/a)</td><td>362.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 <b>(-23.57%)</b></td><td>0.03 (+8.82%)</td><td>0.03 <b>(+29.46%)</b></td><td>0.02 <b>(+20.95%)</b></td><td>0.00 <b>(-63.41%)</b></td><td>512.60 (-17.32%)</td><td>452.44 (-14.14%)</td><td>446.80 <b>(-22.77%)</b></td><td>379.30 <b>(+30.84%)</b></td><td>56.48 <b>(-58.11%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>620.00 (n/a)</td><td>526.94 (n/a)</td><td>578.50 (n/a)</td><td>289.90 (n/a)</td><td>134.84 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (+5.76%)</td><td>0.02 (+0.05%)</td><td>0.02 (+8.72%)</td><td>0.01 (+6.54%)</td><td>0.01 (+1.28%)</td><td>600.60 (-6.14%)</td><td>429.92 (-0.13%)</td><td>406.60 (-8.01%)</td><td>236.50 (-5.44%)</td><td>165.18 (-1.11%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>639.90 (n/a)</td><td>430.46 (n/a)</td><td>442.00 (n/a)</td><td>250.10 (n/a)</td><td>167.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 <b>(+25.57%)</b></td><td>0.03 <b>(+26.30%)</b></td><td>0.02 (+17.52%)</td><td>0.02 (-3.27%)</td><td>0.01 <b>(+89.67%)</b></td><td>633.90 (+3.38%)</td><td>416.14 (-15.58%)</td><td>415.70 (-14.92%)</td><td>275.10 <b>(-20.35%)</b></td><td>149.72 <b>(+50.15%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>613.20 (n/a)</td><td>492.92 (n/a)</td><td>488.60 (n/a)</td><td>345.40 (n/a)</td><td>99.72 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (+8.87%)</td><td>0.02 (-7.37%)</td><td>0.02 (-15.19%)</td><td>0.01 <b>(-26.40%)</b></td><td>0.01 <b>(+67.59%)</b></td><td>566.10 <b>(+35.89%)</b></td><td>411.16 (+17.70%)</td><td>443.20 (+17.90%)</td><td>225.90 (-8.13%)</td><td>146.90 <b>(+113.57%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>416.60 (n/a)</td><td>349.32 (n/a)</td><td>375.90 (n/a)</td><td>245.90 (n/a)</td><td>68.78 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.05 <b>(+28.59%)</b></td><td>0.02 (-5.17%)</td><td>0.02 (-17.88%)</td><td>0.02 (-1.85%)</td><td>0.01 <b>(+36.20%)</b></td><td>618.00 (+1.90%)</td><td>476.62 (+9.46%)</td><td>516.10 <b>(+21.78%)</b></td><td>212.70 <b>(-22.23%)</b></td><td>158.28 (+1.01%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>606.50 (n/a)</td><td>435.42 (n/a)</td><td>423.80 (n/a)</td><td>273.50 (n/a)</td><td>156.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 (+11.60%)</td><td>0.02 (-1.10%)</td><td>0.02 (+1.54%)</td><td>0.01 <b>(-22.21%)</b></td><td>0.01 <b>(+37.97%)</b></td><td>760.50 <b>(+28.57%)</b></td><td>440.30 (+11.94%)</td><td>414.30 (-1.52%)</td><td>215.50 (-10.43%)</td><td>218.15 <b>(+59.71%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.50 (n/a)</td><td>393.32 (n/a)</td><td>420.70 (n/a)</td><td>240.60 (n/a)</td><td>136.60 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.04 <b>(+24.47%)</b></td><td>0.02 (-4.01%)</td><td>0.02 (-17.03%)</td><td>0.01 (-17.99%)</td><td>0.01 <b>(+81.28%)</b></td><td>679.70 <b>(+21.94%)</b></td><td>509.14 (+13.04%)</td><td>551.10 <b>(+20.54%)</b></td><td>243.20 (-19.68%)</td><td>160.89 <b>(+66.66%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>557.40 (n/a)</td><td>450.40 (n/a)</td><td>457.20 (n/a)</td><td>302.80 (n/a)</td><td>96.54 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 <b>(-23.97%)</b></td><td>0.02 (-1.07%)</td><td>0.02 (+6.14%)</td><td>0.01 (+11.73%)</td><td>0.01 <b>(-27.29%)</b></td><td>558.30 (-10.50%)</td><td>403.50 (-3.04%)</td><td>387.40 (-5.79%)</td><td>275.50 <b>(+31.50%)</b></td><td>132.40 (-12.96%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.80 (n/a)</td><td>416.16 (n/a)</td><td>411.20 (n/a)</td><td>209.50 (n/a)</td><td>152.11 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (-14.87%)</td><td>0.02 (+3.49%)</td><td>0.02 <b>(+28.12%)</b></td><td>0.01 <b>(-20.99%)</b></td><td>0.01 (-7.34%)</td><td>628.70 <b>(+26.58%)</b></td><td>433.80 (-2.28%)</td><td>376.00 <b>(-21.96%)</b></td><td>342.60 (+17.45%)</td><td>120.25 <b>(+40.20%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.70 (n/a)</td><td>443.90 (n/a)</td><td>481.80 (n/a)</td><td>291.70 (n/a)</td><td>85.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.03 (-8.26%)</td><td>0.02 (-19.25%)</td><td>0.02 <b>(-22.93%)</b></td><td>0.01 (-10.63%)</td><td>0.01 (+3.35%)</td><td>572.10 (+11.89%)</td><td>483.64 <b>(+25.37%)</b></td><td>518.20 <b>(+29.74%)</b></td><td>292.10 (+8.99%)</td><td>109.77 <b>(+21.21%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.30 (n/a)</td><td>385.76 (n/a)</td><td>399.40 (n/a)</td><td>268.00 (n/a)</td><td>90.56 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.38 (+3.45%)</td><td>0.26 (+7.62%)</td><td>0.31 <b>(+53.52%)</b></td><td>0.05 <b>(-70.93%)</b></td><td>0.14 <b>(+53.34%)</b></td><td>2043.20 <b>(+244.03%)</b></td><td>677.16 <b>(+51.04%)</b></td><td>314.10 <b>(-34.85%)</b></td><td>256.80 (-3.31%)</td><td>770.83 <b>(+401.85%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.37 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>593.90 (n/a)</td><td>448.32 (n/a)</td><td>482.10 (n/a)</td><td>265.60 (n/a)</td><td>153.60 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.51 (-12.37%)</td><td>0.37 <b>(+58.63%)</b></td><td>0.40 <b>(+111.30%)</b></td><td>0.20 <b>(+294.41%)</b></td><td>0.11 <b>(-43.60%)</b></td><td>502.80 <b>(-74.65%)</b></td><td>292.60 <b>(-61.47%)</b></td><td>247.40 <b>(-52.68%)</b></td><td>194.10 (+14.11%)</td><td>121.24 <b>(-82.82%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.58 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>0.20 (n/a)</td><td>1983.30 (n/a)</td><td>759.48 (n/a)</td><td>522.80 (n/a)</td><td>170.10 (n/a)</td><td>705.76 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.44 <b>(+61.73%)</b></td><td>0.30 <b>(+47.09%)</b></td><td>0.33 <b>(+78.67%)</b></td><td>0.17 (+2.32%)</td><td>0.12 <b>(+172.96%)</b></td><td>592.00 (-2.28%)</td><td>382.00 <b>(-23.31%)</b></td><td>302.30 <b>(-44.03%)</b></td><td>221.60 <b>(-38.17%)</b></td><td>171.27 <b>(+74.29%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>605.80 (n/a)</td><td>498.08 (n/a)</td><td>540.10 (n/a)</td><td>358.40 (n/a)</td><td>98.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.28 <b>(-24.68%)</b></td><td>0.22 <b>(-25.26%)</b></td><td>0.24 (-18.03%)</td><td>0.14 <b>(-40.16%)</b></td><td>0.07 <b>(+30.95%)</b></td><td>527.10 <b>(+67.12%)</b></td><td>373.70 <b>(+43.93%)</b></td><td>306.30 <b>(+22.03%)</b></td><td>260.50 <b>(+32.77%)</b></td><td>135.24 <b>(+194.97%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>315.40 (n/a)</td><td>259.64 (n/a)</td><td>251.00 (n/a)</td><td>196.20 (n/a)</td><td>45.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.32 (+7.55%)</td><td>0.23 (+14.16%)</td><td>0.29 <b>(+71.51%)</b></td><td>0.13 (+9.00%)</td><td>0.10 (+13.89%)</td><td>567.60 (-8.26%)</td><td>371.40 (-9.41%)</td><td>251.70 <b>(-41.68%)</b></td><td>230.30 (-7.02%)</td><td>175.84 (+9.48%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>618.70 (n/a)</td><td>410.00 (n/a)</td><td>431.60 (n/a)</td><td>247.70 (n/a)</td><td>160.61 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.30 (-0.08%)</td><td>0.20 <b>(+22.35%)</b></td><td>0.21 <b>(+57.72%)</b></td><td>0.12 (+8.74%)</td><td>0.08 (-1.03%)</td><td>598.40 (-8.04%)</td><td>415.52 (-18.36%)</td><td>354.30 <b>(-36.60%)</b></td><td>247.00 (+0.08%)</td><td>164.24 (-0.67%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.30 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>650.70 (n/a)</td><td>508.96 (n/a)</td><td>558.80 (n/a)</td><td>246.80 (n/a)</td><td>165.35 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.55 <b>(+32.49%)</b></td><td>0.37 <b>(+34.82%)</b></td><td>0.32 <b>(+23.06%)</b></td><td>0.22 (+18.56%)</td><td>0.14 <b>(+56.26%)</b></td><td>583.00 (-15.65%)</td><td>400.52 <b>(-22.84%)</b></td><td>408.60 (-18.75%)</td><td>236.90 <b>(-24.51%)</b></td><td>142.88 (+1.08%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.42 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>691.20 (n/a)</td><td>519.06 (n/a)</td><td>502.90 (n/a)</td><td>313.80 (n/a)</td><td>141.35 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.49 (-17.47%)</td><td>0.35 (+15.55%)</td><td>0.29 (+12.26%)</td><td>0.23 <b>(+52.07%)</b></td><td>0.12 <b>(-27.56%)</b></td><td>570.70 <b>(-34.24%)</b></td><td>411.66 <b>(-21.70%)</b></td><td>459.10 (-10.92%)</td><td>266.50 <b>(+21.19%)</b></td><td>134.91 <b>(-41.82%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.60 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>867.80 (n/a)</td><td>525.76 (n/a)</td><td>515.40 (n/a)</td><td>219.90 (n/a)</td><td>231.89 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.34 <b>(-21.38%)</b></td><td>0.29 (+4.45%)</td><td>0.28 (+4.17%)</td><td>0.24 <b>(+21.40%)</b></td><td>0.04 <b>(-55.17%)</b></td><td>538.20 (-17.63%)</td><td>454.48 (-9.46%)</td><td>475.00 (-4.00%)</td><td>380.50 <b>(+27.17%)</b></td><td>64.33 <b>(-52.26%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.44 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>653.40 (n/a)</td><td>501.94 (n/a)</td><td>494.80 (n/a)</td><td>299.20 (n/a)</td><td>134.75 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.00 (-12.50%)</td><td>0.00 <b>(-38.71%)</b></td><td>0.00 <b>(-66.67%)</b></td><td>0.00 <b>(-50.00%)</b></td><td>0.00 <b>(+67.87%)</b></td><td>22329.93 <b>(+116.75%)</b></td><td>15477.94 <b>(+123.54%)</b></td><td>20933.44 <b>(+221.87%)</b></td><td>5717.79 (+7.71%)</td><td>8304.94 <b>(+325.34%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>10302.30 (n/a)</td><td>6924.09 (n/a)</td><td>6503.73 (n/a)</td><td>5308.59 (n/a)</td><td>1952.55 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.00 (-15.38%)</td><td>0.00 (+16.13%)</td><td>0.00 (+20.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-18.77%)</td><td>21199.65 (-1.86%)</td><td>13604.77 (-17.14%)</td><td>14204.05 (-18.26%)</td><td>7534.07 <b>(+20.38%)</b></td><td>5939.55 (-3.66%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21600.47 (n/a)</td><td>16419.12 (n/a)</td><td>17377.31 (n/a)</td><td>6258.70 (n/a)</td><td>6164.95 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>0.14 (-7.18%)</td><td>0.11 (+15.50%)</td><td>0.12 <b>(+45.67%)</b></td><td>0.08 (+14.54%)</td><td>0.02 (-18.29%)</td><td>24876.33 (-12.65%)</td><td>19286.40 (-15.25%)</td><td>17297.26 <b>(-31.41%)</b></td><td>15293.44 (+7.71%)</td><td>4476.13 <b>(-21.51%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28479.25 (n/a)</td><td>22758.06 (n/a)</td><td>25219.72 (n/a)</td><td>14198.62 (n/a)</td><td>5702.61 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>1.44 (n/a)</td><td>1.00 (n/a)</td><td>0.89 (n/a)</td><td>0.83 (n/a)</td><td>0.26 (n/a)</td><td>630.40 (n/a)</td><td>546.34 (n/a)</td><td>589.80 (n/a)</td><td>362.90 (n/a)</td><td>109.01 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>2.44 (n/a)</td><td>1.32 (n/a)</td><td>1.55 (n/a)</td><td>0.29 (n/a)</td><td>0.99 (n/a)</td><td>3566.50 (n/a)</td><td>1740.52 (n/a)</td><td>676.80 (n/a)</td><td>429.20 (n/a)</td><td>1643.15 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:29:16</td><td>1.28 (n/a)</td><td>1.04 (n/a)</td><td>1.07 (n/a)</td><td>0.76 (n/a)</td><td>0.19 (n/a)</td><td>689.90 (n/a)</td><td>521.62 (n/a)</td><td>491.70 (n/a)</td><td>408.10 (n/a)</td><td>105.17 (n/a)</td>
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
