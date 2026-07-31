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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 <b>(+38.61%)</b></td><td>0.02 (+17.99%)</td><td>0.01 (-16.52%)</td><td>0.01 <b>(+20.99%)</b></td><td>0.01 <b>(+85.89%)</b></td><td>566.10 (-17.35%)</td><td>397.96 (-3.60%)</td><td>480.90 (+19.78%)</td><td>178.80 <b>(-27.85%)</b></td><td>192.63 (+12.63%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>684.90 (n/a)</td><td>412.82 (n/a)</td><td>401.50 (n/a)</td><td>247.80 (n/a)</td><td>171.02 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (-3.88%)</td><td>0.01 (+4.54%)</td><td>0.01 (+8.13%)</td><td>0.01 (+4.26%)</td><td>0.00 (-11.98%)</td><td>543.60 (-4.08%)</td><td>427.02 (-5.60%)</td><td>450.80 (-7.51%)</td><td>322.80 (+4.03%)</td><td>94.19 (-15.06%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.70 (n/a)</td><td>452.34 (n/a)</td><td>487.40 (n/a)</td><td>310.30 (n/a)</td><td>110.88 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (-7.34%)</td><td>0.02 (+18.68%)</td><td>0.02 <b>(+45.02%)</b></td><td>0.01 <b>(+466.34%)</b></td><td>0.01 <b>(-46.47%)</b></td><td>451.90 <b>(-82.34%)</b></td><td>347.82 <b>(-57.60%)</b></td><td>361.40 <b>(-31.04%)</b></td><td>224.80 (+7.92%)</td><td>102.13 <b>(-89.64%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2559.60 (n/a)</td><td>820.40 (n/a)</td><td>524.10 (n/a)</td><td>208.30 (n/a)</td><td>986.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 <b>(-21.72%)</b></td><td>0.02 (-2.67%)</td><td>0.02 (-6.15%)</td><td>0.01 <b>(+241.80%)</b></td><td>0.01 <b>(-45.68%)</b></td><td>561.90 <b>(-70.75%)</b></td><td>360.80 <b>(-42.43%)</b></td><td>284.70 (+6.55%)</td><td>231.70 <b>(+27.73%)</b></td><td>142.58 <b>(-80.63%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1920.70 (n/a)</td><td>626.68 (n/a)</td><td>267.20 (n/a)</td><td>181.40 (n/a)</td><td>735.95 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (+7.13%)</td><td>0.01 (+16.27%)</td><td>0.01 <b>(+20.84%)</b></td><td>0.01 (+12.60%)</td><td>0.00 (-1.33%)</td><td>608.60 (-11.19%)</td><td>458.36 (-14.61%)</td><td>431.30 (-17.25%)</td><td>348.80 (-6.66%)</td><td>98.94 (-16.28%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>685.30 (n/a)</td><td>536.76 (n/a)</td><td>521.20 (n/a)</td><td>373.70 (n/a)</td><td>118.18 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 <b>(+36.79%)</b></td><td>0.02 <b>(+65.05%)</b></td><td>0.02 <b>(+69.57%)</b></td><td>0.02 <b>(+77.49%)</b></td><td>0.00 (+1.31%)</td><td>369.00 <b>(-43.66%)</b></td><td>284.30 <b>(-41.87%)</b></td><td>283.10 <b>(-41.03%)</b></td><td>217.10 <b>(-26.90%)</b></td><td>58.37 <b>(-57.73%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>654.90 (n/a)</td><td>489.06 (n/a)</td><td>480.10 (n/a)</td><td>297.00 (n/a)</td><td>138.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 <b>(+39.50%)</b></td><td>0.06 <b>(+49.17%)</b></td><td>0.05 (+16.69%)</td><td>0.05 <b>(+655.78%)</b></td><td>0.01 <b>(-36.17%)</b></td><td>255.40 <b>(-86.77%)</b></td><td>229.44 <b>(-62.84%)</b></td><td>245.50 (-14.31%)</td><td>158.40 <b>(-28.33%)</b></td><td>40.06 <b>(-94.57%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1930.10 (n/a)</td><td>617.40 (n/a)</td><td>286.50 (n/a)</td><td>221.00 (n/a)</td><td>737.17 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (+7.12%)</td><td>0.04 <b>(+28.69%)</b></td><td>0.05 <b>(+107.23%)</b></td><td>0.02 (+11.24%)</td><td>0.01 (+3.28%)</td><td>575.80 (-10.10%)</td><td>343.84 <b>(-23.66%)</b></td><td>244.50 <b>(-51.75%)</b></td><td>230.50 (-6.64%)</td><td>154.28 (-14.76%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>640.50 (n/a)</td><td>450.40 (n/a)</td><td>506.70 (n/a)</td><td>246.90 (n/a)</td><td>180.99 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 <b>(+22.76%)</b></td><td>0.04 (-0.71%)</td><td>0.03 (-9.68%)</td><td>0.02 <b>(-25.17%)</b></td><td>0.02 <b>(+71.00%)</b></td><td>600.00 <b>(+33.66%)</b></td><td>401.00 (+12.23%)</td><td>449.40 (+10.72%)</td><td>211.70 (-18.55%)</td><td>166.46 <b>(+87.00%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>448.90 (n/a)</td><td>357.30 (n/a)</td><td>405.90 (n/a)</td><td>259.90 (n/a)</td><td>89.02 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (-0.92%)</td><td>0.04 (-0.08%)</td><td>0.04 (-0.69%)</td><td>0.02 (-10.81%)</td><td>0.02 (+12.71%)</td><td>635.80 (+12.13%)</td><td>384.28 (+6.80%)</td><td>276.20 (+0.69%)</td><td>197.50 (+0.92%)</td><td>206.01 <b>(+28.17%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>567.00 (n/a)</td><td>359.80 (n/a)</td><td>274.30 (n/a)</td><td>195.70 (n/a)</td><td>160.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (+16.33%)</td><td>0.04 <b>(+21.68%)</b></td><td>0.04 <b>(+49.61%)</b></td><td>0.02 (-4.75%)</td><td>0.02 <b>(+50.44%)</b></td><td>575.50 (+5.00%)</td><td>384.98 (-10.07%)</td><td>293.10 <b>(-33.16%)</b></td><td>216.60 (-14.05%)</td><td>174.08 <b>(+58.90%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>548.10 (n/a)</td><td>428.10 (n/a)</td><td>438.50 (n/a)</td><td>252.00 (n/a)</td><td>109.55 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (-16.79%)</td><td>0.03 (-17.07%)</td><td>0.02 (-10.29%)</td><td>0.01 <b>(-24.71%)</b></td><td>0.02 (-9.38%)</td><td>1381.10 <b>(+32.81%)</b></td><td>735.36 <b>(+33.31%)</b></td><td>624.70 (+11.47%)</td><td>249.00 <b>(+20.17%)</b></td><td>492.82 <b>(+49.49%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1039.90 (n/a)</td><td>551.60 (n/a)</td><td>560.40 (n/a)</td><td>207.20 (n/a)</td><td>329.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 <b>(-28.10%)</b></td><td>0.09 (-12.61%)</td><td>0.10 (+14.74%)</td><td>0.05 <b>(-27.50%)</b></td><td>0.03 (-18.04%)</td><td>512.30 <b>(+37.94%)</b></td><td>319.82 (+17.61%)</td><td>247.20 (-12.87%)</td><td>221.10 <b>(+39.06%)</b></td><td>125.23 <b>(+63.97%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>371.40 (n/a)</td><td>271.94 (n/a)</td><td>283.70 (n/a)</td><td>159.00 (n/a)</td><td>76.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (+8.41%)</td><td>0.08 <b>(+22.73%)</b></td><td>0.10 <b>(+54.24%)</b></td><td>0.05 (+7.16%)</td><td>0.02 <b>(+35.12%)</b></td><td>471.30 (-6.67%)</td><td>328.40 (-16.32%)</td><td>249.40 <b>(-35.17%)</b></td><td>248.40 (-7.76%)</td><td>110.02 (+9.66%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>505.00 (n/a)</td><td>392.44 (n/a)</td><td>384.70 (n/a)</td><td>269.30 (n/a)</td><td>100.32 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (-2.43%)</td><td>0.07 (-10.49%)</td><td>0.09 (-5.88%)</td><td>0.01 <b>(-68.83%)</b></td><td>0.04 (+19.75%)</td><td>1998.00 <b>(+220.81%)</b></td><td>646.34 <b>(+77.25%)</b></td><td>267.10 (+6.25%)</td><td>231.30 (+2.53%)</td><td>763.01 <b>(+316.07%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>622.80 (n/a)</td><td>364.64 (n/a)</td><td>251.40 (n/a)</td><td>225.60 (n/a)</td><td>183.38 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (-1.92%)</td><td>0.07 <b>(-20.85%)</b></td><td>0.09 (-6.04%)</td><td>0.02 <b>(-72.60%)</b></td><td>0.03 <b>(+320.24%)</b></td><td>1081.10 <b>(+264.99%)</b></td><td>449.74 <b>(+72.13%)</b></td><td>266.80 (+6.42%)</td><td>246.40 (+1.94%)</td><td>359.30 <b>(+1457.28%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>296.20 (n/a)</td><td>261.28 (n/a)</td><td>250.70 (n/a)</td><td>241.70 (n/a)</td><td>23.07 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (+0.25%)</td><td>0.06 (-8.35%)</td><td>0.06 (+12.36%)</td><td>0.03 <b>(-33.22%)</b></td><td>0.02 <b>(+25.16%)</b></td><td>958.90 <b>(+49.73%)</b></td><td>521.44 <b>(+21.70%)</b></td><td>392.70 (-10.99%)</td><td>294.00 (-0.24%)</td><td>279.16 <b>(+96.22%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>640.40 (n/a)</td><td>428.48 (n/a)</td><td>441.20 (n/a)</td><td>294.70 (n/a)</td><td>142.27 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 <b>(+43.33%)</b></td><td>0.09 (+12.30%)</td><td>0.09 (+5.78%)</td><td>0.04 (-3.75%)</td><td>0.04 <b>(+68.74%)</b></td><td>551.80 (+3.90%)</td><td>338.20 (-2.41%)</td><td>280.00 (-5.44%)</td><td>161.30 <b>(-30.23%)</b></td><td>159.25 <b>(+26.07%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>531.10 (n/a)</td><td>346.56 (n/a)</td><td>296.10 (n/a)</td><td>231.20 (n/a)</td><td>126.32 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.21 (-6.74%)</td><td>0.17 (+2.16%)</td><td>0.18 (-9.23%)</td><td>0.09 (-0.91%)</td><td>0.05 <b>(-27.31%)</b></td><td>554.50 (+0.93%)</td><td>319.62 (-7.45%)</td><td>271.00 (+10.16%)</td><td>232.40 (+7.20%)</td><td>132.35 (-15.52%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>549.40 (n/a)</td><td>345.36 (n/a)</td><td>246.00 (n/a)</td><td>216.80 (n/a)</td><td>156.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.20 (-8.09%)</td><td>0.17 <b>(+23.44%)</b></td><td>0.18 <b>(+63.64%)</b></td><td>0.12 <b>(+35.09%)</b></td><td>0.03 <b>(-36.61%)</b></td><td>424.60 <b>(-25.98%)</b></td><td>303.34 <b>(-24.09%)</b></td><td>270.60 <b>(-38.89%)</b></td><td>250.90 (+8.80%)</td><td>71.14 <b>(-46.68%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>573.60 (n/a)</td><td>399.58 (n/a)</td><td>442.80 (n/a)</td><td>230.60 (n/a)</td><td>133.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.23 (+9.36%)</td><td>0.17 <b>(+39.13%)</b></td><td>0.18 <b>(+78.75%)</b></td><td>0.09 <b>(+263.04%)</b></td><td>0.06 <b>(-30.10%)</b></td><td>528.60 <b>(-72.45%)</b></td><td>320.88 <b>(-54.33%)</b></td><td>279.60 <b>(-44.06%)</b></td><td>213.50 (-8.57%)</td><td>127.57 <b>(-81.75%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>1919.00 (n/a)</td><td>702.64 (n/a)</td><td>499.80 (n/a)</td><td>233.50 (n/a)</td><td>698.95 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.21 (+2.64%)</td><td>0.15 (-1.81%)</td><td>0.20 (+16.01%)</td><td>0.02 <b>(-74.19%)</b></td><td>0.08 <b>(+54.32%)</b></td><td>2134.50 <b>(+287.46%)</b></td><td>664.44 <b>(+81.97%)</b></td><td>249.40 (-13.79%)</td><td>233.80 (-2.58%)</td><td>827.83 <b>(+469.00%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>550.90 (n/a)</td><td>365.14 (n/a)</td><td>289.30 (n/a)</td><td>240.00 (n/a)</td><td>145.49 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.19 <b>(+34.28%)</b></td><td>0.11 (+6.34%)</td><td>0.09 (-9.88%)</td><td>0.08 (+5.05%)</td><td>0.05 <b>(+86.37%)</b></td><td>593.80 (-4.79%)</td><td>480.34 (-0.46%)</td><td>549.70 (+10.96%)</td><td>255.40 <b>(-25.54%)</b></td><td>139.92 <b>(+31.81%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>623.70 (n/a)</td><td>482.54 (n/a)</td><td>495.40 (n/a)</td><td>343.00 (n/a)</td><td>106.16 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.20 (-2.86%)</td><td>0.13 (-16.86%)</td><td>0.12 (-17.78%)</td><td>0.09 (-0.41%)</td><td>0.05 (-12.39%)</td><td>573.20 (+0.40%)</td><td>423.82 (+17.77%)</td><td>398.30 <b>(+21.62%)</b></td><td>244.50 (+2.95%)</td><td>125.29 (-9.04%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>570.90 (n/a)</td><td>359.86 (n/a)</td><td>327.50 (n/a)</td><td>237.50 (n/a)</td><td>137.74 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (-0.67%)</td><td>0.01 (-9.73%)</td><td>0.01 (-4.66%)</td><td>0.01 <b>(-36.68%)</b></td><td>0.00 <b>(+98.15%)</b></td><td>472.30 <b>(+57.91%)</b></td><td>308.58 (+16.27%)</td><td>279.00 (+4.89%)</td><td>234.20 (+0.69%)</td><td>93.85 <b>(+235.32%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>299.10 (n/a)</td><td>265.40 (n/a)</td><td>266.00 (n/a)</td><td>232.60 (n/a)</td><td>27.99 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (-16.80%)</td><td>0.01 <b>(-24.52%)</b></td><td>0.01 <b>(-27.65%)</b></td><td>0.00 <b>(-41.65%)</b></td><td>0.00 (+11.54%)</td><td>719.50 <b>(+71.39%)</b></td><td>479.98 <b>(+40.10%)</b></td><td>485.10 <b>(+38.21%)</b></td><td>286.10 <b>(+20.21%)</b></td><td>163.17 <b>(+130.53%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>419.80 (n/a)</td><td>342.60 (n/a)</td><td>351.00 (n/a)</td><td>238.00 (n/a)</td><td>70.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (-10.09%)</td><td>0.01 (+4.29%)</td><td>0.01 <b>(+33.53%)</b></td><td>0.01 (+4.71%)</td><td>0.00 (-7.98%)</td><td>515.10 (-4.51%)</td><td>345.48 (-5.12%)</td><td>300.90 <b>(-25.09%)</b></td><td>221.00 (+11.22%)</td><td>138.35 (-1.43%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>539.40 (n/a)</td><td>364.14 (n/a)</td><td>401.70 (n/a)</td><td>198.70 (n/a)</td><td>140.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (-0.54%)</td><td>0.01 (-8.99%)</td><td>0.01 (-17.33%)</td><td>0.00 <b>(-20.17%)</b></td><td>0.00 (+2.24%)</td><td>650.70 <b>(+25.26%)</b></td><td>376.02 (+13.21%)</td><td>340.70 <b>(+20.94%)</b></td><td>243.10 (+0.54%)</td><td>161.89 <b>(+37.16%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.50 (n/a)</td><td>332.14 (n/a)</td><td>281.70 (n/a)</td><td>241.80 (n/a)</td><td>118.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (-6.96%)</td><td>0.01 <b>(-28.14%)</b></td><td>0.01 <b>(-23.62%)</b></td><td>0.00 <b>(-76.34%)</b></td><td>0.00 <b>(+47.37%)</b></td><td>1959.70 <b>(+322.62%)</b></td><td>763.66 <b>(+116.84%)</b></td><td>501.00 <b>(+30.91%)</b></td><td>251.90 (+7.51%)</td><td>702.38 <b>(+584.02%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.70 (n/a)</td><td>352.18 (n/a)</td><td>382.70 (n/a)</td><td>234.30 (n/a)</td><td>102.68 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 <b>(+48.23%)</b></td><td>0.01 <b>(+31.30%)</b></td><td>0.01 (+18.35%)</td><td>0.00 <b>(+34.83%)</b></td><td>0.00 <b>(+76.95%)</b></td><td>562.30 <b>(-25.84%)</b></td><td>410.42 <b>(-21.77%)</b></td><td>427.80 (-15.50%)</td><td>253.00 <b>(-32.53%)</b></td><td>123.19 (-14.65%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>758.20 (n/a)</td><td>524.62 (n/a)</td><td>506.30 (n/a)</td><td>375.00 (n/a)</td><td>144.33 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 <b>(-20.56%)</b></td><td>0.01 (+12.73%)</td><td>0.02 <b>(+26.41%)</b></td><td>0.01 <b>(+33.47%)</b></td><td>0.00 <b>(-51.99%)</b></td><td>472.70 <b>(-25.06%)</b></td><td>362.12 (-18.02%)</td><td>342.30 <b>(-20.89%)</b></td><td>309.20 <b>(+25.90%)</b></td><td>67.59 <b>(-54.10%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.80 (n/a)</td><td>441.70 (n/a)</td><td>432.70 (n/a)</td><td>245.60 (n/a)</td><td>147.26 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (-5.72%)</td><td>0.02 (+2.03%)</td><td>0.02 (-2.88%)</td><td>0.01 <b>(+24.68%)</b></td><td>0.00 <b>(-22.46%)</b></td><td>474.00 (-19.78%)</td><td>298.66 (-7.64%)</td><td>262.70 (+2.98%)</td><td>231.70 (+6.04%)</td><td>99.87 <b>(-34.81%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.90 (n/a)</td><td>323.36 (n/a)</td><td>255.10 (n/a)</td><td>218.50 (n/a)</td><td>153.22 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 <b>(+21.98%)</b></td><td>0.02 <b>(+52.54%)</b></td><td>0.02 <b>(+57.64%)</b></td><td>0.02 <b>(+100.49%)</b></td><td>0.00 <b>(-30.86%)</b></td><td>289.70 <b>(-50.11%)</b></td><td>254.28 <b>(-38.95%)</b></td><td>261.50 <b>(-36.56%)</b></td><td>196.90 (-18.03%)</td><td>37.20 <b>(-71.30%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>580.70 (n/a)</td><td>416.50 (n/a)</td><td>412.20 (n/a)</td><td>240.20 (n/a)</td><td>129.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (-0.28%)</td><td>0.01 (-5.60%)</td><td>0.02 <b>(+30.53%)</b></td><td>0.00 <b>(-79.65%)</b></td><td>0.01 <b>(+79.02%)</b></td><td>2404.80 <b>(+391.38%)</b></td><td>742.18 <b>(+100.21%)</b></td><td>289.60 <b>(-23.39%)</b></td><td>241.60 (+0.29%)</td><td>934.26 <b>(+861.41%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.40 (n/a)</td><td>370.70 (n/a)</td><td>378.00 (n/a)</td><td>240.90 (n/a)</td><td>97.18 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (+1.91%)</td><td>0.01 (-0.80%)</td><td>0.01 <b>(+23.47%)</b></td><td>0.00 <b>(-40.67%)</b></td><td>0.01 (+16.70%)</td><td>1137.00 <b>(+68.57%)</b></td><td>514.10 (+16.41%)</td><td>382.00 (-19.02%)</td><td>270.10 (-1.85%)</td><td>357.72 <b>(+116.13%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>674.50 (n/a)</td><td>441.64 (n/a)</td><td>471.70 (n/a)</td><td>275.20 (n/a)</td><td>165.51 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (+17.91%)</td><td>0.01 (+6.02%)</td><td>0.01 (-5.69%)</td><td>0.01 <b>(+88.89%)</b></td><td>0.00 (+7.04%)</td><td>983.30 <b>(-47.05%)</b></td><td>587.54 <b>(-20.40%)</b></td><td>521.20 (+6.02%)</td><td>303.80 (-15.19%)</td><td>265.89 <b>(-57.69%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1857.20 (n/a)</td><td>738.12 (n/a)</td><td>491.60 (n/a)</td><td>358.20 (n/a)</td><td>628.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (-4.55%)</td><td>0.03 (-8.05%)</td><td>0.03 (-18.05%)</td><td>0.02 (-7.92%)</td><td>0.01 (-3.53%)</td><td>562.80 (+8.61%)</td><td>334.90 (+9.14%)</td><td>303.90 <b>(+22.00%)</b></td><td>238.90 (+4.78%)</td><td>131.80 (+9.14%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.20 (n/a)</td><td>306.86 (n/a)</td><td>249.10 (n/a)</td><td>228.00 (n/a)</td><td>120.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (-5.78%)</td><td>0.03 <b>(-22.23%)</b></td><td>0.02 <b>(-37.55%)</b></td><td>0.02 (-3.41%)</td><td>0.01 (+6.36%)</td><td>601.10 (+3.53%)</td><td>426.72 <b>(+31.61%)</b></td><td>449.50 <b>(+60.14%)</b></td><td>238.00 (+6.16%)</td><td>165.77 (+12.91%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>580.60 (n/a)</td><td>324.24 (n/a)</td><td>280.70 (n/a)</td><td>224.20 (n/a)</td><td>146.82 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (+14.79%)</td><td>0.03 (+2.99%)</td><td>0.02 <b>(-30.54%)</b></td><td>0.02 <b>(+187.46%)</b></td><td>0.01 (-3.83%)</td><td>664.00 <b>(-65.21%)</b></td><td>429.32 <b>(-32.78%)</b></td><td>454.90 <b>(+43.96%)</b></td><td>233.80 (-12.89%)</td><td>180.96 <b>(-74.57%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1908.60 (n/a)</td><td>638.72 (n/a)</td><td>316.00 (n/a)</td><td>268.40 (n/a)</td><td>711.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (-10.13%)</td><td>0.02 (+2.70%)</td><td>0.02 (-6.21%)</td><td>0.02 <b>(+51.30%)</b></td><td>0.01 <b>(-32.58%)</b></td><td>535.70 <b>(-33.90%)</b></td><td>460.86 (-9.75%)</td><td>528.40 (+6.62%)</td><td>312.00 (+11.27%)</td><td>102.54 <b>(-48.35%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>810.50 (n/a)</td><td>510.64 (n/a)</td><td>495.60 (n/a)</td><td>280.40 (n/a)</td><td>198.55 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (+2.57%)</td><td>0.02 (+3.21%)</td><td>0.02 (+14.20%)</td><td>0.00 <b>(-76.18%)</b></td><td>0.01 <b>(+49.15%)</b></td><td>2474.00 <b>(+319.75%)</b></td><td>815.94 <b>(+62.38%)</b></td><td>486.10 (-12.43%)</td><td>263.00 (-2.52%)</td><td>933.32 <b>(+604.49%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>589.40 (n/a)</td><td>502.50 (n/a)</td><td>555.10 (n/a)</td><td>269.80 (n/a)</td><td>132.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (+3.28%)</td><td>0.02 (-3.64%)</td><td>0.02 (-4.48%)</td><td>0.01 <b>(-67.13%)</b></td><td>0.01 <b>(+73.15%)</b></td><td>1918.70 <b>(+204.27%)</b></td><td>691.70 <b>(+53.39%)</b></td><td>458.00 (+4.69%)</td><td>290.70 (-3.16%)</td><td>689.96 <b>(+467.61%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>630.60 (n/a)</td><td>450.94 (n/a)</td><td>437.50 (n/a)</td><td>300.20 (n/a)</td><td>121.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (+17.58%)</td><td>0.06 (-0.19%)</td><td>0.05 (-9.20%)</td><td>0.02 <b>(-23.49%)</b></td><td>0.03 <b>(+30.07%)</b></td><td>854.80 <b>(+30.70%)</b></td><td>454.88 (+11.31%)</td><td>458.90 (+10.13%)</td><td>209.50 (-14.98%)</td><td>254.91 <b>(+50.67%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>654.00 (n/a)</td><td>408.66 (n/a)</td><td>416.70 (n/a)</td><td>246.40 (n/a)</td><td>169.19 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (+4.92%)</td><td>0.07 (+16.43%)</td><td>0.07 <b>(+58.97%)</b></td><td>0.04 (-5.70%)</td><td>0.03 (-10.18%)</td><td>571.40 (+6.05%)</td><td>327.26 (-16.45%)</td><td>284.70 <b>(-37.10%)</b></td><td>197.10 (-4.64%)</td><td>145.34 (-5.81%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>538.80 (n/a)</td><td>391.68 (n/a)</td><td>452.60 (n/a)</td><td>206.70 (n/a)</td><td>154.31 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 <b>(-21.13%)</b></td><td>0.04 <b>(-46.46%)</b></td><td>0.05 <b>(-38.80%)</b></td><td>0.01 <b>(-88.78%)</b></td><td>0.02 <b>(+277.68%)</b></td><td>2447.40 <b>(+791.58%)</b></td><td>824.02 <b>(+215.79%)</b></td><td>447.50 <b>(+63.44%)</b></td><td>301.10 <b>(+26.78%)</b></td><td>910.12 <b>(+4897.68%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>274.50 (n/a)</td><td>260.94 (n/a)</td><td>273.80 (n/a)</td><td>237.50 (n/a)</td><td>18.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 <b>(-30.04%)</b></td><td>0.06 (-19.51%)</td><td>0.07 (-8.54%)</td><td>0.03 (-9.55%)</td><td>0.02 <b>(-30.63%)</b></td><td>623.70 (+10.57%)</td><td>386.08 <b>(+20.22%)</b></td><td>291.40 (+9.34%)</td><td>263.30 <b>(+42.94%)</b></td><td>154.74 (+4.40%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>564.10 (n/a)</td><td>321.14 (n/a)</td><td>266.50 (n/a)</td><td>184.20 (n/a)</td><td>148.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 <b>(-23.34%)</b></td><td>0.06 (-15.14%)</td><td>0.06 <b>(-26.30%)</b></td><td>0.04 (-0.43%)</td><td>0.02 <b>(-37.65%)</b></td><td>596.20 (+0.44%)</td><td>410.70 (+8.51%)</td><td>373.80 <b>(+35.68%)</b></td><td>285.20 <b>(+30.41%)</b></td><td>133.39 <b>(-23.89%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>593.60 (n/a)</td><td>378.48 (n/a)</td><td>275.50 (n/a)</td><td>218.70 (n/a)</td><td>175.26 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (+4.27%)</td><td>0.05 (+3.20%)</td><td>0.05 (-9.65%)</td><td>0.03 (-7.41%)</td><td>0.02 (+1.18%)</td><td>700.50 (+8.00%)</td><td>441.42 (-3.28%)</td><td>426.60 (+10.69%)</td><td>253.40 (-4.09%)</td><td>163.25 (+0.49%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>648.60 (n/a)</td><td>456.40 (n/a)</td><td>385.40 (n/a)</td><td>264.20 (n/a)</td><td>162.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.00 (n/a)</td><td>348.94 (n/a)</td><td>295.70 (n/a)</td><td>267.50 (n/a)</td><td>97.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.60 (n/a)</td><td>431.18 (n/a)</td><td>473.20 (n/a)</td><td>234.70 (n/a)</td><td>134.63 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1045.90 (n/a)</td><td>549.26 (n/a)</td><td>445.00 (n/a)</td><td>339.70 (n/a)</td><td>282.17 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>586.80 (n/a)</td><td>385.68 (n/a)</td><td>305.80 (n/a)</td><td>243.70 (n/a)</td><td>150.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>584.80 (n/a)</td><td>386.64 (n/a)</td><td>292.10 (n/a)</td><td>257.50 (n/a)</td><td>150.55 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>549.00 (n/a)</td><td>432.66 (n/a)</td><td>490.60 (n/a)</td><td>251.40 (n/a)</td><td>129.83 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>557.50 (n/a)</td><td>390.82 (n/a)</td><td>327.80 (n/a)</td><td>233.20 (n/a)</td><td>150.30 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>647.00 (n/a)</td><td>445.52 (n/a)</td><td>415.00 (n/a)</td><td>274.10 (n/a)</td><td>147.22 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1868.50 (n/a)</td><td>661.06 (n/a)</td><td>445.80 (n/a)</td><td>228.30 (n/a)</td><td>688.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.18 <b>(-21.93%)</b></td><td>0.13 <b>(-33.83%)</b></td><td>0.11 <b>(-44.19%)</b></td><td>0.08 <b>(-47.74%)</b></td><td>0.04 <b>(+55.23%)</b></td><td>581.90 <b>(+91.35%)</b></td><td>412.88 <b>(+60.58%)</b></td><td>445.10 <b>(+79.19%)</b></td><td>273.70 <b>(+28.08%)</b></td><td>123.37 <b>(+269.47%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>304.10 (n/a)</td><td>257.12 (n/a)</td><td>248.40 (n/a)</td><td>213.70 (n/a)</td><td>33.39 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>589.70 (n/a)</td><td>427.18 (n/a)</td><td>441.70 (n/a)</td><td>250.60 (n/a)</td><td>131.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>532.70 (n/a)</td><td>459.14 (n/a)</td><td>457.00 (n/a)</td><td>369.40 (n/a)</td><td>62.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>538.00 (n/a)</td><td>370.20 (n/a)</td><td>294.30 (n/a)</td><td>252.90 (n/a)</td><td>131.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.50 (n/a)</td><td>440.30 (n/a)</td><td>483.90 (n/a)</td><td>245.80 (n/a)</td><td>151.19 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.10 (n/a)</td><td>391.56 (n/a)</td><td>320.10 (n/a)</td><td>242.60 (n/a)</td><td>160.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.00 (n/a)</td><td>377.94 (n/a)</td><td>419.00 (n/a)</td><td>231.00 (n/a)</td><td>118.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>558.20 (n/a)</td><td>312.56 (n/a)</td><td>256.50 (n/a)</td><td>228.90 (n/a)</td><td>138.74 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>396.60 (n/a)</td><td>311.94 (n/a)</td><td>366.90 (n/a)</td><td>185.90 (n/a)</td><td>97.92 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>362.60 (n/a)</td><td>287.66 (n/a)</td><td>267.70 (n/a)</td><td>251.60 (n/a)</td><td>47.17 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>582.00 (n/a)</td><td>378.72 (n/a)</td><td>288.80 (n/a)</td><td>259.00 (n/a)</td><td>148.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>546.20 (n/a)</td><td>394.64 (n/a)</td><td>424.50 (n/a)</td><td>249.10 (n/a)</td><td>120.82 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>484.50 (n/a)</td><td>330.56 (n/a)</td><td>289.10 (n/a)</td><td>243.40 (n/a)</td><td>101.95 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>595.30 (n/a)</td><td>337.86 (n/a)</td><td>258.60 (n/a)</td><td>156.70 (n/a)</td><td>179.15 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>322.60 (n/a)</td><td>259.82 (n/a)</td><td>246.00 (n/a)</td><td>202.80 (n/a)</td><td>47.77 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.10 (n/a)</td><td>287.44 (n/a)</td><td>240.40 (n/a)</td><td>192.90 (n/a)</td><td>105.97 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1041.90 (n/a)</td><td>491.52 (n/a)</td><td>333.30 (n/a)</td><td>236.50 (n/a)</td><td>335.49 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1920.50 (n/a)</td><td>818.12 (n/a)</td><td>589.80 (n/a)</td><td>214.70 (n/a)</td><td>713.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.40 (n/a)</td><td>376.72 (n/a)</td><td>367.30 (n/a)</td><td>235.80 (n/a)</td><td>113.83 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>653.70 (n/a)</td><td>507.98 (n/a)</td><td>547.60 (n/a)</td><td>330.20 (n/a)</td><td>151.01 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.80 (n/a)</td><td>349.62 (n/a)</td><td>310.90 (n/a)</td><td>245.80 (n/a)</td><td>109.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1946.40 (n/a)</td><td>687.72 (n/a)</td><td>467.40 (n/a)</td><td>238.40 (n/a)</td><td>712.54 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2490.80 (n/a)</td><td>774.18 (n/a)</td><td>281.10 (n/a)</td><td>258.80 (n/a)</td><td>967.87 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1100.30 (n/a)</td><td>475.06 (n/a)</td><td>273.20 (n/a)</td><td>256.60 (n/a)</td><td>362.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.10 (n/a)</td><td>394.98 (n/a)</td><td>367.60 (n/a)</td><td>242.00 (n/a)</td><td>148.58 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>636.70 (n/a)</td><td>468.34 (n/a)</td><td>453.70 (n/a)</td><td>365.70 (n/a)</td><td>104.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>502.40 (n/a)</td><td>324.74 (n/a)</td><td>295.60 (n/a)</td><td>259.20 (n/a)</td><td>101.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>809.50 (n/a)</td><td>545.66 (n/a)</td><td>522.90 (n/a)</td><td>288.10 (n/a)</td><td>189.01 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>530.50 (n/a)</td><td>411.14 (n/a)</td><td>460.10 (n/a)</td><td>267.40 (n/a)</td><td>124.24 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>472.80 (n/a)</td><td>342.58 (n/a)</td><td>276.00 (n/a)</td><td>241.20 (n/a)</td><td>115.65 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>503.00 (n/a)</td><td>393.82 (n/a)</td><td>490.60 (n/a)</td><td>207.50 (n/a)</td><td>143.82 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>829.10 (n/a)</td><td>468.20 (n/a)</td><td>302.20 (n/a)</td><td>254.00 (n/a)</td><td>269.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>451.20 (n/a)</td><td>337.78 (n/a)</td><td>300.70 (n/a)</td><td>290.40 (n/a)</td><td>67.58 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1937.10 (n/a)</td><td>758.88 (n/a)</td><td>535.80 (n/a)</td><td>276.00 (n/a)</td><td>670.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>534.10 (n/a)</td><td>346.32 (n/a)</td><td>274.80 (n/a)</td><td>209.20 (n/a)</td><td>140.87 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>657.10 (n/a)</td><td>453.68 (n/a)</td><td>443.90 (n/a)</td><td>272.10 (n/a)</td><td>156.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>534.90 (n/a)</td><td>366.00 (n/a)</td><td>297.10 (n/a)</td><td>239.30 (n/a)</td><td>129.89 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>515.70 (n/a)</td><td>456.20 (n/a)</td><td>470.30 (n/a)</td><td>380.10 (n/a)</td><td>50.90 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.57 <b>(+61.14%)</b></td><td>0.50 <b>(+106.88%)</b></td><td>0.54 <b>(+121.25%)</b></td><td>0.36 <b>(+297.21%)</b></td><td>0.09 (-17.14%)</td><td>622.40 <b>(-74.82%)</b></td><td>460.38 <b>(-61.15%)</b></td><td>407.50 <b>(-54.81%)</b></td><td>387.50 <b>(-37.95%)</b></td><td>99.56 <b>(-86.97%)</b></td><td>24.35 <b>(+61.14%)</b></td><td>21.17 <b>(+106.88%)</b></td><td>23.16 <b>(+121.25%)</b></td><td>15.16 <b>(+297.21%)</b></td><td>3.92 (-17.14%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>2472.20 (n/a)</td><td>1185.06 (n/a)</td><td>901.70 (n/a)</td><td>624.50 (n/a)</td><td>764.17 (n/a)</td><td>15.11 (n/a)</td><td>10.23 (n/a)</td><td>10.47 (n/a)</td><td>3.82 (n/a)</td><td>4.74 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.61 <b>(+20.50%)</b></td><td>0.44 (+1.69%)</td><td>0.37 <b>(-21.83%)</b></td><td>0.34 <b>(+32.66%)</b></td><td>0.12 <b>(+23.44%)</b></td><td>646.60 <b>(-24.61%)</b></td><td>532.06 (-2.04%)</td><td>604.70 <b>(+27.92%)</b></td><td>362.80 (-17.02%)</td><td>134.48 <b>(-24.15%)</b></td><td>26.01 <b>(+20.50%)</b></td><td>18.81 (+1.69%)</td><td>15.61 <b>(-21.83%)</b></td><td>14.60 <b>(+32.66%)</b></td><td>5.31 <b>(+23.44%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.47 (n/a)</td><td>0.26 (n/a)</td><td>0.10 (n/a)</td><td>857.70 (n/a)</td><td>543.12 (n/a)</td><td>472.70 (n/a)</td><td>437.20 (n/a)</td><td>177.30 (n/a)</td><td>21.58 (n/a)</td><td>18.49 (n/a)</td><td>19.97 (n/a)</td><td>11.00 (n/a)</td><td>4.30 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.31 (-0.28%)</td><td>0.31 (-0.68%)</td><td>0.31 (-1.05%)</td><td>0.30 (-1.41%)</td><td>0.00 <b>(+52.98%)</b></td><td>83093.10 (+1.43%)</td><td>81709.36 (+0.69%)</td><td>81620.70 (+1.06%)</td><td>80794.60 (+0.28%)</td><td>973.57 <b>(+55.31%)</b></td><td>212.64 (-0.28%)</td><td>210.28 (-0.68%)</td><td>210.48 (-1.05%)</td><td>206.75 (-1.41%)</td><td>2.50 <b>(+52.97%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.00 (n/a)</td><td>81921.90 (n/a)</td><td>81147.00 (n/a)</td><td>80762.80 (n/a)</td><td>80569.30 (n/a)</td><td>626.87 (n/a)</td><td>213.23 (n/a)</td><td>211.72 (n/a)</td><td>212.72 (n/a)</td><td>209.71 (n/a)</td><td>1.63 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>1.03 (-0.04%)</td><td>1.02 (+0.79%)</td><td>1.01 (-0.07%)</td><td>1.01 (+2.58%)</td><td>0.01 <b>(-44.79%)</b></td><td>25031.70 (-2.52%)</td><td>24723.36 (-0.82%)</td><td>24812.50 (+0.07%)</td><td>24357.10 (+0.04%)</td><td>329.98 <b>(-46.08%)</b></td><td>705.33 (-0.04%)</td><td>694.98 (+0.79%)</td><td>692.39 (-0.07%)</td><td>686.32 (+2.58%)</td><td>9.30 <b>(-44.79%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25677.50 (n/a)</td><td>24927.90 (n/a)</td><td>24795.60 (n/a)</td><td>24347.50 (n/a)</td><td>611.98 (n/a)</td><td>705.61 (n/a)</td><td>689.51 (n/a)</td><td>692.86 (n/a)</td><td>669.06 (n/a)</td><td>16.85 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.82 (+0.40%)</td><td>0.80 (+0.92%)</td><td>0.80 (+0.45%)</td><td>0.78 (+0.50%)</td><td>0.01 (-4.93%)</td><td>96908.60 (-0.50%)</td><td>94128.12 (-0.91%)</td><td>94004.00 (-0.45%)</td><td>92457.40 (-0.40%)</td><td>1742.76 (-5.80%)</td><td>743.26 (+0.40%)</td><td>730.26 (+0.92%)</td><td>731.03 (+0.45%)</td><td>709.12 (+0.50%)</td><td>13.35 (-4.93%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.02 (n/a)</td><td>97395.20 (n/a)</td><td>94996.36 (n/a)</td><td>94426.70 (n/a)</td><td>92831.80 (n/a)</td><td>1849.98 (n/a)</td><td>740.26 (n/a)</td><td>723.61 (n/a)</td><td>727.75 (n/a)</td><td>705.57 (n/a)</td><td>14.04 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.77 (-0.65%)</td><td>0.75 (-1.86%)</td><td>0.75 (-2.48%)</td><td>0.73 (-2.67%)</td><td>0.02 <b>(+67.59%)</b></td><td>102910.70 (+2.75%)</td><td>100273.96 (+1.92%)</td><td>100971.50 (+2.54%)</td><td>97741.70 (+0.66%)</td><td>2141.60 <b>(+73.06%)</b></td><td>703.07 (-0.65%)</td><td>685.57 (-1.86%)</td><td>680.58 (-2.48%)</td><td>667.76 (-2.67%)</td><td>14.67 <b>(+67.59%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100159.40 (n/a)</td><td>98387.06 (n/a)</td><td>98468.10 (n/a)</td><td>97105.20 (n/a)</td><td>1237.50 (n/a)</td><td>707.68 (n/a)</td><td>698.55 (n/a)</td><td>697.89 (n/a)</td><td>686.10 (n/a)</td><td>8.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.80 (-0.04%)</td><td>0.80 (+0.72%)</td><td>0.80 (+1.32%)</td><td>0.79 (+0.57%)</td><td>0.01 <b>(-26.86%)</b></td><td>96028.40 (-0.56%)</td><td>94860.02 (-0.72%)</td><td>94650.60 (-1.30%)</td><td>94459.60 (+0.04%)</td><td>660.07 <b>(-27.12%)</b></td><td>727.50 (-0.04%)</td><td>724.46 (+0.72%)</td><td>726.03 (+1.32%)</td><td>715.62 (+0.57%)</td><td>5.00 <b>(-26.86%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96573.20 (n/a)</td><td>95545.90 (n/a)</td><td>95896.30 (n/a)</td><td>94417.90 (n/a)</td><td>905.73 (n/a)</td><td>727.82 (n/a)</td><td>719.28 (n/a)</td><td>716.60 (n/a)</td><td>711.58 (n/a)</td><td>6.83 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.65 (-14.40%)</td><td>4.01 (-7.92%)</td><td>4.10 (-7.05%)</td><td>2.94 (+4.52%)</td><td>0.65 <b>(-42.19%)</b></td><td>3032.90 (-4.32%)</td><td>2279.14 (+4.77%)</td><td>2172.70 (+7.58%)</td><td>1915.10 (+16.82%)</td><td>437.18 <b>(-31.25%)</b></td><td>280.33 (-14.40%)</td><td>241.49 (-7.92%)</td><td>247.10 (-7.05%)</td><td>177.02 (+4.52%)</td><td>38.95 <b>(-42.19%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.44 (n/a)</td><td>4.35 (n/a)</td><td>4.41 (n/a)</td><td>2.81 (n/a)</td><td>1.12 (n/a)</td><td>3169.90 (n/a)</td><td>2175.38 (n/a)</td><td>2019.60 (n/a)</td><td>1639.40 (n/a)</td><td>635.86 (n/a)</td><td>327.48 (n/a)</td><td>262.26 (n/a)</td><td>265.83 (n/a)</td><td>169.37 (n/a)</td><td>67.38 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.46 (+14.33%)</td><td>2.80 (+4.08%)</td><td>2.27 (-14.06%)</td><td>2.13 (+2.90%)</td><td>0.98 <b>(+34.24%)</b></td><td>4185.70 (-2.82%)</td><td>3433.54 (-1.33%)</td><td>3934.60 (+16.36%)</td><td>1997.60 (-12.54%)</td><td>923.93 (+14.60%)</td><td>268.76 (+14.33%)</td><td>168.92 (+4.08%)</td><td>136.45 (-14.06%)</td><td>128.26 (+2.90%)</td><td>59.25 <b>(+34.24%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.90 (n/a)</td><td>2.69 (n/a)</td><td>2.64 (n/a)</td><td>2.07 (n/a)</td><td>0.73 (n/a)</td><td>4307.30 (n/a)</td><td>3479.94 (n/a)</td><td>3381.40 (n/a)</td><td>2283.90 (n/a)</td><td>806.23 (n/a)</td><td>235.06 (n/a)</td><td>162.30 (n/a)</td><td>158.77 (n/a)</td><td>124.64 (n/a)</td><td>44.14 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>5.37 (+2.27%)</td><td>4.41 <b>(+41.87%)</b></td><td>5.17 <b>(+132.73%)</b></td><td>2.20 (+14.68%)</td><td>1.34 (-8.08%)</td><td>4047.10 (-12.80%)</td><td>2265.78 <b>(-32.24%)</b></td><td>1722.60 <b>(-57.03%)</b></td><td>1658.30 (-2.22%)</td><td>1018.61 <b>(-21.10%)</b></td><td>323.74 (+2.27%)</td><td>265.39 <b>(+41.87%)</b></td><td>311.67 <b>(+132.73%)</b></td><td>132.66 (+14.68%)</td><td>80.47 (-8.08%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.26 (n/a)</td><td>3.11 (n/a)</td><td>2.22 (n/a)</td><td>1.92 (n/a)</td><td>1.45 (n/a)</td><td>4641.00 (n/a)</td><td>3344.06 (n/a)</td><td>4008.90 (n/a)</td><td>1696.00 (n/a)</td><td>1291.04 (n/a)</td><td>316.54 (n/a)</td><td>187.07 (n/a)</td><td>133.92 (n/a)</td><td>115.68 (n/a)</td><td>87.55 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>5.62 (-16.39%)</td><td>4.55 (-17.21%)</td><td>4.38 (-14.29%)</td><td>3.54 (-17.56%)</td><td>0.80 <b>(-31.20%)</b></td><td>9852.50 <b>(+21.30%)</b></td><td>7852.72 (+19.58%)</td><td>7959.10 (+16.67%)</td><td>6201.80 (+19.60%)</td><td>1390.02 (+3.55%)</td><td>346.27 (-16.39%)</td><td>280.33 (-17.21%)</td><td>269.82 (-14.29%)</td><td>217.96 (-17.56%)</td><td>49.00 <b>(-31.20%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>6.72 (n/a)</td><td>5.50 (n/a)</td><td>5.11 (n/a)</td><td>4.29 (n/a)</td><td>1.16 (n/a)</td><td>8122.70 (n/a)</td><td>6567.02 (n/a)</td><td>6822.10 (n/a)</td><td>5185.50 (n/a)</td><td>1342.33 (n/a)</td><td>414.13 (n/a)</td><td>338.60 (n/a)</td><td>314.78 (n/a)</td><td>264.38 (n/a)</td><td>71.22 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>5.62 (-4.60%)</td><td>4.97 (+1.42%)</td><td>5.17 (+7.86%)</td><td>4.01 (-5.90%)</td><td>0.68 (-0.72%)</td><td>8695.70 (+6.27%)</td><td>7123.04 (-1.29%)</td><td>6739.40 (-7.28%)</td><td>6207.40 (+4.82%)</td><td>1045.09 (+8.45%)</td><td>345.95 (-4.60%)</td><td>306.37 (+1.42%)</td><td>318.64 (+7.86%)</td><td>246.96 (-5.90%)</td><td>41.82 (-0.72%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.89 (n/a)</td><td>4.90 (n/a)</td><td>4.80 (n/a)</td><td>4.26 (n/a)</td><td>0.68 (n/a)</td><td>8182.80 (n/a)</td><td>7216.30 (n/a)</td><td>7268.90 (n/a)</td><td>5921.90 (n/a)</td><td>963.68 (n/a)</td><td>362.64 (n/a)</td><td>302.07 (n/a)</td><td>295.44 (n/a)</td><td>262.44 (n/a)</td><td>42.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>6.17 (+12.60%)</td><td>5.26 (+11.33%)</td><td>5.26 (+9.13%)</td><td>4.31 (+9.58%)</td><td>0.66 (+5.62%)</td><td>8095.90 (-8.74%)</td><td>6715.78 (-10.29%)</td><td>6627.20 (-8.37%)</td><td>5653.80 (-11.19%)</td><td>877.86 (-13.68%)</td><td>379.83 (+12.60%)</td><td>323.98 (+11.33%)</td><td>324.04 (+9.13%)</td><td>265.26 (+9.58%)</td><td>40.65 (+5.62%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.48 (n/a)</td><td>4.72 (n/a)</td><td>4.82 (n/a)</td><td>3.93 (n/a)</td><td>0.62 (n/a)</td><td>8871.60 (n/a)</td><td>7486.36 (n/a)</td><td>7232.30 (n/a)</td><td>6366.30 (n/a)</td><td>1016.97 (n/a)</td><td>337.32 (n/a)</td><td>291.02 (n/a)</td><td>296.93 (n/a)</td><td>242.06 (n/a)</td><td>38.49 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.78 (+0.20%)</td><td>0.76 (+0.40%)</td><td>0.76 (+1.73%)</td><td>0.73 (-2.22%)</td><td>0.02 <b>(+38.38%)</b></td><td>103649.10 (+2.27%)</td><td>99461.72 (-0.36%)</td><td>98967.50 (-1.70%)</td><td>96284.40 (-0.20%)</td><td>2861.11 <b>(+41.50%)</b></td><td>713.71 (+0.20%)</td><td>691.37 (+0.40%)</td><td>694.36 (+1.73%)</td><td>663.00 (-2.22%)</td><td>19.68 <b>(+38.38%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>101350.80 (n/a)</td><td>99825.72 (n/a)</td><td>100682.60 (n/a)</td><td>96479.50 (n/a)</td><td>2022.02 (n/a)</td><td>712.27 (n/a)</td><td>688.62 (n/a)</td><td>682.54 (n/a)</td><td>678.04 (n/a)</td><td>14.22 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.78 (+0.78%)</td><td>0.75 (-0.91%)</td><td>0.76 (-0.33%)</td><td>0.71 (-4.26%)</td><td>0.03 <b>(+142.03%)</b></td><td>106103.40 (+4.45%)</td><td>100277.20 (+1.01%)</td><td>99440.10 (+0.33%)</td><td>96645.80 (-0.77%)</td><td>3765.85 <b>(+150.68%)</b></td><td>711.04 (+0.78%)</td><td>686.05 (-0.91%)</td><td>691.06 (-0.33%)</td><td>647.66 (-4.26%)</td><td>25.21 <b>(+142.03%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101586.30 (n/a)</td><td>99271.92 (n/a)</td><td>99111.20 (n/a)</td><td>97395.50 (n/a)</td><td>1502.27 (n/a)</td><td>705.57 (n/a)</td><td>692.36 (n/a)</td><td>693.36 (n/a)</td><td>676.46 (n/a)</td><td>10.41 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.81 (+0.64%)</td><td>0.80 (+1.17%)</td><td>0.80 (+1.41%)</td><td>0.80 (+1.62%)</td><td>0.00 <b>(-42.83%)</b></td><td>94656.40 (-1.59%)</td><td>94023.98 (-1.16%)</td><td>93814.80 (-1.39%)</td><td>93759.00 (-0.64%)</td><td>381.09 <b>(-44.15%)</b></td><td>732.94 (+0.64%)</td><td>730.88 (+1.17%)</td><td>732.50 (+1.41%)</td><td>725.99 (+1.62%)</td><td>2.95 <b>(-42.83%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96189.00 (n/a)</td><td>95123.36 (n/a)</td><td>95141.10 (n/a)</td><td>94360.80 (n/a)</td><td>682.32 (n/a)</td><td>728.26 (n/a)</td><td>722.45 (n/a)</td><td>722.29 (n/a)</td><td>714.42 (n/a)</td><td>5.16 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>3.93 (+14.50%)</td><td>3.02 <b>(+50.61%)</b></td><td>3.78 <b>(+110.49%)</b></td><td>1.78 <b>(+61.09%)</b></td><td>1.13 <b>(+30.78%)</b></td><td>4535.60 <b>(-37.92%)</b></td><td>3065.24 <b>(-33.10%)</b></td><td>2135.00 <b>(-52.49%)</b></td><td>2050.40 (-12.67%)</td><td>1322.53 <b>(-25.51%)</b></td><td>1030.97 (+14.50%)</td><td>791.58 <b>(+50.61%)</b></td><td>990.14 <b>(+110.49%)</b></td><td>466.08 <b>(+61.09%)</b></td><td>295.44 <b>(+30.78%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.43 (n/a)</td><td>2.00 (n/a)</td><td>1.79 (n/a)</td><td>1.10 (n/a)</td><td>0.86 (n/a)</td><td>7306.10 (n/a)</td><td>4581.94 (n/a)</td><td>4494.00 (n/a)</td><td>2347.80 (n/a)</td><td>1775.45 (n/a)</td><td>900.40 (n/a)</td><td>525.58 (n/a)</td><td>470.39 (n/a)</td><td>289.34 (n/a)</td><td>225.91 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.29 (+1.11%)</td><td>0.22 (+6.59%)</td><td>0.19 (-0.53%)</td><td>0.19 (+18.21%)</td><td>0.04 (-11.01%)</td><td>6722.50 (-15.41%)</td><td>5874.48 (-7.20%)</td><td>6400.50 (+0.54%)</td><td>4360.40 (-1.10%)</td><td>977.73 <b>(-22.77%)</b></td><td>15.39 (+1.11%)</td><td>11.72 (+6.59%)</td><td>10.48 (-0.53%)</td><td>9.98 (+18.21%)</td><td>2.25 (-11.01%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>7946.90 (n/a)</td><td>6330.52 (n/a)</td><td>6366.40 (n/a)</td><td>4408.90 (n/a)</td><td>1266.06 (n/a)</td><td>15.22 (n/a)</td><td>11.00 (n/a)</td><td>10.54 (n/a)</td><td>8.44 (n/a)</td><td>2.52 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>3.83 (n/a)</td><td>3.60 (n/a)</td><td>3.53 (n/a)</td><td>3.43 (n/a)</td><td>0.17 (n/a)</td><td>3.83 (n/a)</td><td>3.60 (n/a)</td><td>3.53 (n/a)</td><td>3.43 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>7.29 (+1.53%)</td><td>6.04 (-2.42%)</td><td>5.85 (-2.43%)</td><td>4.71 (-10.22%)</td><td>0.99 <b>(+21.76%)</b></td><td>7.29 (+1.53%)</td><td>6.03 (-2.42%)</td><td>5.84 (-2.43%)</td><td>4.71 (-10.22%)</td><td>0.99 <b>(+21.76%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>7.18 (n/a)</td><td>6.19 (n/a)</td><td>5.99 (n/a)</td><td>5.24 (n/a)</td><td>0.81 (n/a)</td><td>7.18 (n/a)</td><td>6.18 (n/a)</td><td>5.99 (n/a)</td><td>5.24 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>14.43 (+3.30%)</td><td>10.25 (+5.05%)</td><td>8.44 (-1.67%)</td><td>6.09 <b>(-24.93%)</b></td><td>3.73 <b>(+54.06%)</b></td><td>14.42 (+3.30%)</td><td>10.24 (+5.05%)</td><td>8.44 (-1.67%)</td><td>6.09 <b>(-24.93%)</b></td><td>3.73 <b>(+54.06%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>13.97 (n/a)</td><td>9.75 (n/a)</td><td>8.59 (n/a)</td><td>8.11 (n/a)</td><td>2.42 (n/a)</td><td>13.96 (n/a)</td><td>9.75 (n/a)</td><td>8.58 (n/a)</td><td>8.11 (n/a)</td><td>2.42 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>3.93 (n/a)</td><td>3.73 (n/a)</td><td>3.66 (n/a)</td><td>3.62 (n/a)</td><td>0.13 (n/a)</td><td>3.93 (n/a)</td><td>3.73 (n/a)</td><td>3.66 (n/a)</td><td>3.61 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>7.67 (+9.46%)</td><td>6.40 (+0.22%)</td><td>6.31 (-1.64%)</td><td>5.02 (-15.12%)</td><td>0.98 <b>(+126.37%)</b></td><td>7.66 (+9.46%)</td><td>6.40 (+0.22%)</td><td>6.31 (-1.64%)</td><td>5.01 (-15.12%)</td><td>0.98 <b>(+126.37%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>7.00 (n/a)</td><td>6.39 (n/a)</td><td>6.42 (n/a)</td><td>5.91 (n/a)</td><td>0.43 (n/a)</td><td>7.00 (n/a)</td><td>6.39 (n/a)</td><td>6.42 (n/a)</td><td>5.91 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>13.43 (+4.31%)</td><td>9.47 (+3.56%)</td><td>8.20 (+0.51%)</td><td>8.05 (+9.82%)</td><td>2.30 (-0.72%)</td><td>13.43 (+4.31%)</td><td>9.46 (+3.56%)</td><td>8.19 (+0.51%)</td><td>8.05 (+9.82%)</td><td>2.30 (-0.72%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>12.88 (n/a)</td><td>9.14 (n/a)</td><td>8.15 (n/a)</td><td>7.33 (n/a)</td><td>2.32 (n/a)</td><td>12.87 (n/a)</td><td>9.14 (n/a)</td><td>8.15 (n/a)</td><td>7.33 (n/a)</td><td>2.32 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>3.01 (-2.46%)</td><td>1.96 (-2.12%)</td><td>1.70 (-0.82%)</td><td>1.02 (-0.91%)</td><td>0.93 (-3.95%)</td><td>3.00 (-2.46%)</td><td>1.95 (-2.12%)</td><td>1.69 (-0.82%)</td><td>1.02 (-0.91%)</td><td>0.93 (-3.95%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.08 (n/a)</td><td>2.00 (n/a)</td><td>1.71 (n/a)</td><td>1.03 (n/a)</td><td>0.97 (n/a)</td><td>3.07 (n/a)</td><td>1.99 (n/a)</td><td>1.71 (n/a)</td><td>1.03 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.47 (+12.52%)</td><td>0.29 (-5.68%)</td><td>0.35 (-0.80%)</td><td>0.08 <b>(-38.05%)</b></td><td>0.18 <b>(+61.20%)</b></td><td>0.46 (+12.52%)</td><td>0.29 (-5.68%)</td><td>0.34 (-0.80%)</td><td>0.07 <b>(-38.05%)</b></td><td>0.18 <b>(+61.20%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.35 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.41 (n/a)</td><td>0.31 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.74 (+1.29%)</td><td>0.62 <b>(+26.13%)</b></td><td>0.67 (+8.65%)</td><td>0.37 <b>(+168.36%)</b></td><td>0.15 <b>(-44.92%)</b></td><td>0.73 (+1.29%)</td><td>0.61 <b>(+26.13%)</b></td><td>0.66 (+8.65%)</td><td>0.37 <b>(+168.36%)</b></td><td>0.14 <b>(-44.92%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.73 (n/a)</td><td>0.49 (n/a)</td><td>0.61 (n/a)</td><td>0.14 (n/a)</td><td>0.26 (n/a)</td><td>0.72 (n/a)</td><td>0.48 (n/a)</td><td>0.61 (n/a)</td><td>0.14 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.89 (+12.57%)</td><td>1.46 <b>(+29.62%)</b></td><td>1.49 <b>(+215.99%)</b></td><td>0.44 (-1.17%)</td><td>1.04 (+8.19%)</td><td>2.84 (+12.57%)</td><td>1.44 <b>(+29.62%)</b></td><td>1.47 <b>(+215.99%)</b></td><td>0.44 (-1.17%)</td><td>1.03 (+8.19%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>2.56 (n/a)</td><td>1.13 (n/a)</td><td>0.47 (n/a)</td><td>0.45 (n/a)</td><td>0.96 (n/a)</td><td>2.52 (n/a)</td><td>1.11 (n/a)</td><td>0.46 (n/a)</td><td>0.44 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>567.60 (n/a)</td><td>359.36 (n/a)</td><td>297.00 (n/a)</td><td>252.20 (n/a)</td><td>129.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1064.50 (n/a)</td><td>462.12 (n/a)</td><td>318.40 (n/a)</td><td>221.70 (n/a)</td><td>349.79 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>846.90 (n/a)</td><td>522.20 (n/a)</td><td>540.90 (n/a)</td><td>207.20 (n/a)</td><td>235.30 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>830.50 (n/a)</td><td>511.60 (n/a)</td><td>477.00 (n/a)</td><td>315.40 (n/a)</td><td>204.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.70 (n/a)</td><td>406.82 (n/a)</td><td>385.40 (n/a)</td><td>203.60 (n/a)</td><td>161.30 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>669.20 (n/a)</td><td>510.80 (n/a)</td><td>540.90 (n/a)</td><td>367.00 (n/a)</td><td>133.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.90 (n/a)</td><td>355.38 (n/a)</td><td>278.90 (n/a)</td><td>245.90 (n/a)</td><td>126.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.90 (n/a)</td><td>375.90 (n/a)</td><td>392.80 (n/a)</td><td>263.50 (n/a)</td><td>94.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.30 (n/a)</td><td>412.82 (n/a)</td><td>436.60 (n/a)</td><td>261.80 (n/a)</td><td>152.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.20 (n/a)</td><td>525.80 (n/a)</td><td>518.10 (n/a)</td><td>466.30 (n/a)</td><td>50.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.90 (n/a)</td><td>404.72 (n/a)</td><td>445.40 (n/a)</td><td>276.90 (n/a)</td><td>114.31 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>648.90 (n/a)</td><td>524.44 (n/a)</td><td>565.40 (n/a)</td><td>364.60 (n/a)</td><td>132.77 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>530.60 (n/a)</td><td>409.70 (n/a)</td><td>497.60 (n/a)</td><td>244.80 (n/a)</td><td>145.42 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>485.50 (n/a)</td><td>371.44 (n/a)</td><td>396.60 (n/a)</td><td>245.90 (n/a)</td><td>97.77 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1917.30 (n/a)</td><td>781.84 (n/a)</td><td>570.40 (n/a)</td><td>292.00 (n/a)</td><td>672.28 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>589.30 (n/a)</td><td>488.02 (n/a)</td><td>533.70 (n/a)</td><td>365.70 (n/a)</td><td>104.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1371.20 (n/a)</td><td>538.94 (n/a)</td><td>303.10 (n/a)</td><td>249.60 (n/a)</td><td>474.02 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>682.70 (n/a)</td><td>471.26 (n/a)</td><td>514.30 (n/a)</td><td>253.00 (n/a)</td><td>177.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>481.10 (n/a)</td><td>377.82 (n/a)</td><td>413.30 (n/a)</td><td>251.50 (n/a)</td><td>110.65 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1025.70 (n/a)</td><td>603.22 (n/a)</td><td>515.60 (n/a)</td><td>355.30 (n/a)</td><td>253.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1116.30 (n/a)</td><td>662.44 (n/a)</td><td>608.70 (n/a)</td><td>288.70 (n/a)</td><td>321.50 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>520.80 (n/a)</td><td>422.42 (n/a)</td><td>448.70 (n/a)</td><td>267.50 (n/a)</td><td>101.60 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>622.30 (n/a)</td><td>498.72 (n/a)</td><td>519.10 (n/a)</td><td>291.10 (n/a)</td><td>127.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>791.40 (n/a)</td><td>506.38 (n/a)</td><td>466.40 (n/a)</td><td>330.10 (n/a)</td><td>194.95 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (+1.91%)</td><td>0.01 (+12.60%)</td><td>0.02 (+15.35%)</td><td>0.01 (+0.45%)</td><td>0.00 (+9.38%)</td><td>488.40 (-0.45%)</td><td>299.40 (-10.23%)</td><td>243.00 (-13.31%)</td><td>238.30 (-1.89%)</td><td>107.39 (+6.56%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>490.60 (n/a)</td><td>333.52 (n/a)</td><td>280.30 (n/a)</td><td>242.90 (n/a)</td><td>100.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (+8.92%)</td><td>0.01 <b>(+29.01%)</b></td><td>0.01 <b>(+61.62%)</b></td><td>0.01 <b>(+40.50%)</b></td><td>0.00 (-10.37%)</td><td>445.50 <b>(-28.82%)</b></td><td>327.48 <b>(-28.20%)</b></td><td>334.00 <b>(-38.14%)</b></td><td>220.40 (-8.20%)</td><td>102.72 <b>(-43.69%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>625.90 (n/a)</td><td>456.12 (n/a)</td><td>539.90 (n/a)</td><td>240.10 (n/a)</td><td>182.42 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 <b>(-48.24%)</b></td><td>0.01 <b>(-36.55%)</b></td><td>0.01 <b>(-46.59%)</b></td><td>0.01 (-8.64%)</td><td>0.00 <b>(-79.40%)</b></td><td>559.40 (+9.45%)</td><td>462.28 <b>(+38.91%)</b></td><td>458.50 <b>(+87.22%)</b></td><td>397.10 <b>(+93.24%)</b></td><td>60.97 <b>(-57.51%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>511.10 (n/a)</td><td>332.78 (n/a)</td><td>244.90 (n/a)</td><td>205.50 (n/a)</td><td>143.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (-3.04%)</td><td>0.01 (-1.62%)</td><td>0.01 <b>(-26.05%)</b></td><td>0.01 (+9.44%)</td><td>0.00 (+6.79%)</td><td>498.10 (-8.64%)</td><td>390.18 (+1.93%)</td><td>448.40 <b>(+35.22%)</b></td><td>257.10 (+3.13%)</td><td>120.42 (-4.76%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.20 (n/a)</td><td>382.80 (n/a)</td><td>331.60 (n/a)</td><td>249.30 (n/a)</td><td>126.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (+8.30%)</td><td>0.01 <b>(+27.00%)</b></td><td>0.02 <b>(+31.01%)</b></td><td>0.01 <b>(+210.06%)</b></td><td>0.00 (-10.54%)</td><td>800.70 <b>(-67.75%)</b></td><td>370.76 <b>(-50.93%)</b></td><td>272.10 <b>(-23.65%)</b></td><td>246.40 (-7.68%)</td><td>240.66 <b>(-75.10%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2482.70 (n/a)</td><td>755.50 (n/a)</td><td>356.40 (n/a)</td><td>266.90 (n/a)</td><td>966.42 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 <b>(+106.29%)</b></td><td>0.01 <b>(+85.91%)</b></td><td>0.01 <b>(+108.44%)</b></td><td>0.01 <b>(+80.20%)</b></td><td>0.00 <b>(+127.54%)</b></td><td>583.90 <b>(-44.50%)</b></td><td>360.78 <b>(-44.22%)</b></td><td>289.70 <b>(-52.04%)</b></td><td>219.40 <b>(-51.51%)</b></td><td>151.36 <b>(-37.61%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1052.10 (n/a)</td><td>646.78 (n/a)</td><td>604.00 (n/a)</td><td>452.50 (n/a)</td><td>242.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (+15.09%)</td><td>0.03 (+15.06%)</td><td>0.03 (+14.36%)</td><td>0.02 <b>(+278.30%)</b></td><td>0.01 (-11.46%)</td><td>505.00 <b>(-73.57%)</b></td><td>342.56 <b>(-44.36%)</b></td><td>256.20 (-12.56%)</td><td>215.00 (-13.10%)</td><td>145.05 <b>(-80.00%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1910.50 (n/a)</td><td>615.70 (n/a)</td><td>293.00 (n/a)</td><td>247.40 (n/a)</td><td>725.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 <b>(+27.73%)</b></td><td>0.02 (-2.32%)</td><td>0.02 (-16.28%)</td><td>0.01 <b>(-28.09%)</b></td><td>0.01 <b>(+71.43%)</b></td><td>664.20 <b>(+39.07%)</b></td><td>394.40 (+14.86%)</td><td>350.00 (+19.45%)</td><td>190.70 <b>(-21.68%)</b></td><td>183.91 <b>(+83.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>477.60 (n/a)</td><td>343.36 (n/a)</td><td>293.00 (n/a)</td><td>243.50 (n/a)</td><td>100.41 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (+13.03%)</td><td>0.03 (+15.09%)</td><td>0.03 (+2.34%)</td><td>0.02 <b>(+29.75%)</b></td><td>0.01 (-14.81%)</td><td>448.70 <b>(-22.93%)</b></td><td>293.74 (-17.93%)</td><td>283.10 (-2.28%)</td><td>206.90 (-11.54%)</td><td>92.39 <b>(-38.23%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.20 (n/a)</td><td>357.92 (n/a)</td><td>289.70 (n/a)</td><td>233.90 (n/a)</td><td>149.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (+6.89%)</td><td>0.03 (+3.18%)</td><td>0.03 (-0.03%)</td><td>0.02 (+0.84%)</td><td>0.01 (+5.13%)</td><td>430.20 (-0.83%)</td><td>293.10 (-2.82%)</td><td>244.20 (+0.00%)</td><td>221.60 (-6.46%)</td><td>88.25 (+0.28%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>433.80 (n/a)</td><td>301.60 (n/a)</td><td>244.20 (n/a)</td><td>236.90 (n/a)</td><td>88.01 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 <b>(+43.13%)</b></td><td>0.03 <b>(+36.10%)</b></td><td>0.03 (+15.25%)</td><td>0.02 <b>(+298.93%)</b></td><td>0.01 (-5.34%)</td><td>505.90 <b>(-74.93%)</b></td><td>298.38 <b>(-55.57%)</b></td><td>255.90 (-13.22%)</td><td>159.70 <b>(-30.11%)</b></td><td>131.69 <b>(-82.82%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2018.30 (n/a)</td><td>671.60 (n/a)</td><td>294.90 (n/a)</td><td>228.50 (n/a)</td><td>766.60 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (-13.99%)</td><td>0.02 (-4.77%)</td><td>0.02 (+15.59%)</td><td>0.01 (-1.20%)</td><td>0.01 <b>(-37.54%)</b></td><td>578.90 (+1.21%)</td><td>411.80 (-0.76%)</td><td>388.70 (-13.51%)</td><td>286.80 (+16.25%)</td><td>106.57 <b>(-24.77%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.00 (n/a)</td><td>414.94 (n/a)</td><td>449.40 (n/a)</td><td>246.70 (n/a)</td><td>141.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (+9.65%)</td><td>0.03 (+18.20%)</td><td>0.03 (+17.16%)</td><td>0.02 (+10.45%)</td><td>0.01 (+7.75%)</td><td>478.50 (-9.46%)</td><td>301.84 (-15.46%)</td><td>257.50 (-14.65%)</td><td>231.20 (-8.83%)</td><td>101.17 (-8.67%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.50 (n/a)</td><td>357.02 (n/a)</td><td>301.70 (n/a)</td><td>253.60 (n/a)</td><td>110.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (+6.13%)</td><td>0.02 (+18.34%)</td><td>0.03 <b>(+46.34%)</b></td><td>0.01 <b>(-22.51%)</b></td><td>0.01 <b>(+43.24%)</b></td><td>732.10 <b>(+29.05%)</b></td><td>389.48 (-6.98%)</td><td>290.10 <b>(-31.68%)</b></td><td>246.20 (-5.78%)</td><td>203.94 <b>(+77.08%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.30 (n/a)</td><td>418.72 (n/a)</td><td>424.60 (n/a)</td><td>261.30 (n/a)</td><td>115.17 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (+15.71%)</td><td>0.04 (+4.71%)</td><td>0.04 (-7.80%)</td><td>0.03 (-0.90%)</td><td>0.02 <b>(+44.87%)</b></td><td>557.40 (+0.91%)</td><td>406.66 (+0.28%)</td><td>455.40 (+8.45%)</td><td>247.70 (-13.57%)</td><td>140.11 <b>(+26.69%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>552.40 (n/a)</td><td>405.54 (n/a)</td><td>419.90 (n/a)</td><td>286.60 (n/a)</td><td>110.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (-3.33%)</td><td>0.05 (+4.17%)</td><td>0.04 (+11.07%)</td><td>0.03 (+17.11%)</td><td>0.02 (-17.01%)</td><td>553.30 (-14.61%)</td><td>389.48 (-9.55%)</td><td>429.80 (-9.97%)</td><td>239.70 (+3.41%)</td><td>132.87 <b>(-26.10%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>648.00 (n/a)</td><td>430.60 (n/a)</td><td>477.40 (n/a)</td><td>231.80 (n/a)</td><td>179.80 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (+2.58%)</td><td>0.05 <b>(+28.22%)</b></td><td>0.06 <b>(+41.87%)</b></td><td>0.03 (-8.52%)</td><td>0.02 (+16.57%)</td><td>590.20 (+9.32%)</td><td>331.60 (-19.57%)</td><td>260.90 <b>(-29.52%)</b></td><td>253.40 (-2.54%)</td><td>145.47 <b>(+21.82%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>539.90 (n/a)</td><td>412.28 (n/a)</td><td>370.20 (n/a)</td><td>260.00 (n/a)</td><td>119.41 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (+10.02%)</td><td>0.04 (-7.46%)</td><td>0.04 <b>(-27.59%)</b></td><td>0.03 <b>(-23.88%)</b></td><td>0.02 <b>(+46.74%)</b></td><td>652.30 <b>(+31.35%)</b></td><td>438.46 (+19.09%)</td><td>453.80 <b>(+38.14%)</b></td><td>234.30 (-9.12%)</td><td>189.41 <b>(+66.07%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>496.60 (n/a)</td><td>368.18 (n/a)</td><td>328.50 (n/a)</td><td>257.80 (n/a)</td><td>114.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (+14.16%)</td><td>0.04 (-4.78%)</td><td>0.03 <b>(-33.32%)</b></td><td>0.02 (-2.62%)</td><td>0.02 <b>(+44.15%)</b></td><td>675.10 (+2.69%)</td><td>474.18 (+16.36%)</td><td>576.80 <b>(+49.97%)</b></td><td>212.70 (-12.40%)</td><td>214.72 <b>(+32.52%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>657.40 (n/a)</td><td>407.50 (n/a)</td><td>384.60 (n/a)</td><td>242.80 (n/a)</td><td>162.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (-12.90%)</td><td>0.05 <b>(+26.67%)</b></td><td>0.05 <b>(+65.62%)</b></td><td>0.03 <b>(+29.02%)</b></td><td>0.01 <b>(-37.95%)</b></td><td>525.20 <b>(-22.50%)</b></td><td>368.22 <b>(-26.04%)</b></td><td>318.90 <b>(-39.63%)</b></td><td>300.20 (+14.80%)</td><td>92.65 <b>(-40.88%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>677.70 (n/a)</td><td>497.84 (n/a)</td><td>528.20 (n/a)</td><td>261.50 (n/a)</td><td>156.71 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 <b>(-22.31%)</b></td><td>0.08 (-19.47%)</td><td>0.08 (-15.74%)</td><td>0.05 (-13.58%)</td><td>0.02 (-17.29%)</td><td>612.30 (+15.72%)</td><td>464.08 <b>(+24.72%)</b></td><td>435.70 (+18.69%)</td><td>325.90 <b>(+28.71%)</b></td><td>139.76 <b>(+27.16%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>529.10 (n/a)</td><td>372.10 (n/a)</td><td>367.10 (n/a)</td><td>253.20 (n/a)</td><td>109.91 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 (+0.21%)</td><td>0.10 (+19.92%)</td><td>0.09 <b>(+33.50%)</b></td><td>0.06 (+2.62%)</td><td>0.04 (+8.35%)</td><td>573.90 (-2.55%)</td><td>383.24 (-14.96%)</td><td>367.70 <b>(-25.10%)</b></td><td>231.20 (-0.22%)</td><td>148.65 (+10.33%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>588.90 (n/a)</td><td>450.66 (n/a)</td><td>490.90 (n/a)</td><td>231.70 (n/a)</td><td>134.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (-9.33%)</td><td>0.08 <b>(-22.56%)</b></td><td>0.06 (-13.65%)</td><td>0.05 (-13.16%)</td><td>0.03 <b>(-21.94%)</b></td><td>638.40 (+15.15%)</td><td>485.88 <b>(+25.90%)</b></td><td>521.40 (+15.82%)</td><td>247.60 (+10.29%)</td><td>160.98 (+6.69%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>554.40 (n/a)</td><td>385.92 (n/a)</td><td>450.20 (n/a)</td><td>224.50 (n/a)</td><td>150.88 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 <b>(-35.50%)</b></td><td>0.08 (-10.92%)</td><td>0.08 (+6.36%)</td><td>0.06 <b>(+111.35%)</b></td><td>0.01 <b>(-70.65%)</b></td><td>513.70 <b>(-52.68%)</b></td><td>419.96 (-17.01%)</td><td>402.20 (-5.98%)</td><td>339.40 <b>(+55.05%)</b></td><td>79.71 <b>(-77.37%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1085.60 (n/a)</td><td>506.04 (n/a)</td><td>427.80 (n/a)</td><td>218.90 (n/a)</td><td>352.26 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 <b>(-31.98%)</b></td><td>0.07 (-11.59%)</td><td>0.07 (+0.16%)</td><td>0.06 <b>(+25.80%)</b></td><td>0.01 <b>(-63.15%)</b></td><td>554.70 <b>(-20.52%)</b></td><td>475.00 (+3.50%)</td><td>474.30 (-0.17%)</td><td>372.40 <b>(+47.02%)</b></td><td>71.37 <b>(-55.91%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>697.90 (n/a)</td><td>458.94 (n/a)</td><td>475.10 (n/a)</td><td>253.30 (n/a)</td><td>161.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (-9.50%)</td><td>0.01 (-9.61%)</td><td>0.01 <b>(+24.09%)</b></td><td>0.00 <b>(-73.77%)</b></td><td>0.01 <b>(+38.90%)</b></td><td>1825.90 <b>(+281.27%)</b></td><td>626.88 <b>(+80.24%)</b></td><td>295.10 (-19.42%)</td><td>224.70 (+10.47%)</td><td>683.31 <b>(+482.30%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.90 (n/a)</td><td>347.80 (n/a)</td><td>366.20 (n/a)</td><td>203.40 (n/a)</td><td>117.35 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (-9.47%)</td><td>0.01 (-4.91%)</td><td>0.01 (-5.73%)</td><td>0.01 (+6.52%)</td><td>0.00 (-6.19%)</td><td>630.60 (-6.12%)</td><td>414.46 (+4.52%)</td><td>336.90 (+6.08%)</td><td>244.30 (+10.49%)</td><td>179.56 (-1.12%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>671.70 (n/a)</td><td>396.52 (n/a)</td><td>317.60 (n/a)</td><td>221.10 (n/a)</td><td>181.60 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 <b>(+33.27%)</b></td><td>0.01 <b>(+66.39%)</b></td><td>0.02 <b>(+101.12%)</b></td><td>0.01 <b>(+283.47%)</b></td><td>0.01 (+13.61%)</td><td>531.50 <b>(-73.92%)</b></td><td>357.46 <b>(-54.63%)</b></td><td>272.20 <b>(-50.28%)</b></td><td>204.40 <b>(-24.94%)</b></td><td>151.65 <b>(-78.60%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2038.20 (n/a)</td><td>787.90 (n/a)</td><td>547.50 (n/a)</td><td>272.30 (n/a)</td><td>708.77 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (-16.68%)</td><td>0.01 <b>(-20.69%)</b></td><td>0.01 <b>(-29.04%)</b></td><td>0.00 <b>(-68.60%)</b></td><td>0.01 (+10.77%)</td><td>1886.90 <b>(+218.46%)</b></td><td>690.62 <b>(+76.23%)</b></td><td>446.10 <b>(+40.95%)</b></td><td>283.90 <b>(+20.04%)</b></td><td>678.29 <b>(+309.69%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.50 (n/a)</td><td>391.88 (n/a)</td><td>316.50 (n/a)</td><td>236.50 (n/a)</td><td>165.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 <b>(-39.08%)</b></td><td>0.01 <b>(-25.03%)</b></td><td>0.01 (+7.21%)</td><td>0.01 (-1.09%)</td><td>0.00 <b>(-60.48%)</b></td><td>553.90 (+1.10%)</td><td>441.54 (+15.94%)</td><td>408.30 (-6.74%)</td><td>292.60 <b>(+64.20%)</b></td><td>112.12 <b>(-32.40%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.90 (n/a)</td><td>380.82 (n/a)</td><td>437.80 (n/a)</td><td>178.20 (n/a)</td><td>165.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (-14.30%)</td><td>0.01 (-0.54%)</td><td>0.01 <b>(+49.47%)</b></td><td>0.00 <b>(-75.33%)</b></td><td>0.01 (+14.09%)</td><td>2478.10 <b>(+305.38%)</b></td><td>752.30 <b>(+78.91%)</b></td><td>290.30 <b>(-33.08%)</b></td><td>232.50 (+16.72%)</td><td>970.39 <b>(+469.03%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.30 (n/a)</td><td>420.48 (n/a)</td><td>433.80 (n/a)</td><td>199.20 (n/a)</td><td>170.54 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (-16.81%)</td><td>0.01 <b>(-28.44%)</b></td><td>0.01 <b>(-27.56%)</b></td><td>0.00 <b>(-74.90%)</b></td><td>0.00 (-4.57%)</td><td>2428.90 <b>(+298.44%)</b></td><td>840.96 <b>(+102.37%)</b></td><td>503.60 <b>(+38.05%)</b></td><td>282.70 <b>(+20.20%)</b></td><td>892.61 <b>(+407.87%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.60 (n/a)</td><td>415.56 (n/a)</td><td>364.80 (n/a)</td><td>235.20 (n/a)</td><td>175.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 <b>(+22.88%)</b></td><td>0.01 <b>(+33.24%)</b></td><td>0.01 <b>(+50.00%)</b></td><td>0.01 (-0.02%)</td><td>0.00 <b>(+71.92%)</b></td><td>568.70 (+0.02%)</td><td>367.76 (-19.85%)</td><td>312.30 <b>(-33.34%)</b></td><td>242.90 (-18.63%)</td><td>143.07 <b>(+44.53%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.60 (n/a)</td><td>458.86 (n/a)</td><td>468.50 (n/a)</td><td>298.50 (n/a)</td><td>98.99 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (-14.59%)</td><td>0.01 (-1.51%)</td><td>0.01 <b>(+24.52%)</b></td><td>0.00 <b>(-70.62%)</b></td><td>0.01 (-5.94%)</td><td>2083.00 <b>(+240.42%)</b></td><td>732.44 <b>(+43.71%)</b></td><td>468.80 (-19.68%)</td><td>234.70 (+17.12%)</td><td>763.22 <b>(+339.41%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.90 (n/a)</td><td>509.66 (n/a)</td><td>583.70 (n/a)</td><td>200.40 (n/a)</td><td>173.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (-6.65%)</td><td>0.01 (+8.10%)</td><td>0.01 (-3.43%)</td><td>0.01 <b>(+21.76%)</b></td><td>0.00 <b>(-28.49%)</b></td><td>446.60 (-17.87%)</td><td>301.24 (-13.61%)</td><td>295.30 (+3.54%)</td><td>224.40 (+7.11%)</td><td>87.99 <b>(-38.08%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.80 (n/a)</td><td>348.68 (n/a)</td><td>285.20 (n/a)</td><td>209.50 (n/a)</td><td>142.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (-8.30%)</td><td>0.01 (-18.63%)</td><td>0.01 <b>(-36.36%)</b></td><td>0.01 (-17.03%)</td><td>0.00 (-0.51%)</td><td>620.30 <b>(+20.52%)</b></td><td>466.50 <b>(+26.68%)</b></td><td>539.10 <b>(+57.13%)</b></td><td>262.50 (+9.06%)</td><td>170.85 <b>(+32.39%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.70 (n/a)</td><td>368.24 (n/a)</td><td>343.10 (n/a)</td><td>240.70 (n/a)</td><td>129.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (+1.24%)</td><td>0.01 <b>(+29.18%)</b></td><td>0.01 <b>(+55.76%)</b></td><td>0.01 <b>(+60.85%)</b></td><td>0.00 <b>(-41.88%)</b></td><td>367.90 <b>(-37.82%)</b></td><td>304.58 <b>(-30.71%)</b></td><td>330.10 <b>(-35.80%)</b></td><td>230.00 (-1.20%)</td><td>56.84 <b>(-65.45%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.70 (n/a)</td><td>439.58 (n/a)</td><td>514.20 (n/a)</td><td>232.80 (n/a)</td><td>164.53 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (-16.93%)</td><td>0.02 (-12.70%)</td><td>0.02 <b>(-24.57%)</b></td><td>0.01 (-6.94%)</td><td>0.01 <b>(-30.15%)</b></td><td>569.50 (+7.47%)</td><td>374.20 (+8.46%)</td><td>375.00 <b>(+32.56%)</b></td><td>240.00 <b>(+20.42%)</b></td><td>126.55 (-13.44%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.90 (n/a)</td><td>345.00 (n/a)</td><td>282.90 (n/a)</td><td>199.30 (n/a)</td><td>146.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 <b>(+64.56%)</b></td><td>0.03 <b>(+31.46%)</b></td><td>0.03 (+15.01%)</td><td>0.02 (+12.98%)</td><td>0.01 <b>(+71.79%)</b></td><td>425.80 (-11.49%)</td><td>280.80 <b>(-21.59%)</b></td><td>261.60 (-13.06%)</td><td>164.60 <b>(-39.22%)</b></td><td>96.28 (-8.77%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.10 (n/a)</td><td>358.10 (n/a)</td><td>300.90 (n/a)</td><td>270.80 (n/a)</td><td>105.54 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 <b>(+37.33%)</b></td><td>0.03 <b>(+32.72%)</b></td><td>0.03 (+14.72%)</td><td>0.02 <b>(+28.15%)</b></td><td>0.01 <b>(+28.26%)</b></td><td>490.20 <b>(-21.96%)</b></td><td>295.84 <b>(-25.33%)</b></td><td>277.90 (-12.83%)</td><td>178.40 <b>(-27.15%)</b></td><td>117.41 <b>(-26.02%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.10 (n/a)</td><td>396.18 (n/a)</td><td>318.80 (n/a)</td><td>244.90 (n/a)</td><td>158.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 <b>(+21.58%)</b></td><td>0.02 (+7.75%)</td><td>0.02 (+2.61%)</td><td>0.01 (+2.81%)</td><td>0.01 <b>(+25.28%)</b></td><td>573.90 (-2.73%)</td><td>420.40 (-3.95%)</td><td>516.60 (-2.55%)</td><td>208.70 (-17.74%)</td><td>165.53 (+4.28%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.00 (n/a)</td><td>437.70 (n/a)</td><td>530.10 (n/a)</td><td>253.70 (n/a)</td><td>158.74 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (+11.18%)</td><td>0.03 (+13.22%)</td><td>0.02 <b>(+36.29%)</b></td><td>0.01 (-6.83%)</td><td>0.01 (+2.12%)</td><td>546.90 (+7.32%)</td><td>351.42 (-12.53%)</td><td>355.10 <b>(-26.63%)</b></td><td>203.00 (-10.02%)</td><td>126.73 (-6.30%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>509.60 (n/a)</td><td>401.78 (n/a)</td><td>484.00 (n/a)</td><td>225.60 (n/a)</td><td>135.25 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 <b>(+20.42%)</b></td><td>0.03 (+3.37%)</td><td>0.03 (-3.13%)</td><td>0.01 (-14.53%)</td><td>0.01 <b>(+39.74%)</b></td><td>591.90 (+17.00%)</td><td>364.22 (+1.74%)</td><td>300.60 (+3.23%)</td><td>235.90 (-16.97%)</td><td>143.61 <b>(+43.19%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.90 (n/a)</td><td>357.98 (n/a)</td><td>291.20 (n/a)</td><td>284.10 (n/a)</td><td>100.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 <b>(-38.42%)</b></td><td>0.02 <b>(-35.13%)</b></td><td>0.02 <b>(-47.88%)</b></td><td>0.01 <b>(+87.93%)</b></td><td>0.00 <b>(-65.14%)</b></td><td>586.60 <b>(-46.79%)</b></td><td>471.14 (+12.02%)</td><td>492.30 <b>(+91.86%)</b></td><td>352.80 <b>(+62.43%)</b></td><td>102.96 <b>(-73.04%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1102.40 (n/a)</td><td>420.58 (n/a)</td><td>256.60 (n/a)</td><td>217.20 (n/a)</td><td>381.84 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (+0.01%)</td><td>0.02 (+1.28%)</td><td>0.02 (-17.26%)</td><td>0.02 (-1.82%)</td><td>0.01 <b>(+22.27%)</b></td><td>501.10 (+1.87%)</td><td>381.78 (+2.16%)</td><td>448.50 <b>(+20.86%)</b></td><td>236.30 (-0.04%)</td><td>119.55 <b>(+29.03%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.90 (n/a)</td><td>373.72 (n/a)</td><td>371.10 (n/a)</td><td>236.40 (n/a)</td><td>92.65 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 <b>(+33.82%)</b></td><td>0.02 <b>(+45.46%)</b></td><td>0.02 <b>(+70.31%)</b></td><td>0.01 <b>(+132.39%)</b></td><td>0.01 <b>(+28.42%)</b></td><td>836.10 <b>(-56.97%)</b></td><td>470.52 <b>(-40.90%)</b></td><td>333.90 <b>(-41.29%)</b></td><td>310.00 <b>(-25.27%)</b></td><td>229.88 <b>(-64.37%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1943.10 (n/a)</td><td>796.18 (n/a)</td><td>568.70 (n/a)</td><td>414.80 (n/a)</td><td>645.15 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (+12.23%)</td><td>0.02 (-3.05%)</td><td>0.02 (-12.99%)</td><td>0.02 (+15.07%)</td><td>0.01 (+8.69%)</td><td>496.60 (-13.09%)</td><td>393.40 (+2.91%)</td><td>440.70 (+14.92%)</td><td>243.90 (-10.89%)</td><td>106.91 (-11.98%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.40 (n/a)</td><td>382.26 (n/a)</td><td>383.50 (n/a)</td><td>273.70 (n/a)</td><td>121.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (-7.71%)</td><td>0.02 (-7.86%)</td><td>0.02 (+19.85%)</td><td>0.01 (+9.07%)</td><td>0.01 <b>(-30.99%)</b></td><td>583.40 (-8.31%)</td><td>450.68 (-1.74%)</td><td>481.10 (-16.56%)</td><td>250.90 (+8.33%)</td><td>121.92 <b>(-36.63%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.30 (n/a)</td><td>458.66 (n/a)</td><td>576.60 (n/a)</td><td>231.60 (n/a)</td><td>192.38 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (-14.37%)</td><td>0.02 (-16.46%)</td><td>0.02 <b>(-43.71%)</b></td><td>0.01 (+15.05%)</td><td>0.01 <b>(-27.21%)</b></td><td>683.20 (-13.09%)</td><td>484.20 (+7.70%)</td><td>537.00 <b>(+77.64%)</b></td><td>272.80 (+16.78%)</td><td>177.55 <b>(-29.32%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>786.10 (n/a)</td><td>449.60 (n/a)</td><td>302.30 (n/a)</td><td>233.60 (n/a)</td><td>251.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (+11.49%)</td><td>0.05 (+4.27%)</td><td>0.03 (-14.99%)</td><td>0.03 (-12.09%)</td><td>0.02 <b>(+50.68%)</b></td><td>549.20 (+13.75%)</td><td>412.98 (+4.28%)</td><td>511.20 (+17.63%)</td><td>218.50 (-10.30%)</td><td>157.59 <b>(+58.07%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>482.80 (n/a)</td><td>396.02 (n/a)</td><td>434.60 (n/a)</td><td>243.60 (n/a)</td><td>99.70 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 <b>(-36.64%)</b></td><td>0.04 (-16.75%)</td><td>0.04 (-4.37%)</td><td>0.03 (+0.32%)</td><td>0.00 <b>(-71.94%)</b></td><td>523.50 (-0.30%)</td><td>443.36 (+12.03%)</td><td>442.50 (+4.56%)</td><td>385.30 <b>(+57.78%)</b></td><td>52.04 <b>(-55.37%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>525.10 (n/a)</td><td>395.74 (n/a)</td><td>423.20 (n/a)</td><td>244.20 (n/a)</td><td>116.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (+13.58%)</td><td>0.04 (-0.20%)</td><td>0.04 (-11.29%)</td><td>0.03 (-0.42%)</td><td>0.02 (+6.95%)</td><td>598.40 (+0.42%)</td><td>422.40 (+0.20%)</td><td>432.50 (+12.75%)</td><td>241.10 (-11.98%)</td><td>149.13 (-5.22%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>595.90 (n/a)</td><td>421.54 (n/a)</td><td>383.60 (n/a)</td><td>273.90 (n/a)</td><td>157.35 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (+14.99%)</td><td>0.04 <b>(+29.57%)</b></td><td>0.04 <b>(+30.48%)</b></td><td>0.03 <b>(+201.25%)</b></td><td>0.02 (+5.76%)</td><td>629.90 <b>(-66.80%)</b></td><td>435.18 <b>(-40.45%)</b></td><td>424.80 <b>(-23.35%)</b></td><td>238.60 (-13.01%)</td><td>188.49 <b>(-71.60%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1897.50 (n/a)</td><td>730.72 (n/a)</td><td>554.20 (n/a)</td><td>274.30 (n/a)</td><td>663.65 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (-0.73%)</td><td>0.05 (+12.13%)</td><td>0.06 (+0.57%)</td><td>0.03 <b>(+383.67%)</b></td><td>0.01 <b>(-45.44%)</b></td><td>516.90 <b>(-79.33%)</b></td><td>358.04 <b>(-52.75%)</b></td><td>296.30 (-0.57%)</td><td>273.60 (+0.74%)</td><td>103.89 <b>(-89.36%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2500.20 (n/a)</td><td>757.74 (n/a)</td><td>298.00 (n/a)</td><td>271.60 (n/a)</td><td>976.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (-1.77%)</td><td>0.05 (-10.16%)</td><td>0.05 (+9.07%)</td><td>0.03 <b>(-21.13%)</b></td><td>0.02 (+4.70%)</td><td>617.30 <b>(+26.78%)</b></td><td>383.88 (+15.67%)</td><td>314.80 (-8.33%)</td><td>226.50 (+1.84%)</td><td>155.76 <b>(+44.50%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>486.90 (n/a)</td><td>331.88 (n/a)</td><td>343.40 (n/a)</td><td>222.40 (n/a)</td><td>107.79 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (-12.11%)</td><td>0.04 (-15.62%)</td><td>0.04 <b>(-40.92%)</b></td><td>0.03 <b>(+216.19%)</b></td><td>0.01 <b>(-51.17%)</b></td><td>608.10 <b>(-68.37%)</b></td><td>462.24 <b>(-28.17%)</b></td><td>464.00 <b>(+69.28%)</b></td><td>298.80 (+13.79%)</td><td>130.06 <b>(-81.97%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1922.60 (n/a)</td><td>643.56 (n/a)</td><td>274.10 (n/a)</td><td>262.60 (n/a)</td><td>721.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (-8.02%)</td><td>0.05 (-15.31%)</td><td>0.06 (-15.41%)</td><td>0.03 (-11.87%)</td><td>0.02 (+12.22%)</td><td>568.90 (+13.46%)</td><td>372.62 <b>(+23.94%)</b></td><td>287.70 (+18.25%)</td><td>237.10 (+8.71%)</td><td>161.37 <b>(+37.12%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>501.40 (n/a)</td><td>300.64 (n/a)</td><td>243.30 (n/a)</td><td>218.10 (n/a)</td><td>117.68 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (-12.75%)</td><td>0.05 (+9.12%)</td><td>0.05 (+8.40%)</td><td>0.04 <b>(+33.96%)</b></td><td>0.01 <b>(-30.94%)</b></td><td>451.20 <b>(-25.35%)</b></td><td>338.22 (-16.76%)</td><td>303.90 (-7.74%)</td><td>235.70 (+14.64%)</td><td>101.28 <b>(-43.59%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.40 (n/a)</td><td>406.32 (n/a)</td><td>329.40 (n/a)</td><td>205.60 (n/a)</td><td>179.54 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (+13.35%)</td><td>0.05 (+18.57%)</td><td>0.06 <b>(+50.72%)</b></td><td>0.03 (+9.74%)</td><td>0.02 (+17.87%)</td><td>537.10 (-8.87%)</td><td>362.32 (-14.44%)</td><td>278.30 <b>(-33.64%)</b></td><td>236.20 (-11.77%)</td><td>136.88 (-2.05%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>589.40 (n/a)</td><td>423.48 (n/a)</td><td>419.40 (n/a)</td><td>267.70 (n/a)</td><td>139.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (+5.16%)</td><td>0.04 <b>(-25.10%)</b></td><td>0.03 <b>(-47.55%)</b></td><td>0.02 (-8.88%)</td><td>0.02 (+15.32%)</td><td>706.90 (+9.75%)</td><td>541.64 <b>(+38.95%)</b></td><td>621.70 <b>(+90.65%)</b></td><td>234.40 (-4.91%)</td><td>192.06 (+16.83%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>644.10 (n/a)</td><td>389.80 (n/a)</td><td>326.10 (n/a)</td><td>246.50 (n/a)</td><td>164.40 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (+3.72%)</td><td>0.05 (+5.32%)</td><td>0.05 <b>(+39.30%)</b></td><td>0.02 (-16.31%)</td><td>0.02 <b>(+25.07%)</b></td><td>694.20 (+19.48%)</td><td>425.12 (+3.87%)</td><td>314.30 <b>(-28.21%)</b></td><td>239.60 (-3.58%)</td><td>218.45 <b>(+50.82%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>581.00 (n/a)</td><td>409.28 (n/a)</td><td>437.80 (n/a)</td><td>248.50 (n/a)</td><td>144.84 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 <b>(-20.06%)</b></td><td>0.08 <b>(-28.37%)</b></td><td>0.07 <b>(-48.20%)</b></td><td>0.06 (+16.22%)</td><td>0.02 <b>(-46.71%)</b></td><td>534.30 (-13.96%)</td><td>445.50 <b>(+25.51%)</b></td><td>488.80 <b>(+93.05%)</b></td><td>284.30 <b>(+25.08%)</b></td><td>103.60 <b>(-40.26%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>621.00 (n/a)</td><td>354.94 (n/a)</td><td>253.20 (n/a)</td><td>227.30 (n/a)</td><td>173.41 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (-8.60%)</td><td>0.10 (-15.58%)</td><td>0.10 (-17.48%)</td><td>0.06 <b>(-22.88%)</b></td><td>0.03 (+3.07%)</td><td>561.30 <b>(+29.69%)</b></td><td>351.68 <b>(+21.29%)</b></td><td>314.90 <b>(+21.21%)</b></td><td>264.60 (+9.38%)</td><td>120.32 <b>(+49.10%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>432.80 (n/a)</td><td>289.96 (n/a)</td><td>259.80 (n/a)</td><td>241.90 (n/a)</td><td>80.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 (+5.12%)</td><td>0.10 (-13.65%)</td><td>0.11 (-11.89%)</td><td>0.05 (-16.85%)</td><td>0.04 <b>(+23.38%)</b></td><td>640.60 <b>(+20.28%)</b></td><td>380.12 <b>(+22.23%)</b></td><td>296.40 (+13.48%)</td><td>230.60 (-4.87%)</td><td>171.40 <b>(+37.72%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>532.60 (n/a)</td><td>310.98 (n/a)</td><td>261.20 (n/a)</td><td>242.40 (n/a)</td><td>124.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (-12.56%)</td><td>0.09 <b>(-23.27%)</b></td><td>0.09 <b>(-30.44%)</b></td><td>0.06 <b>(-28.08%)</b></td><td>0.02 <b>(+22.90%)</b></td><td>516.10 <b>(+39.04%)</b></td><td>390.24 <b>(+34.11%)</b></td><td>383.90 <b>(+43.73%)</b></td><td>279.00 (+14.39%)</td><td>96.94 <b>(+92.20%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>371.20 (n/a)</td><td>290.98 (n/a)</td><td>267.10 (n/a)</td><td>243.90 (n/a)</td><td>50.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (-9.60%)</td><td>0.08 (+2.79%)</td><td>0.08 (-0.60%)</td><td>0.05 <b>(+22.83%)</b></td><td>0.03 (-9.60%)</td><td>595.90 (-18.58%)</td><td>424.56 (-5.38%)</td><td>421.70 (+0.60%)</td><td>283.10 (+10.63%)</td><td>136.51 <b>(-22.24%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>731.90 (n/a)</td><td>448.70 (n/a)</td><td>419.20 (n/a)</td><td>255.90 (n/a)</td><td>175.54 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 (-4.51%)</td><td>0.09 (-16.26%)</td><td>0.08 <b>(-25.89%)</b></td><td>0.06 (-6.33%)</td><td>0.03 (-6.44%)</td><td>518.70 (+6.77%)</td><td>417.10 (+18.12%)</td><td>421.90 <b>(+34.92%)</b></td><td>229.70 (+4.74%)</td><td>113.30 (-6.17%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>485.80 (n/a)</td><td>353.12 (n/a)</td><td>312.70 (n/a)</td><td>219.30 (n/a)</td><td>120.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (+13.25%)</td><td>0.09 (+9.21%)</td><td>0.11 <b>(+61.74%)</b></td><td>0.02 <b>(-63.96%)</b></td><td>0.05 <b>(+36.87%)</b></td><td>1819.90 <b>(+177.51%)</b></td><td>628.16 <b>(+34.76%)</b></td><td>303.90 <b>(-38.17%)</b></td><td>242.90 (-11.70%)</td><td>671.60 <b>(+277.50%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>655.80 (n/a)</td><td>466.12 (n/a)</td><td>491.50 (n/a)</td><td>275.10 (n/a)</td><td>177.91 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.18 <b>(+28.12%)</b></td><td>0.10 (-7.26%)</td><td>0.07 <b>(-42.63%)</b></td><td>0.04 <b>(-33.32%)</b></td><td>0.06 <b>(+108.39%)</b></td><td>778.20 <b>(+49.94%)</b></td><td>430.72 <b>(+34.36%)</b></td><td>485.30 <b>(+74.32%)</b></td><td>185.90 <b>(-21.96%)</b></td><td>245.10 <b>(+113.26%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>519.00 (n/a)</td><td>320.58 (n/a)</td><td>278.40 (n/a)</td><td>238.20 (n/a)</td><td>114.93 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 <b>(-21.96%)</b></td><td>0.11 <b>(+34.53%)</b></td><td>0.12 <b>(+84.68%)</b></td><td>0.06 <b>(+52.16%)</b></td><td>0.03 <b>(-46.48%)</b></td><td>524.60 <b>(-34.28%)</b></td><td>325.44 <b>(-35.43%)</b></td><td>278.70 <b>(-45.86%)</b></td><td>253.50 <b>(+28.16%)</b></td><td>112.32 <b>(-47.52%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>798.20 (n/a)</td><td>504.02 (n/a)</td><td>514.80 (n/a)</td><td>197.80 (n/a)</td><td>214.04 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.18 <b>(+43.56%)</b></td><td>0.09 <b>(+30.19%)</b></td><td>0.07 (+1.64%)</td><td>0.06 <b>(+40.57%)</b></td><td>0.05 <b>(+56.31%)</b></td><td>550.50 <b>(-28.87%)</b></td><td>428.04 <b>(-20.26%)</b></td><td>492.10 (-1.62%)</td><td>178.00 <b>(-30.33%)</b></td><td>156.89 (-19.48%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>773.90 (n/a)</td><td>536.78 (n/a)</td><td>500.20 (n/a)</td><td>255.50 (n/a)</td><td>194.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 <b>(+26.13%)</b></td><td>0.08 (+11.54%)</td><td>0.07 (-3.78%)</td><td>0.06 (-6.72%)</td><td>0.03 <b>(+73.23%)</b></td><td>582.30 (+7.22%)</td><td>433.26 (-4.98%)</td><td>488.30 (+3.92%)</td><td>244.80 <b>(-20.73%)</b></td><td>135.56 <b>(+49.42%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>543.10 (n/a)</td><td>455.98 (n/a)</td><td>469.90 (n/a)</td><td>308.80 (n/a)</td><td>90.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 <b>(-21.47%)</b></td><td>0.08 (-1.38%)</td><td>0.10 <b>(+46.80%)</b></td><td>0.02 <b>(-65.36%)</b></td><td>0.04 (+5.37%)</td><td>1867.40 <b>(+188.67%)</b></td><td>638.70 <b>(+44.45%)</b></td><td>342.90 <b>(-31.87%)</b></td><td>303.20 <b>(+27.34%)</b></td><td>687.39 <b>(+321.59%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>646.90 (n/a)</td><td>442.16 (n/a)</td><td>503.30 (n/a)</td><td>238.10 (n/a)</td><td>163.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 <b>(+37.47%)</b></td><td>0.01 (+0.07%)</td><td>0.01 <b>(-26.68%)</b></td><td>0.01 (-19.62%)</td><td>0.00 <b>(+297.73%)</b></td><td>577.40 <b>(+24.41%)</b></td><td>448.78 (+11.29%)</td><td>536.20 <b>(+36.40%)</b></td><td>264.80 <b>(-27.25%)</b></td><td>155.14 <b>(+269.29%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.10 (n/a)</td><td>403.24 (n/a)</td><td>393.10 (n/a)</td><td>364.00 (n/a)</td><td>42.01 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 <b>(-39.19%)</b></td><td>0.01 <b>(-36.23%)</b></td><td>0.01 <b>(-29.65%)</b></td><td>0.01 <b>(-59.60%)</b></td><td>0.00 <b>(-20.36%)</b></td><td>1088.60 <b>(+147.52%)</b></td><td>584.40 <b>(+70.83%)</b></td><td>487.50 <b>(+42.13%)</b></td><td>374.30 <b>(+64.46%)</b></td><td>290.84 <b>(+238.27%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>439.80 (n/a)</td><td>342.10 (n/a)</td><td>343.00 (n/a)</td><td>227.60 (n/a)</td><td>85.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (+3.86%)</td><td>0.01 (+6.59%)</td><td>0.01 (+14.10%)</td><td>0.01 (+6.16%)</td><td>0.00 (-1.27%)</td><td>625.30 (-5.81%)</td><td>487.64 (-7.76%)</td><td>530.60 (-12.36%)</td><td>258.30 (-3.73%)</td><td>137.73 (-14.98%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>663.90 (n/a)</td><td>528.66 (n/a)</td><td>605.40 (n/a)</td><td>268.30 (n/a)</td><td>162.00 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (+6.19%)</td><td>0.01 (-18.61%)</td><td>0.01 <b>(-23.17%)</b></td><td>0.01 <b>(-37.16%)</b></td><td>0.00 <b>(+73.25%)</b></td><td>762.30 <b>(+59.14%)</b></td><td>540.76 <b>(+35.13%)</b></td><td>528.60 <b>(+30.13%)</b></td><td>267.60 (-5.81%)</td><td>184.61 <b>(+155.68%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>479.00 (n/a)</td><td>400.18 (n/a)</td><td>406.20 (n/a)</td><td>284.10 (n/a)</td><td>72.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (+19.16%)</td><td>0.01 (+12.26%)</td><td>0.01 (+13.34%)</td><td>0.01 (+5.65%)</td><td>0.01 <b>(+37.22%)</b></td><td>578.80 (-5.35%)</td><td>383.94 (-5.08%)</td><td>303.60 (-11.77%)</td><td>195.80 (-16.07%)</td><td>176.25 (+17.65%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.50 (n/a)</td><td>404.48 (n/a)</td><td>344.10 (n/a)</td><td>233.30 (n/a)</td><td>149.81 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 <b>(-29.94%)</b></td><td>0.01 <b>(-24.60%)</b></td><td>0.01 <b>(-40.66%)</b></td><td>0.01 (+4.97%)</td><td>0.00 <b>(-54.52%)</b></td><td>530.00 (-4.74%)</td><td>396.04 (+17.23%)</td><td>412.60 <b>(+68.55%)</b></td><td>270.40 <b>(+42.77%)</b></td><td>95.03 <b>(-41.36%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.40 (n/a)</td><td>337.82 (n/a)</td><td>244.80 (n/a)</td><td>189.40 (n/a)</td><td>162.06 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 <b>(+72.06%)</b></td><td>0.01 <b>(+55.16%)</b></td><td>0.01 <b>(+32.57%)</b></td><td>0.01 <b>(+236.68%)</b></td><td>0.00 <b>(+40.81%)</b></td><td>550.90 <b>(-70.30%)</b></td><td>424.38 <b>(-46.40%)</b></td><td>445.20 <b>(-24.57%)</b></td><td>231.30 <b>(-41.87%)</b></td><td>130.70 <b>(-78.25%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1854.70 (n/a)</td><td>791.76 (n/a)</td><td>590.20 (n/a)</td><td>397.90 (n/a)</td><td>600.95 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.02 (+1.44%)</td><td>0.01 (+1.41%)</td><td>0.01 (-14.00%)</td><td>0.01 <b>(+183.13%)</b></td><td>0.00 <b>(-30.44%)</b></td><td>633.80 <b>(-64.68%)</b></td><td>475.98 <b>(-29.40%)</b></td><td>541.50 (+16.28%)</td><td>289.70 (-1.43%)</td><td>143.16 <b>(-77.38%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1794.40 (n/a)</td><td>674.16 (n/a)</td><td>465.70 (n/a)</td><td>293.90 (n/a)</td><td>632.83 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 <b>(-22.26%)</b></td><td>0.01 <b>(-20.46%)</b></td><td>0.01 (-15.65%)</td><td>0.01 (-0.44%)</td><td>0.00 <b>(-46.62%)</b></td><td>524.70 (+0.44%)</td><td>455.58 (+17.23%)</td><td>482.60 (+18.57%)</td><td>302.60 <b>(+28.60%)</b></td><td>90.42 <b>(-33.57%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.40 (n/a)</td><td>388.62 (n/a)</td><td>407.00 (n/a)</td><td>235.30 (n/a)</td><td>136.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (-18.75%)</td><td>0.01 (-3.30%)</td><td>0.01 (-11.84%)</td><td>0.01 <b>(+73.39%)</b></td><td>0.00 <b>(-58.42%)</b></td><td>579.20 <b>(-42.33%)</b></td><td>516.36 (-7.69%)</td><td>547.10 (+13.44%)</td><td>407.50 <b>(+23.07%)</b></td><td>70.21 <b>(-72.80%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1004.30 (n/a)</td><td>559.40 (n/a)</td><td>482.30 (n/a)</td><td>331.10 (n/a)</td><td>258.14 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.01 (-19.04%)</td><td>0.01 <b>(-25.84%)</b></td><td>0.01 <b>(-20.53%)</b></td><td>0.01 (-19.82%)</td><td>0.00 <b>(-32.47%)</b></td><td>784.90 <b>(+24.71%)</b></td><td>587.86 <b>(+31.37%)</b></td><td>597.50 <b>(+25.82%)</b></td><td>365.20 <b>(+23.50%)</b></td><td>151.65 (+5.13%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>629.40 (n/a)</td><td>447.48 (n/a)</td><td>474.90 (n/a)</td><td>295.70 (n/a)</td><td>144.25 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 <b>(+27.31%)</b></td><td>0.02 <b>(+25.47%)</b></td><td>0.03 <b>(+41.93%)</b></td><td>0.01 <b>(+36.85%)</b></td><td>0.01 <b>(+42.77%)</b></td><td>591.20 <b>(-26.93%)</b></td><td>401.20 (-18.15%)</td><td>298.80 <b>(-29.53%)</b></td><td>244.10 <b>(-21.46%)</b></td><td>168.51 (-14.07%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>809.10 (n/a)</td><td>490.14 (n/a)</td><td>424.00 (n/a)</td><td>310.80 (n/a)</td><td>196.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 (-2.18%)</td><td>0.03 <b>(-35.46%)</b></td><td>0.02 <b>(-52.04%)</b></td><td>0.01 <b>(-43.08%)</b></td><td>0.01 (+18.54%)</td><td>1097.60 <b>(+75.70%)</b></td><td>599.86 <b>(+75.53%)</b></td><td>559.90 <b>(+108.53%)</b></td><td>266.10 (+2.23%)</td><td>326.13 <b>(+105.51%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>624.70 (n/a)</td><td>341.74 (n/a)</td><td>268.50 (n/a)</td><td>260.30 (n/a)</td><td>158.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (-0.19%)</td><td>0.02 (-9.71%)</td><td>0.02 (+0.04%)</td><td>0.01 (+4.64%)</td><td>0.01 (-1.43%)</td><td>615.90 (-4.44%)</td><td>451.68 (+9.64%)</td><td>446.90 (-0.04%)</td><td>223.60 (+0.22%)</td><td>150.44 (-7.58%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>644.50 (n/a)</td><td>411.96 (n/a)</td><td>447.10 (n/a)</td><td>223.10 (n/a)</td><td>162.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 <b>(+37.13%)</b></td><td>0.03 (-4.51%)</td><td>0.03 <b>(-27.45%)</b></td><td>0.02 <b>(-36.97%)</b></td><td>0.02 <b>(+400.80%)</b></td><td>538.50 <b>(+58.66%)</b></td><td>370.44 <b>(+25.99%)</b></td><td>408.10 <b>(+37.83%)</b></td><td>191.10 <b>(-27.09%)</b></td><td>164.26 <b>(+461.62%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>339.40 (n/a)</td><td>294.02 (n/a)</td><td>296.10 (n/a)</td><td>262.10 (n/a)</td><td>29.25 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (+14.59%)</td><td>0.03 <b>(+57.70%)</b></td><td>0.03 <b>(+99.32%)</b></td><td>0.01 <b>(+72.75%)</b></td><td>0.01 (-3.13%)</td><td>603.00 <b>(-42.11%)</b></td><td>342.34 <b>(-41.16%)</b></td><td>281.60 <b>(-49.82%)</b></td><td>248.80 (-12.73%)</td><td>146.79 <b>(-48.11%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1041.70 (n/a)</td><td>581.84 (n/a)</td><td>561.20 (n/a)</td><td>285.10 (n/a)</td><td>282.89 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 (-7.63%)</td><td>0.02 (-18.08%)</td><td>0.02 <b>(-26.28%)</b></td><td>0.01 (-18.90%)</td><td>0.01 (-13.97%)</td><td>808.30 <b>(+23.29%)</b></td><td>507.64 <b>(+20.65%)</b></td><td>489.50 <b>(+35.67%)</b></td><td>271.10 (+8.27%)</td><td>193.01 (+11.28%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>655.60 (n/a)</td><td>420.76 (n/a)</td><td>360.80 (n/a)</td><td>250.40 (n/a)</td><td>173.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (-8.57%)</td><td>0.02 (+5.64%)</td><td>0.02 (-4.51%)</td><td>0.01 <b>(+140.67%)</b></td><td>0.01 <b>(-20.07%)</b></td><td>783.00 <b>(-58.45%)</b></td><td>504.10 <b>(-29.41%)</b></td><td>511.30 (+4.71%)</td><td>267.10 (+9.38%)</td><td>210.15 <b>(-68.34%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1884.40 (n/a)</td><td>714.08 (n/a)</td><td>488.30 (n/a)</td><td>244.20 (n/a)</td><td>663.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (-0.01%)</td><td>0.02 (-3.68%)</td><td>0.02 (-11.00%)</td><td>0.01 (-1.34%)</td><td>0.01 (+12.65%)</td><td>659.50 (+1.37%)</td><td>445.76 (+6.44%)</td><td>419.20 (+12.36%)</td><td>281.30 (+0.04%)</td><td>172.44 (+11.88%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.60 (n/a)</td><td>418.78 (n/a)</td><td>373.10 (n/a)</td><td>281.20 (n/a)</td><td>154.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (-15.91%)</td><td>0.02 <b>(-31.50%)</b></td><td>0.02 <b>(-32.01%)</b></td><td>0.00 <b>(-73.61%)</b></td><td>0.01 (-2.80%)</td><td>1970.40 <b>(+278.85%)</b></td><td>725.56 <b>(+102.03%)</b></td><td>443.50 <b>(+47.10%)</b></td><td>263.80 (+18.94%)</td><td>704.18 <b>(+373.82%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.10 (n/a)</td><td>359.14 (n/a)</td><td>301.50 (n/a)</td><td>221.80 (n/a)</td><td>148.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 <b>(+22.35%)</b></td><td>0.03 (-16.21%)</td><td>0.02 <b>(-37.63%)</b></td><td>0.01 <b>(-48.37%)</b></td><td>0.01 <b>(+323.03%)</b></td><td>655.40 <b>(+93.68%)</b></td><td>427.70 <b>(+41.90%)</b></td><td>460.70 <b>(+60.36%)</b></td><td>226.00 (-18.29%)</td><td>188.29 <b>(+536.49%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>338.40 (n/a)</td><td>301.40 (n/a)</td><td>287.30 (n/a)</td><td>276.60 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.03 (-12.29%)</td><td>0.02 (-16.94%)</td><td>0.02 (-8.23%)</td><td>0.01 <b>(-21.21%)</b></td><td>0.01 (-15.25%)</td><td>800.80 <b>(+26.93%)</b></td><td>520.90 <b>(+20.10%)</b></td><td>482.90 (+8.96%)</td><td>274.30 (+14.01%)</td><td>193.03 (+19.99%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.90 (n/a)</td><td>433.72 (n/a)</td><td>443.20 (n/a)</td><td>240.60 (n/a)</td><td>160.88 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 <b>(+39.00%)</b></td><td>0.05 <b>(+56.32%)</b></td><td>0.06 <b>(+107.55%)</b></td><td>0.03 (+15.46%)</td><td>0.02 <b>(+90.73%)</b></td><td>570.20 (-13.38%)</td><td>355.80 <b>(-31.24%)</b></td><td>258.60 <b>(-51.83%)</b></td><td>236.20 <b>(-28.05%)</b></td><td>154.32 (+15.92%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>658.30 (n/a)</td><td>517.44 (n/a)</td><td>536.80 (n/a)</td><td>328.30 (n/a)</td><td>133.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (+0.01%)</td><td>0.07 (-8.26%)</td><td>0.08 (-3.87%)</td><td>0.05 (-4.86%)</td><td>0.02 (+14.02%)</td><td>509.70 (+5.09%)</td><td>374.16 (+11.48%)</td><td>326.80 (+4.01%)</td><td>256.40 (-0.04%)</td><td>116.18 <b>(+25.50%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>485.00 (n/a)</td><td>335.64 (n/a)</td><td>314.20 (n/a)</td><td>256.50 (n/a)</td><td>92.57 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (-2.84%)</td><td>0.05 (-9.34%)</td><td>0.04 <b>(-21.92%)</b></td><td>0.03 (+2.74%)</td><td>0.01 (+16.09%)</td><td>497.70 (-2.66%)</td><td>375.00 (+12.03%)</td><td>387.50 <b>(+28.10%)</b></td><td>253.90 (+2.92%)</td><td>110.82 (+7.98%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>511.30 (n/a)</td><td>334.74 (n/a)</td><td>302.50 (n/a)</td><td>246.70 (n/a)</td><td>102.63 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 (+11.54%)</td><td>0.06 (-10.85%)</td><td>0.04 <b>(-22.69%)</b></td><td>0.04 (-14.34%)</td><td>0.02 <b>(+31.88%)</b></td><td>541.20 (+16.74%)</td><td>410.72 (+18.02%)</td><td>457.40 <b>(+29.36%)</b></td><td>219.60 (-10.33%)</td><td>136.18 <b>(+42.54%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>463.60 (n/a)</td><td>348.02 (n/a)</td><td>353.60 (n/a)</td><td>244.90 (n/a)</td><td>95.54 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (+3.43%)</td><td>0.05 (-5.37%)</td><td>0.06 (+11.32%)</td><td>0.03 <b>(-24.35%)</b></td><td>0.02 <b>(+66.69%)</b></td><td>573.20 <b>(+32.20%)</b></td><td>367.90 (+15.00%)</td><td>280.30 (-10.16%)</td><td>236.70 (-3.31%)</td><td>149.01 <b>(+111.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>433.60 (n/a)</td><td>319.90 (n/a)</td><td>312.00 (n/a)</td><td>244.80 (n/a)</td><td>70.57 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 <b>(-54.14%)</b></td><td>0.03 <b>(-39.49%)</b></td><td>0.04 <b>(-36.04%)</b></td><td>0.02 <b>(-41.07%)</b></td><td>0.01 <b>(-63.18%)</b></td><td>1030.50 <b>(+69.69%)</b></td><td>654.76 <b>(+55.68%)</b></td><td>558.60 <b>(+56.34%)</b></td><td>531.20 <b>(+118.06%)</b></td><td>212.37 <b>(+31.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>607.30 (n/a)</td><td>420.58 (n/a)</td><td>357.30 (n/a)</td><td>243.60 (n/a)</td><td>161.93 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (-4.19%)</td><td>0.06 <b>(+39.08%)</b></td><td>0.06 <b>(+65.25%)</b></td><td>0.03 <b>(+39.61%)</b></td><td>0.01 <b>(-22.44%)</b></td><td>496.20 <b>(-28.37%)</b></td><td>304.36 <b>(-32.43%)</b></td><td>270.90 <b>(-39.49%)</b></td><td>235.20 (+4.39%)</td><td>108.42 <b>(-36.50%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>692.70 (n/a)</td><td>450.46 (n/a)</td><td>447.70 (n/a)</td><td>225.30 (n/a)</td><td>170.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 <b>(-59.19%)</b></td><td>0.04 <b>(-46.42%)</b></td><td>0.04 <b>(-42.86%)</b></td><td>0.03 <b>(-23.01%)</b></td><td>0.01 <b>(-78.11%)</b></td><td>616.90 <b>(+29.87%)</b></td><td>509.92 <b>(+70.43%)</b></td><td>513.10 <b>(+75.00%)</b></td><td>424.60 <b>(+145.01%)</b></td><td>77.27 <b>(-31.26%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>475.00 (n/a)</td><td>299.20 (n/a)</td><td>293.20 (n/a)</td><td>173.30 (n/a)</td><td>112.41 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (+2.35%)</td><td>0.06 (+16.65%)</td><td>0.06 <b>(+25.65%)</b></td><td>0.04 (+4.87%)</td><td>0.01 (-10.08%)</td><td>435.70 (-4.64%)</td><td>290.84 (-15.72%)</td><td>258.00 <b>(-20.39%)</b></td><td>234.80 (-2.33%)</td><td>83.69 (-16.91%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>456.90 (n/a)</td><td>345.10 (n/a)</td><td>324.10 (n/a)</td><td>240.40 (n/a)</td><td>100.72 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 <b>(+65.66%)</b></td><td>0.04 (+5.55%)</td><td>0.04 (-17.28%)</td><td>0.03 (-10.42%)</td><td>0.02 <b>(+261.21%)</b></td><td>583.40 (+11.63%)</td><td>470.16 (+4.17%)</td><td>505.70 <b>(+20.89%)</b></td><td>235.20 <b>(-39.65%)</b></td><td>137.67 <b>(+125.62%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>522.60 (n/a)</td><td>451.36 (n/a)</td><td>418.30 (n/a)</td><td>389.70 (n/a)</td><td>61.02 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (+0.75%)</td><td>0.04 (+1.67%)</td><td>0.04 (+1.06%)</td><td>0.03 (+15.09%)</td><td>0.01 <b>(-28.13%)</b></td><td>489.50 (-13.12%)</td><td>403.98 (-5.82%)</td><td>441.40 (-1.05%)</td><td>288.60 (-0.72%)</td><td>81.47 <b>(-37.44%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>563.40 (n/a)</td><td>428.96 (n/a)</td><td>446.10 (n/a)</td><td>290.70 (n/a)</td><td>130.22 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 <b>(+59.94%)</b></td><td>0.10 <b>(+63.90%)</b></td><td>0.11 <b>(+57.94%)</b></td><td>0.06 <b>(+63.68%)</b></td><td>0.02 <b>(+47.77%)</b></td><td>507.50 <b>(-38.91%)</b></td><td>344.96 <b>(-39.40%)</b></td><td>310.60 <b>(-36.68%)</b></td><td>281.10 <b>(-37.46%)</b></td><td>93.03 <b>(-41.63%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>830.70 (n/a)</td><td>569.28 (n/a)</td><td>490.50 (n/a)</td><td>449.50 (n/a)</td><td>159.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 <b>(+24.12%)</b></td><td>0.08 <b>(+38.46%)</b></td><td>0.06 (-9.72%)</td><td>0.05 <b>(+249.64%)</b></td><td>0.04 (+12.85%)</td><td>716.20 <b>(-71.40%)</b></td><td>489.54 <b>(-47.28%)</b></td><td>574.90 (+10.77%)</td><td>259.10 (-19.41%)</td><td>202.28 <b>(-77.47%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2504.10 (n/a)</td><td>928.64 (n/a)</td><td>519.00 (n/a)</td><td>321.50 (n/a)</td><td>897.91 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 <b>(+30.33%)</b></td><td>0.08 (-6.40%)</td><td>0.07 (-15.98%)</td><td>0.05 <b>(-28.10%)</b></td><td>0.03 <b>(+134.04%)</b></td><td>790.40 <b>(+39.08%)</b></td><td>548.44 (+15.78%)</td><td>562.20 (+19.01%)</td><td>298.70 <b>(-23.27%)</b></td><td>176.13 <b>(+137.38%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>568.30 (n/a)</td><td>473.70 (n/a)</td><td>472.40 (n/a)</td><td>389.30 (n/a)</td><td>74.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 <b>(+43.44%)</b></td><td>0.10 <b>(+30.75%)</b></td><td>0.10 <b>(+43.14%)</b></td><td>0.04 <b>(-25.42%)</b></td><td>0.04 <b>(+118.58%)</b></td><td>818.40 <b>(+34.08%)</b></td><td>405.80 (-11.33%)</td><td>324.70 <b>(-30.14%)</b></td><td>221.80 <b>(-30.27%)</b></td><td>236.99 <b>(+126.46%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>610.40 (n/a)</td><td>457.64 (n/a)</td><td>464.80 (n/a)</td><td>318.10 (n/a)</td><td>104.65 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (-6.36%)</td><td>0.08 (-1.54%)</td><td>0.08 <b>(+32.71%)</b></td><td>0.02 <b>(-43.01%)</b></td><td>0.03 (-10.68%)</td><td>1886.90 <b>(+75.48%)</b></td><td>750.08 (+16.37%)</td><td>500.40 <b>(-24.64%)</b></td><td>358.30 (+6.76%)</td><td>640.27 <b>(+104.89%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>1075.30 (n/a)</td><td>644.58 (n/a)</td><td>664.00 (n/a)</td><td>335.60 (n/a)</td><td>312.49 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (-16.73%)</td><td>0.08 <b>(-23.99%)</b></td><td>0.07 <b>(-38.06%)</b></td><td>0.05 (-12.00%)</td><td>0.02 <b>(-26.44%)</b></td><td>598.90 (+13.64%)</td><td>452.94 <b>(+28.14%)</b></td><td>459.40 <b>(+61.48%)</b></td><td>284.40 <b>(+20.10%)</b></td><td>123.62 (-2.26%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>527.00 (n/a)</td><td>353.48 (n/a)</td><td>284.50 (n/a)</td><td>236.80 (n/a)</td><td>126.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 <b>(-50.90%)</b></td><td>0.06 (-19.53%)</td><td>0.06 (-6.84%)</td><td>0.05 <b>(+253.62%)</b></td><td>0.01 <b>(-81.75%)</b></td><td>704.20 <b>(-71.72%)</b></td><td>590.86 <b>(-30.63%)</b></td><td>593.90 (+7.34%)</td><td>466.70 <b>(+103.71%)</b></td><td>84.36 <b>(-90.89%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2490.10 (n/a)</td><td>851.72 (n/a)</td><td>553.30 (n/a)</td><td>229.10 (n/a)</td><td>925.54 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.16 <b>(+32.88%)</b></td><td>0.09 (+6.66%)</td><td>0.07 (+0.03%)</td><td>0.02 <b>(-65.12%)</b></td><td>0.06 <b>(+87.86%)</b></td><td>1954.00 <b>(+186.68%)</b></td><td>692.72 <b>(+51.17%)</b></td><td>456.10 (-0.04%)</td><td>201.90 <b>(-24.75%)</b></td><td>720.05 <b>(+335.55%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>681.60 (n/a)</td><td>458.24 (n/a)</td><td>456.30 (n/a)</td><td>268.30 (n/a)</td><td>165.32 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (+2.22%)</td><td>0.08 (-14.95%)</td><td>0.07 <b>(-24.10%)</b></td><td>0.05 <b>(-23.30%)</b></td><td>0.03 (+0.91%)</td><td>788.30 <b>(+30.36%)</b></td><td>521.92 (+19.08%)</td><td>534.10 <b>(+31.75%)</b></td><td>274.00 (-2.18%)</td><td>183.70 (+18.40%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>604.70 (n/a)</td><td>438.30 (n/a)</td><td>405.40 (n/a)</td><td>280.10 (n/a)</td><td>155.16 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.18 <b>(+73.14%)</b></td><td>0.10 (+15.47%)</td><td>0.07 <b>(-21.15%)</b></td><td>0.07 (-2.07%)</td><td>0.05 <b>(+239.19%)</b></td><td>499.00 (+2.11%)</td><td>392.92 (-2.34%)</td><td>475.10 <b>(+26.83%)</b></td><td>184.90 <b>(-42.24%)</b></td><td>135.89 <b>(+100.02%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>488.70 (n/a)</td><td>402.34 (n/a)</td><td>374.60 (n/a)</td><td>320.10 (n/a)</td><td>67.94 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (+6.85%)</td><td>0.05 (-6.19%)</td><td>0.05 (+7.30%)</td><td>0.03 (-8.66%)</td><td>0.02 (-5.18%)</td><td>712.70 (+9.48%)</td><td>461.96 (+5.95%)</td><td>444.00 (-6.80%)</td><td>249.10 (-6.39%)</td><td>173.43 (+4.22%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>651.00 (n/a)</td><td>436.02 (n/a)</td><td>476.40 (n/a)</td><td>266.10 (n/a)</td><td>166.41 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (-12.79%)</td><td>0.05 (-17.30%)</td><td>0.05 (+8.49%)</td><td>0.01 <b>(-70.66%)</b></td><td>0.02 (+10.57%)</td><td>1938.90 <b>(+240.88%)</b></td><td>711.36 <b>(+71.01%)</b></td><td>439.10 (-7.83%)</td><td>264.10 (+14.68%)</td><td>694.16 <b>(+389.95%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>568.80 (n/a)</td><td>415.98 (n/a)</td><td>476.40 (n/a)</td><td>230.30 (n/a)</td><td>141.68 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 <b>(+44.64%)</b></td><td>0.06 <b>(+20.26%)</b></td><td>0.05 <b>(+27.05%)</b></td><td>0.04 <b>(+83.92%)</b></td><td>0.03 <b>(+21.25%)</b></td><td>579.60 <b>(-45.63%)</b></td><td>420.90 <b>(-24.75%)</b></td><td>440.90 <b>(-21.30%)</b></td><td>190.20 <b>(-30.86%)</b></td><td>142.19 <b>(-55.56%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1066.00 (n/a)</td><td>559.34 (n/a)</td><td>560.20 (n/a)</td><td>275.10 (n/a)</td><td>319.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (-3.87%)</td><td>0.05 <b>(-28.22%)</b></td><td>0.04 <b>(-40.35%)</b></td><td>0.03 <b>(-24.00%)</b></td><td>0.02 <b>(+29.66%)</b></td><td>603.30 <b>(+31.58%)</b></td><td>499.94 <b>(+47.04%)</b></td><td>565.60 <b>(+67.68%)</b></td><td>260.30 (+4.04%)</td><td>141.81 <b>(+73.74%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>458.50 (n/a)</td><td>340.00 (n/a)</td><td>337.30 (n/a)</td><td>250.20 (n/a)</td><td>81.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 <b>(-47.57%)</b></td><td>0.04 <b>(-34.04%)</b></td><td>0.03 (-10.84%)</td><td>0.01 <b>(-50.01%)</b></td><td>0.01 <b>(-53.13%)</b></td><td>1392.00 <b>(+100.06%)</b></td><td>696.26 <b>(+46.77%)</b></td><td>601.60 (+12.16%)</td><td>384.80 <b>(+90.68%)</b></td><td>402.76 <b>(+85.84%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>695.80 (n/a)</td><td>474.38 (n/a)</td><td>536.40 (n/a)</td><td>201.80 (n/a)</td><td>216.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 <b>(-34.39%)</b></td><td>0.05 (-14.11%)</td><td>0.05 (+14.52%)</td><td>0.03 (+0.48%)</td><td>0.01 <b>(-58.88%)</b></td><td>648.60 (-0.48%)</td><td>463.48 (+1.82%)</td><td>450.20 (-12.68%)</td><td>358.40 <b>(+52.38%)</b></td><td>120.24 <b>(-38.60%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>651.70 (n/a)</td><td>455.20 (n/a)</td><td>515.60 (n/a)</td><td>235.20 (n/a)</td><td>195.83 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 (+0.97%)</td><td>0.06 <b>(-21.99%)</b></td><td>0.05 <b>(-38.30%)</b></td><td>0.04 (-14.21%)</td><td>0.03 <b>(+29.43%)</b></td><td>592.50 (+16.57%)</td><td>434.52 <b>(+34.78%)</b></td><td>477.70 <b>(+62.10%)</b></td><td>241.30 (-0.94%)</td><td>149.71 <b>(+41.18%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>508.30 (n/a)</td><td>322.40 (n/a)</td><td>294.70 (n/a)</td><td>243.60 (n/a)</td><td>106.04 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (+9.92%)</td><td>0.08 (+8.33%)</td><td>0.07 (+8.30%)</td><td>0.05 (+13.21%)</td><td>0.02 (+0.09%)</td><td>454.40 (-11.66%)</td><td>343.38 (-9.40%)</td><td>332.90 (-7.66%)</td><td>217.50 (-9.03%)</td><td>97.96 <b>(-21.09%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>514.40 (n/a)</td><td>379.02 (n/a)</td><td>360.50 (n/a)</td><td>239.10 (n/a)</td><td>124.15 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 <b>(-22.68%)</b></td><td>0.06 (+3.16%)</td><td>0.06 (+10.70%)</td><td>0.04 <b>(+81.45%)</b></td><td>0.01 <b>(-54.52%)</b></td><td>562.90 <b>(-44.89%)</b></td><td>415.94 <b>(-20.82%)</b></td><td>428.40 (-9.66%)</td><td>321.10 <b>(+29.32%)</b></td><td>98.22 <b>(-68.09%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1021.40 (n/a)</td><td>525.32 (n/a)</td><td>474.20 (n/a)</td><td>248.30 (n/a)</td><td>307.84 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 <b>(-29.77%)</b></td><td>0.06 (-16.38%)</td><td>0.05 (-11.27%)</td><td>0.04 (+2.10%)</td><td>0.02 <b>(-45.05%)</b></td><td>585.30 (-2.06%)</td><td>471.02 (+10.36%)</td><td>480.10 (+12.70%)</td><td>278.90 <b>(+42.37%)</b></td><td>118.99 <b>(-22.06%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>597.60 (n/a)</td><td>426.82 (n/a)</td><td>426.00 (n/a)</td><td>195.90 (n/a)</td><td>152.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (-17.96%)</td><td>0.06 <b>(-20.00%)</b></td><td>0.07 (-9.94%)</td><td>0.04 (-14.97%)</td><td>0.02 (-7.15%)</td><td>589.60 (+17.59%)</td><td>410.30 <b>(+26.55%)</b></td><td>329.50 (+11.05%)</td><td>292.70 <b>(+21.91%)</b></td><td>131.39 <b>(+27.75%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>501.40 (n/a)</td><td>324.22 (n/a)</td><td>296.70 (n/a)</td><td>240.10 (n/a)</td><td>102.85 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 <b>(+24.88%)</b></td><td>0.06 (-16.01%)</td><td>0.05 <b>(-47.18%)</b></td><td>0.04 (+2.85%)</td><td>0.04 <b>(+35.58%)</b></td><td>605.80 (-2.76%)</td><td>468.50 <b>(+24.74%)</b></td><td>528.60 <b>(+89.33%)</b></td><td>195.90 (-19.91%)</td><td>169.62 (+4.14%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>623.00 (n/a)</td><td>375.58 (n/a)</td><td>279.20 (n/a)</td><td>244.60 (n/a)</td><td>162.88 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.06 (-14.98%)</td><td>0.04 (+2.01%)</td><td>0.05 <b>(+23.57%)</b></td><td>0.03 (-2.43%)</td><td>0.01 (-16.54%)</td><td>569.50 (+2.48%)</td><td>437.84 (-2.70%)</td><td>407.90 (-19.07%)</td><td>315.70 (+17.62%)</td><td>121.97 (+5.68%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>555.70 (n/a)</td><td>450.00 (n/a)</td><td>504.00 (n/a)</td><td>268.40 (n/a)</td><td>115.41 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.08 (+14.21%)</td><td>0.06 (-5.63%)</td><td>0.06 (-7.57%)</td><td>0.03 <b>(-28.95%)</b></td><td>0.02 <b>(+65.85%)</b></td><td>612.60 <b>(+40.73%)</b></td><td>354.36 (+14.24%)</td><td>314.40 (+8.19%)</td><td>225.50 (-12.46%)</td><td>149.78 <b>(+110.20%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>435.30 (n/a)</td><td>310.18 (n/a)</td><td>290.60 (n/a)</td><td>257.60 (n/a)</td><td>71.26 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (-4.83%)</td><td>0.05 (+9.00%)</td><td>0.05 <b>(+29.30%)</b></td><td>0.04 (+18.22%)</td><td>0.01 <b>(-27.62%)</b></td><td>497.80 (-15.41%)</td><td>365.76 (-14.17%)</td><td>384.60 <b>(-22.66%)</b></td><td>259.50 (+5.06%)</td><td>98.86 <b>(-36.27%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.50 (n/a)</td><td>426.14 (n/a)</td><td>497.30 (n/a)</td><td>247.00 (n/a)</td><td>155.14 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.05 <b>(-27.44%)</b></td><td>0.04 (-11.42%)</td><td>0.05 (+16.50%)</td><td>0.03 (-5.02%)</td><td>0.01 <b>(-48.98%)</b></td><td>618.20 (+5.30%)</td><td>441.50 (+6.46%)</td><td>391.40 (-14.17%)</td><td>344.80 <b>(+37.81%)</b></td><td>108.00 <b>(-22.03%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>587.10 (n/a)</td><td>414.72 (n/a)</td><td>456.00 (n/a)</td><td>250.20 (n/a)</td><td>138.52 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (-8.77%)</td><td>0.05 (-2.06%)</td><td>0.04 (-5.69%)</td><td>0.03 (-17.94%)</td><td>0.02 (+16.29%)</td><td>585.00 <b>(+21.88%)</b></td><td>444.60 (+7.28%)</td><td>495.60 (+6.03%)</td><td>271.70 (+9.64%)</td><td>153.81 <b>(+57.83%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>480.00 (n/a)</td><td>414.44 (n/a)</td><td>467.40 (n/a)</td><td>247.80 (n/a)</td><td>97.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.04 <b>(-47.48%)</b></td><td>0.04 <b>(-23.76%)</b></td><td>0.04 (-16.88%)</td><td>0.03 (+10.22%)</td><td>0.00 <b>(-81.34%)</b></td><td>583.50 (-9.27%)</td><td>512.10 (+19.31%)</td><td>515.30 <b>(+20.31%)</b></td><td>450.30 <b>(+90.40%)</b></td><td>48.68 <b>(-66.37%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>643.10 (n/a)</td><td>429.22 (n/a)</td><td>428.30 (n/a)</td><td>236.50 (n/a)</td><td>144.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.39 (+18.10%)</td><td>0.29 (+0.70%)</td><td>0.34 (+7.24%)</td><td>0.18 (-13.32%)</td><td>0.10 <b>(+81.77%)</b></td><td>538.40 (+15.36%)</td><td>379.38 (+7.21%)</td><td>292.80 (-6.75%)</td><td>250.90 (-15.32%)</td><td>144.24 <b>(+92.71%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>466.70 (n/a)</td><td>353.86 (n/a)</td><td>314.00 (n/a)</td><td>296.30 (n/a)</td><td>74.85 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.33 (-15.50%)</td><td>0.22 <b>(-24.29%)</b></td><td>0.19 <b>(-41.91%)</b></td><td>0.16 <b>(+62.82%)</b></td><td>0.07 <b>(-44.97%)</b></td><td>622.30 <b>(-38.58%)</b></td><td>471.90 (+7.52%)</td><td>507.50 <b>(+72.15%)</b></td><td>297.10 (+18.37%)</td><td>120.88 <b>(-62.80%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>1013.20 (n/a)</td><td>438.90 (n/a)</td><td>294.80 (n/a)</td><td>251.00 (n/a)</td><td>324.97 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.37 (-9.49%)</td><td>0.28 (+8.04%)</td><td>0.28 <b>(+54.65%)</b></td><td>0.18 (+8.35%)</td><td>0.09 <b>(-22.26%)</b></td><td>556.70 (-7.71%)</td><td>387.92 (-12.00%)</td><td>345.00 <b>(-35.34%)</b></td><td>266.80 (+10.48%)</td><td>129.22 <b>(-20.94%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.41 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>603.20 (n/a)</td><td>440.80 (n/a)</td><td>533.60 (n/a)</td><td>241.50 (n/a)</td><td>163.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.34 (+15.21%)</td><td>0.24 <b>(+22.47%)</b></td><td>0.21 <b>(+27.78%)</b></td><td>0.14 (+6.92%)</td><td>0.09 (+19.71%)</td><td>534.60 (-6.47%)</td><td>348.30 (-17.53%)</td><td>345.50 <b>(-21.73%)</b></td><td>214.00 (-13.18%)</td><td>129.88 (-6.82%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>571.60 (n/a)</td><td>422.32 (n/a)</td><td>441.40 (n/a)</td><td>246.50 (n/a)</td><td>139.39 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.36 (+15.95%)</td><td>0.18 (-14.89%)</td><td>0.13 <b>(-23.89%)</b></td><td>0.12 <b>(-20.41%)</b></td><td>0.10 <b>(+53.21%)</b></td><td>594.20 <b>(+25.65%)</b></td><td>483.78 <b>(+28.95%)</b></td><td>562.00 <b>(+31.37%)</b></td><td>203.00 (-13.73%)</td><td>160.88 <b>(+57.41%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>472.90 (n/a)</td><td>375.18 (n/a)</td><td>427.80 (n/a)</td><td>235.30 (n/a)</td><td>102.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.25 (-15.97%)</td><td>0.17 (-13.29%)</td><td>0.15 (-12.38%)</td><td>0.13 (+19.62%)</td><td>0.05 <b>(-38.88%)</b></td><td>554.90 (-16.41%)</td><td>464.18 (+6.96%)</td><td>503.60 (+14.14%)</td><td>298.90 (+19.04%)</td><td>99.76 <b>(-40.05%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>663.80 (n/a)</td><td>433.98 (n/a)</td><td>441.20 (n/a)</td><td>251.10 (n/a)</td><td>166.41 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (+12.87%)</td><td>0.10 (-6.00%)</td><td>0.07 <b>(-35.92%)</b></td><td>0.06 (-4.74%)</td><td>0.04 <b>(+51.02%)</b></td><td>568.70 (+4.96%)</td><td>428.40 (+13.56%)</td><td>502.30 <b>(+56.04%)</b></td><td>248.20 (-11.39%)</td><td>154.88 <b>(+40.22%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>541.80 (n/a)</td><td>377.26 (n/a)</td><td>321.90 (n/a)</td><td>280.10 (n/a)</td><td>110.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 <b>(-26.92%)</b></td><td>0.10 (-18.41%)</td><td>0.13 (-7.10%)</td><td>0.04 <b>(-49.56%)</b></td><td>0.05 (-10.15%)</td><td>1010.60 <b>(+98.23%)</b></td><td>475.20 <b>(+37.06%)</b></td><td>287.20 (+7.65%)</td><td>268.10 <b>(+36.86%)</b></td><td>318.71 <b>(+111.14%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>509.80 (n/a)</td><td>346.70 (n/a)</td><td>266.80 (n/a)</td><td>195.90 (n/a)</td><td>150.95 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (-15.09%)</td><td>0.09 (-17.07%)</td><td>0.07 (-8.46%)</td><td>0.06 (-16.58%)</td><td>0.03 <b>(-23.04%)</b></td><td>590.20 (+19.86%)</td><td>455.48 (+18.83%)</td><td>497.70 (+9.24%)</td><td>285.20 (+17.75%)</td><td>130.25 (+9.40%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>492.40 (n/a)</td><td>383.32 (n/a)</td><td>455.60 (n/a)</td><td>242.20 (n/a)</td><td>119.06 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (-0.28%)</td><td>0.10 (-15.24%)</td><td>0.10 <b>(-24.08%)</b></td><td>0.07 (-5.69%)</td><td>0.03 (+3.32%)</td><td>565.40 (+6.04%)</td><td>394.82 (+18.92%)</td><td>379.40 <b>(+31.74%)</b></td><td>246.70 (+0.24%)</td><td>127.26 (+7.98%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>533.20 (n/a)</td><td>332.00 (n/a)</td><td>288.00 (n/a)</td><td>246.10 (n/a)</td><td>117.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (+1.64%)</td><td>0.10 (-8.01%)</td><td>0.08 (-10.83%)</td><td>0.07 (-0.94%)</td><td>0.04 (-7.41%)</td><td>564.00 (+0.97%)</td><td>414.22 (+7.52%)</td><td>463.30 (+12.15%)</td><td>242.20 (-1.62%)</td><td>129.03 (-3.52%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>558.60 (n/a)</td><td>385.26 (n/a)</td><td>413.10 (n/a)</td><td>246.20 (n/a)</td><td>133.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.11 (-10.99%)</td><td>0.09 (-3.02%)</td><td>0.08 (+12.19%)</td><td>0.07 (-1.51%)</td><td>0.02 <b>(-36.77%)</b></td><td>541.80 (+1.54%)</td><td>430.26 (-0.49%)</td><td>449.50 (-10.85%)</td><td>336.60 (+12.31%)</td><td>82.69 <b>(-28.53%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>533.60 (n/a)</td><td>432.38 (n/a)</td><td>504.20 (n/a)</td><td>299.70 (n/a)</td><td>115.70 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.16 (-0.28%)</td><td>0.12 <b>(+24.31%)</b></td><td>0.14 <b>(+71.85%)</b></td><td>0.05 (+0.26%)</td><td>0.05 (+16.39%)</td><td>747.90 (-0.27%)</td><td>415.98 (-15.92%)</td><td>303.20 <b>(-41.80%)</b></td><td>259.80 (+0.27%)</td><td>211.36 (+15.22%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>749.90 (n/a)</td><td>494.72 (n/a)</td><td>521.00 (n/a)</td><td>259.10 (n/a)</td><td>183.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (-4.25%)</td><td>0.12 (-4.39%)</td><td>0.13 (+1.75%)</td><td>0.06 <b>(-24.23%)</b></td><td>0.04 <b>(+25.95%)</b></td><td>670.30 <b>(+31.97%)</b></td><td>405.88 (+12.05%)</td><td>305.90 (-1.70%)</td><td>264.80 (+4.46%)</td><td>179.77 <b>(+64.79%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>507.90 (n/a)</td><td>362.24 (n/a)</td><td>311.20 (n/a)</td><td>253.50 (n/a)</td><td>109.09 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.15 (-7.73%)</td><td>0.11 (+11.33%)</td><td>0.09 (+9.72%)</td><td>0.07 (+6.72%)</td><td>0.03 (-18.65%)</td><td>599.10 (-6.30%)</td><td>414.54 (-13.69%)</td><td>446.50 (-8.84%)</td><td>265.30 (+8.37%)</td><td>130.88 (-19.73%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>639.40 (n/a)</td><td>480.28 (n/a)</td><td>489.80 (n/a)</td><td>244.80 (n/a)</td><td>163.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (-16.76%)</td><td>0.11 (+8.87%)</td><td>0.10 (-3.92%)</td><td>0.06 <b>(+193.09%)</b></td><td>0.03 <b>(-47.28%)</b></td><td>643.10 <b>(-65.88%)</b></td><td>414.80 <b>(-39.02%)</b></td><td>394.60 (+4.09%)</td><td>304.90 <b>(+20.13%)</b></td><td>134.62 <b>(-80.23%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1884.80 (n/a)</td><td>680.20 (n/a)</td><td>379.10 (n/a)</td><td>253.80 (n/a)</td><td>680.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 <b>(-31.68%)</b></td><td>0.10 (-2.78%)</td><td>0.10 (+4.47%)</td><td>0.08 (+18.57%)</td><td>0.02 <b>(-65.67%)</b></td><td>543.00 (-15.67%)</td><td>431.32 (-7.66%)</td><td>421.70 (-4.27%)</td><td>346.10 <b>(+46.34%)</b></td><td>70.72 <b>(-57.41%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>643.90 (n/a)</td><td>467.12 (n/a)</td><td>440.50 (n/a)</td><td>236.50 (n/a)</td><td>166.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.16 (+4.11%)</td><td>0.09 (-12.19%)</td><td>0.08 (-17.14%)</td><td>0.06 (-17.66%)</td><td>0.04 <b>(+27.98%)</b></td><td>668.80 <b>(+21.45%)</b></td><td>491.08 (+19.18%)</td><td>524.50 <b>(+20.69%)</b></td><td>257.40 (-3.96%)</td><td>151.62 <b>(+42.96%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>550.70 (n/a)</td><td>412.06 (n/a)</td><td>434.60 (n/a)</td><td>268.00 (n/a)</td><td>106.06 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.16 (-1.20%)</td><td>0.10 (-13.54%)</td><td>0.08 <b>(-30.91%)</b></td><td>0.06 (+0.73%)</td><td>0.05 (+19.25%)</td><td>609.90 (-0.72%)</td><td>415.48 <b>(+21.15%)</b></td><td>412.20 <b>(+44.73%)</b></td><td>211.30 (+1.20%)</td><td>179.94 (+14.39%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>614.30 (n/a)</td><td>342.94 (n/a)</td><td>284.80 (n/a)</td><td>208.80 (n/a)</td><td>157.30 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (-1.85%)</td><td>0.09 (-3.15%)</td><td>0.11 (+6.00%)</td><td>0.07 (+9.37%)</td><td>0.02 (+11.52%)</td><td>531.60 (-8.57%)</td><td>392.16 (+3.80%)</td><td>323.40 (-5.66%)</td><td>302.70 (+1.88%)</td><td>112.74 (-2.38%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>581.40 (n/a)</td><td>377.80 (n/a)</td><td>342.80 (n/a)</td><td>297.10 (n/a)</td><td>115.49 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (-6.81%)</td><td>0.10 (-3.39%)</td><td>0.12 (-3.99%)</td><td>0.06 <b>(+26.88%)</b></td><td>0.03 (-17.35%)</td><td>549.80 <b>(-21.19%)</b></td><td>387.64 (-2.13%)</td><td>302.60 (+4.13%)</td><td>271.20 (+7.32%)</td><td>142.83 <b>(-25.90%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>697.60 (n/a)</td><td>396.06 (n/a)</td><td>290.60 (n/a)</td><td>252.70 (n/a)</td><td>192.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.16 (+8.90%)</td><td>0.10 (-10.11%)</td><td>0.08 <b>(-37.16%)</b></td><td>0.07 (+13.86%)</td><td>0.04 (-5.83%)</td><td>482.30 (-12.18%)</td><td>390.80 (+7.29%)</td><td>439.10 <b>(+59.15%)</b></td><td>221.50 (-8.17%)</td><td>103.73 <b>(-27.84%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>549.20 (n/a)</td><td>364.24 (n/a)</td><td>275.90 (n/a)</td><td>241.20 (n/a)</td><td>143.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.10 <b>(-27.75%)</b></td><td>0.08 <b>(-21.86%)</b></td><td>0.07 (-11.88%)</td><td>0.06 (-12.86%)</td><td>0.02 <b>(-49.39%)</b></td><td>568.00 (+14.77%)</td><td>471.28 <b>(+21.90%)</b></td><td>496.90 (+13.47%)</td><td>341.80 <b>(+38.44%)</b></td><td>92.05 <b>(-20.24%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>494.90 (n/a)</td><td>386.62 (n/a)</td><td>437.90 (n/a)</td><td>246.90 (n/a)</td><td>115.41 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.09 <b>(-35.70%)</b></td><td>0.06 <b>(-26.95%)</b></td><td>0.07 <b>(-22.84%)</b></td><td>0.03 <b>(+45.50%)</b></td><td>0.02 <b>(-51.97%)</b></td><td>1122.90 <b>(-31.27%)</b></td><td>614.74 (+0.94%)</td><td>506.00 <b>(+29.61%)</b></td><td>380.60 <b>(+55.54%)</b></td><td>293.35 <b>(-49.42%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1633.90 (n/a)</td><td>609.02 (n/a)</td><td>390.40 (n/a)</td><td>244.70 (n/a)</td><td>579.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.47 (-8.73%)</td><td>0.33 (-16.06%)</td><td>0.32 <b>(-24.26%)</b></td><td>0.19 <b>(-27.18%)</b></td><td>0.11 (-4.01%)</td><td>689.00 <b>(+37.31%)</b></td><td>441.64 <b>(+21.93%)</b></td><td>416.00 <b>(+32.02%)</b></td><td>277.30 (+9.56%)</td><td>162.10 <b>(+41.25%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.52 (n/a)</td><td>0.39 (n/a)</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>501.80 (n/a)</td><td>362.20 (n/a)</td><td>315.10 (n/a)</td><td>253.10 (n/a)</td><td>114.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.49 (+9.53%)</td><td>0.34 <b>(+24.09%)</b></td><td>0.34 (+17.32%)</td><td>0.23 <b>(+89.53%)</b></td><td>0.11 (-8.52%)</td><td>569.70 <b>(-47.24%)</b></td><td>421.74 <b>(-27.11%)</b></td><td>380.80 (-14.77%)</td><td>267.90 (-8.72%)</td><td>136.50 <b>(-55.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.45 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>1079.80 (n/a)</td><td>578.60 (n/a)</td><td>446.80 (n/a)</td><td>293.50 (n/a)</td><td>304.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.45 (+11.43%)</td><td>0.31 (+3.68%)</td><td>0.28 (+1.55%)</td><td>0.22 (+11.33%)</td><td>0.09 (+17.10%)</td><td>609.50 (-10.18%)</td><td>450.98 (-3.07%)</td><td>461.60 (-1.54%)</td><td>289.90 (-10.25%)</td><td>123.75 (-8.04%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>678.60 (n/a)</td><td>465.26 (n/a)</td><td>468.80 (n/a)</td><td>323.00 (n/a)</td><td>134.58 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.00 (+0.00%)</td><td>0.00 (+4.17%)</td><td>0.00 (+20.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+21.92%)</b></td><td>16439.00 (-18.88%)</td><td>10073.45 (+0.05%)</td><td>6520.95 <b>(-22.13%)</b></td><td>5639.02 (+1.95%)</td><td>5488.54 (-7.37%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20264.55 (n/a)</td><td>10068.04 (n/a)</td><td>8374.56 (n/a)</td><td>5531.14 (n/a)</td><td>5925.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.00 (-15.38%)</td><td>0.00 <b>(+33.33%)</b></td><td>0.00 <b>(+125.00%)</b></td><td>0.00 <b>(+25.00%)</b></td><td>0.00 <b>(-28.16%)</b></td><td>17061.78 <b>(-22.51%)</b></td><td>11396.32 <b>(-32.13%)</b></td><td>8731.40 <b>(-54.32%)</b></td><td>7139.74 (+13.65%)</td><td>4577.35 <b>(-25.34%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22018.75 (n/a)</td><td>16792.61 (n/a)</td><td>19115.42 (n/a)</td><td>6282.33 (n/a)</td><td>6131.27 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.14 <b>(+55.97%)</b></td><td>0.10 <b>(+34.33%)</b></td><td>0.10 <b>(+31.27%)</b></td><td>0.08 (+9.97%)</td><td>0.03 <b>(+199.95%)</b></td><td>27168.63 (-9.05%)</td><td>21057.45 <b>(-22.79%)</b></td><td>21526.52 <b>(-23.82%)</b></td><td>15300.87 <b>(-35.90%)</b></td><td>4919.82 <b>(+72.77%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>29871.90 (n/a)</td><td>27274.12 (n/a)</td><td>28256.87 (n/a)</td><td>23871.04 (n/a)</td><td>2847.54 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.46 (-1.31%)</td><td>1.98 (+4.15%)</td><td>1.79 (+0.82%)</td><td>1.59 (+15.22%)</td><td>0.37 <b>(-23.02%)</b></td><td>657.80 (-13.21%)</td><td>545.06 (-6.32%)</td><td>584.80 (-0.80%)</td><td>425.40 (+1.33%)</td><td>98.44 <b>(-32.45%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>2.50 (n/a)</td><td>1.90 (n/a)</td><td>1.78 (n/a)</td><td>1.38 (n/a)</td><td>0.49 (n/a)</td><td>757.90 (n/a)</td><td>581.82 (n/a)</td><td>589.50 (n/a)</td><td>419.80 (n/a)</td><td>145.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>3.21 <b>(+29.42%)</b></td><td>2.16 <b>(+99.28%)</b></td><td>1.73 <b>(+479.71%)</b></td><td>1.16 <b>(+293.85%)</b></td><td>0.96 (-11.73%)</td><td>902.30 <b>(-74.61%)</b></td><td>569.26 <b>(-75.32%)</b></td><td>604.40 <b>(-82.75%)</b></td><td>326.50 <b>(-22.74%)</b></td><td>245.68 <b>(-85.38%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>2.48 (n/a)</td><td>1.09 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>1.09 (n/a)</td><td>3553.70 (n/a)</td><td>2306.80 (n/a)</td><td>3503.80 (n/a)</td><td>422.60 (n/a)</td><td>1680.89 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.66 <b>(-34.81%)</b></td><td>1.97 <b>(-24.73%)</b></td><td>1.74 <b>(-29.92%)</b></td><td>1.40 (-11.71%)</td><td>0.58 <b>(-44.34%)</b></td><td>746.50 (+13.26%)</td><td>568.58 <b>(+25.44%)</b></td><td>601.70 <b>(+42.68%)</b></td><td>394.00 <b>(+53.37%)</b></td><td>157.26 (-8.60%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>4.08 (n/a)</td><td>2.62 (n/a)</td><td>2.49 (n/a)</td><td>1.59 (n/a)</td><td>1.03 (n/a)</td><td>659.10 (n/a)</td><td>453.28 (n/a)</td><td>421.70 (n/a)</td><td>256.90 (n/a)</td><td>172.07 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.45 <b>(-33.72%)</b></td><td>1.59 <b>(-23.02%)</b></td><td>1.31 <b>(-48.75%)</b></td><td>0.95 <b>(+222.25%)</b></td><td>0.63 <b>(-52.82%)</b></td><td>1103.80 <b>(-68.97%)</b></td><td>743.34 <b>(-32.88%)</b></td><td>799.70 <b>(+95.10%)</b></td><td>428.20 <b>(+50.88%)</b></td><td>274.49 <b>(-80.23%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.69 (n/a)</td><td>2.07 (n/a)</td><td>2.56 (n/a)</td><td>0.29 (n/a)</td><td>1.33 (n/a)</td><td>3556.90 (n/a)</td><td>1107.48 (n/a)</td><td>409.90 (n/a)</td><td>283.80 (n/a)</td><td>1388.38 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.82 <b>(+149.60%)</b></td><td>2.82 <b>(+160.70%)</b></td><td>3.00 <b>(+190.21%)</b></td><td>0.59 (-0.51%)</td><td>1.51 <b>(+175.85%)</b></td><td>3548.70 (+0.51%)</td><td>1234.08 <b>(-47.45%)</b></td><td>699.90 <b>(-65.54%)</b></td><td>435.30 <b>(-59.93%)</b></td><td>1300.83 <b>(+21.88%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>1.93 (n/a)</td><td>1.08 (n/a)</td><td>1.03 (n/a)</td><td>0.59 (n/a)</td><td>0.55 (n/a)</td><td>3530.60 (n/a)</td><td>2348.48 (n/a)</td><td>2031.20 (n/a)</td><td>1086.40 (n/a)</td><td>1067.31 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>5.79 (+15.47%)</td><td>3.13 (-8.06%)</td><td>2.56 (-18.98%)</td><td>2.11 (+8.36%)</td><td>1.52 <b>(+23.61%)</b></td><td>994.10 (-7.71%)</td><td>764.28 (+10.89%)</td><td>819.70 <b>(+23.43%)</b></td><td>361.90 (-13.40%)</td><td>247.77 (-5.20%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.02 (n/a)</td><td>3.40 (n/a)</td><td>3.16 (n/a)</td><td>1.95 (n/a)</td><td>1.23 (n/a)</td><td>1077.20 (n/a)</td><td>689.20 (n/a)</td><td>664.10 (n/a)</td><td>417.90 (n/a)</td><td>261.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.29 <b>(-23.00%)</b></td><td>3.39 (-1.51%)</td><td>3.64 <b>(+21.21%)</b></td><td>2.42 (-3.65%)</td><td>0.81 <b>(-35.22%)</b></td><td>866.50 (+3.78%)</td><td>651.04 (-1.77%)</td><td>576.20 (-17.50%)</td><td>488.50 <b>(+29.89%)</b></td><td>167.04 (-9.97%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.58 (n/a)</td><td>3.44 (n/a)</td><td>3.00 (n/a)</td><td>2.51 (n/a)</td><td>1.26 (n/a)</td><td>834.90 (n/a)</td><td>662.78 (n/a)</td><td>698.40 (n/a)</td><td>376.10 (n/a)</td><td>185.53 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>5.74 <b>(-20.43%)</b></td><td>3.35 (+5.36%)</td><td>3.14 <b>(+82.16%)</b></td><td>2.02 <b>(+234.64%)</b></td><td>1.50 <b>(-48.20%)</b></td><td>1038.30 <b>(-70.12%)</b></td><td>722.82 <b>(-50.61%)</b></td><td>667.60 <b>(-45.11%)</b></td><td>365.10 <b>(+25.68%)</b></td><td>280.20 <b>(-78.57%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>7.22 (n/a)</td><td>3.18 (n/a)</td><td>1.72 (n/a)</td><td>0.60 (n/a)</td><td>2.90 (n/a)</td><td>3474.60 (n/a)</td><td>1463.48 (n/a)</td><td>1216.20 (n/a)</td><td>290.50 (n/a)</td><td>1307.35 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.00 <b>(-25.91%)</b></td><td>1.80 <b>(-51.53%)</b></td><td>1.02 <b>(-77.27%)</b></td><td>0.59 <b>(-45.30%)</b></td><td>1.53 (-13.11%)</td><td>3574.60 <b>(+82.83%)</b></td><td>2092.66 <b>(+161.91%)</b></td><td>2058.50 <b>(+340.04%)</b></td><td>524.00 <b>(+34.95%)</b></td><td>1467.95 <b>(+121.93%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.40 (n/a)</td><td>3.72 (n/a)</td><td>4.48 (n/a)</td><td>1.07 (n/a)</td><td>1.77 (n/a)</td><td>1955.20 (n/a)</td><td>799.00 (n/a)</td><td>467.80 (n/a)</td><td>388.30 (n/a)</td><td>661.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.84 <b>(-28.74%)</b></td><td>3.22 (-10.06%)</td><td>3.43 (-11.86%)</td><td>0.62 <b>(-29.37%)</b></td><td>1.67 <b>(-30.87%)</b></td><td>3395.80 <b>(+41.59%)</b></td><td>1134.54 (+12.42%)</td><td>611.60 (+13.45%)</td><td>433.00 <b>(+40.36%)</b></td><td>1270.69 <b>(+44.49%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>6.80 (n/a)</td><td>3.58 (n/a)</td><td>3.89 (n/a)</td><td>0.87 (n/a)</td><td>2.42 (n/a)</td><td>2398.30 (n/a)</td><td>1009.18 (n/a)</td><td>539.10 (n/a)</td><td>308.50 (n/a)</td><td>879.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>4.82 (+3.40%)</td><td>4.29 (+6.95%)</td><td>4.16 (+3.96%)</td><td>3.98 (+19.80%)</td><td>0.34 <b>(-28.61%)</b></td><td>1054.50 (-16.53%)</td><td>982.94 (-7.14%)</td><td>1007.90 (-3.81%)</td><td>870.80 (-3.29%)</td><td>73.98 <b>(-43.26%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>4.66 (n/a)</td><td>4.01 (n/a)</td><td>4.00 (n/a)</td><td>3.32 (n/a)</td><td>0.47 (n/a)</td><td>1263.30 (n/a)</td><td>1058.52 (n/a)</td><td>1047.80 (n/a)</td><td>900.40 (n/a)</td><td>130.39 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>6.12 (-17.37%)</td><td>3.77 <b>(-29.43%)</b></td><td>3.82 <b>(-34.91%)</b></td><td>1.18 <b>(-62.16%)</b></td><td>2.16 <b>(+25.90%)</b></td><td>3562.60 <b>(+164.27%)</b></td><td>1621.22 <b>(+87.56%)</b></td><td>1096.90 <b>(+53.63%)</b></td><td>685.60 <b>(+21.02%)</b></td><td>1209.95 <b>(+279.82%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>7.40 (n/a)</td><td>5.35 (n/a)</td><td>5.87 (n/a)</td><td>3.11 (n/a)</td><td>1.72 (n/a)</td><td>1348.10 (n/a)</td><td>864.38 (n/a)</td><td>714.00 (n/a)</td><td>566.50 (n/a)</td><td>318.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>8.46 (+15.36%)</td><td>6.69 <b>(+22.39%)</b></td><td>7.52 <b>(+35.88%)</b></td><td>3.40 (-0.89%)</td><td>2.04 <b>(+45.85%)</b></td><td>1235.00 (+0.90%)</td><td>699.88 (-14.14%)</td><td>558.10 <b>(-26.41%)</b></td><td>495.90 (-13.32%)</td><td>307.67 <b>(+25.97%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>7.33 (n/a)</td><td>5.47 (n/a)</td><td>5.53 (n/a)</td><td>3.43 (n/a)</td><td>1.40 (n/a)</td><td>1224.00 (n/a)</td><td>815.10 (n/a)</td><td>758.40 (n/a)</td><td>572.10 (n/a)</td><td>244.24 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>7.81 <b>(-26.36%)</b></td><td>6.74 (-3.86%)</td><td>6.75 (-14.87%)</td><td>4.70 <b>(+275.27%)</b></td><td>1.25 <b>(-68.55%)</b></td><td>892.70 <b>(-73.35%)</b></td><td>643.46 <b>(-41.98%)</b></td><td>621.80 (+17.48%)</td><td>536.80 <b>(+35.80%)</b></td><td>145.35 <b>(-88.53%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>10.61 (n/a)</td><td>7.01 (n/a)</td><td>7.92 (n/a)</td><td>1.25 (n/a)</td><td>3.99 (n/a)</td><td>3350.20 (n/a)</td><td>1109.12 (n/a)</td><td>529.30 (n/a)</td><td>395.30 (n/a)</td><td>1267.57 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>8.76 (-11.49%)</td><td>6.97 (+8.36%)</td><td>6.96 (+8.14%)</td><td>3.75 (+3.46%)</td><td>2.05 (-10.80%)</td><td>1119.50 (-3.34%)</td><td>662.86 (-8.69%)</td><td>602.70 (-7.53%)</td><td>478.70 (+12.98%)</td><td>264.76 (-3.12%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>9.90 (n/a)</td><td>6.43 (n/a)</td><td>6.44 (n/a)</td><td>3.62 (n/a)</td><td>2.30 (n/a)</td><td>1158.20 (n/a)</td><td>725.96 (n/a)</td><td>651.80 (n/a)</td><td>423.70 (n/a)</td><td>273.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>10.65 <b>(+70.46%)</b></td><td>7.02 <b>(+60.51%)</b></td><td>8.05 <b>(+97.54%)</b></td><td>1.16 <b>(-66.65%)</b></td><td>3.53 <b>(+226.80%)</b></td><td>3604.40 <b>(+199.89%)</b></td><td>1124.96 (+12.78%)</td><td>521.00 <b>(-49.37%)</b></td><td>393.90 <b>(-41.33%)</b></td><td>1387.82 <b>(+603.71%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>6.25 (n/a)</td><td>4.37 (n/a)</td><td>4.08 (n/a)</td><td>3.49 (n/a)</td><td>1.08 (n/a)</td><td>1201.90 (n/a)</td><td>997.44 (n/a)</td><td>1029.10 (n/a)</td><td>671.40 (n/a)</td><td>197.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.56 <b>(+98.40%)</b></td><td>1.32 <b>(+66.66%)</b></td><td>1.07 <b>(+23.92%)</b></td><td>0.83 <b>(+441.54%)</b></td><td>0.71 <b>(+72.95%)</b></td><td>632.10 <b>(-81.53%)</b></td><td>463.78 <b>(-59.33%)</b></td><td>487.80 (-19.31%)</td><td>204.80 <b>(-49.61%)</b></td><td>164.60 <b>(-87.14%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>1.29 (n/a)</td><td>0.79 (n/a)</td><td>0.87 (n/a)</td><td>0.15 (n/a)</td><td>0.41 (n/a)</td><td>3423.10 (n/a)</td><td>1140.38 (n/a)</td><td>604.50 (n/a)</td><td>406.40 (n/a)</td><td>1279.89 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>2.80 (+8.18%)</td><td>2.32 <b>(+49.61%)</b></td><td>2.12 <b>(+61.77%)</b></td><td>1.95 <b>(+341.66%)</b></td><td>0.38 <b>(-58.87%)</b></td><td>537.20 <b>(-77.36%)</b></td><td>461.06 <b>(-54.44%)</b></td><td>495.80 <b>(-38.18%)</b></td><td>374.70 (-7.55%)</td><td>72.02 <b>(-91.07%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>2.59 (n/a)</td><td>1.55 (n/a)</td><td>1.31 (n/a)</td><td>0.44 (n/a)</td><td>0.92 (n/a)</td><td>2372.40 (n/a)</td><td>1011.94 (n/a)</td><td>802.00 (n/a)</td><td>405.30 (n/a)</td><td>806.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>3.92 (+0.78%)</td><td>3.29 <b>(+46.32%)</b></td><td>3.26 <b>(+38.84%)</b></td><td>2.60 <b>(+346.66%)</b></td><td>0.49 <b>(-65.68%)</b></td><td>805.20 <b>(-77.61%)</b></td><td>648.58 <b>(-57.50%)</b></td><td>644.10 <b>(-27.98%)</b></td><td>534.70 (-0.78%)</td><td>101.65 <b>(-92.14%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.89 (n/a)</td><td>2.25 (n/a)</td><td>2.34 (n/a)</td><td>0.58 (n/a)</td><td>1.43 (n/a)</td><td>3596.40 (n/a)</td><td>1526.06 (n/a)</td><td>894.30 (n/a)</td><td>538.90 (n/a)</td><td>1292.83 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>1.66 (+4.62%)</td><td>1.39 <b>(+26.12%)</b></td><td>1.57 <b>(+66.44%)</b></td><td>0.96 <b>(+31.86%)</b></td><td>0.33 (-2.88%)</td><td>546.40 <b>(-24.16%)</b></td><td>398.72 <b>(-22.45%)</b></td><td>332.90 <b>(-39.92%)</b></td><td>316.10 (-4.41%)</td><td>106.82 <b>(-29.86%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>1.59 (n/a)</td><td>1.10 (n/a)</td><td>0.95 (n/a)</td><td>0.73 (n/a)</td><td>0.34 (n/a)</td><td>720.50 (n/a)</td><td>514.14 (n/a)</td><td>554.10 (n/a)</td><td>330.70 (n/a)</td><td>152.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.13 (+11.06%)</td><td>0.10 <b>(+46.30%)</b></td><td>0.11 <b>(+91.76%)</b></td><td>0.06 <b>(+244.05%)</b></td><td>0.03 <b>(-20.36%)</b></td><td>563.60 <b>(-70.94%)</b></td><td>359.74 <b>(-51.67%)</b></td><td>294.70 <b>(-47.86%)</b></td><td>243.30 (-9.96%)</td><td>132.00 <b>(-80.61%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1939.20 (n/a)</td><td>744.34 (n/a)</td><td>565.20 (n/a)</td><td>270.20 (n/a)</td><td>680.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.12 (-8.25%)</td><td>0.09 (+16.88%)</td><td>0.11 <b>(+51.88%)</b></td><td>0.06 (-2.09%)</td><td>0.03 (+6.38%)</td><td>574.40 (+2.13%)</td><td>387.60 (-12.39%)</td><td>299.10 <b>(-34.15%)</b></td><td>277.80 (+8.98%)</td><td>141.31 <b>(+23.81%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>562.40 (n/a)</td><td>442.44 (n/a)</td><td>454.20 (n/a)</td><td>254.90 (n/a)</td><td>114.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.24 (-9.52%)</td><td>0.23 <b>(+46.36%)</b></td><td>0.24 <b>(+74.40%)</b></td><td>0.19 <b>(+70.42%)</b></td><td>0.02 <b>(-63.19%)</b></td><td>353.40 <b>(-41.32%)</b></td><td>292.00 <b>(-37.27%)</b></td><td>278.00 <b>(-42.66%)</b></td><td>272.20 (+10.52%)</td><td>34.55 <b>(-73.91%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>602.20 (n/a)</td><td>465.52 (n/a)</td><td>484.80 (n/a)</td><td>246.30 (n/a)</td><td>132.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.24 (-15.51%)</td><td>0.14 (-19.70%)</td><td>0.13 (-0.17%)</td><td>0.08 <b>(-30.85%)</b></td><td>0.06 (-16.80%)</td><td>847.30 <b>(+44.62%)</b></td><td>538.12 <b>(+26.14%)</b></td><td>507.70 (+0.18%)</td><td>271.80 (+18.38%)</td><td>216.47 <b>(+40.08%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>585.90 (n/a)</td><td>426.60 (n/a)</td><td>506.80 (n/a)</td><td>229.60 (n/a)</td><td>154.53 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.31 <b>(+35.27%)</b></td><td>0.18 (+9.04%)</td><td>0.15 (-14.78%)</td><td>0.11 (-13.30%)</td><td>0.08 <b>(+88.89%)</b></td><td>621.30 (+15.33%)</td><td>412.40 (+0.37%)</td><td>436.90 (+17.35%)</td><td>214.90 <b>(-26.05%)</b></td><td>162.50 <b>(+52.64%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>538.70 (n/a)</td><td>410.86 (n/a)</td><td>372.30 (n/a)</td><td>290.60 (n/a)</td><td>106.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.56 (+14.02%)</td><td>0.37 (+8.25%)</td><td>0.33 <b>(+29.10%)</b></td><td>0.22 (-9.36%)</td><td>0.14 (+18.45%)</td><td>584.00 (+10.33%)</td><td>400.80 (-5.30%)</td><td>395.00 <b>(-22.55%)</b></td><td>233.20 (-12.30%)</td><td>145.46 (+12.18%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>529.30 (n/a)</td><td>423.22 (n/a)</td><td>510.00 (n/a)</td><td>265.90 (n/a)</td><td>129.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.52 (+18.89%)</td><td>0.40 <b>(+33.57%)</b></td><td>0.46 <b>(+77.93%)</b></td><td>0.26 <b>(+63.50%)</b></td><td>0.11 (-11.10%)</td><td>501.30 <b>(-38.83%)</b></td><td>351.26 <b>(-30.91%)</b></td><td>285.50 <b>(-43.80%)</b></td><td>251.60 (-15.88%)</td><td>111.22 <b>(-49.56%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>819.50 (n/a)</td><td>508.38 (n/a)</td><td>508.00 (n/a)</td><td>299.10 (n/a)</td><td>220.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.49 (-8.99%)</td><td>0.30 (-18.08%)</td><td>0.27 (-19.46%)</td><td>0.23 (-19.16%)</td><td>0.11 (+5.52%)</td><td>558.40 <b>(+23.70%)</b></td><td>466.26 <b>(+24.88%)</b></td><td>488.50 <b>(+24.17%)</b></td><td>268.90 (+9.84%)</td><td>116.55 <b>(+40.25%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.54 (n/a)</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.10 (n/a)</td><td>451.40 (n/a)</td><td>373.36 (n/a)</td><td>393.40 (n/a)</td><td>244.80 (n/a)</td><td>83.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:23:38</td><td>0.07 (+12.16%)</td><td>0.05 (-10.33%)</td><td>0.04 <b>(-24.15%)</b></td><td>0.04 <b>(-31.11%)</b></td><td>0.02 <b>(+323.25%)</b></td><td>449.60 <b>(+45.17%)</b></td><td>342.90 <b>(+20.16%)</b></td><td>383.60 <b>(+31.82%)</b></td><td>230.90 (-10.85%)</td><td>101.12 <b>(+428.96%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>309.70 (n/a)</td><td>285.36 (n/a)</td><td>291.00 (n/a)</td><td>259.00 (n/a)</td><td>19.12 (n/a)</td>
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
