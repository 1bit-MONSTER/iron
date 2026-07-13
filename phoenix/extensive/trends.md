# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (-4.40%)</td><td>0.02 (+14.48%)</td><td>0.01 <b>(+20.46%)</b></td><td>0.01 <b>(+24.72%)</b></td><td>0.01 <b>(-24.57%)</b></td><td>492.00 (-19.83%)</td><td>409.14 (-18.38%)</td><td>450.50 (-16.99%)</td><td>241.90 (+4.58%)</td><td>99.32 <b>(-37.05%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.70 (n/a)</td><td>501.30 (n/a)</td><td>542.70 (n/a)</td><td>231.30 (n/a)</td><td>157.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (-9.85%)</td><td>0.02 (-17.36%)</td><td>0.01 <b>(-26.50%)</b></td><td>0.01 (-12.84%)</td><td>0.00 (+7.81%)</td><td>561.80 (+14.75%)</td><td>419.12 <b>(+22.92%)</b></td><td>422.70 <b>(+36.05%)</b></td><td>308.90 (+10.92%)</td><td>111.38 <b>(+28.49%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.60 (n/a)</td><td>340.98 (n/a)</td><td>310.70 (n/a)</td><td>278.50 (n/a)</td><td>86.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 <b>(-22.73%)</b></td><td>0.02 (-3.83%)</td><td>0.02 (-3.33%)</td><td>0.01 (+13.86%)</td><td>0.00 <b>(-43.79%)</b></td><td>490.80 (-12.18%)</td><td>338.42 (-5.74%)</td><td>306.00 (+3.45%)</td><td>248.20 <b>(+29.41%)</b></td><td>96.89 <b>(-38.33%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.90 (n/a)</td><td>359.04 (n/a)</td><td>295.80 (n/a)</td><td>191.80 (n/a)</td><td>157.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (-17.13%)</td><td>0.02 <b>(+27.69%)</b></td><td>0.02 <b>(+64.61%)</b></td><td>0.01 <b>(+24.90%)</b></td><td>0.01 <b>(-35.29%)</b></td><td>474.10 (-19.93%)</td><td>321.84 <b>(-28.00%)</b></td><td>295.20 <b>(-39.25%)</b></td><td>235.40 <b>(+20.72%)</b></td><td>99.82 <b>(-33.24%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.10 (n/a)</td><td>446.98 (n/a)</td><td>485.90 (n/a)</td><td>195.00 (n/a)</td><td>149.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 <b>(+26.19%)</b></td><td>0.02 <b>(+42.83%)</b></td><td>0.01 <b>(+46.99%)</b></td><td>0.01 <b>(+225.11%)</b></td><td>0.01 (-11.07%)</td><td>667.70 <b>(-69.24%)</b></td><td>447.48 <b>(-49.02%)</b></td><td>434.20 <b>(-31.96%)</b></td><td>254.60 <b>(-20.76%)</b></td><td>146.74 <b>(-80.32%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2170.70 (n/a)</td><td>877.74 (n/a)</td><td>638.20 (n/a)</td><td>321.30 (n/a)</td><td>745.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (-6.14%)</td><td>0.02 (+7.37%)</td><td>0.01 (+6.24%)</td><td>0.01 <b>(+138.34%)</b></td><td>0.01 <b>(-24.24%)</b></td><td>767.30 <b>(-58.04%)</b></td><td>457.42 <b>(-33.62%)</b></td><td>480.80 (-5.87%)</td><td>243.00 (+6.53%)</td><td>205.48 <b>(-68.55%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1828.80 (n/a)</td><td>689.10 (n/a)</td><td>510.80 (n/a)</td><td>228.10 (n/a)</td><td>653.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (-12.20%)</td><td>0.04 (-5.97%)</td><td>0.05 (+6.84%)</td><td>0.02 (+9.64%)</td><td>0.01 (-14.59%)</td><td>537.90 (-8.80%)</td><td>338.78 (+2.94%)</td><td>271.50 (-6.41%)</td><td>247.70 (+13.89%)</td><td>122.82 (-17.86%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>589.80 (n/a)</td><td>329.10 (n/a)</td><td>290.10 (n/a)</td><td>217.50 (n/a)</td><td>149.52 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (-13.27%)</td><td>0.04 (-3.40%)</td><td>0.05 <b>(+23.42%)</b></td><td>0.02 (-13.58%)</td><td>0.02 (+3.15%)</td><td>618.40 (+15.70%)</td><td>348.36 (+8.11%)</td><td>243.90 (-19.00%)</td><td>220.00 (+15.30%)</td><td>172.34 <b>(+31.10%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>534.50 (n/a)</td><td>322.22 (n/a)</td><td>301.10 (n/a)</td><td>190.80 (n/a)</td><td>131.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 <b>(-30.22%)</b></td><td>0.03 (-8.00%)</td><td>0.04 <b>(+30.04%)</b></td><td>0.01 <b>(-67.67%)</b></td><td>0.02 (-4.12%)</td><td>1958.00 <b>(+209.37%)</b></td><td>674.90 <b>(+58.58%)</b></td><td>281.80 <b>(-23.09%)</b></td><td>268.50 <b>(+43.35%)</b></td><td>730.62 <b>(+283.52%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>632.90 (n/a)</td><td>425.58 (n/a)</td><td>366.40 (n/a)</td><td>187.30 (n/a)</td><td>190.50 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 <b>(+46.15%)</b></td><td>0.04 (+18.57%)</td><td>0.04 <b>(+43.26%)</b></td><td>0.02 (-15.73%)</td><td>0.02 <b>(+96.77%)</b></td><td>558.70 (+18.67%)</td><td>350.70 (-6.57%)</td><td>284.20 <b>(-30.19%)</b></td><td>181.10 <b>(-31.56%)</b></td><td>151.80 <b>(+65.32%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>470.80 (n/a)</td><td>375.36 (n/a)</td><td>407.10 (n/a)</td><td>264.60 (n/a)</td><td>91.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (-4.12%)</td><td>0.04 (+16.54%)</td><td>0.04 (+13.36%)</td><td>0.02 <b>(+188.95%)</b></td><td>0.02 (-7.84%)</td><td>680.60 <b>(-65.39%)</b></td><td>423.04 <b>(-38.41%)</b></td><td>325.50 (-11.76%)</td><td>231.70 (+4.32%)</td><td>216.34 <b>(-70.08%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1966.60 (n/a)</td><td>686.88 (n/a)</td><td>368.90 (n/a)</td><td>222.10 (n/a)</td><td>723.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (+16.33%)</td><td>0.03 <b>(+20.11%)</b></td><td>0.04 <b>(+39.15%)</b></td><td>0.03 <b>(+23.08%)</b></td><td>0.01 (-7.74%)</td><td>444.00 (-18.74%)</td><td>371.16 (-18.09%)</td><td>349.20 <b>(-28.13%)</b></td><td>291.30 (-14.05%)</td><td>67.80 <b>(-32.91%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.40 (n/a)</td><td>453.14 (n/a)</td><td>485.90 (n/a)</td><td>338.90 (n/a)</td><td>101.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.11 (+1.99%)</td><td>0.08 (+4.80%)</td><td>0.08 (+1.50%)</td><td>0.04 (+6.35%)</td><td>0.02 (-6.23%)</td><td>561.90 (-5.97%)</td><td>350.98 (-6.31%)</td><td>313.70 (-1.48%)</td><td>225.40 (-1.96%)</td><td>126.94 (-11.84%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>597.60 (n/a)</td><td>374.62 (n/a)</td><td>318.40 (n/a)</td><td>229.90 (n/a)</td><td>144.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (+18.42%)</td><td>0.08 (+7.23%)</td><td>0.07 (-6.97%)</td><td>0.04 (+3.72%)</td><td>0.03 <b>(+33.75%)</b></td><td>567.90 (-3.58%)</td><td>382.04 (-1.98%)</td><td>339.20 (+7.48%)</td><td>208.30 (-15.53%)</td><td>168.21 (+11.60%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>589.00 (n/a)</td><td>389.74 (n/a)</td><td>315.60 (n/a)</td><td>246.60 (n/a)</td><td>150.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 <b>(-23.17%)</b></td><td>0.07 (-12.65%)</td><td>0.06 <b>(-24.00%)</b></td><td>0.05 (-3.08%)</td><td>0.02 <b>(-32.76%)</b></td><td>541.20 (+3.18%)</td><td>387.36 (+8.74%)</td><td>392.40 <b>(+31.59%)</b></td><td>247.60 <b>(+30.11%)</b></td><td>119.05 (-13.78%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>524.50 (n/a)</td><td>356.24 (n/a)</td><td>298.20 (n/a)</td><td>190.30 (n/a)</td><td>138.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (-15.77%)</td><td>0.07 (+11.33%)</td><td>0.07 <b>(+29.81%)</b></td><td>0.05 (+15.61%)</td><td>0.02 <b>(-39.08%)</b></td><td>465.10 (-13.50%)</td><td>348.06 (-15.94%)</td><td>350.50 <b>(-22.97%)</b></td><td>243.10 (+18.76%)</td><td>84.32 <b>(-33.05%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>537.70 (n/a)</td><td>414.04 (n/a)</td><td>455.00 (n/a)</td><td>204.70 (n/a)</td><td>125.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (-0.46%)</td><td>0.07 (+7.85%)</td><td>0.07 (+9.31%)</td><td>0.04 (+1.49%)</td><td>0.02 (+5.64%)</td><td>561.00 (-1.48%)</td><td>397.20 (-6.80%)</td><td>370.10 (-8.50%)</td><td>298.00 (+0.47%)</td><td>106.47 (+4.46%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>569.40 (n/a)</td><td>426.18 (n/a)</td><td>404.50 (n/a)</td><td>296.60 (n/a)</td><td>101.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (-12.13%)</td><td>0.08 (+2.55%)</td><td>0.09 <b>(+43.71%)</b></td><td>0.05 (+2.38%)</td><td>0.03 (-11.90%)</td><td>515.70 (-2.33%)</td><td>356.36 (-3.69%)</td><td>262.50 <b>(-30.41%)</b></td><td>254.90 (+13.79%)</td><td>133.20 (-0.88%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>528.00 (n/a)</td><td>370.00 (n/a)</td><td>377.20 (n/a)</td><td>224.00 (n/a)</td><td>134.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.17 (-14.37%)</td><td>0.15 (-0.65%)</td><td>0.16 (-12.01%)</td><td>0.10 <b>(+280.29%)</b></td><td>0.03 <b>(-59.36%)</b></td><td>506.90 <b>(-73.70%)</b></td><td>345.78 <b>(-43.14%)</b></td><td>306.70 (+13.63%)</td><td>285.10 (+16.80%)</td><td>91.32 <b>(-87.64%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1927.70 (n/a)</td><td>608.14 (n/a)</td><td>269.90 (n/a)</td><td>244.10 (n/a)</td><td>738.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.17 <b>(-28.54%)</b></td><td>0.14 (-13.04%)</td><td>0.16 (+1.39%)</td><td>0.09 (-13.45%)</td><td>0.03 <b>(-43.20%)</b></td><td>536.60 (+15.52%)</td><td>364.24 (+9.60%)</td><td>304.70 (-1.36%)</td><td>293.90 <b>(+39.95%)</b></td><td>102.92 (-11.14%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>464.50 (n/a)</td><td>332.34 (n/a)</td><td>308.90 (n/a)</td><td>210.00 (n/a)</td><td>115.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.21 <b>(+21.96%)</b></td><td>0.17 <b>(+29.21%)</b></td><td>0.17 (+19.43%)</td><td>0.12 <b>(+74.34%)</b></td><td>0.03 (-16.25%)</td><td>423.10 <b>(-42.64%)</b></td><td>308.00 <b>(-27.87%)</b></td><td>296.90 (-16.25%)</td><td>238.30 (-18.03%)</td><td>69.83 <b>(-61.31%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>737.60 (n/a)</td><td>426.98 (n/a)</td><td>354.50 (n/a)</td><td>290.70 (n/a)</td><td>180.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.19 <b>(-21.57%)</b></td><td>0.14 (-8.93%)</td><td>0.16 (-3.52%)</td><td>0.09 (+6.55%)</td><td>0.05 <b>(-24.22%)</b></td><td>558.40 (-6.15%)</td><td>388.52 (+5.50%)</td><td>316.40 (+3.67%)</td><td>263.50 <b>(+27.54%)</b></td><td>144.01 (-9.73%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>595.00 (n/a)</td><td>368.28 (n/a)</td><td>305.20 (n/a)</td><td>206.60 (n/a)</td><td>159.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.20 <b>(+121.71%)</b></td><td>0.15 <b>(+113.59%)</b></td><td>0.16 <b>(+93.06%)</b></td><td>0.09 <b>(+355.10%)</b></td><td>0.04 <b>(+46.43%)</b></td><td>533.60 <b>(-78.03%)</b></td><td>347.16 <b>(-63.60%)</b></td><td>301.30 <b>(-48.20%)</b></td><td>246.60 <b>(-54.89%)</b></td><td>115.48 <b>(-86.00%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>2428.40 (n/a)</td><td>953.68 (n/a)</td><td>581.70 (n/a)</td><td>546.70 (n/a)</td><td>824.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.17 (-11.44%)</td><td>0.12 (-3.01%)</td><td>0.11 (+7.84%)</td><td>0.09 (+7.34%)</td><td>0.03 <b>(-27.27%)</b></td><td>559.20 (-6.85%)</td><td>449.02 (-1.29%)</td><td>431.60 (-7.26%)</td><td>287.10 (+12.94%)</td><td>107.99 <b>(-25.24%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>600.30 (n/a)</td><td>454.90 (n/a)</td><td>465.40 (n/a)</td><td>254.20 (n/a)</td><td>144.45 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (-3.88%)</td><td>0.01 (-9.78%)</td><td>0.01 <b>(+30.80%)</b></td><td>0.00 <b>(-71.33%)</b></td><td>0.00 <b>(+50.05%)</b></td><td>1895.70 <b>(+248.79%)</b></td><td>738.84 <b>(+93.14%)</b></td><td>270.90 <b>(-23.54%)</b></td><td>237.00 (+4.04%)</td><td>733.23 <b>(+376.01%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>543.50 (n/a)</td><td>382.54 (n/a)</td><td>354.30 (n/a)</td><td>227.80 (n/a)</td><td>154.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (+3.16%)</td><td>0.01 <b>(+48.84%)</b></td><td>0.01 <b>(+113.62%)</b></td><td>0.01 <b>(+20.39%)</b></td><td>0.00 (-4.40%)</td><td>479.90 (-16.94%)</td><td>306.62 <b>(-34.40%)</b></td><td>244.10 <b>(-53.19%)</b></td><td>230.50 (-3.07%)</td><td>107.03 <b>(-20.18%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>577.80 (n/a)</td><td>467.42 (n/a)</td><td>521.50 (n/a)</td><td>237.80 (n/a)</td><td>134.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (-5.68%)</td><td>0.01 (+14.42%)</td><td>0.01 <b>(+36.51%)</b></td><td>0.00 (+9.39%)</td><td>0.00 <b>(-24.35%)</b></td><td>553.50 (-8.57%)</td><td>394.94 (-17.13%)</td><td>388.20 <b>(-26.74%)</b></td><td>250.30 (+6.01%)</td><td>111.80 <b>(-26.90%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>605.40 (n/a)</td><td>476.56 (n/a)</td><td>529.90 (n/a)</td><td>236.10 (n/a)</td><td>152.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (-15.27%)</td><td>0.01 (+5.23%)</td><td>0.01 (+6.00%)</td><td>0.00 <b>(+296.76%)</b></td><td>0.00 <b>(-40.67%)</b></td><td>594.50 <b>(-74.80%)</b></td><td>483.80 <b>(-41.58%)</b></td><td>501.90 (-5.66%)</td><td>265.00 (+17.99%)</td><td>129.46 <b>(-85.05%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2358.70 (n/a)</td><td>828.14 (n/a)</td><td>532.00 (n/a)</td><td>224.60 (n/a)</td><td>865.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (-13.28%)</td><td>0.01 <b>(-25.99%)</b></td><td>0.01 <b>(-31.17%)</b></td><td>0.00 <b>(-67.16%)</b></td><td>0.00 <b>(+31.93%)</b></td><td>1348.50 <b>(+204.47%)</b></td><td>581.48 <b>(+71.49%)</b></td><td>444.80 <b>(+45.31%)</b></td><td>275.80 (+15.30%)</td><td>437.24 <b>(+384.09%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>442.90 (n/a)</td><td>339.08 (n/a)</td><td>306.10 (n/a)</td><td>239.20 (n/a)</td><td>90.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (+11.88%)</td><td>0.01 <b>(+24.30%)</b></td><td>0.01 <b>(+49.22%)</b></td><td>0.00 (-7.67%)</td><td>0.00 <b>(+37.32%)</b></td><td>604.10 (+8.30%)</td><td>417.40 (-17.68%)</td><td>365.40 <b>(-32.98%)</b></td><td>322.90 (-10.63%)</td><td>113.81 <b>(+37.25%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>557.80 (n/a)</td><td>507.04 (n/a)</td><td>545.20 (n/a)</td><td>361.30 (n/a)</td><td>82.92 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (-5.31%)</td><td>0.02 (+2.51%)</td><td>0.02 (+13.00%)</td><td>0.01 (+13.90%)</td><td>0.00 <b>(-27.22%)</b></td><td>526.60 (-12.20%)</td><td>359.64 (-7.42%)</td><td>320.10 (-11.50%)</td><td>254.40 (+5.60%)</td><td>103.40 <b>(-29.59%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.80 (n/a)</td><td>388.48 (n/a)</td><td>361.70 (n/a)</td><td>240.90 (n/a)</td><td>146.86 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (+13.52%)</td><td>0.01 <b>(-30.93%)</b></td><td>0.01 <b>(-43.03%)</b></td><td>0.01 <b>(-56.81%)</b></td><td>0.01 <b>(+95.43%)</b></td><td>1021.60 <b>(+131.55%)</b></td><td>583.18 <b>(+75.11%)</b></td><td>564.70 <b>(+75.54%)</b></td><td>231.20 (-11.89%)</td><td>285.96 <b>(+285.15%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>441.20 (n/a)</td><td>333.04 (n/a)</td><td>321.70 (n/a)</td><td>262.40 (n/a)</td><td>74.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (+1.31%)</td><td>0.01 (+16.83%)</td><td>0.01 (+11.81%)</td><td>0.00 <b>(-42.92%)</b></td><td>0.01 (+15.15%)</td><td>1947.00 <b>(+75.18%)</b></td><td>711.70 (+12.14%)</td><td>542.90 (-10.56%)</td><td>229.70 (-1.29%)</td><td>706.38 <b>(+114.28%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1111.40 (n/a)</td><td>634.68 (n/a)</td><td>607.00 (n/a)</td><td>232.70 (n/a)</td><td>329.65 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (-18.14%)</td><td>0.02 (+9.99%)</td><td>0.02 <b>(+56.70%)</b></td><td>0.01 (+5.31%)</td><td>0.00 <b>(-32.07%)</b></td><td>519.50 (-5.04%)</td><td>351.82 (-14.32%)</td><td>302.80 <b>(-36.17%)</b></td><td>234.80 <b>(+22.16%)</b></td><td>117.66 (-17.41%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.10 (n/a)</td><td>410.60 (n/a)</td><td>474.40 (n/a)</td><td>192.20 (n/a)</td><td>142.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (-13.82%)</td><td>0.01 <b>(-43.99%)</b></td><td>0.01 <b>(-38.49%)</b></td><td>0.00 <b>(-73.21%)</b></td><td>0.01 (+2.57%)</td><td>2412.00 <b>(+273.32%)</b></td><td>994.56 <b>(+150.81%)</b></td><td>661.20 <b>(+62.58%)</b></td><td>275.60 (+16.04%)</td><td>831.59 <b>(+394.27%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.10 (n/a)</td><td>396.54 (n/a)</td><td>406.70 (n/a)</td><td>237.50 (n/a)</td><td>168.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 <b>(+82.63%)</b></td><td>0.01 <b>(+28.80%)</b></td><td>0.01 <b>(+23.11%)</b></td><td>0.01 (-2.85%)</td><td>0.01 <b>(+291.29%)</b></td><td>641.60 (+2.94%)</td><td>471.40 (-14.10%)</td><td>445.10 (-18.76%)</td><td>246.20 <b>(-45.24%)</b></td><td>159.37 <b>(+117.80%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>623.30 (n/a)</td><td>548.76 (n/a)</td><td>547.90 (n/a)</td><td>449.60 (n/a)</td><td>73.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (-11.40%)</td><td>0.03 (+4.62%)</td><td>0.03 <b>(+24.40%)</b></td><td>0.02 <b>(+24.34%)</b></td><td>0.01 <b>(-35.00%)</b></td><td>420.30 (-19.58%)</td><td>346.58 (-8.28%)</td><td>319.30 (-19.61%)</td><td>271.40 (+12.85%)</td><td>68.02 <b>(-37.36%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.60 (n/a)</td><td>377.86 (n/a)</td><td>397.20 (n/a)</td><td>240.50 (n/a)</td><td>108.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (+17.20%)</td><td>0.03 (-8.84%)</td><td>0.03 <b>(-31.77%)</b></td><td>0.01 <b>(-72.35%)</b></td><td>0.02 <b>(+58.97%)</b></td><td>1999.90 <b>(+261.65%)</b></td><td>664.74 <b>(+88.22%)</b></td><td>403.50 <b>(+46.57%)</b></td><td>185.00 (-14.67%)</td><td>758.24 <b>(+398.62%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>553.00 (n/a)</td><td>353.18 (n/a)</td><td>275.30 (n/a)</td><td>216.80 (n/a)</td><td>152.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 <b>(+39.21%)</b></td><td>0.03 (-1.04%)</td><td>0.04 (-18.67%)</td><td>0.02 (+3.82%)</td><td>0.02 <b>(+35.48%)</b></td><td>587.00 (-3.69%)</td><td>380.22 (+6.60%)</td><td>295.40 <b>(+22.93%)</b></td><td>167.30 <b>(-28.14%)</b></td><td>183.65 (+7.10%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>609.50 (n/a)</td><td>356.68 (n/a)</td><td>240.30 (n/a)</td><td>232.80 (n/a)</td><td>171.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (+9.34%)</td><td>0.03 (+17.27%)</td><td>0.03 <b>(+40.24%)</b></td><td>0.02 <b>(+21.44%)</b></td><td>0.01 <b>(-20.24%)</b></td><td>465.20 (-17.66%)</td><td>351.54 (-19.50%)</td><td>356.90 <b>(-28.69%)</b></td><td>235.50 (-8.54%)</td><td>82.80 <b>(-43.03%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>565.00 (n/a)</td><td>436.70 (n/a)</td><td>500.50 (n/a)</td><td>257.50 (n/a)</td><td>145.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 <b>(+21.14%)</b></td><td>0.02 (-5.64%)</td><td>0.02 (-16.57%)</td><td>0.01 <b>(-44.02%)</b></td><td>0.01 <b>(+77.39%)</b></td><td>1016.00 <b>(+78.62%)</b></td><td>594.76 <b>(+24.49%)</b></td><td>598.50 (+19.87%)</td><td>241.40 (-17.47%)</td><td>282.89 <b>(+157.42%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>568.80 (n/a)</td><td>477.76 (n/a)</td><td>499.30 (n/a)</td><td>292.50 (n/a)</td><td>109.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 <b>(+21.97%)</b></td><td>0.03 (-0.01%)</td><td>0.02 (-7.22%)</td><td>0.02 (-2.81%)</td><td>0.01 <b>(+62.11%)</b></td><td>533.40 (+2.89%)</td><td>438.86 (+5.67%)</td><td>479.20 (+7.78%)</td><td>222.70 (-18.00%)</td><td>123.84 <b>(+35.08%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.40 (n/a)</td><td>415.30 (n/a)</td><td>444.60 (n/a)</td><td>271.60 (n/a)</td><td>91.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 <b>(+25.02%)</b></td><td>0.06 (-11.36%)</td><td>0.05 <b>(-33.32%)</b></td><td>0.04 (-6.56%)</td><td>0.03 <b>(+72.14%)</b></td><td>548.80 (+7.02%)</td><td>408.50 <b>(+22.12%)</b></td><td>448.10 <b>(+49.97%)</b></td><td>208.20 <b>(-20.02%)</b></td><td>149.17 <b>(+45.60%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>512.80 (n/a)</td><td>334.52 (n/a)</td><td>298.80 (n/a)</td><td>260.30 (n/a)</td><td>102.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (-8.62%)</td><td>0.06 (+0.83%)</td><td>0.07 (+1.29%)</td><td>0.04 (-0.61%)</td><td>0.02 (-18.90%)</td><td>524.90 (+0.61%)</td><td>345.00 (-2.69%)</td><td>297.70 (-1.26%)</td><td>267.20 (+9.42%)</td><td>104.33 (-8.68%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>521.70 (n/a)</td><td>354.52 (n/a)</td><td>301.50 (n/a)</td><td>244.20 (n/a)</td><td>114.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (-3.92%)</td><td>0.06 (-9.60%)</td><td>0.04 <b>(-47.53%)</b></td><td>0.04 <b>(+250.54%)</b></td><td>0.02 <b>(-34.47%)</b></td><td>554.70 <b>(-71.47%)</b></td><td>426.56 <b>(-33.05%)</b></td><td>501.30 <b>(+90.54%)</b></td><td>247.90 (+4.07%)</td><td>145.51 <b>(-80.28%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1944.30 (n/a)</td><td>637.16 (n/a)</td><td>263.10 (n/a)</td><td>238.20 (n/a)</td><td>737.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (+13.75%)</td><td>0.07 (+12.07%)</td><td>0.07 (-11.82%)</td><td>0.04 (+3.86%)</td><td>0.02 (-5.76%)</td><td>553.40 (-3.72%)</td><td>328.16 (-14.08%)</td><td>309.90 (+13.43%)</td><td>212.30 (-12.09%)</td><td>133.17 <b>(-20.31%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>574.80 (n/a)</td><td>381.92 (n/a)</td><td>273.20 (n/a)</td><td>241.50 (n/a)</td><td>167.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (+11.28%)</td><td>0.08 <b>(+70.99%)</b></td><td>0.08 <b>(+104.68%)</b></td><td>0.05 <b>(+372.78%)</b></td><td>0.02 <b>(-55.27%)</b></td><td>409.40 <b>(-78.85%)</b></td><td>283.92 <b>(-71.12%)</b></td><td>264.20 <b>(-51.15%)</b></td><td>225.80 (-10.15%)</td><td>73.32 <b>(-91.62%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1935.40 (n/a)</td><td>983.04 (n/a)</td><td>540.80 (n/a)</td><td>251.30 (n/a)</td><td>875.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 <b>(+74.80%)</b></td><td>0.06 (+19.28%)</td><td>0.05 (+3.98%)</td><td>0.04 (+7.64%)</td><td>0.03 <b>(+112.46%)</b></td><td>554.00 (-7.09%)</td><td>412.26 (-8.41%)</td><td>433.90 (-3.83%)</td><td>171.90 <b>(-42.80%)</b></td><td>145.70 (+3.57%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>596.30 (n/a)</td><td>450.10 (n/a)</td><td>451.20 (n/a)</td><td>300.50 (n/a)</td><td>140.68 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


