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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (-19.33%)</td><td>0.02 (-2.28%)</td><td>0.02 (+17.75%)</td><td>0.01 <b>(-25.35%)</b></td><td>0.01 (-1.30%)</td><td>633.80 <b>(+33.97%)</b></td><td>434.04 (+8.14%)</td><td>368.90 (-15.08%)</td><td>270.10 <b>(+23.96%)</b></td><td>181.71 <b>(+74.52%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>473.10 (n/a)</td><td>401.38 (n/a)</td><td>434.40 (n/a)</td><td>217.90 (n/a)</td><td>104.12 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (-19.23%)</td><td>0.02 (-3.31%)</td><td>0.02 (+6.18%)</td><td>0.02 <b>(+37.82%)</b></td><td>0.00 <b>(-59.20%)</b></td><td>401.70 <b>(-27.44%)</b></td><td>330.96 (-7.41%)</td><td>316.70 (-5.83%)</td><td>264.90 <b>(+23.79%)</b></td><td>55.36 <b>(-61.80%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.60 (n/a)</td><td>357.46 (n/a)</td><td>336.30 (n/a)</td><td>214.00 (n/a)</td><td>144.93 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (-1.12%)</td><td>0.02 (+7.76%)</td><td>0.01 (+10.34%)</td><td>0.01 (+17.67%)</td><td>0.01 (-6.73%)</td><td>523.50 (-15.03%)</td><td>388.18 (-10.18%)</td><td>439.60 (-9.38%)</td><td>239.50 (+1.14%)</td><td>129.89 <b>(-20.62%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.10 (n/a)</td><td>432.18 (n/a)</td><td>485.10 (n/a)</td><td>236.80 (n/a)</td><td>163.62 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (-3.66%)</td><td>0.02 <b>(+36.75%)</b></td><td>0.02 <b>(+83.34%)</b></td><td>0.01 <b>(+77.03%)</b></td><td>0.01 (-8.79%)</td><td>636.50 <b>(-43.52%)</b></td><td>398.14 <b>(-33.99%)</b></td><td>287.40 <b>(-45.46%)</b></td><td>230.40 (+3.78%)</td><td>192.40 <b>(-42.89%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1126.90 (n/a)</td><td>603.12 (n/a)</td><td>527.00 (n/a)</td><td>222.00 (n/a)</td><td>336.88 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 <b>(+44.44%)</b></td><td>0.02 <b>(+57.92%)</b></td><td>0.02 <b>(+126.66%)</b></td><td>0.00 <b>(-47.49%)</b></td><td>0.01 <b>(+121.83%)</b></td><td>1897.10 <b>(+90.45%)</b></td><td>626.66 (+1.43%)</td><td>264.40 <b>(-55.87%)</b></td><td>243.60 <b>(-30.76%)</b></td><td>715.92 <b>(+196.76%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>996.10 (n/a)</td><td>617.80 (n/a)</td><td>599.20 (n/a)</td><td>351.80 (n/a)</td><td>241.25 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 <b>(+20.08%)</b></td><td>0.01 <b>(+40.15%)</b></td><td>0.01 <b>(+40.89%)</b></td><td>0.01 <b>(+257.94%)</b></td><td>0.00 (-18.01%)</td><td>634.60 <b>(-72.06%)</b></td><td>452.28 <b>(-48.57%)</b></td><td>438.70 <b>(-29.02%)</b></td><td>280.70 (-16.71%)</td><td>127.75 <b>(-83.76%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2271.60 (n/a)</td><td>879.44 (n/a)</td><td>618.10 (n/a)</td><td>337.00 (n/a)</td><td>786.84 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (+10.10%)</td><td>0.04 (+16.69%)</td><td>0.04 (-11.99%)</td><td>0.02 <b>(+270.84%)</b></td><td>0.02 <b>(-24.24%)</b></td><td>560.90 <b>(-73.04%)</b></td><td>338.04 <b>(-49.63%)</b></td><td>324.50 (+13.62%)</td><td>194.10 (-9.17%)</td><td>137.89 <b>(-82.66%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2080.20 (n/a)</td><td>671.14 (n/a)</td><td>285.60 (n/a)</td><td>213.70 (n/a)</td><td>795.22 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 <b>(+36.99%)</b></td><td>0.04 (+19.63%)</td><td>0.04 <b>(+34.05%)</b></td><td>0.02 (-5.71%)</td><td>0.01 <b>(+94.52%)</b></td><td>577.10 (+6.05%)</td><td>390.88 (-10.21%)</td><td>330.40 <b>(-25.40%)</b></td><td>243.70 <b>(-27.01%)</b></td><td>145.85 <b>(+58.20%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.20 (n/a)</td><td>435.34 (n/a)</td><td>442.90 (n/a)</td><td>333.90 (n/a)</td><td>92.19 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (+11.90%)</td><td>0.04 (+0.09%)</td><td>0.04 (-19.20%)</td><td>0.02 (+13.56%)</td><td>0.01 (+8.03%)</td><td>593.80 (-11.94%)</td><td>361.56 (-1.63%)</td><td>345.70 <b>(+23.77%)</b></td><td>238.30 (-10.62%)</td><td>143.21 (-17.92%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>674.30 (n/a)</td><td>367.56 (n/a)</td><td>279.30 (n/a)</td><td>266.60 (n/a)</td><td>174.47 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (+6.04%)</td><td>0.03 (+8.17%)</td><td>0.03 <b>(+51.61%)</b></td><td>0.02 <b>(-23.79%)</b></td><td>0.01 (+14.28%)</td><td>748.00 <b>(+31.21%)</b></td><td>427.72 (-2.23%)</td><td>352.40 <b>(-34.04%)</b></td><td>245.70 (-5.68%)</td><td>209.89 <b>(+38.74%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>570.10 (n/a)</td><td>437.48 (n/a)</td><td>534.30 (n/a)</td><td>260.50 (n/a)</td><td>151.28 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (-1.95%)</td><td>0.03 <b>(-20.25%)</b></td><td>0.03 <b>(-36.54%)</b></td><td>0.01 <b>(-77.35%)</b></td><td>0.02 <b>(+79.62%)</b></td><td>2019.60 <b>(+341.44%)</b></td><td>710.58 <b>(+112.29%)</b></td><td>453.40 <b>(+57.59%)</b></td><td>235.70 (+1.99%)</td><td>747.99 <b>(+650.47%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>457.50 (n/a)</td><td>334.72 (n/a)</td><td>287.70 (n/a)</td><td>231.10 (n/a)</td><td>99.67 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 <b>(-42.51%)</b></td><td>0.04 (+9.28%)</td><td>0.04 <b>(+74.19%)</b></td><td>0.02 (+10.80%)</td><td>0.01 <b>(-60.32%)</b></td><td>579.40 (-9.74%)</td><td>350.30 <b>(-26.06%)</b></td><td>295.70 <b>(-42.58%)</b></td><td>249.10 <b>(+73.95%)</b></td><td>135.32 <b>(-32.81%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>641.90 (n/a)</td><td>473.76 (n/a)</td><td>515.00 (n/a)</td><td>143.20 (n/a)</td><td>201.41 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (+6.84%)</td><td>0.09 <b>(+44.77%)</b></td><td>0.10 (+19.86%)</td><td>0.09 <b>(+561.21%)</b></td><td>0.01 <b>(-78.51%)</b></td><td>285.60 <b>(-84.88%)</b></td><td>262.62 <b>(-59.75%)</b></td><td>252.90 (-16.59%)</td><td>240.60 (-6.38%)</td><td>21.35 <b>(-96.95%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1888.30 (n/a)</td><td>652.46 (n/a)</td><td>303.20 (n/a)</td><td>257.00 (n/a)</td><td>700.28 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 <b>(-28.96%)</b></td><td>0.08 (-6.57%)</td><td>0.10 (+1.39%)</td><td>0.05 (+1.60%)</td><td>0.02 <b>(-39.93%)</b></td><td>523.40 (-1.58%)</td><td>329.58 (-3.25%)</td><td>251.30 (-1.37%)</td><td>249.80 <b>(+40.81%)</b></td><td>120.56 <b>(-27.42%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>531.80 (n/a)</td><td>340.64 (n/a)</td><td>254.80 (n/a)</td><td>177.40 (n/a)</td><td>166.12 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.11 (+15.70%)</td><td>0.10 <b>(+128.81%)</b></td><td>0.11 <b>(+146.92%)</b></td><td>0.08 <b>(+675.40%)</b></td><td>0.01 <b>(-59.66%)</b></td><td>323.00 <b>(-87.10%)</b></td><td>249.66 <b>(-78.65%)</b></td><td>231.60 <b>(-59.50%)</b></td><td>222.20 (-13.57%)</td><td>42.40 <b>(-95.96%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2504.40 (n/a)</td><td>1169.52 (n/a)</td><td>571.80 (n/a)</td><td>257.10 (n/a)</td><td>1049.66 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (+14.60%)</td><td>0.07 (+3.19%)</td><td>0.09 (+3.64%)</td><td>0.04 (+17.59%)</td><td>0.03 <b>(+24.86%)</b></td><td>588.50 (-14.96%)</td><td>375.46 (-1.68%)</td><td>285.10 (-3.49%)</td><td>236.40 (-12.74%)</td><td>158.97 (-9.90%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>692.00 (n/a)</td><td>381.86 (n/a)</td><td>295.40 (n/a)</td><td>270.90 (n/a)</td><td>176.44 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (-1.38%)</td><td>0.06 (-0.60%)</td><td>0.05 (-8.71%)</td><td>0.04 (+2.13%)</td><td>0.03 (+0.26%)</td><td>642.80 (-2.09%)</td><td>476.60 (+0.83%)</td><td>543.50 (+9.53%)</td><td>247.90 (+1.39%)</td><td>173.09 (+0.34%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>656.50 (n/a)</td><td>472.68 (n/a)</td><td>496.20 (n/a)</td><td>244.50 (n/a)</td><td>172.51 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (+10.27%)</td><td>0.06 (-5.97%)</td><td>0.07 (+1.75%)</td><td>0.01 <b>(-61.82%)</b></td><td>0.03 <b>(+40.61%)</b></td><td>1694.90 <b>(+161.88%)</b></td><td>631.32 <b>(+50.10%)</b></td><td>376.40 (-1.72%)</td><td>244.20 (-9.32%)</td><td>605.46 <b>(+271.32%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>647.20 (n/a)</td><td>420.60 (n/a)</td><td>383.00 (n/a)</td><td>269.30 (n/a)</td><td>163.06 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.21 (+14.48%)</td><td>0.15 <b>(+34.36%)</b></td><td>0.14 <b>(+45.91%)</b></td><td>0.09 <b>(+219.55%)</b></td><td>0.06 (-11.31%)</td><td>576.00 <b>(-68.71%)</b></td><td>380.48 <b>(-46.58%)</b></td><td>348.90 <b>(-31.47%)</b></td><td>233.00 (-12.67%)</td><td>152.72 <b>(-76.49%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>1840.70 (n/a)</td><td>712.24 (n/a)</td><td>509.10 (n/a)</td><td>266.80 (n/a)</td><td>649.58 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.24 <b>(+41.32%)</b></td><td>0.15 <b>(+25.40%)</b></td><td>0.17 <b>(+29.54%)</b></td><td>0.08 (+2.19%)</td><td>0.07 <b>(+81.66%)</b></td><td>581.60 (-2.14%)</td><td>381.02 (-11.99%)</td><td>297.20 <b>(-22.83%)</b></td><td>208.30 <b>(-29.25%)</b></td><td>180.40 <b>(+32.16%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>594.30 (n/a)</td><td>432.94 (n/a)</td><td>385.10 (n/a)</td><td>294.40 (n/a)</td><td>136.51 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.20 <b>(+22.32%)</b></td><td>0.14 <b>(+51.83%)</b></td><td>0.15 <b>(+90.90%)</b></td><td>0.03 (-2.96%)</td><td>0.07 <b>(+42.84%)</b></td><td>1895.30 (+3.05%)</td><td>635.04 (-18.77%)</td><td>318.20 <b>(-47.62%)</b></td><td>246.40 (-18.25%)</td><td>709.72 (+16.32%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1839.20 (n/a)</td><td>781.80 (n/a)</td><td>607.50 (n/a)</td><td>301.40 (n/a)</td><td>610.15 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.18 (-0.56%)</td><td>0.11 (+7.38%)</td><td>0.10 (+4.08%)</td><td>0.08 <b>(+77.99%)</b></td><td>0.04 (-15.85%)</td><td>640.40 <b>(-43.81%)</b></td><td>492.76 (-17.28%)</td><td>498.60 (-3.93%)</td><td>266.30 (+0.57%)</td><td>152.74 <b>(-53.53%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1139.80 (n/a)</td><td>595.72 (n/a)</td><td>519.00 (n/a)</td><td>264.80 (n/a)</td><td>328.70 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.22 <b>(+51.66%)</b></td><td>0.12 (+10.32%)</td><td>0.09 (-7.96%)</td><td>0.08 (-6.98%)</td><td>0.06 <b>(+149.71%)</b></td><td>651.80 (+7.50%)</td><td>484.26 (+0.39%)</td><td>533.30 (+8.64%)</td><td>224.70 <b>(-34.07%)</b></td><td>159.28 <b>(+68.82%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>606.30 (n/a)</td><td>482.40 (n/a)</td><td>490.90 (n/a)</td><td>340.80 (n/a)</td><td>94.35 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.20 (-17.53%)</td><td>0.15 (-0.44%)</td><td>0.15 (+3.61%)</td><td>0.09 (-7.46%)</td><td>0.04 <b>(-27.37%)</b></td><td>534.80 (+8.06%)</td><td>362.46 (-2.07%)</td><td>337.50 (-3.49%)</td><td>250.70 <b>(+21.29%)</b></td><td>110.39 (-1.99%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>494.90 (n/a)</td><td>370.12 (n/a)</td><td>349.70 (n/a)</td><td>206.70 (n/a)</td><td>112.63 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (+17.01%)</td><td>0.01 <b>(+67.18%)</b></td><td>0.01 <b>(+58.25%)</b></td><td>0.00 <b>(+272.57%)</b></td><td>0.00 <b>(-26.05%)</b></td><td>532.80 <b>(-73.16%)</b></td><td>383.94 <b>(-62.57%)</b></td><td>312.40 <b>(-36.81%)</b></td><td>262.60 (-14.55%)</td><td>127.93 <b>(-84.62%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1984.80 (n/a)</td><td>1025.74 (n/a)</td><td>494.40 (n/a)</td><td>307.30 (n/a)</td><td>831.68 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (+4.52%)</td><td>0.01 (-11.24%)</td><td>0.01 (-13.37%)</td><td>0.01 (-9.43%)</td><td>0.00 <b>(+27.03%)</b></td><td>460.10 (+10.42%)</td><td>331.24 (+15.58%)</td><td>310.50 (+15.43%)</td><td>213.40 (-4.30%)</td><td>95.89 <b>(+27.61%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>416.70 (n/a)</td><td>286.58 (n/a)</td><td>269.00 (n/a)</td><td>223.00 (n/a)</td><td>75.14 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 <b>(-24.05%)</b></td><td>0.01 (-14.52%)</td><td>0.01 (-16.55%)</td><td>0.00 (-9.35%)</td><td>0.00 <b>(-36.04%)</b></td><td>585.90 (+10.30%)</td><td>369.68 (+10.15%)</td><td>321.50 (+19.83%)</td><td>243.70 <b>(+31.66%)</b></td><td>134.71 (-8.62%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>531.20 (n/a)</td><td>335.62 (n/a)</td><td>268.30 (n/a)</td><td>185.10 (n/a)</td><td>147.42 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (+5.24%)</td><td>0.01 (-4.56%)</td><td>0.01 (-10.10%)</td><td>0.00 (-7.21%)</td><td>0.00 (+19.02%)</td><td>647.20 (+7.76%)</td><td>429.98 (+9.21%)</td><td>452.10 (+11.25%)</td><td>246.20 (-4.98%)</td><td>169.44 <b>(+22.33%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>600.60 (n/a)</td><td>393.72 (n/a)</td><td>406.40 (n/a)</td><td>259.10 (n/a)</td><td>138.52 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 <b>(-23.49%)</b></td><td>0.01 <b>(-26.76%)</b></td><td>0.01 <b>(-43.37%)</b></td><td>0.00 <b>(-21.34%)</b></td><td>0.00 (-4.17%)</td><td>615.90 <b>(+27.12%)</b></td><td>424.94 <b>(+42.54%)</b></td><td>485.90 <b>(+76.56%)</b></td><td>237.90 <b>(+30.71%)</b></td><td>164.07 <b>(+46.78%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>484.50 (n/a)</td><td>298.12 (n/a)</td><td>275.20 (n/a)</td><td>182.00 (n/a)</td><td>111.78 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (+3.49%)</td><td>0.01 (-7.39%)</td><td>0.01 (-2.76%)</td><td>0.00 (-9.81%)</td><td>0.00 (-1.91%)</td><td>618.20 (+10.89%)</td><td>454.16 (+7.82%)</td><td>481.60 (+2.84%)</td><td>268.00 (-3.35%)</td><td>126.92 (+2.55%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>557.50 (n/a)</td><td>421.24 (n/a)</td><td>468.30 (n/a)</td><td>277.30 (n/a)</td><td>123.76 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (-7.49%)</td><td>0.02 (-5.65%)</td><td>0.01 <b>(-21.08%)</b></td><td>0.01 (+6.16%)</td><td>0.01 (-3.14%)</td><td>471.50 (-5.79%)</td><td>349.52 (+5.33%)</td><td>372.80 <b>(+26.72%)</b></td><td>224.00 (+8.11%)</td><td>115.04 (-5.05%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>500.50 (n/a)</td><td>331.84 (n/a)</td><td>294.20 (n/a)</td><td>207.20 (n/a)</td><td>121.16 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 <b>(+32.20%)</b></td><td>0.02 <b>(+26.25%)</b></td><td>0.02 (+13.86%)</td><td>0.01 <b>(+60.87%)</b></td><td>0.01 <b>(+23.17%)</b></td><td>627.70 <b>(-37.84%)</b></td><td>375.76 <b>(-24.94%)</b></td><td>296.50 (-12.17%)</td><td>221.10 <b>(-24.38%)</b></td><td>181.36 <b>(-40.94%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1009.80 (n/a)</td><td>500.62 (n/a)</td><td>337.60 (n/a)</td><td>292.40 (n/a)</td><td>307.07 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+15.10%)</td><td>0.02 <b>(+67.15%)</b></td><td>0.02 <b>(+151.75%)</b></td><td>0.02 <b>(+186.17%)</b></td><td>0.00 <b>(-57.21%)</b></td><td>286.10 <b>(-65.05%)</b></td><td>248.52 <b>(-50.96%)</b></td><td>232.80 <b>(-60.27%)</b></td><td>212.30 (-13.13%)</td><td>34.23 <b>(-85.77%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>818.70 (n/a)</td><td>506.72 (n/a)</td><td>586.00 (n/a)</td><td>244.40 (n/a)</td><td>240.59 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+9.64%)</td><td>0.02 (-3.17%)</td><td>0.02 (-10.05%)</td><td>0.01 (+1.43%)</td><td>0.01 (+13.52%)</td><td>603.80 (-1.40%)</td><td>352.14 (+4.71%)</td><td>287.00 (+11.20%)</td><td>222.90 (-8.80%)</td><td>158.06 (+0.34%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.40 (n/a)</td><td>336.30 (n/a)</td><td>258.10 (n/a)</td><td>244.40 (n/a)</td><td>157.52 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+8.84%)</td><td>0.01 (-1.07%)</td><td>0.01 <b>(-23.48%)</b></td><td>0.01 <b>(+82.11%)</b></td><td>0.01 (-15.61%)</td><td>528.60 <b>(-45.09%)</b></td><td>407.50 (-12.34%)</td><td>436.10 <b>(+30.69%)</b></td><td>230.70 (-8.12%)</td><td>115.32 <b>(-60.48%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>962.60 (n/a)</td><td>464.88 (n/a)</td><td>333.70 (n/a)</td><td>251.10 (n/a)</td><td>291.78 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (-7.04%)</td><td>0.01 (-2.53%)</td><td>0.01 (+19.56%)</td><td>0.01 <b>(+29.74%)</b></td><td>0.01 (-15.77%)</td><td>1020.60 <b>(-22.92%)</b></td><td>537.20 (-8.65%)</td><td>394.90 (-16.37%)</td><td>252.90 (+7.57%)</td><td>304.12 <b>(-29.93%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1324.10 (n/a)</td><td>588.04 (n/a)</td><td>472.20 (n/a)</td><td>235.10 (n/a)</td><td>434.00 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 <b>(-22.63%)</b></td><td>0.03 (+5.96%)</td><td>0.03 <b>(+45.67%)</b></td><td>0.02 (+15.98%)</td><td>0.01 <b>(-48.28%)</b></td><td>422.50 (-13.78%)</td><td>330.12 (-12.69%)</td><td>304.10 <b>(-31.34%)</b></td><td>265.30 <b>(+29.23%)</b></td><td>70.13 <b>(-43.73%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>490.00 (n/a)</td><td>378.12 (n/a)</td><td>442.90 (n/a)</td><td>205.30 (n/a)</td><td>124.65 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (+6.52%)</td><td>0.04 (+16.48%)</td><td>0.04 <b>(+26.06%)</b></td><td>0.02 (+4.23%)</td><td>0.01 (-12.29%)</td><td>492.70 (-4.05%)</td><td>312.72 (-16.41%)</td><td>297.20 <b>(-20.66%)</b></td><td>231.60 (-6.12%)</td><td>105.61 (-16.98%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.50 (n/a)</td><td>374.12 (n/a)</td><td>374.60 (n/a)</td><td>246.70 (n/a)</td><td>127.21 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (+2.23%)</td><td>0.04 (+19.14%)</td><td>0.04 <b>(+49.65%)</b></td><td>0.02 (+12.08%)</td><td>0.01 <b>(-26.44%)</b></td><td>420.20 (-10.77%)</td><td>297.76 (-19.35%)</td><td>281.20 <b>(-33.19%)</b></td><td>240.70 (-2.19%)</td><td>72.20 <b>(-33.33%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>470.90 (n/a)</td><td>369.18 (n/a)</td><td>420.90 (n/a)</td><td>246.10 (n/a)</td><td>108.29 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 <b>(+44.56%)</b></td><td>0.03 <b>(+29.79%)</b></td><td>0.03 (+9.69%)</td><td>0.02 <b>(+35.46%)</b></td><td>0.01 <b>(+103.36%)</b></td><td>622.60 <b>(-26.17%)</b></td><td>421.72 (-16.70%)</td><td>416.90 (-8.83%)</td><td>235.80 <b>(-30.83%)</b></td><td>182.88 (-5.94%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>843.30 (n/a)</td><td>506.24 (n/a)</td><td>457.30 (n/a)</td><td>340.90 (n/a)</td><td>194.44 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (+1.43%)</td><td>0.03 <b>(-20.75%)</b></td><td>0.02 <b>(-41.04%)</b></td><td>0.02 <b>(-21.18%)</b></td><td>0.01 (+5.10%)</td><td>626.20 <b>(+26.86%)</b></td><td>444.82 <b>(+29.16%)</b></td><td>462.40 <b>(+69.63%)</b></td><td>243.10 (-1.42%)</td><td>147.55 <b>(+27.37%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.60 (n/a)</td><td>344.40 (n/a)</td><td>272.60 (n/a)</td><td>246.60 (n/a)</td><td>115.84 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 <b>(-21.88%)</b></td><td>0.02 (-15.58%)</td><td>0.02 <b>(-20.39%)</b></td><td>0.02 (-10.96%)</td><td>0.00 <b>(-39.19%)</b></td><td>664.70 (+12.30%)</td><td>543.60 (+15.07%)</td><td>551.50 <b>(+25.60%)</b></td><td>391.50 <b>(+28.02%)</b></td><td>97.77 (-18.55%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>591.90 (n/a)</td><td>472.40 (n/a)</td><td>439.10 (n/a)</td><td>305.80 (n/a)</td><td>120.03 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 <b>(+49.00%)</b></td><td>0.06 <b>(+20.79%)</b></td><td>0.07 <b>(+36.92%)</b></td><td>0.03 (-11.61%)</td><td>0.02 <b>(+148.95%)</b></td><td>657.60 (+13.15%)</td><td>409.24 (-6.92%)</td><td>298.80 <b>(-26.96%)</b></td><td>241.50 <b>(-32.90%)</b></td><td>183.78 <b>(+97.66%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>581.20 (n/a)</td><td>439.66 (n/a)</td><td>409.10 (n/a)</td><td>359.90 (n/a)</td><td>92.98 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (+12.12%)</td><td>0.07 (+6.61%)</td><td>0.09 <b>(+22.07%)</b></td><td>0.02 <b>(-47.61%)</b></td><td>0.03 <b>(+46.69%)</b></td><td>1076.00 <b>(+90.88%)</b></td><td>450.40 (+17.71%)</td><td>245.00 (-18.09%)</td><td>231.20 (-10.80%)</td><td>362.18 <b>(+140.90%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>563.70 (n/a)</td><td>382.62 (n/a)</td><td>299.10 (n/a)</td><td>259.20 (n/a)</td><td>150.35 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (+6.70%)</td><td>0.05 (-7.20%)</td><td>0.04 <b>(-29.52%)</b></td><td>0.03 (-11.71%)</td><td>0.02 <b>(+36.82%)</b></td><td>605.40 (+13.26%)</td><td>440.72 (+15.08%)</td><td>490.70 <b>(+41.86%)</b></td><td>249.90 (-6.30%)</td><td>168.27 <b>(+43.23%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>534.50 (n/a)</td><td>382.96 (n/a)</td><td>345.90 (n/a)</td><td>266.70 (n/a)</td><td>117.48 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 <b>(+78.28%)</b></td><td>0.07 <b>(+66.37%)</b></td><td>0.08 <b>(+75.91%)</b></td><td>0.05 <b>(+34.41%)</b></td><td>0.02 <b>(+217.53%)</b></td><td>394.10 <b>(-25.60%)</b></td><td>292.06 <b>(-38.05%)</b></td><td>259.60 <b>(-43.16%)</b></td><td>231.90 <b>(-43.90%)</b></td><td>68.53 <b>(+30.03%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>529.70 (n/a)</td><td>471.46 (n/a)</td><td>456.70 (n/a)</td><td>413.40 (n/a)</td><td>52.70 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 <b>(+21.96%)</b></td><td>0.06 <b>(+43.67%)</b></td><td>0.07 <b>(+68.38%)</b></td><td>0.03 <b>(+72.65%)</b></td><td>0.02 <b>(+34.81%)</b></td><td>620.40 <b>(-42.08%)</b></td><td>405.78 <b>(-31.05%)</b></td><td>320.30 <b>(-40.61%)</b></td><td>243.60 (-18.03%)</td><td>184.70 <b>(-36.34%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1071.10 (n/a)</td><td>588.50 (n/a)</td><td>539.30 (n/a)</td><td>297.20 (n/a)</td><td>290.14 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (-6.55%)</td><td>0.05 (+6.48%)</td><td>0.06 <b>(+22.99%)</b></td><td>0.03 (+12.68%)</td><td>0.01 <b>(-31.40%)</b></td><td>605.20 (-11.26%)</td><td>410.60 (-10.86%)</td><td>381.60 (-18.70%)</td><td>305.40 (+7.01%)</td><td>114.70 <b>(-29.51%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>682.00 (n/a)</td><td>460.60 (n/a)</td><td>469.40 (n/a)</td><td>285.40 (n/a)</td><td>162.71 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>433.70 (n/a)</td><td>282.10 (n/a)</td><td>235.20 (n/a)</td><td>182.20 (n/a)</td><td>101.22 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.60 (n/a)</td><td>377.26 (n/a)</td><td>318.80 (n/a)</td><td>228.10 (n/a)</td><td>168.91 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.10 (n/a)</td><td>465.64 (n/a)</td><td>458.70 (n/a)</td><td>310.50 (n/a)</td><td>123.68 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>693.10 (n/a)</td><td>488.68 (n/a)</td><td>555.60 (n/a)</td><td>206.50 (n/a)</td><td>193.89 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>625.00 (n/a)</td><td>419.42 (n/a)</td><td>304.60 (n/a)</td><td>263.60 (n/a)</td><td>183.23 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>450.80 (n/a)</td><td>314.88 (n/a)</td><td>314.90 (n/a)</td><td>225.80 (n/a)</td><td>89.25 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>617.70 (n/a)</td><td>477.16 (n/a)</td><td>470.20 (n/a)</td><td>262.60 (n/a)</td><td>146.37 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>612.60 (n/a)</td><td>391.92 (n/a)</td><td>297.80 (n/a)</td><td>260.20 (n/a)</td><td>153.76 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>519.20 (n/a)</td><td>418.56 (n/a)</td><td>474.80 (n/a)</td><td>231.30 (n/a)</td><td>125.15 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.19 (-1.80%)</td><td>0.14 (+2.57%)</td><td>0.17 <b>(+32.30%)</b></td><td>0.09 (-8.44%)</td><td>0.05 (+2.88%)</td><td>573.10 (+9.20%)</td><td>386.42 (-0.52%)</td><td>291.80 <b>(-24.42%)</b></td><td>253.30 (+1.81%)</td><td>156.04 (+16.86%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>524.80 (n/a)</td><td>388.44 (n/a)</td><td>386.10 (n/a)</td><td>248.80 (n/a)</td><td>133.53 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>527.00 (n/a)</td><td>370.06 (n/a)</td><td>328.70 (n/a)</td><td>248.00 (n/a)</td><td>131.44 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>680.90 (n/a)</td><td>400.82 (n/a)</td><td>319.00 (n/a)</td><td>231.10 (n/a)</td><td>198.90 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>648.60 (n/a)</td><td>371.28 (n/a)</td><td>295.50 (n/a)</td><td>204.60 (n/a)</td><td>186.32 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>773.60 (n/a)</td><td>546.08 (n/a)</td><td>586.30 (n/a)</td><td>233.50 (n/a)</td><td>197.39 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1346.90 (n/a)</td><td>610.74 (n/a)</td><td>523.90 (n/a)</td><td>243.00 (n/a)</td><td>428.74 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>307.80 (n/a)</td><td>288.88 (n/a)</td><td>292.50 (n/a)</td><td>254.90 (n/a)</td><td>20.10 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.60 (n/a)</td><td>424.18 (n/a)</td><td>466.10 (n/a)</td><td>234.00 (n/a)</td><td>121.99 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>564.80 (n/a)</td><td>409.58 (n/a)</td><td>366.00 (n/a)</td><td>303.70 (n/a)</td><td>115.37 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>456.50 (n/a)</td><td>370.42 (n/a)</td><td>347.00 (n/a)</td><td>291.20 (n/a)</td><td>79.43 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1042.50 (n/a)</td><td>606.36 (n/a)</td><td>537.50 (n/a)</td><td>277.60 (n/a)</td><td>280.73 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>762.70 (n/a)</td><td>445.88 (n/a)</td><td>465.30 (n/a)</td><td>218.70 (n/a)</td><td>216.27 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>568.70 (n/a)</td><td>406.22 (n/a)</td><td>320.60 (n/a)</td><td>292.20 (n/a)</td><td>139.18 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>1944.10 (n/a)</td><td>673.16 (n/a)</td><td>398.70 (n/a)</td><td>259.90 (n/a)</td><td>715.36 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.90 (n/a)</td><td>512.82 (n/a)</td><td>549.10 (n/a)</td><td>222.40 (n/a)</td><td>167.18 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>298.60 (n/a)</td><td>255.78 (n/a)</td><td>241.90 (n/a)</td><td>233.90 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.90 (n/a)</td><td>359.68 (n/a)</td><td>263.60 (n/a)</td><td>233.40 (n/a)</td><td>155.32 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>453.40 (n/a)</td><td>287.98 (n/a)</td><td>249.20 (n/a)</td><td>212.80 (n/a)</td><td>98.28 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.80 (n/a)</td><td>376.14 (n/a)</td><td>273.70 (n/a)</td><td>263.40 (n/a)</td><td>150.23 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>441.10 (n/a)</td><td>347.68 (n/a)</td><td>356.10 (n/a)</td><td>217.20 (n/a)</td><td>93.61 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.00 (n/a)</td><td>407.02 (n/a)</td><td>462.70 (n/a)</td><td>262.00 (n/a)</td><td>105.15 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>642.50 (n/a)</td><td>474.02 (n/a)</td><td>560.10 (n/a)</td><td>244.30 (n/a)</td><td>173.95 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.60 (n/a)</td><td>431.90 (n/a)</td><td>532.10 (n/a)</td><td>226.70 (n/a)</td><td>160.07 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.80 (n/a)</td><td>448.44 (n/a)</td><td>503.60 (n/a)</td><td>264.40 (n/a)</td><td>124.42 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.20 (n/a)</td><td>355.04 (n/a)</td><td>286.50 (n/a)</td><td>181.10 (n/a)</td><td>173.33 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.10 (n/a)</td><td>422.66 (n/a)</td><td>360.60 (n/a)</td><td>291.20 (n/a)</td><td>143.39 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>726.40 (n/a)</td><td>472.56 (n/a)</td><td>411.20 (n/a)</td><td>267.10 (n/a)</td><td>223.28 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>470.10 (n/a)</td><td>372.02 (n/a)</td><td>410.80 (n/a)</td><td>253.90 (n/a)</td><td>97.76 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>798.80 (n/a)</td><td>517.14 (n/a)</td><td>459.50 (n/a)</td><td>322.60 (n/a)</td><td>177.12 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>620.00 (n/a)</td><td>440.40 (n/a)</td><td>469.40 (n/a)</td><td>262.10 (n/a)</td><td>171.52 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.40 (n/a)</td><td>488.70 (n/a)</td><td>524.50 (n/a)</td><td>262.90 (n/a)</td><td>130.76 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>677.00 (n/a)</td><td>468.66 (n/a)</td><td>506.70 (n/a)</td><td>303.90 (n/a)</td><td>162.34 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1905.90 (n/a)</td><td>687.56 (n/a)</td><td>414.00 (n/a)</td><td>275.10 (n/a)</td><td>688.19 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>608.10 (n/a)</td><td>372.18 (n/a)</td><td>308.40 (n/a)</td><td>244.30 (n/a)</td><td>143.41 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>556.30 (n/a)</td><td>385.04 (n/a)</td><td>349.80 (n/a)</td><td>252.50 (n/a)</td><td>130.03 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>490.40 (n/a)</td><td>368.86 (n/a)</td><td>424.30 (n/a)</td><td>193.10 (n/a)</td><td>139.55 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>532.80 (n/a)</td><td>446.40 (n/a)</td><td>507.60 (n/a)</td><td>332.70 (n/a)</td><td>101.83 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.58 (+18.78%)</td><td>0.49 <b>(+25.93%)</b></td><td>0.48 <b>(+20.92%)</b></td><td>0.43 <b>(+116.92%)</b></td><td>0.06 <b>(-50.01%)</b></td><td>509.10 <b>(-53.91%)</b></td><td>457.94 <b>(-27.61%)</b></td><td>459.50 (-17.30%)</td><td>381.70 (-15.83%)</td><td>49.41 <b>(-81.62%)</b></td><td>24.72 (+18.78%)</td><td>20.81 <b>(+25.93%)</b></td><td>20.54 <b>(+20.92%)</b></td><td>18.54 <b>(+116.92%)</b></td><td>2.42 <b>(-50.01%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.49 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>1104.50 (n/a)</td><td>632.62 (n/a)</td><td>555.60 (n/a)</td><td>453.50 (n/a)</td><td>268.79 (n/a)</td><td>20.81 (n/a)</td><td>16.53 (n/a)</td><td>16.98 (n/a)</td><td>8.54 (n/a)</td><td>4.84 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.59 (+4.91%)</td><td>0.41 (+3.62%)</td><td>0.43 (-8.75%)</td><td>0.12 <b>(-36.96%)</b></td><td>0.18 (-6.38%)</td><td>1917.40 <b>(+58.63%)</b></td><td>764.06 (+4.20%)</td><td>515.60 (+9.59%)</td><td>375.30 (-4.70%)</td><td>649.28 <b>(+51.48%)</b></td><td>25.14 (+4.91%)</td><td>17.28 (+3.62%)</td><td>18.30 (-8.75%)</td><td>4.92 <b>(-36.96%)</b></td><td>7.68 (-6.38%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.47 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>1208.70 (n/a)</td><td>733.26 (n/a)</td><td>470.50 (n/a)</td><td>393.80 (n/a)</td><td>428.64 (n/a)</td><td>23.97 (n/a)</td><td>16.68 (n/a)</td><td>20.06 (n/a)</td><td>7.81 (n/a)</td><td>8.20 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.31 (+0.27%)</td><td>0.30 (-0.71%)</td><td>0.30 (-0.94%)</td><td>0.30 (-0.99%)</td><td>0.01 <b>(+30.85%)</b></td><td>84728.40 (+1.00%)</td><td>83025.82 (+0.72%)</td><td>83436.20 (+0.95%)</td><td>80683.90 (-0.27%)</td><td>1495.76 <b>(+31.53%)</b></td><td>212.93 (+0.27%)</td><td>206.98 (-0.71%)</td><td>205.90 (-0.94%)</td><td>202.76 (-0.99%)</td><td>3.77 <b>(+30.86%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83890.40 (n/a)</td><td>82431.34 (n/a)</td><td>82655.10 (n/a)</td><td>80898.60 (n/a)</td><td>1137.21 (n/a)</td><td>212.36 (n/a)</td><td>208.45 (n/a)</td><td>207.85 (n/a)</td><td>204.79 (n/a)</td><td>2.88 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>1.03 (-1.04%)</td><td>1.00 (-2.25%)</td><td>1.01 (-2.12%)</td><td>0.97 (-3.25%)</td><td>0.02 <b>(+62.04%)</b></td><td>25907.80 (+3.36%)</td><td>25118.26 (+2.33%)</td><td>25024.50 (+2.17%)</td><td>24408.20 (+1.05%)</td><td>560.21 <b>(+69.06%)</b></td><td>703.86 (-1.04%)</td><td>684.23 (-2.25%)</td><td>686.52 (-2.12%)</td><td>663.12 (-3.25%)</td><td>15.20 <b>(+62.04%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>1.04 (n/a)</td><td>1.03 (n/a)</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25066.50 (n/a)</td><td>24546.76 (n/a)</td><td>24494.00 (n/a)</td><td>24154.70 (n/a)</td><td>331.36 (n/a)</td><td>711.24 (n/a)</td><td>699.98 (n/a)</td><td>701.39 (n/a)</td><td>685.37 (n/a)</td><td>9.38 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.81 (-0.36%)</td><td>0.80 (-0.10%)</td><td>0.81 (+0.36%)</td><td>0.78 (-0.07%)</td><td>0.02 (-6.11%)</td><td>97213.40 (+0.07%)</td><td>94325.52 (+0.10%)</td><td>93170.40 (-0.36%)</td><td>92640.90 (+0.36%)</td><td>2011.13 (-5.67%)</td><td>741.78 (-0.36%)</td><td>728.80 (-0.10%)</td><td>737.57 (+0.36%)</td><td>706.89 (-0.07%)</td><td>15.37 (-6.11%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.78 (n/a)</td><td>0.02 (n/a)</td><td>97150.20 (n/a)</td><td>94235.16 (n/a)</td><td>93508.50 (n/a)</td><td>92310.50 (n/a)</td><td>2132.09 (n/a)</td><td>744.44 (n/a)</td><td>729.53 (n/a)</td><td>734.90 (n/a)</td><td>707.35 (n/a)</td><td>16.36 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.78 (+1.98%)</td><td>0.77 (+1.74%)</td><td>0.77 (+1.67%)</td><td>0.76 (+0.96%)</td><td>0.01 <b>(+59.67%)</b></td><td>99968.20 (-0.95%)</td><td>98382.02 (-1.71%)</td><td>98237.40 (-1.64%)</td><td>97230.00 (-1.94%)</td><td>1199.25 <b>(+54.64%)</b></td><td>706.77 (+1.98%)</td><td>698.58 (+1.74%)</td><td>699.52 (+1.67%)</td><td>687.41 (+0.96%)</td><td>8.49 <b>(+59.67%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100930.60 (n/a)</td><td>100089.70 (n/a)</td><td>99878.00 (n/a)</td><td>99152.20 (n/a)</td><td>775.52 (n/a)</td><td>693.07 (n/a)</td><td>686.61 (n/a)</td><td>688.03 (n/a)</td><td>680.86 (n/a)</td><td>5.32 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.81 (+1.06%)</td><td>0.80 (+0.70%)</td><td>0.80 (+0.96%)</td><td>0.79 (+0.37%)</td><td>0.01 <b>(+61.21%)</b></td><td>95925.50 (-0.37%)</td><td>94808.20 (-0.69%)</td><td>94545.70 (-0.95%)</td><td>93752.70 (-1.05%)</td><td>873.75 <b>(+58.98%)</b></td><td>732.99 (+1.06%)</td><td>724.88 (+0.70%)</td><td>726.84 (+0.96%)</td><td>716.38 (+0.37%)</td><td>6.67 <b>(+61.21%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96280.50 (n/a)</td><td>95465.60 (n/a)</td><td>95451.30 (n/a)</td><td>94743.00 (n/a)</td><td>549.59 (n/a)</td><td>725.33 (n/a)</td><td>719.85 (n/a)</td><td>719.94 (n/a)</td><td>713.74 (n/a)</td><td>4.14 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>4.98 (+3.37%)</td><td>3.29 (-14.10%)</td><td>2.71 <b>(-32.82%)</b></td><td>2.17 (+0.13%)</td><td>1.19 <b>(+20.22%)</b></td><td>4109.70 (-0.13%)</td><td>2984.06 (+18.72%)</td><td>3292.30 <b>(+48.86%)</b></td><td>1790.60 (-3.26%)</td><td>963.00 (+6.03%)</td><td>299.83 (+3.37%)</td><td>198.02 (-14.10%)</td><td>163.07 <b>(-32.82%)</b></td><td>130.64 (+0.13%)</td><td>71.44 <b>(+20.22%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>4.82 (n/a)</td><td>3.83 (n/a)</td><td>4.03 (n/a)</td><td>2.17 (n/a)</td><td>0.99 (n/a)</td><td>4115.00 (n/a)</td><td>2513.52 (n/a)</td><td>2211.70 (n/a)</td><td>1851.00 (n/a)</td><td>908.23 (n/a)</td><td>290.05 (n/a)</td><td>230.51 (n/a)</td><td>242.74 (n/a)</td><td>130.47 (n/a)</td><td>59.42 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>4.68 (+7.43%)</td><td>2.95 (+1.34%)</td><td>2.79 (-1.88%)</td><td>2.04 (-7.05%)</td><td>1.04 (+18.78%)</td><td>4363.20 (+7.58%)</td><td>3277.98 (+0.80%)</td><td>3199.10 (+1.91%)</td><td>1903.00 (-6.91%)</td><td>956.74 (+15.40%)</td><td>282.11 (+7.43%)</td><td>177.99 (+1.34%)</td><td>167.82 (-1.88%)</td><td>123.05 (-7.05%)</td><td>62.87 (+18.78%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>4.36 (n/a)</td><td>2.92 (n/a)</td><td>2.84 (n/a)</td><td>2.20 (n/a)</td><td>0.88 (n/a)</td><td>4055.70 (n/a)</td><td>3251.96 (n/a)</td><td>3139.00 (n/a)</td><td>2044.30 (n/a)</td><td>829.09 (n/a)</td><td>262.61 (n/a)</td><td>175.64 (n/a)</td><td>171.03 (n/a)</td><td>132.37 (n/a)</td><td>52.93 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>5.53 (-0.39%)</td><td>4.19 (-7.25%)</td><td>4.10 (+0.24%)</td><td>2.80 <b>(-22.61%)</b></td><td>1.09 <b>(+30.69%)</b></td><td>3185.10 <b>(+29.22%)</b></td><td>2255.48 (+11.26%)</td><td>2173.40 (-0.24%)</td><td>1611.20 (+0.39%)</td><td>623.41 <b>(+72.69%)</b></td><td>333.21 (-0.39%)</td><td>252.20 (-7.25%)</td><td>247.02 (+0.24%)</td><td>168.56 <b>(-22.61%)</b></td><td>65.43 <b>(+30.69%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.55 (n/a)</td><td>4.51 (n/a)</td><td>4.09 (n/a)</td><td>3.62 (n/a)</td><td>0.83 (n/a)</td><td>2464.90 (n/a)</td><td>2027.28 (n/a)</td><td>2178.70 (n/a)</td><td>1604.90 (n/a)</td><td>361.01 (n/a)</td><td>334.51 (n/a)</td><td>271.92 (n/a)</td><td>246.42 (n/a)</td><td>217.81 (n/a)</td><td>50.06 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>5.73 (-11.76%)</td><td>4.97 (-8.92%)</td><td>4.95 (-5.20%)</td><td>4.24 (-17.21%)</td><td>0.60 (+2.81%)</td><td>8219.30 <b>(+20.78%)</b></td><td>7094.72 (+10.19%)</td><td>7036.60 (+5.48%)</td><td>6079.80 (+13.32%)</td><td>859.58 <b>(+42.43%)</b></td><td>353.22 (-11.76%)</td><td>306.25 (-8.92%)</td><td>305.19 (-5.20%)</td><td>261.27 (-17.21%)</td><td>36.94 (+2.81%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>6.50 (n/a)</td><td>5.46 (n/a)</td><td>5.23 (n/a)</td><td>5.12 (n/a)</td><td>0.58 (n/a)</td><td>6805.10 (n/a)</td><td>6438.44 (n/a)</td><td>6671.00 (n/a)</td><td>5365.00 (n/a)</td><td>603.53 (n/a)</td><td>400.27 (n/a)</td><td>336.23 (n/a)</td><td>321.91 (n/a)</td><td>315.57 (n/a)</td><td>35.93 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.07 (-1.19%)</td><td>5.19 (-1.58%)</td><td>4.87 (-2.58%)</td><td>4.52 (+2.52%)</td><td>0.70 (-4.71%)</td><td>7719.90 (-2.46%)</td><td>6816.42 (+1.47%)</td><td>7162.10 (+2.64%)</td><td>5745.20 (+1.20%)</td><td>881.88 (-4.84%)</td><td>373.79 (-1.19%)</td><td>319.49 (-1.58%)</td><td>299.84 (-2.58%)</td><td>278.17 (+2.52%)</td><td>42.99 (-4.71%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>6.14 (n/a)</td><td>5.27 (n/a)</td><td>5.00 (n/a)</td><td>4.41 (n/a)</td><td>0.73 (n/a)</td><td>7914.70 (n/a)</td><td>6717.98 (n/a)</td><td>6977.60 (n/a)</td><td>5677.10 (n/a)</td><td>926.79 (n/a)</td><td>378.27 (n/a)</td><td>324.62 (n/a)</td><td>307.77 (n/a)</td><td>271.33 (n/a)</td><td>45.12 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.49 (-0.24%)</td><td>5.44 (-8.23%)</td><td>5.49 (-14.92%)</td><td>4.06 (-16.60%)</td><td>0.92 (+19.28%)</td><td>8577.30 (+19.90%)</td><td>6570.66 (+10.17%)</td><td>6354.00 (+17.54%)</td><td>5375.80 (+0.24%)</td><td>1238.36 <b>(+48.84%)</b></td><td>399.47 (-0.24%)</td><td>335.29 (-8.23%)</td><td>337.97 (-14.92%)</td><td>250.37 (-16.60%)</td><td>56.73 (+19.28%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>6.50 (n/a)</td><td>5.93 (n/a)</td><td>6.45 (n/a)</td><td>4.87 (n/a)</td><td>0.77 (n/a)</td><td>7153.70 (n/a)</td><td>5963.90 (n/a)</td><td>5405.90 (n/a)</td><td>5362.80 (n/a)</td><td>832.00 (n/a)</td><td>400.44 (n/a)</td><td>365.38 (n/a)</td><td>397.25 (n/a)</td><td>300.19 (n/a)</td><td>47.56 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.77 (-1.64%)</td><td>0.75 (-3.32%)</td><td>0.75 (-3.70%)</td><td>0.74 (-3.89%)</td><td>0.01 <b>(+110.68%)</b></td><td>102063.90 (+4.04%)</td><td>100186.96 (+3.46%)</td><td>100198.50 (+3.85%)</td><td>97725.90 (+1.67%)</td><td>1910.42 <b>(+123.70%)</b></td><td>703.19 (-1.64%)</td><td>686.11 (-3.32%)</td><td>685.83 (-3.70%)</td><td>673.30 (-3.89%)</td><td>13.12 <b>(+110.68%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>98096.70 (n/a)</td><td>96837.60 (n/a)</td><td>96486.70 (n/a)</td><td>96119.30 (n/a)</td><td>854.03 (n/a)</td><td>714.94 (n/a)</td><td>709.68 (n/a)</td><td>712.22 (n/a)</td><td>700.53 (n/a)</td><td>6.23 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.78 (+0.78%)</td><td>0.76 (+1.23%)</td><td>0.76 (+1.06%)</td><td>0.75 (+1.43%)</td><td>0.01 (-18.41%)</td><td>100755.00 (-1.41%)</td><td>98959.82 (-1.22%)</td><td>99027.00 (-1.05%)</td><td>96247.70 (-0.77%)</td><td>1687.13 <b>(-20.53%)</b></td><td>713.99 (+0.78%)</td><td>694.58 (+1.23%)</td><td>693.95 (+1.06%)</td><td>682.04 (+1.43%)</td><td>11.99 (-18.41%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>102191.20 (n/a)</td><td>100185.96 (n/a)</td><td>100079.20 (n/a)</td><td>96995.10 (n/a)</td><td>2122.98 (n/a)</td><td>708.48 (n/a)</td><td>686.17 (n/a)</td><td>686.65 (n/a)</td><td>672.46 (n/a)</td><td>14.69 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.81 (+1.13%)</td><td>0.80 (+1.04%)</td><td>0.80 (+0.88%)</td><td>0.79 (+1.48%)</td><td>0.01 (-18.49%)</td><td>95685.10 (-1.46%)</td><td>94404.16 (-1.03%)</td><td>94341.80 (-0.88%)</td><td>93395.50 (-1.12%)</td><td>822.03 <b>(-20.59%)</b></td><td>735.79 (+1.13%)</td><td>727.97 (+1.04%)</td><td>728.41 (+0.88%)</td><td>718.18 (+1.48%)</td><td>6.31 (-18.49%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>97102.40 (n/a)</td><td>95390.38 (n/a)</td><td>95175.80 (n/a)</td><td>94449.30 (n/a)</td><td>1035.18 (n/a)</td><td>727.58 (n/a)</td><td>720.47 (n/a)</td><td>722.03 (n/a)</td><td>707.70 (n/a)</td><td>7.75 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.36 (-9.36%)</td><td>2.90 (+5.70%)</td><td>3.30 (+8.05%)</td><td>2.24 <b>(+67.64%)</b></td><td>0.59 <b>(-39.45%)</b></td><td>3591.70 <b>(-40.35%)</b></td><td>2888.32 (-14.62%)</td><td>2439.70 (-7.45%)</td><td>2398.30 (+10.33%)</td><td>637.41 <b>(-60.03%)</b></td><td>881.42 (-9.36%)</td><td>759.28 (+5.70%)</td><td>866.47 (+8.05%)</td><td>588.56 <b>(+67.64%)</b></td><td>155.14 <b>(-39.45%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.71 (n/a)</td><td>2.74 (n/a)</td><td>3.06 (n/a)</td><td>1.34 (n/a)</td><td>0.98 (n/a)</td><td>6021.20 (n/a)</td><td>3382.82 (n/a)</td><td>2636.10 (n/a)</td><td>2173.70 (n/a)</td><td>1594.70 (n/a)</td><td>972.48 (n/a)</td><td>718.30 (n/a)</td><td>801.92 (n/a)</td><td>351.08 (n/a)</td><td>256.21 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.31 <b>(+25.64%)</b></td><td>0.24 (+11.44%)</td><td>0.22 (+9.11%)</td><td>0.18 (-6.64%)</td><td>0.06 <b>(+141.24%)</b></td><td>7088.00 (+7.11%)</td><td>5504.50 (-6.79%)</td><td>5541.20 (-8.35%)</td><td>4070.80 <b>(-20.40%)</b></td><td>1327.14 <b>(+103.20%)</b></td><td>16.49 <b>(+25.63%)</b></td><td>12.79 (+11.44%)</td><td>12.11 (+9.11%)</td><td>9.47 (-6.64%)</td><td>3.13 <b>(+141.24%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>6617.40 (n/a)</td><td>5905.64 (n/a)</td><td>6045.90 (n/a)</td><td>5114.30 (n/a)</td><td>653.11 (n/a)</td><td>13.12 (n/a)</td><td>11.48 (n/a)</td><td>11.10 (n/a)</td><td>10.14 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.89 (n/a)</td><td>3.66 (n/a)</td><td>3.76 (n/a)</td><td>3.34 (n/a)</td><td>0.22 (n/a)</td><td>3.89 (n/a)</td><td>3.66 (n/a)</td><td>3.76 (n/a)</td><td>3.34 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>7.60 (-1.70%)</td><td>6.01 (-13.90%)</td><td>5.66 <b>(-23.14%)</b></td><td>5.44 (-9.37%)</td><td>0.90 <b>(+23.26%)</b></td><td>7.59 (-1.70%)</td><td>6.01 (-13.90%)</td><td>5.66 <b>(-23.14%)</b></td><td>5.43 (-9.37%)</td><td>0.90 <b>(+23.26%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>7.73 (n/a)</td><td>6.98 (n/a)</td><td>7.37 (n/a)</td><td>6.00 (n/a)</td><td>0.73 (n/a)</td><td>7.72 (n/a)</td><td>6.98 (n/a)</td><td>7.36 (n/a)</td><td>6.00 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>11.83 (-15.80%)</td><td>9.07 <b>(-27.49%)</b></td><td>8.44 <b>(-36.87%)</b></td><td>6.91 (-17.59%)</td><td>1.89 (-19.71%)</td><td>11.82 (-15.80%)</td><td>9.06 <b>(-27.49%)</b></td><td>8.43 <b>(-36.87%)</b></td><td>6.91 (-17.59%)</td><td>1.89 (-19.71%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>14.05 (n/a)</td><td>12.50 (n/a)</td><td>13.37 (n/a)</td><td>8.38 (n/a)</td><td>2.36 (n/a)</td><td>14.04 (n/a)</td><td>12.50 (n/a)</td><td>13.36 (n/a)</td><td>8.38 (n/a)</td><td>2.35 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.88 (n/a)</td><td>3.76 (n/a)</td><td>3.71 (n/a)</td><td>3.67 (n/a)</td><td>0.09 (n/a)</td><td>3.88 (n/a)</td><td>3.76 (n/a)</td><td>3.71 (n/a)</td><td>3.66 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.59 (-12.61%)</td><td>6.02 (-3.13%)</td><td>6.02 (+2.65%)</td><td>5.52 (-1.95%)</td><td>0.38 <b>(-50.68%)</b></td><td>6.59 (-12.61%)</td><td>6.01 (-3.13%)</td><td>6.02 (+2.65%)</td><td>5.52 (-1.95%)</td><td>0.38 <b>(-50.68%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>7.54 (n/a)</td><td>6.21 (n/a)</td><td>5.86 (n/a)</td><td>5.63 (n/a)</td><td>0.78 (n/a)</td><td>7.54 (n/a)</td><td>6.21 (n/a)</td><td>5.86 (n/a)</td><td>5.63 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>13.88 (-1.62%)</td><td>10.66 (+11.23%)</td><td>9.76 <b>(+20.49%)</b></td><td>8.17 (+5.29%)</td><td>2.67 (+0.31%)</td><td>13.87 (-1.62%)</td><td>10.66 (+11.23%)</td><td>9.76 <b>(+20.49%)</b></td><td>8.16 (+5.29%)</td><td>2.67 (+0.31%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>14.11 (n/a)</td><td>9.59 (n/a)</td><td>8.10 (n/a)</td><td>7.76 (n/a)</td><td>2.66 (n/a)</td><td>14.10 (n/a)</td><td>9.58 (n/a)</td><td>8.10 (n/a)</td><td>7.75 (n/a)</td><td>2.66 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.03 (-4.16%)</td><td>1.73 <b>(-32.35%)</b></td><td>1.70 <b>(-37.10%)</b></td><td>1.05 <b>(-31.46%)</b></td><td>0.79 <b>(+25.27%)</b></td><td>3.02 (-4.16%)</td><td>1.73 <b>(-32.35%)</b></td><td>1.70 <b>(-37.10%)</b></td><td>1.04 <b>(-31.46%)</b></td><td>0.79 <b>(+25.27%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.16 (n/a)</td><td>2.56 (n/a)</td><td>2.70 (n/a)</td><td>1.53 (n/a)</td><td>0.63 (n/a)</td><td>3.15 (n/a)</td><td>2.56 (n/a)</td><td>2.70 (n/a)</td><td>1.52 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.45 (-5.86%)</td><td>0.37 (-4.33%)</td><td>0.43 (+16.14%)</td><td>0.23 (-9.19%)</td><td>0.10 (+7.84%)</td><td>0.44 (-5.86%)</td><td>0.36 (-4.33%)</td><td>0.43 (+16.14%)</td><td>0.22 (-9.19%)</td><td>0.10 (+7.84%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.48 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>0.47 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.50 <b>(-27.28%)</b></td><td>0.29 <b>(-36.89%)</b></td><td>0.33 <b>(-36.26%)</b></td><td>0.08 (-6.23%)</td><td>0.20 (-16.56%)</td><td>0.49 <b>(-27.28%)</b></td><td>0.29 <b>(-36.89%)</b></td><td>0.33 <b>(-36.26%)</b></td><td>0.08 (-6.23%)</td><td>0.20 (-16.56%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.68 (n/a)</td><td>0.46 (n/a)</td><td>0.52 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td><td>0.68 (n/a)</td><td>0.45 (n/a)</td><td>0.51 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>2.44 (-18.96%)</td><td>1.50 (-19.28%)</td><td>1.83 (-10.44%)</td><td>0.43 (-8.57%)</td><td>1.00 (+4.55%)</td><td>2.40 (-18.96%)</td><td>1.48 (-19.28%)</td><td>1.80 (-10.44%)</td><td>0.42 (-8.57%)</td><td>0.99 (+4.55%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.01 (n/a)</td><td>1.86 (n/a)</td><td>2.04 (n/a)</td><td>0.47 (n/a)</td><td>0.96 (n/a)</td><td>2.97 (n/a)</td><td>1.83 (n/a)</td><td>2.01 (n/a)</td><td>0.46 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>560.90 (n/a)</td><td>431.82 (n/a)</td><td>510.10 (n/a)</td><td>244.80 (n/a)</td><td>140.76 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>476.50 (n/a)</td><td>400.16 (n/a)</td><td>430.90 (n/a)</td><td>264.80 (n/a)</td><td>84.24 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1845.40 (n/a)</td><td>685.80 (n/a)</td><td>422.40 (n/a)</td><td>220.90 (n/a)</td><td>658.69 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.10 (n/a)</td><td>443.94 (n/a)</td><td>485.70 (n/a)</td><td>239.30 (n/a)</td><td>161.24 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>658.20 (n/a)</td><td>411.96 (n/a)</td><td>324.10 (n/a)</td><td>250.90 (n/a)</td><td>186.53 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1366.30 (n/a)</td><td>580.60 (n/a)</td><td>406.50 (n/a)</td><td>328.50 (n/a)</td><td>442.87 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>303.90 (n/a)</td><td>275.30 (n/a)</td><td>269.10 (n/a)</td><td>242.70 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>421.90 (n/a)</td><td>319.62 (n/a)</td><td>291.30 (n/a)</td><td>241.50 (n/a)</td><td>76.45 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.10 (n/a)</td><td>395.18 (n/a)</td><td>391.80 (n/a)</td><td>237.50 (n/a)</td><td>159.46 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.90 (n/a)</td><td>409.10 (n/a)</td><td>446.60 (n/a)</td><td>245.10 (n/a)</td><td>117.41 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1404.30 (n/a)</td><td>641.50 (n/a)</td><td>558.50 (n/a)</td><td>200.50 (n/a)</td><td>454.34 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.50 (n/a)</td><td>369.76 (n/a)</td><td>338.60 (n/a)</td><td>268.50 (n/a)</td><td>109.14 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>566.70 (n/a)</td><td>466.90 (n/a)</td><td>474.00 (n/a)</td><td>296.50 (n/a)</td><td>103.03 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>542.50 (n/a)</td><td>399.14 (n/a)</td><td>449.90 (n/a)</td><td>230.70 (n/a)</td><td>138.95 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>549.30 (n/a)</td><td>383.30 (n/a)</td><td>395.60 (n/a)</td><td>274.20 (n/a)</td><td>113.53 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>482.80 (n/a)</td><td>334.90 (n/a)</td><td>268.90 (n/a)</td><td>230.40 (n/a)</td><td>121.66 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>681.00 (n/a)</td><td>503.20 (n/a)</td><td>471.70 (n/a)</td><td>238.10 (n/a)</td><td>183.01 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>628.60 (n/a)</td><td>470.62 (n/a)</td><td>482.30 (n/a)</td><td>351.60 (n/a)</td><td>105.33 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (-15.39%)</td><td>0.07 (+8.85%)</td><td>0.06 (+12.35%)</td><td>0.05 <b>(+190.85%)</b></td><td>0.02 <b>(-42.69%)</b></td><td>678.90 <b>(-65.62%)</b></td><td>479.08 <b>(-38.15%)</b></td><td>532.80 (-10.99%)</td><td>317.90 (+18.18%)</td><td>153.39 <b>(-77.98%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1974.50 (n/a)</td><td>774.54 (n/a)</td><td>598.60 (n/a)</td><td>269.00 (n/a)</td><td>696.57 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>546.70 (n/a)</td><td>446.54 (n/a)</td><td>468.00 (n/a)</td><td>253.90 (n/a)</td><td>115.73 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>585.20 (n/a)</td><td>461.40 (n/a)</td><td>531.40 (n/a)</td><td>281.90 (n/a)</td><td>132.48 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>564.80 (n/a)</td><td>460.32 (n/a)</td><td>477.50 (n/a)</td><td>276.20 (n/a)</td><td>117.96 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>666.80 (n/a)</td><td>494.18 (n/a)</td><td>479.50 (n/a)</td><td>252.60 (n/a)</td><td>156.91 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>523.40 (n/a)</td><td>429.38 (n/a)</td><td>461.80 (n/a)</td><td>287.30 (n/a)</td><td>99.24 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+6.60%)</td><td>0.01 (+15.98%)</td><td>0.01 <b>(+43.83%)</b></td><td>0.01 <b>(+32.66%)</b></td><td>0.00 <b>(-31.44%)</b></td><td>438.40 <b>(-24.62%)</b></td><td>299.86 <b>(-20.56%)</b></td><td>287.30 <b>(-30.47%)</b></td><td>214.10 (-6.22%)</td><td>83.18 <b>(-44.53%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.60 (n/a)</td><td>377.48 (n/a)</td><td>413.20 (n/a)</td><td>228.30 (n/a)</td><td>149.98 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 <b>(+56.53%)</b></td><td>0.01 <b>(+36.43%)</b></td><td>0.01 (+19.09%)</td><td>0.01 (-4.68%)</td><td>0.00 <b>(+189.93%)</b></td><td>624.50 (+4.92%)</td><td>418.58 (-17.83%)</td><td>466.40 (-16.02%)</td><td>241.60 <b>(-36.12%)</b></td><td>166.37 <b>(+80.19%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>595.20 (n/a)</td><td>509.38 (n/a)</td><td>555.40 (n/a)</td><td>378.20 (n/a)</td><td>92.33 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 <b>(+21.70%)</b></td><td>0.01 <b>(+85.21%)</b></td><td>0.01 <b>(+59.06%)</b></td><td>0.01 <b>(+375.46%)</b></td><td>0.00 <b>(-30.20%)</b></td><td>517.20 <b>(-78.97%)</b></td><td>315.66 <b>(-71.52%)</b></td><td>285.50 <b>(-37.14%)</b></td><td>207.70 (-17.81%)</td><td>117.50 <b>(-88.40%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2459.10 (n/a)</td><td>1108.20 (n/a)</td><td>454.20 (n/a)</td><td>252.70 (n/a)</td><td>1013.01 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 <b>(+26.44%)</b></td><td>0.01 <b>(+30.71%)</b></td><td>0.01 <b>(+103.23%)</b></td><td>0.01 (+15.68%)</td><td>0.01 (+8.44%)</td><td>554.60 (-13.56%)</td><td>351.12 <b>(-25.35%)</b></td><td>285.60 <b>(-50.79%)</b></td><td>208.00 <b>(-20.91%)</b></td><td>149.10 <b>(-20.98%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.60 (n/a)</td><td>470.36 (n/a)</td><td>580.40 (n/a)</td><td>263.00 (n/a)</td><td>188.68 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 <b>(-30.01%)</b></td><td>0.01 <b>(-22.75%)</b></td><td>0.01 <b>(-38.44%)</b></td><td>0.01 (+17.23%)</td><td>0.00 <b>(-56.86%)</b></td><td>481.40 (-14.71%)</td><td>372.70 (+11.96%)</td><td>367.10 <b>(+62.43%)</b></td><td>276.90 <b>(+42.88%)</b></td><td>89.34 <b>(-47.75%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.40 (n/a)</td><td>332.88 (n/a)</td><td>226.00 (n/a)</td><td>193.80 (n/a)</td><td>170.98 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (+5.47%)</td><td>0.01 <b>(-26.34%)</b></td><td>0.01 <b>(-40.23%)</b></td><td>0.01 (-18.28%)</td><td>0.00 <b>(+47.16%)</b></td><td>612.80 <b>(+22.36%)</b></td><td>505.48 <b>(+41.59%)</b></td><td>545.70 <b>(+67.34%)</b></td><td>291.20 (-5.21%)</td><td>130.72 <b>(+61.54%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.80 (n/a)</td><td>357.00 (n/a)</td><td>326.10 (n/a)</td><td>307.20 (n/a)</td><td>80.92 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (-3.19%)</td><td>0.02 (-16.55%)</td><td>0.02 <b>(-38.89%)</b></td><td>0.01 <b>(-22.83%)</b></td><td>0.01 (+12.05%)</td><td>598.20 <b>(+29.56%)</b></td><td>416.92 <b>(+25.75%)</b></td><td>480.70 <b>(+63.61%)</b></td><td>232.30 (+3.29%)</td><td>158.10 <b>(+42.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>461.70 (n/a)</td><td>331.54 (n/a)</td><td>293.80 (n/a)</td><td>224.90 (n/a)</td><td>111.07 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 <b>(-37.51%)</b></td><td>0.03 (-10.01%)</td><td>0.03 (-11.39%)</td><td>0.03 <b>(+73.59%)</b></td><td>0.00 <b>(-85.11%)</b></td><td>284.90 <b>(-42.39%)</b></td><td>267.60 (-3.59%)</td><td>271.00 (+12.87%)</td><td>240.50 <b>(+60.01%)</b></td><td>16.75 <b>(-87.02%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.50 (n/a)</td><td>277.56 (n/a)</td><td>240.10 (n/a)</td><td>150.30 (n/a)</td><td>129.04 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (-8.86%)</td><td>0.02 (-19.56%)</td><td>0.02 <b>(-21.77%)</b></td><td>0.01 <b>(-36.13%)</b></td><td>0.01 <b>(+30.72%)</b></td><td>771.70 <b>(+56.56%)</b></td><td>430.08 <b>(+37.29%)</b></td><td>347.90 <b>(+27.81%)</b></td><td>259.40 (+9.73%)</td><td>213.77 <b>(+107.43%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.90 (n/a)</td><td>313.26 (n/a)</td><td>272.20 (n/a)</td><td>236.40 (n/a)</td><td>103.06 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (-4.38%)</td><td>0.03 (+13.71%)</td><td>0.03 (+5.38%)</td><td>0.02 (+18.99%)</td><td>0.01 <b>(-30.93%)</b></td><td>447.60 (-15.96%)</td><td>280.48 (-19.92%)</td><td>240.80 (-5.08%)</td><td>216.70 (+4.58%)</td><td>95.50 <b>(-41.22%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.60 (n/a)</td><td>350.24 (n/a)</td><td>253.70 (n/a)</td><td>207.20 (n/a)</td><td>162.48 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (+1.33%)</td><td>0.03 <b>(+24.77%)</b></td><td>0.03 (+16.36%)</td><td>0.03 <b>(+89.23%)</b></td><td>0.00 <b>(-53.50%)</b></td><td>310.50 <b>(-47.16%)</b></td><td>256.56 <b>(-27.83%)</b></td><td>240.50 (-14.08%)</td><td>226.20 (-1.31%)</td><td>35.56 <b>(-76.07%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.60 (n/a)</td><td>355.48 (n/a)</td><td>279.90 (n/a)</td><td>229.20 (n/a)</td><td>148.61 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (-19.49%)</td><td>0.03 (+11.61%)</td><td>0.03 <b>(+55.49%)</b></td><td>0.02 <b>(+29.26%)</b></td><td>0.01 <b>(-29.11%)</b></td><td>503.30 <b>(-22.63%)</b></td><td>359.12 (-17.41%)</td><td>278.20 <b>(-35.68%)</b></td><td>258.30 <b>(+24.18%)</b></td><td>125.97 <b>(-31.64%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.50 (n/a)</td><td>434.84 (n/a)</td><td>432.50 (n/a)</td><td>208.00 (n/a)</td><td>184.27 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 <b>(+25.24%)</b></td><td>0.02 (+9.65%)</td><td>0.02 (+0.44%)</td><td>0.01 <b>(-41.61%)</b></td><td>0.01 <b>(+72.38%)</b></td><td>1056.70 <b>(+71.26%)</b></td><td>488.70 (+15.29%)</td><td>417.60 (-0.43%)</td><td>190.80 <b>(-20.17%)</b></td><td>340.00 <b>(+150.81%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.00 (n/a)</td><td>423.90 (n/a)</td><td>419.40 (n/a)</td><td>239.00 (n/a)</td><td>135.56 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 <b>(+30.29%)</b></td><td>0.02 (+9.95%)</td><td>0.02 (-5.30%)</td><td>0.01 (-1.97%)</td><td>0.01 <b>(+132.87%)</b></td><td>584.20 (+2.01%)</td><td>437.26 (-1.92%)</td><td>462.50 (+5.59%)</td><td>269.10 <b>(-23.27%)</b></td><td>145.30 <b>(+81.22%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.70 (n/a)</td><td>445.84 (n/a)</td><td>438.00 (n/a)</td><td>350.70 (n/a)</td><td>80.18 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (-3.72%)</td><td>0.06 <b>(+24.02%)</b></td><td>0.07 <b>(+86.87%)</b></td><td>0.04 (+15.13%)</td><td>0.02 <b>(-32.54%)</b></td><td>438.70 (-13.15%)</td><td>278.32 <b>(-25.47%)</b></td><td>243.90 <b>(-46.48%)</b></td><td>213.00 (+3.85%)</td><td>91.29 <b>(-35.54%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>505.10 (n/a)</td><td>373.44 (n/a)</td><td>455.70 (n/a)</td><td>205.10 (n/a)</td><td>141.62 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (+8.81%)</td><td>0.05 <b>(+48.82%)</b></td><td>0.04 <b>(+40.45%)</b></td><td>0.03 <b>(+156.97%)</b></td><td>0.02 (-5.88%)</td><td>527.20 <b>(-61.09%)</b></td><td>369.64 <b>(-43.58%)</b></td><td>402.40 <b>(-28.79%)</b></td><td>228.50 (-8.09%)</td><td>129.74 <b>(-68.62%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1354.80 (n/a)</td><td>655.18 (n/a)</td><td>565.10 (n/a)</td><td>248.60 (n/a)</td><td>413.48 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (+0.28%)</td><td>0.06 (-3.30%)</td><td>0.06 (-9.99%)</td><td>0.03 (+3.97%)</td><td>0.02 (-5.91%)</td><td>480.80 (-3.82%)</td><td>295.96 (+1.94%)</td><td>267.70 (+11.08%)</td><td>217.80 (-0.27%)</td><td>105.86 (-10.15%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>499.90 (n/a)</td><td>290.34 (n/a)</td><td>241.00 (n/a)</td><td>218.40 (n/a)</td><td>117.81 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 <b>(-23.59%)</b></td><td>0.04 <b>(-29.43%)</b></td><td>0.03 <b>(-46.82%)</b></td><td>0.03 (-8.96%)</td><td>0.01 <b>(-37.81%)</b></td><td>567.40 (+9.85%)</td><td>455.86 <b>(+33.64%)</b></td><td>489.30 <b>(+88.05%)</b></td><td>276.00 <b>(+30.87%)</b></td><td>120.21 (-14.53%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>516.50 (n/a)</td><td>341.10 (n/a)</td><td>260.20 (n/a)</td><td>210.90 (n/a)</td><td>140.64 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (+0.26%)</td><td>0.05 (+11.08%)</td><td>0.07 <b>(+59.33%)</b></td><td>0.03 (-3.52%)</td><td>0.02 (+13.31%)</td><td>475.80 (+3.66%)</td><td>327.56 (-7.78%)</td><td>252.00 <b>(-37.24%)</b></td><td>228.60 (-0.26%)</td><td>116.45 (+19.52%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>459.00 (n/a)</td><td>355.20 (n/a)</td><td>401.50 (n/a)</td><td>229.20 (n/a)</td><td>97.43 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (+12.99%)</td><td>0.04 (+8.43%)</td><td>0.04 <b>(+21.44%)</b></td><td>0.03 <b>(+23.80%)</b></td><td>0.01 (-10.62%)</td><td>474.70 (-19.23%)</td><td>384.36 (-10.40%)</td><td>377.90 (-17.65%)</td><td>261.10 (-11.49%)</td><td>85.41 <b>(-32.47%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>587.70 (n/a)</td><td>428.98 (n/a)</td><td>458.90 (n/a)</td><td>295.00 (n/a)</td><td>126.47 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (+13.85%)</td><td>0.11 <b>(+20.13%)</b></td><td>0.14 <b>(+87.45%)</b></td><td>0.06 (+7.03%)</td><td>0.04 (+17.51%)</td><td>570.30 (-6.57%)</td><td>346.30 (-14.36%)</td><td>242.10 <b>(-46.65%)</b></td><td>216.30 (-12.14%)</td><td>161.76 (+4.13%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>610.40 (n/a)</td><td>404.36 (n/a)</td><td>453.80 (n/a)</td><td>246.20 (n/a)</td><td>155.35 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (-6.34%)</td><td>0.12 (+1.91%)</td><td>0.13 (-1.56%)</td><td>0.06 (-13.80%)</td><td>0.03 (-4.53%)</td><td>510.20 (+16.01%)</td><td>304.10 (-0.74%)</td><td>254.30 (+1.56%)</td><td>242.50 (+6.78%)</td><td>115.57 <b>(+22.45%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>439.80 (n/a)</td><td>306.36 (n/a)</td><td>250.40 (n/a)</td><td>227.10 (n/a)</td><td>94.38 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.11 <b>(-24.10%)</b></td><td>0.08 <b>(-28.48%)</b></td><td>0.07 <b>(-46.50%)</b></td><td>0.06 (-2.03%)</td><td>0.02 <b>(-47.95%)</b></td><td>556.00 (+2.06%)</td><td>429.08 <b>(+28.45%)</b></td><td>453.70 <b>(+86.94%)</b></td><td>287.90 <b>(+31.76%)</b></td><td>103.04 <b>(-29.81%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>544.80 (n/a)</td><td>334.04 (n/a)</td><td>242.70 (n/a)</td><td>218.50 (n/a)</td><td>146.80 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (+7.80%)</td><td>0.08 (+0.12%)</td><td>0.07 <b>(-23.78%)</b></td><td>0.06 <b>(+253.21%)</b></td><td>0.04 <b>(-22.72%)</b></td><td>595.70 <b>(-71.69%)</b></td><td>451.54 <b>(-37.46%)</b></td><td>493.90 <b>(+31.22%)</b></td><td>224.30 (-7.24%)</td><td>143.56 <b>(-81.72%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2104.00 (n/a)</td><td>721.98 (n/a)</td><td>376.40 (n/a)</td><td>241.80 (n/a)</td><td>785.25 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 <b>(-42.94%)</b></td><td>0.07 <b>(-39.57%)</b></td><td>0.07 <b>(-35.61%)</b></td><td>0.03 <b>(-62.44%)</b></td><td>0.03 <b>(-39.45%)</b></td><td>1259.50 <b>(+166.22%)</b></td><td>616.98 <b>(+80.70%)</b></td><td>485.20 <b>(+55.31%)</b></td><td>280.00 <b>(+75.22%)</b></td><td>381.47 <b>(+186.00%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>473.10 (n/a)</td><td>341.44 (n/a)</td><td>312.40 (n/a)</td><td>159.80 (n/a)</td><td>133.38 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+6.34%)</td><td>0.01 (+13.00%)</td><td>0.01 <b>(-24.70%)</b></td><td>0.01 <b>(+330.97%)</b></td><td>0.00 <b>(-33.47%)</b></td><td>453.10 <b>(-76.80%)</b></td><td>349.24 <b>(-46.49%)</b></td><td>388.40 <b>(+32.79%)</b></td><td>229.00 (-5.95%)</td><td>99.78 <b>(-86.40%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1952.70 (n/a)</td><td>652.62 (n/a)</td><td>292.50 (n/a)</td><td>243.50 (n/a)</td><td>733.45 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (-5.90%)</td><td>0.02 (+6.22%)</td><td>0.02 (-2.22%)</td><td>0.02 <b>(+73.17%)</b></td><td>0.00 <b>(-77.54%)</b></td><td>264.70 <b>(-42.26%)</b></td><td>247.58 (-12.35%)</td><td>248.50 (+2.26%)</td><td>232.90 (+6.25%)</td><td>13.33 <b>(-86.69%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>458.40 (n/a)</td><td>282.48 (n/a)</td><td>243.00 (n/a)</td><td>219.20 (n/a)</td><td>100.19 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (-16.61%)</td><td>0.01 (+5.86%)</td><td>0.01 (-11.53%)</td><td>0.01 <b>(+414.70%)</b></td><td>0.00 <b>(-63.08%)</b></td><td>419.40 <b>(-80.57%)</b></td><td>298.34 <b>(-53.83%)</b></td><td>279.30 (+13.03%)</td><td>236.30 (+19.95%)</td><td>70.35 <b>(-91.71%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2158.70 (n/a)</td><td>646.12 (n/a)</td><td>247.10 (n/a)</td><td>197.00 (n/a)</td><td>848.98 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+1.89%)</td><td>0.01 (-5.20%)</td><td>0.01 <b>(+51.16%)</b></td><td>0.00 <b>(-74.14%)</b></td><td>0.01 <b>(+36.97%)</b></td><td>1871.50 <b>(+286.67%)</b></td><td>628.50 <b>(+67.04%)</b></td><td>285.50 <b>(-33.85%)</b></td><td>239.90 (-1.84%)</td><td>700.06 <b>(+474.76%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>484.00 (n/a)</td><td>376.26 (n/a)</td><td>431.60 (n/a)</td><td>244.40 (n/a)</td><td>121.80 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (-3.84%)</td><td>0.01 (-15.07%)</td><td>0.01 (-19.30%)</td><td>0.00 <b>(-43.88%)</b></td><td>0.01 (+5.50%)</td><td>1057.50 <b>(+78.18%)</b></td><td>542.00 <b>(+32.86%)</b></td><td>531.90 <b>(+23.93%)</b></td><td>241.80 (+4.00%)</td><td>324.88 <b>(+95.71%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.50 (n/a)</td><td>407.94 (n/a)</td><td>429.20 (n/a)</td><td>232.50 (n/a)</td><td>166.01 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+16.29%)</td><td>0.01 (+7.84%)</td><td>0.01 <b>(+22.32%)</b></td><td>0.01 (+3.25%)</td><td>0.00 (+17.95%)</td><td>497.80 (-3.15%)</td><td>356.66 (-6.02%)</td><td>319.60 (-18.24%)</td><td>219.70 (-13.98%)</td><td>113.52 (+2.75%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.00 (n/a)</td><td>379.50 (n/a)</td><td>390.90 (n/a)</td><td>255.40 (n/a)</td><td>110.48 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (-4.08%)</td><td>0.01 <b>(-24.67%)</b></td><td>0.01 <b>(-42.10%)</b></td><td>0.01 (-7.28%)</td><td>0.00 <b>(-20.31%)</b></td><td>721.90 (+7.86%)</td><td>482.56 <b>(+27.24%)</b></td><td>457.00 <b>(+72.71%)</b></td><td>265.00 (+4.25%)</td><td>165.19 (-8.95%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>669.30 (n/a)</td><td>379.26 (n/a)</td><td>264.60 (n/a)</td><td>254.20 (n/a)</td><td>181.43 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 <b>(-23.17%)</b></td><td>0.01 <b>(-32.06%)</b></td><td>0.01 <b>(-48.45%)</b></td><td>0.00 <b>(-70.74%)</b></td><td>0.01 (+3.26%)</td><td>1830.90 <b>(+241.78%)</b></td><td>687.00 <b>(+105.90%)</b></td><td>520.20 <b>(+94.03%)</b></td><td>262.50 <b>(+30.14%)</b></td><td>651.70 <b>(+361.92%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>535.70 (n/a)</td><td>333.66 (n/a)</td><td>268.10 (n/a)</td><td>201.70 (n/a)</td><td>141.08 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+2.61%)</td><td>0.01 (+3.55%)</td><td>0.01 (-6.53%)</td><td>0.01 <b>(+213.01%)</b></td><td>0.00 <b>(-23.21%)</b></td><td>612.10 <b>(-68.05%)</b></td><td>435.64 <b>(-34.97%)</b></td><td>470.60 (+6.98%)</td><td>245.00 (-2.55%)</td><td>152.88 <b>(-78.23%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1915.90 (n/a)</td><td>669.92 (n/a)</td><td>439.90 (n/a)</td><td>251.40 (n/a)</td><td>702.27 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 <b>(-27.53%)</b></td><td>0.01 (-14.85%)</td><td>0.01 (-6.66%)</td><td>0.01 <b>(+28.03%)</b></td><td>0.00 <b>(-69.65%)</b></td><td>483.80 <b>(-21.89%)</b></td><td>414.88 (+3.21%)</td><td>418.60 (+7.14%)</td><td>330.90 <b>(+37.99%)</b></td><td>57.71 <b>(-65.53%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.40 (n/a)</td><td>401.98 (n/a)</td><td>390.70 (n/a)</td><td>239.80 (n/a)</td><td>167.40 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (-14.49%)</td><td>0.01 (-4.02%)</td><td>0.01 (+4.10%)</td><td>0.01 (+4.28%)</td><td>0.00 <b>(-24.98%)</b></td><td>520.50 (-4.11%)</td><td>405.12 (-1.91%)</td><td>457.10 (-3.93%)</td><td>213.60 (+16.91%)</td><td>129.10 (-17.41%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>542.80 (n/a)</td><td>413.02 (n/a)</td><td>475.80 (n/a)</td><td>182.70 (n/a)</td><td>156.32 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 <b>(-29.33%)</b></td><td>0.01 <b>(-28.79%)</b></td><td>0.01 (-2.78%)</td><td>0.00 <b>(-45.32%)</b></td><td>0.00 <b>(-30.94%)</b></td><td>1072.30 <b>(+82.86%)</b></td><td>595.62 <b>(+45.14%)</b></td><td>455.00 (+2.85%)</td><td>366.80 <b>(+41.51%)</b></td><td>283.04 <b>(+98.62%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>586.40 (n/a)</td><td>410.38 (n/a)</td><td>442.40 (n/a)</td><td>259.20 (n/a)</td><td>142.51 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 <b>(-25.10%)</b></td><td>0.02 <b>(-25.90%)</b></td><td>0.02 <b>(-44.88%)</b></td><td>0.01 <b>(+217.10%)</b></td><td>0.01 <b>(-59.91%)</b></td><td>614.10 <b>(-68.47%)</b></td><td>483.38 <b>(-23.66%)</b></td><td>487.90 <b>(+81.44%)</b></td><td>302.30 <b>(+33.52%)</b></td><td>113.70 <b>(-84.66%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1947.40 (n/a)</td><td>633.16 (n/a)</td><td>268.90 (n/a)</td><td>226.40 (n/a)</td><td>741.26 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (-3.84%)</td><td>0.03 (+1.85%)</td><td>0.03 <b>(+20.95%)</b></td><td>0.00 <b>(-72.54%)</b></td><td>0.01 <b>(+40.51%)</b></td><td>1880.90 <b>(+264.09%)</b></td><td>574.98 <b>(+70.29%)</b></td><td>241.30 (-17.33%)</td><td>218.30 (+4.00%)</td><td>730.86 <b>(+460.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.60 (n/a)</td><td>337.64 (n/a)</td><td>291.90 (n/a)</td><td>209.90 (n/a)</td><td>130.43 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (+1.51%)</td><td>0.02 (-14.91%)</td><td>0.02 <b>(-36.08%)</b></td><td>0.01 <b>(-20.07%)</b></td><td>0.01 <b>(+24.98%)</b></td><td>563.90 <b>(+25.09%)</b></td><td>411.08 <b>(+23.76%)</b></td><td>460.10 <b>(+56.44%)</b></td><td>237.30 (-1.49%)</td><td>143.22 <b>(+50.48%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>450.80 (n/a)</td><td>332.16 (n/a)</td><td>294.10 (n/a)</td><td>240.90 (n/a)</td><td>95.18 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (+7.80%)</td><td>0.03 <b>(+23.51%)</b></td><td>0.03 (+7.71%)</td><td>0.03 <b>(+96.73%)</b></td><td>0.00 <b>(-50.19%)</b></td><td>318.10 <b>(-49.17%)</b></td><td>270.96 <b>(-27.79%)</b></td><td>271.40 (-7.15%)</td><td>223.90 (-7.21%)</td><td>38.86 <b>(-76.29%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.80 (n/a)</td><td>375.26 (n/a)</td><td>292.30 (n/a)</td><td>241.30 (n/a)</td><td>163.85 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (-1.25%)</td><td>0.03 (+10.65%)</td><td>0.03 (+11.41%)</td><td>0.02 (+13.42%)</td><td>0.01 <b>(-27.58%)</b></td><td>504.30 (-11.82%)</td><td>317.16 (-15.58%)</td><td>277.70 (-10.25%)</td><td>234.50 (+1.25%)</td><td>107.52 <b>(-32.25%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.90 (n/a)</td><td>375.70 (n/a)</td><td>309.40 (n/a)</td><td>231.60 (n/a)</td><td>158.70 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (+4.59%)</td><td>0.02 (-1.06%)</td><td>0.02 (+11.69%)</td><td>0.01 <b>(-39.46%)</b></td><td>0.01 <b>(+50.79%)</b></td><td>1056.60 <b>(+65.17%)</b></td><td>490.64 <b>(+24.60%)</b></td><td>340.90 (-10.45%)</td><td>230.50 (-4.40%)</td><td>344.44 <b>(+127.93%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>639.70 (n/a)</td><td>393.78 (n/a)</td><td>380.70 (n/a)</td><td>241.10 (n/a)</td><td>151.12 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (-15.87%)</td><td>0.01 (-17.21%)</td><td>0.01 <b>(-24.08%)</b></td><td>0.00 (+9.61%)</td><td>0.01 (-11.89%)</td><td>1941.70 (-8.77%)</td><td>866.60 (+11.17%)</td><td>676.80 <b>(+31.72%)</b></td><td>292.10 (+18.84%)</td><td>652.64 (-14.43%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2128.30 (n/a)</td><td>779.52 (n/a)</td><td>513.80 (n/a)</td><td>245.80 (n/a)</td><td>762.67 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (-13.78%)</td><td>0.02 (-10.36%)</td><td>0.03 (-6.49%)</td><td>0.00 <b>(-30.15%)</b></td><td>0.01 (-5.33%)</td><td>1923.40 <b>(+43.16%)</b></td><td>671.70 <b>(+27.08%)</b></td><td>305.60 (+6.97%)</td><td>282.30 (+15.98%)</td><td>709.17 <b>(+51.94%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1343.50 (n/a)</td><td>528.56 (n/a)</td><td>285.70 (n/a)</td><td>243.40 (n/a)</td><td>466.73 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (+3.77%)</td><td>0.03 (+3.33%)</td><td>0.03 (+2.78%)</td><td>0.02 (+3.23%)</td><td>0.01 (-2.47%)</td><td>468.00 (-3.13%)</td><td>313.98 (-3.67%)</td><td>281.80 (-2.73%)</td><td>239.70 (-3.62%)</td><td>90.41 (-5.77%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>483.10 (n/a)</td><td>325.94 (n/a)</td><td>289.70 (n/a)</td><td>248.70 (n/a)</td><td>95.95 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (+10.26%)</td><td>0.02 (-11.10%)</td><td>0.02 (-7.11%)</td><td>0.00 <b>(-70.82%)</b></td><td>0.01 <b>(+50.08%)</b></td><td>1933.20 <b>(+242.71%)</b></td><td>680.50 <b>(+69.32%)</b></td><td>369.20 (+7.67%)</td><td>250.00 (-9.29%)</td><td>705.85 <b>(+419.04%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.10 (n/a)</td><td>401.90 (n/a)</td><td>342.90 (n/a)</td><td>275.60 (n/a)</td><td>135.99 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 <b>(+25.19%)</b></td><td>0.02 (+6.99%)</td><td>0.02 (+7.12%)</td><td>0.01 (+8.67%)</td><td>0.01 <b>(+44.65%)</b></td><td>574.90 (-7.99%)</td><td>489.78 (-3.76%)</td><td>527.20 (-6.64%)</td><td>257.40 <b>(-20.11%)</b></td><td>132.15 (+1.50%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>624.80 (n/a)</td><td>508.92 (n/a)</td><td>564.70 (n/a)</td><td>322.20 (n/a)</td><td>130.20 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (-6.14%)</td><td>0.02 (+9.30%)</td><td>0.03 <b>(+36.99%)</b></td><td>0.02 (+6.10%)</td><td>0.01 (-8.85%)</td><td>520.60 (-5.74%)</td><td>376.70 (-9.30%)</td><td>316.80 <b>(-27.00%)</b></td><td>286.90 (+6.58%)</td><td>103.16 (-7.15%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.30 (n/a)</td><td>415.34 (n/a)</td><td>434.00 (n/a)</td><td>269.20 (n/a)</td><td>111.11 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (-1.84%)</td><td>0.05 (+0.99%)</td><td>0.06 (+4.26%)</td><td>0.03 <b>(+22.54%)</b></td><td>0.02 (-8.03%)</td><td>590.00 (-18.40%)</td><td>346.18 (-5.81%)</td><td>269.00 (-4.07%)</td><td>248.40 (+1.89%)</td><td>143.05 <b>(-28.56%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>723.00 (n/a)</td><td>367.54 (n/a)</td><td>280.40 (n/a)</td><td>243.80 (n/a)</td><td>200.23 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 <b>(+24.15%)</b></td><td>0.06 <b>(+39.87%)</b></td><td>0.06 <b>(+79.07%)</b></td><td>0.03 (+12.47%)</td><td>0.02 (+15.36%)</td><td>509.10 (-11.09%)</td><td>309.84 <b>(-28.44%)</b></td><td>274.50 <b>(-44.15%)</b></td><td>234.10 (-19.44%)</td><td>114.22 (-11.24%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>572.60 (n/a)</td><td>432.96 (n/a)</td><td>491.50 (n/a)</td><td>290.60 (n/a)</td><td>128.68 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (-5.00%)</td><td>0.04 <b>(-30.09%)</b></td><td>0.04 <b>(-35.81%)</b></td><td>0.01 <b>(-86.02%)</b></td><td>0.02 <b>(+158.65%)</b></td><td>2502.60 <b>(+615.23%)</b></td><td>794.26 <b>(+174.55%)</b></td><td>457.70 <b>(+55.79%)</b></td><td>241.30 (+5.23%)</td><td>960.96 <b>(+2043.56%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>349.90 (n/a)</td><td>289.30 (n/a)</td><td>293.80 (n/a)</td><td>229.30 (n/a)</td><td>44.83 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (+9.17%)</td><td>0.06 (+19.75%)</td><td>0.06 (+9.18%)</td><td>0.03 <b>(+26.96%)</b></td><td>0.02 (-1.14%)</td><td>589.90 <b>(-21.23%)</b></td><td>324.22 (-19.91%)</td><td>272.70 (-8.40%)</td><td>219.90 (-8.41%)</td><td>152.08 <b>(-27.02%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>748.90 (n/a)</td><td>404.84 (n/a)</td><td>297.70 (n/a)</td><td>240.10 (n/a)</td><td>208.38 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (+10.82%)</td><td>0.05 (+11.94%)</td><td>0.05 <b>(+42.31%)</b></td><td>0.03 (+10.43%)</td><td>0.02 (+1.44%)</td><td>541.50 (-9.45%)</td><td>358.72 (-13.01%)</td><td>329.40 <b>(-29.74%)</b></td><td>187.00 (-9.79%)</td><td>136.53 (-16.71%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>598.00 (n/a)</td><td>412.38 (n/a)</td><td>468.80 (n/a)</td><td>207.30 (n/a)</td><td>163.92 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (-7.08%)</td><td>0.05 (-6.47%)</td><td>0.05 (-11.10%)</td><td>0.03 (+13.67%)</td><td>0.01 <b>(-23.22%)</b></td><td>483.40 (-12.03%)</td><td>332.10 (+2.78%)</td><td>308.80 (+12.50%)</td><td>259.70 (+7.63%)</td><td>89.07 <b>(-30.10%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>549.50 (n/a)</td><td>323.12 (n/a)</td><td>274.50 (n/a)</td><td>241.30 (n/a)</td><td>127.42 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 <b>(+22.05%)</b></td><td>0.04 (-10.92%)</td><td>0.03 (-16.53%)</td><td>0.01 <b>(-68.77%)</b></td><td>0.02 <b>(+62.92%)</b></td><td>1903.70 <b>(+220.22%)</b></td><td>709.02 <b>(+67.36%)</b></td><td>514.70 (+19.81%)</td><td>227.00 (-18.05%)</td><td>680.11 <b>(+386.36%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>594.50 (n/a)</td><td>423.64 (n/a)</td><td>429.60 (n/a)</td><td>277.00 (n/a)</td><td>139.84 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (-12.14%)</td><td>0.04 (+8.51%)</td><td>0.04 (+15.63%)</td><td>0.03 <b>(+118.46%)</b></td><td>0.01 <b>(-41.35%)</b></td><td>501.80 <b>(-54.23%)</b></td><td>398.84 <b>(-25.42%)</b></td><td>424.60 (-13.52%)</td><td>276.80 (+13.82%)</td><td>104.84 <b>(-69.09%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1096.30 (n/a)</td><td>534.80 (n/a)</td><td>491.00 (n/a)</td><td>243.20 (n/a)</td><td>339.14 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (+0.87%)</td><td>0.04 <b>(-31.32%)</b></td><td>0.03 <b>(-54.20%)</b></td><td>0.02 <b>(-32.87%)</b></td><td>0.03 <b>(+34.60%)</b></td><td>836.80 <b>(+48.98%)</b></td><td>583.92 <b>(+70.17%)</b></td><td>620.40 <b>(+118.30%)</b></td><td>205.90 (-0.87%)</td><td>269.37 <b>(+96.55%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>561.70 (n/a)</td><td>343.14 (n/a)</td><td>284.20 (n/a)</td><td>207.70 (n/a)</td><td>137.05 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (+1.13%)</td><td>0.06 <b>(+28.69%)</b></td><td>0.06 <b>(+58.09%)</b></td><td>0.03 (+7.46%)</td><td>0.02 (-3.17%)</td><td>502.50 (-6.94%)</td><td>306.62 <b>(-22.99%)</b></td><td>252.50 <b>(-36.75%)</b></td><td>236.30 (-1.09%)</td><td>111.89 (-9.14%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>540.00 (n/a)</td><td>398.14 (n/a)</td><td>399.20 (n/a)</td><td>238.90 (n/a)</td><td>123.14 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (-8.60%)</td><td>0.04 (+4.42%)</td><td>0.04 (+19.47%)</td><td>0.03 <b>(+26.52%)</b></td><td>0.01 <b>(-39.39%)</b></td><td>509.10 <b>(-20.96%)</b></td><td>398.52 (-9.60%)</td><td>377.30 (-16.30%)</td><td>309.70 (+9.40%)</td><td>78.38 <b>(-45.82%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>644.10 (n/a)</td><td>440.82 (n/a)</td><td>450.80 (n/a)</td><td>283.10 (n/a)</td><td>144.65 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (+2.79%)</td><td>0.04 (-2.77%)</td><td>0.04 (+10.45%)</td><td>0.03 (-3.68%)</td><td>0.01 (-9.48%)</td><td>643.90 (+3.82%)</td><td>460.80 (+0.14%)</td><td>462.00 (-9.47%)</td><td>261.10 (-2.72%)</td><td>137.60 (-13.78%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>620.20 (n/a)</td><td>460.16 (n/a)</td><td>510.30 (n/a)</td><td>268.40 (n/a)</td><td>159.59 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 <b>(-28.66%)</b></td><td>0.12 (-6.98%)</td><td>0.13 (+0.12%)</td><td>0.07 (+12.55%)</td><td>0.03 <b>(-42.65%)</b></td><td>451.40 (-11.16%)</td><td>294.20 (+0.27%)</td><td>261.40 (-0.11%)</td><td>235.70 <b>(+40.21%)</b></td><td>89.54 <b>(-29.79%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>508.10 (n/a)</td><td>293.42 (n/a)</td><td>261.70 (n/a)</td><td>168.10 (n/a)</td><td>127.53 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (+4.76%)</td><td>0.10 (-20.00%)</td><td>0.09 <b>(-27.83%)</b></td><td>0.06 (-18.93%)</td><td>0.04 <b>(+29.34%)</b></td><td>543.50 <b>(+23.35%)</b></td><td>385.72 <b>(+32.70%)</b></td><td>351.80 <b>(+38.56%)</b></td><td>216.40 (-4.54%)</td><td>143.57 <b>(+61.00%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>440.60 (n/a)</td><td>290.66 (n/a)</td><td>253.90 (n/a)</td><td>226.70 (n/a)</td><td>89.17 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (-8.68%)</td><td>0.10 (+0.07%)</td><td>0.08 (-1.91%)</td><td>0.07 <b>(+20.64%)</b></td><td>0.03 <b>(-24.75%)</b></td><td>459.80 (-17.11%)</td><td>363.28 (-5.88%)</td><td>390.10 (+1.93%)</td><td>238.50 (+9.50%)</td><td>101.45 <b>(-31.38%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>554.70 (n/a)</td><td>385.96 (n/a)</td><td>382.70 (n/a)</td><td>217.80 (n/a)</td><td>147.83 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.17 (+6.28%)</td><td>0.11 (+18.14%)</td><td>0.09 (+3.25%)</td><td>0.07 <b>(+29.99%)</b></td><td>0.05 (+4.50%)</td><td>495.20 <b>(-23.07%)</b></td><td>353.46 (-17.33%)</td><td>358.60 (-3.13%)</td><td>192.50 (-5.91%)</td><td>135.56 <b>(-22.45%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>643.70 (n/a)</td><td>427.54 (n/a)</td><td>370.20 (n/a)</td><td>204.60 (n/a)</td><td>174.80 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 <b>(-20.95%)</b></td><td>0.11 <b>(+38.87%)</b></td><td>0.12 <b>(+110.69%)</b></td><td>0.06 <b>(+21.27%)</b></td><td>0.03 <b>(-39.81%)</b></td><td>551.60 (-17.55%)</td><td>332.02 <b>(-36.28%)</b></td><td>276.80 <b>(-52.54%)</b></td><td>240.70 <b>(+26.48%)</b></td><td>129.40 <b>(-31.56%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>669.00 (n/a)</td><td>521.08 (n/a)</td><td>583.20 (n/a)</td><td>190.30 (n/a)</td><td>189.08 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 <b>(+39.88%)</b></td><td>0.09 (+12.64%)</td><td>0.09 (+19.96%)</td><td>0.02 <b>(-77.84%)</b></td><td>0.05 <b>(+363.46%)</b></td><td>1960.60 <b>(+351.23%)</b></td><td>642.28 <b>(+58.23%)</b></td><td>355.10 (-16.64%)</td><td>233.00 <b>(-28.53%)</b></td><td>740.68 <b>(+1533.68%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>434.50 (n/a)</td><td>405.92 (n/a)</td><td>426.00 (n/a)</td><td>326.00 (n/a)</td><td>45.34 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (+0.62%)</td><td>0.09 (-13.08%)</td><td>0.06 <b>(-43.85%)</b></td><td>0.06 (-7.28%)</td><td>0.04 (+18.22%)</td><td>592.20 (+7.85%)</td><td>440.74 <b>(+21.79%)</b></td><td>545.10 <b>(+78.08%)</b></td><td>224.60 (-0.62%)</td><td>180.20 <b>(+28.22%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>549.10 (n/a)</td><td>361.90 (n/a)</td><td>306.10 (n/a)</td><td>226.00 (n/a)</td><td>140.54 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (+18.40%)</td><td>0.09 (-1.55%)</td><td>0.07 <b>(-32.26%)</b></td><td>0.05 (+10.44%)</td><td>0.03 <b>(+28.39%)</b></td><td>603.80 (-9.45%)</td><td>423.76 (+3.63%)</td><td>484.10 <b>(+47.64%)</b></td><td>244.50 (-15.54%)</td><td>149.39 (-4.83%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>666.80 (n/a)</td><td>408.92 (n/a)</td><td>327.90 (n/a)</td><td>289.50 (n/a)</td><td>156.97 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 <b>(+36.55%)</b></td><td>0.11 <b>(+59.98%)</b></td><td>0.12 <b>(+87.27%)</b></td><td>0.07 <b>(+21.40%)</b></td><td>0.02 <b>(+61.13%)</b></td><td>459.50 (-17.64%)</td><td>307.92 <b>(-36.25%)</b></td><td>266.80 <b>(-46.60%)</b></td><td>249.40 <b>(-26.75%)</b></td><td>86.94 (+4.56%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>557.90 (n/a)</td><td>482.98 (n/a)</td><td>499.60 (n/a)</td><td>340.50 (n/a)</td><td>83.15 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 <b>(-56.62%)</b></td><td>0.07 <b>(-42.74%)</b></td><td>0.06 <b>(-43.10%)</b></td><td>0.06 (+0.61%)</td><td>0.01 <b>(-77.38%)</b></td><td>531.80 (-0.60%)</td><td>472.26 <b>(+52.43%)</b></td><td>508.20 <b>(+75.73%)</b></td><td>356.60 <b>(+130.51%)</b></td><td>71.72 <b>(-48.77%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>535.00 (n/a)</td><td>309.82 (n/a)</td><td>289.20 (n/a)</td><td>154.70 (n/a)</td><td>140.01 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 <b>(+42.69%)</b></td><td>0.09 <b>(+37.94%)</b></td><td>0.08 <b>(+40.49%)</b></td><td>0.05 <b>(+26.62%)</b></td><td>0.03 <b>(+39.65%)</b></td><td>670.70 <b>(-21.02%)</b></td><td>426.28 <b>(-26.99%)</b></td><td>389.00 <b>(-28.82%)</b></td><td>253.90 <b>(-29.92%)</b></td><td>170.56 <b>(-22.60%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>849.20 (n/a)</td><td>583.90 (n/a)</td><td>546.50 (n/a)</td><td>362.30 (n/a)</td><td>220.35 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (-0.37%)</td><td>0.09 (+14.43%)</td><td>0.08 <b>(+33.15%)</b></td><td>0.05 (-10.59%)</td><td>0.04 (+15.27%)</td><td>662.10 (+11.84%)</td><td>405.38 (-9.33%)</td><td>398.50 <b>(-24.90%)</b></td><td>239.50 (+0.38%)</td><td>178.33 (+17.86%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>592.00 (n/a)</td><td>447.10 (n/a)</td><td>530.60 (n/a)</td><td>238.60 (n/a)</td><td>151.31 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 <b>(-33.68%)</b></td><td>0.01 (-8.22%)</td><td>0.02 (+13.59%)</td><td>0.01 (+5.79%)</td><td>0.00 <b>(-35.16%)</b></td><td>546.20 (-5.47%)</td><td>369.98 (+2.98%)</td><td>269.50 (-11.96%)</td><td>249.90 <b>(+50.72%)</b></td><td>149.84 (-5.41%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.80 (n/a)</td><td>359.28 (n/a)</td><td>306.10 (n/a)</td><td>165.80 (n/a)</td><td>158.41 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 <b>(-33.50%)</b></td><td>0.02 <b>(-29.45%)</b></td><td>0.01 <b>(-35.22%)</b></td><td>0.01 (-4.69%)</td><td>0.01 <b>(-36.52%)</b></td><td>610.90 (+4.93%)</td><td>414.54 <b>(+33.64%)</b></td><td>420.20 <b>(+54.37%)</b></td><td>259.90 <b>(+50.41%)</b></td><td>142.15 (-9.78%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.20 (n/a)</td><td>310.18 (n/a)</td><td>272.20 (n/a)</td><td>172.80 (n/a)</td><td>157.57 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+13.22%)</td><td>0.01 <b>(+36.80%)</b></td><td>0.01 <b>(+71.61%)</b></td><td>0.01 <b>(+42.16%)</b></td><td>0.00 (+9.02%)</td><td>529.70 <b>(-29.65%)</b></td><td>364.76 <b>(-28.52%)</b></td><td>310.10 <b>(-41.72%)</b></td><td>249.30 (-11.69%)</td><td>125.26 <b>(-30.03%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>752.90 (n/a)</td><td>510.32 (n/a)</td><td>532.10 (n/a)</td><td>282.30 (n/a)</td><td>179.02 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 <b>(+46.67%)</b></td><td>0.01 (+16.72%)</td><td>0.01 (+7.17%)</td><td>0.00 (+2.36%)</td><td>0.01 <b>(+41.75%)</b></td><td>2439.90 (-2.30%)</td><td>845.56 (-6.04%)</td><td>484.30 (-6.69%)</td><td>286.20 <b>(-31.82%)</b></td><td>897.51 (+0.19%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2497.40 (n/a)</td><td>899.90 (n/a)</td><td>519.00 (n/a)</td><td>419.80 (n/a)</td><td>895.82 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+7.40%)</td><td>0.01 (+3.60%)</td><td>0.01 (+8.70%)</td><td>0.01 (-7.01%)</td><td>0.00 (+9.77%)</td><td>622.00 (+7.54%)</td><td>424.32 (-1.86%)</td><td>439.40 (-8.00%)</td><td>234.10 (-6.88%)</td><td>159.53 (+7.43%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.40 (n/a)</td><td>432.34 (n/a)</td><td>477.60 (n/a)</td><td>251.40 (n/a)</td><td>148.50 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (-19.62%)</td><td>0.02 <b>(+35.62%)</b></td><td>0.02 <b>(+114.39%)</b></td><td>0.01 <b>(+22.00%)</b></td><td>0.01 <b>(-28.33%)</b></td><td>591.00 (-18.03%)</td><td>332.98 <b>(-32.28%)</b></td><td>238.90 <b>(-53.35%)</b></td><td>228.90 <b>(+24.40%)</b></td><td>155.31 <b>(-21.09%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>721.00 (n/a)</td><td>491.68 (n/a)</td><td>512.10 (n/a)</td><td>184.00 (n/a)</td><td>196.81 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+5.76%)</td><td>0.01 (+8.44%)</td><td>0.01 (-9.53%)</td><td>0.01 <b>(+34.02%)</b></td><td>0.00 (-1.33%)</td><td>593.60 <b>(-25.38%)</b></td><td>462.68 (-10.56%)</td><td>518.00 (+10.52%)</td><td>270.40 (-5.45%)</td><td>131.12 <b>(-30.50%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>795.50 (n/a)</td><td>517.32 (n/a)</td><td>468.70 (n/a)</td><td>286.00 (n/a)</td><td>188.66 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+18.11%)</td><td>0.01 <b>(+29.36%)</b></td><td>0.01 (+6.63%)</td><td>0.01 <b>(+70.15%)</b></td><td>0.01 (+14.59%)</td><td>610.30 <b>(-41.23%)</b></td><td>423.32 <b>(-26.54%)</b></td><td>491.60 (-6.22%)</td><td>208.20 (-15.33%)</td><td>165.58 <b>(-42.38%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1038.50 (n/a)</td><td>576.22 (n/a)</td><td>524.20 (n/a)</td><td>245.90 (n/a)</td><td>287.35 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 <b>(+31.97%)</b></td><td>0.01 (+5.96%)</td><td>0.01 (-4.28%)</td><td>0.01 (-1.13%)</td><td>0.00 <b>(+94.50%)</b></td><td>614.20 (+1.15%)</td><td>515.72 (-1.62%)</td><td>555.40 (+4.46%)</td><td>301.00 <b>(-24.22%)</b></td><td>123.21 <b>(+38.99%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>607.20 (n/a)</td><td>524.22 (n/a)</td><td>531.70 (n/a)</td><td>397.20 (n/a)</td><td>88.65 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+3.40%)</td><td>0.01 (+4.62%)</td><td>0.02 <b>(+41.13%)</b></td><td>0.01 (-5.44%)</td><td>0.01 (+2.92%)</td><td>596.40 (+5.76%)</td><td>395.28 (-2.73%)</td><td>300.00 <b>(-29.13%)</b></td><td>204.70 (-3.31%)</td><td>179.78 (+10.57%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.90 (n/a)</td><td>406.36 (n/a)</td><td>423.30 (n/a)</td><td>211.70 (n/a)</td><td>162.59 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (+10.55%)</td><td>0.01 (-12.74%)</td><td>0.01 (-19.31%)</td><td>0.00 <b>(-69.84%)</b></td><td>0.01 <b>(+84.41%)</b></td><td>1887.50 <b>(+231.61%)</b></td><td>705.76 <b>(+75.34%)</b></td><td>455.20 <b>(+23.93%)</b></td><td>261.60 (-9.54%)</td><td>677.49 <b>(+465.49%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.20 (n/a)</td><td>402.50 (n/a)</td><td>367.30 (n/a)</td><td>289.20 (n/a)</td><td>119.81 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (-0.38%)</td><td>0.02 (-9.00%)</td><td>0.02 (+7.31%)</td><td>0.00 <b>(-75.70%)</b></td><td>0.01 <b>(+32.58%)</b></td><td>1996.00 <b>(+311.46%)</b></td><td>665.62 <b>(+76.58%)</b></td><td>415.40 (-6.82%)</td><td>231.60 (+0.39%)</td><td>749.23 <b>(+484.50%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>485.10 (n/a)</td><td>376.96 (n/a)</td><td>445.80 (n/a)</td><td>230.70 (n/a)</td><td>128.18 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (-15.09%)</td><td>0.04 (-2.93%)</td><td>0.04 <b>(+22.79%)</b></td><td>0.01 <b>(-71.29%)</b></td><td>0.02 (+10.30%)</td><td>1932.00 <b>(+248.30%)</b></td><td>611.60 <b>(+62.41%)</b></td><td>300.90 (-18.57%)</td><td>256.80 (+17.74%)</td><td>738.39 <b>(+391.15%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>554.70 (n/a)</td><td>376.58 (n/a)</td><td>369.50 (n/a)</td><td>218.10 (n/a)</td><td>150.34 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 <b>(-20.05%)</b></td><td>0.02 (-7.46%)</td><td>0.02 (+4.04%)</td><td>0.01 (-5.34%)</td><td>0.01 <b>(-33.45%)</b></td><td>610.50 (+5.64%)</td><td>477.24 (+2.52%)</td><td>516.80 (-3.89%)</td><td>276.50 <b>(+25.06%)</b></td><td>125.82 (-13.79%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.90 (n/a)</td><td>465.50 (n/a)</td><td>537.70 (n/a)</td><td>221.10 (n/a)</td><td>145.94 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (+3.29%)</td><td>0.03 (-18.65%)</td><td>0.02 <b>(-36.63%)</b></td><td>0.02 (-2.26%)</td><td>0.01 (-4.58%)</td><td>613.70 (+2.30%)</td><td>433.02 <b>(+20.76%)</b></td><td>452.20 <b>(+57.78%)</b></td><td>233.70 (-3.19%)</td><td>136.69 (-9.69%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>599.90 (n/a)</td><td>358.58 (n/a)</td><td>286.60 (n/a)</td><td>241.40 (n/a)</td><td>151.35 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (-10.89%)</td><td>0.02 <b>(+25.13%)</b></td><td>0.02 <b>(+54.53%)</b></td><td>0.02 <b>(+48.35%)</b></td><td>0.01 <b>(-33.91%)</b></td><td>443.60 <b>(-32.59%)</b></td><td>351.26 <b>(-26.65%)</b></td><td>350.40 <b>(-35.29%)</b></td><td>259.70 (+12.23%)</td><td>86.60 <b>(-47.97%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.10 (n/a)</td><td>478.86 (n/a)</td><td>541.50 (n/a)</td><td>231.40 (n/a)</td><td>166.46 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 <b>(+88.54%)</b></td><td>0.03 <b>(+66.63%)</b></td><td>0.02 (+17.16%)</td><td>0.02 <b>(+133.08%)</b></td><td>0.01 <b>(+72.75%)</b></td><td>467.20 <b>(-57.10%)</b></td><td>365.76 <b>(-42.34%)</b></td><td>414.00 (-14.66%)</td><td>211.10 <b>(-46.97%)</b></td><td>107.34 <b>(-61.67%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1089.10 (n/a)</td><td>634.30 (n/a)</td><td>485.10 (n/a)</td><td>398.10 (n/a)</td><td>280.03 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (-1.78%)</td><td>0.02 (+14.04%)</td><td>0.02 <b>(+33.79%)</b></td><td>0.01 <b>(+90.04%)</b></td><td>0.01 <b>(-33.10%)</b></td><td>564.40 <b>(-47.39%)</b></td><td>391.86 <b>(-28.60%)</b></td><td>418.70 <b>(-25.26%)</b></td><td>244.40 (+1.79%)</td><td>125.36 <b>(-62.52%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1072.70 (n/a)</td><td>548.84 (n/a)</td><td>560.20 (n/a)</td><td>240.10 (n/a)</td><td>334.43 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (+0.52%)</td><td>0.03 <b>(+28.57%)</b></td><td>0.03 <b>(+44.40%)</b></td><td>0.02 <b>(+49.06%)</b></td><td>0.01 <b>(-26.54%)</b></td><td>545.50 <b>(-32.92%)</b></td><td>336.16 <b>(-31.08%)</b></td><td>305.20 <b>(-30.75%)</b></td><td>242.00 (-0.53%)</td><td>122.37 <b>(-49.13%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>813.20 (n/a)</td><td>487.72 (n/a)</td><td>440.70 (n/a)</td><td>243.30 (n/a)</td><td>240.56 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 <b>(-48.69%)</b></td><td>0.02 <b>(-48.66%)</b></td><td>0.01 <b>(-42.11%)</b></td><td>0.00 <b>(-78.16%)</b></td><td>0.01 <b>(-38.57%)</b></td><td>2460.70 <b>(+357.80%)</b></td><td>877.32 <b>(+173.02%)</b></td><td>549.30 <b>(+72.74%)</b></td><td>302.10 <b>(+94.90%)</b></td><td>895.10 <b>(+526.52%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.50 (n/a)</td><td>321.34 (n/a)</td><td>318.00 (n/a)</td><td>155.00 (n/a)</td><td>142.87 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (-19.28%)</td><td>0.02 <b>(-20.90%)</b></td><td>0.02 <b>(-37.26%)</b></td><td>0.02 <b>(+29.78%)</b></td><td>0.01 <b>(-37.56%)</b></td><td>564.60 <b>(-22.95%)</b></td><td>456.84 (+12.62%)</td><td>488.80 <b>(+59.37%)</b></td><td>266.00 <b>(+23.89%)</b></td><td>116.57 <b>(-44.46%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>732.80 (n/a)</td><td>405.64 (n/a)</td><td>306.70 (n/a)</td><td>214.70 (n/a)</td><td>209.88 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (+4.09%)</td><td>0.02 (+1.33%)</td><td>0.02 (+9.88%)</td><td>0.01 (+7.57%)</td><td>0.01 (-0.61%)</td><td>594.70 (-7.03%)</td><td>461.50 (-3.41%)</td><td>488.80 (-8.98%)</td><td>232.60 (-3.92%)</td><td>139.59 (-17.18%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>639.70 (n/a)</td><td>477.78 (n/a)</td><td>537.00 (n/a)</td><td>242.10 (n/a)</td><td>168.54 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (+11.36%)</td><td>0.05 <b>(+20.89%)</b></td><td>0.06 <b>(+90.25%)</b></td><td>0.03 (+11.00%)</td><td>0.02 (+2.36%)</td><td>592.60 (-9.91%)</td><td>363.94 (-18.18%)</td><td>274.10 <b>(-47.44%)</b></td><td>233.70 (-10.22%)</td><td>159.18 (-10.06%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>657.80 (n/a)</td><td>444.80 (n/a)</td><td>521.50 (n/a)</td><td>260.30 (n/a)</td><td>176.99 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (-6.38%)</td><td>0.06 (-11.60%)</td><td>0.05 <b>(-24.46%)</b></td><td>0.04 (+6.42%)</td><td>0.02 (-16.55%)</td><td>562.30 (-6.03%)</td><td>457.96 (+10.51%)</td><td>512.90 <b>(+32.40%)</b></td><td>293.80 (+6.80%)</td><td>113.40 (-15.63%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>598.40 (n/a)</td><td>414.40 (n/a)</td><td>387.40 (n/a)</td><td>275.10 (n/a)</td><td>134.40 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 <b>(+53.03%)</b></td><td>0.05 <b>(+54.02%)</b></td><td>0.06 <b>(+79.78%)</b></td><td>0.03 <b>(+25.92%)</b></td><td>0.02 <b>(+96.05%)</b></td><td>525.00 <b>(-20.59%)</b></td><td>354.90 <b>(-29.19%)</b></td><td>294.40 <b>(-44.37%)</b></td><td>193.70 <b>(-34.65%)</b></td><td>156.52 (+17.26%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>661.10 (n/a)</td><td>501.22 (n/a)</td><td>529.20 (n/a)</td><td>296.40 (n/a)</td><td>133.48 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (-5.58%)</td><td>0.07 (+18.70%)</td><td>0.06 <b>(+33.88%)</b></td><td>0.04 <b>(+34.97%)</b></td><td>0.02 (-18.64%)</td><td>580.00 <b>(-25.91%)</b></td><td>352.70 <b>(-24.17%)</b></td><td>315.90 <b>(-25.30%)</b></td><td>226.90 (+5.93%)</td><td>146.41 <b>(-38.56%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>782.80 (n/a)</td><td>465.10 (n/a)</td><td>422.90 (n/a)</td><td>214.20 (n/a)</td><td>238.30 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 <b>(-27.14%)</b></td><td>0.06 (-0.13%)</td><td>0.06 (+15.98%)</td><td>0.03 (+13.75%)</td><td>0.01 <b>(-40.98%)</b></td><td>497.20 (-12.08%)</td><td>311.38 (-6.60%)</td><td>274.90 (-13.77%)</td><td>245.00 <b>(+37.25%)</b></td><td>104.92 <b>(-26.50%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>565.50 (n/a)</td><td>333.38 (n/a)</td><td>318.80 (n/a)</td><td>178.50 (n/a)</td><td>142.76 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (+7.64%)</td><td>0.06 (+18.79%)</td><td>0.05 <b>(+27.47%)</b></td><td>0.04 <b>(+201.30%)</b></td><td>0.02 <b>(-22.07%)</b></td><td>570.10 <b>(-66.81%)</b></td><td>402.68 <b>(-39.46%)</b></td><td>404.50 <b>(-21.56%)</b></td><td>240.60 (-7.10%)</td><td>140.39 <b>(-76.67%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1717.70 (n/a)</td><td>665.16 (n/a)</td><td>515.70 (n/a)</td><td>259.00 (n/a)</td><td>601.67 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 <b>(+25.31%)</b></td><td>0.05 <b>(+60.01%)</b></td><td>0.06 <b>(+67.39%)</b></td><td>0.03 <b>(+322.60%)</b></td><td>0.02 (+5.06%)</td><td>576.00 <b>(-76.34%)</b></td><td>363.72 <b>(-57.36%)</b></td><td>297.60 <b>(-40.25%)</b></td><td>233.30 <b>(-20.21%)</b></td><td>150.18 <b>(-83.13%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2434.10 (n/a)</td><td>853.10 (n/a)</td><td>498.10 (n/a)</td><td>292.40 (n/a)</td><td>890.11 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (-0.56%)</td><td>0.05 (+15.80%)</td><td>0.06 <b>(+63.38%)</b></td><td>0.01 <b>(-70.15%)</b></td><td>0.03 <b>(+53.91%)</b></td><td>1961.30 <b>(+235.04%)</b></td><td>635.00 <b>(+43.68%)</b></td><td>285.00 <b>(-38.80%)</b></td><td>242.00 (+0.54%)</td><td>745.07 <b>(+485.29%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>585.40 (n/a)</td><td>441.94 (n/a)</td><td>465.70 (n/a)</td><td>240.70 (n/a)</td><td>127.30 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (+6.15%)</td><td>0.04 (-7.71%)</td><td>0.03 <b>(-42.35%)</b></td><td>0.03 (-7.05%)</td><td>0.02 <b>(+20.87%)</b></td><td>594.30 (+7.59%)</td><td>429.96 (+12.95%)</td><td>524.80 <b>(+73.49%)</b></td><td>225.40 (-5.81%)</td><td>167.55 (+15.67%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>552.40 (n/a)</td><td>380.68 (n/a)</td><td>302.50 (n/a)</td><td>239.30 (n/a)</td><td>144.85 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 <b>(+41.70%)</b></td><td>0.05 <b>(+20.87%)</b></td><td>0.05 (+13.73%)</td><td>0.02 (-19.24%)</td><td>0.02 <b>(+90.10%)</b></td><td>815.90 <b>(+23.81%)</b></td><td>464.10 (-9.31%)</td><td>370.50 (-12.06%)</td><td>290.90 <b>(-29.43%)</b></td><td>215.69 <b>(+66.87%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>659.00 (n/a)</td><td>511.72 (n/a)</td><td>421.30 (n/a)</td><td>412.20 (n/a)</td><td>129.26 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 <b>(+20.04%)</b></td><td>0.04 (+5.10%)</td><td>0.03 (+0.28%)</td><td>0.03 (-10.54%)</td><td>0.02 <b>(+41.36%)</b></td><td>610.20 (+11.80%)</td><td>441.24 (-0.67%)</td><td>484.10 (-0.29%)</td><td>251.40 (-16.67%)</td><td>144.77 <b>(+26.83%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>545.80 (n/a)</td><td>444.22 (n/a)</td><td>485.50 (n/a)</td><td>301.70 (n/a)</td><td>114.14 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (+11.60%)</td><td>0.10 (-0.61%)</td><td>0.11 (+3.90%)</td><td>0.05 (-11.24%)</td><td>0.03 <b>(+31.01%)</b></td><td>677.10 (+12.66%)</td><td>387.54 (+5.21%)</td><td>306.90 (-3.76%)</td><td>257.30 (-10.38%)</td><td>170.17 <b>(+30.15%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>601.00 (n/a)</td><td>368.34 (n/a)</td><td>318.90 (n/a)</td><td>287.10 (n/a)</td><td>130.75 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 (-15.14%)</td><td>0.09 <b>(+31.85%)</b></td><td>0.08 <b>(+27.66%)</b></td><td>0.06 <b>(+270.40%)</b></td><td>0.03 <b>(-41.39%)</b></td><td>517.40 <b>(-73.00%)</b></td><td>378.72 <b>(-48.92%)</b></td><td>415.70 <b>(-21.65%)</b></td><td>267.30 (+17.86%)</td><td>107.41 <b>(-83.97%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1916.40 (n/a)</td><td>741.38 (n/a)</td><td>530.60 (n/a)</td><td>226.80 (n/a)</td><td>669.89 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.19 (+16.01%)</td><td>0.11 (-3.03%)</td><td>0.09 <b>(-31.02%)</b></td><td>0.07 <b>(+43.98%)</b></td><td>0.04 (-4.93%)</td><td>556.40 <b>(-30.55%)</b></td><td>415.90 (-5.80%)</td><td>438.60 <b>(+44.99%)</b></td><td>218.90 (-13.82%)</td><td>122.73 <b>(-47.48%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>801.10 (n/a)</td><td>441.52 (n/a)</td><td>302.50 (n/a)</td><td>254.00 (n/a)</td><td>233.69 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 <b>(+35.98%)</b></td><td>0.10 <b>(+45.82%)</b></td><td>0.11 <b>(+60.74%)</b></td><td>0.08 <b>(+41.51%)</b></td><td>0.02 <b>(+47.79%)</b></td><td>431.30 <b>(-29.34%)</b></td><td>331.38 <b>(-30.90%)</b></td><td>285.50 <b>(-37.77%)</b></td><td>248.90 <b>(-26.47%)</b></td><td>81.80 (-19.86%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>610.40 (n/a)</td><td>479.54 (n/a)</td><td>458.80 (n/a)</td><td>338.50 (n/a)</td><td>102.07 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.19 (+18.15%)</td><td>0.12 (+15.20%)</td><td>0.12 (+13.90%)</td><td>0.06 (-1.78%)</td><td>0.05 <b>(+27.17%)</b></td><td>679.90 (+1.80%)</td><td>399.62 (-9.69%)</td><td>345.90 (-12.21%)</td><td>221.10 (-15.35%)</td><td>189.41 (+6.75%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>667.90 (n/a)</td><td>442.52 (n/a)</td><td>394.00 (n/a)</td><td>261.20 (n/a)</td><td>177.44 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (-5.93%)</td><td>0.08 (-6.87%)</td><td>0.07 (-8.58%)</td><td>0.05 (-17.93%)</td><td>0.03 (+1.33%)</td><td>693.40 <b>(+21.84%)</b></td><td>470.22 (+10.66%)</td><td>459.80 (+9.40%)</td><td>247.20 (+6.32%)</td><td>179.66 <b>(+30.19%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>569.10 (n/a)</td><td>424.92 (n/a)</td><td>420.30 (n/a)</td><td>232.50 (n/a)</td><td>138.00 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.18 <b>(+51.80%)</b></td><td>0.09 <b>(+24.29%)</b></td><td>0.07 (+7.70%)</td><td>0.06 (+4.00%)</td><td>0.05 <b>(+99.18%)</b></td><td>576.50 (-3.85%)</td><td>453.68 (-12.62%)</td><td>509.80 (-7.14%)</td><td>202.30 <b>(-34.13%)</b></td><td>148.04 <b>(+22.02%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>599.60 (n/a)</td><td>519.20 (n/a)</td><td>549.00 (n/a)</td><td>307.10 (n/a)</td><td>121.32 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (+2.96%)</td><td>0.09 (-5.70%)</td><td>0.07 <b>(-41.37%)</b></td><td>0.05 (+4.19%)</td><td>0.04 (+1.68%)</td><td>596.00 (-4.03%)</td><td>402.72 (+4.30%)</td><td>467.10 <b>(+70.60%)</b></td><td>228.20 (-2.85%)</td><td>158.28 (-11.92%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>621.00 (n/a)</td><td>386.12 (n/a)</td><td>273.80 (n/a)</td><td>234.90 (n/a)</td><td>179.71 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 <b>(-51.96%)</b></td><td>0.07 <b>(-23.02%)</b></td><td>0.08 (-4.76%)</td><td>0.06 (-2.10%)</td><td>0.01 <b>(-75.96%)</b></td><td>628.70 (+2.14%)</td><td>507.76 (+15.57%)</td><td>470.60 (+5.00%)</td><td>427.80 <b>(+108.18%)</b></td><td>83.66 <b>(-43.93%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>615.50 (n/a)</td><td>439.36 (n/a)</td><td>448.20 (n/a)</td><td>205.50 (n/a)</td><td>149.19 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.11 (-9.68%)</td><td>0.08 (-3.32%)</td><td>0.07 (-8.70%)</td><td>0.05 (-16.05%)</td><td>0.02 (+3.62%)</td><td>599.20 (+19.13%)</td><td>439.30 (+5.49%)</td><td>468.80 (+9.53%)</td><td>299.20 (+10.73%)</td><td>122.90 <b>(+39.32%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>503.00 (n/a)</td><td>416.44 (n/a)</td><td>428.00 (n/a)</td><td>270.20 (n/a)</td><td>88.22 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (+7.20%)</td><td>0.06 (-19.95%)</td><td>0.04 <b>(-37.75%)</b></td><td>0.04 <b>(-41.33%)</b></td><td>0.02 <b>(+218.89%)</b></td><td>555.20 <b>(+70.46%)</b></td><td>403.46 <b>(+38.78%)</b></td><td>463.90 <b>(+60.69%)</b></td><td>237.50 (-6.72%)</td><td>139.60 <b>(+395.25%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>325.70 (n/a)</td><td>290.72 (n/a)</td><td>288.70 (n/a)</td><td>254.60 (n/a)</td><td>28.19 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 <b>(-32.47%)</b></td><td>0.04 <b>(-27.99%)</b></td><td>0.04 <b>(-27.87%)</b></td><td>0.03 (-19.60%)</td><td>0.01 <b>(-48.69%)</b></td><td>615.50 <b>(+24.37%)</b></td><td>504.56 <b>(+33.33%)</b></td><td>545.30 <b>(+38.65%)</b></td><td>374.80 <b>(+48.08%)</b></td><td>108.02 (-6.00%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>494.90 (n/a)</td><td>378.44 (n/a)</td><td>393.30 (n/a)</td><td>253.10 (n/a)</td><td>114.91 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (+5.04%)</td><td>0.06 (-3.78%)</td><td>0.06 (-15.57%)</td><td>0.04 (-3.01%)</td><td>0.02 <b>(+20.44%)</b></td><td>469.50 (+3.12%)</td><td>362.76 (+5.83%)</td><td>348.80 (+18.44%)</td><td>258.90 (-4.82%)</td><td>98.37 <b>(+20.73%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>455.30 (n/a)</td><td>342.78 (n/a)</td><td>294.50 (n/a)</td><td>272.00 (n/a)</td><td>81.48 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (+2.30%)</td><td>0.06 (+3.04%)</td><td>0.07 <b>(+59.62%)</b></td><td>0.01 <b>(-70.40%)</b></td><td>0.03 <b>(+58.26%)</b></td><td>2051.80 <b>(+237.86%)</b></td><td>679.02 <b>(+64.32%)</b></td><td>279.20 <b>(-37.36%)</b></td><td>237.30 (-2.27%)</td><td>778.69 <b>(+442.14%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>607.30 (n/a)</td><td>413.24 (n/a)</td><td>445.70 (n/a)</td><td>242.80 (n/a)</td><td>143.63 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (+1.54%)</td><td>0.07 <b>(+38.94%)</b></td><td>0.07 <b>(+75.16%)</b></td><td>0.04 <b>(+45.66%)</b></td><td>0.02 (-12.58%)</td><td>459.40 <b>(-31.34%)</b></td><td>329.38 <b>(-31.22%)</b></td><td>293.30 <b>(-42.90%)</b></td><td>248.50 (-1.51%)</td><td>93.64 <b>(-38.34%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>669.10 (n/a)</td><td>478.88 (n/a)</td><td>513.70 (n/a)</td><td>252.30 (n/a)</td><td>151.85 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 <b>(+32.19%)</b></td><td>0.06 (+18.88%)</td><td>0.07 <b>(+52.21%)</b></td><td>0.04 (-11.06%)</td><td>0.02 <b>(+95.25%)</b></td><td>564.70 (+12.42%)</td><td>381.44 (-7.79%)</td><td>282.10 <b>(-34.29%)</b></td><td>239.60 <b>(-24.34%)</b></td><td>159.45 <b>(+77.34%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>502.30 (n/a)</td><td>413.68 (n/a)</td><td>429.30 (n/a)</td><td>316.70 (n/a)</td><td>89.91 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 (+19.04%)</td><td>0.08 (+4.64%)</td><td>0.07 (-14.71%)</td><td>0.05 (+9.42%)</td><td>0.03 (+9.46%)</td><td>532.20 (-8.60%)</td><td>351.32 (-5.47%)</td><td>352.30 (+17.28%)</td><td>212.30 (-16.02%)</td><td>116.83 (-16.16%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>582.30 (n/a)</td><td>371.64 (n/a)</td><td>300.40 (n/a)</td><td>252.80 (n/a)</td><td>139.36 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (+6.76%)</td><td>0.07 (-7.38%)</td><td>0.09 (+9.21%)</td><td>0.01 <b>(-77.28%)</b></td><td>0.04 <b>(+103.21%)</b></td><td>2004.80 <b>(+340.04%)</b></td><td>660.98 <b>(+87.41%)</b></td><td>276.80 (-8.44%)</td><td>250.50 (-6.36%)</td><td>758.76 <b>(+707.07%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>455.60 (n/a)</td><td>352.70 (n/a)</td><td>302.30 (n/a)</td><td>267.50 (n/a)</td><td>94.01 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.11 <b>(+36.37%)</b></td><td>0.07 (+4.83%)</td><td>0.06 <b>(-21.95%)</b></td><td>0.03 (-19.11%)</td><td>0.04 <b>(+83.86%)</b></td><td>802.70 <b>(+23.63%)</b></td><td>461.06 (+10.66%)</td><td>442.60 <b>(+28.10%)</b></td><td>218.30 <b>(-26.67%)</b></td><td>243.13 <b>(+62.14%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>649.30 (n/a)</td><td>416.66 (n/a)</td><td>345.50 (n/a)</td><td>297.70 (n/a)</td><td>149.95 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (-13.27%)</td><td>0.06 (+10.24%)</td><td>0.05 (-5.61%)</td><td>0.04 <b>(+24.38%)</b></td><td>0.02 (-19.10%)</td><td>604.20 (-19.61%)</td><td>445.76 (-13.22%)</td><td>501.50 (+5.94%)</td><td>309.40 (+15.32%)</td><td>130.36 <b>(-27.67%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>751.60 (n/a)</td><td>513.64 (n/a)</td><td>473.40 (n/a)</td><td>268.30 (n/a)</td><td>180.24 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 <b>(+50.07%)</b></td><td>0.07 (+13.95%)</td><td>0.05 (+14.04%)</td><td>0.05 (+11.99%)</td><td>0.04 <b>(+46.16%)</b></td><td>535.90 (-10.71%)</td><td>404.56 (-9.13%)</td><td>466.70 (-12.32%)</td><td>173.10 <b>(-33.37%)</b></td><td>151.95 (-10.12%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>600.20 (n/a)</td><td>445.20 (n/a)</td><td>532.30 (n/a)</td><td>259.80 (n/a)</td><td>169.05 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 <b>(-28.58%)</b></td><td>0.05 (-14.37%)</td><td>0.05 (-0.57%)</td><td>0.01 <b>(-70.06%)</b></td><td>0.03 (-0.00%)</td><td>1924.00 <b>(+234.03%)</b></td><td>704.20 <b>(+62.83%)</b></td><td>470.10 (+0.58%)</td><td>315.90 <b>(+40.03%)</b></td><td>686.58 <b>(+434.11%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>576.00 (n/a)</td><td>432.48 (n/a)</td><td>467.40 (n/a)</td><td>225.60 (n/a)</td><td>128.55 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 <b>(+22.48%)</b></td><td>0.06 <b>(+54.10%)</b></td><td>0.07 <b>(+89.31%)</b></td><td>0.03 (-10.66%)</td><td>0.02 <b>(+46.14%)</b></td><td>622.20 (+11.95%)</td><td>333.88 <b>(-30.83%)</b></td><td>272.10 <b>(-47.19%)</b></td><td>237.40 (-18.36%)</td><td>161.84 <b>(+47.73%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>555.80 (n/a)</td><td>482.68 (n/a)</td><td>515.20 (n/a)</td><td>290.80 (n/a)</td><td>109.55 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 <b>(+41.41%)</b></td><td>0.06 <b>(+54.03%)</b></td><td>0.07 <b>(+84.55%)</b></td><td>0.04 <b>(+30.50%)</b></td><td>0.02 <b>(+80.74%)</b></td><td>488.60 <b>(-23.38%)</b></td><td>329.88 <b>(-30.96%)</b></td><td>247.10 <b>(-45.81%)</b></td><td>208.00 <b>(-29.28%)</b></td><td>136.20 (+6.55%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>637.70 (n/a)</td><td>477.84 (n/a)</td><td>456.00 (n/a)</td><td>294.10 (n/a)</td><td>127.82 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 <b>(+71.16%)</b></td><td>0.06 <b>(+67.26%)</b></td><td>0.07 <b>(+117.03%)</b></td><td>0.04 <b>(+26.10%)</b></td><td>0.02 <b>(+139.98%)</b></td><td>509.20 <b>(-20.70%)</b></td><td>338.72 <b>(-36.65%)</b></td><td>267.90 <b>(-53.92%)</b></td><td>239.10 <b>(-41.58%)</b></td><td>122.46 (+11.37%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>642.10 (n/a)</td><td>534.68 (n/a)</td><td>581.40 (n/a)</td><td>409.30 (n/a)</td><td>109.96 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (-11.45%)</td><td>0.05 (-10.35%)</td><td>0.05 (-1.16%)</td><td>0.01 <b>(-70.96%)</b></td><td>0.02 <b>(+23.62%)</b></td><td>2083.90 <b>(+244.39%)</b></td><td>693.18 <b>(+73.89%)</b></td><td>408.80 (+1.19%)</td><td>266.90 (+12.95%)</td><td>781.00 <b>(+425.63%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>605.10 (n/a)</td><td>398.62 (n/a)</td><td>404.00 (n/a)</td><td>236.30 (n/a)</td><td>148.58 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (+3.29%)</td><td>0.06 (+16.00%)</td><td>0.05 (-6.28%)</td><td>0.04 <b>(+34.47%)</b></td><td>0.03 (+7.31%)</td><td>476.50 <b>(-25.63%)</b></td><td>344.08 (-16.44%)</td><td>380.50 (+6.70%)</td><td>204.60 (-3.17%)</td><td>129.26 <b>(-28.46%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>640.70 (n/a)</td><td>411.76 (n/a)</td><td>356.60 (n/a)</td><td>211.30 (n/a)</td><td>180.68 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 <b>(-39.24%)</b></td><td>0.04 <b>(-21.63%)</b></td><td>0.04 <b>(-20.61%)</b></td><td>0.03 (+0.42%)</td><td>0.01 <b>(-53.91%)</b></td><td>563.40 (-0.41%)</td><td>444.36 (+17.57%)</td><td>469.80 <b>(+25.95%)</b></td><td>309.20 <b>(+64.56%)</b></td><td>110.29 <b>(-21.55%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>565.70 (n/a)</td><td>377.94 (n/a)</td><td>373.00 (n/a)</td><td>187.90 (n/a)</td><td>140.58 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.40 (+0.99%)</td><td>0.33 (+13.87%)</td><td>0.35 (+5.12%)</td><td>0.19 <b>(+24.22%)</b></td><td>0.08 (-19.93%)</td><td>514.10 (-19.50%)</td><td>322.48 (-17.04%)</td><td>279.40 (-4.87%)</td><td>244.10 (-0.97%)</td><td>109.90 <b>(-33.72%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.33 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>638.60 (n/a)</td><td>388.74 (n/a)</td><td>293.70 (n/a)</td><td>246.50 (n/a)</td><td>165.80 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.47 <b>(+44.42%)</b></td><td>0.28 <b>(+45.20%)</b></td><td>0.22 <b>(+26.98%)</b></td><td>0.18 <b>(+133.43%)</b></td><td>0.12 <b>(+29.85%)</b></td><td>535.00 <b>(-57.16%)</b></td><td>401.34 <b>(-37.55%)</b></td><td>456.30 <b>(-21.26%)</b></td><td>208.10 <b>(-30.75%)</b></td><td>137.61 <b>(-62.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.33 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>1248.80 (n/a)</td><td>642.62 (n/a)</td><td>579.50 (n/a)</td><td>300.50 (n/a)</td><td>365.50 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.26 <b>(-34.45%)</b></td><td>0.19 <b>(-29.31%)</b></td><td>0.18 <b>(-20.34%)</b></td><td>0.10 <b>(-40.85%)</b></td><td>0.06 <b>(-44.74%)</b></td><td>1026.20 <b>(+69.06%)</b></td><td>588.28 <b>(+37.93%)</b></td><td>535.30 <b>(+25.54%)</b></td><td>383.10 <b>(+52.57%)</b></td><td>256.13 <b>(+50.32%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>607.00 (n/a)</td><td>426.52 (n/a)</td><td>426.40 (n/a)</td><td>251.10 (n/a)</td><td>170.39 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.33 (+3.02%)</td><td>0.25 <b>(+37.30%)</b></td><td>0.26 <b>(+85.43%)</b></td><td>0.14 <b>(+23.92%)</b></td><td>0.07 (-17.69%)</td><td>529.60 (-19.31%)</td><td>326.24 <b>(-30.89%)</b></td><td>288.30 <b>(-46.07%)</b></td><td>221.40 (-2.89%)</td><td>118.59 <b>(-27.84%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.32 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>656.30 (n/a)</td><td>472.08 (n/a)</td><td>534.60 (n/a)</td><td>228.00 (n/a)</td><td>164.35 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.27 (-9.45%)</td><td>0.19 (+3.17%)</td><td>0.17 (+9.63%)</td><td>0.13 (+0.48%)</td><td>0.06 (-18.89%)</td><td>557.40 (-0.48%)</td><td>416.70 (-5.43%)</td><td>435.40 (-8.78%)</td><td>269.20 (+10.42%)</td><td>115.24 (-11.03%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>560.10 (n/a)</td><td>440.64 (n/a)</td><td>477.30 (n/a)</td><td>243.80 (n/a)</td><td>129.53 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.30 <b>(-36.65%)</b></td><td>0.18 <b>(-26.16%)</b></td><td>0.21 (+2.40%)</td><td>0.03 <b>(-77.65%)</b></td><td>0.11 <b>(-20.49%)</b></td><td>2426.70 <b>(+347.40%)</b></td><td>796.88 <b>(+118.66%)</b></td><td>348.50 (-2.35%)</td><td>243.30 <b>(+57.88%)</b></td><td>925.51 <b>(+525.82%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.48 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>542.40 (n/a)</td><td>364.44 (n/a)</td><td>356.90 (n/a)</td><td>154.10 (n/a)</td><td>147.89 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (+12.66%)</td><td>0.10 (-3.75%)</td><td>0.09 (-16.96%)</td><td>0.07 (-13.45%)</td><td>0.03 <b>(+68.93%)</b></td><td>492.90 (+15.54%)</td><td>380.98 (+8.94%)</td><td>397.20 <b>(+20.44%)</b></td><td>255.50 (-11.22%)</td><td>110.00 <b>(+73.29%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>426.60 (n/a)</td><td>349.72 (n/a)</td><td>329.80 (n/a)</td><td>287.80 (n/a)</td><td>63.47 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.16 (+0.74%)</td><td>0.10 (-19.58%)</td><td>0.07 <b>(-41.47%)</b></td><td>0.06 (-12.16%)</td><td>0.05 <b>(+30.71%)</b></td><td>620.80 (+13.85%)</td><td>447.20 <b>(+34.52%)</b></td><td>532.40 <b>(+70.81%)</b></td><td>229.30 (-0.69%)</td><td>182.68 <b>(+45.27%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>545.30 (n/a)</td><td>332.44 (n/a)</td><td>311.70 (n/a)</td><td>230.90 (n/a)</td><td>125.75 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (+10.01%)</td><td>0.09 (+14.76%)</td><td>0.08 (+3.55%)</td><td>0.02 <b>(-68.11%)</b></td><td>0.06 <b>(+60.64%)</b></td><td>2396.10 <b>(+213.63%)</b></td><td>765.48 <b>(+50.20%)</b></td><td>444.30 (-3.41%)</td><td>240.40 (-9.08%)</td><td>918.22 <b>(+390.40%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>764.00 (n/a)</td><td>509.64 (n/a)</td><td>460.00 (n/a)</td><td>264.40 (n/a)</td><td>187.24 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.22 <b>(+48.76%)</b></td><td>0.13 <b>(+47.32%)</b></td><td>0.13 <b>(+65.06%)</b></td><td>0.06 <b>(+86.31%)</b></td><td>0.06 <b>(+56.29%)</b></td><td>582.20 <b>(-46.32%)</b></td><td>360.10 <b>(-32.72%)</b></td><td>273.50 <b>(-39.41%)</b></td><td>166.20 <b>(-32.77%)</b></td><td>181.39 <b>(-43.30%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1084.60 (n/a)</td><td>535.22 (n/a)</td><td>451.40 (n/a)</td><td>247.20 (n/a)</td><td>319.90 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (+0.45%)</td><td>0.09 (-17.70%)</td><td>0.08 (-18.70%)</td><td>0.06 (-16.30%)</td><td>0.04 (+5.34%)</td><td>624.10 (+19.47%)</td><td>457.90 <b>(+24.92%)</b></td><td>437.60 <b>(+22.99%)</b></td><td>245.60 (-0.45%)</td><td>155.25 <b>(+30.89%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>522.40 (n/a)</td><td>366.54 (n/a)</td><td>355.80 (n/a)</td><td>246.70 (n/a)</td><td>118.61 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (-17.18%)</td><td>0.10 <b>(-20.64%)</b></td><td>0.07 <b>(-34.62%)</b></td><td>0.06 (-19.18%)</td><td>0.04 (-14.83%)</td><td>599.70 <b>(+23.73%)</b></td><td>433.46 <b>(+26.65%)</b></td><td>496.50 <b>(+52.96%)</b></td><td>245.70 <b>(+20.74%)</b></td><td>153.78 <b>(+21.99%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>484.70 (n/a)</td><td>342.26 (n/a)</td><td>324.60 (n/a)</td><td>203.50 (n/a)</td><td>126.06 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.16 (-12.80%)</td><td>0.11 (-9.96%)</td><td>0.08 (-11.06%)</td><td>0.07 (+0.50%)</td><td>0.04 (-16.73%)</td><td>569.70 (-0.51%)</td><td>426.30 (+8.80%)</td><td>488.30 (+12.43%)</td><td>251.60 (+14.68%)</td><td>139.20 (-2.77%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>572.60 (n/a)</td><td>391.82 (n/a)</td><td>434.30 (n/a)</td><td>219.40 (n/a)</td><td>143.17 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (+13.43%)</td><td>0.10 (+5.47%)</td><td>0.09 (+2.72%)</td><td>0.07 (-5.64%)</td><td>0.03 <b>(+47.48%)</b></td><td>569.90 (+5.97%)</td><td>451.36 (-2.38%)</td><td>463.80 (-2.64%)</td><td>293.30 (-11.84%)</td><td>111.82 <b>(+42.34%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>537.80 (n/a)</td><td>462.38 (n/a)</td><td>476.40 (n/a)</td><td>332.70 (n/a)</td><td>78.55 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.19 (-2.91%)</td><td>0.10 <b>(-20.55%)</b></td><td>0.08 (-12.29%)</td><td>0.07 (-3.50%)</td><td>0.05 (-13.34%)</td><td>613.70 (+3.63%)</td><td>487.46 <b>(+21.94%)</b></td><td>536.50 (+14.00%)</td><td>220.30 (+2.99%)</td><td>156.79 (-7.03%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>592.20 (n/a)</td><td>399.74 (n/a)</td><td>470.60 (n/a)</td><td>213.90 (n/a)</td><td>168.65 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.16 (-3.14%)</td><td>0.11 (-6.42%)</td><td>0.10 (-18.78%)</td><td>0.06 (+1.22%)</td><td>0.04 (-11.66%)</td><td>630.70 (-1.21%)</td><td>414.86 (+3.88%)</td><td>409.50 <b>(+23.12%)</b></td><td>251.20 (+3.25%)</td><td>148.93 (-11.29%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>638.40 (n/a)</td><td>399.36 (n/a)</td><td>332.60 (n/a)</td><td>243.30 (n/a)</td><td>167.88 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.16 (+1.72%)</td><td>0.09 <b>(-20.05%)</b></td><td>0.08 <b>(-22.29%)</b></td><td>0.05 <b>(-37.20%)</b></td><td>0.04 <b>(+40.24%)</b></td><td>749.20 <b>(+59.23%)</b></td><td>506.36 <b>(+35.85%)</b></td><td>486.10 <b>(+28.70%)</b></td><td>258.60 (-1.71%)</td><td>186.75 <b>(+112.56%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>470.50 (n/a)</td><td>372.74 (n/a)</td><td>377.70 (n/a)</td><td>263.10 (n/a)</td><td>87.86 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.17 (+10.76%)</td><td>0.09 <b>(-25.24%)</b></td><td>0.08 <b>(-30.99%)</b></td><td>0.02 <b>(-76.67%)</b></td><td>0.05 <b>(+104.51%)</b></td><td>1987.60 <b>(+328.64%)</b></td><td>754.14 <b>(+105.62%)</b></td><td>489.70 <b>(+44.92%)</b></td><td>238.70 (-9.72%)</td><td>702.43 <b>(+754.99%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>463.70 (n/a)</td><td>366.76 (n/a)</td><td>337.90 (n/a)</td><td>264.40 (n/a)</td><td>82.16 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 (+9.89%)</td><td>0.09 (+1.97%)</td><td>0.07 (-19.73%)</td><td>0.06 (-5.37%)</td><td>0.03 <b>(+77.60%)</b></td><td>577.80 (+5.69%)</td><td>446.20 (+5.63%)</td><td>535.20 <b>(+24.58%)</b></td><td>278.60 (-8.98%)</td><td>153.15 <b>(+67.50%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>546.70 (n/a)</td><td>422.42 (n/a)</td><td>429.60 (n/a)</td><td>306.10 (n/a)</td><td>91.43 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 <b>(+93.80%)</b></td><td>0.09 <b>(+73.22%)</b></td><td>0.07 <b>(+34.97%)</b></td><td>0.05 <b>(+87.46%)</b></td><td>0.04 <b>(+112.08%)</b></td><td>729.80 <b>(-46.66%)</b></td><td>475.30 <b>(-40.67%)</b></td><td>467.30 <b>(-25.91%)</b></td><td>243.70 <b>(-48.41%)</b></td><td>204.92 <b>(-43.13%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1368.10 (n/a)</td><td>801.08 (n/a)</td><td>630.70 (n/a)</td><td>472.40 (n/a)</td><td>360.31 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.17 <b>(+45.18%)</b></td><td>0.11 <b>(+38.35%)</b></td><td>0.09 <b>(+43.65%)</b></td><td>0.06 (+1.53%)</td><td>0.05 <b>(+85.87%)</b></td><td>576.60 (-1.50%)</td><td>374.86 <b>(-21.95%)</b></td><td>381.20 <b>(-30.39%)</b></td><td>203.60 <b>(-31.12%)</b></td><td>152.30 <b>(+22.02%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>585.40 (n/a)</td><td>480.28 (n/a)</td><td>547.60 (n/a)</td><td>295.60 (n/a)</td><td>124.81 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (+19.62%)</td><td>0.10 (+1.34%)</td><td>0.09 <b>(-23.86%)</b></td><td>0.06 (-7.34%)</td><td>0.04 <b>(+47.91%)</b></td><td>557.30 (+7.92%)</td><td>394.38 (+4.53%)</td><td>406.00 <b>(+31.35%)</b></td><td>228.40 (-16.40%)</td><td>147.64 <b>(+29.57%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>516.40 (n/a)</td><td>377.28 (n/a)</td><td>309.10 (n/a)</td><td>273.20 (n/a)</td><td>113.94 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (-2.49%)</td><td>0.09 (-4.89%)</td><td>0.08 (-13.86%)</td><td>0.06 (-9.21%)</td><td>0.03 (-0.63%)</td><td>547.90 (+10.15%)</td><td>398.64 (+5.56%)</td><td>427.30 (+16.08%)</td><td>267.90 (+2.53%)</td><td>113.93 (+7.71%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>497.40 (n/a)</td><td>377.66 (n/a)</td><td>368.10 (n/a)</td><td>261.30 (n/a)</td><td>105.77 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (+9.78%)</td><td>0.08 (-15.52%)</td><td>0.06 <b>(-39.42%)</b></td><td>0.06 (-2.34%)</td><td>0.04 (+16.99%)</td><td>599.30 (+2.39%)</td><td>498.74 <b>(+20.02%)</b></td><td>548.80 <b>(+65.05%)</b></td><td>240.80 (-8.89%)</td><td>146.77 (-3.18%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>585.30 (n/a)</td><td>415.54 (n/a)</td><td>332.50 (n/a)</td><td>264.30 (n/a)</td><td>151.59 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.47 (+16.23%)</td><td>0.27 (-4.46%)</td><td>0.23 (-14.12%)</td><td>0.06 <b>(-66.50%)</b></td><td>0.18 <b>(+123.79%)</b></td><td>2116.80 <b>(+198.48%)</b></td><td>826.28 <b>(+67.13%)</b></td><td>567.20 (+16.44%)</td><td>278.20 (-13.98%)</td><td>759.59 <b>(+448.80%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>709.20 (n/a)</td><td>494.40 (n/a)</td><td>487.10 (n/a)</td><td>323.40 (n/a)</td><td>138.41 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.48 (-6.24%)</td><td>0.29 (-4.45%)</td><td>0.24 (-11.68%)</td><td>0.05 (-1.12%)</td><td>0.18 (-5.52%)</td><td>2462.90 (+1.13%)</td><td>825.04 (+2.32%)</td><td>549.90 (+13.22%)</td><td>271.60 (+6.68%)</td><td>925.87 (+0.52%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.51 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>0.19 (n/a)</td><td>2435.40 (n/a)</td><td>806.30 (n/a)</td><td>485.70 (n/a)</td><td>254.60 (n/a)</td><td>921.07 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.46 (+16.95%)</td><td>0.30 (+10.41%)</td><td>0.24 (-6.24%)</td><td>0.17 (-18.59%)</td><td>0.14 <b>(+100.31%)</b></td><td>752.40 <b>(+22.84%)</b></td><td>508.60 (+2.31%)</td><td>538.20 (+6.64%)</td><td>285.00 (-14.49%)</td><td>214.11 <b>(+108.34%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>612.50 (n/a)</td><td>497.10 (n/a)</td><td>504.70 (n/a)</td><td>333.30 (n/a)</td><td>102.77 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.00 (-16.67%)</td><td>0.00 <b>(+21.43%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-15.22%)</td><td>20770.83 (+5.60%)</td><td>14205.58 (-9.20%)</td><td>16046.19 (-4.78%)</td><td>7452.84 (+16.00%)</td><td>6153.67 (+16.19%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19669.53 (n/a)</td><td>15644.39 (n/a)</td><td>16851.43 (n/a)</td><td>6424.65 (n/a)</td><td>5296.31 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.00 <b>(-53.85%)</b></td><td>0.00 <b>(-36.11%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-76.26%)</b></td><td>22581.70 (+8.83%)</td><td>18347.28 <b>(+28.06%)</b></td><td>18600.42 (+4.71%)</td><td>14484.71 <b>(+127.42%)</b></td><td>3072.58 <b>(-51.73%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20749.86 (n/a)</td><td>14327.13 (n/a)</td><td>17764.38 (n/a)</td><td>6369.17 (n/a)</td><td>6365.30 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.16 (+16.73%)</td><td>0.10 (+0.11%)</td><td>0.09 (+3.52%)</td><td>0.07 (-12.72%)</td><td>0.04 <b>(+46.32%)</b></td><td>30896.59 (+14.56%)</td><td>23896.05 (+3.68%)</td><td>24569.85 (-3.35%)</td><td>13414.36 (-14.38%)</td><td>6444.59 <b>(+32.03%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>26969.89 (n/a)</td><td>23047.24 (n/a)</td><td>25420.40 (n/a)</td><td>15666.95 (n/a)</td><td>4881.19 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.24 (+6.21%)</td><td>2.00 <b>(+41.78%)</b></td><td>2.46 <b>(+114.58%)</b></td><td>0.31 (+1.88%)</td><td>1.24 (+17.07%)</td><td>3352.30 (-1.85%)</td><td>1082.14 (-18.06%)</td><td>426.20 <b>(-53.40%)</b></td><td>323.30 (-5.85%)</td><td>1293.70 (+5.30%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.05 (n/a)</td><td>1.41 (n/a)</td><td>1.15 (n/a)</td><td>0.31 (n/a)</td><td>1.06 (n/a)</td><td>3415.40 (n/a)</td><td>1320.70 (n/a)</td><td>914.60 (n/a)</td><td>343.40 (n/a)</td><td>1228.58 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.99 (-0.80%)</td><td>2.01 (-9.19%)</td><td>1.46 (-16.82%)</td><td>1.37 (-11.44%)</td><td>1.12 (+9.74%)</td><td>766.20 (+12.93%)</td><td>613.00 (+15.38%)</td><td>719.20 <b>(+20.23%)</b></td><td>262.90 (+0.81%)</td><td>212.50 <b>(+31.17%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>4.02 (n/a)</td><td>2.22 (n/a)</td><td>1.75 (n/a)</td><td>1.55 (n/a)</td><td>1.02 (n/a)</td><td>678.50 (n/a)</td><td>531.28 (n/a)</td><td>598.20 (n/a)</td><td>260.80 (n/a)</td><td>162.00 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>2.70 (-16.24%)</td><td>1.67 (-9.28%)</td><td>1.71 (+13.39%)</td><td>0.32 <b>(-76.58%)</b></td><td>0.87 (+11.42%)</td><td>3285.90 <b>(+326.91%)</b></td><td>1094.04 <b>(+73.68%)</b></td><td>612.00 (-11.82%)</td><td>387.80 (+19.40%)</td><td>1229.98 <b>(+594.47%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.23 (n/a)</td><td>1.84 (n/a)</td><td>1.51 (n/a)</td><td>1.36 (n/a)</td><td>0.78 (n/a)</td><td>769.70 (n/a)</td><td>629.92 (n/a)</td><td>694.00 (n/a)</td><td>324.80 (n/a)</td><td>177.11 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>4.36 <b>(+59.38%)</b></td><td>2.87 <b>(+42.02%)</b></td><td>2.90 (+14.70%)</td><td>1.71 <b>(+305.20%)</b></td><td>1.01 (+4.22%)</td><td>611.70 <b>(-75.32%)</b></td><td>403.06 <b>(-52.65%)</b></td><td>362.00 (-12.81%)</td><td>240.70 <b>(-37.25%)</b></td><td>142.90 <b>(-84.35%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>2.73 (n/a)</td><td>2.02 (n/a)</td><td>2.53 (n/a)</td><td>0.42 (n/a)</td><td>0.97 (n/a)</td><td>2478.40 (n/a)</td><td>851.22 (n/a)</td><td>415.20 (n/a)</td><td>383.60 (n/a)</td><td>913.10 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>4.23 (+8.98%)</td><td>2.21 (-16.94%)</td><td>2.16 <b>(-29.54%)</b></td><td>0.58 (-17.98%)</td><td>1.64 <b>(+32.49%)</b></td><td>3630.60 <b>(+21.93%)</b></td><td>1795.58 <b>(+56.50%)</b></td><td>971.00 <b>(+41.92%)</b></td><td>495.40 (-8.24%)</td><td>1528.04 <b>(+47.97%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.88 (n/a)</td><td>2.67 (n/a)</td><td>3.07 (n/a)</td><td>0.70 (n/a)</td><td>1.24 (n/a)</td><td>2977.70 (n/a)</td><td>1147.36 (n/a)</td><td>684.20 (n/a)</td><td>539.90 (n/a)</td><td>1032.67 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>5.87 (+0.03%)</td><td>3.84 <b>(+51.40%)</b></td><td>3.66 <b>(+88.35%)</b></td><td>0.87 <b>(+48.78%)</b></td><td>1.93 (-2.34%)</td><td>2408.90 <b>(-32.79%)</b></td><td>866.22 <b>(-38.18%)</b></td><td>573.00 <b>(-46.91%)</b></td><td>357.00 (-0.03%)</td><td>868.46 <b>(-30.86%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.87 (n/a)</td><td>2.53 (n/a)</td><td>1.94 (n/a)</td><td>0.59 (n/a)</td><td>1.98 (n/a)</td><td>3583.90 (n/a)</td><td>1401.18 (n/a)</td><td>1079.30 (n/a)</td><td>357.10 (n/a)</td><td>1256.01 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.00 (+3.95%)</td><td>2.76 (-16.51%)</td><td>2.29 <b>(-34.52%)</b></td><td>0.59 (+1.22%)</td><td>2.16 (+15.58%)</td><td>3553.60 (-1.21%)</td><td>1416.42 <b>(+21.32%)</b></td><td>916.50 <b>(+52.72%)</b></td><td>349.40 (-3.80%)</td><td>1299.28 (-4.77%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.77 (n/a)</td><td>3.31 (n/a)</td><td>3.49 (n/a)</td><td>0.58 (n/a)</td><td>1.87 (n/a)</td><td>3597.10 (n/a)</td><td>1167.50 (n/a)</td><td>600.10 (n/a)</td><td>363.20 (n/a)</td><td>1364.36 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>7.20 (-0.38%)</td><td>4.16 (-11.29%)</td><td>4.91 <b>(+25.95%)</b></td><td>0.58 <b>(-81.51%)</b></td><td>2.57 <b>(+51.64%)</b></td><td>3588.40 <b>(+440.91%)</b></td><td>1095.48 <b>(+122.98%)</b></td><td>427.50 <b>(-20.61%)</b></td><td>291.30 (+0.38%)</td><td>1405.91 <b>(+812.93%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>7.23 (n/a)</td><td>4.68 (n/a)</td><td>3.89 (n/a)</td><td>3.16 (n/a)</td><td>1.69 (n/a)</td><td>663.40 (n/a)</td><td>491.28 (n/a)</td><td>538.50 (n/a)</td><td>290.20 (n/a)</td><td>154.00 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>5.63 (-1.21%)</td><td>4.21 (+17.82%)</td><td>4.05 (-2.65%)</td><td>2.02 <b>(+235.73%)</b></td><td>1.50 <b>(-32.36%)</b></td><td>1039.80 <b>(-70.21%)</b></td><td>572.48 <b>(-50.65%)</b></td><td>517.90 (+2.72%)</td><td>372.40 (+1.22%)</td><td>274.08 <b>(-79.43%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.70 (n/a)</td><td>3.57 (n/a)</td><td>4.16 (n/a)</td><td>0.60 (n/a)</td><td>2.21 (n/a)</td><td>3490.80 (n/a)</td><td>1160.14 (n/a)</td><td>504.20 (n/a)</td><td>367.90 (n/a)</td><td>1332.15 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>7.22 <b>(+43.00%)</b></td><td>4.47 <b>(+34.61%)</b></td><td>3.68 (+18.67%)</td><td>2.62 <b>(+50.99%)</b></td><td>2.01 <b>(+26.06%)</b></td><td>801.10 <b>(-33.77%)</b></td><td>546.38 <b>(-29.27%)</b></td><td>570.40 (-15.72%)</td><td>290.40 <b>(-30.07%)</b></td><td>221.83 <b>(-41.44%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.05 (n/a)</td><td>3.32 (n/a)</td><td>3.10 (n/a)</td><td>1.73 (n/a)</td><td>1.59 (n/a)</td><td>1209.60 (n/a)</td><td>772.44 (n/a)</td><td>676.80 (n/a)</td><td>415.30 (n/a)</td><td>378.81 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>5.54 (+6.68%)</td><td>3.57 (-15.65%)</td><td>3.91 <b>(-20.23%)</b></td><td>1.98 (+15.55%)</td><td>1.56 (+8.87%)</td><td>2114.10 (-13.46%)</td><td>1399.54 (+18.49%)</td><td>1072.80 <b>(+25.36%)</b></td><td>756.50 (-6.27%)</td><td>658.32 (-6.91%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>5.20 (n/a)</td><td>4.23 (n/a)</td><td>4.90 (n/a)</td><td>1.72 (n/a)</td><td>1.43 (n/a)</td><td>2442.90 (n/a)</td><td>1181.14 (n/a)</td><td>855.80 (n/a)</td><td>807.10 (n/a)</td><td>707.23 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.92 <b>(-25.54%)</b></td><td>4.71 (-7.04%)</td><td>4.38 <b>(-26.45%)</b></td><td>2.02 <b>(+72.69%)</b></td><td>1.88 <b>(-49.78%)</b></td><td>2071.40 <b>(-42.09%)</b></td><td>1064.86 <b>(-39.30%)</b></td><td>956.80 <b>(+35.97%)</b></td><td>606.20 <b>(+34.29%)</b></td><td>586.13 <b>(-64.03%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>9.29 (n/a)</td><td>5.07 (n/a)</td><td>5.96 (n/a)</td><td>1.17 (n/a)</td><td>3.73 (n/a)</td><td>3577.00 (n/a)</td><td>1754.16 (n/a)</td><td>703.70 (n/a)</td><td>451.40 (n/a)</td><td>1629.53 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>8.01 (-11.85%)</td><td>5.72 (-6.57%)</td><td>7.26 (+9.95%)</td><td>1.71 (+1.86%)</td><td>2.84 (+5.19%)</td><td>2452.30 (-1.83%)</td><td>1042.28 (+7.17%)</td><td>577.60 (-9.04%)</td><td>523.90 (+13.45%)</td><td>827.68 (-3.31%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>9.08 (n/a)</td><td>6.12 (n/a)</td><td>6.60 (n/a)</td><td>1.68 (n/a)</td><td>2.70 (n/a)</td><td>2497.90 (n/a)</td><td>972.54 (n/a)</td><td>635.00 (n/a)</td><td>461.80 (n/a)</td><td>855.98 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>10.34 (+2.51%)</td><td>7.50 <b>(+34.48%)</b></td><td>6.55 <b>(+65.88%)</b></td><td>6.30 <b>(+439.78%)</b></td><td>1.71 <b>(-54.35%)</b></td><td>665.90 <b>(-81.47%)</b></td><td>579.06 <b>(-56.34%)</b></td><td>639.90 <b>(-39.71%)</b></td><td>405.80 (-2.45%)</td><td>110.27 <b>(-91.56%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>10.08 (n/a)</td><td>5.58 (n/a)</td><td>3.95 (n/a)</td><td>1.17 (n/a)</td><td>3.74 (n/a)</td><td>3594.20 (n/a)</td><td>1326.42 (n/a)</td><td>1061.40 (n/a)</td><td>416.00 (n/a)</td><td>1306.19 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.60 <b>(-36.90%)</b></td><td>3.78 <b>(-28.37%)</b></td><td>3.15 <b>(-23.88%)</b></td><td>1.14 (-3.43%)</td><td>2.53 <b>(-27.78%)</b></td><td>3667.20 (+3.56%)</td><td>1741.16 <b>(+30.66%)</b></td><td>1332.60 <b>(+31.37%)</b></td><td>635.20 <b>(+58.48%)</b></td><td>1292.10 (+2.05%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>10.46 (n/a)</td><td>5.27 (n/a)</td><td>4.13 (n/a)</td><td>1.18 (n/a)</td><td>3.50 (n/a)</td><td>3541.30 (n/a)</td><td>1332.58 (n/a)</td><td>1014.40 (n/a)</td><td>400.80 (n/a)</td><td>1266.09 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>9.97 <b>(+23.53%)</b></td><td>6.78 <b>(+72.21%)</b></td><td>6.63 <b>(+85.94%)</b></td><td>2.26 <b>(+93.22%)</b></td><td>2.91 (-1.15%)</td><td>1859.80 <b>(-48.25%)</b></td><td>809.62 <b>(-56.44%)</b></td><td>633.00 <b>(-46.22%)</b></td><td>420.60 (-19.05%)</td><td>594.70 <b>(-59.07%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>8.07 (n/a)</td><td>3.94 (n/a)</td><td>3.56 (n/a)</td><td>1.17 (n/a)</td><td>2.95 (n/a)</td><td>3593.50 (n/a)</td><td>1858.48 (n/a)</td><td>1177.10 (n/a)</td><td>519.60 (n/a)</td><td>1453.00 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>1.51 <b>(-29.68%)</b></td><td>1.20 (+7.19%)</td><td>1.30 <b>(+23.88%)</b></td><td>0.82 <b>(+417.00%)</b></td><td>0.34 <b>(-52.47%)</b></td><td>638.30 <b>(-80.66%)</b></td><td>468.74 <b>(-53.07%)</b></td><td>402.40 (-19.28%)</td><td>347.20 <b>(+42.24%)</b></td><td>143.04 <b>(-88.92%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>2.15 (n/a)</td><td>1.12 (n/a)</td><td>1.05 (n/a)</td><td>0.16 (n/a)</td><td>0.71 (n/a)</td><td>3300.00 (n/a)</td><td>998.76 (n/a)</td><td>498.50 (n/a)</td><td>244.10 (n/a)</td><td>1291.36 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>2.84 (+3.50%)</td><td>2.34 <b>(+40.48%)</b></td><td>2.42 <b>(+33.33%)</b></td><td>1.78 <b>(+501.60%)</b></td><td>0.50 <b>(-43.11%)</b></td><td>588.30 <b>(-83.38%)</b></td><td>464.76 <b>(-59.27%)</b></td><td>433.20 <b>(-25.00%)</b></td><td>368.60 (-3.38%)</td><td>103.34 <b>(-92.31%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>2.75 (n/a)</td><td>1.67 (n/a)</td><td>1.82 (n/a)</td><td>0.30 (n/a)</td><td>0.88 (n/a)</td><td>3539.50 (n/a)</td><td>1141.14 (n/a)</td><td>577.60 (n/a)</td><td>381.50 (n/a)</td><td>1344.15 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.16 (-14.15%)</td><td>1.79 (+7.19%)</td><td>1.93 <b>(+134.35%)</b></td><td>0.58 (+3.80%)</td><td>1.18 (-17.46%)</td><td>3615.40 (-3.66%)</td><td>1938.86 (-13.71%)</td><td>1089.20 <b>(-57.33%)</b></td><td>663.90 (+16.47%)</td><td>1507.99 (-0.17%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>3.68 (n/a)</td><td>1.67 (n/a)</td><td>0.82 (n/a)</td><td>0.56 (n/a)</td><td>1.44 (n/a)</td><td>3752.90 (n/a)</td><td>2246.82 (n/a)</td><td>2552.50 (n/a)</td><td>570.00 (n/a)</td><td>1510.59 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>1.74 (-19.61%)</td><td>1.52 (+11.15%)</td><td>1.62 (-0.98%)</td><td>1.00 <b>(+266.58%)</b></td><td>0.30 <b>(-60.31%)</b></td><td>525.30 <b>(-72.72%)</b></td><td>360.16 <b>(-45.76%)</b></td><td>323.10 (+1.00%)</td><td>301.30 <b>(+24.40%)</b></td><td>92.96 <b>(-86.98%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>2.16 (n/a)</td><td>1.36 (n/a)</td><td>1.64 (n/a)</td><td>0.27 (n/a)</td><td>0.74 (n/a)</td><td>1925.80 (n/a)</td><td>663.96 (n/a)</td><td>319.90 (n/a)</td><td>242.20 (n/a)</td><td>714.13 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (+3.82%)</td><td>0.09 (-6.87%)</td><td>0.09 (+12.02%)</td><td>0.05 <b>(-20.68%)</b></td><td>0.04 <b>(+29.51%)</b></td><td>633.40 <b>(+26.07%)</b></td><td>422.16 (+15.78%)</td><td>352.90 (-10.73%)</td><td>233.90 (-3.71%)</td><td>176.91 <b>(+70.92%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>502.40 (n/a)</td><td>364.62 (n/a)</td><td>395.30 (n/a)</td><td>242.90 (n/a)</td><td>103.51 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (+7.82%)</td><td>0.09 (+10.39%)</td><td>0.08 (+13.53%)</td><td>0.03 <b>(-40.53%)</b></td><td>0.05 <b>(+58.12%)</b></td><td>1090.00 <b>(+68.13%)</b></td><td>487.70 (+13.06%)</td><td>388.70 (-11.92%)</td><td>229.00 (-7.21%)</td><td>354.54 <b>(+142.57%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>648.30 (n/a)</td><td>431.36 (n/a)</td><td>441.30 (n/a)</td><td>246.80 (n/a)</td><td>146.16 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.24 (-9.48%)</td><td>0.17 (-4.02%)</td><td>0.14 (-3.73%)</td><td>0.13 (+16.59%)</td><td>0.05 <b>(-28.09%)</b></td><td>518.70 (-14.24%)</td><td>416.30 (-1.48%)</td><td>460.60 (+3.88%)</td><td>270.60 (+10.45%)</td><td>105.18 <b>(-30.66%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>604.80 (n/a)</td><td>422.54 (n/a)</td><td>443.40 (n/a)</td><td>245.00 (n/a)</td><td>151.67 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.26 (-0.58%)</td><td>0.21 <b>(+25.25%)</b></td><td>0.22 <b>(+65.64%)</b></td><td>0.14 <b>(+29.27%)</b></td><td>0.04 <b>(-37.37%)</b></td><td>453.50 <b>(-22.64%)</b></td><td>317.94 <b>(-25.95%)</b></td><td>295.20 <b>(-39.62%)</b></td><td>253.50 (+0.60%)</td><td>77.89 <b>(-47.78%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>586.20 (n/a)</td><td>429.38 (n/a)</td><td>488.90 (n/a)</td><td>252.00 (n/a)</td><td>149.18 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.24 (-14.84%)</td><td>0.16 <b>(-22.57%)</b></td><td>0.14 <b>(-41.25%)</b></td><td>0.09 (-15.47%)</td><td>0.06 <b>(-31.24%)</b></td><td>744.90 (+18.31%)</td><td>469.16 <b>(+21.19%)</b></td><td>452.60 <b>(+70.21%)</b></td><td>268.70 (+17.44%)</td><td>175.04 (-6.24%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>629.60 (n/a)</td><td>387.14 (n/a)</td><td>265.90 (n/a)</td><td>228.80 (n/a)</td><td>186.68 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.51 (+1.57%)</td><td>0.42 (+2.20%)</td><td>0.44 (+5.20%)</td><td>0.24 (-4.61%)</td><td>0.11 (+9.28%)</td><td>546.80 (+4.83%)</td><td>333.58 (-0.74%)</td><td>295.20 (-4.93%)</td><td>259.50 (-1.56%)</td><td>120.62 (+13.50%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.50 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>521.60 (n/a)</td><td>336.06 (n/a)</td><td>310.50 (n/a)</td><td>263.60 (n/a)</td><td>106.28 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.47 (-11.64%)</td><td>0.30 (-18.57%)</td><td>0.28 (-19.80%)</td><td>0.13 <b>(-41.38%)</b></td><td>0.14 (+3.94%)</td><td>1025.10 <b>(+70.62%)</b></td><td>538.78 <b>(+36.06%)</b></td><td>471.80 <b>(+24.68%)</b></td><td>281.90 (+13.21%)</td><td>301.28 <b>(+102.25%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.53 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>600.80 (n/a)</td><td>395.98 (n/a)</td><td>378.40 (n/a)</td><td>249.00 (n/a)</td><td>148.97 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.56 <b>(+21.00%)</b></td><td>0.33 (-5.53%)</td><td>0.28 (-15.41%)</td><td>0.26 (+4.60%)</td><td>0.12 <b>(+51.70%)</b></td><td>503.90 (-4.40%)</td><td>425.82 (+9.44%)</td><td>461.10 (+18.23%)</td><td>236.10 (-17.36%)</td><td>107.78 (+14.80%)</td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.46 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.08 (n/a)</td><td>527.10 (n/a)</td><td>389.10 (n/a)</td><td>390.00 (n/a)</td><td>285.70 (n/a)</td><td>93.88 (n/a)</td>
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
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 <b>(+20.60%)</b></td><td>0.05 <b>(+47.72%)</b></td><td>0.06 <b>(+61.56%)</b></td><td>0.02 (-4.47%)</td><td>0.02 <b>(+44.44%)</b></td><td>714.30 (+4.69%)</td><td>355.20 <b>(-26.73%)</b></td><td>281.40 <b>(-38.10%)</b></td><td>235.90 (-17.08%)</td><td>202.32 <b>(+35.26%)</b></td>
</tr>
<tr>
<td><code>ece908d</code> — 2026-07-31 18:29:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>682.30 (n/a)</td><td>484.76 (n/a)</td><td>454.60 (n/a)</td><td>284.50 (n/a)</td><td>149.58 (n/a)</td>
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
