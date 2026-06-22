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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (+13.29%)</td><td>0.02 (+5.04%)</td><td>0.02 (+3.73%)</td><td>0.01 (+11.90%)</td><td>0.01 (+3.29%)</td><td>498.00 (-10.64%)</td><td>351.10 (-6.15%)</td><td>328.10 (-3.59%)</td><td>200.20 (-11.73%)</td><td>134.57 (-13.02%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.30 (n/a)</td><td>374.10 (n/a)</td><td>340.30 (n/a)</td><td>226.80 (n/a)</td><td>154.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (-1.02%)</td><td>0.02 (+11.57%)</td><td>0.02 <b>(+23.51%)</b></td><td>0.01 (-17.08%)</td><td>0.01 <b>(+21.23%)</b></td><td>569.70 <b>(+20.60%)</b></td><td>313.38 (-5.73%)</td><td>248.60 (-19.05%)</td><td>235.00 (+1.03%)</td><td>144.24 <b>(+50.76%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>472.40 (n/a)</td><td>332.44 (n/a)</td><td>307.10 (n/a)</td><td>232.60 (n/a)</td><td>95.67 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (+18.03%)</td><td>0.02 <b>(+23.49%)</b></td><td>0.02 (-1.01%)</td><td>0.01 <b>(+68.83%)</b></td><td>0.01 (-6.74%)</td><td>493.40 <b>(-40.77%)</b></td><td>315.44 <b>(-28.94%)</b></td><td>295.40 (+0.99%)</td><td>186.10 (-15.26%)</td><td>118.34 <b>(-54.22%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>833.00 (n/a)</td><td>443.88 (n/a)</td><td>292.50 (n/a)</td><td>219.60 (n/a)</td><td>258.52 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (+8.66%)</td><td>0.02 (+1.23%)</td><td>0.02 <b>(+54.52%)</b></td><td>0.00 <b>(-75.95%)</b></td><td>0.01 <b>(+65.23%)</b></td><td>2122.30 <b>(+315.81%)</b></td><td>687.50 <b>(+81.68%)</b></td><td>249.90 <b>(-35.28%)</b></td><td>208.70 (-7.94%)</td><td>818.23 <b>(+517.14%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>510.40 (n/a)</td><td>378.42 (n/a)</td><td>386.10 (n/a)</td><td>226.70 (n/a)</td><td>132.58 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 <b>(-23.40%)</b></td><td>0.01 (-16.10%)</td><td>0.01 (-18.06%)</td><td>0.01 <b>(+274.65%)</b></td><td>0.00 <b>(-55.39%)</b></td><td>658.00 <b>(-73.31%)</b></td><td>539.72 <b>(-33.48%)</b></td><td>593.70 <b>(+22.03%)</b></td><td>321.30 <b>(+30.56%)</b></td><td>135.07 <b>(-85.55%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2465.20 (n/a)</td><td>811.42 (n/a)</td><td>486.50 (n/a)</td><td>246.10 (n/a)</td><td>934.87 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (-5.95%)</td><td>0.02 (-16.90%)</td><td>0.01 <b>(-44.65%)</b></td><td>0.01 (+10.03%)</td><td>0.01 (-2.03%)</td><td>518.70 (-9.11%)</td><td>413.86 <b>(+20.06%)</b></td><td>505.40 <b>(+80.63%)</b></td><td>258.60 (+6.33%)</td><td>134.63 (-2.46%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.70 (n/a)</td><td>344.70 (n/a)</td><td>279.80 (n/a)</td><td>243.20 (n/a)</td><td>138.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 <b>(-39.25%)</b></td><td>0.03 <b>(-36.43%)</b></td><td>0.02 <b>(-48.92%)</b></td><td>0.02 (-13.07%)</td><td>0.01 <b>(-41.94%)</b></td><td>600.40 (+15.04%)</td><td>477.48 <b>(+51.75%)</b></td><td>531.40 <b>(+95.73%)</b></td><td>350.00 <b>(+64.63%)</b></td><td>117.78 (-1.93%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.90 (n/a)</td><td>314.64 (n/a)</td><td>271.50 (n/a)</td><td>212.60 (n/a)</td><td>120.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (-2.19%)</td><td>0.04 (+2.57%)</td><td>0.03 <b>(-22.37%)</b></td><td>0.02 <b>(+255.84%)</b></td><td>0.01 <b>(-34.64%)</b></td><td>551.10 <b>(-71.90%)</b></td><td>371.28 <b>(-41.26%)</b></td><td>385.30 <b>(+28.82%)</b></td><td>232.10 (+2.25%)</td><td>120.31 <b>(-83.85%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1961.20 (n/a)</td><td>632.02 (n/a)</td><td>299.10 (n/a)</td><td>227.00 (n/a)</td><td>744.85 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 <b>(-44.71%)</b></td><td>0.03 <b>(-43.63%)</b></td><td>0.02 <b>(-51.32%)</b></td><td>0.02 <b>(-29.91%)</b></td><td>0.01 <b>(-45.08%)</b></td><td>598.20 <b>(+42.67%)</b></td><td>490.24 <b>(+75.01%)</b></td><td>524.30 <b>(+105.45%)</b></td><td>352.40 <b>(+80.90%)</b></td><td>116.48 <b>(+37.89%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>419.30 (n/a)</td><td>280.12 (n/a)</td><td>255.20 (n/a)</td><td>194.80 (n/a)</td><td>84.47 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (-6.48%)</td><td>0.04 (-4.38%)</td><td>0.04 (+16.39%)</td><td>0.02 (-11.82%)</td><td>0.01 (-1.52%)</td><td>620.60 (+13.41%)</td><td>402.58 (+7.57%)</td><td>282.10 (-14.10%)</td><td>250.30 (+6.92%)</td><td>188.60 <b>(+23.00%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>547.20 (n/a)</td><td>374.24 (n/a)</td><td>328.40 (n/a)</td><td>234.10 (n/a)</td><td>153.34 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 <b>(-31.59%)</b></td><td>0.03 <b>(-27.58%)</b></td><td>0.03 <b>(-25.86%)</b></td><td>0.02 <b>(-35.36%)</b></td><td>0.01 (-18.45%)</td><td>645.50 <b>(+54.72%)</b></td><td>478.82 <b>(+41.97%)</b></td><td>481.70 <b>(+34.89%)</b></td><td>317.30 <b>(+46.15%)</b></td><td>143.47 <b>(+95.14%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>417.20 (n/a)</td><td>337.26 (n/a)</td><td>357.10 (n/a)</td><td>217.10 (n/a)</td><td>73.52 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (+0.48%)</td><td>0.03 (-17.22%)</td><td>0.03 (-17.06%)</td><td>0.02 <b>(-32.12%)</b></td><td>0.01 <b>(+29.56%)</b></td><td>725.50 <b>(+47.31%)</b></td><td>478.98 <b>(+29.73%)</b></td><td>437.70 <b>(+20.58%)</b></td><td>242.20 (-0.49%)</td><td>178.00 <b>(+83.84%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.50 (n/a)</td><td>369.20 (n/a)</td><td>363.00 (n/a)</td><td>243.40 (n/a)</td><td>96.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (-6.36%)</td><td>0.07 (-8.00%)</td><td>0.07 <b>(-23.06%)</b></td><td>0.05 (+13.59%)</td><td>0.01 <b>(-41.54%)</b></td><td>456.50 (-11.97%)</td><td>365.72 (+3.82%)</td><td>365.10 <b>(+29.98%)</b></td><td>291.10 (+6.79%)</td><td>63.68 <b>(-42.75%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>518.60 (n/a)</td><td>352.28 (n/a)</td><td>280.90 (n/a)</td><td>272.60 (n/a)</td><td>111.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 (-5.98%)</td><td>0.08 (-11.59%)</td><td>0.08 (-10.57%)</td><td>0.04 (-8.39%)</td><td>0.02 (-0.76%)</td><td>547.40 (+9.15%)</td><td>353.44 (+13.92%)</td><td>296.20 (+11.82%)</td><td>254.10 (+6.36%)</td><td>121.88 (+11.53%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>501.50 (n/a)</td><td>310.26 (n/a)</td><td>264.90 (n/a)</td><td>238.90 (n/a)</td><td>109.28 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 <b>(-42.84%)</b></td><td>0.06 <b>(-21.21%)</b></td><td>0.05 <b>(-41.22%)</b></td><td>0.04 <b>(+230.36%)</b></td><td>0.02 <b>(-58.57%)</b></td><td>568.00 <b>(-69.73%)</b></td><td>439.52 <b>(-29.60%)</b></td><td>491.40 <b>(+70.15%)</b></td><td>274.50 <b>(+74.95%)</b></td><td>142.49 <b>(-80.00%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>1876.30 (n/a)</td><td>624.34 (n/a)</td><td>288.80 (n/a)</td><td>156.90 (n/a)</td><td>712.58 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.12 (+11.82%)</td><td>0.08 (+5.31%)</td><td>0.08 (-10.13%)</td><td>0.05 <b>(+33.54%)</b></td><td>0.03 (-9.96%)</td><td>456.60 <b>(-25.12%)</b></td><td>346.06 (-10.94%)</td><td>316.40 (+11.25%)</td><td>211.10 (-10.55%)</td><td>104.31 <b>(-39.09%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>609.80 (n/a)</td><td>388.58 (n/a)</td><td>284.40 (n/a)</td><td>236.00 (n/a)</td><td>171.26 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 (-3.62%)</td><td>0.06 (-8.65%)</td><td>0.06 (+10.44%)</td><td>0.04 (-10.35%)</td><td>0.02 (-8.11%)</td><td>554.00 (+11.54%)</td><td>412.58 (+9.22%)</td><td>392.50 (-9.46%)</td><td>250.80 (+3.76%)</td><td>119.03 (+7.74%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>496.70 (n/a)</td><td>377.76 (n/a)</td><td>433.50 (n/a)</td><td>241.70 (n/a)</td><td>110.48 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (-4.87%)</td><td>0.06 <b>(+33.67%)</b></td><td>0.06 <b>(+64.97%)</b></td><td>0.05 <b>(+108.58%)</b></td><td>0.01 <b>(-49.81%)</b></td><td>498.80 <b>(-52.06%)</b></td><td>390.84 <b>(-36.31%)</b></td><td>381.10 <b>(-39.38%)</b></td><td>298.80 (+5.14%)</td><td>74.34 <b>(-74.07%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1040.50 (n/a)</td><td>613.66 (n/a)</td><td>628.70 (n/a)</td><td>284.20 (n/a)</td><td>286.69 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.23 (+6.54%)</td><td>0.16 (-9.03%)</td><td>0.16 (-11.84%)</td><td>0.11 (+12.70%)</td><td>0.05 (+6.55%)</td><td>463.40 (-11.26%)</td><td>336.08 (+8.76%)</td><td>300.00 (+13.42%)</td><td>209.60 (-6.14%)</td><td>100.36 (-16.86%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>522.20 (n/a)</td><td>309.00 (n/a)</td><td>264.50 (n/a)</td><td>223.30 (n/a)</td><td>120.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.21 (+18.24%)</td><td>0.16 (+19.84%)</td><td>0.18 <b>(+44.33%)</b></td><td>0.09 (+11.69%)</td><td>0.05 <b>(+33.97%)</b></td><td>523.10 (-10.46%)</td><td>346.26 (-14.05%)</td><td>268.10 <b>(-30.71%)</b></td><td>237.10 (-15.41%)</td><td>131.26 (+3.99%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>584.20 (n/a)</td><td>402.88 (n/a)</td><td>386.90 (n/a)</td><td>280.30 (n/a)</td><td>126.22 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.19 (-9.49%)</td><td>0.16 (-5.18%)</td><td>0.17 (+3.64%)</td><td>0.08 (-16.76%)</td><td>0.04 (+6.39%)</td><td>579.80 <b>(+20.14%)</b></td><td>344.70 (+8.54%)</td><td>289.20 (-3.50%)</td><td>252.80 (+10.49%)</td><td>134.77 <b>(+39.29%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>482.60 (n/a)</td><td>317.58 (n/a)</td><td>299.70 (n/a)</td><td>228.80 (n/a)</td><td>96.75 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.22 (+6.58%)</td><td>0.17 (+7.68%)</td><td>0.17 <b>(+20.05%)</b></td><td>0.08 <b>(-35.92%)</b></td><td>0.05 <b>(+74.65%)</b></td><td>602.10 <b>(+56.07%)</b></td><td>333.26 (+2.06%)</td><td>292.30 (-16.72%)</td><td>227.40 (-6.19%)</td><td>154.36 <b>(+166.42%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>385.80 (n/a)</td><td>326.54 (n/a)</td><td>351.00 (n/a)</td><td>242.40 (n/a)</td><td>57.94 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.18 (-10.87%)</td><td>0.14 (+12.15%)</td><td>0.14 (+19.27%)</td><td>0.10 (+17.00%)</td><td>0.03 <b>(-28.22%)</b></td><td>468.20 (-14.52%)</td><td>362.08 (-13.87%)</td><td>362.70 (-16.16%)</td><td>270.20 (+12.21%)</td><td>81.73 <b>(-26.69%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>547.70 (n/a)</td><td>420.40 (n/a)</td><td>432.60 (n/a)</td><td>240.80 (n/a)</td><td>111.49 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.20 <b>(+21.32%)</b></td><td>0.16 <b>(+48.32%)</b></td><td>0.19 <b>(+70.62%)</b></td><td>0.10 <b>(+294.71%)</b></td><td>0.06 (+1.51%)</td><td>505.60 <b>(-74.66%)</b></td><td>348.56 <b>(-51.89%)</b></td><td>253.70 <b>(-41.40%)</b></td><td>240.60 (-17.57%)</td><td>139.05 <b>(-80.60%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1995.50 (n/a)</td><td>724.58 (n/a)</td><td>432.90 (n/a)</td><td>291.90 (n/a)</td><td>716.88 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (-14.77%)</td><td>0.01 (-12.03%)</td><td>0.01 (-8.49%)</td><td>0.00 (-15.69%)</td><td>0.00 (-14.86%)</td><td>593.90 (+18.61%)</td><td>343.70 (+14.17%)</td><td>304.60 (+9.25%)</td><td>234.10 (+17.34%)</td><td>143.27 <b>(+21.77%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.70 (n/a)</td><td>301.04 (n/a)</td><td>278.80 (n/a)</td><td>199.50 (n/a)</td><td>117.66 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (+17.46%)</td><td>0.01 <b>(+40.49%)</b></td><td>0.01 (+15.58%)</td><td>0.01 <b>(+416.78%)</b></td><td>0.00 <b>(-24.59%)</b></td><td>480.10 <b>(-80.65%)</b></td><td>374.92 <b>(-55.57%)</b></td><td>417.70 (-13.48%)</td><td>250.20 (-14.87%)</td><td>96.56 <b>(-89.50%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2481.10 (n/a)</td><td>843.90 (n/a)</td><td>482.80 (n/a)</td><td>293.90 (n/a)</td><td>919.49 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (+3.66%)</td><td>0.01 (-9.24%)</td><td>0.01 <b>(-31.96%)</b></td><td>0.00 (+2.73%)</td><td>0.00 (-18.96%)</td><td>534.60 (-2.66%)</td><td>375.64 (+4.59%)</td><td>362.80 <b>(+46.94%)</b></td><td>232.90 (-3.52%)</td><td>121.74 <b>(-22.37%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>549.20 (n/a)</td><td>359.16 (n/a)</td><td>246.90 (n/a)</td><td>241.40 (n/a)</td><td>156.82 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 <b>(-24.80%)</b></td><td>0.01 (-6.64%)</td><td>0.01 (+7.79%)</td><td>0.01 <b>(+30.43%)</b></td><td>0.00 <b>(-42.32%)</b></td><td>491.00 <b>(-23.33%)</b></td><td>348.02 (-6.79%)</td><td>280.80 (-7.23%)</td><td>241.80 <b>(+33.00%)</b></td><td>117.88 <b>(-40.47%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>640.40 (n/a)</td><td>373.36 (n/a)</td><td>302.70 (n/a)</td><td>181.80 (n/a)</td><td>198.02 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (+8.12%)</td><td>0.01 (-16.41%)</td><td>0.01 (-6.96%)</td><td>0.00 (-16.13%)</td><td>0.00 (+8.30%)</td><td>562.10 (+19.24%)</td><td>456.44 <b>(+22.19%)</b></td><td>468.00 (+7.49%)</td><td>230.50 (-7.50%)</td><td>134.30 (+18.00%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>471.40 (n/a)</td><td>373.54 (n/a)</td><td>435.40 (n/a)</td><td>249.20 (n/a)</td><td>113.81 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (+9.18%)</td><td>0.01 (+1.02%)</td><td>0.01 <b>(-20.81%)</b></td><td>0.00 <b>(+32.27%)</b></td><td>0.00 (-7.89%)</td><td>579.50 <b>(-24.40%)</b></td><td>422.26 (-6.38%)</td><td>429.00 <b>(+26.29%)</b></td><td>257.60 (-8.39%)</td><td>127.83 <b>(-37.12%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>766.50 (n/a)</td><td>451.04 (n/a)</td><td>339.70 (n/a)</td><td>281.20 (n/a)</td><td>203.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (-6.13%)</td><td>0.01 (-2.94%)</td><td>0.01 (-18.51%)</td><td>0.01 (+12.49%)</td><td>0.01 (-2.13%)</td><td>511.80 (-11.10%)</td><td>398.12 (+2.23%)</td><td>475.50 <b>(+22.74%)</b></td><td>259.90 (+6.56%)</td><td>126.72 (-8.13%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.70 (n/a)</td><td>389.44 (n/a)</td><td>387.40 (n/a)</td><td>243.90 (n/a)</td><td>137.94 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 <b>(-22.75%)</b></td><td>0.01 (-4.41%)</td><td>0.01 (-6.80%)</td><td>0.01 (-1.76%)</td><td>0.01 <b>(-20.20%)</b></td><td>608.30 (+1.79%)</td><td>445.28 (+2.18%)</td><td>491.50 (+7.31%)</td><td>281.50 <b>(+29.48%)</b></td><td>154.98 (-0.93%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.60 (n/a)</td><td>435.76 (n/a)</td><td>458.00 (n/a)</td><td>217.40 (n/a)</td><td>156.44 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (-6.99%)</td><td>0.01 (+10.00%)</td><td>0.01 (+13.12%)</td><td>0.01 (+3.79%)</td><td>0.00 (-2.81%)</td><td>783.40 (-3.65%)</td><td>444.66 (-8.83%)</td><td>400.10 (-11.60%)</td><td>282.30 (+7.50%)</td><td>201.67 (+0.84%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>813.10 (n/a)</td><td>487.74 (n/a)</td><td>452.60 (n/a)</td><td>262.60 (n/a)</td><td>199.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (-9.20%)</td><td>0.01 (-11.43%)</td><td>0.01 (+1.81%)</td><td>0.00 <b>(-48.02%)</b></td><td>0.00 <b>(+24.74%)</b></td><td>1826.70 <b>(+92.39%)</b></td><td>803.16 <b>(+37.42%)</b></td><td>530.90 (-1.78%)</td><td>389.50 (+10.12%)</td><td>591.65 <b>(+169.60%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>949.50 (n/a)</td><td>584.44 (n/a)</td><td>540.50 (n/a)</td><td>353.70 (n/a)</td><td>219.46 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 <b>(+61.65%)</b></td><td>0.02 <b>(+45.05%)</b></td><td>0.02 <b>(+50.60%)</b></td><td>0.01 (-1.59%)</td><td>0.00 <b>(+215.25%)</b></td><td>524.20 (+1.61%)</td><td>329.16 <b>(-26.51%)</b></td><td>285.20 <b>(-33.60%)</b></td><td>233.00 <b>(-38.13%)</b></td><td>114.27 <b>(+107.28%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.90 (n/a)</td><td>447.92 (n/a)</td><td>429.50 (n/a)</td><td>376.60 (n/a)</td><td>55.13 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (+1.03%)</td><td>0.01 (+2.38%)</td><td>0.01 (+3.97%)</td><td>0.01 (+5.04%)</td><td>0.00 (-0.60%)</td><td>521.00 (-4.81%)</td><td>425.80 (-2.69%)</td><td>441.40 (-3.81%)</td><td>239.80 (-1.03%)</td><td>112.85 (-4.01%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.30 (n/a)</td><td>437.56 (n/a)</td><td>458.90 (n/a)</td><td>242.30 (n/a)</td><td>117.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 <b>(+37.92%)</b></td><td>0.03 (+12.62%)</td><td>0.02 (-7.17%)</td><td>0.02 (-12.65%)</td><td>0.02 <b>(+115.84%)</b></td><td>598.80 (+14.49%)</td><td>409.84 (+1.45%)</td><td>464.80 (+7.74%)</td><td>210.70 <b>(-27.49%)</b></td><td>177.39 <b>(+78.66%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.00 (n/a)</td><td>403.98 (n/a)</td><td>431.40 (n/a)</td><td>290.60 (n/a)</td><td>99.29 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 <b>(+27.65%)</b></td><td>0.03 (+1.06%)</td><td>0.02 (+4.43%)</td><td>0.02 (+2.82%)</td><td>0.02 <b>(+41.33%)</b></td><td>583.50 (-2.75%)</td><td>442.48 (+3.90%)</td><td>460.60 (-4.24%)</td><td>191.20 <b>(-21.64%)</b></td><td>156.15 (+5.08%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.00 (n/a)</td><td>425.88 (n/a)</td><td>481.00 (n/a)</td><td>244.00 (n/a)</td><td>148.60 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (+11.61%)</td><td>0.03 (+6.70%)</td><td>0.03 (-1.71%)</td><td>0.02 <b>(+24.20%)</b></td><td>0.01 (+4.94%)</td><td>587.40 (-19.49%)</td><td>379.90 (-8.71%)</td><td>333.40 (+1.74%)</td><td>226.80 (-10.39%)</td><td>161.52 <b>(-21.41%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>729.60 (n/a)</td><td>416.16 (n/a)</td><td>327.70 (n/a)</td><td>253.10 (n/a)</td><td>205.52 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (+17.71%)</td><td>0.03 <b>(+37.54%)</b></td><td>0.03 <b>(+76.27%)</b></td><td>0.02 (-0.70%)</td><td>0.01 <b>(+35.12%)</b></td><td>601.50 (+0.70%)</td><td>364.18 <b>(-22.88%)</b></td><td>300.30 <b>(-43.28%)</b></td><td>208.80 (-15.05%)</td><td>167.34 <b>(+22.92%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>597.30 (n/a)</td><td>472.22 (n/a)</td><td>529.40 (n/a)</td><td>245.80 (n/a)</td><td>136.14 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 <b>(-23.85%)</b></td><td>0.03 (+4.73%)</td><td>0.03 <b>(+28.61%)</b></td><td>0.02 (+15.31%)</td><td>0.01 <b>(-26.61%)</b></td><td>521.40 (-13.27%)</td><td>359.78 (-8.36%)</td><td>306.50 <b>(-22.25%)</b></td><td>244.00 <b>(+31.32%)</b></td><td>131.85 (-10.79%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.20 (n/a)</td><td>392.62 (n/a)</td><td>394.20 (n/a)</td><td>185.80 (n/a)</td><td>147.79 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 <b>(-46.80%)</b></td><td>0.02 <b>(-24.20%)</b></td><td>0.02 (-14.82%)</td><td>0.02 (+0.02%)</td><td>0.01 <b>(-63.72%)</b></td><td>643.50 (-0.02%)</td><td>525.78 (+10.86%)</td><td>576.20 (+17.38%)</td><td>307.90 <b>(+87.97%)</b></td><td>133.60 <b>(-28.49%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>643.60 (n/a)</td><td>474.26 (n/a)</td><td>490.90 (n/a)</td><td>163.80 (n/a)</td><td>186.82 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (+12.49%)</td><td>0.06 (+2.21%)</td><td>0.07 (+11.31%)</td><td>0.04 (-15.06%)</td><td>0.02 <b>(+77.15%)</b></td><td>551.10 (+17.73%)</td><td>377.80 (+6.20%)</td><td>286.50 (-10.16%)</td><td>247.70 (-11.09%)</td><td>149.84 <b>(+91.67%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>468.10 (n/a)</td><td>355.76 (n/a)</td><td>318.90 (n/a)</td><td>278.60 (n/a)</td><td>78.18 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (-10.42%)</td><td>0.07 <b>(+27.63%)</b></td><td>0.07 <b>(+68.21%)</b></td><td>0.04 (+12.13%)</td><td>0.02 <b>(-27.78%)</b></td><td>526.40 (-10.81%)</td><td>326.78 <b>(-25.64%)</b></td><td>284.70 <b>(-40.55%)</b></td><td>244.90 (+11.62%)</td><td>114.41 <b>(-22.68%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>590.20 (n/a)</td><td>439.44 (n/a)</td><td>478.90 (n/a)</td><td>219.40 (n/a)</td><td>147.97 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (+17.86%)</td><td>0.07 <b>(+46.99%)</b></td><td>0.08 <b>(+105.94%)</b></td><td>0.04 <b>(+41.82%)</b></td><td>0.02 <b>(+29.32%)</b></td><td>496.70 <b>(-29.50%)</b></td><td>342.54 <b>(-31.07%)</b></td><td>255.60 <b>(-51.44%)</b></td><td>231.20 (-15.16%)</td><td>132.17 (-15.58%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>704.50 (n/a)</td><td>496.94 (n/a)</td><td>526.40 (n/a)</td><td>272.50 (n/a)</td><td>156.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (+3.97%)</td><td>0.05 (+9.78%)</td><td>0.05 (+4.08%)</td><td>0.04 <b>(+22.93%)</b></td><td>0.02 (-8.06%)</td><td>522.90 (-18.64%)</td><td>403.64 (-11.30%)</td><td>417.30 (-3.91%)</td><td>255.90 (-3.83%)</td><td>96.83 <b>(-28.82%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>642.70 (n/a)</td><td>455.04 (n/a)</td><td>434.30 (n/a)</td><td>266.10 (n/a)</td><td>136.04 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (-0.84%)</td><td>0.07 (+0.75%)</td><td>0.08 (-4.08%)</td><td>0.04 (-16.11%)</td><td>0.02 (-7.41%)</td><td>519.40 (+19.21%)</td><td>326.92 (-0.51%)</td><td>274.90 (+4.29%)</td><td>251.90 (+0.88%)</td><td>110.19 (+12.87%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>435.70 (n/a)</td><td>328.60 (n/a)</td><td>263.60 (n/a)</td><td>249.70 (n/a)</td><td>97.62 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (+13.06%)</td><td>0.05 (-1.38%)</td><td>0.05 (-3.45%)</td><td>0.03 (-11.26%)</td><td>0.02 <b>(+46.05%)</b></td><td>635.60 (+12.70%)</td><td>467.66 (+8.51%)</td><td>460.80 (+3.57%)</td><td>241.50 (-11.54%)</td><td>165.89 <b>(+55.87%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>564.00 (n/a)</td><td>431.00 (n/a)</td><td>444.90 (n/a)</td><td>273.00 (n/a)</td><td>106.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>482.20 (n/a)</td><td>413.02 (n/a)</td><td>461.40 (n/a)</td><td>222.20 (n/a)</td><td>108.64 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.00 (n/a)</td><td>393.04 (n/a)</td><td>434.70 (n/a)</td><td>214.60 (n/a)</td><td>161.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>441.30 (n/a)</td><td>324.30 (n/a)</td><td>297.30 (n/a)</td><td>283.40 (n/a)</td><td>66.22 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>604.70 (n/a)</td><td>421.68 (n/a)</td><td>483.10 (n/a)</td><td>205.60 (n/a)</td><td>167.84 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>505.10 (n/a)</td><td>327.66 (n/a)</td><td>322.30 (n/a)</td><td>198.00 (n/a)</td><td>121.69 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>486.80 (n/a)</td><td>406.20 (n/a)</td><td>398.60 (n/a)</td><td>281.60 (n/a)</td><td>82.61 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>745.30 (n/a)</td><td>478.58 (n/a)</td><td>450.80 (n/a)</td><td>266.20 (n/a)</td><td>172.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>585.90 (n/a)</td><td>499.34 (n/a)</td><td>556.20 (n/a)</td><td>315.40 (n/a)</td><td>110.52 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>609.50 (n/a)</td><td>488.24 (n/a)</td><td>532.60 (n/a)</td><td>286.30 (n/a)</td><td>122.93 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.21 (+3.57%)</td><td>0.14 (+14.67%)</td><td>0.11 (+9.61%)</td><td>0.07 (+16.29%)</td><td>0.06 (+3.39%)</td><td>669.60 (-14.01%)</td><td>415.52 (-15.00%)</td><td>433.70 (-8.77%)</td><td>233.50 (-3.47%)</td><td>179.26 (-18.76%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>778.70 (n/a)</td><td>488.86 (n/a)</td><td>475.40 (n/a)</td><td>241.90 (n/a)</td><td>220.65 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>493.80 (n/a)</td><td>425.00 (n/a)</td><td>402.40 (n/a)</td><td>364.30 (n/a)</td><td>63.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>535.50 (n/a)</td><td>431.54 (n/a)</td><td>443.90 (n/a)</td><td>319.30 (n/a)</td><td>84.72 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>535.40 (n/a)</td><td>321.54 (n/a)</td><td>246.50 (n/a)</td><td>226.30 (n/a)</td><td>129.75 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>287.20 (n/a)</td><td>237.22 (n/a)</td><td>238.90 (n/a)</td><td>191.50 (n/a)</td><td>34.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>494.90 (n/a)</td><td>301.30 (n/a)</td><td>258.60 (n/a)</td><td>202.20 (n/a)</td><td>113.32 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>271.80 (n/a)</td><td>231.64 (n/a)</td><td>244.70 (n/a)</td><td>188.70 (n/a)</td><td>34.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.50 (n/a)</td><td>332.40 (n/a)</td><td>298.90 (n/a)</td><td>210.80 (n/a)</td><td>125.76 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>596.50 (n/a)</td><td>357.74 (n/a)</td><td>248.20 (n/a)</td><td>213.00 (n/a)</td><td>173.87 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>572.00 (n/a)</td><td>359.68 (n/a)</td><td>300.80 (n/a)</td><td>248.30 (n/a)</td><td>134.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>487.70 (n/a)</td><td>418.72 (n/a)</td><td>421.20 (n/a)</td><td>312.50 (n/a)</td><td>68.19 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>662.60 (n/a)</td><td>441.98 (n/a)</td><td>350.70 (n/a)</td><td>282.10 (n/a)</td><td>175.63 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>488.70 (n/a)</td><td>373.86 (n/a)</td><td>365.80 (n/a)</td><td>254.80 (n/a)</td><td>103.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>496.80 (n/a)</td><td>426.26 (n/a)</td><td>475.70 (n/a)</td><td>243.60 (n/a)</td><td>106.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1960.60 (n/a)</td><td>683.58 (n/a)</td><td>313.90 (n/a)</td><td>281.70 (n/a)</td><td>723.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>549.00 (n/a)</td><td>451.42 (n/a)</td><td>475.40 (n/a)</td><td>279.40 (n/a)</td><td>101.37 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2416.90 (n/a)</td><td>1130.72 (n/a)</td><td>486.30 (n/a)</td><td>345.90 (n/a)</td><td>977.89 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>605.70 (n/a)</td><td>448.40 (n/a)</td><td>455.70 (n/a)</td><td>299.90 (n/a)</td><td>143.05 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>445.60 (n/a)</td><td>315.74 (n/a)</td><td>263.20 (n/a)</td><td>237.10 (n/a)</td><td>94.91 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1038.30 (n/a)</td><td>472.48 (n/a)</td><td>323.90 (n/a)</td><td>272.10 (n/a)</td><td>321.29 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.20 (n/a)</td><td>388.52 (n/a)</td><td>351.40 (n/a)</td><td>240.70 (n/a)</td><td>155.04 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.00 (n/a)</td><td>404.28 (n/a)</td><td>330.20 (n/a)</td><td>230.40 (n/a)</td><td>168.26 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.90 (n/a)</td><td>367.58 (n/a)</td><td>317.70 (n/a)</td><td>226.50 (n/a)</td><td>122.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>767.00 (n/a)</td><td>510.98 (n/a)</td><td>516.80 (n/a)</td><td>248.80 (n/a)</td><td>187.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.90 (n/a)</td><td>404.06 (n/a)</td><td>426.60 (n/a)</td><td>230.80 (n/a)</td><td>150.90 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1072.20 (n/a)</td><td>589.56 (n/a)</td><td>460.60 (n/a)</td><td>380.00 (n/a)</td><td>278.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>398.10 (n/a)</td><td>318.44 (n/a)</td><td>308.20 (n/a)</td><td>257.70 (n/a)</td><td>51.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>798.40 (n/a)</td><td>485.80 (n/a)</td><td>428.00 (n/a)</td><td>267.30 (n/a)</td><td>224.42 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>549.60 (n/a)</td><td>407.94 (n/a)</td><td>425.70 (n/a)</td><td>275.40 (n/a)</td><td>113.54 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>514.30 (n/a)</td><td>423.96 (n/a)</td><td>489.80 (n/a)</td><td>198.50 (n/a)</td><td>130.86 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>606.40 (n/a)</td><td>424.82 (n/a)</td><td>414.60 (n/a)</td><td>220.60 (n/a)</td><td>151.61 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>669.00 (n/a)</td><td>456.26 (n/a)</td><td>465.50 (n/a)</td><td>222.20 (n/a)</td><td>158.36 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>498.00 (n/a)</td><td>441.70 (n/a)</td><td>467.30 (n/a)</td><td>321.60 (n/a)</td><td>73.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2134.50 (n/a)</td><td>785.84 (n/a)</td><td>503.50 (n/a)</td><td>217.20 (n/a)</td><td>768.10 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2491.30 (n/a)</td><td>869.78 (n/a)</td><td>520.10 (n/a)</td><td>297.90 (n/a)</td><td>911.55 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>643.50 (n/a)</td><td>384.10 (n/a)</td><td>337.00 (n/a)</td><td>235.60 (n/a)</td><td>154.05 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1383.10 (n/a)</td><td>664.02 (n/a)</td><td>534.50 (n/a)</td><td>307.50 (n/a)</td><td>418.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.54 (-16.57%)</td><td>0.50 <b>(+23.73%)</b></td><td>0.51 <b>(+21.45%)</b></td><td>0.47 <b>(+83.16%)</b></td><td>0.04 <b>(-78.21%)</b></td><td>474.80 <b>(-45.40%)</b></td><td>439.86 <b>(-28.51%)</b></td><td>433.10 (-17.66%)</td><td>407.50 (+19.89%)</td><td>31.39 <b>(-86.72%)</b></td><td>23.16 (-16.57%)</td><td>21.54 <b>(+23.73%)</b></td><td>21.79 <b>(+21.45%)</b></td><td>19.88 <b>(+83.16%)</b></td><td>1.52 <b>(-78.21%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.65 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>869.60 (n/a)</td><td>615.24 (n/a)</td><td>526.00 (n/a)</td><td>339.90 (n/a)</td><td>236.45 (n/a)</td><td>27.76 (n/a)</td><td>17.41 (n/a)</td><td>17.94 (n/a)</td><td>10.85 (n/a)</td><td>6.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.61 <b>(-21.26%)</b></td><td>0.42 (-18.48%)</td><td>0.52 <b>(+23.35%)</b></td><td>0.12 <b>(-64.48%)</b></td><td>0.20 (+4.40%)</td><td>1783.60 <b>(+181.50%)</b></td><td>742.56 <b>(+55.93%)</b></td><td>421.90 (-18.93%)</td><td>361.40 <b>(+27.03%)</b></td><td>601.46 <b>(+272.97%)</b></td><td>26.11 <b>(-21.26%)</b></td><td>17.98 (-18.48%)</td><td>22.37 <b>(+23.35%)</b></td><td>5.29 <b>(-64.48%)</b></td><td>8.71 (+4.40%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.78 (n/a)</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.20 (n/a)</td><td>633.60 (n/a)</td><td>476.22 (n/a)</td><td>520.40 (n/a)</td><td>284.50 (n/a)</td><td>161.26 (n/a)</td><td>33.17 (n/a)</td><td>22.05 (n/a)</td><td>18.13 (n/a)</td><td>14.89 (n/a)</td><td>8.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.31 (-1.15%)</td><td>0.30 (-0.09%)</td><td>0.30 (-0.16%)</td><td>0.30 (+0.59%)</td><td>0.00 <b>(-26.38%)</b></td><td>85027.90 (-0.58%)</td><td>82993.30 (+0.07%)</td><td>82909.30 (+0.16%)</td><td>81738.10 (+1.16%)</td><td>1247.57 <b>(-25.98%)</b></td><td>210.18 (-1.15%)</td><td>207.04 (-0.09%)</td><td>207.21 (-0.16%)</td><td>202.05 (+0.59%)</td><td>3.08 <b>(-26.38%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85528.00 (n/a)</td><td>82931.28 (n/a)</td><td>82776.50 (n/a)</td><td>80802.10 (n/a)</td><td>1685.38 (n/a)</td><td>212.62 (n/a)</td><td>207.23 (n/a)</td><td>207.55 (n/a)</td><td>200.87 (n/a)</td><td>4.18 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.03 (+2.25%)</td><td>1.03 (+4.66%)</td><td>1.03 (+3.13%)</td><td>1.02 (+11.47%)</td><td>0.01 <b>(-82.78%)</b></td><td>24784.00 (-10.29%)</td><td>24540.20 (-4.58%)</td><td>24550.10 (-3.04%)</td><td>24378.60 (-2.20%)</td><td>165.73 <b>(-84.98%)</b></td><td>704.71 (+2.25%)</td><td>700.10 (+4.66%)</td><td>699.79 (+3.13%)</td><td>693.18 (+11.47%)</td><td>4.72 <b>(-82.78%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>1.01 (n/a)</td><td>0.98 (n/a)</td><td>0.99 (n/a)</td><td>0.91 (n/a)</td><td>0.04 (n/a)</td><td>27627.20 (n/a)</td><td>25718.46 (n/a)</td><td>25319.60 (n/a)</td><td>24927.40 (n/a)</td><td>1103.21 (n/a)</td><td>689.20 (n/a)</td><td>668.94 (n/a)</td><td>678.52 (n/a)</td><td>621.85 (n/a)</td><td>27.38 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.82 (+0.45%)</td><td>0.80 (+1.59%)</td><td>0.80 (+1.82%)</td><td>0.79 (+2.35%)</td><td>0.01 <b>(-34.98%)</b></td><td>95808.90 (-2.29%)</td><td>94144.46 (-1.59%)</td><td>94165.40 (-1.79%)</td><td>92440.30 (-0.45%)</td><td>1195.61 <b>(-36.66%)</b></td><td>743.39 (+0.45%)</td><td>730.03 (+1.59%)</td><td>729.77 (+1.82%)</td><td>717.26 (+2.35%)</td><td>9.28 <b>(-34.98%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.02 (n/a)</td><td>98058.30 (n/a)</td><td>95662.44 (n/a)</td><td>95883.30 (n/a)</td><td>92853.50 (n/a)</td><td>1887.55 (n/a)</td><td>740.08 (n/a)</td><td>718.58 (n/a)</td><td>716.70 (n/a)</td><td>700.80 (n/a)</td><td>14.27 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.77 (+0.17%)</td><td>0.76 (+0.31%)</td><td>0.76 (+0.58%)</td><td>0.75 (+0.02%)</td><td>0.01 (+12.93%)</td><td>100276.40 (-0.02%)</td><td>99025.54 (-0.31%)</td><td>98900.50 (-0.58%)</td><td>98180.90 (-0.17%)</td><td>839.70 (+12.75%)</td><td>699.93 (+0.17%)</td><td>694.00 (+0.31%)</td><td>694.83 (+0.58%)</td><td>685.30 (+0.02%)</td><td>5.86 (+12.93%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100291.50 (n/a)</td><td>99334.16 (n/a)</td><td>99474.00 (n/a)</td><td>98352.60 (n/a)</td><td>744.78 (n/a)</td><td>698.71 (n/a)</td><td>691.83 (n/a)</td><td>690.83 (n/a)</td><td>685.20 (n/a)</td><td>5.19 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.80 (+1.62%)</td><td>0.79 (+1.56%)</td><td>0.79 (+1.56%)</td><td>0.78 (+2.03%)</td><td>0.00 <b>(-22.85%)</b></td><td>96304.70 (-1.99%)</td><td>95772.16 (-1.54%)</td><td>95882.30 (-1.54%)</td><td>94923.30 (-1.60%)</td><td>510.03 <b>(-25.69%)</b></td><td>723.95 (+1.62%)</td><td>717.55 (+1.56%)</td><td>716.71 (+1.56%)</td><td>713.56 (+2.03%)</td><td>3.84 <b>(-22.85%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>98263.80 (n/a)</td><td>97266.42 (n/a)</td><td>97379.00 (n/a)</td><td>96465.40 (n/a)</td><td>686.38 (n/a)</td><td>712.37 (n/a)</td><td>706.54 (n/a)</td><td>705.69 (n/a)</td><td>699.34 (n/a)</td><td>4.98 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.52 (+5.55%)</td><td>4.42 <b>(+24.35%)</b></td><td>4.52 (+10.05%)</td><td>2.80 <b>(+30.33%)</b></td><td>1.11 (-17.87%)</td><td>3177.70 <b>(-23.27%)</b></td><td>2142.16 <b>(-25.11%)</b></td><td>1970.50 (-9.13%)</td><td>1614.50 (-5.25%)</td><td>637.68 <b>(-45.86%)</b></td><td>332.54 (+5.55%)</td><td>266.29 <b>(+24.35%)</b></td><td>272.45 (+10.05%)</td><td>168.95 <b>(+30.33%)</b></td><td>67.07 (-17.87%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>5.23 (n/a)</td><td>3.56 (n/a)</td><td>4.11 (n/a)</td><td>2.15 (n/a)</td><td>1.36 (n/a)</td><td>4141.40 (n/a)</td><td>2860.54 (n/a)</td><td>2168.50 (n/a)</td><td>1704.00 (n/a)</td><td>1177.89 (n/a)</td><td>315.06 (n/a)</td><td>214.14 (n/a)</td><td>247.58 (n/a)</td><td>129.63 (n/a)</td><td>81.67 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.52 (-11.90%)</td><td>3.10 <b>(-20.11%)</b></td><td>2.91 <b>(-31.20%)</b></td><td>2.25 (-1.98%)</td><td>0.86 (-19.07%)</td><td>3970.00 (+2.02%)</td><td>3035.08 <b>(+22.45%)</b></td><td>3059.00 <b>(+45.36%)</b></td><td>1971.00 (+13.51%)</td><td>728.65 (-13.54%)</td><td>272.39 (-11.90%)</td><td>186.58 <b>(-20.11%)</b></td><td>175.51 <b>(-31.20%)</b></td><td>135.23 (-1.98%)</td><td>51.85 (-19.07%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>5.13 (n/a)</td><td>3.88 (n/a)</td><td>4.24 (n/a)</td><td>2.29 (n/a)</td><td>1.06 (n/a)</td><td>3891.50 (n/a)</td><td>2478.58 (n/a)</td><td>2104.50 (n/a)</td><td>1736.40 (n/a)</td><td>842.74 (n/a)</td><td>309.19 (n/a)</td><td>233.55 (n/a)</td><td>255.10 (n/a)</td><td>137.96 (n/a)</td><td>64.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.17 (-1.82%)</td><td>3.45 (+5.27%)</td><td>3.70 <b>(+39.18%)</b></td><td>1.93 (-11.54%)</td><td>1.34 (-0.36%)</td><td>4614.30 (+13.05%)</td><td>2957.38 (-3.55%)</td><td>2410.20 <b>(-28.15%)</b></td><td>1725.00 (+1.85%)</td><td>1238.42 (+14.87%)</td><td>311.23 (-1.82%)</td><td>207.88 (+5.27%)</td><td>222.75 <b>(+39.18%)</b></td><td>116.35 (-11.54%)</td><td>80.82 (-0.36%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>5.26 (n/a)</td><td>3.28 (n/a)</td><td>2.66 (n/a)</td><td>2.18 (n/a)</td><td>1.35 (n/a)</td><td>4081.80 (n/a)</td><td>3066.20 (n/a)</td><td>3354.60 (n/a)</td><td>1693.60 (n/a)</td><td>1078.10 (n/a)</td><td>317.01 (n/a)</td><td>197.47 (n/a)</td><td>160.04 (n/a)</td><td>131.53 (n/a)</td><td>81.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.96 (-12.38%)</td><td>5.47 (+6.16%)</td><td>5.56 (+15.69%)</td><td>4.73 (+12.10%)</td><td>0.52 <b>(-47.31%)</b></td><td>7369.90 (-10.80%)</td><td>6418.48 (-7.46%)</td><td>6271.40 (-13.56%)</td><td>5847.20 (+14.14%)</td><td>634.35 <b>(-44.77%)</b></td><td>367.27 (-12.38%)</td><td>337.09 (+6.16%)</td><td>342.43 (+15.69%)</td><td>291.39 (+12.10%)</td><td>31.82 <b>(-47.31%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>6.81 (n/a)</td><td>5.16 (n/a)</td><td>4.81 (n/a)</td><td>4.22 (n/a)</td><td>0.98 (n/a)</td><td>8262.00 (n/a)</td><td>6936.00 (n/a)</td><td>7255.60 (n/a)</td><td>5123.00 (n/a)</td><td>1148.56 (n/a)</td><td>419.18 (n/a)</td><td>317.53 (n/a)</td><td>295.98 (n/a)</td><td>259.92 (n/a)</td><td>60.39 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.34 (+1.85%)</td><td>4.77 (+0.88%)</td><td>4.57 (-5.68%)</td><td>4.30 (+13.87%)</td><td>0.45 <b>(-23.83%)</b></td><td>8105.20 (-12.18%)</td><td>7353.90 (-1.57%)</td><td>7628.60 (+6.02%)</td><td>6532.90 (-1.82%)</td><td>676.57 <b>(-35.39%)</b></td><td>328.72 (+1.85%)</td><td>294.06 (+0.88%)</td><td>281.51 (-5.68%)</td><td>264.95 (+13.87%)</td><td>27.68 <b>(-23.83%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>5.24 (n/a)</td><td>4.73 (n/a)</td><td>4.85 (n/a)</td><td>3.78 (n/a)</td><td>0.59 (n/a)</td><td>9229.40 (n/a)</td><td>7471.12 (n/a)</td><td>7195.20 (n/a)</td><td>6654.00 (n/a)</td><td>1047.10 (n/a)</td><td>322.74 (n/a)</td><td>291.50 (n/a)</td><td>298.46 (n/a)</td><td>232.68 (n/a)</td><td>36.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>6.62 (+0.61%)</td><td>6.16 (+9.44%)</td><td>6.15 (+13.80%)</td><td>5.70 (+12.46%)</td><td>0.33 <b>(-47.59%)</b></td><td>6120.40 (-11.08%)</td><td>5669.28 (-9.28%)</td><td>5664.70 (-12.13%)</td><td>5269.10 (-0.60%)</td><td>305.81 <b>(-53.69%)</b></td><td>407.56 (+0.61%)</td><td>379.67 (+9.44%)</td><td>379.10 (+13.80%)</td><td>350.87 (+12.46%)</td><td>20.32 <b>(-47.59%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>6.58 (n/a)</td><td>5.63 (n/a)</td><td>5.41 (n/a)</td><td>5.07 (n/a)</td><td>0.63 (n/a)</td><td>6882.70 (n/a)</td><td>6249.30 (n/a)</td><td>6446.60 (n/a)</td><td>5301.10 (n/a)</td><td>660.34 (n/a)</td><td>405.10 (n/a)</td><td>346.90 (n/a)</td><td>333.12 (n/a)</td><td>312.01 (n/a)</td><td>38.76 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.79 (+1.01%)</td><td>0.77 (+0.53%)</td><td>0.76 (-0.73%)</td><td>0.76 (+3.16%)</td><td>0.01 <b>(-28.70%)</b></td><td>99727.40 (-3.06%)</td><td>98127.68 (-0.55%)</td><td>98706.40 (+0.74%)</td><td>95539.10 (-1.00%)</td><td>1666.34 <b>(-32.04%)</b></td><td>719.28 (+1.01%)</td><td>700.47 (+0.53%)</td><td>696.20 (-0.73%)</td><td>689.07 (+3.16%)</td><td>12.03 <b>(-28.70%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>102875.30 (n/a)</td><td>98672.68 (n/a)</td><td>97984.70 (n/a)</td><td>96505.70 (n/a)</td><td>2451.83 (n/a)</td><td>712.08 (n/a)</td><td>696.77 (n/a)</td><td>701.33 (n/a)</td><td>667.99 (n/a)</td><td>16.88 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.78 (+0.67%)</td><td>0.76 (+0.82%)</td><td>0.77 (+1.99%)</td><td>0.74 (-0.76%)</td><td>0.02 <b>(+31.47%)</b></td><td>102398.20 (+0.76%)</td><td>98972.66 (-0.79%)</td><td>97722.00 (-1.95%)</td><td>96881.40 (-0.66%)</td><td>2369.61 <b>(+31.18%)</b></td><td>709.32 (+0.67%)</td><td>694.64 (+0.82%)</td><td>703.21 (+1.99%)</td><td>671.10 (-0.76%)</td><td>16.42 <b>(+31.47%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101621.70 (n/a)</td><td>99763.34 (n/a)</td><td>99668.40 (n/a)</td><td>97529.50 (n/a)</td><td>1806.43 (n/a)</td><td>704.60 (n/a)</td><td>689.01 (n/a)</td><td>689.48 (n/a)</td><td>676.23 (n/a)</td><td>12.49 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.81 (+1.42%)</td><td>0.80 (+1.63%)</td><td>0.80 (+1.83%)</td><td>0.80 (+2.05%)</td><td>0.00 <b>(-30.82%)</b></td><td>94321.10 (-2.01%)</td><td>93838.64 (-1.60%)</td><td>93787.20 (-1.80%)</td><td>93291.70 (-1.40%)</td><td>434.08 <b>(-33.10%)</b></td><td>736.61 (+1.42%)</td><td>732.33 (+1.63%)</td><td>732.72 (+1.83%)</td><td>728.57 (+2.05%)</td><td>3.39 <b>(-30.82%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96255.60 (n/a)</td><td>95368.28 (n/a)</td><td>95505.00 (n/a)</td><td>94619.20 (n/a)</td><td>648.81 (n/a)</td><td>726.27 (n/a)</td><td>720.60 (n/a)</td><td>719.54 (n/a)</td><td>713.93 (n/a)</td><td>4.90 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.88 (+9.89%)</td><td>2.95 <b>(+20.72%)</b></td><td>3.52 <b>(+95.99%)</b></td><td>1.65 (-4.09%)</td><td>1.12 <b>(+20.49%)</b></td><td>4887.60 (+4.26%)</td><td>3148.88 (-14.20%)</td><td>2291.60 <b>(-48.98%)</b></td><td>2078.30 (-9.00%)</td><td>1380.18 (+12.89%)</td><td>1017.14 (+9.89%)</td><td>773.46 <b>(+20.72%)</b></td><td>922.47 <b>(+95.99%)</b></td><td>432.51 (-4.09%)</td><td>292.61 <b>(+20.49%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>3.53 (n/a)</td><td>2.44 (n/a)</td><td>1.79 (n/a)</td><td>1.72 (n/a)</td><td>0.93 (n/a)</td><td>4687.80 (n/a)</td><td>3669.86 (n/a)</td><td>4491.20 (n/a)</td><td>2283.90 (n/a)</td><td>1222.57 (n/a)</td><td>925.56 (n/a)</td><td>640.69 (n/a)</td><td>470.68 (n/a)</td><td>450.94 (n/a)</td><td>242.85 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.26 <b>(-22.69%)</b></td><td>0.21 (-7.87%)</td><td>0.21 (+7.28%)</td><td>0.17 (-6.99%)</td><td>0.03 <b>(-46.55%)</b></td><td>7369.40 (+7.52%)</td><td>6082.82 (+5.28%)</td><td>5952.80 (-6.79%)</td><td>4853.10 <b>(+29.35%)</b></td><td>972.37 <b>(-25.76%)</b></td><td>13.83 <b>(-22.69%)</b></td><td>11.26 (-7.87%)</td><td>11.27 (+7.28%)</td><td>9.11 (-6.99%)</td><td>1.82 <b>(-46.55%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>6854.10 (n/a)</td><td>5777.88 (n/a)</td><td>6386.30 (n/a)</td><td>3752.00 (n/a)</td><td>1309.73 (n/a)</td><td>17.89 (n/a)</td><td>12.23 (n/a)</td><td>10.51 (n/a)</td><td>9.79 (n/a)</td><td>3.41 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (+12.18%)</td><td>0.09 (+5.81%)</td><td>0.07 (-10.07%)</td><td>0.05 (-12.40%)</td><td>0.03 <b>(+42.31%)</b></td><td>0.13 (+12.18%)</td><td>0.09 (+5.81%)</td><td>0.07 (-10.07%)</td><td>0.05 (-12.40%)</td><td>0.03 <b>(+42.31%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.78 (+0.91%)</td><td>3.60 (+0.66%)</td><td>3.56 (-2.01%)</td><td>3.45 (+2.82%)</td><td>0.13 <b>(-25.72%)</b></td><td>3.78 (+0.91%)</td><td>3.60 (+0.66%)</td><td>3.56 (-2.01%)</td><td>3.45 (+2.82%)</td><td>0.13 <b>(-25.72%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>3.75 (n/a)</td><td>3.57 (n/a)</td><td>3.63 (n/a)</td><td>3.36 (n/a)</td><td>0.18 (n/a)</td><td>3.75 (n/a)</td><td>3.57 (n/a)</td><td>3.63 (n/a)</td><td>3.36 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.39 (+2.24%)</td><td>6.33 (+0.66%)</td><td>6.58 (-4.22%)</td><td>5.18 (+3.71%)</td><td>0.95 (-6.06%)</td><td>7.38 (+2.24%)</td><td>6.33 (+0.66%)</td><td>6.58 (-4.22%)</td><td>5.18 (+3.71%)</td><td>0.95 (-6.06%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>7.22 (n/a)</td><td>6.29 (n/a)</td><td>6.87 (n/a)</td><td>4.99 (n/a)</td><td>1.01 (n/a)</td><td>7.22 (n/a)</td><td>6.29 (n/a)</td><td>6.87 (n/a)</td><td>4.99 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>13.90 (+3.67%)</td><td>10.46 (-9.76%)</td><td>9.71 <b>(-20.66%)</b></td><td>6.41 <b>(-23.29%)</b></td><td>3.00 <b>(+39.69%)</b></td><td>13.89 (+3.67%)</td><td>10.45 (-9.76%)</td><td>9.71 <b>(-20.66%)</b></td><td>6.40 <b>(-23.29%)</b></td><td>3.00 <b>(+39.69%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>13.40 (n/a)</td><td>11.59 (n/a)</td><td>12.24 (n/a)</td><td>8.35 (n/a)</td><td>2.15 (n/a)</td><td>13.39 (n/a)</td><td>11.58 (n/a)</td><td>12.23 (n/a)</td><td>8.35 (n/a)</td><td>2.14 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.83 (-2.52%)</td><td>3.72 (-1.70%)</td><td>3.75 (-1.84%)</td><td>3.60 (+0.54%)</td><td>0.09 <b>(-38.61%)</b></td><td>3.83 (-2.52%)</td><td>3.72 (-1.70%)</td><td>3.75 (-1.84%)</td><td>3.60 (+0.54%)</td><td>0.09 <b>(-38.61%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>3.93 (n/a)</td><td>3.78 (n/a)</td><td>3.82 (n/a)</td><td>3.58 (n/a)</td><td>0.15 (n/a)</td><td>3.93 (n/a)</td><td>3.78 (n/a)</td><td>3.82 (n/a)</td><td>3.58 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>6.92 (-8.10%)</td><td>6.34 (+3.23%)</td><td>6.44 (+12.75%)</td><td>5.75 (+15.29%)</td><td>0.51 <b>(-59.37%)</b></td><td>6.92 (-8.10%)</td><td>6.33 (+3.23%)</td><td>6.44 (+12.75%)</td><td>5.75 (+15.29%)</td><td>0.51 <b>(-59.37%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>7.53 (n/a)</td><td>6.14 (n/a)</td><td>5.71 (n/a)</td><td>4.99 (n/a)</td><td>1.26 (n/a)</td><td>7.53 (n/a)</td><td>6.14 (n/a)</td><td>5.71 (n/a)</td><td>4.99 (n/a)</td><td>1.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>13.80 (-1.65%)</td><td>9.88 (+3.71%)</td><td>8.51 (+0.71%)</td><td>7.13 (-11.91%)</td><td>2.80 (+10.61%)</td><td>13.79 (-1.65%)</td><td>9.88 (+3.71%)</td><td>8.51 (+0.71%)</td><td>7.13 (-11.91%)</td><td>2.80 (+10.61%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>14.03 (n/a)</td><td>9.53 (n/a)</td><td>8.45 (n/a)</td><td>8.10 (n/a)</td><td>2.53 (n/a)</td><td>14.02 (n/a)</td><td>9.53 (n/a)</td><td>8.45 (n/a)</td><td>8.09 (n/a)</td><td>2.53 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.70 (n/a)</td><td>473.54 (n/a)</td><td>518.30 (n/a)</td><td>212.10 (n/a)</td><td>152.15 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2480.00 (n/a)</td><td>809.32 (n/a)</td><td>506.90 (n/a)</td><td>265.70 (n/a)</td><td>941.45 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.30 (n/a)</td><td>352.04 (n/a)</td><td>294.40 (n/a)</td><td>204.00 (n/a)</td><td>135.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.40 (n/a)</td><td>509.84 (n/a)</td><td>542.00 (n/a)</td><td>366.10 (n/a)</td><td>108.04 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>657.70 (n/a)</td><td>455.88 (n/a)</td><td>441.70 (n/a)</td><td>179.90 (n/a)</td><td>194.22 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1230.50 (n/a)</td><td>635.80 (n/a)</td><td>516.70 (n/a)</td><td>256.20 (n/a)</td><td>363.01 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.90 (n/a)</td><td>350.22 (n/a)</td><td>310.40 (n/a)</td><td>194.70 (n/a)</td><td>150.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1937.40 (n/a)</td><td>601.46 (n/a)</td><td>280.20 (n/a)</td><td>235.00 (n/a)</td><td>747.24 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.00 (n/a)</td><td>385.50 (n/a)</td><td>324.20 (n/a)</td><td>273.30 (n/a)</td><td>118.79 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1989.70 (n/a)</td><td>809.98 (n/a)</td><td>538.30 (n/a)</td><td>471.20 (n/a)</td><td>660.36 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.80 (n/a)</td><td>466.68 (n/a)</td><td>500.90 (n/a)</td><td>286.90 (n/a)</td><td>106.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2466.10 (n/a)</td><td>879.06 (n/a)</td><td>546.80 (n/a)</td><td>375.90 (n/a)</td><td>891.98 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>552.30 (n/a)</td><td>384.66 (n/a)</td><td>386.70 (n/a)</td><td>256.30 (n/a)</td><td>112.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>625.00 (n/a)</td><td>529.82 (n/a)</td><td>572.40 (n/a)</td><td>354.00 (n/a)</td><td>105.33 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>615.50 (n/a)</td><td>510.36 (n/a)</td><td>567.80 (n/a)</td><td>237.30 (n/a)</td><td>154.15 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2438.10 (n/a)</td><td>874.60 (n/a)</td><td>542.40 (n/a)</td><td>314.90 (n/a)</td><td>881.92 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1987.40 (n/a)</td><td>794.16 (n/a)</td><td>513.40 (n/a)</td><td>405.50 (n/a)</td><td>671.91 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>637.40 (n/a)</td><td>545.20 (n/a)</td><td>546.40 (n/a)</td><td>463.00 (n/a)</td><td>65.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 <b>(+24.20%)</b></td><td>0.07 (-7.46%)</td><td>0.06 (-11.23%)</td><td>0.05 (-18.57%)</td><td>0.04 <b>(+67.70%)</b></td><td>656.40 <b>(+22.81%)</b></td><td>510.68 (+16.44%)</td><td>558.50 (+12.65%)</td><td>242.60 (-19.48%)</td><td>159.89 <b>(+53.37%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>534.50 (n/a)</td><td>438.58 (n/a)</td><td>495.80 (n/a)</td><td>301.30 (n/a)</td><td>104.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>694.20 (n/a)</td><td>477.50 (n/a)</td><td>506.20 (n/a)</td><td>250.00 (n/a)</td><td>165.78 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2059.80 (n/a)</td><td>731.52 (n/a)</td><td>463.70 (n/a)</td><td>219.20 (n/a)</td><td>751.42 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>508.50 (n/a)</td><td>471.92 (n/a)</td><td>496.60 (n/a)</td><td>371.50 (n/a)</td><td>57.33 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1964.60 (n/a)</td><td>659.46 (n/a)</td><td>292.20 (n/a)</td><td>244.10 (n/a)</td><td>738.67 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>564.70 (n/a)</td><td>429.96 (n/a)</td><td>394.60 (n/a)</td><td>304.30 (n/a)</td><td>113.38 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (-5.35%)</td><td>0.01 (-10.09%)</td><td>0.01 <b>(-21.58%)</b></td><td>0.01 (+0.52%)</td><td>0.00 (-1.76%)</td><td>518.40 (-0.52%)</td><td>412.52 (+11.46%)</td><td>470.30 <b>(+27.52%)</b></td><td>277.20 (+5.68%)</td><td>106.08 (+4.07%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.10 (n/a)</td><td>370.10 (n/a)</td><td>368.80 (n/a)</td><td>262.30 (n/a)</td><td>101.93 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (+12.64%)</td><td>0.02 <b>(+53.15%)</b></td><td>0.02 <b>(+85.00%)</b></td><td>0.01 <b>(+82.52%)</b></td><td>0.00 <b>(-20.67%)</b></td><td>378.90 <b>(-45.21%)</b></td><td>267.86 <b>(-42.05%)</b></td><td>268.90 <b>(-45.95%)</b></td><td>196.40 (-11.21%)</td><td>73.82 <b>(-62.20%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>691.50 (n/a)</td><td>462.20 (n/a)</td><td>497.50 (n/a)</td><td>221.20 (n/a)</td><td>195.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (+12.69%)</td><td>0.01 (+17.76%)</td><td>0.01 (+5.81%)</td><td>0.01 (+18.95%)</td><td>0.00 <b>(+30.94%)</b></td><td>465.40 (-15.93%)</td><td>360.26 (-12.85%)</td><td>421.50 (-5.49%)</td><td>220.40 (-11.27%)</td><td>116.07 (+2.48%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.60 (n/a)</td><td>413.36 (n/a)</td><td>446.00 (n/a)</td><td>248.40 (n/a)</td><td>113.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (+18.07%)</td><td>0.02 (-0.21%)</td><td>0.02 (+5.31%)</td><td>0.01 <b>(-35.25%)</b></td><td>0.01 <b>(+141.74%)</b></td><td>505.60 <b>(+54.43%)</b></td><td>299.32 (+10.92%)</td><td>248.70 (-5.04%)</td><td>186.70 (-15.29%)</td><td>126.14 <b>(+225.66%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>327.40 (n/a)</td><td>269.86 (n/a)</td><td>261.90 (n/a)</td><td>220.40 (n/a)</td><td>38.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (+6.19%)</td><td>0.01 (-2.37%)</td><td>0.01 (+0.25%)</td><td>0.01 (+1.90%)</td><td>0.00 (+1.64%)</td><td>638.30 (-1.86%)</td><td>369.34 (+2.01%)</td><td>292.90 (-0.27%)</td><td>229.90 (-5.82%)</td><td>161.59 (-3.83%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>650.40 (n/a)</td><td>362.08 (n/a)</td><td>293.70 (n/a)</td><td>244.10 (n/a)</td><td>168.02 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (-7.74%)</td><td>0.01 (-16.97%)</td><td>0.01 (-17.60%)</td><td>0.01 <b>(-27.84%)</b></td><td>0.00 <b>(+62.24%)</b></td><td>435.80 <b>(+38.57%)</b></td><td>333.78 <b>(+24.78%)</b></td><td>321.50 <b>(+21.32%)</b></td><td>250.10 (+8.36%)</td><td>81.92 <b>(+142.60%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>314.50 (n/a)</td><td>267.50 (n/a)</td><td>265.00 (n/a)</td><td>230.80 (n/a)</td><td>33.77 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (-6.02%)</td><td>0.01 (-8.54%)</td><td>0.01 (-10.64%)</td><td>0.01 (-11.85%)</td><td>0.00 (-0.91%)</td><td>551.90 (+13.44%)</td><td>401.64 (+10.55%)</td><td>363.20 (+11.93%)</td><td>275.30 (+6.42%)</td><td>126.33 (+18.60%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>486.50 (n/a)</td><td>363.30 (n/a)</td><td>324.50 (n/a)</td><td>258.70 (n/a)</td><td>106.52 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 <b>(-20.38%)</b></td><td>0.01 (-1.59%)</td><td>0.01 (-7.12%)</td><td>0.01 (+2.12%)</td><td>0.00 <b>(-27.41%)</b></td><td>631.50 (-2.08%)</td><td>513.02 (-1.63%)</td><td>622.10 (+7.65%)</td><td>307.40 <b>(+25.57%)</b></td><td>159.02 (+0.64%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>644.90 (n/a)</td><td>521.52 (n/a)</td><td>577.90 (n/a)</td><td>244.80 (n/a)</td><td>158.00 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 <b>(-63.52%)</b></td><td>0.00 <b>(-59.04%)</b></td><td>0.01 <b>(-46.11%)</b></td><td>0.00 <b>(-72.75%)</b></td><td>0.00 <b>(-55.02%)</b></td><td>1842.00 <b>(+266.93%)</b></td><td>1016.54 <b>(+160.84%)</b></td><td>791.90 <b>(+85.59%)</b></td><td>678.60 <b>(+174.18%)</b></td><td>489.97 <b>(+344.01%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.00 (n/a)</td><td>389.72 (n/a)</td><td>426.70 (n/a)</td><td>247.50 (n/a)</td><td>110.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (-2.53%)</td><td>0.01 (+19.85%)</td><td>0.01 <b>(+36.51%)</b></td><td>0.01 (+3.89%)</td><td>0.00 (+0.15%)</td><td>617.80 (-3.74%)</td><td>402.04 (-16.38%)</td><td>345.80 <b>(-26.74%)</b></td><td>274.70 (+2.58%)</td><td>144.81 (+0.90%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.80 (n/a)</td><td>480.78 (n/a)</td><td>472.00 (n/a)</td><td>267.80 (n/a)</td><td>143.52 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 <b>(-24.05%)</b></td><td>0.01 (-5.55%)</td><td>0.01 <b>(+44.76%)</b></td><td>0.00 <b>(-72.35%)</b></td><td>0.01 (+1.21%)</td><td>2041.70 <b>(+261.68%)</b></td><td>711.94 <b>(+57.50%)</b></td><td>341.60 <b>(-30.91%)</b></td><td>278.60 <b>(+31.66%)</b></td><td>752.52 <b>(+444.78%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.50 (n/a)</td><td>452.02 (n/a)</td><td>494.40 (n/a)</td><td>211.60 (n/a)</td><td>138.13 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 <b>(-21.37%)</b></td><td>0.01 (-6.14%)</td><td>0.01 <b>(-24.50%)</b></td><td>0.01 (-0.77%)</td><td>0.00 <b>(-23.24%)</b></td><td>651.70 (+0.77%)</td><td>423.06 (+1.83%)</td><td>450.60 <b>(+32.45%)</b></td><td>277.40 <b>(+27.19%)</b></td><td>155.23 (-12.31%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>646.70 (n/a)</td><td>415.44 (n/a)</td><td>340.20 (n/a)</td><td>218.10 (n/a)</td><td>177.02 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 <b>(+21.96%)</b></td><td>0.03 <b>(+29.59%)</b></td><td>0.03 <b>(+23.06%)</b></td><td>0.01 (-1.24%)</td><td>0.01 <b>(+25.82%)</b></td><td>557.70 (+1.25%)</td><td>303.92 <b>(-20.82%)</b></td><td>238.30 (-18.72%)</td><td>215.80 (-18.01%)</td><td>144.98 (+3.06%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.80 (n/a)</td><td>383.84 (n/a)</td><td>293.20 (n/a)</td><td>263.20 (n/a)</td><td>140.66 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 <b>(+20.74%)</b></td><td>0.02 (+4.36%)</td><td>0.02 (-18.94%)</td><td>0.02 <b>(+22.58%)</b></td><td>0.01 (+0.37%)</td><td>509.90 (-18.43%)</td><td>353.82 (-6.98%)</td><td>360.20 <b>(+23.36%)</b></td><td>231.40 (-17.15%)</td><td>102.19 <b>(-30.90%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.10 (n/a)</td><td>380.36 (n/a)</td><td>292.00 (n/a)</td><td>279.30 (n/a)</td><td>147.89 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (+4.04%)</td><td>0.03 <b>(+27.43%)</b></td><td>0.03 <b>(+54.22%)</b></td><td>0.01 (+1.30%)</td><td>0.01 <b>(+25.56%)</b></td><td>568.30 (-1.29%)</td><td>360.94 (-17.71%)</td><td>286.00 <b>(-35.15%)</b></td><td>231.40 (-3.86%)</td><td>155.44 <b>(+22.31%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.70 (n/a)</td><td>438.62 (n/a)</td><td>441.00 (n/a)</td><td>240.70 (n/a)</td><td>127.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (+8.38%)</td><td>0.03 (+0.52%)</td><td>0.03 (+9.16%)</td><td>0.01 <b>(-36.85%)</b></td><td>0.01 <b>(+160.68%)</b></td><td>559.30 <b>(+58.35%)</b></td><td>323.96 (+8.04%)</td><td>266.00 (-8.40%)</td><td>244.70 (-7.73%)</td><td>132.35 <b>(+296.46%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>353.20 (n/a)</td><td>299.84 (n/a)</td><td>290.40 (n/a)</td><td>265.20 (n/a)</td><td>33.38 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (+10.44%)</td><td>0.03 <b>(+40.86%)</b></td><td>0.03 <b>(+32.83%)</b></td><td>0.02 <b>(+491.22%)</b></td><td>0.01 <b>(-48.99%)</b></td><td>417.50 <b>(-83.09%)</b></td><td>283.80 <b>(-64.10%)</b></td><td>264.90 <b>(-24.72%)</b></td><td>210.40 (-9.47%)</td><td>78.66 <b>(-91.75%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2468.30 (n/a)</td><td>790.44 (n/a)</td><td>351.90 (n/a)</td><td>232.40 (n/a)</td><td>953.28 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (+12.07%)</td><td>0.03 <b>(+50.61%)</b></td><td>0.04 <b>(+25.55%)</b></td><td>0.03 <b>(+593.62%)</b></td><td>0.00 <b>(-72.00%)</b></td><td>283.10 <b>(-85.58%)</b></td><td>248.74 <b>(-61.94%)</b></td><td>233.80 <b>(-20.37%)</b></td><td>229.20 (-10.78%)</td><td>24.92 <b>(-96.62%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1963.90 (n/a)</td><td>653.56 (n/a)</td><td>293.60 (n/a)</td><td>256.90 (n/a)</td><td>737.20 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (-9.87%)</td><td>0.02 (+6.19%)</td><td>0.02 (+5.72%)</td><td>0.01 <b>(+236.40%)</b></td><td>0.01 <b>(-32.97%)</b></td><td>569.80 <b>(-70.27%)</b></td><td>425.34 <b>(-38.45%)</b></td><td>489.10 (-5.40%)</td><td>255.60 (+10.99%)</td><td>146.36 <b>(-79.03%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1916.80 (n/a)</td><td>691.02 (n/a)</td><td>517.00 (n/a)</td><td>230.30 (n/a)</td><td>698.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (-1.83%)</td><td>0.03 (+19.26%)</td><td>0.03 <b>(+91.05%)</b></td><td>0.01 (+9.88%)</td><td>0.01 (-18.71%)</td><td>572.90 (-9.01%)</td><td>364.74 <b>(-22.27%)</b></td><td>312.00 <b>(-47.66%)</b></td><td>246.30 (+1.86%)</td><td>141.81 <b>(-28.58%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>629.60 (n/a)</td><td>469.22 (n/a)</td><td>596.10 (n/a)</td><td>241.80 (n/a)</td><td>198.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 <b>(+21.76%)</b></td><td>0.02 <b>(+36.63%)</b></td><td>0.03 <b>(+101.29%)</b></td><td>0.02 <b>(+96.19%)</b></td><td>0.01 (-10.02%)</td><td>531.70 <b>(-49.03%)</b></td><td>371.96 <b>(-35.28%)</b></td><td>294.80 <b>(-50.31%)</b></td><td>244.40 (-17.88%)</td><td>131.62 <b>(-56.75%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1043.10 (n/a)</td><td>574.72 (n/a)</td><td>593.30 (n/a)</td><td>297.60 (n/a)</td><td>304.29 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 <b>(+71.48%)</b></td><td>0.03 <b>(+86.17%)</b></td><td>0.03 <b>(+139.99%)</b></td><td>0.02 <b>(+27.84%)</b></td><td>0.01 <b>(+186.68%)</b></td><td>517.70 <b>(-21.77%)</b></td><td>324.38 <b>(-42.80%)</b></td><td>249.10 <b>(-58.32%)</b></td><td>245.30 <b>(-41.68%)</b></td><td>118.97 <b>(+29.00%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>661.80 (n/a)</td><td>567.06 (n/a)</td><td>597.70 (n/a)</td><td>420.60 (n/a)</td><td>92.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 <b>(-28.80%)</b></td><td>0.02 (-9.20%)</td><td>0.01 (-19.64%)</td><td>0.01 (+15.59%)</td><td>0.01 <b>(-33.64%)</b></td><td>588.90 (-13.50%)</td><td>470.12 (+4.08%)</td><td>559.20 <b>(+24.43%)</b></td><td>305.70 <b>(+40.42%)</b></td><td>144.80 (-15.95%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>680.80 (n/a)</td><td>451.70 (n/a)</td><td>449.40 (n/a)</td><td>217.70 (n/a)</td><td>172.29 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (-17.87%)</td><td>0.02 (-4.17%)</td><td>0.02 <b>(+42.10%)</b></td><td>0.02 (-3.66%)</td><td>0.01 <b>(-27.34%)</b></td><td>537.30 (+3.79%)</td><td>392.22 (+0.57%)</td><td>332.40 <b>(-29.62%)</b></td><td>264.50 <b>(+21.78%)</b></td><td>134.28 (-3.97%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.70 (n/a)</td><td>389.98 (n/a)</td><td>472.30 (n/a)</td><td>217.20 (n/a)</td><td>139.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (-12.47%)</td><td>0.06 (-2.30%)</td><td>0.06 (-4.37%)</td><td>0.03 (+6.09%)</td><td>0.01 (-17.30%)</td><td>479.20 (-5.74%)</td><td>314.68 (-0.30%)</td><td>286.20 (+4.57%)</td><td>235.70 (+14.25%)</td><td>100.59 (-14.98%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>508.40 (n/a)</td><td>315.64 (n/a)</td><td>273.70 (n/a)</td><td>206.30 (n/a)</td><td>118.32 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (-2.81%)</td><td>0.05 (+8.78%)</td><td>0.05 (-10.65%)</td><td>0.05 <b>(+57.76%)</b></td><td>0.00 <b>(-72.52%)</b></td><td>358.50 <b>(-36.62%)</b></td><td>326.14 (-15.25%)</td><td>330.80 (+11.91%)</td><td>293.40 (+2.88%)</td><td>24.45 <b>(-81.54%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>565.60 (n/a)</td><td>384.82 (n/a)</td><td>295.60 (n/a)</td><td>285.20 (n/a)</td><td>132.46 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (+2.77%)</td><td>0.05 (-13.85%)</td><td>0.05 (-13.88%)</td><td>0.03 (+0.53%)</td><td>0.02 (+10.80%)</td><td>520.40 (-0.52%)</td><td>363.96 (+17.86%)</td><td>303.20 (+16.12%)</td><td>228.50 (-2.72%)</td><td>130.55 (+7.97%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>523.10 (n/a)</td><td>308.82 (n/a)</td><td>261.10 (n/a)</td><td>234.90 (n/a)</td><td>120.91 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 <b>(+44.22%)</b></td><td>0.06 <b>(+42.38%)</b></td><td>0.06 <b>(+57.31%)</b></td><td>0.03 (+16.47%)</td><td>0.02 <b>(+62.65%)</b></td><td>503.00 (-14.13%)</td><td>304.36 <b>(-27.09%)</b></td><td>270.60 <b>(-36.43%)</b></td><td>190.00 <b>(-30.66%)</b></td><td>117.48 (+3.38%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>585.80 (n/a)</td><td>417.42 (n/a)</td><td>425.70 (n/a)</td><td>274.00 (n/a)</td><td>113.64 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (-2.93%)</td><td>0.05 (-10.50%)</td><td>0.04 <b>(-33.67%)</b></td><td>0.03 (+13.93%)</td><td>0.02 <b>(-25.19%)</b></td><td>501.70 (-12.23%)</td><td>385.36 (+3.47%)</td><td>417.60 <b>(+50.76%)</b></td><td>238.40 (+3.03%)</td><td>114.64 <b>(-33.00%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>571.60 (n/a)</td><td>372.44 (n/a)</td><td>277.00 (n/a)</td><td>231.40 (n/a)</td><td>171.10 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 <b>(-22.98%)</b></td><td>0.03 <b>(-46.15%)</b></td><td>0.03 <b>(-53.06%)</b></td><td>0.01 <b>(-73.85%)</b></td><td>0.02 (+6.11%)</td><td>1952.70 <b>(+282.36%)</b></td><td>758.14 <b>(+154.84%)</b></td><td>520.30 <b>(+113.06%)</b></td><td>275.60 <b>(+29.82%)</b></td><td>677.65 <b>(+457.53%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>510.70 (n/a)</td><td>297.50 (n/a)</td><td>244.20 (n/a)</td><td>212.30 (n/a)</td><td>121.55 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (-12.80%)</td><td>0.04 (-13.30%)</td><td>0.04 (-4.03%)</td><td>0.03 (-0.51%)</td><td>0.01 <b>(-28.94%)</b></td><td>542.60 (+0.52%)</td><td>439.34 (+11.71%)</td><td>449.90 (+4.22%)</td><td>291.70 (+14.66%)</td><td>98.45 (-16.92%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>539.80 (n/a)</td><td>393.28 (n/a)</td><td>431.70 (n/a)</td><td>254.40 (n/a)</td><td>118.50 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 <b>(-21.39%)</b></td><td>0.03 (-12.90%)</td><td>0.03 (-7.09%)</td><td>0.01 (+1.27%)</td><td>0.02 <b>(-38.81%)</b></td><td>1919.40 (-1.25%)</td><td>740.68 (-7.43%)</td><td>498.90 (+7.61%)</td><td>305.60 <b>(+27.17%)</b></td><td>664.07 (-7.95%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1943.70 (n/a)</td><td>800.14 (n/a)</td><td>463.60 (n/a)</td><td>240.30 (n/a)</td><td>721.40 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (-10.46%)</td><td>0.04 (-13.63%)</td><td>0.03 (-3.06%)</td><td>0.03 (+9.17%)</td><td>0.01 <b>(-32.84%)</b></td><td>591.50 (-8.39%)</td><td>479.14 (+7.72%)</td><td>507.80 (+3.15%)</td><td>284.50 (+11.70%)</td><td>120.46 <b>(-30.33%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>645.70 (n/a)</td><td>444.82 (n/a)</td><td>492.30 (n/a)</td><td>254.70 (n/a)</td><td>172.91 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (+6.57%)</td><td>0.04 (-19.59%)</td><td>0.03 <b>(-31.79%)</b></td><td>0.03 (-16.81%)</td><td>0.02 (+7.23%)</td><td>603.60 <b>(+20.22%)</b></td><td>458.24 <b>(+26.24%)</b></td><td>478.90 <b>(+46.63%)</b></td><td>233.50 (-6.19%)</td><td>137.06 (+11.08%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>502.10 (n/a)</td><td>363.00 (n/a)</td><td>326.60 (n/a)</td><td>248.90 (n/a)</td><td>123.39 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (-6.91%)</td><td>0.04 (-19.52%)</td><td>0.03 <b>(-44.90%)</b></td><td>0.03 (-0.91%)</td><td>0.01 (-18.98%)</td><td>611.60 (+0.91%)</td><td>484.76 <b>(+21.44%)</b></td><td>554.80 <b>(+81.49%)</b></td><td>313.20 (+7.41%)</td><td>129.69 (-8.94%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>606.10 (n/a)</td><td>399.18 (n/a)</td><td>305.70 (n/a)</td><td>291.60 (n/a)</td><td>142.42 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (-9.72%)</td><td>0.05 <b>(+34.99%)</b></td><td>0.05 <b>(+96.08%)</b></td><td>0.04 <b>(+348.17%)</b></td><td>0.01 <b>(-65.15%)</b></td><td>430.10 <b>(-77.68%)</b></td><td>346.32 <b>(-54.51%)</b></td><td>320.40 <b>(-49.00%)</b></td><td>291.00 (+10.77%)</td><td>63.06 <b>(-90.77%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1927.40 (n/a)</td><td>761.38 (n/a)</td><td>628.20 (n/a)</td><td>262.70 (n/a)</td><td>683.01 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (+15.47%)</td><td>0.09 (+7.50%)</td><td>0.10 (+8.15%)</td><td>0.06 (+9.85%)</td><td>0.03 (+11.97%)</td><td>514.90 (-8.98%)</td><td>376.96 (-6.63%)</td><td>325.20 (-7.53%)</td><td>254.10 (-13.42%)</td><td>119.87 (-5.70%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>565.70 (n/a)</td><td>403.74 (n/a)</td><td>351.70 (n/a)</td><td>293.50 (n/a)</td><td>127.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.11 (-10.60%)</td><td>0.08 <b>(-22.90%)</b></td><td>0.07 <b>(-33.59%)</b></td><td>0.06 (-6.35%)</td><td>0.02 (-16.14%)</td><td>594.00 (+6.78%)</td><td>447.30 <b>(+27.57%)</b></td><td>452.80 <b>(+50.58%)</b></td><td>291.70 (+11.85%)</td><td>108.18 (-8.63%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>556.30 (n/a)</td><td>350.62 (n/a)</td><td>300.70 (n/a)</td><td>260.80 (n/a)</td><td>118.39 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (-18.05%)</td><td>0.09 <b>(-24.04%)</b></td><td>0.09 (-18.09%)</td><td>0.06 <b>(-39.61%)</b></td><td>0.03 <b>(+27.60%)</b></td><td>587.80 <b>(+65.62%)</b></td><td>406.46 <b>(+43.70%)</b></td><td>358.30 <b>(+22.08%)</b></td><td>241.70 <b>(+22.01%)</b></td><td>158.35 <b>(+180.88%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>354.90 (n/a)</td><td>282.86 (n/a)</td><td>293.50 (n/a)</td><td>198.10 (n/a)</td><td>56.38 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 <b>(+30.99%)</b></td><td>0.10 (+10.75%)</td><td>0.11 <b>(+22.87%)</b></td><td>0.06 (-9.42%)</td><td>0.04 <b>(+79.05%)</b></td><td>574.20 (+10.40%)</td><td>378.84 (-0.70%)</td><td>295.40 (-18.60%)</td><td>213.40 <b>(-23.65%)</b></td><td>164.63 <b>(+63.57%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>520.10 (n/a)</td><td>381.50 (n/a)</td><td>362.90 (n/a)</td><td>279.50 (n/a)</td><td>100.65 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (+12.19%)</td><td>0.10 <b>(+23.26%)</b></td><td>0.11 <b>(+72.61%)</b></td><td>0.06 (+8.89%)</td><td>0.03 <b>(+26.25%)</b></td><td>595.00 (-8.16%)</td><td>388.72 (-16.20%)</td><td>301.40 <b>(-42.07%)</b></td><td>250.30 (-10.86%)</td><td>159.54 (+7.22%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>647.90 (n/a)</td><td>463.88 (n/a)</td><td>520.30 (n/a)</td><td>280.80 (n/a)</td><td>148.79 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (+15.27%)</td><td>0.11 <b>(+20.18%)</b></td><td>0.11 <b>(+51.54%)</b></td><td>0.07 (-4.41%)</td><td>0.03 <b>(+27.58%)</b></td><td>461.20 (+4.60%)</td><td>314.12 (-15.04%)</td><td>285.50 <b>(-34.00%)</b></td><td>222.40 (-13.26%)</td><td>101.60 (+9.98%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>440.90 (n/a)</td><td>369.72 (n/a)</td><td>432.60 (n/a)</td><td>256.40 (n/a)</td><td>92.38 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (+5.86%)</td><td>0.09 (-8.96%)</td><td>0.10 (-7.49%)</td><td>0.05 <b>(-21.44%)</b></td><td>0.04 <b>(+35.41%)</b></td><td>601.10 <b>(+27.30%)</b></td><td>409.68 (+19.12%)</td><td>317.40 (+8.07%)</td><td>230.20 (-5.54%)</td><td>175.96 <b>(+74.51%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>472.20 (n/a)</td><td>343.92 (n/a)</td><td>293.70 (n/a)</td><td>243.70 (n/a)</td><td>100.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.11 (-10.68%)</td><td>0.08 <b>(-21.05%)</b></td><td>0.07 <b>(-38.50%)</b></td><td>0.06 (-9.19%)</td><td>0.02 <b>(-27.50%)</b></td><td>565.00 (+10.14%)</td><td>447.20 <b>(+22.17%)</b></td><td>469.40 <b>(+62.59%)</b></td><td>285.40 (+11.97%)</td><td>105.79 (-17.00%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>513.00 (n/a)</td><td>366.06 (n/a)</td><td>288.70 (n/a)</td><td>254.90 (n/a)</td><td>127.45 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (+8.71%)</td><td>0.11 <b>(+41.69%)</b></td><td>0.13 <b>(+94.53%)</b></td><td>0.06 (+7.18%)</td><td>0.04 <b>(+30.14%)</b></td><td>551.90 (-6.69%)</td><td>354.90 <b>(-26.08%)</b></td><td>257.00 <b>(-48.59%)</b></td><td>232.50 (-8.03%)</td><td>155.73 (+15.64%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>591.50 (n/a)</td><td>480.12 (n/a)</td><td>499.90 (n/a)</td><td>252.80 (n/a)</td><td>134.67 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 <b>(+54.30%)</b></td><td>0.09 <b>(+25.52%)</b></td><td>0.08 (+18.94%)</td><td>0.06 (+8.00%)</td><td>0.03 <b>(+110.28%)</b></td><td>539.70 (-7.41%)</td><td>397.48 (-16.77%)</td><td>399.50 (-15.91%)</td><td>233.30 <b>(-35.19%)</b></td><td>110.52 (+18.08%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>582.90 (n/a)</td><td>477.54 (n/a)</td><td>475.10 (n/a)</td><td>360.00 (n/a)</td><td>93.60 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (+10.55%)</td><td>0.09 <b>(+55.40%)</b></td><td>0.09 <b>(+63.60%)</b></td><td>0.06 <b>(+240.20%)</b></td><td>0.03 <b>(-24.96%)</b></td><td>568.00 <b>(-70.61%)</b></td><td>379.40 <b>(-52.81%)</b></td><td>370.40 <b>(-38.88%)</b></td><td>246.90 (-9.53%)</td><td>121.03 <b>(-81.31%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1932.50 (n/a)</td><td>803.96 (n/a)</td><td>606.00 (n/a)</td><td>272.90 (n/a)</td><td>647.62 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (-2.83%)</td><td>0.10 (-3.86%)</td><td>0.10 (-8.10%)</td><td>0.06 (+0.58%)</td><td>0.03 (-16.51%)</td><td>532.90 (-0.58%)</td><td>369.62 (+1.14%)</td><td>314.80 (+8.85%)</td><td>256.70 (+2.93%)</td><td>114.81 (-14.27%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>536.00 (n/a)</td><td>365.46 (n/a)</td><td>289.20 (n/a)</td><td>249.40 (n/a)</td><td>133.92 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 <b>(+23.60%)</b></td><td>0.01 <b>(+23.36%)</b></td><td>0.01 <b>(+26.05%)</b></td><td>0.01 (+6.47%)</td><td>0.01 <b>(+52.28%)</b></td><td>513.00 (-6.08%)</td><td>336.30 (-13.20%)</td><td>276.60 <b>(-20.65%)</b></td><td>190.30 (-19.09%)</td><td>148.90 (+19.64%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.20 (n/a)</td><td>387.46 (n/a)</td><td>348.60 (n/a)</td><td>235.20 (n/a)</td><td>124.45 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 <b>(+34.66%)</b></td><td>0.02 <b>(+65.80%)</b></td><td>0.02 <b>(+98.09%)</b></td><td>0.01 <b>(+135.37%)</b></td><td>0.01 (+13.27%)</td><td>462.10 <b>(-57.51%)</b></td><td>326.48 <b>(-44.98%)</b></td><td>278.00 <b>(-49.51%)</b></td><td>227.30 <b>(-25.72%)</b></td><td>103.65 <b>(-64.94%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1087.60 (n/a)</td><td>593.38 (n/a)</td><td>550.60 (n/a)</td><td>306.00 (n/a)</td><td>295.61 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 <b>(+77.09%)</b></td><td>0.01 <b>(+39.94%)</b></td><td>0.01 (+2.08%)</td><td>0.01 <b>(+45.37%)</b></td><td>0.01 <b>(+117.72%)</b></td><td>526.30 <b>(-31.21%)</b></td><td>397.54 <b>(-22.08%)</b></td><td>480.60 (-2.04%)</td><td>170.20 <b>(-43.53%)</b></td><td>158.44 (-12.00%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>765.10 (n/a)</td><td>510.16 (n/a)</td><td>490.60 (n/a)</td><td>301.40 (n/a)</td><td>180.04 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 <b>(+21.81%)</b></td><td>0.01 (+1.08%)</td><td>0.01 <b>(-30.22%)</b></td><td>0.01 <b>(+210.67%)</b></td><td>0.01 (-9.71%)</td><td>600.20 <b>(-67.81%)</b></td><td>449.84 <b>(-32.30%)</b></td><td>469.90 <b>(+43.31%)</b></td><td>211.70 (-17.88%)</td><td>163.46 <b>(-76.12%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1864.80 (n/a)</td><td>664.46 (n/a)</td><td>327.90 (n/a)</td><td>257.80 (n/a)</td><td>684.47 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (-4.02%)</td><td>0.01 (-4.80%)</td><td>0.01 <b>(+43.39%)</b></td><td>0.00 <b>(-68.85%)</b></td><td>0.01 <b>(+35.16%)</b></td><td>1918.80 <b>(+221.08%)</b></td><td>655.66 <b>(+65.30%)</b></td><td>291.10 <b>(-30.26%)</b></td><td>241.00 (+4.19%)</td><td>716.75 <b>(+382.46%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>597.60 (n/a)</td><td>396.66 (n/a)</td><td>417.40 (n/a)</td><td>231.30 (n/a)</td><td>148.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (-7.99%)</td><td>0.02 (+2.89%)</td><td>0.02 <b>(+49.40%)</b></td><td>0.01 (+0.29%)</td><td>0.01 <b>(-21.38%)</b></td><td>621.40 (-0.29%)</td><td>381.44 (-7.74%)</td><td>321.70 <b>(-33.08%)</b></td><td>227.40 (+8.70%)</td><td>160.96 (-10.09%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.20 (n/a)</td><td>413.46 (n/a)</td><td>480.70 (n/a)</td><td>209.20 (n/a)</td><td>179.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 <b>(+40.03%)</b></td><td>0.01 (-3.67%)</td><td>0.01 <b>(-36.67%)</b></td><td>0.01 <b>(+67.55%)</b></td><td>0.01 <b>(+24.68%)</b></td><td>630.80 <b>(-40.32%)</b></td><td>459.16 (-5.25%)</td><td>472.40 <b>(+57.89%)</b></td><td>189.30 <b>(-28.57%)</b></td><td>168.34 <b>(-49.94%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1056.90 (n/a)</td><td>484.62 (n/a)</td><td>299.20 (n/a)</td><td>265.00 (n/a)</td><td>336.26 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 <b>(-31.20%)</b></td><td>0.01 <b>(-30.62%)</b></td><td>0.01 <b>(-39.44%)</b></td><td>0.01 (-3.07%)</td><td>0.00 <b>(-50.90%)</b></td><td>559.00 (+3.17%)</td><td>471.24 <b>(+33.93%)</b></td><td>484.60 <b>(+65.11%)</b></td><td>314.40 <b>(+45.35%)</b></td><td>95.43 <b>(-30.29%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>541.80 (n/a)</td><td>351.86 (n/a)</td><td>293.50 (n/a)</td><td>216.30 (n/a)</td><td>136.90 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 <b>(-41.17%)</b></td><td>0.01 <b>(-32.57%)</b></td><td>0.01 <b>(-21.49%)</b></td><td>0.00 <b>(-52.41%)</b></td><td>0.00 <b>(-40.09%)</b></td><td>1124.10 <b>(+110.15%)</b></td><td>646.26 <b>(+52.61%)</b></td><td>576.30 <b>(+27.39%)</b></td><td>389.50 <b>(+70.01%)</b></td><td>284.08 <b>(+127.06%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>534.90 (n/a)</td><td>423.46 (n/a)</td><td>452.40 (n/a)</td><td>229.10 (n/a)</td><td>125.11 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (-9.99%)</td><td>0.01 <b>(-30.79%)</b></td><td>0.01 <b>(-44.68%)</b></td><td>0.01 (-9.18%)</td><td>0.00 (+3.02%)</td><td>615.50 (+10.11%)</td><td>510.26 <b>(+46.65%)</b></td><td>566.80 <b>(+80.74%)</b></td><td>268.50 (+11.09%)</td><td>140.05 (+13.67%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.00 (n/a)</td><td>347.94 (n/a)</td><td>313.60 (n/a)</td><td>241.70 (n/a)</td><td>123.21 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (-7.88%)</td><td>0.01 (-5.56%)</td><td>0.01 (-16.69%)</td><td>0.01 (-6.14%)</td><td>0.00 (+0.88%)</td><td>659.20 (+6.55%)</td><td>457.18 (+7.50%)</td><td>519.90 <b>(+20.04%)</b></td><td>274.20 (+8.59%)</td><td>160.95 (+13.62%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>618.70 (n/a)</td><td>425.28 (n/a)</td><td>433.10 (n/a)</td><td>252.50 (n/a)</td><td>141.65 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (-1.69%)</td><td>0.02 (+6.79%)</td><td>0.02 (+12.22%)</td><td>0.01 (-5.70%)</td><td>0.01 (-7.62%)</td><td>557.80 (+6.05%)</td><td>399.72 (-7.23%)</td><td>404.30 (-10.89%)</td><td>229.10 (+1.73%)</td><td>120.48 (+0.17%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.00 (n/a)</td><td>430.88 (n/a)</td><td>453.70 (n/a)</td><td>225.20 (n/a)</td><td>120.28 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (-6.22%)</td><td>0.03 <b>(-21.38%)</b></td><td>0.03 <b>(-28.36%)</b></td><td>0.02 <b>(-38.31%)</b></td><td>0.01 (+14.26%)</td><td>765.10 <b>(+62.10%)</b></td><td>473.96 <b>(+37.96%)</b></td><td>434.70 <b>(+39.60%)</b></td><td>240.10 (+6.62%)</td><td>207.47 <b>(+90.96%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>472.00 (n/a)</td><td>343.54 (n/a)</td><td>311.40 (n/a)</td><td>225.20 (n/a)</td><td>108.65 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 <b>(+36.15%)</b></td><td>0.03 (+9.38%)</td><td>0.03 (+9.17%)</td><td>0.01 (-16.57%)</td><td>0.01 <b>(+92.97%)</b></td><td>553.30 (+19.87%)</td><td>359.10 (+2.02%)</td><td>268.90 (-8.38%)</td><td>200.50 <b>(-26.56%)</b></td><td>162.22 <b>(+79.44%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>461.60 (n/a)</td><td>351.98 (n/a)</td><td>293.50 (n/a)</td><td>273.00 (n/a)</td><td>90.40 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (+11.34%)</td><td>0.03 (+10.90%)</td><td>0.02 (-15.91%)</td><td>0.02 <b>(+32.63%)</b></td><td>0.01 (+2.90%)</td><td>520.30 <b>(-24.61%)</b></td><td>421.12 (-12.49%)</td><td>500.40 (+18.92%)</td><td>266.20 (-10.19%)</td><td>122.05 <b>(-31.36%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>690.10 (n/a)</td><td>481.20 (n/a)</td><td>420.80 (n/a)</td><td>296.40 (n/a)</td><td>177.81 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 <b>(+27.30%)</b></td><td>0.02 (-8.62%)</td><td>0.02 <b>(-21.77%)</b></td><td>0.01 (-8.03%)</td><td>0.01 <b>(+61.75%)</b></td><td>627.20 (+8.74%)</td><td>480.82 (+17.53%)</td><td>534.30 <b>(+27.82%)</b></td><td>221.90 <b>(-21.45%)</b></td><td>157.66 <b>(+33.17%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.80 (n/a)</td><td>409.12 (n/a)</td><td>418.00 (n/a)</td><td>282.50 (n/a)</td><td>118.39 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (-15.21%)</td><td>0.03 <b>(+20.99%)</b></td><td>0.03 <b>(+52.88%)</b></td><td>0.02 <b>(+25.72%)</b></td><td>0.00 <b>(-45.35%)</b></td><td>529.30 <b>(-20.47%)</b></td><td>404.52 <b>(-22.75%)</b></td><td>368.40 <b>(-34.58%)</b></td><td>324.40 (+17.92%)</td><td>82.72 <b>(-45.28%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>665.50 (n/a)</td><td>523.68 (n/a)</td><td>563.10 (n/a)</td><td>275.10 (n/a)</td><td>151.16 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (-9.97%)</td><td>0.02 (+3.25%)</td><td>0.02 <b>(+35.43%)</b></td><td>0.02 (+15.89%)</td><td>0.01 <b>(-32.04%)</b></td><td>521.50 (-13.72%)</td><td>383.42 (-8.69%)</td><td>338.90 <b>(-26.17%)</b></td><td>274.20 (+11.06%)</td><td>102.61 <b>(-31.36%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.40 (n/a)</td><td>419.92 (n/a)</td><td>459.00 (n/a)</td><td>246.90 (n/a)</td><td>149.49 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 <b>(-30.38%)</b></td><td>0.02 <b>(-28.15%)</b></td><td>0.02 <b>(+23.03%)</b></td><td>0.01 <b>(-62.57%)</b></td><td>0.01 <b>(-20.72%)</b></td><td>1810.70 <b>(+167.18%)</b></td><td>833.50 <b>(+66.70%)</b></td><td>487.70 (-18.72%)</td><td>355.60 <b>(+43.62%)</b></td><td>611.84 <b>(+197.97%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>677.70 (n/a)</td><td>500.00 (n/a)</td><td>600.00 (n/a)</td><td>247.60 (n/a)</td><td>205.34 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (-0.35%)</td><td>0.02 (+10.33%)</td><td>0.02 <b>(+20.85%)</b></td><td>0.01 (-4.45%)</td><td>0.01 <b>(+21.15%)</b></td><td>704.60 (+4.66%)</td><td>392.46 (-4.86%)</td><td>328.80 (-17.24%)</td><td>243.60 (+0.37%)</td><td>191.79 (+19.87%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.20 (n/a)</td><td>412.50 (n/a)</td><td>397.30 (n/a)</td><td>242.70 (n/a)</td><td>159.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 <b>(-21.01%)</b></td><td>0.02 <b>(-22.30%)</b></td><td>0.02 <b>(-38.30%)</b></td><td>0.02 (+4.32%)</td><td>0.00 <b>(-56.79%)</b></td><td>516.90 (-4.15%)</td><td>445.06 (+19.36%)</td><td>460.50 <b>(+62.03%)</b></td><td>334.60 <b>(+26.60%)</b></td><td>68.62 <b>(-49.25%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.30 (n/a)</td><td>372.86 (n/a)</td><td>284.20 (n/a)</td><td>264.30 (n/a)</td><td>135.20 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (+7.64%)</td><td>0.02 (-8.01%)</td><td>0.02 (-1.93%)</td><td>0.01 (-8.36%)</td><td>0.01 (-1.36%)</td><td>573.10 (+9.14%)</td><td>450.40 (+8.09%)</td><td>479.60 (+1.98%)</td><td>258.00 (-7.09%)</td><td>120.03 (-4.13%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.10 (n/a)</td><td>416.68 (n/a)</td><td>470.30 (n/a)</td><td>277.70 (n/a)</td><td>125.20 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (+3.47%)</td><td>0.05 (-7.42%)</td><td>0.05 (-8.10%)</td><td>0.03 <b>(-27.08%)</b></td><td>0.01 <b>(+52.55%)</b></td><td>591.30 <b>(+37.13%)</b></td><td>361.92 (+14.42%)</td><td>325.30 (+8.83%)</td><td>249.70 (-3.37%)</td><td>134.79 <b>(+102.13%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>431.20 (n/a)</td><td>316.32 (n/a)</td><td>298.90 (n/a)</td><td>258.40 (n/a)</td><td>66.68 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (-16.37%)</td><td>0.06 (-12.38%)</td><td>0.06 <b>(-21.99%)</b></td><td>0.04 (-11.37%)</td><td>0.02 (-19.38%)</td><td>676.00 (+12.84%)</td><td>441.78 (+11.50%)</td><td>383.80 <b>(+28.19%)</b></td><td>297.40 (+19.58%)</td><td>165.69 (+1.25%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>599.10 (n/a)</td><td>396.20 (n/a)</td><td>299.40 (n/a)</td><td>248.70 (n/a)</td><td>163.64 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (-2.64%)</td><td>0.05 (-19.85%)</td><td>0.05 (-7.26%)</td><td>0.02 <b>(-55.02%)</b></td><td>0.02 <b>(+122.73%)</b></td><td>814.30 <b>(+122.36%)</b></td><td>447.28 <b>(+50.45%)</b></td><td>310.80 (+7.84%)</td><td>253.90 (+2.71%)</td><td>245.09 <b>(+399.64%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>366.20 (n/a)</td><td>297.30 (n/a)</td><td>288.20 (n/a)</td><td>247.20 (n/a)</td><td>49.05 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 <b>(+25.97%)</b></td><td>0.05 (+3.97%)</td><td>0.04 (-4.31%)</td><td>0.04 (+13.17%)</td><td>0.01 <b>(+30.34%)</b></td><td>552.60 (-11.64%)</td><td>442.82 (-3.12%)</td><td>462.70 (+4.49%)</td><td>272.70 <b>(-20.61%)</b></td><td>103.58 (-11.88%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>625.40 (n/a)</td><td>457.08 (n/a)</td><td>442.80 (n/a)</td><td>343.50 (n/a)</td><td>117.54 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (-18.00%)</td><td>0.04 (+11.87%)</td><td>0.04 <b>(+43.57%)</b></td><td>0.03 <b>(+318.94%)</b></td><td>0.01 <b>(-52.69%)</b></td><td>591.70 <b>(-76.13%)</b></td><td>401.00 <b>(-51.86%)</b></td><td>410.20 <b>(-30.34%)</b></td><td>283.60 <b>(+21.98%)</b></td><td>126.31 <b>(-86.53%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2478.80 (n/a)</td><td>832.96 (n/a)</td><td>588.90 (n/a)</td><td>232.50 (n/a)</td><td>937.51 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (+19.87%)</td><td>0.06 (+6.94%)</td><td>0.04 (-14.01%)</td><td>0.04 (+4.72%)</td><td>0.02 <b>(+62.12%)</b></td><td>481.90 (-4.50%)</td><td>379.18 (-0.75%)</td><td>467.50 (+16.29%)</td><td>230.90 (-16.58%)</td><td>128.96 <b>(+34.76%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>504.60 (n/a)</td><td>382.04 (n/a)</td><td>402.00 (n/a)</td><td>276.80 (n/a)</td><td>95.69 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (+5.64%)</td><td>0.04 <b>(-24.46%)</b></td><td>0.04 <b>(-47.81%)</b></td><td>0.03 (-14.30%)</td><td>0.02 (+9.30%)</td><td>547.90 (+16.67%)</td><td>429.02 <b>(+35.64%)</b></td><td>462.00 <b>(+91.62%)</b></td><td>207.20 (-5.34%)</td><td>138.15 (+17.22%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>469.60 (n/a)</td><td>316.30 (n/a)</td><td>241.10 (n/a)</td><td>218.90 (n/a)</td><td>117.85 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (-16.63%)</td><td>0.05 (-10.28%)</td><td>0.05 (-2.33%)</td><td>0.03 <b>(-21.36%)</b></td><td>0.02 (-2.20%)</td><td>708.20 <b>(+27.15%)</b></td><td>428.26 (+15.56%)</td><td>345.00 (+2.37%)</td><td>279.60 (+19.95%)</td><td>181.09 <b>(+45.53%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>557.00 (n/a)</td><td>370.58 (n/a)</td><td>337.00 (n/a)</td><td>233.10 (n/a)</td><td>124.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 <b>(-54.58%)</b></td><td>0.02 <b>(-57.70%)</b></td><td>0.02 <b>(-45.01%)</b></td><td>0.01 <b>(-68.87%)</b></td><td>0.01 <b>(-41.75%)</b></td><td>1895.60 <b>(+221.18%)</b></td><td>1132.92 <b>(+181.76%)</b></td><td>761.50 <b>(+81.87%)</b></td><td>530.60 <b>(+120.17%)</b></td><td>692.07 <b>(+366.62%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.20 (n/a)</td><td>402.08 (n/a)</td><td>418.70 (n/a)</td><td>241.00 (n/a)</td><td>148.32 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (+0.70%)</td><td>0.04 <b>(-21.70%)</b></td><td>0.04 <b>(-30.87%)</b></td><td>0.03 <b>(-23.93%)</b></td><td>0.01 <b>(+25.33%)</b></td><td>701.80 <b>(+31.45%)</b></td><td>508.40 <b>(+32.44%)</b></td><td>512.10 <b>(+44.66%)</b></td><td>294.80 (-0.67%)</td><td>145.48 <b>(+53.29%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>533.90 (n/a)</td><td>383.86 (n/a)</td><td>354.00 (n/a)</td><td>296.80 (n/a)</td><td>94.90 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (-14.53%)</td><td>0.04 (-6.62%)</td><td>0.03 (+0.80%)</td><td>0.03 (-0.50%)</td><td>0.01 <b>(-26.24%)</b></td><td>544.10 (+0.50%)</td><td>428.40 (+4.00%)</td><td>472.70 (-0.80%)</td><td>302.50 (+17.02%)</td><td>105.36 (-14.13%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>541.40 (n/a)</td><td>411.92 (n/a)</td><td>476.50 (n/a)</td><td>258.50 (n/a)</td><td>122.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (+12.27%)</td><td>0.11 (+13.79%)</td><td>0.12 (+16.55%)</td><td>0.06 (+19.85%)</td><td>0.04 (-5.07%)</td><td>550.50 (-16.57%)</td><td>334.44 (-15.86%)</td><td>266.20 (-14.21%)</td><td>220.10 (-10.93%)</td><td>134.28 <b>(-26.15%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>659.80 (n/a)</td><td>397.46 (n/a)</td><td>310.30 (n/a)</td><td>247.10 (n/a)</td><td>181.82 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (-10.51%)</td><td>0.12 (-3.76%)</td><td>0.12 (-11.96%)</td><td>0.10 <b>(+50.41%)</b></td><td>0.02 <b>(-49.42%)</b></td><td>325.90 <b>(-33.52%)</b></td><td>280.32 (-3.60%)</td><td>281.10 (+13.58%)</td><td>231.20 (+11.74%)</td><td>41.54 <b>(-63.89%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>490.20 (n/a)</td><td>290.78 (n/a)</td><td>247.50 (n/a)</td><td>206.90 (n/a)</td><td>115.06 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 <b>(-24.25%)</b></td><td>0.07 (-8.55%)</td><td>0.07 (-11.34%)</td><td>0.05 <b>(+124.36%)</b></td><td>0.02 <b>(-53.79%)</b></td><td>840.40 <b>(-55.43%)</b></td><td>584.58 <b>(-20.33%)</b></td><td>563.00 (+12.78%)</td><td>417.60 <b>(+32.03%)</b></td><td>157.43 <b>(-75.73%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1885.40 (n/a)</td><td>733.74 (n/a)</td><td>499.20 (n/a)</td><td>316.30 (n/a)</td><td>648.66 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 <b>(-38.51%)</b></td><td>0.08 (-17.76%)</td><td>0.08 (+11.50%)</td><td>0.06 (-2.61%)</td><td>0.01 <b>(-77.35%)</b></td><td>519.80 (+2.69%)</td><td>438.42 (+10.99%)</td><td>412.00 (-10.32%)</td><td>403.60 <b>(+62.61%)</b></td><td>48.88 <b>(-62.03%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>506.20 (n/a)</td><td>395.02 (n/a)</td><td>459.40 (n/a)</td><td>248.20 (n/a)</td><td>128.74 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 <b>(-29.45%)</b></td><td>0.11 (-14.01%)</td><td>0.11 (-4.67%)</td><td>0.07 (-3.54%)</td><td>0.03 <b>(-44.78%)</b></td><td>592.30 (+3.68%)</td><td>410.44 (+8.45%)</td><td>377.30 (+4.92%)</td><td>310.20 <b>(+41.77%)</b></td><td>118.13 <b>(-20.62%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>571.30 (n/a)</td><td>378.46 (n/a)</td><td>359.60 (n/a)</td><td>218.80 (n/a)</td><td>148.82 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.11 <b>(-22.45%)</b></td><td>0.07 (-15.53%)</td><td>0.07 (+18.56%)</td><td>0.05 (-0.93%)</td><td>0.03 <b>(-43.72%)</b></td><td>674.40 (+0.94%)</td><td>483.12 (+5.59%)</td><td>468.60 (-15.66%)</td><td>287.60 <b>(+28.97%)</b></td><td>154.27 <b>(-24.42%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>668.10 (n/a)</td><td>457.54 (n/a)</td><td>555.60 (n/a)</td><td>223.00 (n/a)</td><td>204.13 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 <b>(-24.34%)</b></td><td>0.06 <b>(-29.95%)</b></td><td>0.07 <b>(-24.44%)</b></td><td>0.02 <b>(-73.39%)</b></td><td>0.03 <b>(+31.77%)</b></td><td>1970.40 <b>(+275.74%)</b></td><td>790.86 <b>(+89.20%)</b></td><td>520.30 <b>(+32.32%)</b></td><td>395.00 <b>(+32.15%)</b></td><td>662.40 <b>(+633.96%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>524.40 (n/a)</td><td>418.00 (n/a)</td><td>393.20 (n/a)</td><td>298.90 (n/a)</td><td>90.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.17 <b>(+49.98%)</b></td><td>0.10 <b>(+27.97%)</b></td><td>0.12 (+13.23%)</td><td>0.05 <b>(+69.19%)</b></td><td>0.05 <b>(+35.53%)</b></td><td>626.10 <b>(-40.89%)</b></td><td>388.84 <b>(-24.87%)</b></td><td>282.80 (-11.71%)</td><td>196.50 <b>(-33.32%)</b></td><td>196.42 <b>(-40.05%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1059.20 (n/a)</td><td>517.58 (n/a)</td><td>320.30 (n/a)</td><td>294.70 (n/a)</td><td>327.64 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (-4.25%)</td><td>0.09 (-15.77%)</td><td>0.07 <b>(-31.36%)</b></td><td>0.06 <b>(-20.43%)</b></td><td>0.03 <b>(+21.92%)</b></td><td>632.30 <b>(+25.66%)</b></td><td>476.48 <b>(+25.13%)</b></td><td>526.80 <b>(+45.69%)</b></td><td>262.70 (+4.45%)</td><td>157.46 <b>(+61.92%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>503.20 (n/a)</td><td>380.80 (n/a)</td><td>361.60 (n/a)</td><td>251.50 (n/a)</td><td>97.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 <b>(+26.60%)</b></td><td>0.08 (+19.18%)</td><td>0.06 (+4.40%)</td><td>0.06 <b>(+244.60%)</b></td><td>0.03 (-6.40%)</td><td>548.50 <b>(-70.98%)</b></td><td>459.34 <b>(-38.15%)</b></td><td>517.70 (-4.22%)</td><td>239.20 <b>(-21.00%)</b></td><td>128.31 <b>(-80.39%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1890.10 (n/a)</td><td>742.72 (n/a)</td><td>540.50 (n/a)</td><td>302.80 (n/a)</td><td>654.21 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (-7.47%)</td><td>0.06 (-15.51%)</td><td>0.06 (-12.23%)</td><td>0.04 <b>(-28.36%)</b></td><td>0.02 <b>(+37.36%)</b></td><td>526.60 <b>(+39.57%)</b></td><td>373.34 <b>(+24.41%)</b></td><td>341.80 (+13.93%)</td><td>243.20 (+8.09%)</td><td>115.27 <b>(+113.92%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>377.30 (n/a)</td><td>300.10 (n/a)</td><td>300.00 (n/a)</td><td>225.00 (n/a)</td><td>53.88 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (-19.54%)</td><td>0.07 (+12.82%)</td><td>0.07 (+5.72%)</td><td>0.04 <b>(+290.18%)</b></td><td>0.01 <b>(-56.19%)</b></td><td>486.10 <b>(-74.37%)</b></td><td>327.76 <b>(-48.00%)</b></td><td>291.30 (-5.42%)</td><td>269.60 <b>(+24.30%)</b></td><td>90.63 <b>(-87.29%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1896.70 (n/a)</td><td>630.30 (n/a)</td><td>308.00 (n/a)</td><td>216.90 (n/a)</td><td>713.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (+7.17%)</td><td>0.05 (-4.71%)</td><td>0.04 (-15.36%)</td><td>0.04 (+5.74%)</td><td>0.02 (+9.35%)</td><td>559.30 (-5.43%)</td><td>453.88 (+5.09%)</td><td>523.30 (+18.15%)</td><td>230.20 (-6.69%)</td><td>133.54 (-8.30%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>591.40 (n/a)</td><td>431.88 (n/a)</td><td>442.90 (n/a)</td><td>246.70 (n/a)</td><td>145.63 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 <b>(+25.66%)</b></td><td>0.06 (-11.57%)</td><td>0.04 <b>(-42.68%)</b></td><td>0.04 (-17.86%)</td><td>0.03 <b>(+74.72%)</b></td><td>531.90 <b>(+21.74%)</b></td><td>396.84 <b>(+23.34%)</b></td><td>475.50 <b>(+74.43%)</b></td><td>203.50 <b>(-20.41%)</b></td><td>141.60 <b>(+73.59%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>436.90 (n/a)</td><td>321.74 (n/a)</td><td>272.60 (n/a)</td><td>255.70 (n/a)</td><td>81.57 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (-14.43%)</td><td>0.06 (+14.88%)</td><td>0.05 <b>(+25.89%)</b></td><td>0.04 <b>(+37.82%)</b></td><td>0.01 <b>(-40.62%)</b></td><td>459.30 <b>(-27.44%)</b></td><td>376.64 <b>(-20.07%)</b></td><td>385.90 <b>(-20.56%)</b></td><td>259.80 (+16.87%)</td><td>85.71 <b>(-44.24%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>633.00 (n/a)</td><td>471.20 (n/a)</td><td>485.80 (n/a)</td><td>222.30 (n/a)</td><td>153.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 <b>(+54.72%)</b></td><td>0.07 <b>(+74.92%)</b></td><td>0.08 <b>(+128.22%)</b></td><td>0.04 <b>(+104.51%)</b></td><td>0.02 <b>(+78.68%)</b></td><td>509.40 <b>(-51.10%)</b></td><td>350.04 <b>(-42.65%)</b></td><td>254.50 <b>(-56.18%)</b></td><td>242.90 <b>(-35.35%)</b></td><td>140.13 <b>(-45.46%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1041.70 (n/a)</td><td>610.36 (n/a)</td><td>580.80 (n/a)</td><td>375.70 (n/a)</td><td>256.93 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 <b>(-25.25%)</b></td><td>0.06 <b>(-22.71%)</b></td><td>0.06 <b>(-24.44%)</b></td><td>0.04 (+8.06%)</td><td>0.02 <b>(-46.48%)</b></td><td>599.40 (-7.46%)</td><td>459.98 (+17.96%)</td><td>399.40 <b>(+32.38%)</b></td><td>319.00 <b>(+33.81%)</b></td><td>130.60 <b>(-27.84%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>647.70 (n/a)</td><td>389.94 (n/a)</td><td>301.70 (n/a)</td><td>238.40 (n/a)</td><td>180.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (-13.16%)</td><td>0.06 <b>(-27.36%)</b></td><td>0.05 <b>(-37.03%)</b></td><td>0.04 <b>(-44.64%)</b></td><td>0.02 <b>(+150.38%)</b></td><td>554.10 <b>(+80.61%)</b></td><td>412.42 <b>(+45.72%)</b></td><td>453.40 <b>(+58.81%)</b></td><td>286.00 (+15.14%)</td><td>111.35 <b>(+410.12%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>306.80 (n/a)</td><td>283.02 (n/a)</td><td>285.50 (n/a)</td><td>248.40 (n/a)</td><td>21.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (-10.02%)</td><td>0.06 <b>(-24.98%)</b></td><td>0.06 <b>(-33.80%)</b></td><td>0.04 (-12.35%)</td><td>0.02 (-3.12%)</td><td>584.40 (+14.07%)</td><td>445.98 <b>(+34.54%)</b></td><td>434.30 <b>(+51.06%)</b></td><td>286.70 (+11.12%)</td><td>125.50 <b>(+20.91%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>512.30 (n/a)</td><td>331.48 (n/a)</td><td>287.50 (n/a)</td><td>258.00 (n/a)</td><td>103.80 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 (+3.65%)</td><td>0.07 (-9.50%)</td><td>0.06 (+3.13%)</td><td>0.05 (-16.37%)</td><td>0.02 (+7.13%)</td><td>516.60 (+19.58%)</td><td>398.90 (+12.72%)</td><td>396.40 (-3.01%)</td><td>238.30 (-3.52%)</td><td>118.09 <b>(+27.47%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>432.00 (n/a)</td><td>353.88 (n/a)</td><td>408.70 (n/a)</td><td>247.00 (n/a)</td><td>92.65 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (-6.23%)</td><td>0.05 (-19.77%)</td><td>0.05 (-17.39%)</td><td>0.03 <b>(-35.43%)</b></td><td>0.02 (+12.57%)</td><td>736.80 <b>(+54.85%)</b></td><td>508.20 <b>(+30.49%)</b></td><td>506.50 <b>(+21.06%)</b></td><td>272.00 (+6.67%)</td><td>164.90 <b>(+70.46%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>475.80 (n/a)</td><td>389.46 (n/a)</td><td>418.40 (n/a)</td><td>255.00 (n/a)</td><td>96.74 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 <b>(+39.53%)</b></td><td>0.06 (+14.10%)</td><td>0.05 (+2.37%)</td><td>0.05 (+6.18%)</td><td>0.02 <b>(+110.41%)</b></td><td>492.00 (-5.82%)</td><td>426.32 (-8.18%)</td><td>469.50 (-2.31%)</td><td>243.20 <b>(-28.34%)</b></td><td>103.40 <b>(+40.35%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>522.40 (n/a)</td><td>464.32 (n/a)</td><td>480.60 (n/a)</td><td>339.40 (n/a)</td><td>73.68 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (+10.60%)</td><td>0.04 <b>(+27.33%)</b></td><td>0.04 <b>(+20.50%)</b></td><td>0.03 <b>(+262.88%)</b></td><td>0.00 <b>(-63.83%)</b></td><td>528.60 <b>(-72.44%)</b></td><td>457.28 <b>(-41.64%)</b></td><td>461.40 (-17.01%)</td><td>381.10 (-9.58%)</td><td>53.14 <b>(-91.67%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1918.20 (n/a)</td><td>783.52 (n/a)</td><td>556.00 (n/a)</td><td>421.50 (n/a)</td><td>638.16 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (-5.14%)</td><td>0.06 (+6.38%)</td><td>0.06 (+19.29%)</td><td>0.04 (+8.99%)</td><td>0.02 (-10.41%)</td><td>510.40 (-8.25%)</td><td>360.08 (-7.90%)</td><td>305.90 (-16.17%)</td><td>249.70 (+5.45%)</td><td>116.44 (-13.63%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>556.30 (n/a)</td><td>390.96 (n/a)</td><td>364.90 (n/a)</td><td>236.80 (n/a)</td><td>134.82 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 <b>(-33.68%)</b></td><td>0.05 <b>(-26.28%)</b></td><td>0.04 <b>(-33.55%)</b></td><td>0.03 <b>(-27.28%)</b></td><td>0.02 <b>(-23.81%)</b></td><td>574.00 <b>(+37.52%)</b></td><td>400.86 <b>(+38.33%)</b></td><td>423.90 <b>(+50.48%)</b></td><td>234.40 <b>(+50.84%)</b></td><td>159.13 <b>(+49.35%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>417.40 (n/a)</td><td>289.78 (n/a)</td><td>281.70 (n/a)</td><td>155.40 (n/a)</td><td>106.55 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (-18.27%)</td><td>0.04 (-7.40%)</td><td>0.04 (-10.00%)</td><td>0.03 <b>(+76.53%)</b></td><td>0.01 <b>(-40.93%)</b></td><td>629.70 <b>(-43.35%)</b></td><td>455.64 (-12.10%)</td><td>492.90 (+11.09%)</td><td>301.50 <b>(+22.36%)</b></td><td>141.16 <b>(-59.88%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1111.60 (n/a)</td><td>518.36 (n/a)</td><td>443.70 (n/a)</td><td>246.40 (n/a)</td><td>351.85 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (+2.54%)</td><td>0.06 (+2.04%)</td><td>0.07 (-5.43%)</td><td>0.03 (-1.43%)</td><td>0.02 (+0.51%)</td><td>569.50 (+1.44%)</td><td>345.28 (-2.13%)</td><td>280.90 (+5.76%)</td><td>224.40 (-2.43%)</td><td>142.82 (-0.62%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>561.40 (n/a)</td><td>352.80 (n/a)</td><td>265.60 (n/a)</td><td>230.00 (n/a)</td><td>143.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (+7.20%)</td><td>0.05 (-7.65%)</td><td>0.04 (-14.28%)</td><td>0.03 (+13.43%)</td><td>0.02 (-1.42%)</td><td>635.90 (-11.84%)</td><td>452.64 (+5.87%)</td><td>427.80 (+16.66%)</td><td>244.10 (-6.73%)</td><td>161.38 (-15.36%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>721.30 (n/a)</td><td>427.54 (n/a)</td><td>366.70 (n/a)</td><td>261.70 (n/a)</td><td>190.67 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.39 (-5.78%)</td><td>0.31 (+8.65%)</td><td>0.35 <b>(+31.24%)</b></td><td>0.09 <b>(-37.98%)</b></td><td>0.12 (+9.66%)</td><td>1048.40 <b>(+61.24%)</b></td><td>429.28 (+7.37%)</td><td>277.00 <b>(-23.80%)</b></td><td>249.50 (+6.13%)</td><td>346.84 <b>(+103.09%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.42 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>650.20 (n/a)</td><td>399.82 (n/a)</td><td>363.50 (n/a)</td><td>235.10 (n/a)</td><td>170.78 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.44 (+0.01%)</td><td>0.35 (+9.56%)</td><td>0.39 (+5.10%)</td><td>0.25 <b>(+51.38%)</b></td><td>0.09 <b>(-23.34%)</b></td><td>395.10 <b>(-33.94%)</b></td><td>299.50 (-15.60%)</td><td>252.70 (-4.86%)</td><td>224.30 (+0.00%)</td><td>82.92 <b>(-47.67%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.37 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>598.10 (n/a)</td><td>354.84 (n/a)</td><td>265.60 (n/a)</td><td>224.30 (n/a)</td><td>158.46 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.30 <b>(-28.53%)</b></td><td>0.24 (-7.38%)</td><td>0.23 (+6.49%)</td><td>0.15 (-18.07%)</td><td>0.06 <b>(-37.21%)</b></td><td>656.50 <b>(+22.05%)</b></td><td>439.36 (+4.32%)</td><td>427.30 (-6.09%)</td><td>325.40 <b>(+39.90%)</b></td><td>134.65 (+2.57%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>537.90 (n/a)</td><td>421.16 (n/a)</td><td>455.00 (n/a)</td><td>232.60 (n/a)</td><td>131.27 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.33 <b>(+37.89%)</b></td><td>0.26 <b>(+36.95%)</b></td><td>0.27 <b>(+46.09%)</b></td><td>0.13 (-14.21%)</td><td>0.08 <b>(+116.53%)</b></td><td>555.20 (+16.57%)</td><td>315.14 <b>(-20.91%)</b></td><td>268.50 <b>(-31.54%)</b></td><td>220.20 <b>(-27.49%)</b></td><td>137.04 <b>(+90.27%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>476.30 (n/a)</td><td>398.44 (n/a)</td><td>392.20 (n/a)</td><td>303.70 (n/a)</td><td>72.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.21 <b>(-37.44%)</b></td><td>0.17 <b>(-29.20%)</b></td><td>0.16 <b>(-39.70%)</b></td><td>0.11 (-6.41%)</td><td>0.04 <b>(-56.72%)</b></td><td>641.70 (+6.84%)</td><td>465.72 <b>(+27.92%)</b></td><td>447.30 <b>(+65.85%)</b></td><td>352.70 <b>(+59.88%)</b></td><td>118.49 <b>(-28.17%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>600.60 (n/a)</td><td>364.06 (n/a)</td><td>269.70 (n/a)</td><td>220.60 (n/a)</td><td>164.96 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.34 <b>(+24.66%)</b></td><td>0.22 (-0.76%)</td><td>0.23 (-8.95%)</td><td>0.11 <b>(-31.70%)</b></td><td>0.10 <b>(+66.44%)</b></td><td>690.60 <b>(+46.41%)</b></td><td>405.70 (+13.48%)</td><td>321.80 (+9.83%)</td><td>214.50 (-19.78%)</td><td>198.71 <b>(+92.33%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>471.70 (n/a)</td><td>357.50 (n/a)</td><td>293.00 (n/a)</td><td>267.40 (n/a)</td><td>103.32 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (-5.42%)</td><td>0.11 (-8.45%)</td><td>0.12 (-7.20%)</td><td>0.07 (-11.76%)</td><td>0.03 (-12.46%)</td><td>538.70 (+13.34%)</td><td>362.74 (+8.48%)</td><td>311.10 (+7.76%)</td><td>245.10 (+5.74%)</td><td>116.80 (+6.04%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>475.30 (n/a)</td><td>334.38 (n/a)</td><td>288.70 (n/a)</td><td>231.80 (n/a)</td><td>110.15 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (+4.05%)</td><td>0.10 (+2.20%)</td><td>0.08 (+10.26%)</td><td>0.06 (-16.65%)</td><td>0.04 <b>(+21.67%)</b></td><td>659.40 (+19.98%)</td><td>425.80 (+2.69%)</td><td>437.60 (-9.31%)</td><td>256.50 (-3.90%)</td><td>170.80 <b>(+34.09%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>549.60 (n/a)</td><td>414.64 (n/a)</td><td>482.50 (n/a)</td><td>266.90 (n/a)</td><td>127.38 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (-1.09%)</td><td>0.11 <b>(+25.57%)</b></td><td>0.13 <b>(+26.76%)</b></td><td>0.02 (-2.19%)</td><td>0.05 (-5.51%)</td><td>1959.60 (+2.24%)</td><td>623.40 (-19.91%)</td><td>276.00 <b>(-21.10%)</b></td><td>252.90 (+1.12%)</td><td>748.58 (+3.72%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1916.60 (n/a)</td><td>778.42 (n/a)</td><td>349.80 (n/a)</td><td>250.10 (n/a)</td><td>721.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.12 (-15.60%)</td><td>0.08 <b>(-27.98%)</b></td><td>0.07 <b>(-48.57%)</b></td><td>0.04 <b>(-37.46%)</b></td><td>0.03 (-8.38%)</td><td>819.90 <b>(+59.89%)</b></td><td>513.60 <b>(+44.47%)</b></td><td>543.70 <b>(+94.46%)</b></td><td>300.70 (+18.48%)</td><td>206.39 <b>(+67.36%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>512.80 (n/a)</td><td>355.50 (n/a)</td><td>279.60 (n/a)</td><td>253.80 (n/a)</td><td>123.32 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.16 (-1.11%)</td><td>0.11 (-2.35%)</td><td>0.11 (-10.24%)</td><td>0.08 (+17.00%)</td><td>0.03 <b>(-25.60%)</b></td><td>460.20 (-14.52%)</td><td>351.66 (-4.04%)</td><td>328.80 (+11.42%)</td><td>237.10 (+1.11%)</td><td>98.01 <b>(-34.91%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>538.40 (n/a)</td><td>366.46 (n/a)</td><td>295.10 (n/a)</td><td>234.50 (n/a)</td><td>150.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (-13.57%)</td><td>0.09 <b>(-28.86%)</b></td><td>0.07 <b>(-54.10%)</b></td><td>0.06 (-4.14%)</td><td>0.04 (-17.87%)</td><td>624.70 (+4.33%)</td><td>473.72 <b>(+37.63%)</b></td><td>543.80 <b>(+117.87%)</b></td><td>256.90 (+15.67%)</td><td>161.06 (+1.39%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>598.80 (n/a)</td><td>344.20 (n/a)</td><td>249.60 (n/a)</td><td>222.10 (n/a)</td><td>158.85 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 <b>(-22.50%)</b></td><td>0.10 <b>(-25.82%)</b></td><td>0.08 <b>(-46.75%)</b></td><td>0.07 (+4.97%)</td><td>0.03 <b>(-47.59%)</b></td><td>585.30 (-4.74%)</td><td>438.00 (+16.11%)</td><td>486.50 <b>(+87.77%)</b></td><td>271.40 <b>(+29.05%)</b></td><td>129.25 <b>(-37.64%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>614.40 (n/a)</td><td>377.22 (n/a)</td><td>259.10 (n/a)</td><td>210.30 (n/a)</td><td>207.26 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.16 (-15.49%)</td><td>0.12 (-2.66%)</td><td>0.13 (-11.68%)</td><td>0.08 <b>(+32.16%)</b></td><td>0.03 <b>(-39.77%)</b></td><td>500.30 <b>(-24.35%)</b></td><td>359.60 (-8.68%)</td><td>327.50 (+13.20%)</td><td>256.00 (+18.35%)</td><td>101.53 <b>(-47.38%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>661.30 (n/a)</td><td>393.80 (n/a)</td><td>289.30 (n/a)</td><td>216.30 (n/a)</td><td>192.94 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.16 (+1.04%)</td><td>0.11 (-5.09%)</td><td>0.09 (-19.76%)</td><td>0.08 <b>(+21.24%)</b></td><td>0.04 (-12.91%)</td><td>489.70 (-17.50%)</td><td>401.04 (+1.81%)</td><td>460.80 <b>(+24.64%)</b></td><td>249.80 (-1.03%)</td><td>108.32 <b>(-24.86%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>593.60 (n/a)</td><td>393.92 (n/a)</td><td>369.70 (n/a)</td><td>252.40 (n/a)</td><td>144.16 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 <b>(-48.27%)</b></td><td>0.07 <b>(-47.68%)</b></td><td>0.08 <b>(-48.70%)</b></td><td>0.02 <b>(-75.14%)</b></td><td>0.03 <b>(-35.39%)</b></td><td>2437.00 <b>(+302.21%)</b></td><td>880.54 <b>(+152.96%)</b></td><td>504.10 <b>(+94.93%)</b></td><td>448.30 <b>(+93.32%)</b></td><td>870.88 <b>(+446.59%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>605.90 (n/a)</td><td>348.10 (n/a)</td><td>258.60 (n/a)</td><td>231.90 (n/a)</td><td>159.33 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.23 <b>(+37.46%)</b></td><td>0.13 (+11.47%)</td><td>0.10 (+18.59%)</td><td>0.07 (-19.23%)</td><td>0.07 <b>(+60.30%)</b></td><td>605.50 <b>(+23.80%)</b></td><td>388.58 (-1.75%)</td><td>406.10 (-15.68%)</td><td>177.50 <b>(-27.22%)</b></td><td>168.47 <b>(+35.83%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>489.10 (n/a)</td><td>395.50 (n/a)</td><td>481.60 (n/a)</td><td>243.90 (n/a)</td><td>124.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (-15.59%)</td><td>0.09 (-17.56%)</td><td>0.09 (-6.67%)</td><td>0.06 (-11.50%)</td><td>0.03 <b>(-29.32%)</b></td><td>636.20 (+13.00%)</td><td>486.30 (+18.32%)</td><td>478.10 (+7.15%)</td><td>320.40 (+18.49%)</td><td>124.77 (-1.38%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>563.00 (n/a)</td><td>411.02 (n/a)</td><td>446.20 (n/a)</td><td>270.40 (n/a)</td><td>126.52 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (-14.89%)</td><td>0.11 <b>(+26.08%)</b></td><td>0.11 <b>(+41.46%)</b></td><td>0.08 <b>(+47.09%)</b></td><td>0.02 <b>(-50.20%)</b></td><td>417.00 <b>(-32.02%)</b></td><td>315.34 <b>(-28.83%)</b></td><td>319.10 <b>(-29.31%)</b></td><td>239.80 (+17.49%)</td><td>65.91 <b>(-56.38%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>613.40 (n/a)</td><td>443.08 (n/a)</td><td>451.40 (n/a)</td><td>204.10 (n/a)</td><td>151.08 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (-0.17%)</td><td>0.09 (-17.23%)</td><td>0.09 <b>(-22.44%)</b></td><td>0.06 (-5.68%)</td><td>0.03 (+7.38%)</td><td>545.50 (+6.03%)</td><td>403.32 <b>(+22.62%)</b></td><td>370.10 <b>(+28.91%)</b></td><td>255.60 (+0.16%)</td><td>124.52 (+16.10%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>514.50 (n/a)</td><td>328.92 (n/a)</td><td>287.10 (n/a)</td><td>255.20 (n/a)</td><td>107.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (-1.22%)</td><td>0.08 <b>(-21.06%)</b></td><td>0.08 (-9.84%)</td><td>0.04 <b>(-46.07%)</b></td><td>0.04 <b>(+24.25%)</b></td><td>801.00 <b>(+85.42%)</b></td><td>491.66 <b>(+37.88%)</b></td><td>442.30 (+10.94%)</td><td>252.20 (+1.24%)</td><td>202.91 <b>(+127.51%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>432.00 (n/a)</td><td>356.58 (n/a)</td><td>398.70 (n/a)</td><td>249.10 (n/a)</td><td>89.19 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (-0.47%)</td><td>0.09 (+7.59%)</td><td>0.07 (-4.25%)</td><td>0.05 (-3.11%)</td><td>0.03 <b>(+23.84%)</b></td><td>664.60 (+3.20%)</td><td>449.96 (-2.94%)</td><td>493.40 (+4.45%)</td><td>274.90 (+0.48%)</td><td>166.31 <b>(+26.31%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>644.00 (n/a)</td><td>463.60 (n/a)</td><td>472.40 (n/a)</td><td>273.60 (n/a)</td><td>131.66 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.16 (-0.02%)</td><td>0.10 (-1.10%)</td><td>0.12 <b>(+26.53%)</b></td><td>0.05 <b>(-38.67%)</b></td><td>0.05 <b>(+41.14%)</b></td><td>751.50 <b>(+63.05%)</b></td><td>425.22 (+19.22%)</td><td>281.60 <b>(-20.99%)</b></td><td>211.30 (+0.05%)</td><td>242.04 <b>(+139.37%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>460.90 (n/a)</td><td>356.66 (n/a)</td><td>356.40 (n/a)</td><td>211.20 (n/a)</td><td>101.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 <b>(+20.10%)</b></td><td>0.07 <b>(+22.04%)</b></td><td>0.08 <b>(+32.17%)</b></td><td>0.01 (-18.55%)</td><td>0.04 <b>(+20.89%)</b></td><td>2410.20 <b>(+22.78%)</b></td><td>834.38 (-2.99%)</td><td>440.60 <b>(-24.33%)</b></td><td>256.40 (-16.75%)</td><td>890.75 <b>(+34.62%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1963.00 (n/a)</td><td>860.12 (n/a)</td><td>582.30 (n/a)</td><td>308.00 (n/a)</td><td>661.67 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.49 (-1.08%)</td><td>0.35 (-1.60%)</td><td>0.30 (-12.68%)</td><td>0.23 (-5.33%)</td><td>0.11 (+10.17%)</td><td>576.30 (+5.63%)</td><td>405.32 (+3.26%)</td><td>439.80 (+14.53%)</td><td>266.90 (+1.10%)</td><td>127.37 (+13.09%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.50 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>545.60 (n/a)</td><td>392.54 (n/a)</td><td>384.00 (n/a)</td><td>264.00 (n/a)</td><td>112.62 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.61 <b>(+21.78%)</b></td><td>0.39 (+5.96%)</td><td>0.41 (-6.78%)</td><td>0.23 (+7.83%)</td><td>0.16 (+19.39%)</td><td>568.90 (-7.27%)</td><td>384.92 (-4.34%)</td><td>317.40 (+7.27%)</td><td>213.60 (-17.88%)</td><td>159.49 (-4.34%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.44 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>613.50 (n/a)</td><td>402.38 (n/a)</td><td>295.90 (n/a)</td><td>260.10 (n/a)</td><td>166.72 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.45 (+12.49%)</td><td>0.38 <b>(+74.44%)</b></td><td>0.43 <b>(+72.45%)</b></td><td>0.26 <b>(+286.96%)</b></td><td>0.09 <b>(-35.43%)</b></td><td>512.90 <b>(-74.16%)</b></td><td>369.80 <b>(-64.52%)</b></td><td>304.10 <b>(-42.01%)</b></td><td>289.60 (-11.11%)</td><td>104.42 <b>(-87.51%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.40 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>0.15 (n/a)</td><td>1984.60 (n/a)</td><td>1042.16 (n/a)</td><td>524.40 (n/a)</td><td>325.80 (n/a)</td><td>836.36 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.00 (+16.67%)</td><td>0.00 (-5.56%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 <b>(+54.56%)</b></td><td>21974.63 <b>(+34.76%)</b></td><td>15471.84 (+16.39%)</td><td>16234.94 (+14.93%)</td><td>5938.26 (-14.62%)</td><td>6288.28 <b>(+71.39%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>16306.22 (n/a)</td><td>13293.57 (n/a)</td><td>14125.64 (n/a)</td><td>6954.78 (n/a)</td><td>3668.89 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.00 (+7.14%)</td><td>0.00 <b>(+30.30%)</b></td><td>0.00 (+20.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+29.39%)</b></td><td>22411.25 (+11.90%)</td><td>13482.99 (-12.63%)</td><td>13366.10 <b>(-25.23%)</b></td><td>5514.06 (-6.42%)</td><td>7892.39 <b>(+38.19%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20028.56 (n/a)</td><td>15432.11 (n/a)</td><td>17875.96 (n/a)</td><td>5892.35 (n/a)</td><td>5711.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (+8.90%)</td><td>0.10 (+7.54%)</td><td>0.10 (+18.60%)</td><td>0.07 (-7.48%)</td><td>0.03 <b>(+30.34%)</b></td><td>29758.52 (+8.17%)</td><td>21463.81 (-4.59%)</td><td>20563.97 (-15.67%)</td><td>15306.58 (-8.16%)</td><td>6203.06 <b>(+28.05%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>27511.02 (n/a)</td><td>22495.50 (n/a)</td><td>24385.48 (n/a)</td><td>16667.23 (n/a)</td><td>4844.35 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>2.87 (+4.31%)</td><td>1.84 (-3.53%)</td><td>1.67 (+10.88%)</td><td>1.16 (-14.06%)</td><td>0.63 (-4.76%)</td><td>900.60 (+16.36%)</td><td>619.16 (+3.14%)</td><td>629.00 (-9.82%)</td><td>365.30 (-4.15%)</td><td>192.24 (+3.82%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>2.75 (n/a)</td><td>1.91 (n/a)</td><td>1.50 (n/a)</td><td>1.35 (n/a)</td><td>0.66 (n/a)</td><td>774.00 (n/a)</td><td>600.30 (n/a)</td><td>697.50 (n/a)</td><td>381.10 (n/a)</td><td>185.17 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.35 <b>(+30.43%)</b></td><td>1.99 <b>(+21.03%)</b></td><td>1.77 (-3.65%)</td><td>1.18 <b>(+177.40%)</b></td><td>0.81 (-12.05%)</td><td>888.50 <b>(-63.95%)</b></td><td>590.16 <b>(-40.45%)</b></td><td>593.00 (+3.80%)</td><td>313.10 <b>(-23.33%)</b></td><td>206.87 <b>(-76.14%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>2.57 (n/a)</td><td>1.64 (n/a)</td><td>1.84 (n/a)</td><td>0.43 (n/a)</td><td>0.93 (n/a)</td><td>2464.70 (n/a)</td><td>991.08 (n/a)</td><td>571.30 (n/a)</td><td>408.40 (n/a)</td><td>866.99 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.77 <b>(+33.93%)</b></td><td>2.13 (+6.77%)</td><td>1.80 (+2.61%)</td><td>1.55 (+12.75%)</td><td>0.92 <b>(+63.17%)</b></td><td>675.40 (-11.31%)</td><td>543.54 (-2.51%)</td><td>581.30 (-2.55%)</td><td>278.40 <b>(-25.32%)</b></td><td>153.27 (+2.28%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>2.81 (n/a)</td><td>2.00 (n/a)</td><td>1.76 (n/a)</td><td>1.38 (n/a)</td><td>0.56 (n/a)</td><td>761.50 (n/a)</td><td>557.56 (n/a)</td><td>596.50 (n/a)</td><td>372.80 (n/a)</td><td>149.85 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>2.95 <b>(-20.99%)</b></td><td>2.37 (-4.38%)</td><td>2.31 (+1.69%)</td><td>1.79 (-3.50%)</td><td>0.45 <b>(-40.30%)</b></td><td>585.70 (+3.63%)</td><td>455.68 (+1.35%)</td><td>454.60 (-1.67%)</td><td>355.20 <b>(+26.54%)</b></td><td>89.08 <b>(-20.40%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>3.74 (n/a)</td><td>2.48 (n/a)</td><td>2.27 (n/a)</td><td>1.86 (n/a)</td><td>0.75 (n/a)</td><td>565.20 (n/a)</td><td>449.62 (n/a)</td><td>462.30 (n/a)</td><td>280.70 (n/a)</td><td>111.91 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.06 (+2.02%)</td><td>2.39 (-0.83%)</td><td>2.99 (-12.40%)</td><td>0.59 (+1.49%)</td><td>1.69 (+0.84%)</td><td>3572.00 (-1.47%)</td><td>1775.74 (+0.69%)</td><td>702.40 (+14.16%)</td><td>516.20 (-1.99%)</td><td>1618.74 (-0.01%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>3.98 (n/a)</td><td>2.41 (n/a)</td><td>3.41 (n/a)</td><td>0.58 (n/a)</td><td>1.67 (n/a)</td><td>3625.20 (n/a)</td><td>1763.64 (n/a)</td><td>615.30 (n/a)</td><td>526.70 (n/a)</td><td>1618.82 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.30 <b>(-55.51%)</b></td><td>2.13 <b>(-28.01%)</b></td><td>2.89 (-0.75%)</td><td>0.59 (+2.38%)</td><td>1.41 <b>(-49.51%)</b></td><td>3543.40 (-2.32%)</td><td>1802.06 (+2.33%)</td><td>726.10 (+0.75%)</td><td>635.60 <b>(+124.75%)</b></td><td>1555.50 (-7.07%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>7.42 (n/a)</td><td>2.96 (n/a)</td><td>2.91 (n/a)</td><td>0.58 (n/a)</td><td>2.80 (n/a)</td><td>3627.60 (n/a)</td><td>1761.00 (n/a)</td><td>720.70 (n/a)</td><td>282.80 (n/a)</td><td>1673.89 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.89 (-5.73%)</td><td>3.35 <b>(+21.72%)</b></td><td>3.36 <b>(+71.80%)</b></td><td>0.60 <b>(-42.60%)</b></td><td>1.90 (-13.59%)</td><td>3520.50 <b>(+74.20%)</b></td><td>1146.74 (-5.25%)</td><td>624.80 <b>(-41.79%)</b></td><td>355.90 (+6.08%)</td><td>1332.83 <b>(+69.87%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>6.25 (n/a)</td><td>2.75 (n/a)</td><td>1.95 (n/a)</td><td>1.04 (n/a)</td><td>2.20 (n/a)</td><td>2020.90 (n/a)</td><td>1210.34 (n/a)</td><td>1073.40 (n/a)</td><td>335.50 (n/a)</td><td>784.63 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.68 (+6.70%)</td><td>3.79 <b>(+27.61%)</b></td><td>5.31 <b>(+70.87%)</b></td><td>0.58 (-0.22%)</td><td>2.45 <b>(+30.83%)</b></td><td>3587.70 (+0.22%)</td><td>1190.90 (-6.57%)</td><td>394.60 <b>(-41.48%)</b></td><td>369.40 (-6.29%)</td><td>1389.98 (+4.82%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>5.32 (n/a)</td><td>2.97 (n/a)</td><td>3.11 (n/a)</td><td>0.59 (n/a)</td><td>1.87 (n/a)</td><td>3579.80 (n/a)</td><td>1274.68 (n/a)</td><td>674.30 (n/a)</td><td>394.20 (n/a)</td><td>1326.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.81 <b>(+20.93%)</b></td><td>3.28 (+12.17%)</td><td>4.05 (+11.82%)</td><td>0.59 <b>(-51.36%)</b></td><td>1.66 <b>(+36.97%)</b></td><td>3565.60 <b>(+105.59%)</b></td><td>1153.72 <b>(+30.76%)</b></td><td>518.40 (-10.59%)</td><td>435.70 (-17.31%)</td><td>1352.97 <b>(+162.66%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>3.98 (n/a)</td><td>2.92 (n/a)</td><td>3.62 (n/a)</td><td>1.21 (n/a)</td><td>1.21 (n/a)</td><td>1734.30 (n/a)</td><td>882.34 (n/a)</td><td>579.80 (n/a)</td><td>526.90 (n/a)</td><td>515.10 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.10 <b>(-29.68%)</b></td><td>2.81 <b>(-22.86%)</b></td><td>3.57 <b>(-20.46%)</b></td><td>0.58 <b>(-31.84%)</b></td><td>1.59 <b>(-22.78%)</b></td><td>3600.30 <b>(+46.71%)</b></td><td>1290.32 <b>(+37.85%)</b></td><td>587.00 <b>(+25.72%)</b></td><td>510.90 <b>(+42.19%)</b></td><td>1326.95 <b>(+50.48%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>5.84 (n/a)</td><td>3.64 (n/a)</td><td>4.49 (n/a)</td><td>0.85 (n/a)</td><td>2.06 (n/a)</td><td>2454.10 (n/a)</td><td>936.00 (n/a)</td><td>466.90 (n/a)</td><td>359.30 (n/a)</td><td>881.83 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.27 <b>(+38.70%)</b></td><td>3.82 <b>(+25.42%)</b></td><td>4.19 <b>(+22.60%)</b></td><td>1.23 (+4.50%)</td><td>1.54 <b>(+45.81%)</b></td><td>3406.10 (-4.31%)</td><td>1444.20 (-13.57%)</td><td>1000.00 (-18.43%)</td><td>795.50 <b>(-27.90%)</b></td><td>1102.52 (+4.25%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>3.80 (n/a)</td><td>3.04 (n/a)</td><td>3.42 (n/a)</td><td>1.18 (n/a)</td><td>1.06 (n/a)</td><td>3559.50 (n/a)</td><td>1670.92 (n/a)</td><td>1225.90 (n/a)</td><td>1103.40 (n/a)</td><td>1057.54 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.77 (+2.79%)</td><td>6.41 <b>(+64.76%)</b></td><td>6.77 <b>(+104.87%)</b></td><td>3.79 <b>(+232.95%)</b></td><td>1.61 <b>(-45.34%)</b></td><td>1108.00 <b>(-69.97%)</b></td><td>700.90 <b>(-64.24%)</b></td><td>619.70 <b>(-51.19%)</b></td><td>539.60 (-2.72%)</td><td>234.81 <b>(-85.05%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>7.56 (n/a)</td><td>3.89 (n/a)</td><td>3.30 (n/a)</td><td>1.14 (n/a)</td><td>2.94 (n/a)</td><td>3689.10 (n/a)</td><td>1960.18 (n/a)</td><td>1269.60 (n/a)</td><td>554.70 (n/a)</td><td>1570.77 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>9.05 (+18.95%)</td><td>5.59 (-2.46%)</td><td>6.28 (-12.69%)</td><td>1.89 <b>(+73.41%)</b></td><td>3.37 <b>(+23.98%)</b></td><td>2217.30 <b>(-42.33%)</b></td><td>1139.96 (-9.82%)</td><td>667.90 (+14.54%)</td><td>463.20 (-15.93%)</td><td>831.59 <b>(-42.46%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>7.61 (n/a)</td><td>5.73 (n/a)</td><td>7.19 (n/a)</td><td>1.09 (n/a)</td><td>2.72 (n/a)</td><td>3844.90 (n/a)</td><td>1264.14 (n/a)</td><td>583.10 (n/a)</td><td>551.00 (n/a)</td><td>1445.11 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.76 (+8.34%)</td><td>5.29 (-13.84%)</td><td>6.83 (-1.53%)</td><td>1.14 <b>(-65.17%)</b></td><td>2.76 <b>(+69.31%)</b></td><td>3668.40 <b>(+187.11%)</b></td><td>1307.10 <b>(+75.08%)</b></td><td>613.90 (+1.56%)</td><td>540.40 (-7.69%)</td><td>1339.29 <b>(+348.44%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>7.16 (n/a)</td><td>6.14 (n/a)</td><td>6.94 (n/a)</td><td>3.28 (n/a)</td><td>1.63 (n/a)</td><td>1277.70 (n/a)</td><td>746.58 (n/a)</td><td>604.50 (n/a)</td><td>585.40 (n/a)</td><td>298.65 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>10.37 (+10.48%)</td><td>5.10 <b>(-20.20%)</b></td><td>5.63 (-12.04%)</td><td>1.38 (+9.43%)</td><td>3.55 (+10.07%)</td><td>3049.80 (-8.62%)</td><td>1353.78 <b>(+20.65%)</b></td><td>744.60 (+13.68%)</td><td>404.60 (-9.49%)</td><td>1095.41 (-11.90%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>9.38 (n/a)</td><td>6.39 (n/a)</td><td>6.40 (n/a)</td><td>1.26 (n/a)</td><td>3.23 (n/a)</td><td>3337.50 (n/a)</td><td>1122.06 (n/a)</td><td>655.00 (n/a)</td><td>447.00 (n/a)</td><td>1243.34 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>9.85 <b>(+32.16%)</b></td><td>5.64 (-2.95%)</td><td>4.39 <b>(-36.25%)</b></td><td>3.42 (-7.34%)</td><td>2.66 <b>(+45.05%)</b></td><td>1228.00 (+7.93%)</td><td>864.10 (+8.94%)</td><td>956.10 <b>(+56.87%)</b></td><td>425.80 <b>(-24.33%)</b></td><td>329.75 (+16.61%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>7.45 (n/a)</td><td>5.81 (n/a)</td><td>6.88 (n/a)</td><td>3.69 (n/a)</td><td>1.84 (n/a)</td><td>1137.80 (n/a)</td><td>793.22 (n/a)</td><td>609.50 (n/a)</td><td>562.70 (n/a)</td><td>282.79 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.66 (-6.61%)</td><td>1.11 (+1.24%)</td><td>0.97 (-15.73%)</td><td>0.57 <b>(+269.83%)</b></td><td>0.49 <b>(-21.43%)</b></td><td>913.30 <b>(-72.96%)</b></td><td>556.40 <b>(-44.98%)</b></td><td>538.90 (+18.67%)</td><td>316.80 (+7.10%)</td><td>252.67 <b>(-80.97%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>1.77 (n/a)</td><td>1.10 (n/a)</td><td>1.15 (n/a)</td><td>0.16 (n/a)</td><td>0.63 (n/a)</td><td>3377.70 (n/a)</td><td>1011.36 (n/a)</td><td>454.10 (n/a)</td><td>295.80 (n/a)</td><td>1327.58 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.99 <b>(+89.69%)</b></td><td>1.43 <b>(+74.05%)</b></td><td>1.47 <b>(+72.67%)</b></td><td>0.93 <b>(+86.53%)</b></td><td>0.39 <b>(+96.58%)</b></td><td>565.40 <b>(-46.39%)</b></td><td>390.98 <b>(-42.47%)</b></td><td>356.10 <b>(-42.08%)</b></td><td>264.10 <b>(-47.29%)</b></td><td>113.57 <b>(-47.29%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>1.05 (n/a)</td><td>0.82 (n/a)</td><td>0.85 (n/a)</td><td>0.50 (n/a)</td><td>0.20 (n/a)</td><td>1054.70 (n/a)</td><td>679.58 (n/a)</td><td>614.80 (n/a)</td><td>501.00 (n/a)</td><td>215.47 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (-1.64%)</td><td>0.09 (+17.49%)</td><td>0.09 <b>(+30.19%)</b></td><td>0.06 (-3.45%)</td><td>0.03 (+1.38%)</td><td>541.60 (+3.58%)</td><td>383.36 (-14.18%)</td><td>378.70 <b>(-23.18%)</b></td><td>242.40 (+1.68%)</td><td>129.38 (+9.93%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>522.90 (n/a)</td><td>446.70 (n/a)</td><td>493.00 (n/a)</td><td>238.40 (n/a)</td><td>117.69 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (+3.07%)</td><td>0.09 (+6.80%)</td><td>0.07 <b>(-21.66%)</b></td><td>0.06 <b>(+311.13%)</b></td><td>0.03 <b>(-26.67%)</b></td><td>528.60 <b>(-75.68%)</b></td><td>423.26 <b>(-41.54%)</b></td><td>496.50 <b>(+27.67%)</b></td><td>249.80 (-2.99%)</td><td>130.41 <b>(-83.99%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2173.20 (n/a)</td><td>724.06 (n/a)</td><td>388.90 (n/a)</td><td>257.50 (n/a)</td><td>814.54 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.27 (-0.48%)</td><td>0.17 (+3.23%)</td><td>0.12 (-3.44%)</td><td>0.11 (+3.87%)</td><td>0.07 (+6.34%)</td><td>615.80 (-3.72%)</td><td>444.90 (-1.72%)</td><td>525.90 (+3.56%)</td><td>246.70 (+0.49%)</td><td>160.59 (+4.68%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>639.60 (n/a)</td><td>452.68 (n/a)</td><td>507.80 (n/a)</td><td>245.50 (n/a)</td><td>153.41 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.24 (-2.26%)</td><td>0.20 (+14.19%)</td><td>0.22 <b>(+43.52%)</b></td><td>0.13 <b>(+25.48%)</b></td><td>0.04 <b>(-28.62%)</b></td><td>491.90 <b>(-20.31%)</b></td><td>349.36 (-16.82%)</td><td>301.90 <b>(-30.33%)</b></td><td>278.10 (+2.32%)</td><td>87.72 <b>(-38.54%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>617.30 (n/a)</td><td>420.00 (n/a)</td><td>433.30 (n/a)</td><td>271.80 (n/a)</td><td>142.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.30 <b>(+80.36%)</b></td><td>0.18 <b>(+35.78%)</b></td><td>0.15 (+15.73%)</td><td>0.12 (+15.35%)</td><td>0.07 <b>(+232.11%)</b></td><td>525.10 (-13.31%)</td><td>396.10 (-19.84%)</td><td>437.50 (-13.61%)</td><td>215.50 <b>(-44.54%)</b></td><td>126.79 <b>(+59.70%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>605.70 (n/a)</td><td>494.16 (n/a)</td><td>506.40 (n/a)</td><td>388.60 (n/a)</td><td>79.40 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.46 (-9.28%)</td><td>0.32 (+1.79%)</td><td>0.26 (+5.00%)</td><td>0.22 (+18.12%)</td><td>0.11 <b>(-25.27%)</b></td><td>596.60 (-15.33%)</td><td>448.86 (-8.72%)</td><td>506.60 (-4.76%)</td><td>285.70 (+10.22%)</td><td>136.76 <b>(-31.63%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.51 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>704.60 (n/a)</td><td>491.76 (n/a)</td><td>531.90 (n/a)</td><td>259.20 (n/a)</td><td>200.04 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.45 (+2.90%)</td><td>0.31 <b>(+35.96%)</b></td><td>0.34 <b>(+65.72%)</b></td><td>0.07 (+1.64%)</td><td>0.16 (+19.87%)</td><td>1871.10 (-1.61%)</td><td>679.34 (-16.92%)</td><td>386.40 <b>(-39.65%)</b></td><td>290.90 (-2.81%)</td><td>674.71 (+8.23%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.44 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>0.13 (n/a)</td><td>1901.70 (n/a)</td><td>817.66 (n/a)</td><td>640.30 (n/a)</td><td>299.30 (n/a)</td><td>623.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.62 <b>(+22.89%)</b></td><td>0.37 <b>(+36.23%)</b></td><td>0.29 (+9.03%)</td><td>0.23 <b>(+240.92%)</b></td><td>0.18 (+3.42%)</td><td>577.60 <b>(-70.67%)</b></td><td>414.82 <b>(-46.48%)</b></td><td>454.00 (-8.28%)</td><td>210.90 (-18.63%)</td><td>169.81 <b>(-75.64%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.51 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td><td>1969.10 (n/a)</td><td>775.14 (n/a)</td><td>495.00 (n/a)</td><td>259.20 (n/a)</td><td>697.21 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 <b>(+44.10%)</b></td><td>0.04 <b>(+25.65%)</b></td><td>0.04 <b>(+27.43%)</b></td><td>0.03 (+6.21%)</td><td>0.01 <b>(+100.30%)</b></td><td>569.90 (-5.85%)</td><td>415.38 (-17.40%)</td><td>404.10 <b>(-21.53%)</b></td><td>263.60 <b>(-30.60%)</b></td><td>110.35 <b>(+29.11%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-11 23:33:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>605.30 (n/a)</td><td>502.90 (n/a)</td><td>515.00 (n/a)</td><td>379.80 (n/a)</td><td>85.47 (n/a)</td>
</tr>
</tbody>
</table>


</details>