### test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>301.70 (n/a)</td><td>252.10 (n/a)</td><td>242.00 (n/a)</td><td>214.00 (n/a)</td><td>34.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>446.90 (n/a)</td><td>332.16 (n/a)</td><td>272.40 (n/a)</td><td>252.70 (n/a)</td><td>95.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>795.70 (n/a)</td><td>487.30 (n/a)</td><td>464.10 (n/a)</td><td>243.50 (n/a)</td><td>198.86 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.80 (n/a)</td><td>399.58 (n/a)</td><td>458.50 (n/a)</td><td>237.50 (n/a)</td><td>118.24 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.50 (n/a)</td><td>411.42 (n/a)</td><td>439.00 (n/a)</td><td>293.50 (n/a)</td><td>107.34 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>633.00 (n/a)</td><td>406.28 (n/a)</td><td>330.10 (n/a)</td><td>264.90 (n/a)</td><td>168.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>545.60 (n/a)</td><td>426.70 (n/a)</td><td>448.70 (n/a)</td><td>234.40 (n/a)</td><td>115.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>567.50 (n/a)</td><td>400.70 (n/a)</td><td>366.00 (n/a)</td><td>259.20 (n/a)</td><td>145.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>522.30 (n/a)</td><td>378.72 (n/a)</td><td>355.00 (n/a)</td><td>259.80 (n/a)</td><td>108.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.25 <b>(+35.05%)</b></td><td>0.12 (-12.06%)</td><td>0.10 <b>(-33.67%)</b></td><td>0.05 <b>(-36.04%)</b></td><td>0.07 <b>(+57.88%)</b></td><td>896.50 <b>(+56.35%)</b></td><td>504.80 <b>(+30.22%)</b></td><td>473.30 <b>(+50.78%)</b></td><td>196.60 <b>(-25.95%)</b></td><td>256.28 <b>(+76.13%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>573.40 (n/a)</td><td>387.64 (n/a)</td><td>313.90 (n/a)</td><td>265.50 (n/a)</td><td>145.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>505.30 (n/a)</td><td>342.52 (n/a)</td><td>279.60 (n/a)</td><td>236.80 (n/a)</td><td>121.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>498.80 (n/a)</td><td>362.20 (n/a)</td><td>421.00 (n/a)</td><td>206.80 (n/a)</td><td>126.56 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


