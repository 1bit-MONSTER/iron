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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (+8.99%)</td><td>0.02 (-13.36%)</td><td>0.02 <b>(-35.87%)</b></td><td>0.01 (-16.73%)</td><td>0.01 <b>(+96.07%)</b></td><td>472.00 <b>(+20.07%)</b></td><td>357.58 <b>(+26.26%)</b></td><td>405.80 <b>(+55.96%)</b></td><td>218.60 (-8.23%)</td><td>128.01 <b>(+103.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>393.10 (n/a)</td><td>283.20 (n/a)</td><td>260.20 (n/a)</td><td>238.20 (n/a)</td><td>62.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (+3.62%)</td><td>0.02 (+1.73%)</td><td>0.02 (-0.48%)</td><td>0.01 (+6.36%)</td><td>0.01 (-1.09%)</td><td>482.40 (-5.98%)</td><td>328.86 (-2.51%)</td><td>279.30 (+0.50%)</td><td>227.80 (-3.47%)</td><td>102.41 (-9.81%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>513.10 (n/a)</td><td>337.34 (n/a)</td><td>277.90 (n/a)</td><td>236.00 (n/a)</td><td>113.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (+12.02%)</td><td>0.02 (+8.74%)</td><td>0.02 (+19.00%)</td><td>0.01 (-9.56%)</td><td>0.01 <b>(+42.80%)</b></td><td>478.80 (+10.58%)</td><td>319.74 (-3.04%)</td><td>246.20 (-15.94%)</td><td>210.00 (-10.71%)</td><td>122.84 <b>(+38.37%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>433.00 (n/a)</td><td>329.78 (n/a)</td><td>292.90 (n/a)</td><td>235.20 (n/a)</td><td>88.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(-25.68%)</b></td><td>0.02 (+5.68%)</td><td>0.02 (+19.19%)</td><td>0.01 (-4.07%)</td><td>0.01 <b>(-31.04%)</b></td><td>578.10 (+4.24%)</td><td>333.24 (-8.32%)</td><td>279.50 (-16.12%)</td><td>261.90 <b>(+34.51%)</b></td><td>137.15 (+0.46%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.60 (n/a)</td><td>363.48 (n/a)</td><td>333.20 (n/a)</td><td>194.70 (n/a)</td><td>136.52 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (-1.04%)</td><td>0.02 (+14.21%)</td><td>0.02 <b>(+33.66%)</b></td><td>0.01 <b>(+31.46%)</b></td><td>0.00 <b>(-30.59%)</b></td><td>485.90 <b>(-23.92%)</b></td><td>367.10 (-17.30%)</td><td>349.20 <b>(-25.19%)</b></td><td>292.90 (+1.03%)</td><td>82.11 <b>(-44.80%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.70 (n/a)</td><td>443.92 (n/a)</td><td>466.80 (n/a)</td><td>289.90 (n/a)</td><td>148.74 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (+5.72%)</td><td>0.02 (+15.98%)</td><td>0.02 <b>(+27.25%)</b></td><td>0.01 <b>(+41.12%)</b></td><td>0.01 (-9.70%)</td><td>536.90 <b>(-29.14%)</b></td><td>382.88 <b>(-20.22%)</b></td><td>393.30 <b>(-21.42%)</b></td><td>228.80 (-5.38%)</td><td>137.97 <b>(-37.33%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>757.70 (n/a)</td><td>479.90 (n/a)</td><td>500.50 (n/a)</td><td>241.80 (n/a)</td><td>220.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (-1.08%)</td><td>0.04 <b>(+21.07%)</b></td><td>0.03 <b>(+36.17%)</b></td><td>0.02 (+4.51%)</td><td>0.02 (-6.27%)</td><td>578.70 (-4.32%)</td><td>356.38 (-19.09%)</td><td>352.50 <b>(-26.56%)</b></td><td>197.50 (+1.13%)</td><td>149.73 (-7.09%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>604.80 (n/a)</td><td>440.44 (n/a)</td><td>480.00 (n/a)</td><td>195.30 (n/a)</td><td>161.16 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (+0.39%)</td><td>0.05 <b>(+40.19%)</b></td><td>0.05 <b>(+93.43%)</b></td><td>0.02 (-6.15%)</td><td>0.01 (+10.73%)</td><td>552.10 (+6.54%)</td><td>302.38 <b>(-26.61%)</b></td><td>241.90 <b>(-48.30%)</b></td><td>235.20 (-0.38%)</td><td>139.68 <b>(+20.86%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.20 (n/a)</td><td>412.00 (n/a)</td><td>467.90 (n/a)</td><td>236.10 (n/a)</td><td>115.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (-4.15%)</td><td>0.03 (-7.97%)</td><td>0.03 <b>(-23.32%)</b></td><td>0.02 (-4.69%)</td><td>0.01 (+11.98%)</td><td>600.60 (+4.93%)</td><td>427.96 (+12.50%)</td><td>463.60 <b>(+30.41%)</b></td><td>241.00 (+4.33%)</td><td>158.57 <b>(+21.42%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.40 (n/a)</td><td>380.40 (n/a)</td><td>355.50 (n/a)</td><td>231.00 (n/a)</td><td>130.59 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 <b>(-25.08%)</b></td><td>0.03 <b>(-22.99%)</b></td><td>0.03 <b>(+22.70%)</b></td><td>0.01 <b>(-72.04%)</b></td><td>0.02 <b>(-21.12%)</b></td><td>2435.40 <b>(+257.67%)</b></td><td>820.74 <b>(+83.74%)</b></td><td>440.60 (-18.51%)</td><td>256.00 <b>(+33.47%)</b></td><td>908.63 <b>(+345.05%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>680.90 (n/a)</td><td>446.68 (n/a)</td><td>540.70 (n/a)</td><td>191.80 (n/a)</td><td>204.16 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (-15.34%)</td><td>0.02 (-3.68%)</td><td>0.03 (+15.92%)</td><td>0.01 <b>(-56.89%)</b></td><td>0.01 (+12.61%)</td><td>1853.70 <b>(+131.97%)</b></td><td>709.76 <b>(+35.18%)</b></td><td>435.50 (-13.73%)</td><td>344.90 (+18.12%)</td><td>642.14 <b>(+254.94%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>799.10 (n/a)</td><td>525.06 (n/a)</td><td>504.80 (n/a)</td><td>292.00 (n/a)</td><td>180.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 <b>(+47.97%)</b></td><td>0.03 (-8.84%)</td><td>0.02 <b>(-34.15%)</b></td><td>0.01 <b>(-75.65%)</b></td><td>0.02 <b>(+247.52%)</b></td><td>1951.90 <b>(+310.75%)</b></td><td>764.64 <b>(+89.96%)</b></td><td>633.90 <b>(+51.83%)</b></td><td>208.30 <b>(-32.44%)</b></td><td>699.85 <b>(+842.74%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>475.20 (n/a)</td><td>402.52 (n/a)</td><td>417.50 (n/a)</td><td>308.30 (n/a)</td><td>74.24 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 <b>(+23.51%)</b></td><td>0.08 (+13.22%)</td><td>0.08 <b>(+27.02%)</b></td><td>0.05 (-0.99%)</td><td>0.03 (+15.87%)</td><td>501.50 (+0.99%)</td><td>321.42 (-10.78%)</td><td>308.80 <b>(-21.26%)</b></td><td>190.20 (-19.06%)</td><td>117.26 (+0.41%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>496.60 (n/a)</td><td>360.24 (n/a)</td><td>392.20 (n/a)</td><td>235.00 (n/a)</td><td>116.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (+14.10%)</td><td>0.08 (-3.45%)</td><td>0.08 (-3.30%)</td><td>0.04 (-1.87%)</td><td>0.03 <b>(+55.54%)</b></td><td>564.40 (+1.90%)</td><td>377.62 (+11.86%)</td><td>300.90 (+3.44%)</td><td>228.50 (-12.38%)</td><td>166.94 <b>(+37.09%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>553.90 (n/a)</td><td>337.58 (n/a)</td><td>290.90 (n/a)</td><td>260.80 (n/a)</td><td>121.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 <b>(-35.96%)</b></td><td>0.05 <b>(-32.40%)</b></td><td>0.05 <b>(-43.77%)</b></td><td>0.04 (+4.51%)</td><td>0.01 <b>(-68.35%)</b></td><td>583.90 (-4.31%)</td><td>475.28 <b>(+28.77%)</b></td><td>489.90 <b>(+77.82%)</b></td><td>356.60 <b>(+56.13%)</b></td><td>84.29 <b>(-52.02%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>610.20 (n/a)</td><td>369.10 (n/a)</td><td>275.50 (n/a)</td><td>228.40 (n/a)</td><td>175.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (-19.08%)</td><td>0.07 <b>(-26.44%)</b></td><td>0.06 <b>(-35.56%)</b></td><td>0.04 (-15.95%)</td><td>0.03 (-6.24%)</td><td>626.30 (+18.96%)</td><td>419.22 <b>(+39.61%)</b></td><td>423.40 <b>(+55.21%)</b></td><td>224.70 <b>(+23.60%)</b></td><td>169.26 <b>(+28.18%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>526.50 (n/a)</td><td>300.28 (n/a)</td><td>272.80 (n/a)</td><td>181.80 (n/a)</td><td>132.05 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (-3.68%)</td><td>0.06 <b>(-35.33%)</b></td><td>0.05 <b>(-51.21%)</b></td><td>0.04 <b>(-25.85%)</b></td><td>0.03 <b>(+27.45%)</b></td><td>627.90 <b>(+34.86%)</b></td><td>477.68 <b>(+67.58%)</b></td><td>512.70 <b>(+105.00%)</b></td><td>204.40 (+3.86%)</td><td>167.78 <b>(+59.53%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>465.60 (n/a)</td><td>285.04 (n/a)</td><td>250.10 (n/a)</td><td>196.80 (n/a)</td><td>105.17 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (-3.71%)</td><td>0.07 (+4.49%)</td><td>0.06 (+19.75%)</td><td>0.04 (+13.18%)</td><td>0.02 <b>(-25.58%)</b></td><td>567.10 (-11.64%)</td><td>385.80 (-11.35%)</td><td>400.50 (-16.49%)</td><td>249.90 (+3.87%)</td><td>128.01 <b>(-29.75%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>641.80 (n/a)</td><td>435.18 (n/a)</td><td>479.60 (n/a)</td><td>240.60 (n/a)</td><td>182.22 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.20 (+6.80%)</td><td>0.15 <b>(+50.31%)</b></td><td>0.18 <b>(+93.39%)</b></td><td>0.09 <b>(+379.76%)</b></td><td>0.05 (-18.56%)</td><td>520.60 <b>(-79.16%)</b></td><td>360.74 <b>(-58.10%)</b></td><td>279.00 <b>(-48.29%)</b></td><td>240.60 (-6.34%)</td><td>134.86 <b>(-85.41%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2497.70 (n/a)</td><td>860.88 (n/a)</td><td>539.50 (n/a)</td><td>256.90 (n/a)</td><td>924.34 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.19 (+8.08%)</td><td>0.14 (+2.46%)</td><td>0.17 <b>(+30.83%)</b></td><td>0.08 <b>(-33.27%)</b></td><td>0.06 <b>(+121.92%)</b></td><td>647.60 <b>(+49.87%)</b></td><td>405.76 (+11.41%)</td><td>295.50 <b>(-23.56%)</b></td><td>254.90 (-7.48%)</td><td>187.07 <b>(+210.30%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>432.10 (n/a)</td><td>364.20 (n/a)</td><td>386.60 (n/a)</td><td>275.50 (n/a)</td><td>60.29 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.21 <b>(+25.59%)</b></td><td>0.15 <b>(+20.30%)</b></td><td>0.16 <b>(+24.02%)</b></td><td>0.09 (+7.84%)</td><td>0.05 <b>(+68.76%)</b></td><td>522.10 (-7.26%)</td><td>359.44 (-11.81%)</td><td>299.20 (-19.37%)</td><td>236.00 <b>(-20.38%)</b></td><td>138.49 <b>(+25.88%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>563.00 (n/a)</td><td>407.58 (n/a)</td><td>371.10 (n/a)</td><td>296.40 (n/a)</td><td>110.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.20 (+3.44%)</td><td>0.13 (+18.69%)</td><td>0.11 (+18.91%)</td><td>0.09 <b>(+282.01%)</b></td><td>0.04 <b>(-30.74%)</b></td><td>549.40 <b>(-73.82%)</b></td><td>415.28 <b>(-45.19%)</b></td><td>443.70 (-15.90%)</td><td>245.20 (-3.35%)</td><td>118.60 <b>(-84.41%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2098.80 (n/a)</td><td>757.72 (n/a)</td><td>527.60 (n/a)</td><td>253.70 (n/a)</td><td>760.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.22 (+2.20%)</td><td>0.13 <b>(-27.96%)</b></td><td>0.11 <b>(-45.18%)</b></td><td>0.03 <b>(-71.86%)</b></td><td>0.08 <b>(+51.31%)</b></td><td>1961.40 <b>(+255.33%)</b></td><td>682.48 <b>(+119.84%)</b></td><td>462.40 <b>(+82.48%)</b></td><td>226.60 (-2.16%)</td><td>724.78 <b>(+432.14%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>552.00 (n/a)</td><td>310.44 (n/a)</td><td>253.40 (n/a)</td><td>231.60 (n/a)</td><td>136.20 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.26 (-3.62%)</td><td>0.14 (-15.14%)</td><td>0.10 <b>(-45.09%)</b></td><td>0.07 <b>(-34.20%)</b></td><td>0.08 <b>(+24.79%)</b></td><td>700.90 <b>(+51.97%)</b></td><td>437.54 <b>(+34.03%)</b></td><td>510.40 <b>(+82.09%)</b></td><td>188.80 (+3.74%)</td><td>214.23 <b>(+81.36%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>461.20 (n/a)</td><td>326.44 (n/a)</td><td>280.30 (n/a)</td><td>182.00 (n/a)</td><td>118.13 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (+2.98%)</td><td>0.01 (-1.46%)</td><td>0.01 (+1.98%)</td><td>0.01 <b>(+56.35%)</b></td><td>0.00 (-8.06%)</td><td>488.40 <b>(-36.04%)</b></td><td>351.36 (-6.37%)</td><td>291.00 (-1.92%)</td><td>226.30 (-2.88%)</td><td>120.21 <b>(-45.04%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>763.60 (n/a)</td><td>375.28 (n/a)</td><td>296.70 (n/a)</td><td>233.00 (n/a)</td><td>218.72 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (+15.41%)</td><td>0.01 <b>(+20.61%)</b></td><td>0.01 (+17.73%)</td><td>0.01 (+4.22%)</td><td>0.00 (+12.65%)</td><td>465.30 (-4.04%)</td><td>311.82 (-16.79%)</td><td>290.90 (-15.07%)</td><td>241.70 (-13.34%)</td><td>88.24 (-3.67%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>484.90 (n/a)</td><td>374.74 (n/a)</td><td>342.50 (n/a)</td><td>278.90 (n/a)</td><td>91.60 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 <b>(+43.13%)</b></td><td>0.01 (+13.65%)</td><td>0.01 (-3.85%)</td><td>0.00 <b>(+34.32%)</b></td><td>0.00 <b>(+50.16%)</b></td><td>558.90 <b>(-25.55%)</b></td><td>402.90 (-10.05%)</td><td>462.00 (+4.01%)</td><td>200.70 <b>(-30.12%)</b></td><td>146.76 <b>(-21.08%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>750.70 (n/a)</td><td>447.90 (n/a)</td><td>444.20 (n/a)</td><td>287.20 (n/a)</td><td>185.96 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 <b>(+30.28%)</b></td><td>0.01 <b>(+28.91%)</b></td><td>0.01 <b>(+41.71%)</b></td><td>0.01 <b>(+21.74%)</b></td><td>0.00 <b>(+47.02%)</b></td><td>518.30 (-17.85%)</td><td>391.08 <b>(-21.30%)</b></td><td>354.00 <b>(-29.44%)</b></td><td>273.80 <b>(-23.24%)</b></td><td>97.48 (-4.22%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>630.90 (n/a)</td><td>496.94 (n/a)</td><td>501.70 (n/a)</td><td>356.70 (n/a)</td><td>101.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 <b>(-24.98%)</b></td><td>0.01 (+0.58%)</td><td>0.01 (-0.05%)</td><td>0.00 <b>(+234.69%)</b></td><td>0.00 <b>(-77.18%)</b></td><td>555.90 <b>(-70.12%)</b></td><td>467.46 <b>(-33.15%)</b></td><td>457.90 (+0.07%)</td><td>407.30 <b>(+33.28%)</b></td><td>54.86 <b>(-91.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1860.40 (n/a)</td><td>699.22 (n/a)</td><td>457.60 (n/a)</td><td>305.60 (n/a)</td><td>654.45 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (+15.47%)</td><td>0.01 <b>(+20.68%)</b></td><td>0.00 (+8.25%)</td><td>0.00 <b>(+75.68%)</b></td><td>0.00 (-5.82%)</td><td>587.80 <b>(-43.08%)</b></td><td>490.12 <b>(-21.31%)</b></td><td>526.20 (-7.62%)</td><td>369.60 (-13.40%)</td><td>106.46 <b>(-55.64%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1032.60 (n/a)</td><td>622.84 (n/a)</td><td>569.60 (n/a)</td><td>426.80 (n/a)</td><td>239.97 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (-9.96%)</td><td>0.01 (-0.76%)</td><td>0.01 (-13.34%)</td><td>0.01 (+15.14%)</td><td>0.01 (-7.22%)</td><td>524.40 (-13.15%)</td><td>391.06 (-0.92%)</td><td>414.30 (+15.40%)</td><td>247.90 (+11.07%)</td><td>130.26 (-12.15%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.80 (n/a)</td><td>394.70 (n/a)</td><td>359.00 (n/a)</td><td>223.20 (n/a)</td><td>148.27 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (-14.87%)</td><td>0.02 (-4.70%)</td><td>0.01 <b>(-26.12%)</b></td><td>0.01 (+11.26%)</td><td>0.01 (-19.55%)</td><td>543.90 (-10.11%)</td><td>374.76 (-2.49%)</td><td>403.70 <b>(+35.38%)</b></td><td>215.10 (+17.48%)</td><td>143.51 <b>(-24.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.10 (n/a)</td><td>384.32 (n/a)</td><td>298.20 (n/a)</td><td>183.10 (n/a)</td><td>191.12 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (-10.73%)</td><td>0.01 (+5.14%)</td><td>0.01 <b>(+45.26%)</b></td><td>0.01 (+19.12%)</td><td>0.00 <b>(-30.83%)</b></td><td>530.80 (-16.05%)</td><td>385.72 (-13.48%)</td><td>376.00 <b>(-31.16%)</b></td><td>235.90 (+12.01%)</td><td>119.95 <b>(-34.72%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>632.30 (n/a)</td><td>445.84 (n/a)</td><td>546.20 (n/a)</td><td>210.60 (n/a)</td><td>183.76 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (-1.49%)</td><td>0.01 (-11.04%)</td><td>0.01 (+3.35%)</td><td>0.01 <b>(-32.47%)</b></td><td>0.00 <b>(+39.24%)</b></td><td>617.30 <b>(+48.10%)</b></td><td>419.12 <b>(+20.41%)</b></td><td>363.10 (-3.25%)</td><td>258.70 (+1.49%)</td><td>153.68 <b>(+114.25%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>416.80 (n/a)</td><td>348.08 (n/a)</td><td>375.30 (n/a)</td><td>254.90 (n/a)</td><td>71.73 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (+3.50%)</td><td>0.01 (-12.34%)</td><td>0.02 (+2.44%)</td><td>0.00 <b>(-55.53%)</b></td><td>0.01 <b>(+34.36%)</b></td><td>1334.80 <b>(+124.87%)</b></td><td>548.54 <b>(+50.83%)</b></td><td>296.40 (-2.37%)</td><td>234.30 (-3.38%)</td><td>460.98 <b>(+208.29%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.60 (n/a)</td><td>363.68 (n/a)</td><td>303.60 (n/a)</td><td>242.50 (n/a)</td><td>149.53 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (-16.53%)</td><td>0.01 (-19.25%)</td><td>0.01 <b>(-21.50%)</b></td><td>0.01 (-6.12%)</td><td>0.00 (-17.52%)</td><td>591.20 (+6.52%)</td><td>483.90 <b>(+22.53%)</b></td><td>538.90 <b>(+27.40%)</b></td><td>260.00 (+19.82%)</td><td>130.14 (+4.14%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.00 (n/a)</td><td>394.92 (n/a)</td><td>423.00 (n/a)</td><td>217.00 (n/a)</td><td>124.97 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (+13.50%)</td><td>0.03 (-3.72%)</td><td>0.03 (-10.31%)</td><td>0.02 (+0.67%)</td><td>0.01 <b>(+42.72%)</b></td><td>493.20 (-0.66%)</td><td>350.32 (+9.03%)</td><td>315.60 (+11.48%)</td><td>211.80 (-11.90%)</td><td>129.54 <b>(+26.55%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.50 (n/a)</td><td>321.30 (n/a)</td><td>283.10 (n/a)</td><td>240.40 (n/a)</td><td>102.36 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 <b>(-33.79%)</b></td><td>0.03 <b>(-22.95%)</b></td><td>0.02 <b>(-36.75%)</b></td><td>0.02 (+10.93%)</td><td>0.01 <b>(-50.89%)</b></td><td>485.40 (-9.84%)</td><td>406.52 (+14.32%)</td><td>460.00 <b>(+58.13%)</b></td><td>244.50 <b>(+51.02%)</b></td><td>102.27 <b>(-37.32%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>538.40 (n/a)</td><td>355.60 (n/a)</td><td>290.90 (n/a)</td><td>161.90 (n/a)</td><td>163.17 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (+4.41%)</td><td>0.03 (+17.02%)</td><td>0.02 <b>(+23.68%)</b></td><td>0.01 <b>(-69.45%)</b></td><td>0.02 <b>(+24.52%)</b></td><td>2037.20 <b>(+227.31%)</b></td><td>675.52 <b>(+37.36%)</b></td><td>443.50 (-19.14%)</td><td>184.10 (-4.21%)</td><td>771.20 <b>(+339.06%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>622.40 (n/a)</td><td>491.80 (n/a)</td><td>548.50 (n/a)</td><td>192.20 (n/a)</td><td>175.65 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 <b>(-20.96%)</b></td><td>0.03 <b>(-21.06%)</b></td><td>0.02 <b>(-38.94%)</b></td><td>0.02 (-19.91%)</td><td>0.01 (-19.73%)</td><td>639.40 <b>(+24.86%)</b></td><td>448.00 <b>(+26.06%)</b></td><td>531.00 <b>(+63.79%)</b></td><td>217.40 <b>(+26.54%)</b></td><td>176.67 (+18.00%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>512.10 (n/a)</td><td>355.38 (n/a)</td><td>324.20 (n/a)</td><td>171.80 (n/a)</td><td>149.73 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (-17.49%)</td><td>0.03 (+1.48%)</td><td>0.03 <b>(+36.65%)</b></td><td>0.02 (-4.28%)</td><td>0.01 (-15.22%)</td><td>543.90 (+4.48%)</td><td>383.74 (-2.08%)</td><td>300.40 <b>(-26.82%)</b></td><td>285.70 <b>(+21.16%)</b></td><td>123.34 (+6.46%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.60 (n/a)</td><td>391.88 (n/a)</td><td>410.50 (n/a)</td><td>235.80 (n/a)</td><td>115.85 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 <b>(-26.20%)</b></td><td>0.02 (-8.32%)</td><td>0.02 (-5.81%)</td><td>0.02 <b>(+155.98%)</b></td><td>0.01 <b>(-57.27%)</b></td><td>541.20 <b>(-60.94%)</b></td><td>480.18 <b>(-22.34%)</b></td><td>528.00 (+6.17%)</td><td>300.50 <b>(+35.48%)</b></td><td>102.30 <b>(-77.93%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1385.40 (n/a)</td><td>618.30 (n/a)</td><td>497.30 (n/a)</td><td>221.80 (n/a)</td><td>463.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 <b>(+59.99%)</b></td><td>0.06 (+0.66%)</td><td>0.04 <b>(-26.23%)</b></td><td>0.01 <b>(-70.59%)</b></td><td>0.04 <b>(+203.37%)</b></td><td>1858.30 <b>(+239.97%)</b></td><td>655.44 <b>(+73.76%)</b></td><td>490.50 <b>(+35.57%)</b></td><td>183.80 <b>(-37.48%)</b></td><td>686.61 <b>(+574.61%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>546.60 (n/a)</td><td>377.22 (n/a)</td><td>361.80 (n/a)</td><td>294.00 (n/a)</td><td>101.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (-19.95%)</td><td>0.06 (-16.96%)</td><td>0.05 <b>(-35.41%)</b></td><td>0.03 <b>(-24.55%)</b></td><td>0.02 (-3.72%)</td><td>682.60 <b>(+32.54%)</b></td><td>445.64 <b>(+25.69%)</b></td><td>461.10 <b>(+54.84%)</b></td><td>250.10 <b>(+24.93%)</b></td><td>190.26 <b>(+42.21%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>515.00 (n/a)</td><td>354.56 (n/a)</td><td>297.80 (n/a)</td><td>200.20 (n/a)</td><td>133.79 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 <b>(+23.28%)</b></td><td>0.05 (+16.64%)</td><td>0.04 (+0.59%)</td><td>0.01 (-4.09%)</td><td>0.04 <b>(+25.03%)</b></td><td>2044.30 (+4.27%)</td><td>718.20 (-4.38%)</td><td>513.30 (-0.60%)</td><td>214.60 (-18.90%)</td><td>757.79 (+8.07%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1960.60 (n/a)</td><td>751.12 (n/a)</td><td>516.40 (n/a)</td><td>264.60 (n/a)</td><td>701.23 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (-2.03%)</td><td>0.06 (-3.28%)</td><td>0.06 (+0.43%)</td><td>0.04 (+5.21%)</td><td>0.02 (-5.79%)</td><td>478.50 (-4.95%)</td><td>362.08 (+2.29%)</td><td>351.80 (-0.45%)</td><td>210.90 (+2.08%)</td><td>113.26 (-5.52%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>503.40 (n/a)</td><td>353.98 (n/a)</td><td>353.40 (n/a)</td><td>206.60 (n/a)</td><td>119.88 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 (-13.28%)</td><td>0.05 <b>(-21.50%)</b></td><td>0.05 <b>(-34.04%)</b></td><td>0.04 (-10.93%)</td><td>0.02 (-11.70%)</td><td>547.70 (+12.28%)</td><td>438.68 <b>(+26.93%)</b></td><td>451.70 <b>(+51.58%)</b></td><td>236.10 (+15.34%)</td><td>124.53 (+7.44%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>487.80 (n/a)</td><td>345.60 (n/a)</td><td>298.00 (n/a)</td><td>204.70 (n/a)</td><td>115.91 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 <b>(+23.45%)</b></td><td>0.05 (+6.00%)</td><td>0.04 (-4.45%)</td><td>0.04 (-1.60%)</td><td>0.02 <b>(+61.10%)</b></td><td>597.10 (+1.62%)</td><td>491.28 (-1.21%)</td><td>565.50 (+4.64%)</td><td>269.00 (-19.00%)</td><td>136.14 <b>(+33.63%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>587.60 (n/a)</td><td>497.32 (n/a)</td><td>540.40 (n/a)</td><td>332.10 (n/a)</td><td>101.88 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>501.30 (n/a)</td><td>403.02 (n/a)</td><td>451.50 (n/a)</td><td>199.90 (n/a)</td><td>118.45 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.00 (n/a)</td><td>425.52 (n/a)</td><td>431.90 (n/a)</td><td>273.90 (n/a)</td><td>113.96 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>680.50 (n/a)</td><td>515.84 (n/a)</td><td>564.00 (n/a)</td><td>241.50 (n/a)</td><td>175.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>455.00 (n/a)</td><td>361.04 (n/a)</td><td>326.60 (n/a)</td><td>305.60 (n/a)</td><td>66.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1905.30 (n/a)</td><td>760.84 (n/a)</td><td>552.10 (n/a)</td><td>263.30 (n/a)</td><td>652.99 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.50 (n/a)</td><td>406.52 (n/a)</td><td>458.50 (n/a)</td><td>266.60 (n/a)</td><td>104.93 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>611.40 (n/a)</td><td>394.16 (n/a)</td><td>417.10 (n/a)</td><td>223.00 (n/a)</td><td>153.19 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1083.30 (n/a)</td><td>449.30 (n/a)</td><td>288.20 (n/a)</td><td>241.50 (n/a)</td><td>358.63 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>524.50 (n/a)</td><td>377.08 (n/a)</td><td>382.70 (n/a)</td><td>241.00 (n/a)</td><td>111.32 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.18 (-12.03%)</td><td>0.16 <b>(+25.56%)</b></td><td>0.16 <b>(+48.64%)</b></td><td>0.15 <b>(+214.17%)</b></td><td>0.01 <b>(-82.01%)</b></td><td>334.30 <b>(-68.16%)</b></td><td>305.72 <b>(-40.34%)</b></td><td>309.80 <b>(-32.73%)</b></td><td>277.50 (+13.68%)</td><td>23.55 <b>(-92.89%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>1050.10 (n/a)</td><td>512.40 (n/a)</td><td>460.50 (n/a)</td><td>244.10 (n/a)</td><td>330.97 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>553.70 (n/a)</td><td>407.10 (n/a)</td><td>454.00 (n/a)</td><td>239.70 (n/a)</td><td>133.97 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>581.30 (n/a)</td><td>415.52 (n/a)</td><td>446.30 (n/a)</td><td>279.80 (n/a)</td><td>125.99 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>673.40 (n/a)</td><td>471.86 (n/a)</td><td>464.90 (n/a)</td><td>295.80 (n/a)</td><td>134.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.20 (n/a)</td><td>467.36 (n/a)</td><td>525.70 (n/a)</td><td>237.30 (n/a)</td><td>130.38 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.40 (n/a)</td><td>430.22 (n/a)</td><td>424.20 (n/a)</td><td>268.00 (n/a)</td><td>128.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>443.00 (n/a)</td><td>338.40 (n/a)</td><td>295.80 (n/a)</td><td>271.60 (n/a)</td><td>79.72 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.80 (n/a)</td><td>431.06 (n/a)</td><td>501.20 (n/a)</td><td>277.90 (n/a)</td><td>127.42 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1066.50 (n/a)</td><td>518.08 (n/a)</td><td>355.40 (n/a)</td><td>296.80 (n/a)</td><td>320.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>591.00 (n/a)</td><td>489.10 (n/a)</td><td>510.90 (n/a)</td><td>298.60 (n/a)</td><td>113.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>585.30 (n/a)</td><td>428.80 (n/a)</td><td>482.30 (n/a)</td><td>257.30 (n/a)</td><td>141.35 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1850.70 (n/a)</td><td>740.30 (n/a)</td><td>627.80 (n/a)</td><td>276.40 (n/a)</td><td>646.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>1019.10 (n/a)</td><td>597.06 (n/a)</td><td>573.90 (n/a)</td><td>331.80 (n/a)</td><td>259.03 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>560.80 (n/a)</td><td>450.38 (n/a)</td><td>496.90 (n/a)</td><td>263.90 (n/a)</td><td>114.51 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>461.10 (n/a)</td><td>366.00 (n/a)</td><td>412.30 (n/a)</td><td>227.30 (n/a)</td><td>108.87 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>448.40 (n/a)</td><td>341.46 (n/a)</td><td>318.60 (n/a)</td><td>286.60 (n/a)</td><td>64.36 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.70 (n/a)</td><td>378.16 (n/a)</td><td>429.80 (n/a)</td><td>237.90 (n/a)</td><td>120.61 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1025.00 (n/a)</td><td>567.28 (n/a)</td><td>535.00 (n/a)</td><td>166.00 (n/a)</td><td>305.73 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.80 (n/a)</td><td>447.40 (n/a)</td><td>470.10 (n/a)</td><td>232.90 (n/a)</td><td>140.05 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>612.00 (n/a)</td><td>432.62 (n/a)</td><td>502.70 (n/a)</td><td>253.50 (n/a)</td><td>153.45 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.40 (n/a)</td><td>353.46 (n/a)</td><td>283.50 (n/a)</td><td>222.30 (n/a)</td><td>130.94 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.70 (n/a)</td><td>411.92 (n/a)</td><td>418.50 (n/a)</td><td>281.80 (n/a)</td><td>128.94 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.70 (n/a)</td><td>402.02 (n/a)</td><td>416.50 (n/a)</td><td>274.60 (n/a)</td><td>115.45 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1965.80 (n/a)</td><td>768.94 (n/a)</td><td>597.80 (n/a)</td><td>261.70 (n/a)</td><td>702.43 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.10 (n/a)</td><td>330.74 (n/a)</td><td>307.90 (n/a)</td><td>237.80 (n/a)</td><td>116.67 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>544.90 (n/a)</td><td>406.20 (n/a)</td><td>378.80 (n/a)</td><td>309.40 (n/a)</td><td>94.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>750.40 (n/a)</td><td>387.32 (n/a)</td><td>287.60 (n/a)</td><td>254.20 (n/a)</td><td>209.41 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1990.80 (n/a)</td><td>732.94 (n/a)</td><td>561.00 (n/a)</td><td>252.00 (n/a)</td><td>718.76 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>616.20 (n/a)</td><td>385.34 (n/a)</td><td>292.90 (n/a)</td><td>261.70 (n/a)</td><td>153.75 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>518.00 (n/a)</td><td>351.40 (n/a)</td><td>299.70 (n/a)</td><td>250.50 (n/a)</td><td>118.05 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>493.00 (n/a)</td><td>354.48 (n/a)</td><td>401.30 (n/a)</td><td>192.30 (n/a)</td><td>129.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>534.80 (n/a)</td><td>401.00 (n/a)</td><td>387.00 (n/a)</td><td>264.30 (n/a)</td><td>107.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>519.50 (n/a)</td><td>416.30 (n/a)</td><td>413.80 (n/a)</td><td>317.60 (n/a)</td><td>71.70 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>558.20 (n/a)</td><td>385.14 (n/a)</td><td>306.50 (n/a)</td><td>239.40 (n/a)</td><td>144.30 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1064.20 (n/a)</td><td>569.00 (n/a)</td><td>455.00 (n/a)</td><td>313.50 (n/a)</td><td>297.11 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>510.30 (n/a)</td><td>445.10 (n/a)</td><td>469.30 (n/a)</td><td>292.40 (n/a)</td><td>87.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>615.60 (n/a)</td><td>482.30 (n/a)</td><td>540.10 (n/a)</td><td>268.20 (n/a)</td><td>141.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>631.90 (n/a)</td><td>437.64 (n/a)</td><td>401.20 (n/a)</td><td>330.20 (n/a)</td><td>122.82 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.49 <b>(-23.57%)</b></td><td>0.39 <b>(+31.18%)</b></td><td>0.35 (+10.66%)</td><td>0.32 <b>(+262.34%)</b></td><td>0.08 <b>(-62.51%)</b></td><td>691.40 <b>(-72.40%)</b></td><td>581.48 <b>(-51.48%)</b></td><td>634.20 (-9.65%)</td><td>451.90 <b>(+30.83%)</b></td><td>114.17 <b>(-87.40%)</b></td><td>20.88 <b>(-23.57%)</b></td><td>16.78 <b>(+31.18%)</b></td><td>14.88 (+10.66%)</td><td>13.65 <b>(+262.34%)</b></td><td>3.51 <b>(-62.51%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.64 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>0.22 (n/a)</td><td>2505.10 (n/a)</td><td>1198.34 (n/a)</td><td>701.90 (n/a)</td><td>345.40 (n/a)</td><td>906.44 (n/a)</td><td>27.32 (n/a)</td><td>12.79 (n/a)</td><td>13.45 (n/a)</td><td>3.77 (n/a)</td><td>9.36 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.48 (-2.78%)</td><td>0.37 (-3.85%)</td><td>0.40 (-4.45%)</td><td>0.21 (+15.33%)</td><td>0.11 (-11.68%)</td><td>1061.40 (-13.29%)</td><td>647.66 (-0.33%)</td><td>557.80 (+4.67%)</td><td>463.20 (+2.86%)</td><td>242.79 <b>(-24.83%)</b></td><td>20.37 (-2.78%)</td><td>15.90 (-3.85%)</td><td>16.92 (-4.45%)</td><td>8.89 (+15.33%)</td><td>4.52 (-11.68%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.49 (n/a)</td><td>0.39 (n/a)</td><td>0.42 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>1224.10 (n/a)</td><td>649.82 (n/a)</td><td>532.90 (n/a)</td><td>450.30 (n/a)</td><td>323.00 (n/a)</td><td>20.96 (n/a)</td><td>16.53 (n/a)</td><td>17.71 (n/a)</td><td>7.71 (n/a)</td><td>5.12 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.30 (-2.98%)</td><td>0.30 (-2.54%)</td><td>0.30 (-3.02%)</td><td>0.30 (-2.09%)</td><td>0.00 <b>(-33.09%)</b></td><td>84858.20 (+2.13%)</td><td>83572.40 (+2.60%)</td><td>83487.00 (+3.12%)</td><td>82846.80 (+3.07%)</td><td>771.15 <b>(-29.50%)</b></td><td>207.37 (-2.98%)</td><td>205.58 (-2.54%)</td><td>205.78 (-3.02%)</td><td>202.45 (-2.09%)</td><td>1.88 <b>(-33.09%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83086.80 (n/a)</td><td>81454.48 (n/a)</td><td>80963.80 (n/a)</td><td>80379.50 (n/a)</td><td>1093.77 (n/a)</td><td>213.73 (n/a)</td><td>210.94 (n/a)</td><td>212.19 (n/a)</td><td>206.77 (n/a)</td><td>2.81 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>1.03 (+1.95%)</td><td>1.00 (-1.40%)</td><td>1.00 (-1.23%)</td><td>0.95 (-6.52%)</td><td>0.03 <b>(+3189.02%)</b></td><td>26618.80 (+6.98%)</td><td>25231.72 (+1.51%)</td><td>25169.80 (+1.25%)</td><td>24349.70 (-1.91%)</td><td>848.72 <b>(+3373.40%)</b></td><td>705.55 (+1.95%)</td><td>681.49 (-1.40%)</td><td>682.56 (-1.23%)</td><td>645.40 (-6.52%)</td><td>22.36 <b>(+3190.06%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>0.00 (n/a)</td><td>24882.60 (n/a)</td><td>24857.24 (n/a)</td><td>24860.10 (n/a)</td><td>24824.10 (n/a)</td><td>24.43 (n/a)</td><td>692.07 (n/a)</td><td>691.14 (n/a)</td><td>691.06 (n/a)</td><td>690.44 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.83 (-0.27%)</td><td>0.82 (+0.42%)</td><td>0.82 (-1.01%)</td><td>0.80 (+1.77%)</td><td>0.01 <b>(-53.95%)</b></td><td>94249.70 (-1.74%)</td><td>92502.54 (-0.46%)</td><td>92360.30 (+1.02%)</td><td>91183.90 (+0.27%)</td><td>1104.81 <b>(-54.50%)</b></td><td>753.64 (-0.27%)</td><td>742.98 (+0.42%)</td><td>744.04 (-1.01%)</td><td>729.12 (+1.77%)</td><td>8.82 <b>(-53.95%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.83 (n/a)</td><td>0.81 (n/a)</td><td>0.83 (n/a)</td><td>0.79 (n/a)</td><td>0.02 (n/a)</td><td>95919.10 (n/a)</td><td>92930.88 (n/a)</td><td>91430.40 (n/a)</td><td>90938.80 (n/a)</td><td>2428.37 (n/a)</td><td>755.67 (n/a)</td><td>739.87 (n/a)</td><td>751.60 (n/a)</td><td>716.43 (n/a)</td><td>19.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.78 (-0.43%)</td><td>0.77 (-1.32%)</td><td>0.77 (-1.33%)</td><td>0.75 (-2.34%)</td><td>0.01 <b>(+109.10%)</b></td><td>100143.30 (+2.40%)</td><td>98362.62 (+1.35%)</td><td>98129.90 (+1.34%)</td><td>96975.70 (+0.43%)</td><td>1185.14 <b>(+115.34%)</b></td><td>708.63 (-0.43%)</td><td>698.71 (-1.32%)</td><td>700.29 (-1.33%)</td><td>686.21 (-2.34%)</td><td>8.38 <b>(+109.10%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.00 (n/a)</td><td>97795.40 (n/a)</td><td>97057.12 (n/a)</td><td>96828.80 (n/a)</td><td>96561.40 (n/a)</td><td>550.37 (n/a)</td><td>711.67 (n/a)</td><td>708.05 (n/a)</td><td>709.70 (n/a)</td><td>702.69 (n/a)</td><td>4.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.80 (+1.01%)</td><td>0.80 (+0.90%)</td><td>0.80 (+0.93%)</td><td>0.79 (+0.87%)</td><td>0.00 <b>(+23.15%)</b></td><td>95216.00 (-0.86%)</td><td>94634.46 (-0.89%)</td><td>94550.50 (-0.92%)</td><td>94221.00 (-1.00%)</td><td>408.60 <b>(+20.80%)</b></td><td>729.34 (+1.01%)</td><td>726.17 (+0.90%)</td><td>726.80 (+0.93%)</td><td>721.72 (+0.87%)</td><td>3.13 <b>(+23.15%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>96041.00 (n/a)</td><td>95483.90 (n/a)</td><td>95427.90 (n/a)</td><td>95171.00 (n/a)</td><td>338.24 (n/a)</td><td>722.06 (n/a)</td><td>719.70 (n/a)</td><td>720.12 (n/a)</td><td>715.52 (n/a)</td><td>2.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>5.33 (-5.16%)</td><td>3.30 (-8.27%)</td><td>2.74 <b>(-29.97%)</b></td><td>2.24 (+3.11%)</td><td>1.33 (-8.24%)</td><td>3987.00 (-3.02%)</td><td>3026.48 (+6.53%)</td><td>3248.10 <b>(+42.81%)</b></td><td>1671.40 (+5.44%)</td><td>1036.52 (-11.00%)</td><td>321.21 (-5.16%)</td><td>198.90 (-8.27%)</td><td>165.29 <b>(-29.97%)</b></td><td>134.65 (+3.11%)</td><td>80.34 (-8.24%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.62 (n/a)</td><td>3.60 (n/a)</td><td>3.92 (n/a)</td><td>2.17 (n/a)</td><td>1.45 (n/a)</td><td>4111.20 (n/a)</td><td>2841.04 (n/a)</td><td>2274.50 (n/a)</td><td>1585.20 (n/a)</td><td>1164.69 (n/a)</td><td>338.68 (n/a)</td><td>216.82 (n/a)</td><td>236.04 (n/a)</td><td>130.59 (n/a)</td><td>87.56 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>4.44 (-5.96%)</td><td>2.86 (-15.27%)</td><td>2.84 (-9.52%)</td><td>1.83 (-12.75%)</td><td>0.98 (+0.53%)</td><td>4861.10 (+14.61%)</td><td>3393.64 (+19.56%)</td><td>3142.40 (+10.52%)</td><td>2008.90 (+6.33%)</td><td>1056.25 (+18.94%)</td><td>267.25 (-5.96%)</td><td>172.27 (-15.27%)</td><td>170.85 (-9.52%)</td><td>110.44 (-12.75%)</td><td>59.13 (+0.53%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>4.72 (n/a)</td><td>3.38 (n/a)</td><td>3.13 (n/a)</td><td>2.10 (n/a)</td><td>0.98 (n/a)</td><td>4241.60 (n/a)</td><td>2838.50 (n/a)</td><td>2843.40 (n/a)</td><td>1889.30 (n/a)</td><td>888.04 (n/a)</td><td>284.17 (n/a)</td><td>203.32 (n/a)</td><td>188.82 (n/a)</td><td>126.57 (n/a)</td><td>58.82 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>5.59 (-1.04%)</td><td>3.42 <b>(-24.18%)</b></td><td>3.02 <b>(-42.32%)</b></td><td>2.20 (+10.21%)</td><td>1.36 (-7.98%)</td><td>4055.10 (-9.26%)</td><td>2910.68 <b>(+26.81%)</b></td><td>2954.70 <b>(+73.36%)</b></td><td>1593.10 (+1.05%)</td><td>981.51 <b>(-20.04%)</b></td><td>337.00 (-1.04%)</td><td>205.80 <b>(-24.18%)</b></td><td>181.70 <b>(-42.32%)</b></td><td>132.39 (+10.21%)</td><td>82.11 (-7.98%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.65 (n/a)</td><td>4.51 (n/a)</td><td>5.23 (n/a)</td><td>1.99 (n/a)</td><td>1.48 (n/a)</td><td>4469.00 (n/a)</td><td>2295.38 (n/a)</td><td>1704.40 (n/a)</td><td>1576.60 (n/a)</td><td>1227.48 (n/a)</td><td>340.52 (n/a)</td><td>271.43 (n/a)</td><td>315.00 (n/a)</td><td>120.13 (n/a)</td><td>89.23 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.80 (+15.59%)</td><td>6.20 (+19.76%)</td><td>6.61 <b>(+21.90%)</b></td><td>4.45 (+6.92%)</td><td>0.98 <b>(+41.28%)</b></td><td>7829.50 (-6.47%)</td><td>5771.24 (-15.66%)</td><td>5274.70 (-17.97%)</td><td>5128.50 (-13.49%)</td><td>1154.74 (+16.05%)</td><td>418.74 (+15.59%)</td><td>381.79 (+19.76%)</td><td>407.13 <b>(+21.90%)</b></td><td>274.28 (+6.92%)</td><td>60.57 <b>(+41.28%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.88 (n/a)</td><td>5.18 (n/a)</td><td>5.42 (n/a)</td><td>4.16 (n/a)</td><td>0.70 (n/a)</td><td>8371.30 (n/a)</td><td>6843.02 (n/a)</td><td>6429.90 (n/a)</td><td>5928.10 (n/a)</td><td>995.06 (n/a)</td><td>362.26 (n/a)</td><td>318.79 (n/a)</td><td>333.98 (n/a)</td><td>256.53 (n/a)</td><td>42.87 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>5.52 (-3.46%)</td><td>4.71 (-10.05%)</td><td>4.51 (-18.66%)</td><td>4.08 (-8.76%)</td><td>0.55 (-5.09%)</td><td>8546.30 (+9.61%)</td><td>7482.86 (+11.19%)</td><td>7723.00 <b>(+22.94%)</b></td><td>6316.00 (+3.59%)</td><td>851.49 (+7.96%)</td><td>340.01 (-3.46%)</td><td>290.08 (-10.05%)</td><td>278.06 (-18.66%)</td><td>251.28 (-8.76%)</td><td>34.16 (-5.09%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.72 (n/a)</td><td>5.24 (n/a)</td><td>5.55 (n/a)</td><td>4.47 (n/a)</td><td>0.58 (n/a)</td><td>7797.20 (n/a)</td><td>6729.66 (n/a)</td><td>6281.70 (n/a)</td><td>6097.30 (n/a)</td><td>788.71 (n/a)</td><td>352.20 (n/a)</td><td>322.48 (n/a)</td><td>341.87 (n/a)</td><td>275.42 (n/a)</td><td>35.99 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.37 (-1.13%)</td><td>5.33 (+0.81%)</td><td>5.18 (+1.55%)</td><td>4.58 (-2.37%)</td><td>0.75 (+10.51%)</td><td>7620.00 (+2.43%)</td><td>6637.90 (-0.45%)</td><td>6726.20 (-1.53%)</td><td>5473.40 (+1.14%)</td><td>897.63 (+17.99%)</td><td>392.35 (-1.13%)</td><td>328.48 (+0.81%)</td><td>319.27 (+1.55%)</td><td>281.82 (-2.37%)</td><td>46.02 (+10.51%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>6.44 (n/a)</td><td>5.29 (n/a)</td><td>5.10 (n/a)</td><td>4.69 (n/a)</td><td>0.68 (n/a)</td><td>7439.50 (n/a)</td><td>6668.16 (n/a)</td><td>6830.70 (n/a)</td><td>5411.70 (n/a)</td><td>760.79 (n/a)</td><td>396.82 (n/a)</td><td>325.84 (n/a)</td><td>314.39 (n/a)</td><td>288.66 (n/a)</td><td>41.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.79 (-0.23%)</td><td>0.77 (+1.07%)</td><td>0.77 (+1.48%)</td><td>0.74 (+0.95%)</td><td>0.02 (-11.62%)</td><td>102303.00 (-0.94%)</td><td>98090.16 (-1.07%)</td><td>97688.30 (-1.46%)</td><td>95758.00 (+0.23%)</td><td>2499.69 (-11.90%)</td><td>717.64 (-0.23%)</td><td>700.93 (+1.07%)</td><td>703.46 (+1.48%)</td><td>671.73 (+0.95%)</td><td>17.44 (-11.62%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103274.90 (n/a)</td><td>99149.72 (n/a)</td><td>99133.60 (n/a)</td><td>95540.50 (n/a)</td><td>2837.47 (n/a)</td><td>719.27 (n/a)</td><td>693.54 (n/a)</td><td>693.20 (n/a)</td><td>665.40 (n/a)</td><td>19.74 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.77 (-2.24%)</td><td>0.74 (-2.50%)</td><td>0.75 (-1.58%)</td><td>0.71 (-5.36%)</td><td>0.02 <b>(+68.72%)</b></td><td>106622.20 (+5.66%)</td><td>101511.48 (+2.62%)</td><td>100285.30 (+1.60%)</td><td>98644.80 (+2.29%)</td><td>3071.14 <b>(+83.53%)</b></td><td>696.64 (-2.24%)</td><td>677.45 (-2.50%)</td><td>685.24 (-1.58%)</td><td>644.51 (-5.36%)</td><td>19.96 <b>(+68.72%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100911.60 (n/a)</td><td>98921.78 (n/a)</td><td>98703.40 (n/a)</td><td>96434.40 (n/a)</td><td>1673.35 (n/a)</td><td>712.60 (n/a)</td><td>694.85 (n/a)</td><td>696.22 (n/a)</td><td>680.99 (n/a)</td><td>11.83 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.81 (-0.00%)</td><td>0.81 (+0.23%)</td><td>0.81 (+0.63%)</td><td>0.80 (+0.40%)</td><td>0.01 <b>(-21.63%)</b></td><td>94416.60 (-0.40%)</td><td>93540.50 (-0.23%)</td><td>93290.70 (-0.63%)</td><td>92828.30 (+0.00%)</td><td>707.62 <b>(-21.80%)</b></td><td>740.29 (-0.00%)</td><td>734.68 (+0.23%)</td><td>736.62 (+0.63%)</td><td>727.83 (+0.40%)</td><td>5.55 <b>(-21.63%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94797.30 (n/a)</td><td>93757.62 (n/a)</td><td>93882.40 (n/a)</td><td>92826.40 (n/a)</td><td>904.90 (n/a)</td><td>740.30 (n/a)</td><td>733.00 (n/a)</td><td>731.97 (n/a)</td><td>724.91 (n/a)</td><td>7.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.30 (-8.40%)</td><td>2.16 (-6.25%)</td><td>2.08 (+1.22%)</td><td>1.10 <b>(-41.27%)</b></td><td>0.79 (+7.89%)</td><td>7348.10 <b>(+70.26%)</b></td><td>4225.00 (+14.04%)</td><td>3884.70 (-1.20%)</td><td>2444.10 (+9.17%)</td><td>1850.38 <b>(+117.59%)</b></td><td>864.90 (-8.40%)</td><td>567.66 (-6.25%)</td><td>544.17 (+1.22%)</td><td>287.69 <b>(-41.27%)</b></td><td>206.69 (+7.89%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.60 (n/a)</td><td>2.31 (n/a)</td><td>2.05 (n/a)</td><td>1.87 (n/a)</td><td>0.73 (n/a)</td><td>4315.70 (n/a)</td><td>3704.86 (n/a)</td><td>3932.00 (n/a)</td><td>2238.90 (n/a)</td><td>850.41 (n/a)</td><td>944.19 (n/a)</td><td>605.52 (n/a)</td><td>537.62 (n/a)</td><td>489.82 (n/a)</td><td>191.58 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.21 <b>(-30.46%)</b></td><td>0.19 (-10.37%)</td><td>0.20 (-9.10%)</td><td>0.14 (-5.00%)</td><td>0.03 <b>(-53.78%)</b></td><td>8631.30 (+5.27%)</td><td>6589.36 (+7.13%)</td><td>6246.60 (+10.01%)</td><td>5869.30 <b>(+43.81%)</b></td><td>1158.78 <b>(-30.07%)</b></td><td>11.43 <b>(-30.46%)</b></td><td>10.40 (-10.37%)</td><td>10.74 (-9.10%)</td><td>7.78 (-5.00%)</td><td>1.51 <b>(-53.78%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>8199.40 (n/a)</td><td>6150.74 (n/a)</td><td>5678.10 (n/a)</td><td>4081.40 (n/a)</td><td>1657.05 (n/a)</td><td>16.44 (n/a)</td><td>11.60 (n/a)</td><td>11.82 (n/a)</td><td>8.18 (n/a)</td><td>3.27 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.82 (n/a)</td><td>3.66 (n/a)</td><td>3.65 (n/a)</td><td>3.49 (n/a)</td><td>0.15 (n/a)</td><td>3.81 (n/a)</td><td>3.66 (n/a)</td><td>3.65 (n/a)</td><td>3.48 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>7.32 (-1.28%)</td><td>6.45 (-5.22%)</td><td>6.58 (-1.46%)</td><td>5.04 (-15.13%)</td><td>0.85 <b>(+36.67%)</b></td><td>7.32 (-1.28%)</td><td>6.44 (-5.22%)</td><td>6.58 (-1.46%)</td><td>5.04 (-15.13%)</td><td>0.85 <b>(+36.67%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>7.42 (n/a)</td><td>6.80 (n/a)</td><td>6.68 (n/a)</td><td>5.94 (n/a)</td><td>0.62 (n/a)</td><td>7.41 (n/a)</td><td>6.80 (n/a)</td><td>6.68 (n/a)</td><td>5.93 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>14.33 (+4.16%)</td><td>9.53 (-15.82%)</td><td>8.27 <b>(-37.93%)</b></td><td>7.42 (-3.07%)</td><td>2.77 (-7.35%)</td><td>14.32 (+4.16%)</td><td>9.52 (-15.82%)</td><td>8.27 <b>(-37.93%)</b></td><td>7.41 (-3.07%)</td><td>2.77 (-7.35%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>13.75 (n/a)</td><td>11.32 (n/a)</td><td>13.32 (n/a)</td><td>7.65 (n/a)</td><td>2.99 (n/a)</td><td>13.75 (n/a)</td><td>11.31 (n/a)</td><td>13.32 (n/a)</td><td>7.65 (n/a)</td><td>2.99 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.85 (n/a)</td><td>3.69 (n/a)</td><td>3.66 (n/a)</td><td>3.44 (n/a)</td><td>0.16 (n/a)</td><td>3.85 (n/a)</td><td>3.69 (n/a)</td><td>3.66 (n/a)</td><td>3.44 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.98 (+1.59%)</td><td>6.07 (+4.90%)</td><td>5.79 (+1.32%)</td><td>5.60 (+12.49%)</td><td>0.56 (-18.56%)</td><td>6.98 (+1.59%)</td><td>6.07 (+4.90%)</td><td>5.79 (+1.32%)</td><td>5.60 (+12.49%)</td><td>0.56 (-18.56%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>6.87 (n/a)</td><td>5.79 (n/a)</td><td>5.72 (n/a)</td><td>4.98 (n/a)</td><td>0.68 (n/a)</td><td>6.87 (n/a)</td><td>5.78 (n/a)</td><td>5.71 (n/a)</td><td>4.98 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>9.48 <b>(-29.90%)</b></td><td>8.29 (-17.64%)</td><td>8.35 (-9.02%)</td><td>7.02 (-0.12%)</td><td>0.96 <b>(-69.93%)</b></td><td>9.48 <b>(-29.90%)</b></td><td>8.29 (-17.64%)</td><td>8.34 (-9.02%)</td><td>7.02 (-0.12%)</td><td>0.96 <b>(-69.93%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>13.53 (n/a)</td><td>10.07 (n/a)</td><td>9.18 (n/a)</td><td>7.03 (n/a)</td><td>3.19 (n/a)</td><td>13.52 (n/a)</td><td>10.06 (n/a)</td><td>9.17 (n/a)</td><td>7.03 (n/a)</td><td>3.19 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.06 (-5.02%)</td><td>1.62 <b>(-37.65%)</b></td><td>1.19 <b>(-60.90%)</b></td><td>1.03 (-19.53%)</td><td>0.87 (+4.06%)</td><td>3.06 (-5.02%)</td><td>1.62 <b>(-37.65%)</b></td><td>1.18 <b>(-60.90%)</b></td><td>1.03 (-19.53%)</td><td>0.86 (+4.06%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.23 (n/a)</td><td>2.60 (n/a)</td><td>3.04 (n/a)</td><td>1.28 (n/a)</td><td>0.83 (n/a)</td><td>3.22 (n/a)</td><td>2.60 (n/a)</td><td>3.03 (n/a)</td><td>1.28 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.58 (+1.02%)</td><td>0.38 (-10.38%)</td><td>0.36 <b>(-36.81%)</b></td><td>0.08 (+1.72%)</td><td>0.20 (-10.74%)</td><td>0.57 (+1.02%)</td><td>0.37 (-10.38%)</td><td>0.35 <b>(-36.81%)</b></td><td>0.08 (+1.72%)</td><td>0.19 (-10.74%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.57 (n/a)</td><td>0.42 (n/a)</td><td>0.57 (n/a)</td><td>0.08 (n/a)</td><td>0.22 (n/a)</td><td>0.56 (n/a)</td><td>0.42 (n/a)</td><td>0.56 (n/a)</td><td>0.08 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.71 (-1.18%)</td><td>0.51 (+12.24%)</td><td>0.47 (+0.74%)</td><td>0.32 <b>(+290.34%)</b></td><td>0.18 <b>(-32.84%)</b></td><td>0.70 (-1.18%)</td><td>0.51 (+12.24%)</td><td>0.47 (+0.74%)</td><td>0.31 <b>(+290.34%)</b></td><td>0.18 <b>(-32.84%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.72 (n/a)</td><td>0.46 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>0.27 (n/a)</td><td>0.71 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>2.65 (+4.10%)</td><td>1.93 (+8.79%)</td><td>2.33 (+19.58%)</td><td>0.43 (-5.05%)</td><td>0.90 (+14.64%)</td><td>2.60 (+4.10%)</td><td>1.89 (+8.79%)</td><td>2.29 (+19.58%)</td><td>0.42 (-5.05%)</td><td>0.88 (+14.64%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>2.54 (n/a)</td><td>1.77 (n/a)</td><td>1.94 (n/a)</td><td>0.45 (n/a)</td><td>0.78 (n/a)</td><td>2.50 (n/a)</td><td>1.74 (n/a)</td><td>1.91 (n/a)</td><td>0.44 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.50 (n/a)</td><td>440.46 (n/a)</td><td>486.80 (n/a)</td><td>238.20 (n/a)</td><td>126.30 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1060.40 (n/a)</td><td>471.38 (n/a)</td><td>373.20 (n/a)</td><td>242.40 (n/a)</td><td>335.21 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>905.70 (n/a)</td><td>551.76 (n/a)</td><td>448.00 (n/a)</td><td>351.40 (n/a)</td><td>221.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.30 (n/a)</td><td>443.04 (n/a)</td><td>474.40 (n/a)</td><td>307.30 (n/a)</td><td>85.25 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>601.40 (n/a)</td><td>462.04 (n/a)</td><td>461.20 (n/a)</td><td>245.10 (n/a)</td><td>140.62 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>497.20 (n/a)</td><td>352.76 (n/a)</td><td>295.40 (n/a)</td><td>227.40 (n/a)</td><td>117.94 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.70 (n/a)</td><td>417.00 (n/a)</td><td>468.60 (n/a)</td><td>230.40 (n/a)</td><td>178.17 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>485.50 (n/a)</td><td>343.88 (n/a)</td><td>293.30 (n/a)</td><td>280.70 (n/a)</td><td>87.98 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1924.00 (n/a)</td><td>702.88 (n/a)</td><td>440.70 (n/a)</td><td>261.40 (n/a)</td><td>688.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.30 (n/a)</td><td>354.48 (n/a)</td><td>278.50 (n/a)</td><td>201.20 (n/a)</td><td>152.80 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>712.10 (n/a)</td><td>383.68 (n/a)</td><td>296.30 (n/a)</td><td>234.60 (n/a)</td><td>194.56 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>792.80 (n/a)</td><td>541.98 (n/a)</td><td>532.20 (n/a)</td><td>310.40 (n/a)</td><td>199.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.30 (n/a)</td><td>367.54 (n/a)</td><td>328.50 (n/a)</td><td>252.90 (n/a)</td><td>129.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1879.50 (n/a)</td><td>702.04 (n/a)</td><td>445.60 (n/a)</td><td>266.00 (n/a)</td><td>667.04 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1869.60 (n/a)</td><td>691.32 (n/a)</td><td>434.70 (n/a)</td><td>261.90 (n/a)</td><td>665.81 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>520.60 (n/a)</td><td>382.44 (n/a)</td><td>445.30 (n/a)</td><td>220.50 (n/a)</td><td>128.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>731.20 (n/a)</td><td>466.82 (n/a)</td><td>466.20 (n/a)</td><td>245.30 (n/a)</td><td>173.73 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>926.40 (n/a)</td><td>538.90 (n/a)</td><td>461.80 (n/a)</td><td>356.30 (n/a)</td><td>222.91 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>692.80 (n/a)</td><td>442.88 (n/a)</td><td>391.60 (n/a)</td><td>301.20 (n/a)</td><td>163.09 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1875.10 (n/a)</td><td>711.66 (n/a)</td><td>469.80 (n/a)</td><td>248.10 (n/a)</td><td>658.63 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>606.90 (n/a)</td><td>339.08 (n/a)</td><td>271.90 (n/a)</td><td>251.40 (n/a)</td><td>150.51 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>628.60 (n/a)</td><td>429.26 (n/a)</td><td>361.30 (n/a)</td><td>260.50 (n/a)</td><td>164.19 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>699.90 (n/a)</td><td>469.10 (n/a)</td><td>435.30 (n/a)</td><td>267.80 (n/a)</td><td>160.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>616.80 (n/a)</td><td>499.78 (n/a)</td><td>524.00 (n/a)</td><td>362.10 (n/a)</td><td>95.86 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 <b>(-21.87%)</b></td><td>0.01 (-18.74%)</td><td>0.01 <b>(-22.56%)</b></td><td>0.01 (+9.18%)</td><td>0.00 <b>(-44.49%)</b></td><td>577.80 (-8.42%)</td><td>421.46 (+12.31%)</td><td>408.70 <b>(+29.13%)</b></td><td>289.60 <b>(+27.97%)</b></td><td>114.36 <b>(-33.11%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.90 (n/a)</td><td>375.26 (n/a)</td><td>316.50 (n/a)</td><td>226.30 (n/a)</td><td>170.97 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(-38.17%)</b></td><td>0.01 <b>(-33.08%)</b></td><td>0.01 <b>(-32.54%)</b></td><td>0.01 (-9.25%)</td><td>0.00 <b>(-48.10%)</b></td><td>520.40 (+10.18%)</td><td>411.74 <b>(+40.07%)</b></td><td>440.30 <b>(+48.25%)</b></td><td>245.80 <b>(+61.71%)</b></td><td>108.35 (-7.90%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>472.30 (n/a)</td><td>293.96 (n/a)</td><td>297.00 (n/a)</td><td>152.00 (n/a)</td><td>117.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(-35.28%)</b></td><td>0.01 (-11.54%)</td><td>0.01 <b>(-23.38%)</b></td><td>0.01 <b>(+343.63%)</b></td><td>0.00 <b>(-67.72%)</b></td><td>437.40 <b>(-77.46%)</b></td><td>355.88 <b>(-41.59%)</b></td><td>358.20 <b>(+30.49%)</b></td><td>269.40 <b>(+54.47%)</b></td><td>75.40 <b>(-89.94%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1940.30 (n/a)</td><td>609.24 (n/a)</td><td>274.50 (n/a)</td><td>174.40 (n/a)</td><td>749.50 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 <b>(-33.01%)</b></td><td>0.01 <b>(-38.00%)</b></td><td>0.01 <b>(-39.82%)</b></td><td>0.01 (-16.16%)</td><td>0.00 <b>(-47.34%)</b></td><td>604.60 (+19.27%)</td><td>477.58 <b>(+52.09%)</b></td><td>499.30 <b>(+66.16%)</b></td><td>291.20 <b>(+49.26%)</b></td><td>126.49 (-1.85%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>506.90 (n/a)</td><td>314.02 (n/a)</td><td>300.50 (n/a)</td><td>195.10 (n/a)</td><td>128.88 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (-8.92%)</td><td>0.01 (+7.49%)</td><td>0.01 <b>(+45.37%)</b></td><td>0.01 (+7.72%)</td><td>0.00 <b>(-21.93%)</b></td><td>524.10 (-7.16%)</td><td>365.68 (-11.94%)</td><td>336.80 <b>(-31.21%)</b></td><td>229.40 (+9.81%)</td><td>125.71 <b>(-20.67%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.50 (n/a)</td><td>415.28 (n/a)</td><td>489.60 (n/a)</td><td>208.90 (n/a)</td><td>158.46 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 <b>(-26.26%)</b></td><td>0.01 (-17.36%)</td><td>0.01 (-18.80%)</td><td>0.01 (+0.50%)</td><td>0.00 <b>(-46.49%)</b></td><td>536.20 (-0.50%)</td><td>474.08 (+16.14%)</td><td>520.40 <b>(+23.14%)</b></td><td>346.30 <b>(+35.64%)</b></td><td>82.90 <b>(-26.04%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>538.90 (n/a)</td><td>408.20 (n/a)</td><td>422.60 (n/a)</td><td>255.30 (n/a)</td><td>112.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (-12.34%)</td><td>0.02 <b>(-28.16%)</b></td><td>0.02 <b>(-30.68%)</b></td><td>0.02 <b>(-35.02%)</b></td><td>0.01 (+17.27%)</td><td>454.50 <b>(+53.91%)</b></td><td>379.36 <b>(+48.09%)</b></td><td>405.50 <b>(+44.25%)</b></td><td>187.80 (+14.09%)</td><td>110.19 <b>(+99.65%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>295.30 (n/a)</td><td>256.16 (n/a)</td><td>281.10 (n/a)</td><td>164.60 (n/a)</td><td>55.19 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (+5.84%)</td><td>0.03 (+7.14%)</td><td>0.03 (-6.19%)</td><td>0.02 (+3.82%)</td><td>0.01 (-10.25%)</td><td>442.90 (-3.70%)</td><td>321.02 (-8.37%)</td><td>319.50 (+6.61%)</td><td>240.00 (-5.55%)</td><td>77.40 <b>(-21.71%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>459.90 (n/a)</td><td>350.36 (n/a)</td><td>299.70 (n/a)</td><td>254.10 (n/a)</td><td>98.87 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 <b>(-26.92%)</b></td><td>0.02 (-16.13%)</td><td>0.02 <b>(-20.92%)</b></td><td>0.02 (+5.02%)</td><td>0.00 <b>(-45.36%)</b></td><td>521.50 (-4.77%)</td><td>406.58 (+11.76%)</td><td>379.40 <b>(+26.47%)</b></td><td>296.30 <b>(+36.80%)</b></td><td>95.99 <b>(-29.06%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.60 (n/a)</td><td>363.80 (n/a)</td><td>300.00 (n/a)</td><td>216.60 (n/a)</td><td>135.31 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (-0.25%)</td><td>0.02 (+6.03%)</td><td>0.01 (-3.65%)</td><td>0.01 (+9.17%)</td><td>0.01 (+7.39%)</td><td>613.20 (-8.40%)</td><td>478.74 (-4.96%)</td><td>552.40 (+3.80%)</td><td>305.90 (+0.26%)</td><td>142.39 (+0.81%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>669.40 (n/a)</td><td>503.74 (n/a)</td><td>532.20 (n/a)</td><td>305.10 (n/a)</td><td>141.24 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 <b>(+22.95%)</b></td><td>0.02 (+4.61%)</td><td>0.02 (+8.13%)</td><td>0.00 <b>(-72.37%)</b></td><td>0.01 <b>(+150.60%)</b></td><td>1897.60 <b>(+261.86%)</b></td><td>681.68 <b>(+55.10%)</b></td><td>402.50 (-7.51%)</td><td>246.10 (-18.67%)</td><td>692.67 <b>(+655.85%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>524.40 (n/a)</td><td>439.50 (n/a)</td><td>435.20 (n/a)</td><td>302.60 (n/a)</td><td>91.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 <b>(+38.15%)</b></td><td>0.02 (+7.85%)</td><td>0.02 (+3.54%)</td><td>0.01 (-18.02%)</td><td>0.01 <b>(+87.94%)</b></td><td>570.40 <b>(+21.98%)</b></td><td>390.94 (+1.33%)</td><td>418.70 (-3.41%)</td><td>199.80 <b>(-27.63%)</b></td><td>146.86 <b>(+62.46%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>467.60 (n/a)</td><td>385.80 (n/a)</td><td>433.50 (n/a)</td><td>276.10 (n/a)</td><td>90.40 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 <b>(-23.88%)</b></td><td>0.02 (-1.61%)</td><td>0.03 (+11.84%)</td><td>0.01 <b>(+75.74%)</b></td><td>0.01 <b>(-30.36%)</b></td><td>596.10 <b>(-43.10%)</b></td><td>395.10 (-14.89%)</td><td>300.20 (-10.60%)</td><td>263.60 <b>(+31.41%)</b></td><td>162.15 <b>(-51.96%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1047.60 (n/a)</td><td>464.22 (n/a)</td><td>335.80 (n/a)</td><td>200.60 (n/a)</td><td>337.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (-4.46%)</td><td>0.02 (-19.27%)</td><td>0.02 <b>(-33.56%)</b></td><td>0.01 <b>(-22.70%)</b></td><td>0.01 (+16.48%)</td><td>630.90 <b>(+29.36%)</b></td><td>475.54 <b>(+28.94%)</b></td><td>533.40 <b>(+50.51%)</b></td><td>292.90 (+4.64%)</td><td>146.87 <b>(+60.32%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.70 (n/a)</td><td>368.82 (n/a)</td><td>354.40 (n/a)</td><td>279.90 (n/a)</td><td>91.61 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (+8.09%)</td><td>0.05 (-3.05%)</td><td>0.05 (-7.12%)</td><td>0.03 (+10.46%)</td><td>0.02 (+13.62%)</td><td>533.00 (-9.48%)</td><td>365.28 (+3.41%)</td><td>320.10 (+7.71%)</td><td>225.90 (-7.49%)</td><td>123.60 (-9.10%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.80 (n/a)</td><td>353.22 (n/a)</td><td>297.20 (n/a)</td><td>244.20 (n/a)</td><td>135.98 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 <b>(-21.95%)</b></td><td>0.03 <b>(-24.65%)</b></td><td>0.03 <b>(-28.87%)</b></td><td>0.02 <b>(-28.60%)</b></td><td>0.01 (-14.59%)</td><td>812.60 <b>(+40.06%)</b></td><td>586.00 <b>(+35.14%)</b></td><td>611.60 <b>(+40.57%)</b></td><td>350.00 <b>(+28.11%)</b></td><td>170.27 <b>(+54.43%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>580.20 (n/a)</td><td>433.64 (n/a)</td><td>435.10 (n/a)</td><td>273.20 (n/a)</td><td>110.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (+3.78%)</td><td>0.04 <b>(-23.29%)</b></td><td>0.04 (-10.94%)</td><td>0.01 <b>(-69.97%)</b></td><td>0.03 <b>(+77.12%)</b></td><td>1950.90 <b>(+233.03%)</b></td><td>967.64 <b>(+153.35%)</b></td><td>412.40 (+12.28%)</td><td>242.20 (-3.62%)</td><td>895.91 <b>(+563.80%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>585.80 (n/a)</td><td>381.94 (n/a)</td><td>367.30 (n/a)</td><td>251.30 (n/a)</td><td>134.97 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 <b>(-29.52%)</b></td><td>0.04 <b>(-34.12%)</b></td><td>0.03 <b>(-43.92%)</b></td><td>0.03 (-19.00%)</td><td>0.01 <b>(-40.50%)</b></td><td>596.00 <b>(+23.47%)</b></td><td>450.14 <b>(+43.55%)</b></td><td>474.30 <b>(+78.31%)</b></td><td>259.50 <b>(+41.88%)</b></td><td>123.06 (-4.65%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>482.70 (n/a)</td><td>313.58 (n/a)</td><td>266.00 (n/a)</td><td>182.90 (n/a)</td><td>129.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 <b>(-24.37%)</b></td><td>0.03 <b>(-21.99%)</b></td><td>0.04 <b>(+30.85%)</b></td><td>0.01 <b>(-70.18%)</b></td><td>0.02 (-12.44%)</td><td>1969.80 <b>(+235.29%)</b></td><td>737.60 <b>(+70.21%)</b></td><td>388.60 <b>(-23.56%)</b></td><td>312.50 <b>(+32.19%)</b></td><td>699.31 <b>(+314.55%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>587.50 (n/a)</td><td>433.34 (n/a)</td><td>508.40 (n/a)</td><td>236.40 (n/a)</td><td>168.69 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (-13.21%)</td><td>0.04 (-16.89%)</td><td>0.03 <b>(-32.63%)</b></td><td>0.03 (-11.23%)</td><td>0.01 (-4.87%)</td><td>579.20 (+12.66%)</td><td>448.12 <b>(+21.86%)</b></td><td>480.50 <b>(+48.44%)</b></td><td>279.50 (+15.21%)</td><td>135.59 <b>(+23.38%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>514.10 (n/a)</td><td>367.72 (n/a)</td><td>323.70 (n/a)</td><td>242.60 (n/a)</td><td>109.90 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 <b>(-24.58%)</b></td><td>0.07 <b>(-38.66%)</b></td><td>0.06 <b>(-54.71%)</b></td><td>0.06 (-16.91%)</td><td>0.02 <b>(-35.96%)</b></td><td>590.00 <b>(+20.33%)</b></td><td>501.38 <b>(+58.95%)</b></td><td>547.60 <b>(+120.81%)</b></td><td>318.60 <b>(+32.58%)</b></td><td>111.33 (+3.15%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>490.30 (n/a)</td><td>315.44 (n/a)</td><td>248.00 (n/a)</td><td>240.30 (n/a)</td><td>107.93 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 <b>(-28.17%)</b></td><td>0.08 <b>(-30.78%)</b></td><td>0.07 <b>(-42.82%)</b></td><td>0.05 <b>(-25.87%)</b></td><td>0.03 <b>(-23.59%)</b></td><td>651.20 <b>(+34.88%)</b></td><td>461.46 <b>(+45.70%)</b></td><td>488.00 <b>(+74.91%)</b></td><td>277.30 <b>(+39.21%)</b></td><td>175.34 <b>(+39.59%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>482.80 (n/a)</td><td>316.72 (n/a)</td><td>279.00 (n/a)</td><td>199.20 (n/a)</td><td>125.61 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 <b>(-46.72%)</b></td><td>0.06 <b>(-45.99%)</b></td><td>0.07 <b>(-41.51%)</b></td><td>0.03 <b>(-60.92%)</b></td><td>0.02 <b>(-29.36%)</b></td><td>1021.60 <b>(+155.91%)</b></td><td>587.28 <b>(+96.10%)</b></td><td>468.70 <b>(+71.00%)</b></td><td>438.20 <b>(+87.67%)</b></td><td>246.20 <b>(+252.55%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>399.20 (n/a)</td><td>299.48 (n/a)</td><td>274.10 (n/a)</td><td>233.50 (n/a)</td><td>69.84 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.16 (+6.87%)</td><td>0.10 (-8.50%)</td><td>0.08 <b>(-27.99%)</b></td><td>0.05 (-16.74%)</td><td>0.04 (+11.60%)</td><td>611.20 <b>(+20.13%)</b></td><td>394.82 (+12.62%)</td><td>406.00 <b>(+38.85%)</b></td><td>198.90 (-6.44%)</td><td>164.00 (+16.00%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>508.80 (n/a)</td><td>350.58 (n/a)</td><td>292.40 (n/a)</td><td>212.60 (n/a)</td><td>141.38 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (+4.26%)</td><td>0.07 (+3.56%)</td><td>0.07 (-2.23%)</td><td>0.02 <b>(-41.57%)</b></td><td>0.04 (+14.83%)</td><td>1311.90 <b>(+71.15%)</b></td><td>593.96 (+11.40%)</td><td>490.80 (+2.27%)</td><td>240.30 (-4.07%)</td><td>417.90 <b>(+94.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>766.50 (n/a)</td><td>533.16 (n/a)</td><td>479.90 (n/a)</td><td>250.50 (n/a)</td><td>214.41 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (-3.62%)</td><td>0.01 (+4.89%)</td><td>0.01 (-3.53%)</td><td>0.01 (-5.33%)</td><td>0.00 (+11.37%)</td><td>540.80 (+5.62%)</td><td>408.78 (-2.43%)</td><td>452.70 (+3.66%)</td><td>266.50 (+3.78%)</td><td>121.94 <b>(+27.11%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.00 (n/a)</td><td>418.96 (n/a)</td><td>436.70 (n/a)</td><td>256.80 (n/a)</td><td>95.93 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (+0.57%)</td><td>0.01 (-13.74%)</td><td>0.01 <b>(-30.88%)</b></td><td>0.01 (-4.09%)</td><td>0.00 <b>(+30.23%)</b></td><td>507.30 (+4.28%)</td><td>418.50 (+18.95%)</td><td>487.70 <b>(+44.68%)</b></td><td>292.10 (-0.58%)</td><td>107.12 <b>(+35.24%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>486.50 (n/a)</td><td>351.84 (n/a)</td><td>337.10 (n/a)</td><td>293.80 (n/a)</td><td>79.20 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 <b>(+39.33%)</b></td><td>0.01 (+11.53%)</td><td>0.01 (-9.30%)</td><td>0.01 (-10.11%)</td><td>0.00 <b>(+214.33%)</b></td><td>594.50 (+11.25%)</td><td>429.74 (-3.17%)</td><td>478.70 (+10.25%)</td><td>280.80 <b>(-28.22%)</b></td><td>136.73 <b>(+137.59%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>534.40 (n/a)</td><td>443.80 (n/a)</td><td>434.20 (n/a)</td><td>391.20 (n/a)</td><td>57.55 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (+0.37%)</td><td>0.01 (+5.88%)</td><td>0.01 (+0.62%)</td><td>0.01 (+16.69%)</td><td>0.00 (-9.30%)</td><td>506.10 (-14.31%)</td><td>320.98 (-8.02%)</td><td>289.00 (-0.62%)</td><td>248.40 (-0.36%)</td><td>105.14 <b>(-23.72%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.60 (n/a)</td><td>348.96 (n/a)</td><td>290.80 (n/a)</td><td>249.30 (n/a)</td><td>137.83 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (+4.11%)</td><td>0.01 (-2.45%)</td><td>0.01 <b>(-38.49%)</b></td><td>0.01 (+12.59%)</td><td>0.00 (-7.78%)</td><td>572.90 (-11.18%)</td><td>400.70 (-2.95%)</td><td>455.90 <b>(+62.59%)</b></td><td>238.60 (-3.95%)</td><td>142.70 <b>(-27.63%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>645.00 (n/a)</td><td>412.86 (n/a)</td><td>280.40 (n/a)</td><td>248.40 (n/a)</td><td>197.18 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (-5.18%)</td><td>0.01 (-1.75%)</td><td>0.02 (-10.38%)</td><td>0.01 (-14.29%)</td><td>0.00 (-12.18%)</td><td>581.00 (+16.67%)</td><td>327.88 (+2.20%)</td><td>269.60 (+11.59%)</td><td>241.90 (+5.49%)</td><td>142.24 (+18.52%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>498.00 (n/a)</td><td>320.82 (n/a)</td><td>241.60 (n/a)</td><td>229.30 (n/a)</td><td>120.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 <b>(-29.72%)</b></td><td>0.01 <b>(-42.84%)</b></td><td>0.01 <b>(-48.17%)</b></td><td>0.00 <b>(-75.75%)</b></td><td>0.00 (-18.44%)</td><td>2465.00 <b>(+312.28%)</b></td><td>922.50 <b>(+134.96%)</b></td><td>571.00 <b>(+92.91%)</b></td><td>389.90 <b>(+42.30%)</b></td><td>867.91 <b>(+464.11%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>597.90 (n/a)</td><td>392.62 (n/a)</td><td>296.00 (n/a)</td><td>274.00 (n/a)</td><td>153.85 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (+6.02%)</td><td>0.01 (+16.67%)</td><td>0.01 (+17.23%)</td><td>0.01 (+0.78%)</td><td>0.00 <b>(+27.36%)</b></td><td>627.80 (-0.77%)</td><td>429.52 (-12.24%)</td><td>412.00 (-14.72%)</td><td>305.80 (-5.68%)</td><td>135.81 (+15.31%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>632.70 (n/a)</td><td>489.40 (n/a)</td><td>483.10 (n/a)</td><td>324.20 (n/a)</td><td>117.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (-2.91%)</td><td>0.01 (+0.21%)</td><td>0.01 (+6.50%)</td><td>0.01 (-3.32%)</td><td>0.00 (-9.41%)</td><td>619.90 (+3.44%)</td><td>469.20 (-1.54%)</td><td>461.30 (-6.11%)</td><td>286.60 (+2.98%)</td><td>121.47 (-8.41%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.30 (n/a)</td><td>476.52 (n/a)</td><td>491.30 (n/a)</td><td>278.30 (n/a)</td><td>132.62 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 <b>(-42.48%)</b></td><td>0.01 <b>(-26.55%)</b></td><td>0.01 (-9.27%)</td><td>0.01 (-12.27%)</td><td>0.00 <b>(-69.77%)</b></td><td>622.80 (+13.98%)</td><td>519.08 <b>(+25.30%)</b></td><td>532.10 (+10.21%)</td><td>427.60 <b>(+73.82%)</b></td><td>79.64 <b>(-41.04%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.40 (n/a)</td><td>414.26 (n/a)</td><td>482.80 (n/a)</td><td>246.00 (n/a)</td><td>135.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 <b>(-20.63%)</b></td><td>0.01 (-13.75%)</td><td>0.01 (+3.89%)</td><td>0.01 (-11.08%)</td><td>0.00 <b>(-36.23%)</b></td><td>597.30 (+12.46%)</td><td>466.98 (+12.82%)</td><td>448.60 (-3.75%)</td><td>364.70 <b>(+26.02%)</b></td><td>105.89 (-7.14%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.10 (n/a)</td><td>413.92 (n/a)</td><td>466.10 (n/a)</td><td>289.40 (n/a)</td><td>114.04 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 <b>(-41.83%)</b></td><td>0.01 <b>(-38.11%)</b></td><td>0.01 <b>(-23.56%)</b></td><td>0.00 <b>(-73.10%)</b></td><td>0.00 (-7.50%)</td><td>1911.60 <b>(+271.69%)</b></td><td>806.34 <b>(+101.15%)</b></td><td>542.70 <b>(+30.83%)</b></td><td>469.70 <b>(+71.93%)</b></td><td>619.16 <b>(+550.60%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.30 (n/a)</td><td>400.86 (n/a)</td><td>414.80 (n/a)</td><td>273.20 (n/a)</td><td>95.17 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 <b>(-27.99%)</b></td><td>0.02 (-7.15%)</td><td>0.02 (+19.01%)</td><td>0.01 (-5.94%)</td><td>0.01 <b>(-43.95%)</b></td><td>568.20 (+6.32%)</td><td>398.52 (-0.86%)</td><td>405.60 (-15.97%)</td><td>290.20 <b>(+38.85%)</b></td><td>115.57 <b>(-24.27%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.40 (n/a)</td><td>401.96 (n/a)</td><td>482.70 (n/a)</td><td>209.00 (n/a)</td><td>152.62 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (+6.26%)</td><td>0.03 <b>(+25.92%)</b></td><td>0.03 <b>(+71.63%)</b></td><td>0.02 (+19.81%)</td><td>0.01 (-12.83%)</td><td>436.80 (-16.53%)</td><td>316.72 <b>(-23.60%)</b></td><td>286.90 <b>(-41.73%)</b></td><td>218.70 (-5.90%)</td><td>86.70 <b>(-31.85%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.30 (n/a)</td><td>414.56 (n/a)</td><td>492.40 (n/a)</td><td>232.40 (n/a)</td><td>127.22 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 <b>(+31.21%)</b></td><td>0.02 <b>(+27.72%)</b></td><td>0.02 <b>(+22.48%)</b></td><td>0.02 <b>(+39.57%)</b></td><td>0.01 <b>(+32.81%)</b></td><td>462.40 <b>(-28.35%)</b></td><td>390.64 <b>(-21.65%)</b></td><td>428.50 (-18.35%)</td><td>295.10 <b>(-23.77%)</b></td><td>83.77 <b>(-23.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>645.40 (n/a)</td><td>498.58 (n/a)</td><td>524.80 (n/a)</td><td>387.10 (n/a)</td><td>110.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (-10.14%)</td><td>0.02 <b>(-25.25%)</b></td><td>0.02 <b>(-39.61%)</b></td><td>0.02 (-17.62%)</td><td>0.01 (+17.12%)</td><td>529.60 <b>(+21.38%)</b></td><td>418.22 <b>(+37.82%)</b></td><td>470.30 <b>(+65.60%)</b></td><td>275.90 (+11.29%)</td><td>115.05 <b>(+51.68%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>436.30 (n/a)</td><td>303.46 (n/a)</td><td>284.00 (n/a)</td><td>247.90 (n/a)</td><td>75.85 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (-9.26%)</td><td>0.02 (-1.40%)</td><td>0.02 (+1.73%)</td><td>0.01 <b>(+42.39%)</b></td><td>0.01 <b>(-34.22%)</b></td><td>549.40 <b>(-29.76%)</b></td><td>425.50 (-11.92%)</td><td>491.90 (-1.70%)</td><td>262.60 (+10.24%)</td><td>135.55 <b>(-44.14%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>782.20 (n/a)</td><td>483.08 (n/a)</td><td>500.40 (n/a)</td><td>238.20 (n/a)</td><td>242.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (-15.25%)</td><td>0.02 <b>(-26.49%)</b></td><td>0.02 <b>(-36.56%)</b></td><td>0.02 (-6.10%)</td><td>0.01 (-11.78%)</td><td>503.60 (+6.51%)</td><td>413.70 <b>(+35.51%)</b></td><td>439.20 <b>(+57.65%)</b></td><td>260.90 (+18.00%)</td><td>102.14 (+5.16%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>472.80 (n/a)</td><td>305.30 (n/a)</td><td>278.60 (n/a)</td><td>221.10 (n/a)</td><td>97.13 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (-18.69%)</td><td>0.02 (+8.18%)</td><td>0.02 <b>(+37.89%)</b></td><td>0.01 (+5.10%)</td><td>0.01 <b>(-20.85%)</b></td><td>568.20 (-4.86%)</td><td>422.56 (-9.05%)</td><td>361.70 <b>(-27.47%)</b></td><td>307.60 <b>(+22.99%)</b></td><td>132.58 (+1.39%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.20 (n/a)</td><td>464.60 (n/a)</td><td>498.70 (n/a)</td><td>250.10 (n/a)</td><td>130.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(-20.29%)</b></td><td>0.02 <b>(-22.04%)</b></td><td>0.02 (-7.35%)</td><td>0.01 <b>(-28.07%)</b></td><td>0.00 <b>(-26.02%)</b></td><td>664.00 <b>(+39.03%)</b></td><td>491.84 <b>(+27.92%)</b></td><td>443.80 (+7.93%)</td><td>339.90 <b>(+25.47%)</b></td><td>128.94 <b>(+30.56%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>477.60 (n/a)</td><td>384.50 (n/a)</td><td>411.20 (n/a)</td><td>270.90 (n/a)</td><td>98.76 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(-45.50%)</b></td><td>0.02 <b>(-30.30%)</b></td><td>0.02 (-18.65%)</td><td>0.01 (+5.35%)</td><td>0.00 <b>(-71.70%)</b></td><td>594.20 (-5.06%)</td><td>510.54 <b>(+25.40%)</b></td><td>543.50 <b>(+22.94%)</b></td><td>377.40 <b>(+83.47%)</b></td><td>82.47 <b>(-50.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.90 (n/a)</td><td>407.12 (n/a)</td><td>442.10 (n/a)</td><td>205.70 (n/a)</td><td>168.00 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 <b>(-39.08%)</b></td><td>0.02 (-16.12%)</td><td>0.03 (-6.09%)</td><td>0.01 <b>(+211.96%)</b></td><td>0.01 <b>(-62.65%)</b></td><td>612.80 <b>(-67.94%)</b></td><td>395.70 <b>(-37.36%)</b></td><td>303.90 (+6.48%)</td><td>296.90 <b>(+64.12%)</b></td><td>140.57 <b>(-80.85%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1911.60 (n/a)</td><td>631.72 (n/a)</td><td>285.40 (n/a)</td><td>180.90 (n/a)</td><td>733.99 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (-1.57%)</td><td>0.02 (+3.01%)</td><td>0.02 <b>(+31.14%)</b></td><td>0.01 (+18.52%)</td><td>0.01 <b>(-29.37%)</b></td><td>550.60 (-15.63%)</td><td>392.28 (-10.65%)</td><td>382.20 <b>(-23.76%)</b></td><td>251.20 (+1.58%)</td><td>118.22 <b>(-34.45%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>652.60 (n/a)</td><td>439.04 (n/a)</td><td>501.30 (n/a)</td><td>247.30 (n/a)</td><td>180.35 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (-13.16%)</td><td>0.02 (+14.53%)</td><td>0.03 <b>(+72.54%)</b></td><td>0.02 <b>(+90.94%)</b></td><td>0.01 <b>(-42.18%)</b></td><td>539.20 <b>(-47.63%)</b></td><td>387.54 <b>(-28.77%)</b></td><td>317.80 <b>(-42.04%)</b></td><td>288.50 (+15.17%)</td><td>120.94 <b>(-61.95%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1029.50 (n/a)</td><td>544.08 (n/a)</td><td>548.30 (n/a)</td><td>250.50 (n/a)</td><td>317.82 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 <b>(-28.20%)</b></td><td>0.04 (-15.89%)</td><td>0.05 (-17.37%)</td><td>0.03 (-3.49%)</td><td>0.01 <b>(-37.04%)</b></td><td>495.90 (+3.61%)</td><td>386.88 (+14.55%)</td><td>361.20 <b>(+21.01%)</b></td><td>284.30 <b>(+39.23%)</b></td><td>102.08 (-8.93%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>478.60 (n/a)</td><td>337.74 (n/a)</td><td>298.50 (n/a)</td><td>204.20 (n/a)</td><td>112.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (-18.03%)</td><td>0.04 <b>(-22.96%)</b></td><td>0.04 (-18.38%)</td><td>0.01 <b>(-72.81%)</b></td><td>0.02 (+9.83%)</td><td>1798.90 <b>(+267.80%)</b></td><td>645.44 <b>(+89.02%)</b></td><td>376.80 <b>(+22.50%)</b></td><td>241.80 <b>(+22.00%)</b></td><td>653.02 <b>(+412.44%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>489.10 (n/a)</td><td>341.46 (n/a)</td><td>307.60 (n/a)</td><td>198.20 (n/a)</td><td>127.43 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (+7.67%)</td><td>0.05 (-13.14%)</td><td>0.04 (-1.64%)</td><td>0.03 <b>(-20.56%)</b></td><td>0.02 (+5.82%)</td><td>577.70 <b>(+25.89%)</b></td><td>404.90 (+17.87%)</td><td>395.80 (+1.64%)</td><td>202.10 (-7.12%)</td><td>140.92 <b>(+23.05%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>458.90 (n/a)</td><td>343.50 (n/a)</td><td>389.40 (n/a)</td><td>217.60 (n/a)</td><td>114.53 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (+1.10%)</td><td>0.04 (+13.21%)</td><td>0.04 <b>(+20.85%)</b></td><td>0.03 (+14.22%)</td><td>0.01 (-19.15%)</td><td>506.00 (-12.46%)</td><td>399.40 (-14.15%)</td><td>407.70 (-17.24%)</td><td>290.60 (-1.09%)</td><td>82.50 <b>(-31.88%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>578.00 (n/a)</td><td>465.24 (n/a)</td><td>492.60 (n/a)</td><td>293.80 (n/a)</td><td>121.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (+11.06%)</td><td>0.05 <b>(+34.16%)</b></td><td>0.05 <b>(+34.08%)</b></td><td>0.03 <b>(+281.41%)</b></td><td>0.01 <b>(-26.56%)</b></td><td>521.50 <b>(-73.78%)</b></td><td>371.76 <b>(-48.68%)</b></td><td>298.90 <b>(-25.42%)</b></td><td>282.80 (-9.96%)</td><td>110.57 <b>(-84.47%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1989.20 (n/a)</td><td>724.44 (n/a)</td><td>400.80 (n/a)</td><td>314.10 (n/a)</td><td>712.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 <b>(+28.19%)</b></td><td>0.05 (+9.97%)</td><td>0.04 (-5.80%)</td><td>0.03 (+17.52%)</td><td>0.02 <b>(+30.85%)</b></td><td>515.20 (-14.90%)</td><td>400.66 (-7.31%)</td><td>461.50 (+6.17%)</td><td>224.00 <b>(-21.98%)</b></td><td>132.52 (-6.48%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>605.40 (n/a)</td><td>432.24 (n/a)</td><td>434.70 (n/a)</td><td>287.10 (n/a)</td><td>141.70 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 <b>(-52.84%)</b></td><td>0.03 <b>(-39.65%)</b></td><td>0.03 <b>(-46.76%)</b></td><td>0.03 (-5.82%)</td><td>0.00 <b>(-86.10%)</b></td><td>545.50 (+6.17%)</td><td>505.14 <b>(+50.25%)</b></td><td>519.90 <b>(+87.83%)</b></td><td>463.90 <b>(+112.02%)</b></td><td>38.06 <b>(-69.60%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>513.80 (n/a)</td><td>336.20 (n/a)</td><td>276.80 (n/a)</td><td>218.80 (n/a)</td><td>125.23 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (-0.67%)</td><td>0.04 (-8.42%)</td><td>0.04 (-3.08%)</td><td>0.02 <b>(-46.10%)</b></td><td>0.02 <b>(+29.16%)</b></td><td>1007.00 <b>(+85.55%)</b></td><td>517.82 <b>(+27.81%)</b></td><td>448.20 (+3.18%)</td><td>254.70 (+0.67%)</td><td>309.88 <b>(+128.46%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>542.70 (n/a)</td><td>405.14 (n/a)</td><td>434.40 (n/a)</td><td>253.00 (n/a)</td><td>135.63 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 <b>(+45.69%)</b></td><td>0.05 <b>(+33.37%)</b></td><td>0.04 <b>(+36.02%)</b></td><td>0.03 <b>(+26.78%)</b></td><td>0.03 <b>(+63.43%)</b></td><td>616.30 <b>(-21.13%)</b></td><td>406.26 (-19.20%)</td><td>369.00 <b>(-26.48%)</b></td><td>162.10 <b>(-31.37%)</b></td><td>184.43 (-4.52%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>781.40 (n/a)</td><td>502.78 (n/a)</td><td>501.90 (n/a)</td><td>236.20 (n/a)</td><td>193.16 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (+13.77%)</td><td>0.04 (-9.30%)</td><td>0.03 <b>(-44.23%)</b></td><td>0.03 (-2.21%)</td><td>0.02 <b>(+41.77%)</b></td><td>566.00 (+2.28%)</td><td>430.18 (+17.38%)</td><td>524.30 <b>(+79.31%)</b></td><td>243.20 (-12.11%)</td><td>160.43 <b>(+32.33%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>553.40 (n/a)</td><td>366.48 (n/a)</td><td>292.40 (n/a)</td><td>276.70 (n/a)</td><td>121.24 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (+9.98%)</td><td>0.03 (-1.96%)</td><td>0.03 (+1.90%)</td><td>0.02 <b>(-25.66%)</b></td><td>0.01 <b>(+111.64%)</b></td><td>705.10 <b>(+34.54%)</b></td><td>503.66 (+5.93%)</td><td>472.10 (-1.87%)</td><td>365.00 (-9.09%)</td><td>126.55 <b>(+167.52%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>524.10 (n/a)</td><td>475.46 (n/a)</td><td>481.10 (n/a)</td><td>401.50 (n/a)</td><td>47.31 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 (-3.39%)</td><td>0.03 <b>(-40.74%)</b></td><td>0.03 <b>(-40.43%)</b></td><td>0.01 <b>(-73.95%)</b></td><td>0.02 <b>(+66.86%)</b></td><td>1918.00 <b>(+283.83%)</b></td><td>1019.86 <b>(+170.53%)</b></td><td>569.30 <b>(+67.89%)</b></td><td>278.80 (+3.49%)</td><td>782.29 <b>(+645.81%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>499.70 (n/a)</td><td>376.98 (n/a)</td><td>339.10 (n/a)</td><td>269.40 (n/a)</td><td>104.89 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (-3.48%)</td><td>0.10 (-8.14%)</td><td>0.11 (-1.48%)</td><td>0.07 (-5.58%)</td><td>0.03 (+12.95%)</td><td>458.00 (+5.90%)</td><td>353.12 (+10.84%)</td><td>302.40 (+1.51%)</td><td>251.10 (+3.59%)</td><td>95.26 <b>(+29.46%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>432.50 (n/a)</td><td>318.58 (n/a)</td><td>297.90 (n/a)</td><td>242.40 (n/a)</td><td>73.59 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (-15.54%)</td><td>0.10 (-16.15%)</td><td>0.11 (-11.57%)</td><td>0.04 <b>(-35.65%)</b></td><td>0.03 (+8.89%)</td><td>734.90 <b>(+55.40%)</b></td><td>384.96 <b>(+27.97%)</b></td><td>307.30 (+13.06%)</td><td>274.50 (+18.42%)</td><td>196.12 <b>(+100.88%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>472.90 (n/a)</td><td>300.82 (n/a)</td><td>271.80 (n/a)</td><td>231.80 (n/a)</td><td>97.63 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (-9.14%)</td><td>0.08 (-7.93%)</td><td>0.07 <b>(+20.02%)</b></td><td>0.04 <b>(-24.23%)</b></td><td>0.03 (-15.02%)</td><td>764.60 <b>(+31.99%)</b></td><td>477.62 (+7.88%)</td><td>455.60 (-16.68%)</td><td>255.30 (+10.09%)</td><td>192.56 (+17.74%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>579.30 (n/a)</td><td>442.72 (n/a)</td><td>546.80 (n/a)</td><td>231.90 (n/a)</td><td>163.55 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 <b>(+21.05%)</b></td><td>0.12 <b>(+51.61%)</b></td><td>0.12 <b>(+48.69%)</b></td><td>0.06 <b>(+262.90%)</b></td><td>0.03 <b>(-20.70%)</b></td><td>518.00 <b>(-72.44%)</b></td><td>306.48 <b>(-55.54%)</b></td><td>265.20 <b>(-32.76%)</b></td><td>225.50 (-17.37%)</td><td>122.10 <b>(-82.01%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1879.70 (n/a)</td><td>689.40 (n/a)</td><td>394.40 (n/a)</td><td>272.90 (n/a)</td><td>678.86 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 <b>(-46.33%)</b></td><td>0.06 <b>(-23.80%)</b></td><td>0.06 (-6.32%)</td><td>0.05 <b>(+253.91%)</b></td><td>0.01 <b>(-83.72%)</b></td><td>595.80 <b>(-71.74%)</b></td><td>525.12 <b>(-27.47%)</b></td><td>544.20 (+6.75%)</td><td>442.40 <b>(+86.35%)</b></td><td>68.38 <b>(-91.30%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2108.50 (n/a)</td><td>723.98 (n/a)</td><td>509.80 (n/a)</td><td>237.40 (n/a)</td><td>786.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 <b>(-21.03%)</b></td><td>0.08 <b>(-24.66%)</b></td><td>0.09 (-16.85%)</td><td>0.02 <b>(-75.40%)</b></td><td>0.04 <b>(+31.40%)</b></td><td>1887.70 <b>(+306.48%)</b></td><td>680.50 <b>(+97.92%)</b></td><td>374.70 <b>(+20.25%)</b></td><td>294.60 <b>(+26.66%)</b></td><td>682.45 <b>(+567.29%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>464.40 (n/a)</td><td>343.82 (n/a)</td><td>311.60 (n/a)</td><td>232.60 (n/a)</td><td>102.27 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (-4.04%)</td><td>0.07 <b>(-37.77%)</b></td><td>0.06 <b>(-54.76%)</b></td><td>0.05 (+8.00%)</td><td>0.04 (-5.67%)</td><td>617.30 (-7.41%)</td><td>506.26 <b>(+55.07%)</b></td><td>544.00 <b>(+121.05%)</b></td><td>234.80 (+4.22%)</td><td>156.91 (-17.60%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>666.70 (n/a)</td><td>326.48 (n/a)</td><td>246.10 (n/a)</td><td>225.30 (n/a)</td><td>190.42 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 (-13.25%)</td><td>0.10 <b>(+28.06%)</b></td><td>0.11 <b>(+51.99%)</b></td><td>0.07 <b>(+38.13%)</b></td><td>0.02 <b>(-41.69%)</b></td><td>468.80 <b>(-27.60%)</b></td><td>333.16 <b>(-27.33%)</b></td><td>295.00 <b>(-34.20%)</b></td><td>287.10 (+15.25%)</td><td>77.01 <b>(-49.18%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>647.50 (n/a)</td><td>458.48 (n/a)</td><td>448.30 (n/a)</td><td>249.10 (n/a)</td><td>151.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (+1.33%)</td><td>0.09 (+6.06%)</td><td>0.10 <b>(+30.96%)</b></td><td>0.06 (-19.90%)</td><td>0.03 <b>(+20.58%)</b></td><td>559.00 <b>(+24.83%)</b></td><td>386.44 (-1.63%)</td><td>340.50 <b>(-23.64%)</b></td><td>241.10 (-1.31%)</td><td>134.57 <b>(+52.85%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>447.80 (n/a)</td><td>392.86 (n/a)</td><td>445.90 (n/a)</td><td>244.30 (n/a)</td><td>88.04 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (+18.91%)</td><td>0.07 <b>(-24.34%)</b></td><td>0.07 <b>(-35.61%)</b></td><td>0.02 <b>(-73.06%)</b></td><td>0.04 <b>(+73.14%)</b></td><td>1822.50 <b>(+271.26%)</b></td><td>699.68 <b>(+93.35%)</b></td><td>467.80 <b>(+55.31%)</b></td><td>230.70 (-15.93%)</td><td>637.89 <b>(+501.90%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>490.90 (n/a)</td><td>361.88 (n/a)</td><td>301.20 (n/a)</td><td>274.40 (n/a)</td><td>105.98 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (+20.00%)</td><td>0.09 <b>(+32.99%)</b></td><td>0.08 <b>(+40.38%)</b></td><td>0.05 <b>(+27.18%)</b></td><td>0.04 (+10.23%)</td><td>623.90 <b>(-21.37%)</b></td><td>409.48 <b>(-26.63%)</b></td><td>388.80 <b>(-28.77%)</b></td><td>218.00 (-16.67%)</td><td>147.12 <b>(-24.78%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>793.50 (n/a)</td><td>558.10 (n/a)</td><td>545.80 (n/a)</td><td>261.60 (n/a)</td><td>195.59 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 <b>(+30.98%)</b></td><td>0.09 (+14.14%)</td><td>0.07 (+10.77%)</td><td>0.07 <b>(+22.30%)</b></td><td>0.03 <b>(+29.42%)</b></td><td>470.30 (-18.24%)</td><td>389.08 (-11.61%)</td><td>449.00 (-9.73%)</td><td>239.10 <b>(-23.63%)</b></td><td>105.46 (-11.21%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>575.20 (n/a)</td><td>440.20 (n/a)</td><td>497.40 (n/a)</td><td>313.10 (n/a)</td><td>118.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>513.50 (n/a)</td><td>324.64 (n/a)</td><td>310.60 (n/a)</td><td>241.00 (n/a)</td><td>111.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>609.40 (n/a)</td><td>360.84 (n/a)</td><td>274.10 (n/a)</td><td>248.50 (n/a)</td><td>155.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.98 (n/a)</td><td>2.98 (n/a)</td><td>2.60 (n/a)</td><td>2.44 (n/a)</td><td>0.65 (n/a)</td><td>4293.90 (n/a)</td><td>3646.00 (n/a)</td><td>4037.40 (n/a)</td><td>2635.80 (n/a)</td><td>705.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>400.60 (n/a)</td><td>320.60 (n/a)</td><td>331.70 (n/a)</td><td>218.10 (n/a)</td><td>79.43 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>506.90 (n/a)</td><td>328.62 (n/a)</td><td>285.20 (n/a)</td><td>210.70 (n/a)</td><td>117.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (+5.81%)</td><td>0.01 (+17.96%)</td><td>0.01 (+3.81%)</td><td>0.01 <b>(+99.37%)</b></td><td>0.00 <b>(-37.95%)</b></td><td>394.60 <b>(-49.84%)</b></td><td>315.80 <b>(-26.48%)</b></td><td>281.50 (-3.66%)</td><td>244.80 (-5.48%)</td><td>70.52 <b>(-68.81%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>786.70 (n/a)</td><td>429.52 (n/a)</td><td>292.20 (n/a)</td><td>259.00 (n/a)</td><td>226.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (+15.71%)</td><td>0.02 <b>(-22.71%)</b></td><td>0.01 <b>(-39.13%)</b></td><td>0.00 <b>(-82.45%)</b></td><td>0.01 <b>(+154.20%)</b></td><td>2472.60 <b>(+469.72%)</b></td><td>781.14 <b>(+154.11%)</b></td><td>470.10 <b>(+64.31%)</b></td><td>214.70 (-13.57%)</td><td>953.21 <b>(+1200.38%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>434.00 (n/a)</td><td>307.40 (n/a)</td><td>286.10 (n/a)</td><td>248.40 (n/a)</td><td>73.30 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(+114.03%)</b></td><td>0.01 <b>(+72.40%)</b></td><td>0.01 <b>(+80.74%)</b></td><td>0.01 <b>(+31.48%)</b></td><td>0.01 <b>(+184.44%)</b></td><td>546.80 <b>(-23.94%)</b></td><td>356.74 <b>(-36.18%)</b></td><td>283.50 <b>(-44.68%)</b></td><td>186.00 <b>(-53.28%)</b></td><td>152.63 (+0.99%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>718.90 (n/a)</td><td>559.02 (n/a)</td><td>512.50 (n/a)</td><td>398.10 (n/a)</td><td>151.13 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(+69.15%)</b></td><td>0.01 <b>(+41.79%)</b></td><td>0.01 (+18.39%)</td><td>0.01 <b>(+113.69%)</b></td><td>0.00 <b>(+36.68%)</b></td><td>507.40 <b>(-53.20%)</b></td><td>397.16 <b>(-33.40%)</b></td><td>428.10 (-15.55%)</td><td>257.40 <b>(-40.88%)</b></td><td>98.76 <b>(-64.14%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1084.30 (n/a)</td><td>596.36 (n/a)</td><td>506.90 (n/a)</td><td>435.40 (n/a)</td><td>275.38 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (+7.06%)</td><td>0.01 (+14.18%)</td><td>0.02 (+13.16%)</td><td>0.01 <b>(+35.56%)</b></td><td>0.01 (+6.61%)</td><td>533.90 <b>(-26.24%)</b></td><td>358.62 (-14.80%)</td><td>260.10 (-11.62%)</td><td>226.90 (-6.59%)</td><td>158.53 <b>(-23.78%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>723.80 (n/a)</td><td>420.92 (n/a)</td><td>294.30 (n/a)</td><td>242.90 (n/a)</td><td>208.00 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(-41.44%)</b></td><td>0.01 (-10.04%)</td><td>0.01 <b>(+22.94%)</b></td><td>0.01 (+8.58%)</td><td>0.00 <b>(-65.71%)</b></td><td>556.60 (-7.89%)</td><td>434.36 (-6.15%)</td><td>428.70 (-18.67%)</td><td>292.20 <b>(+70.78%)</b></td><td>95.77 <b>(-43.96%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.30 (n/a)</td><td>462.82 (n/a)</td><td>527.10 (n/a)</td><td>171.10 (n/a)</td><td>170.90 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (+18.00%)</td><td>0.01 (+14.09%)</td><td>0.02 <b>(+32.88%)</b></td><td>0.01 (+0.14%)</td><td>0.00 <b>(+57.88%)</b></td><td>517.30 (-0.14%)</td><td>355.12 (-8.07%)</td><td>269.80 <b>(-24.74%)</b></td><td>257.20 (-15.23%)</td><td>125.47 <b>(+34.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.00 (n/a)</td><td>386.28 (n/a)</td><td>358.50 (n/a)</td><td>303.40 (n/a)</td><td>93.20 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(+25.15%)</b></td><td>0.01 (-10.17%)</td><td>0.01 (-15.69%)</td><td>0.00 <b>(-72.19%)</b></td><td>0.01 <b>(+84.91%)</b></td><td>2306.20 <b>(+259.67%)</b></td><td>818.56 <b>(+75.59%)</b></td><td>494.70 (+18.60%)</td><td>248.40 <b>(-20.10%)</b></td><td>841.35 <b>(+482.30%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.20 (n/a)</td><td>466.18 (n/a)</td><td>417.10 (n/a)</td><td>310.90 (n/a)</td><td>144.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (+10.47%)</td><td>0.01 <b>(+38.24%)</b></td><td>0.01 <b>(+38.31%)</b></td><td>0.01 <b>(+103.69%)</b></td><td>0.00 (-7.83%)</td><td>508.70 <b>(-50.90%)</b></td><td>381.46 <b>(-35.19%)</b></td><td>396.70 <b>(-27.70%)</b></td><td>220.20 (-9.49%)</td><td>125.52 <b>(-55.96%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1036.10 (n/a)</td><td>588.60 (n/a)</td><td>548.70 (n/a)</td><td>243.30 (n/a)</td><td>285.04 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(+21.72%)</b></td><td>0.01 (+3.03%)</td><td>0.01 (-15.17%)</td><td>0.01 <b>(-20.21%)</b></td><td>0.01 <b>(+56.40%)</b></td><td>652.20 <b>(+25.33%)</b></td><td>473.88 (+9.36%)</td><td>581.40 (+17.88%)</td><td>195.40 (-17.83%)</td><td>196.68 <b>(+64.30%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.40 (n/a)</td><td>433.34 (n/a)</td><td>493.20 (n/a)</td><td>237.80 (n/a)</td><td>119.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(+85.20%)</b></td><td>0.01 <b>(+31.82%)</b></td><td>0.01 (+12.87%)</td><td>0.01 <b>(+43.89%)</b></td><td>0.00 <b>(+124.67%)</b></td><td>718.50 <b>(-30.51%)</b></td><td>496.68 <b>(-20.93%)</b></td><td>489.30 (-11.41%)</td><td>250.20 <b>(-46.01%)</b></td><td>167.17 <b>(-27.30%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1033.90 (n/a)</td><td>628.14 (n/a)</td><td>552.30 (n/a)</td><td>463.40 (n/a)</td><td>229.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 <b>(+21.09%)</b></td><td>0.03 <b>(+36.55%)</b></td><td>0.03 <b>(+51.64%)</b></td><td>0.02 <b>(+29.66%)</b></td><td>0.01 (+6.12%)</td><td>506.60 <b>(-22.87%)</b></td><td>308.26 <b>(-28.36%)</b></td><td>263.90 <b>(-34.06%)</b></td><td>235.50 (-17.40%)</td><td>113.41 <b>(-27.81%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>656.80 (n/a)</td><td>430.32 (n/a)</td><td>400.20 (n/a)</td><td>285.10 (n/a)</td><td>157.11 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (-1.89%)</td><td>0.04 (+12.57%)</td><td>0.04 <b>(+62.84%)</b></td><td>0.03 <b>(+20.40%)</b></td><td>0.01 <b>(-24.73%)</b></td><td>472.90 (-16.95%)</td><td>331.38 (-17.30%)</td><td>280.30 <b>(-38.58%)</b></td><td>235.10 (+1.91%)</td><td>109.36 <b>(-31.70%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>569.40 (n/a)</td><td>400.70 (n/a)</td><td>456.40 (n/a)</td><td>230.70 (n/a)</td><td>160.12 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (-18.48%)</td><td>0.02 <b>(-25.68%)</b></td><td>0.02 <b>(-49.61%)</b></td><td>0.02 <b>(+27.74%)</b></td><td>0.01 <b>(-45.73%)</b></td><td>528.10 <b>(-21.72%)</b></td><td>427.56 (+19.24%)</td><td>484.10 <b>(+98.48%)</b></td><td>278.90 <b>(+22.70%)</b></td><td>103.55 <b>(-46.14%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>674.60 (n/a)</td><td>358.58 (n/a)</td><td>243.90 (n/a)</td><td>227.30 (n/a)</td><td>192.27 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (-0.64%)</td><td>0.03 (+8.31%)</td><td>0.03 (+1.68%)</td><td>0.02 (-1.81%)</td><td>0.01 (+0.17%)</td><td>611.80 (+1.85%)</td><td>379.64 (-7.54%)</td><td>378.00 (-1.64%)</td><td>238.10 (+0.63%)</td><td>146.16 (+1.64%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.70 (n/a)</td><td>410.60 (n/a)</td><td>384.30 (n/a)</td><td>236.60 (n/a)</td><td>143.80 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 <b>(+34.66%)</b></td><td>0.02 <b>(+29.47%)</b></td><td>0.02 <b>(+42.32%)</b></td><td>0.01 (-0.94%)</td><td>0.01 <b>(+107.96%)</b></td><td>638.90 (+0.95%)</td><td>407.46 (-17.94%)</td><td>335.20 <b>(-29.73%)</b></td><td>280.70 <b>(-25.74%)</b></td><td>146.65 <b>(+57.87%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>632.90 (n/a)</td><td>496.52 (n/a)</td><td>477.00 (n/a)</td><td>378.00 (n/a)</td><td>92.89 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (+0.02%)</td><td>0.03 <b>(+24.59%)</b></td><td>0.04 <b>(+60.57%)</b></td><td>0.02 (+1.40%)</td><td>0.01 (+11.58%)</td><td>518.50 (-1.39%)</td><td>364.64 (-18.23%)</td><td>292.20 <b>(-37.74%)</b></td><td>261.00 (-0.04%)</td><td>123.06 (+15.73%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.80 (n/a)</td><td>445.94 (n/a)</td><td>469.30 (n/a)</td><td>261.10 (n/a)</td><td>106.33 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (+0.17%)</td><td>0.02 (+10.42%)</td><td>0.02 <b>(+22.04%)</b></td><td>0.02 <b>(+24.07%)</b></td><td>0.00 <b>(-20.79%)</b></td><td>502.70 (-19.40%)</td><td>438.40 (-12.73%)</td><td>463.20 (-18.06%)</td><td>292.30 (-0.17%)</td><td>83.68 <b>(-37.52%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.70 (n/a)</td><td>502.34 (n/a)</td><td>565.30 (n/a)</td><td>292.80 (n/a)</td><td>133.93 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.04 (+10.76%)</td><td>0.03 (+8.70%)</td><td>0.03 <b>(+22.16%)</b></td><td>0.01 <b>(-29.44%)</b></td><td>0.01 <b>(+88.10%)</b></td><td>683.60 <b>(+41.71%)</b></td><td>442.42 (+7.31%)</td><td>361.50 (-18.14%)</td><td>242.00 (-9.70%)</td><td>219.31 <b>(+158.98%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>482.40 (n/a)</td><td>412.30 (n/a)</td><td>441.60 (n/a)</td><td>268.00 (n/a)</td><td>84.68 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.03 (+9.32%)</td><td>0.02 (-1.95%)</td><td>0.01 (-12.03%)</td><td>0.01 (-7.80%)</td><td>0.01 <b>(+31.22%)</b></td><td>605.80 (+8.45%)</td><td>502.08 (+6.16%)</td><td>578.00 (+13.67%)</td><td>264.50 (-8.54%)</td><td>142.26 <b>(+33.87%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.60 (n/a)</td><td>472.96 (n/a)</td><td>508.50 (n/a)</td><td>289.20 (n/a)</td><td>106.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 <b>(+51.13%)</b></td><td>0.03 <b>(+74.68%)</b></td><td>0.04 <b>(+116.67%)</b></td><td>0.01 <b>(+187.09%)</b></td><td>0.01 <b>(+58.59%)</b></td><td>673.20 <b>(-65.17%)</b></td><td>380.88 <b>(-50.22%)</b></td><td>245.20 <b>(-53.86%)</b></td><td>203.00 <b>(-33.85%)</b></td><td>213.41 <b>(-67.65%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1932.60 (n/a)</td><td>765.10 (n/a)</td><td>531.40 (n/a)</td><td>306.90 (n/a)</td><td>659.70 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (+18.43%)</td><td>0.02 <b>(+24.91%)</b></td><td>0.02 (+17.86%)</td><td>0.01 <b>(+262.66%)</b></td><td>0.00 <b>(-45.36%)</b></td><td>669.50 <b>(-72.43%)</b></td><td>526.66 <b>(-43.10%)</b></td><td>524.30 (-15.15%)</td><td>394.70 (-15.57%)</td><td>99.28 <b>(-88.23%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2428.00 (n/a)</td><td>925.58 (n/a)</td><td>617.90 (n/a)</td><td>467.50 (n/a)</td><td>843.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 <b>(+32.96%)</b></td><td>0.05 (+5.01%)</td><td>0.03 <b>(-29.31%)</b></td><td>0.03 (+13.71%)</td><td>0.02 <b>(+72.54%)</b></td><td>528.30 (-12.05%)</td><td>400.18 (+3.52%)</td><td>502.10 <b>(+41.48%)</b></td><td>205.90 <b>(-24.80%)</b></td><td>159.87 <b>(+20.24%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>600.70 (n/a)</td><td>386.56 (n/a)</td><td>354.90 (n/a)</td><td>273.80 (n/a)</td><td>132.96 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (+5.37%)</td><td>0.08 <b>(+23.07%)</b></td><td>0.08 <b>(+58.26%)</b></td><td>0.05 (+6.38%)</td><td>0.02 <b>(+23.31%)</b></td><td>482.90 (-6.00%)</td><td>344.76 (-16.89%)</td><td>289.80 <b>(-36.82%)</b></td><td>248.40 (-5.08%)</td><td>112.07 (+13.45%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>513.70 (n/a)</td><td>414.80 (n/a)</td><td>458.70 (n/a)</td><td>261.70 (n/a)</td><td>98.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 <b>(+92.66%)</b></td><td>0.05 <b>(+59.76%)</b></td><td>0.05 <b>(+56.46%)</b></td><td>0.03 <b>(+33.78%)</b></td><td>0.02 <b>(+286.04%)</b></td><td>469.20 <b>(-25.26%)</b></td><td>336.68 <b>(-31.51%)</b></td><td>303.30 <b>(-36.09%)</b></td><td>221.80 <b>(-48.09%)</b></td><td>124.29 <b>(+51.30%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>627.80 (n/a)</td><td>491.58 (n/a)</td><td>474.60 (n/a)</td><td>427.30 (n/a)</td><td>82.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 <b>(+24.71%)</b></td><td>0.07 <b>(+26.83%)</b></td><td>0.08 <b>(+51.60%)</b></td><td>0.04 (+12.31%)</td><td>0.03 <b>(+48.73%)</b></td><td>506.00 (-10.96%)</td><td>346.36 (-16.61%)</td><td>264.30 <b>(-34.02%)</b></td><td>205.60 (-19.84%)</td><td>146.94 (+14.56%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>568.30 (n/a)</td><td>415.36 (n/a)</td><td>400.60 (n/a)</td><td>256.50 (n/a)</td><td>128.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (-17.68%)</td><td>0.05 <b>(-21.99%)</b></td><td>0.04 <b>(-33.73%)</b></td><td>0.03 (-14.06%)</td><td>0.02 (+1.86%)</td><td>507.70 (+16.34%)</td><td>378.54 <b>(+32.10%)</b></td><td>410.30 <b>(+50.90%)</b></td><td>233.80 <b>(+21.45%)</b></td><td>125.49 <b>(+38.02%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>436.40 (n/a)</td><td>286.56 (n/a)</td><td>271.90 (n/a)</td><td>192.50 (n/a)</td><td>90.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.06 <b>(-38.24%)</b></td><td>0.04 <b>(-24.73%)</b></td><td>0.05 (-18.01%)</td><td>0.03 (+3.44%)</td><td>0.01 <b>(-56.43%)</b></td><td>659.40 (-3.33%)</td><td>487.12 (+18.35%)</td><td>436.90 <b>(+21.97%)</b></td><td>332.80 <b>(+61.95%)</b></td><td>129.07 <b>(-31.63%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>682.10 (n/a)</td><td>411.60 (n/a)</td><td>358.20 (n/a)</td><td>205.50 (n/a)</td><td>188.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (-13.78%)</td><td>0.05 (-13.50%)</td><td>0.05 (-17.56%)</td><td>0.03 (-0.14%)</td><td>0.01 <b>(-29.29%)</b></td><td>492.30 (+0.14%)</td><td>367.36 (+10.12%)</td><td>332.50 <b>(+21.31%)</b></td><td>238.80 (+15.98%)</td><td>102.66 (-19.91%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>491.60 (n/a)</td><td>333.60 (n/a)</td><td>274.10 (n/a)</td><td>205.90 (n/a)</td><td>128.18 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 <b>(+40.57%)</b></td><td>0.05 <b>(+28.27%)</b></td><td>0.04 (+16.68%)</td><td>0.03 (+16.27%)</td><td>0.02 <b>(+108.32%)</b></td><td>535.20 (-14.00%)</td><td>387.92 (-16.88%)</td><td>416.60 (-14.30%)</td><td>246.00 <b>(-28.84%)</b></td><td>133.71 <b>(+23.23%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>622.30 (n/a)</td><td>466.68 (n/a)</td><td>486.10 (n/a)</td><td>345.70 (n/a)</td><td>108.50 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (-0.61%)</td><td>0.04 (+1.57%)</td><td>0.04 (-7.37%)</td><td>0.03 (+15.34%)</td><td>0.01 (-7.46%)</td><td>471.90 (-13.30%)</td><td>401.22 (-3.27%)</td><td>448.70 (+7.96%)</td><td>241.60 (+0.62%)</td><td>95.73 (-18.18%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>544.30 (n/a)</td><td>414.80 (n/a)</td><td>415.60 (n/a)</td><td>240.10 (n/a)</td><td>117.00 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 <b>(-36.07%)</b></td><td>0.04 <b>(-29.66%)</b></td><td>0.03 <b>(-32.67%)</b></td><td>0.03 (-8.20%)</td><td>0.01 <b>(-63.50%)</b></td><td>628.80 (+8.92%)</td><td>511.72 <b>(+27.97%)</b></td><td>526.70 <b>(+48.49%)</b></td><td>374.80 <b>(+56.43%)</b></td><td>95.99 <b>(-41.21%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>577.30 (n/a)</td><td>399.86 (n/a)</td><td>354.70 (n/a)</td><td>239.60 (n/a)</td><td>163.27 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.05 (-18.69%)</td><td>0.04 (-8.07%)</td><td>0.03 (+13.57%)</td><td>0.03 (-4.61%)</td><td>0.01 <b>(-34.71%)</b></td><td>604.00 (+4.82%)</td><td>484.40 (+4.14%)</td><td>477.30 (-11.94%)</td><td>313.50 <b>(+22.99%)</b></td><td>112.42 (-18.43%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>576.20 (n/a)</td><td>465.14 (n/a)</td><td>542.00 (n/a)</td><td>254.90 (n/a)</td><td>137.82 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (+0.01%)</td><td>0.09 (-15.69%)</td><td>0.08 <b>(-37.89%)</b></td><td>0.05 (-2.14%)</td><td>0.04 (-2.16%)</td><td>628.60 (+2.19%)</td><td>425.76 (+18.46%)</td><td>425.40 <b>(+61.01%)</b></td><td>241.60 (-0.04%)</td><td>163.19 (+1.74%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>615.10 (n/a)</td><td>359.42 (n/a)</td><td>264.20 (n/a)</td><td>241.70 (n/a)</td><td>160.39 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (+10.24%)</td><td>0.09 (+3.14%)</td><td>0.07 (-12.58%)</td><td>0.05 (-10.67%)</td><td>0.04 <b>(+42.77%)</b></td><td>599.50 (+11.95%)</td><td>400.98 (+3.04%)</td><td>441.60 (+14.37%)</td><td>226.50 (-9.29%)</td><td>148.26 <b>(+44.69%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>535.50 (n/a)</td><td>389.16 (n/a)</td><td>386.10 (n/a)</td><td>249.70 (n/a)</td><td>102.47 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.18 <b>(+63.58%)</b></td><td>0.11 <b>(+53.45%)</b></td><td>0.11 <b>(+48.01%)</b></td><td>0.05 <b>(+164.33%)</b></td><td>0.05 <b>(+44.24%)</b></td><td>772.50 <b>(-62.17%)</b></td><td>443.30 <b>(-45.50%)</b></td><td>357.50 <b>(-32.45%)</b></td><td>233.70 <b>(-38.85%)</b></td><td>206.18 <b>(-70.16%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>2042.00 (n/a)</td><td>813.42 (n/a)</td><td>529.20 (n/a)</td><td>382.20 (n/a)</td><td>690.91 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.17 <b>(+35.04%)</b></td><td>0.10 <b>(+22.03%)</b></td><td>0.08 (+9.86%)</td><td>0.07 <b>(+49.91%)</b></td><td>0.04 <b>(+45.07%)</b></td><td>440.60 <b>(-33.29%)</b></td><td>372.26 (-17.48%)</td><td>417.40 (-8.96%)</td><td>195.00 <b>(-25.97%)</b></td><td>101.14 <b>(-28.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>660.50 (n/a)</td><td>451.12 (n/a)</td><td>458.50 (n/a)</td><td>263.40 (n/a)</td><td>142.27 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.11 <b>(-30.44%)</b></td><td>0.08 (-14.70%)</td><td>0.06 (-12.74%)</td><td>0.06 (-4.39%)</td><td>0.03 <b>(-40.31%)</b></td><td>718.70 (+4.58%)</td><td>575.78 (+11.62%)</td><td>661.60 (+14.60%)</td><td>361.20 <b>(+43.73%)</b></td><td>162.70 (-2.77%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>687.20 (n/a)</td><td>515.86 (n/a)</td><td>577.30 (n/a)</td><td>251.30 (n/a)</td><td>167.34 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (+6.10%)</td><td>0.08 (+4.16%)</td><td>0.06 (-0.01%)</td><td>0.05 (+8.21%)</td><td>0.04 (+8.11%)</td><td>687.20 (-7.57%)</td><td>505.32 (-3.29%)</td><td>550.80 (+0.02%)</td><td>225.40 (-5.77%)</td><td>179.84 (-3.67%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>743.50 (n/a)</td><td>522.50 (n/a)</td><td>550.70 (n/a)</td><td>239.20 (n/a)</td><td>186.69 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (-3.23%)</td><td>0.09 (-3.37%)</td><td>0.07 (-10.44%)</td><td>0.06 (-7.10%)</td><td>0.03 (-2.98%)</td><td>611.90 (+7.63%)</td><td>451.04 (+3.51%)</td><td>505.30 (+11.67%)</td><td>269.60 (+3.33%)</td><td>136.71 (+3.58%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>568.50 (n/a)</td><td>435.74 (n/a)</td><td>452.50 (n/a)</td><td>260.90 (n/a)</td><td>131.99 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.16 (+16.26%)</td><td>0.10 <b>(+38.90%)</b></td><td>0.09 <b>(+60.35%)</b></td><td>0.06 <b>(+23.07%)</b></td><td>0.04 (+6.89%)</td><td>550.30 (-18.75%)</td><td>371.08 <b>(-29.55%)</b></td><td>353.10 <b>(-37.64%)</b></td><td>202.40 (-13.98%)</td><td>138.25 (-19.12%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>677.30 (n/a)</td><td>526.70 (n/a)</td><td>566.20 (n/a)</td><td>235.30 (n/a)</td><td>170.93 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 <b>(-29.44%)</b></td><td>0.08 (-13.95%)</td><td>0.07 <b>(+21.14%)</b></td><td>0.05 <b>(-21.37%)</b></td><td>0.02 <b>(-49.62%)</b></td><td>812.20 <b>(+27.16%)</b></td><td>523.76 (+7.55%)</td><td>498.70 (-17.46%)</td><td>378.40 <b>(+41.72%)</b></td><td>170.47 (-8.23%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>638.70 (n/a)</td><td>487.00 (n/a)</td><td>604.20 (n/a)</td><td>267.00 (n/a)</td><td>185.76 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.18 <b>(+93.21%)</b></td><td>0.07 (+10.60%)</td><td>0.06 (-13.06%)</td><td>0.02 (+11.21%)</td><td>0.06 <b>(+119.23%)</b></td><td>1733.10 (-10.08%)</td><td>768.68 (+4.54%)</td><td>573.60 (+15.02%)</td><td>178.80 <b>(-48.23%)</b></td><td>582.04 (-13.08%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1927.40 (n/a)</td><td>735.30 (n/a)</td><td>498.70 (n/a)</td><td>345.40 (n/a)</td><td>669.60 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (-2.55%)</td><td>0.04 <b>(-44.15%)</b></td><td>0.04 <b>(-51.07%)</b></td><td>0.01 <b>(-80.25%)</b></td><td>0.03 <b>(+73.11%)</b></td><td>2460.80 <b>(+406.23%)</b></td><td>932.26 <b>(+195.37%)</b></td><td>556.30 <b>(+104.37%)</b></td><td>251.40 (+2.61%)</td><td>887.55 <b>(+810.43%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>486.10 (n/a)</td><td>315.62 (n/a)</td><td>272.20 (n/a)</td><td>245.00 (n/a)</td><td>97.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 <b>(+53.30%)</b></td><td>0.08 <b>(+53.43%)</b></td><td>0.08 <b>(+73.28%)</b></td><td>0.04 <b>(+23.13%)</b></td><td>0.03 <b>(+78.92%)</b></td><td>507.30 (-18.78%)</td><td>313.82 <b>(-30.22%)</b></td><td>244.70 <b>(-42.29%)</b></td><td>166.00 <b>(-34.77%)</b></td><td>141.88 (+0.50%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>624.60 (n/a)</td><td>449.70 (n/a)</td><td>424.00 (n/a)</td><td>254.50 (n/a)</td><td>141.17 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (-0.16%)</td><td>0.05 (-13.28%)</td><td>0.04 (-8.92%)</td><td>0.03 (-18.22%)</td><td>0.02 (-5.80%)</td><td>648.70 <b>(+22.28%)</b></td><td>445.60 (+16.12%)</td><td>458.40 (+9.80%)</td><td>266.70 (+0.15%)</td><td>138.28 <b>(+20.85%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>530.50 (n/a)</td><td>383.74 (n/a)</td><td>417.50 (n/a)</td><td>266.30 (n/a)</td><td>114.42 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 (+15.12%)</td><td>0.05 (+2.36%)</td><td>0.04 (-13.34%)</td><td>0.03 (-14.53%)</td><td>0.02 <b>(+55.68%)</b></td><td>631.70 (+17.00%)</td><td>447.14 (+6.45%)</td><td>521.80 (+15.39%)</td><td>228.80 (-13.14%)</td><td>170.15 <b>(+63.02%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>539.90 (n/a)</td><td>420.06 (n/a)</td><td>452.20 (n/a)</td><td>263.40 (n/a)</td><td>104.38 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 <b>(+43.35%)</b></td><td>0.06 <b>(+35.49%)</b></td><td>0.05 (+5.32%)</td><td>0.03 (+13.09%)</td><td>0.03 <b>(+86.86%)</b></td><td>595.50 (-11.57%)</td><td>386.34 <b>(-20.51%)</b></td><td>432.80 (-5.05%)</td><td>209.80 <b>(-30.25%)</b></td><td>156.51 (+12.43%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>673.40 (n/a)</td><td>486.00 (n/a)</td><td>455.80 (n/a)</td><td>300.80 (n/a)</td><td>139.21 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (-10.24%)</td><td>0.05 (-11.69%)</td><td>0.05 <b>(-30.73%)</b></td><td>0.02 <b>(+97.71%)</b></td><td>0.02 <b>(-22.85%)</b></td><td>952.10 <b>(-49.42%)</b></td><td>510.44 <b>(-20.01%)</b></td><td>431.40 <b>(+44.38%)</b></td><td>250.40 (+11.44%)</td><td>279.32 <b>(-60.24%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1882.50 (n/a)</td><td>638.10 (n/a)</td><td>298.80 (n/a)</td><td>224.70 (n/a)</td><td>702.52 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (+16.31%)</td><td>0.07 (-3.36%)</td><td>0.08 (-4.67%)</td><td>0.04 <b>(-29.55%)</b></td><td>0.03 <b>(+84.14%)</b></td><td>656.30 <b>(+41.96%)</b></td><td>401.32 (+15.26%)</td><td>318.50 (+4.87%)</td><td>247.30 (-14.01%)</td><td>178.92 <b>(+127.70%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>462.30 (n/a)</td><td>348.20 (n/a)</td><td>303.70 (n/a)</td><td>287.60 (n/a)</td><td>78.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 <b>(-27.11%)</b></td><td>0.06 (-11.72%)</td><td>0.06 (-1.31%)</td><td>0.04 (-9.51%)</td><td>0.02 <b>(-30.03%)</b></td><td>606.80 (+10.51%)</td><td>423.14 (+10.31%)</td><td>420.90 (+1.32%)</td><td>287.70 <b>(+37.20%)</b></td><td>135.76 (+4.54%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>549.10 (n/a)</td><td>383.58 (n/a)</td><td>415.40 (n/a)</td><td>209.70 (n/a)</td><td>129.87 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (-13.02%)</td><td>0.06 (-8.18%)</td><td>0.06 (+2.96%)</td><td>0.04 (-3.37%)</td><td>0.02 (-17.85%)</td><td>569.50 (+3.49%)</td><td>430.92 (+7.79%)</td><td>405.20 (-2.88%)</td><td>297.90 (+14.97%)</td><td>114.07 (+1.59%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>550.30 (n/a)</td><td>399.78 (n/a)</td><td>417.20 (n/a)</td><td>259.10 (n/a)</td><td>112.28 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 <b>(+124.79%)</b></td><td>0.07 <b>(+85.37%)</b></td><td>0.05 <b>(+21.47%)</b></td><td>0.04 <b>(+228.87%)</b></td><td>0.04 <b>(+132.46%)</b></td><td>581.40 <b>(-69.59%)</b></td><td>416.34 <b>(-50.12%)</b></td><td>502.50 (-17.68%)</td><td>183.10 <b>(-55.52%)</b></td><td>169.91 <b>(-72.10%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1912.00 (n/a)</td><td>834.68 (n/a)</td><td>610.40 (n/a)</td><td>411.60 (n/a)</td><td>609.05 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (-1.42%)</td><td>0.07 (+4.37%)</td><td>0.05 (-5.71%)</td><td>0.04 (+2.07%)</td><td>0.03 (+3.66%)</td><td>635.10 (-2.04%)</td><td>419.56 (-2.49%)</td><td>478.70 (+6.07%)</td><td>207.20 (+1.42%)</td><td>173.84 (+5.86%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>648.30 (n/a)</td><td>430.28 (n/a)</td><td>451.30 (n/a)</td><td>204.30 (n/a)</td><td>164.22 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 <b>(-27.39%)</b></td><td>0.06 (-14.14%)</td><td>0.05 (-9.21%)</td><td>0.04 <b>(+197.34%)</b></td><td>0.02 <b>(-52.03%)</b></td><td>622.30 <b>(-66.37%)</b></td><td>486.54 <b>(-28.40%)</b></td><td>500.90 (+10.14%)</td><td>268.80 <b>(+37.70%)</b></td><td>137.56 <b>(-79.61%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1850.50 (n/a)</td><td>679.56 (n/a)</td><td>454.80 (n/a)</td><td>195.20 (n/a)</td><td>674.65 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.10 (+19.71%)</td><td>0.05 (-7.43%)</td><td>0.04 <b>(-42.19%)</b></td><td>0.03 (-5.59%)</td><td>0.03 <b>(+26.52%)</b></td><td>563.60 (+5.92%)</td><td>403.70 (+11.89%)</td><td>471.40 <b>(+72.93%)</b></td><td>182.20 (-16.46%)</td><td>159.31 (+3.36%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>532.10 (n/a)</td><td>360.80 (n/a)</td><td>272.60 (n/a)</td><td>218.10 (n/a)</td><td>154.12 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 (+3.69%)</td><td>0.06 <b>(+29.26%)</b></td><td>0.07 <b>(+87.25%)</b></td><td>0.03 (+1.73%)</td><td>0.02 (-5.06%)</td><td>592.00 (-1.69%)</td><td>331.70 <b>(-23.67%)</b></td><td>270.40 <b>(-46.60%)</b></td><td>234.60 (-3.58%)</td><td>148.99 (-5.61%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>602.20 (n/a)</td><td>434.58 (n/a)</td><td>506.40 (n/a)</td><td>243.30 (n/a)</td><td>157.84 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 <b>(+37.16%)</b></td><td>0.05 (+8.07%)</td><td>0.04 (-17.08%)</td><td>0.03 <b>(+25.27%)</b></td><td>0.02 <b>(+23.55%)</b></td><td>543.70 <b>(-20.17%)</b></td><td>406.66 (-9.12%)</td><td>429.50 <b>(+20.58%)</b></td><td>212.50 <b>(-27.10%)</b></td><td>130.96 <b>(-29.31%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>681.10 (n/a)</td><td>447.46 (n/a)</td><td>356.20 (n/a)</td><td>291.50 (n/a)</td><td>185.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (+7.79%)</td><td>0.05 (+10.50%)</td><td>0.05 (+11.48%)</td><td>0.03 <b>(+79.78%)</b></td><td>0.02 (-18.74%)</td><td>603.30 <b>(-44.38%)</b></td><td>401.10 <b>(-21.47%)</b></td><td>360.20 (-10.31%)</td><td>269.50 (-7.20%)</td><td>135.90 <b>(-58.79%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1084.60 (n/a)</td><td>510.76 (n/a)</td><td>401.60 (n/a)</td><td>290.40 (n/a)</td><td>329.81 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (-17.21%)</td><td>0.06 (+17.08%)</td><td>0.06 <b>(+44.82%)</b></td><td>0.04 (+17.70%)</td><td>0.01 <b>(-38.62%)</b></td><td>509.00 (-15.04%)</td><td>340.08 (-19.81%)</td><td>295.20 <b>(-30.95%)</b></td><td>269.20 <b>(+20.83%)</b></td><td>97.09 <b>(-31.97%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.10 (n/a)</td><td>424.08 (n/a)</td><td>427.50 (n/a)</td><td>222.80 (n/a)</td><td>142.72 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 <b>(+87.54%)</b></td><td>0.04 <b>(+22.62%)</b></td><td>0.04 (+1.54%)</td><td>0.03 (+2.11%)</td><td>0.02 <b>(+388.34%)</b></td><td>596.20 (-2.07%)</td><td>476.80 (-10.42%)</td><td>520.90 (-1.51%)</td><td>243.30 <b>(-46.69%)</b></td><td>136.87 <b>(+139.10%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>608.80 (n/a)</td><td>532.26 (n/a)</td><td>528.90 (n/a)</td><td>456.40 (n/a)</td><td>57.24 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.46 <b>(+31.50%)</b></td><td>0.28 (+9.86%)</td><td>0.21 (-10.73%)</td><td>0.20 (+14.98%)</td><td>0.11 <b>(+60.39%)</b></td><td>483.20 (-13.02%)</td><td>390.70 (-5.11%)</td><td>466.20 (+12.01%)</td><td>213.80 <b>(-23.97%)</b></td><td>118.48 (+9.65%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.35 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>555.50 (n/a)</td><td>411.74 (n/a)</td><td>416.20 (n/a)</td><td>281.20 (n/a)</td><td>108.05 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.45 <b>(+38.96%)</b></td><td>0.30 <b>(+77.80%)</b></td><td>0.26 <b>(+60.79%)</b></td><td>0.18 <b>(+239.56%)</b></td><td>0.12 (+13.91%)</td><td>534.10 <b>(-70.55%)</b></td><td>374.92 <b>(-56.12%)</b></td><td>372.40 <b>(-37.81%)</b></td><td>218.60 <b>(-28.04%)</b></td><td>143.72 <b>(-76.38%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.32 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>0.11 (n/a)</td><td>1813.50 (n/a)</td><td>854.44 (n/a)</td><td>598.80 (n/a)</td><td>303.80 (n/a)</td><td>608.44 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.35 (-2.78%)</td><td>0.23 (-9.10%)</td><td>0.21 <b>(-24.15%)</b></td><td>0.13 (-19.31%)</td><td>0.10 (+7.93%)</td><td>752.30 <b>(+23.94%)</b></td><td>483.32 (+13.83%)</td><td>471.70 <b>(+31.83%)</b></td><td>284.30 (+2.86%)</td><td>200.21 <b>(+26.12%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.36 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>607.00 (n/a)</td><td>424.58 (n/a)</td><td>357.80 (n/a)</td><td>276.40 (n/a)</td><td>158.75 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.30 (-18.57%)</td><td>0.16 <b>(-31.77%)</b></td><td>0.13 <b>(-43.89%)</b></td><td>0.09 <b>(-21.89%)</b></td><td>0.08 (-14.95%)</td><td>777.70 <b>(+28.04%)</b></td><td>550.50 <b>(+47.03%)</b></td><td>560.30 <b>(+78.21%)</b></td><td>242.80 <b>(+22.81%)</b></td><td>195.51 (+19.23%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.37 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>607.40 (n/a)</td><td>374.42 (n/a)</td><td>314.40 (n/a)</td><td>197.70 (n/a)</td><td>163.97 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.17 <b>(-40.24%)</b></td><td>0.16 (-14.48%)</td><td>0.16 (+14.72%)</td><td>0.14 <b>(+28.89%)</b></td><td>0.02 <b>(-81.10%)</b></td><td>530.40 <b>(-22.41%)</b></td><td>474.04 (-0.07%)</td><td>465.30 (-12.83%)</td><td>423.10 <b>(+67.30%)</b></td><td>49.58 <b>(-74.71%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>683.60 (n/a)</td><td>474.36 (n/a)</td><td>533.80 (n/a)</td><td>252.90 (n/a)</td><td>196.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.24 <b>(-34.76%)</b></td><td>0.19 (+5.47%)</td><td>0.17 <b>(+25.40%)</b></td><td>0.15 <b>(+36.87%)</b></td><td>0.04 <b>(-59.08%)</b></td><td>500.00 <b>(-26.94%)</b></td><td>411.30 (-18.53%)</td><td>439.60 <b>(-20.25%)</b></td><td>307.40 <b>(+53.32%)</b></td><td>91.62 <b>(-51.88%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.37 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>684.40 (n/a)</td><td>504.86 (n/a)</td><td>551.20 (n/a)</td><td>200.50 (n/a)</td><td>190.41 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 <b>(-20.06%)</b></td><td>0.12 (+1.87%)</td><td>0.12 (+5.77%)</td><td>0.08 (+12.29%)</td><td>0.02 <b>(-44.21%)</b></td><td>434.40 (-10.95%)</td><td>325.20 (-6.59%)</td><td>300.30 (-5.45%)</td><td>269.90 <b>(+25.07%)</b></td><td>66.23 <b>(-37.35%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>487.80 (n/a)</td><td>348.14 (n/a)</td><td>317.60 (n/a)</td><td>215.80 (n/a)</td><td>105.72 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (+1.34%)</td><td>0.10 (-14.60%)</td><td>0.08 <b>(-40.64%)</b></td><td>0.07 (+6.88%)</td><td>0.04 (+15.08%)</td><td>542.70 (-6.43%)</td><td>412.58 (+18.80%)</td><td>472.30 <b>(+68.44%)</b></td><td>263.40 (-1.31%)</td><td>134.94 (+1.35%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>580.00 (n/a)</td><td>347.28 (n/a)</td><td>280.40 (n/a)</td><td>266.90 (n/a)</td><td>133.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.17 (+19.44%)</td><td>0.10 (+16.40%)</td><td>0.07 (-5.30%)</td><td>0.06 <b>(+25.96%)</b></td><td>0.05 <b>(+31.91%)</b></td><td>586.20 <b>(-20.61%)</b></td><td>430.20 (-11.71%)</td><td>512.20 (+5.61%)</td><td>220.00 (-16.25%)</td><td>161.25 (-8.96%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>738.40 (n/a)</td><td>487.26 (n/a)</td><td>485.00 (n/a)</td><td>262.70 (n/a)</td><td>177.11 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.20 (-7.59%)</td><td>0.11 (-10.39%)</td><td>0.08 <b>(-39.62%)</b></td><td>0.07 (+7.73%)</td><td>0.06 (-11.79%)</td><td>521.80 (-7.17%)</td><td>391.02 (+6.12%)</td><td>470.70 <b>(+65.62%)</b></td><td>183.10 (+8.22%)</td><td>143.53 (-19.12%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>562.10 (n/a)</td><td>368.48 (n/a)</td><td>284.20 (n/a)</td><td>169.20 (n/a)</td><td>177.46 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.24 <b>(+47.83%)</b></td><td>0.11 <b>(+24.08%)</b></td><td>0.07 (-1.52%)</td><td>0.02 <b>(-34.13%)</b></td><td>0.09 <b>(+72.48%)</b></td><td>1650.30 <b>(+51.81%)</b></td><td>623.30 (+15.44%)</td><td>532.70 (+1.54%)</td><td>151.90 <b>(-32.37%)</b></td><td>602.59 <b>(+77.79%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1087.10 (n/a)</td><td>539.94 (n/a)</td><td>524.60 (n/a)</td><td>224.60 (n/a)</td><td>338.93 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 <b>(+76.07%)</b></td><td>0.09 (+10.75%)</td><td>0.07 (-14.62%)</td><td>0.06 (-8.87%)</td><td>0.04 <b>(+483.84%)</b></td><td>591.90 (+9.73%)</td><td>484.88 (+0.54%)</td><td>554.80 (+17.12%)</td><td>243.10 <b>(-43.21%)</b></td><td>147.85 <b>(+261.29%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>539.40 (n/a)</td><td>482.26 (n/a)</td><td>473.70 (n/a)</td><td>428.10 (n/a)</td><td>40.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (-18.17%)</td><td>0.11 (-1.52%)</td><td>0.09 (-1.33%)</td><td>0.08 <b>(+51.89%)</b></td><td>0.03 <b>(-43.73%)</b></td><td>517.40 <b>(-34.16%)</b></td><td>400.86 (-14.73%)</td><td>446.40 (+1.36%)</td><td>278.50 <b>(+22.20%)</b></td><td>113.29 <b>(-54.33%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>785.90 (n/a)</td><td>470.12 (n/a)</td><td>440.40 (n/a)</td><td>227.90 (n/a)</td><td>248.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (-6.33%)</td><td>0.09 <b>(-26.89%)</b></td><td>0.09 <b>(-29.31%)</b></td><td>0.04 <b>(-64.90%)</b></td><td>0.04 <b>(+110.65%)</b></td><td>1108.60 <b>(+184.84%)</b></td><td>538.42 <b>(+63.12%)</b></td><td>431.40 <b>(+41.44%)</b></td><td>304.10 (+6.74%)</td><td>323.60 <b>(+607.30%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>389.20 (n/a)</td><td>330.08 (n/a)</td><td>305.00 (n/a)</td><td>284.90 (n/a)</td><td>45.75 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.16 (-1.85%)</td><td>0.10 (-13.77%)</td><td>0.08 (-7.78%)</td><td>0.07 (-7.65%)</td><td>0.04 (-15.59%)</td><td>595.50 (+8.27%)</td><td>467.36 (+13.31%)</td><td>522.90 (+8.44%)</td><td>262.00 (+1.91%)</td><td>131.45 (-6.26%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>550.00 (n/a)</td><td>412.46 (n/a)</td><td>482.20 (n/a)</td><td>257.10 (n/a)</td><td>140.22 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.15 (-18.96%)</td><td>0.11 (+8.49%)</td><td>0.11 <b>(+33.64%)</b></td><td>0.08 <b>(+266.04%)</b></td><td>0.03 <b>(-54.70%)</b></td><td>506.40 <b>(-72.68%)</b></td><td>399.76 <b>(-42.37%)</b></td><td>376.90 <b>(-25.17%)</b></td><td>269.90 <b>(+23.41%)</b></td><td>101.51 <b>(-84.77%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1853.70 (n/a)</td><td>693.68 (n/a)</td><td>503.70 (n/a)</td><td>218.70 (n/a)</td><td>666.55 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.17 (+0.61%)</td><td>0.12 (+5.51%)</td><td>0.10 (+15.13%)</td><td>0.07 (-3.09%)</td><td>0.05 (+11.99%)</td><td>593.40 (+3.20%)</td><td>393.18 (-2.99%)</td><td>394.50 (-13.14%)</td><td>241.80 (-0.62%)</td><td>152.30 (+11.10%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>575.00 (n/a)</td><td>405.30 (n/a)</td><td>454.20 (n/a)</td><td>243.30 (n/a)</td><td>137.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.19 <b>(+27.70%)</b></td><td>0.13 <b>(+28.26%)</b></td><td>0.16 <b>(+73.05%)</b></td><td>0.06 (-17.62%)</td><td>0.05 <b>(+88.64%)</b></td><td>660.00 <b>(+21.39%)</b></td><td>374.76 (-11.67%)</td><td>262.10 <b>(-42.22%)</b></td><td>213.50 <b>(-21.71%)</b></td><td>189.60 <b>(+89.58%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>543.70 (n/a)</td><td>424.28 (n/a)</td><td>453.60 (n/a)</td><td>272.70 (n/a)</td><td>100.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (-8.12%)</td><td>0.07 (-5.80%)</td><td>0.06 (-0.59%)</td><td>0.01 <b>(-73.85%)</b></td><td>0.05 <b>(+20.18%)</b></td><td>2433.00 <b>(+282.43%)</b></td><td>855.84 <b>(+65.03%)</b></td><td>578.40 (+0.59%)</td><td>264.60 (+8.84%)</td><td>896.40 <b>(+453.42%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>636.20 (n/a)</td><td>518.60 (n/a)</td><td>575.00 (n/a)</td><td>243.10 (n/a)</td><td>161.97 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.17 <b>(+37.27%)</b></td><td>0.11 <b>(+25.18%)</b></td><td>0.12 <b>(+28.64%)</b></td><td>0.05 (-15.02%)</td><td>0.04 <b>(+75.12%)</b></td><td>674.70 (+17.69%)</td><td>374.22 (-12.72%)</td><td>301.70 <b>(-22.24%)</b></td><td>209.60 <b>(-27.15%)</b></td><td>179.31 <b>(+54.84%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>573.30 (n/a)</td><td>428.74 (n/a)</td><td>388.00 (n/a)</td><td>287.70 (n/a)</td><td>115.80 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.12 (-7.29%)</td><td>0.07 (-6.85%)</td><td>0.07 (-0.55%)</td><td>0.02 (+2.13%)</td><td>0.04 (-8.95%)</td><td>1892.60 (-2.09%)</td><td>750.62 (+2.59%)</td><td>510.90 (+0.55%)</td><td>286.90 (+7.86%)</td><td>648.95 (-4.58%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1933.00 (n/a)</td><td>731.70 (n/a)</td><td>508.10 (n/a)</td><td>266.00 (n/a)</td><td>680.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.09 <b>(-35.26%)</b></td><td>0.07 <b>(-22.79%)</b></td><td>0.07 (-8.93%)</td><td>0.06 (-7.39%)</td><td>0.02 <b>(-56.76%)</b></td><td>579.10 (+7.98%)</td><td>489.52 <b>(+21.21%)</b></td><td>520.70 (+9.81%)</td><td>367.10 <b>(+54.44%)</b></td><td>94.44 <b>(-26.96%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>536.30 (n/a)</td><td>403.86 (n/a)</td><td>474.20 (n/a)</td><td>237.70 (n/a)</td><td>129.30 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.18 <b>(+37.56%)</b></td><td>0.10 (+18.29%)</td><td>0.08 <b>(+26.81%)</b></td><td>0.05 <b>(+25.03%)</b></td><td>0.05 <b>(+20.87%)</b></td><td>635.90 <b>(-20.01%)</b></td><td>418.14 (-16.79%)</td><td>459.40 <b>(-21.13%)</b></td><td>195.80 <b>(-27.32%)</b></td><td>176.07 <b>(-23.01%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>795.00 (n/a)</td><td>502.54 (n/a)</td><td>582.50 (n/a)</td><td>269.40 (n/a)</td><td>228.68 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.08 <b>(-34.19%)</b></td><td>0.06 <b>(-30.72%)</b></td><td>0.06 <b>(-36.52%)</b></td><td>0.06 (-2.20%)</td><td>0.01 <b>(-64.21%)</b></td><td>623.70 (+2.25%)</td><td>548.58 <b>(+33.70%)</b></td><td>568.20 <b>(+57.53%)</b></td><td>419.60 <b>(+51.97%)</b></td><td>82.11 <b>(-43.97%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>610.00 (n/a)</td><td>410.30 (n/a)</td><td>360.70 (n/a)</td><td>276.10 (n/a)</td><td>146.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.47 (+5.77%)</td><td>0.34 (+1.35%)</td><td>0.38 (+6.22%)</td><td>0.05 <b>(-73.03%)</b></td><td>0.17 <b>(+71.17%)</b></td><td>2466.50 <b>(+270.74%)</b></td><td>752.80 <b>(+76.47%)</b></td><td>347.80 (-5.85%)</td><td>279.60 (-5.44%)</td><td>958.66 <b>(+547.64%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>665.30 (n/a)</td><td>426.60 (n/a)</td><td>369.40 (n/a)</td><td>295.70 (n/a)</td><td>148.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.56 <b>(+40.56%)</b></td><td>0.45 <b>(+47.72%)</b></td><td>0.43 <b>(+56.68%)</b></td><td>0.34 <b>(+71.78%)</b></td><td>0.08 (+2.99%)</td><td>383.00 <b>(-41.78%)</b></td><td>302.16 <b>(-34.44%)</b></td><td>305.10 <b>(-36.17%)</b></td><td>236.00 <b>(-28.85%)</b></td><td>56.04 <b>(-56.66%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>657.90 (n/a)</td><td>460.90 (n/a)</td><td>478.00 (n/a)</td><td>331.70 (n/a)</td><td>129.30 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.39 (-15.05%)</td><td>0.29 (-14.57%)</td><td>0.28 <b>(-31.61%)</b></td><td>0.21 <b>(+214.37%)</b></td><td>0.07 <b>(-57.41%)</b></td><td>611.70 <b>(-68.19%)</b></td><td>466.72 <b>(-27.27%)</b></td><td>469.90 <b>(+46.20%)</b></td><td>339.30 (+17.73%)</td><td>105.87 <b>(-85.23%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.45 (n/a)</td><td>0.34 (n/a)</td><td>0.41 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1923.00 (n/a)</td><td>641.68 (n/a)</td><td>321.40 (n/a)</td><td>288.20 (n/a)</td><td>716.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (-10.14%)</td><td>0.01 (-13.90%)</td><td>0.01 (-1.99%)</td><td>0.01 <b>(-29.85%)</b></td><td>0.00 <b>(+68.27%)</b></td><td>443.80 <b>(+42.56%)</b></td><td>344.00 (+19.90%)</td><td>310.20 (+2.01%)</td><td>273.00 (+11.29%)</td><td>80.04 <b>(+163.22%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>311.30 (n/a)</td><td>286.90 (n/a)</td><td>304.10 (n/a)</td><td>245.30 (n/a)</td><td>30.41 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(+23.73%)</b></td><td>0.01 <b>(+22.25%)</b></td><td>0.02 <b>(+61.38%)</b></td><td>0.01 <b>(-21.46%)</b></td><td>0.00 <b>(+42.63%)</b></td><td>640.50 <b>(+27.34%)</b></td><td>346.80 (-12.14%)</td><td>272.00 <b>(-38.03%)</b></td><td>225.20 (-19.20%)</td><td>168.19 <b>(+62.96%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>503.00 (n/a)</td><td>394.74 (n/a)</td><td>438.90 (n/a)</td><td>278.70 (n/a)</td><td>103.21 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.01 (-1.30%)</td><td>0.01 <b>(+20.78%)</b></td><td>0.01 <b>(+50.75%)</b></td><td>0.01 <b>(+24.79%)</b></td><td>0.00 (-3.84%)</td><td>480.50 (-19.88%)</td><td>373.96 (-18.12%)</td><td>317.50 <b>(-33.66%)</b></td><td>302.30 (+1.34%)</td><td>90.01 (-19.59%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.70 (n/a)</td><td>456.70 (n/a)</td><td>478.60 (n/a)</td><td>298.30 (n/a)</td><td>111.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_llama_full]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>7.28 (-19.44%)</td><td>5.00 <b>(-21.38%)</b></td><td>5.07 <b>(-28.76%)</b></td><td>1.03 <b>(-73.03%)</b></td><td>2.57 (+15.77%)</td><td>2038.50 <b>(+270.77%)</b></td><td>701.86 <b>(+90.53%)</b></td><td>414.20 <b>(+40.36%)</b></td><td>288.30 <b>(+24.11%)</b></td><td>751.69 <b>(+436.54%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>9.03 (n/a)</td><td>6.36 (n/a)</td><td>7.11 (n/a)</td><td>3.82 (n/a)</td><td>2.22 (n/a)</td><td>549.80 (n/a)</td><td>368.38 (n/a)</td><td>295.10 (n/a)</td><td>232.30 (n/a)</td><td>140.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.47 <b>(-27.15%)</b></td><td>0.38 (-8.55%)</td><td>0.46 (+7.20%)</td><td>0.26 <b>(+27.13%)</b></td><td>0.11 <b>(-36.43%)</b></td><td>509.90 <b>(-21.34%)</b></td><td>371.42 (+0.64%)</td><td>289.30 (-6.71%)</td><td>281.30 <b>(+37.29%)</b></td><td>116.97 <b>(-33.16%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.64 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>648.20 (n/a)</td><td>369.06 (n/a)</td><td>310.10 (n/a)</td><td>204.90 (n/a)</td><td>175.00 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.45 (-14.96%)</td><td>0.36 (-14.91%)</td><td>0.37 (-18.36%)</td><td>0.26 (-6.68%)</td><td>0.07 <b>(-40.06%)</b></td><td>502.10 (+7.15%)</td><td>379.96 (+13.10%)</td><td>352.60 <b>(+22.47%)</b></td><td>290.90 (+17.58%)</td><td>80.62 <b>(-22.50%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.53 (n/a)</td><td>0.42 (n/a)</td><td>0.46 (n/a)</td><td>0.28 (n/a)</td><td>0.12 (n/a)</td><td>468.60 (n/a)</td><td>335.94 (n/a)</td><td>287.90 (n/a)</td><td>247.40 (n/a)</td><td>104.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.52 (-6.32%)</td><td>0.40 (-13.12%)</td><td>0.39 <b>(-26.01%)</b></td><td>0.26 (-3.87%)</td><td>0.10 (-15.50%)</td><td>516.10 (+4.03%)</td><td>349.86 (+13.33%)</td><td>341.70 <b>(+35.17%)</b></td><td>253.50 (+6.78%)</td><td>101.49 (-6.19%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.52 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>496.10 (n/a)</td><td>308.70 (n/a)</td><td>252.80 (n/a)</td><td>237.40 (n/a)</td><td>108.19 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.45 (-4.08%)</td><td>0.35 (-0.04%)</td><td>0.35 (+16.12%)</td><td>0.24 (-10.56%)</td><td>0.10 (+9.04%)</td><td>560.20 (+11.79%)</td><td>413.50 (+2.06%)</td><td>373.90 (-13.89%)</td><td>295.70 (+4.27%)</td><td>129.39 <b>(+25.57%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.09 (n/a)</td><td>501.10 (n/a)</td><td>405.14 (n/a)</td><td>434.20 (n/a)</td><td>283.60 (n/a)</td><td>103.04 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.48 (-17.93%)</td><td>0.41 (-11.30%)</td><td>0.46 (-0.64%)</td><td>0.29 (+7.45%)</td><td>0.08 <b>(-34.34%)</b></td><td>448.30 (-6.93%)</td><td>330.90 (+8.66%)</td><td>289.10 (+0.66%)</td><td>278.00 <b>(+21.82%)</b></td><td>73.81 <b>(-28.44%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.58 (n/a)</td><td>0.47 (n/a)</td><td>0.46 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>481.70 (n/a)</td><td>304.54 (n/a)</td><td>287.20 (n/a)</td><td>228.20 (n/a)</td><td>103.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 (+6.78%)</td><td>0.02 <b>(+44.41%)</b></td><td>0.01 <b>(+66.31%)</b></td><td>0.01 <b>(+61.75%)</b></td><td>0.00 <b>(-41.59%)</b></td><td>319.90 <b>(-38.17%)</b></td><td>274.28 <b>(-35.16%)</b></td><td>291.10 <b>(-39.88%)</b></td><td>225.50 (-6.31%)</td><td>39.03 <b>(-66.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>517.40 (n/a)</td><td>423.00 (n/a)</td><td>484.20 (n/a)</td><td>240.70 (n/a)</td><td>116.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.02 <b>(+24.17%)</b></td><td>0.01 <b>(+52.21%)</b></td><td>0.01 <b>(+69.16%)</b></td><td>0.01 <b>(+277.10%)</b></td><td>0.00 (-11.97%)</td><td>508.80 <b>(-73.48%)</b></td><td>373.58 <b>(-51.12%)</b></td><td>310.30 <b>(-40.88%)</b></td><td>264.60 (-19.48%)</td><td>118.18 <b>(-81.99%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1918.60 (n/a)</td><td>764.28 (n/a)</td><td>524.90 (n/a)</td><td>328.60 (n/a)</td><td>656.25 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.00 (+16.67%)</td><td>0.00 (+5.26%)</td><td>0.00 <b>(-25.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+31.10%)</b></td><td>21693.04 (+14.82%)</td><td>13200.60 (+8.27%)</td><td>14460.33 <b>(+40.62%)</b></td><td>6026.43 (-14.12%)</td><td>6713.74 <b>(+21.40%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18893.06 (n/a)</td><td>12192.50 (n/a)</td><td>10283.14 (n/a)</td><td>7017.00 (n/a)</td><td>5530.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.00 (-9.09%)</td><td>0.00 (-17.14%)</td><td>0.00 (-16.67%)</td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (-6.36%)</td><td>19257.90 (+12.42%)</td><td>16043.83 <b>(+21.24%)</b></td><td>17439.10 <b>(+23.47%)</b></td><td>8119.11 (+7.29%)</td><td>4496.81 (+7.39%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17130.83 (n/a)</td><td>13233.35 (n/a)</td><td>14123.64 (n/a)</td><td>7567.52 (n/a)</td><td>4187.24 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (-3.00%)</td><td>0.09 <b>(-23.23%)</b></td><td>0.08 <b>(-41.98%)</b></td><td>0.08 (-12.75%)</td><td>0.03 (-6.10%)</td><td>27848.51 (+14.60%)</td><td>24111.21 <b>(+30.10%)</b></td><td>26231.06 <b>(+72.29%)</b></td><td>14728.32 (+3.12%)</td><td>5317.83 (+4.10%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>24300.26 (n/a)</td><td>18532.32 (n/a)</td><td>15224.72 (n/a)</td><td>14282.91 (n/a)</td><td>5108.41 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>2.62 (+8.01%)</td><td>1.26 <b>(-27.75%)</b></td><td>0.98 <b>(-49.39%)</b></td><td>0.30 <b>(-69.55%)</b></td><td>1.05 <b>(+59.92%)</b></td><td>3513.50 <b>(+228.46%)</b></td><td>1748.44 <b>(+154.65%)</b></td><td>1069.10 <b>(+97.62%)</b></td><td>400.60 (-7.42%)</td><td>1519.10 <b>(+420.96%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>2.42 (n/a)</td><td>1.75 (n/a)</td><td>1.94 (n/a)</td><td>0.98 (n/a)</td><td>0.66 (n/a)</td><td>1069.70 (n/a)</td><td>686.60 (n/a)</td><td>541.00 (n/a)</td><td>432.70 (n/a)</td><td>291.60 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.57 (+13.33%)</td><td>1.90 (+16.88%)</td><td>1.64 (-9.03%)</td><td>1.05 <b>(+256.31%)</b></td><td>0.97 (-8.88%)</td><td>996.60 <b>(-71.94%)</b></td><td>649.16 <b>(-46.59%)</b></td><td>639.90 (+9.93%)</td><td>293.50 (-11.76%)</td><td>252.74 <b>(-81.02%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.15 (n/a)</td><td>1.62 (n/a)</td><td>1.80 (n/a)</td><td>0.30 (n/a)</td><td>1.07 (n/a)</td><td>3551.10 (n/a)</td><td>1215.48 (n/a)</td><td>582.10 (n/a)</td><td>332.60 (n/a)</td><td>1331.32 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.54 (+17.25%)</td><td>1.76 (-18.89%)</td><td>1.50 <b>(-42.28%)</b></td><td>0.94 (-17.76%)</td><td>1.04 <b>(+26.02%)</b></td><td>1120.80 <b>(+21.60%)</b></td><td>734.98 <b>(+31.74%)</b></td><td>701.10 <b>(+73.24%)</b></td><td>296.50 (-14.70%)</td><td>321.17 <b>(+27.07%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.02 (n/a)</td><td>2.17 (n/a)</td><td>2.59 (n/a)</td><td>1.14 (n/a)</td><td>0.83 (n/a)</td><td>921.70 (n/a)</td><td>557.90 (n/a)</td><td>404.70 (n/a)</td><td>347.60 (n/a)</td><td>252.75 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>2.64 (+1.34%)</td><td>1.85 (+10.50%)</td><td>1.77 (-2.96%)</td><td>1.14 <b>(+171.91%)</b></td><td>0.58 <b>(-26.93%)</b></td><td>921.50 <b>(-63.22%)</b></td><td>616.92 <b>(-34.19%)</b></td><td>592.20 (+3.06%)</td><td>397.70 (-1.32%)</td><td>203.25 <b>(-76.94%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>2.60 (n/a)</td><td>1.67 (n/a)</td><td>1.82 (n/a)</td><td>0.42 (n/a)</td><td>0.80 (n/a)</td><td>2505.60 (n/a)</td><td>937.40 (n/a)</td><td>574.60 (n/a)</td><td>403.00 (n/a)</td><td>881.47 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>4.09 (-6.84%)</td><td>1.52 <b>(-55.16%)</b></td><td>1.00 <b>(-67.06%)</b></td><td>0.63 <b>(-73.69%)</b></td><td>1.45 <b>(+60.95%)</b></td><td>3347.80 <b>(+280.04%)</b></td><td>2148.42 <b>(+227.76%)</b></td><td>2086.90 <b>(+203.59%)</b></td><td>512.70 (+7.35%)</td><td>1117.30 <b>(+548.01%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>4.39 (n/a)</td><td>3.39 (n/a)</td><td>3.05 (n/a)</td><td>2.38 (n/a)</td><td>0.90 (n/a)</td><td>880.90 (n/a)</td><td>655.48 (n/a)</td><td>687.40 (n/a)</td><td>477.60 (n/a)</td><td>172.42 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>5.83 (-7.39%)</td><td>4.36 <b>(+27.20%)</b></td><td>4.54 <b>(+21.58%)</b></td><td>2.67 <b>(+362.43%)</b></td><td>1.39 <b>(-36.76%)</b></td><td>786.10 <b>(-78.38%)</b></td><td>527.40 <b>(-56.12%)</b></td><td>461.50 (-17.75%)</td><td>359.50 (+7.99%)</td><td>184.78 <b>(-86.64%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>6.30 (n/a)</td><td>3.43 (n/a)</td><td>3.74 (n/a)</td><td>0.58 (n/a)</td><td>2.20 (n/a)</td><td>3635.20 (n/a)</td><td>1201.98 (n/a)</td><td>561.10 (n/a)</td><td>332.90 (n/a)</td><td>1383.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.05 (+11.74%)</td><td>3.91 <b>(+36.90%)</b></td><td>3.75 <b>(+51.38%)</b></td><td>2.36 <b>(+262.61%)</b></td><td>1.34 <b>(-30.54%)</b></td><td>890.40 <b>(-72.42%)</b></td><td>587.00 <b>(-53.42%)</b></td><td>558.80 <b>(-33.94%)</b></td><td>346.40 (-10.51%)</td><td>195.51 <b>(-83.15%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.42 (n/a)</td><td>2.85 (n/a)</td><td>2.48 (n/a)</td><td>0.65 (n/a)</td><td>1.93 (n/a)</td><td>3228.70 (n/a)</td><td>1260.24 (n/a)</td><td>845.90 (n/a)</td><td>387.10 (n/a)</td><td>1160.36 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.75 (+2.08%)</td><td>3.15 (-6.76%)</td><td>2.71 <b>(-29.03%)</b></td><td>0.59 (-1.44%)</td><td>2.33 (+2.94%)</td><td>3552.20 (+1.46%)</td><td>1259.70 (+5.68%)</td><td>775.10 <b>(+40.93%)</b></td><td>310.50 (-2.05%)</td><td>1314.65 (-0.25%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>6.62 (n/a)</td><td>3.37 (n/a)</td><td>3.81 (n/a)</td><td>0.60 (n/a)</td><td>2.26 (n/a)</td><td>3501.10 (n/a)</td><td>1192.02 (n/a)</td><td>550.00 (n/a)</td><td>317.00 (n/a)</td><td>1317.98 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.80 <b>(-24.75%)</b></td><td>2.82 <b>(-28.71%)</b></td><td>2.80 <b>(-33.20%)</b></td><td>2.04 <b>(-22.32%)</b></td><td>0.63 <b>(-31.45%)</b></td><td>1026.70 <b>(+28.72%)</b></td><td>772.00 <b>(+38.71%)</b></td><td>749.50 <b>(+49.69%)</b></td><td>552.00 <b>(+32.88%)</b></td><td>169.20 (+13.60%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.05 (n/a)</td><td>3.96 (n/a)</td><td>4.19 (n/a)</td><td>2.63 (n/a)</td><td>0.92 (n/a)</td><td>797.60 (n/a)</td><td>556.54 (n/a)</td><td>500.70 (n/a)</td><td>415.40 (n/a)</td><td>148.94 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>6.31 <b>(+34.13%)</b></td><td>3.82 <b>(+67.36%)</b></td><td>3.61 <b>(+65.23%)</b></td><td>1.69 <b>(+184.08%)</b></td><td>1.76 (-0.45%)</td><td>1237.70 <b>(-64.80%)</b></td><td>669.38 <b>(-62.84%)</b></td><td>581.50 <b>(-39.48%)</b></td><td>332.60 <b>(-25.44%)</b></td><td>352.82 <b>(-77.19%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>4.70 (n/a)</td><td>2.28 (n/a)</td><td>2.18 (n/a)</td><td>0.60 (n/a)</td><td>1.77 (n/a)</td><td>3516.00 (n/a)</td><td>1801.56 (n/a)</td><td>960.80 (n/a)</td><td>446.10 (n/a)</td><td>1546.94 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>5.16 (-1.95%)</td><td>4.20 (-3.29%)</td><td>3.88 (-5.42%)</td><td>3.40 (-1.90%)</td><td>0.71 (+0.04%)</td><td>1234.20 (+1.94%)</td><td>1021.42 (+3.49%)</td><td>1079.90 (+5.73%)</td><td>812.70 (+2.00%)</td><td>167.29 (+3.67%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>5.26 (n/a)</td><td>4.34 (n/a)</td><td>4.11 (n/a)</td><td>3.46 (n/a)</td><td>0.71 (n/a)</td><td>1210.70 (n/a)</td><td>986.98 (n/a)</td><td>1021.40 (n/a)</td><td>796.80 (n/a)</td><td>161.37 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>7.70 (+0.06%)</td><td>4.11 (-15.67%)</td><td>3.58 <b>(-36.96%)</b></td><td>1.29 (+9.69%)</td><td>2.69 (-10.79%)</td><td>3255.60 (-8.83%)</td><td>1553.34 (+6.72%)</td><td>1170.50 <b>(+58.63%)</b></td><td>544.90 (-0.06%)</td><td>1126.50 (-13.61%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>7.69 (n/a)</td><td>4.87 (n/a)</td><td>5.68 (n/a)</td><td>1.17 (n/a)</td><td>3.02 (n/a)</td><td>3571.10 (n/a)</td><td>1455.50 (n/a)</td><td>737.90 (n/a)</td><td>545.20 (n/a)</td><td>1304.03 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>8.57 (-2.24%)</td><td>3.89 <b>(-37.99%)</b></td><td>3.88 <b>(-53.85%)</b></td><td>1.27 <b>(-25.71%)</b></td><td>2.91 (-10.78%)</td><td>3313.60 <b>(+34.60%)</b></td><td>1686.46 <b>(+68.57%)</b></td><td>1080.80 <b>(+116.68%)</b></td><td>489.20 (+2.30%)</td><td>1177.96 <b>(+37.75%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>8.77 (n/a)</td><td>6.27 (n/a)</td><td>8.41 (n/a)</td><td>1.70 (n/a)</td><td>3.26 (n/a)</td><td>2461.80 (n/a)</td><td>1000.48 (n/a)</td><td>498.80 (n/a)</td><td>478.20 (n/a)</td><td>855.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>9.15 (-2.17%)</td><td>4.99 <b>(-38.25%)</b></td><td>4.37 <b>(-44.25%)</b></td><td>1.68 <b>(-73.63%)</b></td><td>2.79 <b>(+121.20%)</b></td><td>2497.60 <b>(+279.23%)</b></td><td>1147.54 <b>(+116.40%)</b></td><td>958.70 <b>(+79.36%)</b></td><td>458.30 (+2.23%)</td><td>795.89 <b>(+816.50%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>9.36 (n/a)</td><td>8.07 (n/a)</td><td>7.85 (n/a)</td><td>6.37 (n/a)</td><td>1.26 (n/a)</td><td>658.60 (n/a)</td><td>530.28 (n/a)</td><td>534.50 (n/a)</td><td>448.30 (n/a)</td><td>86.84 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>9.87 (-4.46%)</td><td>7.17 <b>(+29.34%)</b></td><td>6.62 (-5.19%)</td><td>4.92 <b>(+348.37%)</b></td><td>1.88 <b>(-55.39%)</b></td><td>852.90 <b>(-77.70%)</b></td><td>617.84 <b>(-66.02%)</b></td><td>633.40 (+5.46%)</td><td>425.20 (+4.68%)</td><td>161.74 <b>(-91.01%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>10.33 (n/a)</td><td>5.55 (n/a)</td><td>6.98 (n/a)</td><td>1.10 (n/a)</td><td>4.22 (n/a)</td><td>3824.20 (n/a)</td><td>1818.38 (n/a)</td><td>600.60 (n/a)</td><td>406.20 (n/a)</td><td>1798.56 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>9.48 (-2.37%)</td><td>7.16 (-0.69%)</td><td>7.02 (-14.43%)</td><td>4.12 <b>(+246.95%)</b></td><td>1.98 <b>(-43.28%)</b></td><td>1019.00 <b>(-71.18%)</b></td><td>634.10 <b>(-42.18%)</b></td><td>597.40 (+16.86%)</td><td>442.50 (+2.43%)</td><td>224.85 <b>(-83.52%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>9.71 (n/a)</td><td>7.21 (n/a)</td><td>8.20 (n/a)</td><td>1.19 (n/a)</td><td>3.50 (n/a)</td><td>3535.40 (n/a)</td><td>1096.74 (n/a)</td><td>511.20 (n/a)</td><td>432.00 (n/a)</td><td>1364.33 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>1.88 (-4.37%)</td><td>1.21 <b>(+31.95%)</b></td><td>1.14 <b>(+45.77%)</b></td><td>0.72 <b>(+190.65%)</b></td><td>0.50 <b>(-21.49%)</b></td><td>730.60 <b>(-65.60%)</b></td><td>497.46 <b>(-43.74%)</b></td><td>459.00 <b>(-31.40%)</b></td><td>278.60 (+4.54%)</td><td>202.48 <b>(-71.93%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>1.97 (n/a)</td><td>0.92 (n/a)</td><td>0.78 (n/a)</td><td>0.25 (n/a)</td><td>0.64 (n/a)</td><td>2123.60 (n/a)</td><td>884.20 (n/a)</td><td>669.10 (n/a)</td><td>266.50 (n/a)</td><td>721.41 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>2.24 (-13.67%)</td><td>1.17 <b>(-38.68%)</b></td><td>1.50 <b>(-38.23%)</b></td><td>0.31 (-6.07%)</td><td>0.84 (-11.80%)</td><td>3407.10 (+6.47%)</td><td>1720.08 <b>(+69.68%)</b></td><td>699.70 <b>(+61.89%)</b></td><td>467.30 (+15.84%)</td><td>1507.99 <b>(+23.06%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>2.60 (n/a)</td><td>1.91 (n/a)</td><td>2.43 (n/a)</td><td>0.33 (n/a)</td><td>0.96 (n/a)</td><td>3200.20 (n/a)</td><td>1013.70 (n/a)</td><td>432.20 (n/a)</td><td>403.40 (n/a)</td><td>1225.38 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>3.75 (+1.26%)</td><td>2.21 (-17.56%)</td><td>2.39 <b>(-28.87%)</b></td><td>0.61 <b>(-35.98%)</b></td><td>1.34 (+15.04%)</td><td>3414.00 <b>(+56.19%)</b></td><td>1487.28 <b>(+47.17%)</b></td><td>878.10 <b>(+40.59%)</b></td><td>559.70 (-1.24%)</td><td>1206.78 <b>(+76.05%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>3.70 (n/a)</td><td>2.68 (n/a)</td><td>3.36 (n/a)</td><td>0.96 (n/a)</td><td>1.16 (n/a)</td><td>2185.80 (n/a)</td><td>1010.62 (n/a)</td><td>624.60 (n/a)</td><td>566.70 (n/a)</td><td>685.46 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>1.65 (-5.62%)</td><td>1.23 (+3.20%)</td><td>1.01 (-3.31%)</td><td>0.94 (+17.86%)</td><td>0.35 (-14.04%)</td><td>559.40 (-15.15%)</td><td>455.02 (-5.92%)</td><td>516.70 (+3.42%)</td><td>318.10 (+5.93%)</td><td>119.47 <b>(-23.25%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>1.75 (n/a)</td><td>1.19 (n/a)</td><td>1.05 (n/a)</td><td>0.80 (n/a)</td><td>0.41 (n/a)</td><td>659.30 (n/a)</td><td>483.64 (n/a)</td><td>499.60 (n/a)</td><td>300.30 (n/a)</td><td>155.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.13 (+5.23%)</td><td>0.08 (+0.01%)</td><td>0.07 (-4.27%)</td><td>0.05 (-7.18%)</td><td>0.03 (+10.83%)</td><td>663.60 (+7.74%)</td><td>453.34 (+1.64%)</td><td>447.30 (+4.46%)</td><td>243.90 (-4.99%)</td><td>150.21 (+9.90%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>615.90 (n/a)</td><td>446.04 (n/a)</td><td>428.20 (n/a)</td><td>256.70 (n/a)</td><td>136.68 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.14 (+0.31%)</td><td>0.11 (-5.16%)</td><td>0.11 (-7.85%)</td><td>0.07 (-6.83%)</td><td>0.03 (+8.15%)</td><td>460.30 (+7.32%)</td><td>311.78 (+6.53%)</td><td>296.70 (+8.52%)</td><td>229.20 (-0.30%)</td><td>90.71 (+14.01%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>428.90 (n/a)</td><td>292.66 (n/a)</td><td>273.40 (n/a)</td><td>229.90 (n/a)</td><td>79.56 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.28 (+5.58%)</td><td>0.22 (-2.80%)</td><td>0.22 (-11.64%)</td><td>0.15 (+19.91%)</td><td>0.05 (-15.51%)</td><td>429.80 (-16.59%)</td><td>305.32 (-0.68%)</td><td>292.10 (+13.17%)</td><td>233.50 (-5.31%)</td><td>76.90 <b>(-34.01%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>515.30 (n/a)</td><td>307.42 (n/a)</td><td>258.10 (n/a)</td><td>246.60 (n/a)</td><td>116.53 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.26 (-16.37%)</td><td>0.20 (+15.41%)</td><td>0.23 <b>(+77.74%)</b></td><td>0.11 (+1.53%)</td><td>0.07 <b>(-21.40%)</b></td><td>615.40 (-1.50%)</td><td>373.88 (-16.35%)</td><td>280.30 <b>(-43.74%)</b></td><td>248.20 (+19.56%)</td><td>156.84 (-5.55%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.32 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>624.80 (n/a)</td><td>446.96 (n/a)</td><td>498.20 (n/a)</td><td>207.60 (n/a)</td><td>166.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.22 <b>(-24.85%)</b></td><td>0.18 (-19.16%)</td><td>0.20 (+0.72%)</td><td>0.12 (-16.84%)</td><td>0.05 <b>(-23.77%)</b></td><td>561.90 <b>(+20.24%)</b></td><td>399.50 <b>(+23.45%)</b></td><td>332.50 (-0.72%)</td><td>292.30 <b>(+33.05%)</b></td><td>122.11 <b>(+25.07%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>467.30 (n/a)</td><td>323.60 (n/a)</td><td>334.90 (n/a)</td><td>219.70 (n/a)</td><td>97.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.51 (-5.40%)</td><td>0.39 (+1.54%)</td><td>0.42 (-5.64%)</td><td>0.26 <b>(+36.26%)</b></td><td>0.11 <b>(-28.05%)</b></td><td>506.20 <b>(-26.62%)</b></td><td>363.12 (-9.84%)</td><td>312.80 (+6.00%)</td><td>256.10 (+5.74%)</td><td>108.14 <b>(-43.29%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.54 (n/a)</td><td>0.38 (n/a)</td><td>0.44 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>689.80 (n/a)</td><td>402.76 (n/a)</td><td>295.10 (n/a)</td><td>242.20 (n/a)</td><td>190.69 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.55 <b>(+22.22%)</b></td><td>0.32 (+13.43%)</td><td>0.28 (+2.59%)</td><td>0.22 <b>(+90.20%)</b></td><td>0.13 (-10.79%)</td><td>593.30 <b>(-47.43%)</b></td><td>446.08 <b>(-24.66%)</b></td><td>475.00 (-2.52%)</td><td>240.20 (-18.19%)</td><td>133.30 <b>(-61.78%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.45 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>1128.50 (n/a)</td><td>592.12 (n/a)</td><td>487.30 (n/a)</td><td>293.60 (n/a)</td><td>348.76 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.54 (+1.32%)</td><td>0.33 <b>(-24.43%)</b></td><td>0.27 <b>(-41.70%)</b></td><td>0.21 (-0.88%)</td><td>0.13 (+0.01%)</td><td>628.20 (+0.88%)</td><td>445.10 <b>(+31.02%)</b></td><td>489.10 <b>(+71.55%)</b></td><td>243.90 (-1.33%)</td><td>148.82 (-6.75%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.46 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>622.70 (n/a)</td><td>339.72 (n/a)</td><td>285.10 (n/a)</td><td>247.20 (n/a)</td><td>159.60 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:17:43</td><td>0.07 (+0.94%)</td><td>0.05 (+13.99%)</td><td>0.06 <b>(+47.75%)</b></td><td>0.04 <b>(+29.93%)</b></td><td>0.01 (-17.31%)</td><td>449.80 <b>(-23.05%)</b></td><td>320.60 (-16.02%)</td><td>270.90 <b>(-32.31%)</b></td><td>243.50 (-0.94%)</td><td>90.55 <b>(-34.15%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:15:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>584.50 (n/a)</td><td>381.78 (n/a)</td><td>400.20 (n/a)</td><td>245.80 (n/a)</td><td>137.50 (n/a)</td>
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
