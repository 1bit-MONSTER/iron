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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (+7.47%)</td><td>0.02 (-8.19%)</td><td>0.01 (-15.75%)</td><td>0.01 (+10.15%)</td><td>0.01 <b>(+21.74%)</b></td><td>473.10 (-9.23%)</td><td>401.38 (+10.69%)</td><td>434.40 (+18.69%)</td><td>217.90 (-6.96%)</td><td>104.12 (-1.02%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>521.20 (n/a)</td><td>362.60 (n/a)</td><td>366.00 (n/a)</td><td>234.20 (n/a)</td><td>105.20 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 <b>(+40.30%)</b></td><td>0.02 (+19.06%)</td><td>0.02 (-4.22%)</td><td>0.01 (-3.08%)</td><td>0.01 <b>(+74.21%)</b></td><td>553.60 (+3.19%)</td><td>357.46 (-10.22%)</td><td>336.30 (+4.41%)</td><td>214.00 <b>(-28.71%)</b></td><td>144.93 <b>(+22.29%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.50 (n/a)</td><td>398.14 (n/a)</td><td>322.10 (n/a)</td><td>300.20 (n/a)</td><td>118.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 <b>(+53.13%)</b></td><td>0.02 (+19.47%)</td><td>0.01 (-11.74%)</td><td>0.01 (-0.94%)</td><td>0.01 <b>(+112.66%)</b></td><td>616.10 (+0.95%)</td><td>432.18 (-8.73%)</td><td>485.10 (+13.31%)</td><td>236.80 <b>(-34.71%)</b></td><td>163.62 <b>(+35.76%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.30 (n/a)</td><td>473.50 (n/a)</td><td>428.10 (n/a)</td><td>362.70 (n/a)</td><td>120.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (-0.03%)</td><td>0.01 <b>(-23.25%)</b></td><td>0.01 <b>(-31.22%)</b></td><td>0.01 <b>(-47.44%)</b></td><td>0.01 <b>(+25.52%)</b></td><td>1126.90 <b>(+90.26%)</b></td><td>603.12 <b>(+53.17%)</b></td><td>527.00 <b>(+45.38%)</b></td><td>222.00 (+0.05%)</td><td>336.88 <b>(+130.58%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.30 (n/a)</td><td>393.76 (n/a)</td><td>362.50 (n/a)</td><td>221.90 (n/a)</td><td>146.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (+8.29%)</td><td>0.01 (-5.74%)</td><td>0.01 (-0.01%)</td><td>0.01 <b>(-36.08%)</b></td><td>0.00 <b>(+48.20%)</b></td><td>996.10 <b>(+56.45%)</b></td><td>617.80 (+14.44%)</td><td>599.20 (+0.02%)</td><td>351.80 (-7.66%)</td><td>241.25 <b>(+111.34%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>636.70 (n/a)</td><td>539.86 (n/a)</td><td>599.10 (n/a)</td><td>381.00 (n/a)</td><td>114.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (-14.64%)</td><td>0.01 <b>(-38.65%)</b></td><td>0.01 <b>(-46.48%)</b></td><td>0.00 <b>(-78.83%)</b></td><td>0.01 <b>(+44.90%)</b></td><td>2271.60 <b>(+372.36%)</b></td><td>879.44 <b>(+132.19%)</b></td><td>618.10 <b>(+86.85%)</b></td><td>337.00 (+17.14%)</td><td>786.84 <b>(+780.30%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>480.90 (n/a)</td><td>378.76 (n/a)</td><td>330.80 (n/a)</td><td>287.70 (n/a)</td><td>89.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (+10.65%)</td><td>0.04 <b>(-20.61%)</b></td><td>0.04 (-13.00%)</td><td>0.01 <b>(-74.36%)</b></td><td>0.02 <b>(+65.50%)</b></td><td>2080.20 <b>(+290.06%)</b></td><td>671.14 <b>(+119.63%)</b></td><td>285.60 (+14.93%)</td><td>213.70 (-9.64%)</td><td>795.22 <b>(+520.80%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.30 (n/a)</td><td>305.58 (n/a)</td><td>248.50 (n/a)</td><td>236.50 (n/a)</td><td>128.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 <b>(-26.73%)</b></td><td>0.03 <b>(-22.39%)</b></td><td>0.03 <b>(-33.44%)</b></td><td>0.02 (+14.64%)</td><td>0.01 <b>(-49.83%)</b></td><td>544.20 (-12.77%)</td><td>435.34 (+18.83%)</td><td>442.90 <b>(+50.24%)</b></td><td>333.90 <b>(+36.51%)</b></td><td>92.19 <b>(-41.32%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>623.90 (n/a)</td><td>366.36 (n/a)</td><td>294.80 (n/a)</td><td>244.60 (n/a)</td><td>157.12 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (-16.58%)</td><td>0.04 (-6.91%)</td><td>0.04 (+6.44%)</td><td>0.02 <b>(-30.89%)</b></td><td>0.01 (-11.65%)</td><td>674.30 <b>(+44.70%)</b></td><td>367.56 (+10.75%)</td><td>279.30 (-6.05%)</td><td>266.60 (+19.87%)</td><td>174.47 <b>(+53.67%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>466.00 (n/a)</td><td>331.88 (n/a)</td><td>297.30 (n/a)</td><td>222.40 (n/a)</td><td>113.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (-1.33%)</td><td>0.03 (-4.76%)</td><td>0.02 (-15.82%)</td><td>0.02 (-4.15%)</td><td>0.01 (+9.05%)</td><td>570.10 (+4.34%)</td><td>437.48 (+7.69%)</td><td>534.30 (+18.79%)</td><td>260.50 (+1.36%)</td><td>151.28 (+18.03%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.40 (n/a)</td><td>406.24 (n/a)</td><td>449.80 (n/a)</td><td>257.00 (n/a)</td><td>128.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 <b>(+21.43%)</b></td><td>0.04 <b>(+31.81%)</b></td><td>0.04 <b>(+61.64%)</b></td><td>0.03 <b>(+40.98%)</b></td><td>0.01 (-4.61%)</td><td>457.50 <b>(-29.07%)</b></td><td>334.72 <b>(-28.08%)</b></td><td>287.70 <b>(-38.14%)</b></td><td>231.10 (-17.64%)</td><td>99.67 <b>(-42.68%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>645.00 (n/a)</td><td>465.38 (n/a)</td><td>465.10 (n/a)</td><td>280.60 (n/a)</td><td>173.88 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 <b>(+70.26%)</b></td><td>0.04 (+10.77%)</td><td>0.02 <b>(-22.76%)</b></td><td>0.02 (-5.15%)</td><td>0.03 <b>(+129.68%)</b></td><td>641.90 (+5.44%)</td><td>473.76 (+9.22%)</td><td>515.00 <b>(+29.46%)</b></td><td>143.20 <b>(-41.26%)</b></td><td>201.41 <b>(+28.27%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>608.80 (n/a)</td><td>433.78 (n/a)</td><td>397.80 (n/a)</td><td>243.80 (n/a)</td><td>157.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (-3.99%)</td><td>0.06 (-7.99%)</td><td>0.08 (+16.80%)</td><td>0.01 <b>(-69.01%)</b></td><td>0.03 <b>(+66.78%)</b></td><td>1888.30 <b>(+222.73%)</b></td><td>652.46 <b>(+73.11%)</b></td><td>303.20 (-14.37%)</td><td>257.00 (+4.13%)</td><td>700.28 <b>(+450.86%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>585.10 (n/a)</td><td>376.90 (n/a)</td><td>354.10 (n/a)</td><td>246.80 (n/a)</td><td>127.12 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 <b>(+37.15%)</b></td><td>0.09 (+9.03%)</td><td>0.10 (+6.34%)</td><td>0.05 <b>(+59.17%)</b></td><td>0.04 <b>(+35.95%)</b></td><td>531.80 <b>(-37.18%)</b></td><td>340.64 (-10.93%)</td><td>254.80 (-5.98%)</td><td>177.40 <b>(-27.12%)</b></td><td>166.12 <b>(-36.11%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>846.50 (n/a)</td><td>382.46 (n/a)</td><td>271.00 (n/a)</td><td>243.40 (n/a)</td><td>260.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (-4.86%)</td><td>0.04 <b>(-31.02%)</b></td><td>0.04 <b>(-23.07%)</b></td><td>0.01 <b>(-57.33%)</b></td><td>0.04 (+14.63%)</td><td>2504.40 <b>(+134.38%)</b></td><td>1169.52 <b>(+131.85%)</b></td><td>571.80 <b>(+29.98%)</b></td><td>257.10 (+5.11%)</td><td>1049.66 <b>(+215.85%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1068.50 (n/a)</td><td>504.44 (n/a)</td><td>439.90 (n/a)</td><td>244.60 (n/a)</td><td>332.33 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (-4.23%)</td><td>0.07 (+8.23%)</td><td>0.08 (+19.09%)</td><td>0.04 <b>(-25.90%)</b></td><td>0.02 (+14.30%)</td><td>692.00 <b>(+34.95%)</b></td><td>381.86 (-2.72%)</td><td>295.40 (-16.03%)</td><td>270.90 (+4.43%)</td><td>176.44 <b>(+59.48%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>512.80 (n/a)</td><td>392.52 (n/a)</td><td>351.80 (n/a)</td><td>259.40 (n/a)</td><td>110.63 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 <b>(+23.43%)</b></td><td>0.06 (+4.36%)</td><td>0.05 (-12.97%)</td><td>0.04 (-9.41%)</td><td>0.03 <b>(+57.60%)</b></td><td>656.50 (+10.39%)</td><td>472.68 (+2.55%)</td><td>496.20 (+14.91%)</td><td>244.50 (-18.96%)</td><td>172.51 <b>(+36.21%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>594.70 (n/a)</td><td>460.94 (n/a)</td><td>431.80 (n/a)</td><td>301.70 (n/a)</td><td>126.65 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (-6.48%)</td><td>0.07 (-5.41%)</td><td>0.06 (-10.30%)</td><td>0.04 (+19.32%)</td><td>0.02 (-13.51%)</td><td>647.20 (-16.19%)</td><td>420.60 (+0.38%)</td><td>383.00 (+11.50%)</td><td>269.30 (+6.95%)</td><td>163.06 <b>(-24.07%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>772.20 (n/a)</td><td>419.00 (n/a)</td><td>343.50 (n/a)</td><td>251.80 (n/a)</td><td>214.74 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.18 <b>(-20.37%)</b></td><td>0.11 (-13.76%)</td><td>0.10 (-15.25%)</td><td>0.03 <b>(-68.54%)</b></td><td>0.06 (+7.70%)</td><td>1840.70 <b>(+217.91%)</b></td><td>712.24 <b>(+62.01%)</b></td><td>509.10 (+17.98%)</td><td>266.80 <b>(+25.61%)</b></td><td>649.58 <b>(+349.83%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>579.00 (n/a)</td><td>439.64 (n/a)</td><td>431.50 (n/a)</td><td>212.40 (n/a)</td><td>144.40 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.17 <b>(-23.63%)</b></td><td>0.12 (-15.63%)</td><td>0.13 (+0.81%)</td><td>0.08 <b>(+20.92%)</b></td><td>0.04 <b>(-40.72%)</b></td><td>594.30 (-17.30%)</td><td>432.94 (+7.74%)</td><td>385.10 (-0.80%)</td><td>294.40 <b>(+30.96%)</b></td><td>136.51 <b>(-31.16%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>718.60 (n/a)</td><td>401.82 (n/a)</td><td>388.20 (n/a)</td><td>224.80 (n/a)</td><td>198.30 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 <b>(-54.51%)</b></td><td>0.09 <b>(-53.58%)</b></td><td>0.08 <b>(-53.76%)</b></td><td>0.03 (+0.29%)</td><td>0.05 <b>(-58.37%)</b></td><td>1839.20 (-0.29%)</td><td>781.80 <b>(+41.34%)</b></td><td>607.50 <b>(+116.27%)</b></td><td>301.40 <b>(+119.84%)</b></td><td>610.15 (-15.82%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.36 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>0.12 (n/a)</td><td>1844.60 (n/a)</td><td>553.12 (n/a)</td><td>280.90 (n/a)</td><td>137.10 (n/a)</td><td>724.79 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.19 (+0.63%)</td><td>0.10 (-12.57%)</td><td>0.09 <b>(-28.21%)</b></td><td>0.04 (-6.29%)</td><td>0.05 (+1.17%)</td><td>1139.80 (+6.70%)</td><td>595.72 (+14.06%)</td><td>519.00 <b>(+39.29%)</b></td><td>264.80 (-0.60%)</td><td>328.70 (+2.69%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>1068.20 (n/a)</td><td>522.30 (n/a)</td><td>372.60 (n/a)</td><td>266.40 (n/a)</td><td>320.11 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (+17.77%)</td><td>0.11 <b>(+42.69%)</b></td><td>0.10 <b>(+24.72%)</b></td><td>0.08 <b>(+213.56%)</b></td><td>0.02 <b>(-43.43%)</b></td><td>606.30 <b>(-68.11%)</b></td><td>482.40 <b>(-48.39%)</b></td><td>490.90 (-19.81%)</td><td>340.80 (-15.08%)</td><td>94.35 <b>(-85.30%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1901.20 (n/a)</td><td>934.64 (n/a)</td><td>612.20 (n/a)</td><td>401.30 (n/a)</td><td>642.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.24 (-8.93%)</td><td>0.15 (+2.06%)</td><td>0.14 (+9.83%)</td><td>0.10 <b>(+29.50%)</b></td><td>0.05 <b>(-22.23%)</b></td><td>494.90 <b>(-22.78%)</b></td><td>370.12 (-8.58%)</td><td>349.70 (-8.96%)</td><td>206.70 (+9.77%)</td><td>112.63 <b>(-32.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>640.90 (n/a)</td><td>404.86 (n/a)</td><td>384.10 (n/a)</td><td>188.30 (n/a)</td><td>166.33 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 <b>(-29.76%)</b></td><td>0.00 <b>(-46.09%)</b></td><td>0.01 <b>(-38.77%)</b></td><td>0.00 <b>(-73.03%)</b></td><td>0.00 (-2.54%)</td><td>1984.80 <b>(+270.71%)</b></td><td>1025.74 <b>(+183.26%)</b></td><td>494.40 <b>(+63.33%)</b></td><td>307.30 <b>(+42.40%)</b></td><td>831.68 <b>(+466.31%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>535.40 (n/a)</td><td>362.12 (n/a)</td><td>302.70 (n/a)</td><td>215.80 (n/a)</td><td>146.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 <b>(+33.28%)</b></td><td>0.01 <b>(+43.86%)</b></td><td>0.01 <b>(+42.24%)</b></td><td>0.01 <b>(+20.08%)</b></td><td>0.00 <b>(+35.96%)</b></td><td>416.70 (-16.73%)</td><td>286.58 <b>(-30.04%)</b></td><td>269.00 <b>(-29.69%)</b></td><td>223.00 <b>(-24.99%)</b></td><td>75.14 (-13.49%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.40 (n/a)</td><td>409.64 (n/a)</td><td>382.60 (n/a)</td><td>297.30 (n/a)</td><td>86.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 <b>(+35.02%)</b></td><td>0.01 <b>(+32.59%)</b></td><td>0.01 <b>(+67.86%)</b></td><td>0.00 (-4.32%)</td><td>0.00 <b>(+73.30%)</b></td><td>531.20 (+4.53%)</td><td>335.62 (-17.77%)</td><td>268.30 <b>(-40.42%)</b></td><td>185.10 <b>(-25.93%)</b></td><td>147.42 <b>(+42.53%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>508.20 (n/a)</td><td>408.16 (n/a)</td><td>450.30 (n/a)</td><td>249.90 (n/a)</td><td>103.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (-13.90%)</td><td>0.01 (-15.54%)</td><td>0.01 <b>(-26.65%)</b></td><td>0.00 (-6.10%)</td><td>0.00 (-6.60%)</td><td>600.60 (+6.49%)</td><td>393.72 (+18.09%)</td><td>406.40 <b>(+36.33%)</b></td><td>259.10 (+16.14%)</td><td>138.52 (+3.54%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>564.00 (n/a)</td><td>333.40 (n/a)</td><td>298.10 (n/a)</td><td>223.10 (n/a)</td><td>133.79 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 <b>(+63.83%)</b></td><td>0.01 <b>(+49.13%)</b></td><td>0.01 <b>(+76.16%)</b></td><td>0.01 (+14.01%)</td><td>0.00 <b>(+62.84%)</b></td><td>484.50 (-12.28%)</td><td>298.12 <b>(-31.00%)</b></td><td>275.20 <b>(-43.22%)</b></td><td>182.00 <b>(-38.97%)</b></td><td>111.78 (-6.34%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>552.30 (n/a)</td><td>432.06 (n/a)</td><td>484.70 (n/a)</td><td>298.20 (n/a)</td><td>119.35 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 <b>(+29.39%)</b></td><td>0.01 <b>(+41.80%)</b></td><td>0.01 (+16.47%)</td><td>0.00 <b>(+78.83%)</b></td><td>0.00 <b>(+25.58%)</b></td><td>557.50 <b>(-44.08%)</b></td><td>421.24 <b>(-31.79%)</b></td><td>468.30 (-14.14%)</td><td>277.30 <b>(-22.74%)</b></td><td>123.76 <b>(-48.13%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>997.00 (n/a)</td><td>617.52 (n/a)</td><td>545.40 (n/a)</td><td>358.90 (n/a)</td><td>238.60 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 <b>(+26.05%)</b></td><td>0.02 (+11.89%)</td><td>0.02 (+14.15%)</td><td>0.01 (-4.79%)</td><td>0.01 <b>(+62.70%)</b></td><td>500.50 (+5.04%)</td><td>331.84 (-5.54%)</td><td>294.20 (-12.39%)</td><td>207.20 <b>(-20.67%)</b></td><td>121.16 <b>(+38.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>476.50 (n/a)</td><td>351.30 (n/a)</td><td>335.80 (n/a)</td><td>261.20 (n/a)</td><td>87.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (-17.98%)</td><td>0.01 (-6.15%)</td><td>0.02 <b>(+31.90%)</b></td><td>0.01 <b>(-39.98%)</b></td><td>0.01 (+0.84%)</td><td>1009.80 <b>(+66.61%)</b></td><td>500.62 (+18.28%)</td><td>337.60 <b>(-24.19%)</b></td><td>292.40 <b>(+21.93%)</b></td><td>307.07 <b>(+97.71%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.10 (n/a)</td><td>423.26 (n/a)</td><td>445.30 (n/a)</td><td>239.80 (n/a)</td><td>155.31 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (+2.82%)</td><td>0.01 (-15.71%)</td><td>0.01 <b>(-37.75%)</b></td><td>0.01 <b>(-36.14%)</b></td><td>0.01 <b>(+32.05%)</b></td><td>818.70 <b>(+56.60%)</b></td><td>506.72 <b>(+33.96%)</b></td><td>586.00 <b>(+60.64%)</b></td><td>244.40 (-2.75%)</td><td>240.59 <b>(+91.00%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>522.80 (n/a)</td><td>378.26 (n/a)</td><td>364.80 (n/a)</td><td>251.30 (n/a)</td><td>125.96 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (+1.29%)</td><td>0.02 (+10.14%)</td><td>0.02 <b>(+23.88%)</b></td><td>0.01 <b>(-20.54%)</b></td><td>0.01 <b>(+21.31%)</b></td><td>612.40 <b>(+25.85%)</b></td><td>336.30 (-4.26%)</td><td>258.10 (-19.29%)</td><td>244.40 (-1.25%)</td><td>157.52 <b>(+51.30%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>486.60 (n/a)</td><td>351.26 (n/a)</td><td>319.80 (n/a)</td><td>247.50 (n/a)</td><td>104.11 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (-12.24%)</td><td>0.01 (+12.74%)</td><td>0.02 <b>(+31.15%)</b></td><td>0.01 <b>(+101.62%)</b></td><td>0.01 <b>(-20.75%)</b></td><td>962.60 <b>(-50.40%)</b></td><td>464.88 <b>(-33.59%)</b></td><td>333.70 <b>(-23.76%)</b></td><td>251.10 (+13.93%)</td><td>291.78 <b>(-58.52%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1940.70 (n/a)</td><td>700.00 (n/a)</td><td>437.70 (n/a)</td><td>220.40 (n/a)</td><td>703.50 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 <b>(+64.19%)</b></td><td>0.01 (+11.79%)</td><td>0.01 (+3.91%)</td><td>0.00 <b>(-57.89%)</b></td><td>0.01 <b>(+348.24%)</b></td><td>1324.10 <b>(+137.51%)</b></td><td>588.04 <b>(+24.05%)</b></td><td>472.20 (-3.75%)</td><td>235.10 <b>(-39.09%)</b></td><td>434.00 <b>(+575.86%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>557.50 (n/a)</td><td>474.04 (n/a)</td><td>490.60 (n/a)</td><td>386.00 (n/a)</td><td>64.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 <b>(+31.78%)</b></td><td>0.03 (+6.77%)</td><td>0.02 (-14.34%)</td><td>0.02 (+6.19%)</td><td>0.01 <b>(+61.83%)</b></td><td>490.00 (-5.82%)</td><td>378.12 (-1.28%)</td><td>442.90 (+16.74%)</td><td>205.30 <b>(-24.10%)</b></td><td>124.65 (+19.73%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.30 (n/a)</td><td>383.04 (n/a)</td><td>379.40 (n/a)</td><td>270.50 (n/a)</td><td>104.11 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 <b>(+45.68%)</b></td><td>0.03 <b>(+20.61%)</b></td><td>0.03 (+11.29%)</td><td>0.02 (-15.29%)</td><td>0.01 <b>(+434.70%)</b></td><td>513.50 (+18.05%)</td><td>374.12 (-8.86%)</td><td>374.60 (-10.15%)</td><td>246.70 <b>(-31.36%)</b></td><td>127.21 <b>(+324.38%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>435.00 (n/a)</td><td>410.50 (n/a)</td><td>416.90 (n/a)</td><td>359.40 (n/a)</td><td>29.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 <b>(-21.36%)</b></td><td>0.03 (+7.60%)</td><td>0.02 <b>(+20.21%)</b></td><td>0.02 <b>(+310.51%)</b></td><td>0.01 <b>(-50.11%)</b></td><td>470.90 <b>(-75.64%)</b></td><td>369.18 <b>(-46.36%)</b></td><td>420.90 (-16.80%)</td><td>246.10 <b>(+27.18%)</b></td><td>108.29 <b>(-84.85%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1933.20 (n/a)</td><td>688.30 (n/a)</td><td>505.90 (n/a)</td><td>193.50 (n/a)</td><td>714.99 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 <b>(-32.22%)</b></td><td>0.02 <b>(-20.78%)</b></td><td>0.02 <b>(-28.85%)</b></td><td>0.01 <b>(+125.56%)</b></td><td>0.01 <b>(-59.17%)</b></td><td>843.30 <b>(-55.66%)</b></td><td>506.24 <b>(-22.11%)</b></td><td>457.30 <b>(+40.53%)</b></td><td>340.90 <b>(+47.51%)</b></td><td>194.44 <b>(-72.60%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1902.10 (n/a)</td><td>649.94 (n/a)</td><td>325.40 (n/a)</td><td>231.10 (n/a)</td><td>709.59 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 <b>(-31.40%)</b></td><td>0.03 (+1.97%)</td><td>0.04 <b>(+72.03%)</b></td><td>0.02 <b>(+22.98%)</b></td><td>0.01 <b>(-47.13%)</b></td><td>493.60 (-18.68%)</td><td>344.40 (-14.66%)</td><td>272.60 <b>(-41.88%)</b></td><td>246.60 <b>(+45.74%)</b></td><td>115.84 <b>(-36.40%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>607.00 (n/a)</td><td>403.56 (n/a)</td><td>469.00 (n/a)</td><td>169.20 (n/a)</td><td>182.13 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (-7.65%)</td><td>0.02 <b>(-23.83%)</b></td><td>0.02 <b>(-23.77%)</b></td><td>0.02 (-15.16%)</td><td>0.01 (+3.03%)</td><td>591.90 (+17.88%)</td><td>472.40 <b>(+33.37%)</b></td><td>439.10 <b>(+31.19%)</b></td><td>305.80 (+8.29%)</td><td>120.03 <b>(+34.88%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.10 (n/a)</td><td>354.20 (n/a)</td><td>334.70 (n/a)</td><td>282.40 (n/a)</td><td>88.99 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 <b>(-37.59%)</b></td><td>0.05 <b>(-27.35%)</b></td><td>0.05 (-16.31%)</td><td>0.04 (-14.44%)</td><td>0.01 <b>(-53.99%)</b></td><td>581.20 (+16.87%)</td><td>439.66 <b>(+31.48%)</b></td><td>409.10 (+19.48%)</td><td>359.90 <b>(+60.24%)</b></td><td>92.98 (-13.46%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>497.30 (n/a)</td><td>334.40 (n/a)</td><td>342.40 (n/a)</td><td>224.60 (n/a)</td><td>107.44 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (-12.81%)</td><td>0.06 (+5.53%)</td><td>0.07 <b>(+46.88%)</b></td><td>0.04 (+1.68%)</td><td>0.02 (-11.86%)</td><td>563.70 (-1.64%)</td><td>382.62 (-6.49%)</td><td>299.10 <b>(-31.91%)</b></td><td>259.20 (+14.69%)</td><td>150.35 (-0.51%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>573.10 (n/a)</td><td>409.16 (n/a)</td><td>439.30 (n/a)</td><td>226.00 (n/a)</td><td>151.13 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (-10.12%)</td><td>0.06 (-11.02%)</td><td>0.06 (-9.56%)</td><td>0.04 <b>(-22.51%)</b></td><td>0.02 <b>(+20.69%)</b></td><td>534.50 <b>(+29.04%)</b></td><td>382.96 (+16.71%)</td><td>345.90 (+10.58%)</td><td>266.70 (+11.26%)</td><td>117.48 <b>(+74.02%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>414.20 (n/a)</td><td>328.12 (n/a)</td><td>312.80 (n/a)</td><td>239.70 (n/a)</td><td>67.51 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 <b>(-52.18%)</b></td><td>0.04 <b>(-21.50%)</b></td><td>0.05 (-18.15%)</td><td>0.04 <b>(+99.30%)</b></td><td>0.00 <b>(-85.27%)</b></td><td>529.70 <b>(-49.83%)</b></td><td>471.46 (-7.66%)</td><td>456.70 <b>(+22.18%)</b></td><td>413.40 <b>(+109.10%)</b></td><td>52.70 <b>(-84.69%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1055.80 (n/a)</td><td>510.56 (n/a)</td><td>373.80 (n/a)</td><td>197.70 (n/a)</td><td>344.16 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 <b>(-21.89%)</b></td><td>0.04 <b>(-37.75%)</b></td><td>0.04 <b>(-44.70%)</b></td><td>0.02 <b>(-56.53%)</b></td><td>0.02 (+0.34%)</td><td>1071.10 <b>(+130.00%)</b></td><td>588.50 <b>(+78.46%)</b></td><td>539.30 <b>(+80.85%)</b></td><td>297.20 <b>(+28.05%)</b></td><td>290.14 <b>(+202.29%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>465.70 (n/a)</td><td>329.76 (n/a)</td><td>298.20 (n/a)</td><td>232.10 (n/a)</td><td>95.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 <b>(+26.29%)</b></td><td>0.05 (+15.28%)</td><td>0.04 (+7.35%)</td><td>0.03 (-5.09%)</td><td>0.02 <b>(+77.88%)</b></td><td>682.00 (+5.36%)</td><td>460.60 (-7.73%)</td><td>469.40 (-6.85%)</td><td>285.40 <b>(-20.81%)</b></td><td>162.71 <b>(+44.83%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>647.30 (n/a)</td><td>499.20 (n/a)</td><td>503.90 (n/a)</td><td>360.40 (n/a)</td><td>112.35 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.10 (n/a)</td><td>452.12 (n/a)</td><td>494.50 (n/a)</td><td>297.90 (n/a)</td><td>133.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>501.30 (n/a)</td><td>320.82 (n/a)</td><td>294.70 (n/a)</td><td>229.60 (n/a)</td><td>106.42 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>807.80 (n/a)</td><td>489.50 (n/a)</td><td>492.20 (n/a)</td><td>244.80 (n/a)</td><td>227.46 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.20 (n/a)</td><td>351.86 (n/a)</td><td>291.20 (n/a)</td><td>226.30 (n/a)</td><td>143.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.40 (n/a)</td><td>375.44 (n/a)</td><td>342.80 (n/a)</td><td>230.10 (n/a)</td><td>124.80 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>684.70 (n/a)</td><td>450.46 (n/a)</td><td>413.00 (n/a)</td><td>247.80 (n/a)</td><td>167.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1983.20 (n/a)</td><td>703.70 (n/a)</td><td>486.80 (n/a)</td><td>245.10 (n/a)</td><td>725.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>610.00 (n/a)</td><td>400.04 (n/a)</td><td>355.20 (n/a)</td><td>198.00 (n/a)</td><td>167.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>507.00 (n/a)</td><td>415.28 (n/a)</td><td>414.60 (n/a)</td><td>298.90 (n/a)</td><td>91.78 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.20 (+13.27%)</td><td>0.14 (-1.93%)</td><td>0.13 <b>(-22.56%)</b></td><td>0.09 (+5.97%)</td><td>0.05 <b>(+25.69%)</b></td><td>524.80 (-5.63%)</td><td>388.44 (+4.73%)</td><td>386.10 <b>(+29.13%)</b></td><td>248.80 (-11.71%)</td><td>133.53 (+9.65%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>556.10 (n/a)</td><td>370.90 (n/a)</td><td>299.00 (n/a)</td><td>281.80 (n/a)</td><td>121.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>614.60 (n/a)</td><td>374.62 (n/a)</td><td>288.50 (n/a)</td><td>244.50 (n/a)</td><td>162.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2496.40 (n/a)</td><td>966.32 (n/a)</td><td>461.90 (n/a)</td><td>323.40 (n/a)</td><td>907.74 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>293.70 (n/a)</td><td>267.64 (n/a)</td><td>270.10 (n/a)</td><td>234.10 (n/a)</td><td>23.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.50 (n/a)</td><td>475.90 (n/a)</td><td>508.00 (n/a)</td><td>195.80 (n/a)</td><td>167.33 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>657.70 (n/a)</td><td>439.44 (n/a)</td><td>411.10 (n/a)</td><td>225.20 (n/a)</td><td>207.61 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>614.80 (n/a)</td><td>347.64 (n/a)</td><td>300.60 (n/a)</td><td>198.60 (n/a)</td><td>173.93 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>536.40 (n/a)</td><td>348.10 (n/a)</td><td>303.00 (n/a)</td><td>203.60 (n/a)</td><td>140.39 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>631.70 (n/a)</td><td>410.36 (n/a)</td><td>416.70 (n/a)</td><td>213.40 (n/a)</td><td>158.36 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>598.30 (n/a)</td><td>435.22 (n/a)</td><td>421.10 (n/a)</td><td>322.10 (n/a)</td><td>107.41 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>606.00 (n/a)</td><td>375.56 (n/a)</td><td>285.70 (n/a)</td><td>244.30 (n/a)</td><td>163.16 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>621.60 (n/a)</td><td>460.16 (n/a)</td><td>494.40 (n/a)</td><td>205.10 (n/a)</td><td>171.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>530.40 (n/a)</td><td>403.24 (n/a)</td><td>452.30 (n/a)</td><td>237.40 (n/a)</td><td>127.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>658.10 (n/a)</td><td>494.94 (n/a)</td><td>529.60 (n/a)</td><td>308.50 (n/a)</td><td>131.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.50 (n/a)</td><td>436.24 (n/a)</td><td>408.80 (n/a)</td><td>281.60 (n/a)</td><td>111.57 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>485.70 (n/a)</td><td>437.46 (n/a)</td><td>470.20 (n/a)</td><td>352.40 (n/a)</td><td>56.44 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1827.70 (n/a)</td><td>771.50 (n/a)</td><td>536.50 (n/a)</td><td>264.70 (n/a)</td><td>628.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>449.90 (n/a)</td><td>387.10 (n/a)</td><td>431.40 (n/a)</td><td>267.20 (n/a)</td><td>77.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.40 (n/a)</td><td>407.80 (n/a)</td><td>475.80 (n/a)</td><td>218.30 (n/a)</td><td>145.96 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.80 (n/a)</td><td>423.54 (n/a)</td><td>438.80 (n/a)</td><td>313.20 (n/a)</td><td>88.35 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>434.60 (n/a)</td><td>329.88 (n/a)</td><td>279.60 (n/a)</td><td>243.70 (n/a)</td><td>90.36 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.40 (n/a)</td><td>381.54 (n/a)</td><td>391.30 (n/a)</td><td>217.60 (n/a)</td><td>138.31 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.30 (n/a)</td><td>347.74 (n/a)</td><td>366.60 (n/a)</td><td>234.90 (n/a)</td><td>109.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1045.10 (n/a)</td><td>523.16 (n/a)</td><td>422.10 (n/a)</td><td>244.80 (n/a)</td><td>336.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>389.90 (n/a)</td><td>288.38 (n/a)</td><td>281.10 (n/a)</td><td>220.10 (n/a)</td><td>62.34 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2497.20 (n/a)</td><td>804.60 (n/a)</td><td>404.00 (n/a)</td><td>304.00 (n/a)</td><td>948.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>655.90 (n/a)</td><td>453.82 (n/a)</td><td>485.90 (n/a)</td><td>252.80 (n/a)</td><td>175.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>530.50 (n/a)</td><td>365.84 (n/a)</td><td>274.10 (n/a)</td><td>250.90 (n/a)</td><td>138.89 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2127.20 (n/a)</td><td>725.14 (n/a)</td><td>423.90 (n/a)</td><td>243.50 (n/a)</td><td>790.30 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>652.00 (n/a)</td><td>516.20 (n/a)</td><td>603.70 (n/a)</td><td>213.70 (n/a)</td><td>177.96 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>581.40 (n/a)</td><td>465.90 (n/a)</td><td>471.70 (n/a)</td><td>290.70 (n/a)</td><td>108.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>537.20 (n/a)</td><td>396.18 (n/a)</td><td>408.80 (n/a)</td><td>266.60 (n/a)</td><td>102.64 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>560.00 (n/a)</td><td>383.24 (n/a)</td><td>299.90 (n/a)</td><td>259.70 (n/a)</td><td>137.27 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>553.20 (n/a)</td><td>379.34 (n/a)</td><td>318.80 (n/a)</td><td>225.10 (n/a)</td><td>141.12 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>597.20 (n/a)</td><td>398.64 (n/a)</td><td>374.70 (n/a)</td><td>274.90 (n/a)</td><td>132.34 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>609.70 (n/a)</td><td>401.82 (n/a)</td><td>352.10 (n/a)</td><td>248.70 (n/a)</td><td>169.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>643.80 (n/a)</td><td>454.98 (n/a)</td><td>524.60 (n/a)</td><td>250.10 (n/a)</td><td>170.05 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.49 <b>(-28.76%)</b></td><td>0.39 (+1.79%)</td><td>0.40 (+11.41%)</td><td>0.20 <b>(+53.79%)</b></td><td>0.11 <b>(-42.69%)</b></td><td>1104.50 <b>(-34.98%)</b></td><td>632.62 (-17.91%)</td><td>555.60 (-10.24%)</td><td>453.50 <b>(+40.36%)</b></td><td>268.79 <b>(-49.64%)</b></td><td>20.81 <b>(-28.76%)</b></td><td>16.53 (+1.79%)</td><td>16.98 (+11.41%)</td><td>8.54 <b>(+53.79%)</b></td><td>4.84 <b>(-42.69%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.68 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.13 (n/a)</td><td>0.20 (n/a)</td><td>1698.60 (n/a)</td><td>770.62 (n/a)</td><td>619.00 (n/a)</td><td>323.10 (n/a)</td><td>533.72 (n/a)</td><td>29.21 (n/a)</td><td>16.24 (n/a)</td><td>15.24 (n/a)</td><td>5.56 (n/a)</td><td>8.44 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.56 <b>(-28.99%)</b></td><td>0.39 (+3.28%)</td><td>0.47 <b>(+47.96%)</b></td><td>0.18 <b>(+47.98%)</b></td><td>0.19 <b>(-27.56%)</b></td><td>1208.70 <b>(-32.42%)</b></td><td>733.26 (-16.47%)</td><td>470.50 <b>(-32.42%)</b></td><td>393.80 <b>(+40.84%)</b></td><td>428.64 <b>(-29.04%)</b></td><td>23.97 <b>(-28.99%)</b></td><td>16.68 (+3.28%)</td><td>20.06 <b>(+47.96%)</b></td><td>7.81 <b>(+47.98%)</b></td><td>8.20 <b>(-27.56%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.79 (n/a)</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.12 (n/a)</td><td>0.27 (n/a)</td><td>1788.50 (n/a)</td><td>877.82 (n/a)</td><td>696.20 (n/a)</td><td>279.60 (n/a)</td><td>604.09 (n/a)</td><td>33.75 (n/a)</td><td>16.15 (n/a)</td><td>13.55 (n/a)</td><td>5.28 (n/a)</td><td>11.32 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.31 (+1.16%)</td><td>0.31 (+0.58%)</td><td>0.30 (-0.20%)</td><td>0.30 (+2.25%)</td><td>0.00 <b>(-27.67%)</b></td><td>83890.40 (-2.20%)</td><td>82431.34 (-0.59%)</td><td>82655.10 (+0.20%)</td><td>80898.60 (-1.15%)</td><td>1137.21 <b>(-30.28%)</b></td><td>212.36 (+1.16%)</td><td>208.45 (+0.58%)</td><td>207.85 (-0.20%)</td><td>204.79 (+2.25%)</td><td>2.88 <b>(-27.67%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85776.40 (n/a)</td><td>82920.94 (n/a)</td><td>82487.50 (n/a)</td><td>81840.40 (n/a)</td><td>1631.01 (n/a)</td><td>209.92 (n/a)</td><td>207.25 (n/a)</td><td>208.27 (n/a)</td><td>200.29 (n/a)</td><td>3.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>1.04 (-1.05%)</td><td>1.03 (+0.28%)</td><td>1.03 (+0.49%)</td><td>1.00 (+0.90%)</td><td>0.01 <b>(-35.98%)</b></td><td>25066.50 (-0.89%)</td><td>24546.76 (-0.30%)</td><td>24494.00 (-0.49%)</td><td>24154.70 (+1.06%)</td><td>331.36 <b>(-35.72%)</b></td><td>711.24 (-1.05%)</td><td>699.98 (+0.28%)</td><td>701.39 (+0.49%)</td><td>685.37 (+0.90%)</td><td>9.38 <b>(-35.98%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>1.05 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>0.02 (n/a)</td><td>25291.40 (n/a)</td><td>24619.66 (n/a)</td><td>24615.00 (n/a)</td><td>23901.60 (n/a)</td><td>515.47 (n/a)</td><td>718.77 (n/a)</td><td>698.06 (n/a)</td><td>697.94 (n/a)</td><td>679.28 (n/a)</td><td>14.66 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.82 (-0.76%)</td><td>0.80 (-1.07%)</td><td>0.81 (-1.10%)</td><td>0.78 (-2.16%)</td><td>0.02 <b>(+28.60%)</b></td><td>97150.20 (+2.21%)</td><td>94235.16 (+1.10%)</td><td>93508.50 (+1.11%)</td><td>92310.50 (+0.76%)</td><td>2132.09 <b>(+31.93%)</b></td><td>744.44 (-0.76%)</td><td>729.53 (-1.07%)</td><td>734.90 (-1.10%)</td><td>707.35 (-2.16%)</td><td>16.36 <b>(+28.60%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95048.20 (n/a)</td><td>93214.16 (n/a)</td><td>92479.70 (n/a)</td><td>91612.30 (n/a)</td><td>1616.11 (n/a)</td><td>750.11 (n/a)</td><td>737.40 (n/a)</td><td>743.08 (n/a)</td><td>723.00 (n/a)</td><td>12.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.76 (-1.18%)</td><td>0.75 (-1.13%)</td><td>0.76 (-1.29%)</td><td>0.75 (-0.07%)</td><td>0.01 <b>(-31.04%)</b></td><td>100930.60 (+0.07%)</td><td>100089.70 (+1.14%)</td><td>99878.00 (+1.31%)</td><td>99152.20 (+1.20%)</td><td>775.52 <b>(-30.24%)</b></td><td>693.07 (-1.18%)</td><td>686.61 (-1.13%)</td><td>688.03 (-1.29%)</td><td>680.86 (-0.07%)</td><td>5.32 <b>(-31.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100859.80 (n/a)</td><td>98961.86 (n/a)</td><td>98586.80 (n/a)</td><td>97981.30 (n/a)</td><td>1111.65 (n/a)</td><td>701.35 (n/a)</td><td>694.47 (n/a)</td><td>697.05 (n/a)</td><td>681.34 (n/a)</td><td>7.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.80 (-0.54%)</td><td>0.79 (-0.41%)</td><td>0.79 (-0.18%)</td><td>0.78 (-0.61%)</td><td>0.00 (-17.47%)</td><td>96280.50 (+0.62%)</td><td>95465.60 (+0.41%)</td><td>95451.30 (+0.18%)</td><td>94743.00 (+0.54%)</td><td>549.59 (-16.51%)</td><td>725.33 (-0.54%)</td><td>719.85 (-0.41%)</td><td>719.94 (-0.18%)</td><td>713.74 (-0.61%)</td><td>4.14 (-17.47%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95689.80 (n/a)</td><td>95077.52 (n/a)</td><td>95282.10 (n/a)</td><td>94235.00 (n/a)</td><td>658.28 (n/a)</td><td>729.24 (n/a)</td><td>722.80 (n/a)</td><td>721.22 (n/a)</td><td>718.15 (n/a)</td><td>5.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>4.82 (-14.41%)</td><td>3.83 (-5.53%)</td><td>4.03 (-1.91%)</td><td>2.17 (+0.92%)</td><td>0.99 <b>(-38.21%)</b></td><td>4115.00 (-0.91%)</td><td>2513.52 (-1.20%)</td><td>2211.70 (+1.95%)</td><td>1851.00 (+16.83%)</td><td>908.23 (-18.97%)</td><td>290.05 (-14.41%)</td><td>230.51 (-5.53%)</td><td>242.74 (-1.91%)</td><td>130.47 (+0.92%)</td><td>59.42 <b>(-38.21%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.63 (n/a)</td><td>4.05 (n/a)</td><td>4.11 (n/a)</td><td>2.15 (n/a)</td><td>1.60 (n/a)</td><td>4152.80 (n/a)</td><td>2543.96 (n/a)</td><td>2169.50 (n/a)</td><td>1584.30 (n/a)</td><td>1120.85 (n/a)</td><td>338.86 (n/a)</td><td>244.01 (n/a)</td><td>247.46 (n/a)</td><td>129.28 (n/a)</td><td>96.18 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>4.36 (-0.94%)</td><td>2.92 (+7.24%)</td><td>2.84 <b>(+27.23%)</b></td><td>2.20 (+7.30%)</td><td>0.88 (-9.72%)</td><td>4055.70 (-6.81%)</td><td>3251.96 (-8.17%)</td><td>3139.00 <b>(-21.40%)</b></td><td>2044.30 (+0.94%)</td><td>829.09 (-11.31%)</td><td>262.61 (-0.94%)</td><td>175.64 (+7.24%)</td><td>171.03 <b>(+27.23%)</b></td><td>132.37 (+7.30%)</td><td>52.93 (-9.72%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>4.40 (n/a)</td><td>2.72 (n/a)</td><td>2.23 (n/a)</td><td>2.05 (n/a)</td><td>0.97 (n/a)</td><td>4352.00 (n/a)</td><td>3541.38 (n/a)</td><td>3993.70 (n/a)</td><td>2025.20 (n/a)</td><td>934.82 (n/a)</td><td>265.10 (n/a)</td><td>163.79 (n/a)</td><td>134.43 (n/a)</td><td>123.36 (n/a)</td><td>58.63 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.55 <b>(+51.73%)</b></td><td>4.51 <b>(+56.20%)</b></td><td>4.09 <b>(+39.09%)</b></td><td>3.62 <b>(+65.04%)</b></td><td>0.83 <b>(+33.66%)</b></td><td>2464.90 <b>(-39.41%)</b></td><td>2027.28 <b>(-36.72%)</b></td><td>2178.70 <b>(-28.10%)</b></td><td>1604.90 <b>(-34.10%)</b></td><td>361.01 <b>(-48.53%)</b></td><td>334.51 <b>(+51.73%)</b></td><td>271.92 <b>(+56.20%)</b></td><td>246.42 <b>(+39.09%)</b></td><td>217.81 <b>(+65.04%)</b></td><td>50.06 <b>(+33.66%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.66 (n/a)</td><td>2.89 (n/a)</td><td>2.94 (n/a)</td><td>2.19 (n/a)</td><td>0.62 (n/a)</td><td>4068.00 (n/a)</td><td>3203.74 (n/a)</td><td>3030.30 (n/a)</td><td>2435.20 (n/a)</td><td>701.43 (n/a)</td><td>220.47 (n/a)</td><td>174.08 (n/a)</td><td>177.17 (n/a)</td><td>131.97 (n/a)</td><td>37.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>6.50 (+2.33%)</td><td>5.46 (+10.02%)</td><td>5.23 (+8.94%)</td><td>5.12 (+17.06%)</td><td>0.58 <b>(-27.81%)</b></td><td>6805.10 (-14.58%)</td><td>6438.44 (-10.04%)</td><td>6671.00 (-8.20%)</td><td>5365.00 (-2.28%)</td><td>603.53 <b>(-39.72%)</b></td><td>400.27 (+2.33%)</td><td>336.23 (+10.02%)</td><td>321.91 (+8.94%)</td><td>315.57 (+17.06%)</td><td>35.93 <b>(-27.81%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>6.35 (n/a)</td><td>4.96 (n/a)</td><td>4.80 (n/a)</td><td>4.38 (n/a)</td><td>0.81 (n/a)</td><td>7966.20 (n/a)</td><td>7156.78 (n/a)</td><td>7267.20 (n/a)</td><td>5490.00 (n/a)</td><td>1001.25 (n/a)</td><td>391.16 (n/a)</td><td>305.61 (n/a)</td><td>295.50 (n/a)</td><td>269.57 (n/a)</td><td>49.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>6.14 (+13.12%)</td><td>5.27 (+18.70%)</td><td>5.00 (+11.19%)</td><td>4.41 <b>(+43.71%)</b></td><td>0.73 (-15.69%)</td><td>7914.70 <b>(-30.41%)</b></td><td>6717.98 (-17.52%)</td><td>6977.60 (-10.07%)</td><td>5677.10 (-11.60%)</td><td>926.79 <b>(-51.20%)</b></td><td>378.27 (+13.12%)</td><td>324.62 (+18.70%)</td><td>307.77 (+11.19%)</td><td>271.33 <b>(+43.71%)</b></td><td>45.12 (-15.69%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.43 (n/a)</td><td>4.44 (n/a)</td><td>4.49 (n/a)</td><td>3.07 (n/a)</td><td>0.87 (n/a)</td><td>11374.10 (n/a)</td><td>8145.20 (n/a)</td><td>7758.80 (n/a)</td><td>6422.20 (n/a)</td><td>1898.99 (n/a)</td><td>334.39 (n/a)</td><td>273.49 (n/a)</td><td>276.78 (n/a)</td><td>188.80 (n/a)</td><td>53.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>6.50 (+13.95%)</td><td>5.93 (+12.18%)</td><td>6.45 <b>(+23.52%)</b></td><td>4.87 (+5.55%)</td><td>0.77 <b>(+73.89%)</b></td><td>7153.70 (-5.26%)</td><td>5963.90 (-10.08%)</td><td>5405.90 (-19.04%)</td><td>5362.80 (-12.24%)</td><td>832.00 <b>(+42.35%)</b></td><td>400.44 (+13.95%)</td><td>365.38 (+12.18%)</td><td>397.25 <b>(+23.52%)</b></td><td>300.19 (+5.55%)</td><td>47.56 <b>(+73.89%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.71 (n/a)</td><td>5.29 (n/a)</td><td>5.22 (n/a)</td><td>4.62 (n/a)</td><td>0.44 (n/a)</td><td>7550.70 (n/a)</td><td>6632.52 (n/a)</td><td>6677.60 (n/a)</td><td>6110.70 (n/a)</td><td>584.49 (n/a)</td><td>351.43 (n/a)</td><td>325.70 (n/a)</td><td>321.59 (n/a)</td><td>284.41 (n/a)</td><td>27.35 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.79 (+0.34%)</td><td>0.78 (+0.82%)</td><td>0.78 (+1.61%)</td><td>0.77 (+0.36%)</td><td>0.01 (+0.10%)</td><td>98096.70 (-0.36%)</td><td>96837.60 (-0.81%)</td><td>96486.70 (-1.59%)</td><td>96119.30 (-0.34%)</td><td>854.03 (-0.66%)</td><td>714.94 (+0.34%)</td><td>709.68 (+0.82%)</td><td>712.22 (+1.61%)</td><td>700.53 (+0.36%)</td><td>6.23 (+0.10%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>98446.60 (n/a)</td><td>97633.30 (n/a)</td><td>98042.80 (n/a)</td><td>96444.20 (n/a)</td><td>859.71 (n/a)</td><td>712.53 (n/a)</td><td>703.90 (n/a)</td><td>700.91 (n/a)</td><td>698.04 (n/a)</td><td>6.22 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.78 (+2.84%)</td><td>0.75 (+0.42%)</td><td>0.75 (+0.36%)</td><td>0.74 (-0.04%)</td><td>0.02 <b>(+125.85%)</b></td><td>102191.20 (+0.04%)</td><td>100185.96 (-0.39%)</td><td>100079.20 (-0.36%)</td><td>96995.10 (-2.76%)</td><td>2122.98 <b>(+119.97%)</b></td><td>708.48 (+2.84%)</td><td>686.17 (+0.42%)</td><td>686.65 (+0.36%)</td><td>672.46 (-0.04%)</td><td>14.69 <b>(+125.85%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>102154.30 (n/a)</td><td>100579.66 (n/a)</td><td>100438.80 (n/a)</td><td>99747.00 (n/a)</td><td>965.14 (n/a)</td><td>688.94 (n/a)</td><td>683.28 (n/a)</td><td>684.19 (n/a)</td><td>672.70 (n/a)</td><td>6.51 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.80 (-1.20%)</td><td>0.79 (-1.10%)</td><td>0.79 (-0.68%)</td><td>0.78 (-1.56%)</td><td>0.01 (+4.84%)</td><td>97102.40 (+1.59%)</td><td>95390.38 (+1.12%)</td><td>95175.80 (+0.68%)</td><td>94449.30 (+1.21%)</td><td>1035.18 (+8.13%)</td><td>727.58 (-1.20%)</td><td>720.47 (-1.10%)</td><td>722.03 (-0.68%)</td><td>707.70 (-1.56%)</td><td>7.75 (+4.84%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95586.60 (n/a)</td><td>94338.44 (n/a)</td><td>94529.80 (n/a)</td><td>93320.10 (n/a)</td><td>957.37 (n/a)</td><td>736.38 (n/a)</td><td>728.50 (n/a)</td><td>726.96 (n/a)</td><td>718.92 (n/a)</td><td>7.39 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.71 (-6.09%)</td><td>2.74 (+7.08%)</td><td>3.06 <b>(+49.18%)</b></td><td>1.34 (+8.21%)</td><td>0.98 <b>(-22.97%)</b></td><td>6021.20 (-7.59%)</td><td>3382.82 (-12.66%)</td><td>2636.10 <b>(-32.97%)</b></td><td>2173.70 (+6.48%)</td><td>1594.70 (-15.96%)</td><td>972.48 (-6.09%)</td><td>718.30 (+7.08%)</td><td>801.92 <b>(+49.18%)</b></td><td>351.08 (+8.21%)</td><td>256.21 <b>(-22.97%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.95 (n/a)</td><td>2.56 (n/a)</td><td>2.05 (n/a)</td><td>1.24 (n/a)</td><td>1.27 (n/a)</td><td>6515.50 (n/a)</td><td>3873.12 (n/a)</td><td>3932.50 (n/a)</td><td>2041.40 (n/a)</td><td>1897.45 (n/a)</td><td>1035.52 (n/a)</td><td>670.81 (n/a)</td><td>537.56 (n/a)</td><td>324.44 (n/a)</td><td>332.62 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.24 (+14.43%)</td><td>0.21 (+12.21%)</td><td>0.21 (+7.92%)</td><td>0.19 <b>(+23.58%)</b></td><td>0.02 (+4.81%)</td><td>6617.40 (-19.08%)</td><td>5905.64 (-11.16%)</td><td>6045.90 (-7.34%)</td><td>5114.30 (-12.61%)</td><td>653.11 <b>(-27.74%)</b></td><td>13.12 (+14.43%)</td><td>11.48 (+12.21%)</td><td>11.10 (+7.92%)</td><td>10.14 <b>(+23.58%)</b></td><td>1.30 (+4.81%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>8178.00 (n/a)</td><td>6647.66 (n/a)</td><td>6524.70 (n/a)</td><td>5852.20 (n/a)</td><td>903.81 (n/a)</td><td>11.47 (n/a)</td><td>10.23 (n/a)</td><td>10.29 (n/a)</td><td>8.21 (n/a)</td><td>1.24 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.82 (n/a)</td><td>3.58 (n/a)</td><td>3.53 (n/a)</td><td>3.33 (n/a)</td><td>0.23 (n/a)</td><td>3.81 (n/a)</td><td>3.57 (n/a)</td><td>3.53 (n/a)</td><td>3.33 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>7.73 (+9.92%)</td><td>6.98 (+13.63%)</td><td>7.37 <b>(+23.02%)</b></td><td>6.00 (+10.12%)</td><td>0.73 <b>(+20.59%)</b></td><td>7.72 (+9.92%)</td><td>6.98 (+13.63%)</td><td>7.36 <b>(+23.02%)</b></td><td>6.00 (+10.12%)</td><td>0.73 <b>(+20.59%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>7.03 (n/a)</td><td>6.14 (n/a)</td><td>5.99 (n/a)</td><td>5.45 (n/a)</td><td>0.61 (n/a)</td><td>7.03 (n/a)</td><td>6.14 (n/a)</td><td>5.98 (n/a)</td><td>5.45 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>14.05 <b>(+28.98%)</b></td><td>12.50 <b>(+45.40%)</b></td><td>13.37 <b>(+61.25%)</b></td><td>8.38 <b>(+21.61%)</b></td><td>2.36 <b>(+53.79%)</b></td><td>14.04 <b>(+28.98%)</b></td><td>12.50 <b>(+45.40%)</b></td><td>13.36 <b>(+61.25%)</b></td><td>8.38 <b>(+21.61%)</b></td><td>2.35 <b>(+53.79%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>10.90 (n/a)</td><td>8.60 (n/a)</td><td>8.29 (n/a)</td><td>6.89 (n/a)</td><td>1.53 (n/a)</td><td>10.89 (n/a)</td><td>8.59 (n/a)</td><td>8.28 (n/a)</td><td>6.89 (n/a)</td><td>1.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.81 (n/a)</td><td>3.69 (n/a)</td><td>3.72 (n/a)</td><td>3.45 (n/a)</td><td>0.15 (n/a)</td><td>3.81 (n/a)</td><td>3.68 (n/a)</td><td>3.72 (n/a)</td><td>3.44 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>7.54 <b>(+23.11%)</b></td><td>6.21 (+13.72%)</td><td>5.86 (+3.36%)</td><td>5.63 <b>(+31.70%)</b></td><td>0.78 (+11.06%)</td><td>7.54 <b>(+23.11%)</b></td><td>6.21 (+13.72%)</td><td>5.86 (+3.36%)</td><td>5.63 <b>(+31.70%)</b></td><td>0.78 (+11.06%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>6.13 (n/a)</td><td>5.46 (n/a)</td><td>5.67 (n/a)</td><td>4.27 (n/a)</td><td>0.70 (n/a)</td><td>6.12 (n/a)</td><td>5.46 (n/a)</td><td>5.67 (n/a)</td><td>4.27 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>14.11 (+0.16%)</td><td>9.59 (-14.16%)</td><td>8.10 <b>(-31.08%)</b></td><td>7.76 (+1.47%)</td><td>2.66 (-11.80%)</td><td>14.10 (+0.16%)</td><td>9.58 (-14.16%)</td><td>8.10 <b>(-31.08%)</b></td><td>7.75 (+1.47%)</td><td>2.66 (-11.80%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>14.08 (n/a)</td><td>11.17 (n/a)</td><td>11.76 (n/a)</td><td>7.65 (n/a)</td><td>3.01 (n/a)</td><td>14.07 (n/a)</td><td>11.16 (n/a)</td><td>11.75 (n/a)</td><td>7.64 (n/a)</td><td>3.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.16 (-3.02%)</td><td>2.56 <b>(+56.51%)</b></td><td>2.70 <b>(+117.48%)</b></td><td>1.53 <b>(+48.01%)</b></td><td>0.63 <b>(-31.05%)</b></td><td>3.15 (-3.02%)</td><td>2.56 <b>(+56.51%)</b></td><td>2.70 <b>(+117.48%)</b></td><td>1.52 <b>(+48.01%)</b></td><td>0.63 <b>(-31.05%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.25 (n/a)</td><td>1.64 (n/a)</td><td>1.24 (n/a)</td><td>1.03 (n/a)</td><td>0.92 (n/a)</td><td>3.25 (n/a)</td><td>1.63 (n/a)</td><td>1.24 (n/a)</td><td>1.03 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.48 (-1.01%)</td><td>0.38 <b>(+21.68%)</b></td><td>0.37 (+16.65%)</td><td>0.25 <b>(+235.09%)</b></td><td>0.10 <b>(-40.42%)</b></td><td>0.47 (-1.01%)</td><td>0.38 <b>(+21.68%)</b></td><td>0.37 (+16.65%)</td><td>0.25 <b>(+235.09%)</b></td><td>0.09 <b>(-40.42%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.48 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.68 (-7.19%)</td><td>0.46 (-1.17%)</td><td>0.52 <b>(+31.87%)</b></td><td>0.08 <b>(-76.37%)</b></td><td>0.24 <b>(+48.22%)</b></td><td>0.68 (-7.19%)</td><td>0.45 (-1.17%)</td><td>0.51 <b>(+31.87%)</b></td><td>0.08 <b>(-76.37%)</b></td><td>0.24 <b>(+48.22%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.74 (n/a)</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.16 (n/a)</td><td>0.73 (n/a)</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.01 <b>(+38.00%)</b></td><td>1.86 <b>(+28.11%)</b></td><td>2.04 <b>(+39.88%)</b></td><td>0.47 (+1.55%)</td><td>0.96 <b>(+51.42%)</b></td><td>2.97 <b>(+38.00%)</b></td><td>1.83 <b>(+28.11%)</b></td><td>2.01 <b>(+39.88%)</b></td><td>0.46 (+1.55%)</td><td>0.94 <b>(+51.42%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>2.18 (n/a)</td><td>1.45 (n/a)</td><td>1.46 (n/a)</td><td>0.46 (n/a)</td><td>0.63 (n/a)</td><td>2.15 (n/a)</td><td>1.43 (n/a)</td><td>1.44 (n/a)</td><td>0.45 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1903.30 (n/a)</td><td>765.06 (n/a)</td><td>568.40 (n/a)</td><td>226.80 (n/a)</td><td>653.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1332.00 (n/a)</td><td>567.46 (n/a)</td><td>471.10 (n/a)</td><td>253.00 (n/a)</td><td>442.50 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>577.30 (n/a)</td><td>439.98 (n/a)</td><td>434.80 (n/a)</td><td>293.30 (n/a)</td><td>107.72 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.80 (n/a)</td><td>378.90 (n/a)</td><td>318.80 (n/a)</td><td>217.70 (n/a)</td><td>168.51 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2435.10 (n/a)</td><td>910.14 (n/a)</td><td>603.40 (n/a)</td><td>276.40 (n/a)</td><td>866.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>963.70 (n/a)</td><td>549.98 (n/a)</td><td>551.90 (n/a)</td><td>231.10 (n/a)</td><td>292.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>680.90 (n/a)</td><td>443.06 (n/a)</td><td>458.20 (n/a)</td><td>279.80 (n/a)</td><td>163.22 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.60 (n/a)</td><td>441.88 (n/a)</td><td>492.50 (n/a)</td><td>282.30 (n/a)</td><td>129.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>698.50 (n/a)</td><td>529.14 (n/a)</td><td>553.10 (n/a)</td><td>370.50 (n/a)</td><td>124.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>404.50 (n/a)</td><td>301.86 (n/a)</td><td>277.70 (n/a)</td><td>252.60 (n/a)</td><td>60.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>526.50 (n/a)</td><td>463.58 (n/a)</td><td>455.00 (n/a)</td><td>371.70 (n/a)</td><td>64.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.80 (n/a)</td><td>462.98 (n/a)</td><td>460.00 (n/a)</td><td>307.50 (n/a)</td><td>116.55 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>339.00 (n/a)</td><td>286.94 (n/a)</td><td>283.30 (n/a)</td><td>251.40 (n/a)</td><td>34.58 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.90 (n/a)</td><td>350.28 (n/a)</td><td>295.00 (n/a)</td><td>220.80 (n/a)</td><td>153.81 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>544.80 (n/a)</td><td>366.02 (n/a)</td><td>280.70 (n/a)</td><td>207.60 (n/a)</td><td>160.39 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1120.70 (n/a)</td><td>560.04 (n/a)</td><td>489.50 (n/a)</td><td>258.70 (n/a)</td><td>328.72 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>837.10 (n/a)</td><td>485.18 (n/a)</td><td>476.40 (n/a)</td><td>269.40 (n/a)</td><td>233.95 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>628.10 (n/a)</td><td>474.38 (n/a)</td><td>450.30 (n/a)</td><td>345.60 (n/a)</td><td>117.65 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 (+17.62%)</td><td>0.07 (-17.53%)</td><td>0.05 <b>(-42.39%)</b></td><td>0.02 <b>(-66.20%)</b></td><td>0.04 <b>(+83.05%)</b></td><td>1974.50 <b>(+195.89%)</b></td><td>774.54 <b>(+81.12%)</b></td><td>598.60 <b>(+73.56%)</b></td><td>269.00 (-14.98%)</td><td>696.57 <b>(+365.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>667.30 (n/a)</td><td>427.64 (n/a)</td><td>344.90 (n/a)</td><td>316.40 (n/a)</td><td>149.79 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1989.10 (n/a)</td><td>736.08 (n/a)</td><td>524.30 (n/a)</td><td>218.30 (n/a)</td><td>719.93 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>656.10 (n/a)</td><td>404.98 (n/a)</td><td>364.70 (n/a)</td><td>314.50 (n/a)</td><td>142.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1891.80 (n/a)</td><td>947.10 (n/a)</td><td>399.40 (n/a)</td><td>232.10 (n/a)</td><td>849.56 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>593.90 (n/a)</td><td>517.94 (n/a)</td><td>532.30 (n/a)</td><td>434.10 (n/a)</td><td>75.08 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>519.20 (n/a)</td><td>429.06 (n/a)</td><td>458.30 (n/a)</td><td>310.10 (n/a)</td><td>88.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 <b>(+24.55%)</b></td><td>0.01 <b>(+26.94%)</b></td><td>0.01 (+9.09%)</td><td>0.01 (-0.19%)</td><td>0.01 <b>(+80.38%)</b></td><td>581.60 (+0.19%)</td><td>377.48 (-14.83%)</td><td>413.20 (-8.34%)</td><td>228.30 (-19.70%)</td><td>149.98 <b>(+36.36%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>580.50 (n/a)</td><td>443.22 (n/a)</td><td>450.80 (n/a)</td><td>284.30 (n/a)</td><td>109.99 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 <b>(-33.49%)</b></td><td>0.01 <b>(-27.96%)</b></td><td>0.01 <b>(-34.92%)</b></td><td>0.01 (+0.56%)</td><td>0.00 <b>(-63.21%)</b></td><td>595.20 (-0.57%)</td><td>509.38 <b>(+24.67%)</b></td><td>555.40 <b>(+53.68%)</b></td><td>378.20 <b>(+50.38%)</b></td><td>92.33 <b>(-45.06%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.60 (n/a)</td><td>408.58 (n/a)</td><td>361.40 (n/a)</td><td>251.50 (n/a)</td><td>168.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 <b>(-31.20%)</b></td><td>0.01 <b>(-51.19%)</b></td><td>0.01 <b>(-40.09%)</b></td><td>0.00 <b>(-75.40%)</b></td><td>0.01 (-3.95%)</td><td>2459.10 <b>(+306.46%)</b></td><td>1108.20 <b>(+255.26%)</b></td><td>454.20 <b>(+66.92%)</b></td><td>252.70 <b>(+45.31%)</b></td><td>1013.01 <b>(+494.24%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.00 (n/a)</td><td>311.94 (n/a)</td><td>272.10 (n/a)</td><td>173.90 (n/a)</td><td>170.47 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 <b>(-28.30%)</b></td><td>0.01 <b>(-24.62%)</b></td><td>0.01 <b>(-50.72%)</b></td><td>0.01 (-16.92%)</td><td>0.00 (-19.72%)</td><td>641.60 <b>(+20.38%)</b></td><td>470.36 <b>(+32.26%)</b></td><td>580.40 <b>(+102.94%)</b></td><td>263.00 <b>(+39.45%)</b></td><td>188.68 (+18.35%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>533.00 (n/a)</td><td>355.64 (n/a)</td><td>286.00 (n/a)</td><td>188.60 (n/a)</td><td>159.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 <b>(+54.33%)</b></td><td>0.01 <b>(+59.66%)</b></td><td>0.02 <b>(+128.66%)</b></td><td>0.01 (-7.19%)</td><td>0.01 <b>(+154.33%)</b></td><td>564.40 (+7.75%)</td><td>332.88 <b>(-27.54%)</b></td><td>226.00 <b>(-56.27%)</b></td><td>193.80 <b>(-35.21%)</b></td><td>170.98 <b>(+77.10%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>523.80 (n/a)</td><td>459.40 (n/a)</td><td>516.80 (n/a)</td><td>299.10 (n/a)</td><td>96.54 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (-3.88%)</td><td>0.01 <b>(+39.07%)</b></td><td>0.01 <b>(+73.92%)</b></td><td>0.01 <b>(+22.38%)</b></td><td>0.00 <b>(-31.23%)</b></td><td>500.80 (-18.29%)</td><td>357.00 <b>(-31.00%)</b></td><td>326.10 <b>(-42.51%)</b></td><td>307.20 (+4.07%)</td><td>80.92 <b>(-37.76%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>612.90 (n/a)</td><td>517.36 (n/a)</td><td>567.20 (n/a)</td><td>295.20 (n/a)</td><td>130.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (+4.90%)</td><td>0.03 (+0.11%)</td><td>0.03 (+2.09%)</td><td>0.02 (+14.16%)</td><td>0.01 (+9.03%)</td><td>461.70 (-12.39%)</td><td>331.54 (+0.20%)</td><td>293.80 (-2.03%)</td><td>224.90 (-4.66%)</td><td>111.07 (-6.52%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.00 (n/a)</td><td>330.88 (n/a)</td><td>299.90 (n/a)</td><td>235.90 (n/a)</td><td>118.81 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 <b>(+51.44%)</b></td><td>0.03 <b>(+22.04%)</b></td><td>0.03 (-2.28%)</td><td>0.02 (+19.96%)</td><td>0.01 <b>(+30.55%)</b></td><td>494.50 (-16.64%)</td><td>277.56 (-18.39%)</td><td>240.10 (+2.34%)</td><td>150.30 <b>(-33.96%)</b></td><td>129.04 <b>(-20.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.20 (n/a)</td><td>340.12 (n/a)</td><td>234.60 (n/a)</td><td>227.60 (n/a)</td><td>161.87 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (+0.52%)</td><td>0.03 (-1.56%)</td><td>0.03 (-4.40%)</td><td>0.02 (+10.40%)</td><td>0.01 (-12.43%)</td><td>492.90 (-9.43%)</td><td>313.26 (-1.14%)</td><td>272.20 (+4.61%)</td><td>236.40 (-0.55%)</td><td>103.06 (-19.99%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.20 (n/a)</td><td>316.88 (n/a)</td><td>260.20 (n/a)</td><td>237.70 (n/a)</td><td>128.81 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (-17.45%)</td><td>0.03 (-4.03%)</td><td>0.03 (+4.27%)</td><td>0.02 (+5.85%)</td><td>0.01 <b>(-20.40%)</b></td><td>532.60 (-5.52%)</td><td>350.24 (-1.46%)</td><td>253.70 (-4.12%)</td><td>207.20 <b>(+21.10%)</b></td><td>162.48 (-11.77%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.70 (n/a)</td><td>355.44 (n/a)</td><td>264.60 (n/a)</td><td>171.10 (n/a)</td><td>184.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (+15.07%)</td><td>0.03 (+13.74%)</td><td>0.03 (+3.58%)</td><td>0.01 <b>(+41.44%)</b></td><td>0.01 (-7.79%)</td><td>587.60 <b>(-29.30%)</b></td><td>355.48 (-19.36%)</td><td>279.90 (-3.45%)</td><td>229.20 (-13.08%)</td><td>148.61 <b>(-40.00%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>831.10 (n/a)</td><td>440.84 (n/a)</td><td>289.90 (n/a)</td><td>263.70 (n/a)</td><td>247.67 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 <b>(+24.90%)</b></td><td>0.02 (+0.30%)</td><td>0.02 <b>(-25.94%)</b></td><td>0.01 <b>(+23.06%)</b></td><td>0.01 (+15.78%)</td><td>650.50 (-18.74%)</td><td>434.84 (-2.21%)</td><td>432.50 <b>(+35.03%)</b></td><td>208.00 (-19.94%)</td><td>184.27 <b>(-21.59%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>800.50 (n/a)</td><td>444.68 (n/a)</td><td>320.30 (n/a)</td><td>259.80 (n/a)</td><td>235.01 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (-13.38%)</td><td>0.02 (-2.17%)</td><td>0.02 (-3.03%)</td><td>0.01 <b>(+197.57%)</b></td><td>0.01 <b>(-42.57%)</b></td><td>617.00 <b>(-66.40%)</b></td><td>423.90 <b>(-35.78%)</b></td><td>419.40 (+3.12%)</td><td>239.00 (+15.46%)</td><td>135.56 <b>(-79.85%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1836.10 (n/a)</td><td>660.08 (n/a)</td><td>406.70 (n/a)</td><td>207.00 (n/a)</td><td>672.67 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (-9.32%)</td><td>0.02 (+16.67%)</td><td>0.02 <b>(+31.53%)</b></td><td>0.01 <b>(+22.33%)</b></td><td>0.00 <b>(-41.81%)</b></td><td>572.70 (-18.26%)</td><td>445.84 (-18.24%)</td><td>438.00 <b>(-23.97%)</b></td><td>350.70 (+10.28%)</td><td>80.18 <b>(-43.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>700.60 (n/a)</td><td>545.32 (n/a)</td><td>576.10 (n/a)</td><td>318.00 (n/a)</td><td>140.76 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 <b>(+28.99%)</b></td><td>0.05 (+4.90%)</td><td>0.04 <b>(-36.96%)</b></td><td>0.03 <b>(+20.94%)</b></td><td>0.02 <b>(+40.64%)</b></td><td>505.10 (-17.31%)</td><td>373.44 (-1.50%)</td><td>455.70 <b>(+58.61%)</b></td><td>205.10 <b>(-22.49%)</b></td><td>141.62 (-6.94%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>610.80 (n/a)</td><td>379.12 (n/a)</td><td>287.30 (n/a)</td><td>264.60 (n/a)</td><td>152.18 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (-5.44%)</td><td>0.03 <b>(-26.83%)</b></td><td>0.03 (-17.10%)</td><td>0.01 <b>(-52.64%)</b></td><td>0.02 (-1.11%)</td><td>1354.80 <b>(+111.16%)</b></td><td>655.18 <b>(+56.09%)</b></td><td>565.10 <b>(+20.62%)</b></td><td>248.60 (+5.74%)</td><td>413.48 <b>(+140.18%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>641.60 (n/a)</td><td>419.74 (n/a)</td><td>468.50 (n/a)</td><td>235.10 (n/a)</td><td>172.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (+12.68%)</td><td>0.06 <b>(+22.92%)</b></td><td>0.07 (+18.74%)</td><td>0.03 (+2.91%)</td><td>0.02 (+6.00%)</td><td>499.90 (-2.82%)</td><td>290.34 (-18.58%)</td><td>241.00 (-15.76%)</td><td>218.40 (-11.22%)</td><td>117.81 (-4.87%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>514.40 (n/a)</td><td>356.58 (n/a)</td><td>286.10 (n/a)</td><td>246.00 (n/a)</td><td>123.84 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (-3.80%)</td><td>0.05 (+5.39%)</td><td>0.06 <b>(+68.62%)</b></td><td>0.03 (+0.93%)</td><td>0.02 (-13.62%)</td><td>516.50 (-0.94%)</td><td>341.10 (-7.40%)</td><td>260.20 <b>(-40.70%)</b></td><td>210.90 (+3.94%)</td><td>140.64 (-3.46%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>521.40 (n/a)</td><td>368.36 (n/a)</td><td>438.80 (n/a)</td><td>202.90 (n/a)</td><td>145.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (+7.26%)</td><td>0.05 (-7.44%)</td><td>0.04 <b>(-25.77%)</b></td><td>0.04 (+0.59%)</td><td>0.02 <b>(+35.97%)</b></td><td>459.00 (-0.61%)</td><td>355.20 (+10.88%)</td><td>401.50 <b>(+34.69%)</b></td><td>229.20 (-6.75%)</td><td>97.43 (+18.34%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>461.80 (n/a)</td><td>320.34 (n/a)</td><td>298.10 (n/a)</td><td>245.80 (n/a)</td><td>82.33 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (+9.19%)</td><td>0.04 <b>(+24.33%)</b></td><td>0.04 <b>(+22.27%)</b></td><td>0.03 (+6.80%)</td><td>0.01 <b>(+25.06%)</b></td><td>587.70 (-6.36%)</td><td>428.98 (-18.10%)</td><td>458.90 (-18.21%)</td><td>295.00 (-8.41%)</td><td>126.47 (+7.21%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>627.60 (n/a)</td><td>523.76 (n/a)</td><td>561.10 (n/a)</td><td>322.10 (n/a)</td><td>117.97 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (-8.83%)</td><td>0.09 (-6.39%)</td><td>0.07 (-12.44%)</td><td>0.05 (-10.22%)</td><td>0.04 (-8.17%)</td><td>610.40 (+11.37%)</td><td>404.36 (+6.49%)</td><td>453.80 (+14.19%)</td><td>246.20 (+9.67%)</td><td>155.35 (+6.91%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>548.10 (n/a)</td><td>379.70 (n/a)</td><td>397.40 (n/a)</td><td>224.50 (n/a)</td><td>145.31 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (-0.17%)</td><td>0.11 (+8.45%)</td><td>0.13 (+14.12%)</td><td>0.07 <b>(+26.70%)</b></td><td>0.03 (-19.00%)</td><td>439.80 <b>(-21.07%)</b></td><td>306.36 (-12.95%)</td><td>250.40 (-12.36%)</td><td>227.10 (+0.13%)</td><td>94.38 <b>(-35.31%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>557.20 (n/a)</td><td>351.92 (n/a)</td><td>285.70 (n/a)</td><td>226.80 (n/a)</td><td>145.91 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (+10.87%)</td><td>0.11 <b>(+26.17%)</b></td><td>0.14 <b>(+39.57%)</b></td><td>0.06 <b>(+20.52%)</b></td><td>0.04 (+18.14%)</td><td>544.80 (-17.03%)</td><td>334.04 <b>(-20.74%)</b></td><td>242.70 <b>(-28.36%)</b></td><td>218.50 (-9.82%)</td><td>146.80 (-16.81%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>656.60 (n/a)</td><td>421.46 (n/a)</td><td>338.80 (n/a)</td><td>242.30 (n/a)</td><td>176.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (+2.57%)</td><td>0.08 <b>(-21.12%)</b></td><td>0.09 <b>(-28.06%)</b></td><td>0.02 <b>(-47.00%)</b></td><td>0.05 (+13.79%)</td><td>2104.00 <b>(+88.67%)</b></td><td>721.98 <b>(+64.53%)</b></td><td>376.40 <b>(+39.00%)</b></td><td>241.80 (-2.50%)</td><td>785.25 <b>(+107.44%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1115.20 (n/a)</td><td>438.82 (n/a)</td><td>270.80 (n/a)</td><td>248.00 (n/a)</td><td>378.55 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.21 <b>(+72.01%)</b></td><td>0.11 <b>(+48.52%)</b></td><td>0.10 <b>(+49.72%)</b></td><td>0.07 <b>(+300.60%)</b></td><td>0.06 <b>(+37.55%)</b></td><td>473.10 <b>(-75.04%)</b></td><td>341.44 <b>(-50.60%)</b></td><td>312.40 <b>(-33.22%)</b></td><td>159.80 <b>(-41.85%)</b></td><td>133.38 <b>(-80.41%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1895.20 (n/a)</td><td>691.18 (n/a)</td><td>467.80 (n/a)</td><td>274.80 (n/a)</td><td>680.92 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (-1.11%)</td><td>0.01 (-10.87%)</td><td>0.01 (+0.47%)</td><td>0.00 <b>(-73.24%)</b></td><td>0.01 <b>(+47.89%)</b></td><td>1952.70 <b>(+273.72%)</b></td><td>652.62 <b>(+81.69%)</b></td><td>292.50 (-0.48%)</td><td>243.50 (+1.12%)</td><td>733.45 <b>(+475.38%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.50 (n/a)</td><td>359.20 (n/a)</td><td>293.90 (n/a)</td><td>240.80 (n/a)</td><td>127.47 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (-0.20%)</td><td>0.02 <b>(+21.86%)</b></td><td>0.02 <b>(+46.40%)</b></td><td>0.01 (+11.08%)</td><td>0.00 (-19.04%)</td><td>458.40 (-9.98%)</td><td>282.48 <b>(-21.44%)</b></td><td>243.00 <b>(-31.70%)</b></td><td>219.20 (+0.23%)</td><td>100.19 <b>(-24.42%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.20 (n/a)</td><td>359.58 (n/a)</td><td>355.80 (n/a)</td><td>218.70 (n/a)</td><td>132.57 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 <b>(+22.82%)</b></td><td>0.01 (+5.76%)</td><td>0.02 (+8.63%)</td><td>0.00 <b>(-69.25%)</b></td><td>0.01 <b>(+56.04%)</b></td><td>2158.70 <b>(+225.20%)</b></td><td>646.12 <b>(+71.98%)</b></td><td>247.10 (-7.94%)</td><td>197.00 (-18.60%)</td><td>848.98 <b>(+365.44%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>663.80 (n/a)</td><td>375.70 (n/a)</td><td>268.40 (n/a)</td><td>242.00 (n/a)</td><td>182.40 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (-7.40%)</td><td>0.01 (+6.46%)</td><td>0.01 (-1.78%)</td><td>0.01 <b>(+116.01%)</b></td><td>0.00 <b>(-28.86%)</b></td><td>484.00 <b>(-53.70%)</b></td><td>376.26 <b>(-23.77%)</b></td><td>431.60 (+1.79%)</td><td>244.40 (+8.00%)</td><td>121.80 <b>(-63.53%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1045.40 (n/a)</td><td>493.60 (n/a)</td><td>424.00 (n/a)</td><td>226.30 (n/a)</td><td>333.96 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (+3.30%)</td><td>0.01 (-5.18%)</td><td>0.01 <b>(-30.22%)</b></td><td>0.01 (+9.82%)</td><td>0.01 (+3.79%)</td><td>593.50 (-8.94%)</td><td>407.94 (+4.55%)</td><td>429.20 <b>(+43.31%)</b></td><td>232.50 (-3.21%)</td><td>166.01 (-9.65%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>651.80 (n/a)</td><td>390.18 (n/a)</td><td>299.50 (n/a)</td><td>240.20 (n/a)</td><td>183.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (-6.18%)</td><td>0.01 (-5.44%)</td><td>0.01 (-6.30%)</td><td>0.01 (+4.08%)</td><td>0.00 (-1.84%)</td><td>514.00 (-3.93%)</td><td>379.50 (+5.64%)</td><td>390.90 (+6.72%)</td><td>255.40 (+6.59%)</td><td>110.48 (-1.86%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>535.00 (n/a)</td><td>359.24 (n/a)</td><td>366.30 (n/a)</td><td>239.60 (n/a)</td><td>112.57 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (-4.29%)</td><td>0.01 (-7.33%)</td><td>0.02 (+9.63%)</td><td>0.01 (-7.16%)</td><td>0.00 (+11.90%)</td><td>669.30 (+7.71%)</td><td>379.26 (+11.18%)</td><td>264.60 (-8.79%)</td><td>254.20 (+4.48%)</td><td>181.43 (+14.42%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>621.40 (n/a)</td><td>341.12 (n/a)</td><td>290.10 (n/a)</td><td>243.30 (n/a)</td><td>158.56 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (+15.12%)</td><td>0.01 <b>(+33.56%)</b></td><td>0.02 <b>(+98.86%)</b></td><td>0.01 <b>(+99.76%)</b></td><td>0.01 (-15.20%)</td><td>535.70 <b>(-49.94%)</b></td><td>333.66 <b>(-37.95%)</b></td><td>268.10 <b>(-49.72%)</b></td><td>201.70 (-13.14%)</td><td>141.08 <b>(-58.64%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1070.20 (n/a)</td><td>537.70 (n/a)</td><td>533.20 (n/a)</td><td>232.20 (n/a)</td><td>341.08 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (-14.64%)</td><td>0.01 (-19.11%)</td><td>0.01 <b>(-22.36%)</b></td><td>0.00 <b>(-71.79%)</b></td><td>0.01 <b>(+29.10%)</b></td><td>1915.90 <b>(+254.47%)</b></td><td>669.92 <b>(+88.30%)</b></td><td>439.90 <b>(+28.81%)</b></td><td>251.40 (+17.15%)</td><td>702.27 <b>(+483.58%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>540.50 (n/a)</td><td>355.78 (n/a)</td><td>341.50 (n/a)</td><td>214.60 (n/a)</td><td>120.34 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (+6.19%)</td><td>0.01 (+0.65%)</td><td>0.01 (-5.02%)</td><td>0.01 (-19.36%)</td><td>0.00 <b>(+36.95%)</b></td><td>619.40 <b>(+24.00%)</b></td><td>401.98 (+6.58%)</td><td>390.70 (+5.28%)</td><td>239.80 (-5.81%)</td><td>167.40 <b>(+47.96%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>499.50 (n/a)</td><td>377.18 (n/a)</td><td>371.10 (n/a)</td><td>254.60 (n/a)</td><td>113.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 <b>(+22.83%)</b></td><td>0.01 (-1.41%)</td><td>0.01 <b>(-35.97%)</b></td><td>0.01 (+15.66%)</td><td>0.01 <b>(+25.96%)</b></td><td>542.80 (-13.54%)</td><td>413.02 (+2.26%)</td><td>475.80 <b>(+56.20%)</b></td><td>182.70 (-18.58%)</td><td>156.32 (-15.22%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.80 (n/a)</td><td>403.90 (n/a)</td><td>304.60 (n/a)</td><td>224.40 (n/a)</td><td>184.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (+18.87%)</td><td>0.01 (+16.21%)</td><td>0.01 (+14.42%)</td><td>0.01 (+2.63%)</td><td>0.00 <b>(+47.28%)</b></td><td>586.40 (-2.56%)</td><td>410.38 (-10.21%)</td><td>442.40 (-12.59%)</td><td>259.20 (-15.87%)</td><td>142.51 (+16.20%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>601.80 (n/a)</td><td>457.04 (n/a)</td><td>506.10 (n/a)</td><td>308.10 (n/a)</td><td>122.64 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (-4.51%)</td><td>0.02 (-1.53%)</td><td>0.03 (-0.80%)</td><td>0.00 (-2.95%)</td><td>0.01 (-7.89%)</td><td>1947.40 (+3.04%)</td><td>633.16 (+0.23%)</td><td>268.90 (+0.79%)</td><td>226.40 (+4.72%)</td><td>741.26 (+3.45%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1889.90 (n/a)</td><td>631.70 (n/a)</td><td>266.80 (n/a)</td><td>216.20 (n/a)</td><td>716.55 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (+7.03%)</td><td>0.03 (-3.73%)</td><td>0.03 (-1.23%)</td><td>0.02 (-3.73%)</td><td>0.01 <b>(+30.38%)</b></td><td>516.60 (+3.88%)</td><td>337.64 (+8.20%)</td><td>291.90 (+1.28%)</td><td>209.90 (-6.59%)</td><td>130.43 <b>(+21.30%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.30 (n/a)</td><td>312.06 (n/a)</td><td>288.20 (n/a)</td><td>224.70 (n/a)</td><td>107.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (-8.54%)</td><td>0.03 (+13.32%)</td><td>0.03 <b>(+57.51%)</b></td><td>0.02 <b>(+35.10%)</b></td><td>0.01 <b>(-35.32%)</b></td><td>450.80 <b>(-25.98%)</b></td><td>332.16 <b>(-20.58%)</b></td><td>294.10 <b>(-36.52%)</b></td><td>240.90 (+9.35%)</td><td>95.18 <b>(-45.57%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.00 (n/a)</td><td>418.24 (n/a)</td><td>463.30 (n/a)</td><td>220.30 (n/a)</td><td>174.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (-0.44%)</td><td>0.02 (-9.31%)</td><td>0.03 (-4.32%)</td><td>0.01 (-19.78%)</td><td>0.01 <b>(+32.74%)</b></td><td>625.80 <b>(+24.66%)</b></td><td>375.26 (+17.69%)</td><td>292.30 (+4.54%)</td><td>241.30 (+0.42%)</td><td>163.85 <b>(+55.90%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.00 (n/a)</td><td>318.86 (n/a)</td><td>279.60 (n/a)</td><td>240.30 (n/a)</td><td>105.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (-7.03%)</td><td>0.03 <b>(+20.95%)</b></td><td>0.03 <b>(+45.05%)</b></td><td>0.01 (+2.74%)</td><td>0.01 (-2.78%)</td><td>571.90 (-2.67%)</td><td>375.70 (-16.83%)</td><td>309.40 <b>(-31.06%)</b></td><td>231.60 (+7.57%)</td><td>158.70 (+5.62%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.60 (n/a)</td><td>451.70 (n/a)</td><td>448.80 (n/a)</td><td>215.30 (n/a)</td><td>150.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (-3.97%)</td><td>0.02 (-8.99%)</td><td>0.02 (-18.46%)</td><td>0.01 (-12.45%)</td><td>0.01 <b>(-20.27%)</b></td><td>639.70 (+14.21%)</td><td>393.78 (+6.29%)</td><td>380.70 <b>(+22.65%)</b></td><td>241.10 (+4.10%)</td><td>151.12 (-2.70%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.10 (n/a)</td><td>370.46 (n/a)</td><td>310.40 (n/a)</td><td>231.60 (n/a)</td><td>155.31 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 <b>(+45.07%)</b></td><td>0.02 (-2.31%)</td><td>0.02 (+1.96%)</td><td>0.00 <b>(-71.58%)</b></td><td>0.01 <b>(+149.37%)</b></td><td>2128.30 <b>(+251.90%)</b></td><td>779.52 <b>(+59.65%)</b></td><td>513.80 (-1.93%)</td><td>245.80 <b>(-31.07%)</b></td><td>762.67 <b>(+593.72%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>604.80 (n/a)</td><td>488.26 (n/a)</td><td>523.90 (n/a)</td><td>356.60 (n/a)</td><td>109.94 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (+0.46%)</td><td>0.02 (-2.57%)</td><td>0.03 (+5.23%)</td><td>0.01 <b>(-55.36%)</b></td><td>0.01 <b>(+29.63%)</b></td><td>1343.50 <b>(+123.99%)</b></td><td>528.56 <b>(+33.44%)</b></td><td>285.70 (-4.99%)</td><td>243.40 (-0.45%)</td><td>466.73 <b>(+181.62%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.80 (n/a)</td><td>396.10 (n/a)</td><td>300.70 (n/a)</td><td>244.50 (n/a)</td><td>165.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (+10.65%)</td><td>0.03 (+19.82%)</td><td>0.03 (+3.38%)</td><td>0.02 <b>(+28.08%)</b></td><td>0.01 <b>(-20.37%)</b></td><td>483.10 <b>(-21.93%)</b></td><td>325.94 <b>(-22.46%)</b></td><td>289.70 (-3.27%)</td><td>248.70 (-9.63%)</td><td>95.95 <b>(-45.78%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.80 (n/a)</td><td>420.36 (n/a)</td><td>299.50 (n/a)</td><td>275.20 (n/a)</td><td>176.94 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (-0.81%)</td><td>0.02 (+5.53%)</td><td>0.02 <b>(+45.25%)</b></td><td>0.01 (-4.05%)</td><td>0.01 (-5.26%)</td><td>564.10 (+4.21%)</td><td>401.90 (-5.51%)</td><td>342.90 <b>(-31.16%)</b></td><td>275.60 (+0.80%)</td><td>135.99 (+2.73%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.30 (n/a)</td><td>425.34 (n/a)</td><td>498.10 (n/a)</td><td>273.40 (n/a)</td><td>132.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (-10.78%)</td><td>0.02 <b>(-23.14%)</b></td><td>0.01 <b>(-43.41%)</b></td><td>0.01 <b>(+58.87%)</b></td><td>0.01 <b>(-38.26%)</b></td><td>624.80 <b>(-37.05%)</b></td><td>508.92 (+11.49%)</td><td>564.70 <b>(+76.74%)</b></td><td>322.20 (+12.07%)</td><td>130.20 <b>(-57.01%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>992.60 (n/a)</td><td>456.46 (n/a)</td><td>319.50 (n/a)</td><td>287.50 (n/a)</td><td>302.87 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (+17.03%)</td><td>0.02 <b>(+27.44%)</b></td><td>0.02 <b>(+23.85%)</b></td><td>0.01 <b>(+241.05%)</b></td><td>0.01 <b>(-25.18%)</b></td><td>552.30 <b>(-70.68%)</b></td><td>415.34 <b>(-43.30%)</b></td><td>434.00 (-19.26%)</td><td>269.20 (-14.57%)</td><td>111.11 <b>(-82.96%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1883.70 (n/a)</td><td>732.56 (n/a)</td><td>537.50 (n/a)</td><td>315.10 (n/a)</td><td>651.96 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 <b>(+45.40%)</b></td><td>0.05 <b>(+37.04%)</b></td><td>0.06 <b>(+65.94%)</b></td><td>0.02 <b>(-34.58%)</b></td><td>0.02 <b>(+251.38%)</b></td><td>723.00 <b>(+52.85%)</b></td><td>367.54 (-15.98%)</td><td>280.40 <b>(-39.74%)</b></td><td>243.80 <b>(-31.25%)</b></td><td>200.23 <b>(+300.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>473.00 (n/a)</td><td>437.46 (n/a)</td><td>465.30 (n/a)</td><td>354.60 (n/a)</td><td>50.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 <b>(-27.73%)</b></td><td>0.04 <b>(-21.35%)</b></td><td>0.03 <b>(-41.02%)</b></td><td>0.03 (-0.95%)</td><td>0.01 <b>(-29.57%)</b></td><td>572.60 (+0.97%)</td><td>432.96 <b>(+22.55%)</b></td><td>491.50 <b>(+69.54%)</b></td><td>290.60 <b>(+38.38%)</b></td><td>128.68 (-8.34%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>567.10 (n/a)</td><td>353.30 (n/a)</td><td>289.90 (n/a)</td><td>210.00 (n/a)</td><td>140.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (+3.80%)</td><td>0.06 <b>(+20.84%)</b></td><td>0.06 (+1.80%)</td><td>0.05 <b>(+75.85%)</b></td><td>0.01 <b>(-52.73%)</b></td><td>349.90 <b>(-43.13%)</b></td><td>289.30 <b>(-28.17%)</b></td><td>293.80 (-1.77%)</td><td>229.30 (-3.66%)</td><td>44.83 <b>(-75.83%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>615.30 (n/a)</td><td>402.74 (n/a)</td><td>299.10 (n/a)</td><td>238.00 (n/a)</td><td>185.47 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (-0.81%)</td><td>0.05 (+5.09%)</td><td>0.06 <b>(+60.82%)</b></td><td>0.02 <b>(-31.70%)</b></td><td>0.02 (+9.36%)</td><td>748.90 <b>(+46.41%)</b></td><td>404.84 (+1.63%)</td><td>297.70 <b>(-37.81%)</b></td><td>240.10 (+0.80%)</td><td>208.38 <b>(+62.64%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>511.50 (n/a)</td><td>398.36 (n/a)</td><td>478.70 (n/a)</td><td>238.20 (n/a)</td><td>128.12 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (-1.84%)</td><td>0.05 <b>(-29.81%)</b></td><td>0.03 <b>(-48.91%)</b></td><td>0.03 <b>(-50.54%)</b></td><td>0.02 <b>(+115.49%)</b></td><td>598.00 <b>(+102.16%)</b></td><td>412.38 <b>(+63.69%)</b></td><td>468.80 <b>(+95.74%)</b></td><td>207.30 (+1.92%)</td><td>163.92 <b>(+330.67%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>295.80 (n/a)</td><td>251.92 (n/a)</td><td>239.50 (n/a)</td><td>203.40 (n/a)</td><td>38.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (+1.25%)</td><td>0.06 (+5.06%)</td><td>0.06 (+9.65%)</td><td>0.03 (+0.64%)</td><td>0.01 (+5.23%)</td><td>549.50 (-0.63%)</td><td>323.12 (-4.10%)</td><td>274.50 (-8.80%)</td><td>241.30 (-1.23%)</td><td>127.42 (+3.30%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>553.00 (n/a)</td><td>336.94 (n/a)</td><td>301.00 (n/a)</td><td>244.30 (n/a)</td><td>123.36 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (-5.14%)</td><td>0.04 (+0.24%)</td><td>0.04 (+16.45%)</td><td>0.03 (+1.68%)</td><td>0.01 (-15.42%)</td><td>594.50 (-1.64%)</td><td>423.64 (-3.18%)</td><td>429.60 (-14.13%)</td><td>277.00 (+5.40%)</td><td>139.84 (-11.38%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.40 (n/a)</td><td>437.56 (n/a)</td><td>500.30 (n/a)</td><td>262.80 (n/a)</td><td>157.79 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 <b>(+20.49%)</b></td><td>0.04 (-6.99%)</td><td>0.03 <b>(-32.23%)</b></td><td>0.01 <b>(-44.76%)</b></td><td>0.02 <b>(+66.67%)</b></td><td>1096.30 <b>(+81.03%)</b></td><td>534.80 <b>(+30.34%)</b></td><td>491.00 <b>(+47.54%)</b></td><td>243.20 (-17.00%)</td><td>339.14 <b>(+148.43%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>605.60 (n/a)</td><td>410.32 (n/a)</td><td>332.80 (n/a)</td><td>293.00 (n/a)</td><td>136.51 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (+19.32%)</td><td>0.05 (+12.13%)</td><td>0.06 (+7.88%)</td><td>0.03 (-3.77%)</td><td>0.02 (+14.84%)</td><td>561.70 (+3.90%)</td><td>343.14 (-10.24%)</td><td>284.20 (-7.31%)</td><td>207.70 (-16.18%)</td><td>137.05 (-3.52%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>540.60 (n/a)</td><td>382.30 (n/a)</td><td>306.60 (n/a)</td><td>247.80 (n/a)</td><td>142.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (+1.05%)</td><td>0.04 (-13.03%)</td><td>0.04 <b>(-24.73%)</b></td><td>0.03 (+3.37%)</td><td>0.02 (+11.39%)</td><td>540.00 (-3.26%)</td><td>398.14 (+15.95%)</td><td>399.20 <b>(+32.85%)</b></td><td>238.90 (-1.04%)</td><td>123.14 (-0.26%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>558.20 (n/a)</td><td>343.36 (n/a)</td><td>300.50 (n/a)</td><td>241.40 (n/a)</td><td>123.46 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (+2.22%)</td><td>0.04 (+13.09%)</td><td>0.04 (+9.56%)</td><td>0.03 (-2.59%)</td><td>0.01 (+8.78%)</td><td>644.10 (+2.66%)</td><td>440.82 (-10.40%)</td><td>450.80 (-8.71%)</td><td>283.10 (-2.18%)</td><td>144.65 (+9.02%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>627.40 (n/a)</td><td>492.00 (n/a)</td><td>493.80 (n/a)</td><td>289.40 (n/a)</td><td>132.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (+7.18%)</td><td>0.04 (+8.91%)</td><td>0.03 (-5.46%)</td><td>0.03 <b>(+296.38%)</b></td><td>0.02 <b>(-24.65%)</b></td><td>620.20 <b>(-74.77%)</b></td><td>460.16 <b>(-43.47%)</b></td><td>510.30 (+5.78%)</td><td>268.40 (-6.71%)</td><td>159.59 <b>(-82.77%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2458.50 (n/a)</td><td>814.08 (n/a)</td><td>482.40 (n/a)</td><td>287.70 (n/a)</td><td>926.33 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.19 <b>(+48.11%)</b></td><td>0.13 <b>(+41.46%)</b></td><td>0.13 <b>(+69.14%)</b></td><td>0.06 (+6.27%)</td><td>0.05 <b>(+57.36%)</b></td><td>508.10 (-5.89%)</td><td>293.42 <b>(-26.05%)</b></td><td>261.70 <b>(-40.87%)</b></td><td>168.10 <b>(-32.49%)</b></td><td>127.53 (+7.26%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>539.90 (n/a)</td><td>396.78 (n/a)</td><td>442.60 (n/a)</td><td>249.00 (n/a)</td><td>118.90 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (+6.34%)</td><td>0.12 (+6.44%)</td><td>0.13 (+7.10%)</td><td>0.07 (+9.30%)</td><td>0.03 (+6.90%)</td><td>440.60 (-8.51%)</td><td>290.66 (-6.27%)</td><td>253.90 (-6.62%)</td><td>226.70 (-5.93%)</td><td>89.17 (-10.18%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>481.60 (n/a)</td><td>310.12 (n/a)</td><td>271.90 (n/a)</td><td>241.00 (n/a)</td><td>99.28 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (-9.94%)</td><td>0.10 (+1.04%)</td><td>0.09 (+17.33%)</td><td>0.06 (+14.11%)</td><td>0.04 (-15.92%)</td><td>554.70 (-12.37%)</td><td>385.96 (-5.21%)</td><td>382.70 (-14.77%)</td><td>217.80 (+11.07%)</td><td>147.83 (-14.75%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>633.00 (n/a)</td><td>407.18 (n/a)</td><td>449.00 (n/a)</td><td>196.10 (n/a)</td><td>173.41 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (+9.12%)</td><td>0.09 (-5.24%)</td><td>0.09 (+19.01%)</td><td>0.05 <b>(-23.94%)</b></td><td>0.04 <b>(+25.17%)</b></td><td>643.70 <b>(+31.47%)</b></td><td>427.54 (+12.87%)</td><td>370.20 (-15.98%)</td><td>204.60 (-8.37%)</td><td>174.80 <b>(+50.51%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>489.60 (n/a)</td><td>378.80 (n/a)</td><td>440.60 (n/a)</td><td>223.30 (n/a)</td><td>116.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.17 (+0.30%)</td><td>0.08 <b>(-31.66%)</b></td><td>0.06 <b>(-52.92%)</b></td><td>0.05 (-10.17%)</td><td>0.05 (+5.86%)</td><td>669.00 (+11.31%)</td><td>521.08 <b>(+50.87%)</b></td><td>583.20 <b>(+112.38%)</b></td><td>190.30 (-0.31%)</td><td>189.08 (+8.84%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>601.00 (n/a)</td><td>345.38 (n/a)</td><td>274.60 (n/a)</td><td>190.90 (n/a)</td><td>173.72 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 <b>(-36.65%)</b></td><td>0.08 (-13.87%)</td><td>0.08 (+17.84%)</td><td>0.08 <b>(+35.98%)</b></td><td>0.01 <b>(-77.16%)</b></td><td>434.50 <b>(-26.47%)</b></td><td>405.92 (-1.41%)</td><td>426.00 (-15.14%)</td><td>326.00 <b>(+57.87%)</b></td><td>45.34 <b>(-73.50%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>590.90 (n/a)</td><td>411.74 (n/a)</td><td>502.00 (n/a)</td><td>206.50 (n/a)</td><td>171.11 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (-13.74%)</td><td>0.10 (-0.12%)</td><td>0.11 <b>(+56.29%)</b></td><td>0.06 (+13.80%)</td><td>0.04 <b>(-32.83%)</b></td><td>549.10 (-12.13%)</td><td>361.90 (-9.66%)</td><td>306.10 <b>(-36.02%)</b></td><td>226.00 (+15.96%)</td><td>140.54 <b>(-25.31%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>624.90 (n/a)</td><td>400.58 (n/a)</td><td>478.40 (n/a)</td><td>194.90 (n/a)</td><td>188.16 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.11 <b>(+20.37%)</b></td><td>0.09 <b>(+26.64%)</b></td><td>0.10 <b>(+47.92%)</b></td><td>0.05 (-9.65%)</td><td>0.03 <b>(+79.03%)</b></td><td>666.80 (+10.67%)</td><td>408.92 (-15.93%)</td><td>327.90 <b>(-32.41%)</b></td><td>289.50 (-16.93%)</td><td>156.97 <b>(+70.53%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>602.50 (n/a)</td><td>486.42 (n/a)</td><td>485.10 (n/a)</td><td>348.50 (n/a)</td><td>92.05 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (-14.28%)</td><td>0.07 <b>(-20.94%)</b></td><td>0.07 <b>(-29.19%)</b></td><td>0.06 (+6.46%)</td><td>0.01 <b>(-40.66%)</b></td><td>557.90 (-6.06%)</td><td>482.98 <b>(+20.84%)</b></td><td>499.60 <b>(+41.21%)</b></td><td>340.50 (+16.65%)</td><td>83.15 <b>(-35.73%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>593.90 (n/a)</td><td>399.68 (n/a)</td><td>353.80 (n/a)</td><td>291.90 (n/a)</td><td>129.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.21 <b>(+60.83%)</b></td><td>0.12 <b>(+52.77%)</b></td><td>0.11 (+3.24%)</td><td>0.06 <b>(+346.27%)</b></td><td>0.06 (+1.43%)</td><td>535.00 <b>(-77.59%)</b></td><td>309.82 <b>(-63.69%)</b></td><td>289.20 (-3.12%)</td><td>154.70 <b>(-37.82%)</b></td><td>140.01 <b>(-84.82%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2387.40 (n/a)</td><td>853.30 (n/a)</td><td>298.50 (n/a)</td><td>248.80 (n/a)</td><td>922.23 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (+8.53%)</td><td>0.06 (-1.59%)</td><td>0.06 (-2.87%)</td><td>0.04 <b>(-24.98%)</b></td><td>0.02 <b>(+85.85%)</b></td><td>849.20 <b>(+33.29%)</b></td><td>583.90 (+10.99%)</td><td>546.50 (+2.96%)</td><td>362.30 (-7.86%)</td><td>220.35 <b>(+127.03%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>637.10 (n/a)</td><td>526.08 (n/a)</td><td>530.80 (n/a)</td><td>393.20 (n/a)</td><td>97.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (+6.18%)</td><td>0.08 (-3.92%)</td><td>0.06 <b>(-27.86%)</b></td><td>0.06 (-1.57%)</td><td>0.03 <b>(+21.98%)</b></td><td>592.00 (+1.60%)</td><td>447.10 (+7.77%)</td><td>530.60 <b>(+38.61%)</b></td><td>238.60 (-5.80%)</td><td>151.31 (+16.59%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>582.70 (n/a)</td><td>414.88 (n/a)</td><td>382.80 (n/a)</td><td>253.30 (n/a)</td><td>129.78 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 <b>(+28.46%)</b></td><td>0.01 (+8.34%)</td><td>0.01 (-1.52%)</td><td>0.01 (-5.81%)</td><td>0.01 <b>(+37.77%)</b></td><td>577.80 (+6.17%)</td><td>359.28 (-3.51%)</td><td>306.10 (+1.53%)</td><td>165.80 <b>(-22.12%)</b></td><td>158.41 (+4.46%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>544.20 (n/a)</td><td>372.36 (n/a)</td><td>301.50 (n/a)</td><td>212.90 (n/a)</td><td>151.65 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 <b>(+57.19%)</b></td><td>0.02 <b>(+22.84%)</b></td><td>0.02 (+1.17%)</td><td>0.01 <b>(-21.24%)</b></td><td>0.01 <b>(+80.76%)</b></td><td>582.20 <b>(+26.98%)</b></td><td>310.18 (-10.61%)</td><td>272.20 (-1.16%)</td><td>172.80 <b>(-36.40%)</b></td><td>157.57 <b>(+57.57%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>458.50 (n/a)</td><td>346.98 (n/a)</td><td>275.40 (n/a)</td><td>271.70 (n/a)</td><td>100.00 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (-1.63%)</td><td>0.01 (+7.44%)</td><td>0.01 (+7.39%)</td><td>0.01 (+3.06%)</td><td>0.00 (-4.74%)</td><td>752.90 (-2.98%)</td><td>510.32 (-7.58%)</td><td>532.10 (-6.88%)</td><td>282.30 (+1.66%)</td><td>179.02 (-1.66%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>776.00 (n/a)</td><td>552.16 (n/a)</td><td>571.40 (n/a)</td><td>277.70 (n/a)</td><td>182.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 <b>(-42.02%)</b></td><td>0.01 <b>(-38.74%)</b></td><td>0.01 (-9.43%)</td><td>0.00 <b>(-79.19%)</b></td><td>0.00 <b>(-28.19%)</b></td><td>2497.40 <b>(+380.45%)</b></td><td>899.90 <b>(+124.27%)</b></td><td>519.00 (+10.40%)</td><td>419.80 <b>(+72.47%)</b></td><td>895.82 <b>(+549.47%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>519.80 (n/a)</td><td>401.26 (n/a)</td><td>470.10 (n/a)</td><td>243.40 (n/a)</td><td>137.93 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (+6.90%)</td><td>0.01 (-15.13%)</td><td>0.01 <b>(-39.08%)</b></td><td>0.01 (-10.70%)</td><td>0.00 <b>(+28.03%)</b></td><td>578.40 (+11.98%)</td><td>432.34 <b>(+23.51%)</b></td><td>477.60 <b>(+64.12%)</b></td><td>251.40 (-6.47%)</td><td>148.50 <b>(+38.68%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>516.50 (n/a)</td><td>350.04 (n/a)</td><td>291.00 (n/a)</td><td>268.80 (n/a)</td><td>107.08 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 <b>(+31.03%)</b></td><td>0.01 <b>(-22.86%)</b></td><td>0.01 <b>(-46.59%)</b></td><td>0.01 <b>(-39.84%)</b></td><td>0.01 <b>(+84.47%)</b></td><td>721.00 <b>(+66.21%)</b></td><td>491.68 <b>(+50.95%)</b></td><td>512.10 <b>(+87.24%)</b></td><td>184.00 <b>(-23.68%)</b></td><td>196.81 <b>(+103.92%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>433.80 (n/a)</td><td>325.72 (n/a)</td><td>273.50 (n/a)</td><td>241.10 (n/a)</td><td>96.51 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (-14.45%)</td><td>0.01 (-12.42%)</td><td>0.01 (+12.46%)</td><td>0.01 <b>(-27.01%)</b></td><td>0.00 (-18.56%)</td><td>795.50 <b>(+37.01%)</b></td><td>517.32 (+13.77%)</td><td>468.70 (-11.06%)</td><td>286.00 (+16.88%)</td><td>188.66 <b>(+24.07%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>580.60 (n/a)</td><td>454.70 (n/a)</td><td>527.00 (n/a)</td><td>244.70 (n/a)</td><td>152.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (-4.81%)</td><td>0.01 <b>(-21.56%)</b></td><td>0.01 (-15.31%)</td><td>0.00 <b>(-54.87%)</b></td><td>0.01 <b>(+27.81%)</b></td><td>1038.50 <b>(+121.62%)</b></td><td>576.22 <b>(+46.61%)</b></td><td>524.20 (+18.09%)</td><td>245.90 (+5.04%)</td><td>287.35 <b>(+192.59%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>468.60 (n/a)</td><td>393.04 (n/a)</td><td>443.90 (n/a)</td><td>234.10 (n/a)</td><td>98.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 <b>(-37.62%)</b></td><td>0.01 <b>(-21.36%)</b></td><td>0.01 (-9.52%)</td><td>0.01 (-11.54%)</td><td>0.00 <b>(-59.23%)</b></td><td>607.20 (+13.05%)</td><td>524.22 <b>(+20.89%)</b></td><td>531.70 (+10.52%)</td><td>397.20 <b>(+60.29%)</b></td><td>88.65 <b>(-21.21%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.10 (n/a)</td><td>433.62 (n/a)</td><td>481.10 (n/a)</td><td>247.80 (n/a)</td><td>112.50 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 <b>(+30.48%)</b></td><td>0.01 (+15.46%)</td><td>0.01 (+8.28%)</td><td>0.01 (+8.24%)</td><td>0.01 <b>(+39.29%)</b></td><td>563.90 (-7.62%)</td><td>406.36 (-9.74%)</td><td>423.30 (-7.66%)</td><td>211.70 <b>(-23.35%)</b></td><td>162.59 (+1.72%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.40 (n/a)</td><td>450.22 (n/a)</td><td>458.40 (n/a)</td><td>276.20 (n/a)</td><td>159.84 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (-16.62%)</td><td>0.01 (+0.83%)</td><td>0.01 (+17.15%)</td><td>0.01 <b>(+236.45%)</b></td><td>0.00 <b>(-52.08%)</b></td><td>569.20 <b>(-70.28%)</b></td><td>402.50 <b>(-39.31%)</b></td><td>367.30 (-14.64%)</td><td>289.20 (+19.90%)</td><td>119.81 <b>(-83.09%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1915.00 (n/a)</td><td>663.22 (n/a)</td><td>430.30 (n/a)</td><td>241.20 (n/a)</td><td>708.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (+6.81%)</td><td>0.02 (-8.35%)</td><td>0.02 <b>(-41.64%)</b></td><td>0.02 <b>(+280.25%)</b></td><td>0.01 <b>(-24.33%)</b></td><td>485.10 <b>(-73.70%)</b></td><td>376.96 <b>(-34.34%)</b></td><td>445.80 <b>(+71.33%)</b></td><td>230.70 (-6.41%)</td><td>128.18 <b>(-81.95%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1844.50 (n/a)</td><td>574.08 (n/a)</td><td>260.20 (n/a)</td><td>246.50 (n/a)</td><td>710.27 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (+13.78%)</td><td>0.04 (-7.19%)</td><td>0.03 <b>(-29.36%)</b></td><td>0.02 <b>(-21.91%)</b></td><td>0.02 <b>(+41.38%)</b></td><td>554.70 <b>(+28.05%)</b></td><td>376.58 (+15.68%)</td><td>369.50 <b>(+41.57%)</b></td><td>218.10 (-12.09%)</td><td>150.34 <b>(+54.02%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>433.20 (n/a)</td><td>325.54 (n/a)</td><td>261.00 (n/a)</td><td>248.10 (n/a)</td><td>97.61 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 <b>(-30.06%)</b></td><td>0.02 <b>(-38.42%)</b></td><td>0.02 <b>(-52.82%)</b></td><td>0.01 (+0.56%)</td><td>0.01 <b>(-29.85%)</b></td><td>577.90 (-0.55%)</td><td>465.50 <b>(+54.04%)</b></td><td>537.70 <b>(+112.03%)</b></td><td>221.10 <b>(+43.01%)</b></td><td>145.94 (-10.15%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.10 (n/a)</td><td>302.20 (n/a)</td><td>253.60 (n/a)</td><td>154.60 (n/a)</td><td>162.44 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (-2.87%)</td><td>0.03 (-0.71%)</td><td>0.04 (-6.68%)</td><td>0.02 (-3.11%)</td><td>0.01 (-2.79%)</td><td>599.90 (+3.22%)</td><td>358.58 (+0.53%)</td><td>286.60 (+7.18%)</td><td>241.40 (+2.99%)</td><td>151.35 (+1.86%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>581.20 (n/a)</td><td>356.68 (n/a)</td><td>267.40 (n/a)</td><td>234.40 (n/a)</td><td>148.59 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (-11.34%)</td><td>0.02 <b>(-25.90%)</b></td><td>0.02 <b>(-45.89%)</b></td><td>0.01 (-13.36%)</td><td>0.01 (-18.34%)</td><td>658.10 (+15.42%)</td><td>478.86 <b>(+30.22%)</b></td><td>541.50 <b>(+84.81%)</b></td><td>231.40 (+12.77%)</td><td>166.46 (-3.06%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.20 (n/a)</td><td>367.72 (n/a)</td><td>293.00 (n/a)</td><td>205.20 (n/a)</td><td>171.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 <b>(-42.46%)</b></td><td>0.02 <b>(-45.85%)</b></td><td>0.02 <b>(-44.17%)</b></td><td>0.01 <b>(-60.15%)</b></td><td>0.01 <b>(-32.21%)</b></td><td>1089.10 <b>(+150.94%)</b></td><td>634.30 <b>(+95.76%)</b></td><td>485.10 <b>(+79.14%)</b></td><td>398.10 <b>(+73.84%)</b></td><td>280.03 <b>(+187.71%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>434.00 (n/a)</td><td>324.02 (n/a)</td><td>270.80 (n/a)</td><td>229.00 (n/a)</td><td>97.33 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 <b>(+22.35%)</b></td><td>0.02 (-5.81%)</td><td>0.01 <b>(-26.18%)</b></td><td>0.01 <b>(-52.10%)</b></td><td>0.01 <b>(+148.50%)</b></td><td>1072.70 <b>(+108.78%)</b></td><td>548.84 <b>(+37.16%)</b></td><td>560.20 <b>(+35.48%)</b></td><td>240.10 (-18.25%)</td><td>334.43 <b>(+301.01%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>513.80 (n/a)</td><td>400.16 (n/a)</td><td>413.50 (n/a)</td><td>293.70 (n/a)</td><td>83.40 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (-17.73%)</td><td>0.02 <b>(-26.66%)</b></td><td>0.02 <b>(-43.48%)</b></td><td>0.01 <b>(-28.21%)</b></td><td>0.01 (-11.74%)</td><td>813.20 <b>(+39.29%)</b></td><td>487.72 <b>(+41.80%)</b></td><td>440.70 <b>(+76.92%)</b></td><td>243.30 <b>(+21.59%)</b></td><td>240.56 <b>(+46.00%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>583.80 (n/a)</td><td>343.96 (n/a)</td><td>249.10 (n/a)</td><td>200.10 (n/a)</td><td>164.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 <b>(+153.71%)</b></td><td>0.03 <b>(+75.49%)</b></td><td>0.03 <b>(+36.48%)</b></td><td>0.02 (+15.87%)</td><td>0.01 <b>(+307.47%)</b></td><td>537.50 (-13.70%)</td><td>321.34 <b>(-34.99%)</b></td><td>318.00 <b>(-26.73%)</b></td><td>155.00 <b>(-60.59%)</b></td><td>142.87 <b>(+32.95%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>622.80 (n/a)</td><td>494.26 (n/a)</td><td>434.00 (n/a)</td><td>393.30 (n/a)</td><td>107.46 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (+10.40%)</td><td>0.03 (-3.07%)</td><td>0.03 (-10.38%)</td><td>0.01 <b>(-27.19%)</b></td><td>0.01 (+18.37%)</td><td>732.80 <b>(+37.36%)</b></td><td>405.64 (+10.27%)</td><td>306.70 (+11.61%)</td><td>214.70 (-9.45%)</td><td>209.88 <b>(+42.54%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.50 (n/a)</td><td>367.86 (n/a)</td><td>274.80 (n/a)</td><td>237.10 (n/a)</td><td>147.24 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (+19.74%)</td><td>0.02 (+3.77%)</td><td>0.02 (-19.27%)</td><td>0.01 (+4.62%)</td><td>0.01 <b>(+42.85%)</b></td><td>639.70 (-4.42%)</td><td>477.78 (+1.28%)</td><td>537.00 <b>(+23.85%)</b></td><td>242.10 (-16.49%)</td><td>168.54 (+14.59%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>669.30 (n/a)</td><td>471.72 (n/a)</td><td>433.60 (n/a)</td><td>289.90 (n/a)</td><td>147.08 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 <b>(-35.82%)</b></td><td>0.04 <b>(-25.98%)</b></td><td>0.03 <b>(-51.73%)</b></td><td>0.02 (-8.93%)</td><td>0.02 <b>(-36.18%)</b></td><td>657.80 (+9.82%)</td><td>444.80 <b>(+24.04%)</b></td><td>521.50 <b>(+107.19%)</b></td><td>260.30 <b>(+55.87%)</b></td><td>176.99 (-8.07%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>599.00 (n/a)</td><td>358.60 (n/a)</td><td>251.70 (n/a)</td><td>167.00 (n/a)</td><td>192.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (-7.83%)</td><td>0.06 (-14.12%)</td><td>0.06 (-3.32%)</td><td>0.04 <b>(-26.78%)</b></td><td>0.02 (+3.92%)</td><td>598.40 <b>(+36.59%)</b></td><td>414.40 <b>(+20.16%)</b></td><td>387.40 (+3.42%)</td><td>275.10 (+8.52%)</td><td>134.40 <b>(+60.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>438.10 (n/a)</td><td>344.86 (n/a)</td><td>374.60 (n/a)</td><td>253.50 (n/a)</td><td>83.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (-11.00%)</td><td>0.04 <b>(-25.32%)</b></td><td>0.03 <b>(-24.27%)</b></td><td>0.02 <b>(-28.68%)</b></td><td>0.01 (-1.10%)</td><td>661.10 <b>(+40.21%)</b></td><td>501.22 <b>(+36.95%)</b></td><td>529.20 <b>(+32.07%)</b></td><td>296.40 (+12.36%)</td><td>133.48 <b>(+51.58%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>471.50 (n/a)</td><td>366.00 (n/a)</td><td>400.70 (n/a)</td><td>263.80 (n/a)</td><td>88.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 <b>(+23.04%)</b></td><td>0.06 (+15.07%)</td><td>0.05 (+4.91%)</td><td>0.03 (-14.71%)</td><td>0.03 <b>(+53.85%)</b></td><td>782.80 (+17.24%)</td><td>465.10 (-2.34%)</td><td>422.90 (-4.69%)</td><td>214.20 (-18.74%)</td><td>238.30 <b>(+43.65%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>667.70 (n/a)</td><td>476.26 (n/a)</td><td>443.70 (n/a)</td><td>263.60 (n/a)</td><td>165.89 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 <b>(+53.06%)</b></td><td>0.06 <b>(+64.88%)</b></td><td>0.05 <b>(+65.12%)</b></td><td>0.03 <b>(+86.86%)</b></td><td>0.02 <b>(+40.47%)</b></td><td>565.50 <b>(-46.48%)</b></td><td>333.38 <b>(-42.32%)</b></td><td>318.80 <b>(-39.44%)</b></td><td>178.50 <b>(-34.66%)</b></td><td>142.76 <b>(-50.92%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1056.70 (n/a)</td><td>578.00 (n/a)</td><td>526.40 (n/a)</td><td>273.20 (n/a)</td><td>290.88 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (+1.77%)</td><td>0.05 <b>(-22.80%)</b></td><td>0.04 <b>(-40.12%)</b></td><td>0.01 <b>(-69.21%)</b></td><td>0.03 <b>(+62.87%)</b></td><td>1717.70 <b>(+224.77%)</b></td><td>665.16 <b>(+87.13%)</b></td><td>515.70 <b>(+67.00%)</b></td><td>259.00 (-1.75%)</td><td>601.67 <b>(+441.15%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>528.90 (n/a)</td><td>355.46 (n/a)</td><td>308.80 (n/a)</td><td>263.60 (n/a)</td><td>111.18 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (-7.54%)</td><td>0.03 <b>(-31.74%)</b></td><td>0.03 <b>(-40.81%)</b></td><td>0.01 <b>(-73.21%)</b></td><td>0.02 (+13.45%)</td><td>2434.10 <b>(+273.27%)</b></td><td>853.10 <b>(+116.88%)</b></td><td>498.10 <b>(+68.96%)</b></td><td>292.40 (+8.14%)</td><td>890.11 <b>(+442.64%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>652.10 (n/a)</td><td>393.36 (n/a)</td><td>294.80 (n/a)</td><td>270.40 (n/a)</td><td>164.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (+15.68%)</td><td>0.05 (+13.51%)</td><td>0.04 (+17.75%)</td><td>0.03 <b>(+86.63%)</b></td><td>0.02 (-5.76%)</td><td>585.40 <b>(-46.42%)</b></td><td>441.94 <b>(-21.95%)</b></td><td>465.70 (-15.08%)</td><td>240.70 (-13.54%)</td><td>127.30 <b>(-59.88%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1092.50 (n/a)</td><td>566.20 (n/a)</td><td>548.40 (n/a)</td><td>278.40 (n/a)</td><td>317.31 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (+2.07%)</td><td>0.05 (+3.92%)</td><td>0.05 (+18.73%)</td><td>0.03 (-10.39%)</td><td>0.02 <b>(+25.74%)</b></td><td>552.40 (+11.60%)</td><td>380.68 (+1.07%)</td><td>302.50 (-15.79%)</td><td>239.30 (-2.05%)</td><td>144.85 <b>(+44.31%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>495.00 (n/a)</td><td>376.64 (n/a)</td><td>359.20 (n/a)</td><td>244.30 (n/a)</td><td>100.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 <b>(-43.44%)</b></td><td>0.04 (-11.93%)</td><td>0.04 (+19.10%)</td><td>0.03 <b>(+189.59%)</b></td><td>0.01 <b>(-66.90%)</b></td><td>659.00 <b>(-65.47%)</b></td><td>511.72 <b>(-27.87%)</b></td><td>421.30 (-16.04%)</td><td>412.20 <b>(+76.83%)</b></td><td>129.26 <b>(-81.12%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1908.30 (n/a)</td><td>709.40 (n/a)</td><td>501.80 (n/a)</td><td>233.10 (n/a)</td><td>684.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 <b>(+26.91%)</b></td><td>0.04 (+18.73%)</td><td>0.03 (+16.50%)</td><td>0.03 (+13.06%)</td><td>0.01 <b>(+49.39%)</b></td><td>545.80 (-11.55%)</td><td>444.22 (-13.94%)</td><td>485.50 (-14.15%)</td><td>301.70 <b>(-21.21%)</b></td><td>114.14 (+6.20%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>617.10 (n/a)</td><td>516.20 (n/a)</td><td>565.50 (n/a)</td><td>382.90 (n/a)</td><td>107.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.11 (-10.83%)</td><td>0.10 (+5.07%)</td><td>0.10 (+12.42%)</td><td>0.05 (+13.49%)</td><td>0.02 <b>(-31.32%)</b></td><td>601.00 (-11.89%)</td><td>368.34 (-10.52%)</td><td>318.90 (-11.05%)</td><td>287.10 (+12.15%)</td><td>130.75 <b>(-26.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>682.10 (n/a)</td><td>411.64 (n/a)</td><td>358.50 (n/a)</td><td>256.00 (n/a)</td><td>177.35 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (-11.09%)</td><td>0.07 <b>(-25.75%)</b></td><td>0.06 <b>(-20.35%)</b></td><td>0.02 <b>(-71.59%)</b></td><td>0.05 (+6.99%)</td><td>1916.40 <b>(+252.02%)</b></td><td>741.38 <b>(+85.64%)</b></td><td>530.60 <b>(+25.53%)</b></td><td>226.80 (+12.44%)</td><td>669.89 <b>(+347.25%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>544.40 (n/a)</td><td>399.36 (n/a)</td><td>422.70 (n/a)</td><td>201.70 (n/a)</td><td>149.78 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (+3.99%)</td><td>0.11 (+3.05%)</td><td>0.14 <b>(+24.02%)</b></td><td>0.05 <b>(-21.54%)</b></td><td>0.05 <b>(+26.29%)</b></td><td>801.10 <b>(+27.44%)</b></td><td>441.52 (+5.88%)</td><td>302.50 (-19.38%)</td><td>254.00 (-3.82%)</td><td>233.69 <b>(+54.07%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>628.60 (n/a)</td><td>417.00 (n/a)</td><td>375.20 (n/a)</td><td>264.10 (n/a)</td><td>151.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 <b>(-31.25%)</b></td><td>0.07 <b>(-20.83%)</b></td><td>0.07 (-5.30%)</td><td>0.05 (+0.48%)</td><td>0.02 <b>(-51.41%)</b></td><td>610.40 (-0.47%)</td><td>479.54 (+18.06%)</td><td>458.80 (+5.59%)</td><td>338.50 <b>(+45.47%)</b></td><td>102.07 <b>(-29.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>613.30 (n/a)</td><td>406.18 (n/a)</td><td>434.50 (n/a)</td><td>232.70 (n/a)</td><td>143.85 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (-16.90%)</td><td>0.11 <b>(-24.98%)</b></td><td>0.10 <b>(-25.08%)</b></td><td>0.06 <b>(-32.16%)</b></td><td>0.04 (+15.14%)</td><td>667.90 <b>(+47.41%)</b></td><td>442.52 <b>(+43.26%)</b></td><td>394.00 <b>(+33.47%)</b></td><td>261.20 <b>(+20.31%)</b></td><td>177.44 <b>(+101.25%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>453.10 (n/a)</td><td>308.90 (n/a)</td><td>295.20 (n/a)</td><td>217.10 (n/a)</td><td>88.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (+1.22%)</td><td>0.09 (+16.04%)</td><td>0.08 <b>(+32.53%)</b></td><td>0.06 <b>(+24.92%)</b></td><td>0.03 (-9.52%)</td><td>569.10 (-19.94%)</td><td>424.92 (-17.08%)</td><td>420.30 <b>(-24.56%)</b></td><td>232.50 (-1.23%)</td><td>138.00 <b>(-21.17%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>710.80 (n/a)</td><td>512.42 (n/a)</td><td>557.10 (n/a)</td><td>235.40 (n/a)</td><td>175.07 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 (-15.24%)</td><td>0.08 <b>(-26.06%)</b></td><td>0.07 <b>(-38.52%)</b></td><td>0.06 (-9.59%)</td><td>0.02 (-18.44%)</td><td>599.60 (+10.61%)</td><td>519.20 <b>(+33.51%)</b></td><td>549.00 <b>(+62.67%)</b></td><td>307.10 (+17.98%)</td><td>121.32 (-0.02%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>542.10 (n/a)</td><td>388.88 (n/a)</td><td>337.50 (n/a)</td><td>260.30 (n/a)</td><td>121.35 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (+10.22%)</td><td>0.10 <b>(+25.32%)</b></td><td>0.12 <b>(+75.85%)</b></td><td>0.05 <b>(+85.25%)</b></td><td>0.04 (-1.47%)</td><td>621.00 <b>(-46.01%)</b></td><td>386.12 <b>(-29.13%)</b></td><td>273.80 <b>(-43.14%)</b></td><td>234.90 (-9.31%)</td><td>179.71 <b>(-50.09%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1150.30 (n/a)</td><td>544.86 (n/a)</td><td>481.50 (n/a)</td><td>259.00 (n/a)</td><td>360.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.18 <b>(+24.41%)</b></td><td>0.10 <b>(+32.49%)</b></td><td>0.08 <b>(+23.81%)</b></td><td>0.06 <b>(+203.78%)</b></td><td>0.05 (+5.86%)</td><td>615.50 <b>(-67.08%)</b></td><td>439.36 <b>(-42.07%)</b></td><td>448.20 (-19.23%)</td><td>205.50 (-19.63%)</td><td>149.19 <b>(-76.50%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1869.80 (n/a)</td><td>758.44 (n/a)</td><td>554.90 (n/a)</td><td>255.70 (n/a)</td><td>634.97 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 (-8.31%)</td><td>0.08 (+2.31%)</td><td>0.08 (+13.53%)</td><td>0.07 <b>(+58.03%)</b></td><td>0.02 <b>(-42.01%)</b></td><td>503.00 <b>(-36.72%)</b></td><td>416.44 (-14.85%)</td><td>428.00 (-11.92%)</td><td>270.20 (+9.04%)</td><td>88.22 <b>(-60.82%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>794.90 (n/a)</td><td>489.04 (n/a)</td><td>485.90 (n/a)</td><td>247.80 (n/a)</td><td>225.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (-9.41%)</td><td>0.07 <b>(+27.82%)</b></td><td>0.07 <b>(+42.53%)</b></td><td>0.06 <b>(+78.52%)</b></td><td>0.01 <b>(-69.08%)</b></td><td>325.70 <b>(-43.98%)</b></td><td>290.72 <b>(-30.20%)</b></td><td>288.70 <b>(-29.86%)</b></td><td>254.60 (+10.36%)</td><td>28.19 <b>(-81.43%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>581.40 (n/a)</td><td>416.52 (n/a)</td><td>411.60 (n/a)</td><td>230.70 (n/a)</td><td>151.83 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (+2.61%)</td><td>0.06 (-14.92%)</td><td>0.05 <b>(-21.78%)</b></td><td>0.04 <b>(-28.80%)</b></td><td>0.02 <b>(+131.41%)</b></td><td>494.90 <b>(+40.44%)</b></td><td>378.44 <b>(+25.95%)</b></td><td>393.30 <b>(+27.82%)</b></td><td>253.10 (-2.54%)</td><td>114.91 <b>(+217.27%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>352.40 (n/a)</td><td>300.46 (n/a)</td><td>307.70 (n/a)</td><td>259.70 (n/a)</td><td>36.22 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 <b>(-30.49%)</b></td><td>0.06 (-13.40%)</td><td>0.07 (-16.90%)</td><td>0.04 (+16.30%)</td><td>0.01 <b>(-55.47%)</b></td><td>455.30 (-14.01%)</td><td>342.78 (+1.78%)</td><td>294.50 <b>(+20.35%)</b></td><td>272.00 <b>(+43.92%)</b></td><td>81.48 <b>(-48.34%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>529.50 (n/a)</td><td>336.78 (n/a)</td><td>244.70 (n/a)</td><td>189.00 (n/a)</td><td>157.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (+12.33%)</td><td>0.06 (-3.22%)</td><td>0.05 (-11.79%)</td><td>0.03 <b>(-20.49%)</b></td><td>0.02 <b>(+33.44%)</b></td><td>607.30 <b>(+25.76%)</b></td><td>413.24 (+8.47%)</td><td>445.70 (+13.38%)</td><td>242.80 (-10.96%)</td><td>143.63 <b>(+46.38%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>482.90 (n/a)</td><td>380.98 (n/a)</td><td>393.10 (n/a)</td><td>272.70 (n/a)</td><td>98.12 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (-4.12%)</td><td>0.05 (-19.14%)</td><td>0.04 (-15.18%)</td><td>0.03 (-13.87%)</td><td>0.02 (-17.55%)</td><td>669.10 (+16.10%)</td><td>478.88 <b>(+20.93%)</b></td><td>513.70 (+17.90%)</td><td>252.30 (+4.26%)</td><td>151.85 (+1.85%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>576.30 (n/a)</td><td>396.00 (n/a)</td><td>435.70 (n/a)</td><td>242.00 (n/a)</td><td>149.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 <b>(-21.46%)</b></td><td>0.05 (-2.68%)</td><td>0.05 (-8.70%)</td><td>0.04 <b>(+288.16%)</b></td><td>0.01 <b>(-60.08%)</b></td><td>502.30 <b>(-74.24%)</b></td><td>413.68 <b>(-38.15%)</b></td><td>429.30 (+9.52%)</td><td>316.70 <b>(+27.29%)</b></td><td>89.91 <b>(-87.56%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1949.60 (n/a)</td><td>668.80 (n/a)</td><td>392.00 (n/a)</td><td>248.80 (n/a)</td><td>722.83 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (-2.00%)</td><td>0.07 (+1.89%)</td><td>0.08 (+1.99%)</td><td>0.04 (-2.47%)</td><td>0.02 (+1.44%)</td><td>582.30 (+2.54%)</td><td>371.64 (-1.36%)</td><td>300.40 (-1.96%)</td><td>252.80 (+2.06%)</td><td>139.36 (+3.94%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>567.90 (n/a)</td><td>376.78 (n/a)</td><td>306.40 (n/a)</td><td>247.70 (n/a)</td><td>134.08 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (-14.28%)</td><td>0.07 (+2.88%)</td><td>0.08 <b>(+24.77%)</b></td><td>0.05 (+19.75%)</td><td>0.02 <b>(-25.62%)</b></td><td>455.60 (-16.50%)</td><td>352.70 (-6.30%)</td><td>302.30 (-19.86%)</td><td>267.50 (+16.66%)</td><td>94.01 <b>(-23.72%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>545.60 (n/a)</td><td>376.40 (n/a)</td><td>377.20 (n/a)</td><td>229.30 (n/a)</td><td>123.26 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 <b>(+35.52%)</b></td><td>0.06 <b>(+28.22%)</b></td><td>0.07 <b>(+54.06%)</b></td><td>0.04 (-11.22%)</td><td>0.02 <b>(+121.98%)</b></td><td>649.30 (+12.65%)</td><td>416.66 (-16.69%)</td><td>345.50 <b>(-35.08%)</b></td><td>297.70 <b>(-26.20%)</b></td><td>149.95 <b>(+81.18%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>576.40 (n/a)</td><td>500.16 (n/a)</td><td>532.20 (n/a)</td><td>403.40 (n/a)</td><td>82.76 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (-0.97%)</td><td>0.05 (-19.08%)</td><td>0.05 <b>(-30.85%)</b></td><td>0.03 (-14.68%)</td><td>0.02 (-14.27%)</td><td>751.60 (+17.20%)</td><td>513.64 (+19.46%)</td><td>473.40 <b>(+44.59%)</b></td><td>268.30 (+0.98%)</td><td>180.24 (-6.39%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>641.30 (n/a)</td><td>429.96 (n/a)</td><td>327.40 (n/a)</td><td>265.70 (n/a)</td><td>192.54 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (-9.46%)</td><td>0.06 (-8.02%)</td><td>0.05 (-11.88%)</td><td>0.04 (+5.01%)</td><td>0.03 (-7.36%)</td><td>600.20 (-4.76%)</td><td>445.20 (+8.07%)</td><td>532.30 (+13.50%)</td><td>259.80 (+10.46%)</td><td>169.05 (+1.03%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>630.20 (n/a)</td><td>411.94 (n/a)</td><td>469.00 (n/a)</td><td>235.20 (n/a)</td><td>167.34 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.11 (-8.25%)</td><td>0.06 <b>(-26.58%)</b></td><td>0.05 <b>(-37.48%)</b></td><td>0.04 <b>(-28.10%)</b></td><td>0.03 <b>(+23.58%)</b></td><td>576.00 <b>(+39.06%)</b></td><td>432.48 <b>(+43.63%)</b></td><td>467.40 <b>(+59.96%)</b></td><td>225.60 (+8.99%)</td><td>128.55 <b>(+73.58%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>414.20 (n/a)</td><td>301.10 (n/a)</td><td>292.20 (n/a)</td><td>207.00 (n/a)</td><td>74.06 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 <b>(-20.40%)</b></td><td>0.04 <b>(-29.05%)</b></td><td>0.04 <b>(-24.28%)</b></td><td>0.03 (-14.05%)</td><td>0.01 <b>(-38.08%)</b></td><td>555.80 (+16.35%)</td><td>482.68 <b>(+35.11%)</b></td><td>515.20 <b>(+32.07%)</b></td><td>290.80 <b>(+25.67%)</b></td><td>109.55 (-8.07%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>477.70 (n/a)</td><td>357.24 (n/a)</td><td>390.10 (n/a)</td><td>231.40 (n/a)</td><td>119.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 <b>(-42.41%)</b></td><td>0.04 <b>(-26.49%)</b></td><td>0.04 (+12.25%)</td><td>0.03 (+0.09%)</td><td>0.01 <b>(-63.33%)</b></td><td>637.70 (-0.09%)</td><td>477.84 (+10.40%)</td><td>456.00 (-10.92%)</td><td>294.10 <b>(+73.61%)</b></td><td>127.82 <b>(-40.31%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>638.30 (n/a)</td><td>432.82 (n/a)</td><td>511.90 (n/a)</td><td>169.40 (n/a)</td><td>214.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 <b>(-46.00%)</b></td><td>0.04 <b>(-40.16%)</b></td><td>0.03 <b>(-48.12%)</b></td><td>0.03 <b>(-27.53%)</b></td><td>0.01 <b>(-57.36%)</b></td><td>642.10 <b>(+38.00%)</b></td><td>534.68 <b>(+60.12%)</b></td><td>581.40 <b>(+92.77%)</b></td><td>409.30 <b>(+85.20%)</b></td><td>109.96 (+4.38%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>465.30 (n/a)</td><td>333.92 (n/a)</td><td>301.60 (n/a)</td><td>221.00 (n/a)</td><td>105.34 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (+7.59%)</td><td>0.05 (-9.55%)</td><td>0.05 <b>(-33.53%)</b></td><td>0.03 (-7.74%)</td><td>0.02 (+4.45%)</td><td>605.10 (+8.38%)</td><td>398.62 (+11.58%)</td><td>404.00 <b>(+50.41%)</b></td><td>236.30 (-7.08%)</td><td>148.58 (+7.11%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>558.30 (n/a)</td><td>357.24 (n/a)</td><td>268.60 (n/a)</td><td>254.30 (n/a)</td><td>138.72 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 <b>(+29.93%)</b></td><td>0.05 (+10.58%)</td><td>0.05 <b>(+32.83%)</b></td><td>0.03 (-4.38%)</td><td>0.02 <b>(+42.69%)</b></td><td>640.70 (+4.57%)</td><td>411.76 (-3.28%)</td><td>356.60 <b>(-24.72%)</b></td><td>211.30 <b>(-23.02%)</b></td><td>180.68 <b>(+26.56%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>612.70 (n/a)</td><td>425.74 (n/a)</td><td>473.70 (n/a)</td><td>274.50 (n/a)</td><td>142.76 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (+18.74%)</td><td>0.06 (+19.00%)</td><td>0.05 (+15.42%)</td><td>0.03 (+10.35%)</td><td>0.03 <b>(+22.19%)</b></td><td>565.70 (-9.39%)</td><td>377.94 (-14.55%)</td><td>373.00 (-13.36%)</td><td>187.90 (-15.78%)</td><td>140.58 (-4.58%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>624.30 (n/a)</td><td>442.28 (n/a)</td><td>430.50 (n/a)</td><td>223.10 (n/a)</td><td>147.33 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.40 (-15.35%)</td><td>0.29 (-11.95%)</td><td>0.33 (-5.14%)</td><td>0.15 (-16.71%)</td><td>0.10 (-19.28%)</td><td>638.60 <b>(+20.06%)</b></td><td>388.74 (+12.00%)</td><td>293.70 (+5.42%)</td><td>246.50 (+18.11%)</td><td>165.80 (+11.68%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>531.90 (n/a)</td><td>347.08 (n/a)</td><td>278.60 (n/a)</td><td>208.70 (n/a)</td><td>148.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.33 (-14.34%)</td><td>0.19 <b>(-31.21%)</b></td><td>0.17 <b>(-38.02%)</b></td><td>0.08 <b>(-53.11%)</b></td><td>0.09 (+14.78%)</td><td>1248.80 <b>(+113.29%)</b></td><td>642.62 <b>(+67.89%)</b></td><td>579.50 <b>(+61.33%)</b></td><td>300.50 (+16.74%)</td><td>365.50 <b>(+188.46%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>585.50 (n/a)</td><td>382.76 (n/a)</td><td>359.20 (n/a)</td><td>257.40 (n/a)</td><td>126.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.39 (+0.19%)</td><td>0.27 (-16.06%)</td><td>0.23 <b>(-34.37%)</b></td><td>0.16 (-1.88%)</td><td>0.11 <b>(+24.85%)</b></td><td>607.00 (+1.91%)</td><td>426.52 <b>(+24.45%)</b></td><td>426.40 <b>(+52.34%)</b></td><td>251.10 (-0.20%)</td><td>170.39 (+18.96%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.35 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>595.60 (n/a)</td><td>342.72 (n/a)</td><td>279.90 (n/a)</td><td>251.60 (n/a)</td><td>143.24 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.32 (+8.76%)</td><td>0.18 <b>(-24.79%)</b></td><td>0.14 <b>(-42.73%)</b></td><td>0.11 <b>(-30.87%)</b></td><td>0.08 <b>(+73.35%)</b></td><td>656.30 <b>(+44.66%)</b></td><td>472.08 <b>(+46.35%)</b></td><td>534.60 <b>(+74.59%)</b></td><td>228.00 (-8.06%)</td><td>164.35 <b>(+110.84%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>453.70 (n/a)</td><td>322.58 (n/a)</td><td>306.20 (n/a)</td><td>248.00 (n/a)</td><td>77.95 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.30 (+13.24%)</td><td>0.18 (-15.13%)</td><td>0.15 <b>(-36.27%)</b></td><td>0.13 (+0.55%)</td><td>0.07 <b>(+25.48%)</b></td><td>560.10 (-0.55%)</td><td>440.64 <b>(+20.60%)</b></td><td>477.30 <b>(+56.90%)</b></td><td>243.80 (-11.67%)</td><td>129.53 (+8.57%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>563.20 (n/a)</td><td>365.38 (n/a)</td><td>304.20 (n/a)</td><td>276.00 (n/a)</td><td>119.30 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.48 <b>(+75.38%)</b></td><td>0.24 <b>(+52.24%)</b></td><td>0.21 <b>(+48.98%)</b></td><td>0.14 <b>(+351.77%)</b></td><td>0.14 <b>(+37.15%)</b></td><td>542.40 <b>(-77.87%)</b></td><td>364.44 <b>(-56.69%)</b></td><td>356.90 <b>(-32.88%)</b></td><td>154.10 <b>(-42.99%)</b></td><td>147.89 <b>(-83.82%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.10 (n/a)</td><td>2450.60 (n/a)</td><td>841.46 (n/a)</td><td>531.70 (n/a)</td><td>270.30 (n/a)</td><td>913.84 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (-15.35%)</td><td>0.11 (-11.80%)</td><td>0.11 (-6.89%)</td><td>0.09 (+19.57%)</td><td>0.02 <b>(-40.91%)</b></td><td>426.60 (-16.37%)</td><td>349.72 (+8.27%)</td><td>329.80 (+7.39%)</td><td>287.80 (+18.14%)</td><td>63.47 <b>(-41.88%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>510.10 (n/a)</td><td>323.02 (n/a)</td><td>307.10 (n/a)</td><td>243.60 (n/a)</td><td>109.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (+10.70%)</td><td>0.12 (-4.02%)</td><td>0.12 (-5.41%)</td><td>0.07 <b>(-40.05%)</b></td><td>0.04 <b>(+208.57%)</b></td><td>545.30 <b>(+66.81%)</b></td><td>332.44 (+13.35%)</td><td>311.70 (+5.73%)</td><td>230.90 (-9.66%)</td><td>125.75 <b>(+378.21%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>326.90 (n/a)</td><td>293.28 (n/a)</td><td>294.80 (n/a)</td><td>255.60 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (+17.74%)</td><td>0.08 (+2.57%)</td><td>0.08 (+0.97%)</td><td>0.05 <b>(+34.19%)</b></td><td>0.03 (+18.90%)</td><td>764.00 <b>(-25.49%)</b></td><td>509.64 (-5.31%)</td><td>460.00 (-0.97%)</td><td>264.40 (-15.07%)</td><td>187.24 <b>(-33.00%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>1025.30 (n/a)</td><td>538.24 (n/a)</td><td>464.50 (n/a)</td><td>311.30 (n/a)</td><td>279.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (+2.09%)</td><td>0.09 <b>(-27.02%)</b></td><td>0.08 <b>(-37.32%)</b></td><td>0.03 <b>(-47.05%)</b></td><td>0.04 <b>(+22.25%)</b></td><td>1084.60 <b>(+88.86%)</b></td><td>535.22 <b>(+56.29%)</b></td><td>451.40 <b>(+59.56%)</b></td><td>247.20 (-2.02%)</td><td>319.90 <b>(+137.79%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>574.30 (n/a)</td><td>342.46 (n/a)</td><td>282.90 (n/a)</td><td>252.30 (n/a)</td><td>134.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (+17.71%)</td><td>0.11 (+8.16%)</td><td>0.10 (-14.28%)</td><td>0.07 (+15.01%)</td><td>0.03 (+11.56%)</td><td>522.40 (-13.05%)</td><td>366.54 (-8.25%)</td><td>355.80 (+16.69%)</td><td>246.70 (-15.05%)</td><td>118.61 (-17.30%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>600.80 (n/a)</td><td>399.48 (n/a)</td><td>304.90 (n/a)</td><td>290.40 (n/a)</td><td>143.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.18 <b>(+82.50%)</b></td><td>0.12 <b>(+70.67%)</b></td><td>0.11 <b>(+88.94%)</b></td><td>0.08 <b>(+28.88%)</b></td><td>0.05 <b>(+163.51%)</b></td><td>484.70 <b>(-22.41%)</b></td><td>342.26 <b>(-36.85%)</b></td><td>324.60 <b>(-47.07%)</b></td><td>203.50 <b>(-45.19%)</b></td><td>126.06 (+13.46%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>624.70 (n/a)</td><td>542.00 (n/a)</td><td>613.30 (n/a)</td><td>371.30 (n/a)</td><td>111.11 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.19 (+12.44%)</td><td>0.12 (-16.20%)</td><td>0.09 <b>(-40.93%)</b></td><td>0.07 (+4.05%)</td><td>0.05 (+16.24%)</td><td>572.60 (-3.88%)</td><td>391.82 <b>(+20.28%)</b></td><td>434.30 <b>(+69.32%)</b></td><td>219.40 (-11.07%)</td><td>143.17 (-5.53%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>595.70 (n/a)</td><td>325.76 (n/a)</td><td>256.50 (n/a)</td><td>246.70 (n/a)</td><td>151.56 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 <b>(-22.49%)</b></td><td>0.09 <b>(-29.67%)</b></td><td>0.09 <b>(-36.81%)</b></td><td>0.08 <b>(-21.37%)</b></td><td>0.02 <b>(-23.14%)</b></td><td>537.80 <b>(+27.20%)</b></td><td>462.38 <b>(+41.90%)</b></td><td>476.40 <b>(+58.27%)</b></td><td>332.70 <b>(+29.00%)</b></td><td>78.55 <b>(+20.51%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>422.80 (n/a)</td><td>325.86 (n/a)</td><td>301.00 (n/a)</td><td>257.90 (n/a)</td><td>65.18 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.19 (+7.09%)</td><td>0.12 (-2.66%)</td><td>0.09 <b>(-40.86%)</b></td><td>0.07 (+7.80%)</td><td>0.06 (+6.21%)</td><td>592.20 (-7.24%)</td><td>399.74 (+0.67%)</td><td>470.60 <b>(+69.10%)</b></td><td>213.90 (-6.63%)</td><td>168.65 (-16.17%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>638.40 (n/a)</td><td>397.08 (n/a)</td><td>278.30 (n/a)</td><td>229.10 (n/a)</td><td>201.16 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.17 (-0.05%)</td><td>0.12 (+9.17%)</td><td>0.12 <b>(+45.02%)</b></td><td>0.06 (-3.54%)</td><td>0.04 (+0.16%)</td><td>638.40 (+3.67%)</td><td>399.36 (-7.75%)</td><td>332.60 <b>(-31.04%)</b></td><td>243.30 (+0.08%)</td><td>167.88 (+6.42%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>615.80 (n/a)</td><td>432.92 (n/a)</td><td>482.30 (n/a)</td><td>243.10 (n/a)</td><td>157.75 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (-7.38%)</td><td>0.12 (-3.92%)</td><td>0.11 (-7.44%)</td><td>0.09 <b>(+32.56%)</b></td><td>0.03 <b>(-27.97%)</b></td><td>470.50 <b>(-24.56%)</b></td><td>372.74 (-1.87%)</td><td>377.70 (+8.04%)</td><td>263.10 (+7.96%)</td><td>87.86 <b>(-41.45%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>623.70 (n/a)</td><td>379.84 (n/a)</td><td>349.60 (n/a)</td><td>243.70 (n/a)</td><td>150.05 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (+12.18%)</td><td>0.12 (+2.27%)</td><td>0.12 (-2.60%)</td><td>0.09 (+17.23%)</td><td>0.03 (+0.38%)</td><td>463.70 (-14.68%)</td><td>366.76 (-3.26%)</td><td>337.90 (+2.64%)</td><td>264.40 (-10.83%)</td><td>82.16 <b>(-21.08%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>543.50 (n/a)</td><td>379.12 (n/a)</td><td>329.20 (n/a)</td><td>296.50 (n/a)</td><td>104.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.11 <b>(-30.91%)</b></td><td>0.09 (-16.26%)</td><td>0.08 (-19.03%)</td><td>0.06 <b>(+28.42%)</b></td><td>0.02 <b>(-55.26%)</b></td><td>546.70 <b>(-22.13%)</b></td><td>422.42 (+6.01%)</td><td>429.60 <b>(+23.52%)</b></td><td>306.10 <b>(+44.73%)</b></td><td>91.43 <b>(-51.32%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>702.10 (n/a)</td><td>398.48 (n/a)</td><td>347.80 (n/a)</td><td>211.50 (n/a)</td><td>187.81 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 <b>(-55.10%)</b></td><td>0.05 <b>(-57.22%)</b></td><td>0.06 <b>(-50.48%)</b></td><td>0.03 <b>(-58.51%)</b></td><td>0.02 <b>(-50.38%)</b></td><td>1368.10 <b>(+141.03%)</b></td><td>801.08 <b>(+140.97%)</b></td><td>630.70 <b>(+101.95%)</b></td><td>472.40 <b>(+122.73%)</b></td><td>360.31 <b>(+160.38%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>567.60 (n/a)</td><td>332.44 (n/a)</td><td>312.30 (n/a)</td><td>212.10 (n/a)</td><td>138.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 <b>(-39.25%)</b></td><td>0.08 <b>(-25.64%)</b></td><td>0.06 <b>(-21.70%)</b></td><td>0.06 (+1.68%)</td><td>0.02 <b>(-56.19%)</b></td><td>585.40 (-1.65%)</td><td>480.28 (+17.96%)</td><td>547.60 <b>(+27.74%)</b></td><td>295.60 <b>(+64.59%)</b></td><td>124.81 <b>(-29.65%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>595.20 (n/a)</td><td>407.14 (n/a)</td><td>428.70 (n/a)</td><td>179.60 (n/a)</td><td>177.42 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 <b>(-29.02%)</b></td><td>0.10 (-11.40%)</td><td>0.11 (+10.17%)</td><td>0.07 (+2.73%)</td><td>0.03 <b>(-34.70%)</b></td><td>516.40 (-2.66%)</td><td>377.28 (+9.05%)</td><td>309.10 (-9.25%)</td><td>273.20 <b>(+40.90%)</b></td><td>113.94 (-5.85%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>530.50 (n/a)</td><td>345.96 (n/a)</td><td>340.60 (n/a)</td><td>193.90 (n/a)</td><td>121.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (+5.58%)</td><td>0.10 (+19.13%)</td><td>0.09 (+16.52%)</td><td>0.07 <b>(+55.44%)</b></td><td>0.03 (-3.63%)</td><td>497.40 <b>(-35.67%)</b></td><td>377.66 (-19.59%)</td><td>368.10 (-14.18%)</td><td>261.30 (-5.26%)</td><td>105.77 <b>(-42.43%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>773.20 (n/a)</td><td>469.66 (n/a)</td><td>428.90 (n/a)</td><td>275.80 (n/a)</td><td>183.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (+15.36%)</td><td>0.09 (+17.92%)</td><td>0.10 <b>(+41.79%)</b></td><td>0.06 (+4.56%)</td><td>0.03 <b>(+47.09%)</b></td><td>585.30 (-4.36%)</td><td>415.54 (-10.76%)</td><td>332.50 <b>(-29.47%)</b></td><td>264.30 (-13.32%)</td><td>151.59 <b>(+35.74%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>612.00 (n/a)</td><td>465.64 (n/a)</td><td>471.40 (n/a)</td><td>304.90 (n/a)</td><td>111.67 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.41 (-17.34%)</td><td>0.28 <b>(-33.13%)</b></td><td>0.27 <b>(-34.56%)</b></td><td>0.18 <b>(-48.52%)</b></td><td>0.08 <b>(+54.93%)</b></td><td>709.20 <b>(+94.25%)</b></td><td>494.40 <b>(+57.26%)</b></td><td>487.10 <b>(+52.79%)</b></td><td>323.40 <b>(+20.99%)</b></td><td>138.41 <b>(+265.24%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.05 (n/a)</td><td>365.10 (n/a)</td><td>314.38 (n/a)</td><td>318.80 (n/a)</td><td>267.30 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.51 <b>(+25.56%)</b></td><td>0.31 (+11.03%)</td><td>0.27 (+5.25%)</td><td>0.05 <b>(-73.34%)</b></td><td>0.19 <b>(+142.15%)</b></td><td>2435.40 <b>(+275.08%)</b></td><td>806.30 <b>(+61.73%)</b></td><td>485.70 (-4.99%)</td><td>254.60 <b>(-20.36%)</b></td><td>921.07 <b>(+685.18%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>649.30 (n/a)</td><td>498.56 (n/a)</td><td>511.20 (n/a)</td><td>319.70 (n/a)</td><td>117.31 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.39 (-3.01%)</td><td>0.27 (+14.31%)</td><td>0.26 (+1.97%)</td><td>0.21 <b>(+254.32%)</b></td><td>0.07 <b>(-43.66%)</b></td><td>612.50 <b>(-71.78%)</b></td><td>497.10 <b>(-39.37%)</b></td><td>504.70 (-1.92%)</td><td>333.30 (+3.13%)</td><td>102.77 <b>(-86.49%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.41 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>0.12 (n/a)</td><td>2170.20 (n/a)</td><td>819.94 (n/a)</td><td>514.60 (n/a)</td><td>323.20 (n/a)</td><td>760.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-17.49%)</td><td>19669.53 (+13.64%)</td><td>15644.39 <b>(+30.09%)</b></td><td>16851.43 (+17.99%)</td><td>6424.65 (+2.81%)</td><td>5296.31 (+0.26%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17308.17 (n/a)</td><td>12025.76 (n/a)</td><td>14282.19 (n/a)</td><td>6249.35 (n/a)</td><td>5282.80 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.00 (-7.14%)</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-13.09%)</td><td>20749.86 (-6.02%)</td><td>14327.13 (+10.65%)</td><td>17764.38 <b>(+107.87%)</b></td><td>6369.17 (+7.09%)</td><td>6365.30 (-16.21%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22078.52 (n/a)</td><td>12948.70 (n/a)</td><td>8546.00 (n/a)</td><td>5947.46 (n/a)</td><td>7596.55 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (-3.04%)</td><td>0.10 (-8.65%)</td><td>0.08 (-9.44%)</td><td>0.08 (+5.99%)</td><td>0.02 (-17.24%)</td><td>26969.89 (-5.65%)</td><td>23047.24 (+7.59%)</td><td>25420.40 (+10.39%)</td><td>15666.95 (+3.17%)</td><td>4881.19 (-14.81%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28586.24 (n/a)</td><td>21421.34 (n/a)</td><td>23027.80 (n/a)</td><td>15184.85 (n/a)</td><td>5730.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.05 (+18.12%)</td><td>1.41 (-16.65%)</td><td>1.15 <b>(-32.74%)</b></td><td>0.31 (-1.69%)</td><td>1.06 (+18.76%)</td><td>3415.40 (+1.72%)</td><td>1320.70 (+19.62%)</td><td>914.60 <b>(+48.69%)</b></td><td>343.40 (-15.34%)</td><td>1228.58 (-2.92%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>2.59 (n/a)</td><td>1.69 (n/a)</td><td>1.70 (n/a)</td><td>0.31 (n/a)</td><td>0.89 (n/a)</td><td>3357.60 (n/a)</td><td>1104.04 (n/a)</td><td>615.10 (n/a)</td><td>405.60 (n/a)</td><td>1265.57 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>4.02 (+13.91%)</td><td>2.22 (+8.99%)</td><td>1.75 <b>(-25.21%)</b></td><td>1.55 <b>(+431.01%)</b></td><td>1.02 (-14.35%)</td><td>678.50 <b>(-81.17%)</b></td><td>531.28 <b>(-51.14%)</b></td><td>598.20 <b>(+33.71%)</b></td><td>260.80 (-12.22%)</td><td>162.00 <b>(-88.53%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.53 (n/a)</td><td>2.04 (n/a)</td><td>2.34 (n/a)</td><td>0.29 (n/a)</td><td>1.19 (n/a)</td><td>3602.90 (n/a)</td><td>1087.44 (n/a)</td><td>447.40 (n/a)</td><td>297.10 (n/a)</td><td>1411.99 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.23 (-18.53%)</td><td>1.84 <b>(-23.20%)</b></td><td>1.51 <b>(-28.48%)</b></td><td>1.36 (-14.32%)</td><td>0.78 (-16.25%)</td><td>769.70 (+16.71%)</td><td>629.92 <b>(+30.40%)</b></td><td>694.00 <b>(+39.83%)</b></td><td>324.80 <b>(+22.75%)</b></td><td>177.11 (+18.10%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.96 (n/a)</td><td>2.39 (n/a)</td><td>2.11 (n/a)</td><td>1.59 (n/a)</td><td>0.94 (n/a)</td><td>659.50 (n/a)</td><td>483.08 (n/a)</td><td>496.30 (n/a)</td><td>264.60 (n/a)</td><td>149.97 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>2.73 (+2.75%)</td><td>2.02 (+9.10%)</td><td>2.53 <b>(+42.58%)</b></td><td>0.42 <b>(-60.72%)</b></td><td>0.97 <b>(+59.17%)</b></td><td>2478.40 <b>(+154.61%)</b></td><td>851.22 <b>(+36.98%)</b></td><td>415.20 <b>(-29.86%)</b></td><td>383.60 (-2.69%)</td><td>913.10 <b>(+307.58%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>2.66 (n/a)</td><td>1.86 (n/a)</td><td>1.77 (n/a)</td><td>1.08 (n/a)</td><td>0.61 (n/a)</td><td>973.40 (n/a)</td><td>621.44 (n/a)</td><td>592.00 (n/a)</td><td>394.20 (n/a)</td><td>224.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.88 (+6.73%)</td><td>2.67 <b>(+24.17%)</b></td><td>3.07 (+15.51%)</td><td>0.70 (-17.98%)</td><td>1.24 (+2.11%)</td><td>2977.70 <b>(+21.92%)</b></td><td>1147.36 (-16.40%)</td><td>684.20 (-13.43%)</td><td>539.90 (-6.30%)</td><td>1032.67 (+14.54%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.64 (n/a)</td><td>2.15 (n/a)</td><td>2.65 (n/a)</td><td>0.86 (n/a)</td><td>1.21 (n/a)</td><td>2442.40 (n/a)</td><td>1372.48 (n/a)</td><td>790.30 (n/a)</td><td>576.20 (n/a)</td><td>901.56 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.87 (-1.61%)</td><td>2.53 <b>(-20.18%)</b></td><td>1.94 <b>(-22.91%)</b></td><td>0.59 <b>(-69.55%)</b></td><td>1.98 <b>(+23.45%)</b></td><td>3583.90 <b>(+228.44%)</b></td><td>1401.18 <b>(+83.29%)</b></td><td>1079.30 <b>(+29.71%)</b></td><td>357.10 (+1.62%)</td><td>1256.01 <b>(+366.34%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.97 (n/a)</td><td>3.17 (n/a)</td><td>2.52 (n/a)</td><td>1.92 (n/a)</td><td>1.60 (n/a)</td><td>1091.20 (n/a)</td><td>764.46 (n/a)</td><td>832.10 (n/a)</td><td>351.40 (n/a)</td><td>269.34 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.77 <b>(+44.77%)</b></td><td>3.31 <b>(+74.81%)</b></td><td>3.49 <b>(+453.32%)</b></td><td>0.58 (+0.85%)</td><td>1.87 (+5.18%)</td><td>3597.10 (-0.85%)</td><td>1167.50 <b>(-49.78%)</b></td><td>600.10 <b>(-81.93%)</b></td><td>363.20 <b>(-30.92%)</b></td><td>1364.36 (-16.11%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.99 (n/a)</td><td>1.89 (n/a)</td><td>0.63 (n/a)</td><td>0.58 (n/a)</td><td>1.78 (n/a)</td><td>3627.80 (n/a)</td><td>2324.98 (n/a)</td><td>3320.40 (n/a)</td><td>525.80 (n/a)</td><td>1626.45 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>7.23 <b>(+61.72%)</b></td><td>4.68 <b>(+45.93%)</b></td><td>3.89 <b>(+30.55%)</b></td><td>3.16 <b>(+58.95%)</b></td><td>1.69 <b>(+64.82%)</b></td><td>663.40 <b>(-37.09%)</b></td><td>491.28 <b>(-31.02%)</b></td><td>538.50 <b>(-23.40%)</b></td><td>290.20 <b>(-38.15%)</b></td><td>154.00 <b>(-34.91%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>4.47 (n/a)</td><td>3.21 (n/a)</td><td>2.98 (n/a)</td><td>1.99 (n/a)</td><td>1.03 (n/a)</td><td>1054.50 (n/a)</td><td>712.24 (n/a)</td><td>703.00 (n/a)</td><td>469.20 (n/a)</td><td>236.58 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.70 (+1.21%)</td><td>3.57 (-1.03%)</td><td>4.16 <b>(+29.17%)</b></td><td>0.60 <b>(-78.66%)</b></td><td>2.21 <b>(+89.19%)</b></td><td>3490.80 <b>(+368.63%)</b></td><td>1160.14 <b>(+87.25%)</b></td><td>504.20 <b>(-22.57%)</b></td><td>367.90 (-1.18%)</td><td>1332.15 <b>(+776.62%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.63 (n/a)</td><td>3.61 (n/a)</td><td>3.22 (n/a)</td><td>2.82 (n/a)</td><td>1.17 (n/a)</td><td>744.90 (n/a)</td><td>619.58 (n/a)</td><td>651.20 (n/a)</td><td>372.30 (n/a)</td><td>151.96 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.05 <b>(-21.60%)</b></td><td>3.32 (+12.38%)</td><td>3.10 <b>(+23.58%)</b></td><td>1.73 <b>(+201.90%)</b></td><td>1.59 <b>(-38.14%)</b></td><td>1209.60 <b>(-66.88%)</b></td><td>772.44 <b>(-56.01%)</b></td><td>676.80 (-19.08%)</td><td>415.30 <b>(+27.55%)</b></td><td>378.81 <b>(-77.45%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>6.44 (n/a)</td><td>2.96 (n/a)</td><td>2.51 (n/a)</td><td>0.57 (n/a)</td><td>2.58 (n/a)</td><td>3651.90 (n/a)</td><td>1755.78 (n/a)</td><td>836.40 (n/a)</td><td>325.60 (n/a)</td><td>1680.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.20 (+1.64%)</td><td>4.23 (+12.29%)</td><td>4.90 <b>(+20.36%)</b></td><td>1.72 <b>(+22.53%)</b></td><td>1.43 (+2.71%)</td><td>2442.90 (-18.39%)</td><td>1181.14 (-14.12%)</td><td>855.80 (-16.91%)</td><td>807.10 (-1.62%)</td><td>707.23 <b>(-22.19%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.11 (n/a)</td><td>3.77 (n/a)</td><td>4.07 (n/a)</td><td>1.40 (n/a)</td><td>1.40 (n/a)</td><td>2993.30 (n/a)</td><td>1375.30 (n/a)</td><td>1030.00 (n/a)</td><td>820.40 (n/a)</td><td>908.92 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>9.29 (+18.25%)</td><td>5.07 <b>(-26.00%)</b></td><td>5.96 (-19.70%)</td><td>1.17 <b>(-74.87%)</b></td><td>3.73 <b>(+188.84%)</b></td><td>3577.00 <b>(+297.93%)</b></td><td>1754.16 <b>(+176.20%)</b></td><td>703.70 <b>(+24.53%)</b></td><td>451.40 (-15.44%)</td><td>1629.53 <b>(+976.14%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>7.86 (n/a)</td><td>6.85 (n/a)</td><td>7.42 (n/a)</td><td>4.67 (n/a)</td><td>1.29 (n/a)</td><td>898.90 (n/a)</td><td>635.10 (n/a)</td><td>565.10 (n/a)</td><td>533.80 (n/a)</td><td>151.42 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>9.08 <b>(+41.30%)</b></td><td>6.12 <b>(+46.01%)</b></td><td>6.60 (+13.53%)</td><td>1.68 <b>(+44.07%)</b></td><td>2.70 (+6.73%)</td><td>2497.90 <b>(-30.59%)</b></td><td>972.54 <b>(-40.29%)</b></td><td>635.00 (-11.93%)</td><td>461.80 <b>(-29.23%)</b></td><td>855.98 <b>(-36.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>6.43 (n/a)</td><td>4.19 (n/a)</td><td>5.82 (n/a)</td><td>1.17 (n/a)</td><td>2.53 (n/a)</td><td>3598.80 (n/a)</td><td>1628.70 (n/a)</td><td>721.00 (n/a)</td><td>652.50 (n/a)</td><td>1338.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>10.08 <b>(+43.34%)</b></td><td>5.58 (+3.73%)</td><td>3.95 <b>(-40.93%)</b></td><td>1.17 <b>(-42.27%)</b></td><td>3.74 <b>(+72.26%)</b></td><td>3594.20 <b>(+73.21%)</b></td><td>1326.42 <b>(+35.87%)</b></td><td>1061.40 <b>(+69.28%)</b></td><td>416.00 <b>(-30.24%)</b></td><td>1306.19 <b>(+106.34%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>7.03 (n/a)</td><td>5.38 (n/a)</td><td>6.69 (n/a)</td><td>2.02 (n/a)</td><td>2.17 (n/a)</td><td>2075.00 (n/a)</td><td>976.24 (n/a)</td><td>627.00 (n/a)</td><td>596.30 (n/a)</td><td>633.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>10.46 <b>(+52.39%)</b></td><td>5.27 (+1.89%)</td><td>4.13 (-18.41%)</td><td>1.18 <b>(-66.68%)</b></td><td>3.50 <b>(+148.60%)</b></td><td>3541.30 <b>(+200.08%)</b></td><td>1332.58 <b>(+54.65%)</b></td><td>1014.40 <b>(+22.56%)</b></td><td>400.80 <b>(-34.38%)</b></td><td>1266.09 <b>(+427.88%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>6.87 (n/a)</td><td>5.18 (n/a)</td><td>5.07 (n/a)</td><td>3.55 (n/a)</td><td>1.41 (n/a)</td><td>1180.10 (n/a)</td><td>861.66 (n/a)</td><td>827.70 (n/a)</td><td>610.80 (n/a)</td><td>239.84 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>8.07 (-12.34%)</td><td>3.94 <b>(-23.35%)</b></td><td>3.56 <b>(-26.62%)</b></td><td>1.17 (+0.05%)</td><td>2.95 (-2.06%)</td><td>3593.50 (-0.05%)</td><td>1858.48 <b>(+40.04%)</b></td><td>1177.10 <b>(+36.29%)</b></td><td>519.60 (+14.07%)</td><td>1453.00 (+12.64%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>9.21 (n/a)</td><td>5.14 (n/a)</td><td>4.86 (n/a)</td><td>1.17 (n/a)</td><td>3.01 (n/a)</td><td>3595.30 (n/a)</td><td>1327.06 (n/a)</td><td>863.70 (n/a)</td><td>455.50 (n/a)</td><td>1289.95 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>2.15 <b>(+51.39%)</b></td><td>1.12 <b>(+44.81%)</b></td><td>1.05 <b>(+48.70%)</b></td><td>0.16 (+0.27%)</td><td>0.71 <b>(+47.42%)</b></td><td>3300.00 (-0.27%)</td><td>998.76 (-15.38%)</td><td>498.50 <b>(-32.74%)</b></td><td>244.10 <b>(-33.96%)</b></td><td>1291.36 (+6.47%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>1.42 (n/a)</td><td>0.77 (n/a)</td><td>0.71 (n/a)</td><td>0.16 (n/a)</td><td>0.48 (n/a)</td><td>3309.00 (n/a)</td><td>1180.32 (n/a)</td><td>741.20 (n/a)</td><td>369.60 (n/a)</td><td>1212.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>2.75 (+6.63%)</td><td>1.67 (-5.03%)</td><td>1.82 (-1.89%)</td><td>0.30 (-4.64%)</td><td>0.88 (-2.48%)</td><td>3539.50 (+4.86%)</td><td>1141.14 (+5.08%)</td><td>577.60 (+1.94%)</td><td>381.50 (-6.22%)</td><td>1344.15 (+4.71%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>2.58 (n/a)</td><td>1.76 (n/a)</td><td>1.85 (n/a)</td><td>0.31 (n/a)</td><td>0.90 (n/a)</td><td>3375.40 (n/a)</td><td>1086.02 (n/a)</td><td>566.60 (n/a)</td><td>406.80 (n/a)</td><td>1283.72 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.68 (+17.61%)</td><td>1.67 (-14.26%)</td><td>0.82 <b>(-56.92%)</b></td><td>0.56 (-2.67%)</td><td>1.44 <b>(+46.59%)</b></td><td>3752.90 (+2.74%)</td><td>2246.82 <b>(+48.07%)</b></td><td>2552.50 <b>(+132.13%)</b></td><td>570.00 (-14.96%)</td><td>1510.59 <b>(+23.60%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.13 (n/a)</td><td>1.95 (n/a)</td><td>1.91 (n/a)</td><td>0.57 (n/a)</td><td>0.98 (n/a)</td><td>3652.70 (n/a)</td><td>1517.44 (n/a)</td><td>1099.60 (n/a)</td><td>670.30 (n/a)</td><td>1222.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>2.16 <b>(+75.35%)</b></td><td>1.36 <b>(+35.26%)</b></td><td>1.64 <b>(+70.22%)</b></td><td>0.27 <b>(-65.32%)</b></td><td>0.74 <b>(+323.28%)</b></td><td>1925.80 <b>(+188.34%)</b></td><td>663.96 <b>(+24.62%)</b></td><td>319.90 <b>(-41.25%)</b></td><td>242.20 <b>(-42.97%)</b></td><td>714.13 <b>(+655.83%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>1.23 (n/a)</td><td>1.01 (n/a)</td><td>0.96 (n/a)</td><td>0.78 (n/a)</td><td>0.18 (n/a)</td><td>667.90 (n/a)</td><td>532.78 (n/a)</td><td>544.50 (n/a)</td><td>424.70 (n/a)</td><td>94.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (-2.70%)</td><td>0.10 (+2.08%)</td><td>0.08 <b>(-37.45%)</b></td><td>0.07 <b>(+292.81%)</b></td><td>0.03 <b>(-50.44%)</b></td><td>502.40 <b>(-74.54%)</b></td><td>364.62 <b>(-45.96%)</b></td><td>395.30 <b>(+59.91%)</b></td><td>242.90 (+2.79%)</td><td>103.51 <b>(-86.19%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1973.40 (n/a)</td><td>674.78 (n/a)</td><td>247.20 (n/a)</td><td>236.30 (n/a)</td><td>749.66 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (+1.88%)</td><td>0.08 <b>(-20.58%)</b></td><td>0.07 <b>(-35.74%)</b></td><td>0.05 (-6.67%)</td><td>0.03 (+1.21%)</td><td>648.30 (+7.16%)</td><td>431.36 <b>(+25.40%)</b></td><td>441.30 <b>(+55.66%)</b></td><td>246.80 (-1.87%)</td><td>146.16 (-1.04%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>605.00 (n/a)</td><td>343.98 (n/a)</td><td>283.50 (n/a)</td><td>251.50 (n/a)</td><td>147.69 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.27 (+18.45%)</td><td>0.17 (+11.70%)</td><td>0.15 <b>(+28.82%)</b></td><td>0.11 (-0.31%)</td><td>0.07 (+12.04%)</td><td>604.80 (+0.32%)</td><td>422.54 (-10.12%)</td><td>443.40 <b>(-22.37%)</b></td><td>245.00 (-15.58%)</td><td>151.67 (-5.49%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>602.90 (n/a)</td><td>470.14 (n/a)</td><td>571.20 (n/a)</td><td>290.20 (n/a)</td><td>160.49 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.26 <b>(+35.08%)</b></td><td>0.17 <b>(+23.08%)</b></td><td>0.13 (+0.25%)</td><td>0.11 (+2.17%)</td><td>0.07 <b>(+108.43%)</b></td><td>586.20 (-2.14%)</td><td>429.38 (-12.25%)</td><td>488.90 (-0.24%)</td><td>252.00 <b>(-25.99%)</b></td><td>149.18 <b>(+52.67%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>599.00 (n/a)</td><td>489.34 (n/a)</td><td>490.10 (n/a)</td><td>340.50 (n/a)</td><td>97.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.29 (-1.67%)</td><td>0.20 (-2.35%)</td><td>0.25 <b>(+20.56%)</b></td><td>0.10 <b>(-24.02%)</b></td><td>0.08 (+18.56%)</td><td>629.60 <b>(+31.61%)</b></td><td>387.14 (+10.32%)</td><td>265.90 (-17.06%)</td><td>228.80 (+1.69%)</td><td>186.68 <b>(+53.94%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>478.40 (n/a)</td><td>350.94 (n/a)</td><td>320.60 (n/a)</td><td>225.00 (n/a)</td><td>121.27 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.50 (+7.24%)</td><td>0.41 <b>(+65.00%)</b></td><td>0.42 <b>(+65.46%)</b></td><td>0.25 <b>(+259.74%)</b></td><td>0.10 <b>(-30.42%)</b></td><td>521.60 <b>(-72.20%)</b></td><td>336.06 <b>(-55.86%)</b></td><td>310.50 <b>(-39.57%)</b></td><td>263.60 (-6.76%)</td><td>106.28 <b>(-83.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.46 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>0.14 (n/a)</td><td>1876.50 (n/a)</td><td>761.28 (n/a)</td><td>513.80 (n/a)</td><td>282.70 (n/a)</td><td>635.74 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.53 (-5.37%)</td><td>0.37 (-7.37%)</td><td>0.35 (-19.16%)</td><td>0.22 (-19.71%)</td><td>0.14 (+14.42%)</td><td>600.80 <b>(+24.54%)</b></td><td>395.98 (+12.39%)</td><td>378.40 <b>(+23.70%)</b></td><td>249.00 (+5.64%)</td><td>148.97 <b>(+39.48%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.56 (n/a)</td><td>0.40 (n/a)</td><td>0.43 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>482.40 (n/a)</td><td>352.34 (n/a)</td><td>305.90 (n/a)</td><td>235.70 (n/a)</td><td>106.80 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.46 (-15.78%)</td><td>0.35 (+0.97%)</td><td>0.34 (+4.48%)</td><td>0.25 (+13.91%)</td><td>0.08 <b>(-37.60%)</b></td><td>527.10 (-12.22%)</td><td>389.10 (-6.95%)</td><td>390.00 (-4.29%)</td><td>285.70 (+18.74%)</td><td>93.88 <b>(-35.71%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.54 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>600.50 (n/a)</td><td>418.16 (n/a)</td><td>407.50 (n/a)</td><td>240.60 (n/a)</td><td>146.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (-16.74%)</td><td>0.04 <b>(-38.84%)</b></td><td>0.04 <b>(-45.49%)</b></td><td>0.02 <b>(-40.47%)</b></td><td>0.01 (+7.58%)</td><td>682.30 <b>(+67.97%)</b></td><td>484.76 <b>(+71.18%)</b></td><td>454.60 <b>(+83.45%)</b></td><td>284.50 <b>(+20.09%)</b></td><td>149.58 <b>(+110.46%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>406.20 (n/a)</td><td>283.18 (n/a)</td><td>247.80 (n/a)</td><td>236.90 (n/a)</td><td>71.08 (n/a)</td>
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
