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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (+3.40%)</td><td>0.02 (-7.15%)</td><td>0.02 (-10.25%)</td><td>0.01 (-9.90%)</td><td>0.01 <b>(+22.83%)</b></td><td>587.50 (+11.00%)</td><td>355.78 (+13.67%)</td><td>282.40 (+11.44%)</td><td>211.70 (-3.29%)</td><td>163.39 <b>(+28.20%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>529.30 (n/a)</td><td>312.98 (n/a)</td><td>253.40 (n/a)</td><td>218.90 (n/a)</td><td>127.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (+12.10%)</td><td>0.02 (+8.20%)</td><td>0.02 (+13.58%)</td><td>0.01 (-3.81%)</td><td>0.01 (+4.21%)</td><td>581.30 (+3.97%)</td><td>384.56 (-8.03%)</td><td>394.50 (-11.96%)</td><td>226.40 (-10.76%)</td><td>132.97 (-5.37%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.10 (n/a)</td><td>418.14 (n/a)</td><td>448.10 (n/a)</td><td>253.70 (n/a)</td><td>140.52 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 <b>(-21.29%)</b></td><td>0.01 (-12.61%)</td><td>0.01 (-16.57%)</td><td>0.01 <b>(+249.49%)</b></td><td>0.01 <b>(-49.96%)</b></td><td>551.10 <b>(-71.38%)</b></td><td>447.72 <b>(-32.05%)</b></td><td>511.20 (+19.86%)</td><td>257.20 <b>(+27.08%)</b></td><td>120.87 <b>(-83.17%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1925.90 (n/a)</td><td>658.90 (n/a)</td><td>426.50 (n/a)</td><td>202.40 (n/a)</td><td>718.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (-5.97%)</td><td>0.02 (-1.70%)</td><td>0.02 (+9.61%)</td><td>0.01 <b>(-21.96%)</b></td><td>0.01 (-3.18%)</td><td>622.30 <b>(+28.15%)</b></td><td>390.08 (+3.42%)</td><td>390.50 (-8.78%)</td><td>252.20 (+6.37%)</td><td>147.96 <b>(+27.70%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>485.60 (n/a)</td><td>377.18 (n/a)</td><td>428.10 (n/a)</td><td>237.10 (n/a)</td><td>115.86 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (-1.74%)</td><td>0.02 (+13.32%)</td><td>0.01 (+8.56%)</td><td>0.01 (+14.69%)</td><td>0.01 (-13.57%)</td><td>531.30 (-12.80%)</td><td>417.44 (-14.86%)</td><td>471.70 (-7.87%)</td><td>244.40 (+1.75%)</td><td>118.47 <b>(-21.09%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.30 (n/a)</td><td>490.30 (n/a)</td><td>512.00 (n/a)</td><td>240.20 (n/a)</td><td>150.15 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (+12.48%)</td><td>0.02 <b>(+31.11%)</b></td><td>0.02 <b>(+32.06%)</b></td><td>0.01 <b>(+39.46%)</b></td><td>0.00 (+3.44%)</td><td>501.80 <b>(-28.29%)</b></td><td>374.98 <b>(-25.72%)</b></td><td>403.40 <b>(-24.27%)</b></td><td>273.50 (-11.09%)</td><td>97.39 <b>(-36.33%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>699.80 (n/a)</td><td>504.84 (n/a)</td><td>532.70 (n/a)</td><td>307.60 (n/a)</td><td>152.96 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 <b>(+38.69%)</b></td><td>0.05 <b>(+75.58%)</b></td><td>0.05 <b>(+83.82%)</b></td><td>0.04 <b>(+131.62%)</b></td><td>0.00 <b>(-59.82%)</b></td><td>274.60 <b>(-56.82%)</b></td><td>256.86 <b>(-46.74%)</b></td><td>254.90 <b>(-45.60%)</b></td><td>236.20 <b>(-27.90%)</b></td><td>17.42 <b>(-87.61%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>636.00 (n/a)</td><td>482.30 (n/a)</td><td>468.60 (n/a)</td><td>327.60 (n/a)</td><td>140.51 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (-3.38%)</td><td>0.03 (-14.87%)</td><td>0.05 (+14.48%)</td><td>0.01 <b>(-73.29%)</b></td><td>0.02 <b>(+102.21%)</b></td><td>1970.80 <b>(+274.32%)</b></td><td>701.92 <b>(+116.52%)</b></td><td>251.50 (-12.64%)</td><td>235.10 (+3.52%)</td><td>751.81 <b>(+546.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.50 (n/a)</td><td>324.18 (n/a)</td><td>287.90 (n/a)</td><td>227.10 (n/a)</td><td>116.26 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 <b>(+45.72%)</b></td><td>0.03 <b>(+42.93%)</b></td><td>0.03 (+13.98%)</td><td>0.02 <b>(+307.63%)</b></td><td>0.01 (+14.06%)</td><td>599.20 <b>(-75.47%)</b></td><td>434.20 <b>(-50.28%)</b></td><td>452.50 (-12.27%)</td><td>256.20 <b>(-31.37%)</b></td><td>157.49 <b>(-82.16%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2442.50 (n/a)</td><td>873.34 (n/a)</td><td>515.80 (n/a)</td><td>373.30 (n/a)</td><td>882.87 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (+13.59%)</td><td>0.03 (+12.70%)</td><td>0.02 (-5.04%)</td><td>0.02 (+2.91%)</td><td>0.01 <b>(+41.46%)</b></td><td>585.70 (-2.82%)</td><td>444.44 (-5.16%)</td><td>532.90 (+5.32%)</td><td>235.20 (-11.98%)</td><td>171.25 <b>(+29.43%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>602.70 (n/a)</td><td>468.62 (n/a)</td><td>506.00 (n/a)</td><td>267.20 (n/a)</td><td>132.31 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (-17.55%)</td><td>0.03 <b>(-26.16%)</b></td><td>0.02 <b>(-36.44%)</b></td><td>0.02 (-10.38%)</td><td>0.01 <b>(-28.16%)</b></td><td>678.50 (+11.58%)</td><td>526.26 <b>(+30.11%)</b></td><td>556.20 <b>(+57.34%)</b></td><td>297.40 <b>(+21.29%)</b></td><td>151.26 (-6.29%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>608.10 (n/a)</td><td>404.46 (n/a)</td><td>353.50 (n/a)</td><td>245.20 (n/a)</td><td>161.42 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (-9.19%)</td><td>0.03 (-12.04%)</td><td>0.02 <b>(-24.82%)</b></td><td>0.02 <b>(-27.06%)</b></td><td>0.01 (+16.27%)</td><td>686.40 <b>(+37.09%)</b></td><td>477.40 <b>(+20.29%)</b></td><td>546.10 <b>(+33.00%)</b></td><td>279.00 (+10.10%)</td><td>174.17 <b>(+64.66%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.70 (n/a)</td><td>396.86 (n/a)</td><td>410.60 (n/a)</td><td>253.40 (n/a)</td><td>105.77 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (-0.71%)</td><td>0.07 (+7.77%)</td><td>0.07 (+8.74%)</td><td>0.05 (+18.58%)</td><td>0.02 (-18.84%)</td><td>516.00 (-15.67%)</td><td>365.96 (-10.26%)</td><td>358.50 (-8.03%)</td><td>278.30 (+0.69%)</td><td>93.55 <b>(-30.15%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>611.90 (n/a)</td><td>407.82 (n/a)</td><td>389.80 (n/a)</td><td>276.40 (n/a)</td><td>133.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (-6.15%)</td><td>0.06 <b>(-24.68%)</b></td><td>0.05 <b>(-36.50%)</b></td><td>0.04 (-17.36%)</td><td>0.03 (+9.37%)</td><td>624.60 <b>(+21.00%)</b></td><td>447.88 <b>(+37.96%)</b></td><td>471.50 <b>(+57.48%)</b></td><td>244.10 (+6.55%)</td><td>157.42 <b>(+37.90%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>516.20 (n/a)</td><td>324.64 (n/a)</td><td>299.40 (n/a)</td><td>229.10 (n/a)</td><td>114.15 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (+0.17%)</td><td>0.07 (-1.97%)</td><td>0.06 <b>(-20.52%)</b></td><td>0.04 (-12.38%)</td><td>0.03 (+16.96%)</td><td>590.40 (+14.13%)</td><td>392.52 (+6.26%)</td><td>433.00 <b>(+25.84%)</b></td><td>221.20 (-0.18%)</td><td>157.09 <b>(+21.26%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>517.30 (n/a)</td><td>369.38 (n/a)</td><td>344.10 (n/a)</td><td>221.60 (n/a)</td><td>129.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (-7.58%)</td><td>0.07 (+5.41%)</td><td>0.06 (+10.03%)</td><td>0.04 (-12.75%)</td><td>0.03 (+0.10%)</td><td>601.00 (+14.61%)</td><td>409.44 (-2.47%)</td><td>404.20 (-9.13%)</td><td>235.10 (+8.24%)</td><td>157.62 <b>(+29.86%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>524.40 (n/a)</td><td>419.82 (n/a)</td><td>444.80 (n/a)</td><td>217.20 (n/a)</td><td>121.37 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 <b>(+60.98%)</b></td><td>0.08 <b>(+42.03%)</b></td><td>0.07 <b>(+22.84%)</b></td><td>0.05 <b>(+31.15%)</b></td><td>0.03 <b>(+112.30%)</b></td><td>532.60 <b>(-23.76%)</b></td><td>358.54 <b>(-24.30%)</b></td><td>354.80 (-18.61%)</td><td>192.60 <b>(-37.89%)</b></td><td>142.26 (-0.44%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>698.60 (n/a)</td><td>473.66 (n/a)</td><td>435.90 (n/a)</td><td>310.10 (n/a)</td><td>142.89 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 <b>(-25.97%)</b></td><td>0.04 <b>(-27.26%)</b></td><td>0.05 <b>(-23.01%)</b></td><td>0.01 <b>(-21.25%)</b></td><td>0.02 <b>(-26.97%)</b></td><td>2440.20 <b>(+26.99%)</b></td><td>909.68 <b>(+32.32%)</b></td><td>540.50 <b>(+29.90%)</b></td><td>374.50 <b>(+35.05%)</b></td><td>861.43 <b>(+24.33%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1921.60 (n/a)</td><td>687.46 (n/a)</td><td>416.10 (n/a)</td><td>277.30 (n/a)</td><td>692.86 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.24 <b>(+25.44%)</b></td><td>0.18 (+12.98%)</td><td>0.19 (+9.10%)</td><td>0.09 <b>(-22.67%)</b></td><td>0.06 <b>(+83.69%)</b></td><td>533.30 <b>(+29.32%)</b></td><td>300.94 (-4.17%)</td><td>258.70 (-8.36%)</td><td>200.70 <b>(-20.29%)</b></td><td>132.70 <b>(+103.16%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>412.40 (n/a)</td><td>314.04 (n/a)</td><td>282.30 (n/a)</td><td>251.80 (n/a)</td><td>65.32 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.21 (+4.07%)</td><td>0.15 <b>(+34.17%)</b></td><td>0.13 (+11.28%)</td><td>0.11 <b>(+295.63%)</b></td><td>0.05 <b>(-32.19%)</b></td><td>453.20 <b>(-74.73%)</b></td><td>342.18 <b>(-51.10%)</b></td><td>378.20 (-10.14%)</td><td>238.00 (-3.92%)</td><td>98.36 <b>(-84.66%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1793.10 (n/a)</td><td>699.80 (n/a)</td><td>420.90 (n/a)</td><td>247.70 (n/a)</td><td>641.05 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.22 <b>(+85.05%)</b></td><td>0.18 <b>(+112.95%)</b></td><td>0.19 <b>(+105.48%)</b></td><td>0.10 <b>(+423.35%)</b></td><td>0.04 (+11.35%)</td><td>475.70 <b>(-80.89%)</b></td><td>298.52 <b>(-67.18%)</b></td><td>264.90 <b>(-51.33%)</b></td><td>227.70 <b>(-45.97%)</b></td><td>100.94 <b>(-88.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2489.70 (n/a)</td><td>909.70 (n/a)</td><td>544.30 (n/a)</td><td>421.40 (n/a)</td><td>888.17 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.21 (-2.06%)</td><td>0.18 <b>(+20.32%)</b></td><td>0.20 <b>(+61.64%)</b></td><td>0.11 (+1.72%)</td><td>0.04 (-8.15%)</td><td>430.70 (-1.69%)</td><td>293.48 (-17.73%)</td><td>249.60 <b>(-38.14%)</b></td><td>232.00 (+2.11%)</td><td>83.19 (-9.02%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>438.10 (n/a)</td><td>356.72 (n/a)</td><td>403.50 (n/a)</td><td>227.20 (n/a)</td><td>91.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.17 (+0.24%)</td><td>0.10 <b>(-21.96%)</b></td><td>0.11 <b>(-21.12%)</b></td><td>0.04 <b>(-54.53%)</b></td><td>0.05 <b>(+35.36%)</b></td><td>1388.60 <b>(+119.92%)</b></td><td>642.54 <b>(+55.53%)</b></td><td>444.00 <b>(+26.78%)</b></td><td>296.70 (-0.24%)</td><td>435.61 <b>(+216.96%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>631.40 (n/a)</td><td>413.12 (n/a)</td><td>350.20 (n/a)</td><td>297.40 (n/a)</td><td>137.44 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.21 <b>(-38.34%)</b></td><td>0.14 (-19.26%)</td><td>0.13 (+7.42%)</td><td>0.04 <b>(-56.99%)</b></td><td>0.07 <b>(-32.77%)</b></td><td>1094.30 <b>(+132.53%)</b></td><td>478.56 <b>(+37.59%)</b></td><td>366.00 (-6.89%)</td><td>234.50 <b>(+62.17%)</b></td><td>354.92 <b>(+152.99%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.34 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>470.60 (n/a)</td><td>347.82 (n/a)</td><td>393.10 (n/a)</td><td>144.60 (n/a)</td><td>140.29 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (-6.23%)</td><td>0.01 (-4.57%)</td><td>0.01 (-11.24%)</td><td>0.01 (+10.42%)</td><td>0.00 <b>(-26.47%)</b></td><td>496.10 (-9.45%)</td><td>338.26 (-0.08%)</td><td>314.10 (+12.66%)</td><td>249.80 (+6.66%)</td><td>98.60 <b>(-26.45%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>547.90 (n/a)</td><td>338.54 (n/a)</td><td>278.80 (n/a)</td><td>234.20 (n/a)</td><td>134.06 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (-18.07%)</td><td>0.01 <b>(-20.78%)</b></td><td>0.01 <b>(-41.24%)</b></td><td>0.00 <b>(+258.25%)</b></td><td>0.00 <b>(-55.97%)</b></td><td>566.70 <b>(-72.09%)</b></td><td>434.18 <b>(-34.63%)</b></td><td>446.80 <b>(+70.21%)</b></td><td>249.60 <b>(+22.05%)</b></td><td>116.37 <b>(-85.14%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2030.20 (n/a)</td><td>664.16 (n/a)</td><td>262.50 (n/a)</td><td>204.50 (n/a)</td><td>782.92 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (-3.80%)</td><td>0.01 (-17.91%)</td><td>0.01 <b>(-46.21%)</b></td><td>0.00 (+0.13%)</td><td>0.00 (-12.06%)</td><td>536.50 (-0.13%)</td><td>406.14 (+18.77%)</td><td>485.50 <b>(+85.87%)</b></td><td>219.10 (+3.94%)</td><td>150.15 (-5.28%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>537.20 (n/a)</td><td>341.96 (n/a)</td><td>261.20 (n/a)</td><td>210.80 (n/a)</td><td>158.52 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 <b>(-48.94%)</b></td><td>0.01 <b>(-45.17%)</b></td><td>0.01 <b>(-47.32%)</b></td><td>0.01 <b>(-41.67%)</b></td><td>0.00 <b>(-58.62%)</b></td><td>518.80 <b>(+71.45%)</b></td><td>466.82 <b>(+80.34%)</b></td><td>496.40 <b>(+89.83%)</b></td><td>367.70 <b>(+95.90%)</b></td><td>63.26 <b>(+41.96%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>302.60 (n/a)</td><td>258.86 (n/a)</td><td>261.50 (n/a)</td><td>187.70 (n/a)</td><td>44.56 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (-5.98%)</td><td>0.01 <b>(-25.25%)</b></td><td>0.00 <b>(-28.59%)</b></td><td>0.00 (-13.65%)</td><td>0.00 (+3.21%)</td><td>585.70 (+15.82%)</td><td>488.04 <b>(+36.55%)</b></td><td>525.20 <b>(+40.05%)</b></td><td>267.00 (+6.37%)</td><td>130.73 <b>(+27.62%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.70 (n/a)</td><td>357.42 (n/a)</td><td>375.00 (n/a)</td><td>251.00 (n/a)</td><td>102.44 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 <b>(-50.84%)</b></td><td>0.00 <b>(-40.79%)</b></td><td>0.01 <b>(-31.95%)</b></td><td>0.00 <b>(-41.15%)</b></td><td>0.00 <b>(-50.59%)</b></td><td>1058.80 <b>(+69.92%)</b></td><td>648.60 <b>(+66.58%)</b></td><td>524.20 <b>(+46.96%)</b></td><td>486.70 <b>(+103.47%)</b></td><td>241.08 <b>(+66.63%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>623.10 (n/a)</td><td>389.36 (n/a)</td><td>356.70 (n/a)</td><td>239.20 (n/a)</td><td>144.67 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 <b>(-20.99%)</b></td><td>0.01 <b>(-25.51%)</b></td><td>0.01 <b>(-39.05%)</b></td><td>0.01 (-6.48%)</td><td>0.00 <b>(-23.51%)</b></td><td>582.20 (+6.92%)</td><td>428.66 <b>(+31.15%)</b></td><td>460.70 <b>(+64.07%)</b></td><td>260.70 <b>(+26.55%)</b></td><td>136.54 (+1.01%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>544.50 (n/a)</td><td>326.84 (n/a)</td><td>280.80 (n/a)</td><td>206.00 (n/a)</td><td>135.17 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 <b>(-52.44%)</b></td><td>0.01 <b>(-57.79%)</b></td><td>0.01 <b>(-56.13%)</b></td><td>0.00 <b>(-76.60%)</b></td><td>0.00 <b>(-39.34%)</b></td><td>2069.50 <b>(+327.32%)</b></td><td>812.26 <b>(+199.59%)</b></td><td>532.90 <b>(+127.93%)</b></td><td>367.10 <b>(+110.25%)</b></td><td>707.16 <b>(+478.75%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>484.30 (n/a)</td><td>271.12 (n/a)</td><td>233.80 (n/a)</td><td>174.60 (n/a)</td><td>122.19 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (-15.01%)</td><td>0.01 <b>(-30.31%)</b></td><td>0.01 <b>(-49.93%)</b></td><td>0.01 <b>(-29.44%)</b></td><td>0.01 (+5.93%)</td><td>787.40 <b>(+41.75%)</b></td><td>473.94 <b>(+55.32%)</b></td><td>521.00 <b>(+99.69%)</b></td><td>215.30 (+17.65%)</td><td>226.79 <b>(+57.01%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.50 (n/a)</td><td>305.14 (n/a)</td><td>260.90 (n/a)</td><td>183.00 (n/a)</td><td>144.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 <b>(-28.58%)</b></td><td>0.02 (-16.38%)</td><td>0.02 (+2.56%)</td><td>0.01 (-19.60%)</td><td>0.00 (-16.93%)</td><td>518.00 <b>(+24.37%)</b></td><td>376.06 <b>(+21.47%)</b></td><td>297.60 (-2.49%)</td><td>279.10 <b>(+39.97%)</b></td><td>121.13 <b>(+48.33%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>416.50 (n/a)</td><td>309.58 (n/a)</td><td>305.20 (n/a)</td><td>199.40 (n/a)</td><td>81.67 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (-9.84%)</td><td>0.01 (-2.58%)</td><td>0.01 <b>(+28.62%)</b></td><td>0.01 (+19.61%)</td><td>0.00 <b>(-29.92%)</b></td><td>667.10 (-16.39%)</td><td>483.70 (-8.88%)</td><td>429.70 <b>(-22.25%)</b></td><td>265.30 (+10.91%)</td><td>174.06 <b>(-32.85%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>797.90 (n/a)</td><td>530.82 (n/a)</td><td>552.70 (n/a)</td><td>239.20 (n/a)</td><td>259.21 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 <b>(+26.97%)</b></td><td>0.01 (-4.86%)</td><td>0.01 (-19.83%)</td><td>0.01 (-15.87%)</td><td>0.01 <b>(+72.41%)</b></td><td>671.90 (+18.88%)</td><td>500.54 (+13.32%)</td><td>521.90 <b>(+24.74%)</b></td><td>234.70 <b>(-21.24%)</b></td><td>161.28 <b>(+42.16%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.20 (n/a)</td><td>441.70 (n/a)</td><td>418.40 (n/a)</td><td>298.00 (n/a)</td><td>113.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 <b>(-22.65%)</b></td><td>0.03 (-4.09%)</td><td>0.04 <b>(+43.81%)</b></td><td>0.02 (-8.80%)</td><td>0.01 <b>(-23.56%)</b></td><td>532.40 (+9.64%)</td><td>374.98 (+2.70%)</td><td>291.70 <b>(-30.46%)</b></td><td>251.20 <b>(+29.28%)</b></td><td>142.74 (+12.16%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>485.60 (n/a)</td><td>365.12 (n/a)</td><td>419.50 (n/a)</td><td>194.30 (n/a)</td><td>127.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (+19.36%)</td><td>0.03 (+14.21%)</td><td>0.03 (-7.32%)</td><td>0.02 <b>(+279.65%)</b></td><td>0.01 <b>(-23.18%)</b></td><td>524.70 <b>(-73.66%)</b></td><td>367.12 <b>(-44.76%)</b></td><td>310.00 (+7.90%)</td><td>230.00 (-16.24%)</td><td>134.75 <b>(-81.98%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1991.90 (n/a)</td><td>664.60 (n/a)</td><td>287.30 (n/a)</td><td>274.60 (n/a)</td><td>747.63 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (+17.01%)</td><td>0.02 (+6.48%)</td><td>0.02 (+7.79%)</td><td>0.02 (+5.95%)</td><td>0.01 <b>(+28.45%)</b></td><td>610.10 (-5.62%)</td><td>487.32 (-3.03%)</td><td>520.80 (-7.23%)</td><td>223.90 (-14.51%)</td><td>154.37 (+2.82%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>646.40 (n/a)</td><td>502.56 (n/a)</td><td>561.40 (n/a)</td><td>261.90 (n/a)</td><td>150.14 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (+5.10%)</td><td>0.03 (-0.28%)</td><td>0.04 <b>(+20.61%)</b></td><td>0.01 <b>(-69.57%)</b></td><td>0.01 <b>(+60.90%)</b></td><td>1911.50 <b>(+228.66%)</b></td><td>640.38 <b>(+60.19%)</b></td><td>278.00 (-17.06%)</td><td>263.80 (-4.87%)</td><td>716.38 <b>(+404.85%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>581.60 (n/a)</td><td>399.76 (n/a)</td><td>335.20 (n/a)</td><td>277.30 (n/a)</td><td>141.90 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 <b>(-44.90%)</b></td><td>0.02 <b>(-42.31%)</b></td><td>0.02 <b>(-33.11%)</b></td><td>0.00 <b>(-77.12%)</b></td><td>0.01 (-16.49%)</td><td>2102.30 <b>(+336.98%)</b></td><td>832.04 <b>(+125.64%)</b></td><td>531.40 <b>(+49.52%)</b></td><td>440.70 <b>(+81.51%)</b></td><td>712.10 <b>(+611.50%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.10 (n/a)</td><td>368.74 (n/a)</td><td>355.40 (n/a)</td><td>242.80 (n/a)</td><td>100.08 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (-0.30%)</td><td>0.03 (+6.43%)</td><td>0.02 (+1.24%)</td><td>0.02 (+2.43%)</td><td>0.01 (-4.31%)</td><td>567.00 (-2.38%)</td><td>421.76 (-6.67%)</td><td>452.70 (-1.22%)</td><td>257.60 (+0.27%)</td><td>117.64 (-4.24%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>580.80 (n/a)</td><td>451.90 (n/a)</td><td>458.30 (n/a)</td><td>256.90 (n/a)</td><td>122.84 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (+3.62%)</td><td>0.06 (+3.90%)</td><td>0.04 (-7.24%)</td><td>0.04 (+4.60%)</td><td>0.02 (+13.95%)</td><td>540.70 (-4.40%)</td><td>408.82 (-1.98%)</td><td>482.30 (+7.80%)</td><td>244.60 (-3.51%)</td><td>139.27 (+4.86%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>565.60 (n/a)</td><td>417.08 (n/a)</td><td>447.40 (n/a)</td><td>253.50 (n/a)</td><td>132.81 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (-9.61%)</td><td>0.06 (-5.74%)</td><td>0.07 (-9.32%)</td><td>0.03 (-13.04%)</td><td>0.02 (-7.91%)</td><td>631.90 (+15.00%)</td><td>384.18 (+6.68%)</td><td>315.90 (+10.26%)</td><td>274.40 (+10.65%)</td><td>148.69 (+16.54%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>549.50 (n/a)</td><td>360.12 (n/a)</td><td>286.50 (n/a)</td><td>248.00 (n/a)</td><td>127.59 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (-10.44%)</td><td>0.06 (+8.75%)</td><td>0.06 <b>(+27.71%)</b></td><td>0.04 (-2.92%)</td><td>0.02 (-7.07%)</td><td>595.60 (+3.01%)</td><td>405.20 (-8.30%)</td><td>353.00 <b>(-21.68%)</b></td><td>269.10 (+11.66%)</td><td>148.68 (+2.65%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>578.20 (n/a)</td><td>441.88 (n/a)</td><td>450.70 (n/a)</td><td>241.00 (n/a)</td><td>144.84 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (-3.58%)</td><td>0.06 (-6.06%)</td><td>0.08 (+2.34%)</td><td>0.03 (-13.96%)</td><td>0.02 (+5.18%)</td><td>610.20 (+16.23%)</td><td>378.84 (+10.13%)</td><td>272.40 (-2.26%)</td><td>247.80 (+3.73%)</td><td>166.29 <b>(+27.98%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>525.00 (n/a)</td><td>344.00 (n/a)</td><td>278.70 (n/a)</td><td>238.90 (n/a)</td><td>129.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (-16.45%)</td><td>0.05 (-13.53%)</td><td>0.05 (-0.84%)</td><td>0.01 (+1.22%)</td><td>0.02 (-19.28%)</td><td>1881.30 (-1.20%)</td><td>717.10 (+6.04%)</td><td>444.10 (+0.84%)</td><td>287.20 (+19.67%)</td><td>664.38 (-4.54%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1904.20 (n/a)</td><td>676.28 (n/a)</td><td>440.40 (n/a)</td><td>240.00 (n/a)</td><td>695.98 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 <b>(+20.14%)</b></td><td>0.05 (-0.06%)</td><td>0.05 (-0.06%)</td><td>0.02 <b>(-38.36%)</b></td><td>0.02 <b>(+138.43%)</b></td><td>990.90 <b>(+62.26%)</b></td><td>540.44 (+13.70%)</td><td>453.00 (+0.07%)</td><td>324.70 (-16.76%)</td><td>266.21 <b>(+225.13%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>610.70 (n/a)</td><td>475.34 (n/a)</td><td>452.70 (n/a)</td><td>390.10 (n/a)</td><td>81.88 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>478.20 (n/a)</td><td>346.52 (n/a)</td><td>290.00 (n/a)</td><td>263.50 (n/a)</td><td>102.17 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.10 (n/a)</td><td>384.26 (n/a)</td><td>347.80 (n/a)</td><td>250.50 (n/a)</td><td>143.91 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>842.40 (n/a)</td><td>469.56 (n/a)</td><td>457.50 (n/a)</td><td>233.20 (n/a)</td><td>244.98 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>321.30 (n/a)</td><td>259.58 (n/a)</td><td>239.40 (n/a)</td><td>215.30 (n/a)</td><td>42.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1067.90 (n/a)</td><td>472.02 (n/a)</td><td>283.10 (n/a)</td><td>244.30 (n/a)</td><td>350.81 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1342.20 (n/a)</td><td>513.88 (n/a)</td><td>308.90 (n/a)</td><td>210.80 (n/a)</td><td>469.38 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1979.20 (n/a)</td><td>661.42 (n/a)</td><td>317.20 (n/a)</td><td>286.70 (n/a)</td><td>738.71 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>627.80 (n/a)</td><td>444.96 (n/a)</td><td>452.00 (n/a)</td><td>261.30 (n/a)</td><td>130.10 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>518.00 (n/a)</td><td>467.52 (n/a)</td><td>474.20 (n/a)</td><td>403.20 (n/a)</td><td>45.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.20 (-2.03%)</td><td>0.14 (-3.28%)</td><td>0.12 <b>(-25.44%)</b></td><td>0.10 <b>(+282.02%)</b></td><td>0.04 <b>(-40.05%)</b></td><td>502.90 <b>(-73.82%)</b></td><td>383.10 <b>(-38.41%)</b></td><td>405.90 <b>(+34.14%)</b></td><td>247.10 (+2.07%)</td><td>111.99 <b>(-84.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1921.10 (n/a)</td><td>622.00 (n/a)</td><td>302.60 (n/a)</td><td>242.10 (n/a)</td><td>729.12 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2096.80 (n/a)</td><td>758.00 (n/a)</td><td>540.00 (n/a)</td><td>279.60 (n/a)</td><td>761.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>652.10 (n/a)</td><td>435.30 (n/a)</td><td>428.80 (n/a)</td><td>285.90 (n/a)</td><td>145.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>749.80 (n/a)</td><td>396.12 (n/a)</td><td>295.20 (n/a)</td><td>230.70 (n/a)</td><td>211.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>536.60 (n/a)</td><td>413.92 (n/a)</td><td>428.80 (n/a)</td><td>236.50 (n/a)</td><td>125.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>615.40 (n/a)</td><td>448.62 (n/a)</td><td>373.50 (n/a)</td><td>318.40 (n/a)</td><td>142.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>576.90 (n/a)</td><td>406.72 (n/a)</td><td>471.10 (n/a)</td><td>244.60 (n/a)</td><td>143.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.60 (n/a)</td><td>409.36 (n/a)</td><td>420.10 (n/a)</td><td>271.60 (n/a)</td><td>96.64 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>582.70 (n/a)</td><td>471.54 (n/a)</td><td>494.70 (n/a)</td><td>247.30 (n/a)</td><td>135.71 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>594.50 (n/a)</td><td>421.88 (n/a)</td><td>482.70 (n/a)</td><td>218.30 (n/a)</td><td>154.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>598.70 (n/a)</td><td>480.78 (n/a)</td><td>544.20 (n/a)</td><td>237.70 (n/a)</td><td>144.60 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>578.80 (n/a)</td><td>434.24 (n/a)</td><td>479.40 (n/a)</td><td>203.70 (n/a)</td><td>155.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>598.60 (n/a)</td><td>415.56 (n/a)</td><td>452.30 (n/a)</td><td>236.50 (n/a)</td><td>147.84 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>477.80 (n/a)</td><td>426.54 (n/a)</td><td>447.40 (n/a)</td><td>309.50 (n/a)</td><td>67.87 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.60 (n/a)</td><td>462.36 (n/a)</td><td>458.20 (n/a)</td><td>278.70 (n/a)</td><td>116.25 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.30 (n/a)</td><td>423.86 (n/a)</td><td>420.40 (n/a)</td><td>313.30 (n/a)</td><td>74.63 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>916.10 (n/a)</td><td>546.54 (n/a)</td><td>520.50 (n/a)</td><td>281.10 (n/a)</td><td>232.23 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>630.90 (n/a)</td><td>427.16 (n/a)</td><td>472.70 (n/a)</td><td>236.10 (n/a)</td><td>168.61 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>663.30 (n/a)</td><td>530.20 (n/a)</td><td>529.20 (n/a)</td><td>424.00 (n/a)</td><td>90.67 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>670.90 (n/a)</td><td>514.38 (n/a)</td><td>523.90 (n/a)</td><td>307.00 (n/a)</td><td>132.53 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>423.50 (n/a)</td><td>330.32 (n/a)</td><td>305.10 (n/a)</td><td>282.50 (n/a)</td><td>56.35 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>725.50 (n/a)</td><td>552.98 (n/a)</td><td>635.10 (n/a)</td><td>202.00 (n/a)</td><td>215.06 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.00 (n/a)</td><td>408.10 (n/a)</td><td>408.00 (n/a)</td><td>265.70 (n/a)</td><td>129.28 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.00 (n/a)</td><td>482.42 (n/a)</td><td>543.20 (n/a)</td><td>225.60 (n/a)</td><td>162.88 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.10 (n/a)</td><td>398.40 (n/a)</td><td>355.90 (n/a)</td><td>289.50 (n/a)</td><td>131.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>683.30 (n/a)</td><td>464.98 (n/a)</td><td>472.50 (n/a)</td><td>236.20 (n/a)</td><td>192.33 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1066.20 (n/a)</td><td>549.48 (n/a)</td><td>528.20 (n/a)</td><td>262.80 (n/a)</td><td>317.25 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>517.70 (n/a)</td><td>421.38 (n/a)</td><td>442.10 (n/a)</td><td>277.10 (n/a)</td><td>92.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1696.30 (n/a)</td><td>662.24 (n/a)</td><td>476.20 (n/a)</td><td>247.20 (n/a)</td><td>599.11 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1016.80 (n/a)</td><td>549.58 (n/a)</td><td>453.30 (n/a)</td><td>234.10 (n/a)</td><td>292.19 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1020.30 (n/a)</td><td>486.42 (n/a)</td><td>373.80 (n/a)</td><td>220.70 (n/a)</td><td>330.90 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>660.80 (n/a)</td><td>436.52 (n/a)</td><td>366.80 (n/a)</td><td>327.40 (n/a)</td><td>138.99 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1891.80 (n/a)</td><td>707.42 (n/a)</td><td>342.60 (n/a)</td><td>275.30 (n/a)</td><td>687.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>869.40 (n/a)</td><td>490.92 (n/a)</td><td>440.20 (n/a)</td><td>264.90 (n/a)</td><td>255.51 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>557.00 (n/a)</td><td>439.30 (n/a)</td><td>504.20 (n/a)</td><td>250.10 (n/a)</td><td>128.05 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>602.90 (n/a)</td><td>383.94 (n/a)</td><td>341.30 (n/a)</td><td>264.80 (n/a)</td><td>132.29 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>689.50 (n/a)</td><td>463.98 (n/a)</td><td>490.60 (n/a)</td><td>305.50 (n/a)</td><td>161.80 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.62 (+9.34%)</td><td>0.44 (+5.40%)</td><td>0.42 (+11.07%)</td><td>0.25 (-4.10%)</td><td>0.15 (+18.65%)</td><td>893.80 (+4.27%)</td><td>558.16 (-2.62%)</td><td>528.40 (-9.98%)</td><td>354.10 (-8.55%)</td><td>213.05 (+14.88%)</td><td>26.65 (+9.34%)</td><td>18.77 (+5.40%)</td><td>17.86 (+11.07%)</td><td>10.56 (-4.10%)</td><td>6.37 (+18.65%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.57 (n/a)</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>857.20 (n/a)</td><td>573.18 (n/a)</td><td>587.00 (n/a)</td><td>387.20 (n/a)</td><td>185.45 (n/a)</td><td>24.37 (n/a)</td><td>17.81 (n/a)</td><td>16.08 (n/a)</td><td>11.01 (n/a)</td><td>5.37 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.65 (+6.87%)</td><td>0.43 (-9.88%)</td><td>0.35 <b>(-28.75%)</b></td><td>0.21 <b>(-31.17%)</b></td><td>0.18 <b>(+66.70%)</b></td><td>1029.70 <b>(+45.27%)</b></td><td>610.06 <b>(+24.04%)</b></td><td>639.80 <b>(+40.34%)</b></td><td>340.00 (-6.44%)</td><td>277.40 <b>(+108.84%)</b></td><td>27.76 (+6.87%)</td><td>18.19 (-9.88%)</td><td>14.75 <b>(-28.75%)</b></td><td>9.17 <b>(-31.17%)</b></td><td>7.88 <b>(+66.70%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.61 (n/a)</td><td>0.47 (n/a)</td><td>0.49 (n/a)</td><td>0.31 (n/a)</td><td>0.11 (n/a)</td><td>708.80 (n/a)</td><td>491.84 (n/a)</td><td>455.90 (n/a)</td><td>363.40 (n/a)</td><td>132.83 (n/a)</td><td>25.97 (n/a)</td><td>20.19 (n/a)</td><td>20.70 (n/a)</td><td>13.32 (n/a)</td><td>4.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.31 (+2.77%)</td><td>0.30 (+1.30%)</td><td>0.30 (-0.21%)</td><td>0.30 (+1.72%)</td><td>0.01 (+15.55%)</td><td>84009.40 (-1.69%)</td><td>82649.08 (-1.28%)</td><td>83183.90 (+0.21%)</td><td>80401.00 (-2.70%)</td><td>1402.57 (+10.38%)</td><td>213.68 (+2.77%)</td><td>207.91 (+1.30%)</td><td>206.53 (-0.21%)</td><td>204.50 (+1.72%)</td><td>3.58 (+15.55%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.00 (n/a)</td><td>85451.40 (n/a)</td><td>83721.64 (n/a)</td><td>83010.80 (n/a)</td><td>82628.60 (n/a)</td><td>1270.66 (n/a)</td><td>207.92 (n/a)</td><td>205.24 (n/a)</td><td>206.96 (n/a)</td><td>201.05 (n/a)</td><td>3.09 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>1.03 (-2.00%)</td><td>1.00 (-0.75%)</td><td>0.99 (-3.40%)</td><td>0.98 (+7.15%)</td><td>0.02 <b>(-60.87%)</b></td><td>25644.70 (-6.67%)</td><td>25188.24 (+0.56%)</td><td>25460.40 (+3.51%)</td><td>24437.10 (+2.04%)</td><td>514.74 <b>(-63.14%)</b></td><td>703.02 (-2.00%)</td><td>682.29 (-0.75%)</td><td>674.77 (-3.40%)</td><td>669.92 (+7.15%)</td><td>14.10 <b>(-60.87%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>1.05 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td><td>0.92 (n/a)</td><td>0.05 (n/a)</td><td>27478.40 (n/a)</td><td>25048.80 (n/a)</td><td>24595.90 (n/a)</td><td>23949.30 (n/a)</td><td>1396.47 (n/a)</td><td>717.34 (n/a)</td><td>687.46 (n/a)</td><td>698.49 (n/a)</td><td>625.21 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.82 (+0.28%)</td><td>0.81 (-0.29%)</td><td>0.81 (-0.79%)</td><td>0.80 (+0.35%)</td><td>0.01 (-1.33%)</td><td>94099.00 (-0.35%)</td><td>93480.90 (+0.29%)</td><td>93664.30 (+0.80%)</td><td>92429.90 (-0.27%)</td><td>698.44 (-1.98%)</td><td>743.48 (+0.28%)</td><td>735.15 (-0.29%)</td><td>733.68 (-0.79%)</td><td>730.29 (+0.35%)</td><td>5.52 (-1.33%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94431.40 (n/a)</td><td>93213.82 (n/a)</td><td>92924.90 (n/a)</td><td>92684.40 (n/a)</td><td>712.54 (n/a)</td><td>741.44 (n/a)</td><td>737.26 (n/a)</td><td>739.52 (n/a)</td><td>727.72 (n/a)</td><td>5.59 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.78 (+0.60%)</td><td>0.76 (-0.67%)</td><td>0.76 (-0.10%)</td><td>0.75 (-1.66%)</td><td>0.01 <b>(+117.10%)</b></td><td>101126.40 (+1.69%)</td><td>99577.48 (+0.69%)</td><td>99499.50 (+0.10%)</td><td>97408.40 (-0.59%)</td><td>1573.05 <b>(+119.83%)</b></td><td>705.48 (+0.60%)</td><td>690.25 (-0.67%)</td><td>690.65 (-0.10%)</td><td>679.54 (-1.66%)</td><td>10.95 <b>(+117.10%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99443.10 (n/a)</td><td>98897.74 (n/a)</td><td>99401.00 (n/a)</td><td>97991.40 (n/a)</td><td>715.56 (n/a)</td><td>701.28 (n/a)</td><td>694.88 (n/a)</td><td>691.34 (n/a)</td><td>691.04 (n/a)</td><td>5.04 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.80 (+0.01%)</td><td>0.79 (+0.24%)</td><td>0.79 (+0.38%)</td><td>0.79 (+0.36%)</td><td>0.01 (-12.83%)</td><td>95912.60 (-0.36%)</td><td>95136.78 (-0.25%)</td><td>95540.00 (-0.38%)</td><td>94076.40 (-0.01%)</td><td>821.23 (-13.16%)</td><td>730.46 (+0.01%)</td><td>722.37 (+0.24%)</td><td>719.27 (+0.38%)</td><td>716.48 (+0.36%)</td><td>6.26 (-12.83%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96261.40 (n/a)</td><td>95371.54 (n/a)</td><td>95902.40 (n/a)</td><td>94083.50 (n/a)</td><td>945.67 (n/a)</td><td>730.41 (n/a)</td><td>720.60 (n/a)</td><td>716.56 (n/a)</td><td>713.88 (n/a)</td><td>7.18 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.18 (-4.85%)</td><td>3.46 (-14.35%)</td><td>3.69 (-5.76%)</td><td>2.16 (-18.61%)</td><td>1.30 (-5.20%)</td><td>4125.50 <b>(+22.86%)</b></td><td>2910.72 (+19.63%)</td><td>2415.20 (+6.11%)</td><td>1721.60 (+5.10%)</td><td>1131.61 <b>(+34.96%)</b></td><td>311.84 (-4.85%)</td><td>208.27 (-14.35%)</td><td>222.29 (-5.76%)</td><td>130.14 (-18.61%)</td><td>78.34 (-5.20%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>5.44 (n/a)</td><td>4.04 (n/a)</td><td>3.92 (n/a)</td><td>2.65 (n/a)</td><td>1.37 (n/a)</td><td>3357.80 (n/a)</td><td>2433.14 (n/a)</td><td>2276.20 (n/a)</td><td>1638.10 (n/a)</td><td>838.50 (n/a)</td><td>327.74 (n/a)</td><td>243.16 (n/a)</td><td>235.87 (n/a)</td><td>159.89 (n/a)</td><td>82.64 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>4.36 (-8.62%)</td><td>2.84 <b>(-21.56%)</b></td><td>2.31 <b>(-35.88%)</b></td><td>2.13 (-5.74%)</td><td>0.94 (-15.65%)</td><td>4177.70 (+6.09%)</td><td>3369.64 <b>(+26.15%)</b></td><td>3864.70 <b>(+55.97%)</b></td><td>2044.90 (+9.43%)</td><td>906.76 (+2.50%)</td><td>262.54 (-8.62%)</td><td>171.34 <b>(-21.56%)</b></td><td>138.91 <b>(-35.88%)</b></td><td>128.51 (-5.74%)</td><td>56.60 (-15.65%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>4.77 (n/a)</td><td>3.63 (n/a)</td><td>3.60 (n/a)</td><td>2.26 (n/a)</td><td>1.11 (n/a)</td><td>3937.70 (n/a)</td><td>2671.06 (n/a)</td><td>2477.90 (n/a)</td><td>1868.60 (n/a)</td><td>884.62 (n/a)</td><td>287.31 (n/a)</td><td>218.43 (n/a)</td><td>216.66 (n/a)</td><td>136.34 (n/a)</td><td>67.11 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.41 (-2.64%)</td><td>3.23 (-18.98%)</td><td>2.22 <b>(-43.77%)</b></td><td>2.19 (+1.84%)</td><td>1.48 (-1.65%)</td><td>4072.90 (-1.81%)</td><td>3188.80 <b>(+25.12%)</b></td><td>4010.90 <b>(+77.83%)</b></td><td>1648.90 (+2.71%)</td><td>1193.11 (+10.82%)</td><td>325.59 (-2.64%)</td><td>194.74 (-18.98%)</td><td>133.85 <b>(-43.77%)</b></td><td>131.81 (+1.84%)</td><td>89.21 (-1.65%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>5.55 (n/a)</td><td>3.99 (n/a)</td><td>3.95 (n/a)</td><td>2.15 (n/a)</td><td>1.51 (n/a)</td><td>4147.80 (n/a)</td><td>2548.62 (n/a)</td><td>2255.50 (n/a)</td><td>1605.40 (n/a)</td><td>1076.62 (n/a)</td><td>334.42 (n/a)</td><td>240.35 (n/a)</td><td>238.03 (n/a)</td><td>129.43 (n/a)</td><td>90.70 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>6.74 (+4.42%)</td><td>6.04 (+7.04%)</td><td>6.13 (+3.14%)</td><td>4.98 <b>(+28.83%)</b></td><td>0.66 <b>(-36.49%)</b></td><td>6995.50 <b>(-22.38%)</b></td><td>5830.02 (-8.83%)</td><td>5691.20 (-3.04%)</td><td>5172.10 (-4.23%)</td><td>699.93 <b>(-53.15%)</b></td><td>415.21 (+4.42%)</td><td>372.25 (+7.04%)</td><td>377.33 (+3.14%)</td><td>306.98 <b>(+28.83%)</b></td><td>40.77 <b>(-36.49%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>6.46 (n/a)</td><td>5.65 (n/a)</td><td>5.94 (n/a)</td><td>3.87 (n/a)</td><td>1.04 (n/a)</td><td>9012.30 (n/a)</td><td>6394.58 (n/a)</td><td>5869.80 (n/a)</td><td>5400.40 (n/a)</td><td>1493.86 (n/a)</td><td>397.65 (n/a)</td><td>347.76 (n/a)</td><td>365.85 (n/a)</td><td>238.28 (n/a)</td><td>64.20 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.63 (-1.84%)</td><td>4.66 (+3.15%)</td><td>4.69 (+5.54%)</td><td>3.82 (+2.26%)</td><td>0.77 (-3.40%)</td><td>9118.30 (-2.21%)</td><td>7656.82 (-3.18%)</td><td>7435.40 (-5.25%)</td><td>6191.70 (+1.88%)</td><td>1273.29 (-2.90%)</td><td>346.83 (-1.84%)</td><td>286.78 (+3.15%)</td><td>288.82 (+5.54%)</td><td>235.51 (+2.26%)</td><td>47.67 (-3.40%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>5.74 (n/a)</td><td>4.51 (n/a)</td><td>4.44 (n/a)</td><td>3.74 (n/a)</td><td>0.80 (n/a)</td><td>9324.60 (n/a)</td><td>7908.62 (n/a)</td><td>7847.00 (n/a)</td><td>6077.60 (n/a)</td><td>1311.27 (n/a)</td><td>353.34 (n/a)</td><td>278.03 (n/a)</td><td>273.67 (n/a)</td><td>230.30 (n/a)</td><td>49.34 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>6.45 (+1.11%)</td><td>5.78 (+6.03%)</td><td>5.98 (+14.58%)</td><td>5.05 (+9.95%)</td><td>0.68 (-3.40%)</td><td>6909.60 (-9.05%)</td><td>6099.72 (-5.86%)</td><td>5829.60 (-12.72%)</td><td>5401.70 (-1.10%)</td><td>739.76 (-11.33%)</td><td>397.56 (+1.11%)</td><td>356.14 (+6.03%)</td><td>368.38 (+14.58%)</td><td>310.80 (+9.95%)</td><td>42.05 (-3.40%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>6.38 (n/a)</td><td>5.45 (n/a)</td><td>5.22 (n/a)</td><td>4.59 (n/a)</td><td>0.71 (n/a)</td><td>7596.90 (n/a)</td><td>6479.64 (n/a)</td><td>6679.50 (n/a)</td><td>5461.70 (n/a)</td><td>834.33 (n/a)</td><td>393.19 (n/a)</td><td>335.88 (n/a)</td><td>321.50 (n/a)</td><td>282.68 (n/a)</td><td>43.53 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.77 (-2.15%)</td><td>0.76 (-1.60%)</td><td>0.76 (-0.94%)</td><td>0.74 (-2.14%)</td><td>0.01 (-8.55%)</td><td>101684.90 (+2.19%)</td><td>99468.84 (+1.63%)</td><td>98916.50 (+0.95%)</td><td>98484.10 (+2.20%)</td><td>1314.17 (-4.28%)</td><td>697.77 (-2.15%)</td><td>690.96 (-1.60%)</td><td>694.72 (-0.94%)</td><td>675.81 (-2.14%)</td><td>9.01 (-8.55%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99505.60 (n/a)</td><td>97876.96 (n/a)</td><td>97983.80 (n/a)</td><td>96365.40 (n/a)</td><td>1372.97 (n/a)</td><td>713.11 (n/a)</td><td>702.21 (n/a)</td><td>701.34 (n/a)</td><td>690.61 (n/a)</td><td>9.85 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.74 (-3.97%)</td><td>0.74 (-0.54%)</td><td>0.74 (+0.50%)</td><td>0.73 (+1.31%)</td><td>0.01 <b>(-73.87%)</b></td><td>103491.20 (-1.30%)</td><td>102191.78 (+0.48%)</td><td>102010.30 (-0.49%)</td><td>101348.80 (+4.14%)</td><td>797.65 <b>(-73.06%)</b></td><td>678.05 (-3.97%)</td><td>672.49 (-0.54%)</td><td>673.65 (+0.50%)</td><td>664.01 (+1.31%)</td><td>5.22 <b>(-73.87%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.72 (n/a)</td><td>0.02 (n/a)</td><td>104849.70 (n/a)</td><td>101703.62 (n/a)</td><td>102516.30 (n/a)</td><td>97321.20 (n/a)</td><td>2960.52 (n/a)</td><td>706.11 (n/a)</td><td>676.15 (n/a)</td><td>670.33 (n/a)</td><td>655.41 (n/a)</td><td>19.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.81 (+0.53%)</td><td>0.80 (+0.24%)</td><td>0.80 (-0.29%)</td><td>0.79 (-0.08%)</td><td>0.01 <b>(+25.38%)</b></td><td>95393.80 (+0.08%)</td><td>94095.68 (-0.23%)</td><td>94315.00 (+0.29%)</td><td>92913.10 (-0.53%)</td><td>963.00 <b>(+24.69%)</b></td><td>739.61 (+0.53%)</td><td>730.38 (+0.24%)</td><td>728.62 (-0.29%)</td><td>720.38 (-0.08%)</td><td>7.47 <b>(+25.38%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95314.90 (n/a)</td><td>94314.12 (n/a)</td><td>94038.00 (n/a)</td><td>93407.40 (n/a)</td><td>772.32 (n/a)</td><td>735.70 (n/a)</td><td>728.66 (n/a)</td><td>730.76 (n/a)</td><td>720.97 (n/a)</td><td>5.96 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.37 (+3.02%)</td><td>2.39 (+5.46%)</td><td>2.27 (-3.05%)</td><td>1.56 (+16.35%)</td><td>0.78 (-11.75%)</td><td>5176.10 (-14.05%)</td><td>3682.30 (-9.76%)</td><td>3550.50 (+3.15%)</td><td>2394.80 (-2.93%)</td><td>1198.91 <b>(-29.38%)</b></td><td>882.73 (+3.02%)</td><td>626.55 (+5.46%)</td><td>595.39 (-3.05%)</td><td>408.40 (+16.35%)</td><td>204.93 (-11.75%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>3.27 (n/a)</td><td>2.27 (n/a)</td><td>2.34 (n/a)</td><td>1.34 (n/a)</td><td>0.89 (n/a)</td><td>6022.40 (n/a)</td><td>4080.60 (n/a)</td><td>3442.10 (n/a)</td><td>2467.00 (n/a)</td><td>1697.66 (n/a)</td><td>856.88 (n/a)</td><td>594.11 (n/a)</td><td>614.15 (n/a)</td><td>351.01 (n/a)</td><td>232.21 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.21 <b>(-34.74%)</b></td><td>0.20 (-11.91%)</td><td>0.20 (+11.45%)</td><td>0.18 (+1.31%)</td><td>0.01 <b>(-82.24%)</b></td><td>6780.00 (-1.29%)</td><td>6266.60 (+7.59%)</td><td>6092.30 (-10.28%)</td><td>5883.00 <b>(+53.23%)</b></td><td>366.44 <b>(-74.11%)</b></td><td>11.41 <b>(-34.74%)</b></td><td>10.74 (-11.91%)</td><td>11.02 (+11.45%)</td><td>9.90 (+1.31%)</td><td>0.61 <b>(-82.24%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>6868.70 (n/a)</td><td>5824.60 (n/a)</td><td>6790.10 (n/a)</td><td>3839.40 (n/a)</td><td>1415.23 (n/a)</td><td>17.48 (n/a)</td><td>12.19 (n/a)</td><td>9.88 (n/a)</td><td>9.77 (n/a)</td><td>3.46 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 <b>(-22.15%)</b></td><td>0.07 <b>(-38.73%)</b></td><td>0.06 <b>(-47.81%)</b></td><td>0.05 <b>(-31.90%)</b></td><td>0.02 (-8.13%)</td><td>0.10 <b>(-22.15%)</b></td><td>0.07 <b>(-38.73%)</b></td><td>0.06 <b>(-47.81%)</b></td><td>0.05 <b>(-31.90%)</b></td><td>0.02 (-8.13%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.93 (+3.33%)</td><td>3.61 (-1.15%)</td><td>3.70 (+0.42%)</td><td>3.21 (-7.25%)</td><td>0.31 <b>(+142.68%)</b></td><td>3.93 (+3.33%)</td><td>3.60 (-1.15%)</td><td>3.69 (+0.42%)</td><td>3.20 (-7.25%)</td><td>0.31 <b>(+142.68%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>3.80 (n/a)</td><td>3.65 (n/a)</td><td>3.68 (n/a)</td><td>3.46 (n/a)</td><td>0.13 (n/a)</td><td>3.80 (n/a)</td><td>3.65 (n/a)</td><td>3.68 (n/a)</td><td>3.45 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>7.63 (+13.29%)</td><td>6.31 (-1.81%)</td><td>6.52 (-0.81%)</td><td>5.19 (-9.35%)</td><td>0.99 <b>(+146.64%)</b></td><td>7.63 (+13.29%)</td><td>6.31 (-1.81%)</td><td>6.51 (-0.81%)</td><td>5.18 (-9.35%)</td><td>0.99 <b>(+146.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>6.74 (n/a)</td><td>6.43 (n/a)</td><td>6.57 (n/a)</td><td>5.72 (n/a)</td><td>0.40 (n/a)</td><td>6.73 (n/a)</td><td>6.42 (n/a)</td><td>6.57 (n/a)</td><td>5.72 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>14.22 (+10.57%)</td><td>10.80 (+8.43%)</td><td>10.08 (+1.12%)</td><td>8.15 (+4.10%)</td><td>2.87 <b>(+52.24%)</b></td><td>14.21 (+10.57%)</td><td>10.80 (+8.43%)</td><td>10.07 (+1.12%)</td><td>8.14 (+4.10%)</td><td>2.87 <b>(+52.24%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>12.86 (n/a)</td><td>9.96 (n/a)</td><td>9.97 (n/a)</td><td>7.83 (n/a)</td><td>1.89 (n/a)</td><td>12.85 (n/a)</td><td>9.96 (n/a)</td><td>9.96 (n/a)</td><td>7.82 (n/a)</td><td>1.88 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.91 (+6.24%)</td><td>3.71 (+4.75%)</td><td>3.75 (+6.96%)</td><td>3.36 (-0.90%)</td><td>0.20 <b>(+81.32%)</b></td><td>3.91 (+6.24%)</td><td>3.70 (+4.75%)</td><td>3.75 (+6.96%)</td><td>3.36 (-0.90%)</td><td>0.20 <b>(+81.32%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>3.68 (n/a)</td><td>3.54 (n/a)</td><td>3.51 (n/a)</td><td>3.39 (n/a)</td><td>0.11 (n/a)</td><td>3.68 (n/a)</td><td>3.53 (n/a)</td><td>3.51 (n/a)</td><td>3.39 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>7.44 (+6.00%)</td><td>6.71 (+9.40%)</td><td>6.88 (+5.38%)</td><td>5.67 <b>(+24.20%)</b></td><td>0.65 <b>(-37.23%)</b></td><td>7.44 (+6.00%)</td><td>6.71 (+9.40%)</td><td>6.87 (+5.38%)</td><td>5.66 <b>(+24.20%)</b></td><td>0.65 <b>(-37.23%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>7.02 (n/a)</td><td>6.13 (n/a)</td><td>6.52 (n/a)</td><td>4.56 (n/a)</td><td>1.04 (n/a)</td><td>7.02 (n/a)</td><td>6.13 (n/a)</td><td>6.52 (n/a)</td><td>4.56 (n/a)</td><td>1.04 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>14.77 (+4.15%)</td><td>10.88 (+2.35%)</td><td>10.12 (+17.73%)</td><td>8.12 (-1.80%)</td><td>2.65 (-13.22%)</td><td>14.76 (+4.15%)</td><td>10.87 (+2.35%)</td><td>10.11 (+17.73%)</td><td>8.11 (-1.80%)</td><td>2.65 (-13.22%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>14.18 (n/a)</td><td>10.63 (n/a)</td><td>8.59 (n/a)</td><td>8.27 (n/a)</td><td>3.06 (n/a)</td><td>14.18 (n/a)</td><td>10.62 (n/a)</td><td>8.59 (n/a)</td><td>8.26 (n/a)</td><td>3.06 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2066.30 (n/a)</td><td>723.48 (n/a)</td><td>478.00 (n/a)</td><td>260.50 (n/a)</td><td>757.63 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.50 (n/a)</td><td>358.88 (n/a)</td><td>279.60 (n/a)</td><td>226.80 (n/a)</td><td>157.67 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>475.20 (n/a)</td><td>293.26 (n/a)</td><td>244.90 (n/a)</td><td>222.00 (n/a)</td><td>104.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1360.70 (n/a)</td><td>560.06 (n/a)</td><td>306.40 (n/a)</td><td>226.50 (n/a)</td><td>475.06 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2459.00 (n/a)</td><td>831.88 (n/a)</td><td>421.70 (n/a)</td><td>212.80 (n/a)</td><td>927.88 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>627.60 (n/a)</td><td>486.34 (n/a)</td><td>518.90 (n/a)</td><td>350.90 (n/a)</td><td>118.92 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>435.90 (n/a)</td><td>290.08 (n/a)</td><td>270.30 (n/a)</td><td>221.70 (n/a)</td><td>84.37 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>670.20 (n/a)</td><td>462.94 (n/a)</td><td>490.50 (n/a)</td><td>242.00 (n/a)</td><td>154.43 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.50 (n/a)</td><td>395.42 (n/a)</td><td>370.30 (n/a)</td><td>257.50 (n/a)</td><td>144.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.90 (n/a)</td><td>396.64 (n/a)</td><td>288.50 (n/a)</td><td>262.90 (n/a)</td><td>167.43 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>429.20 (n/a)</td><td>320.42 (n/a)</td><td>287.70 (n/a)</td><td>274.10 (n/a)</td><td>65.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>500.10 (n/a)</td><td>438.52 (n/a)</td><td>448.60 (n/a)</td><td>378.00 (n/a)</td><td>47.10 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>317.50 (n/a)</td><td>295.48 (n/a)</td><td>307.30 (n/a)</td><td>255.30 (n/a)</td><td>25.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>605.00 (n/a)</td><td>452.96 (n/a)</td><td>440.40 (n/a)</td><td>330.40 (n/a)</td><td>99.49 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>608.50 (n/a)</td><td>416.08 (n/a)</td><td>470.80 (n/a)</td><td>195.60 (n/a)</td><td>189.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>584.60 (n/a)</td><td>454.98 (n/a)</td><td>467.40 (n/a)</td><td>310.00 (n/a)</td><td>101.43 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>510.40 (n/a)</td><td>373.00 (n/a)</td><td>329.50 (n/a)</td><td>239.30 (n/a)</td><td>128.43 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>647.00 (n/a)</td><td>516.12 (n/a)</td><td>537.60 (n/a)</td><td>402.80 (n/a)</td><td>93.89 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (-13.57%)</td><td>0.08 <b>(-23.56%)</b></td><td>0.09 (-15.10%)</td><td>0.05 <b>(-48.04%)</b></td><td>0.03 <b>(+113.21%)</b></td><td>674.20 <b>(+92.46%)</b></td><td>431.30 <b>(+42.16%)</b></td><td>353.90 (+17.77%)</td><td>301.20 (+15.71%)</td><td>157.96 <b>(+370.41%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>350.30 (n/a)</td><td>303.38 (n/a)</td><td>300.50 (n/a)</td><td>260.30 (n/a)</td><td>33.58 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>504.40 (n/a)</td><td>371.00 (n/a)</td><td>339.80 (n/a)</td><td>267.50 (n/a)</td><td>107.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>556.10 (n/a)</td><td>340.06 (n/a)</td><td>285.30 (n/a)</td><td>276.80 (n/a)</td><td>120.98 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>594.10 (n/a)</td><td>468.30 (n/a)</td><td>507.60 (n/a)</td><td>238.30 (n/a)</td><td>149.37 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>620.70 (n/a)</td><td>455.34 (n/a)</td><td>441.80 (n/a)</td><td>312.30 (n/a)</td><td>111.22 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>613.20 (n/a)</td><td>417.28 (n/a)</td><td>430.60 (n/a)</td><td>261.90 (n/a)</td><td>147.40 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (+13.48%)</td><td>0.01 (+16.01%)</td><td>0.01 <b>(+28.16%)</b></td><td>0.01 (+6.11%)</td><td>0.00 (+6.33%)</td><td>543.90 (-5.77%)</td><td>323.34 (-13.44%)</td><td>283.90 <b>(-21.98%)</b></td><td>232.00 (-11.89%)</td><td>125.82 (-2.02%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>577.20 (n/a)</td><td>373.54 (n/a)</td><td>363.90 (n/a)</td><td>263.30 (n/a)</td><td>128.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 <b>(-26.08%)</b></td><td>0.01 <b>(-30.80%)</b></td><td>0.01 <b>(-35.65%)</b></td><td>0.01 (-18.51%)</td><td>0.00 <b>(-37.65%)</b></td><td>502.90 <b>(+22.72%)</b></td><td>406.22 <b>(+42.43%)</b></td><td>391.70 <b>(+55.37%)</b></td><td>320.70 <b>(+35.26%)</b></td><td>71.42 (+0.61%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>409.80 (n/a)</td><td>285.20 (n/a)</td><td>252.10 (n/a)</td><td>237.10 (n/a)</td><td>70.99 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (-0.18%)</td><td>0.01 (+10.14%)</td><td>0.01 (+7.76%)</td><td>0.01 (+8.23%)</td><td>0.00 (-17.72%)</td><td>557.60 (-7.59%)</td><td>358.94 (-13.24%)</td><td>334.10 (-7.22%)</td><td>234.60 (+0.17%)</td><td>119.51 <b>(-24.28%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.40 (n/a)</td><td>413.70 (n/a)</td><td>360.10 (n/a)</td><td>234.20 (n/a)</td><td>157.82 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (-0.98%)</td><td>0.01 (+10.93%)</td><td>0.01 <b>(+46.08%)</b></td><td>0.01 (+0.84%)</td><td>0.00 (-6.00%)</td><td>526.40 (-0.83%)</td><td>383.32 (-10.71%)</td><td>343.40 <b>(-31.55%)</b></td><td>238.60 (+0.97%)</td><td>125.58 (-3.89%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.80 (n/a)</td><td>429.32 (n/a)</td><td>501.70 (n/a)</td><td>236.30 (n/a)</td><td>130.66 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (-16.64%)</td><td>0.01 (-17.93%)</td><td>0.01 <b>(-47.30%)</b></td><td>0.01 (+19.35%)</td><td>0.00 <b>(-34.72%)</b></td><td>565.40 (-16.21%)</td><td>433.56 (+6.85%)</td><td>514.60 <b>(+89.75%)</b></td><td>265.50 (+19.97%)</td><td>144.59 <b>(-36.41%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>674.80 (n/a)</td><td>405.78 (n/a)</td><td>271.20 (n/a)</td><td>221.30 (n/a)</td><td>227.38 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (-12.94%)</td><td>0.01 (-7.54%)</td><td>0.01 (-8.93%)</td><td>0.01 <b>(+30.58%)</b></td><td>0.00 <b>(-41.23%)</b></td><td>436.90 <b>(-23.43%)</b></td><td>338.90 (+1.14%)</td><td>307.10 (+9.84%)</td><td>270.40 (+14.87%)</td><td>67.27 <b>(-50.44%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.60 (n/a)</td><td>335.08 (n/a)</td><td>279.60 (n/a)</td><td>235.40 (n/a)</td><td>135.72 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 <b>(-24.25%)</b></td><td>0.01 <b>(-30.01%)</b></td><td>0.01 <b>(-27.84%)</b></td><td>0.01 <b>(-25.43%)</b></td><td>0.00 (-18.22%)</td><td>611.90 <b>(+34.10%)</b></td><td>491.68 <b>(+44.40%)</b></td><td>472.90 <b>(+38.60%)</b></td><td>305.20 <b>(+32.01%)</b></td><td>125.30 <b>(+47.17%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>456.30 (n/a)</td><td>340.50 (n/a)</td><td>341.20 (n/a)</td><td>231.20 (n/a)</td><td>85.14 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 <b>(-44.89%)</b></td><td>0.01 <b>(-41.27%)</b></td><td>0.01 <b>(-32.47%)</b></td><td>0.00 <b>(-66.39%)</b></td><td>0.00 <b>(-37.49%)</b></td><td>2419.00 <b>(+197.58%)</b></td><td>913.86 <b>(+107.52%)</b></td><td>526.90 <b>(+48.09%)</b></td><td>485.70 <b>(+81.43%)</b></td><td>843.20 <b>(+269.98%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>812.90 (n/a)</td><td>440.38 (n/a)</td><td>355.80 (n/a)</td><td>267.70 (n/a)</td><td>227.91 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (+11.24%)</td><td>0.01 (+10.94%)</td><td>0.01 (+3.27%)</td><td>0.01 (-1.63%)</td><td>0.01 <b>(+38.52%)</b></td><td>612.50 (+1.66%)</td><td>397.26 (-4.21%)</td><td>397.30 (-3.17%)</td><td>222.80 (-10.13%)</td><td>164.98 <b>(+24.28%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.50 (n/a)</td><td>414.72 (n/a)</td><td>410.30 (n/a)</td><td>247.90 (n/a)</td><td>132.74 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (-8.76%)</td><td>0.01 <b>(-28.68%)</b></td><td>0.01 <b>(-24.80%)</b></td><td>0.01 <b>(-51.97%)</b></td><td>0.00 <b>(+127.39%)</b></td><td>674.80 <b>(+108.21%)</b></td><td>424.62 <b>(+55.60%)</b></td><td>354.20 <b>(+32.96%)</b></td><td>270.00 (+9.62%)</td><td>168.86 <b>(+425.50%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>324.10 (n/a)</td><td>272.90 (n/a)</td><td>266.40 (n/a)</td><td>246.30 (n/a)</td><td>32.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (-1.92%)</td><td>0.01 (-11.67%)</td><td>0.01 <b>(-29.42%)</b></td><td>0.01 (+5.61%)</td><td>0.00 (-15.66%)</td><td>591.70 (-5.31%)</td><td>432.72 (+9.61%)</td><td>430.30 <b>(+41.69%)</b></td><td>274.50 (+1.97%)</td><td>126.86 (-17.86%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>624.90 (n/a)</td><td>394.78 (n/a)</td><td>303.70 (n/a)</td><td>269.20 (n/a)</td><td>154.44 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (-0.25%)</td><td>0.01 (-4.70%)</td><td>0.01 (-17.75%)</td><td>0.01 (+1.13%)</td><td>0.00 (+0.93%)</td><td>545.20 (-1.12%)</td><td>423.92 (+4.80%)</td><td>459.10 <b>(+21.58%)</b></td><td>265.40 (+0.26%)</td><td>104.24 (-3.83%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.40 (n/a)</td><td>404.52 (n/a)</td><td>377.60 (n/a)</td><td>264.70 (n/a)</td><td>108.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (-12.77%)</td><td>0.02 <b>(-42.25%)</b></td><td>0.02 <b>(-48.11%)</b></td><td>0.02 <b>(-52.04%)</b></td><td>0.01 <b>(+197.30%)</b></td><td>522.60 <b>(+108.46%)</b></td><td>438.40 <b>(+85.12%)</b></td><td>473.00 <b>(+92.75%)</b></td><td>251.50 (+14.63%)</td><td>106.86 <b>(+576.84%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>250.70 (n/a)</td><td>236.82 (n/a)</td><td>245.40 (n/a)</td><td>219.40 (n/a)</td><td>15.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (-5.34%)</td><td>0.03 (-8.81%)</td><td>0.03 (-7.79%)</td><td>0.02 (+2.10%)</td><td>0.01 (-12.05%)</td><td>493.70 (-2.04%)</td><td>336.42 (+7.95%)</td><td>303.00 (+8.49%)</td><td>251.80 (+5.62%)</td><td>97.75 (-11.11%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.00 (n/a)</td><td>311.64 (n/a)</td><td>279.30 (n/a)</td><td>238.40 (n/a)</td><td>109.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (+11.81%)</td><td>0.02 (-19.26%)</td><td>0.02 <b>(-35.29%)</b></td><td>0.01 <b>(-27.97%)</b></td><td>0.01 <b>(+56.61%)</b></td><td>600.40 <b>(+38.82%)</b></td><td>417.92 <b>(+36.17%)</b></td><td>411.10 <b>(+54.55%)</b></td><td>213.50 (-10.56%)</td><td>163.28 <b>(+100.00%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>432.50 (n/a)</td><td>306.90 (n/a)</td><td>266.00 (n/a)</td><td>238.70 (n/a)</td><td>81.64 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (+2.63%)</td><td>0.02 (-15.96%)</td><td>0.02 <b>(-20.56%)</b></td><td>0.02 <b>(-20.24%)</b></td><td>0.01 <b>(+46.65%)</b></td><td>540.00 <b>(+25.38%)</b></td><td>392.08 <b>(+26.08%)</b></td><td>372.90 <b>(+25.85%)</b></td><td>233.10 (-2.55%)</td><td>129.60 <b>(+78.79%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>430.70 (n/a)</td><td>310.98 (n/a)</td><td>296.30 (n/a)</td><td>239.20 (n/a)</td><td>72.49 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (-14.21%)</td><td>0.02 <b>(-32.49%)</b></td><td>0.02 <b>(-45.21%)</b></td><td>0.01 (-12.29%)</td><td>0.01 <b>(-26.85%)</b></td><td>632.50 (+14.01%)</td><td>445.58 <b>(+42.73%)</b></td><td>432.10 <b>(+82.55%)</b></td><td>264.40 (+16.58%)</td><td>131.16 (-6.39%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.80 (n/a)</td><td>312.18 (n/a)</td><td>236.70 (n/a)</td><td>226.80 (n/a)</td><td>140.11 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (-18.66%)</td><td>0.02 (-13.92%)</td><td>0.02 <b>(-24.67%)</b></td><td>0.02 (-0.75%)</td><td>0.01 <b>(-32.97%)</b></td><td>481.40 (+0.75%)</td><td>357.46 (+9.45%)</td><td>329.30 <b>(+32.73%)</b></td><td>246.40 <b>(+22.95%)</b></td><td>106.87 <b>(-20.99%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>477.80 (n/a)</td><td>326.60 (n/a)</td><td>248.10 (n/a)</td><td>200.40 (n/a)</td><td>135.26 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 <b>(+52.71%)</b></td><td>0.03 (+18.73%)</td><td>0.02 (+19.25%)</td><td>0.02 (+17.92%)</td><td>0.01 <b>(+65.40%)</b></td><td>478.70 (-15.20%)</td><td>369.86 (-12.00%)</td><td>398.20 (-16.15%)</td><td>182.20 <b>(-34.51%)</b></td><td>123.99 (-3.43%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.50 (n/a)</td><td>420.28 (n/a)</td><td>474.90 (n/a)</td><td>278.20 (n/a)</td><td>128.40 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (-10.15%)</td><td>0.02 (-15.73%)</td><td>0.02 <b>(-25.40%)</b></td><td>0.01 <b>(-21.55%)</b></td><td>0.01 (-10.46%)</td><td>596.80 <b>(+27.47%)</b></td><td>397.56 (+19.40%)</td><td>353.80 <b>(+34.07%)</b></td><td>248.30 (+11.30%)</td><td>142.34 <b>(+21.97%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>468.20 (n/a)</td><td>332.96 (n/a)</td><td>263.90 (n/a)</td><td>223.10 (n/a)</td><td>116.70 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 <b>(-28.51%)</b></td><td>0.02 (-19.54%)</td><td>0.02 (-15.85%)</td><td>0.01 (+5.87%)</td><td>0.00 <b>(-50.40%)</b></td><td>573.20 (-5.55%)</td><td>444.04 (+14.66%)</td><td>424.50 (+18.84%)</td><td>320.30 <b>(+39.87%)</b></td><td>102.64 <b>(-33.35%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.90 (n/a)</td><td>387.28 (n/a)</td><td>357.20 (n/a)</td><td>229.00 (n/a)</td><td>154.00 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (-4.18%)</td><td>0.02 (-12.29%)</td><td>0.02 <b>(-25.79%)</b></td><td>0.01 (-7.89%)</td><td>0.01 (-4.06%)</td><td>613.00 (+8.57%)</td><td>473.06 (+13.91%)</td><td>542.70 <b>(+34.73%)</b></td><td>261.00 (+4.36%)</td><td>143.64 (+3.24%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.60 (n/a)</td><td>415.30 (n/a)</td><td>402.80 (n/a)</td><td>250.10 (n/a)</td><td>139.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 <b>(-37.95%)</b></td><td>0.01 <b>(-25.51%)</b></td><td>0.01 (-7.27%)</td><td>0.00 <b>(-67.55%)</b></td><td>0.01 (-16.40%)</td><td>1967.60 <b>(+208.16%)</b></td><td>818.82 <b>(+64.81%)</b></td><td>556.30 (+7.83%)</td><td>457.00 <b>(+61.14%)</b></td><td>644.39 <b>(+380.85%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.50 (n/a)</td><td>496.82 (n/a)</td><td>515.90 (n/a)</td><td>283.60 (n/a)</td><td>134.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (+15.91%)</td><td>0.02 (-0.52%)</td><td>0.02 (-9.83%)</td><td>0.01 (-3.78%)</td><td>0.01 <b>(+46.70%)</b></td><td>706.30 (+3.93%)</td><td>525.74 (+3.97%)</td><td>536.60 (+10.91%)</td><td>309.50 (-13.74%)</td><td>145.60 <b>(+25.55%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>679.60 (n/a)</td><td>505.68 (n/a)</td><td>483.80 (n/a)</td><td>358.80 (n/a)</td><td>115.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (+13.08%)</td><td>0.06 (+16.76%)</td><td>0.06 <b>(+37.72%)</b></td><td>0.03 (-9.45%)</td><td>0.02 (+13.40%)</td><td>483.10 (+10.42%)</td><td>300.10 (-12.82%)</td><td>286.80 <b>(-27.39%)</b></td><td>170.50 (-11.57%)</td><td>114.05 (+12.06%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>437.50 (n/a)</td><td>344.22 (n/a)</td><td>395.00 (n/a)</td><td>192.80 (n/a)</td><td>101.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (+2.65%)</td><td>0.06 (+8.98%)</td><td>0.06 (-1.80%)</td><td>0.03 <b>(+22.21%)</b></td><td>0.01 <b>(-24.71%)</b></td><td>529.30 (-18.18%)</td><td>321.86 (-14.54%)</td><td>285.00 (+1.82%)</td><td>237.30 (-2.59%)</td><td>117.91 <b>(-33.23%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>646.90 (n/a)</td><td>376.60 (n/a)</td><td>279.90 (n/a)</td><td>243.60 (n/a)</td><td>176.59 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (+1.64%)</td><td>0.04 (+5.60%)</td><td>0.03 (+4.51%)</td><td>0.01 <b>(-62.63%)</b></td><td>0.03 <b>(+40.02%)</b></td><td>1898.40 <b>(+167.61%)</b></td><td>674.56 <b>(+43.62%)</b></td><td>501.30 (-4.33%)</td><td>224.80 (-1.62%)</td><td>697.40 <b>(+280.10%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>709.40 (n/a)</td><td>469.68 (n/a)</td><td>524.00 (n/a)</td><td>228.50 (n/a)</td><td>183.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 <b>(+21.62%)</b></td><td>0.05 <b>(+27.52%)</b></td><td>0.06 (+17.81%)</td><td>0.01 (-4.18%)</td><td>0.03 <b>(+20.84%)</b></td><td>1919.30 (+4.37%)</td><td>588.42 (-8.94%)</td><td>260.10 (-15.11%)</td><td>225.10 (-17.79%)</td><td>744.53 (+10.40%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1839.00 (n/a)</td><td>646.22 (n/a)</td><td>306.40 (n/a)</td><td>273.80 (n/a)</td><td>674.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (-10.67%)</td><td>0.04 (-10.54%)</td><td>0.03 (-12.40%)</td><td>0.03 (+4.59%)</td><td>0.01 (-18.77%)</td><td>592.70 (-4.39%)</td><td>454.62 (+9.05%)</td><td>494.20 (+14.16%)</td><td>288.70 (+11.94%)</td><td>121.20 (-13.09%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>619.90 (n/a)</td><td>416.88 (n/a)</td><td>432.90 (n/a)</td><td>257.90 (n/a)</td><td>139.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (-14.50%)</td><td>0.06 <b>(+27.10%)</b></td><td>0.06 <b>(+41.82%)</b></td><td>0.05 <b>(+69.73%)</b></td><td>0.01 <b>(-62.82%)</b></td><td>302.60 <b>(-41.08%)</b></td><td>260.02 <b>(-28.82%)</b></td><td>267.00 <b>(-29.48%)</b></td><td>218.70 (+16.95%)</td><td>32.36 <b>(-72.61%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>513.60 (n/a)</td><td>365.32 (n/a)</td><td>378.60 (n/a)</td><td>187.00 (n/a)</td><td>118.14 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (-19.99%)</td><td>0.05 (+14.40%)</td><td>0.05 <b>(+64.19%)</b></td><td>0.04 <b>(+62.00%)</b></td><td>0.01 <b>(-60.91%)</b></td><td>413.60 <b>(-38.28%)</b></td><td>319.02 <b>(-27.08%)</b></td><td>304.50 <b>(-39.10%)</b></td><td>245.40 <b>(+25.01%)</b></td><td>61.39 <b>(-68.98%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>670.10 (n/a)</td><td>437.52 (n/a)</td><td>500.00 (n/a)</td><td>196.30 (n/a)</td><td>197.91 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (-8.92%)</td><td>0.05 (-19.50%)</td><td>0.06 (+1.64%)</td><td>0.01 <b>(-80.96%)</b></td><td>0.03 <b>(+100.43%)</b></td><td>2017.80 <b>(+425.20%)</b></td><td>641.90 <b>(+128.00%)</b></td><td>266.80 (-1.62%)</td><td>230.20 (+9.83%)</td><td>774.20 <b>(+1077.78%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>384.20 (n/a)</td><td>281.54 (n/a)</td><td>271.20 (n/a)</td><td>209.60 (n/a)</td><td>65.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (+19.44%)</td><td>0.05 (+17.10%)</td><td>0.04 (-1.03%)</td><td>0.03 (+1.33%)</td><td>0.02 <b>(+75.61%)</b></td><td>530.70 (-1.32%)</td><td>374.74 (-9.81%)</td><td>409.40 (+1.04%)</td><td>245.60 (-16.26%)</td><td>123.77 <b>(+36.97%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>537.80 (n/a)</td><td>415.52 (n/a)</td><td>405.20 (n/a)</td><td>293.30 (n/a)</td><td>90.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 <b>(+34.51%)</b></td><td>0.04 (+3.48%)</td><td>0.03 (-18.62%)</td><td>0.02 <b>(-45.11%)</b></td><td>0.02 <b>(+179.31%)</b></td><td>1015.10 <b>(+82.21%)</b></td><td>533.12 <b>(+21.62%)</b></td><td>534.80 <b>(+22.89%)</b></td><td>247.50 <b>(-25.65%)</b></td><td>309.05 <b>(+255.48%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>557.10 (n/a)</td><td>438.34 (n/a)</td><td>435.20 (n/a)</td><td>332.90 (n/a)</td><td>86.94 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (-5.69%)</td><td>0.03 (-19.00%)</td><td>0.03 <b>(-29.65%)</b></td><td>0.02 (-18.57%)</td><td>0.01 (+13.71%)</td><td>697.40 <b>(+22.80%)</b></td><td>509.92 <b>(+26.00%)</b></td><td>533.30 <b>(+42.14%)</b></td><td>336.40 (+6.05%)</td><td>133.32 <b>(+39.03%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>567.90 (n/a)</td><td>404.70 (n/a)</td><td>375.20 (n/a)</td><td>317.20 (n/a)</td><td>95.90 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (-6.35%)</td><td>0.03 (+3.76%)</td><td>0.04 (+17.03%)</td><td>0.03 (+11.20%)</td><td>0.01 <b>(-35.44%)</b></td><td>565.70 (-10.06%)</td><td>484.80 (-6.09%)</td><td>455.10 (-14.57%)</td><td>396.20 (+6.76%)</td><td>71.94 <b>(-37.86%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>629.00 (n/a)</td><td>516.22 (n/a)</td><td>532.70 (n/a)</td><td>371.10 (n/a)</td><td>115.76 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (+2.33%)</td><td>0.13 <b>(+85.02%)</b></td><td>0.12 <b>(+105.93%)</b></td><td>0.11 <b>(+566.87%)</b></td><td>0.01 <b>(-73.71%)</b></td><td>292.20 <b>(-85.00%)</b></td><td>261.36 <b>(-65.50%)</b></td><td>266.90 <b>(-51.45%)</b></td><td>228.30 (-2.27%)</td><td>23.77 <b>(-96.50%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1948.50 (n/a)</td><td>757.56 (n/a)</td><td>549.70 (n/a)</td><td>233.60 (n/a)</td><td>678.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (+6.02%)</td><td>0.11 (-8.61%)</td><td>0.10 (-15.55%)</td><td>0.08 (-15.74%)</td><td>0.02 <b>(+103.06%)</b></td><td>393.00 (+18.66%)</td><td>317.18 (+12.36%)</td><td>327.30 (+18.42%)</td><td>239.60 (-5.67%)</td><td>63.99 <b>(+120.37%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>331.20 (n/a)</td><td>282.30 (n/a)</td><td>276.40 (n/a)</td><td>254.00 (n/a)</td><td>29.04 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.16 <b>(+43.16%)</b></td><td>0.11 <b>(+40.55%)</b></td><td>0.13 <b>(+77.78%)</b></td><td>0.06 (-10.23%)</td><td>0.04 <b>(+136.55%)</b></td><td>587.90 (+11.41%)</td><td>354.80 (-19.45%)</td><td>261.10 <b>(-43.75%)</b></td><td>209.70 <b>(-30.15%)</b></td><td>167.27 <b>(+94.15%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>527.70 (n/a)</td><td>440.46 (n/a)</td><td>464.20 (n/a)</td><td>300.20 (n/a)</td><td>86.16 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 <b>(+28.90%)</b></td><td>0.12 <b>(+28.21%)</b></td><td>0.13 <b>(+21.99%)</b></td><td>0.06 (+0.22%)</td><td>0.04 <b>(+32.68%)</b></td><td>557.80 (-0.21%)</td><td>303.30 (-19.00%)</td><td>243.00 (-18.02%)</td><td>213.00 <b>(-22.40%)</b></td><td>143.56 (+12.54%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>559.00 (n/a)</td><td>374.46 (n/a)</td><td>296.40 (n/a)</td><td>274.50 (n/a)</td><td>127.57 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 (-18.89%)</td><td>0.11 (+14.08%)</td><td>0.09 <b>(+20.76%)</b></td><td>0.09 <b>(+88.27%)</b></td><td>0.02 <b>(-54.92%)</b></td><td>359.80 <b>(-46.88%)</b></td><td>314.70 <b>(-25.42%)</b></td><td>352.20 (-17.19%)</td><td>248.90 <b>(+23.28%)</b></td><td>58.02 <b>(-69.95%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>677.30 (n/a)</td><td>421.96 (n/a)</td><td>425.30 (n/a)</td><td>201.90 (n/a)</td><td>193.10 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (-0.39%)</td><td>0.09 (+6.69%)</td><td>0.10 (-6.54%)</td><td>0.05 <b>(+191.23%)</b></td><td>0.04 <b>(-22.53%)</b></td><td>654.70 <b>(-65.66%)</b></td><td>403.54 <b>(-37.97%)</b></td><td>337.10 (+6.98%)</td><td>240.80 (+0.38%)</td><td>177.52 <b>(-75.00%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1906.60 (n/a)</td><td>650.60 (n/a)</td><td>315.10 (n/a)</td><td>239.90 (n/a)</td><td>710.16 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (+16.74%)</td><td>0.12 (+14.81%)</td><td>0.11 (-2.31%)</td><td>0.08 <b>(+160.81%)</b></td><td>0.03 <b>(-28.75%)</b></td><td>428.20 <b>(-61.66%)</b></td><td>296.50 <b>(-33.00%)</b></td><td>287.50 (+2.39%)</td><td>214.90 (-14.31%)</td><td>82.91 <b>(-78.02%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1116.80 (n/a)</td><td>442.56 (n/a)</td><td>280.80 (n/a)</td><td>250.80 (n/a)</td><td>377.21 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (-13.96%)</td><td>0.09 (-2.19%)</td><td>0.10 (-15.67%)</td><td>0.06 <b>(+329.48%)</b></td><td>0.03 <b>(-42.40%)</b></td><td>586.70 <b>(-76.72%)</b></td><td>402.98 <b>(-46.82%)</b></td><td>342.20 (+18.57%)</td><td>263.00 (+16.22%)</td><td>144.44 <b>(-85.41%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2519.80 (n/a)</td><td>757.74 (n/a)</td><td>288.60 (n/a)</td><td>226.30 (n/a)</td><td>989.71 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 <b>(-20.32%)</b></td><td>0.09 (-17.14%)</td><td>0.07 <b>(-35.51%)</b></td><td>0.07 <b>(+21.60%)</b></td><td>0.03 <b>(-37.14%)</b></td><td>466.50 (-17.75%)</td><td>380.12 (+10.66%)</td><td>444.30 <b>(+55.08%)</b></td><td>243.00 <b>(+25.52%)</b></td><td>102.91 <b>(-34.08%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>567.20 (n/a)</td><td>343.50 (n/a)</td><td>286.50 (n/a)</td><td>193.60 (n/a)</td><td>156.12 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (-11.92%)</td><td>0.07 <b>(-31.89%)</b></td><td>0.06 <b>(-49.23%)</b></td><td>0.04 <b>(-27.76%)</b></td><td>0.03 <b>(-22.93%)</b></td><td>763.80 <b>(+38.42%)</b></td><td>531.42 <b>(+44.11%)</b></td><td>525.90 <b>(+96.97%)</b></td><td>287.20 (+13.52%)</td><td>169.05 (+14.22%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>551.80 (n/a)</td><td>368.76 (n/a)</td><td>267.00 (n/a)</td><td>253.00 (n/a)</td><td>148.00 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 <b>(-20.15%)</b></td><td>0.07 <b>(-25.38%)</b></td><td>0.06 <b>(-25.82%)</b></td><td>0.05 <b>(-29.30%)</b></td><td>0.03 (-10.12%)</td><td>654.70 <b>(+41.43%)</b></td><td>509.84 <b>(+37.85%)</b></td><td>568.20 <b>(+34.84%)</b></td><td>306.20 <b>(+25.24%)</b></td><td>159.70 <b>(+62.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>462.90 (n/a)</td><td>369.86 (n/a)</td><td>421.40 (n/a)</td><td>244.50 (n/a)</td><td>98.19 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (+2.14%)</td><td>0.08 (-8.20%)</td><td>0.08 (-19.27%)</td><td>0.05 (-5.45%)</td><td>0.03 (-8.11%)</td><td>666.80 (+5.77%)</td><td>426.20 (+7.69%)</td><td>407.10 <b>(+23.85%)</b></td><td>264.80 (-2.11%)</td><td>153.59 (-0.85%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>630.40 (n/a)</td><td>395.78 (n/a)</td><td>328.70 (n/a)</td><td>270.50 (n/a)</td><td>154.91 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (-15.64%)</td><td>0.01 (+9.69%)</td><td>0.01 <b>(+62.16%)</b></td><td>0.00 <b>(-62.02%)</b></td><td>0.01 (+8.03%)</td><td>1956.80 <b>(+163.33%)</b></td><td>632.02 <b>(+34.19%)</b></td><td>295.60 <b>(-38.33%)</b></td><td>289.60 (+18.54%)</td><td>740.72 <b>(+256.76%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>743.10 (n/a)</td><td>470.98 (n/a)</td><td>479.30 (n/a)</td><td>244.30 (n/a)</td><td>207.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 <b>(-39.97%)</b></td><td>0.01 <b>(-43.91%)</b></td><td>0.01 <b>(-58.76%)</b></td><td>0.00 (-6.88%)</td><td>0.00 <b>(-53.80%)</b></td><td>2117.00 (+7.39%)</td><td>872.30 <b>(+32.23%)</b></td><td>649.10 <b>(+142.47%)</b></td><td>405.00 <b>(+66.60%)</b></td><td>705.80 (-5.40%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1971.30 (n/a)</td><td>659.70 (n/a)</td><td>267.70 (n/a)</td><td>243.10 (n/a)</td><td>746.06 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 <b>(+22.45%)</b></td><td>0.01 (-3.11%)</td><td>0.01 (+5.78%)</td><td>0.01 (+1.60%)</td><td>0.01 <b>(+20.21%)</b></td><td>600.50 (-1.57%)</td><td>482.12 (+4.43%)</td><td>536.90 (-5.46%)</td><td>207.90 (-18.31%)</td><td>161.58 (-8.27%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.10 (n/a)</td><td>461.66 (n/a)</td><td>567.90 (n/a)</td><td>254.50 (n/a)</td><td>176.16 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 <b>(-21.18%)</b></td><td>0.02 (+8.69%)</td><td>0.02 (+18.81%)</td><td>0.01 <b>(+450.95%)</b></td><td>0.00 <b>(-66.33%)</b></td><td>450.10 <b>(-81.85%)</b></td><td>347.30 <b>(-53.60%)</b></td><td>307.20 (-15.84%)</td><td>301.70 <b>(+26.87%)</b></td><td>65.08 <b>(-93.29%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2479.60 (n/a)</td><td>748.52 (n/a)</td><td>365.00 (n/a)</td><td>237.80 (n/a)</td><td>969.64 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 (+4.31%)</td><td>0.01 (-2.93%)</td><td>0.01 (-9.02%)</td><td>0.01 (+8.10%)</td><td>0.00 (+15.46%)</td><td>572.70 (-7.49%)</td><td>420.86 (+4.87%)</td><td>394.20 (+9.90%)</td><td>277.10 (-4.15%)</td><td>144.24 (+6.09%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.10 (n/a)</td><td>401.30 (n/a)</td><td>358.70 (n/a)</td><td>289.10 (n/a)</td><td>135.96 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (-16.98%)</td><td>0.01 <b>(-25.33%)</b></td><td>0.01 <b>(-40.71%)</b></td><td>0.01 (+12.90%)</td><td>0.01 <b>(-27.31%)</b></td><td>522.60 (-11.42%)</td><td>452.04 <b>(+24.33%)</b></td><td>515.70 <b>(+68.69%)</b></td><td>228.70 <b>(+20.43%)</b></td><td>126.33 <b>(-25.89%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.00 (n/a)</td><td>363.58 (n/a)</td><td>305.70 (n/a)</td><td>189.90 (n/a)</td><td>170.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (+11.49%)</td><td>0.01 (+1.12%)</td><td>0.01 (+10.73%)</td><td>0.01 <b>(-36.70%)</b></td><td>0.01 <b>(+141.44%)</b></td><td>766.00 <b>(+57.97%)</b></td><td>450.68 (+17.84%)</td><td>337.00 (-9.68%)</td><td>258.40 (-10.31%)</td><td>234.35 <b>(+233.18%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>484.90 (n/a)</td><td>382.46 (n/a)</td><td>373.10 (n/a)</td><td>288.10 (n/a)</td><td>70.34 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.01 <b>(-30.08%)</b></td><td>0.01 <b>(-21.29%)</b></td><td>0.01 <b>(-22.54%)</b></td><td>0.01 <b>(-25.62%)</b></td><td>0.00 <b>(-38.46%)</b></td><td>684.80 <b>(+34.46%)</b></td><td>518.92 <b>(+24.45%)</b></td><td>542.00 <b>(+29.11%)</b></td><td>339.50 <b>(+43.01%)</b></td><td>130.09 (+18.44%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.30 (n/a)</td><td>416.98 (n/a)</td><td>419.80 (n/a)</td><td>237.40 (n/a)</td><td>109.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (+14.53%)</td><td>0.01 (+3.42%)</td><td>0.01 (-5.53%)</td><td>0.01 (-9.37%)</td><td>0.00 <b>(+27.64%)</b></td><td>657.40 (+10.34%)</td><td>395.28 (+1.78%)</td><td>312.00 (+5.83%)</td><td>244.00 (-12.70%)</td><td>179.63 <b>(+24.94%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>595.80 (n/a)</td><td>388.36 (n/a)</td><td>294.80 (n/a)</td><td>279.50 (n/a)</td><td>143.77 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (+11.54%)</td><td>0.02 <b>(+28.02%)</b></td><td>0.01 <b>(+37.91%)</b></td><td>0.01 (+17.02%)</td><td>0.00 (-3.58%)</td><td>440.70 (-14.56%)</td><td>322.78 <b>(-23.96%)</b></td><td>316.70 <b>(-27.50%)</b></td><td>201.60 (-10.36%)</td><td>87.88 <b>(-25.41%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.80 (n/a)</td><td>424.46 (n/a)</td><td>436.80 (n/a)</td><td>224.90 (n/a)</td><td>117.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 (+5.29%)</td><td>0.01 (-14.16%)</td><td>0.01 <b>(-23.56%)</b></td><td>0.01 <b>(-34.73%)</b></td><td>0.00 <b>(+91.60%)</b></td><td>666.50 <b>(+53.22%)</b></td><td>437.48 <b>(+27.61%)</b></td><td>447.90 <b>(+30.81%)</b></td><td>261.70 (-5.01%)</td><td>163.15 <b>(+169.22%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>435.00 (n/a)</td><td>342.82 (n/a)</td><td>342.40 (n/a)</td><td>275.50 (n/a)</td><td>60.60 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.04 (-9.37%)</td><td>0.02 <b>(-38.00%)</b></td><td>0.02 <b>(-44.05%)</b></td><td>0.00 <b>(-81.88%)</b></td><td>0.02 <b>(+145.96%)</b></td><td>1916.00 <b>(+451.68%)</b></td><td>935.50 <b>(+258.37%)</b></td><td>440.10 <b>(+78.76%)</b></td><td>216.20 (+10.31%)</td><td>880.90 <b>(+1483.25%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>347.30 (n/a)</td><td>261.04 (n/a)</td><td>246.20 (n/a)</td><td>196.00 (n/a)</td><td>55.64 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (+17.12%)</td><td>0.04 (-9.22%)</td><td>0.03 <b>(-40.93%)</b></td><td>0.03 (+12.83%)</td><td>0.02 <b>(+21.78%)</b></td><td>487.60 (-11.38%)</td><td>358.94 (+11.62%)</td><td>418.70 <b>(+69.31%)</b></td><td>198.60 (-14.65%)</td><td>124.93 (-7.27%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>550.20 (n/a)</td><td>321.56 (n/a)</td><td>247.30 (n/a)</td><td>232.70 (n/a)</td><td>134.72 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (-14.95%)</td><td>0.02 (-10.76%)</td><td>0.03 (-5.81%)</td><td>0.01 (-4.32%)</td><td>0.01 (-18.03%)</td><td>622.80 (+4.51%)</td><td>406.30 (+8.63%)</td><td>282.60 (+6.16%)</td><td>237.00 (+17.62%)</td><td>192.73 (+0.71%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.90 (n/a)</td><td>374.02 (n/a)</td><td>266.20 (n/a)</td><td>201.50 (n/a)</td><td>191.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 (-19.93%)</td><td>0.03 (-19.08%)</td><td>0.02 (+3.21%)</td><td>0.02 (-3.31%)</td><td>0.01 <b>(-33.52%)</b></td><td>532.60 (+3.44%)</td><td>426.08 (+14.82%)</td><td>429.00 (-3.12%)</td><td>227.20 <b>(+24.90%)</b></td><td>122.73 (-17.88%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>514.90 (n/a)</td><td>371.08 (n/a)</td><td>442.80 (n/a)</td><td>181.90 (n/a)</td><td>149.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (-10.64%)</td><td>0.02 (+7.73%)</td><td>0.02 (+5.77%)</td><td>0.01 <b>(+44.29%)</b></td><td>0.01 <b>(-27.29%)</b></td><td>703.30 <b>(-30.70%)</b></td><td>469.48 (-17.63%)</td><td>499.00 (-5.46%)</td><td>266.40 (+11.93%)</td><td>163.21 <b>(-43.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1014.80 (n/a)</td><td>569.96 (n/a)</td><td>527.80 (n/a)</td><td>238.00 (n/a)</td><td>289.58 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 <b>(-24.81%)</b></td><td>0.02 <b>(-34.68%)</b></td><td>0.02 <b>(-33.02%)</b></td><td>0.01 <b>(-53.17%)</b></td><td>0.01 (+12.90%)</td><td>1052.00 <b>(+113.52%)</b></td><td>597.94 <b>(+67.13%)</b></td><td>480.30 <b>(+49.30%)</b></td><td>377.00 <b>(+32.98%)</b></td><td>267.97 <b>(+228.21%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.70 (n/a)</td><td>357.76 (n/a)</td><td>321.70 (n/a)</td><td>283.50 (n/a)</td><td>81.64 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.02 <b>(-33.63%)</b></td><td>0.02 <b>(-32.53%)</b></td><td>0.02 <b>(-41.08%)</b></td><td>0.02 (+1.11%)</td><td>0.00 <b>(-62.17%)</b></td><td>532.70 (-1.10%)</td><td>454.96 <b>(+38.10%)</b></td><td>462.30 <b>(+69.71%)</b></td><td>351.00 <b>(+50.71%)</b></td><td>66.29 <b>(-46.70%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.60 (n/a)</td><td>329.44 (n/a)</td><td>272.40 (n/a)</td><td>232.90 (n/a)</td><td>124.37 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 <b>(+64.61%)</b></td><td>0.03 (-15.99%)</td><td>0.02 <b>(-38.43%)</b></td><td>0.01 <b>(-36.74%)</b></td><td>0.02 <b>(+202.18%)</b></td><td>672.40 <b>(+58.06%)</b></td><td>469.08 <b>(+53.83%)</b></td><td>467.90 <b>(+62.41%)</b></td><td>145.00 <b>(-39.25%)</b></td><td>205.12 <b>(+170.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>425.40 (n/a)</td><td>304.94 (n/a)</td><td>288.10 (n/a)</td><td>238.70 (n/a)</td><td>75.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (-12.94%)</td><td>0.02 <b>(-28.91%)</b></td><td>0.02 <b>(-43.68%)</b></td><td>0.00 (-2.87%)</td><td>0.01 <b>(-27.91%)</b></td><td>1893.60 (+2.95%)</td><td>702.70 (+18.29%)</td><td>444.60 <b>(+77.56%)</b></td><td>263.00 (+14.85%)</td><td>672.28 (-4.01%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1839.30 (n/a)</td><td>594.06 (n/a)</td><td>250.40 (n/a)</td><td>229.00 (n/a)</td><td>700.35 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 (-10.41%)</td><td>0.02 (-8.44%)</td><td>0.02 (-5.97%)</td><td>0.02 <b>(-23.57%)</b></td><td>0.00 (+1.71%)</td><td>608.00 <b>(+30.84%)</b></td><td>441.10 (+10.86%)</td><td>427.60 (+6.34%)</td><td>322.20 (+11.64%)</td><td>105.21 <b>(+55.19%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>464.70 (n/a)</td><td>397.90 (n/a)</td><td>402.10 (n/a)</td><td>288.60 (n/a)</td><td>67.80 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.03 <b>(-30.09%)</b></td><td>0.02 <b>(-31.67%)</b></td><td>0.02 <b>(-32.91%)</b></td><td>0.00 <b>(-68.15%)</b></td><td>0.01 (-15.67%)</td><td>1896.70 <b>(+214.02%)</b></td><td>725.16 <b>(+88.90%)</b></td><td>452.40 <b>(+49.06%)</b></td><td>320.70 <b>(+43.04%)</b></td><td>665.86 <b>(+279.57%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.00 (n/a)</td><td>383.88 (n/a)</td><td>303.50 (n/a)</td><td>224.20 (n/a)</td><td>175.43 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (-5.12%)</td><td>0.05 (+0.02%)</td><td>0.05 (+0.62%)</td><td>0.03 (+18.18%)</td><td>0.02 <b>(-23.22%)</b></td><td>506.30 (-15.39%)</td><td>350.36 (-7.83%)</td><td>305.20 (-0.62%)</td><td>214.90 (+5.39%)</td><td>118.41 <b>(-33.27%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>598.40 (n/a)</td><td>380.12 (n/a)</td><td>307.10 (n/a)</td><td>203.90 (n/a)</td><td>177.43 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (-4.16%)</td><td>0.04 <b>(-50.25%)</b></td><td>0.04 <b>(-58.56%)</b></td><td>0.01 <b>(-85.52%)</b></td><td>0.04 <b>(+174.97%)</b></td><td>2502.50 <b>(+590.54%)</b></td><td>1141.50 <b>(+303.10%)</b></td><td>632.70 <b>(+141.30%)</b></td><td>253.10 (+4.33%)</td><td>1007.73 <b>(+1996.21%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>362.40 (n/a)</td><td>283.18 (n/a)</td><td>262.20 (n/a)</td><td>242.60 (n/a)</td><td>48.07 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (-17.22%)</td><td>0.04 <b>(-25.31%)</b></td><td>0.03 <b>(-48.97%)</b></td><td>0.03 <b>(-21.00%)</b></td><td>0.02 (+4.68%)</td><td>535.50 <b>(+26.57%)</b></td><td>427.38 <b>(+38.90%)</b></td><td>520.90 <b>(+95.97%)</b></td><td>276.90 <b>(+20.81%)</b></td><td>135.22 <b>(+57.62%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>423.10 (n/a)</td><td>307.70 (n/a)</td><td>265.80 (n/a)</td><td>229.20 (n/a)</td><td>85.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (-18.70%)</td><td>0.05 (-14.93%)</td><td>0.05 (-19.46%)</td><td>0.05 (+14.77%)</td><td>0.01 <b>(-59.92%)</b></td><td>438.90 (-12.88%)</td><td>387.86 (+8.60%)</td><td>387.60 <b>(+24.15%)</b></td><td>302.10 <b>(+23.00%)</b></td><td>52.94 <b>(-57.74%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>503.80 (n/a)</td><td>357.14 (n/a)</td><td>312.20 (n/a)</td><td>245.60 (n/a)</td><td>125.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 (-12.73%)</td><td>0.04 <b>(-28.74%)</b></td><td>0.03 <b>(-43.75%)</b></td><td>0.03 (-18.65%)</td><td>0.01 (-10.85%)</td><td>559.40 <b>(+22.92%)</b></td><td>478.98 <b>(+40.67%)</b></td><td>510.80 <b>(+77.79%)</b></td><td>282.60 (+14.55%)</td><td>113.35 (+16.84%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>455.10 (n/a)</td><td>340.50 (n/a)</td><td>287.30 (n/a)</td><td>246.70 (n/a)</td><td>97.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (-2.33%)</td><td>0.04 <b>(-35.81%)</b></td><td>0.04 <b>(-51.88%)</b></td><td>0.01 <b>(-72.17%)</b></td><td>0.03 <b>(+23.07%)</b></td><td>1967.40 <b>(+259.28%)</b></td><td>769.00 <b>(+119.93%)</b></td><td>576.30 <b>(+107.83%)</b></td><td>234.40 (+2.40%)</td><td>684.94 <b>(+390.61%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>547.60 (n/a)</td><td>349.66 (n/a)</td><td>277.30 (n/a)</td><td>228.90 (n/a)</td><td>139.61 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (+7.83%)</td><td>0.05 (+4.02%)</td><td>0.03 (-16.73%)</td><td>0.03 (-8.69%)</td><td>0.02 <b>(+48.23%)</b></td><td>599.90 (+9.53%)</td><td>405.90 (+4.55%)</td><td>473.90 <b>(+20.10%)</b></td><td>225.90 (-7.27%)</td><td>169.21 <b>(+39.90%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>547.70 (n/a)</td><td>388.24 (n/a)</td><td>394.60 (n/a)</td><td>243.60 (n/a)</td><td>120.95 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.06 <b>(-22.93%)</b></td><td>0.04 (-14.00%)</td><td>0.04 (+1.12%)</td><td>0.01 <b>(-53.08%)</b></td><td>0.02 (-14.07%)</td><td>1354.30 <b>(+113.14%)</b></td><td>632.36 <b>(+31.57%)</b></td><td>488.70 (-1.11%)</td><td>321.00 <b>(+29.75%)</b></td><td>411.30 <b>(+188.37%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>635.40 (n/a)</td><td>480.64 (n/a)</td><td>494.20 (n/a)</td><td>247.40 (n/a)</td><td>142.63 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (+14.85%)</td><td>0.06 <b>(+40.16%)</b></td><td>0.06 <b>(+57.92%)</b></td><td>0.03 <b>(+295.76%)</b></td><td>0.02 <b>(-37.75%)</b></td><td>494.30 <b>(-74.73%)</b></td><td>301.74 <b>(-56.91%)</b></td><td>275.00 <b>(-36.68%)</b></td><td>204.20 (-12.92%)</td><td>111.57 <b>(-84.54%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1956.10 (n/a)</td><td>700.22 (n/a)</td><td>434.30 (n/a)</td><td>234.50 (n/a)</td><td>721.74 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (+5.18%)</td><td>0.05 (-11.31%)</td><td>0.04 <b>(-31.97%)</b></td><td>0.03 (-13.98%)</td><td>0.02 <b>(+25.20%)</b></td><td>570.90 (+16.25%)</td><td>416.08 (+16.76%)</td><td>464.50 <b>(+46.99%)</b></td><td>242.40 (-4.90%)</td><td>129.23 <b>(+32.93%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>491.10 (n/a)</td><td>356.34 (n/a)</td><td>316.00 (n/a)</td><td>254.90 (n/a)</td><td>97.21 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 <b>(-31.53%)</b></td><td>0.04 (-14.22%)</td><td>0.04 (-12.05%)</td><td>0.03 (-18.54%)</td><td>0.01 <b>(-38.04%)</b></td><td>633.60 <b>(+22.77%)</b></td><td>450.94 (+13.54%)</td><td>421.70 (+13.70%)</td><td>335.00 <b>(+46.03%)</b></td><td>125.69 (+7.67%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>516.10 (n/a)</td><td>397.18 (n/a)</td><td>370.90 (n/a)</td><td>229.40 (n/a)</td><td>116.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (+11.52%)</td><td>0.10 (+4.67%)</td><td>0.08 (-16.35%)</td><td>0.07 (+10.73%)</td><td>0.03 (+6.55%)</td><td>471.20 (-9.68%)</td><td>366.60 (-5.45%)</td><td>400.80 (+19.53%)</td><td>233.10 (-10.31%)</td><td>92.68 (-19.98%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>521.70 (n/a)</td><td>387.72 (n/a)</td><td>335.30 (n/a)</td><td>259.90 (n/a)</td><td>115.81 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (+14.45%)</td><td>0.09 (+8.92%)</td><td>0.08 (+17.19%)</td><td>0.06 (+6.80%)</td><td>0.03 (-0.26%)</td><td>541.50 (-6.38%)</td><td>382.42 (-9.68%)</td><td>395.50 (-14.67%)</td><td>238.10 (-12.66%)</td><td>121.63 (-14.90%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>578.40 (n/a)</td><td>423.42 (n/a)</td><td>463.50 (n/a)</td><td>272.60 (n/a)</td><td>142.92 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.25 <b>(+72.52%)</b></td><td>0.12 <b>(+26.22%)</b></td><td>0.09 (+18.26%)</td><td>0.06 <b>(+26.26%)</b></td><td>0.08 <b>(+80.90%)</b></td><td>672.30 <b>(-20.79%)</b></td><td>441.22 (-16.27%)</td><td>451.30 (-15.42%)</td><td>162.40 <b>(-42.04%)</b></td><td>183.85 <b>(-22.21%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>848.80 (n/a)</td><td>526.98 (n/a)</td><td>533.60 (n/a)</td><td>280.20 (n/a)</td><td>236.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 (-9.00%)</td><td>0.08 (+5.96%)</td><td>0.07 (+3.91%)</td><td>0.05 (-7.48%)</td><td>0.02 (+3.36%)</td><td>649.00 (+8.08%)</td><td>450.96 (-4.13%)</td><td>479.10 (-3.76%)</td><td>311.20 (+9.89%)</td><td>142.51 <b>(+20.65%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>600.50 (n/a)</td><td>470.40 (n/a)</td><td>497.80 (n/a)</td><td>283.20 (n/a)</td><td>118.11 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 <b>(-20.40%)</b></td><td>0.08 (-19.89%)</td><td>0.09 (-7.40%)</td><td>0.04 <b>(-49.14%)</b></td><td>0.03 (+19.43%)</td><td>1073.60 <b>(+96.63%)</b></td><td>584.88 <b>(+37.51%)</b></td><td>479.70 (+7.99%)</td><td>383.50 <b>(+25.66%)</b></td><td>283.42 <b>(+208.84%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>546.00 (n/a)</td><td>425.34 (n/a)</td><td>444.20 (n/a)</td><td>305.20 (n/a)</td><td>91.77 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (+14.42%)</td><td>0.10 (+18.23%)</td><td>0.07 (-7.38%)</td><td>0.06 (+16.50%)</td><td>0.04 <b>(+49.20%)</b></td><td>543.40 (-14.17%)</td><td>394.22 (-10.25%)</td><td>473.60 (+7.98%)</td><td>224.00 (-12.57%)</td><td>150.46 (+12.75%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>633.10 (n/a)</td><td>439.22 (n/a)</td><td>438.60 (n/a)</td><td>256.20 (n/a)</td><td>133.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.16 <b>(+36.38%)</b></td><td>0.09 (+4.29%)</td><td>0.08 (+5.69%)</td><td>0.03 <b>(-45.51%)</b></td><td>0.04 <b>(+94.78%)</b></td><td>1093.20 <b>(+83.52%)</b></td><td>545.94 (+14.71%)</td><td>468.90 (-5.39%)</td><td>234.20 <b>(-26.68%)</b></td><td>322.46 <b>(+166.40%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>595.70 (n/a)</td><td>475.92 (n/a)</td><td>495.60 (n/a)</td><td>319.40 (n/a)</td><td>121.04 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (+12.30%)</td><td>0.09 <b>(+21.97%)</b></td><td>0.10 <b>(+41.91%)</b></td><td>0.05 <b>(+221.36%)</b></td><td>0.04 (-8.56%)</td><td>598.60 <b>(-68.88%)</b></td><td>403.06 <b>(-41.76%)</b></td><td>317.60 <b>(-29.53%)</b></td><td>219.80 (-10.98%)</td><td>174.96 <b>(-74.89%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1923.60 (n/a)</td><td>692.10 (n/a)</td><td>450.70 (n/a)</td><td>246.90 (n/a)</td><td>696.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.16 <b>(+26.27%)</b></td><td>0.11 (+15.92%)</td><td>0.09 (+13.47%)</td><td>0.07 (-7.13%)</td><td>0.04 <b>(+92.18%)</b></td><td>494.60 (+7.66%)</td><td>379.20 (-8.64%)</td><td>389.20 (-11.87%)</td><td>236.00 <b>(-20.83%)</b></td><td>116.02 <b>(+71.52%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>459.40 (n/a)</td><td>415.06 (n/a)</td><td>441.60 (n/a)</td><td>298.10 (n/a)</td><td>67.64 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.11 <b>(+45.44%)</b></td><td>0.07 (+5.07%)</td><td>0.06 (-6.53%)</td><td>0.05 (-4.53%)</td><td>0.02 <b>(+273.42%)</b></td><td>600.00 (+4.75%)</td><td>518.92 (+0.68%)</td><td>554.60 (+6.98%)</td><td>307.60 <b>(-31.23%)</b></td><td>120.67 <b>(+163.32%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>572.80 (n/a)</td><td>515.40 (n/a)</td><td>518.40 (n/a)</td><td>447.30 (n/a)</td><td>45.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (-2.78%)</td><td>0.05 <b>(-24.80%)</b></td><td>0.05 <b>(-36.80%)</b></td><td>0.02 <b>(-63.03%)</b></td><td>0.03 <b>(+91.56%)</b></td><td>1090.50 <b>(+170.46%)</b></td><td>503.30 <b>(+69.64%)</b></td><td>438.60 <b>(+58.23%)</b></td><td>251.50 (+2.86%)</td><td>343.57 <b>(+423.52%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>403.20 (n/a)</td><td>296.68 (n/a)</td><td>277.20 (n/a)</td><td>244.50 (n/a)</td><td>65.63 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (+3.62%)</td><td>0.07 (+4.93%)</td><td>0.08 (+12.29%)</td><td>0.04 (-13.54%)</td><td>0.02 <b>(+30.42%)</b></td><td>581.80 (+15.67%)</td><td>321.70 (+0.12%)</td><td>254.20 (-10.93%)</td><td>243.10 (-3.49%)</td><td>146.14 <b>(+42.15%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>503.00 (n/a)</td><td>321.30 (n/a)</td><td>285.40 (n/a)</td><td>251.90 (n/a)</td><td>102.81 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (+5.96%)</td><td>0.05 (+4.48%)</td><td>0.05 (+16.12%)</td><td>0.01 <b>(-69.19%)</b></td><td>0.03 <b>(+36.03%)</b></td><td>1973.00 <b>(+224.56%)</b></td><td>692.02 <b>(+45.01%)</b></td><td>436.70 (-13.88%)</td><td>225.00 (-5.62%)</td><td>723.18 <b>(+396.80%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>607.90 (n/a)</td><td>477.22 (n/a)</td><td>507.10 (n/a)</td><td>238.40 (n/a)</td><td>145.57 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (-7.06%)</td><td>0.06 (+9.10%)</td><td>0.06 (+11.86%)</td><td>0.05 <b>(+74.39%)</b></td><td>0.01 <b>(-48.04%)</b></td><td>454.50 <b>(-42.66%)</b></td><td>331.40 <b>(-22.33%)</b></td><td>323.10 (-10.60%)</td><td>244.10 (+7.58%)</td><td>77.31 <b>(-66.57%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>792.60 (n/a)</td><td>426.70 (n/a)</td><td>361.40 (n/a)</td><td>226.90 (n/a)</td><td>231.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (+13.39%)</td><td>0.05 <b>(-25.24%)</b></td><td>0.05 <b>(-44.14%)</b></td><td>0.04 (-4.90%)</td><td>0.02 <b>(+23.75%)</b></td><td>562.90 (+5.16%)</td><td>430.66 <b>(+37.23%)</b></td><td>443.60 <b>(+79.02%)</b></td><td>213.50 (-11.78%)</td><td>134.08 (+6.56%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>535.30 (n/a)</td><td>313.82 (n/a)</td><td>247.80 (n/a)</td><td>242.00 (n/a)</td><td>125.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (+4.72%)</td><td>0.06 (+0.04%)</td><td>0.05 (-5.95%)</td><td>0.03 (-10.30%)</td><td>0.03 <b>(+26.43%)</b></td><td>606.30 (+11.47%)</td><td>398.74 (+5.46%)</td><td>430.50 (+6.32%)</td><td>233.00 (-4.51%)</td><td>160.84 <b>(+29.89%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>543.90 (n/a)</td><td>378.10 (n/a)</td><td>404.90 (n/a)</td><td>244.00 (n/a)</td><td>123.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (-16.85%)</td><td>0.08 (+8.26%)</td><td>0.09 <b>(+49.53%)</b></td><td>0.04 (-0.48%)</td><td>0.03 <b>(-31.01%)</b></td><td>618.40 (+0.49%)</td><td>338.16 (-12.92%)</td><td>287.80 <b>(-33.13%)</b></td><td>234.20 <b>(+20.29%)</b></td><td>158.71 (-7.42%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>615.40 (n/a)</td><td>388.34 (n/a)</td><td>430.40 (n/a)</td><td>194.70 (n/a)</td><td>171.44 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 (+0.41%)</td><td>0.08 (+11.94%)</td><td>0.08 (+5.07%)</td><td>0.05 (+15.86%)</td><td>0.02 <b>(-26.36%)</b></td><td>454.70 (-13.69%)</td><td>321.22 (-14.09%)</td><td>297.20 (-4.84%)</td><td>260.50 (-0.42%)</td><td>76.74 <b>(-35.28%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>526.80 (n/a)</td><td>373.90 (n/a)</td><td>312.30 (n/a)</td><td>261.60 (n/a)</td><td>118.58 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (+9.54%)</td><td>0.07 (-5.02%)</td><td>0.07 (+7.50%)</td><td>0.04 <b>(-25.58%)</b></td><td>0.02 <b>(+70.51%)</b></td><td>598.40 <b>(+34.35%)</b></td><td>393.00 (+13.80%)</td><td>332.70 (-6.99%)</td><td>243.00 (-8.72%)</td><td>148.39 <b>(+115.35%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>445.40 (n/a)</td><td>345.34 (n/a)</td><td>357.70 (n/a)</td><td>266.20 (n/a)</td><td>68.90 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (+0.31%)</td><td>0.06 (+4.15%)</td><td>0.05 (-12.10%)</td><td>0.04 (+0.90%)</td><td>0.03 <b>(+24.58%)</b></td><td>682.70 (-0.89%)</td><td>465.18 (+1.48%)</td><td>536.60 (+13.78%)</td><td>252.60 (-0.32%)</td><td>198.18 (+16.46%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>688.80 (n/a)</td><td>458.40 (n/a)</td><td>471.60 (n/a)</td><td>253.40 (n/a)</td><td>170.17 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (-3.68%)</td><td>0.07 (-6.79%)</td><td>0.06 <b>(-23.57%)</b></td><td>0.05 (+9.23%)</td><td>0.02 (-16.07%)</td><td>466.60 (-8.46%)</td><td>368.88 (+4.41%)</td><td>409.40 <b>(+30.84%)</b></td><td>250.20 (+3.82%)</td><td>92.30 <b>(-20.98%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>509.70 (n/a)</td><td>353.30 (n/a)</td><td>312.90 (n/a)</td><td>241.00 (n/a)</td><td>116.80 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.10 (-1.05%)</td><td>0.07 (-14.88%)</td><td>0.06 <b>(-29.95%)</b></td><td>0.05 (-13.60%)</td><td>0.02 (-1.02%)</td><td>526.50 (+15.74%)</td><td>399.38 (+17.92%)</td><td>416.80 <b>(+42.79%)</b></td><td>255.40 (+1.07%)</td><td>100.96 (+10.19%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>454.90 (n/a)</td><td>338.68 (n/a)</td><td>291.90 (n/a)</td><td>252.70 (n/a)</td><td>91.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (-6.27%)</td><td>0.04 <b>(-25.28%)</b></td><td>0.03 <b>(-25.21%)</b></td><td>0.02 <b>(-28.24%)</b></td><td>0.02 (-7.69%)</td><td>807.30 <b>(+39.36%)</b></td><td>528.60 <b>(+37.49%)</b></td><td>538.60 <b>(+33.71%)</b></td><td>252.60 (+6.72%)</td><td>204.51 <b>(+40.28%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>579.30 (n/a)</td><td>384.46 (n/a)</td><td>402.80 (n/a)</td><td>236.70 (n/a)</td><td>145.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (+0.25%)</td><td>0.04 <b>(-28.83%)</b></td><td>0.03 <b>(-46.40%)</b></td><td>0.03 <b>(-33.61%)</b></td><td>0.02 <b>(+69.73%)</b></td><td>631.00 <b>(+50.63%)</b></td><td>470.80 <b>(+53.52%)</b></td><td>538.80 <b>(+86.57%)</b></td><td>245.80 (-0.24%)</td><td>158.34 <b>(+141.54%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>418.90 (n/a)</td><td>306.68 (n/a)</td><td>288.80 (n/a)</td><td>246.40 (n/a)</td><td>65.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (-12.27%)</td><td>0.05 (+6.31%)</td><td>0.05 (+9.69%)</td><td>0.03 (+5.12%)</td><td>0.02 (-13.76%)</td><td>611.20 (-4.87%)</td><td>387.02 (-9.52%)</td><td>407.00 (-8.83%)</td><td>243.40 (+13.95%)</td><td>153.08 (-13.66%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>642.50 (n/a)</td><td>427.72 (n/a)</td><td>446.40 (n/a)</td><td>213.60 (n/a)</td><td>177.28 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (+11.06%)</td><td>0.05 (+19.69%)</td><td>0.05 (+8.46%)</td><td>0.02 <b>(+146.97%)</b></td><td>0.02 (-15.72%)</td><td>812.50 <b>(-59.51%)</b></td><td>419.54 <b>(-42.75%)</b></td><td>343.00 (-7.80%)</td><td>226.40 (-9.94%)</td><td>237.10 <b>(-68.05%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2006.70 (n/a)</td><td>732.84 (n/a)</td><td>372.00 (n/a)</td><td>251.40 (n/a)</td><td>742.09 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.05 <b>(-32.25%)</b></td><td>0.04 <b>(-28.24%)</b></td><td>0.04 (-17.40%)</td><td>0.03 (-18.43%)</td><td>0.01 <b>(-46.53%)</b></td><td>656.50 <b>(+22.60%)</b></td><td>513.82 <b>(+34.56%)</b></td><td>502.20 <b>(+21.04%)</b></td><td>363.60 <b>(+47.62%)</b></td><td>112.84 (-1.30%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>535.50 (n/a)</td><td>381.84 (n/a)</td><td>414.90 (n/a)</td><td>246.30 (n/a)</td><td>114.33 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.08 (-1.84%)</td><td>0.06 (+15.52%)</td><td>0.07 <b>(+54.46%)</b></td><td>0.04 <b>(+27.55%)</b></td><td>0.02 <b>(-29.05%)</b></td><td>474.80 <b>(-21.60%)</b></td><td>317.68 <b>(-20.66%)</b></td><td>270.30 <b>(-35.26%)</b></td><td>227.90 (+1.88%)</td><td>101.27 <b>(-39.69%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>605.60 (n/a)</td><td>400.42 (n/a)</td><td>417.50 (n/a)</td><td>223.70 (n/a)</td><td>167.91 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.43 (-7.15%)</td><td>0.35 (+18.45%)</td><td>0.34 <b>(+21.93%)</b></td><td>0.28 <b>(+68.00%)</b></td><td>0.06 <b>(-51.84%)</b></td><td>354.50 <b>(-40.48%)</b></td><td>288.84 <b>(-25.44%)</b></td><td>289.30 (-17.98%)</td><td>230.00 (+7.68%)</td><td>49.36 <b>(-69.71%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>595.60 (n/a)</td><td>387.38 (n/a)</td><td>352.70 (n/a)</td><td>213.60 (n/a)</td><td>162.95 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.38 (-6.03%)</td><td>0.32 (-1.98%)</td><td>0.33 (-2.44%)</td><td>0.23 <b>(+27.79%)</b></td><td>0.06 <b>(-36.81%)</b></td><td>432.60 <b>(-21.74%)</b></td><td>317.36 (-3.66%)</td><td>297.20 (+2.48%)</td><td>260.80 (+6.45%)</td><td>67.39 <b>(-47.22%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.40 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>552.80 (n/a)</td><td>329.40 (n/a)</td><td>290.00 (n/a)</td><td>245.00 (n/a)</td><td>127.68 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.33 (-14.81%)</td><td>0.21 <b>(-26.94%)</b></td><td>0.21 (-13.06%)</td><td>0.10 <b>(-48.66%)</b></td><td>0.09 (-3.79%)</td><td>1014.00 <b>(+94.78%)</b></td><td>563.00 <b>(+48.54%)</b></td><td>478.60 (+14.99%)</td><td>293.70 (+17.39%)</td><td>272.52 <b>(+137.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>520.60 (n/a)</td><td>379.02 (n/a)</td><td>416.20 (n/a)</td><td>250.20 (n/a)</td><td>114.68 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.27 (-10.41%)</td><td>0.21 (+7.88%)</td><td>0.25 (+1.84%)</td><td>0.11 <b>(+283.88%)</b></td><td>0.07 <b>(-36.53%)</b></td><td>655.20 <b>(-73.95%)</b></td><td>391.90 <b>(-49.11%)</b></td><td>290.80 (-1.82%)</td><td>275.20 (+11.60%)</td><td>163.16 <b>(-83.36%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>0.11 (n/a)</td><td>2515.30 (n/a)</td><td>770.12 (n/a)</td><td>296.20 (n/a)</td><td>246.60 (n/a)</td><td>980.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.30 (-0.60%)</td><td>0.25 (+2.18%)</td><td>0.27 (+6.34%)</td><td>0.14 (-19.34%)</td><td>0.07 <b>(+40.64%)</b></td><td>519.10 <b>(+23.98%)</b></td><td>314.46 (+2.52%)</td><td>276.00 (-5.93%)</td><td>242.40 (+0.62%)</td><td>116.39 <b>(+73.55%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>418.70 (n/a)</td><td>306.74 (n/a)</td><td>293.40 (n/a)</td><td>240.90 (n/a)</td><td>67.07 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.18 <b>(-31.76%)</b></td><td>0.16 (-17.21%)</td><td>0.15 (-7.63%)</td><td>0.15 (+6.28%)</td><td>0.01 <b>(-80.31%)</b></td><td>499.20 (-5.90%)</td><td>469.56 (+12.96%)</td><td>480.20 (+8.28%)</td><td>416.90 <b>(+46.54%)</b></td><td>31.79 <b>(-73.01%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>530.50 (n/a)</td><td>415.70 (n/a)</td><td>443.50 (n/a)</td><td>284.50 (n/a)</td><td>117.81 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.19 <b>(+101.84%)</b></td><td>0.13 <b>(+55.13%)</b></td><td>0.13 <b>(+48.74%)</b></td><td>0.08 (+19.51%)</td><td>0.04 <b>(+227.14%)</b></td><td>487.90 (-16.33%)</td><td>309.30 <b>(-30.87%)</b></td><td>294.20 <b>(-32.77%)</b></td><td>189.10 <b>(-50.45%)</b></td><td>110.12 <b>(+36.74%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>583.10 (n/a)</td><td>447.40 (n/a)</td><td>437.60 (n/a)</td><td>381.60 (n/a)</td><td>80.53 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.21 <b>(+47.90%)</b></td><td>0.12 (-3.41%)</td><td>0.15 (+10.27%)</td><td>0.02 <b>(-77.52%)</b></td><td>0.08 <b>(+200.35%)</b></td><td>2022.60 <b>(+344.92%)</b></td><td>637.56 <b>(+106.52%)</b></td><td>252.70 (-9.30%)</td><td>173.10 <b>(-32.38%)</b></td><td>783.76 <b>(+851.59%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>454.60 (n/a)</td><td>308.72 (n/a)</td><td>278.60 (n/a)</td><td>256.00 (n/a)</td><td>82.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (+13.67%)</td><td>0.10 <b>(+28.94%)</b></td><td>0.09 (+15.31%)</td><td>0.06 <b>(+246.67%)</b></td><td>0.03 (-12.74%)</td><td>608.30 <b>(-71.16%)</b></td><td>414.86 <b>(-45.71%)</b></td><td>410.90 (-13.28%)</td><td>258.90 (-12.03%)</td><td>144.05 <b>(-80.98%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2108.90 (n/a)</td><td>764.18 (n/a)</td><td>473.80 (n/a)</td><td>294.30 (n/a)</td><td>757.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (-4.69%)</td><td>0.11 (-5.74%)</td><td>0.12 (-15.16%)</td><td>0.07 (-5.59%)</td><td>0.03 (-16.79%)</td><td>523.40 (+5.93%)</td><td>359.10 (+3.83%)</td><td>312.70 (+17.87%)</td><td>260.30 (+4.92%)</td><td>110.83 (-8.29%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>494.10 (n/a)</td><td>345.84 (n/a)</td><td>265.30 (n/a)</td><td>248.10 (n/a)</td><td>120.84 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (-3.96%)</td><td>0.11 (+18.28%)</td><td>0.12 <b>(+62.67%)</b></td><td>0.06 <b>(+67.24%)</b></td><td>0.04 <b>(-27.44%)</b></td><td>659.70 <b>(-40.21%)</b></td><td>369.96 <b>(-29.73%)</b></td><td>317.60 <b>(-38.52%)</b></td><td>241.00 (+4.15%)</td><td>171.25 <b>(-51.36%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1103.30 (n/a)</td><td>526.46 (n/a)</td><td>516.60 (n/a)</td><td>231.40 (n/a)</td><td>352.06 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 <b>(-21.33%)</b></td><td>0.07 <b>(-28.38%)</b></td><td>0.07 (-2.82%)</td><td>0.03 <b>(-45.75%)</b></td><td>0.03 <b>(-29.32%)</b></td><td>1058.70 <b>(+84.35%)</b></td><td>589.44 <b>(+42.78%)</b></td><td>495.30 (+2.89%)</td><td>299.30 <b>(+27.15%)</b></td><td>289.87 <b>(+78.71%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>574.30 (n/a)</td><td>412.82 (n/a)</td><td>481.40 (n/a)</td><td>235.40 (n/a)</td><td>162.20 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (-18.73%)</td><td>0.12 (-0.72%)</td><td>0.13 (+2.83%)</td><td>0.09 <b>(+26.30%)</b></td><td>0.03 <b>(-43.21%)</b></td><td>479.70 <b>(-20.83%)</b></td><td>360.88 (-8.85%)</td><td>312.20 (-2.74%)</td><td>278.70 <b>(+23.05%)</b></td><td>90.87 <b>(-46.98%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>605.90 (n/a)</td><td>395.94 (n/a)</td><td>321.00 (n/a)</td><td>226.50 (n/a)</td><td>171.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.16 (+1.66%)</td><td>0.12 (+5.53%)</td><td>0.14 <b>(+61.39%)</b></td><td>0.02 <b>(-70.53%)</b></td><td>0.06 <b>(+41.78%)</b></td><td>1930.90 <b>(+239.35%)</b></td><td>623.98 <b>(+52.62%)</b></td><td>285.90 <b>(-38.04%)</b></td><td>260.90 (-1.66%)</td><td>732.16 <b>(+434.16%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>569.00 (n/a)</td><td>408.84 (n/a)</td><td>461.40 (n/a)</td><td>265.30 (n/a)</td><td>137.07 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.20 <b>(+22.40%)</b></td><td>0.12 <b>(-21.11%)</b></td><td>0.09 <b>(-38.95%)</b></td><td>0.08 <b>(-43.03%)</b></td><td>0.05 <b>(+321.70%)</b></td><td>520.80 <b>(+75.53%)</b></td><td>396.96 <b>(+44.70%)</b></td><td>454.90 <b>(+63.81%)</b></td><td>203.70 (-18.29%)</td><td>144.75 <b>(+532.10%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>296.70 (n/a)</td><td>274.34 (n/a)</td><td>277.70 (n/a)</td><td>249.30 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (-7.19%)</td><td>0.12 (-0.65%)</td><td>0.15 (+3.77%)</td><td>0.08 (+19.83%)</td><td>0.04 (-15.23%)</td><td>533.50 (-16.55%)</td><td>364.28 (-3.88%)</td><td>272.20 (-3.61%)</td><td>266.00 (+7.78%)</td><td>132.01 <b>(-23.47%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>639.30 (n/a)</td><td>379.00 (n/a)</td><td>282.40 (n/a)</td><td>246.80 (n/a)</td><td>172.50 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.09 <b>(-44.91%)</b></td><td>0.08 <b>(-27.08%)</b></td><td>0.08 (-13.60%)</td><td>0.07 (-11.24%)</td><td>0.01 <b>(-76.93%)</b></td><td>549.30 (+12.68%)</td><td>497.04 <b>(+28.12%)</b></td><td>499.10 (+15.75%)</td><td>434.10 <b>(+81.48%)</b></td><td>51.22 <b>(-53.27%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>487.50 (n/a)</td><td>387.96 (n/a)</td><td>431.20 (n/a)</td><td>239.20 (n/a)</td><td>109.61 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.17 (+0.34%)</td><td>0.12 (-9.47%)</td><td>0.09 <b>(-26.29%)</b></td><td>0.09 (+13.98%)</td><td>0.04 (+0.27%)</td><td>474.90 (-12.25%)</td><td>382.52 (+9.75%)</td><td>436.10 <b>(+35.65%)</b></td><td>244.70 (-0.33%)</td><td>105.83 (-10.67%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>541.20 (n/a)</td><td>348.54 (n/a)</td><td>321.50 (n/a)</td><td>245.50 (n/a)</td><td>118.47 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (-4.43%)</td><td>0.09 <b>(-36.02%)</b></td><td>0.07 <b>(-46.86%)</b></td><td>0.05 <b>(-56.53%)</b></td><td>0.04 <b>(+154.31%)</b></td><td>696.70 <b>(+130.01%)</b></td><td>454.58 <b>(+75.16%)</b></td><td>477.30 <b>(+88.21%)</b></td><td>237.90 (+4.66%)</td><td>167.43 <b>(+485.02%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>302.90 (n/a)</td><td>259.52 (n/a)</td><td>253.60 (n/a)</td><td>227.30 (n/a)</td><td>28.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (+4.75%)</td><td>0.11 (+2.46%)</td><td>0.12 (+12.95%)</td><td>0.06 <b>(-20.20%)</b></td><td>0.03 <b>(+39.48%)</b></td><td>614.70 <b>(+25.30%)</b></td><td>347.64 (+3.56%)</td><td>283.40 (-11.47%)</td><td>256.10 (-4.55%)</td><td>151.67 <b>(+68.16%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>490.60 (n/a)</td><td>335.70 (n/a)</td><td>320.10 (n/a)</td><td>268.30 (n/a)</td><td>90.20 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (-16.39%)</td><td>0.10 (-3.67%)</td><td>0.10 <b>(+28.96%)</b></td><td>0.06 (-12.05%)</td><td>0.04 (-13.44%)</td><td>578.30 (+13.70%)</td><td>396.96 (+4.56%)</td><td>339.00 <b>(-22.46%)</b></td><td>241.50 (+19.55%)</td><td>160.36 <b>(+22.14%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>508.60 (n/a)</td><td>379.64 (n/a)</td><td>437.20 (n/a)</td><td>202.00 (n/a)</td><td>131.29 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 <b>(-39.77%)</b></td><td>0.12 (+16.77%)</td><td>0.12 (+15.89%)</td><td>0.08 <b>(+332.77%)</b></td><td>0.02 <b>(-73.23%)</b></td><td>441.60 <b>(-76.90%)</b></td><td>312.04 <b>(-65.66%)</b></td><td>290.30 (-13.70%)</td><td>258.00 <b>(+66.02%)</b></td><td>75.99 <b>(-91.58%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.09 (n/a)</td><td>1911.30 (n/a)</td><td>908.78 (n/a)</td><td>336.40 (n/a)</td><td>155.40 (n/a)</td><td>902.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (-14.79%)</td><td>0.09 (+8.12%)</td><td>0.10 <b>(+33.94%)</b></td><td>0.05 <b>(+259.88%)</b></td><td>0.03 <b>(-50.71%)</b></td><td>662.70 <b>(-72.22%)</b></td><td>410.50 <b>(-48.59%)</b></td><td>335.80 <b>(-25.33%)</b></td><td>285.40 (+17.35%)</td><td>154.28 <b>(-82.94%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.06 (n/a)</td><td>2385.10 (n/a)</td><td>798.52 (n/a)</td><td>449.70 (n/a)</td><td>243.20 (n/a)</td><td>904.40 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.13 (-13.56%)</td><td>0.09 <b>(-29.08%)</b></td><td>0.07 <b>(-49.18%)</b></td><td>0.06 <b>(-23.27%)</b></td><td>0.03 (+11.92%)</td><td>581.60 <b>(+30.35%)</b></td><td>437.04 <b>(+47.25%)</b></td><td>493.20 <b>(+96.81%)</b></td><td>278.20 (+15.68%)</td><td>142.14 <b>(+63.01%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>446.20 (n/a)</td><td>296.80 (n/a)</td><td>250.60 (n/a)</td><td>240.50 (n/a)</td><td>87.20 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.30 <b>(-41.98%)</b></td><td>0.26 <b>(-43.88%)</b></td><td>0.26 <b>(-45.69%)</b></td><td>0.19 <b>(-41.05%)</b></td><td>0.04 <b>(-46.60%)</b></td><td>674.30 <b>(+69.64%)</b></td><td>518.72 <b>(+77.36%)</b></td><td>506.90 <b>(+84.13%)</b></td><td>441.40 <b>(+72.35%)</b></td><td>92.47 <b>(+55.53%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.51 (n/a)</td><td>0.46 (n/a)</td><td>0.48 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>397.50 (n/a)</td><td>292.46 (n/a)</td><td>275.30 (n/a)</td><td>256.10 (n/a)</td><td>59.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.49 (+1.24%)</td><td>0.42 <b>(+50.23%)</b></td><td>0.43 <b>(+67.01%)</b></td><td>0.33 <b>(+69.33%)</b></td><td>0.07 <b>(-42.17%)</b></td><td>399.30 <b>(-40.95%)</b></td><td>315.90 <b>(-38.44%)</b></td><td>301.40 <b>(-40.13%)</b></td><td>270.20 (-1.21%)</td><td>53.82 <b>(-65.21%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.48 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>676.20 (n/a)</td><td>513.18 (n/a)</td><td>503.40 (n/a)</td><td>273.50 (n/a)</td><td>154.69 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.42 <b>(-22.39%)</b></td><td>0.31 (+0.07%)</td><td>0.26 (+17.12%)</td><td>0.23 (+19.17%)</td><td>0.09 <b>(-37.69%)</b></td><td>560.30 (-16.09%)</td><td>452.66 (-8.91%)</td><td>512.50 (-14.63%)</td><td>311.90 <b>(+28.83%)</b></td><td>125.26 <b>(-35.44%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.54 (n/a)</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>667.70 (n/a)</td><td>496.96 (n/a)</td><td>600.30 (n/a)</td><td>242.10 (n/a)</td><td>194.04 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.00 (-12.50%)</td><td>0.00 <b>(-36.36%)</b></td><td>0.00 <b>(-57.14%)</b></td><td>0.00 <b>(-60.00%)</b></td><td>0.00 <b>(+90.14%)</b></td><td>17251.44 <b>(+113.32%)</b></td><td>12128.84 <b>(+94.55%)</b></td><td>14897.89 <b>(+161.38%)</b></td><td>5918.51 (+16.31%)</td><td>5474.88 <b>(+347.49%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>8087.11 (n/a)</td><td>6234.32 (n/a)</td><td>5699.64 (n/a)</td><td>5088.66 (n/a)</td><td>1223.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.00 (-16.67%)</td><td>0.00 (-4.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-55.28%)</b></td><td>21690.41 (+2.23%)</td><td>17464.83 (+1.87%)</td><td>16385.53 (-4.35%)</td><td>15704.75 (+13.97%)</td><td>2478.53 <b>(-25.49%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21217.65 (n/a)</td><td>17144.41 (n/a)</td><td>17130.72 (n/a)</td><td>13779.24 (n/a)</td><td>3326.43 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.14 (+4.81%)</td><td>0.09 (-10.05%)</td><td>0.08 <b>(-21.51%)</b></td><td>0.07 (-0.41%)</td><td>0.03 (+6.33%)</td><td>28460.84 (+0.44%)</td><td>24865.55 (+11.40%)</td><td>27635.52 <b>(+27.47%)</b></td><td>15283.52 (-4.59%)</td><td>5484.32 (-3.31%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28335.83 (n/a)</td><td>22321.49 (n/a)</td><td>21680.22 (n/a)</td><td>16019.55 (n/a)</td><td>5672.15 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>2.98 <b>(+24.70%)</b></td><td>1.90 (+19.33%)</td><td>2.31 (+17.26%)</td><td>0.29 <b>(-30.50%)</b></td><td>1.03 <b>(+20.14%)</b></td><td>3598.50 <b>(+43.89%)</b></td><td>1102.36 (+9.84%)</td><td>454.30 (-14.72%)</td><td>351.60 (-19.82%)</td><td>1399.86 <b>(+59.84%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>2.39 (n/a)</td><td>1.59 (n/a)</td><td>1.97 (n/a)</td><td>0.42 (n/a)</td><td>0.85 (n/a)</td><td>2500.90 (n/a)</td><td>1003.56 (n/a)</td><td>532.70 (n/a)</td><td>438.50 (n/a)</td><td>875.80 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>1.92 <b>(-55.66%)</b></td><td>1.30 <b>(-47.27%)</b></td><td>1.42 <b>(-43.46%)</b></td><td>0.56 <b>(-49.14%)</b></td><td>0.54 <b>(-59.35%)</b></td><td>1874.60 <b>(+96.60%)</b></td><td>976.06 <b>(+77.65%)</b></td><td>735.90 <b>(+76.86%)</b></td><td>546.90 <b>(+125.53%)</b></td><td>539.83 <b>(+76.19%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>4.32 (n/a)</td><td>2.46 (n/a)</td><td>2.52 (n/a)</td><td>1.10 (n/a)</td><td>1.32 (n/a)</td><td>953.50 (n/a)</td><td>549.44 (n/a)</td><td>416.10 (n/a)</td><td>242.50 (n/a)</td><td>306.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.41 (-2.50%)</td><td>2.47 (+3.59%)</td><td>2.43 (-10.92%)</td><td>1.48 <b>(+169.07%)</b></td><td>0.69 <b>(-45.90%)</b></td><td>708.00 <b>(-62.83%)</b></td><td>456.30 <b>(-35.16%)</b></td><td>431.80 (+12.24%)</td><td>307.80 (+2.57%)</td><td>149.81 <b>(-78.12%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>3.49 (n/a)</td><td>2.39 (n/a)</td><td>2.73 (n/a)</td><td>0.55 (n/a)</td><td>1.27 (n/a)</td><td>1904.90 (n/a)</td><td>703.76 (n/a)</td><td>384.70 (n/a)</td><td>300.10 (n/a)</td><td>684.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.88 <b>(+27.54%)</b></td><td>2.23 (-0.93%)</td><td>1.78 (-14.71%)</td><td>1.13 <b>(-31.09%)</b></td><td>1.13 <b>(+98.09%)</b></td><td>927.80 <b>(+45.10%)</b></td><td>570.64 (+16.59%)</td><td>590.40 (+17.24%)</td><td>270.00 <b>(-21.58%)</b></td><td>262.63 <b>(+122.28%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>3.05 (n/a)</td><td>2.25 (n/a)</td><td>2.08 (n/a)</td><td>1.64 (n/a)</td><td>0.57 (n/a)</td><td>639.40 (n/a)</td><td>489.44 (n/a)</td><td>503.60 (n/a)</td><td>344.30 (n/a)</td><td>118.15 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>4.64 (+14.35%)</td><td>2.53 <b>(-26.80%)</b></td><td>1.98 <b>(-43.55%)</b></td><td>0.59 <b>(-76.91%)</b></td><td>1.59 <b>(+179.43%)</b></td><td>3565.20 <b>(+333.20%)</b></td><td>1355.24 <b>(+118.19%)</b></td><td>1061.60 <b>(+77.14%)</b></td><td>451.60 (-12.55%)</td><td>1268.60 <b>(+968.04%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>4.06 (n/a)</td><td>3.46 (n/a)</td><td>3.50 (n/a)</td><td>2.55 (n/a)</td><td>0.57 (n/a)</td><td>823.00 (n/a)</td><td>621.14 (n/a)</td><td>599.30 (n/a)</td><td>516.40 (n/a)</td><td>118.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.14 (+0.58%)</td><td>2.76 (-0.70%)</td><td>2.38 (-7.60%)</td><td>0.59 (+2.38%)</td><td>2.24 (-0.13%)</td><td>3531.40 (-2.32%)</td><td>1689.58 (-3.69%)</td><td>880.70 (+8.23%)</td><td>407.80 (-0.59%)</td><td>1551.51 (-6.66%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>5.11 (n/a)</td><td>2.78 (n/a)</td><td>2.58 (n/a)</td><td>0.58 (n/a)</td><td>2.25 (n/a)</td><td>3615.30 (n/a)</td><td>1754.32 (n/a)</td><td>813.70 (n/a)</td><td>410.20 (n/a)</td><td>1662.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>6.30 <b>(+34.87%)</b></td><td>4.77 <b>(+109.60%)</b></td><td>4.40 <b>(+75.20%)</b></td><td>3.77 <b>(+544.48%)</b></td><td>1.02 <b>(-37.92%)</b></td><td>556.30 <b>(-84.48%)</b></td><td>454.96 <b>(-71.83%)</b></td><td>476.50 <b>(-42.93%)</b></td><td>332.70 <b>(-25.85%)</b></td><td>89.80 <b>(-93.34%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>4.67 (n/a)</td><td>2.28 (n/a)</td><td>2.51 (n/a)</td><td>0.58 (n/a)</td><td>1.65 (n/a)</td><td>3585.40 (n/a)</td><td>1615.16 (n/a)</td><td>834.90 (n/a)</td><td>448.70 (n/a)</td><td>1347.66 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>4.43 <b>(-35.45%)</b></td><td>1.90 <b>(-62.45%)</b></td><td>0.87 <b>(-81.76%)</b></td><td>0.59 <b>(-82.37%)</b></td><td>1.74 <b>(+23.06%)</b></td><td>3580.80 <b>(+467.21%)</b></td><td>2130.20 <b>(+381.79%)</b></td><td>2398.00 <b>(+448.11%)</b></td><td>473.20 <b>(+54.89%)</b></td><td>1489.35 <b>(+1056.52%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>6.87 (n/a)</td><td>5.07 (n/a)</td><td>4.79 (n/a)</td><td>3.32 (n/a)</td><td>1.42 (n/a)</td><td>631.30 (n/a)</td><td>442.14 (n/a)</td><td>437.50 (n/a)</td><td>305.50 (n/a)</td><td>128.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>7.83 <b>(+23.33%)</b></td><td>3.70 (-0.95%)</td><td>2.65 <b>(-24.96%)</b></td><td>2.02 <b>(+246.60%)</b></td><td>2.37 (+3.43%)</td><td>1037.60 <b>(-71.15%)</b></td><td>709.10 <b>(-37.59%)</b></td><td>789.90 <b>(+33.25%)</b></td><td>267.90 (-18.92%)</td><td>293.71 <b>(-78.82%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>6.35 (n/a)</td><td>3.73 (n/a)</td><td>3.54 (n/a)</td><td>0.58 (n/a)</td><td>2.30 (n/a)</td><td>3596.10 (n/a)</td><td>1136.20 (n/a)</td><td>592.80 (n/a)</td><td>330.40 (n/a)</td><td>1386.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>6.21 (-7.18%)</td><td>3.00 <b>(-25.96%)</b></td><td>3.14 (-11.99%)</td><td>0.59 <b>(-76.49%)</b></td><td>2.10 <b>(+33.98%)</b></td><td>3563.40 <b>(+325.38%)</b></td><td>1274.74 <b>(+123.14%)</b></td><td>668.20 (+13.62%)</td><td>338.00 (+7.75%)</td><td>1313.61 <b>(+601.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>6.69 (n/a)</td><td>4.06 (n/a)</td><td>3.57 (n/a)</td><td>2.50 (n/a)</td><td>1.57 (n/a)</td><td>837.70 (n/a)</td><td>571.28 (n/a)</td><td>588.10 (n/a)</td><td>313.70 (n/a)</td><td>187.22 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.18 (-4.60%)</td><td>3.30 (+3.11%)</td><td>3.28 (-17.49%)</td><td>1.23 (+6.39%)</td><td>1.48 <b>(-20.60%)</b></td><td>3412.00 (-6.01%)</td><td>1613.04 (-15.54%)</td><td>1277.60 <b>(+21.19%)</b></td><td>810.40 (+4.82%)</td><td>1041.37 <b>(-21.68%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>5.43 (n/a)</td><td>3.20 (n/a)</td><td>3.98 (n/a)</td><td>1.16 (n/a)</td><td>1.86 (n/a)</td><td>3630.10 (n/a)</td><td>1909.74 (n/a)</td><td>1054.20 (n/a)</td><td>773.10 (n/a)</td><td>1329.68 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>5.80 <b>(-30.34%)</b></td><td>3.56 <b>(-39.12%)</b></td><td>3.51 <b>(-44.27%)</b></td><td>1.15 <b>(-68.80%)</b></td><td>2.18 (+14.57%)</td><td>3656.90 <b>(+220.56%)</b></td><td>1762.84 <b>(+124.75%)</b></td><td>1195.80 <b>(+79.44%)</b></td><td>723.00 <b>(+43.57%)</b></td><td>1283.41 <b>(+378.68%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>8.33 (n/a)</td><td>5.86 (n/a)</td><td>6.29 (n/a)</td><td>3.68 (n/a)</td><td>1.90 (n/a)</td><td>1140.80 (n/a)</td><td>784.34 (n/a)</td><td>666.40 (n/a)</td><td>503.60 (n/a)</td><td>268.12 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>8.16 (-5.22%)</td><td>6.38 <b>(+45.42%)</b></td><td>6.27 <b>(+107.09%)</b></td><td>4.88 <b>(+186.89%)</b></td><td>1.19 <b>(-62.21%)</b></td><td>860.20 <b>(-65.14%)</b></td><td>676.28 <b>(-54.03%)</b></td><td>668.80 <b>(-51.71%)</b></td><td>513.90 (+5.52%)</td><td>125.46 <b>(-86.73%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>8.61 (n/a)</td><td>4.38 (n/a)</td><td>3.03 (n/a)</td><td>1.70 (n/a)</td><td>3.16 (n/a)</td><td>2467.70 (n/a)</td><td>1471.26 (n/a)</td><td>1385.00 (n/a)</td><td>487.00 (n/a)</td><td>945.24 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>9.42 (-7.50%)</td><td>5.34 <b>(-30.18%)</b></td><td>3.86 <b>(-52.94%)</b></td><td>1.19 <b>(-60.86%)</b></td><td>3.46 <b>(+27.09%)</b></td><td>3520.10 <b>(+155.49%)</b></td><td>1328.70 <b>(+101.31%)</b></td><td>1086.00 <b>(+112.48%)</b></td><td>445.20 (+8.11%)</td><td>1263.54 <b>(+212.99%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>10.18 (n/a)</td><td>7.65 (n/a)</td><td>8.21 (n/a)</td><td>3.04 (n/a)</td><td>2.72 (n/a)</td><td>1377.80 (n/a)</td><td>660.04 (n/a)</td><td>511.10 (n/a)</td><td>411.80 (n/a)</td><td>403.71 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>8.82 (-1.29%)</td><td>5.55 (+12.43%)</td><td>4.64 (+14.92%)</td><td>3.84 <b>(+218.66%)</b></td><td>2.08 <b>(-30.05%)</b></td><td>1092.60 <b>(-68.62%)</b></td><td>830.84 <b>(-38.18%)</b></td><td>904.70 (-12.98%)</td><td>475.40 (+1.30%)</td><td>258.72 <b>(-78.88%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>8.94 (n/a)</td><td>4.94 (n/a)</td><td>4.03 (n/a)</td><td>1.20 (n/a)</td><td>2.97 (n/a)</td><td>3481.50 (n/a)</td><td>1344.02 (n/a)</td><td>1039.60 (n/a)</td><td>469.30 (n/a)</td><td>1225.07 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>8.25 (-6.49%)</td><td>6.67 (-9.66%)</td><td>7.25 (-1.10%)</td><td>4.72 (-14.20%)</td><td>1.71 <b>(+34.85%)</b></td><td>888.10 (+16.55%)</td><td>666.06 (+14.29%)</td><td>578.20 (+1.10%)</td><td>508.40 (+6.94%)</td><td>184.35 <b>(+66.07%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>8.82 (n/a)</td><td>7.39 (n/a)</td><td>7.33 (n/a)</td><td>5.50 (n/a)</td><td>1.27 (n/a)</td><td>762.00 (n/a)</td><td>582.78 (n/a)</td><td>571.90 (n/a)</td><td>475.40 (n/a)</td><td>111.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>1.50 <b>(-23.49%)</b></td><td>1.04 (-18.25%)</td><td>1.06 (-0.96%)</td><td>0.58 <b>(-36.62%)</b></td><td>0.37 (-15.27%)</td><td>903.10 <b>(+57.77%)</b></td><td>566.22 <b>(+26.68%)</b></td><td>492.80 (+0.96%)</td><td>350.30 <b>(+30.71%)</b></td><td>223.11 <b>(+76.22%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>1.96 (n/a)</td><td>1.27 (n/a)</td><td>1.07 (n/a)</td><td>0.92 (n/a)</td><td>0.43 (n/a)</td><td>572.40 (n/a)</td><td>446.98 (n/a)</td><td>488.10 (n/a)</td><td>268.00 (n/a)</td><td>126.61 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>3.01 (-0.31%)</td><td>1.75 <b>(-20.78%)</b></td><td>1.41 <b>(-43.23%)</b></td><td>0.42 <b>(+41.88%)</b></td><td>1.10 (-0.57%)</td><td>2483.50 <b>(-29.52%)</b></td><td>971.98 (-4.72%)</td><td>741.90 <b>(+76.14%)</b></td><td>347.80 (+0.29%)</td><td>877.37 <b>(-37.33%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>3.02 (n/a)</td><td>2.21 (n/a)</td><td>2.49 (n/a)</td><td>0.30 (n/a)</td><td>1.10 (n/a)</td><td>3523.60 (n/a)</td><td>1020.08 (n/a)</td><td>421.20 (n/a)</td><td>346.80 (n/a)</td><td>1400.07 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>4.03 <b>(+25.19%)</b></td><td>2.33 (+15.47%)</td><td>2.66 <b>(+73.16%)</b></td><td>0.55 <b>(-40.71%)</b></td><td>1.46 <b>(+49.52%)</b></td><td>3790.80 <b>(+68.67%)</b></td><td>1521.84 (+19.49%)</td><td>788.50 <b>(-42.25%)</b></td><td>520.80 <b>(-20.12%)</b></td><td>1377.20 <b>(+114.68%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>3.22 (n/a)</td><td>2.02 (n/a)</td><td>1.54 (n/a)</td><td>0.93 (n/a)</td><td>0.98 (n/a)</td><td>2247.40 (n/a)</td><td>1273.62 (n/a)</td><td>1365.30 (n/a)</td><td>652.00 (n/a)</td><td>641.53 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>1.96 (-12.48%)</td><td>1.11 <b>(-24.10%)</b></td><td>0.95 <b>(-37.79%)</b></td><td>0.74 (+17.29%)</td><td>0.48 <b>(-27.44%)</b></td><td>705.00 (-14.74%)</td><td>523.82 (+18.67%)</td><td>549.50 <b>(+60.77%)</b></td><td>266.90 (+14.30%)</td><td>158.71 <b>(-35.30%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>2.24 (n/a)</td><td>1.47 (n/a)</td><td>1.53 (n/a)</td><td>0.63 (n/a)</td><td>0.67 (n/a)</td><td>826.90 (n/a)</td><td>441.42 (n/a)</td><td>341.80 (n/a)</td><td>233.50 (n/a)</td><td>245.29 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.12 (-15.80%)</td><td>0.09 (+8.40%)</td><td>0.08 (+13.41%)</td><td>0.06 (+7.34%)</td><td>0.03 <b>(-24.69%)</b></td><td>512.40 (-6.84%)</td><td>372.54 (-10.72%)</td><td>400.90 (-11.81%)</td><td>268.00 (+18.74%)</td><td>102.16 (-16.00%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>550.00 (n/a)</td><td>417.28 (n/a)</td><td>454.60 (n/a)</td><td>225.70 (n/a)</td><td>121.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.15 (+10.68%)</td><td>0.08 (+16.89%)</td><td>0.06 (+7.70%)</td><td>0.06 <b>(+88.34%)</b></td><td>0.04 (-0.87%)</td><td>591.00 <b>(-46.91%)</b></td><td>469.40 <b>(-22.65%)</b></td><td>539.40 (-7.16%)</td><td>225.20 (-9.67%)</td><td>149.08 <b>(-52.82%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1113.10 (n/a)</td><td>606.82 (n/a)</td><td>581.00 (n/a)</td><td>249.30 (n/a)</td><td>315.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.26 (-10.23%)</td><td>0.19 <b>(-28.18%)</b></td><td>0.21 (-19.81%)</td><td>0.07 <b>(-66.88%)</b></td><td>0.07 <b>(+169.48%)</b></td><td>881.30 <b>(+202.02%)</b></td><td>429.40 <b>(+69.23%)</b></td><td>307.80 <b>(+24.72%)</b></td><td>248.60 (+11.38%)</td><td>261.26 <b>(+845.71%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>291.80 (n/a)</td><td>253.74 (n/a)</td><td>246.80 (n/a)</td><td>223.20 (n/a)</td><td>27.63 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.26 (+1.57%)</td><td>0.15 (-18.76%)</td><td>0.12 (-14.27%)</td><td>0.10 (-13.82%)</td><td>0.06 (-0.74%)</td><td>641.80 (+16.04%)</td><td>500.00 <b>(+24.63%)</b></td><td>526.50 (+16.64%)</td><td>256.50 (-1.54%)</td><td>152.70 (+16.56%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>553.10 (n/a)</td><td>401.18 (n/a)</td><td>451.40 (n/a)</td><td>260.50 (n/a)</td><td>131.00 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.20 <b>(-32.48%)</b></td><td>0.14 <b>(-21.98%)</b></td><td>0.13 (-7.09%)</td><td>0.09 <b>(-29.03%)</b></td><td>0.04 <b>(-42.68%)</b></td><td>763.40 <b>(+40.90%)</b></td><td>518.18 <b>(+24.51%)</b></td><td>496.80 (+7.63%)</td><td>333.20 <b>(+48.09%)</b></td><td>155.48 <b>(+24.12%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.29 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>541.80 (n/a)</td><td>416.16 (n/a)</td><td>461.60 (n/a)</td><td>225.00 (n/a)</td><td>125.26 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.33 <b>(-29.88%)</b></td><td>0.24 <b>(-42.86%)</b></td><td>0.22 <b>(-47.54%)</b></td><td>0.13 <b>(-64.87%)</b></td><td>0.09 <b>(+74.58%)</b></td><td>1028.60 <b>(+184.62%)</b></td><td>612.00 <b>(+95.50%)</b></td><td>597.60 <b>(+90.62%)</b></td><td>394.30 <b>(+42.60%)</b></td><td>257.31 <b>(+596.04%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.47 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.05 (n/a)</td><td>361.40 (n/a)</td><td>313.04 (n/a)</td><td>313.50 (n/a)</td><td>276.50 (n/a)</td><td>36.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.47 <b>(-31.10%)</b></td><td>0.29 <b>(-24.27%)</b></td><td>0.24 (-16.08%)</td><td>0.21 (-7.18%)</td><td>0.10 <b>(-44.24%)</b></td><td>611.70 (+7.73%)</td><td>480.42 <b>(+22.50%)</b></td><td>537.20 (+19.17%)</td><td>279.60 <b>(+45.10%)</b></td><td>130.68 (-13.71%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.68 (n/a)</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>567.80 (n/a)</td><td>392.18 (n/a)</td><td>450.80 (n/a)</td><td>192.70 (n/a)</td><td>151.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.64 <b>(+102.47%)</b></td><td>0.33 <b>(+22.56%)</b></td><td>0.28 (+8.91%)</td><td>0.14 <b>(-38.44%)</b></td><td>0.19 <b>(+370.24%)</b></td><td>970.90 <b>(+62.44%)</b></td><td>507.02 (+2.54%)</td><td>464.70 (-8.18%)</td><td>204.70 <b>(-50.60%)</b></td><td>283.89 <b>(+281.50%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>597.70 (n/a)</td><td>494.48 (n/a)</td><td>506.10 (n/a)</td><td>414.40 (n/a)</td><td>74.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:11:11</td><td>0.07 (+2.12%)</td><td>0.04 <b>(-23.22%)</b></td><td>0.03 <b>(-48.25%)</b></td><td>0.03 (-12.31%)</td><td>0.02 (+5.20%)</td><td>551.20 (+14.05%)</td><td>436.10 <b>(+32.79%)</b></td><td>493.60 <b>(+93.27%)</b></td><td>232.60 (-2.06%)</td><td>134.95 (+19.75%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>483.30 (n/a)</td><td>328.42 (n/a)</td><td>255.40 (n/a)</td><td>237.50 (n/a)</td><td>112.69 (n/a)</td>
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
