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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.05 <b>(+32.61%)</b></td><td>0.03 (+4.50%)</td><td>0.02 <b>(-32.43%)</b></td><td>0.02 (-10.74%)</td><td>0.02 <b>(+127.36%)</b></td><td>614.80 (+12.03%)</td><td>433.62 (+10.68%)</td><td>543.50 <b>(+47.97%)</b></td><td>225.10 <b>(-24.59%)</b></td><td>188.75 <b>(+84.71%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>548.80 (n/a)</td><td>391.78 (n/a)</td><td>367.30 (n/a)</td><td>298.50 (n/a)</td><td>102.19 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 <b>(-32.68%)</b></td><td>0.03 (-12.80%)</td><td>0.02 (-11.10%)</td><td>0.02 (+10.20%)</td><td>0.01 <b>(-52.29%)</b></td><td>571.70 (-9.25%)</td><td>472.94 (+2.82%)</td><td>523.00 (+12.50%)</td><td>291.30 <b>(+48.55%)</b></td><td>109.67 <b>(-33.26%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>630.00 (n/a)</td><td>459.98 (n/a)</td><td>464.90 (n/a)</td><td>196.10 (n/a)</td><td>164.32 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (-15.21%)</td><td>0.02 <b>(-30.70%)</b></td><td>0.02 <b>(-39.66%)</b></td><td>0.02 <b>(-22.46%)</b></td><td>0.01 (-4.19%)</td><td>662.70 <b>(+28.96%)</b></td><td>552.74 <b>(+46.02%)</b></td><td>593.60 <b>(+65.72%)</b></td><td>359.10 (+17.97%)</td><td>118.03 <b>(+40.04%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.90 (n/a)</td><td>378.54 (n/a)</td><td>358.20 (n/a)</td><td>304.40 (n/a)</td><td>84.28 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (-2.43%)</td><td>0.02 (+12.43%)</td><td>0.02 <b>(+32.12%)</b></td><td>0.01 <b>(+150.12%)</b></td><td>0.01 (-17.52%)</td><td>765.40 <b>(-60.02%)</b></td><td>374.14 <b>(-40.98%)</b></td><td>247.60 <b>(-24.30%)</b></td><td>189.40 (+2.49%)</td><td>235.40 <b>(-67.58%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1914.50 (n/a)</td><td>633.92 (n/a)</td><td>327.10 (n/a)</td><td>184.80 (n/a)</td><td>726.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.01 <b>(-36.63%)</b></td><td>0.01 <b>(-24.22%)</b></td><td>0.01 (+3.49%)</td><td>0.01 <b>(-26.00%)</b></td><td>0.00 <b>(-56.26%)</b></td><td>659.10 <b>(+35.12%)</b></td><td>452.30 <b>(+24.39%)</b></td><td>395.50 (-3.37%)</td><td>358.60 <b>(+57.77%)</b></td><td>121.72 (-0.96%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>487.80 (n/a)</td><td>363.60 (n/a)</td><td>409.30 (n/a)</td><td>227.30 (n/a)</td><td>122.90 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (-8.04%)</td><td>0.02 (+6.88%)</td><td>0.02 <b>(+27.75%)</b></td><td>0.01 (-4.66%)</td><td>0.00 (-11.04%)</td><td>483.50 (+4.88%)</td><td>328.00 (-6.69%)</td><td>284.10 <b>(-21.71%)</b></td><td>239.80 (+8.75%)</td><td>97.05 (+6.65%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>461.00 (n/a)</td><td>351.52 (n/a)</td><td>362.90 (n/a)</td><td>220.50 (n/a)</td><td>90.99 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (-8.48%)</td><td>0.02 (+18.03%)</td><td>0.02 <b>(+26.01%)</b></td><td>0.01 <b>(+218.35%)</b></td><td>0.01 <b>(-34.54%)</b></td><td>603.50 <b>(-68.59%)</b></td><td>376.98 <b>(-45.40%)</b></td><td>348.80 <b>(-20.64%)</b></td><td>246.00 (+9.28%)</td><td>146.04 <b>(-79.21%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1921.30 (n/a)</td><td>690.38 (n/a)</td><td>439.50 (n/a)</td><td>225.10 (n/a)</td><td>702.52 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (-19.73%)</td><td>0.02 (+1.81%)</td><td>0.02 <b>(+29.76%)</b></td><td>0.01 (-5.71%)</td><td>0.01 (-12.12%)</td><td>579.60 (+6.06%)</td><td>365.44 (-0.57%)</td><td>289.50 <b>(-22.94%)</b></td><td>237.90 <b>(+24.55%)</b></td><td>153.18 <b>(+20.57%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.50 (n/a)</td><td>367.54 (n/a)</td><td>375.70 (n/a)</td><td>191.00 (n/a)</td><td>127.04 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.01 <b>(-41.08%)</b></td><td>0.01 <b>(-23.64%)</b></td><td>0.01 (-12.70%)</td><td>0.01 <b>(-21.25%)</b></td><td>0.00 <b>(-50.90%)</b></td><td>690.20 <b>(+26.99%)</b></td><td>479.22 <b>(+24.57%)</b></td><td>415.50 (+14.53%)</td><td>356.30 <b>(+69.75%)</b></td><td>139.71 (+5.65%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>543.50 (n/a)</td><td>384.70 (n/a)</td><td>362.80 (n/a)</td><td>209.90 (n/a)</td><td>132.24 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>451.60 (n/a)</td><td>357.36 (n/a)</td><td>402.20 (n/a)</td><td>203.40 (n/a)</td><td>109.87 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>547.60 (n/a)</td><td>496.48 (n/a)</td><td>505.50 (n/a)</td><td>420.50 (n/a)</td><td>52.05 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1923.90 (n/a)</td><td>736.74 (n/a)</td><td>494.50 (n/a)</td><td>262.60 (n/a)</td><td>673.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.00 (n/a)</td><td>322.16 (n/a)</td><td>278.30 (n/a)</td><td>247.60 (n/a)</td><td>115.82 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>506.70 (n/a)</td><td>359.18 (n/a)</td><td>426.40 (n/a)</td><td>195.40 (n/a)</td><td>137.53 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>681.70 (n/a)</td><td>469.44 (n/a)</td><td>579.00 (n/a)</td><td>200.10 (n/a)</td><td>215.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1924.70 (n/a)</td><td>653.66 (n/a)</td><td>274.10 (n/a)</td><td>258.40 (n/a)</td><td>720.44 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>484.60 (n/a)</td><td>341.88 (n/a)</td><td>304.40 (n/a)</td><td>197.30 (n/a)</td><td>121.88 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.90 (n/a)</td><td>349.18 (n/a)</td><td>257.30 (n/a)</td><td>194.60 (n/a)</td><td>163.09 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.80 (n/a)</td><td>414.38 (n/a)</td><td>396.50 (n/a)</td><td>258.90 (n/a)</td><td>127.51 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>669.80 (n/a)</td><td>465.00 (n/a)</td><td>448.50 (n/a)</td><td>279.10 (n/a)</td><td>189.43 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>653.70 (n/a)</td><td>407.24 (n/a)</td><td>299.50 (n/a)</td><td>248.50 (n/a)</td><td>180.65 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.65 <b>(+28.49%)</b></td><td>0.51 <b>(+33.89%)</b></td><td>0.52 (+16.26%)</td><td>0.35 <b>(+171.49%)</b></td><td>0.11 <b>(-26.51%)</b></td><td>639.40 <b>(-63.17%)</b></td><td>455.44 <b>(-39.55%)</b></td><td>428.60 (-13.99%)</td><td>341.80 <b>(-22.18%)</b></td><td>111.43 <b>(-79.82%)</b></td><td>27.61 <b>(+28.49%)</b></td><td>21.61 <b>(+33.89%)</b></td><td>22.02 (+16.26%)</td><td>14.76 <b>(+171.49%)</b></td><td>4.65 <b>(-26.51%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.50 (n/a)</td><td>0.38 (n/a)</td><td>0.44 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>1735.90 (n/a)</td><td>753.42 (n/a)</td><td>498.30 (n/a)</td><td>439.20 (n/a)</td><td>552.26 (n/a)</td><td>21.49 (n/a)</td><td>16.14 (n/a)</td><td>18.94 (n/a)</td><td>5.44 (n/a)</td><td>6.32 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.50 (-2.36%)</td><td>0.38 (-7.18%)</td><td>0.37 (-16.12%)</td><td>0.21 <b>(-30.12%)</b></td><td>0.12 <b>(+25.78%)</b></td><td>1077.40 <b>(+43.10%)</b></td><td>638.66 (+13.99%)</td><td>593.00 (+19.22%)</td><td>441.70 (+2.41%)</td><td>259.83 <b>(+83.22%)</b></td><td>21.36 (-2.36%)</td><td>16.41 (-7.18%)</td><td>15.92 (-16.12%)</td><td>8.76 <b>(-30.12%)</b></td><td>5.19 <b>(+25.78%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.10 (n/a)</td><td>752.90 (n/a)</td><td>560.30 (n/a)</td><td>497.40 (n/a)</td><td>431.30 (n/a)</td><td>141.81 (n/a)</td><td>21.88 (n/a)</td><td>17.67 (n/a)</td><td>18.97 (n/a)</td><td>12.53 (n/a)</td><td>4.13 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.31 (+1.28%)</td><td>0.31 (+0.54%)</td><td>0.31 (+1.26%)</td><td>0.30 (-0.67%)</td><td>0.01 <b>(+69.43%)</b></td><td>83783.80 (+0.68%)</td><td>81983.54 (-0.52%)</td><td>81611.20 (-1.24%)</td><td>80305.80 (-1.26%)</td><td>1425.64 <b>(+68.52%)</b></td><td>213.93 (+1.28%)</td><td>209.60 (+0.54%)</td><td>210.51 (+1.26%)</td><td>205.05 (-0.67%)</td><td>3.64 <b>(+69.43%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83218.80 (n/a)</td><td>82414.68 (n/a)</td><td>82635.90 (n/a)</td><td>81333.30 (n/a)</td><td>845.99 (n/a)</td><td>211.23 (n/a)</td><td>208.47 (n/a)</td><td>207.90 (n/a)</td><td>206.44 (n/a)</td><td>2.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>1.03 (-0.32%)</td><td>1.01 (+0.27%)</td><td>1.01 (-0.05%)</td><td>1.00 (+1.13%)</td><td>0.01 <b>(-30.38%)</b></td><td>25155.80 (-1.12%)</td><td>24846.00 (-0.28%)</td><td>24858.90 (+0.05%)</td><td>24369.90 (+0.32%)</td><td>297.47 <b>(-31.01%)</b></td><td>704.96 (-0.32%)</td><td>691.53 (+0.27%)</td><td>691.09 (-0.05%)</td><td>682.94 (+1.13%)</td><td>8.35 <b>(-30.38%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>1.04 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>0.99 (n/a)</td><td>0.02 (n/a)</td><td>25440.40 (n/a)</td><td>24916.20 (n/a)</td><td>24846.90 (n/a)</td><td>24292.50 (n/a)</td><td>431.16 (n/a)</td><td>707.21 (n/a)</td><td>689.67 (n/a)</td><td>691.43 (n/a)</td><td>675.30 (n/a)</td><td>11.99 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>3.78 (+9.66%)</td><td>2.16 <b>(-21.24%)</b></td><td>1.85 <b>(-30.87%)</b></td><td>1.52 <b>(-22.22%)</b></td><td>0.92 <b>(+39.11%)</b></td><td>5308.70 <b>(+28.56%)</b></td><td>4134.84 <b>(+33.98%)</b></td><td>4351.30 <b>(+44.65%)</b></td><td>2132.70 (-8.81%)</td><td>1205.81 <b>(+56.85%)</b></td><td>991.18 (+9.66%)</td><td>566.40 <b>(-21.24%)</b></td><td>485.82 <b>(-30.87%)</b></td><td>398.20 <b>(-22.22%)</b></td><td>241.34 <b>(+39.11%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>3.45 (n/a)</td><td>2.74 (n/a)</td><td>2.68 (n/a)</td><td>1.95 (n/a)</td><td>0.66 (n/a)</td><td>4129.30 (n/a)</td><td>3086.20 (n/a)</td><td>3008.10 (n/a)</td><td>2338.80 (n/a)</td><td>768.75 (n/a)</td><td>903.85 (n/a)</td><td>719.16 (n/a)</td><td>702.76 (n/a)</td><td>511.94 (n/a)</td><td>173.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.27 (-10.62%)</td><td>0.21 (+4.17%)</td><td>0.21 (+6.83%)</td><td>0.17 <b>(+29.40%)</b></td><td>0.04 <b>(-35.15%)</b></td><td>7287.50 <b>(-22.72%)</b></td><td>6002.22 (-8.10%)</td><td>5930.00 (-6.39%)</td><td>4531.10 (+11.88%)</td><td>1102.87 <b>(-42.65%)</b></td><td>14.81 (-10.62%)</td><td>11.51 (+4.17%)</td><td>11.32 (+6.83%)</td><td>9.21 <b>(+29.40%)</b></td><td>2.23 <b>(-35.15%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>9429.70 (n/a)</td><td>6531.54 (n/a)</td><td>6334.90 (n/a)</td><td>4050.00 (n/a)</td><td>1923.07 (n/a)</td><td>16.57 (n/a)</td><td>11.05 (n/a)</td><td>10.59 (n/a)</td><td>7.12 (n/a)</td><td>3.44 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>3.94 (n/a)</td><td>3.69 (n/a)</td><td>3.71 (n/a)</td><td>3.52 (n/a)</td><td>0.17 (n/a)</td><td>3.94 (n/a)</td><td>3.69 (n/a)</td><td>3.70 (n/a)</td><td>3.52 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>7.17 (-5.51%)</td><td>6.24 (-12.33%)</td><td>5.91 (-16.32%)</td><td>5.48 (-17.26%)</td><td>0.72 <b>(+80.73%)</b></td><td>7.17 (-5.51%)</td><td>6.23 (-12.33%)</td><td>5.91 (-16.32%)</td><td>5.47 (-17.26%)</td><td>0.72 <b>(+80.73%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>7.59 (n/a)</td><td>7.12 (n/a)</td><td>7.06 (n/a)</td><td>6.62 (n/a)</td><td>0.40 (n/a)</td><td>7.58 (n/a)</td><td>7.11 (n/a)</td><td>7.06 (n/a)</td><td>6.61 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>9.88 (+0.23%)</td><td>8.04 (-8.06%)</td><td>8.04 (-5.80%)</td><td>6.81 (-11.49%)</td><td>1.16 <b>(+32.21%)</b></td><td>9.87 (+0.23%)</td><td>8.04 (-8.06%)</td><td>8.04 (-5.80%)</td><td>6.81 (-11.49%)</td><td>1.16 <b>(+32.21%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>9.86 (n/a)</td><td>8.75 (n/a)</td><td>8.54 (n/a)</td><td>7.70 (n/a)</td><td>0.88 (n/a)</td><td>9.85 (n/a)</td><td>8.74 (n/a)</td><td>8.54 (n/a)</td><td>7.69 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>3.91 (n/a)</td><td>3.69 (n/a)</td><td>3.77 (n/a)</td><td>3.40 (n/a)</td><td>0.23 (n/a)</td><td>3.90 (n/a)</td><td>3.69 (n/a)</td><td>3.77 (n/a)</td><td>3.40 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>7.58 (+0.25%)</td><td>6.07 (-11.33%)</td><td>5.81 (-16.44%)</td><td>4.80 (-16.04%)</td><td>1.21 <b>(+69.68%)</b></td><td>7.58 (+0.25%)</td><td>6.07 (-11.33%)</td><td>5.81 (-16.44%)</td><td>4.80 (-16.04%)</td><td>1.21 <b>(+69.68%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>7.56 (n/a)</td><td>6.85 (n/a)</td><td>6.95 (n/a)</td><td>5.72 (n/a)</td><td>0.72 (n/a)</td><td>7.56 (n/a)</td><td>6.85 (n/a)</td><td>6.95 (n/a)</td><td>5.72 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>13.39 (-4.46%)</td><td>9.94 (-8.43%)</td><td>9.67 (+0.37%)</td><td>8.33 (+8.78%)</td><td>2.06 <b>(-25.08%)</b></td><td>13.38 (-4.46%)</td><td>9.94 (-8.43%)</td><td>9.67 (+0.37%)</td><td>8.32 (+8.78%)</td><td>2.06 <b>(-25.08%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>14.02 (n/a)</td><td>10.86 (n/a)</td><td>9.64 (n/a)</td><td>7.65 (n/a)</td><td>2.75 (n/a)</td><td>14.01 (n/a)</td><td>10.85 (n/a)</td><td>9.63 (n/a)</td><td>7.65 (n/a)</td><td>2.75 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>2.84 (+0.19%)</td><td>2.10 (+6.68%)</td><td>2.22 (+14.60%)</td><td>1.01 <b>(-20.64%)</b></td><td>0.77 <b>(+34.20%)</b></td><td>2.84 (+0.19%)</td><td>2.09 (+6.68%)</td><td>2.22 (+14.60%)</td><td>1.01 <b>(-20.64%)</b></td><td>0.77 <b>(+34.20%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>2.84 (n/a)</td><td>1.97 (n/a)</td><td>1.94 (n/a)</td><td>1.27 (n/a)</td><td>0.57 (n/a)</td><td>2.83 (n/a)</td><td>1.96 (n/a)</td><td>1.94 (n/a)</td><td>1.27 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.47 <b>(-23.00%)</b></td><td>0.40 (-1.36%)</td><td>0.41 (-5.85%)</td><td>0.32 <b>(+325.14%)</b></td><td>0.06 <b>(-73.56%)</b></td><td>0.47 <b>(-23.00%)</b></td><td>0.40 (-1.36%)</td><td>0.40 (-5.85%)</td><td>0.32 <b>(+325.14%)</b></td><td>0.06 <b>(-73.56%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.62 (n/a)</td><td>0.41 (n/a)</td><td>0.44 (n/a)</td><td>0.08 (n/a)</td><td>0.21 (n/a)</td><td>0.61 (n/a)</td><td>0.40 (n/a)</td><td>0.43 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.78 (+4.26%)</td><td>0.57 (+2.27%)</td><td>0.61 (+12.12%)</td><td>0.38 (-2.56%)</td><td>0.16 (+6.38%)</td><td>0.77 (+4.26%)</td><td>0.56 (+2.27%)</td><td>0.61 (+12.12%)</td><td>0.37 (-2.56%)</td><td>0.16 (+6.38%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.75 (n/a)</td><td>0.56 (n/a)</td><td>0.55 (n/a)</td><td>0.39 (n/a)</td><td>0.15 (n/a)</td><td>0.74 (n/a)</td><td>0.55 (n/a)</td><td>0.54 (n/a)</td><td>0.38 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>2.01 (-15.44%)</td><td>1.29 (-18.58%)</td><td>1.52 (-14.16%)</td><td>0.44 <b>(-46.21%)</b></td><td>0.79 (+9.59%)</td><td>1.97 (-15.44%)</td><td>1.26 (-18.58%)</td><td>1.50 (-14.16%)</td><td>0.44 <b>(-46.21%)</b></td><td>0.78 (+9.59%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>2.37 (n/a)</td><td>1.58 (n/a)</td><td>1.77 (n/a)</td><td>0.82 (n/a)</td><td>0.72 (n/a)</td><td>2.33 (n/a)</td><td>1.55 (n/a)</td><td>1.74 (n/a)</td><td>0.81 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.90 (n/a)</td><td>341.00 (n/a)</td><td>292.90 (n/a)</td><td>267.00 (n/a)</td><td>96.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1940.60 (n/a)</td><td>675.02 (n/a)</td><td>393.80 (n/a)</td><td>263.90 (n/a)</td><td>713.19 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>458.70 (n/a)</td><td>362.16 (n/a)</td><td>383.50 (n/a)</td><td>254.60 (n/a)</td><td>98.21 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>676.70 (n/a)</td><td>522.28 (n/a)</td><td>549.90 (n/a)</td><td>291.00 (n/a)</td><td>143.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1792.20 (n/a)</td><td>667.94 (n/a)</td><td>416.80 (n/a)</td><td>310.80 (n/a)</td><td>633.56 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.10 (n/a)</td><td>458.72 (n/a)</td><td>411.10 (n/a)</td><td>316.20 (n/a)</td><td>143.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (-14.93%)</td><td>0.02 (-10.03%)</td><td>0.02 (-9.56%)</td><td>0.02 (-0.75%)</td><td>0.01 <b>(-22.02%)</b></td><td>526.10 (+0.77%)</td><td>396.72 (+8.59%)</td><td>356.70 (+10.57%)</td><td>282.70 (+17.55%)</td><td>116.38 (-6.42%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.10 (n/a)</td><td>365.34 (n/a)</td><td>322.60 (n/a)</td><td>240.50 (n/a)</td><td>124.36 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (-12.07%)</td><td>0.02 (-2.47%)</td><td>0.02 (-6.61%)</td><td>0.02 (+2.34%)</td><td>0.01 <b>(-26.85%)</b></td><td>537.30 (-2.29%)</td><td>369.94 (-2.48%)</td><td>349.20 (+7.08%)</td><td>268.80 (+13.71%)</td><td>110.96 <b>(-23.74%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.90 (n/a)</td><td>379.36 (n/a)</td><td>326.10 (n/a)</td><td>236.40 (n/a)</td><td>145.51 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (-13.71%)</td><td>0.02 (-2.51%)</td><td>0.03 (+0.02%)</td><td>0.02 <b>(+25.10%)</b></td><td>0.01 <b>(-33.84%)</b></td><td>459.00 <b>(-20.05%)</b></td><td>346.08 (-2.92%)</td><td>292.00 (+0.00%)</td><td>288.60 (+15.86%)</td><td>79.11 <b>(-41.04%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.10 (n/a)</td><td>356.50 (n/a)</td><td>292.00 (n/a)</td><td>249.10 (n/a)</td><td>134.18 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (+14.95%)</td><td>0.02 <b>(+20.60%)</b></td><td>0.02 <b>(+28.44%)</b></td><td>0.02 (+6.16%)</td><td>0.01 <b>(+31.93%)</b></td><td>521.40 (-5.82%)</td><td>364.24 (-15.31%)</td><td>344.20 <b>(-22.14%)</b></td><td>251.80 (-13.02%)</td><td>117.31 (+3.77%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.60 (n/a)</td><td>430.08 (n/a)</td><td>442.10 (n/a)</td><td>289.50 (n/a)</td><td>113.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (-5.00%)</td><td>0.02 (+3.29%)</td><td>0.02 (+12.84%)</td><td>0.01 (-1.43%)</td><td>0.01 (-7.87%)</td><td>594.30 (+1.45%)</td><td>399.50 (-5.26%)</td><td>447.20 (-11.38%)</td><td>230.70 (+5.25%)</td><td>153.65 (-6.98%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.80 (n/a)</td><td>421.68 (n/a)</td><td>504.60 (n/a)</td><td>219.20 (n/a)</td><td>165.18 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (+12.16%)</td><td>0.02 <b>(+22.54%)</b></td><td>0.02 (+1.75%)</td><td>0.01 <b>(+77.85%)</b></td><td>0.01 (+6.68%)</td><td>599.30 <b>(-43.78%)</b></td><td>408.82 <b>(-25.90%)</b></td><td>442.80 (-1.71%)</td><td>236.30 (-10.83%)</td><td>162.04 <b>(-49.82%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1065.90 (n/a)</td><td>551.72 (n/a)</td><td>450.50 (n/a)</td><td>265.00 (n/a)</td><td>322.89 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (-4.78%)</td><td>0.02 (-18.84%)</td><td>0.02 <b>(-34.52%)</b></td><td>0.01 (+3.43%)</td><td>0.01 (+3.39%)</td><td>564.90 (-3.30%)</td><td>467.50 <b>(+24.65%)</b></td><td>504.50 <b>(+52.69%)</b></td><td>213.70 (+5.01%)</td><td>144.68 (+0.73%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.20 (n/a)</td><td>375.06 (n/a)</td><td>330.40 (n/a)</td><td>203.50 (n/a)</td><td>143.62 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 <b>(-21.46%)</b></td><td>0.02 <b>(-26.15%)</b></td><td>0.02 <b>(-40.91%)</b></td><td>0.01 (-6.07%)</td><td>0.00 <b>(-46.23%)</b></td><td>602.00 (+6.45%)</td><td>512.42 <b>(+29.98%)</b></td><td>526.70 <b>(+69.25%)</b></td><td>382.00 <b>(+27.33%)</b></td><td>92.68 <b>(-24.32%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.50 (n/a)</td><td>394.22 (n/a)</td><td>311.20 (n/a)</td><td>300.00 (n/a)</td><td>122.46 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (+3.49%)</td><td>0.03 <b>(+29.16%)</b></td><td>0.03 (+14.07%)</td><td>0.03 <b>(+570.32%)</b></td><td>0.00 <b>(-65.36%)</b></td><td>298.30 <b>(-85.08%)</b></td><td>270.30 <b>(-57.34%)</b></td><td>269.90 (-12.34%)</td><td>217.60 (-3.37%)</td><td>32.47 <b>(-95.75%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1999.60 (n/a)</td><td>633.60 (n/a)</td><td>307.90 (n/a)</td><td>225.20 (n/a)</td><td>764.72 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (-6.66%)</td><td>0.02 (-0.04%)</td><td>0.02 (+8.67%)</td><td>0.01 <b>(-28.33%)</b></td><td>0.01 (+1.80%)</td><td>734.90 <b>(+39.53%)</b></td><td>434.00 (+5.71%)</td><td>423.70 (-7.97%)</td><td>223.40 (+7.15%)</td><td>196.88 <b>(+60.28%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.70 (n/a)</td><td>410.54 (n/a)</td><td>460.40 (n/a)</td><td>208.50 (n/a)</td><td>122.84 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (-10.26%)</td><td>0.02 <b>(-30.30%)</b></td><td>0.02 <b>(-44.38%)</b></td><td>0.02 <b>(-40.40%)</b></td><td>0.01 <b>(+211.48%)</b></td><td>456.00 <b>(+67.77%)</b></td><td>379.96 <b>(+51.55%)</b></td><td>438.80 <b>(+79.84%)</b></td><td>260.70 (+11.41%)</td><td>95.57 <b>(+495.05%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>271.80 (n/a)</td><td>250.72 (n/a)</td><td>244.00 (n/a)</td><td>234.00 (n/a)</td><td>16.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (+9.23%)</td><td>0.02 <b>(-31.77%)</b></td><td>0.01 <b>(-51.61%)</b></td><td>0.01 <b>(-40.44%)</b></td><td>0.01 <b>(+31.45%)</b></td><td>995.20 <b>(+67.91%)</b></td><td>609.72 <b>(+65.36%)</b></td><td>596.30 <b>(+106.62%)</b></td><td>228.80 (-8.44%)</td><td>273.19 <b>(+85.58%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.70 (n/a)</td><td>368.72 (n/a)</td><td>288.60 (n/a)</td><td>249.90 (n/a)</td><td>147.21 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (-17.96%)</td><td>0.02 <b>(-49.92%)</b></td><td>0.02 <b>(-55.23%)</b></td><td>0.00 <b>(-78.31%)</b></td><td>0.01 <b>(+42.37%)</b></td><td>1833.90 <b>(+361.01%)</b></td><td>749.06 <b>(+175.71%)</b></td><td>543.90 <b>(+123.37%)</b></td><td>284.50 <b>(+21.89%)</b></td><td>617.00 <b>(+773.47%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>397.80 (n/a)</td><td>271.68 (n/a)</td><td>243.50 (n/a)</td><td>233.40 (n/a)</td><td>70.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 <b>(-34.36%)</b></td><td>0.02 <b>(-32.66%)</b></td><td>0.02 <b>(-39.16%)</b></td><td>0.01 <b>(-51.48%)</b></td><td>0.01 <b>(-32.33%)</b></td><td>1249.50 <b>(+106.09%)</b></td><td>614.10 <b>(+56.45%)</b></td><td>534.90 <b>(+64.38%)</b></td><td>360.40 <b>(+52.32%)</b></td><td>365.95 <b>(+115.05%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.30 (n/a)</td><td>392.52 (n/a)</td><td>325.40 (n/a)</td><td>236.60 (n/a)</td><td>170.17 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/repeat</summary>


### test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word]

_No metrics available._


### test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>534.10 (n/a)</td><td>367.38 (n/a)</td><td>296.40 (n/a)</td><td>274.40 (n/a)</td><td>119.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>570.10 (n/a)</td><td>367.34 (n/a)</td><td>257.60 (n/a)</td><td>224.70 (n/a)</td><td>172.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.90 (n/a)</td><td>408.20 (n/a)</td><td>393.00 (n/a)</td><td>272.80 (n/a)</td><td>119.05 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (-13.00%)</td><td>0.02 <b>(-21.79%)</b></td><td>0.03 (-14.78%)</td><td>0.01 <b>(-41.61%)</b></td><td>0.01 <b>(+45.79%)</b></td><td>620.90 <b>(+71.28%)</b></td><td>387.38 <b>(+40.74%)</b></td><td>289.10 (+17.38%)</td><td>250.30 (+14.92%)</td><td>164.44 <b>(+182.64%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>362.50 (n/a)</td><td>275.24 (n/a)</td><td>246.30 (n/a)</td><td>217.80 (n/a)</td><td>58.18 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.05 (+10.70%)</td><td>0.04 (+2.14%)</td><td>0.03 <b>(-21.15%)</b></td><td>0.02 (+6.13%)</td><td>0.02 (+9.83%)</td><td>583.80 (-5.78%)</td><td>389.08 (-2.45%)</td><td>376.50 <b>(+26.81%)</b></td><td>223.90 (-9.64%)</td><td>158.18 (-10.07%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>619.60 (n/a)</td><td>398.86 (n/a)</td><td>296.90 (n/a)</td><td>247.80 (n/a)</td><td>175.90 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (-5.39%)</td><td>0.02 <b>(-21.61%)</b></td><td>0.02 <b>(-42.88%)</b></td><td>0.01 (-6.10%)</td><td>0.01 (-5.97%)</td><td>548.70 (+6.50%)</td><td>434.58 <b>(+27.87%)</b></td><td>482.80 <b>(+75.05%)</b></td><td>256.00 (+5.70%)</td><td>129.70 (+9.90%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.20 (n/a)</td><td>339.86 (n/a)</td><td>275.80 (n/a)</td><td>242.20 (n/a)</td><td>118.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (+6.17%)</td><td>0.03 (-0.62%)</td><td>0.02 (-0.95%)</td><td>0.02 (+7.14%)</td><td>0.01 (-3.70%)</td><td>513.00 (-6.66%)</td><td>396.62 (-0.42%)</td><td>445.70 (+0.95%)</td><td>250.90 (-5.78%)</td><td>115.10 (-8.93%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>549.60 (n/a)</td><td>398.28 (n/a)</td><td>441.50 (n/a)</td><td>266.30 (n/a)</td><td>126.39 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (+3.80%)</td><td>0.03 <b>(+26.49%)</b></td><td>0.03 <b>(+41.91%)</b></td><td>0.02 <b>(+290.82%)</b></td><td>0.01 <b>(-43.73%)</b></td><td>476.60 <b>(-74.41%)</b></td><td>307.70 <b>(-51.39%)</b></td><td>281.60 <b>(-29.53%)</b></td><td>232.20 (-3.65%)</td><td>97.30 <b>(-85.95%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1862.60 (n/a)</td><td>633.02 (n/a)</td><td>399.60 (n/a)</td><td>241.00 (n/a)</td><td>692.33 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.06 <b>(+26.40%)</b></td><td>0.03 (+4.42%)</td><td>0.02 (+8.77%)</td><td>0.01 <b>(-57.88%)</b></td><td>0.02 <b>(+54.68%)</b></td><td>1877.40 <b>(+137.44%)</b></td><td>688.66 <b>(+46.92%)</b></td><td>443.40 (-8.07%)</td><td>177.30 <b>(-20.88%)</b></td><td>689.65 <b>(+211.29%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>790.70 (n/a)</td><td>468.74 (n/a)</td><td>482.30 (n/a)</td><td>224.10 (n/a)</td><td>221.55 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 (+1.85%)</td><td>0.02 <b>(+32.33%)</b></td><td>0.02 (+5.66%)</td><td>0.01 <b>(+290.55%)</b></td><td>0.01 <b>(-34.19%)</b></td><td>627.80 <b>(-74.40%)</b></td><td>418.66 <b>(-61.06%)</b></td><td>458.20 (-5.37%)</td><td>244.60 (-1.81%)</td><td>154.35 <b>(-84.81%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2452.00 (n/a)</td><td>1075.02 (n/a)</td><td>484.20 (n/a)</td><td>249.10 (n/a)</td><td>1016.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (+7.40%)</td><td>0.03 (+15.59%)</td><td>0.03 <b>(+21.80%)</b></td><td>0.02 (+18.67%)</td><td>0.01 (+11.54%)</td><td>564.00 (-15.73%)</td><td>385.86 (-12.90%)</td><td>314.60 (-17.90%)</td><td>231.90 (-6.90%)</td><td>149.52 (-7.41%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>669.30 (n/a)</td><td>443.00 (n/a)</td><td>383.20 (n/a)</td><td>249.10 (n/a)</td><td>161.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 <b>(-21.20%)</b></td><td>0.02 (-12.87%)</td><td>0.02 <b>(-28.18%)</b></td><td>0.02 (+5.01%)</td><td>0.01 <b>(-36.19%)</b></td><td>544.50 (-4.77%)</td><td>387.64 (+3.32%)</td><td>420.70 <b>(+39.21%)</b></td><td>236.90 <b>(+26.89%)</b></td><td>124.41 <b>(-31.84%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.80 (n/a)</td><td>375.18 (n/a)</td><td>302.20 (n/a)</td><td>186.70 (n/a)</td><td>182.52 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.04 (-1.12%)</td><td>0.03 (+3.41%)</td><td>0.03 <b>(+28.38%)</b></td><td>0.02 (+6.69%)</td><td>0.01 (-0.67%)</td><td>573.70 (-6.27%)</td><td>388.06 (-3.02%)</td><td>307.70 <b>(-22.12%)</b></td><td>235.30 (+1.16%)</td><td>153.76 (+1.27%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>612.10 (n/a)</td><td>400.14 (n/a)</td><td>395.10 (n/a)</td><td>232.60 (n/a)</td><td>151.83 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 <b>(+50.22%)</b></td><td>0.02 <b>(+26.84%)</b></td><td>0.02 <b>(+28.35%)</b></td><td>0.01 (-0.44%)</td><td>0.01 <b>(+108.44%)</b></td><td>675.80 (+0.45%)</td><td>439.58 (-14.89%)</td><td>430.60 <b>(-22.08%)</b></td><td>246.00 <b>(-33.42%)</b></td><td>166.65 <b>(+40.35%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>672.80 (n/a)</td><td>516.46 (n/a)</td><td>552.60 (n/a)</td><td>369.50 (n/a)</td><td>118.74 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.37 (+11.13%)</td><td>0.24 (-11.93%)</td><td>0.18 <b>(-37.81%)</b></td><td>0.15 <b>(-22.81%)</b></td><td>0.11 <b>(+81.14%)</b></td><td>635.50 <b>(+29.54%)</b></td><td>472.88 <b>(+26.09%)</b></td><td>553.10 <b>(+60.83%)</b></td><td>266.90 (-10.01%)</td><td>181.52 <b>(+111.81%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>490.60 (n/a)</td><td>375.04 (n/a)</td><td>343.90 (n/a)</td><td>296.60 (n/a)</td><td>85.70 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.38 (+18.24%)</td><td>0.31 <b>(+44.30%)</b></td><td>0.32 <b>(+36.51%)</b></td><td>0.22 <b>(+132.95%)</b></td><td>0.06 <b>(-26.98%)</b></td><td>437.60 <b>(-57.07%)</b></td><td>325.82 <b>(-39.65%)</b></td><td>304.00 <b>(-26.75%)</b></td><td>256.90 (-15.44%)</td><td>72.84 <b>(-74.56%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>1019.40 (n/a)</td><td>539.84 (n/a)</td><td>415.00 (n/a)</td><td>303.80 (n/a)</td><td>286.36 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.40 (-6.58%)</td><td>0.32 (-3.84%)</td><td>0.38 (-6.35%)</td><td>0.21 (+5.27%)</td><td>0.10 (-16.72%)</td><td>473.90 (-5.01%)</td><td>331.50 (+0.66%)</td><td>255.70 (+6.76%)</td><td>244.20 (+7.06%)</td><td>112.58 (-14.76%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.41 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>498.90 (n/a)</td><td>329.34 (n/a)</td><td>239.50 (n/a)</td><td>228.10 (n/a)</td><td>132.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.36 <b>(+31.15%)</b></td><td>0.25 <b>(+24.82%)</b></td><td>0.26 <b>(+65.93%)</b></td><td>0.16 (+9.98%)</td><td>0.09 <b>(+32.41%)</b></td><td>475.10 (-9.07%)</td><td>334.68 (-17.80%)</td><td>284.90 <b>(-39.73%)</b></td><td>205.00 <b>(-23.76%)</b></td><td>125.30 (+0.93%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>522.50 (n/a)</td><td>407.14 (n/a)</td><td>472.70 (n/a)</td><td>268.90 (n/a)</td><td>124.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.29 (+10.12%)</td><td>0.22 (-6.03%)</td><td>0.23 (-5.69%)</td><td>0.14 (-14.78%)</td><td>0.07 <b>(+66.34%)</b></td><td>545.20 (+17.32%)</td><td>379.96 (+14.06%)</td><td>319.70 (+6.04%)</td><td>251.60 (-9.20%)</td><td>140.86 <b>(+80.69%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>464.70 (n/a)</td><td>333.12 (n/a)</td><td>301.50 (n/a)</td><td>277.10 (n/a)</td><td>77.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.30 (+0.89%)</td><td>0.24 (+10.31%)</td><td>0.27 (+13.84%)</td><td>0.17 <b>(+31.31%)</b></td><td>0.06 (-8.44%)</td><td>441.20 <b>(-23.85%)</b></td><td>327.50 (-12.06%)</td><td>271.90 (-12.18%)</td><td>242.20 (-0.86%)</td><td>91.43 <b>(-30.90%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>579.40 (n/a)</td><td>372.40 (n/a)</td><td>309.60 (n/a)</td><td>244.30 (n/a)</td><td>132.31 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.48 (-5.68%)</td><td>0.37 <b>(+26.77%)</b></td><td>0.38 <b>(+41.92%)</b></td><td>0.19 <b>(+182.10%)</b></td><td>0.11 <b>(-39.67%)</b></td><td>677.00 <b>(-64.55%)</b></td><td>389.46 <b>(-46.68%)</b></td><td>344.10 <b>(-29.55%)</b></td><td>273.30 (+6.01%)</td><td>163.46 <b>(-76.01%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.51 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>0.18 (n/a)</td><td>1909.80 (n/a)</td><td>730.40 (n/a)</td><td>488.40 (n/a)</td><td>257.80 (n/a)</td><td>681.34 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.50 (+12.07%)</td><td>0.35 <b>(+20.39%)</b></td><td>0.33 <b>(+28.76%)</b></td><td>0.21 <b>(+36.36%)</b></td><td>0.13 (-6.23%)</td><td>634.10 <b>(-26.66%)</b></td><td>422.70 <b>(-23.01%)</b></td><td>399.20 <b>(-22.32%)</b></td><td>263.50 (-10.77%)</td><td>160.85 <b>(-38.07%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>864.60 (n/a)</td><td>549.04 (n/a)</td><td>513.90 (n/a)</td><td>295.30 (n/a)</td><td>259.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.51 <b>(+79.32%)</b></td><td>0.30 <b>(+27.70%)</b></td><td>0.30 (+18.30%)</td><td>0.07 <b>(-59.95%)</b></td><td>0.17 <b>(+245.02%)</b></td><td>1877.10 <b>(+149.68%)</b></td><td>706.14 <b>(+20.14%)</b></td><td>435.20 (-15.48%)</td><td>257.20 <b>(-44.23%)</b></td><td>668.74 <b>(+408.72%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>751.80 (n/a)</td><td>587.76 (n/a)</td><td>514.90 (n/a)</td><td>461.20 (n/a)</td><td>131.46 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (+0.01%)</td><td>0.01 (-8.11%)</td><td>0.01 <b>(-32.64%)</b></td><td>0.01 (+5.62%)</td><td>0.00 (-17.12%)</td><td>570.70 (-5.31%)</td><td>422.28 (+4.03%)</td><td>434.10 <b>(+48.46%)</b></td><td>269.80 (+0.00%)</td><td>127.88 <b>(-23.40%)</b></td>
</tr>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (+0.96%)</td><td>0.01 (-8.75%)</td><td>0.01 (-0.90%)</td><td>0.01 (-17.74%)</td><td>0.00 <b>(+68.56%)</b></td><td>464.80 <b>(+21.55%)</b></td><td>344.24 (+15.64%)</td><td>297.70 (+0.92%)</td><td>245.80 (-0.97%)</td><td>108.20 <b>(+106.98%)</b></td>
</tr>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (+15.60%)</td><td>0.01 (-7.69%)</td><td>0.01 <b>(-21.14%)</b></td><td>0.01 <b>(+212.85%)</b></td><td>0.01 (-12.59%)</td><td>590.90 <b>(-68.03%)</b></td><td>457.84 <b>(-27.55%)</b></td><td>485.90 <b>(+26.80%)</b></td><td>204.60 (-13.49%)</td><td>157.50 <b>(-77.05%)</b></td>
</tr>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.67 (+14.41%)</td><td>0.43 (-8.31%)</td><td>0.42 (-11.68%)</td><td>0.24 <b>(-30.44%)</b></td><td>0.19 <b>(+114.42%)</b></td><td>558.40 <b>(+43.77%)</b></td><td>366.76 <b>(+25.90%)</b></td><td>313.40 (+13.22%)</td><td>196.50 (-12.59%)</td><td>168.98 <b>(+178.25%)</b></td>
</tr>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.49 (-4.91%)</td><td>0.33 <b>(-21.84%)</b></td><td>0.40 (-10.79%)</td><td>0.07 <b>(-74.56%)</b></td><td>0.17 <b>(+87.50%)</b></td><td>1939.80 <b>(+293.15%)</b></td><td>676.28 <b>(+105.03%)</b></td><td>329.80 (+12.10%)</td><td>269.00 (+5.16%)</td><td>714.69 <b>(+662.64%)</b></td>
</tr>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.55 (+4.00%)</td><td>0.38 (-4.99%)</td><td>0.33 <b>(-31.16%)</b></td><td>0.25 (+5.62%)</td><td>0.14 (-4.42%)</td><td>535.40 (-5.32%)</td><td>385.10 (+2.83%)</td><td>403.10 <b>(+45.26%)</b></td><td>242.20 (-3.85%)</td><td>130.16 (-15.20%)</td>
</tr>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.58 (+13.01%)</td><td>0.43 <b>(+25.13%)</b></td><td>0.49 <b>(+82.17%)</b></td><td>0.26 (-3.17%)</td><td>0.14 <b>(+25.37%)</b></td><td>517.60 (+3.27%)</td><td>340.12 (-17.95%)</td><td>266.90 <b>(-45.10%)</b></td><td>229.50 (-11.53%)</td><td>124.54 (+11.48%)</td>
</tr>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.87 <b>(+61.80%)</b></td><td>0.49 (+10.59%)</td><td>0.47 (-4.82%)</td><td>0.25 (+14.17%)</td><td>0.24 <b>(+81.60%)</b></td><td>534.90 (-12.41%)</td><td>320.34 (-3.58%)</td><td>279.50 (+5.04%)</td><td>151.60 <b>(-38.17%)</b></td><td>148.14 (-5.35%)</td>
</tr>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.02 (-11.07%)</td><td>0.01 (-7.06%)</td><td>0.01 (+0.79%)</td><td>0.00 <b>(-29.56%)</b></td><td>0.01 (-3.71%)</td><td>1048.30 <b>(+41.95%)</b></td><td>467.44 (+16.94%)</td><td>292.60 (-0.78%)</td><td>238.40 (+12.45%)</td><td>344.11 <b>(+51.54%)</b></td>
</tr>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.03 <b>(+32.14%)</b></td><td>0.01 (+1.36%)</td><td>0.01 (-1.69%)</td><td>0.01 (+5.02%)</td><td>0.01 <b>(+30.14%)</b></td><td>645.70 (-4.78%)</td><td>395.52 (+3.64%)</td><td>296.00 (+1.72%)</td><td>159.80 <b>(-24.34%)</b></td><td>208.52 (+2.69%)</td>
</tr>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.00 <b>(-66.67%)</b></td><td>0.00 <b>(-28.57%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-100.00%)</b></td><td>21427.35 (+0.47%)</td><td>19885.82 (+13.22%)</td><td>20769.78 (-0.84%)</td><td>16821.89 <b>(+134.07%)</b></td><td>1902.35 <b>(-68.65%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21328.00 (n/a)</td><td>17564.65 (n/a)</td><td>20945.13 (n/a)</td><td>7186.63 (n/a)</td><td>6067.43 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.00 <b>(-50.00%)</b></td><td>0.00 <b>(-30.56%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-80.16%)</b></td><td>18890.03 (+2.78%)</td><td>16792.67 <b>(+29.14%)</b></td><td>16640.05 (+8.30%)</td><td>14342.14 <b>(+111.26%)</b></td><td>1743.73 <b>(-66.85%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18378.71 (n/a)</td><td>13003.58 (n/a)</td><td>15364.46 (n/a)</td><td>6788.75 (n/a)</td><td>5259.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>0.11 <b>(-28.14%)</b></td><td>0.09 (-10.98%)</td><td>0.09 (+5.36%)</td><td>0.07 (+6.55%)</td><td>0.02 <b>(-57.93%)</b></td><td>29274.86 (-6.16%)</td><td>23727.88 (+4.31%)</td><td>23726.25 (-5.04%)</td><td>18714.51 <b>(+39.19%)</b></td><td>4088.38 <b>(-44.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>31196.28 (n/a)</td><td>22747.45 (n/a)</td><td>24986.08 (n/a)</td><td>13445.52 (n/a)</td><td>7382.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>1.53 (-4.09%)</td><td>1.24 <b>(+32.15%)</b></td><td>1.47 <b>(+83.10%)</b></td><td>0.74 (+16.17%)</td><td>0.36 (-5.15%)</td><td>706.90 (-13.92%)</td><td>459.98 <b>(-25.32%)</b></td><td>355.70 <b>(-45.39%)</b></td><td>343.20 (+4.28%)</td><td>160.11 (-11.41%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>1.59 (n/a)</td><td>0.94 (n/a)</td><td>0.80 (n/a)</td><td>0.64 (n/a)</td><td>0.38 (n/a)</td><td>821.20 (n/a)</td><td>615.92 (n/a)</td><td>651.30 (n/a)</td><td>329.10 (n/a)</td><td>180.74 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>1.69 <b>(-30.85%)</b></td><td>0.95 <b>(-32.13%)</b></td><td>1.13 <b>(-41.19%)</b></td><td>0.32 (+6.96%)</td><td>0.61 <b>(-40.69%)</b></td><td>3313.00 (-6.51%)</td><td>1774.42 (+3.66%)</td><td>927.60 <b>(+70.01%)</b></td><td>621.80 <b>(+44.60%)</b></td><td>1359.02 (-18.47%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>2.44 (n/a)</td><td>1.40 (n/a)</td><td>1.92 (n/a)</td><td>0.30 (n/a)</td><td>1.03 (n/a)</td><td>3543.60 (n/a)</td><td>1711.78 (n/a)</td><td>545.60 (n/a)</td><td>430.00 (n/a)</td><td>1666.86 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:11:11</td><td>1.25 <b>(-38.24%)</b></td><td>0.92 <b>(-22.59%)</b></td><td>1.07 (+7.06%)</td><td>0.15 <b>(-82.61%)</b></td><td>0.44 (-8.27%)</td><td>3423.30 <b>(+475.15%)</b></td><td>1064.42 <b>(+120.34%)</b></td><td>491.20 (-6.60%)</td><td>418.10 <b>(+61.93%)</b></td><td>1319.07 <b>(+911.29%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:32:13</td><td>2.03 (n/a)</td><td>1.19 (n/a)</td><td>1.00 (n/a)</td><td>0.88 (n/a)</td><td>0.48 (n/a)</td><td>595.20 (n/a)</td><td>483.08 (n/a)</td><td>525.90 (n/a)</td><td>258.20 (n/a)</td><td>130.43 (n/a)</td>
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
