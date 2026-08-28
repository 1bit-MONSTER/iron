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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (-15.20%)</td><td>0.03 (+1.39%)</td><td>0.03 (+9.16%)</td><td>0.02 (-1.69%)</td><td>0.01 <b>(-28.01%)</b></td><td>514.80 (+1.72%)</td><td>409.44 (-3.77%)</td><td>436.00 (-8.38%)</td><td>291.00 (+17.91%)</td><td>92.91 (-11.03%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.10 (n/a)</td><td>425.46 (n/a)</td><td>475.90 (n/a)</td><td>246.80 (n/a)</td><td>104.44 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 <b>(-51.46%)</b></td><td>0.02 <b>(-27.34%)</b></td><td>0.02 (-5.67%)</td><td>0.02 <b>(+220.24%)</b></td><td>0.00 <b>(-80.92%)</b></td><td>593.10 <b>(-68.77%)</b></td><td>530.82 <b>(-22.48%)</b></td><td>556.80 (+6.02%)</td><td>392.60 <b>(+105.98%)</b></td><td>79.30 <b>(-88.61%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1899.30 (n/a)</td><td>684.72 (n/a)</td><td>525.20 (n/a)</td><td>190.60 (n/a)</td><td>696.23 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 (-19.44%)</td><td>0.03 (-14.76%)</td><td>0.03 <b>(-29.94%)</b></td><td>0.02 (-7.18%)</td><td>0.01 (-16.46%)</td><td>591.00 (+7.73%)</td><td>435.10 (+15.72%)</td><td>475.40 <b>(+42.76%)</b></td><td>266.80 <b>(+24.15%)</b></td><td>152.51 (+3.94%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>548.60 (n/a)</td><td>375.98 (n/a)</td><td>333.00 (n/a)</td><td>214.90 (n/a)</td><td>146.73 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (+5.07%)</td><td>0.02 (-4.98%)</td><td>0.01 <b>(-33.08%)</b></td><td>0.01 (+1.87%)</td><td>0.01 (+5.93%)</td><td>473.00 (-1.83%)</td><td>356.32 (+5.33%)</td><td>412.40 <b>(+49.42%)</b></td><td>222.00 (-4.84%)</td><td>117.58 (-4.96%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>481.80 (n/a)</td><td>338.30 (n/a)</td><td>276.00 (n/a)</td><td>233.30 (n/a)</td><td>123.72 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (+10.13%)</td><td>0.01 <b>(-21.31%)</b></td><td>0.01 <b>(-50.75%)</b></td><td>0.01 (+19.89%)</td><td>0.01 (+0.73%)</td><td>535.50 (-16.59%)</td><td>426.56 <b>(+22.07%)</b></td><td>484.10 <b>(+103.06%)</b></td><td>197.20 (-9.17%)</td><td>133.93 <b>(-26.46%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>642.00 (n/a)</td><td>349.44 (n/a)</td><td>238.40 (n/a)</td><td>217.10 (n/a)</td><td>182.10 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (-10.91%)</td><td>0.01 <b>(-22.91%)</b></td><td>0.01 <b>(-44.57%)</b></td><td>0.01 (-7.52%)</td><td>0.00 (-13.70%)</td><td>548.90 (+8.14%)</td><td>416.94 <b>(+29.00%)</b></td><td>457.30 <b>(+80.39%)</b></td><td>262.20 (+12.29%)</td><td>130.80 (+8.35%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>507.60 (n/a)</td><td>323.20 (n/a)</td><td>253.50 (n/a)</td><td>233.50 (n/a)</td><td>120.72 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 <b>(-22.78%)</b></td><td>0.02 <b>(-21.39%)</b></td><td>0.02 <b>(-24.54%)</b></td><td>0.01 (-12.31%)</td><td>0.00 <b>(-29.59%)</b></td><td>530.90 (+14.02%)</td><td>359.72 <b>(+24.54%)</b></td><td>328.10 <b>(+32.51%)</b></td><td>271.40 <b>(+29.48%)</b></td><td>102.27 (+0.63%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>465.60 (n/a)</td><td>288.84 (n/a)</td><td>247.60 (n/a)</td><td>209.60 (n/a)</td><td>101.64 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (-11.39%)</td><td>0.01 <b>(-20.23%)</b></td><td>0.01 (-8.41%)</td><td>0.01 <b>(-42.13%)</b></td><td>0.01 (-15.44%)</td><td>1016.40 <b>(+72.80%)</b></td><td>560.50 <b>(+30.02%)</b></td><td>515.70 (+9.19%)</td><td>274.10 (+12.84%)</td><td>278.02 <b>(+66.69%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.20 (n/a)</td><td>431.08 (n/a)</td><td>472.30 (n/a)</td><td>242.90 (n/a)</td><td>166.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (-7.71%)</td><td>0.01 (-19.01%)</td><td>0.01 <b>(-23.74%)</b></td><td>0.00 <b>(-50.59%)</b></td><td>0.00 <b>(+23.62%)</b></td><td>1201.50 <b>(+102.41%)</b></td><td>665.28 <b>(+42.01%)</b></td><td>649.50 <b>(+31.13%)</b></td><td>309.20 (+8.34%)</td><td>347.85 <b>(+159.89%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>593.60 (n/a)</td><td>468.48 (n/a)</td><td>495.30 (n/a)</td><td>285.40 (n/a)</td><td>133.84 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>461.00 (n/a)</td><td>387.02 (n/a)</td><td>430.20 (n/a)</td><td>227.70 (n/a)</td><td>93.26 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>591.40 (n/a)</td><td>474.26 (n/a)</td><td>496.60 (n/a)</td><td>294.20 (n/a)</td><td>120.89 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>623.70 (n/a)</td><td>499.86 (n/a)</td><td>500.90 (n/a)</td><td>373.90 (n/a)</td><td>89.54 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>462.90 (n/a)</td><td>329.90 (n/a)</td><td>283.40 (n/a)</td><td>237.10 (n/a)</td><td>96.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1044.10 (n/a)</td><td>447.38 (n/a)</td><td>310.30 (n/a)</td><td>225.00 (n/a)</td><td>339.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.30 (n/a)</td><td>439.86 (n/a)</td><td>443.00 (n/a)</td><td>304.20 (n/a)</td><td>87.09 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.50 (n/a)</td><td>372.20 (n/a)</td><td>289.90 (n/a)</td><td>235.10 (n/a)</td><td>165.27 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.50 (n/a)</td><td>408.14 (n/a)</td><td>409.70 (n/a)</td><td>280.30 (n/a)</td><td>118.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.40 (n/a)</td><td>409.90 (n/a)</td><td>422.40 (n/a)</td><td>278.20 (n/a)</td><td>122.92 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.80 (n/a)</td><td>396.64 (n/a)</td><td>423.30 (n/a)</td><td>201.40 (n/a)</td><td>154.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>439.70 (n/a)</td><td>297.38 (n/a)</td><td>273.10 (n/a)</td><td>210.00 (n/a)</td><td>86.04 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.20 (n/a)</td><td>446.02 (n/a)</td><td>474.90 (n/a)</td><td>224.40 (n/a)</td><td>147.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.51 (-10.77%)</td><td>0.43 (+4.96%)</td><td>0.49 (+4.32%)</td><td>0.31 <b>(+144.02%)</b></td><td>0.09 <b>(-50.54%)</b></td><td>709.70 <b>(-59.02%)</b></td><td>531.24 <b>(-26.76%)</b></td><td>455.80 (-4.14%)</td><td>430.70 (+12.04%)</td><td>121.97 <b>(-78.61%)</b></td><td>21.91 (-10.77%)</td><td>18.46 (+4.96%)</td><td>20.70 (+4.32%)</td><td>13.30 <b>(+144.02%)</b></td><td>3.80 <b>(-50.54%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.58 (n/a)</td><td>0.41 (n/a)</td><td>0.47 (n/a)</td><td>0.13 (n/a)</td><td>0.18 (n/a)</td><td>1731.80 (n/a)</td><td>725.36 (n/a)</td><td>475.50 (n/a)</td><td>384.40 (n/a)</td><td>570.25 (n/a)</td><td>24.55 (n/a)</td><td>17.59 (n/a)</td><td>19.85 (n/a)</td><td>5.45 (n/a)</td><td>7.68 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.76 (-12.03%)</td><td>0.47 (+16.70%)</td><td>0.38 (+7.90%)</td><td>0.34 <b>(+189.91%)</b></td><td>0.18 <b>(-42.98%)</b></td><td>655.70 <b>(-65.51%)</b></td><td>515.74 <b>(-47.72%)</b></td><td>584.20 (-7.33%)</td><td>291.00 (+13.67%)</td><td>159.30 <b>(-79.62%)</b></td><td>32.43 (-12.03%)</td><td>20.17 (+16.70%)</td><td>16.15 (+7.90%)</td><td>14.39 <b>(+189.91%)</b></td><td>7.71 <b>(-42.98%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.86 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.12 (n/a)</td><td>0.32 (n/a)</td><td>1900.90 (n/a)</td><td>986.50 (n/a)</td><td>630.40 (n/a)</td><td>256.00 (n/a)</td><td>781.81 (n/a)</td><td>36.86 (n/a)</td><td>17.28 (n/a)</td><td>14.97 (n/a)</td><td>4.96 (n/a)</td><td>13.51 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.31 (+1.43%)</td><td>0.30 (-0.58%)</td><td>0.31 (+0.49%)</td><td>0.29 (-3.73%)</td><td>0.01 <b>(+200.16%)</b></td><td>86737.70 (+3.88%)</td><td>82653.04 (+0.65%)</td><td>81337.30 (-0.49%)</td><td>80369.00 (-1.41%)</td><td>2574.98 <b>(+208.00%)</b></td><td>213.76 (+1.43%)</td><td>208.01 (-0.58%)</td><td>211.22 (+0.49%)</td><td>198.07 (-3.73%)</td><td>6.33 <b>(+200.16%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83500.60 (n/a)</td><td>82118.76 (n/a)</td><td>81739.00 (n/a)</td><td>81519.50 (n/a)</td><td>836.05 (n/a)</td><td>210.75 (n/a)</td><td>209.22 (n/a)</td><td>210.18 (n/a)</td><td>205.75 (n/a)</td><td>2.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>1.02 (-2.37%)</td><td>1.00 (-1.87%)</td><td>1.00 (-0.78%)</td><td>0.97 (-2.63%)</td><td>0.02 <b>(+26.94%)</b></td><td>26002.20 (+2.70%)</td><td>25265.40 (+1.92%)</td><td>25048.10 (+0.79%)</td><td>24665.20 (+2.43%)</td><td>618.42 <b>(+33.94%)</b></td><td>696.52 (-2.37%)</td><td>680.30 (-1.87%)</td><td>685.87 (-0.78%)</td><td>660.71 (-2.63%)</td><td>16.55 <b>(+26.93%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>1.05 (n/a)</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>0.99 (n/a)</td><td>0.02 (n/a)</td><td>25318.30 (n/a)</td><td>24789.32 (n/a)</td><td>24852.20 (n/a)</td><td>24080.60 (n/a)</td><td>461.73 (n/a)</td><td>713.43 (n/a)</td><td>693.23 (n/a)</td><td>691.28 (n/a)</td><td>678.56 (n/a)</td><td>13.04 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>2.34 <b>(-42.97%)</b></td><td>1.91 <b>(-25.25%)</b></td><td>1.79 (-15.78%)</td><td>1.64 (+3.67%)</td><td>0.30 <b>(-73.39%)</b></td><td>4925.50 (-3.54%)</td><td>4309.28 (+17.64%)</td><td>4508.30 (+18.74%)</td><td>3447.50 <b>(+75.35%)</b></td><td>634.07 <b>(-56.35%)</b></td><td>613.17 <b>(-42.97%)</b></td><td>499.76 <b>(-25.25%)</b></td><td>468.90 (-15.78%)</td><td>429.18 (+3.67%)</td><td>78.50 <b>(-73.39%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>4.10 (n/a)</td><td>2.55 (n/a)</td><td>2.12 (n/a)</td><td>1.58 (n/a)</td><td>1.13 (n/a)</td><td>5106.20 (n/a)</td><td>3663.16 (n/a)</td><td>3796.80 (n/a)</td><td>1966.10 (n/a)</td><td>1452.53 (n/a)</td><td>1075.19 (n/a)</td><td>668.58 (n/a)</td><td>556.77 (n/a)</td><td>413.99 (n/a)</td><td>295.03 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.28 <b>(+20.87%)</b></td><td>0.21 (+0.71%)</td><td>0.20 (-0.07%)</td><td>0.17 (-9.32%)</td><td>0.04 <b>(+135.82%)</b></td><td>7423.20 (+10.28%)</td><td>6194.88 (+1.72%)</td><td>6221.60 (+0.07%)</td><td>4436.10 (-17.26%)</td><td>1118.26 <b>(+109.60%)</b></td><td>15.13 <b>(+20.87%)</b></td><td>11.17 (+0.71%)</td><td>10.79 (-0.07%)</td><td>9.04 (-9.32%)</td><td>2.35 <b>(+135.82%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>6731.20 (n/a)</td><td>6089.84 (n/a)</td><td>6217.10 (n/a)</td><td>5361.80 (n/a)</td><td>533.52 (n/a)</td><td>12.52 (n/a)</td><td>11.09 (n/a)</td><td>10.79 (n/a)</td><td>9.97 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>0.06 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>3.89 (n/a)</td><td>3.68 (n/a)</td><td>3.77 (n/a)</td><td>3.40 (n/a)</td><td>0.20 (n/a)</td><td>3.89 (n/a)</td><td>3.68 (n/a)</td><td>3.77 (n/a)</td><td>3.39 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>7.56 (+7.94%)</td><td>7.19 (+12.10%)</td><td>7.40 (+10.94%)</td><td>6.67 <b>(+21.58%)</b></td><td>0.41 <b>(-37.31%)</b></td><td>7.56 (+7.94%)</td><td>7.19 (+12.10%)</td><td>7.39 (+10.94%)</td><td>6.66 <b>(+21.58%)</b></td><td>0.41 <b>(-37.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>7.01 (n/a)</td><td>6.42 (n/a)</td><td>6.67 (n/a)</td><td>5.48 (n/a)</td><td>0.66 (n/a)</td><td>7.00 (n/a)</td><td>6.41 (n/a)</td><td>6.67 (n/a)</td><td>5.48 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>13.00 (+1.84%)</td><td>9.77 (-4.12%)</td><td>9.82 (-12.50%)</td><td>7.11 (-7.18%)</td><td>2.54 (+14.35%)</td><td>13.00 (+1.84%)</td><td>9.77 (-4.12%)</td><td>9.81 (-12.50%)</td><td>7.10 (-7.18%)</td><td>2.54 (+14.35%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>12.77 (n/a)</td><td>10.19 (n/a)</td><td>11.22 (n/a)</td><td>7.66 (n/a)</td><td>2.22 (n/a)</td><td>12.76 (n/a)</td><td>10.19 (n/a)</td><td>11.22 (n/a)</td><td>7.65 (n/a)</td><td>2.22 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>3.96 (n/a)</td><td>3.65 (n/a)</td><td>3.52 (n/a)</td><td>3.39 (n/a)</td><td>0.29 (n/a)</td><td>3.96 (n/a)</td><td>3.65 (n/a)</td><td>3.51 (n/a)</td><td>3.39 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>7.37 (+0.06%)</td><td>6.92 (+9.45%)</td><td>6.89 (+12.67%)</td><td>6.62 <b>(+26.75%)</b></td><td>0.28 <b>(-68.04%)</b></td><td>7.37 (+0.06%)</td><td>6.92 (+9.45%)</td><td>6.89 (+12.67%)</td><td>6.62 <b>(+26.75%)</b></td><td>0.28 <b>(-68.04%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>7.37 (n/a)</td><td>6.32 (n/a)</td><td>6.12 (n/a)</td><td>5.23 (n/a)</td><td>0.86 (n/a)</td><td>7.36 (n/a)</td><td>6.32 (n/a)</td><td>6.11 (n/a)</td><td>5.22 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>13.36 (+0.61%)</td><td>10.57 (+6.56%)</td><td>9.99 (+1.35%)</td><td>8.20 <b>(+41.22%)</b></td><td>1.93 <b>(-38.93%)</b></td><td>13.35 (+0.61%)</td><td>10.56 (+6.56%)</td><td>9.98 (+1.35%)</td><td>8.20 <b>(+41.22%)</b></td><td>1.93 <b>(-38.93%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>13.27 (n/a)</td><td>9.92 (n/a)</td><td>9.85 (n/a)</td><td>5.81 (n/a)</td><td>3.17 (n/a)</td><td>13.27 (n/a)</td><td>9.91 (n/a)</td><td>9.85 (n/a)</td><td>5.81 (n/a)</td><td>3.17 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>3.09 (-0.16%)</td><td>1.89 <b>(-33.67%)</b></td><td>1.50 <b>(-46.50%)</b></td><td>1.20 <b>(-54.52%)</b></td><td>0.84 <b>(+299.48%)</b></td><td>3.08 (-0.16%)</td><td>1.89 <b>(-33.67%)</b></td><td>1.49 <b>(-46.50%)</b></td><td>1.19 <b>(-54.52%)</b></td><td>0.84 <b>(+299.48%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>3.10 (n/a)</td><td>2.86 (n/a)</td><td>2.80 (n/a)</td><td>2.63 (n/a)</td><td>0.21 (n/a)</td><td>3.09 (n/a)</td><td>2.85 (n/a)</td><td>2.79 (n/a)</td><td>2.62 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.58 <b>(+42.19%)</b></td><td>0.44 <b>(+107.64%)</b></td><td>0.56 <b>(+341.82%)</b></td><td>0.14 <b>(+93.92%)</b></td><td>0.20 (+18.86%)</td><td>0.58 <b>(+42.19%)</b></td><td>0.43 <b>(+107.64%)</b></td><td>0.55 <b>(+341.82%)</b></td><td>0.14 <b>(+93.92%)</b></td><td>0.19 (+18.86%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.41 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>0.40 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.67 (+4.56%)</td><td>0.46 (+2.41%)</td><td>0.46 (+4.95%)</td><td>0.08 <b>(-73.20%)</b></td><td>0.24 <b>(+76.20%)</b></td><td>0.66 (+4.56%)</td><td>0.45 (+2.41%)</td><td>0.45 (+4.95%)</td><td>0.08 <b>(-73.20%)</b></td><td>0.24 <b>(+76.20%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.64 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.14 (n/a)</td><td>0.63 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>2.44 (+3.58%)</td><td>1.23 (-19.13%)</td><td>0.43 <b>(-79.42%)</b></td><td>0.42 (-1.06%)</td><td>1.10 (+11.12%)</td><td>2.40 (+3.58%)</td><td>1.21 (-19.13%)</td><td>0.42 <b>(-79.42%)</b></td><td>0.42 (-1.06%)</td><td>1.08 (+11.12%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>2.35 (n/a)</td><td>1.52 (n/a)</td><td>2.08 (n/a)</td><td>0.43 (n/a)</td><td>0.99 (n/a)</td><td>2.32 (n/a)</td><td>1.49 (n/a)</td><td>2.05 (n/a)</td><td>0.42 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.60 (n/a)</td><td>357.14 (n/a)</td><td>277.50 (n/a)</td><td>247.10 (n/a)</td><td>136.59 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1853.60 (n/a)</td><td>691.68 (n/a)</td><td>480.90 (n/a)</td><td>246.50 (n/a)</td><td>658.59 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.50 (n/a)</td><td>384.80 (n/a)</td><td>272.20 (n/a)</td><td>257.50 (n/a)</td><td>165.60 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.50 (n/a)</td><td>380.92 (n/a)</td><td>273.70 (n/a)</td><td>234.80 (n/a)</td><td>170.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>500.90 (n/a)</td><td>419.44 (n/a)</td><td>415.00 (n/a)</td><td>290.10 (n/a)</td><td>87.02 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.90 (n/a)</td><td>410.54 (n/a)</td><td>370.40 (n/a)</td><td>244.20 (n/a)</td><td>128.65 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 <b>(-21.94%)</b></td><td>0.02 <b>(-24.20%)</b></td><td>0.02 <b>(-31.47%)</b></td><td>0.01 (-6.37%)</td><td>0.01 <b>(-25.21%)</b></td><td>585.90 (+6.80%)</td><td>464.46 <b>(+29.14%)</b></td><td>509.90 <b>(+45.94%)</b></td><td>259.30 <b>(+28.11%)</b></td><td>141.85 (+5.62%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.60 (n/a)</td><td>359.66 (n/a)</td><td>349.40 (n/a)</td><td>202.40 (n/a)</td><td>134.30 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 <b>(-20.23%)</b></td><td>0.02 <b>(-36.03%)</b></td><td>0.02 <b>(-34.72%)</b></td><td>0.00 <b>(-80.00%)</b></td><td>0.01 (+13.53%)</td><td>2469.60 <b>(+400.12%)</b></td><td>807.16 <b>(+165.20%)</b></td><td>411.90 <b>(+53.18%)</b></td><td>225.10 <b>(+25.40%)</b></td><td>935.82 <b>(+704.22%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.80 (n/a)</td><td>304.36 (n/a)</td><td>268.90 (n/a)</td><td>179.50 (n/a)</td><td>116.36 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 <b>(-27.74%)</b></td><td>0.03 (-3.81%)</td><td>0.03 (-0.28%)</td><td>0.03 <b>(+57.07%)</b></td><td>0.00 <b>(-81.90%)</b></td><td>325.40 <b>(-36.33%)</b></td><td>301.46 (-4.71%)</td><td>296.10 (+0.27%)</td><td>279.10 <b>(+38.44%)</b></td><td>17.62 <b>(-84.79%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.10 (n/a)</td><td>316.36 (n/a)</td><td>295.30 (n/a)</td><td>201.60 (n/a)</td><td>115.83 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (-9.54%)</td><td>0.02 (-0.79%)</td><td>0.02 <b>(+39.89%)</b></td><td>0.02 <b>(+118.76%)</b></td><td>0.01 <b>(-45.49%)</b></td><td>495.60 <b>(-54.28%)</b></td><td>382.84 <b>(-25.06%)</b></td><td>373.60 <b>(-28.52%)</b></td><td>225.10 (+10.51%)</td><td>109.46 <b>(-69.34%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1084.10 (n/a)</td><td>510.84 (n/a)</td><td>522.70 (n/a)</td><td>203.70 (n/a)</td><td>357.03 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (+12.36%)</td><td>0.03 (+2.42%)</td><td>0.02 <b>(-33.27%)</b></td><td>0.02 <b>(+35.58%)</b></td><td>0.01 (+5.08%)</td><td>514.30 <b>(-26.24%)</b></td><td>371.04 (-6.88%)</td><td>402.30 <b>(+49.89%)</b></td><td>202.10 (-11.01%)</td><td>145.76 <b>(-30.04%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>697.30 (n/a)</td><td>398.44 (n/a)</td><td>268.40 (n/a)</td><td>227.10 (n/a)</td><td>208.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (+2.22%)</td><td>0.02 (+1.92%)</td><td>0.02 (+10.43%)</td><td>0.01 (+9.85%)</td><td>0.01 (-14.43%)</td><td>558.50 (-8.96%)</td><td>414.34 (-6.60%)</td><td>425.20 (-9.45%)</td><td>240.60 (-2.16%)</td><td>113.32 <b>(-29.92%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.50 (n/a)</td><td>443.60 (n/a)</td><td>469.60 (n/a)</td><td>245.90 (n/a)</td><td>161.71 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 <b>(-21.64%)</b></td><td>0.03 (-5.58%)</td><td>0.02 <b>(-26.85%)</b></td><td>0.02 <b>(+39.56%)</b></td><td>0.01 <b>(-42.01%)</b></td><td>438.10 <b>(-28.36%)</b></td><td>333.16 (-5.83%)</td><td>360.60 <b>(+36.69%)</b></td><td>246.80 <b>(+27.61%)</b></td><td>83.46 <b>(-51.40%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.50 (n/a)</td><td>353.80 (n/a)</td><td>263.80 (n/a)</td><td>193.40 (n/a)</td><td>171.72 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 <b>(-26.30%)</b></td><td>0.01 <b>(-25.19%)</b></td><td>0.02 (-5.38%)</td><td>0.00 <b>(-71.12%)</b></td><td>0.01 (+15.55%)</td><td>1875.80 <b>(+246.22%)</b></td><td>778.52 <b>(+72.87%)</b></td><td>489.50 (+5.70%)</td><td>387.70 <b>(+35.65%)</b></td><td>621.16 <b>(+512.03%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.80 (n/a)</td><td>450.36 (n/a)</td><td>463.10 (n/a)</td><td>285.80 (n/a)</td><td>101.49 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 <b>(+38.06%)</b></td><td>0.04 <b>(+33.44%)</b></td><td>0.03 (+5.08%)</td><td>0.03 <b>(+77.87%)</b></td><td>0.01 (-0.61%)</td><td>293.50 <b>(-43.77%)</b></td><td>240.74 <b>(-29.19%)</b></td><td>255.90 (-4.83%)</td><td>174.40 <b>(-27.57%)</b></td><td>53.60 <b>(-57.87%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.00 (n/a)</td><td>340.00 (n/a)</td><td>268.90 (n/a)</td><td>240.80 (n/a)</td><td>127.22 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 <b>(+28.60%)</b></td><td>0.03 (+1.33%)</td><td>0.03 (-0.33%)</td><td>0.02 (-16.72%)</td><td>0.01 <b>(+76.32%)</b></td><td>507.30 <b>(+20.10%)</b></td><td>304.30 (+7.31%)</td><td>259.90 (+0.35%)</td><td>177.40 <b>(-22.26%)</b></td><td>131.15 <b>(+63.87%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>422.40 (n/a)</td><td>283.56 (n/a)</td><td>259.00 (n/a)</td><td>228.20 (n/a)</td><td>80.03 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (-14.70%)</td><td>0.02 (-18.76%)</td><td>0.02 <b>(-40.00%)</b></td><td>0.00 <b>(-55.76%)</b></td><td>0.01 (+2.30%)</td><td>2434.30 <b>(+126.01%)</b></td><td>801.28 <b>(+72.47%)</b></td><td>492.10 <b>(+66.64%)</b></td><td>237.80 (+17.20%)</td><td>924.35 <b>(+159.74%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1077.10 (n/a)</td><td>464.60 (n/a)</td><td>295.30 (n/a)</td><td>202.90 (n/a)</td><td>355.87 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (-4.87%)</td><td>0.02 <b>(+41.64%)</b></td><td>0.02 <b>(+30.87%)</b></td><td>0.02 <b>(+260.32%)</b></td><td>0.01 <b>(-38.48%)</b></td><td>525.40 <b>(-72.25%)</b></td><td>395.36 <b>(-52.63%)</b></td><td>445.30 <b>(-23.59%)</b></td><td>245.70 (+5.13%)</td><td>113.30 <b>(-82.61%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1893.10 (n/a)</td><td>834.60 (n/a)</td><td>582.80 (n/a)</td><td>233.70 (n/a)</td><td>651.35 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 <b>(+42.61%)</b></td><td>0.03 <b>(+44.51%)</b></td><td>0.03 <b>(+40.49%)</b></td><td>0.02 <b>(+41.51%)</b></td><td>0.01 <b>(+51.22%)</b></td><td>442.60 <b>(-29.33%)</b></td><td>344.58 <b>(-30.47%)</b></td><td>308.20 <b>(-28.82%)</b></td><td>261.80 <b>(-29.89%)</b></td><td>88.01 <b>(-26.77%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>626.30 (n/a)</td><td>495.60 (n/a)</td><td>433.00 (n/a)</td><td>373.40 (n/a)</td><td>120.19 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 (+13.20%)</td><td>0.02 (-19.82%)</td><td>0.02 <b>(-41.76%)</b></td><td>0.01 (-15.30%)</td><td>0.01 <b>(+25.27%)</b></td><td>684.20 (+18.07%)</td><td>503.56 <b>(+30.93%)</b></td><td>498.40 <b>(+71.74%)</b></td><td>212.70 (-11.67%)</td><td>181.99 (+17.44%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.50 (n/a)</td><td>384.60 (n/a)</td><td>290.20 (n/a)</td><td>240.80 (n/a)</td><td>154.96 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (+5.86%)</td><td>0.03 (+0.59%)</td><td>0.03 (+5.49%)</td><td>0.02 (-3.72%)</td><td>0.01 (+15.25%)</td><td>511.50 (+3.86%)</td><td>311.82 (+1.08%)</td><td>254.80 (-5.21%)</td><td>237.50 (-5.53%)</td><td>115.01 (+11.49%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.50 (n/a)</td><td>308.50 (n/a)</td><td>268.80 (n/a)</td><td>251.40 (n/a)</td><td>103.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 (-11.03%)</td><td>0.03 (-5.19%)</td><td>0.03 (+12.45%)</td><td>0.02 (-7.23%)</td><td>0.01 (-14.25%)</td><td>573.40 (+7.80%)</td><td>411.24 (+3.92%)</td><td>420.10 (-11.07%)</td><td>245.70 (+12.40%)</td><td>148.69 (+3.26%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>531.90 (n/a)</td><td>395.74 (n/a)</td><td>472.40 (n/a)</td><td>218.60 (n/a)</td><td>143.99 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 <b>(-26.54%)</b></td><td>0.02 (-14.30%)</td><td>0.02 (+1.92%)</td><td>0.01 (-11.71%)</td><td>0.01 <b>(-37.11%)</b></td><td>615.30 (+13.27%)</td><td>409.70 (+12.10%)</td><td>383.50 (-1.87%)</td><td>295.40 <b>(+36.13%)</b></td><td>129.76 (-1.19%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.20 (n/a)</td><td>365.48 (n/a)</td><td>390.80 (n/a)</td><td>217.00 (n/a)</td><td>131.32 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.05 (+13.44%)</td><td>0.03 (+2.25%)</td><td>0.04 <b>(+54.63%)</b></td><td>0.01 <b>(-73.41%)</b></td><td>0.02 <b>(+57.49%)</b></td><td>1925.70 <b>(+276.11%)</b></td><td>641.72 <b>(+68.32%)</b></td><td>291.50 <b>(-35.32%)</b></td><td>199.30 (-11.85%)</td><td>731.82 <b>(+448.49%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.00 (n/a)</td><td>381.24 (n/a)</td><td>450.70 (n/a)</td><td>226.10 (n/a)</td><td>133.42 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 <b>(-20.06%)</b></td><td>0.02 <b>(-27.44%)</b></td><td>0.02 <b>(-43.28%)</b></td><td>0.01 <b>(-35.90%)</b></td><td>0.01 (+3.09%)</td><td>977.90 <b>(+56.01%)</b></td><td>503.50 <b>(+51.57%)</b></td><td>476.50 <b>(+76.35%)</b></td><td>250.70 <b>(+25.10%)</b></td><td>293.19 <b>(+74.15%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.80 (n/a)</td><td>332.20 (n/a)</td><td>270.20 (n/a)</td><td>200.40 (n/a)</td><td>168.35 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.04 <b>(-30.51%)</b></td><td>0.03 <b>(-22.27%)</b></td><td>0.02 <b>(-48.93%)</b></td><td>0.01 <b>(+104.14%)</b></td><td>0.02 <b>(-24.88%)</b></td><td>1005.70 <b>(-51.01%)</b></td><td>541.72 (-14.95%)</td><td>596.30 <b>(+95.76%)</b></td><td>240.60 <b>(+43.90%)</b></td><td>318.32 <b>(-60.03%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2053.00 (n/a)</td><td>636.96 (n/a)</td><td>304.60 (n/a)</td><td>167.20 (n/a)</td><td>796.31 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (-14.00%)</td><td>0.03 (-11.26%)</td><td>0.03 (-7.30%)</td><td>0.01 (+9.98%)</td><td>0.01 <b>(-30.26%)</b></td><td>549.60 (-9.07%)</td><td>345.16 (+6.16%)</td><td>297.90 (+7.90%)</td><td>265.20 (+16.26%)</td><td>117.18 <b>(-26.02%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.40 (n/a)</td><td>325.14 (n/a)</td><td>276.10 (n/a)</td><td>228.10 (n/a)</td><td>158.39 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (-12.36%)</td><td>0.02 (+2.40%)</td><td>0.02 (+2.87%)</td><td>0.01 (-2.75%)</td><td>0.01 (-3.76%)</td><td>679.80 (+2.83%)</td><td>493.60 (-0.19%)</td><td>534.00 (-2.80%)</td><td>273.30 (+14.11%)</td><td>196.36 <b>(+20.75%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>661.10 (n/a)</td><td>494.54 (n/a)</td><td>549.40 (n/a)</td><td>239.50 (n/a)</td><td>162.63 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (-0.61%)</td><td>0.02 (-2.11%)</td><td>0.02 <b>(-27.20%)</b></td><td>0.01 (+3.13%)</td><td>0.01 <b>(+34.77%)</b></td><td>631.40 (-3.04%)</td><td>450.18 (+10.18%)</td><td>537.30 <b>(+37.35%)</b></td><td>240.40 (+0.59%)</td><td>190.83 <b>(+24.82%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.20 (n/a)</td><td>408.58 (n/a)</td><td>391.20 (n/a)</td><td>239.00 (n/a)</td><td>152.89 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.03 (+6.37%)</td><td>0.02 <b>(-20.54%)</b></td><td>0.02 <b>(-25.30%)</b></td><td>0.01 <b>(-42.65%)</b></td><td>0.01 <b>(+42.09%)</b></td><td>1031.50 <b>(+74.36%)</b></td><td>616.10 <b>(+41.24%)</b></td><td>579.90 <b>(+33.86%)</b></td><td>269.00 (-5.98%)</td><td>272.20 <b>(+120.17%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>591.60 (n/a)</td><td>436.22 (n/a)</td><td>433.20 (n/a)</td><td>286.10 (n/a)</td><td>123.63 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.02 (-18.23%)</td><td>0.02 (-18.06%)</td><td>0.02 (-18.50%)</td><td>0.01 <b>(-23.29%)</b></td><td>0.00 (-6.38%)</td><td>620.90 <b>(+30.36%)</b></td><td>487.26 <b>(+23.49%)</b></td><td>460.50 <b>(+22.70%)</b></td><td>360.00 <b>(+22.28%)</b></td><td>110.01 <b>(+50.58%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>476.30 (n/a)</td><td>394.58 (n/a)</td><td>375.30 (n/a)</td><td>294.40 (n/a)</td><td>73.06 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.35 (+3.36%)</td><td>0.26 (+11.75%)</td><td>0.24 (+13.43%)</td><td>0.17 (-2.05%)</td><td>0.07 (+15.60%)</td><td>571.00 (+2.09%)</td><td>400.38 (-9.14%)</td><td>412.30 (-11.83%)</td><td>284.00 (-3.24%)</td><td>114.17 (+15.56%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>559.30 (n/a)</td><td>440.66 (n/a)</td><td>467.60 (n/a)</td><td>293.50 (n/a)</td><td>98.80 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.33 <b>(-20.83%)</b></td><td>0.20 <b>(-20.96%)</b></td><td>0.19 (-13.52%)</td><td>0.13 <b>(-33.50%)</b></td><td>0.08 (-15.66%)</td><td>773.60 <b>(+50.39%)</b></td><td>546.76 <b>(+29.77%)</b></td><td>521.60 (+15.63%)</td><td>296.20 <b>(+26.31%)</b></td><td>178.07 <b>(+65.08%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.42 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>514.40 (n/a)</td><td>421.32 (n/a)</td><td>451.10 (n/a)</td><td>234.50 (n/a)</td><td>107.87 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.29 <b>(-25.41%)</b></td><td>0.21 (-13.37%)</td><td>0.20 (-11.22%)</td><td>0.17 (+0.68%)</td><td>0.05 <b>(-45.26%)</b></td><td>585.80 (-0.68%)</td><td>474.36 (+10.26%)</td><td>484.40 (+12.62%)</td><td>334.90 <b>(+34.07%)</b></td><td>90.74 <b>(-26.03%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.39 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>589.80 (n/a)</td><td>430.22 (n/a)</td><td>430.10 (n/a)</td><td>249.80 (n/a)</td><td>122.67 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.23 (-13.59%)</td><td>0.19 (+7.80%)</td><td>0.18 <b>(+21.71%)</b></td><td>0.15 (+12.96%)</td><td>0.03 <b>(-40.61%)</b></td><td>478.90 (-11.46%)</td><td>406.06 (-10.84%)</td><td>420.00 (-17.84%)</td><td>321.10 (+15.75%)</td><td>67.81 <b>(-39.05%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>540.90 (n/a)</td><td>455.42 (n/a)</td><td>511.20 (n/a)</td><td>277.40 (n/a)</td><td>111.26 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.32 (+18.40%)</td><td>0.19 (+10.45%)</td><td>0.18 (+15.35%)</td><td>0.04 <b>(-62.34%)</b></td><td>0.10 <b>(+70.54%)</b></td><td>1883.40 <b>(+165.57%)</b></td><td>649.96 <b>(+39.09%)</b></td><td>401.50 (-13.30%)</td><td>231.40 (-15.55%)</td><td>694.10 <b>(+339.79%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>709.20 (n/a)</td><td>467.30 (n/a)</td><td>463.10 (n/a)</td><td>274.00 (n/a)</td><td>157.83 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.32 (+3.89%)</td><td>0.16 <b>(-20.75%)</b></td><td>0.13 <b>(-39.29%)</b></td><td>0.11 (-8.54%)</td><td>0.09 (+3.88%)</td><td>654.10 (+9.34%)</td><td>518.46 <b>(+26.65%)</b></td><td>584.30 <b>(+64.73%)</b></td><td>233.90 (-3.74%)</td><td>167.45 (-1.21%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>598.20 (n/a)</td><td>409.36 (n/a)</td><td>354.70 (n/a)</td><td>243.00 (n/a)</td><td>169.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.49 (+2.35%)</td><td>0.37 (+16.63%)</td><td>0.38 <b>(+35.00%)</b></td><td>0.26 <b>(+54.52%)</b></td><td>0.09 <b>(-35.71%)</b></td><td>506.20 <b>(-35.29%)</b></td><td>375.60 <b>(-23.84%)</b></td><td>344.60 <b>(-25.92%)</b></td><td>265.40 (-2.32%)</td><td>93.18 <b>(-57.70%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.48 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>782.20 (n/a)</td><td>493.20 (n/a)</td><td>465.20 (n/a)</td><td>271.70 (n/a)</td><td>220.29 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.52 (-9.86%)</td><td>0.34 (-11.20%)</td><td>0.27 <b>(-39.96%)</b></td><td>0.18 (-3.73%)</td><td>0.15 (-11.45%)</td><td>721.80 (+3.87%)</td><td>452.26 (+8.55%)</td><td>492.30 <b>(+66.54%)</b></td><td>253.70 (+10.93%)</td><td>194.47 (-8.57%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.57 (n/a)</td><td>0.38 (n/a)</td><td>0.44 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>694.90 (n/a)</td><td>416.64 (n/a)</td><td>295.60 (n/a)</td><td>228.70 (n/a)</td><td>212.69 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.57 (+9.73%)</td><td>0.33 (+9.11%)</td><td>0.26 (+0.15%)</td><td>0.23 (-1.00%)</td><td>0.14 (+14.42%)</td><td>575.20 (+1.02%)</td><td>443.76 (-6.84%)</td><td>506.10 (-0.16%)</td><td>230.70 (-8.85%)</td><td>135.96 (+5.78%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.52 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>569.40 (n/a)</td><td>476.32 (n/a)</td><td>506.90 (n/a)</td><td>253.10 (n/a)</td><td>128.54 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.00 <b>(-57.14%)</b></td><td>0.00 <b>(-38.89%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-78.43%)</b></td><td>20474.01 (-15.54%)</td><td>17921.90 (+18.53%)</td><td>16973.57 (+4.82%)</td><td>15584.75 <b>(+154.93%)</b></td><td>2042.26 <b>(-72.01%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>24241.21 (n/a)</td><td>15120.02 (n/a)</td><td>16192.69 (n/a)</td><td>6113.36 (n/a)</td><td>7296.29 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.00 <b>(-38.46%)</b></td><td>0.00 <b>(-39.02%)</b></td><td>0.00 <b>(-42.86%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-57.62%)</b></td><td>20941.47 (+12.83%)</td><td>17402.61 <b>(+44.55%)</b></td><td>19265.13 <b>(+63.30%)</b></td><td>10072.64 <b>(+58.24%)</b></td><td>4293.97 <b>(-21.25%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18560.02 (n/a)</td><td>12039.50 (n/a)</td><td>11797.07 (n/a)</td><td>6365.53 (n/a)</td><td>5452.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>0.14 (+0.59%)</td><td>0.09 <b>(-21.19%)</b></td><td>0.08 <b>(-38.31%)</b></td><td>0.07 (+6.01%)</td><td>0.03 (-7.08%)</td><td>28309.06 (-5.69%)</td><td>24018.04 <b>(+25.22%)</b></td><td>25639.76 <b>(+62.16%)</b></td><td>15394.14 (-0.64%)</td><td>5266.30 (-15.12%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>30016.64 (n/a)</td><td>19180.16 (n/a)</td><td>15810.96 (n/a)</td><td>15492.53 (n/a)</td><td>6204.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>1.61 (+4.55%)</td><td>1.32 (-5.74%)</td><td>1.51 (+2.15%)</td><td>0.84 <b>(-21.11%)</b></td><td>0.32 <b>(+68.20%)</b></td><td>620.70 <b>(+26.75%)</b></td><td>419.74 (+10.48%)</td><td>347.10 (-2.12%)</td><td>326.50 (-4.34%)</td><td>124.06 <b>(+99.37%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>1.54 (n/a)</td><td>1.41 (n/a)</td><td>1.48 (n/a)</td><td>1.07 (n/a)</td><td>0.19 (n/a)</td><td>489.70 (n/a)</td><td>379.94 (n/a)</td><td>354.60 (n/a)</td><td>341.30 (n/a)</td><td>62.23 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>2.57 (+8.22%)</td><td>1.82 (+2.06%)</td><td>2.03 <b>(+25.71%)</b></td><td>0.32 <b>(-74.74%)</b></td><td>0.90 <b>(+69.31%)</b></td><td>3298.30 <b>(+295.95%)</b></td><td>1052.42 <b>(+66.33%)</b></td><td>515.60 <b>(-20.46%)</b></td><td>407.30 (-7.60%)</td><td>1258.02 <b>(+589.96%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>2.38 (n/a)</td><td>1.78 (n/a)</td><td>1.62 (n/a)</td><td>1.26 (n/a)</td><td>0.53 (n/a)</td><td>833.00 (n/a)</td><td>632.72 (n/a)</td><td>648.20 (n/a)</td><td>440.80 (n/a)</td><td>182.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:09:54</td><td>1.96 (+18.39%)</td><td>1.22 (-5.96%)</td><td>0.97 <b>(-30.34%)</b></td><td>0.90 (+3.25%)</td><td>0.44 (+14.14%)</td><td>582.20 (-3.16%)</td><td>468.96 (+6.60%)</td><td>539.90 <b>(+43.55%)</b></td><td>267.40 (-15.54%)</td><td>130.87 (-8.42%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:48:14</td><td>1.66 (n/a)</td><td>1.29 (n/a)</td><td>1.39 (n/a)</td><td>0.87 (n/a)</td><td>0.39 (n/a)</td><td>601.20 (n/a)</td><td>439.92 (n/a)</td><td>376.10 (n/a)</td><td>316.60 (n/a)</td><td>142.89 (n/a)</td>
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
