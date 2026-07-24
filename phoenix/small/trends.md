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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.05 (+4.45%)</td><td>0.03 (-11.24%)</td><td>0.02 <b>(-43.43%)</b></td><td>0.02 <b>(-24.01%)</b></td><td>0.02 <b>(+41.53%)</b></td><td>602.10 <b>(+31.58%)</b></td><td>421.40 <b>(+22.89%)</b></td><td>511.10 <b>(+76.79%)</b></td><td>226.30 (-4.27%)</td><td>170.37 <b>(+60.70%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>457.60 (n/a)</td><td>342.90 (n/a)</td><td>289.10 (n/a)</td><td>236.40 (n/a)</td><td>106.02 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 <b>(-27.47%)</b></td><td>0.03 <b>(-24.95%)</b></td><td>0.03 <b>(-23.28%)</b></td><td>0.02 (-16.37%)</td><td>0.01 <b>(-35.50%)</b></td><td>605.00 (+19.57%)</td><td>489.86 <b>(+31.15%)</b></td><td>478.20 <b>(+30.37%)</b></td><td>357.20 <b>(+37.92%)</b></td><td>108.07 (+9.71%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.00 (n/a)</td><td>373.52 (n/a)</td><td>366.80 (n/a)</td><td>259.00 (n/a)</td><td>98.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.05 (-5.93%)</td><td>0.04 (-2.22%)</td><td>0.05 (+8.08%)</td><td>0.02 (-0.08%)</td><td>0.01 (-9.16%)</td><td>525.30 (+0.08%)</td><td>360.88 (+0.75%)</td><td>262.60 (-7.47%)</td><td>246.50 (+6.34%)</td><td>145.37 (-3.61%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.90 (n/a)</td><td>358.20 (n/a)</td><td>283.80 (n/a)</td><td>231.80 (n/a)</td><td>150.82 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 <b>(+37.87%)</b></td><td>0.02 <b>(+28.65%)</b></td><td>0.02 <b>(+40.53%)</b></td><td>0.01 <b>(+20.49%)</b></td><td>0.01 <b>(+90.37%)</b></td><td>424.30 (-17.02%)</td><td>298.80 (-17.16%)</td><td>245.20 <b>(-28.85%)</b></td><td>193.70 <b>(-27.48%)</b></td><td>115.47 <b>(+20.28%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.30 (n/a)</td><td>360.68 (n/a)</td><td>344.60 (n/a)</td><td>267.10 (n/a)</td><td>96.00 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 <b>(+29.72%)</b></td><td>0.02 (+1.63%)</td><td>0.02 (+7.32%)</td><td>0.01 <b>(-23.37%)</b></td><td>0.01 <b>(+120.04%)</b></td><td>584.90 <b>(+30.50%)</b></td><td>370.02 (+14.60%)</td><td>267.90 (-6.82%)</td><td>200.80 <b>(-22.89%)</b></td><td>184.80 <b>(+137.99%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>448.20 (n/a)</td><td>322.88 (n/a)</td><td>287.50 (n/a)</td><td>260.40 (n/a)</td><td>77.65 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.02 (+13.84%)</td><td>0.02 <b>(+27.21%)</b></td><td>0.02 <b>(+80.79%)</b></td><td>0.01 <b>(+54.57%)</b></td><td>0.01 (-2.02%)</td><td>537.60 <b>(-35.30%)</b></td><td>376.44 <b>(-26.26%)</b></td><td>317.50 <b>(-44.69%)</b></td><td>228.00 (-12.17%)</td><td>147.44 <b>(-36.78%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>830.90 (n/a)</td><td>510.52 (n/a)</td><td>574.00 (n/a)</td><td>259.60 (n/a)</td><td>233.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.02 <b>(-34.03%)</b></td><td>0.01 (-14.51%)</td><td>0.01 <b>(+20.70%)</b></td><td>0.01 <b>(+22.75%)</b></td><td>0.00 <b>(-60.91%)</b></td><td>479.70 (-18.54%)</td><td>374.80 (-4.14%)</td><td>402.80 (-17.15%)</td><td>255.70 <b>(+51.57%)</b></td><td>91.66 <b>(-51.53%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.90 (n/a)</td><td>391.00 (n/a)</td><td>486.20 (n/a)</td><td>168.70 (n/a)</td><td>189.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 <b>(+35.65%)</b></td><td>0.01 (-19.43%)</td><td>0.01 <b>(-37.43%)</b></td><td>0.01 <b>(-41.27%)</b></td><td>0.01 <b>(+127.29%)</b></td><td>801.30 <b>(+70.27%)</b></td><td>477.32 <b>(+45.69%)</b></td><td>481.60 <b>(+59.84%)</b></td><td>199.00 <b>(-26.30%)</b></td><td>216.19 <b>(+162.11%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>470.60 (n/a)</td><td>327.62 (n/a)</td><td>301.30 (n/a)</td><td>270.00 (n/a)</td><td>82.48 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 <b>(+117.89%)</b></td><td>0.02 <b>(+66.39%)</b></td><td>0.02 <b>(+57.36%)</b></td><td>0.01 <b>(+45.30%)</b></td><td>0.01 <b>(+222.65%)</b></td><td>534.20 <b>(-31.17%)</b></td><td>373.10 <b>(-33.48%)</b></td><td>336.60 <b>(-36.44%)</b></td><td>181.90 <b>(-54.10%)</b></td><td>146.14 (+3.78%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>776.10 (n/a)</td><td>560.88 (n/a)</td><td>529.60 (n/a)</td><td>396.30 (n/a)</td><td>140.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2108.40 (n/a)</td><td>680.14 (n/a)</td><td>246.40 (n/a)</td><td>214.30 (n/a)</td><td>812.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>648.30 (n/a)</td><td>349.16 (n/a)</td><td>300.70 (n/a)</td><td>241.80 (n/a)</td><td>169.74 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>485.20 (n/a)</td><td>362.30 (n/a)</td><td>441.30 (n/a)</td><td>182.00 (n/a)</td><td>136.95 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>450.00 (n/a)</td><td>292.56 (n/a)</td><td>269.30 (n/a)</td><td>235.30 (n/a)</td><td>89.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2064.70 (n/a)</td><td>799.76 (n/a)</td><td>494.30 (n/a)</td><td>303.10 (n/a)</td><td>729.07 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.20 (n/a)</td><td>345.20 (n/a)</td><td>315.30 (n/a)</td><td>272.60 (n/a)</td><td>101.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1863.70 (n/a)</td><td>676.06 (n/a)</td><td>439.40 (n/a)</td><td>256.80 (n/a)</td><td>673.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>499.40 (n/a)</td><td>400.30 (n/a)</td><td>464.30 (n/a)</td><td>239.10 (n/a)</td><td>119.53 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1937.90 (n/a)</td><td>682.28 (n/a)</td><td>382.30 (n/a)</td><td>225.50 (n/a)</td><td>714.16 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.40 (n/a)</td><td>434.12 (n/a)</td><td>538.20 (n/a)</td><td>235.80 (n/a)</td><td>182.47 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.00 (n/a)</td><td>331.90 (n/a)</td><td>284.40 (n/a)</td><td>249.20 (n/a)</td><td>129.11 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>688.30 (n/a)</td><td>420.30 (n/a)</td><td>353.10 (n/a)</td><td>279.10 (n/a)</td><td>167.66 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.45 <b>(-34.23%)</b></td><td>0.35 (-15.80%)</td><td>0.41 (+15.20%)</td><td>0.13 <b>(-50.41%)</b></td><td>0.13 (-17.62%)</td><td>1714.30 <b>(+101.63%)</b></td><td>780.78 <b>(+33.64%)</b></td><td>540.30 (-13.19%)</td><td>492.70 <b>(+52.07%)</b></td><td>526.30 <b>(+169.21%)</b></td><td>19.15 <b>(-34.23%)</b></td><td>15.09 (-15.80%)</td><td>17.47 (+15.20%)</td><td>5.50 <b>(-50.41%)</b></td><td>5.71 (-17.62%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.68 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>850.20 (n/a)</td><td>584.22 (n/a)</td><td>622.40 (n/a)</td><td>324.00 (n/a)</td><td>195.50 (n/a)</td><td>29.12 (n/a)</td><td>17.92 (n/a)</td><td>15.16 (n/a)</td><td>11.10 (n/a)</td><td>6.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.46 (-17.71%)</td><td>0.39 (-14.58%)</td><td>0.39 (-17.04%)</td><td>0.35 (-0.11%)</td><td>0.04 <b>(-51.57%)</b></td><td>636.80 (+0.11%)</td><td>572.98 (+14.44%)</td><td>569.90 <b>(+20.54%)</b></td><td>484.70 <b>(+21.51%)</b></td><td>59.97 <b>(-41.03%)</b></td><td>19.47 (-17.71%)</td><td>16.62 (-14.58%)</td><td>16.56 (-17.04%)</td><td>14.82 (-0.11%)</td><td>1.83 <b>(-51.57%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>636.10 (n/a)</td><td>500.66 (n/a)</td><td>472.80 (n/a)</td><td>398.90 (n/a)</td><td>101.69 (n/a)</td><td>23.66 (n/a)</td><td>19.46 (n/a)</td><td>19.96 (n/a)</td><td>14.84 (n/a)</td><td>3.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.31 (+0.69%)</td><td>0.31 (+0.71%)</td><td>0.31 (+0.72%)</td><td>0.30 (+0.16%)</td><td>0.00 <b>(+59.19%)</b></td><td>83298.60 (-0.16%)</td><td>82394.82 (-0.70%)</td><td>82438.00 (-0.72%)</td><td>81830.00 (-0.69%)</td><td>588.70 <b>(+57.89%)</b></td><td>209.95 (+0.69%)</td><td>208.52 (+0.71%)</td><td>208.40 (+0.72%)</td><td>206.24 (+0.16%)</td><td>1.48 <b>(+59.19%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83435.40 (n/a)</td><td>82973.98 (n/a)</td><td>83034.70 (n/a)</td><td>82398.00 (n/a)</td><td>372.86 (n/a)</td><td>208.50 (n/a)</td><td>207.05 (n/a)</td><td>206.90 (n/a)</td><td>205.91 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>1.02 (+0.27%)</td><td>1.02 (+1.95%)</td><td>1.02 (+2.29%)</td><td>1.01 (+3.05%)</td><td>0.01 <b>(-60.14%)</b></td><td>24977.70 (-2.96%)</td><td>24735.92 (-1.93%)</td><td>24717.00 (-2.24%)</td><td>24568.50 (-0.27%)</td><td>153.18 <b>(-61.34%)</b></td><td>699.27 (+0.27%)</td><td>694.55 (+1.95%)</td><td>695.06 (+2.29%)</td><td>687.81 (+3.05%)</td><td>4.28 <b>(-60.14%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>1.00 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25740.70 (n/a)</td><td>25221.58 (n/a)</td><td>25284.20 (n/a)</td><td>24634.10 (n/a)</td><td>396.19 (n/a)</td><td>697.40 (n/a)</td><td>681.29 (n/a)</td><td>679.47 (n/a)</td><td>667.42 (n/a)</td><td>10.75 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>3.87 (-0.82%)</td><td>2.01 <b>(-28.71%)</b></td><td>1.55 <b>(-54.33%)</b></td><td>1.08 (-14.68%)</td><td>1.11 (+1.54%)</td><td>7497.60 (+17.21%)</td><td>4861.04 <b>(+42.92%)</b></td><td>5214.70 <b>(+118.95%)</b></td><td>2080.60 (+0.82%)</td><td>2058.45 (+13.77%)</td><td>1016.01 (-0.82%)</td><td>527.19 <b>(-28.71%)</b></td><td>405.38 <b>(-54.33%)</b></td><td>281.95 (-14.68%)</td><td>292.28 (+1.54%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>3.91 (n/a)</td><td>2.82 (n/a)</td><td>3.38 (n/a)</td><td>1.26 (n/a)</td><td>1.10 (n/a)</td><td>6396.70 (n/a)</td><td>3401.30 (n/a)</td><td>2381.70 (n/a)</td><td>2063.60 (n/a)</td><td>1809.33 (n/a)</td><td>1024.38 (n/a)</td><td>739.52 (n/a)</td><td>887.59 (n/a)</td><td>330.47 (n/a)</td><td>287.84 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.20 <b>(-36.95%)</b></td><td>0.18 (-16.54%)</td><td>0.19 (-7.29%)</td><td>0.16 (-12.46%)</td><td>0.02 <b>(-67.97%)</b></td><td>7866.10 (+14.23%)</td><td>6782.86 (+16.21%)</td><td>6527.50 (+7.86%)</td><td>6232.00 <b>(+58.60%)</b></td><td>682.70 <b>(-39.30%)</b></td><td>10.77 <b>(-36.95%)</b></td><td>9.97 (-16.54%)</td><td>10.28 (-7.29%)</td><td>8.53 (-12.46%)</td><td>0.94 <b>(-67.97%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>6886.40 (n/a)</td><td>5836.70 (n/a)</td><td>6051.70 (n/a)</td><td>3929.40 (n/a)</td><td>1124.66 (n/a)</td><td>17.08 (n/a)</td><td>11.95 (n/a)</td><td>11.09 (n/a)</td><td>9.75 (n/a)</td><td>2.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.14 <b>(+80.52%)</b></td><td>0.10 <b>(+58.34%)</b></td><td>0.11 <b>(+68.15%)</b></td><td>0.06 (+9.66%)</td><td>0.03 <b>(+309.57%)</b></td><td>0.14 <b>(+80.52%)</b></td><td>0.10 <b>(+58.34%)</b></td><td>0.11 <b>(+68.15%)</b></td><td>0.06 (+9.66%)</td><td>0.03 <b>(+309.57%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>3.71 (-1.40%)</td><td>3.58 (-0.63%)</td><td>3.63 (-0.97%)</td><td>3.37 (-0.54%)</td><td>0.14 (-15.35%)</td><td>3.71 (-1.40%)</td><td>3.58 (-0.63%)</td><td>3.63 (-0.97%)</td><td>3.37 (-0.54%)</td><td>0.14 (-15.35%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>3.76 (n/a)</td><td>3.61 (n/a)</td><td>3.67 (n/a)</td><td>3.39 (n/a)</td><td>0.17 (n/a)</td><td>3.76 (n/a)</td><td>3.60 (n/a)</td><td>3.66 (n/a)</td><td>3.39 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>6.94 (-0.99%)</td><td>6.48 (-0.62%)</td><td>6.58 (-1.97%)</td><td>5.68 (+1.06%)</td><td>0.47 (-13.98%)</td><td>6.94 (-0.99%)</td><td>6.47 (-0.62%)</td><td>6.58 (-1.97%)</td><td>5.68 (+1.06%)</td><td>0.47 (-13.98%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>7.01 (n/a)</td><td>6.52 (n/a)</td><td>6.72 (n/a)</td><td>5.62 (n/a)</td><td>0.55 (n/a)</td><td>7.00 (n/a)</td><td>6.51 (n/a)</td><td>6.71 (n/a)</td><td>5.62 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>14.05 <b>(+42.02%)</b></td><td>10.19 <b>(+24.88%)</b></td><td>9.89 <b>(+21.71%)</b></td><td>8.35 <b>(+34.01%)</b></td><td>2.32 <b>(+58.45%)</b></td><td>14.04 <b>(+42.02%)</b></td><td>10.19 <b>(+24.88%)</b></td><td>9.89 <b>(+21.71%)</b></td><td>8.34 <b>(+34.01%)</b></td><td>2.32 <b>(+58.45%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>9.89 (n/a)</td><td>8.16 (n/a)</td><td>8.13 (n/a)</td><td>6.23 (n/a)</td><td>1.47 (n/a)</td><td>9.89 (n/a)</td><td>8.16 (n/a)</td><td>8.12 (n/a)</td><td>6.22 (n/a)</td><td>1.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>3.78 (+0.30%)</td><td>3.70 (+2.77%)</td><td>3.70 (+1.19%)</td><td>3.65 (+9.14%)</td><td>0.05 <b>(-69.76%)</b></td><td>3.77 (+0.30%)</td><td>3.70 (+2.77%)</td><td>3.69 (+1.19%)</td><td>3.65 (+9.14%)</td><td>0.05 <b>(-69.76%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>3.76 (n/a)</td><td>3.60 (n/a)</td><td>3.65 (n/a)</td><td>3.35 (n/a)</td><td>0.17 (n/a)</td><td>3.76 (n/a)</td><td>3.60 (n/a)</td><td>3.65 (n/a)</td><td>3.35 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>7.68 (+5.66%)</td><td>6.20 (-4.68%)</td><td>5.91 (-10.25%)</td><td>4.91 (-11.29%)</td><td>1.09 <b>(+74.19%)</b></td><td>7.67 (+5.66%)</td><td>6.20 (-4.68%)</td><td>5.91 (-10.25%)</td><td>4.91 (-11.29%)</td><td>1.09 <b>(+74.19%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>7.27 (n/a)</td><td>6.51 (n/a)</td><td>6.58 (n/a)</td><td>5.54 (n/a)</td><td>0.63 (n/a)</td><td>7.26 (n/a)</td><td>6.50 (n/a)</td><td>6.58 (n/a)</td><td>5.53 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>11.14 <b>(-20.35%)</b></td><td>8.92 (-0.78%)</td><td>8.46 (+9.38%)</td><td>7.40 (+0.46%)</td><td>1.54 <b>(-45.48%)</b></td><td>11.13 <b>(-20.35%)</b></td><td>8.92 (-0.78%)</td><td>8.46 (+9.38%)</td><td>7.39 (+0.46%)</td><td>1.54 <b>(-45.48%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>13.98 (n/a)</td><td>8.99 (n/a)</td><td>7.74 (n/a)</td><td>7.37 (n/a)</td><td>2.83 (n/a)</td><td>13.97 (n/a)</td><td>8.99 (n/a)</td><td>7.73 (n/a)</td><td>7.36 (n/a)</td><td>2.82 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>2.77 (-13.77%)</td><td>2.41 (-8.51%)</td><td>2.68 (-11.09%)</td><td>1.24 (+12.39%)</td><td>0.66 <b>(-24.64%)</b></td><td>2.76 (-13.77%)</td><td>2.41 (-8.51%)</td><td>2.68 (-11.09%)</td><td>1.24 (+12.39%)</td><td>0.66 <b>(-24.64%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>3.21 (n/a)</td><td>2.64 (n/a)</td><td>3.02 (n/a)</td><td>1.10 (n/a)</td><td>0.87 (n/a)</td><td>3.21 (n/a)</td><td>2.63 (n/a)</td><td>3.01 (n/a)</td><td>1.10 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.33 <b>(-39.22%)</b></td><td>0.26 <b>(-27.18%)</b></td><td>0.30 <b>(-33.94%)</b></td><td>0.08 (-1.02%)</td><td>0.10 <b>(-46.41%)</b></td><td>0.32 <b>(-39.22%)</b></td><td>0.25 <b>(-27.18%)</b></td><td>0.30 <b>(-33.94%)</b></td><td>0.07 (-1.02%)</td><td>0.10 <b>(-46.41%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.54 (n/a)</td><td>0.35 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.53 (n/a)</td><td>0.35 (n/a)</td><td>0.45 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.62 (-7.93%)</td><td>0.50 (+4.55%)</td><td>0.53 (-15.26%)</td><td>0.30 <b>(+263.81%)</b></td><td>0.13 <b>(-48.19%)</b></td><td>0.62 (-7.93%)</td><td>0.49 (+4.55%)</td><td>0.52 (-15.26%)</td><td>0.29 <b>(+263.81%)</b></td><td>0.13 <b>(-48.19%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.68 (n/a)</td><td>0.48 (n/a)</td><td>0.62 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td><td>0.67 (n/a)</td><td>0.47 (n/a)</td><td>0.61 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>2.11 (+3.43%)</td><td>1.35 <b>(+25.09%)</b></td><td>1.66 <b>(+107.57%)</b></td><td>0.44 (+5.39%)</td><td>0.85 <b>(+28.65%)</b></td><td>2.08 (+3.43%)</td><td>1.33 <b>(+25.09%)</b></td><td>1.63 <b>(+107.57%)</b></td><td>0.43 (+5.39%)</td><td>0.83 <b>(+28.65%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>2.04 (n/a)</td><td>1.08 (n/a)</td><td>0.80 (n/a)</td><td>0.42 (n/a)</td><td>0.66 (n/a)</td><td>2.01 (n/a)</td><td>1.06 (n/a)</td><td>0.79 (n/a)</td><td>0.41 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.70 (n/a)</td><td>419.60 (n/a)</td><td>437.30 (n/a)</td><td>278.30 (n/a)</td><td>142.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>631.20 (n/a)</td><td>522.26 (n/a)</td><td>534.80 (n/a)</td><td>348.20 (n/a)</td><td>114.43 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1972.90 (n/a)</td><td>680.56 (n/a)</td><td>375.80 (n/a)</td><td>240.20 (n/a)</td><td>728.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.80 (n/a)</td><td>396.94 (n/a)</td><td>351.90 (n/a)</td><td>236.60 (n/a)</td><td>168.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.80 (n/a)</td><td>450.66 (n/a)</td><td>526.70 (n/a)</td><td>266.60 (n/a)</td><td>157.52 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1051.50 (n/a)</td><td>560.88 (n/a)</td><td>473.10 (n/a)</td><td>333.60 (n/a)</td><td>289.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (+0.93%)</td><td>0.02 (-12.55%)</td><td>0.03 (+3.19%)</td><td>0.00 <b>(-73.54%)</b></td><td>0.01 <b>(+85.60%)</b></td><td>1968.70 <b>(+277.94%)</b></td><td>702.40 <b>(+104.02%)</b></td><td>279.60 (-3.08%)</td><td>232.50 (-0.90%)</td><td>745.58 <b>(+536.26%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.90 (n/a)</td><td>344.28 (n/a)</td><td>288.50 (n/a)</td><td>234.60 (n/a)</td><td>117.18 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (-16.51%)</td><td>0.03 (-1.80%)</td><td>0.02 <b>(+23.17%)</b></td><td>0.02 (+4.30%)</td><td>0.01 <b>(-40.70%)</b></td><td>470.70 (-4.11%)</td><td>334.80 (-6.10%)</td><td>331.80 (-18.82%)</td><td>239.20 (+19.78%)</td><td>91.83 <b>(-31.96%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>490.90 (n/a)</td><td>356.54 (n/a)</td><td>408.70 (n/a)</td><td>199.70 (n/a)</td><td>134.97 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.05 <b>(+88.42%)</b></td><td>0.03 <b>(+48.03%)</b></td><td>0.03 <b>(+54.23%)</b></td><td>0.02 (-2.92%)</td><td>0.02 <b>(+191.87%)</b></td><td>527.80 (+3.01%)</td><td>345.78 <b>(-22.10%)</b></td><td>312.50 <b>(-35.17%)</b></td><td>154.20 <b>(-46.92%)</b></td><td>150.89 <b>(+62.67%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.40 (n/a)</td><td>443.90 (n/a)</td><td>482.00 (n/a)</td><td>290.50 (n/a)</td><td>92.76 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (+17.74%)</td><td>0.02 (+19.32%)</td><td>0.02 <b>(+22.12%)</b></td><td>0.01 (-7.98%)</td><td>0.01 <b>(+52.96%)</b></td><td>641.60 (+8.67%)</td><td>409.80 (-8.56%)</td><td>375.90 (-18.12%)</td><td>224.20 (-15.08%)</td><td>185.06 <b>(+39.70%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.40 (n/a)</td><td>448.14 (n/a)</td><td>459.10 (n/a)</td><td>264.00 (n/a)</td><td>132.47 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (+13.86%)</td><td>0.02 (+5.45%)</td><td>0.02 <b>(+34.21%)</b></td><td>0.02 (+13.15%)</td><td>0.01 (-11.15%)</td><td>502.90 (-11.63%)</td><td>385.26 (-9.46%)</td><td>382.20 <b>(-25.48%)</b></td><td>227.10 (-12.18%)</td><td>105.79 <b>(-30.11%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.10 (n/a)</td><td>425.52 (n/a)</td><td>512.90 (n/a)</td><td>258.60 (n/a)</td><td>151.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (-1.67%)</td><td>0.02 (-12.48%)</td><td>0.02 <b>(-30.95%)</b></td><td>0.02 <b>(+21.54%)</b></td><td>0.01 (-5.16%)</td><td>476.00 (-17.72%)</td><td>385.98 (+11.57%)</td><td>437.80 <b>(+44.82%)</b></td><td>239.10 (+1.66%)</td><td>103.44 <b>(-23.65%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.50 (n/a)</td><td>345.94 (n/a)</td><td>302.30 (n/a)</td><td>235.20 (n/a)</td><td>135.49 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 <b>(+32.96%)</b></td><td>0.02 (-3.16%)</td><td>0.02 (-2.72%)</td><td>0.00 <b>(-63.13%)</b></td><td>0.01 <b>(+87.71%)</b></td><td>1896.40 <b>(+171.22%)</b></td><td>750.90 <b>(+54.84%)</b></td><td>524.80 (+2.78%)</td><td>198.30 <b>(-24.80%)</b></td><td>660.81 <b>(+319.28%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>699.20 (n/a)</td><td>484.96 (n/a)</td><td>510.60 (n/a)</td><td>263.70 (n/a)</td><td>157.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.02 <b>(-35.39%)</b></td><td>0.02 (-14.99%)</td><td>0.02 <b>(+24.44%)</b></td><td>0.01 (-9.42%)</td><td>0.01 <b>(-52.75%)</b></td><td>745.40 (+10.40%)</td><td>496.46 (+4.28%)</td><td>445.60 (-19.65%)</td><td>349.30 <b>(+54.76%)</b></td><td>163.43 <b>(-21.50%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>675.20 (n/a)</td><td>476.08 (n/a)</td><td>554.60 (n/a)</td><td>225.70 (n/a)</td><td>208.18 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 <b>(+23.09%)</b></td><td>0.03 <b>(+47.27%)</b></td><td>0.03 <b>(+100.13%)</b></td><td>0.01 (+3.74%)</td><td>0.01 <b>(+75.21%)</b></td><td>558.10 (-3.61%)</td><td>363.28 <b>(-25.51%)</b></td><td>255.10 <b>(-50.03%)</b></td><td>233.40 (-18.79%)</td><td>167.36 <b>(+44.49%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.00 (n/a)</td><td>487.66 (n/a)</td><td>510.50 (n/a)</td><td>287.40 (n/a)</td><td>115.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (-1.43%)</td><td>0.02 (-19.69%)</td><td>0.02 <b>(-49.22%)</b></td><td>0.02 (-9.81%)</td><td>0.01 (+15.03%)</td><td>529.00 (+10.88%)</td><td>397.22 <b>(+30.32%)</b></td><td>460.10 <b>(+96.96%)</b></td><td>231.00 (+1.45%)</td><td>147.48 <b>(+33.96%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>477.10 (n/a)</td><td>304.80 (n/a)</td><td>233.60 (n/a)</td><td>227.70 (n/a)</td><td>110.09 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (-4.32%)</td><td>0.03 (+17.44%)</td><td>0.03 (+4.56%)</td><td>0.02 <b>(+61.24%)</b></td><td>0.00 <b>(-57.65%)</b></td><td>364.40 <b>(-37.99%)</b></td><td>288.26 <b>(-25.95%)</b></td><td>281.80 (-4.38%)</td><td>238.20 (+4.52%)</td><td>46.38 <b>(-73.78%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.60 (n/a)</td><td>389.26 (n/a)</td><td>294.70 (n/a)</td><td>227.90 (n/a)</td><td>176.90 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 <b>(+24.90%)</b></td><td>0.02 <b>(+27.47%)</b></td><td>0.02 (+10.01%)</td><td>0.01 (+14.37%)</td><td>0.01 <b>(+52.99%)</b></td><td>633.50 (-12.56%)</td><td>440.88 (-14.76%)</td><td>480.20 (-9.10%)</td><td>214.80 (-19.94%)</td><td>194.42 (+16.89%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>724.50 (n/a)</td><td>517.20 (n/a)</td><td>528.30 (n/a)</td><td>268.30 (n/a)</td><td>166.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (-0.65%)</td><td>0.03 (+8.00%)</td><td>0.03 (-2.07%)</td><td>0.02 <b>(+24.08%)</b></td><td>0.01 <b>(-28.87%)</b></td><td>481.80 (-19.40%)</td><td>334.68 (-13.20%)</td><td>320.50 (+2.14%)</td><td>263.30 (+0.65%)</td><td>89.51 <b>(-41.09%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.80 (n/a)</td><td>385.58 (n/a)</td><td>313.80 (n/a)</td><td>261.60 (n/a)</td><td>151.95 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 <b>(+45.88%)</b></td><td>0.02 <b>(+73.37%)</b></td><td>0.03 <b>(+72.52%)</b></td><td>0.02 <b>(+284.47%)</b></td><td>0.01 (+18.99%)</td><td>544.30 <b>(-73.99%)</b></td><td>363.88 <b>(-55.67%)</b></td><td>316.70 <b>(-42.03%)</b></td><td>246.10 <b>(-31.43%)</b></td><td>129.93 <b>(-81.86%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2092.70 (n/a)</td><td>820.92 (n/a)</td><td>546.30 (n/a)</td><td>358.90 (n/a)</td><td>716.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (+3.35%)</td><td>0.03 (+8.06%)</td><td>0.03 (+11.07%)</td><td>0.02 (+10.02%)</td><td>0.01 (+14.97%)</td><td>537.90 (-9.12%)</td><td>332.82 (-6.89%)</td><td>294.10 (-9.98%)</td><td>233.40 (-3.23%)</td><td>126.03 (-7.36%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.90 (n/a)</td><td>357.44 (n/a)</td><td>326.70 (n/a)</td><td>241.20 (n/a)</td><td>136.04 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.06 <b>(+50.37%)</b></td><td>0.04 <b>(+52.55%)</b></td><td>0.05 <b>(+68.87%)</b></td><td>0.02 (-0.60%)</td><td>0.01 <b>(+108.08%)</b></td><td>526.20 (+0.61%)</td><td>302.66 <b>(-30.09%)</b></td><td>255.70 <b>(-40.78%)</b></td><td>215.80 <b>(-33.50%)</b></td><td>126.41 <b>(+47.34%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.00 (n/a)</td><td>432.90 (n/a)</td><td>431.80 (n/a)</td><td>324.50 (n/a)</td><td>85.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (-12.72%)</td><td>0.02 <b>(-29.50%)</b></td><td>0.02 <b>(-45.21%)</b></td><td>0.01 (-16.08%)</td><td>0.01 <b>(-24.74%)</b></td><td>670.70 (+19.17%)</td><td>498.78 <b>(+37.28%)</b></td><td>539.80 <b>(+82.49%)</b></td><td>265.40 (+14.59%)</td><td>157.58 (+1.62%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.80 (n/a)</td><td>363.32 (n/a)</td><td>295.80 (n/a)</td><td>231.60 (n/a)</td><td>155.07 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 <b>(+22.08%)</b></td><td>0.03 <b>(+46.05%)</b></td><td>0.04 <b>(+96.54%)</b></td><td>0.02 (+5.46%)</td><td>0.01 <b>(+62.67%)</b></td><td>581.50 (-5.17%)</td><td>363.40 <b>(-26.87%)</b></td><td>262.90 <b>(-49.12%)</b></td><td>244.90 (-18.09%)</td><td>154.09 <b>(+30.53%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>613.20 (n/a)</td><td>496.94 (n/a)</td><td>516.70 (n/a)</td><td>299.00 (n/a)</td><td>118.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 <b>(-21.89%)</b></td><td>0.02 (-9.96%)</td><td>0.02 <b>(-22.13%)</b></td><td>0.02 <b>(+25.58%)</b></td><td>0.01 <b>(-40.98%)</b></td><td>533.50 <b>(-20.37%)</b></td><td>437.76 (-1.47%)</td><td>518.30 <b>(+28.42%)</b></td><td>302.10 <b>(+28.01%)</b></td><td>122.24 <b>(-41.68%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>670.00 (n/a)</td><td>444.28 (n/a)</td><td>403.60 (n/a)</td><td>236.00 (n/a)</td><td>209.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.04 (+2.14%)</td><td>0.03 (+15.74%)</td><td>0.04 <b>(+102.12%)</b></td><td>0.01 (-17.38%)</td><td>0.01 (+4.32%)</td><td>802.80 <b>(+21.03%)</b></td><td>429.06 (-10.09%)</td><td>288.50 <b>(-50.53%)</b></td><td>231.40 (-2.07%)</td><td>240.92 <b>(+23.47%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>663.30 (n/a)</td><td>477.22 (n/a)</td><td>583.20 (n/a)</td><td>236.30 (n/a)</td><td>195.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (-14.72%)</td><td>0.02 <b>(-24.60%)</b></td><td>0.03 <b>(-23.39%)</b></td><td>0.02 <b>(-26.54%)</b></td><td>0.01 (+13.63%)</td><td>536.50 <b>(+36.13%)</b></td><td>380.06 <b>(+38.71%)</b></td><td>319.30 <b>(+30.54%)</b></td><td>256.90 (+17.25%)</td><td>128.88 <b>(+82.67%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>394.10 (n/a)</td><td>274.00 (n/a)</td><td>244.60 (n/a)</td><td>219.10 (n/a)</td><td>70.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 <b>(+56.31%)</b></td><td>0.03 <b>(+58.55%)</b></td><td>0.03 <b>(+75.07%)</b></td><td>0.02 <b>(+75.59%)</b></td><td>0.01 <b>(+59.45%)</b></td><td>554.50 <b>(-43.05%)</b></td><td>372.58 <b>(-37.29%)</b></td><td>293.70 <b>(-42.87%)</b></td><td>267.10 <b>(-36.01%)</b></td><td>132.52 <b>(-42.44%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>973.70 (n/a)</td><td>594.10 (n/a)</td><td>514.10 (n/a)</td><td>417.40 (n/a)</td><td>230.23 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 (-1.44%)</td><td>0.02 (-14.45%)</td><td>0.02 <b>(-31.11%)</b></td><td>0.01 <b>(-28.33%)</b></td><td>0.01 (+9.72%)</td><td>638.00 <b>(+39.55%)</b></td><td>409.60 <b>(+21.82%)</b></td><td>417.00 <b>(+45.14%)</b></td><td>240.70 (+1.43%)</td><td>158.21 <b>(+45.96%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>457.20 (n/a)</td><td>336.22 (n/a)</td><td>287.30 (n/a)</td><td>237.30 (n/a)</td><td>108.39 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 <b>(+22.14%)</b></td><td>0.02 (+10.35%)</td><td>0.02 (+10.06%)</td><td>0.02 (-13.60%)</td><td>0.01 <b>(+101.30%)</b></td><td>538.50 (+15.73%)</td><td>406.88 (-5.72%)</td><td>410.80 (-9.16%)</td><td>276.30 (-18.13%)</td><td>102.40 <b>(+92.41%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>465.30 (n/a)</td><td>431.58 (n/a)</td><td>452.20 (n/a)</td><td>337.50 (n/a)</td><td>53.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.03 <b>(-24.80%)</b></td><td>0.02 (-11.49%)</td><td>0.01 <b>(-26.06%)</b></td><td>0.01 <b>(+208.84%)</b></td><td>0.01 <b>(-50.24%)</b></td><td>671.90 <b>(-67.62%)</b></td><td>541.48 <b>(-27.52%)</b></td><td>566.10 <b>(+35.24%)</b></td><td>320.60 <b>(+32.97%)</b></td><td>141.50 <b>(-81.22%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2075.10 (n/a)</td><td>747.12 (n/a)</td><td>418.60 (n/a)</td><td>241.10 (n/a)</td><td>753.65 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.31 <b>(-22.98%)</b></td><td>0.27 (+8.16%)</td><td>0.28 <b>(+29.41%)</b></td><td>0.20 (+7.57%)</td><td>0.05 <b>(-46.46%)</b></td><td>492.90 (-7.04%)</td><td>375.62 (-11.81%)</td><td>354.50 <b>(-22.73%)</b></td><td>314.10 <b>(+29.85%)</b></td><td>74.47 <b>(-31.98%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.41 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>530.20 (n/a)</td><td>425.94 (n/a)</td><td>458.80 (n/a)</td><td>241.90 (n/a)</td><td>109.48 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.35 <b>(+75.59%)</b></td><td>0.22 <b>(+41.58%)</b></td><td>0.19 (+14.74%)</td><td>0.16 <b>(+62.52%)</b></td><td>0.08 <b>(+73.43%)</b></td><td>633.80 <b>(-38.47%)</b></td><td>490.08 <b>(-29.36%)</b></td><td>521.80 (-12.84%)</td><td>284.40 <b>(-43.05%)</b></td><td>131.10 <b>(-41.75%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>1030.10 (n/a)</td><td>693.78 (n/a)</td><td>598.70 (n/a)</td><td>499.40 (n/a)</td><td>225.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.43 (+12.08%)</td><td>0.24 (-1.12%)</td><td>0.19 (+0.34%)</td><td>0.18 (+0.59%)</td><td>0.11 <b>(+21.91%)</b></td><td>556.60 (-0.57%)</td><td>467.66 (+3.41%)</td><td>526.30 (-0.34%)</td><td>229.00 (-10.79%)</td><td>137.22 (+2.24%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.38 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>559.80 (n/a)</td><td>452.24 (n/a)</td><td>528.10 (n/a)</td><td>256.70 (n/a)</td><td>134.21 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.24 (+0.56%)</td><td>0.15 (-8.30%)</td><td>0.13 (-13.49%)</td><td>0.11 (-14.93%)</td><td>0.05 (+15.50%)</td><td>680.00 (+17.55%)</td><td>523.82 (+11.60%)</td><td>567.20 (+15.59%)</td><td>306.60 (-0.58%)</td><td>138.26 <b>(+29.43%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>578.50 (n/a)</td><td>469.38 (n/a)</td><td>490.70 (n/a)</td><td>308.40 (n/a)</td><td>106.82 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.28 (+13.66%)</td><td>0.18 (-0.94%)</td><td>0.14 (-11.18%)</td><td>0.13 (+7.86%)</td><td>0.06 <b>(+28.72%)</b></td><td>556.80 (-7.29%)</td><td>456.48 (+3.46%)</td><td>536.50 (+12.59%)</td><td>265.40 (-12.03%)</td><td>130.50 (+10.66%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>600.60 (n/a)</td><td>441.22 (n/a)</td><td>476.50 (n/a)</td><td>301.70 (n/a)</td><td>117.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.27 (+11.11%)</td><td>0.16 (-5.33%)</td><td>0.14 (-5.84%)</td><td>0.11 (-17.87%)</td><td>0.07 <b>(+46.68%)</b></td><td>685.20 <b>(+21.75%)</b></td><td>509.24 (+11.65%)</td><td>511.00 (+6.21%)</td><td>268.90 (-10.01%)</td><td>153.75 <b>(+59.04%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>562.80 (n/a)</td><td>456.10 (n/a)</td><td>481.10 (n/a)</td><td>298.80 (n/a)</td><td>96.67 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.44 (+12.03%)</td><td>0.28 (+2.77%)</td><td>0.24 (-1.87%)</td><td>0.21 (+1.89%)</td><td>0.09 <b>(+31.83%)</b></td><td>624.10 (-1.86%)</td><td>503.02 (-0.14%)</td><td>537.70 (+1.91%)</td><td>298.50 (-10.74%)</td><td>134.08 (+19.11%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>635.90 (n/a)</td><td>503.70 (n/a)</td><td>527.60 (n/a)</td><td>334.40 (n/a)</td><td>112.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.41 (-8.68%)</td><td>0.26 (-14.15%)</td><td>0.25 (-5.72%)</td><td>0.13 <b>(-43.53%)</b></td><td>0.10 (+13.54%)</td><td>1042.80 <b>(+77.11%)</b></td><td>583.94 <b>(+26.74%)</b></td><td>519.80 (+6.06%)</td><td>319.50 (+9.53%)</td><td>271.84 <b>(+138.15%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.45 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>588.80 (n/a)</td><td>460.74 (n/a)</td><td>490.10 (n/a)</td><td>291.70 (n/a)</td><td>114.15 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.42 (-11.16%)</td><td>0.34 (-8.14%)</td><td>0.30 <b>(-21.90%)</b></td><td>0.28 <b>(+30.13%)</b></td><td>0.06 <b>(-36.04%)</b></td><td>463.10 <b>(-23.15%)</b></td><td>399.60 (+4.06%)</td><td>430.40 <b>(+28.06%)</b></td><td>312.30 (+12.54%)</td><td>67.15 <b>(-47.36%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.47 (n/a)</td><td>0.37 (n/a)</td><td>0.39 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>602.60 (n/a)</td><td>384.02 (n/a)</td><td>336.10 (n/a)</td><td>277.50 (n/a)</td><td>127.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+33.33%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+4.88%)</td><td>21012.89 (-4.04%)</td><td>13104.67 <b>(-20.66%)</b></td><td>13281.81 <b>(-29.12%)</b></td><td>6197.35 (+5.90%)</td><td>6496.54 (+4.71%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21898.35 (n/a)</td><td>16517.63 (n/a)</td><td>18739.14 (n/a)</td><td>5852.25 (n/a)</td><td>6204.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.00 (-7.14%)</td><td>0.00 <b>(+20.00%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-1.96%)</td><td>23010.60 (+2.06%)</td><td>13252.01 (-11.38%)</td><td>7927.55 <b>(-54.13%)</b></td><td>6441.89 (+9.44%)</td><td>8280.10 (+19.69%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22545.35 (n/a)</td><td>14954.29 (n/a)</td><td>17282.65 (n/a)</td><td>5886.27 (n/a)</td><td>6918.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>0.15 (+7.23%)</td><td>0.12 <b>(+23.91%)</b></td><td>0.13 <b>(+44.24%)</b></td><td>0.07 (+1.22%)</td><td>0.03 (+15.67%)</td><td>27986.88 (-1.30%)</td><td>19303.07 (-18.11%)</td><td>16582.76 <b>(-30.61%)</b></td><td>13866.77 (-6.76%)</td><td>5872.92 (+11.00%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28354.21 (n/a)</td><td>23571.54 (n/a)</td><td>23899.28 (n/a)</td><td>14871.63 (n/a)</td><td>5290.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>2.43 <b>(+40.37%)</b></td><td>1.29 (+5.86%)</td><td>1.02 (-0.25%)</td><td>0.57 <b>(-29.32%)</b></td><td>0.70 <b>(+69.86%)</b></td><td>916.60 <b>(+41.49%)</b></td><td>508.58 (+7.86%)</td><td>515.60 (+0.25%)</td><td>216.20 <b>(-28.76%)</b></td><td>260.98 <b>(+74.28%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>1.73 (n/a)</td><td>1.22 (n/a)</td><td>1.02 (n/a)</td><td>0.81 (n/a)</td><td>0.41 (n/a)</td><td>647.80 (n/a)</td><td>471.50 (n/a)</td><td>514.30 (n/a)</td><td>303.50 (n/a)</td><td>149.75 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>1.69 <b>(-40.65%)</b></td><td>1.06 <b>(-22.80%)</b></td><td>1.33 (-8.93%)</td><td>0.30 (+2.63%)</td><td>0.69 <b>(-31.87%)</b></td><td>3487.00 (-2.56%)</td><td>1738.86 <b>(+21.13%)</b></td><td>791.00 (+9.80%)</td><td>620.20 <b>(+68.49%)</b></td><td>1452.72 (+8.78%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>2.85 (n/a)</td><td>1.37 (n/a)</td><td>1.46 (n/a)</td><td>0.29 (n/a)</td><td>1.02 (n/a)</td><td>3578.60 (n/a)</td><td>1435.54 (n/a)</td><td>720.40 (n/a)</td><td>368.10 (n/a)</td><td>1335.52 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:54:13</td><td>1.70 (+2.57%)</td><td>1.18 (-1.44%)</td><td>0.92 (-8.70%)</td><td>0.85 (+9.21%)</td><td>0.39 (-3.95%)</td><td>618.70 (-8.44%)</td><td>484.44 (+0.41%)</td><td>568.80 (+9.53%)</td><td>308.00 (-2.50%)</td><td>143.85 (-8.77%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:47:53</td><td>1.66 (n/a)</td><td>1.19 (n/a)</td><td>1.01 (n/a)</td><td>0.78 (n/a)</td><td>0.41 (n/a)</td><td>675.70 (n/a)</td><td>482.44 (n/a)</td><td>519.30 (n/a)</td><td>315.90 (n/a)</td><td>157.67 (n/a)</td>
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
