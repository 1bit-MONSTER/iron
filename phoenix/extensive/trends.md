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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-13.78%)</td><td>0.02 (+12.37%)</td><td>0.03 <b>(+35.22%)</b></td><td>0.01 (+8.49%)</td><td>0.01 <b>(-29.96%)</b></td><td>459.10 (-7.81%)</td><td>294.18 (-16.21%)</td><td>242.60 <b>(-26.06%)</b></td><td>232.20 (+15.98%)</td><td>96.18 <b>(-28.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>498.00 (n/a)</td><td>351.10 (n/a)</td><td>328.10 (n/a)</td><td>200.20 (n/a)</td><td>134.57 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (+6.69%)</td><td>0.02 (-11.76%)</td><td>0.02 (-17.03%)</td><td>0.01 (-13.52%)</td><td>0.01 (+11.60%)</td><td>658.70 (+15.62%)</td><td>366.66 (+17.00%)</td><td>299.70 <b>(+20.56%)</b></td><td>220.30 (-6.26%)</td><td>175.42 <b>(+21.62%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.70 (n/a)</td><td>313.38 (n/a)</td><td>248.60 (n/a)</td><td>235.00 (n/a)</td><td>144.24 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-10.51%)</td><td>0.02 (-11.50%)</td><td>0.02 <b>(-25.06%)</b></td><td>0.01 (-11.39%)</td><td>0.01 (-0.80%)</td><td>556.80 (+12.85%)</td><td>364.02 (+15.40%)</td><td>394.20 <b>(+33.45%)</b></td><td>207.90 (+11.71%)</td><td>141.57 (+19.63%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>493.40 (n/a)</td><td>315.44 (n/a)</td><td>295.40 (n/a)</td><td>186.10 (n/a)</td><td>118.34 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-6.20%)</td><td>0.02 (-0.75%)</td><td>0.02 (-14.54%)</td><td>0.00 (-13.60%)</td><td>0.01 (-11.70%)</td><td>2456.40 (+15.74%)</td><td>725.28 (+5.50%)</td><td>292.40 (+17.01%)</td><td>222.50 (+6.61%)</td><td>970.32 (+18.59%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2122.30 (n/a)</td><td>687.50 (n/a)</td><td>249.90 (n/a)</td><td>208.70 (n/a)</td><td>818.23 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(+20.21%)</b></td><td>0.02 <b>(+47.28%)</b></td><td>0.02 <b>(+65.41%)</b></td><td>0.01 <b>(+41.70%)</b></td><td>0.00 (+11.23%)</td><td>464.40 <b>(-29.42%)</b></td><td>360.22 <b>(-33.26%)</b></td><td>358.90 <b>(-39.55%)</b></td><td>267.30 (-16.81%)</td><td>89.10 <b>(-34.03%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>658.00 (n/a)</td><td>539.72 (n/a)</td><td>593.70 (n/a)</td><td>321.30 (n/a)</td><td>135.07 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (+13.17%)</td><td>0.02 <b>(+25.97%)</b></td><td>0.02 <b>(+73.65%)</b></td><td>0.01 (+16.30%)</td><td>0.01 (-12.75%)</td><td>446.00 (-14.02%)</td><td>314.70 <b>(-23.96%)</b></td><td>291.10 <b>(-42.40%)</b></td><td>228.50 (-11.64%)</td><td>88.07 <b>(-34.59%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>518.70 (n/a)</td><td>413.86 (n/a)</td><td>505.40 (n/a)</td><td>258.60 (n/a)</td><td>134.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 <b>(+62.14%)</b></td><td>0.04 <b>(+62.57%)</b></td><td>0.05 <b>(+96.39%)</b></td><td>0.03 <b>(+32.92%)</b></td><td>0.01 <b>(+55.71%)</b></td><td>451.70 <b>(-24.77%)</b></td><td>296.70 <b>(-37.86%)</b></td><td>270.60 <b>(-49.08%)</b></td><td>215.90 <b>(-38.31%)</b></td><td>92.27 <b>(-21.66%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.40 (n/a)</td><td>477.48 (n/a)</td><td>531.40 (n/a)</td><td>350.00 (n/a)</td><td>117.78 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (-5.41%)</td><td>0.04 (+13.97%)</td><td>0.04 <b>(+40.02%)</b></td><td>0.03 <b>(+24.30%)</b></td><td>0.01 <b>(-25.73%)</b></td><td>443.40 (-19.54%)</td><td>312.64 (-15.79%)</td><td>275.20 <b>(-28.58%)</b></td><td>245.30 (+5.69%)</td><td>78.69 <b>(-34.59%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>551.10 (n/a)</td><td>371.28 (n/a)</td><td>385.30 (n/a)</td><td>232.10 (n/a)</td><td>120.31 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 <b>(+47.64%)</b></td><td>0.03 (+12.66%)</td><td>0.03 (+10.41%)</td><td>0.02 (-0.61%)</td><td>0.01 <b>(+87.40%)</b></td><td>601.90 (+0.62%)</td><td>460.54 (-6.06%)</td><td>474.90 (-9.42%)</td><td>238.70 <b>(-32.26%)</b></td><td>140.76 <b>(+20.84%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>598.20 (n/a)</td><td>490.24 (n/a)</td><td>524.30 (n/a)</td><td>352.40 (n/a)</td><td>116.48 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 <b>(+23.28%)</b></td><td>0.04 <b>(+25.18%)</b></td><td>0.05 (+15.75%)</td><td>0.02 (+17.26%)</td><td>0.01 (+0.61%)</td><td>529.20 (-14.73%)</td><td>306.34 <b>(-23.91%)</b></td><td>243.80 (-13.58%)</td><td>203.00 (-18.90%)</td><td>132.18 <b>(-29.92%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>620.60 (n/a)</td><td>402.58 (n/a)</td><td>282.10 (n/a)</td><td>250.30 (n/a)</td><td>188.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 <b>(+38.51%)</b></td><td>0.03 (-2.48%)</td><td>0.02 <b>(-21.77%)</b></td><td>0.02 (+4.33%)</td><td>0.01 <b>(+72.80%)</b></td><td>618.70 (-4.15%)</td><td>529.36 (+10.56%)</td><td>615.70 <b>(+27.82%)</b></td><td>229.10 <b>(-27.80%)</b></td><td>169.42 (+18.09%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>645.50 (n/a)</td><td>478.82 (n/a)</td><td>481.70 (n/a)</td><td>317.30 (n/a)</td><td>143.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (-9.91%)</td><td>0.03 (-7.45%)</td><td>0.02 <b>(-20.57%)</b></td><td>0.01 <b>(-21.50%)</b></td><td>0.01 (-3.24%)</td><td>924.30 <b>(+27.40%)</b></td><td>539.26 (+12.59%)</td><td>551.10 <b>(+25.91%)</b></td><td>268.90 (+11.02%)</td><td>249.77 <b>(+40.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>725.50 (n/a)</td><td>478.98 (n/a)</td><td>437.70 (n/a)</td><td>242.20 (n/a)</td><td>178.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 <b>(+32.99%)</b></td><td>0.08 <b>(+21.33%)</b></td><td>0.09 <b>(+31.55%)</b></td><td>0.04 <b>(-25.32%)</b></td><td>0.03 <b>(+131.31%)</b></td><td>611.30 <b>(+33.91%)</b></td><td>334.40 (-8.56%)</td><td>277.50 <b>(-23.99%)</b></td><td>218.90 <b>(-24.80%)</b></td><td>158.74 <b>(+149.26%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>456.50 (n/a)</td><td>365.72 (n/a)</td><td>365.10 (n/a)</td><td>291.10 (n/a)</td><td>63.68 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (+6.48%)</td><td>0.08 (+3.71%)</td><td>0.08 (-0.02%)</td><td>0.04 (-3.46%)</td><td>0.02 (+1.19%)</td><td>567.00 (+3.58%)</td><td>342.40 (-3.12%)</td><td>296.20 (+0.00%)</td><td>238.70 (-6.06%)</td><td>129.04 (+5.87%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>547.40 (n/a)</td><td>353.44 (n/a)</td><td>296.20 (n/a)</td><td>254.10 (n/a)</td><td>121.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (-17.60%)</td><td>0.06 (+2.36%)</td><td>0.06 <b>(+21.52%)</b></td><td>0.05 (+18.97%)</td><td>0.01 <b>(-54.60%)</b></td><td>477.40 (-15.95%)</td><td>397.48 (-9.56%)</td><td>404.40 (-17.70%)</td><td>333.10 <b>(+21.35%)</b></td><td>63.49 <b>(-55.44%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>568.00 (n/a)</td><td>439.52 (n/a)</td><td>491.40 (n/a)</td><td>274.50 (n/a)</td><td>142.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 <b>(-22.66%)</b></td><td>0.07 (-10.35%)</td><td>0.07 (-14.85%)</td><td>0.05 (-13.53%)</td><td>0.02 <b>(-36.83%)</b></td><td>528.10 (+15.66%)</td><td>373.56 (+7.95%)</td><td>371.60 (+17.45%)</td><td>272.90 <b>(+29.28%)</b></td><td>96.27 (-7.71%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>456.60 (n/a)</td><td>346.06 (n/a)</td><td>316.40 (n/a)</td><td>211.10 (n/a)</td><td>104.31 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (-7.38%)</td><td>0.07 (+10.36%)</td><td>0.08 <b>(+32.56%)</b></td><td>0.04 (-7.03%)</td><td>0.02 (+5.99%)</td><td>595.90 (+7.56%)</td><td>382.04 (-7.40%)</td><td>296.10 <b>(-24.56%)</b></td><td>270.80 (+7.97%)</td><td>143.22 <b>(+20.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>554.00 (n/a)</td><td>412.58 (n/a)</td><td>392.50 (n/a)</td><td>250.80 (n/a)</td><td>119.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (+14.10%)</td><td>0.06 (-0.47%)</td><td>0.05 (-17.20%)</td><td>0.05 (-5.91%)</td><td>0.02 <b>(+66.01%)</b></td><td>530.20 (+6.30%)</td><td>410.02 (+4.91%)</td><td>460.30 <b>(+20.78%)</b></td><td>261.80 (-12.38%)</td><td>114.14 <b>(+53.54%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>498.80 (n/a)</td><td>390.84 (n/a)</td><td>381.10 (n/a)</td><td>298.80 (n/a)</td><td>74.34 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.20 (-14.96%)</td><td>0.13 <b>(-20.10%)</b></td><td>0.10 <b>(-37.02%)</b></td><td>0.09 (-15.82%)</td><td>0.04 (-10.64%)</td><td>550.40 (+18.77%)</td><td>423.40 <b>(+25.98%)</b></td><td>476.30 <b>(+58.77%)</b></td><td>246.50 (+17.60%)</td><td>121.36 <b>(+20.92%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>463.40 (n/a)</td><td>336.08 (n/a)</td><td>300.00 (n/a)</td><td>209.60 (n/a)</td><td>100.36 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.19 (-6.09%)</td><td>0.13 (-19.99%)</td><td>0.12 <b>(-34.18%)</b></td><td>0.05 <b>(-48.44%)</b></td><td>0.06 (+9.57%)</td><td>1014.40 <b>(+93.92%)</b></td><td>491.92 <b>(+42.07%)</b></td><td>407.30 <b>(+51.92%)</b></td><td>252.50 (+6.50%)</td><td>306.73 <b>(+133.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>523.10 (n/a)</td><td>346.26 (n/a)</td><td>268.10 (n/a)</td><td>237.10 (n/a)</td><td>131.26 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.20 (+2.92%)</td><td>0.16 (+0.57%)</td><td>0.17 (-2.09%)</td><td>0.09 (+3.62%)</td><td>0.04 (+0.76%)</td><td>559.50 (-3.50%)</td><td>341.10 (-1.04%)</td><td>295.30 (+2.11%)</td><td>245.60 (-2.85%)</td><td>127.00 (-5.76%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>579.80 (n/a)</td><td>344.70 (n/a)</td><td>289.20 (n/a)</td><td>252.80 (n/a)</td><td>134.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.20 (-7.95%)</td><td>0.17 (-0.49%)</td><td>0.17 (-1.38%)</td><td>0.13 <b>(+54.32%)</b></td><td>0.03 <b>(-47.76%)</b></td><td>390.10 <b>(-35.21%)</b></td><td>303.62 (-8.89%)</td><td>296.40 (+1.40%)</td><td>247.00 (+8.62%)</td><td>55.39 <b>(-64.11%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>602.10 (n/a)</td><td>333.26 (n/a)</td><td>292.30 (n/a)</td><td>227.40 (n/a)</td><td>154.36 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 (-8.63%)</td><td>0.14 (-3.87%)</td><td>0.15 (+9.70%)</td><td>0.07 <b>(-28.85%)</b></td><td>0.04 (+10.53%)</td><td>658.00 <b>(+40.54%)</b></td><td>392.32 (+8.35%)</td><td>330.60 (-8.85%)</td><td>295.70 (+9.44%)</td><td>149.72 <b>(+83.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>468.20 (n/a)</td><td>362.08 (n/a)</td><td>362.70 (n/a)</td><td>270.20 (n/a)</td><td>81.73 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.20 (-3.49%)</td><td>0.15 (-5.00%)</td><td>0.17 (-13.94%)</td><td>0.10 (+4.69%)</td><td>0.04 <b>(-30.23%)</b></td><td>482.90 (-4.49%)</td><td>345.56 (-0.86%)</td><td>294.80 (+16.20%)</td><td>249.30 (+3.62%)</td><td>96.30 <b>(-30.75%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>505.60 (n/a)</td><td>348.56 (n/a)</td><td>253.70 (n/a)</td><td>240.60 (n/a)</td><td>139.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (+8.97%)</td><td>0.01 (-3.26%)</td><td>0.01 <b>(-29.80%)</b></td><td>0.01 (+19.84%)</td><td>0.00 <b>(+32.29%)</b></td><td>495.60 (-16.55%)</td><td>363.28 (+5.70%)</td><td>434.00 <b>(+42.48%)</b></td><td>214.80 (-8.24%)</td><td>130.43 (-8.96%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>593.90 (n/a)</td><td>343.70 (n/a)</td><td>304.60 (n/a)</td><td>234.10 (n/a)</td><td>143.27 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (+2.44%)</td><td>0.01 (-0.52%)</td><td>0.01 (+3.17%)</td><td>0.00 <b>(-43.33%)</b></td><td>0.00 <b>(+50.72%)</b></td><td>847.20 <b>(+76.46%)</b></td><td>434.08 (+15.78%)</td><td>404.90 (-3.06%)</td><td>244.20 (-2.40%)</td><td>245.53 <b>(+154.27%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>480.10 (n/a)</td><td>374.92 (n/a)</td><td>417.70 (n/a)</td><td>250.20 (n/a)</td><td>96.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (+0.91%)</td><td>0.01 (+2.19%)</td><td>0.01 <b>(+24.17%)</b></td><td>0.00 (-13.59%)</td><td>0.00 (+18.49%)</td><td>618.70 (+15.73%)</td><td>388.40 (+3.40%)</td><td>292.20 (-19.46%)</td><td>230.80 (-0.90%)</td><td>170.18 <b>(+39.80%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>534.60 (n/a)</td><td>375.64 (n/a)</td><td>362.80 (n/a)</td><td>232.90 (n/a)</td><td>121.74 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (+1.15%)</td><td>0.01 (-9.43%)</td><td>0.01 <b>(-21.76%)</b></td><td>0.00 (-15.11%)</td><td>0.00 (+4.01%)</td><td>578.40 (+17.80%)</td><td>390.84 (+12.30%)</td><td>358.90 <b>(+27.81%)</b></td><td>239.10 (-1.12%)</td><td>139.90 (+18.67%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.00 (n/a)</td><td>348.02 (n/a)</td><td>280.80 (n/a)</td><td>241.80 (n/a)</td><td>117.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (+4.75%)</td><td>0.01 (+7.72%)</td><td>0.01 (-10.27%)</td><td>0.00 (-10.97%)</td><td>0.00 <b>(+23.41%)</b></td><td>631.30 (+12.31%)</td><td>456.34 (-0.02%)</td><td>521.50 (+11.43%)</td><td>220.00 (-4.56%)</td><td>191.70 <b>(+42.74%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>562.10 (n/a)</td><td>456.44 (n/a)</td><td>468.00 (n/a)</td><td>230.50 (n/a)</td><td>134.30 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (-3.82%)</td><td>0.01 (+7.05%)</td><td>0.01 <b>(+31.77%)</b></td><td>0.00 (+8.75%)</td><td>0.00 (-6.78%)</td><td>532.90 (-8.04%)</td><td>391.24 (-7.35%)</td><td>325.60 <b>(-24.10%)</b></td><td>267.80 (+3.96%)</td><td>120.82 (-5.48%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>579.50 (n/a)</td><td>422.26 (n/a)</td><td>429.00 (n/a)</td><td>257.60 (n/a)</td><td>127.83 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (-3.82%)</td><td>0.01 (-15.46%)</td><td>0.01 (+8.05%)</td><td>0.00 <b>(-74.48%)</b></td><td>0.01 <b>(+34.64%)</b></td><td>2005.80 <b>(+291.91%)</b></td><td>718.82 <b>(+80.55%)</b></td><td>440.00 (-7.47%)</td><td>270.20 (+3.96%)</td><td>731.48 <b>(+477.24%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>511.80 (n/a)</td><td>398.12 (n/a)</td><td>475.50 (n/a)</td><td>259.90 (n/a)</td><td>126.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (+18.78%)</td><td>0.02 (+18.99%)</td><td>0.02 <b>(+65.80%)</b></td><td>0.01 (+7.32%)</td><td>0.01 (+3.89%)</td><td>566.80 (-6.82%)</td><td>370.42 (-16.81%)</td><td>296.40 <b>(-39.69%)</b></td><td>237.00 (-15.81%)</td><td>137.00 (-11.60%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.30 (n/a)</td><td>445.28 (n/a)</td><td>491.50 (n/a)</td><td>281.50 (n/a)</td><td>154.98 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(+24.31%)</b></td><td>0.02 (+18.00%)</td><td>0.01 (-0.30%)</td><td>0.01 <b>(+37.30%)</b></td><td>0.01 <b>(+29.34%)</b></td><td>570.60 <b>(-27.16%)</b></td><td>373.52 (-16.00%)</td><td>401.30 (+0.30%)</td><td>227.10 (-19.55%)</td><td>142.13 <b>(-29.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>783.40 (n/a)</td><td>444.66 (n/a)</td><td>400.10 (n/a)</td><td>282.30 (n/a)</td><td>201.67 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(+60.84%)</b></td><td>0.01 <b>(+64.51%)</b></td><td>0.01 <b>(+35.81%)</b></td><td>0.01 <b>(+208.88%)</b></td><td>0.01 <b>(+31.19%)</b></td><td>591.40 <b>(-67.62%)</b></td><td>406.80 <b>(-49.35%)</b></td><td>390.90 <b>(-26.37%)</b></td><td>242.20 <b>(-37.82%)</b></td><td>148.36 <b>(-74.92%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1826.70 (n/a)</td><td>803.16 (n/a)</td><td>530.90 (n/a)</td><td>389.50 (n/a)</td><td>591.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (-5.23%)</td><td>0.01 (-16.84%)</td><td>0.01 <b>(-33.11%)</b></td><td>0.01 (-17.18%)</td><td>0.01 <b>(+39.83%)</b></td><td>633.00 <b>(+20.76%)</b></td><td>434.48 <b>(+32.00%)</b></td><td>426.30 <b>(+49.47%)</b></td><td>245.80 (+5.49%)</td><td>189.35 <b>(+65.71%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.20 (n/a)</td><td>329.16 (n/a)</td><td>285.20 (n/a)</td><td>233.00 (n/a)</td><td>114.27 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(-27.33%)</b></td><td>0.01 <b>(-22.63%)</b></td><td>0.01 (-7.15%)</td><td>0.01 <b>(-46.56%)</b></td><td>0.00 (-9.83%)</td><td>975.00 <b>(+87.14%)</b></td><td>600.96 <b>(+41.14%)</b></td><td>475.40 (+7.70%)</td><td>330.00 <b>(+37.61%)</b></td><td>279.69 <b>(+147.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.00 (n/a)</td><td>425.80 (n/a)</td><td>441.40 (n/a)</td><td>239.80 (n/a)</td><td>112.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (-11.01%)</td><td>0.04 <b>(+24.40%)</b></td><td>0.04 <b>(+77.60%)</b></td><td>0.03 <b>(+59.57%)</b></td><td>0.01 <b>(-57.39%)</b></td><td>375.20 <b>(-37.34%)</b></td><td>281.34 <b>(-31.35%)</b></td><td>261.70 <b>(-43.70%)</b></td><td>236.70 (+12.34%)</td><td>55.82 <b>(-68.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>598.80 (n/a)</td><td>409.84 (n/a)</td><td>464.80 (n/a)</td><td>210.70 (n/a)</td><td>177.39 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 <b>(-26.43%)</b></td><td>0.03 (+3.60%)</td><td>0.02 (+7.36%)</td><td>0.02 <b>(+22.33%)</b></td><td>0.01 <b>(-46.57%)</b></td><td>477.00 (-18.25%)</td><td>385.04 (-12.98%)</td><td>429.00 (-6.86%)</td><td>259.80 <b>(+35.88%)</b></td><td>97.85 <b>(-37.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>583.50 (n/a)</td><td>442.48 (n/a)</td><td>460.60 (n/a)</td><td>191.20 (n/a)</td><td>156.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (-11.57%)</td><td>0.03 (-6.54%)</td><td>0.03 (+8.71%)</td><td>0.02 (+6.13%)</td><td>0.01 <b>(-24.50%)</b></td><td>553.50 (-5.77%)</td><td>387.52 (+2.01%)</td><td>306.70 (-8.01%)</td><td>256.50 (+13.10%)</td><td>137.68 (-14.76%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>587.40 (n/a)</td><td>379.90 (n/a)</td><td>333.40 (n/a)</td><td>226.80 (n/a)</td><td>161.52 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (+7.22%)</td><td>0.03 (-7.20%)</td><td>0.03 <b>(-25.20%)</b></td><td>0.02 (+5.15%)</td><td>0.01 (+0.08%)</td><td>572.00 (-4.90%)</td><td>383.20 (+5.22%)</td><td>401.50 <b>(+33.70%)</b></td><td>194.70 (-6.75%)</td><td>143.61 (-14.19%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.50 (n/a)</td><td>364.18 (n/a)</td><td>300.30 (n/a)</td><td>208.80 (n/a)</td><td>167.34 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (-17.35%)</td><td>0.03 (-18.41%)</td><td>0.02 <b>(-33.51%)</b></td><td>0.02 (-10.64%)</td><td>0.01 <b>(-30.00%)</b></td><td>583.40 (+11.89%)</td><td>425.20 (+18.18%)</td><td>461.00 <b>(+50.41%)</b></td><td>295.30 <b>(+21.02%)</b></td><td>120.24 (-8.81%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.40 (n/a)</td><td>359.78 (n/a)</td><td>306.50 (n/a)</td><td>244.00 (n/a)</td><td>131.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-19.76%)</td><td>0.02 (+8.51%)</td><td>0.02 <b>(+22.29%)</b></td><td>0.02 (+18.41%)</td><td>0.00 <b>(-49.73%)</b></td><td>543.40 (-15.56%)</td><td>460.46 (-12.42%)</td><td>471.20 (-18.22%)</td><td>383.70 <b>(+24.62%)</b></td><td>71.58 <b>(-46.42%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>643.50 (n/a)</td><td>525.78 (n/a)</td><td>576.20 (n/a)</td><td>307.90 (n/a)</td><td>133.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (+1.22%)</td><td>0.07 (+4.14%)</td><td>0.07 (+1.27%)</td><td>0.04 (+6.21%)</td><td>0.02 (-10.68%)</td><td>518.90 (-5.84%)</td><td>351.14 (-7.06%)</td><td>282.90 (-1.26%)</td><td>244.70 (-1.21%)</td><td>120.04 (-19.89%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>551.10 (n/a)</td><td>377.80 (n/a)</td><td>286.50 (n/a)</td><td>247.70 (n/a)</td><td>149.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (+13.83%)</td><td>0.07 (+3.74%)</td><td>0.07 (-3.50%)</td><td>0.05 <b>(+28.83%)</b></td><td>0.02 (-2.59%)</td><td>408.60 <b>(-22.38%)</b></td><td>306.30 (-6.27%)</td><td>295.00 (+3.62%)</td><td>215.20 (-12.13%)</td><td>72.23 <b>(-36.87%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>526.40 (n/a)</td><td>326.78 (n/a)</td><td>284.70 (n/a)</td><td>244.90 (n/a)</td><td>114.41 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (-3.60%)</td><td>0.06 (-5.29%)</td><td>0.08 (-4.14%)</td><td>0.03 (-18.72%)</td><td>0.02 (+4.28%)</td><td>611.20 <b>(+23.05%)</b></td><td>373.50 (+9.04%)</td><td>266.70 (+4.34%)</td><td>239.80 (+3.72%)</td><td>167.54 <b>(+26.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>496.70 (n/a)</td><td>342.54 (n/a)</td><td>255.60 (n/a)</td><td>231.20 (n/a)</td><td>132.17 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (+4.59%)</td><td>0.07 (+19.13%)</td><td>0.07 <b>(+47.15%)</b></td><td>0.04 (-1.84%)</td><td>0.02 <b>(+29.75%)</b></td><td>532.70 (+1.87%)</td><td>352.36 (-12.70%)</td><td>283.60 <b>(-32.04%)</b></td><td>244.70 (-4.38%)</td><td>127.63 <b>(+31.81%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>522.90 (n/a)</td><td>403.64 (n/a)</td><td>417.30 (n/a)</td><td>255.90 (n/a)</td><td>96.83 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 <b>(+33.81%)</b></td><td>0.07 (-5.40%)</td><td>0.07 (-12.17%)</td><td>0.03 <b>(-20.17%)</b></td><td>0.03 <b>(+78.91%)</b></td><td>650.60 <b>(+25.26%)</b></td><td>385.16 (+17.81%)</td><td>313.00 (+13.86%)</td><td>188.20 <b>(-25.29%)</b></td><td>180.03 <b>(+63.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>519.40 (n/a)</td><td>326.92 (n/a)</td><td>274.90 (n/a)</td><td>251.90 (n/a)</td><td>110.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (+0.76%)</td><td>0.06 (+13.01%)</td><td>0.06 <b>(+27.04%)</b></td><td>0.03 <b>(-22.40%)</b></td><td>0.02 (+6.02%)</td><td>819.00 <b>(+28.85%)</b></td><td>434.42 (-7.11%)</td><td>362.70 <b>(-21.29%)</b></td><td>239.70 (-0.75%)</td><td>228.74 <b>(+37.89%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>635.60 (n/a)</td><td>467.66 (n/a)</td><td>460.80 (n/a)</td><td>241.50 (n/a)</td><td>165.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>335.30 (n/a)</td><td>268.72 (n/a)</td><td>263.80 (n/a)</td><td>232.90 (n/a)</td><td>39.67 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.20 (n/a)</td><td>346.12 (n/a)</td><td>305.70 (n/a)</td><td>270.40 (n/a)</td><td>108.69 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.20 (n/a)</td><td>355.78 (n/a)</td><td>308.90 (n/a)</td><td>266.50 (n/a)</td><td>139.40 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>713.60 (n/a)</td><td>368.04 (n/a)</td><td>238.20 (n/a)</td><td>197.50 (n/a)</td><td>219.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.10 (n/a)</td><td>339.66 (n/a)</td><td>270.80 (n/a)</td><td>263.50 (n/a)</td><td>100.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.60 (n/a)</td><td>327.80 (n/a)</td><td>291.30 (n/a)</td><td>215.00 (n/a)</td><td>113.40 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>504.90 (n/a)</td><td>371.14 (n/a)</td><td>380.00 (n/a)</td><td>236.00 (n/a)</td><td>98.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>549.50 (n/a)</td><td>376.12 (n/a)</td><td>396.30 (n/a)</td><td>237.50 (n/a)</td><td>135.57 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>593.20 (n/a)</td><td>372.18 (n/a)</td><td>305.20 (n/a)</td><td>241.40 (n/a)</td><td>141.16 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.20 (-5.21%)</td><td>0.16 (+18.20%)</td><td>0.18 <b>(+54.45%)</b></td><td>0.09 <b>(+29.16%)</b></td><td>0.04 <b>(-29.67%)</b></td><td>518.40 <b>(-22.58%)</b></td><td>323.76 <b>(-22.08%)</b></td><td>280.80 <b>(-35.25%)</b></td><td>246.40 (+5.52%)</td><td>112.36 <b>(-37.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>669.60 (n/a)</td><td>415.52 (n/a)</td><td>433.70 (n/a)</td><td>233.50 (n/a)</td><td>179.26 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>603.30 (n/a)</td><td>372.48 (n/a)</td><td>247.30 (n/a)</td><td>234.30 (n/a)</td><td>184.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>632.00 (n/a)</td><td>398.46 (n/a)</td><td>356.40 (n/a)</td><td>246.00 (n/a)</td><td>153.93 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.10 (n/a)</td><td>434.62 (n/a)</td><td>491.80 (n/a)</td><td>285.00 (n/a)</td><td>115.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.30 (n/a)</td><td>374.32 (n/a)</td><td>315.30 (n/a)</td><td>231.20 (n/a)</td><td>143.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>780.70 (n/a)</td><td>487.00 (n/a)</td><td>476.80 (n/a)</td><td>209.00 (n/a)</td><td>218.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.90 (n/a)</td><td>345.46 (n/a)</td><td>306.90 (n/a)</td><td>245.10 (n/a)</td><td>114.62 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2047.70 (n/a)</td><td>710.46 (n/a)</td><td>425.00 (n/a)</td><td>225.30 (n/a)</td><td>755.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1154.60 (n/a)</td><td>650.08 (n/a)</td><td>597.10 (n/a)</td><td>393.70 (n/a)</td><td>296.08 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>437.10 (n/a)</td><td>337.52 (n/a)</td><td>324.00 (n/a)</td><td>265.30 (n/a)</td><td>65.41 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>563.80 (n/a)</td><td>385.16 (n/a)</td><td>289.30 (n/a)</td><td>242.30 (n/a)</td><td>160.75 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>625.90 (n/a)</td><td>495.16 (n/a)</td><td>547.40 (n/a)</td><td>248.90 (n/a)</td><td>144.81 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>391.10 (n/a)</td><td>324.70 (n/a)</td><td>380.00 (n/a)</td><td>231.00 (n/a)</td><td>85.32 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>632.20 (n/a)</td><td>445.62 (n/a)</td><td>458.40 (n/a)</td><td>234.50 (n/a)</td><td>182.13 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>503.70 (n/a)</td><td>315.14 (n/a)</td><td>291.10 (n/a)</td><td>236.50 (n/a)</td><td>110.14 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.80 (n/a)</td><td>389.68 (n/a)</td><td>386.30 (n/a)</td><td>196.10 (n/a)</td><td>165.25 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.10 (n/a)</td><td>326.40 (n/a)</td><td>259.70 (n/a)</td><td>212.20 (n/a)</td><td>161.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>379.70 (n/a)</td><td>286.42 (n/a)</td><td>291.40 (n/a)</td><td>205.70 (n/a)</td><td>63.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.00 (n/a)</td><td>366.80 (n/a)</td><td>340.70 (n/a)</td><td>242.60 (n/a)</td><td>131.34 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>460.80 (n/a)</td><td>339.08 (n/a)</td><td>314.20 (n/a)</td><td>232.00 (n/a)</td><td>108.34 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2028.80 (n/a)</td><td>709.22 (n/a)</td><td>405.90 (n/a)</td><td>246.30 (n/a)</td><td>747.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.00 (n/a)</td><td>361.70 (n/a)</td><td>286.20 (n/a)</td><td>253.20 (n/a)</td><td>135.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.60 (n/a)</td><td>395.68 (n/a)</td><td>461.80 (n/a)</td><td>242.10 (n/a)</td><td>124.26 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.20 (n/a)</td><td>489.38 (n/a)</td><td>466.30 (n/a)</td><td>289.40 (n/a)</td><td>137.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>727.00 (n/a)</td><td>464.12 (n/a)</td><td>458.30 (n/a)</td><td>278.40 (n/a)</td><td>164.44 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2189.60 (n/a)</td><td>793.50 (n/a)</td><td>480.60 (n/a)</td><td>218.50 (n/a)</td><td>793.55 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>643.40 (n/a)</td><td>424.86 (n/a)</td><td>395.70 (n/a)</td><td>276.90 (n/a)</td><td>158.79 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>617.10 (n/a)</td><td>432.82 (n/a)</td><td>435.80 (n/a)</td><td>264.10 (n/a)</td><td>160.04 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.00 (n/a)</td><td>493.68 (n/a)</td><td>568.50 (n/a)</td><td>246.90 (n/a)</td><td>142.86 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1052.00 (n/a)</td><td>594.38 (n/a)</td><td>560.00 (n/a)</td><td>362.30 (n/a)</td><td>274.10 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>402.50 (n/a)</td><td>282.72 (n/a)</td><td>301.20 (n/a)</td><td>171.40 (n/a)</td><td>97.43 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>781.70 (n/a)</td><td>489.64 (n/a)</td><td>534.60 (n/a)</td><td>253.00 (n/a)</td><td>212.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>658.20 (n/a)</td><td>380.74 (n/a)</td><td>313.40 (n/a)</td><td>271.10 (n/a)</td><td>158.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>470.70 (n/a)</td><td>327.00 (n/a)</td><td>318.60 (n/a)</td><td>235.40 (n/a)</td><td>87.58 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>575.60 (n/a)</td><td>435.30 (n/a)</td><td>448.80 (n/a)</td><td>279.30 (n/a)</td><td>126.61 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1034.90 (n/a)</td><td>640.08 (n/a)</td><td>616.50 (n/a)</td><td>299.00 (n/a)</td><td>275.07 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>583.40 (n/a)</td><td>414.58 (n/a)</td><td>374.90 (n/a)</td><td>231.40 (n/a)</td><td>146.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.53 (-2.89%)</td><td>0.41 (-18.43%)</td><td>0.40 <b>(-20.96%)</b></td><td>0.33 <b>(-29.97%)</b></td><td>0.07 <b>(+103.04%)</b></td><td>678.00 <b>(+42.80%)</b></td><td>549.74 <b>(+24.98%)</b></td><td>547.90 <b>(+26.51%)</b></td><td>419.60 (+2.97%)</td><td>91.63 <b>(+191.90%)</b></td><td>22.49 (-2.89%)</td><td>17.57 (-18.43%)</td><td>17.22 <b>(-20.96%)</b></td><td>13.92 <b>(-29.97%)</b></td><td>3.09 <b>(+103.04%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.54 (n/a)</td><td>0.50 (n/a)</td><td>0.51 (n/a)</td><td>0.47 (n/a)</td><td>0.04 (n/a)</td><td>474.80 (n/a)</td><td>439.86 (n/a)</td><td>433.10 (n/a)</td><td>407.50 (n/a)</td><td>31.39 (n/a)</td><td>23.16 (n/a)</td><td>21.54 (n/a)</td><td>21.79 (n/a)</td><td>19.88 (n/a)</td><td>1.52 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.52 (-15.60%)</td><td>0.41 (-3.17%)</td><td>0.45 (-14.44%)</td><td>0.16 <b>(+27.61%)</b></td><td>0.14 <b>(-30.25%)</b></td><td>1397.70 <b>(-21.64%)</b></td><td>657.00 (-11.52%)</td><td>493.10 (+16.88%)</td><td>428.20 (+18.48%)</td><td>414.95 <b>(-31.01%)</b></td><td>22.04 (-15.60%)</td><td>17.41 (-3.17%)</td><td>19.14 (-14.44%)</td><td>6.75 <b>(+27.61%)</b></td><td>6.08 <b>(-30.25%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.61 (n/a)</td><td>0.42 (n/a)</td><td>0.52 (n/a)</td><td>0.12 (n/a)</td><td>0.20 (n/a)</td><td>1783.60 (n/a)</td><td>742.56 (n/a)</td><td>421.90 (n/a)</td><td>361.40 (n/a)</td><td>601.46 (n/a)</td><td>26.11 (n/a)</td><td>17.98 (n/a)</td><td>22.37 (n/a)</td><td>5.29 (n/a)</td><td>8.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.31 (-0.46%)</td><td>0.30 (-1.41%)</td><td>0.30 (-1.90%)</td><td>0.29 (-0.90%)</td><td>0.01 <b>(+30.19%)</b></td><td>85799.70 (+0.91%)</td><td>84188.60 (+1.44%)</td><td>84511.00 (+1.93%)</td><td>82116.10 (+0.46%)</td><td>1644.72 <b>(+31.83%)</b></td><td>209.21 (-0.46%)</td><td>204.13 (-1.41%)</td><td>203.29 (-1.90%)</td><td>200.23 (-0.90%)</td><td>4.01 <b>(+30.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>85027.90 (n/a)</td><td>82993.30 (n/a)</td><td>82909.30 (n/a)</td><td>81738.10 (n/a)</td><td>1247.57 (n/a)</td><td>210.18 (n/a)</td><td>207.04 (n/a)</td><td>207.21 (n/a)</td><td>202.05 (n/a)</td><td>3.08 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>1.03 (-0.05%)</td><td>1.01 (-1.23%)</td><td>1.02 (-0.40%)</td><td>0.98 (-3.51%)</td><td>0.02 <b>(+196.55%)</b></td><td>25685.20 (+3.64%)</td><td>24852.84 (+1.27%)</td><td>24649.50 (+0.40%)</td><td>24389.60 (+0.05%)</td><td>511.12 <b>(+208.39%)</b></td><td>704.39 (-0.05%)</td><td>691.49 (-1.23%)</td><td>696.97 (-0.40%)</td><td>668.86 (-3.51%)</td><td>13.98 <b>(+196.55%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.03 (n/a)</td><td>1.03 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.01 (n/a)</td><td>24784.00 (n/a)</td><td>24540.20 (n/a)</td><td>24550.10 (n/a)</td><td>24378.60 (n/a)</td><td>165.73 (n/a)</td><td>704.71 (n/a)</td><td>700.10 (n/a)</td><td>699.79 (n/a)</td><td>693.18 (n/a)</td><td>4.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.82 (+0.71%)</td><td>0.81 (+1.21%)</td><td>0.81 (+1.07%)</td><td>0.81 (+2.17%)</td><td>0.01 <b>(-27.62%)</b></td><td>93772.70 (-2.13%)</td><td>93009.86 (-1.21%)</td><td>93171.30 (-1.06%)</td><td>91787.60 (-0.71%)</td><td>842.06 <b>(-29.57%)</b></td><td>748.68 (+0.71%)</td><td>738.89 (+1.21%)</td><td>737.56 (+1.07%)</td><td>732.83 (+2.17%)</td><td>6.72 <b>(-27.62%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95808.90 (n/a)</td><td>94144.46 (n/a)</td><td>94165.40 (n/a)</td><td>92440.30 (n/a)</td><td>1195.61 (n/a)</td><td>743.39 (n/a)</td><td>730.03 (n/a)</td><td>729.77 (n/a)</td><td>717.26 (n/a)</td><td>9.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.77 (+0.57%)</td><td>0.77 (+0.88%)</td><td>0.77 (+0.83%)</td><td>0.76 (+0.97%)</td><td>0.01 (-16.97%)</td><td>99314.50 (-0.96%)</td><td>98161.70 (-0.87%)</td><td>98090.70 (-0.82%)</td><td>97620.10 (-0.57%)</td><td>686.86 (-18.20%)</td><td>703.95 (+0.57%)</td><td>700.09 (+0.88%)</td><td>700.57 (+0.83%)</td><td>691.94 (+0.97%)</td><td>4.87 (-16.97%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100276.40 (n/a)</td><td>99025.54 (n/a)</td><td>98900.50 (n/a)</td><td>98180.90 (n/a)</td><td>839.70 (n/a)</td><td>699.93 (n/a)</td><td>694.00 (n/a)</td><td>694.83 (n/a)</td><td>685.30 (n/a)</td><td>5.86 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.80 (+0.80%)</td><td>0.80 (+1.51%)</td><td>0.80 (+1.62%)</td><td>0.80 (+1.87%)</td><td>0.00 <b>(-72.76%)</b></td><td>94538.80 (-1.83%)</td><td>94346.14 (-1.49%)</td><td>94353.10 (-1.59%)</td><td>94173.10 (-0.79%)</td><td>135.47 <b>(-73.44%)</b></td><td>729.71 (+0.80%)</td><td>728.38 (+1.51%)</td><td>728.32 (+1.62%)</td><td>726.89 (+1.87%)</td><td>1.05 <b>(-72.76%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96304.70 (n/a)</td><td>95772.16 (n/a)</td><td>95882.30 (n/a)</td><td>94923.30 (n/a)</td><td>510.03 (n/a)</td><td>723.95 (n/a)</td><td>717.55 (n/a)</td><td>716.71 (n/a)</td><td>713.56 (n/a)</td><td>3.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.44 (-1.46%)</td><td>3.48 <b>(-21.37%)</b></td><td>3.63 (-19.72%)</td><td>2.15 <b>(-23.31%)</b></td><td>1.37 <b>(+23.04%)</b></td><td>4143.40 <b>(+30.39%)</b></td><td>2908.76 <b>(+35.79%)</b></td><td>2454.60 <b>(+24.57%)</b></td><td>1638.40 (+1.48%)</td><td>1128.91 <b>(+77.03%)</b></td><td>327.67 (-1.46%)</td><td>209.38 <b>(-21.37%)</b></td><td>218.72 (-19.72%)</td><td>129.57 <b>(-23.31%)</b></td><td>82.53 <b>(+23.04%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.52 (n/a)</td><td>4.42 (n/a)</td><td>4.52 (n/a)</td><td>2.80 (n/a)</td><td>1.11 (n/a)</td><td>3177.70 (n/a)</td><td>2142.16 (n/a)</td><td>1970.50 (n/a)</td><td>1614.50 (n/a)</td><td>637.68 (n/a)</td><td>332.54 (n/a)</td><td>266.29 (n/a)</td><td>272.45 (n/a)</td><td>168.95 (n/a)</td><td>67.07 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>4.87 (+7.68%)</td><td>3.21 (+3.64%)</td><td>2.86 (-1.71%)</td><td>2.20 (-1.84%)</td><td>1.01 (+17.83%)</td><td>4044.30 (+1.87%)</td><td>2974.84 (-1.98%)</td><td>3112.30 (+1.74%)</td><td>1830.40 (-7.13%)</td><td>812.90 (+11.56%)</td><td>293.31 (+7.68%)</td><td>193.38 (+3.64%)</td><td>172.50 (-1.71%)</td><td>132.75 (-1.84%)</td><td>61.09 (+17.83%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.52 (n/a)</td><td>3.10 (n/a)</td><td>2.91 (n/a)</td><td>2.25 (n/a)</td><td>0.86 (n/a)</td><td>3970.00 (n/a)</td><td>3035.08 (n/a)</td><td>3059.00 (n/a)</td><td>1971.00 (n/a)</td><td>728.65 (n/a)</td><td>272.39 (n/a)</td><td>186.58 (n/a)</td><td>175.51 (n/a)</td><td>135.23 (n/a)</td><td>51.85 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.63 (+9.00%)</td><td>3.37 (-2.25%)</td><td>2.87 <b>(-22.42%)</b></td><td>1.97 (+1.74%)</td><td>1.53 (+14.35%)</td><td>4535.30 (-1.71%)</td><td>3080.50 (+4.16%)</td><td>3106.90 <b>(+28.91%)</b></td><td>1582.60 (-8.26%)</td><td>1249.06 (+0.86%)</td><td>339.24 (+9.00%)</td><td>203.20 (-2.25%)</td><td>172.80 <b>(-22.42%)</b></td><td>118.38 (+1.74%)</td><td>92.42 (+14.35%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.17 (n/a)</td><td>3.45 (n/a)</td><td>3.70 (n/a)</td><td>1.93 (n/a)</td><td>1.34 (n/a)</td><td>4614.30 (n/a)</td><td>2957.38 (n/a)</td><td>2410.20 (n/a)</td><td>1725.00 (n/a)</td><td>1238.42 (n/a)</td><td>311.23 (n/a)</td><td>207.88 (n/a)</td><td>222.75 (n/a)</td><td>116.35 (n/a)</td><td>80.82 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>6.77 (+13.60%)</td><td>5.67 (+3.67%)</td><td>6.34 (+14.12%)</td><td>4.11 (-13.11%)</td><td>1.17 <b>(+125.59%)</b></td><td>8481.50 (+15.08%)</td><td>6382.80 (-0.56%)</td><td>5495.30 (-12.38%)</td><td>5147.30 (-11.97%)</td><td>1453.07 <b>(+129.06%)</b></td><td>417.21 (+13.60%)</td><td>349.46 (+3.67%)</td><td>390.78 (+14.12%)</td><td>253.20 (-13.11%)</td><td>71.79 <b>(+125.59%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.96 (n/a)</td><td>5.47 (n/a)</td><td>5.56 (n/a)</td><td>4.73 (n/a)</td><td>0.52 (n/a)</td><td>7369.90 (n/a)</td><td>6418.48 (n/a)</td><td>6271.40 (n/a)</td><td>5847.20 (n/a)</td><td>634.35 (n/a)</td><td>367.27 (n/a)</td><td>337.09 (n/a)</td><td>342.43 (n/a)</td><td>291.39 (n/a)</td><td>31.82 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.86 (+9.82%)</td><td>4.72 (-1.05%)</td><td>4.58 (+0.12%)</td><td>4.23 (-1.62%)</td><td>0.67 <b>(+48.74%)</b></td><td>8238.60 (+1.65%)</td><td>7485.68 (+1.79%)</td><td>7619.80 (-0.12%)</td><td>5948.70 (-8.94%)</td><td>933.63 <b>(+38.00%)</b></td><td>361.00 (+9.82%)</td><td>290.97 (-1.05%)</td><td>281.83 (+0.12%)</td><td>260.66 (-1.62%)</td><td>41.18 <b>(+48.74%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.34 (n/a)</td><td>4.77 (n/a)</td><td>4.57 (n/a)</td><td>4.30 (n/a)</td><td>0.45 (n/a)</td><td>8105.20 (n/a)</td><td>7353.90 (n/a)</td><td>7628.60 (n/a)</td><td>6532.90 (n/a)</td><td>676.57 (n/a)</td><td>328.72 (n/a)</td><td>294.06 (n/a)</td><td>281.51 (n/a)</td><td>264.95 (n/a)</td><td>27.68 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.81 (-12.16%)</td><td>5.14 (-16.56%)</td><td>4.90 <b>(-20.44%)</b></td><td>4.83 (-15.18%)</td><td>0.42 <b>(+26.40%)</b></td><td>7215.90 (+17.90%)</td><td>6812.40 <b>(+20.16%)</b></td><td>7120.30 <b>(+25.70%)</b></td><td>5998.40 (+13.84%)</td><td>518.99 <b>(+69.71%)</b></td><td>358.01 (-12.16%)</td><td>316.80 (-16.56%)</td><td>301.60 <b>(-20.44%)</b></td><td>297.60 (-15.18%)</td><td>25.68 <b>(+26.40%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>6.62 (n/a)</td><td>6.16 (n/a)</td><td>6.15 (n/a)</td><td>5.70 (n/a)</td><td>0.33 (n/a)</td><td>6120.40 (n/a)</td><td>5669.28 (n/a)</td><td>5664.70 (n/a)</td><td>5269.10 (n/a)</td><td>305.81 (n/a)</td><td>407.56 (n/a)</td><td>379.67 (n/a)</td><td>379.10 (n/a)</td><td>350.87 (n/a)</td><td>20.32 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.77 (-2.02%)</td><td>0.76 (-1.00%)</td><td>0.76 (-0.65%)</td><td>0.75 (-1.15%)</td><td>0.01 <b>(-21.53%)</b></td><td>100884.80 (+1.16%)</td><td>99105.74 (+1.00%)</td><td>99351.00 (+0.65%)</td><td>97512.10 (+2.07%)</td><td>1350.16 (-18.97%)</td><td>704.73 (-2.02%)</td><td>693.50 (-1.00%)</td><td>691.68 (-0.65%)</td><td>681.17 (-1.15%)</td><td>9.44 <b>(-21.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99727.40 (n/a)</td><td>98127.68 (n/a)</td><td>98706.40 (n/a)</td><td>95539.10 (n/a)</td><td>1666.34 (n/a)</td><td>719.28 (n/a)</td><td>700.47 (n/a)</td><td>696.20 (n/a)</td><td>689.07 (n/a)</td><td>12.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.76 (-2.41%)</td><td>0.75 (-2.18%)</td><td>0.76 (-2.24%)</td><td>0.73 (-1.48%)</td><td>0.01 (-17.12%)</td><td>103939.70 (+1.51%)</td><td>101162.94 (+2.21%)</td><td>99960.30 (+2.29%)</td><td>99270.40 (+2.47%)</td><td>2044.06 (-13.74%)</td><td>692.25 (-2.41%)</td><td>679.51 (-2.18%)</td><td>687.47 (-2.24%)</td><td>661.15 (-1.48%)</td><td>13.61 (-17.12%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>102398.20 (n/a)</td><td>98972.66 (n/a)</td><td>97722.00 (n/a)</td><td>96881.40 (n/a)</td><td>2369.61 (n/a)</td><td>709.32 (n/a)</td><td>694.64 (n/a)</td><td>703.21 (n/a)</td><td>671.10 (n/a)</td><td>16.42 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.81 (-0.32%)</td><td>0.80 (-0.62%)</td><td>0.80 (-1.00%)</td><td>0.80 (-0.50%)</td><td>0.00 (+19.83%)</td><td>94798.10 (+0.51%)</td><td>94422.34 (+0.62%)</td><td>94736.00 (+1.01%)</td><td>93594.10 (+0.32%)</td><td>524.48 <b>(+20.83%)</b></td><td>734.23 (-0.32%)</td><td>727.81 (-0.62%)</td><td>725.38 (-1.00%)</td><td>724.90 (-0.50%)</td><td>4.06 (+19.83%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94321.10 (n/a)</td><td>93838.64 (n/a)</td><td>93787.20 (n/a)</td><td>93291.70 (n/a)</td><td>434.08 (n/a)</td><td>736.61 (n/a)</td><td>732.33 (n/a)</td><td>732.72 (n/a)</td><td>728.57 (n/a)</td><td>3.39 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.91 (+0.92%)</td><td>2.64 (-10.63%)</td><td>2.54 <b>(-27.93%)</b></td><td>1.41 (-14.24%)</td><td>1.02 (-8.71%)</td><td>5699.50 (+16.61%)</td><td>3494.68 (+10.98%)</td><td>3179.60 <b>(+38.75%)</b></td><td>2059.40 (-0.91%)</td><td>1470.99 (+6.58%)</td><td>1026.47 (+0.92%)</td><td>691.22 (-10.63%)</td><td>664.83 <b>(-27.93%)</b></td><td>370.90 (-14.24%)</td><td>267.13 (-8.71%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.88 (n/a)</td><td>2.95 (n/a)</td><td>3.52 (n/a)</td><td>1.65 (n/a)</td><td>1.12 (n/a)</td><td>4887.60 (n/a)</td><td>3148.88 (n/a)</td><td>2291.60 (n/a)</td><td>2078.30 (n/a)</td><td>1380.18 (n/a)</td><td>1017.14 (n/a)</td><td>773.46 (n/a)</td><td>922.47 (n/a)</td><td>432.51 (n/a)</td><td>292.61 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.28 (+9.17%)</td><td>0.21 (+1.37%)</td><td>0.20 (-3.74%)</td><td>0.18 (+9.42%)</td><td>0.04 (+15.01%)</td><td>6734.80 (-8.61%)</td><td>6010.30 (-1.19%)</td><td>6183.90 (+3.88%)</td><td>4445.50 (-8.40%)</td><td>908.08 (-6.61%)</td><td>15.10 (+9.17%)</td><td>11.42 (+1.37%)</td><td>10.85 (-3.74%)</td><td>9.96 (+9.42%)</td><td>2.09 (+15.01%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>7369.40 (n/a)</td><td>6082.82 (n/a)</td><td>5952.80 (n/a)</td><td>4853.10 (n/a)</td><td>972.37 (n/a)</td><td>13.83 (n/a)</td><td>11.26 (n/a)</td><td>11.27 (n/a)</td><td>9.11 (n/a)</td><td>1.82 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (+11.51%)</td><td>0.12 <b>(+37.30%)</b></td><td>0.13 <b>(+69.60%)</b></td><td>0.10 <b>(+93.40%)</b></td><td>0.02 <b>(-46.74%)</b></td><td>0.15 (+11.51%)</td><td>0.12 <b>(+37.30%)</b></td><td>0.12 <b>(+69.60%)</b></td><td>0.10 <b>(+93.40%)</b></td><td>0.02 <b>(-46.74%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.98 (+5.12%)</td><td>3.76 (+4.48%)</td><td>3.74 (+4.95%)</td><td>3.60 (+4.26%)</td><td>0.14 (+5.44%)</td><td>3.97 (+5.12%)</td><td>3.76 (+4.48%)</td><td>3.73 (+4.95%)</td><td>3.60 (+4.26%)</td><td>0.14 (+5.44%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.78 (n/a)</td><td>3.60 (n/a)</td><td>3.56 (n/a)</td><td>3.45 (n/a)</td><td>0.13 (n/a)</td><td>3.78 (n/a)</td><td>3.60 (n/a)</td><td>3.56 (n/a)</td><td>3.45 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.61 (+3.05%)</td><td>6.87 (+8.53%)</td><td>6.92 (+5.16%)</td><td>6.13 (+18.36%)</td><td>0.72 <b>(-23.86%)</b></td><td>7.61 (+3.05%)</td><td>6.87 (+8.53%)</td><td>6.92 (+5.16%)</td><td>6.13 (+18.36%)</td><td>0.72 <b>(-23.86%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.39 (n/a)</td><td>6.33 (n/a)</td><td>6.58 (n/a)</td><td>5.18 (n/a)</td><td>0.95 (n/a)</td><td>7.38 (n/a)</td><td>6.33 (n/a)</td><td>6.58 (n/a)</td><td>5.18 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>14.09 (+1.40%)</td><td>10.86 (+3.84%)</td><td>10.43 (+7.39%)</td><td>8.15 <b>(+27.21%)</b></td><td>2.78 (-7.25%)</td><td>14.08 (+1.40%)</td><td>10.85 (+3.84%)</td><td>10.42 (+7.39%)</td><td>8.14 <b>(+27.21%)</b></td><td>2.78 (-7.25%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>13.90 (n/a)</td><td>10.46 (n/a)</td><td>9.71 (n/a)</td><td>6.41 (n/a)</td><td>3.00 (n/a)</td><td>13.89 (n/a)</td><td>10.45 (n/a)</td><td>9.71 (n/a)</td><td>6.40 (n/a)</td><td>3.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.72 (-3.09%)</td><td>3.53 (-5.05%)</td><td>3.44 (-8.14%)</td><td>3.38 (-6.21%)</td><td>0.17 <b>(+86.95%)</b></td><td>3.71 (-3.09%)</td><td>3.53 (-5.05%)</td><td>3.44 (-8.14%)</td><td>3.38 (-6.21%)</td><td>0.17 <b>(+86.95%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.83 (n/a)</td><td>3.72 (n/a)</td><td>3.75 (n/a)</td><td>3.60 (n/a)</td><td>0.09 (n/a)</td><td>3.83 (n/a)</td><td>3.72 (n/a)</td><td>3.75 (n/a)</td><td>3.60 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.14 (+3.18%)</td><td>6.19 (-2.36%)</td><td>6.52 (+1.31%)</td><td>4.71 (-18.21%)</td><td>0.93 <b>(+82.78%)</b></td><td>7.14 (+3.18%)</td><td>6.18 (-2.36%)</td><td>6.52 (+1.31%)</td><td>4.70 (-18.21%)</td><td>0.93 <b>(+82.78%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>6.92 (n/a)</td><td>6.34 (n/a)</td><td>6.44 (n/a)</td><td>5.75 (n/a)</td><td>0.51 (n/a)</td><td>6.92 (n/a)</td><td>6.33 (n/a)</td><td>6.44 (n/a)</td><td>5.75 (n/a)</td><td>0.51 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>13.91 (+0.81%)</td><td>11.60 (+17.38%)</td><td>12.01 <b>(+41.13%)</b></td><td>9.51 <b>(+33.38%)</b></td><td>1.77 <b>(-36.79%)</b></td><td>13.90 (+0.81%)</td><td>11.60 (+17.38%)</td><td>12.01 <b>(+41.13%)</b></td><td>9.51 <b>(+33.38%)</b></td><td>1.77 <b>(-36.79%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>13.80 (n/a)</td><td>9.88 (n/a)</td><td>8.51 (n/a)</td><td>7.13 (n/a)</td><td>2.80 (n/a)</td><td>13.79 (n/a)</td><td>9.88 (n/a)</td><td>8.51 (n/a)</td><td>7.13 (n/a)</td><td>2.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>733.20 (n/a)</td><td>473.02 (n/a)</td><td>484.90 (n/a)</td><td>284.10 (n/a)</td><td>177.44 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.70 (n/a)</td><td>387.20 (n/a)</td><td>367.30 (n/a)</td><td>181.20 (n/a)</td><td>164.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>635.70 (n/a)</td><td>361.30 (n/a)</td><td>295.60 (n/a)</td><td>207.20 (n/a)</td><td>167.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.20 (n/a)</td><td>371.60 (n/a)</td><td>311.80 (n/a)</td><td>243.00 (n/a)</td><td>136.81 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.40 (n/a)</td><td>435.64 (n/a)</td><td>420.40 (n/a)</td><td>200.90 (n/a)</td><td>156.45 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.60 (n/a)</td><td>410.30 (n/a)</td><td>438.00 (n/a)</td><td>263.30 (n/a)</td><td>102.42 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>722.90 (n/a)</td><td>428.62 (n/a)</td><td>449.00 (n/a)</td><td>219.40 (n/a)</td><td>207.07 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2423.30 (n/a)</td><td>800.48 (n/a)</td><td>518.20 (n/a)</td><td>231.20 (n/a)</td><td>919.00 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.70 (n/a)</td><td>363.54 (n/a)</td><td>291.70 (n/a)</td><td>244.50 (n/a)</td><td>128.07 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>803.90 (n/a)</td><td>489.48 (n/a)</td><td>452.40 (n/a)</td><td>311.60 (n/a)</td><td>195.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>516.10 (n/a)</td><td>429.42 (n/a)</td><td>458.30 (n/a)</td><td>294.00 (n/a)</td><td>84.01 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1408.20 (n/a)</td><td>632.24 (n/a)</td><td>453.70 (n/a)</td><td>336.30 (n/a)</td><td>438.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>515.10 (n/a)</td><td>359.78 (n/a)</td><td>332.20 (n/a)</td><td>283.50 (n/a)</td><td>93.86 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>826.60 (n/a)</td><td>507.30 (n/a)</td><td>484.20 (n/a)</td><td>278.90 (n/a)</td><td>199.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2045.80 (n/a)</td><td>725.58 (n/a)</td><td>472.20 (n/a)</td><td>299.20 (n/a)</td><td>744.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2390.90 (n/a)</td><td>772.02 (n/a)</td><td>393.30 (n/a)</td><td>234.90 (n/a)</td><td>909.13 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>569.30 (n/a)</td><td>397.54 (n/a)</td><td>473.30 (n/a)</td><td>158.40 (n/a)</td><td>163.61 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>541.80 (n/a)</td><td>415.96 (n/a)</td><td>501.90 (n/a)</td><td>219.50 (n/a)</td><td>142.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (+2.65%)</td><td>0.10 <b>(+40.99%)</b></td><td>0.10 <b>(+70.13%)</b></td><td>0.07 <b>(+45.11%)</b></td><td>0.02 <b>(-32.61%)</b></td><td>452.30 <b>(-31.09%)</b></td><td>333.10 <b>(-34.77%)</b></td><td>328.30 <b>(-41.22%)</b></td><td>236.30 (-2.60%)</td><td>77.64 <b>(-51.44%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>656.40 (n/a)</td><td>510.68 (n/a)</td><td>558.50 (n/a)</td><td>242.60 (n/a)</td><td>159.89 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>610.40 (n/a)</td><td>506.98 (n/a)</td><td>550.50 (n/a)</td><td>257.70 (n/a)</td><td>143.92 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>540.80 (n/a)</td><td>478.60 (n/a)</td><td>526.20 (n/a)</td><td>277.30 (n/a)</td><td>112.79 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>530.50 (n/a)</td><td>412.96 (n/a)</td><td>484.50 (n/a)</td><td>251.60 (n/a)</td><td>125.94 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>561.40 (n/a)</td><td>380.36 (n/a)</td><td>351.90 (n/a)</td><td>204.90 (n/a)</td><td>146.36 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>631.30 (n/a)</td><td>499.90 (n/a)</td><td>466.80 (n/a)</td><td>430.30 (n/a)</td><td>84.93 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (+16.44%)</td><td>0.01 (+16.43%)</td><td>0.01 <b>(+21.32%)</b></td><td>0.01 <b>(+21.38%)</b></td><td>0.00 (+10.32%)</td><td>427.10 (-17.61%)</td><td>351.78 (-14.72%)</td><td>387.70 (-17.56%)</td><td>238.00 (-14.14%)</td><td>84.65 <b>(-20.20%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.40 (n/a)</td><td>412.52 (n/a)</td><td>470.30 (n/a)</td><td>277.20 (n/a)</td><td>106.08 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (-6.38%)</td><td>0.01 (-18.24%)</td><td>0.01 (-2.61%)</td><td>0.01 <b>(-28.52%)</b></td><td>0.01 <b>(+20.92%)</b></td><td>530.00 <b>(+39.88%)</b></td><td>352.86 <b>(+31.73%)</b></td><td>276.10 (+2.68%)</td><td>209.70 (+6.77%)</td><td>145.39 <b>(+96.95%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>378.90 (n/a)</td><td>267.86 (n/a)</td><td>268.90 (n/a)</td><td>196.40 (n/a)</td><td>73.82 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (-18.24%)</td><td>0.01 <b>(-21.02%)</b></td><td>0.01 (-13.79%)</td><td>0.00 <b>(-43.76%)</b></td><td>0.00 (-6.19%)</td><td>827.50 <b>(+77.80%)</b></td><td>487.58 <b>(+35.34%)</b></td><td>488.90 (+15.99%)</td><td>269.60 <b>(+22.32%)</b></td><td>224.63 <b>(+93.53%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>465.40 (n/a)</td><td>360.26 (n/a)</td><td>421.50 (n/a)</td><td>220.40 (n/a)</td><td>116.07 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(-22.35%)</b></td><td>0.01 (-18.83%)</td><td>0.01 <b>(-23.96%)</b></td><td>0.01 (-12.24%)</td><td>0.00 <b>(-32.74%)</b></td><td>576.20 (+13.96%)</td><td>355.96 (+18.92%)</td><td>327.00 <b>(+31.48%)</b></td><td>240.40 <b>(+28.76%)</b></td><td>128.46 (+1.84%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>505.60 (n/a)</td><td>299.32 (n/a)</td><td>248.70 (n/a)</td><td>186.70 (n/a)</td><td>126.14 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (-10.89%)</td><td>0.01 (-1.52%)</td><td>0.01 (-0.36%)</td><td>0.01 (+16.59%)</td><td>0.00 (-11.75%)</td><td>547.50 (-14.23%)</td><td>363.32 (-1.63%)</td><td>294.00 (+0.38%)</td><td>258.00 (+12.22%)</td><td>128.96 <b>(-20.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>638.30 (n/a)</td><td>369.34 (n/a)</td><td>292.90 (n/a)</td><td>229.90 (n/a)</td><td>161.59 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(+27.25%)</b></td><td>0.02 <b>(+26.50%)</b></td><td>0.02 <b>(+33.48%)</b></td><td>0.01 <b>(+28.32%)</b></td><td>0.00 (+8.74%)</td><td>339.60 <b>(-22.07%)</b></td><td>260.58 <b>(-21.93%)</b></td><td>240.90 <b>(-25.07%)</b></td><td>196.60 <b>(-21.39%)</b></td><td>55.61 <b>(-32.11%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>435.80 (n/a)</td><td>333.78 (n/a)</td><td>321.50 (n/a)</td><td>250.10 (n/a)</td><td>81.92 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(+30.83%)</b></td><td>0.01 <b>(+28.47%)</b></td><td>0.02 <b>(+40.52%)</b></td><td>0.01 (-15.45%)</td><td>0.01 <b>(+55.03%)</b></td><td>652.80 (+18.28%)</td><td>339.94 (-15.36%)</td><td>258.40 <b>(-28.85%)</b></td><td>210.40 <b>(-23.57%)</b></td><td>181.45 <b>(+43.63%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.90 (n/a)</td><td>401.64 (n/a)</td><td>363.20 (n/a)</td><td>275.30 (n/a)</td><td>126.33 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(+37.57%)</b></td><td>0.01 <b>(+61.65%)</b></td><td>0.01 <b>(+126.56%)</b></td><td>0.01 (+11.66%)</td><td>0.00 <b>(+34.55%)</b></td><td>565.60 (-10.44%)</td><td>321.88 <b>(-37.26%)</b></td><td>274.60 <b>(-55.86%)</b></td><td>223.40 <b>(-27.33%)</b></td><td>139.58 (-12.22%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>631.50 (n/a)</td><td>513.02 (n/a)</td><td>622.10 (n/a)</td><td>307.40 (n/a)</td><td>159.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(+199.17%)</b></td><td>0.01 <b>(+177.61%)</b></td><td>0.01 <b>(+122.57%)</b></td><td>0.01 <b>(+318.64%)</b></td><td>0.00 <b>(+134.16%)</b></td><td>440.00 <b>(-76.11%)</b></td><td>340.08 <b>(-66.55%)</b></td><td>355.80 <b>(-55.07%)</b></td><td>226.80 <b>(-66.58%)</b></td><td>93.32 <b>(-80.95%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1842.00 (n/a)</td><td>1016.54 (n/a)</td><td>791.90 (n/a)</td><td>678.60 (n/a)</td><td>489.97 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (+11.99%)</td><td>0.01 (-8.19%)</td><td>0.01 <b>(-20.78%)</b></td><td>0.01 (+1.12%)</td><td>0.00 (+18.09%)</td><td>611.00 (-1.10%)</td><td>449.36 (+11.77%)</td><td>436.40 <b>(+26.20%)</b></td><td>245.30 (-10.70%)</td><td>160.90 (+11.11%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.80 (n/a)</td><td>402.04 (n/a)</td><td>345.80 (n/a)</td><td>274.70 (n/a)</td><td>144.81 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (-5.07%)</td><td>0.01 (-17.07%)</td><td>0.01 <b>(-40.05%)</b></td><td>0.00 <b>(+139.83%)</b></td><td>0.00 <b>(-32.39%)</b></td><td>851.30 <b>(-58.30%)</b></td><td>573.16 (-19.49%)</td><td>569.70 <b>(+66.77%)</b></td><td>293.50 (+5.35%)</td><td>200.76 <b>(-73.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2041.70 (n/a)</td><td>711.94 (n/a)</td><td>341.60 (n/a)</td><td>278.60 (n/a)</td><td>752.52 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (-11.04%)</td><td>0.01 <b>(-21.28%)</b></td><td>0.01 (-6.65%)</td><td>0.00 <b>(-21.15%)</b></td><td>0.00 <b>(-20.57%)</b></td><td>826.60 <b>(+26.84%)</b></td><td>534.62 <b>(+26.37%)</b></td><td>482.80 (+7.15%)</td><td>311.80 (+12.40%)</td><td>190.47 <b>(+22.71%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>651.70 (n/a)</td><td>423.06 (n/a)</td><td>450.60 (n/a)</td><td>277.40 (n/a)</td><td>155.23 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-18.81%)</td><td>0.02 <b>(-29.53%)</b></td><td>0.03 (-19.78%)</td><td>0.00 <b>(-73.18%)</b></td><td>0.01 (+14.55%)</td><td>2079.00 <b>(+272.78%)</b></td><td>681.42 <b>(+124.21%)</b></td><td>297.00 <b>(+24.63%)</b></td><td>265.80 <b>(+23.17%)</b></td><td>785.63 <b>(+441.91%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.70 (n/a)</td><td>303.92 (n/a)</td><td>238.30 (n/a)</td><td>215.80 (n/a)</td><td>144.98 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-15.25%)</td><td>0.02 (-13.00%)</td><td>0.02 (-13.73%)</td><td>0.02 (+4.90%)</td><td>0.01 <b>(-28.51%)</b></td><td>486.10 (-4.67%)</td><td>395.54 (+11.79%)</td><td>417.60 (+15.94%)</td><td>273.00 (+17.98%)</td><td>79.34 <b>(-22.36%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>509.90 (n/a)</td><td>353.82 (n/a)</td><td>360.20 (n/a)</td><td>231.40 (n/a)</td><td>102.19 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-4.20%)</td><td>0.02 <b>(-24.17%)</b></td><td>0.02 <b>(-47.41%)</b></td><td>0.01 <b>(-20.16%)</b></td><td>0.01 (-7.99%)</td><td>711.80 <b>(+25.25%)</b></td><td>480.48 <b>(+33.12%)</b></td><td>543.70 <b>(+90.10%)</b></td><td>241.60 (+4.41%)</td><td>186.30 (+19.85%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.30 (n/a)</td><td>360.94 (n/a)</td><td>286.00 (n/a)</td><td>231.40 (n/a)</td><td>155.44 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-7.12%)</td><td>0.03 (-1.72%)</td><td>0.03 (-15.68%)</td><td>0.02 <b>(+58.84%)</b></td><td>0.00 <b>(-54.73%)</b></td><td>352.10 <b>(-37.05%)</b></td><td>304.40 (-6.04%)</td><td>315.50 (+18.61%)</td><td>263.40 (+7.64%)</td><td>37.66 <b>(-71.54%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.30 (n/a)</td><td>323.96 (n/a)</td><td>266.00 (n/a)</td><td>244.70 (n/a)</td><td>132.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(-40.67%)</b></td><td>0.02 <b>(-45.34%)</b></td><td>0.02 <b>(-48.66%)</b></td><td>0.01 <b>(-40.91%)</b></td><td>0.00 <b>(-39.78%)</b></td><td>706.60 <b>(+69.25%)</b></td><td>518.36 <b>(+82.65%)</b></td><td>516.00 <b>(+94.79%)</b></td><td>354.70 <b>(+68.58%)</b></td><td>127.28 <b>(+61.82%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>417.50 (n/a)</td><td>283.80 (n/a)</td><td>264.90 (n/a)</td><td>210.40 (n/a)</td><td>78.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(-44.60%)</b></td><td>0.02 <b>(-51.28%)</b></td><td>0.02 <b>(-53.81%)</b></td><td>0.01 <b>(-54.93%)</b></td><td>0.00 <b>(-21.87%)</b></td><td>628.20 <b>(+121.90%)</b></td><td>516.18 <b>(+107.52%)</b></td><td>506.30 <b>(+116.55%)</b></td><td>413.70 <b>(+80.50%)</b></td><td>78.76 <b>(+215.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>283.10 (n/a)</td><td>248.74 (n/a)</td><td>233.80 (n/a)</td><td>229.20 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-12.01%)</td><td>0.02 (-14.28%)</td><td>0.02 (-2.68%)</td><td>0.01 (-12.11%)</td><td>0.01 <b>(-29.63%)</b></td><td>648.30 (+13.78%)</td><td>475.44 (+11.78%)</td><td>502.50 (+2.74%)</td><td>290.40 (+13.62%)</td><td>129.86 (-11.27%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.80 (n/a)</td><td>425.34 (n/a)</td><td>489.10 (n/a)</td><td>255.60 (n/a)</td><td>146.36 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-15.49%)</td><td>0.02 <b>(-22.53%)</b></td><td>0.02 <b>(-31.18%)</b></td><td>0.01 (+1.21%)</td><td>0.01 <b>(-37.75%)</b></td><td>566.10 (-1.19%)</td><td>444.50 <b>(+21.87%)</b></td><td>453.40 <b>(+45.32%)</b></td><td>291.50 (+18.35%)</td><td>105.37 <b>(-25.70%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.90 (n/a)</td><td>364.74 (n/a)</td><td>312.00 (n/a)</td><td>246.30 (n/a)</td><td>141.81 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (+9.89%)</td><td>0.02 (-17.33%)</td><td>0.02 <b>(-43.90%)</b></td><td>0.01 (-3.22%)</td><td>0.01 (+19.59%)</td><td>549.40 (+3.33%)</td><td>460.14 <b>(+23.71%)</b></td><td>525.40 <b>(+78.22%)</b></td><td>222.40 (-9.00%)</td><td>137.21 (+4.25%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.70 (n/a)</td><td>371.96 (n/a)</td><td>294.80 (n/a)</td><td>244.40 (n/a)</td><td>131.62 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (+3.70%)</td><td>0.02 <b>(-28.09%)</b></td><td>0.02 <b>(-49.23%)</b></td><td>0.01 (-5.42%)</td><td>0.01 (+4.22%)</td><td>547.30 (+5.72%)</td><td>455.06 <b>(+40.29%)</b></td><td>490.50 <b>(+96.91%)</b></td><td>236.50 (-3.59%)</td><td>125.12 (+5.17%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.70 (n/a)</td><td>324.38 (n/a)</td><td>249.10 (n/a)</td><td>245.30 (n/a)</td><td>118.97 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (+9.74%)</td><td>0.02 (-0.63%)</td><td>0.02 (+10.03%)</td><td>0.01 (-10.99%)</td><td>0.01 (+4.73%)</td><td>661.70 (+12.36%)</td><td>476.38 (+1.33%)</td><td>508.30 (-9.10%)</td><td>278.60 (-8.86%)</td><td>153.40 (+5.94%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.90 (n/a)</td><td>470.12 (n/a)</td><td>559.20 (n/a)</td><td>305.70 (n/a)</td><td>144.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(-24.63%)</b></td><td>0.02 <b>(-28.69%)</b></td><td>0.02 <b>(-38.05%)</b></td><td>0.01 <b>(-21.04%)</b></td><td>0.00 <b>(-36.15%)</b></td><td>680.50 <b>(+26.65%)</b></td><td>533.44 <b>(+36.01%)</b></td><td>536.60 <b>(+61.43%)</b></td><td>350.90 <b>(+32.67%)</b></td><td>138.25 (+2.96%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.30 (n/a)</td><td>392.22 (n/a)</td><td>332.40 (n/a)</td><td>264.50 (n/a)</td><td>134.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 (+10.19%)</td><td>0.06 (+0.23%)</td><td>0.05 (-8.65%)</td><td>0.03 (-0.17%)</td><td>0.02 (+7.12%)</td><td>480.10 (+0.19%)</td><td>315.36 (+0.22%)</td><td>313.30 (+9.47%)</td><td>213.90 (-9.25%)</td><td>101.55 (+0.95%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>479.20 (n/a)</td><td>314.68 (n/a)</td><td>286.20 (n/a)</td><td>235.70 (n/a)</td><td>100.59 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (+19.64%)</td><td>0.04 (-12.80%)</td><td>0.04 <b>(-23.41%)</b></td><td>0.03 <b>(-34.96%)</b></td><td>0.02 <b>(+319.95%)</b></td><td>551.20 <b>(+53.75%)</b></td><td>410.92 <b>(+25.99%)</b></td><td>431.90 <b>(+30.56%)</b></td><td>245.30 (-16.39%)</td><td>134.60 <b>(+450.42%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>358.50 (n/a)</td><td>326.14 (n/a)</td><td>330.80 (n/a)</td><td>293.40 (n/a)</td><td>24.45 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (-10.72%)</td><td>0.05 (-3.65%)</td><td>0.05 (+0.14%)</td><td>0.03 (-6.22%)</td><td>0.01 (-16.22%)</td><td>554.90 (+6.63%)</td><td>370.68 (+1.85%)</td><td>302.80 (-0.13%)</td><td>256.00 (+12.04%)</td><td>125.34 (-3.99%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>520.40 (n/a)</td><td>363.96 (n/a)</td><td>303.20 (n/a)</td><td>228.50 (n/a)</td><td>130.55 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 <b>(-25.85%)</b></td><td>0.05 (-13.22%)</td><td>0.06 (-6.14%)</td><td>0.03 (-5.34%)</td><td>0.01 <b>(-27.59%)</b></td><td>531.30 (+5.63%)</td><td>342.06 (+12.39%)</td><td>288.30 (+6.54%)</td><td>256.30 <b>(+34.89%)</b></td><td>114.63 (-2.43%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>503.00 (n/a)</td><td>304.36 (n/a)</td><td>270.60 (n/a)</td><td>190.00 (n/a)</td><td>117.48 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 (+9.76%)</td><td>0.05 (+1.76%)</td><td>0.03 (-13.06%)</td><td>0.03 (-9.31%)</td><td>0.02 <b>(+40.17%)</b></td><td>553.20 (+10.27%)</td><td>408.58 (+6.03%)</td><td>480.30 (+15.01%)</td><td>217.20 (-8.89%)</td><td>162.50 <b>(+41.75%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>501.70 (n/a)</td><td>385.36 (n/a)</td><td>417.60 (n/a)</td><td>238.40 (n/a)</td><td>114.64 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (+0.67%)</td><td>0.05 <b>(+52.05%)</b></td><td>0.06 <b>(+74.95%)</b></td><td>0.04 <b>(+327.71%)</b></td><td>0.01 <b>(-38.57%)</b></td><td>456.50 <b>(-76.62%)</b></td><td>345.64 <b>(-54.41%)</b></td><td>297.40 <b>(-42.84%)</b></td><td>273.80 (-0.65%)</td><td>85.39 <b>(-87.40%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1952.70 (n/a)</td><td>758.14 (n/a)</td><td>520.30 (n/a)</td><td>275.60 (n/a)</td><td>677.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 <b>(+23.28%)</b></td><td>0.04 (+1.43%)</td><td>0.03 (-5.57%)</td><td>0.03 (-14.19%)</td><td>0.02 <b>(+65.47%)</b></td><td>632.30 (+16.53%)</td><td>461.54 (+5.05%)</td><td>476.40 (+5.89%)</td><td>236.70 (-18.85%)</td><td>146.38 <b>(+48.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>542.60 (n/a)</td><td>439.34 (n/a)</td><td>449.90 (n/a)</td><td>291.70 (n/a)</td><td>98.45 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 <b>(+26.77%)</b></td><td>0.04 (+11.56%)</td><td>0.03 (-1.35%)</td><td>0.01 (-8.58%)</td><td>0.02 <b>(+37.26%)</b></td><td>2099.60 (+9.39%)</td><td>757.24 (+2.24%)</td><td>505.80 (+1.38%)</td><td>241.10 <b>(-21.11%)</b></td><td>760.61 (+14.54%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1919.40 (n/a)</td><td>740.68 (n/a)</td><td>498.90 (n/a)</td><td>305.60 (n/a)</td><td>664.07 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (+10.16%)</td><td>0.04 (+5.71%)</td><td>0.04 <b>(+20.04%)</b></td><td>0.01 <b>(-70.90%)</b></td><td>0.02 <b>(+81.58%)</b></td><td>2032.80 <b>(+243.67%)</b></td><td>719.78 <b>(+50.22%)</b></td><td>423.10 (-16.68%)</td><td>258.30 (-9.21%)</td><td>745.30 <b>(+518.71%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.50 (n/a)</td><td>479.14 (n/a)</td><td>507.80 (n/a)</td><td>284.50 (n/a)</td><td>120.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (-11.00%)</td><td>0.04 (+4.72%)</td><td>0.03 (+0.30%)</td><td>0.03 (-2.90%)</td><td>0.02 (-12.80%)</td><td>621.60 (+2.98%)</td><td>434.50 (-5.18%)</td><td>477.50 (-0.29%)</td><td>262.40 (+12.38%)</td><td>145.81 (+6.39%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>603.60 (n/a)</td><td>458.24 (n/a)</td><td>478.90 (n/a)</td><td>233.50 (n/a)</td><td>137.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (+9.45%)</td><td>0.04 (+13.22%)</td><td>0.04 <b>(+25.93%)</b></td><td>0.03 (+11.68%)</td><td>0.01 (+6.20%)</td><td>547.60 (-10.46%)</td><td>426.14 (-12.09%)</td><td>440.60 <b>(-20.58%)</b></td><td>286.20 (-8.62%)</td><td>113.43 (-12.54%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>611.60 (n/a)</td><td>484.76 (n/a)</td><td>554.80 (n/a)</td><td>313.20 (n/a)</td><td>129.69 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (+15.57%)</td><td>0.05 (+0.33%)</td><td>0.06 (+10.11%)</td><td>0.03 <b>(-26.88%)</b></td><td>0.02 <b>(+123.23%)</b></td><td>588.20 <b>(+36.76%)</b></td><td>388.02 (+12.04%)</td><td>290.90 (-9.21%)</td><td>251.80 (-13.47%)</td><td>169.16 <b>(+168.25%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>430.10 (n/a)</td><td>346.32 (n/a)</td><td>320.40 (n/a)</td><td>291.00 (n/a)</td><td>63.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 (-13.76%)</td><td>0.08 (-14.34%)</td><td>0.09 (-7.21%)</td><td>0.02 <b>(-72.63%)</b></td><td>0.04 <b>(+28.44%)</b></td><td>1881.50 <b>(+265.41%)</b></td><td>650.96 <b>(+72.69%)</b></td><td>350.50 (+7.78%)</td><td>294.70 (+15.98%)</td><td>688.71 <b>(+474.55%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>514.90 (n/a)</td><td>376.96 (n/a)</td><td>325.20 (n/a)</td><td>254.10 (n/a)</td><td>119.87 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.16 <b>(+38.43%)</b></td><td>0.12 <b>(+51.66%)</b></td><td>0.13 <b>(+74.38%)</b></td><td>0.07 <b>(+27.90%)</b></td><td>0.03 <b>(+53.16%)</b></td><td>464.40 <b>(-21.82%)</b></td><td>301.38 <b>(-32.62%)</b></td><td>259.70 <b>(-42.65%)</b></td><td>210.70 <b>(-27.77%)</b></td><td>100.05 (-7.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>594.00 (n/a)</td><td>447.30 (n/a)</td><td>452.80 (n/a)</td><td>291.70 (n/a)</td><td>108.18 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.16 <b>(+20.82%)</b></td><td>0.11 (+18.24%)</td><td>0.12 <b>(+33.88%)</b></td><td>0.06 (+7.95%)</td><td>0.05 <b>(+30.94%)</b></td><td>544.50 (-7.37%)</td><td>358.70 (-11.75%)</td><td>267.60 <b>(-25.31%)</b></td><td>200.10 (-17.21%)</td><td>165.77 (+4.68%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.80 (n/a)</td><td>406.46 (n/a)</td><td>358.30 (n/a)</td><td>241.70 (n/a)</td><td>158.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.21 <b>(+35.46%)</b></td><td>0.12 (+19.85%)</td><td>0.11 (+3.34%)</td><td>0.07 <b>(+26.79%)</b></td><td>0.06 <b>(+34.56%)</b></td><td>452.90 <b>(-21.13%)</b></td><td>316.20 (-16.53%)</td><td>285.80 (-3.25%)</td><td>157.50 <b>(-26.19%)</b></td><td>126.00 <b>(-23.46%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>574.20 (n/a)</td><td>378.84 (n/a)</td><td>295.40 (n/a)</td><td>213.40 (n/a)</td><td>164.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 <b>(+30.27%)</b></td><td>0.10 (+3.82%)</td><td>0.10 (-10.13%)</td><td>0.05 (-2.58%)</td><td>0.04 <b>(+29.57%)</b></td><td>610.80 (+2.66%)</td><td>384.32 (-1.13%)</td><td>335.40 (+11.28%)</td><td>192.10 <b>(-23.25%)</b></td><td>160.26 (+0.46%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>595.00 (n/a)</td><td>388.72 (n/a)</td><td>301.40 (n/a)</td><td>250.30 (n/a)</td><td>159.54 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.16 (+9.69%)</td><td>0.11 (+1.60%)</td><td>0.12 (+5.07%)</td><td>0.06 (-19.06%)</td><td>0.05 <b>(+45.08%)</b></td><td>569.80 <b>(+23.55%)</b></td><td>339.66 (+8.13%)</td><td>271.70 (-4.83%)</td><td>202.80 (-8.81%)</td><td>163.32 <b>(+60.75%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>461.20 (n/a)</td><td>314.12 (n/a)</td><td>285.50 (n/a)</td><td>222.40 (n/a)</td><td>101.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.18 <b>(+28.97%)</b></td><td>0.10 (+3.28%)</td><td>0.08 <b>(-24.59%)</b></td><td>0.04 <b>(-27.94%)</b></td><td>0.06 <b>(+53.64%)</b></td><td>834.20 <b>(+38.78%)</b></td><td>457.46 (+11.66%)</td><td>420.90 <b>(+32.61%)</b></td><td>178.50 <b>(-22.46%)</b></td><td>261.00 <b>(+48.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>601.10 (n/a)</td><td>409.68 (n/a)</td><td>317.40 (n/a)</td><td>230.20 (n/a)</td><td>175.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (+18.72%)</td><td>0.10 <b>(+33.29%)</b></td><td>0.10 <b>(+49.77%)</b></td><td>0.08 <b>(+34.09%)</b></td><td>0.03 (+13.30%)</td><td>421.30 <b>(-25.43%)</b></td><td>333.34 <b>(-25.46%)</b></td><td>313.40 <b>(-33.23%)</b></td><td>240.40 (-15.77%)</td><td>81.34 <b>(-23.11%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>565.00 (n/a)</td><td>447.20 (n/a)</td><td>469.40 (n/a)</td><td>285.40 (n/a)</td><td>105.79 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 <b>(-21.86%)</b></td><td>0.08 <b>(-21.82%)</b></td><td>0.08 <b>(-41.12%)</b></td><td>0.06 (+1.92%)</td><td>0.02 <b>(-45.39%)</b></td><td>541.50 (-1.88%)</td><td>416.00 (+17.22%)</td><td>436.40 <b>(+69.81%)</b></td><td>297.50 <b>(+27.96%)</b></td><td>105.35 <b>(-32.35%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>551.90 (n/a)</td><td>354.90 (n/a)</td><td>257.00 (n/a)</td><td>232.50 (n/a)</td><td>155.73 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (-2.04%)</td><td>0.09 (+5.49%)</td><td>0.08 (-0.87%)</td><td>0.07 (+12.28%)</td><td>0.03 (-6.57%)</td><td>480.70 (-10.93%)</td><td>372.56 (-6.27%)</td><td>403.00 (+0.88%)</td><td>238.20 (+2.10%)</td><td>98.15 (-11.19%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>539.70 (n/a)</td><td>397.48 (n/a)</td><td>399.50 (n/a)</td><td>233.30 (n/a)</td><td>110.52 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 (-15.19%)</td><td>0.08 (-15.95%)</td><td>0.09 (+3.20%)</td><td>0.04 <b>(-26.49%)</b></td><td>0.03 (+4.11%)</td><td>772.80 <b>(+36.06%)</b></td><td>477.68 <b>(+25.90%)</b></td><td>358.90 (-3.10%)</td><td>291.10 (+17.90%)</td><td>204.62 <b>(+69.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>568.00 (n/a)</td><td>379.40 (n/a)</td><td>370.40 (n/a)</td><td>246.90 (n/a)</td><td>121.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.19 <b>(+50.71%)</b></td><td>0.10 (+7.90%)</td><td>0.08 (-19.99%)</td><td>0.05 (-19.75%)</td><td>0.05 <b>(+100.84%)</b></td><td>664.10 <b>(+24.62%)</b></td><td>387.30 (+4.78%)</td><td>393.40 <b>(+24.97%)</b></td><td>170.30 <b>(-33.66%)</b></td><td>181.10 <b>(+57.74%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>532.90 (n/a)</td><td>369.62 (n/a)</td><td>314.80 (n/a)</td><td>256.70 (n/a)</td><td>114.81 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (-4.80%)</td><td>0.01 (-1.63%)</td><td>0.01 (-8.06%)</td><td>0.01 (+6.55%)</td><td>0.00 (-18.60%)</td><td>481.50 (-6.14%)</td><td>323.00 (-3.95%)</td><td>300.80 (+8.75%)</td><td>199.90 (+5.04%)</td><td>113.94 <b>(-23.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>513.00 (n/a)</td><td>336.30 (n/a)</td><td>276.60 (n/a)</td><td>190.30 (n/a)</td><td>148.90 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (-11.69%)</td><td>0.02 (-14.23%)</td><td>0.02 <b>(-26.22%)</b></td><td>0.01 (-19.90%)</td><td>0.01 (+1.89%)</td><td>576.90 <b>(+24.84%)</b></td><td>390.52 (+19.62%)</td><td>376.80 <b>(+35.54%)</b></td><td>257.40 (+13.24%)</td><td>138.97 <b>(+34.08%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>462.10 (n/a)</td><td>326.48 (n/a)</td><td>278.00 (n/a)</td><td>227.30 (n/a)</td><td>103.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(-24.19%)</b></td><td>0.01 (-10.79%)</td><td>0.01 (-2.50%)</td><td>0.01 (-5.95%)</td><td>0.00 <b>(-30.21%)</b></td><td>559.60 (+6.33%)</td><td>422.06 (+6.17%)</td><td>492.90 (+2.56%)</td><td>224.50 <b>(+31.90%)</b></td><td>154.24 (-2.65%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>526.30 (n/a)</td><td>397.54 (n/a)</td><td>480.60 (n/a)</td><td>170.20 (n/a)</td><td>158.44 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(-34.97%)</b></td><td>0.01 (-4.64%)</td><td>0.01 <b>(+24.78%)</b></td><td>0.01 (+6.62%)</td><td>0.00 <b>(-56.35%)</b></td><td>563.00 (-6.20%)</td><td>425.42 (-5.43%)</td><td>376.60 (-19.86%)</td><td>325.50 <b>(+53.76%)</b></td><td>103.03 <b>(-36.97%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.20 (n/a)</td><td>449.84 (n/a)</td><td>469.90 (n/a)</td><td>211.70 (n/a)</td><td>163.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (+0.07%)</td><td>0.01 (-12.22%)</td><td>0.01 <b>(-27.91%)</b></td><td>0.00 (-0.31%)</td><td>0.01 (-12.58%)</td><td>1924.70 (+0.31%)</td><td>687.04 (+4.79%)</td><td>403.80 <b>(+38.72%)</b></td><td>240.80 (-0.08%)</td><td>698.08 (-2.61%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1918.80 (n/a)</td><td>655.66 (n/a)</td><td>291.10 (n/a)</td><td>241.00 (n/a)</td><td>716.75 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (-2.15%)</td><td>0.01 <b>(-20.78%)</b></td><td>0.01 <b>(-38.01%)</b></td><td>0.01 (-0.93%)</td><td>0.01 (-2.42%)</td><td>627.20 (+0.93%)</td><td>475.72 <b>(+24.72%)</b></td><td>519.10 <b>(+61.36%)</b></td><td>232.40 (+2.20%)</td><td>147.14 (-8.58%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.40 (n/a)</td><td>381.44 (n/a)</td><td>321.70 (n/a)</td><td>227.40 (n/a)</td><td>160.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(-23.76%)</b></td><td>0.01 (+1.95%)</td><td>0.01 (+0.96%)</td><td>0.01 (+1.88%)</td><td>0.00 <b>(-29.19%)</b></td><td>619.10 (-1.85%)</td><td>426.96 (-7.01%)</td><td>467.90 (-0.95%)</td><td>248.20 <b>(+31.11%)</b></td><td>159.07 (-5.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.80 (n/a)</td><td>459.16 (n/a)</td><td>472.40 (n/a)</td><td>189.30 (n/a)</td><td>168.34 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 <b>(+39.97%)</b></td><td>0.01 <b>(+23.29%)</b></td><td>0.01 (+6.96%)</td><td>0.01 (-14.76%)</td><td>0.01 <b>(+114.40%)</b></td><td>655.80 (+17.32%)</td><td>425.00 (-9.81%)</td><td>453.00 (-6.52%)</td><td>224.60 <b>(-28.56%)</b></td><td>172.35 <b>(+80.61%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.00 (n/a)</td><td>471.24 (n/a)</td><td>484.60 (n/a)</td><td>314.40 (n/a)</td><td>95.43 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 <b>(+33.67%)</b></td><td>0.01 <b>(+38.04%)</b></td><td>0.01 <b>(+32.45%)</b></td><td>0.01 <b>(+105.32%)</b></td><td>0.00 (-2.33%)</td><td>547.50 <b>(-51.29%)</b></td><td>431.38 <b>(-33.25%)</b></td><td>435.10 <b>(-24.50%)</b></td><td>291.40 <b>(-25.19%)</b></td><td>92.51 <b>(-67.43%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1124.10 (n/a)</td><td>646.26 (n/a)</td><td>576.30 (n/a)</td><td>389.50 (n/a)</td><td>284.08 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (+0.94%)</td><td>0.01 (+11.55%)</td><td>0.01 (+15.87%)</td><td>0.01 (+15.36%)</td><td>0.00 (-10.69%)</td><td>533.50 (-13.32%)</td><td>445.46 (-12.70%)</td><td>489.20 (-13.69%)</td><td>266.00 (-0.93%)</td><td>111.58 <b>(-20.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>615.50 (n/a)</td><td>510.26 (n/a)</td><td>566.80 (n/a)</td><td>268.50 (n/a)</td><td>140.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (-6.49%)</td><td>0.01 (-5.76%)</td><td>0.01 (-0.55%)</td><td>0.01 (+5.25%)</td><td>0.00 (-12.11%)</td><td>626.30 (-4.99%)</td><td>476.54 (+4.23%)</td><td>522.70 (+0.54%)</td><td>293.20 (+6.93%)</td><td>150.87 (-6.26%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>659.20 (n/a)</td><td>457.18 (n/a)</td><td>519.90 (n/a)</td><td>274.20 (n/a)</td><td>160.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (-0.90%)</td><td>0.03 (+13.75%)</td><td>0.03 <b>(+33.44%)</b></td><td>0.02 (+9.91%)</td><td>0.01 (+0.45%)</td><td>507.50 (-9.02%)</td><td>351.90 (-11.96%)</td><td>303.00 <b>(-25.06%)</b></td><td>231.10 (+0.87%)</td><td>119.02 (-1.21%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.80 (n/a)</td><td>399.72 (n/a)</td><td>404.30 (n/a)</td><td>229.10 (n/a)</td><td>120.48 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (-13.77%)</td><td>0.03 (+3.02%)</td><td>0.03 (-4.38%)</td><td>0.02 (-0.25%)</td><td>0.01 (-10.96%)</td><td>767.10 (+0.26%)</td><td>450.86 (-4.87%)</td><td>454.60 (+4.58%)</td><td>278.50 (+15.99%)</td><td>199.83 (-3.68%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>765.10 (n/a)</td><td>473.96 (n/a)</td><td>434.70 (n/a)</td><td>240.10 (n/a)</td><td>207.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (-12.03%)</td><td>0.02 (-15.94%)</td><td>0.02 <b>(-29.03%)</b></td><td>0.00 <b>(-70.88%)</b></td><td>0.01 (+19.33%)</td><td>1900.20 <b>(+243.43%)</b></td><td>652.32 <b>(+81.65%)</b></td><td>378.90 <b>(+40.91%)</b></td><td>227.90 (+13.67%)</td><td>707.73 <b>(+336.28%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.30 (n/a)</td><td>359.10 (n/a)</td><td>268.90 (n/a)</td><td>200.50 (n/a)</td><td>162.22 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (-0.06%)</td><td>0.03 (+4.44%)</td><td>0.03 <b>(+50.47%)</b></td><td>0.02 (-14.75%)</td><td>0.01 (+1.97%)</td><td>610.30 (+17.30%)</td><td>409.38 (-2.79%)</td><td>332.60 <b>(-33.53%)</b></td><td>266.40 (+0.08%)</td><td>145.49 (+19.20%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.30 (n/a)</td><td>421.12 (n/a)</td><td>500.40 (n/a)</td><td>266.20 (n/a)</td><td>122.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (+1.29%)</td><td>0.03 <b>(+39.71%)</b></td><td>0.03 <b>(+74.60%)</b></td><td>0.02 <b>(+49.83%)</b></td><td>0.01 <b>(-25.13%)</b></td><td>418.60 <b>(-33.26%)</b></td><td>317.66 <b>(-33.93%)</b></td><td>306.00 <b>(-42.73%)</b></td><td>219.10 (-1.26%)</td><td>84.07 <b>(-46.67%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.20 (n/a)</td><td>480.82 (n/a)</td><td>534.30 (n/a)</td><td>221.90 (n/a)</td><td>157.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-2.22%)</td><td>0.02 (-15.59%)</td><td>0.02 (-15.99%)</td><td>0.01 <b>(-35.55%)</b></td><td>0.01 <b>(+65.60%)</b></td><td>821.30 <b>(+55.17%)</b></td><td>526.52 <b>(+30.16%)</b></td><td>438.50 (+19.03%)</td><td>331.80 (+2.28%)</td><td>214.64 <b>(+159.47%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>529.30 (n/a)</td><td>404.52 (n/a)</td><td>368.40 (n/a)</td><td>324.40 (n/a)</td><td>82.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (+5.38%)</td><td>0.02 (-6.12%)</td><td>0.02 (-17.19%)</td><td>0.01 <b>(-22.52%)</b></td><td>0.01 <b>(+35.38%)</b></td><td>673.10 <b>(+29.07%)</b></td><td>433.34 (+13.02%)</td><td>409.30 <b>(+20.77%)</b></td><td>260.20 (-5.11%)</td><td>165.39 <b>(+61.17%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.50 (n/a)</td><td>383.42 (n/a)</td><td>338.90 (n/a)</td><td>274.20 (n/a)</td><td>102.61 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 <b>(+32.96%)</b></td><td>0.02 <b>(+51.64%)</b></td><td>0.02 (+6.04%)</td><td>0.02 <b>(+217.65%)</b></td><td>0.01 (-8.02%)</td><td>570.00 <b>(-68.52%)</b></td><td>418.68 <b>(-49.77%)</b></td><td>459.90 (-5.70%)</td><td>267.50 <b>(-24.78%)</b></td><td>127.85 <b>(-79.10%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1810.70 (n/a)</td><td>833.50 (n/a)</td><td>487.70 (n/a)</td><td>355.60 (n/a)</td><td>611.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (+11.35%)</td><td>0.03 <b>(+33.92%)</b></td><td>0.03 <b>(+36.16%)</b></td><td>0.03 <b>(+129.56%)</b></td><td>0.00 <b>(-54.79%)</b></td><td>306.90 <b>(-56.44%)</b></td><td>254.24 <b>(-35.22%)</b></td><td>241.50 <b>(-26.55%)</b></td><td>218.80 (-10.18%)</td><td>35.33 <b>(-81.58%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>704.60 (n/a)</td><td>392.46 (n/a)</td><td>328.80 (n/a)</td><td>243.60 (n/a)</td><td>191.79 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (+0.72%)</td><td>0.02 (+2.64%)</td><td>0.02 (+3.76%)</td><td>0.02 (-12.31%)</td><td>0.01 <b>(+48.79%)</b></td><td>589.50 (+14.05%)</td><td>447.82 (+0.62%)</td><td>443.80 (-3.63%)</td><td>332.20 (-0.72%)</td><td>115.52 <b>(+68.36%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>516.90 (n/a)</td><td>445.06 (n/a)</td><td>460.50 (n/a)</td><td>334.60 (n/a)</td><td>68.62 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (-3.05%)</td><td>0.03 <b>(+27.95%)</b></td><td>0.02 <b>(+37.31%)</b></td><td>0.02 <b>(+49.53%)</b></td><td>0.00 <b>(-38.78%)</b></td><td>383.20 <b>(-33.14%)</b></td><td>333.14 <b>(-26.03%)</b></td><td>349.30 <b>(-27.17%)</b></td><td>266.10 (+3.14%)</td><td>53.88 <b>(-55.11%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>573.10 (n/a)</td><td>450.40 (n/a)</td><td>479.60 (n/a)</td><td>258.00 (n/a)</td><td>120.03 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (-0.91%)</td><td>0.05 (+9.85%)</td><td>0.05 (+6.85%)</td><td>0.04 <b>(+42.95%)</b></td><td>0.01 <b>(-24.84%)</b></td><td>413.60 <b>(-30.05%)</b></td><td>312.36 (-13.69%)</td><td>304.40 (-6.42%)</td><td>252.00 (+0.92%)</td><td>66.82 <b>(-50.43%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.30 (n/a)</td><td>361.92 (n/a)</td><td>325.30 (n/a)</td><td>249.70 (n/a)</td><td>134.79 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (+9.18%)</td><td>0.06 (-2.49%)</td><td>0.05 (-15.39%)</td><td>0.05 <b>(+25.83%)</b></td><td>0.02 (-17.10%)</td><td>537.20 <b>(-20.53%)</b></td><td>429.98 (-2.67%)</td><td>453.60 (+18.19%)</td><td>272.40 (-8.41%)</td><td>97.53 <b>(-41.14%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>676.00 (n/a)</td><td>441.78 (n/a)</td><td>383.80 (n/a)</td><td>297.40 (n/a)</td><td>165.69 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 (+16.60%)</td><td>0.06 <b>(+30.80%)</b></td><td>0.06 <b>(+22.15%)</b></td><td>0.03 <b>(+35.09%)</b></td><td>0.02 (-6.10%)</td><td>602.80 <b>(-25.97%)</b></td><td>317.70 <b>(-28.97%)</b></td><td>254.40 (-18.15%)</td><td>217.80 (-14.22%)</td><td>160.67 <b>(-34.45%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>814.30 (n/a)</td><td>447.28 (n/a)</td><td>310.80 (n/a)</td><td>253.90 (n/a)</td><td>245.09 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (+15.37%)</td><td>0.06 (+13.55%)</td><td>0.04 (-3.29%)</td><td>0.03 (-15.72%)</td><td>0.03 <b>(+84.29%)</b></td><td>655.70 (+18.66%)</td><td>445.96 (+0.71%)</td><td>478.50 (+3.41%)</td><td>236.30 (-13.35%)</td><td>199.60 <b>(+92.70%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>552.60 (n/a)</td><td>442.82 (n/a)</td><td>462.70 (n/a)</td><td>272.70 (n/a)</td><td>103.58 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (+13.17%)</td><td>0.05 (+9.36%)</td><td>0.04 (+0.15%)</td><td>0.04 <b>(+32.91%)</b></td><td>0.01 (+6.07%)</td><td>445.20 <b>(-24.76%)</b></td><td>361.50 (-9.85%)</td><td>409.60 (-0.15%)</td><td>250.60 (-11.64%)</td><td>93.68 <b>(-25.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.70 (n/a)</td><td>401.00 (n/a)</td><td>410.20 (n/a)</td><td>283.60 (n/a)</td><td>126.31 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 <b>(-25.10%)</b></td><td>0.04 <b>(-32.99%)</b></td><td>0.04 (-12.85%)</td><td>0.02 <b>(-55.43%)</b></td><td>0.02 <b>(-24.07%)</b></td><td>1081.00 <b>(+124.32%)</b></td><td>602.08 <b>(+58.78%)</b></td><td>536.40 (+14.74%)</td><td>308.20 <b>(+33.48%)</b></td><td>296.59 <b>(+129.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>481.90 (n/a)</td><td>379.18 (n/a)</td><td>467.50 (n/a)</td><td>230.90 (n/a)</td><td>128.96 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (-12.30%)</td><td>0.04 (-1.53%)</td><td>0.04 (+6.65%)</td><td>0.03 (-10.66%)</td><td>0.02 (-12.53%)</td><td>613.30 (+11.94%)</td><td>437.56 (+1.99%)</td><td>433.20 (-6.23%)</td><td>236.30 (+14.04%)</td><td>164.39 (+18.99%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>547.90 (n/a)</td><td>429.02 (n/a)</td><td>462.00 (n/a)</td><td>207.20 (n/a)</td><td>138.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 <b>(-31.73%)</b></td><td>0.04 (-19.34%)</td><td>0.04 <b>(-26.24%)</b></td><td>0.03 <b>(+26.07%)</b></td><td>0.01 <b>(-69.78%)</b></td><td>561.80 <b>(-20.67%)</b></td><td>476.22 (+11.20%)</td><td>467.80 <b>(+35.59%)</b></td><td>409.50 <b>(+46.46%)</b></td><td>64.02 <b>(-64.65%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>708.20 (n/a)</td><td>428.26 (n/a)</td><td>345.00 (n/a)</td><td>279.60 (n/a)</td><td>181.09 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 <b>(+115.26%)</b></td><td>0.05 <b>(+163.65%)</b></td><td>0.06 <b>(+187.15%)</b></td><td>0.03 <b>(+264.78%)</b></td><td>0.02 <b>(+72.31%)</b></td><td>519.70 <b>(-72.58%)</b></td><td>360.06 <b>(-68.22%)</b></td><td>265.20 <b>(-65.17%)</b></td><td>246.50 <b>(-53.54%)</b></td><td>142.85 <b>(-79.36%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1895.60 (n/a)</td><td>1132.92 (n/a)</td><td>761.50 (n/a)</td><td>530.60 (n/a)</td><td>692.07 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 <b>(+41.73%)</b></td><td>0.05 <b>(+22.72%)</b></td><td>0.04 (+17.63%)</td><td>0.03 (+19.12%)</td><td>0.02 <b>(+69.71%)</b></td><td>589.20 (-16.04%)</td><td>437.32 (-13.98%)</td><td>435.30 (-15.00%)</td><td>208.00 <b>(-29.44%)</b></td><td>147.52 (+1.40%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>701.80 (n/a)</td><td>508.40 (n/a)</td><td>512.10 (n/a)</td><td>294.80 (n/a)</td><td>145.48 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 <b>(+25.80%)</b></td><td>0.04 (+1.26%)</td><td>0.04 (+8.25%)</td><td>0.03 (-10.56%)</td><td>0.02 <b>(+54.68%)</b></td><td>608.40 (+11.82%)</td><td>447.14 (+4.37%)</td><td>436.70 (-7.62%)</td><td>240.40 <b>(-20.53%)</b></td><td>147.62 <b>(+40.10%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>544.10 (n/a)</td><td>428.40 (n/a)</td><td>472.70 (n/a)</td><td>302.50 (n/a)</td><td>105.36 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 <b>(-20.29%)</b></td><td>0.10 (-11.75%)</td><td>0.11 (-10.30%)</td><td>0.06 (+3.00%)</td><td>0.03 <b>(-25.84%)</b></td><td>534.50 (-2.91%)</td><td>365.56 (+9.31%)</td><td>296.80 (+11.50%)</td><td>276.10 <b>(+25.44%)</b></td><td>115.65 (-13.88%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>550.50 (n/a)</td><td>334.44 (n/a)</td><td>266.20 (n/a)</td><td>220.10 (n/a)</td><td>134.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.16 (+10.80%)</td><td>0.10 (-16.88%)</td><td>0.12 (-0.61%)</td><td>0.02 <b>(-76.42%)</b></td><td>0.06 <b>(+207.56%)</b></td><td>1381.90 <b>(+324.03%)</b></td><td>529.74 <b>(+88.98%)</b></td><td>282.90 (+0.64%)</td><td>208.60 (-9.78%)</td><td>493.60 <b>(+1088.20%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>325.90 (n/a)</td><td>280.32 (n/a)</td><td>281.10 (n/a)</td><td>231.20 (n/a)</td><td>41.54 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 <b>(+70.54%)</b></td><td>0.11 <b>(+44.80%)</b></td><td>0.09 <b>(+21.89%)</b></td><td>0.07 <b>(+49.79%)</b></td><td>0.04 <b>(+131.95%)</b></td><td>561.00 <b>(-33.25%)</b></td><td>427.18 <b>(-26.93%)</b></td><td>461.90 (-17.96%)</td><td>244.90 <b>(-41.36%)</b></td><td>144.02 (-8.52%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>840.40 (n/a)</td><td>584.58 (n/a)</td><td>563.00 (n/a)</td><td>417.60 (n/a)</td><td>157.43 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 <b>(+56.37%)</b></td><td>0.10 <b>(+30.18%)</b></td><td>0.11 <b>(+41.10%)</b></td><td>0.06 (-2.61%)</td><td>0.03 <b>(+294.24%)</b></td><td>533.70 (+2.67%)</td><td>364.44 (-16.87%)</td><td>292.00 <b>(-29.13%)</b></td><td>258.10 <b>(-36.05%)</b></td><td>126.14 <b>(+158.07%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>519.80 (n/a)</td><td>438.42 (n/a)</td><td>412.00 (n/a)</td><td>403.60 (n/a)</td><td>48.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 <b>(+25.51%)</b></td><td>0.12 (+14.86%)</td><td>0.13 (+16.87%)</td><td>0.07 (+5.92%)</td><td>0.04 <b>(+48.16%)</b></td><td>559.20 (-5.59%)</td><td>371.34 (-9.53%)</td><td>322.80 (-14.44%)</td><td>247.10 <b>(-20.34%)</b></td><td>134.18 (+13.58%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>592.30 (n/a)</td><td>410.44 (n/a)</td><td>377.30 (n/a)</td><td>310.20 (n/a)</td><td>118.13 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (-14.67%)</td><td>0.07 (-1.01%)</td><td>0.07 (-1.51%)</td><td>0.05 (+0.41%)</td><td>0.02 <b>(-29.11%)</b></td><td>671.70 (-0.40%)</td><td>470.82 (-2.55%)</td><td>475.80 (+1.54%)</td><td>337.00 (+17.18%)</td><td>128.03 (-17.01%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>674.40 (n/a)</td><td>483.12 (n/a)</td><td>468.60 (n/a)</td><td>287.60 (n/a)</td><td>154.27 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 <b>(+36.01%)</b></td><td>0.09 <b>(+39.22%)</b></td><td>0.07 (+3.71%)</td><td>0.06 <b>(+245.94%)</b></td><td>0.03 (+4.56%)</td><td>569.60 <b>(-71.09%)</b></td><td>445.06 <b>(-43.72%)</b></td><td>501.70 (-3.57%)</td><td>290.40 <b>(-26.48%)</b></td><td>129.14 <b>(-80.50%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1970.40 (n/a)</td><td>790.86 (n/a)</td><td>520.30 (n/a)</td><td>395.00 (n/a)</td><td>662.40 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 <b>(-23.54%)</b></td><td>0.07 <b>(-33.65%)</b></td><td>0.06 <b>(-48.42%)</b></td><td>0.03 <b>(-41.06%)</b></td><td>0.04 <b>(-26.17%)</b></td><td>1062.20 <b>(+69.65%)</b></td><td>585.58 <b>(+50.60%)</b></td><td>548.30 <b>(+93.88%)</b></td><td>257.00 <b>(+30.79%)</b></td><td>293.78 <b>(+49.56%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>626.10 (n/a)</td><td>388.84 (n/a)</td><td>282.80 (n/a)</td><td>196.50 (n/a)</td><td>196.42 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 (-6.44%)</td><td>0.09 (-0.10%)</td><td>0.08 (+11.33%)</td><td>0.06 (-0.29%)</td><td>0.03 (-13.33%)</td><td>634.20 (+0.30%)</td><td>467.10 (-1.97%)</td><td>473.10 (-10.19%)</td><td>280.70 (+6.85%)</td><td>145.80 (-7.41%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>632.30 (n/a)</td><td>476.48 (n/a)</td><td>526.80 (n/a)</td><td>262.70 (n/a)</td><td>157.46 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 <b>(-20.70%)</b></td><td>0.08 (+5.67%)</td><td>0.08 <b>(+26.06%)</b></td><td>0.07 (+14.56%)</td><td>0.02 <b>(-50.42%)</b></td><td>478.80 (-12.71%)</td><td>405.66 (-11.69%)</td><td>410.70 <b>(-20.67%)</b></td><td>301.60 <b>(+26.09%)</b></td><td>72.58 <b>(-43.44%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>548.50 (n/a)</td><td>459.34 (n/a)</td><td>517.70 (n/a)</td><td>239.20 (n/a)</td><td>128.31 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (-11.56%)</td><td>0.05 (-19.79%)</td><td>0.05 <b>(-22.90%)</b></td><td>0.01 <b>(-72.28%)</b></td><td>0.03 <b>(+38.79%)</b></td><td>1899.50 <b>(+260.71%)</b></td><td>689.62 <b>(+84.72%)</b></td><td>443.30 <b>(+29.70%)</b></td><td>275.00 (+13.08%)</td><td>683.95 <b>(+493.37%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>526.60 (n/a)</td><td>373.34 (n/a)</td><td>341.80 (n/a)</td><td>243.20 (n/a)</td><td>115.27 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (-5.85%)</td><td>0.05 <b>(-28.71%)</b></td><td>0.04 <b>(-46.49%)</b></td><td>0.03 <b>(-23.58%)</b></td><td>0.02 <b>(+25.47%)</b></td><td>636.10 <b>(+30.86%)</b></td><td>484.62 <b>(+47.86%)</b></td><td>544.40 <b>(+86.89%)</b></td><td>286.40 (+6.23%)</td><td>156.93 <b>(+73.16%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>486.10 (n/a)</td><td>327.76 (n/a)</td><td>291.30 (n/a)</td><td>269.60 (n/a)</td><td>90.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (-1.00%)</td><td>0.06 <b>(+23.57%)</b></td><td>0.06 <b>(+63.59%)</b></td><td>0.03 (-10.84%)</td><td>0.02 (-2.50%)</td><td>627.30 (+12.16%)</td><td>371.52 (-18.15%)</td><td>319.90 <b>(-38.87%)</b></td><td>232.50 (+1.00%)</td><td>156.73 (+17.37%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>559.30 (n/a)</td><td>453.88 (n/a)</td><td>523.30 (n/a)</td><td>230.20 (n/a)</td><td>133.54 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 <b>(-31.64%)</b></td><td>0.05 <b>(-20.83%)</b></td><td>0.05 (+8.17%)</td><td>0.01 <b>(-78.83%)</b></td><td>0.02 (-8.34%)</td><td>2512.70 <b>(+372.40%)</b></td><td>805.24 <b>(+102.91%)</b></td><td>439.60 (-7.55%)</td><td>297.60 <b>(+46.24%)</b></td><td>957.48 <b>(+576.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>531.90 (n/a)</td><td>396.84 (n/a)</td><td>475.50 (n/a)</td><td>203.50 (n/a)</td><td>141.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (-5.44%)</td><td>0.04 <b>(-28.12%)</b></td><td>0.04 <b>(-33.73%)</b></td><td>0.02 <b>(-57.92%)</b></td><td>0.02 <b>(+45.29%)</b></td><td>1091.40 <b>(+137.62%)</b></td><td>610.24 <b>(+62.02%)</b></td><td>582.20 <b>(+50.87%)</b></td><td>274.80 (+5.77%)</td><td>303.07 <b>(+253.61%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>459.30 (n/a)</td><td>376.64 (n/a)</td><td>385.90 (n/a)</td><td>259.80 (n/a)</td><td>85.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (+1.31%)</td><td>0.06 (-12.40%)</td><td>0.05 <b>(-35.96%)</b></td><td>0.04 (-6.34%)</td><td>0.02 (-14.71%)</td><td>543.80 (+6.75%)</td><td>387.80 (+10.79%)</td><td>397.40 <b>(+56.15%)</b></td><td>239.70 (-1.32%)</td><td>123.85 (-11.61%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>509.40 (n/a)</td><td>350.04 (n/a)</td><td>254.50 (n/a)</td><td>242.90 (n/a)</td><td>140.13 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 <b>(+33.97%)</b></td><td>0.08 <b>(+36.26%)</b></td><td>0.08 <b>(+37.35%)</b></td><td>0.05 (+11.06%)</td><td>0.02 <b>(+48.81%)</b></td><td>539.70 (-9.96%)</td><td>345.72 <b>(-24.84%)</b></td><td>290.70 <b>(-27.22%)</b></td><td>238.10 <b>(-25.36%)</b></td><td>123.37 (-5.53%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>599.40 (n/a)</td><td>459.98 (n/a)</td><td>399.40 (n/a)</td><td>319.00 (n/a)</td><td>130.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (+4.23%)</td><td>0.06 (-6.82%)</td><td>0.06 (+4.49%)</td><td>0.04 (+1.13%)</td><td>0.02 (+0.06%)</td><td>547.90 (-1.12%)</td><td>441.30 (+7.00%)</td><td>433.90 (-4.30%)</td><td>274.40 (-4.06%)</td><td>106.35 (-4.50%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>554.10 (n/a)</td><td>412.42 (n/a)</td><td>453.40 (n/a)</td><td>286.00 (n/a)</td><td>111.35 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (+9.39%)</td><td>0.05 (-17.89%)</td><td>0.05 (-18.93%)</td><td>0.01 <b>(-76.53%)</b></td><td>0.03 <b>(+66.45%)</b></td><td>2490.20 <b>(+326.11%)</b></td><td>869.72 <b>(+95.01%)</b></td><td>535.60 <b>(+23.32%)</b></td><td>262.10 (-8.58%)</td><td>913.62 <b>(+627.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>584.40 (n/a)</td><td>445.98 (n/a)</td><td>434.30 (n/a)</td><td>286.70 (n/a)</td><td>125.50 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (-9.02%)</td><td>0.06 (-5.64%)</td><td>0.05 (-13.80%)</td><td>0.04 (-6.30%)</td><td>0.02 (-2.91%)</td><td>551.40 (+6.74%)</td><td>426.84 (+7.00%)</td><td>459.80 (+15.99%)</td><td>262.00 (+9.95%)</td><td>134.63 (+14.00%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>516.60 (n/a)</td><td>398.90 (n/a)</td><td>396.40 (n/a)</td><td>238.30 (n/a)</td><td>118.09 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (+9.08%)</td><td>0.06 <b>(+21.10%)</b></td><td>0.05 (+12.93%)</td><td>0.05 <b>(+55.28%)</b></td><td>0.02 (-8.85%)</td><td>474.50 <b>(-35.60%)</b></td><td>400.72 <b>(-21.15%)</b></td><td>448.50 (-11.45%)</td><td>249.30 (-8.35%)</td><td>93.71 <b>(-43.17%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>736.80 (n/a)</td><td>508.20 (n/a)</td><td>506.50 (n/a)</td><td>272.00 (n/a)</td><td>164.90 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 <b>(+23.40%)</b></td><td>0.09 <b>(+42.76%)</b></td><td>0.10 <b>(+96.99%)</b></td><td>0.04 <b>(-20.07%)</b></td><td>0.04 <b>(+71.01%)</b></td><td>615.50 <b>(+25.10%)</b></td><td>337.86 <b>(-20.75%)</b></td><td>238.30 <b>(-49.24%)</b></td><td>197.10 (-18.96%)</td><td>180.97 <b>(+75.02%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>492.00 (n/a)</td><td>426.32 (n/a)</td><td>469.50 (n/a)</td><td>243.20 (n/a)</td><td>103.40 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 <b>(+77.35%)</b></td><td>0.05 <b>(+34.51%)</b></td><td>0.04 (-6.26%)</td><td>0.03 (-11.35%)</td><td>0.03 <b>(+453.82%)</b></td><td>596.30 (+12.81%)</td><td>405.12 (-11.41%)</td><td>492.20 (+6.68%)</td><td>214.90 <b>(-43.61%)</b></td><td>175.48 <b>(+230.20%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>528.60 (n/a)</td><td>457.28 (n/a)</td><td>461.40 (n/a)</td><td>381.10 (n/a)</td><td>53.14 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (-15.63%)</td><td>0.04 <b>(-25.38%)</b></td><td>0.03 <b>(-41.99%)</b></td><td>0.03 (-10.30%)</td><td>0.01 <b>(-22.87%)</b></td><td>569.00 (+11.48%)</td><td>474.46 <b>(+31.77%)</b></td><td>527.20 <b>(+72.34%)</b></td><td>295.90 (+18.50%)</td><td>118.37 (+1.65%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>510.40 (n/a)</td><td>360.08 (n/a)</td><td>305.90 (n/a)</td><td>249.70 (n/a)</td><td>116.44 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 (-1.51%)</td><td>0.05 (-13.12%)</td><td>0.04 (-8.93%)</td><td>0.03 (-5.01%)</td><td>0.02 (-18.49%)</td><td>604.30 (+5.28%)</td><td>442.76 (+10.45%)</td><td>465.50 (+9.81%)</td><td>238.00 (+1.54%)</td><td>139.64 (-12.25%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>574.00 (n/a)</td><td>400.86 (n/a)</td><td>423.90 (n/a)</td><td>234.40 (n/a)</td><td>159.13 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 <b>(+23.46%)</b></td><td>0.06 <b>(+26.62%)</b></td><td>0.06 <b>(+53.81%)</b></td><td>0.04 <b>(+41.57%)</b></td><td>0.01 (-2.98%)</td><td>444.80 <b>(-29.36%)</b></td><td>347.88 <b>(-23.65%)</b></td><td>320.50 <b>(-34.98%)</b></td><td>244.20 (-19.00%)</td><td>85.01 <b>(-39.78%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>629.70 (n/a)</td><td>455.64 (n/a)</td><td>492.90 (n/a)</td><td>301.50 (n/a)</td><td>141.16 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (-19.34%)</td><td>0.04 <b>(-26.05%)</b></td><td>0.04 <b>(-35.84%)</b></td><td>0.03 (-4.18%)</td><td>0.01 <b>(-36.07%)</b></td><td>594.40 (+4.37%)</td><td>441.22 <b>(+27.79%)</b></td><td>437.80 <b>(+55.86%)</b></td><td>278.10 <b>(+23.93%)</b></td><td>112.76 <b>(-21.05%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>569.50 (n/a)</td><td>345.28 (n/a)</td><td>280.90 (n/a)</td><td>224.40 (n/a)</td><td>142.82 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (-9.83%)</td><td>0.05 (+4.50%)</td><td>0.05 (+14.41%)</td><td>0.03 (+10.92%)</td><td>0.01 <b>(-28.59%)</b></td><td>573.30 (-9.84%)</td><td>409.08 (-9.62%)</td><td>373.90 (-12.60%)</td><td>270.70 (+10.90%)</td><td>112.96 <b>(-30.00%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>635.90 (n/a)</td><td>452.64 (n/a)</td><td>427.80 (n/a)</td><td>244.10 (n/a)</td><td>161.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.31 <b>(-20.38%)</b></td><td>0.23 <b>(-24.93%)</b></td><td>0.21 <b>(-40.71%)</b></td><td>0.16 <b>(+73.07%)</b></td><td>0.06 <b>(-52.72%)</b></td><td>605.70 <b>(-42.23%)</b></td><td>448.14 (+4.39%)</td><td>467.20 <b>(+68.66%)</b></td><td>313.40 <b>(+25.61%)</b></td><td>110.82 <b>(-68.05%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>0.12 (n/a)</td><td>1048.40 (n/a)</td><td>429.28 (n/a)</td><td>277.00 (n/a)</td><td>249.50 (n/a)</td><td>346.84 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.34 <b>(-22.41%)</b></td><td>0.25 <b>(-28.94%)</b></td><td>0.21 <b>(-45.90%)</b></td><td>0.18 <b>(-27.52%)</b></td><td>0.07 (-16.91%)</td><td>545.10 <b>(+37.97%)</b></td><td>425.46 <b>(+42.06%)</b></td><td>467.00 <b>(+84.80%)</b></td><td>289.10 <b>(+28.89%)</b></td><td>116.84 <b>(+40.91%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.39 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>395.10 (n/a)</td><td>299.50 (n/a)</td><td>252.70 (n/a)</td><td>224.30 (n/a)</td><td>82.92 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.36 (+17.55%)</td><td>0.22 (-7.10%)</td><td>0.21 (-7.37%)</td><td>0.09 <b>(-38.60%)</b></td><td>0.10 <b>(+59.88%)</b></td><td>1069.20 <b>(+62.86%)</b></td><td>548.10 <b>(+24.75%)</b></td><td>461.30 (+7.96%)</td><td>276.80 (-14.94%)</td><td>313.55 <b>(+132.86%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>656.50 (n/a)</td><td>439.36 (n/a)</td><td>427.30 (n/a)</td><td>325.40 (n/a)</td><td>134.65 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 <b>(-48.31%)</b></td><td>0.13 <b>(-48.52%)</b></td><td>0.13 <b>(-53.74%)</b></td><td>0.11 (-15.14%)</td><td>0.02 <b>(-69.13%)</b></td><td>654.30 (+17.85%)</td><td>562.64 <b>(+78.54%)</b></td><td>580.30 <b>(+116.13%)</b></td><td>426.00 <b>(+93.46%)</b></td><td>90.38 <b>(-34.05%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>555.20 (n/a)</td><td>315.14 (n/a)</td><td>268.50 (n/a)</td><td>220.20 (n/a)</td><td>137.04 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.32 <b>(+54.23%)</b></td><td>0.19 (+14.19%)</td><td>0.14 (-16.90%)</td><td>0.12 (+5.58%)</td><td>0.09 <b>(+119.80%)</b></td><td>607.80 (-5.28%)</td><td>446.98 (-4.02%)</td><td>538.30 <b>(+20.34%)</b></td><td>228.70 <b>(-35.16%)</b></td><td>164.20 <b>(+38.58%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>641.70 (n/a)</td><td>465.72 (n/a)</td><td>447.30 (n/a)</td><td>352.70 (n/a)</td><td>118.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.29 (-15.88%)</td><td>0.19 (-11.80%)</td><td>0.17 <b>(-26.93%)</b></td><td>0.12 (+13.55%)</td><td>0.07 <b>(-26.32%)</b></td><td>608.20 (-11.93%)</td><td>426.30 (+5.08%)</td><td>440.40 <b>(+36.86%)</b></td><td>255.00 (+18.88%)</td><td>147.69 <b>(-25.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.34 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>690.60 (n/a)</td><td>405.70 (n/a)</td><td>321.80 (n/a)</td><td>214.50 (n/a)</td><td>198.71 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (+1.23%)</td><td>0.08 <b>(-29.67%)</b></td><td>0.07 <b>(-38.39%)</b></td><td>0.02 <b>(-72.20%)</b></td><td>0.06 <b>(+88.12%)</b></td><td>1937.90 <b>(+259.74%)</b></td><td>984.76 <b>(+171.48%)</b></td><td>504.90 <b>(+62.30%)</b></td><td>242.10 (-1.22%)</td><td>875.31 <b>(+649.40%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>538.70 (n/a)</td><td>362.74 (n/a)</td><td>311.10 (n/a)</td><td>245.10 (n/a)</td><td>116.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 (-10.04%)</td><td>0.11 (+6.64%)</td><td>0.12 <b>(+40.44%)</b></td><td>0.08 <b>(+35.25%)</b></td><td>0.02 <b>(-41.55%)</b></td><td>487.60 <b>(-26.05%)</b></td><td>364.54 (-14.39%)</td><td>311.60 <b>(-28.79%)</b></td><td>285.10 (+11.15%)</td><td>88.78 <b>(-48.02%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>659.40 (n/a)</td><td>425.80 (n/a)</td><td>437.60 (n/a)</td><td>256.50 (n/a)</td><td>170.80 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (-14.49%)</td><td>0.09 <b>(-21.05%)</b></td><td>0.08 <b>(-39.71%)</b></td><td>0.07 <b>(+263.59%)</b></td><td>0.02 <b>(-57.28%)</b></td><td>538.90 <b>(-72.50%)</b></td><td>451.70 <b>(-27.54%)</b></td><td>457.70 <b>(+65.83%)</b></td><td>295.70 (+16.92%)</td><td>96.82 <b>(-87.07%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1959.60 (n/a)</td><td>623.40 (n/a)</td><td>276.00 (n/a)</td><td>252.90 (n/a)</td><td>748.58 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 <b>(+35.01%)</b></td><td>0.11 <b>(+40.14%)</b></td><td>0.12 <b>(+81.31%)</b></td><td>0.07 <b>(+62.94%)</b></td><td>0.04 <b>(+22.34%)</b></td><td>503.20 <b>(-38.63%)</b></td><td>356.16 <b>(-30.65%)</b></td><td>299.90 <b>(-44.84%)</b></td><td>222.70 <b>(-25.94%)</b></td><td>126.24 <b>(-38.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>819.90 (n/a)</td><td>513.60 (n/a)</td><td>543.70 (n/a)</td><td>300.70 (n/a)</td><td>206.39 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (-6.10%)</td><td>0.09 (-17.91%)</td><td>0.06 <b>(-42.47%)</b></td><td>0.06 <b>(-24.88%)</b></td><td>0.04 <b>(+28.98%)</b></td><td>612.60 <b>(+33.12%)</b></td><td>464.20 <b>(+32.00%)</b></td><td>571.50 <b>(+73.81%)</b></td><td>252.50 (+6.50%)</td><td>176.00 <b>(+79.58%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>460.20 (n/a)</td><td>351.66 (n/a)</td><td>328.80 (n/a)</td><td>237.10 (n/a)</td><td>98.01 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (-0.32%)</td><td>0.09 (+3.00%)</td><td>0.08 <b>(+20.36%)</b></td><td>0.07 (+10.16%)</td><td>0.03 (-11.52%)</td><td>567.00 (-9.24%)</td><td>444.98 (-6.07%)</td><td>451.80 (-16.92%)</td><td>257.80 (+0.35%)</td><td>129.53 (-19.58%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>624.70 (n/a)</td><td>473.72 (n/a)</td><td>543.80 (n/a)</td><td>256.90 (n/a)</td><td>161.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 (+10.00%)</td><td>0.10 (+3.49%)</td><td>0.09 (+3.36%)</td><td>0.08 (+16.37%)</td><td>0.04 (+4.47%)</td><td>503.00 (-14.06%)</td><td>418.26 (-4.51%)</td><td>470.70 (-3.25%)</td><td>246.70 (-9.10%)</td><td>104.56 (-19.10%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>585.30 (n/a)</td><td>438.00 (n/a)</td><td>486.50 (n/a)</td><td>271.40 (n/a)</td><td>129.25 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 (-19.89%)</td><td>0.09 <b>(-22.73%)</b></td><td>0.08 <b>(-35.12%)</b></td><td>0.08 (-3.49%)</td><td>0.02 <b>(-35.07%)</b></td><td>518.40 (+3.62%)</td><td>452.92 <b>(+25.95%)</b></td><td>504.80 <b>(+54.14%)</b></td><td>319.50 <b>(+24.80%)</b></td><td>85.21 (-16.08%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>500.30 (n/a)</td><td>359.60 (n/a)</td><td>327.50 (n/a)</td><td>256.00 (n/a)</td><td>101.53 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (-15.52%)</td><td>0.09 <b>(-20.42%)</b></td><td>0.09 (+5.48%)</td><td>0.02 <b>(-75.08%)</b></td><td>0.04 <b>(+22.71%)</b></td><td>1965.20 <b>(+301.31%)</b></td><td>722.20 <b>(+80.08%)</b></td><td>436.90 (-5.19%)</td><td>295.70 (+18.37%)</td><td>699.66 <b>(+545.92%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>489.70 (n/a)</td><td>401.04 (n/a)</td><td>460.80 (n/a)</td><td>249.80 (n/a)</td><td>108.32 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.16 <b>(+77.19%)</b></td><td>0.13 <b>(+91.65%)</b></td><td>0.15 <b>(+84.84%)</b></td><td>0.06 <b>(+259.20%)</b></td><td>0.04 <b>(+37.44%)</b></td><td>678.40 <b>(-72.16%)</b></td><td>349.30 <b>(-60.33%)</b></td><td>272.70 <b>(-45.90%)</b></td><td>253.00 <b>(-43.56%)</b></td><td>184.22 <b>(-78.85%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>2437.00 (n/a)</td><td>880.54 (n/a)</td><td>504.10 (n/a)</td><td>448.30 (n/a)</td><td>870.88 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 <b>(-35.77%)</b></td><td>0.11 (-15.68%)</td><td>0.10 (-3.49%)</td><td>0.09 <b>(+35.28%)</b></td><td>0.02 <b>(-64.21%)</b></td><td>447.60 <b>(-26.08%)</b></td><td>394.98 (+1.65%)</td><td>420.80 (+3.62%)</td><td>276.30 <b>(+55.66%)</b></td><td>69.07 <b>(-59.00%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>605.50 (n/a)</td><td>388.58 (n/a)</td><td>406.10 (n/a)</td><td>177.50 (n/a)</td><td>168.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (+18.03%)</td><td>0.11 <b>(+21.66%)</b></td><td>0.09 (+9.16%)</td><td>0.09 <b>(+33.75%)</b></td><td>0.03 (+13.88%)</td><td>475.70 <b>(-25.23%)</b></td><td>396.38 (-18.49%)</td><td>438.00 (-8.39%)</td><td>271.40 (-15.29%)</td><td>91.99 <b>(-26.27%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>636.20 (n/a)</td><td>486.30 (n/a)</td><td>478.10 (n/a)</td><td>320.40 (n/a)</td><td>124.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (-18.92%)</td><td>0.09 (-16.98%)</td><td>0.11 (+3.22%)</td><td>0.06 <b>(-25.03%)</b></td><td>0.03 <b>(+27.57%)</b></td><td>556.20 <b>(+33.38%)</b></td><td>401.14 <b>(+27.21%)</b></td><td>309.10 (-3.13%)</td><td>295.70 <b>(+23.31%)</b></td><td>138.03 <b>(+109.43%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>417.00 (n/a)</td><td>315.34 (n/a)</td><td>319.10 (n/a)</td><td>239.80 (n/a)</td><td>65.91 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (+9.98%)</td><td>0.10 (+7.77%)</td><td>0.10 (+5.18%)</td><td>0.07 (+3.46%)</td><td>0.03 (+11.03%)</td><td>527.30 (-3.34%)</td><td>375.52 (-6.89%)</td><td>351.90 (-4.92%)</td><td>232.40 (-9.08%)</td><td>117.92 (-5.30%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>545.50 (n/a)</td><td>403.32 (n/a)</td><td>370.10 (n/a)</td><td>255.60 (n/a)</td><td>124.52 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (-14.32%)</td><td>0.09 (+14.14%)</td><td>0.08 (+1.20%)</td><td>0.07 <b>(+71.28%)</b></td><td>0.02 <b>(-38.05%)</b></td><td>467.70 <b>(-41.61%)</b></td><td>390.02 <b>(-20.67%)</b></td><td>437.00 (-1.20%)</td><td>294.40 (+16.73%)</td><td>84.88 <b>(-58.17%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>801.00 (n/a)</td><td>491.66 (n/a)</td><td>442.30 (n/a)</td><td>252.20 (n/a)</td><td>202.91 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 <b>(-36.91%)</b></td><td>0.07 <b>(-24.76%)</b></td><td>0.07 (-5.84%)</td><td>0.05 (+1.48%)</td><td>0.01 <b>(-71.44%)</b></td><td>655.00 (-1.44%)</td><td>539.88 (+19.98%)</td><td>524.00 (+6.20%)</td><td>435.70 <b>(+58.49%)</b></td><td>79.41 <b>(-52.25%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>664.60 (n/a)</td><td>449.96 (n/a)</td><td>493.40 (n/a)</td><td>274.90 (n/a)</td><td>166.31 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (-9.13%)</td><td>0.09 (-9.76%)</td><td>0.07 <b>(-40.03%)</b></td><td>0.05 (+16.00%)</td><td>0.04 <b>(-22.87%)</b></td><td>647.90 (-13.79%)</td><td>422.34 (-0.68%)</td><td>469.70 <b>(+66.80%)</b></td><td>232.50 (+10.03%)</td><td>164.80 <b>(-31.91%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>751.50 (n/a)</td><td>425.22 (n/a)</td><td>281.60 (n/a)</td><td>211.30 (n/a)</td><td>242.04 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 <b>(-35.21%)</b></td><td>0.07 (+1.25%)</td><td>0.07 (-9.39%)</td><td>0.06 <b>(+346.64%)</b></td><td>0.01 <b>(-80.36%)</b></td><td>539.60 <b>(-77.61%)</b></td><td>476.50 <b>(-42.89%)</b></td><td>486.30 (+10.37%)</td><td>395.80 <b>(+54.37%)</b></td><td>52.03 <b>(-94.16%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2410.20 (n/a)</td><td>834.38 (n/a)</td><td>440.60 (n/a)</td><td>256.40 (n/a)</td><td>890.75 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.55 (+11.44%)</td><td>0.46 <b>(+31.26%)</b></td><td>0.44 <b>(+45.97%)</b></td><td>0.42 <b>(+83.36%)</b></td><td>0.06 <b>(-50.96%)</b></td><td>314.30 <b>(-45.46%)</b></td><td>287.34 <b>(-29.11%)</b></td><td>301.30 <b>(-31.49%)</b></td><td>239.50 (-10.27%)</td><td>32.15 <b>(-74.76%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.49 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>576.30 (n/a)</td><td>405.32 (n/a)</td><td>439.80 (n/a)</td><td>266.90 (n/a)</td><td>127.37 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.50 (-18.84%)</td><td>0.46 (+18.43%)</td><td>0.49 (+17.76%)</td><td>0.42 <b>(+83.27%)</b></td><td>0.04 <b>(-76.00%)</b></td><td>310.40 <b>(-45.44%)</b></td><td>283.94 <b>(-26.23%)</b></td><td>269.60 (-15.06%)</td><td>263.10 <b>(+23.17%)</b></td><td>24.17 <b>(-84.84%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.61 (n/a)</td><td>0.39 (n/a)</td><td>0.41 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>568.90 (n/a)</td><td>384.92 (n/a)</td><td>317.40 (n/a)</td><td>213.60 (n/a)</td><td>159.49 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.47 (+3.23%)</td><td>0.31 (-16.65%)</td><td>0.29 <b>(-32.38%)</b></td><td>0.25 (-2.72%)</td><td>0.09 (-6.86%)</td><td>527.20 (+2.79%)</td><td>439.68 (+18.90%)</td><td>449.70 <b>(+47.88%)</b></td><td>280.60 (-3.11%)</td><td>94.87 (-9.15%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.45 (n/a)</td><td>0.38 (n/a)</td><td>0.43 (n/a)</td><td>0.26 (n/a)</td><td>0.09 (n/a)</td><td>512.90 (n/a)</td><td>369.80 (n/a)</td><td>304.10 (n/a)</td><td>289.60 (n/a)</td><td>104.42 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.00 (+14.29%)</td><td>0.00 (+5.88%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+25.75%)</b></td><td>21243.41 (-3.33%)</td><td>15385.94 (-0.56%)</td><td>18935.86 (+16.64%)</td><td>5364.12 (-9.67%)</td><td>6835.82 (+8.71%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21974.63 (n/a)</td><td>15471.84 (n/a)</td><td>16234.94 (n/a)</td><td>5938.26 (n/a)</td><td>6288.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 (-0.84%)</td><td>20013.74 (-10.70%)</td><td>13185.76 (-2.20%)</td><td>16384.24 <b>(+22.58%)</b></td><td>5486.26 (-0.50%)</td><td>6985.77 (-11.49%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22411.25 (n/a)</td><td>13482.99 (n/a)</td><td>13366.10 (n/a)</td><td>5514.06 (n/a)</td><td>7892.39 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (-12.55%)</td><td>0.09 (-15.79%)</td><td>0.08 (-19.41%)</td><td>0.08 (+7.52%)</td><td>0.02 <b>(-37.50%)</b></td><td>27652.54 (-7.08%)</td><td>24536.30 (+14.31%)</td><td>25515.81 <b>(+24.08%)</b></td><td>17511.68 (+14.41%)</td><td>4118.96 <b>(-33.60%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29758.52 (n/a)</td><td>21463.81 (n/a)</td><td>20563.97 (n/a)</td><td>15306.58 (n/a)</td><td>6203.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>2.72 (-5.32%)</td><td>1.79 (-2.96%)</td><td>1.83 (+9.94%)</td><td>1.17 (+0.84%)</td><td>0.64 (+0.92%)</td><td>893.10 (-0.83%)</td><td>648.00 (+4.66%)</td><td>572.10 (-9.05%)</td><td>385.80 (+5.61%)</td><td>222.03 (+15.50%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>2.87 (n/a)</td><td>1.84 (n/a)</td><td>1.67 (n/a)</td><td>1.16 (n/a)</td><td>0.63 (n/a)</td><td>900.60 (n/a)</td><td>619.16 (n/a)</td><td>629.00 (n/a)</td><td>365.30 (n/a)</td><td>192.24 (n/a)</td>
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
