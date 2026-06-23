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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (-18.46%)</td><td>0.03 (-11.81%)</td><td>0.03 <b>(-28.46%)</b></td><td>0.02 (-1.52%)</td><td>0.01 <b>(-49.10%)</b></td><td>533.00 (+1.54%)</td><td>381.92 (+4.67%)</td><td>371.60 <b>(+39.75%)</b></td><td>302.70 <b>(+22.65%)</b></td><td>90.59 <b>(-37.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.90 (n/a)</td><td>364.88 (n/a)</td><td>265.90 (n/a)</td><td>246.80 (n/a)</td><td>145.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.06 (-8.61%)</td><td>0.04 (+18.94%)</td><td>0.04 <b>(+58.18%)</b></td><td>0.02 (+5.17%)</td><td>0.01 <b>(-25.69%)</b></td><td>503.10 (-4.93%)</td><td>312.04 <b>(-21.23%)</b></td><td>302.10 <b>(-36.79%)</b></td><td>217.00 (+9.43%)</td><td>114.12 <b>(-24.34%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>529.20 (n/a)</td><td>396.12 (n/a)</td><td>477.90 (n/a)</td><td>198.30 (n/a)</td><td>150.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.05 (-14.60%)</td><td>0.02 <b>(-25.39%)</b></td><td>0.02 (-11.52%)</td><td>0.01 <b>(-65.72%)</b></td><td>0.01 (-5.94%)</td><td>1973.40 <b>(+191.71%)</b></td><td>757.34 <b>(+74.83%)</b></td><td>523.40 (+13.02%)</td><td>264.00 (+17.07%)</td><td>689.15 <b>(+275.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>676.50 (n/a)</td><td>433.18 (n/a)</td><td>463.10 (n/a)</td><td>225.50 (n/a)</td><td>183.68 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 <b>(+25.32%)</b></td><td>0.02 (+6.92%)</td><td>0.02 (+5.42%)</td><td>0.01 (-8.69%)</td><td>0.01 <b>(+100.23%)</b></td><td>482.70 (+9.51%)</td><td>319.02 (+0.48%)</td><td>272.60 (-5.15%)</td><td>210.80 <b>(-20.21%)</b></td><td>118.89 <b>(+67.57%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>440.80 (n/a)</td><td>317.50 (n/a)</td><td>287.40 (n/a)</td><td>264.20 (n/a)</td><td>70.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 (+19.38%)</td><td>0.01 (-13.19%)</td><td>0.01 <b>(-33.00%)</b></td><td>0.01 (-6.71%)</td><td>0.01 <b>(+36.47%)</b></td><td>479.30 (+7.18%)</td><td>391.04 (+18.50%)</td><td>425.50 <b>(+49.25%)</b></td><td>218.90 (-16.26%)</td><td>100.42 (+17.64%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>447.20 (n/a)</td><td>329.98 (n/a)</td><td>285.10 (n/a)</td><td>261.40 (n/a)</td><td>85.37 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 (+16.76%)</td><td>0.01 (-18.09%)</td><td>0.01 <b>(-25.90%)</b></td><td>0.00 <b>(-48.28%)</b></td><td>0.01 <b>(+28.63%)</b></td><td>1118.10 <b>(+93.34%)</b></td><td>596.80 <b>(+41.08%)</b></td><td>592.10 <b>(+34.94%)</b></td><td>224.20 (-14.36%)</td><td>329.37 <b>(+110.61%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.30 (n/a)</td><td>423.02 (n/a)</td><td>438.80 (n/a)</td><td>261.80 (n/a)</td><td>156.39 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 <b>(+22.43%)</b></td><td>0.01 <b>(+23.62%)</b></td><td>0.01 (+5.16%)</td><td>0.01 <b>(+246.20%)</b></td><td>0.00 (-16.50%)</td><td>594.20 <b>(-71.12%)</b></td><td>451.28 <b>(-41.92%)</b></td><td>449.20 (-4.89%)</td><td>271.30 (-18.31%)</td><td>122.48 <b>(-83.03%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2057.20 (n/a)</td><td>777.02 (n/a)</td><td>472.30 (n/a)</td><td>332.10 (n/a)</td><td>721.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (+17.27%)</td><td>0.02 (-2.94%)</td><td>0.02 (-15.54%)</td><td>0.01 <b>(+27.29%)</b></td><td>0.01 <b>(+20.64%)</b></td><td>496.70 <b>(-21.45%)</b></td><td>340.18 (+2.02%)</td><td>322.00 (+18.43%)</td><td>208.20 (-14.71%)</td><td>129.46 <b>(-22.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>632.30 (n/a)</td><td>333.44 (n/a)</td><td>271.90 (n/a)</td><td>244.10 (n/a)</td><td>167.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 <b>(+30.29%)</b></td><td>0.01 (-2.00%)</td><td>0.01 <b>(-20.93%)</b></td><td>0.01 (+15.84%)</td><td>0.01 <b>(+49.11%)</b></td><td>519.60 (-13.67%)</td><td>407.78 (+4.59%)</td><td>451.90 <b>(+26.44%)</b></td><td>234.60 <b>(-23.26%)</b></td><td>117.49 (-3.81%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>601.90 (n/a)</td><td>389.90 (n/a)</td><td>357.40 (n/a)</td><td>305.70 (n/a)</td><td>122.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>286.20 (n/a)</td><td>259.12 (n/a)</td><td>265.30 (n/a)</td><td>211.10 (n/a)</td><td>28.43 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>599.20 (n/a)</td><td>449.26 (n/a)</td><td>548.00 (n/a)</td><td>264.80 (n/a)</td><td>167.32 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.50 (n/a)</td><td>400.90 (n/a)</td><td>401.20 (n/a)</td><td>252.00 (n/a)</td><td>97.41 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>499.20 (n/a)</td><td>309.42 (n/a)</td><td>272.10 (n/a)</td><td>234.50 (n/a)</td><td>107.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.90 (n/a)</td><td>378.08 (n/a)</td><td>361.20 (n/a)</td><td>253.60 (n/a)</td><td>125.24 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>470.70 (n/a)</td><td>377.70 (n/a)</td><td>420.20 (n/a)</td><td>180.60 (n/a)</td><td>114.62 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.60 (n/a)</td><td>399.66 (n/a)</td><td>432.40 (n/a)</td><td>279.30 (n/a)</td><td>98.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.60 (n/a)</td><td>336.92 (n/a)</td><td>256.70 (n/a)</td><td>227.90 (n/a)</td><td>137.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.10 (n/a)</td><td>382.52 (n/a)</td><td>275.70 (n/a)</td><td>222.30 (n/a)</td><td>187.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.90 (n/a)</td><td>334.14 (n/a)</td><td>276.80 (n/a)</td><td>235.70 (n/a)</td><td>142.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.90 (n/a)</td><td>419.44 (n/a)</td><td>478.70 (n/a)</td><td>241.90 (n/a)</td><td>164.52 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1019.70 (n/a)</td><td>579.98 (n/a)</td><td>477.70 (n/a)</td><td>405.80 (n/a)</td><td>252.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.40 <b>(-38.99%)</b></td><td>0.35 <b>(-25.29%)</b></td><td>0.38 (-16.59%)</td><td>0.23 <b>(-31.35%)</b></td><td>0.07 <b>(-42.34%)</b></td><td>976.40 <b>(+45.67%)</b></td><td>669.72 <b>(+32.80%)</b></td><td>588.10 (+19.90%)</td><td>548.70 <b>(+63.94%)</b></td><td>177.17 <b>(+43.61%)</b></td><td>17.20 <b>(-38.99%)</b></td><td>14.73 <b>(-25.29%)</b></td><td>16.05 (-16.59%)</td><td>9.67 <b>(-31.35%)</b></td><td>3.05 <b>(-42.34%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.66 (n/a)</td><td>0.46 (n/a)</td><td>0.45 (n/a)</td><td>0.33 (n/a)</td><td>0.12 (n/a)</td><td>670.30 (n/a)</td><td>504.30 (n/a)</td><td>490.50 (n/a)</td><td>334.70 (n/a)</td><td>123.36 (n/a)</td><td>28.19 (n/a)</td><td>19.72 (n/a)</td><td>19.24 (n/a)</td><td>14.08 (n/a)</td><td>5.29 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.52 <b>(+27.50%)</b></td><td>0.44 <b>(+22.99%)</b></td><td>0.41 (+14.11%)</td><td>0.38 (+19.13%)</td><td>0.06 <b>(+103.94%)</b></td><td>583.50 (-16.06%)</td><td>509.00 (-17.86%)</td><td>544.50 (-12.36%)</td><td>429.00 <b>(-21.57%)</b></td><td>70.67 <b>(+31.82%)</b></td><td>22.00 <b>(+27.50%)</b></td><td>18.84 <b>(+22.99%)</b></td><td>17.33 (+14.11%)</td><td>16.17 (+19.13%)</td><td>2.72 <b>(+103.94%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.03 (n/a)</td><td>695.10 (n/a)</td><td>619.70 (n/a)</td><td>621.30 (n/a)</td><td>547.00 (n/a)</td><td>53.61 (n/a)</td><td>17.25 (n/a)</td><td>15.32 (n/a)</td><td>15.19 (n/a)</td><td>13.58 (n/a)</td><td>1.33 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.31 (-1.45%)</td><td>0.31 (-0.54%)</td><td>0.31 (-0.44%)</td><td>0.30 (-0.02%)</td><td>0.00 <b>(-47.37%)</b></td><td>83618.80 (+0.02%)</td><td>82451.88 (+0.52%)</td><td>82269.00 (+0.45%)</td><td>81638.70 (+1.47%)</td><td>804.21 <b>(-46.64%)</b></td><td>210.44 (-1.45%)</td><td>208.38 (-0.54%)</td><td>208.83 (-0.44%)</td><td>205.45 (-0.02%)</td><td>2.02 <b>(-47.37%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>83603.40 (n/a)</td><td>82023.64 (n/a)</td><td>81903.40 (n/a)</td><td>80454.70 (n/a)</td><td>1507.16 (n/a)</td><td>213.53 (n/a)</td><td>209.51 (n/a)</td><td>209.76 (n/a)</td><td>205.49 (n/a)</td><td>3.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>1.03 (+0.04%)</td><td>1.01 (-1.39%)</td><td>1.00 (-1.72%)</td><td>0.99 (-1.06%)</td><td>0.01 <b>(+52.99%)</b></td><td>25326.60 (+1.07%)</td><td>25019.68 (+1.42%)</td><td>25057.00 (+1.75%)</td><td>24428.10 (-0.04%)</td><td>355.16 <b>(+53.94%)</b></td><td>703.28 (+0.04%)</td><td>686.77 (-1.39%)</td><td>685.63 (-1.72%)</td><td>678.33 (-1.06%)</td><td>9.88 <b>(+52.98%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25057.80 (n/a)</td><td>24670.26 (n/a)</td><td>24626.20 (n/a)</td><td>24437.30 (n/a)</td><td>230.71 (n/a)</td><td>703.02 (n/a)</td><td>696.43 (n/a)</td><td>697.63 (n/a)</td><td>685.61 (n/a)</td><td>6.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>2.31 <b>(-33.77%)</b></td><td>1.96 (-3.98%)</td><td>1.93 (+14.95%)</td><td>1.69 <b>(+27.40%)</b></td><td>0.22 <b>(-73.63%)</b></td><td>4758.00 <b>(-21.51%)</b></td><td>4158.24 (-5.36%)</td><td>4174.00 (-13.01%)</td><td>3494.60 <b>(+50.97%)</b></td><td>453.85 <b>(-67.18%)</b></td><td>604.91 <b>(-33.77%)</b></td><td>513.44 (-3.98%)</td><td>506.45 (+14.95%)</td><td>444.29 <b>(+27.40%)</b></td><td>58.40 <b>(-73.63%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>3.48 (n/a)</td><td>2.04 (n/a)</td><td>1.68 (n/a)</td><td>1.33 (n/a)</td><td>0.84 (n/a)</td><td>6061.80 (n/a)</td><td>4393.58 (n/a)</td><td>4798.00 (n/a)</td><td>2314.70 (n/a)</td><td>1382.73 (n/a)</td><td>913.28 (n/a)</td><td>534.74 (n/a)</td><td>440.59 (n/a)</td><td>348.73 (n/a)</td><td>221.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.34 (+6.58%)</td><td>0.25 (+9.18%)</td><td>0.25 (+18.91%)</td><td>0.17 (-2.21%)</td><td>0.06 (+9.19%)</td><td>7148.80 (+2.26%)</td><td>5215.98 (-7.83%)</td><td>4935.90 (-15.91%)</td><td>3622.00 (-6.18%)</td><td>1293.71 (+7.17%)</td><td>18.53 (+6.58%)</td><td>13.51 (+9.18%)</td><td>13.60 (+18.91%)</td><td>9.39 (-2.21%)</td><td>3.35 (+9.19%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>6990.80 (n/a)</td><td>5658.88 (n/a)</td><td>5869.50 (n/a)</td><td>3860.40 (n/a)</td><td>1207.19 (n/a)</td><td>17.38 (n/a)</td><td>12.37 (n/a)</td><td>11.43 (n/a)</td><td>9.60 (n/a)</td><td>3.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.16 (+18.62%)</td><td>0.08 (-7.32%)</td><td>0.07 <b>(-20.55%)</b></td><td>0.05 (-5.94%)</td><td>0.04 <b>(+55.05%)</b></td><td>0.15 (+18.62%)</td><td>0.08 (-7.32%)</td><td>0.07 <b>(-20.55%)</b></td><td>0.05 (-5.94%)</td><td>0.04 <b>(+55.05%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>3.91 (-0.00%)</td><td>3.66 (+1.37%)</td><td>3.61 (-3.56%)</td><td>3.52 (+6.15%)</td><td>0.15 <b>(-45.59%)</b></td><td>3.91 (-0.00%)</td><td>3.66 (+1.37%)</td><td>3.61 (-3.56%)</td><td>3.52 (+6.15%)</td><td>0.15 <b>(-45.59%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>3.91 (n/a)</td><td>3.61 (n/a)</td><td>3.75 (n/a)</td><td>3.31 (n/a)</td><td>0.27 (n/a)</td><td>3.91 (n/a)</td><td>3.61 (n/a)</td><td>3.74 (n/a)</td><td>3.31 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>7.40 (+1.75%)</td><td>6.36 (+0.35%)</td><td>6.60 (+4.72%)</td><td>5.51 (-3.33%)</td><td>0.80 <b>(+37.68%)</b></td><td>7.39 (+1.75%)</td><td>6.36 (+0.35%)</td><td>6.60 (+4.72%)</td><td>5.51 (-3.33%)</td><td>0.80 <b>(+37.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>7.27 (n/a)</td><td>6.34 (n/a)</td><td>6.31 (n/a)</td><td>5.70 (n/a)</td><td>0.58 (n/a)</td><td>7.27 (n/a)</td><td>6.34 (n/a)</td><td>6.30 (n/a)</td><td>5.70 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>13.94 <b>(+46.21%)</b></td><td>10.17 <b>(+20.51%)</b></td><td>8.22 (-3.91%)</td><td>7.15 (-1.54%)</td><td>3.24 <b>(+230.15%)</b></td><td>13.93 <b>(+46.21%)</b></td><td>10.16 <b>(+20.51%)</b></td><td>8.22 (-3.91%)</td><td>7.14 (-1.54%)</td><td>3.24 <b>(+230.15%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>9.53 (n/a)</td><td>8.44 (n/a)</td><td>8.56 (n/a)</td><td>7.26 (n/a)</td><td>0.98 (n/a)</td><td>9.53 (n/a)</td><td>8.43 (n/a)</td><td>8.55 (n/a)</td><td>7.25 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>3.86 (-1.49%)</td><td>3.65 (-2.96%)</td><td>3.64 (-3.67%)</td><td>3.41 (-6.42%)</td><td>0.17 <b>(+58.64%)</b></td><td>3.86 (-1.49%)</td><td>3.65 (-2.96%)</td><td>3.63 (-3.67%)</td><td>3.41 (-6.42%)</td><td>0.17 <b>(+58.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>3.92 (n/a)</td><td>3.76 (n/a)</td><td>3.77 (n/a)</td><td>3.64 (n/a)</td><td>0.11 (n/a)</td><td>3.92 (n/a)</td><td>3.76 (n/a)</td><td>3.77 (n/a)</td><td>3.64 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>7.53 (+8.89%)</td><td>7.21 (+15.36%)</td><td>7.14 (+17.52%)</td><td>6.79 (+19.95%)</td><td>0.32 <b>(-46.72%)</b></td><td>7.53 (+8.89%)</td><td>7.20 (+15.36%)</td><td>7.13 (+17.52%)</td><td>6.79 (+19.95%)</td><td>0.32 <b>(-46.72%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>6.92 (n/a)</td><td>6.25 (n/a)</td><td>6.07 (n/a)</td><td>5.66 (n/a)</td><td>0.60 (n/a)</td><td>6.91 (n/a)</td><td>6.24 (n/a)</td><td>6.07 (n/a)</td><td>5.66 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>13.80 (-2.24%)</td><td>9.23 (-15.20%)</td><td>8.18 <b>(-29.58%)</b></td><td>7.42 (+0.44%)</td><td>2.59 <b>(-21.99%)</b></td><td>13.79 (-2.24%)</td><td>9.22 (-15.20%)</td><td>8.17 <b>(-29.58%)</b></td><td>7.41 (+0.44%)</td><td>2.59 <b>(-21.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>14.12 (n/a)</td><td>10.88 (n/a)</td><td>11.61 (n/a)</td><td>7.39 (n/a)</td><td>3.32 (n/a)</td><td>14.11 (n/a)</td><td>10.88 (n/a)</td><td>11.60 (n/a)</td><td>7.38 (n/a)</td><td>3.32 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.10 (n/a)</td><td>307.20 (n/a)</td><td>241.50 (n/a)</td><td>207.30 (n/a)</td><td>117.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1393.90 (n/a)</td><td>552.52 (n/a)</td><td>272.00 (n/a)</td><td>256.10 (n/a)</td><td>488.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>448.30 (n/a)</td><td>273.18 (n/a)</td><td>248.00 (n/a)</td><td>179.20 (n/a)</td><td>102.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2456.60 (n/a)</td><td>867.06 (n/a)</td><td>556.10 (n/a)</td><td>283.60 (n/a)</td><td>902.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.50 (n/a)</td><td>440.54 (n/a)</td><td>500.40 (n/a)</td><td>237.00 (n/a)</td><td>163.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>744.40 (n/a)</td><td>456.50 (n/a)</td><td>375.90 (n/a)</td><td>305.90 (n/a)</td><td>177.27 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (+18.36%)</td><td>0.03 <b>(+34.27%)</b></td><td>0.03 <b>(+72.76%)</b></td><td>0.02 (+11.38%)</td><td>0.01 (+13.41%)</td><td>531.40 (-10.22%)</td><td>355.24 <b>(-25.72%)</b></td><td>309.70 <b>(-42.12%)</b></td><td>217.90 (-15.51%)</td><td>123.57 (-12.99%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.90 (n/a)</td><td>478.24 (n/a)</td><td>535.10 (n/a)</td><td>257.90 (n/a)</td><td>142.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 <b>(+21.30%)</b></td><td>0.03 <b>(+40.10%)</b></td><td>0.03 <b>(+60.01%)</b></td><td>0.01 (-4.51%)</td><td>0.01 <b>(+49.07%)</b></td><td>547.30 (+4.73%)</td><td>319.04 <b>(-25.04%)</b></td><td>291.40 <b>(-37.51%)</b></td><td>224.30 (-17.57%)</td><td>132.84 <b>(+31.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.60 (n/a)</td><td>425.62 (n/a)</td><td>466.30 (n/a)</td><td>272.10 (n/a)</td><td>100.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 <b>(+23.29%)</b></td><td>0.02 (+4.53%)</td><td>0.02 (-4.89%)</td><td>0.01 (-19.90%)</td><td>0.01 <b>(+46.95%)</b></td><td>629.40 <b>(+24.83%)</b></td><td>407.00 (+2.07%)</td><td>436.40 (+5.16%)</td><td>231.40 (-18.89%)</td><td>158.58 <b>(+45.97%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.20 (n/a)</td><td>398.76 (n/a)</td><td>415.00 (n/a)</td><td>285.30 (n/a)</td><td>108.64 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (-3.30%)</td><td>0.02 <b>(+27.61%)</b></td><td>0.02 <b>(+43.09%)</b></td><td>0.02 <b>(+40.25%)</b></td><td>0.01 <b>(-21.49%)</b></td><td>494.90 <b>(-28.69%)</b></td><td>383.66 <b>(-25.36%)</b></td><td>365.60 <b>(-30.11%)</b></td><td>279.40 (+3.44%)</td><td>98.58 <b>(-36.74%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>694.00 (n/a)</td><td>514.00 (n/a)</td><td>523.10 (n/a)</td><td>270.10 (n/a)</td><td>155.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (-3.01%)</td><td>0.02 <b>(-29.74%)</b></td><td>0.02 <b>(-46.63%)</b></td><td>0.01 <b>(-46.97%)</b></td><td>0.01 (+17.49%)</td><td>1053.20 <b>(+88.58%)</b></td><td>518.82 <b>(+62.48%)</b></td><td>473.70 <b>(+87.38%)</b></td><td>235.80 (+3.10%)</td><td>314.74 <b>(+129.93%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.50 (n/a)</td><td>319.32 (n/a)</td><td>252.80 (n/a)</td><td>228.70 (n/a)</td><td>136.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 (-8.37%)</td><td>0.01 (-9.78%)</td><td>0.01 (-15.88%)</td><td>0.01 (-15.98%)</td><td>0.01 (+15.83%)</td><td>1181.60 (+19.02%)</td><td>737.06 (+18.37%)</td><td>681.50 (+18.87%)</td><td>416.10 (+9.16%)</td><td>338.21 <b>(+41.42%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>992.80 (n/a)</td><td>622.66 (n/a)</td><td>573.30 (n/a)</td><td>381.20 (n/a)</td><td>239.16 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (+15.52%)</td><td>0.03 <b>(+74.31%)</b></td><td>0.03 <b>(+115.81%)</b></td><td>0.03 <b>(+212.95%)</b></td><td>0.00 <b>(-60.78%)</b></td><td>296.00 <b>(-68.05%)</b></td><td>253.82 <b>(-52.67%)</b></td><td>249.00 <b>(-53.67%)</b></td><td>217.90 (-13.43%)</td><td>29.27 <b>(-88.87%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>926.50 (n/a)</td><td>536.26 (n/a)</td><td>537.40 (n/a)</td><td>251.70 (n/a)</td><td>263.01 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.05 (-4.39%)</td><td>0.04 <b>(+26.27%)</b></td><td>0.05 <b>(+40.86%)</b></td><td>0.02 <b>(+56.75%)</b></td><td>0.01 <b>(-27.32%)</b></td><td>516.10 <b>(-36.21%)</b></td><td>310.90 <b>(-29.51%)</b></td><td>256.00 <b>(-28.99%)</b></td><td>243.80 (+4.59%)</td><td>115.86 <b>(-50.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>809.00 (n/a)</td><td>441.06 (n/a)</td><td>360.50 (n/a)</td><td>233.10 (n/a)</td><td>233.25 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (+10.78%)</td><td>0.03 <b>(+46.55%)</b></td><td>0.03 <b>(+77.69%)</b></td><td>0.02 <b>(+64.08%)</b></td><td>0.01 (-7.04%)</td><td>471.60 <b>(-39.05%)</b></td><td>322.00 <b>(-35.55%)</b></td><td>279.80 <b>(-43.72%)</b></td><td>230.70 (-9.74%)</td><td>99.65 <b>(-46.20%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>773.80 (n/a)</td><td>499.60 (n/a)</td><td>497.20 (n/a)</td><td>255.60 (n/a)</td><td>185.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (+7.52%)</td><td>0.03 <b>(+22.09%)</b></td><td>0.02 (-9.14%)</td><td>0.02 <b>(+198.41%)</b></td><td>0.01 (-0.56%)</td><td>620.50 <b>(-66.49%)</b></td><td>459.24 <b>(-36.46%)</b></td><td>526.50 (+10.05%)</td><td>244.00 (-6.98%)</td><td>181.15 <b>(-71.73%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1851.60 (n/a)</td><td>722.74 (n/a)</td><td>478.40 (n/a)</td><td>262.30 (n/a)</td><td>640.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 <b>(+27.96%)</b></td><td>0.02 (+8.63%)</td><td>0.03 (+2.14%)</td><td>0.01 (+5.60%)</td><td>0.01 <b>(+30.07%)</b></td><td>570.40 (-5.30%)</td><td>390.74 (-5.31%)</td><td>324.60 (-2.11%)</td><td>215.40 <b>(-21.84%)</b></td><td>157.63 (+1.16%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.30 (n/a)</td><td>412.64 (n/a)</td><td>331.60 (n/a)</td><td>275.60 (n/a)</td><td>155.83 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (+13.39%)</td><td>0.03 (+18.54%)</td><td>0.03 <b>(+49.71%)</b></td><td>0.02 (+3.22%)</td><td>0.01 <b>(+44.71%)</b></td><td>538.80 (-3.13%)</td><td>367.92 (-10.53%)</td><td>296.10 <b>(-33.19%)</b></td><td>238.00 (-11.82%)</td><td>151.53 <b>(+29.12%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>556.20 (n/a)</td><td>411.20 (n/a)</td><td>443.20 (n/a)</td><td>269.90 (n/a)</td><td>117.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (-11.92%)</td><td>0.02 (-19.45%)</td><td>0.01 <b>(-47.72%)</b></td><td>0.01 (+2.36%)</td><td>0.01 (-3.81%)</td><td>609.50 (-2.31%)</td><td>472.70 <b>(+25.23%)</b></td><td>584.60 <b>(+91.23%)</b></td><td>260.30 (+13.52%)</td><td>170.39 (+8.23%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.90 (n/a)</td><td>377.46 (n/a)</td><td>305.70 (n/a)</td><td>229.30 (n/a)</td><td>157.43 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 <b>(+125.42%)</b></td><td>0.03 <b>(+62.60%)</b></td><td>0.02 <b>(+27.86%)</b></td><td>0.01 (+4.94%)</td><td>0.01 <b>(+851.91%)</b></td><td>614.80 (-4.70%)</td><td>410.20 <b>(-29.16%)</b></td><td>454.40 <b>(-21.79%)</b></td><td>233.70 <b>(-55.63%)</b></td><td>164.21 <b>(+275.56%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>645.10 (n/a)</td><td>579.08 (n/a)</td><td>581.00 (n/a)</td><td>526.70 (n/a)</td><td>43.73 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.03 (-12.04%)</td><td>0.02 (-12.98%)</td><td>0.02 (-3.85%)</td><td>0.00 (+15.72%)</td><td>0.01 <b>(-20.20%)</b></td><td>2049.90 (-13.58%)</td><td>760.20 (-3.74%)</td><td>520.20 (+4.00%)</td><td>251.00 (+13.68%)</td><td>729.71 (-18.49%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2372.10 (n/a)</td><td>789.76 (n/a)</td><td>500.20 (n/a)</td><td>220.80 (n/a)</td><td>895.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.04 (-3.66%)</td><td>0.02 <b>(-27.90%)</b></td><td>0.02 <b>(-40.19%)</b></td><td>0.01 <b>(-31.33%)</b></td><td>0.01 <b>(+35.36%)</b></td><td>627.10 <b>(+45.60%)</b></td><td>434.24 <b>(+48.14%)</b></td><td>445.00 <b>(+67.23%)</b></td><td>247.50 (+3.82%)</td><td>152.22 <b>(+94.24%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>430.70 (n/a)</td><td>293.12 (n/a)</td><td>266.10 (n/a)</td><td>238.40 (n/a)</td><td>78.37 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.02 <b>(-39.98%)</b></td><td>0.02 (-10.25%)</td><td>0.02 (-4.57%)</td><td>0.01 (+12.89%)</td><td>0.00 <b>(-70.31%)</b></td><td>577.00 (-11.41%)</td><td>491.68 (-0.04%)</td><td>521.10 (+4.81%)</td><td>393.30 <b>(+66.65%)</b></td><td>73.43 <b>(-53.89%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.30 (n/a)</td><td>491.86 (n/a)</td><td>497.20 (n/a)</td><td>236.00 (n/a)</td><td>159.27 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.36 (-14.87%)</td><td>0.25 (-2.40%)</td><td>0.30 <b>(+34.02%)</b></td><td>0.05 <b>(-62.95%)</b></td><td>0.13 (+4.14%)</td><td>2096.50 <b>(+169.92%)</b></td><td>693.70 <b>(+49.25%)</b></td><td>328.00 <b>(-25.39%)</b></td><td>272.10 (+17.49%)</td><td>788.22 <b>(+256.96%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>776.70 (n/a)</td><td>464.78 (n/a)</td><td>439.60 (n/a)</td><td>231.60 (n/a)</td><td>220.81 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.39 <b>(+37.13%)</b></td><td>0.29 <b>(+63.40%)</b></td><td>0.31 <b>(+60.17%)</b></td><td>0.18 <b>(+256.91%)</b></td><td>0.10 (+10.72%)</td><td>545.70 <b>(-71.98%)</b></td><td>370.90 <b>(-52.48%)</b></td><td>314.00 <b>(-37.56%)</b></td><td>250.00 <b>(-27.07%)</b></td><td>132.45 <b>(-79.93%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>0.09 (n/a)</td><td>1947.60 (n/a)</td><td>780.52 (n/a)</td><td>502.90 (n/a)</td><td>342.80 (n/a)</td><td>660.10 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.43 <b>(+59.23%)</b></td><td>0.30 <b>(+58.02%)</b></td><td>0.33 <b>(+91.86%)</b></td><td>0.17 (+11.87%)</td><td>0.11 <b>(+149.06%)</b></td><td>573.90 (-10.61%)</td><td>379.58 <b>(-30.17%)</b></td><td>297.00 <b>(-47.87%)</b></td><td>230.80 <b>(-37.20%)</b></td><td>159.84 <b>(+54.34%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>642.00 (n/a)</td><td>543.60 (n/a)</td><td>569.70 (n/a)</td><td>367.50 (n/a)</td><td>103.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.28 <b>(+44.81%)</b></td><td>0.24 <b>(+43.90%)</b></td><td>0.26 <b>(+50.20%)</b></td><td>0.13 (-9.76%)</td><td>0.06 <b>(+204.27%)</b></td><td>569.20 (+10.80%)</td><td>337.30 <b>(-25.46%)</b></td><td>287.20 <b>(-33.43%)</b></td><td>267.50 <b>(-30.95%)</b></td><td>129.91 <b>(+135.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>513.70 (n/a)</td><td>452.50 (n/a)</td><td>431.40 (n/a)</td><td>387.40 (n/a)</td><td>55.16 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.27 (+4.14%)</td><td>0.21 <b>(+40.13%)</b></td><td>0.19 <b>(+40.44%)</b></td><td>0.16 <b>(+331.48%)</b></td><td>0.04 <b>(-48.25%)</b></td><td>451.40 <b>(-76.83%)</b></td><td>371.12 <b>(-51.37%)</b></td><td>396.90 <b>(-28.79%)</b></td><td>276.60 (-3.96%)</td><td>70.88 <b>(-89.51%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>0.08 (n/a)</td><td>1947.80 (n/a)</td><td>763.12 (n/a)</td><td>557.40 (n/a)</td><td>288.00 (n/a)</td><td>675.98 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.23 (-3.72%)</td><td>0.18 (+0.94%)</td><td>0.18 <b>(+23.17%)</b></td><td>0.11 (-16.96%)</td><td>0.05 (-12.49%)</td><td>678.60 <b>(+20.43%)</b></td><td>440.04 (-0.87%)</td><td>413.70 (-18.82%)</td><td>321.40 (+3.84%)</td><td>139.77 (+18.05%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>563.50 (n/a)</td><td>443.88 (n/a)</td><td>509.60 (n/a)</td><td>309.50 (n/a)</td><td>118.40 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.49 <b>(+26.53%)</b></td><td>0.28 (+16.72%)</td><td>0.28 (+5.77%)</td><td>0.16 <b>(+147.06%)</b></td><td>0.13 (-7.62%)</td><td>820.00 <b>(-59.52%)</b></td><td>548.02 <b>(-36.41%)</b></td><td>473.90 (-5.47%)</td><td>265.40 <b>(-20.96%)</b></td><td>219.35 <b>(-69.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.39 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>0.14 (n/a)</td><td>2025.90 (n/a)</td><td>861.80 (n/a)</td><td>501.30 (n/a)</td><td>335.80 (n/a)</td><td>716.33 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.34 <b>(-22.25%)</b></td><td>0.21 <b>(-28.04%)</b></td><td>0.26 (-7.73%)</td><td>0.06 <b>(-66.64%)</b></td><td>0.11 (+18.04%)</td><td>2064.80 <b>(+199.72%)</b></td><td>900.82 <b>(+84.66%)</b></td><td>511.70 (+8.37%)</td><td>385.90 <b>(+28.59%)</b></td><td>698.50 <b>(+370.07%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>688.90 (n/a)</td><td>487.82 (n/a)</td><td>472.20 (n/a)</td><td>300.10 (n/a)</td><td>148.59 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.47 (-6.93%)</td><td>0.32 (+4.72%)</td><td>0.31 <b>(+20.75%)</b></td><td>0.17 (+7.17%)</td><td>0.12 (-16.48%)</td><td>768.90 (-6.69%)</td><td>468.80 (-9.00%)</td><td>428.50 (-17.18%)</td><td>276.60 (+7.42%)</td><td>196.15 (-14.89%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.51 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>824.00 (n/a)</td><td>515.14 (n/a)</td><td>517.40 (n/a)</td><td>257.50 (n/a)</td><td>230.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.00 <b>(-25.00%)</b></td><td>0.00 (-18.18%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-12.71%)</td><td>18650.65 (+4.88%)</td><td>13567.80 (+15.71%)</td><td>16862.69 <b>(+22.41%)</b></td><td>7098.01 <b>(+37.13%)</b></td><td>5934.85 (+12.41%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17782.11 (n/a)</td><td>11725.34 (n/a)</td><td>13775.42 (n/a)</td><td>5176.26 (n/a)</td><td>5279.68 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.00 (+14.29%)</td><td>0.00 <b>(-32.65%)</b></td><td>0.00 <b>(-66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+17.31%)</td><td>21177.89 (+11.48%)</td><td>16270.58 <b>(+59.22%)</b></td><td>18440.41 <b>(+162.92%)</b></td><td>5284.27 (-11.71%)</td><td>6572.98 (+16.40%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18997.36 (n/a)</td><td>10218.74 (n/a)</td><td>7013.58 (n/a)</td><td>5985.05 (n/a)</td><td>5646.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>0.14 (+5.69%)</td><td>0.10 (+13.86%)</td><td>0.10 (+18.07%)</td><td>0.08 (-2.20%)</td><td>0.03 <b>(+21.97%)</b></td><td>27830.72 (+2.32%)</td><td>21305.12 (-10.82%)</td><td>21990.48 (-15.27%)</td><td>15462.39 (-5.43%)</td><td>5216.31 (+18.77%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>27199.35 (n/a)</td><td>23890.15 (n/a)</td><td>25953.98 (n/a)</td><td>16350.74 (n/a)</td><td>4391.76 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>1.63 <b>(+49.52%)</b></td><td>1.14 (+11.58%)</td><td>0.91 (-13.01%)</td><td>0.83 (-14.54%)</td><td>0.38 <b>(+665.11%)</b></td><td>633.90 (+17.00%)</td><td>498.02 (-2.74%)</td><td>577.20 (+14.96%)</td><td>322.20 <b>(-33.11%)</b></td><td>149.40 <b>(+492.29%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>1.09 (n/a)</td><td>1.03 (n/a)</td><td>1.04 (n/a)</td><td>0.97 (n/a)</td><td>0.05 (n/a)</td><td>541.80 (n/a)</td><td>512.04 (n/a)</td><td>502.10 (n/a)</td><td>481.70 (n/a)</td><td>25.22 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>2.07 (-0.94%)</td><td>1.32 (+8.03%)</td><td>1.11 (+6.88%)</td><td>0.96 <b>(+85.89%)</b></td><td>0.46 <b>(-21.30%)</b></td><td>547.90 <b>(-46.21%)</b></td><td>430.40 (-18.76%)</td><td>471.60 (-6.43%)</td><td>253.70 (+0.91%)</td><td>123.02 <b>(-58.20%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:12:43</td><td>2.09 (n/a)</td><td>1.22 (n/a)</td><td>1.04 (n/a)</td><td>0.51 (n/a)</td><td>0.59 (n/a)</td><td>1018.50 (n/a)</td><td>529.80 (n/a)</td><td>504.00 (n/a)</td><td>251.40 (n/a)</td><td>294.28 (n/a)</td>
</tr>
</tbody>
</table>


</details>
