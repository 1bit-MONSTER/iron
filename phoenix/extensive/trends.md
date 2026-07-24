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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(-32.51%)</b></td><td>0.01 <b>(-35.63%)</b></td><td>0.01 <b>(-43.78%)</b></td><td>0.01 (-8.72%)</td><td>0.00 <b>(-49.40%)</b></td><td>538.50 (+9.56%)</td><td>476.56 <b>(+49.82%)</b></td><td>524.60 <b>(+77.89%)</b></td><td>355.30 <b>(+48.17%)</b></td><td>78.88 <b>(-21.18%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.50 (n/a)</td><td>318.08 (n/a)</td><td>294.90 (n/a)</td><td>239.80 (n/a)</td><td>100.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (-4.90%)</td><td>0.02 <b>(+25.97%)</b></td><td>0.02 <b>(+48.15%)</b></td><td>0.01 <b>(+124.17%)</b></td><td>0.00 <b>(-36.64%)</b></td><td>529.10 <b>(-55.40%)</b></td><td>346.98 <b>(-36.62%)</b></td><td>304.80 <b>(-32.49%)</b></td><td>260.10 (+5.13%)</td><td>110.25 <b>(-70.73%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1186.20 (n/a)</td><td>547.50 (n/a)</td><td>451.50 (n/a)</td><td>247.40 (n/a)</td><td>376.64 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (-17.35%)</td><td>0.02 <b>(-34.91%)</b></td><td>0.01 <b>(-42.18%)</b></td><td>0.01 <b>(-46.26%)</b></td><td>0.00 <b>(+65.11%)</b></td><td>530.70 <b>(+86.08%)</b></td><td>403.44 <b>(+60.21%)</b></td><td>431.10 <b>(+72.92%)</b></td><td>272.90 <b>(+20.97%)</b></td><td>97.19 <b>(+268.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>285.20 (n/a)</td><td>251.82 (n/a)</td><td>249.30 (n/a)</td><td>225.60 (n/a)</td><td>26.40 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (-4.19%)</td><td>0.02 (-18.77%)</td><td>0.02 (-9.84%)</td><td>0.01 <b>(-33.16%)</b></td><td>0.01 <b>(+103.16%)</b></td><td>456.40 <b>(+49.59%)</b></td><td>331.08 <b>(+32.80%)</b></td><td>276.90 (+10.89%)</td><td>229.70 (+4.41%)</td><td>113.43 <b>(+230.29%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>305.10 (n/a)</td><td>249.30 (n/a)</td><td>249.70 (n/a)</td><td>220.00 (n/a)</td><td>34.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(+22.16%)</b></td><td>0.02 (+11.78%)</td><td>0.01 (+2.98%)</td><td>0.01 <b>(+29.12%)</b></td><td>0.01 <b>(+32.20%)</b></td><td>499.10 <b>(-22.55%)</b></td><td>426.82 (-9.78%)</td><td>465.60 (-2.90%)</td><td>242.90 (-18.16%)</td><td>104.04 (-16.78%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>644.40 (n/a)</td><td>473.10 (n/a)</td><td>479.50 (n/a)</td><td>296.80 (n/a)</td><td>125.02 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (+13.40%)</td><td>0.01 (-2.75%)</td><td>0.01 (-0.23%)</td><td>0.01 <b>(-22.17%)</b></td><td>0.01 (+12.11%)</td><td>1069.10 <b>(+28.48%)</b></td><td>535.78 (+9.10%)</td><td>450.00 (+0.22%)</td><td>219.90 (-11.83%)</td><td>321.12 <b>(+32.57%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>832.10 (n/a)</td><td>491.10 (n/a)</td><td>449.00 (n/a)</td><td>249.40 (n/a)</td><td>242.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (+16.07%)</td><td>0.04 <b>(+20.23%)</b></td><td>0.05 <b>(+33.49%)</b></td><td>0.02 (-2.93%)</td><td>0.02 <b>(+45.94%)</b></td><td>516.60 (+3.03%)</td><td>334.50 (-10.96%)</td><td>256.70 <b>(-25.09%)</b></td><td>200.50 (-13.87%)</td><td>148.61 <b>(+28.32%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.40 (n/a)</td><td>375.68 (n/a)</td><td>342.70 (n/a)</td><td>232.80 (n/a)</td><td>115.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (-4.25%)</td><td>0.03 (-17.28%)</td><td>0.02 <b>(-46.45%)</b></td><td>0.02 <b>(+21.99%)</b></td><td>0.01 (+7.03%)</td><td>571.40 (-18.02%)</td><td>439.94 <b>(+20.20%)</b></td><td>547.20 <b>(+86.76%)</b></td><td>239.50 (+4.45%)</td><td>162.98 (-13.36%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>697.00 (n/a)</td><td>366.02 (n/a)</td><td>293.00 (n/a)</td><td>229.30 (n/a)</td><td>188.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (+7.77%)</td><td>0.04 (+11.25%)</td><td>0.04 <b>(+43.26%)</b></td><td>0.02 (-14.42%)</td><td>0.01 <b>(+45.16%)</b></td><td>527.70 (+16.85%)</td><td>361.78 (-3.62%)</td><td>301.90 <b>(-30.18%)</b></td><td>227.50 (-7.22%)</td><td>145.43 <b>(+60.24%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>451.60 (n/a)</td><td>375.36 (n/a)</td><td>432.40 (n/a)</td><td>245.20 (n/a)</td><td>90.76 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (+6.54%)</td><td>0.03 (+4.03%)</td><td>0.02 <b>(-22.66%)</b></td><td>0.02 <b>(-26.53%)</b></td><td>0.02 <b>(+52.44%)</b></td><td>753.10 <b>(+36.11%)</b></td><td>477.86 (+10.35%)</td><td>568.20 <b>(+29.28%)</b></td><td>230.10 (-6.12%)</td><td>224.91 <b>(+93.73%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>553.30 (n/a)</td><td>433.04 (n/a)</td><td>439.50 (n/a)</td><td>245.10 (n/a)</td><td>116.09 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (-0.68%)</td><td>0.03 (-10.91%)</td><td>0.02 <b>(-27.61%)</b></td><td>0.02 <b>(+170.14%)</b></td><td>0.01 (-14.49%)</td><td>700.60 <b>(-62.98%)</b></td><td>552.36 (-19.34%)</td><td>660.20 <b>(+38.15%)</b></td><td>239.90 (+0.67%)</td><td>193.50 <b>(-71.69%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1892.60 (n/a)</td><td>684.76 (n/a)</td><td>477.90 (n/a)</td><td>238.30 (n/a)</td><td>683.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (+0.52%)</td><td>0.03 (+9.66%)</td><td>0.02 (+12.76%)</td><td>0.02 <b>(+23.76%)</b></td><td>0.01 (-10.11%)</td><td>571.90 (-19.19%)</td><td>478.44 (-12.95%)</td><td>522.70 (-11.32%)</td><td>244.60 (-0.49%)</td><td>133.33 <b>(-27.02%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>707.70 (n/a)</td><td>549.60 (n/a)</td><td>589.40 (n/a)</td><td>245.80 (n/a)</td><td>182.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (+1.79%)</td><td>0.07 (+18.12%)</td><td>0.08 <b>(+90.78%)</b></td><td>0.04 (+14.42%)</td><td>0.03 (-10.27%)</td><td>616.00 (-12.61%)</td><td>389.50 (-19.02%)</td><td>295.90 <b>(-47.58%)</b></td><td>254.00 (-1.74%)</td><td>164.91 (-18.86%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>704.90 (n/a)</td><td>481.00 (n/a)</td><td>564.50 (n/a)</td><td>258.50 (n/a)</td><td>203.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (+5.08%)</td><td>0.07 (+15.30%)</td><td>0.08 <b>(+67.79%)</b></td><td>0.04 (-5.90%)</td><td>0.02 (+3.06%)</td><td>608.10 (+6.27%)</td><td>374.92 (-12.57%)</td><td>298.70 <b>(-40.40%)</b></td><td>238.50 (-4.83%)</td><td>148.73 (+7.15%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>572.20 (n/a)</td><td>428.82 (n/a)</td><td>501.20 (n/a)</td><td>250.60 (n/a)</td><td>138.80 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (-2.55%)</td><td>0.07 (-8.68%)</td><td>0.08 (-16.20%)</td><td>0.04 (-17.76%)</td><td>0.03 (+2.69%)</td><td>608.20 <b>(+21.59%)</b></td><td>391.34 (+12.63%)</td><td>326.20 (+19.31%)</td><td>237.40 (+2.64%)</td><td>171.36 <b>(+23.20%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>500.20 (n/a)</td><td>347.46 (n/a)</td><td>273.40 (n/a)</td><td>231.30 (n/a)</td><td>139.09 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 <b>(+75.00%)</b></td><td>0.10 <b>(+30.58%)</b></td><td>0.09 (+4.01%)</td><td>0.06 <b>(+45.83%)</b></td><td>0.04 <b>(+70.73%)</b></td><td>442.80 <b>(-31.42%)</b></td><td>284.04 <b>(-23.08%)</b></td><td>278.30 (-3.87%)</td><td>148.40 <b>(-42.86%)</b></td><td>104.65 <b>(-35.61%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>645.70 (n/a)</td><td>369.28 (n/a)</td><td>289.50 (n/a)</td><td>259.70 (n/a)</td><td>162.53 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (-0.20%)</td><td>0.06 (-6.49%)</td><td>0.05 (+3.66%)</td><td>0.05 (+1.43%)</td><td>0.02 (-10.66%)</td><td>526.10 (-1.42%)</td><td>424.64 (+4.40%)</td><td>472.30 (-3.53%)</td><td>240.00 (+0.21%)</td><td>118.60 (-12.90%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>533.70 (n/a)</td><td>406.76 (n/a)</td><td>489.60 (n/a)</td><td>239.50 (n/a)</td><td>136.16 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (+9.04%)</td><td>0.06 (+4.66%)</td><td>0.06 <b>(+28.21%)</b></td><td>0.04 (+4.37%)</td><td>0.02 (-2.50%)</td><td>596.40 (-4.19%)</td><td>444.04 (-6.04%)</td><td>419.00 <b>(-21.99%)</b></td><td>264.60 (-8.32%)</td><td>133.08 (-13.34%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>622.50 (n/a)</td><td>472.60 (n/a)</td><td>537.10 (n/a)</td><td>288.60 (n/a)</td><td>153.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.18 (+1.75%)</td><td>0.11 (-13.49%)</td><td>0.10 (-13.22%)</td><td>0.04 <b>(-51.70%)</b></td><td>0.06 <b>(+47.89%)</b></td><td>1133.50 <b>(+107.03%)</b></td><td>556.10 <b>(+39.42%)</b></td><td>486.40 (+15.23%)</td><td>279.20 (-1.72%)</td><td>347.05 <b>(+208.60%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>547.50 (n/a)</td><td>398.86 (n/a)</td><td>422.10 (n/a)</td><td>284.10 (n/a)</td><td>112.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.20 (-5.45%)</td><td>0.17 <b>(+50.07%)</b></td><td>0.17 <b>(+93.79%)</b></td><td>0.12 <b>(+48.06%)</b></td><td>0.03 <b>(-46.45%)</b></td><td>403.10 <b>(-32.46%)</b></td><td>302.12 <b>(-39.36%)</b></td><td>286.90 <b>(-48.40%)</b></td><td>250.20 (+5.79%)</td><td>60.50 <b>(-59.25%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>596.80 (n/a)</td><td>498.22 (n/a)</td><td>556.00 (n/a)</td><td>236.50 (n/a)</td><td>148.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.18 (-8.20%)</td><td>0.12 (-13.24%)</td><td>0.12 <b>(-21.88%)</b></td><td>0.10 (-1.27%)</td><td>0.03 <b>(-24.04%)</b></td><td>509.40 (+1.27%)</td><td>415.46 (+11.79%)</td><td>410.00 <b>(+28.04%)</b></td><td>277.90 (+8.94%)</td><td>98.08 (-18.42%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>503.00 (n/a)</td><td>371.64 (n/a)</td><td>320.20 (n/a)</td><td>255.10 (n/a)</td><td>120.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.16 (-3.09%)</td><td>0.12 (+14.64%)</td><td>0.10 (-11.72%)</td><td>0.09 <b>(+295.14%)</b></td><td>0.03 <b>(-39.87%)</b></td><td>534.30 <b>(-74.69%)</b></td><td>440.78 <b>(-42.11%)</b></td><td>498.20 (+13.28%)</td><td>304.10 (+3.19%)</td><td>106.97 <b>(-85.94%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2111.10 (n/a)</td><td>761.36 (n/a)</td><td>439.80 (n/a)</td><td>294.70 (n/a)</td><td>760.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 (-4.17%)</td><td>0.13 (-4.84%)</td><td>0.11 <b>(-20.40%)</b></td><td>0.09 (+16.05%)</td><td>0.04 (-12.56%)</td><td>535.00 (-13.83%)</td><td>406.04 (+2.22%)</td><td>431.60 <b>(+25.65%)</b></td><td>291.70 (+4.36%)</td><td>107.25 <b>(-24.24%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>620.90 (n/a)</td><td>397.24 (n/a)</td><td>343.50 (n/a)</td><td>279.50 (n/a)</td><td>141.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.19 (-17.89%)</td><td>0.12 <b>(-27.31%)</b></td><td>0.11 <b>(-40.10%)</b></td><td>0.08 (-11.76%)</td><td>0.05 <b>(-22.80%)</b></td><td>608.20 (+13.34%)</td><td>452.14 <b>(+34.72%)</b></td><td>446.40 <b>(+66.94%)</b></td><td>255.10 <b>(+21.82%)</b></td><td>146.47 (+6.75%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>536.60 (n/a)</td><td>335.62 (n/a)</td><td>267.40 (n/a)</td><td>209.40 (n/a)</td><td>137.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (-17.06%)</td><td>0.01 <b>(-20.46%)</b></td><td>0.00 <b>(-47.28%)</b></td><td>0.00 <b>(-21.85%)</b></td><td>0.00 (-0.90%)</td><td>651.30 <b>(+27.96%)</b></td><td>466.26 <b>(+30.21%)</b></td><td>557.40 <b>(+89.72%)</b></td><td>270.10 <b>(+20.58%)</b></td><td>178.44 <b>(+35.15%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.00 (n/a)</td><td>358.08 (n/a)</td><td>293.80 (n/a)</td><td>224.00 (n/a)</td><td>132.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (-2.60%)</td><td>0.01 (-1.07%)</td><td>0.01 (+16.97%)</td><td>0.00 <b>(-25.01%)</b></td><td>0.00 (-7.19%)</td><td>837.50 <b>(+33.36%)</b></td><td>464.22 (+2.50%)</td><td>448.70 (-14.52%)</td><td>243.90 (+2.65%)</td><td>234.68 <b>(+24.79%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>628.00 (n/a)</td><td>452.90 (n/a)</td><td>524.90 (n/a)</td><td>237.60 (n/a)</td><td>188.06 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (-5.13%)</td><td>0.01 <b>(+37.55%)</b></td><td>0.01 <b>(+72.39%)</b></td><td>0.01 <b>(+61.09%)</b></td><td>0.00 <b>(-51.51%)</b></td><td>356.30 <b>(-37.93%)</b></td><td>285.40 <b>(-34.32%)</b></td><td>285.00 <b>(-42.00%)</b></td><td>225.70 (+5.42%)</td><td>46.84 <b>(-66.63%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>574.00 (n/a)</td><td>434.52 (n/a)</td><td>491.40 (n/a)</td><td>214.10 (n/a)</td><td>140.38 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 <b>(+27.49%)</b></td><td>0.01 <b>(+20.98%)</b></td><td>0.01 (+18.98%)</td><td>0.00 (-3.86%)</td><td>0.00 <b>(+53.06%)</b></td><td>563.70 (+4.00%)</td><td>404.58 (-13.90%)</td><td>433.20 (-15.97%)</td><td>232.10 <b>(-21.56%)</b></td><td>125.41 <b>(+24.15%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>542.00 (n/a)</td><td>469.90 (n/a)</td><td>515.50 (n/a)</td><td>295.90 (n/a)</td><td>101.01 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (+2.70%)</td><td>0.01 (-6.25%)</td><td>0.01 (-10.08%)</td><td>0.00 <b>(-75.61%)</b></td><td>0.00 <b>(+70.57%)</b></td><td>2471.50 <b>(+310.00%)</b></td><td>811.28 <b>(+81.73%)</b></td><td>455.60 (+11.20%)</td><td>273.70 (-2.63%)</td><td>933.96 <b>(+651.38%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>602.80 (n/a)</td><td>446.42 (n/a)</td><td>409.70 (n/a)</td><td>281.10 (n/a)</td><td>124.30 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 <b>(-44.11%)</b></td><td>0.00 <b>(-24.85%)</b></td><td>0.00 <b>(-21.70%)</b></td><td>0.00 (+0.94%)</td><td>0.00 <b>(-64.38%)</b></td><td>679.10 (-0.93%)</td><td>576.14 <b>(+22.61%)</b></td><td>616.60 <b>(+27.71%)</b></td><td>458.20 <b>(+78.98%)</b></td><td>103.11 <b>(-35.78%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>685.50 (n/a)</td><td>469.88 (n/a)</td><td>482.80 (n/a)</td><td>256.00 (n/a)</td><td>160.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(-21.21%)</b></td><td>0.01 (-14.10%)</td><td>0.01 <b>(-30.64%)</b></td><td>0.01 (-4.77%)</td><td>0.00 <b>(-22.53%)</b></td><td>494.60 (+5.01%)</td><td>388.90 (+14.52%)</td><td>449.60 <b>(+44.19%)</b></td><td>246.10 <b>(+26.92%)</b></td><td>114.20 (+3.00%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>471.00 (n/a)</td><td>339.60 (n/a)</td><td>311.80 (n/a)</td><td>193.90 (n/a)</td><td>110.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(-27.96%)</b></td><td>0.01 (-2.07%)</td><td>0.01 <b>(+28.80%)</b></td><td>0.01 (+0.52%)</td><td>0.00 <b>(-45.94%)</b></td><td>584.60 (-0.51%)</td><td>449.92 (-7.97%)</td><td>424.60 <b>(-22.36%)</b></td><td>266.40 <b>(+38.82%)</b></td><td>133.04 <b>(-20.32%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.60 (n/a)</td><td>488.86 (n/a)</td><td>546.90 (n/a)</td><td>191.90 (n/a)</td><td>166.98 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(+28.25%)</b></td><td>0.02 (+2.90%)</td><td>0.02 (-18.56%)</td><td>0.01 (-6.68%)</td><td>0.01 <b>(+51.91%)</b></td><td>552.00 (+7.16%)</td><td>355.70 (+7.35%)</td><td>315.90 <b>(+22.82%)</b></td><td>168.00 <b>(-22.04%)</b></td><td>174.98 <b>(+33.16%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>515.10 (n/a)</td><td>331.34 (n/a)</td><td>257.20 (n/a)</td><td>215.50 (n/a)</td><td>131.40 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(+41.95%)</b></td><td>0.01 (+16.16%)</td><td>0.01 (-2.61%)</td><td>0.01 (-0.42%)</td><td>0.01 <b>(+114.23%)</b></td><td>553.50 (+0.42%)</td><td>407.36 (-5.45%)</td><td>457.20 (+2.70%)</td><td>207.50 <b>(-29.54%)</b></td><td>147.43 <b>(+58.40%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.20 (n/a)</td><td>430.82 (n/a)</td><td>445.20 (n/a)</td><td>294.50 (n/a)</td><td>93.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 <b>(-46.39%)</b></td><td>0.01 <b>(-20.47%)</b></td><td>0.01 (+1.08%)</td><td>0.01 <b>(+24.90%)</b></td><td>0.00 <b>(-83.22%)</b></td><td>505.60 (-19.94%)</td><td>447.86 (+3.93%)</td><td>460.60 (-1.07%)</td><td>391.50 <b>(+86.52%)</b></td><td>47.80 <b>(-75.37%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>631.50 (n/a)</td><td>430.92 (n/a)</td><td>465.60 (n/a)</td><td>209.90 (n/a)</td><td>194.07 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(+38.30%)</b></td><td>0.01 (+15.10%)</td><td>0.01 (-2.11%)</td><td>0.01 (-16.79%)</td><td>0.01 <b>(+152.51%)</b></td><td>594.40 <b>(+20.18%)</b></td><td>420.72 (-3.58%)</td><td>473.60 (+2.16%)</td><td>230.70 <b>(-27.70%)</b></td><td>154.02 <b>(+122.98%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>494.60 (n/a)</td><td>436.34 (n/a)</td><td>463.60 (n/a)</td><td>319.10 (n/a)</td><td>69.07 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (-6.10%)</td><td>0.03 (+13.68%)</td><td>0.03 <b>(+27.33%)</b></td><td>0.02 <b>(+24.01%)</b></td><td>0.01 (-2.32%)</td><td>545.10 (-19.36%)</td><td>354.60 (-13.70%)</td><td>306.80 <b>(-21.45%)</b></td><td>212.60 (+6.51%)</td><td>152.21 (-15.54%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>676.00 (n/a)</td><td>410.90 (n/a)</td><td>390.60 (n/a)</td><td>199.60 (n/a)</td><td>180.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (-0.20%)</td><td>0.03 <b>(-23.56%)</b></td><td>0.02 <b>(-36.40%)</b></td><td>0.02 (+11.36%)</td><td>0.01 (-6.20%)</td><td>499.60 (-10.19%)</td><td>423.98 <b>(+28.04%)</b></td><td>444.30 <b>(+57.22%)</b></td><td>257.40 (+0.19%)</td><td>98.74 <b>(-21.85%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>556.30 (n/a)</td><td>331.12 (n/a)</td><td>282.60 (n/a)</td><td>256.90 (n/a)</td><td>126.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (+16.91%)</td><td>0.03 (+3.52%)</td><td>0.02 (-0.63%)</td><td>0.02 (-2.73%)</td><td>0.01 <b>(+29.72%)</b></td><td>598.40 (+2.82%)</td><td>406.72 (+1.66%)</td><td>431.10 (+0.65%)</td><td>215.60 (-14.48%)</td><td>165.03 (+18.95%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>582.00 (n/a)</td><td>400.06 (n/a)</td><td>428.30 (n/a)</td><td>252.10 (n/a)</td><td>138.74 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 <b>(+36.41%)</b></td><td>0.03 <b>(+25.05%)</b></td><td>0.02 (-2.56%)</td><td>0.01 (+1.02%)</td><td>0.02 <b>(+47.95%)</b></td><td>1915.50 (-1.01%)</td><td>677.86 (-8.34%)</td><td>467.60 (+2.61%)</td><td>215.70 <b>(-26.71%)</b></td><td>701.89 (+3.73%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1935.00 (n/a)</td><td>739.52 (n/a)</td><td>455.70 (n/a)</td><td>294.30 (n/a)</td><td>676.66 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 <b>(+30.09%)</b></td><td>0.03 <b>(+30.76%)</b></td><td>0.02 (+16.53%)</td><td>0.02 (+12.26%)</td><td>0.01 <b>(+56.40%)</b></td><td>604.40 (-10.92%)</td><td>413.68 (-18.99%)</td><td>426.30 (-14.17%)</td><td>224.10 <b>(-23.15%)</b></td><td>163.99 (+8.91%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>678.50 (n/a)</td><td>510.66 (n/a)</td><td>496.70 (n/a)</td><td>291.60 (n/a)</td><td>150.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(-39.46%)</b></td><td>0.02 (-19.71%)</td><td>0.02 (-4.40%)</td><td>0.02 <b>(-25.64%)</b></td><td>0.01 <b>(-47.49%)</b></td><td>624.50 <b>(+34.47%)</b></td><td>470.66 <b>(+20.95%)</b></td><td>445.20 (+4.61%)</td><td>354.60 <b>(+65.16%)</b></td><td>120.69 (+19.87%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>464.40 (n/a)</td><td>389.14 (n/a)</td><td>425.60 (n/a)</td><td>214.70 (n/a)</td><td>100.69 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 <b>(+29.53%)</b></td><td>0.06 (+12.17%)</td><td>0.07 <b>(+27.73%)</b></td><td>0.01 <b>(-69.29%)</b></td><td>0.03 <b>(+146.27%)</b></td><td>1899.50 <b>(+225.65%)</b></td><td>656.10 <b>(+47.64%)</b></td><td>305.90 <b>(-21.70%)</b></td><td>244.00 <b>(-22.81%)</b></td><td>705.63 <b>(+522.79%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>583.30 (n/a)</td><td>444.40 (n/a)</td><td>390.70 (n/a)</td><td>316.10 (n/a)</td><td>113.30 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (-11.86%)</td><td>0.07 (+17.03%)</td><td>0.07 <b>(+65.33%)</b></td><td>0.04 (+2.58%)</td><td>0.02 <b>(-31.20%)</b></td><td>536.10 (-2.53%)</td><td>328.50 (-19.10%)</td><td>280.70 <b>(-39.52%)</b></td><td>255.40 (+13.46%)</td><td>116.76 <b>(-20.14%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>550.00 (n/a)</td><td>406.06 (n/a)</td><td>464.10 (n/a)</td><td>225.10 (n/a)</td><td>146.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (+4.76%)</td><td>0.06 <b>(+34.53%)</b></td><td>0.07 <b>(+91.44%)</b></td><td>0.04 (+8.90%)</td><td>0.02 (+12.34%)</td><td>542.00 (-8.18%)</td><td>371.02 <b>(-24.91%)</b></td><td>297.00 <b>(-47.76%)</b></td><td>256.60 (-4.54%)</td><td>135.91 (-1.42%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>590.30 (n/a)</td><td>494.08 (n/a)</td><td>568.50 (n/a)</td><td>268.80 (n/a)</td><td>137.86 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 <b>(-60.22%)</b></td><td>0.05 <b>(-35.05%)</b></td><td>0.05 <b>(-23.66%)</b></td><td>0.04 (-6.84%)</td><td>0.01 <b>(-80.91%)</b></td><td>573.50 (+7.34%)</td><td>465.26 <b>(+30.03%)</b></td><td>454.80 <b>(+30.99%)</b></td><td>372.70 <b>(+151.48%)</b></td><td>79.65 <b>(-45.40%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>534.30 (n/a)</td><td>357.80 (n/a)</td><td>347.20 (n/a)</td><td>148.20 (n/a)</td><td>145.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (-11.32%)</td><td>0.06 (+12.52%)</td><td>0.06 <b>(+40.52%)</b></td><td>0.04 (-8.17%)</td><td>0.02 (-17.13%)</td><td>580.50 (+8.89%)</td><td>367.26 (-13.14%)</td><td>352.10 <b>(-28.83%)</b></td><td>223.90 (+12.74%)</td><td>142.33 (+0.73%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>533.10 (n/a)</td><td>422.84 (n/a)</td><td>494.70 (n/a)</td><td>198.60 (n/a)</td><td>141.30 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (-14.53%)</td><td>0.05 (-6.83%)</td><td>0.04 (+0.20%)</td><td>0.03 (+0.60%)</td><td>0.02 <b>(-22.49%)</b></td><td>610.70 (-0.60%)</td><td>499.12 (+3.46%)</td><td>519.50 (-0.21%)</td><td>256.20 (+16.99%)</td><td>145.08 (-6.70%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>614.40 (n/a)</td><td>482.44 (n/a)</td><td>520.60 (n/a)</td><td>219.00 (n/a)</td><td>155.49 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>607.20 (n/a)</td><td>475.64 (n/a)</td><td>512.00 (n/a)</td><td>295.90 (n/a)</td><td>115.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>449.30 (n/a)</td><td>331.56 (n/a)</td><td>295.40 (n/a)</td><td>271.70 (n/a)</td><td>76.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>392.40 (n/a)</td><td>341.54 (n/a)</td><td>337.50 (n/a)</td><td>298.60 (n/a)</td><td>38.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>602.80 (n/a)</td><td>405.82 (n/a)</td><td>315.80 (n/a)</td><td>229.00 (n/a)</td><td>182.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.80 (n/a)</td><td>360.20 (n/a)</td><td>271.40 (n/a)</td><td>248.60 (n/a)</td><td>139.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.90 (n/a)</td><td>362.38 (n/a)</td><td>325.10 (n/a)</td><td>268.00 (n/a)</td><td>96.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>507.50 (n/a)</td><td>324.78 (n/a)</td><td>289.00 (n/a)</td><td>241.90 (n/a)</td><td>104.43 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>358.10 (n/a)</td><td>295.26 (n/a)</td><td>295.30 (n/a)</td><td>234.10 (n/a)</td><td>56.73 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>843.70 (n/a)</td><td>432.34 (n/a)</td><td>296.40 (n/a)</td><td>249.90 (n/a)</td><td>251.09 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.20 (+11.78%)</td><td>0.13 (-14.41%)</td><td>0.11 <b>(-28.63%)</b></td><td>0.08 (-17.82%)</td><td>0.05 <b>(+46.54%)</b></td><td>579.20 <b>(+21.68%)</b></td><td>406.24 <b>(+22.79%)</b></td><td>441.10 <b>(+40.12%)</b></td><td>240.40 (-10.53%)</td><td>130.72 <b>(+54.05%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>476.00 (n/a)</td><td>330.84 (n/a)</td><td>314.80 (n/a)</td><td>268.70 (n/a)</td><td>84.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>607.00 (n/a)</td><td>459.38 (n/a)</td><td>478.20 (n/a)</td><td>227.90 (n/a)</td><td>159.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>627.50 (n/a)</td><td>479.22 (n/a)</td><td>472.80 (n/a)</td><td>234.40 (n/a)</td><td>156.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.80 (n/a)</td><td>357.36 (n/a)</td><td>289.40 (n/a)</td><td>249.30 (n/a)</td><td>143.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>654.10 (n/a)</td><td>421.64 (n/a)</td><td>348.80 (n/a)</td><td>236.40 (n/a)</td><td>176.78 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.60 (n/a)</td><td>403.80 (n/a)</td><td>468.80 (n/a)</td><td>193.50 (n/a)</td><td>162.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>321.60 (n/a)</td><td>260.72 (n/a)</td><td>263.10 (n/a)</td><td>202.10 (n/a)</td><td>46.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>564.90 (n/a)</td><td>353.72 (n/a)</td><td>302.30 (n/a)</td><td>239.30 (n/a)</td><td>129.25 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1981.80 (n/a)</td><td>912.28 (n/a)</td><td>608.00 (n/a)</td><td>267.30 (n/a)</td><td>736.21 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2085.40 (n/a)</td><td>779.20 (n/a)</td><td>516.00 (n/a)</td><td>314.40 (n/a)</td><td>736.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>519.50 (n/a)</td><td>350.84 (n/a)</td><td>342.30 (n/a)</td><td>249.50 (n/a)</td><td>110.42 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>506.00 (n/a)</td><td>337.76 (n/a)</td><td>309.70 (n/a)</td><td>239.00 (n/a)</td><td>102.63 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>538.90 (n/a)</td><td>378.56 (n/a)</td><td>403.50 (n/a)</td><td>194.70 (n/a)</td><td>165.48 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>520.40 (n/a)</td><td>377.98 (n/a)</td><td>361.60 (n/a)</td><td>259.10 (n/a)</td><td>122.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.80 (n/a)</td><td>486.26 (n/a)</td><td>518.20 (n/a)</td><td>329.50 (n/a)</td><td>112.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>763.70 (n/a)</td><td>376.12 (n/a)</td><td>269.80 (n/a)</td><td>228.80 (n/a)</td><td>225.06 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>648.00 (n/a)</td><td>440.34 (n/a)</td><td>495.20 (n/a)</td><td>230.00 (n/a)</td><td>177.32 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>535.10 (n/a)</td><td>451.44 (n/a)</td><td>495.20 (n/a)</td><td>239.40 (n/a)</td><td>121.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1033.00 (n/a)</td><td>552.96 (n/a)</td><td>544.00 (n/a)</td><td>226.10 (n/a)</td><td>308.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>791.60 (n/a)</td><td>506.90 (n/a)</td><td>580.40 (n/a)</td><td>252.20 (n/a)</td><td>236.14 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.90 (n/a)</td><td>403.80 (n/a)</td><td>487.30 (n/a)</td><td>190.50 (n/a)</td><td>134.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.00 (n/a)</td><td>307.96 (n/a)</td><td>267.00 (n/a)</td><td>205.40 (n/a)</td><td>123.30 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.70 (n/a)</td><td>315.76 (n/a)</td><td>274.00 (n/a)</td><td>230.80 (n/a)</td><td>130.72 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.40 (n/a)</td><td>409.02 (n/a)</td><td>473.20 (n/a)</td><td>227.50 (n/a)</td><td>132.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>639.50 (n/a)</td><td>435.30 (n/a)</td><td>457.70 (n/a)</td><td>175.50 (n/a)</td><td>167.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1955.20 (n/a)</td><td>716.88 (n/a)</td><td>546.50 (n/a)</td><td>207.70 (n/a)</td><td>707.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>690.90 (n/a)</td><td>411.62 (n/a)</td><td>336.90 (n/a)</td><td>268.30 (n/a)</td><td>173.82 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>721.40 (n/a)</td><td>476.80 (n/a)</td><td>503.50 (n/a)</td><td>242.60 (n/a)</td><td>184.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>588.10 (n/a)</td><td>392.58 (n/a)</td><td>443.30 (n/a)</td><td>196.00 (n/a)</td><td>172.41 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.70 (n/a)</td><td>438.72 (n/a)</td><td>451.00 (n/a)</td><td>232.40 (n/a)</td><td>131.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1813.10 (n/a)</td><td>725.44 (n/a)</td><td>507.10 (n/a)</td><td>229.70 (n/a)</td><td>623.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>543.60 (n/a)</td><td>426.14 (n/a)</td><td>468.00 (n/a)</td><td>240.70 (n/a)</td><td>126.74 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>701.90 (n/a)</td><td>480.34 (n/a)</td><td>582.80 (n/a)</td><td>256.20 (n/a)</td><td>204.31 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1020.90 (n/a)</td><td>573.04 (n/a)</td><td>641.80 (n/a)</td><td>269.20 (n/a)</td><td>315.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>554.60 (n/a)</td><td>472.98 (n/a)</td><td>516.30 (n/a)</td><td>269.10 (n/a)</td><td>117.53 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>610.20 (n/a)</td><td>434.84 (n/a)</td><td>461.60 (n/a)</td><td>242.20 (n/a)</td><td>149.25 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>615.30 (n/a)</td><td>479.94 (n/a)</td><td>455.00 (n/a)</td><td>346.50 (n/a)</td><td>118.95 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.62 (+17.08%)</td><td>0.45 <b>(+23.47%)</b></td><td>0.42 (+18.53%)</td><td>0.35 <b>(+59.66%)</b></td><td>0.11 (-5.74%)</td><td>633.70 <b>(-37.37%)</b></td><td>513.32 <b>(-22.30%)</b></td><td>520.80 (-15.63%)</td><td>356.00 (-14.61%)</td><td>104.76 <b>(-51.81%)</b></td><td>26.51 (+17.08%)</td><td>19.11 <b>(+23.47%)</b></td><td>18.12 (+18.53%)</td><td>14.89 <b>(+59.66%)</b></td><td>4.49 (-5.74%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.53 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>1011.80 (n/a)</td><td>660.64 (n/a)</td><td>617.30 (n/a)</td><td>416.90 (n/a)</td><td>217.41 (n/a)</td><td>22.64 (n/a)</td><td>15.47 (n/a)</td><td>15.29 (n/a)</td><td>9.33 (n/a)</td><td>4.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.79 <b>(+51.86%)</b></td><td>0.56 <b>(+28.43%)</b></td><td>0.57 <b>(+30.01%)</b></td><td>0.38 (+4.29%)</td><td>0.15 <b>(+149.23%)</b></td><td>579.90 (-4.12%)</td><td>415.80 (-18.82%)</td><td>388.20 <b>(-23.08%)</b></td><td>278.60 <b>(-34.14%)</b></td><td>110.63 <b>(+56.91%)</b></td><td>33.88 <b>(+51.86%)</b></td><td>24.03 <b>(+28.43%)</b></td><td>24.31 <b>(+30.01%)</b></td><td>16.27 (+4.29%)</td><td>6.47 <b>(+149.23%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.37 (n/a)</td><td>0.06 (n/a)</td><td>604.80 (n/a)</td><td>512.20 (n/a)</td><td>504.70 (n/a)</td><td>423.00 (n/a)</td><td>70.51 (n/a)</td><td>22.31 (n/a)</td><td>18.71 (n/a)</td><td>18.70 (n/a)</td><td>15.60 (n/a)</td><td>2.60 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.31 (-1.30%)</td><td>0.30 (-2.51%)</td><td>0.30 (-2.31%)</td><td>0.29 (-2.74%)</td><td>0.01 <b>(+43.22%)</b></td><td>86261.50 (+2.82%)</td><td>84211.84 (+2.59%)</td><td>83746.20 (+2.36%)</td><td>82343.10 (+1.32%)</td><td>1546.82 <b>(+48.97%)</b></td><td>208.64 (-1.30%)</td><td>204.06 (-2.51%)</td><td>205.14 (-2.31%)</td><td>199.16 (-2.74%)</td><td>3.74 <b>(+43.22%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83898.60 (n/a)</td><td>82088.62 (n/a)</td><td>81814.00 (n/a)</td><td>81272.20 (n/a)</td><td>1038.36 (n/a)</td><td>211.39 (n/a)</td><td>209.31 (n/a)</td><td>209.99 (n/a)</td><td>204.77 (n/a)</td><td>2.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>1.04 (+1.38%)</td><td>1.01 (-1.24%)</td><td>1.00 (-2.22%)</td><td>0.99 (-2.72%)</td><td>0.02 <b>(+338.58%)</b></td><td>25542.70 (+2.80%)</td><td>24934.98 (+1.30%)</td><td>25139.70 (+2.27%)</td><td>24152.20 (-1.36%)</td><td>607.91 <b>(+344.17%)</b></td><td>711.32 (+1.38%)</td><td>689.32 (-1.24%)</td><td>683.38 (-2.22%)</td><td>672.59 (-2.72%)</td><td>16.93 <b>(+338.60%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>0.01 (n/a)</td><td>24846.80 (n/a)</td><td>24615.70 (n/a)</td><td>24582.10 (n/a)</td><td>24484.50 (n/a)</td><td>136.87 (n/a)</td><td>701.66 (n/a)</td><td>697.94 (n/a)</td><td>698.88 (n/a)</td><td>691.43 (n/a)</td><td>3.86 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.82 (-0.52%)</td><td>0.82 (+1.03%)</td><td>0.82 (+0.90%)</td><td>0.81 (+2.05%)</td><td>0.00 <b>(-65.87%)</b></td><td>93141.20 (-2.01%)</td><td>92467.24 (-1.04%)</td><td>92432.60 (-0.89%)</td><td>92008.00 (+0.52%)</td><td>439.56 <b>(-66.35%)</b></td><td>746.89 (-0.52%)</td><td>743.19 (+1.03%)</td><td>743.46 (+0.90%)</td><td>737.80 (+2.05%)</td><td>3.52 <b>(-65.87%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95047.90 (n/a)</td><td>93435.44 (n/a)</td><td>93262.20 (n/a)</td><td>91532.10 (n/a)</td><td>1306.39 (n/a)</td><td>750.77 (n/a)</td><td>735.59 (n/a)</td><td>736.84 (n/a)</td><td>723.00 (n/a)</td><td>10.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.78 (+0.07%)</td><td>0.76 (-0.09%)</td><td>0.77 (-0.01%)</td><td>0.75 (+0.12%)</td><td>0.01 (-1.68%)</td><td>101119.50 (-0.12%)</td><td>98948.36 (+0.09%)</td><td>98618.30 (+0.01%)</td><td>97201.90 (-0.07%)</td><td>1452.36 (-1.97%)</td><td>706.98 (+0.07%)</td><td>694.62 (-0.09%)</td><td>696.82 (-0.01%)</td><td>679.59 (+0.12%)</td><td>10.14 (-1.68%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101239.50 (n/a)</td><td>98855.00 (n/a)</td><td>98607.90 (n/a)</td><td>97270.00 (n/a)</td><td>1481.58 (n/a)</td><td>706.48 (n/a)</td><td>695.28 (n/a)</td><td>696.90 (n/a)</td><td>678.78 (n/a)</td><td>10.31 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.80 (-0.39%)</td><td>0.80 (+0.10%)</td><td>0.80 (+0.56%)</td><td>0.79 (+0.11%)</td><td>0.00 (-14.85%)</td><td>95429.40 (-0.11%)</td><td>94555.08 (-0.11%)</td><td>94247.20 (-0.56%)</td><td>94051.60 (+0.39%)</td><td>580.71 (-14.58%)</td><td>730.66 (-0.39%)</td><td>726.79 (+0.10%)</td><td>729.14 (+0.56%)</td><td>720.11 (+0.11%)</td><td>4.45 (-14.85%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95532.70 (n/a)</td><td>94654.94 (n/a)</td><td>94775.90 (n/a)</td><td>93685.70 (n/a)</td><td>679.85 (n/a)</td><td>733.51 (n/a)</td><td>726.03 (n/a)</td><td>725.07 (n/a)</td><td>719.33 (n/a)</td><td>5.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>5.60 (-0.88%)</td><td>5.37 (+16.19%)</td><td>5.28 (+0.81%)</td><td>5.19 <b>(+98.98%)</b></td><td>0.19 <b>(-84.90%)</b></td><td>1716.00 <b>(-49.74%)</b></td><td>1661.56 <b>(-20.79%)</b></td><td>1689.20 (-0.80%)</td><td>1592.00 (+0.89%)</td><td>59.23 <b>(-92.35%)</b></td><td>337.24 (-0.88%)</td><td>323.45 (+16.19%)</td><td>317.82 (+0.81%)</td><td>312.87 <b>(+98.98%)</b></td><td>11.66 <b>(-84.90%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>5.65 (n/a)</td><td>4.62 (n/a)</td><td>5.23 (n/a)</td><td>2.61 (n/a)</td><td>1.28 (n/a)</td><td>3414.40 (n/a)</td><td>2097.56 (n/a)</td><td>1702.80 (n/a)</td><td>1577.90 (n/a)</td><td>774.73 (n/a)</td><td>340.25 (n/a)</td><td>278.37 (n/a)</td><td>315.28 (n/a)</td><td>157.24 (n/a)</td><td>77.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>4.87 <b>(+62.58%)</b></td><td>3.44 <b>(+41.36%)</b></td><td>2.87 <b>(+27.01%)</b></td><td>2.16 (+1.87%)</td><td>1.19 <b>(+228.10%)</b></td><td>4122.50 (-1.84%)</td><td>2847.28 <b>(-23.43%)</b></td><td>3108.80 <b>(-21.27%)</b></td><td>1829.20 <b>(-38.49%)</b></td><td>955.80 <b>(+87.91%)</b></td><td>293.51 <b>(+62.58%)</b></td><td>207.46 <b>(+41.36%)</b></td><td>172.69 <b>(+27.01%)</b></td><td>130.23 (+1.87%)</td><td>71.82 <b>(+228.11%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.00 (n/a)</td><td>2.44 (n/a)</td><td>2.26 (n/a)</td><td>2.12 (n/a)</td><td>0.36 (n/a)</td><td>4199.60 (n/a)</td><td>3718.64 (n/a)</td><td>3948.60 (n/a)</td><td>2973.80 (n/a)</td><td>508.64 (n/a)</td><td>180.54 (n/a)</td><td>146.76 (n/a)</td><td>135.96 (n/a)</td><td>127.84 (n/a)</td><td>21.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>5.19 (-0.82%)</td><td>4.10 (+0.74%)</td><td>4.12 (-3.14%)</td><td>3.09 <b>(+41.57%)</b></td><td>0.75 <b>(-41.41%)</b></td><td>2887.60 <b>(-29.37%)</b></td><td>2231.14 (-8.07%)</td><td>2165.30 (+3.24%)</td><td>1717.40 (+0.83%)</td><td>419.78 <b>(-57.50%)</b></td><td>312.61 (-0.82%)</td><td>247.26 (+0.74%)</td><td>247.94 (-3.14%)</td><td>185.92 <b>(+41.57%)</b></td><td>44.94 <b>(-41.41%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>5.23 (n/a)</td><td>4.07 (n/a)</td><td>4.25 (n/a)</td><td>2.18 (n/a)</td><td>1.27 (n/a)</td><td>4088.20 (n/a)</td><td>2427.02 (n/a)</td><td>2097.40 (n/a)</td><td>1703.30 (n/a)</td><td>987.65 (n/a)</td><td>315.20 (n/a)</td><td>245.43 (n/a)</td><td>255.97 (n/a)</td><td>131.32 (n/a)</td><td>76.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>6.73 (+1.09%)</td><td>5.48 (-3.53%)</td><td>5.69 (+0.48%)</td><td>4.14 (-11.81%)</td><td>0.99 (+13.57%)</td><td>8411.40 (+13.39%)</td><td>6543.46 (+4.55%)</td><td>6130.50 (-0.48%)</td><td>5179.50 (-1.08%)</td><td>1246.89 <b>(+29.39%)</b></td><td>414.61 (+1.09%)</td><td>337.33 (-3.53%)</td><td>350.29 (+0.48%)</td><td>255.31 (-11.81%)</td><td>60.68 (+13.57%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>6.66 (n/a)</td><td>5.68 (n/a)</td><td>5.66 (n/a)</td><td>4.70 (n/a)</td><td>0.87 (n/a)</td><td>7417.90 (n/a)</td><td>6258.50 (n/a)</td><td>6160.20 (n/a)</td><td>5235.80 (n/a)</td><td>963.67 (n/a)</td><td>410.16 (n/a)</td><td>349.69 (n/a)</td><td>348.60 (n/a)</td><td>289.50 (n/a)</td><td>53.43 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>5.72 (+3.90%)</td><td>5.12 (+8.74%)</td><td>5.16 (+7.41%)</td><td>4.13 (+11.19%)</td><td>0.60 (-6.11%)</td><td>8446.70 (-10.06%)</td><td>6889.94 (-8.39%)</td><td>6753.20 (-6.89%)</td><td>6096.10 (-3.75%)</td><td>914.24 (-19.09%)</td><td>352.27 (+3.90%)</td><td>315.62 (+8.74%)</td><td>318.00 (+7.41%)</td><td>254.24 (+11.19%)</td><td>37.26 (-6.11%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>5.50 (n/a)</td><td>4.71 (n/a)</td><td>4.81 (n/a)</td><td>3.71 (n/a)</td><td>0.64 (n/a)</td><td>9392.00 (n/a)</td><td>7521.20 (n/a)</td><td>7253.30 (n/a)</td><td>6333.70 (n/a)</td><td>1129.97 (n/a)</td><td>339.06 (n/a)</td><td>290.25 (n/a)</td><td>296.07 (n/a)</td><td>228.65 (n/a)</td><td>39.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>6.68 (+4.31%)</td><td>5.93 (+5.76%)</td><td>6.16 (+12.28%)</td><td>4.95 (-0.78%)</td><td>0.80 <b>(+33.23%)</b></td><td>7038.10 (+0.78%)</td><td>5972.56 (-4.86%)</td><td>5658.50 (-10.93%)</td><td>5221.60 (-4.13%)</td><td>839.53 <b>(+27.44%)</b></td><td>411.27 (+4.31%)</td><td>365.10 (+5.76%)</td><td>379.51 (+12.28%)</td><td>305.12 (-0.78%)</td><td>49.37 <b>(+33.23%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>6.40 (n/a)</td><td>5.60 (n/a)</td><td>5.49 (n/a)</td><td>4.99 (n/a)</td><td>0.60 (n/a)</td><td>6983.30 (n/a)</td><td>6277.38 (n/a)</td><td>6353.10 (n/a)</td><td>5446.50 (n/a)</td><td>658.79 (n/a)</td><td>394.29 (n/a)</td><td>345.20 (n/a)</td><td>338.02 (n/a)</td><td>307.52 (n/a)</td><td>37.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.78 (-0.16%)</td><td>0.77 (+1.29%)</td><td>0.76 (+0.80%)</td><td>0.76 (+3.24%)</td><td>0.01 <b>(-58.20%)</b></td><td>99219.10 (-3.14%)</td><td>98240.20 (-1.32%)</td><td>98692.10 (-0.80%)</td><td>96776.90 (+0.16%)</td><td>1058.96 <b>(-59.47%)</b></td><td>710.08 (-0.16%)</td><td>699.57 (+1.29%)</td><td>696.30 (+0.80%)</td><td>692.60 (+3.24%)</td><td>7.58 <b>(-58.20%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>102430.80 (n/a)</td><td>99557.80 (n/a)</td><td>99485.80 (n/a)</td><td>96620.40 (n/a)</td><td>2612.52 (n/a)</td><td>711.23 (n/a)</td><td>690.63 (n/a)</td><td>690.75 (n/a)</td><td>670.89 (n/a)</td><td>18.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.76 (-1.00%)</td><td>0.75 (-1.04%)</td><td>0.75 (-1.14%)</td><td>0.73 (-0.38%)</td><td>0.01 (-15.82%)</td><td>103556.90 (+0.38%)</td><td>100916.64 (+1.04%)</td><td>100825.60 (+1.16%)</td><td>98921.50 (+1.01%)</td><td>1726.81 (-14.70%)</td><td>694.69 (-1.00%)</td><td>681.11 (-1.04%)</td><td>681.57 (-1.14%)</td><td>663.59 (-0.38%)</td><td>11.57 (-15.82%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103161.50 (n/a)</td><td>99874.76 (n/a)</td><td>99671.90 (n/a)</td><td>97928.30 (n/a)</td><td>2024.40 (n/a)</td><td>701.73 (n/a)</td><td>688.28 (n/a)</td><td>689.46 (n/a)</td><td>666.13 (n/a)</td><td>13.74 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.81 (+0.09%)</td><td>0.80 (-0.47%)</td><td>0.80 (-0.82%)</td><td>0.80 (+0.21%)</td><td>0.00 (-8.85%)</td><td>94785.50 (-0.21%)</td><td>94368.88 (+0.48%)</td><td>94530.80 (+0.83%)</td><td>93409.70 (-0.09%)</td><td>555.46 (-9.28%)</td><td>735.68 (+0.09%)</td><td>728.22 (-0.47%)</td><td>726.95 (-0.82%)</td><td>725.00 (+0.21%)</td><td>4.31 (-8.85%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>94988.90 (n/a)</td><td>93921.86 (n/a)</td><td>93754.40 (n/a)</td><td>93494.00 (n/a)</td><td>612.31 (n/a)</td><td>735.01 (n/a)</td><td>731.69 (n/a)</td><td>732.97 (n/a)</td><td>723.45 (n/a)</td><td>4.73 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.80 (-3.68%)</td><td>2.59 (+18.00%)</td><td>2.71 <b>(+45.23%)</b></td><td>1.63 <b>(+57.10%)</b></td><td>0.82 <b>(-27.45%)</b></td><td>4953.30 <b>(-36.35%)</b></td><td>3374.34 <b>(-24.99%)</b></td><td>2978.60 <b>(-31.14%)</b></td><td>2118.60 (+3.82%)</td><td>1076.91 <b>(-50.93%)</b></td><td>997.81 (-3.68%)</td><td>679.23 (+18.00%)</td><td>709.71 <b>(+45.23%)</b></td><td>426.78 <b>(+57.10%)</b></td><td>214.97 <b>(-27.45%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.95 (n/a)</td><td>2.19 (n/a)</td><td>1.86 (n/a)</td><td>1.04 (n/a)</td><td>1.13 (n/a)</td><td>7781.80 (n/a)</td><td>4498.24 (n/a)</td><td>4325.90 (n/a)</td><td>2040.70 (n/a)</td><td>2194.50 (n/a)</td><td>1035.89 (n/a)</td><td>575.62 (n/a)</td><td>488.67 (n/a)</td><td>271.65 (n/a)</td><td>296.30 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.30 (+3.49%)</td><td>0.22 (+5.32%)</td><td>0.21 (+5.00%)</td><td>0.18 (+16.64%)</td><td>0.05 (-9.36%)</td><td>6961.40 (-14.26%)</td><td>5702.46 (-6.37%)</td><td>5821.30 (-4.76%)</td><td>4129.50 (-3.37%)</td><td>1014.76 <b>(-27.04%)</b></td><td>16.25 (+3.49%)</td><td>12.11 (+5.32%)</td><td>11.53 (+5.00%)</td><td>9.64 (+16.64%)</td><td>2.46 (-9.36%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>8119.50 (n/a)</td><td>6090.20 (n/a)</td><td>6112.20 (n/a)</td><td>4273.50 (n/a)</td><td>1390.77 (n/a)</td><td>15.70 (n/a)</td><td>11.50 (n/a)</td><td>10.98 (n/a)</td><td>8.27 (n/a)</td><td>2.72 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (-8.45%)</td><td>0.09 (-15.07%)</td><td>0.11 (-1.26%)</td><td>0.02 <b>(-72.54%)</b></td><td>0.05 <b>(+54.73%)</b></td><td>0.13 (-8.45%)</td><td>0.09 (-15.07%)</td><td>0.11 (-1.26%)</td><td>0.02 <b>(-72.54%)</b></td><td>0.05 <b>(+54.73%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.96 (+4.82%)</td><td>3.61 (-0.35%)</td><td>3.75 (+2.40%)</td><td>3.05 (-10.52%)</td><td>0.36 <b>(+133.90%)</b></td><td>3.95 (+4.82%)</td><td>3.61 (-0.35%)</td><td>3.74 (+2.40%)</td><td>3.05 (-10.52%)</td><td>0.36 <b>(+133.90%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.77 (n/a)</td><td>3.62 (n/a)</td><td>3.66 (n/a)</td><td>3.41 (n/a)</td><td>0.15 (n/a)</td><td>3.77 (n/a)</td><td>3.62 (n/a)</td><td>3.66 (n/a)</td><td>3.41 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>7.34 (-0.62%)</td><td>6.25 (+2.22%)</td><td>5.75 (+1.46%)</td><td>5.44 (+1.86%)</td><td>0.91 (+4.39%)</td><td>7.34 (-0.62%)</td><td>6.24 (+2.22%)</td><td>5.75 (+1.46%)</td><td>5.44 (+1.86%)</td><td>0.91 (+4.39%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>7.39 (n/a)</td><td>6.11 (n/a)</td><td>5.67 (n/a)</td><td>5.34 (n/a)</td><td>0.87 (n/a)</td><td>7.38 (n/a)</td><td>6.11 (n/a)</td><td>5.67 (n/a)</td><td>5.34 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>13.97 <b>(+65.28%)</b></td><td>9.54 <b>(+20.28%)</b></td><td>8.62 (+8.01%)</td><td>7.45 (+0.48%)</td><td>2.56 <b>(+468.64%)</b></td><td>13.96 <b>(+65.28%)</b></td><td>9.53 <b>(+20.28%)</b></td><td>8.61 (+8.01%)</td><td>7.45 (+0.48%)</td><td>2.56 <b>(+468.64%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>8.45 (n/a)</td><td>7.93 (n/a)</td><td>7.98 (n/a)</td><td>7.42 (n/a)</td><td>0.45 (n/a)</td><td>8.45 (n/a)</td><td>7.92 (n/a)</td><td>7.97 (n/a)</td><td>7.41 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.82 (-1.63%)</td><td>3.62 (+3.32%)</td><td>3.60 (-1.28%)</td><td>3.50 (+14.29%)</td><td>0.12 <b>(-66.37%)</b></td><td>3.82 (-1.63%)</td><td>3.62 (+3.32%)</td><td>3.60 (-1.28%)</td><td>3.50 (+14.29%)</td><td>0.12 <b>(-66.37%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.88 (n/a)</td><td>3.51 (n/a)</td><td>3.65 (n/a)</td><td>3.06 (n/a)</td><td>0.36 (n/a)</td><td>3.88 (n/a)</td><td>3.51 (n/a)</td><td>3.65 (n/a)</td><td>3.06 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>6.63 (-4.52%)</td><td>6.10 (-0.35%)</td><td>6.07 (+5.71%)</td><td>5.76 (+2.99%)</td><td>0.35 <b>(-45.10%)</b></td><td>6.62 (-4.52%)</td><td>6.09 (-0.35%)</td><td>6.07 (+5.71%)</td><td>5.76 (+2.99%)</td><td>0.35 <b>(-45.10%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>6.94 (n/a)</td><td>6.12 (n/a)</td><td>5.74 (n/a)</td><td>5.59 (n/a)</td><td>0.64 (n/a)</td><td>6.94 (n/a)</td><td>6.11 (n/a)</td><td>5.74 (n/a)</td><td>5.59 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>11.90 (-17.86%)</td><td>9.15 (-3.15%)</td><td>8.17 (-2.69%)</td><td>7.33 (-0.18%)</td><td>1.90 <b>(-33.93%)</b></td><td>11.89 (-17.86%)</td><td>9.14 (-3.15%)</td><td>8.16 (-2.69%)</td><td>7.32 (-0.18%)</td><td>1.90 <b>(-33.93%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>14.49 (n/a)</td><td>9.45 (n/a)</td><td>8.39 (n/a)</td><td>7.34 (n/a)</td><td>2.88 (n/a)</td><td>14.48 (n/a)</td><td>9.44 (n/a)</td><td>8.39 (n/a)</td><td>7.34 (n/a)</td><td>2.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.13 <b>(+82.92%)</b></td><td>2.16 <b>(+59.70%)</b></td><td>2.66 <b>(+127.17%)</b></td><td>1.06 (+0.40%)</td><td>1.01 <b>(+223.12%)</b></td><td>3.12 <b>(+82.92%)</b></td><td>2.16 <b>(+59.70%)</b></td><td>2.65 <b>(+127.17%)</b></td><td>1.06 (+0.40%)</td><td>1.00 <b>(+223.12%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>1.71 (n/a)</td><td>1.35 (n/a)</td><td>1.17 (n/a)</td><td>1.05 (n/a)</td><td>0.31 (n/a)</td><td>1.71 (n/a)</td><td>1.35 (n/a)</td><td>1.17 (n/a)</td><td>1.05 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.54 (+15.90%)</td><td>0.39 <b>(+21.44%)</b></td><td>0.49 <b>(+51.69%)</b></td><td>0.08 (-3.30%)</td><td>0.19 <b>(+22.38%)</b></td><td>0.53 (+15.90%)</td><td>0.39 <b>(+21.44%)</b></td><td>0.49 <b>(+51.69%)</b></td><td>0.07 (-3.30%)</td><td>0.19 <b>(+22.38%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.16 (n/a)</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.61 (-3.84%)</td><td>0.44 (+6.62%)</td><td>0.42 (+16.38%)</td><td>0.24 (-10.31%)</td><td>0.16 (+12.26%)</td><td>0.60 (-3.84%)</td><td>0.44 (+6.62%)</td><td>0.41 (+16.38%)</td><td>0.24 (-10.31%)</td><td>0.15 (+12.26%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.63 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.14 (n/a)</td><td>0.63 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>2.61 (+13.99%)</td><td>1.27 (-14.54%)</td><td>0.46 <b>(-65.66%)</b></td><td>0.44 <b>(-42.54%)</b></td><td>1.13 <b>(+93.12%)</b></td><td>2.57 (+13.99%)</td><td>1.25 (-14.54%)</td><td>0.45 <b>(-65.66%)</b></td><td>0.43 <b>(-42.54%)</b></td><td>1.11 <b>(+93.12%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>2.29 (n/a)</td><td>1.49 (n/a)</td><td>1.34 (n/a)</td><td>0.76 (n/a)</td><td>0.59 (n/a)</td><td>2.26 (n/a)</td><td>1.47 (n/a)</td><td>1.32 (n/a)</td><td>0.75 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>443.20 (n/a)</td><td>371.46 (n/a)</td><td>437.60 (n/a)</td><td>235.00 (n/a)</td><td>98.25 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1851.40 (n/a)</td><td>598.42 (n/a)</td><td>298.20 (n/a)</td><td>209.20 (n/a)</td><td>703.43 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>812.20 (n/a)</td><td>494.06 (n/a)</td><td>424.10 (n/a)</td><td>317.20 (n/a)</td><td>191.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.00 (n/a)</td><td>461.88 (n/a)</td><td>485.00 (n/a)</td><td>266.30 (n/a)</td><td>118.26 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.60 (n/a)</td><td>356.70 (n/a)</td><td>269.10 (n/a)</td><td>197.90 (n/a)</td><td>168.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>661.10 (n/a)</td><td>412.98 (n/a)</td><td>375.40 (n/a)</td><td>253.70 (n/a)</td><td>171.11 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.30 (n/a)</td><td>307.92 (n/a)</td><td>240.40 (n/a)</td><td>171.80 (n/a)</td><td>188.69 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1936.70 (n/a)</td><td>632.34 (n/a)</td><td>272.90 (n/a)</td><td>189.00 (n/a)</td><td>745.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>451.70 (n/a)</td><td>293.24 (n/a)</td><td>227.70 (n/a)</td><td>192.70 (n/a)</td><td>122.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>994.20 (n/a)</td><td>487.26 (n/a)</td><td>425.80 (n/a)</td><td>233.80 (n/a)</td><td>304.26 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.60 (n/a)</td><td>525.40 (n/a)</td><td>555.70 (n/a)</td><td>436.30 (n/a)</td><td>59.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.50 (n/a)</td><td>450.30 (n/a)</td><td>440.40 (n/a)</td><td>341.40 (n/a)</td><td>99.38 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>650.40 (n/a)</td><td>495.98 (n/a)</td><td>490.20 (n/a)</td><td>285.50 (n/a)</td><td>148.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>637.70 (n/a)</td><td>465.16 (n/a)</td><td>489.30 (n/a)</td><td>270.40 (n/a)</td><td>135.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>652.90 (n/a)</td><td>387.14 (n/a)</td><td>290.80 (n/a)</td><td>248.70 (n/a)</td><td>178.25 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>646.30 (n/a)</td><td>397.14 (n/a)</td><td>298.60 (n/a)</td><td>260.90 (n/a)</td><td>166.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>614.10 (n/a)</td><td>492.30 (n/a)</td><td>475.40 (n/a)</td><td>407.90 (n/a)</td><td>75.10 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>564.50 (n/a)</td><td>438.36 (n/a)</td><td>469.00 (n/a)</td><td>238.10 (n/a)</td><td>134.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 <b>(+32.26%)</b></td><td>0.09 <b>(+38.95%)</b></td><td>0.11 <b>(+72.03%)</b></td><td>0.06 (+10.32%)</td><td>0.03 <b>(+110.24%)</b></td><td>519.80 (-9.36%)</td><td>382.22 <b>(-23.99%)</b></td><td>310.20 <b>(-41.88%)</b></td><td>277.30 <b>(-24.38%)</b></td><td>124.94 <b>(+52.40%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>573.50 (n/a)</td><td>502.84 (n/a)</td><td>533.70 (n/a)</td><td>366.70 (n/a)</td><td>81.98 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>624.90 (n/a)</td><td>476.78 (n/a)</td><td>461.60 (n/a)</td><td>267.10 (n/a)</td><td>138.91 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1912.10 (n/a)</td><td>749.48 (n/a)</td><td>517.70 (n/a)</td><td>303.20 (n/a)</td><td>670.19 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>511.20 (n/a)</td><td>356.48 (n/a)</td><td>304.80 (n/a)</td><td>207.80 (n/a)</td><td>136.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1959.20 (n/a)</td><td>663.92 (n/a)</td><td>369.60 (n/a)</td><td>268.20 (n/a)</td><td>725.43 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>824.80 (n/a)</td><td>529.26 (n/a)</td><td>492.80 (n/a)</td><td>350.60 (n/a)</td><td>180.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (+6.18%)</td><td>0.01 (+7.70%)</td><td>0.01 <b>(+43.16%)</b></td><td>0.01 (-8.30%)</td><td>0.00 <b>(+20.57%)</b></td><td>530.60 (+9.06%)</td><td>369.50 (-2.80%)</td><td>294.40 <b>(-30.15%)</b></td><td>212.50 (-5.81%)</td><td>144.48 <b>(+35.39%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>486.50 (n/a)</td><td>380.14 (n/a)</td><td>421.50 (n/a)</td><td>225.60 (n/a)</td><td>106.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (+3.56%)</td><td>0.01 (+9.69%)</td><td>0.01 (+7.41%)</td><td>0.01 <b>(+21.56%)</b></td><td>0.00 (-4.25%)</td><td>483.00 (-17.75%)</td><td>382.28 (-11.71%)</td><td>452.50 (-6.89%)</td><td>221.90 (-3.44%)</td><td>122.98 <b>(-22.54%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.20 (n/a)</td><td>432.98 (n/a)</td><td>486.00 (n/a)</td><td>229.80 (n/a)</td><td>158.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 <b>(-36.40%)</b></td><td>0.01 <b>(-32.58%)</b></td><td>0.01 <b>(-25.41%)</b></td><td>0.00 <b>(-43.81%)</b></td><td>0.00 (-15.75%)</td><td>962.10 <b>(+77.97%)</b></td><td>493.70 <b>(+63.54%)</b></td><td>347.40 <b>(+34.08%)</b></td><td>276.40 <b>(+57.22%)</b></td><td>294.16 <b>(+110.25%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>540.60 (n/a)</td><td>301.88 (n/a)</td><td>259.10 (n/a)</td><td>175.80 (n/a)</td><td>139.91 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (+4.70%)</td><td>0.01 (+8.43%)</td><td>0.01 (+11.42%)</td><td>0.01 <b>(-29.87%)</b></td><td>0.00 <b>(+49.62%)</b></td><td>812.10 <b>(+42.60%)</b></td><td>400.38 (+2.84%)</td><td>301.60 (-10.26%)</td><td>281.40 (-4.48%)</td><td>230.75 <b>(+107.59%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.50 (n/a)</td><td>389.34 (n/a)</td><td>336.10 (n/a)</td><td>294.60 (n/a)</td><td>111.16 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(-33.33%)</b></td><td>0.01 (-10.36%)</td><td>0.01 (-10.07%)</td><td>0.01 (+1.19%)</td><td>0.00 <b>(-48.42%)</b></td><td>528.90 (-1.18%)</td><td>403.00 (+3.23%)</td><td>443.70 (+11.20%)</td><td>269.20 <b>(+49.97%)</b></td><td>107.71 (-18.18%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>535.20 (n/a)</td><td>390.38 (n/a)</td><td>399.00 (n/a)</td><td>179.50 (n/a)</td><td>131.64 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (+9.20%)</td><td>0.01 <b>(+37.64%)</b></td><td>0.01 <b>(+84.64%)</b></td><td>0.00 <b>(-37.58%)</b></td><td>0.00 <b>(+33.31%)</b></td><td>1064.00 <b>(+60.19%)</b></td><td>451.08 (-14.12%)</td><td>325.10 <b>(-45.83%)</b></td><td>252.50 (-8.41%)</td><td>344.69 <b>(+111.82%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>664.20 (n/a)</td><td>525.22 (n/a)</td><td>600.20 (n/a)</td><td>275.70 (n/a)</td><td>162.73 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (+6.29%)</td><td>0.03 (+2.49%)</td><td>0.03 (-6.05%)</td><td>0.02 (+15.76%)</td><td>0.01 (-13.15%)</td><td>469.60 (-13.61%)</td><td>320.56 (-4.97%)</td><td>293.50 (+6.42%)</td><td>247.50 (-5.89%)</td><td>86.50 <b>(-26.96%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.60 (n/a)</td><td>337.34 (n/a)</td><td>275.80 (n/a)</td><td>263.00 (n/a)</td><td>118.43 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(+36.84%)</b></td><td>0.02 (+17.04%)</td><td>0.02 (+9.72%)</td><td>0.01 (-15.16%)</td><td>0.01 <b>(+193.95%)</b></td><td>638.50 (+17.87%)</td><td>441.68 (-4.50%)</td><td>429.50 (-8.87%)</td><td>271.70 <b>(-26.92%)</b></td><td>172.61 <b>(+144.19%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>541.70 (n/a)</td><td>462.48 (n/a)</td><td>471.30 (n/a)</td><td>371.80 (n/a)</td><td>70.69 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (+6.95%)</td><td>0.02 (-10.10%)</td><td>0.02 <b>(-32.93%)</b></td><td>0.01 (-15.96%)</td><td>0.01 <b>(+36.97%)</b></td><td>582.00 (+18.99%)</td><td>419.66 (+18.88%)</td><td>456.40 <b>(+49.10%)</b></td><td>235.10 (-6.52%)</td><td>158.30 <b>(+50.11%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>489.10 (n/a)</td><td>353.02 (n/a)</td><td>306.10 (n/a)</td><td>251.50 (n/a)</td><td>105.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (+7.63%)</td><td>0.02 (-11.64%)</td><td>0.02 <b>(-27.69%)</b></td><td>0.01 <b>(-28.56%)</b></td><td>0.01 <b>(+39.35%)</b></td><td>561.10 <b>(+39.96%)</b></td><td>373.92 (+18.67%)</td><td>383.00 <b>(+38.32%)</b></td><td>233.90 (-7.11%)</td><td>121.97 <b>(+78.51%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>400.90 (n/a)</td><td>315.08 (n/a)</td><td>276.90 (n/a)</td><td>251.80 (n/a)</td><td>68.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 <b>(+22.52%)</b></td><td>0.03 <b>(+38.49%)</b></td><td>0.03 <b>(+65.55%)</b></td><td>0.02 (+16.30%)</td><td>0.01 (+13.46%)</td><td>517.90 (-14.01%)</td><td>314.06 <b>(-28.11%)</b></td><td>290.90 <b>(-39.58%)</b></td><td>230.10 (-18.38%)</td><td>118.19 (-15.33%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.30 (n/a)</td><td>436.88 (n/a)</td><td>481.50 (n/a)</td><td>281.90 (n/a)</td><td>139.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (-7.15%)</td><td>0.02 (-12.54%)</td><td>0.02 <b>(+22.57%)</b></td><td>0.00 <b>(-69.31%)</b></td><td>0.01 (+5.29%)</td><td>2080.00 <b>(+225.87%)</b></td><td>716.52 <b>(+66.53%)</b></td><td>397.40 (-18.43%)</td><td>233.00 (+7.72%)</td><td>768.15 <b>(+335.87%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.30 (n/a)</td><td>430.26 (n/a)</td><td>487.20 (n/a)</td><td>216.30 (n/a)</td><td>176.23 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(-22.00%)</b></td><td>0.02 (+19.63%)</td><td>0.03 <b>(+50.73%)</b></td><td>0.00 (-1.82%)</td><td>0.01 (-19.74%)</td><td>2039.00 (+1.85%)</td><td>646.38 (-12.78%)</td><td>315.70 <b>(-33.66%)</b></td><td>258.50 <b>(+28.22%)</b></td><td>778.94 (+7.83%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2001.90 (n/a)</td><td>741.12 (n/a)</td><td>475.90 (n/a)</td><td>201.60 (n/a)</td><td>722.35 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (+4.06%)</td><td>0.02 (+12.36%)</td><td>0.02 <b>(+35.78%)</b></td><td>0.01 (+5.08%)</td><td>0.01 (-11.82%)</td><td>636.50 (-4.83%)</td><td>437.36 (-12.83%)</td><td>404.70 <b>(-26.34%)</b></td><td>321.90 (-3.88%)</td><td>126.26 (-16.00%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>668.80 (n/a)</td><td>501.76 (n/a)</td><td>549.40 (n/a)</td><td>334.90 (n/a)</td><td>150.32 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (+17.94%)</td><td>0.05 (+18.98%)</td><td>0.06 <b>(+59.73%)</b></td><td>0.01 <b>(-76.81%)</b></td><td>0.02 <b>(+79.79%)</b></td><td>2496.80 <b>(+331.30%)</b></td><td>722.90 <b>(+66.02%)</b></td><td>296.60 <b>(-37.40%)</b></td><td>239.80 (-15.21%)</td><td>991.93 <b>(+653.94%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>578.90 (n/a)</td><td>435.42 (n/a)</td><td>473.80 (n/a)</td><td>282.80 (n/a)</td><td>131.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 <b>(-30.01%)</b></td><td>0.03 <b>(-20.08%)</b></td><td>0.04 (+4.66%)</td><td>0.03 (-16.49%)</td><td>0.01 <b>(-58.47%)</b></td><td>599.50 (+19.73%)</td><td>482.02 (+19.29%)</td><td>453.30 (-4.45%)</td><td>390.50 <b>(+42.88%)</b></td><td>79.04 <b>(-28.25%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>500.70 (n/a)</td><td>404.06 (n/a)</td><td>474.40 (n/a)</td><td>273.30 (n/a)</td><td>110.17 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 <b>(-29.01%)</b></td><td>0.03 <b>(-20.90%)</b></td><td>0.04 (-9.42%)</td><td>0.01 (+7.82%)</td><td>0.01 <b>(-39.79%)</b></td><td>1956.10 (-7.25%)</td><td>753.54 (+2.65%)</td><td>466.70 (+10.41%)</td><td>346.50 <b>(+40.85%)</b></td><td>676.20 (-13.56%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2109.10 (n/a)</td><td>734.10 (n/a)</td><td>422.70 (n/a)</td><td>246.00 (n/a)</td><td>782.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 <b>(+23.35%)</b></td><td>0.05 <b>(+26.14%)</b></td><td>0.05 <b>(+49.66%)</b></td><td>0.03 <b>(+20.21%)</b></td><td>0.01 <b>(+29.49%)</b></td><td>491.60 (-16.80%)</td><td>344.64 (-19.90%)</td><td>303.30 <b>(-33.18%)</b></td><td>234.10 (-18.94%)</td><td>105.15 (-9.58%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>590.90 (n/a)</td><td>430.24 (n/a)</td><td>453.90 (n/a)</td><td>288.80 (n/a)</td><td>116.29 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (-3.33%)</td><td>0.04 (-14.59%)</td><td>0.04 <b>(-36.88%)</b></td><td>0.03 (+13.26%)</td><td>0.01 (+0.83%)</td><td>524.00 (-11.71%)</td><td>415.18 (+16.23%)</td><td>466.80 <b>(+58.40%)</b></td><td>269.30 (+3.42%)</td><td>121.68 (-10.71%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>593.50 (n/a)</td><td>357.22 (n/a)</td><td>294.70 (n/a)</td><td>260.40 (n/a)</td><td>136.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 <b>(+76.99%)</b></td><td>0.04 <b>(+20.87%)</b></td><td>0.03 (-2.19%)</td><td>0.02 <b>(-25.61%)</b></td><td>0.02 <b>(+206.37%)</b></td><td>852.10 <b>(+34.42%)</b></td><td>507.64 (+0.17%)</td><td>537.80 (+2.24%)</td><td>213.50 <b>(-43.50%)</b></td><td>248.45 <b>(+128.19%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>633.90 (n/a)</td><td>506.78 (n/a)</td><td>526.00 (n/a)</td><td>377.90 (n/a)</td><td>108.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.13 <b>(+25.24%)</b></td><td>0.09 <b>(+50.33%)</b></td><td>0.09 <b>(+49.13%)</b></td><td>0.05 <b>(+196.74%)</b></td><td>0.03 (+3.03%)</td><td>647.80 <b>(-66.30%)</b></td><td>410.84 <b>(-47.71%)</b></td><td>383.10 <b>(-32.95%)</b></td><td>247.10 <b>(-20.16%)</b></td><td>158.87 <b>(-75.40%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1922.30 (n/a)</td><td>785.64 (n/a)</td><td>571.40 (n/a)</td><td>309.50 (n/a)</td><td>645.72 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (-3.80%)</td><td>0.08 (-6.57%)</td><td>0.07 (+7.83%)</td><td>0.02 <b>(-66.94%)</b></td><td>0.05 (+8.20%)</td><td>2012.50 <b>(+202.54%)</b></td><td>688.42 <b>(+55.84%)</b></td><td>456.40 (-7.25%)</td><td>235.90 (+3.97%)</td><td>748.70 <b>(+273.96%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>665.20 (n/a)</td><td>441.74 (n/a)</td><td>492.10 (n/a)</td><td>226.90 (n/a)</td><td>200.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 <b>(-32.18%)</b></td><td>0.08 <b>(-26.20%)</b></td><td>0.07 <b>(-42.30%)</b></td><td>0.06 (+4.01%)</td><td>0.03 <b>(-46.68%)</b></td><td>587.80 (-3.86%)</td><td>452.28 <b>(+20.38%)</b></td><td>483.00 <b>(+73.30%)</b></td><td>267.00 <b>(+47.43%)</b></td><td>132.07 <b>(-29.04%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>611.40 (n/a)</td><td>375.72 (n/a)</td><td>278.70 (n/a)</td><td>181.10 (n/a)</td><td>186.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 <b>(-32.91%)</b></td><td>0.09 (+5.20%)</td><td>0.08 <b>(+25.85%)</b></td><td>0.07 <b>(+199.39%)</b></td><td>0.02 <b>(-66.78%)</b></td><td>456.80 <b>(-66.60%)</b></td><td>389.38 <b>(-34.47%)</b></td><td>423.60 <b>(-20.54%)</b></td><td>285.60 <b>(+49.06%)</b></td><td>74.08 <b>(-83.75%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1367.80 (n/a)</td><td>594.18 (n/a)</td><td>533.10 (n/a)</td><td>191.60 (n/a)</td><td>455.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 <b>(-20.74%)</b></td><td>0.06 (-19.22%)</td><td>0.06 (-11.10%)</td><td>0.05 <b>(-20.01%)</b></td><td>0.01 <b>(-32.16%)</b></td><td>608.00 <b>(+25.03%)</b></td><td>517.02 <b>(+22.62%)</b></td><td>528.40 (+12.50%)</td><td>396.00 <b>(+26.15%)</b></td><td>83.52 (+4.07%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>486.30 (n/a)</td><td>421.64 (n/a)</td><td>469.70 (n/a)</td><td>313.90 (n/a)</td><td>80.25 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (+4.05%)</td><td>0.01 <b>(+24.17%)</b></td><td>0.01 <b>(+37.49%)</b></td><td>0.01 (+3.31%)</td><td>0.00 (-5.84%)</td><td>525.80 (-3.20%)</td><td>320.58 <b>(-20.55%)</b></td><td>290.80 <b>(-27.26%)</b></td><td>239.70 (-3.89%)</td><td>116.89 (-10.52%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.20 (n/a)</td><td>403.52 (n/a)</td><td>399.80 (n/a)</td><td>249.40 (n/a)</td><td>130.64 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (-12.54%)</td><td>0.01 (+11.27%)</td><td>0.02 (+14.68%)</td><td>0.01 (-0.30%)</td><td>0.00 <b>(-26.67%)</b></td><td>495.10 (+0.30%)</td><td>302.48 (-14.30%)</td><td>262.50 (-12.79%)</td><td>212.70 (+14.35%)</td><td>111.83 (-16.70%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>493.60 (n/a)</td><td>352.96 (n/a)</td><td>301.00 (n/a)</td><td>186.00 (n/a)</td><td>134.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (-3.52%)</td><td>0.01 (+15.32%)</td><td>0.02 <b>(+93.22%)</b></td><td>0.01 (-5.37%)</td><td>0.01 (+12.93%)</td><td>627.10 (+5.68%)</td><td>396.38 (-8.20%)</td><td>269.90 <b>(-48.24%)</b></td><td>234.60 (+3.62%)</td><td>204.58 <b>(+26.14%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>593.40 (n/a)</td><td>431.78 (n/a)</td><td>521.40 (n/a)</td><td>226.40 (n/a)</td><td>162.18 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(+55.96%)</b></td><td>0.01 (+17.83%)</td><td>0.01 <b>(-21.79%)</b></td><td>0.01 (+19.68%)</td><td>0.01 <b>(+97.52%)</b></td><td>484.20 (-16.45%)</td><td>353.20 (-6.44%)</td><td>418.50 <b>(+27.86%)</b></td><td>157.60 <b>(-35.88%)</b></td><td>146.96 (+8.57%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.50 (n/a)</td><td>377.52 (n/a)</td><td>327.30 (n/a)</td><td>245.80 (n/a)</td><td>135.36 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(+22.50%)</b></td><td>0.01 <b>(+29.96%)</b></td><td>0.02 <b>(+62.61%)</b></td><td>0.01 <b>(+30.16%)</b></td><td>0.00 <b>(+22.02%)</b></td><td>463.10 <b>(-23.18%)</b></td><td>318.34 <b>(-23.15%)</b></td><td>253.00 <b>(-38.52%)</b></td><td>232.80 (-18.37%)</td><td>106.15 <b>(-20.57%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.80 (n/a)</td><td>414.24 (n/a)</td><td>411.50 (n/a)</td><td>285.20 (n/a)</td><td>133.64 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (-12.83%)</td><td>0.01 (+13.53%)</td><td>0.01 <b>(+38.15%)</b></td><td>0.01 (+1.30%)</td><td>0.00 <b>(-23.39%)</b></td><td>484.70 (-1.28%)</td><td>300.86 (-14.30%)</td><td>274.40 <b>(-27.62%)</b></td><td>232.20 (+14.72%)</td><td>104.71 (-8.47%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.00 (n/a)</td><td>351.06 (n/a)</td><td>379.10 (n/a)</td><td>202.40 (n/a)</td><td>114.39 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (+9.66%)</td><td>0.01 <b>(+25.51%)</b></td><td>0.01 <b>(+45.15%)</b></td><td>0.01 (+5.63%)</td><td>0.00 (-1.14%)</td><td>541.00 (-5.32%)</td><td>386.62 <b>(-21.35%)</b></td><td>377.90 <b>(-31.12%)</b></td><td>247.20 (-8.82%)</td><td>108.98 (-13.06%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>571.40 (n/a)</td><td>491.58 (n/a)</td><td>548.60 (n/a)</td><td>271.10 (n/a)</td><td>125.35 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(+20.72%)</b></td><td>0.01 <b>(+36.39%)</b></td><td>0.01 <b>(+33.35%)</b></td><td>0.01 <b>(+275.35%)</b></td><td>0.00 <b>(-25.34%)</b></td><td>507.30 <b>(-73.36%)</b></td><td>365.14 <b>(-48.86%)</b></td><td>328.00 <b>(-25.01%)</b></td><td>250.20 (-17.15%)</td><td>103.76 <b>(-84.59%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1904.20 (n/a)</td><td>713.98 (n/a)</td><td>437.40 (n/a)</td><td>302.00 (n/a)</td><td>673.16 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(+146.80%)</b></td><td>0.01 <b>(+58.44%)</b></td><td>0.01 (+11.01%)</td><td>0.01 (+7.11%)</td><td>0.01 <b>(+438.71%)</b></td><td>607.60 (-6.64%)</td><td>422.32 <b>(-22.98%)</b></td><td>475.10 (-9.92%)</td><td>181.50 <b>(-59.49%)</b></td><td>191.80 <b>(+107.07%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>650.80 (n/a)</td><td>548.30 (n/a)</td><td>527.40 (n/a)</td><td>448.00 (n/a)</td><td>92.62 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (+12.80%)</td><td>0.01 <b>(+23.27%)</b></td><td>0.01 (+6.54%)</td><td>0.01 <b>(+325.81%)</b></td><td>0.00 (-10.20%)</td><td>573.10 <b>(-76.51%)</b></td><td>381.04 <b>(-50.67%)</b></td><td>367.70 (-6.15%)</td><td>244.80 (-11.34%)</td><td>142.06 <b>(-84.78%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2440.20 (n/a)</td><td>772.46 (n/a)</td><td>391.80 (n/a)</td><td>276.10 (n/a)</td><td>933.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 (-19.78%)</td><td>0.01 (-14.20%)</td><td>0.01 (+1.39%)</td><td>0.01 (-13.25%)</td><td>0.00 <b>(-30.42%)</b></td><td>635.70 (+15.27%)</td><td>475.68 (+13.53%)</td><td>463.00 (-1.38%)</td><td>306.60 <b>(+24.68%)</b></td><td>123.23 (-0.61%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.50 (n/a)</td><td>418.98 (n/a)</td><td>469.50 (n/a)</td><td>245.90 (n/a)</td><td>123.99 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(+39.61%)</b></td><td>0.01 <b>(+44.58%)</b></td><td>0.01 <b>(+56.71%)</b></td><td>0.01 <b>(+21.00%)</b></td><td>0.00 <b>(+65.17%)</b></td><td>553.80 (-17.36%)</td><td>338.26 <b>(-28.77%)</b></td><td>286.00 <b>(-36.20%)</b></td><td>267.10 <b>(-28.37%)</b></td><td>121.67 (+1.13%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>670.10 (n/a)</td><td>474.88 (n/a)</td><td>448.30 (n/a)</td><td>372.90 (n/a)</td><td>120.32 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (-4.98%)</td><td>0.03 <b>(+31.05%)</b></td><td>0.03 <b>(+76.84%)</b></td><td>0.02 <b>(+35.92%)</b></td><td>0.01 <b>(-34.68%)</b></td><td>463.40 <b>(-26.43%)</b></td><td>298.70 <b>(-32.72%)</b></td><td>283.10 <b>(-43.45%)</b></td><td>208.80 (+5.24%)</td><td>97.74 <b>(-48.54%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>629.90 (n/a)</td><td>443.96 (n/a)</td><td>500.60 (n/a)</td><td>198.40 (n/a)</td><td>189.95 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (+13.46%)</td><td>0.02 <b>(+34.71%)</b></td><td>0.03 <b>(+67.57%)</b></td><td>0.01 <b>(+20.92%)</b></td><td>0.01 (+15.09%)</td><td>564.20 (-17.31%)</td><td>369.70 <b>(-25.35%)</b></td><td>303.30 <b>(-40.32%)</b></td><td>246.20 (-11.88%)</td><td>131.19 (-8.92%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>682.30 (n/a)</td><td>495.22 (n/a)</td><td>508.20 (n/a)</td><td>279.40 (n/a)</td><td>144.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 <b>(+36.06%)</b></td><td>0.03 <b>(+30.02%)</b></td><td>0.03 <b>(+55.23%)</b></td><td>0.02 (+0.35%)</td><td>0.01 <b>(+73.99%)</b></td><td>539.20 (-0.35%)</td><td>339.78 (-16.61%)</td><td>270.20 <b>(-35.59%)</b></td><td>192.00 <b>(-26.52%)</b></td><td>148.69 <b>(+33.23%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.10 (n/a)</td><td>407.46 (n/a)</td><td>419.50 (n/a)</td><td>261.30 (n/a)</td><td>111.60 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (+1.68%)</td><td>0.03 <b>(+21.99%)</b></td><td>0.03 <b>(+58.46%)</b></td><td>0.02 (-1.36%)</td><td>0.01 (+3.50%)</td><td>461.40 (+1.38%)</td><td>287.04 (-17.46%)</td><td>241.00 <b>(-36.89%)</b></td><td>235.90 (-1.63%)</td><td>98.02 (+7.48%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>455.10 (n/a)</td><td>347.74 (n/a)</td><td>381.90 (n/a)</td><td>239.80 (n/a)</td><td>91.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (+6.73%)</td><td>0.03 <b>(+33.35%)</b></td><td>0.03 <b>(+23.20%)</b></td><td>0.01 <b>(+241.02%)</b></td><td>0.01 <b>(-35.53%)</b></td><td>560.00 <b>(-70.68%)</b></td><td>328.12 <b>(-53.48%)</b></td><td>263.50 (-18.85%)</td><td>232.90 (-6.32%)</td><td>134.32 <b>(-80.99%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1909.70 (n/a)</td><td>705.38 (n/a)</td><td>324.70 (n/a)</td><td>248.60 (n/a)</td><td>706.72 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (+14.71%)</td><td>0.03 <b>(+22.94%)</b></td><td>0.03 <b>(+24.97%)</b></td><td>0.01 (-9.82%)</td><td>0.01 <b>(+25.29%)</b></td><td>661.20 (+10.88%)</td><td>338.96 (-14.97%)</td><td>234.50 (-19.97%)</td><td>206.80 (-12.82%)</td><td>193.83 (+8.38%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.30 (n/a)</td><td>398.62 (n/a)</td><td>293.00 (n/a)</td><td>237.20 (n/a)</td><td>178.84 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (+2.93%)</td><td>0.02 (+14.00%)</td><td>0.02 <b>(+23.09%)</b></td><td>0.02 (+17.84%)</td><td>0.01 (+2.90%)</td><td>544.60 (-15.14%)</td><td>383.56 (-13.96%)</td><td>393.60 (-18.76%)</td><td>240.70 (-2.87%)</td><td>140.15 (-17.80%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>641.80 (n/a)</td><td>445.80 (n/a)</td><td>484.50 (n/a)</td><td>247.80 (n/a)</td><td>170.49 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (-14.81%)</td><td>0.02 (-13.52%)</td><td>0.02 <b>(-25.83%)</b></td><td>0.01 (+2.57%)</td><td>0.01 (-9.57%)</td><td>572.70 (-2.50%)</td><td>416.36 (+14.71%)</td><td>482.80 <b>(+34.82%)</b></td><td>261.30 (+17.39%)</td><td>144.66 (-0.70%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.40 (n/a)</td><td>362.96 (n/a)</td><td>358.10 (n/a)</td><td>222.60 (n/a)</td><td>145.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (+10.16%)</td><td>0.03 <b>(+32.33%)</b></td><td>0.03 <b>(+100.49%)</b></td><td>0.02 <b>(+29.40%)</b></td><td>0.01 (-3.48%)</td><td>477.00 <b>(-22.72%)</b></td><td>331.54 <b>(-27.55%)</b></td><td>261.50 <b>(-50.11%)</b></td><td>240.60 (-9.24%)</td><td>112.97 <b>(-32.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.20 (n/a)</td><td>457.64 (n/a)</td><td>524.20 (n/a)</td><td>265.10 (n/a)</td><td>166.94 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (+4.97%)</td><td>0.02 <b>(+25.13%)</b></td><td>0.03 <b>(+91.54%)</b></td><td>0.01 <b>(+50.02%)</b></td><td>0.01 <b>(-21.89%)</b></td><td>559.10 <b>(-33.35%)</b></td><td>374.72 <b>(-28.45%)</b></td><td>309.00 <b>(-47.79%)</b></td><td>246.00 (-4.76%)</td><td>130.55 <b>(-46.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>838.80 (n/a)</td><td>523.70 (n/a)</td><td>591.80 (n/a)</td><td>258.30 (n/a)</td><td>242.70 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (-7.11%)</td><td>0.02 <b>(-21.03%)</b></td><td>0.02 <b>(-34.30%)</b></td><td>0.01 (-15.67%)</td><td>0.01 (-7.23%)</td><td>617.20 (+18.60%)</td><td>484.84 <b>(+26.62%)</b></td><td>501.40 <b>(+52.17%)</b></td><td>292.50 (+7.66%)</td><td>121.72 (+8.99%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.40 (n/a)</td><td>382.90 (n/a)</td><td>329.50 (n/a)</td><td>271.70 (n/a)</td><td>111.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (+3.99%)</td><td>0.02 <b>(-21.44%)</b></td><td>0.02 (-11.97%)</td><td>0.00 <b>(-77.91%)</b></td><td>0.01 <b>(+105.90%)</b></td><td>2498.20 <b>(+352.74%)</b></td><td>876.26 <b>(+100.82%)</b></td><td>518.70 (+13.60%)</td><td>319.30 (-3.85%)</td><td>910.92 <b>(+968.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.80 (n/a)</td><td>436.34 (n/a)</td><td>456.60 (n/a)</td><td>332.10 (n/a)</td><td>85.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (-8.50%)</td><td>0.05 <b>(+21.88%)</b></td><td>0.06 <b>(+53.59%)</b></td><td>0.03 (-11.42%)</td><td>0.01 (-9.80%)</td><td>596.60 (+12.89%)</td><td>351.58 (-17.15%)</td><td>296.80 <b>(-34.90%)</b></td><td>257.00 (+9.27%)</td><td>139.72 <b>(+25.28%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>528.50 (n/a)</td><td>424.36 (n/a)</td><td>455.90 (n/a)</td><td>235.20 (n/a)</td><td>111.52 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (+6.16%)</td><td>0.05 (-12.92%)</td><td>0.04 <b>(-27.20%)</b></td><td>0.03 (-14.30%)</td><td>0.01 <b>(+35.39%)</b></td><td>511.60 (+16.67%)</td><td>364.32 (+18.45%)</td><td>382.30 <b>(+37.37%)</b></td><td>236.50 (-5.78%)</td><td>104.59 <b>(+39.78%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>438.50 (n/a)</td><td>307.56 (n/a)</td><td>278.30 (n/a)</td><td>251.00 (n/a)</td><td>74.82 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 <b>(-31.69%)</b></td><td>0.03 (-15.64%)</td><td>0.03 (-3.63%)</td><td>0.03 (-8.24%)</td><td>0.01 <b>(-45.59%)</b></td><td>653.40 (+8.99%)</td><td>539.48 (+7.46%)</td><td>592.50 (+3.77%)</td><td>285.80 <b>(+46.41%)</b></td><td>146.03 (-15.13%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.50 (n/a)</td><td>502.02 (n/a)</td><td>571.00 (n/a)</td><td>195.20 (n/a)</td><td>172.07 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (+0.49%)</td><td>0.04 (-5.17%)</td><td>0.04 (-7.04%)</td><td>0.03 <b>(-20.89%)</b></td><td>0.01 (+19.36%)</td><td>622.00 <b>(+26.42%)</b></td><td>416.94 (+9.42%)</td><td>408.20 (+7.56%)</td><td>261.60 (-0.49%)</td><td>140.23 <b>(+48.14%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>492.00 (n/a)</td><td>381.06 (n/a)</td><td>379.50 (n/a)</td><td>262.90 (n/a)</td><td>94.67 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (-11.27%)</td><td>0.03 <b>(-27.06%)</b></td><td>0.03 (-4.65%)</td><td>0.01 <b>(-78.63%)</b></td><td>0.02 (+17.42%)</td><td>2466.80 <b>(+367.91%)</b></td><td>864.40 <b>(+108.36%)</b></td><td>514.70 (+4.87%)</td><td>295.10 (+12.72%)</td><td>901.50 <b>(+617.76%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>527.20 (n/a)</td><td>414.86 (n/a)</td><td>490.80 (n/a)</td><td>261.80 (n/a)</td><td>125.60 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-9.15%)</td><td>0.06 (+18.23%)</td><td>0.06 <b>(+40.21%)</b></td><td>0.04 (+18.87%)</td><td>0.01 <b>(-26.87%)</b></td><td>438.60 (-15.88%)</td><td>310.44 <b>(-20.07%)</b></td><td>270.80 <b>(-28.68%)</b></td><td>235.70 (+10.09%)</td><td>86.13 <b>(-35.76%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>521.40 (n/a)</td><td>388.40 (n/a)</td><td>379.70 (n/a)</td><td>214.10 (n/a)</td><td>134.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 <b>(+110.40%)</b></td><td>0.05 <b>(+99.87%)</b></td><td>0.04 <b>(+46.35%)</b></td><td>0.04 <b>(+434.17%)</b></td><td>0.02 <b>(+53.17%)</b></td><td>463.20 <b>(-81.28%)</b></td><td>353.82 <b>(-62.29%)</b></td><td>366.30 <b>(-31.66%)</b></td><td>239.90 <b>(-52.48%)</b></td><td>109.36 <b>(-87.29%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2474.30 (n/a)</td><td>938.22 (n/a)</td><td>536.00 (n/a)</td><td>504.80 (n/a)</td><td>860.36 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-18.94%)</td><td>0.05 (-4.92%)</td><td>0.06 (+5.65%)</td><td>0.03 (+12.38%)</td><td>0.02 <b>(-25.22%)</b></td><td>536.50 (-11.01%)</td><td>347.86 (-1.23%)</td><td>267.20 (-5.35%)</td><td>236.70 <b>(+23.41%)</b></td><td>136.08 <b>(-20.18%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>602.90 (n/a)</td><td>352.18 (n/a)</td><td>282.30 (n/a)</td><td>191.80 (n/a)</td><td>170.48 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 <b>(-32.68%)</b></td><td>0.04 (-12.36%)</td><td>0.04 (-0.74%)</td><td>0.03 (-3.86%)</td><td>0.01 <b>(-46.79%)</b></td><td>627.20 (+4.03%)</td><td>473.32 (+4.18%)</td><td>466.00 (+0.76%)</td><td>274.30 <b>(+48.51%)</b></td><td>146.56 (-10.60%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>602.90 (n/a)</td><td>454.32 (n/a)</td><td>462.50 (n/a)</td><td>184.70 (n/a)</td><td>163.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 <b>(+28.05%)</b></td><td>0.05 <b>(+45.94%)</b></td><td>0.06 <b>(+60.82%)</b></td><td>0.04 <b>(+24.70%)</b></td><td>0.01 <b>(+47.32%)</b></td><td>459.70 (-19.82%)</td><td>326.04 <b>(-30.35%)</b></td><td>287.40 <b>(-37.82%)</b></td><td>241.90 <b>(-21.92%)</b></td><td>96.04 (-8.83%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>573.30 (n/a)</td><td>468.08 (n/a)</td><td>462.20 (n/a)</td><td>309.80 (n/a)</td><td>105.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (+2.18%)</td><td>0.05 <b>(+27.74%)</b></td><td>0.05 <b>(+60.13%)</b></td><td>0.03 (+19.35%)</td><td>0.01 (-0.57%)</td><td>538.50 (-16.21%)</td><td>367.88 <b>(-22.40%)</b></td><td>308.60 <b>(-37.54%)</b></td><td>272.00 (-2.16%)</td><td>112.96 (-13.70%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>642.70 (n/a)</td><td>474.10 (n/a)</td><td>494.10 (n/a)</td><td>278.00 (n/a)</td><td>130.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 <b>(+20.86%)</b></td><td>0.04 <b>(+43.18%)</b></td><td>0.04 <b>(+59.29%)</b></td><td>0.03 <b>(+41.69%)</b></td><td>0.02 <b>(+27.94%)</b></td><td>575.50 <b>(-29.42%)</b></td><td>407.34 <b>(-30.31%)</b></td><td>393.20 <b>(-37.22%)</b></td><td>264.80 (-17.28%)</td><td>143.71 <b>(-25.13%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>815.40 (n/a)</td><td>584.50 (n/a)</td><td>626.30 (n/a)</td><td>320.10 (n/a)</td><td>191.94 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 <b>(-27.86%)</b></td><td>0.10 (-17.15%)</td><td>0.11 (-15.77%)</td><td>0.06 (-4.75%)</td><td>0.03 <b>(-37.46%)</b></td><td>508.80 (+4.97%)</td><td>372.52 (+13.61%)</td><td>304.10 (+18.74%)</td><td>265.90 <b>(+38.63%)</b></td><td>121.77 (-12.68%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>484.70 (n/a)</td><td>327.88 (n/a)</td><td>256.10 (n/a)</td><td>191.80 (n/a)</td><td>139.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.13 (-8.45%)</td><td>0.11 <b>(+54.78%)</b></td><td>0.12 <b>(+71.24%)</b></td><td>0.06 <b>(+247.39%)</b></td><td>0.03 <b>(-37.99%)</b></td><td>549.20 <b>(-71.22%)</b></td><td>328.40 <b>(-55.56%)</b></td><td>279.60 <b>(-41.59%)</b></td><td>255.80 (+9.22%)</td><td>124.00 <b>(-81.40%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1908.00 (n/a)</td><td>738.98 (n/a)</td><td>478.70 (n/a)</td><td>234.20 (n/a)</td><td>666.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 <b>(+36.71%)</b></td><td>0.10 <b>(+50.85%)</b></td><td>0.13 <b>(+107.97%)</b></td><td>0.06 (+13.59%)</td><td>0.04 <b>(+98.66%)</b></td><td>541.00 (-11.96%)</td><td>357.46 <b>(-28.26%)</b></td><td>256.60 <b>(-51.92%)</b></td><td>236.60 <b>(-26.84%)</b></td><td>149.28 <b>(+33.76%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>614.50 (n/a)</td><td>498.26 (n/a)</td><td>533.70 (n/a)</td><td>323.40 (n/a)</td><td>111.60 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (-9.96%)</td><td>0.07 (-7.56%)</td><td>0.07 (-1.26%)</td><td>0.06 (+3.08%)</td><td>0.02 <b>(-29.27%)</b></td><td>538.30 (-2.97%)</td><td>463.22 (+4.90%)</td><td>493.10 (+1.29%)</td><td>319.70 (+11.05%)</td><td>84.80 <b>(-27.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>554.80 (n/a)</td><td>441.60 (n/a)</td><td>486.80 (n/a)</td><td>287.90 (n/a)</td><td>116.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 <b>(-36.93%)</b></td><td>0.07 <b>(-35.75%)</b></td><td>0.07 <b>(-36.89%)</b></td><td>0.05 (-6.45%)</td><td>0.02 <b>(-45.36%)</b></td><td>630.60 (+6.88%)</td><td>486.82 <b>(+46.37%)</b></td><td>478.50 <b>(+58.44%)</b></td><td>310.80 <b>(+58.57%)</b></td><td>132.35 (-11.95%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>590.00 (n/a)</td><td>332.60 (n/a)</td><td>302.00 (n/a)</td><td>196.00 (n/a)</td><td>150.31 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (-14.98%)</td><td>0.10 (-19.52%)</td><td>0.09 <b>(-25.78%)</b></td><td>0.07 (+5.55%)</td><td>0.03 <b>(-24.12%)</b></td><td>491.90 (-5.26%)</td><td>370.08 (+19.60%)</td><td>371.00 <b>(+34.76%)</b></td><td>233.40 (+17.64%)</td><td>105.02 (-17.16%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>519.20 (n/a)</td><td>309.44 (n/a)</td><td>275.30 (n/a)</td><td>198.40 (n/a)</td><td>126.78 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (-12.78%)</td><td>0.07 <b>(-23.81%)</b></td><td>0.06 <b>(-38.35%)</b></td><td>0.06 (+1.99%)</td><td>0.02 <b>(-35.80%)</b></td><td>560.70 (-1.94%)</td><td>483.72 <b>(+24.48%)</b></td><td>517.00 <b>(+62.22%)</b></td><td>310.30 (+14.67%)</td><td>101.62 <b>(-28.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>571.80 (n/a)</td><td>388.58 (n/a)</td><td>318.70 (n/a)</td><td>270.60 (n/a)</td><td>142.25 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 <b>(+35.43%)</b></td><td>0.09 <b>(+56.04%)</b></td><td>0.10 <b>(+68.79%)</b></td><td>0.05 <b>(+305.26%)</b></td><td>0.02 (-14.48%)</td><td>608.10 <b>(-75.32%)</b></td><td>374.36 <b>(-56.67%)</b></td><td>313.20 <b>(-40.76%)</b></td><td>287.30 <b>(-26.16%)</b></td><td>134.05 <b>(-85.06%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2464.30 (n/a)</td><td>863.90 (n/a)</td><td>528.70 (n/a)</td><td>389.10 (n/a)</td><td>897.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 <b>(-20.88%)</b></td><td>0.07 (-12.08%)</td><td>0.06 (-1.35%)</td><td>0.05 (-11.82%)</td><td>0.03 <b>(-28.92%)</b></td><td>674.60 (+13.42%)</td><td>521.40 (+9.50%)</td><td>536.20 (+1.36%)</td><td>268.80 <b>(+26.43%)</b></td><td>156.18 (+2.78%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>594.80 (n/a)</td><td>476.18 (n/a)</td><td>529.00 (n/a)</td><td>212.60 (n/a)</td><td>151.96 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 <b>(-50.91%)</b></td><td>0.07 <b>(-24.55%)</b></td><td>0.08 (-16.73%)</td><td>0.05 (+3.02%)</td><td>0.02 <b>(-68.70%)</b></td><td>675.90 (-2.93%)</td><td>464.10 (+15.30%)</td><td>415.80 <b>(+20.10%)</b></td><td>375.00 <b>(+103.69%)</b></td><td>122.37 <b>(-35.09%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>696.30 (n/a)</td><td>402.50 (n/a)</td><td>346.20 (n/a)</td><td>184.10 (n/a)</td><td>188.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 <b>(+48.96%)</b></td><td>0.07 (+7.00%)</td><td>0.07 (+12.73%)</td><td>0.03 <b>(-47.00%)</b></td><td>0.04 <b>(+139.88%)</b></td><td>1134.60 <b>(+88.66%)</b></td><td>566.60 (+15.70%)</td><td>475.70 (-11.28%)</td><td>241.10 <b>(-32.86%)</b></td><td>343.04 <b>(+216.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>601.40 (n/a)</td><td>489.70 (n/a)</td><td>536.20 (n/a)</td><td>359.10 (n/a)</td><td>108.44 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-11.74%)</td><td>0.04 <b>(-34.63%)</b></td><td>0.05 (-11.00%)</td><td>0.02 <b>(-68.06%)</b></td><td>0.02 <b>(+96.74%)</b></td><td>1926.30 <b>(+213.07%)</b></td><td>1093.66 <b>(+112.60%)</b></td><td>614.70 (+12.36%)</td><td>463.90 (+13.28%)</td><td>738.40 <b>(+696.62%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>615.30 (n/a)</td><td>514.42 (n/a)</td><td>547.10 (n/a)</td><td>409.50 (n/a)</td><td>92.69 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (+12.79%)</td><td>0.01 <b>(+33.83%)</b></td><td>0.01 <b>(+56.41%)</b></td><td>0.01 <b>(+69.82%)</b></td><td>0.00 <b>(-45.80%)</b></td><td>340.40 <b>(-41.11%)</b></td><td>288.40 <b>(-30.28%)</b></td><td>285.40 <b>(-36.07%)</b></td><td>237.50 (-11.31%)</td><td>37.42 <b>(-70.87%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.00 (n/a)</td><td>413.68 (n/a)</td><td>446.40 (n/a)</td><td>267.80 (n/a)</td><td>128.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(-27.72%)</b></td><td>0.02 <b>(-24.80%)</b></td><td>0.01 <b>(-41.39%)</b></td><td>0.01 (+1.29%)</td><td>0.01 <b>(-20.93%)</b></td><td>601.70 (-1.28%)</td><td>426.02 <b>(+28.99%)</b></td><td>485.40 <b>(+70.62%)</b></td><td>265.70 <b>(+38.31%)</b></td><td>150.12 (-7.14%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.50 (n/a)</td><td>330.28 (n/a)</td><td>284.50 (n/a)</td><td>192.10 (n/a)</td><td>161.66 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (+0.87%)</td><td>0.01 <b>(+27.13%)</b></td><td>0.01 <b>(+68.45%)</b></td><td>0.01 <b>(+30.04%)</b></td><td>0.00 <b>(-32.62%)</b></td><td>449.10 <b>(-23.10%)</b></td><td>308.10 <b>(-28.64%)</b></td><td>289.30 <b>(-40.64%)</b></td><td>228.30 (-0.83%)</td><td>86.23 <b>(-49.12%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.00 (n/a)</td><td>431.76 (n/a)</td><td>487.40 (n/a)</td><td>230.20 (n/a)</td><td>169.49 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (+3.84%)</td><td>0.01 (+6.56%)</td><td>0.01 <b>(+23.36%)</b></td><td>0.01 (+12.60%)</td><td>0.00 (-12.20%)</td><td>509.10 (-11.20%)</td><td>399.58 (-8.81%)</td><td>418.30 (-18.93%)</td><td>273.30 (-3.70%)</td><td>110.15 <b>(-21.20%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.30 (n/a)</td><td>438.16 (n/a)</td><td>516.00 (n/a)</td><td>283.80 (n/a)</td><td>139.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(+28.76%)</b></td><td>0.02 <b>(+52.66%)</b></td><td>0.02 (+11.43%)</td><td>0.01 <b>(+270.01%)</b></td><td>0.00 <b>(-55.95%)</b></td><td>294.80 <b>(-72.97%)</b></td><td>260.60 <b>(-49.69%)</b></td><td>269.40 (-10.26%)</td><td>220.00 <b>(-22.34%)</b></td><td>34.23 <b>(-90.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1090.70 (n/a)</td><td>517.94 (n/a)</td><td>300.20 (n/a)</td><td>283.30 (n/a)</td><td>349.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(+21.54%)</b></td><td>0.01 (-13.74%)</td><td>0.01 <b>(-27.18%)</b></td><td>0.01 <b>(-27.98%)</b></td><td>0.01 <b>(+78.36%)</b></td><td>610.40 <b>(+38.85%)</b></td><td>453.02 <b>(+28.20%)</b></td><td>472.50 <b>(+37.31%)</b></td><td>204.20 (-17.73%)</td><td>157.00 <b>(+84.60%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>439.60 (n/a)</td><td>353.36 (n/a)</td><td>344.10 (n/a)</td><td>248.20 (n/a)</td><td>85.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (+15.30%)</td><td>0.01 <b>(-20.92%)</b></td><td>0.01 <b>(-45.07%)</b></td><td>0.00 <b>(-75.68%)</b></td><td>0.01 <b>(+93.15%)</b></td><td>1925.10 <b>(+311.26%)</b></td><td>702.02 <b>(+104.89%)</b></td><td>528.10 <b>(+82.04%)</b></td><td>224.40 (-13.29%)</td><td>699.28 <b>(+612.31%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>468.10 (n/a)</td><td>342.64 (n/a)</td><td>290.10 (n/a)</td><td>258.80 (n/a)</td><td>98.17 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (-7.71%)</td><td>0.01 (+9.27%)</td><td>0.01 (+10.09%)</td><td>0.01 <b>(+22.06%)</b></td><td>0.00 <b>(-22.46%)</b></td><td>519.90 (-18.07%)</td><td>426.14 (-13.01%)</td><td>487.10 (-9.16%)</td><td>265.60 (+8.32%)</td><td>114.74 <b>(-28.25%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>634.60 (n/a)</td><td>489.90 (n/a)</td><td>536.20 (n/a)</td><td>245.20 (n/a)</td><td>159.91 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 (-2.35%)</td><td>0.01 <b>(-27.03%)</b></td><td>0.01 <b>(-53.25%)</b></td><td>0.01 <b>(-41.36%)</b></td><td>0.01 <b>(+85.20%)</b></td><td>576.40 <b>(+70.53%)</b></td><td>423.62 <b>(+62.10%)</b></td><td>527.00 <b>(+113.88%)</b></td><td>199.30 (+2.42%)</td><td>184.91 <b>(+235.79%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>338.00 (n/a)</td><td>261.34 (n/a)</td><td>246.40 (n/a)</td><td>194.60 (n/a)</td><td>55.07 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.02 <b>(+43.86%)</b></td><td>0.01 (+3.70%)</td><td>0.01 <b>(-21.96%)</b></td><td>0.01 (-3.65%)</td><td>0.01 <b>(+69.53%)</b></td><td>520.70 (+3.79%)</td><td>381.26 (+0.82%)</td><td>410.10 <b>(+28.16%)</b></td><td>205.70 <b>(-30.48%)</b></td><td>115.49 (+14.95%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>501.70 (n/a)</td><td>378.16 (n/a)</td><td>320.00 (n/a)</td><td>295.90 (n/a)</td><td>100.47 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.01 <b>(+48.56%)</b></td><td>0.01 <b>(+47.81%)</b></td><td>0.01 <b>(+60.83%)</b></td><td>0.01 (+11.83%)</td><td>0.00 <b>(+129.21%)</b></td><td>552.80 (-10.58%)</td><td>393.46 <b>(-29.30%)</b></td><td>372.40 <b>(-37.83%)</b></td><td>280.40 <b>(-32.69%)</b></td><td>114.63 <b>(+36.74%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>618.20 (n/a)</td><td>556.52 (n/a)</td><td>599.00 (n/a)</td><td>416.60 (n/a)</td><td>83.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (-6.74%)</td><td>0.03 (-8.43%)</td><td>0.02 (-19.00%)</td><td>0.02 (+18.64%)</td><td>0.01 (-19.41%)</td><td>470.10 (-15.71%)</td><td>355.60 (+3.35%)</td><td>349.50 <b>(+23.45%)</b></td><td>210.90 (+7.22%)</td><td>108.21 <b>(-27.16%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.70 (n/a)</td><td>344.06 (n/a)</td><td>283.10 (n/a)</td><td>196.70 (n/a)</td><td>148.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (+4.99%)</td><td>0.05 (+16.47%)</td><td>0.05 <b>(+22.79%)</b></td><td>0.02 (+6.01%)</td><td>0.01 (-12.39%)</td><td>586.10 (-5.68%)</td><td>308.36 (-17.15%)</td><td>242.50 (-18.57%)</td><td>209.50 (-4.73%)</td><td>156.41 (-12.12%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>621.40 (n/a)</td><td>372.20 (n/a)</td><td>297.80 (n/a)</td><td>219.90 (n/a)</td><td>177.98 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(-22.95%)</b></td><td>0.02 (-19.79%)</td><td>0.03 <b>(-22.81%)</b></td><td>0.01 <b>(-21.69%)</b></td><td>0.01 <b>(-20.64%)</b></td><td>618.40 <b>(+27.69%)</b></td><td>402.08 <b>(+24.74%)</b></td><td>316.50 <b>(+29.55%)</b></td><td>244.10 <b>(+29.77%)</b></td><td>174.53 <b>(+26.01%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>484.30 (n/a)</td><td>322.34 (n/a)</td><td>244.30 (n/a)</td><td>188.10 (n/a)</td><td>138.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (+17.26%)</td><td>0.03 (-8.81%)</td><td>0.03 (-17.38%)</td><td>0.02 (-19.16%)</td><td>0.01 <b>(+67.21%)</b></td><td>531.80 <b>(+23.70%)</b></td><td>357.10 (+16.04%)</td><td>349.00 <b>(+21.01%)</b></td><td>204.00 (-14.72%)</td><td>117.10 <b>(+63.16%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>429.90 (n/a)</td><td>307.74 (n/a)</td><td>288.40 (n/a)</td><td>239.20 (n/a)</td><td>71.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 (-7.67%)</td><td>0.02 <b>(-26.59%)</b></td><td>0.02 <b>(-36.71%)</b></td><td>0.01 <b>(-30.23%)</b></td><td>0.01 (-9.97%)</td><td>777.40 <b>(+43.33%)</b></td><td>514.66 <b>(+37.33%)</b></td><td>493.60 <b>(+58.00%)</b></td><td>256.20 (+8.28%)</td><td>186.97 <b>(+26.20%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.40 (n/a)</td><td>374.76 (n/a)</td><td>312.40 (n/a)</td><td>236.60 (n/a)</td><td>148.16 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (-16.58%)</td><td>0.03 (-13.27%)</td><td>0.04 (-7.88%)</td><td>0.02 (-0.32%)</td><td>0.01 (-12.14%)</td><td>642.40 (+0.33%)</td><td>400.22 (+13.96%)</td><td>274.50 (+8.54%)</td><td>265.80 (+19.89%)</td><td>179.60 (+2.04%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>640.30 (n/a)</td><td>351.18 (n/a)</td><td>252.90 (n/a)</td><td>221.70 (n/a)</td><td>176.00 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(-25.54%)</b></td><td>0.02 (+12.59%)</td><td>0.02 <b>(+35.22%)</b></td><td>0.02 <b>(+178.33%)</b></td><td>0.01 <b>(-52.80%)</b></td><td>469.70 <b>(-64.07%)</b></td><td>370.94 <b>(-37.44%)</b></td><td>413.90 <b>(-26.04%)</b></td><td>257.70 <b>(+34.36%)</b></td><td>98.07 <b>(-77.47%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1307.20 (n/a)</td><td>592.90 (n/a)</td><td>559.60 (n/a)</td><td>191.80 (n/a)</td><td>435.31 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (-0.19%)</td><td>0.02 (+11.57%)</td><td>0.02 (-2.16%)</td><td>0.02 <b>(+301.65%)</b></td><td>0.01 <b>(-29.22%)</b></td><td>574.20 <b>(-75.11%)</b></td><td>490.68 <b>(-42.09%)</b></td><td>541.60 (+2.21%)</td><td>260.90 (+0.19%)</td><td>130.90 <b>(-84.31%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2306.50 (n/a)</td><td>847.26 (n/a)</td><td>529.90 (n/a)</td><td>260.40 (n/a)</td><td>834.06 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.04 (-14.87%)</td><td>0.02 (-0.57%)</td><td>0.02 <b>(+34.14%)</b></td><td>0.01 <b>(+86.57%)</b></td><td>0.01 <b>(-46.29%)</b></td><td>571.10 <b>(-46.41%)</b></td><td>396.02 <b>(-27.21%)</b></td><td>441.40 <b>(-25.45%)</b></td><td>232.20 (+17.45%)</td><td>139.81 <b>(-61.52%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1065.60 (n/a)</td><td>544.08 (n/a)</td><td>592.10 (n/a)</td><td>197.70 (n/a)</td><td>363.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(-32.32%)</b></td><td>0.02 (-9.41%)</td><td>0.02 <b>(+30.00%)</b></td><td>0.01 (-8.75%)</td><td>0.00 <b>(-53.98%)</b></td><td>643.20 (+9.57%)</td><td>441.74 (+1.49%)</td><td>385.30 <b>(-23.09%)</b></td><td>341.30 <b>(+47.75%)</b></td><td>119.57 <b>(-24.16%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>587.00 (n/a)</td><td>435.24 (n/a)</td><td>501.00 (n/a)</td><td>231.00 (n/a)</td><td>157.65 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.03 <b>(-20.55%)</b></td><td>0.02 <b>(-21.17%)</b></td><td>0.02 <b>(-20.71%)</b></td><td>0.01 (-9.94%)</td><td>0.01 <b>(-32.05%)</b></td><td>667.10 (+11.04%)</td><td>451.78 <b>(+22.68%)</b></td><td>449.90 <b>(+26.13%)</b></td><td>304.30 <b>(+25.85%)</b></td><td>134.87 (-4.47%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.80 (n/a)</td><td>368.26 (n/a)</td><td>356.70 (n/a)</td><td>241.80 (n/a)</td><td>141.18 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 <b>(-36.62%)</b></td><td>0.04 <b>(-34.65%)</b></td><td>0.05 <b>(-26.02%)</b></td><td>0.03 <b>(-45.67%)</b></td><td>0.02 (-5.39%)</td><td>560.20 <b>(+84.03%)</b></td><td>401.86 <b>(+62.88%)</b></td><td>347.80 <b>(+35.17%)</b></td><td>270.10 <b>(+57.77%)</b></td><td>142.73 <b>(+195.77%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>304.40 (n/a)</td><td>246.72 (n/a)</td><td>257.30 (n/a)</td><td>171.20 (n/a)</td><td>48.26 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (-18.27%)</td><td>0.07 (+12.97%)</td><td>0.08 <b>(+47.62%)</b></td><td>0.04 (+13.86%)</td><td>0.02 <b>(-34.63%)</b></td><td>577.60 (-12.18%)</td><td>355.50 (-17.26%)</td><td>302.30 <b>(-32.25%)</b></td><td>286.20 <b>(+22.36%)</b></td><td>125.17 <b>(-26.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>657.70 (n/a)</td><td>429.64 (n/a)</td><td>446.20 (n/a)</td><td>233.90 (n/a)</td><td>170.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-10.40%)</td><td>0.05 (-7.20%)</td><td>0.06 (+2.34%)</td><td>0.03 (+0.62%)</td><td>0.01 <b>(-20.17%)</b></td><td>485.10 (-0.61%)</td><td>344.02 (+5.15%)</td><td>284.30 (-2.27%)</td><td>242.20 (+11.61%)</td><td>106.29 (-8.61%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>488.10 (n/a)</td><td>327.16 (n/a)</td><td>290.90 (n/a)</td><td>217.00 (n/a)</td><td>116.31 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-12.92%)</td><td>0.05 <b>(-26.31%)</b></td><td>0.05 <b>(-26.98%)</b></td><td>0.02 <b>(-46.96%)</b></td><td>0.02 (+16.85%)</td><td>1008.30 <b>(+88.50%)</b></td><td>516.42 <b>(+52.61%)</b></td><td>410.60 <b>(+36.96%)</b></td><td>289.90 (+14.86%)</td><td>289.28 <b>(+153.77%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>534.90 (n/a)</td><td>338.40 (n/a)</td><td>299.80 (n/a)</td><td>252.40 (n/a)</td><td>113.99 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-15.17%)</td><td>0.05 <b>(-20.51%)</b></td><td>0.04 <b>(-41.46%)</b></td><td>0.03 (+16.28%)</td><td>0.02 <b>(-31.47%)</b></td><td>570.70 (-14.00%)</td><td>393.86 (+14.36%)</td><td>422.20 <b>(+70.79%)</b></td><td>238.10 (+17.87%)</td><td>127.04 <b>(-33.35%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>663.60 (n/a)</td><td>344.40 (n/a)</td><td>247.20 (n/a)</td><td>202.00 (n/a)</td><td>190.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (+0.38%)</td><td>0.06 <b>(+22.55%)</b></td><td>0.04 (+6.76%)</td><td>0.04 <b>(+95.78%)</b></td><td>0.02 (-5.57%)</td><td>577.80 <b>(-48.92%)</b></td><td>423.42 <b>(-27.63%)</b></td><td>510.40 (-6.33%)</td><td>244.30 (-0.41%)</td><td>157.37 <b>(-53.48%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1131.20 (n/a)</td><td>585.04 (n/a)</td><td>544.90 (n/a)</td><td>245.30 (n/a)</td><td>338.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 <b>(-21.13%)</b></td><td>0.05 (-8.54%)</td><td>0.05 (+16.15%)</td><td>0.03 (+2.23%)</td><td>0.01 <b>(-49.78%)</b></td><td>495.10 (-2.17%)</td><td>365.56 (+0.79%)</td><td>341.00 (-13.91%)</td><td>272.70 <b>(+26.78%)</b></td><td>85.91 <b>(-35.04%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>506.10 (n/a)</td><td>362.70 (n/a)</td><td>396.10 (n/a)</td><td>215.10 (n/a)</td><td>132.26 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 <b>(+41.81%)</b></td><td>0.06 <b>(+40.61%)</b></td><td>0.06 <b>(+84.63%)</b></td><td>0.03 (-1.36%)</td><td>0.02 <b>(+67.35%)</b></td><td>587.50 (+1.38%)</td><td>352.52 <b>(-24.00%)</b></td><td>284.70 <b>(-45.83%)</b></td><td>206.90 <b>(-29.48%)</b></td><td>156.86 (+18.62%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>579.50 (n/a)</td><td>463.82 (n/a)</td><td>525.60 (n/a)</td><td>293.40 (n/a)</td><td>132.23 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (+13.60%)</td><td>0.04 (+13.32%)</td><td>0.04 <b>(+26.23%)</b></td><td>0.02 <b>(-45.59%)</b></td><td>0.02 <b>(+60.66%)</b></td><td>1057.90 <b>(+83.79%)</b></td><td>483.32 (+6.20%)</td><td>378.10 <b>(-20.78%)</b></td><td>249.40 (-11.97%)</td><td>329.06 <b>(+183.00%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>575.60 (n/a)</td><td>455.10 (n/a)</td><td>477.30 (n/a)</td><td>283.30 (n/a)</td><td>116.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 <b>(+20.13%)</b></td><td>0.05 (-7.26%)</td><td>0.04 <b>(-28.50%)</b></td><td>0.03 (+15.69%)</td><td>0.03 <b>(+35.22%)</b></td><td>564.40 (-13.57%)</td><td>421.30 (+11.51%)</td><td>503.80 <b>(+39.87%)</b></td><td>200.20 (-16.76%)</td><td>154.79 (-4.97%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>653.00 (n/a)</td><td>377.82 (n/a)</td><td>360.20 (n/a)</td><td>240.50 (n/a)</td><td>162.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.05 (+9.47%)</td><td>0.04 (+15.72%)</td><td>0.04 <b>(+21.57%)</b></td><td>0.03 (+9.90%)</td><td>0.01 (-4.68%)</td><td>482.80 (-9.01%)</td><td>411.78 (-14.02%)</td><td>420.80 (-17.75%)</td><td>332.20 (-8.64%)</td><td>54.44 <b>(-21.48%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>530.60 (n/a)</td><td>478.90 (n/a)</td><td>511.60 (n/a)</td><td>363.60 (n/a)</td><td>69.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 <b>(-25.09%)</b></td><td>0.08 <b>(-27.71%)</b></td><td>0.07 <b>(-36.03%)</b></td><td>0.05 <b>(-42.15%)</b></td><td>0.03 <b>(+27.45%)</b></td><td>621.80 <b>(+72.87%)</b></td><td>444.28 <b>(+49.70%)</b></td><td>475.20 <b>(+56.37%)</b></td><td>282.00 <b>(+33.52%)</b></td><td>155.57 <b>(+189.20%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>359.70 (n/a)</td><td>296.78 (n/a)</td><td>303.90 (n/a)</td><td>211.20 (n/a)</td><td>53.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.13 (-11.94%)</td><td>0.10 (-2.22%)</td><td>0.09 <b>(-35.98%)</b></td><td>0.07 <b>(+315.32%)</b></td><td>0.03 <b>(-56.14%)</b></td><td>459.60 <b>(-75.92%)</b></td><td>346.76 <b>(-45.06%)</b></td><td>371.30 <b>(+56.21%)</b></td><td>248.40 (+13.58%)</td><td>89.81 <b>(-87.69%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1908.90 (n/a)</td><td>631.14 (n/a)</td><td>237.70 (n/a)</td><td>218.70 (n/a)</td><td>729.80 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (-12.79%)</td><td>0.10 <b>(-23.16%)</b></td><td>0.09 <b>(-37.77%)</b></td><td>0.07 (+6.98%)</td><td>0.03 (-17.81%)</td><td>556.10 (-6.52%)</td><td>422.76 <b>(+26.03%)</b></td><td>448.60 <b>(+60.67%)</b></td><td>290.10 (+14.66%)</td><td>119.84 (-17.81%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>594.90 (n/a)</td><td>335.44 (n/a)</td><td>279.20 (n/a)</td><td>253.00 (n/a)</td><td>145.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 (+7.86%)</td><td>0.10 <b>(+21.95%)</b></td><td>0.11 <b>(+52.55%)</b></td><td>0.06 <b>(+237.21%)</b></td><td>0.04 (-17.14%)</td><td>580.90 <b>(-70.34%)</b></td><td>386.56 <b>(-44.42%)</b></td><td>289.60 <b>(-34.45%)</b></td><td>224.20 (-7.28%)</td><td>167.82 <b>(-76.60%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1958.80 (n/a)</td><td>695.54 (n/a)</td><td>441.80 (n/a)</td><td>241.80 (n/a)</td><td>717.29 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 (+7.29%)</td><td>0.09 (-14.42%)</td><td>0.08 <b>(-37.59%)</b></td><td>0.02 <b>(-72.02%)</b></td><td>0.06 <b>(+70.32%)</b></td><td>2065.50 <b>(+257.35%)</b></td><td>750.74 <b>(+81.75%)</b></td><td>531.80 <b>(+60.23%)</b></td><td>269.20 (-6.79%)</td><td>749.79 <b>(+442.98%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>578.00 (n/a)</td><td>413.06 (n/a)</td><td>331.90 (n/a)</td><td>288.80 (n/a)</td><td>138.09 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 <b>(-45.30%)</b></td><td>0.06 <b>(-32.51%)</b></td><td>0.06 (-12.80%)</td><td>0.03 <b>(-42.31%)</b></td><td>0.02 <b>(-44.55%)</b></td><td>1131.50 <b>(+73.33%)</b></td><td>633.56 <b>(+48.79%)</b></td><td>519.90 (+14.67%)</td><td>433.80 <b>(+82.81%)</b></td><td>288.91 <b>(+83.30%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>652.80 (n/a)</td><td>425.80 (n/a)</td><td>453.40 (n/a)</td><td>237.30 (n/a)</td><td>157.62 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.13 (-0.60%)</td><td>0.09 (-5.72%)</td><td>0.07 (-18.73%)</td><td>0.06 (-8.50%)</td><td>0.03 <b>(+34.01%)</b></td><td>604.40 (+9.29%)</td><td>466.94 (+10.88%)</td><td>531.40 <b>(+23.04%)</b></td><td>293.20 (+0.62%)</td><td>143.53 <b>(+50.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>553.00 (n/a)</td><td>421.14 (n/a)</td><td>431.90 (n/a)</td><td>291.40 (n/a)</td><td>95.48 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 <b>(-35.77%)</b></td><td>0.08 (+7.42%)</td><td>0.08 (+12.79%)</td><td>0.06 <b>(+266.47%)</b></td><td>0.02 <b>(-70.65%)</b></td><td>541.90 <b>(-72.71%)</b></td><td>418.04 <b>(-57.61%)</b></td><td>416.80 (-11.34%)</td><td>302.80 <b>(+55.68%)</b></td><td>94.91 <b>(-89.63%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1985.80 (n/a)</td><td>986.12 (n/a)</td><td>470.10 (n/a)</td><td>194.50 (n/a)</td><td>915.64 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 (+5.21%)</td><td>0.11 (+5.90%)</td><td>0.13 (+9.11%)</td><td>0.06 <b>(+198.79%)</b></td><td>0.04 (-15.00%)</td><td>587.20 <b>(-66.53%)</b></td><td>380.06 <b>(-35.70%)</b></td><td>294.50 (-8.34%)</td><td>216.40 (-4.96%)</td><td>159.28 <b>(-75.57%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1754.60 (n/a)</td><td>591.10 (n/a)</td><td>321.30 (n/a)</td><td>227.70 (n/a)</td><td>652.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (-13.89%)</td><td>0.08 (-8.71%)</td><td>0.08 (+10.06%)</td><td>0.05 (-7.90%)</td><td>0.03 (-15.84%)</td><td>610.80 (+8.59%)</td><td>451.24 (+8.85%)</td><td>432.70 (-9.13%)</td><td>293.60 (+16.14%)</td><td>150.44 (+11.10%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>562.50 (n/a)</td><td>414.56 (n/a)</td><td>476.20 (n/a)</td><td>252.80 (n/a)</td><td>135.40 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (+5.57%)</td><td>0.07 (+1.25%)</td><td>0.07 (-9.33%)</td><td>0.05 <b>(+33.08%)</b></td><td>0.02 <b>(-21.51%)</b></td><td>447.50 <b>(-24.85%)</b></td><td>326.52 (-8.72%)</td><td>297.90 (+10.29%)</td><td>210.40 (-5.27%)</td><td>90.41 <b>(-44.04%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>595.50 (n/a)</td><td>357.72 (n/a)</td><td>270.10 (n/a)</td><td>222.10 (n/a)</td><td>161.56 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-12.20%)</td><td>0.05 (-6.37%)</td><td>0.05 (+1.28%)</td><td>0.04 (+6.74%)</td><td>0.02 <b>(-20.06%)</b></td><td>523.10 (-6.30%)</td><td>404.86 (+4.09%)</td><td>424.70 (-1.26%)</td><td>284.20 (+13.91%)</td><td>111.02 (-12.73%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>558.30 (n/a)</td><td>388.94 (n/a)</td><td>430.10 (n/a)</td><td>249.50 (n/a)</td><td>127.21 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (+5.48%)</td><td>0.07 <b>(+44.41%)</b></td><td>0.07 <b>(+74.05%)</b></td><td>0.05 <b>(+150.08%)</b></td><td>0.02 <b>(-23.08%)</b></td><td>428.00 <b>(-60.01%)</b></td><td>322.76 <b>(-41.11%)</b></td><td>275.20 <b>(-42.55%)</b></td><td>235.70 (-5.23%)</td><td>92.03 <b>(-70.60%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1070.40 (n/a)</td><td>548.10 (n/a)</td><td>479.00 (n/a)</td><td>248.70 (n/a)</td><td>313.02 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-14.92%)</td><td>0.04 (-1.36%)</td><td>0.04 (+5.25%)</td><td>0.02 (-2.69%)</td><td>0.02 <b>(-20.24%)</b></td><td>1055.10 (+2.76%)</td><td>549.44 (-1.33%)</td><td>490.30 (-4.98%)</td><td>288.50 (+17.52%)</td><td>295.72 (+2.80%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1026.80 (n/a)</td><td>556.82 (n/a)</td><td>516.00 (n/a)</td><td>245.50 (n/a)</td><td>287.65 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-3.70%)</td><td>0.05 (-0.62%)</td><td>0.05 (+13.67%)</td><td>0.04 (+0.55%)</td><td>0.01 (-15.89%)</td><td>551.80 (-0.54%)</td><td>446.18 (-0.84%)</td><td>445.20 (-12.03%)</td><td>313.70 (+3.84%)</td><td>91.66 (-14.22%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>554.80 (n/a)</td><td>449.96 (n/a)</td><td>506.10 (n/a)</td><td>302.10 (n/a)</td><td>106.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 <b>(-46.38%)</b></td><td>0.03 <b>(-41.36%)</b></td><td>0.03 <b>(-29.75%)</b></td><td>0.01 <b>(-68.55%)</b></td><td>0.02 <b>(-36.67%)</b></td><td>1954.70 <b>(+217.94%)</b></td><td>843.36 <b>(+105.12%)</b></td><td>619.10 <b>(+42.35%)</b></td><td>367.30 <b>(+86.54%)</b></td><td>644.99 <b>(+312.26%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>614.80 (n/a)</td><td>411.16 (n/a)</td><td>434.90 (n/a)</td><td>196.90 (n/a)</td><td>156.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (-7.03%)</td><td>0.08 (+16.23%)</td><td>0.09 <b>(+70.98%)</b></td><td>0.04 (-2.18%)</td><td>0.02 (-1.46%)</td><td>562.50 (+2.24%)</td><td>362.06 (-13.35%)</td><td>276.60 <b>(-41.51%)</b></td><td>250.00 (+7.57%)</td><td>139.79 (+7.64%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>550.20 (n/a)</td><td>417.84 (n/a)</td><td>472.90 (n/a)</td><td>232.40 (n/a)</td><td>129.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 <b>(+26.79%)</b></td><td>0.09 <b>(+24.84%)</b></td><td>0.09 <b>(+82.42%)</b></td><td>0.05 (-4.28%)</td><td>0.03 (+16.37%)</td><td>514.20 (+4.47%)</td><td>317.62 (-19.07%)</td><td>260.30 <b>(-45.19%)</b></td><td>200.40 <b>(-21.13%)</b></td><td>123.22 (-0.40%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>492.20 (n/a)</td><td>392.48 (n/a)</td><td>474.90 (n/a)</td><td>254.10 (n/a)</td><td>123.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 (+4.73%)</td><td>0.05 (-18.91%)</td><td>0.04 <b>(-29.91%)</b></td><td>0.01 <b>(-71.71%)</b></td><td>0.04 <b>(+76.21%)</b></td><td>2506.10 <b>(+253.42%)</b></td><td>1111.74 <b>(+150.43%)</b></td><td>610.40 <b>(+42.68%)</b></td><td>248.10 (-4.54%)</td><td>1040.57 <b>(+479.53%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>709.10 (n/a)</td><td>443.94 (n/a)</td><td>427.80 (n/a)</td><td>259.90 (n/a)</td><td>179.56 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 <b>(+33.87%)</b></td><td>0.07 (+15.57%)</td><td>0.05 (-0.43%)</td><td>0.05 (+16.71%)</td><td>0.03 <b>(+42.22%)</b></td><td>516.70 (-14.33%)</td><td>393.60 (-10.68%)</td><td>461.60 (+0.41%)</td><td>215.40 <b>(-25.29%)</b></td><td>137.53 (-3.27%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>603.10 (n/a)</td><td>440.64 (n/a)</td><td>459.70 (n/a)</td><td>288.30 (n/a)</td><td>142.19 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.11 (+18.78%)</td><td>0.07 (+1.46%)</td><td>0.05 <b>(-36.03%)</b></td><td>0.04 (+15.47%)</td><td>0.03 (+1.44%)</td><td>603.00 (-13.40%)</td><td>406.64 (-6.35%)</td><td>458.40 <b>(+56.29%)</b></td><td>221.60 (-15.81%)</td><td>154.59 <b>(-28.64%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>696.30 (n/a)</td><td>434.20 (n/a)</td><td>293.30 (n/a)</td><td>263.20 (n/a)</td><td>216.62 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 (+7.57%)</td><td>0.06 (+14.81%)</td><td>0.05 (-13.01%)</td><td>0.04 <b>(+70.32%)</b></td><td>0.02 (+7.23%)</td><td>574.60 <b>(-41.28%)</b></td><td>445.54 (-17.21%)</td><td>536.90 (+14.94%)</td><td>266.80 (-7.04%)</td><td>147.81 <b>(-43.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>978.60 (n/a)</td><td>538.18 (n/a)</td><td>467.10 (n/a)</td><td>287.00 (n/a)</td><td>261.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (-5.53%)</td><td>0.07 (+10.33%)</td><td>0.07 (-12.68%)</td><td>0.05 <b>(+100.61%)</b></td><td>0.01 <b>(-53.64%)</b></td><td>391.50 <b>(-50.16%)</b></td><td>284.64 <b>(-25.95%)</b></td><td>275.70 (+14.54%)</td><td>237.80 (+5.88%)</td><td>62.48 <b>(-74.08%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>785.50 (n/a)</td><td>384.38 (n/a)</td><td>240.70 (n/a)</td><td>224.60 (n/a)</td><td>241.09 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-4.28%)</td><td>0.05 (-11.43%)</td><td>0.05 <b>(-27.62%)</b></td><td>0.04 (+1.62%)</td><td>0.02 (+4.33%)</td><td>507.50 (-1.59%)</td><td>380.36 (+13.66%)</td><td>389.50 <b>(+38.17%)</b></td><td>256.60 (+4.48%)</td><td>115.00 (+4.06%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>515.70 (n/a)</td><td>334.64 (n/a)</td><td>281.90 (n/a)</td><td>245.60 (n/a)</td><td>110.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.08 (+3.07%)</td><td>0.07 (+8.69%)</td><td>0.08 (+2.68%)</td><td>0.05 <b>(+25.45%)</b></td><td>0.01 <b>(-25.01%)</b></td><td>377.20 <b>(-20.30%)</b></td><td>276.66 (-11.83%)</td><td>245.10 (-2.62%)</td><td>224.50 (-2.98%)</td><td>62.68 <b>(-40.50%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>473.30 (n/a)</td><td>313.78 (n/a)</td><td>251.70 (n/a)</td><td>231.40 (n/a)</td><td>105.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-5.76%)</td><td>0.06 (+0.68%)</td><td>0.07 (+12.89%)</td><td>0.03 <b>(-20.70%)</b></td><td>0.02 (+9.76%)</td><td>600.30 <b>(+26.09%)</b></td><td>338.10 (+3.63%)</td><td>266.80 (-11.42%)</td><td>247.80 (+6.12%)</td><td>150.00 <b>(+50.38%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>476.10 (n/a)</td><td>326.26 (n/a)</td><td>301.20 (n/a)</td><td>233.50 (n/a)</td><td>99.75 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (-12.58%)</td><td>0.04 (-16.67%)</td><td>0.04 <b>(-20.39%)</b></td><td>0.03 <b>(-23.99%)</b></td><td>0.01 (-4.89%)</td><td>580.60 <b>(+31.57%)</b></td><td>440.20 <b>(+21.86%)</b></td><td>446.90 <b>(+25.60%)</b></td><td>262.90 (+14.40%)</td><td>116.80 <b>(+36.96%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>441.30 (n/a)</td><td>361.24 (n/a)</td><td>355.80 (n/a)</td><td>229.80 (n/a)</td><td>85.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.07 (+1.87%)</td><td>0.04 (+5.73%)</td><td>0.04 (-14.57%)</td><td>0.02 (+0.27%)</td><td>0.02 <b>(+20.36%)</b></td><td>1040.70 (-0.27%)</td><td>536.42 (-0.95%)</td><td>470.60 (+17.04%)</td><td>269.50 (-1.86%)</td><td>320.19 (+3.85%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1043.50 (n/a)</td><td>541.54 (n/a)</td><td>402.10 (n/a)</td><td>274.60 (n/a)</td><td>308.31 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.44 (+13.08%)</td><td>0.36 (+19.33%)</td><td>0.37 (+11.03%)</td><td>0.22 <b>(+23.64%)</b></td><td>0.09 (-6.91%)</td><td>439.70 (-19.13%)</td><td>293.88 (-19.33%)</td><td>268.70 (-9.92%)</td><td>222.70 (-11.59%)</td><td>89.84 <b>(-33.38%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.33 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>543.70 (n/a)</td><td>364.32 (n/a)</td><td>298.30 (n/a)</td><td>251.90 (n/a)</td><td>134.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.36 (-12.24%)</td><td>0.22 <b>(-28.76%)</b></td><td>0.19 <b>(-47.21%)</b></td><td>0.14 (-7.84%)</td><td>0.08 (-16.53%)</td><td>712.80 (+8.51%)</td><td>503.88 <b>(+36.87%)</b></td><td>530.00 <b>(+89.42%)</b></td><td>275.80 (+13.92%)</td><td>163.38 (-3.93%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.35 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>656.90 (n/a)</td><td>368.14 (n/a)</td><td>279.80 (n/a)</td><td>242.10 (n/a)</td><td>170.06 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.60 <b>(+34.85%)</b></td><td>0.28 (-6.28%)</td><td>0.17 <b>(-33.25%)</b></td><td>0.15 <b>(-20.22%)</b></td><td>0.19 <b>(+65.11%)</b></td><td>661.40 <b>(+25.34%)</b></td><td>465.38 <b>(+24.55%)</b></td><td>583.00 <b>(+49.83%)</b></td><td>164.60 <b>(-25.86%)</b></td><td>213.13 <b>(+57.62%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>527.70 (n/a)</td><td>373.66 (n/a)</td><td>389.10 (n/a)</td><td>222.00 (n/a)</td><td>135.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.38 (+19.71%)</td><td>0.23 (-7.77%)</td><td>0.19 <b>(-26.04%)</b></td><td>0.12 (+3.43%)</td><td>0.11 <b>(+39.33%)</b></td><td>614.40 (-3.32%)</td><td>396.12 (+15.14%)</td><td>386.10 <b>(+35.19%)</b></td><td>192.40 (-16.49%)</td><td>181.44 (+8.68%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>635.50 (n/a)</td><td>344.04 (n/a)</td><td>285.60 (n/a)</td><td>230.40 (n/a)</td><td>166.95 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.32 (+7.72%)</td><td>0.22 (+13.10%)</td><td>0.17 (+8.90%)</td><td>0.14 (+7.93%)</td><td>0.08 (+10.10%)</td><td>530.60 (-7.35%)</td><td>381.70 (-11.73%)</td><td>442.30 (-8.16%)</td><td>231.00 (-7.19%)</td><td>131.69 (-10.75%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>572.70 (n/a)</td><td>432.40 (n/a)</td><td>481.60 (n/a)</td><td>248.90 (n/a)</td><td>147.56 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.20 <b>(-31.01%)</b></td><td>0.15 (-15.83%)</td><td>0.14 (-19.62%)</td><td>0.11 <b>(+65.03%)</b></td><td>0.03 <b>(-59.95%)</b></td><td>669.70 <b>(-39.40%)</b></td><td>508.50 (-2.95%)</td><td>526.70 <b>(+24.43%)</b></td><td>376.50 <b>(+44.92%)</b></td><td>110.87 <b>(-67.14%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>1105.20 (n/a)</td><td>523.96 (n/a)</td><td>423.30 (n/a)</td><td>259.80 (n/a)</td><td>337.35 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (-1.12%)</td><td>0.09 (+12.52%)</td><td>0.11 <b>(+65.30%)</b></td><td>0.02 <b>(-42.06%)</b></td><td>0.05 (+17.41%)</td><td>1851.60 <b>(+72.58%)</b></td><td>655.84 (+17.25%)</td><td>335.70 <b>(-39.50%)</b></td><td>257.80 (+1.14%)</td><td>678.33 <b>(+113.58%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1072.90 (n/a)</td><td>559.36 (n/a)</td><td>554.90 (n/a)</td><td>254.90 (n/a)</td><td>317.60 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (+0.33%)</td><td>0.12 (+16.25%)</td><td>0.13 <b>(+69.25%)</b></td><td>0.08 (+10.38%)</td><td>0.03 <b>(-30.92%)</b></td><td>474.30 (-9.42%)</td><td>335.34 (-18.73%)</td><td>293.00 <b>(-40.92%)</b></td><td>258.80 (-0.31%)</td><td>86.33 <b>(-36.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>523.60 (n/a)</td><td>412.60 (n/a)</td><td>495.90 (n/a)</td><td>259.60 (n/a)</td><td>135.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.16 <b>(+20.64%)</b></td><td>0.11 (+16.75%)</td><td>0.13 <b>(+54.33%)</b></td><td>0.06 (-19.26%)</td><td>0.04 <b>(+82.29%)</b></td><td>603.80 <b>(+23.86%)</b></td><td>388.56 (-4.47%)</td><td>278.10 <b>(-35.21%)</b></td><td>228.90 (-17.10%)</td><td>176.46 <b>(+93.48%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>487.50 (n/a)</td><td>406.74 (n/a)</td><td>429.20 (n/a)</td><td>276.10 (n/a)</td><td>91.21 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.16 (+17.89%)</td><td>0.09 <b>(+23.97%)</b></td><td>0.08 (+14.99%)</td><td>0.05 (+12.08%)</td><td>0.04 <b>(+21.72%)</b></td><td>724.70 (-10.77%)</td><td>456.76 (-17.83%)</td><td>461.00 (-13.04%)</td><td>234.20 (-15.14%)</td><td>188.49 (-5.24%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>812.20 (n/a)</td><td>555.88 (n/a)</td><td>530.10 (n/a)</td><td>276.00 (n/a)</td><td>198.91 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 (-2.75%)</td><td>0.10 (-0.49%)</td><td>0.09 (+0.84%)</td><td>0.07 (+5.20%)</td><td>0.03 (-14.23%)</td><td>516.60 (-4.95%)</td><td>392.88 (-2.72%)</td><td>426.40 (-0.81%)</td><td>246.10 (+2.84%)</td><td>119.27 (-17.30%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>543.50 (n/a)</td><td>403.88 (n/a)</td><td>429.90 (n/a)</td><td>239.30 (n/a)</td><td>144.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 <b>(+44.73%)</b></td><td>0.10 <b>(+29.37%)</b></td><td>0.10 <b>(+34.65%)</b></td><td>0.06 (+4.52%)</td><td>0.04 <b>(+114.96%)</b></td><td>618.70 (-4.31%)</td><td>426.78 (-15.03%)</td><td>354.80 <b>(-25.74%)</b></td><td>241.20 <b>(-30.91%)</b></td><td>175.79 <b>(+55.71%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>646.60 (n/a)</td><td>502.30 (n/a)</td><td>477.80 (n/a)</td><td>349.10 (n/a)</td><td>112.90 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.20 (+9.94%)</td><td>0.14 (+16.76%)</td><td>0.13 <b>(+46.82%)</b></td><td>0.09 <b>(+24.40%)</b></td><td>0.04 (-16.72%)</td><td>458.80 (-19.61%)</td><td>320.78 (-19.45%)</td><td>304.80 <b>(-31.90%)</b></td><td>206.10 (-9.05%)</td><td>92.86 <b>(-37.35%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>570.70 (n/a)</td><td>398.24 (n/a)</td><td>447.60 (n/a)</td><td>226.60 (n/a)</td><td>148.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.19 (+16.00%)</td><td>0.15 <b>(+32.20%)</b></td><td>0.15 (+19.58%)</td><td>0.09 <b>(+59.44%)</b></td><td>0.04 (-16.86%)</td><td>454.10 <b>(-37.28%)</b></td><td>293.26 <b>(-32.04%)</b></td><td>281.20 (-16.36%)</td><td>211.60 (-13.77%)</td><td>96.39 <b>(-54.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>724.00 (n/a)</td><td>431.50 (n/a)</td><td>336.20 (n/a)</td><td>245.40 (n/a)</td><td>211.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.19 <b>(+73.34%)</b></td><td>0.09 (+12.41%)</td><td>0.08 (-0.09%)</td><td>0.05 <b>(-28.19%)</b></td><td>0.06 <b>(+221.88%)</b></td><td>814.40 <b>(+39.26%)</b></td><td>528.56 (+5.63%)</td><td>540.00 (+0.09%)</td><td>212.60 <b>(-42.31%)</b></td><td>220.83 <b>(+136.94%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>584.80 (n/a)</td><td>500.40 (n/a)</td><td>539.50 (n/a)</td><td>368.50 (n/a)</td><td>93.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 <b>(-38.45%)</b></td><td>0.11 (-8.72%)</td><td>0.10 (+10.77%)</td><td>0.07 (-2.61%)</td><td>0.03 <b>(-54.62%)</b></td><td>567.40 (+2.68%)</td><td>400.40 (-1.68%)</td><td>393.80 (-9.72%)</td><td>296.90 <b>(+62.42%)</b></td><td>112.14 <b>(-28.12%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>552.60 (n/a)</td><td>407.24 (n/a)</td><td>436.20 (n/a)</td><td>182.80 (n/a)</td><td>156.01 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 <b>(+24.21%)</b></td><td>0.13 <b>(+26.28%)</b></td><td>0.14 <b>(+57.41%)</b></td><td>0.06 (-19.23%)</td><td>0.05 <b>(+90.22%)</b></td><td>649.20 <b>(+23.82%)</b></td><td>373.50 (-12.48%)</td><td>294.90 <b>(-36.46%)</b></td><td>236.20 (-19.50%)</td><td>172.79 <b>(+91.47%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>524.30 (n/a)</td><td>426.74 (n/a)</td><td>464.10 (n/a)</td><td>293.40 (n/a)</td><td>90.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 <b>(+34.14%)</b></td><td>0.11 <b>(+27.70%)</b></td><td>0.10 <b>(+21.16%)</b></td><td>0.07 (-6.80%)</td><td>0.05 <b>(+117.09%)</b></td><td>620.10 (+7.28%)</td><td>428.70 (-12.33%)</td><td>421.30 (-17.46%)</td><td>241.10 <b>(-25.45%)</b></td><td>179.12 <b>(+82.58%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>578.00 (n/a)</td><td>489.00 (n/a)</td><td>510.40 (n/a)</td><td>323.40 (n/a)</td><td>98.10 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 (+17.03%)</td><td>0.12 (+18.76%)</td><td>0.13 (+17.19%)</td><td>0.06 (-6.61%)</td><td>0.03 <b>(+31.14%)</b></td><td>539.70 (+7.08%)</td><td>320.98 (-13.03%)</td><td>261.40 (-14.66%)</td><td>239.70 (-14.55%)</td><td>125.26 <b>(+23.25%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>504.00 (n/a)</td><td>369.08 (n/a)</td><td>306.30 (n/a)</td><td>280.50 (n/a)</td><td>101.63 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 <b>(+62.64%)</b></td><td>0.10 <b>(+44.94%)</b></td><td>0.12 <b>(+74.39%)</b></td><td>0.06 (-5.59%)</td><td>0.04 <b>(+337.67%)</b></td><td>575.70 (+5.91%)</td><td>387.88 <b>(-22.23%)</b></td><td>292.90 <b>(-42.66%)</b></td><td>250.40 <b>(-38.52%)</b></td><td>161.65 <b>(+201.16%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>543.60 (n/a)</td><td>498.76 (n/a)</td><td>510.80 (n/a)</td><td>407.30 (n/a)</td><td>53.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 (+17.65%)</td><td>0.11 (+13.51%)</td><td>0.12 <b>(+47.17%)</b></td><td>0.07 (+17.90%)</td><td>0.04 (+0.67%)</td><td>494.70 (-15.19%)</td><td>337.96 (-13.83%)</td><td>278.50 <b>(-32.06%)</b></td><td>204.80 (-15.02%)</td><td>122.50 (-18.32%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>583.30 (n/a)</td><td>392.22 (n/a)</td><td>409.90 (n/a)</td><td>241.00 (n/a)</td><td>149.98 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.17 <b>(+79.31%)</b></td><td>0.11 <b>(+46.08%)</b></td><td>0.08 (+19.50%)</td><td>0.06 (+18.36%)</td><td>0.05 <b>(+171.06%)</b></td><td>554.90 (-15.51%)</td><td>369.94 <b>(-24.46%)</b></td><td>411.00 (-16.33%)</td><td>205.70 <b>(-44.22%)</b></td><td>146.78 <b>(+24.89%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>656.80 (n/a)</td><td>489.72 (n/a)</td><td>491.20 (n/a)</td><td>368.80 (n/a)</td><td>117.53 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.10 <b>(-29.05%)</b></td><td>0.07 <b>(-36.32%)</b></td><td>0.06 <b>(-38.27%)</b></td><td>0.02 <b>(-68.31%)</b></td><td>0.03 (+0.73%)</td><td>1713.90 <b>(+215.58%)</b></td><td>730.70 <b>(+98.98%)</b></td><td>582.50 <b>(+62.03%)</b></td><td>344.80 <b>(+40.91%)</b></td><td>563.36 <b>(+371.87%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>543.10 (n/a)</td><td>367.22 (n/a)</td><td>359.50 (n/a)</td><td>244.70 (n/a)</td><td>119.39 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.12 (-12.74%)</td><td>0.09 (-3.81%)</td><td>0.08 (-9.84%)</td><td>0.06 (+2.18%)</td><td>0.03 (-19.83%)</td><td>606.00 (-2.13%)</td><td>437.64 (+1.76%)</td><td>458.20 (+10.92%)</td><td>284.40 (+14.59%)</td><td>123.14 (-8.59%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>619.20 (n/a)</td><td>430.08 (n/a)</td><td>413.10 (n/a)</td><td>248.20 (n/a)</td><td>134.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.51 (-4.62%)</td><td>0.33 (-3.44%)</td><td>0.29 <b>(-31.66%)</b></td><td>0.21 <b>(+290.88%)</b></td><td>0.12 <b>(-35.35%)</b></td><td>619.10 <b>(-74.42%)</b></td><td>444.00 <b>(-41.70%)</b></td><td>458.50 <b>(+46.35%)</b></td><td>256.60 (+4.86%)</td><td>149.40 <b>(-84.00%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.54 (n/a)</td><td>0.34 (n/a)</td><td>0.42 (n/a)</td><td>0.05 (n/a)</td><td>0.19 (n/a)</td><td>2419.80 (n/a)</td><td>761.64 (n/a)</td><td>313.30 (n/a)</td><td>244.70 (n/a)</td><td>933.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.43 <b>(+50.90%)</b></td><td>0.23 (-6.44%)</td><td>0.21 (-17.69%)</td><td>0.08 <b>(-60.47%)</b></td><td>0.13 <b>(+296.82%)</b></td><td>1671.70 <b>(+152.98%)</b></td><td>767.32 <b>(+42.77%)</b></td><td>629.30 <b>(+21.49%)</b></td><td>301.70 <b>(-33.74%)</b></td><td>529.25 <b>(+588.00%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>660.80 (n/a)</td><td>537.44 (n/a)</td><td>518.00 (n/a)</td><td>455.30 (n/a)</td><td>76.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.42 (+14.71%)</td><td>0.32 <b>(+20.93%)</b></td><td>0.27 (+3.98%)</td><td>0.24 <b>(+38.97%)</b></td><td>0.09 (+15.24%)</td><td>553.50 <b>(-28.04%)</b></td><td>439.78 (-18.38%)</td><td>486.40 (-3.84%)</td><td>311.40 (-12.82%)</td><td>116.71 <b>(-30.06%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>769.20 (n/a)</td><td>538.84 (n/a)</td><td>505.80 (n/a)</td><td>357.20 (n/a)</td><td>166.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.00 (+0.00%)</td><td>0.00 (-5.00%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+6.17%)</td><td>21462.15 (-6.86%)</td><td>13799.88 (+1.12%)</td><td>16400.32 (+4.02%)</td><td>6201.76 (+2.49%)</td><td>6804.02 (-7.10%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23043.86 (n/a)</td><td>13646.80 (n/a)</td><td>15766.04 (n/a)</td><td>6051.20 (n/a)</td><td>7323.76 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+253.14%)</b></td><td>22182.98 (-3.16%)</td><td>15023.07 (-17.03%)</td><td>19052.88 (+2.43%)</td><td>5946.29 <b>(-47.55%)</b></td><td>7271.38 <b>(+50.05%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22906.99 (n/a)</td><td>18105.93 (n/a)</td><td>18600.16 (n/a)</td><td>11337.32 (n/a)</td><td>4846.06 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.09 <b>(-35.83%)</b></td><td>0.08 (-10.75%)</td><td>0.08 (-5.88%)</td><td>0.07 (+0.56%)</td><td>0.01 <b>(-69.49%)</b></td><td>29170.75 (-0.58%)</td><td>26072.67 (+6.36%)</td><td>27287.51 (+6.36%)</td><td>23106.04 <b>(+55.94%)</b></td><td>2767.51 <b>(-52.51%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29339.52 (n/a)</td><td>24512.95 (n/a)</td><td>25656.33 (n/a)</td><td>14817.03 (n/a)</td><td>5827.99 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>2.53 (-14.54%)</td><td>1.51 <b>(-38.71%)</b></td><td>1.35 <b>(-42.53%)</b></td><td>0.32 <b>(-84.25%)</b></td><td>0.92 <b>(+160.75%)</b></td><td>3283.60 <b>(+535.13%)</b></td><td>1190.80 <b>(+175.42%)</b></td><td>774.60 <b>(+73.99%)</b></td><td>414.00 (+17.02%)</td><td>1196.97 <b>(+1849.89%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>2.96 (n/a)</td><td>2.47 (n/a)</td><td>2.36 (n/a)</td><td>2.03 (n/a)</td><td>0.35 (n/a)</td><td>517.00 (n/a)</td><td>432.36 (n/a)</td><td>445.20 (n/a)</td><td>353.80 (n/a)</td><td>61.39 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>2.12 <b>(-36.25%)</b></td><td>1.72 (+2.73%)</td><td>1.69 (-5.33%)</td><td>1.41 <b>(+366.39%)</b></td><td>0.27 <b>(-79.82%)</b></td><td>741.90 <b>(-78.56%)</b></td><td>621.12 <b>(-61.24%)</b></td><td>619.80 (+5.62%)</td><td>493.60 <b>(+56.85%)</b></td><td>95.54 <b>(-94.05%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.33 (n/a)</td><td>1.68 (n/a)</td><td>1.79 (n/a)</td><td>0.30 (n/a)</td><td>1.36 (n/a)</td><td>3460.10 (n/a)</td><td>1602.44 (n/a)</td><td>586.80 (n/a)</td><td>314.70 (n/a)</td><td>1605.80 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>2.53 (+1.06%)</td><td>1.80 (+15.63%)</td><td>1.81 (+3.91%)</td><td>0.98 <b>(+227.37%)</b></td><td>0.64 <b>(-20.11%)</b></td><td>1070.60 <b>(-69.45%)</b></td><td>656.64 <b>(-43.73%)</b></td><td>578.60 (-3.78%)</td><td>415.00 (-1.05%)</td><td>268.28 <b>(-79.54%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>2.50 (n/a)</td><td>1.56 (n/a)</td><td>1.74 (n/a)</td><td>0.30 (n/a)</td><td>0.80 (n/a)</td><td>3504.90 (n/a)</td><td>1167.00 (n/a)</td><td>601.30 (n/a)</td><td>419.40 (n/a)</td><td>1311.32 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.51 (+12.43%)</td><td>1.84 <b>(-20.50%)</b></td><td>1.45 <b>(-38.87%)</b></td><td>1.14 (-9.16%)</td><td>0.96 (+18.54%)</td><td>919.70 (+10.08%)</td><td>664.04 <b>(+30.12%)</b></td><td>724.20 <b>(+63.59%)</b></td><td>298.80 (-11.04%)</td><td>233.77 (+11.63%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.12 (n/a)</td><td>2.31 (n/a)</td><td>2.37 (n/a)</td><td>1.26 (n/a)</td><td>0.81 (n/a)</td><td>835.50 (n/a)</td><td>510.32 (n/a)</td><td>442.70 (n/a)</td><td>335.90 (n/a)</td><td>209.41 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>4.24 (-2.08%)</td><td>2.87 <b>(+28.79%)</b></td><td>2.91 <b>(+43.66%)</b></td><td>1.09 <b>(+95.07%)</b></td><td>1.19 <b>(-30.67%)</b></td><td>1920.70 <b>(-48.74%)</b></td><td>910.48 <b>(-51.03%)</b></td><td>720.40 <b>(-30.39%)</b></td><td>494.60 (+2.13%)</td><td>579.14 <b>(-63.91%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>4.33 (n/a)</td><td>2.23 (n/a)</td><td>2.03 (n/a)</td><td>0.56 (n/a)</td><td>1.72 (n/a)</td><td>3746.70 (n/a)</td><td>1859.08 (n/a)</td><td>1034.90 (n/a)</td><td>484.30 (n/a)</td><td>1604.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>5.27 <b>(+35.25%)</b></td><td>2.99 (-4.32%)</td><td>2.66 (-18.00%)</td><td>0.95 <b>(-48.92%)</b></td><td>1.61 <b>(+98.59%)</b></td><td>2202.00 <b>(+95.77%)</b></td><td>968.36 <b>(+34.63%)</b></td><td>789.40 <b>(+21.95%)</b></td><td>397.60 <b>(-26.06%)</b></td><td>715.71 <b>(+199.92%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.90 (n/a)</td><td>3.13 (n/a)</td><td>3.24 (n/a)</td><td>1.86 (n/a)</td><td>0.81 (n/a)</td><td>1124.80 (n/a)</td><td>719.30 (n/a)</td><td>647.30 (n/a)</td><td>537.70 (n/a)</td><td>238.64 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>4.89 (+10.18%)</td><td>2.58 <b>(-20.98%)</b></td><td>2.58 (-15.19%)</td><td>0.59 <b>(-76.53%)</b></td><td>1.54 <b>(+95.54%)</b></td><td>3527.60 <b>(+325.99%)</b></td><td>1304.04 <b>(+94.64%)</b></td><td>811.80 (+17.91%)</td><td>429.20 (-9.24%)</td><td>1258.62 <b>(+751.48%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>4.43 (n/a)</td><td>3.27 (n/a)</td><td>3.05 (n/a)</td><td>2.53 (n/a)</td><td>0.79 (n/a)</td><td>828.10 (n/a)</td><td>669.96 (n/a)</td><td>688.50 (n/a)</td><td>472.90 (n/a)</td><td>147.82 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.77 <b>(-44.45%)</b></td><td>3.08 (+8.22%)</td><td>3.32 <b>(+24.61%)</b></td><td>1.74 <b>(+199.84%)</b></td><td>0.84 <b>(-67.14%)</b></td><td>1207.10 <b>(-66.65%)</b></td><td>740.24 <b>(-58.45%)</b></td><td>631.80 (-19.75%)</td><td>555.80 <b>(+80.05%)</b></td><td>272.15 <b>(-83.82%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>6.79 (n/a)</td><td>2.84 (n/a)</td><td>2.66 (n/a)</td><td>0.58 (n/a)</td><td>2.57 (n/a)</td><td>3619.40 (n/a)</td><td>1781.50 (n/a)</td><td>787.30 (n/a)</td><td>308.70 (n/a)</td><td>1681.75 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>4.74 (+13.42%)</td><td>2.25 <b>(-33.50%)</b></td><td>2.03 <b>(-44.71%)</b></td><td>0.58 <b>(-67.15%)</b></td><td>1.52 <b>(+55.49%)</b></td><td>3598.50 <b>(+204.36%)</b></td><td>1450.56 <b>(+111.95%)</b></td><td>1034.00 <b>(+80.86%)</b></td><td>442.90 (-11.83%)</td><td>1234.65 <b>(+333.47%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>4.18 (n/a)</td><td>3.38 (n/a)</td><td>3.67 (n/a)</td><td>1.77 (n/a)</td><td>0.98 (n/a)</td><td>1182.30 (n/a)</td><td>684.40 (n/a)</td><td>571.70 (n/a)</td><td>502.30 (n/a)</td><td>284.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.60 <b>(-35.36%)</b></td><td>2.03 <b>(-37.71%)</b></td><td>1.51 <b>(-46.73%)</b></td><td>0.59 <b>(-32.24%)</b></td><td>1.38 <b>(-23.64%)</b></td><td>3559.90 <b>(+47.59%)</b></td><td>1620.30 <b>(+68.67%)</b></td><td>1393.00 <b>(+87.74%)</b></td><td>583.20 <b>(+54.69%)</b></td><td>1225.49 <b>(+47.52%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>5.56 (n/a)</td><td>3.27 (n/a)</td><td>2.83 (n/a)</td><td>0.87 (n/a)</td><td>1.81 (n/a)</td><td>2412.10 (n/a)</td><td>960.62 (n/a)</td><td>742.00 (n/a)</td><td>377.00 (n/a)</td><td>830.75 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>4.06 <b>(-20.93%)</b></td><td>3.08 <b>(-29.95%)</b></td><td>3.90 (-4.53%)</td><td>1.68 <b>(-56.58%)</b></td><td>1.27 <b>(+106.57%)</b></td><td>2492.70 <b>(+130.32%)</b></td><td>1620.08 <b>(+67.25%)</b></td><td>1074.40 (+4.75%)</td><td>1032.70 <b>(+26.46%)</b></td><td>783.50 <b>(+505.69%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>5.14 (n/a)</td><td>4.40 (n/a)</td><td>4.09 (n/a)</td><td>3.88 (n/a)</td><td>0.61 (n/a)</td><td>1082.30 (n/a)</td><td>968.68 (n/a)</td><td>1025.70 (n/a)</td><td>816.60 (n/a)</td><td>129.36 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>7.46 (-0.74%)</td><td>3.12 <b>(-53.55%)</b></td><td>1.67 <b>(-77.18%)</b></td><td>1.10 <b>(-73.20%)</b></td><td>2.74 <b>(+86.18%)</b></td><td>3821.70 <b>(+273.14%)</b></td><td>2299.32 <b>(+248.48%)</b></td><td>2509.90 <b>(+338.26%)</b></td><td>562.10 (+0.75%)</td><td>1482.61 <b>(+627.07%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>7.52 (n/a)</td><td>6.72 (n/a)</td><td>7.32 (n/a)</td><td>4.10 (n/a)</td><td>1.47 (n/a)</td><td>1024.20 (n/a)</td><td>659.82 (n/a)</td><td>572.70 (n/a)</td><td>557.90 (n/a)</td><td>203.91 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>7.70 (+0.29%)</td><td>3.97 <b>(-36.89%)</b></td><td>3.93 <b>(-38.62%)</b></td><td>1.17 <b>(-70.08%)</b></td><td>2.37 <b>(+53.41%)</b></td><td>3577.70 <b>(+234.24%)</b></td><td>1521.12 <b>(+114.91%)</b></td><td>1066.00 <b>(+62.92%)</b></td><td>545.00 (-0.29%)</td><td>1186.92 <b>(+451.02%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>7.67 (n/a)</td><td>6.30 (n/a)</td><td>6.41 (n/a)</td><td>3.92 (n/a)</td><td>1.55 (n/a)</td><td>1070.40 (n/a)</td><td>707.80 (n/a)</td><td>654.30 (n/a)</td><td>546.60 (n/a)</td><td>215.40 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>8.99 (-4.58%)</td><td>5.65 <b>(+25.12%)</b></td><td>7.39 <b>(+73.68%)</b></td><td>1.16 (+1.77%)</td><td>3.88 (+9.09%)</td><td>3626.90 (-1.74%)</td><td>1497.88 (-18.84%)</td><td>567.20 <b>(-42.43%)</b></td><td>466.80 (+4.80%)</td><td>1437.60 (-9.98%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>9.42 (n/a)</td><td>4.52 (n/a)</td><td>4.26 (n/a)</td><td>1.14 (n/a)</td><td>3.56 (n/a)</td><td>3691.00 (n/a)</td><td>1845.64 (n/a)</td><td>985.20 (n/a)</td><td>445.40 (n/a)</td><td>1597.00 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>10.48 <b>(+20.95%)</b></td><td>7.08 (+6.43%)</td><td>6.75 (+0.78%)</td><td>1.23 <b>(-68.69%)</b></td><td>3.79 <b>(+118.81%)</b></td><td>3402.50 <b>(+219.42%)</b></td><td>1094.04 <b>(+61.84%)</b></td><td>621.80 (-0.78%)</td><td>400.40 (-17.31%)</td><td>1295.72 <b>(+473.05%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>8.66 (n/a)</td><td>6.66 (n/a)</td><td>6.69 (n/a)</td><td>3.94 (n/a)</td><td>1.73 (n/a)</td><td>1065.20 (n/a)</td><td>676.02 (n/a)</td><td>626.70 (n/a)</td><td>484.20 (n/a)</td><td>226.11 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>11.32 <b>(+36.52%)</b></td><td>5.76 (+2.39%)</td><td>3.82 <b>(-43.18%)</b></td><td>3.36 <b>(+183.65%)</b></td><td>3.37 <b>(+23.46%)</b></td><td>1246.60 <b>(-64.74%)</b></td><td>898.28 <b>(-26.45%)</b></td><td>1097.60 <b>(+75.98%)</b></td><td>370.60 <b>(-26.76%)</b></td><td>376.90 <b>(-70.99%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>8.29 (n/a)</td><td>5.62 (n/a)</td><td>6.73 (n/a)</td><td>1.19 (n/a)</td><td>2.73 (n/a)</td><td>3535.80 (n/a)</td><td>1221.26 (n/a)</td><td>623.70 (n/a)</td><td>506.00 (n/a)</td><td>1299.10 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>1.52 <b>(-20.28%)</b></td><td>1.16 <b>(-23.71%)</b></td><td>1.08 <b>(-31.09%)</b></td><td>0.89 (-19.26%)</td><td>0.29 (-6.73%)</td><td>589.90 <b>(+23.85%)</b></td><td>475.68 <b>(+32.73%)</b></td><td>483.80 <b>(+45.15%)</b></td><td>345.30 <b>(+25.43%)</b></td><td>113.13 <b>(+45.25%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>1.90 (n/a)</td><td>1.52 (n/a)</td><td>1.57 (n/a)</td><td>1.10 (n/a)</td><td>0.31 (n/a)</td><td>476.30 (n/a)</td><td>358.38 (n/a)</td><td>333.30 (n/a)</td><td>275.30 (n/a)</td><td>77.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>2.76 (-0.78%)</td><td>1.64 <b>(-21.79%)</b></td><td>1.73 (-19.03%)</td><td>0.30 <b>(-80.15%)</b></td><td>0.88 <b>(+62.84%)</b></td><td>3480.60 <b>(+403.85%)</b></td><td>1140.32 <b>(+115.81%)</b></td><td>607.30 <b>(+23.51%)</b></td><td>379.40 (+0.80%)</td><td>1312.26 <b>(+855.84%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>2.79 (n/a)</td><td>2.10 (n/a)</td><td>2.13 (n/a)</td><td>1.52 (n/a)</td><td>0.54 (n/a)</td><td>690.80 (n/a)</td><td>528.40 (n/a)</td><td>491.70 (n/a)</td><td>376.40 (n/a)</td><td>137.29 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>3.60 (+0.85%)</td><td>1.78 <b>(-20.64%)</b></td><td>0.60 <b>(-76.52%)</b></td><td>0.56 (-7.32%)</td><td>1.63 (+15.72%)</td><td>3713.40 (+7.89%)</td><td>2382.18 <b>(+54.71%)</b></td><td>3508.40 <b>(+325.88%)</b></td><td>583.30 (-0.85%)</td><td>1640.39 <b>(+29.14%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.57 (n/a)</td><td>2.24 (n/a)</td><td>2.55 (n/a)</td><td>0.61 (n/a)</td><td>1.41 (n/a)</td><td>3441.70 (n/a)</td><td>1539.74 (n/a)</td><td>823.80 (n/a)</td><td>588.30 (n/a)</td><td>1270.21 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>1.61 (-7.37%)</td><td>1.12 (+7.02%)</td><td>1.44 <b>(+46.95%)</b></td><td>0.26 <b>(-49.00%)</b></td><td>0.58 <b>(+29.73%)</b></td><td>2048.30 <b>(+96.07%)</b></td><td>750.62 <b>(+27.97%)</b></td><td>364.50 <b>(-31.96%)</b></td><td>324.80 (+7.94%)</td><td>738.79 <b>(+167.34%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>1.74 (n/a)</td><td>1.05 (n/a)</td><td>0.98 (n/a)</td><td>0.50 (n/a)</td><td>0.45 (n/a)</td><td>1044.70 (n/a)</td><td>586.54 (n/a)</td><td>535.70 (n/a)</td><td>300.90 (n/a)</td><td>276.35 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (+10.75%)</td><td>0.09 (+11.08%)</td><td>0.07 (-7.58%)</td><td>0.06 <b>(+261.52%)</b></td><td>0.03 <b>(-21.55%)</b></td><td>534.60 <b>(-72.34%)</b></td><td>405.68 <b>(-40.06%)</b></td><td>465.50 (+8.21%)</td><td>235.80 (-9.72%)</td><td>128.67 <b>(-81.82%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1932.70 (n/a)</td><td>676.78 (n/a)</td><td>430.20 (n/a)</td><td>261.20 (n/a)</td><td>707.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.14 (-12.16%)</td><td>0.09 (+0.57%)</td><td>0.08 (+10.78%)</td><td>0.05 <b>(+79.68%)</b></td><td>0.04 <b>(-26.25%)</b></td><td>598.10 <b>(-44.34%)</b></td><td>423.16 (-16.48%)</td><td>429.00 (-9.72%)</td><td>232.10 (+13.83%)</td><td>156.96 <b>(-53.60%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1074.60 (n/a)</td><td>506.66 (n/a)</td><td>475.20 (n/a)</td><td>203.90 (n/a)</td><td>338.30 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.28 (+8.11%)</td><td>0.22 (+6.87%)</td><td>0.22 (-4.60%)</td><td>0.14 (+0.85%)</td><td>0.05 (-14.84%)</td><td>468.40 (-0.85%)</td><td>318.08 (-8.83%)</td><td>294.40 (+4.84%)</td><td>234.40 (-7.46%)</td><td>88.74 <b>(-21.11%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>472.40 (n/a)</td><td>348.88 (n/a)</td><td>280.80 (n/a)</td><td>253.30 (n/a)</td><td>112.50 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.24 (-6.75%)</td><td>0.16 (-3.93%)</td><td>0.13 (-12.48%)</td><td>0.13 (+14.46%)</td><td>0.05 (-19.39%)</td><td>519.30 (-12.62%)</td><td>437.38 (+0.71%)</td><td>496.30 (+14.25%)</td><td>276.90 (+7.24%)</td><td>102.47 <b>(-24.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>594.30 (n/a)</td><td>434.30 (n/a)</td><td>434.40 (n/a)</td><td>258.20 (n/a)</td><td>135.84 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.15 <b>(-43.60%)</b></td><td>0.10 <b>(-38.28%)</b></td><td>0.11 <b>(-28.06%)</b></td><td>0.03 <b>(-69.07%)</b></td><td>0.04 <b>(-38.04%)</b></td><td>2113.70 <b>(+223.34%)</b></td><td>859.24 <b>(+91.27%)</b></td><td>582.00 <b>(+39.00%)</b></td><td>440.70 <b>(+77.34%)</b></td><td>704.39 <b>(+285.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>653.70 (n/a)</td><td>449.24 (n/a)</td><td>418.70 (n/a)</td><td>248.50 (n/a)</td><td>182.80 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.45 <b>(+43.86%)</b></td><td>0.32 <b>(+23.64%)</b></td><td>0.31 (+15.90%)</td><td>0.18 (-12.45%)</td><td>0.11 <b>(+156.61%)</b></td><td>721.00 (+14.23%)</td><td>453.74 (-12.19%)</td><td>424.50 (-13.72%)</td><td>288.50 <b>(-30.50%)</b></td><td>171.62 <b>(+101.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>631.20 (n/a)</td><td>516.72 (n/a)</td><td>492.00 (n/a)</td><td>415.10 (n/a)</td><td>85.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.54 (+11.91%)</td><td>0.32 (-4.97%)</td><td>0.29 (-11.19%)</td><td>0.23 (+2.44%)</td><td>0.13 <b>(+29.32%)</b></td><td>575.90 (-2.37%)</td><td>449.46 (+8.54%)</td><td>453.10 (+12.60%)</td><td>240.90 (-10.65%)</td><td>138.01 (+13.15%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>589.90 (n/a)</td><td>414.10 (n/a)</td><td>402.40 (n/a)</td><td>269.60 (n/a)</td><td>121.97 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.50 <b>(+21.69%)</b></td><td>0.37 (+13.77%)</td><td>0.36 (+15.81%)</td><td>0.23 (-13.67%)</td><td>0.11 <b>(+105.24%)</b></td><td>568.20 (+15.84%)</td><td>388.34 (-6.50%)</td><td>361.20 (-13.67%)</td><td>260.00 (-17.83%)</td><td>127.35 <b>(+99.42%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>490.50 (n/a)</td><td>415.32 (n/a)</td><td>418.40 (n/a)</td><td>316.40 (n/a)</td><td>63.86 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:32:39</td><td>0.06 (-9.37%)</td><td>0.05 (+5.11%)</td><td>0.05 (-0.36%)</td><td>0.03 (+6.56%)</td><td>0.01 <b>(-24.79%)</b></td><td>558.90 (-6.16%)</td><td>343.02 (-8.75%)</td><td>299.10 (+0.37%)</td><td>273.70 (+10.32%)</td><td>121.28 (-19.00%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>595.60 (n/a)</td><td>375.90 (n/a)</td><td>298.00 (n/a)</td><td>248.10 (n/a)</td><td>149.72 (n/a)</td>
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
