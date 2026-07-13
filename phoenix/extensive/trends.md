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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (+3.48%)</td><td>0.01 (-13.03%)</td><td>0.01 (-14.91%)</td><td>0.01 (-5.17%)</td><td>0.01 (+6.72%)</td><td>613.70 (+5.46%)</td><td>501.30 (+16.22%)</td><td>542.70 (+17.52%)</td><td>231.30 (-3.34%)</td><td>157.79 (+1.75%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.90 (n/a)</td><td>431.34 (n/a)</td><td>461.80 (n/a)</td><td>239.30 (n/a)</td><td>155.09 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-10.98%)</td><td>0.02 (+10.97%)</td><td>0.02 <b>(+52.22%)</b></td><td>0.01 (+5.95%)</td><td>0.00 <b>(-38.82%)</b></td><td>489.60 (-5.61%)</td><td>340.98 (-15.09%)</td><td>310.70 <b>(-34.30%)</b></td><td>278.50 (+12.34%)</td><td>86.68 <b>(-33.91%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>518.70 (n/a)</td><td>401.56 (n/a)</td><td>472.90 (n/a)</td><td>247.90 (n/a)</td><td>131.16 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 <b>(+50.26%)</b></td><td>0.02 <b>(+46.36%)</b></td><td>0.02 <b>(+75.89%)</b></td><td>0.01 <b>(+234.41%)</b></td><td>0.01 (+12.41%)</td><td>558.90 <b>(-70.09%)</b></td><td>359.04 <b>(-49.25%)</b></td><td>295.80 <b>(-43.14%)</b></td><td>191.80 <b>(-33.43%)</b></td><td>157.10 <b>(-76.27%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1868.90 (n/a)</td><td>707.44 (n/a)</td><td>520.20 (n/a)</td><td>288.10 (n/a)</td><td>661.94 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 <b>(+23.59%)</b></td><td>0.02 (+9.74%)</td><td>0.01 (+7.07%)</td><td>0.01 (+4.07%)</td><td>0.01 <b>(+33.84%)</b></td><td>592.10 (-3.91%)</td><td>446.98 (-6.13%)</td><td>485.90 (-6.61%)</td><td>195.00 (-19.09%)</td><td>149.53 (-6.67%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.20 (n/a)</td><td>476.16 (n/a)</td><td>520.30 (n/a)</td><td>241.00 (n/a)</td><td>160.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 <b>(-29.00%)</b></td><td>0.01 <b>(-39.57%)</b></td><td>0.01 <b>(-48.83%)</b></td><td>0.00 <b>(-74.77%)</b></td><td>0.01 (-6.04%)</td><td>2170.70 <b>(+296.26%)</b></td><td>877.74 <b>(+122.83%)</b></td><td>638.20 <b>(+95.41%)</b></td><td>321.30 <b>(+40.86%)</b></td><td>745.80 <b>(+414.32%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.80 (n/a)</td><td>393.90 (n/a)</td><td>326.60 (n/a)</td><td>228.10 (n/a)</td><td>145.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (-1.60%)</td><td>0.01 <b>(-21.24%)</b></td><td>0.01 <b>(-25.40%)</b></td><td>0.00 <b>(-68.55%)</b></td><td>0.01 <b>(+33.03%)</b></td><td>1828.80 <b>(+217.94%)</b></td><td>689.10 <b>(+86.75%)</b></td><td>510.80 <b>(+34.07%)</b></td><td>228.10 (+1.65%)</td><td>653.46 <b>(+366.24%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.20 (n/a)</td><td>369.00 (n/a)</td><td>381.00 (n/a)</td><td>224.40 (n/a)</td><td>140.15 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-9.02%)</td><td>0.04 (-1.47%)</td><td>0.04 (+16.13%)</td><td>0.02 (-11.98%)</td><td>0.01 (-16.73%)</td><td>589.80 (+13.62%)</td><td>329.10 (+1.16%)</td><td>290.10 (-13.89%)</td><td>217.50 (+9.90%)</td><td>149.52 (+15.94%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>519.10 (n/a)</td><td>325.34 (n/a)</td><td>336.90 (n/a)</td><td>197.90 (n/a)</td><td>128.96 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 <b>(+41.67%)</b></td><td>0.04 <b>(+63.54%)</b></td><td>0.04 <b>(+88.12%)</b></td><td>0.02 <b>(+29.44%)</b></td><td>0.02 <b>(+36.38%)</b></td><td>534.50 <b>(-22.74%)</b></td><td>322.22 <b>(-38.69%)</b></td><td>301.10 <b>(-46.84%)</b></td><td>190.80 <b>(-29.44%)</b></td><td>131.46 <b>(-22.88%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>691.80 (n/a)</td><td>525.56 (n/a)</td><td>566.40 (n/a)</td><td>270.40 (n/a)</td><td>170.45 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (+15.99%)</td><td>0.04 (+14.23%)</td><td>0.03 <b>(+36.56%)</b></td><td>0.02 (-2.16%)</td><td>0.02 <b>(+26.60%)</b></td><td>632.90 (+2.20%)</td><td>425.58 (-6.58%)</td><td>366.40 <b>(-26.76%)</b></td><td>187.30 (-13.81%)</td><td>190.50 <b>(+26.46%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>619.30 (n/a)</td><td>455.56 (n/a)</td><td>500.30 (n/a)</td><td>217.30 (n/a)</td><td>150.65 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (-12.37%)</td><td>0.03 (-18.58%)</td><td>0.03 <b>(-28.45%)</b></td><td>0.03 (-11.52%)</td><td>0.01 (+7.05%)</td><td>470.80 (+13.04%)</td><td>375.36 <b>(+24.75%)</b></td><td>407.10 <b>(+39.75%)</b></td><td>264.60 (+14.10%)</td><td>91.82 <b>(+32.23%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>416.50 (n/a)</td><td>300.88 (n/a)</td><td>291.30 (n/a)</td><td>231.90 (n/a)</td><td>69.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-6.15%)</td><td>0.03 (+2.35%)</td><td>0.03 <b>(+54.38%)</b></td><td>0.01 (-2.99%)</td><td>0.02 (-13.44%)</td><td>1966.60 (+3.08%)</td><td>686.88 (-4.07%)</td><td>368.90 <b>(-35.24%)</b></td><td>222.10 (+6.52%)</td><td>723.15 (+5.14%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1907.80 (n/a)</td><td>716.04 (n/a)</td><td>569.60 (n/a)</td><td>208.50 (n/a)</td><td>687.76 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 <b>(-38.39%)</b></td><td>0.03 (-6.40%)</td><td>0.03 (+0.04%)</td><td>0.02 (+9.59%)</td><td>0.01 <b>(-58.38%)</b></td><td>546.40 (-8.77%)</td><td>453.14 (-3.95%)</td><td>485.90 (-0.04%)</td><td>338.90 <b>(+62.31%)</b></td><td>101.05 <b>(-35.49%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>598.90 (n/a)</td><td>471.76 (n/a)</td><td>486.10 (n/a)</td><td>208.80 (n/a)</td><td>156.65 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (+5.79%)</td><td>0.07 (-4.92%)</td><td>0.08 (-13.07%)</td><td>0.04 (-0.55%)</td><td>0.03 (+2.72%)</td><td>597.60 (+0.56%)</td><td>374.62 (+5.17%)</td><td>318.40 (+15.03%)</td><td>229.90 (-5.47%)</td><td>144.00 (-0.98%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>594.30 (n/a)</td><td>356.22 (n/a)</td><td>276.80 (n/a)</td><td>243.20 (n/a)</td><td>145.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.10 (-15.56%)</td><td>0.07 <b>(-21.69%)</b></td><td>0.08 (-12.77%)</td><td>0.04 <b>(-27.55%)</b></td><td>0.02 (+8.68%)</td><td>589.00 <b>(+38.00%)</b></td><td>389.74 <b>(+34.74%)</b></td><td>315.60 (+14.64%)</td><td>246.60 (+18.39%)</td><td>150.73 <b>(+78.56%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>426.80 (n/a)</td><td>289.26 (n/a)</td><td>275.30 (n/a)</td><td>208.30 (n/a)</td><td>84.41 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 <b>(+27.91%)</b></td><td>0.08 (-15.21%)</td><td>0.08 (-14.56%)</td><td>0.05 <b>(-35.27%)</b></td><td>0.03 <b>(+176.37%)</b></td><td>524.50 <b>(+54.49%)</b></td><td>356.24 <b>(+32.47%)</b></td><td>298.20 (+17.03%)</td><td>190.30 <b>(-21.82%)</b></td><td>138.07 <b>(+242.28%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>339.50 (n/a)</td><td>268.92 (n/a)</td><td>254.80 (n/a)</td><td>243.40 (n/a)</td><td>40.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (+12.39%)</td><td>0.07 (-18.89%)</td><td>0.05 <b>(-34.86%)</b></td><td>0.05 (-18.43%)</td><td>0.03 <b>(+37.55%)</b></td><td>537.70 <b>(+22.59%)</b></td><td>414.04 <b>(+30.01%)</b></td><td>455.00 <b>(+53.51%)</b></td><td>204.70 (-11.04%)</td><td>125.94 <b>(+40.18%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>438.60 (n/a)</td><td>318.48 (n/a)</td><td>296.40 (n/a)</td><td>230.10 (n/a)</td><td>89.84 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (-1.22%)</td><td>0.06 (-19.73%)</td><td>0.06 <b>(-24.13%)</b></td><td>0.04 <b>(-28.11%)</b></td><td>0.01 <b>(+41.99%)</b></td><td>569.40 <b>(+39.12%)</b></td><td>426.18 <b>(+28.38%)</b></td><td>404.50 <b>(+31.80%)</b></td><td>296.60 (+1.23%)</td><td>101.93 <b>(+102.21%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>409.30 (n/a)</td><td>331.96 (n/a)</td><td>306.90 (n/a)</td><td>293.00 (n/a)</td><td>50.41 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 <b>(-20.85%)</b></td><td>0.07 (-13.22%)</td><td>0.07 <b>(-36.19%)</b></td><td>0.05 (+15.45%)</td><td>0.03 <b>(-34.03%)</b></td><td>528.00 (-13.39%)</td><td>370.00 (+0.43%)</td><td>377.20 <b>(+56.71%)</b></td><td>224.00 <b>(+26.34%)</b></td><td>134.38 <b>(-35.99%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>609.60 (n/a)</td><td>368.42 (n/a)</td><td>240.70 (n/a)</td><td>177.30 (n/a)</td><td>209.94 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.20 (+14.54%)</td><td>0.15 (+8.13%)</td><td>0.18 (+10.08%)</td><td>0.03 <b>(-67.34%)</b></td><td>0.07 <b>(+66.82%)</b></td><td>1927.70 <b>(+206.23%)</b></td><td>608.14 <b>(+54.27%)</b></td><td>269.90 (-9.16%)</td><td>244.10 (-12.70%)</td><td>738.90 <b>(+382.61%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>629.50 (n/a)</td><td>394.20 (n/a)</td><td>297.10 (n/a)</td><td>279.60 (n/a)</td><td>153.11 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.23 (+7.19%)</td><td>0.16 (-12.02%)</td><td>0.16 (-18.21%)</td><td>0.11 <b>(-20.09%)</b></td><td>0.06 <b>(+69.60%)</b></td><td>464.50 <b>(+25.17%)</b></td><td>332.34 <b>(+21.81%)</b></td><td>308.90 <b>(+22.24%)</b></td><td>210.00 (-6.71%)</td><td>115.82 <b>(+98.83%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>371.10 (n/a)</td><td>272.84 (n/a)</td><td>252.70 (n/a)</td><td>225.10 (n/a)</td><td>58.25 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.17 (-19.66%)</td><td>0.13 (-0.38%)</td><td>0.14 <b>(+31.49%)</b></td><td>0.07 (-13.96%)</td><td>0.04 <b>(-32.38%)</b></td><td>737.60 (+16.23%)</td><td>426.98 (-4.25%)</td><td>354.50 <b>(-23.96%)</b></td><td>290.70 <b>(+24.50%)</b></td><td>180.49 (+0.49%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>634.60 (n/a)</td><td>445.92 (n/a)</td><td>466.20 (n/a)</td><td>233.50 (n/a)</td><td>179.61 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.24 <b>(+24.60%)</b></td><td>0.15 (+10.08%)</td><td>0.16 <b>(+38.86%)</b></td><td>0.08 <b>(-20.21%)</b></td><td>0.06 <b>(+43.76%)</b></td><td>595.00 <b>(+25.32%)</b></td><td>368.28 (-2.33%)</td><td>305.20 <b>(-27.98%)</b></td><td>206.60 (-19.77%)</td><td>159.53 <b>(+50.37%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>474.80 (n/a)</td><td>377.08 (n/a)</td><td>423.80 (n/a)</td><td>257.50 (n/a)</td><td>106.09 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 <b>(-55.09%)</b></td><td>0.07 <b>(-42.62%)</b></td><td>0.08 (-17.88%)</td><td>0.02 <b>(-65.58%)</b></td><td>0.03 <b>(-48.54%)</b></td><td>2428.40 <b>(+190.55%)</b></td><td>953.68 <b>(+101.83%)</b></td><td>581.70 <b>(+21.77%)</b></td><td>546.70 <b>(+122.69%)</b></td><td>824.98 <b>(+257.16%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>835.80 (n/a)</td><td>472.52 (n/a)</td><td>477.70 (n/a)</td><td>245.50 (n/a)</td><td>230.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.19 (+2.45%)</td><td>0.12 (-9.82%)</td><td>0.11 (-18.79%)</td><td>0.08 (-5.64%)</td><td>0.05 (+0.79%)</td><td>600.30 (+5.99%)</td><td>454.90 (+11.01%)</td><td>465.40 <b>(+23.12%)</b></td><td>254.20 (-2.38%)</td><td>144.45 (+1.88%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>566.40 (n/a)</td><td>409.80 (n/a)</td><td>378.00 (n/a)</td><td>260.40 (n/a)</td><td>141.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (+7.71%)</td><td>0.01 (-4.67%)</td><td>0.01 (-17.04%)</td><td>0.00 (-9.76%)</td><td>0.00 <b>(+42.60%)</b></td><td>543.50 (+10.83%)</td><td>382.54 (+12.53%)</td><td>354.30 <b>(+20.55%)</b></td><td>227.80 (-7.17%)</td><td>154.04 <b>(+50.55%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>490.40 (n/a)</td><td>339.96 (n/a)</td><td>293.90 (n/a)</td><td>245.40 (n/a)</td><td>102.31 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (-11.68%)</td><td>0.01 <b>(-21.63%)</b></td><td>0.01 <b>(-33.20%)</b></td><td>0.00 (-3.74%)</td><td>0.00 (-9.26%)</td><td>577.80 (+3.88%)</td><td>467.42 <b>(+26.95%)</b></td><td>521.50 <b>(+49.68%)</b></td><td>237.80 (+13.24%)</td><td>134.09 (+1.11%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>556.20 (n/a)</td><td>368.18 (n/a)</td><td>348.40 (n/a)</td><td>210.00 (n/a)</td><td>132.62 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 <b>(-20.92%)</b></td><td>0.01 <b>(-23.99%)</b></td><td>0.00 <b>(-30.18%)</b></td><td>0.00 (-5.53%)</td><td>0.00 <b>(-25.72%)</b></td><td>605.40 (+5.86%)</td><td>476.56 <b>(+26.66%)</b></td><td>529.90 <b>(+43.22%)</b></td><td>236.10 <b>(+26.46%)</b></td><td>152.93 (-1.77%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>571.90 (n/a)</td><td>376.26 (n/a)</td><td>370.00 (n/a)</td><td>186.70 (n/a)</td><td>155.69 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (+16.27%)</td><td>0.01 <b>(-27.30%)</b></td><td>0.00 <b>(-50.19%)</b></td><td>0.00 <b>(-65.36%)</b></td><td>0.00 <b>(+20.18%)</b></td><td>2358.70 <b>(+188.67%)</b></td><td>828.14 <b>(+98.48%)</b></td><td>532.00 <b>(+100.75%)</b></td><td>224.60 (-13.98%)</td><td>865.69 <b>(+257.38%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>817.10 (n/a)</td><td>417.24 (n/a)</td><td>265.00 (n/a)</td><td>261.10 (n/a)</td><td>242.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 <b>(+50.49%)</b></td><td>0.01 <b>(+39.69%)</b></td><td>0.01 <b>(+50.51%)</b></td><td>0.01 <b>(+35.98%)</b></td><td>0.00 <b>(+90.05%)</b></td><td>442.90 <b>(-26.47%)</b></td><td>339.08 <b>(-26.56%)</b></td><td>306.10 <b>(-33.57%)</b></td><td>239.20 <b>(-33.56%)</b></td><td>90.32 (-3.15%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>602.30 (n/a)</td><td>461.74 (n/a)</td><td>460.80 (n/a)</td><td>360.00 (n/a)</td><td>93.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (+1.38%)</td><td>0.01 (-16.68%)</td><td>0.00 <b>(-27.20%)</b></td><td>0.00 (-2.66%)</td><td>0.00 (+18.32%)</td><td>557.80 (+2.73%)</td><td>507.04 <b>(+20.90%)</b></td><td>545.20 <b>(+37.36%)</b></td><td>361.30 (-1.37%)</td><td>82.92 (+15.72%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>543.00 (n/a)</td><td>419.38 (n/a)</td><td>396.90 (n/a)</td><td>366.30 (n/a)</td><td>71.66 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 <b>(+86.61%)</b></td><td>0.02 <b>(+41.84%)</b></td><td>0.01 <b>(+28.86%)</b></td><td>0.01 (+2.04%)</td><td>0.01 <b>(+332.34%)</b></td><td>599.80 (-1.99%)</td><td>388.48 <b>(-22.21%)</b></td><td>361.70 <b>(-22.40%)</b></td><td>240.90 <b>(-46.41%)</b></td><td>146.86 <b>(+121.60%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>612.00 (n/a)</td><td>499.42 (n/a)</td><td>466.10 (n/a)</td><td>449.50 (n/a)</td><td>66.27 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-3.88%)</td><td>0.02 <b>(+37.01%)</b></td><td>0.02 <b>(+80.74%)</b></td><td>0.01 <b>(+336.89%)</b></td><td>0.00 <b>(-54.27%)</b></td><td>441.20 <b>(-77.11%)</b></td><td>333.04 <b>(-54.36%)</b></td><td>321.70 <b>(-44.68%)</b></td><td>262.40 (+4.00%)</td><td>74.25 <b>(-89.23%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1927.70 (n/a)</td><td>729.78 (n/a)</td><td>581.50 (n/a)</td><td>252.30 (n/a)</td><td>689.11 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-0.26%)</td><td>0.01 <b>(-34.18%)</b></td><td>0.01 <b>(-54.19%)</b></td><td>0.00 <b>(-33.29%)</b></td><td>0.01 (+2.80%)</td><td>1111.40 <b>(+49.91%)</b></td><td>634.68 <b>(+63.81%)</b></td><td>607.00 <b>(+118.27%)</b></td><td>232.70 (+0.26%)</td><td>329.65 <b>(+52.43%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>741.40 (n/a)</td><td>387.46 (n/a)</td><td>278.10 (n/a)</td><td>232.10 (n/a)</td><td>216.27 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (+11.48%)</td><td>0.01 (-17.46%)</td><td>0.01 <b>(-39.15%)</b></td><td>0.01 (-6.70%)</td><td>0.01 <b>(+32.52%)</b></td><td>547.10 (+7.19%)</td><td>410.60 <b>(+27.63%)</b></td><td>474.40 <b>(+64.32%)</b></td><td>192.20 (-10.27%)</td><td>142.46 <b>(+21.59%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>510.40 (n/a)</td><td>321.70 (n/a)</td><td>288.70 (n/a)</td><td>214.20 (n/a)</td><td>117.16 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (+0.90%)</td><td>0.02 (+7.35%)</td><td>0.01 <b>(-21.35%)</b></td><td>0.01 <b>(+65.52%)</b></td><td>0.01 (-7.30%)</td><td>646.10 <b>(-39.59%)</b></td><td>396.54 (-18.82%)</td><td>406.70 <b>(+27.13%)</b></td><td>237.50 (-0.88%)</td><td>168.25 <b>(-50.67%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1069.50 (n/a)</td><td>488.46 (n/a)</td><td>319.90 (n/a)</td><td>239.60 (n/a)</td><td>341.10 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 <b>(-26.42%)</b></td><td>0.01 (-11.16%)</td><td>0.01 <b>(-25.73%)</b></td><td>0.01 <b>(+220.87%)</b></td><td>0.00 <b>(-73.48%)</b></td><td>623.30 <b>(-68.83%)</b></td><td>548.76 <b>(-25.02%)</b></td><td>547.90 <b>(+34.65%)</b></td><td>449.60 <b>(+35.91%)</b></td><td>73.17 <b>(-89.73%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1999.90 (n/a)</td><td>731.92 (n/a)</td><td>406.90 (n/a)</td><td>330.80 (n/a)</td><td>712.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (+11.11%)</td><td>0.03 (+6.02%)</td><td>0.03 (-15.75%)</td><td>0.02 (+17.89%)</td><td>0.01 (-5.17%)</td><td>522.60 (-15.18%)</td><td>377.86 (-9.18%)</td><td>397.20 (+18.71%)</td><td>240.50 (-9.99%)</td><td>108.58 <b>(-31.31%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>616.10 (n/a)</td><td>416.04 (n/a)</td><td>334.60 (n/a)</td><td>267.20 (n/a)</td><td>158.07 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (+19.31%)</td><td>0.03 <b>(+50.44%)</b></td><td>0.04 <b>(+70.57%)</b></td><td>0.02 <b>(+101.76%)</b></td><td>0.01 (+14.77%)</td><td>553.00 <b>(-50.43%)</b></td><td>353.18 <b>(-38.66%)</b></td><td>275.30 <b>(-41.38%)</b></td><td>216.80 (-16.16%)</td><td>152.07 <b>(-52.95%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1115.70 (n/a)</td><td>575.74 (n/a)</td><td>469.60 (n/a)</td><td>258.60 (n/a)</td><td>323.19 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (+13.20%)</td><td>0.03 (+8.47%)</td><td>0.04 <b>(+27.07%)</b></td><td>0.02 (-5.75%)</td><td>0.01 <b>(+48.97%)</b></td><td>609.50 (+6.11%)</td><td>356.68 (-0.51%)</td><td>240.30 <b>(-21.29%)</b></td><td>232.80 (-11.68%)</td><td>171.48 <b>(+32.45%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>574.40 (n/a)</td><td>358.50 (n/a)</td><td>305.30 (n/a)</td><td>263.60 (n/a)</td><td>129.46 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (-16.54%)</td><td>0.03 (-15.34%)</td><td>0.02 <b>(-37.16%)</b></td><td>0.02 <b>(+45.11%)</b></td><td>0.01 <b>(-33.61%)</b></td><td>565.00 <b>(-31.08%)</b></td><td>436.70 (+2.30%)</td><td>500.50 <b>(+59.14%)</b></td><td>257.50 (+19.82%)</td><td>145.35 <b>(-43.04%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>819.80 (n/a)</td><td>426.90 (n/a)</td><td>314.50 (n/a)</td><td>214.90 (n/a)</td><td>255.18 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (+9.03%)</td><td>0.02 (+17.66%)</td><td>0.02 (+8.78%)</td><td>0.02 <b>(+262.52%)</b></td><td>0.01 <b>(-30.49%)</b></td><td>568.80 <b>(-72.41%)</b></td><td>477.76 <b>(-39.96%)</b></td><td>499.30 (-8.06%)</td><td>292.50 (-8.28%)</td><td>109.89 <b>(-84.70%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2061.90 (n/a)</td><td>795.72 (n/a)</td><td>543.10 (n/a)</td><td>318.90 (n/a)</td><td>718.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 <b>(-35.48%)</b></td><td>0.03 (-18.49%)</td><td>0.02 (-16.50%)</td><td>0.02 (+18.18%)</td><td>0.01 <b>(-56.32%)</b></td><td>518.40 (-15.39%)</td><td>415.30 (+8.81%)</td><td>444.60 (+19.74%)</td><td>271.60 <b>(+54.93%)</b></td><td>91.68 <b>(-42.73%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>612.70 (n/a)</td><td>381.68 (n/a)</td><td>371.30 (n/a)</td><td>175.30 (n/a)</td><td>160.08 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (-6.64%)</td><td>0.07 (-2.38%)</td><td>0.07 (-16.72%)</td><td>0.04 <b>(+27.68%)</b></td><td>0.02 <b>(-36.84%)</b></td><td>512.80 <b>(-21.67%)</b></td><td>334.52 (-6.55%)</td><td>298.80 <b>(+20.10%)</b></td><td>260.30 (+7.08%)</td><td>102.45 <b>(-42.42%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>654.70 (n/a)</td><td>357.96 (n/a)</td><td>248.80 (n/a)</td><td>243.10 (n/a)</td><td>177.93 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (-0.64%)</td><td>0.06 (+16.09%)</td><td>0.07 <b>(+38.13%)</b></td><td>0.04 (+18.90%)</td><td>0.02 (-6.67%)</td><td>521.70 (-15.90%)</td><td>354.52 (-15.52%)</td><td>301.50 <b>(-27.61%)</b></td><td>244.20 (+0.66%)</td><td>114.25 (-18.15%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>620.30 (n/a)</td><td>419.64 (n/a)</td><td>416.50 (n/a)</td><td>242.60 (n/a)</td><td>139.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 <b>(-26.81%)</b></td><td>0.06 (-15.63%)</td><td>0.08 (+8.15%)</td><td>0.01 <b>(-70.05%)</b></td><td>0.03 (-3.55%)</td><td>1944.30 <b>(+233.84%)</b></td><td>637.16 <b>(+80.15%)</b></td><td>263.10 (-7.52%)</td><td>238.20 <b>(+36.66%)</b></td><td>737.87 <b>(+324.29%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>582.40 (n/a)</td><td>353.68 (n/a)</td><td>284.50 (n/a)</td><td>174.30 (n/a)</td><td>173.91 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (-0.49%)</td><td>0.06 <b>(+26.04%)</b></td><td>0.08 <b>(+82.08%)</b></td><td>0.04 (-0.91%)</td><td>0.02 (+15.72%)</td><td>574.80 (+0.91%)</td><td>381.92 (-16.87%)</td><td>273.20 <b>(-45.09%)</b></td><td>241.50 (+0.50%)</td><td>167.11 <b>(+30.28%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>569.60 (n/a)</td><td>459.44 (n/a)</td><td>497.50 (n/a)</td><td>240.30 (n/a)</td><td>128.27 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (+8.15%)</td><td>0.05 <b>(-28.16%)</b></td><td>0.04 <b>(-48.40%)</b></td><td>0.01 (-2.45%)</td><td>0.04 <b>(+24.55%)</b></td><td>1935.40 (+2.52%)</td><td>983.04 <b>(+64.06%)</b></td><td>540.80 <b>(+93.84%)</b></td><td>251.30 (-7.54%)</td><td>875.20 <b>(+21.48%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1887.90 (n/a)</td><td>599.20 (n/a)</td><td>279.00 (n/a)</td><td>271.80 (n/a)</td><td>720.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 <b>(+25.25%)</b></td><td>0.05 <b>(+23.51%)</b></td><td>0.05 <b>(+24.63%)</b></td><td>0.04 (-3.66%)</td><td>0.02 <b>(+98.58%)</b></td><td>596.30 (+3.79%)</td><td>450.10 (-14.25%)</td><td>451.20 (-19.76%)</td><td>300.50 <b>(-20.16%)</b></td><td>140.68 <b>(+68.19%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>574.50 (n/a)</td><td>524.88 (n/a)</td><td>562.30 (n/a)</td><td>376.40 (n/a)</td><td>83.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1950.20 (n/a)</td><td>702.02 (n/a)</td><td>478.00 (n/a)</td><td>263.70 (n/a)</td><td>709.07 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.00 (n/a)</td><td>405.62 (n/a)</td><td>464.90 (n/a)</td><td>229.80 (n/a)</td><td>159.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>442.80 (n/a)</td><td>303.16 (n/a)</td><td>323.60 (n/a)</td><td>148.90 (n/a)</td><td>111.97 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>419.70 (n/a)</td><td>284.00 (n/a)</td><td>276.60 (n/a)</td><td>177.10 (n/a)</td><td>87.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>593.90 (n/a)</td><td>418.94 (n/a)</td><td>355.00 (n/a)</td><td>256.50 (n/a)</td><td>147.77 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>631.90 (n/a)</td><td>330.88 (n/a)</td><td>261.40 (n/a)</td><td>214.10 (n/a)</td><td>171.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>531.80 (n/a)</td><td>307.66 (n/a)</td><td>274.50 (n/a)</td><td>227.50 (n/a)</td><td>127.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>516.00 (n/a)</td><td>330.00 (n/a)</td><td>254.70 (n/a)</td><td>239.60 (n/a)</td><td>123.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>562.20 (n/a)</td><td>413.38 (n/a)</td><td>378.60 (n/a)</td><td>308.90 (n/a)</td><td>98.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.19 <b>(-20.58%)</b></td><td>0.14 (-10.61%)</td><td>0.16 (-7.85%)</td><td>0.09 (+0.51%)</td><td>0.05 <b>(-22.24%)</b></td><td>573.40 (-0.50%)</td><td>387.64 (+8.30%)</td><td>313.90 (+8.50%)</td><td>265.50 <b>(+25.89%)</b></td><td>145.50 (-5.36%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>576.30 (n/a)</td><td>357.94 (n/a)</td><td>289.30 (n/a)</td><td>210.90 (n/a)</td><td>153.74 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>592.70 (n/a)</td><td>392.42 (n/a)</td><td>323.90 (n/a)</td><td>244.60 (n/a)</td><td>154.22 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>595.30 (n/a)</td><td>447.30 (n/a)</td><td>448.00 (n/a)</td><td>233.10 (n/a)</td><td>139.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.50 (n/a)</td><td>425.92 (n/a)</td><td>515.70 (n/a)</td><td>232.80 (n/a)</td><td>169.51 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1983.70 (n/a)</td><td>783.06 (n/a)</td><td>603.70 (n/a)</td><td>192.00 (n/a)</td><td>692.63 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.60 (n/a)</td><td>440.00 (n/a)</td><td>511.30 (n/a)</td><td>269.60 (n/a)</td><td>142.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.80 (n/a)</td><td>329.48 (n/a)</td><td>295.10 (n/a)</td><td>263.30 (n/a)</td><td>102.67 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.10 (n/a)</td><td>423.56 (n/a)</td><td>492.00 (n/a)</td><td>269.20 (n/a)</td><td>115.27 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>471.40 (n/a)</td><td>361.82 (n/a)</td><td>385.80 (n/a)</td><td>234.10 (n/a)</td><td>101.88 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1018.10 (n/a)</td><td>480.34 (n/a)</td><td>300.10 (n/a)</td><td>277.00 (n/a)</td><td>315.76 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2431.00 (n/a)</td><td>917.08 (n/a)</td><td>573.00 (n/a)</td><td>464.80 (n/a)</td><td>848.22 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>550.60 (n/a)</td><td>498.06 (n/a)</td><td>528.00 (n/a)</td><td>361.90 (n/a)</td><td>78.53 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1953.50 (n/a)</td><td>805.18 (n/a)</td><td>495.90 (n/a)</td><td>446.20 (n/a)</td><td>646.00 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>575.40 (n/a)</td><td>425.86 (n/a)</td><td>408.60 (n/a)</td><td>290.60 (n/a)</td><td>134.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>552.90 (n/a)</td><td>395.60 (n/a)</td><td>455.90 (n/a)</td><td>220.20 (n/a)</td><td>142.13 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.10 (n/a)</td><td>359.84 (n/a)</td><td>288.90 (n/a)</td><td>222.40 (n/a)</td><td>142.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.50 (n/a)</td><td>445.82 (n/a)</td><td>473.00 (n/a)</td><td>207.20 (n/a)</td><td>143.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.30 (n/a)</td><td>342.04 (n/a)</td><td>302.40 (n/a)</td><td>254.10 (n/a)</td><td>93.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>661.30 (n/a)</td><td>470.00 (n/a)</td><td>516.20 (n/a)</td><td>280.90 (n/a)</td><td>164.91 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.70 (n/a)</td><td>430.98 (n/a)</td><td>416.30 (n/a)</td><td>326.20 (n/a)</td><td>102.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.00 (n/a)</td><td>444.56 (n/a)</td><td>471.90 (n/a)</td><td>259.30 (n/a)</td><td>105.50 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.30 (n/a)</td><td>470.88 (n/a)</td><td>513.80 (n/a)</td><td>243.30 (n/a)</td><td>129.55 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.60 (n/a)</td><td>377.40 (n/a)</td><td>295.90 (n/a)</td><td>235.90 (n/a)</td><td>151.90 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.60 (n/a)</td><td>408.62 (n/a)</td><td>292.70 (n/a)</td><td>276.80 (n/a)</td><td>170.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.00 (n/a)</td><td>435.98 (n/a)</td><td>463.50 (n/a)</td><td>228.50 (n/a)</td><td>169.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>973.40 (n/a)</td><td>591.14 (n/a)</td><td>491.20 (n/a)</td><td>448.00 (n/a)</td><td>217.10 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>555.70 (n/a)</td><td>354.72 (n/a)</td><td>317.50 (n/a)</td><td>270.90 (n/a)</td><td>118.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>576.70 (n/a)</td><td>430.76 (n/a)</td><td>502.20 (n/a)</td><td>246.90 (n/a)</td><td>160.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>579.70 (n/a)</td><td>505.58 (n/a)</td><td>529.10 (n/a)</td><td>388.00 (n/a)</td><td>72.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>674.40 (n/a)</td><td>518.62 (n/a)</td><td>533.70 (n/a)</td><td>290.20 (n/a)</td><td>148.74 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>521.60 (n/a)</td><td>420.34 (n/a)</td><td>461.10 (n/a)</td><td>214.80 (n/a)</td><td>121.43 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>497.80 (n/a)</td><td>365.38 (n/a)</td><td>337.00 (n/a)</td><td>174.30 (n/a)</td><td>131.48 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>624.40 (n/a)</td><td>441.18 (n/a)</td><td>469.20 (n/a)</td><td>262.70 (n/a)</td><td>158.46 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1334.40 (n/a)</td><td>662.96 (n/a)</td><td>638.50 (n/a)</td><td>291.50 (n/a)</td><td>411.97 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1891.40 (n/a)</td><td>693.96 (n/a)</td><td>501.90 (n/a)</td><td>252.90 (n/a)</td><td>684.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>642.20 (n/a)</td><td>508.26 (n/a)</td><td>514.20 (n/a)</td><td>383.40 (n/a)</td><td>96.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>572.50 (n/a)</td><td>430.44 (n/a)</td><td>435.50 (n/a)</td><td>268.30 (n/a)</td><td>124.09 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.60 (+10.69%)</td><td>0.38 (-14.89%)</td><td>0.35 <b>(-23.80%)</b></td><td>0.16 <b>(-55.69%)</b></td><td>0.21 <b>(+203.49%)</b></td><td>1364.60 <b>(+125.67%)</b></td><td>762.84 <b>(+51.80%)</b></td><td>632.40 <b>(+31.23%)</b></td><td>367.70 (-9.66%)</td><td>442.11 <b>(+479.11%)</b></td><td>25.66 (+10.69%)</td><td>16.28 (-14.89%)</td><td>14.92 <b>(-23.80%)</b></td><td>6.92 <b>(-55.69%)</b></td><td>8.83 <b>(+203.49%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.54 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.37 (n/a)</td><td>0.07 (n/a)</td><td>604.70 (n/a)</td><td>502.54 (n/a)</td><td>481.90 (n/a)</td><td>407.00 (n/a)</td><td>76.34 (n/a)</td><td>23.19 (n/a)</td><td>19.13 (n/a)</td><td>19.58 (n/a)</td><td>15.61 (n/a)</td><td>2.91 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.50 (-12.92%)</td><td>0.41 (-12.00%)</td><td>0.47 (-6.45%)</td><td>0.20 (-13.13%)</td><td>0.12 (-9.62%)</td><td>1111.20 (+15.13%)</td><td>607.10 (+14.27%)</td><td>470.60 (+6.91%)</td><td>446.20 (+14.82%)</td><td>284.74 (+16.68%)</td><td>21.15 (-12.92%)</td><td>17.50 (-12.00%)</td><td>20.06 (-6.45%)</td><td>8.49 (-13.13%)</td><td>5.27 (-9.62%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.57 (n/a)</td><td>0.47 (n/a)</td><td>0.50 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>965.20 (n/a)</td><td>531.30 (n/a)</td><td>440.20 (n/a)</td><td>388.60 (n/a)</td><td>244.03 (n/a)</td><td>24.29 (n/a)</td><td>19.88 (n/a)</td><td>21.44 (n/a)</td><td>9.78 (n/a)</td><td>5.83 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.31 (-0.49%)</td><td>0.31 (+0.80%)</td><td>0.31 (-0.13%)</td><td>0.31 (+4.62%)</td><td>0.00 <b>(-79.81%)</b></td><td>81936.60 (-4.42%)</td><td>81615.68 (-0.84%)</td><td>81812.30 (+0.13%)</td><td>81097.40 (+0.49%)</td><td>378.90 <b>(-80.71%)</b></td><td>211.84 (-0.49%)</td><td>210.50 (+0.80%)</td><td>209.99 (-0.13%)</td><td>209.67 (+4.62%)</td><td>0.98 <b>(-79.81%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85725.20 (n/a)</td><td>82304.54 (n/a)</td><td>81708.70 (n/a)</td><td>80699.90 (n/a)</td><td>1964.10 (n/a)</td><td>212.89 (n/a)</td><td>208.83 (n/a)</td><td>210.26 (n/a)</td><td>200.41 (n/a)</td><td>4.85 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>1.05 (+1.89%)</td><td>1.03 (+2.80%)</td><td>1.03 (+2.55%)</td><td>1.02 (+4.14%)</td><td>0.01 <b>(-39.44%)</b></td><td>24684.00 (-3.98%)</td><td>24454.60 (-2.74%)</td><td>24550.10 (-2.48%)</td><td>24013.40 (-1.85%)</td><td>264.56 <b>(-42.95%)</b></td><td>715.43 (+1.89%)</td><td>702.59 (+2.80%)</td><td>699.79 (+2.55%)</td><td>695.99 (+4.14%)</td><td>7.68 <b>(-39.44%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>1.00 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25707.00 (n/a)</td><td>25144.14 (n/a)</td><td>25175.60 (n/a)</td><td>24466.90 (n/a)</td><td>463.70 (n/a)</td><td>702.17 (n/a)</td><td>683.44 (n/a)</td><td>682.40 (n/a)</td><td>668.29 (n/a)</td><td>12.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.82 (-1.29%)</td><td>0.79 (-1.63%)</td><td>0.80 (-0.88%)</td><td>0.77 (-1.43%)</td><td>0.02 <b>(+22.21%)</b></td><td>98002.00 (+1.45%)</td><td>95082.96 (+1.68%)</td><td>94212.20 (+0.89%)</td><td>92395.60 (+1.31%)</td><td>2628.75 <b>(+25.96%)</b></td><td>743.75 (-1.29%)</td><td>723.17 (-1.63%)</td><td>729.41 (-0.88%)</td><td>701.20 (-1.43%)</td><td>19.88 <b>(+22.21%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.83 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.78 (n/a)</td><td>0.02 (n/a)</td><td>96599.20 (n/a)</td><td>93509.58 (n/a)</td><td>93383.50 (n/a)</td><td>91205.00 (n/a)</td><td>2087.05 (n/a)</td><td>753.46 (n/a)</td><td>735.18 (n/a)</td><td>735.88 (n/a)</td><td>711.39 (n/a)</td><td>16.27 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.77 (-0.78%)</td><td>0.76 (-1.23%)</td><td>0.76 (-1.66%)</td><td>0.75 (-1.42%)</td><td>0.01 <b>(+33.24%)</b></td><td>100636.10 (+1.44%)</td><td>99191.12 (+1.26%)</td><td>99589.10 (+1.69%)</td><td>97420.00 (+0.78%)</td><td>1483.43 <b>(+36.18%)</b></td><td>705.39 (-0.78%)</td><td>692.92 (-1.23%)</td><td>690.03 (-1.66%)</td><td>682.85 (-1.42%)</td><td>10.40 <b>(+33.24%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99207.70 (n/a)</td><td>97959.44 (n/a)</td><td>97936.80 (n/a)</td><td>96662.80 (n/a)</td><td>1089.31 (n/a)</td><td>710.92 (n/a)</td><td>701.58 (n/a)</td><td>701.67 (n/a)</td><td>692.68 (n/a)</td><td>7.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.80 (-0.28%)</td><td>0.79 (-0.36%)</td><td>0.79 (-0.21%)</td><td>0.77 (-0.65%)</td><td>0.01 <b>(+20.66%)</b></td><td>97472.00 (+0.65%)</td><td>95724.28 (+0.37%)</td><td>95173.10 (+0.21%)</td><td>94366.50 (+0.28%)</td><td>1362.55 <b>(+21.74%)</b></td><td>728.22 (-0.28%)</td><td>718.01 (-0.36%)</td><td>722.05 (-0.21%)</td><td>705.02 (-0.65%)</td><td>10.17 <b>(+20.66%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96840.60 (n/a)</td><td>95370.44 (n/a)</td><td>94970.20 (n/a)</td><td>94102.00 (n/a)</td><td>1119.20 (n/a)</td><td>730.27 (n/a)</td><td>720.63 (n/a)</td><td>723.59 (n/a)</td><td>709.61 (n/a)</td><td>8.43 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>5.69 (-1.14%)</td><td>5.23 (+14.57%)</td><td>5.17 (-2.97%)</td><td>4.67 <b>(+67.63%)</b></td><td>0.45 <b>(-66.53%)</b></td><td>1909.60 <b>(-40.34%)</b></td><td>1714.18 (-19.15%)</td><td>1724.70 (+3.07%)</td><td>1565.90 (+1.16%)</td><td>147.30 <b>(-79.72%)</b></td><td>342.85 (-1.14%)</td><td>315.04 (+14.57%)</td><td>311.29 (-2.97%)</td><td>281.15 <b>(+67.63%)</b></td><td>26.83 <b>(-66.53%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.76 (n/a)</td><td>4.56 (n/a)</td><td>5.33 (n/a)</td><td>2.78 (n/a)</td><td>1.33 (n/a)</td><td>3200.90 (n/a)</td><td>2120.10 (n/a)</td><td>1673.40 (n/a)</td><td>1548.00 (n/a)</td><td>726.20 (n/a)</td><td>346.82 (n/a)</td><td>274.97 (n/a)</td><td>320.83 (n/a)</td><td>167.72 (n/a)</td><td>80.16 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>4.87 <b>(+37.80%)</b></td><td>3.10 (+18.16%)</td><td>2.90 <b>(+28.08%)</b></td><td>2.17 (-1.54%)</td><td>1.09 <b>(+85.89%)</b></td><td>4113.10 (+1.56%)</td><td>3132.86 (-11.04%)</td><td>3068.80 <b>(-21.92%)</b></td><td>1830.80 <b>(-27.43%)</b></td><td>937.79 <b>(+35.43%)</b></td><td>293.24 <b>(+37.80%)</b></td><td>186.68 (+18.16%)</td><td>174.95 <b>(+28.08%)</b></td><td>130.53 (-1.54%)</td><td>65.91 <b>(+85.89%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.53 (n/a)</td><td>2.62 (n/a)</td><td>2.27 (n/a)</td><td>2.20 (n/a)</td><td>0.59 (n/a)</td><td>4049.80 (n/a)</td><td>3521.64 (n/a)</td><td>3930.50 (n/a)</td><td>2522.80 (n/a)</td><td>692.46 (n/a)</td><td>212.81 (n/a)</td><td>157.99 (n/a)</td><td>136.59 (n/a)</td><td>132.57 (n/a)</td><td>35.46 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>4.04 <b>(-23.37%)</b></td><td>2.66 <b>(-27.43%)</b></td><td>2.17 <b>(-45.38%)</b></td><td>2.16 (-1.77%)</td><td>0.81 <b>(-32.43%)</b></td><td>4121.60 (+1.80%)</td><td>3554.94 <b>(+33.03%)</b></td><td>4106.10 <b>(+83.07%)</b></td><td>2205.30 <b>(+30.49%)</b></td><td>845.66 (-10.58%)</td><td>243.45 <b>(-23.37%)</b></td><td>160.24 <b>(-27.43%)</b></td><td>130.75 <b>(-45.38%)</b></td><td>130.26 (-1.77%)</td><td>49.01 <b>(-32.43%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.27 (n/a)</td><td>3.67 (n/a)</td><td>3.97 (n/a)</td><td>2.20 (n/a)</td><td>1.20 (n/a)</td><td>4048.70 (n/a)</td><td>2672.38 (n/a)</td><td>2242.90 (n/a)</td><td>1690.00 (n/a)</td><td>945.73 (n/a)</td><td>317.68 (n/a)</td><td>220.81 (n/a)</td><td>239.37 (n/a)</td><td>132.60 (n/a)</td><td>72.53 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.37 (-3.34%)</td><td>5.64 (+7.73%)</td><td>5.60 (+7.15%)</td><td>4.90 <b>(+37.74%)</b></td><td>0.67 <b>(-41.08%)</b></td><td>7114.90 <b>(-27.40%)</b></td><td>6250.36 (-10.08%)</td><td>6229.00 (-6.68%)</td><td>5470.20 (+3.46%)</td><td>738.88 <b>(-57.24%)</b></td><td>392.58 (-3.34%)</td><td>347.45 (+7.73%)</td><td>344.75 (+7.15%)</td><td>301.83 <b>(+37.74%)</b></td><td>41.02 <b>(-41.08%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>6.59 (n/a)</td><td>5.24 (n/a)</td><td>5.22 (n/a)</td><td>3.56 (n/a)</td><td>1.13 (n/a)</td><td>9800.10 (n/a)</td><td>6951.28 (n/a)</td><td>6674.70 (n/a)</td><td>5287.30 (n/a)</td><td>1727.86 (n/a)</td><td>406.16 (n/a)</td><td>322.51 (n/a)</td><td>321.74 (n/a)</td><td>219.13 (n/a)</td><td>69.62 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>5.77 (+7.34%)</td><td>5.10 (+1.63%)</td><td>5.41 (+3.44%)</td><td>4.18 (+2.00%)</td><td>0.65 <b>(+23.98%)</b></td><td>8337.10 (-1.96%)</td><td>6931.20 (-1.23%)</td><td>6441.30 (-3.32%)</td><td>6037.70 (-6.84%)</td><td>939.68 (+11.95%)</td><td>355.68 (+7.34%)</td><td>314.14 (+1.63%)</td><td>333.39 (+3.44%)</td><td>257.58 (+2.00%)</td><td>39.86 <b>(+23.98%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.38 (n/a)</td><td>5.02 (n/a)</td><td>5.23 (n/a)</td><td>4.10 (n/a)</td><td>0.52 (n/a)</td><td>8503.50 (n/a)</td><td>7017.34 (n/a)</td><td>6662.60 (n/a)</td><td>6480.80 (n/a)</td><td>839.39 (n/a)</td><td>331.36 (n/a)</td><td>309.10 (n/a)</td><td>322.32 (n/a)</td><td>252.54 (n/a)</td><td>32.15 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.67 (+3.82%)</td><td>5.43 (-7.83%)</td><td>5.33 (-10.21%)</td><td>4.44 (-8.07%)</td><td>0.84 <b>(+30.47%)</b></td><td>7853.30 (+8.78%)</td><td>6537.88 (+9.36%)</td><td>6547.20 (+11.37%)</td><td>5227.80 (-3.68%)</td><td>980.02 <b>(+34.66%)</b></td><td>410.78 (+3.82%)</td><td>334.59 (-7.83%)</td><td>328.00 (-10.21%)</td><td>273.45 (-8.07%)</td><td>51.56 <b>(+30.47%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>6.42 (n/a)</td><td>5.89 (n/a)</td><td>5.93 (n/a)</td><td>4.83 (n/a)</td><td>0.64 (n/a)</td><td>7219.20 (n/a)</td><td>5978.58 (n/a)</td><td>5878.60 (n/a)</td><td>5427.30 (n/a)</td><td>727.75 (n/a)</td><td>395.68 (n/a)</td><td>363.03 (n/a)</td><td>365.30 (n/a)</td><td>297.47 (n/a)</td><td>39.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.77 (-1.85%)</td><td>0.77 (-0.04%)</td><td>0.77 (+0.55%)</td><td>0.76 (+1.47%)</td><td>0.01 <b>(-52.97%)</b></td><td>99408.10 (-1.44%)</td><td>98449.02 (+0.02%)</td><td>98008.10 (-0.55%)</td><td>97623.10 (+1.89%)</td><td>850.95 <b>(-52.67%)</b></td><td>703.93 (-1.85%)</td><td>698.06 (-0.04%)</td><td>701.16 (+0.55%)</td><td>691.29 (+1.47%)</td><td>6.02 <b>(-52.97%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100864.70 (n/a)</td><td>98429.32 (n/a)</td><td>98552.00 (n/a)</td><td>95814.00 (n/a)</td><td>1797.99 (n/a)</td><td>717.22 (n/a)</td><td>698.35 (n/a)</td><td>697.29 (n/a)</td><td>681.30 (n/a)</td><td>12.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.78 (+1.08%)</td><td>0.75 (+1.04%)</td><td>0.75 (+1.70%)</td><td>0.73 (+1.76%)</td><td>0.02 (-14.51%)</td><td>102814.00 (-1.73%)</td><td>100448.28 (-1.04%)</td><td>101135.50 (-1.67%)</td><td>96952.80 (-1.06%)</td><td>2344.39 (-16.74%)</td><td>708.79 (+1.08%)</td><td>684.43 (+1.04%)</td><td>679.48 (+1.70%)</td><td>668.39 (+1.76%)</td><td>16.18 (-14.51%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.72 (n/a)</td><td>0.02 (n/a)</td><td>104619.70 (n/a)</td><td>101507.38 (n/a)</td><td>102852.30 (n/a)</td><td>97995.30 (n/a)</td><td>2815.60 (n/a)</td><td>701.25 (n/a)</td><td>677.41 (n/a)</td><td>668.14 (n/a)</td><td>656.85 (n/a)</td><td>18.92 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.81 (+0.04%)</td><td>0.80 (-0.74%)</td><td>0.80 (-0.70%)</td><td>0.78 (-2.36%)</td><td>0.01 <b>(+148.11%)</b></td><td>97196.70 (+2.42%)</td><td>94835.14 (+0.77%)</td><td>94872.30 (+0.70%)</td><td>92973.70 (-0.04%)</td><td>1742.20 <b>(+153.96%)</b></td><td>739.13 (+0.04%)</td><td>724.82 (-0.74%)</td><td>724.34 (-0.70%)</td><td>707.01 (-2.36%)</td><td>13.27 <b>(+148.11%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94902.20 (n/a)</td><td>94109.98 (n/a)</td><td>94210.20 (n/a)</td><td>93012.30 (n/a)</td><td>686.02 (n/a)</td><td>738.82 (n/a)</td><td>730.24 (n/a)</td><td>729.43 (n/a)</td><td>724.11 (n/a)</td><td>5.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>3.92 (+2.35%)</td><td>2.92 (-10.91%)</td><td>2.87 <b>(-22.50%)</b></td><td>1.99 (+19.25%)</td><td>0.91 (-0.66%)</td><td>4047.30 (-16.14%)</td><td>2987.44 (+9.92%)</td><td>2805.70 <b>(+29.04%)</b></td><td>2054.20 (-2.29%)</td><td>941.32 <b>(-20.37%)</b></td><td>1029.09 (+2.35%)</td><td>766.93 (-10.91%)</td><td>753.44 <b>(-22.50%)</b></td><td>522.31 (+19.25%)</td><td>237.86 (-0.66%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.83 (n/a)</td><td>3.28 (n/a)</td><td>3.71 (n/a)</td><td>1.67 (n/a)</td><td>0.91 (n/a)</td><td>4826.30 (n/a)</td><td>2717.84 (n/a)</td><td>2174.30 (n/a)</td><td>2102.40 (n/a)</td><td>1182.08 (n/a)</td><td>1005.50 (n/a)</td><td>860.81 (n/a)</td><td>972.22 (n/a)</td><td>438.00 (n/a)</td><td>239.43 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.28 (+12.21%)</td><td>0.22 (+1.29%)</td><td>0.20 (-10.96%)</td><td>0.15 (-11.40%)</td><td>0.06 <b>(+74.91%)</b></td><td>8249.70 (+12.87%)</td><td>6066.84 (+2.51%)</td><td>6254.90 (+12.31%)</td><td>4395.60 (-10.88%)</td><td>1619.62 <b>(+67.59%)</b></td><td>15.27 (+12.21%)</td><td>11.72 (+1.29%)</td><td>10.73 (-10.96%)</td><td>8.13 (-11.40%)</td><td>3.13 <b>(+74.91%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>7308.90 (n/a)</td><td>5918.48 (n/a)</td><td>5569.10 (n/a)</td><td>4932.10 (n/a)</td><td>966.41 (n/a)</td><td>13.61 (n/a)</td><td>11.57 (n/a)</td><td>12.05 (n/a)</td><td>9.18 (n/a)</td><td>1.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (+0.10%)</td><td>0.09 (-9.47%)</td><td>0.10 <b>(+27.68%)</b></td><td>0.02 <b>(-76.66%)</b></td><td>0.04 <b>(+64.92%)</b></td><td>0.13 (+0.10%)</td><td>0.09 (-9.47%)</td><td>0.10 <b>(+27.68%)</b></td><td>0.02 <b>(-76.66%)</b></td><td>0.04 <b>(+64.92%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>3.76 (-0.71%)</td><td>3.61 (-2.61%)</td><td>3.58 (-4.14%)</td><td>3.51 (+0.20%)</td><td>0.09 (-17.56%)</td><td>3.76 (-0.71%)</td><td>3.60 (-2.61%)</td><td>3.58 (-4.14%)</td><td>3.51 (+0.20%)</td><td>0.09 (-17.56%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.79 (n/a)</td><td>3.70 (n/a)</td><td>3.73 (n/a)</td><td>3.50 (n/a)</td><td>0.11 (n/a)</td><td>3.79 (n/a)</td><td>3.70 (n/a)</td><td>3.73 (n/a)</td><td>3.50 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.60 (-12.61%)</td><td>5.91 (-8.62%)</td><td>5.76 (-7.84%)</td><td>5.68 (+3.93%)</td><td>0.39 <b>(-59.58%)</b></td><td>6.60 (-12.61%)</td><td>5.90 (-8.62%)</td><td>5.76 (-7.84%)</td><td>5.67 (+3.93%)</td><td>0.39 <b>(-59.58%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>7.55 (n/a)</td><td>6.46 (n/a)</td><td>6.25 (n/a)</td><td>5.46 (n/a)</td><td>0.97 (n/a)</td><td>7.55 (n/a)</td><td>6.46 (n/a)</td><td>6.25 (n/a)</td><td>5.46 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>10.74 (+9.34%)</td><td>9.27 (+9.43%)</td><td>9.81 (+16.80%)</td><td>6.76 (-8.85%)</td><td>1.66 <b>(+87.32%)</b></td><td>10.73 (+9.34%)</td><td>9.26 (+9.43%)</td><td>9.80 (+16.80%)</td><td>6.75 (-8.85%)</td><td>1.66 <b>(+87.32%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>9.82 (n/a)</td><td>8.47 (n/a)</td><td>8.39 (n/a)</td><td>7.41 (n/a)</td><td>0.89 (n/a)</td><td>9.81 (n/a)</td><td>8.47 (n/a)</td><td>8.39 (n/a)</td><td>7.41 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>3.95 (+4.48%)</td><td>3.70 (+2.87%)</td><td>3.75 (+4.78%)</td><td>3.46 (+4.80%)</td><td>0.20 (-1.69%)</td><td>3.95 (+4.48%)</td><td>3.70 (+2.87%)</td><td>3.75 (+4.78%)</td><td>3.46 (+4.80%)</td><td>0.20 (-1.69%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.78 (n/a)</td><td>3.60 (n/a)</td><td>3.58 (n/a)</td><td>3.30 (n/a)</td><td>0.20 (n/a)</td><td>3.78 (n/a)</td><td>3.59 (n/a)</td><td>3.57 (n/a)</td><td>3.30 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>7.53 (+6.65%)</td><td>6.65 (+7.84%)</td><td>6.84 (+16.57%)</td><td>5.39 (+2.63%)</td><td>0.85 (+13.15%)</td><td>7.52 (+6.65%)</td><td>6.64 (+7.84%)</td><td>6.83 (+16.57%)</td><td>5.39 (+2.63%)</td><td>0.85 (+13.15%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>7.06 (n/a)</td><td>6.16 (n/a)</td><td>5.86 (n/a)</td><td>5.25 (n/a)</td><td>0.75 (n/a)</td><td>7.05 (n/a)</td><td>6.16 (n/a)</td><td>5.86 (n/a)</td><td>5.25 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>13.79 (+2.57%)</td><td>10.00 (-8.19%)</td><td>8.41 <b>(-32.11%)</b></td><td>7.01 (+1.81%)</td><td>3.14 (+12.30%)</td><td>13.78 (+2.57%)</td><td>9.99 (-8.19%)</td><td>8.41 <b>(-32.11%)</b></td><td>7.01 (+1.81%)</td><td>3.14 (+12.30%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>13.45 (n/a)</td><td>10.89 (n/a)</td><td>12.40 (n/a)</td><td>6.89 (n/a)</td><td>2.80 (n/a)</td><td>13.44 (n/a)</td><td>10.88 (n/a)</td><td>12.39 (n/a)</td><td>6.88 (n/a)</td><td>2.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.60 (n/a)</td><td>330.22 (n/a)</td><td>269.70 (n/a)</td><td>242.30 (n/a)</td><td>116.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1910.50 (n/a)</td><td>633.74 (n/a)</td><td>322.00 (n/a)</td><td>250.10 (n/a)</td><td>714.95 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>571.30 (n/a)</td><td>454.58 (n/a)</td><td>444.90 (n/a)</td><td>245.80 (n/a)</td><td>132.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.30 (n/a)</td><td>412.62 (n/a)</td><td>453.40 (n/a)</td><td>275.90 (n/a)</td><td>107.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.70 (n/a)</td><td>438.16 (n/a)</td><td>425.10 (n/a)</td><td>380.60 (n/a)</td><td>65.91 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.60 (n/a)</td><td>439.40 (n/a)</td><td>453.90 (n/a)</td><td>320.30 (n/a)</td><td>98.89 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.80 (n/a)</td><td>376.38 (n/a)</td><td>302.80 (n/a)</td><td>221.50 (n/a)</td><td>167.74 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>443.30 (n/a)</td><td>322.94 (n/a)</td><td>296.00 (n/a)</td><td>257.20 (n/a)</td><td>75.21 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1024.80 (n/a)</td><td>626.88 (n/a)</td><td>551.50 (n/a)</td><td>395.10 (n/a)</td><td>240.41 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>540.30 (n/a)</td><td>394.24 (n/a)</td><td>369.20 (n/a)</td><td>317.70 (n/a)</td><td>85.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.80 (n/a)</td><td>373.64 (n/a)</td><td>301.40 (n/a)</td><td>250.50 (n/a)</td><td>137.83 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>969.40 (n/a)</td><td>571.70 (n/a)</td><td>435.30 (n/a)</td><td>283.40 (n/a)</td><td>295.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>528.70 (n/a)</td><td>398.00 (n/a)</td><td>427.40 (n/a)</td><td>248.10 (n/a)</td><td>121.94 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>673.40 (n/a)</td><td>434.46 (n/a)</td><td>496.40 (n/a)</td><td>250.10 (n/a)</td><td>181.67 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>681.00 (n/a)</td><td>435.52 (n/a)</td><td>445.80 (n/a)</td><td>198.10 (n/a)</td><td>179.93 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>550.80 (n/a)</td><td>480.32 (n/a)</td><td>512.20 (n/a)</td><td>307.00 (n/a)</td><td>100.90 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>323.60 (n/a)</td><td>283.00 (n/a)</td><td>275.10 (n/a)</td><td>240.00 (n/a)</td><td>34.78 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>538.00 (n/a)</td><td>418.90 (n/a)</td><td>472.20 (n/a)</td><td>255.20 (n/a)</td><td>122.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.15 <b>(+22.81%)</b></td><td>0.09 <b>(+24.07%)</b></td><td>0.08 <b>(+39.41%)</b></td><td>0.02 <b>(-63.02%)</b></td><td>0.05 <b>(+65.15%)</b></td><td>1916.40 <b>(+170.45%)</b></td><td>659.02 <b>(+25.10%)</b></td><td>397.20 <b>(-28.28%)</b></td><td>220.50 (-18.57%)</td><td>711.22 <b>(+286.71%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>708.60 (n/a)</td><td>526.78 (n/a)</td><td>553.80 (n/a)</td><td>270.80 (n/a)</td><td>183.92 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>642.40 (n/a)</td><td>442.12 (n/a)</td><td>477.30 (n/a)</td><td>278.70 (n/a)</td><td>143.33 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>794.10 (n/a)</td><td>508.92 (n/a)</td><td>515.20 (n/a)</td><td>320.10 (n/a)</td><td>198.14 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>746.30 (n/a)</td><td>541.22 (n/a)</td><td>555.70 (n/a)</td><td>233.80 (n/a)</td><td>202.74 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>477.10 (n/a)</td><td>405.68 (n/a)</td><td>410.40 (n/a)</td><td>321.20 (n/a)</td><td>65.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>955.00 (n/a)</td><td>531.72 (n/a)</td><td>437.70 (n/a)</td><td>335.20 (n/a)</td><td>259.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-6.63%)</td><td>0.01 (-0.73%)</td><td>0.01 (+1.73%)</td><td>0.01 (-4.92%)</td><td>0.00 <b>(-23.59%)</b></td><td>510.70 (+5.19%)</td><td>333.22 (-1.42%)</td><td>291.90 (-1.72%)</td><td>262.30 (+7.10%)</td><td>101.07 (-6.83%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>485.50 (n/a)</td><td>338.02 (n/a)</td><td>297.00 (n/a)</td><td>244.90 (n/a)</td><td>108.48 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (-14.15%)</td><td>0.01 (+6.17%)</td><td>0.01 <b>(+36.23%)</b></td><td>0.01 <b>(+166.39%)</b></td><td>0.00 <b>(-42.05%)</b></td><td>708.40 <b>(-62.46%)</b></td><td>441.36 <b>(-37.15%)</b></td><td>371.30 <b>(-26.59%)</b></td><td>297.60 (+16.48%)</td><td>173.84 <b>(-74.41%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1887.10 (n/a)</td><td>702.20 (n/a)</td><td>505.80 (n/a)</td><td>255.50 (n/a)</td><td>679.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-1.37%)</td><td>0.01 (-0.20%)</td><td>0.01 <b>(+28.78%)</b></td><td>0.01 (-12.76%)</td><td>0.00 (+5.04%)</td><td>605.50 (+14.63%)</td><td>379.32 (+3.30%)</td><td>284.10 <b>(-22.36%)</b></td><td>243.80 (+1.41%)</td><td>158.07 <b>(+27.68%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.20 (n/a)</td><td>367.20 (n/a)</td><td>365.90 (n/a)</td><td>240.40 (n/a)</td><td>123.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 <b>(-29.87%)</b></td><td>0.01 (-6.75%)</td><td>0.01 <b>(+29.75%)</b></td><td>0.01 (-16.52%)</td><td>0.01 <b>(-34.62%)</b></td><td>664.30 (+19.78%)</td><td>387.14 (+1.63%)</td><td>343.30 <b>(-22.92%)</b></td><td>210.90 <b>(+42.60%)</b></td><td>185.23 (+12.87%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.60 (n/a)</td><td>380.94 (n/a)</td><td>445.40 (n/a)</td><td>147.90 (n/a)</td><td>164.11 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-0.02%)</td><td>0.02 <b>(+36.89%)</b></td><td>0.02 <b>(+59.99%)</b></td><td>0.01 <b>(+118.71%)</b></td><td>0.00 <b>(-71.96%)</b></td><td>284.70 <b>(-54.28%)</b></td><td>262.16 <b>(-34.15%)</b></td><td>257.80 <b>(-37.49%)</b></td><td>240.10 (+0.04%)</td><td>19.42 <b>(-86.91%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>622.70 (n/a)</td><td>398.14 (n/a)</td><td>412.40 (n/a)</td><td>240.00 (n/a)</td><td>148.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (+2.95%)</td><td>0.01 (-11.05%)</td><td>0.01 (-12.64%)</td><td>0.00 <b>(-39.36%)</b></td><td>0.00 <b>(+21.62%)</b></td><td>1142.20 <b>(+64.89%)</b></td><td>598.34 <b>(+24.23%)</b></td><td>492.70 (+14.47%)</td><td>314.70 (-2.87%)</td><td>322.00 <b>(+104.02%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>692.70 (n/a)</td><td>481.62 (n/a)</td><td>430.40 (n/a)</td><td>324.00 (n/a)</td><td>157.83 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 <b>(+29.89%)</b></td><td>0.03 <b>(+35.14%)</b></td><td>0.03 <b>(+57.46%)</b></td><td>0.02 (+14.61%)</td><td>0.01 (+9.20%)</td><td>507.20 (-12.75%)</td><td>307.16 <b>(-27.14%)</b></td><td>295.20 <b>(-36.50%)</b></td><td>204.50 <b>(-23.00%)</b></td><td>118.62 (-19.36%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.30 (n/a)</td><td>421.60 (n/a)</td><td>464.90 (n/a)</td><td>265.60 (n/a)</td><td>147.11 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (-0.07%)</td><td>0.02 (+9.68%)</td><td>0.03 <b>(+40.36%)</b></td><td>0.02 <b>(+59.13%)</b></td><td>0.01 (-16.76%)</td><td>526.30 <b>(-37.16%)</b></td><td>375.16 (-17.28%)</td><td>319.70 <b>(-28.75%)</b></td><td>225.10 (+0.04%)</td><td>140.09 <b>(-42.01%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>837.50 (n/a)</td><td>453.52 (n/a)</td><td>448.70 (n/a)</td><td>225.00 (n/a)</td><td>241.57 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (-6.53%)</td><td>0.02 (-9.60%)</td><td>0.03 (-9.28%)</td><td>0.01 <b>(-28.73%)</b></td><td>0.01 (+11.13%)</td><td>584.30 <b>(+40.29%)</b></td><td>365.28 (+14.78%)</td><td>301.70 (+10.23%)</td><td>261.30 (+7.00%)</td><td>132.06 <b>(+66.24%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>416.50 (n/a)</td><td>318.24 (n/a)</td><td>273.70 (n/a)</td><td>244.20 (n/a)</td><td>79.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 <b>(+30.41%)</b></td><td>0.03 (-4.68%)</td><td>0.03 (+5.39%)</td><td>0.01 (-19.14%)</td><td>0.01 <b>(+82.08%)</b></td><td>619.30 <b>(+23.66%)</b></td><td>371.44 <b>(+24.48%)</b></td><td>250.60 (-5.11%)</td><td>171.30 <b>(-23.29%)</b></td><td>210.83 <b>(+83.13%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.80 (n/a)</td><td>298.40 (n/a)</td><td>264.10 (n/a)</td><td>223.30 (n/a)</td><td>115.12 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (-12.40%)</td><td>0.03 <b>(+30.40%)</b></td><td>0.03 <b>(+99.63%)</b></td><td>0.02 <b>(+56.57%)</b></td><td>0.01 <b>(-54.50%)</b></td><td>367.40 <b>(-36.13%)</b></td><td>262.58 <b>(-35.27%)</b></td><td>237.40 <b>(-49.89%)</b></td><td>217.10 (+14.20%)</td><td>60.41 <b>(-66.33%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.20 (n/a)</td><td>405.64 (n/a)</td><td>473.80 (n/a)</td><td>190.10 (n/a)</td><td>179.40 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (-12.60%)</td><td>0.02 <b>(-21.97%)</b></td><td>0.02 <b>(-37.51%)</b></td><td>0.02 (+17.70%)</td><td>0.01 <b>(-34.28%)</b></td><td>514.90 (-15.03%)</td><td>430.00 (+19.01%)</td><td>479.20 <b>(+60.00%)</b></td><td>264.10 (+14.38%)</td><td>100.26 <b>(-36.53%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.00 (n/a)</td><td>361.30 (n/a)</td><td>299.50 (n/a)</td><td>230.90 (n/a)</td><td>157.96 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (-17.76%)</td><td>0.02 (-17.08%)</td><td>0.03 (-10.39%)</td><td>0.01 <b>(-20.24%)</b></td><td>0.01 (-11.27%)</td><td>594.40 <b>(+25.37%)</b></td><td>394.32 <b>(+22.89%)</b></td><td>302.30 (+11.59%)</td><td>259.90 <b>(+21.56%)</b></td><td>153.92 <b>(+35.86%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>474.10 (n/a)</td><td>320.86 (n/a)</td><td>270.90 (n/a)</td><td>213.80 (n/a)</td><td>113.29 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (-1.57%)</td><td>0.02 (+9.97%)</td><td>0.02 (+15.35%)</td><td>0.02 <b>(+25.94%)</b></td><td>0.01 (-9.97%)</td><td>520.10 <b>(-20.60%)</b></td><td>405.66 (-13.99%)</td><td>453.80 (-13.31%)</td><td>178.30 (+1.60%)</td><td>141.97 <b>(-20.50%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.00 (n/a)</td><td>471.64 (n/a)</td><td>523.50 (n/a)</td><td>175.50 (n/a)</td><td>178.57 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (+1.06%)</td><td>0.05 (-1.17%)</td><td>0.06 (+7.35%)</td><td>0.03 (-2.72%)</td><td>0.02 (+13.83%)</td><td>579.40 (+2.79%)</td><td>386.90 (+5.21%)</td><td>275.50 (-6.86%)</td><td>243.10 (-1.02%)</td><td>170.04 <b>(+21.69%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>563.70 (n/a)</td><td>367.74 (n/a)</td><td>295.80 (n/a)</td><td>245.60 (n/a)</td><td>139.73 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (-4.79%)</td><td>0.04 (-10.04%)</td><td>0.03 (-11.28%)</td><td>0.03 (-13.52%)</td><td>0.02 (-2.57%)</td><td>606.00 (+15.65%)</td><td>421.82 (+13.28%)</td><td>468.70 (+12.72%)</td><td>242.40 (+5.03%)</td><td>159.53 <b>(+21.16%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>524.00 (n/a)</td><td>372.38 (n/a)</td><td>415.80 (n/a)</td><td>230.80 (n/a)</td><td>131.67 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (+16.49%)</td><td>0.05 (+4.99%)</td><td>0.04 <b>(-30.26%)</b></td><td>0.03 <b>(+21.40%)</b></td><td>0.02 (+6.37%)</td><td>550.10 (-17.63%)</td><td>382.70 (-8.05%)</td><td>407.50 <b>(+43.38%)</b></td><td>226.10 (-14.16%)</td><td>144.28 <b>(-26.73%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>667.80 (n/a)</td><td>416.22 (n/a)</td><td>284.20 (n/a)</td><td>263.40 (n/a)</td><td>196.91 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (+8.69%)</td><td>0.04 (-0.45%)</td><td>0.04 (-19.75%)</td><td>0.03 <b>(+67.90%)</b></td><td>0.01 (-8.21%)</td><td>588.60 <b>(-40.44%)</b></td><td>441.20 (-8.84%)</td><td>451.90 <b>(+24.63%)</b></td><td>274.90 (-8.00%)</td><td>136.50 <b>(-52.33%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>988.30 (n/a)</td><td>484.00 (n/a)</td><td>362.60 (n/a)</td><td>298.80 (n/a)</td><td>286.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (-3.29%)</td><td>0.05 <b>(+22.27%)</b></td><td>0.05 <b>(+55.31%)</b></td><td>0.03 (+17.57%)</td><td>0.02 (-17.43%)</td><td>512.50 (-14.95%)</td><td>350.18 <b>(-22.34%)</b></td><td>303.10 <b>(-35.62%)</b></td><td>203.70 (+3.45%)</td><td>124.26 <b>(-20.36%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>602.60 (n/a)</td><td>450.90 (n/a)</td><td>470.80 (n/a)</td><td>196.90 (n/a)</td><td>156.02 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-12.57%)</td><td>0.04 (+4.19%)</td><td>0.03 (+18.87%)</td><td>0.03 (+2.15%)</td><td>0.01 <b>(-24.53%)</b></td><td>626.30 (-2.11%)</td><td>481.02 (-7.74%)</td><td>489.90 (-15.88%)</td><td>289.20 (+14.35%)</td><td>141.72 (-12.01%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>639.80 (n/a)</td><td>521.38 (n/a)</td><td>582.40 (n/a)</td><td>252.90 (n/a)</td><td>161.06 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (-5.96%)</td><td>0.10 (-10.70%)</td><td>0.12 (-15.00%)</td><td>0.07 (+2.76%)</td><td>0.03 (-3.15%)</td><td>469.80 (-2.67%)</td><td>344.80 (+12.33%)</td><td>284.40 (+17.62%)</td><td>244.00 (+6.36%)</td><td>114.45 (+6.19%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>482.70 (n/a)</td><td>306.96 (n/a)</td><td>241.80 (n/a)</td><td>229.40 (n/a)</td><td>107.78 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (+5.32%)</td><td>0.10 (+10.35%)</td><td>0.11 (+18.40%)</td><td>0.06 (+12.81%)</td><td>0.04 (-1.42%)</td><td>531.40 (-11.36%)</td><td>362.34 (-11.62%)</td><td>295.70 (-15.54%)</td><td>231.00 (-5.06%)</td><td>141.35 (-18.04%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>599.50 (n/a)</td><td>409.98 (n/a)</td><td>350.10 (n/a)</td><td>243.30 (n/a)</td><td>172.47 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (+11.62%)</td><td>0.08 (-7.23%)</td><td>0.08 (+1.42%)</td><td>0.04 <b>(-29.70%)</b></td><td>0.03 <b>(+31.01%)</b></td><td>762.80 <b>(+42.23%)</b></td><td>452.52 (+15.00%)</td><td>416.20 (-1.40%)</td><td>253.90 (-10.41%)</td><td>187.58 <b>(+79.46%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>536.30 (n/a)</td><td>393.50 (n/a)</td><td>422.10 (n/a)</td><td>283.40 (n/a)</td><td>104.52 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (+10.64%)</td><td>0.09 (+1.07%)</td><td>0.08 (-2.34%)</td><td>0.06 (-8.19%)</td><td>0.04 <b>(+20.42%)</b></td><td>592.50 (+8.92%)</td><td>405.48 (+2.52%)</td><td>402.80 (+2.39%)</td><td>243.30 (-9.62%)</td><td>152.55 <b>(+20.62%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>544.00 (n/a)</td><td>395.52 (n/a)</td><td>393.40 (n/a)</td><td>269.20 (n/a)</td><td>126.46 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (-14.70%)</td><td>0.09 (-10.84%)</td><td>0.10 (-0.38%)</td><td>0.03 <b>(-47.40%)</b></td><td>0.04 (+10.29%)</td><td>1039.50 <b>(+90.11%)</b></td><td>497.46 <b>(+29.43%)</b></td><td>312.80 (+0.39%)</td><td>268.40 (+17.26%)</td><td>328.70 <b>(+118.20%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>546.80 (n/a)</td><td>384.34 (n/a)</td><td>311.60 (n/a)</td><td>228.90 (n/a)</td><td>150.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 <b>(+22.57%)</b></td><td>0.01 (-2.98%)</td><td>0.01 <b>(-30.87%)</b></td><td>0.01 (+1.78%)</td><td>0.00 (+2.31%)</td><td>486.40 (-1.74%)</td><td>341.18 (+0.38%)</td><td>354.50 <b>(+44.63%)</b></td><td>193.30 (-18.40%)</td><td>107.20 <b>(-21.39%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.00 (n/a)</td><td>339.88 (n/a)</td><td>245.10 (n/a)</td><td>236.90 (n/a)</td><td>136.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (+3.19%)</td><td>0.01 (+4.95%)</td><td>0.01 (+6.10%)</td><td>0.01 (+4.78%)</td><td>0.00 (+3.85%)</td><td>546.00 (-4.56%)</td><td>419.60 (-4.86%)</td><td>491.30 (-5.74%)</td><td>266.40 (-3.09%)</td><td>136.80 (-5.27%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.10 (n/a)</td><td>441.04 (n/a)</td><td>521.20 (n/a)</td><td>274.90 (n/a)</td><td>144.41 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 <b>(-26.92%)</b></td><td>0.01 <b>(-37.01%)</b></td><td>0.01 <b>(-39.45%)</b></td><td>0.01 <b>(-27.22%)</b></td><td>0.00 <b>(-30.12%)</b></td><td>608.20 <b>(+37.42%)</b></td><td>488.62 <b>(+57.06%)</b></td><td>491.10 <b>(+65.19%)</b></td><td>267.80 <b>(+36.84%)</b></td><td>136.13 <b>(+27.00%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>442.60 (n/a)</td><td>311.10 (n/a)</td><td>297.30 (n/a)</td><td>195.70 (n/a)</td><td>107.19 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 <b>(+46.89%)</b></td><td>0.02 <b>(+27.58%)</b></td><td>0.01 (+6.24%)</td><td>0.01 (+8.40%)</td><td>0.01 <b>(+112.60%)</b></td><td>441.00 (-7.74%)</td><td>304.84 (-14.51%)</td><td>291.80 (-5.87%)</td><td>183.10 <b>(-31.91%)</b></td><td>123.52 <b>(+29.67%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.00 (n/a)</td><td>356.58 (n/a)</td><td>310.00 (n/a)</td><td>268.90 (n/a)</td><td>95.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 <b>(-30.06%)</b></td><td>0.01 (-17.41%)</td><td>0.01 (+8.04%)</td><td>0.01 (+2.57%)</td><td>0.00 <b>(-51.20%)</b></td><td>568.50 (-2.50%)</td><td>431.50 (+7.31%)</td><td>427.30 (-7.43%)</td><td>272.90 <b>(+43.03%)</b></td><td>114.86 <b>(-32.74%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.10 (n/a)</td><td>402.12 (n/a)</td><td>461.60 (n/a)</td><td>190.80 (n/a)</td><td>170.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (-2.07%)</td><td>0.01 <b>(-20.58%)</b></td><td>0.01 (-11.92%)</td><td>0.00 <b>(-73.16%)</b></td><td>0.00 <b>(+37.31%)</b></td><td>2112.10 <b>(+272.64%)</b></td><td>795.02 <b>(+79.54%)</b></td><td>525.20 (+13.51%)</td><td>297.60 (+2.13%)</td><td>744.25 <b>(+483.06%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.80 (n/a)</td><td>442.82 (n/a)</td><td>462.70 (n/a)</td><td>291.40 (n/a)</td><td>127.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 <b>(+83.39%)</b></td><td>0.01 (+4.79%)</td><td>0.01 (-19.48%)</td><td>0.01 <b>(-22.56%)</b></td><td>0.01 <b>(+147.52%)</b></td><td>779.90 <b>(+29.12%)</b></td><td>516.10 <b>(+20.82%)</b></td><td>521.80 <b>(+24.18%)</b></td><td>148.00 <b>(-45.47%)</b></td><td>238.27 <b>(+60.19%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>604.00 (n/a)</td><td>427.16 (n/a)</td><td>420.20 (n/a)</td><td>271.40 (n/a)</td><td>148.75 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-10.66%)</td><td>0.01 <b>(-29.76%)</b></td><td>0.01 (-10.45%)</td><td>0.00 <b>(-85.93%)</b></td><td>0.01 <b>(+258.33%)</b></td><td>2021.30 <b>(+610.97%)</b></td><td>676.06 <b>(+163.18%)</b></td><td>284.40 (+11.66%)</td><td>241.20 (+11.93%)</td><td>764.63 <b>(+2742.49%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>284.30 (n/a)</td><td>256.88 (n/a)</td><td>254.70 (n/a)</td><td>215.50 (n/a)</td><td>26.90 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-0.86%)</td><td>0.01 (-17.72%)</td><td>0.01 (-15.07%)</td><td>0.01 <b>(-25.95%)</b></td><td>0.01 <b>(+34.37%)</b></td><td>600.70 <b>(+35.05%)</b></td><td>383.82 <b>(+34.51%)</b></td><td>296.90 (+17.72%)</td><td>198.60 (+0.86%)</td><td>178.23 <b>(+87.31%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>444.80 (n/a)</td><td>285.34 (n/a)</td><td>252.20 (n/a)</td><td>196.90 (n/a)</td><td>95.15 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-0.02%)</td><td>0.01 <b>(-26.52%)</b></td><td>0.01 <b>(-47.90%)</b></td><td>0.00 <b>(-78.72%)</b></td><td>0.01 <b>(+32.80%)</b></td><td>2474.70 <b>(+369.85%)</b></td><td>818.62 <b>(+129.05%)</b></td><td>511.80 <b>(+91.97%)</b></td><td>249.20 (+0.04%)</td><td>935.04 <b>(+575.69%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>526.70 (n/a)</td><td>357.40 (n/a)</td><td>266.60 (n/a)</td><td>249.10 (n/a)</td><td>138.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (+18.24%)</td><td>0.01 (+1.34%)</td><td>0.01 (-16.33%)</td><td>0.01 (+7.80%)</td><td>0.01 <b>(+38.24%)</b></td><td>651.50 (-7.25%)</td><td>487.40 (+3.59%)</td><td>546.40 (+19.51%)</td><td>219.80 (-15.43%)</td><td>167.27 (+6.43%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>702.40 (n/a)</td><td>470.52 (n/a)</td><td>457.20 (n/a)</td><td>259.90 (n/a)</td><td>157.16 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 <b>(+23.62%)</b></td><td>0.01 (-7.78%)</td><td>0.01 <b>(-47.86%)</b></td><td>0.01 (+8.49%)</td><td>0.01 <b>(+31.82%)</b></td><td>561.70 (-7.83%)</td><td>437.96 (+12.08%)</td><td>546.10 <b>(+91.75%)</b></td><td>178.90 (-19.12%)</td><td>168.67 (-5.37%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.40 (n/a)</td><td>390.74 (n/a)</td><td>284.80 (n/a)</td><td>221.20 (n/a)</td><td>178.23 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 <b>(+70.79%)</b></td><td>0.03 <b>(+54.89%)</b></td><td>0.03 <b>(+81.37%)</b></td><td>0.02 (+9.79%)</td><td>0.02 <b>(+103.89%)</b></td><td>538.20 (-8.92%)</td><td>330.68 <b>(-28.86%)</b></td><td>280.30 <b>(-44.87%)</b></td><td>152.20 <b>(-41.46%)</b></td><td>155.03 (+8.41%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.90 (n/a)</td><td>464.80 (n/a)</td><td>508.40 (n/a)</td><td>260.00 (n/a)</td><td>143.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 <b>(+20.42%)</b></td><td>0.02 (+18.69%)</td><td>0.02 <b>(+28.67%)</b></td><td>0.02 <b>(+31.16%)</b></td><td>0.01 <b>(+24.16%)</b></td><td>494.80 <b>(-23.76%)</b></td><td>366.60 (-15.36%)</td><td>333.30 <b>(-22.29%)</b></td><td>222.70 (-16.96%)</td><td>119.74 (-16.47%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.00 (n/a)</td><td>433.12 (n/a)</td><td>428.90 (n/a)</td><td>268.20 (n/a)</td><td>143.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 <b>(+91.84%)</b></td><td>0.02 <b>(+48.08%)</b></td><td>0.02 <b>(+34.74%)</b></td><td>0.01 (+10.82%)</td><td>0.01 <b>(+214.01%)</b></td><td>565.30 (-9.75%)</td><td>387.04 <b>(-24.21%)</b></td><td>385.50 <b>(-25.79%)</b></td><td>205.80 <b>(-47.89%)</b></td><td>156.91 <b>(+51.36%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>626.40 (n/a)</td><td>510.66 (n/a)</td><td>519.50 (n/a)</td><td>394.90 (n/a)</td><td>103.67 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (+14.04%)</td><td>0.03 (-4.56%)</td><td>0.03 (-12.27%)</td><td>0.02 (-8.47%)</td><td>0.01 (+18.70%)</td><td>504.50 (+9.25%)</td><td>306.90 (+7.30%)</td><td>272.50 (+13.97%)</td><td>197.80 (-12.32%)</td><td>117.74 (+17.41%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>461.80 (n/a)</td><td>286.02 (n/a)</td><td>239.10 (n/a)</td><td>225.60 (n/a)</td><td>100.28 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 <b>(+34.80%)</b></td><td>0.02 (+4.45%)</td><td>0.01 (+8.05%)</td><td>0.01 (+7.64%)</td><td>0.02 <b>(+41.51%)</b></td><td>564.10 (-7.10%)</td><td>461.20 (-0.10%)</td><td>549.00 (-7.45%)</td><td>164.00 <b>(-25.83%)</b></td><td>170.40 (-11.22%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.20 (n/a)</td><td>461.68 (n/a)</td><td>593.20 (n/a)</td><td>221.10 (n/a)</td><td>191.94 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (-4.00%)</td><td>0.02 <b>(-26.30%)</b></td><td>0.02 <b>(-40.96%)</b></td><td>0.02 (+18.42%)</td><td>0.01 (-15.41%)</td><td>498.70 (-15.56%)</td><td>431.70 <b>(+29.90%)</b></td><td>465.90 <b>(+69.42%)</b></td><td>240.20 (+4.16%)</td><td>108.13 <b>(-28.09%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.60 (n/a)</td><td>332.32 (n/a)</td><td>275.00 (n/a)</td><td>230.60 (n/a)</td><td>150.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 <b>(+36.01%)</b></td><td>0.02 (+17.78%)</td><td>0.02 (-3.12%)</td><td>0.01 <b>(+42.90%)</b></td><td>0.01 <b>(+50.39%)</b></td><td>610.20 <b>(-30.02%)</b></td><td>473.52 (-11.12%)</td><td>545.50 (+3.24%)</td><td>170.50 <b>(-26.48%)</b></td><td>178.83 <b>(-21.42%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>872.00 (n/a)</td><td>532.76 (n/a)</td><td>528.40 (n/a)</td><td>231.90 (n/a)</td><td>227.57 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (-14.41%)</td><td>0.02 <b>(-34.01%)</b></td><td>0.01 <b>(-46.75%)</b></td><td>0.01 <b>(-33.11%)</b></td><td>0.01 (+13.53%)</td><td>666.90 <b>(+49.50%)</b></td><td>508.12 <b>(+58.84%)</b></td><td>546.70 <b>(+87.74%)</b></td><td>273.20 (+16.85%)</td><td>146.67 <b>(+81.49%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>446.10 (n/a)</td><td>319.90 (n/a)</td><td>291.20 (n/a)</td><td>233.80 (n/a)</td><td>80.82 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (+6.27%)</td><td>0.02 (-4.08%)</td><td>0.02 (+19.04%)</td><td>0.01 (-14.80%)</td><td>0.01 (+5.19%)</td><td>659.40 (+17.37%)</td><td>451.40 (+5.84%)</td><td>424.40 (-15.99%)</td><td>244.20 (-5.90%)</td><td>158.83 (+15.39%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.80 (n/a)</td><td>426.50 (n/a)</td><td>505.20 (n/a)</td><td>259.50 (n/a)</td><td>137.66 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 <b>(-25.52%)</b></td><td>0.02 (-10.79%)</td><td>0.02 <b>(-27.52%)</b></td><td>0.01 (+3.17%)</td><td>0.01 <b>(-41.59%)</b></td><td>598.30 (-3.08%)</td><td>404.98 (+2.21%)</td><td>417.70 <b>(+37.95%)</b></td><td>278.50 <b>(+34.22%)</b></td><td>125.45 <b>(-29.38%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.30 (n/a)</td><td>396.22 (n/a)</td><td>302.80 (n/a)</td><td>207.50 (n/a)</td><td>177.63 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 <b>(-22.68%)</b></td><td>0.02 (-4.62%)</td><td>0.02 (-4.02%)</td><td>0.01 <b>(+38.48%)</b></td><td>0.00 <b>(-43.47%)</b></td><td>583.70 <b>(-27.79%)</b></td><td>442.20 (-4.71%)</td><td>458.00 (+4.19%)</td><td>325.70 <b>(+29.35%)</b></td><td>104.05 <b>(-49.93%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>808.30 (n/a)</td><td>464.04 (n/a)</td><td>439.60 (n/a)</td><td>251.80 (n/a)</td><td>207.82 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 <b>(-28.29%)</b></td><td>0.01 <b>(-43.77%)</b></td><td>0.02 <b>(-43.75%)</b></td><td>0.01 <b>(-50.25%)</b></td><td>0.01 (-8.51%)</td><td>1096.10 <b>(+101.01%)</b></td><td>652.02 <b>(+92.69%)</b></td><td>528.70 <b>(+77.77%)</b></td><td>362.20 <b>(+39.41%)</b></td><td>295.42 <b>(+151.04%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.30 (n/a)</td><td>338.38 (n/a)</td><td>297.40 (n/a)</td><td>259.80 (n/a)</td><td>117.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-8.02%)</td><td>0.05 (-17.98%)</td><td>0.05 <b>(-20.60%)</b></td><td>0.03 (-14.22%)</td><td>0.01 (+7.41%)</td><td>489.80 (+16.56%)</td><td>375.32 <b>(+24.59%)</b></td><td>357.40 <b>(+25.93%)</b></td><td>255.90 (+8.71%)</td><td>105.08 <b>(+41.16%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>420.20 (n/a)</td><td>301.24 (n/a)</td><td>283.80 (n/a)</td><td>235.40 (n/a)</td><td>74.44 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-3.39%)</td><td>0.05 (-16.41%)</td><td>0.05 (-14.91%)</td><td>0.03 <b>(-30.12%)</b></td><td>0.01 <b>(+86.81%)</b></td><td>504.50 <b>(+43.08%)</b></td><td>377.14 <b>(+26.00%)</b></td><td>359.50 (+17.52%)</td><td>261.20 (+3.49%)</td><td>106.28 <b>(+181.18%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>352.60 (n/a)</td><td>299.32 (n/a)</td><td>305.90 (n/a)</td><td>252.40 (n/a)</td><td>37.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-10.97%)</td><td>0.04 (-10.61%)</td><td>0.04 (-3.40%)</td><td>0.03 (-0.54%)</td><td>0.01 (-19.21%)</td><td>643.90 (+0.53%)</td><td>444.22 (+9.09%)</td><td>407.70 (+3.53%)</td><td>280.70 (+12.32%)</td><td>140.68 (-7.65%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>640.50 (n/a)</td><td>407.20 (n/a)</td><td>393.80 (n/a)</td><td>249.90 (n/a)</td><td>152.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-10.38%)</td><td>0.05 <b>(+23.14%)</b></td><td>0.05 <b>(+41.02%)</b></td><td>0.04 <b>(+38.24%)</b></td><td>0.01 <b>(-44.58%)</b></td><td>431.40 <b>(-27.67%)</b></td><td>340.64 <b>(-22.95%)</b></td><td>320.80 <b>(-29.09%)</b></td><td>291.60 (+11.60%)</td><td>57.04 <b>(-52.44%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>596.40 (n/a)</td><td>442.12 (n/a)</td><td>452.40 (n/a)</td><td>261.30 (n/a)</td><td>119.95 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (+15.43%)</td><td>0.04 <b>(+33.50%)</b></td><td>0.04 (+11.49%)</td><td>0.03 <b>(+249.72%)</b></td><td>0.01 (-13.22%)</td><td>551.90 <b>(-71.41%)</b></td><td>407.70 <b>(-44.99%)</b></td><td>458.30 (-10.31%)</td><td>276.50 (-13.35%)</td><td>120.64 <b>(-82.00%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1930.10 (n/a)</td><td>741.16 (n/a)</td><td>511.00 (n/a)</td><td>319.10 (n/a)</td><td>670.28 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 <b>(-23.15%)</b></td><td>0.05 (+13.87%)</td><td>0.05 <b>(+52.36%)</b></td><td>0.03 <b>(+267.02%)</b></td><td>0.01 <b>(-59.78%)</b></td><td>527.80 <b>(-72.75%)</b></td><td>336.84 <b>(-50.17%)</b></td><td>302.00 <b>(-34.38%)</b></td><td>262.00 <b>(+30.09%)</b></td><td>108.71 <b>(-84.92%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1937.20 (n/a)</td><td>675.96 (n/a)</td><td>460.20 (n/a)</td><td>201.40 (n/a)</td><td>720.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 <b>(-25.91%)</b></td><td>0.03 <b>(-29.90%)</b></td><td>0.03 <b>(-20.92%)</b></td><td>0.01 <b>(-70.77%)</b></td><td>0.02 (+8.33%)</td><td>1968.20 <b>(+242.12%)</b></td><td>825.04 <b>(+89.52%)</b></td><td>539.20 <b>(+26.45%)</b></td><td>347.00 <b>(+34.97%)</b></td><td>663.46 <b>(+441.46%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>575.30 (n/a)</td><td>435.34 (n/a)</td><td>426.40 (n/a)</td><td>257.10 (n/a)</td><td>122.53 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-13.06%)</td><td>0.04 <b>(+36.54%)</b></td><td>0.04 (+18.50%)</td><td>0.03 <b>(+326.18%)</b></td><td>0.01 <b>(-48.18%)</b></td><td>583.00 <b>(-76.54%)</b></td><td>447.74 <b>(-61.15%)</b></td><td>463.10 (-15.60%)</td><td>272.80 (+15.06%)</td><td>127.22 <b>(-87.30%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2484.60 (n/a)</td><td>1152.58 (n/a)</td><td>548.70 (n/a)</td><td>237.10 (n/a)</td><td>1001.43 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 <b>(+27.70%)</b></td><td>0.03 (-14.59%)</td><td>0.03 (-13.65%)</td><td>0.01 <b>(-78.23%)</b></td><td>0.02 <b>(+227.11%)</b></td><td>2475.10 <b>(+359.29%)</b></td><td>875.84 <b>(+90.46%)</b></td><td>542.00 (+15.81%)</td><td>287.90 <b>(-21.70%)</b></td><td>900.60 <b>(+1282.89%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>538.90 (n/a)</td><td>459.86 (n/a)</td><td>468.00 (n/a)</td><td>367.70 (n/a)</td><td>65.12 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-13.67%)</td><td>0.04 <b>(-21.68%)</b></td><td>0.03 <b>(-35.07%)</b></td><td>0.03 (-17.05%)</td><td>0.01 (-13.86%)</td><td>601.10 <b>(+20.56%)</b></td><td>452.60 <b>(+27.21%)</b></td><td>476.90 <b>(+54.04%)</b></td><td>271.80 (+15.81%)</td><td>119.03 (+10.95%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>498.60 (n/a)</td><td>355.78 (n/a)</td><td>309.60 (n/a)</td><td>234.70 (n/a)</td><td>107.29 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (-6.71%)</td><td>0.04 (-5.37%)</td><td>0.04 <b>(+20.37%)</b></td><td>0.02 <b>(-24.58%)</b></td><td>0.02 (-6.58%)</td><td>824.20 <b>(+32.57%)</b></td><td>518.26 (+7.38%)</td><td>460.60 (-16.92%)</td><td>246.90 (+7.21%)</td><td>212.73 <b>(+26.91%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>621.70 (n/a)</td><td>482.64 (n/a)</td><td>554.40 (n/a)</td><td>230.30 (n/a)</td><td>167.63 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-5.83%)</td><td>0.04 (-15.69%)</td><td>0.03 (-15.71%)</td><td>0.03 (+2.45%)</td><td>0.01 <b>(-22.58%)</b></td><td>581.50 (-2.40%)</td><td>477.44 (+14.89%)</td><td>516.00 (+18.65%)</td><td>294.00 (+6.21%)</td><td>110.78 (-18.59%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>595.80 (n/a)</td><td>415.56 (n/a)</td><td>434.90 (n/a)</td><td>276.80 (n/a)</td><td>136.07 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 <b>(-33.43%)</b></td><td>0.09 (+1.73%)</td><td>0.10 <b>(+74.53%)</b></td><td>0.05 <b>(+206.67%)</b></td><td>0.03 <b>(-54.57%)</b></td><td>643.20 <b>(-67.39%)</b></td><td>412.48 <b>(-42.32%)</b></td><td>323.80 <b>(-42.71%)</b></td><td>283.70 <b>(+50.19%)</b></td><td>158.59 <b>(-78.17%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1972.60 (n/a)</td><td>715.06 (n/a)</td><td>565.20 (n/a)</td><td>188.90 (n/a)</td><td>726.32 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 <b>(-22.97%)</b></td><td>0.10 <b>(-22.07%)</b></td><td>0.11 (-13.23%)</td><td>0.06 <b>(-47.30%)</b></td><td>0.03 <b>(+28.23%)</b></td><td>576.20 <b>(+89.79%)</b></td><td>346.56 <b>(+36.08%)</b></td><td>295.20 (+15.22%)</td><td>271.30 <b>(+29.81%)</b></td><td>128.81 <b>(+233.64%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>303.60 (n/a)</td><td>254.68 (n/a)</td><td>256.20 (n/a)</td><td>209.00 (n/a)</td><td>38.61 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (-14.05%)</td><td>0.09 <b>(-29.83%)</b></td><td>0.10 <b>(-25.86%)</b></td><td>0.02 <b>(-73.47%)</b></td><td>0.05 <b>(+42.03%)</b></td><td>1937.50 <b>(+277.02%)</b></td><td>674.48 <b>(+131.40%)</b></td><td>321.90 <b>(+34.86%)</b></td><td>240.70 (+16.34%)</td><td>722.65 <b>(+473.85%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>513.90 (n/a)</td><td>291.48 (n/a)</td><td>238.70 (n/a)</td><td>206.90 (n/a)</td><td>125.93 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.23 <b>(+52.88%)</b></td><td>0.12 (-3.11%)</td><td>0.11 (-5.42%)</td><td>0.07 <b>(-36.47%)</b></td><td>0.07 <b>(+230.76%)</b></td><td>473.30 <b>(+57.40%)</b></td><td>322.48 <b>(+22.20%)</b></td><td>302.00 (+5.74%)</td><td>142.70 <b>(-34.60%)</b></td><td>138.12 <b>(+253.46%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>300.70 (n/a)</td><td>263.90 (n/a)</td><td>285.60 (n/a)</td><td>218.20 (n/a)</td><td>39.08 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (-2.26%)</td><td>0.10 (-10.10%)</td><td>0.11 (-13.55%)</td><td>0.07 <b>(+26.58%)</b></td><td>0.03 (-13.66%)</td><td>478.30 <b>(-20.99%)</b></td><td>344.24 (+5.86%)</td><td>305.00 (+15.71%)</td><td>240.90 (+2.34%)</td><td>107.15 <b>(-32.09%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>605.40 (n/a)</td><td>325.18 (n/a)</td><td>263.60 (n/a)</td><td>235.40 (n/a)</td><td>157.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (-6.08%)</td><td>0.09 <b>(-22.53%)</b></td><td>0.09 <b>(-27.70%)</b></td><td>0.05 (-14.67%)</td><td>0.03 (+1.31%)</td><td>654.30 (+17.20%)</td><td>424.44 <b>(+31.77%)</b></td><td>381.80 <b>(+38.33%)</b></td><td>253.00 (+6.48%)</td><td>164.68 <b>(+22.74%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>558.30 (n/a)</td><td>322.10 (n/a)</td><td>276.00 (n/a)</td><td>237.60 (n/a)</td><td>134.17 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (+2.99%)</td><td>0.08 <b>(-21.81%)</b></td><td>0.08 <b>(-31.16%)</b></td><td>0.05 <b>(-26.60%)</b></td><td>0.03 (+19.14%)</td><td>600.10 <b>(+36.26%)</b></td><td>446.20 <b>(+34.12%)</b></td><td>436.20 <b>(+45.25%)</b></td><td>243.40 (-2.91%)</td><td>146.99 <b>(+60.53%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>440.40 (n/a)</td><td>332.68 (n/a)</td><td>300.30 (n/a)</td><td>250.70 (n/a)</td><td>91.57 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 (+17.69%)</td><td>0.10 <b>(+28.32%)</b></td><td>0.11 <b>(+47.55%)</b></td><td>0.06 <b>(+331.91%)</b></td><td>0.04 <b>(-27.47%)</b></td><td>577.60 <b>(-76.85%)</b></td><td>352.78 <b>(-56.46%)</b></td><td>309.40 <b>(-32.22%)</b></td><td>203.30 (-15.04%)</td><td>138.89 <b>(-85.44%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2494.60 (n/a)</td><td>810.22 (n/a)</td><td>456.50 (n/a)</td><td>239.30 (n/a)</td><td>953.89 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 <b>(-28.15%)</b></td><td>0.09 (-5.98%)</td><td>0.09 <b>(+38.12%)</b></td><td>0.05 (-2.11%)</td><td>0.03 <b>(-44.54%)</b></td><td>678.20 (+2.15%)</td><td>414.24 (-5.35%)</td><td>370.20 <b>(-27.60%)</b></td><td>283.10 <b>(+39.18%)</b></td><td>161.75 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>663.90 (n/a)</td><td>437.64 (n/a)</td><td>511.30 (n/a)</td><td>203.40 (n/a)</td><td>202.34 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (+8.50%)</td><td>0.09 <b>(+27.57%)</b></td><td>0.08 <b>(+20.68%)</b></td><td>0.07 <b>(+286.22%)</b></td><td>0.03 <b>(-29.81%)</b></td><td>486.50 <b>(-74.11%)</b></td><td>401.26 <b>(-44.83%)</b></td><td>415.80 (-17.14%)</td><td>250.10 (-7.81%)</td><td>95.60 <b>(-85.36%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1879.00 (n/a)</td><td>727.38 (n/a)</td><td>501.80 (n/a)</td><td>271.30 (n/a)</td><td>652.89 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 <b>(+49.60%)</b></td><td>0.10 <b>(+34.45%)</b></td><td>0.09 <b>(+44.13%)</b></td><td>0.06 (+13.03%)</td><td>0.04 <b>(+94.27%)</b></td><td>545.50 (-11.53%)</td><td>387.52 <b>(-20.00%)</b></td><td>352.00 <b>(-30.61%)</b></td><td>205.50 <b>(-33.17%)</b></td><td>145.56 <b>(+25.40%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>616.60 (n/a)</td><td>484.40 (n/a)</td><td>507.30 (n/a)</td><td>307.50 (n/a)</td><td>116.08 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (+5.44%)</td><td>0.07 <b>(-28.81%)</b></td><td>0.07 <b>(-40.61%)</b></td><td>0.02 <b>(-70.55%)</b></td><td>0.04 <b>(+61.47%)</b></td><td>1878.90 <b>(+239.64%)</b></td><td>705.76 <b>(+104.96%)</b></td><td>490.60 <b>(+68.36%)</b></td><td>247.90 (-5.16%)</td><td>664.69 <b>(+457.45%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>553.20 (n/a)</td><td>344.34 (n/a)</td><td>291.40 (n/a)</td><td>261.40 (n/a)</td><td>119.24 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (-9.67%)</td><td>0.01 (-12.16%)</td><td>0.01 <b>(-21.52%)</b></td><td>0.01 (+4.02%)</td><td>0.00 <b>(-29.56%)</b></td><td>623.60 (-3.85%)</td><td>442.54 (+6.31%)</td><td>483.90 <b>(+27.41%)</b></td><td>273.20 (+10.70%)</td><td>139.52 <b>(-23.15%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>648.60 (n/a)</td><td>416.26 (n/a)</td><td>379.80 (n/a)</td><td>246.80 (n/a)</td><td>181.55 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (+19.91%)</td><td>0.02 <b>(+23.25%)</b></td><td>0.02 <b>(+36.15%)</b></td><td>0.01 (-6.29%)</td><td>0.01 <b>(+41.38%)</b></td><td>570.10 (+6.72%)</td><td>360.34 (-14.58%)</td><td>323.20 <b>(-26.55%)</b></td><td>212.80 (-16.58%)</td><td>140.41 <b>(+33.52%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>534.20 (n/a)</td><td>421.84 (n/a)</td><td>440.00 (n/a)</td><td>255.10 (n/a)</td><td>105.16 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (+18.03%)</td><td>0.01 <b>(+25.87%)</b></td><td>0.01 <b>(+56.68%)</b></td><td>0.01 <b>(-31.57%)</b></td><td>0.01 <b>(+74.90%)</b></td><td>812.40 <b>(+46.14%)</b></td><td>407.52 (-8.11%)</td><td>304.10 <b>(-36.18%)</b></td><td>236.10 (-15.29%)</td><td>238.78 <b>(+129.06%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>555.90 (n/a)</td><td>443.50 (n/a)</td><td>476.50 (n/a)</td><td>278.70 (n/a)</td><td>104.24 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-12.94%)</td><td>0.02 <b>(+25.47%)</b></td><td>0.02 <b>(+59.83%)</b></td><td>0.01 <b>(+24.00%)</b></td><td>0.00 <b>(-31.92%)</b></td><td>456.70 (-19.35%)</td><td>331.72 <b>(-25.89%)</b></td><td>309.30 <b>(-37.43%)</b></td><td>232.00 (+14.85%)</td><td>96.83 <b>(-32.00%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.30 (n/a)</td><td>447.62 (n/a)</td><td>494.30 (n/a)</td><td>202.00 (n/a)</td><td>142.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 <b>(-33.99%)</b></td><td>0.01 <b>(-40.83%)</b></td><td>0.01 <b>(-43.37%)</b></td><td>0.00 <b>(-54.49%)</b></td><td>0.00 (-16.96%)</td><td>1084.60 <b>(+119.73%)</b></td><td>568.14 <b>(+83.19%)</b></td><td>477.60 <b>(+76.56%)</b></td><td>365.10 <b>(+51.49%)</b></td><td>294.91 <b>(+182.02%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>493.60 (n/a)</td><td>310.14 (n/a)</td><td>270.50 (n/a)</td><td>241.00 (n/a)</td><td>104.57 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (+13.87%)</td><td>0.01 (+15.64%)</td><td>0.01 <b>(+31.57%)</b></td><td>0.01 <b>(+26.97%)</b></td><td>0.00 (-1.39%)</td><td>531.70 <b>(-21.24%)</b></td><td>393.54 (-15.56%)</td><td>351.60 <b>(-23.99%)</b></td><td>268.60 (-12.16%)</td><td>104.15 <b>(-29.65%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>675.10 (n/a)</td><td>466.06 (n/a)</td><td>462.60 (n/a)</td><td>305.80 (n/a)</td><td>148.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 <b>(+81.78%)</b></td><td>0.01 <b>(+60.88%)</b></td><td>0.01 <b>(+88.65%)</b></td><td>0.01 (+10.12%)</td><td>0.00 <b>(+205.93%)</b></td><td>531.40 (-9.19%)</td><td>345.70 <b>(-33.27%)</b></td><td>300.50 <b>(-46.99%)</b></td><td>228.20 <b>(-45.00%)</b></td><td>123.11 <b>(+52.76%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.20 (n/a)</td><td>518.02 (n/a)</td><td>566.90 (n/a)</td><td>414.90 (n/a)</td><td>80.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-9.57%)</td><td>0.01 (-10.95%)</td><td>0.01 (+1.08%)</td><td>0.01 (-7.93%)</td><td>0.00 (-12.10%)</td><td>641.90 (+8.61%)</td><td>475.54 (+11.72%)</td><td>459.30 (-1.06%)</td><td>291.10 (+10.60%)</td><td>133.40 (+6.15%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.00 (n/a)</td><td>425.66 (n/a)</td><td>464.20 (n/a)</td><td>263.20 (n/a)</td><td>125.66 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (-9.57%)</td><td>0.01 (-2.92%)</td><td>0.01 (-4.28%)</td><td>0.01 (-5.16%)</td><td>0.00 (-6.33%)</td><td>495.60 (+5.42%)</td><td>406.38 (+3.43%)</td><td>453.50 (+4.47%)</td><td>273.60 (+10.59%)</td><td>102.26 (+14.39%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>470.10 (n/a)</td><td>392.92 (n/a)</td><td>434.10 (n/a)</td><td>247.40 (n/a)</td><td>89.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 (-5.61%)</td><td>0.01 (+8.03%)</td><td>0.01 (+0.31%)</td><td>0.01 (+10.76%)</td><td>0.00 (-2.34%)</td><td>554.70 (-9.72%)</td><td>413.38 (-7.42%)</td><td>432.70 (-0.30%)</td><td>256.10 (+5.91%)</td><td>136.35 (-0.24%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.40 (n/a)</td><td>446.52 (n/a)</td><td>434.00 (n/a)</td><td>241.80 (n/a)</td><td>136.69 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.01 (-3.85%)</td><td>0.01 (+0.49%)</td><td>0.01 (+6.21%)</td><td>0.01 (-8.11%)</td><td>0.00 (+9.11%)</td><td>620.50 (+8.82%)</td><td>436.58 (+0.97%)</td><td>388.80 (-5.84%)</td><td>322.30 (+4.00%)</td><td>118.70 <b>(+26.29%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.20 (n/a)</td><td>432.38 (n/a)</td><td>412.90 (n/a)</td><td>309.90 (n/a)</td><td>93.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (-10.39%)</td><td>0.02 <b>(-23.18%)</b></td><td>0.02 <b>(-43.05%)</b></td><td>0.02 (+9.23%)</td><td>0.01 (-12.29%)</td><td>529.90 (-8.45%)</td><td>405.92 <b>(+26.84%)</b></td><td>437.50 <b>(+75.56%)</b></td><td>256.80 (+11.60%)</td><td>127.15 (-13.36%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.80 (n/a)</td><td>320.02 (n/a)</td><td>249.20 (n/a)</td><td>230.10 (n/a)</td><td>146.75 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (-12.87%)</td><td>0.03 (-15.15%)</td><td>0.03 <b>(-37.33%)</b></td><td>0.02 (+18.17%)</td><td>0.01 <b>(-27.90%)</b></td><td>503.60 (-15.38%)</td><td>414.74 (+11.81%)</td><td>469.00 <b>(+59.58%)</b></td><td>269.10 (+14.80%)</td><td>101.82 <b>(-30.60%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>595.10 (n/a)</td><td>370.94 (n/a)</td><td>293.90 (n/a)</td><td>234.40 (n/a)</td><td>146.70 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (+8.51%)</td><td>0.02 (-5.51%)</td><td>0.03 (-10.52%)</td><td>0.01 <b>(+68.94%)</b></td><td>0.01 (-7.17%)</td><td>665.00 <b>(-40.80%)</b></td><td>388.04 (-11.24%)</td><td>296.00 (+11.74%)</td><td>222.00 (-7.85%)</td><td>185.00 <b>(-51.84%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1123.40 (n/a)</td><td>437.20 (n/a)</td><td>264.90 (n/a)</td><td>240.90 (n/a)</td><td>384.14 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 (-1.57%)</td><td>0.03 (+17.04%)</td><td>0.03 <b>(+45.70%)</b></td><td>0.02 <b>(+206.55%)</b></td><td>0.01 <b>(-20.39%)</b></td><td>647.00 <b>(-67.38%)</b></td><td>401.94 <b>(-43.00%)</b></td><td>313.20 <b>(-31.36%)</b></td><td>212.60 (+1.58%)</td><td>192.11 <b>(-73.70%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1983.50 (n/a)</td><td>705.16 (n/a)</td><td>456.30 (n/a)</td><td>209.30 (n/a)</td><td>730.57 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 <b>(+24.52%)</b></td><td>0.03 <b>(+20.99%)</b></td><td>0.03 <b>(+43.34%)</b></td><td>0.02 <b>(+30.01%)</b></td><td>0.01 <b>(+20.14%)</b></td><td>451.90 <b>(-23.08%)</b></td><td>313.72 (-17.10%)</td><td>253.70 <b>(-30.24%)</b></td><td>192.40 (-19.67%)</td><td>123.69 (-15.69%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.50 (n/a)</td><td>378.42 (n/a)</td><td>363.70 (n/a)</td><td>239.50 (n/a)</td><td>146.72 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 (-7.37%)</td><td>0.02 <b>(-26.21%)</b></td><td>0.02 <b>(-28.45%)</b></td><td>0.01 <b>(-29.35%)</b></td><td>0.01 (-11.26%)</td><td>961.90 <b>(+41.52%)</b></td><td>557.66 <b>(+40.91%)</b></td><td>550.10 <b>(+39.76%)</b></td><td>239.50 (+7.98%)</td><td>276.88 <b>(+45.57%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>679.70 (n/a)</td><td>395.76 (n/a)</td><td>393.60 (n/a)</td><td>221.80 (n/a)</td><td>190.21 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 <b>(+23.15%)</b></td><td>0.02 <b>(-23.50%)</b></td><td>0.01 <b>(-43.80%)</b></td><td>0.00 <b>(-66.86%)</b></td><td>0.01 <b>(+56.36%)</b></td><td>1931.10 <b>(+201.73%)</b></td><td>814.26 <b>(+90.39%)</b></td><td>634.60 <b>(+77.91%)</b></td><td>190.80 (-18.77%)</td><td>660.73 <b>(+249.79%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.00 (n/a)</td><td>427.68 (n/a)</td><td>356.70 (n/a)</td><td>234.90 (n/a)</td><td>188.90 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 <b>(-30.20%)</b></td><td>0.02 <b>(-37.70%)</b></td><td>0.02 <b>(-35.89%)</b></td><td>0.01 <b>(-65.04%)</b></td><td>0.01 (-1.97%)</td><td>1340.60 <b>(+186.03%)</b></td><td>667.60 <b>(+85.37%)</b></td><td>552.70 <b>(+56.00%)</b></td><td>342.40 <b>(+43.26%)</b></td><td>387.09 <b>(+348.29%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>468.70 (n/a)</td><td>360.14 (n/a)</td><td>354.30 (n/a)</td><td>239.00 (n/a)</td><td>86.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.02 <b>(-34.74%)</b></td><td>0.02 <b>(-44.99%)</b></td><td>0.02 <b>(-40.22%)</b></td><td>0.00 <b>(-81.02%)</b></td><td>0.01 (-5.12%)</td><td>2453.90 <b>(+426.93%)</b></td><td>864.42 <b>(+169.98%)</b></td><td>484.70 <b>(+67.25%)</b></td><td>347.80 <b>(+53.22%)</b></td><td>891.69 <b>(+797.33%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.70 (n/a)</td><td>320.18 (n/a)</td><td>289.80 (n/a)</td><td>227.00 (n/a)</td><td>99.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 <b>(-38.57%)</b></td><td>0.02 <b>(-24.28%)</b></td><td>0.02 (-10.41%)</td><td>0.01 <b>(-20.20%)</b></td><td>0.01 <b>(-51.58%)</b></td><td>649.10 <b>(+25.31%)</b></td><td>490.46 <b>(+22.96%)</b></td><td>526.10 (+11.60%)</td><td>353.70 <b>(+62.77%)</b></td><td>129.18 (-10.16%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.00 (n/a)</td><td>398.88 (n/a)</td><td>471.40 (n/a)</td><td>217.30 (n/a)</td><td>143.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.03 (-2.18%)</td><td>0.02 (-17.82%)</td><td>0.02 <b>(-35.45%)</b></td><td>0.02 (-2.40%)</td><td>0.01 (-3.53%)</td><td>542.40 (+2.46%)</td><td>460.74 <b>(+20.83%)</b></td><td>500.00 <b>(+54.89%)</b></td><td>265.20 (+2.20%)</td><td>112.53 (-6.57%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.40 (n/a)</td><td>381.32 (n/a)</td><td>322.80 (n/a)</td><td>259.50 (n/a)</td><td>120.45 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (+14.55%)</td><td>0.05 (-7.34%)</td><td>0.05 (-18.42%)</td><td>0.03 (+1.30%)</td><td>0.02 (+10.05%)</td><td>503.30 (-1.29%)</td><td>341.00 (+7.97%)</td><td>312.90 <b>(+22.56%)</b></td><td>215.50 (-12.68%)</td><td>105.89 (-5.36%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>509.90 (n/a)</td><td>315.84 (n/a)</td><td>255.30 (n/a)</td><td>246.80 (n/a)</td><td>111.88 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 <b>(-50.55%)</b></td><td>0.04 <b>(-26.26%)</b></td><td>0.05 (-2.11%)</td><td>0.02 <b>(-40.26%)</b></td><td>0.01 <b>(-57.45%)</b></td><td>1051.70 <b>(+67.39%)</b></td><td>639.16 <b>(+30.38%)</b></td><td>524.50 (+2.16%)</td><td>499.50 <b>(+102.23%)</b></td><td>234.12 <b>(+49.42%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>628.30 (n/a)</td><td>490.24 (n/a)</td><td>513.40 (n/a)</td><td>247.00 (n/a)</td><td>156.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (+2.21%)</td><td>0.05 (-10.58%)</td><td>0.03 <b>(-46.86%)</b></td><td>0.03 (+10.15%)</td><td>0.02 (-12.76%)</td><td>608.70 (-9.20%)</td><td>411.44 (+5.27%)</td><td>473.90 <b>(+88.13%)</b></td><td>236.50 (-2.15%)</td><td>158.16 <b>(-22.39%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>670.40 (n/a)</td><td>390.84 (n/a)</td><td>251.90 (n/a)</td><td>241.70 (n/a)</td><td>203.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (+14.53%)</td><td>0.06 <b>(+22.99%)</b></td><td>0.07 <b>(+41.52%)</b></td><td>0.04 (+13.41%)</td><td>0.02 <b>(+36.94%)</b></td><td>557.10 (-11.84%)</td><td>382.94 (-15.64%)</td><td>309.90 <b>(-29.34%)</b></td><td>248.70 (-12.71%)</td><td>140.07 (+13.07%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>631.90 (n/a)</td><td>453.96 (n/a)</td><td>438.60 (n/a)</td><td>284.90 (n/a)</td><td>123.88 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (+5.88%)</td><td>0.04 <b>(-22.90%)</b></td><td>0.03 <b>(-40.36%)</b></td><td>0.03 (-16.97%)</td><td>0.02 (+4.56%)</td><td>608.50 <b>(+20.45%)</b></td><td>464.32 <b>(+31.19%)</b></td><td>471.30 <b>(+67.66%)</b></td><td>229.40 (-5.52%)</td><td>144.79 (+9.05%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>505.20 (n/a)</td><td>353.92 (n/a)</td><td>281.10 (n/a)</td><td>242.80 (n/a)</td><td>132.78 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 (-15.40%)</td><td>0.06 (+17.60%)</td><td>0.06 <b>(+43.59%)</b></td><td>0.04 (+13.84%)</td><td>0.01 <b>(-44.62%)</b></td><td>494.60 (-12.15%)</td><td>361.52 <b>(-20.31%)</b></td><td>342.50 <b>(-30.34%)</b></td><td>277.70 (+18.22%)</td><td>81.07 <b>(-37.81%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>563.00 (n/a)</td><td>453.68 (n/a)</td><td>491.70 (n/a)</td><td>234.90 (n/a)</td><td>130.37 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-16.90%)</td><td>0.04 (-9.41%)</td><td>0.03 (-6.73%)</td><td>0.03 (-5.76%)</td><td>0.01 <b>(-24.06%)</b></td><td>588.30 (+6.11%)</td><td>440.62 (+6.47%)</td><td>502.50 (+7.21%)</td><td>274.60 <b>(+20.39%)</b></td><td>140.49 (-7.07%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>554.40 (n/a)</td><td>413.84 (n/a)</td><td>468.70 (n/a)</td><td>228.10 (n/a)</td><td>151.18 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (+10.84%)</td><td>0.04 <b>(-27.38%)</b></td><td>0.03 <b>(-37.68%)</b></td><td>0.01 <b>(-69.29%)</b></td><td>0.02 <b>(+59.41%)</b></td><td>1944.30 <b>(+225.57%)</b></td><td>757.16 <b>(+99.93%)</b></td><td>562.30 <b>(+60.47%)</b></td><td>240.90 (-9.78%)</td><td>678.82 <b>(+410.07%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>597.20 (n/a)</td><td>378.72 (n/a)</td><td>350.40 (n/a)</td><td>267.00 (n/a)</td><td>133.08 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.04 <b>(-38.93%)</b></td><td>0.03 (-12.81%)</td><td>0.03 (-8.44%)</td><td>0.03 <b>(+88.03%)</b></td><td>0.01 <b>(-71.94%)</b></td><td>560.10 <b>(-46.81%)</b></td><td>488.30 (-7.81%)</td><td>498.50 (+9.22%)</td><td>370.90 <b>(+63.75%)</b></td><td>71.18 <b>(-77.08%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1053.10 (n/a)</td><td>529.68 (n/a)</td><td>456.40 (n/a)</td><td>226.50 (n/a)</td><td>310.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 <b>(+27.10%)</b></td><td>0.04 (-4.23%)</td><td>0.04 (-3.98%)</td><td>0.01 <b>(-72.33%)</b></td><td>0.03 <b>(+107.71%)</b></td><td>2036.00 <b>(+261.44%)</b></td><td>752.72 <b>(+62.67%)</b></td><td>489.30 (+4.15%)</td><td>227.30 <b>(-21.32%)</b></td><td>728.08 <b>(+585.87%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>563.30 (n/a)</td><td>462.72 (n/a)</td><td>469.80 (n/a)</td><td>288.90 (n/a)</td><td>106.15 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.05 <b>(-27.03%)</b></td><td>0.04 (-10.99%)</td><td>0.04 (+10.11%)</td><td>0.03 (-4.50%)</td><td>0.01 <b>(-50.06%)</b></td><td>521.10 (+4.72%)</td><td>421.60 (+6.58%)</td><td>401.60 (-9.18%)</td><td>330.60 <b>(+37.06%)</b></td><td>82.21 <b>(-29.38%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>497.60 (n/a)</td><td>395.58 (n/a)</td><td>442.20 (n/a)</td><td>241.20 (n/a)</td><td>116.40 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (-15.50%)</td><td>0.06 (-13.71%)</td><td>0.06 (-12.74%)</td><td>0.01 <b>(-69.32%)</b></td><td>0.04 (+2.06%)</td><td>2517.30 <b>(+225.91%)</b></td><td>863.54 <b>(+70.45%)</b></td><td>527.90 (+14.61%)</td><td>293.00 (+18.34%)</td><td>929.56 <b>(+377.69%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>772.40 (n/a)</td><td>506.62 (n/a)</td><td>460.60 (n/a)</td><td>247.60 (n/a)</td><td>194.59 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 <b>(+33.92%)</b></td><td>0.11 (+15.82%)</td><td>0.11 (-1.63%)</td><td>0.06 (-10.41%)</td><td>0.04 <b>(+56.91%)</b></td><td>576.60 (+11.61%)</td><td>336.56 (-8.63%)</td><td>310.70 (+1.67%)</td><td>211.20 <b>(-25.34%)</b></td><td>141.41 <b>(+38.66%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>516.60 (n/a)</td><td>368.36 (n/a)</td><td>305.60 (n/a)</td><td>282.90 (n/a)</td><td>101.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.20 <b>(+25.50%)</b></td><td>0.13 <b>(+43.69%)</b></td><td>0.13 <b>(+41.15%)</b></td><td>0.07 <b>(+254.39%)</b></td><td>0.06 (+13.84%)</td><td>599.50 <b>(-71.78%)</b></td><td>369.94 <b>(-50.19%)</b></td><td>310.60 <b>(-29.15%)</b></td><td>204.80 <b>(-20.34%)</b></td><td>171.32 <b>(-77.95%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2124.60 (n/a)</td><td>742.74 (n/a)</td><td>438.40 (n/a)</td><td>257.10 (n/a)</td><td>776.91 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (+16.11%)</td><td>0.09 <b>(+85.52%)</b></td><td>0.07 <b>(+198.32%)</b></td><td>0.06 <b>(+224.29%)</b></td><td>0.03 <b>(-23.91%)</b></td><td>590.80 <b>(-69.16%)</b></td><td>411.68 <b>(-65.50%)</b></td><td>457.20 <b>(-66.48%)</b></td><td>237.10 (-13.88%)</td><td>138.91 <b>(-81.57%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1915.80 (n/a)</td><td>1193.40 (n/a)</td><td>1363.80 (n/a)</td><td>275.30 (n/a)</td><td>753.63 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.17 (+8.91%)</td><td>0.10 (-12.07%)</td><td>0.08 <b>(-43.70%)</b></td><td>0.04 <b>(-47.41%)</b></td><td>0.06 <b>(+46.82%)</b></td><td>1043.70 <b>(+90.14%)</b></td><td>529.48 <b>(+37.34%)</b></td><td>539.40 <b>(+77.67%)</b></td><td>237.10 (-8.17%)</td><td>327.06 <b>(+123.51%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>548.90 (n/a)</td><td>385.52 (n/a)</td><td>303.60 (n/a)</td><td>258.20 (n/a)</td><td>146.33 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (-10.37%)</td><td>0.07 (-0.77%)</td><td>0.08 (+15.27%)</td><td>0.05 <b>(+191.00%)</b></td><td>0.02 <b>(-42.43%)</b></td><td>631.30 <b>(-65.63%)</b></td><td>471.82 <b>(-30.98%)</b></td><td>428.70 (-13.24%)</td><td>296.40 (+11.60%)</td><td>140.46 <b>(-78.52%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1837.00 (n/a)</td><td>683.64 (n/a)</td><td>494.10 (n/a)</td><td>265.60 (n/a)</td><td>654.03 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 <b>(-40.39%)</b></td><td>0.08 <b>(-38.09%)</b></td><td>0.08 <b>(-34.59%)</b></td><td>0.04 <b>(-45.32%)</b></td><td>0.03 <b>(-46.51%)</b></td><td>1005.50 <b>(+82.88%)</b></td><td>542.14 <b>(+60.99%)</b></td><td>456.40 <b>(+52.90%)</b></td><td>338.10 <b>(+67.79%)</b></td><td>264.00 <b>(+83.47%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>549.80 (n/a)</td><td>336.76 (n/a)</td><td>298.50 (n/a)</td><td>201.50 (n/a)</td><td>143.89 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (+0.91%)</td><td>0.08 (+16.85%)</td><td>0.06 (+10.22%)</td><td>0.06 (+12.83%)</td><td>0.03 (+3.32%)</td><td>547.80 (-11.37%)</td><td>426.76 (-14.50%)</td><td>506.90 (-9.27%)</td><td>268.90 (-0.88%)</td><td>130.33 (-5.49%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>618.10 (n/a)</td><td>499.16 (n/a)</td><td>558.70 (n/a)</td><td>271.30 (n/a)</td><td>137.90 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 <b>(-46.60%)</b></td><td>0.07 <b>(-24.70%)</b></td><td>0.07 <b>(-24.99%)</b></td><td>0.06 <b>(+66.33%)</b></td><td>0.01 <b>(-82.50%)</b></td><td>623.70 <b>(-39.88%)</b></td><td>539.84 (+3.99%)</td><td>554.10 <b>(+33.33%)</b></td><td>475.10 <b>(+87.27%)</b></td><td>62.43 <b>(-80.47%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1037.40 (n/a)</td><td>519.14 (n/a)</td><td>415.60 (n/a)</td><td>253.70 (n/a)</td><td>319.70 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.18 <b>(+89.51%)</b></td><td>0.08 (+9.44%)</td><td>0.06 <b>(-20.69%)</b></td><td>0.05 (+1.47%)</td><td>0.05 <b>(+251.91%)</b></td><td>615.60 (-1.44%)</td><td>493.24 (+8.08%)</td><td>567.80 <b>(+26.09%)</b></td><td>186.50 <b>(-47.24%)</b></td><td>178.64 <b>(+72.68%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>624.60 (n/a)</td><td>456.36 (n/a)</td><td>450.30 (n/a)</td><td>353.50 (n/a)</td><td>103.45 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (-3.65%)</td><td>0.06 <b>(-22.23%)</b></td><td>0.06 <b>(-33.81%)</b></td><td>0.04 (-4.65%)</td><td>0.02 (-8.79%)</td><td>521.40 (+4.89%)</td><td>373.36 <b>(+27.00%)</b></td><td>371.70 <b>(+51.10%)</b></td><td>241.80 (+3.78%)</td><td>107.99 (-5.03%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>497.10 (n/a)</td><td>293.98 (n/a)</td><td>246.00 (n/a)</td><td>233.00 (n/a)</td><td>113.70 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (-14.09%)</td><td>0.07 (+13.32%)</td><td>0.08 (+9.21%)</td><td>0.04 <b>(+24.35%)</b></td><td>0.02 <b>(-36.44%)</b></td><td>505.30 (-19.59%)</td><td>308.84 <b>(-20.61%)</b></td><td>272.20 (-8.44%)</td><td>238.50 (+16.40%)</td><td>110.71 <b>(-40.39%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>628.40 (n/a)</td><td>389.00 (n/a)</td><td>297.30 (n/a)</td><td>204.90 (n/a)</td><td>185.73 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (+7.47%)</td><td>0.04 <b>(-26.35%)</b></td><td>0.04 <b>(-33.64%)</b></td><td>0.01 <b>(-76.95%)</b></td><td>0.03 <b>(+54.21%)</b></td><td>2445.20 <b>(+333.85%)</b></td><td>856.12 <b>(+121.61%)</b></td><td>522.80 <b>(+50.71%)</b></td><td>225.50 (-6.97%)</td><td>898.99 <b>(+583.22%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>563.60 (n/a)</td><td>386.32 (n/a)</td><td>346.90 (n/a)</td><td>242.40 (n/a)</td><td>131.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (+18.91%)</td><td>0.06 (+4.90%)</td><td>0.04 (-6.91%)</td><td>0.03 (-15.65%)</td><td>0.03 <b>(+52.69%)</b></td><td>615.70 (+18.54%)</td><td>430.72 (+6.03%)</td><td>493.50 (+7.42%)</td><td>217.50 (-15.89%)</td><td>191.69 <b>(+49.02%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>519.40 (n/a)</td><td>406.22 (n/a)</td><td>459.40 (n/a)</td><td>258.60 (n/a)</td><td>128.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (-1.85%)</td><td>0.06 (-1.16%)</td><td>0.06 (-4.40%)</td><td>0.04 <b>(+24.83%)</b></td><td>0.02 <b>(-22.97%)</b></td><td>497.70 (-19.89%)</td><td>357.76 (-4.85%)</td><td>327.70 (+4.60%)</td><td>241.30 (+1.90%)</td><td>101.65 <b>(-36.15%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>621.30 (n/a)</td><td>376.00 (n/a)</td><td>313.30 (n/a)</td><td>236.80 (n/a)</td><td>159.21 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 <b>(-34.67%)</b></td><td>0.04 <b>(-25.71%)</b></td><td>0.04 <b>(-20.33%)</b></td><td>0.03 (-18.87%)</td><td>0.01 <b>(-52.10%)</b></td><td>587.30 <b>(+23.28%)</b></td><td>495.64 <b>(+29.58%)</b></td><td>533.80 <b>(+25.54%)</b></td><td>359.20 <b>(+53.05%)</b></td><td>88.61 (-10.98%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>476.40 (n/a)</td><td>382.50 (n/a)</td><td>425.20 (n/a)</td><td>234.70 (n/a)</td><td>99.53 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 <b>(+77.39%)</b></td><td>0.07 <b>(+30.04%)</b></td><td>0.05 (+8.18%)</td><td>0.04 (-4.22%)</td><td>0.04 <b>(+137.60%)</b></td><td>626.70 (+4.40%)</td><td>415.86 (-11.95%)</td><td>492.90 (-7.56%)</td><td>177.80 <b>(-43.63%)</b></td><td>180.89 <b>(+37.74%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>600.30 (n/a)</td><td>472.30 (n/a)</td><td>533.20 (n/a)</td><td>315.40 (n/a)</td><td>131.32 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (+9.76%)</td><td>0.08 (-7.62%)</td><td>0.09 (+7.16%)</td><td>0.05 <b>(-36.64%)</b></td><td>0.03 <b>(+138.01%)</b></td><td>507.20 <b>(+57.86%)</b></td><td>338.76 (+19.66%)</td><td>281.90 (-6.69%)</td><td>220.60 (-8.92%)</td><td>131.57 <b>(+251.90%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>321.30 (n/a)</td><td>283.10 (n/a)</td><td>302.10 (n/a)</td><td>242.20 (n/a)</td><td>37.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 <b>(+26.38%)</b></td><td>0.07 (+3.93%)</td><td>0.07 (-9.86%)</td><td>0.04 (-17.83%)</td><td>0.03 <b>(+57.89%)</b></td><td>627.70 <b>(+21.69%)</b></td><td>380.54 (+3.35%)</td><td>374.10 (+10.94%)</td><td>217.00 <b>(-20.89%)</b></td><td>157.82 <b>(+54.33%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>515.80 (n/a)</td><td>368.20 (n/a)</td><td>337.20 (n/a)</td><td>274.30 (n/a)</td><td>102.27 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 <b>(-30.85%)</b></td><td>0.05 <b>(-28.91%)</b></td><td>0.05 (-10.06%)</td><td>0.03 <b>(-36.84%)</b></td><td>0.02 <b>(-41.00%)</b></td><td>814.60 <b>(+58.33%)</b></td><td>521.96 <b>(+38.52%)</b></td><td>482.00 (+11.19%)</td><td>352.10 <b>(+44.60%)</b></td><td>182.47 <b>(+46.22%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>514.50 (n/a)</td><td>376.82 (n/a)</td><td>433.50 (n/a)</td><td>243.50 (n/a)</td><td>124.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 <b>(+22.09%)</b></td><td>0.07 <b>(+47.44%)</b></td><td>0.06 <b>(+52.32%)</b></td><td>0.05 <b>(+268.45%)</b></td><td>0.03 (+3.38%)</td><td>529.30 <b>(-72.86%)</b></td><td>379.68 <b>(-50.01%)</b></td><td>383.20 <b>(-34.34%)</b></td><td>231.70 (-18.07%)</td><td>145.37 <b>(-78.66%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1950.10 (n/a)</td><td>759.58 (n/a)</td><td>583.60 (n/a)</td><td>282.80 (n/a)</td><td>681.25 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.10 (-8.62%)</td><td>0.06 (+0.89%)</td><td>0.05 (-19.29%)</td><td>0.04 <b>(+238.50%)</b></td><td>0.03 <b>(-22.60%)</b></td><td>585.90 <b>(-70.46%)</b></td><td>449.86 <b>(-34.01%)</b></td><td>543.70 <b>(+23.88%)</b></td><td>241.50 (+9.42%)</td><td>167.87 <b>(-77.11%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1983.10 (n/a)</td><td>681.76 (n/a)</td><td>438.90 (n/a)</td><td>220.70 (n/a)</td><td>733.40 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 <b>(-30.35%)</b></td><td>0.05 <b>(-28.49%)</b></td><td>0.04 <b>(-30.03%)</b></td><td>0.03 (-15.03%)</td><td>0.02 <b>(-29.23%)</b></td><td>590.60 (+17.70%)</td><td>416.28 <b>(+37.92%)</b></td><td>427.20 <b>(+42.92%)</b></td><td>235.90 <b>(+43.58%)</b></td><td>149.34 (+19.08%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>501.80 (n/a)</td><td>301.82 (n/a)</td><td>298.90 (n/a)</td><td>164.30 (n/a)</td><td>125.41 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 <b>(+58.27%)</b></td><td>0.05 <b>(+27.46%)</b></td><td>0.04 (+14.81%)</td><td>0.03 <b>(+268.78%)</b></td><td>0.03 <b>(+37.42%)</b></td><td>555.80 <b>(-72.88%)</b></td><td>410.24 <b>(-43.59%)</b></td><td>444.20 (-12.90%)</td><td>161.60 <b>(-36.83%)</b></td><td>147.26 <b>(-80.32%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2049.70 (n/a)</td><td>727.30 (n/a)</td><td>510.00 (n/a)</td><td>255.80 (n/a)</td><td>748.41 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 (+11.03%)</td><td>0.06 <b>(+39.17%)</b></td><td>0.07 <b>(+70.52%)</b></td><td>0.04 <b>(+29.25%)</b></td><td>0.02 (-12.58%)</td><td>480.60 <b>(-22.63%)</b></td><td>306.14 <b>(-31.94%)</b></td><td>262.40 <b>(-41.35%)</b></td><td>243.40 (-9.95%)</td><td>100.24 <b>(-39.62%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>621.20 (n/a)</td><td>449.80 (n/a)</td><td>447.40 (n/a)</td><td>270.30 (n/a)</td><td>166.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.09 (+12.98%)</td><td>0.04 <b>(-27.01%)</b></td><td>0.03 <b>(-46.36%)</b></td><td>0.01 <b>(-74.97%)</b></td><td>0.03 <b>(+113.25%)</b></td><td>1880.60 <b>(+299.45%)</b></td><td>867.98 <b>(+140.49%)</b></td><td>616.10 <b>(+86.41%)</b></td><td>215.70 (-11.49%)</td><td>710.83 <b>(+629.35%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>470.80 (n/a)</td><td>360.92 (n/a)</td><td>330.50 (n/a)</td><td>243.70 (n/a)</td><td>97.46 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 <b>(-26.72%)</b></td><td>0.05 <b>(-22.48%)</b></td><td>0.06 (-19.94%)</td><td>0.03 <b>(+22.06%)</b></td><td>0.02 <b>(-32.50%)</b></td><td>588.90 (-18.07%)</td><td>376.60 (+14.85%)</td><td>314.90 <b>(+24.91%)</b></td><td>252.10 <b>(+36.49%)</b></td><td>149.08 <b>(-32.70%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>718.80 (n/a)</td><td>327.90 (n/a)</td><td>252.10 (n/a)</td><td>184.70 (n/a)</td><td>221.51 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.06 (-14.52%)</td><td>0.04 (-16.88%)</td><td>0.04 (-5.47%)</td><td>0.03 <b>(-30.12%)</b></td><td>0.01 (-7.05%)</td><td>650.10 <b>(+43.10%)</b></td><td>463.38 <b>(+22.97%)</b></td><td>469.10 (+5.80%)</td><td>291.50 (+16.97%)</td><td>145.96 <b>(+49.30%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>454.30 (n/a)</td><td>376.82 (n/a)</td><td>443.40 (n/a)</td><td>249.20 (n/a)</td><td>97.76 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.38 (-1.89%)</td><td>0.33 <b>(+20.24%)</b></td><td>0.33 (+2.36%)</td><td>0.29 <b>(+90.62%)</b></td><td>0.04 <b>(-67.25%)</b></td><td>337.90 <b>(-47.53%)</b></td><td>298.20 <b>(-27.41%)</b></td><td>297.20 (-2.30%)</td><td>256.00 (+1.95%)</td><td>30.70 <b>(-83.04%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.32 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>644.00 (n/a)</td><td>410.80 (n/a)</td><td>304.20 (n/a)</td><td>251.10 (n/a)</td><td>181.06 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.38 <b>(-26.93%)</b></td><td>0.31 (-7.67%)</td><td>0.31 (-12.28%)</td><td>0.21 <b>(+34.77%)</b></td><td>0.07 <b>(-55.79%)</b></td><td>466.50 <b>(-25.80%)</b></td><td>337.58 (-9.99%)</td><td>314.90 (+14.01%)</td><td>256.00 <b>(+36.83%)</b></td><td>86.64 <b>(-57.66%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.53 (n/a)</td><td>0.33 (n/a)</td><td>0.36 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>628.70 (n/a)</td><td>375.04 (n/a)</td><td>276.20 (n/a)</td><td>187.10 (n/a)</td><td>204.64 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.23 <b>(-33.85%)</b></td><td>0.17 (-19.92%)</td><td>0.17 (-1.66%)</td><td>0.05 <b>(-68.87%)</b></td><td>0.07 (-7.43%)</td><td>1917.10 <b>(+221.28%)</b></td><td>798.46 <b>(+55.83%)</b></td><td>568.40 (+1.68%)</td><td>430.00 <b>(+51.14%)</b></td><td>631.49 <b>(+385.75%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.35 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>596.70 (n/a)</td><td>512.40 (n/a)</td><td>559.00 (n/a)</td><td>284.50 (n/a)</td><td>130.00 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.26 <b>(-24.74%)</b></td><td>0.17 <b>(-32.45%)</b></td><td>0.14 <b>(-49.93%)</b></td><td>0.09 <b>(-33.08%)</b></td><td>0.07 (-8.59%)</td><td>776.70 <b>(+49.42%)</b></td><td>494.04 <b>(+55.06%)</b></td><td>514.30 <b>(+99.73%)</b></td><td>287.20 <b>(+32.90%)</b></td><td>204.13 <b>(+65.91%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.29 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>519.80 (n/a)</td><td>318.62 (n/a)</td><td>257.50 (n/a)</td><td>216.10 (n/a)</td><td>123.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.31 <b>(+21.76%)</b></td><td>0.19 <b>(+54.73%)</b></td><td>0.15 (+1.93%)</td><td>0.09 <b>(+204.36%)</b></td><td>0.09 (+1.47%)</td><td>810.40 <b>(-67.14%)</b></td><td>466.84 <b>(-58.48%)</b></td><td>502.00 (-1.88%)</td><td>236.00 (-17.88%)</td><td>231.65 <b>(-76.47%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.09 (n/a)</td><td>2466.40 (n/a)</td><td>1124.46 (n/a)</td><td>511.60 (n/a)</td><td>287.40 (n/a)</td><td>984.48 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.24 <b>(-24.36%)</b></td><td>0.19 (-6.71%)</td><td>0.16 (-5.23%)</td><td>0.15 (-6.02%)</td><td>0.04 <b>(-35.39%)</b></td><td>476.20 (+6.41%)</td><td>405.60 (+4.66%)</td><td>460.60 (+5.52%)</td><td>307.70 <b>(+32.17%)</b></td><td>83.35 (-7.36%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.32 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>447.50 (n/a)</td><td>387.54 (n/a)</td><td>436.50 (n/a)</td><td>232.80 (n/a)</td><td>89.98 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 (+6.14%)</td><td>0.14 <b>(+35.21%)</b></td><td>0.14 <b>(+27.00%)</b></td><td>0.11 <b>(+89.76%)</b></td><td>0.02 <b>(-56.21%)</b></td><td>322.50 <b>(-47.30%)</b></td><td>269.42 <b>(-33.76%)</b></td><td>258.60 <b>(-21.25%)</b></td><td>232.30 (-5.80%)</td><td>34.12 <b>(-78.90%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>611.90 (n/a)</td><td>406.72 (n/a)</td><td>328.40 (n/a)</td><td>246.60 (n/a)</td><td>161.68 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.18 <b>(+38.43%)</b></td><td>0.12 <b>(+33.00%)</b></td><td>0.14 (+9.69%)</td><td>0.06 <b>(+243.22%)</b></td><td>0.04 (-10.18%)</td><td>567.40 <b>(-70.87%)</b></td><td>339.42 <b>(-50.10%)</b></td><td>271.30 (-8.84%)</td><td>204.40 <b>(-27.75%)</b></td><td>144.00 <b>(-79.99%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1947.60 (n/a)</td><td>680.26 (n/a)</td><td>297.60 (n/a)</td><td>282.90 (n/a)</td><td>719.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.15 (-3.19%)</td><td>0.08 <b>(-30.47%)</b></td><td>0.06 <b>(-47.96%)</b></td><td>0.06 (-19.07%)</td><td>0.04 (-0.12%)</td><td>665.60 <b>(+23.56%)</b></td><td>540.84 <b>(+46.85%)</b></td><td>600.10 <b>(+92.15%)</b></td><td>243.70 (+3.31%)</td><td>170.32 (+18.43%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>538.70 (n/a)</td><td>368.30 (n/a)</td><td>312.30 (n/a)</td><td>235.90 (n/a)</td><td>143.82 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (-19.33%)</td><td>0.08 <b>(-24.23%)</b></td><td>0.07 (-11.32%)</td><td>0.05 <b>(-23.01%)</b></td><td>0.03 <b>(-30.99%)</b></td><td>742.60 <b>(+29.87%)</b></td><td>520.16 <b>(+28.22%)</b></td><td>504.10 (+12.77%)</td><td>302.10 <b>(+23.96%)</b></td><td>156.88 (+10.09%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>571.80 (n/a)</td><td>405.68 (n/a)</td><td>447.00 (n/a)</td><td>243.70 (n/a)</td><td>142.51 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 <b>(+55.08%)</b></td><td>0.09 <b>(+30.84%)</b></td><td>0.08 (+2.78%)</td><td>0.06 <b>(+76.94%)</b></td><td>0.04 <b>(+47.52%)</b></td><td>638.50 <b>(-43.49%)</b></td><td>447.34 <b>(-26.71%)</b></td><td>456.20 (-2.71%)</td><td>236.70 <b>(-35.52%)</b></td><td>145.32 <b>(-52.27%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1129.80 (n/a)</td><td>610.34 (n/a)</td><td>468.90 (n/a)</td><td>367.10 (n/a)</td><td>304.46 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (-8.61%)</td><td>0.08 (-18.85%)</td><td>0.07 (-8.87%)</td><td>0.01 <b>(-75.87%)</b></td><td>0.05 (+10.20%)</td><td>2503.90 <b>(+314.42%)</b></td><td>845.80 <b>(+95.68%)</b></td><td>543.80 (+9.73%)</td><td>260.80 (+9.40%)</td><td>939.94 <b>(+432.90%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>604.20 (n/a)</td><td>432.24 (n/a)</td><td>495.60 (n/a)</td><td>238.40 (n/a)</td><td>176.38 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.20 <b>(+23.26%)</b></td><td>0.15 <b>(+24.11%)</b></td><td>0.16 (+17.77%)</td><td>0.09 <b>(+27.14%)</b></td><td>0.04 (+2.50%)</td><td>459.20 <b>(-21.34%)</b></td><td>286.10 <b>(-21.48%)</b></td><td>260.00 (-15.09%)</td><td>204.60 (-18.87%)</td><td>99.52 <b>(-28.59%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>583.80 (n/a)</td><td>364.38 (n/a)</td><td>306.20 (n/a)</td><td>252.20 (n/a)</td><td>139.36 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.15 (-0.35%)</td><td>0.11 (-12.10%)</td><td>0.13 (-9.43%)</td><td>0.02 (-14.94%)</td><td>0.06 (-2.13%)</td><td>2420.60 (+17.57%)</td><td>754.92 (+18.05%)</td><td>309.80 (+10.41%)</td><td>268.60 (+0.37%)</td><td>934.98 (+17.79%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2058.90 (n/a)</td><td>639.50 (n/a)</td><td>280.60 (n/a)</td><td>267.60 (n/a)</td><td>793.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.08 <b>(-48.89%)</b></td><td>0.07 <b>(-25.87%)</b></td><td>0.08 (-13.04%)</td><td>0.06 (-14.12%)</td><td>0.01 <b>(-75.32%)</b></td><td>679.10 (+16.44%)</td><td>554.54 <b>(+25.93%)</b></td><td>526.40 (+14.98%)</td><td>486.80 <b>(+95.66%)</b></td><td>74.87 <b>(-38.73%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>583.20 (n/a)</td><td>440.36 (n/a)</td><td>457.80 (n/a)</td><td>248.80 (n/a)</td><td>122.18 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.17 (-16.01%)</td><td>0.11 (-7.30%)</td><td>0.08 (+5.54%)</td><td>0.07 (+8.07%)</td><td>0.04 <b>(-29.52%)</b></td><td>549.60 (-7.47%)</td><td>429.54 (-0.92%)</td><td>510.40 (-5.27%)</td><td>241.70 (+19.06%)</td><td>145.39 <b>(-22.31%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>594.00 (n/a)</td><td>433.52 (n/a)</td><td>538.80 (n/a)</td><td>203.00 (n/a)</td><td>187.14 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.15 (+0.98%)</td><td>0.11 (+1.52%)</td><td>0.10 (+3.62%)</td><td>0.07 (+15.25%)</td><td>0.03 (-8.93%)</td><td>605.90 (-13.22%)</td><td>410.30 (-4.31%)</td><td>404.90 (-3.48%)</td><td>278.50 (-0.96%)</td><td>135.45 <b>(-20.70%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>698.20 (n/a)</td><td>428.76 (n/a)</td><td>419.50 (n/a)</td><td>281.20 (n/a)</td><td>170.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (-5.58%)</td><td>0.07 <b>(-28.78%)</b></td><td>0.08 (-17.29%)</td><td>0.02 <b>(-69.22%)</b></td><td>0.04 (+17.56%)</td><td>1934.20 <b>(+224.91%)</b></td><td>793.58 <b>(+85.29%)</b></td><td>544.70 <b>(+20.91%)</b></td><td>297.50 (+5.91%)</td><td>650.80 <b>(+369.89%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>595.30 (n/a)</td><td>428.28 (n/a)</td><td>450.50 (n/a)</td><td>280.90 (n/a)</td><td>138.50 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.16 (+11.37%)</td><td>0.10 (-3.42%)</td><td>0.10 (-14.69%)</td><td>0.02 <b>(-68.40%)</b></td><td>0.05 <b>(+45.71%)</b></td><td>1917.90 <b>(+216.43%)</b></td><td>634.18 <b>(+64.13%)</b></td><td>361.00 (+17.21%)</td><td>216.90 (-10.22%)</td><td>722.07 <b>(+352.79%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>606.10 (n/a)</td><td>386.40 (n/a)</td><td>308.00 (n/a)</td><td>241.60 (n/a)</td><td>159.47 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.13 (+3.55%)</td><td>0.09 (-7.02%)</td><td>0.09 (-19.28%)</td><td>0.05 (-8.86%)</td><td>0.03 (+2.34%)</td><td>637.40 (+9.73%)</td><td>438.28 (+8.47%)</td><td>393.20 <b>(+23.88%)</b></td><td>266.10 (-3.41%)</td><td>160.48 (+8.40%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>580.90 (n/a)</td><td>404.06 (n/a)</td><td>317.40 (n/a)</td><td>275.50 (n/a)</td><td>148.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 <b>(-46.30%)</b></td><td>0.09 (-1.81%)</td><td>0.07 (+16.86%)</td><td>0.07 <b>(+110.84%)</b></td><td>0.02 <b>(-74.46%)</b></td><td>484.30 <b>(-52.57%)</b></td><td>420.10 <b>(-24.62%)</b></td><td>465.60 (-14.44%)</td><td>322.50 <b>(+86.20%)</b></td><td>76.15 <b>(-75.12%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1021.10 (n/a)</td><td>557.32 (n/a)</td><td>544.20 (n/a)</td><td>173.20 (n/a)</td><td>306.09 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (+19.26%)</td><td>0.09 (+2.45%)</td><td>0.07 <b>(-31.14%)</b></td><td>0.06 <b>(+246.19%)</b></td><td>0.03 (-18.59%)</td><td>555.90 <b>(-71.11%)</b></td><td>422.44 <b>(-34.99%)</b></td><td>490.60 <b>(+45.23%)</b></td><td>251.90 (-16.15%)</td><td>131.43 <b>(-81.57%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1924.50 (n/a)</td><td>649.84 (n/a)</td><td>337.80 (n/a)</td><td>300.40 (n/a)</td><td>713.09 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (+7.91%)</td><td>0.09 (-0.40%)</td><td>0.08 (+1.64%)</td><td>0.06 (-10.38%)</td><td>0.03 (+14.31%)</td><td>617.10 (+11.59%)</td><td>422.54 (+2.79%)</td><td>447.40 (-1.63%)</td><td>245.90 (-7.31%)</td><td>143.13 (+18.33%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>553.00 (n/a)</td><td>411.06 (n/a)</td><td>454.80 (n/a)</td><td>265.30 (n/a)</td><td>120.95 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.11 (-10.91%)</td><td>0.08 (-7.42%)</td><td>0.08 (-9.67%)</td><td>0.03 <b>(-48.00%)</b></td><td>0.03 <b>(+33.16%)</b></td><td>1032.70 <b>(+92.31%)</b></td><td>514.26 <b>(+24.13%)</b></td><td>445.80 (+10.70%)</td><td>303.20 (+12.25%)</td><td>300.42 <b>(+190.50%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>537.00 (n/a)</td><td>414.28 (n/a)</td><td>402.70 (n/a)</td><td>270.10 (n/a)</td><td>103.41 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.49 (-8.34%)</td><td>0.35 (+1.35%)</td><td>0.32 <b>(+21.22%)</b></td><td>0.21 (-6.74%)</td><td>0.13 (-14.32%)</td><td>628.10 (+7.22%)</td><td>417.16 (-3.87%)</td><td>414.30 (-17.50%)</td><td>268.40 (+9.11%)</td><td>152.98 (-5.45%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.53 (n/a)</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>585.80 (n/a)</td><td>433.94 (n/a)</td><td>502.20 (n/a)</td><td>246.00 (n/a)</td><td>161.80 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.39 <b>(+34.91%)</b></td><td>0.31 <b>(+29.98%)</b></td><td>0.32 <b>(+37.99%)</b></td><td>0.24 (+14.71%)</td><td>0.06 <b>(+77.18%)</b></td><td>555.40 (-12.82%)</td><td>431.96 <b>(-21.87%)</b></td><td>415.90 <b>(-27.53%)</b></td><td>333.20 <b>(-25.89%)</b></td><td>85.47 (+16.20%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>637.10 (n/a)</td><td>552.86 (n/a)</td><td>573.90 (n/a)</td><td>449.60 (n/a)</td><td>73.55 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.53 (+13.38%)</td><td>0.39 <b>(+36.98%)</b></td><td>0.37 <b>(+39.65%)</b></td><td>0.27 <b>(+69.39%)</b></td><td>0.10 (-17.27%)</td><td>493.00 <b>(-40.96%)</b></td><td>353.14 <b>(-33.63%)</b></td><td>357.50 <b>(-28.40%)</b></td><td>249.50 (-11.81%)</td><td>95.80 <b>(-57.58%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>835.00 (n/a)</td><td>532.06 (n/a)</td><td>499.30 (n/a)</td><td>282.90 (n/a)</td><td>225.82 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.00 (-12.50%)</td><td>0.00 (+9.09%)</td><td>0.00 <b>(+100.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+3.13%)</td><td>20906.15 (-0.15%)</td><td>11896.23 (-3.89%)</td><td>7355.38 <b>(-49.03%)</b></td><td>6128.98 (+15.63%)</td><td>7352.77 (+12.65%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20937.02 (n/a)</td><td>12378.30 (n/a)</td><td>14429.78 (n/a)</td><td>5300.67 (n/a)</td><td>6527.12 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.00 <b>(+30.00%)</b></td><td>0.00 (-2.86%)</td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+35.55%)</b></td><td>22877.59 <b>(+21.10%)</b></td><td>15636.08 <b>(+20.85%)</b></td><td>16800.66 (+18.05%)</td><td>6370.63 <b>(-21.59%)</b></td><td>7441.22 <b>(+60.53%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18892.26 (n/a)</td><td>12938.64 (n/a)</td><td>14232.17 (n/a)</td><td>8124.65 (n/a)</td><td>4635.26 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.15 (+17.82%)</td><td>0.11 (+8.88%)</td><td>0.11 <b>(+27.84%)</b></td><td>0.07 (-3.98%)</td><td>0.03 <b>(+28.52%)</b></td><td>31065.28 (+4.08%)</td><td>21487.67 (-5.70%)</td><td>19184.60 <b>(-21.78%)</b></td><td>13967.92 (-15.15%)</td><td>6870.78 (+19.99%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29848.17 (n/a)</td><td>22786.95 (n/a)</td><td>24525.94 (n/a)</td><td>16461.40 (n/a)</td><td>5726.25 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>2.06 (+11.81%)</td><td>1.65 <b>(+21.30%)</b></td><td>1.68 (+7.17%)</td><td>1.31 <b>(+340.49%)</b></td><td>0.34 <b>(-45.83%)</b></td><td>802.60 <b>(-77.30%)</b></td><td>659.30 <b>(-46.44%)</b></td><td>622.40 (-6.69%)</td><td>509.90 (-10.56%)</td><td>136.09 <b>(-89.45%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>1.84 (n/a)</td><td>1.36 (n/a)</td><td>1.57 (n/a)</td><td>0.30 (n/a)</td><td>0.62 (n/a)</td><td>3535.30 (n/a)</td><td>1231.00 (n/a)</td><td>667.00 (n/a)</td><td>570.10 (n/a)</td><td>1290.35 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>3.57 (+11.34%)</td><td>2.21 <b>(+23.87%)</b></td><td>1.80 <b>(+59.06%)</b></td><td>1.38 <b>(+177.04%)</b></td><td>0.88 <b>(-31.55%)</b></td><td>757.10 <b>(-63.91%)</b></td><td>531.58 <b>(-44.69%)</b></td><td>583.40 <b>(-37.13%)</b></td><td>294.10 (-10.20%)</td><td>183.77 <b>(-74.72%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.20 (n/a)</td><td>1.78 (n/a)</td><td>1.13 (n/a)</td><td>0.50 (n/a)</td><td>1.29 (n/a)</td><td>2097.60 (n/a)</td><td>961.10 (n/a)</td><td>927.90 (n/a)</td><td>327.50 (n/a)</td><td>726.94 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>2.99 (-12.88%)</td><td>1.97 (-18.87%)</td><td>1.50 <b>(-45.82%)</b></td><td>1.16 (-16.36%)</td><td>0.86 (+1.52%)</td><td>907.70 (+19.54%)</td><td>617.36 <b>(+27.33%)</b></td><td>696.90 <b>(+84.56%)</b></td><td>351.20 (+14.77%)</td><td>244.97 <b>(+27.98%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.43 (n/a)</td><td>2.42 (n/a)</td><td>2.78 (n/a)</td><td>1.38 (n/a)</td><td>0.85 (n/a)</td><td>759.30 (n/a)</td><td>484.84 (n/a)</td><td>377.60 (n/a)</td><td>306.00 (n/a)</td><td>191.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>2.95 <b>(-22.07%)</b></td><td>2.00 <b>(-20.94%)</b></td><td>1.80 <b>(-31.10%)</b></td><td>1.48 (-6.58%)</td><td>0.56 <b>(-32.73%)</b></td><td>710.80 (+7.05%)</td><td>551.72 <b>(+22.26%)</b></td><td>581.00 <b>(+45.10%)</b></td><td>355.00 <b>(+28.30%)</b></td><td>129.62 (-12.44%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.79 (n/a)</td><td>2.54 (n/a)</td><td>2.62 (n/a)</td><td>1.58 (n/a)</td><td>0.84 (n/a)</td><td>664.00 (n/a)</td><td>451.26 (n/a)</td><td>400.40 (n/a)</td><td>276.70 (n/a)</td><td>148.05 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>4.10 (-5.43%)</td><td>2.99 (-9.54%)</td><td>3.02 (-9.74%)</td><td>2.00 (+4.63%)</td><td>0.85 (-4.66%)</td><td>1048.10 (-4.42%)</td><td>748.74 (+9.55%)</td><td>693.40 (+10.78%)</td><td>511.30 (+5.73%)</td><td>218.15 (-8.73%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>4.34 (n/a)</td><td>3.31 (n/a)</td><td>3.35 (n/a)</td><td>1.91 (n/a)</td><td>0.89 (n/a)</td><td>1096.60 (n/a)</td><td>683.48 (n/a)</td><td>625.90 (n/a)</td><td>483.60 (n/a)</td><td>239.01 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.43 <b>(+27.19%)</b></td><td>3.90 <b>(+25.15%)</b></td><td>3.60 (+0.08%)</td><td>1.96 <b>(+235.78%)</b></td><td>2.03 <b>(+22.92%)</b></td><td>1070.70 <b>(-70.22%)</b></td><td>682.50 <b>(-42.65%)</b></td><td>583.00 (-0.07%)</td><td>326.40 <b>(-21.37%)</b></td><td>358.89 <b>(-73.43%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.05 (n/a)</td><td>3.11 (n/a)</td><td>3.59 (n/a)</td><td>0.58 (n/a)</td><td>1.65 (n/a)</td><td>3595.10 (n/a)</td><td>1190.12 (n/a)</td><td>583.40 (n/a)</td><td>415.10 (n/a)</td><td>1350.87 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>4.89 (-8.04%)</td><td>4.38 (+19.54%)</td><td>4.30 (+8.89%)</td><td>3.85 <b>(+58.35%)</b></td><td>0.40 <b>(-67.26%)</b></td><td>544.20 <b>(-36.85%)</b></td><td>481.66 <b>(-23.30%)</b></td><td>487.40 (-8.18%)</td><td>429.20 (+8.74%)</td><td>44.53 <b>(-79.20%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.31 (n/a)</td><td>3.67 (n/a)</td><td>3.95 (n/a)</td><td>2.43 (n/a)</td><td>1.22 (n/a)</td><td>861.80 (n/a)</td><td>628.00 (n/a)</td><td>530.80 (n/a)</td><td>394.70 (n/a)</td><td>214.04 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.46 (+12.83%)</td><td>2.67 <b>(-21.35%)</b></td><td>1.34 <b>(-61.16%)</b></td><td>0.59 (-2.98%)</td><td>2.50 <b>(+35.02%)</b></td><td>3552.60 (+3.07%)</td><td>1623.94 <b>(+44.77%)</b></td><td>1569.10 <b>(+157.44%)</b></td><td>324.60 (-11.38%)</td><td>1312.67 (+0.60%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.73 (n/a)</td><td>3.40 (n/a)</td><td>3.44 (n/a)</td><td>0.61 (n/a)</td><td>1.85 (n/a)</td><td>3446.70 (n/a)</td><td>1121.70 (n/a)</td><td>609.50 (n/a)</td><td>366.30 (n/a)</td><td>1304.85 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>6.46 <b>(+20.47%)</b></td><td>4.30 <b>(+21.68%)</b></td><td>3.86 <b>(+52.45%)</b></td><td>2.07 (-10.43%)</td><td>2.01 <b>(+34.58%)</b></td><td>1010.90 (+11.65%)</td><td>593.10 (-12.51%)</td><td>543.90 <b>(-34.41%)</b></td><td>324.60 (-16.98%)</td><td>292.65 (+17.62%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.36 (n/a)</td><td>3.53 (n/a)</td><td>2.53 (n/a)</td><td>2.32 (n/a)</td><td>1.49 (n/a)</td><td>905.40 (n/a)</td><td>677.88 (n/a)</td><td>829.20 (n/a)</td><td>391.00 (n/a)</td><td>248.82 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>7.62 <b>(+21.87%)</b></td><td>3.45 (-19.37%)</td><td>2.90 <b>(-39.71%)</b></td><td>0.59 <b>(-72.85%)</b></td><td>2.59 <b>(+63.15%)</b></td><td>3567.80 <b>(+268.27%)</b></td><td>1196.98 <b>(+112.95%)</b></td><td>723.20 <b>(+65.87%)</b></td><td>275.20 (-17.95%)</td><td>1342.52 <b>(+428.77%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>6.25 (n/a)</td><td>4.28 (n/a)</td><td>4.81 (n/a)</td><td>2.16 (n/a)</td><td>1.59 (n/a)</td><td>968.80 (n/a)</td><td>562.10 (n/a)</td><td>436.00 (n/a)</td><td>335.40 (n/a)</td><td>253.89 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>5.17 (+2.16%)</td><td>3.92 (+2.88%)</td><td>4.35 (+6.04%)</td><td>1.69 <b>(+45.34%)</b></td><td>1.40 (-10.43%)</td><td>2486.00 <b>(-31.20%)</b></td><td>1261.28 (-14.81%)</td><td>964.80 (-5.70%)</td><td>811.50 (-2.11%)</td><td>699.57 <b>(-41.53%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>5.06 (n/a)</td><td>3.81 (n/a)</td><td>4.10 (n/a)</td><td>1.16 (n/a)</td><td>1.56 (n/a)</td><td>3613.20 (n/a)</td><td>1480.48 (n/a)</td><td>1023.10 (n/a)</td><td>829.00 (n/a)</td><td>1196.49 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>7.80 (-1.43%)</td><td>5.16 (-4.84%)</td><td>6.00 <b>(+47.76%)</b></td><td>1.69 <b>(-51.86%)</b></td><td>2.42 (+8.39%)</td><td>2485.20 <b>(+107.74%)</b></td><td>1094.24 <b>(+24.52%)</b></td><td>698.50 <b>(-32.32%)</b></td><td>537.80 (+1.45%)</td><td>806.59 <b>(+152.07%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>7.91 (n/a)</td><td>5.42 (n/a)</td><td>4.06 (n/a)</td><td>3.51 (n/a)</td><td>2.23 (n/a)</td><td>1196.30 (n/a)</td><td>878.76 (n/a)</td><td>1032.10 (n/a)</td><td>530.10 (n/a)</td><td>319.99 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>8.23 (+0.53%)</td><td>5.28 (-17.43%)</td><td>5.84 (-4.24%)</td><td>1.70 <b>(-68.16%)</b></td><td>2.56 <b>(+139.68%)</b></td><td>2463.70 <b>(+214.09%)</b></td><td>1079.66 <b>(+61.46%)</b></td><td>718.10 (+4.44%)</td><td>509.80 (-0.53%)</td><td>803.81 <b>(+712.20%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>8.18 (n/a)</td><td>6.40 (n/a)</td><td>6.10 (n/a)</td><td>5.35 (n/a)</td><td>1.07 (n/a)</td><td>784.40 (n/a)</td><td>668.68 (n/a)</td><td>687.60 (n/a)</td><td>512.50 (n/a)</td><td>98.97 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>9.03 (-1.42%)</td><td>6.56 (+15.19%)</td><td>7.53 <b>(+65.99%)</b></td><td>1.18 <b>(-29.94%)</b></td><td>3.12 (-3.69%)</td><td>3563.00 <b>(+42.73%)</b></td><td>1141.78 (+6.71%)</td><td>556.70 <b>(-39.75%)</b></td><td>464.50 (+1.44%)</td><td>1354.71 <b>(+62.09%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>9.16 (n/a)</td><td>5.70 (n/a)</td><td>4.54 (n/a)</td><td>1.68 (n/a)</td><td>3.24 (n/a)</td><td>2496.30 (n/a)</td><td>1070.02 (n/a)</td><td>924.00 (n/a)</td><td>457.90 (n/a)</td><td>835.79 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>10.49 (+13.26%)</td><td>6.26 <b>(+44.72%)</b></td><td>6.52 <b>(+69.48%)</b></td><td>1.92 <b>(+54.30%)</b></td><td>3.59 (+13.21%)</td><td>2186.00 <b>(-35.19%)</b></td><td>981.58 <b>(-36.91%)</b></td><td>643.20 <b>(-41.00%)</b></td><td>399.90 (-11.70%)</td><td>744.08 <b>(-36.91%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>9.26 (n/a)</td><td>4.33 (n/a)</td><td>3.85 (n/a)</td><td>1.24 (n/a)</td><td>3.17 (n/a)</td><td>3373.00 (n/a)</td><td>1555.94 (n/a)</td><td>1090.20 (n/a)</td><td>452.90 (n/a)</td><td>1179.40 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>7.48 (-0.74%)</td><td>5.54 (+19.02%)</td><td>6.10 <b>(+48.76%)</b></td><td>3.04 (-4.12%)</td><td>1.82 (+8.90%)</td><td>1379.80 (+4.30%)</td><td>843.22 (-13.66%)</td><td>687.10 <b>(-32.78%)</b></td><td>561.00 (+0.74%)</td><td>338.10 <b>(+23.06%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>7.53 (n/a)</td><td>4.66 (n/a)</td><td>4.10 (n/a)</td><td>3.17 (n/a)</td><td>1.67 (n/a)</td><td>1322.90 (n/a)</td><td>976.66 (n/a)</td><td>1022.10 (n/a)</td><td>556.90 (n/a)</td><td>274.74 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>1.76 (+8.91%)</td><td>1.15 (+0.39%)</td><td>1.20 (+0.32%)</td><td>0.62 <b>(+25.20%)</b></td><td>0.48 (+8.15%)</td><td>847.00 <b>(-20.13%)</b></td><td>535.94 (-2.23%)</td><td>436.20 (-0.32%)</td><td>297.30 (-8.18%)</td><td>240.35 (-19.99%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>1.62 (n/a)</td><td>1.14 (n/a)</td><td>1.20 (n/a)</td><td>0.49 (n/a)</td><td>0.45 (n/a)</td><td>1060.50 (n/a)</td><td>548.16 (n/a)</td><td>437.60 (n/a)</td><td>323.80 (n/a)</td><td>300.39 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>2.43 (-4.75%)</td><td>1.66 (+15.68%)</td><td>1.76 (+1.17%)</td><td>0.30 <b>(-29.92%)</b></td><td>0.86 (-5.34%)</td><td>3543.90 <b>(+42.69%)</b></td><td>1148.32 (-3.18%)</td><td>596.30 (-1.14%)</td><td>432.10 (+5.01%)</td><td>1344.55 <b>(+43.63%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>2.55 (n/a)</td><td>1.43 (n/a)</td><td>1.74 (n/a)</td><td>0.42 (n/a)</td><td>0.91 (n/a)</td><td>2483.60 (n/a)</td><td>1186.08 (n/a)</td><td>603.20 (n/a)</td><td>411.50 (n/a)</td><td>936.14 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>3.93 (+10.10%)</td><td>2.54 (-12.25%)</td><td>2.51 (-16.20%)</td><td>0.60 <b>(-72.36%)</b></td><td>1.30 <b>(+131.91%)</b></td><td>3524.40 <b>(+261.81%)</b></td><td>1292.78 <b>(+72.55%)</b></td><td>836.40 (+19.33%)</td><td>533.70 (-9.17%)</td><td>1259.68 <b>(+717.62%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>3.57 (n/a)</td><td>2.89 (n/a)</td><td>2.99 (n/a)</td><td>2.15 (n/a)</td><td>0.56 (n/a)</td><td>974.10 (n/a)</td><td>749.20 (n/a)</td><td>700.90 (n/a)</td><td>587.60 (n/a)</td><td>154.07 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>2.01 <b>(+23.28%)</b></td><td>1.26 (+7.92%)</td><td>1.07 (+10.93%)</td><td>0.86 (-5.28%)</td><td>0.49 <b>(+49.25%)</b></td><td>607.70 (+5.58%)</td><td>460.84 (-2.86%)</td><td>489.10 (-9.86%)</td><td>260.90 (-18.90%)</td><td>150.47 <b>(+28.77%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>1.63 (n/a)</td><td>1.17 (n/a)</td><td>0.97 (n/a)</td><td>0.91 (n/a)</td><td>0.32 (n/a)</td><td>575.60 (n/a)</td><td>474.42 (n/a)</td><td>542.60 (n/a)</td><td>321.70 (n/a)</td><td>116.85 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.12 (-14.87%)</td><td>0.09 <b>(-20.52%)</b></td><td>0.07 <b>(-45.28%)</b></td><td>0.06 (+5.33%)</td><td>0.03 <b>(-29.84%)</b></td><td>513.40 (-5.05%)</td><td>411.92 (+19.40%)</td><td>481.50 <b>(+82.80%)</b></td><td>269.70 (+17.47%)</td><td>116.25 (-19.20%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>540.70 (n/a)</td><td>345.00 (n/a)</td><td>263.40 (n/a)</td><td>229.60 (n/a)</td><td>143.88 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.14 (+7.57%)</td><td>0.10 (+18.26%)</td><td>0.11 <b>(+51.16%)</b></td><td>0.06 (+16.85%)</td><td>0.03 (-8.46%)</td><td>529.30 (-14.42%)</td><td>356.24 (-18.64%)</td><td>298.90 <b>(-33.86%)</b></td><td>231.20 (-7.04%)</td><td>119.04 <b>(-26.00%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>618.50 (n/a)</td><td>437.88 (n/a)</td><td>451.90 (n/a)</td><td>248.70 (n/a)</td><td>160.86 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.22 (+0.68%)</td><td>0.15 (+2.15%)</td><td>0.13 (-17.89%)</td><td>0.12 <b>(+95.15%)</b></td><td>0.04 <b>(-26.20%)</b></td><td>550.90 <b>(-48.76%)</b></td><td>466.14 (-14.21%)</td><td>512.10 <b>(+21.78%)</b></td><td>296.50 (-0.67%)</td><td>107.87 <b>(-65.02%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>1075.20 (n/a)</td><td>543.34 (n/a)</td><td>420.50 (n/a)</td><td>298.50 (n/a)</td><td>308.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.23 <b>(+37.65%)</b></td><td>0.15 (+10.57%)</td><td>0.15 (+10.72%)</td><td>0.11 (-1.34%)</td><td>0.04 <b>(+91.81%)</b></td><td>591.50 (+1.37%)</td><td>448.40 (-6.21%)</td><td>433.00 (-9.68%)</td><td>290.80 <b>(-27.35%)</b></td><td>114.50 <b>(+43.88%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>583.50 (n/a)</td><td>478.10 (n/a)</td><td>479.40 (n/a)</td><td>400.30 (n/a)</td><td>79.58 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.20 <b>(-33.18%)</b></td><td>0.13 <b>(-28.07%)</b></td><td>0.11 <b>(-29.11%)</b></td><td>0.10 (-14.19%)</td><td>0.04 <b>(-47.44%)</b></td><td>630.50 (+16.54%)</td><td>521.42 <b>(+30.92%)</b></td><td>599.10 <b>(+41.06%)</b></td><td>334.30 <b>(+49.64%)</b></td><td>128.58 (-9.11%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>541.00 (n/a)</td><td>398.28 (n/a)</td><td>424.70 (n/a)</td><td>223.40 (n/a)</td><td>141.47 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.49 <b>(-25.17%)</b></td><td>0.32 <b>(-20.84%)</b></td><td>0.28 <b>(-33.22%)</b></td><td>0.12 <b>(-41.42%)</b></td><td>0.15 (-18.56%)</td><td>1118.40 <b>(+70.70%)</b></td><td>529.94 <b>(+34.84%)</b></td><td>469.80 <b>(+49.76%)</b></td><td>265.50 <b>(+33.62%)</b></td><td>345.55 <b>(+78.60%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.66 (n/a)</td><td>0.40 (n/a)</td><td>0.42 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>655.20 (n/a)</td><td>393.00 (n/a)</td><td>313.70 (n/a)</td><td>198.70 (n/a)</td><td>193.48 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.50 (-15.03%)</td><td>0.37 (-12.35%)</td><td>0.41 (-4.39%)</td><td>0.23 (+6.40%)</td><td>0.12 (-9.33%)</td><td>563.60 (-6.02%)</td><td>391.18 (+12.95%)</td><td>322.40 (+4.61%)</td><td>259.60 (+17.68%)</td><td>140.37 (-4.13%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.59 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>599.70 (n/a)</td><td>346.32 (n/a)</td><td>308.20 (n/a)</td><td>220.60 (n/a)</td><td>146.42 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.51 (+2.34%)</td><td>0.31 (-2.05%)</td><td>0.26 (+9.46%)</td><td>0.21 (-1.44%)</td><td>0.12 (-5.18%)</td><td>613.20 (+1.47%)</td><td>462.92 (+0.41%)</td><td>503.80 (-8.65%)</td><td>258.00 (-2.31%)</td><td>140.29 (-9.47%)</td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.50 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>604.30 (n/a)</td><td>461.02 (n/a)</td><td>551.50 (n/a)</td><td>264.10 (n/a)</td><td>154.97 (n/a)</td>
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
<td><code>1f9e5a9</code> — 2026-07-13 18:05:30</td><td>0.07 <b>(+54.91%)</b></td><td>0.05 <b>(+32.85%)</b></td><td>0.05 <b>(+40.99%)</b></td><td>0.03 (+9.83%)</td><td>0.02 <b>(+140.75%)</b></td><td>491.30 (-8.95%)</td><td>370.70 <b>(-20.32%)</b></td><td>337.60 <b>(-29.08%)</b></td><td>230.70 <b>(-35.43%)</b></td><td>113.46 <b>(+47.48%)</b></td>
</tr>
<tr>
<td><code>17769b8</code> — 2026-07-09 22:43:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>539.60 (n/a)</td><td>465.26 (n/a)</td><td>476.00 (n/a)</td><td>357.30 (n/a)</td><td>76.93 (n/a)</td>
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
