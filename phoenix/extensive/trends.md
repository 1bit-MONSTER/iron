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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+8.99%)</td><td>0.02 (+3.51%)</td><td>0.02 (-8.11%)</td><td>0.01 (-7.46%)</td><td>0.01 (-2.96%)</td><td>684.90 (+8.06%)</td><td>412.82 (-4.89%)</td><td>401.50 (+8.84%)</td><td>247.80 (-8.26%)</td><td>171.02 (-5.88%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.80 (n/a)</td><td>434.04 (n/a)</td><td>368.90 (n/a)</td><td>270.10 (n/a)</td><td>181.71 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (-14.62%)</td><td>0.01 <b>(-24.49%)</b></td><td>0.01 <b>(-35.02%)</b></td><td>0.01 <b>(-29.12%)</b></td><td>0.00 <b>(+22.33%)</b></td><td>566.70 <b>(+41.08%)</b></td><td>452.34 <b>(+36.68%)</b></td><td>487.40 <b>(+53.90%)</b></td><td>310.30 (+17.14%)</td><td>110.88 <b>(+100.29%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>401.70 (n/a)</td><td>330.96 (n/a)</td><td>316.70 (n/a)</td><td>264.90 (n/a)</td><td>55.36 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (+15.01%)</td><td>0.02 (-8.51%)</td><td>0.01 (-16.12%)</td><td>0.00 <b>(-79.55%)</b></td><td>0.01 <b>(+73.37%)</b></td><td>2559.60 <b>(+388.94%)</b></td><td>820.40 <b>(+111.35%)</b></td><td>524.10 (+19.22%)</td><td>208.30 (-13.03%)</td><td>986.08 <b>(+659.19%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>523.50 (n/a)</td><td>388.18 (n/a)</td><td>439.60 (n/a)</td><td>239.50 (n/a)</td><td>129.89 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 <b>(+27.05%)</b></td><td>0.02 (+6.61%)</td><td>0.02 (+7.56%)</td><td>0.00 <b>(-66.86%)</b></td><td>0.01 <b>(+57.25%)</b></td><td>1920.70 <b>(+201.76%)</b></td><td>626.68 <b>(+57.40%)</b></td><td>267.20 (-7.03%)</td><td>181.40 <b>(-21.27%)</b></td><td>735.95 <b>(+282.50%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.50 (n/a)</td><td>398.14 (n/a)</td><td>287.40 (n/a)</td><td>230.40 (n/a)</td><td>192.40 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 <b>(-34.82%)</b></td><td>0.01 <b>(-32.35%)</b></td><td>0.01 <b>(-49.28%)</b></td><td>0.01 <b>(+176.84%)</b></td><td>0.00 <b>(-69.33%)</b></td><td>685.30 <b>(-63.88%)</b></td><td>536.76 (-14.35%)</td><td>521.20 <b>(+97.13%)</b></td><td>373.70 <b>(+53.41%)</b></td><td>118.18 <b>(-83.49%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1897.10 (n/a)</td><td>626.66 (n/a)</td><td>264.40 (n/a)</td><td>243.60 (n/a)</td><td>715.92 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (-5.50%)</td><td>0.01 (-7.08%)</td><td>0.01 (-8.62%)</td><td>0.01 (-3.09%)</td><td>0.00 (-2.19%)</td><td>654.90 (+3.20%)</td><td>489.06 (+8.13%)</td><td>480.10 (+9.44%)</td><td>297.00 (+5.81%)</td><td>138.11 (+8.11%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>634.60 (n/a)</td><td>452.28 (n/a)</td><td>438.70 (n/a)</td><td>280.70 (n/a)</td><td>127.75 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (-12.14%)</td><td>0.04 (-9.60%)</td><td>0.04 (+13.28%)</td><td>0.01 <b>(-70.94%)</b></td><td>0.02 <b>(+28.27%)</b></td><td>1930.10 <b>(+244.11%)</b></td><td>617.40 <b>(+82.64%)</b></td><td>286.50 (-11.71%)</td><td>221.00 (+13.86%)</td><td>737.17 <b>(+434.59%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>560.90 (n/a)</td><td>338.04 (n/a)</td><td>324.50 (n/a)</td><td>194.10 (n/a)</td><td>137.89 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (-1.31%)</td><td>0.03 (-9.04%)</td><td>0.02 <b>(-34.80%)</b></td><td>0.02 (-9.89%)</td><td>0.01 (+17.38%)</td><td>640.50 (+10.99%)</td><td>450.40 (+15.23%)</td><td>506.70 <b>(+53.36%)</b></td><td>246.90 (+1.31%)</td><td>180.99 <b>(+24.09%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>577.10 (n/a)</td><td>390.88 (n/a)</td><td>330.40 (n/a)</td><td>243.70 (n/a)</td><td>145.85 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (-8.33%)</td><td>0.04 (-4.00%)</td><td>0.03 (-14.84%)</td><td>0.03 <b>(+32.27%)</b></td><td>0.01 <b>(-22.87%)</b></td><td>448.90 <b>(-24.40%)</b></td><td>357.30 (-1.18%)</td><td>405.90 (+17.41%)</td><td>259.90 (+9.06%)</td><td>89.02 <b>(-37.84%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>593.80 (n/a)</td><td>361.56 (n/a)</td><td>345.70 (n/a)</td><td>238.30 (n/a)</td><td>143.21 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 <b>(+25.51%)</b></td><td>0.04 (+17.20%)</td><td>0.04 <b>(+28.49%)</b></td><td>0.02 <b>(+31.92%)</b></td><td>0.02 (+18.01%)</td><td>567.00 <b>(-24.20%)</b></td><td>359.80 (-15.88%)</td><td>274.30 <b>(-22.16%)</b></td><td>195.70 <b>(-20.35%)</b></td><td>160.73 <b>(-23.42%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>748.00 (n/a)</td><td>427.72 (n/a)</td><td>352.40 (n/a)</td><td>245.70 (n/a)</td><td>209.89 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (-6.45%)</td><td>0.03 (-1.88%)</td><td>0.03 (+3.40%)</td><td>0.02 <b>(+268.45%)</b></td><td>0.01 <b>(-48.21%)</b></td><td>548.10 <b>(-72.86%)</b></td><td>428.10 <b>(-39.75%)</b></td><td>438.50 (-3.29%)</td><td>252.00 (+6.92%)</td><td>109.55 <b>(-85.35%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2019.60 (n/a)</td><td>710.58 (n/a)</td><td>453.40 (n/a)</td><td>235.70 (n/a)</td><td>747.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 <b>(+20.23%)</b></td><td>0.03 <b>(-20.19%)</b></td><td>0.02 <b>(-47.24%)</b></td><td>0.01 <b>(-44.29%)</b></td><td>0.02 <b>(+72.49%)</b></td><td>1039.90 <b>(+79.48%)</b></td><td>551.60 <b>(+57.47%)</b></td><td>560.40 <b>(+89.52%)</b></td><td>207.20 (-16.82%)</td><td>329.66 <b>(+143.61%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>579.40 (n/a)</td><td>350.30 (n/a)</td><td>295.70 (n/a)</td><td>249.10 (n/a)</td><td>135.32 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 <b>(+51.31%)</b></td><td>0.10 (+3.81%)</td><td>0.09 (-10.83%)</td><td>0.07 <b>(-23.11%)</b></td><td>0.03 <b>(+347.60%)</b></td><td>371.40 <b>(+30.04%)</b></td><td>271.94 (+3.55%)</td><td>283.70 (+12.18%)</td><td>159.00 <b>(-33.92%)</b></td><td>76.37 <b>(+257.76%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>285.60 (n/a)</td><td>262.62 (n/a)</td><td>252.90 (n/a)</td><td>240.60 (n/a)</td><td>21.35 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (-7.25%)</td><td>0.07 (-18.69%)</td><td>0.06 <b>(-34.66%)</b></td><td>0.05 (+3.65%)</td><td>0.02 <b>(-25.31%)</b></td><td>505.00 (-3.52%)</td><td>392.44 (+19.07%)</td><td>384.70 <b>(+53.08%)</b></td><td>269.30 (+7.81%)</td><td>100.32 (-16.79%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>523.40 (n/a)</td><td>329.58 (n/a)</td><td>251.30 (n/a)</td><td>249.80 (n/a)</td><td>120.56 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (-1.53%)</td><td>0.08 (-19.62%)</td><td>0.10 (-7.87%)</td><td>0.04 <b>(-48.14%)</b></td><td>0.03 <b>(+132.27%)</b></td><td>622.80 <b>(+92.82%)</b></td><td>364.64 <b>(+46.05%)</b></td><td>251.40 (+8.55%)</td><td>225.60 (+1.53%)</td><td>183.38 <b>(+332.48%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>323.00 (n/a)</td><td>249.66 (n/a)</td><td>231.60 (n/a)</td><td>222.20 (n/a)</td><td>42.40 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (-2.18%)</td><td>0.09 <b>(+26.65%)</b></td><td>0.10 (+13.70%)</td><td>0.08 <b>(+98.68%)</b></td><td>0.01 <b>(-71.28%)</b></td><td>296.20 <b>(-49.67%)</b></td><td>261.28 <b>(-30.41%)</b></td><td>250.70 (-12.07%)</td><td>241.70 (+2.24%)</td><td>23.07 <b>(-85.49%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>588.50 (n/a)</td><td>375.46 (n/a)</td><td>285.10 (n/a)</td><td>236.40 (n/a)</td><td>158.97 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (-15.89%)</td><td>0.06 (+5.79%)</td><td>0.06 <b>(+23.20%)</b></td><td>0.04 (+0.37%)</td><td>0.02 <b>(-25.13%)</b></td><td>640.40 (-0.37%)</td><td>428.48 (-10.10%)</td><td>441.20 (-18.82%)</td><td>294.70 (+18.88%)</td><td>142.27 (-17.81%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>642.80 (n/a)</td><td>476.60 (n/a)</td><td>543.50 (n/a)</td><td>247.90 (n/a)</td><td>173.09 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (+5.62%)</td><td>0.08 <b>(+26.56%)</b></td><td>0.08 <b>(+27.10%)</b></td><td>0.05 <b>(+219.10%)</b></td><td>0.03 <b>(-24.57%)</b></td><td>531.10 <b>(-68.66%)</b></td><td>346.56 <b>(-45.11%)</b></td><td>296.10 <b>(-21.33%)</b></td><td>231.20 (-5.32%)</td><td>126.32 <b>(-79.14%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1694.90 (n/a)</td><td>631.32 (n/a)</td><td>376.40 (n/a)</td><td>244.20 (n/a)</td><td>605.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.23 (+7.50%)</td><td>0.17 (+12.46%)</td><td>0.20 <b>(+41.85%)</b></td><td>0.09 (+4.84%)</td><td>0.06 (+12.39%)</td><td>549.40 (-4.62%)</td><td>345.36 (-9.23%)</td><td>246.00 <b>(-29.49%)</b></td><td>216.80 (-6.95%)</td><td>156.67 (+2.59%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>576.00 (n/a)</td><td>380.48 (n/a)</td><td>348.90 (n/a)</td><td>233.00 (n/a)</td><td>152.72 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.21 (-9.67%)</td><td>0.14 (-11.60%)</td><td>0.11 <b>(-32.87%)</b></td><td>0.09 (+1.39%)</td><td>0.05 <b>(-24.63%)</b></td><td>573.60 (-1.38%)</td><td>399.58 (+4.87%)</td><td>442.80 <b>(+48.99%)</b></td><td>230.60 (+10.71%)</td><td>133.43 <b>(-26.04%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>581.60 (n/a)</td><td>381.02 (n/a)</td><td>297.20 (n/a)</td><td>208.30 (n/a)</td><td>180.40 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.21 (+5.55%)</td><td>0.12 (-10.01%)</td><td>0.10 <b>(-36.32%)</b></td><td>0.03 (-1.24%)</td><td>0.08 (+10.14%)</td><td>1919.00 (+1.25%)</td><td>702.64 (+10.64%)</td><td>499.80 <b>(+57.07%)</b></td><td>233.50 (-5.24%)</td><td>698.95 (-1.52%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1895.30 (n/a)</td><td>635.04 (n/a)</td><td>318.20 (n/a)</td><td>246.40 (n/a)</td><td>709.72 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.20 (+10.94%)</td><td>0.15 <b>(+37.39%)</b></td><td>0.17 <b>(+72.34%)</b></td><td>0.09 (+16.24%)</td><td>0.05 <b>(+21.90%)</b></td><td>550.90 (-13.98%)</td><td>365.14 <b>(-25.90%)</b></td><td>289.30 <b>(-41.98%)</b></td><td>240.00 (-9.88%)</td><td>145.49 (-4.75%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>640.40 (n/a)</td><td>492.76 (n/a)</td><td>498.60 (n/a)</td><td>266.30 (n/a)</td><td>152.74 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 <b>(-34.49%)</b></td><td>0.11 (-8.78%)</td><td>0.10 (+7.65%)</td><td>0.08 (+4.50%)</td><td>0.02 <b>(-57.52%)</b></td><td>623.70 (-4.31%)</td><td>482.54 (-0.36%)</td><td>495.40 (-7.11%)</td><td>343.00 <b>(+52.65%)</b></td><td>106.16 <b>(-33.35%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>651.80 (n/a)</td><td>484.26 (n/a)</td><td>533.30 (n/a)</td><td>224.70 (n/a)</td><td>159.28 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.21 (+5.57%)</td><td>0.15 (+4.68%)</td><td>0.15 (+3.07%)</td><td>0.09 (-6.32%)</td><td>0.05 <b>(+28.69%)</b></td><td>570.90 (+6.75%)</td><td>359.86 (-0.72%)</td><td>327.50 (-2.96%)</td><td>237.50 (-5.27%)</td><td>137.74 <b>(+24.78%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>534.80 (n/a)</td><td>362.46 (n/a)</td><td>337.50 (n/a)</td><td>250.70 (n/a)</td><td>110.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (+12.90%)</td><td>0.01 <b>(+34.12%)</b></td><td>0.01 (+17.43%)</td><td>0.01 <b>(+78.14%)</b></td><td>0.00 <b>(-53.71%)</b></td><td>299.10 <b>(-43.86%)</b></td><td>265.40 <b>(-30.87%)</b></td><td>266.00 (-14.85%)</td><td>232.60 (-11.42%)</td><td>27.99 <b>(-78.12%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>532.80 (n/a)</td><td>383.94 (n/a)</td><td>312.40 (n/a)</td><td>262.60 (n/a)</td><td>127.93 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (-10.33%)</td><td>0.01 (-6.23%)</td><td>0.01 (-11.54%)</td><td>0.01 (+9.59%)</td><td>0.00 <b>(-26.04%)</b></td><td>419.80 (-8.76%)</td><td>342.60 (+3.43%)</td><td>351.00 (+13.04%)</td><td>238.00 (+11.53%)</td><td>70.78 <b>(-26.18%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>460.10 (n/a)</td><td>331.24 (n/a)</td><td>310.50 (n/a)</td><td>213.40 (n/a)</td><td>95.89 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 <b>(+22.67%)</b></td><td>0.01 (+6.28%)</td><td>0.01 (-19.98%)</td><td>0.00 (+8.64%)</td><td>0.00 <b>(+46.43%)</b></td><td>539.40 (-7.94%)</td><td>364.14 (-1.50%)</td><td>401.70 <b>(+24.95%)</b></td><td>198.70 (-18.47%)</td><td>140.36 (+4.19%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>585.90 (n/a)</td><td>369.68 (n/a)</td><td>321.50 (n/a)</td><td>243.70 (n/a)</td><td>134.71 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (+1.81%)</td><td>0.01 <b>(+23.00%)</b></td><td>0.01 <b>(+60.49%)</b></td><td>0.01 <b>(+24.60%)</b></td><td>0.00 (-12.91%)</td><td>519.50 (-19.73%)</td><td>332.14 <b>(-22.75%)</b></td><td>281.70 <b>(-37.69%)</b></td><td>241.80 (-1.79%)</td><td>118.03 <b>(-30.34%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>647.20 (n/a)</td><td>429.98 (n/a)</td><td>452.10 (n/a)</td><td>246.20 (n/a)</td><td>169.44 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (+1.53%)</td><td>0.01 (+13.12%)</td><td>0.01 <b>(+26.97%)</b></td><td>0.01 <b>(+32.83%)</b></td><td>0.00 (-17.17%)</td><td>463.70 <b>(-24.71%)</b></td><td>352.18 (-17.12%)</td><td>382.70 <b>(-21.24%)</b></td><td>234.30 (-1.51%)</td><td>102.68 <b>(-37.41%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>615.90 (n/a)</td><td>424.94 (n/a)</td><td>485.90 (n/a)</td><td>237.90 (n/a)</td><td>164.07 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 <b>(-28.54%)</b></td><td>0.01 (-15.31%)</td><td>0.01 (-4.89%)</td><td>0.00 (-18.47%)</td><td>0.00 <b>(-38.56%)</b></td><td>758.20 <b>(+22.65%)</b></td><td>524.62 (+15.51%)</td><td>506.30 (+5.13%)</td><td>375.00 <b>(+39.93%)</b></td><td>144.33 (+13.72%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>618.20 (n/a)</td><td>454.16 (n/a)</td><td>481.60 (n/a)</td><td>268.00 (n/a)</td><td>126.92 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (-8.80%)</td><td>0.01 <b>(-20.36%)</b></td><td>0.01 (-13.85%)</td><td>0.01 <b>(-25.27%)</b></td><td>0.01 (-13.40%)</td><td>630.80 <b>(+33.79%)</b></td><td>441.70 <b>(+26.37%)</b></td><td>432.70 (+16.07%)</td><td>245.60 (+9.64%)</td><td>147.26 <b>(+28.01%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>471.50 (n/a)</td><td>349.52 (n/a)</td><td>372.80 (n/a)</td><td>224.00 (n/a)</td><td>115.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+1.23%)</td><td>0.02 (+10.79%)</td><td>0.02 (+16.22%)</td><td>0.01 (+6.23%)</td><td>0.01 (-16.05%)</td><td>590.90 (-5.86%)</td><td>323.36 (-13.95%)</td><td>255.10 (-13.96%)</td><td>218.50 (-1.18%)</td><td>153.22 (-15.52%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.70 (n/a)</td><td>375.76 (n/a)</td><td>296.50 (n/a)</td><td>221.10 (n/a)</td><td>181.36 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (-11.58%)</td><td>0.01 <b>(-35.64%)</b></td><td>0.01 <b>(-43.53%)</b></td><td>0.01 <b>(-50.74%)</b></td><td>0.00 <b>(+73.30%)</b></td><td>580.70 <b>(+102.97%)</b></td><td>416.50 <b>(+67.59%)</b></td><td>412.20 <b>(+77.06%)</b></td><td>240.20 (+13.14%)</td><td>129.62 <b>(+278.63%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>286.10 (n/a)</td><td>248.52 (n/a)</td><td>232.80 (n/a)</td><td>212.30 (n/a)</td><td>34.23 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (-7.50%)</td><td>0.02 (-11.77%)</td><td>0.01 <b>(-24.09%)</b></td><td>0.01 <b>(+23.36%)</b></td><td>0.00 <b>(-29.68%)</b></td><td>489.40 (-18.95%)</td><td>370.70 (+5.27%)</td><td>378.00 <b>(+31.71%)</b></td><td>240.90 (+8.08%)</td><td>97.18 <b>(-38.52%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.80 (n/a)</td><td>352.14 (n/a)</td><td>287.00 (n/a)</td><td>222.90 (n/a)</td><td>158.06 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (-16.17%)</td><td>0.01 (-4.80%)</td><td>0.01 (-7.54%)</td><td>0.01 <b>(-21.64%)</b></td><td>0.01 (-2.75%)</td><td>674.50 <b>(+27.60%)</b></td><td>441.64 (+8.38%)</td><td>471.70 (+8.16%)</td><td>275.20 (+19.29%)</td><td>165.51 <b>(+43.53%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>528.60 (n/a)</td><td>407.50 (n/a)</td><td>436.10 (n/a)</td><td>230.70 (n/a)</td><td>115.32 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 <b>(-29.39%)</b></td><td>0.01 (-19.11%)</td><td>0.01 (-19.66%)</td><td>0.00 <b>(-45.05%)</b></td><td>0.00 <b>(-27.52%)</b></td><td>1857.20 <b>(+81.97%)</b></td><td>738.12 <b>(+37.40%)</b></td><td>491.60 <b>(+24.49%)</b></td><td>358.20 <b>(+41.64%)</b></td><td>628.43 <b>(+106.64%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1020.60 (n/a)</td><td>537.20 (n/a)</td><td>394.90 (n/a)</td><td>252.90 (n/a)</td><td>304.12 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (+16.35%)</td><td>0.04 (+13.65%)</td><td>0.04 <b>(+22.08%)</b></td><td>0.02 (-18.48%)</td><td>0.01 <b>(+56.53%)</b></td><td>518.20 <b>(+22.65%)</b></td><td>306.86 (-7.05%)</td><td>249.10 (-18.09%)</td><td>228.00 (-14.06%)</td><td>120.76 <b>(+72.19%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>422.50 (n/a)</td><td>330.12 (n/a)</td><td>304.10 (n/a)</td><td>265.30 (n/a)</td><td>70.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (+3.28%)</td><td>0.04 (+0.81%)</td><td>0.04 (+5.86%)</td><td>0.02 (-15.14%)</td><td>0.01 (+19.14%)</td><td>580.60 (+17.84%)</td><td>324.24 (+3.68%)</td><td>280.70 (-5.55%)</td><td>224.20 (-3.20%)</td><td>146.82 <b>(+39.02%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.70 (n/a)</td><td>312.72 (n/a)</td><td>297.20 (n/a)</td><td>231.60 (n/a)</td><td>105.61 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (-10.31%)</td><td>0.03 <b>(-24.12%)</b></td><td>0.03 (-10.99%)</td><td>0.01 <b>(-77.99%)</b></td><td>0.01 <b>(+81.48%)</b></td><td>1908.60 <b>(+354.21%)</b></td><td>638.72 <b>(+114.51%)</b></td><td>316.00 (+12.38%)</td><td>268.40 (+11.51%)</td><td>711.62 <b>(+885.63%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>420.20 (n/a)</td><td>297.76 (n/a)</td><td>281.20 (n/a)</td><td>240.70 (n/a)</td><td>72.20 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (-15.90%)</td><td>0.02 <b>(-21.04%)</b></td><td>0.02 (-15.87%)</td><td>0.01 <b>(-23.19%)</b></td><td>0.01 <b>(-31.02%)</b></td><td>810.50 <b>(+30.18%)</b></td><td>510.64 <b>(+21.09%)</b></td><td>495.60 (+18.88%)</td><td>280.40 (+18.91%)</td><td>198.55 (+8.57%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>622.60 (n/a)</td><td>421.72 (n/a)</td><td>416.90 (n/a)</td><td>235.80 (n/a)</td><td>182.88 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (-9.87%)</td><td>0.02 (-13.21%)</td><td>0.02 (-16.70%)</td><td>0.02 (+6.24%)</td><td>0.01 (-13.25%)</td><td>589.40 (-5.88%)</td><td>502.50 (+12.97%)</td><td>555.10 <b>(+20.05%)</b></td><td>269.80 (+10.98%)</td><td>132.48 (-10.22%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>626.20 (n/a)</td><td>444.82 (n/a)</td><td>462.40 (n/a)</td><td>243.10 (n/a)</td><td>147.55 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 <b>(+30.40%)</b></td><td>0.02 <b>(+24.11%)</b></td><td>0.02 <b>(+26.08%)</b></td><td>0.02 (+5.41%)</td><td>0.01 <b>(+64.67%)</b></td><td>630.60 (-5.13%)</td><td>450.94 (-17.05%)</td><td>437.50 <b>(-20.67%)</b></td><td>300.20 <b>(-23.32%)</b></td><td>121.56 <b>(+24.33%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>664.70 (n/a)</td><td>543.60 (n/a)</td><td>551.50 (n/a)</td><td>391.50 (n/a)</td><td>97.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (-1.96%)</td><td>0.06 (-1.07%)</td><td>0.05 <b>(-28.30%)</b></td><td>0.03 (+0.55%)</td><td>0.02 (+0.81%)</td><td>654.00 (-0.55%)</td><td>408.66 (-0.14%)</td><td>416.70 <b>(+39.46%)</b></td><td>246.40 (+2.03%)</td><td>169.19 (-7.94%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>657.60 (n/a)</td><td>409.24 (n/a)</td><td>298.80 (n/a)</td><td>241.50 (n/a)</td><td>183.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (+11.84%)</td><td>0.06 (-4.75%)</td><td>0.05 <b>(-45.86%)</b></td><td>0.04 <b>(+99.68%)</b></td><td>0.03 (-8.84%)</td><td>538.80 <b>(-49.93%)</b></td><td>391.68 (-13.04%)</td><td>452.60 <b>(+84.73%)</b></td><td>206.70 (-10.60%)</td><td>154.31 <b>(-57.40%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1076.00 (n/a)</td><td>450.40 (n/a)</td><td>245.00 (n/a)</td><td>231.20 (n/a)</td><td>362.18 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (+5.24%)</td><td>0.08 <b>(+47.57%)</b></td><td>0.08 <b>(+79.22%)</b></td><td>0.08 <b>(+120.54%)</b></td><td>0.01 <b>(-75.24%)</b></td><td>274.50 <b>(-54.66%)</b></td><td>260.94 <b>(-40.79%)</b></td><td>273.80 <b>(-44.20%)</b></td><td>237.50 (-4.96%)</td><td>18.21 <b>(-89.18%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>605.40 (n/a)</td><td>440.72 (n/a)</td><td>490.70 (n/a)</td><td>249.90 (n/a)</td><td>168.27 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 <b>(+25.88%)</b></td><td>0.08 (+0.76%)</td><td>0.08 (-2.58%)</td><td>0.04 <b>(-30.13%)</b></td><td>0.03 <b>(+82.75%)</b></td><td>564.10 <b>(+43.14%)</b></td><td>321.14 (+9.96%)</td><td>266.50 (+2.66%)</td><td>184.20 <b>(-20.57%)</b></td><td>148.21 <b>(+116.28%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>394.10 (n/a)</td><td>292.06 (n/a)</td><td>259.60 (n/a)</td><td>231.90 (n/a)</td><td>68.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (+11.43%)</td><td>0.07 (+7.51%)</td><td>0.08 (+16.27%)</td><td>0.04 (+4.51%)</td><td>0.03 (+7.48%)</td><td>593.60 (-4.32%)</td><td>378.48 (-6.73%)</td><td>275.50 (-13.99%)</td><td>218.70 (-10.22%)</td><td>175.26 (-5.12%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>620.40 (n/a)</td><td>405.78 (n/a)</td><td>320.30 (n/a)</td><td>243.60 (n/a)</td><td>184.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (+15.58%)</td><td>0.05 (-4.86%)</td><td>0.05 (-0.99%)</td><td>0.03 (-6.68%)</td><td>0.02 <b>(+52.99%)</b></td><td>648.60 (+7.17%)</td><td>456.40 (+11.15%)</td><td>385.40 (+1.00%)</td><td>264.20 (-13.49%)</td><td>162.45 <b>(+41.63%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>605.20 (n/a)</td><td>410.60 (n/a)</td><td>381.60 (n/a)</td><td>305.40 (n/a)</td><td>114.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.70 (n/a)</td><td>314.06 (n/a)</td><td>254.50 (n/a)</td><td>198.10 (n/a)</td><td>169.76 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.00 (n/a)</td><td>424.10 (n/a)</td><td>524.20 (n/a)</td><td>218.10 (n/a)</td><td>181.27 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.70 (n/a)</td><td>447.10 (n/a)</td><td>512.00 (n/a)</td><td>232.40 (n/a)</td><td>174.31 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>432.60 (n/a)</td><td>392.88 (n/a)</td><td>404.90 (n/a)</td><td>347.70 (n/a)</td><td>40.94 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>477.50 (n/a)</td><td>346.20 (n/a)</td><td>291.40 (n/a)</td><td>241.90 (n/a)</td><td>121.38 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>627.80 (n/a)</td><td>378.52 (n/a)</td><td>294.10 (n/a)</td><td>209.60 (n/a)</td><td>171.72 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>542.00 (n/a)</td><td>340.32 (n/a)</td><td>307.50 (n/a)</td><td>244.00 (n/a)</td><td>115.91 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1079.90 (n/a)</td><td>472.90 (n/a)</td><td>300.80 (n/a)</td><td>273.00 (n/a)</td><td>343.82 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>450.80 (n/a)</td><td>355.42 (n/a)</td><td>311.80 (n/a)</td><td>274.60 (n/a)</td><td>85.25 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.23 (+18.54%)</td><td>0.19 <b>(+34.86%)</b></td><td>0.20 (+17.46%)</td><td>0.16 <b>(+88.47%)</b></td><td>0.03 <b>(-50.78%)</b></td><td>304.10 <b>(-46.94%)</b></td><td>257.12 <b>(-33.46%)</b></td><td>248.40 (-14.87%)</td><td>213.70 (-15.63%)</td><td>33.39 <b>(-78.60%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>573.10 (n/a)</td><td>386.42 (n/a)</td><td>291.80 (n/a)</td><td>253.30 (n/a)</td><td>156.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>576.00 (n/a)</td><td>324.44 (n/a)</td><td>267.40 (n/a)</td><td>219.20 (n/a)</td><td>147.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>615.30 (n/a)</td><td>401.18 (n/a)</td><td>351.90 (n/a)</td><td>275.30 (n/a)</td><td>146.29 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>528.00 (n/a)</td><td>335.40 (n/a)</td><td>275.30 (n/a)</td><td>251.20 (n/a)</td><td>115.43 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1987.40 (n/a)</td><td>709.18 (n/a)</td><td>423.70 (n/a)</td><td>226.80 (n/a)</td><td>729.40 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.00 (n/a)</td><td>432.22 (n/a)</td><td>471.40 (n/a)</td><td>265.20 (n/a)</td><td>123.42 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>592.80 (n/a)</td><td>442.66 (n/a)</td><td>506.40 (n/a)</td><td>226.20 (n/a)</td><td>171.03 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>516.10 (n/a)</td><td>393.32 (n/a)</td><td>489.40 (n/a)</td><td>214.50 (n/a)</td><td>153.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1970.30 (n/a)</td><td>768.48 (n/a)</td><td>538.00 (n/a)</td><td>280.80 (n/a)</td><td>681.26 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>483.30 (n/a)</td><td>389.30 (n/a)</td><td>422.00 (n/a)</td><td>261.50 (n/a)</td><td>90.64 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>614.10 (n/a)</td><td>488.32 (n/a)</td><td>524.90 (n/a)</td><td>256.70 (n/a)</td><td>137.62 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>510.20 (n/a)</td><td>428.54 (n/a)</td><td>455.50 (n/a)</td><td>296.00 (n/a)</td><td>91.96 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>568.30 (n/a)</td><td>345.88 (n/a)</td><td>287.70 (n/a)</td><td>242.00 (n/a)</td><td>135.89 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>623.10 (n/a)</td><td>500.64 (n/a)</td><td>532.80 (n/a)</td><td>247.20 (n/a)</td><td>150.42 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>444.80 (n/a)</td><td>371.28 (n/a)</td><td>404.60 (n/a)</td><td>270.00 (n/a)</td><td>81.83 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.80 (n/a)</td><td>441.50 (n/a)</td><td>528.90 (n/a)</td><td>241.80 (n/a)</td><td>168.05 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>479.50 (n/a)</td><td>365.90 (n/a)</td><td>403.80 (n/a)</td><td>254.10 (n/a)</td><td>95.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.00 (n/a)</td><td>390.66 (n/a)</td><td>413.00 (n/a)</td><td>239.20 (n/a)</td><td>109.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>535.10 (n/a)</td><td>398.12 (n/a)</td><td>459.10 (n/a)</td><td>222.70 (n/a)</td><td>145.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2380.80 (n/a)</td><td>859.82 (n/a)</td><td>534.10 (n/a)</td><td>380.30 (n/a)</td><td>854.83 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.00 (n/a)</td><td>378.06 (n/a)</td><td>281.20 (n/a)</td><td>252.50 (n/a)</td><td>161.10 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1383.50 (n/a)</td><td>659.80 (n/a)</td><td>517.30 (n/a)</td><td>379.50 (n/a)</td><td>410.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.10 (n/a)</td><td>351.74 (n/a)</td><td>328.90 (n/a)</td><td>244.10 (n/a)</td><td>105.07 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.30 (n/a)</td><td>412.66 (n/a)</td><td>417.70 (n/a)</td><td>234.20 (n/a)</td><td>141.06 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.00 (n/a)</td><td>378.02 (n/a)</td><td>394.40 (n/a)</td><td>230.30 (n/a)</td><td>126.59 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.50 (n/a)</td><td>484.48 (n/a)</td><td>481.10 (n/a)</td><td>369.20 (n/a)</td><td>98.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>537.30 (n/a)</td><td>364.92 (n/a)</td><td>271.50 (n/a)</td><td>231.10 (n/a)</td><td>149.69 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>510.40 (n/a)</td><td>311.30 (n/a)</td><td>263.70 (n/a)</td><td>250.00 (n/a)</td><td>112.02 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>586.30 (n/a)</td><td>404.50 (n/a)</td><td>452.00 (n/a)</td><td>234.40 (n/a)</td><td>153.94 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1914.30 (n/a)</td><td>710.56 (n/a)</td><td>507.20 (n/a)</td><td>242.90 (n/a)</td><td>688.03 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1070.60 (n/a)</td><td>574.64 (n/a)</td><td>533.60 (n/a)</td><td>226.40 (n/a)</td><td>308.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>610.90 (n/a)</td><td>472.64 (n/a)</td><td>495.20 (n/a)</td><td>273.20 (n/a)</td><td>139.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1996.40 (n/a)</td><td>776.12 (n/a)</td><td>543.10 (n/a)</td><td>289.00 (n/a)</td><td>690.98 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>675.30 (n/a)</td><td>355.34 (n/a)</td><td>289.00 (n/a)</td><td>251.90 (n/a)</td><td>179.71 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>592.50 (n/a)</td><td>389.94 (n/a)</td><td>295.70 (n/a)</td><td>263.40 (n/a)</td><td>160.21 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>552.00 (n/a)</td><td>362.52 (n/a)</td><td>295.40 (n/a)</td><td>284.70 (n/a)</td><td>113.75 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>565.60 (n/a)</td><td>464.38 (n/a)</td><td>480.20 (n/a)</td><td>321.60 (n/a)</td><td>104.01 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.35 <b>(-38.87%)</b></td><td>0.24 <b>(-50.83%)</b></td><td>0.25 <b>(-49.04%)</b></td><td>0.09 <b>(-79.40%)</b></td><td>0.11 <b>(+95.83%)</b></td><td>2472.20 <b>(+385.60%)</b></td><td>1185.06 <b>(+158.78%)</b></td><td>901.70 <b>(+96.24%)</b></td><td>624.50 <b>(+63.61%)</b></td><td>764.17 <b>(+1446.47%)</b></td><td>15.11 <b>(-38.87%)</b></td><td>10.23 <b>(-50.83%)</b></td><td>10.47 <b>(-49.04%)</b></td><td>3.82 <b>(-79.40%)</b></td><td>4.74 <b>(+95.83%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.58 (n/a)</td><td>0.49 (n/a)</td><td>0.48 (n/a)</td><td>0.43 (n/a)</td><td>0.06 (n/a)</td><td>509.10 (n/a)</td><td>457.94 (n/a)</td><td>459.50 (n/a)</td><td>381.70 (n/a)</td><td>49.41 (n/a)</td><td>24.72 (n/a)</td><td>20.81 (n/a)</td><td>20.54 (n/a)</td><td>18.54 (n/a)</td><td>2.42 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.51 (-14.15%)</td><td>0.43 (+7.01%)</td><td>0.47 (+9.09%)</td><td>0.26 <b>(+123.55%)</b></td><td>0.10 <b>(-43.99%)</b></td><td>857.70 <b>(-55.27%)</b></td><td>543.12 <b>(-28.92%)</b></td><td>472.70 (-8.32%)</td><td>437.20 (+16.49%)</td><td>177.30 <b>(-72.69%)</b></td><td>21.58 (-14.15%)</td><td>18.49 (+7.01%)</td><td>19.97 (+9.09%)</td><td>11.00 <b>(+123.55%)</b></td><td>4.30 <b>(-43.99%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.59 (n/a)</td><td>0.41 (n/a)</td><td>0.43 (n/a)</td><td>0.12 (n/a)</td><td>0.18 (n/a)</td><td>1917.40 (n/a)</td><td>764.06 (n/a)</td><td>515.60 (n/a)</td><td>375.30 (n/a)</td><td>649.28 (n/a)</td><td>25.14 (n/a)</td><td>17.28 (n/a)</td><td>18.30 (n/a)</td><td>4.92 (n/a)</td><td>7.68 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.31 (+0.14%)</td><td>0.31 (+2.29%)</td><td>0.31 (+3.31%)</td><td>0.31 (+3.43%)</td><td>0.00 <b>(-56.73%)</b></td><td>81921.90 (-3.31%)</td><td>81147.00 (-2.26%)</td><td>80762.80 (-3.20%)</td><td>80569.30 (-0.14%)</td><td>626.87 <b>(-58.09%)</b></td><td>213.23 (+0.14%)</td><td>211.72 (+2.29%)</td><td>212.72 (+3.31%)</td><td>209.71 (+3.43%)</td><td>1.63 <b>(-56.73%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84728.40 (n/a)</td><td>83025.82 (n/a)</td><td>83436.20 (n/a)</td><td>80683.90 (n/a)</td><td>1495.76 (n/a)</td><td>212.93 (n/a)</td><td>206.98 (n/a)</td><td>205.90 (n/a)</td><td>202.76 (n/a)</td><td>3.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>1.03 (+0.25%)</td><td>1.01 (+0.77%)</td><td>1.01 (+0.92%)</td><td>0.98 (+0.90%)</td><td>0.02 (+10.79%)</td><td>25677.50 (-0.89%)</td><td>24927.90 (-0.76%)</td><td>24795.60 (-0.91%)</td><td>24347.50 (-0.25%)</td><td>611.98 (+9.24%)</td><td>705.61 (+0.25%)</td><td>689.51 (+0.77%)</td><td>692.86 (+0.92%)</td><td>669.06 (+0.90%)</td><td>16.85 (+10.79%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>1.01 (n/a)</td><td>0.97 (n/a)</td><td>0.02 (n/a)</td><td>25907.80 (n/a)</td><td>25118.26 (n/a)</td><td>25024.50 (n/a)</td><td>24408.20 (n/a)</td><td>560.21 (n/a)</td><td>703.86 (n/a)</td><td>684.23 (n/a)</td><td>686.52 (n/a)</td><td>663.12 (n/a)</td><td>15.20 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.81 (-0.21%)</td><td>0.79 (-0.71%)</td><td>0.80 (-1.33%)</td><td>0.78 (-0.19%)</td><td>0.02 (-8.61%)</td><td>97395.20 (+0.19%)</td><td>94996.36 (+0.71%)</td><td>94426.70 (+1.35%)</td><td>92831.80 (+0.21%)</td><td>1849.98 (-8.01%)</td><td>740.26 (-0.21%)</td><td>723.61 (-0.71%)</td><td>727.75 (-1.33%)</td><td>705.57 (-0.19%)</td><td>14.04 (-8.61%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.78 (n/a)</td><td>0.02 (n/a)</td><td>97213.40 (n/a)</td><td>94325.52 (n/a)</td><td>93170.40 (n/a)</td><td>92640.90 (n/a)</td><td>2011.13 (n/a)</td><td>741.78 (n/a)</td><td>728.80 (n/a)</td><td>737.57 (n/a)</td><td>706.89 (n/a)</td><td>15.37 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.78 (+0.13%)</td><td>0.77 (-0.00%)</td><td>0.77 (-0.23%)</td><td>0.75 (-0.19%)</td><td>0.01 (+3.08%)</td><td>100159.40 (+0.19%)</td><td>98387.06 (+0.01%)</td><td>98468.10 (+0.23%)</td><td>97105.20 (-0.13%)</td><td>1237.50 (+3.19%)</td><td>707.68 (+0.13%)</td><td>698.55 (-0.00%)</td><td>697.89 (-0.23%)</td><td>686.10 (-0.19%)</td><td>8.75 (+3.08%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99968.20 (n/a)</td><td>98382.02 (n/a)</td><td>98237.40 (n/a)</td><td>97230.00 (n/a)</td><td>1199.25 (n/a)</td><td>706.77 (n/a)</td><td>698.58 (n/a)</td><td>699.52 (n/a)</td><td>687.41 (n/a)</td><td>8.49 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.80 (-0.70%)</td><td>0.79 (-0.77%)</td><td>0.79 (-1.41%)</td><td>0.78 (-0.67%)</td><td>0.01 (+2.40%)</td><td>96573.20 (+0.68%)</td><td>95545.90 (+0.78%)</td><td>95896.30 (+1.43%)</td><td>94417.90 (+0.71%)</td><td>905.73 (+3.66%)</td><td>727.82 (-0.70%)</td><td>719.28 (-0.77%)</td><td>716.60 (-1.41%)</td><td>711.58 (-0.67%)</td><td>6.83 (+2.40%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95925.50 (n/a)</td><td>94808.20 (n/a)</td><td>94545.70 (n/a)</td><td>93752.70 (n/a)</td><td>873.75 (n/a)</td><td>732.99 (n/a)</td><td>724.88 (n/a)</td><td>726.84 (n/a)</td><td>716.38 (n/a)</td><td>6.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.44 (+9.22%)</td><td>4.35 <b>(+32.45%)</b></td><td>4.41 <b>(+63.02%)</b></td><td>2.81 <b>(+29.65%)</b></td><td>1.12 (-5.68%)</td><td>3169.90 <b>(-22.87%)</b></td><td>2175.38 <b>(-27.10%)</b></td><td>2019.60 <b>(-38.66%)</b></td><td>1639.40 (-8.44%)</td><td>635.86 <b>(-33.97%)</b></td><td>327.48 (+9.22%)</td><td>262.26 <b>(+32.45%)</b></td><td>265.83 <b>(+63.02%)</b></td><td>169.37 <b>(+29.65%)</b></td><td>67.38 (-5.68%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>4.98 (n/a)</td><td>3.29 (n/a)</td><td>2.71 (n/a)</td><td>2.17 (n/a)</td><td>1.19 (n/a)</td><td>4109.70 (n/a)</td><td>2984.06 (n/a)</td><td>3292.30 (n/a)</td><td>1790.60 (n/a)</td><td>963.00 (n/a)</td><td>299.83 (n/a)</td><td>198.02 (n/a)</td><td>163.07 (n/a)</td><td>130.64 (n/a)</td><td>71.44 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.90 (-16.68%)</td><td>2.69 (-8.82%)</td><td>2.64 (-5.39%)</td><td>2.07 (+1.30%)</td><td>0.73 <b>(-29.79%)</b></td><td>4307.30 (-1.28%)</td><td>3479.94 (+6.16%)</td><td>3381.40 (+5.70%)</td><td>2283.90 <b>(+20.02%)</b></td><td>806.23 (-15.73%)</td><td>235.06 (-16.68%)</td><td>162.30 (-8.82%)</td><td>158.77 (-5.39%)</td><td>124.64 (+1.30%)</td><td>44.14 <b>(-29.79%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>4.68 (n/a)</td><td>2.95 (n/a)</td><td>2.79 (n/a)</td><td>2.04 (n/a)</td><td>1.04 (n/a)</td><td>4363.20 (n/a)</td><td>3277.98 (n/a)</td><td>3199.10 (n/a)</td><td>1903.00 (n/a)</td><td>956.74 (n/a)</td><td>282.11 (n/a)</td><td>177.99 (n/a)</td><td>167.82 (n/a)</td><td>123.05 (n/a)</td><td>62.87 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.26 (-5.00%)</td><td>3.11 <b>(-25.83%)</b></td><td>2.22 <b>(-45.79%)</b></td><td>1.92 <b>(-31.37%)</b></td><td>1.45 <b>(+33.82%)</b></td><td>4641.00 <b>(+45.71%)</b></td><td>3344.06 <b>(+48.26%)</b></td><td>4008.90 <b>(+84.45%)</b></td><td>1696.00 (+5.26%)</td><td>1291.04 <b>(+107.09%)</b></td><td>316.54 (-5.00%)</td><td>187.07 <b>(-25.83%)</b></td><td>133.92 <b>(-45.79%)</b></td><td>115.68 <b>(-31.37%)</b></td><td>87.55 <b>(+33.82%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>5.53 (n/a)</td><td>4.19 (n/a)</td><td>4.10 (n/a)</td><td>2.80 (n/a)</td><td>1.09 (n/a)</td><td>3185.10 (n/a)</td><td>2255.48 (n/a)</td><td>2173.40 (n/a)</td><td>1611.20 (n/a)</td><td>623.41 (n/a)</td><td>333.21 (n/a)</td><td>252.20 (n/a)</td><td>247.02 (n/a)</td><td>168.56 (n/a)</td><td>65.43 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>6.72 (+17.25%)</td><td>5.50 (+10.56%)</td><td>5.11 (+3.15%)</td><td>4.29 (+1.19%)</td><td>1.16 <b>(+92.80%)</b></td><td>8122.70 (-1.18%)</td><td>6567.02 (-7.44%)</td><td>6822.10 (-3.05%)</td><td>5185.50 (-14.71%)</td><td>1342.33 <b>(+56.16%)</b></td><td>414.13 (+17.25%)</td><td>338.60 (+10.56%)</td><td>314.78 (+3.14%)</td><td>264.38 (+1.19%)</td><td>71.22 <b>(+92.80%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>5.73 (n/a)</td><td>4.97 (n/a)</td><td>4.95 (n/a)</td><td>4.24 (n/a)</td><td>0.60 (n/a)</td><td>8219.30 (n/a)</td><td>7094.72 (n/a)</td><td>7036.60 (n/a)</td><td>6079.80 (n/a)</td><td>859.58 (n/a)</td><td>353.22 (n/a)</td><td>306.25 (n/a)</td><td>305.19 (n/a)</td><td>261.27 (n/a)</td><td>36.94 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.89 (-2.98%)</td><td>4.90 (-5.45%)</td><td>4.80 (-1.47%)</td><td>4.26 (-5.66%)</td><td>0.68 (-2.03%)</td><td>8182.80 (+6.00%)</td><td>7216.30 (+5.87%)</td><td>7268.90 (+1.49%)</td><td>5921.90 (+3.08%)</td><td>963.68 (+9.28%)</td><td>362.64 (-2.98%)</td><td>302.07 (-5.45%)</td><td>295.44 (-1.47%)</td><td>262.44 (-5.66%)</td><td>42.12 (-2.03%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.07 (n/a)</td><td>5.19 (n/a)</td><td>4.87 (n/a)</td><td>4.52 (n/a)</td><td>0.70 (n/a)</td><td>7719.90 (n/a)</td><td>6816.42 (n/a)</td><td>7162.10 (n/a)</td><td>5745.20 (n/a)</td><td>881.88 (n/a)</td><td>373.79 (n/a)</td><td>319.49 (n/a)</td><td>299.84 (n/a)</td><td>278.17 (n/a)</td><td>42.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.48 (-15.56%)</td><td>4.72 (-13.20%)</td><td>4.82 (-12.14%)</td><td>3.93 (-3.32%)</td><td>0.62 <b>(-32.16%)</b></td><td>8871.60 (+3.43%)</td><td>7486.36 (+13.94%)</td><td>7232.30 (+13.82%)</td><td>6366.30 (+18.43%)</td><td>1016.97 (-17.88%)</td><td>337.32 (-15.56%)</td><td>291.02 (-13.20%)</td><td>296.93 (-12.14%)</td><td>242.06 (-3.32%)</td><td>38.49 <b>(-32.16%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.49 (n/a)</td><td>5.44 (n/a)</td><td>5.49 (n/a)</td><td>4.06 (n/a)</td><td>0.92 (n/a)</td><td>8577.30 (n/a)</td><td>6570.66 (n/a)</td><td>6354.00 (n/a)</td><td>5375.80 (n/a)</td><td>1238.36 (n/a)</td><td>399.47 (n/a)</td><td>335.29 (n/a)</td><td>337.97 (n/a)</td><td>250.37 (n/a)</td><td>56.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.78 (+1.29%)</td><td>0.76 (+0.37%)</td><td>0.75 (-0.48%)</td><td>0.74 (+0.70%)</td><td>0.02 (+8.36%)</td><td>101350.80 (-0.70%)</td><td>99825.72 (-0.36%)</td><td>100682.60 (+0.48%)</td><td>96479.50 (-1.28%)</td><td>2022.02 (+5.84%)</td><td>712.27 (+1.29%)</td><td>688.62 (+0.37%)</td><td>682.54 (-0.48%)</td><td>678.04 (+0.70%)</td><td>14.22 (+8.36%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>102063.90 (n/a)</td><td>100186.96 (n/a)</td><td>100198.50 (n/a)</td><td>97725.90 (n/a)</td><td>1910.42 (n/a)</td><td>703.19 (n/a)</td><td>686.11 (n/a)</td><td>685.83 (n/a)</td><td>673.30 (n/a)</td><td>13.12 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.78 (-1.18%)</td><td>0.76 (-0.32%)</td><td>0.76 (-0.08%)</td><td>0.74 (-0.82%)</td><td>0.01 (-13.13%)</td><td>101586.30 (+0.83%)</td><td>99271.92 (+0.32%)</td><td>99111.20 (+0.09%)</td><td>97395.50 (+1.19%)</td><td>1502.27 (-10.96%)</td><td>705.57 (-1.18%)</td><td>692.36 (-0.32%)</td><td>693.36 (-0.09%)</td><td>676.46 (-0.82%)</td><td>10.41 (-13.13%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100755.00 (n/a)</td><td>98959.82 (n/a)</td><td>99027.00 (n/a)</td><td>96247.70 (n/a)</td><td>1687.13 (n/a)</td><td>713.99 (n/a)</td><td>694.58 (n/a)</td><td>693.95 (n/a)</td><td>682.04 (n/a)</td><td>11.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.80 (-1.02%)</td><td>0.79 (-0.76%)</td><td>0.79 (-0.84%)</td><td>0.78 (-0.52%)</td><td>0.01 (-18.24%)</td><td>96189.00 (+0.53%)</td><td>95123.36 (+0.76%)</td><td>95141.10 (+0.85%)</td><td>94360.80 (+1.03%)</td><td>682.32 (-17.00%)</td><td>728.26 (-1.02%)</td><td>722.45 (-0.76%)</td><td>722.29 (-0.84%)</td><td>714.42 (-0.52%)</td><td>5.16 (-18.24%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95685.10 (n/a)</td><td>94404.16 (n/a)</td><td>94341.80 (n/a)</td><td>93395.50 (n/a)</td><td>822.03 (n/a)</td><td>735.79 (n/a)</td><td>727.97 (n/a)</td><td>728.41 (n/a)</td><td>718.18 (n/a)</td><td>6.31 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.43 (+2.15%)</td><td>2.00 <b>(-30.78%)</b></td><td>1.79 <b>(-45.71%)</b></td><td>1.10 <b>(-50.84%)</b></td><td>0.86 <b>(+45.61%)</b></td><td>7306.10 <b>(+103.42%)</b></td><td>4581.94 <b>(+58.64%)</b></td><td>4494.00 <b>(+84.20%)</b></td><td>2347.80 (-2.11%)</td><td>1775.45 <b>(+178.54%)</b></td><td>900.40 (+2.15%)</td><td>525.58 <b>(-30.78%)</b></td><td>470.39 <b>(-45.71%)</b></td><td>289.34 <b>(-50.84%)</b></td><td>225.91 <b>(+45.61%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.36 (n/a)</td><td>2.90 (n/a)</td><td>3.30 (n/a)</td><td>2.24 (n/a)</td><td>0.59 (n/a)</td><td>3591.70 (n/a)</td><td>2888.32 (n/a)</td><td>2439.70 (n/a)</td><td>2398.30 (n/a)</td><td>637.41 (n/a)</td><td>881.42 (n/a)</td><td>759.28 (n/a)</td><td>866.47 (n/a)</td><td>588.56 (n/a)</td><td>155.14 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.28 (-7.67%)</td><td>0.20 (-14.03%)</td><td>0.20 (-12.96%)</td><td>0.16 (-10.81%)</td><td>0.05 (-19.48%)</td><td>7946.90 (+12.12%)</td><td>6330.52 (+15.01%)</td><td>6366.40 (+14.89%)</td><td>4408.90 (+8.31%)</td><td>1266.06 (-4.60%)</td><td>15.22 (-7.67%)</td><td>11.00 (-14.03%)</td><td>10.54 (-12.96%)</td><td>8.44 (-10.81%)</td><td>2.52 (-19.48%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>7088.00 (n/a)</td><td>5504.50 (n/a)</td><td>5541.20 (n/a)</td><td>4070.80 (n/a)</td><td>1327.14 (n/a)</td><td>16.49 (n/a)</td><td>12.79 (n/a)</td><td>12.11 (n/a)</td><td>9.47 (n/a)</td><td>3.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.80 (n/a)</td><td>3.50 (n/a)</td><td>3.40 (n/a)</td><td>3.21 (n/a)</td><td>0.24 (n/a)</td><td>3.80 (n/a)</td><td>3.50 (n/a)</td><td>3.40 (n/a)</td><td>3.21 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>7.18 (-5.45%)</td><td>6.19 (+2.91%)</td><td>5.99 (+5.82%)</td><td>5.24 (-3.53%)</td><td>0.81 (-10.19%)</td><td>7.18 (-5.45%)</td><td>6.18 (+2.91%)</td><td>5.99 (+5.82%)</td><td>5.24 (-3.53%)</td><td>0.81 (-10.19%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>7.60 (n/a)</td><td>6.01 (n/a)</td><td>5.66 (n/a)</td><td>5.44 (n/a)</td><td>0.90 (n/a)</td><td>7.59 (n/a)</td><td>6.01 (n/a)</td><td>5.66 (n/a)</td><td>5.43 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>13.97 (+18.06%)</td><td>9.75 (+7.57%)</td><td>8.59 (+1.75%)</td><td>8.11 (+17.37%)</td><td>2.42 <b>(+28.06%)</b></td><td>13.96 (+18.06%)</td><td>9.75 (+7.57%)</td><td>8.58 (+1.75%)</td><td>8.11 (+17.37%)</td><td>2.42 <b>(+28.06%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>11.83 (n/a)</td><td>9.07 (n/a)</td><td>8.44 (n/a)</td><td>6.91 (n/a)</td><td>1.89 (n/a)</td><td>11.82 (n/a)</td><td>9.06 (n/a)</td><td>8.43 (n/a)</td><td>6.91 (n/a)</td><td>1.89 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.95 (n/a)</td><td>3.56 (n/a)</td><td>3.58 (n/a)</td><td>3.04 (n/a)</td><td>0.34 (n/a)</td><td>3.95 (n/a)</td><td>3.56 (n/a)</td><td>3.58 (n/a)</td><td>3.04 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>7.00 (+6.28%)</td><td>6.39 (+6.20%)</td><td>6.42 (+6.66%)</td><td>5.91 (+7.05%)</td><td>0.43 (+12.61%)</td><td>7.00 (+6.28%)</td><td>6.39 (+6.20%)</td><td>6.42 (+6.66%)</td><td>5.91 (+7.05%)</td><td>0.43 (+12.61%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.59 (n/a)</td><td>6.02 (n/a)</td><td>6.02 (n/a)</td><td>5.52 (n/a)</td><td>0.38 (n/a)</td><td>6.59 (n/a)</td><td>6.01 (n/a)</td><td>6.02 (n/a)</td><td>5.52 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>12.88 (-7.19%)</td><td>9.14 (-14.27%)</td><td>8.15 (-16.47%)</td><td>7.33 (-10.24%)</td><td>2.32 (-12.96%)</td><td>12.87 (-7.19%)</td><td>9.14 (-14.27%)</td><td>8.15 (-16.47%)</td><td>7.33 (-10.24%)</td><td>2.32 (-12.96%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>13.88 (n/a)</td><td>10.66 (n/a)</td><td>9.76 (n/a)</td><td>8.17 (n/a)</td><td>2.67 (n/a)</td><td>13.87 (n/a)</td><td>10.66 (n/a)</td><td>9.76 (n/a)</td><td>8.16 (n/a)</td><td>2.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.08 (+1.84%)</td><td>2.00 (+15.32%)</td><td>1.71 (+0.66%)</td><td>1.03 (-1.75%)</td><td>0.97 <b>(+21.47%)</b></td><td>3.07 (+1.84%)</td><td>1.99 (+15.32%)</td><td>1.71 (+0.66%)</td><td>1.03 (-1.75%)</td><td>0.96 <b>(+21.47%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.03 (n/a)</td><td>1.73 (n/a)</td><td>1.70 (n/a)</td><td>1.05 (n/a)</td><td>0.79 (n/a)</td><td>3.02 (n/a)</td><td>1.73 (n/a)</td><td>1.70 (n/a)</td><td>1.04 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.42 (-7.33%)</td><td>0.31 (-14.51%)</td><td>0.35 (-19.68%)</td><td>0.12 <b>(-46.14%)</b></td><td>0.11 (+9.36%)</td><td>0.41 (-7.33%)</td><td>0.31 (-14.51%)</td><td>0.34 (-19.68%)</td><td>0.12 <b>(-46.14%)</b></td><td>0.11 (+9.36%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.45 (n/a)</td><td>0.37 (n/a)</td><td>0.43 (n/a)</td><td>0.23 (n/a)</td><td>0.10 (n/a)</td><td>0.44 (n/a)</td><td>0.36 (n/a)</td><td>0.43 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.73 <b>(+45.97%)</b></td><td>0.49 <b>(+68.76%)</b></td><td>0.61 <b>(+84.84%)</b></td><td>0.14 <b>(+78.25%)</b></td><td>0.26 <b>(+32.19%)</b></td><td>0.72 <b>(+45.97%)</b></td><td>0.48 <b>(+68.76%)</b></td><td>0.61 <b>(+84.84%)</b></td><td>0.14 <b>(+78.25%)</b></td><td>0.26 <b>(+32.19%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.50 (n/a)</td><td>0.29 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.49 (n/a)</td><td>0.29 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>2.56 (+5.02%)</td><td>1.13 <b>(-24.73%)</b></td><td>0.47 <b>(-74.18%)</b></td><td>0.45 (+5.19%)</td><td>0.96 (-3.97%)</td><td>2.52 (+5.02%)</td><td>1.11 <b>(-24.73%)</b></td><td>0.46 <b>(-74.18%)</b></td><td>0.44 (+5.19%)</td><td>0.95 (-3.97%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>2.44 (n/a)</td><td>1.50 (n/a)</td><td>1.83 (n/a)</td><td>0.43 (n/a)</td><td>1.00 (n/a)</td><td>2.40 (n/a)</td><td>1.48 (n/a)</td><td>1.80 (n/a)</td><td>0.42 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.90 (n/a)</td><td>372.52 (n/a)</td><td>295.50 (n/a)</td><td>263.40 (n/a)</td><td>130.21 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.10 (n/a)</td><td>385.34 (n/a)</td><td>428.80 (n/a)</td><td>267.50 (n/a)</td><td>108.19 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.10 (n/a)</td><td>386.96 (n/a)</td><td>373.80 (n/a)</td><td>294.50 (n/a)</td><td>94.00 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2023.20 (n/a)</td><td>857.40 (n/a)</td><td>600.70 (n/a)</td><td>493.40 (n/a)</td><td>653.38 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.70 (n/a)</td><td>502.70 (n/a)</td><td>519.80 (n/a)</td><td>356.70 (n/a)</td><td>90.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>671.90 (n/a)</td><td>521.58 (n/a)</td><td>559.70 (n/a)</td><td>315.20 (n/a)</td><td>141.57 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>448.70 (n/a)</td><td>313.28 (n/a)</td><td>307.10 (n/a)</td><td>200.10 (n/a)</td><td>88.51 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1062.00 (n/a)</td><td>626.78 (n/a)</td><td>588.00 (n/a)</td><td>338.10 (n/a)</td><td>265.25 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.10 (n/a)</td><td>453.82 (n/a)</td><td>544.00 (n/a)</td><td>291.60 (n/a)</td><td>142.43 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.60 (n/a)</td><td>505.36 (n/a)</td><td>547.50 (n/a)</td><td>286.10 (n/a)</td><td>128.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1064.50 (n/a)</td><td>619.10 (n/a)</td><td>515.50 (n/a)</td><td>432.10 (n/a)</td><td>258.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>638.90 (n/a)</td><td>550.48 (n/a)</td><td>551.50 (n/a)</td><td>432.90 (n/a)</td><td>76.98 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1896.20 (n/a)</td><td>679.78 (n/a)</td><td>478.60 (n/a)</td><td>251.50 (n/a)</td><td>688.09 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>616.00 (n/a)</td><td>487.88 (n/a)</td><td>514.70 (n/a)</td><td>346.10 (n/a)</td><td>118.88 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>599.70 (n/a)</td><td>416.20 (n/a)</td><td>437.40 (n/a)</td><td>287.30 (n/a)</td><td>128.02 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>472.40 (n/a)</td><td>426.42 (n/a)</td><td>428.00 (n/a)</td><td>367.20 (n/a)</td><td>38.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>449.40 (n/a)</td><td>336.62 (n/a)</td><td>291.90 (n/a)</td><td>235.40 (n/a)</td><td>97.26 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>582.80 (n/a)</td><td>427.80 (n/a)</td><td>411.60 (n/a)</td><td>297.10 (n/a)</td><td>104.31 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (+5.21%)</td><td>0.08 (+12.19%)</td><td>0.08 <b>(+31.51%)</b></td><td>0.06 (+18.96%)</td><td>0.02 (-18.81%)</td><td>570.70 (-15.94%)</td><td>411.16 (-14.18%)</td><td>405.10 <b>(-23.97%)</b></td><td>302.20 (-4.94%)</td><td>105.49 <b>(-31.23%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>678.90 (n/a)</td><td>479.08 (n/a)</td><td>532.80 (n/a)</td><td>317.90 (n/a)</td><td>153.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>659.90 (n/a)</td><td>427.66 (n/a)</td><td>454.00 (n/a)</td><td>252.60 (n/a)</td><td>161.11 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>839.90 (n/a)</td><td>486.64 (n/a)</td><td>493.10 (n/a)</td><td>282.10 (n/a)</td><td>228.20 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1059.60 (n/a)</td><td>550.46 (n/a)</td><td>497.70 (n/a)</td><td>235.30 (n/a)</td><td>305.62 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2504.00 (n/a)</td><td>884.70 (n/a)</td><td>570.70 (n/a)</td><td>282.30 (n/a)</td><td>912.96 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>576.50 (n/a)</td><td>468.00 (n/a)</td><td>483.30 (n/a)</td><td>374.40 (n/a)</td><td>77.49 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (-11.84%)</td><td>0.01 (-9.13%)</td><td>0.01 (+2.49%)</td><td>0.01 (-10.63%)</td><td>0.00 (-2.03%)</td><td>490.60 (+11.91%)</td><td>333.52 (+11.23%)</td><td>280.30 (-2.44%)</td><td>242.90 (+13.45%)</td><td>100.78 <b>(+21.15%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>438.40 (n/a)</td><td>299.86 (n/a)</td><td>287.30 (n/a)</td><td>214.10 (n/a)</td><td>83.18 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+0.66%)</td><td>0.01 (-6.67%)</td><td>0.01 (-13.61%)</td><td>0.01 (-0.23%)</td><td>0.00 (+1.76%)</td><td>625.90 (+0.22%)</td><td>456.12 (+8.97%)</td><td>539.90 (+15.76%)</td><td>240.10 (-0.62%)</td><td>182.42 (+9.65%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>624.50 (n/a)</td><td>418.58 (n/a)</td><td>466.40 (n/a)</td><td>241.60 (n/a)</td><td>166.37 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+1.04%)</td><td>0.01 (-0.15%)</td><td>0.02 (+16.60%)</td><td>0.01 (+1.20%)</td><td>0.01 <b>(+28.52%)</b></td><td>511.10 (-1.18%)</td><td>332.78 (+5.42%)</td><td>244.90 (-14.22%)</td><td>205.50 (-1.06%)</td><td>143.48 <b>(+22.11%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>517.20 (n/a)</td><td>315.66 (n/a)</td><td>285.50 (n/a)</td><td>207.70 (n/a)</td><td>117.50 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (-16.56%)</td><td>0.01 (-12.86%)</td><td>0.01 (-13.87%)</td><td>0.01 (+1.73%)</td><td>0.00 <b>(-28.64%)</b></td><td>545.20 (-1.69%)</td><td>382.80 (+9.02%)</td><td>331.60 (+16.11%)</td><td>249.30 (+19.86%)</td><td>126.43 (-15.20%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.60 (n/a)</td><td>351.12 (n/a)</td><td>285.60 (n/a)</td><td>208.00 (n/a)</td><td>149.10 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+3.77%)</td><td>0.01 (-7.71%)</td><td>0.01 (+2.99%)</td><td>0.00 <b>(-80.61%)</b></td><td>0.01 <b>(+91.73%)</b></td><td>2482.70 <b>(+415.72%)</b></td><td>755.50 <b>(+102.71%)</b></td><td>356.40 (-2.91%)</td><td>266.90 (-3.61%)</td><td>966.42 <b>(+981.68%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>481.40 (n/a)</td><td>372.70 (n/a)</td><td>367.10 (n/a)</td><td>276.90 (n/a)</td><td>89.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 <b>(-35.64%)</b></td><td>0.01 <b>(-20.50%)</b></td><td>0.01 (-9.65%)</td><td>0.00 <b>(-41.76%)</b></td><td>0.00 <b>(-31.99%)</b></td><td>1052.10 <b>(+71.69%)</b></td><td>646.78 <b>(+27.95%)</b></td><td>604.00 (+10.68%)</td><td>452.50 <b>(+55.39%)</b></td><td>242.59 <b>(+85.59%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>612.80 (n/a)</td><td>505.48 (n/a)</td><td>545.70 (n/a)</td><td>291.20 (n/a)</td><td>130.72 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-6.12%)</td><td>0.02 (+5.65%)</td><td>0.03 <b>(+64.06%)</b></td><td>0.00 <b>(-68.69%)</b></td><td>0.01 <b>(+20.82%)</b></td><td>1910.50 <b>(+219.37%)</b></td><td>615.70 <b>(+47.68%)</b></td><td>293.00 <b>(-39.05%)</b></td><td>247.40 (+6.50%)</td><td>725.21 <b>(+358.70%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.20 (n/a)</td><td>416.92 (n/a)</td><td>480.70 (n/a)</td><td>232.30 (n/a)</td><td>158.10 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-1.23%)</td><td>0.03 (-17.12%)</td><td>0.03 (-7.51%)</td><td>0.02 <b>(-40.35%)</b></td><td>0.01 <b>(+241.97%)</b></td><td>477.60 <b>(+67.64%)</b></td><td>343.36 <b>(+28.31%)</b></td><td>293.00 (+8.12%)</td><td>243.50 (+1.25%)</td><td>100.41 <b>(+499.57%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>284.90 (n/a)</td><td>267.60 (n/a)</td><td>271.00 (n/a)</td><td>240.50 (n/a)</td><td>16.75 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (+10.90%)</td><td>0.03 (+15.22%)</td><td>0.03 <b>(+20.10%)</b></td><td>0.01 <b>(+32.55%)</b></td><td>0.01 (+2.30%)</td><td>582.20 <b>(-24.56%)</b></td><td>357.92 (-16.78%)</td><td>289.70 (-16.73%)</td><td>233.90 (-9.83%)</td><td>149.56 <b>(-30.04%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>771.70 (n/a)</td><td>430.08 (n/a)</td><td>347.90 (n/a)</td><td>259.40 (n/a)</td><td>213.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-8.51%)</td><td>0.03 (-7.85%)</td><td>0.03 (-1.38%)</td><td>0.02 (+3.18%)</td><td>0.01 (-6.74%)</td><td>433.80 (-3.08%)</td><td>301.60 (+7.53%)</td><td>244.20 (+1.41%)</td><td>236.90 (+9.32%)</td><td>88.01 (-7.85%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>447.60 (n/a)</td><td>280.48 (n/a)</td><td>240.80 (n/a)</td><td>216.70 (n/a)</td><td>95.50 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (-1.04%)</td><td>0.02 <b>(-27.98%)</b></td><td>0.03 (-18.44%)</td><td>0.00 <b>(-84.62%)</b></td><td>0.01 <b>(+232.50%)</b></td><td>2018.30 <b>(+550.02%)</b></td><td>671.60 <b>(+161.77%)</b></td><td>294.90 <b>(+22.62%)</b></td><td>228.50 (+1.02%)</td><td>766.60 <b>(+2055.53%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>310.50 (n/a)</td><td>256.56 (n/a)</td><td>240.50 (n/a)</td><td>226.20 (n/a)</td><td>35.56 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (+4.72%)</td><td>0.02 (-12.09%)</td><td>0.02 <b>(-38.10%)</b></td><td>0.01 (-12.01%)</td><td>0.01 (+6.41%)</td><td>572.00 (+13.65%)</td><td>414.94 (+15.54%)</td><td>449.40 <b>(+61.54%)</b></td><td>246.70 (-4.49%)</td><td>141.67 (+12.47%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.30 (n/a)</td><td>359.12 (n/a)</td><td>278.20 (n/a)</td><td>258.30 (n/a)</td><td>125.97 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 <b>(-24.74%)</b></td><td>0.02 (+5.54%)</td><td>0.03 <b>(+38.41%)</b></td><td>0.02 <b>(+99.96%)</b></td><td>0.01 <b>(-50.86%)</b></td><td>528.50 <b>(-49.99%)</b></td><td>357.02 <b>(-26.94%)</b></td><td>301.70 <b>(-27.75%)</b></td><td>253.60 <b>(+32.91%)</b></td><td>110.78 <b>(-67.42%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1056.70 (n/a)</td><td>488.70 (n/a)</td><td>417.60 (n/a)</td><td>190.80 (n/a)</td><td>340.00 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (+2.98%)</td><td>0.02 (+1.21%)</td><td>0.02 (+8.94%)</td><td>0.01 (+2.98%)</td><td>0.01 (-13.20%)</td><td>567.30 (-2.89%)</td><td>418.72 (-4.24%)</td><td>424.60 (-8.19%)</td><td>261.30 (-2.90%)</td><td>115.17 <b>(-20.73%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.20 (n/a)</td><td>437.26 (n/a)</td><td>462.50 (n/a)</td><td>269.10 (n/a)</td><td>145.30 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 <b>(-25.68%)</b></td><td>0.04 <b>(-31.60%)</b></td><td>0.04 <b>(-41.92%)</b></td><td>0.03 <b>(-20.58%)</b></td><td>0.01 <b>(-21.66%)</b></td><td>552.40 <b>(+25.92%)</b></td><td>405.54 <b>(+45.71%)</b></td><td>419.90 <b>(+72.16%)</b></td><td>286.60 <b>(+34.55%)</b></td><td>110.59 <b>(+21.14%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>438.70 (n/a)</td><td>278.32 (n/a)</td><td>243.90 (n/a)</td><td>213.00 (n/a)</td><td>91.29 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (-1.41%)</td><td>0.04 (-9.46%)</td><td>0.03 (-15.72%)</td><td>0.03 (-18.64%)</td><td>0.02 (+10.88%)</td><td>648.00 <b>(+22.91%)</b></td><td>430.60 (+16.49%)</td><td>477.40 (+18.64%)</td><td>231.80 (+1.44%)</td><td>179.80 <b>(+38.59%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>527.20 (n/a)</td><td>369.64 (n/a)</td><td>402.40 (n/a)</td><td>228.50 (n/a)</td><td>129.74 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (-16.24%)</td><td>0.04 <b>(-28.46%)</b></td><td>0.04 <b>(-27.69%)</b></td><td>0.03 (-10.95%)</td><td>0.01 (-14.96%)</td><td>539.90 (+12.29%)</td><td>412.28 <b>(+39.30%)</b></td><td>370.20 <b>(+38.29%)</b></td><td>260.00 (+19.38%)</td><td>119.41 (+12.81%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>480.80 (n/a)</td><td>295.96 (n/a)</td><td>267.70 (n/a)</td><td>217.80 (n/a)</td><td>105.86 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (+7.08%)</td><td>0.05 <b>(+24.46%)</b></td><td>0.05 <b>(+48.93%)</b></td><td>0.03 (+14.26%)</td><td>0.01 (+12.43%)</td><td>496.60 (-12.48%)</td><td>368.18 (-19.23%)</td><td>328.50 <b>(-32.86%)</b></td><td>257.80 (-6.59%)</td><td>114.05 (-5.12%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>567.40 (n/a)</td><td>455.86 (n/a)</td><td>489.30 (n/a)</td><td>276.00 (n/a)</td><td>120.21 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (-5.83%)</td><td>0.05 (-17.60%)</td><td>0.04 <b>(-34.47%)</b></td><td>0.02 <b>(-27.63%)</b></td><td>0.02 (-4.03%)</td><td>657.40 <b>(+38.17%)</b></td><td>407.50 <b>(+24.40%)</b></td><td>384.60 <b>(+52.62%)</b></td><td>242.80 (+6.21%)</td><td>162.03 <b>(+39.15%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>475.80 (n/a)</td><td>327.56 (n/a)</td><td>252.00 (n/a)</td><td>228.60 (n/a)</td><td>116.45 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (-0.15%)</td><td>0.04 (-17.90%)</td><td>0.03 <b>(-28.46%)</b></td><td>0.02 <b>(-29.95%)</b></td><td>0.02 <b>(+35.42%)</b></td><td>677.70 <b>(+42.76%)</b></td><td>497.84 <b>(+29.52%)</b></td><td>528.20 <b>(+39.77%)</b></td><td>261.50 (+0.15%)</td><td>156.71 <b>(+83.48%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>474.70 (n/a)</td><td>384.36 (n/a)</td><td>377.90 (n/a)</td><td>261.10 (n/a)</td><td>85.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (-14.57%)</td><td>0.09 (-14.76%)</td><td>0.09 <b>(-34.06%)</b></td><td>0.06 (+7.78%)</td><td>0.03 <b>(-37.38%)</b></td><td>529.10 (-7.22%)</td><td>372.10 (+7.45%)</td><td>367.10 <b>(+51.63%)</b></td><td>253.20 (+17.06%)</td><td>109.91 <b>(-32.05%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>570.30 (n/a)</td><td>346.30 (n/a)</td><td>242.10 (n/a)</td><td>216.30 (n/a)</td><td>161.76 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (+4.68%)</td><td>0.08 <b>(-30.80%)</b></td><td>0.07 <b>(-48.19%)</b></td><td>0.06 (-13.36%)</td><td>0.03 (+16.60%)</td><td>588.90 (+15.43%)</td><td>450.66 <b>(+48.19%)</b></td><td>490.90 <b>(+93.04%)</b></td><td>231.70 (-4.45%)</td><td>134.73 (+16.58%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>510.20 (n/a)</td><td>304.10 (n/a)</td><td>254.30 (n/a)</td><td>242.50 (n/a)</td><td>115.57 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 <b>(+28.26%)</b></td><td>0.10 <b>(+22.11%)</b></td><td>0.07 (+0.78%)</td><td>0.06 (+0.30%)</td><td>0.04 <b>(+99.56%)</b></td><td>554.40 (-0.29%)</td><td>385.92 (-10.06%)</td><td>450.20 (-0.77%)</td><td>224.50 <b>(-22.02%)</b></td><td>150.88 <b>(+46.43%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>556.00 (n/a)</td><td>429.08 (n/a)</td><td>453.70 (n/a)</td><td>287.90 (n/a)</td><td>103.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (+2.45%)</td><td>0.09 (+10.26%)</td><td>0.08 (+15.45%)</td><td>0.03 <b>(-45.13%)</b></td><td>0.05 <b>(+36.88%)</b></td><td>1085.60 <b>(+82.24%)</b></td><td>506.04 (+12.07%)</td><td>427.80 (-13.38%)</td><td>218.90 (-2.41%)</td><td>352.26 <b>(+145.38%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>595.70 (n/a)</td><td>451.54 (n/a)</td><td>493.90 (n/a)</td><td>224.30 (n/a)</td><td>143.56 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (+10.51%)</td><td>0.08 (+17.15%)</td><td>0.07 (+2.14%)</td><td>0.05 <b>(+80.48%)</b></td><td>0.03 (-8.52%)</td><td>697.90 <b>(-44.59%)</b></td><td>458.94 <b>(-25.62%)</b></td><td>475.10 (-2.08%)</td><td>253.30 (-9.54%)</td><td>161.86 <b>(-57.57%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1259.50 (n/a)</td><td>616.98 (n/a)</td><td>485.20 (n/a)</td><td>280.00 (n/a)</td><td>381.47 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+12.58%)</td><td>0.01 (+3.53%)</td><td>0.01 (+6.07%)</td><td>0.01 (-5.39%)</td><td>0.00 <b>(+23.60%)</b></td><td>478.90 (+5.69%)</td><td>347.80 (-0.41%)</td><td>366.20 (-5.72%)</td><td>203.40 (-11.18%)</td><td>117.35 (+17.61%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>453.10 (n/a)</td><td>349.24 (n/a)</td><td>388.40 (n/a)</td><td>229.00 (n/a)</td><td>99.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+5.32%)</td><td>0.01 <b>(-27.42%)</b></td><td>0.01 <b>(-21.75%)</b></td><td>0.01 <b>(-60.59%)</b></td><td>0.00 <b>(+448.41%)</b></td><td>671.70 <b>(+153.76%)</b></td><td>396.52 <b>(+60.16%)</b></td><td>317.60 <b>(+27.81%)</b></td><td>221.10 (-5.07%)</td><td>181.60 <b>(+1262.01%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>264.70 (n/a)</td><td>247.58 (n/a)</td><td>248.50 (n/a)</td><td>232.90 (n/a)</td><td>13.33 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (-13.25%)</td><td>0.01 <b>(-44.27%)</b></td><td>0.01 <b>(-48.98%)</b></td><td>0.00 <b>(-79.42%)</b></td><td>0.00 <b>(+67.70%)</b></td><td>2038.20 <b>(+385.98%)</b></td><td>787.90 <b>(+164.09%)</b></td><td>547.50 <b>(+96.03%)</b></td><td>272.30 (+15.23%)</td><td>708.77 <b>(+907.51%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>419.40 (n/a)</td><td>298.34 (n/a)</td><td>279.30 (n/a)</td><td>236.30 (n/a)</td><td>70.35 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+1.44%)</td><td>0.01 (+5.43%)</td><td>0.01 (-9.79%)</td><td>0.01 <b>(+215.87%)</b></td><td>0.00 <b>(-21.75%)</b></td><td>592.50 <b>(-68.34%)</b></td><td>391.88 <b>(-37.65%)</b></td><td>316.50 (+10.86%)</td><td>236.50 (-1.42%)</td><td>165.56 <b>(-76.35%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1871.50 (n/a)</td><td>628.50 (n/a)</td><td>285.50 (n/a)</td><td>239.90 (n/a)</td><td>700.06 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 <b>(+35.67%)</b></td><td>0.01 <b>(+31.92%)</b></td><td>0.01 <b>(+21.49%)</b></td><td>0.01 <b>(+93.01%)</b></td><td>0.01 <b>(+26.61%)</b></td><td>547.90 <b>(-48.19%)</b></td><td>380.82 <b>(-29.74%)</b></td><td>437.80 (-17.69%)</td><td>178.20 <b>(-26.30%)</b></td><td>165.86 <b>(-48.95%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1057.50 (n/a)</td><td>542.00 (n/a)</td><td>531.90 (n/a)</td><td>241.80 (n/a)</td><td>324.88 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+10.26%)</td><td>0.01 (-8.02%)</td><td>0.01 <b>(-26.34%)</b></td><td>0.01 (-18.56%)</td><td>0.01 <b>(+37.42%)</b></td><td>611.30 <b>(+22.80%)</b></td><td>420.48 (+17.89%)</td><td>433.80 <b>(+35.73%)</b></td><td>199.20 (-9.33%)</td><td>170.54 <b>(+50.23%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>497.80 (n/a)</td><td>356.66 (n/a)</td><td>319.60 (n/a)</td><td>219.70 (n/a)</td><td>113.52 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+12.66%)</td><td>0.01 <b>(+21.17%)</b></td><td>0.01 <b>(+25.27%)</b></td><td>0.01 (+18.41%)</td><td>0.00 <b>(+29.81%)</b></td><td>609.60 (-15.56%)</td><td>415.56 (-13.88%)</td><td>364.80 <b>(-20.18%)</b></td><td>235.20 (-11.25%)</td><td>175.76 (+6.39%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>721.90 (n/a)</td><td>482.56 (n/a)</td><td>457.00 (n/a)</td><td>265.00 (n/a)</td><td>165.19 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (-12.03%)</td><td>0.01 (-1.69%)</td><td>0.01 (+11.03%)</td><td>0.01 <b>(+221.98%)</b></td><td>0.00 <b>(-53.42%)</b></td><td>568.60 <b>(-68.94%)</b></td><td>458.86 <b>(-33.21%)</b></td><td>468.50 (-9.94%)</td><td>298.50 (+13.71%)</td><td>98.99 <b>(-84.81%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1830.90 (n/a)</td><td>687.00 (n/a)</td><td>520.20 (n/a)</td><td>262.50 (n/a)</td><td>651.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 <b>(+22.22%)</b></td><td>0.01 (-8.36%)</td><td>0.01 (-19.38%)</td><td>0.01 (+0.03%)</td><td>0.01 <b>(+42.90%)</b></td><td>611.90 (-0.03%)</td><td>509.66 (+16.99%)</td><td>583.70 <b>(+24.03%)</b></td><td>200.40 (-18.20%)</td><td>173.69 (+13.61%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>612.10 (n/a)</td><td>435.64 (n/a)</td><td>470.60 (n/a)</td><td>245.00 (n/a)</td><td>152.88 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 <b>(+57.96%)</b></td><td>0.01 <b>(+32.79%)</b></td><td>0.01 <b>(+46.76%)</b></td><td>0.01 (-11.02%)</td><td>0.00 <b>(+233.16%)</b></td><td>543.80 (+12.40%)</td><td>348.68 (-15.96%)</td><td>285.20 <b>(-31.87%)</b></td><td>209.50 <b>(-36.69%)</b></td><td>142.10 <b>(+146.22%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>483.80 (n/a)</td><td>414.88 (n/a)</td><td>418.60 (n/a)</td><td>330.90 (n/a)</td><td>57.71 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (-11.27%)</td><td>0.01 (+8.94%)</td><td>0.01 <b>(+33.23%)</b></td><td>0.01 (+1.13%)</td><td>0.00 (-10.37%)</td><td>514.70 (-1.11%)</td><td>368.24 (-9.10%)</td><td>343.10 <b>(-24.94%)</b></td><td>240.70 (+12.69%)</td><td>129.05 (-0.03%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.50 (n/a)</td><td>405.12 (n/a)</td><td>457.10 (n/a)</td><td>213.60 (n/a)</td><td>129.10 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 <b>(+57.52%)</b></td><td>0.01 <b>(+35.79%)</b></td><td>0.01 (-11.51%)</td><td>0.01 <b>(+81.22%)</b></td><td>0.00 <b>(+69.82%)</b></td><td>591.70 <b>(-44.82%)</b></td><td>439.58 <b>(-26.20%)</b></td><td>514.20 (+13.01%)</td><td>232.80 <b>(-36.53%)</b></td><td>164.53 <b>(-41.87%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1072.30 (n/a)</td><td>595.62 (n/a)</td><td>455.00 (n/a)</td><td>366.80 (n/a)</td><td>283.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 <b>(+51.66%)</b></td><td>0.03 <b>(+52.52%)</b></td><td>0.03 <b>(+72.50%)</b></td><td>0.02 (+15.88%)</td><td>0.01 <b>(+104.46%)</b></td><td>529.90 (-13.71%)</td><td>345.00 <b>(-28.63%)</b></td><td>282.90 <b>(-42.02%)</b></td><td>199.30 <b>(-34.07%)</b></td><td>146.21 <b>(+28.59%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.10 (n/a)</td><td>483.38 (n/a)</td><td>487.90 (n/a)</td><td>302.30 (n/a)</td><td>113.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-19.39%)</td><td>0.02 (-11.86%)</td><td>0.03 (-19.81%)</td><td>0.02 <b>(+290.95%)</b></td><td>0.01 <b>(-51.94%)</b></td><td>481.10 <b>(-74.42%)</b></td><td>358.10 <b>(-37.72%)</b></td><td>300.90 <b>(+24.70%)</b></td><td>270.80 <b>(+24.05%)</b></td><td>105.54 <b>(-85.56%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1880.90 (n/a)</td><td>574.98 (n/a)</td><td>241.30 (n/a)</td><td>218.30 (n/a)</td><td>730.86 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-3.14%)</td><td>0.02 (+4.02%)</td><td>0.03 <b>(+44.35%)</b></td><td>0.01 (-10.22%)</td><td>0.01 (-6.45%)</td><td>628.10 (+11.38%)</td><td>396.18 (-3.62%)</td><td>318.80 <b>(-30.71%)</b></td><td>244.90 (+3.20%)</td><td>158.69 (+10.80%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.90 (n/a)</td><td>411.08 (n/a)</td><td>460.10 (n/a)</td><td>237.30 (n/a)</td><td>143.22 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-11.78%)</td><td>0.02 <b>(-30.83%)</b></td><td>0.02 <b>(-48.81%)</b></td><td>0.01 <b>(-46.09%)</b></td><td>0.01 <b>(+97.69%)</b></td><td>590.00 <b>(+85.48%)</b></td><td>437.70 <b>(+61.54%)</b></td><td>530.10 <b>(+95.32%)</b></td><td>253.70 (+13.31%)</td><td>158.74 <b>(+308.54%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>318.10 (n/a)</td><td>270.96 (n/a)</td><td>271.40 (n/a)</td><td>223.90 (n/a)</td><td>38.86 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (+3.92%)</td><td>0.02 (-17.54%)</td><td>0.02 <b>(-42.62%)</b></td><td>0.02 (-1.04%)</td><td>0.01 <b>(+31.11%)</b></td><td>509.60 (+1.05%)</td><td>401.78 <b>(+26.68%)</b></td><td>484.00 <b>(+74.29%)</b></td><td>225.60 (-3.80%)</td><td>135.25 <b>(+25.79%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.30 (n/a)</td><td>317.16 (n/a)</td><td>277.70 (n/a)</td><td>234.50 (n/a)</td><td>107.52 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-18.85%)</td><td>0.02 (+5.97%)</td><td>0.03 (+17.07%)</td><td>0.02 <b>(+108.85%)</b></td><td>0.01 <b>(-50.01%)</b></td><td>505.90 <b>(-52.12%)</b></td><td>357.98 <b>(-27.04%)</b></td><td>291.20 (-14.58%)</td><td>284.10 <b>(+23.25%)</b></td><td>100.29 <b>(-70.88%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1056.60 (n/a)</td><td>490.64 (n/a)</td><td>340.90 (n/a)</td><td>230.50 (n/a)</td><td>344.44 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 <b>(+34.47%)</b></td><td>0.03 <b>(+96.82%)</b></td><td>0.03 <b>(+163.78%)</b></td><td>0.01 <b>(+76.13%)</b></td><td>0.01 <b>(+27.92%)</b></td><td>1102.40 <b>(-43.23%)</b></td><td>420.58 <b>(-51.47%)</b></td><td>256.60 <b>(-62.09%)</b></td><td>217.20 <b>(-25.64%)</b></td><td>381.84 <b>(-41.49%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1941.70 (n/a)</td><td>866.60 (n/a)</td><td>676.80 (n/a)</td><td>292.10 (n/a)</td><td>652.64 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (+19.43%)</td><td>0.02 (+12.67%)</td><td>0.02 (-17.65%)</td><td>0.02 <b>(+290.97%)</b></td><td>0.01 <b>(-37.21%)</b></td><td>491.90 <b>(-74.43%)</b></td><td>373.72 <b>(-44.36%)</b></td><td>371.10 <b>(+21.43%)</b></td><td>236.40 (-16.26%)</td><td>92.65 <b>(-86.94%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1923.40 (n/a)</td><td>671.70 (n/a)</td><td>305.60 (n/a)</td><td>282.30 (n/a)</td><td>709.17 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 <b>(-42.22%)</b></td><td>0.01 <b>(-49.23%)</b></td><td>0.01 <b>(-50.44%)</b></td><td>0.00 <b>(-75.91%)</b></td><td>0.01 (-6.22%)</td><td>1943.10 <b>(+315.19%)</b></td><td>796.18 <b>(+153.58%)</b></td><td>568.70 <b>(+101.81%)</b></td><td>414.80 <b>(+73.05%)</b></td><td>645.15 <b>(+613.57%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>468.00 (n/a)</td><td>313.98 (n/a)</td><td>281.80 (n/a)</td><td>239.70 (n/a)</td><td>90.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-8.66%)</td><td>0.02 (+16.60%)</td><td>0.02 (-3.73%)</td><td>0.01 <b>(+238.30%)</b></td><td>0.01 <b>(-36.79%)</b></td><td>571.40 <b>(-70.44%)</b></td><td>382.26 <b>(-43.83%)</b></td><td>383.50 (+3.87%)</td><td>273.70 (+9.48%)</td><td>121.46 <b>(-82.79%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1933.20 (n/a)</td><td>680.50 (n/a)</td><td>369.20 (n/a)</td><td>250.00 (n/a)</td><td>705.85 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (+11.15%)</td><td>0.02 (+16.71%)</td><td>0.01 (-8.58%)</td><td>0.01 (-9.65%)</td><td>0.01 <b>(+41.18%)</b></td><td>636.30 (+10.68%)</td><td>458.66 (-6.35%)</td><td>576.60 (+9.37%)</td><td>231.60 (-10.02%)</td><td>192.38 <b>(+45.57%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.90 (n/a)</td><td>489.78 (n/a)</td><td>527.20 (n/a)</td><td>257.40 (n/a)</td><td>132.15 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 <b>(+22.80%)</b></td><td>0.02 (+0.03%)</td><td>0.03 (+4.80%)</td><td>0.01 <b>(-33.78%)</b></td><td>0.01 <b>(+92.58%)</b></td><td>786.10 <b>(+51.00%)</b></td><td>449.60 (+19.35%)</td><td>302.30 (-4.58%)</td><td>233.60 (-18.58%)</td><td>251.20 <b>(+143.49%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.60 (n/a)</td><td>376.70 (n/a)</td><td>316.80 (n/a)</td><td>286.90 (n/a)</td><td>103.16 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (+1.97%)</td><td>0.04 (-15.86%)</td><td>0.04 <b>(-38.11%)</b></td><td>0.03 <b>(+22.21%)</b></td><td>0.01 (-12.17%)</td><td>482.80 (-18.17%)</td><td>396.02 (+14.40%)</td><td>434.60 <b>(+61.56%)</b></td><td>243.60 (-1.93%)</td><td>99.70 <b>(-30.31%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.00 (n/a)</td><td>346.18 (n/a)</td><td>269.00 (n/a)</td><td>248.40 (n/a)</td><td>143.05 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (-4.14%)</td><td>0.04 <b>(-21.73%)</b></td><td>0.04 <b>(-35.14%)</b></td><td>0.03 (-3.06%)</td><td>0.01 (-2.36%)</td><td>525.10 (+3.14%)</td><td>395.74 <b>(+27.72%)</b></td><td>423.20 <b>(+54.17%)</b></td><td>244.20 (+4.31%)</td><td>116.59 (+2.08%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>509.10 (n/a)</td><td>309.84 (n/a)</td><td>274.50 (n/a)</td><td>234.10 (n/a)</td><td>114.22 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (-11.89%)</td><td>0.04 (+7.77%)</td><td>0.04 (+19.31%)</td><td>0.03 <b>(+320.00%)</b></td><td>0.02 <b>(-33.81%)</b></td><td>595.90 <b>(-76.19%)</b></td><td>421.54 <b>(-46.93%)</b></td><td>383.60 (-16.19%)</td><td>273.90 (+13.51%)</td><td>157.35 <b>(-83.63%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2502.60 (n/a)</td><td>794.26 (n/a)</td><td>457.70 (n/a)</td><td>241.30 (n/a)</td><td>960.96 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (-19.83%)</td><td>0.03 <b>(-39.96%)</b></td><td>0.03 <b>(-50.80%)</b></td><td>0.01 <b>(-68.91%)</b></td><td>0.02 (+4.27%)</td><td>1897.50 <b>(+221.66%)</b></td><td>730.72 <b>(+125.38%)</b></td><td>554.20 <b>(+103.23%)</b></td><td>274.30 <b>(+24.74%)</b></td><td>663.65 <b>(+336.39%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>589.90 (n/a)</td><td>324.22 (n/a)</td><td>272.70 (n/a)</td><td>219.90 (n/a)</td><td>152.08 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 <b>(-31.14%)</b></td><td>0.04 (-16.85%)</td><td>0.05 (+10.55%)</td><td>0.01 <b>(-78.34%)</b></td><td>0.02 (-0.16%)</td><td>2500.20 <b>(+361.72%)</b></td><td>757.74 <b>(+111.23%)</b></td><td>298.00 (-9.53%)</td><td>271.60 <b>(+45.24%)</b></td><td>976.03 <b>(+614.86%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>541.50 (n/a)</td><td>358.72 (n/a)</td><td>329.40 (n/a)</td><td>187.00 (n/a)</td><td>136.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (+16.75%)</td><td>0.05 (+3.78%)</td><td>0.05 (-10.08%)</td><td>0.03 (-0.72%)</td><td>0.02 <b>(+50.62%)</b></td><td>486.90 (+0.72%)</td><td>331.88 (-0.07%)</td><td>343.40 (+11.20%)</td><td>222.40 (-14.36%)</td><td>107.79 <b>(+21.02%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>483.40 (n/a)</td><td>332.10 (n/a)</td><td>308.80 (n/a)</td><td>259.70 (n/a)</td><td>89.07 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (-13.58%)</td><td>0.05 (+19.17%)</td><td>0.06 <b>(+87.75%)</b></td><td>0.01 (-0.99%)</td><td>0.02 (+0.92%)</td><td>1922.60 (+0.99%)</td><td>643.56 (-9.23%)</td><td>274.10 <b>(-46.75%)</b></td><td>262.60 (+15.68%)</td><td>721.45 (+6.08%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1903.70 (n/a)</td><td>709.02 (n/a)</td><td>514.70 (n/a)</td><td>227.00 (n/a)</td><td>680.11 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 <b>(+26.90%)</b></td><td>0.06 <b>(+37.01%)</b></td><td>0.07 <b>(+74.49%)</b></td><td>0.03 (+0.09%)</td><td>0.02 <b>(+40.56%)</b></td><td>501.40 (-0.08%)</td><td>300.64 <b>(-24.62%)</b></td><td>243.30 <b>(-42.70%)</b></td><td>218.10 <b>(-21.21%)</b></td><td>117.68 (+12.25%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>501.80 (n/a)</td><td>398.84 (n/a)</td><td>424.60 (n/a)</td><td>276.80 (n/a)</td><td>104.84 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (+0.12%)</td><td>0.05 <b>(+29.87%)</b></td><td>0.05 <b>(+88.34%)</b></td><td>0.03 <b>(+38.45%)</b></td><td>0.02 (-13.63%)</td><td>604.40 <b>(-27.77%)</b></td><td>406.32 <b>(-30.42%)</b></td><td>329.40 <b>(-46.91%)</b></td><td>205.60 (-0.15%)</td><td>179.54 <b>(-33.35%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>836.80 (n/a)</td><td>583.92 (n/a)</td><td>620.40 (n/a)</td><td>205.90 (n/a)</td><td>269.37 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (-11.74%)</td><td>0.04 <b>(-26.51%)</b></td><td>0.04 <b>(-39.79%)</b></td><td>0.03 (-14.75%)</td><td>0.01 (-3.48%)</td><td>589.40 (+17.29%)</td><td>423.48 <b>(+38.11%)</b></td><td>419.40 <b>(+66.10%)</b></td><td>267.70 (+13.29%)</td><td>139.75 <b>(+24.90%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>502.50 (n/a)</td><td>306.62 (n/a)</td><td>252.50 (n/a)</td><td>236.30 (n/a)</td><td>111.89 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 <b>(+25.66%)</b></td><td>0.05 (+12.34%)</td><td>0.05 (+15.71%)</td><td>0.03 <b>(-20.95%)</b></td><td>0.02 <b>(+110.78%)</b></td><td>644.10 <b>(+26.52%)</b></td><td>389.80 (-2.19%)</td><td>326.10 (-13.57%)</td><td>246.50 <b>(-20.41%)</b></td><td>164.40 <b>(+109.75%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>509.10 (n/a)</td><td>398.52 (n/a)</td><td>377.30 (n/a)</td><td>309.70 (n/a)</td><td>78.38 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (+5.08%)</td><td>0.04 (+15.44%)</td><td>0.04 (+5.53%)</td><td>0.03 (+10.83%)</td><td>0.02 <b>(+20.24%)</b></td><td>581.00 (-9.77%)</td><td>409.28 (-11.18%)</td><td>437.80 (-5.24%)</td><td>248.50 (-4.83%)</td><td>144.84 (+5.26%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>643.90 (n/a)</td><td>460.80 (n/a)</td><td>462.00 (n/a)</td><td>261.10 (n/a)</td><td>137.60 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (+3.68%)</td><td>0.11 (-7.97%)</td><td>0.13 (+3.23%)</td><td>0.05 <b>(-27.30%)</b></td><td>0.04 <b>(+57.78%)</b></td><td>621.00 <b>(+37.57%)</b></td><td>354.94 <b>(+20.65%)</b></td><td>253.20 (-3.14%)</td><td>227.30 (-3.56%)</td><td>173.41 <b>(+93.66%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>451.40 (n/a)</td><td>294.20 (n/a)</td><td>261.40 (n/a)</td><td>235.70 (n/a)</td><td>89.54 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (-10.53%)</td><td>0.12 <b>(+23.58%)</b></td><td>0.13 <b>(+35.40%)</b></td><td>0.08 <b>(+25.56%)</b></td><td>0.02 <b>(-34.98%)</b></td><td>432.80 <b>(-20.37%)</b></td><td>289.96 <b>(-24.83%)</b></td><td>259.80 <b>(-26.15%)</b></td><td>241.90 (+11.78%)</td><td>80.69 <b>(-43.80%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>543.50 (n/a)</td><td>385.72 (n/a)</td><td>351.80 (n/a)</td><td>216.40 (n/a)</td><td>143.57 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (-1.63%)</td><td>0.12 (+18.91%)</td><td>0.13 <b>(+49.38%)</b></td><td>0.06 (-13.68%)</td><td>0.03 (+2.57%)</td><td>532.60 (+15.83%)</td><td>310.98 (-14.40%)</td><td>261.20 <b>(-33.04%)</b></td><td>242.40 (+1.64%)</td><td>124.45 <b>(+22.68%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>459.80 (n/a)</td><td>363.28 (n/a)</td><td>390.10 (n/a)</td><td>238.50 (n/a)</td><td>101.45 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 <b>(-21.06%)</b></td><td>0.12 (+8.39%)</td><td>0.12 <b>(+34.28%)</b></td><td>0.09 <b>(+33.41%)</b></td><td>0.02 <b>(-60.11%)</b></td><td>371.20 <b>(-25.04%)</b></td><td>290.98 (-17.68%)</td><td>267.10 <b>(-25.52%)</b></td><td>243.90 <b>(+26.70%)</b></td><td>50.44 <b>(-62.79%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>495.20 (n/a)</td><td>353.46 (n/a)</td><td>358.60 (n/a)</td><td>192.50 (n/a)</td><td>135.56 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (-5.92%)</td><td>0.08 <b>(-24.49%)</b></td><td>0.08 <b>(-33.96%)</b></td><td>0.04 <b>(-24.63%)</b></td><td>0.03 (-4.83%)</td><td>731.90 <b>(+32.69%)</b></td><td>448.70 <b>(+35.14%)</b></td><td>419.20 <b>(+51.45%)</b></td><td>255.90 (+6.31%)</td><td>175.54 <b>(+35.66%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>551.60 (n/a)</td><td>332.02 (n/a)</td><td>276.80 (n/a)</td><td>240.70 (n/a)</td><td>129.40 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (+6.27%)</td><td>0.10 (+11.02%)</td><td>0.10 (+13.57%)</td><td>0.07 <b>(+303.55%)</b></td><td>0.03 <b>(-29.23%)</b></td><td>485.80 <b>(-75.22%)</b></td><td>353.12 <b>(-45.02%)</b></td><td>312.70 (-11.94%)</td><td>219.30 (-5.88%)</td><td>120.76 <b>(-83.70%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1960.60 (n/a)</td><td>642.28 (n/a)</td><td>355.10 (n/a)</td><td>233.00 (n/a)</td><td>740.68 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (-18.38%)</td><td>0.08 (-9.14%)</td><td>0.07 (+10.91%)</td><td>0.05 (-9.71%)</td><td>0.03 <b>(-23.13%)</b></td><td>655.80 (+10.74%)</td><td>466.12 (+5.76%)</td><td>491.50 (-9.83%)</td><td>275.10 <b>(+22.48%)</b></td><td>177.91 (-1.27%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>592.20 (n/a)</td><td>440.74 (n/a)</td><td>545.10 (n/a)</td><td>224.60 (n/a)</td><td>180.20 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (+2.66%)</td><td>0.11 <b>(+27.42%)</b></td><td>0.12 <b>(+73.87%)</b></td><td>0.06 (+16.34%)</td><td>0.03 (-13.36%)</td><td>519.00 (-14.04%)</td><td>320.58 <b>(-24.35%)</b></td><td>278.40 <b>(-42.49%)</b></td><td>238.20 (-2.58%)</td><td>114.93 <b>(-23.07%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>603.80 (n/a)</td><td>423.76 (n/a)</td><td>484.10 (n/a)</td><td>244.50 (n/a)</td><td>149.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.17 <b>(+26.05%)</b></td><td>0.08 <b>(-28.29%)</b></td><td>0.06 <b>(-48.18%)</b></td><td>0.04 <b>(-42.43%)</b></td><td>0.05 <b>(+102.88%)</b></td><td>798.20 <b>(+73.71%)</b></td><td>504.02 <b>(+63.69%)</b></td><td>514.80 <b>(+92.95%)</b></td><td>197.80 <b>(-20.69%)</b></td><td>214.04 <b>(+146.18%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>459.50 (n/a)</td><td>307.92 (n/a)</td><td>266.80 (n/a)</td><td>249.40 (n/a)</td><td>86.94 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 <b>(+39.56%)</b></td><td>0.07 (-0.78%)</td><td>0.07 (+1.61%)</td><td>0.04 <b>(-31.29%)</b></td><td>0.03 <b>(+171.10%)</b></td><td>773.90 <b>(+45.52%)</b></td><td>536.78 (+13.66%)</td><td>500.20 (-1.57%)</td><td>255.50 <b>(-28.35%)</b></td><td>194.86 <b>(+171.69%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>531.80 (n/a)</td><td>472.26 (n/a)</td><td>508.20 (n/a)</td><td>356.60 (n/a)</td><td>71.72 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 (-17.77%)</td><td>0.07 (-14.15%)</td><td>0.07 (-17.22%)</td><td>0.06 <b>(+23.49%)</b></td><td>0.02 <b>(-44.51%)</b></td><td>543.10 (-19.02%)</td><td>455.98 (+6.97%)</td><td>469.90 <b>(+20.80%)</b></td><td>308.80 <b>(+21.62%)</b></td><td>90.73 <b>(-46.81%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>670.70 (n/a)</td><td>426.28 (n/a)</td><td>389.00 (n/a)</td><td>253.90 (n/a)</td><td>170.56 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (+0.59%)</td><td>0.08 (-10.78%)</td><td>0.07 <b>(-20.82%)</b></td><td>0.05 (+2.34%)</td><td>0.04 (-11.39%)</td><td>646.90 (-2.30%)</td><td>442.16 (+9.07%)</td><td>503.30 <b>(+26.30%)</b></td><td>238.10 (-0.58%)</td><td>163.05 (-8.57%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>662.10 (n/a)</td><td>405.38 (n/a)</td><td>398.50 (n/a)</td><td>239.50 (n/a)</td><td>178.33 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 <b>(-31.34%)</b></td><td>0.01 (-18.07%)</td><td>0.01 <b>(-31.45%)</b></td><td>0.01 (+17.68%)</td><td>0.00 <b>(-76.84%)</b></td><td>464.10 (-15.03%)</td><td>403.24 (+8.99%)</td><td>393.10 <b>(+45.86%)</b></td><td>364.00 <b>(+45.66%)</b></td><td>42.01 <b>(-71.96%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.20 (n/a)</td><td>369.98 (n/a)</td><td>269.50 (n/a)</td><td>249.90 (n/a)</td><td>149.84 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (+14.19%)</td><td>0.02 (+16.34%)</td><td>0.02 <b>(+22.52%)</b></td><td>0.01 <b>(+38.88%)</b></td><td>0.01 (-6.89%)</td><td>439.80 <b>(-28.01%)</b></td><td>342.10 (-17.47%)</td><td>343.00 (-18.37%)</td><td>227.60 (-12.43%)</td><td>85.98 <b>(-39.52%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.90 (n/a)</td><td>414.54 (n/a)</td><td>420.20 (n/a)</td><td>259.90 (n/a)</td><td>142.15 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (-7.07%)</td><td>0.01 <b>(-29.43%)</b></td><td>0.01 <b>(-48.78%)</b></td><td>0.01 <b>(-20.22%)</b></td><td>0.00 (-1.12%)</td><td>663.90 <b>(+25.34%)</b></td><td>528.66 <b>(+44.93%)</b></td><td>605.40 <b>(+95.23%)</b></td><td>268.30 (+7.62%)</td><td>162.00 <b>(+29.33%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.70 (n/a)</td><td>364.76 (n/a)</td><td>310.10 (n/a)</td><td>249.30 (n/a)</td><td>125.26 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+0.73%)</td><td>0.01 <b>(+29.19%)</b></td><td>0.01 (+19.25%)</td><td>0.01 <b>(+409.35%)</b></td><td>0.00 <b>(-50.22%)</b></td><td>479.00 <b>(-80.37%)</b></td><td>400.18 <b>(-52.67%)</b></td><td>406.20 (-16.13%)</td><td>284.10 (-0.73%)</td><td>72.20 <b>(-91.96%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2439.90 (n/a)</td><td>845.56 (n/a)</td><td>484.30 (n/a)</td><td>286.20 (n/a)</td><td>897.51 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 (+0.34%)</td><td>0.01 (+3.17%)</td><td>0.01 <b>(+27.72%)</b></td><td>0.01 (+1.72%)</td><td>0.00 (-6.98%)</td><td>611.50 (-1.69%)</td><td>404.48 (-4.68%)</td><td>344.10 <b>(-21.69%)</b></td><td>233.30 (-0.34%)</td><td>149.81 (-6.10%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>622.00 (n/a)</td><td>424.32 (n/a)</td><td>439.40 (n/a)</td><td>234.10 (n/a)</td><td>159.53 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 <b>(+20.85%)</b></td><td>0.02 (+2.43%)</td><td>0.02 (-2.43%)</td><td>0.01 (+6.22%)</td><td>0.01 <b>(+25.64%)</b></td><td>556.40 (-5.85%)</td><td>337.82 (+1.45%)</td><td>244.80 (+2.47%)</td><td>189.40 (-17.26%)</td><td>162.06 (+4.35%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.00 (n/a)</td><td>332.98 (n/a)</td><td>238.90 (n/a)</td><td>228.90 (n/a)</td><td>155.31 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 <b>(-32.04%)</b></td><td>0.01 <b>(-28.47%)</b></td><td>0.01 (-12.23%)</td><td>0.00 <b>(-68.00%)</b></td><td>0.00 (-11.61%)</td><td>1854.70 <b>(+212.45%)</b></td><td>791.76 <b>(+71.12%)</b></td><td>590.20 (+13.94%)</td><td>397.90 <b>(+47.15%)</b></td><td>600.95 <b>(+358.31%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>593.60 (n/a)</td><td>462.68 (n/a)</td><td>518.00 (n/a)</td><td>270.40 (n/a)</td><td>131.12 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 <b>(-29.16%)</b></td><td>0.01 (-18.34%)</td><td>0.01 (+5.55%)</td><td>0.00 <b>(-65.99%)</b></td><td>0.01 (-14.21%)</td><td>1794.40 <b>(+194.02%)</b></td><td>674.16 <b>(+59.26%)</b></td><td>465.70 (-5.27%)</td><td>293.90 <b>(+41.16%)</b></td><td>632.83 <b>(+282.19%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.30 (n/a)</td><td>423.32 (n/a)</td><td>491.60 (n/a)</td><td>208.20 (n/a)</td><td>165.58 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.02 <b>(+27.92%)</b></td><td>0.01 <b>(+38.71%)</b></td><td>0.01 <b>(+36.46%)</b></td><td>0.01 (+17.58%)</td><td>0.00 <b>(+55.02%)</b></td><td>522.40 (-14.95%)</td><td>388.62 <b>(-24.65%)</b></td><td>407.00 <b>(-26.72%)</b></td><td>235.30 <b>(-21.83%)</b></td><td>136.11 (+10.47%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.20 (n/a)</td><td>515.72 (n/a)</td><td>555.40 (n/a)</td><td>301.00 (n/a)</td><td>123.21 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 <b>(-38.17%)</b></td><td>0.01 <b>(-32.11%)</b></td><td>0.01 <b>(-37.81%)</b></td><td>0.00 <b>(-40.62%)</b></td><td>0.00 <b>(-46.32%)</b></td><td>1004.30 <b>(+68.39%)</b></td><td>559.40 <b>(+41.52%)</b></td><td>482.30 <b>(+60.77%)</b></td><td>331.10 <b>(+61.75%)</b></td><td>258.14 <b>(+43.59%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.40 (n/a)</td><td>395.28 (n/a)</td><td>300.00 (n/a)</td><td>204.70 (n/a)</td><td>179.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.01 (-11.52%)</td><td>0.01 (+5.36%)</td><td>0.01 (-4.14%)</td><td>0.01 <b>(+199.90%)</b></td><td>0.00 <b>(-39.63%)</b></td><td>629.40 <b>(-66.65%)</b></td><td>447.48 <b>(-36.60%)</b></td><td>474.90 (+4.33%)</td><td>295.70 (+13.04%)</td><td>144.25 <b>(-78.71%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1887.50 (n/a)</td><td>705.76 (n/a)</td><td>455.20 (n/a)</td><td>261.60 (n/a)</td><td>677.49 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 <b>(-25.47%)</b></td><td>0.02 (-15.71%)</td><td>0.02 (-2.03%)</td><td>0.01 <b>(+146.70%)</b></td><td>0.01 <b>(-50.05%)</b></td><td>809.10 <b>(-59.46%)</b></td><td>490.14 <b>(-26.36%)</b></td><td>424.00 (+2.07%)</td><td>310.80 <b>(+34.20%)</b></td><td>196.11 <b>(-73.82%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1996.00 (n/a)</td><td>665.62 (n/a)</td><td>415.40 (n/a)</td><td>231.60 (n/a)</td><td>749.23 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 (-1.34%)</td><td>0.04 (+10.77%)</td><td>0.05 (+12.06%)</td><td>0.02 <b>(+209.25%)</b></td><td>0.01 <b>(-31.40%)</b></td><td>624.70 <b>(-67.67%)</b></td><td>341.74 <b>(-44.12%)</b></td><td>268.50 (-10.77%)</td><td>260.30 (+1.36%)</td><td>158.69 <b>(-78.51%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1932.00 (n/a)</td><td>611.60 (n/a)</td><td>300.90 (n/a)</td><td>256.80 (n/a)</td><td>738.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 <b>(+23.92%)</b></td><td>0.02 <b>(+22.94%)</b></td><td>0.02 (+15.60%)</td><td>0.01 (-5.27%)</td><td>0.01 <b>(+47.27%)</b></td><td>644.50 (+5.57%)</td><td>411.96 (-13.68%)</td><td>447.10 (-13.49%)</td><td>223.10 (-19.31%)</td><td>162.78 <b>(+29.37%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.50 (n/a)</td><td>477.24 (n/a)</td><td>516.80 (n/a)</td><td>276.50 (n/a)</td><td>125.82 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (-10.82%)</td><td>0.04 <b>(+34.23%)</b></td><td>0.03 <b>(+52.75%)</b></td><td>0.03 <b>(+80.80%)</b></td><td>0.00 <b>(-67.74%)</b></td><td>339.40 <b>(-44.70%)</b></td><td>294.02 <b>(-32.10%)</b></td><td>296.10 <b>(-34.52%)</b></td><td>262.10 (+12.15%)</td><td>29.25 <b>(-78.60%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>613.70 (n/a)</td><td>433.02 (n/a)</td><td>452.20 (n/a)</td><td>233.70 (n/a)</td><td>136.69 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-8.91%)</td><td>0.02 <b>(-31.58%)</b></td><td>0.01 <b>(-37.56%)</b></td><td>0.01 <b>(-57.42%)</b></td><td>0.01 <b>(+25.20%)</b></td><td>1041.70 <b>(+134.83%)</b></td><td>581.84 <b>(+65.64%)</b></td><td>561.20 <b>(+60.16%)</b></td><td>285.10 (+9.78%)</td><td>282.89 <b>(+226.65%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>443.60 (n/a)</td><td>351.26 (n/a)</td><td>350.40 (n/a)</td><td>259.70 (n/a)</td><td>86.60 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 (-15.67%)</td><td>0.03 (-9.12%)</td><td>0.03 (+14.75%)</td><td>0.02 <b>(-28.72%)</b></td><td>0.01 (-3.93%)</td><td>655.60 <b>(+40.33%)</b></td><td>420.76 (+15.04%)</td><td>360.80 (-12.85%)</td><td>250.40 (+18.62%)</td><td>173.45 <b>(+61.59%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>467.20 (n/a)</td><td>365.76 (n/a)</td><td>414.00 (n/a)</td><td>211.10 (n/a)</td><td>107.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (+0.11%)</td><td>0.02 <b>(-21.34%)</b></td><td>0.02 (-14.25%)</td><td>0.00 <b>(-70.05%)</b></td><td>0.01 <b>(+38.02%)</b></td><td>1884.40 <b>(+233.88%)</b></td><td>714.08 <b>(+82.23%)</b></td><td>488.30 (+16.62%)</td><td>244.20 (-0.08%)</td><td>663.69 <b>(+429.44%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.40 (n/a)</td><td>391.86 (n/a)</td><td>418.70 (n/a)</td><td>244.40 (n/a)</td><td>125.36 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-13.94%)</td><td>0.02 (-18.44%)</td><td>0.02 (-18.22%)</td><td>0.01 (-16.15%)</td><td>0.01 (-4.46%)</td><td>650.60 (+19.27%)</td><td>418.78 <b>(+24.58%)</b></td><td>373.10 <b>(+22.25%)</b></td><td>281.20 (+16.20%)</td><td>154.13 <b>(+25.96%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.50 (n/a)</td><td>336.16 (n/a)</td><td>305.20 (n/a)</td><td>242.00 (n/a)</td><td>122.37 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.04 <b>(+36.22%)</b></td><td>0.03 <b>(+68.61%)</b></td><td>0.03 <b>(+82.15%)</b></td><td>0.02 <b>(+373.15%)</b></td><td>0.01 (+14.76%)</td><td>520.10 <b>(-78.86%)</b></td><td>359.14 <b>(-59.06%)</b></td><td>301.50 <b>(-45.11%)</b></td><td>221.80 <b>(-26.58%)</b></td><td>148.62 <b>(-83.40%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2460.70 (n/a)</td><td>877.32 (n/a)</td><td>549.30 (n/a)</td><td>302.10 (n/a)</td><td>895.10 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-3.81%)</td><td>0.03 <b>(+42.16%)</b></td><td>0.03 <b>(+70.14%)</b></td><td>0.03 <b>(+66.86%)</b></td><td>0.00 <b>(-60.74%)</b></td><td>338.40 <b>(-40.06%)</b></td><td>301.40 <b>(-34.03%)</b></td><td>287.30 <b>(-41.22%)</b></td><td>276.60 (+3.98%)</td><td>29.58 <b>(-74.62%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>564.60 (n/a)</td><td>456.84 (n/a)</td><td>488.80 (n/a)</td><td>266.00 (n/a)</td><td>116.57 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.03 (-3.32%)</td><td>0.02 (+7.92%)</td><td>0.02 (+10.29%)</td><td>0.01 (-5.75%)</td><td>0.01 (-0.61%)</td><td>630.90 (+6.09%)</td><td>433.72 (-6.02%)</td><td>443.20 (-9.33%)</td><td>240.60 (+3.44%)</td><td>160.88 (+15.25%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.70 (n/a)</td><td>461.50 (n/a)</td><td>488.80 (n/a)</td><td>232.60 (n/a)</td><td>139.59 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 <b>(-28.81%)</b></td><td>0.03 <b>(-34.66%)</b></td><td>0.03 <b>(-48.93%)</b></td><td>0.02 (-9.98%)</td><td>0.01 <b>(-46.89%)</b></td><td>658.30 (+11.09%)</td><td>517.44 <b>(+42.18%)</b></td><td>536.80 <b>(+95.84%)</b></td><td>328.30 <b>(+40.48%)</b></td><td>133.13 (-16.37%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>592.60 (n/a)</td><td>363.94 (n/a)</td><td>274.10 (n/a)</td><td>233.70 (n/a)</td><td>159.18 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (+14.56%)</td><td>0.08 <b>(+35.56%)</b></td><td>0.08 <b>(+63.24%)</b></td><td>0.05 (+15.94%)</td><td>0.02 (+9.28%)</td><td>485.00 (-13.75%)</td><td>335.64 <b>(-26.71%)</b></td><td>314.20 <b>(-38.74%)</b></td><td>256.50 (-12.70%)</td><td>92.57 (-18.36%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>562.30 (n/a)</td><td>457.96 (n/a)</td><td>512.90 (n/a)</td><td>293.80 (n/a)</td><td>113.40 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 <b>(-21.50%)</b></td><td>0.05 (-3.97%)</td><td>0.05 (-2.70%)</td><td>0.03 (+2.69%)</td><td>0.01 <b>(-45.63%)</b></td><td>511.30 (-2.61%)</td><td>334.74 (-5.68%)</td><td>302.50 (+2.75%)</td><td>246.70 <b>(+27.36%)</b></td><td>102.63 <b>(-34.43%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>525.00 (n/a)</td><td>354.90 (n/a)</td><td>294.40 (n/a)</td><td>193.70 (n/a)</td><td>156.52 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (-7.37%)</td><td>0.06 (-4.52%)</td><td>0.06 (-10.67%)</td><td>0.04 <b>(+25.11%)</b></td><td>0.02 <b>(-25.38%)</b></td><td>463.60 <b>(-20.07%)</b></td><td>348.02 (-1.33%)</td><td>353.60 (+11.93%)</td><td>244.90 (+7.93%)</td><td>95.54 <b>(-34.75%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>580.00 (n/a)</td><td>352.70 (n/a)</td><td>315.90 (n/a)</td><td>226.90 (n/a)</td><td>146.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (+0.07%)</td><td>0.05 (-5.63%)</td><td>0.05 (-11.90%)</td><td>0.04 (+14.66%)</td><td>0.01 <b>(-20.95%)</b></td><td>433.60 (-12.79%)</td><td>319.90 (+2.74%)</td><td>312.00 (+13.50%)</td><td>244.80 (-0.08%)</td><td>70.57 <b>(-32.74%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>497.20 (n/a)</td><td>311.38 (n/a)</td><td>274.90 (n/a)</td><td>245.00 (n/a)</td><td>104.92 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (-1.22%)</td><td>0.05 (-2.79%)</td><td>0.06 (+13.22%)</td><td>0.03 (-6.13%)</td><td>0.02 (+0.42%)</td><td>607.30 (+6.53%)</td><td>420.58 (+4.45%)</td><td>357.30 (-11.67%)</td><td>243.60 (+1.25%)</td><td>161.93 (+15.34%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>570.10 (n/a)</td><td>402.68 (n/a)</td><td>404.50 (n/a)</td><td>240.60 (n/a)</td><td>140.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (+3.55%)</td><td>0.04 (-18.43%)</td><td>0.04 <b>(-33.54%)</b></td><td>0.02 (-16.85%)</td><td>0.02 (+0.78%)</td><td>692.70 <b>(+20.26%)</b></td><td>450.46 <b>(+23.85%)</b></td><td>447.70 <b>(+50.44%)</b></td><td>225.30 (-3.43%)</td><td>170.75 (+13.69%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>576.00 (n/a)</td><td>363.72 (n/a)</td><td>297.60 (n/a)</td><td>233.30 (n/a)</td><td>150.18 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 <b>(+39.68%)</b></td><td>0.07 <b>(+29.82%)</b></td><td>0.06 (-2.77%)</td><td>0.04 <b>(+312.91%)</b></td><td>0.03 (-8.55%)</td><td>475.00 <b>(-75.78%)</b></td><td>299.20 <b>(-52.88%)</b></td><td>293.20 (+2.88%)</td><td>173.30 <b>(-28.39%)</b></td><td>112.41 <b>(-84.91%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1961.30 (n/a)</td><td>635.00 (n/a)</td><td>285.00 (n/a)</td><td>242.00 (n/a)</td><td>745.07 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (-6.20%)</td><td>0.05 (+14.54%)</td><td>0.05 <b>(+61.90%)</b></td><td>0.04 <b>(+30.07%)</b></td><td>0.01 <b>(-28.36%)</b></td><td>456.90 <b>(-23.12%)</b></td><td>345.10 (-19.74%)</td><td>324.10 <b>(-38.24%)</b></td><td>240.40 (+6.65%)</td><td>100.72 <b>(-39.88%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>594.30 (n/a)</td><td>429.96 (n/a)</td><td>524.80 (n/a)</td><td>225.40 (n/a)</td><td>167.55 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.05 <b>(-25.36%)</b></td><td>0.04 (-9.31%)</td><td>0.04 (-11.44%)</td><td>0.04 <b>(+56.13%)</b></td><td>0.01 <b>(-67.42%)</b></td><td>522.60 <b>(-35.95%)</b></td><td>451.36 (-2.75%)</td><td>418.30 (+12.90%)</td><td>389.70 <b>(+33.96%)</b></td><td>61.02 <b>(-71.71%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>815.90 (n/a)</td><td>464.10 (n/a)</td><td>370.50 (n/a)</td><td>290.90 (n/a)</td><td>215.69 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (-13.54%)</td><td>0.04 (+0.58%)</td><td>0.04 (+8.52%)</td><td>0.03 (+8.30%)</td><td>0.01 (-15.50%)</td><td>563.40 (-7.67%)</td><td>428.96 (-2.78%)</td><td>446.10 (-7.85%)</td><td>290.70 (+15.63%)</td><td>130.22 (-10.05%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>610.20 (n/a)</td><td>441.24 (n/a)</td><td>484.10 (n/a)</td><td>251.40 (n/a)</td><td>144.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 <b>(-42.77%)</b></td><td>0.06 <b>(-36.15%)</b></td><td>0.07 <b>(-37.42%)</b></td><td>0.04 (-18.49%)</td><td>0.01 <b>(-54.42%)</b></td><td>830.70 <b>(+22.68%)</b></td><td>569.28 <b>(+46.90%)</b></td><td>490.50 <b>(+59.82%)</b></td><td>449.50 <b>(+74.70%)</b></td><td>159.37 (-6.35%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>677.10 (n/a)</td><td>387.54 (n/a)</td><td>306.90 (n/a)</td><td>257.30 (n/a)</td><td>170.17 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (-16.88%)</td><td>0.06 <b>(-38.34%)</b></td><td>0.06 (-19.91%)</td><td>0.01 <b>(-79.34%)</b></td><td>0.03 <b>(+21.72%)</b></td><td>2504.10 <b>(+383.98%)</b></td><td>928.64 <b>(+145.20%)</b></td><td>519.00 <b>(+24.85%)</b></td><td>321.50 <b>(+20.28%)</b></td><td>897.91 <b>(+735.96%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>517.40 (n/a)</td><td>378.72 (n/a)</td><td>415.70 (n/a)</td><td>267.30 (n/a)</td><td>107.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.11 <b>(-43.77%)</b></td><td>0.09 (-18.90%)</td><td>0.09 (-7.16%)</td><td>0.07 (-2.10%)</td><td>0.01 <b>(-69.19%)</b></td><td>568.30 (+2.14%)</td><td>473.70 (+13.90%)</td><td>472.40 (+7.71%)</td><td>389.30 <b>(+77.84%)</b></td><td>74.20 <b>(-39.55%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>556.40 (n/a)</td><td>415.90 (n/a)</td><td>438.60 (n/a)</td><td>218.90 (n/a)</td><td>122.73 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 <b>(-21.75%)</b></td><td>0.07 <b>(-27.83%)</b></td><td>0.07 <b>(-38.59%)</b></td><td>0.05 <b>(-29.33%)</b></td><td>0.02 <b>(-25.91%)</b></td><td>610.40 <b>(+41.53%)</b></td><td>457.64 <b>(+38.10%)</b></td><td>464.80 <b>(+62.80%)</b></td><td>318.10 <b>(+27.80%)</b></td><td>104.65 <b>(+27.94%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>431.30 (n/a)</td><td>331.38 (n/a)</td><td>285.50 (n/a)</td><td>248.90 (n/a)</td><td>81.80 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 <b>(-34.12%)</b></td><td>0.08 <b>(-35.77%)</b></td><td>0.06 <b>(-47.90%)</b></td><td>0.04 <b>(-36.77%)</b></td><td>0.04 <b>(-25.70%)</b></td><td>1075.30 <b>(+58.16%)</b></td><td>644.58 <b>(+61.30%)</b></td><td>664.00 <b>(+91.96%)</b></td><td>335.60 <b>(+51.79%)</b></td><td>312.49 <b>(+64.98%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>679.90 (n/a)</td><td>399.62 (n/a)</td><td>345.90 (n/a)</td><td>221.10 (n/a)</td><td>189.41 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (+4.36%)</td><td>0.10 <b>(+27.84%)</b></td><td>0.12 <b>(+61.60%)</b></td><td>0.06 <b>(+31.58%)</b></td><td>0.03 (-4.85%)</td><td>527.00 <b>(-24.00%)</b></td><td>353.48 <b>(-24.83%)</b></td><td>284.50 <b>(-38.13%)</b></td><td>236.80 (-4.21%)</td><td>126.48 <b>(-29.60%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>693.40 (n/a)</td><td>470.22 (n/a)</td><td>459.80 (n/a)</td><td>247.20 (n/a)</td><td>179.66 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.16 (-11.70%)</td><td>0.08 (-16.10%)</td><td>0.07 (-7.87%)</td><td>0.01 <b>(-76.85%)</b></td><td>0.05 (+6.32%)</td><td>2490.10 <b>(+331.93%)</b></td><td>851.72 <b>(+87.74%)</b></td><td>553.30 (+8.53%)</td><td>229.10 (+13.25%)</td><td>925.54 <b>(+525.20%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>576.50 (n/a)</td><td>453.68 (n/a)</td><td>509.80 (n/a)</td><td>202.30 (n/a)</td><td>148.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (-14.95%)</td><td>0.08 (-14.91%)</td><td>0.07 (+2.36%)</td><td>0.05 (-12.56%)</td><td>0.03 <b>(-25.95%)</b></td><td>681.60 (+14.36%)</td><td>458.24 (+13.79%)</td><td>456.30 (-2.31%)</td><td>268.30 (+17.57%)</td><td>165.32 (+4.45%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>596.00 (n/a)</td><td>402.72 (n/a)</td><td>467.10 (n/a)</td><td>228.20 (n/a)</td><td>158.28 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 <b>(+52.76%)</b></td><td>0.09 <b>(+25.80%)</b></td><td>0.09 (+16.09%)</td><td>0.06 (+3.98%)</td><td>0.03 <b>(+185.71%)</b></td><td>604.70 (-3.82%)</td><td>438.30 (-13.68%)</td><td>405.40 (-13.85%)</td><td>280.10 <b>(-34.53%)</b></td><td>155.16 <b>(+85.47%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>628.70 (n/a)</td><td>507.76 (n/a)</td><td>470.60 (n/a)</td><td>427.80 (n/a)</td><td>83.66 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (-6.53%)</td><td>0.08 (+4.56%)</td><td>0.09 <b>(+25.13%)</b></td><td>0.07 <b>(+22.61%)</b></td><td>0.01 <b>(-39.33%)</b></td><td>488.70 (-18.44%)</td><td>402.34 (-8.41%)</td><td>374.60 <b>(-20.09%)</b></td><td>320.10 (+6.99%)</td><td>67.94 <b>(-44.72%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>599.20 (n/a)</td><td>439.30 (n/a)</td><td>468.80 (n/a)</td><td>299.20 (n/a)</td><td>122.90 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (-10.75%)</td><td>0.05 (-6.06%)</td><td>0.04 (-2.63%)</td><td>0.03 (-14.72%)</td><td>0.02 (-3.23%)</td><td>651.00 (+17.26%)</td><td>436.02 (+8.07%)</td><td>476.40 (+2.69%)</td><td>266.10 (+12.04%)</td><td>166.41 (+19.21%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>555.20 (n/a)</td><td>403.46 (n/a)</td><td>463.90 (n/a)</td><td>237.50 (n/a)</td><td>139.60 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 <b>(+62.74%)</b></td><td>0.06 <b>(+30.64%)</b></td><td>0.04 (+14.47%)</td><td>0.04 (+8.21%)</td><td>0.02 <b>(+130.47%)</b></td><td>568.80 (-7.59%)</td><td>415.98 (-17.56%)</td><td>476.40 (-12.64%)</td><td>230.30 <b>(-38.55%)</b></td><td>141.68 <b>(+31.16%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>615.50 (n/a)</td><td>504.56 (n/a)</td><td>545.30 (n/a)</td><td>374.80 (n/a)</td><td>108.02 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (-5.90%)</td><td>0.05 <b>(-21.97%)</b></td><td>0.04 <b>(-37.73%)</b></td><td>0.02 <b>(-55.96%)</b></td><td>0.02 <b>(+47.96%)</b></td><td>1066.00 <b>(+127.05%)</b></td><td>559.34 <b>(+54.19%)</b></td><td>560.20 <b>(+60.61%)</b></td><td>275.10 (+6.26%)</td><td>319.98 <b>(+225.27%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>469.50 (n/a)</td><td>362.76 (n/a)</td><td>348.80 (n/a)</td><td>258.90 (n/a)</td><td>98.37 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 (-5.15%)</td><td>0.06 (+11.04%)</td><td>0.06 (-17.23%)</td><td>0.04 <b>(+347.47%)</b></td><td>0.01 <b>(-54.72%)</b></td><td>458.50 <b>(-77.65%)</b></td><td>340.00 <b>(-49.93%)</b></td><td>337.30 <b>(+20.81%)</b></td><td>250.20 (+5.44%)</td><td>81.62 <b>(-89.52%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2051.80 (n/a)</td><td>679.02 (n/a)</td><td>279.20 (n/a)</td><td>237.30 (n/a)</td><td>778.69 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 <b>(+23.16%)</b></td><td>0.05 (-18.11%)</td><td>0.04 <b>(-45.33%)</b></td><td>0.03 <b>(-33.99%)</b></td><td>0.03 <b>(+80.36%)</b></td><td>695.80 <b>(+51.46%)</b></td><td>474.38 <b>(+44.02%)</b></td><td>536.40 <b>(+82.88%)</b></td><td>201.80 (-18.79%)</td><td>216.73 <b>(+131.45%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>459.40 (n/a)</td><td>329.38 (n/a)</td><td>293.30 (n/a)</td><td>248.50 (n/a)</td><td>93.64 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 (+1.89%)</td><td>0.05 (-11.76%)</td><td>0.04 <b>(-45.29%)</b></td><td>0.03 (-13.34%)</td><td>0.03 (+16.96%)</td><td>651.70 (+15.41%)</td><td>455.20 (+19.34%)</td><td>515.60 <b>(+82.77%)</b></td><td>235.20 (-1.84%)</td><td>195.83 <b>(+22.82%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>564.70 (n/a)</td><td>381.44 (n/a)</td><td>282.10 (n/a)</td><td>239.60 (n/a)</td><td>159.45 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (-12.84%)</td><td>0.08 (+6.54%)</td><td>0.08 (+19.51%)</td><td>0.05 (+4.70%)</td><td>0.02 <b>(-22.23%)</b></td><td>508.30 (-4.49%)</td><td>322.40 (-8.23%)</td><td>294.70 (-16.35%)</td><td>243.60 (+14.74%)</td><td>106.04 (-9.23%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>532.20 (n/a)</td><td>351.32 (n/a)</td><td>352.30 (n/a)</td><td>212.30 (n/a)</td><td>116.83 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (+4.79%)</td><td>0.07 (+4.20%)</td><td>0.07 <b>(-23.22%)</b></td><td>0.05 <b>(+289.76%)</b></td><td>0.02 <b>(-35.47%)</b></td><td>514.40 <b>(-74.34%)</b></td><td>379.02 <b>(-42.66%)</b></td><td>360.50 <b>(+30.24%)</b></td><td>239.10 (-4.55%)</td><td>124.15 <b>(-83.64%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2004.80 (n/a)</td><td>660.98 (n/a)</td><td>276.80 (n/a)</td><td>250.50 (n/a)</td><td>758.76 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 (-12.07%)</td><td>0.06 (-11.60%)</td><td>0.05 (-6.67%)</td><td>0.02 <b>(-21.41%)</b></td><td>0.03 (-15.33%)</td><td>1021.40 <b>(+27.25%)</b></td><td>525.32 (+13.94%)</td><td>474.20 (+7.14%)</td><td>248.30 (+13.74%)</td><td>307.84 <b>(+26.62%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>802.70 (n/a)</td><td>461.06 (n/a)</td><td>442.60 (n/a)</td><td>218.30 (n/a)</td><td>243.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 <b>(+57.92%)</b></td><td>0.07 (+12.51%)</td><td>0.06 (+17.72%)</td><td>0.04 (+1.11%)</td><td>0.03 <b>(+84.57%)</b></td><td>597.60 (-1.09%)</td><td>426.82 (-4.25%)</td><td>426.00 (-15.05%)</td><td>195.90 <b>(-36.68%)</b></td><td>152.66 (+17.10%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>604.20 (n/a)</td><td>445.76 (n/a)</td><td>501.50 (n/a)</td><td>309.40 (n/a)</td><td>130.36 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 <b>(-27.89%)</b></td><td>0.08 (+11.46%)</td><td>0.08 <b>(+57.29%)</b></td><td>0.05 (+6.89%)</td><td>0.02 <b>(-50.71%)</b></td><td>501.40 (-6.44%)</td><td>324.22 (-19.86%)</td><td>296.70 <b>(-36.43%)</b></td><td>240.10 <b>(+38.71%)</b></td><td>102.85 <b>(-32.31%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>535.90 (n/a)</td><td>404.56 (n/a)</td><td>466.70 (n/a)</td><td>173.10 (n/a)</td><td>151.95 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.10 <b>(+29.15%)</b></td><td>0.07 <b>(+38.24%)</b></td><td>0.09 <b>(+68.37%)</b></td><td>0.04 <b>(+208.82%)</b></td><td>0.03 (+0.69%)</td><td>623.00 <b>(-67.62%)</b></td><td>375.58 <b>(-46.67%)</b></td><td>279.20 <b>(-40.61%)</b></td><td>244.60 <b>(-22.57%)</b></td><td>162.88 <b>(-76.28%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1924.00 (n/a)</td><td>704.20 (n/a)</td><td>470.10 (n/a)</td><td>315.90 (n/a)</td><td>686.58 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (-11.55%)</td><td>0.04 <b>(-29.68%)</b></td><td>0.04 <b>(-46.00%)</b></td><td>0.03 (+11.97%)</td><td>0.01 <b>(-22.46%)</b></td><td>555.70 (-10.69%)</td><td>450.00 <b>(+34.78%)</b></td><td>504.00 <b>(+85.23%)</b></td><td>268.40 (+13.06%)</td><td>115.41 <b>(-28.69%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>622.20 (n/a)</td><td>333.88 (n/a)</td><td>272.10 (n/a)</td><td>237.40 (n/a)</td><td>161.84 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (-19.24%)</td><td>0.06 (-3.27%)</td><td>0.06 (-14.96%)</td><td>0.04 (+12.26%)</td><td>0.01 <b>(-52.12%)</b></td><td>435.30 (-10.91%)</td><td>310.18 (-5.97%)</td><td>290.60 (+17.60%)</td><td>257.60 <b>(+23.85%)</b></td><td>71.26 <b>(-47.68%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>488.60 (n/a)</td><td>329.88 (n/a)</td><td>247.10 (n/a)</td><td>208.00 (n/a)</td><td>136.20 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (-3.20%)</td><td>0.05 (-17.92%)</td><td>0.04 <b>(-46.12%)</b></td><td>0.03 (-13.48%)</td><td>0.02 (+7.50%)</td><td>588.50 (+15.57%)</td><td>426.14 <b>(+25.81%)</b></td><td>497.30 <b>(+85.63%)</b></td><td>247.00 (+3.30%)</td><td>155.14 <b>(+26.68%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>509.20 (n/a)</td><td>338.72 (n/a)</td><td>267.90 (n/a)</td><td>239.10 (n/a)</td><td>122.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (+6.67%)</td><td>0.05 (+5.57%)</td><td>0.04 (-10.36%)</td><td>0.03 <b>(+254.92%)</b></td><td>0.02 <b>(-26.40%)</b></td><td>587.10 <b>(-71.83%)</b></td><td>414.72 <b>(-40.17%)</b></td><td>456.00 (+11.55%)</td><td>250.20 (-6.26%)</td><td>138.52 <b>(-82.26%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2083.90 (n/a)</td><td>693.18 (n/a)</td><td>408.80 (n/a)</td><td>266.90 (n/a)</td><td>781.00 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.07 (-17.46%)</td><td>0.05 <b>(-22.59%)</b></td><td>0.04 (-18.59%)</td><td>0.04 (-0.74%)</td><td>0.02 <b>(-39.69%)</b></td><td>480.00 (+0.73%)</td><td>414.44 <b>(+20.45%)</b></td><td>467.40 <b>(+22.84%)</b></td><td>247.80 <b>(+21.11%)</b></td><td>97.45 <b>(-24.61%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>476.50 (n/a)</td><td>344.08 (n/a)</td><td>380.50 (n/a)</td><td>204.60 (n/a)</td><td>129.26 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.08 <b>(+30.75%)</b></td><td>0.05 (+8.61%)</td><td>0.04 (+9.69%)</td><td>0.03 (-12.41%)</td><td>0.02 <b>(+56.12%)</b></td><td>643.10 (+14.15%)</td><td>429.22 (-3.41%)</td><td>428.30 (-8.83%)</td><td>236.50 <b>(-23.51%)</b></td><td>144.75 <b>(+31.25%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>563.40 (n/a)</td><td>444.36 (n/a)</td><td>469.80 (n/a)</td><td>309.20 (n/a)</td><td>110.29 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.33 (-17.63%)</td><td>0.29 (-12.23%)</td><td>0.31 (-11.03%)</td><td>0.21 (+10.15%)</td><td>0.05 <b>(-33.96%)</b></td><td>466.70 (-9.22%)</td><td>353.86 (+9.73%)</td><td>314.00 (+12.38%)</td><td>296.30 <b>(+21.38%)</b></td><td>74.85 <b>(-31.89%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.40 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>514.10 (n/a)</td><td>322.48 (n/a)</td><td>279.40 (n/a)</td><td>244.10 (n/a)</td><td>109.90 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.39 (-17.11%)</td><td>0.29 (+5.58%)</td><td>0.33 <b>(+54.81%)</b></td><td>0.10 <b>(-47.19%)</b></td><td>0.12 (+0.04%)</td><td>1013.20 <b>(+89.38%)</b></td><td>438.90 (+9.36%)</td><td>294.80 <b>(-35.39%)</b></td><td>251.00 <b>(+20.62%)</b></td><td>324.97 <b>(+136.16%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.47 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>535.00 (n/a)</td><td>401.34 (n/a)</td><td>456.30 (n/a)</td><td>208.10 (n/a)</td><td>137.61 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.41 <b>(+58.64%)</b></td><td>0.26 <b>(+36.14%)</b></td><td>0.18 (+0.32%)</td><td>0.16 <b>(+70.12%)</b></td><td>0.11 <b>(+79.87%)</b></td><td>603.20 <b>(-41.22%)</b></td><td>440.80 <b>(-25.07%)</b></td><td>533.60 (-0.32%)</td><td>241.50 <b>(-36.96%)</b></td><td>163.44 <b>(-36.19%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>1026.20 (n/a)</td><td>588.28 (n/a)</td><td>535.30 (n/a)</td><td>383.10 (n/a)</td><td>256.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.30 (-10.21%)</td><td>0.19 <b>(-21.35%)</b></td><td>0.17 <b>(-34.69%)</b></td><td>0.13 (-7.35%)</td><td>0.07 (+2.89%)</td><td>571.60 (+7.93%)</td><td>422.32 <b>(+29.45%)</b></td><td>441.40 <b>(+53.10%)</b></td><td>246.50 (+11.34%)</td><td>139.39 (+17.54%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>529.60 (n/a)</td><td>326.24 (n/a)</td><td>288.30 (n/a)</td><td>221.40 (n/a)</td><td>118.59 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.31 (+14.40%)</td><td>0.21 (+11.44%)</td><td>0.17 (+1.77%)</td><td>0.16 (+17.87%)</td><td>0.07 (+17.55%)</td><td>472.90 (-15.16%)</td><td>375.18 (-9.96%)</td><td>427.80 (-1.75%)</td><td>235.30 (-12.59%)</td><td>102.20 (-11.31%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>557.40 (n/a)</td><td>416.70 (n/a)</td><td>435.40 (n/a)</td><td>269.20 (n/a)</td><td>115.24 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.29 (-3.12%)</td><td>0.19 (+6.79%)</td><td>0.17 <b>(-21.01%)</b></td><td>0.11 <b>(+265.57%)</b></td><td>0.08 <b>(-30.66%)</b></td><td>663.80 <b>(-72.65%)</b></td><td>433.98 <b>(-45.54%)</b></td><td>441.20 <b>(+26.60%)</b></td><td>251.10 (+3.21%)</td><td>166.41 <b>(-82.02%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>0.11 (n/a)</td><td>2426.70 (n/a)</td><td>796.88 (n/a)</td><td>348.50 (n/a)</td><td>243.30 (n/a)</td><td>925.51 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (-8.79%)</td><td>0.10 (-0.17%)</td><td>0.11 <b>(+23.39%)</b></td><td>0.07 (-9.02%)</td><td>0.03 (-16.35%)</td><td>541.80 (+9.92%)</td><td>377.26 (-0.98%)</td><td>321.90 (-18.96%)</td><td>280.10 (+9.63%)</td><td>110.46 (+0.42%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>492.90 (n/a)</td><td>380.98 (n/a)</td><td>397.20 (n/a)</td><td>255.50 (n/a)</td><td>110.00 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.19 (+17.00%)</td><td>0.12 <b>(+26.44%)</b></td><td>0.14 <b>(+99.57%)</b></td><td>0.07 <b>(+21.76%)</b></td><td>0.05 (+7.04%)</td><td>509.80 (-17.88%)</td><td>346.70 <b>(-22.47%)</b></td><td>266.80 <b>(-49.89%)</b></td><td>195.90 (-14.57%)</td><td>150.95 (-17.37%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>620.80 (n/a)</td><td>447.20 (n/a)</td><td>532.40 (n/a)</td><td>229.30 (n/a)</td><td>182.68 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (-0.77%)</td><td>0.11 (+11.92%)</td><td>0.08 (-2.48%)</td><td>0.07 <b>(+386.65%)</b></td><td>0.04 <b>(-34.26%)</b></td><td>492.40 <b>(-79.45%)</b></td><td>383.32 <b>(-49.92%)</b></td><td>455.60 (+2.54%)</td><td>242.20 (+0.75%)</td><td>119.06 <b>(-87.03%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2396.10 (n/a)</td><td>765.48 (n/a)</td><td>444.30 (n/a)</td><td>240.40 (n/a)</td><td>918.22 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 <b>(-32.47%)</b></td><td>0.12 (-5.37%)</td><td>0.13 (-5.04%)</td><td>0.07 (+9.17%)</td><td>0.03 <b>(-49.57%)</b></td><td>533.20 (-8.42%)</td><td>332.00 (-7.80%)</td><td>288.00 (+5.30%)</td><td>246.10 <b>(+48.07%)</b></td><td>117.86 <b>(-35.03%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>582.20 (n/a)</td><td>360.10 (n/a)</td><td>273.50 (n/a)</td><td>166.20 (n/a)</td><td>181.39 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (-0.22%)</td><td>0.11 (+17.81%)</td><td>0.09 (+5.93%)</td><td>0.07 (+11.72%)</td><td>0.04 (+4.13%)</td><td>558.60 (-10.50%)</td><td>385.26 (-15.86%)</td><td>413.10 (-5.60%)</td><td>246.20 (+0.24%)</td><td>133.73 (-13.86%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>624.10 (n/a)</td><td>457.90 (n/a)</td><td>437.60 (n/a)</td><td>245.60 (n/a)</td><td>155.25 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (-18.02%)</td><td>0.09 (-5.13%)</td><td>0.07 (-1.53%)</td><td>0.07 (+12.38%)</td><td>0.03 <b>(-30.85%)</b></td><td>533.60 (-11.02%)</td><td>432.38 (-0.25%)</td><td>504.20 (+1.55%)</td><td>299.70 <b>(+21.98%)</b></td><td>115.70 <b>(-24.76%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>599.70 (n/a)</td><td>433.46 (n/a)</td><td>496.50 (n/a)</td><td>245.70 (n/a)</td><td>153.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.16 (-2.88%)</td><td>0.09 (-11.65%)</td><td>0.08 (-6.28%)</td><td>0.05 <b>(-24.03%)</b></td><td>0.04 (+0.11%)</td><td>749.90 <b>(+31.63%)</b></td><td>494.72 (+16.05%)</td><td>521.00 (+6.70%)</td><td>259.10 (+2.98%)</td><td>183.44 <b>(+31.78%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>569.70 (n/a)</td><td>426.30 (n/a)</td><td>488.30 (n/a)</td><td>251.60 (n/a)</td><td>139.20 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.16 (+15.71%)</td><td>0.12 <b>(+26.09%)</b></td><td>0.13 <b>(+49.00%)</b></td><td>0.08 (+12.21%)</td><td>0.03 <b>(+23.81%)</b></td><td>507.90 (-10.88%)</td><td>362.24 (-19.74%)</td><td>311.20 <b>(-32.90%)</b></td><td>253.50 (-13.57%)</td><td>109.09 (-2.44%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>569.90 (n/a)</td><td>451.36 (n/a)</td><td>463.80 (n/a)</td><td>293.30 (n/a)</td><td>111.82 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.17 (-10.01%)</td><td>0.10 (-0.41%)</td><td>0.08 (+9.54%)</td><td>0.06 (-4.01%)</td><td>0.04 (-15.69%)</td><td>639.40 (+4.19%)</td><td>480.28 (-1.47%)</td><td>489.80 (-8.70%)</td><td>244.80 (+11.12%)</td><td>163.05 (+3.99%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>613.70 (n/a)</td><td>487.46 (n/a)</td><td>536.50 (n/a)</td><td>220.30 (n/a)</td><td>156.79 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.16 (-1.04%)</td><td>0.10 (-11.35%)</td><td>0.11 (+8.00%)</td><td>0.02 <b>(-66.54%)</b></td><td>0.05 <b>(+33.34%)</b></td><td>1884.80 <b>(+198.84%)</b></td><td>680.20 <b>(+63.96%)</b></td><td>379.10 (-7.42%)</td><td>253.80 (+1.04%)</td><td>680.98 <b>(+357.23%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>630.70 (n/a)</td><td>414.86 (n/a)</td><td>409.50 (n/a)</td><td>251.20 (n/a)</td><td>148.93 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.17 (+9.38%)</td><td>0.10 (+8.19%)</td><td>0.09 (+10.34%)</td><td>0.06 (+16.36%)</td><td>0.04 (+9.54%)</td><td>643.90 (-14.05%)</td><td>467.12 (-7.75%)</td><td>440.50 (-9.38%)</td><td>236.50 (-8.55%)</td><td>166.05 (-11.08%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>749.20 (n/a)</td><td>506.36 (n/a)</td><td>486.10 (n/a)</td><td>258.60 (n/a)</td><td>186.75 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.15 (-10.94%)</td><td>0.11 <b>(+21.16%)</b></td><td>0.09 (+12.66%)</td><td>0.07 <b>(+260.90%)</b></td><td>0.03 <b>(-44.97%)</b></td><td>550.70 <b>(-72.29%)</b></td><td>412.06 <b>(-45.36%)</b></td><td>434.60 (-11.25%)</td><td>268.00 (+12.27%)</td><td>106.06 <b>(-84.90%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1987.60 (n/a)</td><td>754.14 (n/a)</td><td>489.70 (n/a)</td><td>238.70 (n/a)</td><td>702.43 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.17 <b>(+33.41%)</b></td><td>0.12 <b>(+31.89%)</b></td><td>0.12 <b>(+87.90%)</b></td><td>0.06 (-5.95%)</td><td>0.04 (+15.96%)</td><td>614.30 (+6.32%)</td><td>342.94 <b>(-23.14%)</b></td><td>284.80 <b>(-46.79%)</b></td><td>208.80 <b>(-25.05%)</b></td><td>157.30 (+2.71%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>577.80 (n/a)</td><td>446.20 (n/a)</td><td>535.20 (n/a)</td><td>278.60 (n/a)</td><td>153.15 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (-17.96%)</td><td>0.10 (+12.63%)</td><td>0.10 <b>(+36.33%)</b></td><td>0.06 <b>(+25.53%)</b></td><td>0.02 <b>(-44.99%)</b></td><td>581.40 <b>(-20.33%)</b></td><td>377.80 <b>(-20.51%)</b></td><td>342.80 <b>(-26.64%)</b></td><td>297.10 <b>(+21.91%)</b></td><td>115.49 <b>(-43.64%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>729.80 (n/a)</td><td>475.30 (n/a)</td><td>467.30 (n/a)</td><td>243.70 (n/a)</td><td>204.92 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (-19.44%)</td><td>0.10 (-4.13%)</td><td>0.12 <b>(+31.19%)</b></td><td>0.05 (-17.34%)</td><td>0.04 (-14.31%)</td><td>697.60 <b>(+20.99%)</b></td><td>396.06 (+5.66%)</td><td>290.60 <b>(-23.77%)</b></td><td>252.70 <b>(+24.12%)</b></td><td>192.76 <b>(+26.57%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>576.60 (n/a)</td><td>374.86 (n/a)</td><td>381.20 (n/a)</td><td>203.60 (n/a)</td><td>152.30 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (-5.30%)</td><td>0.11 (+7.08%)</td><td>0.13 <b>(+47.14%)</b></td><td>0.06 (+1.48%)</td><td>0.04 (-7.89%)</td><td>549.20 (-1.45%)</td><td>364.24 (-7.64%)</td><td>275.90 <b>(-32.04%)</b></td><td>241.20 (+5.60%)</td><td>143.75 (-2.63%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>557.30 (n/a)</td><td>394.38 (n/a)</td><td>406.00 (n/a)</td><td>228.40 (n/a)</td><td>147.64 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (+8.50%)</td><td>0.10 (+4.53%)</td><td>0.08 (-2.40%)</td><td>0.07 (+10.70%)</td><td>0.03 (+17.78%)</td><td>494.90 (-9.67%)</td><td>386.62 (-3.02%)</td><td>437.90 (+2.48%)</td><td>246.90 (-7.84%)</td><td>115.41 (+1.30%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>547.90 (n/a)</td><td>398.64 (n/a)</td><td>427.30 (n/a)</td><td>267.90 (n/a)</td><td>113.93 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.14 (-1.61%)</td><td>0.09 (+12.84%)</td><td>0.09 <b>(+40.57%)</b></td><td>0.02 <b>(-63.32%)</b></td><td>0.05 <b>(+24.34%)</b></td><td>1633.90 <b>(+172.63%)</b></td><td>609.02 <b>(+22.11%)</b></td><td>390.40 <b>(-28.86%)</b></td><td>244.70 (+1.62%)</td><td>579.96 <b>(+295.14%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>599.30 (n/a)</td><td>498.74 (n/a)</td><td>548.80 (n/a)</td><td>240.80 (n/a)</td><td>146.77 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.52 (+9.94%)</td><td>0.39 <b>(+45.09%)</b></td><td>0.42 <b>(+80.01%)</b></td><td>0.26 <b>(+321.87%)</b></td><td>0.12 <b>(-34.58%)</b></td><td>501.80 <b>(-76.29%)</b></td><td>362.20 <b>(-56.16%)</b></td><td>315.10 <b>(-44.45%)</b></td><td>253.10 (-9.02%)</td><td>114.76 <b>(-84.89%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.47 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>0.18 (n/a)</td><td>2116.80 (n/a)</td><td>826.28 (n/a)</td><td>567.20 (n/a)</td><td>278.20 (n/a)</td><td>759.59 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.45 (-7.46%)</td><td>0.27 (-7.16%)</td><td>0.29 <b>(+23.07%)</b></td><td>0.12 <b>(+128.09%)</b></td><td>0.12 <b>(-32.51%)</b></td><td>1079.80 <b>(-56.16%)</b></td><td>578.60 <b>(-29.87%)</b></td><td>446.80 (-18.75%)</td><td>293.50 (+8.06%)</td><td>304.36 <b>(-67.13%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.48 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>0.18 (n/a)</td><td>2462.90 (n/a)</td><td>825.04 (n/a)</td><td>549.90 (n/a)</td><td>271.60 (n/a)</td><td>925.87 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.41 (-11.77%)</td><td>0.30 (-1.33%)</td><td>0.28 (+14.82%)</td><td>0.19 (+10.88%)</td><td>0.08 <b>(-42.66%)</b></td><td>678.60 (-9.81%)</td><td>465.26 (-8.52%)</td><td>468.80 (-12.89%)</td><td>323.00 (+13.33%)</td><td>134.58 <b>(-37.14%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.46 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>752.40 (n/a)</td><td>508.60 (n/a)</td><td>538.20 (n/a)</td><td>285.00 (n/a)</td><td>214.11 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.00 <b>(+40.00%)</b></td><td>0.00 <b>(+41.18%)</b></td><td>0.00 <b>(+66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+26.83%)</b></td><td>20264.55 (-2.44%)</td><td>10068.04 <b>(-29.13%)</b></td><td>8374.56 <b>(-47.81%)</b></td><td>5531.14 <b>(-25.78%)</b></td><td>5925.37 (-3.71%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20770.83 (n/a)</td><td>14205.58 (n/a)</td><td>16046.19 (n/a)</td><td>7452.84 (n/a)</td><td>6153.67 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.00 <b>(+116.67%)</b></td><td>0.00 <b>(+30.43%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+340.17%)</b></td><td>22018.75 (-2.49%)</td><td>16792.61 (-8.47%)</td><td>19115.42 (+2.77%)</td><td>6282.33 <b>(-56.63%)</b></td><td>6131.27 <b>(+99.55%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22581.70 (n/a)</td><td>18347.28 (n/a)</td><td>18600.42 (n/a)</td><td>14484.71 (n/a)</td><td>3072.58 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.09 <b>(-43.76%)</b></td><td>0.08 (-18.44%)</td><td>0.07 (-13.11%)</td><td>0.07 (+3.39%)</td><td>0.01 <b>(-76.07%)</b></td><td>29871.90 (-3.32%)</td><td>27274.12 (+14.14%)</td><td>28256.87 (+15.01%)</td><td>23871.04 <b>(+77.95%)</b></td><td>2847.54 <b>(-55.82%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>30896.59 (n/a)</td><td>23896.05 (n/a)</td><td>24569.85 (n/a)</td><td>13414.36 (n/a)</td><td>6444.59 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>2.50 <b>(-23.00%)</b></td><td>1.90 (-5.15%)</td><td>1.78 <b>(-27.70%)</b></td><td>1.38 <b>(+342.31%)</b></td><td>0.49 <b>(-60.82%)</b></td><td>757.90 <b>(-77.39%)</b></td><td>581.82 <b>(-46.23%)</b></td><td>589.50 <b>(+38.32%)</b></td><td>419.80 <b>(+29.85%)</b></td><td>145.73 <b>(-88.74%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.24 (n/a)</td><td>2.00 (n/a)</td><td>2.46 (n/a)</td><td>0.31 (n/a)</td><td>1.24 (n/a)</td><td>3352.30 (n/a)</td><td>1082.14 (n/a)</td><td>426.20 (n/a)</td><td>323.30 (n/a)</td><td>1293.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>2.48 <b>(-37.78%)</b></td><td>1.09 <b>(-46.08%)</b></td><td>0.30 <b>(-79.47%)</b></td><td>0.30 <b>(-78.44%)</b></td><td>1.09 (-2.75%)</td><td>3553.70 <b>(+363.81%)</b></td><td>2306.80 <b>(+276.31%)</b></td><td>3503.80 <b>(+387.18%)</b></td><td>422.60 <b>(+60.75%)</b></td><td>1680.89 <b>(+691.02%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.99 (n/a)</td><td>2.01 (n/a)</td><td>1.46 (n/a)</td><td>1.37 (n/a)</td><td>1.12 (n/a)</td><td>766.20 (n/a)</td><td>613.00 (n/a)</td><td>719.20 (n/a)</td><td>262.90 (n/a)</td><td>212.50 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>4.08 <b>(+50.98%)</b></td><td>2.62 <b>(+56.94%)</b></td><td>2.49 <b>(+45.13%)</b></td><td>1.59 <b>(+398.57%)</b></td><td>1.03 (+18.60%)</td><td>659.10 <b>(-79.94%)</b></td><td>453.28 <b>(-58.57%)</b></td><td>421.70 <b>(-31.09%)</b></td><td>256.90 <b>(-33.75%)</b></td><td>172.07 <b>(-86.01%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>2.70 (n/a)</td><td>1.67 (n/a)</td><td>1.71 (n/a)</td><td>0.32 (n/a)</td><td>0.87 (n/a)</td><td>3285.90 (n/a)</td><td>1094.04 (n/a)</td><td>612.00 (n/a)</td><td>387.80 (n/a)</td><td>1229.98 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.69 (-15.19%)</td><td>2.07 <b>(-28.12%)</b></td><td>2.56 (-11.68%)</td><td>0.29 <b>(-82.80%)</b></td><td>1.33 <b>(+32.10%)</b></td><td>3556.90 <b>(+481.48%)</b></td><td>1107.48 <b>(+174.77%)</b></td><td>409.90 (+13.23%)</td><td>283.80 (+17.91%)</td><td>1388.38 <b>(+871.54%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>4.36 (n/a)</td><td>2.87 (n/a)</td><td>2.90 (n/a)</td><td>1.71 (n/a)</td><td>1.01 (n/a)</td><td>611.70 (n/a)</td><td>403.06 (n/a)</td><td>362.00 (n/a)</td><td>240.70 (n/a)</td><td>142.90 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>1.93 <b>(-54.40%)</b></td><td>1.08 <b>(-51.22%)</b></td><td>1.03 <b>(-52.19%)</b></td><td>0.59 (+2.83%)</td><td>0.55 <b>(-66.74%)</b></td><td>3530.60 (-2.75%)</td><td>2348.48 <b>(+30.79%)</b></td><td>2031.20 <b>(+109.19%)</b></td><td>1086.40 <b>(+119.30%)</b></td><td>1067.31 <b>(-30.15%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>4.23 (n/a)</td><td>2.21 (n/a)</td><td>2.16 (n/a)</td><td>0.58 (n/a)</td><td>1.64 (n/a)</td><td>3630.60 (n/a)</td><td>1795.58 (n/a)</td><td>971.00 (n/a)</td><td>495.40 (n/a)</td><td>1528.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.02 (-14.58%)</td><td>3.40 (-11.29%)</td><td>3.16 (-13.71%)</td><td>1.95 <b>(+123.63%)</b></td><td>1.23 <b>(-36.38%)</b></td><td>1077.20 <b>(-55.28%)</b></td><td>689.20 <b>(-20.44%)</b></td><td>664.10 (+15.90%)</td><td>417.90 (+17.06%)</td><td>261.37 <b>(-69.90%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>5.87 (n/a)</td><td>3.84 (n/a)</td><td>3.66 (n/a)</td><td>0.87 (n/a)</td><td>1.93 (n/a)</td><td>2408.90 (n/a)</td><td>866.22 (n/a)</td><td>573.00 (n/a)</td><td>357.00 (n/a)</td><td>868.46 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.58 (-7.12%)</td><td>3.44 <b>(+24.52%)</b></td><td>3.00 <b>(+31.23%)</b></td><td>2.51 <b>(+325.66%)</b></td><td>1.26 <b>(-41.77%)</b></td><td>834.90 <b>(-76.51%)</b></td><td>662.78 <b>(-53.21%)</b></td><td>698.40 <b>(-23.80%)</b></td><td>376.10 (+7.64%)</td><td>185.53 <b>(-85.72%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.00 (n/a)</td><td>2.76 (n/a)</td><td>2.29 (n/a)</td><td>0.59 (n/a)</td><td>2.16 (n/a)</td><td>3553.60 (n/a)</td><td>1416.42 (n/a)</td><td>916.50 (n/a)</td><td>349.40 (n/a)</td><td>1299.28 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>7.22 (+0.27%)</td><td>3.18 <b>(-23.59%)</b></td><td>1.72 <b>(-64.85%)</b></td><td>0.60 (+3.27%)</td><td>2.90 (+13.20%)</td><td>3474.60 (-3.17%)</td><td>1463.48 <b>(+33.59%)</b></td><td>1216.20 <b>(+184.49%)</b></td><td>290.50 (-0.27%)</td><td>1307.35 (-7.01%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>7.20 (n/a)</td><td>4.16 (n/a)</td><td>4.91 (n/a)</td><td>0.58 (n/a)</td><td>2.57 (n/a)</td><td>3588.40 (n/a)</td><td>1095.48 (n/a)</td><td>427.50 (n/a)</td><td>291.30 (n/a)</td><td>1405.91 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>5.40 (-4.08%)</td><td>3.72 (-11.75%)</td><td>4.48 (+10.70%)</td><td>1.07 <b>(-46.82%)</b></td><td>1.77 (+18.03%)</td><td>1955.20 <b>(+88.04%)</b></td><td>799.00 <b>(+39.57%)</b></td><td>467.80 (-9.67%)</td><td>388.30 (+4.27%)</td><td>661.44 <b>(+141.33%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>5.63 (n/a)</td><td>4.21 (n/a)</td><td>4.05 (n/a)</td><td>2.02 (n/a)</td><td>1.50 (n/a)</td><td>1039.80 (n/a)</td><td>572.48 (n/a)</td><td>517.90 (n/a)</td><td>372.40 (n/a)</td><td>274.08 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>6.80 (-5.88%)</td><td>3.58 (-20.00%)</td><td>3.89 (+5.80%)</td><td>0.87 <b>(-66.60%)</b></td><td>2.42 <b>(+20.49%)</b></td><td>2398.30 <b>(+199.38%)</b></td><td>1009.18 <b>(+84.70%)</b></td><td>539.10 (-5.49%)</td><td>308.50 (+6.23%)</td><td>879.46 <b>(+296.45%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>7.22 (n/a)</td><td>4.47 (n/a)</td><td>3.68 (n/a)</td><td>2.62 (n/a)</td><td>2.01 (n/a)</td><td>801.10 (n/a)</td><td>546.38 (n/a)</td><td>570.40 (n/a)</td><td>290.40 (n/a)</td><td>221.83 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>4.66 (-15.97%)</td><td>4.01 (+12.28%)</td><td>4.00 (+2.38%)</td><td>3.32 <b>(+67.35%)</b></td><td>0.47 <b>(-69.58%)</b></td><td>1263.30 <b>(-40.24%)</b></td><td>1058.52 <b>(-24.37%)</b></td><td>1047.80 (-2.33%)</td><td>900.40 (+19.02%)</td><td>130.39 <b>(-80.19%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>5.54 (n/a)</td><td>3.57 (n/a)</td><td>3.91 (n/a)</td><td>1.98 (n/a)</td><td>1.56 (n/a)</td><td>2114.10 (n/a)</td><td>1399.54 (n/a)</td><td>1072.80 (n/a)</td><td>756.50 (n/a)</td><td>658.32 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>7.40 (+7.01%)</td><td>5.35 (+13.46%)</td><td>5.87 <b>(+34.01%)</b></td><td>3.11 <b>(+53.65%)</b></td><td>1.72 (-8.42%)</td><td>1348.10 <b>(-34.92%)</b></td><td>864.38 (-18.83%)</td><td>714.00 <b>(-25.38%)</b></td><td>566.50 (-6.55%)</td><td>318.56 <b>(-45.65%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.92 (n/a)</td><td>4.71 (n/a)</td><td>4.38 (n/a)</td><td>2.02 (n/a)</td><td>1.88 (n/a)</td><td>2071.40 (n/a)</td><td>1064.86 (n/a)</td><td>956.80 (n/a)</td><td>606.20 (n/a)</td><td>586.13 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>7.33 (-8.43%)</td><td>5.47 (-4.34%)</td><td>5.53 <b>(-23.84%)</b></td><td>3.43 <b>(+100.34%)</b></td><td>1.40 <b>(-50.83%)</b></td><td>1224.00 <b>(-50.09%)</b></td><td>815.10 <b>(-21.80%)</b></td><td>758.40 <b>(+31.30%)</b></td><td>572.10 (+9.20%)</td><td>244.24 <b>(-70.49%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>8.01 (n/a)</td><td>5.72 (n/a)</td><td>7.26 (n/a)</td><td>1.71 (n/a)</td><td>2.84 (n/a)</td><td>2452.30 (n/a)</td><td>1042.28 (n/a)</td><td>577.60 (n/a)</td><td>523.90 (n/a)</td><td>827.68 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>10.61 (+2.66%)</td><td>7.01 (-6.50%)</td><td>7.92 <b>(+20.89%)</b></td><td>1.25 <b>(-80.12%)</b></td><td>3.99 <b>(+133.83%)</b></td><td>3350.20 <b>(+403.11%)</b></td><td>1109.12 <b>(+91.54%)</b></td><td>529.30 (-17.28%)</td><td>395.30 (-2.59%)</td><td>1267.57 <b>(+1049.57%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>10.34 (n/a)</td><td>7.50 (n/a)</td><td>6.55 (n/a)</td><td>6.30 (n/a)</td><td>1.71 (n/a)</td><td>665.90 (n/a)</td><td>579.06 (n/a)</td><td>639.90 (n/a)</td><td>405.80 (n/a)</td><td>110.27 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>9.90 <b>(+49.92%)</b></td><td>6.43 <b>(+70.14%)</b></td><td>6.44 <b>(+104.46%)</b></td><td>3.62 <b>(+216.62%)</b></td><td>2.30 (-8.94%)</td><td>1158.20 <b>(-68.42%)</b></td><td>725.96 <b>(-58.31%)</b></td><td>651.80 <b>(-51.09%)</b></td><td>423.70 <b>(-33.30%)</b></td><td>273.29 <b>(-78.85%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>6.60 (n/a)</td><td>3.78 (n/a)</td><td>3.15 (n/a)</td><td>1.14 (n/a)</td><td>2.53 (n/a)</td><td>3667.20 (n/a)</td><td>1741.16 (n/a)</td><td>1332.60 (n/a)</td><td>635.20 (n/a)</td><td>1292.10 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>6.25 <b>(-37.36%)</b></td><td>4.37 <b>(-35.52%)</b></td><td>4.08 <b>(-38.49%)</b></td><td>3.49 <b>(+54.74%)</b></td><td>1.08 <b>(-62.95%)</b></td><td>1201.90 <b>(-35.37%)</b></td><td>997.44 <b>(+23.20%)</b></td><td>1029.10 <b>(+62.58%)</b></td><td>671.40 <b>(+59.63%)</b></td><td>197.21 <b>(-66.84%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>9.97 (n/a)</td><td>6.78 (n/a)</td><td>6.63 (n/a)</td><td>2.26 (n/a)</td><td>2.91 (n/a)</td><td>1859.80 (n/a)</td><td>809.62 (n/a)</td><td>633.00 (n/a)</td><td>420.60 (n/a)</td><td>594.70 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>1.29 (-14.56%)</td><td>0.79 <b>(-33.87%)</b></td><td>0.87 <b>(-33.44%)</b></td><td>0.15 <b>(-81.35%)</b></td><td>0.41 <b>(+20.94%)</b></td><td>3423.10 <b>(+436.28%)</b></td><td>1140.38 <b>(+143.29%)</b></td><td>604.50 <b>(+50.22%)</b></td><td>406.40 (+17.05%)</td><td>1279.89 <b>(+794.79%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>1.51 (n/a)</td><td>1.20 (n/a)</td><td>1.30 (n/a)</td><td>0.82 (n/a)</td><td>0.34 (n/a)</td><td>638.30 (n/a)</td><td>468.74 (n/a)</td><td>402.40 (n/a)</td><td>347.20 (n/a)</td><td>143.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>2.59 (-9.06%)</td><td>1.55 <b>(-33.82%)</b></td><td>1.31 <b>(-45.99%)</b></td><td>0.44 <b>(-75.20%)</b></td><td>0.92 <b>(+84.65%)</b></td><td>2372.40 <b>(+303.26%)</b></td><td>1011.94 <b>(+117.73%)</b></td><td>802.00 <b>(+85.13%)</b></td><td>405.30 (+9.96%)</td><td>806.12 <b>(+680.05%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>2.84 (n/a)</td><td>2.34 (n/a)</td><td>2.42 (n/a)</td><td>1.78 (n/a)</td><td>0.50 (n/a)</td><td>588.30 (n/a)</td><td>464.76 (n/a)</td><td>433.20 (n/a)</td><td>368.60 (n/a)</td><td>103.34 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>3.89 <b>(+23.19%)</b></td><td>2.25 <b>(+25.75%)</b></td><td>2.34 <b>(+21.79%)</b></td><td>0.58 (+0.53%)</td><td>1.43 <b>(+20.64%)</b></td><td>3596.40 (-0.53%)</td><td>1526.06 <b>(-21.29%)</b></td><td>894.30 (-17.89%)</td><td>538.90 (-18.83%)</td><td>1292.83 (-14.27%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>3.16 (n/a)</td><td>1.79 (n/a)</td><td>1.93 (n/a)</td><td>0.58 (n/a)</td><td>1.18 (n/a)</td><td>3615.40 (n/a)</td><td>1938.86 (n/a)</td><td>1089.20 (n/a)</td><td>663.90 (n/a)</td><td>1507.99 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>1.59 (-8.89%)</td><td>1.10 <b>(-27.55%)</b></td><td>0.95 <b>(-41.70%)</b></td><td>0.73 <b>(-27.08%)</b></td><td>0.34 (+15.71%)</td><td>720.50 <b>(+37.16%)</b></td><td>514.14 <b>(+42.75%)</b></td><td>554.10 <b>(+71.49%)</b></td><td>330.70 (+9.76%)</td><td>152.29 <b>(+63.83%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>1.74 (n/a)</td><td>1.52 (n/a)</td><td>1.62 (n/a)</td><td>1.00 (n/a)</td><td>0.30 (n/a)</td><td>525.30 (n/a)</td><td>360.16 (n/a)</td><td>323.10 (n/a)</td><td>301.30 (n/a)</td><td>92.96 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.12 (-13.42%)</td><td>0.07 <b>(-23.68%)</b></td><td>0.06 <b>(-37.57%)</b></td><td>0.02 <b>(-67.34%)</b></td><td>0.04 (+6.19%)</td><td>1939.20 <b>(+206.16%)</b></td><td>744.34 <b>(+76.32%)</b></td><td>565.20 <b>(+60.16%)</b></td><td>270.20 (+15.52%)</td><td>680.78 <b>(+284.82%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>633.40 (n/a)</td><td>422.16 (n/a)</td><td>352.90 (n/a)</td><td>233.90 (n/a)</td><td>176.91 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.13 (-10.18%)</td><td>0.08 (-13.82%)</td><td>0.07 (-14.43%)</td><td>0.06 <b>(+93.82%)</b></td><td>0.03 <b>(-42.27%)</b></td><td>562.40 <b>(-48.40%)</b></td><td>442.44 (-9.28%)</td><td>454.20 (+16.85%)</td><td>254.90 (+11.31%)</td><td>114.13 <b>(-67.81%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1090.00 (n/a)</td><td>487.70 (n/a)</td><td>388.70 (n/a)</td><td>229.00 (n/a)</td><td>354.54 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.27 (+9.88%)</td><td>0.15 (-7.38%)</td><td>0.14 (-4.99%)</td><td>0.11 (-13.86%)</td><td>0.06 <b>(+29.26%)</b></td><td>602.20 (+16.10%)</td><td>465.52 (+11.82%)</td><td>484.80 (+5.25%)</td><td>246.30 (-8.98%)</td><td>132.43 <b>(+25.92%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>518.70 (n/a)</td><td>416.30 (n/a)</td><td>460.60 (n/a)</td><td>270.60 (n/a)</td><td>105.18 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.29 (+10.41%)</td><td>0.18 (-18.29%)</td><td>0.13 <b>(-41.76%)</b></td><td>0.11 <b>(-22.61%)</b></td><td>0.08 <b>(+79.21%)</b></td><td>585.90 <b>(+29.20%)</b></td><td>426.60 <b>(+34.18%)</b></td><td>506.80 <b>(+71.68%)</b></td><td>229.60 (-9.43%)</td><td>154.53 <b>(+98.39%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>453.50 (n/a)</td><td>317.94 (n/a)</td><td>295.20 (n/a)</td><td>253.50 (n/a)</td><td>77.89 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.23 (-7.55%)</td><td>0.17 (+8.17%)</td><td>0.18 <b>(+21.57%)</b></td><td>0.12 <b>(+38.28%)</b></td><td>0.04 <b>(-24.57%)</b></td><td>538.70 <b>(-27.68%)</b></td><td>410.86 (-12.43%)</td><td>372.30 (-17.74%)</td><td>290.60 (+8.15%)</td><td>106.46 <b>(-39.18%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>744.90 (n/a)</td><td>469.16 (n/a)</td><td>452.60 (n/a)</td><td>268.70 (n/a)</td><td>175.04 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.49 (-2.39%)</td><td>0.34 <b>(-20.08%)</b></td><td>0.26 <b>(-42.12%)</b></td><td>0.25 (+3.31%)</td><td>0.12 (+10.07%)</td><td>529.30 (-3.20%)</td><td>423.22 <b>(+26.87%)</b></td><td>510.00 <b>(+72.76%)</b></td><td>265.90 (+2.47%)</td><td>129.67 (+7.50%)</td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.44 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>546.80 (n/a)</td><td>333.58 (n/a)</td><td>295.20 (n/a)</td><td>259.50 (n/a)</td><td>120.62 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.44 (-5.77%)</td><td>0.30 (-0.31%)</td><td>0.26 (-7.13%)</td><td>0.16 <b>(+25.08%)</b></td><td>0.13 (-8.52%)</td><td>819.50 <b>(-20.06%)</b></td><td>508.38 (-5.64%)</td><td>508.00 (+7.67%)</td><td>299.10 (+6.10%)</td><td>220.48 <b>(-26.82%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.47 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>1025.10 (n/a)</td><td>538.78 (n/a)</td><td>471.80 (n/a)</td><td>281.90 (n/a)</td><td>301.28 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.54 (-3.53%)</td><td>0.37 (+10.71%)</td><td>0.33 (+17.19%)</td><td>0.29 (+11.63%)</td><td>0.10 (-19.93%)</td><td>451.40 (-10.42%)</td><td>373.36 (-12.32%)</td><td>393.40 (-14.68%)</td><td>244.80 (+3.68%)</td><td>83.10 <b>(-22.89%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.56 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>503.90 (n/a)</td><td>425.82 (n/a)</td><td>461.10 (n/a)</td><td>236.10 (n/a)</td><td>107.78 (n/a)</td>
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
<td><code>2df13d5</code> — 2026-07-31 22:04:20</td><td>0.06 (-8.91%)</td><td>0.06 (+5.89%)</td><td>0.06 (-3.30%)</td><td>0.05 <b>(+130.64%)</b></td><td>0.00 <b>(-78.86%)</b></td><td>309.70 <b>(-56.64%)</b></td><td>285.36 (-19.66%)</td><td>291.00 (+3.41%)</td><td>259.00 (+9.79%)</td><td>19.12 <b>(-90.55%)</b></td>
</tr>
<tr>
<td><code>d7be779</code> — 2026-07-31 21:33:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>714.30 (n/a)</td><td>355.20 (n/a)</td><td>281.40 (n/a)</td><td>235.90 (n/a)</td><td>202.32 (n/a)</td>
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
