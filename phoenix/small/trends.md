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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.06 <b>(+23.71%)</b></td><td>0.04 (+19.92%)</td><td>0.03 (-1.28%)</td><td>0.02 (+12.62%)</td><td>0.02 <b>(+44.58%)</b></td><td>526.20 (-11.20%)</td><td>367.14 (-12.73%)</td><td>422.00 (+1.30%)</td><td>196.60 (-19.13%)</td><td>140.03 (+2.86%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>592.60 (n/a)</td><td>420.68 (n/a)</td><td>416.60 (n/a)</td><td>243.10 (n/a)</td><td>136.14 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.06 (-10.32%)</td><td>0.04 <b>(+26.14%)</b></td><td>0.05 <b>(+126.23%)</b></td><td>0.02 (+9.00%)</td><td>0.02 (-15.97%)</td><td>553.20 (-8.26%)</td><td>333.38 <b>(-25.04%)</b></td><td>238.80 <b>(-55.79%)</b></td><td>222.60 (+11.52%)</td><td>146.08 (-19.92%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>603.00 (n/a)</td><td>444.76 (n/a)</td><td>540.20 (n/a)</td><td>199.60 (n/a)</td><td>182.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.06 <b>(+24.02%)</b></td><td>0.04 (+9.13%)</td><td>0.04 (-2.74%)</td><td>0.02 (-13.65%)</td><td>0.01 <b>(+38.52%)</b></td><td>566.20 (+15.81%)</td><td>338.98 (-4.27%)</td><td>307.70 (+2.81%)</td><td>206.00 (-19.37%)</td><td>134.70 <b>(+33.40%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>488.90 (n/a)</td><td>354.10 (n/a)</td><td>299.30 (n/a)</td><td>255.50 (n/a)</td><td>100.98 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (-17.06%)</td><td>0.01 <b>(-28.25%)</b></td><td>0.01 <b>(-45.93%)</b></td><td>0.01 (-13.35%)</td><td>0.00 <b>(-21.06%)</b></td><td>534.80 (+15.41%)</td><td>438.50 <b>(+38.66%)</b></td><td>499.70 <b>(+84.94%)</b></td><td>286.70 <b>(+20.56%)</b></td><td>115.38 (+16.60%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.40 (n/a)</td><td>316.24 (n/a)</td><td>270.20 (n/a)</td><td>237.80 (n/a)</td><td>98.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (+1.32%)</td><td>0.02 (-9.17%)</td><td>0.01 <b>(-30.26%)</b></td><td>0.01 <b>(+28.63%)</b></td><td>0.01 (+3.75%)</td><td>464.40 <b>(-22.26%)</b></td><td>366.72 (+7.74%)</td><td>419.50 <b>(+43.37%)</b></td><td>228.50 (-1.34%)</td><td>108.31 <b>(-25.80%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.40 (n/a)</td><td>340.38 (n/a)</td><td>292.60 (n/a)</td><td>231.60 (n/a)</td><td>145.98 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (-4.84%)</td><td>0.01 <b>(-32.36%)</b></td><td>0.01 <b>(-44.08%)</b></td><td>0.01 (-5.02%)</td><td>0.01 (-1.25%)</td><td>605.00 (+5.29%)</td><td>478.08 <b>(+47.63%)</b></td><td>485.20 <b>(+78.84%)</b></td><td>247.10 (+5.10%)</td><td>142.91 (+0.67%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.60 (n/a)</td><td>323.84 (n/a)</td><td>271.30 (n/a)</td><td>235.10 (n/a)</td><td>141.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (+3.28%)</td><td>0.01 (+3.08%)</td><td>0.01 (+3.30%)</td><td>0.01 <b>(+69.25%)</b></td><td>0.00 <b>(-29.78%)</b></td><td>474.90 <b>(-40.92%)</b></td><td>384.58 (-15.48%)</td><td>374.90 (-3.20%)</td><td>234.80 (-3.18%)</td><td>96.66 <b>(-58.94%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>803.80 (n/a)</td><td>455.02 (n/a)</td><td>387.30 (n/a)</td><td>242.50 (n/a)</td><td>235.43 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (+5.05%)</td><td>0.02 (+4.83%)</td><td>0.01 (-2.29%)</td><td>0.01 <b>(+310.67%)</b></td><td>0.00 <b>(-37.99%)</b></td><td>487.50 <b>(-75.65%)</b></td><td>364.96 <b>(-43.45%)</b></td><td>363.60 (+2.34%)</td><td>238.40 (-4.79%)</td><td>103.37 <b>(-86.41%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2002.10 (n/a)</td><td>645.36 (n/a)</td><td>355.30 (n/a)</td><td>250.40 (n/a)</td><td>760.46 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.01 <b>(-44.50%)</b></td><td>0.01 <b>(-36.42%)</b></td><td>0.01 <b>(-37.61%)</b></td><td>0.01 (-12.45%)</td><td>0.00 <b>(-57.05%)</b></td><td>665.20 (+14.22%)</td><td>533.56 <b>(+49.18%)</b></td><td>493.40 <b>(+60.30%)</b></td><td>438.00 <b>(+80.17%)</b></td><td>108.19 (-17.56%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.40 (n/a)</td><td>357.66 (n/a)</td><td>307.80 (n/a)</td><td>243.10 (n/a)</td><td>131.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>439.30 (n/a)</td><td>287.82 (n/a)</td><td>253.30 (n/a)</td><td>237.40 (n/a)</td><td>85.47 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>520.10 (n/a)</td><td>438.86 (n/a)</td><td>455.60 (n/a)</td><td>377.90 (n/a)</td><td>59.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.50 (n/a)</td><td>391.64 (n/a)</td><td>424.30 (n/a)</td><td>280.70 (n/a)</td><td>91.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>561.70 (n/a)</td><td>350.12 (n/a)</td><td>288.70 (n/a)</td><td>251.40 (n/a)</td><td>127.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>620.00 (n/a)</td><td>328.46 (n/a)</td><td>253.70 (n/a)</td><td>242.60 (n/a)</td><td>163.73 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>363.50 (n/a)</td><td>280.46 (n/a)</td><td>256.40 (n/a)</td><td>236.00 (n/a)</td><td>50.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.20 (n/a)</td><td>425.14 (n/a)</td><td>314.80 (n/a)</td><td>276.50 (n/a)</td><td>174.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>428.10 (n/a)</td><td>277.48 (n/a)</td><td>300.20 (n/a)</td><td>137.30 (n/a)</td><td>108.75 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.90 (n/a)</td><td>362.94 (n/a)</td><td>319.30 (n/a)</td><td>242.40 (n/a)</td><td>126.33 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.40 (n/a)</td><td>380.58 (n/a)</td><td>285.50 (n/a)</td><td>200.70 (n/a)</td><td>177.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.40 (n/a)</td><td>380.88 (n/a)</td><td>351.10 (n/a)</td><td>230.50 (n/a)</td><td>127.60 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.90 (n/a)</td><td>416.92 (n/a)</td><td>416.10 (n/a)</td><td>244.70 (n/a)</td><td>119.78 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.52 <b>(-33.87%)</b></td><td>0.39 <b>(-22.46%)</b></td><td>0.39 <b>(-22.07%)</b></td><td>0.22 <b>(-28.87%)</b></td><td>0.12 <b>(-34.96%)</b></td><td>1013.80 <b>(+40.59%)</b></td><td>617.22 <b>(+28.27%)</b></td><td>565.80 <b>(+28.33%)</b></td><td>426.50 <b>(+51.19%)</b></td><td>234.55 <b>(+42.19%)</b></td><td>22.12 <b>(-33.87%)</b></td><td>16.76 <b>(-22.46%)</b></td><td>16.68 <b>(-22.07%)</b></td><td>9.31 <b>(-28.87%)</b></td><td>4.99 <b>(-34.96%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.78 (n/a)</td><td>0.51 (n/a)</td><td>0.50 (n/a)</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>721.10 (n/a)</td><td>481.18 (n/a)</td><td>440.90 (n/a)</td><td>282.10 (n/a)</td><td>164.96 (n/a)</td><td>33.46 (n/a)</td><td>21.61 (n/a)</td><td>21.40 (n/a)</td><td>13.09 (n/a)</td><td>7.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.62 <b>(+26.75%)</b></td><td>0.35 (+6.52%)</td><td>0.35 (-6.07%)</td><td>0.13 <b>(+39.75%)</b></td><td>0.18 (+10.48%)</td><td>1745.30 <b>(-28.44%)</b></td><td>814.80 (-15.88%)</td><td>637.70 (+6.46%)</td><td>355.60 <b>(-21.12%)</b></td><td>537.06 <b>(-35.81%)</b></td><td>26.54 <b>(+26.75%)</b></td><td>15.02 (+6.52%)</td><td>14.80 (-6.07%)</td><td>5.41 <b>(+39.75%)</b></td><td>7.54 (+10.48%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.49 (n/a)</td><td>0.33 (n/a)</td><td>0.37 (n/a)</td><td>0.09 (n/a)</td><td>0.16 (n/a)</td><td>2439.10 (n/a)</td><td>968.62 (n/a)</td><td>599.00 (n/a)</td><td>450.80 (n/a)</td><td>836.68 (n/a)</td><td>20.94 (n/a)</td><td>14.10 (n/a)</td><td>15.75 (n/a)</td><td>3.87 (n/a)</td><td>6.83 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.31 (+1.09%)</td><td>0.30 (+0.27%)</td><td>0.30 (-0.86%)</td><td>0.30 (+0.92%)</td><td>0.00 (-4.01%)</td><td>84368.80 (-0.91%)</td><td>82734.44 (-0.27%)</td><td>82946.40 (+0.87%)</td><td>81300.10 (-1.08%)</td><td>1199.83 (-5.97%)</td><td>211.31 (+1.09%)</td><td>207.69 (+0.27%)</td><td>207.12 (-0.86%)</td><td>203.63 (+0.92%)</td><td>3.01 (-4.01%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>85145.40 (n/a)</td><td>82955.38 (n/a)</td><td>82231.70 (n/a)</td><td>82184.20 (n/a)</td><td>1275.94 (n/a)</td><td>209.04 (n/a)</td><td>207.14 (n/a)</td><td>208.92 (n/a)</td><td>201.77 (n/a)</td><td>3.13 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>1.03 (-0.09%)</td><td>1.02 (+0.46%)</td><td>1.02 (+0.80%)</td><td>0.99 (-0.15%)</td><td>0.02 (+12.89%)</td><td>25383.10 (+0.15%)</td><td>24775.26 (-0.46%)</td><td>24691.10 (-0.80%)</td><td>24424.60 (+0.09%)</td><td>380.00 (+13.35%)</td><td>703.38 (-0.09%)</td><td>693.56 (+0.46%)</td><td>695.79 (+0.80%)</td><td>676.82 (-0.15%)</td><td>10.52 (+12.89%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>0.99 (n/a)</td><td>0.01 (n/a)</td><td>25345.50 (n/a)</td><td>24888.94 (n/a)</td><td>24889.20 (n/a)</td><td>24403.30 (n/a)</td><td>335.25 (n/a)</td><td>704.00 (n/a)</td><td>690.36 (n/a)</td><td>690.25 (n/a)</td><td>677.83 (n/a)</td><td>9.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>2.85 <b>(+33.14%)</b></td><td>1.97 (+19.34%)</td><td>1.78 (+12.77%)</td><td>1.06 <b>(-24.82%)</b></td><td>0.83 <b>(+184.41%)</b></td><td>7571.40 <b>(+33.02%)</b></td><td>4753.40 (-4.67%)</td><td>4530.50 (-11.33%)</td><td>2830.80 <b>(-24.89%)</b></td><td>2046.05 <b>(+168.30%)</b></td><td>746.77 <b>(+33.14%)</b></td><td>517.00 (+19.34%)</td><td>466.60 (+12.77%)</td><td>279.20 <b>(-24.82%)</b></td><td>216.49 <b>(+184.41%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>2.14 (n/a)</td><td>1.65 (n/a)</td><td>1.58 (n/a)</td><td>1.42 (n/a)</td><td>0.29 (n/a)</td><td>5692.10 (n/a)</td><td>4986.06 (n/a)</td><td>5109.20 (n/a)</td><td>3769.00 (n/a)</td><td>762.59 (n/a)</td><td>560.88 (n/a)</td><td>433.22 (n/a)</td><td>413.75 (n/a)</td><td>371.38 (n/a)</td><td>76.12 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.33 (+0.04%)</td><td>0.21 (-2.77%)</td><td>0.19 (-0.92%)</td><td>0.17 (-3.56%)</td><td>0.06 (+6.14%)</td><td>7211.60 (+3.69%)</td><td>6219.64 (+3.71%)</td><td>6529.70 (+0.93%)</td><td>3828.90 (-0.04%)</td><td>1384.34 (+11.69%)</td><td>17.53 (+0.04%)</td><td>11.40 (-2.77%)</td><td>10.28 (-0.92%)</td><td>9.31 (-3.56%)</td><td>3.46 (+6.14%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>6954.80 (n/a)</td><td>5997.28 (n/a)</td><td>6469.50 (n/a)</td><td>3830.40 (n/a)</td><td>1239.42 (n/a)</td><td>17.52 (n/a)</td><td>11.73 (n/a)</td><td>10.37 (n/a)</td><td>9.65 (n/a)</td><td>3.26 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>3.78 (n/a)</td><td>3.60 (n/a)</td><td>3.62 (n/a)</td><td>3.39 (n/a)</td><td>0.14 (n/a)</td><td>3.78 (n/a)</td><td>3.60 (n/a)</td><td>3.61 (n/a)</td><td>3.38 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>7.37 (+7.96%)</td><td>6.52 (+5.62%)</td><td>6.75 (+9.80%)</td><td>5.66 (+3.19%)</td><td>0.80 <b>(+42.59%)</b></td><td>7.36 (+7.96%)</td><td>6.52 (+5.62%)</td><td>6.75 (+9.80%)</td><td>5.66 (+3.19%)</td><td>0.80 <b>(+42.59%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>6.82 (n/a)</td><td>6.18 (n/a)</td><td>6.15 (n/a)</td><td>5.48 (n/a)</td><td>0.56 (n/a)</td><td>6.82 (n/a)</td><td>6.17 (n/a)</td><td>6.14 (n/a)</td><td>5.48 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>14.03 <b>(+45.65%)</b></td><td>9.98 (+17.54%)</td><td>8.14 (-1.51%)</td><td>7.74 (-4.18%)</td><td>2.85 <b>(+342.96%)</b></td><td>14.02 <b>(+45.65%)</b></td><td>9.98 (+17.54%)</td><td>8.13 (-1.51%)</td><td>7.74 (-4.18%)</td><td>2.85 <b>(+342.96%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>9.63 (n/a)</td><td>8.49 (n/a)</td><td>8.26 (n/a)</td><td>8.08 (n/a)</td><td>0.64 (n/a)</td><td>9.62 (n/a)</td><td>8.49 (n/a)</td><td>8.26 (n/a)</td><td>8.07 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>3.94 (n/a)</td><td>3.79 (n/a)</td><td>3.70 (n/a)</td><td>3.69 (n/a)</td><td>0.13 (n/a)</td><td>3.94 (n/a)</td><td>3.79 (n/a)</td><td>3.70 (n/a)</td><td>3.69 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>7.59 (+17.74%)</td><td>6.63 (+10.38%)</td><td>7.06 (+18.03%)</td><td>5.66 (-0.07%)</td><td>0.88 <b>(+166.48%)</b></td><td>7.59 (+17.74%)</td><td>6.63 (+10.38%)</td><td>7.06 (+18.03%)</td><td>5.65 (-0.07%)</td><td>0.88 <b>(+166.48%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>6.45 (n/a)</td><td>6.01 (n/a)</td><td>5.98 (n/a)</td><td>5.66 (n/a)</td><td>0.33 (n/a)</td><td>6.45 (n/a)</td><td>6.00 (n/a)</td><td>5.98 (n/a)</td><td>5.66 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>14.56 <b>(+48.84%)</b></td><td>10.59 <b>(+23.35%)</b></td><td>8.60 (+1.65%)</td><td>7.62 (+8.53%)</td><td>3.35 <b>(+199.79%)</b></td><td>14.55 <b>(+48.84%)</b></td><td>10.59 <b>(+23.35%)</b></td><td>8.60 (+1.65%)</td><td>7.62 (+8.53%)</td><td>3.34 <b>(+199.79%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>9.78 (n/a)</td><td>8.59 (n/a)</td><td>8.46 (n/a)</td><td>7.02 (n/a)</td><td>1.12 (n/a)</td><td>9.77 (n/a)</td><td>8.58 (n/a)</td><td>8.46 (n/a)</td><td>7.02 (n/a)</td><td>1.12 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>3.11 (+6.65%)</td><td>2.29 <b>(+29.41%)</b></td><td>2.75 <b>(+159.98%)</b></td><td>1.16 (+13.52%)</td><td>0.84 (-16.98%)</td><td>3.10 (+6.65%)</td><td>2.29 <b>(+29.41%)</b></td><td>2.74 <b>(+159.98%)</b></td><td>1.15 (+13.52%)</td><td>0.83 (-16.98%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>2.91 (n/a)</td><td>1.77 (n/a)</td><td>1.06 (n/a)</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>2.91 (n/a)</td><td>1.77 (n/a)</td><td>1.05 (n/a)</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.50 (+8.13%)</td><td>0.31 (+15.78%)</td><td>0.32 (+3.63%)</td><td>0.07 (+0.01%)</td><td>0.16 (-2.07%)</td><td>0.49 (+8.13%)</td><td>0.30 (+15.78%)</td><td>0.31 (+3.63%)</td><td>0.07 (+0.01%)</td><td>0.15 (-2.07%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.46 (n/a)</td><td>0.27 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>0.46 (n/a)</td><td>0.26 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.46 <b>(-37.89%)</b></td><td>0.37 <b>(-41.16%)</b></td><td>0.44 <b>(-30.40%)</b></td><td>0.08 <b>(-83.44%)</b></td><td>0.16 <b>(+66.80%)</b></td><td>0.45 <b>(-37.89%)</b></td><td>0.36 <b>(-41.16%)</b></td><td>0.43 <b>(-30.40%)</b></td><td>0.08 <b>(-83.44%)</b></td><td>0.16 <b>(+66.80%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.74 (n/a)</td><td>0.62 (n/a)</td><td>0.63 (n/a)</td><td>0.49 (n/a)</td><td>0.10 (n/a)</td><td>0.73 (n/a)</td><td>0.62 (n/a)</td><td>0.62 (n/a)</td><td>0.48 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>2.65 (-0.53%)</td><td>1.30 <b>(-39.29%)</b></td><td>1.40 <b>(-41.76%)</b></td><td>0.44 <b>(-44.36%)</b></td><td>0.91 <b>(+20.76%)</b></td><td>2.60 (-0.53%)</td><td>1.28 <b>(-39.29%)</b></td><td>1.38 <b>(-41.76%)</b></td><td>0.44 <b>(-44.36%)</b></td><td>0.90 <b>(+20.76%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>2.66 (n/a)</td><td>2.14 (n/a)</td><td>2.40 (n/a)</td><td>0.80 (n/a)</td><td>0.76 (n/a)</td><td>2.62 (n/a)</td><td>2.10 (n/a)</td><td>2.36 (n/a)</td><td>0.79 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.50 (n/a)</td><td>318.08 (n/a)</td><td>299.30 (n/a)</td><td>220.80 (n/a)</td><td>97.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.10 (n/a)</td><td>387.92 (n/a)</td><td>340.50 (n/a)</td><td>285.60 (n/a)</td><td>117.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>346.80 (n/a)</td><td>311.94 (n/a)</td><td>314.40 (n/a)</td><td>261.00 (n/a)</td><td>35.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>519.70 (n/a)</td><td>427.80 (n/a)</td><td>450.20 (n/a)</td><td>317.40 (n/a)</td><td>84.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.00 (n/a)</td><td>402.56 (n/a)</td><td>350.60 (n/a)</td><td>283.60 (n/a)</td><td>134.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>719.90 (n/a)</td><td>559.58 (n/a)</td><td>517.20 (n/a)</td><td>477.00 (n/a)</td><td>96.33 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (-1.48%)</td><td>0.02 (-8.26%)</td><td>0.03 (-4.25%)</td><td>0.01 <b>(-23.06%)</b></td><td>0.01 (+8.55%)</td><td>645.20 <b>(+29.98%)</b></td><td>402.86 (+14.53%)</td><td>312.00 (+4.45%)</td><td>244.30 (+1.50%)</td><td>180.18 <b>(+42.77%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.40 (n/a)</td><td>351.74 (n/a)</td><td>298.70 (n/a)</td><td>240.70 (n/a)</td><td>126.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (+0.79%)</td><td>0.02 (+9.45%)</td><td>0.03 <b>(+62.93%)</b></td><td>0.00 <b>(-75.48%)</b></td><td>0.01 <b>(+45.79%)</b></td><td>2066.00 <b>(+307.82%)</b></td><td>634.10 <b>(+58.82%)</b></td><td>286.20 <b>(-38.62%)</b></td><td>242.40 (-0.78%)</td><td>800.73 <b>(+538.86%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.60 (n/a)</td><td>399.26 (n/a)</td><td>466.30 (n/a)</td><td>244.30 (n/a)</td><td>125.34 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 <b>(+44.69%)</b></td><td>0.03 <b>(+30.60%)</b></td><td>0.03 <b>(+29.42%)</b></td><td>0.01 (+5.67%)</td><td>0.01 <b>(+103.91%)</b></td><td>557.30 (-5.37%)</td><td>362.42 (-16.64%)</td><td>305.20 <b>(-22.71%)</b></td><td>211.20 <b>(-30.89%)</b></td><td>151.13 <b>(+35.52%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.90 (n/a)</td><td>434.78 (n/a)</td><td>394.90 (n/a)</td><td>305.60 (n/a)</td><td>111.52 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (+11.85%)</td><td>0.02 (-10.92%)</td><td>0.02 <b>(-30.24%)</b></td><td>0.02 (-12.83%)</td><td>0.01 <b>(+81.33%)</b></td><td>512.30 (+14.71%)</td><td>385.64 <b>(+20.05%)</b></td><td>416.20 <b>(+43.32%)</b></td><td>242.50 (-10.58%)</td><td>127.19 <b>(+78.12%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>446.60 (n/a)</td><td>321.22 (n/a)</td><td>290.40 (n/a)</td><td>271.20 (n/a)</td><td>71.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (-6.60%)</td><td>0.02 (-7.14%)</td><td>0.02 (-9.49%)</td><td>0.01 <b>(+73.72%)</b></td><td>0.01 (-13.87%)</td><td>1092.50 <b>(-42.44%)</b></td><td>588.68 (-15.83%)</td><td>505.90 (+10.48%)</td><td>244.90 (+7.08%)</td><td>313.44 <b>(-53.76%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1897.90 (n/a)</td><td>699.36 (n/a)</td><td>457.90 (n/a)</td><td>228.70 (n/a)</td><td>677.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (-0.05%)</td><td>0.02 (-10.76%)</td><td>0.01 (-15.94%)</td><td>0.01 (-11.47%)</td><td>0.01 (+9.51%)</td><td>640.60 (+12.96%)</td><td>518.94 (+13.61%)</td><td>558.80 (+18.97%)</td><td>300.10 (+0.07%)</td><td>129.08 (+13.54%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.10 (n/a)</td><td>456.78 (n/a)</td><td>469.70 (n/a)</td><td>299.90 (n/a)</td><td>113.68 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 <b>(+66.02%)</b></td><td>0.02 (+4.84%)</td><td>0.01 <b>(-20.20%)</b></td><td>0.01 <b>(-34.11%)</b></td><td>0.02 <b>(+198.79%)</b></td><td>781.80 <b>(+51.78%)</b></td><td>528.20 <b>(+20.30%)</b></td><td>595.00 <b>(+25.32%)</b></td><td>174.20 <b>(-39.74%)</b></td><td>227.97 <b>(+158.55%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.10 (n/a)</td><td>439.08 (n/a)</td><td>474.80 (n/a)</td><td>289.10 (n/a)</td><td>88.17 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 <b>(+89.36%)</b></td><td>0.02 <b>(+42.87%)</b></td><td>0.02 (+13.69%)</td><td>0.01 (+15.09%)</td><td>0.01 <b>(+477.92%)</b></td><td>576.80 (-13.11%)</td><td>457.12 <b>(-24.44%)</b></td><td>539.80 (-12.04%)</td><td>292.40 <b>(-47.19%)</b></td><td>135.03 <b>(+171.73%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>663.80 (n/a)</td><td>604.96 (n/a)</td><td>613.70 (n/a)</td><td>553.70 (n/a)</td><td>49.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (+3.33%)</td><td>0.02 (-9.08%)</td><td>0.02 (-19.74%)</td><td>0.01 <b>(-24.55%)</b></td><td>0.01 <b>(+67.87%)</b></td><td>595.10 <b>(+32.54%)</b></td><td>421.20 (+16.92%)</td><td>462.90 <b>(+24.60%)</b></td><td>273.70 (-3.22%)</td><td>134.05 <b>(+107.70%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>449.00 (n/a)</td><td>360.26 (n/a)</td><td>371.50 (n/a)</td><td>282.80 (n/a)</td><td>64.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 <b>(+51.87%)</b></td><td>0.02 (+4.16%)</td><td>0.02 <b>(-25.47%)</b></td><td>0.01 (-2.72%)</td><td>0.01 <b>(+114.42%)</b></td><td>546.50 (+2.80%)</td><td>412.76 (+8.80%)</td><td>493.80 <b>(+34.18%)</b></td><td>175.40 <b>(-34.13%)</b></td><td>162.70 <b>(+50.88%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.60 (n/a)</td><td>379.36 (n/a)</td><td>368.00 (n/a)</td><td>266.30 (n/a)</td><td>107.84 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 <b>(+96.41%)</b></td><td>0.02 <b>(+43.32%)</b></td><td>0.02 (+16.24%)</td><td>0.01 (-8.22%)</td><td>0.01 <b>(+525.45%)</b></td><td>627.50 (+8.96%)</td><td>408.10 <b>(-20.61%)</b></td><td>442.60 (-13.97%)</td><td>227.00 <b>(-49.09%)</b></td><td>161.23 <b>(+237.19%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>575.90 (n/a)</td><td>514.04 (n/a)</td><td>514.50 (n/a)</td><td>445.90 (n/a)</td><td>47.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 <b>(+42.31%)</b></td><td>0.02 <b>(+38.89%)</b></td><td>0.02 <b>(+36.46%)</b></td><td>0.01 <b>(+83.46%)</b></td><td>0.01 <b>(+40.90%)</b></td><td>579.60 <b>(-45.50%)</b></td><td>409.40 <b>(-30.26%)</b></td><td>384.30 <b>(-26.72%)</b></td><td>232.60 <b>(-29.73%)</b></td><td>144.49 <b>(-48.15%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1063.40 (n/a)</td><td>587.00 (n/a)</td><td>524.40 (n/a)</td><td>331.00 (n/a)</td><td>278.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (+18.96%)</td><td>0.02 (+17.74%)</td><td>0.02 (-0.68%)</td><td>0.01 <b>(+26.98%)</b></td><td>0.01 <b>(+36.81%)</b></td><td>648.30 <b>(-21.25%)</b></td><td>450.58 (-13.62%)</td><td>481.90 (+0.69%)</td><td>274.40 (-15.93%)</td><td>155.83 (-15.14%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>823.20 (n/a)</td><td>521.62 (n/a)</td><td>478.60 (n/a)</td><td>326.40 (n/a)</td><td>183.63 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (+13.20%)</td><td>0.02 (-3.42%)</td><td>0.01 (-17.86%)</td><td>0.01 (+1.68%)</td><td>0.00 <b>(+56.33%)</b></td><td>590.20 (-1.65%)</td><td>500.24 (+6.39%)</td><td>564.80 <b>(+21.75%)</b></td><td>323.30 (-11.64%)</td><td>113.33 <b>(+35.19%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>600.10 (n/a)</td><td>470.18 (n/a)</td><td>463.90 (n/a)</td><td>365.90 (n/a)</td><td>83.83 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 <b>(-22.16%)</b></td><td>0.02 (-19.03%)</td><td>0.02 <b>(-28.72%)</b></td><td>0.02 (+9.26%)</td><td>0.00 <b>(-41.70%)</b></td><td>519.00 (-8.48%)</td><td>404.50 (+17.49%)</td><td>413.50 <b>(+40.26%)</b></td><td>325.40 <b>(+28.46%)</b></td><td>79.68 <b>(-37.33%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.10 (n/a)</td><td>344.28 (n/a)</td><td>294.80 (n/a)</td><td>253.30 (n/a)</td><td>127.13 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 (+4.53%)</td><td>0.04 (-8.38%)</td><td>0.04 (-9.91%)</td><td>0.02 (-18.04%)</td><td>0.02 <b>(+42.23%)</b></td><td>609.20 <b>(+22.01%)</b></td><td>394.32 (+19.34%)</td><td>338.00 (+11.00%)</td><td>234.40 (-4.33%)</td><td>175.82 <b>(+67.29%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>499.30 (n/a)</td><td>330.42 (n/a)</td><td>304.50 (n/a)</td><td>245.00 (n/a)</td><td>105.10 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 (+16.89%)</td><td>0.02 (-7.62%)</td><td>0.02 (-17.21%)</td><td>0.01 (-2.57%)</td><td>0.01 (+12.61%)</td><td>607.50 (+2.65%)</td><td>432.94 (+7.83%)</td><td>476.40 <b>(+20.76%)</b></td><td>182.00 (-14.43%)</td><td>156.22 (-11.79%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.80 (n/a)</td><td>401.52 (n/a)</td><td>394.50 (n/a)</td><td>212.70 (n/a)</td><td>177.10 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (+0.69%)</td><td>0.03 (+14.71%)</td><td>0.02 (+0.53%)</td><td>0.02 <b>(+65.03%)</b></td><td>0.01 (-5.25%)</td><td>632.30 <b>(-39.40%)</b></td><td>431.40 <b>(-21.70%)</b></td><td>447.10 (-0.53%)</td><td>248.30 (-0.68%)</td><td>174.40 <b>(-45.68%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1043.40 (n/a)</td><td>550.98 (n/a)</td><td>449.50 (n/a)</td><td>250.00 (n/a)</td><td>321.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (-10.68%)</td><td>0.02 (-15.16%)</td><td>0.02 <b>(-30.20%)</b></td><td>0.02 (+3.14%)</td><td>0.01 <b>(-27.70%)</b></td><td>523.40 (-3.04%)</td><td>413.68 (+13.25%)</td><td>437.80 <b>(+43.26%)</b></td><td>275.10 (+11.92%)</td><td>96.70 <b>(-24.02%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.80 (n/a)</td><td>365.28 (n/a)</td><td>305.60 (n/a)</td><td>245.80 (n/a)</td><td>127.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 (+1.65%)</td><td>0.03 (-19.18%)</td><td>0.02 <b>(-35.14%)</b></td><td>0.02 (-18.69%)</td><td>0.01 (+14.49%)</td><td>608.00 <b>(+22.98%)</b></td><td>449.44 <b>(+27.56%)</b></td><td>475.00 <b>(+54.17%)</b></td><td>237.80 (-1.61%)</td><td>139.10 <b>(+28.21%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.40 (n/a)</td><td>352.34 (n/a)</td><td>308.10 (n/a)</td><td>241.70 (n/a)</td><td>108.50 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (+4.70%)</td><td>0.02 <b>(+31.11%)</b></td><td>0.03 <b>(+67.74%)</b></td><td>0.01 <b>(+69.07%)</b></td><td>0.01 (-15.85%)</td><td>596.10 <b>(-40.85%)</b></td><td>388.30 <b>(-33.84%)</b></td><td>298.20 <b>(-40.38%)</b></td><td>257.30 (-4.49%)</td><td>153.98 <b>(-52.42%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1007.80 (n/a)</td><td>586.94 (n/a)</td><td>500.20 (n/a)</td><td>269.40 (n/a)</td><td>323.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.05 <b>(+66.29%)</b></td><td>0.03 <b>(+37.26%)</b></td><td>0.02 (+15.35%)</td><td>0.02 <b>(+36.18%)</b></td><td>0.02 <b>(+76.47%)</b></td><td>608.30 <b>(-26.57%)</b></td><td>390.24 <b>(-22.65%)</b></td><td>408.30 (-13.31%)</td><td>173.30 <b>(-39.87%)</b></td><td>183.23 (-18.86%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>828.40 (n/a)</td><td>504.48 (n/a)</td><td>471.00 (n/a)</td><td>288.20 (n/a)</td><td>225.83 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.03 (-6.13%)</td><td>0.02 (-12.78%)</td><td>0.02 <b>(-32.67%)</b></td><td>0.01 (-1.22%)</td><td>0.01 (-19.37%)</td><td>568.40 (+1.25%)</td><td>416.80 (+9.64%)</td><td>419.60 <b>(+48.53%)</b></td><td>252.30 (+6.50%)</td><td>132.67 (-17.52%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.40 (n/a)</td><td>380.16 (n/a)</td><td>282.50 (n/a)</td><td>236.90 (n/a)</td><td>160.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.04 <b>(+33.87%)</b></td><td>0.02 (+16.32%)</td><td>0.02 (-1.98%)</td><td>0.02 <b>(+128.99%)</b></td><td>0.01 (+0.96%)</td><td>591.60 <b>(-56.33%)</b></td><td>451.38 <b>(-26.72%)</b></td><td>471.50 (+2.01%)</td><td>256.50 <b>(-25.31%)</b></td><td>130.61 <b>(-69.05%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1354.80 (n/a)</td><td>615.98 (n/a)</td><td>462.20 (n/a)</td><td>343.40 (n/a)</td><td>422.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.02 <b>(-24.70%)</b></td><td>0.02 (-13.26%)</td><td>0.02 (-1.30%)</td><td>0.01 (-16.26%)</td><td>0.00 <b>(-38.35%)</b></td><td>663.70 (+19.41%)</td><td>520.58 (+12.14%)</td><td>531.80 (+1.33%)</td><td>357.90 <b>(+32.80%)</b></td><td>114.62 (-1.62%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.80 (n/a)</td><td>464.22 (n/a)</td><td>524.80 (n/a)</td><td>269.50 (n/a)</td><td>116.50 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.45 <b>(+29.08%)</b></td><td>0.24 <b>(-26.69%)</b></td><td>0.23 <b>(-31.16%)</b></td><td>0.09 <b>(-71.11%)</b></td><td>0.13 <b>(+814.36%)</b></td><td>1091.60 <b>(+246.10%)</b></td><td>537.06 <b>(+77.55%)</b></td><td>435.30 <b>(+45.29%)</b></td><td>219.80 <b>(-22.52%)</b></td><td>331.25 <b>(+2411.70%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.01 (n/a)</td><td>315.40 (n/a)</td><td>302.48 (n/a)</td><td>299.60 (n/a)</td><td>283.70 (n/a)</td><td>13.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.40 <b>(+22.31%)</b></td><td>0.28 (+17.99%)</td><td>0.21 (-3.42%)</td><td>0.19 (+12.07%)</td><td>0.10 <b>(+75.21%)</b></td><td>513.30 (-10.78%)</td><td>390.62 (-10.34%)</td><td>459.30 (+3.56%)</td><td>244.50 (-18.23%)</td><td>128.96 <b>(+26.83%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>575.30 (n/a)</td><td>435.68 (n/a)</td><td>443.50 (n/a)</td><td>299.00 (n/a)</td><td>101.68 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.38 <b>(+104.67%)</b></td><td>0.23 <b>(+33.33%)</b></td><td>0.20 (+12.88%)</td><td>0.16 (+2.83%)</td><td>0.09 <b>(+593.14%)</b></td><td>620.30 (-2.76%)</td><td>475.22 (-17.68%)</td><td>503.50 (-11.40%)</td><td>256.90 <b>(-51.14%)</b></td><td>143.03 <b>(+218.89%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>637.90 (n/a)</td><td>577.30 (n/a)</td><td>568.30 (n/a)</td><td>525.80 (n/a)</td><td>44.85 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.27 (+2.61%)</td><td>0.20 (-12.73%)</td><td>0.17 <b>(-29.88%)</b></td><td>0.14 (-6.26%)</td><td>0.06 <b>(+38.24%)</b></td><td>514.00 (+6.68%)</td><td>397.34 (+18.18%)</td><td>443.70 <b>(+42.58%)</b></td><td>273.00 (-2.53%)</td><td>110.11 <b>(+33.48%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>481.80 (n/a)</td><td>336.22 (n/a)</td><td>311.20 (n/a)</td><td>280.10 (n/a)</td><td>82.49 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.26 (-14.31%)</td><td>0.20 (-10.30%)</td><td>0.17 <b>(-30.60%)</b></td><td>0.15 (+13.17%)</td><td>0.05 <b>(-38.71%)</b></td><td>483.60 (-11.64%)</td><td>389.92 (+4.20%)</td><td>429.10 <b>(+44.09%)</b></td><td>279.80 (+16.73%)</td><td>84.47 <b>(-40.28%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>547.30 (n/a)</td><td>374.20 (n/a)</td><td>297.80 (n/a)</td><td>239.70 (n/a)</td><td>141.43 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.28 (+5.30%)</td><td>0.16 (-12.66%)</td><td>0.14 (-14.29%)</td><td>0.04 <b>(-70.26%)</b></td><td>0.11 <b>(+90.67%)</b></td><td>1868.50 <b>(+236.24%)</b></td><td>795.20 <b>(+81.96%)</b></td><td>528.40 (+16.67%)</td><td>259.00 (-5.06%)</td><td>674.93 <b>(+467.10%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>555.70 (n/a)</td><td>437.02 (n/a)</td><td>452.90 (n/a)</td><td>272.80 (n/a)</td><td>119.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.42 (-9.91%)</td><td>0.31 (+0.11%)</td><td>0.27 (-7.85%)</td><td>0.22 (+10.20%)</td><td>0.08 (-17.17%)</td><td>585.00 (-9.26%)</td><td>449.96 (-2.19%)</td><td>478.70 (+8.52%)</td><td>309.50 (+11.01%)</td><td>113.59 (-15.82%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>644.70 (n/a)</td><td>460.02 (n/a)</td><td>441.10 (n/a)</td><td>278.80 (n/a)</td><td>134.93 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.56 (+11.21%)</td><td>0.33 (-3.64%)</td><td>0.28 (-18.41%)</td><td>0.23 <b>(+36.17%)</b></td><td>0.13 (-7.51%)</td><td>561.50 <b>(-26.55%)</b></td><td>430.08 (-2.85%)</td><td>474.10 <b>(+22.57%)</b></td><td>234.90 (-10.07%)</td><td>123.73 <b>(-40.43%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>764.50 (n/a)</td><td>442.70 (n/a)</td><td>386.80 (n/a)</td><td>261.20 (n/a)</td><td>207.70 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.53 (+14.88%)</td><td>0.30 (+8.90%)</td><td>0.24 (+9.59%)</td><td>0.05 (-13.33%)</td><td>0.19 <b>(+20.82%)</b></td><td>2446.10 (+15.38%)</td><td>832.82 (+6.06%)</td><td>540.30 (-8.76%)</td><td>247.20 (-12.96%)</td><td>917.34 <b>(+20.55%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.46 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>0.16 (n/a)</td><td>2120.10 (n/a)</td><td>785.22 (n/a)</td><td>592.20 (n/a)</td><td>284.00 (n/a)</td><td>760.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.00 (-14.29%)</td><td>0.00 <b>(+23.53%)</b></td><td>0.00 <b>(+150.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-6.46%)</td><td>21440.62 (+7.89%)</td><td>12178.71 (-12.61%)</td><td>8612.22 <b>(-48.41%)</b></td><td>6467.20 (+14.90%)</td><td>6953.58 (+16.06%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19872.73 (n/a)</td><td>13935.32 (n/a)</td><td>16694.63 (n/a)</td><td>5628.59 (n/a)</td><td>5991.37 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.00 <b>(-28.57%)</b></td><td>0.00 <b>(-23.26%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-56.73%)</b></td><td>17709.86 (-2.30%)</td><td>13580.99 (+8.77%)</td><td>14220.72 (-3.05%)</td><td>8161.88 <b>(+36.85%)</b></td><td>3461.07 <b>(-41.77%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18126.97 (n/a)</td><td>12485.75 (n/a)</td><td>14667.55 (n/a)</td><td>5964.32 (n/a)</td><td>5944.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>0.13 (-14.72%)</td><td>0.09 (-14.27%)</td><td>0.08 (-15.44%)</td><td>0.08 (+2.56%)</td><td>0.02 <b>(-27.85%)</b></td><td>27575.71 (-2.42%)</td><td>24499.12 (+13.20%)</td><td>26400.37 (+18.24%)</td><td>15799.27 (+17.24%)</td><td>4941.82 (-19.96%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28260.78 (n/a)</td><td>21642.72 (n/a)</td><td>22328.66 (n/a)</td><td>13476.33 (n/a)</td><td>6173.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>1.81 (-1.56%)</td><td>1.36 (-3.01%)</td><td>1.61 (+13.45%)</td><td>0.71 (-14.34%)</td><td>0.46 <b>(+20.44%)</b></td><td>735.70 (+16.76%)</td><td>434.72 (+7.97%)</td><td>326.20 (-11.86%)</td><td>290.20 (+1.58%)</td><td>186.44 <b>(+38.01%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>1.84 (n/a)</td><td>1.40 (n/a)</td><td>1.42 (n/a)</td><td>0.83 (n/a)</td><td>0.38 (n/a)</td><td>630.10 (n/a)</td><td>402.62 (n/a)</td><td>370.10 (n/a)</td><td>285.70 (n/a)</td><td>135.09 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>3.14 <b>(+21.12%)</b></td><td>1.96 (+16.44%)</td><td>1.66 (-2.45%)</td><td>1.32 <b>(+321.73%)</b></td><td>0.77 (-17.69%)</td><td>796.90 <b>(-76.29%)</b></td><td>594.14 <b>(-46.80%)</b></td><td>633.10 (+2.53%)</td><td>334.30 (-17.44%)</td><td>197.39 <b>(-84.38%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>2.59 (n/a)</td><td>1.69 (n/a)</td><td>1.70 (n/a)</td><td>0.31 (n/a)</td><td>0.93 (n/a)</td><td>3360.70 (n/a)</td><td>1116.82 (n/a)</td><td>617.50 (n/a)</td><td>404.90 (n/a)</td><td>1263.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:17:03</td><td>2.01 <b>(+24.14%)</b></td><td>1.25 (+8.63%)</td><td>1.01 (-4.41%)</td><td>0.90 (+12.12%)</td><td>0.48 <b>(+42.31%)</b></td><td>583.10 (-10.81%)</td><td>461.42 (-4.84%)</td><td>521.60 (+4.63%)</td><td>261.10 (-19.44%)</td><td>144.85 (+7.20%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:14:08</td><td>1.62 (n/a)</td><td>1.16 (n/a)</td><td>1.05 (n/a)</td><td>0.80 (n/a)</td><td>0.34 (n/a)</td><td>653.80 (n/a)</td><td>484.90 (n/a)</td><td>498.50 (n/a)</td><td>324.10 (n/a)</td><td>135.12 (n/a)</td>
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
