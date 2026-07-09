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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 <b>(-21.74%)</b></td><td>0.02 (-19.82%)</td><td>0.02 (-17.46%)</td><td>0.01 (+1.29%)</td><td>0.00 <b>(-28.60%)</b></td><td>520.90 (-1.29%)</td><td>359.46 (+19.79%)</td><td>300.90 <b>(+21.14%)</b></td><td>264.50 <b>(+27.78%)</b></td><td>108.39 (-16.30%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>527.70 (n/a)</td><td>300.08 (n/a)</td><td>248.40 (n/a)</td><td>207.00 (n/a)</td><td>129.50 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (-17.20%)</td><td>0.01 <b>(-21.51%)</b></td><td>0.01 <b>(-35.92%)</b></td><td>0.00 <b>(-70.64%)</b></td><td>0.01 (+14.72%)</td><td>1937.90 <b>(+240.52%)</b></td><td>695.60 <b>(+81.23%)</b></td><td>463.90 <b>(+56.09%)</b></td><td>299.20 <b>(+20.74%)</b></td><td>699.52 <b>(+375.25%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.10 (n/a)</td><td>383.82 (n/a)</td><td>297.20 (n/a)</td><td>247.80 (n/a)</td><td>147.19 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (-7.51%)</td><td>0.01 <b>(-29.27%)</b></td><td>0.01 <b>(-22.63%)</b></td><td>0.01 <b>(-60.11%)</b></td><td>0.01 (+14.96%)</td><td>1109.50 <b>(+150.68%)</b></td><td>552.94 <b>(+65.84%)</b></td><td>472.40 <b>(+29.25%)</b></td><td>236.00 (+8.11%)</td><td>327.69 <b>(+230.75%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>442.60 (n/a)</td><td>333.42 (n/a)</td><td>365.50 (n/a)</td><td>218.30 (n/a)</td><td>99.08 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (+3.26%)</td><td>0.02 (-4.59%)</td><td>0.01 (-14.05%)</td><td>0.01 (-17.23%)</td><td>0.01 <b>(+40.44%)</b></td><td>614.10 <b>(+20.81%)</b></td><td>432.68 (+13.41%)</td><td>466.50 (+16.33%)</td><td>238.90 (-3.16%)</td><td>168.07 <b>(+66.17%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>508.30 (n/a)</td><td>381.52 (n/a)</td><td>401.00 (n/a)</td><td>246.70 (n/a)</td><td>101.15 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (+0.96%)</td><td>0.01 (-15.79%)</td><td>0.01 (-15.16%)</td><td>0.01 (-9.97%)</td><td>0.00 (+9.59%)</td><td>643.30 (+11.07%)</td><td>483.68 <b>(+21.56%)</b></td><td>478.40 (+17.86%)</td><td>294.00 (-0.94%)</td><td>147.78 <b>(+28.19%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.20 (n/a)</td><td>397.88 (n/a)</td><td>405.90 (n/a)</td><td>296.80 (n/a)</td><td>115.28 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (-10.62%)</td><td>0.02 (-13.91%)</td><td>0.02 (-2.21%)</td><td>0.01 (-1.33%)</td><td>0.01 (-3.22%)</td><td>625.90 (+1.34%)</td><td>393.52 (+16.97%)</td><td>280.70 (+2.26%)</td><td>251.80 (+11.86%)</td><td>172.86 (+6.47%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.60 (n/a)</td><td>336.44 (n/a)</td><td>274.50 (n/a)</td><td>225.10 (n/a)</td><td>162.35 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (+4.03%)</td><td>0.04 (-4.15%)</td><td>0.05 (+0.56%)</td><td>0.02 (-15.87%)</td><td>0.01 <b>(+29.30%)</b></td><td>510.20 (+18.84%)</td><td>305.70 (+9.02%)</td><td>241.10 (-0.58%)</td><td>219.30 (-3.90%)</td><td>122.07 <b>(+44.15%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>429.30 (n/a)</td><td>280.42 (n/a)</td><td>242.50 (n/a)</td><td>228.20 (n/a)</td><td>84.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (+11.91%)</td><td>0.04 (+9.93%)</td><td>0.05 (+8.81%)</td><td>0.03 <b>(+30.22%)</b></td><td>0.01 (+18.21%)</td><td>474.10 <b>(-23.21%)</b></td><td>337.20 (-9.03%)</td><td>266.30 (-8.11%)</td><td>233.80 (-10.66%)</td><td>122.91 (-16.83%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>617.40 (n/a)</td><td>370.66 (n/a)</td><td>289.80 (n/a)</td><td>261.70 (n/a)</td><td>147.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (-5.90%)</td><td>0.03 <b>(-21.36%)</b></td><td>0.03 <b>(-39.69%)</b></td><td>0.02 (-10.77%)</td><td>0.01 (-3.70%)</td><td>613.10 (+12.06%)</td><td>451.08 <b>(+27.86%)</b></td><td>464.30 <b>(+65.82%)</b></td><td>233.50 (+6.28%)</td><td>152.54 (+10.71%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>547.10 (n/a)</td><td>352.80 (n/a)</td><td>280.00 (n/a)</td><td>219.70 (n/a)</td><td>137.78 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (-11.70%)</td><td>0.04 (+11.83%)</td><td>0.04 <b>(+20.78%)</b></td><td>0.02 (+14.28%)</td><td>0.01 <b>(-22.81%)</b></td><td>522.60 (-12.49%)</td><td>346.52 (-16.36%)</td><td>315.40 (-17.20%)</td><td>243.00 (+13.29%)</td><td>118.42 <b>(-30.84%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>597.20 (n/a)</td><td>414.28 (n/a)</td><td>380.90 (n/a)</td><td>214.50 (n/a)</td><td>171.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (-9.15%)</td><td>0.03 (-8.64%)</td><td>0.02 <b>(-33.60%)</b></td><td>0.02 (-8.47%)</td><td>0.01 (+11.96%)</td><td>600.20 (+9.27%)</td><td>461.58 (+14.60%)</td><td>569.40 <b>(+50.60%)</b></td><td>261.50 (+10.11%)</td><td>174.51 <b>(+31.15%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>549.30 (n/a)</td><td>402.78 (n/a)</td><td>378.10 (n/a)</td><td>237.50 (n/a)</td><td>133.06 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 <b>(+42.78%)</b></td><td>0.03 <b>(+26.42%)</b></td><td>0.03 (-2.64%)</td><td>0.03 <b>(+309.15%)</b></td><td>0.01 (-7.99%)</td><td>474.10 <b>(-75.56%)</b></td><td>397.94 <b>(-43.87%)</b></td><td>457.30 (+2.72%)</td><td>240.40 <b>(-29.95%)</b></td><td>99.50 <b>(-85.57%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1940.00 (n/a)</td><td>709.00 (n/a)</td><td>445.20 (n/a)</td><td>343.20 (n/a)</td><td>689.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (+0.14%)</td><td>0.09 (+11.57%)</td><td>0.08 (-3.90%)</td><td>0.08 <b>(+46.80%)</b></td><td>0.01 <b>(-58.95%)</b></td><td>320.40 <b>(-31.89%)</b></td><td>288.92 (-15.67%)</td><td>299.00 (+4.04%)</td><td>249.90 (-0.12%)</td><td>28.22 <b>(-72.74%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>470.40 (n/a)</td><td>342.60 (n/a)</td><td>287.40 (n/a)</td><td>250.20 (n/a)</td><td>103.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (-2.56%)</td><td>0.08 (-15.23%)</td><td>0.09 (-2.52%)</td><td>0.04 <b>(-44.60%)</b></td><td>0.03 <b>(+114.71%)</b></td><td>591.20 <b>(+80.52%)</b></td><td>367.90 <b>(+32.10%)</b></td><td>274.40 (+2.58%)</td><td>246.90 (+2.62%)</td><td>157.22 <b>(+286.16%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>327.50 (n/a)</td><td>278.50 (n/a)</td><td>267.50 (n/a)</td><td>240.60 (n/a)</td><td>40.71 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 <b>(-20.19%)</b></td><td>0.07 (-2.97%)</td><td>0.08 <b>(+56.21%)</b></td><td>0.04 (-8.61%)</td><td>0.03 <b>(-32.47%)</b></td><td>611.40 (+9.43%)</td><td>386.34 (-3.54%)</td><td>317.90 <b>(-35.98%)</b></td><td>245.40 <b>(+25.33%)</b></td><td>154.40 (-7.86%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>558.70 (n/a)</td><td>400.52 (n/a)</td><td>496.60 (n/a)</td><td>195.80 (n/a)</td><td>167.57 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (-18.36%)</td><td>0.07 (-14.46%)</td><td>0.08 <b>(-20.08%)</b></td><td>0.04 (-13.66%)</td><td>0.03 <b>(-23.30%)</b></td><td>603.10 (+15.82%)</td><td>383.94 (+13.32%)</td><td>305.40 <b>(+25.11%)</b></td><td>243.70 <b>(+22.52%)</b></td><td>157.55 (+2.93%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>520.70 (n/a)</td><td>338.82 (n/a)</td><td>244.10 (n/a)</td><td>198.90 (n/a)</td><td>153.07 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.12 (+15.52%)</td><td>0.07 (-13.88%)</td><td>0.04 <b>(-47.86%)</b></td><td>0.04 (-8.18%)</td><td>0.04 <b>(+73.75%)</b></td><td>617.40 (+8.91%)</td><td>447.50 <b>(+32.34%)</b></td><td>565.80 <b>(+91.80%)</b></td><td>213.40 (-13.43%)</td><td>201.18 <b>(+55.14%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>566.90 (n/a)</td><td>338.14 (n/a)</td><td>295.00 (n/a)</td><td>246.50 (n/a)</td><td>129.67 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (+18.64%)</td><td>0.07 (-4.36%)</td><td>0.07 (-5.26%)</td><td>0.04 (-11.81%)</td><td>0.03 <b>(+64.15%)</b></td><td>640.20 (+13.39%)</td><td>403.96 (+16.19%)</td><td>335.00 (+5.55%)</td><td>214.80 (-15.70%)</td><td>191.76 <b>(+54.16%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>564.60 (n/a)</td><td>347.68 (n/a)</td><td>317.40 (n/a)</td><td>254.80 (n/a)</td><td>124.39 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.18 (-10.56%)</td><td>0.16 (+4.18%)</td><td>0.16 (+2.30%)</td><td>0.12 <b>(+54.01%)</b></td><td>0.02 <b>(-50.94%)</b></td><td>407.90 <b>(-35.06%)</b></td><td>313.24 (-12.47%)</td><td>298.60 (-2.26%)</td><td>266.00 (+11.81%)</td><td>54.85 <b>(-64.96%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>628.10 (n/a)</td><td>357.86 (n/a)</td><td>305.50 (n/a)</td><td>237.90 (n/a)</td><td>156.51 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.20 (-8.18%)</td><td>0.13 (-19.66%)</td><td>0.10 <b>(-38.85%)</b></td><td>0.08 (-13.64%)</td><td>0.06 <b>(+24.98%)</b></td><td>639.40 (+15.79%)</td><td>439.26 <b>(+32.63%)</b></td><td>487.90 <b>(+63.51%)</b></td><td>246.00 (+8.90%)</td><td>176.95 <b>(+39.04%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>552.20 (n/a)</td><td>331.18 (n/a)</td><td>298.40 (n/a)</td><td>225.90 (n/a)</td><td>127.26 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.21 (+14.13%)</td><td>0.13 (+1.35%)</td><td>0.09 <b>(-41.25%)</b></td><td>0.07 <b>(+52.53%)</b></td><td>0.06 (+14.46%)</td><td>675.20 <b>(-34.43%)</b></td><td>448.22 (-7.31%)</td><td>518.70 <b>(+70.18%)</b></td><td>235.60 (-12.35%)</td><td>196.03 <b>(-38.87%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>1029.80 (n/a)</td><td>483.58 (n/a)</td><td>304.80 (n/a)</td><td>268.80 (n/a)</td><td>320.67 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.18 (-10.74%)</td><td>0.11 <b>(-33.71%)</b></td><td>0.12 <b>(-28.11%)</b></td><td>0.02 <b>(-80.20%)</b></td><td>0.06 <b>(+55.45%)</b></td><td>2419.10 <b>(+405.03%)</b></td><td>796.34 <b>(+154.28%)</b></td><td>395.30 <b>(+39.09%)</b></td><td>269.80 (+12.04%)</td><td>911.17 <b>(+862.13%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>479.00 (n/a)</td><td>313.18 (n/a)</td><td>284.20 (n/a)</td><td>240.80 (n/a)</td><td>94.70 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.23 (+16.12%)</td><td>0.13 (-18.38%)</td><td>0.11 <b>(-34.18%)</b></td><td>0.08 <b>(-24.28%)</b></td><td>0.06 <b>(+57.41%)</b></td><td>615.10 <b>(+32.08%)</b></td><td>434.72 <b>(+31.92%)</b></td><td>453.30 <b>(+51.91%)</b></td><td>210.10 (-13.89%)</td><td>145.04 <b>(+62.17%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>465.70 (n/a)</td><td>329.54 (n/a)</td><td>298.40 (n/a)</td><td>244.00 (n/a)</td><td>89.44 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.17 (-6.20%)</td><td>0.11 (+1.78%)</td><td>0.08 (-14.65%)</td><td>0.07 <b>(+181.65%)</b></td><td>0.05 <b>(-25.54%)</b></td><td>662.80 <b>(-64.49%)</b></td><td>502.34 <b>(-29.46%)</b></td><td>603.20 (+17.17%)</td><td>294.90 (+6.62%)</td><td>185.83 <b>(-71.91%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>1866.70 (n/a)</td><td>712.14 (n/a)</td><td>514.80 (n/a)</td><td>276.60 (n/a)</td><td>661.48 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (+6.72%)</td><td>0.01 (-9.73%)</td><td>0.01 <b>(-30.60%)</b></td><td>0.00 (-0.58%)</td><td>0.00 (+11.25%)</td><td>615.60 (+0.59%)</td><td>422.18 (+12.28%)</td><td>429.40 <b>(+44.09%)</b></td><td>231.10 (-6.32%)</td><td>154.87 (+2.82%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>612.00 (n/a)</td><td>376.00 (n/a)</td><td>298.00 (n/a)</td><td>246.70 (n/a)</td><td>150.63 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (-0.79%)</td><td>0.01 (-19.89%)</td><td>0.01 <b>(-29.04%)</b></td><td>0.00 <b>(-33.55%)</b></td><td>0.00 <b>(+40.19%)</b></td><td>600.50 <b>(+50.50%)</b></td><td>420.92 <b>(+31.70%)</b></td><td>420.40 <b>(+40.93%)</b></td><td>245.90 (+0.78%)</td><td>129.75 <b>(+101.98%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>399.00 (n/a)</td><td>319.60 (n/a)</td><td>298.30 (n/a)</td><td>244.00 (n/a)</td><td>64.24 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 <b>(-23.57%)</b></td><td>0.01 <b>(-46.69%)</b></td><td>0.01 <b>(-50.76%)</b></td><td>0.00 <b>(-88.87%)</b></td><td>0.00 <b>(+115.73%)</b></td><td>2464.80 <b>(+798.91%)</b></td><td>814.34 <b>(+248.31%)</b></td><td>477.30 <b>(+103.11%)</b></td><td>240.70 <b>(+30.89%)</b></td><td>932.13 <b>(+2748.12%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>274.20 (n/a)</td><td>233.80 (n/a)</td><td>235.00 (n/a)</td><td>183.90 (n/a)</td><td>32.73 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (-13.73%)</td><td>0.01 (+2.02%)</td><td>0.01 (+7.05%)</td><td>0.00 (+15.10%)</td><td>0.00 (-19.35%)</td><td>592.30 (-13.11%)</td><td>327.68 (-6.94%)</td><td>264.40 (-6.57%)</td><td>251.00 (+15.94%)</td><td>148.24 <b>(-21.60%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>681.70 (n/a)</td><td>352.10 (n/a)</td><td>283.00 (n/a)</td><td>216.50 (n/a)</td><td>189.08 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (-1.81%)</td><td>0.01 (-17.26%)</td><td>0.01 <b>(-30.22%)</b></td><td>0.00 (-13.49%)</td><td>0.00 (-3.92%)</td><td>659.90 (+15.59%)</td><td>474.98 <b>(+21.58%)</b></td><td>505.70 <b>(+43.34%)</b></td><td>278.30 (+1.83%)</td><td>147.31 (+13.62%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>570.90 (n/a)</td><td>390.66 (n/a)</td><td>352.80 (n/a)</td><td>273.30 (n/a)</td><td>129.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 <b>(-32.25%)</b></td><td>0.01 (-17.68%)</td><td>0.00 (-18.09%)</td><td>0.00 <b>(-23.49%)</b></td><td>0.00 <b>(-28.38%)</b></td><td>757.20 <b>(+30.71%)</b></td><td>513.60 (+19.16%)</td><td>601.00 <b>(+22.08%)</b></td><td>299.60 <b>(+47.59%)</b></td><td>204.47 <b>(+20.40%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>579.30 (n/a)</td><td>431.02 (n/a)</td><td>492.30 (n/a)</td><td>203.00 (n/a)</td><td>169.82 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (+5.97%)</td><td>0.02 (+18.64%)</td><td>0.02 <b>(+49.74%)</b></td><td>0.01 (+0.57%)</td><td>0.00 (-8.95%)</td><td>477.60 (-0.56%)</td><td>324.58 (-17.14%)</td><td>304.80 <b>(-33.20%)</b></td><td>238.40 (-5.66%)</td><td>92.99 (-15.00%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>480.30 (n/a)</td><td>391.72 (n/a)</td><td>456.30 (n/a)</td><td>252.70 (n/a)</td><td>109.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (+11.39%)</td><td>0.02 (+14.48%)</td><td>0.02 <b>(+31.74%)</b></td><td>0.01 (+11.61%)</td><td>0.01 <b>(+20.96%)</b></td><td>506.80 (-10.40%)</td><td>350.82 (-11.18%)</td><td>266.50 <b>(-24.10%)</b></td><td>242.40 (-10.22%)</td><td>128.37 (-0.96%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.60 (n/a)</td><td>395.00 (n/a)</td><td>351.10 (n/a)</td><td>270.00 (n/a)</td><td>129.62 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (+19.54%)</td><td>0.01 (+5.28%)</td><td>0.01 <b>(+28.56%)</b></td><td>0.00 <b>(-66.45%)</b></td><td>0.01 <b>(+55.19%)</b></td><td>2026.60 <b>(+198.07%)</b></td><td>686.08 <b>(+50.58%)</b></td><td>395.90 <b>(-22.20%)</b></td><td>231.80 (-16.35%)</td><td>757.50 <b>(+343.66%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>679.90 (n/a)</td><td>455.64 (n/a)</td><td>508.90 (n/a)</td><td>277.10 (n/a)</td><td>170.74 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 <b>(+37.97%)</b></td><td>0.01 (-2.36%)</td><td>0.01 (-19.23%)</td><td>0.01 <b>(-46.49%)</b></td><td>0.01 <b>(+91.18%)</b></td><td>993.70 <b>(+86.86%)</b></td><td>514.56 <b>(+28.75%)</b></td><td>501.30 <b>(+23.81%)</b></td><td>168.20 <b>(-27.53%)</b></td><td>300.59 <b>(+141.47%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>531.80 (n/a)</td><td>399.66 (n/a)</td><td>404.90 (n/a)</td><td>232.10 (n/a)</td><td>124.49 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (-13.04%)</td><td>0.01 (-12.30%)</td><td>0.01 (-3.87%)</td><td>0.01 (-2.64%)</td><td>0.00 <b>(-22.64%)</b></td><td>582.30 (+2.72%)</td><td>463.16 (+9.45%)</td><td>501.20 (+4.03%)</td><td>253.40 (+14.97%)</td><td>125.22 (-15.17%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.90 (n/a)</td><td>423.16 (n/a)</td><td>481.80 (n/a)</td><td>220.40 (n/a)</td><td>147.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (+17.64%)</td><td>0.01 <b>(+22.37%)</b></td><td>0.01 <b>(+20.68%)</b></td><td>0.01 <b>(+61.53%)</b></td><td>0.00 <b>(-23.79%)</b></td><td>478.50 <b>(-38.10%)</b></td><td>396.44 <b>(-21.70%)</b></td><td>379.50 (-17.14%)</td><td>329.00 (-14.99%)</td><td>62.64 <b>(-60.22%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>773.00 (n/a)</td><td>506.30 (n/a)</td><td>458.00 (n/a)</td><td>387.00 (n/a)</td><td>157.45 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (-3.27%)</td><td>0.03 (-3.77%)</td><td>0.02 (-1.06%)</td><td>0.02 (+0.11%)</td><td>0.01 (-14.65%)</td><td>525.30 (-0.11%)</td><td>394.40 (+1.19%)</td><td>423.80 (+1.07%)</td><td>244.20 (+3.39%)</td><td>118.11 (-12.06%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.90 (n/a)</td><td>389.76 (n/a)</td><td>419.30 (n/a)</td><td>236.20 (n/a)</td><td>134.30 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 <b>(+31.19%)</b></td><td>0.04 <b>(+49.36%)</b></td><td>0.04 <b>(+93.29%)</b></td><td>0.02 (+14.22%)</td><td>0.01 (+17.25%)</td><td>515.20 (-12.44%)</td><td>308.50 <b>(-33.21%)</b></td><td>271.10 <b>(-48.26%)</b></td><td>233.50 <b>(-23.77%)</b></td><td>117.11 (-16.56%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>588.40 (n/a)</td><td>461.92 (n/a)</td><td>524.00 (n/a)</td><td>306.30 (n/a)</td><td>140.36 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (-13.72%)</td><td>0.03 (-2.81%)</td><td>0.02 (+4.37%)</td><td>0.02 (+0.03%)</td><td>0.01 <b>(-35.13%)</b></td><td>557.00 (-0.02%)</td><td>417.16 (-1.97%)</td><td>423.50 (-4.19%)</td><td>290.60 (+15.92%)</td><td>96.19 <b>(-27.90%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>557.10 (n/a)</td><td>425.56 (n/a)</td><td>442.00 (n/a)</td><td>250.70 (n/a)</td><td>133.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (-3.01%)</td><td>0.03 <b>(+39.77%)</b></td><td>0.03 <b>(+45.54%)</b></td><td>0.02 <b>(+65.03%)</b></td><td>0.01 <b>(-24.59%)</b></td><td>487.90 <b>(-39.41%)</b></td><td>336.64 <b>(-35.91%)</b></td><td>329.20 <b>(-31.29%)</b></td><td>241.80 (+3.11%)</td><td>101.94 <b>(-54.01%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>805.30 (n/a)</td><td>525.26 (n/a)</td><td>479.10 (n/a)</td><td>234.50 (n/a)</td><td>221.63 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (+17.38%)</td><td>0.03 (+12.29%)</td><td>0.04 <b>(+53.20%)</b></td><td>0.00 <b>(-79.96%)</b></td><td>0.02 <b>(+179.22%)</b></td><td>2451.70 <b>(+399.12%)</b></td><td>739.80 <b>(+77.05%)</b></td><td>291.20 <b>(-34.74%)</b></td><td>257.00 (-14.82%)</td><td>960.02 <b>(+1119.51%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.20 (n/a)</td><td>417.84 (n/a)</td><td>446.20 (n/a)</td><td>301.70 (n/a)</td><td>78.72 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (+18.62%)</td><td>0.03 (+14.41%)</td><td>0.02 (-0.20%)</td><td>0.02 (+19.06%)</td><td>0.01 (+12.25%)</td><td>540.90 (-16.01%)</td><td>405.44 (-13.56%)</td><td>465.60 (+0.22%)</td><td>257.30 (-15.69%)</td><td>129.59 <b>(-21.26%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>644.00 (n/a)</td><td>469.02 (n/a)</td><td>464.60 (n/a)</td><td>305.20 (n/a)</td><td>164.58 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (+7.46%)</td><td>0.07 (+15.31%)</td><td>0.07 (+12.95%)</td><td>0.06 <b>(+41.80%)</b></td><td>0.01 <b>(-27.65%)</b></td><td>367.00 <b>(-29.48%)</b></td><td>300.42 (-16.19%)</td><td>305.50 (-11.47%)</td><td>244.60 (-6.96%)</td><td>45.29 <b>(-53.88%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>520.40 (n/a)</td><td>358.46 (n/a)</td><td>345.10 (n/a)</td><td>262.90 (n/a)</td><td>98.20 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (+6.29%)</td><td>0.07 (-3.00%)</td><td>0.08 (+2.69%)</td><td>0.04 (+15.13%)</td><td>0.02 (+6.27%)</td><td>520.30 (-13.14%)</td><td>330.80 (+1.65%)</td><td>256.40 (-2.62%)</td><td>221.50 (-5.90%)</td><td>127.65 (-17.12%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>599.00 (n/a)</td><td>325.42 (n/a)</td><td>263.30 (n/a)</td><td>235.40 (n/a)</td><td>154.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 <b>(+27.51%)</b></td><td>0.08 (+7.91%)</td><td>0.08 (-2.70%)</td><td>0.04 (-18.49%)</td><td>0.03 <b>(+71.58%)</b></td><td>550.80 <b>(+22.67%)</b></td><td>304.80 (+0.56%)</td><td>271.20 (+2.77%)</td><td>196.20 <b>(-21.55%)</b></td><td>142.69 <b>(+70.14%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>449.00 (n/a)</td><td>303.10 (n/a)</td><td>263.90 (n/a)</td><td>250.10 (n/a)</td><td>83.87 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 <b>(+24.41%)</b></td><td>0.07 (+11.07%)</td><td>0.05 <b>(-27.29%)</b></td><td>0.05 <b>(+24.36%)</b></td><td>0.03 <b>(+78.91%)</b></td><td>435.20 (-19.60%)</td><td>333.06 (-3.20%)</td><td>414.30 <b>(+37.55%)</b></td><td>190.50 (-19.62%)</td><td>128.60 (+9.43%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>541.30 (n/a)</td><td>344.08 (n/a)</td><td>301.20 (n/a)</td><td>237.00 (n/a)</td><td>117.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (-0.60%)</td><td>0.06 (+4.76%)</td><td>0.05 <b>(+31.20%)</b></td><td>0.03 <b>(-29.66%)</b></td><td>0.03 (+10.52%)</td><td>778.70 <b>(+42.18%)</b></td><td>423.42 (+2.55%)</td><td>382.00 <b>(-23.78%)</b></td><td>213.80 (+0.61%)</td><td>230.77 <b>(+45.57%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>547.70 (n/a)</td><td>412.90 (n/a)</td><td>501.20 (n/a)</td><td>212.50 (n/a)</td><td>158.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 <b>(-36.86%)</b></td><td>0.04 (-2.40%)</td><td>0.04 (-1.34%)</td><td>0.04 <b>(+220.92%)</b></td><td>0.01 <b>(-70.58%)</b></td><td>596.80 <b>(-68.84%)</b></td><td>501.36 <b>(-33.60%)</b></td><td>502.50 (+1.35%)</td><td>363.00 <b>(+58.38%)</b></td><td>86.61 <b>(-87.00%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1915.10 (n/a)</td><td>755.02 (n/a)</td><td>495.80 (n/a)</td><td>229.20 (n/a)</td><td>666.04 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>678.40 (n/a)</td><td>403.98 (n/a)</td><td>357.80 (n/a)</td><td>238.90 (n/a)</td><td>175.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>481.70 (n/a)</td><td>343.60 (n/a)</td><td>281.80 (n/a)</td><td>226.40 (n/a)</td><td>120.72 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1038.60 (n/a)</td><td>553.60 (n/a)</td><td>514.60 (n/a)</td><td>297.00 (n/a)</td><td>295.48 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.60 (n/a)</td><td>369.64 (n/a)</td><td>296.50 (n/a)</td><td>245.00 (n/a)</td><td>142.49 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>529.20 (n/a)</td><td>360.10 (n/a)</td><td>281.10 (n/a)</td><td>226.80 (n/a)</td><td>153.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>554.90 (n/a)</td><td>433.88 (n/a)</td><td>486.10 (n/a)</td><td>247.90 (n/a)</td><td>139.78 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>601.50 (n/a)</td><td>348.48 (n/a)</td><td>272.50 (n/a)</td><td>239.20 (n/a)</td><td>150.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>610.20 (n/a)</td><td>386.16 (n/a)</td><td>322.10 (n/a)</td><td>267.50 (n/a)</td><td>138.69 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1933.00 (n/a)</td><td>693.98 (n/a)</td><td>479.00 (n/a)</td><td>227.10 (n/a)</td><td>705.64 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.21 (-13.49%)</td><td>0.14 (+2.20%)</td><td>0.13 <b>(+22.34%)</b></td><td>0.08 (-0.91%)</td><td>0.05 <b>(-27.41%)</b></td><td>594.90 (+0.92%)</td><td>384.92 (-9.15%)</td><td>379.30 (-18.27%)</td><td>230.20 (+15.56%)</td><td>142.68 <b>(-20.21%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>589.50 (n/a)</td><td>423.70 (n/a)</td><td>464.10 (n/a)</td><td>199.20 (n/a)</td><td>178.81 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>1075.60 (n/a)</td><td>532.54 (n/a)</td><td>428.00 (n/a)</td><td>273.90 (n/a)</td><td>326.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>516.20 (n/a)</td><td>347.76 (n/a)</td><td>242.50 (n/a)</td><td>241.30 (n/a)</td><td>144.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.60 (n/a)</td><td>423.46 (n/a)</td><td>461.00 (n/a)</td><td>274.60 (n/a)</td><td>101.85 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>540.90 (n/a)</td><td>302.84 (n/a)</td><td>244.30 (n/a)</td><td>194.30 (n/a)</td><td>144.46 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.00 (n/a)</td><td>390.34 (n/a)</td><td>373.70 (n/a)</td><td>254.80 (n/a)</td><td>141.03 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.90 (n/a)</td><td>421.40 (n/a)</td><td>429.30 (n/a)</td><td>264.00 (n/a)</td><td>100.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>765.00 (n/a)</td><td>438.94 (n/a)</td><td>460.60 (n/a)</td><td>232.80 (n/a)</td><td>210.51 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>554.10 (n/a)</td><td>346.38 (n/a)</td><td>330.10 (n/a)</td><td>153.70 (n/a)</td><td>153.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>645.90 (n/a)</td><td>371.24 (n/a)</td><td>293.90 (n/a)</td><td>259.60 (n/a)</td><td>162.17 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2027.70 (n/a)</td><td>757.46 (n/a)</td><td>561.30 (n/a)</td><td>172.80 (n/a)</td><td>727.78 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>530.40 (n/a)</td><td>468.12 (n/a)</td><td>476.10 (n/a)</td><td>346.90 (n/a)</td><td>72.05 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>584.80 (n/a)</td><td>442.10 (n/a)</td><td>447.70 (n/a)</td><td>240.90 (n/a)</td><td>127.28 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>584.20 (n/a)</td><td>465.66 (n/a)</td><td>495.40 (n/a)</td><td>309.40 (n/a)</td><td>101.75 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.60 (n/a)</td><td>335.78 (n/a)</td><td>296.00 (n/a)</td><td>245.80 (n/a)</td><td>107.51 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2020.40 (n/a)</td><td>721.40 (n/a)</td><td>432.30 (n/a)</td><td>336.20 (n/a)</td><td>727.60 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1022.20 (n/a)</td><td>593.00 (n/a)</td><td>510.90 (n/a)</td><td>427.90 (n/a)</td><td>242.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>829.30 (n/a)</td><td>500.32 (n/a)</td><td>434.70 (n/a)</td><td>283.20 (n/a)</td><td>214.37 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.10 (n/a)</td><td>422.10 (n/a)</td><td>447.80 (n/a)</td><td>257.20 (n/a)</td><td>151.47 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>472.00 (n/a)</td><td>378.62 (n/a)</td><td>378.90 (n/a)</td><td>301.30 (n/a)</td><td>61.55 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>442.60 (n/a)</td><td>327.04 (n/a)</td><td>294.90 (n/a)</td><td>253.50 (n/a)</td><td>77.35 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.20 (n/a)</td><td>373.16 (n/a)</td><td>405.20 (n/a)</td><td>241.80 (n/a)</td><td>115.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>486.50 (n/a)</td><td>345.30 (n/a)</td><td>296.80 (n/a)</td><td>243.60 (n/a)</td><td>105.77 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.20 (n/a)</td><td>331.58 (n/a)</td><td>255.90 (n/a)</td><td>235.70 (n/a)</td><td>162.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1090.90 (n/a)</td><td>537.10 (n/a)</td><td>502.20 (n/a)</td><td>248.70 (n/a)</td><td>328.31 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1040.10 (n/a)</td><td>553.12 (n/a)</td><td>492.90 (n/a)</td><td>249.70 (n/a)</td><td>293.82 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>603.30 (n/a)</td><td>350.14 (n/a)</td><td>291.30 (n/a)</td><td>274.70 (n/a)</td><td>141.71 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>646.10 (n/a)</td><td>455.68 (n/a)</td><td>565.90 (n/a)</td><td>236.80 (n/a)</td><td>201.71 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1883.50 (n/a)</td><td>688.28 (n/a)</td><td>446.90 (n/a)</td><td>272.40 (n/a)</td><td>672.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>559.50 (n/a)</td><td>365.82 (n/a)</td><td>337.10 (n/a)</td><td>201.80 (n/a)</td><td>153.11 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>574.30 (n/a)</td><td>465.60 (n/a)</td><td>497.20 (n/a)</td><td>234.30 (n/a)</td><td>133.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>596.20 (n/a)</td><td>456.88 (n/a)</td><td>463.00 (n/a)</td><td>337.80 (n/a)</td><td>109.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>571.20 (n/a)</td><td>395.98 (n/a)</td><td>323.30 (n/a)</td><td>267.20 (n/a)</td><td>152.03 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>647.10 (n/a)</td><td>463.18 (n/a)</td><td>518.40 (n/a)</td><td>295.70 (n/a)</td><td>149.92 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1921.70 (n/a)</td><td>776.48 (n/a)</td><td>587.50 (n/a)</td><td>249.90 (n/a)</td><td>657.21 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>456.00 (n/a)</td><td>374.44 (n/a)</td><td>412.60 (n/a)</td><td>258.70 (n/a)</td><td>90.81 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>696.10 (n/a)</td><td>496.24 (n/a)</td><td>482.90 (n/a)</td><td>376.10 (n/a)</td><td>126.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.51 (+10.10%)</td><td>0.38 (-3.57%)</td><td>0.45 (+18.31%)</td><td>0.24 <b>(-31.17%)</b></td><td>0.13 <b>(+148.05%)</b></td><td>938.30 <b>(+45.29%)</b></td><td>645.98 (+13.95%)</td><td>496.60 (-15.49%)</td><td>437.60 (-9.19%)</td><td>245.39 <b>(+239.56%)</b></td><td>21.56 (+10.10%)</td><td>16.27 (-3.57%)</td><td>19.00 (+18.31%)</td><td>10.06 <b>(-31.17%)</b></td><td>5.49 <b>(+148.05%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.46 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.05 (n/a)</td><td>645.80 (n/a)</td><td>566.88 (n/a)</td><td>587.60 (n/a)</td><td>481.90 (n/a)</td><td>72.27 (n/a)</td><td>19.58 (n/a)</td><td>16.87 (n/a)</td><td>16.06 (n/a)</td><td>14.61 (n/a)</td><td>2.21 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.54 (+11.73%)</td><td>0.46 (+13.22%)</td><td>0.44 (+18.21%)</td><td>0.38 (+2.31%)</td><td>0.06 <b>(+33.54%)</b></td><td>581.00 (-2.25%)</td><td>493.22 (-11.20%)</td><td>502.40 (-15.41%)</td><td>411.00 (-10.50%)</td><td>68.37 (+14.79%)</td><td>22.96 (+11.73%)</td><td>19.44 (+13.22%)</td><td>18.78 (+18.21%)</td><td>16.24 (+2.31%)</td><td>2.72 <b>(+33.54%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.48 (n/a)</td><td>0.40 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.05 (n/a)</td><td>594.40 (n/a)</td><td>555.40 (n/a)</td><td>593.90 (n/a)</td><td>459.20 (n/a)</td><td>59.56 (n/a)</td><td>20.55 (n/a)</td><td>17.17 (n/a)</td><td>15.89 (n/a)</td><td>15.88 (n/a)</td><td>2.04 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.31 (-0.51%)</td><td>0.30 (-1.10%)</td><td>0.30 (-0.89%)</td><td>0.30 (-0.60%)</td><td>0.01 (-7.64%)</td><td>84780.80 (+0.60%)</td><td>83072.92 (+1.11%)</td><td>82923.40 (+0.90%)</td><td>80846.70 (+0.52%)</td><td>1560.47 (-6.31%)</td><td>212.50 (-0.51%)</td><td>206.86 (-1.10%)</td><td>207.18 (-0.89%)</td><td>202.64 (-0.60%)</td><td>3.91 (-7.64%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84272.90 (n/a)</td><td>82164.04 (n/a)</td><td>82187.70 (n/a)</td><td>80431.60 (n/a)</td><td>1665.56 (n/a)</td><td>213.60 (n/a)</td><td>209.16 (n/a)</td><td>209.03 (n/a)</td><td>203.86 (n/a)</td><td>4.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>1.04 (+1.54%)</td><td>1.02 (+0.39%)</td><td>1.02 (+0.94%)</td><td>1.00 (-1.23%)</td><td>0.02 <b>(+118.15%)</b></td><td>25233.40 (+1.24%)</td><td>24695.12 (-0.37%)</td><td>24686.20 (-0.93%)</td><td>24115.30 (-1.52%)</td><td>427.39 <b>(+117.26%)</b></td><td>712.41 (+1.54%)</td><td>695.85 (+0.39%)</td><td>695.93 (+0.94%)</td><td>680.84 (-1.23%)</td><td>12.07 <b>(+118.15%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>0.01 (n/a)</td><td>24923.90 (n/a)</td><td>24787.42 (n/a)</td><td>24918.90 (n/a)</td><td>24486.90 (n/a)</td><td>196.72 (n/a)</td><td>701.60 (n/a)</td><td>693.12 (n/a)</td><td>689.43 (n/a)</td><td>689.29 (n/a)</td><td>5.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.82 (+0.93%)</td><td>0.81 (+2.69%)</td><td>0.81 (+2.71%)</td><td>0.80 (+3.72%)</td><td>0.01 <b>(-64.38%)</b></td><td>93982.30 (-3.59%)</td><td>92989.42 (-2.64%)</td><td>92921.10 (-2.64%)</td><td>92485.80 (-0.92%)</td><td>606.53 <b>(-66.02%)</b></td><td>743.03 (+0.93%)</td><td>739.03 (+2.69%)</td><td>739.55 (+2.71%)</td><td>731.20 (+3.72%)</td><td>4.79 <b>(-64.38%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>97476.90 (n/a)</td><td>95513.26 (n/a)</td><td>95437.80 (n/a)</td><td>93344.20 (n/a)</td><td>1784.97 (n/a)</td><td>736.19 (n/a)</td><td>719.68 (n/a)</td><td>720.04 (n/a)</td><td>704.98 (n/a)</td><td>13.46 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.78 (-0.68%)</td><td>0.76 (-1.26%)</td><td>0.76 (-0.96%)</td><td>0.75 (-1.87%)</td><td>0.01 <b>(+67.20%)</b></td><td>101047.10 (+1.90%)</td><td>99094.16 (+1.29%)</td><td>98846.30 (+0.97%)</td><td>97413.30 (+0.68%)</td><td>1628.91 <b>(+71.55%)</b></td><td>705.44 (-0.68%)</td><td>693.63 (-1.26%)</td><td>695.22 (-0.96%)</td><td>680.07 (-1.87%)</td><td>11.38 <b>(+67.20%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99158.30 (n/a)</td><td>97832.86 (n/a)</td><td>97896.40 (n/a)</td><td>96750.80 (n/a)</td><td>949.50 (n/a)</td><td>710.27 (n/a)</td><td>702.47 (n/a)</td><td>701.96 (n/a)</td><td>693.03 (n/a)</td><td>6.80 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.80 (+0.12%)</td><td>0.79 (-0.06%)</td><td>0.79 (+0.37%)</td><td>0.77 (-1.22%)</td><td>0.01 <b>(+67.44%)</b></td><td>97662.20 (+1.24%)</td><td>95450.42 (+0.07%)</td><td>95003.90 (-0.37%)</td><td>94446.60 (-0.12%)</td><td>1298.60 <b>(+69.63%)</b></td><td>727.60 (+0.12%)</td><td>720.05 (-0.06%)</td><td>723.33 (+0.37%)</td><td>703.64 (-1.22%)</td><td>9.66 <b>(+67.44%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96470.60 (n/a)</td><td>95384.56 (n/a)</td><td>95355.00 (n/a)</td><td>94558.90 (n/a)</td><td>765.55 (n/a)</td><td>726.74 (n/a)</td><td>720.48 (n/a)</td><td>720.67 (n/a)</td><td>712.34 (n/a)</td><td>5.77 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.58 (-0.88%)</td><td>3.94 (+8.33%)</td><td>4.22 (+3.11%)</td><td>2.56 <b>(+29.96%)</b></td><td>1.17 <b>(-24.91%)</b></td><td>3482.60 <b>(-23.06%)</b></td><td>2433.96 (-15.99%)</td><td>2112.30 (-3.02%)</td><td>1598.20 (+0.89%)</td><td>740.81 <b>(-44.60%)</b></td><td>335.92 (-0.88%)</td><td>237.20 (+8.33%)</td><td>254.17 (+3.11%)</td><td>154.16 <b>(+29.96%)</b></td><td>70.23 <b>(-24.91%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.63 (n/a)</td><td>3.64 (n/a)</td><td>4.09 (n/a)</td><td>1.97 (n/a)</td><td>1.55 (n/a)</td><td>4526.10 (n/a)</td><td>2897.12 (n/a)</td><td>2178.10 (n/a)</td><td>1584.10 (n/a)</td><td>1337.29 (n/a)</td><td>338.91 (n/a)</td><td>218.97 (n/a)</td><td>246.49 (n/a)</td><td>118.62 (n/a)</td><td>93.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>2.20 <b>(-56.43%)</b></td><td>2.16 <b>(-25.21%)</b></td><td>2.17 (-4.24%)</td><td>2.07 (-3.31%)</td><td>0.05 <b>(-95.72%)</b></td><td>4303.70 (+3.42%)</td><td>4134.60 <b>(+20.44%)</b></td><td>4100.50 (+4.43%)</td><td>4046.00 <b>(+129.52%)</b></td><td>103.99 <b>(-89.71%)</b></td><td>132.69 <b>(-56.43%)</b></td><td>129.91 <b>(-25.21%)</b></td><td>130.93 (-4.24%)</td><td>124.75 (-3.31%)</td><td>3.20 <b>(-95.72%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.06 (n/a)</td><td>2.88 (n/a)</td><td>2.27 (n/a)</td><td>2.14 (n/a)</td><td>1.24 (n/a)</td><td>4161.30 (n/a)</td><td>3433.02 (n/a)</td><td>3926.60 (n/a)</td><td>1762.80 (n/a)</td><td>1010.38 (n/a)</td><td>304.56 (n/a)</td><td>173.71 (n/a)</td><td>136.73 (n/a)</td><td>129.01 (n/a)</td><td>74.82 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.56 <b>(+79.21%)</b></td><td>3.42 <b>(+27.25%)</b></td><td>2.73 (-0.60%)</td><td>2.18 (+0.05%)</td><td>1.42 <b>(+315.95%)</b></td><td>4090.60 (-0.05%)</td><td>2940.28 (-12.47%)</td><td>3266.30 (+0.61%)</td><td>1602.20 <b>(-44.20%)</b></td><td>1038.75 <b>(+126.58%)</b></td><td>335.07 <b>(+79.21%)</b></td><td>206.21 <b>(+27.25%)</b></td><td>164.37 (-0.60%)</td><td>131.25 (+0.05%)</td><td>85.63 <b>(+315.95%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.10 (n/a)</td><td>2.69 (n/a)</td><td>2.75 (n/a)</td><td>2.18 (n/a)</td><td>0.34 (n/a)</td><td>4092.60 (n/a)</td><td>3359.36 (n/a)</td><td>3246.60 (n/a)</td><td>2871.40 (n/a)</td><td>458.45 (n/a)</td><td>186.97 (n/a)</td><td>162.05 (n/a)</td><td>165.37 (n/a)</td><td>131.18 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>6.46 (+10.14%)</td><td>5.73 (+13.74%)</td><td>6.09 <b>(+23.01%)</b></td><td>4.83 (+15.90%)</td><td>0.77 <b>(+21.41%)</b></td><td>7222.10 (-13.72%)</td><td>6177.86 (-11.89%)</td><td>5724.90 (-18.71%)</td><td>5393.30 (-9.20%)</td><td>863.46 (-4.56%)</td><td>398.18 (+10.14%)</td><td>352.88 (+13.74%)</td><td>375.11 <b>(+23.01%)</b></td><td>297.35 (+15.90%)</td><td>47.22 <b>(+21.41%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.87 (n/a)</td><td>5.04 (n/a)</td><td>4.95 (n/a)</td><td>4.17 (n/a)</td><td>0.63 (n/a)</td><td>8370.30 (n/a)</td><td>7011.64 (n/a)</td><td>7042.40 (n/a)</td><td>5940.00 (n/a)</td><td>904.70 (n/a)</td><td>361.53 (n/a)</td><td>310.26 (n/a)</td><td>304.94 (n/a)</td><td>256.56 (n/a)</td><td>38.89 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.71 (+6.37%)</td><td>4.81 (-1.54%)</td><td>4.85 (-3.71%)</td><td>3.85 (-3.07%)</td><td>0.87 <b>(+61.90%)</b></td><td>9046.30 (+3.16%)</td><td>7445.04 (+3.18%)</td><td>7190.60 (+3.85%)</td><td>6102.50 (-5.99%)</td><td>1365.60 <b>(+52.46%)</b></td><td>351.90 (+6.37%)</td><td>296.24 (-1.54%)</td><td>298.65 (-3.71%)</td><td>237.39 (-3.07%)</td><td>53.33 <b>(+61.90%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.37 (n/a)</td><td>4.88 (n/a)</td><td>5.04 (n/a)</td><td>3.98 (n/a)</td><td>0.53 (n/a)</td><td>8769.00 (n/a)</td><td>7215.56 (n/a)</td><td>6923.80 (n/a)</td><td>6491.30 (n/a)</td><td>895.72 (n/a)</td><td>330.83 (n/a)</td><td>300.88 (n/a)</td><td>310.16 (n/a)</td><td>244.90 (n/a)</td><td>32.94 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>6.62 (-1.92%)</td><td>5.42 (-7.38%)</td><td>5.23 (-14.45%)</td><td>4.42 (-11.37%)</td><td>0.97 <b>(+33.35%)</b></td><td>7882.20 (+12.83%)</td><td>6596.72 (+9.36%)</td><td>6662.00 (+16.89%)</td><td>5269.00 (+1.95%)</td><td>1158.85 <b>(+51.31%)</b></td><td>407.57 (-1.92%)</td><td>333.92 (-7.38%)</td><td>322.35 (-14.45%)</td><td>272.45 (-11.37%)</td><td>59.89 <b>(+33.35%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>6.75 (n/a)</td><td>5.85 (n/a)</td><td>6.12 (n/a)</td><td>4.99 (n/a)</td><td>0.73 (n/a)</td><td>6985.70 (n/a)</td><td>6032.34 (n/a)</td><td>5699.20 (n/a)</td><td>5168.00 (n/a)</td><td>765.85 (n/a)</td><td>415.54 (n/a)</td><td>360.54 (n/a)</td><td>376.80 (n/a)</td><td>307.41 (n/a)</td><td>44.91 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.79 (+1.66%)</td><td>0.77 (-0.11%)</td><td>0.76 (-0.80%)</td><td>0.75 (-0.59%)</td><td>0.02 <b>(+99.98%)</b></td><td>101332.10 (+0.59%)</td><td>98679.12 (+0.15%)</td><td>99100.40 (+0.81%)</td><td>95625.70 (-1.64%)</td><td>2611.78 <b>(+97.36%)</b></td><td>718.63 (+1.66%)</td><td>696.79 (-0.11%)</td><td>693.43 (-0.80%)</td><td>678.16 (-0.59%)</td><td>18.52 <b>(+99.98%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100737.70 (n/a)</td><td>98527.78 (n/a)</td><td>98307.10 (n/a)</td><td>97215.90 (n/a)</td><td>1323.37 (n/a)</td><td>706.87 (n/a)</td><td>697.56 (n/a)</td><td>699.03 (n/a)</td><td>682.16 (n/a)</td><td>9.26 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.77 (-0.08%)</td><td>0.75 (-0.53%)</td><td>0.76 (-1.39%)</td><td>0.73 (+0.84%)</td><td>0.02 <b>(-24.17%)</b></td><td>103835.30 (-0.83%)</td><td>100160.68 (+0.50%)</td><td>99649.70 (+1.41%)</td><td>97974.00 (+0.08%)</td><td>2182.07 <b>(-24.46%)</b></td><td>701.41 (-0.08%)</td><td>686.35 (-0.53%)</td><td>689.61 (-1.39%)</td><td>661.81 (+0.84%)</td><td>14.66 <b>(-24.17%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.02 (n/a)</td><td>104704.10 (n/a)</td><td>99661.36 (n/a)</td><td>98266.70 (n/a)</td><td>97898.40 (n/a)</td><td>2888.81 (n/a)</td><td>701.95 (n/a)</td><td>689.98 (n/a)</td><td>699.32 (n/a)</td><td>656.32 (n/a)</td><td>19.33 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.81 (-0.21%)</td><td>0.80 (+0.44%)</td><td>0.80 (+0.41%)</td><td>0.79 (+1.31%)</td><td>0.01 <b>(-39.16%)</b></td><td>95801.60 (-1.30%)</td><td>94439.06 (-0.45%)</td><td>94172.20 (-0.41%)</td><td>93437.20 (+0.21%)</td><td>895.46 <b>(-39.81%)</b></td><td>735.46 (-0.21%)</td><td>727.71 (+0.44%)</td><td>729.72 (+0.41%)</td><td>717.31 (+1.31%)</td><td>6.87 <b>(-39.16%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>97060.20 (n/a)</td><td>94861.62 (n/a)</td><td>94556.20 (n/a)</td><td>93244.20 (n/a)</td><td>1487.70 (n/a)</td><td>736.98 (n/a)</td><td>724.56 (n/a)</td><td>726.76 (n/a)</td><td>708.01 (n/a)</td><td>11.29 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.36 (+0.60%)</td><td>1.94 (-16.55%)</td><td>1.73 (-1.65%)</td><td>1.09 <b>(-30.36%)</b></td><td>0.86 (-4.53%)</td><td>7385.90 <b>(+43.59%)</b></td><td>4747.84 <b>(+22.69%)</b></td><td>4669.80 (+1.68%)</td><td>2396.90 (-0.60%)</td><td>1829.34 <b>(+37.61%)</b></td><td>881.95 (+0.60%)</td><td>510.03 (-16.55%)</td><td>452.68 (-1.65%)</td><td>286.21 <b>(-30.36%)</b></td><td>226.14 (-4.53%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.34 (n/a)</td><td>2.33 (n/a)</td><td>1.76 (n/a)</td><td>1.57 (n/a)</td><td>0.90 (n/a)</td><td>5143.60 (n/a)</td><td>3869.94 (n/a)</td><td>4592.60 (n/a)</td><td>2411.30 (n/a)</td><td>1329.38 (n/a)</td><td>876.67 (n/a)</td><td>611.15 (n/a)</td><td>460.29 (n/a)</td><td>410.99 (n/a)</td><td>236.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.23 (-5.32%)</td><td>0.21 (+1.40%)</td><td>0.21 (+2.61%)</td><td>0.18 (+8.42%)</td><td>0.02 <b>(-28.63%)</b></td><td>6823.40 (-7.77%)</td><td>6114.16 (-2.08%)</td><td>5848.40 (-2.55%)</td><td>5510.40 (+5.62%)</td><td>585.35 <b>(-30.19%)</b></td><td>12.18 (-5.32%)</td><td>11.06 (+1.40%)</td><td>11.47 (+2.61%)</td><td>9.84 (+8.42%)</td><td>1.03 <b>(-28.63%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>7397.90 (n/a)</td><td>6243.82 (n/a)</td><td>6001.20 (n/a)</td><td>5217.30 (n/a)</td><td>838.44 (n/a)</td><td>12.86 (n/a)</td><td>10.90 (n/a)</td><td>11.18 (n/a)</td><td>9.07 (n/a)</td><td>1.45 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (+9.32%)</td><td>0.10 (+6.37%)</td><td>0.11 (+18.02%)</td><td>0.07 (-13.24%)</td><td>0.02 <b>(+28.63%)</b></td><td>0.13 (+9.32%)</td><td>0.10 (+6.37%)</td><td>0.10 (+18.02%)</td><td>0.06 (-13.24%)</td><td>0.02 <b>(+28.63%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.94 (+0.56%)</td><td>3.69 (-0.07%)</td><td>3.64 (-4.03%)</td><td>3.51 (+2.04%)</td><td>0.16 <b>(-21.80%)</b></td><td>3.93 (+0.56%)</td><td>3.69 (-0.07%)</td><td>3.64 (-4.03%)</td><td>3.51 (+2.04%)</td><td>0.16 <b>(-21.80%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.91 (n/a)</td><td>3.69 (n/a)</td><td>3.79 (n/a)</td><td>3.44 (n/a)</td><td>0.21 (n/a)</td><td>3.91 (n/a)</td><td>3.69 (n/a)</td><td>3.79 (n/a)</td><td>3.44 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>7.21 (-0.00%)</td><td>6.16 (-9.52%)</td><td>5.85 (-13.40%)</td><td>5.58 (-15.98%)</td><td>0.67 <b>(+184.52%)</b></td><td>7.20 (-0.00%)</td><td>6.15 (-9.52%)</td><td>5.84 (-13.40%)</td><td>5.57 (-15.98%)</td><td>0.67 <b>(+184.52%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>7.21 (n/a)</td><td>6.81 (n/a)</td><td>6.75 (n/a)</td><td>6.64 (n/a)</td><td>0.23 (n/a)</td><td>7.20 (n/a)</td><td>6.80 (n/a)</td><td>6.75 (n/a)</td><td>6.63 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>13.95 (+5.28%)</td><td>8.78 (-11.53%)</td><td>8.43 (+0.50%)</td><td>5.49 <b>(-24.81%)</b></td><td>3.13 (+15.06%)</td><td>13.94 (+5.28%)</td><td>8.78 (-11.53%)</td><td>8.42 (+0.50%)</td><td>5.48 <b>(-24.81%)</b></td><td>3.13 (+15.06%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>13.25 (n/a)</td><td>9.93 (n/a)</td><td>8.39 (n/a)</td><td>7.30 (n/a)</td><td>2.72 (n/a)</td><td>13.24 (n/a)</td><td>9.92 (n/a)</td><td>8.38 (n/a)</td><td>7.29 (n/a)</td><td>2.72 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.86 (-0.95%)</td><td>3.52 (-3.77%)</td><td>3.46 (-8.50%)</td><td>3.09 (+2.42%)</td><td>0.30 (-16.75%)</td><td>3.86 (-0.95%)</td><td>3.51 (-3.77%)</td><td>3.46 (-8.50%)</td><td>3.09 (+2.42%)</td><td>0.30 (-16.75%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.90 (n/a)</td><td>3.65 (n/a)</td><td>3.78 (n/a)</td><td>3.02 (n/a)</td><td>0.36 (n/a)</td><td>3.90 (n/a)</td><td>3.65 (n/a)</td><td>3.78 (n/a)</td><td>3.02 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>6.81 (-6.15%)</td><td>6.27 (-3.42%)</td><td>6.76 (+0.01%)</td><td>4.87 (-11.50%)</td><td>0.84 (+12.76%)</td><td>6.81 (-6.15%)</td><td>6.27 (-3.42%)</td><td>6.76 (+0.01%)</td><td>4.87 (-11.50%)</td><td>0.84 (+12.76%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>7.26 (n/a)</td><td>6.49 (n/a)</td><td>6.76 (n/a)</td><td>5.50 (n/a)</td><td>0.74 (n/a)</td><td>7.25 (n/a)</td><td>6.49 (n/a)</td><td>6.76 (n/a)</td><td>5.50 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>13.95 (+0.82%)</td><td>9.96 (+4.90%)</td><td>8.47 (-1.14%)</td><td>7.80 (-4.78%)</td><td>2.64 (+8.20%)</td><td>13.94 (+0.82%)</td><td>9.95 (+4.90%)</td><td>8.47 (-1.14%)</td><td>7.79 (-4.78%)</td><td>2.63 (+8.20%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>13.84 (n/a)</td><td>9.49 (n/a)</td><td>8.57 (n/a)</td><td>8.19 (n/a)</td><td>2.44 (n/a)</td><td>13.83 (n/a)</td><td>9.49 (n/a)</td><td>8.57 (n/a)</td><td>8.19 (n/a)</td><td>2.44 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.30 (n/a)</td><td>400.46 (n/a)</td><td>418.00 (n/a)</td><td>235.50 (n/a)</td><td>168.38 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.90 (n/a)</td><td>362.86 (n/a)</td><td>371.70 (n/a)</td><td>220.40 (n/a)</td><td>126.38 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>517.40 (n/a)</td><td>360.82 (n/a)</td><td>293.90 (n/a)</td><td>261.30 (n/a)</td><td>114.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.10 (n/a)</td><td>393.56 (n/a)</td><td>301.30 (n/a)</td><td>220.70 (n/a)</td><td>167.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>581.70 (n/a)</td><td>419.32 (n/a)</td><td>425.80 (n/a)</td><td>221.90 (n/a)</td><td>143.46 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>630.20 (n/a)</td><td>452.62 (n/a)</td><td>500.60 (n/a)</td><td>231.30 (n/a)</td><td>172.29 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>572.40 (n/a)</td><td>400.98 (n/a)</td><td>476.40 (n/a)</td><td>161.40 (n/a)</td><td>168.44 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.90 (n/a)</td><td>411.08 (n/a)</td><td>420.80 (n/a)</td><td>216.60 (n/a)</td><td>122.58 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.60 (n/a)</td><td>409.00 (n/a)</td><td>428.70 (n/a)</td><td>195.30 (n/a)</td><td>140.46 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.80 (n/a)</td><td>426.82 (n/a)</td><td>406.30 (n/a)</td><td>280.40 (n/a)</td><td>145.54 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.20 (n/a)</td><td>449.66 (n/a)</td><td>405.30 (n/a)</td><td>210.40 (n/a)</td><td>182.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>469.40 (n/a)</td><td>398.16 (n/a)</td><td>416.10 (n/a)</td><td>320.10 (n/a)</td><td>57.03 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1934.00 (n/a)</td><td>669.46 (n/a)</td><td>392.50 (n/a)</td><td>288.00 (n/a)</td><td>709.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2479.10 (n/a)</td><td>845.64 (n/a)</td><td>516.00 (n/a)</td><td>233.10 (n/a)</td><td>921.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>639.30 (n/a)</td><td>385.92 (n/a)</td><td>243.80 (n/a)</td><td>238.00 (n/a)</td><td>200.28 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1880.70 (n/a)</td><td>616.28 (n/a)</td><td>274.80 (n/a)</td><td>175.80 (n/a)</td><td>715.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>582.60 (n/a)</td><td>389.56 (n/a)</td><td>361.30 (n/a)</td><td>238.10 (n/a)</td><td>153.69 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>590.30 (n/a)</td><td>429.02 (n/a)</td><td>485.20 (n/a)</td><td>274.50 (n/a)</td><td>133.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 <b>(+22.72%)</b></td><td>0.09 <b>(+32.77%)</b></td><td>0.09 <b>(+41.33%)</b></td><td>0.07 <b>(+111.47%)</b></td><td>0.03 (-13.28%)</td><td>479.60 <b>(-52.72%)</b></td><td>372.16 <b>(-33.48%)</b></td><td>367.30 <b>(-29.24%)</b></td><td>247.10 (-18.50%)</td><td>103.53 <b>(-64.00%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1014.30 (n/a)</td><td>559.44 (n/a)</td><td>519.10 (n/a)</td><td>303.20 (n/a)</td><td>287.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>673.40 (n/a)</td><td>527.30 (n/a)</td><td>559.00 (n/a)</td><td>234.60 (n/a)</td><td>172.78 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>723.00 (n/a)</td><td>412.26 (n/a)</td><td>281.70 (n/a)</td><td>239.30 (n/a)</td><td>212.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>494.60 (n/a)</td><td>344.46 (n/a)</td><td>340.60 (n/a)</td><td>216.20 (n/a)</td><td>120.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>545.40 (n/a)</td><td>451.70 (n/a)</td><td>507.60 (n/a)</td><td>248.40 (n/a)</td><td>119.04 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>506.70 (n/a)</td><td>376.90 (n/a)</td><td>309.80 (n/a)</td><td>295.20 (n/a)</td><td>101.73 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (-19.28%)</td><td>0.01 (+14.09%)</td><td>0.01 <b>(+44.26%)</b></td><td>0.01 <b>(+97.85%)</b></td><td>0.00 <b>(-40.24%)</b></td><td>523.70 <b>(-49.46%)</b></td><td>387.74 <b>(-28.69%)</b></td><td>383.70 <b>(-30.69%)</b></td><td>269.80 <b>(+23.88%)</b></td><td>118.17 <b>(-62.80%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1036.20 (n/a)</td><td>543.76 (n/a)</td><td>553.60 (n/a)</td><td>217.80 (n/a)</td><td>317.71 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (-10.20%)</td><td>0.01 (-9.69%)</td><td>0.01 (-7.00%)</td><td>0.01 (-9.05%)</td><td>0.00 (-15.50%)</td><td>559.10 (+9.95%)</td><td>351.64 (+9.65%)</td><td>319.60 (+7.50%)</td><td>226.90 (+11.39%)</td><td>123.79 (+6.03%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>508.50 (n/a)</td><td>320.70 (n/a)</td><td>297.30 (n/a)</td><td>203.70 (n/a)</td><td>116.75 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (-10.51%)</td><td>0.01 (-15.11%)</td><td>0.01 (-4.93%)</td><td>0.01 <b>(-24.87%)</b></td><td>0.00 (-7.18%)</td><td>680.90 <b>(+33.09%)</b></td><td>449.54 <b>(+21.91%)</b></td><td>463.10 (+5.18%)</td><td>238.30 (+11.77%)</td><td>193.06 <b>(+40.29%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>511.60 (n/a)</td><td>368.74 (n/a)</td><td>440.30 (n/a)</td><td>213.20 (n/a)</td><td>137.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (+4.56%)</td><td>0.01 (+9.69%)</td><td>0.02 <b>(+51.14%)</b></td><td>0.00 <b>(-63.21%)</b></td><td>0.01 (+15.15%)</td><td>1959.90 <b>(+171.79%)</b></td><td>592.34 <b>(+47.53%)</b></td><td>267.10 <b>(-33.84%)</b></td><td>193.00 (-4.36%)</td><td>765.28 <b>(+268.07%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>721.10 (n/a)</td><td>401.50 (n/a)</td><td>403.70 (n/a)</td><td>201.80 (n/a)</td><td>207.92 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 <b>(-36.11%)</b></td><td>0.01 (-7.48%)</td><td>0.01 <b>(+29.82%)</b></td><td>0.01 (-10.14%)</td><td>0.00 <b>(-42.71%)</b></td><td>546.00 (+11.29%)</td><td>377.82 (+2.50%)</td><td>293.50 <b>(-22.97%)</b></td><td>289.20 <b>(+56.58%)</b></td><td>120.79 (-4.48%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>490.60 (n/a)</td><td>368.62 (n/a)</td><td>381.00 (n/a)</td><td>184.70 (n/a)</td><td>126.46 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 <b>(+34.51%)</b></td><td>0.01 <b>(+27.59%)</b></td><td>0.01 <b>(+20.07%)</b></td><td>0.01 <b>(+27.24%)</b></td><td>0.01 <b>(+26.62%)</b></td><td>501.00 <b>(-21.41%)</b></td><td>325.70 <b>(-22.79%)</b></td><td>299.00 (-16.71%)</td><td>184.40 <b>(-25.65%)</b></td><td>115.25 <b>(-29.17%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>637.50 (n/a)</td><td>421.86 (n/a)</td><td>359.00 (n/a)</td><td>248.00 (n/a)</td><td>162.71 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 <b>(+78.25%)</b></td><td>0.01 (+18.11%)</td><td>0.01 (-14.06%)</td><td>0.01 (-13.07%)</td><td>0.01 <b>(+232.76%)</b></td><td>675.40 (+15.04%)</td><td>465.20 (-1.17%)</td><td>538.10 (+16.35%)</td><td>209.30 <b>(-43.90%)</b></td><td>191.51 <b>(+113.44%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.10 (n/a)</td><td>470.70 (n/a)</td><td>462.50 (n/a)</td><td>373.10 (n/a)</td><td>89.73 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 <b>(-23.65%)</b></td><td>0.01 (+2.79%)</td><td>0.01 <b>(+25.19%)</b></td><td>0.01 (+4.06%)</td><td>0.00 <b>(-38.15%)</b></td><td>511.50 (-3.89%)</td><td>374.10 (-9.02%)</td><td>390.20 <b>(-20.12%)</b></td><td>272.90 <b>(+30.95%)</b></td><td>101.15 <b>(-27.33%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>532.20 (n/a)</td><td>411.20 (n/a)</td><td>488.50 (n/a)</td><td>208.40 (n/a)</td><td>139.20 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 <b>(-22.80%)</b></td><td>0.01 <b>(-23.92%)</b></td><td>0.01 (-17.56%)</td><td>0.00 <b>(-62.38%)</b></td><td>0.00 (-19.91%)</td><td>2127.30 <b>(+165.78%)</b></td><td>794.90 <b>(+64.40%)</b></td><td>549.70 <b>(+21.29%)</b></td><td>312.20 <b>(+29.54%)</b></td><td>751.93 <b>(+218.61%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>800.40 (n/a)</td><td>483.52 (n/a)</td><td>453.20 (n/a)</td><td>241.00 (n/a)</td><td>236.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (-2.27%)</td><td>0.01 (+14.47%)</td><td>0.01 (+18.23%)</td><td>0.01 <b>(+43.38%)</b></td><td>0.00 <b>(-23.34%)</b></td><td>496.50 <b>(-30.26%)</b></td><td>389.52 (-18.27%)</td><td>411.20 (-15.41%)</td><td>244.10 (+2.35%)</td><td>94.12 <b>(-43.93%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>711.90 (n/a)</td><td>476.62 (n/a)</td><td>486.10 (n/a)</td><td>238.50 (n/a)</td><td>167.87 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (+15.66%)</td><td>0.01 (+7.76%)</td><td>0.01 (-11.20%)</td><td>0.01 (+3.53%)</td><td>0.00 <b>(+39.92%)</b></td><td>535.60 (-3.43%)</td><td>402.00 (-3.83%)</td><td>466.30 (+12.61%)</td><td>243.30 (-13.54%)</td><td>127.85 (+15.37%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>554.60 (n/a)</td><td>418.00 (n/a)</td><td>414.10 (n/a)</td><td>281.40 (n/a)</td><td>110.82 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (+3.28%)</td><td>0.01 <b>(+40.93%)</b></td><td>0.01 <b>(+73.25%)</b></td><td>0.01 <b>(+73.09%)</b></td><td>0.00 <b>(-31.53%)</b></td><td>464.20 <b>(-42.23%)</b></td><td>359.38 <b>(-34.56%)</b></td><td>321.50 <b>(-42.29%)</b></td><td>277.60 (-3.14%)</td><td>77.37 <b>(-59.16%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>803.50 (n/a)</td><td>549.14 (n/a)</td><td>557.10 (n/a)</td><td>286.60 (n/a)</td><td>189.45 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 <b>(+20.56%)</b></td><td>0.03 <b>(+21.51%)</b></td><td>0.03 <b>(+58.38%)</b></td><td>0.01 (+8.43%)</td><td>0.01 <b>(+27.10%)</b></td><td>577.60 (-7.76%)</td><td>363.46 (-15.45%)</td><td>295.90 <b>(-36.87%)</b></td><td>222.60 (-17.06%)</td><td>148.03 (+2.60%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.20 (n/a)</td><td>429.86 (n/a)</td><td>468.70 (n/a)</td><td>268.40 (n/a)</td><td>144.27 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 <b>(+56.83%)</b></td><td>0.03 <b>(+21.02%)</b></td><td>0.03 (+4.42%)</td><td>0.02 <b>(+21.76%)</b></td><td>0.01 <b>(+58.52%)</b></td><td>476.60 (-17.87%)</td><td>302.16 (-15.70%)</td><td>278.60 (-4.23%)</td><td>175.00 <b>(-36.25%)</b></td><td>109.27 (-16.01%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.30 (n/a)</td><td>358.42 (n/a)</td><td>290.90 (n/a)</td><td>274.50 (n/a)</td><td>130.09 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 <b>(+21.66%)</b></td><td>0.02 (+6.50%)</td><td>0.02 (-14.56%)</td><td>0.01 (+8.65%)</td><td>0.01 <b>(+35.71%)</b></td><td>585.40 (-7.97%)</td><td>409.78 (+0.11%)</td><td>482.80 (+17.01%)</td><td>195.40 (-17.80%)</td><td>182.74 (+8.77%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.10 (n/a)</td><td>409.32 (n/a)</td><td>412.60 (n/a)</td><td>237.70 (n/a)</td><td>168.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (-10.03%)</td><td>0.02 (-2.16%)</td><td>0.03 <b>(+21.30%)</b></td><td>0.02 (-6.58%)</td><td>0.01 (-14.76%)</td><td>510.40 (+7.05%)</td><td>361.14 (+1.54%)</td><td>313.50 (-17.57%)</td><td>253.70 (+11.17%)</td><td>102.04 (+5.26%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.80 (n/a)</td><td>355.66 (n/a)</td><td>380.30 (n/a)</td><td>228.20 (n/a)</td><td>96.94 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 <b>(-40.66%)</b></td><td>0.02 <b>(-36.65%)</b></td><td>0.02 <b>(-39.32%)</b></td><td>0.01 <b>(-28.13%)</b></td><td>0.00 <b>(-62.71%)</b></td><td>588.50 <b>(+39.13%)</b></td><td>503.60 <b>(+54.66%)</b></td><td>497.20 <b>(+64.80%)</b></td><td>431.20 <b>(+68.57%)</b></td><td>56.58 (-13.37%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>423.00 (n/a)</td><td>325.62 (n/a)</td><td>301.70 (n/a)</td><td>255.80 (n/a)</td><td>65.31 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (-6.91%)</td><td>0.02 <b>(-34.79%)</b></td><td>0.02 <b>(-48.23%)</b></td><td>0.00 <b>(-83.01%)</b></td><td>0.01 <b>(+133.35%)</b></td><td>1857.60 <b>(+488.59%)</b></td><td>666.72 <b>(+151.02%)</b></td><td>462.20 <b>(+93.15%)</b></td><td>242.30 (+7.40%)</td><td>675.66 <b>(+1394.03%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>315.60 (n/a)</td><td>265.60 (n/a)</td><td>239.30 (n/a)</td><td>225.60 (n/a)</td><td>45.22 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 <b>(-25.70%)</b></td><td>0.02 <b>(-21.62%)</b></td><td>0.02 (-19.15%)</td><td>0.01 (+4.08%)</td><td>0.00 <b>(-49.65%)</b></td><td>595.30 (-3.92%)</td><td>488.34 <b>(+20.89%)</b></td><td>465.00 <b>(+23.70%)</b></td><td>369.40 <b>(+34.57%)</b></td><td>90.50 <b>(-34.13%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.60 (n/a)</td><td>403.94 (n/a)</td><td>375.90 (n/a)</td><td>274.50 (n/a)</td><td>137.39 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (-7.18%)</td><td>0.02 (-7.59%)</td><td>0.02 <b>(-25.84%)</b></td><td>0.00 (+5.31%)</td><td>0.01 (-14.93%)</td><td>1819.60 (-5.05%)</td><td>659.02 (-3.19%)</td><td>392.00 <b>(+34.85%)</b></td><td>229.60 (+7.74%)</td><td>659.70 (-7.95%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1916.30 (n/a)</td><td>680.72 (n/a)</td><td>290.70 (n/a)</td><td>213.10 (n/a)</td><td>716.71 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (+17.77%)</td><td>0.02 <b>(+23.79%)</b></td><td>0.02 <b>(+20.26%)</b></td><td>0.02 <b>(+40.98%)</b></td><td>0.00 (-16.28%)</td><td>537.70 <b>(-29.06%)</b></td><td>461.92 <b>(-20.51%)</b></td><td>451.00 (-16.85%)</td><td>387.80 (-15.09%)</td><td>55.65 <b>(-50.55%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>758.00 (n/a)</td><td>581.12 (n/a)</td><td>542.40 (n/a)</td><td>456.70 (n/a)</td><td>112.55 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (+11.58%)</td><td>0.02 (-2.75%)</td><td>0.02 (-16.85%)</td><td>0.01 (-11.95%)</td><td>0.01 <b>(+41.79%)</b></td><td>571.10 (+13.58%)</td><td>431.36 (+7.32%)</td><td>472.50 <b>(+20.29%)</b></td><td>247.80 (-10.38%)</td><td>128.53 <b>(+40.08%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.80 (n/a)</td><td>401.92 (n/a)</td><td>392.80 (n/a)</td><td>276.50 (n/a)</td><td>91.75 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (+17.57%)</td><td>0.02 (-1.12%)</td><td>0.02 <b>(-30.39%)</b></td><td>0.01 (-13.06%)</td><td>0.01 <b>(+128.01%)</b></td><td>568.10 (+15.02%)</td><td>429.30 (+13.57%)</td><td>532.90 <b>(+43.64%)</b></td><td>244.50 (-14.93%)</td><td>164.70 <b>(+118.29%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>493.90 (n/a)</td><td>378.00 (n/a)</td><td>371.00 (n/a)</td><td>287.40 (n/a)</td><td>75.45 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 <b>(+25.95%)</b></td><td>0.02 <b>(+54.13%)</b></td><td>0.01 <b>(+90.14%)</b></td><td>0.01 <b>(+229.07%)</b></td><td>0.01 (-5.18%)</td><td>615.10 <b>(-69.61%)</b></td><td>469.58 <b>(-54.62%)</b></td><td>591.20 <b>(-47.41%)</b></td><td>232.70 <b>(-20.58%)</b></td><td>188.95 <b>(-73.76%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2024.30 (n/a)</td><td>1034.74 (n/a)</td><td>1124.20 (n/a)</td><td>293.00 (n/a)</td><td>720.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (+12.81%)</td><td>0.05 (-1.08%)</td><td>0.05 (-8.81%)</td><td>0.03 (-0.71%)</td><td>0.02 (+19.92%)</td><td>529.40 (+0.72%)</td><td>337.72 (+2.69%)</td><td>308.90 (+9.66%)</td><td>194.10 (-11.37%)</td><td>121.79 (+2.62%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>525.60 (n/a)</td><td>328.86 (n/a)</td><td>281.70 (n/a)</td><td>219.00 (n/a)</td><td>118.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 <b>(-23.78%)</b></td><td>0.05 (-10.82%)</td><td>0.06 (+0.95%)</td><td>0.03 (-12.37%)</td><td>0.02 <b>(-27.20%)</b></td><td>532.10 (+14.11%)</td><td>352.32 (+9.72%)</td><td>283.00 (-0.95%)</td><td>187.30 <b>(+31.25%)</b></td><td>152.74 (+15.71%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>466.30 (n/a)</td><td>321.10 (n/a)</td><td>285.70 (n/a)</td><td>142.70 (n/a)</td><td>132.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 <b>(+24.90%)</b></td><td>0.06 (+6.89%)</td><td>0.06 (+19.13%)</td><td>0.03 (-9.75%)</td><td>0.02 <b>(+92.34%)</b></td><td>495.10 (+10.81%)</td><td>335.60 (+4.14%)</td><td>258.70 (-16.03%)</td><td>190.20 (-19.95%)</td><td>147.68 <b>(+85.61%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>446.80 (n/a)</td><td>322.26 (n/a)</td><td>308.10 (n/a)</td><td>237.60 (n/a)</td><td>79.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (+0.64%)</td><td>0.04 (+1.18%)</td><td>0.04 (+5.74%)</td><td>0.03 (+5.25%)</td><td>0.01 (-12.83%)</td><td>555.50 (-4.98%)</td><td>460.26 (-1.83%)</td><td>459.70 (-5.43%)</td><td>370.40 (-0.64%)</td><td>67.70 (-17.36%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>584.60 (n/a)</td><td>468.84 (n/a)</td><td>486.10 (n/a)</td><td>372.80 (n/a)</td><td>81.92 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (+7.71%)</td><td>0.04 (+6.17%)</td><td>0.03 (-14.63%)</td><td>0.03 (+4.17%)</td><td>0.02 <b>(+34.29%)</b></td><td>550.00 (-4.00%)</td><td>428.44 (-1.20%)</td><td>529.80 (+17.16%)</td><td>249.30 (-7.15%)</td><td>151.00 <b>(+23.09%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>572.90 (n/a)</td><td>433.64 (n/a)</td><td>452.20 (n/a)</td><td>268.50 (n/a)</td><td>122.67 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (+18.34%)</td><td>0.07 <b>(+37.56%)</b></td><td>0.07 <b>(+32.74%)</b></td><td>0.03 (+6.43%)</td><td>0.02 <b>(+25.39%)</b></td><td>483.10 (-6.05%)</td><td>260.76 <b>(-25.39%)</b></td><td>222.90 <b>(-24.65%)</b></td><td>173.20 (-15.47%)</td><td>127.57 (-0.03%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>514.20 (n/a)</td><td>349.50 (n/a)</td><td>295.80 (n/a)</td><td>204.90 (n/a)</td><td>127.60 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 <b>(+21.19%)</b></td><td>0.05 <b>(+44.47%)</b></td><td>0.04 <b>(+38.28%)</b></td><td>0.04 <b>(+193.85%)</b></td><td>0.01 (-18.91%)</td><td>461.80 <b>(-65.97%)</b></td><td>378.32 <b>(-42.90%)</b></td><td>373.70 <b>(-27.68%)</b></td><td>245.70 (-17.49%)</td><td>89.92 <b>(-78.10%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1357.10 (n/a)</td><td>662.56 (n/a)</td><td>516.70 (n/a)</td><td>297.80 (n/a)</td><td>410.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (+3.06%)</td><td>0.06 <b>(+45.17%)</b></td><td>0.05 <b>(+44.22%)</b></td><td>0.04 <b>(+317.53%)</b></td><td>0.02 <b>(-27.61%)</b></td><td>445.30 <b>(-76.05%)</b></td><td>323.36 <b>(-54.76%)</b></td><td>330.10 <b>(-30.65%)</b></td><td>204.30 (-2.95%)</td><td>103.40 <b>(-84.35%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1859.30 (n/a)</td><td>714.74 (n/a)</td><td>476.00 (n/a)</td><td>210.50 (n/a)</td><td>660.85 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 <b>(+25.09%)</b></td><td>0.04 (-8.07%)</td><td>0.03 <b>(-37.58%)</b></td><td>0.01 <b>(-77.21%)</b></td><td>0.03 <b>(+158.09%)</b></td><td>2464.50 <b>(+338.91%)</b></td><td>826.06 <b>(+108.99%)</b></td><td>560.90 <b>(+60.17%)</b></td><td>225.50 <b>(-20.06%)</b></td><td>934.15 <b>(+759.97%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>561.50 (n/a)</td><td>395.26 (n/a)</td><td>350.20 (n/a)</td><td>282.10 (n/a)</td><td>108.63 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 <b>(-22.49%)</b></td><td>0.04 (-2.99%)</td><td>0.04 <b>(+26.82%)</b></td><td>0.03 (+7.02%)</td><td>0.01 <b>(-36.58%)</b></td><td>560.50 (-6.57%)</td><td>413.56 (-4.76%)</td><td>417.00 <b>(-21.14%)</b></td><td>273.40 <b>(+29.02%)</b></td><td>126.45 <b>(-24.83%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.90 (n/a)</td><td>434.22 (n/a)</td><td>528.80 (n/a)</td><td>211.90 (n/a)</td><td>168.22 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 <b>(+31.54%)</b></td><td>0.04 (+6.74%)</td><td>0.04 (-4.99%)</td><td>0.03 (+1.00%)</td><td>0.01 <b>(+102.73%)</b></td><td>529.30 (-0.99%)</td><td>437.76 (-2.99%)</td><td>459.30 (+5.25%)</td><td>273.60 <b>(-23.98%)</b></td><td>97.82 <b>(+44.70%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>534.60 (n/a)</td><td>451.26 (n/a)</td><td>436.40 (n/a)</td><td>359.90 (n/a)</td><td>67.60 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (-3.70%)</td><td>0.03 (-11.10%)</td><td>0.03 (-2.80%)</td><td>0.02 <b>(-38.42%)</b></td><td>0.01 <b>(+22.03%)</b></td><td>1044.40 <b>(+62.40%)</b></td><td>590.06 <b>(+22.35%)</b></td><td>501.00 (+2.87%)</td><td>323.40 (+3.85%)</td><td>271.17 <b>(+121.14%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>643.10 (n/a)</td><td>482.28 (n/a)</td><td>487.00 (n/a)</td><td>311.40 (n/a)</td><td>122.63 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 <b>(+34.14%)</b></td><td>0.10 (+16.61%)</td><td>0.11 <b>(+32.02%)</b></td><td>0.06 (+0.11%)</td><td>0.03 <b>(+63.70%)</b></td><td>529.00 (-0.11%)</td><td>369.48 (-9.70%)</td><td>310.40 <b>(-24.26%)</b></td><td>224.90 <b>(-25.46%)</b></td><td>130.76 <b>(+30.04%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>529.60 (n/a)</td><td>409.16 (n/a)</td><td>409.80 (n/a)</td><td>301.70 (n/a)</td><td>100.55 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (-2.75%)</td><td>0.09 (+15.19%)</td><td>0.09 <b>(+22.70%)</b></td><td>0.07 (+11.95%)</td><td>0.02 (-8.87%)</td><td>490.70 (-10.67%)</td><td>377.00 (-14.17%)</td><td>350.30 (-18.50%)</td><td>302.90 (+2.82%)</td><td>82.91 (-17.55%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>549.30 (n/a)</td><td>439.22 (n/a)</td><td>429.80 (n/a)</td><td>294.60 (n/a)</td><td>100.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (+1.44%)</td><td>0.08 (+3.13%)</td><td>0.06 (-0.15%)</td><td>0.06 <b>(+258.93%)</b></td><td>0.03 <b>(-35.67%)</b></td><td>529.00 <b>(-72.14%)</b></td><td>466.00 <b>(-35.34%)</b></td><td>510.80 (+0.16%)</td><td>259.20 (-1.44%)</td><td>116.07 <b>(-82.83%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1898.80 (n/a)</td><td>720.74 (n/a)</td><td>510.00 (n/a)</td><td>263.00 (n/a)</td><td>676.19 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (-8.17%)</td><td>0.08 (+5.44%)</td><td>0.07 (+0.46%)</td><td>0.06 (-4.01%)</td><td>0.03 (+2.79%)</td><td>545.00 (+4.19%)</td><td>420.08 (-3.97%)</td><td>476.60 (-0.46%)</td><td>285.00 (+8.90%)</td><td>121.46 (+16.32%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>523.10 (n/a)</td><td>437.44 (n/a)</td><td>478.80 (n/a)</td><td>261.70 (n/a)</td><td>104.42 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.12 (+8.95%)</td><td>0.09 <b>(+38.28%)</b></td><td>0.07 (+13.15%)</td><td>0.07 <b>(+424.39%)</b></td><td>0.03 <b>(-23.03%)</b></td><td>475.30 <b>(-80.93%)</b></td><td>388.58 <b>(-54.54%)</b></td><td>462.70 (-11.61%)</td><td>263.20 (-8.23%)</td><td>107.98 <b>(-88.28%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2492.60 (n/a)</td><td>854.86 (n/a)</td><td>523.50 (n/a)</td><td>286.80 (n/a)</td><td>921.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 <b>(+40.81%)</b></td><td>0.09 <b>(+25.57%)</b></td><td>0.06 (-1.75%)</td><td>0.05 <b>(+203.54%)</b></td><td>0.04 (+18.03%)</td><td>635.30 <b>(-67.06%)</b></td><td>448.24 <b>(-38.38%)</b></td><td>539.90 (+1.79%)</td><td>223.40 <b>(-28.97%)</b></td><td>182.91 <b>(-73.11%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1928.40 (n/a)</td><td>727.44 (n/a)</td><td>530.40 (n/a)</td><td>314.50 (n/a)</td><td>680.14 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.12 (+4.93%)</td><td>0.08 (+1.26%)</td><td>0.07 (+8.83%)</td><td>0.05 (-4.02%)</td><td>0.03 (-1.78%)</td><td>650.50 (+4.20%)</td><td>457.34 (-1.67%)</td><td>493.00 (-8.11%)</td><td>274.30 (-4.72%)</td><td>162.30 (-0.91%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>624.30 (n/a)</td><td>465.10 (n/a)</td><td>536.50 (n/a)</td><td>287.90 (n/a)</td><td>163.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 <b>(-27.30%)</b></td><td>0.08 (-10.16%)</td><td>0.07 (+9.28%)</td><td>0.06 (-0.73%)</td><td>0.03 <b>(-37.02%)</b></td><td>587.50 (+0.72%)</td><td>448.18 (+3.22%)</td><td>474.90 (-8.48%)</td><td>289.50 <b>(+37.53%)</b></td><td>144.65 (-16.50%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>583.30 (n/a)</td><td>434.18 (n/a)</td><td>518.90 (n/a)</td><td>210.50 (n/a)</td><td>173.24 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.12 <b>(+62.84%)</b></td><td>0.07 <b>(+21.87%)</b></td><td>0.06 (+4.15%)</td><td>0.05 (-0.43%)</td><td>0.03 <b>(+262.52%)</b></td><td>617.80 (+0.44%)</td><td>489.98 (-10.94%)</td><td>549.40 (-3.97%)</td><td>279.10 <b>(-38.61%)</b></td><td>148.98 <b>(+130.95%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>615.10 (n/a)</td><td>550.18 (n/a)</td><td>572.10 (n/a)</td><td>454.60 (n/a)</td><td>64.51 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (-3.70%)</td><td>0.09 (-0.67%)</td><td>0.08 <b>(-29.65%)</b></td><td>0.06 <b>(+253.46%)</b></td><td>0.03 <b>(-35.37%)</b></td><td>547.00 <b>(-71.71%)</b></td><td>389.68 <b>(-38.90%)</b></td><td>427.80 <b>(+42.13%)</b></td><td>243.90 (+3.83%)</td><td>127.56 <b>(-82.53%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1933.30 (n/a)</td><td>637.82 (n/a)</td><td>301.00 (n/a)</td><td>234.90 (n/a)</td><td>730.03 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (+3.15%)</td><td>0.09 (+16.85%)</td><td>0.07 (-3.95%)</td><td>0.07 <b>(+302.60%)</b></td><td>0.03 <b>(-35.34%)</b></td><td>482.90 <b>(-75.16%)</b></td><td>405.58 <b>(-43.43%)</b></td><td>447.90 (+4.11%)</td><td>248.40 (-3.04%)</td><td>95.90 <b>(-86.24%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1944.10 (n/a)</td><td>716.98 (n/a)</td><td>430.20 (n/a)</td><td>256.20 (n/a)</td><td>696.95 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 <b>(-34.66%)</b></td><td>0.07 <b>(-35.54%)</b></td><td>0.06 <b>(-51.93%)</b></td><td>0.04 <b>(-20.74%)</b></td><td>0.02 <b>(-47.55%)</b></td><td>805.30 <b>(+26.18%)</b></td><td>545.02 <b>(+40.84%)</b></td><td>567.00 <b>(+108.00%)</b></td><td>315.00 <b>(+53.06%)</b></td><td>184.14 (-6.09%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>638.20 (n/a)</td><td>386.98 (n/a)</td><td>272.60 (n/a)</td><td>205.80 (n/a)</td><td>196.08 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (-1.62%)</td><td>0.01 (-11.94%)</td><td>0.01 (-7.93%)</td><td>0.01 (-19.91%)</td><td>0.00 <b>(+33.41%)</b></td><td>582.80 <b>(+24.85%)</b></td><td>374.22 <b>(+22.70%)</b></td><td>299.60 (+8.63%)</td><td>233.70 (+1.65%)</td><td>162.79 <b>(+67.83%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>466.80 (n/a)</td><td>305.00 (n/a)</td><td>275.80 (n/a)</td><td>229.90 (n/a)</td><td>96.99 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 <b>(+31.02%)</b></td><td>0.02 <b>(+52.63%)</b></td><td>0.02 <b>(+92.88%)</b></td><td>0.01 (-13.35%)</td><td>0.01 <b>(+57.33%)</b></td><td>728.00 (+15.41%)</td><td>368.86 <b>(-28.25%)</b></td><td>287.80 <b>(-48.14%)</b></td><td>233.20 <b>(-23.67%)</b></td><td>202.73 <b>(+59.20%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>630.80 (n/a)</td><td>514.12 (n/a)</td><td>555.00 (n/a)</td><td>305.50 (n/a)</td><td>127.34 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 <b>(-49.38%)</b></td><td>0.01 <b>(-27.60%)</b></td><td>0.01 (-15.43%)</td><td>0.01 (-4.39%)</td><td>0.00 <b>(-68.20%)</b></td><td>595.90 (+4.60%)</td><td>503.90 (+18.55%)</td><td>529.20 (+18.26%)</td><td>321.70 <b>(+97.60%)</b></td><td>107.46 <b>(-31.14%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.70 (n/a)</td><td>425.04 (n/a)</td><td>447.50 (n/a)</td><td>162.80 (n/a)</td><td>156.05 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 <b>(-20.94%)</b></td><td>0.01 (-2.58%)</td><td>0.02 (+4.90%)</td><td>0.01 (+8.36%)</td><td>0.00 <b>(-31.22%)</b></td><td>588.90 (-7.72%)</td><td>375.78 (-4.44%)</td><td>296.30 (-4.67%)</td><td>263.00 <b>(+26.50%)</b></td><td>138.22 <b>(-22.99%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.20 (n/a)</td><td>393.24 (n/a)</td><td>310.80 (n/a)</td><td>207.90 (n/a)</td><td>179.49 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 (-15.39%)</td><td>0.01 (-4.37%)</td><td>0.01 (+2.18%)</td><td>0.01 (-5.06%)</td><td>0.00 (-19.21%)</td><td>568.30 (+5.34%)</td><td>434.04 (+3.84%)</td><td>416.80 (-2.11%)</td><td>286.70 (+18.18%)</td><td>121.21 (+10.74%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.50 (n/a)</td><td>418.00 (n/a)</td><td>425.80 (n/a)</td><td>242.60 (n/a)</td><td>109.46 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 <b>(-26.08%)</b></td><td>0.02 <b>(+21.81%)</b></td><td>0.02 <b>(+112.40%)</b></td><td>0.01 <b>(+38.61%)</b></td><td>0.00 <b>(-53.09%)</b></td><td>431.20 <b>(-27.86%)</b></td><td>288.38 <b>(-32.34%)</b></td><td>251.40 <b>(-52.92%)</b></td><td>214.40 <b>(+35.27%)</b></td><td>87.35 <b>(-54.60%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.70 (n/a)</td><td>426.22 (n/a)</td><td>534.00 (n/a)</td><td>158.50 (n/a)</td><td>192.39 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 <b>(+30.68%)</b></td><td>0.01 (+12.10%)</td><td>0.01 (+1.56%)</td><td>0.01 (+3.24%)</td><td>0.01 <b>(+50.38%)</b></td><td>544.20 (-3.13%)</td><td>402.26 (-5.81%)</td><td>469.50 (-1.53%)</td><td>212.80 <b>(-23.45%)</b></td><td>147.11 (+15.44%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>561.80 (n/a)</td><td>427.06 (n/a)</td><td>476.80 (n/a)</td><td>278.00 (n/a)</td><td>127.44 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (-1.02%)</td><td>0.01 (-0.09%)</td><td>0.01 (+13.97%)</td><td>0.01 (-16.35%)</td><td>0.00 (+11.26%)</td><td>655.10 (+19.54%)</td><td>465.24 (+4.51%)</td><td>399.20 (-12.26%)</td><td>257.50 (+1.02%)</td><td>172.04 <b>(+46.54%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.00 (n/a)</td><td>445.18 (n/a)</td><td>455.00 (n/a)</td><td>254.90 (n/a)</td><td>117.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 <b>(-36.05%)</b></td><td>0.01 <b>(-30.35%)</b></td><td>0.01 <b>(-36.67%)</b></td><td>0.01 (-11.72%)</td><td>0.00 <b>(-62.91%)</b></td><td>524.40 (+13.29%)</td><td>447.36 <b>(+34.17%)</b></td><td>441.30 <b>(+57.89%)</b></td><td>345.00 <b>(+56.39%)</b></td><td>69.49 <b>(-38.33%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>462.90 (n/a)</td><td>333.42 (n/a)</td><td>279.50 (n/a)</td><td>220.60 (n/a)</td><td>112.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.01 <b>(-22.51%)</b></td><td>0.01 (-19.31%)</td><td>0.01 <b>(-32.76%)</b></td><td>0.01 <b>(+61.32%)</b></td><td>0.00 <b>(-61.21%)</b></td><td>642.60 <b>(-38.01%)</b></td><td>506.02 (+4.28%)</td><td>516.90 <b>(+48.71%)</b></td><td>417.20 <b>(+29.04%)</b></td><td>91.08 <b>(-70.58%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1036.70 (n/a)</td><td>485.24 (n/a)</td><td>347.60 (n/a)</td><td>323.30 (n/a)</td><td>309.58 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.02 (-1.92%)</td><td>0.01 (+1.99%)</td><td>0.01 (+15.60%)</td><td>0.01 (+7.11%)</td><td>0.00 (-11.88%)</td><td>514.80 (-6.64%)</td><td>399.18 (-3.99%)</td><td>415.80 (-13.48%)</td><td>270.60 (+1.96%)</td><td>113.70 (-13.27%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.40 (n/a)</td><td>415.78 (n/a)</td><td>480.60 (n/a)</td><td>265.40 (n/a)</td><td>131.09 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (+1.61%)</td><td>0.02 (+1.86%)</td><td>0.02 (+0.50%)</td><td>0.02 (+5.19%)</td><td>0.01 (-3.17%)</td><td>500.40 (-4.94%)</td><td>388.04 (-3.01%)</td><td>443.90 (-0.49%)</td><td>232.10 (-1.61%)</td><td>117.11 (-9.74%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.40 (n/a)</td><td>400.10 (n/a)</td><td>446.10 (n/a)</td><td>235.90 (n/a)</td><td>129.75 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (-5.81%)</td><td>0.03 (+15.84%)</td><td>0.03 (+15.02%)</td><td>0.02 (+7.13%)</td><td>0.01 (-11.34%)</td><td>540.80 (-6.65%)</td><td>402.34 (-15.03%)</td><td>431.10 (-13.07%)</td><td>282.90 (+6.19%)</td><td>108.79 (-11.13%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>579.30 (n/a)</td><td>473.50 (n/a)</td><td>495.90 (n/a)</td><td>266.40 (n/a)</td><td>122.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 <b>(+31.81%)</b></td><td>0.02 (+17.13%)</td><td>0.02 (+19.28%)</td><td>0.01 (+6.34%)</td><td>0.01 <b>(+31.94%)</b></td><td>784.60 (-5.96%)</td><td>427.78 (-11.23%)</td><td>351.70 (-16.16%)</td><td>200.70 <b>(-24.15%)</b></td><td>230.36 (-2.10%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>834.30 (n/a)</td><td>481.88 (n/a)</td><td>419.50 (n/a)</td><td>264.60 (n/a)</td><td>235.30 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 <b>(-23.83%)</b></td><td>0.02 (-15.38%)</td><td>0.02 (+10.74%)</td><td>0.02 (-14.46%)</td><td>0.01 <b>(-41.06%)</b></td><td>636.70 (+16.91%)</td><td>455.56 (+11.13%)</td><td>445.70 (-9.69%)</td><td>293.10 <b>(+31.32%)</b></td><td>129.63 (-11.94%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.60 (n/a)</td><td>409.92 (n/a)</td><td>493.50 (n/a)</td><td>223.20 (n/a)</td><td>147.21 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 <b>(+25.70%)</b></td><td>0.03 <b>(+51.15%)</b></td><td>0.03 <b>(+72.14%)</b></td><td>0.02 <b>(+22.68%)</b></td><td>0.01 (+17.11%)</td><td>453.30 (-18.50%)</td><td>290.42 <b>(-34.29%)</b></td><td>274.10 <b>(-41.90%)</b></td><td>217.80 <b>(-20.42%)</b></td><td>94.41 <b>(-22.80%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.20 (n/a)</td><td>442.00 (n/a)</td><td>471.80 (n/a)</td><td>273.70 (n/a)</td><td>122.30 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 (+7.26%)</td><td>0.03 (+11.91%)</td><td>0.02 (+12.05%)</td><td>0.02 <b>(+139.17%)</b></td><td>0.01 (-12.89%)</td><td>572.00 <b>(-58.18%)</b></td><td>411.48 <b>(-28.88%)</b></td><td>432.70 (-10.75%)</td><td>219.60 (-6.75%)</td><td>149.44 <b>(-67.23%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1367.90 (n/a)</td><td>578.54 (n/a)</td><td>484.80 (n/a)</td><td>235.50 (n/a)</td><td>455.96 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 <b>(+22.55%)</b></td><td>0.02 <b>(+41.89%)</b></td><td>0.02 <b>(+23.87%)</b></td><td>0.02 <b>(+105.92%)</b></td><td>0.01 (+12.67%)</td><td>542.70 <b>(-51.44%)</b></td><td>404.64 <b>(-35.29%)</b></td><td>450.10 (-19.26%)</td><td>221.00 (-18.39%)</td><td>147.44 <b>(-53.59%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1117.50 (n/a)</td><td>625.30 (n/a)</td><td>557.50 (n/a)</td><td>270.80 (n/a)</td><td>317.69 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 <b>(+47.54%)</b></td><td>0.03 <b>(+52.02%)</b></td><td>0.02 <b>(+40.68%)</b></td><td>0.01 (-0.19%)</td><td>0.01 <b>(+126.92%)</b></td><td>643.40 (+0.19%)</td><td>378.58 <b>(-28.32%)</b></td><td>376.20 <b>(-28.92%)</b></td><td>244.70 <b>(-32.22%)</b></td><td>161.94 <b>(+54.53%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>642.20 (n/a)</td><td>528.16 (n/a)</td><td>529.30 (n/a)</td><td>361.00 (n/a)</td><td>104.80 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (+2.29%)</td><td>0.02 (-13.44%)</td><td>0.01 (-6.74%)</td><td>0.01 (-7.91%)</td><td>0.01 (-2.24%)</td><td>636.00 (+8.59%)</td><td>504.18 (+15.83%)</td><td>553.60 (+7.22%)</td><td>262.10 (-2.24%)</td><td>156.48 (+7.06%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.70 (n/a)</td><td>435.28 (n/a)</td><td>516.30 (n/a)</td><td>268.10 (n/a)</td><td>146.16 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.04 (+19.52%)</td><td>0.03 <b>(+20.68%)</b></td><td>0.02 (-1.93%)</td><td>0.02 (+12.86%)</td><td>0.01 <b>(+64.43%)</b></td><td>606.30 (-11.40%)</td><td>413.04 (-11.40%)</td><td>479.60 (+1.98%)</td><td>240.50 (-16.35%)</td><td>162.46 (+13.47%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>684.30 (n/a)</td><td>466.16 (n/a)</td><td>470.30 (n/a)</td><td>287.50 (n/a)</td><td>143.17 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.03 (+3.83%)</td><td>0.02 (-11.75%)</td><td>0.02 (-5.27%)</td><td>0.01 <b>(-51.34%)</b></td><td>0.01 <b>(+27.09%)</b></td><td>1082.80 <b>(+105.50%)</b></td><td>551.50 <b>(+31.94%)</b></td><td>523.00 (+5.57%)</td><td>235.10 (-3.69%)</td><td>323.21 <b>(+145.95%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.90 (n/a)</td><td>417.98 (n/a)</td><td>495.40 (n/a)</td><td>244.10 (n/a)</td><td>131.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (-1.84%)</td><td>0.05 (+19.17%)</td><td>0.06 <b>(+69.47%)</b></td><td>0.02 <b>(-20.13%)</b></td><td>0.01 (-0.63%)</td><td>656.20 <b>(+25.21%)</b></td><td>362.50 (-14.08%)</td><td>295.60 <b>(-41.00%)</b></td><td>267.20 (+1.87%)</td><td>164.79 <b>(+30.09%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>524.10 (n/a)</td><td>421.90 (n/a)</td><td>501.00 (n/a)</td><td>262.30 (n/a)</td><td>126.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 (+5.51%)</td><td>0.07 (-8.23%)</td><td>0.08 (-3.11%)</td><td>0.04 (-5.70%)</td><td>0.02 (+18.02%)</td><td>625.30 (+6.05%)</td><td>384.20 (+11.92%)</td><td>294.90 (+3.22%)</td><td>254.50 (-5.25%)</td><td>157.20 (+13.97%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>589.60 (n/a)</td><td>343.28 (n/a)</td><td>285.70 (n/a)</td><td>268.60 (n/a)</td><td>137.94 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 <b>(+54.75%)</b></td><td>0.04 (+10.12%)</td><td>0.03 (-10.81%)</td><td>0.01 <b>(-71.97%)</b></td><td>0.03 <b>(+304.74%)</b></td><td>1871.60 <b>(+256.77%)</b></td><td>683.04 <b>(+56.15%)</b></td><td>515.20 (+12.12%)</td><td>216.50 <b>(-35.37%)</b></td><td>682.18 <b>(+842.21%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>524.60 (n/a)</td><td>437.42 (n/a)</td><td>459.50 (n/a)</td><td>335.00 (n/a)</td><td>72.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 <b>(+43.02%)</b></td><td>0.06 <b>(+41.21%)</b></td><td>0.06 <b>(+74.08%)</b></td><td>0.03 (-16.81%)</td><td>0.03 <b>(+71.04%)</b></td><td>714.80 <b>(+20.22%)</b></td><td>396.44 <b>(-21.57%)</b></td><td>323.40 <b>(-42.56%)</b></td><td>194.90 <b>(-30.09%)</b></td><td>198.59 <b>(+51.99%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>594.60 (n/a)</td><td>505.46 (n/a)</td><td>563.00 (n/a)</td><td>278.80 (n/a)</td><td>130.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (+14.96%)</td><td>0.05 <b>(+21.38%)</b></td><td>0.06 <b>(+46.77%)</b></td><td>0.03 (-4.61%)</td><td>0.02 <b>(+33.20%)</b></td><td>544.90 (+4.83%)</td><td>338.82 (-14.64%)</td><td>273.60 <b>(-31.87%)</b></td><td>237.60 (-13.03%)</td><td>131.29 (+18.78%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>519.80 (n/a)</td><td>396.92 (n/a)</td><td>401.60 (n/a)</td><td>273.20 (n/a)</td><td>110.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 <b>(+36.06%)</b></td><td>0.05 (-6.52%)</td><td>0.04 (-18.31%)</td><td>0.03 <b>(-32.99%)</b></td><td>0.03 <b>(+166.07%)</b></td><td>672.20 <b>(+49.21%)</b></td><td>495.96 <b>(+21.55%)</b></td><td>522.00 <b>(+22.42%)</b></td><td>220.30 <b>(-26.49%)</b></td><td>168.54 <b>(+173.24%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>450.50 (n/a)</td><td>408.04 (n/a)</td><td>426.40 (n/a)</td><td>299.70 (n/a)</td><td>61.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (-10.19%)</td><td>0.04 (+5.39%)</td><td>0.04 (+12.47%)</td><td>0.03 (-3.06%)</td><td>0.01 <b>(-25.55%)</b></td><td>614.70 (+3.15%)</td><td>426.16 (-8.30%)</td><td>400.30 (-11.08%)</td><td>283.30 (+11.36%)</td><td>120.75 (-14.35%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>595.90 (n/a)</td><td>464.74 (n/a)</td><td>450.20 (n/a)</td><td>254.40 (n/a)</td><td>140.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 <b>(-32.91%)</b></td><td>0.04 (-7.58%)</td><td>0.04 (+6.10%)</td><td>0.03 (-5.33%)</td><td>0.01 <b>(-43.89%)</b></td><td>625.40 (+5.62%)</td><td>466.00 (+1.01%)</td><td>460.50 (-5.73%)</td><td>299.70 <b>(+49.03%)</b></td><td>148.34 (-4.90%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>592.10 (n/a)</td><td>461.32 (n/a)</td><td>488.50 (n/a)</td><td>201.10 (n/a)</td><td>155.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 <b>(-23.17%)</b></td><td>0.04 (-7.82%)</td><td>0.03 (+1.47%)</td><td>0.03 (+0.97%)</td><td>0.02 <b>(-24.55%)</b></td><td>629.90 (-0.96%)</td><td>441.58 (+3.41%)</td><td>495.20 (-1.45%)</td><td>243.40 <b>(+30.16%)</b></td><td>176.71 (-4.35%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>636.00 (n/a)</td><td>427.02 (n/a)</td><td>502.50 (n/a)</td><td>187.00 (n/a)</td><td>184.75 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 <b>(-26.56%)</b></td><td>0.05 (-6.01%)</td><td>0.04 (-1.31%)</td><td>0.03 <b>(-21.01%)</b></td><td>0.02 <b>(-23.23%)</b></td><td>590.30 <b>(+26.59%)</b></td><td>411.86 (+5.80%)</td><td>453.20 (+1.34%)</td><td>266.60 <b>(+36.23%)</b></td><td>141.75 <b>(+23.22%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>466.30 (n/a)</td><td>389.30 (n/a)</td><td>447.20 (n/a)</td><td>195.70 (n/a)</td><td>115.03 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 (+12.29%)</td><td>0.04 (-1.22%)</td><td>0.04 (-7.66%)</td><td>0.03 (+8.81%)</td><td>0.01 (+17.28%)</td><td>601.50 (-8.10%)</td><td>419.24 (+2.38%)</td><td>366.30 (+8.31%)</td><td>280.30 (-10.96%)</td><td>141.49 (-1.78%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>654.50 (n/a)</td><td>409.48 (n/a)</td><td>338.20 (n/a)</td><td>314.80 (n/a)</td><td>144.05 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (+11.02%)</td><td>0.09 (+4.42%)</td><td>0.11 <b>(+33.29%)</b></td><td>0.03 <b>(-38.03%)</b></td><td>0.04 <b>(+52.82%)</b></td><td>1092.00 <b>(+61.35%)</b></td><td>487.56 (+17.68%)</td><td>291.50 <b>(-24.97%)</b></td><td>251.50 (-9.92%)</td><td>358.28 <b>(+120.97%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>676.80 (n/a)</td><td>414.32 (n/a)</td><td>388.50 (n/a)</td><td>279.20 (n/a)</td><td>162.14 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (-3.53%)</td><td>0.09 (-3.85%)</td><td>0.08 (+8.79%)</td><td>0.05 (-10.67%)</td><td>0.03 (-1.00%)</td><td>627.30 (+11.96%)</td><td>422.08 (+5.46%)</td><td>399.40 (-8.08%)</td><td>250.50 (+3.64%)</td><td>153.92 (+17.72%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>560.30 (n/a)</td><td>400.24 (n/a)</td><td>434.50 (n/a)</td><td>241.70 (n/a)</td><td>130.76 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.19 <b>(+53.52%)</b></td><td>0.10 (+16.15%)</td><td>0.07 (-8.21%)</td><td>0.07 (+8.88%)</td><td>0.05 <b>(+117.23%)</b></td><td>603.20 (-8.16%)</td><td>489.96 (-5.96%)</td><td>567.90 (+8.96%)</td><td>220.10 <b>(-34.86%)</b></td><td>156.53 <b>(+26.11%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>656.80 (n/a)</td><td>521.00 (n/a)</td><td>521.20 (n/a)</td><td>337.90 (n/a)</td><td>124.11 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.17 <b>(+30.85%)</b></td><td>0.09 (+2.17%)</td><td>0.06 <b>(-27.99%)</b></td><td>0.06 (-9.06%)</td><td>0.05 <b>(+71.62%)</b></td><td>574.30 (+9.96%)</td><td>430.32 (+8.35%)</td><td>536.20 <b>(+38.88%)</b></td><td>198.50 <b>(-23.57%)</b></td><td>172.09 <b>(+45.39%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>522.30 (n/a)</td><td>397.14 (n/a)</td><td>386.10 (n/a)</td><td>259.70 (n/a)</td><td>118.37 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.16 <b>(+20.80%)</b></td><td>0.10 (+3.74%)</td><td>0.09 (+4.40%)</td><td>0.06 <b>(-27.03%)</b></td><td>0.04 <b>(+75.40%)</b></td><td>732.20 <b>(+37.04%)</b></td><td>484.96 (+5.93%)</td><td>444.10 (-4.21%)</td><td>252.10 (-17.21%)</td><td>188.81 <b>(+103.35%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>534.30 (n/a)</td><td>457.82 (n/a)</td><td>463.60 (n/a)</td><td>304.50 (n/a)</td><td>92.85 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 (+6.30%)</td><td>0.08 (-14.85%)</td><td>0.06 <b>(-26.98%)</b></td><td>0.05 (+16.67%)</td><td>0.04 (-3.40%)</td><td>601.00 (-14.29%)</td><td>460.82 (+13.47%)</td><td>509.80 <b>(+36.93%)</b></td><td>232.40 (-5.91%)</td><td>141.03 <b>(-23.96%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>701.20 (n/a)</td><td>406.10 (n/a)</td><td>372.30 (n/a)</td><td>247.00 (n/a)</td><td>185.46 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 <b>(-22.37%)</b></td><td>0.09 (-0.08%)</td><td>0.09 <b>(+31.25%)</b></td><td>0.06 (-4.51%)</td><td>0.03 <b>(-38.77%)</b></td><td>665.70 (+4.74%)</td><td>464.68 (-6.33%)</td><td>424.20 <b>(-23.81%)</b></td><td>292.90 <b>(+28.80%)</b></td><td>142.19 (-14.48%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>635.60 (n/a)</td><td>496.10 (n/a)</td><td>556.80 (n/a)</td><td>227.40 (n/a)</td><td>166.26 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.11 (+19.13%)</td><td>0.08 <b>(+24.32%)</b></td><td>0.07 <b>(+28.13%)</b></td><td>0.05 (-2.05%)</td><td>0.03 <b>(+52.68%)</b></td><td>643.30 (+2.09%)</td><td>450.16 (-15.92%)</td><td>450.90 <b>(-21.96%)</b></td><td>290.60 (-16.06%)</td><td>149.64 <b>(+30.14%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>630.10 (n/a)</td><td>535.40 (n/a)</td><td>577.80 (n/a)</td><td>346.20 (n/a)</td><td>114.99 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 <b>(-21.27%)</b></td><td>0.09 (-8.32%)</td><td>0.09 (+6.49%)</td><td>0.07 <b>(+33.09%)</b></td><td>0.02 <b>(-47.74%)</b></td><td>521.50 <b>(-24.87%)</b></td><td>431.22 (-1.80%)</td><td>431.20 (-6.10%)</td><td>293.90 <b>(+27.01%)</b></td><td>94.04 <b>(-48.25%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>694.10 (n/a)</td><td>439.12 (n/a)</td><td>459.20 (n/a)</td><td>231.40 (n/a)</td><td>181.74 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (-15.58%)</td><td>0.07 (+16.39%)</td><td>0.07 (+16.49%)</td><td>0.06 <b>(+248.93%)</b></td><td>0.01 <b>(-78.07%)</b></td><td>565.70 <b>(-71.34%)</b></td><td>493.06 <b>(-38.25%)</b></td><td>469.20 (-14.14%)</td><td>453.00 (+18.46%)</td><td>45.79 <b>(-93.12%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1973.90 (n/a)</td><td>798.48 (n/a)</td><td>546.50 (n/a)</td><td>382.40 (n/a)</td><td>665.17 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (-14.60%)</td><td>0.06 (-8.97%)</td><td>0.07 (+12.89%)</td><td>0.03 (-13.22%)</td><td>0.03 (-15.37%)</td><td>589.10 (+15.24%)</td><td>380.84 (+9.57%)</td><td>276.80 (-11.40%)</td><td>220.40 (+17.11%)</td><td>171.28 (+14.60%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>511.20 (n/a)</td><td>347.58 (n/a)</td><td>312.40 (n/a)</td><td>188.20 (n/a)</td><td>149.46 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 <b>(-28.00%)</b></td><td>0.06 (-2.66%)</td><td>0.06 (+9.61%)</td><td>0.04 (-13.81%)</td><td>0.02 <b>(-35.52%)</b></td><td>573.40 (+16.00%)</td><td>374.38 (-0.50%)</td><td>327.00 (-8.76%)</td><td>276.80 <b>(+38.89%)</b></td><td>123.12 (+4.25%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>494.30 (n/a)</td><td>376.28 (n/a)</td><td>358.40 (n/a)</td><td>199.30 (n/a)</td><td>118.10 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.05 <b>(-39.09%)</b></td><td>0.04 <b>(-35.86%)</b></td><td>0.04 <b>(-42.28%)</b></td><td>0.03 <b>(+201.98%)</b></td><td>0.01 <b>(-72.89%)</b></td><td>657.10 <b>(-66.89%)</b></td><td>517.32 (-15.79%)</td><td>514.00 <b>(+73.30%)</b></td><td>375.20 <b>(+64.20%)</b></td><td>103.80 <b>(-86.47%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1984.40 (n/a)</td><td>614.34 (n/a)</td><td>296.60 (n/a)</td><td>228.50 (n/a)</td><td>767.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (-5.07%)</td><td>0.06 (-19.86%)</td><td>0.06 <b>(-20.78%)</b></td><td>0.03 <b>(-35.77%)</b></td><td>0.02 <b>(+45.55%)</b></td><td>678.70 <b>(+55.70%)</b></td><td>416.70 <b>(+38.46%)</b></td><td>337.00 <b>(+26.22%)</b></td><td>255.60 (+5.36%)</td><td>188.05 <b>(+133.02%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>435.90 (n/a)</td><td>300.96 (n/a)</td><td>267.00 (n/a)</td><td>242.60 (n/a)</td><td>80.70 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (-6.08%)</td><td>0.06 (-0.51%)</td><td>0.05 (+11.54%)</td><td>0.05 <b>(+25.95%)</b></td><td>0.01 <b>(-40.31%)</b></td><td>437.40 <b>(-20.59%)</b></td><td>382.44 (-6.38%)</td><td>408.70 (-10.35%)</td><td>267.90 (+6.48%)</td><td>70.03 <b>(-48.88%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>550.80 (n/a)</td><td>408.52 (n/a)</td><td>455.90 (n/a)</td><td>251.60 (n/a)</td><td>136.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (-8.59%)</td><td>0.06 (-10.01%)</td><td>0.07 (-0.25%)</td><td>0.03 (-15.06%)</td><td>0.02 (+6.51%)</td><td>636.50 (+17.74%)</td><td>397.30 (+15.98%)</td><td>296.80 (+0.27%)</td><td>251.50 (+9.40%)</td><td>173.55 <b>(+36.78%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>540.60 (n/a)</td><td>342.56 (n/a)</td><td>296.00 (n/a)</td><td>229.90 (n/a)</td><td>126.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (+7.09%)</td><td>0.05 <b>(-20.92%)</b></td><td>0.05 <b>(-27.63%)</b></td><td>0.01 <b>(-60.09%)</b></td><td>0.03 <b>(+37.64%)</b></td><td>1956.10 <b>(+150.53%)</b></td><td>765.86 <b>(+73.81%)</b></td><td>533.10 <b>(+38.18%)</b></td><td>269.00 (-6.63%)</td><td>684.40 <b>(+241.13%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>780.80 (n/a)</td><td>440.62 (n/a)</td><td>385.80 (n/a)</td><td>288.10 (n/a)</td><td>200.63 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (-19.98%)</td><td>0.06 (-15.37%)</td><td>0.05 (-3.09%)</td><td>0.04 (-11.83%)</td><td>0.01 <b>(-35.96%)</b></td><td>601.80 (+13.42%)</td><td>460.54 (+14.64%)</td><td>459.90 (+3.19%)</td><td>326.90 <b>(+24.96%)</b></td><td>105.84 (-8.16%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>530.60 (n/a)</td><td>401.74 (n/a)</td><td>445.70 (n/a)</td><td>261.60 (n/a)</td><td>115.25 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (-11.35%)</td><td>0.06 <b>(-23.97%)</b></td><td>0.05 <b>(-35.26%)</b></td><td>0.04 (-19.75%)</td><td>0.02 <b>(+20.75%)</b></td><td>599.50 <b>(+24.61%)</b></td><td>438.44 <b>(+38.70%)</b></td><td>458.50 <b>(+54.48%)</b></td><td>265.90 (+12.81%)</td><td>154.42 <b>(+61.06%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>481.10 (n/a)</td><td>316.10 (n/a)</td><td>296.80 (n/a)</td><td>235.70 (n/a)</td><td>95.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (-6.69%)</td><td>0.06 (-1.66%)</td><td>0.05 (-6.28%)</td><td>0.04 (-2.39%)</td><td>0.02 (-7.08%)</td><td>574.90 (+2.44%)</td><td>419.46 (+0.82%)</td><td>450.30 (+6.68%)</td><td>293.40 (+7.16%)</td><td>122.99 (-4.07%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>561.20 (n/a)</td><td>416.06 (n/a)</td><td>422.10 (n/a)</td><td>273.80 (n/a)</td><td>128.21 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 <b>(-43.06%)</b></td><td>0.05 <b>(-37.61%)</b></td><td>0.05 <b>(-50.35%)</b></td><td>0.04 (+11.00%)</td><td>0.01 <b>(-79.43%)</b></td><td>590.20 (-9.91%)</td><td>534.96 <b>(+38.77%)</b></td><td>537.60 <b>(+101.42%)</b></td><td>436.40 <b>(+75.61%)</b></td><td>61.62 <b>(-66.30%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>655.10 (n/a)</td><td>385.50 (n/a)</td><td>266.90 (n/a)</td><td>248.50 (n/a)</td><td>182.86 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 (+10.64%)</td><td>0.07 (+18.55%)</td><td>0.06 (+7.05%)</td><td>0.04 (+6.57%)</td><td>0.02 <b>(+40.98%)</b></td><td>571.40 (-6.16%)</td><td>401.84 (-12.41%)</td><td>411.10 (-6.59%)</td><td>263.60 (-9.60%)</td><td>137.24 (+14.68%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>608.90 (n/a)</td><td>458.80 (n/a)</td><td>440.10 (n/a)</td><td>291.60 (n/a)</td><td>119.67 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 (-1.14%)</td><td>0.06 (+7.70%)</td><td>0.07 (+17.67%)</td><td>0.04 (+19.52%)</td><td>0.02 (-14.70%)</td><td>486.20 (-16.35%)</td><td>326.78 (-11.63%)</td><td>268.90 (-15.01%)</td><td>229.90 (+1.14%)</td><td>114.45 <b>(-27.15%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>581.20 (n/a)</td><td>369.78 (n/a)</td><td>316.40 (n/a)</td><td>227.30 (n/a)</td><td>157.10 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (-3.00%)</td><td>0.05 (-3.08%)</td><td>0.05 <b>(-22.47%)</b></td><td>0.03 (-6.28%)</td><td>0.02 (-13.07%)</td><td>551.40 (+6.70%)</td><td>364.36 (+0.94%)</td><td>365.50 <b>(+28.97%)</b></td><td>254.30 (+3.12%)</td><td>118.72 (-9.25%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>516.80 (n/a)</td><td>360.96 (n/a)</td><td>283.40 (n/a)</td><td>246.60 (n/a)</td><td>130.82 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 <b>(-21.43%)</b></td><td>0.03 <b>(-50.08%)</b></td><td>0.03 <b>(-52.58%)</b></td><td>0.01 <b>(-70.58%)</b></td><td>0.02 <b>(+24.69%)</b></td><td>1956.90 <b>(+239.86%)</b></td><td>1030.94 <b>(+213.28%)</b></td><td>590.40 <b>(+110.86%)</b></td><td>282.80 <b>(+27.27%)</b></td><td>808.22 <b>(+474.96%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>575.80 (n/a)</td><td>329.08 (n/a)</td><td>280.00 (n/a)</td><td>222.20 (n/a)</td><td>140.57 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (+1.57%)</td><td>0.04 (-17.13%)</td><td>0.04 <b>(-32.09%)</b></td><td>0.02 <b>(-44.23%)</b></td><td>0.02 (-4.73%)</td><td>1114.40 <b>(+79.31%)</b></td><td>536.72 <b>(+30.21%)</b></td><td>425.50 <b>(+47.28%)</b></td><td>270.70 (-1.53%)</td><td>332.54 <b>(+83.94%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>621.50 (n/a)</td><td>412.20 (n/a)</td><td>288.90 (n/a)</td><td>274.90 (n/a)</td><td>180.78 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.06 <b>(-23.27%)</b></td><td>0.04 <b>(-25.06%)</b></td><td>0.04 <b>(-34.26%)</b></td><td>0.03 (+3.08%)</td><td>0.01 <b>(-41.93%)</b></td><td>570.30 (-2.98%)</td><td>451.66 <b>(+24.44%)</b></td><td>483.50 <b>(+52.09%)</b></td><td>290.40 <b>(+30.34%)</b></td><td>105.84 <b>(-29.02%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>587.80 (n/a)</td><td>362.96 (n/a)</td><td>317.90 (n/a)</td><td>222.80 (n/a)</td><td>149.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.08 <b>(+23.74%)</b></td><td>0.05 <b>(+31.10%)</b></td><td>0.04 (-1.91%)</td><td>0.04 <b>(+244.86%)</b></td><td>0.02 (-4.92%)</td><td>500.80 <b>(-71.00%)</b></td><td>400.82 <b>(-42.65%)</b></td><td>454.90 (+1.95%)</td><td>217.30 (-19.19%)</td><td>116.77 <b>(-80.14%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1727.10 (n/a)</td><td>698.94 (n/a)</td><td>446.20 (n/a)</td><td>268.90 (n/a)</td><td>588.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.33 (-10.41%)</td><td>0.26 (-2.63%)</td><td>0.24 (-19.80%)</td><td>0.23 <b>(+43.28%)</b></td><td>0.04 <b>(-58.80%)</b></td><td>432.40 <b>(-30.21%)</b></td><td>382.98 (-8.14%)</td><td>402.90 <b>(+24.70%)</b></td><td>302.20 (+11.60%)</td><td>54.21 <b>(-68.58%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.30 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>619.60 (n/a)</td><td>416.90 (n/a)</td><td>323.10 (n/a)</td><td>270.80 (n/a)</td><td>172.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.41 (+15.11%)</td><td>0.29 (+5.67%)</td><td>0.27 (-13.64%)</td><td>0.18 (+19.39%)</td><td>0.11 (+15.87%)</td><td>531.90 (-16.24%)</td><td>381.00 (-5.22%)</td><td>361.70 (+15.78%)</td><td>242.40 (-13.12%)</td><td>140.19 (-12.32%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.31 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>635.00 (n/a)</td><td>402.00 (n/a)</td><td>312.40 (n/a)</td><td>279.00 (n/a)</td><td>159.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.39 (+9.90%)</td><td>0.28 (+8.47%)</td><td>0.25 (+16.75%)</td><td>0.21 (+17.65%)</td><td>0.08 (-2.06%)</td><td>468.20 (-15.00%)</td><td>371.00 (-9.19%)</td><td>390.80 (-14.34%)</td><td>253.90 (-9.00%)</td><td>99.35 (-18.29%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>550.80 (n/a)</td><td>408.54 (n/a)</td><td>456.20 (n/a)</td><td>279.00 (n/a)</td><td>121.60 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.28 <b>(+44.60%)</b></td><td>0.20 <b>(+37.20%)</b></td><td>0.21 <b>(+51.35%)</b></td><td>0.13 <b>(+24.33%)</b></td><td>0.06 <b>(+66.84%)</b></td><td>551.00 (-19.56%)</td><td>405.76 <b>(-25.13%)</b></td><td>359.10 <b>(-33.93%)</b></td><td>261.60 <b>(-30.85%)</b></td><td>122.23 (-4.60%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>685.00 (n/a)</td><td>541.96 (n/a)</td><td>543.50 (n/a)</td><td>378.30 (n/a)</td><td>128.13 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.30 (+7.00%)</td><td>0.21 (+18.79%)</td><td>0.19 (+16.95%)</td><td>0.12 (+1.55%)</td><td>0.07 (+7.56%)</td><td>600.10 (-1.53%)</td><td>395.22 (-15.44%)</td><td>393.60 (-14.49%)</td><td>243.50 (-6.56%)</td><td>138.51 (-1.77%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>609.40 (n/a)</td><td>467.40 (n/a)</td><td>460.30 (n/a)</td><td>260.60 (n/a)</td><td>141.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.29 <b>(+64.99%)</b></td><td>0.23 <b>(+48.02%)</b></td><td>0.25 <b>(+57.71%)</b></td><td>0.16 <b>(+24.47%)</b></td><td>0.06 <b>(+253.91%)</b></td><td>463.40 (-19.66%)</td><td>341.00 <b>(-29.01%)</b></td><td>293.20 <b>(-36.59%)</b></td><td>258.20 <b>(-39.38%)</b></td><td>96.16 <b>(+67.92%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>576.80 (n/a)</td><td>480.34 (n/a)</td><td>462.40 (n/a)</td><td>425.90 (n/a)</td><td>57.27 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (-9.47%)</td><td>0.12 (+9.96%)</td><td>0.14 <b>(+21.32%)</b></td><td>0.08 <b>(+39.25%)</b></td><td>0.03 <b>(-29.26%)</b></td><td>488.80 <b>(-28.18%)</b></td><td>323.74 (-17.00%)</td><td>272.30 (-17.56%)</td><td>247.60 (+10.44%)</td><td>102.43 <b>(-44.74%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>680.60 (n/a)</td><td>390.04 (n/a)</td><td>330.30 (n/a)</td><td>224.20 (n/a)</td><td>185.36 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (-5.41%)</td><td>0.10 (+11.49%)</td><td>0.11 <b>(+63.82%)</b></td><td>0.06 (-4.67%)</td><td>0.03 (-16.81%)</td><td>658.40 (+4.89%)</td><td>397.22 (-12.89%)</td><td>334.30 <b>(-38.95%)</b></td><td>273.60 (+5.72%)</td><td>158.73 (-5.81%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>627.70 (n/a)</td><td>456.00 (n/a)</td><td>547.60 (n/a)</td><td>258.80 (n/a)</td><td>168.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.09 <b>(-42.35%)</b></td><td>0.06 <b>(-42.10%)</b></td><td>0.08 <b>(-27.08%)</b></td><td>0.01 <b>(-79.06%)</b></td><td>0.03 (-19.85%)</td><td>2464.20 <b>(+377.56%)</b></td><td>882.70 <b>(+143.84%)</b></td><td>468.40 <b>(+37.16%)</b></td><td>423.10 <b>(+73.47%)</b></td><td>886.71 <b>(+628.27%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>516.00 (n/a)</td><td>362.00 (n/a)</td><td>341.50 (n/a)</td><td>243.90 (n/a)</td><td>121.75 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 (-18.02%)</td><td>0.09 (-11.24%)</td><td>0.08 (-4.05%)</td><td>0.06 (+11.64%)</td><td>0.03 <b>(-39.58%)</b></td><td>602.80 (-10.43%)</td><td>453.08 (+0.01%)</td><td>480.10 (+4.23%)</td><td>265.70 <b>(+21.99%)</b></td><td>127.91 <b>(-38.01%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>673.00 (n/a)</td><td>453.02 (n/a)</td><td>460.60 (n/a)</td><td>217.80 (n/a)</td><td>206.34 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (-0.88%)</td><td>0.11 (-4.20%)</td><td>0.09 <b>(-20.93%)</b></td><td>0.07 (+16.78%)</td><td>0.04 (+6.92%)</td><td>523.00 (-14.37%)</td><td>377.66 (+3.52%)</td><td>426.30 <b>(+26.46%)</b></td><td>250.60 (+0.93%)</td><td>120.12 (-16.78%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>610.80 (n/a)</td><td>364.82 (n/a)</td><td>337.10 (n/a)</td><td>248.30 (n/a)</td><td>144.34 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (-15.21%)</td><td>0.10 (+3.34%)</td><td>0.12 <b>(+48.80%)</b></td><td>0.06 <b>(+30.50%)</b></td><td>0.03 <b>(-23.71%)</b></td><td>623.20 <b>(-23.37%)</b></td><td>400.50 (-10.56%)</td><td>297.30 <b>(-32.80%)</b></td><td>275.00 (+17.92%)</td><td>157.76 <b>(-31.02%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>813.30 (n/a)</td><td>447.78 (n/a)</td><td>442.40 (n/a)</td><td>233.20 (n/a)</td><td>228.72 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (-6.09%)</td><td>0.11 (-9.75%)</td><td>0.11 <b>(-20.06%)</b></td><td>0.06 <b>(-21.99%)</b></td><td>0.04 (+13.92%)</td><td>661.00 <b>(+28.20%)</b></td><td>403.62 (+15.16%)</td><td>387.50 <b>(+25.08%)</b></td><td>280.00 (+6.46%)</td><td>155.16 <b>(+51.10%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>515.60 (n/a)</td><td>350.48 (n/a)</td><td>309.80 (n/a)</td><td>263.00 (n/a)</td><td>102.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (-2.22%)</td><td>0.09 (-2.00%)</td><td>0.08 (-6.43%)</td><td>0.07 (+5.89%)</td><td>0.02 (-16.73%)</td><td>610.70 (-5.57%)</td><td>479.30 (-0.40%)</td><td>505.00 (+6.88%)</td><td>323.60 (+2.24%)</td><td>105.16 <b>(-23.04%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>646.70 (n/a)</td><td>481.24 (n/a)</td><td>472.50 (n/a)</td><td>316.50 (n/a)</td><td>136.64 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 <b>(-25.89%)</b></td><td>0.10 (-4.73%)</td><td>0.08 (+15.61%)</td><td>0.06 <b>(+196.32%)</b></td><td>0.04 <b>(-51.68%)</b></td><td>630.20 <b>(-66.25%)</b></td><td>454.24 <b>(-35.54%)</b></td><td>499.00 (-13.50%)</td><td>293.30 <b>(+34.91%)</b></td><td>150.78 <b>(-77.73%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>1867.40 (n/a)</td><td>704.66 (n/a)</td><td>576.90 (n/a)</td><td>217.40 (n/a)</td><td>677.09 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (+1.95%)</td><td>0.11 <b>(+24.60%)</b></td><td>0.11 <b>(+41.46%)</b></td><td>0.08 <b>(+103.13%)</b></td><td>0.04 (-19.12%)</td><td>540.00 <b>(-50.77%)</b></td><td>396.36 <b>(-30.35%)</b></td><td>383.20 <b>(-29.30%)</b></td><td>264.60 (-1.89%)</td><td>125.31 <b>(-61.09%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>1096.90 (n/a)</td><td>569.06 (n/a)</td><td>542.00 (n/a)</td><td>269.70 (n/a)</td><td>322.08 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.17 <b>(-23.87%)</b></td><td>0.10 <b>(-21.53%)</b></td><td>0.09 (-5.21%)</td><td>0.02 <b>(-70.77%)</b></td><td>0.06 (-8.09%)</td><td>2063.00 <b>(+242.12%)</b></td><td>726.32 <b>(+83.37%)</b></td><td>446.60 (+5.48%)</td><td>247.60 <b>(+31.35%)</b></td><td>757.25 <b>(+357.46%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>603.00 (n/a)</td><td>396.10 (n/a)</td><td>423.40 (n/a)</td><td>188.50 (n/a)</td><td>165.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.16 <b>(-25.25%)</b></td><td>0.08 <b>(-26.33%)</b></td><td>0.08 (-9.93%)</td><td>0.02 (+0.86%)</td><td>0.05 <b>(-32.48%)</b></td><td>2450.20 (-0.85%)</td><td>863.34 (+10.27%)</td><td>496.80 (+11.04%)</td><td>255.40 <b>(+33.79%)</b></td><td>897.19 (-6.00%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.08 (n/a)</td><td>2471.30 (n/a)</td><td>782.92 (n/a)</td><td>447.40 (n/a)</td><td>190.90 (n/a)</td><td>954.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 <b>(+29.29%)</b></td><td>0.12 <b>(+66.33%)</b></td><td>0.13 <b>(+96.27%)</b></td><td>0.07 <b>(+21.03%)</b></td><td>0.03 <b>(+28.23%)</b></td><td>503.70 (-17.37%)</td><td>308.66 <b>(-39.29%)</b></td><td>272.70 <b>(-49.04%)</b></td><td>231.30 <b>(-22.64%)</b></td><td>111.11 (-9.85%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>609.60 (n/a)</td><td>508.42 (n/a)</td><td>535.10 (n/a)</td><td>299.00 (n/a)</td><td>123.24 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (-4.94%)</td><td>0.10 <b>(+21.06%)</b></td><td>0.12 <b>(+48.87%)</b></td><td>0.04 <b>(-33.86%)</b></td><td>0.04 <b>(+22.48%)</b></td><td>909.90 <b>(+51.20%)</b></td><td>416.80 (-6.41%)</td><td>300.80 <b>(-32.83%)</b></td><td>273.20 (+5.20%)</td><td>275.91 <b>(+113.55%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>601.80 (n/a)</td><td>445.34 (n/a)</td><td>447.80 (n/a)</td><td>259.70 (n/a)</td><td>129.20 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.12 <b>(-21.56%)</b></td><td>0.09 <b>(-34.69%)</b></td><td>0.09 <b>(-36.67%)</b></td><td>0.06 <b>(-49.15%)</b></td><td>0.03 <b>(+146.24%)</b></td><td>571.10 <b>(+96.66%)</b></td><td>425.72 <b>(+65.95%)</b></td><td>399.90 <b>(+57.88%)</b></td><td>290.80 <b>(+27.49%)</b></td><td>138.65 <b>(+522.50%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>290.40 (n/a)</td><td>256.54 (n/a)</td><td>253.30 (n/a)</td><td>228.10 (n/a)</td><td>22.27 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.13 (-4.78%)</td><td>0.07 <b>(-36.55%)</b></td><td>0.06 <b>(-46.90%)</b></td><td>0.01 <b>(-82.11%)</b></td><td>0.04 <b>(+59.52%)</b></td><td>2426.80 <b>(+459.04%)</b></td><td>859.04 <b>(+154.44%)</b></td><td>554.10 <b>(+88.34%)</b></td><td>265.80 (+5.02%)</td><td>886.09 <b>(+915.41%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>434.10 (n/a)</td><td>337.62 (n/a)</td><td>294.20 (n/a)</td><td>253.10 (n/a)</td><td>87.26 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 (+5.33%)</td><td>0.10 (-8.54%)</td><td>0.08 <b>(-28.99%)</b></td><td>0.05 (-11.16%)</td><td>0.04 <b>(+26.44%)</b></td><td>644.60 (+12.55%)</td><td>423.90 (+15.43%)</td><td>422.40 <b>(+40.85%)</b></td><td>239.50 (-5.07%)</td><td>173.82 <b>(+30.46%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>572.70 (n/a)</td><td>367.22 (n/a)</td><td>299.90 (n/a)</td><td>252.30 (n/a)</td><td>133.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 (+8.10%)</td><td>0.11 <b>(+23.40%)</b></td><td>0.12 <b>(+43.84%)</b></td><td>0.06 (-6.82%)</td><td>0.03 <b>(+26.62%)</b></td><td>596.10 (+7.33%)</td><td>363.04 (-15.74%)</td><td>297.80 <b>(-30.49%)</b></td><td>249.90 (-7.48%)</td><td>140.70 <b>(+35.53%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>555.40 (n/a)</td><td>430.84 (n/a)</td><td>428.40 (n/a)</td><td>270.10 (n/a)</td><td>103.82 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.38 <b>(-31.61%)</b></td><td>0.22 (-16.11%)</td><td>0.21 (-19.54%)</td><td>0.07 (-0.05%)</td><td>0.16 (-15.35%)</td><td>1914.90 (+0.05%)</td><td>1025.58 <b>(+30.19%)</b></td><td>613.30 <b>(+24.28%)</b></td><td>341.70 <b>(+46.21%)</b></td><td>818.57 <b>(+23.49%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.56 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>0.19 (n/a)</td><td>1913.90 (n/a)</td><td>787.76 (n/a)</td><td>493.50 (n/a)</td><td>233.70 (n/a)</td><td>662.87 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.42 <b>(+47.97%)</b></td><td>0.34 <b>(+60.47%)</b></td><td>0.37 <b>(+55.54%)</b></td><td>0.23 <b>(+241.77%)</b></td><td>0.08 (-0.94%)</td><td>571.80 <b>(-70.74%)</b></td><td>404.36 <b>(-50.27%)</b></td><td>351.50 <b>(-35.72%)</b></td><td>310.10 <b>(-32.43%)</b></td><td>112.16 <b>(-82.46%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>1954.40 (n/a)</td><td>813.12 (n/a)</td><td>546.80 (n/a)</td><td>458.90 (n/a)</td><td>639.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.50 (+8.03%)</td><td>0.28 (+19.89%)</td><td>0.24 (+9.55%)</td><td>0.19 <b>(+178.92%)</b></td><td>0.12 (-13.28%)</td><td>698.90 <b>(-64.15%)</b></td><td>513.46 <b>(-36.37%)</b></td><td>541.80 (-8.73%)</td><td>260.70 (-7.45%)</td><td>158.52 <b>(-75.76%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.47 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>0.14 (n/a)</td><td>1949.50 (n/a)</td><td>806.96 (n/a)</td><td>593.60 (n/a)</td><td>281.70 (n/a)</td><td>654.03 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.00 <b>(-25.00%)</b></td><td>0.00 <b>(-39.29%)</b></td><td>0.00 <b>(-57.14%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 <b>(-37.03%)</b></td><td>17069.48 (+6.88%)</td><td>12588.78 <b>(+34.33%)</b></td><td>13235.10 <b>(+130.71%)</b></td><td>6611.28 <b>(+34.40%)</b></td><td>3805.07 <b>(-30.49%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>15970.04 (n/a)</td><td>9371.51 (n/a)</td><td>5736.60 (n/a)</td><td>4919.26 (n/a)</td><td>5474.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.00 <b>(-26.67%)</b></td><td>0.00 <b>(-31.11%)</b></td><td>0.00 <b>(-28.57%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-46.10%)</b></td><td>19046.52 (-5.97%)</td><td>14677.32 <b>(+23.09%)</b></td><td>15515.79 <b>(+28.76%)</b></td><td>7337.44 <b>(+30.11%)</b></td><td>4616.10 <b>(-26.86%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20255.29 (n/a)</td><td>11924.38 (n/a)</td><td>12049.90 (n/a)</td><td>5639.32 (n/a)</td><td>6311.43 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.14 <b>(+38.07%)</b></td><td>0.11 <b>(+22.62%)</b></td><td>0.10 (+17.74%)</td><td>0.09 (+7.46%)</td><td>0.02 <b>(+140.25%)</b></td><td>24671.75 (-6.96%)</td><td>20011.77 (-16.20%)</td><td>20939.26 (-15.03%)</td><td>14980.77 <b>(-27.58%)</b></td><td>4155.24 <b>(+60.50%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>26517.21 (n/a)</td><td>23881.28 (n/a)</td><td>24644.33 (n/a)</td><td>20684.74 (n/a)</td><td>2588.92 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>2.24 <b>(-30.64%)</b></td><td>1.34 <b>(-30.69%)</b></td><td>1.32 <b>(-43.89%)</b></td><td>0.30 (-7.01%)</td><td>0.71 <b>(-39.13%)</b></td><td>3513.70 (+7.54%)</td><td>1260.52 (+17.89%)</td><td>794.60 <b>(+78.20%)</b></td><td>468.70 <b>(+44.17%)</b></td><td>1270.44 (+1.66%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.23 (n/a)</td><td>1.93 (n/a)</td><td>2.35 (n/a)</td><td>0.32 (n/a)</td><td>1.17 (n/a)</td><td>3267.40 (n/a)</td><td>1069.24 (n/a)</td><td>445.90 (n/a)</td><td>325.10 (n/a)</td><td>1249.71 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>2.23 <b>(-22.85%)</b></td><td>1.63 <b>(-21.70%)</b></td><td>1.76 <b>(-30.50%)</b></td><td>1.07 <b>(+34.15%)</b></td><td>0.52 <b>(-44.89%)</b></td><td>979.80 <b>(-25.46%)</b></td><td>703.26 (+9.08%)</td><td>596.50 <b>(+43.91%)</b></td><td>470.90 <b>(+29.62%)</b></td><td>237.97 <b>(-41.73%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>2.89 (n/a)</td><td>2.08 (n/a)</td><td>2.53 (n/a)</td><td>0.80 (n/a)</td><td>0.94 (n/a)</td><td>1314.40 (n/a)</td><td>644.72 (n/a)</td><td>414.50 (n/a)</td><td>363.30 (n/a)</td><td>408.36 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.63 (-3.90%)</td><td>2.45 (+0.53%)</td><td>2.38 (+13.58%)</td><td>1.13 (-2.82%)</td><td>0.92 <b>(-24.05%)</b></td><td>925.70 (+2.90%)</td><td>498.06 (-6.47%)</td><td>441.00 (-11.96%)</td><td>288.60 (+4.08%)</td><td>249.46 (-7.01%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.78 (n/a)</td><td>2.44 (n/a)</td><td>2.09 (n/a)</td><td>1.17 (n/a)</td><td>1.21 (n/a)</td><td>899.60 (n/a)</td><td>532.50 (n/a)</td><td>500.90 (n/a)</td><td>277.30 (n/a)</td><td>268.27 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>2.76 <b>(-23.17%)</b></td><td>1.56 <b>(-35.60%)</b></td><td>1.74 <b>(-24.21%)</b></td><td>0.54 <b>(-61.81%)</b></td><td>0.99 (+6.12%)</td><td>1928.90 <b>(+161.83%)</b></td><td>1059.92 <b>(+116.09%)</b></td><td>601.90 <b>(+31.97%)</b></td><td>379.70 <b>(+30.17%)</b></td><td>790.65 <b>(+312.26%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.59 (n/a)</td><td>2.42 (n/a)</td><td>2.30 (n/a)</td><td>1.42 (n/a)</td><td>0.94 (n/a)</td><td>736.70 (n/a)</td><td>490.50 (n/a)</td><td>456.10 (n/a)</td><td>291.70 (n/a)</td><td>191.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.52 <b>(-24.98%)</b></td><td>1.77 <b>(-28.08%)</b></td><td>1.87 <b>(-24.27%)</b></td><td>0.61 (+5.48%)</td><td>1.15 <b>(-32.91%)</b></td><td>3433.80 (-5.20%)</td><td>1733.74 (+14.35%)</td><td>1124.30 <b>(+32.05%)</b></td><td>595.00 <b>(+33.29%)</b></td><td>1180.40 (-11.95%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>4.70 (n/a)</td><td>2.46 (n/a)</td><td>2.46 (n/a)</td><td>0.58 (n/a)</td><td>1.72 (n/a)</td><td>3622.00 (n/a)</td><td>1516.20 (n/a)</td><td>851.40 (n/a)</td><td>446.40 (n/a)</td><td>1340.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.06 (+1.30%)</td><td>3.97 <b>(+39.80%)</b></td><td>3.90 <b>(+58.59%)</b></td><td>2.73 <b>(+386.98%)</b></td><td>0.89 <b>(-47.32%)</b></td><td>769.30 <b>(-79.47%)</b></td><td>552.24 <b>(-57.35%)</b></td><td>537.30 <b>(-36.94%)</b></td><td>414.80 (-1.29%)</td><td>136.91 <b>(-90.12%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>4.99 (n/a)</td><td>2.84 (n/a)</td><td>2.46 (n/a)</td><td>0.56 (n/a)</td><td>1.69 (n/a)</td><td>3746.50 (n/a)</td><td>1294.78 (n/a)</td><td>852.10 (n/a)</td><td>420.20 (n/a)</td><td>1386.36 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.52 <b>(+42.22%)</b></td><td>2.89 <b>(+22.64%)</b></td><td>2.44 (-1.51%)</td><td>0.99 <b>(+69.60%)</b></td><td>1.74 <b>(+39.84%)</b></td><td>2110.00 <b>(-41.04%)</b></td><td>1007.04 <b>(-26.15%)</b></td><td>860.60 (+1.53%)</td><td>379.90 <b>(-29.69%)</b></td><td>674.28 <b>(-46.45%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.88 (n/a)</td><td>2.36 (n/a)</td><td>2.47 (n/a)</td><td>0.59 (n/a)</td><td>1.25 (n/a)</td><td>3578.50 (n/a)</td><td>1363.70 (n/a)</td><td>847.60 (n/a)</td><td>540.30 (n/a)</td><td>1259.16 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.88 <b>(-30.21%)</b></td><td>2.74 (-7.93%)</td><td>2.76 (-8.97%)</td><td>0.60 (-0.27%)</td><td>1.34 <b>(-27.78%)</b></td><td>3522.80 (+0.27%)</td><td>1233.30 (-0.38%)</td><td>759.70 (+9.86%)</td><td>541.00 <b>(+43.31%)</b></td><td>1285.52 (-0.72%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.56 (n/a)</td><td>2.98 (n/a)</td><td>3.03 (n/a)</td><td>0.60 (n/a)</td><td>1.86 (n/a)</td><td>3513.40 (n/a)</td><td>1238.04 (n/a)</td><td>691.50 (n/a)</td><td>377.50 (n/a)</td><td>1294.85 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>6.88 <b>(+22.77%)</b></td><td>2.99 (-8.97%)</td><td>2.31 <b>(-28.51%)</b></td><td>1.08 <b>(+86.33%)</b></td><td>2.25 (+19.68%)</td><td>1942.60 <b>(-46.33%)</b></td><td>993.50 (-15.92%)</td><td>908.70 <b>(+39.86%)</b></td><td>304.90 (-18.54%)</td><td>594.55 <b>(-56.65%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.60 (n/a)</td><td>3.28 (n/a)</td><td>3.23 (n/a)</td><td>0.58 (n/a)</td><td>1.88 (n/a)</td><td>3619.50 (n/a)</td><td>1181.62 (n/a)</td><td>649.70 (n/a)</td><td>374.30 (n/a)</td><td>1371.50 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.81 (-16.78%)</td><td>3.57 <b>(+34.24%)</b></td><td>3.31 <b>(+98.65%)</b></td><td>2.08 <b>(+253.51%)</b></td><td>1.40 <b>(-46.80%)</b></td><td>1007.20 <b>(-71.71%)</b></td><td>657.18 <b>(-60.07%)</b></td><td>633.50 <b>(-49.66%)</b></td><td>360.70 <b>(+20.19%)</b></td><td>236.94 <b>(-82.41%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>6.99 (n/a)</td><td>2.66 (n/a)</td><td>1.67 (n/a)</td><td>0.59 (n/a)</td><td>2.62 (n/a)</td><td>3560.60 (n/a)</td><td>1646.00 (n/a)</td><td>1258.50 (n/a)</td><td>300.10 (n/a)</td><td>1347.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>5.55 (+4.67%)</td><td>3.55 (-19.54%)</td><td>3.87 (-16.00%)</td><td>1.18 <b>(-64.47%)</b></td><td>1.88 <b>(+125.12%)</b></td><td>3548.30 <b>(+181.48%)</b></td><td>1647.30 <b>(+67.95%)</b></td><td>1084.00 (+19.06%)</td><td>756.30 (-4.46%)</td><td>1176.64 <b>(+492.21%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.30 (n/a)</td><td>4.41 (n/a)</td><td>4.61 (n/a)</td><td>3.33 (n/a)</td><td>0.84 (n/a)</td><td>1260.60 (n/a)</td><td>980.80 (n/a)</td><td>910.50 (n/a)</td><td>791.60 (n/a)</td><td>198.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>7.92 (-5.36%)</td><td>5.00 (-16.87%)</td><td>3.87 <b>(-32.78%)</b></td><td>1.73 <b>(-54.86%)</b></td><td>2.71 <b>(+66.25%)</b></td><td>2426.80 <b>(+121.56%)</b></td><td>1138.28 <b>(+53.34%)</b></td><td>1083.60 <b>(+48.76%)</b></td><td>529.80 (+5.64%)</td><td>772.62 <b>(+253.90%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>8.36 (n/a)</td><td>6.02 (n/a)</td><td>5.76 (n/a)</td><td>3.83 (n/a)</td><td>1.63 (n/a)</td><td>1095.30 (n/a)</td><td>742.34 (n/a)</td><td>728.40 (n/a)</td><td>501.50 (n/a)</td><td>218.32 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>6.88 (-5.74%)</td><td>4.32 (+0.06%)</td><td>4.01 (+2.69%)</td><td>1.15 (+1.13%)</td><td>2.22 (-2.35%)</td><td>3646.60 (-1.11%)</td><td>1432.66 (-0.64%)</td><td>1045.80 (-2.62%)</td><td>609.70 (+6.09%)</td><td>1258.03 (-1.28%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>7.30 (n/a)</td><td>4.32 (n/a)</td><td>3.91 (n/a)</td><td>1.14 (n/a)</td><td>2.27 (n/a)</td><td>3687.70 (n/a)</td><td>1441.82 (n/a)</td><td>1073.90 (n/a)</td><td>574.70 (n/a)</td><td>1274.32 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>10.01 <b>(+30.89%)</b></td><td>6.28 (+19.53%)</td><td>7.36 (+12.64%)</td><td>1.15 (+5.64%)</td><td>3.81 <b>(+39.05%)</b></td><td>3639.60 (-5.34%)</td><td>1252.14 (-6.64%)</td><td>569.80 (-11.22%)</td><td>419.00 <b>(-23.61%)</b></td><td>1370.09 (-3.24%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>7.65 (n/a)</td><td>5.25 (n/a)</td><td>6.54 (n/a)</td><td>1.09 (n/a)</td><td>2.74 (n/a)</td><td>3845.00 (n/a)</td><td>1341.24 (n/a)</td><td>641.80 (n/a)</td><td>548.50 (n/a)</td><td>1415.92 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>9.50 <b>(+38.44%)</b></td><td>6.81 (+14.76%)</td><td>8.27 <b>(+25.50%)</b></td><td>3.77 (-19.90%)</td><td>2.69 <b>(+139.15%)</b></td><td>1113.60 <b>(+24.83%)</b></td><td>718.96 (-1.47%)</td><td>507.00 <b>(-20.32%)</b></td><td>441.60 <b>(-27.77%)</b></td><td>326.90 <b>(+120.58%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>6.86 (n/a)</td><td>5.93 (n/a)</td><td>6.59 (n/a)</td><td>4.70 (n/a)</td><td>1.12 (n/a)</td><td>892.10 (n/a)</td><td>729.72 (n/a)</td><td>636.30 (n/a)</td><td>611.40 (n/a)</td><td>148.20 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>9.60 (+12.61%)</td><td>5.79 (-9.42%)</td><td>6.78 (-4.55%)</td><td>1.71 <b>(+44.73%)</b></td><td>3.43 (+13.47%)</td><td>2459.60 <b>(-30.91%)</b></td><td>1114.70 (-3.33%)</td><td>618.40 (+4.78%)</td><td>437.00 (-11.20%)</td><td>874.04 <b>(-35.09%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>8.52 (n/a)</td><td>6.39 (n/a)</td><td>7.11 (n/a)</td><td>1.18 (n/a)</td><td>3.02 (n/a)</td><td>3559.80 (n/a)</td><td>1153.14 (n/a)</td><td>590.20 (n/a)</td><td>492.10 (n/a)</td><td>1346.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>1.56 (-4.06%)</td><td>1.01 (-16.31%)</td><td>0.98 <b>(-26.11%)</b></td><td>0.48 <b>(-32.10%)</b></td><td>0.48 <b>(+27.46%)</b></td><td>1096.20 <b>(+47.28%)</b></td><td>646.28 <b>(+34.66%)</b></td><td>534.20 <b>(+35.34%)</b></td><td>336.10 (+4.22%)</td><td>335.64 <b>(+91.30%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>1.63 (n/a)</td><td>1.20 (n/a)</td><td>1.33 (n/a)</td><td>0.70 (n/a)</td><td>0.38 (n/a)</td><td>744.30 (n/a)</td><td>479.92 (n/a)</td><td>394.70 (n/a)</td><td>322.50 (n/a)</td><td>175.45 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>2.35 <b>(-28.36%)</b></td><td>1.54 (-13.65%)</td><td>1.54 (+6.25%)</td><td>0.30 (+3.12%)</td><td>0.80 <b>(-31.64%)</b></td><td>3487.60 (-3.03%)</td><td>1170.44 (+0.33%)</td><td>681.60 (-5.87%)</td><td>446.80 <b>(+39.58%)</b></td><td>1301.16 (-5.23%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.28 (n/a)</td><td>1.79 (n/a)</td><td>1.45 (n/a)</td><td>0.29 (n/a)</td><td>1.16 (n/a)</td><td>3596.40 (n/a)</td><td>1166.58 (n/a)</td><td>724.10 (n/a)</td><td>320.10 (n/a)</td><td>1372.99 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>3.89 (+10.05%)</td><td>1.85 (-2.55%)</td><td>1.82 <b>(+76.47%)</b></td><td>0.60 (-0.16%)</td><td>1.37 (-7.18%)</td><td>3493.30 (+0.16%)</td><td>1899.02 (+3.53%)</td><td>1155.10 <b>(-43.33%)</b></td><td>539.30 (-9.13%)</td><td>1433.33 (+15.08%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.53 (n/a)</td><td>1.90 (n/a)</td><td>1.03 (n/a)</td><td>0.60 (n/a)</td><td>1.47 (n/a)</td><td>3487.80 (n/a)</td><td>1834.24 (n/a)</td><td>2038.30 (n/a)</td><td>593.50 (n/a)</td><td>1245.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>1.76 (-5.11%)</td><td>1.02 (-6.32%)</td><td>0.91 (-4.35%)</td><td>0.28 <b>(-62.54%)</b></td><td>0.61 <b>(+38.89%)</b></td><td>1889.20 <b>(+166.99%)</b></td><td>788.00 <b>(+48.13%)</b></td><td>574.40 (+4.55%)</td><td>298.20 (+5.37%)</td><td>650.28 <b>(+321.96%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>1.85 (n/a)</td><td>1.08 (n/a)</td><td>0.95 (n/a)</td><td>0.74 (n/a)</td><td>0.44 (n/a)</td><td>707.60 (n/a)</td><td>531.96 (n/a)</td><td>549.40 (n/a)</td><td>283.00 (n/a)</td><td>154.11 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.15 <b>(+27.27%)</b></td><td>0.09 (-0.34%)</td><td>0.10 (-4.40%)</td><td>0.02 <b>(-66.67%)</b></td><td>0.05 <b>(+59.97%)</b></td><td>1925.40 <b>(+200.00%)</b></td><td>654.50 <b>(+56.99%)</b></td><td>316.10 (+4.60%)</td><td>225.80 <b>(-21.43%)</b></td><td>718.13 <b>(+327.02%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>641.80 (n/a)</td><td>416.90 (n/a)</td><td>302.20 (n/a)</td><td>287.40 (n/a)</td><td>168.17 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.10 <b>(-29.29%)</b></td><td>0.07 <b>(-38.32%)</b></td><td>0.07 <b>(-44.73%)</b></td><td>0.03 <b>(-52.36%)</b></td><td>0.03 <b>(-34.57%)</b></td><td>1212.30 <b>(+109.92%)</b></td><td>604.96 <b>(+69.76%)</b></td><td>499.70 <b>(+80.92%)</b></td><td>325.50 <b>(+41.40%)</b></td><td>348.01 <b>(+121.54%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>577.50 (n/a)</td><td>356.36 (n/a)</td><td>276.20 (n/a)</td><td>230.20 (n/a)</td><td>157.09 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.17 <b>(-39.85%)</b></td><td>0.13 <b>(-34.69%)</b></td><td>0.13 <b>(-42.50%)</b></td><td>0.11 (-7.22%)</td><td>0.02 <b>(-65.26%)</b></td><td>605.00 (+7.79%)</td><td>506.56 <b>(+40.45%)</b></td><td>498.20 <b>(+73.89%)</b></td><td>389.00 <b>(+66.31%)</b></td><td>87.99 <b>(-37.76%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>561.30 (n/a)</td><td>360.68 (n/a)</td><td>286.50 (n/a)</td><td>233.90 (n/a)</td><td>141.36 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.25 (-7.09%)</td><td>0.15 <b>(-20.61%)</b></td><td>0.12 <b>(-29.35%)</b></td><td>0.03 <b>(-74.78%)</b></td><td>0.09 <b>(+45.48%)</b></td><td>1953.50 <b>(+296.57%)</b></td><td>727.58 <b>(+93.68%)</b></td><td>557.60 <b>(+41.56%)</b></td><td>261.40 (+7.66%)</td><td>703.26 <b>(+489.96%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>492.60 (n/a)</td><td>375.66 (n/a)</td><td>393.90 (n/a)</td><td>242.80 (n/a)</td><td>119.21 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.23 (-9.60%)</td><td>0.18 (+10.73%)</td><td>0.17 <b>(+32.66%)</b></td><td>0.14 <b>(+35.01%)</b></td><td>0.04 <b>(-37.96%)</b></td><td>467.20 <b>(-25.94%)</b></td><td>375.76 (-17.32%)</td><td>377.80 <b>(-24.62%)</b></td><td>285.70 (+10.61%)</td><td>86.48 <b>(-49.10%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>630.80 (n/a)</td><td>454.46 (n/a)</td><td>501.20 (n/a)</td><td>258.30 (n/a)</td><td>169.89 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.62 <b>(+37.22%)</b></td><td>0.39 <b>(+41.94%)</b></td><td>0.28 (+15.45%)</td><td>0.24 <b>(+243.77%)</b></td><td>0.17 (+19.68%)</td><td>557.30 <b>(-70.91%)</b></td><td>391.18 <b>(-46.39%)</b></td><td>459.90 (-13.39%)</td><td>212.60 <b>(-27.12%)</b></td><td>151.24 <b>(-77.49%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.45 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>0.14 (n/a)</td><td>1915.80 (n/a)</td><td>729.64 (n/a)</td><td>531.00 (n/a)</td><td>291.70 (n/a)</td><td>671.86 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.52 (-17.66%)</td><td>0.33 (-8.82%)</td><td>0.28 <b>(-22.02%)</b></td><td>0.10 <b>(+42.38%)</b></td><td>0.18 (-15.52%)</td><td>1340.20 <b>(-29.76%)</b></td><td>574.12 (-11.81%)</td><td>474.40 <b>(+28.22%)</b></td><td>253.20 <b>(+21.44%)</b></td><td>446.16 <b>(-37.19%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.63 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td><td>1908.10 (n/a)</td><td>650.98 (n/a)</td><td>370.00 (n/a)</td><td>208.50 (n/a)</td><td>710.38 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.47 (-14.65%)</td><td>0.30 (-15.68%)</td><td>0.26 (-6.48%)</td><td>0.21 (+5.21%)</td><td>0.10 <b>(-31.03%)</b></td><td>614.40 (-4.95%)</td><td>469.38 (+11.66%)</td><td>498.00 (+6.91%)</td><td>278.30 (+17.18%)</td><td>126.96 <b>(-23.18%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.55 (n/a)</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>646.40 (n/a)</td><td>420.36 (n/a)</td><td>465.80 (n/a)</td><td>237.50 (n/a)</td><td>165.26 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:12</td><td>0.07 (+10.09%)</td><td>0.03 <b>(-20.30%)</b></td><td>0.03 <b>(-32.69%)</b></td><td>0.02 (-9.84%)</td><td>0.02 <b>(+28.64%)</b></td><td>694.60 (+10.91%)</td><td>545.12 <b>(+32.07%)</b></td><td>625.40 <b>(+48.59%)</b></td><td>251.90 (-9.16%)</td><td>176.06 <b>(+26.43%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>626.30 (n/a)</td><td>412.76 (n/a)</td><td>420.90 (n/a)</td><td>277.30 (n/a)</td><td>139.26 (n/a)</td>
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
