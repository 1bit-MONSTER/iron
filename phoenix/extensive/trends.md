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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-5.31%)</td><td>0.02 (-0.27%)</td><td>0.02 (+1.40%)</td><td>0.01 (-18.43%)</td><td>0.01 (+5.22%)</td><td>638.60 <b>(+22.60%)</b></td><td>371.20 (+3.27%)</td><td>296.70 (-1.40%)</td><td>279.40 (+5.63%)</td><td>151.85 <b>(+40.10%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.90 (n/a)</td><td>359.46 (n/a)</td><td>300.90 (n/a)</td><td>264.50 (n/a)</td><td>108.39 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-5.11%)</td><td>0.01 (+3.10%)</td><td>0.01 (-0.31%)</td><td>0.01 <b>(+276.54%)</b></td><td>0.00 <b>(-58.23%)</b></td><td>514.70 <b>(-73.44%)</b></td><td>436.84 <b>(-37.20%)</b></td><td>465.30 (+0.30%)</td><td>315.30 (+5.38%)</td><td>75.76 <b>(-89.17%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1937.90 (n/a)</td><td>695.60 (n/a)</td><td>463.90 (n/a)</td><td>299.20 (n/a)</td><td>699.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-13.09%)</td><td>0.02 (+13.20%)</td><td>0.02 (+17.84%)</td><td>0.01 <b>(+85.86%)</b></td><td>0.01 <b>(-25.69%)</b></td><td>596.90 <b>(-46.20%)</b></td><td>424.46 <b>(-23.24%)</b></td><td>400.90 (-15.14%)</td><td>271.60 (+15.08%)</td><td>146.50 <b>(-55.29%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1109.50 (n/a)</td><td>552.94 (n/a)</td><td>472.40 (n/a)</td><td>236.00 (n/a)</td><td>327.69 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (+6.25%)</td><td>0.02 (+3.94%)</td><td>0.01 (+2.23%)</td><td>0.01 (-6.72%)</td><td>0.01 (+9.04%)</td><td>658.30 (+7.20%)</td><td>424.12 (-1.98%)</td><td>456.30 (-2.19%)</td><td>224.90 (-5.86%)</td><td>178.92 (+6.45%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.10 (n/a)</td><td>432.68 (n/a)</td><td>466.50 (n/a)</td><td>238.90 (n/a)</td><td>168.07 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 <b>(+20.41%)</b></td><td>0.02 <b>(+23.01%)</b></td><td>0.01 (+11.16%)</td><td>0.01 <b>(+20.52%)</b></td><td>0.01 <b>(+32.26%)</b></td><td>533.80 (-17.02%)</td><td>399.46 (-17.41%)</td><td>430.40 (-10.03%)</td><td>244.20 (-16.94%)</td><td>131.90 (-10.75%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>643.30 (n/a)</td><td>483.68 (n/a)</td><td>478.40 (n/a)</td><td>294.00 (n/a)</td><td>147.78 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-0.48%)</td><td>0.02 (-4.99%)</td><td>0.02 (-18.50%)</td><td>0.01 (+10.78%)</td><td>0.01 (-17.27%)</td><td>565.00 (-9.73%)</td><td>394.36 (+0.21%)</td><td>344.40 <b>(+22.69%)</b></td><td>253.10 (+0.52%)</td><td>133.98 <b>(-22.49%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.90 (n/a)</td><td>393.52 (n/a)</td><td>280.70 (n/a)</td><td>251.80 (n/a)</td><td>172.86 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (-12.20%)</td><td>0.04 (-16.21%)</td><td>0.04 (-13.99%)</td><td>0.02 (-14.06%)</td><td>0.01 (-7.53%)</td><td>593.70 (+16.37%)</td><td>369.26 <b>(+20.79%)</b></td><td>280.30 (+16.26%)</td><td>249.80 (+13.91%)</td><td>148.19 <b>(+21.40%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.20 (n/a)</td><td>305.70 (n/a)</td><td>241.10 (n/a)</td><td>219.30 (n/a)</td><td>122.07 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (+1.73%)</td><td>0.04 (+3.47%)</td><td>0.05 (+0.17%)</td><td>0.03 (+7.51%)</td><td>0.01 (-3.23%)</td><td>441.00 (-6.98%)</td><td>321.14 (-4.76%)</td><td>265.90 (-0.15%)</td><td>229.80 (-1.71%)</td><td>107.61 (-12.45%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>474.10 (n/a)</td><td>337.20 (n/a)</td><td>266.30 (n/a)</td><td>233.80 (n/a)</td><td>122.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (+12.65%)</td><td>0.03 (+2.23%)</td><td>0.03 (+8.16%)</td><td>0.01 <b>(-74.37%)</b></td><td>0.02 <b>(+56.30%)</b></td><td>2392.40 <b>(+290.21%)</b></td><td>779.68 <b>(+72.85%)</b></td><td>429.20 (-7.56%)</td><td>207.30 (-11.22%)</td><td>912.72 <b>(+498.34%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>613.10 (n/a)</td><td>451.08 (n/a)</td><td>464.30 (n/a)</td><td>233.50 (n/a)</td><td>152.54 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (-10.00%)</td><td>0.03 <b>(-22.30%)</b></td><td>0.02 <b>(-37.27%)</b></td><td>0.02 <b>(-24.23%)</b></td><td>0.01 (+4.05%)</td><td>689.70 <b>(+31.97%)</b></td><td>467.14 <b>(+34.81%)</b></td><td>502.80 <b>(+59.42%)</b></td><td>269.90 (+11.07%)</td><td>179.33 <b>(+51.44%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.60 (n/a)</td><td>346.52 (n/a)</td><td>315.40 (n/a)</td><td>243.00 (n/a)</td><td>118.42 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (-5.88%)</td><td>0.03 (-15.57%)</td><td>0.02 (+0.82%)</td><td>0.01 <b>(-70.81%)</b></td><td>0.02 (+12.05%)</td><td>2055.90 <b>(+242.54%)</b></td><td>766.78 <b>(+66.12%)</b></td><td>564.80 (-0.81%)</td><td>277.80 (+6.23%)</td><td>734.68 <b>(+321.00%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.20 (n/a)</td><td>461.58 (n/a)</td><td>569.40 (n/a)</td><td>261.50 (n/a)</td><td>174.51 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (+4.63%)</td><td>0.02 <b>(-24.32%)</b></td><td>0.02 (-17.06%)</td><td>0.01 <b>(-75.43%)</b></td><td>0.02 <b>(+63.23%)</b></td><td>1929.70 <b>(+307.02%)</b></td><td>779.18 <b>(+95.80%)</b></td><td>551.30 <b>(+20.56%)</b></td><td>229.70 (-4.45%)</td><td>664.71 <b>(+568.08%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>474.10 (n/a)</td><td>397.94 (n/a)</td><td>457.30 (n/a)</td><td>240.40 (n/a)</td><td>99.50 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (-8.94%)</td><td>0.06 <b>(-25.82%)</b></td><td>0.05 <b>(-35.25%)</b></td><td>0.04 <b>(-42.64%)</b></td><td>0.02 <b>(+149.76%)</b></td><td>558.70 <b>(+74.38%)</b></td><td>422.54 <b>(+46.25%)</b></td><td>461.90 <b>(+54.48%)</b></td><td>274.40 (+9.80%)</td><td>132.73 <b>(+370.29%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>320.40 (n/a)</td><td>288.92 (n/a)</td><td>299.00 (n/a)</td><td>249.90 (n/a)</td><td>28.22 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 <b>(-30.73%)</b></td><td>0.05 <b>(-34.64%)</b></td><td>0.05 <b>(-47.94%)</b></td><td>0.04 (-14.46%)</td><td>0.01 <b>(-54.83%)</b></td><td>691.20 (+16.91%)</td><td>518.06 <b>(+40.82%)</b></td><td>527.10 <b>(+92.09%)</b></td><td>356.50 <b>(+44.39%)</b></td><td>122.38 <b>(-22.16%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>591.20 (n/a)</td><td>367.90 (n/a)</td><td>274.40 (n/a)</td><td>246.90 (n/a)</td><td>157.22 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (-11.34%)</td><td>0.06 (-12.45%)</td><td>0.06 <b>(-21.51%)</b></td><td>0.04 (+3.23%)</td><td>0.02 <b>(-29.92%)</b></td><td>592.30 (-3.12%)</td><td>418.34 (+8.28%)</td><td>405.10 <b>(+27.43%)</b></td><td>276.80 (+12.80%)</td><td>117.31 <b>(-24.03%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>611.40 (n/a)</td><td>386.34 (n/a)</td><td>317.90 (n/a)</td><td>245.40 (n/a)</td><td>154.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 <b>(-36.44%)</b></td><td>0.05 <b>(-30.34%)</b></td><td>0.05 <b>(-39.88%)</b></td><td>0.04 (+6.48%)</td><td>0.01 <b>(-68.41%)</b></td><td>566.50 (-6.07%)</td><td>496.34 <b>(+29.28%)</b></td><td>508.00 <b>(+66.34%)</b></td><td>383.40 <b>(+57.32%)</b></td><td>72.17 <b>(-54.19%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>603.10 (n/a)</td><td>383.94 (n/a)</td><td>305.40 (n/a)</td><td>243.70 (n/a)</td><td>157.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 <b>(-20.34%)</b></td><td>0.06 (-17.37%)</td><td>0.05 (+9.04%)</td><td>0.04 (-10.58%)</td><td>0.02 <b>(-34.63%)</b></td><td>690.40 (+11.82%)</td><td>499.06 (+11.52%)</td><td>518.90 (-8.29%)</td><td>267.90 <b>(+25.54%)</b></td><td>186.94 (-7.08%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>617.40 (n/a)</td><td>447.50 (n/a)</td><td>565.80 (n/a)</td><td>213.40 (n/a)</td><td>201.18 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 <b>(-26.34%)</b></td><td>0.06 <b>(-24.45%)</b></td><td>0.04 <b>(-40.68%)</b></td><td>0.04 (-2.11%)</td><td>0.02 <b>(-35.89%)</b></td><td>654.00 (+2.16%)</td><td>496.00 <b>(+22.78%)</b></td><td>564.70 <b>(+68.57%)</b></td><td>291.60 <b>(+35.75%)</b></td><td>165.87 (-13.50%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>640.20 (n/a)</td><td>403.96 (n/a)</td><td>335.00 (n/a)</td><td>214.80 (n/a)</td><td>191.76 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.20 (+9.06%)</td><td>0.13 <b>(-20.53%)</b></td><td>0.11 <b>(-36.19%)</b></td><td>0.09 <b>(-22.82%)</b></td><td>0.04 <b>(+84.54%)</b></td><td>528.50 <b>(+29.57%)</b></td><td>416.56 <b>(+32.98%)</b></td><td>468.00 <b>(+56.73%)</b></td><td>243.90 (-8.31%)</td><td>112.60 <b>(+105.30%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>407.90 (n/a)</td><td>313.24 (n/a)</td><td>298.60 (n/a)</td><td>266.00 (n/a)</td><td>54.85 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.20 (-0.51%)</td><td>0.18 <b>(+35.30%)</b></td><td>0.17 <b>(+70.28%)</b></td><td>0.16 <b>(+108.27%)</b></td><td>0.01 <b>(-74.70%)</b></td><td>307.00 <b>(-51.99%)</b></td><td>280.14 <b>(-36.22%)</b></td><td>286.50 <b>(-41.28%)</b></td><td>247.30 (+0.53%)</td><td>22.53 <b>(-87.27%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>639.40 (n/a)</td><td>439.26 (n/a)</td><td>487.90 (n/a)</td><td>246.00 (n/a)</td><td>176.95 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.16 <b>(-23.51%)</b></td><td>0.10 <b>(-25.58%)</b></td><td>0.09 (-8.78%)</td><td>0.05 <b>(-37.61%)</b></td><td>0.04 <b>(-32.73%)</b></td><td>1082.20 <b>(+60.28%)</b></td><td>598.30 <b>(+33.48%)</b></td><td>568.70 (+9.64%)</td><td>308.00 <b>(+30.73%)</b></td><td>299.14 <b>(+52.60%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>675.20 (n/a)</td><td>448.22 (n/a)</td><td>518.70 (n/a)</td><td>235.60 (n/a)</td><td>196.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.17 (-7.82%)</td><td>0.08 <b>(-25.58%)</b></td><td>0.09 <b>(-28.57%)</b></td><td>0.02 <b>(+22.26%)</b></td><td>0.06 (+1.33%)</td><td>1978.60 (-18.21%)</td><td>1048.10 <b>(+31.61%)</b></td><td>553.40 <b>(+39.99%)</b></td><td>292.70 (+8.49%)</td><td>835.67 (-8.29%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2419.10 (n/a)</td><td>796.34 (n/a)</td><td>395.30 (n/a)</td><td>269.80 (n/a)</td><td>911.17 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 <b>(-23.43%)</b></td><td>0.11 (-12.51%)</td><td>0.11 (-2.79%)</td><td>0.08 (+3.42%)</td><td>0.04 <b>(-35.82%)</b></td><td>594.70 (-3.32%)</td><td>470.90 (+8.32%)</td><td>466.30 (+2.87%)</td><td>274.40 <b>(+30.60%)</b></td><td>124.22 (-14.36%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>615.10 (n/a)</td><td>434.72 (n/a)</td><td>453.30 (n/a)</td><td>210.10 (n/a)</td><td>145.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 (+8.98%)</td><td>0.12 (+9.46%)</td><td>0.09 (+14.35%)</td><td>0.09 (+16.56%)</td><td>0.05 (-3.62%)</td><td>568.60 (-14.21%)</td><td>444.74 (-11.47%)</td><td>527.50 (-12.55%)</td><td>270.60 (-8.24%)</td><td>145.42 <b>(-21.74%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>662.80 (n/a)</td><td>502.34 (n/a)</td><td>603.20 (n/a)</td><td>294.90 (n/a)</td><td>185.83 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (+0.76%)</td><td>0.01 (-3.33%)</td><td>0.01 (-5.04%)</td><td>0.00 (+5.28%)</td><td>0.00 (-6.17%)</td><td>584.70 (-5.02%)</td><td>425.48 (+0.78%)</td><td>452.20 (+5.31%)</td><td>229.40 (-0.74%)</td><td>128.63 (-16.95%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>615.60 (n/a)</td><td>422.18 (n/a)</td><td>429.40 (n/a)</td><td>231.10 (n/a)</td><td>154.87 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (+9.26%)</td><td>0.01 (+19.63%)</td><td>0.01 <b>(+28.02%)</b></td><td>0.00 (-3.31%)</td><td>0.00 <b>(+29.73%)</b></td><td>621.10 (+3.43%)</td><td>369.98 (-12.10%)</td><td>328.40 <b>(-21.88%)</b></td><td>225.00 (-8.50%)</td><td>161.65 <b>(+24.58%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>600.50 (n/a)</td><td>420.92 (n/a)</td><td>420.40 (n/a)</td><td>245.90 (n/a)</td><td>129.75 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (+0.34%)</td><td>0.01 <b>(+24.48%)</b></td><td>0.01 <b>(+47.96%)</b></td><td>0.00 <b>(+345.46%)</b></td><td>0.00 <b>(-28.83%)</b></td><td>553.30 <b>(-77.55%)</b></td><td>386.30 <b>(-52.56%)</b></td><td>322.60 <b>(-32.41%)</b></td><td>239.80 (-0.37%)</td><td>143.67 <b>(-84.59%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2464.80 (n/a)</td><td>814.34 (n/a)</td><td>477.30 (n/a)</td><td>240.70 (n/a)</td><td>932.13 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (+13.19%)</td><td>0.01 (-4.96%)</td><td>0.01 (-3.71%)</td><td>0.00 <b>(-43.28%)</b></td><td>0.00 <b>(+39.41%)</b></td><td>1044.30 <b>(+76.31%)</b></td><td>422.14 <b>(+28.83%)</b></td><td>274.50 (+3.82%)</td><td>221.70 (-11.67%)</td><td>349.08 <b>(+135.49%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>592.30 (n/a)</td><td>327.68 (n/a)</td><td>264.40 (n/a)</td><td>251.00 (n/a)</td><td>148.24 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (+4.14%)</td><td>0.01 (+4.51%)</td><td>0.01 (+3.63%)</td><td>0.00 (+7.74%)</td><td>0.00 (+8.83%)</td><td>612.50 (-7.18%)</td><td>458.70 (-3.43%)</td><td>488.00 (-3.50%)</td><td>267.20 (-3.99%)</td><td>148.28 (+0.66%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>659.90 (n/a)</td><td>474.98 (n/a)</td><td>505.70 (n/a)</td><td>278.30 (n/a)</td><td>147.31 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 <b>(+22.16%)</b></td><td>0.01 (+2.37%)</td><td>0.01 <b>(+21.69%)</b></td><td>0.00 (+10.90%)</td><td>0.00 (+2.86%)</td><td>682.70 (-9.84%)</td><td>485.56 (-5.46%)</td><td>493.90 (-17.82%)</td><td>245.30 (-18.12%)</td><td>157.15 <b>(-23.15%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>757.20 (n/a)</td><td>513.60 (n/a)</td><td>601.00 (n/a)</td><td>299.60 (n/a)</td><td>204.47 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-13.77%)</td><td>0.01 <b>(-23.48%)</b></td><td>0.01 <b>(-25.29%)</b></td><td>0.01 <b>(-24.61%)</b></td><td>0.00 (-8.34%)</td><td>633.50 <b>(+32.64%)</b></td><td>429.68 <b>(+32.38%)</b></td><td>407.90 <b>(+33.83%)</b></td><td>276.50 (+15.98%)</td><td>128.84 <b>(+38.55%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>477.60 (n/a)</td><td>324.58 (n/a)</td><td>304.80 (n/a)</td><td>238.40 (n/a)</td><td>92.99 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-1.08%)</td><td>0.02 (-1.99%)</td><td>0.02 (-9.43%)</td><td>0.01 (-15.10%)</td><td>0.00 (-11.29%)</td><td>596.90 (+17.78%)</td><td>356.08 (+1.50%)</td><td>294.30 (+10.43%)</td><td>245.00 (+1.07%)</td><td>140.25 (+9.25%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>506.80 (n/a)</td><td>350.82 (n/a)</td><td>266.50 (n/a)</td><td>242.40 (n/a)</td><td>128.37 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (+7.29%)</td><td>0.02 (+9.78%)</td><td>0.01 (-14.58%)</td><td>0.01 <b>(+206.28%)</b></td><td>0.01 (+2.90%)</td><td>661.70 <b>(-67.35%)</b></td><td>440.36 <b>(-35.82%)</b></td><td>463.50 (+17.08%)</td><td>216.00 (-6.82%)</td><td>215.26 <b>(-71.58%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2026.60 (n/a)</td><td>686.08 (n/a)</td><td>395.90 (n/a)</td><td>231.80 (n/a)</td><td>757.50 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 <b>(-49.98%)</b></td><td>0.01 <b>(-27.11%)</b></td><td>0.01 (+5.48%)</td><td>0.00 <b>(-50.85%)</b></td><td>0.00 <b>(-52.71%)</b></td><td>2021.80 <b>(+103.46%)</b></td><td>757.66 <b>(+47.24%)</b></td><td>475.30 (-5.19%)</td><td>336.30 <b>(+99.94%)</b></td><td>709.30 <b>(+135.97%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>993.70 (n/a)</td><td>514.56 (n/a)</td><td>501.30 (n/a)</td><td>168.20 (n/a)</td><td>300.59 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-8.99%)</td><td>0.01 (+8.13%)</td><td>0.01 (+13.90%)</td><td>0.01 (-0.42%)</td><td>0.00 (-6.40%)</td><td>584.80 (+0.43%)</td><td>429.14 (-7.35%)</td><td>440.10 (-12.19%)</td><td>278.50 (+9.91%)</td><td>136.24 (+8.80%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.30 (n/a)</td><td>463.16 (n/a)</td><td>501.20 (n/a)</td><td>253.40 (n/a)</td><td>125.22 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (+6.00%)</td><td>0.01 (-10.04%)</td><td>0.01 <b>(-20.38%)</b></td><td>0.01 (-6.49%)</td><td>0.00 <b>(+30.52%)</b></td><td>511.70 (+6.94%)</td><td>446.14 (+12.54%)</td><td>476.60 <b>(+25.59%)</b></td><td>310.30 (-5.68%)</td><td>78.97 <b>(+26.07%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.50 (n/a)</td><td>396.44 (n/a)</td><td>379.50 (n/a)</td><td>329.00 (n/a)</td><td>62.64 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (+16.83%)</td><td>0.04 <b>(+35.57%)</b></td><td>0.04 <b>(+51.06%)</b></td><td>0.02 <b>(+21.56%)</b></td><td>0.01 (+13.26%)</td><td>432.10 (-17.74%)</td><td>287.88 <b>(-27.01%)</b></td><td>280.60 <b>(-33.79%)</b></td><td>209.00 (-14.41%)</td><td>91.27 <b>(-22.73%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.30 (n/a)</td><td>394.40 (n/a)</td><td>423.80 (n/a)</td><td>244.20 (n/a)</td><td>118.11 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (+1.08%)</td><td>0.04 (-2.56%)</td><td>0.04 (-7.41%)</td><td>0.02 <b>(+21.14%)</b></td><td>0.01 <b>(-22.40%)</b></td><td>425.20 (-17.47%)</td><td>303.60 (-1.59%)</td><td>292.80 (+8.00%)</td><td>231.00 (-1.07%)</td><td>73.32 <b>(-37.39%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.20 (n/a)</td><td>308.50 (n/a)</td><td>271.10 (n/a)</td><td>233.50 (n/a)</td><td>117.11 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 <b>(+31.49%)</b></td><td>0.04 <b>(+37.52%)</b></td><td>0.04 <b>(+75.47%)</b></td><td>0.02 (+12.24%)</td><td>0.01 <b>(+91.95%)</b></td><td>496.30 (-10.90%)</td><td>323.76 <b>(-22.39%)</b></td><td>241.40 <b>(-43.00%)</b></td><td>221.00 <b>(-23.95%)</b></td><td>125.73 <b>(+30.71%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>557.00 (n/a)</td><td>417.16 (n/a)</td><td>423.50 (n/a)</td><td>290.60 (n/a)</td><td>96.19 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (-1.32%)</td><td>0.03 (-17.17%)</td><td>0.03 (-15.53%)</td><td>0.02 <b>(-21.82%)</b></td><td>0.01 (+2.81%)</td><td>624.10 <b>(+27.92%)</b></td><td>416.58 <b>(+23.75%)</b></td><td>389.70 (+18.38%)</td><td>245.00 (+1.32%)</td><td>140.50 <b>(+37.83%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.90 (n/a)</td><td>336.64 (n/a)</td><td>329.20 (n/a)</td><td>241.80 (n/a)</td><td>101.94 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (+8.03%)</td><td>0.02 (-16.97%)</td><td>0.02 <b>(-45.83%)</b></td><td>0.02 <b>(+322.72%)</b></td><td>0.01 <b>(-28.16%)</b></td><td>580.00 <b>(-76.34%)</b></td><td>485.50 <b>(-34.37%)</b></td><td>537.70 <b>(+84.65%)</b></td><td>237.90 (-7.43%)</td><td>140.80 <b>(-85.33%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2451.70 (n/a)</td><td>739.80 (n/a)</td><td>291.20 (n/a)</td><td>257.00 (n/a)</td><td>960.02 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 <b>(-26.48%)</b></td><td>0.02 <b>(-29.29%)</b></td><td>0.02 (-3.98%)</td><td>0.01 <b>(-72.26%)</b></td><td>0.01 (-10.46%)</td><td>1949.40 <b>(+260.40%)</b></td><td>750.34 <b>(+85.07%)</b></td><td>484.90 (+4.15%)</td><td>350.00 <b>(+36.03%)</b></td><td>673.16 <b>(+419.45%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.90 (n/a)</td><td>405.44 (n/a)</td><td>465.60 (n/a)</td><td>257.30 (n/a)</td><td>129.59 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (+18.27%)</td><td>0.06 (-15.34%)</td><td>0.05 <b>(-23.57%)</b></td><td>0.03 <b>(-45.75%)</b></td><td>0.03 <b>(+146.43%)</b></td><td>676.50 <b>(+84.33%)</b></td><td>403.30 <b>(+34.25%)</b></td><td>399.70 <b>(+30.83%)</b></td><td>206.80 (-15.45%)</td><td>172.95 <b>(+281.84%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>367.00 (n/a)</td><td>300.42 (n/a)</td><td>305.50 (n/a)</td><td>244.60 (n/a)</td><td>45.29 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 <b>(-23.16%)</b></td><td>0.05 <b>(-30.90%)</b></td><td>0.04 <b>(-47.53%)</b></td><td>0.04 (-9.26%)</td><td>0.01 <b>(-37.46%)</b></td><td>573.40 (+10.21%)</td><td>456.92 <b>(+38.13%)</b></td><td>488.70 <b>(+90.60%)</b></td><td>288.30 <b>(+30.16%)</b></td><td>111.16 (-12.92%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>520.30 (n/a)</td><td>330.80 (n/a)</td><td>256.40 (n/a)</td><td>221.50 (n/a)</td><td>127.65 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (-16.84%)</td><td>0.06 <b>(-27.81%)</b></td><td>0.04 <b>(-42.33%)</b></td><td>0.04 (-4.05%)</td><td>0.02 (-17.42%)</td><td>574.10 (+4.23%)</td><td>413.02 <b>(+35.51%)</b></td><td>470.30 <b>(+73.41%)</b></td><td>235.90 <b>(+20.23%)</b></td><td>139.04 (-2.56%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>550.80 (n/a)</td><td>304.80 (n/a)</td><td>271.20 (n/a)</td><td>196.20 (n/a)</td><td>142.69 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 <b>(-24.22%)</b></td><td>0.05 <b>(-29.56%)</b></td><td>0.05 (-5.02%)</td><td>0.02 <b>(-57.69%)</b></td><td>0.03 <b>(-20.76%)</b></td><td>1028.80 <b>(+136.40%)</b></td><td>525.08 <b>(+57.65%)</b></td><td>436.20 (+5.29%)</td><td>251.40 <b>(+31.97%)</b></td><td>315.55 <b>(+145.36%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>435.20 (n/a)</td><td>333.06 (n/a)</td><td>414.30 (n/a)</td><td>190.50 (n/a)</td><td>128.60 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 <b>(-27.29%)</b></td><td>0.06 (-10.02%)</td><td>0.05 (-5.19%)</td><td>0.04 <b>(+57.29%)</b></td><td>0.01 <b>(-55.35%)</b></td><td>495.10 <b>(-36.42%)</b></td><td>394.26 (-6.89%)</td><td>402.90 (+5.47%)</td><td>294.00 <b>(+37.51%)</b></td><td>92.96 <b>(-59.72%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>778.70 (n/a)</td><td>423.42 (n/a)</td><td>382.00 (n/a)</td><td>213.80 (n/a)</td><td>230.77 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (-0.97%)</td><td>0.04 (-18.25%)</td><td>0.04 (-11.44%)</td><td>0.01 <b>(-68.90%)</b></td><td>0.02 <b>(+90.00%)</b></td><td>1918.80 <b>(+221.51%)</b></td><td>809.14 <b>(+61.39%)</b></td><td>567.50 (+12.94%)</td><td>366.50 (+0.96%)</td><td>628.55 <b>(+625.73%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>596.80 (n/a)</td><td>501.36 (n/a)</td><td>502.50 (n/a)</td><td>363.00 (n/a)</td><td>86.61 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>528.50 (n/a)</td><td>335.20 (n/a)</td><td>292.90 (n/a)</td><td>233.00 (n/a)</td><td>113.43 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.10 (n/a)</td><td>402.22 (n/a)</td><td>320.40 (n/a)</td><td>226.10 (n/a)</td><td>163.26 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.10 (n/a)</td><td>354.70 (n/a)</td><td>293.80 (n/a)</td><td>251.90 (n/a)</td><td>141.78 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.30 (n/a)</td><td>361.86 (n/a)</td><td>321.70 (n/a)</td><td>240.10 (n/a)</td><td>126.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>778.20 (n/a)</td><td>342.84 (n/a)</td><td>239.60 (n/a)</td><td>192.70 (n/a)</td><td>244.86 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>364.40 (n/a)</td><td>302.42 (n/a)</td><td>305.70 (n/a)</td><td>252.90 (n/a)</td><td>43.83 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>985.10 (n/a)</td><td>533.32 (n/a)</td><td>408.80 (n/a)</td><td>291.80 (n/a)</td><td>288.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>501.90 (n/a)</td><td>359.94 (n/a)</td><td>293.30 (n/a)</td><td>249.70 (n/a)</td><td>121.10 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>528.90 (n/a)</td><td>450.92 (n/a)</td><td>468.60 (n/a)</td><td>348.50 (n/a)</td><td>71.92 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.16 <b>(-23.17%)</b></td><td>0.13 (-10.60%)</td><td>0.11 (-13.21%)</td><td>0.09 (+14.86%)</td><td>0.03 <b>(-35.01%)</b></td><td>518.00 (-12.93%)</td><td>407.42 (+5.85%)</td><td>437.10 (+15.24%)</td><td>299.70 <b>(+30.19%)</b></td><td>101.63 <b>(-28.77%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>594.90 (n/a)</td><td>384.92 (n/a)</td><td>379.30 (n/a)</td><td>230.20 (n/a)</td><td>142.68 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>599.50 (n/a)</td><td>438.84 (n/a)</td><td>516.80 (n/a)</td><td>262.50 (n/a)</td><td>150.61 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>416.00 (n/a)</td><td>304.88 (n/a)</td><td>277.70 (n/a)</td><td>218.70 (n/a)</td><td>75.84 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>352.00 (n/a)</td><td>292.52 (n/a)</td><td>266.70 (n/a)</td><td>242.80 (n/a)</td><td>54.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>270.20 (n/a)</td><td>251.88 (n/a)</td><td>244.50 (n/a)</td><td>237.80 (n/a)</td><td>16.36 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>696.10 (n/a)</td><td>444.42 (n/a)</td><td>486.40 (n/a)</td><td>211.20 (n/a)</td><td>190.36 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.80 (n/a)</td><td>323.36 (n/a)</td><td>292.70 (n/a)</td><td>227.60 (n/a)</td><td>116.84 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>559.90 (n/a)</td><td>408.56 (n/a)</td><td>475.20 (n/a)</td><td>239.60 (n/a)</td><td>156.59 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.10 (n/a)</td><td>406.78 (n/a)</td><td>441.10 (n/a)</td><td>296.70 (n/a)</td><td>102.49 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>338.90 (n/a)</td><td>295.44 (n/a)</td><td>291.00 (n/a)</td><td>251.70 (n/a)</td><td>31.60 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>662.10 (n/a)</td><td>429.22 (n/a)</td><td>365.90 (n/a)</td><td>242.20 (n/a)</td><td>164.01 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>553.70 (n/a)</td><td>338.98 (n/a)</td><td>287.10 (n/a)</td><td>251.60 (n/a)</td><td>122.73 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>303.50 (n/a)</td><td>266.76 (n/a)</td><td>255.30 (n/a)</td><td>235.60 (n/a)</td><td>27.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>625.40 (n/a)</td><td>399.22 (n/a)</td><td>431.80 (n/a)</td><td>247.60 (n/a)</td><td>157.73 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>468.40 (n/a)</td><td>330.94 (n/a)</td><td>274.50 (n/a)</td><td>184.80 (n/a)</td><td>128.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>654.30 (n/a)</td><td>444.36 (n/a)</td><td>441.50 (n/a)</td><td>271.20 (n/a)</td><td>137.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>501.20 (n/a)</td><td>341.04 (n/a)</td><td>282.60 (n/a)</td><td>229.90 (n/a)</td><td>119.93 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>651.40 (n/a)</td><td>466.32 (n/a)</td><td>429.60 (n/a)</td><td>271.20 (n/a)</td><td>145.00 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.70 (n/a)</td><td>438.54 (n/a)</td><td>437.30 (n/a)</td><td>267.40 (n/a)</td><td>127.99 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.60 (n/a)</td><td>419.52 (n/a)</td><td>483.90 (n/a)</td><td>269.60 (n/a)</td><td>107.96 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.80 (n/a)</td><td>356.24 (n/a)</td><td>275.30 (n/a)</td><td>249.40 (n/a)</td><td>162.92 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.20 (n/a)</td><td>374.04 (n/a)</td><td>387.50 (n/a)</td><td>247.50 (n/a)</td><td>99.54 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.80 (n/a)</td><td>361.72 (n/a)</td><td>280.20 (n/a)</td><td>240.50 (n/a)</td><td>154.45 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>409.20 (n/a)</td><td>270.84 (n/a)</td><td>247.70 (n/a)</td><td>205.10 (n/a)</td><td>79.45 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>804.60 (n/a)</td><td>469.54 (n/a)</td><td>316.90 (n/a)</td><td>217.00 (n/a)</td><td>290.44 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1917.30 (n/a)</td><td>727.70 (n/a)</td><td>433.70 (n/a)</td><td>307.50 (n/a)</td><td>672.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>539.00 (n/a)</td><td>342.40 (n/a)</td><td>302.40 (n/a)</td><td>259.20 (n/a)</td><td>114.30 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2508.80 (n/a)</td><td>833.58 (n/a)</td><td>417.60 (n/a)</td><td>255.60 (n/a)</td><td>946.32 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>655.80 (n/a)</td><td>466.62 (n/a)</td><td>472.30 (n/a)</td><td>279.40 (n/a)</td><td>136.58 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>608.00 (n/a)</td><td>353.50 (n/a)</td><td>294.10 (n/a)</td><td>224.00 (n/a)</td><td>157.41 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1083.50 (n/a)</td><td>715.30 (n/a)</td><td>510.40 (n/a)</td><td>440.90 (n/a)</td><td>315.83 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>557.80 (n/a)</td><td>444.50 (n/a)</td><td>500.50 (n/a)</td><td>290.00 (n/a)</td><td>111.84 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1096.30 (n/a)</td><td>634.68 (n/a)</td><td>528.40 (n/a)</td><td>453.20 (n/a)</td><td>263.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2426.70 (n/a)</td><td>792.14 (n/a)</td><td>429.00 (n/a)</td><td>299.40 (n/a)</td><td>916.88 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1840.60 (n/a)</td><td>730.82 (n/a)</td><td>562.80 (n/a)</td><td>213.00 (n/a)</td><td>640.81 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>569.20 (n/a)</td><td>421.52 (n/a)</td><td>445.20 (n/a)</td><td>269.40 (n/a)</td><td>144.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>574.20 (n/a)</td><td>462.88 (n/a)</td><td>481.40 (n/a)</td><td>337.00 (n/a)</td><td>104.80 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.40 <b>(-20.83%)</b></td><td>0.31 (-17.96%)</td><td>0.35 <b>(-22.05%)</b></td><td>0.12 <b>(-49.94%)</b></td><td>0.11 (-12.02%)</td><td>1874.20 <b>(+99.74%)</b></td><td>867.88 <b>(+34.35%)</b></td><td>637.10 <b>(+28.29%)</b></td><td>552.80 <b>(+26.33%)</b></td><td>565.10 <b>(+130.29%)</b></td><td>17.07 <b>(-20.83%)</b></td><td>13.35 (-17.96%)</td><td>14.81 <b>(-22.05%)</b></td><td>5.04 <b>(-49.94%)</b></td><td>4.83 (-12.02%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.51 (n/a)</td><td>0.38 (n/a)</td><td>0.45 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>938.30 (n/a)</td><td>645.98 (n/a)</td><td>496.60 (n/a)</td><td>437.60 (n/a)</td><td>245.39 (n/a)</td><td>21.56 (n/a)</td><td>16.27 (n/a)</td><td>19.00 (n/a)</td><td>10.06 (n/a)</td><td>5.49 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.56 (+4.25%)</td><td>0.45 (-2.30%)</td><td>0.42 (-4.64%)</td><td>0.34 (-10.97%)</td><td>0.09 <b>(+34.33%)</b></td><td>652.60 (+12.32%)</td><td>512.04 (+3.82%)</td><td>526.80 (+4.86%)</td><td>394.20 (-4.09%)</td><td>99.06 <b>(+44.88%)</b></td><td>23.94 (+4.25%)</td><td>18.99 (-2.30%)</td><td>17.91 (-4.64%)</td><td>14.46 (-10.97%)</td><td>3.66 <b>(+34.33%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.54 (n/a)</td><td>0.46 (n/a)</td><td>0.44 (n/a)</td><td>0.38 (n/a)</td><td>0.06 (n/a)</td><td>581.00 (n/a)</td><td>493.22 (n/a)</td><td>502.40 (n/a)</td><td>411.00 (n/a)</td><td>68.37 (n/a)</td><td>22.96 (n/a)</td><td>19.44 (n/a)</td><td>18.78 (n/a)</td><td>16.24 (n/a)</td><td>2.72 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.31 (+0.49%)</td><td>0.31 (+1.90%)</td><td>0.31 (+2.31%)</td><td>0.30 (+2.11%)</td><td>0.00 <b>(-32.16%)</b></td><td>83028.50 (-2.07%)</td><td>81508.32 (-1.88%)</td><td>81053.40 (-2.26%)</td><td>80455.60 (-0.48%)</td><td>1031.61 <b>(-33.89%)</b></td><td>213.53 (+0.49%)</td><td>210.80 (+1.90%)</td><td>211.96 (+2.31%)</td><td>206.92 (+2.11%)</td><td>2.65 <b>(-32.16%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84780.80 (n/a)</td><td>83072.92 (n/a)</td><td>82923.40 (n/a)</td><td>80846.70 (n/a)</td><td>1560.47 (n/a)</td><td>212.50 (n/a)</td><td>206.86 (n/a)</td><td>207.18 (n/a)</td><td>202.64 (n/a)</td><td>3.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>1.03 (-1.74%)</td><td>1.01 (-0.44%)</td><td>1.02 (-0.19%)</td><td>1.00 (+0.47%)</td><td>0.01 <b>(-47.77%)</b></td><td>25115.90 (-0.47%)</td><td>24799.58 (+0.42%)</td><td>24733.60 (+0.19%)</td><td>24542.80 (+1.77%)</td><td>226.24 <b>(-47.06%)</b></td><td>700.00 (-1.74%)</td><td>692.79 (-0.44%)</td><td>694.60 (-0.19%)</td><td>684.02 (+0.47%)</td><td>6.30 <b>(-47.77%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>1.04 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>0.02 (n/a)</td><td>25233.40 (n/a)</td><td>24695.12 (n/a)</td><td>24686.20 (n/a)</td><td>24115.30 (n/a)</td><td>427.39 (n/a)</td><td>712.41 (n/a)</td><td>695.85 (n/a)</td><td>695.93 (n/a)</td><td>680.84 (n/a)</td><td>12.07 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.82 (+0.83%)</td><td>0.81 (-0.66%)</td><td>0.80 (-0.92%)</td><td>0.79 (-1.69%)</td><td>0.01 <b>(+129.93%)</b></td><td>95601.40 (+1.72%)</td><td>93622.86 (+0.68%)</td><td>93786.30 (+0.93%)</td><td>91722.80 (-0.82%)</td><td>1406.83 <b>(+131.95%)</b></td><td>749.21 (+0.83%)</td><td>734.14 (-0.66%)</td><td>732.72 (-0.92%)</td><td>718.81 (-1.69%)</td><td>11.02 <b>(+129.93%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>93982.30 (n/a)</td><td>92989.42 (n/a)</td><td>92921.10 (n/a)</td><td>92485.80 (n/a)</td><td>606.53 (n/a)</td><td>743.03 (n/a)</td><td>739.03 (n/a)</td><td>739.55 (n/a)</td><td>731.20 (n/a)</td><td>4.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.77 (-0.26%)</td><td>0.76 (+0.25%)</td><td>0.76 (-0.11%)</td><td>0.75 (+0.98%)</td><td>0.01 <b>(-41.73%)</b></td><td>100062.50 (-0.97%)</td><td>98828.46 (-0.27%)</td><td>98957.70 (+0.11%)</td><td>97670.10 (+0.26%)</td><td>942.27 <b>(-42.15%)</b></td><td>703.59 (-0.26%)</td><td>695.39 (+0.25%)</td><td>694.43 (-0.11%)</td><td>686.77 (+0.98%)</td><td>6.63 <b>(-41.73%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101047.10 (n/a)</td><td>99094.16 (n/a)</td><td>98846.30 (n/a)</td><td>97413.30 (n/a)</td><td>1628.91 (n/a)</td><td>705.44 (n/a)</td><td>693.63 (n/a)</td><td>695.22 (n/a)</td><td>680.07 (n/a)</td><td>11.38 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.80 (+0.26%)</td><td>0.79 (+0.10%)</td><td>0.79 (-0.19%)</td><td>0.78 (+0.81%)</td><td>0.01 <b>(-24.89%)</b></td><td>96881.50 (-0.80%)</td><td>95348.24 (-0.11%)</td><td>95188.00 (+0.19%)</td><td>94201.20 (-0.26%)</td><td>965.21 <b>(-25.67%)</b></td><td>729.50 (+0.26%)</td><td>720.78 (+0.10%)</td><td>721.93 (-0.19%)</td><td>709.31 (+0.81%)</td><td>7.25 <b>(-24.89%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>97662.20 (n/a)</td><td>95450.42 (n/a)</td><td>95003.90 (n/a)</td><td>94446.60 (n/a)</td><td>1298.60 (n/a)</td><td>727.60 (n/a)</td><td>720.05 (n/a)</td><td>723.33 (n/a)</td><td>703.64 (n/a)</td><td>9.66 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>5.20 (-6.73%)</td><td>3.92 (-0.56%)</td><td>4.05 (-4.05%)</td><td>2.16 (-15.67%)</td><td>1.16 (-0.28%)</td><td>4129.80 (+18.58%)</td><td>2497.36 (+2.60%)</td><td>2201.50 (+4.22%)</td><td>1713.60 (+7.22%)</td><td>960.98 <b>(+29.72%)</b></td><td>313.29 (-6.73%)</td><td>235.87 (-0.56%)</td><td>243.87 (-4.05%)</td><td>130.00 (-15.67%)</td><td>70.03 (-0.28%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.58 (n/a)</td><td>3.94 (n/a)</td><td>4.22 (n/a)</td><td>2.56 (n/a)</td><td>1.17 (n/a)</td><td>3482.60 (n/a)</td><td>2433.96 (n/a)</td><td>2112.30 (n/a)</td><td>1598.20 (n/a)</td><td>740.81 (n/a)</td><td>335.92 (n/a)</td><td>237.20 (n/a)</td><td>254.17 (n/a)</td><td>154.16 (n/a)</td><td>70.23 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>4.97 <b>(+125.57%)</b></td><td>3.33 <b>(+54.44%)</b></td><td>2.71 <b>(+24.88%)</b></td><td>2.18 (+5.33%)</td><td>1.31 <b>(+2368.19%)</b></td><td>4086.10 (-5.06%)</td><td>3010.20 <b>(-27.19%)</b></td><td>3283.50 (-19.92%)</td><td>1793.70 <b>(-55.67%)</b></td><td>1071.82 <b>(+930.72%)</b></td><td>299.31 <b>(+125.57%)</b></td><td>200.63 <b>(+54.44%)</b></td><td>163.50 <b>(+24.88%)</b></td><td>131.39 (+5.33%)</td><td>79.03 <b>(+2368.19%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>2.20 (n/a)</td><td>2.16 (n/a)</td><td>2.17 (n/a)</td><td>2.07 (n/a)</td><td>0.05 (n/a)</td><td>4303.70 (n/a)</td><td>4134.60 (n/a)</td><td>4100.50 (n/a)</td><td>4046.00 (n/a)</td><td>103.99 (n/a)</td><td>132.69 (n/a)</td><td>129.91 (n/a)</td><td>130.93 (n/a)</td><td>124.75 (n/a)</td><td>3.20 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>5.24 (-5.86%)</td><td>3.72 (+8.59%)</td><td>3.56 <b>(+30.63%)</b></td><td>2.19 (+0.46%)</td><td>1.10 <b>(-22.68%)</b></td><td>4071.70 (-0.46%)</td><td>2598.30 (-11.63%)</td><td>2500.50 <b>(-23.45%)</b></td><td>1702.00 (+6.23%)</td><td>888.41 (-14.47%)</td><td>315.44 (-5.86%)</td><td>223.93 (+8.59%)</td><td>214.71 <b>(+30.63%)</b></td><td>131.85 (+0.46%)</td><td>66.21 <b>(-22.68%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.56 (n/a)</td><td>3.42 (n/a)</td><td>2.73 (n/a)</td><td>2.18 (n/a)</td><td>1.42 (n/a)</td><td>4090.60 (n/a)</td><td>2940.28 (n/a)</td><td>3266.30 (n/a)</td><td>1602.20 (n/a)</td><td>1038.75 (n/a)</td><td>335.07 (n/a)</td><td>206.21 (n/a)</td><td>164.37 (n/a)</td><td>131.25 (n/a)</td><td>85.63 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>5.82 (-10.04%)</td><td>5.23 (-8.73%)</td><td>5.39 (-11.50%)</td><td>4.26 (-11.74%)</td><td>0.65 (-15.15%)</td><td>8182.80 (+13.30%)</td><td>6758.10 (+9.39%)</td><td>6468.60 (+12.99%)</td><td>5995.50 (+11.17%)</td><td>909.86 (+5.37%)</td><td>358.18 (-10.04%)</td><td>322.06 (-8.73%)</td><td>331.99 (-11.50%)</td><td>262.44 (-11.74%)</td><td>40.06 (-15.15%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>6.46 (n/a)</td><td>5.73 (n/a)</td><td>6.09 (n/a)</td><td>4.83 (n/a)</td><td>0.77 (n/a)</td><td>7222.10 (n/a)</td><td>6177.86 (n/a)</td><td>5724.90 (n/a)</td><td>5393.30 (n/a)</td><td>863.46 (n/a)</td><td>398.18 (n/a)</td><td>352.88 (n/a)</td><td>375.11 (n/a)</td><td>297.35 (n/a)</td><td>47.22 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>6.11 (+6.96%)</td><td>4.95 (+2.84%)</td><td>4.52 (-6.86%)</td><td>4.14 (+7.46%)</td><td>0.83 (-4.24%)</td><td>8418.50 (-6.94%)</td><td>7200.38 (-3.29%)</td><td>7720.20 (+7.37%)</td><td>5705.40 (-6.51%)</td><td>1134.23 (-16.94%)</td><td>376.40 (+6.96%)</td><td>304.66 (+2.84%)</td><td>278.17 (-6.86%)</td><td>255.09 (+7.46%)</td><td>51.07 (-4.24%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.71 (n/a)</td><td>4.81 (n/a)</td><td>4.85 (n/a)</td><td>3.85 (n/a)</td><td>0.87 (n/a)</td><td>9046.30 (n/a)</td><td>7445.04 (n/a)</td><td>7190.60 (n/a)</td><td>6102.50 (n/a)</td><td>1365.60 (n/a)</td><td>351.90 (n/a)</td><td>296.24 (n/a)</td><td>298.65 (n/a)</td><td>237.39 (n/a)</td><td>53.33 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>6.75 (+2.04%)</td><td>5.94 (+9.49%)</td><td>6.07 (+15.98%)</td><td>4.81 (+8.76%)</td><td>0.70 <b>(-27.50%)</b></td><td>7247.60 (-8.05%)</td><td>5947.00 (-9.85%)</td><td>5744.20 (-13.78%)</td><td>5163.70 (-2.00%)</td><td>777.20 <b>(-32.93%)</b></td><td>415.88 (+2.04%)</td><td>365.62 (+9.49%)</td><td>373.85 (+15.98%)</td><td>296.30 (+8.76%)</td><td>43.42 <b>(-27.50%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>6.62 (n/a)</td><td>5.42 (n/a)</td><td>5.23 (n/a)</td><td>4.42 (n/a)</td><td>0.97 (n/a)</td><td>7882.20 (n/a)</td><td>6596.72 (n/a)</td><td>6662.00 (n/a)</td><td>5269.00 (n/a)</td><td>1158.85 (n/a)</td><td>407.57 (n/a)</td><td>333.92 (n/a)</td><td>322.35 (n/a)</td><td>272.45 (n/a)</td><td>59.89 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.77 (-2.62%)</td><td>0.75 (-2.64%)</td><td>0.74 (-2.39%)</td><td>0.73 (-2.49%)</td><td>0.02 (-8.74%)</td><td>103914.60 (+2.55%)</td><td>101343.92 (+2.70%)</td><td>101522.90 (+2.44%)</td><td>98193.80 (+2.69%)</td><td>2514.48 (-3.73%)</td><td>699.84 (-2.62%)</td><td>678.42 (-2.64%)</td><td>676.89 (-2.39%)</td><td>661.31 (-2.49%)</td><td>16.90 (-8.74%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.02 (n/a)</td><td>101332.10 (n/a)</td><td>98679.12 (n/a)</td><td>99100.40 (n/a)</td><td>95625.70 (n/a)</td><td>2611.78 (n/a)</td><td>718.63 (n/a)</td><td>696.79 (n/a)</td><td>693.43 (n/a)</td><td>678.16 (n/a)</td><td>18.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.77 (+0.36%)</td><td>0.76 (+0.89%)</td><td>0.76 (+0.56%)</td><td>0.74 (+2.02%)</td><td>0.01 <b>(-26.92%)</b></td><td>101784.30 (-1.98%)</td><td>99262.74 (-0.90%)</td><td>99096.70 (-0.55%)</td><td>97623.20 (-0.36%)</td><td>1553.56 <b>(-28.80%)</b></td><td>703.93 (+0.36%)</td><td>692.43 (+0.89%)</td><td>693.46 (+0.56%)</td><td>675.15 (+2.02%)</td><td>10.71 <b>(-26.92%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103835.30 (n/a)</td><td>100160.68 (n/a)</td><td>99649.70 (n/a)</td><td>97974.00 (n/a)</td><td>2182.07 (n/a)</td><td>701.41 (n/a)</td><td>686.35 (n/a)</td><td>689.61 (n/a)</td><td>661.81 (n/a)</td><td>14.66 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.81 (-0.29%)</td><td>0.79 (-1.16%)</td><td>0.79 (-1.79%)</td><td>0.78 (-1.39%)</td><td>0.01 <b>(+41.10%)</b></td><td>97156.90 (+1.41%)</td><td>95554.02 (+1.18%)</td><td>95892.30 (+1.83%)</td><td>93709.20 (+0.29%)</td><td>1282.46 <b>(+43.22%)</b></td><td>733.33 (-0.29%)</td><td>719.27 (-1.16%)</td><td>716.63 (-1.79%)</td><td>707.30 (-1.39%)</td><td>9.69 <b>(+41.10%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95801.60 (n/a)</td><td>94439.06 (n/a)</td><td>94172.20 (n/a)</td><td>93437.20 (n/a)</td><td>895.46 (n/a)</td><td>735.46 (n/a)</td><td>727.71 (n/a)</td><td>729.72 (n/a)</td><td>717.31 (n/a)</td><td>6.87 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.43 (+2.11%)</td><td>2.83 <b>(+45.71%)</b></td><td>2.99 <b>(+73.49%)</b></td><td>1.89 <b>(+73.24%)</b></td><td>0.59 <b>(-32.02%)</b></td><td>4263.50 <b>(-42.28%)</b></td><td>2968.16 <b>(-37.48%)</b></td><td>2691.70 <b>(-42.36%)</b></td><td>2347.40 (-2.07%)</td><td>757.09 <b>(-58.61%)</b></td><td>900.54 (+2.11%)</td><td>743.18 <b>(+45.71%)</b></td><td>785.36 <b>(+73.49%)</b></td><td>495.82 <b>(+73.24%)</b></td><td>153.73 <b>(-32.02%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.36 (n/a)</td><td>1.94 (n/a)</td><td>1.73 (n/a)</td><td>1.09 (n/a)</td><td>0.86 (n/a)</td><td>7385.90 (n/a)</td><td>4747.84 (n/a)</td><td>4669.80 (n/a)</td><td>2396.90 (n/a)</td><td>1829.34 (n/a)</td><td>881.95 (n/a)</td><td>510.03 (n/a)</td><td>452.68 (n/a)</td><td>286.21 (n/a)</td><td>226.14 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.29 <b>(+28.38%)</b></td><td>0.22 (+5.85%)</td><td>0.19 (-8.76%)</td><td>0.19 (+4.74%)</td><td>0.04 <b>(+119.85%)</b></td><td>6514.80 (-4.52%)</td><td>5881.10 (-3.81%)</td><td>6409.90 (+9.60%)</td><td>4292.40 <b>(-22.10%)</b></td><td>943.86 <b>(+61.25%)</b></td><td>15.63 <b>(+28.38%)</b></td><td>11.70 (+5.85%)</td><td>10.47 (-8.76%)</td><td>10.30 (+4.74%)</td><td>2.27 <b>(+119.85%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>6823.40 (n/a)</td><td>6114.16 (n/a)</td><td>5848.40 (n/a)</td><td>5510.40 (n/a)</td><td>585.35 (n/a)</td><td>12.18 (n/a)</td><td>11.06 (n/a)</td><td>11.47 (n/a)</td><td>9.84 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (+0.48%)</td><td>0.10 (-0.68%)</td><td>0.10 (-7.24%)</td><td>0.07 (+9.68%)</td><td>0.03 (+11.13%)</td><td>0.13 (+0.48%)</td><td>0.10 (-0.68%)</td><td>0.10 (-7.24%)</td><td>0.07 (+9.68%)</td><td>0.03 (+11.13%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.64 (-7.47%)</td><td>3.56 (-3.38%)</td><td>3.60 (-1.01%)</td><td>3.45 (-1.94%)</td><td>0.08 <b>(-49.02%)</b></td><td>3.64 (-7.47%)</td><td>3.56 (-3.38%)</td><td>3.60 (-1.01%)</td><td>3.44 (-1.94%)</td><td>0.08 <b>(-49.02%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.94 (n/a)</td><td>3.69 (n/a)</td><td>3.64 (n/a)</td><td>3.51 (n/a)</td><td>0.16 (n/a)</td><td>3.93 (n/a)</td><td>3.69 (n/a)</td><td>3.64 (n/a)</td><td>3.51 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>7.61 (+5.50%)</td><td>6.47 (+5.07%)</td><td>6.97 (+19.28%)</td><td>4.94 (-11.48%)</td><td>1.15 <b>(+71.63%)</b></td><td>7.60 (+5.50%)</td><td>6.47 (+5.07%)</td><td>6.97 (+19.28%)</td><td>4.93 (-11.48%)</td><td>1.15 <b>(+71.63%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>7.21 (n/a)</td><td>6.16 (n/a)</td><td>5.85 (n/a)</td><td>5.58 (n/a)</td><td>0.67 (n/a)</td><td>7.20 (n/a)</td><td>6.15 (n/a)</td><td>5.84 (n/a)</td><td>5.57 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>13.97 (+0.18%)</td><td>10.82 <b>(+23.18%)</b></td><td>9.72 (+15.33%)</td><td>8.24 <b>(+50.16%)</b></td><td>2.47 <b>(-20.97%)</b></td><td>13.96 (+0.18%)</td><td>10.81 <b>(+23.18%)</b></td><td>9.71 (+15.33%)</td><td>8.24 <b>(+50.16%)</b></td><td>2.47 <b>(-20.97%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>13.95 (n/a)</td><td>8.78 (n/a)</td><td>8.43 (n/a)</td><td>5.49 (n/a)</td><td>3.13 (n/a)</td><td>13.94 (n/a)</td><td>8.78 (n/a)</td><td>8.42 (n/a)</td><td>5.48 (n/a)</td><td>3.13 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.74 (-3.10%)</td><td>3.58 (+1.86%)</td><td>3.63 (+4.99%)</td><td>3.34 (+8.08%)</td><td>0.16 <b>(-47.23%)</b></td><td>3.74 (-3.10%)</td><td>3.58 (+1.86%)</td><td>3.63 (+4.99%)</td><td>3.34 (+8.08%)</td><td>0.16 <b>(-47.23%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.86 (n/a)</td><td>3.52 (n/a)</td><td>3.46 (n/a)</td><td>3.09 (n/a)</td><td>0.30 (n/a)</td><td>3.86 (n/a)</td><td>3.51 (n/a)</td><td>3.46 (n/a)</td><td>3.09 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>7.35 (+7.95%)</td><td>6.12 (-2.31%)</td><td>6.08 (-10.17%)</td><td>4.72 (-3.07%)</td><td>1.05 <b>(+25.17%)</b></td><td>7.35 (+7.95%)</td><td>6.12 (-2.31%)</td><td>6.07 (-10.17%)</td><td>4.72 (-3.07%)</td><td>1.05 <b>(+25.17%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>6.81 (n/a)</td><td>6.27 (n/a)</td><td>6.76 (n/a)</td><td>4.87 (n/a)</td><td>0.84 (n/a)</td><td>6.81 (n/a)</td><td>6.27 (n/a)</td><td>6.76 (n/a)</td><td>4.87 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>13.91 (-0.24%)</td><td>10.21 (+2.51%)</td><td>9.72 (+14.68%)</td><td>7.97 (+2.22%)</td><td>2.21 (-16.32%)</td><td>13.91 (-0.24%)</td><td>10.20 (+2.51%)</td><td>9.71 (+14.68%)</td><td>7.97 (+2.22%)</td><td>2.20 (-16.32%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>13.95 (n/a)</td><td>9.96 (n/a)</td><td>8.47 (n/a)</td><td>7.80 (n/a)</td><td>2.64 (n/a)</td><td>13.94 (n/a)</td><td>9.95 (n/a)</td><td>8.47 (n/a)</td><td>7.79 (n/a)</td><td>2.63 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>498.60 (n/a)</td><td>305.76 (n/a)</td><td>264.60 (n/a)</td><td>235.10 (n/a)</td><td>109.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.50 (n/a)</td><td>404.18 (n/a)</td><td>481.10 (n/a)</td><td>213.50 (n/a)</td><td>162.59 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.30 (n/a)</td><td>402.64 (n/a)</td><td>476.20 (n/a)</td><td>221.20 (n/a)</td><td>139.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1847.70 (n/a)</td><td>844.28 (n/a)</td><td>532.50 (n/a)</td><td>304.80 (n/a)</td><td>618.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.20 (n/a)</td><td>473.06 (n/a)</td><td>470.60 (n/a)</td><td>369.00 (n/a)</td><td>66.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.80 (n/a)</td><td>468.18 (n/a)</td><td>496.40 (n/a)</td><td>237.70 (n/a)</td><td>137.11 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2443.90 (n/a)</td><td>776.24 (n/a)</td><td>446.60 (n/a)</td><td>240.10 (n/a)</td><td>937.60 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.50 (n/a)</td><td>398.10 (n/a)</td><td>428.60 (n/a)</td><td>234.30 (n/a)</td><td>103.58 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.20 (n/a)</td><td>462.18 (n/a)</td><td>480.90 (n/a)</td><td>279.50 (n/a)</td><td>121.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2329.20 (n/a)</td><td>909.72 (n/a)</td><td>592.90 (n/a)</td><td>231.00 (n/a)</td><td>869.81 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>552.00 (n/a)</td><td>489.80 (n/a)</td><td>526.60 (n/a)</td><td>310.90 (n/a)</td><td>101.23 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>477.00 (n/a)</td><td>350.62 (n/a)</td><td>319.20 (n/a)</td><td>303.40 (n/a)</td><td>71.72 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>533.60 (n/a)</td><td>430.98 (n/a)</td><td>511.60 (n/a)</td><td>273.10 (n/a)</td><td>129.69 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.10 (n/a)</td><td>389.32 (n/a)</td><td>394.40 (n/a)</td><td>241.70 (n/a)</td><td>134.38 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>554.00 (n/a)</td><td>418.16 (n/a)</td><td>424.60 (n/a)</td><td>288.90 (n/a)</td><td>105.86 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>688.60 (n/a)</td><td>416.72 (n/a)</td><td>457.70 (n/a)</td><td>191.00 (n/a)</td><td>209.89 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>586.50 (n/a)</td><td>479.44 (n/a)</td><td>508.20 (n/a)</td><td>286.50 (n/a)</td><td>113.71 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>672.20 (n/a)</td><td>504.90 (n/a)</td><td>546.90 (n/a)</td><td>248.40 (n/a)</td><td>162.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (-1.61%)</td><td>0.10 (+2.70%)</td><td>0.11 <b>(+27.81%)</b></td><td>0.06 (-13.81%)</td><td>0.03 <b>(+22.71%)</b></td><td>556.40 (+16.01%)</td><td>381.18 (+2.42%)</td><td>287.40 <b>(-21.75%)</b></td><td>251.10 (+1.62%)</td><td>150.73 <b>(+45.59%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>479.60 (n/a)</td><td>372.16 (n/a)</td><td>367.30 (n/a)</td><td>247.10 (n/a)</td><td>103.53 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>488.10 (n/a)</td><td>406.12 (n/a)</td><td>435.50 (n/a)</td><td>248.20 (n/a)</td><td>92.12 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>683.10 (n/a)</td><td>455.72 (n/a)</td><td>499.50 (n/a)</td><td>220.20 (n/a)</td><td>201.78 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>526.40 (n/a)</td><td>482.36 (n/a)</td><td>466.50 (n/a)</td><td>448.10 (n/a)</td><td>34.00 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>563.20 (n/a)</td><td>420.74 (n/a)</td><td>514.40 (n/a)</td><td>221.80 (n/a)</td><td>162.11 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>628.30 (n/a)</td><td>500.78 (n/a)</td><td>517.30 (n/a)</td><td>276.40 (n/a)</td><td>133.88 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (-14.17%)</td><td>0.01 (-18.59%)</td><td>0.01 (-1.45%)</td><td>0.00 <b>(-75.84%)</b></td><td>0.00 <b>(+27.31%)</b></td><td>2168.10 <b>(+314.00%)</b></td><td>735.70 <b>(+89.74%)</b></td><td>389.40 (+1.49%)</td><td>314.30 (+16.49%)</td><td>803.32 <b>(+579.79%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>523.70 (n/a)</td><td>387.74 (n/a)</td><td>383.70 (n/a)</td><td>269.80 (n/a)</td><td>118.17 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-11.93%)</td><td>0.01 <b>(-23.79%)</b></td><td>0.01 <b>(-36.01%)</b></td><td>0.01 (+7.64%)</td><td>0.00 (-8.35%)</td><td>519.40 (-7.10%)</td><td>456.48 <b>(+29.81%)</b></td><td>499.50 <b>(+56.29%)</b></td><td>257.60 (+13.53%)</td><td>111.55 (-9.89%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.10 (n/a)</td><td>351.64 (n/a)</td><td>319.60 (n/a)</td><td>226.90 (n/a)</td><td>123.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-6.64%)</td><td>0.01 <b>(+20.57%)</b></td><td>0.01 <b>(+56.22%)</b></td><td>0.01 <b>(+46.28%)</b></td><td>0.00 <b>(-44.36%)</b></td><td>465.50 <b>(-31.63%)</b></td><td>329.00 <b>(-26.81%)</b></td><td>296.40 <b>(-36.00%)</b></td><td>255.20 (+7.09%)</td><td>82.77 <b>(-57.13%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>680.90 (n/a)</td><td>449.54 (n/a)</td><td>463.10 (n/a)</td><td>238.30 (n/a)</td><td>193.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (+5.54%)</td><td>0.02 <b>(+26.47%)</b></td><td>0.02 (+13.88%)</td><td>0.01 <b>(+463.55%)</b></td><td>0.00 <b>(-43.38%)</b></td><td>347.80 <b>(-82.25%)</b></td><td>246.14 <b>(-58.45%)</b></td><td>234.60 (-12.17%)</td><td>182.90 (-5.23%)</td><td>63.32 <b>(-91.73%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1959.90 (n/a)</td><td>592.34 (n/a)</td><td>267.10 (n/a)</td><td>193.00 (n/a)</td><td>765.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 <b>(+20.57%)</b></td><td>0.01 (-3.62%)</td><td>0.01 <b>(-25.46%)</b></td><td>0.01 (-7.82%)</td><td>0.00 <b>(+39.12%)</b></td><td>592.30 (+8.48%)</td><td>415.52 (+9.98%)</td><td>393.70 <b>(+34.14%)</b></td><td>239.80 (-17.08%)</td><td>163.00 <b>(+34.94%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.00 (n/a)</td><td>377.82 (n/a)</td><td>293.50 (n/a)</td><td>289.20 (n/a)</td><td>120.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 <b>(-20.03%)</b></td><td>0.01 (-8.12%)</td><td>0.01 (-0.09%)</td><td>0.01 (-14.16%)</td><td>0.00 <b>(-24.54%)</b></td><td>583.60 (+16.49%)</td><td>351.48 (+7.92%)</td><td>299.30 (+0.10%)</td><td>230.50 <b>(+25.00%)</b></td><td>136.26 (+18.22%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>501.00 (n/a)</td><td>325.70 (n/a)</td><td>299.00 (n/a)</td><td>184.40 (n/a)</td><td>115.25 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 <b>(-23.83%)</b></td><td>0.01 (+11.63%)</td><td>0.01 <b>(+70.37%)</b></td><td>0.01 (+12.91%)</td><td>0.00 <b>(-37.65%)</b></td><td>598.20 (-11.43%)</td><td>378.76 (-18.58%)</td><td>315.90 <b>(-41.29%)</b></td><td>274.80 <b>(+31.29%)</b></td><td>137.25 <b>(-28.33%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>675.40 (n/a)</td><td>465.20 (n/a)</td><td>538.10 (n/a)</td><td>209.30 (n/a)</td><td>191.51 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (-7.79%)</td><td>0.01 (-10.25%)</td><td>0.01 (-6.40%)</td><td>0.01 (-10.67%)</td><td>0.00 <b>(-20.69%)</b></td><td>572.50 (+11.93%)</td><td>412.10 (+10.16%)</td><td>416.90 (+6.84%)</td><td>295.90 (+8.43%)</td><td>103.70 (+2.52%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.50 (n/a)</td><td>374.10 (n/a)</td><td>390.20 (n/a)</td><td>272.90 (n/a)</td><td>101.15 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 <b>(+35.22%)</b></td><td>0.01 <b>(+31.00%)</b></td><td>0.01 (+0.65%)</td><td>0.01 <b>(+215.93%)</b></td><td>0.01 <b>(+22.21%)</b></td><td>673.30 <b>(-68.35%)</b></td><td>466.76 <b>(-41.28%)</b></td><td>546.10 (-0.65%)</td><td>230.90 <b>(-26.04%)</b></td><td>188.09 <b>(-74.99%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2127.30 (n/a)</td><td>794.90 (n/a)</td><td>549.70 (n/a)</td><td>312.20 (n/a)</td><td>751.93 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (+17.52%)</td><td>0.01 (+12.79%)</td><td>0.01 <b>(+36.83%)</b></td><td>0.01 (-16.42%)</td><td>0.01 <b>(+61.20%)</b></td><td>594.00 (+19.64%)</td><td>382.80 (-1.73%)</td><td>300.50 <b>(-26.92%)</b></td><td>207.70 (-14.91%)</td><td>172.07 <b>(+82.82%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.50 (n/a)</td><td>389.52 (n/a)</td><td>411.20 (n/a)</td><td>244.10 (n/a)</td><td>94.12 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-1.76%)</td><td>0.01 (+3.14%)</td><td>0.01 <b>(+43.41%)</b></td><td>0.01 <b>(-22.99%)</b></td><td>0.00 (+16.61%)</td><td>695.60 <b>(+29.87%)</b></td><td>417.28 (+3.80%)</td><td>325.20 <b>(-30.26%)</b></td><td>247.70 (+1.81%)</td><td>197.01 <b>(+54.09%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>535.60 (n/a)</td><td>402.00 (n/a)</td><td>466.30 (n/a)</td><td>243.30 (n/a)</td><td>127.85 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (-4.23%)</td><td>0.01 <b>(-30.78%)</b></td><td>0.01 <b>(-43.45%)</b></td><td>0.00 <b>(-75.64%)</b></td><td>0.00 <b>(+86.79%)</b></td><td>1905.40 <b>(+310.47%)</b></td><td>752.22 <b>(+109.31%)</b></td><td>568.60 <b>(+76.86%)</b></td><td>289.80 (+4.39%)</td><td>658.30 <b>(+750.85%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.20 (n/a)</td><td>359.38 (n/a)</td><td>321.50 (n/a)</td><td>277.60 (n/a)</td><td>77.37 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (-16.51%)</td><td>0.02 (-7.05%)</td><td>0.03 (-8.89%)</td><td>0.02 (+9.16%)</td><td>0.01 <b>(-32.12%)</b></td><td>529.10 (-8.40%)</td><td>368.74 (+1.45%)</td><td>324.80 (+9.77%)</td><td>266.60 (+19.77%)</td><td>108.77 <b>(-26.52%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.60 (n/a)</td><td>363.46 (n/a)</td><td>295.90 (n/a)</td><td>222.60 (n/a)</td><td>148.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 <b>(-29.64%)</b></td><td>0.02 (-17.82%)</td><td>0.03 (-10.03%)</td><td>0.01 (-14.32%)</td><td>0.01 <b>(-34.94%)</b></td><td>556.20 (+16.70%)</td><td>358.92 (+18.78%)</td><td>309.60 (+11.13%)</td><td>248.80 <b>(+42.17%)</b></td><td>120.97 (+10.71%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.60 (n/a)</td><td>302.16 (n/a)</td><td>278.60 (n/a)</td><td>175.00 (n/a)</td><td>109.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (-14.21%)</td><td>0.02 (-18.40%)</td><td>0.02 (+4.39%)</td><td>0.00 <b>(-68.45%)</b></td><td>0.01 (-8.23%)</td><td>1855.70 <b>(+217.00%)</b></td><td>676.86 <b>(+65.18%)</b></td><td>462.50 (-4.20%)</td><td>227.70 (+16.53%)</td><td>670.03 <b>(+266.67%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.40 (n/a)</td><td>409.78 (n/a)</td><td>482.80 (n/a)</td><td>195.40 (n/a)</td><td>182.74 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (+4.47%)</td><td>0.02 (-4.20%)</td><td>0.03 (+6.55%)</td><td>0.00 <b>(-75.59%)</b></td><td>0.01 <b>(+81.56%)</b></td><td>2090.90 <b>(+309.66%)</b></td><td>659.04 <b>(+82.49%)</b></td><td>294.30 (-6.12%)</td><td>242.80 (-4.30%)</td><td>801.84 <b>(+685.77%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.40 (n/a)</td><td>361.14 (n/a)</td><td>313.50 (n/a)</td><td>253.70 (n/a)</td><td>102.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 <b>(+119.21%)</b></td><td>0.02 <b>(+37.68%)</b></td><td>0.02 (+4.79%)</td><td>0.00 <b>(-76.32%)</b></td><td>0.02 <b>(+737.91%)</b></td><td>2485.20 <b>(+322.29%)</b></td><td>776.80 <b>(+54.25%)</b></td><td>474.50 (-4.57%)</td><td>196.70 <b>(-54.38%)</b></td><td>964.12 <b>(+1604.04%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.50 (n/a)</td><td>503.60 (n/a)</td><td>497.20 (n/a)</td><td>431.20 (n/a)</td><td>56.58 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 <b>(+21.74%)</b></td><td>0.03 <b>(+39.62%)</b></td><td>0.03 <b>(+78.59%)</b></td><td>0.02 <b>(+245.91%)</b></td><td>0.01 (-10.65%)</td><td>537.00 <b>(-71.09%)</b></td><td>325.62 <b>(-51.16%)</b></td><td>258.80 <b>(-44.01%)</b></td><td>199.10 (-17.83%)</td><td>140.44 <b>(-79.21%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1857.60 (n/a)</td><td>666.72 (n/a)</td><td>462.20 (n/a)</td><td>242.30 (n/a)</td><td>675.66 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 <b>(+88.47%)</b></td><td>0.03 <b>(+58.17%)</b></td><td>0.03 <b>(+42.35%)</b></td><td>0.01 (-4.30%)</td><td>0.01 <b>(+246.10%)</b></td><td>622.10 (+4.50%)</td><td>354.00 <b>(-27.51%)</b></td><td>326.70 <b>(-29.74%)</b></td><td>196.00 <b>(-46.94%)</b></td><td>169.63 <b>(+87.43%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>595.30 (n/a)</td><td>488.34 (n/a)</td><td>465.00 (n/a)</td><td>369.40 (n/a)</td><td>90.50 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (-9.30%)</td><td>0.03 <b>(+32.23%)</b></td><td>0.03 <b>(+36.96%)</b></td><td>0.02 <b>(+296.74%)</b></td><td>0.01 <b>(-53.69%)</b></td><td>458.70 <b>(-74.79%)</b></td><td>314.00 <b>(-52.35%)</b></td><td>286.20 <b>(-26.99%)</b></td><td>253.10 (+10.24%)</td><td>82.15 <b>(-87.55%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1819.60 (n/a)</td><td>659.02 (n/a)</td><td>392.00 (n/a)</td><td>229.60 (n/a)</td><td>659.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 <b>(+53.18%)</b></td><td>0.03 <b>(+41.44%)</b></td><td>0.03 <b>(+65.90%)</b></td><td>0.02 (+10.34%)</td><td>0.01 <b>(+251.90%)</b></td><td>487.30 (-9.37%)</td><td>351.66 <b>(-23.87%)</b></td><td>271.80 <b>(-39.73%)</b></td><td>253.20 <b>(-34.71%)</b></td><td>119.21 <b>(+114.21%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>537.70 (n/a)</td><td>461.92 (n/a)</td><td>451.00 (n/a)</td><td>387.80 (n/a)</td><td>55.65 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (-3.62%)</td><td>0.02 (-4.82%)</td><td>0.02 (-6.18%)</td><td>0.01 (-10.17%)</td><td>0.01 (+3.94%)</td><td>635.70 (+11.31%)</td><td>463.44 (+7.44%)</td><td>503.60 (+6.58%)</td><td>257.10 (+3.75%)</td><td>156.73 <b>(+21.94%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.10 (n/a)</td><td>431.36 (n/a)</td><td>472.50 (n/a)</td><td>247.80 (n/a)</td><td>128.53 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (+2.35%)</td><td>0.02 (+10.06%)</td><td>0.03 <b>(+70.34%)</b></td><td>0.02 (+13.02%)</td><td>0.01 <b>(-22.87%)</b></td><td>502.70 (-11.51%)</td><td>365.64 (-14.83%)</td><td>312.80 <b>(-41.30%)</b></td><td>238.90 (-2.29%)</td><td>117.41 <b>(-28.71%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.10 (n/a)</td><td>429.30 (n/a)</td><td>532.90 (n/a)</td><td>244.50 (n/a)</td><td>164.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 <b>(-23.13%)</b></td><td>0.02 <b>(-22.14%)</b></td><td>0.01 (+7.21%)</td><td>0.01 <b>(-32.73%)</b></td><td>0.01 <b>(-33.97%)</b></td><td>914.50 <b>(+48.68%)</b></td><td>577.14 <b>(+22.91%)</b></td><td>551.50 (-6.72%)</td><td>302.70 <b>(+30.08%)</b></td><td>221.99 (+17.48%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.10 (n/a)</td><td>469.58 (n/a)</td><td>591.20 (n/a)</td><td>232.70 (n/a)</td><td>188.95 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 <b>(-26.90%)</b></td><td>0.05 (-8.37%)</td><td>0.06 (+9.77%)</td><td>0.03 (+3.15%)</td><td>0.01 <b>(-27.22%)</b></td><td>513.30 (-3.04%)</td><td>359.36 (+6.41%)</td><td>281.40 (-8.90%)</td><td>265.60 <b>(+36.84%)</b></td><td>116.44 (-4.40%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>529.40 (n/a)</td><td>337.72 (n/a)</td><td>308.90 (n/a)</td><td>194.10 (n/a)</td><td>121.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 <b>(-27.72%)</b></td><td>0.05 (-4.79%)</td><td>0.06 (+2.46%)</td><td>0.03 (+3.98%)</td><td>0.01 <b>(-42.37%)</b></td><td>511.80 (-3.82%)</td><td>338.96 (-3.79%)</td><td>276.20 (-2.40%)</td><td>259.10 <b>(+38.33%)</b></td><td>107.68 <b>(-29.50%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>532.10 (n/a)</td><td>352.32 (n/a)</td><td>283.00 (n/a)</td><td>187.30 (n/a)</td><td>152.74 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (-8.20%)</td><td>0.05 (-6.73%)</td><td>0.05 <b>(-20.96%)</b></td><td>0.03 (-8.83%)</td><td>0.02 <b>(-23.46%)</b></td><td>543.00 (+9.67%)</td><td>340.70 (+1.52%)</td><td>327.20 <b>(+26.48%)</b></td><td>207.20 (+8.94%)</td><td>125.03 (-15.34%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>495.10 (n/a)</td><td>335.60 (n/a)</td><td>258.70 (n/a)</td><td>190.20 (n/a)</td><td>147.68 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 <b>(+75.80%)</b></td><td>0.05 <b>(+44.08%)</b></td><td>0.05 <b>(+53.44%)</b></td><td>0.03 (-7.33%)</td><td>0.02 <b>(+255.24%)</b></td><td>599.40 (+7.90%)</td><td>356.62 <b>(-22.52%)</b></td><td>299.60 <b>(-34.83%)</b></td><td>210.70 <b>(-43.12%)</b></td><td>152.45 <b>(+125.18%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>555.50 (n/a)</td><td>460.26 (n/a)</td><td>459.70 (n/a)</td><td>370.40 (n/a)</td><td>67.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 <b>(+33.40%)</b></td><td>0.05 (+17.55%)</td><td>0.04 <b>(+22.56%)</b></td><td>0.03 (-7.74%)</td><td>0.03 <b>(+55.77%)</b></td><td>596.10 (+8.38%)</td><td>402.84 (-5.98%)</td><td>432.30 (-18.40%)</td><td>186.90 <b>(-25.03%)</b></td><td>190.01 <b>(+25.84%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>550.00 (n/a)</td><td>428.44 (n/a)</td><td>529.80 (n/a)</td><td>249.30 (n/a)</td><td>151.00 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 <b>(-36.35%)</b></td><td>0.05 <b>(-32.76%)</b></td><td>0.05 <b>(-34.56%)</b></td><td>0.03 (-4.86%)</td><td>0.01 <b>(-56.14%)</b></td><td>507.80 (+5.11%)</td><td>354.48 <b>(+35.94%)</b></td><td>340.60 <b>(+52.80%)</b></td><td>272.10 <b>(+57.10%)</b></td><td>91.61 <b>(-28.19%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>483.10 (n/a)</td><td>260.76 (n/a)</td><td>222.90 (n/a)</td><td>173.20 (n/a)</td><td>127.57 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (-15.71%)</td><td>0.04 (-11.95%)</td><td>0.03 <b>(-21.57%)</b></td><td>0.03 <b>(-27.68%)</b></td><td>0.01 (+5.62%)</td><td>638.60 <b>(+38.28%)</b></td><td>445.56 (+17.77%)</td><td>476.40 <b>(+27.48%)</b></td><td>291.50 (+18.64%)</td><td>145.54 <b>(+61.86%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>461.80 (n/a)</td><td>378.32 (n/a)</td><td>373.70 (n/a)</td><td>245.70 (n/a)</td><td>89.92 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 <b>(-56.47%)</b></td><td>0.03 <b>(-45.88%)</b></td><td>0.03 <b>(-41.20%)</b></td><td>0.03 <b>(-25.85%)</b></td><td>0.00 <b>(-84.55%)</b></td><td>600.60 <b>(+34.88%)</b></td><td>550.44 <b>(+70.23%)</b></td><td>561.40 <b>(+70.07%)</b></td><td>469.20 <b>(+129.66%)</b></td><td>48.64 <b>(-52.96%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>445.30 (n/a)</td><td>323.36 (n/a)</td><td>330.10 (n/a)</td><td>204.30 (n/a)</td><td>103.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (-10.94%)</td><td>0.04 (-12.12%)</td><td>0.04 <b>(+22.12%)</b></td><td>0.01 <b>(+112.18%)</b></td><td>0.02 <b>(-34.07%)</b></td><td>1161.50 <b>(-52.87%)</b></td><td>590.92 <b>(-28.47%)</b></td><td>459.30 (-18.11%)</td><td>253.20 (+12.28%)</td><td>346.27 <b>(-62.93%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2464.50 (n/a)</td><td>826.06 (n/a)</td><td>560.90 (n/a)</td><td>225.50 (n/a)</td><td>934.15 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 <b>(+20.20%)</b></td><td>0.05 (+18.91%)</td><td>0.06 <b>(+41.92%)</b></td><td>0.03 (-1.80%)</td><td>0.02 <b>(+33.57%)</b></td><td>570.80 (+1.84%)</td><td>361.82 (-12.51%)</td><td>293.80 <b>(-29.54%)</b></td><td>227.50 (-16.79%)</td><td>145.90 (+15.37%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>560.50 (n/a)</td><td>413.56 (n/a)</td><td>417.00 (n/a)</td><td>273.40 (n/a)</td><td>126.45 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (-7.07%)</td><td>0.04 (+5.71%)</td><td>0.04 (+14.20%)</td><td>0.03 (+3.45%)</td><td>0.01 (-19.08%)</td><td>511.70 (-3.33%)</td><td>408.08 (-6.78%)</td><td>402.20 (-12.43%)</td><td>294.40 (+7.60%)</td><td>87.21 (-10.85%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>529.30 (n/a)</td><td>437.76 (n/a)</td><td>459.30 (n/a)</td><td>273.60 (n/a)</td><td>97.82 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 (+5.11%)</td><td>0.04 <b>(+33.14%)</b></td><td>0.04 <b>(+37.12%)</b></td><td>0.03 <b>(+74.07%)</b></td><td>0.01 <b>(-21.94%)</b></td><td>600.00 <b>(-42.55%)</b></td><td>405.24 <b>(-31.32%)</b></td><td>365.40 <b>(-27.07%)</b></td><td>307.70 (-4.85%)</td><td>114.95 <b>(-57.61%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1044.40 (n/a)</td><td>590.06 (n/a)</td><td>501.00 (n/a)</td><td>323.40 (n/a)</td><td>271.17 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (-9.19%)</td><td>0.10 (-3.20%)</td><td>0.09 (-18.38%)</td><td>0.06 (-9.92%)</td><td>0.03 (+1.57%)</td><td>587.30 (+11.02%)</td><td>386.30 (+4.55%)</td><td>380.30 <b>(+22.52%)</b></td><td>247.60 (+10.09%)</td><td>144.92 (+10.83%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>529.00 (n/a)</td><td>369.48 (n/a)</td><td>310.40 (n/a)</td><td>224.90 (n/a)</td><td>130.76 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.15 <b>(+34.55%)</b></td><td>0.12 <b>(+32.16%)</b></td><td>0.13 <b>(+42.41%)</b></td><td>0.06 (-5.63%)</td><td>0.03 <b>(+78.96%)</b></td><td>519.90 (+5.95%)</td><td>302.26 (-19.82%)</td><td>246.00 <b>(-29.77%)</b></td><td>225.10 <b>(-25.69%)</b></td><td>123.65 <b>(+49.14%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>490.70 (n/a)</td><td>377.00 (n/a)</td><td>350.30 (n/a)</td><td>302.90 (n/a)</td><td>82.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (+7.64%)</td><td>0.11 <b>(+40.23%)</b></td><td>0.11 <b>(+78.32%)</b></td><td>0.07 (+12.44%)</td><td>0.03 (+6.38%)</td><td>470.50 (-11.06%)</td><td>330.64 <b>(-29.05%)</b></td><td>286.40 <b>(-43.93%)</b></td><td>240.80 (-7.10%)</td><td>102.63 (-11.58%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>529.00 (n/a)</td><td>466.00 (n/a)</td><td>510.80 (n/a)</td><td>259.20 (n/a)</td><td>116.07 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (+6.41%)</td><td>0.10 <b>(+23.21%)</b></td><td>0.11 <b>(+62.07%)</b></td><td>0.08 <b>(+33.46%)</b></td><td>0.02 <b>(-34.44%)</b></td><td>408.30 <b>(-25.08%)</b></td><td>323.96 <b>(-22.88%)</b></td><td>294.10 <b>(-38.29%)</b></td><td>267.90 (-6.00%)</td><td>58.66 <b>(-51.71%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>545.00 (n/a)</td><td>420.08 (n/a)</td><td>476.60 (n/a)</td><td>285.00 (n/a)</td><td>121.46 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (+7.32%)</td><td>0.11 <b>(+22.05%)</b></td><td>0.12 <b>(+64.11%)</b></td><td>0.06 (-7.85%)</td><td>0.03 (-0.45%)</td><td>515.80 (+8.52%)</td><td>318.86 (-17.94%)</td><td>281.90 <b>(-39.07%)</b></td><td>245.30 (-6.80%)</td><td>112.10 (+3.82%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>475.30 (n/a)</td><td>388.58 (n/a)</td><td>462.70 (n/a)</td><td>263.20 (n/a)</td><td>107.98 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.15 (+2.26%)</td><td>0.09 (+8.38%)</td><td>0.11 <b>(+81.72%)</b></td><td>0.02 <b>(-69.72%)</b></td><td>0.05 <b>(+22.02%)</b></td><td>2097.90 <b>(+230.22%)</b></td><td>666.30 <b>(+48.65%)</b></td><td>297.10 <b>(-44.97%)</b></td><td>218.40 (-2.24%)</td><td>804.70 <b>(+339.96%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>635.30 (n/a)</td><td>448.24 (n/a)</td><td>539.90 (n/a)</td><td>223.40 (n/a)</td><td>182.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (+7.06%)</td><td>0.10 <b>(+20.13%)</b></td><td>0.12 <b>(+73.38%)</b></td><td>0.06 (+17.91%)</td><td>0.03 (+10.22%)</td><td>551.70 (-15.19%)</td><td>382.90 (-16.28%)</td><td>284.30 <b>(-42.33%)</b></td><td>256.20 (-6.60%)</td><td>153.06 (-5.70%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>650.50 (n/a)</td><td>457.34 (n/a)</td><td>493.00 (n/a)</td><td>274.30 (n/a)</td><td>162.30 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (+19.46%)</td><td>0.11 <b>(+30.97%)</b></td><td>0.11 <b>(+64.26%)</b></td><td>0.06 (+14.41%)</td><td>0.03 (-0.07%)</td><td>513.50 (-12.60%)</td><td>334.30 <b>(-25.41%)</b></td><td>289.10 <b>(-39.12%)</b></td><td>242.30 (-16.30%)</td><td>108.55 <b>(-24.96%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.50 (n/a)</td><td>448.18 (n/a)</td><td>474.90 (n/a)</td><td>289.50 (n/a)</td><td>144.65 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (+19.73%)</td><td>0.11 <b>(+44.82%)</b></td><td>0.13 <b>(+111.05%)</b></td><td>0.06 (+13.16%)</td><td>0.04 <b>(+42.63%)</b></td><td>545.90 (-11.64%)</td><td>352.28 <b>(-28.10%)</b></td><td>260.30 <b>(-52.62%)</b></td><td>233.10 (-16.48%)</td><td>150.53 (+1.04%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>617.80 (n/a)</td><td>489.98 (n/a)</td><td>549.40 (n/a)</td><td>279.10 (n/a)</td><td>148.98 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (-2.43%)</td><td>0.08 (-9.58%)</td><td>0.08 (+10.79%)</td><td>0.06 (-8.17%)</td><td>0.03 (-4.23%)</td><td>595.60 (+8.88%)</td><td>434.96 (+11.62%)</td><td>386.20 (-9.72%)</td><td>250.00 (+2.50%)</td><td>149.46 (+17.17%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>547.00 (n/a)</td><td>389.68 (n/a)</td><td>427.80 (n/a)</td><td>243.90 (n/a)</td><td>127.56 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 <b>(-43.96%)</b></td><td>0.06 <b>(-33.94%)</b></td><td>0.05 <b>(-26.83%)</b></td><td>0.05 <b>(-28.87%)</b></td><td>0.01 <b>(-62.76%)</b></td><td>678.80 <b>(+40.57%)</b></td><td>590.44 <b>(+45.58%)</b></td><td>612.10 <b>(+36.66%)</b></td><td>443.30 <b>(+78.46%)</b></td><td>87.64 (-8.61%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>482.90 (n/a)</td><td>405.58 (n/a)</td><td>447.90 (n/a)</td><td>248.40 (n/a)</td><td>95.90 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (-6.13%)</td><td>0.06 (-6.20%)</td><td>0.07 <b>(+22.10%)</b></td><td>0.02 <b>(-55.96%)</b></td><td>0.03 <b>(+20.92%)</b></td><td>1828.70 <b>(+127.08%)</b></td><td>739.46 <b>(+35.68%)</b></td><td>464.40 (-18.10%)</td><td>335.50 (+6.51%)</td><td>616.71 <b>(+234.92%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>805.30 (n/a)</td><td>545.02 (n/a)</td><td>567.00 (n/a)</td><td>315.00 (n/a)</td><td>184.14 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 <b>(+29.11%)</b></td><td>0.02 <b>(+27.33%)</b></td><td>0.02 <b>(+25.23%)</b></td><td>0.01 (+19.65%)</td><td>0.01 <b>(+38.17%)</b></td><td>487.10 (-16.42%)</td><td>302.04 (-19.29%)</td><td>239.20 <b>(-20.16%)</b></td><td>181.00 <b>(-22.55%)</b></td><td>142.85 (-12.25%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.80 (n/a)</td><td>374.22 (n/a)</td><td>299.60 (n/a)</td><td>233.70 (n/a)</td><td>162.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-6.40%)</td><td>0.02 (-11.96%)</td><td>0.01 <b>(-31.86%)</b></td><td>0.01 <b>(+37.54%)</b></td><td>0.01 (-4.99%)</td><td>529.30 <b>(-27.29%)</b></td><td>397.30 (+7.71%)</td><td>422.30 <b>(+46.73%)</b></td><td>249.10 (+6.82%)</td><td>135.11 <b>(-33.35%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>728.00 (n/a)</td><td>368.86 (n/a)</td><td>287.80 (n/a)</td><td>233.20 (n/a)</td><td>202.73 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 <b>(+57.32%)</b></td><td>0.01 <b>(+47.57%)</b></td><td>0.01 <b>(+58.79%)</b></td><td>0.01 (+5.63%)</td><td>0.01 <b>(+130.52%)</b></td><td>564.10 (-5.34%)</td><td>381.94 <b>(-24.20%)</b></td><td>333.30 <b>(-37.02%)</b></td><td>204.50 <b>(-36.43%)</b></td><td>166.74 <b>(+55.17%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>595.90 (n/a)</td><td>503.90 (n/a)</td><td>529.20 (n/a)</td><td>321.70 (n/a)</td><td>107.46 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 <b>(+46.32%)</b></td><td>0.02 (+6.00%)</td><td>0.01 <b>(-29.62%)</b></td><td>0.01 (-13.06%)</td><td>0.01 <b>(+91.61%)</b></td><td>677.30 (+15.01%)</td><td>408.66 (+8.75%)</td><td>421.00 <b>(+42.09%)</b></td><td>179.70 <b>(-31.67%)</b></td><td>203.99 <b>(+47.58%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.90 (n/a)</td><td>375.78 (n/a)</td><td>296.30 (n/a)</td><td>263.00 (n/a)</td><td>138.22 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.01 (-5.68%)</td><td>0.01 (-5.59%)</td><td>0.01 (-13.19%)</td><td>0.01 (+6.81%)</td><td>0.00 <b>(-22.02%)</b></td><td>532.00 (-6.39%)</td><td>446.98 (+2.98%)</td><td>480.10 (+15.19%)</td><td>304.00 (+6.03%)</td><td>87.51 <b>(-27.80%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.30 (n/a)</td><td>434.04 (n/a)</td><td>416.80 (n/a)</td><td>286.70 (n/a)</td><td>121.21 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (+0.32%)</td><td>0.02 (-16.86%)</td><td>0.02 <b>(-24.27%)</b></td><td>0.01 (-5.62%)</td><td>0.01 (+5.87%)</td><td>456.90 (+5.96%)</td><td>349.74 <b>(+21.28%)</b></td><td>332.00 <b>(+32.06%)</b></td><td>213.70 (-0.33%)</td><td>94.96 (+8.71%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>431.20 (n/a)</td><td>288.38 (n/a)</td><td>251.40 (n/a)</td><td>214.40 (n/a)</td><td>87.35 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (-13.22%)</td><td>0.01 (-4.31%)</td><td>0.01 (+11.12%)</td><td>0.01 (+14.37%)</td><td>0.00 <b>(-35.48%)</b></td><td>475.80 (-12.57%)</td><td>388.84 (-3.34%)</td><td>422.50 (-10.01%)</td><td>245.20 (+15.23%)</td><td>92.64 <b>(-37.03%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>544.20 (n/a)</td><td>402.26 (n/a)</td><td>469.50 (n/a)</td><td>212.80 (n/a)</td><td>147.11 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 (+4.43%)</td><td>0.01 (+15.78%)</td><td>0.01 (+4.75%)</td><td>0.01 (+15.80%)</td><td>0.00 (-8.26%)</td><td>565.70 (-13.65%)</td><td>386.20 (-16.99%)</td><td>381.10 (-4.53%)</td><td>246.60 (-4.23%)</td><td>122.35 <b>(-28.88%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>655.10 (n/a)</td><td>465.24 (n/a)</td><td>399.20 (n/a)</td><td>257.50 (n/a)</td><td>172.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 <b>(+68.12%)</b></td><td>0.01 (+10.65%)</td><td>0.01 (-17.93%)</td><td>0.00 <b>(-73.43%)</b></td><td>0.01 <b>(+347.07%)</b></td><td>1973.50 <b>(+276.33%)</b></td><td>713.46 <b>(+59.48%)</b></td><td>537.70 <b>(+21.84%)</b></td><td>205.20 <b>(-40.52%)</b></td><td>722.69 <b>(+939.99%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.40 (n/a)</td><td>447.36 (n/a)</td><td>441.30 (n/a)</td><td>345.00 (n/a)</td><td>69.49 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 <b>(+90.87%)</b></td><td>0.01 <b>(+31.79%)</b></td><td>0.01 <b>(+22.44%)</b></td><td>0.01 (+6.59%)</td><td>0.01 <b>(+234.04%)</b></td><td>602.90 (-6.18%)</td><td>424.02 (-16.20%)</td><td>422.20 (-18.32%)</td><td>218.60 <b>(-47.60%)</b></td><td>149.35 <b>(+63.98%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>642.60 (n/a)</td><td>506.02 (n/a)</td><td>516.90 (n/a)</td><td>417.20 (n/a)</td><td>91.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.02 <b>(+55.63%)</b></td><td>0.01 (+10.64%)</td><td>0.01 (-3.55%)</td><td>0.01 (-14.63%)</td><td>0.01 <b>(+98.98%)</b></td><td>603.00 (+17.13%)</td><td>400.44 (+0.32%)</td><td>431.00 (+3.66%)</td><td>173.90 <b>(-35.74%)</b></td><td>158.17 <b>(+39.11%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.80 (n/a)</td><td>399.18 (n/a)</td><td>415.80 (n/a)</td><td>270.60 (n/a)</td><td>113.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (-2.36%)</td><td>0.02 (+0.32%)</td><td>0.02 (-1.63%)</td><td>0.01 (-19.55%)</td><td>0.01 <b>(+22.60%)</b></td><td>622.10 <b>(+24.32%)</b></td><td>410.68 (+5.83%)</td><td>451.30 (+1.67%)</td><td>237.70 (+2.41%)</td><td>166.68 <b>(+42.32%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.40 (n/a)</td><td>388.04 (n/a)</td><td>443.90 (n/a)</td><td>232.10 (n/a)</td><td>117.11 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 <b>(+28.92%)</b></td><td>0.04 <b>(+28.92%)</b></td><td>0.04 <b>(+40.99%)</b></td><td>0.03 <b>(+26.55%)</b></td><td>0.01 <b>(+39.28%)</b></td><td>427.30 <b>(-20.99%)</b></td><td>316.30 <b>(-21.38%)</b></td><td>305.80 <b>(-29.07%)</b></td><td>219.40 <b>(-22.45%)</b></td><td>95.68 (-12.05%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.80 (n/a)</td><td>402.34 (n/a)</td><td>431.10 (n/a)</td><td>282.90 (n/a)</td><td>108.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (-15.34%)</td><td>0.02 (-9.44%)</td><td>0.02 (-19.83%)</td><td>0.01 <b>(+20.67%)</b></td><td>0.01 <b>(-28.85%)</b></td><td>650.20 (-17.13%)</td><td>425.40 (-0.56%)</td><td>438.70 <b>(+24.74%)</b></td><td>237.10 (+18.14%)</td><td>154.47 <b>(-32.94%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>784.60 (n/a)</td><td>427.78 (n/a)</td><td>351.70 (n/a)</td><td>200.70 (n/a)</td><td>230.36 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 <b>(+23.90%)</b></td><td>0.03 (+8.76%)</td><td>0.02 (-3.36%)</td><td>0.02 <b>(+28.29%)</b></td><td>0.01 <b>(+34.40%)</b></td><td>496.30 <b>(-22.05%)</b></td><td>422.58 (-7.24%)</td><td>461.20 (+3.48%)</td><td>236.60 (-19.28%)</td><td>106.44 (-17.89%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>636.70 (n/a)</td><td>455.56 (n/a)</td><td>445.70 (n/a)</td><td>293.10 (n/a)</td><td>129.63 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 <b>(+23.77%)</b></td><td>0.03 (-1.48%)</td><td>0.03 (+14.33%)</td><td>0.01 <b>(-24.13%)</b></td><td>0.01 <b>(+78.84%)</b></td><td>597.50 <b>(+31.81%)</b></td><td>338.22 (+16.46%)</td><td>239.80 (-12.51%)</td><td>175.90 (-19.24%)</td><td>178.37 <b>(+88.92%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>453.30 (n/a)</td><td>290.42 (n/a)</td><td>274.10 (n/a)</td><td>217.80 (n/a)</td><td>94.41 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.04 (-10.52%)</td><td>0.02 <b>(-25.36%)</b></td><td>0.02 (-19.72%)</td><td>0.01 <b>(-70.21%)</b></td><td>0.01 (+9.18%)</td><td>1919.80 <b>(+235.63%)</b></td><td>750.38 <b>(+82.36%)</b></td><td>538.90 <b>(+24.54%)</b></td><td>245.40 (+11.75%)</td><td>666.14 <b>(+345.76%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.00 (n/a)</td><td>411.48 (n/a)</td><td>432.70 (n/a)</td><td>219.60 (n/a)</td><td>149.44 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 <b>(+53.93%)</b></td><td>0.03 <b>(+43.25%)</b></td><td>0.03 <b>(+82.92%)</b></td><td>0.01 <b>(-21.02%)</b></td><td>0.02 <b>(+64.65%)</b></td><td>687.10 <b>(+26.61%)</b></td><td>320.20 <b>(-20.87%)</b></td><td>246.10 <b>(-45.32%)</b></td><td>143.60 <b>(-35.02%)</b></td><td>211.36 <b>(+43.35%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.70 (n/a)</td><td>404.64 (n/a)</td><td>450.10 (n/a)</td><td>221.00 (n/a)</td><td>147.44 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 <b>(-20.38%)</b></td><td>0.02 <b>(-26.11%)</b></td><td>0.02 <b>(-28.54%)</b></td><td>0.02 (+12.44%)</td><td>0.01 <b>(-42.68%)</b></td><td>572.20 (-11.07%)</td><td>475.52 <b>(+25.61%)</b></td><td>526.50 <b>(+39.95%)</b></td><td>307.30 <b>(+25.58%)</b></td><td>104.68 <b>(-35.36%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.40 (n/a)</td><td>378.58 (n/a)</td><td>376.20 (n/a)</td><td>244.70 (n/a)</td><td>161.94 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 (+7.08%)</td><td>0.02 <b>(+28.19%)</b></td><td>0.02 <b>(+36.04%)</b></td><td>0.02 <b>(+23.20%)</b></td><td>0.01 (-2.27%)</td><td>516.20 (-18.84%)</td><td>382.04 <b>(-24.23%)</b></td><td>406.90 <b>(-26.50%)</b></td><td>244.80 (-6.60%)</td><td>114.41 <b>(-26.88%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.00 (n/a)</td><td>504.18 (n/a)</td><td>553.60 (n/a)</td><td>262.10 (n/a)</td><td>156.48 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 <b>(+27.25%)</b></td><td>0.03 (+14.38%)</td><td>0.03 <b>(+60.36%)</b></td><td>0.02 (+8.97%)</td><td>0.01 (+16.53%)</td><td>556.40 (-8.23%)</td><td>365.28 (-11.56%)</td><td>299.10 <b>(-37.64%)</b></td><td>189.00 <b>(-21.41%)</b></td><td>156.25 (-3.82%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>606.30 (n/a)</td><td>413.04 (n/a)</td><td>479.60 (n/a)</td><td>240.50 (n/a)</td><td>162.46 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.03 <b>(-23.49%)</b></td><td>0.02 (-2.59%)</td><td>0.02 (+11.80%)</td><td>0.01 <b>(+72.29%)</b></td><td>0.01 <b>(-46.21%)</b></td><td>628.40 <b>(-41.97%)</b></td><td>471.42 (-14.52%)</td><td>467.70 (-10.57%)</td><td>307.20 <b>(+30.67%)</b></td><td>131.01 <b>(-59.47%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1082.80 (n/a)</td><td>551.50 (n/a)</td><td>523.00 (n/a)</td><td>235.10 (n/a)</td><td>323.21 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (+9.90%)</td><td>0.05 (-3.12%)</td><td>0.06 (+3.12%)</td><td>0.03 (+1.35%)</td><td>0.02 <b>(+26.30%)</b></td><td>647.50 (-1.33%)</td><td>386.84 (+6.71%)</td><td>286.70 (-3.01%)</td><td>243.10 (-9.02%)</td><td>175.20 (+6.31%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>656.20 (n/a)</td><td>362.50 (n/a)</td><td>295.60 (n/a)</td><td>267.20 (n/a)</td><td>164.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (+1.94%)</td><td>0.08 (+7.66%)</td><td>0.08 (-1.06%)</td><td>0.04 (+8.85%)</td><td>0.02 (-13.64%)</td><td>574.40 (-8.14%)</td><td>345.90 (-9.97%)</td><td>298.00 (+1.05%)</td><td>249.70 (-1.89%)</td><td>130.57 (-16.94%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>625.30 (n/a)</td><td>384.20 (n/a)</td><td>294.90 (n/a)</td><td>254.50 (n/a)</td><td>157.20 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (-8.32%)</td><td>0.05 (+9.76%)</td><td>0.04 (+19.50%)</td><td>0.03 <b>(+207.77%)</b></td><td>0.02 <b>(-28.51%)</b></td><td>608.10 <b>(-67.51%)</b></td><td>408.44 <b>(-40.20%)</b></td><td>431.10 (-16.32%)</td><td>236.10 (+9.05%)</td><td>163.96 <b>(-75.96%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1871.60 (n/a)</td><td>683.04 (n/a)</td><td>515.20 (n/a)</td><td>216.50 (n/a)</td><td>682.18 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (-18.78%)</td><td>0.06 (-11.29%)</td><td>0.04 <b>(-35.67%)</b></td><td>0.04 <b>(+35.48%)</b></td><td>0.02 <b>(-25.15%)</b></td><td>527.60 <b>(-26.19%)</b></td><td>413.94 (+4.41%)</td><td>502.70 <b>(+55.44%)</b></td><td>240.00 <b>(+23.14%)</b></td><td>136.11 <b>(-31.46%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>714.80 (n/a)</td><td>396.44 (n/a)</td><td>323.40 (n/a)</td><td>194.90 (n/a)</td><td>198.59 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.05 <b>(-22.72%)</b></td><td>0.04 <b>(-20.69%)</b></td><td>0.04 <b>(-32.40%)</b></td><td>0.03 (+10.91%)</td><td>0.01 <b>(-55.97%)</b></td><td>491.30 (-9.84%)</td><td>395.58 (+16.75%)</td><td>404.80 <b>(+47.95%)</b></td><td>307.50 <b>(+29.42%)</b></td><td>68.52 <b>(-47.81%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>544.90 (n/a)</td><td>338.82 (n/a)</td><td>273.60 (n/a)</td><td>237.60 (n/a)</td><td>131.29 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (-15.62%)</td><td>0.06 (+18.87%)</td><td>0.06 <b>(+41.52%)</b></td><td>0.03 (+6.93%)</td><td>0.02 <b>(-23.42%)</b></td><td>628.70 (-6.47%)</td><td>399.20 (-19.51%)</td><td>368.90 <b>(-29.33%)</b></td><td>261.10 (+18.52%)</td><td>151.68 (-10.00%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>672.20 (n/a)</td><td>495.96 (n/a)</td><td>522.00 (n/a)</td><td>220.30 (n/a)</td><td>168.54 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (+13.01%)</td><td>0.05 <b>(+23.03%)</b></td><td>0.05 <b>(+21.94%)</b></td><td>0.03 (+12.63%)</td><td>0.01 <b>(+32.82%)</b></td><td>545.70 (-11.22%)</td><td>353.72 (-17.00%)</td><td>328.30 (-17.99%)</td><td>250.70 (-11.51%)</td><td>121.39 (+0.53%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>614.70 (n/a)</td><td>426.16 (n/a)</td><td>400.30 (n/a)</td><td>283.30 (n/a)</td><td>120.75 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (+2.06%)</td><td>0.04 (-11.50%)</td><td>0.03 <b>(-22.33%)</b></td><td>0.03 (-5.67%)</td><td>0.01 (+2.04%)</td><td>663.00 (+6.01%)</td><td>528.46 (+13.40%)</td><td>592.90 <b>(+28.75%)</b></td><td>293.70 (-2.00%)</td><td>152.58 (+2.86%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>625.40 (n/a)</td><td>466.00 (n/a)</td><td>460.50 (n/a)</td><td>299.70 (n/a)</td><td>148.34 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (+8.16%)</td><td>0.04 (+2.40%)</td><td>0.03 (+2.92%)</td><td>0.02 (-7.96%)</td><td>0.02 (+6.43%)</td><td>684.50 (+8.67%)</td><td>437.48 (-0.93%)</td><td>481.10 (-2.85%)</td><td>225.00 (-7.56%)</td><td>187.55 (+6.13%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>629.90 (n/a)</td><td>441.58 (n/a)</td><td>495.20 (n/a)</td><td>243.40 (n/a)</td><td>176.71 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (+16.47%)</td><td>0.06 (+14.43%)</td><td>0.07 <b>(+63.99%)</b></td><td>0.03 (+8.32%)</td><td>0.02 (+19.14%)</td><td>545.00 (-7.67%)</td><td>371.50 (-9.80%)</td><td>276.30 <b>(-39.03%)</b></td><td>228.90 (-14.14%)</td><td>156.86 (+10.66%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.30 (n/a)</td><td>411.86 (n/a)</td><td>453.20 (n/a)</td><td>266.60 (n/a)</td><td>141.75 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (-0.93%)</td><td>0.04 (-10.50%)</td><td>0.03 <b>(-24.29%)</b></td><td>0.02 (-10.06%)</td><td>0.01 (-5.53%)</td><td>668.80 (+11.19%)</td><td>466.14 (+11.19%)</td><td>483.80 <b>(+32.08%)</b></td><td>283.00 (+0.96%)</td><td>144.56 (+2.17%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>601.50 (n/a)</td><td>419.24 (n/a)</td><td>366.30 (n/a)</td><td>280.30 (n/a)</td><td>141.49 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (-9.33%)</td><td>0.07 <b>(-20.88%)</b></td><td>0.06 <b>(-44.86%)</b></td><td>0.06 <b>(+98.10%)</b></td><td>0.03 <b>(-42.25%)</b></td><td>551.20 <b>(-49.52%)</b></td><td>484.42 (-0.64%)</td><td>528.60 <b>(+81.34%)</b></td><td>277.40 (+10.30%)</td><td>116.58 <b>(-67.46%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1092.00 (n/a)</td><td>487.56 (n/a)</td><td>291.50 (n/a)</td><td>251.50 (n/a)</td><td>358.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 <b>(-40.03%)</b></td><td>0.06 <b>(-31.86%)</b></td><td>0.07 (-18.68%)</td><td>0.02 <b>(-65.91%)</b></td><td>0.02 <b>(-24.76%)</b></td><td>1840.10 <b>(+193.34%)</b></td><td>749.68 <b>(+77.62%)</b></td><td>491.10 <b>(+22.96%)</b></td><td>417.70 <b>(+66.75%)</b></td><td>611.46 <b>(+297.24%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>627.30 (n/a)</td><td>422.08 (n/a)</td><td>399.40 (n/a)</td><td>250.50 (n/a)</td><td>153.92 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 (-4.93%)</td><td>0.11 (+12.47%)</td><td>0.09 <b>(+20.54%)</b></td><td>0.07 (-0.74%)</td><td>0.05 (-10.73%)</td><td>607.70 (+0.75%)</td><td>427.18 (-12.81%)</td><td>471.10 (-17.05%)</td><td>231.50 (+5.18%)</td><td>152.37 (-2.66%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>603.20 (n/a)</td><td>489.96 (n/a)</td><td>567.90 (n/a)</td><td>220.10 (n/a)</td><td>156.53 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 <b>(-58.55%)</b></td><td>0.06 <b>(-39.45%)</b></td><td>0.06 (-3.28%)</td><td>0.03 <b>(-48.12%)</b></td><td>0.02 <b>(-67.89%)</b></td><td>1107.00 <b>(+92.76%)</b></td><td>651.50 <b>(+51.40%)</b></td><td>554.40 (+3.39%)</td><td>478.80 <b>(+141.21%)</b></td><td>258.90 <b>(+50.45%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>574.30 (n/a)</td><td>430.32 (n/a)</td><td>536.20 (n/a)</td><td>198.50 (n/a)</td><td>172.09 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (-17.10%)</td><td>0.10 (+7.50%)</td><td>0.10 (+9.33%)</td><td>0.07 <b>(+32.12%)</b></td><td>0.03 <b>(-39.69%)</b></td><td>554.20 <b>(-24.31%)</b></td><td>413.26 (-14.78%)</td><td>406.20 (-8.53%)</td><td>304.10 <b>(+20.63%)</b></td><td>102.36 <b>(-45.79%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>732.20 (n/a)</td><td>484.96 (n/a)</td><td>444.10 (n/a)</td><td>252.10 (n/a)</td><td>188.81 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (-17.50%)</td><td>0.08 (+1.04%)</td><td>0.06 (-4.88%)</td><td>0.06 (+3.03%)</td><td>0.03 (-15.22%)</td><td>583.30 (-2.95%)</td><td>451.86 (-1.94%)</td><td>535.90 (+5.12%)</td><td>281.70 <b>(+21.21%)</b></td><td>148.29 (+5.15%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>601.00 (n/a)</td><td>460.82 (n/a)</td><td>509.80 (n/a)</td><td>232.40 (n/a)</td><td>141.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.17 <b>(+35.44%)</b></td><td>0.10 <b>(+21.59%)</b></td><td>0.09 (-0.52%)</td><td>0.07 <b>(+23.47%)</b></td><td>0.04 <b>(+63.15%)</b></td><td>539.10 (-19.02%)</td><td>400.62 (-13.79%)</td><td>426.40 (+0.52%)</td><td>216.30 <b>(-26.15%)</b></td><td>142.71 (+0.37%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>665.70 (n/a)</td><td>464.68 (n/a)</td><td>424.20 (n/a)</td><td>292.90 (n/a)</td><td>142.19 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (+10.65%)</td><td>0.07 (-15.60%)</td><td>0.06 (-16.30%)</td><td>0.02 <b>(-67.33%)</b></td><td>0.04 <b>(+44.18%)</b></td><td>1969.20 <b>(+206.11%)</b></td><td>751.50 <b>(+66.94%)</b></td><td>538.70 (+19.47%)</td><td>262.60 (-9.64%)</td><td>690.43 <b>(+361.38%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>643.30 (n/a)</td><td>450.16 (n/a)</td><td>450.90 (n/a)</td><td>290.60 (n/a)</td><td>149.64 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.15 <b>(+20.08%)</b></td><td>0.09 (-4.74%)</td><td>0.07 (-14.55%)</td><td>0.06 (-17.38%)</td><td>0.04 <b>(+66.85%)</b></td><td>631.20 <b>(+21.04%)</b></td><td>482.84 (+11.97%)</td><td>504.70 (+17.05%)</td><td>244.80 (-16.71%)</td><td>144.99 <b>(+54.18%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>521.50 (n/a)</td><td>431.22 (n/a)</td><td>431.20 (n/a)</td><td>293.90 (n/a)</td><td>94.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 <b>(+41.27%)</b></td><td>0.08 (+12.25%)</td><td>0.06 (-10.02%)</td><td>0.05 (-10.61%)</td><td>0.02 <b>(+296.48%)</b></td><td>632.80 (+11.86%)</td><td>469.58 (-4.76%)</td><td>521.40 (+11.13%)</td><td>320.60 <b>(-29.23%)</b></td><td>136.13 <b>(+197.28%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>565.70 (n/a)</td><td>493.06 (n/a)</td><td>469.20 (n/a)</td><td>453.00 (n/a)</td><td>45.79 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 <b>(-22.84%)</b></td><td>0.06 (-12.34%)</td><td>0.05 <b>(-37.64%)</b></td><td>0.04 <b>(+22.85%)</b></td><td>0.01 <b>(-43.90%)</b></td><td>479.50 (-18.60%)</td><td>391.48 (+2.79%)</td><td>443.90 <b>(+60.37%)</b></td><td>285.60 <b>(+29.58%)</b></td><td>93.30 <b>(-45.53%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>589.10 (n/a)</td><td>380.84 (n/a)</td><td>276.80 (n/a)</td><td>220.40 (n/a)</td><td>171.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (-0.53%)</td><td>0.06 (+1.43%)</td><td>0.07 (+4.64%)</td><td>0.04 (-0.36%)</td><td>0.02 (-6.23%)</td><td>575.50 (+0.37%)</td><td>367.22 (-1.91%)</td><td>312.50 (-4.43%)</td><td>278.30 (+0.54%)</td><td>121.32 (-1.46%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>573.40 (n/a)</td><td>374.38 (n/a)</td><td>327.00 (n/a)</td><td>276.80 (n/a)</td><td>123.12 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 <b>(+61.09%)</b></td><td>0.06 <b>(+41.07%)</b></td><td>0.04 (+8.97%)</td><td>0.03 (+11.62%)</td><td>0.03 <b>(+204.54%)</b></td><td>588.70 (-10.41%)</td><td>416.44 (-19.50%)</td><td>471.70 (-8.23%)</td><td>232.90 <b>(-37.93%)</b></td><td>169.90 <b>(+63.67%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>657.10 (n/a)</td><td>517.32 (n/a)</td><td>514.00 (n/a)</td><td>375.20 (n/a)</td><td>103.80 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (+9.90%)</td><td>0.05 (-8.19%)</td><td>0.05 <b>(-24.80%)</b></td><td>0.03 (+11.34%)</td><td>0.02 (-5.79%)</td><td>609.60 (-10.18%)</td><td>435.08 (+4.41%)</td><td>448.20 <b>(+33.00%)</b></td><td>232.60 (-9.00%)</td><td>143.70 <b>(-23.58%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>678.70 (n/a)</td><td>416.70 (n/a)</td><td>337.00 (n/a)</td><td>255.60 (n/a)</td><td>188.05 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (-10.18%)</td><td>0.05 (-15.32%)</td><td>0.05 (-9.72%)</td><td>0.03 <b>(-30.34%)</b></td><td>0.01 (+15.01%)</td><td>627.90 <b>(+43.55%)</b></td><td>467.72 <b>(+22.30%)</b></td><td>452.70 (+10.77%)</td><td>298.30 (+11.35%)</td><td>130.15 <b>(+85.86%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>437.40 (n/a)</td><td>382.44 (n/a)</td><td>408.70 (n/a)</td><td>267.90 (n/a)</td><td>70.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 <b>(-27.57%)</b></td><td>0.04 <b>(-28.85%)</b></td><td>0.04 <b>(-44.30%)</b></td><td>0.04 (+10.77%)</td><td>0.01 <b>(-56.03%)</b></td><td>574.60 (-9.73%)</td><td>503.44 <b>(+26.72%)</b></td><td>532.80 <b>(+79.51%)</b></td><td>347.20 <b>(+38.05%)</b></td><td>94.16 <b>(-45.74%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>636.50 (n/a)</td><td>397.30 (n/a)</td><td>296.80 (n/a)</td><td>251.50 (n/a)</td><td>173.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 (+12.65%)</td><td>0.07 <b>(+34.42%)</b></td><td>0.06 <b>(+27.84%)</b></td><td>0.03 <b>(+132.73%)</b></td><td>0.03 (+9.37%)</td><td>840.50 <b>(-57.03%)</b></td><td>455.04 <b>(-40.58%)</b></td><td>417.00 <b>(-21.78%)</b></td><td>238.80 (-11.23%)</td><td>247.95 <b>(-63.77%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1956.10 (n/a)</td><td>765.86 (n/a)</td><td>533.10 (n/a)</td><td>269.00 (n/a)</td><td>684.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 <b>(+30.61%)</b></td><td>0.08 <b>(+48.60%)</b></td><td>0.09 <b>(+65.57%)</b></td><td>0.05 <b>(+24.63%)</b></td><td>0.02 <b>(+43.24%)</b></td><td>482.80 (-19.77%)</td><td>314.14 <b>(-31.79%)</b></td><td>277.80 <b>(-39.60%)</b></td><td>250.30 <b>(-23.43%)</b></td><td>96.45 (-8.88%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>601.80 (n/a)</td><td>460.54 (n/a)</td><td>459.90 (n/a)</td><td>326.90 (n/a)</td><td>105.84 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (+0.20%)</td><td>0.06 (-8.14%)</td><td>0.04 <b>(-22.08%)</b></td><td>0.02 <b>(-42.83%)</b></td><td>0.03 <b>(+31.32%)</b></td><td>1048.80 <b>(+74.95%)</b></td><td>555.66 <b>(+26.74%)</b></td><td>588.50 <b>(+28.35%)</b></td><td>265.30 (-0.23%)</td><td>319.71 <b>(+107.04%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>599.50 (n/a)</td><td>438.44 (n/a)</td><td>458.50 (n/a)</td><td>265.90 (n/a)</td><td>154.42 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 <b>(-24.91%)</b></td><td>0.05 <b>(-27.15%)</b></td><td>0.04 (-18.18%)</td><td>0.02 <b>(-43.88%)</b></td><td>0.02 (-19.45%)</td><td>1024.50 <b>(+78.20%)</b></td><td>600.74 <b>(+43.22%)</b></td><td>550.40 <b>(+22.23%)</b></td><td>390.80 <b>(+33.20%)</b></td><td>253.90 <b>(+106.44%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>574.90 (n/a)</td><td>419.46 (n/a)</td><td>450.30 (n/a)</td><td>293.40 (n/a)</td><td>122.99 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.10 <b>(+78.78%)</b></td><td>0.07 <b>(+46.56%)</b></td><td>0.05 (+17.78%)</td><td>0.04 (+7.33%)</td><td>0.03 <b>(+340.06%)</b></td><td>549.90 (-6.83%)</td><td>402.58 <b>(-24.75%)</b></td><td>456.40 (-15.10%)</td><td>244.10 <b>(-44.07%)</b></td><td>138.09 <b>(+124.08%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>590.20 (n/a)</td><td>534.96 (n/a)</td><td>537.60 (n/a)</td><td>436.40 (n/a)</td><td>61.62 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (-11.84%)</td><td>0.06 (-14.81%)</td><td>0.07 (+18.24%)</td><td>0.01 <b>(-72.70%)</b></td><td>0.03 (+18.18%)</td><td>2092.70 <b>(+266.24%)</b></td><td>712.98 <b>(+77.43%)</b></td><td>347.70 (-15.42%)</td><td>299.00 (+13.43%)</td><td>774.57 <b>(+464.41%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>571.40 (n/a)</td><td>401.84 (n/a)</td><td>411.10 (n/a)</td><td>263.60 (n/a)</td><td>137.24 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (+12.88%)</td><td>0.05 (-12.18%)</td><td>0.04 <b>(-40.03%)</b></td><td>0.03 (-11.98%)</td><td>0.03 <b>(+32.78%)</b></td><td>552.40 (+13.62%)</td><td>398.10 <b>(+21.83%)</b></td><td>448.40 <b>(+66.75%)</b></td><td>203.70 (-11.40%)</td><td>157.77 <b>(+37.85%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>486.20 (n/a)</td><td>326.78 (n/a)</td><td>268.90 (n/a)</td><td>229.90 (n/a)</td><td>114.45 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.09 (+18.54%)</td><td>0.06 (+13.64%)</td><td>0.06 (+18.43%)</td><td>0.04 (+7.23%)</td><td>0.02 (+14.81%)</td><td>514.20 (-6.75%)</td><td>322.80 (-11.41%)</td><td>308.60 (-15.57%)</td><td>214.50 (-15.65%)</td><td>114.25 (-3.76%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>551.40 (n/a)</td><td>364.36 (n/a)</td><td>365.50 (n/a)</td><td>254.30 (n/a)</td><td>118.72 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (+4.52%)</td><td>0.05 <b>(+45.49%)</b></td><td>0.03 (+10.08%)</td><td>0.03 <b>(+234.05%)</b></td><td>0.02 <b>(-25.88%)</b></td><td>585.80 <b>(-70.06%)</b></td><td>453.48 <b>(-56.01%)</b></td><td>536.30 (-9.16%)</td><td>270.50 (-4.35%)</td><td>149.97 <b>(-81.44%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1956.90 (n/a)</td><td>1030.94 (n/a)</td><td>590.40 (n/a)</td><td>282.80 (n/a)</td><td>808.22 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (+6.10%)</td><td>0.06 <b>(+38.66%)</b></td><td>0.07 <b>(+61.70%)</b></td><td>0.04 <b>(+116.67%)</b></td><td>0.02 (-8.65%)</td><td>514.30 <b>(-53.85%)</b></td><td>337.42 <b>(-37.13%)</b></td><td>263.20 <b>(-38.14%)</b></td><td>255.10 (-5.76%)</td><td>115.75 <b>(-65.19%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1114.40 (n/a)</td><td>536.72 (n/a)</td><td>425.50 (n/a)</td><td>270.70 (n/a)</td><td>332.54 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.07 (+10.05%)</td><td>0.04 (+4.42%)</td><td>0.04 (-3.36%)</td><td>0.03 (-6.73%)</td><td>0.02 <b>(+31.94%)</b></td><td>611.40 (+7.21%)</td><td>448.66 (-0.66%)</td><td>500.30 (+3.47%)</td><td>263.90 (-9.13%)</td><td>138.33 <b>(+30.70%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>570.30 (n/a)</td><td>451.66 (n/a)</td><td>483.50 (n/a)</td><td>290.40 (n/a)</td><td>105.84 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.08 (-7.90%)</td><td>0.06 (+14.35%)</td><td>0.07 <b>(+61.90%)</b></td><td>0.03 (-12.55%)</td><td>0.02 (-7.11%)</td><td>572.70 (+14.36%)</td><td>353.56 (-11.79%)</td><td>281.00 <b>(-38.23%)</b></td><td>235.90 (+8.56%)</td><td>138.46 (+18.58%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>500.80 (n/a)</td><td>400.82 (n/a)</td><td>454.90 (n/a)</td><td>217.30 (n/a)</td><td>116.77 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.38 (+15.69%)</td><td>0.32 <b>(+20.83%)</b></td><td>0.32 <b>(+31.82%)</b></td><td>0.24 (+7.26%)</td><td>0.05 (+16.15%)</td><td>403.20 (-6.75%)</td><td>317.60 (-17.07%)</td><td>305.70 <b>(-24.13%)</b></td><td>261.30 (-13.53%)</td><td>52.06 (-3.96%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>432.40 (n/a)</td><td>382.98 (n/a)</td><td>402.90 (n/a)</td><td>302.20 (n/a)</td><td>54.21 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.35 (-12.65%)</td><td>0.22 <b>(-22.31%)</b></td><td>0.20 <b>(-27.46%)</b></td><td>0.18 (-0.66%)</td><td>0.07 <b>(-31.75%)</b></td><td>535.40 (+0.66%)</td><td>465.44 <b>(+22.16%)</b></td><td>498.60 <b>(+37.85%)</b></td><td>277.50 (+14.48%)</td><td>106.58 <b>(-23.97%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>531.90 (n/a)</td><td>381.00 (n/a)</td><td>361.70 (n/a)</td><td>242.40 (n/a)</td><td>140.19 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.40 (+2.29%)</td><td>0.28 (-1.16%)</td><td>0.29 (+16.17%)</td><td>0.19 (-11.48%)</td><td>0.09 (+8.31%)</td><td>529.00 (+12.99%)</td><td>382.82 (+3.19%)</td><td>336.40 (-13.92%)</td><td>248.20 (-2.24%)</td><td>122.76 <b>(+23.57%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>468.20 (n/a)</td><td>371.00 (n/a)</td><td>390.80 (n/a)</td><td>253.90 (n/a)</td><td>99.35 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.31 (+9.87%)</td><td>0.22 (+11.23%)</td><td>0.23 (+13.31%)</td><td>0.12 (-10.29%)</td><td>0.09 <b>(+42.31%)</b></td><td>614.10 (+11.45%)</td><td>390.92 (-3.66%)</td><td>316.90 (-11.75%)</td><td>238.10 (-8.98%)</td><td>170.25 <b>(+39.28%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>551.00 (n/a)</td><td>405.76 (n/a)</td><td>359.10 (n/a)</td><td>261.60 (n/a)</td><td>122.23 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.31 (+1.79%)</td><td>0.21 (+4.56%)</td><td>0.24 <b>(+25.46%)</b></td><td>0.12 (+0.37%)</td><td>0.07 (+1.65%)</td><td>597.90 (-0.37%)</td><td>379.74 (-3.92%)</td><td>313.70 <b>(-20.30%)</b></td><td>239.20 (-1.77%)</td><td>142.60 (+2.95%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>600.10 (n/a)</td><td>395.22 (n/a)</td><td>393.60 (n/a)</td><td>243.50 (n/a)</td><td>138.51 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.16 <b>(-43.51%)</b></td><td>0.14 <b>(-40.38%)</b></td><td>0.14 <b>(-42.83%)</b></td><td>0.11 <b>(-32.09%)</b></td><td>0.02 <b>(-60.80%)</b></td><td>682.50 <b>(+47.28%)</b></td><td>552.10 <b>(+61.91%)</b></td><td>512.90 <b>(+74.93%)</b></td><td>457.00 <b>(+76.99%)</b></td><td>98.79 (+2.73%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>463.40 (n/a)</td><td>341.00 (n/a)</td><td>293.20 (n/a)</td><td>258.20 (n/a)</td><td>96.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (-18.80%)</td><td>0.08 <b>(-35.57%)</b></td><td>0.07 <b>(-48.05%)</b></td><td>0.06 <b>(-26.57%)</b></td><td>0.03 <b>(-20.95%)</b></td><td>665.70 <b>(+36.19%)</b></td><td>502.28 <b>(+55.15%)</b></td><td>524.10 <b>(+92.47%)</b></td><td>305.00 <b>(+23.18%)</b></td><td>130.84 <b>(+27.73%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>488.80 (n/a)</td><td>323.74 (n/a)</td><td>272.30 (n/a)</td><td>247.60 (n/a)</td><td>102.43 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (-3.62%)</td><td>0.08 <b>(-23.46%)</b></td><td>0.07 <b>(-33.02%)</b></td><td>0.05 (-12.10%)</td><td>0.03 (+0.69%)</td><td>749.00 (+13.76%)</td><td>530.10 <b>(+33.45%)</b></td><td>499.10 <b>(+49.30%)</b></td><td>283.90 (+3.76%)</td><td>194.57 <b>(+22.58%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>658.40 (n/a)</td><td>397.22 (n/a)</td><td>334.30 (n/a)</td><td>273.60 (n/a)</td><td>158.73 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 <b>(+100.89%)</b></td><td>0.09 <b>(+43.92%)</b></td><td>0.08 (-1.36%)</td><td>0.05 <b>(+200.98%)</b></td><td>0.05 <b>(+74.91%)</b></td><td>818.70 <b>(-66.78%)</b></td><td>492.46 <b>(-44.21%)</b></td><td>474.80 (+1.37%)</td><td>210.60 <b>(-50.22%)</b></td><td>235.91 <b>(-73.39%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2464.20 (n/a)</td><td>882.70 (n/a)</td><td>468.40 (n/a)</td><td>423.10 (n/a)</td><td>886.71 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.11 <b>(-21.76%)</b></td><td>0.08 (-5.25%)</td><td>0.08 (-1.13%)</td><td>0.07 <b>(+21.19%)</b></td><td>0.01 <b>(-52.52%)</b></td><td>497.40 (-17.49%)</td><td>450.92 (-0.48%)</td><td>485.60 (+1.15%)</td><td>339.60 <b>(+27.81%)</b></td><td>65.74 <b>(-48.60%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>602.80 (n/a)</td><td>453.08 (n/a)</td><td>480.10 (n/a)</td><td>265.70 (n/a)</td><td>127.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (-9.29%)</td><td>0.09 (-11.22%)</td><td>0.09 (+9.18%)</td><td>0.06 (-10.99%)</td><td>0.03 <b>(-26.26%)</b></td><td>587.60 (+12.35%)</td><td>414.90 (+9.86%)</td><td>390.50 (-8.40%)</td><td>276.20 (+10.22%)</td><td>118.23 (-1.58%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>523.00 (n/a)</td><td>377.66 (n/a)</td><td>426.30 (n/a)</td><td>250.60 (n/a)</td><td>120.12 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.16 (+16.74%)</td><td>0.10 (+1.44%)</td><td>0.10 (-16.27%)</td><td>0.07 (+17.16%)</td><td>0.04 (+4.58%)</td><td>531.90 (-14.65%)</td><td>388.20 (-3.07%)</td><td>355.00 (+19.41%)</td><td>235.60 (-14.33%)</td><td>128.95 (-18.27%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>623.20 (n/a)</td><td>400.50 (n/a)</td><td>297.30 (n/a)</td><td>275.00 (n/a)</td><td>157.76 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.17 (+15.36%)</td><td>0.12 (+2.86%)</td><td>0.09 (-18.66%)</td><td>0.08 <b>(+33.19%)</b></td><td>0.04 <b>(+21.41%)</b></td><td>496.30 <b>(-24.92%)</b></td><td>393.50 (-2.51%)</td><td>476.40 <b>(+22.94%)</b></td><td>242.80 (-13.29%)</td><td>127.35 (-17.92%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>661.00 (n/a)</td><td>403.62 (n/a)</td><td>387.50 (n/a)</td><td>280.00 (n/a)</td><td>155.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (+11.07%)</td><td>0.11 <b>(+26.67%)</b></td><td>0.13 <b>(+57.63%)</b></td><td>0.08 (+19.61%)</td><td>0.03 <b>(+27.99%)</b></td><td>510.60 (-16.39%)</td><td>383.76 (-19.93%)</td><td>320.40 <b>(-36.55%)</b></td><td>291.40 (-9.95%)</td><td>107.00 (+1.75%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>610.70 (n/a)</td><td>479.30 (n/a)</td><td>505.00 (n/a)</td><td>323.60 (n/a)</td><td>105.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.15 (+5.90%)</td><td>0.09 (-4.86%)</td><td>0.09 (+8.22%)</td><td>0.07 (+1.40%)</td><td>0.03 (-10.97%)</td><td>621.50 (-1.38%)</td><td>465.60 (+2.50%)</td><td>461.10 (-7.60%)</td><td>277.00 (-5.56%)</td><td>127.21 (-15.63%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>630.20 (n/a)</td><td>454.24 (n/a)</td><td>499.00 (n/a)</td><td>293.30 (n/a)</td><td>150.78 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.16 (+5.39%)</td><td>0.11 (-5.98%)</td><td>0.10 (-5.25%)</td><td>0.05 <b>(-34.18%)</b></td><td>0.04 <b>(+22.43%)</b></td><td>820.40 <b>(+51.93%)</b></td><td>457.56 (+15.44%)</td><td>404.40 (+5.53%)</td><td>251.00 (-5.14%)</td><td>223.89 <b>(+78.67%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>540.00 (n/a)</td><td>396.36 (n/a)</td><td>383.20 (n/a)</td><td>264.60 (n/a)</td><td>125.31 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 (+7.87%)</td><td>0.11 (+9.92%)</td><td>0.08 (-15.22%)</td><td>0.07 <b>(+240.34%)</b></td><td>0.05 (-11.23%)</td><td>606.20 <b>(-70.62%)</b></td><td>451.20 <b>(-37.88%)</b></td><td>526.80 (+17.96%)</td><td>229.50 (-7.31%)</td><td>174.90 <b>(-76.90%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2063.00 (n/a)</td><td>726.32 (n/a)</td><td>446.60 (n/a)</td><td>247.60 (n/a)</td><td>757.25 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.19 (+16.98%)</td><td>0.11 <b>(+31.02%)</b></td><td>0.08 (+2.90%)</td><td>0.06 <b>(+249.62%)</b></td><td>0.05 (+3.62%)</td><td>700.80 <b>(-71.40%)</b></td><td>457.90 <b>(-46.96%)</b></td><td>482.80 (-2.82%)</td><td>218.30 (-14.53%)</td><td>197.95 <b>(-77.94%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2450.20 (n/a)</td><td>863.34 (n/a)</td><td>496.80 (n/a)</td><td>255.40 (n/a)</td><td>897.19 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (-5.59%)</td><td>0.11 (-11.02%)</td><td>0.13 (-1.49%)</td><td>0.01 <b>(-79.69%)</b></td><td>0.05 <b>(+69.59%)</b></td><td>2479.60 <b>(+392.28%)</b></td><td>707.98 <b>(+129.37%)</b></td><td>276.80 (+1.50%)</td><td>245.00 (+5.92%)</td><td>990.51 <b>(+791.49%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>503.70 (n/a)</td><td>308.66 (n/a)</td><td>272.70 (n/a)</td><td>231.30 (n/a)</td><td>111.11 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (+2.44%)</td><td>0.08 (-18.37%)</td><td>0.07 <b>(-40.50%)</b></td><td>0.03 (-17.41%)</td><td>0.04 (+14.87%)</td><td>1101.70 <b>(+21.08%)</b></td><td>537.88 <b>(+29.05%)</b></td><td>505.50 <b>(+68.05%)</b></td><td>266.70 (-2.38%)</td><td>338.05 <b>(+22.52%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>909.90 (n/a)</td><td>416.80 (n/a)</td><td>300.80 (n/a)</td><td>273.20 (n/a)</td><td>275.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (-0.67%)</td><td>0.09 (-1.17%)</td><td>0.08 (-7.91%)</td><td>0.06 (-5.65%)</td><td>0.03 (-5.10%)</td><td>605.30 (+5.99%)</td><td>427.14 (+0.33%)</td><td>434.30 (+8.60%)</td><td>292.80 (+0.69%)</td><td>132.12 (-4.71%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>571.10 (n/a)</td><td>425.72 (n/a)</td><td>399.90 (n/a)</td><td>290.80 (n/a)</td><td>138.65 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (-4.15%)</td><td>0.09 <b>(+30.43%)</b></td><td>0.07 (+16.77%)</td><td>0.06 <b>(+317.82%)</b></td><td>0.03 <b>(-27.31%)</b></td><td>580.80 <b>(-76.07%)</b></td><td>423.76 <b>(-50.67%)</b></td><td>474.50 (-14.37%)</td><td>277.30 (+4.33%)</td><td>134.16 <b>(-84.86%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2426.80 (n/a)</td><td>859.04 (n/a)</td><td>554.10 (n/a)</td><td>265.80 (n/a)</td><td>886.09 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (-10.67%)</td><td>0.08 <b>(-20.47%)</b></td><td>0.07 <b>(-20.67%)</b></td><td>0.06 (+4.13%)</td><td>0.03 <b>(-24.12%)</b></td><td>619.00 (-3.97%)</td><td>504.68 (+19.06%)</td><td>532.40 <b>(+26.04%)</b></td><td>268.10 (+11.94%)</td><td>137.02 <b>(-21.17%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>644.60 (n/a)</td><td>423.90 (n/a)</td><td>422.40 (n/a)</td><td>239.50 (n/a)</td><td>173.82 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.14 (-2.41%)</td><td>0.08 <b>(-22.91%)</b></td><td>0.07 <b>(-37.31%)</b></td><td>0.06 (-1.50%)</td><td>0.03 (-2.97%)</td><td>605.20 (+1.53%)</td><td>466.30 <b>(+28.44%)</b></td><td>475.10 <b>(+59.54%)</b></td><td>256.10 (+2.48%)</td><td>129.14 (-8.22%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>596.10 (n/a)</td><td>363.04 (n/a)</td><td>297.80 (n/a)</td><td>249.90 (n/a)</td><td>140.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.27 <b>(-30.83%)</b></td><td>0.23 (+5.26%)</td><td>0.23 (+9.95%)</td><td>0.20 <b>(+187.42%)</b></td><td>0.03 <b>(-84.00%)</b></td><td>666.20 <b>(-65.21%)</b></td><td>564.08 <b>(-45.00%)</b></td><td>557.80 (-9.05%)</td><td>494.00 <b>(+44.57%)</b></td><td>63.91 <b>(-92.19%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.38 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1914.90 (n/a)</td><td>1025.58 (n/a)</td><td>613.30 (n/a)</td><td>341.70 (n/a)</td><td>818.57 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.45 (+5.45%)</td><td>0.29 (-14.05%)</td><td>0.22 <b>(-41.01%)</b></td><td>0.21 (-9.69%)</td><td>0.11 <b>(+32.47%)</b></td><td>633.20 (+10.74%)</td><td>493.42 <b>(+22.02%)</b></td><td>595.90 <b>(+69.53%)</b></td><td>294.10 (-5.16%)</td><td>160.81 <b>(+43.37%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.37 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>571.80 (n/a)</td><td>404.36 (n/a)</td><td>351.50 (n/a)</td><td>310.10 (n/a)</td><td>112.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.41 (-17.67%)</td><td>0.26 (-7.22%)</td><td>0.24 (-2.85%)</td><td>0.20 (+9.09%)</td><td>0.09 <b>(-30.87%)</b></td><td>640.70 (-8.33%)</td><td>528.92 (+3.01%)</td><td>557.70 (+2.93%)</td><td>316.70 <b>(+21.48%)</b></td><td>128.99 (-18.63%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.50 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>698.90 (n/a)</td><td>513.46 (n/a)</td><td>541.80 (n/a)</td><td>260.70 (n/a)</td><td>158.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.00 (+16.67%)</td><td>0.00 (+17.65%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+54.64%)</b></td><td>21941.42 <b>(+28.54%)</b></td><td>13493.07 (+7.18%)</td><td>14319.57 (+8.19%)</td><td>5773.77 (-12.67%)</td><td>6970.08 <b>(+83.18%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17069.48 (n/a)</td><td>12588.78 (n/a)</td><td>13235.10 (n/a)</td><td>6611.28 (n/a)</td><td>3805.07 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.00 (-9.09%)</td><td>0.00 (+6.45%)</td><td>0.00 (+20.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-21.05%)</b></td><td>19144.65 (+0.52%)</td><td>13224.53 (-9.90%)</td><td>13027.28 (-16.04%)</td><td>7901.79 (+7.69%)</td><td>4032.70 (-12.64%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19046.52 (n/a)</td><td>14677.32 (n/a)</td><td>15515.79 (n/a)</td><td>7337.44 (n/a)</td><td>4616.10 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.12 (-11.71%)</td><td>0.10 (-12.25%)</td><td>0.09 (-13.07%)</td><td>0.08 (-6.24%)</td><td>0.02 <b>(-27.04%)</b></td><td>26321.51 (+6.69%)</td><td>22505.83 (+12.46%)</td><td>24086.19 (+15.03%)</td><td>16966.30 (+13.25%)</td><td>3628.00 (-12.69%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>24671.75 (n/a)</td><td>20011.77 (n/a)</td><td>20939.26 (n/a)</td><td>14980.77 (n/a)</td><td>4155.24 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>2.64 (+18.00%)</td><td>1.73 <b>(+29.08%)</b></td><td>1.53 (+15.78%)</td><td>1.09 <b>(+263.85%)</b></td><td>0.60 (-16.40%)</td><td>965.70 <b>(-72.52%)</b></td><td>662.98 <b>(-47.40%)</b></td><td>686.30 (-13.63%)</td><td>397.20 (-15.25%)</td><td>214.63 <b>(-83.11%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>2.24 (n/a)</td><td>1.34 (n/a)</td><td>1.32 (n/a)</td><td>0.30 (n/a)</td><td>0.71 (n/a)</td><td>3513.70 (n/a)</td><td>1260.52 (n/a)</td><td>794.60 (n/a)</td><td>468.70 (n/a)</td><td>1270.44 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.37 <b>(+51.14%)</b></td><td>1.80 (+10.38%)</td><td>1.85 (+5.26%)</td><td>0.29 <b>(-72.44%)</b></td><td>1.18 <b>(+129.40%)</b></td><td>3555.10 <b>(+262.84%)</b></td><td>1168.82 <b>(+66.20%)</b></td><td>566.70 (-5.00%)</td><td>311.60 <b>(-33.83%)</b></td><td>1357.08 <b>(+470.27%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>2.23 (n/a)</td><td>1.63 (n/a)</td><td>1.76 (n/a)</td><td>1.07 (n/a)</td><td>0.52 (n/a)</td><td>979.80 (n/a)</td><td>703.26 (n/a)</td><td>596.50 (n/a)</td><td>470.90 (n/a)</td><td>237.97 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.45 (-5.02%)</td><td>2.29 (-6.67%)</td><td>2.12 (-10.98%)</td><td>1.50 <b>(+32.06%)</b></td><td>0.75 (-18.33%)</td><td>701.00 <b>(-24.27%)</b></td><td>496.56 (-0.30%)</td><td>495.40 (+12.34%)</td><td>303.80 (+5.27%)</td><td>150.44 <b>(-39.69%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.63 (n/a)</td><td>2.45 (n/a)</td><td>2.38 (n/a)</td><td>1.13 (n/a)</td><td>0.92 (n/a)</td><td>925.70 (n/a)</td><td>498.06 (n/a)</td><td>441.00 (n/a)</td><td>288.60 (n/a)</td><td>249.46 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>2.93 (+5.94%)</td><td>2.24 <b>(+43.19%)</b></td><td>2.13 <b>(+22.47%)</b></td><td>1.77 <b>(+225.31%)</b></td><td>0.46 <b>(-53.33%)</b></td><td>592.90 <b>(-69.26%)</b></td><td>484.58 <b>(-54.28%)</b></td><td>491.40 (-18.36%)</td><td>358.40 (-5.61%)</td><td>94.01 <b>(-88.11%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>2.76 (n/a)</td><td>1.56 (n/a)</td><td>1.74 (n/a)</td><td>0.54 (n/a)</td><td>0.99 (n/a)</td><td>1928.90 (n/a)</td><td>1059.92 (n/a)</td><td>601.90 (n/a)</td><td>379.70 (n/a)</td><td>790.65 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.59 (+1.77%)</td><td>2.56 <b>(+44.72%)</b></td><td>3.21 <b>(+72.20%)</b></td><td>0.58 (-4.61%)</td><td>1.28 (+10.82%)</td><td>3599.60 (+4.83%)</td><td>1301.36 <b>(-24.94%)</b></td><td>652.90 <b>(-41.93%)</b></td><td>584.60 (-1.75%)</td><td>1299.66 (+10.10%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.52 (n/a)</td><td>1.77 (n/a)</td><td>1.87 (n/a)</td><td>0.61 (n/a)</td><td>1.15 (n/a)</td><td>3433.80 (n/a)</td><td>1733.74 (n/a)</td><td>1124.30 (n/a)</td><td>595.00 (n/a)</td><td>1180.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>4.01 <b>(-20.63%)</b></td><td>2.60 <b>(-34.61%)</b></td><td>2.78 <b>(-28.88%)</b></td><td>1.01 <b>(-62.97%)</b></td><td>1.24 <b>(+39.28%)</b></td><td>2077.70 <b>(+170.08%)</b></td><td>1038.28 <b>(+88.01%)</b></td><td>755.40 <b>(+40.59%)</b></td><td>522.60 <b>(+25.99%)</b></td><td>643.16 <b>(+369.77%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.06 (n/a)</td><td>3.97 (n/a)</td><td>3.90 (n/a)</td><td>2.73 (n/a)</td><td>0.89 (n/a)</td><td>769.30 (n/a)</td><td>552.24 (n/a)</td><td>537.30 (n/a)</td><td>414.80 (n/a)</td><td>136.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>4.87 (-11.83%)</td><td>3.28 (+13.63%)</td><td>2.77 (+13.48%)</td><td>1.99 <b>(+100.47%)</b></td><td>1.19 <b>(-31.84%)</b></td><td>1052.50 <b>(-50.12%)</b></td><td>708.88 <b>(-29.61%)</b></td><td>758.40 (-11.88%)</td><td>430.90 (+13.42%)</td><td>249.06 <b>(-63.06%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.52 (n/a)</td><td>2.89 (n/a)</td><td>2.44 (n/a)</td><td>0.99 (n/a)</td><td>1.74 (n/a)</td><td>2110.00 (n/a)</td><td>1007.04 (n/a)</td><td>860.60 (n/a)</td><td>379.90 (n/a)</td><td>674.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.58 (-7.62%)</td><td>2.70 (-1.62%)</td><td>3.05 (+10.46%)</td><td>1.21 <b>(+103.27%)</b></td><td>0.99 <b>(-25.86%)</b></td><td>1733.10 <b>(-50.80%)</b></td><td>913.36 <b>(-25.94%)</b></td><td>687.70 (-9.48%)</td><td>585.60 (+8.24%)</td><td>481.27 <b>(-62.56%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.88 (n/a)</td><td>2.74 (n/a)</td><td>2.76 (n/a)</td><td>0.60 (n/a)</td><td>1.34 (n/a)</td><td>3522.80 (n/a)</td><td>1233.30 (n/a)</td><td>759.70 (n/a)</td><td>541.00 (n/a)</td><td>1285.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>5.82 (-15.35%)</td><td>3.92 <b>(+31.02%)</b></td><td>3.35 <b>(+45.37%)</b></td><td>2.97 <b>(+175.15%)</b></td><td>1.17 <b>(-47.96%)</b></td><td>706.00 <b>(-63.66%)</b></td><td>568.54 <b>(-42.77%)</b></td><td>625.10 <b>(-31.21%)</b></td><td>360.20 (+18.14%)</td><td>140.23 <b>(-76.41%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>6.88 (n/a)</td><td>2.99 (n/a)</td><td>2.31 (n/a)</td><td>1.08 (n/a)</td><td>2.25 (n/a)</td><td>1942.60 (n/a)</td><td>993.50 (n/a)</td><td>908.70 (n/a)</td><td>304.90 (n/a)</td><td>594.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>6.05 (+4.11%)</td><td>3.93 (+10.14%)</td><td>4.11 <b>(+24.05%)</b></td><td>2.52 <b>(+21.01%)</b></td><td>1.41 (+1.31%)</td><td>832.30 (-17.36%)</td><td>589.68 (-10.27%)</td><td>510.70 (-19.38%)</td><td>346.40 (-3.96%)</td><td>201.63 (-14.90%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.81 (n/a)</td><td>3.57 (n/a)</td><td>3.31 (n/a)</td><td>2.08 (n/a)</td><td>1.40 (n/a)</td><td>1007.20 (n/a)</td><td>657.18 (n/a)</td><td>633.50 (n/a)</td><td>360.70 (n/a)</td><td>236.94 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>5.11 (-7.89%)</td><td>3.91 (+10.16%)</td><td>4.10 (+6.03%)</td><td>2.02 <b>(+70.57%)</b></td><td>1.15 <b>(-39.19%)</b></td><td>2080.30 <b>(-41.37%)</b></td><td>1188.68 <b>(-27.84%)</b></td><td>1022.40 (-5.68%)</td><td>821.00 (+8.55%)</td><td>506.31 <b>(-56.97%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.55 (n/a)</td><td>3.55 (n/a)</td><td>3.87 (n/a)</td><td>1.18 (n/a)</td><td>1.88 (n/a)</td><td>3548.30 (n/a)</td><td>1647.30 (n/a)</td><td>1084.00 (n/a)</td><td>756.30 (n/a)</td><td>1176.64 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>8.48 (+7.11%)</td><td>5.36 (+7.22%)</td><td>5.81 <b>(+50.09%)</b></td><td>1.07 <b>(-38.37%)</b></td><td>2.97 (+9.77%)</td><td>3937.50 <b>(+62.25%)</b></td><td>1356.42 (+19.16%)</td><td>722.00 <b>(-33.37%)</b></td><td>494.70 (-6.63%)</td><td>1460.27 <b>(+89.00%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>7.92 (n/a)</td><td>5.00 (n/a)</td><td>3.87 (n/a)</td><td>1.73 (n/a)</td><td>2.71 (n/a)</td><td>2426.80 (n/a)</td><td>1138.28 (n/a)</td><td>1083.60 (n/a)</td><td>529.80 (n/a)</td><td>772.62 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>7.66 (+11.36%)</td><td>4.10 (-5.02%)</td><td>3.63 (-9.49%)</td><td>1.18 (+2.89%)</td><td>2.69 <b>(+21.04%)</b></td><td>3544.20 (-2.81%)</td><td>1591.78 (+11.11%)</td><td>1155.40 (+10.48%)</td><td>547.50 (-10.20%)</td><td>1229.89 (-2.24%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>6.88 (n/a)</td><td>4.32 (n/a)</td><td>4.01 (n/a)</td><td>1.15 (n/a)</td><td>2.22 (n/a)</td><td>3646.60 (n/a)</td><td>1432.66 (n/a)</td><td>1045.80 (n/a)</td><td>609.70 (n/a)</td><td>1258.03 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>9.40 (-6.07%)</td><td>5.98 (-4.73%)</td><td>6.66 (-9.53%)</td><td>1.09 (-4.99%)</td><td>3.21 (-15.92%)</td><td>3830.60 (+5.25%)</td><td>1260.68 (+0.68%)</td><td>629.80 (+10.53%)</td><td>446.10 (+6.47%)</td><td>1445.27 (+5.49%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>10.01 (n/a)</td><td>6.28 (n/a)</td><td>7.36 (n/a)</td><td>1.15 (n/a)</td><td>3.81 (n/a)</td><td>3639.60 (n/a)</td><td>1252.14 (n/a)</td><td>569.80 (n/a)</td><td>419.00 (n/a)</td><td>1370.09 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>9.62 (+1.30%)</td><td>6.19 (-9.08%)</td><td>5.63 <b>(-32.00%)</b></td><td>4.56 <b>(+21.05%)</b></td><td>2.02 <b>(-24.82%)</b></td><td>920.00 (-17.39%)</td><td>725.70 (+0.94%)</td><td>745.60 <b>(+47.06%)</b></td><td>435.90 (-1.29%)</td><td>187.29 <b>(-42.71%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>9.50 (n/a)</td><td>6.81 (n/a)</td><td>8.27 (n/a)</td><td>3.77 (n/a)</td><td>2.69 (n/a)</td><td>1113.60 (n/a)</td><td>718.96 (n/a)</td><td>507.00 (n/a)</td><td>441.60 (n/a)</td><td>326.90 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>7.95 (-17.15%)</td><td>6.43 (+11.04%)</td><td>6.96 (+2.65%)</td><td>4.03 <b>(+136.47%)</b></td><td>1.71 <b>(-50.12%)</b></td><td>1040.10 <b>(-57.71%)</b></td><td>698.64 <b>(-37.32%)</b></td><td>602.50 (-2.57%)</td><td>527.40 <b>(+20.69%)</b></td><td>218.65 <b>(-74.98%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>9.60 (n/a)</td><td>5.79 (n/a)</td><td>6.78 (n/a)</td><td>1.71 (n/a)</td><td>3.43 (n/a)</td><td>2459.60 (n/a)</td><td>1114.70 (n/a)</td><td>618.40 (n/a)</td><td>437.00 (n/a)</td><td>874.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>1.65 (+6.10%)</td><td>1.05 (+4.79%)</td><td>0.95 (-2.91%)</td><td>0.16 <b>(-66.68%)</b></td><td>0.61 <b>(+25.84%)</b></td><td>3290.30 <b>(+200.16%)</b></td><td>1012.80 <b>(+56.71%)</b></td><td>550.20 (+3.00%)</td><td>316.80 (-5.74%)</td><td>1278.88 <b>(+281.03%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>1.56 (n/a)</td><td>1.01 (n/a)</td><td>0.98 (n/a)</td><td>0.48 (n/a)</td><td>0.48 (n/a)</td><td>1096.20 (n/a)</td><td>646.28 (n/a)</td><td>534.20 (n/a)</td><td>336.10 (n/a)</td><td>335.64 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>2.76 (+17.72%)</td><td>1.53 (-0.97%)</td><td>1.89 <b>(+22.68%)</b></td><td>0.29 (-2.04%)</td><td>1.16 <b>(+45.57%)</b></td><td>3560.10 (+2.08%)</td><td>1648.58 <b>(+40.85%)</b></td><td>555.60 (-18.49%)</td><td>379.50 (-15.06%)</td><td>1633.30 <b>(+25.53%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>2.35 (n/a)</td><td>1.54 (n/a)</td><td>1.54 (n/a)</td><td>0.30 (n/a)</td><td>0.80 (n/a)</td><td>3487.60 (n/a)</td><td>1170.44 (n/a)</td><td>681.60 (n/a)</td><td>446.80 (n/a)</td><td>1301.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>3.68 (-5.34%)</td><td>1.58 (-14.69%)</td><td>0.63 <b>(-65.27%)</b></td><td>0.58 (-3.77%)</td><td>1.41 (+2.96%)</td><td>3630.20 (+3.92%)</td><td>2368.52 <b>(+24.72%)</b></td><td>3325.70 <b>(+187.91%)</b></td><td>569.70 (+5.64%)</td><td>1509.97 (+5.35%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.89 (n/a)</td><td>1.85 (n/a)</td><td>1.82 (n/a)</td><td>0.60 (n/a)</td><td>1.37 (n/a)</td><td>3493.30 (n/a)</td><td>1899.02 (n/a)</td><td>1155.10 (n/a)</td><td>539.30 (n/a)</td><td>1433.33 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>2.29 <b>(+30.35%)</b></td><td>1.41 <b>(+38.73%)</b></td><td>1.50 <b>(+64.37%)</b></td><td>0.71 <b>(+156.75%)</b></td><td>0.68 (+11.85%)</td><td>735.80 <b>(-61.05%)</b></td><td>461.48 <b>(-41.44%)</b></td><td>349.40 <b>(-39.17%)</b></td><td>228.80 <b>(-23.27%)</b></td><td>238.70 <b>(-63.29%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>1.76 (n/a)</td><td>1.02 (n/a)</td><td>0.91 (n/a)</td><td>0.28 (n/a)</td><td>0.61 (n/a)</td><td>1889.20 (n/a)</td><td>788.00 (n/a)</td><td>574.40 (n/a)</td><td>298.20 (n/a)</td><td>650.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 (-11.61%)</td><td>0.09 (+1.22%)</td><td>0.08 <b>(-21.36%)</b></td><td>0.06 <b>(+252.12%)</b></td><td>0.03 <b>(-39.68%)</b></td><td>546.80 <b>(-71.60%)</b></td><td>400.26 <b>(-38.84%)</b></td><td>402.00 <b>(+27.17%)</b></td><td>255.50 (+13.15%)</td><td>126.40 <b>(-82.40%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1925.40 (n/a)</td><td>654.50 (n/a)</td><td>316.10 (n/a)</td><td>225.80 (n/a)</td><td>718.13 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.13 <b>(+29.37%)</b></td><td>0.10 <b>(+46.40%)</b></td><td>0.11 <b>(+67.77%)</b></td><td>0.05 <b>(+100.49%)</b></td><td>0.03 <b>(+27.54%)</b></td><td>604.60 <b>(-50.13%)</b></td><td>385.82 <b>(-36.22%)</b></td><td>297.90 <b>(-40.38%)</b></td><td>251.60 <b>(-22.70%)</b></td><td>155.85 <b>(-55.22%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1212.30 (n/a)</td><td>604.96 (n/a)</td><td>499.70 (n/a)</td><td>325.50 (n/a)</td><td>348.01 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.21 <b>(+26.15%)</b></td><td>0.12 (-10.70%)</td><td>0.10 <b>(-20.37%)</b></td><td>0.03 <b>(-70.63%)</b></td><td>0.07 <b>(+172.02%)</b></td><td>2060.30 <b>(+240.55%)</b></td><td>820.34 <b>(+61.94%)</b></td><td>625.70 <b>(+25.59%)</b></td><td>308.40 <b>(-20.72%)</b></td><td>706.52 <b>(+702.98%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>605.00 (n/a)</td><td>506.56 (n/a)</td><td>498.20 (n/a)</td><td>389.00 (n/a)</td><td>87.99 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.18 <b>(-29.15%)</b></td><td>0.14 (-5.90%)</td><td>0.13 (+12.18%)</td><td>0.11 <b>(+216.40%)</b></td><td>0.03 <b>(-69.31%)</b></td><td>617.40 <b>(-68.40%)</b></td><td>475.74 <b>(-34.61%)</b></td><td>497.00 (-10.87%)</td><td>368.90 <b>(+41.12%)</b></td><td>98.85 <b>(-85.94%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.09 (n/a)</td><td>1953.50 (n/a)</td><td>727.58 (n/a)</td><td>557.60 (n/a)</td><td>261.40 (n/a)</td><td>703.26 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.35 <b>(+51.32%)</b></td><td>0.20 (+9.80%)</td><td>0.17 (+0.12%)</td><td>0.13 (-8.14%)</td><td>0.09 <b>(+105.84%)</b></td><td>508.60 (+8.86%)</td><td>370.50 (-1.40%)</td><td>377.40 (-0.11%)</td><td>188.80 <b>(-33.92%)</b></td><td>127.16 <b>(+47.05%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>467.20 (n/a)</td><td>375.76 (n/a)</td><td>377.80 (n/a)</td><td>285.70 (n/a)</td><td>86.48 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.55 (-11.33%)</td><td>0.38 (-0.72%)</td><td>0.44 <b>(+52.83%)</b></td><td>0.24 (+2.18%)</td><td>0.13 <b>(-24.72%)</b></td><td>545.40 (-2.14%)</td><td>376.48 (-3.76%)</td><td>300.90 <b>(-34.57%)</b></td><td>239.80 (+12.79%)</td><td>134.89 (-10.81%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.62 (n/a)</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>557.30 (n/a)</td><td>391.18 (n/a)</td><td>459.90 (n/a)</td><td>212.60 (n/a)</td><td>151.24 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.58 (+11.56%)</td><td>0.37 (+14.32%)</td><td>0.39 <b>(+39.67%)</b></td><td>0.21 <b>(+114.19%)</b></td><td>0.15 (-18.10%)</td><td>625.70 <b>(-53.31%)</b></td><td>400.20 <b>(-30.29%)</b></td><td>339.70 <b>(-28.39%)</b></td><td>227.00 (-10.35%)</td><td>161.27 <b>(-63.86%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.52 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>0.18 (n/a)</td><td>1340.20 (n/a)</td><td>574.12 (n/a)</td><td>474.40 (n/a)</td><td>253.20 (n/a)</td><td>446.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.50 (+5.29%)</td><td>0.30 (+1.43%)</td><td>0.28 (+4.63%)</td><td>0.21 (-1.84%)</td><td>0.11 (+9.73%)</td><td>625.90 (+1.87%)</td><td>467.18 (-0.47%)</td><td>476.00 (-4.42%)</td><td>264.30 (-5.03%)</td><td>132.00 (+3.97%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.47 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>614.40 (n/a)</td><td>469.38 (n/a)</td><td>498.00 (n/a)</td><td>278.30 (n/a)</td><td>126.96 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:35</td><td>0.06 (-15.10%)</td><td>0.04 (+7.15%)</td><td>0.03 <b>(+29.29%)</b></td><td>0.03 (+8.13%)</td><td>0.01 <b>(-30.30%)</b></td><td>642.40 (-7.52%)</td><td>480.14 (-11.92%)</td><td>483.70 <b>(-22.66%)</b></td><td>296.70 (+17.78%)</td><td>141.78 (-19.47%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>694.60 (n/a)</td><td>545.12 (n/a)</td><td>625.40 (n/a)</td><td>251.90 (n/a)</td><td>176.06 (n/a)</td>
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
