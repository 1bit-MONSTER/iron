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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (-15.10%)</td><td>0.01 <b>(-24.48%)</b></td><td>0.01 <b>(-26.15%)</b></td><td>0.01 (-14.83%)</td><td>0.00 <b>(-21.93%)</b></td><td>715.60 (+17.43%)</td><td>557.32 <b>(+29.46%)</b></td><td>621.50 <b>(+35.40%)</b></td><td>295.00 (+17.76%)</td><td>160.24 (+3.01%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.40 (n/a)</td><td>430.50 (n/a)</td><td>459.00 (n/a)</td><td>250.50 (n/a)</td><td>155.56 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (-8.79%)</td><td>0.02 <b>(+20.79%)</b></td><td>0.02 <b>(+46.54%)</b></td><td>0.01 <b>(+23.86%)</b></td><td>0.00 <b>(-31.17%)</b></td><td>434.90 (-19.25%)</td><td>345.42 <b>(-20.65%)</b></td><td>311.70 <b>(-31.76%)</b></td><td>266.70 (+9.66%)</td><td>76.07 <b>(-33.72%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>538.60 (n/a)</td><td>435.30 (n/a)</td><td>456.80 (n/a)</td><td>243.20 (n/a)</td><td>114.77 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-3.85%)</td><td>0.02 <b>(-24.30%)</b></td><td>0.01 <b>(-45.85%)</b></td><td>0.01 (+3.85%)</td><td>0.01 (-1.52%)</td><td>573.70 (-3.71%)</td><td>414.26 <b>(+30.64%)</b></td><td>487.10 <b>(+84.72%)</b></td><td>230.60 (+4.01%)</td><td>145.43 (-7.55%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.80 (n/a)</td><td>317.10 (n/a)</td><td>263.70 (n/a)</td><td>221.70 (n/a)</td><td>157.31 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (-9.55%)</td><td>0.01 (-7.02%)</td><td>0.01 (-13.87%)</td><td>0.01 <b>(-45.88%)</b></td><td>0.01 <b>(+33.99%)</b></td><td>1040.90 <b>(+84.79%)</b></td><td>553.64 <b>(+26.12%)</b></td><td>512.00 (+16.10%)</td><td>282.50 (+10.57%)</td><td>313.24 <b>(+149.71%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.30 (n/a)</td><td>438.98 (n/a)</td><td>441.00 (n/a)</td><td>255.50 (n/a)</td><td>125.44 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 <b>(+32.40%)</b></td><td>0.02 <b>(+45.39%)</b></td><td>0.01 <b>(+28.32%)</b></td><td>0.01 <b>(+68.19%)</b></td><td>0.01 <b>(+50.87%)</b></td><td>603.80 <b>(-40.55%)</b></td><td>427.68 <b>(-30.85%)</b></td><td>492.60 <b>(-22.07%)</b></td><td>242.20 <b>(-24.48%)</b></td><td>172.24 <b>(-35.13%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1015.60 (n/a)</td><td>618.48 (n/a)</td><td>632.10 (n/a)</td><td>320.70 (n/a)</td><td>265.51 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (+12.05%)</td><td>0.02 (-3.88%)</td><td>0.02 (-6.18%)</td><td>0.01 <b>(-41.34%)</b></td><td>0.01 <b>(+103.76%)</b></td><td>793.00 <b>(+70.50%)</b></td><td>426.46 <b>(+25.50%)</b></td><td>326.60 (+6.59%)</td><td>225.20 (-10.78%)</td><td>242.41 <b>(+194.31%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>465.10 (n/a)</td><td>339.80 (n/a)</td><td>306.40 (n/a)</td><td>252.40 (n/a)</td><td>82.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (+1.40%)</td><td>0.04 (-10.50%)</td><td>0.04 (-4.89%)</td><td>0.02 <b>(-29.40%)</b></td><td>0.01 <b>(+54.45%)</b></td><td>538.20 <b>(+41.67%)</b></td><td>344.26 (+19.75%)</td><td>302.10 (+5.15%)</td><td>229.80 (-1.37%)</td><td>128.69 <b>(+116.22%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>379.90 (n/a)</td><td>287.48 (n/a)</td><td>287.30 (n/a)</td><td>233.00 (n/a)</td><td>59.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (+1.25%)</td><td>0.04 <b>(+30.35%)</b></td><td>0.05 <b>(+46.61%)</b></td><td>0.03 <b>(+77.38%)</b></td><td>0.01 <b>(-41.26%)</b></td><td>381.40 <b>(-43.62%)</b></td><td>283.72 <b>(-31.68%)</b></td><td>271.30 <b>(-31.78%)</b></td><td>231.90 (-1.24%)</td><td>60.27 <b>(-66.39%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>676.50 (n/a)</td><td>415.30 (n/a)</td><td>397.70 (n/a)</td><td>234.80 (n/a)</td><td>179.32 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 <b>(-42.76%)</b></td><td>0.02 <b>(-25.73%)</b></td><td>0.02 (-18.95%)</td><td>0.02 <b>(+64.07%)</b></td><td>0.00 <b>(-84.77%)</b></td><td>604.10 <b>(-39.05%)</b></td><td>541.06 (+8.79%)</td><td>534.90 <b>(+23.39%)</b></td><td>470.80 <b>(+74.69%)</b></td><td>48.55 <b>(-83.50%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>991.20 (n/a)</td><td>497.34 (n/a)</td><td>433.50 (n/a)</td><td>269.50 (n/a)</td><td>294.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 <b>(+21.83%)</b></td><td>0.04 <b>(+26.06%)</b></td><td>0.04 <b>(+45.82%)</b></td><td>0.02 (+8.64%)</td><td>0.01 <b>(+22.78%)</b></td><td>542.70 (-7.95%)</td><td>338.54 (-19.63%)</td><td>296.60 <b>(-31.42%)</b></td><td>227.70 (-17.92%)</td><td>128.33 (-4.21%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>589.60 (n/a)</td><td>421.24 (n/a)</td><td>432.50 (n/a)</td><td>277.40 (n/a)</td><td>133.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 <b>(+65.63%)</b></td><td>0.03 <b>(+46.22%)</b></td><td>0.03 <b>(+50.62%)</b></td><td>0.01 <b>(-47.03%)</b></td><td>0.02 <b>(+161.83%)</b></td><td>1872.00 <b>(+88.77%)</b></td><td>635.70 (+8.36%)</td><td>354.60 <b>(-33.61%)</b></td><td>231.30 <b>(-39.61%)</b></td><td>697.40 <b>(+196.26%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>991.70 (n/a)</td><td>586.68 (n/a)</td><td>534.10 (n/a)</td><td>383.00 (n/a)</td><td>235.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 <b>(+23.27%)</b></td><td>0.03 (+4.70%)</td><td>0.04 (+11.35%)</td><td>0.02 (-13.95%)</td><td>0.01 <b>(+76.42%)</b></td><td>602.30 (+16.21%)</td><td>395.78 (+3.13%)</td><td>315.60 (-10.19%)</td><td>239.40 (-18.87%)</td><td>154.81 <b>(+71.32%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.30 (n/a)</td><td>383.78 (n/a)</td><td>351.40 (n/a)</td><td>295.10 (n/a)</td><td>90.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.10 (-7.92%)</td><td>0.08 (+0.90%)</td><td>0.08 (+14.92%)</td><td>0.05 (+19.39%)</td><td>0.02 <b>(-23.72%)</b></td><td>474.90 (-16.26%)</td><td>352.38 (-5.92%)</td><td>289.50 (-12.96%)</td><td>250.50 (+8.63%)</td><td>109.23 <b>(-26.65%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>567.10 (n/a)</td><td>374.56 (n/a)</td><td>332.60 (n/a)</td><td>230.60 (n/a)</td><td>148.91 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (+4.08%)</td><td>0.07 (+5.71%)</td><td>0.06 (+1.29%)</td><td>0.05 (-2.30%)</td><td>0.03 (+18.85%)</td><td>543.80 (+2.35%)</td><td>378.40 (-2.47%)</td><td>425.30 (-1.28%)</td><td>223.30 (-3.92%)</td><td>137.23 (+13.97%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>531.30 (n/a)</td><td>387.98 (n/a)</td><td>430.80 (n/a)</td><td>232.40 (n/a)</td><td>120.41 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.10 (-2.98%)</td><td>0.05 (-15.84%)</td><td>0.05 (-8.49%)</td><td>0.04 (-4.18%)</td><td>0.02 (-10.70%)</td><td>618.60 (+4.37%)</td><td>499.36 (+16.33%)</td><td>530.70 (+9.29%)</td><td>254.10 (+3.04%)</td><td>143.82 (-7.71%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>592.70 (n/a)</td><td>429.28 (n/a)</td><td>485.60 (n/a)</td><td>246.60 (n/a)</td><td>155.84 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (+2.10%)</td><td>0.07 (+10.06%)</td><td>0.06 <b>(+40.31%)</b></td><td>0.01 (+8.01%)</td><td>0.04 (-0.64%)</td><td>1943.30 (-7.41%)</td><td>671.48 (-10.36%)</td><td>402.40 <b>(-28.73%)</b></td><td>188.20 (-2.03%)</td><td>721.77 (-6.47%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2098.90 (n/a)</td><td>749.12 (n/a)</td><td>564.60 (n/a)</td><td>192.10 (n/a)</td><td>771.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 <b>(+27.63%)</b></td><td>0.08 <b>(+29.67%)</b></td><td>0.08 <b>(+31.44%)</b></td><td>0.05 (+18.85%)</td><td>0.02 <b>(+31.04%)</b></td><td>534.60 (-15.85%)</td><td>338.86 <b>(-22.09%)</b></td><td>290.70 <b>(-23.90%)</b></td><td>272.40 <b>(-21.63%)</b></td><td>110.12 (-9.00%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>635.30 (n/a)</td><td>434.96 (n/a)</td><td>382.00 (n/a)</td><td>347.60 (n/a)</td><td>121.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.10 (+19.38%)</td><td>0.07 (+16.18%)</td><td>0.05 (-1.89%)</td><td>0.05 <b>(+22.73%)</b></td><td>0.02 <b>(+30.37%)</b></td><td>517.00 (-18.53%)</td><td>405.28 (-12.77%)</td><td>466.30 (+1.92%)</td><td>252.80 (-16.24%)</td><td>124.27 (-10.36%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>634.60 (n/a)</td><td>464.62 (n/a)</td><td>457.50 (n/a)</td><td>301.80 (n/a)</td><td>138.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.24 (+3.00%)</td><td>0.15 (-3.27%)</td><td>0.11 <b>(-32.39%)</b></td><td>0.09 (+8.30%)</td><td>0.07 (+15.43%)</td><td>522.30 (-7.67%)</td><td>377.42 (+5.77%)</td><td>442.00 <b>(+47.93%)</b></td><td>205.70 (-2.93%)</td><td>151.35 (+0.35%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>565.70 (n/a)</td><td>356.82 (n/a)</td><td>298.80 (n/a)</td><td>211.90 (n/a)</td><td>150.81 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.24 (+19.86%)</td><td>0.12 (+15.46%)</td><td>0.09 (-14.04%)</td><td>0.09 <b>(+262.50%)</b></td><td>0.06 (+2.76%)</td><td>570.00 <b>(-72.41%)</b></td><td>456.98 <b>(-38.83%)</b></td><td>522.80 (+16.33%)</td><td>208.00 (-16.57%)</td><td>145.33 <b>(-80.48%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2066.10 (n/a)</td><td>747.08 (n/a)</td><td>449.40 (n/a)</td><td>249.30 (n/a)</td><td>744.63 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.20 (+1.67%)</td><td>0.12 <b>(-24.09%)</b></td><td>0.10 <b>(-37.48%)</b></td><td>0.02 <b>(-83.13%)</b></td><td>0.07 <b>(+98.01%)</b></td><td>2487.40 <b>(+492.94%)</b></td><td>811.72 <b>(+144.24%)</b></td><td>493.40 <b>(+59.99%)</b></td><td>244.50 (-1.61%)</td><td>946.76 <b>(+1051.51%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>419.50 (n/a)</td><td>332.34 (n/a)</td><td>308.40 (n/a)</td><td>248.50 (n/a)</td><td>82.22 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.24 (-3.57%)</td><td>0.15 (-6.19%)</td><td>0.14 (-19.04%)</td><td>0.11 (+19.93%)</td><td>0.06 <b>(-20.21%)</b></td><td>454.90 (-16.62%)</td><td>352.00 (-1.16%)</td><td>356.80 <b>(+23.50%)</b></td><td>200.80 (+3.72%)</td><td>104.89 <b>(-34.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>545.60 (n/a)</td><td>356.14 (n/a)</td><td>288.90 (n/a)</td><td>193.60 (n/a)</td><td>160.95 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 <b>(-22.05%)</b></td><td>0.11 (-19.31%)</td><td>0.10 <b>(-36.59%)</b></td><td>0.09 (+12.26%)</td><td>0.03 <b>(-44.98%)</b></td><td>564.80 (-10.91%)</td><td>468.64 (+15.21%)</td><td>495.90 <b>(+57.73%)</b></td><td>333.80 <b>(+28.29%)</b></td><td>100.91 <b>(-37.31%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>634.00 (n/a)</td><td>406.78 (n/a)</td><td>314.40 (n/a)</td><td>260.20 (n/a)</td><td>160.98 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 <b>(-32.26%)</b></td><td>0.10 <b>(-28.55%)</b></td><td>0.10 <b>(-41.45%)</b></td><td>0.09 (+3.20%)</td><td>0.02 <b>(-63.54%)</b></td><td>578.10 (-3.10%)</td><td>489.56 <b>(+23.76%)</b></td><td>510.00 <b>(+70.80%)</b></td><td>353.00 <b>(+47.64%)</b></td><td>82.83 <b>(-52.95%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>596.60 (n/a)</td><td>395.56 (n/a)</td><td>298.60 (n/a)</td><td>239.10 (n/a)</td><td>176.07 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (-10.17%)</td><td>0.01 (+11.60%)</td><td>0.01 <b>(+33.86%)</b></td><td>0.00 (-12.41%)</td><td>0.00 (-17.57%)</td><td>596.70 (+14.18%)</td><td>341.38 (-10.76%)</td><td>292.00 <b>(-25.30%)</b></td><td>227.70 (+11.34%)</td><td>145.75 (+16.05%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.60 (n/a)</td><td>382.54 (n/a)</td><td>390.90 (n/a)</td><td>204.50 (n/a)</td><td>125.59 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (-16.11%)</td><td>0.01 <b>(-24.13%)</b></td><td>0.01 <b>(-42.63%)</b></td><td>0.00 (-15.21%)</td><td>0.00 (-2.34%)</td><td>576.50 (+17.94%)</td><td>421.80 <b>(+35.30%)</b></td><td>473.60 <b>(+74.31%)</b></td><td>247.40 (+19.23%)</td><td>145.81 <b>(+32.17%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.80 (n/a)</td><td>311.76 (n/a)</td><td>271.70 (n/a)</td><td>207.50 (n/a)</td><td>110.32 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (+4.99%)</td><td>0.01 (-2.75%)</td><td>0.01 (-2.79%)</td><td>0.00 (+2.66%)</td><td>0.00 (-1.14%)</td><td>562.50 (-2.60%)</td><td>414.20 (+2.27%)</td><td>439.30 (+2.86%)</td><td>231.20 (-4.74%)</td><td>145.61 (-2.82%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>577.50 (n/a)</td><td>405.00 (n/a)</td><td>427.10 (n/a)</td><td>242.70 (n/a)</td><td>149.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 <b>(+94.48%)</b></td><td>0.01 <b>(+36.95%)</b></td><td>0.01 (+4.71%)</td><td>0.00 (+10.63%)</td><td>0.00 <b>(+289.58%)</b></td><td>588.00 (-9.61%)</td><td>432.84 (-19.24%)</td><td>480.10 (-4.50%)</td><td>239.50 <b>(-48.57%)</b></td><td>150.80 <b>(+84.66%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>650.50 (n/a)</td><td>535.96 (n/a)</td><td>502.70 (n/a)</td><td>465.70 (n/a)</td><td>81.67 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 <b>(-24.48%)</b></td><td>0.00 <b>(-32.23%)</b></td><td>0.01 <b>(-29.88%)</b></td><td>0.00 <b>(-44.46%)</b></td><td>0.00 <b>(-26.76%)</b></td><td>988.40 <b>(+80.07%)</b></td><td>596.50 <b>(+50.76%)</b></td><td>512.00 <b>(+42.62%)</b></td><td>355.10 <b>(+32.40%)</b></td><td>239.34 <b>(+79.59%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>548.90 (n/a)</td><td>395.66 (n/a)</td><td>359.00 (n/a)</td><td>268.20 (n/a)</td><td>133.27 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (+2.54%)</td><td>0.01 (+11.00%)</td><td>0.01 (+14.27%)</td><td>0.00 (+18.24%)</td><td>0.00 (-8.45%)</td><td>548.80 (-15.43%)</td><td>455.10 (-12.69%)</td><td>479.10 (-12.49%)</td><td>256.00 (-2.48%)</td><td>114.99 <b>(-24.39%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>648.90 (n/a)</td><td>521.26 (n/a)</td><td>547.50 (n/a)</td><td>262.50 (n/a)</td><td>152.08 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (+15.01%)</td><td>0.02 (+5.01%)</td><td>0.01 (-14.91%)</td><td>0.01 <b>(+33.07%)</b></td><td>0.00 (-11.78%)</td><td>490.00 <b>(-24.86%)</b></td><td>351.36 (-10.21%)</td><td>368.40 (+17.51%)</td><td>227.30 (-13.08%)</td><td>98.47 <b>(-41.26%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>652.10 (n/a)</td><td>391.32 (n/a)</td><td>313.50 (n/a)</td><td>261.50 (n/a)</td><td>167.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 <b>(+49.10%)</b></td><td>0.01 (-9.95%)</td><td>0.01 <b>(-43.15%)</b></td><td>0.01 (-3.31%)</td><td>0.01 <b>(+76.94%)</b></td><td>562.50 (+3.42%)</td><td>453.58 <b>(+23.18%)</b></td><td>500.70 <b>(+75.87%)</b></td><td>165.90 <b>(-32.94%)</b></td><td>164.84 (+15.55%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>543.90 (n/a)</td><td>368.24 (n/a)</td><td>284.70 (n/a)</td><td>247.40 (n/a)</td><td>142.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (-0.68%)</td><td>0.01 (-0.87%)</td><td>0.01 (-17.68%)</td><td>0.01 (+14.65%)</td><td>0.01 (+1.48%)</td><td>491.40 (-12.78%)</td><td>386.28 (+0.47%)</td><td>458.60 <b>(+21.48%)</b></td><td>229.80 (+0.70%)</td><td>122.43 (-8.05%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.40 (n/a)</td><td>384.46 (n/a)</td><td>377.50 (n/a)</td><td>228.20 (n/a)</td><td>133.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (+11.79%)</td><td>0.02 <b>(+26.77%)</b></td><td>0.02 <b>(+43.96%)</b></td><td>0.01 <b>(+25.86%)</b></td><td>0.00 <b>(-20.42%)</b></td><td>435.50 <b>(-20.56%)</b></td><td>306.60 <b>(-25.46%)</b></td><td>308.50 <b>(-30.55%)</b></td><td>235.00 (-10.54%)</td><td>80.54 <b>(-42.54%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.20 (n/a)</td><td>411.30 (n/a)</td><td>444.20 (n/a)</td><td>262.70 (n/a)</td><td>140.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 <b>(-46.85%)</b></td><td>0.01 <b>(-40.20%)</b></td><td>0.01 <b>(-36.36%)</b></td><td>0.00 <b>(-77.16%)</b></td><td>0.00 <b>(-23.87%)</b></td><td>2382.40 <b>(+337.78%)</b></td><td>872.46 <b>(+125.89%)</b></td><td>509.90 <b>(+57.13%)</b></td><td>461.10 <b>(+88.13%)</b></td><td>844.35 <b>(+530.10%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>544.20 (n/a)</td><td>386.24 (n/a)</td><td>324.50 (n/a)</td><td>245.10 (n/a)</td><td>134.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (-10.17%)</td><td>0.01 (+16.73%)</td><td>0.01 (+5.83%)</td><td>0.01 <b>(+270.26%)</b></td><td>0.00 <b>(-65.26%)</b></td><td>535.80 <b>(-72.99%)</b></td><td>450.78 <b>(-40.58%)</b></td><td>455.20 (-5.52%)</td><td>363.80 (+11.32%)</td><td>61.41 <b>(-91.09%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1983.80 (n/a)</td><td>758.64 (n/a)</td><td>481.80 (n/a)</td><td>326.80 (n/a)</td><td>689.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 <b>(+21.72%)</b></td><td>0.04 <b>(+28.30%)</b></td><td>0.04 <b>(+88.02%)</b></td><td>0.02 (-12.15%)</td><td>0.01 <b>(+61.70%)</b></td><td>595.30 (+13.82%)</td><td>352.46 (-13.74%)</td><td>246.80 <b>(-46.82%)</b></td><td>204.20 (-17.83%)</td><td>173.33 <b>(+54.89%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.00 (n/a)</td><td>408.60 (n/a)</td><td>464.10 (n/a)</td><td>248.50 (n/a)</td><td>111.91 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 <b>(+30.03%)</b></td><td>0.02 (+1.94%)</td><td>0.03 (+12.60%)</td><td>0.01 <b>(-67.55%)</b></td><td>0.02 <b>(+136.32%)</b></td><td>1872.50 <b>(+208.13%)</b></td><td>781.72 <b>(+65.28%)</b></td><td>415.40 (-11.20%)</td><td>242.40 <b>(-23.07%)</b></td><td>700.78 <b>(+427.04%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>607.70 (n/a)</td><td>472.98 (n/a)</td><td>467.80 (n/a)</td><td>315.10 (n/a)</td><td>132.96 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 <b>(+88.09%)</b></td><td>0.03 <b>(+50.73%)</b></td><td>0.04 <b>(+72.61%)</b></td><td>0.02 <b>(-21.76%)</b></td><td>0.01 <b>(+440.22%)</b></td><td>680.30 <b>(+27.80%)</b></td><td>368.98 <b>(-24.59%)</b></td><td>297.50 <b>(-42.06%)</b></td><td>233.80 <b>(-46.83%)</b></td><td>179.20 <b>(+299.35%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>532.30 (n/a)</td><td>489.28 (n/a)</td><td>513.50 (n/a)</td><td>439.70 (n/a)</td><td>44.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-0.02%)</td><td>0.03 (+4.08%)</td><td>0.02 (-7.83%)</td><td>0.02 (+0.16%)</td><td>0.01 <b>(+30.28%)</b></td><td>498.70 (-0.16%)</td><td>414.68 (-1.78%)</td><td>473.70 (+8.50%)</td><td>301.70 (+0.03%)</td><td>99.30 <b>(+34.49%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>499.50 (n/a)</td><td>422.18 (n/a)</td><td>436.60 (n/a)</td><td>301.60 (n/a)</td><td>73.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-4.34%)</td><td>0.02 (-7.02%)</td><td>0.02 (-0.84%)</td><td>0.01 <b>(-37.21%)</b></td><td>0.01 (+12.14%)</td><td>1015.70 <b>(+59.28%)</b></td><td>570.80 (+16.15%)</td><td>514.90 (+0.84%)</td><td>301.30 (+4.51%)</td><td>266.71 <b>(+102.92%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>637.70 (n/a)</td><td>491.44 (n/a)</td><td>510.60 (n/a)</td><td>288.30 (n/a)</td><td>131.44 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 <b>(-29.37%)</b></td><td>0.02 (-11.92%)</td><td>0.02 (-2.02%)</td><td>0.02 (+8.65%)</td><td>0.00 <b>(-61.25%)</b></td><td>549.30 (-7.96%)</td><td>505.70 (+7.49%)</td><td>522.10 (+2.07%)</td><td>396.00 <b>(+41.58%)</b></td><td>62.63 <b>(-48.09%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>596.80 (n/a)</td><td>470.46 (n/a)</td><td>511.50 (n/a)</td><td>279.70 (n/a)</td><td>120.67 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (-13.76%)</td><td>0.06 (-0.68%)</td><td>0.06 <b>(+40.71%)</b></td><td>0.04 (-9.77%)</td><td>0.02 (-13.60%)</td><td>598.00 (+10.84%)</td><td>399.84 (+0.68%)</td><td>325.00 <b>(-28.93%)</b></td><td>263.20 (+15.95%)</td><td>146.68 (+14.83%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>539.50 (n/a)</td><td>397.14 (n/a)</td><td>457.30 (n/a)</td><td>227.00 (n/a)</td><td>127.73 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 <b>(+38.70%)</b></td><td>0.06 (+17.56%)</td><td>0.05 (-5.37%)</td><td>0.05 <b>(+22.76%)</b></td><td>0.02 <b>(+69.65%)</b></td><td>462.90 (-18.53%)</td><td>384.80 (-13.02%)</td><td>421.80 (+5.66%)</td><td>249.30 <b>(-27.91%)</b></td><td>92.26 (-0.24%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>568.20 (n/a)</td><td>442.38 (n/a)</td><td>399.20 (n/a)</td><td>345.80 (n/a)</td><td>92.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (+12.40%)</td><td>0.07 <b>(+22.58%)</b></td><td>0.08 <b>(+73.52%)</b></td><td>0.04 <b>(-21.21%)</b></td><td>0.02 <b>(+44.37%)</b></td><td>583.20 <b>(+26.92%)</b></td><td>331.32 (-12.70%)</td><td>251.60 <b>(-42.36%)</b></td><td>227.30 (-11.04%)</td><td>150.82 <b>(+56.92%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>459.50 (n/a)</td><td>379.52 (n/a)</td><td>436.50 (n/a)</td><td>255.50 (n/a)</td><td>96.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 <b>(+35.14%)</b></td><td>0.05 (+13.96%)</td><td>0.04 (-6.52%)</td><td>0.04 (-7.20%)</td><td>0.02 <b>(+147.37%)</b></td><td>593.80 (+7.77%)</td><td>453.54 (-4.01%)</td><td>529.10 (+6.95%)</td><td>262.30 <b>(-26.01%)</b></td><td>154.69 <b>(+105.26%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>551.00 (n/a)</td><td>472.50 (n/a)</td><td>494.70 (n/a)</td><td>354.50 (n/a)</td><td>75.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (+3.44%)</td><td>0.04 (+4.48%)</td><td>0.04 (+15.71%)</td><td>0.01 <b>(-31.02%)</b></td><td>0.03 (+8.19%)</td><td>1933.50 <b>(+44.97%)</b></td><td>735.56 (+13.24%)</td><td>499.90 (-13.59%)</td><td>242.30 (-3.35%)</td><td>679.62 <b>(+66.89%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1333.70 (n/a)</td><td>649.54 (n/a)</td><td>578.50 (n/a)</td><td>250.70 (n/a)</td><td>407.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (-6.99%)</td><td>0.04 <b>(-24.76%)</b></td><td>0.04 <b>(-26.76%)</b></td><td>0.01 <b>(-68.59%)</b></td><td>0.02 <b>(+26.45%)</b></td><td>1947.00 <b>(+218.40%)</b></td><td>722.14 <b>(+87.42%)</b></td><td>488.10 <b>(+36.53%)</b></td><td>282.60 (+7.53%)</td><td>691.00 <b>(+393.01%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.50 (n/a)</td><td>385.30 (n/a)</td><td>357.50 (n/a)</td><td>262.80 (n/a)</td><td>140.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>372.30 (n/a)</td><td>318.60 (n/a)</td><td>310.40 (n/a)</td><td>275.90 (n/a)</td><td>37.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.70 (n/a)</td><td>418.00 (n/a)</td><td>498.40 (n/a)</td><td>247.50 (n/a)</td><td>155.09 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>768.70 (n/a)</td><td>546.20 (n/a)</td><td>549.90 (n/a)</td><td>330.70 (n/a)</td><td>157.81 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>669.80 (n/a)</td><td>460.68 (n/a)</td><td>464.90 (n/a)</td><td>275.60 (n/a)</td><td>162.14 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2082.50 (n/a)</td><td>792.16 (n/a)</td><td>476.40 (n/a)</td><td>407.20 (n/a)</td><td>722.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.10 (n/a)</td><td>450.46 (n/a)</td><td>477.60 (n/a)</td><td>283.60 (n/a)</td><td>102.35 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>415.40 (n/a)</td><td>324.08 (n/a)</td><td>274.20 (n/a)</td><td>250.10 (n/a)</td><td>83.41 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>528.20 (n/a)</td><td>408.54 (n/a)</td><td>429.40 (n/a)</td><td>211.50 (n/a)</td><td>122.18 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>503.40 (n/a)</td><td>376.56 (n/a)</td><td>429.40 (n/a)</td><td>214.00 (n/a)</td><td>117.26 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.18 (-10.76%)</td><td>0.13 (+0.10%)</td><td>0.13 (-3.38%)</td><td>0.09 (+19.45%)</td><td>0.04 <b>(-25.29%)</b></td><td>527.90 (-16.29%)</td><td>392.16 (-5.18%)</td><td>390.40 (+3.50%)</td><td>280.40 (+12.07%)</td><td>106.02 <b>(-31.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>630.60 (n/a)</td><td>413.58 (n/a)</td><td>377.20 (n/a)</td><td>250.20 (n/a)</td><td>155.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>673.00 (n/a)</td><td>483.40 (n/a)</td><td>477.60 (n/a)</td><td>315.30 (n/a)</td><td>131.25 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>533.30 (n/a)</td><td>417.06 (n/a)</td><td>482.10 (n/a)</td><td>270.40 (n/a)</td><td>123.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1913.20 (n/a)</td><td>723.62 (n/a)</td><td>501.50 (n/a)</td><td>229.40 (n/a)</td><td>675.26 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1093.30 (n/a)</td><td>587.90 (n/a)</td><td>533.90 (n/a)</td><td>297.40 (n/a)</td><td>305.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.40 (n/a)</td><td>478.06 (n/a)</td><td>524.70 (n/a)</td><td>302.70 (n/a)</td><td>139.45 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>486.60 (n/a)</td><td>368.70 (n/a)</td><td>377.80 (n/a)</td><td>265.10 (n/a)</td><td>99.17 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>563.40 (n/a)</td><td>474.12 (n/a)</td><td>496.80 (n/a)</td><td>290.90 (n/a)</td><td>108.86 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.20 (n/a)</td><td>439.76 (n/a)</td><td>467.00 (n/a)</td><td>250.40 (n/a)</td><td>112.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>273.60 (n/a)</td><td>253.02 (n/a)</td><td>244.30 (n/a)</td><td>231.60 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>598.40 (n/a)</td><td>362.72 (n/a)</td><td>238.40 (n/a)</td><td>172.60 (n/a)</td><td>206.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>559.40 (n/a)</td><td>396.32 (n/a)</td><td>296.60 (n/a)</td><td>295.20 (n/a)</td><td>137.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>534.30 (n/a)</td><td>405.90 (n/a)</td><td>420.80 (n/a)</td><td>262.10 (n/a)</td><td>113.86 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>626.40 (n/a)</td><td>348.76 (n/a)</td><td>296.40 (n/a)</td><td>240.20 (n/a)</td><td>157.08 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.30 (n/a)</td><td>331.74 (n/a)</td><td>269.60 (n/a)</td><td>223.00 (n/a)</td><td>127.96 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.70 (n/a)</td><td>362.24 (n/a)</td><td>337.50 (n/a)</td><td>263.50 (n/a)</td><td>100.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2496.40 (n/a)</td><td>780.62 (n/a)</td><td>424.70 (n/a)</td><td>203.70 (n/a)</td><td>969.29 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.50 (n/a)</td><td>460.62 (n/a)</td><td>508.30 (n/a)</td><td>276.20 (n/a)</td><td>144.30 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.40 (n/a)</td><td>421.74 (n/a)</td><td>443.80 (n/a)</td><td>293.20 (n/a)</td><td>93.17 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>622.80 (n/a)</td><td>553.52 (n/a)</td><td>597.80 (n/a)</td><td>359.90 (n/a)</td><td>110.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2117.20 (n/a)</td><td>703.00 (n/a)</td><td>378.40 (n/a)</td><td>219.80 (n/a)</td><td>797.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.80 (n/a)</td><td>452.66 (n/a)</td><td>463.70 (n/a)</td><td>311.80 (n/a)</td><td>108.91 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.50 (n/a)</td><td>372.96 (n/a)</td><td>446.50 (n/a)</td><td>190.80 (n/a)</td><td>167.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.40 (n/a)</td><td>440.16 (n/a)</td><td>526.20 (n/a)</td><td>229.80 (n/a)</td><td>191.76 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.10 (n/a)</td><td>345.74 (n/a)</td><td>277.90 (n/a)</td><td>254.20 (n/a)</td><td>113.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1966.90 (n/a)</td><td>717.72 (n/a)</td><td>433.80 (n/a)</td><td>339.30 (n/a)</td><td>699.94 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>575.50 (n/a)</td><td>412.74 (n/a)</td><td>398.60 (n/a)</td><td>258.90 (n/a)</td><td>117.17 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.70 (n/a)</td><td>431.38 (n/a)</td><td>459.00 (n/a)</td><td>257.10 (n/a)</td><td>165.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2003.90 (n/a)</td><td>766.82 (n/a)</td><td>522.50 (n/a)</td><td>282.60 (n/a)</td><td>700.36 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>788.80 (n/a)</td><td>412.94 (n/a)</td><td>281.00 (n/a)</td><td>268.20 (n/a)</td><td>222.98 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2478.40 (n/a)</td><td>867.56 (n/a)</td><td>479.20 (n/a)</td><td>395.90 (n/a)</td><td>901.77 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>671.50 (n/a)</td><td>499.82 (n/a)</td><td>586.90 (n/a)</td><td>261.00 (n/a)</td><td>184.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>959.60 (n/a)</td><td>527.42 (n/a)</td><td>483.60 (n/a)</td><td>280.90 (n/a)</td><td>269.78 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>634.70 (n/a)</td><td>495.98 (n/a)</td><td>497.90 (n/a)</td><td>272.00 (n/a)</td><td>144.41 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>579.80 (n/a)</td><td>482.48 (n/a)</td><td>552.90 (n/a)</td><td>237.20 (n/a)</td><td>142.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>619.10 (n/a)</td><td>530.10 (n/a)</td><td>558.70 (n/a)</td><td>373.20 (n/a)</td><td>93.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2526.30 (n/a)</td><td>838.54 (n/a)</td><td>463.70 (n/a)</td><td>275.40 (n/a)</td><td>947.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>680.90 (n/a)</td><td>548.54 (n/a)</td><td>520.40 (n/a)</td><td>479.20 (n/a)</td><td>82.39 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.58 (+6.34%)</td><td>0.34 (-18.99%)</td><td>0.36 <b>(-21.28%)</b></td><td>0.13 <b>(-41.03%)</b></td><td>0.17 <b>(+36.57%)</b></td><td>1750.60 <b>(+69.60%)</b></td><td>840.34 <b>(+44.30%)</b></td><td>619.40 <b>(+27.03%)</b></td><td>383.30 (-5.96%)</td><td>542.69 <b>(+112.85%)</b></td><td>24.62 (+6.34%)</td><td>14.61 (-18.99%)</td><td>15.24 <b>(-21.28%)</b></td><td>5.39 <b>(-41.03%)</b></td><td>7.25 <b>(+36.57%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.54 (n/a)</td><td>0.42 (n/a)</td><td>0.45 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>1032.20 (n/a)</td><td>582.36 (n/a)</td><td>487.60 (n/a)</td><td>407.60 (n/a)</td><td>254.97 (n/a)</td><td>23.15 (n/a)</td><td>18.03 (n/a)</td><td>19.35 (n/a)</td><td>9.14 (n/a)</td><td>5.31 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.56 (-3.04%)</td><td>0.39 (-2.09%)</td><td>0.38 (-2.03%)</td><td>0.22 <b>(+150.31%)</b></td><td>0.12 <b>(-38.79%)</b></td><td>988.20 <b>(-60.05%)</b></td><td>624.50 <b>(-29.65%)</b></td><td>580.60 (+2.07%)</td><td>393.70 (+3.14%)</td><td>219.59 <b>(-75.40%)</b></td><td>23.97 (-3.04%)</td><td>16.48 (-2.09%)</td><td>16.25 (-2.03%)</td><td>9.55 <b>(+150.31%)</b></td><td>5.13 <b>(-38.79%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.58 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.09 (n/a)</td><td>0.20 (n/a)</td><td>2473.60 (n/a)</td><td>887.72 (n/a)</td><td>568.80 (n/a)</td><td>381.70 (n/a)</td><td>892.49 (n/a)</td><td>24.72 (n/a)</td><td>16.83 (n/a)</td><td>16.59 (n/a)</td><td>3.82 (n/a)</td><td>8.39 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.31 (+1.03%)</td><td>0.31 (+0.47%)</td><td>0.31 (+0.37%)</td><td>0.30 (+0.32%)</td><td>0.00 <b>(+33.53%)</b></td><td>82936.50 (-0.32%)</td><td>81784.84 (-0.46%)</td><td>81616.10 (-0.36%)</td><td>81004.90 (-1.02%)</td><td>769.42 <b>(+31.71%)</b></td><td>212.08 (+1.03%)</td><td>210.08 (+0.47%)</td><td>210.50 (+0.37%)</td><td>207.14 (+0.32%)</td><td>1.97 <b>(+33.53%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83201.60 (n/a)</td><td>82162.64 (n/a)</td><td>81914.70 (n/a)</td><td>81840.20 (n/a)</td><td>584.19 (n/a)</td><td>209.92 (n/a)</td><td>209.10 (n/a)</td><td>209.73 (n/a)</td><td>206.48 (n/a)</td><td>1.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>1.05 (+1.04%)</td><td>1.01 (-0.36%)</td><td>1.03 (+1.69%)</td><td>0.94 (-4.63%)</td><td>0.05 <b>(+104.21%)</b></td><td>26885.00 (+4.85%)</td><td>24902.40 (+0.49%)</td><td>24369.90 (-1.66%)</td><td>23950.10 (-1.02%)</td><td>1165.96 <b>(+112.99%)</b></td><td>717.32 (+1.04%)</td><td>691.04 (-0.36%)</td><td>704.96 (+1.69%)</td><td>639.01 (-4.63%)</td><td>30.88 <b>(+104.21%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>1.04 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25641.50 (n/a)</td><td>24780.04 (n/a)</td><td>24782.50 (n/a)</td><td>24198.10 (n/a)</td><td>547.43 (n/a)</td><td>709.97 (n/a)</td><td>693.56 (n/a)</td><td>693.23 (n/a)</td><td>670.00 (n/a)</td><td>15.12 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.82 (+0.42%)</td><td>0.80 (-0.42%)</td><td>0.79 (-1.92%)</td><td>0.79 (+2.43%)</td><td>0.01 <b>(-33.32%)</b></td><td>95909.80 (-2.38%)</td><td>94818.64 (+0.40%)</td><td>95362.90 (+1.96%)</td><td>92485.00 (-0.42%)</td><td>1417.88 <b>(-35.40%)</b></td><td>743.03 (+0.42%)</td><td>724.88 (-0.42%)</td><td>720.61 (-1.92%)</td><td>716.50 (+2.43%)</td><td>10.99 <b>(-33.32%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.77 (n/a)</td><td>0.02 (n/a)</td><td>98244.40 (n/a)</td><td>94439.38 (n/a)</td><td>93530.60 (n/a)</td><td>92874.90 (n/a)</td><td>2194.88 (n/a)</td><td>739.91 (n/a)</td><td>727.96 (n/a)</td><td>734.73 (n/a)</td><td>699.48 (n/a)</td><td>16.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.78 (+0.77%)</td><td>0.76 (-0.52%)</td><td>0.77 (+0.78%)</td><td>0.74 (-2.97%)</td><td>0.02 <b>(+347.11%)</b></td><td>102118.70 (+3.06%)</td><td>98938.66 (+0.56%)</td><td>97655.50 (-0.78%)</td><td>97169.60 (-0.76%)</td><td>2207.65 <b>(+356.67%)</b></td><td>707.21 (+0.77%)</td><td>694.84 (-0.52%)</td><td>703.69 (+0.78%)</td><td>672.94 (-2.97%)</td><td>15.32 <b>(+347.11%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.00 (n/a)</td><td>99085.40 (n/a)</td><td>98390.54 (n/a)</td><td>98421.80 (n/a)</td><td>97914.20 (n/a)</td><td>483.42 (n/a)</td><td>701.83 (n/a)</td><td>698.45 (n/a)</td><td>698.21 (n/a)</td><td>693.54 (n/a)</td><td>3.43 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.80 (+0.22%)</td><td>0.79 (+0.37%)</td><td>0.79 (+0.33%)</td><td>0.78 (+0.64%)</td><td>0.01 (-19.96%)</td><td>96407.90 (-0.64%)</td><td>95274.10 (-0.38%)</td><td>95424.80 (-0.33%)</td><td>94132.00 (-0.22%)</td><td>894.47 <b>(-20.61%)</b></td><td>730.03 (+0.22%)</td><td>721.33 (+0.37%)</td><td>720.14 (+0.33%)</td><td>712.80 (+0.64%)</td><td>6.78 (-19.96%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>97025.10 (n/a)</td><td>95634.34 (n/a)</td><td>95742.20 (n/a)</td><td>94343.40 (n/a)</td><td>1126.67 (n/a)</td><td>728.40 (n/a)</td><td>718.64 (n/a)</td><td>717.76 (n/a)</td><td>708.26 (n/a)</td><td>8.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.77 (+7.66%)</td><td>3.47 (-15.90%)</td><td>2.88 <b>(-28.86%)</b></td><td>1.96 (-0.48%)</td><td>1.50 (+11.58%)</td><td>4539.00 (+0.48%)</td><td>2953.00 (+19.98%)</td><td>3091.10 <b>(+40.57%)</b></td><td>1544.40 (-7.11%)</td><td>1155.51 (-1.86%)</td><td>347.62 (+7.66%)</td><td>208.74 (-15.90%)</td><td>173.68 <b>(-28.86%)</b></td><td>118.28 (-0.48%)</td><td>90.59 (+11.58%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.36 (n/a)</td><td>4.12 (n/a)</td><td>4.05 (n/a)</td><td>1.97 (n/a)</td><td>1.35 (n/a)</td><td>4517.30 (n/a)</td><td>2461.16 (n/a)</td><td>2198.90 (n/a)</td><td>1662.70 (n/a)</td><td>1177.39 (n/a)</td><td>322.89 (n/a)</td><td>248.22 (n/a)</td><td>244.16 (n/a)</td><td>118.85 (n/a)</td><td>81.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>4.60 (-4.71%)</td><td>2.86 (-9.69%)</td><td>2.18 <b>(-22.04%)</b></td><td>2.14 (-0.86%)</td><td>1.07 (-7.32%)</td><td>4173.90 (+0.87%)</td><td>3410.96 (+9.86%)</td><td>4090.20 <b>(+28.27%)</b></td><td>1939.30 (+4.95%)</td><td>1012.85 (-1.35%)</td><td>276.84 (-4.71%)</td><td>172.51 (-9.69%)</td><td>131.26 <b>(-22.04%)</b></td><td>128.63 (-0.86%)</td><td>64.65 (-7.32%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>4.82 (n/a)</td><td>3.17 (n/a)</td><td>2.80 (n/a)</td><td>2.15 (n/a)</td><td>1.16 (n/a)</td><td>4137.80 (n/a)</td><td>3104.80 (n/a)</td><td>3188.70 (n/a)</td><td>1847.90 (n/a)</td><td>1026.74 (n/a)</td><td>290.53 (n/a)</td><td>191.02 (n/a)</td><td>168.37 (n/a)</td><td>129.75 (n/a)</td><td>69.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>4.24 (-17.86%)</td><td>3.47 (-13.47%)</td><td>3.92 (-5.70%)</td><td>2.16 <b>(-21.54%)</b></td><td>0.91 <b>(-22.25%)</b></td><td>4130.70 <b>(+27.45%)</b></td><td>2746.58 (+14.86%)</td><td>2275.50 (+6.05%)</td><td>2100.10 <b>(+21.74%)</b></td><td>870.21 (+18.32%)</td><td>255.64 (-17.86%)</td><td>209.21 (-13.47%)</td><td>235.93 (-5.70%)</td><td>129.97 <b>(-21.54%)</b></td><td>54.90 <b>(-22.25%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.17 (n/a)</td><td>4.01 (n/a)</td><td>4.15 (n/a)</td><td>2.75 (n/a)</td><td>1.17 (n/a)</td><td>3241.00 (n/a)</td><td>2391.20 (n/a)</td><td>2145.70 (n/a)</td><td>1725.00 (n/a)</td><td>735.48 (n/a)</td><td>311.23 (n/a)</td><td>241.76 (n/a)</td><td>250.21 (n/a)</td><td>165.65 (n/a)</td><td>70.61 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>6.65 (+3.89%)</td><td>5.06 (-8.88%)</td><td>4.95 (-9.34%)</td><td>3.83 (-15.71%)</td><td>1.03 <b>(+39.08%)</b></td><td>9092.20 (+18.63%)</td><td>7115.54 (+11.64%)</td><td>7046.60 (+10.31%)</td><td>5244.90 (-3.75%)</td><td>1394.85 <b>(+58.27%)</b></td><td>409.44 (+3.89%)</td><td>311.56 (-8.88%)</td><td>304.75 (-9.34%)</td><td>236.19 (-15.71%)</td><td>63.46 <b>(+39.08%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>6.40 (n/a)</td><td>5.55 (n/a)</td><td>5.46 (n/a)</td><td>4.55 (n/a)</td><td>0.74 (n/a)</td><td>7664.20 (n/a)</td><td>6373.92 (n/a)</td><td>6388.10 (n/a)</td><td>5449.00 (n/a)</td><td>881.32 (n/a)</td><td>394.11 (n/a)</td><td>341.94 (n/a)</td><td>336.17 (n/a)</td><td>280.20 (n/a)</td><td>45.63 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.87 (+5.69%)</td><td>5.23 (+11.55%)</td><td>5.29 (+11.08%)</td><td>4.64 <b>(+21.85%)</b></td><td>0.47 <b>(-25.24%)</b></td><td>7508.50 (-17.93%)</td><td>6712.18 (-11.12%)</td><td>6592.60 (-9.98%)</td><td>5937.30 (-5.38%)</td><td>609.15 <b>(-42.28%)</b></td><td>361.69 (+5.69%)</td><td>322.05 (+11.55%)</td><td>325.74 (+11.08%)</td><td>286.01 <b>(+21.85%)</b></td><td>29.25 <b>(-25.24%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.56 (n/a)</td><td>4.69 (n/a)</td><td>4.76 (n/a)</td><td>3.81 (n/a)</td><td>0.64 (n/a)</td><td>9149.30 (n/a)</td><td>7551.58 (n/a)</td><td>7323.20 (n/a)</td><td>6274.90 (n/a)</td><td>1055.28 (n/a)</td><td>342.23 (n/a)</td><td>288.71 (n/a)</td><td>293.24 (n/a)</td><td>234.71 (n/a)</td><td>39.13 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>6.45 (+2.53%)</td><td>5.78 (+4.27%)</td><td>5.89 (+10.61%)</td><td>4.91 (+0.72%)</td><td>0.61 (+6.42%)</td><td>7103.00 (-0.71%)</td><td>6085.26 (-4.00%)</td><td>5921.20 (-9.59%)</td><td>5408.30 (-2.47%)</td><td>673.50 (+4.28%)</td><td>397.07 (+2.53%)</td><td>356.21 (+4.27%)</td><td>362.68 (+10.61%)</td><td>302.33 (+0.72%)</td><td>37.53 (+6.42%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>6.29 (n/a)</td><td>5.55 (n/a)</td><td>5.32 (n/a)</td><td>4.87 (n/a)</td><td>0.57 (n/a)</td><td>7154.00 (n/a)</td><td>6339.10 (n/a)</td><td>6549.30 (n/a)</td><td>5545.00 (n/a)</td><td>645.85 (n/a)</td><td>387.28 (n/a)</td><td>341.64 (n/a)</td><td>327.90 (n/a)</td><td>300.18 (n/a)</td><td>35.27 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.78 (-1.09%)</td><td>0.76 (-1.42%)</td><td>0.76 (-1.65%)</td><td>0.74 (-0.74%)</td><td>0.02 (-1.69%)</td><td>101456.40 (+0.75%)</td><td>98874.14 (+1.44%)</td><td>99140.40 (+1.68%)</td><td>96263.30 (+1.10%)</td><td>2049.57 (-0.19%)</td><td>713.87 (-1.09%)</td><td>695.26 (-1.42%)</td><td>693.15 (-1.65%)</td><td>677.33 (-0.74%)</td><td>14.43 (-1.69%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.02 (n/a)</td><td>100701.50 (n/a)</td><td>97469.16 (n/a)</td><td>97501.90 (n/a)</td><td>95218.70 (n/a)</td><td>2053.46 (n/a)</td><td>721.70 (n/a)</td><td>705.29 (n/a)</td><td>704.80 (n/a)</td><td>682.41 (n/a)</td><td>14.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.76 (-1.83%)</td><td>0.75 (-0.64%)</td><td>0.75 (-0.89%)</td><td>0.75 (+0.35%)</td><td>0.01 <b>(-38.68%)</b></td><td>100907.60 (-0.35%)</td><td>100095.42 (+0.63%)</td><td>100471.10 (+0.89%)</td><td>98924.30 (+1.86%)</td><td>933.73 <b>(-37.56%)</b></td><td>694.67 (-1.83%)</td><td>686.59 (-0.64%)</td><td>683.97 (-0.89%)</td><td>681.01 (+0.35%)</td><td>6.42 <b>(-38.68%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101258.40 (n/a)</td><td>99464.08 (n/a)</td><td>99580.70 (n/a)</td><td>97113.20 (n/a)</td><td>1495.31 (n/a)</td><td>707.62 (n/a)</td><td>691.02 (n/a)</td><td>690.09 (n/a)</td><td>678.65 (n/a)</td><td>10.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.80 (-1.33%)</td><td>0.79 (-0.27%)</td><td>0.79 (-1.04%)</td><td>0.79 (+1.10%)</td><td>0.01 <b>(-49.85%)</b></td><td>95884.80 (-1.08%)</td><td>95006.92 (+0.26%)</td><td>95320.80 (+1.06%)</td><td>94036.00 (+1.34%)</td><td>820.68 <b>(-49.82%)</b></td><td>730.78 (-1.33%)</td><td>723.35 (-0.27%)</td><td>720.93 (-1.04%)</td><td>716.69 (+1.10%)</td><td>6.26 <b>(-49.85%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96936.40 (n/a)</td><td>94765.02 (n/a)</td><td>94325.30 (n/a)</td><td>92789.10 (n/a)</td><td>1635.57 (n/a)</td><td>740.60 (n/a)</td><td>725.33 (n/a)</td><td>728.54 (n/a)</td><td>708.91 (n/a)</td><td>12.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>2.31 <b>(-32.49%)</b></td><td>1.75 <b>(-29.36%)</b></td><td>1.90 <b>(-38.90%)</b></td><td>1.26 (+11.87%)</td><td>0.47 <b>(-59.18%)</b></td><td>6390.80 (-10.61%)</td><td>4887.86 (+19.61%)</td><td>4238.30 <b>(+63.67%)</b></td><td>3489.40 <b>(+48.12%)</b></td><td>1365.52 <b>(-40.48%)</b></td><td>605.82 <b>(-32.49%)</b></td><td>459.59 <b>(-29.36%)</b></td><td>498.77 <b>(-38.90%)</b></td><td>330.78 (+11.87%)</td><td>122.26 <b>(-59.18%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>3.42 (n/a)</td><td>2.48 (n/a)</td><td>3.11 (n/a)</td><td>1.13 (n/a)</td><td>1.14 (n/a)</td><td>7149.60 (n/a)</td><td>4086.66 (n/a)</td><td>2589.60 (n/a)</td><td>2355.80 (n/a)</td><td>2294.06 (n/a)</td><td>897.34 (n/a)</td><td>650.61 (n/a)</td><td>816.33 (n/a)</td><td>295.67 (n/a)</td><td>299.49 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.32 (-1.66%)</td><td>0.24 (+1.75%)</td><td>0.22 (-10.34%)</td><td>0.19 <b>(+27.48%)</b></td><td>0.06 (-8.12%)</td><td>6416.30 <b>(-21.56%)</b></td><td>5322.76 (-3.57%)</td><td>5703.60 (+11.54%)</td><td>3946.70 (+1.69%)</td><td>1128.71 <b>(-29.45%)</b></td><td>17.00 (-1.66%)</td><td>13.11 (+1.75%)</td><td>11.77 (-10.34%)</td><td>10.46 <b>(+27.48%)</b></td><td>2.98 (-8.12%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>8179.70 (n/a)</td><td>5519.64 (n/a)</td><td>5113.60 (n/a)</td><td>3881.10 (n/a)</td><td>1599.89 (n/a)</td><td>17.29 (n/a)</td><td>12.89 (n/a)</td><td>13.12 (n/a)</td><td>8.20 (n/a)</td><td>3.25 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.96 (n/a)</td><td>3.72 (n/a)</td><td>3.88 (n/a)</td><td>3.41 (n/a)</td><td>0.28 (n/a)</td><td>3.96 (n/a)</td><td>3.72 (n/a)</td><td>3.88 (n/a)</td><td>3.41 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>6.69 (-3.55%)</td><td>6.09 (-6.31%)</td><td>6.58 (+0.14%)</td><td>4.89 (-13.11%)</td><td>0.81 <b>(+51.12%)</b></td><td>6.69 (-3.55%)</td><td>6.08 (-6.31%)</td><td>6.57 (+0.14%)</td><td>4.88 (-13.11%)</td><td>0.81 <b>(+51.12%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>6.94 (n/a)</td><td>6.50 (n/a)</td><td>6.57 (n/a)</td><td>5.63 (n/a)</td><td>0.53 (n/a)</td><td>6.93 (n/a)</td><td>6.49 (n/a)</td><td>6.57 (n/a)</td><td>5.62 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>13.94 <b>(+27.53%)</b></td><td>9.35 (+10.60%)</td><td>8.63 (+1.38%)</td><td>6.86 <b>(+21.61%)</b></td><td>2.70 <b>(+33.20%)</b></td><td>13.93 <b>(+27.53%)</b></td><td>9.34 (+10.60%)</td><td>8.62 (+1.38%)</td><td>6.86 <b>(+21.61%)</b></td><td>2.70 <b>(+33.20%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>10.93 (n/a)</td><td>8.45 (n/a)</td><td>8.51 (n/a)</td><td>5.64 (n/a)</td><td>2.02 (n/a)</td><td>10.92 (n/a)</td><td>8.45 (n/a)</td><td>8.51 (n/a)</td><td>5.64 (n/a)</td><td>2.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.80 (n/a)</td><td>3.53 (n/a)</td><td>3.49 (n/a)</td><td>3.25 (n/a)</td><td>0.23 (n/a)</td><td>3.80 (n/a)</td><td>3.53 (n/a)</td><td>3.49 (n/a)</td><td>3.25 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>7.14 (-0.99%)</td><td>6.24 (-5.11%)</td><td>6.55 (-5.69%)</td><td>5.05 (-12.12%)</td><td>0.87 (+16.47%)</td><td>7.13 (-0.99%)</td><td>6.24 (-5.11%)</td><td>6.55 (-5.69%)</td><td>5.04 (-12.12%)</td><td>0.87 (+16.47%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>7.21 (n/a)</td><td>6.58 (n/a)</td><td>6.95 (n/a)</td><td>5.74 (n/a)</td><td>0.74 (n/a)</td><td>7.21 (n/a)</td><td>6.58 (n/a)</td><td>6.94 (n/a)</td><td>5.74 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>13.33 (-2.02%)</td><td>10.05 (-2.32%)</td><td>10.05 (+9.53%)</td><td>8.15 (+15.40%)</td><td>2.06 <b>(-34.09%)</b></td><td>13.32 (-2.02%)</td><td>10.05 (-2.32%)</td><td>10.04 (+9.53%)</td><td>8.14 (+15.40%)</td><td>2.05 <b>(-34.09%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>13.61 (n/a)</td><td>10.29 (n/a)</td><td>9.17 (n/a)</td><td>7.06 (n/a)</td><td>3.12 (n/a)</td><td>13.60 (n/a)</td><td>10.28 (n/a)</td><td>9.17 (n/a)</td><td>7.05 (n/a)</td><td>3.12 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.10 (+5.03%)</td><td>1.89 (+18.68%)</td><td>1.46 (+15.07%)</td><td>1.01 (-3.68%)</td><td>1.02 <b>(+30.60%)</b></td><td>3.09 (+5.03%)</td><td>1.89 (+18.68%)</td><td>1.46 (+15.07%)</td><td>1.01 (-3.68%)</td><td>1.02 <b>(+30.60%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.95 (n/a)</td><td>1.59 (n/a)</td><td>1.27 (n/a)</td><td>1.05 (n/a)</td><td>0.78 (n/a)</td><td>2.95 (n/a)</td><td>1.59 (n/a)</td><td>1.27 (n/a)</td><td>1.04 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.54 (+13.60%)</td><td>0.41 <b>(+24.43%)</b></td><td>0.35 (+0.49%)</td><td>0.32 <b>(+326.90%)</b></td><td>0.09 <b>(-44.54%)</b></td><td>0.53 (+13.60%)</td><td>0.40 <b>(+24.43%)</b></td><td>0.35 (+0.49%)</td><td>0.32 <b>(+326.90%)</b></td><td>0.09 <b>(-44.54%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.48 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>0.17 (n/a)</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.35 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.56 (-16.06%)</td><td>0.26 <b>(-56.05%)</b></td><td>0.08 <b>(-87.66%)</b></td><td>0.08 <b>(-82.00%)</b></td><td>0.25 <b>(+152.60%)</b></td><td>0.55 (-16.06%)</td><td>0.25 <b>(-56.05%)</b></td><td>0.07 <b>(-87.66%)</b></td><td>0.07 <b>(-82.00%)</b></td><td>0.25 <b>(+152.60%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.67 (n/a)</td><td>0.59 (n/a)</td><td>0.61 (n/a)</td><td>0.42 (n/a)</td><td>0.10 (n/a)</td><td>0.66 (n/a)</td><td>0.58 (n/a)</td><td>0.61 (n/a)</td><td>0.41 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>2.67 (+2.09%)</td><td>1.66 (+8.92%)</td><td>2.29 <b>(+23.87%)</b></td><td>0.42 (-2.69%)</td><td>1.13 (+9.89%)</td><td>2.63 (+2.09%)</td><td>1.64 (+8.92%)</td><td>2.25 <b>(+23.87%)</b></td><td>0.41 (-2.69%)</td><td>1.11 (+9.89%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.62 (n/a)</td><td>1.53 (n/a)</td><td>1.85 (n/a)</td><td>0.43 (n/a)</td><td>1.03 (n/a)</td><td>2.58 (n/a)</td><td>1.50 (n/a)</td><td>1.82 (n/a)</td><td>0.42 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.10 (n/a)</td><td>391.48 (n/a)</td><td>347.60 (n/a)</td><td>259.00 (n/a)</td><td>136.99 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>645.50 (n/a)</td><td>334.22 (n/a)</td><td>283.40 (n/a)</td><td>209.60 (n/a)</td><td>177.55 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>317.00 (n/a)</td><td>257.80 (n/a)</td><td>259.60 (n/a)</td><td>192.20 (n/a)</td><td>50.33 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>669.30 (n/a)</td><td>447.34 (n/a)</td><td>525.20 (n/a)</td><td>228.60 (n/a)</td><td>192.46 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1955.80 (n/a)</td><td>661.92 (n/a)</td><td>318.30 (n/a)</td><td>245.20 (n/a)</td><td>729.45 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>744.50 (n/a)</td><td>533.36 (n/a)</td><td>598.00 (n/a)</td><td>237.70 (n/a)</td><td>196.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.70 (n/a)</td><td>378.56 (n/a)</td><td>404.10 (n/a)</td><td>246.20 (n/a)</td><td>105.41 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.50 (n/a)</td><td>364.02 (n/a)</td><td>367.20 (n/a)</td><td>248.70 (n/a)</td><td>84.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2415.80 (n/a)</td><td>751.92 (n/a)</td><td>288.00 (n/a)</td><td>251.10 (n/a)</td><td>936.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.80 (n/a)</td><td>332.68 (n/a)</td><td>282.20 (n/a)</td><td>245.30 (n/a)</td><td>116.44 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.50 (n/a)</td><td>429.70 (n/a)</td><td>475.40 (n/a)</td><td>239.00 (n/a)</td><td>162.55 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.40 (n/a)</td><td>464.84 (n/a)</td><td>463.50 (n/a)</td><td>287.70 (n/a)</td><td>112.23 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>733.50 (n/a)</td><td>463.50 (n/a)</td><td>522.40 (n/a)</td><td>249.60 (n/a)</td><td>199.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1127.40 (n/a)</td><td>475.08 (n/a)</td><td>299.30 (n/a)</td><td>234.50 (n/a)</td><td>371.98 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>635.90 (n/a)</td><td>439.88 (n/a)</td><td>446.60 (n/a)</td><td>274.20 (n/a)</td><td>159.78 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>456.00 (n/a)</td><td>400.28 (n/a)</td><td>447.10 (n/a)</td><td>277.00 (n/a)</td><td>78.49 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>652.60 (n/a)</td><td>476.88 (n/a)</td><td>476.10 (n/a)</td><td>237.40 (n/a)</td><td>163.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>605.40 (n/a)</td><td>500.84 (n/a)</td><td>525.70 (n/a)</td><td>337.70 (n/a)</td><td>104.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>696.60 (n/a)</td><td>610.22 (n/a)</td><td>608.90 (n/a)</td><td>470.70 (n/a)</td><td>88.62 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>536.80 (n/a)</td><td>388.66 (n/a)</td><td>323.40 (n/a)</td><td>242.40 (n/a)</td><td>137.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>798.70 (n/a)</td><td>473.24 (n/a)</td><td>562.90 (n/a)</td><td>168.40 (n/a)</td><td>253.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>588.50 (n/a)</td><td>448.86 (n/a)</td><td>490.80 (n/a)</td><td>271.30 (n/a)</td><td>147.42 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1895.50 (n/a)</td><td>677.94 (n/a)</td><td>421.10 (n/a)</td><td>236.90 (n/a)</td><td>690.33 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>451.20 (n/a)</td><td>407.88 (n/a)</td><td>439.20 (n/a)</td><td>296.90 (n/a)</td><td>63.81 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (-1.77%)</td><td>0.01 (-7.35%)</td><td>0.01 (-4.69%)</td><td>0.01 (+10.56%)</td><td>0.00 (-2.56%)</td><td>496.80 (-9.54%)</td><td>356.54 (+6.77%)</td><td>296.30 (+4.92%)</td><td>260.20 (+1.80%)</td><td>107.20 (-12.47%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>549.20 (n/a)</td><td>333.92 (n/a)</td><td>282.40 (n/a)</td><td>255.60 (n/a)</td><td>122.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 <b>(-30.54%)</b></td><td>0.01 <b>(-33.11%)</b></td><td>0.01 (-18.66%)</td><td>0.00 <b>(-71.18%)</b></td><td>0.00 <b>(-20.69%)</b></td><td>2507.50 <b>(+247.06%)</b></td><td>867.76 <b>(+111.03%)</b></td><td>510.10 <b>(+22.95%)</b></td><td>280.10 <b>(+44.01%)</b></td><td>922.63 <b>(+366.43%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>722.50 (n/a)</td><td>411.20 (n/a)</td><td>414.90 (n/a)</td><td>194.50 (n/a)</td><td>197.81 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (-3.08%)</td><td>0.01 <b>(-27.06%)</b></td><td>0.01 <b>(-41.35%)</b></td><td>0.01 <b>(-28.65%)</b></td><td>0.01 (+12.17%)</td><td>599.20 <b>(+40.16%)</b></td><td>450.70 <b>(+44.26%)</b></td><td>490.60 <b>(+70.47%)</b></td><td>200.00 (+3.20%)</td><td>149.61 <b>(+40.04%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>427.50 (n/a)</td><td>312.42 (n/a)</td><td>287.80 (n/a)</td><td>193.80 (n/a)</td><td>106.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 <b>(-47.04%)</b></td><td>0.01 (-15.62%)</td><td>0.01 (-6.57%)</td><td>0.00 <b>(+83.64%)</b></td><td>0.00 <b>(-58.23%)</b></td><td>1094.10 <b>(-45.55%)</b></td><td>594.48 <b>(-22.57%)</b></td><td>584.90 (+7.03%)</td><td>313.00 <b>(+88.78%)</b></td><td>304.80 <b>(-57.34%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2009.20 (n/a)</td><td>767.76 (n/a)</td><td>546.50 (n/a)</td><td>165.80 (n/a)</td><td>714.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (-5.53%)</td><td>0.01 (-8.45%)</td><td>0.01 <b>(-35.89%)</b></td><td>0.01 (-5.94%)</td><td>0.00 (+8.83%)</td><td>648.80 (+6.33%)</td><td>437.74 (+12.18%)</td><td>500.10 <b>(+55.99%)</b></td><td>245.80 (+5.86%)</td><td>176.96 (+11.48%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.20 (n/a)</td><td>390.20 (n/a)</td><td>320.60 (n/a)</td><td>232.20 (n/a)</td><td>158.74 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (-7.60%)</td><td>0.01 (-5.63%)</td><td>0.01 (+11.57%)</td><td>0.01 (+12.24%)</td><td>0.00 <b>(-29.78%)</b></td><td>583.60 (-10.90%)</td><td>444.70 (-2.29%)</td><td>459.90 (-10.37%)</td><td>261.60 (+8.23%)</td><td>115.63 <b>(-35.86%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>655.00 (n/a)</td><td>455.12 (n/a)</td><td>513.10 (n/a)</td><td>241.70 (n/a)</td><td>180.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (+1.38%)</td><td>0.02 (-4.30%)</td><td>0.02 <b>(-26.81%)</b></td><td>0.01 (-6.34%)</td><td>0.01 (-0.67%)</td><td>631.00 (+6.77%)</td><td>411.00 (+2.78%)</td><td>423.20 <b>(+36.60%)</b></td><td>200.90 (-1.33%)</td><td>162.87 (-8.35%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.00 (n/a)</td><td>399.90 (n/a)</td><td>309.80 (n/a)</td><td>203.60 (n/a)</td><td>177.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-14.04%)</td><td>0.02 (+1.24%)</td><td>0.03 <b>(+84.87%)</b></td><td>0.01 (-11.71%)</td><td>0.01 (-16.61%)</td><td>594.20 (+13.27%)</td><td>390.62 (-2.56%)</td><td>279.10 <b>(-45.90%)</b></td><td>244.40 (+16.33%)</td><td>179.37 (+9.73%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.60 (n/a)</td><td>400.90 (n/a)</td><td>515.90 (n/a)</td><td>210.10 (n/a)</td><td>163.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (+5.85%)</td><td>0.02 (-0.52%)</td><td>0.02 <b>(-25.12%)</b></td><td>0.02 (-6.75%)</td><td>0.01 <b>(+20.81%)</b></td><td>520.40 (+7.23%)</td><td>368.06 (+2.93%)</td><td>387.00 <b>(+33.54%)</b></td><td>234.40 (-5.52%)</td><td>127.57 (+8.89%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>485.30 (n/a)</td><td>357.58 (n/a)</td><td>289.80 (n/a)</td><td>248.10 (n/a)</td><td>117.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 <b>(-31.72%)</b></td><td>0.02 (-8.94%)</td><td>0.02 (+8.19%)</td><td>0.02 (+3.28%)</td><td>0.01 <b>(-48.87%)</b></td><td>511.00 (-3.16%)</td><td>382.96 (+0.13%)</td><td>409.00 (-7.59%)</td><td>284.60 <b>(+46.47%)</b></td><td>97.52 <b>(-32.33%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.70 (n/a)</td><td>382.48 (n/a)</td><td>442.60 (n/a)</td><td>194.30 (n/a)</td><td>144.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (+9.89%)</td><td>0.02 (+1.00%)</td><td>0.03 (-1.47%)</td><td>0.01 (+3.48%)</td><td>0.01 (+14.25%)</td><td>596.00 (-3.36%)</td><td>379.46 (+0.88%)</td><td>298.30 (+1.50%)</td><td>238.20 (-9.01%)</td><td>156.49 (+3.62%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.70 (n/a)</td><td>376.14 (n/a)</td><td>293.90 (n/a)</td><td>261.80 (n/a)</td><td>151.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(-43.93%)</b></td><td>0.01 <b>(-48.58%)</b></td><td>0.01 <b>(-46.49%)</b></td><td>0.01 <b>(-48.07%)</b></td><td>0.01 <b>(-43.95%)</b></td><td>1087.00 <b>(+92.56%)</b></td><td>626.16 <b>(+95.49%)</b></td><td>547.20 <b>(+86.89%)</b></td><td>356.80 <b>(+78.31%)</b></td><td>273.81 <b>(+91.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.50 (n/a)</td><td>320.30 (n/a)</td><td>292.80 (n/a)</td><td>200.10 (n/a)</td><td>142.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 <b>(-21.00%)</b></td><td>0.02 (-4.39%)</td><td>0.02 (-9.48%)</td><td>0.01 <b>(+200.96%)</b></td><td>0.01 <b>(-47.21%)</b></td><td>631.20 <b>(-66.78%)</b></td><td>498.22 <b>(-30.03%)</b></td><td>482.90 (+10.48%)</td><td>298.80 <b>(+26.56%)</b></td><td>136.42 <b>(-79.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1899.80 (n/a)</td><td>712.04 (n/a)</td><td>437.10 (n/a)</td><td>236.10 (n/a)</td><td>676.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 <b>(+43.60%)</b></td><td>0.02 <b>(+29.43%)</b></td><td>0.02 <b>(+43.59%)</b></td><td>0.01 <b>(-27.34%)</b></td><td>0.01 <b>(+131.48%)</b></td><td>967.50 <b>(+37.62%)</b></td><td>515.50 (-9.84%)</td><td>420.30 <b>(-30.36%)</b></td><td>270.60 <b>(-30.37%)</b></td><td>278.32 <b>(+134.23%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>703.00 (n/a)</td><td>571.74 (n/a)</td><td>603.50 (n/a)</td><td>388.60 (n/a)</td><td>118.82 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (-4.96%)</td><td>0.06 <b>(+34.32%)</b></td><td>0.06 <b>(+76.10%)</b></td><td>0.05 <b>(+78.26%)</b></td><td>0.01 <b>(-62.18%)</b></td><td>336.90 <b>(-43.91%)</b></td><td>276.32 <b>(-35.53%)</b></td><td>270.10 <b>(-43.21%)</b></td><td>243.80 (+5.22%)</td><td>38.47 <b>(-77.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>600.60 (n/a)</td><td>428.62 (n/a)</td><td>475.60 (n/a)</td><td>231.70 (n/a)</td><td>173.51 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 <b>(+60.51%)</b></td><td>0.06 <b>(+56.66%)</b></td><td>0.06 <b>(+83.62%)</b></td><td>0.03 (-19.65%)</td><td>0.02 <b>(+254.46%)</b></td><td>638.70 <b>(+24.45%)</b></td><td>330.42 <b>(-27.04%)</b></td><td>252.10 <b>(-45.54%)</b></td><td>221.50 <b>(-37.69%)</b></td><td>174.92 <b>(+199.59%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>513.20 (n/a)</td><td>452.90 (n/a)</td><td>462.90 (n/a)</td><td>355.50 (n/a)</td><td>58.39 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (+15.87%)</td><td>0.05 (+19.15%)</td><td>0.04 (+16.97%)</td><td>0.03 (+9.25%)</td><td>0.01 <b>(+31.80%)</b></td><td>541.50 (-8.45%)</td><td>391.88 (-14.37%)</td><td>418.50 (-14.50%)</td><td>257.30 (-13.69%)</td><td>115.09 (+4.90%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.50 (n/a)</td><td>457.64 (n/a)</td><td>489.50 (n/a)</td><td>298.10 (n/a)</td><td>109.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 <b>(+43.00%)</b></td><td>0.05 <b>(+38.26%)</b></td><td>0.05 <b>(+41.77%)</b></td><td>0.02 <b>(+57.13%)</b></td><td>0.02 <b>(+47.52%)</b></td><td>686.90 <b>(-36.36%)</b></td><td>403.60 <b>(-28.03%)</b></td><td>303.00 <b>(-29.45%)</b></td><td>244.20 <b>(-30.07%)</b></td><td>195.94 <b>(-35.77%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1079.40 (n/a)</td><td>560.80 (n/a)</td><td>429.50 (n/a)</td><td>349.20 (n/a)</td><td>305.07 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (-6.72%)</td><td>0.05 (+3.14%)</td><td>0.05 <b>(+39.80%)</b></td><td>0.03 <b>(-25.35%)</b></td><td>0.01 (-0.56%)</td><td>614.40 <b>(+33.97%)</b></td><td>376.02 (-0.56%)</td><td>316.00 <b>(-28.47%)</b></td><td>258.10 (+7.23%)</td><td>142.80 <b>(+42.96%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>458.60 (n/a)</td><td>378.12 (n/a)</td><td>441.80 (n/a)</td><td>240.70 (n/a)</td><td>99.89 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 <b>(+72.99%)</b></td><td>0.04 <b>(+24.57%)</b></td><td>0.03 (-1.62%)</td><td>0.03 (+16.44%)</td><td>0.02 <b>(+191.02%)</b></td><td>562.40 (-14.12%)</td><td>443.46 (-14.08%)</td><td>495.10 (+1.64%)</td><td>248.50 <b>(-42.20%)</b></td><td>129.96 <b>(+43.24%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>654.90 (n/a)</td><td>516.12 (n/a)</td><td>487.10 (n/a)</td><td>429.90 (n/a)</td><td>90.72 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (-6.91%)</td><td>0.10 <b>(+21.83%)</b></td><td>0.11 <b>(+69.76%)</b></td><td>0.05 (+19.49%)</td><td>0.04 (-4.68%)</td><td>636.50 (-16.31%)</td><td>402.54 (-19.05%)</td><td>298.60 <b>(-41.08%)</b></td><td>241.70 (+7.42%)</td><td>186.40 (-9.31%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>760.50 (n/a)</td><td>497.26 (n/a)</td><td>506.80 (n/a)</td><td>225.00 (n/a)</td><td>205.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 <b>(+20.61%)</b></td><td>0.08 (-16.70%)</td><td>0.07 <b>(-28.82%)</b></td><td>0.01 <b>(-82.78%)</b></td><td>0.05 <b>(+170.14%)</b></td><td>2450.20 <b>(+480.48%)</b></td><td>782.16 <b>(+122.96%)</b></td><td>444.70 <b>(+40.46%)</b></td><td>243.20 (-17.08%)</td><td>937.24 <b>(+1333.94%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>422.10 (n/a)</td><td>350.80 (n/a)</td><td>316.60 (n/a)</td><td>293.30 (n/a)</td><td>65.36 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (+16.27%)</td><td>0.09 <b>(+44.90%)</b></td><td>0.09 <b>(+50.16%)</b></td><td>0.06 <b>(+238.89%)</b></td><td>0.03 <b>(-20.76%)</b></td><td>561.60 <b>(-70.49%)</b></td><td>385.06 <b>(-50.78%)</b></td><td>363.50 <b>(-33.40%)</b></td><td>249.40 (-14.00%)</td><td>128.90 <b>(-80.41%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1903.30 (n/a)</td><td>782.26 (n/a)</td><td>545.80 (n/a)</td><td>290.00 (n/a)</td><td>657.91 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (-9.14%)</td><td>0.10 <b>(+38.33%)</b></td><td>0.11 <b>(+43.80%)</b></td><td>0.08 <b>(+168.93%)</b></td><td>0.02 <b>(-50.44%)</b></td><td>391.40 <b>(-62.82%)</b></td><td>323.20 <b>(-40.81%)</b></td><td>298.70 <b>(-30.45%)</b></td><td>265.30 (+10.08%)</td><td>62.11 <b>(-79.86%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1052.60 (n/a)</td><td>546.00 (n/a)</td><td>429.50 (n/a)</td><td>241.00 (n/a)</td><td>308.41 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (-7.91%)</td><td>0.08 (-1.44%)</td><td>0.09 <b>(+38.50%)</b></td><td>0.03 <b>(-44.19%)</b></td><td>0.03 (+3.92%)</td><td>1128.10 <b>(+79.18%)</b></td><td>521.24 (+14.10%)</td><td>375.90 <b>(-27.79%)</b></td><td>307.60 (+8.58%)</td><td>345.44 <b>(+120.67%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>629.60 (n/a)</td><td>456.82 (n/a)</td><td>520.60 (n/a)</td><td>283.30 (n/a)</td><td>156.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (+19.83%)</td><td>0.01 (+6.72%)</td><td>0.01 (+1.97%)</td><td>0.01 (+15.22%)</td><td>0.00 <b>(+28.40%)</b></td><td>524.30 (-13.21%)</td><td>374.00 (-4.04%)</td><td>309.60 (-1.93%)</td><td>244.70 (-16.54%)</td><td>136.98 (+1.83%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>604.10 (n/a)</td><td>389.74 (n/a)</td><td>315.70 (n/a)</td><td>293.20 (n/a)</td><td>134.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (-8.37%)</td><td>0.01 (-12.71%)</td><td>0.01 (+5.89%)</td><td>0.01 <b>(-36.79%)</b></td><td>0.00 <b>(+115.97%)</b></td><td>527.50 <b>(+58.22%)</b></td><td>360.88 <b>(+23.00%)</b></td><td>277.10 (-5.56%)</td><td>271.40 (+9.17%)</td><td>121.46 <b>(+257.66%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>333.40 (n/a)</td><td>293.40 (n/a)</td><td>293.40 (n/a)</td><td>248.60 (n/a)</td><td>33.96 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 <b>(-24.09%)</b></td><td>0.01 <b>(-32.55%)</b></td><td>0.01 (-13.11%)</td><td>0.00 <b>(-79.74%)</b></td><td>0.00 (+11.78%)</td><td>2452.50 <b>(+393.66%)</b></td><td>864.28 <b>(+119.97%)</b></td><td>499.70 (+15.09%)</td><td>374.00 <b>(+31.74%)</b></td><td>889.58 <b>(+774.61%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.80 (n/a)</td><td>392.90 (n/a)</td><td>434.20 (n/a)</td><td>283.90 (n/a)</td><td>101.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (+4.61%)</td><td>0.01 (+18.55%)</td><td>0.02 <b>(+30.05%)</b></td><td>0.01 (+9.00%)</td><td>0.00 (+6.46%)</td><td>486.90 (-8.27%)</td><td>325.20 (-16.40%)</td><td>259.10 <b>(-23.12%)</b></td><td>240.10 (-4.42%)</td><td>111.52 (-15.92%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.80 (n/a)</td><td>389.00 (n/a)</td><td>337.00 (n/a)</td><td>251.20 (n/a)</td><td>132.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (-0.26%)</td><td>0.01 (+5.15%)</td><td>0.01 (-10.82%)</td><td>0.01 <b>(+243.12%)</b></td><td>0.00 <b>(-34.83%)</b></td><td>548.80 <b>(-70.85%)</b></td><td>458.14 <b>(-34.09%)</b></td><td>473.90 (+12.11%)</td><td>280.80 (+0.29%)</td><td>104.25 <b>(-84.39%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1882.90 (n/a)</td><td>695.06 (n/a)</td><td>422.70 (n/a)</td><td>280.00 (n/a)</td><td>667.96 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(+23.09%)</b></td><td>0.01 <b>(+50.74%)</b></td><td>0.01 <b>(+57.77%)</b></td><td>0.01 <b>(+36.82%)</b></td><td>0.00 (+15.03%)</td><td>411.00 <b>(-26.91%)</b></td><td>291.46 <b>(-34.46%)</b></td><td>294.30 <b>(-36.61%)</b></td><td>227.60 (-18.74%)</td><td>74.74 <b>(-31.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.30 (n/a)</td><td>444.72 (n/a)</td><td>464.30 (n/a)</td><td>280.10 (n/a)</td><td>109.33 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (-18.61%)</td><td>0.01 <b>(-26.57%)</b></td><td>0.01 (-14.52%)</td><td>0.00 <b>(-77.71%)</b></td><td>0.00 <b>(+86.85%)</b></td><td>2421.30 <b>(+348.64%)</b></td><td>890.44 <b>(+97.89%)</b></td><td>538.30 (+17.00%)</td><td>449.10 <b>(+22.84%)</b></td><td>856.87 <b>(+1038.32%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.70 (n/a)</td><td>449.96 (n/a)</td><td>460.10 (n/a)</td><td>365.60 (n/a)</td><td>75.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(+63.08%)</b></td><td>0.01 <b>(+33.79%)</b></td><td>0.01 <b>(+53.46%)</b></td><td>0.01 <b>(-20.18%)</b></td><td>0.01 <b>(+105.94%)</b></td><td>604.60 <b>(+25.28%)</b></td><td>329.34 (-17.18%)</td><td>285.40 <b>(-34.84%)</b></td><td>178.40 <b>(-38.67%)</b></td><td>161.23 <b>(+70.02%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>482.60 (n/a)</td><td>397.66 (n/a)</td><td>438.00 (n/a)</td><td>290.90 (n/a)</td><td>94.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(+43.23%)</b></td><td>0.01 <b>(+35.88%)</b></td><td>0.01 <b>(+56.53%)</b></td><td>0.01 (+7.59%)</td><td>0.00 <b>(+128.15%)</b></td><td>555.80 (-7.06%)</td><td>392.38 <b>(-20.48%)</b></td><td>308.50 <b>(-36.12%)</b></td><td>251.00 <b>(-30.18%)</b></td><td>147.09 <b>(+61.34%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.00 (n/a)</td><td>493.42 (n/a)</td><td>482.90 (n/a)</td><td>359.50 (n/a)</td><td>91.17 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (-19.73%)</td><td>0.01 (-17.19%)</td><td>0.01 (-14.84%)</td><td>0.01 (-10.52%)</td><td>0.00 <b>(-26.20%)</b></td><td>455.60 (+11.75%)</td><td>363.16 (+19.74%)</td><td>341.60 (+17.43%)</td><td>282.20 <b>(+24.54%)</b></td><td>66.70 (+1.71%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>407.70 (n/a)</td><td>303.28 (n/a)</td><td>290.90 (n/a)</td><td>226.60 (n/a)</td><td>65.57 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 <b>(-29.52%)</b></td><td>0.01 (-8.21%)</td><td>0.01 <b>(+21.06%)</b></td><td>0.00 <b>(-27.45%)</b></td><td>0.00 <b>(-35.29%)</b></td><td>1102.90 <b>(+37.85%)</b></td><td>623.46 (+7.56%)</td><td>525.80 (-17.40%)</td><td>356.20 <b>(+41.91%)</b></td><td>292.23 <b>(+44.61%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>800.10 (n/a)</td><td>579.64 (n/a)</td><td>636.60 (n/a)</td><td>251.00 (n/a)</td><td>202.07 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (+17.17%)</td><td>0.01 (-11.38%)</td><td>0.01 <b>(-29.56%)</b></td><td>0.00 <b>(-68.67%)</b></td><td>0.01 <b>(+69.37%)</b></td><td>1967.50 <b>(+219.19%)</b></td><td>730.16 <b>(+70.01%)</b></td><td>527.90 <b>(+41.95%)</b></td><td>254.80 (-14.64%)</td><td>706.29 <b>(+384.41%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.40 (n/a)</td><td>429.48 (n/a)</td><td>371.90 (n/a)</td><td>298.50 (n/a)</td><td>145.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-7.77%)</td><td>0.02 (-2.01%)</td><td>0.03 (-5.46%)</td><td>0.02 (-1.59%)</td><td>0.01 (-13.44%)</td><td>528.60 (+1.61%)</td><td>367.72 (-0.17%)</td><td>311.60 (+5.77%)</td><td>252.40 (+8.42%)</td><td>121.92 (-9.92%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.20 (n/a)</td><td>368.34 (n/a)</td><td>294.60 (n/a)</td><td>232.80 (n/a)</td><td>135.34 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-11.26%)</td><td>0.02 (-17.38%)</td><td>0.02 <b>(-25.92%)</b></td><td>0.01 (-13.63%)</td><td>0.01 (-11.83%)</td><td>559.70 (+15.78%)</td><td>414.16 <b>(+21.38%)</b></td><td>409.80 <b>(+34.98%)</b></td><td>267.30 (+12.69%)</td><td>133.87 (+17.80%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>483.40 (n/a)</td><td>341.20 (n/a)</td><td>303.60 (n/a)</td><td>237.20 (n/a)</td><td>113.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-5.51%)</td><td>0.02 (-6.35%)</td><td>0.03 (+4.20%)</td><td>0.02 (-9.45%)</td><td>0.01 (-6.06%)</td><td>526.00 (+10.43%)</td><td>381.24 (+7.24%)</td><td>319.10 (-4.03%)</td><td>257.00 (+5.80%)</td><td>123.35 (+12.75%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.30 (n/a)</td><td>355.50 (n/a)</td><td>332.50 (n/a)</td><td>242.90 (n/a)</td><td>109.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 <b>(+87.51%)</b></td><td>0.03 <b>(+49.00%)</b></td><td>0.03 <b>(+50.26%)</b></td><td>0.02 (+16.85%)</td><td>0.01 <b>(+170.96%)</b></td><td>478.30 (-14.42%)</td><td>330.08 <b>(-27.24%)</b></td><td>289.80 <b>(-33.44%)</b></td><td>181.10 <b>(-46.67%)</b></td><td>121.56 <b>(+22.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.90 (n/a)</td><td>453.64 (n/a)</td><td>435.40 (n/a)</td><td>339.60 (n/a)</td><td>98.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-6.20%)</td><td>0.02 <b>(+23.50%)</b></td><td>0.03 <b>(+47.49%)</b></td><td>0.02 <b>(+21.03%)</b></td><td>0.01 <b>(-22.57%)</b></td><td>497.80 (-17.38%)</td><td>351.32 <b>(-21.78%)</b></td><td>301.40 <b>(-32.19%)</b></td><td>274.10 (+6.61%)</td><td>92.26 <b>(-28.04%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.50 (n/a)</td><td>449.16 (n/a)</td><td>444.50 (n/a)</td><td>257.10 (n/a)</td><td>128.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 <b>(+25.74%)</b></td><td>0.03 (+1.63%)</td><td>0.02 (-12.93%)</td><td>0.01 (-6.48%)</td><td>0.01 <b>(+56.30%)</b></td><td>563.00 (+6.93%)</td><td>355.20 (+3.52%)</td><td>344.50 (+14.83%)</td><td>209.10 <b>(-20.49%)</b></td><td>134.43 <b>(+27.13%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.50 (n/a)</td><td>343.12 (n/a)</td><td>300.00 (n/a)</td><td>263.00 (n/a)</td><td>105.74 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 <b>(-35.91%)</b></td><td>0.02 <b>(-42.90%)</b></td><td>0.01 <b>(-52.26%)</b></td><td>0.01 <b>(-52.11%)</b></td><td>0.01 <b>(-28.76%)</b></td><td>1065.60 <b>(+108.82%)</b></td><td>594.72 <b>(+87.72%)</b></td><td>581.20 <b>(+109.44%)</b></td><td>252.50 <b>(+56.06%)</b></td><td>297.85 <b>(+127.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.30 (n/a)</td><td>316.82 (n/a)</td><td>277.50 (n/a)</td><td>161.80 (n/a)</td><td>130.74 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 <b>(+32.50%)</b></td><td>0.02 (+18.84%)</td><td>0.02 (+10.90%)</td><td>0.00 <b>(+28.64%)</b></td><td>0.01 <b>(+28.75%)</b></td><td>1861.30 <b>(-22.26%)</b></td><td>659.64 (-18.33%)</td><td>424.10 (-9.82%)</td><td>228.90 <b>(-24.53%)</b></td><td>679.10 <b>(-23.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2394.30 (n/a)</td><td>807.70 (n/a)</td><td>470.30 (n/a)</td><td>303.30 (n/a)</td><td>891.58 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-18.91%)</td><td>0.02 (-15.38%)</td><td>0.02 <b>(-27.04%)</b></td><td>0.00 (+7.94%)</td><td>0.01 <b>(-21.40%)</b></td><td>2275.70 (-7.35%)</td><td>800.56 (+1.56%)</td><td>501.40 <b>(+37.07%)</b></td><td>313.30 <b>(+23.30%)</b></td><td>831.63 (-11.53%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2456.30 (n/a)</td><td>788.28 (n/a)</td><td>365.80 (n/a)</td><td>254.10 (n/a)</td><td>939.99 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-0.14%)</td><td>0.02 (+14.88%)</td><td>0.02 (+14.25%)</td><td>0.01 (+10.69%)</td><td>0.01 (+1.92%)</td><td>594.70 (-9.66%)</td><td>437.68 (-12.91%)</td><td>467.50 (-12.49%)</td><td>266.20 (+0.15%)</td><td>145.05 (-2.65%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.30 (n/a)</td><td>502.58 (n/a)</td><td>534.20 (n/a)</td><td>265.80 (n/a)</td><td>149.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 <b>(+49.68%)</b></td><td>0.03 <b>(+37.45%)</b></td><td>0.03 <b>(+65.63%)</b></td><td>0.01 (-10.48%)</td><td>0.01 <b>(+152.22%)</b></td><td>618.20 (+11.71%)</td><td>367.32 <b>(-20.38%)</b></td><td>292.30 <b>(-39.63%)</b></td><td>244.00 <b>(-33.19%)</b></td><td>154.76 <b>(+92.16%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.40 (n/a)</td><td>461.34 (n/a)</td><td>484.20 (n/a)</td><td>365.20 (n/a)</td><td>80.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (-4.13%)</td><td>0.02 (+9.20%)</td><td>0.02 (+5.05%)</td><td>0.01 <b>(+28.47%)</b></td><td>0.00 <b>(-25.20%)</b></td><td>806.20 <b>(-22.17%)</b></td><td>543.84 (-15.69%)</td><td>536.40 (-4.81%)</td><td>347.90 (+4.32%)</td><td>168.87 <b>(-39.92%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1035.80 (n/a)</td><td>645.08 (n/a)</td><td>563.50 (n/a)</td><td>333.50 (n/a)</td><td>281.06 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (-12.59%)</td><td>0.05 (+11.25%)</td><td>0.05 <b>(+41.64%)</b></td><td>0.04 (+18.48%)</td><td>0.01 <b>(-49.19%)</b></td><td>435.90 (-15.59%)</td><td>344.40 (-16.50%)</td><td>339.50 <b>(-29.40%)</b></td><td>269.70 (+14.43%)</td><td>61.02 <b>(-52.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>516.40 (n/a)</td><td>412.44 (n/a)</td><td>480.90 (n/a)</td><td>235.70 (n/a)</td><td>128.82 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (+11.16%)</td><td>0.05 (+1.00%)</td><td>0.05 (-6.59%)</td><td>0.03 <b>(+40.89%)</b></td><td>0.01 (-16.75%)</td><td>512.50 <b>(-29.03%)</b></td><td>374.46 (-8.42%)</td><td>362.80 (+7.05%)</td><td>233.60 (-10.05%)</td><td>100.05 <b>(-47.81%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>722.10 (n/a)</td><td>408.90 (n/a)</td><td>338.90 (n/a)</td><td>259.70 (n/a)</td><td>191.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (+4.01%)</td><td>0.04 (-12.17%)</td><td>0.03 (-6.54%)</td><td>0.01 <b>(-68.90%)</b></td><td>0.03 <b>(+50.05%)</b></td><td>1887.80 <b>(+221.60%)</b></td><td>776.50 <b>(+78.06%)</b></td><td>537.80 (+7.00%)</td><td>220.10 (-3.89%)</td><td>681.03 <b>(+364.03%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>587.00 (n/a)</td><td>436.08 (n/a)</td><td>502.60 (n/a)</td><td>229.00 (n/a)</td><td>146.76 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (-17.77%)</td><td>0.04 (-17.72%)</td><td>0.04 <b>(-23.44%)</b></td><td>0.01 <b>(-46.85%)</b></td><td>0.02 (-6.95%)</td><td>2094.70 <b>(+88.15%)</b></td><td>720.30 <b>(+52.70%)</b></td><td>401.40 <b>(+30.62%)</b></td><td>248.20 <b>(+21.61%)</b></td><td>778.90 <b>(+109.72%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1113.30 (n/a)</td><td>471.70 (n/a)</td><td>307.30 (n/a)</td><td>204.10 (n/a)</td><td>371.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (+9.69%)</td><td>0.04 (+12.17%)</td><td>0.04 (+18.78%)</td><td>0.02 <b>(-22.64%)</b></td><td>0.02 <b>(+68.08%)</b></td><td>765.80 <b>(+29.27%)</b></td><td>444.34 (-0.87%)</td><td>380.90 (-15.82%)</td><td>269.10 (-8.84%)</td><td>208.59 <b>(+96.24%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>592.40 (n/a)</td><td>448.22 (n/a)</td><td>452.50 (n/a)</td><td>295.20 (n/a)</td><td>106.29 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (-13.61%)</td><td>0.04 <b>(-33.36%)</b></td><td>0.04 <b>(-37.14%)</b></td><td>0.01 <b>(-71.27%)</b></td><td>0.02 <b>(+33.19%)</b></td><td>1784.60 <b>(+248.08%)</b></td><td>697.78 <b>(+109.62%)</b></td><td>433.20 <b>(+59.09%)</b></td><td>293.30 (+15.75%)</td><td>620.52 <b>(+471.68%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>512.70 (n/a)</td><td>332.88 (n/a)</td><td>272.30 (n/a)</td><td>253.40 (n/a)</td><td>108.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (-16.13%)</td><td>0.03 <b>(-40.85%)</b></td><td>0.03 <b>(-46.87%)</b></td><td>0.01 <b>(-70.59%)</b></td><td>0.02 (+6.77%)</td><td>1943.90 <b>(+240.02%)</b></td><td>792.10 <b>(+126.11%)</b></td><td>603.60 <b>(+88.21%)</b></td><td>275.70 (+19.25%)</td><td>660.13 <b>(+378.25%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>571.70 (n/a)</td><td>350.32 (n/a)</td><td>320.70 (n/a)</td><td>231.20 (n/a)</td><td>138.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 <b>(+74.53%)</b></td><td>0.05 <b>(+69.93%)</b></td><td>0.05 <b>(+74.73%)</b></td><td>0.03 <b>(+74.11%)</b></td><td>0.01 <b>(+73.68%)</b></td><td>635.50 <b>(-42.56%)</b></td><td>376.28 <b>(-41.27%)</b></td><td>308.40 <b>(-42.76%)</b></td><td>261.60 <b>(-42.71%)</b></td><td>150.45 <b>(-43.31%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1106.40 (n/a)</td><td>640.68 (n/a)</td><td>538.80 (n/a)</td><td>456.60 (n/a)</td><td>265.38 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (-12.57%)</td><td>0.04 (-7.06%)</td><td>0.04 (+3.26%)</td><td>0.03 (+11.78%)</td><td>0.01 <b>(-47.01%)</b></td><td>554.60 (-10.53%)</td><td>440.12 (-0.04%)</td><td>459.00 (-3.14%)</td><td>320.10 (+14.36%)</td><td>86.31 <b>(-43.40%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>619.90 (n/a)</td><td>440.30 (n/a)</td><td>473.90 (n/a)</td><td>279.90 (n/a)</td><td>152.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 <b>(-42.20%)</b></td><td>0.04 (-3.34%)</td><td>0.04 (+1.36%)</td><td>0.03 <b>(+275.77%)</b></td><td>0.01 <b>(-73.22%)</b></td><td>512.90 <b>(-73.39%)</b></td><td>435.28 <b>(-37.91%)</b></td><td>455.30 (-1.32%)</td><td>333.50 <b>(+72.98%)</b></td><td>78.29 <b>(-88.74%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1927.20 (n/a)</td><td>701.02 (n/a)</td><td>461.40 (n/a)</td><td>192.80 (n/a)</td><td>695.57 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (+5.69%)</td><td>0.04 (+2.43%)</td><td>0.03 (-4.56%)</td><td>0.03 (+0.24%)</td><td>0.01 (+18.54%)</td><td>623.90 (-0.22%)</td><td>478.96 (-0.77%)</td><td>540.70 (+4.77%)</td><td>321.80 (-5.38%)</td><td>132.02 (+11.47%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>625.30 (n/a)</td><td>482.68 (n/a)</td><td>516.10 (n/a)</td><td>340.10 (n/a)</td><td>118.44 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 <b>(+58.61%)</b></td><td>0.05 <b>(+61.06%)</b></td><td>0.05 <b>(+61.86%)</b></td><td>0.03 <b>(+46.83%)</b></td><td>0.01 <b>(+78.25%)</b></td><td>476.70 <b>(-31.89%)</b></td><td>320.02 <b>(-36.77%)</b></td><td>305.70 <b>(-38.22%)</b></td><td>221.20 <b>(-36.94%)</b></td><td>97.70 <b>(-22.18%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>699.90 (n/a)</td><td>506.10 (n/a)</td><td>494.80 (n/a)</td><td>350.80 (n/a)</td><td>125.55 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (-16.99%)</td><td>0.10 <b>(+28.06%)</b></td><td>0.12 <b>(+63.29%)</b></td><td>0.07 <b>(+25.48%)</b></td><td>0.02 <b>(-37.35%)</b></td><td>500.40 <b>(-20.32%)</b></td><td>328.62 <b>(-26.94%)</b></td><td>284.10 <b>(-38.75%)</b></td><td>276.70 <b>(+20.46%)</b></td><td>96.51 <b>(-35.53%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>628.00 (n/a)</td><td>449.80 (n/a)</td><td>463.80 (n/a)</td><td>229.70 (n/a)</td><td>149.70 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 <b>(-26.08%)</b></td><td>0.07 <b>(-38.38%)</b></td><td>0.06 <b>(-48.52%)</b></td><td>0.02 <b>(-79.05%)</b></td><td>0.04 (+17.45%)</td><td>2066.30 <b>(+377.32%)</b></td><td>765.60 <b>(+149.89%)</b></td><td>592.30 <b>(+94.26%)</b></td><td>265.90 <b>(+35.25%)</b></td><td>744.09 <b>(+671.35%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>432.90 (n/a)</td><td>306.38 (n/a)</td><td>304.90 (n/a)</td><td>196.60 (n/a)</td><td>96.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (-14.81%)</td><td>0.09 (-5.72%)</td><td>0.10 (-11.70%)</td><td>0.06 (+5.47%)</td><td>0.02 <b>(-33.97%)</b></td><td>548.10 (-5.19%)</td><td>384.90 (-1.60%)</td><td>319.10 (+13.24%)</td><td>294.40 (+17.38%)</td><td>115.48 <b>(-31.88%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>578.10 (n/a)</td><td>391.14 (n/a)</td><td>281.80 (n/a)</td><td>250.80 (n/a)</td><td>169.53 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (-11.20%)</td><td>0.07 (-17.44%)</td><td>0.08 (+6.25%)</td><td>0.02 <b>(-71.30%)</b></td><td>0.03 (+18.87%)</td><td>1933.40 <b>(+248.49%)</b></td><td>703.74 <b>(+71.18%)</b></td><td>398.40 (-5.88%)</td><td>298.60 (+12.64%)</td><td>691.05 <b>(+433.75%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>554.80 (n/a)</td><td>411.10 (n/a)</td><td>423.30 (n/a)</td><td>265.10 (n/a)</td><td>129.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (-12.96%)</td><td>0.09 (-14.53%)</td><td>0.06 <b>(-21.83%)</b></td><td>0.05 <b>(-21.76%)</b></td><td>0.04 (-1.28%)</td><td>602.80 <b>(+27.82%)</b></td><td>445.86 <b>(+22.73%)</b></td><td>520.40 <b>(+27.93%)</b></td><td>224.20 (+14.92%)</td><td>171.54 <b>(+50.08%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>471.60 (n/a)</td><td>363.28 (n/a)</td><td>406.80 (n/a)</td><td>195.10 (n/a)</td><td>114.30 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 <b>(+28.68%)</b></td><td>0.10 (+7.89%)</td><td>0.10 (-4.40%)</td><td>0.07 (+6.38%)</td><td>0.03 <b>(+22.13%)</b></td><td>459.00 (-6.00%)</td><td>339.74 (-6.95%)</td><td>316.50 (+4.63%)</td><td>215.90 <b>(-22.28%)</b></td><td>96.29 (-10.86%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>488.30 (n/a)</td><td>365.12 (n/a)</td><td>302.50 (n/a)</td><td>277.80 (n/a)</td><td>108.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (+19.94%)</td><td>0.10 (+16.44%)</td><td>0.09 <b>(+29.12%)</b></td><td>0.07 <b>(+24.48%)</b></td><td>0.03 (+11.84%)</td><td>475.20 (-19.68%)</td><td>365.12 (-14.62%)</td><td>352.90 <b>(-22.54%)</b></td><td>241.80 (-16.62%)</td><td>106.69 (-17.61%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>591.60 (n/a)</td><td>427.66 (n/a)</td><td>455.60 (n/a)</td><td>290.00 (n/a)</td><td>129.49 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.16 (+2.96%)</td><td>0.09 (-2.41%)</td><td>0.08 <b>(+23.11%)</b></td><td>0.06 (+4.38%)</td><td>0.04 (-16.60%)</td><td>584.30 (-4.20%)</td><td>401.34 (-4.17%)</td><td>408.30 (-18.78%)</td><td>208.50 (-2.89%)</td><td>139.23 <b>(-22.70%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>609.90 (n/a)</td><td>418.82 (n/a)</td><td>502.70 (n/a)</td><td>214.70 (n/a)</td><td>180.12 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.17 <b>(+111.96%)</b></td><td>0.11 <b>(+47.12%)</b></td><td>0.10 <b>(+39.31%)</b></td><td>0.06 (-1.50%)</td><td>0.05 <b>(+402.72%)</b></td><td>560.60 (+1.52%)</td><td>369.96 <b>(-20.57%)</b></td><td>313.90 <b>(-28.22%)</b></td><td>188.50 <b>(-52.83%)</b></td><td>165.60 <b>(+155.55%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>552.20 (n/a)</td><td>465.78 (n/a)</td><td>437.30 (n/a)</td><td>399.60 (n/a)</td><td>64.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (-7.54%)</td><td>0.09 (+2.23%)</td><td>0.09 <b>(+29.37%)</b></td><td>0.04 <b>(-34.43%)</b></td><td>0.04 <b>(+24.62%)</b></td><td>800.00 <b>(+52.53%)</b></td><td>487.18 (+13.44%)</td><td>357.70 <b>(-22.69%)</b></td><td>246.80 (+8.15%)</td><td>268.46 <b>(+130.09%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>524.50 (n/a)</td><td>429.46 (n/a)</td><td>462.70 (n/a)</td><td>228.20 (n/a)</td><td>116.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.16 <b>(+37.31%)</b></td><td>0.09 <b>(+21.38%)</b></td><td>0.06 (-2.57%)</td><td>0.05 (-7.78%)</td><td>0.05 <b>(+96.25%)</b></td><td>646.30 (+8.44%)</td><td>445.46 (-4.07%)</td><td>538.90 (+2.63%)</td><td>198.80 <b>(-27.18%)</b></td><td>207.77 <b>(+58.08%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>596.00 (n/a)</td><td>464.38 (n/a)</td><td>525.10 (n/a)</td><td>273.00 (n/a)</td><td>131.43 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (-15.05%)</td><td>0.07 (-13.88%)</td><td>0.06 (-14.62%)</td><td>0.03 <b>(-32.73%)</b></td><td>0.03 (-3.44%)</td><td>945.40 <b>(+48.67%)</b></td><td>558.08 <b>(+23.21%)</b></td><td>539.10 (+17.12%)</td><td>293.00 (+17.72%)</td><td>253.97 <b>(+72.26%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>635.90 (n/a)</td><td>452.96 (n/a)</td><td>460.30 (n/a)</td><td>248.90 (n/a)</td><td>147.43 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (-9.15%)</td><td>0.01 (-14.59%)</td><td>0.01 (-19.20%)</td><td>0.01 (-8.54%)</td><td>0.00 (+5.79%)</td><td>547.30 (+9.35%)</td><td>395.86 <b>(+20.18%)</b></td><td>370.40 <b>(+23.80%)</b></td><td>259.90 (+10.08%)</td><td>137.37 <b>(+28.47%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.50 (n/a)</td><td>329.40 (n/a)</td><td>299.20 (n/a)</td><td>236.10 (n/a)</td><td>106.92 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (+3.58%)</td><td>0.02 <b>(+34.18%)</b></td><td>0.02 <b>(+86.22%)</b></td><td>0.01 <b>(+98.87%)</b></td><td>0.01 <b>(-32.55%)</b></td><td>547.40 <b>(-49.72%)</b></td><td>334.82 <b>(-39.28%)</b></td><td>293.50 <b>(-46.29%)</b></td><td>237.40 (-3.46%)</td><td>124.10 <b>(-63.44%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1088.70 (n/a)</td><td>551.42 (n/a)</td><td>546.50 (n/a)</td><td>245.90 (n/a)</td><td>339.45 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(+33.91%)</b></td><td>0.01 <b>(+22.76%)</b></td><td>0.01 (-5.16%)</td><td>0.01 (+2.14%)</td><td>0.01 <b>(+74.27%)</b></td><td>619.10 (-2.10%)</td><td>430.90 (-9.43%)</td><td>525.00 (+5.42%)</td><td>200.50 <b>(-25.33%)</b></td><td>184.39 <b>(+32.96%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>632.40 (n/a)</td><td>475.76 (n/a)</td><td>498.00 (n/a)</td><td>268.50 (n/a)</td><td>138.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(+37.30%)</b></td><td>0.01 <b>(+49.60%)</b></td><td>0.01 <b>(+25.93%)</b></td><td>0.01 <b>(+277.86%)</b></td><td>0.01 (+10.14%)</td><td>544.10 <b>(-73.53%)</b></td><td>392.14 <b>(-50.28%)</b></td><td>420.20 <b>(-20.60%)</b></td><td>227.50 <b>(-27.18%)</b></td><td>133.01 <b>(-81.43%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2055.90 (n/a)</td><td>788.64 (n/a)</td><td>529.20 (n/a)</td><td>312.40 (n/a)</td><td>716.33 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(+27.66%)</b></td><td>0.01 (+19.23%)</td><td>0.01 (+5.23%)</td><td>0.01 (+18.74%)</td><td>0.01 <b>(+52.73%)</b></td><td>628.50 (-15.78%)</td><td>449.12 (-10.11%)</td><td>503.70 (-4.98%)</td><td>214.00 <b>(-21.67%)</b></td><td>186.74 (+7.50%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>746.30 (n/a)</td><td>499.66 (n/a)</td><td>530.10 (n/a)</td><td>273.20 (n/a)</td><td>173.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(+98.10%)</b></td><td>0.02 <b>(+63.43%)</b></td><td>0.02 <b>(+108.32%)</b></td><td>0.01 (-4.84%)</td><td>0.01 <b>(+464.23%)</b></td><td>641.60 (+5.09%)</td><td>387.22 <b>(-29.11%)</b></td><td>275.20 <b>(-52.00%)</b></td><td>239.30 <b>(-49.53%)</b></td><td>181.43 <b>(+200.63%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.50 (n/a)</td><td>546.20 (n/a)</td><td>573.30 (n/a)</td><td>474.10 (n/a)</td><td>60.35 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 <b>(-36.76%)</b></td><td>0.01 <b>(-35.26%)</b></td><td>0.01 <b>(-23.84%)</b></td><td>0.00 <b>(-71.59%)</b></td><td>0.00 (+3.96%)</td><td>2103.30 <b>(+252.02%)</b></td><td>888.20 <b>(+98.72%)</b></td><td>578.60 <b>(+31.32%)</b></td><td>457.20 <b>(+58.09%)</b></td><td>693.24 <b>(+518.40%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>597.50 (n/a)</td><td>446.96 (n/a)</td><td>440.60 (n/a)</td><td>289.20 (n/a)</td><td>112.10 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (+8.12%)</td><td>0.01 (-7.06%)</td><td>0.02 (-0.91%)</td><td>0.01 (-16.23%)</td><td>0.00 <b>(+58.15%)</b></td><td>530.20 (+19.39%)</td><td>365.44 (+14.64%)</td><td>284.30 (+0.89%)</td><td>243.90 (-7.51%)</td><td>133.25 <b>(+78.96%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>444.10 (n/a)</td><td>318.76 (n/a)</td><td>281.80 (n/a)</td><td>263.70 (n/a)</td><td>74.46 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (+3.39%)</td><td>0.01 (-13.99%)</td><td>0.01 (-19.39%)</td><td>0.01 (-14.42%)</td><td>0.00 (-2.39%)</td><td>599.90 (+16.85%)</td><td>440.72 (+16.22%)</td><td>437.80 <b>(+24.06%)</b></td><td>260.10 (-3.27%)</td><td>121.37 (+4.79%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.40 (n/a)</td><td>379.22 (n/a)</td><td>352.90 (n/a)</td><td>268.90 (n/a)</td><td>115.82 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(+56.86%)</b></td><td>0.01 <b>(+77.68%)</b></td><td>0.02 <b>(+95.29%)</b></td><td>0.01 <b>(+372.77%)</b></td><td>0.01 <b>(+25.78%)</b></td><td>518.10 <b>(-78.85%)</b></td><td>349.92 <b>(-60.31%)</b></td><td>293.20 <b>(-48.80%)</b></td><td>201.40 <b>(-36.27%)</b></td><td>135.24 <b>(-84.68%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2449.40 (n/a)</td><td>881.66 (n/a)</td><td>572.70 (n/a)</td><td>316.00 (n/a)</td><td>882.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(+50.12%)</b></td><td>0.01 <b>(+25.05%)</b></td><td>0.01 (+12.86%)</td><td>0.01 <b>(+97.36%)</b></td><td>0.00 <b>(+29.34%)</b></td><td>562.20 <b>(-49.33%)</b></td><td>453.06 <b>(-24.85%)</b></td><td>495.20 (-11.40%)</td><td>248.10 <b>(-33.40%)</b></td><td>127.47 <b>(-57.34%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1109.50 (n/a)</td><td>602.86 (n/a)</td><td>558.90 (n/a)</td><td>372.50 (n/a)</td><td>298.82 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-14.54%)</td><td>0.02 (-11.41%)</td><td>0.02 <b>(-20.77%)</b></td><td>0.02 (+7.58%)</td><td>0.01 (-17.37%)</td><td>509.40 (-7.04%)</td><td>371.42 (+9.93%)</td><td>358.50 <b>(+26.23%)</b></td><td>234.10 (+17.05%)</td><td>121.92 (-10.22%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.00 (n/a)</td><td>337.86 (n/a)</td><td>284.00 (n/a)</td><td>200.00 (n/a)</td><td>135.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (+9.94%)</td><td>0.04 (+6.70%)</td><td>0.05 (+17.58%)</td><td>0.02 (-9.74%)</td><td>0.01 <b>(+24.16%)</b></td><td>550.10 (+10.80%)</td><td>334.40 (-2.82%)</td><td>254.30 (-14.98%)</td><td>235.60 (-9.03%)</td><td>133.29 <b>(+27.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.50 (n/a)</td><td>344.10 (n/a)</td><td>299.10 (n/a)</td><td>259.00 (n/a)</td><td>104.43 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-7.42%)</td><td>0.02 <b>(-25.30%)</b></td><td>0.02 <b>(-35.81%)</b></td><td>0.00 <b>(-80.57%)</b></td><td>0.01 <b>(+65.29%)</b></td><td>2470.30 <b>(+414.75%)</b></td><td>839.22 <b>(+136.37%)</b></td><td>528.90 <b>(+55.79%)</b></td><td>247.30 (+8.04%)</td><td>926.47 <b>(+866.76%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.90 (n/a)</td><td>355.04 (n/a)</td><td>339.50 (n/a)</td><td>228.90 (n/a)</td><td>95.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (-3.31%)</td><td>0.03 (+1.63%)</td><td>0.04 (+8.09%)</td><td>0.02 (+4.85%)</td><td>0.02 (+4.26%)</td><td>598.60 (-4.64%)</td><td>369.34 (+0.55%)</td><td>250.80 (-7.49%)</td><td>202.30 (+3.43%)</td><td>189.63 (+5.58%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>627.70 (n/a)</td><td>367.32 (n/a)</td><td>271.10 (n/a)</td><td>195.60 (n/a)</td><td>179.61 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (+3.81%)</td><td>0.03 <b>(+22.93%)</b></td><td>0.03 <b>(+47.29%)</b></td><td>0.01 (+0.68%)</td><td>0.01 (-2.73%)</td><td>564.20 (-0.67%)</td><td>334.00 (-19.01%)</td><td>290.20 <b>(-32.10%)</b></td><td>244.80 (-3.66%)</td><td>131.47 (-2.33%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.00 (n/a)</td><td>412.42 (n/a)</td><td>427.40 (n/a)</td><td>254.10 (n/a)</td><td>134.60 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (+18.30%)</td><td>0.03 (+12.15%)</td><td>0.04 (+13.66%)</td><td>0.02 (+13.23%)</td><td>0.01 (+16.85%)</td><td>554.90 (-11.68%)</td><td>353.40 (-9.96%)</td><td>250.00 (-12.00%)</td><td>223.70 (-15.46%)</td><td>156.91 (-7.98%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>628.30 (n/a)</td><td>392.50 (n/a)</td><td>284.10 (n/a)</td><td>264.60 (n/a)</td><td>170.51 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(-54.27%)</b></td><td>0.02 <b>(-32.51%)</b></td><td>0.02 (-3.84%)</td><td>0.01 <b>(-40.45%)</b></td><td>0.00 <b>(-62.68%)</b></td><td>1045.40 <b>(+67.91%)</b></td><td>578.58 <b>(+37.09%)</b></td><td>477.80 (+4.01%)</td><td>424.00 <b>(+118.67%)</b></td><td>262.03 <b>(+45.63%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.60 (n/a)</td><td>422.04 (n/a)</td><td>459.40 (n/a)</td><td>193.90 (n/a)</td><td>179.93 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 <b>(-21.07%)</b></td><td>0.02 (-12.32%)</td><td>0.02 <b>(-34.22%)</b></td><td>0.02 <b>(+24.60%)</b></td><td>0.01 <b>(-27.52%)</b></td><td>535.80 (-19.74%)</td><td>411.38 (+5.63%)</td><td>447.90 <b>(+52.04%)</b></td><td>265.90 <b>(+26.68%)</b></td><td>133.27 <b>(-29.25%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>667.60 (n/a)</td><td>389.44 (n/a)</td><td>294.60 (n/a)</td><td>209.90 (n/a)</td><td>188.36 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 <b>(-31.08%)</b></td><td>0.02 (-15.28%)</td><td>0.02 (-15.42%)</td><td>0.02 (+1.49%)</td><td>0.01 <b>(-48.12%)</b></td><td>523.20 (-1.47%)</td><td>390.02 (+9.54%)</td><td>367.80 (+18.26%)</td><td>291.10 <b>(+45.11%)</b></td><td>97.94 <b>(-28.54%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.00 (n/a)</td><td>356.04 (n/a)</td><td>311.00 (n/a)</td><td>200.60 (n/a)</td><td>137.06 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 <b>(-43.06%)</b></td><td>0.02 <b>(-33.54%)</b></td><td>0.02 <b>(-43.56%)</b></td><td>0.01 (+0.93%)</td><td>0.00 <b>(-74.00%)</b></td><td>616.70 (-0.93%)</td><td>522.60 <b>(+29.89%)</b></td><td>521.90 <b>(+77.16%)</b></td><td>403.80 <b>(+75.64%)</b></td><td>77.02 <b>(-58.93%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.50 (n/a)</td><td>402.34 (n/a)</td><td>294.60 (n/a)</td><td>229.90 (n/a)</td><td>187.55 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (-17.99%)</td><td>0.02 <b>(-26.23%)</b></td><td>0.01 (-11.67%)</td><td>0.00 <b>(-71.12%)</b></td><td>0.01 (+14.83%)</td><td>1807.20 <b>(+246.27%)</b></td><td>754.66 <b>(+75.36%)</b></td><td>548.20 (+13.22%)</td><td>322.70 <b>(+21.96%)</b></td><td>597.65 <b>(+438.56%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.90 (n/a)</td><td>430.36 (n/a)</td><td>484.20 (n/a)</td><td>264.60 (n/a)</td><td>110.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (+4.14%)</td><td>0.04 (-0.37%)</td><td>0.03 (-13.71%)</td><td>0.03 (+10.25%)</td><td>0.02 (+2.66%)</td><td>599.10 (-9.30%)</td><td>421.78 (-0.37%)</td><td>475.20 (+15.87%)</td><td>240.90 (-3.99%)</td><td>155.87 (-9.59%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>660.50 (n/a)</td><td>423.34 (n/a)</td><td>410.10 (n/a)</td><td>250.90 (n/a)</td><td>172.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (+0.13%)</td><td>0.07 (+7.95%)</td><td>0.08 <b>(+53.89%)</b></td><td>0.04 (-17.14%)</td><td>0.02 <b>(+27.15%)</b></td><td>620.70 <b>(+20.66%)</b></td><td>413.22 (-1.77%)</td><td>316.20 <b>(-35.01%)</b></td><td>274.30 (-0.11%)</td><td>171.48 <b>(+48.84%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>514.40 (n/a)</td><td>420.66 (n/a)</td><td>486.50 (n/a)</td><td>274.60 (n/a)</td><td>115.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (-13.28%)</td><td>0.03 <b>(-20.47%)</b></td><td>0.03 (-10.93%)</td><td>0.01 <b>(-70.95%)</b></td><td>0.01 <b>(+74.08%)</b></td><td>2093.00 <b>(+244.19%)</b></td><td>874.36 <b>(+71.43%)</b></td><td>590.20 (+12.27%)</td><td>407.80 (+15.30%)</td><td>701.51 <b>(+645.02%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>608.10 (n/a)</td><td>510.04 (n/a)</td><td>525.70 (n/a)</td><td>353.70 (n/a)</td><td>94.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 <b>(-43.06%)</b></td><td>0.04 <b>(-31.24%)</b></td><td>0.04 <b>(-32.70%)</b></td><td>0.03 (-18.17%)</td><td>0.01 <b>(-63.39%)</b></td><td>696.50 <b>(+22.19%)</b></td><td>527.96 <b>(+37.53%)</b></td><td>484.60 <b>(+48.60%)</b></td><td>461.90 <b>(+75.63%)</b></td><td>98.53 <b>(-22.20%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>570.00 (n/a)</td><td>383.88 (n/a)</td><td>326.10 (n/a)</td><td>263.00 (n/a)</td><td>126.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 <b>(+24.23%)</b></td><td>0.03 (-12.45%)</td><td>0.04 (+2.99%)</td><td>0.01 <b>(-68.82%)</b></td><td>0.02 <b>(+132.11%)</b></td><td>1942.20 <b>(+220.65%)</b></td><td>967.74 <b>(+110.04%)</b></td><td>444.50 (-2.91%)</td><td>244.60 (-19.49%)</td><td>844.78 <b>(+600.45%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>605.70 (n/a)</td><td>460.74 (n/a)</td><td>457.80 (n/a)</td><td>303.80 (n/a)</td><td>120.61 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (-5.27%)</td><td>0.05 (-14.02%)</td><td>0.05 <b>(-26.23%)</b></td><td>0.04 (+14.22%)</td><td>0.02 (+1.88%)</td><td>582.10 (-12.45%)</td><td>425.94 (+15.47%)</td><td>409.70 <b>(+35.57%)</b></td><td>257.60 (+5.57%)</td><td>152.63 (-9.45%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>664.90 (n/a)</td><td>368.88 (n/a)</td><td>302.20 (n/a)</td><td>244.00 (n/a)</td><td>168.55 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (-8.32%)</td><td>0.05 (+13.90%)</td><td>0.05 <b>(+42.64%)</b></td><td>0.03 (-3.26%)</td><td>0.01 (-9.51%)</td><td>612.60 (+3.37%)</td><td>384.32 (-11.99%)</td><td>315.50 <b>(-29.90%)</b></td><td>257.10 (+9.08%)</td><td>144.26 (+12.50%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>592.60 (n/a)</td><td>436.66 (n/a)</td><td>450.10 (n/a)</td><td>235.70 (n/a)</td><td>128.23 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (-10.98%)</td><td>0.05 (-7.23%)</td><td>0.04 (+6.88%)</td><td>0.03 (-15.38%)</td><td>0.02 (-16.17%)</td><td>632.50 (+18.18%)</td><td>439.36 (+6.68%)</td><td>436.90 (-6.43%)</td><td>267.90 (+12.33%)</td><td>143.34 (+8.26%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>535.20 (n/a)</td><td>411.86 (n/a)</td><td>466.90 (n/a)</td><td>238.50 (n/a)</td><td>132.41 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 <b>(+42.87%)</b></td><td>0.04 (+10.14%)</td><td>0.04 (+13.56%)</td><td>0.02 <b>(-28.31%)</b></td><td>0.02 <b>(+146.73%)</b></td><td>773.20 <b>(+39.49%)</b></td><td>462.74 (+7.29%)</td><td>397.90 (-11.95%)</td><td>222.50 <b>(-29.99%)</b></td><td>229.41 <b>(+148.98%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>554.30 (n/a)</td><td>431.30 (n/a)</td><td>451.90 (n/a)</td><td>317.80 (n/a)</td><td>92.14 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (+7.30%)</td><td>0.04 (-9.77%)</td><td>0.03 <b>(-32.59%)</b></td><td>0.03 (+8.33%)</td><td>0.01 (-1.60%)</td><td>553.20 (-7.69%)</td><td>456.00 (+9.62%)</td><td>527.10 <b>(+48.35%)</b></td><td>274.00 (-6.80%)</td><td>125.51 (-11.22%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.30 (n/a)</td><td>415.98 (n/a)</td><td>355.30 (n/a)</td><td>294.00 (n/a)</td><td>141.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (-15.44%)</td><td>0.03 (-14.44%)</td><td>0.03 (-16.01%)</td><td>0.02 <b>(-44.07%)</b></td><td>0.01 (+11.44%)</td><td>1029.40 <b>(+78.81%)</b></td><td>617.82 <b>(+25.78%)</b></td><td>619.70 (+19.06%)</td><td>370.70 (+18.28%)</td><td>256.06 <b>(+144.10%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>575.70 (n/a)</td><td>491.18 (n/a)</td><td>520.50 (n/a)</td><td>313.40 (n/a)</td><td>104.90 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 <b>(-24.21%)</b></td><td>0.07 (-6.33%)</td><td>0.06 (-5.73%)</td><td>0.05 (-2.21%)</td><td>0.01 <b>(-40.93%)</b></td><td>692.90 (+2.26%)</td><td>517.78 (+3.54%)</td><td>509.80 (+6.08%)</td><td>419.90 <b>(+31.96%)</b></td><td>108.07 (-17.91%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>677.60 (n/a)</td><td>500.10 (n/a)</td><td>480.60 (n/a)</td><td>318.20 (n/a)</td><td>131.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 <b>(+41.83%)</b></td><td>0.09 <b>(+39.82%)</b></td><td>0.07 (+11.27%)</td><td>0.05 <b>(+39.65%)</b></td><td>0.04 <b>(+68.26%)</b></td><td>604.20 <b>(-28.40%)</b></td><td>416.04 <b>(-25.08%)</b></td><td>495.20 (-10.13%)</td><td>220.50 <b>(-29.51%)</b></td><td>165.32 (-15.99%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>843.80 (n/a)</td><td>555.32 (n/a)</td><td>551.00 (n/a)</td><td>312.80 (n/a)</td><td>196.79 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.17 (+5.75%)</td><td>0.12 <b>(+48.72%)</b></td><td>0.15 <b>(+92.71%)</b></td><td>0.07 <b>(+261.12%)</b></td><td>0.05 (-19.45%)</td><td>578.50 <b>(-72.31%)</b></td><td>377.54 <b>(-56.04%)</b></td><td>269.60 <b>(-48.11%)</b></td><td>247.90 (-5.45%)</td><td>163.82 <b>(-78.54%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2089.10 (n/a)</td><td>858.88 (n/a)</td><td>519.60 (n/a)</td><td>262.20 (n/a)</td><td>763.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (+1.04%)</td><td>0.06 <b>(-44.17%)</b></td><td>0.05 <b>(-52.56%)</b></td><td>0.01 <b>(-77.87%)</b></td><td>0.05 <b>(+65.69%)</b></td><td>2496.50 <b>(+351.94%)</b></td><td>1144.38 <b>(+229.96%)</b></td><td>598.20 <b>(+110.78%)</b></td><td>253.70 (-1.05%)</td><td>999.15 <b>(+708.12%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>552.40 (n/a)</td><td>346.82 (n/a)</td><td>283.80 (n/a)</td><td>256.40 (n/a)</td><td>123.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (-18.92%)</td><td>0.09 <b>(-24.99%)</b></td><td>0.08 <b>(-36.75%)</b></td><td>0.06 (-0.98%)</td><td>0.03 <b>(-42.53%)</b></td><td>686.30 (+1.00%)</td><td>513.38 <b>(+21.41%)</b></td><td>525.10 <b>(+58.12%)</b></td><td>316.20 <b>(+23.32%)</b></td><td>134.34 <b>(-30.81%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>679.50 (n/a)</td><td>422.84 (n/a)</td><td>332.10 (n/a)</td><td>256.40 (n/a)</td><td>194.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 <b>(-38.07%)</b></td><td>0.06 <b>(-24.44%)</b></td><td>0.07 (-7.97%)</td><td>0.03 <b>(-53.23%)</b></td><td>0.02 <b>(-29.50%)</b></td><td>1076.70 <b>(+113.80%)</b></td><td>587.58 <b>(+39.90%)</b></td><td>492.80 (+8.67%)</td><td>403.00 <b>(+61.46%)</b></td><td>276.50 <b>(+173.93%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>503.60 (n/a)</td><td>420.00 (n/a)</td><td>453.50 (n/a)</td><td>249.60 (n/a)</td><td>100.94 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 <b>(-33.21%)</b></td><td>0.07 <b>(-30.11%)</b></td><td>0.07 <b>(-30.59%)</b></td><td>0.06 (-3.46%)</td><td>0.01 <b>(-57.01%)</b></td><td>618.10 (+3.59%)</td><td>518.12 <b>(+36.48%)</b></td><td>496.70 <b>(+44.05%)</b></td><td>434.00 <b>(+49.71%)</b></td><td>81.06 <b>(-35.19%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>596.70 (n/a)</td><td>379.62 (n/a)</td><td>344.80 (n/a)</td><td>289.90 (n/a)</td><td>125.07 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 <b>(+22.91%)</b></td><td>0.12 <b>(+31.08%)</b></td><td>0.13 <b>(+82.07%)</b></td><td>0.06 (-10.59%)</td><td>0.04 <b>(+32.33%)</b></td><td>575.80 (+11.85%)</td><td>315.48 (-19.83%)</td><td>248.40 <b>(-45.08%)</b></td><td>221.50 (-18.66%)</td><td>148.78 <b>(+31.72%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>514.80 (n/a)</td><td>393.50 (n/a)</td><td>452.30 (n/a)</td><td>272.30 (n/a)</td><td>112.95 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (+5.05%)</td><td>0.06 (-11.02%)</td><td>0.06 (-17.68%)</td><td>0.04 <b>(-33.22%)</b></td><td>0.02 <b>(+50.43%)</b></td><td>1041.90 <b>(+49.74%)</b></td><td>677.34 (+18.53%)</td><td>664.50 <b>(+21.46%)</b></td><td>442.60 (-4.80%)</td><td>225.13 <b>(+118.15%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>695.80 (n/a)</td><td>571.44 (n/a)</td><td>547.10 (n/a)</td><td>464.90 (n/a)</td><td>103.20 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (+14.04%)</td><td>0.08 <b>(+21.68%)</b></td><td>0.09 <b>(+63.35%)</b></td><td>0.04 (-11.22%)</td><td>0.03 <b>(+38.64%)</b></td><td>731.00 (+12.63%)</td><td>437.88 (-13.65%)</td><td>347.90 <b>(-38.77%)</b></td><td>307.50 (-12.32%)</td><td>180.86 <b>(+36.01%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>649.00 (n/a)</td><td>507.12 (n/a)</td><td>568.20 (n/a)</td><td>350.70 (n/a)</td><td>132.98 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (+13.83%)</td><td>0.05 (+6.30%)</td><td>0.04 (+1.41%)</td><td>0.03 (-18.10%)</td><td>0.02 <b>(+39.50%)</b></td><td>751.30 <b>(+22.10%)</b></td><td>484.06 (+1.78%)</td><td>509.40 (-1.37%)</td><td>240.60 (-12.16%)</td><td>200.75 <b>(+51.22%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>615.30 (n/a)</td><td>475.58 (n/a)</td><td>516.50 (n/a)</td><td>273.90 (n/a)</td><td>132.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 <b>(+28.62%)</b></td><td>0.06 (+5.88%)</td><td>0.05 (-0.72%)</td><td>0.03 (+1.36%)</td><td>0.03 <b>(+49.74%)</b></td><td>615.10 (-1.35%)</td><td>436.94 (+1.55%)</td><td>451.60 (+0.71%)</td><td>216.10 <b>(-22.27%)</b></td><td>179.51 <b>(+25.37%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>623.50 (n/a)</td><td>430.26 (n/a)</td><td>448.40 (n/a)</td><td>278.00 (n/a)</td><td>143.18 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (+7.32%)</td><td>0.07 (-6.65%)</td><td>0.07 (-6.35%)</td><td>0.04 (-14.16%)</td><td>0.02 <b>(+45.44%)</b></td><td>496.80 (+16.48%)</td><td>339.06 (+11.44%)</td><td>298.70 (+6.79%)</td><td>233.40 (-6.83%)</td><td>107.10 <b>(+52.86%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>426.50 (n/a)</td><td>304.24 (n/a)</td><td>279.70 (n/a)</td><td>250.50 (n/a)</td><td>70.06 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (-12.47%)</td><td>0.05 <b>(-27.36%)</b></td><td>0.04 <b>(-42.76%)</b></td><td>0.03 <b>(-25.35%)</b></td><td>0.03 (-1.93%)</td><td>726.90 <b>(+33.94%)</b></td><td>512.22 <b>(+43.68%)</b></td><td>566.30 <b>(+74.73%)</b></td><td>226.40 (+14.23%)</td><td>192.01 <b>(+40.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>542.70 (n/a)</td><td>356.50 (n/a)</td><td>324.10 (n/a)</td><td>198.20 (n/a)</td><td>136.34 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 <b>(+24.02%)</b></td><td>0.05 <b>(+33.13%)</b></td><td>0.05 <b>(+23.99%)</b></td><td>0.03 <b>(+240.42%)</b></td><td>0.02 (+6.18%)</td><td>613.40 <b>(-70.62%)</b></td><td>435.26 <b>(-44.07%)</b></td><td>412.30 (-19.35%)</td><td>231.90 (-19.37%)</td><td>169.95 <b>(-76.99%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2088.10 (n/a)</td><td>778.20 (n/a)</td><td>511.20 (n/a)</td><td>287.60 (n/a)</td><td>738.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (-16.25%)</td><td>0.04 (-7.62%)</td><td>0.04 <b>(+25.73%)</b></td><td>0.02 <b>(-40.74%)</b></td><td>0.02 (-18.76%)</td><td>1084.10 <b>(+68.76%)</b></td><td>551.52 (+12.62%)</td><td>482.90 <b>(-20.46%)</b></td><td>350.60 (+19.41%)</td><td>305.02 <b>(+71.59%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>642.40 (n/a)</td><td>489.70 (n/a)</td><td>607.10 (n/a)</td><td>293.60 (n/a)</td><td>177.77 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 <b>(+32.55%)</b></td><td>0.07 <b>(+33.88%)</b></td><td>0.06 (+15.86%)</td><td>0.04 (+12.97%)</td><td>0.03 <b>(+50.44%)</b></td><td>564.60 (-11.48%)</td><td>389.54 <b>(-21.84%)</b></td><td>432.90 (-13.70%)</td><td>204.70 <b>(-24.55%)</b></td><td>147.14 (+1.74%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>637.80 (n/a)</td><td>498.38 (n/a)</td><td>501.60 (n/a)</td><td>271.30 (n/a)</td><td>144.62 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.10 (+5.49%)</td><td>0.07 (-17.70%)</td><td>0.06 <b>(-35.43%)</b></td><td>0.04 (-17.20%)</td><td>0.03 <b>(+49.49%)</b></td><td>566.40 <b>(+20.79%)</b></td><td>407.20 <b>(+29.49%)</b></td><td>437.30 <b>(+54.91%)</b></td><td>240.20 (-5.21%)</td><td>142.22 <b>(+61.90%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>468.90 (n/a)</td><td>314.46 (n/a)</td><td>282.30 (n/a)</td><td>253.40 (n/a)</td><td>87.84 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (+17.04%)</td><td>0.08 (-6.37%)</td><td>0.06 <b>(-38.41%)</b></td><td>0.05 (+7.38%)</td><td>0.03 (+17.30%)</td><td>533.80 (-6.86%)</td><td>377.40 (+8.59%)</td><td>406.20 <b>(+62.35%)</b></td><td>197.10 (-14.56%)</td><td>148.86 (-2.50%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>573.10 (n/a)</td><td>347.56 (n/a)</td><td>250.20 (n/a)</td><td>230.70 (n/a)</td><td>152.67 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (+4.45%)</td><td>0.08 (+10.39%)</td><td>0.08 (+7.21%)</td><td>0.04 <b>(+37.90%)</b></td><td>0.03 (+9.12%)</td><td>548.60 <b>(-27.48%)</b></td><td>355.92 (-12.30%)</td><td>316.70 (-6.72%)</td><td>233.90 (-4.26%)</td><td>134.68 <b>(-32.93%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>756.50 (n/a)</td><td>405.84 (n/a)</td><td>339.50 (n/a)</td><td>244.30 (n/a)</td><td>200.81 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (-15.59%)</td><td>0.05 (-1.91%)</td><td>0.05 (+16.04%)</td><td>0.04 (-3.54%)</td><td>0.01 <b>(-31.12%)</b></td><td>621.80 (+3.67%)</td><td>497.18 (+0.58%)</td><td>453.00 (-13.83%)</td><td>431.20 (+18.46%)</td><td>81.16 (-15.23%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>599.80 (n/a)</td><td>494.32 (n/a)</td><td>525.70 (n/a)</td><td>364.00 (n/a)</td><td>95.74 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.10 <b>(+56.95%)</b></td><td>0.06 (+12.88%)</td><td>0.04 (-11.61%)</td><td>0.04 (-6.36%)</td><td>0.02 <b>(+231.06%)</b></td><td>633.30 (+6.78%)</td><td>478.10 (-1.87%)</td><td>546.80 (+13.14%)</td><td>253.40 <b>(-36.30%)</b></td><td>162.14 <b>(+126.68%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>593.10 (n/a)</td><td>487.20 (n/a)</td><td>483.30 (n/a)</td><td>397.80 (n/a)</td><td>71.53 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (-17.89%)</td><td>0.05 (+6.92%)</td><td>0.04 (+11.92%)</td><td>0.03 (+7.02%)</td><td>0.01 <b>(-27.17%)</b></td><td>554.20 (-6.56%)</td><td>420.84 (-10.19%)</td><td>437.70 (-10.66%)</td><td>293.60 <b>(+21.78%)</b></td><td>117.72 (-17.62%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.10 (n/a)</td><td>468.60 (n/a)</td><td>489.90 (n/a)</td><td>241.10 (n/a)</td><td>142.91 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (-6.22%)</td><td>0.06 (+3.06%)</td><td>0.06 (+3.41%)</td><td>0.04 (+3.09%)</td><td>0.01 (-10.74%)</td><td>484.30 (-3.00%)</td><td>331.26 (-3.85%)</td><td>294.30 (-3.29%)</td><td>271.50 (+6.64%)</td><td>88.38 (-8.17%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>499.30 (n/a)</td><td>344.52 (n/a)</td><td>304.30 (n/a)</td><td>254.60 (n/a)</td><td>96.25 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (+14.40%)</td><td>0.06 (+0.39%)</td><td>0.06 (-8.51%)</td><td>0.04 (-0.46%)</td><td>0.02 <b>(+44.99%)</b></td><td>512.30 (+0.47%)</td><td>338.04 (+4.33%)</td><td>294.60 (+9.31%)</td><td>223.80 (-12.58%)</td><td>129.23 <b>(+21.00%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>509.90 (n/a)</td><td>324.02 (n/a)</td><td>269.50 (n/a)</td><td>256.00 (n/a)</td><td>106.81 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (-19.69%)</td><td>0.04 <b>(-34.62%)</b></td><td>0.04 <b>(-44.77%)</b></td><td>0.03 (-17.79%)</td><td>0.01 <b>(-26.54%)</b></td><td>588.20 <b>(+21.63%)</b></td><td>464.02 <b>(+50.59%)</b></td><td>469.90 <b>(+81.08%)</b></td><td>304.70 <b>(+24.52%)</b></td><td>102.96 (+2.95%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>483.60 (n/a)</td><td>308.14 (n/a)</td><td>259.50 (n/a)</td><td>244.70 (n/a)</td><td>100.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (+3.90%)</td><td>0.05 <b>(+24.03%)</b></td><td>0.04 <b>(+32.46%)</b></td><td>0.03 (+9.34%)</td><td>0.02 (-3.90%)</td><td>598.50 (-8.54%)</td><td>399.60 <b>(-21.41%)</b></td><td>427.40 <b>(-24.51%)</b></td><td>205.80 (-3.74%)</td><td>153.02 (-10.52%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>654.40 (n/a)</td><td>508.48 (n/a)</td><td>566.20 (n/a)</td><td>213.80 (n/a)</td><td>171.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 <b>(+21.23%)</b></td><td>0.05 (+16.94%)</td><td>0.05 <b>(+46.69%)</b></td><td>0.03 (-18.37%)</td><td>0.02 <b>(+49.73%)</b></td><td>656.10 <b>(+22.52%)</b></td><td>415.10 (-7.08%)</td><td>338.80 <b>(-31.83%)</b></td><td>216.70 (-17.54%)</td><td>178.80 <b>(+58.16%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>535.50 (n/a)</td><td>446.74 (n/a)</td><td>497.00 (n/a)</td><td>262.80 (n/a)</td><td>113.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.60 <b>(+53.74%)</b></td><td>0.26 (-0.94%)</td><td>0.18 <b>(-29.95%)</b></td><td>0.05 <b>(-64.43%)</b></td><td>0.22 <b>(+120.53%)</b></td><td>1922.30 <b>(+181.16%)</b></td><td>724.24 <b>(+71.93%)</b></td><td>560.30 <b>(+42.75%)</b></td><td>163.60 <b>(-34.95%)</b></td><td>700.55 <b>(+310.55%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.39 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>683.70 (n/a)</td><td>421.24 (n/a)</td><td>392.50 (n/a)</td><td>251.50 (n/a)</td><td>170.63 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.37 <b>(+24.06%)</b></td><td>0.21 (-10.68%)</td><td>0.18 <b>(-30.66%)</b></td><td>0.15 (-8.48%)</td><td>0.09 <b>(+53.46%)</b></td><td>646.40 (+9.28%)</td><td>505.32 (+17.08%)</td><td>539.60 <b>(+44.20%)</b></td><td>267.50 (-19.40%)</td><td>143.98 <b>(+26.94%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>591.50 (n/a)</td><td>431.62 (n/a)</td><td>374.20 (n/a)</td><td>331.90 (n/a)</td><td>113.43 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.26 (-11.86%)</td><td>0.20 (-15.81%)</td><td>0.19 <b>(-28.15%)</b></td><td>0.15 (+7.20%)</td><td>0.05 <b>(-23.75%)</b></td><td>644.40 (-6.73%)</td><td>510.70 (+15.57%)</td><td>519.30 <b>(+39.19%)</b></td><td>376.60 (+13.47%)</td><td>117.65 <b>(-20.63%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>690.90 (n/a)</td><td>441.88 (n/a)</td><td>373.10 (n/a)</td><td>331.90 (n/a)</td><td>148.25 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.29 (+12.86%)</td><td>0.20 (-11.22%)</td><td>0.21 (-12.24%)</td><td>0.11 <b>(-24.88%)</b></td><td>0.08 <b>(+78.97%)</b></td><td>651.30 <b>(+33.14%)</b></td><td>419.98 <b>(+23.87%)</b></td><td>347.00 (+13.92%)</td><td>255.70 (-11.40%)</td><td>175.33 <b>(+107.61%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>489.20 (n/a)</td><td>339.04 (n/a)</td><td>304.60 (n/a)</td><td>288.60 (n/a)</td><td>84.46 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.38 <b>(+43.65%)</b></td><td>0.25 <b>(+27.26%)</b></td><td>0.26 <b>(+47.28%)</b></td><td>0.14 (-12.16%)</td><td>0.10 <b>(+124.43%)</b></td><td>539.90 (+13.85%)</td><td>347.84 (-12.13%)</td><td>288.60 <b>(-32.11%)</b></td><td>192.00 <b>(-30.38%)</b></td><td>150.65 <b>(+87.04%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>474.20 (n/a)</td><td>395.84 (n/a)</td><td>425.10 (n/a)</td><td>275.80 (n/a)</td><td>80.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.27 (-3.86%)</td><td>0.20 (+17.31%)</td><td>0.22 <b>(+46.81%)</b></td><td>0.13 (-3.78%)</td><td>0.07 (+12.52%)</td><td>565.10 (+3.92%)</td><td>397.96 (-12.37%)</td><td>342.80 <b>(-31.88%)</b></td><td>274.70 (+4.05%)</td><td>140.95 <b>(+25.78%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>543.80 (n/a)</td><td>454.12 (n/a)</td><td>503.20 (n/a)</td><td>264.00 (n/a)</td><td>112.06 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (+2.09%)</td><td>0.10 (-13.11%)</td><td>0.08 <b>(-31.19%)</b></td><td>0.05 (-15.92%)</td><td>0.04 <b>(+21.64%)</b></td><td>803.20 (+18.92%)</td><td>456.70 <b>(+22.07%)</b></td><td>439.70 <b>(+45.31%)</b></td><td>245.30 (-2.04%)</td><td>224.00 <b>(+29.27%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>675.40 (n/a)</td><td>374.14 (n/a)</td><td>302.60 (n/a)</td><td>250.40 (n/a)</td><td>173.27 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (+5.99%)</td><td>0.11 <b>(+53.01%)</b></td><td>0.12 <b>(+60.09%)</b></td><td>0.08 <b>(+334.41%)</b></td><td>0.02 <b>(-48.38%)</b></td><td>447.90 <b>(-76.98%)</b></td><td>331.58 <b>(-55.77%)</b></td><td>311.40 <b>(-37.55%)</b></td><td>258.70 (-5.65%)</td><td>70.32 <b>(-89.65%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1945.60 (n/a)</td><td>749.64 (n/a)</td><td>498.60 (n/a)</td><td>274.20 (n/a)</td><td>679.34 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.17 (+7.49%)</td><td>0.12 (+16.34%)</td><td>0.12 <b>(+44.60%)</b></td><td>0.08 <b>(+24.03%)</b></td><td>0.04 (+2.40%)</td><td>487.10 (-19.38%)</td><td>346.82 (-15.25%)</td><td>303.10 <b>(-30.83%)</b></td><td>220.10 (-6.93%)</td><td>114.47 (-18.24%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>604.20 (n/a)</td><td>409.24 (n/a)</td><td>438.20 (n/a)</td><td>236.50 (n/a)</td><td>140.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (-15.95%)</td><td>0.08 <b>(-28.78%)</b></td><td>0.08 <b>(-28.85%)</b></td><td>0.01 <b>(-77.71%)</b></td><td>0.05 <b>(+30.58%)</b></td><td>2496.30 <b>(+348.57%)</b></td><td>822.88 <b>(+136.17%)</b></td><td>459.30 <b>(+40.54%)</b></td><td>279.30 (+18.95%)</td><td>943.56 <b>(+633.35%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>556.50 (n/a)</td><td>348.42 (n/a)</td><td>326.80 (n/a)</td><td>234.80 (n/a)</td><td>128.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (+11.03%)</td><td>0.09 (+8.65%)</td><td>0.13 <b>(+60.16%)</b></td><td>0.01 <b>(-73.92%)</b></td><td>0.05 <b>(+61.89%)</b></td><td>2482.00 <b>(+283.44%)</b></td><td>772.64 <b>(+64.28%)</b></td><td>291.60 <b>(-37.57%)</b></td><td>273.40 (-9.95%)</td><td>961.62 <b>(+474.10%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>647.30 (n/a)</td><td>470.32 (n/a)</td><td>467.10 (n/a)</td><td>303.60 (n/a)</td><td>167.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 <b>(+23.02%)</b></td><td>0.11 <b>(+49.84%)</b></td><td>0.12 <b>(+76.39%)</b></td><td>0.06 <b>(+58.70%)</b></td><td>0.04 <b>(+24.94%)</b></td><td>666.10 <b>(-36.99%)</b></td><td>378.20 <b>(-35.13%)</b></td><td>304.90 <b>(-43.30%)</b></td><td>244.70 (-18.70%)</td><td>174.96 <b>(-38.61%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1057.20 (n/a)</td><td>583.02 (n/a)</td><td>537.70 (n/a)</td><td>301.00 (n/a)</td><td>285.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.17 (+7.99%)</td><td>0.10 (-10.04%)</td><td>0.08 <b>(-41.16%)</b></td><td>0.05 <b>(+159.71%)</b></td><td>0.05 (-10.63%)</td><td>777.70 <b>(-61.49%)</b></td><td>502.02 <b>(-24.29%)</b></td><td>544.10 <b>(+69.93%)</b></td><td>237.00 (-7.39%)</td><td>225.58 <b>(-70.41%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2019.70 (n/a)</td><td>663.10 (n/a)</td><td>320.20 (n/a)</td><td>255.90 (n/a)</td><td>762.32 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (+2.57%)</td><td>0.13 (+1.97%)</td><td>0.13 (-6.32%)</td><td>0.09 (+6.37%)</td><td>0.02 <b>(-21.18%)</b></td><td>471.80 (-6.00%)</td><td>335.28 (-4.06%)</td><td>313.90 (+6.73%)</td><td>267.20 (-2.52%)</td><td>78.83 <b>(-21.52%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>501.90 (n/a)</td><td>349.46 (n/a)</td><td>294.10 (n/a)</td><td>274.10 (n/a)</td><td>100.45 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.21 (+17.37%)</td><td>0.12 <b>(+23.24%)</b></td><td>0.10 <b>(+31.36%)</b></td><td>0.08 (+13.60%)</td><td>0.05 (+14.27%)</td><td>500.30 (-11.97%)</td><td>388.54 (-19.15%)</td><td>411.80 <b>(-23.88%)</b></td><td>196.40 (-14.79%)</td><td>122.40 (-13.07%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>568.30 (n/a)</td><td>480.56 (n/a)</td><td>541.00 (n/a)</td><td>230.50 (n/a)</td><td>140.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (+6.22%)</td><td>0.10 (+0.27%)</td><td>0.09 (+2.78%)</td><td>0.07 <b>(-20.96%)</b></td><td>0.03 <b>(+81.39%)</b></td><td>627.70 <b>(+26.53%)</b></td><td>461.96 (+7.30%)</td><td>458.30 (-2.70%)</td><td>303.60 (-5.86%)</td><td>158.50 <b>(+110.55%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>496.10 (n/a)</td><td>430.52 (n/a)</td><td>471.00 (n/a)</td><td>322.50 (n/a)</td><td>75.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.22 <b>(+42.23%)</b></td><td>0.12 <b>(+27.44%)</b></td><td>0.10 (+18.52%)</td><td>0.07 (-3.84%)</td><td>0.06 <b>(+85.99%)</b></td><td>602.30 (+3.99%)</td><td>405.40 (-12.78%)</td><td>426.40 (-15.63%)</td><td>190.10 <b>(-29.67%)</b></td><td>171.93 <b>(+40.90%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>579.20 (n/a)</td><td>464.82 (n/a)</td><td>505.40 (n/a)</td><td>270.30 (n/a)</td><td>122.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (-7.12%)</td><td>0.09 <b>(-23.60%)</b></td><td>0.09 <b>(-30.72%)</b></td><td>0.06 <b>(-30.56%)</b></td><td>0.03 (-0.85%)</td><td>633.60 <b>(+44.00%)</b></td><td>464.14 <b>(+33.44%)</b></td><td>450.90 <b>(+44.33%)</b></td><td>293.80 (+7.70%)</td><td>126.83 <b>(+48.34%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>440.00 (n/a)</td><td>347.82 (n/a)</td><td>312.40 (n/a)</td><td>272.80 (n/a)</td><td>85.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (+5.86%)</td><td>0.09 (+15.76%)</td><td>0.08 <b>(-23.59%)</b></td><td>0.07 <b>(+290.35%)</b></td><td>0.03 <b>(-47.74%)</b></td><td>517.80 <b>(-74.38%)</b></td><td>414.44 <b>(-57.75%)</b></td><td>437.60 <b>(+30.86%)</b></td><td>247.70 (-5.53%)</td><td>100.40 <b>(-89.24%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2021.40 (n/a)</td><td>980.84 (n/a)</td><td>334.40 (n/a)</td><td>262.20 (n/a)</td><td>933.18 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.16 (+19.79%)</td><td>0.10 (+8.03%)</td><td>0.07 (-3.87%)</td><td>0.06 <b>(+36.22%)</b></td><td>0.04 (+17.86%)</td><td>541.40 <b>(-26.59%)</b></td><td>414.22 (-8.34%)</td><td>492.30 (+4.01%)</td><td>215.80 (-16.52%)</td><td>143.63 <b>(-23.92%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>737.50 (n/a)</td><td>451.92 (n/a)</td><td>473.30 (n/a)</td><td>258.50 (n/a)</td><td>188.79 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (-11.38%)</td><td>0.07 <b>(-38.03%)</b></td><td>0.07 <b>(-37.76%)</b></td><td>0.02 <b>(-72.36%)</b></td><td>0.06 <b>(+22.77%)</b></td><td>1921.60 <b>(+261.75%)</b></td><td>989.88 <b>(+175.44%)</b></td><td>491.00 <b>(+60.67%)</b></td><td>228.60 (+12.83%)</td><td>847.46 <b>(+468.08%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>531.20 (n/a)</td><td>359.38 (n/a)</td><td>305.60 (n/a)</td><td>202.60 (n/a)</td><td>149.18 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (-6.33%)</td><td>0.10 (+10.02%)</td><td>0.12 <b>(+81.03%)</b></td><td>0.06 (+5.47%)</td><td>0.03 (-18.69%)</td><td>587.70 (-5.18%)</td><td>385.92 (-12.95%)</td><td>290.20 <b>(-44.77%)</b></td><td>274.70 (+6.76%)</td><td>146.87 (-14.95%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>619.80 (n/a)</td><td>443.34 (n/a)</td><td>525.40 (n/a)</td><td>257.30 (n/a)</td><td>172.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 <b>(-41.37%)</b></td><td>0.07 (-17.38%)</td><td>0.07 (-2.89%)</td><td>0.06 (-9.00%)</td><td>0.01 <b>(-76.20%)</b></td><td>609.30 (+9.90%)</td><td>522.96 (+14.50%)</td><td>510.10 (+2.99%)</td><td>473.60 <b>(+70.61%)</b></td><td>51.68 <b>(-53.45%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>554.40 (n/a)</td><td>456.72 (n/a)</td><td>495.30 (n/a)</td><td>277.60 (n/a)</td><td>111.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.19 <b>(+36.24%)</b></td><td>0.14 <b>(+73.55%)</b></td><td>0.14 <b>(+86.61%)</b></td><td>0.06 <b>(+151.83%)</b></td><td>0.05 (+14.00%)</td><td>550.50 <b>(-60.29%)</b></td><td>292.10 <b>(-51.59%)</b></td><td>249.80 <b>(-46.42%)</b></td><td>182.70 <b>(-26.60%)</b></td><td>148.13 <b>(-67.15%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1386.30 (n/a)</td><td>603.42 (n/a)</td><td>466.20 (n/a)</td><td>248.90 (n/a)</td><td>451.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.48 <b>(+21.38%)</b></td><td>0.40 <b>(+35.81%)</b></td><td>0.43 <b>(+62.92%)</b></td><td>0.25 (+8.93%)</td><td>0.09 <b>(+34.37%)</b></td><td>528.10 (-8.20%)</td><td>344.92 <b>(-25.13%)</b></td><td>305.30 <b>(-38.63%)</b></td><td>274.40 (-17.60%)</td><td>104.58 (+6.75%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>575.30 (n/a)</td><td>460.72 (n/a)</td><td>497.50 (n/a)</td><td>333.00 (n/a)</td><td>97.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.48 (+5.06%)</td><td>0.35 <b>(+32.58%)</b></td><td>0.35 <b>(+49.12%)</b></td><td>0.22 <b>(+54.90%)</b></td><td>0.11 (-8.16%)</td><td>584.30 <b>(-35.44%)</b></td><td>409.74 <b>(-28.79%)</b></td><td>374.60 <b>(-32.94%)</b></td><td>274.80 (-4.81%)</td><td>132.37 <b>(-41.46%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.45 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>905.10 (n/a)</td><td>575.38 (n/a)</td><td>558.60 (n/a)</td><td>288.70 (n/a)</td><td>226.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.45 (-0.82%)</td><td>0.29 (+7.84%)</td><td>0.27 (+18.11%)</td><td>0.16 (-3.49%)</td><td>0.11 (-0.24%)</td><td>805.90 (+3.61%)</td><td>518.82 (-6.38%)</td><td>493.80 (-15.33%)</td><td>288.70 (+0.84%)</td><td>200.10 (+9.89%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.46 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>777.80 (n/a)</td><td>554.20 (n/a)</td><td>583.20 (n/a)</td><td>286.30 (n/a)</td><td>182.09 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.00 <b>(+40.00%)</b></td><td>0.00 <b>(+26.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+57.06%)</b></td><td>18051.22 (-11.45%)</td><td>13013.80 (-16.40%)</td><td>15737.41 (+5.06%)</td><td>6128.38 <b>(-30.12%)</b></td><td>5018.61 (+11.34%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20384.69 (n/a)</td><td>15567.08 (n/a)</td><td>14979.64 (n/a)</td><td>8770.42 (n/a)</td><td>4507.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.00 (-15.38%)</td><td>0.00 <b>(+38.24%)</b></td><td>0.00 <b>(+83.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-14.43%)</td><td>19999.75 (-8.83%)</td><td>10150.68 <b>(-30.57%)</b></td><td>7522.72 <b>(-47.31%)</b></td><td>7470.09 <b>(+20.32%)</b></td><td>5515.22 (-2.44%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21935.83 (n/a)</td><td>14619.84 (n/a)</td><td>14276.29 (n/a)</td><td>6208.41 (n/a)</td><td>5653.20 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (-4.31%)</td><td>0.10 (+8.97%)</td><td>0.07 (+3.41%)</td><td>0.07 (-0.44%)</td><td>0.04 (+3.37%)</td><td>31163.29 (+0.42%)</td><td>24087.57 (-6.98%)</td><td>28847.96 (-3.26%)</td><td>14548.21 (+4.54%)</td><td>7959.40 (+10.84%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>31031.62 (n/a)</td><td>25893.77 (n/a)</td><td>29819.45 (n/a)</td><td>13917.06 (n/a)</td><td>7181.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>2.70 (-7.80%)</td><td>1.64 <b>(-37.87%)</b></td><td>1.52 <b>(-45.97%)</b></td><td>1.02 <b>(-49.78%)</b></td><td>0.63 <b>(+67.23%)</b></td><td>1028.80 <b>(+99.15%)</b></td><td>704.28 <b>(+74.23%)</b></td><td>689.80 <b>(+85.08%)</b></td><td>388.10 (+8.47%)</td><td>227.73 <b>(+242.22%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.93 (n/a)</td><td>2.64 (n/a)</td><td>2.81 (n/a)</td><td>2.03 (n/a)</td><td>0.38 (n/a)</td><td>516.60 (n/a)</td><td>404.22 (n/a)</td><td>372.70 (n/a)</td><td>357.80 (n/a)</td><td>66.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.21 <b>(-31.96%)</b></td><td>2.02 <b>(-25.88%)</b></td><td>2.12 <b>(-23.26%)</b></td><td>1.13 (-18.91%)</td><td>0.80 <b>(-39.13%)</b></td><td>928.70 <b>(+23.32%)</b></td><td>591.58 <b>(+27.25%)</b></td><td>494.00 <b>(+30.31%)</b></td><td>327.00 <b>(+46.97%)</b></td><td>236.41 (+8.50%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>4.71 (n/a)</td><td>2.72 (n/a)</td><td>2.77 (n/a)</td><td>1.39 (n/a)</td><td>1.32 (n/a)</td><td>753.10 (n/a)</td><td>464.88 (n/a)</td><td>379.10 (n/a)</td><td>222.50 (n/a)</td><td>217.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.01 (+15.09%)</td><td>1.66 (-18.94%)</td><td>1.59 <b>(-24.44%)</b></td><td>0.30 <b>(-78.69%)</b></td><td>0.97 <b>(+80.25%)</b></td><td>3474.20 <b>(+369.23%)</b></td><td>1147.94 <b>(+111.28%)</b></td><td>660.00 <b>(+32.34%)</b></td><td>348.60 (-13.11%)</td><td>1308.08 <b>(+765.05%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.61 (n/a)</td><td>2.05 (n/a)</td><td>2.10 (n/a)</td><td>1.42 (n/a)</td><td>0.54 (n/a)</td><td>740.40 (n/a)</td><td>543.32 (n/a)</td><td>498.70 (n/a)</td><td>401.20 (n/a)</td><td>151.22 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.49 <b>(+42.68%)</b></td><td>2.44 <b>(+27.95%)</b></td><td>2.37 (+11.74%)</td><td>1.20 (-6.80%)</td><td>0.87 <b>(+75.65%)</b></td><td>876.20 (+7.30%)</td><td>491.94 (-15.92%)</td><td>442.00 (-10.49%)</td><td>300.60 <b>(-29.90%)</b></td><td>227.47 <b>(+35.28%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.45 (n/a)</td><td>1.91 (n/a)</td><td>2.12 (n/a)</td><td>1.28 (n/a)</td><td>0.50 (n/a)</td><td>816.60 (n/a)</td><td>585.10 (n/a)</td><td>493.80 (n/a)</td><td>428.80 (n/a)</td><td>168.15 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>4.33 (+4.85%)</td><td>3.44 <b>(+27.88%)</b></td><td>3.73 (+2.27%)</td><td>2.51 <b>(+336.46%)</b></td><td>0.79 <b>(-53.37%)</b></td><td>836.70 <b>(-77.09%)</b></td><td>639.38 <b>(-55.29%)</b></td><td>561.50 (-2.23%)</td><td>484.70 (-4.62%)</td><td>157.11 <b>(-88.56%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>4.13 (n/a)</td><td>2.69 (n/a)</td><td>3.65 (n/a)</td><td>0.57 (n/a)</td><td>1.70 (n/a)</td><td>3651.90 (n/a)</td><td>1430.06 (n/a)</td><td>574.30 (n/a)</td><td>508.20 (n/a)</td><td>1372.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.81 (+11.49%)</td><td>3.49 (+18.47%)</td><td>3.82 <b>(+55.84%)</b></td><td>0.60 (-4.53%)</td><td>1.90 (+3.45%)</td><td>3510.30 (+4.74%)</td><td>1120.90 (-8.03%)</td><td>548.70 <b>(-35.83%)</b></td><td>360.70 (-10.32%)</td><td>1340.49 (+10.02%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.21 (n/a)</td><td>2.95 (n/a)</td><td>2.45 (n/a)</td><td>0.63 (n/a)</td><td>1.84 (n/a)</td><td>3351.50 (n/a)</td><td>1218.74 (n/a)</td><td>855.10 (n/a)</td><td>402.20 (n/a)</td><td>1218.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.32 (-7.39%)</td><td>3.11 (+0.42%)</td><td>3.41 (-7.86%)</td><td>0.57 <b>(-42.67%)</b></td><td>1.72 (-16.50%)</td><td>3679.80 <b>(+74.44%)</b></td><td>1213.44 (+7.39%)</td><td>614.90 (+8.52%)</td><td>394.60 (+7.99%)</td><td>1385.99 <b>(+56.25%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.74 (n/a)</td><td>3.09 (n/a)</td><td>3.70 (n/a)</td><td>0.99 (n/a)</td><td>2.06 (n/a)</td><td>2109.50 (n/a)</td><td>1129.92 (n/a)</td><td>566.60 (n/a)</td><td>365.40 (n/a)</td><td>887.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.90 (-9.02%)</td><td>3.54 <b>(-23.28%)</b></td><td>3.52 <b>(-32.28%)</b></td><td>0.61 <b>(-65.06%)</b></td><td>1.99 (+11.47%)</td><td>3459.30 <b>(+186.22%)</b></td><td>1111.94 <b>(+97.63%)</b></td><td>596.40 <b>(+47.70%)</b></td><td>355.40 (+9.93%)</td><td>1319.00 <b>(+260.76%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>6.49 (n/a)</td><td>4.62 (n/a)</td><td>5.19 (n/a)</td><td>1.74 (n/a)</td><td>1.78 (n/a)</td><td>1208.60 (n/a)</td><td>562.64 (n/a)</td><td>403.80 (n/a)</td><td>323.30 (n/a)</td><td>365.62 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>6.17 <b>(+57.46%)</b></td><td>2.62 <b>(-23.22%)</b></td><td>1.75 <b>(-50.25%)</b></td><td>0.59 <b>(-79.83%)</b></td><td>2.42 <b>(+493.22%)</b></td><td>3556.20 <b>(+395.91%)</b></td><td>1807.38 <b>(+190.73%)</b></td><td>1197.90 <b>(+100.99%)</b></td><td>340.10 <b>(-36.48%)</b></td><td>1566.00 <b>(+1978.31%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>3.92 (n/a)</td><td>3.41 (n/a)</td><td>3.52 (n/a)</td><td>2.92 (n/a)</td><td>0.41 (n/a)</td><td>717.10 (n/a)</td><td>621.66 (n/a)</td><td>596.00 (n/a)</td><td>535.40 (n/a)</td><td>75.35 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.91 <b>(-47.46%)</b></td><td>2.80 (-10.14%)</td><td>3.15 <b>(+28.94%)</b></td><td>0.60 (-0.78%)</td><td>1.28 <b>(-50.35%)</b></td><td>3517.40 (+0.79%)</td><td>1208.32 (-4.49%)</td><td>666.20 <b>(-22.44%)</b></td><td>536.60 <b>(+90.35%)</b></td><td>1292.14 (+1.55%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>7.44 (n/a)</td><td>3.12 (n/a)</td><td>2.44 (n/a)</td><td>0.60 (n/a)</td><td>2.57 (n/a)</td><td>3489.80 (n/a)</td><td>1265.14 (n/a)</td><td>858.90 (n/a)</td><td>281.90 (n/a)</td><td>1272.38 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.07 (+6.59%)</td><td>3.97 (+10.22%)</td><td>3.76 (-5.98%)</td><td>3.19 <b>(+155.55%)</b></td><td>0.78 <b>(-46.27%)</b></td><td>1315.50 <b>(-60.87%)</b></td><td>1089.22 <b>(-27.03%)</b></td><td>1115.10 (+6.35%)</td><td>827.30 (-6.18%)</td><td>202.00 <b>(-80.89%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>4.76 (n/a)</td><td>3.60 (n/a)</td><td>4.00 (n/a)</td><td>1.25 (n/a)</td><td>1.45 (n/a)</td><td>3361.60 (n/a)</td><td>1492.76 (n/a)</td><td>1048.50 (n/a)</td><td>881.80 (n/a)</td><td>1057.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>7.34 (+1.05%)</td><td>6.42 <b>(+35.76%)</b></td><td>7.29 <b>(+78.97%)</b></td><td>3.49 <b>(+105.66%)</b></td><td>1.66 <b>(-27.46%)</b></td><td>1202.10 <b>(-51.38%)</b></td><td>710.26 <b>(-38.67%)</b></td><td>575.60 <b>(-44.12%)</b></td><td>571.70 (-1.04%)</td><td>275.97 <b>(-64.18%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>7.26 (n/a)</td><td>4.73 (n/a)</td><td>4.07 (n/a)</td><td>1.70 (n/a)</td><td>2.29 (n/a)</td><td>2472.20 (n/a)</td><td>1158.04 (n/a)</td><td>1030.10 (n/a)</td><td>577.70 (n/a)</td><td>770.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>8.35 (+18.64%)</td><td>5.23 (+1.81%)</td><td>6.02 (+13.88%)</td><td>1.23 <b>(-66.74%)</b></td><td>2.75 <b>(+97.26%)</b></td><td>3417.30 <b>(+200.66%)</b></td><td>1263.66 <b>(+45.98%)</b></td><td>697.30 (-12.18%)</td><td>502.60 (-15.71%)</td><td>1222.54 <b>(+423.22%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>7.03 (n/a)</td><td>5.14 (n/a)</td><td>5.28 (n/a)</td><td>3.69 (n/a)</td><td>1.39 (n/a)</td><td>1136.60 (n/a)</td><td>865.64 (n/a)</td><td>794.00 (n/a)</td><td>596.30 (n/a)</td><td>233.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>12.22 <b>(+108.47%)</b></td><td>5.81 <b>(+47.94%)</b></td><td>4.20 (+5.37%)</td><td>1.19 <b>(-29.81%)</b></td><td>4.23 <b>(+186.17%)</b></td><td>3511.50 <b>(+42.48%)</b></td><td>1297.24 (+2.78%)</td><td>999.70 (-5.10%)</td><td>343.30 <b>(-52.03%)</b></td><td>1274.57 <b>(+85.47%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>5.86 (n/a)</td><td>3.92 (n/a)</td><td>3.98 (n/a)</td><td>1.70 (n/a)</td><td>1.48 (n/a)</td><td>2464.60 (n/a)</td><td>1262.18 (n/a)</td><td>1053.40 (n/a)</td><td>715.60 (n/a)</td><td>687.20 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>11.76 (-4.90%)</td><td>5.93 <b>(-31.28%)</b></td><td>4.45 <b>(-44.64%)</b></td><td>3.91 <b>(-39.37%)</b></td><td>3.29 <b>(+40.55%)</b></td><td>1073.60 <b>(+64.94%)</b></td><td>829.08 <b>(+61.96%)</b></td><td>943.10 <b>(+80.64%)</b></td><td>356.70 (+5.13%)</td><td>280.52 <b>(+130.25%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>12.36 (n/a)</td><td>8.63 (n/a)</td><td>8.03 (n/a)</td><td>6.44 (n/a)</td><td>2.34 (n/a)</td><td>650.90 (n/a)</td><td>511.90 (n/a)</td><td>522.10 (n/a)</td><td>339.30 (n/a)</td><td>121.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>8.44 (+6.57%)</td><td>5.58 (+0.14%)</td><td>6.64 (+18.74%)</td><td>1.93 (+14.59%)</td><td>2.56 (-0.00%)</td><td>2176.60 (-12.73%)</td><td>988.72 (-4.48%)</td><td>632.10 (-15.78%)</td><td>496.80 (-6.16%)</td><td>692.49 (-16.38%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>7.92 (n/a)</td><td>5.57 (n/a)</td><td>5.59 (n/a)</td><td>1.68 (n/a)</td><td>2.56 (n/a)</td><td>2494.20 (n/a)</td><td>1035.10 (n/a)</td><td>750.50 (n/a)</td><td>529.40 (n/a)</td><td>828.17 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>1.66 (-11.58%)</td><td>1.32 (-10.89%)</td><td>1.51 (-0.52%)</td><td>0.76 <b>(-24.54%)</b></td><td>0.39 <b>(+20.42%)</b></td><td>689.70 <b>(+32.53%)</b></td><td>435.46 (+17.53%)</td><td>346.30 (+0.52%)</td><td>316.40 (+13.12%)</td><td>160.42 <b>(+72.45%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>1.87 (n/a)</td><td>1.48 (n/a)</td><td>1.52 (n/a)</td><td>1.01 (n/a)</td><td>0.33 (n/a)</td><td>520.40 (n/a)</td><td>370.52 (n/a)</td><td>344.50 (n/a)</td><td>279.70 (n/a)</td><td>93.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.07 <b>(+21.55%)</b></td><td>1.82 (+12.17%)</td><td>1.71 <b>(-24.40%)</b></td><td>0.31 <b>(-27.39%)</b></td><td>1.01 (-2.78%)</td><td>3437.70 <b>(+37.73%)</b></td><td>1092.10 (-4.53%)</td><td>612.80 <b>(+32.27%)</b></td><td>342.10 (-17.72%)</td><td>1316.21 <b>(+33.67%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>2.52 (n/a)</td><td>1.62 (n/a)</td><td>2.26 (n/a)</td><td>0.42 (n/a)</td><td>1.04 (n/a)</td><td>2495.90 (n/a)</td><td>1143.90 (n/a)</td><td>463.30 (n/a)</td><td>415.80 (n/a)</td><td>984.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>4.37 (+14.60%)</td><td>2.87 <b>(+61.20%)</b></td><td>2.80 <b>(+58.56%)</b></td><td>1.54 <b>(+173.36%)</b></td><td>1.15 (-14.33%)</td><td>1359.80 <b>(-63.42%)</b></td><td>841.16 <b>(-58.12%)</b></td><td>748.30 <b>(-36.93%)</b></td><td>479.60 (-12.74%)</td><td>358.87 <b>(-76.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>3.82 (n/a)</td><td>1.78 (n/a)</td><td>1.77 (n/a)</td><td>0.56 (n/a)</td><td>1.34 (n/a)</td><td>3717.10 (n/a)</td><td>2008.72 (n/a)</td><td>1186.50 (n/a)</td><td>549.60 (n/a)</td><td>1536.14 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>1.71 (-3.47%)</td><td>1.26 <b>(+20.48%)</b></td><td>1.34 <b>(+41.73%)</b></td><td>0.77 <b>(+66.39%)</b></td><td>0.41 <b>(-25.79%)</b></td><td>679.30 <b>(-39.90%)</b></td><td>458.44 <b>(-28.86%)</b></td><td>392.20 <b>(-29.45%)</b></td><td>307.10 (+3.61%)</td><td>165.00 <b>(-53.48%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>1.77 (n/a)</td><td>1.05 (n/a)</td><td>0.94 (n/a)</td><td>0.46 (n/a)</td><td>0.56 (n/a)</td><td>1130.20 (n/a)</td><td>644.40 (n/a)</td><td>555.90 (n/a)</td><td>296.40 (n/a)</td><td>354.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (+13.80%)</td><td>0.10 (+13.54%)</td><td>0.11 <b>(+29.38%)</b></td><td>0.06 (-0.75%)</td><td>0.03 <b>(+22.72%)</b></td><td>557.90 (+0.76%)</td><td>353.66 (-9.84%)</td><td>309.00 <b>(-22.69%)</b></td><td>225.60 (-12.12%)</td><td>125.61 (+13.42%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>553.70 (n/a)</td><td>392.26 (n/a)</td><td>399.70 (n/a)</td><td>256.70 (n/a)</td><td>110.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (-12.25%)</td><td>0.06 <b>(-22.57%)</b></td><td>0.06 (-6.21%)</td><td>0.01 <b>(-69.31%)</b></td><td>0.05 (+17.21%)</td><td>2420.00 <b>(+225.88%)</b></td><td>1098.04 <b>(+127.68%)</b></td><td>541.90 (+6.61%)</td><td>264.20 (+13.98%)</td><td>1017.97 <b>(+351.20%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>742.60 (n/a)</td><td>482.28 (n/a)</td><td>508.30 (n/a)</td><td>231.80 (n/a)</td><td>225.62 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.22 (-14.50%)</td><td>0.18 (+2.92%)</td><td>0.20 <b>(+47.76%)</b></td><td>0.13 (+10.06%)</td><td>0.04 <b>(-40.04%)</b></td><td>491.40 (-9.13%)</td><td>376.60 (-8.51%)</td><td>325.10 <b>(-32.33%)</b></td><td>300.70 (+16.96%)</td><td>87.69 <b>(-34.85%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>540.80 (n/a)</td><td>411.62 (n/a)</td><td>480.40 (n/a)</td><td>257.10 (n/a)</td><td>134.59 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.23 (-17.70%)</td><td>0.15 (-5.01%)</td><td>0.16 (+15.28%)</td><td>0.06 <b>(-51.94%)</b></td><td>0.07 (+0.75%)</td><td>1072.30 <b>(+108.05%)</b></td><td>528.58 (+19.58%)</td><td>420.20 (-13.25%)</td><td>282.20 <b>(+21.48%)</b></td><td>320.24 <b>(+171.13%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.28 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>515.40 (n/a)</td><td>442.04 (n/a)</td><td>484.40 (n/a)</td><td>232.30 (n/a)</td><td>118.12 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.23 <b>(-21.18%)</b></td><td>0.16 <b>(-21.07%)</b></td><td>0.14 <b>(-40.56%)</b></td><td>0.08 <b>(-28.68%)</b></td><td>0.07 <b>(-22.06%)</b></td><td>844.80 <b>(+40.19%)</b></td><td>480.90 <b>(+25.11%)</b></td><td>481.50 <b>(+68.24%)</b></td><td>282.30 <b>(+26.88%)</b></td><td>229.41 <b>(+23.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>602.60 (n/a)</td><td>384.38 (n/a)</td><td>286.20 (n/a)</td><td>222.50 (n/a)</td><td>185.26 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.41 (-16.55%)</td><td>0.30 <b>(-28.52%)</b></td><td>0.27 <b>(-38.18%)</b></td><td>0.21 <b>(-29.28%)</b></td><td>0.08 (+12.13%)</td><td>631.30 <b>(+41.39%)</b></td><td>465.64 <b>(+44.21%)</b></td><td>493.80 <b>(+61.74%)</b></td><td>317.10 (+19.84%)</td><td>126.68 <b>(+77.71%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>446.50 (n/a)</td><td>322.90 (n/a)</td><td>305.30 (n/a)</td><td>264.60 (n/a)</td><td>71.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.54 (+10.25%)</td><td>0.30 (-13.41%)</td><td>0.23 (-19.95%)</td><td>0.19 (-17.44%)</td><td>0.14 (+9.66%)</td><td>690.90 <b>(+21.10%)</b></td><td>502.12 (+18.65%)</td><td>559.10 <b>(+24.94%)</b></td><td>244.10 (-9.29%)</td><td>174.31 (+19.03%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>570.50 (n/a)</td><td>423.18 (n/a)</td><td>447.50 (n/a)</td><td>269.10 (n/a)</td><td>146.44 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.45 (-16.84%)</td><td>0.29 (-18.43%)</td><td>0.25 <b>(-27.07%)</b></td><td>0.21 (+4.83%)</td><td>0.10 (-19.63%)</td><td>617.20 (-4.61%)</td><td>492.56 (+19.96%)</td><td>530.40 <b>(+37.13%)</b></td><td>291.40 <b>(+20.26%)</b></td><td>138.78 (-7.30%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.54 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>647.00 (n/a)</td><td>410.60 (n/a)</td><td>386.80 (n/a)</td><td>242.30 (n/a)</td><td>149.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (-8.93%)</td><td>0.05 (+5.61%)</td><td>0.05 <b>(+44.64%)</b></td><td>0.03 (+18.44%)</td><td>0.01 <b>(-31.07%)</b></td><td>480.20 (-15.58%)</td><td>354.42 (-11.28%)</td><td>305.40 <b>(-30.86%)</b></td><td>248.10 (+9.83%)</td><td>98.81 <b>(-32.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>568.80 (n/a)</td><td>399.50 (n/a)</td><td>441.70 (n/a)</td><td>225.90 (n/a)</td><td>146.67 (n/a)</td>
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
