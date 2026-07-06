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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (+2.26%)</td><td>0.02 (+12.77%)</td><td>0.02 (+13.71%)</td><td>0.01 (+11.34%)</td><td>0.01 (-16.68%)</td><td>527.70 (-10.18%)</td><td>300.08 (-15.66%)</td><td>248.40 (-12.04%)</td><td>207.00 (-2.22%)</td><td>129.50 <b>(-20.74%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.50 (n/a)</td><td>355.78 (n/a)</td><td>282.40 (n/a)</td><td>211.70 (n/a)</td><td>163.39 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (-8.64%)</td><td>0.02 (+1.42%)</td><td>0.02 <b>(+32.73%)</b></td><td>0.01 (+2.14%)</td><td>0.01 (-1.72%)</td><td>569.10 (-2.10%)</td><td>383.82 (-0.19%)</td><td>297.20 <b>(-24.66%)</b></td><td>247.80 (+9.45%)</td><td>147.19 (+10.70%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.30 (n/a)</td><td>384.56 (n/a)</td><td>394.50 (n/a)</td><td>226.40 (n/a)</td><td>132.97 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (+17.81%)</td><td>0.02 <b>(+34.30%)</b></td><td>0.02 <b>(+39.86%)</b></td><td>0.01 <b>(+24.52%)</b></td><td>0.01 <b>(+21.33%)</b></td><td>442.60 (-19.69%)</td><td>333.42 <b>(-25.53%)</b></td><td>365.50 <b>(-28.50%)</b></td><td>218.30 (-15.12%)</td><td>99.08 (-18.03%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.10 (n/a)</td><td>447.72 (n/a)</td><td>511.20 (n/a)</td><td>257.20 (n/a)</td><td>120.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (+2.21%)</td><td>0.02 (-1.93%)</td><td>0.02 (-2.60%)</td><td>0.01 <b>(+22.43%)</b></td><td>0.01 (-15.26%)</td><td>508.30 (-18.32%)</td><td>381.52 (-2.19%)</td><td>401.00 (+2.69%)</td><td>246.70 (-2.18%)</td><td>101.15 <b>(-31.64%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.30 (n/a)</td><td>390.08 (n/a)</td><td>390.50 (n/a)</td><td>252.20 (n/a)</td><td>147.96 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (-17.66%)</td><td>0.02 (+2.73%)</td><td>0.02 (+16.20%)</td><td>0.01 (-8.27%)</td><td>0.00 <b>(-24.16%)</b></td><td>579.20 (+9.02%)</td><td>397.88 (-4.69%)</td><td>405.90 (-13.95%)</td><td>296.80 <b>(+21.44%)</b></td><td>115.28 (-2.70%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>531.30 (n/a)</td><td>417.44 (n/a)</td><td>471.70 (n/a)</td><td>244.40 (n/a)</td><td>118.47 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 <b>(+21.50%)</b></td><td>0.02 <b>(+20.40%)</b></td><td>0.02 <b>(+46.94%)</b></td><td>0.01 (-18.75%)</td><td>0.01 <b>(+51.56%)</b></td><td>617.60 <b>(+23.08%)</b></td><td>336.44 (-10.28%)</td><td>274.50 <b>(-31.95%)</b></td><td>225.10 (-17.70%)</td><td>162.35 <b>(+66.70%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>501.80 (n/a)</td><td>374.98 (n/a)</td><td>403.40 (n/a)</td><td>273.50 (n/a)</td><td>97.39 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (+3.53%)</td><td>0.05 (-3.55%)</td><td>0.05 (+5.12%)</td><td>0.03 <b>(-36.04%)</b></td><td>0.01 <b>(+218.11%)</b></td><td>429.30 <b>(+56.34%)</b></td><td>280.42 (+9.17%)</td><td>242.50 (-4.86%)</td><td>228.20 (-3.39%)</td><td>84.68 <b>(+386.23%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>274.60 (n/a)</td><td>256.86 (n/a)</td><td>254.90 (n/a)</td><td>236.20 (n/a)</td><td>17.42 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (-10.16%)</td><td>0.04 (+4.95%)</td><td>0.04 (-13.21%)</td><td>0.02 <b>(+219.23%)</b></td><td>0.01 <b>(-50.32%)</b></td><td>617.40 <b>(-68.67%)</b></td><td>370.66 <b>(-47.19%)</b></td><td>289.80 (+15.23%)</td><td>261.70 (+11.31%)</td><td>147.79 <b>(-80.34%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1970.80 (n/a)</td><td>701.92 (n/a)</td><td>251.50 (n/a)</td><td>235.10 (n/a)</td><td>751.81 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (+16.61%)</td><td>0.04 <b>(+22.36%)</b></td><td>0.04 <b>(+61.61%)</b></td><td>0.02 (+9.52%)</td><td>0.01 (+9.46%)</td><td>547.10 (-8.69%)</td><td>352.80 (-18.75%)</td><td>280.00 <b>(-38.12%)</b></td><td>219.70 (-14.25%)</td><td>137.78 (-12.51%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>599.20 (n/a)</td><td>434.20 (n/a)</td><td>452.50 (n/a)</td><td>256.20 (n/a)</td><td>157.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (+9.63%)</td><td>0.03 (+7.54%)</td><td>0.03 <b>(+39.89%)</b></td><td>0.02 (-1.93%)</td><td>0.02 (+4.95%)</td><td>597.20 (+1.96%)</td><td>414.28 (-6.79%)</td><td>380.90 <b>(-28.52%)</b></td><td>214.50 (-8.80%)</td><td>171.23 (-0.01%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>585.70 (n/a)</td><td>444.44 (n/a)</td><td>532.90 (n/a)</td><td>235.20 (n/a)</td><td>171.25 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 <b>(+25.21%)</b></td><td>0.03 <b>(+31.96%)</b></td><td>0.03 <b>(+47.12%)</b></td><td>0.02 <b>(+23.51%)</b></td><td>0.01 <b>(+27.97%)</b></td><td>549.30 (-19.04%)</td><td>402.78 <b>(-23.46%)</b></td><td>378.10 <b>(-32.02%)</b></td><td>237.50 <b>(-20.14%)</b></td><td>133.06 (-12.03%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>678.50 (n/a)</td><td>526.26 (n/a)</td><td>556.20 (n/a)</td><td>297.40 (n/a)</td><td>151.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (-18.71%)</td><td>0.03 (-10.28%)</td><td>0.03 <b>(+22.66%)</b></td><td>0.01 <b>(-64.62%)</b></td><td>0.01 (-0.32%)</td><td>1940.00 <b>(+182.63%)</b></td><td>709.00 <b>(+48.51%)</b></td><td>445.20 (-18.48%)</td><td>343.20 <b>(+23.01%)</b></td><td>689.68 <b>(+295.98%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>686.40 (n/a)</td><td>477.40 (n/a)</td><td>546.10 (n/a)</td><td>279.00 (n/a)</td><td>174.17 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (+11.24%)</td><td>0.08 (+9.23%)</td><td>0.09 <b>(+24.74%)</b></td><td>0.05 (+9.70%)</td><td>0.02 <b>(+33.20%)</b></td><td>470.40 (-8.84%)</td><td>342.60 (-6.38%)</td><td>287.40 (-19.83%)</td><td>250.20 (-10.10%)</td><td>103.53 (+10.66%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>516.00 (n/a)</td><td>365.96 (n/a)</td><td>358.50 (n/a)</td><td>278.30 (n/a)</td><td>93.55 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (+1.45%)</td><td>0.09 <b>(+45.23%)</b></td><td>0.09 <b>(+76.22%)</b></td><td>0.08 <b>(+90.70%)</b></td><td>0.01 <b>(-49.58%)</b></td><td>327.50 <b>(-47.57%)</b></td><td>278.50 <b>(-37.82%)</b></td><td>267.50 <b>(-43.27%)</b></td><td>240.60 (-1.43%)</td><td>40.71 <b>(-74.14%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>624.60 (n/a)</td><td>447.88 (n/a)</td><td>471.50 (n/a)</td><td>244.10 (n/a)</td><td>157.42 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (+12.95%)</td><td>0.07 (+1.73%)</td><td>0.05 (-12.81%)</td><td>0.04 (+5.67%)</td><td>0.04 (+18.99%)</td><td>558.70 (-5.37%)</td><td>400.52 (+2.04%)</td><td>496.60 (+14.69%)</td><td>195.80 (-11.48%)</td><td>167.57 (+6.67%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>590.40 (n/a)</td><td>392.52 (n/a)</td><td>433.00 (n/a)</td><td>221.20 (n/a)</td><td>157.09 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (+18.16%)</td><td>0.08 <b>(+24.04%)</b></td><td>0.10 <b>(+65.61%)</b></td><td>0.05 (+15.41%)</td><td>0.03 <b>(+24.00%)</b></td><td>520.70 (-13.36%)</td><td>338.82 (-17.25%)</td><td>244.10 <b>(-39.61%)</b></td><td>198.90 (-15.40%)</td><td>153.07 (-2.88%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>601.00 (n/a)</td><td>409.44 (n/a)</td><td>404.20 (n/a)</td><td>235.10 (n/a)</td><td>157.62 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 <b>(-21.87%)</b></td><td>0.08 (+0.18%)</td><td>0.08 <b>(+20.28%)</b></td><td>0.04 (-6.04%)</td><td>0.02 <b>(-37.45%)</b></td><td>566.90 (+6.44%)</td><td>338.14 (-5.69%)</td><td>295.00 (-16.85%)</td><td>246.50 <b>(+27.99%)</b></td><td>129.67 (-8.85%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>532.60 (n/a)</td><td>358.54 (n/a)</td><td>354.80 (n/a)</td><td>192.60 (n/a)</td><td>142.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 <b>(+46.99%)</b></td><td>0.08 <b>(+86.75%)</b></td><td>0.08 <b>(+70.32%)</b></td><td>0.04 <b>(+332.21%)</b></td><td>0.02 (-0.04%)</td><td>564.60 <b>(-76.86%)</b></td><td>347.68 <b>(-61.78%)</b></td><td>317.40 <b>(-41.28%)</b></td><td>254.80 <b>(-31.96%)</b></td><td>124.39 <b>(-85.56%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2440.20 (n/a)</td><td>909.68 (n/a)</td><td>540.50 (n/a)</td><td>374.50 (n/a)</td><td>861.43 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.21 (-15.62%)</td><td>0.15 (-15.73%)</td><td>0.16 (-15.31%)</td><td>0.08 (-15.10%)</td><td>0.05 (-13.32%)</td><td>628.10 (+17.78%)</td><td>357.86 (+18.91%)</td><td>305.50 (+18.09%)</td><td>237.90 (+18.54%)</td><td>156.51 (+17.95%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>533.30 (n/a)</td><td>300.94 (n/a)</td><td>258.70 (n/a)</td><td>200.70 (n/a)</td><td>132.70 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.22 (+5.38%)</td><td>0.16 (+5.03%)</td><td>0.16 <b>(+26.77%)</b></td><td>0.09 (-17.92%)</td><td>0.05 (-2.24%)</td><td>552.20 <b>(+21.84%)</b></td><td>331.18 (-3.21%)</td><td>298.40 <b>(-21.10%)</b></td><td>225.90 (-5.08%)</td><td>127.26 <b>(+29.39%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>453.20 (n/a)</td><td>342.18 (n/a)</td><td>378.20 (n/a)</td><td>238.00 (n/a)</td><td>98.36 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.18 (-15.30%)</td><td>0.13 <b>(-26.09%)</b></td><td>0.16 (-13.09%)</td><td>0.05 <b>(-53.81%)</b></td><td>0.06 <b>(+30.64%)</b></td><td>1029.80 <b>(+116.48%)</b></td><td>483.58 <b>(+61.99%)</b></td><td>304.80 (+15.06%)</td><td>268.80 (+18.05%)</td><td>320.67 <b>(+217.70%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>475.70 (n/a)</td><td>298.52 (n/a)</td><td>264.90 (n/a)</td><td>227.70 (n/a)</td><td>100.94 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.20 (-3.66%)</td><td>0.17 (-6.02%)</td><td>0.17 (-12.16%)</td><td>0.10 (-10.08%)</td><td>0.04 (-7.16%)</td><td>479.00 (+11.21%)</td><td>313.18 (+6.71%)</td><td>284.20 (+13.86%)</td><td>240.80 (+3.79%)</td><td>94.70 (+13.84%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>430.70 (n/a)</td><td>293.48 (n/a)</td><td>249.60 (n/a)</td><td>232.00 (n/a)</td><td>83.19 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.20 <b>(+21.63%)</b></td><td>0.16 <b>(+57.16%)</b></td><td>0.16 <b>(+48.80%)</b></td><td>0.11 <b>(+198.16%)</b></td><td>0.04 <b>(-20.66%)</b></td><td>465.70 <b>(-66.46%)</b></td><td>329.54 <b>(-48.71%)</b></td><td>298.40 <b>(-32.79%)</b></td><td>244.00 (-17.76%)</td><td>89.44 <b>(-79.47%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1388.60 (n/a)</td><td>642.54 (n/a)</td><td>444.00 (n/a)</td><td>296.70 (n/a)</td><td>435.61 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.18 (-15.22%)</td><td>0.11 <b>(-20.84%)</b></td><td>0.10 <b>(-28.91%)</b></td><td>0.03 <b>(-41.38%)</b></td><td>0.06 (-4.52%)</td><td>1866.70 <b>(+70.58%)</b></td><td>712.14 <b>(+48.81%)</b></td><td>514.80 <b>(+40.66%)</b></td><td>276.60 (+17.95%)</td><td>661.48 <b>(+86.37%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>0.07 (n/a)</td><td>1094.30 (n/a)</td><td>478.56 (n/a)</td><td>366.00 (n/a)</td><td>234.50 (n/a)</td><td>354.92 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (+1.26%)</td><td>0.01 (-5.42%)</td><td>0.01 (+5.39%)</td><td>0.00 (-18.93%)</td><td>0.00 <b>(+24.27%)</b></td><td>612.00 <b>(+23.36%)</b></td><td>376.00 (+11.16%)</td><td>298.00 (-5.13%)</td><td>246.70 (-1.24%)</td><td>150.63 <b>(+52.77%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.10 (n/a)</td><td>338.26 (n/a)</td><td>314.10 (n/a)</td><td>249.80 (n/a)</td><td>98.60 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (+2.33%)</td><td>0.01 <b>(+30.00%)</b></td><td>0.01 <b>(+49.78%)</b></td><td>0.01 <b>(+42.03%)</b></td><td>0.00 <b>(-26.29%)</b></td><td>399.00 <b>(-29.59%)</b></td><td>319.60 <b>(-26.39%)</b></td><td>298.30 <b>(-33.24%)</b></td><td>244.00 (-2.24%)</td><td>64.24 <b>(-44.80%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>566.70 (n/a)</td><td>434.18 (n/a)</td><td>446.80 (n/a)</td><td>249.60 (n/a)</td><td>116.37 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (+19.11%)</td><td>0.01 <b>(+53.98%)</b></td><td>0.01 <b>(+106.59%)</b></td><td>0.01 <b>(+95.64%)</b></td><td>0.00 <b>(-46.43%)</b></td><td>274.20 <b>(-48.89%)</b></td><td>233.80 <b>(-42.43%)</b></td><td>235.00 <b>(-51.60%)</b></td><td>183.90 (-16.07%)</td><td>32.73 <b>(-78.20%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>536.50 (n/a)</td><td>406.14 (n/a)</td><td>485.50 (n/a)</td><td>219.10 (n/a)</td><td>150.15 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 <b>(+69.83%)</b></td><td>0.01 <b>(+53.06%)</b></td><td>0.01 <b>(+75.42%)</b></td><td>0.00 <b>(-23.90%)</b></td><td>0.00 <b>(+261.82%)</b></td><td>681.70 <b>(+31.40%)</b></td><td>352.10 <b>(-24.57%)</b></td><td>283.00 <b>(-42.99%)</b></td><td>216.50 <b>(-41.12%)</b></td><td>189.08 <b>(+198.90%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.80 (n/a)</td><td>466.82 (n/a)</td><td>496.40 (n/a)</td><td>367.70 (n/a)</td><td>63.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (-2.30%)</td><td>0.01 <b>(+24.74%)</b></td><td>0.01 <b>(+48.84%)</b></td><td>0.00 (+2.59%)</td><td>0.00 (-0.63%)</td><td>570.90 (-2.53%)</td><td>390.66 (-19.95%)</td><td>352.80 <b>(-32.83%)</b></td><td>273.30 (+2.36%)</td><td>129.65 (-0.83%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>585.70 (n/a)</td><td>488.04 (n/a)</td><td>525.20 (n/a)</td><td>267.00 (n/a)</td><td>130.73 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 <b>(+139.76%)</b></td><td>0.01 <b>(+63.42%)</b></td><td>0.01 (+6.48%)</td><td>0.00 <b>(+82.76%)</b></td><td>0.00 <b>(+195.90%)</b></td><td>579.30 <b>(-45.29%)</b></td><td>431.02 <b>(-33.55%)</b></td><td>492.30 (-6.09%)</td><td>203.00 <b>(-58.29%)</b></td><td>169.82 <b>(-29.56%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1058.80 (n/a)</td><td>648.60 (n/a)</td><td>524.20 (n/a)</td><td>486.70 (n/a)</td><td>241.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (+3.17%)</td><td>0.01 (+7.32%)</td><td>0.01 (+0.96%)</td><td>0.01 <b>(+21.22%)</b></td><td>0.00 (-3.44%)</td><td>480.30 (-17.50%)</td><td>391.72 (-8.62%)</td><td>456.30 (-0.96%)</td><td>252.70 (-3.07%)</td><td>109.41 (-19.88%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.20 (n/a)</td><td>428.66 (n/a)</td><td>460.70 (n/a)</td><td>260.70 (n/a)</td><td>136.54 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(+35.95%)</b></td><td>0.01 <b>(+57.05%)</b></td><td>0.01 <b>(+51.78%)</b></td><td>0.01 <b>(+265.92%)</b></td><td>0.00 (+4.84%)</td><td>565.60 <b>(-72.67%)</b></td><td>395.00 <b>(-51.37%)</b></td><td>351.10 <b>(-34.12%)</b></td><td>270.00 <b>(-26.45%)</b></td><td>129.62 <b>(-81.67%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2069.50 (n/a)</td><td>812.26 (n/a)</td><td>532.90 (n/a)</td><td>367.10 (n/a)</td><td>707.16 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(-22.29%)</b></td><td>0.01 (-4.92%)</td><td>0.01 (+2.37%)</td><td>0.01 (+15.81%)</td><td>0.01 <b>(-29.62%)</b></td><td>679.90 (-13.65%)</td><td>455.64 (-3.86%)</td><td>508.90 (-2.32%)</td><td>277.10 <b>(+28.70%)</b></td><td>170.74 <b>(-24.71%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>787.40 (n/a)</td><td>473.94 (n/a)</td><td>521.00 (n/a)</td><td>215.30 (n/a)</td><td>226.79 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(+20.27%)</b></td><td>0.01 (-4.51%)</td><td>0.01 <b>(-26.51%)</b></td><td>0.01 (-2.58%)</td><td>0.01 (+19.75%)</td><td>531.80 (+2.66%)</td><td>399.66 (+6.28%)</td><td>404.90 <b>(+36.06%)</b></td><td>232.10 (-16.84%)</td><td>124.49 (+2.77%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.00 (n/a)</td><td>376.06 (n/a)</td><td>297.60 (n/a)</td><td>279.10 (n/a)</td><td>121.13 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(+20.40%)</b></td><td>0.01 (+15.40%)</td><td>0.01 (-10.82%)</td><td>0.01 (+17.67%)</td><td>0.01 <b>(+26.25%)</b></td><td>566.90 (-15.02%)</td><td>423.16 (-12.52%)</td><td>481.80 (+12.12%)</td><td>220.40 (-16.92%)</td><td>147.61 (-15.19%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>667.10 (n/a)</td><td>483.70 (n/a)</td><td>429.70 (n/a)</td><td>265.30 (n/a)</td><td>174.06 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 <b>(-39.34%)</b></td><td>0.01 (-7.76%)</td><td>0.01 (+13.95%)</td><td>0.01 (-13.08%)</td><td>0.00 <b>(-53.73%)</b></td><td>773.00 (+15.05%)</td><td>506.30 (+1.15%)</td><td>458.00 (-12.24%)</td><td>387.00 <b>(+64.89%)</b></td><td>157.45 (-2.38%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>671.90 (n/a)</td><td>500.54 (n/a)</td><td>521.90 (n/a)</td><td>234.70 (n/a)</td><td>161.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (+6.32%)</td><td>0.03 (-3.81%)</td><td>0.03 <b>(-30.43%)</b></td><td>0.02 (+1.24%)</td><td>0.01 (+6.80%)</td><td>525.90 (-1.22%)</td><td>389.76 (+3.94%)</td><td>419.30 <b>(+43.74%)</b></td><td>236.20 (-5.97%)</td><td>134.30 (-5.91%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.40 (n/a)</td><td>374.98 (n/a)</td><td>291.70 (n/a)</td><td>251.20 (n/a)</td><td>142.74 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 <b>(-24.90%)</b></td><td>0.02 <b>(-22.18%)</b></td><td>0.02 <b>(-40.85%)</b></td><td>0.02 (-10.83%)</td><td>0.01 <b>(-24.95%)</b></td><td>588.40 (+12.14%)</td><td>461.92 <b>(+25.82%)</b></td><td>524.00 <b>(+69.03%)</b></td><td>306.30 <b>(+33.17%)</b></td><td>140.36 (+4.16%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.70 (n/a)</td><td>367.12 (n/a)</td><td>310.00 (n/a)</td><td>230.00 (n/a)</td><td>134.75 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (-10.72%)</td><td>0.03 (+9.68%)</td><td>0.02 (+17.83%)</td><td>0.02 (+9.50%)</td><td>0.01 <b>(-22.28%)</b></td><td>557.10 (-8.69%)</td><td>425.56 (-12.67%)</td><td>442.00 (-15.13%)</td><td>250.70 (+11.97%)</td><td>133.41 (-13.58%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>610.10 (n/a)</td><td>487.32 (n/a)</td><td>520.80 (n/a)</td><td>223.90 (n/a)</td><td>154.37 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (+12.50%)</td><td>0.02 (-16.97%)</td><td>0.02 <b>(-41.98%)</b></td><td>0.01 <b>(+137.38%)</b></td><td>0.01 (-16.40%)</td><td>805.30 <b>(-57.87%)</b></td><td>525.26 (-17.98%)</td><td>479.10 <b>(+72.34%)</b></td><td>234.50 (-11.11%)</td><td>221.63 <b>(-69.06%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1911.50 (n/a)</td><td>640.38 (n/a)</td><td>278.00 (n/a)</td><td>263.80 (n/a)</td><td>716.38 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 <b>(+46.08%)</b></td><td>0.03 <b>(+48.31%)</b></td><td>0.02 (+19.11%)</td><td>0.02 <b>(+327.97%)</b></td><td>0.01 <b>(-23.92%)</b></td><td>491.20 <b>(-76.64%)</b></td><td>417.84 <b>(-49.78%)</b></td><td>446.20 (-16.03%)</td><td>301.70 <b>(-31.54%)</b></td><td>78.72 <b>(-88.95%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2102.30 (n/a)</td><td>832.04 (n/a)</td><td>531.40 (n/a)</td><td>440.70 (n/a)</td><td>712.10 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (-15.58%)</td><td>0.02 (-7.11%)</td><td>0.02 (-2.58%)</td><td>0.02 (-11.95%)</td><td>0.01 (+3.36%)</td><td>644.00 (+13.58%)</td><td>469.02 (+11.21%)</td><td>464.60 (+2.63%)</td><td>305.20 (+18.48%)</td><td>164.58 <b>(+39.90%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>567.00 (n/a)</td><td>421.76 (n/a)</td><td>452.70 (n/a)</td><td>257.60 (n/a)</td><td>117.64 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (-6.95%)</td><td>0.06 (+7.49%)</td><td>0.06 <b>(+39.76%)</b></td><td>0.04 (+3.89%)</td><td>0.01 <b>(-34.36%)</b></td><td>520.40 (-3.75%)</td><td>358.46 (-12.32%)</td><td>345.10 <b>(-28.45%)</b></td><td>262.90 (+7.48%)</td><td>98.20 <b>(-29.49%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>540.70 (n/a)</td><td>408.82 (n/a)</td><td>482.30 (n/a)</td><td>244.60 (n/a)</td><td>139.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (+16.53%)</td><td>0.07 <b>(+20.96%)</b></td><td>0.08 (+19.99%)</td><td>0.04 (+5.49%)</td><td>0.02 <b>(+21.34%)</b></td><td>599.00 (-5.21%)</td><td>325.42 (-15.29%)</td><td>263.30 (-16.65%)</td><td>235.40 (-14.21%)</td><td>154.01 (+3.58%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>631.90 (n/a)</td><td>384.18 (n/a)</td><td>315.90 (n/a)</td><td>274.40 (n/a)</td><td>148.69 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (+7.57%)</td><td>0.07 <b>(+26.37%)</b></td><td>0.08 <b>(+33.73%)</b></td><td>0.05 <b>(+32.65%)</b></td><td>0.02 <b>(-21.26%)</b></td><td>449.00 <b>(-24.61%)</b></td><td>303.10 <b>(-25.20%)</b></td><td>263.90 <b>(-25.24%)</b></td><td>250.10 (-7.06%)</td><td>83.87 <b>(-43.59%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>595.60 (n/a)</td><td>405.20 (n/a)</td><td>353.00 (n/a)</td><td>269.10 (n/a)</td><td>148.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (+4.55%)</td><td>0.07 (+3.54%)</td><td>0.07 (-9.59%)</td><td>0.04 (+12.73%)</td><td>0.02 <b>(-22.15%)</b></td><td>541.30 (-11.29%)</td><td>344.08 (-9.18%)</td><td>301.20 (+10.57%)</td><td>237.00 (-4.36%)</td><td>117.52 <b>(-29.33%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>610.20 (n/a)</td><td>378.84 (n/a)</td><td>272.40 (n/a)</td><td>247.80 (n/a)</td><td>166.29 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 <b>(+35.16%)</b></td><td>0.06 <b>(+30.49%)</b></td><td>0.04 (-11.39%)</td><td>0.04 <b>(+243.48%)</b></td><td>0.03 (+12.80%)</td><td>547.70 <b>(-70.89%)</b></td><td>412.90 <b>(-42.42%)</b></td><td>501.20 (+12.86%)</td><td>212.50 <b>(-26.01%)</b></td><td>158.53 <b>(-76.14%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1881.30 (n/a)</td><td>717.10 (n/a)</td><td>444.10 (n/a)</td><td>287.20 (n/a)</td><td>664.38 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 <b>(+41.69%)</b></td><td>0.04 (-2.15%)</td><td>0.04 (-8.63%)</td><td>0.01 <b>(-48.26%)</b></td><td>0.03 <b>(+77.17%)</b></td><td>1915.10 <b>(+93.27%)</b></td><td>755.02 <b>(+39.70%)</b></td><td>495.80 (+9.45%)</td><td>229.20 <b>(-29.41%)</b></td><td>666.04 <b>(+150.19%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>990.90 (n/a)</td><td>540.44 (n/a)</td><td>453.00 (n/a)</td><td>324.70 (n/a)</td><td>266.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.80 (n/a)</td><td>449.56 (n/a)</td><td>474.50 (n/a)</td><td>196.40 (n/a)</td><td>147.76 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>498.20 (n/a)</td><td>361.62 (n/a)</td><td>360.60 (n/a)</td><td>223.60 (n/a)</td><td>123.90 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.30 (n/a)</td><td>369.44 (n/a)</td><td>381.40 (n/a)</td><td>255.70 (n/a)</td><td>105.03 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>507.40 (n/a)</td><td>337.92 (n/a)</td><td>286.70 (n/a)</td><td>166.50 (n/a)</td><td>153.34 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.20 (n/a)</td><td>429.34 (n/a)</td><td>439.50 (n/a)</td><td>264.60 (n/a)</td><td>100.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.70 (n/a)</td><td>413.56 (n/a)</td><td>486.60 (n/a)</td><td>232.70 (n/a)</td><td>134.65 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>561.30 (n/a)</td><td>452.76 (n/a)</td><td>488.40 (n/a)</td><td>323.40 (n/a)</td><td>118.76 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>598.30 (n/a)</td><td>468.30 (n/a)</td><td>507.30 (n/a)</td><td>195.80 (n/a)</td><td>160.76 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>546.60 (n/a)</td><td>455.14 (n/a)</td><td>478.50 (n/a)</td><td>282.10 (n/a)</td><td>102.25 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.25 <b>(+24.05%)</b></td><td>0.14 (+0.60%)</td><td>0.11 (-12.54%)</td><td>0.08 (-14.70%)</td><td>0.07 <b>(+61.28%)</b></td><td>589.50 (+17.22%)</td><td>423.70 (+10.60%)</td><td>464.10 (+14.34%)</td><td>199.20 (-19.38%)</td><td>178.81 <b>(+59.66%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>502.90 (n/a)</td><td>383.10 (n/a)</td><td>405.90 (n/a)</td><td>247.10 (n/a)</td><td>111.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>603.00 (n/a)</td><td>394.48 (n/a)</td><td>375.60 (n/a)</td><td>194.70 (n/a)</td><td>163.50 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1093.90 (n/a)</td><td>572.46 (n/a)</td><td>535.90 (n/a)</td><td>306.70 (n/a)</td><td>313.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1936.60 (n/a)</td><td>653.04 (n/a)</td><td>271.70 (n/a)</td><td>260.40 (n/a)</td><td>726.30 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1008.10 (n/a)</td><td>513.16 (n/a)</td><td>402.20 (n/a)</td><td>235.50 (n/a)</td><td>318.19 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.50 (n/a)</td><td>480.28 (n/a)</td><td>551.20 (n/a)</td><td>261.70 (n/a)</td><td>153.22 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1020.40 (n/a)</td><td>437.26 (n/a)</td><td>288.90 (n/a)</td><td>271.00 (n/a)</td><td>326.42 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>659.90 (n/a)</td><td>440.36 (n/a)</td><td>484.80 (n/a)</td><td>234.90 (n/a)</td><td>187.33 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.80 (n/a)</td><td>416.36 (n/a)</td><td>396.10 (n/a)</td><td>301.50 (n/a)</td><td>91.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>667.70 (n/a)</td><td>467.18 (n/a)</td><td>475.30 (n/a)</td><td>275.30 (n/a)</td><td>141.58 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>483.70 (n/a)</td><td>391.76 (n/a)</td><td>416.70 (n/a)</td><td>310.10 (n/a)</td><td>77.36 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>660.80 (n/a)</td><td>473.12 (n/a)</td><td>513.80 (n/a)</td><td>267.00 (n/a)</td><td>156.93 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>1862.70 (n/a)</td><td>660.06 (n/a)</td><td>299.70 (n/a)</td><td>231.20 (n/a)</td><td>690.48 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>600.00 (n/a)</td><td>427.94 (n/a)</td><td>381.80 (n/a)</td><td>269.00 (n/a)</td><td>157.13 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>612.90 (n/a)</td><td>346.76 (n/a)</td><td>290.90 (n/a)</td><td>231.60 (n/a)</td><td>154.73 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.10 (n/a)</td><td>406.94 (n/a)</td><td>335.50 (n/a)</td><td>203.40 (n/a)</td><td>186.15 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.00 (n/a)</td><td>443.22 (n/a)</td><td>471.80 (n/a)</td><td>257.30 (n/a)</td><td>152.72 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.10 (n/a)</td><td>311.22 (n/a)</td><td>253.80 (n/a)</td><td>232.50 (n/a)</td><td>110.72 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.10 (n/a)</td><td>415.84 (n/a)</td><td>407.60 (n/a)</td><td>330.00 (n/a)</td><td>86.57 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>620.80 (n/a)</td><td>470.52 (n/a)</td><td>430.20 (n/a)</td><td>302.60 (n/a)</td><td>129.91 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.50 (n/a)</td><td>394.26 (n/a)</td><td>414.40 (n/a)</td><td>249.90 (n/a)</td><td>132.54 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>657.20 (n/a)</td><td>470.18 (n/a)</td><td>466.20 (n/a)</td><td>291.20 (n/a)</td><td>129.77 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.60 (n/a)</td><td>424.72 (n/a)</td><td>377.20 (n/a)</td><td>280.10 (n/a)</td><td>150.24 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.50 (n/a)</td><td>386.14 (n/a)</td><td>346.20 (n/a)</td><td>253.00 (n/a)</td><td>129.07 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>692.90 (n/a)</td><td>513.62 (n/a)</td><td>488.10 (n/a)</td><td>370.00 (n/a)</td><td>121.93 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2492.10 (n/a)</td><td>889.52 (n/a)</td><td>498.60 (n/a)</td><td>450.30 (n/a)</td><td>896.37 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>574.40 (n/a)</td><td>445.76 (n/a)</td><td>473.00 (n/a)</td><td>313.60 (n/a)</td><td>122.92 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>569.70 (n/a)</td><td>388.20 (n/a)</td><td>396.20 (n/a)</td><td>272.30 (n/a)</td><td>117.40 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1048.40 (n/a)</td><td>548.76 (n/a)</td><td>467.50 (n/a)</td><td>305.50 (n/a)</td><td>290.34 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.60 (n/a)</td><td>481.80 (n/a)</td><td>504.90 (n/a)</td><td>273.00 (n/a)</td><td>126.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>589.70 (n/a)</td><td>406.62 (n/a)</td><td>431.00 (n/a)</td><td>272.40 (n/a)</td><td>127.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1970.10 (n/a)</td><td>704.86 (n/a)</td><td>383.90 (n/a)</td><td>297.90 (n/a)</td><td>713.06 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>702.00 (n/a)</td><td>579.02 (n/a)</td><td>630.60 (n/a)</td><td>276.10 (n/a)</td><td>174.12 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1954.20 (n/a)</td><td>691.84 (n/a)</td><td>360.40 (n/a)</td><td>240.60 (n/a)</td><td>716.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2412.60 (n/a)</td><td>831.08 (n/a)</td><td>462.00 (n/a)</td><td>351.90 (n/a)</td><td>885.92 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>646.00 (n/a)</td><td>454.74 (n/a)</td><td>416.70 (n/a)</td><td>272.00 (n/a)</td><td>150.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2429.50 (n/a)</td><td>783.10 (n/a)</td><td>456.00 (n/a)</td><td>258.30 (n/a)</td><td>925.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.46 <b>(-26.51%)</b></td><td>0.40 (-10.12%)</td><td>0.38 (-10.06%)</td><td>0.34 <b>(+38.41%)</b></td><td>0.05 <b>(-65.23%)</b></td><td>645.80 <b>(-27.75%)</b></td><td>566.88 (+1.56%)</td><td>587.60 (+11.20%)</td><td>481.90 <b>(+36.09%)</b></td><td>72.27 <b>(-66.08%)</b></td><td>19.58 <b>(-26.51%)</b></td><td>16.87 (-10.12%)</td><td>16.06 (-10.06%)</td><td>14.61 <b>(+38.41%)</b></td><td>2.21 <b>(-65.23%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.62 (n/a)</td><td>0.44 (n/a)</td><td>0.42 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>893.80 (n/a)</td><td>558.16 (n/a)</td><td>528.40 (n/a)</td><td>354.10 (n/a)</td><td>213.05 (n/a)</td><td>26.65 (n/a)</td><td>18.77 (n/a)</td><td>17.86 (n/a)</td><td>10.56 (n/a)</td><td>6.37 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.48 <b>(-25.95%)</b></td><td>0.40 (-5.65%)</td><td>0.37 (+7.74%)</td><td>0.37 <b>(+73.23%)</b></td><td>0.05 <b>(-74.13%)</b></td><td>594.40 <b>(-42.27%)</b></td><td>555.40 (-8.96%)</td><td>593.90 (-7.17%)</td><td>459.20 <b>(+35.06%)</b></td><td>59.56 <b>(-78.53%)</b></td><td>20.55 <b>(-25.95%)</b></td><td>17.17 (-5.65%)</td><td>15.89 (+7.74%)</td><td>15.88 <b>(+73.23%)</b></td><td>2.04 <b>(-74.13%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.65 (n/a)</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>1029.70 (n/a)</td><td>610.06 (n/a)</td><td>639.80 (n/a)</td><td>340.00 (n/a)</td><td>277.40 (n/a)</td><td>27.76 (n/a)</td><td>18.19 (n/a)</td><td>14.75 (n/a)</td><td>9.17 (n/a)</td><td>7.88 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.31 (-0.04%)</td><td>0.31 (+0.60%)</td><td>0.31 (+1.21%)</td><td>0.30 (-0.31%)</td><td>0.01 (+18.36%)</td><td>84272.90 (+0.31%)</td><td>82164.04 (-0.59%)</td><td>82187.70 (-1.20%)</td><td>80431.60 (+0.04%)</td><td>1665.56 (+18.75%)</td><td>213.60 (-0.04%)</td><td>209.16 (+0.60%)</td><td>209.03 (+1.21%)</td><td>203.86 (-0.31%)</td><td>4.23 (+18.36%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84009.40 (n/a)</td><td>82649.08 (n/a)</td><td>83183.90 (n/a)</td><td>80401.00 (n/a)</td><td>1402.57 (n/a)</td><td>213.68 (n/a)</td><td>207.91 (n/a)</td><td>206.53 (n/a)</td><td>204.50 (n/a)</td><td>3.58 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>1.03 (-0.20%)</td><td>1.02 (+1.59%)</td><td>1.01 (+2.17%)</td><td>1.01 (+2.89%)</td><td>0.01 <b>(-60.78%)</b></td><td>24923.90 (-2.81%)</td><td>24787.42 (-1.59%)</td><td>24918.90 (-2.13%)</td><td>24486.90 (+0.20%)</td><td>196.72 <b>(-61.78%)</b></td><td>701.60 (-0.20%)</td><td>693.12 (+1.59%)</td><td>689.43 (+2.17%)</td><td>689.29 (+2.89%)</td><td>5.53 <b>(-60.78%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>0.99 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25644.70 (n/a)</td><td>25188.24 (n/a)</td><td>25460.40 (n/a)</td><td>24437.10 (n/a)</td><td>514.74 (n/a)</td><td>703.02 (n/a)</td><td>682.29 (n/a)</td><td>674.77 (n/a)</td><td>669.92 (n/a)</td><td>14.10 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.81 (-0.98%)</td><td>0.79 (-2.10%)</td><td>0.79 (-1.86%)</td><td>0.77 (-3.47%)</td><td>0.01 <b>(+144.04%)</b></td><td>97476.90 (+3.59%)</td><td>95513.26 (+2.17%)</td><td>95437.80 (+1.89%)</td><td>93344.20 (+0.99%)</td><td>1784.97 <b>(+155.56%)</b></td><td>736.19 (-0.98%)</td><td>719.68 (-2.10%)</td><td>720.04 (-1.86%)</td><td>704.98 (-3.47%)</td><td>13.46 <b>(+144.04%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94099.00 (n/a)</td><td>93480.90 (n/a)</td><td>93664.30 (n/a)</td><td>92429.90 (n/a)</td><td>698.44 (n/a)</td><td>743.48 (n/a)</td><td>735.15 (n/a)</td><td>733.68 (n/a)</td><td>730.29 (n/a)</td><td>5.52 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.78 (+0.68%)</td><td>0.77 (+1.77%)</td><td>0.77 (+1.64%)</td><td>0.76 (+1.98%)</td><td>0.01 <b>(-37.85%)</b></td><td>99158.30 (-1.95%)</td><td>97832.86 (-1.75%)</td><td>97896.40 (-1.61%)</td><td>96750.80 (-0.68%)</td><td>949.50 <b>(-39.64%)</b></td><td>710.27 (+0.68%)</td><td>702.47 (+1.77%)</td><td>701.96 (+1.64%)</td><td>693.03 (+1.98%)</td><td>6.80 <b>(-37.85%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101126.40 (n/a)</td><td>99577.48 (n/a)</td><td>99499.50 (n/a)</td><td>97408.40 (n/a)</td><td>1573.05 (n/a)</td><td>705.48 (n/a)</td><td>690.25 (n/a)</td><td>690.65 (n/a)</td><td>679.54 (n/a)</td><td>10.95 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.80 (-0.51%)</td><td>0.79 (-0.26%)</td><td>0.79 (+0.19%)</td><td>0.78 (-0.58%)</td><td>0.01 (-7.78%)</td><td>96470.60 (+0.58%)</td><td>95384.56 (+0.26%)</td><td>95355.00 (-0.19%)</td><td>94558.90 (+0.51%)</td><td>765.55 (-6.78%)</td><td>726.74 (-0.51%)</td><td>720.48 (-0.26%)</td><td>720.67 (+0.19%)</td><td>712.34 (-0.58%)</td><td>5.77 (-7.78%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95912.60 (n/a)</td><td>95136.78 (n/a)</td><td>95540.00 (n/a)</td><td>94076.40 (n/a)</td><td>821.23 (n/a)</td><td>730.46 (n/a)</td><td>722.37 (n/a)</td><td>719.27 (n/a)</td><td>716.48 (n/a)</td><td>6.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.63 (+8.68%)</td><td>3.64 (+5.14%)</td><td>4.09 (+10.89%)</td><td>1.97 (-8.85%)</td><td>1.55 (+19.38%)</td><td>4526.10 (+9.71%)</td><td>2897.12 (-0.47%)</td><td>2178.10 (-9.82%)</td><td>1584.10 (-7.99%)</td><td>1337.29 (+18.18%)</td><td>338.91 (+8.68%)</td><td>218.97 (+5.14%)</td><td>246.49 (+10.89%)</td><td>118.62 (-8.85%)</td><td>93.52 (+19.38%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.18 (n/a)</td><td>3.46 (n/a)</td><td>3.69 (n/a)</td><td>2.16 (n/a)</td><td>1.30 (n/a)</td><td>4125.50 (n/a)</td><td>2910.72 (n/a)</td><td>2415.20 (n/a)</td><td>1721.60 (n/a)</td><td>1131.61 (n/a)</td><td>311.84 (n/a)</td><td>208.27 (n/a)</td><td>222.29 (n/a)</td><td>130.14 (n/a)</td><td>78.34 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.06 (+16.00%)</td><td>2.88 (+1.39%)</td><td>2.27 (-1.58%)</td><td>2.14 (+0.39%)</td><td>1.24 <b>(+32.18%)</b></td><td>4161.30 (-0.39%)</td><td>3433.02 (+1.88%)</td><td>3926.60 (+1.60%)</td><td>1762.80 (-13.80%)</td><td>1010.38 (+11.43%)</td><td>304.56 (+16.00%)</td><td>173.71 (+1.39%)</td><td>136.73 (-1.58%)</td><td>129.01 (+0.39%)</td><td>74.82 <b>(+32.18%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>4.36 (n/a)</td><td>2.84 (n/a)</td><td>2.31 (n/a)</td><td>2.13 (n/a)</td><td>0.94 (n/a)</td><td>4177.70 (n/a)</td><td>3369.64 (n/a)</td><td>3864.70 (n/a)</td><td>2044.90 (n/a)</td><td>906.76 (n/a)</td><td>262.54 (n/a)</td><td>171.34 (n/a)</td><td>138.91 (n/a)</td><td>128.51 (n/a)</td><td>56.60 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.10 <b>(-42.57%)</b></td><td>2.69 (-16.79%)</td><td>2.75 <b>(+23.54%)</b></td><td>2.18 (-0.48%)</td><td>0.34 <b>(-76.92%)</b></td><td>4092.60 (+0.48%)</td><td>3359.36 (+5.35%)</td><td>3246.60 (-19.06%)</td><td>2871.40 <b>(+74.14%)</b></td><td>458.45 <b>(-61.58%)</b></td><td>186.97 <b>(-42.57%)</b></td><td>162.05 (-16.79%)</td><td>165.37 <b>(+23.54%)</b></td><td>131.18 (-0.48%)</td><td>20.59 <b>(-76.92%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.41 (n/a)</td><td>3.23 (n/a)</td><td>2.22 (n/a)</td><td>2.19 (n/a)</td><td>1.48 (n/a)</td><td>4072.90 (n/a)</td><td>3188.80 (n/a)</td><td>4010.90 (n/a)</td><td>1648.90 (n/a)</td><td>1193.11 (n/a)</td><td>325.59 (n/a)</td><td>194.74 (n/a)</td><td>133.85 (n/a)</td><td>131.81 (n/a)</td><td>89.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.87 (-12.93%)</td><td>5.04 (-16.65%)</td><td>4.95 (-19.19%)</td><td>4.17 (-16.42%)</td><td>0.63 (-4.61%)</td><td>8370.30 (+19.65%)</td><td>7011.64 <b>(+20.27%)</b></td><td>7042.40 <b>(+23.74%)</b></td><td>5940.00 (+14.85%)</td><td>904.70 <b>(+29.26%)</b></td><td>361.53 (-12.93%)</td><td>310.26 (-16.65%)</td><td>304.94 (-19.19%)</td><td>256.56 (-16.42%)</td><td>38.89 (-4.61%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>6.74 (n/a)</td><td>6.04 (n/a)</td><td>6.13 (n/a)</td><td>4.98 (n/a)</td><td>0.66 (n/a)</td><td>6995.50 (n/a)</td><td>5830.02 (n/a)</td><td>5691.20 (n/a)</td><td>5172.10 (n/a)</td><td>699.93 (n/a)</td><td>415.21 (n/a)</td><td>372.25 (n/a)</td><td>377.33 (n/a)</td><td>306.98 (n/a)</td><td>40.77 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.37 (-4.62%)</td><td>4.88 (+4.92%)</td><td>5.04 (+7.39%)</td><td>3.98 (+3.98%)</td><td>0.53 <b>(-30.89%)</b></td><td>8769.00 (-3.83%)</td><td>7215.56 (-5.76%)</td><td>6923.80 (-6.88%)</td><td>6491.30 (+4.84%)</td><td>895.72 <b>(-29.65%)</b></td><td>330.83 (-4.62%)</td><td>300.88 (+4.92%)</td><td>310.16 (+7.39%)</td><td>244.90 (+3.98%)</td><td>32.94 <b>(-30.89%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.63 (n/a)</td><td>4.66 (n/a)</td><td>4.69 (n/a)</td><td>3.82 (n/a)</td><td>0.77 (n/a)</td><td>9118.30 (n/a)</td><td>7656.82 (n/a)</td><td>7435.40 (n/a)</td><td>6191.70 (n/a)</td><td>1273.29 (n/a)</td><td>346.83 (n/a)</td><td>286.78 (n/a)</td><td>288.82 (n/a)</td><td>235.51 (n/a)</td><td>47.67 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>6.75 (+4.52%)</td><td>5.85 (+1.24%)</td><td>6.12 (+2.29%)</td><td>4.99 (-1.09%)</td><td>0.73 (+6.80%)</td><td>6985.70 (+1.10%)</td><td>6032.34 (-1.10%)</td><td>5699.20 (-2.24%)</td><td>5168.00 (-4.33%)</td><td>765.85 (+3.53%)</td><td>415.54 (+4.52%)</td><td>360.54 (+1.24%)</td><td>376.80 (+2.29%)</td><td>307.41 (-1.09%)</td><td>44.91 (+6.80%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>6.45 (n/a)</td><td>5.78 (n/a)</td><td>5.98 (n/a)</td><td>5.05 (n/a)</td><td>0.68 (n/a)</td><td>6909.60 (n/a)</td><td>6099.72 (n/a)</td><td>5829.60 (n/a)</td><td>5401.70 (n/a)</td><td>739.76 (n/a)</td><td>397.56 (n/a)</td><td>356.14 (n/a)</td><td>368.38 (n/a)</td><td>310.80 (n/a)</td><td>42.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.78 (+1.30%)</td><td>0.77 (+0.96%)</td><td>0.77 (+0.62%)</td><td>0.75 (+0.94%)</td><td>0.01 (+2.77%)</td><td>100737.70 (-0.93%)</td><td>98527.78 (-0.95%)</td><td>98307.10 (-0.62%)</td><td>97215.90 (-1.29%)</td><td>1323.37 (+0.70%)</td><td>706.87 (+1.30%)</td><td>697.56 (+0.96%)</td><td>699.03 (+0.62%)</td><td>682.16 (+0.94%)</td><td>9.26 (+2.77%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101684.90 (n/a)</td><td>99468.84 (n/a)</td><td>98916.50 (n/a)</td><td>98484.10 (n/a)</td><td>1314.17 (n/a)</td><td>697.77 (n/a)</td><td>690.96 (n/a)</td><td>694.72 (n/a)</td><td>675.81 (n/a)</td><td>9.01 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.77 (+3.52%)</td><td>0.76 (+2.60%)</td><td>0.77 (+3.81%)</td><td>0.72 (-1.16%)</td><td>0.02 <b>(+270.52%)</b></td><td>104704.10 (+1.17%)</td><td>99661.36 (-2.48%)</td><td>98266.70 (-3.67%)</td><td>97898.40 (-3.40%)</td><td>2888.81 <b>(+262.17%)</b></td><td>701.95 (+3.52%)</td><td>689.98 (+2.60%)</td><td>699.32 (+3.81%)</td><td>656.32 (-1.16%)</td><td>19.33 <b>(+270.52%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.01 (n/a)</td><td>103491.20 (n/a)</td><td>102191.78 (n/a)</td><td>102010.30 (n/a)</td><td>101348.80 (n/a)</td><td>797.65 (n/a)</td><td>678.05 (n/a)</td><td>672.49 (n/a)</td><td>673.65 (n/a)</td><td>664.01 (n/a)</td><td>5.22 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.81 (-0.36%)</td><td>0.80 (-0.80%)</td><td>0.80 (-0.26%)</td><td>0.78 (-1.72%)</td><td>0.01 <b>(+51.10%)</b></td><td>97060.20 (+1.75%)</td><td>94861.62 (+0.81%)</td><td>94556.20 (+0.26%)</td><td>93244.20 (+0.36%)</td><td>1487.70 <b>(+54.48%)</b></td><td>736.98 (-0.36%)</td><td>724.56 (-0.80%)</td><td>726.76 (-0.26%)</td><td>708.01 (-1.72%)</td><td>11.29 <b>(+51.10%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95393.80 (n/a)</td><td>94095.68 (n/a)</td><td>94315.00 (n/a)</td><td>92913.10 (n/a)</td><td>963.00 (n/a)</td><td>739.61 (n/a)</td><td>730.38 (n/a)</td><td>728.62 (n/a)</td><td>720.38 (n/a)</td><td>7.47 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.34 (-0.69%)</td><td>2.33 (-2.46%)</td><td>1.76 <b>(-22.69%)</b></td><td>1.57 (+0.63%)</td><td>0.90 (+15.59%)</td><td>5143.60 (-0.63%)</td><td>3869.94 (+5.10%)</td><td>4592.60 <b>(+29.35%)</b></td><td>2411.30 (+0.69%)</td><td>1329.38 (+10.88%)</td><td>876.67 (-0.69%)</td><td>611.15 (-2.46%)</td><td>460.29 <b>(-22.69%)</b></td><td>410.99 (+0.63%)</td><td>236.88 (+15.59%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.37 (n/a)</td><td>2.39 (n/a)</td><td>2.27 (n/a)</td><td>1.56 (n/a)</td><td>0.78 (n/a)</td><td>5176.10 (n/a)</td><td>3682.30 (n/a)</td><td>3550.50 (n/a)</td><td>2394.80 (n/a)</td><td>1198.91 (n/a)</td><td>882.73 (n/a)</td><td>626.55 (n/a)</td><td>595.39 (n/a)</td><td>408.40 (n/a)</td><td>204.93 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.24 (+12.76%)</td><td>0.20 (+1.54%)</td><td>0.21 (+1.52%)</td><td>0.17 (-8.35%)</td><td>0.03 <b>(+135.79%)</b></td><td>7397.90 (+9.11%)</td><td>6243.82 (-0.36%)</td><td>6001.20 (-1.50%)</td><td>5217.30 (-11.32%)</td><td>838.44 <b>(+128.81%)</b></td><td>12.86 (+12.76%)</td><td>10.90 (+1.54%)</td><td>11.18 (+1.52%)</td><td>9.07 (-8.35%)</td><td>1.45 <b>(+135.79%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>6780.00 (n/a)</td><td>6266.60 (n/a)</td><td>6092.30 (n/a)</td><td>5883.00 (n/a)</td><td>366.44 (n/a)</td><td>11.41 (n/a)</td><td>10.74 (n/a)</td><td>11.02 (n/a)</td><td>9.90 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (+12.80%)</td><td>0.10 <b>(+36.44%)</b></td><td>0.09 <b>(+41.55%)</b></td><td>0.08 <b>(+38.81%)</b></td><td>0.02 (-7.00%)</td><td>0.11 (+12.80%)</td><td>0.09 <b>(+36.44%)</b></td><td>0.09 <b>(+41.55%)</b></td><td>0.07 <b>(+38.81%)</b></td><td>0.02 (-7.00%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.91 (-0.41%)</td><td>3.69 (+2.39%)</td><td>3.79 (+2.64%)</td><td>3.44 (+7.42%)</td><td>0.21 <b>(-32.93%)</b></td><td>3.91 (-0.41%)</td><td>3.69 (+2.39%)</td><td>3.79 (+2.64%)</td><td>3.44 (+7.42%)</td><td>0.21 <b>(-32.93%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.93 (n/a)</td><td>3.61 (n/a)</td><td>3.70 (n/a)</td><td>3.21 (n/a)</td><td>0.31 (n/a)</td><td>3.93 (n/a)</td><td>3.60 (n/a)</td><td>3.69 (n/a)</td><td>3.20 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>7.21 (-5.54%)</td><td>6.81 (+7.88%)</td><td>6.75 (+3.55%)</td><td>6.64 <b>(+27.96%)</b></td><td>0.23 <b>(-76.39%)</b></td><td>7.20 (-5.54%)</td><td>6.80 (+7.88%)</td><td>6.75 (+3.55%)</td><td>6.63 <b>(+27.96%)</b></td><td>0.23 <b>(-76.39%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>7.63 (n/a)</td><td>6.31 (n/a)</td><td>6.52 (n/a)</td><td>5.19 (n/a)</td><td>0.99 (n/a)</td><td>7.63 (n/a)</td><td>6.31 (n/a)</td><td>6.51 (n/a)</td><td>5.18 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>13.25 (-6.85%)</td><td>9.93 (-8.10%)</td><td>8.39 (-16.81%)</td><td>7.30 (-10.44%)</td><td>2.72 (-5.26%)</td><td>13.24 (-6.85%)</td><td>9.92 (-8.10%)</td><td>8.38 (-16.81%)</td><td>7.29 (-10.44%)</td><td>2.72 (-5.26%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>14.22 (n/a)</td><td>10.80 (n/a)</td><td>10.08 (n/a)</td><td>8.15 (n/a)</td><td>2.87 (n/a)</td><td>14.21 (n/a)</td><td>10.80 (n/a)</td><td>10.07 (n/a)</td><td>8.14 (n/a)</td><td>2.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.90 (-0.34%)</td><td>3.65 (-1.37%)</td><td>3.78 (+0.78%)</td><td>3.02 (-10.24%)</td><td>0.36 <b>(+75.92%)</b></td><td>3.90 (-0.34%)</td><td>3.65 (-1.37%)</td><td>3.78 (+0.78%)</td><td>3.02 (-10.24%)</td><td>0.36 <b>(+75.92%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.91 (n/a)</td><td>3.71 (n/a)</td><td>3.75 (n/a)</td><td>3.36 (n/a)</td><td>0.20 (n/a)</td><td>3.91 (n/a)</td><td>3.70 (n/a)</td><td>3.75 (n/a)</td><td>3.36 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>7.26 (-2.46%)</td><td>6.49 (-3.26%)</td><td>6.76 (-1.65%)</td><td>5.50 (-2.90%)</td><td>0.74 (+13.69%)</td><td>7.25 (-2.46%)</td><td>6.49 (-3.26%)</td><td>6.76 (-1.65%)</td><td>5.50 (-2.90%)</td><td>0.74 (+13.69%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>7.44 (n/a)</td><td>6.71 (n/a)</td><td>6.88 (n/a)</td><td>5.67 (n/a)</td><td>0.65 (n/a)</td><td>7.44 (n/a)</td><td>6.71 (n/a)</td><td>6.87 (n/a)</td><td>5.66 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>13.84 (-6.35%)</td><td>9.49 (-12.75%)</td><td>8.57 (-15.27%)</td><td>8.19 (+0.91%)</td><td>2.44 (-8.17%)</td><td>13.83 (-6.35%)</td><td>9.49 (-12.75%)</td><td>8.57 (-15.27%)</td><td>8.19 (+0.91%)</td><td>2.44 (-8.17%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>14.77 (n/a)</td><td>10.88 (n/a)</td><td>10.12 (n/a)</td><td>8.12 (n/a)</td><td>2.65 (n/a)</td><td>14.76 (n/a)</td><td>10.87 (n/a)</td><td>10.11 (n/a)</td><td>8.11 (n/a)</td><td>2.65 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.50 (n/a)</td><td>399.98 (n/a)</td><td>392.90 (n/a)</td><td>249.60 (n/a)</td><td>142.75 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.40 (n/a)</td><td>404.06 (n/a)</td><td>460.30 (n/a)</td><td>248.80 (n/a)</td><td>136.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.50 (n/a)</td><td>398.64 (n/a)</td><td>439.90 (n/a)</td><td>221.30 (n/a)</td><td>138.64 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1902.90 (n/a)</td><td>655.12 (n/a)</td><td>313.00 (n/a)</td><td>279.00 (n/a)</td><td>703.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>678.60 (n/a)</td><td>475.90 (n/a)</td><td>449.00 (n/a)</td><td>321.30 (n/a)</td><td>146.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1953.20 (n/a)</td><td>765.34 (n/a)</td><td>504.10 (n/a)</td><td>341.60 (n/a)</td><td>668.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.80 (n/a)</td><td>359.74 (n/a)</td><td>297.10 (n/a)</td><td>265.00 (n/a)</td><td>111.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.40 (n/a)</td><td>363.84 (n/a)</td><td>376.90 (n/a)</td><td>231.00 (n/a)</td><td>112.59 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.60 (n/a)</td><td>397.38 (n/a)</td><td>395.30 (n/a)</td><td>241.20 (n/a)</td><td>123.25 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1127.40 (n/a)</td><td>536.42 (n/a)</td><td>431.80 (n/a)</td><td>293.10 (n/a)</td><td>337.51 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.10 (n/a)</td><td>347.04 (n/a)</td><td>268.40 (n/a)</td><td>228.00 (n/a)</td><td>131.17 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.90 (n/a)</td><td>476.88 (n/a)</td><td>440.50 (n/a)</td><td>396.80 (n/a)</td><td>85.64 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>585.60 (n/a)</td><td>382.82 (n/a)</td><td>314.90 (n/a)</td><td>270.50 (n/a)</td><td>130.36 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>514.10 (n/a)</td><td>388.00 (n/a)</td><td>370.10 (n/a)</td><td>269.00 (n/a)</td><td>109.89 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>532.20 (n/a)</td><td>369.42 (n/a)</td><td>338.50 (n/a)</td><td>266.80 (n/a)</td><td>107.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>667.10 (n/a)</td><td>456.46 (n/a)</td><td>443.10 (n/a)</td><td>210.40 (n/a)</td><td>165.61 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>536.30 (n/a)</td><td>421.92 (n/a)</td><td>476.00 (n/a)</td><td>186.30 (n/a)</td><td>137.47 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.10 (n/a)</td><td>448.72 (n/a)</td><td>489.40 (n/a)</td><td>320.90 (n/a)</td><td>120.04 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (-0.67%)</td><td>0.07 (-14.99%)</td><td>0.06 <b>(-31.83%)</b></td><td>0.03 <b>(-33.53%)</b></td><td>0.03 <b>(+23.99%)</b></td><td>1014.30 <b>(+50.44%)</b></td><td>559.44 <b>(+29.71%)</b></td><td>519.10 <b>(+46.68%)</b></td><td>303.20 (+0.66%)</td><td>287.61 <b>(+82.08%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>674.20 (n/a)</td><td>431.30 (n/a)</td><td>353.90 (n/a)</td><td>301.20 (n/a)</td><td>157.96 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>612.50 (n/a)</td><td>463.34 (n/a)</td><td>538.50 (n/a)</td><td>271.10 (n/a)</td><td>165.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>581.50 (n/a)</td><td>435.20 (n/a)</td><td>442.00 (n/a)</td><td>195.80 (n/a)</td><td>150.94 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>620.50 (n/a)</td><td>365.44 (n/a)</td><td>258.00 (n/a)</td><td>215.70 (n/a)</td><td>176.34 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>581.60 (n/a)</td><td>415.58 (n/a)</td><td>434.40 (n/a)</td><td>233.30 (n/a)</td><td>129.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>562.20 (n/a)</td><td>487.36 (n/a)</td><td>514.70 (n/a)</td><td>375.90 (n/a)</td><td>73.82 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (+6.56%)</td><td>0.01 <b>(-27.68%)</b></td><td>0.01 <b>(-48.71%)</b></td><td>0.00 <b>(-47.51%)</b></td><td>0.01 <b>(+54.41%)</b></td><td>1036.20 <b>(+90.51%)</b></td><td>543.76 <b>(+68.17%)</b></td><td>553.60 <b>(+95.00%)</b></td><td>217.80 (-6.12%)</td><td>317.71 <b>(+152.51%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.90 (n/a)</td><td>323.34 (n/a)</td><td>283.90 (n/a)</td><td>232.00 (n/a)</td><td>125.82 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(+57.43%)</b></td><td>0.01 <b>(+35.76%)</b></td><td>0.01 <b>(+31.78%)</b></td><td>0.01 (-1.10%)</td><td>0.00 <b>(+150.30%)</b></td><td>508.50 (+1.11%)</td><td>320.70 <b>(-21.05%)</b></td><td>297.30 <b>(-24.10%)</b></td><td>203.70 <b>(-36.48%)</b></td><td>116.75 <b>(+63.46%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.90 (n/a)</td><td>406.22 (n/a)</td><td>391.70 (n/a)</td><td>320.70 (n/a)</td><td>71.42 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (+10.01%)</td><td>0.01 (+3.06%)</td><td>0.01 <b>(-24.11%)</b></td><td>0.01 (+8.99%)</td><td>0.01 <b>(+49.59%)</b></td><td>511.60 (-8.25%)</td><td>368.74 (+2.73%)</td><td>440.30 <b>(+31.79%)</b></td><td>213.20 (-9.12%)</td><td>137.61 (+15.15%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>557.60 (n/a)</td><td>358.94 (n/a)</td><td>334.10 (n/a)</td><td>234.60 (n/a)</td><td>119.51 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (+18.26%)</td><td>0.01 (+7.67%)</td><td>0.01 (-14.93%)</td><td>0.01 <b>(-27.00%)</b></td><td>0.01 <b>(+57.60%)</b></td><td>721.10 <b>(+36.99%)</b></td><td>401.50 (+4.74%)</td><td>403.70 (+17.56%)</td><td>201.80 (-15.42%)</td><td>207.92 <b>(+65.57%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>526.40 (n/a)</td><td>383.32 (n/a)</td><td>343.40 (n/a)</td><td>238.60 (n/a)</td><td>125.58 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(+43.71%)</b></td><td>0.01 <b>(+20.08%)</b></td><td>0.01 <b>(+35.07%)</b></td><td>0.01 (+15.25%)</td><td>0.01 <b>(+43.03%)</b></td><td>490.60 (-13.23%)</td><td>368.62 (-14.98%)</td><td>381.00 <b>(-25.96%)</b></td><td>184.70 <b>(-30.43%)</b></td><td>126.46 (-12.54%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.40 (n/a)</td><td>433.56 (n/a)</td><td>514.60 (n/a)</td><td>265.50 (n/a)</td><td>144.59 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (+9.04%)</td><td>0.01 (-12.19%)</td><td>0.01 (-14.46%)</td><td>0.01 <b>(-31.46%)</b></td><td>0.00 <b>(+77.21%)</b></td><td>637.50 <b>(+45.91%)</b></td><td>421.86 <b>(+24.48%)</b></td><td>359.00 (+16.90%)</td><td>248.00 (-8.28%)</td><td>162.71 <b>(+141.88%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>436.90 (n/a)</td><td>338.90 (n/a)</td><td>307.10 (n/a)</td><td>270.40 (n/a)</td><td>67.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (-18.19%)</td><td>0.01 (+0.93%)</td><td>0.01 (+2.25%)</td><td>0.01 (+4.22%)</td><td>0.00 <b>(-38.23%)</b></td><td>587.10 (-4.05%)</td><td>470.70 (-4.27%)</td><td>462.50 (-2.20%)</td><td>373.10 <b>(+22.25%)</b></td><td>89.73 <b>(-28.39%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.90 (n/a)</td><td>491.68 (n/a)</td><td>472.90 (n/a)</td><td>305.20 (n/a)</td><td>125.30 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(+133.13%)</b></td><td>0.01 <b>(+74.07%)</b></td><td>0.01 (+7.87%)</td><td>0.01 <b>(+354.51%)</b></td><td>0.01 <b>(+82.56%)</b></td><td>532.20 <b>(-78.00%)</b></td><td>411.20 <b>(-55.00%)</b></td><td>488.50 (-7.29%)</td><td>208.40 <b>(-57.09%)</b></td><td>139.20 <b>(-83.49%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2419.00 (n/a)</td><td>913.86 (n/a)</td><td>526.90 (n/a)</td><td>485.70 (n/a)</td><td>843.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (-7.55%)</td><td>0.01 (-13.21%)</td><td>0.01 (-12.31%)</td><td>0.01 <b>(-23.47%)</b></td><td>0.01 (-0.16%)</td><td>800.40 <b>(+30.68%)</b></td><td>483.52 <b>(+21.71%)</b></td><td>453.20 (+14.07%)</td><td>241.00 (+8.17%)</td><td>236.00 <b>(+43.05%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.50 (n/a)</td><td>397.26 (n/a)</td><td>397.30 (n/a)</td><td>222.80 (n/a)</td><td>164.98 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (+13.20%)</td><td>0.01 (-9.98%)</td><td>0.01 <b>(-27.14%)</b></td><td>0.01 (-5.22%)</td><td>0.00 (+15.04%)</td><td>711.90 (+5.50%)</td><td>476.62 (+12.25%)</td><td>486.10 <b>(+37.24%)</b></td><td>238.50 (-11.67%)</td><td>167.87 (-0.59%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>674.80 (n/a)</td><td>424.62 (n/a)</td><td>354.20 (n/a)</td><td>270.00 (n/a)</td><td>168.86 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (-2.48%)</td><td>0.01 (+1.99%)</td><td>0.01 (+3.90%)</td><td>0.01 (+6.70%)</td><td>0.00 (-9.52%)</td><td>554.60 (-6.27%)</td><td>418.00 (-3.40%)</td><td>414.10 (-3.76%)</td><td>281.40 (+2.51%)</td><td>110.82 (-12.65%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.70 (n/a)</td><td>432.72 (n/a)</td><td>430.30 (n/a)</td><td>274.50 (n/a)</td><td>126.86 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (-7.42%)</td><td>0.01 (-18.28%)</td><td>0.01 (-17.58%)</td><td>0.01 <b>(-32.15%)</b></td><td>0.00 (+14.62%)</td><td>803.50 <b>(+47.38%)</b></td><td>549.14 <b>(+29.54%)</b></td><td>557.10 <b>(+21.35%)</b></td><td>286.60 (+7.99%)</td><td>189.45 <b>(+81.74%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.20 (n/a)</td><td>423.92 (n/a)</td><td>459.10 (n/a)</td><td>265.40 (n/a)</td><td>104.24 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (-6.29%)</td><td>0.02 (+4.55%)</td><td>0.02 (+0.94%)</td><td>0.01 (-16.54%)</td><td>0.01 (+3.41%)</td><td>626.20 (+19.82%)</td><td>429.86 (-1.95%)</td><td>468.70 (-0.91%)</td><td>268.40 (+6.72%)</td><td>144.27 <b>(+35.01%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.60 (n/a)</td><td>438.40 (n/a)</td><td>473.00 (n/a)</td><td>251.50 (n/a)</td><td>106.86 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (-8.27%)</td><td>0.02 (-3.99%)</td><td>0.03 (+4.16%)</td><td>0.01 (-14.92%)</td><td>0.01 (+5.36%)</td><td>580.30 (+17.54%)</td><td>358.42 (+6.54%)</td><td>290.90 (-3.99%)</td><td>274.50 (+9.02%)</td><td>130.09 <b>(+33.08%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.70 (n/a)</td><td>336.42 (n/a)</td><td>303.00 (n/a)</td><td>251.80 (n/a)</td><td>97.75 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (-10.17%)</td><td>0.02 (+1.83%)</td><td>0.02 (-0.36%)</td><td>0.01 (-5.61%)</td><td>0.01 (-5.82%)</td><td>636.10 (+5.95%)</td><td>409.32 (-2.06%)</td><td>412.60 (+0.36%)</td><td>237.70 (+11.33%)</td><td>168.01 (+2.89%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.40 (n/a)</td><td>417.92 (n/a)</td><td>411.10 (n/a)</td><td>213.50 (n/a)</td><td>163.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (+2.13%)</td><td>0.02 (+7.04%)</td><td>0.02 (-1.94%)</td><td>0.02 (+13.27%)</td><td>0.01 (-9.20%)</td><td>476.80 (-11.70%)</td><td>355.66 (-9.29%)</td><td>380.30 (+1.98%)</td><td>228.20 (-2.10%)</td><td>96.94 <b>(-25.20%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.00 (n/a)</td><td>392.08 (n/a)</td><td>372.90 (n/a)</td><td>233.10 (n/a)</td><td>129.60 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (+3.36%)</td><td>0.03 <b>(+30.42%)</b></td><td>0.03 <b>(+43.21%)</b></td><td>0.02 <b>(+49.54%)</b></td><td>0.00 <b>(-27.01%)</b></td><td>423.00 <b>(-33.12%)</b></td><td>325.62 <b>(-26.92%)</b></td><td>301.70 <b>(-30.18%)</b></td><td>255.80 (-3.25%)</td><td>65.31 <b>(-50.21%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>632.50 (n/a)</td><td>445.58 (n/a)</td><td>432.10 (n/a)</td><td>264.40 (n/a)</td><td>131.16 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (+9.23%)</td><td>0.03 <b>(+28.11%)</b></td><td>0.03 <b>(+37.64%)</b></td><td>0.03 <b>(+52.52%)</b></td><td>0.01 <b>(-29.17%)</b></td><td>315.60 <b>(-34.44%)</b></td><td>265.60 <b>(-25.70%)</b></td><td>239.30 <b>(-27.33%)</b></td><td>225.60 (-8.44%)</td><td>45.22 <b>(-57.68%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.40 (n/a)</td><td>357.46 (n/a)</td><td>329.30 (n/a)</td><td>246.40 (n/a)</td><td>106.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 <b>(-33.64%)</b></td><td>0.02 (-12.48%)</td><td>0.02 (+5.94%)</td><td>0.01 <b>(-22.74%)</b></td><td>0.01 <b>(-43.10%)</b></td><td>619.60 <b>(+29.43%)</b></td><td>403.94 (+9.21%)</td><td>375.90 (-5.60%)</td><td>274.50 <b>(+50.66%)</b></td><td>137.39 (+10.80%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.70 (n/a)</td><td>369.86 (n/a)</td><td>398.20 (n/a)</td><td>182.20 (n/a)</td><td>123.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 (+16.51%)</td><td>0.02 (-2.13%)</td><td>0.03 <b>(+21.72%)</b></td><td>0.00 <b>(-68.86%)</b></td><td>0.01 <b>(+79.23%)</b></td><td>1916.30 <b>(+221.10%)</b></td><td>680.72 <b>(+71.22%)</b></td><td>290.70 (-17.83%)</td><td>213.10 (-14.18%)</td><td>716.71 <b>(+403.53%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.80 (n/a)</td><td>397.56 (n/a)</td><td>353.80 (n/a)</td><td>248.30 (n/a)</td><td>142.34 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(-29.86%)</b></td><td>0.01 <b>(-24.79%)</b></td><td>0.02 <b>(-21.73%)</b></td><td>0.01 <b>(-24.38%)</b></td><td>0.00 <b>(-42.22%)</b></td><td>758.00 <b>(+32.24%)</b></td><td>581.12 <b>(+30.87%)</b></td><td>542.40 <b>(+27.77%)</b></td><td>456.70 <b>(+42.59%)</b></td><td>112.55 (+9.66%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.20 (n/a)</td><td>444.04 (n/a)</td><td>424.50 (n/a)</td><td>320.30 (n/a)</td><td>102.64 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (-5.58%)</td><td>0.02 (+11.83%)</td><td>0.02 <b>(+38.16%)</b></td><td>0.02 <b>(+21.91%)</b></td><td>0.01 <b>(-28.17%)</b></td><td>502.80 (-17.98%)</td><td>401.92 (-15.04%)</td><td>392.80 <b>(-27.62%)</b></td><td>276.50 (+5.94%)</td><td>91.75 <b>(-36.12%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.00 (n/a)</td><td>473.06 (n/a)</td><td>542.70 (n/a)</td><td>261.00 (n/a)</td><td>143.64 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 <b>(+59.01%)</b></td><td>0.02 <b>(+68.19%)</b></td><td>0.02 <b>(+49.96%)</b></td><td>0.02 <b>(+298.39%)</b></td><td>0.00 (-19.26%)</td><td>493.90 <b>(-74.90%)</b></td><td>378.00 <b>(-53.84%)</b></td><td>371.00 <b>(-33.31%)</b></td><td>287.40 <b>(-37.11%)</b></td><td>75.45 <b>(-88.29%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1967.60 (n/a)</td><td>818.82 (n/a)</td><td>556.30 (n/a)</td><td>457.00 (n/a)</td><td>644.39 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (+5.63%)</td><td>0.01 <b>(-20.15%)</b></td><td>0.01 <b>(-52.27%)</b></td><td>0.00 <b>(-65.11%)</b></td><td>0.01 <b>(+87.54%)</b></td><td>2024.30 <b>(+186.61%)</b></td><td>1034.74 <b>(+96.82%)</b></td><td>1124.20 <b>(+109.50%)</b></td><td>293.00 (-5.33%)</td><td>720.12 <b>(+394.59%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>706.30 (n/a)</td><td>525.74 (n/a)</td><td>536.60 (n/a)</td><td>309.50 (n/a)</td><td>145.60 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 <b>(-22.14%)</b></td><td>0.05 (-10.85%)</td><td>0.06 (+1.82%)</td><td>0.03 (-8.09%)</td><td>0.02 <b>(-28.01%)</b></td><td>525.60 (+8.80%)</td><td>328.86 (+9.58%)</td><td>281.70 (-1.78%)</td><td>219.00 <b>(+28.45%)</b></td><td>118.68 (+4.06%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>483.10 (n/a)</td><td>300.10 (n/a)</td><td>286.80 (n/a)</td><td>170.50 (n/a)</td><td>114.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 <b>(+66.26%)</b></td><td>0.06 (+10.64%)</td><td>0.06 (-0.22%)</td><td>0.04 (+13.51%)</td><td>0.03 <b>(+123.25%)</b></td><td>466.30 (-11.90%)</td><td>321.10 (-0.24%)</td><td>285.70 (+0.25%)</td><td>142.70 <b>(-39.87%)</b></td><td>132.01 (+11.96%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>529.30 (n/a)</td><td>321.86 (n/a)</td><td>285.00 (n/a)</td><td>237.30 (n/a)</td><td>117.91 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (-5.36%)</td><td>0.05 <b>(+24.13%)</b></td><td>0.05 <b>(+62.69%)</b></td><td>0.04 <b>(+324.87%)</b></td><td>0.01 <b>(-55.09%)</b></td><td>446.80 <b>(-76.46%)</b></td><td>322.26 <b>(-52.23%)</b></td><td>308.10 <b>(-38.54%)</b></td><td>237.60 (+5.69%)</td><td>79.56 <b>(-88.59%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1898.40 (n/a)</td><td>674.56 (n/a)</td><td>501.30 (n/a)</td><td>224.80 (n/a)</td><td>697.40 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 <b>(-39.61%)</b></td><td>0.04 <b>(-33.17%)</b></td><td>0.03 <b>(-46.50%)</b></td><td>0.03 <b>(+228.31%)</b></td><td>0.01 <b>(-76.20%)</b></td><td>584.60 <b>(-69.54%)</b></td><td>468.84 <b>(-20.32%)</b></td><td>486.10 <b>(+86.89%)</b></td><td>372.80 <b>(+65.62%)</b></td><td>81.92 <b>(-89.00%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1919.30 (n/a)</td><td>588.42 (n/a)</td><td>260.10 (n/a)</td><td>225.10 (n/a)</td><td>744.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (+7.50%)</td><td>0.04 (+5.67%)</td><td>0.04 (+9.28%)</td><td>0.03 (+3.45%)</td><td>0.01 (+11.46%)</td><td>572.90 (-3.34%)</td><td>433.64 (-4.61%)</td><td>452.20 (-8.50%)</td><td>268.50 (-7.00%)</td><td>122.67 (+1.21%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>592.70 (n/a)</td><td>454.62 (n/a)</td><td>494.20 (n/a)</td><td>288.70 (n/a)</td><td>121.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (+6.73%)</td><td>0.05 (-18.05%)</td><td>0.06 (-9.77%)</td><td>0.03 <b>(-41.15%)</b></td><td>0.02 <b>(+137.89%)</b></td><td>514.20 <b>(+69.93%)</b></td><td>349.50 <b>(+34.41%)</b></td><td>295.80 (+10.79%)</td><td>204.90 (-6.31%)</td><td>127.60 <b>(+294.36%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>302.60 (n/a)</td><td>260.02 (n/a)</td><td>267.00 (n/a)</td><td>218.70 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (-17.59%)</td><td>0.03 <b>(-40.14%)</b></td><td>0.03 <b>(-41.06%)</b></td><td>0.01 <b>(-69.52%)</b></td><td>0.02 <b>(+60.82%)</b></td><td>1357.10 <b>(+228.12%)</b></td><td>662.56 <b>(+107.69%)</b></td><td>516.70 <b>(+69.69%)</b></td><td>297.80 <b>(+21.35%)</b></td><td>410.66 <b>(+568.88%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>413.60 (n/a)</td><td>319.02 (n/a)</td><td>304.50 (n/a)</td><td>245.40 (n/a)</td><td>61.39 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (+9.32%)</td><td>0.04 <b>(-21.80%)</b></td><td>0.03 <b>(-43.95%)</b></td><td>0.01 (+8.52%)</td><td>0.03 (-2.02%)</td><td>1859.30 (-7.86%)</td><td>714.74 (+11.35%)</td><td>476.00 <b>(+78.41%)</b></td><td>210.50 (-8.56%)</td><td>660.85 (-14.64%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2017.80 (n/a)</td><td>641.90 (n/a)</td><td>266.80 (n/a)</td><td>230.20 (n/a)</td><td>774.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (-12.94%)</td><td>0.04 (-8.83%)</td><td>0.05 (+16.92%)</td><td>0.03 (-5.49%)</td><td>0.01 <b>(-33.97%)</b></td><td>561.50 (+5.80%)</td><td>395.26 (+5.48%)</td><td>350.20 (-14.46%)</td><td>282.10 (+14.86%)</td><td>108.63 (-12.24%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>530.70 (n/a)</td><td>374.74 (n/a)</td><td>409.40 (n/a)</td><td>245.60 (n/a)</td><td>123.77 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (+16.78%)</td><td>0.04 (+10.77%)</td><td>0.03 (+1.12%)</td><td>0.03 <b>(+69.21%)</b></td><td>0.02 (-0.16%)</td><td>599.90 <b>(-40.90%)</b></td><td>434.22 (-18.55%)</td><td>528.80 (-1.12%)</td><td>211.90 (-14.38%)</td><td>168.22 <b>(-45.57%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1015.10 (n/a)</td><td>533.12 (n/a)</td><td>534.80 (n/a)</td><td>247.50 (n/a)</td><td>309.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (-6.53%)</td><td>0.04 (+8.63%)</td><td>0.04 <b>(+22.22%)</b></td><td>0.03 <b>(+30.45%)</b></td><td>0.01 <b>(-39.36%)</b></td><td>534.60 <b>(-23.34%)</b></td><td>451.26 (-11.50%)</td><td>436.40 (-18.17%)</td><td>359.90 (+6.99%)</td><td>67.60 <b>(-49.29%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>697.40 (n/a)</td><td>509.92 (n/a)</td><td>533.30 (n/a)</td><td>336.40 (n/a)</td><td>133.32 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 <b>(+27.24%)</b></td><td>0.04 (+4.67%)</td><td>0.03 (-6.54%)</td><td>0.03 (-12.04%)</td><td>0.01 <b>(+100.70%)</b></td><td>643.10 (+13.68%)</td><td>482.28 (-0.52%)</td><td>487.00 (+7.01%)</td><td>311.40 <b>(-21.40%)</b></td><td>122.63 <b>(+70.46%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>565.70 (n/a)</td><td>484.80 (n/a)</td><td>455.10 (n/a)</td><td>396.20 (n/a)</td><td>71.94 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 <b>(-24.32%)</b></td><td>0.08 <b>(-33.32%)</b></td><td>0.08 <b>(-34.86%)</b></td><td>0.06 <b>(-44.83%)</b></td><td>0.02 <b>(+78.20%)</b></td><td>529.60 <b>(+81.25%)</b></td><td>409.16 <b>(+56.55%)</b></td><td>409.80 <b>(+53.54%)</b></td><td>301.70 <b>(+32.15%)</b></td><td>100.55 <b>(+322.96%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>292.20 (n/a)</td><td>261.36 (n/a)</td><td>266.90 (n/a)</td><td>228.30 (n/a)</td><td>23.77 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (-18.67%)</td><td>0.08 <b>(-26.78%)</b></td><td>0.08 <b>(-23.84%)</b></td><td>0.06 <b>(-28.45%)</b></td><td>0.02 (-9.04%)</td><td>549.30 <b>(+39.77%)</b></td><td>439.22 <b>(+38.48%)</b></td><td>429.80 <b>(+31.32%)</b></td><td>294.60 <b>(+22.95%)</b></td><td>100.56 <b>(+57.15%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>393.00 (n/a)</td><td>317.18 (n/a)</td><td>327.30 (n/a)</td><td>239.60 (n/a)</td><td>63.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 <b>(-20.26%)</b></td><td>0.07 <b>(-32.20%)</b></td><td>0.06 <b>(-48.80%)</b></td><td>0.02 <b>(-69.04%)</b></td><td>0.04 (+0.00%)</td><td>1898.80 <b>(+222.98%)</b></td><td>720.74 <b>(+103.14%)</b></td><td>510.00 <b>(+95.33%)</b></td><td>263.00 <b>(+25.42%)</b></td><td>676.19 <b>(+304.26%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>587.90 (n/a)</td><td>354.80 (n/a)</td><td>261.10 (n/a)</td><td>209.70 (n/a)</td><td>167.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (-18.62%)</td><td>0.08 <b>(-34.50%)</b></td><td>0.07 <b>(-49.25%)</b></td><td>0.06 (+6.63%)</td><td>0.03 <b>(-29.92%)</b></td><td>523.10 (-6.22%)</td><td>437.44 <b>(+44.23%)</b></td><td>478.80 <b>(+97.04%)</b></td><td>261.70 <b>(+22.86%)</b></td><td>104.42 <b>(-27.27%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>557.80 (n/a)</td><td>303.30 (n/a)</td><td>243.00 (n/a)</td><td>213.00 (n/a)</td><td>143.56 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (-13.21%)</td><td>0.07 <b>(-38.94%)</b></td><td>0.06 <b>(-32.72%)</b></td><td>0.01 <b>(-85.57%)</b></td><td>0.04 <b>(+72.14%)</b></td><td>2492.60 <b>(+592.77%)</b></td><td>854.86 <b>(+171.64%)</b></td><td>523.50 <b>(+48.64%)</b></td><td>286.80 (+15.23%)</td><td>921.40 <b>(+1488.05%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>359.80 (n/a)</td><td>314.70 (n/a)</td><td>352.20 (n/a)</td><td>248.90 (n/a)</td><td>58.02 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 <b>(-23.43%)</b></td><td>0.07 <b>(-26.49%)</b></td><td>0.06 <b>(-36.44%)</b></td><td>0.02 <b>(-66.05%)</b></td><td>0.04 (-3.38%)</td><td>1928.40 <b>(+194.55%)</b></td><td>727.44 <b>(+80.26%)</b></td><td>530.40 <b>(+57.34%)</b></td><td>314.50 <b>(+30.61%)</b></td><td>680.14 <b>(+283.14%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>654.70 (n/a)</td><td>403.54 (n/a)</td><td>337.10 (n/a)</td><td>240.80 (n/a)</td><td>177.52 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 <b>(-25.36%)</b></td><td>0.08 <b>(-32.22%)</b></td><td>0.06 <b>(-46.42%)</b></td><td>0.05 <b>(-31.41%)</b></td><td>0.03 (+7.05%)</td><td>624.30 <b>(+45.80%)</b></td><td>465.10 <b>(+56.86%)</b></td><td>536.50 <b>(+86.61%)</b></td><td>287.90 <b>(+33.97%)</b></td><td>163.79 <b>(+97.54%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>428.20 (n/a)</td><td>296.50 (n/a)</td><td>287.50 (n/a)</td><td>214.90 (n/a)</td><td>82.91 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 <b>(+24.98%)</b></td><td>0.09 (-0.49%)</td><td>0.06 <b>(-34.06%)</b></td><td>0.06 (+0.59%)</td><td>0.04 <b>(+48.00%)</b></td><td>583.30 (-0.58%)</td><td>434.18 (+7.74%)</td><td>518.90 <b>(+51.64%)</b></td><td>210.50 (-19.96%)</td><td>173.24 (+19.94%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>586.70 (n/a)</td><td>402.98 (n/a)</td><td>342.20 (n/a)</td><td>263.00 (n/a)</td><td>144.44 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 <b>(-46.54%)</b></td><td>0.06 <b>(-34.80%)</b></td><td>0.06 <b>(-22.34%)</b></td><td>0.05 <b>(-24.15%)</b></td><td>0.01 <b>(-73.77%)</b></td><td>615.10 <b>(+31.85%)</b></td><td>550.18 <b>(+44.74%)</b></td><td>572.10 <b>(+28.76%)</b></td><td>454.60 <b>(+87.08%)</b></td><td>64.51 <b>(-37.32%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>466.50 (n/a)</td><td>380.12 (n/a)</td><td>444.30 (n/a)</td><td>243.00 (n/a)</td><td>102.91 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 <b>(+22.29%)</b></td><td>0.09 <b>(+36.57%)</b></td><td>0.11 <b>(+74.73%)</b></td><td>0.02 <b>(-60.49%)</b></td><td>0.05 <b>(+86.60%)</b></td><td>1933.30 <b>(+153.12%)</b></td><td>637.82 <b>(+20.02%)</b></td><td>301.00 <b>(-42.76%)</b></td><td>234.90 (-18.21%)</td><td>730.03 <b>(+331.85%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>763.80 (n/a)</td><td>531.42 (n/a)</td><td>525.90 (n/a)</td><td>287.20 (n/a)</td><td>169.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (+19.52%)</td><td>0.07 (+4.04%)</td><td>0.08 <b>(+32.07%)</b></td><td>0.02 <b>(-66.32%)</b></td><td>0.04 <b>(+62.53%)</b></td><td>1944.10 <b>(+196.95%)</b></td><td>716.98 <b>(+40.63%)</b></td><td>430.20 <b>(-24.29%)</b></td><td>256.20 (-16.33%)</td><td>696.95 <b>(+336.42%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>654.70 (n/a)</td><td>509.84 (n/a)</td><td>568.20 (n/a)</td><td>306.20 (n/a)</td><td>159.70 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 <b>(+28.66%)</b></td><td>0.10 <b>(+21.68%)</b></td><td>0.12 <b>(+49.35%)</b></td><td>0.05 (+4.48%)</td><td>0.05 <b>(+64.11%)</b></td><td>638.20 (-4.29%)</td><td>386.98 (-9.20%)</td><td>272.60 <b>(-33.04%)</b></td><td>205.80 <b>(-22.28%)</b></td><td>196.08 <b>(+27.66%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>666.80 (n/a)</td><td>426.20 (n/a)</td><td>407.10 (n/a)</td><td>264.80 (n/a)</td><td>153.59 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(+25.95%)</b></td><td>0.01 <b>(+26.57%)</b></td><td>0.01 (+7.15%)</td><td>0.01 <b>(+319.20%)</b></td><td>0.00 <b>(-29.07%)</b></td><td>466.80 <b>(-76.14%)</b></td><td>305.00 <b>(-51.74%)</b></td><td>275.80 (-6.70%)</td><td>229.90 <b>(-20.61%)</b></td><td>96.99 <b>(-86.91%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1956.80 (n/a)</td><td>632.02 (n/a)</td><td>295.60 (n/a)</td><td>289.60 (n/a)</td><td>740.72 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(+32.55%)</b></td><td>0.01 <b>(+30.80%)</b></td><td>0.01 (+16.94%)</td><td>0.01 <b>(+235.58%)</b></td><td>0.00 (-8.26%)</td><td>630.80 <b>(-70.20%)</b></td><td>514.12 <b>(-41.06%)</b></td><td>555.00 (-14.50%)</td><td>305.50 <b>(-24.57%)</b></td><td>127.34 <b>(-81.96%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2117.00 (n/a)</td><td>872.30 (n/a)</td><td>649.10 (n/a)</td><td>405.00 (n/a)</td><td>705.80 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 <b>(+27.65%)</b></td><td>0.01 (+18.51%)</td><td>0.01 (+19.97%)</td><td>0.01 (+5.41%)</td><td>0.01 <b>(+36.69%)</b></td><td>569.70 (-5.13%)</td><td>425.04 (-11.84%)</td><td>447.50 (-16.65%)</td><td>162.80 <b>(-21.69%)</b></td><td>156.05 (-3.42%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.50 (n/a)</td><td>482.12 (n/a)</td><td>536.90 (n/a)</td><td>207.90 (n/a)</td><td>161.58 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(+45.10%)</b></td><td>0.02 (+1.54%)</td><td>0.02 (-1.16%)</td><td>0.01 <b>(-29.47%)</b></td><td>0.01 <b>(+166.28%)</b></td><td>638.20 <b>(+41.79%)</b></td><td>393.24 (+13.23%)</td><td>310.80 (+1.17%)</td><td>207.90 <b>(-31.09%)</b></td><td>179.49 <b>(+175.78%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>450.10 (n/a)</td><td>347.30 (n/a)</td><td>307.20 (n/a)</td><td>301.70 (n/a)</td><td>65.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (+14.25%)</td><td>0.01 (-1.60%)</td><td>0.01 (-7.43%)</td><td>0.01 (+6.15%)</td><td>0.00 (+0.41%)</td><td>539.50 (-5.80%)</td><td>418.00 (-0.68%)</td><td>425.80 (+8.02%)</td><td>242.60 (-12.45%)</td><td>109.46 <b>(-24.11%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.70 (n/a)</td><td>420.86 (n/a)</td><td>394.20 (n/a)</td><td>277.10 (n/a)</td><td>144.24 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 <b>(+44.31%)</b></td><td>0.02 <b>(+23.49%)</b></td><td>0.01 (-3.43%)</td><td>0.01 (-12.56%)</td><td>0.01 <b>(+83.66%)</b></td><td>597.70 (+14.37%)</td><td>426.22 (-5.71%)</td><td>534.00 (+3.55%)</td><td>158.50 <b>(-30.70%)</b></td><td>192.39 <b>(+52.30%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>522.60 (n/a)</td><td>452.04 (n/a)</td><td>515.70 (n/a)</td><td>228.70 (n/a)</td><td>126.33 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 (-7.06%)</td><td>0.01 (-6.59%)</td><td>0.01 <b>(-29.34%)</b></td><td>0.01 <b>(+36.35%)</b></td><td>0.00 <b>(-32.05%)</b></td><td>561.80 <b>(-26.66%)</b></td><td>427.06 (-5.24%)</td><td>476.80 <b>(+41.48%)</b></td><td>278.00 (+7.59%)</td><td>127.44 <b>(-45.62%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>766.00 (n/a)</td><td>450.68 (n/a)</td><td>337.00 (n/a)</td><td>258.40 (n/a)</td><td>234.35 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 <b>(+33.21%)</b></td><td>0.01 (+18.92%)</td><td>0.01 (+19.11%)</td><td>0.01 <b>(+24.96%)</b></td><td>0.00 <b>(+50.74%)</b></td><td>548.00 (-19.98%)</td><td>445.18 (-14.21%)</td><td>455.00 (-16.05%)</td><td>254.90 <b>(-24.92%)</b></td><td>117.40 (-9.75%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>684.80 (n/a)</td><td>518.92 (n/a)</td><td>542.00 (n/a)</td><td>339.50 (n/a)</td><td>130.09 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (+10.61%)</td><td>0.01 (+11.70%)</td><td>0.01 (+11.65%)</td><td>0.01 <b>(+42.00%)</b></td><td>0.00 (-8.56%)</td><td>462.90 <b>(-29.59%)</b></td><td>333.42 (-15.65%)</td><td>279.50 (-10.42%)</td><td>220.60 (-9.59%)</td><td>112.68 <b>(-37.27%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>657.40 (n/a)</td><td>395.28 (n/a)</td><td>312.00 (n/a)</td><td>244.00 (n/a)</td><td>179.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.01 <b>(-37.64%)</b></td><td>0.01 <b>(-24.19%)</b></td><td>0.01 (-8.89%)</td><td>0.00 <b>(-57.49%)</b></td><td>0.00 (-12.15%)</td><td>1036.70 <b>(+135.24%)</b></td><td>485.24 <b>(+50.33%)</b></td><td>347.60 (+9.76%)</td><td>323.30 <b>(+60.37%)</b></td><td>309.58 <b>(+252.25%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>440.70 (n/a)</td><td>322.78 (n/a)</td><td>316.70 (n/a)</td><td>201.60 (n/a)</td><td>87.88 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.02 (-1.39%)</td><td>0.01 (+2.83%)</td><td>0.01 (-6.81%)</td><td>0.01 <b>(+20.88%)</b></td><td>0.00 (-4.23%)</td><td>551.40 (-17.27%)</td><td>415.78 (-4.96%)</td><td>480.60 (+7.30%)</td><td>265.40 (+1.41%)</td><td>131.09 (-19.65%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>666.50 (n/a)</td><td>437.48 (n/a)</td><td>447.90 (n/a)</td><td>261.70 (n/a)</td><td>163.15 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (-8.33%)</td><td>0.02 (+12.38%)</td><td>0.02 (-1.36%)</td><td>0.02 <b>(+263.97%)</b></td><td>0.01 <b>(-48.01%)</b></td><td>526.40 <b>(-72.53%)</b></td><td>400.10 <b>(-57.23%)</b></td><td>446.10 (+1.36%)</td><td>235.90 (+9.11%)</td><td>129.75 <b>(-85.27%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1916.00 (n/a)</td><td>935.50 (n/a)</td><td>440.10 (n/a)</td><td>216.20 (n/a)</td><td>880.90 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 <b>(-25.45%)</b></td><td>0.03 <b>(-27.29%)</b></td><td>0.02 (-15.57%)</td><td>0.02 (-15.83%)</td><td>0.01 <b>(-35.30%)</b></td><td>579.30 (+18.81%)</td><td>473.50 <b>(+31.92%)</b></td><td>495.90 (+18.44%)</td><td>266.40 <b>(+34.14%)</b></td><td>122.41 (-2.02%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>487.60 (n/a)</td><td>358.94 (n/a)</td><td>418.70 (n/a)</td><td>198.60 (n/a)</td><td>124.93 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (-10.44%)</td><td>0.02 (-14.97%)</td><td>0.02 <b>(-32.63%)</b></td><td>0.01 <b>(-25.35%)</b></td><td>0.01 (-10.26%)</td><td>834.30 <b>(+33.96%)</b></td><td>481.88 (+18.60%)</td><td>419.50 <b>(+48.44%)</b></td><td>264.60 (+11.65%)</td><td>235.30 <b>(+22.09%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.80 (n/a)</td><td>406.30 (n/a)</td><td>282.60 (n/a)</td><td>237.00 (n/a)</td><td>192.73 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (+1.78%)</td><td>0.03 (+7.54%)</td><td>0.02 (-13.07%)</td><td>0.02 (-2.21%)</td><td>0.01 (+13.84%)</td><td>544.60 (+2.25%)</td><td>409.92 (-3.79%)</td><td>493.50 (+15.03%)</td><td>223.20 (-1.76%)</td><td>147.21 (+19.94%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.60 (n/a)</td><td>426.08 (n/a)</td><td>429.00 (n/a)</td><td>227.20 (n/a)</td><td>122.73 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (-2.68%)</td><td>0.02 (+2.86%)</td><td>0.02 (+5.75%)</td><td>0.01 <b>(+26.45%)</b></td><td>0.01 (-11.81%)</td><td>556.20 <b>(-20.92%)</b></td><td>442.00 (-5.85%)</td><td>471.80 (-5.45%)</td><td>273.70 (+2.74%)</td><td>122.30 <b>(-25.07%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>703.30 (n/a)</td><td>469.48 (n/a)</td><td>499.00 (n/a)</td><td>266.40 (n/a)</td><td>163.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.04 <b>(+60.08%)</b></td><td>0.03 <b>(+30.38%)</b></td><td>0.02 (-0.93%)</td><td>0.01 <b>(-23.09%)</b></td><td>0.01 <b>(+110.30%)</b></td><td>1367.90 <b>(+30.03%)</b></td><td>578.54 (-3.24%)</td><td>484.80 (+0.94%)</td><td>235.50 <b>(-37.53%)</b></td><td>455.96 <b>(+70.16%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1052.00 (n/a)</td><td>597.94 (n/a)</td><td>480.30 (n/a)</td><td>377.00 (n/a)</td><td>267.97 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 <b>(+29.61%)</b></td><td>0.02 (-11.48%)</td><td>0.01 (-17.07%)</td><td>0.01 <b>(-52.33%)</b></td><td>0.01 <b>(+190.26%)</b></td><td>1117.50 <b>(+109.78%)</b></td><td>625.30 <b>(+37.44%)</b></td><td>557.50 <b>(+20.59%)</b></td><td>270.80 <b>(-22.85%)</b></td><td>317.69 <b>(+379.25%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>532.70 (n/a)</td><td>454.96 (n/a)</td><td>462.30 (n/a)</td><td>351.00 (n/a)</td><td>66.29 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 <b>(-59.83%)</b></td><td>0.02 <b>(-31.67%)</b></td><td>0.02 (-11.60%)</td><td>0.01 (+4.70%)</td><td>0.00 <b>(-79.25%)</b></td><td>642.20 (-4.49%)</td><td>528.16 (+12.59%)</td><td>529.30 (+13.12%)</td><td>361.00 <b>(+148.97%)</b></td><td>104.80 <b>(-48.91%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>672.40 (n/a)</td><td>469.08 (n/a)</td><td>467.90 (n/a)</td><td>145.00 (n/a)</td><td>205.12 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (-1.90%)</td><td>0.02 (+15.57%)</td><td>0.02 (-13.89%)</td><td>0.01 <b>(+223.32%)</b></td><td>0.01 (-18.45%)</td><td>585.70 <b>(-69.07%)</b></td><td>435.28 <b>(-38.06%)</b></td><td>516.30 (+16.13%)</td><td>268.10 (+1.94%)</td><td>146.16 <b>(-78.26%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1893.60 (n/a)</td><td>702.70 (n/a)</td><td>444.60 (n/a)</td><td>263.00 (n/a)</td><td>672.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 (+12.06%)</td><td>0.02 (-2.05%)</td><td>0.02 (-9.09%)</td><td>0.01 (-11.15%)</td><td>0.01 <b>(+39.44%)</b></td><td>684.30 (+12.55%)</td><td>466.16 (+5.68%)</td><td>470.30 (+9.99%)</td><td>287.50 (-10.77%)</td><td>143.17 <b>(+36.08%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>608.00 (n/a)</td><td>441.10 (n/a)</td><td>427.60 (n/a)</td><td>322.20 (n/a)</td><td>105.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.03 <b>(+31.40%)</b></td><td>0.02 <b>(+26.22%)</b></td><td>0.02 (-8.69%)</td><td>0.02 <b>(+259.95%)</b></td><td>0.01 (-7.42%)</td><td>526.90 <b>(-72.22%)</b></td><td>417.98 <b>(-42.36%)</b></td><td>495.40 (+9.50%)</td><td>244.10 <b>(-23.89%)</b></td><td>131.41 <b>(-80.26%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1896.70 (n/a)</td><td>725.16 (n/a)</td><td>452.40 (n/a)</td><td>320.70 (n/a)</td><td>665.86 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (-18.05%)</td><td>0.04 (-17.52%)</td><td>0.03 <b>(-39.07%)</b></td><td>0.03 (-3.40%)</td><td>0.01 (-15.86%)</td><td>524.10 (+3.52%)</td><td>421.90 <b>(+20.42%)</b></td><td>501.00 <b>(+64.15%)</b></td><td>262.30 <b>(+22.06%)</b></td><td>126.68 (+6.98%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>506.30 (n/a)</td><td>350.36 (n/a)</td><td>305.20 (n/a)</td><td>214.90 (n/a)</td><td>118.41 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (-5.75%)</td><td>0.08 <b>(+77.44%)</b></td><td>0.09 <b>(+121.47%)</b></td><td>0.04 <b>(+324.43%)</b></td><td>0.02 <b>(-43.50%)</b></td><td>589.60 <b>(-76.44%)</b></td><td>343.28 <b>(-69.93%)</b></td><td>285.70 <b>(-54.84%)</b></td><td>268.60 (+6.12%)</td><td>137.94 <b>(-86.31%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2502.50 (n/a)</td><td>1141.50 (n/a)</td><td>632.70 (n/a)</td><td>253.10 (n/a)</td><td>1007.73 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (-17.33%)</td><td>0.04 (-9.00%)</td><td>0.04 (+13.37%)</td><td>0.03 (+2.08%)</td><td>0.01 <b>(-54.51%)</b></td><td>524.60 (-2.04%)</td><td>437.42 (+2.35%)</td><td>459.50 (-11.79%)</td><td>335.00 <b>(+20.98%)</b></td><td>72.40 <b>(-46.46%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>535.50 (n/a)</td><td>427.38 (n/a)</td><td>520.90 (n/a)</td><td>276.90 (n/a)</td><td>135.22 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (+8.36%)</td><td>0.04 (-18.19%)</td><td>0.04 <b>(-31.15%)</b></td><td>0.03 <b>(-26.19%)</b></td><td>0.02 <b>(+99.68%)</b></td><td>594.60 <b>(+35.48%)</b></td><td>505.46 <b>(+30.32%)</b></td><td>563.00 <b>(+45.25%)</b></td><td>278.80 (-7.71%)</td><td>130.66 <b>(+146.82%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>438.90 (n/a)</td><td>387.86 (n/a)</td><td>387.60 (n/a)</td><td>302.10 (n/a)</td><td>52.94 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (+3.47%)</td><td>0.04 <b>(+20.85%)</b></td><td>0.04 <b>(+27.19%)</b></td><td>0.03 (+7.62%)</td><td>0.01 (+5.19%)</td><td>519.80 (-7.08%)</td><td>396.92 (-17.13%)</td><td>401.60 <b>(-21.38%)</b></td><td>273.20 (-3.33%)</td><td>110.53 (-2.49%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>559.40 (n/a)</td><td>478.98 (n/a)</td><td>510.80 (n/a)</td><td>282.60 (n/a)</td><td>113.35 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 <b>(-21.80%)</b></td><td>0.05 <b>(+21.67%)</b></td><td>0.05 <b>(+35.14%)</b></td><td>0.05 <b>(+336.72%)</b></td><td>0.01 <b>(-65.89%)</b></td><td>450.50 <b>(-77.10%)</b></td><td>408.04 <b>(-46.94%)</b></td><td>426.40 <b>(-26.01%)</b></td><td>299.70 <b>(+27.86%)</b></td><td>61.68 <b>(-90.99%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1967.40 (n/a)</td><td>769.00 (n/a)</td><td>576.30 (n/a)</td><td>234.40 (n/a)</td><td>684.94 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (-11.21%)</td><td>0.04 (-18.64%)</td><td>0.04 (+5.27%)</td><td>0.03 (+0.67%)</td><td>0.02 <b>(-32.10%)</b></td><td>595.90 (-0.67%)</td><td>464.74 (+14.50%)</td><td>450.20 (-5.00%)</td><td>254.40 (+12.62%)</td><td>140.98 (-16.68%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.90 (n/a)</td><td>405.90 (n/a)</td><td>473.90 (n/a)</td><td>225.90 (n/a)</td><td>169.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 <b>(+59.63%)</b></td><td>0.05 <b>(+27.54%)</b></td><td>0.04 (+0.03%)</td><td>0.03 <b>(+128.73%)</b></td><td>0.03 <b>(+62.82%)</b></td><td>592.10 <b>(-56.28%)</b></td><td>461.32 <b>(-27.05%)</b></td><td>488.50 (-0.04%)</td><td>201.10 <b>(-37.35%)</b></td><td>155.98 <b>(-62.08%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1354.30 (n/a)</td><td>632.36 (n/a)</td><td>488.70 (n/a)</td><td>321.00 (n/a)</td><td>411.30 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (+9.17%)</td><td>0.05 <b>(-20.61%)</b></td><td>0.03 <b>(-45.27%)</b></td><td>0.03 <b>(-22.29%)</b></td><td>0.03 <b>(+52.95%)</b></td><td>636.00 <b>(+28.67%)</b></td><td>427.02 <b>(+41.52%)</b></td><td>502.50 <b>(+82.73%)</b></td><td>187.00 (-8.42%)</td><td>184.75 <b>(+65.58%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>494.30 (n/a)</td><td>301.74 (n/a)</td><td>275.00 (n/a)</td><td>204.20 (n/a)</td><td>111.57 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 <b>(+23.82%)</b></td><td>0.05 (+8.77%)</td><td>0.04 (+3.86%)</td><td>0.04 <b>(+22.43%)</b></td><td>0.02 <b>(+33.41%)</b></td><td>466.30 (-18.32%)</td><td>389.30 (-6.44%)</td><td>447.20 (-3.72%)</td><td>195.70 (-19.27%)</td><td>115.03 (-10.98%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>570.90 (n/a)</td><td>416.08 (n/a)</td><td>464.50 (n/a)</td><td>242.40 (n/a)</td><td>129.23 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.05 (+6.43%)</td><td>0.04 (+12.19%)</td><td>0.05 <b>(+24.69%)</b></td><td>0.03 (-3.19%)</td><td>0.01 (+16.14%)</td><td>654.50 (+3.30%)</td><td>409.48 (-9.19%)</td><td>338.20 (-19.80%)</td><td>314.80 (-6.03%)</td><td>144.05 (+14.61%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>633.60 (n/a)</td><td>450.94 (n/a)</td><td>421.70 (n/a)</td><td>335.00 (n/a)</td><td>125.69 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 (-16.52%)</td><td>0.09 (-7.56%)</td><td>0.08 (+3.17%)</td><td>0.05 <b>(-30.38%)</b></td><td>0.03 (+2.22%)</td><td>676.80 <b>(+43.63%)</b></td><td>414.32 (+13.02%)</td><td>388.50 (-3.07%)</td><td>279.20 (+19.78%)</td><td>162.14 <b>(+74.95%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>471.20 (n/a)</td><td>366.60 (n/a)</td><td>400.80 (n/a)</td><td>233.10 (n/a)</td><td>92.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (-1.46%)</td><td>0.09 (-3.57%)</td><td>0.08 (-8.97%)</td><td>0.06 (-3.35%)</td><td>0.03 (+2.86%)</td><td>560.30 (+3.47%)</td><td>400.24 (+4.66%)</td><td>434.50 (+9.86%)</td><td>241.70 (+1.51%)</td><td>130.76 (+7.51%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>541.50 (n/a)</td><td>382.42 (n/a)</td><td>395.50 (n/a)</td><td>238.10 (n/a)</td><td>121.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 <b>(-51.94%)</b></td><td>0.08 <b>(-28.89%)</b></td><td>0.08 (-13.43%)</td><td>0.06 (+2.36%)</td><td>0.02 <b>(-69.81%)</b></td><td>656.80 (-2.31%)</td><td>521.00 (+18.08%)</td><td>521.20 (+15.49%)</td><td>337.90 <b>(+108.07%)</b></td><td>124.11 <b>(-32.49%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>672.30 (n/a)</td><td>441.22 (n/a)</td><td>451.30 (n/a)</td><td>162.40 (n/a)</td><td>183.85 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (+19.80%)</td><td>0.09 (+12.89%)</td><td>0.08 <b>(+24.07%)</b></td><td>0.06 <b>(+24.27%)</b></td><td>0.03 (+10.90%)</td><td>522.30 (-19.52%)</td><td>397.14 (-11.93%)</td><td>386.10 (-19.41%)</td><td>259.70 (-16.55%)</td><td>118.37 (-16.94%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>649.00 (n/a)</td><td>450.96 (n/a)</td><td>479.10 (n/a)</td><td>311.20 (n/a)</td><td>142.51 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 <b>(+25.94%)</b></td><td>0.09 (+16.25%)</td><td>0.09 (+3.47%)</td><td>0.08 <b>(+100.93%)</b></td><td>0.02 (-12.84%)</td><td>534.30 <b>(-50.23%)</b></td><td>457.82 <b>(-21.72%)</b></td><td>463.60 (-3.36%)</td><td>304.50 <b>(-20.60%)</b></td><td>92.85 <b>(-67.24%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>1073.60 (n/a)</td><td>584.88 (n/a)</td><td>479.70 (n/a)</td><td>383.50 (n/a)</td><td>283.42 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (-9.34%)</td><td>0.09 (-2.58%)</td><td>0.09 <b>(+27.21%)</b></td><td>0.05 <b>(-22.50%)</b></td><td>0.04 (-13.02%)</td><td>701.20 <b>(+29.04%)</b></td><td>406.10 (+3.01%)</td><td>372.30 <b>(-21.39%)</b></td><td>247.00 (+10.27%)</td><td>185.46 <b>(+23.26%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>543.40 (n/a)</td><td>394.22 (n/a)</td><td>473.60 (n/a)</td><td>224.00 (n/a)</td><td>150.46 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (+2.99%)</td><td>0.09 (+0.14%)</td><td>0.07 (-15.79%)</td><td>0.06 <b>(+71.99%)</b></td><td>0.04 (-2.28%)</td><td>635.60 <b>(-41.86%)</b></td><td>496.10 (-9.13%)</td><td>556.80 (+18.75%)</td><td>227.40 (-2.90%)</td><td>166.26 <b>(-48.44%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1093.20 (n/a)</td><td>545.94 (n/a)</td><td>468.90 (n/a)</td><td>234.20 (n/a)</td><td>322.46 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 <b>(-36.50%)</b></td><td>0.06 <b>(-32.21%)</b></td><td>0.06 <b>(-45.02%)</b></td><td>0.05 (-5.00%)</td><td>0.02 <b>(-55.70%)</b></td><td>630.10 (+5.26%)</td><td>535.40 <b>(+32.83%)</b></td><td>577.80 <b>(+81.93%)</b></td><td>346.20 <b>(+57.51%)</b></td><td>114.99 <b>(-34.28%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>598.60 (n/a)</td><td>403.06 (n/a)</td><td>317.60 (n/a)</td><td>219.80 (n/a)</td><td>174.96 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (+2.01%)</td><td>0.10 (-7.86%)</td><td>0.08 (-15.25%)</td><td>0.05 <b>(-28.73%)</b></td><td>0.04 <b>(+20.58%)</b></td><td>694.10 <b>(+40.34%)</b></td><td>439.12 (+15.80%)</td><td>459.20 (+17.99%)</td><td>231.40 (-1.95%)</td><td>181.74 <b>(+56.64%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>494.60 (n/a)</td><td>379.20 (n/a)</td><td>389.20 (n/a)</td><td>236.00 (n/a)</td><td>116.02 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (-19.57%)</td><td>0.06 (-14.53%)</td><td>0.06 (+1.47%)</td><td>0.02 <b>(-69.60%)</b></td><td>0.03 <b>(+20.25%)</b></td><td>1973.90 <b>(+228.98%)</b></td><td>798.48 <b>(+53.87%)</b></td><td>546.50 (-1.46%)</td><td>382.40 <b>(+24.32%)</b></td><td>665.17 <b>(+451.23%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>600.00 (n/a)</td><td>518.92 (n/a)</td><td>554.60 (n/a)</td><td>307.60 (n/a)</td><td>120.67 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 <b>(+33.63%)</b></td><td>0.07 <b>(+28.35%)</b></td><td>0.07 <b>(+40.37%)</b></td><td>0.04 <b>(+113.31%)</b></td><td>0.03 (+14.05%)</td><td>511.20 <b>(-53.12%)</b></td><td>347.58 <b>(-30.94%)</b></td><td>312.40 <b>(-28.77%)</b></td><td>188.20 <b>(-25.17%)</b></td><td>149.46 <b>(-56.50%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1090.50 (n/a)</td><td>503.30 (n/a)</td><td>438.60 (n/a)</td><td>251.50 (n/a)</td><td>343.57 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 <b>(+22.00%)</b></td><td>0.06 (-14.95%)</td><td>0.06 <b>(-29.09%)</b></td><td>0.04 (+17.70%)</td><td>0.02 <b>(+21.11%)</b></td><td>494.30 (-15.04%)</td><td>376.28 (+16.97%)</td><td>358.40 <b>(+40.99%)</b></td><td>199.30 (-18.02%)</td><td>118.10 (-19.18%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>581.80 (n/a)</td><td>321.70 (n/a)</td><td>254.20 (n/a)</td><td>243.10 (n/a)</td><td>146.14 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (-1.57%)</td><td>0.06 <b>(+27.18%)</b></td><td>0.07 <b>(+47.21%)</b></td><td>0.01 (-0.58%)</td><td>0.03 (+9.86%)</td><td>1984.40 (+0.58%)</td><td>614.34 (-11.23%)</td><td>296.60 <b>(-32.08%)</b></td><td>228.50 (+1.56%)</td><td>767.12 (+6.08%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1973.00 (n/a)</td><td>692.02 (n/a)</td><td>436.70 (n/a)</td><td>225.00 (n/a)</td><td>723.18 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (+0.63%)</td><td>0.07 (+10.92%)</td><td>0.08 <b>(+21.02%)</b></td><td>0.05 (+4.26%)</td><td>0.02 (+11.82%)</td><td>435.90 (-4.09%)</td><td>300.96 (-9.19%)</td><td>267.00 (-17.36%)</td><td>242.60 (-0.61%)</td><td>80.70 (+4.38%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>454.50 (n/a)</td><td>331.40 (n/a)</td><td>323.10 (n/a)</td><td>244.10 (n/a)</td><td>77.31 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (-15.17%)</td><td>0.06 (+4.11%)</td><td>0.04 (-2.69%)</td><td>0.04 (+2.19%)</td><td>0.02 (-14.82%)</td><td>550.80 (-2.15%)</td><td>408.52 (-5.14%)</td><td>455.90 (+2.77%)</td><td>251.60 (+17.85%)</td><td>136.98 (+2.16%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>562.90 (n/a)</td><td>430.66 (n/a)</td><td>443.60 (n/a)</td><td>213.50 (n/a)</td><td>134.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (+1.36%)</td><td>0.07 (+10.92%)</td><td>0.07 <b>(+45.43%)</b></td><td>0.04 (+12.16%)</td><td>0.02 (-17.43%)</td><td>540.60 (-10.84%)</td><td>342.56 (-14.09%)</td><td>296.00 <b>(-31.24%)</b></td><td>229.90 (-1.33%)</td><td>126.88 <b>(-21.11%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>606.30 (n/a)</td><td>398.74 (n/a)</td><td>430.50 (n/a)</td><td>233.00 (n/a)</td><td>160.84 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (-18.70%)</td><td>0.06 <b>(-22.69%)</b></td><td>0.06 <b>(-25.39%)</b></td><td>0.03 <b>(-20.79%)</b></td><td>0.02 (-14.06%)</td><td>780.80 <b>(+26.26%)</b></td><td>440.62 <b>(+30.30%)</b></td><td>385.80 <b>(+34.05%)</b></td><td>288.10 <b>(+23.01%)</b></td><td>200.63 <b>(+26.41%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>618.40 (n/a)</td><td>338.16 (n/a)</td><td>287.80 (n/a)</td><td>234.20 (n/a)</td><td>158.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (-0.41%)</td><td>0.07 (-17.00%)</td><td>0.06 <b>(-33.31%)</b></td><td>0.05 (-14.31%)</td><td>0.02 <b>(+36.60%)</b></td><td>530.60 (+16.69%)</td><td>401.74 <b>(+25.07%)</b></td><td>445.70 <b>(+49.97%)</b></td><td>261.60 (+0.42%)</td><td>115.25 <b>(+50.17%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>454.70 (n/a)</td><td>321.22 (n/a)</td><td>297.20 (n/a)</td><td>260.50 (n/a)</td><td>76.74 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (+3.11%)</td><td>0.08 (+18.20%)</td><td>0.08 (+12.10%)</td><td>0.05 <b>(+24.38%)</b></td><td>0.02 (-19.52%)</td><td>481.10 (-19.60%)</td><td>316.10 (-19.57%)</td><td>296.80 (-10.79%)</td><td>235.70 (-3.00%)</td><td>95.88 <b>(-35.39%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>598.40 (n/a)</td><td>393.00 (n/a)</td><td>332.70 (n/a)</td><td>243.00 (n/a)</td><td>148.39 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.09 (-7.73%)</td><td>0.06 (+1.63%)</td><td>0.06 <b>(+27.13%)</b></td><td>0.04 <b>(+21.65%)</b></td><td>0.02 <b>(-32.13%)</b></td><td>561.20 (-17.80%)</td><td>416.06 (-10.56%)</td><td>422.10 <b>(-21.34%)</b></td><td>273.80 (+8.39%)</td><td>128.21 <b>(-35.30%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>682.70 (n/a)</td><td>465.18 (n/a)</td><td>536.60 (n/a)</td><td>252.60 (n/a)</td><td>198.18 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 (+0.71%)</td><td>0.07 (+5.67%)</td><td>0.09 <b>(+53.38%)</b></td><td>0.04 <b>(-28.77%)</b></td><td>0.03 <b>(+46.94%)</b></td><td>655.10 <b>(+40.40%)</b></td><td>385.50 (+4.51%)</td><td>266.90 <b>(-34.81%)</b></td><td>248.50 (-0.68%)</td><td>182.86 <b>(+98.12%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>466.60 (n/a)</td><td>368.88 (n/a)</td><td>409.40 (n/a)</td><td>250.20 (n/a)</td><td>92.30 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (-12.41%)</td><td>0.06 (-12.72%)</td><td>0.06 (-5.29%)</td><td>0.04 (-13.54%)</td><td>0.02 (-11.36%)</td><td>608.90 (+15.65%)</td><td>458.80 (+14.88%)</td><td>440.10 (+5.59%)</td><td>291.60 (+14.17%)</td><td>119.67 (+18.53%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>526.50 (n/a)</td><td>399.38 (n/a)</td><td>416.80 (n/a)</td><td>255.40 (n/a)</td><td>100.96 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (+11.11%)</td><td>0.06 <b>(+41.53%)</b></td><td>0.06 <b>(+70.23%)</b></td><td>0.03 <b>(+38.91%)</b></td><td>0.02 (+15.24%)</td><td>581.20 <b>(-28.01%)</b></td><td>369.78 <b>(-30.05%)</b></td><td>316.40 <b>(-41.26%)</b></td><td>227.30 (-10.02%)</td><td>157.10 <b>(-23.18%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>807.30 (n/a)</td><td>528.60 (n/a)</td><td>538.60 (n/a)</td><td>252.60 (n/a)</td><td>204.51 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (-0.34%)</td><td>0.06 <b>(+27.72%)</b></td><td>0.07 <b>(+90.12%)</b></td><td>0.04 <b>(+22.10%)</b></td><td>0.02 (-3.46%)</td><td>516.80 (-18.10%)</td><td>360.96 <b>(-23.33%)</b></td><td>283.40 <b>(-47.40%)</b></td><td>246.60 (+0.33%)</td><td>130.82 (-17.38%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>631.00 (n/a)</td><td>470.80 (n/a)</td><td>538.80 (n/a)</td><td>245.80 (n/a)</td><td>158.34 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 (+9.57%)</td><td>0.06 (+15.28%)</td><td>0.07 <b>(+45.37%)</b></td><td>0.03 (+6.16%)</td><td>0.02 (-10.07%)</td><td>575.80 (-5.79%)</td><td>329.08 (-14.97%)</td><td>280.00 <b>(-31.20%)</b></td><td>222.20 (-8.71%)</td><td>140.57 (-8.17%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.20 (n/a)</td><td>387.02 (n/a)</td><td>407.00 (n/a)</td><td>243.40 (n/a)</td><td>153.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (-17.65%)</td><td>0.05 (-4.32%)</td><td>0.06 (+18.70%)</td><td>0.03 <b>(+30.74%)</b></td><td>0.02 (-17.13%)</td><td>621.50 <b>(-23.51%)</b></td><td>412.20 (-1.75%)</td><td>288.90 (-15.77%)</td><td>274.90 <b>(+21.42%)</b></td><td>180.78 <b>(-23.75%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>812.50 (n/a)</td><td>419.54 (n/a)</td><td>343.00 (n/a)</td><td>226.40 (n/a)</td><td>237.10 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.08 <b>(+63.18%)</b></td><td>0.06 <b>(+53.70%)</b></td><td>0.06 <b>(+58.00%)</b></td><td>0.03 (+11.69%)</td><td>0.02 <b>(+140.55%)</b></td><td>587.80 (-10.46%)</td><td>362.96 <b>(-29.36%)</b></td><td>317.90 <b>(-36.70%)</b></td><td>222.80 <b>(-38.72%)</b></td><td>149.12 <b>(+32.15%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>656.50 (n/a)</td><td>513.82 (n/a)</td><td>502.20 (n/a)</td><td>363.60 (n/a)</td><td>112.84 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.07 (-15.23%)</td><td>0.04 <b>(-38.09%)</b></td><td>0.04 <b>(-39.43%)</b></td><td>0.01 <b>(-72.51%)</b></td><td>0.02 <b>(+23.50%)</b></td><td>1727.10 <b>(+263.75%)</b></td><td>698.94 <b>(+120.01%)</b></td><td>446.20 <b>(+65.08%)</b></td><td>268.90 (+17.99%)</td><td>588.00 <b>(+480.63%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>474.80 (n/a)</td><td>317.68 (n/a)</td><td>270.30 (n/a)</td><td>227.90 (n/a)</td><td>101.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.36 (-15.05%)</td><td>0.27 <b>(-23.00%)</b></td><td>0.30 (-10.48%)</td><td>0.16 <b>(-42.78%)</b></td><td>0.10 <b>(+65.35%)</b></td><td>619.60 <b>(+74.78%)</b></td><td>416.90 <b>(+44.34%)</b></td><td>323.10 (+11.68%)</td><td>270.80 (+17.74%)</td><td>172.56 <b>(+249.57%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.06 (n/a)</td><td>354.50 (n/a)</td><td>288.84 (n/a)</td><td>289.30 (n/a)</td><td>230.00 (n/a)</td><td>49.36 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.35 (-6.55%)</td><td>0.27 (-14.35%)</td><td>0.31 (-4.85%)</td><td>0.15 <b>(-31.88%)</b></td><td>0.09 <b>(+62.44%)</b></td><td>635.00 <b>(+46.79%)</b></td><td>402.00 <b>(+26.67%)</b></td><td>312.40 (+5.11%)</td><td>279.00 (+6.98%)</td><td>159.88 <b>(+137.25%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>432.60 (n/a)</td><td>317.36 (n/a)</td><td>297.20 (n/a)</td><td>260.80 (n/a)</td><td>67.39 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.35 (+5.29%)</td><td>0.26 <b>(+26.79%)</b></td><td>0.22 (+4.91%)</td><td>0.18 <b>(+84.08%)</b></td><td>0.08 (-4.39%)</td><td>550.80 <b>(-45.68%)</b></td><td>408.54 <b>(-27.44%)</b></td><td>456.20 (-4.68%)</td><td>279.00 (-5.01%)</td><td>121.60 <b>(-55.38%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>1014.00 (n/a)</td><td>563.00 (n/a)</td><td>478.60 (n/a)</td><td>293.70 (n/a)</td><td>272.52 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.19 <b>(-27.24%)</b></td><td>0.14 <b>(-32.16%)</b></td><td>0.14 <b>(-46.49%)</b></td><td>0.11 (-4.35%)</td><td>0.04 <b>(-47.29%)</b></td><td>685.00 (+4.55%)</td><td>541.96 <b>(+38.29%)</b></td><td>543.50 <b>(+86.90%)</b></td><td>378.30 <b>(+37.46%)</b></td><td>128.13 <b>(-21.47%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>655.20 (n/a)</td><td>391.90 (n/a)</td><td>290.80 (n/a)</td><td>275.20 (n/a)</td><td>163.16 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.28 (-6.98%)</td><td>0.17 <b>(-31.84%)</b></td><td>0.16 <b>(-40.04%)</b></td><td>0.12 (-14.82%)</td><td>0.07 (-1.38%)</td><td>609.40 (+17.40%)</td><td>467.40 <b>(+48.64%)</b></td><td>460.30 <b>(+66.78%)</b></td><td>260.60 (+7.51%)</td><td>141.00 <b>(+21.14%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>519.10 (n/a)</td><td>314.46 (n/a)</td><td>276.00 (n/a)</td><td>242.40 (n/a)</td><td>116.39 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.17 (-2.12%)</td><td>0.16 (-1.63%)</td><td>0.16 (+3.83%)</td><td>0.13 (-13.46%)</td><td>0.02 <b>(+47.21%)</b></td><td>576.80 (+15.54%)</td><td>480.34 (+2.30%)</td><td>462.40 (-3.71%)</td><td>425.90 (+2.16%)</td><td>57.27 <b>(+80.12%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>499.20 (n/a)</td><td>469.56 (n/a)</td><td>480.20 (n/a)</td><td>416.90 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (-15.66%)</td><td>0.11 (-15.29%)</td><td>0.11 (-10.93%)</td><td>0.05 <b>(-28.31%)</b></td><td>0.04 (+4.07%)</td><td>680.60 <b>(+39.50%)</b></td><td>390.04 <b>(+26.10%)</b></td><td>330.30 (+12.27%)</td><td>224.20 (+18.56%)</td><td>185.36 <b>(+68.33%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>487.90 (n/a)</td><td>309.30 (n/a)</td><td>294.20 (n/a)</td><td>189.10 (n/a)</td><td>110.12 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 <b>(-33.11%)</b></td><td>0.09 <b>(-23.40%)</b></td><td>0.07 <b>(-53.87%)</b></td><td>0.06 <b>(+222.22%)</b></td><td>0.04 <b>(-48.13%)</b></td><td>627.70 <b>(-68.97%)</b></td><td>456.00 <b>(-28.48%)</b></td><td>547.60 <b>(+116.70%)</b></td><td>258.80 <b>(+49.51%)</b></td><td>168.53 <b>(-78.50%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.08 (n/a)</td><td>2022.60 (n/a)</td><td>637.56 (n/a)</td><td>252.70 (n/a)</td><td>173.10 (n/a)</td><td>783.76 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.15 (+6.12%)</td><td>0.11 (+13.61%)</td><td>0.11 <b>(+20.31%)</b></td><td>0.07 (+17.90%)</td><td>0.04 (+6.56%)</td><td>516.00 (-15.17%)</td><td>362.00 (-12.74%)</td><td>341.50 (-16.89%)</td><td>243.90 (-5.79%)</td><td>121.75 (-15.48%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>608.30 (n/a)</td><td>414.86 (n/a)</td><td>410.90 (n/a)</td><td>258.90 (n/a)</td><td>144.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.17 (+19.48%)</td><td>0.10 (-9.80%)</td><td>0.08 <b>(-32.11%)</b></td><td>0.05 <b>(-22.23%)</b></td><td>0.05 <b>(+67.79%)</b></td><td>673.00 <b>(+28.58%)</b></td><td>453.02 <b>(+26.15%)</b></td><td>460.60 <b>(+47.30%)</b></td><td>217.80 (-16.33%)</td><td>206.34 <b>(+86.18%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>523.40 (n/a)</td><td>359.10 (n/a)</td><td>312.70 (n/a)</td><td>260.30 (n/a)</td><td>110.83 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.15 (-2.96%)</td><td>0.11 (-1.99%)</td><td>0.11 (-5.78%)</td><td>0.06 (+8.01%)</td><td>0.03 (-14.12%)</td><td>610.80 (-7.41%)</td><td>364.82 (-1.39%)</td><td>337.10 (+6.14%)</td><td>248.30 (+3.03%)</td><td>144.34 (-15.71%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>659.70 (n/a)</td><td>369.96 (n/a)</td><td>317.60 (n/a)</td><td>241.00 (n/a)</td><td>171.25 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 <b>(+28.34%)</b></td><td>0.10 <b>(+33.86%)</b></td><td>0.08 (+11.98%)</td><td>0.05 <b>(+30.17%)</b></td><td>0.05 <b>(+38.02%)</b></td><td>813.30 <b>(-23.18%)</b></td><td>447.78 <b>(-24.03%)</b></td><td>442.40 (-10.68%)</td><td>233.20 <b>(-22.08%)</b></td><td>228.72 <b>(-21.10%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1058.70 (n/a)</td><td>589.44 (n/a)</td><td>495.30 (n/a)</td><td>299.30 (n/a)</td><td>289.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.16 (+5.97%)</td><td>0.12 (+4.13%)</td><td>0.13 (+0.78%)</td><td>0.08 (-6.96%)</td><td>0.03 (+11.36%)</td><td>515.60 (+7.48%)</td><td>350.48 (-2.88%)</td><td>309.80 (-0.77%)</td><td>263.00 (-5.63%)</td><td>102.68 (+13.00%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>479.70 (n/a)</td><td>360.88 (n/a)</td><td>312.20 (n/a)</td><td>278.70 (n/a)</td><td>90.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (-17.55%)</td><td>0.09 <b>(-22.09%)</b></td><td>0.09 <b>(-39.49%)</b></td><td>0.06 <b>(+198.55%)</b></td><td>0.03 <b>(-52.47%)</b></td><td>646.70 <b>(-66.51%)</b></td><td>481.24 <b>(-22.88%)</b></td><td>472.50 <b>(+65.27%)</b></td><td>316.50 <b>(+21.31%)</b></td><td>136.64 <b>(-81.34%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1930.90 (n/a)</td><td>623.98 (n/a)</td><td>285.90 (n/a)</td><td>260.90 (n/a)</td><td>732.16 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.19 (-6.31%)</td><td>0.10 (-11.83%)</td><td>0.07 <b>(-21.15%)</b></td><td>0.02 <b>(-72.11%)</b></td><td>0.07 <b>(+37.36%)</b></td><td>1867.40 <b>(+258.56%)</b></td><td>704.66 <b>(+77.51%)</b></td><td>576.90 <b>(+26.82%)</b></td><td>217.40 (+6.73%)</td><td>677.09 <b>(+367.75%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>520.80 (n/a)</td><td>396.96 (n/a)</td><td>454.90 (n/a)</td><td>203.70 (n/a)</td><td>144.75 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.15 (-1.39%)</td><td>0.09 <b>(-27.21%)</b></td><td>0.08 <b>(-49.79%)</b></td><td>0.04 <b>(-51.36%)</b></td><td>0.04 (+12.69%)</td><td>1096.90 <b>(+105.60%)</b></td><td>569.06 <b>(+56.21%)</b></td><td>542.00 <b>(+99.12%)</b></td><td>269.70 (+1.39%)</td><td>322.08 <b>(+143.99%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>533.50 (n/a)</td><td>364.28 (n/a)</td><td>272.20 (n/a)</td><td>266.00 (n/a)</td><td>132.01 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.22 <b>(+130.34%)</b></td><td>0.12 <b>(+47.71%)</b></td><td>0.10 (+17.88%)</td><td>0.07 (-8.90%)</td><td>0.06 <b>(+598.92%)</b></td><td>603.00 (+9.78%)</td><td>396.10 <b>(-20.31%)</b></td><td>423.40 (-15.17%)</td><td>188.50 <b>(-56.58%)</b></td><td>165.53 <b>(+223.20%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>549.30 (n/a)</td><td>497.04 (n/a)</td><td>499.10 (n/a)</td><td>434.10 (n/a)</td><td>51.22 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.21 <b>(+28.17%)</b></td><td>0.11 (-3.51%)</td><td>0.09 (-2.53%)</td><td>0.02 <b>(-80.79%)</b></td><td>0.08 <b>(+109.97%)</b></td><td>2471.30 <b>(+420.38%)</b></td><td>782.92 <b>(+104.67%)</b></td><td>447.40 (+2.59%)</td><td>190.90 <b>(-21.99%)</b></td><td>954.41 <b>(+801.86%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>474.90 (n/a)</td><td>382.52 (n/a)</td><td>436.10 (n/a)</td><td>244.70 (n/a)</td><td>105.83 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.12 <b>(-20.46%)</b></td><td>0.07 (-15.52%)</td><td>0.07 (-10.81%)</td><td>0.06 (+14.29%)</td><td>0.02 <b>(-32.69%)</b></td><td>609.60 (-12.50%)</td><td>508.42 (+11.84%)</td><td>535.10 (+12.11%)</td><td>299.00 <b>(+25.68%)</b></td><td>123.24 <b>(-26.39%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>696.70 (n/a)</td><td>454.58 (n/a)</td><td>477.30 (n/a)</td><td>237.90 (n/a)</td><td>167.43 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (-1.37%)</td><td>0.08 <b>(-23.80%)</b></td><td>0.08 <b>(-36.71%)</b></td><td>0.06 (+2.15%)</td><td>0.03 (-8.83%)</td><td>601.80 (-2.10%)</td><td>445.34 <b>(+28.10%)</b></td><td>447.80 <b>(+58.01%)</b></td><td>259.70 (+1.41%)</td><td>129.20 (-14.81%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>614.70 (n/a)</td><td>347.64 (n/a)</td><td>283.40 (n/a)</td><td>256.10 (n/a)</td><td>151.67 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.15 (+5.89%)</td><td>0.14 <b>(+36.72%)</b></td><td>0.14 <b>(+33.86%)</b></td><td>0.12 <b>(+99.11%)</b></td><td>0.01 <b>(-69.55%)</b></td><td>290.40 <b>(-49.78%)</b></td><td>256.54 <b>(-35.37%)</b></td><td>253.30 <b>(-25.28%)</b></td><td>228.10 (-5.55%)</td><td>22.27 <b>(-86.11%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>578.30 (n/a)</td><td>396.96 (n/a)</td><td>339.00 (n/a)</td><td>241.50 (n/a)</td><td>160.36 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (+1.92%)</td><td>0.11 (-6.44%)</td><td>0.12 (-1.33%)</td><td>0.08 (+1.73%)</td><td>0.03 (+14.30%)</td><td>434.10 (-1.70%)</td><td>337.62 (+8.20%)</td><td>294.20 (+1.34%)</td><td>253.10 (-1.90%)</td><td>87.26 (+14.83%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>441.60 (n/a)</td><td>312.04 (n/a)</td><td>290.30 (n/a)</td><td>258.00 (n/a)</td><td>75.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (+13.11%)</td><td>0.10 (+11.68%)</td><td>0.12 (+11.94%)</td><td>0.06 (+15.73%)</td><td>0.03 (+14.05%)</td><td>572.70 (-13.58%)</td><td>367.22 (-10.54%)</td><td>299.90 (-10.69%)</td><td>252.30 (-11.60%)</td><td>133.23 (-13.64%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>662.70 (n/a)</td><td>410.50 (n/a)</td><td>335.80 (n/a)</td><td>285.40 (n/a)</td><td>154.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.13 (+2.98%)</td><td>0.09 (-2.58%)</td><td>0.08 (+15.12%)</td><td>0.06 (+4.70%)</td><td>0.03 (-19.69%)</td><td>555.40 (-4.50%)</td><td>430.84 (-1.42%)</td><td>428.40 (-13.14%)</td><td>270.10 (-2.91%)</td><td>103.82 <b>(-26.96%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>581.60 (n/a)</td><td>437.04 (n/a)</td><td>493.20 (n/a)</td><td>278.20 (n/a)</td><td>142.14 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.56 <b>(+88.89%)</b></td><td>0.27 (+2.85%)</td><td>0.27 (+2.72%)</td><td>0.07 <b>(-64.77%)</b></td><td>0.19 <b>(+362.32%)</b></td><td>1913.90 <b>(+183.84%)</b></td><td>787.76 <b>(+51.87%)</b></td><td>493.50 (-2.64%)</td><td>233.70 <b>(-47.05%)</b></td><td>662.87 <b>(+616.87%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>674.30 (n/a)</td><td>518.72 (n/a)</td><td>506.90 (n/a)</td><td>441.40 (n/a)</td><td>92.47 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.29 <b>(-41.13%)</b></td><td>0.21 <b>(-49.64%)</b></td><td>0.24 <b>(-44.87%)</b></td><td>0.07 <b>(-79.57%)</b></td><td>0.08 <b>(+27.90%)</b></td><td>1954.40 <b>(+389.46%)</b></td><td>813.12 <b>(+157.40%)</b></td><td>546.80 <b>(+81.42%)</b></td><td>458.90 <b>(+69.84%)</b></td><td>639.41 <b>(+1088.17%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>399.30 (n/a)</td><td>315.90 (n/a)</td><td>301.40 (n/a)</td><td>270.20 (n/a)</td><td>53.82 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.47 (+10.72%)</td><td>0.24 <b>(-23.46%)</b></td><td>0.22 (-13.65%)</td><td>0.07 <b>(-71.26%)</b></td><td>0.14 <b>(+51.63%)</b></td><td>1949.50 <b>(+247.94%)</b></td><td>806.96 <b>(+78.27%)</b></td><td>593.60 (+15.82%)</td><td>281.70 (-9.68%)</td><td>654.03 <b>(+422.13%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.09 (n/a)</td><td>560.30 (n/a)</td><td>452.66 (n/a)</td><td>512.50 (n/a)</td><td>311.90 (n/a)</td><td>125.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.00 (+14.29%)</td><td>0.00 <b>(+33.33%)</b></td><td>0.00 <b>(+133.33%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+11.09%)</td><td>15970.04 (-7.43%)</td><td>9371.51 <b>(-22.73%)</b></td><td>5736.60 <b>(-61.49%)</b></td><td>4919.26 (-16.88%)</td><td>5474.00 (-0.02%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17251.44 (n/a)</td><td>12128.84 (n/a)</td><td>14897.89 (n/a)</td><td>5918.51 (n/a)</td><td>5474.88 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.00 <b>(+200.00%)</b></td><td>0.00 <b>(+87.50%)</b></td><td>0.00 <b>(+40.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+1051.09%)</b></td><td>20255.29 (-6.62%)</td><td>11924.38 <b>(-31.72%)</b></td><td>12049.90 <b>(-26.46%)</b></td><td>5639.32 <b>(-64.09%)</b></td><td>6311.43 <b>(+154.64%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21690.41 (n/a)</td><td>17464.83 (n/a)</td><td>16385.53 (n/a)</td><td>15704.75 (n/a)</td><td>2478.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.10 <b>(-26.09%)</b></td><td>0.09 (-0.49%)</td><td>0.09 (+12.12%)</td><td>0.08 (+7.33%)</td><td>0.01 <b>(-63.50%)</b></td><td>26517.21 (-6.83%)</td><td>23881.28 (-3.96%)</td><td>24644.33 (-10.82%)</td><td>20684.74 <b>(+35.34%)</b></td><td>2588.92 <b>(-52.79%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28460.84 (n/a)</td><td>24865.55 (n/a)</td><td>27635.52 (n/a)</td><td>15283.52 (n/a)</td><td>5484.32 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.23 (+8.16%)</td><td>1.93 (+1.67%)</td><td>2.35 (+1.88%)</td><td>0.32 (+10.13%)</td><td>1.17 (+14.42%)</td><td>3267.40 (-9.20%)</td><td>1069.24 (-3.00%)</td><td>445.90 (-1.85%)</td><td>325.10 (-7.54%)</td><td>1249.71 (-10.73%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>2.98 (n/a)</td><td>1.90 (n/a)</td><td>2.31 (n/a)</td><td>0.29 (n/a)</td><td>1.03 (n/a)</td><td>3598.50 (n/a)</td><td>1102.36 (n/a)</td><td>454.30 (n/a)</td><td>351.60 (n/a)</td><td>1399.86 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>2.89 <b>(+50.53%)</b></td><td>2.08 <b>(+60.23%)</b></td><td>2.53 <b>(+77.53%)</b></td><td>0.80 <b>(+42.62%)</b></td><td>0.94 <b>(+74.77%)</b></td><td>1314.40 <b>(-29.88%)</b></td><td>644.72 <b>(-33.95%)</b></td><td>414.50 <b>(-43.67%)</b></td><td>363.30 <b>(-33.57%)</b></td><td>408.36 <b>(-24.35%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>1.92 (n/a)</td><td>1.30 (n/a)</td><td>1.42 (n/a)</td><td>0.56 (n/a)</td><td>0.54 (n/a)</td><td>1874.60 (n/a)</td><td>976.06 (n/a)</td><td>735.90 (n/a)</td><td>546.90 (n/a)</td><td>539.83 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.78 (+11.01%)</td><td>2.44 (-1.34%)</td><td>2.09 (-13.79%)</td><td>1.17 <b>(-21.31%)</b></td><td>1.21 <b>(+76.46%)</b></td><td>899.60 <b>(+27.06%)</b></td><td>532.50 (+16.70%)</td><td>500.90 (+16.00%)</td><td>277.30 (-9.91%)</td><td>268.27 <b>(+79.08%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.41 (n/a)</td><td>2.47 (n/a)</td><td>2.43 (n/a)</td><td>1.48 (n/a)</td><td>0.69 (n/a)</td><td>708.00 (n/a)</td><td>456.30 (n/a)</td><td>431.80 (n/a)</td><td>307.80 (n/a)</td><td>149.81 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.59 (-7.45%)</td><td>2.42 (+8.71%)</td><td>2.30 <b>(+29.45%)</b></td><td>1.42 <b>(+25.94%)</b></td><td>0.94 (-16.76%)</td><td>736.70 <b>(-20.60%)</b></td><td>490.50 (-14.04%)</td><td>456.10 <b>(-22.75%)</b></td><td>291.70 (+8.04%)</td><td>191.79 <b>(-26.97%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.88 (n/a)</td><td>2.23 (n/a)</td><td>1.78 (n/a)</td><td>1.13 (n/a)</td><td>1.13 (n/a)</td><td>927.80 (n/a)</td><td>570.64 (n/a)</td><td>590.40 (n/a)</td><td>270.00 (n/a)</td><td>262.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>4.70 (+1.16%)</td><td>2.46 (-2.84%)</td><td>2.46 <b>(+24.68%)</b></td><td>0.58 (-1.57%)</td><td>1.72 (+8.56%)</td><td>3622.00 (+1.59%)</td><td>1516.20 (+11.88%)</td><td>851.40 (-19.80%)</td><td>446.40 (-1.15%)</td><td>1340.65 (+5.68%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>4.64 (n/a)</td><td>2.53 (n/a)</td><td>1.98 (n/a)</td><td>0.59 (n/a)</td><td>1.59 (n/a)</td><td>3565.20 (n/a)</td><td>1355.24 (n/a)</td><td>1061.60 (n/a)</td><td>451.60 (n/a)</td><td>1268.60 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>4.99 (-2.95%)</td><td>2.84 (+2.83%)</td><td>2.46 (+3.36%)</td><td>0.56 (-5.74%)</td><td>1.69 <b>(-24.74%)</b></td><td>3746.50 (+6.09%)</td><td>1294.78 <b>(-23.37%)</b></td><td>852.10 (-3.25%)</td><td>420.20 (+3.04%)</td><td>1386.36 (-10.64%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.14 (n/a)</td><td>2.76 (n/a)</td><td>2.38 (n/a)</td><td>0.59 (n/a)</td><td>2.24 (n/a)</td><td>3531.40 (n/a)</td><td>1689.58 (n/a)</td><td>880.70 (n/a)</td><td>407.80 (n/a)</td><td>1551.51 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.88 <b>(-38.42%)</b></td><td>2.36 <b>(-50.61%)</b></td><td>2.47 <b>(-43.78%)</b></td><td>0.59 <b>(-84.45%)</b></td><td>1.25 <b>(+21.76%)</b></td><td>3578.50 <b>(+543.27%)</b></td><td>1363.70 <b>(+199.74%)</b></td><td>847.60 <b>(+77.88%)</b></td><td>540.30 <b>(+62.40%)</b></td><td>1259.16 <b>(+1302.11%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>6.30 (n/a)</td><td>4.77 (n/a)</td><td>4.40 (n/a)</td><td>3.77 (n/a)</td><td>1.02 (n/a)</td><td>556.30 (n/a)</td><td>454.96 (n/a)</td><td>476.50 (n/a)</td><td>332.70 (n/a)</td><td>89.80 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.56 <b>(+25.36%)</b></td><td>2.98 <b>(+56.70%)</b></td><td>3.03 <b>(+246.77%)</b></td><td>0.60 (+1.92%)</td><td>1.86 (+6.53%)</td><td>3513.40 (-1.88%)</td><td>1238.04 <b>(-41.88%)</b></td><td>691.50 <b>(-71.16%)</b></td><td>377.50 <b>(-20.22%)</b></td><td>1294.85 (-13.06%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>4.43 (n/a)</td><td>1.90 (n/a)</td><td>0.87 (n/a)</td><td>0.59 (n/a)</td><td>1.74 (n/a)</td><td>3580.80 (n/a)</td><td>2130.20 (n/a)</td><td>2398.00 (n/a)</td><td>473.20 (n/a)</td><td>1489.35 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.60 <b>(-28.42%)</b></td><td>3.28 (-11.21%)</td><td>3.23 <b>(+21.59%)</b></td><td>0.58 <b>(-71.33%)</b></td><td>1.88 <b>(-20.93%)</b></td><td>3619.50 <b>(+248.83%)</b></td><td>1181.62 <b>(+66.64%)</b></td><td>649.70 (-17.75%)</td><td>374.30 <b>(+39.72%)</b></td><td>1371.50 <b>(+366.96%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>7.83 (n/a)</td><td>3.70 (n/a)</td><td>2.65 (n/a)</td><td>2.02 (n/a)</td><td>2.37 (n/a)</td><td>1037.60 (n/a)</td><td>709.10 (n/a)</td><td>789.90 (n/a)</td><td>267.90 (n/a)</td><td>293.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>6.99 (+12.60%)</td><td>2.66 (-11.52%)</td><td>1.67 <b>(-46.90%)</b></td><td>0.59 (+0.08%)</td><td>2.62 <b>(+24.95%)</b></td><td>3560.60 (-0.08%)</td><td>1646.00 <b>(+29.12%)</b></td><td>1258.50 <b>(+88.34%)</b></td><td>300.10 (-11.21%)</td><td>1347.23 (+2.56%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>6.21 (n/a)</td><td>3.00 (n/a)</td><td>3.14 (n/a)</td><td>0.59 (n/a)</td><td>2.10 (n/a)</td><td>3563.40 (n/a)</td><td>1274.74 (n/a)</td><td>668.20 (n/a)</td><td>338.00 (n/a)</td><td>1313.61 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>5.30 (+2.38%)</td><td>4.41 <b>(+33.76%)</b></td><td>4.61 <b>(+40.32%)</b></td><td>3.33 <b>(+170.66%)</b></td><td>0.84 <b>(-43.32%)</b></td><td>1260.60 <b>(-63.05%)</b></td><td>980.80 <b>(-39.20%)</b></td><td>910.50 <b>(-28.73%)</b></td><td>791.60 (-2.32%)</td><td>198.68 <b>(-80.92%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.18 (n/a)</td><td>3.30 (n/a)</td><td>3.28 (n/a)</td><td>1.23 (n/a)</td><td>1.48 (n/a)</td><td>3412.00 (n/a)</td><td>1613.04 (n/a)</td><td>1277.60 (n/a)</td><td>810.40 (n/a)</td><td>1041.37 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>8.36 <b>(+44.18%)</b></td><td>6.02 <b>(+68.82%)</b></td><td>5.76 <b>(+64.16%)</b></td><td>3.83 <b>(+233.86%)</b></td><td>1.63 <b>(-25.18%)</b></td><td>1095.30 <b>(-70.05%)</b></td><td>742.34 <b>(-57.89%)</b></td><td>728.40 <b>(-39.09%)</b></td><td>501.50 <b>(-30.64%)</b></td><td>218.32 <b>(-82.99%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.80 (n/a)</td><td>3.56 (n/a)</td><td>3.51 (n/a)</td><td>1.15 (n/a)</td><td>2.18 (n/a)</td><td>3656.90 (n/a)</td><td>1762.84 (n/a)</td><td>1195.80 (n/a)</td><td>723.00 (n/a)</td><td>1283.41 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>7.30 (-10.59%)</td><td>4.32 <b>(-32.31%)</b></td><td>3.91 <b>(-37.72%)</b></td><td>1.14 <b>(-76.67%)</b></td><td>2.27 <b>(+90.35%)</b></td><td>3687.70 <b>(+328.70%)</b></td><td>1441.82 <b>(+113.20%)</b></td><td>1073.90 <b>(+60.57%)</b></td><td>574.70 (+11.83%)</td><td>1274.32 <b>(+915.70%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>8.16 (n/a)</td><td>6.38 (n/a)</td><td>6.27 (n/a)</td><td>4.88 (n/a)</td><td>1.19 (n/a)</td><td>860.20 (n/a)</td><td>676.28 (n/a)</td><td>668.80 (n/a)</td><td>513.90 (n/a)</td><td>125.46 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>7.65 (-18.82%)</td><td>5.25 (-1.70%)</td><td>6.54 <b>(+69.21%)</b></td><td>1.09 (-8.45%)</td><td>2.74 <b>(-20.65%)</b></td><td>3845.00 (+9.23%)</td><td>1341.24 (+0.94%)</td><td>641.80 <b>(-40.90%)</b></td><td>548.50 <b>(+23.20%)</b></td><td>1415.92 (+12.06%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>9.42 (n/a)</td><td>5.34 (n/a)</td><td>3.86 (n/a)</td><td>1.19 (n/a)</td><td>3.46 (n/a)</td><td>3520.10 (n/a)</td><td>1328.70 (n/a)</td><td>1086.00 (n/a)</td><td>445.20 (n/a)</td><td>1263.54 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>6.86 <b>(-22.24%)</b></td><td>5.93 (+6.76%)</td><td>6.59 <b>(+42.17%)</b></td><td>4.70 <b>(+22.48%)</b></td><td>1.12 <b>(-45.90%)</b></td><td>892.10 (-18.35%)</td><td>729.72 (-12.17%)</td><td>636.30 <b>(-29.67%)</b></td><td>611.40 <b>(+28.61%)</b></td><td>148.20 <b>(-42.72%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>8.82 (n/a)</td><td>5.55 (n/a)</td><td>4.64 (n/a)</td><td>3.84 (n/a)</td><td>2.08 (n/a)</td><td>1092.60 (n/a)</td><td>830.84 (n/a)</td><td>904.70 (n/a)</td><td>475.40 (n/a)</td><td>258.72 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>8.52 (+3.30%)</td><td>6.39 (-4.28%)</td><td>7.11 (-2.04%)</td><td>1.18 <b>(-75.05%)</b></td><td>3.02 <b>(+76.71%)</b></td><td>3559.80 <b>(+300.83%)</b></td><td>1153.14 <b>(+73.13%)</b></td><td>590.20 (+2.08%)</td><td>492.10 (-3.21%)</td><td>1346.65 <b>(+630.47%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>8.25 (n/a)</td><td>6.67 (n/a)</td><td>7.25 (n/a)</td><td>4.72 (n/a)</td><td>1.71 (n/a)</td><td>888.10 (n/a)</td><td>666.06 (n/a)</td><td>578.20 (n/a)</td><td>508.40 (n/a)</td><td>184.35 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>1.63 (+8.62%)</td><td>1.20 (+15.78%)</td><td>1.33 <b>(+24.84%)</b></td><td>0.70 <b>(+21.33%)</b></td><td>0.38 (+3.62%)</td><td>744.30 (-17.58%)</td><td>479.92 (-15.24%)</td><td>394.70 (-19.91%)</td><td>322.50 (-7.94%)</td><td>175.45 <b>(-21.36%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>1.50 (n/a)</td><td>1.04 (n/a)</td><td>1.06 (n/a)</td><td>0.58 (n/a)</td><td>0.37 (n/a)</td><td>903.10 (n/a)</td><td>566.22 (n/a)</td><td>492.80 (n/a)</td><td>350.30 (n/a)</td><td>223.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.28 (+8.67%)</td><td>1.79 (+2.15%)</td><td>1.45 (+2.46%)</td><td>0.29 <b>(-30.94%)</b></td><td>1.16 (+6.24%)</td><td>3596.40 <b>(+44.81%)</b></td><td>1166.58 <b>(+20.02%)</b></td><td>724.10 (-2.40%)</td><td>320.10 (-7.96%)</td><td>1372.99 <b>(+56.49%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.01 (n/a)</td><td>1.75 (n/a)</td><td>1.41 (n/a)</td><td>0.42 (n/a)</td><td>1.10 (n/a)</td><td>2483.50 (n/a)</td><td>971.98 (n/a)</td><td>741.90 (n/a)</td><td>347.80 (n/a)</td><td>877.37 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>3.53 (-12.25%)</td><td>1.90 (-18.44%)</td><td>1.03 <b>(-61.32%)</b></td><td>0.60 (+8.69%)</td><td>1.47 (+1.01%)</td><td>3487.80 (-7.99%)</td><td>1834.24 <b>(+20.53%)</b></td><td>2038.30 <b>(+158.50%)</b></td><td>593.50 (+13.96%)</td><td>1245.53 (-9.56%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>4.03 (n/a)</td><td>2.33 (n/a)</td><td>2.66 (n/a)</td><td>0.55 (n/a)</td><td>1.46 (n/a)</td><td>3790.80 (n/a)</td><td>1521.84 (n/a)</td><td>788.50 (n/a)</td><td>520.80 (n/a)</td><td>1377.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>1.85 (-5.70%)</td><td>1.08 (-2.71%)</td><td>0.95 (+0.01%)</td><td>0.74 (-0.37%)</td><td>0.44 (-9.36%)</td><td>707.60 (+0.37%)</td><td>531.96 (+1.55%)</td><td>549.40 (-0.02%)</td><td>283.00 (+6.03%)</td><td>154.11 (-2.90%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>1.96 (n/a)</td><td>1.11 (n/a)</td><td>0.95 (n/a)</td><td>0.74 (n/a)</td><td>0.48 (n/a)</td><td>705.00 (n/a)</td><td>523.82 (n/a)</td><td>549.50 (n/a)</td><td>266.90 (n/a)</td><td>158.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.11 (-6.75%)</td><td>0.09 (-5.43%)</td><td>0.11 <b>(+32.64%)</b></td><td>0.05 <b>(-20.17%)</b></td><td>0.03 (+19.21%)</td><td>641.80 <b>(+25.25%)</b></td><td>416.90 (+11.91%)</td><td>302.20 <b>(-24.62%)</b></td><td>287.40 (+7.24%)</td><td>168.17 <b>(+64.62%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>512.40 (n/a)</td><td>372.54 (n/a)</td><td>400.90 (n/a)</td><td>268.00 (n/a)</td><td>102.16 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.14 (-2.17%)</td><td>0.11 <b>(+33.61%)</b></td><td>0.12 <b>(+95.30%)</b></td><td>0.06 (+2.34%)</td><td>0.04 (+5.77%)</td><td>577.50 (-2.28%)</td><td>356.36 <b>(-24.08%)</b></td><td>276.20 <b>(-48.79%)</b></td><td>230.20 (+2.22%)</td><td>157.09 (+5.38%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>591.00 (n/a)</td><td>469.40 (n/a)</td><td>539.40 (n/a)</td><td>225.20 (n/a)</td><td>149.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.28 (+6.25%)</td><td>0.20 (+8.53%)</td><td>0.23 (+7.44%)</td><td>0.12 <b>(+56.99%)</b></td><td>0.07 (-6.54%)</td><td>561.30 <b>(-36.31%)</b></td><td>360.68 (-16.00%)</td><td>286.50 (-6.92%)</td><td>233.90 (-5.91%)</td><td>141.36 <b>(-45.89%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>881.30 (n/a)</td><td>429.40 (n/a)</td><td>307.80 (n/a)</td><td>248.60 (n/a)</td><td>261.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.27 (+5.62%)</td><td>0.19 <b>(+30.59%)</b></td><td>0.17 <b>(+33.66%)</b></td><td>0.13 <b>(+30.29%)</b></td><td>0.06 (+2.89%)</td><td>492.60 <b>(-23.25%)</b></td><td>375.66 <b>(-24.87%)</b></td><td>393.90 <b>(-25.19%)</b></td><td>242.80 (-5.34%)</td><td>119.21 <b>(-21.93%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>641.80 (n/a)</td><td>500.00 (n/a)</td><td>526.50 (n/a)</td><td>256.50 (n/a)</td><td>152.70 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.25 <b>(+29.02%)</b></td><td>0.16 <b>(+21.40%)</b></td><td>0.13 (-0.88%)</td><td>0.10 <b>(+21.03%)</b></td><td>0.07 <b>(+73.41%)</b></td><td>630.80 (-17.37%)</td><td>454.46 (-12.30%)</td><td>501.20 (+0.89%)</td><td>258.30 <b>(-22.48%)</b></td><td>169.89 (+9.27%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>763.40 (n/a)</td><td>518.18 (n/a)</td><td>496.80 (n/a)</td><td>333.20 (n/a)</td><td>155.48 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.45 <b>(+35.15%)</b></td><td>0.27 (+12.79%)</td><td>0.25 (+12.55%)</td><td>0.07 <b>(-46.31%)</b></td><td>0.14 <b>(+65.92%)</b></td><td>1915.80 <b>(+86.25%)</b></td><td>729.64 (+19.22%)</td><td>531.00 (-11.14%)</td><td>291.70 <b>(-26.02%)</b></td><td>671.86 <b>(+161.11%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>1028.60 (n/a)</td><td>612.00 (n/a)</td><td>597.60 (n/a)</td><td>394.30 (n/a)</td><td>257.31 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.63 <b>(+34.12%)</b></td><td>0.36 <b>(+21.19%)</b></td><td>0.35 <b>(+45.21%)</b></td><td>0.07 <b>(-67.94%)</b></td><td>0.21 <b>(+103.58%)</b></td><td>1908.10 <b>(+211.93%)</b></td><td>650.98 <b>(+35.50%)</b></td><td>370.00 <b>(-31.12%)</b></td><td>208.50 <b>(-25.43%)</b></td><td>710.38 <b>(+443.60%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.47 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>611.70 (n/a)</td><td>480.42 (n/a)</td><td>537.20 (n/a)</td><td>279.60 (n/a)</td><td>130.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.55 (-13.82%)</td><td>0.36 (+7.79%)</td><td>0.28 (-0.24%)</td><td>0.20 <b>(+50.20%)</b></td><td>0.15 <b>(-21.91%)</b></td><td>646.40 <b>(-33.42%)</b></td><td>420.36 (-17.09%)</td><td>465.80 (+0.24%)</td><td>237.50 (+16.02%)</td><td>165.26 <b>(-41.79%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.64 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.14 (n/a)</td><td>0.19 (n/a)</td><td>970.90 (n/a)</td><td>507.02 (n/a)</td><td>464.70 (n/a)</td><td>204.70 (n/a)</td><td>283.89 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 23:00:17</td><td>0.06 (-16.12%)</td><td>0.04 (+3.62%)</td><td>0.04 (+17.26%)</td><td>0.03 (-11.99%)</td><td>0.01 <b>(-21.25%)</b></td><td>626.30 (+13.62%)</td><td>412.76 (-5.35%)</td><td>420.90 (-14.73%)</td><td>277.30 (+19.22%)</td><td>139.26 (+3.20%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>551.20 (n/a)</td><td>436.10 (n/a)</td><td>493.60 (n/a)</td><td>232.60 (n/a)</td><td>134.95 (n/a)</td>
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
