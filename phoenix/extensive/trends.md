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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (+0.88%)</td><td>0.02 <b>(+28.06%)</b></td><td>0.02 <b>(+52.75%)</b></td><td>0.01 (+0.11%)</td><td>0.00 (-7.00%)</td><td>491.50 (-0.10%)</td><td>318.08 <b>(-22.26%)</b></td><td>294.90 <b>(-34.54%)</b></td><td>239.80 (-0.87%)</td><td>100.08 (+0.76%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>492.00 (n/a)</td><td>409.14 (n/a)</td><td>450.50 (n/a)</td><td>241.90 (n/a)</td><td>99.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(+24.87%)</b></td><td>0.02 (-3.25%)</td><td>0.01 (-6.38%)</td><td>0.01 <b>(-52.64%)</b></td><td>0.01 <b>(+86.53%)</b></td><td>1186.20 <b>(+111.14%)</b></td><td>547.50 <b>(+30.63%)</b></td><td>451.50 (+6.81%)</td><td>247.40 (-19.91%)</td><td>376.64 <b>(+238.16%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>561.80 (n/a)</td><td>419.12 (n/a)</td><td>422.70 (n/a)</td><td>308.90 (n/a)</td><td>111.38 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (+10.00%)</td><td>0.02 <b>(+27.93%)</b></td><td>0.02 <b>(+22.74%)</b></td><td>0.02 <b>(+72.12%)</b></td><td>0.00 <b>(-47.26%)</b></td><td>285.20 <b>(-41.89%)</b></td><td>251.82 <b>(-25.59%)</b></td><td>249.30 (-18.53%)</td><td>225.60 (-9.11%)</td><td>26.40 <b>(-72.76%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>490.80 (n/a)</td><td>338.42 (n/a)</td><td>306.00 (n/a)</td><td>248.20 (n/a)</td><td>96.89 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (+6.97%)</td><td>0.02 <b>(+22.11%)</b></td><td>0.02 (+18.22%)</td><td>0.02 <b>(+55.40%)</b></td><td>0.00 <b>(-44.24%)</b></td><td>305.10 <b>(-35.65%)</b></td><td>249.30 <b>(-22.54%)</b></td><td>249.70 (-15.41%)</td><td>220.00 (-6.54%)</td><td>34.34 <b>(-65.60%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>474.10 (n/a)</td><td>321.84 (n/a)</td><td>295.20 (n/a)</td><td>235.40 (n/a)</td><td>99.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (-14.20%)</td><td>0.01 (-8.23%)</td><td>0.01 (-9.44%)</td><td>0.01 (+3.61%)</td><td>0.00 <b>(-23.93%)</b></td><td>644.40 (-3.49%)</td><td>473.10 (+5.73%)</td><td>479.50 (+10.43%)</td><td>296.80 (+16.58%)</td><td>125.02 (-14.80%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>667.70 (n/a)</td><td>447.48 (n/a)</td><td>434.20 (n/a)</td><td>254.60 (n/a)</td><td>146.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (-2.54%)</td><td>0.02 (-3.32%)</td><td>0.01 (+7.08%)</td><td>0.01 (-7.79%)</td><td>0.01 (+5.30%)</td><td>832.10 (+8.45%)</td><td>491.10 (+7.36%)</td><td>449.00 (-6.61%)</td><td>249.40 (+2.63%)</td><td>242.22 (+17.88%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>767.30 (n/a)</td><td>457.42 (n/a)</td><td>480.80 (n/a)</td><td>243.00 (n/a)</td><td>205.48 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (+6.42%)</td><td>0.04 (-10.20%)</td><td>0.04 <b>(-20.77%)</b></td><td>0.02 (+7.28%)</td><td>0.01 (+1.45%)</td><td>501.40 (-6.79%)</td><td>375.68 (+10.89%)</td><td>342.70 <b>(+26.22%)</b></td><td>232.80 (-6.02%)</td><td>115.81 (-5.70%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.90 (n/a)</td><td>338.78 (n/a)</td><td>271.50 (n/a)</td><td>247.70 (n/a)</td><td>122.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (-4.07%)</td><td>0.04 (-6.46%)</td><td>0.04 (-16.75%)</td><td>0.02 (-11.28%)</td><td>0.01 (-17.75%)</td><td>697.00 (+12.71%)</td><td>366.02 (+5.07%)</td><td>293.00 <b>(+20.13%)</b></td><td>229.30 (+4.23%)</td><td>188.12 (+9.16%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>618.40 (n/a)</td><td>348.36 (n/a)</td><td>243.90 (n/a)</td><td>220.00 (n/a)</td><td>172.34 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (+9.50%)</td><td>0.03 (+7.17%)</td><td>0.03 <b>(-34.85%)</b></td><td>0.03 <b>(+333.55%)</b></td><td>0.01 <b>(-44.89%)</b></td><td>451.60 <b>(-76.94%)</b></td><td>375.36 <b>(-44.38%)</b></td><td>432.40 <b>(+53.44%)</b></td><td>245.20 (-8.68%)</td><td>90.76 <b>(-87.58%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1958.00 (n/a)</td><td>674.90 (n/a)</td><td>281.80 (n/a)</td><td>268.50 (n/a)</td><td>730.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 <b>(-26.13%)</b></td><td>0.03 <b>(-24.93%)</b></td><td>0.03 <b>(-35.33%)</b></td><td>0.02 (+0.97%)</td><td>0.01 <b>(-37.92%)</b></td><td>553.30 (-0.97%)</td><td>433.04 <b>(+23.48%)</b></td><td>439.50 <b>(+54.64%)</b></td><td>245.10 <b>(+35.34%)</b></td><td>116.09 <b>(-23.52%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>558.70 (n/a)</td><td>350.70 (n/a)</td><td>284.20 (n/a)</td><td>181.10 (n/a)</td><td>151.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (-2.78%)</td><td>0.03 (-17.65%)</td><td>0.03 <b>(-31.90%)</b></td><td>0.01 <b>(-64.04%)</b></td><td>0.02 (+1.89%)</td><td>1892.60 <b>(+178.08%)</b></td><td>684.76 <b>(+61.87%)</b></td><td>477.90 <b>(+46.82%)</b></td><td>238.30 (+2.85%)</td><td>683.58 <b>(+215.97%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>680.60 (n/a)</td><td>423.04 (n/a)</td><td>325.50 (n/a)</td><td>231.70 (n/a)</td><td>216.34 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (+18.50%)</td><td>0.03 <b>(-23.84%)</b></td><td>0.02 <b>(-40.76%)</b></td><td>0.02 <b>(-37.27%)</b></td><td>0.01 <b>(+119.84%)</b></td><td>707.70 <b>(+59.39%)</b></td><td>549.60 <b>(+48.08%)</b></td><td>589.40 <b>(+68.79%)</b></td><td>245.80 (-15.62%)</td><td>182.71 <b>(+169.50%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>444.00 (n/a)</td><td>371.16 (n/a)</td><td>349.20 (n/a)</td><td>291.30 (n/a)</td><td>67.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (-12.82%)</td><td>0.06 <b>(-20.49%)</b></td><td>0.04 <b>(-44.43%)</b></td><td>0.03 <b>(-20.29%)</b></td><td>0.03 <b>(+23.79%)</b></td><td>704.90 <b>(+25.45%)</b></td><td>481.00 <b>(+37.04%)</b></td><td>564.50 <b>(+79.95%)</b></td><td>258.50 (+14.69%)</td><td>203.24 <b>(+60.11%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>561.90 (n/a)</td><td>350.98 (n/a)</td><td>313.70 (n/a)</td><td>225.40 (n/a)</td><td>126.94 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (-16.90%)</td><td>0.06 (-16.26%)</td><td>0.05 <b>(-32.32%)</b></td><td>0.04 (-0.75%)</td><td>0.02 <b>(-28.11%)</b></td><td>572.20 (+0.76%)</td><td>428.82 (+12.24%)</td><td>501.20 <b>(+47.76%)</b></td><td>250.60 <b>(+20.31%)</b></td><td>138.80 (-17.49%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>567.90 (n/a)</td><td>382.04 (n/a)</td><td>339.20 (n/a)</td><td>208.30 (n/a)</td><td>168.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (+7.06%)</td><td>0.08 (+16.15%)</td><td>0.09 <b>(+43.55%)</b></td><td>0.05 (+8.19%)</td><td>0.03 <b>(+29.79%)</b></td><td>500.20 (-7.58%)</td><td>347.46 (-10.30%)</td><td>273.40 <b>(-30.33%)</b></td><td>231.30 (-6.58%)</td><td>139.09 (+16.83%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>541.20 (n/a)</td><td>387.36 (n/a)</td><td>392.40 (n/a)</td><td>247.60 (n/a)</td><td>119.05 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (-6.40%)</td><td>0.07 (+0.84%)</td><td>0.08 <b>(+21.09%)</b></td><td>0.04 <b>(-27.97%)</b></td><td>0.02 <b>(+29.02%)</b></td><td>645.70 <b>(+38.83%)</b></td><td>369.28 (+6.10%)</td><td>289.50 (-17.40%)</td><td>259.70 (+6.83%)</td><td>162.53 <b>(+92.75%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>465.10 (n/a)</td><td>348.06 (n/a)</td><td>350.50 (n/a)</td><td>243.10 (n/a)</td><td>84.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 <b>(+24.40%)</b></td><td>0.07 (+3.30%)</td><td>0.05 <b>(-24.42%)</b></td><td>0.05 (+5.13%)</td><td>0.03 <b>(+65.73%)</b></td><td>533.70 (-4.87%)</td><td>406.76 (+2.41%)</td><td>489.60 <b>(+32.29%)</b></td><td>239.50 (-19.63%)</td><td>136.16 <b>(+27.88%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>561.00 (n/a)</td><td>397.20 (n/a)</td><td>370.10 (n/a)</td><td>298.00 (n/a)</td><td>106.47 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (-11.67%)</td><td>0.06 <b>(-24.89%)</b></td><td>0.05 <b>(-51.13%)</b></td><td>0.04 (-17.16%)</td><td>0.02 (-16.12%)</td><td>622.50 <b>(+20.71%)</b></td><td>472.60 <b>(+32.62%)</b></td><td>537.10 <b>(+104.61%)</b></td><td>288.60 (+13.22%)</td><td>153.57 (+15.29%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>515.70 (n/a)</td><td>356.36 (n/a)</td><td>262.50 (n/a)</td><td>254.90 (n/a)</td><td>133.20 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (+0.35%)</td><td>0.13 (-11.32%)</td><td>0.12 <b>(-27.34%)</b></td><td>0.09 (-7.41%)</td><td>0.04 <b>(+26.37%)</b></td><td>547.50 (+8.01%)</td><td>398.86 (+15.35%)</td><td>422.10 <b>(+37.63%)</b></td><td>284.10 (-0.35%)</td><td>112.46 <b>(+23.16%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>506.90 (n/a)</td><td>345.78 (n/a)</td><td>306.70 (n/a)</td><td>285.10 (n/a)</td><td>91.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.21 <b>(+24.26%)</b></td><td>0.11 <b>(-21.59%)</b></td><td>0.09 <b>(-45.21%)</b></td><td>0.08 (-10.08%)</td><td>0.05 <b>(+67.47%)</b></td><td>596.80 (+11.22%)</td><td>498.22 <b>(+36.78%)</b></td><td>556.00 <b>(+82.47%)</b></td><td>236.50 (-19.53%)</td><td>148.46 <b>(+44.25%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>536.60 (n/a)</td><td>364.24 (n/a)</td><td>304.70 (n/a)</td><td>293.90 (n/a)</td><td>102.92 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.19 (-6.56%)</td><td>0.14 (-13.31%)</td><td>0.15 (-7.30%)</td><td>0.10 (-15.89%)</td><td>0.04 <b>(+32.14%)</b></td><td>503.00 (+18.88%)</td><td>371.64 <b>(+20.66%)</b></td><td>320.20 (+7.85%)</td><td>255.10 (+7.05%)</td><td>120.22 <b>(+72.15%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>423.10 (n/a)</td><td>308.00 (n/a)</td><td>296.90 (n/a)</td><td>238.30 (n/a)</td><td>69.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (-10.59%)</td><td>0.10 <b>(-26.89%)</b></td><td>0.11 <b>(-28.06%)</b></td><td>0.02 <b>(-73.55%)</b></td><td>0.05 (+12.38%)</td><td>2111.10 <b>(+278.06%)</b></td><td>761.36 <b>(+95.96%)</b></td><td>439.80 <b>(+39.00%)</b></td><td>294.70 (+11.84%)</td><td>760.85 <b>(+428.32%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>558.40 (n/a)</td><td>388.52 (n/a)</td><td>316.40 (n/a)</td><td>263.50 (n/a)</td><td>144.01 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.18 (-11.78%)</td><td>0.14 (-11.54%)</td><td>0.14 (-12.29%)</td><td>0.08 (-14.06%)</td><td>0.04 (-4.59%)</td><td>620.90 (+16.36%)</td><td>397.24 (+14.43%)</td><td>343.50 (+14.01%)</td><td>279.50 (+13.34%)</td><td>141.57 <b>(+22.59%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>533.60 (n/a)</td><td>347.16 (n/a)</td><td>301.30 (n/a)</td><td>246.60 (n/a)</td><td>115.48 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.23 <b>(+37.06%)</b></td><td>0.17 <b>(+42.78%)</b></td><td>0.18 <b>(+61.37%)</b></td><td>0.09 (+4.21%)</td><td>0.06 <b>(+77.09%)</b></td><td>536.60 (-4.04%)</td><td>335.62 <b>(-25.25%)</b></td><td>267.40 <b>(-38.04%)</b></td><td>209.40 <b>(-27.06%)</b></td><td>137.20 <b>(+27.05%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>559.20 (n/a)</td><td>449.02 (n/a)</td><td>431.60 (n/a)</td><td>287.10 (n/a)</td><td>107.99 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (+5.81%)</td><td>0.01 (+14.99%)</td><td>0.01 (-7.80%)</td><td>0.01 <b>(+272.43%)</b></td><td>0.00 <b>(-40.09%)</b></td><td>509.00 <b>(-73.15%)</b></td><td>358.08 <b>(-51.53%)</b></td><td>293.80 (+8.45%)</td><td>224.00 (-5.49%)</td><td>132.03 <b>(-81.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1895.70 (n/a)</td><td>738.84 (n/a)</td><td>270.90 (n/a)</td><td>237.00 (n/a)</td><td>733.23 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (-2.98%)</td><td>0.01 <b>(-25.76%)</b></td><td>0.00 <b>(-53.49%)</b></td><td>0.00 <b>(-23.58%)</b></td><td>0.00 <b>(+27.54%)</b></td><td>628.00 <b>(+30.86%)</b></td><td>452.90 <b>(+47.71%)</b></td><td>524.90 <b>(+115.03%)</b></td><td>237.60 (+3.08%)</td><td>188.06 <b>(+75.71%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>479.90 (n/a)</td><td>306.62 (n/a)</td><td>244.10 (n/a)</td><td>230.50 (n/a)</td><td>107.03 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (+16.89%)</td><td>0.01 (-4.02%)</td><td>0.01 <b>(-21.00%)</b></td><td>0.00 (-3.58%)</td><td>0.00 <b>(+46.15%)</b></td><td>574.00 (+3.70%)</td><td>434.52 (+10.02%)</td><td>491.40 <b>(+26.58%)</b></td><td>214.10 (-14.46%)</td><td>140.38 <b>(+25.56%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>553.50 (n/a)</td><td>394.94 (n/a)</td><td>388.20 (n/a)</td><td>250.30 (n/a)</td><td>111.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (-10.44%)</td><td>0.01 (-0.48%)</td><td>0.01 (-2.63%)</td><td>0.00 (+9.69%)</td><td>0.00 <b>(-25.16%)</b></td><td>542.00 (-8.83%)</td><td>469.90 (-2.87%)</td><td>515.50 (+2.71%)</td><td>295.90 (+11.66%)</td><td>101.01 <b>(-21.97%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>594.50 (n/a)</td><td>483.80 (n/a)</td><td>501.90 (n/a)</td><td>265.00 (n/a)</td><td>129.46 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (-1.87%)</td><td>0.01 (+3.85%)</td><td>0.01 (+8.56%)</td><td>0.00 <b>(+123.70%)</b></td><td>0.00 <b>(-31.78%)</b></td><td>602.80 <b>(-55.30%)</b></td><td>446.42 <b>(-23.23%)</b></td><td>409.70 (-7.89%)</td><td>281.10 (+1.92%)</td><td>124.30 <b>(-71.57%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1348.50 (n/a)</td><td>581.48 (n/a)</td><td>444.80 (n/a)</td><td>275.80 (n/a)</td><td>437.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 <b>(+26.13%)</b></td><td>0.01 (-5.77%)</td><td>0.01 <b>(-24.32%)</b></td><td>0.00 (-11.87%)</td><td>0.00 <b>(+64.67%)</b></td><td>685.50 (+13.47%)</td><td>469.88 (+12.57%)</td><td>482.80 <b>(+32.13%)</b></td><td>256.00 <b>(-20.72%)</b></td><td>160.57 <b>(+41.08%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>604.10 (n/a)</td><td>417.40 (n/a)</td><td>365.40 (n/a)</td><td>322.90 (n/a)</td><td>113.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 <b>(+31.21%)</b></td><td>0.02 (+10.12%)</td><td>0.02 (+2.66%)</td><td>0.01 (+11.80%)</td><td>0.01 <b>(+60.42%)</b></td><td>471.00 (-10.56%)</td><td>339.60 (-5.57%)</td><td>311.80 (-2.59%)</td><td>193.90 <b>(-23.78%)</b></td><td>110.87 (+7.23%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>526.60 (n/a)</td><td>359.64 (n/a)</td><td>320.10 (n/a)</td><td>254.40 (n/a)</td><td>103.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 <b>(+20.45%)</b></td><td>0.01 (+14.42%)</td><td>0.01 (+3.26%)</td><td>0.01 <b>(+73.84%)</b></td><td>0.01 <b>(+20.24%)</b></td><td>587.60 <b>(-42.48%)</b></td><td>488.86 (-16.17%)</td><td>546.90 (-3.15%)</td><td>191.90 (-17.00%)</td><td>166.98 <b>(-41.61%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1021.60 (n/a)</td><td>583.18 (n/a)</td><td>564.70 (n/a)</td><td>231.20 (n/a)</td><td>285.96 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (+6.59%)</td><td>0.02 <b>(+40.33%)</b></td><td>0.02 <b>(+111.04%)</b></td><td>0.01 <b>(+278.00%)</b></td><td>0.01 <b>(-23.58%)</b></td><td>515.10 <b>(-73.54%)</b></td><td>331.34 <b>(-53.44%)</b></td><td>257.20 <b>(-52.62%)</b></td><td>215.50 (-6.18%)</td><td>131.40 <b>(-81.40%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1947.00 (n/a)</td><td>711.70 (n/a)</td><td>542.90 (n/a)</td><td>229.70 (n/a)</td><td>706.38 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(-20.28%)</b></td><td>0.01 <b>(-21.67%)</b></td><td>0.01 <b>(-32.00%)</b></td><td>0.01 (-5.75%)</td><td>0.00 <b>(-37.49%)</b></td><td>551.20 (+6.10%)</td><td>430.82 <b>(+22.45%)</b></td><td>445.20 <b>(+47.03%)</b></td><td>294.50 <b>(+25.43%)</b></td><td>93.08 <b>(-20.89%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.50 (n/a)</td><td>351.82 (n/a)</td><td>302.80 (n/a)</td><td>234.80 (n/a)</td><td>117.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 <b>(+31.32%)</b></td><td>0.01 <b>(+74.03%)</b></td><td>0.01 <b>(+42.02%)</b></td><td>0.01 <b>(+281.97%)</b></td><td>0.01 <b>(+20.06%)</b></td><td>631.50 <b>(-73.82%)</b></td><td>430.92 <b>(-56.67%)</b></td><td>465.60 <b>(-29.58%)</b></td><td>209.90 <b>(-23.84%)</b></td><td>194.07 <b>(-76.66%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2412.00 (n/a)</td><td>994.56 (n/a)</td><td>661.20 (n/a)</td><td>275.60 (n/a)</td><td>831.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(-22.85%)</b></td><td>0.01 (-1.41%)</td><td>0.01 (-4.00%)</td><td>0.01 <b>(+29.71%)</b></td><td>0.00 <b>(-55.25%)</b></td><td>494.60 <b>(-22.91%)</b></td><td>436.34 (-7.44%)</td><td>463.60 (+4.16%)</td><td>319.10 <b>(+29.61%)</b></td><td>69.07 <b>(-56.66%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>641.60 (n/a)</td><td>471.40 (n/a)</td><td>445.10 (n/a)</td><td>246.20 (n/a)</td><td>159.37 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 <b>(+35.98%)</b></td><td>0.03 (-3.44%)</td><td>0.03 (-18.27%)</td><td>0.02 <b>(-37.83%)</b></td><td>0.01 <b>(+136.87%)</b></td><td>676.00 <b>(+60.84%)</b></td><td>410.90 (+18.56%)</td><td>390.60 <b>(+22.33%)</b></td><td>199.60 <b>(-26.46%)</b></td><td>180.20 <b>(+164.94%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>420.30 (n/a)</td><td>346.58 (n/a)</td><td>319.30 (n/a)</td><td>271.40 (n/a)</td><td>68.02 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 <b>(-28.00%)</b></td><td>0.03 (+10.43%)</td><td>0.04 <b>(+42.80%)</b></td><td>0.02 <b>(+259.49%)</b></td><td>0.01 <b>(-57.56%)</b></td><td>556.30 <b>(-72.18%)</b></td><td>331.12 <b>(-50.19%)</b></td><td>282.60 <b>(-29.96%)</b></td><td>256.90 <b>(+38.86%)</b></td><td>126.34 <b>(-83.34%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1999.90 (n/a)</td><td>664.74 (n/a)</td><td>403.50 (n/a)</td><td>185.00 (n/a)</td><td>758.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 <b>(-33.64%)</b></td><td>0.03 (-14.88%)</td><td>0.02 <b>(-31.03%)</b></td><td>0.02 (+0.86%)</td><td>0.01 <b>(-42.48%)</b></td><td>582.00 (-0.85%)</td><td>400.06 (+5.22%)</td><td>428.30 <b>(+44.99%)</b></td><td>252.10 <b>(+50.69%)</b></td><td>138.74 <b>(-24.45%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>587.00 (n/a)</td><td>380.22 (n/a)</td><td>295.40 (n/a)</td><td>167.30 (n/a)</td><td>183.65 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (-19.98%)</td><td>0.02 <b>(-31.86%)</b></td><td>0.02 <b>(-21.68%)</b></td><td>0.01 <b>(-75.96%)</b></td><td>0.01 <b>(+35.28%)</b></td><td>1935.00 <b>(+315.95%)</b></td><td>739.52 <b>(+110.37%)</b></td><td>455.70 <b>(+27.68%)</b></td><td>294.30 <b>(+24.97%)</b></td><td>676.66 <b>(+717.20%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.20 (n/a)</td><td>351.54 (n/a)</td><td>356.90 (n/a)</td><td>235.50 (n/a)</td><td>82.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (-17.19%)</td><td>0.02 (+2.02%)</td><td>0.02 <b>(+20.48%)</b></td><td>0.02 <b>(+49.74%)</b></td><td>0.01 <b>(-36.17%)</b></td><td>678.50 <b>(-33.22%)</b></td><td>510.66 (-14.14%)</td><td>496.70 (-17.01%)</td><td>291.60 <b>(+20.80%)</b></td><td>150.58 <b>(-46.77%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1016.00 (n/a)</td><td>594.76 (n/a)</td><td>598.50 (n/a)</td><td>241.40 (n/a)</td><td>282.89 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (+3.73%)</td><td>0.03 (+10.32%)</td><td>0.02 (+12.61%)</td><td>0.02 (+14.86%)</td><td>0.01 (-4.41%)</td><td>464.40 (-12.94%)</td><td>389.14 (-11.33%)</td><td>425.60 (-11.19%)</td><td>214.70 (-3.59%)</td><td>100.69 (-18.70%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.40 (n/a)</td><td>438.86 (n/a)</td><td>479.20 (n/a)</td><td>222.70 (n/a)</td><td>123.84 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 <b>(-34.12%)</b></td><td>0.05 (-15.59%)</td><td>0.05 (+14.69%)</td><td>0.04 (-5.92%)</td><td>0.01 <b>(-53.09%)</b></td><td>583.30 (+6.29%)</td><td>444.40 (+8.79%)</td><td>390.70 (-12.81%)</td><td>316.10 <b>(+51.83%)</b></td><td>113.30 <b>(-24.05%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>548.80 (n/a)</td><td>408.50 (n/a)</td><td>448.10 (n/a)</td><td>208.20 (n/a)</td><td>149.17 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (+18.69%)</td><td>0.06 (-8.93%)</td><td>0.05 <b>(-35.86%)</b></td><td>0.04 (-4.56%)</td><td>0.02 <b>(+63.50%)</b></td><td>550.00 (+4.78%)</td><td>406.06 (+17.70%)</td><td>464.10 <b>(+55.90%)</b></td><td>225.10 (-15.76%)</td><td>146.20 <b>(+40.13%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>524.90 (n/a)</td><td>345.00 (n/a)</td><td>297.70 (n/a)</td><td>267.20 (n/a)</td><td>104.33 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (-7.77%)</td><td>0.05 (-15.64%)</td><td>0.04 (-11.82%)</td><td>0.04 (-6.04%)</td><td>0.02 (-16.34%)</td><td>590.30 (+6.42%)</td><td>494.08 (+15.83%)</td><td>568.50 (+13.41%)</td><td>268.80 (+8.43%)</td><td>137.86 (-5.26%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>554.70 (n/a)</td><td>426.56 (n/a)</td><td>501.30 (n/a)</td><td>247.90 (n/a)</td><td>145.51 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 <b>(+43.22%)</b></td><td>0.07 (+0.05%)</td><td>0.06 (-10.74%)</td><td>0.04 (+3.59%)</td><td>0.04 <b>(+79.24%)</b></td><td>534.30 (-3.45%)</td><td>357.80 (+9.03%)</td><td>347.20 (+12.04%)</td><td>148.20 <b>(-30.19%)</b></td><td>145.87 (+9.54%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>553.40 (n/a)</td><td>328.16 (n/a)</td><td>309.90 (n/a)</td><td>212.30 (n/a)</td><td>133.17 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (+13.71%)</td><td>0.06 <b>(-26.21%)</b></td><td>0.04 <b>(-46.59%)</b></td><td>0.04 <b>(-23.21%)</b></td><td>0.03 <b>(+74.49%)</b></td><td>533.10 <b>(+30.21%)</b></td><td>422.84 <b>(+48.93%)</b></td><td>494.70 <b>(+87.24%)</b></td><td>198.60 (-12.05%)</td><td>141.30 <b>(+92.71%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>409.40 (n/a)</td><td>283.92 (n/a)</td><td>264.20 (n/a)</td><td>225.80 (n/a)</td><td>73.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 <b>(-21.49%)</b></td><td>0.05 (-17.22%)</td><td>0.04 (-16.65%)</td><td>0.03 (-9.84%)</td><td>0.03 <b>(-25.82%)</b></td><td>614.40 (+10.90%)</td><td>482.44 (+17.02%)</td><td>520.60 (+19.98%)</td><td>219.00 <b>(+27.40%)</b></td><td>155.49 (+6.72%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>554.00 (n/a)</td><td>412.26 (n/a)</td><td>433.90 (n/a)</td><td>171.90 (n/a)</td><td>145.70 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>519.50 (n/a)</td><td>349.22 (n/a)</td><td>303.80 (n/a)</td><td>224.30 (n/a)</td><td>124.42 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>486.60 (n/a)</td><td>350.24 (n/a)</td><td>288.50 (n/a)</td><td>249.50 (n/a)</td><td>105.92 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1931.60 (n/a)</td><td>719.60 (n/a)</td><td>480.70 (n/a)</td><td>293.50 (n/a)</td><td>682.45 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2115.20 (n/a)</td><td>676.34 (n/a)</td><td>294.70 (n/a)</td><td>233.50 (n/a)</td><td>811.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1075.90 (n/a)</td><td>509.46 (n/a)</td><td>472.60 (n/a)</td><td>229.50 (n/a)</td><td>342.85 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>448.20 (n/a)</td><td>353.50 (n/a)</td><td>340.00 (n/a)</td><td>269.40 (n/a)</td><td>79.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1041.80 (n/a)</td><td>489.38 (n/a)</td><td>276.20 (n/a)</td><td>242.10 (n/a)</td><td>345.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>493.90 (n/a)</td><td>384.22 (n/a)</td><td>450.40 (n/a)</td><td>252.60 (n/a)</td><td>116.70 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>522.50 (n/a)</td><td>411.00 (n/a)</td><td>481.40 (n/a)</td><td>239.40 (n/a)</td><td>132.27 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.18 <b>(-26.82%)</b></td><td>0.16 <b>(+25.19%)</b></td><td>0.16 <b>(+50.36%)</b></td><td>0.10 <b>(+88.35%)</b></td><td>0.03 <b>(-56.86%)</b></td><td>476.00 <b>(-46.90%)</b></td><td>330.84 <b>(-34.46%)</b></td><td>314.80 <b>(-33.49%)</b></td><td>268.70 <b>(+36.67%)</b></td><td>84.85 <b>(-66.89%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>896.50 (n/a)</td><td>504.80 (n/a)</td><td>473.30 (n/a)</td><td>196.60 (n/a)</td><td>256.28 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>676.30 (n/a)</td><td>363.90 (n/a)</td><td>299.40 (n/a)</td><td>250.70 (n/a)</td><td>175.93 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>616.30 (n/a)</td><td>431.78 (n/a)</td><td>460.00 (n/a)</td><td>246.90 (n/a)</td><td>151.44 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.70 (n/a)</td><td>434.78 (n/a)</td><td>522.30 (n/a)</td><td>258.50 (n/a)</td><td>147.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.20 (n/a)</td><td>313.66 (n/a)</td><td>242.80 (n/a)</td><td>236.40 (n/a)</td><td>161.34 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.50 (n/a)</td><td>369.96 (n/a)</td><td>362.60 (n/a)</td><td>231.40 (n/a)</td><td>150.92 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>562.00 (n/a)</td><td>366.04 (n/a)</td><td>266.30 (n/a)</td><td>223.80 (n/a)</td><td>157.97 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>655.20 (n/a)</td><td>478.64 (n/a)</td><td>506.90 (n/a)</td><td>242.40 (n/a)</td><td>168.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>651.90 (n/a)</td><td>481.44 (n/a)</td><td>436.00 (n/a)</td><td>363.70 (n/a)</td><td>113.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>577.00 (n/a)</td><td>321.12 (n/a)</td><td>297.60 (n/a)</td><td>182.00 (n/a)</td><td>151.01 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>896.20 (n/a)</td><td>493.12 (n/a)</td><td>482.50 (n/a)</td><td>249.40 (n/a)</td><td>265.28 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>546.30 (n/a)</td><td>381.46 (n/a)</td><td>384.60 (n/a)</td><td>240.90 (n/a)</td><td>117.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>445.40 (n/a)</td><td>312.44 (n/a)</td><td>288.60 (n/a)</td><td>246.30 (n/a)</td><td>77.72 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>541.30 (n/a)</td><td>410.32 (n/a)</td><td>503.80 (n/a)</td><td>194.70 (n/a)</td><td>159.69 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>600.80 (n/a)</td><td>369.48 (n/a)</td><td>271.00 (n/a)</td><td>248.30 (n/a)</td><td>157.84 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.30 (n/a)</td><td>405.28 (n/a)</td><td>373.70 (n/a)</td><td>276.90 (n/a)</td><td>121.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.00 (n/a)</td><td>407.70 (n/a)</td><td>485.70 (n/a)</td><td>218.10 (n/a)</td><td>166.06 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.00 (n/a)</td><td>469.46 (n/a)</td><td>523.50 (n/a)</td><td>278.00 (n/a)</td><td>110.86 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.70 (n/a)</td><td>453.34 (n/a)</td><td>495.60 (n/a)</td><td>230.10 (n/a)</td><td>191.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1840.60 (n/a)</td><td>777.14 (n/a)</td><td>542.40 (n/a)</td><td>434.80 (n/a)</td><td>596.20 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.70 (n/a)</td><td>382.96 (n/a)</td><td>299.40 (n/a)</td><td>286.10 (n/a)</td><td>131.29 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>483.20 (n/a)</td><td>378.62 (n/a)</td><td>406.60 (n/a)</td><td>244.90 (n/a)</td><td>89.02 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.50 (n/a)</td><td>504.20 (n/a)</td><td>521.60 (n/a)</td><td>257.00 (n/a)</td><td>145.56 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>753.40 (n/a)</td><td>550.68 (n/a)</td><td>576.20 (n/a)</td><td>290.60 (n/a)</td><td>177.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1978.60 (n/a)</td><td>1083.00 (n/a)</td><td>827.10 (n/a)</td><td>223.90 (n/a)</td><td>806.52 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>874.80 (n/a)</td><td>618.56 (n/a)</td><td>609.70 (n/a)</td><td>361.40 (n/a)</td><td>186.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>585.30 (n/a)</td><td>426.00 (n/a)</td><td>473.90 (n/a)</td><td>258.20 (n/a)</td><td>133.06 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>598.80 (n/a)</td><td>463.44 (n/a)</td><td>489.40 (n/a)</td><td>268.40 (n/a)</td><td>120.37 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>528.20 (n/a)</td><td>385.92 (n/a)</td><td>333.20 (n/a)</td><td>294.20 (n/a)</td><td>102.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>662.30 (n/a)</td><td>467.66 (n/a)</td><td>543.50 (n/a)</td><td>226.30 (n/a)</td><td>184.93 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2028.80 (n/a)</td><td>766.52 (n/a)</td><td>515.80 (n/a)</td><td>251.30 (n/a)</td><td>715.07 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>714.30 (n/a)</td><td>433.46 (n/a)</td><td>350.10 (n/a)</td><td>193.70 (n/a)</td><td>207.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>640.00 (n/a)</td><td>369.58 (n/a)</td><td>287.30 (n/a)</td><td>267.20 (n/a)</td><td>156.90 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>801.20 (n/a)</td><td>440.38 (n/a)</td><td>409.20 (n/a)</td><td>273.40 (n/a)</td><td>211.54 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>486.70 (n/a)</td><td>314.06 (n/a)</td><td>275.40 (n/a)</td><td>245.30 (n/a)</td><td>99.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>522.30 (n/a)</td><td>394.54 (n/a)</td><td>465.10 (n/a)</td><td>168.70 (n/a)</td><td>154.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>613.00 (n/a)</td><td>488.26 (n/a)</td><td>528.40 (n/a)</td><td>217.50 (n/a)</td><td>157.01 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.53 <b>(-22.20%)</b></td><td>0.36 <b>(-24.22%)</b></td><td>0.36 <b>(-27.18%)</b></td><td>0.22 (-16.67%)</td><td>0.11 <b>(-25.16%)</b></td><td>1011.80 <b>(+20.01%)</b></td><td>660.64 <b>(+29.87%)</b></td><td>617.30 <b>(+37.33%)</b></td><td>416.90 <b>(+28.55%)</b></td><td>217.41 (+10.73%)</td><td>22.64 <b>(-22.20%)</b></td><td>15.47 <b>(-24.22%)</b></td><td>15.29 <b>(-27.18%)</b></td><td>9.33 (-16.67%)</td><td>4.77 <b>(-25.16%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.68 (n/a)</td><td>0.48 (n/a)</td><td>0.49 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>843.10 (n/a)</td><td>508.70 (n/a)</td><td>449.50 (n/a)</td><td>324.30 (n/a)</td><td>196.34 (n/a)</td><td>29.10 (n/a)</td><td>20.42 (n/a)</td><td>21.00 (n/a)</td><td>11.19 (n/a)</td><td>6.37 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.52 <b>(-25.28%)</b></td><td>0.44 (+11.65%)</td><td>0.44 <b>(+22.70%)</b></td><td>0.37 <b>(+122.31%)</b></td><td>0.06 <b>(-70.30%)</b></td><td>604.80 <b>(-55.02%)</b></td><td>512.20 <b>(-28.10%)</b></td><td>504.70 (-18.50%)</td><td>423.00 <b>(+33.82%)</b></td><td>70.51 <b>(-82.28%)</b></td><td>22.31 <b>(-25.28%)</b></td><td>18.71 (+11.65%)</td><td>18.70 <b>(+22.70%)</b></td><td>15.60 <b>(+122.31%)</b></td><td>2.60 <b>(-70.30%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.70 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.16 (n/a)</td><td>0.20 (n/a)</td><td>1344.50 (n/a)</td><td>712.34 (n/a)</td><td>619.30 (n/a)</td><td>316.10 (n/a)</td><td>397.81 (n/a)</td><td>29.86 (n/a)</td><td>16.76 (n/a)</td><td>15.24 (n/a)</td><td>7.02 (n/a)</td><td>8.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.31 (-0.84%)</td><td>0.31 (-0.39%)</td><td>0.31 (-0.10%)</td><td>0.30 (-0.68%)</td><td>0.00 (+1.85%)</td><td>83898.60 (+0.69%)</td><td>82088.62 (+0.39%)</td><td>81814.00 (+0.10%)</td><td>81272.20 (+0.85%)</td><td>1038.36 (+3.54%)</td><td>211.39 (-0.84%)</td><td>209.31 (-0.39%)</td><td>209.99 (-0.10%)</td><td>204.77 (-0.68%)</td><td>2.61 (+1.85%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83325.00 (n/a)</td><td>81769.94 (n/a)</td><td>81730.00 (n/a)</td><td>80587.90 (n/a)</td><td>1002.88 (n/a)</td><td>213.18 (n/a)</td><td>210.13 (n/a)</td><td>210.20 (n/a)</td><td>206.18 (n/a)</td><td>2.56 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>1.03 (-0.29%)</td><td>1.02 (+1.75%)</td><td>1.02 (+1.50%)</td><td>1.01 (+4.50%)</td><td>0.01 <b>(-78.99%)</b></td><td>24846.80 (-4.31%)</td><td>24615.70 (-1.77%)</td><td>24582.10 (-1.48%)</td><td>24484.50 (+0.30%)</td><td>136.87 <b>(-79.76%)</b></td><td>701.66 (-0.29%)</td><td>697.94 (+1.75%)</td><td>698.88 (+1.50%)</td><td>691.43 (+4.50%)</td><td>3.86 <b>(-79.00%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>1.01 (n/a)</td><td>0.97 (n/a)</td><td>0.03 (n/a)</td><td>25964.70 (n/a)</td><td>25059.84 (n/a)</td><td>24951.00 (n/a)</td><td>24412.30 (n/a)</td><td>676.23 (n/a)</td><td>703.74 (n/a)</td><td>685.95 (n/a)</td><td>688.54 (n/a)</td><td>661.66 (n/a)</td><td>18.38 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.82 (+2.45%)</td><td>0.81 (+1.79%)</td><td>0.81 (+2.31%)</td><td>0.79 (+1.86%)</td><td>0.01 (+6.07%)</td><td>95047.90 (-1.83%)</td><td>93435.44 (-1.76%)</td><td>93262.20 (-2.26%)</td><td>91532.10 (-2.39%)</td><td>1306.39 (+1.82%)</td><td>750.77 (+2.45%)</td><td>735.59 (+1.79%)</td><td>736.84 (+2.31%)</td><td>723.00 (+1.86%)</td><td>10.33 (+6.07%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96814.90 (n/a)</td><td>95107.92 (n/a)</td><td>95420.30 (n/a)</td><td>93774.20 (n/a)</td><td>1282.99 (n/a)</td><td>732.82 (n/a)</td><td>722.65 (n/a)</td><td>720.18 (n/a)</td><td>709.80 (n/a)</td><td>9.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.78 (-0.13%)</td><td>0.76 (-0.06%)</td><td>0.77 (-0.50%)</td><td>0.75 (+0.35%)</td><td>0.01 (-15.12%)</td><td>101239.50 (-0.35%)</td><td>98855.00 (+0.06%)</td><td>98607.90 (+0.50%)</td><td>97270.00 (+0.13%)</td><td>1481.58 (-15.25%)</td><td>706.48 (-0.13%)</td><td>695.28 (-0.06%)</td><td>696.90 (-0.50%)</td><td>678.78 (+0.35%)</td><td>10.31 (-15.12%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101590.40 (n/a)</td><td>98800.12 (n/a)</td><td>98116.00 (n/a)</td><td>97144.10 (n/a)</td><td>1748.10 (n/a)</td><td>707.40 (n/a)</td><td>695.71 (n/a)</td><td>700.39 (n/a)</td><td>676.44 (n/a)</td><td>12.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.81 (+0.76%)</td><td>0.80 (+0.76%)</td><td>0.80 (+0.45%)</td><td>0.79 (+1.24%)</td><td>0.01 <b>(-31.24%)</b></td><td>95532.70 (-1.23%)</td><td>94654.94 (-0.76%)</td><td>94775.90 (-0.45%)</td><td>93685.70 (-0.75%)</td><td>679.85 <b>(-32.55%)</b></td><td>733.51 (+0.76%)</td><td>726.03 (+0.76%)</td><td>725.07 (+0.45%)</td><td>719.33 (+1.24%)</td><td>5.22 <b>(-31.24%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96717.50 (n/a)</td><td>95376.86 (n/a)</td><td>95205.90 (n/a)</td><td>94393.50 (n/a)</td><td>1007.99 (n/a)</td><td>728.01 (n/a)</td><td>720.57 (n/a)</td><td>721.80 (n/a)</td><td>710.52 (n/a)</td><td>7.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>5.65 <b>(+22.54%)</b></td><td>4.62 <b>(+51.92%)</b></td><td>5.23 <b>(+127.20%)</b></td><td>2.61 <b>(+21.08%)</b></td><td>1.28 (+9.90%)</td><td>3414.40 (-17.41%)</td><td>2097.56 <b>(-35.66%)</b></td><td>1702.80 <b>(-55.99%)</b></td><td>1577.90 (-18.39%)</td><td>774.73 <b>(-28.38%)</b></td><td>340.25 <b>(+22.54%)</b></td><td>278.37 <b>(+51.92%)</b></td><td>315.28 <b>(+127.20%)</b></td><td>157.24 <b>(+21.08%)</b></td><td>77.20 (+9.90%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>4.61 (n/a)</td><td>3.04 (n/a)</td><td>2.30 (n/a)</td><td>2.16 (n/a)</td><td>1.17 (n/a)</td><td>4134.20 (n/a)</td><td>3260.00 (n/a)</td><td>3868.80 (n/a)</td><td>1933.50 (n/a)</td><td>1081.68 (n/a)</td><td>277.66 (n/a)</td><td>183.23 (n/a)</td><td>138.77 (n/a)</td><td>129.86 (n/a)</td><td>70.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.00 <b>(-34.95%)</b></td><td>2.44 <b>(-30.85%)</b></td><td>2.26 <b>(-35.30%)</b></td><td>2.12 (-9.54%)</td><td>0.36 <b>(-63.20%)</b></td><td>4199.60 (+10.55%)</td><td>3718.64 <b>(+37.45%)</b></td><td>3948.60 <b>(+54.56%)</b></td><td>2973.80 <b>(+53.72%)</b></td><td>508.64 <b>(-36.13%)</b></td><td>180.54 <b>(-34.95%)</b></td><td>146.76 <b>(-30.85%)</b></td><td>135.96 <b>(-35.30%)</b></td><td>127.84 (-9.54%)</td><td>21.89 <b>(-63.20%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>4.61 (n/a)</td><td>3.52 (n/a)</td><td>3.49 (n/a)</td><td>2.35 (n/a)</td><td>0.99 (n/a)</td><td>3798.90 (n/a)</td><td>2705.38 (n/a)</td><td>2554.80 (n/a)</td><td>1934.50 (n/a)</td><td>796.38 (n/a)</td><td>277.52 (n/a)</td><td>212.25 (n/a)</td><td>210.14 (n/a)</td><td>141.32 (n/a)</td><td>59.49 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>5.23 (+15.12%)</td><td>4.07 (+4.98%)</td><td>4.25 (+5.14%)</td><td>2.18 <b>(-22.15%)</b></td><td>1.27 <b>(+96.98%)</b></td><td>4088.20 <b>(+28.45%)</b></td><td>2427.02 (+2.88%)</td><td>2097.40 (-4.88%)</td><td>1703.30 (-13.14%)</td><td>987.65 <b>(+108.38%)</b></td><td>315.20 (+15.12%)</td><td>245.43 (+4.98%)</td><td>255.97 (+5.14%)</td><td>131.32 <b>(-22.15%)</b></td><td>76.71 <b>(+96.98%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>4.55 (n/a)</td><td>3.88 (n/a)</td><td>4.04 (n/a)</td><td>2.80 (n/a)</td><td>0.65 (n/a)</td><td>3182.60 (n/a)</td><td>2359.04 (n/a)</td><td>2205.10 (n/a)</td><td>1960.90 (n/a)</td><td>473.96 (n/a)</td><td>273.79 (n/a)</td><td>233.79 (n/a)</td><td>243.46 (n/a)</td><td>168.69 (n/a)</td><td>38.94 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>6.66 (-0.65%)</td><td>5.68 (+2.90%)</td><td>5.66 (+4.27%)</td><td>4.70 (+1.59%)</td><td>0.87 (+11.00%)</td><td>7417.90 (-1.56%)</td><td>6258.50 (-2.47%)</td><td>6160.20 (-4.10%)</td><td>5235.80 (+0.65%)</td><td>963.67 (+10.53%)</td><td>410.16 (-0.65%)</td><td>349.69 (+2.90%)</td><td>348.60 (+4.27%)</td><td>289.50 (+1.59%)</td><td>53.43 (+11.00%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>6.70 (n/a)</td><td>5.52 (n/a)</td><td>5.43 (n/a)</td><td>4.63 (n/a)</td><td>0.78 (n/a)</td><td>7535.70 (n/a)</td><td>6417.08 (n/a)</td><td>6423.40 (n/a)</td><td>5201.90 (n/a)</td><td>871.83 (n/a)</td><td>412.83 (n/a)</td><td>339.84 (n/a)</td><td>334.32 (n/a)</td><td>284.98 (n/a)</td><td>48.14 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>5.50 (+4.77%)</td><td>4.71 (+6.75%)</td><td>4.81 (+13.48%)</td><td>3.71 (-9.34%)</td><td>0.64 <b>(+32.76%)</b></td><td>9392.00 (+10.30%)</td><td>7521.20 (-5.59%)</td><td>7253.30 (-11.88%)</td><td>6333.70 (-4.55%)</td><td>1129.97 <b>(+44.59%)</b></td><td>339.06 (+4.77%)</td><td>290.25 (+6.75%)</td><td>296.07 (+13.48%)</td><td>228.65 (-9.34%)</td><td>39.68 <b>(+32.76%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>5.25 (n/a)</td><td>4.41 (n/a)</td><td>4.24 (n/a)</td><td>4.09 (n/a)</td><td>0.49 (n/a)</td><td>8515.10 (n/a)</td><td>7966.72 (n/a)</td><td>8231.00 (n/a)</td><td>6635.90 (n/a)</td><td>781.48 (n/a)</td><td>323.62 (n/a)</td><td>271.90 (n/a)</td><td>260.90 (n/a)</td><td>252.20 (n/a)</td><td>29.89 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>6.40 (+6.86%)</td><td>5.60 (+13.71%)</td><td>5.49 (+11.06%)</td><td>4.99 (+17.64%)</td><td>0.60 (-13.04%)</td><td>6983.30 (-14.99%)</td><td>6277.38 (-12.57%)</td><td>6353.10 (-9.96%)</td><td>5446.50 (-6.42%)</td><td>658.79 <b>(-30.84%)</b></td><td>394.29 (+6.86%)</td><td>345.20 (+13.71%)</td><td>338.02 (+11.06%)</td><td>307.52 (+17.64%)</td><td>37.05 (-13.04%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>5.99 (n/a)</td><td>4.93 (n/a)</td><td>4.94 (n/a)</td><td>4.24 (n/a)</td><td>0.69 (n/a)</td><td>8215.00 (n/a)</td><td>7180.28 (n/a)</td><td>7055.70 (n/a)</td><td>5820.10 (n/a)</td><td>952.52 (n/a)</td><td>368.98 (n/a)</td><td>303.58 (n/a)</td><td>304.36 (n/a)</td><td>261.41 (n/a)</td><td>42.61 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.78 (+0.24%)</td><td>0.76 (-0.55%)</td><td>0.76 (-0.50%)</td><td>0.74 (-1.35%)</td><td>0.02 <b>(+72.93%)</b></td><td>102430.80 (+1.37%)</td><td>99557.80 (+0.59%)</td><td>99485.80 (+0.51%)</td><td>96620.40 (-0.24%)</td><td>2612.52 <b>(+75.07%)</b></td><td>711.23 (+0.24%)</td><td>690.63 (-0.55%)</td><td>690.75 (-0.50%)</td><td>670.89 (-1.35%)</td><td>18.12 <b>(+72.93%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101050.10 (n/a)</td><td>98970.18 (n/a)</td><td>98984.30 (n/a)</td><td>96853.50 (n/a)</td><td>1492.25 (n/a)</td><td>709.52 (n/a)</td><td>694.47 (n/a)</td><td>694.25 (n/a)</td><td>680.05 (n/a)</td><td>10.48 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.77 (+1.88%)</td><td>0.76 (+0.85%)</td><td>0.76 (+0.78%)</td><td>0.73 (-1.45%)</td><td>0.02 <b>(+126.69%)</b></td><td>103161.50 (+1.47%)</td><td>99874.76 (-0.82%)</td><td>99671.90 (-0.78%)</td><td>97928.30 (-1.85%)</td><td>2024.40 <b>(+126.03%)</b></td><td>701.73 (+1.88%)</td><td>688.28 (+0.85%)</td><td>689.46 (+0.78%)</td><td>666.13 (-1.45%)</td><td>13.74 <b>(+126.69%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101665.80 (n/a)</td><td>100698.16 (n/a)</td><td>100451.20 (n/a)</td><td>99771.50 (n/a)</td><td>895.65 (n/a)</td><td>688.77 (n/a)</td><td>682.47 (n/a)</td><td>684.11 (n/a)</td><td>675.93 (n/a)</td><td>6.06 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.81 (+0.46%)</td><td>0.80 (+1.13%)</td><td>0.81 (+1.55%)</td><td>0.79 (+1.00%)</td><td>0.01 <b>(-23.16%)</b></td><td>94988.90 (-0.99%)</td><td>93921.86 (-1.12%)</td><td>93754.40 (-1.52%)</td><td>93494.00 (-0.45%)</td><td>612.31 <b>(-24.16%)</b></td><td>735.01 (+0.46%)</td><td>731.69 (+1.13%)</td><td>732.97 (+1.55%)</td><td>723.45 (+1.00%)</td><td>4.73 <b>(-23.16%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95935.20 (n/a)</td><td>94983.70 (n/a)</td><td>95204.70 (n/a)</td><td>93920.60 (n/a)</td><td>807.39 (n/a)</td><td>731.68 (n/a)</td><td>723.53 (n/a)</td><td>721.81 (n/a)</td><td>716.31 (n/a)</td><td>6.16 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.95 <b>(+50.99%)</b></td><td>2.19 <b>(+23.80%)</b></td><td>1.86 (+14.83%)</td><td>1.04 <b>(-24.54%)</b></td><td>1.13 <b>(+130.84%)</b></td><td>7781.80 <b>(+32.51%)</b></td><td>4498.24 (-5.78%)</td><td>4325.90 (-12.92%)</td><td>2040.70 <b>(-33.77%)</b></td><td>2194.50 <b>(+109.32%)</b></td><td>1035.89 <b>(+50.99%)</b></td><td>575.62 <b>(+23.80%)</b></td><td>488.67 (+14.83%)</td><td>271.65 <b>(-24.54%)</b></td><td>296.30 <b>(+130.84%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>2.62 (n/a)</td><td>1.77 (n/a)</td><td>1.62 (n/a)</td><td>1.37 (n/a)</td><td>0.49 (n/a)</td><td>5872.50 (n/a)</td><td>4774.44 (n/a)</td><td>4967.50 (n/a)</td><td>3081.30 (n/a)</td><td>1048.38 (n/a)</td><td>686.04 (n/a)</td><td>464.97 (n/a)</td><td>425.56 (n/a)</td><td>359.97 (n/a)</td><td>128.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.29 <b>(+33.91%)</b></td><td>0.21 (+13.19%)</td><td>0.20 (+15.66%)</td><td>0.15 (-10.75%)</td><td>0.05 <b>(+141.30%)</b></td><td>8119.50 (+12.04%)</td><td>6090.20 (-8.64%)</td><td>6112.20 (-13.54%)</td><td>4273.50 <b>(-25.32%)</b></td><td>1390.77 <b>(+98.00%)</b></td><td>15.70 <b>(+33.91%)</b></td><td>11.50 (+13.19%)</td><td>10.98 (+15.66%)</td><td>8.27 (-10.74%)</td><td>2.72 <b>(+141.30%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>7247.10 (n/a)</td><td>6666.40 (n/a)</td><td>7069.30 (n/a)</td><td>5722.50 (n/a)</td><td>702.41 (n/a)</td><td>11.73 (n/a)</td><td>10.16 (n/a)</td><td>9.49 (n/a)</td><td>9.26 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.15 <b>(+50.46%)</b></td><td>0.11 <b>(+56.16%)</b></td><td>0.11 <b>(+84.93%)</b></td><td>0.07 <b>(+33.35%)</b></td><td>0.03 <b>(+36.78%)</b></td><td>0.15 <b>(+50.46%)</b></td><td>0.11 <b>(+56.16%)</b></td><td>0.11 <b>(+84.93%)</b></td><td>0.06 <b>(+33.35%)</b></td><td>0.03 <b>(+36.78%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.77 (-3.41%)</td><td>3.62 (-2.00%)</td><td>3.66 (-3.57%)</td><td>3.41 (+1.07%)</td><td>0.15 <b>(-35.55%)</b></td><td>3.77 (-3.41%)</td><td>3.62 (-2.00%)</td><td>3.66 (-3.57%)</td><td>3.41 (+1.07%)</td><td>0.15 <b>(-35.55%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.91 (n/a)</td><td>3.69 (n/a)</td><td>3.79 (n/a)</td><td>3.38 (n/a)</td><td>0.24 (n/a)</td><td>3.90 (n/a)</td><td>3.69 (n/a)</td><td>3.79 (n/a)</td><td>3.37 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>7.39 (-1.94%)</td><td>6.11 (-13.13%)</td><td>5.67 <b>(-24.28%)</b></td><td>5.34 (-12.26%)</td><td>0.87 <b>(+28.97%)</b></td><td>7.38 (-1.94%)</td><td>6.11 (-13.13%)</td><td>5.67 <b>(-24.28%)</b></td><td>5.34 (-12.26%)</td><td>0.87 <b>(+28.97%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>7.53 (n/a)</td><td>7.04 (n/a)</td><td>7.49 (n/a)</td><td>6.09 (n/a)</td><td>0.67 (n/a)</td><td>7.53 (n/a)</td><td>7.03 (n/a)</td><td>7.48 (n/a)</td><td>6.08 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>8.45 <b>(-35.56%)</b></td><td>7.93 (-17.60%)</td><td>7.98 (-7.56%)</td><td>7.42 (-9.28%)</td><td>0.45 <b>(-78.22%)</b></td><td>8.45 <b>(-35.56%)</b></td><td>7.92 (-17.60%)</td><td>7.97 (-7.56%)</td><td>7.41 (-9.28%)</td><td>0.45 <b>(-78.22%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>13.12 (n/a)</td><td>9.62 (n/a)</td><td>8.63 (n/a)</td><td>8.18 (n/a)</td><td>2.07 (n/a)</td><td>13.11 (n/a)</td><td>9.62 (n/a)</td><td>8.62 (n/a)</td><td>8.17 (n/a)</td><td>2.07 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.88 (+0.76%)</td><td>3.51 (-5.74%)</td><td>3.65 (-2.69%)</td><td>3.06 (-13.31%)</td><td>0.36 <b>(+192.41%)</b></td><td>3.88 (+0.76%)</td><td>3.51 (-5.74%)</td><td>3.65 (-2.69%)</td><td>3.06 (-13.31%)</td><td>0.36 <b>(+192.41%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.85 (n/a)</td><td>3.72 (n/a)</td><td>3.75 (n/a)</td><td>3.53 (n/a)</td><td>0.12 (n/a)</td><td>3.85 (n/a)</td><td>3.72 (n/a)</td><td>3.75 (n/a)</td><td>3.53 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>6.94 (-6.46%)</td><td>6.12 (-4.18%)</td><td>5.74 (-4.10%)</td><td>5.59 (+1.16%)</td><td>0.64 <b>(-30.41%)</b></td><td>6.94 (-6.46%)</td><td>6.11 (-4.18%)</td><td>5.74 (-4.10%)</td><td>5.59 (+1.16%)</td><td>0.64 <b>(-30.41%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>7.42 (n/a)</td><td>6.39 (n/a)</td><td>5.99 (n/a)</td><td>5.53 (n/a)</td><td>0.92 (n/a)</td><td>7.42 (n/a)</td><td>6.38 (n/a)</td><td>5.99 (n/a)</td><td>5.52 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>14.49 (+2.26%)</td><td>9.45 (-16.73%)</td><td>8.39 <b>(-36.16%)</b></td><td>7.34 (-5.68%)</td><td>2.88 (-3.18%)</td><td>14.48 (+2.26%)</td><td>9.44 (-16.73%)</td><td>8.39 <b>(-36.16%)</b></td><td>7.34 (-5.68%)</td><td>2.88 (-3.18%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>14.17 (n/a)</td><td>11.35 (n/a)</td><td>13.14 (n/a)</td><td>7.78 (n/a)</td><td>2.97 (n/a)</td><td>14.16 (n/a)</td><td>11.34 (n/a)</td><td>13.14 (n/a)</td><td>7.78 (n/a)</td><td>2.97 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>1.71 <b>(-47.22%)</b></td><td>1.35 (-9.21%)</td><td>1.17 (+11.95%)</td><td>1.05 (+2.51%)</td><td>0.31 <b>(-68.22%)</b></td><td>1.71 <b>(-47.22%)</b></td><td>1.35 (-9.21%)</td><td>1.17 (+11.95%)</td><td>1.05 (+2.51%)</td><td>0.31 <b>(-68.22%)</b></td>
</tr>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.47 <b>(+45.30%)</b></td><td>0.32 <b>(+86.78%)</b></td><td>0.33 <b>(+146.42%)</b></td><td>0.08 (+4.20%)</td><td>0.16 <b>(+37.36%)</b></td><td>0.46 <b>(+45.30%)</b></td><td>0.32 <b>(+86.78%)</b></td><td>0.32 <b>(+146.42%)</b></td><td>0.08 (+4.20%)</td><td>0.15 <b>(+37.36%)</b></td>
</tr>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.63 (+7.32%)</td><td>0.42 (+16.87%)</td><td>0.36 <b>(-20.26%)</b></td><td>0.27 <b>(+249.96%)</b></td><td>0.14 <b>(-40.06%)</b></td><td>0.63 (+7.32%)</td><td>0.41 (+16.87%)</td><td>0.36 <b>(-20.26%)</b></td><td>0.27 <b>(+249.96%)</b></td><td>0.14 <b>(-40.06%)</b></td>
</tr>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>2.29 (-7.03%)</td><td>1.49 (+4.24%)</td><td>1.34 <b>(-28.75%)</b></td><td>0.76 <b>(+76.96%)</b></td><td>0.59 <b>(-37.52%)</b></td><td>2.26 (-7.03%)</td><td>1.47 (+4.24%)</td><td>1.32 <b>(-28.75%)</b></td><td>0.75 <b>(+76.96%)</b></td><td>0.58 <b>(-37.52%)</b></td>
</tr>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>359.60 (n/a)</td><td>297.06 (n/a)</td><td>286.00 (n/a)</td><td>232.30 (n/a)</td><td>51.98 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.10 (n/a)</td><td>395.00 (n/a)</td><td>440.20 (n/a)</td><td>249.70 (n/a)</td><td>132.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>631.00 (n/a)</td><td>426.38 (n/a)</td><td>478.30 (n/a)</td><td>239.80 (n/a)</td><td>159.14 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>669.70 (n/a)</td><td>502.38 (n/a)</td><td>600.00 (n/a)</td><td>280.00 (n/a)</td><td>193.63 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.10 (n/a)</td><td>461.86 (n/a)</td><td>497.90 (n/a)</td><td>259.00 (n/a)</td><td>125.72 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.60 (n/a)</td><td>466.08 (n/a)</td><td>449.20 (n/a)</td><td>331.80 (n/a)</td><td>110.46 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.20 (n/a)</td><td>445.28 (n/a)</td><td>462.20 (n/a)</td><td>275.60 (n/a)</td><td>114.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>741.20 (n/a)</td><td>407.86 (n/a)</td><td>291.50 (n/a)</td><td>241.60 (n/a)</td><td>219.09 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.20 (n/a)</td><td>418.56 (n/a)</td><td>433.60 (n/a)</td><td>234.80 (n/a)</td><td>155.29 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1847.70 (n/a)</td><td>715.74 (n/a)</td><td>560.10 (n/a)</td><td>288.40 (n/a)</td><td>648.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.90 (n/a)</td><td>484.56 (n/a)</td><td>538.90 (n/a)</td><td>242.70 (n/a)</td><td>150.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>966.00 (n/a)</td><td>601.74 (n/a)</td><td>578.10 (n/a)</td><td>308.60 (n/a)</td><td>239.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>482.20 (n/a)</td><td>339.28 (n/a)</td><td>285.30 (n/a)</td><td>258.10 (n/a)</td><td>93.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>729.10 (n/a)</td><td>521.62 (n/a)</td><td>562.70 (n/a)</td><td>233.30 (n/a)</td><td>184.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>566.30 (n/a)</td><td>410.30 (n/a)</td><td>461.00 (n/a)</td><td>194.40 (n/a)</td><td>165.31 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>552.20 (n/a)</td><td>374.94 (n/a)</td><td>311.30 (n/a)</td><td>206.80 (n/a)</td><td>165.51 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>589.30 (n/a)</td><td>416.96 (n/a)</td><td>412.80 (n/a)</td><td>267.70 (n/a)</td><td>122.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>586.30 (n/a)</td><td>335.30 (n/a)</td><td>293.20 (n/a)</td><td>212.60 (n/a)</td><td>148.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 <b>(-29.68%)</b></td><td>0.07 <b>(-33.46%)</b></td><td>0.06 <b>(-42.90%)</b></td><td>0.06 (+1.87%)</td><td>0.01 <b>(-52.61%)</b></td><td>573.50 (-1.83%)</td><td>502.84 <b>(+41.80%)</b></td><td>533.70 <b>(+75.16%)</b></td><td>366.70 <b>(+42.19%)</b></td><td>81.98 <b>(-38.15%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>584.20 (n/a)</td><td>354.62 (n/a)</td><td>304.70 (n/a)</td><td>257.90 (n/a)</td><td>132.54 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1825.50 (n/a)</td><td>656.06 (n/a)</td><td>310.60 (n/a)</td><td>285.80 (n/a)</td><td>662.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>705.40 (n/a)</td><td>392.54 (n/a)</td><td>310.50 (n/a)</td><td>286.30 (n/a)</td><td>177.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>555.90 (n/a)</td><td>467.18 (n/a)</td><td>482.30 (n/a)</td><td>319.10 (n/a)</td><td>92.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>570.60 (n/a)</td><td>384.26 (n/a)</td><td>331.90 (n/a)</td><td>219.00 (n/a)</td><td>144.03 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>566.50 (n/a)</td><td>457.78 (n/a)</td><td>460.50 (n/a)</td><td>335.60 (n/a)</td><td>107.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(+34.25%)</b></td><td>0.01 (+12.94%)</td><td>0.01 (+4.91%)</td><td>0.01 (+15.43%)</td><td>0.00 <b>(+42.37%)</b></td><td>486.50 (-13.37%)</td><td>380.14 (-9.70%)</td><td>421.50 (-4.68%)</td><td>225.60 <b>(-25.52%)</b></td><td>106.71 (-4.59%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>561.60 (n/a)</td><td>420.96 (n/a)</td><td>442.20 (n/a)</td><td>302.90 (n/a)</td><td>111.85 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(+103.61%)</b></td><td>0.01 <b>(+59.09%)</b></td><td>0.01 (+5.16%)</td><td>0.01 <b>(+313.35%)</b></td><td>0.00 <b>(+62.64%)</b></td><td>587.20 <b>(-75.81%)</b></td><td>432.98 <b>(-51.50%)</b></td><td>486.00 (-4.91%)</td><td>229.80 <b>(-50.89%)</b></td><td>158.77 <b>(-81.50%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2427.10 (n/a)</td><td>892.74 (n/a)</td><td>511.10 (n/a)</td><td>467.90 (n/a)</td><td>858.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(+48.08%)</b></td><td>0.02 <b>(+47.00%)</b></td><td>0.02 <b>(+91.84%)</b></td><td>0.01 (+9.57%)</td><td>0.01 <b>(+41.09%)</b></td><td>540.60 (-8.73%)</td><td>301.88 <b>(-30.09%)</b></td><td>259.10 <b>(-47.87%)</b></td><td>175.80 <b>(-32.49%)</b></td><td>139.91 (-4.51%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.30 (n/a)</td><td>431.84 (n/a)</td><td>497.00 (n/a)</td><td>260.40 (n/a)</td><td>146.52 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 <b>(-20.60%)</b></td><td>0.01 (-1.46%)</td><td>0.01 (+15.38%)</td><td>0.01 (+2.45%)</td><td>0.00 <b>(-38.78%)</b></td><td>569.50 (-2.40%)</td><td>389.34 (-4.48%)</td><td>336.10 (-13.33%)</td><td>294.60 <b>(+25.95%)</b></td><td>111.16 <b>(-25.33%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.50 (n/a)</td><td>407.58 (n/a)</td><td>387.80 (n/a)</td><td>233.90 (n/a)</td><td>148.86 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(+104.44%)</b></td><td>0.01 <b>(+41.46%)</b></td><td>0.01 (+9.72%)</td><td>0.01 <b>(+22.36%)</b></td><td>0.01 <b>(+191.14%)</b></td><td>535.20 (-18.28%)</td><td>390.38 <b>(-22.65%)</b></td><td>399.00 (-8.86%)</td><td>179.50 <b>(-51.09%)</b></td><td>131.64 (+2.29%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>654.90 (n/a)</td><td>504.70 (n/a)</td><td>437.80 (n/a)</td><td>367.00 (n/a)</td><td>128.70 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (+0.27%)</td><td>0.01 (+0.08%)</td><td>0.01 (-10.75%)</td><td>0.01 (+1.45%)</td><td>0.00 (+2.79%)</td><td>664.20 (-1.42%)</td><td>525.22 (+0.70%)</td><td>600.20 (+12.04%)</td><td>275.70 (-0.29%)</td><td>162.73 (+4.89%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>673.80 (n/a)</td><td>521.56 (n/a)</td><td>535.70 (n/a)</td><td>276.50 (n/a)</td><td>155.14 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (-1.15%)</td><td>0.03 (-0.10%)</td><td>0.03 (+6.18%)</td><td>0.02 (+1.87%)</td><td>0.01 (+0.90%)</td><td>543.60 (-1.84%)</td><td>337.34 (-0.08%)</td><td>275.80 (-5.81%)</td><td>263.00 (+1.15%)</td><td>118.43 (-3.03%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.80 (n/a)</td><td>337.60 (n/a)</td><td>292.80 (n/a)</td><td>260.00 (n/a)</td><td>122.14 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(-31.62%)</b></td><td>0.02 <b>(-32.30%)</b></td><td>0.02 <b>(-40.40%)</b></td><td>0.02 (+18.07%)</td><td>0.00 <b>(-63.71%)</b></td><td>541.70 (-15.31%)</td><td>462.48 <b>(+33.70%)</b></td><td>471.30 <b>(+67.78%)</b></td><td>371.80 <b>(+46.21%)</b></td><td>70.69 <b>(-57.10%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>639.60 (n/a)</td><td>345.92 (n/a)</td><td>280.90 (n/a)</td><td>254.30 (n/a)</td><td>164.79 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (+9.31%)</td><td>0.02 (+15.53%)</td><td>0.03 <b>(+38.65%)</b></td><td>0.02 <b>(+21.28%)</b></td><td>0.01 (-5.99%)</td><td>489.10 (-17.55%)</td><td>353.02 (-15.66%)</td><td>306.10 <b>(-27.89%)</b></td><td>251.50 (-8.51%)</td><td>105.46 <b>(-24.47%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.20 (n/a)</td><td>418.56 (n/a)</td><td>424.50 (n/a)</td><td>274.90 (n/a)</td><td>139.63 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (-19.19%)</td><td>0.03 (+14.69%)</td><td>0.03 <b>(+67.41%)</b></td><td>0.02 <b>(+38.86%)</b></td><td>0.01 <b>(-50.62%)</b></td><td>400.90 <b>(-27.99%)</b></td><td>315.08 <b>(-22.46%)</b></td><td>276.90 <b>(-40.27%)</b></td><td>251.80 <b>(+23.73%)</b></td><td>68.33 <b>(-56.35%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.70 (n/a)</td><td>406.32 (n/a)</td><td>463.60 (n/a)</td><td>203.50 (n/a)</td><td>156.52 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (-6.87%)</td><td>0.02 (-12.55%)</td><td>0.02 (-15.81%)</td><td>0.01 <b>(-22.40%)</b></td><td>0.01 (+9.41%)</td><td>602.30 <b>(+28.86%)</b></td><td>436.88 (+18.24%)</td><td>481.50 (+18.77%)</td><td>281.90 (+7.35%)</td><td>139.59 <b>(+48.38%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>467.40 (n/a)</td><td>369.48 (n/a)</td><td>405.40 (n/a)</td><td>262.60 (n/a)</td><td>94.08 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 <b>(+28.74%)</b></td><td>0.02 (-8.37%)</td><td>0.02 <b>(-38.30%)</b></td><td>0.01 (-10.58%)</td><td>0.01 <b>(+76.03%)</b></td><td>638.30 (+11.83%)</td><td>430.26 <b>(+20.06%)</b></td><td>487.20 <b>(+62.08%)</b></td><td>216.30 <b>(-22.33%)</b></td><td>176.23 <b>(+44.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.80 (n/a)</td><td>358.38 (n/a)</td><td>300.60 (n/a)</td><td>278.50 (n/a)</td><td>121.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (-0.34%)</td><td>0.02 <b>(-25.49%)</b></td><td>0.02 (-13.92%)</td><td>0.00 <b>(-76.46%)</b></td><td>0.01 <b>(+28.73%)</b></td><td>2001.90 <b>(+324.76%)</b></td><td>741.12 <b>(+106.65%)</b></td><td>475.90 (+16.19%)</td><td>201.60 (+0.30%)</td><td>722.35 <b>(+475.82%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>471.30 (n/a)</td><td>358.64 (n/a)</td><td>409.60 (n/a)</td><td>201.00 (n/a)</td><td>125.45 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(-25.59%)</b></td><td>0.02 (+2.87%)</td><td>0.01 (+7.77%)</td><td>0.01 (+3.39%)</td><td>0.01 <b>(-35.13%)</b></td><td>668.80 (-3.28%)</td><td>501.76 (-8.07%)</td><td>549.40 (-7.21%)</td><td>334.90 <b>(+34.39%)</b></td><td>150.32 (-12.13%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>691.50 (n/a)</td><td>545.80 (n/a)</td><td>592.10 (n/a)</td><td>249.20 (n/a)</td><td>171.07 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (+2.08%)</td><td>0.04 (+0.43%)</td><td>0.03 <b>(-37.08%)</b></td><td>0.03 <b>(+312.71%)</b></td><td>0.01 <b>(-39.28%)</b></td><td>578.90 <b>(-75.77%)</b></td><td>435.42 <b>(-43.17%)</b></td><td>473.80 <b>(+58.94%)</b></td><td>282.80 (-2.04%)</td><td>131.57 <b>(-85.62%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2389.30 (n/a)</td><td>766.16 (n/a)</td><td>298.10 (n/a)</td><td>288.70 (n/a)</td><td>914.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (-0.77%)</td><td>0.04 (+2.69%)</td><td>0.03 (-18.18%)</td><td>0.03 <b>(+27.20%)</b></td><td>0.01 (-16.72%)</td><td>500.70 <b>(-21.38%)</b></td><td>404.06 (-7.67%)</td><td>474.40 <b>(+22.24%)</b></td><td>273.30 (+0.77%)</td><td>110.17 <b>(-35.28%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>636.90 (n/a)</td><td>437.64 (n/a)</td><td>388.10 (n/a)</td><td>271.20 (n/a)</td><td>170.22 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (+8.79%)</td><td>0.04 (-17.26%)</td><td>0.04 (-14.38%)</td><td>0.01 <b>(-75.04%)</b></td><td>0.02 <b>(+88.12%)</b></td><td>2109.10 <b>(+300.59%)</b></td><td>734.10 <b>(+102.22%)</b></td><td>422.70 (+16.80%)</td><td>246.00 (-8.07%)</td><td>782.28 <b>(+641.37%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>526.50 (n/a)</td><td>363.02 (n/a)</td><td>361.90 (n/a)</td><td>267.60 (n/a)</td><td>105.52 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 <b>(-20.89%)</b></td><td>0.04 <b>(-34.39%)</b></td><td>0.04 <b>(-44.94%)</b></td><td>0.03 <b>(-38.02%)</b></td><td>0.01 (+7.26%)</td><td>590.90 <b>(+61.32%)</b></td><td>430.24 <b>(+57.53%)</b></td><td>453.90 <b>(+81.63%)</b></td><td>288.80 <b>(+26.39%)</b></td><td>116.29 <b>(+110.57%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>366.30 (n/a)</td><td>273.12 (n/a)</td><td>249.90 (n/a)</td><td>228.50 (n/a)</td><td>55.23 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (+3.62%)</td><td>0.05 (+9.71%)</td><td>0.06 (+9.49%)</td><td>0.03 (-8.58%)</td><td>0.01 (-2.48%)</td><td>593.50 (+9.38%)</td><td>357.22 (-8.96%)</td><td>294.70 (-8.65%)</td><td>260.40 (-3.48%)</td><td>136.27 (+2.30%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>542.60 (n/a)</td><td>392.38 (n/a)</td><td>322.60 (n/a)</td><td>269.80 (n/a)</td><td>133.22 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (-15.98%)</td><td>0.03 (-11.97%)</td><td>0.03 (-11.44%)</td><td>0.03 (-3.28%)</td><td>0.01 <b>(-20.84%)</b></td><td>633.90 (+3.39%)</td><td>506.78 (+12.38%)</td><td>526.00 (+12.90%)</td><td>377.90 (+19.02%)</td><td>108.88 (-2.90%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>613.10 (n/a)</td><td>450.94 (n/a)</td><td>465.90 (n/a)</td><td>317.50 (n/a)</td><td>112.14 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (-12.14%)</td><td>0.06 <b>(-30.39%)</b></td><td>0.06 <b>(-24.22%)</b></td><td>0.02 <b>(-70.99%)</b></td><td>0.03 <b>(+23.67%)</b></td><td>1922.30 <b>(+244.68%)</b></td><td>785.64 <b>(+91.28%)</b></td><td>571.40 <b>(+31.96%)</b></td><td>309.50 (+13.83%)</td><td>645.72 <b>(+455.90%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>557.70 (n/a)</td><td>410.72 (n/a)</td><td>433.00 (n/a)</td><td>271.90 (n/a)</td><td>116.16 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (+5.58%)</td><td>0.09 (-0.94%)</td><td>0.07 (-2.87%)</td><td>0.05 (-13.85%)</td><td>0.05 (+12.18%)</td><td>665.20 (+16.07%)</td><td>441.74 (+5.87%)</td><td>492.10 (+2.95%)</td><td>226.90 (-5.30%)</td><td>200.20 <b>(+21.02%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>573.10 (n/a)</td><td>417.26 (n/a)</td><td>478.00 (n/a)</td><td>239.60 (n/a)</td><td>165.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.18 <b>(+27.17%)</b></td><td>0.11 (+11.82%)</td><td>0.12 <b>(+30.39%)</b></td><td>0.05 (-17.92%)</td><td>0.05 <b>(+61.89%)</b></td><td>611.40 <b>(+21.84%)</b></td><td>375.72 (+0.52%)</td><td>278.70 <b>(-23.31%)</b></td><td>181.10 <b>(-21.36%)</b></td><td>186.12 <b>(+60.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>501.80 (n/a)</td><td>373.78 (n/a)</td><td>363.40 (n/a)</td><td>230.30 (n/a)</td><td>115.97 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 <b>(+33.21%)</b></td><td>0.08 (+15.09%)</td><td>0.06 (-10.35%)</td><td>0.02 <b>(+49.96%)</b></td><td>0.06 <b>(+34.69%)</b></td><td>1367.80 <b>(-33.31%)</b></td><td>594.18 <b>(-20.18%)</b></td><td>533.10 (+11.55%)</td><td>191.60 <b>(-24.95%)</b></td><td>455.79 <b>(-38.38%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2051.10 (n/a)</td><td>744.44 (n/a)</td><td>477.90 (n/a)</td><td>255.30 (n/a)</td><td>739.71 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (+8.57%)</td><td>0.08 (+13.65%)</td><td>0.07 (+11.54%)</td><td>0.07 <b>(+31.56%)</b></td><td>0.02 <b>(-21.85%)</b></td><td>486.30 <b>(-23.99%)</b></td><td>421.64 (-15.45%)</td><td>469.70 (-10.35%)</td><td>313.90 (-7.89%)</td><td>80.25 <b>(-43.96%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>639.80 (n/a)</td><td>498.66 (n/a)</td><td>523.90 (n/a)</td><td>340.80 (n/a)</td><td>143.19 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (+11.85%)</td><td>0.01 (+7.81%)</td><td>0.01 <b>(-26.43%)</b></td><td>0.01 <b>(+253.57%)</b></td><td>0.00 <b>(-31.25%)</b></td><td>543.20 <b>(-71.72%)</b></td><td>403.52 <b>(-40.35%)</b></td><td>399.80 <b>(+35.89%)</b></td><td>249.40 (-10.58%)</td><td>130.64 <b>(-81.55%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1920.70 (n/a)</td><td>676.52 (n/a)</td><td>294.20 (n/a)</td><td>278.90 (n/a)</td><td>708.14 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(+35.06%)</b></td><td>0.01 (+4.28%)</td><td>0.01 (-4.14%)</td><td>0.01 (+0.93%)</td><td>0.01 <b>(+67.70%)</b></td><td>493.60 (-0.92%)</td><td>352.96 (+2.55%)</td><td>301.00 (+4.30%)</td><td>186.00 <b>(-25.96%)</b></td><td>134.24 <b>(+30.28%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>498.20 (n/a)</td><td>344.18 (n/a)</td><td>288.60 (n/a)</td><td>251.20 (n/a)</td><td>103.04 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (+15.82%)</td><td>0.01 <b>(+43.47%)</b></td><td>0.01 (+18.62%)</td><td>0.01 <b>(+224.87%)</b></td><td>0.00 (+0.09%)</td><td>593.40 <b>(-69.22%)</b></td><td>431.78 <b>(-46.08%)</b></td><td>521.40 (-15.70%)</td><td>226.40 (-13.65%)</td><td>162.18 <b>(-74.97%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1927.90 (n/a)</td><td>800.74 (n/a)</td><td>618.50 (n/a)</td><td>262.20 (n/a)</td><td>647.90 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (+10.71%)</td><td>0.01 (-3.48%)</td><td>0.01 (-5.26%)</td><td>0.01 (-17.32%)</td><td>0.00 <b>(+31.01%)</b></td><td>579.50 <b>(+20.96%)</b></td><td>377.52 (+8.23%)</td><td>327.30 (+5.55%)</td><td>245.80 (-9.67%)</td><td>135.36 <b>(+48.17%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>479.10 (n/a)</td><td>348.80 (n/a)</td><td>310.10 (n/a)</td><td>272.10 (n/a)</td><td>91.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 <b>(-21.37%)</b></td><td>0.01 (-0.66%)</td><td>0.01 <b>(-21.53%)</b></td><td>0.01 <b>(+228.52%)</b></td><td>0.00 <b>(-46.41%)</b></td><td>602.80 <b>(-69.56%)</b></td><td>414.24 <b>(-38.87%)</b></td><td>411.50 <b>(+27.44%)</b></td><td>285.20 <b>(+27.21%)</b></td><td>133.64 <b>(-81.92%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1980.20 (n/a)</td><td>677.64 (n/a)</td><td>322.90 (n/a)</td><td>224.20 (n/a)</td><td>739.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (+12.12%)</td><td>0.01 (+18.31%)</td><td>0.01 <b>(+37.31%)</b></td><td>0.01 (+15.87%)</td><td>0.00 (-0.40%)</td><td>491.00 (-13.69%)</td><td>351.06 (-18.52%)</td><td>379.10 <b>(-27.17%)</b></td><td>202.40 (-10.80%)</td><td>114.39 <b>(-26.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.90 (n/a)</td><td>430.86 (n/a)</td><td>520.50 (n/a)</td><td>226.90 (n/a)</td><td>156.69 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (-10.18%)</td><td>0.01 (+2.82%)</td><td>0.01 (-5.79%)</td><td>0.01 <b>(+136.86%)</b></td><td>0.00 <b>(-31.74%)</b></td><td>571.40 <b>(-57.78%)</b></td><td>491.58 <b>(-21.60%)</b></td><td>548.60 (+6.15%)</td><td>271.10 (+11.33%)</td><td>125.35 <b>(-70.39%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1353.40 (n/a)</td><td>627.04 (n/a)</td><td>516.80 (n/a)</td><td>243.50 (n/a)</td><td>423.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (-6.16%)</td><td>0.01 <b>(-32.23%)</b></td><td>0.01 <b>(-32.88%)</b></td><td>0.00 <b>(-73.75%)</b></td><td>0.00 <b>(+65.11%)</b></td><td>1904.20 <b>(+280.92%)</b></td><td>713.98 <b>(+114.86%)</b></td><td>437.40 <b>(+48.98%)</b></td><td>302.00 (+6.56%)</td><td>673.16 <b>(+616.57%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>499.90 (n/a)</td><td>332.30 (n/a)</td><td>293.60 (n/a)</td><td>283.40 (n/a)</td><td>93.94 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 <b>(-35.91%)</b></td><td>0.01 <b>(-27.92%)</b></td><td>0.01 (-16.90%)</td><td>0.01 (-18.58%)</td><td>0.00 <b>(-56.00%)</b></td><td>650.80 <b>(+22.82%)</b></td><td>548.30 <b>(+34.00%)</b></td><td>527.40 <b>(+20.33%)</b></td><td>448.00 <b>(+56.04%)</b></td><td>92.62 (-12.01%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.90 (n/a)</td><td>409.18 (n/a)</td><td>438.30 (n/a)</td><td>287.10 (n/a)</td><td>105.26 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (-13.87%)</td><td>0.01 (-14.08%)</td><td>0.01 (-4.08%)</td><td>0.00 <b>(-74.03%)</b></td><td>0.00 (+17.03%)</td><td>2440.20 <b>(+285.01%)</b></td><td>772.46 <b>(+91.24%)</b></td><td>391.80 (+4.26%)</td><td>276.10 (+16.11%)</td><td>933.61 <b>(+505.94%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>633.80 (n/a)</td><td>403.92 (n/a)</td><td>375.80 (n/a)</td><td>237.80 (n/a)</td><td>154.07 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (+17.42%)</td><td>0.01 <b>(+23.53%)</b></td><td>0.01 <b>(+25.19%)</b></td><td>0.01 <b>(+22.36%)</b></td><td>0.00 (+14.73%)</td><td>551.50 (-18.27%)</td><td>418.98 (-19.52%)</td><td>469.50 <b>(-20.11%)</b></td><td>245.90 (-14.85%)</td><td>123.99 (-18.82%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>674.80 (n/a)</td><td>520.58 (n/a)</td><td>587.70 (n/a)</td><td>288.80 (n/a)</td><td>152.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 <b>(-32.65%)</b></td><td>0.01 <b>(-26.82%)</b></td><td>0.01 <b>(-28.05%)</b></td><td>0.01 <b>(-24.56%)</b></td><td>0.00 <b>(-49.86%)</b></td><td>670.10 <b>(+32.56%)</b></td><td>474.88 <b>(+30.68%)</b></td><td>448.30 <b>(+39.01%)</b></td><td>372.90 <b>(+48.45%)</b></td><td>120.32 (-1.82%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.50 (n/a)</td><td>363.38 (n/a)</td><td>322.50 (n/a)</td><td>251.20 (n/a)</td><td>122.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (+8.18%)</td><td>0.02 <b>(-24.08%)</b></td><td>0.02 <b>(-42.94%)</b></td><td>0.01 <b>(-30.89%)</b></td><td>0.01 <b>(+65.15%)</b></td><td>629.90 <b>(+44.70%)</b></td><td>443.96 <b>(+51.26%)</b></td><td>500.60 <b>(+75.28%)</b></td><td>198.40 (-7.55%)</td><td>189.95 <b>(+121.61%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>435.30 (n/a)</td><td>293.50 (n/a)</td><td>285.60 (n/a)</td><td>214.60 (n/a)</td><td>85.71 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 <b>(-24.99%)</b></td><td>0.02 <b>(-39.18%)</b></td><td>0.02 <b>(-41.42%)</b></td><td>0.01 <b>(-26.37%)</b></td><td>0.01 <b>(-29.39%)</b></td><td>682.30 <b>(+35.84%)</b></td><td>495.22 <b>(+62.17%)</b></td><td>508.20 <b>(+70.71%)</b></td><td>279.40 <b>(+33.30%)</b></td><td>144.03 <b>(+21.51%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.30 (n/a)</td><td>305.38 (n/a)</td><td>297.70 (n/a)</td><td>209.60 (n/a)</td><td>118.54 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (-12.28%)</td><td>0.02 (+1.82%)</td><td>0.02 (+16.78%)</td><td>0.02 <b>(+268.47%)</b></td><td>0.01 <b>(-51.39%)</b></td><td>541.10 <b>(-72.86%)</b></td><td>407.46 <b>(-41.68%)</b></td><td>419.50 (-14.37%)</td><td>261.30 (+14.01%)</td><td>111.60 <b>(-84.87%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1993.80 (n/a)</td><td>698.70 (n/a)</td><td>489.90 (n/a)</td><td>229.20 (n/a)</td><td>737.44 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (-0.26%)</td><td>0.03 (-2.83%)</td><td>0.02 <b>(-24.54%)</b></td><td>0.02 (+6.54%)</td><td>0.01 (-2.94%)</td><td>455.10 (-6.15%)</td><td>347.74 (+1.86%)</td><td>381.90 <b>(+32.51%)</b></td><td>239.80 (+0.25%)</td><td>91.20 (-12.72%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>484.90 (n/a)</td><td>341.40 (n/a)</td><td>288.20 (n/a)</td><td>239.20 (n/a)</td><td>104.48 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 <b>(-21.68%)</b></td><td>0.02 <b>(-29.40%)</b></td><td>0.03 (-10.87%)</td><td>0.00 <b>(-76.50%)</b></td><td>0.01 <b>(+27.64%)</b></td><td>1909.70 <b>(+325.61%)</b></td><td>705.38 <b>(+129.42%)</b></td><td>324.70 (+12.20%)</td><td>248.60 <b>(+27.68%)</b></td><td>706.72 <b>(+571.48%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>448.70 (n/a)</td><td>307.46 (n/a)</td><td>289.40 (n/a)</td><td>194.70 (n/a)</td><td>105.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (-4.93%)</td><td>0.02 (+15.05%)</td><td>0.03 <b>(+55.68%)</b></td><td>0.01 <b>(+244.73%)</b></td><td>0.01 <b>(-22.18%)</b></td><td>596.30 <b>(-70.99%)</b></td><td>398.62 <b>(-43.03%)</b></td><td>293.00 <b>(-35.77%)</b></td><td>237.20 (+5.19%)</td><td>178.84 <b>(-76.64%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2055.60 (n/a)</td><td>699.76 (n/a)</td><td>456.20 (n/a)</td><td>225.50 (n/a)</td><td>765.46 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (-3.22%)</td><td>0.02 (-16.73%)</td><td>0.02 <b>(-36.16%)</b></td><td>0.01 (-16.82%)</td><td>0.01 (+1.43%)</td><td>641.80 <b>(+20.21%)</b></td><td>445.80 <b>(+23.32%)</b></td><td>484.50 <b>(+56.64%)</b></td><td>247.80 (+3.34%)</td><td>170.49 <b>(+24.87%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.90 (n/a)</td><td>361.50 (n/a)</td><td>309.30 (n/a)</td><td>239.80 (n/a)</td><td>136.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (+11.16%)</td><td>0.03 (+4.02%)</td><td>0.02 (-15.40%)</td><td>0.01 (-2.59%)</td><td>0.01 (+2.42%)</td><td>587.40 (+2.67%)</td><td>362.96 (-4.98%)</td><td>358.10 (+18.22%)</td><td>222.60 (-10.02%)</td><td>145.68 (-8.54%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.10 (n/a)</td><td>381.98 (n/a)</td><td>302.90 (n/a)</td><td>247.40 (n/a)</td><td>159.28 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (-4.96%)</td><td>0.02 (+0.63%)</td><td>0.02 (+2.27%)</td><td>0.01 (-10.10%)</td><td>0.01 (+8.57%)</td><td>617.20 (+11.23%)</td><td>457.64 (+2.43%)</td><td>524.20 (-2.22%)</td><td>265.10 (+5.24%)</td><td>166.94 <b>(+21.46%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.90 (n/a)</td><td>446.80 (n/a)</td><td>536.10 (n/a)</td><td>251.90 (n/a)</td><td>137.45 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (-9.00%)</td><td>0.02 <b>(-33.51%)</b></td><td>0.01 <b>(-57.45%)</b></td><td>0.01 <b>(-33.92%)</b></td><td>0.01 (+18.56%)</td><td>838.80 <b>(+51.33%)</b></td><td>523.70 <b>(+66.13%)</b></td><td>591.80 <b>(+135.03%)</b></td><td>258.30 (+9.91%)</td><td>242.70 <b>(+79.42%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.30 (n/a)</td><td>315.24 (n/a)</td><td>251.80 (n/a)</td><td>235.00 (n/a)</td><td>135.27 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (-0.98%)</td><td>0.02 (-3.53%)</td><td>0.02 (+7.57%)</td><td>0.02 (+11.18%)</td><td>0.01 (+0.75%)</td><td>520.40 (-10.06%)</td><td>382.90 (+3.22%)</td><td>329.50 (-7.03%)</td><td>271.70 (+1.00%)</td><td>111.68 (-8.62%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.60 (n/a)</td><td>370.96 (n/a)</td><td>354.40 (n/a)</td><td>269.00 (n/a)</td><td>122.22 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(-20.78%)</b></td><td>0.02 (-9.05%)</td><td>0.02 (-8.34%)</td><td>0.01 <b>(+22.39%)</b></td><td>0.00 <b>(-52.86%)</b></td><td>551.80 (-18.30%)</td><td>436.34 (+0.09%)</td><td>456.60 (+9.10%)</td><td>332.10 <b>(+26.23%)</b></td><td>85.27 <b>(-50.43%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>675.40 (n/a)</td><td>435.96 (n/a)</td><td>418.50 (n/a)</td><td>263.10 (n/a)</td><td>172.01 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (+10.25%)</td><td>0.04 <b>(-22.99%)</b></td><td>0.04 <b>(-41.16%)</b></td><td>0.03 (+1.18%)</td><td>0.02 (+14.06%)</td><td>528.50 (-1.16%)</td><td>424.36 <b>(+30.48%)</b></td><td>455.90 <b>(+69.92%)</b></td><td>235.20 (-9.29%)</td><td>111.52 (-5.91%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>534.70 (n/a)</td><td>325.22 (n/a)</td><td>268.30 (n/a)</td><td>259.30 (n/a)</td><td>118.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (-7.73%)</td><td>0.06 (+9.08%)</td><td>0.06 (+2.75%)</td><td>0.04 <b>(+27.57%)</b></td><td>0.01 <b>(-46.26%)</b></td><td>438.50 <b>(-21.61%)</b></td><td>307.56 (-17.68%)</td><td>278.30 (-2.69%)</td><td>251.00 (+8.38%)</td><td>74.82 <b>(-54.23%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>559.40 (n/a)</td><td>373.62 (n/a)</td><td>286.00 (n/a)</td><td>231.60 (n/a)</td><td>163.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (+13.42%)</td><td>0.04 <b>(-36.81%)</b></td><td>0.03 <b>(-55.58%)</b></td><td>0.03 <b>(-40.73%)</b></td><td>0.02 <b>(+143.85%)</b></td><td>599.50 <b>(+68.73%)</b></td><td>502.02 <b>(+86.60%)</b></td><td>571.00 <b>(+125.16%)</b></td><td>195.20 (-11.83%)</td><td>172.07 <b>(+238.26%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>355.30 (n/a)</td><td>269.04 (n/a)</td><td>253.60 (n/a)</td><td>221.40 (n/a)</td><td>50.87 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (-6.59%)</td><td>0.05 <b>(-25.07%)</b></td><td>0.04 <b>(-30.28%)</b></td><td>0.03 <b>(-38.30%)</b></td><td>0.01 <b>(+147.02%)</b></td><td>492.00 <b>(+62.06%)</b></td><td>381.06 <b>(+39.97%)</b></td><td>379.50 <b>(+43.42%)</b></td><td>262.90 (+7.04%)</td><td>94.67 <b>(+330.27%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>303.60 (n/a)</td><td>272.24 (n/a)</td><td>264.60 (n/a)</td><td>245.60 (n/a)</td><td>22.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (-9.77%)</td><td>0.04 <b>(-21.00%)</b></td><td>0.03 <b>(-29.90%)</b></td><td>0.03 <b>(-26.62%)</b></td><td>0.01 (+12.78%)</td><td>527.20 <b>(+36.30%)</b></td><td>414.86 <b>(+32.05%)</b></td><td>490.80 <b>(+42.67%)</b></td><td>261.80 (+10.79%)</td><td>125.60 <b>(+77.42%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>386.80 (n/a)</td><td>314.18 (n/a)</td><td>344.00 (n/a)</td><td>236.30 (n/a)</td><td>70.79 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (+0.16%)</td><td>0.05 <b>(-23.41%)</b></td><td>0.04 <b>(-31.79%)</b></td><td>0.03 <b>(-34.28%)</b></td><td>0.02 <b>(+66.29%)</b></td><td>521.40 <b>(+52.14%)</b></td><td>388.40 <b>(+42.09%)</b></td><td>379.70 <b>(+46.60%)</b></td><td>214.10 (-0.19%)</td><td>134.08 <b>(+162.46%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>342.70 (n/a)</td><td>273.34 (n/a)</td><td>259.00 (n/a)</td><td>214.50 (n/a)</td><td>51.09 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (-12.18%)</td><td>0.03 (-8.37%)</td><td>0.03 (+2.88%)</td><td>0.01 <b>(-57.11%)</b></td><td>0.01 (+18.17%)</td><td>2474.30 <b>(+133.14%)</b></td><td>938.22 <b>(+41.54%)</b></td><td>536.00 (-2.81%)</td><td>504.80 (+13.87%)</td><td>860.36 <b>(+232.77%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1061.30 (n/a)</td><td>662.88 (n/a)</td><td>551.50 (n/a)</td><td>443.30 (n/a)</td><td>258.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (+10.49%)</td><td>0.06 (+11.58%)</td><td>0.06 <b>(+36.12%)</b></td><td>0.03 <b>(-20.01%)</b></td><td>0.02 <b>(+34.05%)</b></td><td>602.90 <b>(+25.01%)</b></td><td>352.18 (-2.46%)</td><td>282.30 <b>(-26.52%)</b></td><td>191.80 (-9.53%)</td><td>170.48 <b>(+54.95%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>482.30 (n/a)</td><td>361.06 (n/a)</td><td>384.20 (n/a)</td><td>212.00 (n/a)</td><td>110.02 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 <b>(+48.98%)</b></td><td>0.04 (-5.03%)</td><td>0.04 <b>(-20.97%)</b></td><td>0.03 (-11.57%)</td><td>0.03 <b>(+112.96%)</b></td><td>602.90 (+13.07%)</td><td>454.32 (+18.93%)</td><td>462.50 <b>(+26.54%)</b></td><td>184.70 <b>(-32.86%)</b></td><td>163.93 <b>(+53.82%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>533.20 (n/a)</td><td>382.00 (n/a)</td><td>365.50 (n/a)</td><td>275.10 (n/a)</td><td>106.57 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (-13.03%)</td><td>0.04 <b>(-26.23%)</b></td><td>0.04 <b>(-37.57%)</b></td><td>0.03 (-14.57%)</td><td>0.01 <b>(-21.81%)</b></td><td>573.30 (+17.07%)</td><td>468.08 <b>(+34.21%)</b></td><td>462.20 <b>(+60.15%)</b></td><td>309.80 (+15.00%)</td><td>105.34 (+6.51%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>489.70 (n/a)</td><td>348.76 (n/a)</td><td>288.60 (n/a)</td><td>269.40 (n/a)</td><td>98.90 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (-12.06%)</td><td>0.04 (+6.33%)</td><td>0.03 (-1.77%)</td><td>0.03 <b>(+205.88%)</b></td><td>0.01 <b>(-41.07%)</b></td><td>642.70 <b>(-67.31%)</b></td><td>474.10 <b>(-36.70%)</b></td><td>494.10 (+1.79%)</td><td>278.00 (+13.70%)</td><td>130.89 <b>(-81.19%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1965.80 (n/a)</td><td>748.94 (n/a)</td><td>485.40 (n/a)</td><td>244.50 (n/a)</td><td>695.69 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (-5.19%)</td><td>0.03 (-18.06%)</td><td>0.03 (-19.59%)</td><td>0.02 (-18.68%)</td><td>0.01 (-15.51%)</td><td>815.40 <b>(+22.95%)</b></td><td>584.50 <b>(+20.77%)</b></td><td>626.30 <b>(+24.36%)</b></td><td>320.10 (+5.47%)</td><td>191.94 (+9.94%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>663.20 (n/a)</td><td>483.96 (n/a)</td><td>503.60 (n/a)</td><td>303.50 (n/a)</td><td>174.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 <b>(+38.41%)</b></td><td>0.12 (+17.51%)</td><td>0.13 (+8.96%)</td><td>0.07 (+12.01%)</td><td>0.05 <b>(+40.86%)</b></td><td>484.70 (-10.72%)</td><td>327.88 (-11.63%)</td><td>256.10 (-8.24%)</td><td>191.80 <b>(-27.76%)</b></td><td>139.46 (+0.36%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>542.90 (n/a)</td><td>371.04 (n/a)</td><td>279.10 (n/a)</td><td>265.50 (n/a)</td><td>138.95 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (+12.96%)</td><td>0.07 <b>(-29.31%)</b></td><td>0.07 <b>(-36.44%)</b></td><td>0.02 <b>(-75.41%)</b></td><td>0.04 <b>(+72.40%)</b></td><td>1908.00 <b>(+306.65%)</b></td><td>738.98 <b>(+109.68%)</b></td><td>478.70 <b>(+57.31%)</b></td><td>234.20 (-11.49%)</td><td>666.71 <b>(+571.23%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>469.20 (n/a)</td><td>352.44 (n/a)</td><td>304.30 (n/a)</td><td>264.60 (n/a)</td><td>99.33 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 <b>(-32.25%)</b></td><td>0.07 (-11.91%)</td><td>0.06 (-2.63%)</td><td>0.05 (-5.17%)</td><td>0.02 <b>(-52.24%)</b></td><td>614.50 (+5.46%)</td><td>498.26 (+4.44%)</td><td>533.70 (+2.69%)</td><td>323.40 <b>(+47.60%)</b></td><td>111.60 <b>(-24.32%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>582.70 (n/a)</td><td>477.08 (n/a)</td><td>519.70 (n/a)</td><td>219.10 (n/a)</td><td>147.46 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (-14.67%)</td><td>0.08 <b>(-24.16%)</b></td><td>0.07 <b>(-47.20%)</b></td><td>0.06 (-6.37%)</td><td>0.02 <b>(-34.18%)</b></td><td>554.80 (+6.79%)</td><td>441.60 <b>(+25.31%)</b></td><td>486.80 <b>(+89.42%)</b></td><td>287.90 (+17.18%)</td><td>116.68 (-16.32%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>519.50 (n/a)</td><td>352.40 (n/a)</td><td>257.00 (n/a)</td><td>245.70 (n/a)</td><td>139.44 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (+15.81%)</td><td>0.11 <b>(+23.45%)</b></td><td>0.11 <b>(+52.96%)</b></td><td>0.06 (-19.40%)</td><td>0.04 <b>(+21.82%)</b></td><td>590.00 <b>(+24.08%)</b></td><td>332.60 (-15.31%)</td><td>302.00 <b>(-34.62%)</b></td><td>196.00 (-13.66%)</td><td>150.31 <b>(+35.66%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>475.50 (n/a)</td><td>392.72 (n/a)</td><td>461.90 (n/a)</td><td>227.00 (n/a)</td><td>110.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 (+14.19%)</td><td>0.12 (+2.47%)</td><td>0.12 (+1.50%)</td><td>0.06 <b>(-23.06%)</b></td><td>0.04 <b>(+74.28%)</b></td><td>519.20 <b>(+29.96%)</b></td><td>309.44 (+5.31%)</td><td>275.30 (-1.50%)</td><td>198.40 (-12.44%)</td><td>126.78 <b>(+97.16%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>399.50 (n/a)</td><td>293.84 (n/a)</td><td>279.50 (n/a)</td><td>226.60 (n/a)</td><td>64.30 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.12 (+5.98%)</td><td>0.09 (+2.70%)</td><td>0.10 (-3.61%)</td><td>0.06 (-6.89%)</td><td>0.03 (+19.00%)</td><td>571.80 (+7.40%)</td><td>388.58 (-0.03%)</td><td>318.70 (+3.74%)</td><td>270.60 (-5.65%)</td><td>142.25 (+16.20%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>532.40 (n/a)</td><td>388.70 (n/a)</td><td>307.20 (n/a)</td><td>286.80 (n/a)</td><td>122.42 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 <b>(-38.33%)</b></td><td>0.06 <b>(-32.23%)</b></td><td>0.06 (-9.55%)</td><td>0.01 <b>(-78.78%)</b></td><td>0.03 (-14.60%)</td><td>2464.30 <b>(+371.19%)</b></td><td>863.90 <b>(+112.87%)</b></td><td>528.70 (+10.56%)</td><td>389.10 <b>(+62.13%)</b></td><td>897.46 <b>(+585.79%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>523.00 (n/a)</td><td>405.84 (n/a)</td><td>478.20 (n/a)</td><td>240.00 (n/a)</td><td>130.87 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.15 <b>(+83.12%)</b></td><td>0.08 <b>(+23.17%)</b></td><td>0.06 (-2.98%)</td><td>0.06 <b>(+48.19%)</b></td><td>0.04 <b>(+139.53%)</b></td><td>594.80 <b>(-32.52%)</b></td><td>476.18 (-13.29%)</td><td>529.00 (+3.08%)</td><td>212.60 <b>(-45.40%)</b></td><td>151.96 <b>(-21.42%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>881.50 (n/a)</td><td>549.16 (n/a)</td><td>513.20 (n/a)</td><td>389.40 (n/a)</td><td>193.38 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.18 <b>(+31.33%)</b></td><td>0.10 (+14.37%)</td><td>0.09 <b>(+37.22%)</b></td><td>0.05 <b>(-26.46%)</b></td><td>0.05 <b>(+64.19%)</b></td><td>696.30 <b>(+35.97%)</b></td><td>402.50 (-2.72%)</td><td>346.20 <b>(-27.13%)</b></td><td>184.10 <b>(-23.86%)</b></td><td>188.51 <b>(+68.82%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>512.10 (n/a)</td><td>413.76 (n/a)</td><td>475.10 (n/a)</td><td>241.80 (n/a)</td><td>111.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 <b>(-21.35%)</b></td><td>0.07 (-0.66%)</td><td>0.06 (+3.96%)</td><td>0.05 (+2.51%)</td><td>0.02 <b>(-35.75%)</b></td><td>601.40 (-2.45%)</td><td>489.70 (-2.85%)</td><td>536.20 (-3.82%)</td><td>359.10 <b>(+27.12%)</b></td><td>108.44 (-16.81%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>616.50 (n/a)</td><td>504.06 (n/a)</td><td>557.50 (n/a)</td><td>282.50 (n/a)</td><td>130.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 <b>(-36.91%)</b></td><td>0.07 (-18.05%)</td><td>0.06 (-10.07%)</td><td>0.05 (-9.90%)</td><td>0.01 <b>(-55.11%)</b></td><td>615.30 (+10.98%)</td><td>514.42 (+16.54%)</td><td>547.10 (+11.20%)</td><td>409.50 <b>(+58.54%)</b></td><td>92.69 (-19.91%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>554.40 (n/a)</td><td>441.42 (n/a)</td><td>492.00 (n/a)</td><td>258.30 (n/a)</td><td>115.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (-5.57%)</td><td>0.01 (-9.41%)</td><td>0.01 <b>(-32.39%)</b></td><td>0.01 (-9.28%)</td><td>0.00 (-5.28%)</td><td>578.00 (+10.22%)</td><td>413.68 (+9.93%)</td><td>446.40 <b>(+47.91%)</b></td><td>267.80 (+5.89%)</td><td>128.46 (+1.19%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.40 (n/a)</td><td>376.32 (n/a)</td><td>301.80 (n/a)</td><td>252.90 (n/a)</td><td>126.94 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (+5.27%)</td><td>0.02 (+6.23%)</td><td>0.02 (+4.56%)</td><td>0.01 (+4.64%)</td><td>0.01 (-14.84%)</td><td>609.50 (-4.44%)</td><td>330.28 (-10.93%)</td><td>284.50 (-4.34%)</td><td>192.10 (-5.00%)</td><td>161.66 (-14.86%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.80 (n/a)</td><td>370.82 (n/a)</td><td>297.40 (n/a)</td><td>202.20 (n/a)</td><td>189.86 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (+17.56%)</td><td>0.01 (-5.87%)</td><td>0.01 <b>(-39.11%)</b></td><td>0.01 (-8.80%)</td><td>0.01 <b>(+40.94%)</b></td><td>584.00 (+9.63%)</td><td>431.76 (+13.53%)</td><td>487.40 <b>(+64.22%)</b></td><td>230.20 (-14.96%)</td><td>169.49 <b>(+32.03%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.70 (n/a)</td><td>380.30 (n/a)</td><td>296.80 (n/a)</td><td>270.70 (n/a)</td><td>128.37 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (-4.13%)</td><td>0.01 (+1.32%)</td><td>0.01 (-9.60%)</td><td>0.01 (-7.93%)</td><td>0.00 <b>(+21.14%)</b></td><td>573.30 (+8.62%)</td><td>438.16 (+2.23%)</td><td>516.00 (+10.63%)</td><td>283.80 (+4.30%)</td><td>139.79 <b>(+31.80%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.80 (n/a)</td><td>428.60 (n/a)</td><td>466.40 (n/a)</td><td>272.10 (n/a)</td><td>106.06 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 (-16.37%)</td><td>0.01 (+14.13%)</td><td>0.01 <b>(+93.35%)</b></td><td>0.00 <b>(+79.97%)</b></td><td>0.00 <b>(-35.98%)</b></td><td>1090.70 <b>(-44.44%)</b></td><td>517.94 <b>(-47.78%)</b></td><td>300.20 <b>(-48.29%)</b></td><td>283.30 (+19.59%)</td><td>349.46 <b>(-60.63%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1963.00 (n/a)</td><td>991.92 (n/a)</td><td>580.50 (n/a)</td><td>236.90 (n/a)</td><td>887.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(-22.81%)</b></td><td>0.02 (+10.37%)</td><td>0.01 (+9.33%)</td><td>0.01 <b>(+373.63%)</b></td><td>0.00 <b>(-56.13%)</b></td><td>439.60 <b>(-78.88%)</b></td><td>353.36 <b>(-48.82%)</b></td><td>344.10 (-8.53%)</td><td>248.20 <b>(+29.54%)</b></td><td>85.05 <b>(-89.15%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2081.90 (n/a)</td><td>690.44 (n/a)</td><td>376.20 (n/a)</td><td>191.60 (n/a)</td><td>784.03 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (+0.91%)</td><td>0.01 <b>(+23.44%)</b></td><td>0.01 <b>(+47.43%)</b></td><td>0.01 <b>(+307.45%)</b></td><td>0.00 <b>(-38.27%)</b></td><td>468.10 <b>(-75.46%)</b></td><td>342.64 <b>(-48.24%)</b></td><td>290.10 <b>(-32.17%)</b></td><td>258.80 (-0.88%)</td><td>98.17 <b>(-85.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1907.40 (n/a)</td><td>662.04 (n/a)</td><td>427.70 (n/a)</td><td>261.10 (n/a)</td><td>700.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(+21.00%)</b></td><td>0.01 (-3.91%)</td><td>0.01 (-14.06%)</td><td>0.01 (-3.77%)</td><td>0.00 <b>(+30.19%)</b></td><td>634.60 (+3.91%)</td><td>489.90 (+7.66%)</td><td>536.20 (+16.34%)</td><td>245.20 (-17.33%)</td><td>159.91 (+10.37%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.70 (n/a)</td><td>455.04 (n/a)</td><td>460.90 (n/a)</td><td>296.60 (n/a)</td><td>144.88 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 <b>(+24.42%)</b></td><td>0.02 <b>(+50.62%)</b></td><td>0.02 <b>(+69.88%)</b></td><td>0.01 <b>(+47.11%)</b></td><td>0.00 (-2.41%)</td><td>338.00 <b>(-32.03%)</b></td><td>261.34 <b>(-35.40%)</b></td><td>246.40 <b>(-41.12%)</b></td><td>194.60 (-19.62%)</td><td>55.07 <b>(-42.92%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>497.30 (n/a)</td><td>404.58 (n/a)</td><td>418.50 (n/a)</td><td>242.10 (n/a)</td><td>96.47 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.02 (+11.34%)</td><td>0.01 (+16.24%)</td><td>0.01 <b>(+37.28%)</b></td><td>0.01 (-2.00%)</td><td>0.00 <b>(+79.64%)</b></td><td>501.70 (+2.05%)</td><td>378.16 (-10.87%)</td><td>320.00 <b>(-27.16%)</b></td><td>295.90 (-10.17%)</td><td>100.47 <b>(+69.77%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.60 (n/a)</td><td>424.26 (n/a)</td><td>439.30 (n/a)</td><td>329.40 (n/a)</td><td>59.18 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.01 <b>(-51.13%)</b></td><td>0.01 <b>(-38.79%)</b></td><td>0.01 <b>(-29.47%)</b></td><td>0.01 (-16.30%)</td><td>0.00 <b>(-73.68%)</b></td><td>618.20 (+19.48%)</td><td>556.52 <b>(+48.15%)</b></td><td>599.00 <b>(+41.78%)</b></td><td>416.60 <b>(+104.62%)</b></td><td>83.83 <b>(-35.79%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>517.40 (n/a)</td><td>375.64 (n/a)</td><td>422.50 (n/a)</td><td>203.60 (n/a)</td><td>130.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (+2.31%)</td><td>0.03 (-6.61%)</td><td>0.03 (+1.15%)</td><td>0.01 <b>(-24.60%)</b></td><td>0.01 <b>(+42.96%)</b></td><td>557.70 <b>(+32.63%)</b></td><td>344.06 (+16.71%)</td><td>283.10 (-1.12%)</td><td>196.70 (-2.24%)</td><td>148.55 <b>(+87.21%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>420.50 (n/a)</td><td>294.80 (n/a)</td><td>286.30 (n/a)</td><td>201.20 (n/a)</td><td>79.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (+10.51%)</td><td>0.04 <b>(+45.85%)</b></td><td>0.04 <b>(+50.07%)</b></td><td>0.02 <b>(+221.48%)</b></td><td>0.02 <b>(-20.33%)</b></td><td>621.40 <b>(-68.89%)</b></td><td>372.20 <b>(-62.51%)</b></td><td>297.80 <b>(-33.36%)</b></td><td>219.90 (-9.51%)</td><td>177.98 <b>(-80.66%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1997.50 (n/a)</td><td>992.86 (n/a)</td><td>446.90 (n/a)</td><td>243.00 (n/a)</td><td>920.04 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 <b>(+28.49%)</b></td><td>0.03 <b>(+28.83%)</b></td><td>0.03 <b>(+89.53%)</b></td><td>0.02 (+17.63%)</td><td>0.01 (+16.03%)</td><td>484.30 (-14.98%)</td><td>322.34 <b>(-22.64%)</b></td><td>244.30 <b>(-47.24%)</b></td><td>188.10 <b>(-22.14%)</b></td><td>138.51 (-15.23%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.60 (n/a)</td><td>416.68 (n/a)</td><td>463.00 (n/a)</td><td>241.60 (n/a)</td><td>163.39 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 <b>(+23.76%)</b></td><td>0.03 <b>(+48.63%)</b></td><td>0.04 <b>(+65.71%)</b></td><td>0.02 <b>(+32.42%)</b></td><td>0.01 (+4.27%)</td><td>429.90 <b>(-24.49%)</b></td><td>307.74 <b>(-33.58%)</b></td><td>288.40 <b>(-39.64%)</b></td><td>239.20 (-19.19%)</td><td>71.77 <b>(-29.42%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>569.30 (n/a)</td><td>463.34 (n/a)</td><td>477.80 (n/a)</td><td>296.00 (n/a)</td><td>101.68 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (+7.91%)</td><td>0.02 (+0.15%)</td><td>0.03 (-12.49%)</td><td>0.02 (+3.08%)</td><td>0.01 (+6.72%)</td><td>542.40 (-2.99%)</td><td>374.76 (+0.54%)</td><td>312.40 (+14.26%)</td><td>236.60 (-7.32%)</td><td>148.16 (+0.55%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.10 (n/a)</td><td>372.76 (n/a)</td><td>273.40 (n/a)</td><td>255.30 (n/a)</td><td>147.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (-8.81%)</td><td>0.03 <b>(+26.15%)</b></td><td>0.04 <b>(+86.20%)</b></td><td>0.02 (-14.19%)</td><td>0.01 (-4.79%)</td><td>640.30 (+16.52%)</td><td>351.18 (-18.75%)</td><td>252.90 <b>(-46.28%)</b></td><td>221.70 (+9.64%)</td><td>176.00 <b>(+27.62%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>549.50 (n/a)</td><td>432.24 (n/a)</td><td>470.80 (n/a)</td><td>202.20 (n/a)</td><td>137.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 <b>(+24.37%)</b></td><td>0.02 (-5.22%)</td><td>0.01 (-18.29%)</td><td>0.01 <b>(-54.32%)</b></td><td>0.01 <b>(+51.63%)</b></td><td>1307.20 <b>(+118.92%)</b></td><td>592.90 <b>(+38.59%)</b></td><td>559.60 <b>(+22.37%)</b></td><td>191.80 (-19.61%)</td><td>435.31 <b>(+162.88%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.10 (n/a)</td><td>427.82 (n/a)</td><td>457.30 (n/a)</td><td>238.60 (n/a)</td><td>165.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 (+4.95%)</td><td>0.02 (-8.57%)</td><td>0.02 (+2.91%)</td><td>0.00 <b>(-74.94%)</b></td><td>0.01 <b>(+53.45%)</b></td><td>2306.50 <b>(+298.98%)</b></td><td>847.26 <b>(+70.76%)</b></td><td>529.90 (-2.84%)</td><td>260.40 (-4.72%)</td><td>834.06 <b>(+553.42%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>578.10 (n/a)</td><td>496.16 (n/a)</td><td>545.40 (n/a)</td><td>273.30 (n/a)</td><td>127.64 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 <b>(+23.13%)</b></td><td>0.02 (+5.97%)</td><td>0.01 <b>(-21.19%)</b></td><td>0.01 <b>(-45.22%)</b></td><td>0.02 <b>(+77.07%)</b></td><td>1065.60 <b>(+82.56%)</b></td><td>544.08 <b>(+27.07%)</b></td><td>592.10 <b>(+26.90%)</b></td><td>197.70 (-18.78%)</td><td>363.33 <b>(+121.66%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.70 (n/a)</td><td>428.18 (n/a)</td><td>466.60 (n/a)</td><td>243.40 (n/a)</td><td>163.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.04 <b>(+32.31%)</b></td><td>0.02 (+10.34%)</td><td>0.02 (-3.43%)</td><td>0.02 (-1.65%)</td><td>0.01 <b>(+69.57%)</b></td><td>587.00 (+1.68%)</td><td>435.24 (-2.64%)</td><td>501.00 (+3.56%)</td><td>231.00 <b>(-24.41%)</b></td><td>157.65 <b>(+34.41%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>577.30 (n/a)</td><td>447.06 (n/a)</td><td>483.80 (n/a)</td><td>305.60 (n/a)</td><td>117.29 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.03 (+4.51%)</td><td>0.02 (+11.90%)</td><td>0.02 (+9.20%)</td><td>0.01 (-5.21%)</td><td>0.01 (+1.11%)</td><td>600.80 (+5.50%)</td><td>368.26 (-10.78%)</td><td>356.70 (-8.42%)</td><td>241.80 (-4.31%)</td><td>141.18 (-0.83%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.50 (n/a)</td><td>412.76 (n/a)</td><td>389.50 (n/a)</td><td>252.70 (n/a)</td><td>142.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 <b>(+42.26%)</b></td><td>0.07 <b>(+42.17%)</b></td><td>0.06 <b>(+30.96%)</b></td><td>0.05 <b>(+71.06%)</b></td><td>0.02 (-1.95%)</td><td>304.40 <b>(-41.53%)</b></td><td>246.72 <b>(-33.70%)</b></td><td>257.30 <b>(-23.65%)</b></td><td>171.20 <b>(-29.69%)</b></td><td>48.26 <b>(-62.35%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>520.60 (n/a)</td><td>372.12 (n/a)</td><td>337.00 (n/a)</td><td>243.50 (n/a)</td><td>128.19 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (+12.19%)</td><td>0.07 (-6.12%)</td><td>0.06 <b>(-35.17%)</b></td><td>0.04 (-4.10%)</td><td>0.03 (+9.37%)</td><td>657.70 (+4.28%)</td><td>429.64 (+7.33%)</td><td>446.20 <b>(+54.23%)</b></td><td>233.90 (-10.86%)</td><td>170.45 (+0.11%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>630.70 (n/a)</td><td>400.30 (n/a)</td><td>289.30 (n/a)</td><td>262.40 (n/a)</td><td>170.27 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (+17.16%)</td><td>0.06 <b>(+27.57%)</b></td><td>0.06 <b>(+66.60%)</b></td><td>0.03 <b>(+65.42%)</b></td><td>0.02 (-9.47%)</td><td>488.10 <b>(-39.55%)</b></td><td>327.16 <b>(-28.67%)</b></td><td>290.90 <b>(-39.98%)</b></td><td>217.00 (-14.67%)</td><td>116.31 <b>(-48.84%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>807.40 (n/a)</td><td>458.64 (n/a)</td><td>484.70 (n/a)</td><td>254.30 (n/a)</td><td>227.34 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 <b>(+23.10%)</b></td><td>0.06 <b>(+46.36%)</b></td><td>0.07 <b>(+59.10%)</b></td><td>0.04 <b>(+258.69%)</b></td><td>0.02 <b>(-24.98%)</b></td><td>534.90 <b>(-72.12%)</b></td><td>338.40 <b>(-52.35%)</b></td><td>299.80 <b>(-37.15%)</b></td><td>252.40 (-18.76%)</td><td>113.99 <b>(-83.27%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1918.50 (n/a)</td><td>710.22 (n/a)</td><td>477.00 (n/a)</td><td>310.70 (n/a)</td><td>681.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (+9.39%)</td><td>0.06 (+9.51%)</td><td>0.07 (+18.54%)</td><td>0.02 (-13.96%)</td><td>0.02 <b>(+22.49%)</b></td><td>663.60 (+16.22%)</td><td>344.40 (-2.60%)</td><td>247.20 (-15.63%)</td><td>202.00 (-8.56%)</td><td>190.61 <b>(+31.70%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>571.00 (n/a)</td><td>353.60 (n/a)</td><td>293.00 (n/a)</td><td>220.90 (n/a)</td><td>144.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 <b>(-27.96%)</b></td><td>0.05 <b>(-33.85%)</b></td><td>0.04 <b>(-49.28%)</b></td><td>0.02 <b>(-47.75%)</b></td><td>0.02 <b>(-22.69%)</b></td><td>1131.20 <b>(+91.40%)</b></td><td>585.04 <b>(+62.10%)</b></td><td>544.90 <b>(+97.14%)</b></td><td>245.30 <b>(+38.82%)</b></td><td>338.27 <b>(+98.07%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>591.00 (n/a)</td><td>360.92 (n/a)</td><td>276.40 (n/a)</td><td>176.70 (n/a)</td><td>170.78 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 <b>(+38.13%)</b></td><td>0.05 <b>(+38.47%)</b></td><td>0.04 (+18.94%)</td><td>0.03 <b>(+64.86%)</b></td><td>0.02 <b>(+45.96%)</b></td><td>506.10 <b>(-39.35%)</b></td><td>362.70 <b>(-28.25%)</b></td><td>396.10 (-15.92%)</td><td>215.10 <b>(-27.58%)</b></td><td>132.26 <b>(-37.59%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>834.40 (n/a)</td><td>505.54 (n/a)</td><td>471.10 (n/a)</td><td>297.00 (n/a)</td><td>211.94 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 <b>(-22.86%)</b></td><td>0.04 (-16.69%)</td><td>0.04 (-9.65%)</td><td>0.03 (-5.63%)</td><td>0.01 <b>(-32.69%)</b></td><td>579.50 (+5.96%)</td><td>463.82 (+15.36%)</td><td>525.60 (+10.70%)</td><td>293.40 <b>(+29.65%)</b></td><td>132.23 (-4.81%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>546.90 (n/a)</td><td>402.06 (n/a)</td><td>474.80 (n/a)</td><td>226.30 (n/a)</td><td>138.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.06 (-17.73%)</td><td>0.04 (-14.85%)</td><td>0.03 (+12.86%)</td><td>0.03 (-1.61%)</td><td>0.01 <b>(-44.34%)</b></td><td>575.60 (+1.64%)</td><td>455.10 (+6.18%)</td><td>477.30 (-11.38%)</td><td>283.30 <b>(+21.54%)</b></td><td>116.27 <b>(-32.60%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>566.30 (n/a)</td><td>428.62 (n/a)</td><td>538.60 (n/a)</td><td>233.10 (n/a)</td><td>172.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (+14.47%)</td><td>0.05 <b>(+21.97%)</b></td><td>0.05 <b>(+47.17%)</b></td><td>0.03 (-4.82%)</td><td>0.02 (+10.59%)</td><td>653.00 (+5.07%)</td><td>377.82 (-16.83%)</td><td>360.20 <b>(-32.05%)</b></td><td>240.50 (-12.67%)</td><td>162.89 (+7.55%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>621.50 (n/a)</td><td>454.30 (n/a)</td><td>530.10 (n/a)</td><td>275.40 (n/a)</td><td>151.46 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.05 (-7.66%)</td><td>0.03 (-7.77%)</td><td>0.03 <b>(-20.98%)</b></td><td>0.03 (+10.86%)</td><td>0.01 <b>(-34.09%)</b></td><td>530.60 (-9.81%)</td><td>478.90 (+5.42%)</td><td>511.60 <b>(+26.57%)</b></td><td>363.60 (+8.31%)</td><td>69.33 <b>(-38.36%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.30 (n/a)</td><td>454.26 (n/a)</td><td>404.20 (n/a)</td><td>335.70 (n/a)</td><td>112.47 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.16 (+3.53%)</td><td>0.11 (+1.58%)</td><td>0.11 (+3.70%)</td><td>0.09 (+17.65%)</td><td>0.02 (-10.89%)</td><td>359.70 (-15.00%)</td><td>296.78 (-3.29%)</td><td>303.90 (-3.59%)</td><td>211.20 (-3.43%)</td><td>53.79 <b>(-30.04%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>423.20 (n/a)</td><td>306.88 (n/a)</td><td>315.20 (n/a)</td><td>218.70 (n/a)</td><td>76.89 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.15 (+13.53%)</td><td>0.10 <b>(+36.70%)</b></td><td>0.14 <b>(+105.89%)</b></td><td>0.02 <b>(-66.71%)</b></td><td>0.06 <b>(+87.44%)</b></td><td>1908.90 <b>(+200.38%)</b></td><td>631.14 <b>(+29.26%)</b></td><td>237.70 <b>(-51.43%)</b></td><td>218.70 (-11.92%)</td><td>729.80 <b>(+393.14%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>635.50 (n/a)</td><td>488.26 (n/a)</td><td>489.40 (n/a)</td><td>248.30 (n/a)</td><td>147.99 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.16 <b>(+20.93%)</b></td><td>0.14 <b>(+89.38%)</b></td><td>0.15 <b>(+86.78%)</b></td><td>0.07 <b>(+215.72%)</b></td><td>0.04 <b>(-22.91%)</b></td><td>594.90 <b>(-68.33%)</b></td><td>335.44 <b>(-66.35%)</b></td><td>279.20 <b>(-46.45%)</b></td><td>253.00 (-17.29%)</td><td>145.81 <b>(-81.91%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1878.30 (n/a)</td><td>996.88 (n/a)</td><td>521.40 (n/a)</td><td>305.90 (n/a)</td><td>805.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (+15.94%)</td><td>0.08 (+4.32%)</td><td>0.07 (+16.49%)</td><td>0.02 <b>(-63.13%)</b></td><td>0.05 <b>(+57.75%)</b></td><td>1958.80 <b>(+171.26%)</b></td><td>695.54 <b>(+45.35%)</b></td><td>441.80 (-14.15%)</td><td>241.80 (-13.77%)</td><td>717.29 <b>(+302.41%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>722.10 (n/a)</td><td>478.54 (n/a)</td><td>514.60 (n/a)</td><td>280.40 (n/a)</td><td>178.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (-12.42%)</td><td>0.11 (-9.63%)</td><td>0.12 (-7.34%)</td><td>0.07 (+15.14%)</td><td>0.03 <b>(-27.91%)</b></td><td>578.00 (-13.15%)</td><td>413.06 (+4.09%)</td><td>331.90 (+7.90%)</td><td>288.80 (+14.20%)</td><td>138.09 <b>(-23.50%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>665.50 (n/a)</td><td>396.84 (n/a)</td><td>307.60 (n/a)</td><td>252.90 (n/a)</td><td>180.51 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (-5.06%)</td><td>0.09 (+1.74%)</td><td>0.07 (-0.88%)</td><td>0.05 (-19.10%)</td><td>0.03 (-1.00%)</td><td>652.80 <b>(+23.61%)</b></td><td>425.80 (+0.67%)</td><td>453.40 (+0.89%)</td><td>237.30 (+5.33%)</td><td>157.62 <b>(+32.91%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>528.10 (n/a)</td><td>422.98 (n/a)</td><td>449.40 (n/a)</td><td>225.30 (n/a)</td><td>118.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 (-18.82%)</td><td>0.09 (-2.76%)</td><td>0.09 (+10.21%)</td><td>0.07 <b>(+72.20%)</b></td><td>0.02 <b>(-54.33%)</b></td><td>553.00 <b>(-41.93%)</b></td><td>421.14 (-16.00%)</td><td>431.90 (-9.26%)</td><td>291.40 <b>(+23.16%)</b></td><td>95.48 <b>(-66.68%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>952.30 (n/a)</td><td>501.38 (n/a)</td><td>476.00 (n/a)</td><td>236.60 (n/a)</td><td>286.56 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 <b>(+125.78%)</b></td><td>0.08 <b>(+31.57%)</b></td><td>0.07 (+6.62%)</td><td>0.02 (+1.44%)</td><td>0.06 <b>(+170.13%)</b></td><td>1985.80 (-1.42%)</td><td>986.12 <b>(+24.86%)</b></td><td>470.10 (-6.22%)</td><td>194.50 <b>(-55.70%)</b></td><td>915.64 <b>(+33.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>2014.40 (n/a)</td><td>789.76 (n/a)</td><td>501.30 (n/a)</td><td>439.10 (n/a)</td><td>685.92 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.16 (+19.15%)</td><td>0.11 (+14.66%)</td><td>0.11 (+16.42%)</td><td>0.02 (+8.74%)</td><td>0.05 (+12.17%)</td><td>1754.60 (-8.04%)</td><td>591.10 (-10.79%)</td><td>321.30 (-14.11%)</td><td>227.70 (-16.07%)</td><td>652.08 (-6.90%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1908.00 (n/a)</td><td>662.62 (n/a)</td><td>374.10 (n/a)</td><td>271.30 (n/a)</td><td>700.39 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 <b>(+36.82%)</b></td><td>0.09 <b>(+29.33%)</b></td><td>0.07 (-2.43%)</td><td>0.06 <b>(+45.03%)</b></td><td>0.03 <b>(+58.25%)</b></td><td>562.50 <b>(-31.05%)</b></td><td>414.56 <b>(-21.28%)</b></td><td>476.20 (+2.50%)</td><td>252.80 <b>(-26.92%)</b></td><td>135.40 <b>(-24.39%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>815.80 (n/a)</td><td>526.60 (n/a)</td><td>464.60 (n/a)</td><td>345.90 (n/a)</td><td>179.08 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 <b>(+24.21%)</b></td><td>0.07 <b>(+22.73%)</b></td><td>0.08 <b>(+52.31%)</b></td><td>0.03 (-3.75%)</td><td>0.03 <b>(+43.61%)</b></td><td>595.50 (+3.89%)</td><td>357.72 (-13.56%)</td><td>270.10 <b>(-34.33%)</b></td><td>222.10 (-19.50%)</td><td>161.56 <b>(+22.57%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>573.20 (n/a)</td><td>413.82 (n/a)</td><td>411.30 (n/a)</td><td>275.90 (n/a)</td><td>131.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (-13.81%)</td><td>0.06 <b>(-20.42%)</b></td><td>0.05 <b>(-34.42%)</b></td><td>0.04 (-16.18%)</td><td>0.02 (-0.63%)</td><td>558.30 (+19.29%)</td><td>388.94 <b>(+28.13%)</b></td><td>430.10 <b>(+52.46%)</b></td><td>249.50 (+16.05%)</td><td>127.21 <b>(+28.23%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>468.00 (n/a)</td><td>303.56 (n/a)</td><td>282.10 (n/a)</td><td>215.00 (n/a)</td><td>99.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (+5.69%)</td><td>0.05 (-7.55%)</td><td>0.04 (-9.61%)</td><td>0.02 <b>(-47.01%)</b></td><td>0.02 <b>(+45.22%)</b></td><td>1070.40 <b>(+88.72%)</b></td><td>548.10 <b>(+26.80%)</b></td><td>479.00 (+10.62%)</td><td>248.70 (-5.37%)</td><td>313.02 <b>(+182.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>567.20 (n/a)</td><td>432.24 (n/a)</td><td>433.00 (n/a)</td><td>262.80 (n/a)</td><td>110.61 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (-19.81%)</td><td>0.05 (-10.94%)</td><td>0.04 (+1.93%)</td><td>0.02 <b>(-42.67%)</b></td><td>0.02 <b>(-21.63%)</b></td><td>1026.80 <b>(+74.42%)</b></td><td>556.82 (+16.45%)</td><td>516.00 (-1.90%)</td><td>245.50 <b>(+24.68%)</b></td><td>287.65 <b>(+79.66%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>588.70 (n/a)</td><td>478.16 (n/a)</td><td>526.00 (n/a)</td><td>196.90 (n/a)</td><td>160.11 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 <b>(-24.61%)</b></td><td>0.05 (-3.35%)</td><td>0.04 (-1.48%)</td><td>0.04 (+8.68%)</td><td>0.01 <b>(-43.03%)</b></td><td>554.80 (-7.99%)</td><td>449.96 (-3.11%)</td><td>506.10 (+1.50%)</td><td>302.10 <b>(+32.67%)</b></td><td>106.85 <b>(-25.60%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>603.00 (n/a)</td><td>464.40 (n/a)</td><td>498.60 (n/a)</td><td>227.70 (n/a)</td><td>143.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (+17.10%)</td><td>0.06 (+6.88%)</td><td>0.05 (+6.48%)</td><td>0.03 <b>(-21.47%)</b></td><td>0.03 <b>(+40.83%)</b></td><td>614.80 <b>(+27.34%)</b></td><td>411.16 (+0.52%)</td><td>434.90 (-6.09%)</td><td>196.90 (-14.61%)</td><td>156.45 <b>(+50.41%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>482.80 (n/a)</td><td>409.02 (n/a)</td><td>463.10 (n/a)</td><td>230.60 (n/a)</td><td>104.02 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 (+12.59%)</td><td>0.06 (-0.48%)</td><td>0.05 <b>(-38.57%)</b></td><td>0.04 <b>(+251.03%)</b></td><td>0.03 <b>(-27.67%)</b></td><td>550.20 <b>(-71.51%)</b></td><td>417.84 <b>(-36.52%)</b></td><td>472.90 <b>(+62.79%)</b></td><td>232.40 (-11.20%)</td><td>129.88 <b>(-81.97%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1931.50 (n/a)</td><td>658.20 (n/a)</td><td>290.50 (n/a)</td><td>261.70 (n/a)</td><td>720.29 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.10 (+0.74%)</td><td>0.07 (-14.22%)</td><td>0.05 <b>(-38.37%)</b></td><td>0.05 (-14.60%)</td><td>0.02 <b>(+74.13%)</b></td><td>492.20 (+17.11%)</td><td>392.48 <b>(+24.49%)</b></td><td>474.90 <b>(+62.25%)</b></td><td>254.10 (-0.74%)</td><td>123.71 <b>(+95.26%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>420.30 (n/a)</td><td>315.26 (n/a)</td><td>292.70 (n/a)</td><td>256.00 (n/a)</td><td>63.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (-3.18%)</td><td>0.06 (+2.43%)</td><td>0.06 (+6.41%)</td><td>0.03 <b>(-26.97%)</b></td><td>0.02 (+18.44%)</td><td>709.10 <b>(+36.94%)</b></td><td>443.94 (+3.84%)</td><td>427.80 (-6.02%)</td><td>259.90 (+3.30%)</td><td>179.56 <b>(+73.59%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>517.80 (n/a)</td><td>427.54 (n/a)</td><td>455.20 (n/a)</td><td>251.60 (n/a)</td><td>103.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (-4.42%)</td><td>0.06 (+12.64%)</td><td>0.05 (-5.29%)</td><td>0.04 <b>(+306.83%)</b></td><td>0.02 <b>(-27.93%)</b></td><td>603.10 <b>(-75.42%)</b></td><td>440.64 <b>(-45.35%)</b></td><td>459.70 (+5.58%)</td><td>288.30 (+4.61%)</td><td>142.19 <b>(-84.62%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2453.50 (n/a)</td><td>806.28 (n/a)</td><td>435.40 (n/a)</td><td>275.60 (n/a)</td><td>924.29 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 <b>(+49.84%)</b></td><td>0.07 <b>(+31.49%)</b></td><td>0.08 <b>(+58.22%)</b></td><td>0.04 (-17.73%)</td><td>0.03 <b>(+292.15%)</b></td><td>696.30 <b>(+21.56%)</b></td><td>434.20 (-9.98%)</td><td>293.30 <b>(-36.79%)</b></td><td>263.20 <b>(-33.27%)</b></td><td>216.62 <b>(+219.56%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>572.80 (n/a)</td><td>482.34 (n/a)</td><td>464.00 (n/a)</td><td>394.40 (n/a)</td><td>67.79 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 (+11.78%)</td><td>0.05 (+2.34%)</td><td>0.05 (-7.33%)</td><td>0.03 <b>(+90.90%)</b></td><td>0.02 (-9.94%)</td><td>978.60 <b>(-47.62%)</b></td><td>538.18 <b>(-23.15%)</b></td><td>467.10 (+7.93%)</td><td>287.00 (-10.54%)</td><td>261.89 <b>(-60.12%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1868.30 (n/a)</td><td>700.34 (n/a)</td><td>432.80 (n/a)</td><td>320.80 (n/a)</td><td>656.65 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (+9.74%)</td><td>0.06 (+3.19%)</td><td>0.08 <b>(+27.70%)</b></td><td>0.02 <b>(-23.40%)</b></td><td>0.03 <b>(+46.18%)</b></td><td>785.50 <b>(+30.55%)</b></td><td>384.38 (+10.23%)</td><td>240.70 <b>(-21.70%)</b></td><td>224.60 (-8.88%)</td><td>241.09 <b>(+64.34%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>601.70 (n/a)</td><td>348.72 (n/a)</td><td>307.40 (n/a)</td><td>246.50 (n/a)</td><td>146.70 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (+0.46%)</td><td>0.06 (+14.96%)</td><td>0.07 <b>(+40.12%)</b></td><td>0.04 (+8.91%)</td><td>0.02 (-9.76%)</td><td>515.70 (-8.19%)</td><td>334.64 (-14.79%)</td><td>281.90 <b>(-28.63%)</b></td><td>245.60 (-0.49%)</td><td>110.51 (-15.12%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>561.70 (n/a)</td><td>392.74 (n/a)</td><td>395.00 (n/a)</td><td>246.80 (n/a)</td><td>130.20 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (-6.75%)</td><td>0.06 <b>(+20.99%)</b></td><td>0.07 <b>(+70.59%)</b></td><td>0.04 <b>(+25.93%)</b></td><td>0.02 <b>(-22.03%)</b></td><td>473.30 <b>(-20.59%)</b></td><td>313.78 <b>(-22.69%)</b></td><td>251.70 <b>(-41.37%)</b></td><td>231.40 (+7.23%)</td><td>105.33 <b>(-34.18%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>596.00 (n/a)</td><td>405.88 (n/a)</td><td>429.30 (n/a)</td><td>215.80 (n/a)</td><td>160.04 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (+8.07%)</td><td>0.06 (+18.69%)</td><td>0.06 <b>(+50.32%)</b></td><td>0.04 <b>(+26.96%)</b></td><td>0.02 (-17.27%)</td><td>476.10 <b>(-21.23%)</b></td><td>326.26 <b>(-20.28%)</b></td><td>301.20 <b>(-33.47%)</b></td><td>233.50 (-7.45%)</td><td>99.75 <b>(-34.92%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.40 (n/a)</td><td>409.28 (n/a)</td><td>452.70 (n/a)</td><td>252.30 (n/a)</td><td>153.27 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.08 (+19.24%)</td><td>0.05 (+13.71%)</td><td>0.05 <b>(+26.26%)</b></td><td>0.04 <b>(+36.80%)</b></td><td>0.02 (+0.31%)</td><td>441.30 <b>(-26.90%)</b></td><td>361.24 (-14.67%)</td><td>355.80 <b>(-20.79%)</b></td><td>229.80 (-16.13%)</td><td>85.28 <b>(-36.74%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>603.70 (n/a)</td><td>423.36 (n/a)</td><td>449.20 (n/a)</td><td>274.00 (n/a)</td><td>134.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (-4.35%)</td><td>0.04 (-4.82%)</td><td>0.05 (+19.27%)</td><td>0.02 <b>(-41.56%)</b></td><td>0.02 <b>(+24.28%)</b></td><td>1043.50 <b>(+71.12%)</b></td><td>541.54 <b>(+20.22%)</b></td><td>402.10 (-16.16%)</td><td>274.60 (+4.57%)</td><td>308.31 <b>(+142.40%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>609.80 (n/a)</td><td>450.44 (n/a)</td><td>479.60 (n/a)</td><td>262.60 (n/a)</td><td>127.19 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.39 (+14.09%)</td><td>0.30 (+0.15%)</td><td>0.33 (+4.74%)</td><td>0.18 (-3.62%)</td><td>0.10 <b>(+56.02%)</b></td><td>543.70 (+3.76%)</td><td>364.32 (+5.17%)</td><td>298.30 (-4.54%)</td><td>251.90 (-12.35%)</td><td>134.85 <b>(+34.89%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>524.00 (n/a)</td><td>346.42 (n/a)</td><td>312.50 (n/a)</td><td>287.40 (n/a)</td><td>99.97 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.41 (+1.48%)</td><td>0.30 (+19.48%)</td><td>0.35 <b>(+59.42%)</b></td><td>0.15 <b>(-26.49%)</b></td><td>0.10 <b>(+23.84%)</b></td><td>656.90 <b>(+36.03%)</b></td><td>368.14 (-10.51%)</td><td>279.80 <b>(-37.26%)</b></td><td>242.10 (-1.43%)</td><td>170.06 <b>(+79.75%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.40 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>482.90 (n/a)</td><td>411.36 (n/a)</td><td>446.00 (n/a)</td><td>245.60 (n/a)</td><td>94.61 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.44 (+19.30%)</td><td>0.30 (+11.68%)</td><td>0.25 (-17.97%)</td><td>0.19 (+18.69%)</td><td>0.12 <b>(+24.08%)</b></td><td>527.70 (-15.74%)</td><td>373.66 (-10.13%)</td><td>389.10 <b>(+21.90%)</b></td><td>222.00 (-16.16%)</td><td>135.22 (-16.43%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.31 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>626.30 (n/a)</td><td>415.78 (n/a)</td><td>319.20 (n/a)</td><td>264.80 (n/a)</td><td>161.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.32 (-2.53%)</td><td>0.24 <b>(+22.85%)</b></td><td>0.26 <b>(+35.89%)</b></td><td>0.12 (-2.55%)</td><td>0.08 (-7.27%)</td><td>635.50 (+2.62%)</td><td>344.04 (-19.68%)</td><td>285.60 <b>(-26.39%)</b></td><td>230.40 (+2.63%)</td><td>166.95 (-3.69%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.33 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>619.30 (n/a)</td><td>428.32 (n/a)</td><td>388.00 (n/a)</td><td>224.50 (n/a)</td><td>173.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.30 (-4.90%)</td><td>0.19 (+4.60%)</td><td>0.15 (-3.43%)</td><td>0.13 <b>(+331.88%)</b></td><td>0.07 <b>(-37.08%)</b></td><td>572.70 <b>(-76.85%)</b></td><td>432.40 <b>(-46.56%)</b></td><td>481.60 (+3.55%)</td><td>248.90 (+5.15%)</td><td>147.56 <b>(-84.36%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.12 (n/a)</td><td>2473.40 (n/a)</td><td>809.06 (n/a)</td><td>465.10 (n/a)</td><td>236.70 (n/a)</td><td>943.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.28 (-14.87%)</td><td>0.18 (-12.64%)</td><td>0.17 (-0.21%)</td><td>0.07 <b>(-38.06%)</b></td><td>0.08 <b>(-22.45%)</b></td><td>1105.20 <b>(+61.44%)</b></td><td>523.96 (+17.07%)</td><td>423.30 (+0.19%)</td><td>259.80 (+17.45%)</td><td>337.35 <b>(+53.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.33 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>684.60 (n/a)</td><td>447.56 (n/a)</td><td>422.50 (n/a)</td><td>221.20 (n/a)</td><td>219.79 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (-11.74%)</td><td>0.08 (-3.69%)</td><td>0.07 (-7.91%)</td><td>0.03 <b>(-41.41%)</b></td><td>0.04 (-1.87%)</td><td>1072.90 <b>(+70.68%)</b></td><td>559.36 (+14.67%)</td><td>554.90 (+8.61%)</td><td>254.90 (+13.34%)</td><td>317.60 <b>(+99.91%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>628.60 (n/a)</td><td>487.80 (n/a)</td><td>510.90 (n/a)</td><td>224.90 (n/a)</td><td>158.87 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (+2.62%)</td><td>0.10 (-15.30%)</td><td>0.07 <b>(-38.63%)</b></td><td>0.07 (-15.33%)</td><td>0.04 <b>(+79.83%)</b></td><td>523.60 (+18.11%)</td><td>412.60 <b>(+26.99%)</b></td><td>495.90 <b>(+62.96%)</b></td><td>259.60 (-2.55%)</td><td>135.34 <b>(+97.29%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>443.30 (n/a)</td><td>324.90 (n/a)</td><td>304.30 (n/a)</td><td>266.40 (n/a)</td><td>68.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 <b>(-32.21%)</b></td><td>0.09 (-11.00%)</td><td>0.09 (+9.17%)</td><td>0.08 (+4.44%)</td><td>0.02 <b>(-53.23%)</b></td><td>487.50 (-4.24%)</td><td>406.74 (+2.63%)</td><td>429.20 (-8.41%)</td><td>276.10 <b>(+47.49%)</b></td><td>91.21 <b>(-31.47%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>509.10 (n/a)</td><td>396.30 (n/a)</td><td>468.60 (n/a)</td><td>187.20 (n/a)</td><td>133.10 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 (-10.68%)</td><td>0.08 (-13.52%)</td><td>0.07 (-17.54%)</td><td>0.05 (+1.82%)</td><td>0.03 (-10.75%)</td><td>812.20 (-1.78%)</td><td>555.88 (+13.64%)</td><td>530.10 <b>(+21.25%)</b></td><td>276.00 (+11.92%)</td><td>198.91 (-5.92%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>826.90 (n/a)</td><td>489.18 (n/a)</td><td>437.20 (n/a)</td><td>246.60 (n/a)</td><td>211.42 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.15 <b>(+46.70%)</b></td><td>0.10 <b>(+25.09%)</b></td><td>0.09 (+9.85%)</td><td>0.07 (+2.25%)</td><td>0.04 <b>(+158.31%)</b></td><td>543.50 (-2.20%)</td><td>403.88 (-12.53%)</td><td>429.90 (-8.98%)</td><td>239.30 <b>(-31.84%)</b></td><td>144.22 <b>(+75.43%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>555.70 (n/a)</td><td>461.74 (n/a)</td><td>472.30 (n/a)</td><td>351.10 (n/a)</td><td>82.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 <b>(-21.75%)</b></td><td>0.08 (-11.06%)</td><td>0.08 (-2.88%)</td><td>0.06 (-5.24%)</td><td>0.02 <b>(-35.06%)</b></td><td>646.60 (+5.53%)</td><td>502.30 (+9.39%)</td><td>477.80 (+2.95%)</td><td>349.10 <b>(+27.78%)</b></td><td>112.90 (-7.82%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>612.70 (n/a)</td><td>459.18 (n/a)</td><td>464.10 (n/a)</td><td>273.20 (n/a)</td><td>122.48 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.18 (+8.05%)</td><td>0.12 (+16.15%)</td><td>0.09 (+3.61%)</td><td>0.07 (-0.60%)</td><td>0.05 <b>(+27.89%)</b></td><td>570.70 (+0.60%)</td><td>398.24 (-9.81%)</td><td>447.60 (-3.47%)</td><td>226.60 (-7.43%)</td><td>148.22 <b>(+24.33%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>567.30 (n/a)</td><td>441.58 (n/a)</td><td>463.70 (n/a)</td><td>244.80 (n/a)</td><td>119.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.17 <b>(+65.92%)</b></td><td>0.11 <b>(+37.95%)</b></td><td>0.12 <b>(+49.68%)</b></td><td>0.06 (-0.88%)</td><td>0.05 <b>(+186.83%)</b></td><td>724.00 (+0.89%)</td><td>431.50 (-16.66%)</td><td>336.20 <b>(-33.20%)</b></td><td>245.40 <b>(-39.73%)</b></td><td>211.05 <b>(+72.44%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>717.60 (n/a)</td><td>517.74 (n/a)</td><td>503.30 (n/a)</td><td>407.20 (n/a)</td><td>122.39 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.11 <b>(-37.70%)</b></td><td>0.08 <b>(-23.26%)</b></td><td>0.08 (-17.40%)</td><td>0.07 (-4.83%)</td><td>0.02 <b>(-59.01%)</b></td><td>584.80 (+5.07%)</td><td>500.40 <b>(+21.38%)</b></td><td>539.50 <b>(+21.07%)</b></td><td>368.50 <b>(+60.50%)</b></td><td>93.20 <b>(-29.53%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>556.60 (n/a)</td><td>412.26 (n/a)</td><td>445.60 (n/a)</td><td>229.60 (n/a)</td><td>132.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.22 <b>(+37.62%)</b></td><td>0.12 (-14.97%)</td><td>0.09 <b>(-35.56%)</b></td><td>0.07 <b>(-21.17%)</b></td><td>0.06 <b>(+129.09%)</b></td><td>552.60 <b>(+26.86%)</b></td><td>407.24 <b>(+33.71%)</b></td><td>436.20 <b>(+55.18%)</b></td><td>182.80 <b>(-27.32%)</b></td><td>156.01 <b>(+107.43%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>435.60 (n/a)</td><td>304.58 (n/a)</td><td>281.10 (n/a)</td><td>251.50 (n/a)</td><td>75.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (-12.08%)</td><td>0.10 (-9.55%)</td><td>0.09 <b>(-33.03%)</b></td><td>0.08 <b>(+25.42%)</b></td><td>0.02 <b>(-43.85%)</b></td><td>524.30 <b>(-20.27%)</b></td><td>426.74 (-0.77%)</td><td>464.10 <b>(+49.32%)</b></td><td>293.40 (+13.72%)</td><td>90.24 <b>(-52.85%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>657.60 (n/a)</td><td>430.04 (n/a)</td><td>310.80 (n/a)</td><td>258.00 (n/a)</td><td>191.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 <b>(-30.98%)</b></td><td>0.09 <b>(-34.54%)</b></td><td>0.08 <b>(-44.76%)</b></td><td>0.07 (-1.67%)</td><td>0.02 <b>(-54.05%)</b></td><td>578.00 (+1.71%)</td><td>489.00 <b>(+39.82%)</b></td><td>510.40 <b>(+81.06%)</b></td><td>323.40 <b>(+44.89%)</b></td><td>98.10 <b>(-34.21%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>568.30 (n/a)</td><td>349.74 (n/a)</td><td>281.90 (n/a)</td><td>223.20 (n/a)</td><td>149.11 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.12 (+1.67%)</td><td>0.10 (+16.77%)</td><td>0.11 <b>(+75.68%)</b></td><td>0.07 <b>(+20.82%)</b></td><td>0.02 <b>(-24.37%)</b></td><td>504.00 (-17.23%)</td><td>369.08 (-18.94%)</td><td>306.30 <b>(-43.08%)</b></td><td>280.50 (-1.65%)</td><td>101.63 <b>(-34.86%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>608.90 (n/a)</td><td>455.32 (n/a)</td><td>538.10 (n/a)</td><td>285.20 (n/a)</td><td>156.03 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 <b>(-37.44%)</b></td><td>0.07 <b>(-21.35%)</b></td><td>0.07 (-11.59%)</td><td>0.06 (+11.66%)</td><td>0.01 <b>(-71.70%)</b></td><td>543.60 (-10.44%)</td><td>498.76 (+18.01%)</td><td>510.80 (+13.11%)</td><td>407.30 <b>(+59.85%)</b></td><td>53.68 <b>(-59.39%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>607.00 (n/a)</td><td>422.64 (n/a)</td><td>451.60 (n/a)</td><td>254.80 (n/a)</td><td>132.16 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (+9.90%)</td><td>0.10 (+3.43%)</td><td>0.08 (+0.55%)</td><td>0.06 (-13.99%)</td><td>0.04 <b>(+38.73%)</b></td><td>583.30 (+16.26%)</td><td>392.22 (+2.58%)</td><td>409.90 (-0.56%)</td><td>241.00 (-8.99%)</td><td>149.98 <b>(+40.81%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>501.70 (n/a)</td><td>382.36 (n/a)</td><td>412.20 (n/a)</td><td>264.80 (n/a)</td><td>106.52 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.09 <b>(-34.46%)</b></td><td>0.07 <b>(-28.42%)</b></td><td>0.07 <b>(-39.47%)</b></td><td>0.05 (-17.79%)</td><td>0.02 <b>(-49.41%)</b></td><td>656.80 <b>(+21.65%)</b></td><td>489.72 <b>(+32.51%)</b></td><td>491.20 <b>(+65.22%)</b></td><td>368.80 <b>(+52.59%)</b></td><td>117.53 (-11.45%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>539.90 (n/a)</td><td>369.58 (n/a)</td><td>297.30 (n/a)</td><td>241.70 (n/a)</td><td>132.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 <b>(+100.98%)</b></td><td>0.10 <b>(+74.88%)</b></td><td>0.10 <b>(+59.68%)</b></td><td>0.06 <b>(+40.65%)</b></td><td>0.03 <b>(+232.96%)</b></td><td>543.10 <b>(-28.89%)</b></td><td>367.22 <b>(-39.34%)</b></td><td>359.50 <b>(-37.38%)</b></td><td>244.70 <b>(-50.24%)</b></td><td>119.39 (+14.48%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>763.80 (n/a)</td><td>605.38 (n/a)</td><td>574.10 (n/a)</td><td>491.80 (n/a)</td><td>104.29 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 <b>(+20.30%)</b></td><td>0.09 (+2.68%)</td><td>0.08 (+8.86%)</td><td>0.06 (-11.64%)</td><td>0.03 <b>(+30.42%)</b></td><td>619.20 (+13.18%)</td><td>430.08 (+0.16%)</td><td>413.10 (-8.14%)</td><td>248.20 (-16.88%)</td><td>134.71 (+18.81%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>547.10 (n/a)</td><td>429.38 (n/a)</td><td>449.70 (n/a)</td><td>298.60 (n/a)</td><td>113.38 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.54 (+14.73%)</td><td>0.34 (+5.52%)</td><td>0.42 <b>(+37.07%)</b></td><td>0.05 <b>(-68.54%)</b></td><td>0.19 <b>(+37.88%)</b></td><td>2419.80 <b>(+217.85%)</b></td><td>761.64 <b>(+58.66%)</b></td><td>313.30 <b>(-27.05%)</b></td><td>244.70 (-12.86%)</td><td>933.55 <b>(+332.96%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>761.30 (n/a)</td><td>480.06 (n/a)</td><td>429.50 (n/a)</td><td>280.80 (n/a)</td><td>215.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.29 <b>(-45.55%)</b></td><td>0.25 <b>(-21.80%)</b></td><td>0.25 (-8.77%)</td><td>0.20 (+0.45%)</td><td>0.03 <b>(-74.89%)</b></td><td>660.80 (-0.45%)</td><td>537.44 (+15.59%)</td><td>518.00 (+9.63%)</td><td>455.30 <b>(+83.66%)</b></td><td>76.93 <b>(-52.25%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.53 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>663.80 (n/a)</td><td>464.96 (n/a)</td><td>472.50 (n/a)</td><td>247.90 (n/a)</td><td>161.09 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.37 (-5.04%)</td><td>0.26 (+0.82%)</td><td>0.26 (-4.32%)</td><td>0.17 <b>(+211.98%)</b></td><td>0.08 <b>(-37.56%)</b></td><td>769.20 <b>(-67.94%)</b></td><td>538.84 <b>(-34.79%)</b></td><td>505.80 (+4.53%)</td><td>357.20 (+5.31%)</td><td>166.87 <b>(-81.09%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.39 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>0.13 (n/a)</td><td>2399.60 (n/a)</td><td>826.30 (n/a)</td><td>483.90 (n/a)</td><td>339.20 (n/a)</td><td>882.52 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.00 (+16.67%)</td><td>0.00 (+17.65%)</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+20.31%)</b></td><td>23043.86 (+6.61%)</td><td>13646.80 (-10.04%)</td><td>15766.04 (-15.26%)</td><td>6051.20 (-9.38%)</td><td>7323.76 (+3.16%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21614.17 (n/a)</td><td>15170.68 (n/a)</td><td>18604.87 (n/a)</td><td>6677.20 (n/a)</td><td>7099.56 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.00 <b>(-46.15%)</b></td><td>0.00 <b>(-41.46%)</b></td><td>0.00 <b>(-50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-65.99%)</b></td><td>22906.99 (+17.74%)</td><td>18105.93 <b>(+46.95%)</b></td><td>18600.16 <b>(+76.53%)</b></td><td>11337.32 <b>(+82.35%)</b></td><td>4846.06 <b>(-20.14%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19454.85 (n/a)</td><td>12321.45 (n/a)</td><td>10536.64 (n/a)</td><td>6217.35 (n/a)</td><td>6068.12 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.14 (+7.20%)</td><td>0.09 (+2.02%)</td><td>0.08 (+1.49%)</td><td>0.07 (-1.11%)</td><td>0.03 (+17.75%)</td><td>29339.52 (+1.15%)</td><td>24512.95 (-0.60%)</td><td>25656.33 (-1.55%)</td><td>14817.03 (-6.73%)</td><td>5827.99 (+11.08%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>29004.66 (n/a)</td><td>24660.91 (n/a)</td><td>26060.24 (n/a)</td><td>15885.92 (n/a)</td><td>5246.76 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>2.96 <b>(+30.49%)</b></td><td>2.47 <b>(+42.21%)</b></td><td>2.36 <b>(+41.84%)</b></td><td>2.03 <b>(+94.52%)</b></td><td>0.35 <b>(-26.71%)</b></td><td>517.00 <b>(-48.59%)</b></td><td>432.36 <b>(-33.64%)</b></td><td>445.20 <b>(-29.50%)</b></td><td>353.80 <b>(-23.35%)</b></td><td>61.39 <b>(-71.51%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>2.27 (n/a)</td><td>1.73 (n/a)</td><td>1.66 (n/a)</td><td>1.04 (n/a)</td><td>0.48 (n/a)</td><td>1005.70 (n/a)</td><td>651.56 (n/a)</td><td>631.50 (n/a)</td><td>461.60 (n/a)</td><td>215.45 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.33 <b>(+47.82%)</b></td><td>1.68 (+15.34%)</td><td>1.79 <b>(+24.09%)</b></td><td>0.30 (+0.58%)</td><td>1.36 <b>(+81.53%)</b></td><td>3460.10 (-0.58%)</td><td>1602.44 <b>(+33.35%)</b></td><td>586.80 (-19.41%)</td><td>314.70 <b>(-32.34%)</b></td><td>1605.80 <b>(+25.35%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>2.25 (n/a)</td><td>1.45 (n/a)</td><td>1.44 (n/a)</td><td>0.30 (n/a)</td><td>0.75 (n/a)</td><td>3480.30 (n/a)</td><td>1201.70 (n/a)</td><td>728.10 (n/a)</td><td>465.10 (n/a)</td><td>1281.05 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>2.50 (-2.58%)</td><td>1.56 (-5.72%)</td><td>1.74 (+4.29%)</td><td>0.30 (-7.59%)</td><td>0.80 (-9.31%)</td><td>3504.90 (+8.22%)</td><td>1167.00 (+6.26%)</td><td>601.30 (-4.11%)</td><td>419.40 (+2.67%)</td><td>1311.32 (+8.83%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>2.57 (n/a)</td><td>1.65 (n/a)</td><td>1.67 (n/a)</td><td>0.32 (n/a)</td><td>0.88 (n/a)</td><td>3238.70 (n/a)</td><td>1098.22 (n/a)</td><td>627.10 (n/a)</td><td>408.50 (n/a)</td><td>1204.95 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.12 (-15.13%)</td><td>2.31 <b>(+44.13%)</b></td><td>2.37 <b>(+39.23%)</b></td><td>1.26 <b>(+330.12%)</b></td><td>0.81 <b>(-39.47%)</b></td><td>835.50 <b>(-76.75%)</b></td><td>510.32 <b>(-63.23%)</b></td><td>442.70 <b>(-28.18%)</b></td><td>335.90 (+17.82%)</td><td>209.41 <b>(-84.75%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.68 (n/a)</td><td>1.60 (n/a)</td><td>1.70 (n/a)</td><td>0.29 (n/a)</td><td>1.34 (n/a)</td><td>3593.70 (n/a)</td><td>1387.90 (n/a)</td><td>616.40 (n/a)</td><td>285.10 (n/a)</td><td>1372.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>4.33 (+14.58%)</td><td>2.23 (-10.33%)</td><td>2.03 <b>(-41.71%)</b></td><td>0.56 (-3.89%)</td><td>1.72 (+6.31%)</td><td>3746.70 (+4.05%)</td><td>1859.08 (+19.95%)</td><td>1034.90 <b>(+71.54%)</b></td><td>484.30 (-12.72%)</td><td>1604.61 (+14.65%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.78 (n/a)</td><td>2.49 (n/a)</td><td>3.48 (n/a)</td><td>0.58 (n/a)</td><td>1.62 (n/a)</td><td>3601.00 (n/a)</td><td>1549.86 (n/a)</td><td>603.30 (n/a)</td><td>554.90 (n/a)</td><td>1399.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.90 (-0.55%)</td><td>3.13 <b>(+48.11%)</b></td><td>3.24 <b>(+59.15%)</b></td><td>1.86 <b>(+222.42%)</b></td><td>0.81 <b>(-41.46%)</b></td><td>1124.80 <b>(-68.98%)</b></td><td>719.30 <b>(-54.95%)</b></td><td>647.30 <b>(-37.17%)</b></td><td>537.70 (+0.54%)</td><td>238.64 <b>(-81.47%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.92 (n/a)</td><td>2.11 (n/a)</td><td>2.04 (n/a)</td><td>0.58 (n/a)</td><td>1.39 (n/a)</td><td>3626.50 (n/a)</td><td>1596.78 (n/a)</td><td>1030.20 (n/a)</td><td>534.80 (n/a)</td><td>1287.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>4.43 <b>(-21.93%)</b></td><td>3.27 (-12.88%)</td><td>3.05 <b>(-25.64%)</b></td><td>2.53 <b>(+33.58%)</b></td><td>0.79 <b>(-49.45%)</b></td><td>828.10 <b>(-25.13%)</b></td><td>669.96 (+1.77%)</td><td>688.50 <b>(+34.47%)</b></td><td>472.90 <b>(+28.09%)</b></td><td>147.82 <b>(-52.26%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>5.68 (n/a)</td><td>3.75 (n/a)</td><td>4.10 (n/a)</td><td>1.90 (n/a)</td><td>1.55 (n/a)</td><td>1106.10 (n/a)</td><td>658.32 (n/a)</td><td>512.00 (n/a)</td><td>369.20 (n/a)</td><td>309.63 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>6.79 <b>(+25.41%)</b></td><td>2.84 (-15.84%)</td><td>2.66 <b>(-25.22%)</b></td><td>0.58 (+0.23%)</td><td>2.57 <b>(+46.60%)</b></td><td>3619.40 (-0.23%)</td><td>1781.50 <b>(+54.87%)</b></td><td>787.30 <b>(+33.74%)</b></td><td>308.70 <b>(-20.27%)</b></td><td>1681.75 <b>(+21.20%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>5.42 (n/a)</td><td>3.38 (n/a)</td><td>3.56 (n/a)</td><td>0.58 (n/a)</td><td>1.75 (n/a)</td><td>3627.60 (n/a)</td><td>1150.34 (n/a)</td><td>588.70 (n/a)</td><td>387.20 (n/a)</td><td>1387.57 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>4.18 (-15.89%)</td><td>3.38 (+2.84%)</td><td>3.67 <b>(+22.10%)</b></td><td>1.77 (-8.50%)</td><td>0.98 (-13.31%)</td><td>1182.30 (+9.30%)</td><td>684.40 (-2.45%)</td><td>571.70 (-18.11%)</td><td>502.30 (+18.89%)</td><td>284.83 (+15.52%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>4.96 (n/a)</td><td>3.29 (n/a)</td><td>3.00 (n/a)</td><td>1.94 (n/a)</td><td>1.13 (n/a)</td><td>1081.70 (n/a)</td><td>701.56 (n/a)</td><td>698.10 (n/a)</td><td>422.50 (n/a)</td><td>246.56 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>5.56 <b>(+70.73%)</b></td><td>3.27 <b>(+55.70%)</b></td><td>2.83 <b>(+37.73%)</b></td><td>0.87 (-11.78%)</td><td>1.81 <b>(+124.36%)</b></td><td>2412.10 (+13.36%)</td><td>960.62 (-17.13%)</td><td>742.00 <b>(-27.40%)</b></td><td>377.00 <b>(-41.43%)</b></td><td>830.75 <b>(+47.18%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.26 (n/a)</td><td>2.10 (n/a)</td><td>2.05 (n/a)</td><td>0.99 (n/a)</td><td>0.80 (n/a)</td><td>2127.80 (n/a)</td><td>1159.12 (n/a)</td><td>1022.00 (n/a)</td><td>643.70 (n/a)</td><td>564.44 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>5.14 (+1.23%)</td><td>4.40 (-2.56%)</td><td>4.09 (-10.26%)</td><td>3.88 (-3.41%)</td><td>0.61 <b>(+57.39%)</b></td><td>1082.30 (+3.53%)</td><td>968.68 (+3.56%)</td><td>1025.70 (+11.43%)</td><td>816.60 (-1.21%)</td><td>129.36 <b>(+61.25%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>5.07 (n/a)</td><td>4.51 (n/a)</td><td>4.56 (n/a)</td><td>4.01 (n/a)</td><td>0.39 (n/a)</td><td>1045.40 (n/a)</td><td>935.38 (n/a)</td><td>920.50 (n/a)</td><td>826.60 (n/a)</td><td>80.22 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>7.52 (-9.97%)</td><td>6.72 <b>(+32.72%)</b></td><td>7.32 <b>(+28.67%)</b></td><td>4.10 <b>(+104.61%)</b></td><td>1.47 <b>(-38.91%)</b></td><td>1024.20 <b>(-51.13%)</b></td><td>659.82 <b>(-37.11%)</b></td><td>572.70 <b>(-22.28%)</b></td><td>557.90 (+11.07%)</td><td>203.91 <b>(-67.83%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>8.35 (n/a)</td><td>5.06 (n/a)</td><td>5.69 (n/a)</td><td>2.00 (n/a)</td><td>2.41 (n/a)</td><td>2095.60 (n/a)</td><td>1049.22 (n/a)</td><td>736.90 (n/a)</td><td>502.30 (n/a)</td><td>633.85 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>7.67 (-19.10%)</td><td>6.30 (-2.10%)</td><td>6.41 (-8.33%)</td><td>3.92 (+0.48%)</td><td>1.55 <b>(-34.39%)</b></td><td>1070.40 (-0.47%)</td><td>707.80 (-3.50%)</td><td>654.30 (+9.09%)</td><td>546.60 <b>(+23.64%)</b></td><td>215.40 <b>(-23.84%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>9.49 (n/a)</td><td>6.43 (n/a)</td><td>6.99 (n/a)</td><td>3.90 (n/a)</td><td>2.36 (n/a)</td><td>1075.50 (n/a)</td><td>733.46 (n/a)</td><td>599.80 (n/a)</td><td>442.10 (n/a)</td><td>282.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>9.42 <b>(-24.79%)</b></td><td>4.52 <b>(-45.62%)</b></td><td>4.26 <b>(-39.97%)</b></td><td>1.14 <b>(-82.80%)</b></td><td>3.56 <b>(+42.95%)</b></td><td>3691.00 <b>(+481.26%)</b></td><td>1845.64 <b>(+245.25%)</b></td><td>985.20 <b>(+66.59%)</b></td><td>445.40 <b>(+32.96%)</b></td><td>1597.00 <b>(+1163.69%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>12.52 (n/a)</td><td>8.31 (n/a)</td><td>7.09 (n/a)</td><td>6.61 (n/a)</td><td>2.49 (n/a)</td><td>635.00 (n/a)</td><td>534.58 (n/a)</td><td>591.40 (n/a)</td><td>335.00 (n/a)</td><td>126.38 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>8.66 (+1.91%)</td><td>6.66 (+13.82%)</td><td>6.69 (+9.27%)</td><td>3.94 <b>(+127.30%)</b></td><td>1.73 <b>(-31.42%)</b></td><td>1065.20 <b>(-56.01%)</b></td><td>676.02 <b>(-31.22%)</b></td><td>626.70 (-8.47%)</td><td>484.20 (-1.88%)</td><td>226.11 <b>(-72.05%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>8.50 (n/a)</td><td>5.85 (n/a)</td><td>6.13 (n/a)</td><td>1.73 (n/a)</td><td>2.53 (n/a)</td><td>2421.20 (n/a)</td><td>982.90 (n/a)</td><td>684.70 (n/a)</td><td>493.50 (n/a)</td><td>808.92 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>8.29 <b>(-26.58%)</b></td><td>5.62 (-15.50%)</td><td>6.73 (+0.47%)</td><td>1.19 <b>(-44.09%)</b></td><td>2.73 (-15.89%)</td><td>3535.80 <b>(+78.86%)</b></td><td>1221.26 <b>(+43.65%)</b></td><td>623.70 (-0.46%)</td><td>506.00 <b>(+36.20%)</b></td><td>1299.10 <b>(+102.91%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>11.29 (n/a)</td><td>6.65 (n/a)</td><td>6.69 (n/a)</td><td>2.12 (n/a)</td><td>3.25 (n/a)</td><td>1976.90 (n/a)</td><td>850.18 (n/a)</td><td>626.60 (n/a)</td><td>371.50 (n/a)</td><td>640.22 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>1.90 <b>(+35.92%)</b></td><td>1.52 <b>(+33.93%)</b></td><td>1.57 <b>(+22.98%)</b></td><td>1.10 <b>(+58.64%)</b></td><td>0.31 (+1.10%)</td><td>476.30 <b>(-36.96%)</b></td><td>358.38 <b>(-27.98%)</b></td><td>333.30 (-18.69%)</td><td>275.30 <b>(-26.43%)</b></td><td>77.89 <b>(-51.89%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>1.40 (n/a)</td><td>1.13 (n/a)</td><td>1.28 (n/a)</td><td>0.69 (n/a)</td><td>0.30 (n/a)</td><td>755.60 (n/a)</td><td>497.62 (n/a)</td><td>409.90 (n/a)</td><td>374.20 (n/a)</td><td>161.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>2.79 (-18.72%)</td><td>2.10 <b>(-29.31%)</b></td><td>2.13 <b>(-23.55%)</b></td><td>1.52 <b>(-41.01%)</b></td><td>0.54 <b>(+35.72%)</b></td><td>690.80 <b>(+69.52%)</b></td><td>528.40 <b>(+47.29%)</b></td><td>491.70 <b>(+30.81%)</b></td><td>376.40 <b>(+23.05%)</b></td><td>137.29 <b>(+195.31%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.43 (n/a)</td><td>2.96 (n/a)</td><td>2.79 (n/a)</td><td>2.57 (n/a)</td><td>0.40 (n/a)</td><td>407.50 (n/a)</td><td>358.76 (n/a)</td><td>375.90 (n/a)</td><td>305.90 (n/a)</td><td>46.49 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>3.57 (+2.83%)</td><td>2.24 (-2.21%)</td><td>2.55 (-0.95%)</td><td>0.61 (-3.20%)</td><td>1.41 <b>(+29.56%)</b></td><td>3441.70 (+3.30%)</td><td>1539.74 (+16.99%)</td><td>823.80 (+0.96%)</td><td>588.30 (-2.74%)</td><td>1270.21 (+11.25%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>3.47 (n/a)</td><td>2.29 (n/a)</td><td>2.57 (n/a)</td><td>0.63 (n/a)</td><td>1.09 (n/a)</td><td>3331.60 (n/a)</td><td>1316.18 (n/a)</td><td>816.00 (n/a)</td><td>604.90 (n/a)</td><td>1141.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>1.74 <b>(+64.13%)</b></td><td>1.05 <b>(+26.21%)</b></td><td>0.98 (+4.52%)</td><td>0.50 <b>(+137.61%)</b></td><td>0.45 <b>(+28.16%)</b></td><td>1044.70 <b>(-57.91%)</b></td><td>586.54 <b>(-36.53%)</b></td><td>535.70 (-4.32%)</td><td>300.90 <b>(-39.06%)</b></td><td>276.35 <b>(-68.29%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>1.06 (n/a)</td><td>0.83 (n/a)</td><td>0.94 (n/a)</td><td>0.21 (n/a)</td><td>0.35 (n/a)</td><td>2482.30 (n/a)</td><td>924.18 (n/a)</td><td>559.90 (n/a)</td><td>493.80 (n/a)</td><td>871.51 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.13 (-6.68%)</td><td>0.08 <b>(-23.39%)</b></td><td>0.08 <b>(-31.80%)</b></td><td>0.02 <b>(-75.01%)</b></td><td>0.04 <b>(+56.14%)</b></td><td>1932.70 <b>(+300.23%)</b></td><td>676.78 <b>(+103.20%)</b></td><td>430.20 <b>(+46.63%)</b></td><td>261.20 (+7.18%)</td><td>707.61 <b>(+620.54%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>482.90 (n/a)</td><td>333.06 (n/a)</td><td>293.40 (n/a)</td><td>243.70 (n/a)</td><td>98.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.16 (+6.87%)</td><td>0.09 (-12.36%)</td><td>0.07 <b>(-39.63%)</b></td><td>0.03 <b>(-47.50%)</b></td><td>0.05 <b>(+23.89%)</b></td><td>1074.60 <b>(+90.46%)</b></td><td>506.66 <b>(+33.57%)</b></td><td>475.20 <b>(+65.63%)</b></td><td>203.90 (-6.42%)</td><td>338.30 <b>(+108.07%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>564.20 (n/a)</td><td>379.32 (n/a)</td><td>286.90 (n/a)</td><td>217.90 (n/a)</td><td>162.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.26 (-15.40%)</td><td>0.20 (-14.97%)</td><td>0.23 (-0.12%)</td><td>0.14 (+14.48%)</td><td>0.06 <b>(-20.92%)</b></td><td>472.40 (-12.65%)</td><td>348.88 (+13.58%)</td><td>280.80 (+0.11%)</td><td>253.30 (+18.20%)</td><td>112.50 (-16.53%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>540.80 (n/a)</td><td>307.16 (n/a)</td><td>280.50 (n/a)</td><td>214.30 (n/a)</td><td>134.77 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.25 <b>(-23.58%)</b></td><td>0.16 <b>(-24.46%)</b></td><td>0.15 <b>(-37.58%)</b></td><td>0.11 (-3.44%)</td><td>0.06 <b>(-35.44%)</b></td><td>594.30 (+3.55%)</td><td>434.30 <b>(+23.77%)</b></td><td>434.40 <b>(+60.24%)</b></td><td>258.20 <b>(+30.87%)</b></td><td>135.84 (-15.02%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>573.90 (n/a)</td><td>350.90 (n/a)</td><td>271.10 (n/a)</td><td>197.30 (n/a)</td><td>159.86 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.26 <b>(-22.93%)</b></td><td>0.17 (-18.68%)</td><td>0.16 <b>(-30.01%)</b></td><td>0.10 <b>(+64.57%)</b></td><td>0.07 <b>(-35.32%)</b></td><td>653.70 <b>(-39.24%)</b></td><td>449.24 (-1.11%)</td><td>418.70 <b>(+42.85%)</b></td><td>248.50 <b>(+29.77%)</b></td><td>182.80 <b>(-49.56%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>0.11 (n/a)</td><td>1075.90 (n/a)</td><td>454.28 (n/a)</td><td>293.10 (n/a)</td><td>191.50 (n/a)</td><td>362.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.32 <b>(-46.48%)</b></td><td>0.26 <b>(-37.11%)</b></td><td>0.27 <b>(-37.49%)</b></td><td>0.21 (-4.91%)</td><td>0.04 <b>(-70.66%)</b></td><td>631.20 (+5.16%)</td><td>516.72 <b>(+44.25%)</b></td><td>492.00 <b>(+59.95%)</b></td><td>415.10 <b>(+86.90%)</b></td><td>85.24 <b>(-43.15%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.59 (n/a)</td><td>0.41 (n/a)</td><td>0.43 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>600.20 (n/a)</td><td>358.20 (n/a)</td><td>307.60 (n/a)</td><td>222.10 (n/a)</td><td>149.94 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.49 (-15.40%)</td><td>0.34 <b>(-25.91%)</b></td><td>0.33 <b>(-32.98%)</b></td><td>0.22 (-14.81%)</td><td>0.10 (-15.80%)</td><td>589.90 (+17.37%)</td><td>414.10 <b>(+34.09%)</b></td><td>402.40 <b>(+49.20%)</b></td><td>269.60 (+18.19%)</td><td>121.97 (+10.07%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.57 (n/a)</td><td>0.46 (n/a)</td><td>0.49 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>502.60 (n/a)</td><td>308.82 (n/a)</td><td>269.70 (n/a)</td><td>228.10 (n/a)</td><td>110.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.41 <b>(-23.43%)</b></td><td>0.32 (+6.34%)</td><td>0.31 <b>(+32.10%)</b></td><td>0.27 <b>(+412.94%)</b></td><td>0.06 <b>(-71.48%)</b></td><td>490.50 <b>(-80.51%)</b></td><td>415.32 <b>(-50.12%)</b></td><td>418.40 <b>(-24.30%)</b></td><td>316.40 <b>(+30.58%)</b></td><td>63.86 <b>(-93.30%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.54 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>0.19 (n/a)</td><td>2516.10 (n/a)</td><td>832.66 (n/a)</td><td>552.70 (n/a)</td><td>242.30 (n/a)</td><td>952.45 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:33:18</td><td>0.07 (+0.59%)</td><td>0.05 <b>(+41.80%)</b></td><td>0.05 <b>(+59.04%)</b></td><td>0.03 <b>(+317.21%)</b></td><td>0.02 <b>(-21.49%)</b></td><td>595.60 <b>(-76.03%)</b></td><td>375.90 <b>(-55.59%)</b></td><td>298.00 <b>(-37.12%)</b></td><td>248.10 (-0.56%)</td><td>149.72 <b>(-83.79%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:01:25</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2484.90 (n/a)</td><td>846.40 (n/a)</td><td>473.90 (n/a)</td><td>249.50 (n/a)</td><td>923.77 (n/a)</td>
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