### test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>473.80 (n/a)</td><td>295.86 (n/a)</td><td>268.70 (n/a)</td><td>229.10 (n/a)</td><td>101.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1927.40 (n/a)</td><td>696.22 (n/a)</td><td>514.00 (n/a)</td><td>237.50 (n/a)</td><td>702.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>524.70 (n/a)</td><td>353.80 (n/a)</td><td>280.10 (n/a)</td><td>244.90 (n/a)</td><td>123.80 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>459.50 (n/a)</td><td>320.28 (n/a)</td><td>283.80 (n/a)</td><td>201.00 (n/a)</td><td>127.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>326.10 (n/a)</td><td>256.00 (n/a)</td><td>246.80 (n/a)</td><td>202.10 (n/a)</td><td>46.17 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>577.50 (n/a)</td><td>382.46 (n/a)</td><td>354.10 (n/a)</td><td>222.30 (n/a)</td><td>137.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>544.90 (n/a)</td><td>318.52 (n/a)</td><td>264.10 (n/a)</td><td>252.70 (n/a)</td><td>126.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>563.30 (n/a)</td><td>427.88 (n/a)</td><td>462.10 (n/a)</td><td>211.80 (n/a)</td><td>132.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>517.90 (n/a)</td><td>403.64 (n/a)</td><td>385.50 (n/a)</td><td>299.40 (n/a)</td><td>97.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>1079.60 (n/a)</td><td>534.08 (n/a)</td><td>439.70 (n/a)</td><td>265.80 (n/a)</td><td>314.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1897.70 (n/a)</td><td>618.94 (n/a)</td><td>355.20 (n/a)</td><td>234.60 (n/a)</td><td>717.48 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gelu</summary>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.40 (n/a)</td><td>448.02 (n/a)</td><td>446.70 (n/a)</td><td>272.80 (n/a)</td><td>119.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1406.30 (n/a)</td><td>647.58 (n/a)</td><td>507.40 (n/a)</td><td>282.90 (n/a)</td><td>440.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.00 (n/a)</td><td>474.52 (n/a)</td><td>530.50 (n/a)</td><td>329.00 (n/a)</td><td>99.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>623.90 (n/a)</td><td>513.10 (n/a)</td><td>551.30 (n/a)</td><td>291.20 (n/a)</td><td>128.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>668.50 (n/a)</td><td>456.32 (n/a)</td><td>495.90 (n/a)</td><td>286.70 (n/a)</td><td>162.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1913.10 (n/a)</td><td>1075.48 (n/a)</td><td>585.20 (n/a)</td><td>415.70 (n/a)</td><td>765.17 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.90 (n/a)</td><td>332.10 (n/a)</td><td>284.90 (n/a)</td><td>276.50 (n/a)</td><td>103.92 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.40 (n/a)</td><td>425.96 (n/a)</td><td>473.20 (n/a)</td><td>232.90 (n/a)</td><td>144.98 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>445.50 (n/a)</td><td>314.34 (n/a)</td><td>293.70 (n/a)</td><td>259.80 (n/a)</td><td>75.07 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.60 (n/a)</td><td>435.72 (n/a)</td><td>436.10 (n/a)</td><td>291.50 (n/a)</td><td>97.91 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.00 (n/a)</td><td>525.48 (n/a)</td><td>531.70 (n/a)</td><td>445.70 (n/a)</td><td>50.75 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.60 (n/a)</td><td>455.32 (n/a)</td><td>501.50 (n/a)</td><td>286.00 (n/a)</td><td>105.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>541.60 (n/a)</td><td>341.86 (n/a)</td><td>295.70 (n/a)</td><td>272.70 (n/a)</td><td>112.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1063.70 (n/a)</td><td>423.52 (n/a)</td><td>270.40 (n/a)</td><td>219.80 (n/a)</td><td>359.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1847.30 (n/a)</td><td>709.28 (n/a)</td><td>519.80 (n/a)</td><td>250.90 (n/a)</td><td>657.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>517.10 (n/a)</td><td>471.34 (n/a)</td><td>488.10 (n/a)</td><td>421.60 (n/a)</td><td>44.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1001.60 (n/a)</td><td>509.64 (n/a)</td><td>524.40 (n/a)</td><td>222.60 (n/a)</td><td>309.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>604.40 (n/a)</td><td>476.72 (n/a)</td><td>569.50 (n/a)</td><td>287.30 (n/a)</td><td>154.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>666.80 (n/a)</td><td>428.30 (n/a)</td><td>408.60 (n/a)</td><td>212.70 (n/a)</td><td>193.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1403.90 (n/a)</td><td>617.48 (n/a)</td><td>479.80 (n/a)</td><td>274.30 (n/a)</td><td>454.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>650.40 (n/a)</td><td>452.88 (n/a)</td><td>395.70 (n/a)</td><td>298.10 (n/a)</td><td>149.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>582.10 (n/a)</td><td>382.30 (n/a)</td><td>297.20 (n/a)</td><td>191.50 (n/a)</td><td>177.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>540.40 (n/a)</td><td>458.64 (n/a)</td><td>499.30 (n/a)</td><td>278.20 (n/a)</td><td>104.91 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.68 (+13.39%)</td><td>0.48 <b>(+25.41%)</b></td><td>0.49 <b>(+40.70%)</b></td><td>0.26 <b>(+61.86%)</b></td><td>0.15 <b>(-27.87%)</b></td><td>843.10 <b>(-38.22%)</b></td><td>508.70 <b>(-33.31%)</b></td><td>449.50 <b>(-28.92%)</b></td><td>324.30 (-11.80%)</td><td>196.34 <b>(-55.59%)</b></td><td>29.10 (+13.39%)</td><td>20.42 <b>(+25.41%)</b></td><td>21.00 <b>(+40.70%)</b></td><td>11.19 <b>(+61.86%)</b></td><td>6.37 <b>(-27.87%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.60 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.16 (n/a)</td><td>0.21 (n/a)</td><td>1364.60 (n/a)</td><td>762.84 (n/a)</td><td>632.40 (n/a)</td><td>367.70 (n/a)</td><td>442.11 (n/a)</td><td>25.66 (n/a)</td><td>16.28 (n/a)</td><td>14.92 (n/a)</td><td>6.92 (n/a)</td><td>8.83 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.70 <b>(+41.18%)</b></td><td>0.39 (-4.23%)</td><td>0.36 <b>(-24.01%)</b></td><td>0.16 (-17.36%)</td><td>0.20 <b>(+65.97%)</b></td><td>1344.50 <b>(+21.00%)</b></td><td>712.34 (+17.33%)</td><td>619.30 <b>(+31.60%)</b></td><td>316.10 <b>(-29.16%)</b></td><td>397.81 <b>(+39.71%)</b></td><td>29.86 <b>(+41.18%)</b></td><td>16.76 (-4.23%)</td><td>15.24 <b>(-24.01%)</b></td><td>7.02 (-17.36%)</td><td>8.74 <b>(+65.97%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.50 (n/a)</td><td>0.41 (n/a)</td><td>0.47 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>1111.20 (n/a)</td><td>607.10 (n/a)</td><td>470.60 (n/a)</td><td>446.20 (n/a)</td><td>284.74 (n/a)</td><td>21.15 (n/a)</td><td>17.50 (n/a)</td><td>20.06 (n/a)</td><td>8.49 (n/a)</td><td>5.27 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.31 (+0.63%)</td><td>0.31 (-0.18%)</td><td>0.31 (+0.10%)</td><td>0.30 (-1.67%)</td><td>0.00 <b>(+161.60%)</b></td><td>83325.00 (+1.69%)</td><td>81769.94 (+0.19%)</td><td>81730.00 (-0.10%)</td><td>80587.90 (-0.63%)</td><td>1002.88 <b>(+164.68%)</b></td><td>213.18 (+0.63%)</td><td>210.13 (-0.18%)</td><td>210.20 (+0.10%)</td><td>206.18 (-1.67%)</td><td>2.56 <b>(+161.61%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.00 (n/a)</td><td>81936.60 (n/a)</td><td>81615.68 (n/a)</td><td>81812.30 (n/a)</td><td>81097.40 (n/a)</td><td>378.90 (n/a)</td><td>211.84 (n/a)</td><td>210.50 (n/a)</td><td>209.99 (n/a)</td><td>209.67 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>1.03 (-1.63%)</td><td>1.00 (-2.37%)</td><td>1.01 (-1.61%)</td><td>0.97 (-4.93%)</td><td>0.03 <b>(+139.33%)</b></td><td>25964.70 (+5.19%)</td><td>25059.84 (+2.47%)</td><td>24951.00 (+1.63%)</td><td>24412.30 (+1.66%)</td><td>676.23 <b>(+155.61%)</b></td><td>703.74 (-1.63%)</td><td>685.95 (-2.37%)</td><td>688.54 (-1.61%)</td><td>661.66 (-4.93%)</td><td>18.38 <b>(+139.33%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>1.05 (n/a)</td><td>1.03 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.01 (n/a)</td><td>24684.00 (n/a)</td><td>24454.60 (n/a)</td><td>24550.10 (n/a)</td><td>24013.40 (n/a)</td><td>264.56 (n/a)</td><td>715.43 (n/a)</td><td>702.59 (n/a)</td><td>699.79 (n/a)</td><td>695.99 (n/a)</td><td>7.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.81 (-1.47%)</td><td>0.79 (-0.07%)</td><td>0.79 (-1.27%)</td><td>0.78 (+1.23%)</td><td>0.01 <b>(-51.03%)</b></td><td>96814.90 (-1.21%)</td><td>95107.92 (+0.03%)</td><td>95420.30 (+1.28%)</td><td>93774.20 (+1.49%)</td><td>1282.99 <b>(-51.19%)</b></td><td>732.82 (-1.47%)</td><td>722.65 (-0.07%)</td><td>720.18 (-1.27%)</td><td>709.80 (+1.23%)</td><td>9.73 <b>(-51.03%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.77 (n/a)</td><td>0.02 (n/a)</td><td>98002.00 (n/a)</td><td>95082.96 (n/a)</td><td>94212.20 (n/a)</td><td>92395.60 (n/a)</td><td>2628.75 (n/a)</td><td>743.75 (n/a)</td><td>723.17 (n/a)</td><td>729.41 (n/a)</td><td>701.20 (n/a)</td><td>19.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.78 (+0.28%)</td><td>0.76 (+0.40%)</td><td>0.77 (+1.50%)</td><td>0.74 (-0.94%)</td><td>0.01 (+16.86%)</td><td>101590.40 (+0.95%)</td><td>98800.12 (-0.39%)</td><td>98116.00 (-1.48%)</td><td>97144.10 (-0.28%)</td><td>1748.10 (+17.84%)</td><td>707.40 (+0.28%)</td><td>695.71 (+0.40%)</td><td>700.39 (+1.50%)</td><td>676.44 (-0.94%)</td><td>12.15 (+16.86%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100636.10 (n/a)</td><td>99191.12 (n/a)</td><td>99589.10 (n/a)</td><td>97420.00 (n/a)</td><td>1483.43 (n/a)</td><td>705.39 (n/a)</td><td>692.92 (n/a)</td><td>690.03 (n/a)</td><td>682.85 (n/a)</td><td>10.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.80 (-0.03%)</td><td>0.79 (+0.36%)</td><td>0.79 (-0.03%)</td><td>0.78 (+0.78%)</td><td>0.01 <b>(-25.36%)</b></td><td>96717.50 (-0.77%)</td><td>95376.86 (-0.36%)</td><td>95205.90 (+0.03%)</td><td>94393.50 (+0.03%)</td><td>1007.99 <b>(-26.02%)</b></td><td>728.01 (-0.03%)</td><td>720.57 (+0.36%)</td><td>721.80 (-0.03%)</td><td>710.52 (+0.78%)</td><td>7.59 <b>(-25.36%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>97472.00 (n/a)</td><td>95724.28 (n/a)</td><td>95173.10 (n/a)</td><td>94366.50 (n/a)</td><td>1362.55 (n/a)</td><td>728.22 (n/a)</td><td>718.01 (n/a)</td><td>722.05 (n/a)</td><td>705.02 (n/a)</td><td>10.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>4.61 (-19.01%)</td><td>3.04 <b>(-41.84%)</b></td><td>2.30 <b>(-55.42%)</b></td><td>2.16 <b>(-53.81%)</b></td><td>1.17 <b>(+161.81%)</b></td><td>4134.20 <b>(+116.50%)</b></td><td>3260.00 <b>(+90.18%)</b></td><td>3868.80 <b>(+124.32%)</b></td><td>1933.50 <b>(+23.48%)</b></td><td>1081.68 <b>(+634.33%)</b></td><td>277.66 (-19.01%)</td><td>183.23 <b>(-41.84%)</b></td><td>138.77 <b>(-55.42%)</b></td><td>129.86 <b>(-53.81%)</b></td><td>70.25 <b>(+161.81%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>5.69 (n/a)</td><td>5.23 (n/a)</td><td>5.17 (n/a)</td><td>4.67 (n/a)</td><td>0.45 (n/a)</td><td>1909.60 (n/a)</td><td>1714.18 (n/a)</td><td>1724.70 (n/a)</td><td>1565.90 (n/a)</td><td>147.30 (n/a)</td><td>342.85 (n/a)</td><td>315.04 (n/a)</td><td>311.29 (n/a)</td><td>281.15 (n/a)</td><td>26.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>4.61 (-5.36%)</td><td>3.52 (+13.70%)</td><td>3.49 <b>(+20.12%)</b></td><td>2.35 (+8.27%)</td><td>0.99 (-9.75%)</td><td>3798.90 (-7.64%)</td><td>2705.38 (-13.65%)</td><td>2554.80 (-16.75%)</td><td>1934.50 (+5.66%)</td><td>796.38 (-15.08%)</td><td>277.52 (-5.36%)</td><td>212.25 (+13.70%)</td><td>210.14 <b>(+20.12%)</b></td><td>141.32 (+8.27%)</td><td>59.49 (-9.75%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>4.87 (n/a)</td><td>3.10 (n/a)</td><td>2.90 (n/a)</td><td>2.17 (n/a)</td><td>1.09 (n/a)</td><td>4113.10 (n/a)</td><td>3132.86 (n/a)</td><td>3068.80 (n/a)</td><td>1830.80 (n/a)</td><td>937.79 (n/a)</td><td>293.24 (n/a)</td><td>186.68 (n/a)</td><td>174.95 (n/a)</td><td>130.53 (n/a)</td><td>65.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>4.55 (+12.46%)</td><td>3.88 <b>(+45.90%)</b></td><td>4.04 <b>(+86.20%)</b></td><td>2.80 <b>(+29.50%)</b></td><td>0.65 <b>(-20.54%)</b></td><td>3182.60 <b>(-22.78%)</b></td><td>2359.04 <b>(-33.64%)</b></td><td>2205.10 <b>(-46.30%)</b></td><td>1960.90 (-11.08%)</td><td>473.96 <b>(-43.95%)</b></td><td>273.79 (+12.46%)</td><td>233.79 <b>(+45.90%)</b></td><td>243.46 <b>(+86.20%)</b></td><td>168.69 <b>(+29.50%)</b></td><td>38.94 <b>(-20.54%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>4.04 (n/a)</td><td>2.66 (n/a)</td><td>2.17 (n/a)</td><td>2.16 (n/a)</td><td>0.81 (n/a)</td><td>4121.60 (n/a)</td><td>3554.94 (n/a)</td><td>4106.10 (n/a)</td><td>2205.30 (n/a)</td><td>845.66 (n/a)</td><td>243.45 (n/a)</td><td>160.24 (n/a)</td><td>130.75 (n/a)</td><td>130.26 (n/a)</td><td>49.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>6.70 (+5.16%)</td><td>5.52 (-2.19%)</td><td>5.43 (-3.03%)</td><td>4.63 (-5.58%)</td><td>0.78 (+17.35%)</td><td>7535.70 (+5.91%)</td><td>6417.08 (+2.67%)</td><td>6423.40 (+3.12%)</td><td>5201.90 (-4.90%)</td><td>871.83 (+17.99%)</td><td>412.83 (+5.16%)</td><td>339.84 (-2.19%)</td><td>334.32 (-3.03%)</td><td>284.98 (-5.58%)</td><td>48.14 (+17.35%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.37 (n/a)</td><td>5.64 (n/a)</td><td>5.60 (n/a)</td><td>4.90 (n/a)</td><td>0.67 (n/a)</td><td>7114.90 (n/a)</td><td>6250.36 (n/a)</td><td>6229.00 (n/a)</td><td>5470.20 (n/a)</td><td>738.88 (n/a)</td><td>392.58 (n/a)</td><td>347.45 (n/a)</td><td>344.75 (n/a)</td><td>301.83 (n/a)</td><td>41.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>5.25 (-9.02%)</td><td>4.41 (-13.45%)</td><td>4.24 <b>(-21.74%)</b></td><td>4.09 (-2.09%)</td><td>0.49 <b>(-25.01%)</b></td><td>8515.10 (+2.14%)</td><td>7966.72 (+14.94%)</td><td>8231.00 <b>(+27.78%)</b></td><td>6635.90 (+9.91%)</td><td>781.48 (-16.84%)</td><td>323.62 (-9.02%)</td><td>271.90 (-13.45%)</td><td>260.90 <b>(-21.74%)</b></td><td>252.20 (-2.09%)</td><td>29.89 <b>(-25.01%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>5.77 (n/a)</td><td>5.10 (n/a)</td><td>5.41 (n/a)</td><td>4.18 (n/a)</td><td>0.65 (n/a)</td><td>8337.10 (n/a)</td><td>6931.20 (n/a)</td><td>6441.30 (n/a)</td><td>6037.70 (n/a)</td><td>939.68 (n/a)</td><td>355.68 (n/a)</td><td>314.14 (n/a)</td><td>333.39 (n/a)</td><td>257.58 (n/a)</td><td>39.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>5.99 (-10.18%)</td><td>4.93 (-9.27%)</td><td>4.94 (-7.21%)</td><td>4.24 (-4.40%)</td><td>0.69 (-17.36%)</td><td>8215.00 (+4.61%)</td><td>7180.28 (+9.83%)</td><td>7055.70 (+7.77%)</td><td>5820.10 (+11.33%)</td><td>952.52 (-2.81%)</td><td>368.98 (-10.18%)</td><td>303.58 (-9.27%)</td><td>304.36 (-7.21%)</td><td>261.41 (-4.40%)</td><td>42.61 (-17.36%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.67 (n/a)</td><td>5.43 (n/a)</td><td>5.33 (n/a)</td><td>4.44 (n/a)</td><td>0.84 (n/a)</td><td>7853.30 (n/a)</td><td>6537.88 (n/a)</td><td>6547.20 (n/a)</td><td>5227.80 (n/a)</td><td>980.02 (n/a)</td><td>410.78 (n/a)</td><td>334.59 (n/a)</td><td>328.00 (n/a)</td><td>273.45 (n/a)</td><td>51.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.78 (+0.79%)</td><td>0.76 (-0.51%)</td><td>0.76 (-0.99%)</td><td>0.75 (-1.62%)</td><td>0.01 <b>(+74.15%)</b></td><td>101050.10 (+1.65%)</td><td>98970.18 (+0.53%)</td><td>98984.30 (+1.00%)</td><td>96853.50 (-0.79%)</td><td>1492.25 <b>(+75.36%)</b></td><td>709.52 (+0.79%)</td><td>694.47 (-0.51%)</td><td>694.25 (-0.99%)</td><td>680.05 (-1.62%)</td><td>10.48 <b>(+74.15%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99408.10 (n/a)</td><td>98449.02 (n/a)</td><td>98008.10 (n/a)</td><td>97623.10 (n/a)</td><td>850.95 (n/a)</td><td>703.93 (n/a)</td><td>698.06 (n/a)</td><td>701.16 (n/a)</td><td>691.29 (n/a)</td><td>6.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.76 (-2.83%)</td><td>0.75 (-0.29%)</td><td>0.75 (+0.68%)</td><td>0.74 (+1.13%)</td><td>0.01 <b>(-62.53%)</b></td><td>101665.80 (-1.12%)</td><td>100698.16 (+0.25%)</td><td>100451.20 (-0.68%)</td><td>99771.50 (+2.91%)</td><td>895.65 <b>(-61.80%)</b></td><td>688.77 (-2.83%)</td><td>682.47 (-0.29%)</td><td>684.11 (+0.68%)</td><td>675.93 (+1.13%)</td><td>6.06 <b>(-62.53%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>102814.00 (n/a)</td><td>100448.28 (n/a)</td><td>101135.50 (n/a)</td><td>96952.80 (n/a)</td><td>2344.39 (n/a)</td><td>708.79 (n/a)</td><td>684.43 (n/a)</td><td>679.48 (n/a)</td><td>668.39 (n/a)</td><td>16.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.80 (-1.01%)</td><td>0.79 (-0.18%)</td><td>0.79 (-0.35%)</td><td>0.79 (+1.31%)</td><td>0.01 <b>(-53.57%)</b></td><td>95935.20 (-1.30%)</td><td>94983.70 (+0.16%)</td><td>95204.70 (+0.35%)</td><td>93920.60 (+1.02%)</td><td>807.39 <b>(-53.66%)</b></td><td>731.68 (-1.01%)</td><td>723.53 (-0.18%)</td><td>721.81 (-0.35%)</td><td>716.31 (+1.31%)</td><td>6.16 <b>(-53.57%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>97196.70 (n/a)</td><td>94835.14 (n/a)</td><td>94872.30 (n/a)</td><td>92973.70 (n/a)</td><td>1742.20 (n/a)</td><td>739.13 (n/a)</td><td>724.82 (n/a)</td><td>724.34 (n/a)</td><td>707.01 (n/a)</td><td>13.27 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>2.62 <b>(-33.33%)</b></td><td>1.77 <b>(-39.37%)</b></td><td>1.62 <b>(-43.52%)</b></td><td>1.37 <b>(-31.08%)</b></td><td>0.49 <b>(-46.04%)</b></td><td>5872.50 <b>(+45.10%)</b></td><td>4774.44 <b>(+59.82%)</b></td><td>4967.50 <b>(+77.05%)</b></td><td>3081.30 <b>(+50.00%)</b></td><td>1048.38 (+11.37%)</td><td>686.04 <b>(-33.33%)</b></td><td>464.97 <b>(-39.37%)</b></td><td>425.56 <b>(-43.52%)</b></td><td>359.97 <b>(-31.08%)</b></td><td>128.36 <b>(-46.04%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>3.92 (n/a)</td><td>2.92 (n/a)</td><td>2.87 (n/a)</td><td>1.99 (n/a)</td><td>0.91 (n/a)</td><td>4047.30 (n/a)</td><td>2987.44 (n/a)</td><td>2805.70 (n/a)</td><td>2054.20 (n/a)</td><td>941.32 (n/a)</td><td>1029.09 (n/a)</td><td>766.93 (n/a)</td><td>753.44 (n/a)</td><td>522.31 (n/a)</td><td>237.86 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.22 <b>(-23.19%)</b></td><td>0.19 (-13.30%)</td><td>0.18 (-11.52%)</td><td>0.17 (+13.84%)</td><td>0.02 <b>(-63.99%)</b></td><td>7247.10 (-12.15%)</td><td>6666.40 (+9.88%)</td><td>7069.30 (+13.02%)</td><td>5722.50 <b>(+30.19%)</b></td><td>702.41 <b>(-56.63%)</b></td><td>11.73 <b>(-23.19%)</b></td><td>10.16 (-13.30%)</td><td>9.49 (-11.52%)</td><td>9.26 (+13.84%)</td><td>1.13 <b>(-63.99%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>8249.70 (n/a)</td><td>6066.84 (n/a)</td><td>6254.90 (n/a)</td><td>4395.60 (n/a)</td><td>1619.62 (n/a)</td><td>15.27 (n/a)</td><td>11.72 (n/a)</td><td>10.73 (n/a)</td><td>8.13 (n/a)</td><td>3.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 <b>(-23.59%)</b></td><td>0.07 <b>(-22.26%)</b></td><td>0.06 <b>(-41.68%)</b></td><td>0.05 <b>(+176.88%)</b></td><td>0.02 <b>(-50.92%)</b></td><td>0.10 <b>(-23.59%)</b></td><td>0.07 <b>(-22.26%)</b></td><td>0.06 <b>(-41.68%)</b></td><td>0.05 <b>(+176.89%)</b></td><td>0.02 <b>(-50.92%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.91 (+3.87%)</td><td>3.69 (+2.45%)</td><td>3.79 (+6.03%)</td><td>3.38 (-3.78%)</td><td>0.24 <b>(+150.38%)</b></td><td>3.90 (+3.87%)</td><td>3.69 (+2.45%)</td><td>3.79 (+6.03%)</td><td>3.37 (-3.78%)</td><td>0.24 <b>(+150.38%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>3.76 (n/a)</td><td>3.61 (n/a)</td><td>3.58 (n/a)</td><td>3.51 (n/a)</td><td>0.09 (n/a)</td><td>3.76 (n/a)</td><td>3.60 (n/a)</td><td>3.58 (n/a)</td><td>3.51 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>7.53 (+14.12%)</td><td>7.04 (+19.15%)</td><td>7.49 <b>(+30.03%)</b></td><td>6.09 (+7.19%)</td><td>0.67 <b>(+72.10%)</b></td><td>7.53 (+14.12%)</td><td>7.03 (+19.15%)</td><td>7.48 <b>(+30.03%)</b></td><td>6.08 (+7.19%)</td><td>0.67 <b>(+72.10%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.60 (n/a)</td><td>5.91 (n/a)</td><td>5.76 (n/a)</td><td>5.68 (n/a)</td><td>0.39 (n/a)</td><td>6.60 (n/a)</td><td>5.90 (n/a)</td><td>5.76 (n/a)</td><td>5.67 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>13.12 <b>(+22.20%)</b></td><td>9.62 (+3.79%)</td><td>8.63 (-11.99%)</td><td>8.18 <b>(+21.01%)</b></td><td>2.07 <b>(+24.50%)</b></td><td>13.11 <b>(+22.20%)</b></td><td>9.62 (+3.79%)</td><td>8.62 (-11.99%)</td><td>8.17 <b>(+21.01%)</b></td><td>2.07 <b>(+24.50%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>10.74 (n/a)</td><td>9.27 (n/a)</td><td>9.81 (n/a)</td><td>6.76 (n/a)</td><td>1.66 (n/a)</td><td>10.73 (n/a)</td><td>9.26 (n/a)</td><td>9.80 (n/a)</td><td>6.75 (n/a)</td><td>1.66 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.85 (-2.53%)</td><td>3.72 (+0.58%)</td><td>3.75 (+0.13%)</td><td>3.53 (+2.00%)</td><td>0.12 <b>(-37.18%)</b></td><td>3.85 (-2.53%)</td><td>3.72 (+0.58%)</td><td>3.75 (+0.13%)</td><td>3.53 (+2.00%)</td><td>0.12 <b>(-37.18%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>3.95 (n/a)</td><td>3.70 (n/a)</td><td>3.75 (n/a)</td><td>3.46 (n/a)</td><td>0.20 (n/a)</td><td>3.95 (n/a)</td><td>3.70 (n/a)</td><td>3.75 (n/a)</td><td>3.46 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>7.42 (-1.41%)</td><td>6.39 (-3.94%)</td><td>5.99 (-12.40%)</td><td>5.53 (+2.53%)</td><td>0.92 (+8.18%)</td><td>7.42 (-1.41%)</td><td>6.38 (-3.94%)</td><td>5.99 (-12.40%)</td><td>5.52 (+2.53%)</td><td>0.92 (+8.18%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>7.53 (n/a)</td><td>6.65 (n/a)</td><td>6.84 (n/a)</td><td>5.39 (n/a)</td><td>0.85 (n/a)</td><td>7.52 (n/a)</td><td>6.64 (n/a)</td><td>6.83 (n/a)</td><td>5.39 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>14.17 (+2.74%)</td><td>11.35 (+13.49%)</td><td>13.14 <b>(+56.21%)</b></td><td>7.78 (+11.00%)</td><td>2.97 (-5.38%)</td><td>14.16 (+2.74%)</td><td>11.34 (+13.49%)</td><td>13.14 <b>(+56.21%)</b></td><td>7.78 (+11.00%)</td><td>2.97 (-5.38%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>13.79 (n/a)</td><td>10.00 (n/a)</td><td>8.41 (n/a)</td><td>7.01 (n/a)</td><td>3.14 (n/a)</td><td>13.78 (n/a)</td><td>9.99 (n/a)</td><td>8.41 (n/a)</td><td>7.01 (n/a)</td><td>3.14 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.24 (n/a)</td><td>1.49 (n/a)</td><td>1.04 (n/a)</td><td>1.03 (n/a)</td><td>0.98 (n/a)</td><td>3.24 (n/a)</td><td>1.49 (n/a)</td><td>1.04 (n/a)</td><td>1.03 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.32 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.11 (n/a)</td><td>0.32 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.59 (n/a)</td><td>0.36 (n/a)</td><td>0.45 (n/a)</td><td>0.08 (n/a)</td><td>0.23 (n/a)</td><td>0.58 (n/a)</td><td>0.35 (n/a)</td><td>0.45 (n/a)</td><td>0.08 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>2.47 (n/a)</td><td>1.43 (n/a)</td><td>1.88 (n/a)</td><td>0.43 (n/a)</td><td>0.94 (n/a)</td><td>2.43 (n/a)</td><td>1.41 (n/a)</td><td>1.85 (n/a)</td><td>0.42 (n/a)</td><td>0.92 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/layer_norm</summary>


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.50 (n/a)</td><td>375.12 (n/a)</td><td>393.10 (n/a)</td><td>277.90 (n/a)</td><td>87.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>631.60 (n/a)</td><td>440.20 (n/a)</td><td>465.30 (n/a)</td><td>229.50 (n/a)</td><td>176.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.00 (n/a)</td><td>481.26 (n/a)</td><td>537.70 (n/a)</td><td>298.80 (n/a)</td><td>128.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.30 (n/a)</td><td>422.86 (n/a)</td><td>446.60 (n/a)</td><td>268.90 (n/a)</td><td>137.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>830.70 (n/a)</td><td>534.04 (n/a)</td><td>525.50 (n/a)</td><td>379.50 (n/a)</td><td>183.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>673.40 (n/a)</td><td>549.00 (n/a)</td><td>504.90 (n/a)</td><td>474.60 (n/a)</td><td>85.62 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.70 (n/a)</td><td>390.32 (n/a)</td><td>382.60 (n/a)</td><td>291.10 (n/a)</td><td>89.93 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.30 (n/a)</td><td>433.10 (n/a)</td><td>465.00 (n/a)</td><td>269.20 (n/a)</td><td>102.29 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.00 (n/a)</td><td>425.60 (n/a)</td><td>409.80 (n/a)</td><td>277.10 (n/a)</td><td>150.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1869.70 (n/a)</td><td>682.16 (n/a)</td><td>407.40 (n/a)</td><td>244.90 (n/a)</td><td>677.68 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.30 (n/a)</td><td>352.70 (n/a)</td><td>298.90 (n/a)</td><td>253.90 (n/a)</td><td>101.26 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.90 (n/a)</td><td>440.98 (n/a)</td><td>483.90 (n/a)</td><td>264.60 (n/a)</td><td>159.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>622.20 (n/a)</td><td>358.64 (n/a)</td><td>297.60 (n/a)</td><td>273.70 (n/a)</td><td>148.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>516.00 (n/a)</td><td>467.94 (n/a)</td><td>471.90 (n/a)</td><td>399.40 (n/a)</td><td>44.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1296.80 (n/a)</td><td>610.54 (n/a)</td><td>547.70 (n/a)</td><td>282.50 (n/a)</td><td>400.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>771.00 (n/a)</td><td>469.90 (n/a)</td><td>499.20 (n/a)</td><td>251.60 (n/a)</td><td>216.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>471.10 (n/a)</td><td>333.26 (n/a)</td><td>321.80 (n/a)</td><td>223.70 (n/a)</td><td>88.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>602.40 (n/a)</td><td>408.30 (n/a)</td><td>444.70 (n/a)</td><td>254.70 (n/a)</td><td>148.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (-14.49%)</td><td>0.10 (+14.79%)</td><td>0.11 <b>(+30.36%)</b></td><td>0.06 <b>(+228.03%)</b></td><td>0.03 <b>(-46.02%)</b></td><td>584.20 <b>(-69.52%)</b></td><td>354.62 <b>(-46.19%)</b></td><td>304.70 <b>(-23.29%)</b></td><td>257.90 (+16.96%)</td><td>132.54 <b>(-81.36%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1916.40 (n/a)</td><td>659.02 (n/a)</td><td>397.20 (n/a)</td><td>220.50 (n/a)</td><td>711.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>620.30 (n/a)</td><td>444.48 (n/a)</td><td>502.30 (n/a)</td><td>234.90 (n/a)</td><td>164.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1898.80 (n/a)</td><td>817.86 (n/a)</td><td>591.60 (n/a)</td><td>275.10 (n/a)</td><td>680.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>528.80 (n/a)</td><td>431.52 (n/a)</td><td>459.70 (n/a)</td><td>289.30 (n/a)</td><td>96.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>597.60 (n/a)</td><td>475.70 (n/a)</td><td>490.10 (n/a)</td><td>300.60 (n/a)</td><td>118.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>620.80 (n/a)</td><td>452.14 (n/a)</td><td>459.20 (n/a)</td><td>302.50 (n/a)</td><td>124.95 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (-13.41%)</td><td>0.01 <b>(-20.59%)</b></td><td>0.01 <b>(-33.98%)</b></td><td>0.01 (-9.07%)</td><td>0.00 (-4.16%)</td><td>561.60 (+9.97%)</td><td>420.96 <b>(+26.33%)</b></td><td>442.20 <b>(+51.49%)</b></td><td>302.90 (+15.48%)</td><td>111.85 (+10.67%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.70 (n/a)</td><td>333.22 (n/a)</td><td>291.90 (n/a)</td><td>262.30 (n/a)</td><td>101.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 <b>(-36.40%)</b></td><td>0.01 <b>(-34.26%)</b></td><td>0.01 <b>(-27.35%)</b></td><td>0.00 <b>(-70.81%)</b></td><td>0.00 (-15.98%)</td><td>2427.10 <b>(+242.62%)</b></td><td>892.74 <b>(+102.27%)</b></td><td>511.10 <b>(+37.65%)</b></td><td>467.90 <b>(+57.22%)</b></td><td>858.36 <b>(+393.77%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>708.40 (n/a)</td><td>441.36 (n/a)</td><td>371.30 (n/a)</td><td>297.60 (n/a)</td><td>173.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (-6.36%)</td><td>0.01 (-13.65%)</td><td>0.01 <b>(-42.83%)</b></td><td>0.01 (+2.22%)</td><td>0.00 (-8.22%)</td><td>592.30 (-2.18%)</td><td>431.84 (+13.85%)</td><td>497.00 <b>(+74.94%)</b></td><td>260.40 (+6.81%)</td><td>146.52 (-7.31%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>605.50 (n/a)</td><td>379.32 (n/a)</td><td>284.10 (n/a)</td><td>243.80 (n/a)</td><td>158.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (-9.82%)</td><td>0.01 (-10.30%)</td><td>0.01 (-11.48%)</td><td>0.01 (+13.85%)</td><td>0.00 <b>(-20.67%)</b></td><td>583.50 (-12.16%)</td><td>407.58 (+5.28%)</td><td>387.80 (+12.96%)</td><td>233.90 (+10.91%)</td><td>148.86 (-19.63%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>664.30 (n/a)</td><td>387.14 (n/a)</td><td>343.30 (n/a)</td><td>210.90 (n/a)</td><td>185.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 <b>(-34.58%)</b></td><td>0.01 <b>(-45.58%)</b></td><td>0.01 <b>(-41.12%)</b></td><td>0.01 <b>(-56.53%)</b></td><td>0.00 <b>(+81.66%)</b></td><td>654.90 <b>(+130.03%)</b></td><td>504.70 <b>(+92.52%)</b></td><td>437.80 <b>(+69.82%)</b></td><td>367.00 <b>(+52.85%)</b></td><td>128.70 <b>(+562.85%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>284.70 (n/a)</td><td>262.16 (n/a)</td><td>257.80 (n/a)</td><td>240.10 (n/a)</td><td>19.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (+13.83%)</td><td>0.01 (+5.55%)</td><td>0.01 (-8.02%)</td><td>0.01 <b>(+69.52%)</b></td><td>0.00 (+2.19%)</td><td>673.80 <b>(-41.01%)</b></td><td>521.56 (-12.83%)</td><td>535.70 (+8.73%)</td><td>276.50 (-12.14%)</td><td>155.14 <b>(-51.82%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1142.20 (n/a)</td><td>598.34 (n/a)</td><td>492.70 (n/a)</td><td>314.70 (n/a)</td><td>322.00 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 <b>(-21.34%)</b></td><td>0.03 (-10.88%)</td><td>0.03 (+0.84%)</td><td>0.01 (-8.42%)</td><td>0.01 <b>(-26.93%)</b></td><td>553.80 (+9.19%)</td><td>337.60 (+9.91%)</td><td>292.80 (-0.81%)</td><td>260.00 <b>(+27.14%)</b></td><td>122.14 (+2.96%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.20 (n/a)</td><td>307.16 (n/a)</td><td>295.20 (n/a)</td><td>204.50 (n/a)</td><td>118.62 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (-11.46%)</td><td>0.03 (+9.12%)</td><td>0.03 (+13.82%)</td><td>0.01 (-17.71%)</td><td>0.01 (-11.52%)</td><td>639.60 <b>(+21.53%)</b></td><td>345.92 (-7.79%)</td><td>280.90 (-12.14%)</td><td>254.30 (+12.97%)</td><td>164.79 (+17.63%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.30 (n/a)</td><td>375.16 (n/a)</td><td>319.70 (n/a)</td><td>225.10 (n/a)</td><td>140.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (-4.94%)</td><td>0.02 (-11.87%)</td><td>0.02 <b>(-28.91%)</b></td><td>0.01 (-1.49%)</td><td>0.01 (+5.45%)</td><td>593.20 (+1.52%)</td><td>418.56 (+14.59%)</td><td>424.50 <b>(+40.70%)</b></td><td>274.90 (+5.20%)</td><td>139.63 (+5.73%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.30 (n/a)</td><td>365.28 (n/a)</td><td>301.70 (n/a)</td><td>261.30 (n/a)</td><td>132.06 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (-15.84%)</td><td>0.02 (-17.61%)</td><td>0.02 <b>(-45.95%)</b></td><td>0.01 (+11.25%)</td><td>0.01 <b>(-24.94%)</b></td><td>556.70 (-10.11%)</td><td>406.32 (+9.39%)</td><td>463.60 <b>(+85.00%)</b></td><td>203.50 (+18.80%)</td><td>156.52 <b>(-25.76%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.30 (n/a)</td><td>371.44 (n/a)</td><td>250.60 (n/a)</td><td>171.30 (n/a)</td><td>210.83 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (-17.33%)</td><td>0.02 <b>(-27.30%)</b></td><td>0.02 <b>(-41.44%)</b></td><td>0.02 <b>(-21.41%)</b></td><td>0.01 (+7.62%)</td><td>467.40 <b>(+27.22%)</b></td><td>369.48 <b>(+40.71%)</b></td><td>405.40 <b>(+70.77%)</b></td><td>262.60 <b>(+20.96%)</b></td><td>94.08 <b>(+55.74%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>367.40 (n/a)</td><td>262.58 (n/a)</td><td>237.40 (n/a)</td><td>217.10 (n/a)</td><td>60.41 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (-5.17%)</td><td>0.02 <b>(+21.21%)</b></td><td>0.03 <b>(+59.43%)</b></td><td>0.01 (-9.80%)</td><td>0.01 (-2.71%)</td><td>570.80 (+10.86%)</td><td>358.38 (-16.66%)</td><td>300.60 <b>(-37.27%)</b></td><td>278.50 (+5.45%)</td><td>121.55 <b>(+21.23%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.90 (n/a)</td><td>430.00 (n/a)</td><td>479.20 (n/a)</td><td>264.10 (n/a)</td><td>100.26 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 <b>(+29.34%)</b></td><td>0.03 (+10.73%)</td><td>0.02 <b>(-26.21%)</b></td><td>0.02 <b>(+26.14%)</b></td><td>0.01 <b>(+31.47%)</b></td><td>471.30 <b>(-20.71%)</b></td><td>358.64 (-9.05%)</td><td>409.60 <b>(+35.49%)</b></td><td>201.00 <b>(-22.66%)</b></td><td>125.45 (-18.50%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.40 (n/a)</td><td>394.32 (n/a)</td><td>302.30 (n/a)</td><td>259.90 (n/a)</td><td>153.92 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 <b>(-28.44%)</b></td><td>0.02 <b>(-27.33%)</b></td><td>0.01 <b>(-23.36%)</b></td><td>0.01 <b>(-24.79%)</b></td><td>0.01 <b>(-30.96%)</b></td><td>691.50 <b>(+32.96%)</b></td><td>545.80 <b>(+34.55%)</b></td><td>592.10 <b>(+30.48%)</b></td><td>249.20 <b>(+39.76%)</b></td><td>171.07 <b>(+20.50%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.10 (n/a)</td><td>405.66 (n/a)</td><td>453.80 (n/a)</td><td>178.30 (n/a)</td><td>141.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (-15.79%)</td><td>0.04 (-16.88%)</td><td>0.05 (-7.57%)</td><td>0.01 <b>(-75.75%)</b></td><td>0.02 (+17.63%)</td><td>2389.30 <b>(+312.37%)</b></td><td>766.16 <b>(+98.03%)</b></td><td>298.10 (+8.20%)</td><td>288.70 (+18.76%)</td><td>914.60 <b>(+437.88%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>579.40 (n/a)</td><td>386.90 (n/a)</td><td>275.50 (n/a)</td><td>243.10 (n/a)</td><td>170.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (-10.62%)</td><td>0.04 (-4.69%)</td><td>0.04 <b>(+20.75%)</b></td><td>0.03 (-4.85%)</td><td>0.02 (-14.50%)</td><td>636.90 (+5.10%)</td><td>437.64 (+3.75%)</td><td>388.10 (-17.20%)</td><td>271.20 (+11.88%)</td><td>170.22 (+6.70%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>606.00 (n/a)</td><td>421.82 (n/a)</td><td>468.70 (n/a)</td><td>242.40 (n/a)</td><td>159.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (-15.49%)</td><td>0.05 (-1.37%)</td><td>0.05 (+12.60%)</td><td>0.03 (+4.49%)</td><td>0.01 <b>(-35.82%)</b></td><td>526.50 (-4.29%)</td><td>363.02 (-5.14%)</td><td>361.90 (-11.19%)</td><td>267.60 (+18.35%)</td><td>105.52 <b>(-26.87%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>550.10 (n/a)</td><td>382.70 (n/a)</td><td>407.50 (n/a)</td><td>226.10 (n/a)</td><td>144.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 <b>(+20.33%)</b></td><td>0.06 <b>(+52.53%)</b></td><td>0.07 <b>(+80.84%)</b></td><td>0.04 <b>(+60.71%)</b></td><td>0.01 <b>(-22.30%)</b></td><td>366.30 <b>(-37.77%)</b></td><td>273.12 <b>(-38.10%)</b></td><td>249.90 <b>(-44.70%)</b></td><td>228.50 (-16.88%)</td><td>55.23 <b>(-59.54%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.60 (n/a)</td><td>441.20 (n/a)</td><td>451.90 (n/a)</td><td>274.90 (n/a)</td><td>136.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 <b>(-24.52%)</b></td><td>0.05 (-12.32%)</td><td>0.05 (-6.04%)</td><td>0.03 (-5.54%)</td><td>0.01 <b>(-25.54%)</b></td><td>542.60 (+5.87%)</td><td>392.38 (+12.05%)</td><td>322.60 (+6.43%)</td><td>269.80 <b>(+32.45%)</b></td><td>133.22 (+7.21%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>512.50 (n/a)</td><td>350.18 (n/a)</td><td>303.10 (n/a)</td><td>203.70 (n/a)</td><td>124.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (-8.92%)</td><td>0.04 (+3.32%)</td><td>0.04 (+5.17%)</td><td>0.03 (+2.15%)</td><td>0.01 <b>(-24.40%)</b></td><td>613.10 (-2.11%)</td><td>450.94 (-6.25%)</td><td>465.90 (-4.90%)</td><td>317.50 (+9.79%)</td><td>112.14 <b>(-20.88%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>626.30 (n/a)</td><td>481.02 (n/a)</td><td>489.90 (n/a)</td><td>289.20 (n/a)</td><td>141.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (-10.26%)</td><td>0.09 (-17.27%)</td><td>0.08 <b>(-34.31%)</b></td><td>0.06 (-15.77%)</td><td>0.03 (-18.31%)</td><td>557.70 (+18.71%)</td><td>410.72 (+19.12%)</td><td>433.00 <b>(+52.25%)</b></td><td>271.90 (+11.43%)</td><td>116.16 (+1.50%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>469.80 (n/a)</td><td>344.80 (n/a)</td><td>284.40 (n/a)</td><td>244.00 (n/a)</td><td>114.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (-3.58%)</td><td>0.09 (-9.97%)</td><td>0.07 <b>(-38.14%)</b></td><td>0.06 (-7.28%)</td><td>0.04 (+13.36%)</td><td>573.10 (+7.85%)</td><td>417.26 (+15.16%)</td><td>478.00 <b>(+61.65%)</b></td><td>239.60 (+3.72%)</td><td>165.43 (+17.03%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>531.40 (n/a)</td><td>362.34 (n/a)</td><td>295.70 (n/a)</td><td>231.00 (n/a)</td><td>141.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (+10.23%)</td><td>0.10 (+16.60%)</td><td>0.09 (+14.54%)</td><td>0.07 <b>(+52.02%)</b></td><td>0.03 (+3.62%)</td><td>501.80 <b>(-34.22%)</b></td><td>373.78 (-17.40%)</td><td>363.40 (-12.69%)</td><td>230.30 (-9.29%)</td><td>115.97 <b>(-38.17%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>762.80 (n/a)</td><td>452.52 (n/a)</td><td>416.20 (n/a)</td><td>253.90 (n/a)</td><td>187.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (-4.70%)</td><td>0.07 <b>(-21.30%)</b></td><td>0.07 (-15.71%)</td><td>0.02 <b>(-71.11%)</b></td><td>0.04 (+16.44%)</td><td>2051.10 <b>(+246.18%)</b></td><td>744.44 <b>(+83.59%)</b></td><td>477.90 (+18.64%)</td><td>255.30 (+4.93%)</td><td>739.71 <b>(+384.91%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>592.50 (n/a)</td><td>405.48 (n/a)</td><td>402.80 (n/a)</td><td>243.30 (n/a)</td><td>152.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 <b>(-21.25%)</b></td><td>0.07 (-17.77%)</td><td>0.06 <b>(-40.30%)</b></td><td>0.05 <b>(+62.47%)</b></td><td>0.02 <b>(-45.73%)</b></td><td>639.80 <b>(-38.45%)</b></td><td>498.66 (+0.24%)</td><td>523.90 <b>(+67.49%)</b></td><td>340.80 <b>(+26.97%)</b></td><td>143.19 <b>(-56.44%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1039.50 (n/a)</td><td>497.46 (n/a)</td><td>312.80 (n/a)</td><td>268.40 (n/a)</td><td>328.70 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 <b>(-30.71%)</b></td><td>0.01 <b>(-21.67%)</b></td><td>0.01 <b>(+20.51%)</b></td><td>0.00 <b>(-74.68%)</b></td><td>0.01 (+14.62%)</td><td>1920.70 <b>(+294.88%)</b></td><td>676.52 <b>(+98.29%)</b></td><td>294.20 (-17.01%)</td><td>278.90 <b>(+44.28%)</b></td><td>708.14 <b>(+560.58%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>486.40 (n/a)</td><td>341.18 (n/a)</td><td>354.50 (n/a)</td><td>193.30 (n/a)</td><td>107.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (+6.03%)</td><td>0.01 (+17.62%)</td><td>0.01 <b>(+70.25%)</b></td><td>0.01 (+9.58%)</td><td>0.00 (-15.44%)</td><td>498.20 (-8.75%)</td><td>344.18 (-17.97%)</td><td>288.60 <b>(-41.26%)</b></td><td>251.20 (-5.71%)</td><td>103.04 <b>(-24.68%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.00 (n/a)</td><td>419.60 (n/a)</td><td>491.30 (n/a)</td><td>266.40 (n/a)</td><td>136.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (+2.12%)</td><td>0.01 (-16.68%)</td><td>0.01 <b>(-20.60%)</b></td><td>0.00 <b>(-68.45%)</b></td><td>0.00 <b>(+39.37%)</b></td><td>1927.90 <b>(+216.98%)</b></td><td>800.74 <b>(+63.88%)</b></td><td>618.50 <b>(+25.94%)</b></td><td>262.20 (-2.09%)</td><td>647.90 <b>(+375.94%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.20 (n/a)</td><td>488.62 (n/a)</td><td>491.10 (n/a)</td><td>267.80 (n/a)</td><td>136.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 <b>(-32.72%)</b></td><td>0.01 <b>(-20.13%)</b></td><td>0.01 (-5.89%)</td><td>0.01 (-7.96%)</td><td>0.00 <b>(-53.98%)</b></td><td>479.10 (+8.64%)</td><td>348.80 (+14.42%)</td><td>310.10 (+6.27%)</td><td>272.10 <b>(+48.61%)</b></td><td>91.35 <b>(-26.04%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>441.00 (n/a)</td><td>304.84 (n/a)</td><td>291.80 (n/a)</td><td>183.10 (n/a)</td><td>123.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 <b>(+21.69%)</b></td><td>0.01 (+6.70%)</td><td>0.01 <b>(+32.33%)</b></td><td>0.00 <b>(-71.29%)</b></td><td>0.01 <b>(+104.30%)</b></td><td>1980.20 <b>(+248.32%)</b></td><td>677.64 <b>(+57.04%)</b></td><td>322.90 <b>(-24.43%)</b></td><td>224.20 (-17.85%)</td><td>739.13 <b>(+543.48%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.50 (n/a)</td><td>431.50 (n/a)</td><td>427.30 (n/a)</td><td>272.90 (n/a)</td><td>114.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 <b>(+31.15%)</b></td><td>0.01 <b>(+37.72%)</b></td><td>0.01 (+0.91%)</td><td>0.01 <b>(+271.27%)</b></td><td>0.00 (+13.52%)</td><td>568.90 <b>(-73.06%)</b></td><td>430.86 <b>(-45.81%)</b></td><td>520.50 (-0.89%)</td><td>226.90 <b>(-23.76%)</b></td><td>156.69 <b>(-78.95%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2112.10 (n/a)</td><td>795.02 (n/a)</td><td>525.20 (n/a)</td><td>297.60 (n/a)</td><td>744.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 <b>(-39.22%)</b></td><td>0.01 <b>(-21.14%)</b></td><td>0.01 (+0.98%)</td><td>0.00 <b>(-42.37%)</b></td><td>0.01 <b>(-46.44%)</b></td><td>1353.40 <b>(+73.54%)</b></td><td>627.04 <b>(+21.50%)</b></td><td>516.80 (-0.96%)</td><td>243.50 <b>(+64.53%)</b></td><td>423.25 <b>(+77.63%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>779.90 (n/a)</td><td>516.10 (n/a)</td><td>521.80 (n/a)</td><td>148.00 (n/a)</td><td>238.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (-14.89%)</td><td>0.01 (+14.37%)</td><td>0.01 (-3.12%)</td><td>0.01 <b>(+304.34%)</b></td><td>0.00 <b>(-58.83%)</b></td><td>499.90 <b>(-75.27%)</b></td><td>332.30 <b>(-50.85%)</b></td><td>293.60 (+3.23%)</td><td>283.40 (+17.50%)</td><td>93.94 <b>(-87.71%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2021.30 (n/a)</td><td>676.06 (n/a)</td><td>284.40 (n/a)</td><td>241.20 (n/a)</td><td>764.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 <b>(-30.85%)</b></td><td>0.01 (-16.61%)</td><td>0.01 <b>(-32.26%)</b></td><td>0.01 (+13.36%)</td><td>0.00 <b>(-49.24%)</b></td><td>529.90 (-11.79%)</td><td>409.18 (+6.61%)</td><td>438.30 <b>(+47.63%)</b></td><td>287.10 <b>(+44.56%)</b></td><td>105.26 <b>(-40.94%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.70 (n/a)</td><td>383.82 (n/a)</td><td>296.90 (n/a)</td><td>198.60 (n/a)</td><td>178.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (+4.79%)</td><td>0.01 <b>(+20.71%)</b></td><td>0.01 <b>(+36.18%)</b></td><td>0.01 <b>(+290.45%)</b></td><td>0.00 <b>(-27.67%)</b></td><td>633.80 <b>(-74.39%)</b></td><td>403.92 <b>(-50.66%)</b></td><td>375.80 <b>(-26.57%)</b></td><td>237.80 (-4.57%)</td><td>154.07 <b>(-83.52%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2474.70 (n/a)</td><td>818.62 (n/a)</td><td>511.80 (n/a)</td><td>249.20 (n/a)</td><td>935.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 <b>(-23.90%)</b></td><td>0.01 (-11.58%)</td><td>0.01 (-7.03%)</td><td>0.01 (-3.44%)</td><td>0.00 <b>(-35.00%)</b></td><td>674.80 (+3.58%)</td><td>520.58 (+6.81%)</td><td>587.70 (+7.56%)</td><td>288.80 <b>(+31.39%)</b></td><td>152.74 (-8.69%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.50 (n/a)</td><td>487.40 (n/a)</td><td>546.40 (n/a)</td><td>219.80 (n/a)</td><td>167.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 <b>(-28.76%)</b></td><td>0.01 (+8.63%)</td><td>0.01 <b>(+69.33%)</b></td><td>0.01 (+11.11%)</td><td>0.00 <b>(-41.24%)</b></td><td>505.50 (-10.01%)</td><td>363.38 (-17.03%)</td><td>322.50 <b>(-40.94%)</b></td><td>251.20 <b>(+40.41%)</b></td><td>122.55 <b>(-27.34%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.70 (n/a)</td><td>437.96 (n/a)</td><td>546.10 (n/a)</td><td>178.90 (n/a)</td><td>168.67 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 <b>(-29.07%)</b></td><td>0.03 (-1.65%)</td><td>0.03 (-1.87%)</td><td>0.02 <b>(+23.64%)</b></td><td>0.01 <b>(-51.74%)</b></td><td>435.30 (-19.12%)</td><td>293.50 (-11.24%)</td><td>285.60 (+1.89%)</td><td>214.60 <b>(+41.00%)</b></td><td>85.71 <b>(-44.71%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>538.20 (n/a)</td><td>330.68 (n/a)</td><td>280.30 (n/a)</td><td>152.20 (n/a)</td><td>155.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (+6.28%)</td><td>0.03 <b>(+21.01%)</b></td><td>0.03 (+11.95%)</td><td>0.02 (-1.50%)</td><td>0.01 (+11.40%)</td><td>502.30 (+1.52%)</td><td>305.38 (-16.70%)</td><td>297.70 (-10.68%)</td><td>209.60 (-5.88%)</td><td>118.54 (-1.00%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.80 (n/a)</td><td>366.60 (n/a)</td><td>333.30 (n/a)</td><td>222.70 (n/a)</td><td>119.74 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (-10.19%)</td><td>0.02 (-14.10%)</td><td>0.02 <b>(-21.30%)</b></td><td>0.00 <b>(-71.65%)</b></td><td>0.01 <b>(+23.41%)</b></td><td>1993.80 <b>(+252.70%)</b></td><td>698.70 <b>(+80.52%)</b></td><td>489.90 <b>(+27.08%)</b></td><td>229.20 (+11.37%)</td><td>737.44 <b>(+369.96%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.30 (n/a)</td><td>387.04 (n/a)</td><td>385.50 (n/a)</td><td>205.80 (n/a)</td><td>156.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (-17.30%)</td><td>0.03 (-12.41%)</td><td>0.03 (-5.46%)</td><td>0.02 (+4.05%)</td><td>0.01 <b>(-21.43%)</b></td><td>484.90 (-3.89%)</td><td>341.40 (+11.24%)</td><td>288.20 (+5.76%)</td><td>239.20 <b>(+20.93%)</b></td><td>104.48 (-11.26%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.50 (n/a)</td><td>306.90 (n/a)</td><td>272.50 (n/a)</td><td>197.80 (n/a)</td><td>117.74 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (-15.77%)</td><td>0.03 <b>(+31.33%)</b></td><td>0.03 <b>(+89.72%)</b></td><td>0.02 <b>(+25.72%)</b></td><td>0.01 <b>(-36.38%)</b></td><td>448.70 <b>(-20.46%)</b></td><td>307.46 <b>(-33.33%)</b></td><td>289.40 <b>(-47.29%)</b></td><td>194.70 (+18.72%)</td><td>105.25 <b>(-38.23%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>564.10 (n/a)</td><td>461.20 (n/a)</td><td>549.00 (n/a)</td><td>164.00 (n/a)</td><td>170.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (+6.51%)</td><td>0.02 (+1.54%)</td><td>0.02 (+2.12%)</td><td>0.00 <b>(-75.74%)</b></td><td>0.01 <b>(+61.22%)</b></td><td>2055.60 <b>(+312.19%)</b></td><td>699.76 <b>(+62.09%)</b></td><td>456.20 (-2.08%)</td><td>225.50 (-6.12%)</td><td>765.46 <b>(+607.89%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.70 (n/a)</td><td>431.70 (n/a)</td><td>465.90 (n/a)</td><td>240.20 (n/a)</td><td>108.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 <b>(-28.91%)</b></td><td>0.03 (+16.66%)</td><td>0.03 <b>(+76.34%)</b></td><td>0.02 (+14.31%)</td><td>0.01 <b>(-40.50%)</b></td><td>533.90 (-12.50%)</td><td>361.50 <b>(-23.66%)</b></td><td>309.30 <b>(-43.30%)</b></td><td>239.80 <b>(+40.65%)</b></td><td>136.53 <b>(-23.65%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.20 (n/a)</td><td>473.52 (n/a)</td><td>545.50 (n/a)</td><td>170.50 (n/a)</td><td>178.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (+10.39%)</td><td>0.02 <b>(+38.20%)</b></td><td>0.03 <b>(+80.48%)</b></td><td>0.01 (+16.56%)</td><td>0.01 <b>(+29.76%)</b></td><td>572.10 (-14.22%)</td><td>381.98 <b>(-24.82%)</b></td><td>302.90 <b>(-44.59%)</b></td><td>247.40 (-9.44%)</td><td>159.28 (+8.60%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.90 (n/a)</td><td>508.12 (n/a)</td><td>546.70 (n/a)</td><td>273.20 (n/a)</td><td>146.67 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (-3.05%)</td><td>0.02 (-0.61%)</td><td>0.02 <b>(-20.83%)</b></td><td>0.01 (+18.84%)</td><td>0.01 (-5.24%)</td><td>554.90 (-15.85%)</td><td>446.80 (-1.02%)</td><td>536.10 <b>(+26.32%)</b></td><td>251.90 (+3.15%)</td><td>137.45 (-13.47%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>659.40 (n/a)</td><td>451.40 (n/a)</td><td>424.40 (n/a)</td><td>244.20 (n/a)</td><td>158.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (+18.51%)</td><td>0.03 <b>(+32.38%)</b></td><td>0.03 <b>(+65.89%)</b></td><td>0.01 (+7.94%)</td><td>0.01 <b>(+31.39%)</b></td><td>554.30 (-7.35%)</td><td>315.24 <b>(-22.16%)</b></td><td>251.80 <b>(-39.72%)</b></td><td>235.00 (-15.62%)</td><td>135.27 (+7.84%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.30 (n/a)</td><td>404.98 (n/a)</td><td>417.70 (n/a)</td><td>278.50 (n/a)</td><td>125.45 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 <b>(+21.08%)</b></td><td>0.02 <b>(+22.20%)</b></td><td>0.02 <b>(+29.22%)</b></td><td>0.01 (+0.88%)</td><td>0.01 <b>(+35.63%)</b></td><td>578.60 (-0.87%)</td><td>370.96 (-16.11%)</td><td>354.40 <b>(-22.62%)</b></td><td>269.00 (-17.41%)</td><td>122.22 (+17.46%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.70 (n/a)</td><td>442.20 (n/a)</td><td>458.00 (n/a)</td><td>325.70 (n/a)</td><td>104.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 <b>(+37.69%)</b></td><td>0.02 <b>(+45.68%)</b></td><td>0.02 <b>(+26.31%)</b></td><td>0.01 <b>(+62.29%)</b></td><td>0.01 <b>(+37.51%)</b></td><td>675.40 <b>(-38.38%)</b></td><td>435.96 <b>(-33.14%)</b></td><td>418.50 <b>(-20.84%)</b></td><td>263.10 <b>(-27.36%)</b></td><td>172.01 <b>(-41.78%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1096.10 (n/a)</td><td>652.02 (n/a)</td><td>528.70 (n/a)</td><td>362.20 (n/a)</td><td>295.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (-1.29%)</td><td>0.05 (+16.74%)</td><td>0.06 <b>(+33.22%)</b></td><td>0.03 (-8.39%)</td><td>0.01 (+4.24%)</td><td>534.70 (+9.17%)</td><td>325.22 (-13.35%)</td><td>268.30 <b>(-24.93%)</b></td><td>259.30 (+1.33%)</td><td>118.53 (+12.80%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>489.80 (n/a)</td><td>375.32 (n/a)</td><td>357.40 (n/a)</td><td>255.90 (n/a)</td><td>105.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (+12.79%)</td><td>0.05 (+9.44%)</td><td>0.06 <b>(+25.73%)</b></td><td>0.03 (-9.81%)</td><td>0.02 <b>(+51.61%)</b></td><td>559.40 (+10.88%)</td><td>373.62 (-0.93%)</td><td>286.00 <b>(-20.45%)</b></td><td>231.60 (-11.33%)</td><td>163.50 <b>(+53.83%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>504.50 (n/a)</td><td>377.14 (n/a)</td><td>359.50 (n/a)</td><td>261.20 (n/a)</td><td>106.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 <b>(+26.79%)</b></td><td>0.06 <b>(+56.15%)</b></td><td>0.06 <b>(+60.74%)</b></td><td>0.05 <b>(+81.23%)</b></td><td>0.01 (-19.31%)</td><td>355.30 <b>(-44.82%)</b></td><td>269.04 <b>(-39.44%)</b></td><td>253.60 <b>(-37.80%)</b></td><td>221.40 <b>(-21.13%)</b></td><td>50.87 <b>(-63.84%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>643.90 (n/a)</td><td>444.22 (n/a)</td><td>407.70 (n/a)</td><td>280.70 (n/a)</td><td>140.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (+18.74%)</td><td>0.06 <b>(+23.25%)</b></td><td>0.06 <b>(+21.26%)</b></td><td>0.05 <b>(+42.10%)</b></td><td>0.00 <b>(-35.08%)</b></td><td>303.60 <b>(-29.62%)</b></td><td>272.24 <b>(-20.08%)</b></td><td>264.60 (-17.52%)</td><td>245.60 (-15.78%)</td><td>22.00 <b>(-61.43%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>431.40 (n/a)</td><td>340.64 (n/a)</td><td>320.80 (n/a)</td><td>291.60 (n/a)</td><td>57.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (+17.01%)</td><td>0.05 <b>(+25.60%)</b></td><td>0.05 <b>(+33.22%)</b></td><td>0.04 <b>(+42.68%)</b></td><td>0.01 (-4.15%)</td><td>386.80 <b>(-29.91%)</b></td><td>314.18 <b>(-22.94%)</b></td><td>344.00 <b>(-24.94%)</b></td><td>236.30 (-14.54%)</td><td>70.79 <b>(-41.32%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>551.90 (n/a)</td><td>407.70 (n/a)</td><td>458.30 (n/a)</td><td>276.50 (n/a)</td><td>120.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 <b>(+22.19%)</b></td><td>0.06 (+19.00%)</td><td>0.06 (+16.62%)</td><td>0.05 <b>(+54.02%)</b></td><td>0.01 (-8.19%)</td><td>342.70 <b>(-35.07%)</b></td><td>273.34 (-18.85%)</td><td>259.00 (-14.24%)</td><td>214.50 (-18.13%)</td><td>51.09 <b>(-53.01%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>527.80 (n/a)</td><td>336.84 (n/a)</td><td>302.00 (n/a)</td><td>262.00 (n/a)</td><td>108.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 <b>(-21.73%)</b></td><td>0.03 (-3.61%)</td><td>0.03 (-2.23%)</td><td>0.02 <b>(+85.46%)</b></td><td>0.01 <b>(-39.73%)</b></td><td>1061.30 <b>(-46.08%)</b></td><td>662.88 (-19.65%)</td><td>551.50 (+2.28%)</td><td>443.30 <b>(+27.75%)</b></td><td>258.55 <b>(-61.03%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1968.20 (n/a)</td><td>825.04 (n/a)</td><td>539.20 (n/a)</td><td>347.00 (n/a)</td><td>663.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 <b>(+28.68%)</b></td><td>0.05 <b>(+25.57%)</b></td><td>0.04 <b>(+20.51%)</b></td><td>0.03 <b>(+20.87%)</b></td><td>0.02 <b>(+35.76%)</b></td><td>482.30 (-17.27%)</td><td>361.06 (-19.36%)</td><td>384.20 (-17.04%)</td><td>212.00 <b>(-22.29%)</b></td><td>110.02 (-13.52%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>583.00 (n/a)</td><td>447.74 (n/a)</td><td>463.10 (n/a)</td><td>272.80 (n/a)</td><td>127.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (+4.66%)</td><td>0.05 <b>(+47.12%)</b></td><td>0.04 <b>(+48.27%)</b></td><td>0.03 <b>(+364.20%)</b></td><td>0.01 <b>(-32.13%)</b></td><td>533.20 <b>(-78.46%)</b></td><td>382.00 <b>(-56.38%)</b></td><td>365.50 <b>(-32.56%)</b></td><td>275.10 (-4.45%)</td><td>106.57 <b>(-88.17%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2475.10 (n/a)</td><td>875.84 (n/a)</td><td>542.00 (n/a)</td><td>287.90 (n/a)</td><td>900.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (+0.90%)</td><td>0.05 <b>(+28.41%)</b></td><td>0.06 <b>(+65.25%)</b></td><td>0.03 <b>(+22.74%)</b></td><td>0.01 (-1.15%)</td><td>489.70 (-18.53%)</td><td>348.76 <b>(-22.94%)</b></td><td>288.60 <b>(-39.48%)</b></td><td>269.40 (-0.88%)</td><td>98.90 (-16.91%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>601.10 (n/a)</td><td>452.60 (n/a)</td><td>476.90 (n/a)</td><td>271.80 (n/a)</td><td>119.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (+0.98%)</td><td>0.04 (-5.17%)</td><td>0.03 (-5.11%)</td><td>0.01 <b>(-58.07%)</b></td><td>0.02 <b>(+21.99%)</b></td><td>1965.80 <b>(+138.51%)</b></td><td>748.94 <b>(+44.51%)</b></td><td>485.40 (+5.38%)</td><td>244.50 (-0.97%)</td><td>695.69 <b>(+227.03%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>824.20 (n/a)</td><td>518.26 (n/a)</td><td>460.60 (n/a)</td><td>246.90 (n/a)</td><td>212.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (-3.13%)</td><td>0.04 (+4.62%)</td><td>0.03 (+2.45%)</td><td>0.02 (-12.31%)</td><td>0.01 <b>(+31.66%)</b></td><td>663.20 (+14.05%)</td><td>483.96 (+1.37%)</td><td>503.60 (-2.40%)</td><td>303.50 (+3.23%)</td><td>174.59 <b>(+57.60%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>581.50 (n/a)</td><td>477.44 (n/a)</td><td>516.00 (n/a)</td><td>294.00 (n/a)</td><td>110.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (+6.85%)</td><td>0.10 (+11.01%)</td><td>0.12 (+16.02%)</td><td>0.06 (+18.49%)</td><td>0.03 (+11.22%)</td><td>542.90 (-15.59%)</td><td>371.04 (-10.05%)</td><td>279.10 (-13.80%)</td><td>265.50 (-6.42%)</td><td>138.95 (-12.38%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>643.20 (n/a)</td><td>412.48 (n/a)</td><td>323.80 (n/a)</td><td>283.70 (n/a)</td><td>158.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (+2.55%)</td><td>0.10 (-3.31%)</td><td>0.11 (-2.98%)</td><td>0.07 <b>(+22.81%)</b></td><td>0.03 (+0.44%)</td><td>469.20 (-18.57%)</td><td>352.44 (+1.70%)</td><td>304.30 (+3.08%)</td><td>264.60 (-2.47%)</td><td>99.33 <b>(-22.89%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>576.20 (n/a)</td><td>346.56 (n/a)</td><td>295.20 (n/a)</td><td>271.30 (n/a)</td><td>128.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.15 (+9.85%)</td><td>0.08 (-10.33%)</td><td>0.06 <b>(-38.05%)</b></td><td>0.06 <b>(+232.51%)</b></td><td>0.04 <b>(-22.35%)</b></td><td>582.70 <b>(-69.93%)</b></td><td>477.08 <b>(-29.27%)</b></td><td>519.70 <b>(+61.45%)</b></td><td>219.10 (-8.97%)</td><td>147.46 <b>(-79.59%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1937.50 (n/a)</td><td>674.48 (n/a)</td><td>321.90 (n/a)</td><td>240.70 (n/a)</td><td>722.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 <b>(-41.90%)</b></td><td>0.10 (-14.83%)</td><td>0.13 (+17.51%)</td><td>0.06 (-8.90%)</td><td>0.04 <b>(-44.70%)</b></td><td>519.50 (+9.76%)</td><td>352.40 (+9.28%)</td><td>257.00 (-14.90%)</td><td>245.70 <b>(+72.18%)</b></td><td>139.44 (+0.95%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>473.30 (n/a)</td><td>322.48 (n/a)</td><td>302.00 (n/a)</td><td>142.70 (n/a)</td><td>138.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (+6.13%)</td><td>0.09 (-11.61%)</td><td>0.07 <b>(-33.97%)</b></td><td>0.07 (+0.58%)</td><td>0.03 (+8.57%)</td><td>475.50 (-0.59%)</td><td>392.72 (+14.08%)</td><td>461.90 <b>(+51.44%)</b></td><td>227.00 (-5.77%)</td><td>110.80 (+3.41%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>478.30 (n/a)</td><td>344.24 (n/a)</td><td>305.00 (n/a)</td><td>240.90 (n/a)</td><td>107.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (+11.63%)</td><td>0.12 <b>(+32.75%)</b></td><td>0.12 <b>(+36.62%)</b></td><td>0.08 <b>(+63.78%)</b></td><td>0.02 <b>(-30.30%)</b></td><td>399.50 <b>(-38.94%)</b></td><td>293.84 <b>(-30.77%)</b></td><td>279.50 <b>(-26.79%)</b></td><td>226.60 (-10.43%)</td><td>64.30 <b>(-60.95%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>654.30 (n/a)</td><td>424.44 (n/a)</td><td>381.80 (n/a)</td><td>253.00 (n/a)</td><td>164.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.11 (-15.13%)</td><td>0.09 (+11.13%)</td><td>0.11 <b>(+41.98%)</b></td><td>0.06 (+12.71%)</td><td>0.03 <b>(-20.68%)</b></td><td>532.40 (-11.28%)</td><td>388.70 (-12.89%)</td><td>307.20 <b>(-29.57%)</b></td><td>286.80 (+17.83%)</td><td>122.42 (-16.71%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>600.10 (n/a)</td><td>446.20 (n/a)</td><td>436.20 (n/a)</td><td>243.40 (n/a)</td><td>146.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (-15.26%)</td><td>0.09 (-14.12%)</td><td>0.07 <b>(-35.29%)</b></td><td>0.06 (+10.43%)</td><td>0.03 (-11.45%)</td><td>523.00 (-9.45%)</td><td>405.84 (+15.04%)</td><td>478.20 <b>(+54.56%)</b></td><td>240.00 (+18.05%)</td><td>130.87 (-5.78%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>577.60 (n/a)</td><td>352.78 (n/a)</td><td>309.40 (n/a)</td><td>203.30 (n/a)</td><td>138.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 <b>(-27.31%)</b></td><td>0.06 <b>(-26.38%)</b></td><td>0.06 <b>(-27.87%)</b></td><td>0.04 <b>(-23.06%)</b></td><td>0.02 <b>(-37.42%)</b></td><td>881.50 <b>(+29.98%)</b></td><td>549.16 <b>(+32.57%)</b></td><td>513.20 <b>(+38.63%)</b></td><td>389.40 <b>(+37.55%)</b></td><td>193.38 (+19.55%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>678.20 (n/a)</td><td>414.24 (n/a)</td><td>370.20 (n/a)</td><td>283.10 (n/a)</td><td>161.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (+3.42%)</td><td>0.09 (-1.19%)</td><td>0.07 (-12.48%)</td><td>0.06 (-5.00%)</td><td>0.03 (+14.20%)</td><td>512.10 (+5.26%)</td><td>413.76 (+3.12%)</td><td>475.10 (+14.26%)</td><td>241.80 (-3.32%)</td><td>111.67 (+16.81%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>486.50 (n/a)</td><td>401.26 (n/a)</td><td>415.80 (n/a)</td><td>250.10 (n/a)</td><td>95.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 <b>(-27.24%)</b></td><td>0.07 <b>(-26.92%)</b></td><td>0.06 <b>(-36.86%)</b></td><td>0.05 (-11.50%)</td><td>0.03 <b>(-36.04%)</b></td><td>616.50 (+13.02%)</td><td>504.06 <b>(+30.07%)</b></td><td>557.50 <b>(+58.38%)</b></td><td>282.50 <b>(+37.47%)</b></td><td>130.36 (-10.45%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>545.50 (n/a)</td><td>387.52 (n/a)</td><td>352.00 (n/a)</td><td>205.50 (n/a)</td><td>145.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (-4.04%)</td><td>0.08 (+9.80%)</td><td>0.07 (-0.28%)</td><td>0.06 <b>(+238.91%)</b></td><td>0.03 <b>(-33.84%)</b></td><td>554.40 <b>(-70.49%)</b></td><td>441.42 <b>(-37.45%)</b></td><td>492.00 (+0.29%)</td><td>258.30 (+4.20%)</td><td>115.74 <b>(-82.59%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1878.90 (n/a)</td><td>705.76 (n/a)</td><td>490.60 (n/a)</td><td>247.90 (n/a)</td><td>664.69 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (+8.01%)</td><td>0.01 (+17.58%)</td><td>0.01 <b>(+60.32%)</b></td><td>0.01 (+18.92%)</td><td>0.00 (+8.04%)</td><td>524.40 (-15.91%)</td><td>376.32 (-14.96%)</td><td>301.80 <b>(-37.63%)</b></td><td>252.90 (-7.43%)</td><td>126.94 (-9.01%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>623.60 (n/a)</td><td>442.54 (n/a)</td><td>483.90 (n/a)</td><td>273.20 (n/a)</td><td>139.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (+5.24%)</td><td>0.02 (+5.56%)</td><td>0.02 (+8.66%)</td><td>0.01 (-10.62%)</td><td>0.01 <b>(+30.88%)</b></td><td>637.80 (+11.88%)</td><td>370.82 (+2.91%)</td><td>297.40 (-7.98%)</td><td>202.20 (-4.98%)</td><td>189.86 <b>(+35.22%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.10 (n/a)</td><td>360.34 (n/a)</td><td>323.20 (n/a)</td><td>212.80 (n/a)</td><td>140.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (-12.76%)</td><td>0.01 (-4.62%)</td><td>0.01 (+2.48%)</td><td>0.01 <b>(+52.51%)</b></td><td>0.00 <b>(-29.58%)</b></td><td>532.70 <b>(-34.43%)</b></td><td>380.30 (-6.68%)</td><td>296.80 (-2.40%)</td><td>270.70 (+14.65%)</td><td>128.37 <b>(-46.24%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>812.40 (n/a)</td><td>407.52 (n/a)</td><td>304.10 (n/a)</td><td>236.10 (n/a)</td><td>238.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (-14.75%)</td><td>0.01 <b>(-23.18%)</b></td><td>0.01 <b>(-33.69%)</b></td><td>0.01 (-13.47%)</td><td>0.00 (-18.96%)</td><td>527.80 (+15.57%)</td><td>428.60 <b>(+29.21%)</b></td><td>466.40 <b>(+50.79%)</b></td><td>272.10 (+17.28%)</td><td>106.06 (+9.54%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>456.70 (n/a)</td><td>331.72 (n/a)</td><td>309.30 (n/a)</td><td>232.00 (n/a)</td><td>96.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 <b>(+54.13%)</b></td><td>0.01 (+9.43%)</td><td>0.01 (-17.73%)</td><td>0.00 <b>(-44.75%)</b></td><td>0.01 <b>(+166.39%)</b></td><td>1963.00 <b>(+80.99%)</b></td><td>991.92 <b>(+74.59%)</b></td><td>580.50 <b>(+21.55%)</b></td><td>236.90 <b>(-35.11%)</b></td><td>887.67 <b>(+201.00%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1084.60 (n/a)</td><td>568.14 (n/a)</td><td>477.60 (n/a)</td><td>365.10 (n/a)</td><td>294.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 <b>(+40.20%)</b></td><td>0.01 (+0.13%)</td><td>0.01 (-6.53%)</td><td>0.00 <b>(-74.46%)</b></td><td>0.01 <b>(+137.52%)</b></td><td>2081.90 <b>(+291.56%)</b></td><td>690.44 <b>(+75.44%)</b></td><td>376.20 (+7.00%)</td><td>191.60 <b>(-28.67%)</b></td><td>784.03 <b>(+652.78%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.70 (n/a)</td><td>393.54 (n/a)</td><td>351.60 (n/a)</td><td>268.60 (n/a)</td><td>104.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (-12.60%)</td><td>0.01 <b>(-20.73%)</b></td><td>0.01 <b>(-29.74%)</b></td><td>0.00 <b>(-72.14%)</b></td><td>0.01 <b>(+30.70%)</b></td><td>1907.40 <b>(+258.94%)</b></td><td>662.04 <b>(+91.51%)</b></td><td>427.70 <b>(+42.33%)</b></td><td>261.10 (+14.42%)</td><td>700.83 <b>(+469.27%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.40 (n/a)</td><td>345.70 (n/a)</td><td>300.50 (n/a)</td><td>228.20 (n/a)</td><td>123.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (-1.87%)</td><td>0.01 (+6.10%)</td><td>0.01 (-0.34%)</td><td>0.01 (+5.11%)</td><td>0.00 (+10.02%)</td><td>610.70 (-4.86%)</td><td>455.04 (-4.31%)</td><td>460.90 (+0.35%)</td><td>296.60 (+1.89%)</td><td>144.88 (+8.61%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.90 (n/a)</td><td>475.54 (n/a)</td><td>459.30 (n/a)</td><td>291.10 (n/a)</td><td>133.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (+13.00%)</td><td>0.01 (+0.91%)</td><td>0.01 (+8.35%)</td><td>0.01 (-0.33%)</td><td>0.00 (+15.43%)</td><td>497.30 (+0.34%)</td><td>404.58 (-0.44%)</td><td>418.50 (-7.72%)</td><td>242.10 (-11.51%)</td><td>96.47 (-5.66%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.60 (n/a)</td><td>406.38 (n/a)</td><td>453.50 (n/a)</td><td>273.60 (n/a)</td><td>102.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 <b>(-22.25%)</b></td><td>0.01 (-10.06%)</td><td>0.01 (-1.51%)</td><td>0.01 (+12.83%)</td><td>0.00 <b>(-60.36%)</b></td><td>491.60 (-11.38%)</td><td>424.26 (+2.63%)</td><td>439.30 (+1.53%)</td><td>329.40 <b>(+28.62%)</b></td><td>59.18 <b>(-56.60%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>554.70 (n/a)</td><td>413.38 (n/a)</td><td>432.70 (n/a)</td><td>256.10 (n/a)</td><td>136.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 <b>(+58.30%)</b></td><td>0.01 <b>(+24.21%)</b></td><td>0.01 (-7.98%)</td><td>0.01 (+19.93%)</td><td>0.01 <b>(+113.51%)</b></td><td>517.40 (-16.62%)</td><td>375.64 (-13.96%)</td><td>422.50 (+8.67%)</td><td>203.60 <b>(-36.83%)</b></td><td>130.55 (+9.98%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>620.50 (n/a)</td><td>436.58 (n/a)</td><td>388.80 (n/a)</td><td>322.30 (n/a)</td><td>118.70 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 <b>(+27.65%)</b></td><td>0.03 <b>(+33.06%)</b></td><td>0.03 <b>(+52.79%)</b></td><td>0.02 <b>(+26.01%)</b></td><td>0.01 (+0.05%)</td><td>420.50 <b>(-20.65%)</b></td><td>294.80 <b>(-27.37%)</b></td><td>286.30 <b>(-34.56%)</b></td><td>201.20 <b>(-21.65%)</b></td><td>79.35 <b>(-37.59%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.90 (n/a)</td><td>405.92 (n/a)</td><td>437.50 (n/a)</td><td>256.80 (n/a)</td><td>127.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (+10.71%)</td><td>0.03 (-14.49%)</td><td>0.03 (+4.94%)</td><td>0.01 <b>(-74.79%)</b></td><td>0.02 <b>(+126.91%)</b></td><td>1997.50 <b>(+296.64%)</b></td><td>992.86 <b>(+139.39%)</b></td><td>446.90 (-4.71%)</td><td>243.00 (-9.70%)</td><td>920.04 <b>(+803.63%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.60 (n/a)</td><td>414.74 (n/a)</td><td>469.00 (n/a)</td><td>269.10 (n/a)</td><td>101.82 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (-8.10%)</td><td>0.02 (-8.29%)</td><td>0.02 <b>(-36.07%)</b></td><td>0.01 (+16.74%)</td><td>0.01 (-0.96%)</td><td>569.60 (-14.35%)</td><td>416.68 (+7.38%)</td><td>463.00 <b>(+56.42%)</b></td><td>241.60 (+8.83%)</td><td>163.39 (-11.68%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>665.00 (n/a)</td><td>388.04 (n/a)</td><td>296.00 (n/a)</td><td>222.00 (n/a)</td><td>185.00 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 <b>(-28.16%)</b></td><td>0.02 <b>(-23.85%)</b></td><td>0.02 <b>(-34.45%)</b></td><td>0.02 (+13.65%)</td><td>0.01 <b>(-51.90%)</b></td><td>569.30 (-12.01%)</td><td>463.34 (+15.28%)</td><td>477.80 <b>(+52.55%)</b></td><td>296.00 <b>(+39.23%)</b></td><td>101.68 <b>(-47.07%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>647.00 (n/a)</td><td>401.94 (n/a)</td><td>313.20 (n/a)</td><td>212.60 (n/a)</td><td>192.11 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 <b>(-24.65%)</b></td><td>0.02 (-16.37%)</td><td>0.03 (-7.19%)</td><td>0.01 (-19.18%)</td><td>0.01 <b>(-21.65%)</b></td><td>559.10 <b>(+23.72%)</b></td><td>372.76 (+18.82%)</td><td>273.40 (+7.77%)</td><td>255.30 <b>(+32.69%)</b></td><td>147.35 (+19.12%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>451.90 (n/a)</td><td>313.72 (n/a)</td><td>253.70 (n/a)</td><td>192.40 (n/a)</td><td>123.69 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (+18.44%)</td><td>0.03 (+17.96%)</td><td>0.02 (+16.83%)</td><td>0.02 <b>(+75.06%)</b></td><td>0.01 (+6.33%)</td><td>549.50 <b>(-42.87%)</b></td><td>432.24 <b>(-22.49%)</b></td><td>470.80 (-14.42%)</td><td>202.20 (-15.57%)</td><td>137.91 <b>(-50.19%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>961.90 (n/a)</td><td>557.66 (n/a)</td><td>550.10 (n/a)</td><td>239.50 (n/a)</td><td>276.88 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 <b>(-20.05%)</b></td><td>0.02 <b>(+28.30%)</b></td><td>0.02 <b>(+38.79%)</b></td><td>0.01 <b>(+223.42%)</b></td><td>0.01 <b>(-36.80%)</b></td><td>597.10 <b>(-69.08%)</b></td><td>427.82 <b>(-47.46%)</b></td><td>457.30 <b>(-27.94%)</b></td><td>238.60 <b>(+25.05%)</b></td><td>165.60 <b>(-74.94%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1931.10 (n/a)</td><td>814.26 (n/a)</td><td>634.60 (n/a)</td><td>190.80 (n/a)</td><td>660.73 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 <b>(+25.29%)</b></td><td>0.02 (+19.98%)</td><td>0.02 (+1.33%)</td><td>0.02 <b>(+131.90%)</b></td><td>0.01 (+7.77%)</td><td>578.10 <b>(-56.88%)</b></td><td>496.16 <b>(-25.68%)</b></td><td>545.40 (-1.32%)</td><td>273.30 <b>(-20.18%)</b></td><td>127.64 <b>(-67.02%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1340.60 (n/a)</td><td>667.60 (n/a)</td><td>552.70 (n/a)</td><td>342.40 (n/a)</td><td>387.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 <b>(+42.88%)</b></td><td>0.02 <b>(+45.31%)</b></td><td>0.02 (+3.88%)</td><td>0.01 <b>(+320.39%)</b></td><td>0.01 <b>(+27.26%)</b></td><td>583.70 <b>(-76.21%)</b></td><td>428.18 <b>(-50.47%)</b></td><td>466.60 (-3.73%)</td><td>243.40 <b>(-30.02%)</b></td><td>163.91 <b>(-81.62%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2453.90 (n/a)</td><td>864.42 (n/a)</td><td>484.70 (n/a)</td><td>347.80 (n/a)</td><td>891.69 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (+15.74%)</td><td>0.02 (+9.92%)</td><td>0.02 (+8.76%)</td><td>0.02 (+12.43%)</td><td>0.01 (+13.77%)</td><td>577.30 (-11.06%)</td><td>447.06 (-8.85%)</td><td>483.80 (-8.04%)</td><td>305.60 (-13.60%)</td><td>117.29 (-9.21%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.10 (n/a)</td><td>490.46 (n/a)</td><td>526.10 (n/a)</td><td>353.70 (n/a)</td><td>129.18 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (+4.96%)</td><td>0.02 (+15.09%)</td><td>0.02 <b>(+28.36%)</b></td><td>0.01 (-4.75%)</td><td>0.01 (+16.85%)</td><td>569.50 (+5.00%)</td><td>412.76 (-10.41%)</td><td>389.50 <b>(-22.10%)</b></td><td>252.70 (-4.71%)</td><td>142.36 <b>(+26.51%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.40 (n/a)</td><td>460.74 (n/a)</td><td>500.00 (n/a)</td><td>265.20 (n/a)</td><td>112.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (-11.51%)</td><td>0.05 (-6.56%)</td><td>0.05 (-7.15%)</td><td>0.03 (-3.32%)</td><td>0.02 (+1.60%)</td><td>520.60 (+3.44%)</td><td>372.12 (+9.13%)</td><td>337.00 (+7.70%)</td><td>243.50 (+12.99%)</td><td>128.19 <b>(+21.06%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>503.30 (n/a)</td><td>341.00 (n/a)</td><td>312.90 (n/a)</td><td>215.50 (n/a)</td><td>105.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 <b>(+90.35%)</b></td><td>0.07 <b>(+68.47%)</b></td><td>0.08 <b>(+81.31%)</b></td><td>0.04 <b>(+66.74%)</b></td><td>0.03 <b>(+138.78%)</b></td><td>630.70 <b>(-40.03%)</b></td><td>400.30 <b>(-37.37%)</b></td><td>289.30 <b>(-44.84%)</b></td><td>262.40 <b>(-47.47%)</b></td><td>170.27 <b>(-27.27%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1051.70 (n/a)</td><td>639.16 (n/a)</td><td>524.50 (n/a)</td><td>499.50 (n/a)</td><td>234.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (-6.99%)</td><td>0.04 (-5.11%)</td><td>0.03 (-2.21%)</td><td>0.02 <b>(-24.61%)</b></td><td>0.02 (+5.40%)</td><td>807.40 <b>(+32.64%)</b></td><td>458.64 (+11.47%)</td><td>484.70 (+2.28%)</td><td>254.30 (+7.53%)</td><td>227.34 <b>(+43.74%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>608.70 (n/a)</td><td>411.44 (n/a)</td><td>473.90 (n/a)</td><td>236.50 (n/a)</td><td>158.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (-19.95%)</td><td>0.04 <b>(-25.11%)</b></td><td>0.04 <b>(-35.02%)</b></td><td>0.01 <b>(-70.96%)</b></td><td>0.02 (+11.40%)</td><td>1918.50 <b>(+244.37%)</b></td><td>710.22 <b>(+85.47%)</b></td><td>477.00 <b>(+53.92%)</b></td><td>310.70 <b>(+24.93%)</b></td><td>681.55 <b>(+386.57%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>557.10 (n/a)</td><td>382.94 (n/a)</td><td>309.90 (n/a)</td><td>248.70 (n/a)</td><td>140.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (+3.80%)</td><td>0.05 <b>(+31.69%)</b></td><td>0.06 <b>(+60.84%)</b></td><td>0.03 (+6.57%)</td><td>0.02 (+2.80%)</td><td>571.00 (-6.16%)</td><td>353.60 <b>(-23.85%)</b></td><td>293.00 <b>(-37.83%)</b></td><td>220.90 (-3.71%)</td><td>144.73 (-0.04%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>608.50 (n/a)</td><td>464.32 (n/a)</td><td>471.30 (n/a)</td><td>229.40 (n/a)</td><td>144.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 <b>(+57.12%)</b></td><td>0.07 (+16.22%)</td><td>0.07 <b>(+23.90%)</b></td><td>0.03 (-16.32%)</td><td>0.03 <b>(+174.74%)</b></td><td>591.00 (+19.49%)</td><td>360.92 (-0.17%)</td><td>276.40 (-19.30%)</td><td>176.70 <b>(-36.37%)</b></td><td>170.78 <b>(+110.65%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>494.60 (n/a)</td><td>361.52 (n/a)</td><td>342.50 (n/a)</td><td>277.70 (n/a)</td><td>81.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (-7.57%)</td><td>0.04 (-9.71%)</td><td>0.03 (+6.67%)</td><td>0.02 <b>(-29.49%)</b></td><td>0.01 (-3.40%)</td><td>834.40 <b>(+41.83%)</b></td><td>505.54 (+14.73%)</td><td>471.10 (-6.25%)</td><td>297.00 (+8.16%)</td><td>211.94 <b>(+50.86%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.30 (n/a)</td><td>440.62 (n/a)</td><td>502.50 (n/a)</td><td>274.60 (n/a)</td><td>140.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (+6.45%)</td><td>0.05 <b>(+34.15%)</b></td><td>0.04 (+18.41%)</td><td>0.03 <b>(+255.51%)</b></td><td>0.02 (-15.27%)</td><td>546.90 <b>(-71.87%)</b></td><td>402.06 <b>(-46.90%)</b></td><td>474.80 (-15.56%)</td><td>226.30 (-6.06%)</td><td>138.91 <b>(-79.54%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1944.30 (n/a)</td><td>757.16 (n/a)</td><td>562.30 (n/a)</td><td>240.90 (n/a)</td><td>678.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 <b>(+59.14%)</b></td><td>0.05 <b>(+31.68%)</b></td><td>0.03 (-7.45%)</td><td>0.03 (-1.10%)</td><td>0.02 <b>(+266.83%)</b></td><td>566.30 (+1.11%)</td><td>428.62 (-12.22%)</td><td>538.60 (+8.04%)</td><td>233.10 <b>(-37.15%)</b></td><td>172.50 <b>(+142.34%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>560.10 (n/a)</td><td>488.30 (n/a)</td><td>498.50 (n/a)</td><td>370.90 (n/a)</td><td>71.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (-17.45%)</td><td>0.04 (+11.60%)</td><td>0.03 (-7.70%)</td><td>0.03 <b>(+227.58%)</b></td><td>0.02 <b>(-35.53%)</b></td><td>621.50 <b>(-69.47%)</b></td><td>454.30 <b>(-39.65%)</b></td><td>530.10 (+8.34%)</td><td>275.40 <b>(+21.16%)</b></td><td>151.46 <b>(-79.20%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2036.00 (n/a)</td><td>752.72 (n/a)</td><td>489.30 (n/a)</td><td>227.30 (n/a)</td><td>728.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (-1.54%)</td><td>0.04 (-5.55%)</td><td>0.04 (-0.65%)</td><td>0.03 (-11.42%)</td><td>0.01 (+16.90%)</td><td>588.30 (+12.90%)</td><td>454.26 (+7.75%)</td><td>404.20 (+0.65%)</td><td>335.70 (+1.54%)</td><td>112.47 <b>(+36.81%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>521.10 (n/a)</td><td>421.60 (n/a)</td><td>401.60 (n/a)</td><td>330.60 (n/a)</td><td>82.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.15 <b>(+33.97%)</b></td><td>0.11 <b>(+74.16%)</b></td><td>0.10 <b>(+67.48%)</b></td><td>0.08 <b>(+494.84%)</b></td><td>0.03 <b>(-22.98%)</b></td><td>423.20 <b>(-83.19%)</b></td><td>306.88 <b>(-64.46%)</b></td><td>315.20 <b>(-40.29%)</b></td><td>218.70 <b>(-25.36%)</b></td><td>76.89 <b>(-91.73%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2517.30 (n/a)</td><td>863.54 (n/a)</td><td>527.90 (n/a)</td><td>293.00 (n/a)</td><td>929.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (-14.94%)</td><td>0.07 <b>(-31.29%)</b></td><td>0.07 <b>(-36.51%)</b></td><td>0.05 (-9.27%)</td><td>0.03 (-9.56%)</td><td>635.50 (+10.22%)</td><td>488.26 <b>(+45.07%)</b></td><td>489.40 <b>(+57.52%)</b></td><td>248.30 (+17.57%)</td><td>147.99 (+4.65%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>576.60 (n/a)</td><td>336.56 (n/a)</td><td>310.70 (n/a)</td><td>211.20 (n/a)</td><td>141.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 <b>(-33.06%)</b></td><td>0.07 <b>(-45.50%)</b></td><td>0.08 <b>(-40.43%)</b></td><td>0.02 <b>(-68.08%)</b></td><td>0.05 (-12.73%)</td><td>1878.30 <b>(+213.31%)</b></td><td>996.88 <b>(+169.47%)</b></td><td>521.40 <b>(+67.87%)</b></td><td>305.90 <b>(+49.37%)</b></td><td>805.91 <b>(+370.40%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>599.50 (n/a)</td><td>369.94 (n/a)</td><td>310.60 (n/a)</td><td>204.80 (n/a)</td><td>171.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (-15.43%)</td><td>0.08 (-12.66%)</td><td>0.06 (-11.16%)</td><td>0.05 (-18.19%)</td><td>0.03 (-10.12%)</td><td>722.10 <b>(+22.22%)</b></td><td>478.54 (+16.24%)</td><td>514.60 (+12.55%)</td><td>280.40 (+18.26%)</td><td>178.25 <b>(+28.32%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>590.80 (n/a)</td><td>411.68 (n/a)</td><td>457.20 (n/a)</td><td>237.10 (n/a)</td><td>138.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.16 (-6.26%)</td><td>0.12 (+14.63%)</td><td>0.13 <b>(+75.36%)</b></td><td>0.06 <b>(+56.83%)</b></td><td>0.05 <b>(-23.41%)</b></td><td>665.50 <b>(-36.24%)</b></td><td>396.84 <b>(-25.05%)</b></td><td>307.60 <b>(-42.97%)</b></td><td>252.90 (+6.66%)</td><td>180.51 <b>(-44.81%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>1043.70 (n/a)</td><td>529.48 (n/a)</td><td>539.40 (n/a)</td><td>237.10 (n/a)</td><td>327.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.15 <b>(+31.57%)</b></td><td>0.09 (+13.47%)</td><td>0.07 (-4.60%)</td><td>0.06 (+19.53%)</td><td>0.03 <b>(+44.92%)</b></td><td>528.10 (-16.35%)</td><td>422.98 (-10.35%)</td><td>449.40 (+4.83%)</td><td>225.30 <b>(-23.99%)</b></td><td>118.59 (-15.57%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>631.30 (n/a)</td><td>471.82 (n/a)</td><td>428.70 (n/a)</td><td>296.40 (n/a)</td><td>140.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.16 <b>(+42.90%)</b></td><td>0.09 <b>(+21.09%)</b></td><td>0.08 (-4.12%)</td><td>0.04 (+5.58%)</td><td>0.05 <b>(+87.74%)</b></td><td>952.30 (-5.29%)</td><td>501.38 (-7.52%)</td><td>476.00 (+4.29%)</td><td>236.60 <b>(-30.02%)</b></td><td>286.56 (+8.55%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>1005.50 (n/a)</td><td>542.14 (n/a)</td><td>456.40 (n/a)</td><td>338.10 (n/a)</td><td>264.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 <b>(-38.77%)</b></td><td>0.06 <b>(-30.97%)</b></td><td>0.07 (+1.12%)</td><td>0.02 <b>(-72.81%)</b></td><td>0.02 (-17.27%)</td><td>2014.40 <b>(+267.73%)</b></td><td>789.76 <b>(+85.06%)</b></td><td>501.30 (-1.10%)</td><td>439.10 <b>(+63.29%)</b></td><td>685.92 <b>(+426.29%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>547.80 (n/a)</td><td>426.76 (n/a)</td><td>506.90 (n/a)</td><td>268.90 (n/a)</td><td>130.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 <b>(+75.14%)</b></td><td>0.09 <b>(+32.85%)</b></td><td>0.10 <b>(+48.12%)</b></td><td>0.02 <b>(-67.31%)</b></td><td>0.05 <b>(+483.03%)</b></td><td>1908.00 <b>(+205.92%)</b></td><td>662.62 <b>(+22.74%)</b></td><td>374.10 <b>(-32.49%)</b></td><td>271.30 <b>(-42.90%)</b></td><td>700.39 <b>(+1021.94%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>623.70 (n/a)</td><td>539.84 (n/a)</td><td>554.10 (n/a)</td><td>475.10 (n/a)</td><td>62.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 <b>(-46.08%)</b></td><td>0.07 (-17.21%)</td><td>0.07 <b>(+22.21%)</b></td><td>0.04 <b>(-24.54%)</b></td><td>0.02 <b>(-61.94%)</b></td><td>815.80 <b>(+32.52%)</b></td><td>526.60 (+6.76%)</td><td>464.60 (-18.18%)</td><td>345.90 <b>(+85.47%)</b></td><td>179.08 (+0.25%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>615.60 (n/a)</td><td>493.24 (n/a)</td><td>567.80 (n/a)</td><td>186.50 (n/a)</td><td>178.64 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (-12.37%)</td><td>0.05 (-8.42%)</td><td>0.05 (-9.64%)</td><td>0.04 (-9.03%)</td><td>0.02 (-1.21%)</td><td>573.20 (+9.93%)</td><td>413.82 (+10.84%)</td><td>411.30 (+10.65%)</td><td>275.90 (+14.10%)</td><td>131.81 <b>(+22.06%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>521.40 (n/a)</td><td>373.36 (n/a)</td><td>371.70 (n/a)</td><td>241.80 (n/a)</td><td>107.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (+10.90%)</td><td>0.07 (+1.52%)</td><td>0.07 (-3.49%)</td><td>0.04 (+7.98%)</td><td>0.02 (+10.54%)</td><td>468.00 (-7.38%)</td><td>303.56 (-1.71%)</td><td>282.10 (+3.64%)</td><td>215.00 (-9.85%)</td><td>99.21 (-10.39%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>505.30 (n/a)</td><td>308.84 (n/a)</td><td>272.20 (n/a)</td><td>238.50 (n/a)</td><td>110.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (-14.18%)</td><td>0.05 (+18.09%)</td><td>0.05 <b>(+20.75%)</b></td><td>0.04 <b>(+331.13%)</b></td><td>0.02 <b>(-46.28%)</b></td><td>567.20 <b>(-76.80%)</b></td><td>432.24 <b>(-49.51%)</b></td><td>433.00 (-17.18%)</td><td>262.80 (+16.54%)</td><td>110.61 <b>(-87.70%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2445.20 (n/a)</td><td>856.12 (n/a)</td><td>522.80 (n/a)</td><td>225.50 (n/a)</td><td>898.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (+10.47%)</td><td>0.05 (-12.55%)</td><td>0.04 (-6.17%)</td><td>0.03 (+4.60%)</td><td>0.03 (+0.06%)</td><td>588.70 (-4.39%)</td><td>478.16 (+11.01%)</td><td>526.00 (+6.59%)</td><td>196.90 (-9.47%)</td><td>160.11 (-16.48%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>615.70 (n/a)</td><td>430.72 (n/a)</td><td>493.50 (n/a)</td><td>217.50 (n/a)</td><td>191.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (+5.95%)</td><td>0.05 (-18.69%)</td><td>0.04 <b>(-34.27%)</b></td><td>0.03 (-17.45%)</td><td>0.02 <b>(+33.95%)</b></td><td>603.00 <b>(+21.16%)</b></td><td>464.40 <b>(+29.81%)</b></td><td>498.60 <b>(+52.15%)</b></td><td>227.70 (-5.64%)</td><td>143.62 <b>(+41.29%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>497.70 (n/a)</td><td>357.76 (n/a)</td><td>327.70 (n/a)</td><td>241.30 (n/a)</td><td>101.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 <b>(+55.79%)</b></td><td>0.05 <b>(+26.97%)</b></td><td>0.04 (+15.26%)</td><td>0.04 <b>(+21.64%)</b></td><td>0.02 <b>(+124.18%)</b></td><td>482.80 (-17.79%)</td><td>409.02 (-17.48%)</td><td>463.10 (-13.24%)</td><td>230.60 <b>(-35.80%)</b></td><td>104.02 (+17.39%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>587.30 (n/a)</td><td>495.64 (n/a)</td><td>533.80 (n/a)</td><td>359.20 (n/a)</td><td>88.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 <b>(-32.05%)</b></td><td>0.07 (-10.14%)</td><td>0.08 <b>(+69.66%)</b></td><td>0.01 <b>(-67.55%)</b></td><td>0.03 (-14.60%)</td><td>1931.50 <b>(+208.20%)</b></td><td>658.20 <b>(+58.27%)</b></td><td>290.50 <b>(-41.06%)</b></td><td>261.70 <b>(+47.19%)</b></td><td>720.29 <b>(+298.20%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>626.70 (n/a)</td><td>415.86 (n/a)</td><td>492.90 (n/a)</td><td>177.80 (n/a)</td><td>180.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (-13.83%)</td><td>0.08 (-1.46%)</td><td>0.08 (-3.69%)</td><td>0.06 <b>(+20.67%)</b></td><td>0.01 <b>(-51.16%)</b></td><td>420.30 (-17.13%)</td><td>315.26 (-6.94%)</td><td>292.70 (+3.83%)</td><td>256.00 (+16.05%)</td><td>63.36 <b>(-51.84%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>507.20 (n/a)</td><td>338.76 (n/a)</td><td>281.90 (n/a)</td><td>220.60 (n/a)</td><td>131.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (-13.74%)</td><td>0.06 (-16.41%)</td><td>0.05 (-17.82%)</td><td>0.05 <b>(+21.23%)</b></td><td>0.02 <b>(-27.74%)</b></td><td>517.80 (-17.51%)</td><td>427.54 (+12.35%)</td><td>455.20 <b>(+21.68%)</b></td><td>251.60 (+15.94%)</td><td>103.43 <b>(-34.46%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>627.70 (n/a)</td><td>380.54 (n/a)</td><td>374.10 (n/a)</td><td>217.00 (n/a)</td><td>157.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 <b>(+27.78%)</b></td><td>0.05 (+5.76%)</td><td>0.06 (+10.70%)</td><td>0.01 <b>(-66.80%)</b></td><td>0.03 <b>(+86.43%)</b></td><td>2453.50 <b>(+201.19%)</b></td><td>806.28 <b>(+54.47%)</b></td><td>435.40 (-9.67%)</td><td>275.60 <b>(-21.73%)</b></td><td>924.29 <b>(+406.55%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>814.60 (n/a)</td><td>521.96 (n/a)</td><td>482.00 (n/a)</td><td>352.10 (n/a)</td><td>182.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 <b>(-41.26%)</b></td><td>0.05 <b>(-29.75%)</b></td><td>0.05 (-17.42%)</td><td>0.04 (-7.60%)</td><td>0.01 <b>(-75.22%)</b></td><td>572.80 (+8.22%)</td><td>482.34 <b>(+27.04%)</b></td><td>464.00 <b>(+21.09%)</b></td><td>394.40 <b>(+70.22%)</b></td><td>67.79 <b>(-53.37%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>529.30 (n/a)</td><td>379.68 (n/a)</td><td>383.20 (n/a)</td><td>231.70 (n/a)</td><td>145.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 <b>(-24.72%)</b></td><td>0.05 (-16.99%)</td><td>0.06 <b>(+25.63%)</b></td><td>0.01 <b>(-68.64%)</b></td><td>0.02 (-13.17%)</td><td>1868.30 <b>(+218.88%)</b></td><td>700.34 <b>(+55.68%)</b></td><td>432.80 <b>(-20.40%)</b></td><td>320.80 <b>(+32.84%)</b></td><td>656.65 <b>(+291.17%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>585.90 (n/a)</td><td>449.86 (n/a)</td><td>543.70 (n/a)</td><td>241.50 (n/a)</td><td>167.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (-4.32%)</td><td>0.06 (+17.97%)</td><td>0.06 <b>(+38.98%)</b></td><td>0.03 (-1.84%)</td><td>0.02 (-8.73%)</td><td>601.70 (+1.88%)</td><td>348.72 (-16.23%)</td><td>307.40 <b>(-28.04%)</b></td><td>246.50 (+4.49%)</td><td>146.70 (-1.76%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.60 (n/a)</td><td>416.28 (n/a)</td><td>427.20 (n/a)</td><td>235.90 (n/a)</td><td>149.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 <b>(-34.50%)</b></td><td>0.05 (-5.22%)</td><td>0.05 (+12.47%)</td><td>0.03 (-1.05%)</td><td>0.02 <b>(-47.66%)</b></td><td>561.70 (+1.06%)</td><td>392.74 (-4.27%)</td><td>395.00 (-11.08%)</td><td>246.80 <b>(+52.72%)</b></td><td>130.20 (-11.59%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>555.80 (n/a)</td><td>410.24 (n/a)</td><td>444.20 (n/a)</td><td>161.60 (n/a)</td><td>147.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (+12.82%)</td><td>0.05 (-18.27%)</td><td>0.04 <b>(-38.89%)</b></td><td>0.03 (-19.36%)</td><td>0.02 <b>(+48.35%)</b></td><td>596.00 <b>(+24.01%)</b></td><td>405.88 <b>(+32.58%)</b></td><td>429.30 <b>(+63.61%)</b></td><td>215.80 (-11.34%)</td><td>160.04 <b>(+59.66%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>480.60 (n/a)</td><td>306.14 (n/a)</td><td>262.40 (n/a)</td><td>243.40 (n/a)</td><td>100.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (-14.53%)</td><td>0.05 <b>(+28.71%)</b></td><td>0.04 <b>(+36.07%)</b></td><td>0.03 <b>(+211.16%)</b></td><td>0.02 <b>(-36.88%)</b></td><td>604.40 <b>(-67.86%)</b></td><td>409.28 <b>(-52.85%)</b></td><td>452.70 <b>(-26.52%)</b></td><td>252.30 (+16.97%)</td><td>153.27 <b>(-78.44%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1880.60 (n/a)</td><td>867.98 (n/a)</td><td>616.10 (n/a)</td><td>215.70 (n/a)</td><td>710.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (-8.01%)</td><td>0.05 (-13.65%)</td><td>0.04 <b>(-29.90%)</b></td><td>0.03 (-2.45%)</td><td>0.02 (-18.99%)</td><td>603.70 (+2.51%)</td><td>423.36 (+12.42%)</td><td>449.20 <b>(+42.65%)</b></td><td>274.00 (+8.69%)</td><td>134.80 (-9.57%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.90 (n/a)</td><td>376.60 (n/a)</td><td>314.90 (n/a)</td><td>252.10 (n/a)</td><td>149.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (+10.99%)</td><td>0.04 (+2.24%)</td><td>0.04 (-2.19%)</td><td>0.03 (+6.60%)</td><td>0.02 (+7.44%)</td><td>609.80 (-6.20%)</td><td>450.44 (-2.79%)</td><td>479.60 (+2.24%)</td><td>262.60 (-9.91%)</td><td>127.19 (-12.86%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>650.10 (n/a)</td><td>463.38 (n/a)</td><td>469.10 (n/a)</td><td>291.50 (n/a)</td><td>145.96 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.34 (-10.93%)</td><td>0.30 (-10.30%)</td><td>0.31 (-4.90%)</td><td>0.19 <b>(-35.52%)</b></td><td>0.06 <b>(+80.48%)</b></td><td>524.00 <b>(+55.08%)</b></td><td>346.42 (+16.17%)</td><td>312.50 (+5.15%)</td><td>287.40 (+12.27%)</td><td>99.97 <b>(+225.64%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.04 (n/a)</td><td>337.90 (n/a)</td><td>298.20 (n/a)</td><td>297.20 (n/a)</td><td>256.00 (n/a)</td><td>30.70 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.40 (+4.23%)</td><td>0.25 (-16.92%)</td><td>0.22 <b>(-29.39%)</b></td><td>0.20 (-3.38%)</td><td>0.08 (+14.38%)</td><td>482.90 (+3.52%)</td><td>411.36 <b>(+21.86%)</b></td><td>446.00 <b>(+41.63%)</b></td><td>245.60 (-4.06%)</td><td>94.61 (+9.20%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>466.50 (n/a)</td><td>337.58 (n/a)</td><td>314.90 (n/a)</td><td>256.00 (n/a)</td><td>86.64 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.37 <b>(+62.37%)</b></td><td>0.26 <b>(+59.41%)</b></td><td>0.31 <b>(+78.06%)</b></td><td>0.16 <b>(+206.09%)</b></td><td>0.09 <b>(+29.11%)</b></td><td>626.30 <b>(-67.33%)</b></td><td>415.78 <b>(-47.93%)</b></td><td>319.20 <b>(-43.84%)</b></td><td>264.80 <b>(-38.42%)</b></td><td>161.82 <b>(-74.38%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>1917.10 (n/a)</td><td>798.46 (n/a)</td><td>568.40 (n/a)</td><td>430.00 (n/a)</td><td>631.49 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.33 <b>(+27.91%)</b></td><td>0.20 (+15.54%)</td><td>0.19 <b>(+32.54%)</b></td><td>0.12 <b>(+25.42%)</b></td><td>0.09 <b>(+20.31%)</b></td><td>619.30 <b>(-20.27%)</b></td><td>428.32 (-13.30%)</td><td>388.00 <b>(-24.56%)</b></td><td>224.50 <b>(-21.83%)</b></td><td>173.35 (-15.08%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>776.70 (n/a)</td><td>494.04 (n/a)</td><td>514.30 (n/a)</td><td>287.20 (n/a)</td><td>204.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.31 (-0.28%)</td><td>0.18 (-5.82%)</td><td>0.16 (+7.93%)</td><td>0.03 <b>(-67.24%)</b></td><td>0.12 <b>(+25.21%)</b></td><td>2473.40 <b>(+205.21%)</b></td><td>809.06 <b>(+73.31%)</b></td><td>465.10 (-7.35%)</td><td>236.70 (+0.30%)</td><td>943.73 <b>(+307.40%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.31 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>810.40 (n/a)</td><td>466.84 (n/a)</td><td>502.00 (n/a)</td><td>236.00 (n/a)</td><td>231.65 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.33 <b>(+39.15%)</b></td><td>0.20 (+8.53%)</td><td>0.17 (+9.02%)</td><td>0.11 <b>(-30.44%)</b></td><td>0.10 <b>(+150.09%)</b></td><td>684.60 <b>(+43.76%)</b></td><td>447.56 (+10.35%)</td><td>422.50 (-8.27%)</td><td>221.20 <b>(-28.11%)</b></td><td>219.79 <b>(+163.69%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>476.20 (n/a)</td><td>405.60 (n/a)</td><td>460.60 (n/a)</td><td>307.70 (n/a)</td><td>83.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.16 (+3.28%)</td><td>0.09 <b>(-37.40%)</b></td><td>0.07 <b>(-49.38%)</b></td><td>0.06 <b>(-48.70%)</b></td><td>0.04 <b>(+164.32%)</b></td><td>628.60 <b>(+94.91%)</b></td><td>487.80 <b>(+81.06%)</b></td><td>510.90 <b>(+97.56%)</b></td><td>224.90 (-3.19%)</td><td>158.87 <b>(+365.67%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>322.50 (n/a)</td><td>269.42 (n/a)</td><td>258.60 (n/a)</td><td>232.30 (n/a)</td><td>34.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 <b>(-23.29%)</b></td><td>0.12 (-5.00%)</td><td>0.12 (-10.86%)</td><td>0.08 <b>(+28.01%)</b></td><td>0.02 <b>(-53.90%)</b></td><td>443.30 <b>(-21.87%)</b></td><td>324.90 (-4.28%)</td><td>304.30 (+12.16%)</td><td>266.40 <b>(+30.33%)</b></td><td>68.60 <b>(-52.36%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>567.40 (n/a)</td><td>339.42 (n/a)</td><td>271.30 (n/a)</td><td>204.40 (n/a)</td><td>144.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.20 <b>(+30.21%)</b></td><td>0.11 <b>(+36.15%)</b></td><td>0.08 <b>(+28.06%)</b></td><td>0.07 <b>(+30.74%)</b></td><td>0.05 <b>(+27.93%)</b></td><td>509.10 <b>(-23.51%)</b></td><td>396.30 <b>(-26.73%)</b></td><td>468.60 <b>(-21.91%)</b></td><td>187.20 <b>(-23.18%)</b></td><td>133.10 <b>(-21.86%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>665.60 (n/a)</td><td>540.84 (n/a)</td><td>600.10 (n/a)</td><td>243.70 (n/a)</td><td>170.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.15 <b>(+22.52%)</b></td><td>0.09 (+13.41%)</td><td>0.08 (+15.32%)</td><td>0.04 (-10.19%)</td><td>0.04 <b>(+42.55%)</b></td><td>826.90 (+11.35%)</td><td>489.18 (-5.96%)</td><td>437.20 (-13.27%)</td><td>246.60 (-18.37%)</td><td>211.42 <b>(+34.76%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>742.60 (n/a)</td><td>520.16 (n/a)</td><td>504.10 (n/a)</td><td>302.10 (n/a)</td><td>156.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.11 <b>(-32.57%)</b></td><td>0.08 (-10.54%)</td><td>0.08 (-3.40%)</td><td>0.07 (+14.91%)</td><td>0.02 <b>(-58.63%)</b></td><td>555.70 (-12.97%)</td><td>461.74 (+3.22%)</td><td>472.30 (+3.53%)</td><td>351.10 <b>(+48.33%)</b></td><td>82.21 <b>(-43.43%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>638.50 (n/a)</td><td>447.34 (n/a)</td><td>456.20 (n/a)</td><td>236.70 (n/a)</td><td>145.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (-4.54%)</td><td>0.09 (+5.78%)</td><td>0.08 (+17.19%)</td><td>0.06 <b>(+308.66%)</b></td><td>0.03 <b>(-44.45%)</b></td><td>612.70 <b>(-75.53%)</b></td><td>459.18 <b>(-45.71%)</b></td><td>464.10 (-14.66%)</td><td>273.20 (+4.75%)</td><td>122.48 <b>(-86.97%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2503.90 (n/a)</td><td>845.80 (n/a)</td><td>543.80 (n/a)</td><td>260.80 (n/a)</td><td>939.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.17 (-16.43%)</td><td>0.10 <b>(-34.63%)</b></td><td>0.09 <b>(-43.94%)</b></td><td>0.07 (-19.06%)</td><td>0.04 (-6.30%)</td><td>567.30 <b>(+23.54%)</b></td><td>441.58 <b>(+54.34%)</b></td><td>463.70 <b>(+78.35%)</b></td><td>244.80 (+19.65%)</td><td>119.21 (+19.79%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>459.20 (n/a)</td><td>286.10 (n/a)</td><td>260.00 (n/a)</td><td>204.60 (n/a)</td><td>99.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 <b>(-34.05%)</b></td><td>0.08 <b>(-21.84%)</b></td><td>0.08 <b>(-38.45%)</b></td><td>0.06 <b>(+237.30%)</b></td><td>0.02 <b>(-69.47%)</b></td><td>717.60 <b>(-70.35%)</b></td><td>517.74 <b>(-31.42%)</b></td><td>503.30 <b>(+62.46%)</b></td><td>407.20 <b>(+51.60%)</b></td><td>122.39 <b>(-86.91%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2420.60 (n/a)</td><td>754.92 (n/a)</td><td>309.80 (n/a)</td><td>268.60 (n/a)</td><td>934.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.18 <b>(+112.05%)</b></td><td>0.11 <b>(+47.04%)</b></td><td>0.09 (+18.12%)</td><td>0.07 <b>(+22.01%)</b></td><td>0.04 <b>(+370.83%)</b></td><td>556.60 (-18.04%)</td><td>412.26 <b>(-25.66%)</b></td><td>445.60 (-15.35%)</td><td>229.60 <b>(-52.83%)</b></td><td>132.25 <b>(+76.64%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>679.10 (n/a)</td><td>554.54 (n/a)</td><td>526.40 (n/a)</td><td>486.80 (n/a)</td><td>74.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.16 (-3.90%)</td><td>0.14 <b>(+30.81%)</b></td><td>0.15 <b>(+81.60%)</b></td><td>0.09 <b>(+26.18%)</b></td><td>0.03 <b>(-36.66%)</b></td><td>435.60 <b>(-20.74%)</b></td><td>304.58 <b>(-29.09%)</b></td><td>281.10 <b>(-44.93%)</b></td><td>251.50 (+4.05%)</td><td>75.21 <b>(-48.27%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>549.60 (n/a)</td><td>429.54 (n/a)</td><td>510.40 (n/a)</td><td>241.70 (n/a)</td><td>145.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.16 (+7.95%)</td><td>0.11 (+1.80%)</td><td>0.13 <b>(+30.25%)</b></td><td>0.06 (-7.87%)</td><td>0.04 <b>(+27.37%)</b></td><td>657.60 (+8.53%)</td><td>430.04 (+4.81%)</td><td>310.80 <b>(-23.24%)</b></td><td>258.00 (-7.36%)</td><td>191.41 <b>(+41.32%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>605.90 (n/a)</td><td>410.30 (n/a)</td><td>404.90 (n/a)</td><td>278.50 (n/a)</td><td>135.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.18 <b>(+33.31%)</b></td><td>0.13 <b>(+78.92%)</b></td><td>0.15 <b>(+93.17%)</b></td><td>0.07 <b>(+240.32%)</b></td><td>0.05 (+17.09%)</td><td>568.30 <b>(-70.62%)</b></td><td>349.74 <b>(-55.93%)</b></td><td>281.90 <b>(-48.25%)</b></td><td>223.20 <b>(-24.97%)</b></td><td>149.11 <b>(-77.09%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1934.20 (n/a)</td><td>793.58 (n/a)</td><td>544.70 (n/a)</td><td>297.50 (n/a)</td><td>650.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 <b>(-23.94%)</b></td><td>0.09 (-13.45%)</td><td>0.06 <b>(-32.91%)</b></td><td>0.06 <b>(+214.96%)</b></td><td>0.03 <b>(-39.59%)</b></td><td>608.90 <b>(-68.25%)</b></td><td>455.32 <b>(-28.20%)</b></td><td>538.10 <b>(+49.06%)</b></td><td>285.20 <b>(+31.49%)</b></td><td>156.03 <b>(-78.39%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1917.90 (n/a)</td><td>634.18 (n/a)</td><td>361.00 (n/a)</td><td>216.90 (n/a)</td><td>722.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (+4.43%)</td><td>0.09 (+1.24%)</td><td>0.08 (-12.92%)</td><td>0.06 (+5.02%)</td><td>0.03 (-5.02%)</td><td>607.00 (-4.77%)</td><td>422.64 (-3.57%)</td><td>451.60 (+14.85%)</td><td>254.80 (-4.25%)</td><td>132.16 (-17.65%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>637.40 (n/a)</td><td>438.28 (n/a)</td><td>393.20 (n/a)</td><td>266.10 (n/a)</td><td>160.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 <b>(+21.76%)</b></td><td>0.10 (+14.24%)</td><td>0.08 (+12.97%)</td><td>0.07 (-3.47%)</td><td>0.03 <b>(+72.50%)</b></td><td>501.70 (+3.59%)</td><td>382.36 (-8.98%)</td><td>412.20 (-11.47%)</td><td>264.80 (-17.89%)</td><td>106.52 <b>(+39.88%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>484.30 (n/a)</td><td>420.10 (n/a)</td><td>465.60 (n/a)</td><td>322.50 (n/a)</td><td>76.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (+4.22%)</td><td>0.10 (+14.87%)</td><td>0.12 <b>(+65.03%)</b></td><td>0.06 (+2.96%)</td><td>0.03 (+4.55%)</td><td>539.90 (-2.88%)</td><td>369.58 (-12.51%)</td><td>297.30 <b>(-39.40%)</b></td><td>241.70 (-4.05%)</td><td>132.74 (+0.99%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>555.90 (n/a)</td><td>422.44 (n/a)</td><td>490.60 (n/a)</td><td>251.90 (n/a)</td><td>131.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 <b>(-50.00%)</b></td><td>0.06 <b>(-35.47%)</b></td><td>0.06 <b>(-22.06%)</b></td><td>0.05 (-19.21%)</td><td>0.01 <b>(-71.54%)</b></td><td>763.80 <b>(+23.77%)</b></td><td>605.38 <b>(+43.27%)</b></td><td>574.10 <b>(+28.32%)</b></td><td>491.80 <b>(+100.00%)</b></td><td>104.29 <b>(-27.14%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>617.10 (n/a)</td><td>422.54 (n/a)</td><td>447.40 (n/a)</td><td>245.90 (n/a)</td><td>143.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (+1.55%)</td><td>0.09 (+4.67%)</td><td>0.08 (-0.85%)</td><td>0.06 <b>(+88.76%)</b></td><td>0.02 <b>(-27.39%)</b></td><td>547.10 <b>(-47.02%)</b></td><td>429.38 (-16.51%)</td><td>449.70 (+0.87%)</td><td>298.60 (-1.52%)</td><td>113.38 <b>(-62.26%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1032.70 (n/a)</td><td>514.26 (n/a)</td><td>445.80 (n/a)</td><td>303.20 (n/a)</td><td>300.42 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.47 (-4.41%)</td><td>0.32 (-8.26%)</td><td>0.31 (-3.54%)</td><td>0.17 (-17.49%)</td><td>0.14 (+9.45%)</td><td>761.30 <b>(+21.21%)</b></td><td>480.06 (+15.08%)</td><td>429.50 (+3.67%)</td><td>280.80 (+4.62%)</td><td>215.62 <b>(+40.94%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.49 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>628.10 (n/a)</td><td>417.16 (n/a)</td><td>414.30 (n/a)</td><td>268.40 (n/a)</td><td>152.98 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.53 <b>(+34.43%)</b></td><td>0.32 (+1.22%)</td><td>0.28 (-11.98%)</td><td>0.20 (-16.33%)</td><td>0.13 <b>(+117.78%)</b></td><td>663.80 (+19.52%)</td><td>464.96 (+7.64%)</td><td>472.50 (+13.61%)</td><td>247.90 <b>(-25.60%)</b></td><td>161.09 <b>(+88.48%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>555.40 (n/a)</td><td>431.96 (n/a)</td><td>415.90 (n/a)</td><td>333.20 (n/a)</td><td>85.47 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.39 <b>(-26.43%)</b></td><td>0.26 <b>(-33.79%)</b></td><td>0.27 <b>(-26.12%)</b></td><td>0.05 <b>(-79.46%)</b></td><td>0.13 <b>(+22.75%)</b></td><td>2399.60 <b>(+386.73%)</b></td><td>826.30 <b>(+133.99%)</b></td><td>483.90 <b>(+35.36%)</b></td><td>339.20 <b>(+35.95%)</b></td><td>882.52 <b>(+821.22%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.53 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>493.00 (n/a)</td><td>353.14 (n/a)</td><td>357.50 (n/a)</td><td>249.50 (n/a)</td><td>95.80 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-29.17%)</b></td><td>0.00 <b>(-66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-24.69%)</b></td><td>21614.17 (+3.39%)</td><td>15170.68 <b>(+27.53%)</b></td><td>18604.87 <b>(+152.94%)</b></td><td>6677.20 (+8.94%)</td><td>7099.56 (-3.44%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20906.15 (n/a)</td><td>11896.23 (n/a)</td><td>7355.38 (n/a)</td><td>6128.98 (n/a)</td><td>7352.77 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+20.59%)</b></td><td>0.00 <b>(+60.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>19454.85 (-14.96%)</td><td>12321.45 <b>(-21.20%)</b></td><td>10536.64 <b>(-37.28%)</b></td><td>6217.35 (-2.41%)</td><td>6068.12 (-18.45%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22877.59 (n/a)</td><td>15636.08 (n/a)</td><td>16800.66 (n/a)</td><td>6370.63 (n/a)</td><td>7441.22 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (-12.06%)</td><td>0.09 (-15.65%)</td><td>0.08 <b>(-26.35%)</b></td><td>0.07 (+7.11%)</td><td>0.02 <b>(-24.65%)</b></td><td>29004.66 (-6.63%)</td><td>24660.91 (+14.77%)</td><td>26060.24 <b>(+35.84%)</b></td><td>15885.92 (+13.73%)</td><td>5246.76 <b>(-23.64%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>31065.28 (n/a)</td><td>21487.67 (n/a)</td><td>19184.60 (n/a)</td><td>13967.92 (n/a)</td><td>6870.78 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>2.27 (+10.46%)</td><td>1.73 (+5.34%)</td><td>1.66 (-1.44%)</td><td>1.04 <b>(-20.20%)</b></td><td>0.48 <b>(+44.11%)</b></td><td>1005.70 <b>(+25.31%)</b></td><td>651.56 (-1.17%)</td><td>631.50 (+1.46%)</td><td>461.60 (-9.47%)</td><td>215.45 <b>(+58.31%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>2.06 (n/a)</td><td>1.65 (n/a)</td><td>1.68 (n/a)</td><td>1.31 (n/a)</td><td>0.34 (n/a)</td><td>802.60 (n/a)</td><td>659.30 (n/a)</td><td>622.40 (n/a)</td><td>509.90 (n/a)</td><td>136.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>2.72 (-5.32%)</td><td>1.79 (-2.96%)</td><td>1.83 (+9.94%)</td><td>1.17 (+0.84%)</td><td>0.64 (+0.92%)</td><td>893.10 (-0.83%)</td><td>648.00 (+4.66%)</td><td>572.10 (-9.05%)</td><td>385.80 (+5.61%)</td><td>222.03 (+15.50%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>2.87 (n/a)</td><td>1.84 (n/a)</td><td>1.67 (n/a)</td><td>1.16 (n/a)</td><td>0.63 (n/a)</td><td>900.60 (n/a)</td><td>619.16 (n/a)</td><td>629.00 (n/a)</td><td>365.30 (n/a)</td><td>192.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>2.25 <b>(-36.77%)</b></td><td>1.45 <b>(-34.23%)</b></td><td>1.44 (-19.88%)</td><td>0.30 <b>(-78.24%)</b></td><td>0.75 (-15.27%)</td><td>3480.30 <b>(+359.69%)</b></td><td>1201.70 <b>(+126.06%)</b></td><td>728.10 <b>(+24.80%)</b></td><td>465.10 <b>(+58.14%)</b></td><td>1281.05 <b>(+597.08%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>3.57 (n/a)</td><td>2.21 (n/a)</td><td>1.80 (n/a)</td><td>1.38 (n/a)</td><td>0.88 (n/a)</td><td>757.10 (n/a)</td><td>531.58 (n/a)</td><td>583.40 (n/a)</td><td>294.10 (n/a)</td><td>183.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.20 (-4.35%)</td><td>2.02 (+1.57%)</td><td>2.01 (+13.57%)</td><td>1.35 (+14.36%)</td><td>0.74 (-9.77%)</td><td>777.00 (-12.55%)</td><td>569.10 (-3.57%)</td><td>522.10 (-11.96%)</td><td>327.30 (+4.54%)</td><td>180.13 (-12.93%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.35 (n/a)</td><td>1.99 (n/a)</td><td>1.77 (n/a)</td><td>1.18 (n/a)</td><td>0.81 (n/a)</td><td>888.50 (n/a)</td><td>590.16 (n/a)</td><td>593.00 (n/a)</td><td>313.10 (n/a)</td><td>206.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>2.57 (-14.03%)</td><td>1.65 (-16.09%)</td><td>1.67 (+11.13%)</td><td>0.32 <b>(-71.97%)</b></td><td>0.88 (+2.92%)</td><td>3238.70 <b>(+256.80%)</b></td><td>1098.22 <b>(+77.89%)</b></td><td>627.10 (-10.02%)</td><td>408.50 (+16.32%)</td><td>1204.95 <b>(+391.88%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>2.99 (n/a)</td><td>1.97 (n/a)</td><td>1.50 (n/a)</td><td>1.16 (n/a)</td><td>0.86 (n/a)</td><td>907.70 (n/a)</td><td>617.36 (n/a)</td><td>696.90 (n/a)</td><td>351.20 (n/a)</td><td>244.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.00 <b>(-20.24%)</b></td><td>2.12 (-0.61%)</td><td>1.78 (-1.19%)</td><td>1.26 (-19.13%)</td><td>0.76 (-17.59%)</td><td>835.20 <b>(+23.66%)</b></td><td>549.46 (+1.09%)</td><td>588.30 (+1.20%)</td><td>349.00 <b>(+25.36%)</b></td><td>198.89 <b>(+29.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.77 (n/a)</td><td>2.13 (n/a)</td><td>1.80 (n/a)</td><td>1.55 (n/a)</td><td>0.92 (n/a)</td><td>675.40 (n/a)</td><td>543.54 (n/a)</td><td>581.30 (n/a)</td><td>278.40 (n/a)</td><td>153.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.68 <b>(+24.52%)</b></td><td>1.60 (-19.95%)</td><td>1.70 (-5.73%)</td><td>0.29 <b>(-80.22%)</b></td><td>1.34 <b>(+136.97%)</b></td><td>3593.70 <b>(+405.59%)</b></td><td>1387.90 <b>(+151.56%)</b></td><td>616.40 (+6.09%)</td><td>285.10 (-19.69%)</td><td>1372.81 <b>(+959.07%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>2.95 (n/a)</td><td>2.00 (n/a)</td><td>1.80 (n/a)</td><td>1.48 (n/a)</td><td>0.56 (n/a)</td><td>710.80 (n/a)</td><td>551.72 (n/a)</td><td>581.00 (n/a)</td><td>355.00 (n/a)</td><td>129.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.42 (+15.72%)</td><td>2.00 (-15.76%)</td><td>1.92 (-16.79%)</td><td>0.30 <b>(-83.18%)</b></td><td>1.19 <b>(+164.52%)</b></td><td>3483.00 <b>(+494.67%)</b></td><td>1075.72 <b>(+136.07%)</b></td><td>546.40 <b>(+20.19%)</b></td><td>307.00 (-13.57%)</td><td>1352.93 <b>(+1418.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>2.95 (n/a)</td><td>2.37 (n/a)</td><td>2.31 (n/a)</td><td>1.79 (n/a)</td><td>0.45 (n/a)</td><td>585.70 (n/a)</td><td>455.68 (n/a)</td><td>454.60 (n/a)</td><td>355.20 (n/a)</td><td>89.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.78 (-7.86%)</td><td>2.49 (-17.00%)</td><td>3.48 (+14.94%)</td><td>0.58 <b>(-70.90%)</b></td><td>1.62 <b>(+91.13%)</b></td><td>3601.00 <b>(+243.57%)</b></td><td>1549.86 <b>(+107.00%)</b></td><td>603.30 (-12.99%)</td><td>554.90 (+8.53%)</td><td>1399.62 <b>(+541.60%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>4.10 (n/a)</td><td>2.99 (n/a)</td><td>3.02 (n/a)</td><td>2.00 (n/a)</td><td>0.85 (n/a)</td><td>1048.10 (n/a)</td><td>748.74 (n/a)</td><td>693.40 (n/a)</td><td>511.30 (n/a)</td><td>218.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>4.27 (+5.01%)</td><td>2.38 (-0.41%)</td><td>2.30 <b>(-23.02%)</b></td><td>0.85 <b>(+44.01%)</b></td><td>1.22 <b>(-27.53%)</b></td><td>2480.30 <b>(-30.56%)</b></td><td>1151.68 <b>(-35.14%)</b></td><td>912.40 <b>(+29.90%)</b></td><td>491.60 (-4.77%)</td><td>766.82 <b>(-52.63%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.06 (n/a)</td><td>2.39 (n/a)</td><td>2.99 (n/a)</td><td>0.59 (n/a)</td><td>1.69 (n/a)</td><td>3572.00 (n/a)</td><td>1775.74 (n/a)</td><td>702.40 (n/a)</td><td>516.20 (n/a)</td><td>1618.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.92 <b>(-38.97%)</b></td><td>2.11 <b>(-45.84%)</b></td><td>2.04 <b>(-43.41%)</b></td><td>0.58 <b>(-70.48%)</b></td><td>1.39 <b>(-31.67%)</b></td><td>3626.50 <b>(+238.70%)</b></td><td>1596.78 <b>(+133.96%)</b></td><td>1030.20 <b>(+76.71%)</b></td><td>534.80 <b>(+63.85%)</b></td><td>1287.81 <b>(+258.83%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.43 (n/a)</td><td>3.90 (n/a)</td><td>3.60 (n/a)</td><td>1.96 (n/a)</td><td>2.03 (n/a)</td><td>1070.70 (n/a)</td><td>682.50 (n/a)</td><td>583.00 (n/a)</td><td>326.40 (n/a)</td><td>358.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.35 <b>(+62.04%)</b></td><td>3.73 <b>(+74.69%)</b></td><td>3.84 <b>(+33.01%)</b></td><td>1.65 <b>(+179.02%)</b></td><td>1.65 (+16.55%)</td><td>1269.90 <b>(-64.16%)</b></td><td>687.54 <b>(-61.85%)</b></td><td>545.90 <b>(-24.82%)</b></td><td>392.20 <b>(-38.29%)</b></td><td>371.48 <b>(-76.12%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.30 (n/a)</td><td>2.13 (n/a)</td><td>2.89 (n/a)</td><td>0.59 (n/a)</td><td>1.41 (n/a)</td><td>3543.40 (n/a)</td><td>1802.06 (n/a)</td><td>726.10 (n/a)</td><td>635.60 (n/a)</td><td>1555.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>5.68 (+16.25%)</td><td>3.75 (-14.44%)</td><td>4.10 (-4.79%)</td><td>1.90 <b>(-50.80%)</b></td><td>1.55 <b>(+287.66%)</b></td><td>1106.10 <b>(+103.25%)</b></td><td>658.32 <b>(+36.68%)</b></td><td>512.00 (+5.05%)</td><td>369.20 (-13.98%)</td><td>309.63 <b>(+595.37%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>4.89 (n/a)</td><td>4.38 (n/a)</td><td>4.30 (n/a)</td><td>3.85 (n/a)</td><td>0.40 (n/a)</td><td>544.20 (n/a)</td><td>481.66 (n/a)</td><td>487.40 (n/a)</td><td>429.20 (n/a)</td><td>44.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>4.95 (-15.99%)</td><td>4.07 <b>(+21.39%)</b></td><td>4.13 <b>(+23.08%)</b></td><td>3.21 <b>(+439.17%)</b></td><td>0.83 <b>(-56.43%)</b></td><td>652.90 <b>(-81.45%)</b></td><td>533.80 <b>(-53.45%)</b></td><td>507.60 (-18.76%)</td><td>423.60 (+19.02%)</td><td>110.95 <b>(-91.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.89 (n/a)</td><td>3.35 (n/a)</td><td>3.36 (n/a)</td><td>0.60 (n/a)</td><td>1.90 (n/a)</td><td>3520.50 (n/a)</td><td>1146.74 (n/a)</td><td>624.80 (n/a)</td><td>355.90 (n/a)</td><td>1332.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>5.42 (-16.15%)</td><td>3.38 <b>(+26.49%)</b></td><td>3.56 <b>(+166.51%)</b></td><td>0.58 (-2.07%)</td><td>1.75 <b>(-29.96%)</b></td><td>3627.60 (+2.11%)</td><td>1150.34 <b>(-29.16%)</b></td><td>588.70 <b>(-62.48%)</b></td><td>387.20 (+19.29%)</td><td>1387.57 (+5.71%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.46 (n/a)</td><td>2.67 (n/a)</td><td>1.34 (n/a)</td><td>0.59 (n/a)</td><td>2.50 (n/a)</td><td>3552.60 (n/a)</td><td>1623.94 (n/a)</td><td>1569.10 (n/a)</td><td>324.60 (n/a)</td><td>1312.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.47 (-3.67%)</td><td>3.39 (-10.38%)</td><td>2.67 <b>(-49.85%)</b></td><td>1.75 <b>(+199.68%)</b></td><td>1.54 <b>(-37.16%)</b></td><td>1197.20 <b>(-66.63%)</b></td><td>729.76 <b>(-38.72%)</b></td><td>786.90 <b>(+99.42%)</b></td><td>383.50 (+3.82%)</td><td>323.98 <b>(-76.69%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.68 (n/a)</td><td>3.79 (n/a)</td><td>5.31 (n/a)</td><td>0.58 (n/a)</td><td>2.45 (n/a)</td><td>3587.70 (n/a)</td><td>1190.90 (n/a)</td><td>394.60 (n/a)</td><td>369.40 (n/a)</td><td>1389.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>4.96 <b>(-23.17%)</b></td><td>3.29 <b>(-23.38%)</b></td><td>3.00 <b>(-22.08%)</b></td><td>1.94 (-6.55%)</td><td>1.13 <b>(-43.71%)</b></td><td>1081.70 (+7.00%)</td><td>701.56 (+18.29%)</td><td>698.10 <b>(+28.35%)</b></td><td>422.50 <b>(+30.16%)</b></td><td>246.56 (-15.75%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.46 (n/a)</td><td>4.30 (n/a)</td><td>3.86 (n/a)</td><td>2.07 (n/a)</td><td>2.01 (n/a)</td><td>1010.90 (n/a)</td><td>593.10 (n/a)</td><td>543.90 (n/a)</td><td>324.60 (n/a)</td><td>292.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.96 <b>(+23.76%)</b></td><td>3.51 (+6.96%)</td><td>2.99 <b>(-26.20%)</b></td><td>1.55 <b>(+163.99%)</b></td><td>1.64 (-1.15%)</td><td>1350.70 <b>(-62.12%)</b></td><td>726.38 <b>(-37.04%)</b></td><td>702.50 <b>(+35.51%)</b></td><td>352.00 (-19.21%)</td><td>379.90 <b>(-71.92%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.81 (n/a)</td><td>3.28 (n/a)</td><td>4.05 (n/a)</td><td>0.59 (n/a)</td><td>1.66 (n/a)</td><td>3565.60 (n/a)</td><td>1153.72 (n/a)</td><td>518.40 (n/a)</td><td>435.70 (n/a)</td><td>1352.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.26 <b>(-57.24%)</b></td><td>2.10 <b>(-39.22%)</b></td><td>2.05 <b>(-29.24%)</b></td><td>0.99 <b>(+67.67%)</b></td><td>0.80 <b>(-68.95%)</b></td><td>2127.80 <b>(-40.36%)</b></td><td>1159.12 (-3.16%)</td><td>1022.00 <b>(+41.32%)</b></td><td>643.70 <b>(+133.90%)</b></td><td>564.44 <b>(-57.96%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>7.62 (n/a)</td><td>3.45 (n/a)</td><td>2.90 (n/a)</td><td>0.59 (n/a)</td><td>2.59 (n/a)</td><td>3567.80 (n/a)</td><td>1196.98 (n/a)</td><td>723.20 (n/a)</td><td>275.20 (n/a)</td><td>1342.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.28 <b>(+28.71%)</b></td><td>3.36 (+19.70%)</td><td>3.13 (-12.45%)</td><td>0.60 (+2.21%)</td><td>1.86 (+17.42%)</td><td>3522.30 (-2.17%)</td><td>1147.98 (-11.03%)</td><td>670.40 (+14.21%)</td><td>396.90 <b>(-22.31%)</b></td><td>1334.91 (+0.60%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.10 (n/a)</td><td>2.81 (n/a)</td><td>3.57 (n/a)</td><td>0.58 (n/a)</td><td>1.59 (n/a)</td><td>3600.30 (n/a)</td><td>1290.32 (n/a)</td><td>587.00 (n/a)</td><td>510.90 (n/a)</td><td>1326.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>5.07 (-1.83%)</td><td>4.51 (+14.93%)</td><td>4.56 (+4.82%)</td><td>4.01 <b>(+137.80%)</b></td><td>0.39 <b>(-72.08%)</b></td><td>1045.40 <b>(-57.95%)</b></td><td>935.38 <b>(-25.84%)</b></td><td>920.50 (-4.59%)</td><td>826.60 (+1.86%)</td><td>80.22 <b>(-88.53%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>5.17 (n/a)</td><td>3.92 (n/a)</td><td>4.35 (n/a)</td><td>1.69 (n/a)</td><td>1.40 (n/a)</td><td>2486.00 (n/a)</td><td>1261.28 (n/a)</td><td>964.80 (n/a)</td><td>811.50 (n/a)</td><td>699.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.37 (+1.85%)</td><td>3.79 (-0.55%)</td><td>4.04 (-3.64%)</td><td>1.21 (-1.35%)</td><td>1.55 (+0.44%)</td><td>3452.90 (+1.37%)</td><td>1457.76 (+0.94%)</td><td>1037.80 (+3.78%)</td><td>781.10 (-1.81%)</td><td>1120.90 (+1.67%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.27 (n/a)</td><td>3.82 (n/a)</td><td>4.19 (n/a)</td><td>1.23 (n/a)</td><td>1.54 (n/a)</td><td>3406.10 (n/a)</td><td>1444.20 (n/a)</td><td>1000.00 (n/a)</td><td>795.50 (n/a)</td><td>1102.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>8.35 (+7.06%)</td><td>5.06 (-1.82%)</td><td>5.69 (-5.21%)</td><td>2.00 (+18.59%)</td><td>2.41 (-0.29%)</td><td>2095.60 (-15.68%)</td><td>1049.22 (-4.11%)</td><td>736.90 (+5.50%)</td><td>502.30 (-6.60%)</td><td>633.85 <b>(-21.42%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>7.80 (n/a)</td><td>5.16 (n/a)</td><td>6.00 (n/a)</td><td>1.69 (n/a)</td><td>2.42 (n/a)</td><td>2485.20 (n/a)</td><td>1094.24 (n/a)</td><td>698.50 (n/a)</td><td>537.80 (n/a)</td><td>806.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>8.72 (+12.22%)</td><td>5.54 (-13.52%)</td><td>4.21 <b>(-37.76%)</b></td><td>2.86 <b>(-24.46%)</b></td><td>2.53 <b>(+57.48%)</b></td><td>1466.70 <b>(+32.37%)</b></td><td>897.28 <b>(+28.02%)</b></td><td>995.70 <b>(+60.67%)</b></td><td>480.80 (-10.90%)</td><td>401.00 <b>(+70.78%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.77 (n/a)</td><td>6.41 (n/a)</td><td>6.77 (n/a)</td><td>3.79 (n/a)</td><td>1.61 (n/a)</td><td>1108.00 (n/a)</td><td>700.90 (n/a)</td><td>619.70 (n/a)</td><td>539.60 (n/a)</td><td>234.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>9.49 (+15.30%)</td><td>6.43 <b>(+21.74%)</b></td><td>6.99 (+19.73%)</td><td>3.90 <b>(+129.08%)</b></td><td>2.36 (-7.73%)</td><td>1075.50 <b>(-56.35%)</b></td><td>733.46 <b>(-32.07%)</b></td><td>599.80 (-16.47%)</td><td>442.10 (-13.28%)</td><td>282.82 <b>(-64.82%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>8.23 (n/a)</td><td>5.28 (n/a)</td><td>5.84 (n/a)</td><td>1.70 (n/a)</td><td>2.56 (n/a)</td><td>2463.70 (n/a)</td><td>1079.66 (n/a)</td><td>718.10 (n/a)</td><td>509.80 (n/a)</td><td>803.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.21 <b>(-20.35%)</b></td><td>4.99 (-10.67%)</td><td>4.41 <b>(-29.75%)</b></td><td>3.49 <b>(+84.64%)</b></td><td>1.46 <b>(-56.57%)</b></td><td>1200.90 <b>(-45.84%)</b></td><td>895.24 <b>(-21.47%)</b></td><td>950.80 <b>(+42.36%)</b></td><td>581.60 <b>(+25.56%)</b></td><td>239.06 <b>(-71.25%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>9.05 (n/a)</td><td>5.59 (n/a)</td><td>6.28 (n/a)</td><td>1.89 (n/a)</td><td>3.37 (n/a)</td><td>2217.30 (n/a)</td><td>1139.96 (n/a)</td><td>667.90 (n/a)</td><td>463.20 (n/a)</td><td>831.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>12.52 <b>(+38.66%)</b></td><td>8.31 <b>(+26.67%)</b></td><td>7.09 (-5.87%)</td><td>6.61 <b>(+461.10%)</b></td><td>2.49 <b>(-20.26%)</b></td><td>635.00 <b>(-82.18%)</b></td><td>534.58 <b>(-53.18%)</b></td><td>591.40 (+6.23%)</td><td>335.00 <b>(-27.88%)</b></td><td>126.38 <b>(-90.67%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>9.03 (n/a)</td><td>6.56 (n/a)</td><td>7.53 (n/a)</td><td>1.18 (n/a)</td><td>3.12 (n/a)</td><td>3563.00 (n/a)</td><td>1141.78 (n/a)</td><td>556.70 (n/a)</td><td>464.50 (n/a)</td><td>1354.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>11.34 <b>(+46.16%)</b></td><td>4.97 (-6.08%)</td><td>3.94 <b>(-42.29%)</b></td><td>1.67 <b>(+45.76%)</b></td><td>3.70 <b>(+33.91%)</b></td><td>2516.70 <b>(-31.40%)</b></td><td>1216.70 (-6.92%)</td><td>1063.80 <b>(+73.29%)</b></td><td>369.70 <b>(-31.59%)</b></td><td>787.40 <b>(-41.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.76 (n/a)</td><td>5.29 (n/a)</td><td>6.83 (n/a)</td><td>1.14 (n/a)</td><td>2.76 (n/a)</td><td>3668.40 (n/a)</td><td>1307.10 (n/a)</td><td>613.90 (n/a)</td><td>540.40 (n/a)</td><td>1339.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>8.50 (-18.96%)</td><td>5.85 (-6.57%)</td><td>6.13 (-6.06%)</td><td>1.73 (-9.71%)</td><td>2.53 <b>(-29.53%)</b></td><td>2421.20 (+10.76%)</td><td>982.90 (+0.13%)</td><td>684.70 (+6.45%)</td><td>493.50 <b>(+23.41%)</b></td><td>808.92 (+8.71%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>10.49 (n/a)</td><td>6.26 (n/a)</td><td>6.52 (n/a)</td><td>1.92 (n/a)</td><td>3.59 (n/a)</td><td>2186.00 (n/a)</td><td>981.58 (n/a)</td><td>643.20 (n/a)</td><td>399.90 (n/a)</td><td>744.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.78 <b>(-24.93%)</b></td><td>5.95 (+16.74%)</td><td>6.18 (+9.78%)</td><td>3.89 <b>(+182.61%)</b></td><td>1.55 <b>(-56.33%)</b></td><td>1079.20 <b>(-64.61%)</b></td><td>749.56 <b>(-44.63%)</b></td><td>678.20 (-8.92%)</td><td>539.00 <b>(+33.22%)</b></td><td>217.01 <b>(-80.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>10.37 (n/a)</td><td>5.10 (n/a)</td><td>5.63 (n/a)</td><td>1.38 (n/a)</td><td>3.55 (n/a)</td><td>3049.80 (n/a)</td><td>1353.78 (n/a)</td><td>744.60 (n/a)</td><td>404.60 (n/a)</td><td>1095.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>11.29 <b>(+51.02%)</b></td><td>6.65 <b>(+20.04%)</b></td><td>6.69 (+9.65%)</td><td>2.12 <b>(-30.20%)</b></td><td>3.25 <b>(+78.20%)</b></td><td>1976.90 <b>(+43.27%)</b></td><td>850.18 (+0.83%)</td><td>626.60 (-8.81%)</td><td>371.50 <b>(-33.78%)</b></td><td>640.22 <b>(+89.36%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>7.48 (n/a)</td><td>5.54 (n/a)</td><td>6.10 (n/a)</td><td>3.04 (n/a)</td><td>1.82 (n/a)</td><td>1379.80 (n/a)</td><td>843.22 (n/a)</td><td>687.10 (n/a)</td><td>561.00 (n/a)</td><td>338.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>8.34 (-15.31%)</td><td>5.95 (+5.52%)</td><td>7.42 <b>(+69.24%)</b></td><td>1.15 <b>(-66.33%)</b></td><td>3.09 (+16.03%)</td><td>3646.90 <b>(+196.98%)</b></td><td>1228.06 <b>(+42.12%)</b></td><td>564.90 <b>(-40.92%)</b></td><td>502.70 (+18.06%)</td><td>1363.09 <b>(+313.37%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>9.85 (n/a)</td><td>5.64 (n/a)</td><td>4.39 (n/a)</td><td>3.42 (n/a)</td><td>2.66 (n/a)</td><td>1228.00 (n/a)</td><td>864.10 (n/a)</td><td>956.10 (n/a)</td><td>425.80 (n/a)</td><td>329.75 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>1.40 <b>(-20.53%)</b></td><td>1.13 (-1.26%)</td><td>1.28 (+6.40%)</td><td>0.69 (+12.09%)</td><td>0.30 <b>(-36.94%)</b></td><td>755.60 (-10.79%)</td><td>497.62 (-7.15%)</td><td>409.90 (-6.03%)</td><td>374.20 <b>(+25.87%)</b></td><td>161.91 <b>(-32.64%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>1.76 (n/a)</td><td>1.15 (n/a)</td><td>1.20 (n/a)</td><td>0.62 (n/a)</td><td>0.48 (n/a)</td><td>847.00 (n/a)</td><td>535.94 (n/a)</td><td>436.20 (n/a)</td><td>297.30 (n/a)</td><td>240.35 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.43 <b>(+41.22%)</b></td><td>2.96 <b>(+78.81%)</b></td><td>2.79 <b>(+58.61%)</b></td><td>2.57 <b>(+769.75%)</b></td><td>0.40 <b>(-54.13%)</b></td><td>407.50 <b>(-88.50%)</b></td><td>358.76 <b>(-68.76%)</b></td><td>375.90 <b>(-36.96%)</b></td><td>305.90 <b>(-29.21%)</b></td><td>46.49 <b>(-96.54%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>2.43 (n/a)</td><td>1.66 (n/a)</td><td>1.76 (n/a)</td><td>0.30 (n/a)</td><td>0.86 (n/a)</td><td>3543.90 (n/a)</td><td>1148.32 (n/a)</td><td>596.30 (n/a)</td><td>432.10 (n/a)</td><td>1344.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.47 (-11.78%)</td><td>2.29 (-9.59%)</td><td>2.57 (+2.49%)</td><td>0.63 (+5.79%)</td><td>1.09 (-16.00%)</td><td>3331.60 (-5.47%)</td><td>1316.18 (+1.81%)</td><td>816.00 (-2.44%)</td><td>604.90 (+13.34%)</td><td>1141.80 (-9.36%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>3.93 (n/a)</td><td>2.54 (n/a)</td><td>2.51 (n/a)</td><td>0.60 (n/a)</td><td>1.30 (n/a)</td><td>3524.40 (n/a)</td><td>1292.78 (n/a)</td><td>836.40 (n/a)</td><td>533.70 (n/a)</td><td>1259.68 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>1.97 (+19.29%)</td><td>1.41 <b>(+26.75%)</b></td><td>1.28 <b>(+31.21%)</b></td><td>0.79 <b>(+38.25%)</b></td><td>0.48 (-2.22%)</td><td>660.60 <b>(-27.67%)</b></td><td>412.38 <b>(-25.88%)</b></td><td>410.70 <b>(-23.79%)</b></td><td>265.60 (-16.16%)</td><td>157.56 <b>(-37.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.66 (n/a)</td><td>1.11 (n/a)</td><td>0.97 (n/a)</td><td>0.57 (n/a)</td><td>0.49 (n/a)</td><td>913.30 (n/a)</td><td>556.40 (n/a)</td><td>538.90 (n/a)</td><td>316.80 (n/a)</td><td>252.67 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>1.06 <b>(-47.16%)</b></td><td>0.83 <b>(-34.27%)</b></td><td>0.94 (-12.64%)</td><td>0.21 <b>(-75.52%)</b></td><td>0.35 <b>(-27.89%)</b></td><td>2482.30 <b>(+308.47%)</b></td><td>924.18 <b>(+100.54%)</b></td><td>559.90 (+14.48%)</td><td>493.80 <b>(+89.27%)</b></td><td>871.51 <b>(+479.18%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>2.01 (n/a)</td><td>1.26 (n/a)</td><td>1.07 (n/a)</td><td>0.86 (n/a)</td><td>0.49 (n/a)</td><td>607.70 (n/a)</td><td>460.84 (n/a)</td><td>489.10 (n/a)</td><td>260.90 (n/a)</td><td>150.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>1.59 (-19.93%)</td><td>1.24 (-13.53%)</td><td>1.30 (-11.39%)</td><td>0.90 (-2.42%)</td><td>0.31 <b>(-21.60%)</b></td><td>579.40 (+2.48%)</td><td>447.26 (+14.39%)</td><td>401.80 (+12.83%)</td><td>329.80 <b>(+24.88%)</b></td><td>116.43 (+2.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.99 (n/a)</td><td>1.43 (n/a)</td><td>1.47 (n/a)</td><td>0.93 (n/a)</td><td>0.39 (n/a)</td><td>565.40 (n/a)</td><td>390.98 (n/a)</td><td>356.10 (n/a)</td><td>264.10 (n/a)</td><td>113.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (+10.64%)</td><td>0.10 <b>(+22.19%)</b></td><td>0.11 <b>(+64.10%)</b></td><td>0.07 (+6.30%)</td><td>0.03 (-0.08%)</td><td>482.90 (-5.94%)</td><td>333.06 (-19.14%)</td><td>293.40 <b>(-39.07%)</b></td><td>243.70 (-9.64%)</td><td>98.21 (-15.53%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>513.40 (n/a)</td><td>411.92 (n/a)</td><td>481.50 (n/a)</td><td>269.70 (n/a)</td><td>116.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (+0.75%)</td><td>0.12 <b>(+25.51%)</b></td><td>0.12 <b>(+36.03%)</b></td><td>0.10 <b>(+67.75%)</b></td><td>0.01 <b>(-56.00%)</b></td><td>322.90 <b>(-40.38%)</b></td><td>280.66 <b>(-26.79%)</b></td><td>278.40 <b>(-26.49%)</b></td><td>240.50 (-0.78%)</td><td>34.05 <b>(-73.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>541.60 (n/a)</td><td>383.36 (n/a)</td><td>378.70 (n/a)</td><td>242.40 (n/a)</td><td>129.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.15 (+6.11%)</td><td>0.10 (-0.31%)</td><td>0.11 (+4.20%)</td><td>0.06 (-6.19%)</td><td>0.04 <b>(+27.78%)</b></td><td>564.20 (+6.59%)</td><td>379.32 (+6.48%)</td><td>286.90 (-4.01%)</td><td>217.90 (-5.75%)</td><td>162.59 <b>(+36.59%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>529.30 (n/a)</td><td>356.24 (n/a)</td><td>298.90 (n/a)</td><td>231.20 (n/a)</td><td>119.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (+12.42%)</td><td>0.09 (+6.12%)</td><td>0.09 <b>(+32.18%)</b></td><td>0.05 (-19.76%)</td><td>0.04 <b>(+26.65%)</b></td><td>658.70 <b>(+24.61%)</b></td><td>423.32 (+0.01%)</td><td>375.60 <b>(-24.35%)</b></td><td>222.20 (-11.05%)</td><td>180.07 <b>(+38.08%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>528.60 (n/a)</td><td>423.26 (n/a)</td><td>496.50 (n/a)</td><td>249.80 (n/a)</td><td>130.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.31 <b>(+38.32%)</b></td><td>0.24 <b>(+60.85%)</b></td><td>0.23 <b>(+82.55%)</b></td><td>0.12 (+1.88%)</td><td>0.07 <b>(+73.75%)</b></td><td>540.80 (-1.83%)</td><td>307.16 <b>(-34.11%)</b></td><td>280.50 <b>(-45.23%)</b></td><td>214.30 <b>(-27.72%)</b></td><td>134.77 <b>(+24.94%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>550.90 (n/a)</td><td>466.14 (n/a)</td><td>512.10 (n/a)</td><td>296.50 (n/a)</td><td>107.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.29 (+10.69%)</td><td>0.18 (+9.40%)</td><td>0.12 (-5.48%)</td><td>0.12 (+8.59%)</td><td>0.09 <b>(+30.24%)</b></td><td>567.10 (-7.91%)</td><td>430.14 (-3.32%)</td><td>556.40 (+5.80%)</td><td>222.80 (-9.69%)</td><td>180.68 (+12.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>615.80 (n/a)</td><td>444.90 (n/a)</td><td>525.90 (n/a)</td><td>246.70 (n/a)</td><td>160.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.33 <b>(+47.38%)</b></td><td>0.22 <b>(+40.95%)</b></td><td>0.24 <b>(+59.69%)</b></td><td>0.11 (+3.06%)</td><td>0.09 <b>(+102.94%)</b></td><td>573.90 (-2.98%)</td><td>350.90 <b>(-21.74%)</b></td><td>271.10 <b>(-37.39%)</b></td><td>197.30 <b>(-32.15%)</b></td><td>159.86 <b>(+39.61%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>591.50 (n/a)</td><td>448.40 (n/a)</td><td>433.00 (n/a)</td><td>290.80 (n/a)</td><td>114.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.27 (+14.48%)</td><td>0.16 <b>(-20.48%)</b></td><td>0.13 <b>(-41.15%)</b></td><td>0.10 <b>(-23.64%)</b></td><td>0.07 <b>(+65.25%)</b></td><td>644.20 <b>(+30.96%)</b></td><td>476.14 <b>(+36.29%)</b></td><td>513.00 <b>(+69.92%)</b></td><td>242.90 (-12.66%)</td><td>162.21 <b>(+84.91%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>491.90 (n/a)</td><td>349.36 (n/a)</td><td>301.90 (n/a)</td><td>278.10 (n/a)</td><td>87.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.34 <b>(+74.54%)</b></td><td>0.21 <b>(+55.15%)</b></td><td>0.22 <b>(+104.43%)</b></td><td>0.06 <b>(-41.40%)</b></td><td>0.11 <b>(+177.71%)</b></td><td>1075.90 <b>(+70.64%)</b></td><td>454.28 (-12.88%)</td><td>293.10 <b>(-51.08%)</b></td><td>191.50 <b>(-42.72%)</b></td><td>362.40 <b>(+181.84%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>630.50 (n/a)</td><td>521.42 (n/a)</td><td>599.10 (n/a)</td><td>334.30 (n/a)</td><td>128.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.26 (-13.49%)</td><td>0.20 (+7.41%)</td><td>0.18 <b>(+23.46%)</b></td><td>0.13 (+6.95%)</td><td>0.06 <b>(-24.32%)</b></td><td>491.00 (-6.49%)</td><td>354.42 (-10.52%)</td><td>354.40 (-18.99%)</td><td>249.10 (+15.59%)</td><td>101.36 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>525.10 (n/a)</td><td>396.10 (n/a)</td><td>437.50 (n/a)</td><td>215.50 (n/a)</td><td>126.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.59 (+19.54%)</td><td>0.41 <b>(+28.80%)</b></td><td>0.43 <b>(+52.73%)</b></td><td>0.22 <b>(+86.33%)</b></td><td>0.14 (-5.84%)</td><td>600.20 <b>(-46.33%)</b></td><td>358.20 <b>(-32.41%)</b></td><td>307.60 <b>(-34.53%)</b></td><td>222.10 (-16.35%)</td><td>149.94 <b>(-56.61%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.49 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>1118.40 (n/a)</td><td>529.94 (n/a)</td><td>469.80 (n/a)</td><td>265.50 (n/a)</td><td>345.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.44 (-3.31%)</td><td>0.34 (+7.72%)</td><td>0.31 (+19.91%)</td><td>0.23 (+4.85%)</td><td>0.09 (-14.01%)</td><td>569.00 (-4.63%)</td><td>406.64 (-9.41%)</td><td>422.50 (-16.60%)</td><td>295.50 (+3.43%)</td><td>112.84 (-17.49%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>596.60 (n/a)</td><td>448.86 (n/a)</td><td>506.60 (n/a)</td><td>285.70 (n/a)</td><td>136.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.57 (+13.81%)</td><td>0.46 <b>(+23.96%)</b></td><td>0.49 (+19.54%)</td><td>0.26 (+12.15%)</td><td>0.12 (-1.69%)</td><td>502.60 (-10.82%)</td><td>308.82 <b>(-21.05%)</b></td><td>269.70 (-16.35%)</td><td>228.10 (-12.13%)</td><td>110.81 <b>(-21.06%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.41 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>563.60 (n/a)</td><td>391.18 (n/a)</td><td>322.40 (n/a)</td><td>259.60 (n/a)</td><td>140.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.37 (-17.09%)</td><td>0.27 (-11.22%)</td><td>0.25 <b>(-26.39%)</b></td><td>0.20 <b>(+189.58%)</b></td><td>0.07 <b>(-53.11%)</b></td><td>646.10 <b>(-65.47%)</b></td><td>506.90 <b>(-25.38%)</b></td><td>524.90 <b>(+35.84%)</b></td><td>350.80 <b>(+20.59%)</b></td><td>130.20 <b>(-80.70%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.45 (n/a)</td><td>0.31 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1871.10 (n/a)</td><td>679.34 (n/a)</td><td>386.40 (n/a)</td><td>290.90 (n/a)</td><td>674.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.54 (+6.49%)</td><td>0.30 (-2.60%)</td><td>0.24 (-8.84%)</td><td>0.05 <b>(-75.63%)</b></td><td>0.19 <b>(+63.36%)</b></td><td>2516.10 <b>(+310.32%)</b></td><td>832.66 <b>(+79.87%)</b></td><td>552.70 (+9.71%)</td><td>242.30 (-6.09%)</td><td>952.45 <b>(+578.89%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.51 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>613.20 (n/a)</td><td>462.92 (n/a)</td><td>503.80 (n/a)</td><td>258.00 (n/a)</td><td>140.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.54 (-13.61%)</td><td>0.37 (-2.01%)</td><td>0.30 (+4.69%)</td><td>0.25 (+11.13%)</td><td>0.12 <b>(-30.23%)</b></td><td>519.80 (-10.01%)</td><td>390.46 (-5.87%)</td><td>433.60 (-4.49%)</td><td>244.10 (+15.74%)</td><td>118.23 <b>(-30.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.62 (n/a)</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>577.60 (n/a)</td><td>414.82 (n/a)</td><td>454.00 (n/a)</td><td>210.90 (n/a)</td><td>169.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (-7.57%)</td><td>0.03 <b>(-28.17%)</b></td><td>0.03 <b>(-28.77%)</b></td><td>0.01 <b>(-80.23%)</b></td><td>0.02 <b>(+36.34%)</b></td><td>2484.90 <b>(+405.78%)</b></td><td>846.40 <b>(+128.32%)</b></td><td>473.90 <b>(+40.37%)</b></td><td>249.50 (+8.15%)</td><td>923.77 <b>(+714.15%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>491.30 (n/a)</td><td>370.70 (n/a)</td><td>337.60 (n/a)</td><td>230.70 (n/a)</td><td>113.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 <b>(+53.54%)</b></td><td>0.06 <b>(+34.40%)</b></td><td>0.06 <b>(+46.03%)</b></td><td>0.03 (-6.25%)</td><td>0.03 <b>(+108.82%)</b></td><td>608.00 (+6.69%)</td><td>347.14 (-16.43%)</td><td>276.80 <b>(-31.50%)</b></td><td>171.70 <b>(-34.86%)</b></td><td>168.16 <b>(+52.39%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>569.90 (n/a)</td><td>415.38 (n/a)</td><td>404.10 (n/a)</td><td>263.60 (n/a)</td><td>110.35 (n/a)</td>
</tr>
</tbody>
</table>


</details>
