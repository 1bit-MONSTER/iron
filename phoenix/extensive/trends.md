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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (+6.09%)</td><td>0.02 (-2.63%)</td><td>0.02 (-4.27%)</td><td>0.01 (-13.27%)</td><td>0.01 (+19.15%)</td><td>529.30 (+15.29%)</td><td>312.98 (+6.39%)</td><td>253.40 (+4.45%)</td><td>218.90 (-5.73%)</td><td>127.45 <b>(+32.50%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>459.10 (n/a)</td><td>294.18 (n/a)</td><td>242.60 (n/a)</td><td>232.20 (n/a)</td><td>96.18 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-13.20%)</td><td>0.02 (-15.89%)</td><td>0.01 <b>(-33.13%)</b></td><td>0.01 (+17.81%)</td><td>0.01 (-16.01%)</td><td>559.10 (-15.12%)</td><td>418.14 (+14.04%)</td><td>448.10 <b>(+49.52%)</b></td><td>253.70 (+15.16%)</td><td>140.52 (-19.90%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.70 (n/a)</td><td>366.66 (n/a)</td><td>299.70 (n/a)</td><td>220.30 (n/a)</td><td>175.42 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (+2.72%)</td><td>0.02 (-11.64%)</td><td>0.01 (-7.56%)</td><td>0.00 <b>(-71.09%)</b></td><td>0.01 <b>(+35.68%)</b></td><td>1925.90 <b>(+245.89%)</b></td><td>658.90 <b>(+81.01%)</b></td><td>426.50 (+8.19%)</td><td>202.40 (-2.65%)</td><td>718.13 <b>(+407.26%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.80 (n/a)</td><td>364.02 (n/a)</td><td>394.20 (n/a)</td><td>207.90 (n/a)</td><td>141.57 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (-6.19%)</td><td>0.02 (-2.28%)</td><td>0.01 <b>(-31.70%)</b></td><td>0.01 <b>(+405.84%)</b></td><td>0.01 <b>(-38.25%)</b></td><td>485.60 <b>(-80.23%)</b></td><td>377.18 <b>(-48.00%)</b></td><td>428.10 <b>(+46.41%)</b></td><td>237.10 (+6.56%)</td><td>115.86 <b>(-88.06%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2456.40 (n/a)</td><td>725.28 (n/a)</td><td>292.40 (n/a)</td><td>222.50 (n/a)</td><td>970.32 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (+11.29%)</td><td>0.01 <b>(-21.42%)</b></td><td>0.01 <b>(-29.90%)</b></td><td>0.01 <b>(-23.79%)</b></td><td>0.01 <b>(+45.36%)</b></td><td>609.30 <b>(+31.20%)</b></td><td>490.30 <b>(+36.11%)</b></td><td>512.00 <b>(+42.66%)</b></td><td>240.20 (-10.14%)</td><td>150.15 <b>(+68.52%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.40 (n/a)</td><td>360.22 (n/a)</td><td>358.90 (n/a)</td><td>267.30 (n/a)</td><td>89.10 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 <b>(-25.72%)</b></td><td>0.01 <b>(-36.12%)</b></td><td>0.01 <b>(-45.36%)</b></td><td>0.01 <b>(-36.27%)</b></td><td>0.00 (-16.21%)</td><td>699.80 <b>(+56.91%)</b></td><td>504.84 <b>(+60.42%)</b></td><td>532.70 <b>(+83.00%)</b></td><td>307.60 <b>(+34.62%)</b></td><td>152.96 <b>(+73.69%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>446.00 (n/a)</td><td>314.70 (n/a)</td><td>291.10 (n/a)</td><td>228.50 (n/a)</td><td>88.07 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 <b>(-34.11%)</b></td><td>0.03 <b>(-38.05%)</b></td><td>0.03 <b>(-42.25%)</b></td><td>0.02 <b>(-28.97%)</b></td><td>0.01 <b>(-27.69%)</b></td><td>636.00 <b>(+40.80%)</b></td><td>482.30 <b>(+62.55%)</b></td><td>468.60 <b>(+73.17%)</b></td><td>327.60 <b>(+51.74%)</b></td><td>140.51 <b>(+52.28%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>451.70 (n/a)</td><td>296.70 (n/a)</td><td>270.60 (n/a)</td><td>215.90 (n/a)</td><td>92.27 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (+8.01%)</td><td>0.04 (-0.08%)</td><td>0.04 (-4.44%)</td><td>0.02 (-15.78%)</td><td>0.01 <b>(+28.03%)</b></td><td>526.50 (+18.74%)</td><td>324.18 (+3.69%)</td><td>287.90 (+4.61%)</td><td>227.10 (-7.42%)</td><td>116.26 <b>(+47.74%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>443.40 (n/a)</td><td>312.64 (n/a)</td><td>275.20 (n/a)</td><td>245.30 (n/a)</td><td>78.69 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 <b>(-36.06%)</b></td><td>0.02 <b>(-24.82%)</b></td><td>0.02 (-7.92%)</td><td>0.01 <b>(-75.36%)</b></td><td>0.01 (-12.70%)</td><td>2442.50 <b>(+305.80%)</b></td><td>873.34 <b>(+89.63%)</b></td><td>515.80 (+8.61%)</td><td>373.30 <b>(+56.39%)</b></td><td>882.87 <b>(+527.23%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.90 (n/a)</td><td>460.54 (n/a)</td><td>474.90 (n/a)</td><td>238.70 (n/a)</td><td>140.76 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 <b>(-24.01%)</b></td><td>0.03 <b>(-36.63%)</b></td><td>0.02 <b>(-51.83%)</b></td><td>0.02 (-12.20%)</td><td>0.01 <b>(-28.92%)</b></td><td>602.70 (+13.89%)</td><td>468.62 <b>(+52.97%)</b></td><td>506.00 <b>(+107.55%)</b></td><td>267.20 <b>(+31.63%)</b></td><td>132.31 (+0.10%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.20 (n/a)</td><td>306.34 (n/a)</td><td>243.80 (n/a)</td><td>203.00 (n/a)</td><td>132.18 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (-6.57%)</td><td>0.03 <b>(+27.62%)</b></td><td>0.03 <b>(+74.17%)</b></td><td>0.02 (+1.75%)</td><td>0.01 (-12.10%)</td><td>608.10 (-1.71%)</td><td>404.46 <b>(-23.59%)</b></td><td>353.50 <b>(-42.59%)</b></td><td>245.20 (+7.03%)</td><td>161.42 (-4.73%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>618.70 (n/a)</td><td>529.36 (n/a)</td><td>615.70 (n/a)</td><td>229.10 (n/a)</td><td>169.42 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (+6.13%)</td><td>0.03 <b>(+22.19%)</b></td><td>0.03 <b>(+34.22%)</b></td><td>0.02 <b>(+84.61%)</b></td><td>0.01 (-19.71%)</td><td>500.70 <b>(-45.83%)</b></td><td>396.86 <b>(-26.41%)</b></td><td>410.60 <b>(-25.49%)</b></td><td>253.40 (-5.76%)</td><td>105.77 <b>(-57.65%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>924.30 (n/a)</td><td>539.26 (n/a)</td><td>551.10 (n/a)</td><td>268.90 (n/a)</td><td>249.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 <b>(-20.79%)</b></td><td>0.07 <b>(-21.82%)</b></td><td>0.06 <b>(-28.80%)</b></td><td>0.04 (-0.10%)</td><td>0.02 <b>(-27.97%)</b></td><td>611.90 (+0.10%)</td><td>407.82 <b>(+21.96%)</b></td><td>389.80 <b>(+40.47%)</b></td><td>276.40 <b>(+26.27%)</b></td><td>133.93 (-15.63%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>611.30 (n/a)</td><td>334.40 (n/a)</td><td>277.50 (n/a)</td><td>218.90 (n/a)</td><td>158.74 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.11 (+4.19%)</td><td>0.08 (+4.96%)</td><td>0.08 (-1.06%)</td><td>0.05 (+9.85%)</td><td>0.02 (+6.37%)</td><td>516.20 (-8.96%)</td><td>324.64 (-5.19%)</td><td>299.40 (+1.08%)</td><td>229.10 (-4.02%)</td><td>114.15 (-11.53%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>567.00 (n/a)</td><td>342.40 (n/a)</td><td>296.20 (n/a)</td><td>238.70 (n/a)</td><td>129.04 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.11 <b>(+50.31%)</b></td><td>0.07 (+16.99%)</td><td>0.07 (+17.50%)</td><td>0.05 (-7.72%)</td><td>0.03 <b>(+164.13%)</b></td><td>517.30 (+8.36%)</td><td>369.38 (-7.07%)</td><td>344.10 (-14.91%)</td><td>221.60 <b>(-33.47%)</b></td><td>129.54 <b>(+104.02%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>477.40 (n/a)</td><td>397.48 (n/a)</td><td>404.40 (n/a)</td><td>333.10 (n/a)</td><td>63.49 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.11 <b>(+25.63%)</b></td><td>0.06 (-6.15%)</td><td>0.06 (-16.46%)</td><td>0.05 (+0.71%)</td><td>0.03 <b>(+70.61%)</b></td><td>524.40 (-0.70%)</td><td>419.82 (+12.38%)</td><td>444.80 (+19.70%)</td><td>217.20 <b>(-20.41%)</b></td><td>121.37 <b>(+26.07%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>528.10 (n/a)</td><td>373.56 (n/a)</td><td>371.60 (n/a)</td><td>272.90 (n/a)</td><td>96.27 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (-12.68%)</td><td>0.06 <b>(-21.66%)</b></td><td>0.06 <b>(-32.07%)</b></td><td>0.04 (-14.69%)</td><td>0.02 <b>(-28.50%)</b></td><td>698.60 (+17.23%)</td><td>473.66 <b>(+23.98%)</b></td><td>435.90 <b>(+47.21%)</b></td><td>310.10 (+14.51%)</td><td>142.89 (-0.23%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>595.90 (n/a)</td><td>382.04 (n/a)</td><td>296.10 (n/a)</td><td>270.80 (n/a)</td><td>143.22 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (-5.56%)</td><td>0.06 (-12.76%)</td><td>0.06 (+10.60%)</td><td>0.01 <b>(-72.41%)</b></td><td>0.03 <b>(+35.57%)</b></td><td>1921.60 <b>(+262.43%)</b></td><td>687.46 <b>(+67.66%)</b></td><td>416.10 (-9.60%)</td><td>277.30 (+5.92%)</td><td>692.86 <b>(+507.00%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>530.20 (n/a)</td><td>410.02 (n/a)</td><td>460.30 (n/a)</td><td>261.80 (n/a)</td><td>114.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.20 (-2.12%)</td><td>0.16 <b>(+28.08%)</b></td><td>0.17 <b>(+68.73%)</b></td><td>0.12 <b>(+33.47%)</b></td><td>0.03 <b>(-31.74%)</b></td><td>412.40 <b>(-25.07%)</b></td><td>314.04 <b>(-25.83%)</b></td><td>282.30 <b>(-40.73%)</b></td><td>251.80 (+2.15%)</td><td>65.32 <b>(-46.18%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>550.40 (n/a)</td><td>423.40 (n/a)</td><td>476.30 (n/a)</td><td>246.50 (n/a)</td><td>121.36 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.20 (+1.91%)</td><td>0.12 (-8.72%)</td><td>0.12 (-3.24%)</td><td>0.03 <b>(-43.43%)</b></td><td>0.07 <b>(+22.77%)</b></td><td>1793.10 <b>(+76.76%)</b></td><td>699.80 <b>(+42.26%)</b></td><td>420.90 (+3.34%)</td><td>247.70 (-1.90%)</td><td>641.05 <b>(+109.00%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>1014.40 (n/a)</td><td>491.92 (n/a)</td><td>407.30 (n/a)</td><td>252.50 (n/a)</td><td>306.73 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 <b>(-41.71%)</b></td><td>0.08 <b>(-47.22%)</b></td><td>0.09 <b>(-45.74%)</b></td><td>0.02 <b>(-77.53%)</b></td><td>0.04 (-10.66%)</td><td>2489.70 <b>(+344.99%)</b></td><td>909.70 <b>(+166.70%)</b></td><td>544.30 <b>(+84.32%)</b></td><td>421.40 <b>(+71.58%)</b></td><td>888.17 <b>(+599.35%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>559.50 (n/a)</td><td>341.10 (n/a)</td><td>295.30 (n/a)</td><td>245.60 (n/a)</td><td>127.00 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.22 (+8.73%)</td><td>0.15 (-11.51%)</td><td>0.12 <b>(-26.54%)</b></td><td>0.11 (-10.94%)</td><td>0.04 <b>(+59.01%)</b></td><td>438.10 (+12.30%)</td><td>356.72 (+17.49%)</td><td>403.50 <b>(+36.13%)</b></td><td>227.20 (-8.02%)</td><td>91.45 <b>(+65.09%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>390.10 (n/a)</td><td>303.62 (n/a)</td><td>296.40 (n/a)</td><td>247.00 (n/a)</td><td>55.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 (-0.58%)</td><td>0.13 (-5.67%)</td><td>0.14 (-5.60%)</td><td>0.08 (+4.21%)</td><td>0.04 (+0.75%)</td><td>631.40 (-4.04%)</td><td>413.12 (+5.30%)</td><td>350.20 (+5.93%)</td><td>297.40 (+0.57%)</td><td>137.44 (-8.20%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>658.00 (n/a)</td><td>392.32 (n/a)</td><td>330.60 (n/a)</td><td>295.70 (n/a)</td><td>149.72 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.34 <b>(+72.38%)</b></td><td>0.17 (+14.08%)</td><td>0.13 <b>(-25.01%)</b></td><td>0.10 (+2.61%)</td><td>0.10 <b>(+157.23%)</b></td><td>470.60 (-2.55%)</td><td>347.82 (+0.65%)</td><td>393.10 <b>(+33.34%)</b></td><td>144.60 <b>(-42.00%)</b></td><td>140.29 <b>(+45.69%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>482.90 (n/a)</td><td>345.56 (n/a)</td><td>294.80 (n/a)</td><td>249.30 (n/a)</td><td>96.30 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (-8.26%)</td><td>0.01 (+5.56%)</td><td>0.01 <b>(+55.68%)</b></td><td>0.00 (-9.54%)</td><td>0.00 (-14.93%)</td><td>547.90 (+10.55%)</td><td>338.54 (-6.81%)</td><td>278.80 <b>(-35.76%)</b></td><td>234.20 (+9.03%)</td><td>134.06 (+2.78%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.60 (n/a)</td><td>363.28 (n/a)</td><td>434.00 (n/a)</td><td>214.80 (n/a)</td><td>130.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (+19.42%)</td><td>0.01 (+11.37%)</td><td>0.01 <b>(+54.21%)</b></td><td>0.00 <b>(-58.27%)</b></td><td>0.01 <b>(+62.87%)</b></td><td>2030.20 <b>(+139.64%)</b></td><td>664.16 <b>(+53.00%)</b></td><td>262.50 <b>(-35.17%)</b></td><td>204.50 (-16.26%)</td><td>782.92 <b>(+218.87%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>847.20 (n/a)</td><td>434.08 (n/a)</td><td>404.90 (n/a)</td><td>244.20 (n/a)</td><td>245.53 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (+9.49%)</td><td>0.01 (+15.82%)</td><td>0.01 (+11.88%)</td><td>0.00 (+15.18%)</td><td>0.00 <b>(+22.07%)</b></td><td>537.20 (-13.17%)</td><td>341.96 (-11.96%)</td><td>261.20 (-10.61%)</td><td>210.80 (-8.67%)</td><td>158.52 (-6.85%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>618.70 (n/a)</td><td>388.40 (n/a)</td><td>292.20 (n/a)</td><td>230.80 (n/a)</td><td>170.18 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 <b>(+27.33%)</b></td><td>0.01 <b>(+40.00%)</b></td><td>0.01 <b>(+37.23%)</b></td><td>0.01 <b>(+91.15%)</b></td><td>0.00 (-19.97%)</td><td>302.60 <b>(-47.68%)</b></td><td>258.86 <b>(-33.77%)</b></td><td>261.50 <b>(-27.14%)</b></td><td>187.70 <b>(-21.50%)</b></td><td>44.56 <b>(-68.15%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>578.40 (n/a)</td><td>390.84 (n/a)</td><td>358.90 (n/a)</td><td>239.10 (n/a)</td><td>139.90 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (-12.35%)</td><td>0.01 (+13.56%)</td><td>0.01 <b>(+39.06%)</b></td><td>0.01 <b>(+24.84%)</b></td><td>0.00 <b>(-37.26%)</b></td><td>505.70 (-19.90%)</td><td>357.42 <b>(-21.68%)</b></td><td>375.00 <b>(-28.09%)</b></td><td>251.00 (+14.09%)</td><td>102.44 <b>(-46.56%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>631.30 (n/a)</td><td>456.34 (n/a)</td><td>521.50 (n/a)</td><td>220.00 (n/a)</td><td>191.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (+11.93%)</td><td>0.01 (+2.97%)</td><td>0.01 (-8.74%)</td><td>0.00 (-14.48%)</td><td>0.00 (+17.57%)</td><td>623.10 (+16.93%)</td><td>389.36 (-0.48%)</td><td>356.70 (+9.55%)</td><td>239.20 (-10.68%)</td><td>144.67 (+19.74%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>532.90 (n/a)</td><td>391.24 (n/a)</td><td>325.60 (n/a)</td><td>267.80 (n/a)</td><td>120.82 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 <b>(+31.20%)</b></td><td>0.02 <b>(+47.09%)</b></td><td>0.02 <b>(+56.72%)</b></td><td>0.01 <b>(+268.39%)</b></td><td>0.01 (-11.07%)</td><td>544.50 <b>(-72.85%)</b></td><td>326.84 <b>(-54.53%)</b></td><td>280.80 <b>(-36.18%)</b></td><td>206.00 <b>(-23.76%)</b></td><td>135.17 <b>(-81.52%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2005.80 (n/a)</td><td>718.82 (n/a)</td><td>440.00 (n/a)</td><td>270.20 (n/a)</td><td>731.48 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 <b>(+35.76%)</b></td><td>0.02 <b>(+38.88%)</b></td><td>0.02 <b>(+26.78%)</b></td><td>0.01 (+17.04%)</td><td>0.01 <b>(+33.51%)</b></td><td>484.30 (-14.56%)</td><td>271.12 <b>(-26.81%)</b></td><td>233.80 <b>(-21.12%)</b></td><td>174.60 <b>(-26.33%)</b></td><td>122.19 (-10.81%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.80 (n/a)</td><td>370.42 (n/a)</td><td>296.40 (n/a)</td><td>237.00 (n/a)</td><td>137.00 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 <b>(+24.10%)</b></td><td>0.02 <b>(+23.86%)</b></td><td>0.02 <b>(+53.80%)</b></td><td>0.01 (+2.71%)</td><td>0.01 (+12.02%)</td><td>555.50 (-2.65%)</td><td>305.14 (-18.31%)</td><td>260.90 <b>(-34.99%)</b></td><td>183.00 (-19.42%)</td><td>144.45 (+1.63%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.60 (n/a)</td><td>373.52 (n/a)</td><td>401.30 (n/a)</td><td>227.10 (n/a)</td><td>142.13 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 <b>(+21.48%)</b></td><td>0.02 <b>(+24.87%)</b></td><td>0.02 <b>(+28.11%)</b></td><td>0.01 <b>(+41.99%)</b></td><td>0.01 (-2.93%)</td><td>416.50 <b>(-29.57%)</b></td><td>309.58 <b>(-23.90%)</b></td><td>305.20 <b>(-21.92%)</b></td><td>199.40 (-17.67%)</td><td>81.67 <b>(-44.95%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.40 (n/a)</td><td>406.80 (n/a)</td><td>390.90 (n/a)</td><td>242.20 (n/a)</td><td>148.36 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (+2.75%)</td><td>0.01 (-12.50%)</td><td>0.01 <b>(-22.86%)</b></td><td>0.01 <b>(-20.67%)</b></td><td>0.01 (+6.61%)</td><td>797.90 <b>(+26.05%)</b></td><td>530.82 <b>(+22.17%)</b></td><td>552.70 <b>(+29.65%)</b></td><td>239.20 (-2.69%)</td><td>259.21 <b>(+36.89%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.00 (n/a)</td><td>434.48 (n/a)</td><td>426.30 (n/a)</td><td>245.80 (n/a)</td><td>189.35 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (+10.72%)</td><td>0.01 <b>(+21.75%)</b></td><td>0.01 (+13.61%)</td><td>0.01 <b>(+72.50%)</b></td><td>0.00 <b>(-22.52%)</b></td><td>565.20 <b>(-42.03%)</b></td><td>441.70 <b>(-26.50%)</b></td><td>418.40 (-11.99%)</td><td>298.00 (-9.70%)</td><td>113.45 <b>(-59.44%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>975.00 (n/a)</td><td>600.96 (n/a)</td><td>475.40 (n/a)</td><td>330.00 (n/a)</td><td>279.69 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 <b>(+21.85%)</b></td><td>0.03 (-15.08%)</td><td>0.03 <b>(-37.62%)</b></td><td>0.02 <b>(-22.72%)</b></td><td>0.01 <b>(+114.53%)</b></td><td>485.60 <b>(+29.42%)</b></td><td>365.12 <b>(+29.78%)</b></td><td>419.50 <b>(+60.30%)</b></td><td>194.30 (-17.91%)</td><td>127.27 <b>(+128.01%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>375.20 (n/a)</td><td>281.34 (n/a)</td><td>261.70 (n/a)</td><td>236.70 (n/a)</td><td>55.82 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (-5.37%)</td><td>0.03 (-3.74%)</td><td>0.04 <b>(+49.36%)</b></td><td>0.01 <b>(-76.05%)</b></td><td>0.01 <b>(+75.84%)</b></td><td>1991.90 <b>(+317.59%)</b></td><td>664.60 <b>(+72.61%)</b></td><td>287.30 <b>(-33.03%)</b></td><td>274.60 (+5.70%)</td><td>747.63 <b>(+664.05%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>477.00 (n/a)</td><td>385.04 (n/a)</td><td>429.00 (n/a)</td><td>259.80 (n/a)</td><td>97.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (-2.08%)</td><td>0.02 <b>(-22.32%)</b></td><td>0.02 <b>(-45.37%)</b></td><td>0.02 (-14.37%)</td><td>0.01 (+0.45%)</td><td>646.40 (+16.78%)</td><td>502.56 <b>(+29.69%)</b></td><td>561.40 <b>(+83.05%)</b></td><td>261.90 (+2.11%)</td><td>150.14 (+9.05%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>553.50 (n/a)</td><td>387.52 (n/a)</td><td>306.70 (n/a)</td><td>256.50 (n/a)</td><td>137.68 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 <b>(-29.76%)</b></td><td>0.03 (-7.91%)</td><td>0.03 (+19.76%)</td><td>0.02 (-1.65%)</td><td>0.01 <b>(-33.32%)</b></td><td>581.60 (+1.68%)</td><td>399.76 (+4.32%)</td><td>335.20 (-16.51%)</td><td>277.30 <b>(+42.42%)</b></td><td>141.90 (-1.19%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.00 (n/a)</td><td>383.20 (n/a)</td><td>401.50 (n/a)</td><td>194.70 (n/a)</td><td>143.61 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 <b>(+21.60%)</b></td><td>0.03 (+14.92%)</td><td>0.03 <b>(+29.72%)</b></td><td>0.02 <b>(+21.28%)</b></td><td>0.01 (+14.40%)</td><td>481.10 (-17.54%)</td><td>368.74 (-13.28%)</td><td>355.40 <b>(-22.91%)</b></td><td>242.80 (-17.78%)</td><td>100.08 (-16.76%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>583.40 (n/a)</td><td>425.20 (n/a)</td><td>461.00 (n/a)</td><td>295.30 (n/a)</td><td>120.24 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 <b>(+49.38%)</b></td><td>0.03 (+8.20%)</td><td>0.02 (+2.81%)</td><td>0.02 (-6.44%)</td><td>0.01 <b>(+147.25%)</b></td><td>580.80 (+6.88%)</td><td>451.90 (-1.86%)</td><td>458.30 (-2.74%)</td><td>256.90 <b>(-33.05%)</b></td><td>122.84 <b>(+71.61%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>543.40 (n/a)</td><td>460.46 (n/a)</td><td>471.20 (n/a)</td><td>383.70 (n/a)</td><td>71.58 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (-3.45%)</td><td>0.06 (-15.18%)</td><td>0.05 <b>(-36.77%)</b></td><td>0.04 (-8.25%)</td><td>0.02 (-0.75%)</td><td>565.60 (+9.00%)</td><td>417.08 (+18.78%)</td><td>447.40 <b>(+58.15%)</b></td><td>253.50 (+3.60%)</td><td>132.81 (+10.65%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>518.90 (n/a)</td><td>351.14 (n/a)</td><td>282.90 (n/a)</td><td>244.70 (n/a)</td><td>120.04 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (-13.25%)</td><td>0.06 (-11.13%)</td><td>0.07 (+2.97%)</td><td>0.04 <b>(-25.65%)</b></td><td>0.02 (+12.81%)</td><td>549.50 <b>(+34.48%)</b></td><td>360.12 (+17.57%)</td><td>286.50 (-2.88%)</td><td>248.00 (+15.24%)</td><td>127.59 <b>(+76.63%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>408.60 (n/a)</td><td>306.30 (n/a)</td><td>295.00 (n/a)</td><td>215.20 (n/a)</td><td>72.23 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (-0.48%)</td><td>0.05 (-18.48%)</td><td>0.05 <b>(-40.84%)</b></td><td>0.04 (+5.70%)</td><td>0.02 (-13.29%)</td><td>578.20 (-5.40%)</td><td>441.88 (+18.31%)</td><td>450.70 <b>(+68.99%)</b></td><td>241.00 (+0.50%)</td><td>144.84 (-13.55%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.20 (n/a)</td><td>373.50 (n/a)</td><td>266.70 (n/a)</td><td>239.80 (n/a)</td><td>167.54 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (+2.43%)</td><td>0.07 (+3.36%)</td><td>0.08 (+1.74%)</td><td>0.04 (+1.46%)</td><td>0.02 (+8.19%)</td><td>525.00 (-1.45%)</td><td>344.00 (-2.37%)</td><td>278.70 (-1.73%)</td><td>238.90 (-2.37%)</td><td>129.93 (+1.81%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>532.70 (n/a)</td><td>352.36 (n/a)</td><td>283.60 (n/a)</td><td>244.70 (n/a)</td><td>127.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 <b>(-21.56%)</b></td><td>0.05 (-19.33%)</td><td>0.05 <b>(-28.93%)</b></td><td>0.01 <b>(-65.83%)</b></td><td>0.03 (-0.58%)</td><td>1904.20 <b>(+192.68%)</b></td><td>676.28 <b>(+75.58%)</b></td><td>440.40 <b>(+40.70%)</b></td><td>240.00 <b>(+27.52%)</b></td><td>695.98 <b>(+286.60%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>650.60 (n/a)</td><td>385.16 (n/a)</td><td>313.00 (n/a)</td><td>188.20 (n/a)</td><td>180.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 <b>(-38.57%)</b></td><td>0.05 <b>(-21.58%)</b></td><td>0.05 (-19.88%)</td><td>0.03 <b>(+34.11%)</b></td><td>0.01 <b>(-70.12%)</b></td><td>610.70 <b>(-25.43%)</b></td><td>475.34 (+9.42%)</td><td>452.70 <b>(+24.81%)</b></td><td>390.10 <b>(+62.75%)</b></td><td>81.88 <b>(-64.21%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>819.00 (n/a)</td><td>434.42 (n/a)</td><td>362.70 (n/a)</td><td>239.70 (n/a)</td><td>228.74 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.20 (n/a)</td><td>366.92 (n/a)</td><td>286.60 (n/a)</td><td>236.90 (n/a)</td><td>163.93 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>273.50 (n/a)</td><td>243.64 (n/a)</td><td>252.50 (n/a)</td><td>192.40 (n/a)</td><td>30.69 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>465.00 (n/a)</td><td>300.68 (n/a)</td><td>246.40 (n/a)</td><td>206.80 (n/a)</td><td>109.18 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.10 (n/a)</td><td>364.52 (n/a)</td><td>360.40 (n/a)</td><td>227.90 (n/a)</td><td>121.75 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>564.10 (n/a)</td><td>359.30 (n/a)</td><td>353.90 (n/a)</td><td>236.00 (n/a)</td><td>130.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>557.10 (n/a)</td><td>438.48 (n/a)</td><td>446.80 (n/a)</td><td>264.00 (n/a)</td><td>108.47 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>595.30 (n/a)</td><td>382.64 (n/a)</td><td>295.60 (n/a)</td><td>250.80 (n/a)</td><td>156.51 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>611.20 (n/a)</td><td>389.24 (n/a)</td><td>405.50 (n/a)</td><td>231.20 (n/a)</td><td>159.47 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>479.70 (n/a)</td><td>403.40 (n/a)</td><td>468.40 (n/a)</td><td>263.10 (n/a)</td><td>99.91 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.20 (+1.78%)</td><td>0.14 (-12.32%)</td><td>0.16 (-7.21%)</td><td>0.03 <b>(-73.01%)</b></td><td>0.07 <b>(+75.04%)</b></td><td>1921.10 <b>(+270.58%)</b></td><td>622.00 <b>(+92.12%)</b></td><td>302.60 (+7.76%)</td><td>242.10 (-1.75%)</td><td>729.12 <b>(+548.92%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>518.40 (n/a)</td><td>323.76 (n/a)</td><td>280.80 (n/a)</td><td>246.40 (n/a)</td><td>112.36 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>567.10 (n/a)</td><td>437.74 (n/a)</td><td>452.00 (n/a)</td><td>273.20 (n/a)</td><td>105.36 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>501.90 (n/a)</td><td>428.46 (n/a)</td><td>466.40 (n/a)</td><td>218.60 (n/a)</td><td>118.58 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1972.20 (n/a)</td><td>727.22 (n/a)</td><td>498.80 (n/a)</td><td>223.60 (n/a)</td><td>719.94 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>803.00 (n/a)</td><td>423.94 (n/a)</td><td>306.30 (n/a)</td><td>242.10 (n/a)</td><td>230.62 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1957.40 (n/a)</td><td>652.42 (n/a)</td><td>246.40 (n/a)</td><td>242.90 (n/a)</td><td>743.24 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.20 (n/a)</td><td>368.46 (n/a)</td><td>289.70 (n/a)</td><td>264.00 (n/a)</td><td>128.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.80 (n/a)</td><td>332.84 (n/a)</td><td>270.60 (n/a)</td><td>231.90 (n/a)</td><td>122.69 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1063.30 (n/a)</td><td>521.36 (n/a)</td><td>319.00 (n/a)</td><td>282.10 (n/a)</td><td>341.91 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>505.10 (n/a)</td><td>338.04 (n/a)</td><td>308.10 (n/a)</td><td>243.00 (n/a)</td><td>100.06 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>595.90 (n/a)</td><td>470.58 (n/a)</td><td>451.60 (n/a)</td><td>284.10 (n/a)</td><td>127.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>606.20 (n/a)</td><td>417.94 (n/a)</td><td>309.60 (n/a)</td><td>281.40 (n/a)</td><td>169.61 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>641.10 (n/a)</td><td>344.50 (n/a)</td><td>275.00 (n/a)</td><td>245.60 (n/a)</td><td>167.59 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>444.60 (n/a)</td><td>351.80 (n/a)</td><td>387.80 (n/a)</td><td>228.20 (n/a)</td><td>92.76 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>455.80 (n/a)</td><td>370.90 (n/a)</td><td>362.50 (n/a)</td><td>287.80 (n/a)</td><td>80.20 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.50 (n/a)</td><td>303.38 (n/a)</td><td>255.50 (n/a)</td><td>182.40 (n/a)</td><td>148.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>631.00 (n/a)</td><td>414.92 (n/a)</td><td>338.70 (n/a)</td><td>240.90 (n/a)</td><td>177.52 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>686.90 (n/a)</td><td>381.54 (n/a)</td><td>242.20 (n/a)</td><td>223.00 (n/a)</td><td>212.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.30 (n/a)</td><td>335.82 (n/a)</td><td>234.10 (n/a)</td><td>193.00 (n/a)</td><td>170.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.60 (n/a)</td><td>460.28 (n/a)</td><td>481.00 (n/a)</td><td>257.10 (n/a)</td><td>131.22 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>441.00 (n/a)</td><td>325.58 (n/a)</td><td>295.60 (n/a)</td><td>217.50 (n/a)</td><td>101.35 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>488.60 (n/a)</td><td>310.36 (n/a)</td><td>275.90 (n/a)</td><td>245.30 (n/a)</td><td>100.59 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.30 (n/a)</td><td>318.16 (n/a)</td><td>268.70 (n/a)</td><td>243.80 (n/a)</td><td>113.93 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>677.80 (n/a)</td><td>496.20 (n/a)</td><td>562.70 (n/a)</td><td>273.40 (n/a)</td><td>159.74 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.70 (n/a)</td><td>417.90 (n/a)</td><td>484.30 (n/a)</td><td>222.50 (n/a)</td><td>150.70 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>697.90 (n/a)</td><td>423.70 (n/a)</td><td>314.30 (n/a)</td><td>271.50 (n/a)</td><td>182.20 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>706.40 (n/a)</td><td>366.24 (n/a)</td><td>284.30 (n/a)</td><td>253.10 (n/a)</td><td>191.95 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>650.40 (n/a)</td><td>393.54 (n/a)</td><td>298.10 (n/a)</td><td>224.90 (n/a)</td><td>190.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>828.70 (n/a)</td><td>477.64 (n/a)</td><td>472.10 (n/a)</td><td>246.20 (n/a)</td><td>244.36 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.30 (n/a)</td><td>331.24 (n/a)</td><td>298.50 (n/a)</td><td>206.30 (n/a)</td><td>157.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1903.40 (n/a)</td><td>685.88 (n/a)</td><td>424.20 (n/a)</td><td>265.30 (n/a)</td><td>685.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>546.20 (n/a)</td><td>413.58 (n/a)</td><td>406.20 (n/a)</td><td>328.90 (n/a)</td><td>88.97 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>657.60 (n/a)</td><td>429.24 (n/a)</td><td>338.50 (n/a)</td><td>271.70 (n/a)</td><td>179.32 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>1928.60 (n/a)</td><td>795.18 (n/a)</td><td>516.90 (n/a)</td><td>179.30 (n/a)</td><td>722.28 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>653.60 (n/a)</td><td>496.06 (n/a)</td><td>552.00 (n/a)</td><td>266.40 (n/a)</td><td>154.87 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>598.90 (n/a)</td><td>423.18 (n/a)</td><td>440.40 (n/a)</td><td>240.60 (n/a)</td><td>170.31 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>485.10 (n/a)</td><td>372.94 (n/a)</td><td>396.80 (n/a)</td><td>276.00 (n/a)</td><td>91.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.57 (+8.35%)</td><td>0.42 (+1.37%)</td><td>0.38 (-6.65%)</td><td>0.26 <b>(-20.90%)</b></td><td>0.13 <b>(+73.49%)</b></td><td>857.20 <b>(+26.43%)</b></td><td>573.18 (+4.26%)</td><td>587.00 (+7.14%)</td><td>387.20 (-7.72%)</td><td>185.45 <b>(+102.39%)</b></td><td>24.37 (+8.35%)</td><td>17.81 (+1.37%)</td><td>16.08 (-6.65%)</td><td>11.01 <b>(-20.90%)</b></td><td>5.37 <b>(+73.49%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>678.00 (n/a)</td><td>549.74 (n/a)</td><td>547.90 (n/a)</td><td>419.60 (n/a)</td><td>91.63 (n/a)</td><td>22.49 (n/a)</td><td>17.57 (n/a)</td><td>17.22 (n/a)</td><td>13.92 (n/a)</td><td>3.09 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.61 (+17.84%)</td><td>0.47 (+15.98%)</td><td>0.49 (+8.17%)</td><td>0.31 <b>(+97.21%)</b></td><td>0.11 <b>(-22.17%)</b></td><td>708.80 <b>(-49.29%)</b></td><td>491.84 <b>(-25.14%)</b></td><td>455.90 (-7.54%)</td><td>363.40 (-15.13%)</td><td>132.83 <b>(-67.99%)</b></td><td>25.97 (+17.84%)</td><td>20.19 (+15.98%)</td><td>20.70 (+8.17%)</td><td>13.32 <b>(+97.21%)</b></td><td>4.73 <b>(-22.17%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.52 (n/a)</td><td>0.41 (n/a)</td><td>0.45 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>1397.70 (n/a)</td><td>657.00 (n/a)</td><td>493.10 (n/a)</td><td>428.20 (n/a)</td><td>414.95 (n/a)</td><td>22.04 (n/a)</td><td>17.41 (n/a)</td><td>19.14 (n/a)</td><td>6.75 (n/a)</td><td>6.08 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.30 (-0.62%)</td><td>0.30 (+0.55%)</td><td>0.30 (+1.81%)</td><td>0.29 (+0.41%)</td><td>0.00 <b>(-22.76%)</b></td><td>85451.40 (-0.41%)</td><td>83721.64 (-0.55%)</td><td>83010.80 (-1.78%)</td><td>82628.60 (+0.62%)</td><td>1270.66 <b>(-22.74%)</b></td><td>207.92 (-0.62%)</td><td>205.24 (+0.55%)</td><td>206.96 (+1.81%)</td><td>201.05 (+0.41%)</td><td>3.09 <b>(-22.76%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85799.70 (n/a)</td><td>84188.60 (n/a)</td><td>84511.00 (n/a)</td><td>82116.10 (n/a)</td><td>1644.72 (n/a)</td><td>209.21 (n/a)</td><td>204.13 (n/a)</td><td>203.29 (n/a)</td><td>200.23 (n/a)</td><td>4.01 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>1.05 (+1.84%)</td><td>1.01 (-0.58%)</td><td>1.02 (+0.22%)</td><td>0.92 (-6.53%)</td><td>0.05 <b>(+157.75%)</b></td><td>27478.40 (+6.98%)</td><td>25048.80 (+0.79%)</td><td>24595.90 (-0.22%)</td><td>23949.30 (-1.81%)</td><td>1396.47 <b>(+173.22%)</b></td><td>717.34 (+1.84%)</td><td>687.46 (-0.58%)</td><td>698.49 (+0.22%)</td><td>625.21 (-6.53%)</td><td>36.04 <b>(+157.75%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25685.20 (n/a)</td><td>24852.84 (n/a)</td><td>24649.50 (n/a)</td><td>24389.60 (n/a)</td><td>511.12 (n/a)</td><td>704.39 (n/a)</td><td>691.49 (n/a)</td><td>696.97 (n/a)</td><td>668.86 (n/a)</td><td>13.98 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.81 (-0.97%)</td><td>0.81 (-0.22%)</td><td>0.81 (+0.27%)</td><td>0.80 (-0.70%)</td><td>0.01 (-16.77%)</td><td>94431.40 (+0.70%)</td><td>93213.82 (+0.22%)</td><td>92924.90 (-0.26%)</td><td>92684.40 (+0.98%)</td><td>712.54 (-15.38%)</td><td>741.44 (-0.97%)</td><td>737.26 (-0.22%)</td><td>739.52 (+0.27%)</td><td>727.72 (-0.70%)</td><td>5.59 (-16.77%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.01 (n/a)</td><td>93772.70 (n/a)</td><td>93009.86 (n/a)</td><td>93171.30 (n/a)</td><td>91787.60 (n/a)</td><td>842.06 (n/a)</td><td>748.68 (n/a)</td><td>738.89 (n/a)</td><td>737.56 (n/a)</td><td>732.83 (n/a)</td><td>6.72 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.77 (-0.38%)</td><td>0.76 (-0.74%)</td><td>0.76 (-1.32%)</td><td>0.76 (-0.13%)</td><td>0.01 (+3.62%)</td><td>99443.10 (+0.13%)</td><td>98897.74 (+0.75%)</td><td>99401.00 (+1.34%)</td><td>97991.40 (+0.38%)</td><td>715.56 (+4.18%)</td><td>701.28 (-0.38%)</td><td>694.88 (-0.74%)</td><td>691.34 (-1.32%)</td><td>691.04 (-0.13%)</td><td>5.04 (+3.62%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99314.50 (n/a)</td><td>98161.70 (n/a)</td><td>98090.70 (n/a)</td><td>97620.10 (n/a)</td><td>686.86 (n/a)</td><td>703.95 (n/a)</td><td>700.09 (n/a)</td><td>700.57 (n/a)</td><td>691.94 (n/a)</td><td>4.87 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.80 (+0.10%)</td><td>0.79 (-1.07%)</td><td>0.79 (-1.62%)</td><td>0.78 (-1.79%)</td><td>0.01 <b>(+586.28%)</b></td><td>96261.40 (+1.82%)</td><td>95371.54 (+1.09%)</td><td>95902.40 (+1.64%)</td><td>94083.50 (-0.10%)</td><td>945.67 <b>(+598.04%)</b></td><td>730.41 (+0.10%)</td><td>720.60 (-1.07%)</td><td>716.56 (-1.62%)</td><td>713.88 (-1.79%)</td><td>7.18 <b>(+586.28%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94538.80 (n/a)</td><td>94346.14 (n/a)</td><td>94353.10 (n/a)</td><td>94173.10 (n/a)</td><td>135.47 (n/a)</td><td>729.71 (n/a)</td><td>728.38 (n/a)</td><td>728.32 (n/a)</td><td>726.89 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>5.44 (+0.02%)</td><td>4.04 (+16.13%)</td><td>3.92 (+7.84%)</td><td>2.65 <b>(+23.40%)</b></td><td>1.37 (+0.14%)</td><td>3357.80 (-18.96%)</td><td>2433.14 (-16.35%)</td><td>2276.20 (-7.27%)</td><td>1638.10 (-0.02%)</td><td>838.50 <b>(-25.72%)</b></td><td>327.74 (+0.02%)</td><td>243.16 (+16.13%)</td><td>235.87 (+7.84%)</td><td>159.89 <b>(+23.40%)</b></td><td>82.64 (+0.14%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.44 (n/a)</td><td>3.48 (n/a)</td><td>3.63 (n/a)</td><td>2.15 (n/a)</td><td>1.37 (n/a)</td><td>4143.40 (n/a)</td><td>2908.76 (n/a)</td><td>2454.60 (n/a)</td><td>1638.40 (n/a)</td><td>1128.91 (n/a)</td><td>327.67 (n/a)</td><td>209.38 (n/a)</td><td>218.72 (n/a)</td><td>129.57 (n/a)</td><td>82.53 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>4.77 (-2.04%)</td><td>3.63 (+12.95%)</td><td>3.60 <b>(+25.60%)</b></td><td>2.26 (+2.71%)</td><td>1.11 (+9.85%)</td><td>3937.70 (-2.64%)</td><td>2671.06 (-10.21%)</td><td>2477.90 <b>(-20.38%)</b></td><td>1868.60 (+2.09%)</td><td>884.62 (+8.82%)</td><td>287.31 (-2.04%)</td><td>218.43 (+12.95%)</td><td>216.66 <b>(+25.60%)</b></td><td>136.34 (+2.71%)</td><td>67.11 (+9.85%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>4.87 (n/a)</td><td>3.21 (n/a)</td><td>2.86 (n/a)</td><td>2.20 (n/a)</td><td>1.01 (n/a)</td><td>4044.30 (n/a)</td><td>2974.84 (n/a)</td><td>3112.30 (n/a)</td><td>1830.40 (n/a)</td><td>812.90 (n/a)</td><td>293.31 (n/a)</td><td>193.38 (n/a)</td><td>172.50 (n/a)</td><td>132.75 (n/a)</td><td>61.09 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>5.55 (-1.42%)</td><td>3.99 (+18.28%)</td><td>3.95 <b>(+37.75%)</b></td><td>2.15 (+9.34%)</td><td>1.51 (-1.86%)</td><td>4147.80 (-8.54%)</td><td>2548.62 (-17.27%)</td><td>2255.50 <b>(-27.40%)</b></td><td>1605.40 (+1.44%)</td><td>1076.62 (-13.81%)</td><td>334.42 (-1.42%)</td><td>240.35 (+18.28%)</td><td>238.03 <b>(+37.75%)</b></td><td>129.43 (+9.34%)</td><td>90.70 (-1.86%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.63 (n/a)</td><td>3.37 (n/a)</td><td>2.87 (n/a)</td><td>1.97 (n/a)</td><td>1.53 (n/a)</td><td>4535.30 (n/a)</td><td>3080.50 (n/a)</td><td>3106.90 (n/a)</td><td>1582.60 (n/a)</td><td>1249.06 (n/a)</td><td>339.24 (n/a)</td><td>203.20 (n/a)</td><td>172.80 (n/a)</td><td>118.38 (n/a)</td><td>92.42 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>6.46 (-4.69%)</td><td>5.65 (-0.49%)</td><td>5.94 (-6.38%)</td><td>3.87 (-5.89%)</td><td>1.04 (-10.58%)</td><td>9012.30 (+6.26%)</td><td>6394.58 (+0.18%)</td><td>5869.80 (+6.81%)</td><td>5400.40 (+4.92%)</td><td>1493.86 (+2.81%)</td><td>397.65 (-4.69%)</td><td>347.76 (-0.49%)</td><td>365.85 (-6.38%)</td><td>238.28 (-5.89%)</td><td>64.20 (-10.58%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>6.77 (n/a)</td><td>5.67 (n/a)</td><td>6.34 (n/a)</td><td>4.11 (n/a)</td><td>1.17 (n/a)</td><td>8481.50 (n/a)</td><td>6382.80 (n/a)</td><td>5495.30 (n/a)</td><td>5147.30 (n/a)</td><td>1453.07 (n/a)</td><td>417.21 (n/a)</td><td>349.46 (n/a)</td><td>390.78 (n/a)</td><td>253.20 (n/a)</td><td>71.79 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>5.74 (-2.12%)</td><td>4.51 (-4.45%)</td><td>4.44 (-2.90%)</td><td>3.74 (-11.65%)</td><td>0.80 (+19.83%)</td><td>9324.60 (+13.18%)</td><td>7908.62 (+5.65%)</td><td>7847.00 (+2.98%)</td><td>6077.60 (+2.17%)</td><td>1311.27 <b>(+40.45%)</b></td><td>353.34 (-2.12%)</td><td>278.03 (-4.45%)</td><td>273.67 (-2.90%)</td><td>230.30 (-11.65%)</td><td>49.34 (+19.83%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.86 (n/a)</td><td>4.72 (n/a)</td><td>4.58 (n/a)</td><td>4.23 (n/a)</td><td>0.67 (n/a)</td><td>8238.60 (n/a)</td><td>7485.68 (n/a)</td><td>7619.80 (n/a)</td><td>5948.70 (n/a)</td><td>933.63 (n/a)</td><td>361.00 (n/a)</td><td>290.97 (n/a)</td><td>281.83 (n/a)</td><td>260.66 (n/a)</td><td>41.18 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>6.38 (+9.83%)</td><td>5.45 (+6.02%)</td><td>5.22 (+6.60%)</td><td>4.59 (-5.02%)</td><td>0.71 <b>(+69.51%)</b></td><td>7596.90 (+5.28%)</td><td>6479.64 (-4.88%)</td><td>6679.50 (-6.19%)</td><td>5461.70 (-8.95%)</td><td>834.33 <b>(+60.76%)</b></td><td>393.19 (+9.83%)</td><td>335.88 (+6.02%)</td><td>321.50 (+6.60%)</td><td>282.68 (-5.02%)</td><td>43.53 <b>(+69.51%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.81 (n/a)</td><td>5.14 (n/a)</td><td>4.90 (n/a)</td><td>4.83 (n/a)</td><td>0.42 (n/a)</td><td>7215.90 (n/a)</td><td>6812.40 (n/a)</td><td>7120.30 (n/a)</td><td>5998.40 (n/a)</td><td>518.99 (n/a)</td><td>358.01 (n/a)</td><td>316.80 (n/a)</td><td>301.60 (n/a)</td><td>297.60 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.78 (+1.19%)</td><td>0.77 (+1.26%)</td><td>0.77 (+1.40%)</td><td>0.76 (+1.39%)</td><td>0.01 (+4.35%)</td><td>99505.60 (-1.37%)</td><td>97876.96 (-1.24%)</td><td>97983.80 (-1.38%)</td><td>96365.40 (-1.18%)</td><td>1372.97 (+1.69%)</td><td>713.11 (+1.19%)</td><td>702.21 (+1.26%)</td><td>701.34 (+1.40%)</td><td>690.61 (+1.39%)</td><td>9.85 (+4.35%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100884.80 (n/a)</td><td>99105.74 (n/a)</td><td>99351.00 (n/a)</td><td>97512.10 (n/a)</td><td>1350.16 (n/a)</td><td>704.73 (n/a)</td><td>693.50 (n/a)</td><td>691.68 (n/a)</td><td>681.17 (n/a)</td><td>9.44 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.78 (+2.00%)</td><td>0.74 (-0.50%)</td><td>0.74 (-2.49%)</td><td>0.72 (-0.87%)</td><td>0.02 <b>(+46.71%)</b></td><td>104849.70 (+0.88%)</td><td>101703.62 (+0.53%)</td><td>102516.30 (+2.56%)</td><td>97321.20 (-1.96%)</td><td>2960.52 <b>(+44.84%)</b></td><td>706.11 (+2.00%)</td><td>676.15 (-0.50%)</td><td>670.33 (-2.49%)</td><td>655.41 (-0.87%)</td><td>19.97 <b>(+46.71%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.01 (n/a)</td><td>103939.70 (n/a)</td><td>101162.94 (n/a)</td><td>99960.30 (n/a)</td><td>99270.40 (n/a)</td><td>2044.06 (n/a)</td><td>692.25 (n/a)</td><td>679.51 (n/a)</td><td>687.47 (n/a)</td><td>661.15 (n/a)</td><td>13.61 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.81 (+0.20%)</td><td>0.80 (+0.12%)</td><td>0.80 (+0.74%)</td><td>0.79 (-0.54%)</td><td>0.01 <b>(+46.72%)</b></td><td>95314.90 (+0.55%)</td><td>94314.12 (-0.11%)</td><td>94038.00 (-0.74%)</td><td>93407.40 (-0.20%)</td><td>772.32 <b>(+47.25%)</b></td><td>735.70 (+0.20%)</td><td>728.66 (+0.12%)</td><td>730.76 (+0.74%)</td><td>720.97 (-0.54%)</td><td>5.96 <b>(+46.72%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94798.10 (n/a)</td><td>94422.34 (n/a)</td><td>94736.00 (n/a)</td><td>93594.10 (n/a)</td><td>524.48 (n/a)</td><td>734.23 (n/a)</td><td>727.81 (n/a)</td><td>725.38 (n/a)</td><td>724.90 (n/a)</td><td>4.06 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>3.27 (-16.52%)</td><td>2.27 (-14.05%)</td><td>2.34 (-7.62%)</td><td>1.34 (-5.36%)</td><td>0.89 (-13.07%)</td><td>6022.40 (+5.67%)</td><td>4080.60 (+16.77%)</td><td>3442.10 (+8.26%)</td><td>2467.00 (+19.79%)</td><td>1697.66 (+15.41%)</td><td>856.88 (-16.52%)</td><td>594.11 (-14.05%)</td><td>614.15 (-7.62%)</td><td>351.01 (-5.36%)</td><td>232.21 (-13.07%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.91 (n/a)</td><td>2.64 (n/a)</td><td>2.54 (n/a)</td><td>1.41 (n/a)</td><td>1.02 (n/a)</td><td>5699.50 (n/a)</td><td>3494.68 (n/a)</td><td>3179.60 (n/a)</td><td>2059.40 (n/a)</td><td>1470.99 (n/a)</td><td>1026.47 (n/a)</td><td>691.22 (n/a)</td><td>664.83 (n/a)</td><td>370.90 (n/a)</td><td>267.13 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.32 (+15.79%)</td><td>0.23 (+6.75%)</td><td>0.18 (-8.93%)</td><td>0.18 (-1.95%)</td><td>0.06 <b>(+65.27%)</b></td><td>6868.70 (+1.99%)</td><td>5824.60 (-3.09%)</td><td>6790.10 (+9.80%)</td><td>3839.40 (-13.63%)</td><td>1415.23 <b>(+55.85%)</b></td><td>17.48 (+15.79%)</td><td>12.19 (+6.75%)</td><td>9.88 (-8.93%)</td><td>9.77 (-1.95%)</td><td>3.46 <b>(+65.27%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>6734.80 (n/a)</td><td>6010.30 (n/a)</td><td>6183.90 (n/a)</td><td>4445.50 (n/a)</td><td>908.08 (n/a)</td><td>15.10 (n/a)</td><td>11.42 (n/a)</td><td>10.85 (n/a)</td><td>9.96 (n/a)</td><td>2.09 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (-10.00%)</td><td>0.12 (-6.44%)</td><td>0.12 (-4.00%)</td><td>0.08 (-19.22%)</td><td>0.02 (+15.68%)</td><td>0.13 (-10.00%)</td><td>0.11 (-6.44%)</td><td>0.12 (-4.00%)</td><td>0.08 (-19.22%)</td><td>0.02 (+15.68%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>3.80 (-4.31%)</td><td>3.65 (-2.92%)</td><td>3.68 (-1.48%)</td><td>3.46 (-4.04%)</td><td>0.13 (-8.53%)</td><td>3.80 (-4.31%)</td><td>3.65 (-2.92%)</td><td>3.68 (-1.48%)</td><td>3.45 (-4.04%)</td><td>0.13 (-8.53%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.98 (n/a)</td><td>3.76 (n/a)</td><td>3.74 (n/a)</td><td>3.60 (n/a)</td><td>0.14 (n/a)</td><td>3.97 (n/a)</td><td>3.76 (n/a)</td><td>3.73 (n/a)</td><td>3.60 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>6.74 (-11.50%)</td><td>6.43 (-6.49%)</td><td>6.57 (-5.05%)</td><td>5.72 (-6.68%)</td><td>0.40 <b>(-44.34%)</b></td><td>6.73 (-11.50%)</td><td>6.42 (-6.49%)</td><td>6.57 (-5.05%)</td><td>5.72 (-6.68%)</td><td>0.40 <b>(-44.34%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.61 (n/a)</td><td>6.87 (n/a)</td><td>6.92 (n/a)</td><td>6.13 (n/a)</td><td>0.72 (n/a)</td><td>7.61 (n/a)</td><td>6.87 (n/a)</td><td>6.92 (n/a)</td><td>6.13 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>12.86 (-8.71%)</td><td>9.96 (-8.27%)</td><td>9.97 (-4.41%)</td><td>7.83 (-3.94%)</td><td>1.89 <b>(-32.19%)</b></td><td>12.85 (-8.71%)</td><td>9.96 (-8.27%)</td><td>9.96 (-4.41%)</td><td>7.82 (-3.94%)</td><td>1.88 <b>(-32.19%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>14.09 (n/a)</td><td>10.86 (n/a)</td><td>10.43 (n/a)</td><td>8.15 (n/a)</td><td>2.78 (n/a)</td><td>14.08 (n/a)</td><td>10.85 (n/a)</td><td>10.42 (n/a)</td><td>8.14 (n/a)</td><td>2.78 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>3.68 (-0.90%)</td><td>3.54 (+0.18%)</td><td>3.51 (+1.90%)</td><td>3.39 (+0.44%)</td><td>0.11 <b>(-34.10%)</b></td><td>3.68 (-0.90%)</td><td>3.53 (+0.18%)</td><td>3.51 (+1.90%)</td><td>3.39 (+0.44%)</td><td>0.11 <b>(-34.10%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.72 (n/a)</td><td>3.53 (n/a)</td><td>3.44 (n/a)</td><td>3.38 (n/a)</td><td>0.17 (n/a)</td><td>3.71 (n/a)</td><td>3.53 (n/a)</td><td>3.44 (n/a)</td><td>3.38 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>7.02 (-1.67%)</td><td>6.13 (-0.88%)</td><td>6.52 (+0.01%)</td><td>4.56 (-3.04%)</td><td>1.04 (+11.53%)</td><td>7.02 (-1.67%)</td><td>6.13 (-0.88%)</td><td>6.52 (+0.01%)</td><td>4.56 (-3.04%)</td><td>1.04 (+11.53%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.14 (n/a)</td><td>6.19 (n/a)</td><td>6.52 (n/a)</td><td>4.71 (n/a)</td><td>0.93 (n/a)</td><td>7.14 (n/a)</td><td>6.18 (n/a)</td><td>6.52 (n/a)</td><td>4.70 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>14.18 (+1.99%)</td><td>10.63 (-8.39%)</td><td>8.59 <b>(-28.47%)</b></td><td>8.27 (-13.10%)</td><td>3.06 <b>(+72.89%)</b></td><td>14.18 (+1.99%)</td><td>10.62 (-8.39%)</td><td>8.59 <b>(-28.47%)</b></td><td>8.26 (-13.10%)</td><td>3.06 <b>(+72.89%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>13.91 (n/a)</td><td>11.60 (n/a)</td><td>12.01 (n/a)</td><td>9.51 (n/a)</td><td>1.77 (n/a)</td><td>13.90 (n/a)</td><td>11.60 (n/a)</td><td>12.01 (n/a)</td><td>9.51 (n/a)</td><td>1.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.70 (n/a)</td><td>369.72 (n/a)</td><td>326.40 (n/a)</td><td>212.20 (n/a)</td><td>144.15 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>622.10 (n/a)</td><td>329.42 (n/a)</td><td>273.50 (n/a)</td><td>208.10 (n/a)</td><td>166.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.10 (n/a)</td><td>376.84 (n/a)</td><td>416.80 (n/a)</td><td>189.40 (n/a)</td><td>153.78 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>812.00 (n/a)</td><td>516.02 (n/a)</td><td>546.00 (n/a)</td><td>305.50 (n/a)</td><td>205.91 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>437.10 (n/a)</td><td>347.14 (n/a)</td><td>332.40 (n/a)</td><td>237.30 (n/a)</td><td>86.55 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>550.10 (n/a)</td><td>437.80 (n/a)</td><td>451.90 (n/a)</td><td>298.90 (n/a)</td><td>92.28 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>275.70 (n/a)</td><td>247.38 (n/a)</td><td>250.20 (n/a)</td><td>210.40 (n/a)</td><td>25.83 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.20 (n/a)</td><td>340.72 (n/a)</td><td>259.20 (n/a)</td><td>236.70 (n/a)</td><td>141.51 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.90 (n/a)</td><td>469.62 (n/a)</td><td>471.80 (n/a)</td><td>264.00 (n/a)</td><td>130.56 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>522.10 (n/a)</td><td>487.82 (n/a)</td><td>482.70 (n/a)</td><td>460.00 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.10 (n/a)</td><td>428.96 (n/a)</td><td>441.30 (n/a)</td><td>296.40 (n/a)</td><td>101.09 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.30 (n/a)</td><td>489.72 (n/a)</td><td>555.80 (n/a)</td><td>329.90 (n/a)</td><td>116.67 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>573.80 (n/a)</td><td>366.82 (n/a)</td><td>246.80 (n/a)</td><td>209.70 (n/a)</td><td>182.52 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>501.20 (n/a)</td><td>315.72 (n/a)</td><td>277.60 (n/a)</td><td>233.90 (n/a)</td><td>105.83 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>799.90 (n/a)</td><td>509.56 (n/a)</td><td>489.90 (n/a)</td><td>232.50 (n/a)</td><td>203.48 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>530.40 (n/a)</td><td>391.08 (n/a)</td><td>455.40 (n/a)</td><td>234.50 (n/a)</td><td>144.41 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>663.20 (n/a)</td><td>440.94 (n/a)</td><td>472.70 (n/a)</td><td>185.80 (n/a)</td><td>223.50 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1970.70 (n/a)</td><td>742.88 (n/a)</td><td>531.40 (n/a)</td><td>252.00 (n/a)</td><td>696.46 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (-9.21%)</td><td>0.11 (+6.24%)</td><td>0.11 (+9.26%)</td><td>0.09 <b>(+29.12%)</b></td><td>0.01 <b>(-49.23%)</b></td><td>350.30 <b>(-22.55%)</b></td><td>303.38 (-8.92%)</td><td>300.50 (-8.47%)</td><td>260.30 (+10.16%)</td><td>33.58 <b>(-56.75%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>452.30 (n/a)</td><td>333.10 (n/a)</td><td>328.30 (n/a)</td><td>236.30 (n/a)</td><td>77.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>597.90 (n/a)</td><td>441.46 (n/a)</td><td>505.40 (n/a)</td><td>238.30 (n/a)</td><td>170.46 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>580.00 (n/a)</td><td>406.42 (n/a)</td><td>379.90 (n/a)</td><td>188.10 (n/a)</td><td>170.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>629.30 (n/a)</td><td>425.56 (n/a)</td><td>467.10 (n/a)</td><td>249.80 (n/a)</td><td>152.66 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>538.10 (n/a)</td><td>454.24 (n/a)</td><td>517.80 (n/a)</td><td>200.00 (n/a)</td><td>143.48 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>649.20 (n/a)</td><td>492.50 (n/a)</td><td>513.40 (n/a)</td><td>260.90 (n/a)</td><td>144.54 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-9.61%)</td><td>0.01 (-2.90%)</td><td>0.01 (+6.54%)</td><td>0.01 <b>(-26.00%)</b></td><td>0.00 (+7.61%)</td><td>577.20 <b>(+35.14%)</b></td><td>373.54 (+6.19%)</td><td>363.90 (-6.14%)</td><td>263.30 (+10.63%)</td><td>128.41 <b>(+51.69%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>427.10 (n/a)</td><td>351.78 (n/a)</td><td>387.70 (n/a)</td><td>238.00 (n/a)</td><td>84.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-11.52%)</td><td>0.01 (+12.78%)</td><td>0.02 (+9.53%)</td><td>0.01 <b>(+29.33%)</b></td><td>0.00 <b>(-42.79%)</b></td><td>409.80 <b>(-22.68%)</b></td><td>285.20 (-19.17%)</td><td>252.10 (-8.69%)</td><td>237.10 (+13.07%)</td><td>70.99 <b>(-51.17%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>530.00 (n/a)</td><td>352.86 (n/a)</td><td>276.10 (n/a)</td><td>209.70 (n/a)</td><td>145.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (+15.12%)</td><td>0.01 (+12.89%)</td><td>0.01 <b>(+35.78%)</b></td><td>0.01 <b>(+37.12%)</b></td><td>0.00 (+1.12%)</td><td>603.40 <b>(-27.08%)</b></td><td>413.70 (-15.15%)</td><td>360.10 <b>(-26.34%)</b></td><td>234.20 (-13.13%)</td><td>157.82 <b>(-29.74%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>827.50 (n/a)</td><td>487.58 (n/a)</td><td>488.90 (n/a)</td><td>269.60 (n/a)</td><td>224.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (+1.74%)</td><td>0.01 (-15.72%)</td><td>0.01 <b>(-34.82%)</b></td><td>0.01 (+8.56%)</td><td>0.00 (+16.34%)</td><td>530.80 (-7.88%)</td><td>429.32 <b>(+20.61%)</b></td><td>501.70 <b>(+53.43%)</b></td><td>236.30 (-1.71%)</td><td>130.66 (+1.72%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.20 (n/a)</td><td>355.96 (n/a)</td><td>327.00 (n/a)</td><td>240.40 (n/a)</td><td>128.46 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (+16.58%)</td><td>0.01 (+3.70%)</td><td>0.02 (+8.41%)</td><td>0.01 (-18.88%)</td><td>0.01 <b>(+60.05%)</b></td><td>674.80 <b>(+23.25%)</b></td><td>405.78 (+11.69%)</td><td>271.20 (-7.76%)</td><td>221.30 (-14.22%)</td><td>227.38 <b>(+76.33%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.50 (n/a)</td><td>363.32 (n/a)</td><td>294.00 (n/a)</td><td>258.00 (n/a)</td><td>128.96 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-16.51%)</td><td>0.01 (-17.33%)</td><td>0.01 (-13.86%)</td><td>0.01 <b>(-40.48%)</b></td><td>0.00 (+16.25%)</td><td>570.60 <b>(+68.02%)</b></td><td>335.08 <b>(+28.59%)</b></td><td>279.60 (+16.06%)</td><td>235.40 (+19.74%)</td><td>135.72 <b>(+144.05%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>339.60 (n/a)</td><td>260.58 (n/a)</td><td>240.90 (n/a)</td><td>196.60 (n/a)</td><td>55.61 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-8.99%)</td><td>0.01 (-10.50%)</td><td>0.01 <b>(-24.26%)</b></td><td>0.01 <b>(+43.06%)</b></td><td>0.00 <b>(-35.42%)</b></td><td>456.30 <b>(-30.10%)</b></td><td>340.50 (+0.16%)</td><td>341.20 <b>(+32.04%)</b></td><td>231.20 (+9.89%)</td><td>85.14 <b>(-53.08%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>652.80 (n/a)</td><td>339.94 (n/a)</td><td>258.40 (n/a)</td><td>210.40 (n/a)</td><td>181.45 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-16.53%)</td><td>0.01 <b>(-22.00%)</b></td><td>0.01 <b>(-22.82%)</b></td><td>0.01 <b>(-30.43%)</b></td><td>0.00 (+3.70%)</td><td>812.90 <b>(+43.72%)</b></td><td>440.38 <b>(+36.81%)</b></td><td>355.80 <b>(+29.57%)</b></td><td>267.70 (+19.83%)</td><td>227.91 <b>(+63.28%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.60 (n/a)</td><td>321.88 (n/a)</td><td>274.60 (n/a)</td><td>223.40 (n/a)</td><td>139.58 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-8.49%)</td><td>0.01 (-16.23%)</td><td>0.01 (-13.29%)</td><td>0.01 <b>(-26.97%)</b></td><td>0.00 (-3.07%)</td><td>602.50 <b>(+36.93%)</b></td><td>414.72 <b>(+21.95%)</b></td><td>410.30 (+15.32%)</td><td>247.90 (+9.30%)</td><td>132.74 <b>(+42.25%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>440.00 (n/a)</td><td>340.08 (n/a)</td><td>355.80 (n/a)</td><td>226.80 (n/a)</td><td>93.32 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-0.41%)</td><td>0.02 <b>(+47.67%)</b></td><td>0.02 <b>(+63.84%)</b></td><td>0.01 <b>(+88.50%)</b></td><td>0.00 <b>(-60.23%)</b></td><td>324.10 <b>(-46.96%)</b></td><td>272.90 <b>(-39.27%)</b></td><td>266.40 <b>(-38.96%)</b></td><td>246.30 (+0.41%)</td><td>32.13 <b>(-80.03%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.00 (n/a)</td><td>449.36 (n/a)</td><td>436.40 (n/a)</td><td>245.30 (n/a)</td><td>160.90 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (+9.03%)</td><td>0.01 <b>(+43.23%)</b></td><td>0.01 <b>(+87.59%)</b></td><td>0.01 <b>(+36.23%)</b></td><td>0.00 (+9.06%)</td><td>624.90 <b>(-26.59%)</b></td><td>394.78 <b>(-31.12%)</b></td><td>303.70 <b>(-46.69%)</b></td><td>269.20 (-8.28%)</td><td>154.44 <b>(-23.07%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>851.30 (n/a)</td><td>573.16 (n/a)</td><td>569.70 (n/a)</td><td>293.50 (n/a)</td><td>200.76 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (+17.80%)</td><td>0.01 <b>(+27.01%)</b></td><td>0.01 <b>(+27.85%)</b></td><td>0.01 <b>(+49.92%)</b></td><td>0.00 (+1.15%)</td><td>551.40 <b>(-33.29%)</b></td><td>404.52 <b>(-24.34%)</b></td><td>377.60 <b>(-21.79%)</b></td><td>264.70 (-15.11%)</td><td>108.39 <b>(-43.09%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>826.60 (n/a)</td><td>534.62 (n/a)</td><td>482.80 (n/a)</td><td>311.80 (n/a)</td><td>190.47 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 <b>(+21.16%)</b></td><td>0.03 <b>(+61.13%)</b></td><td>0.03 <b>(+21.00%)</b></td><td>0.03 <b>(+729.39%)</b></td><td>0.00 <b>(-78.68%)</b></td><td>250.70 <b>(-87.94%)</b></td><td>236.82 <b>(-65.25%)</b></td><td>245.40 (-17.37%)</td><td>219.40 (-17.46%)</td><td>15.79 <b>(-97.99%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2079.00 (n/a)</td><td>681.42 (n/a)</td><td>297.00 (n/a)</td><td>265.80 (n/a)</td><td>785.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (+14.53%)</td><td>0.03 <b>(+31.57%)</b></td><td>0.03 <b>(+49.48%)</b></td><td>0.02 (-3.56%)</td><td>0.01 <b>(+43.14%)</b></td><td>504.00 (+3.68%)</td><td>311.64 <b>(-21.21%)</b></td><td>279.30 <b>(-33.12%)</b></td><td>238.40 (-12.67%)</td><td>109.97 <b>(+38.61%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>486.10 (n/a)</td><td>395.54 (n/a)</td><td>417.60 (n/a)</td><td>273.00 (n/a)</td><td>79.34 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (+1.18%)</td><td>0.03 <b>(+42.00%)</b></td><td>0.03 <b>(+104.41%)</b></td><td>0.02 <b>(+64.57%)</b></td><td>0.01 <b>(-28.64%)</b></td><td>432.50 <b>(-39.24%)</b></td><td>306.90 <b>(-36.13%)</b></td><td>266.00 <b>(-51.08%)</b></td><td>238.70 (-1.20%)</td><td>81.64 <b>(-56.18%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>711.80 (n/a)</td><td>480.48 (n/a)</td><td>543.70 (n/a)</td><td>241.60 (n/a)</td><td>186.30 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (+10.13%)</td><td>0.03 (+0.44%)</td><td>0.03 (+6.48%)</td><td>0.02 (-18.25%)</td><td>0.01 <b>(+64.34%)</b></td><td>430.70 <b>(+22.32%)</b></td><td>310.98 (+2.16%)</td><td>296.30 (-6.09%)</td><td>239.20 (-9.19%)</td><td>72.49 <b>(+92.46%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>352.10 (n/a)</td><td>304.40 (n/a)</td><td>315.50 (n/a)</td><td>263.40 (n/a)</td><td>37.66 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 <b>(+56.37%)</b></td><td>0.03 <b>(+77.40%)</b></td><td>0.03 <b>(+117.97%)</b></td><td>0.01 <b>(+27.36%)</b></td><td>0.01 <b>(+117.73%)</b></td><td>554.80 <b>(-21.48%)</b></td><td>312.18 <b>(-39.78%)</b></td><td>236.70 <b>(-54.13%)</b></td><td>226.80 <b>(-36.06%)</b></td><td>140.11 (+10.08%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>706.60 (n/a)</td><td>518.36 (n/a)</td><td>516.00 (n/a)</td><td>354.70 (n/a)</td><td>127.28 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 <b>(+106.40%)</b></td><td>0.03 <b>(+76.85%)</b></td><td>0.03 <b>(+104.06%)</b></td><td>0.02 <b>(+31.48%)</b></td><td>0.01 <b>(+331.65%)</b></td><td>477.80 <b>(-23.94%)</b></td><td>326.60 <b>(-36.73%)</b></td><td>248.10 <b>(-51.00%)</b></td><td>200.40 <b>(-51.56%)</b></td><td>135.26 <b>(+71.73%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>628.20 (n/a)</td><td>516.18 (n/a)</td><td>506.30 (n/a)</td><td>413.70 (n/a)</td><td>78.76 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (+4.40%)</td><td>0.02 (+14.76%)</td><td>0.02 (+5.82%)</td><td>0.01 (+14.86%)</td><td>0.01 (+19.43%)</td><td>564.50 (-12.93%)</td><td>420.28 (-11.60%)</td><td>474.90 (-5.49%)</td><td>278.20 (-4.20%)</td><td>128.40 (-1.13%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>648.30 (n/a)</td><td>475.44 (n/a)</td><td>502.50 (n/a)</td><td>290.40 (n/a)</td><td>129.86 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 <b>(+30.66%)</b></td><td>0.03 <b>(+39.09%)</b></td><td>0.03 <b>(+71.76%)</b></td><td>0.02 <b>(+20.92%)</b></td><td>0.01 <b>(+62.37%)</b></td><td>468.20 (-17.29%)</td><td>332.96 <b>(-25.09%)</b></td><td>263.90 <b>(-41.80%)</b></td><td>223.10 <b>(-23.46%)</b></td><td>116.70 (+10.75%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.10 (n/a)</td><td>444.50 (n/a)</td><td>453.40 (n/a)</td><td>291.50 (n/a)</td><td>105.37 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (-2.88%)</td><td>0.02 (+19.53%)</td><td>0.02 <b>(+47.07%)</b></td><td>0.01 (-9.47%)</td><td>0.01 (-3.55%)</td><td>606.90 (+10.47%)</td><td>387.28 (-15.83%)</td><td>357.20 <b>(-32.01%)</b></td><td>229.00 (+2.97%)</td><td>154.00 (+12.23%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.40 (n/a)</td><td>460.14 (n/a)</td><td>525.40 (n/a)</td><td>222.40 (n/a)</td><td>137.21 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (-5.44%)</td><td>0.02 (+9.78%)</td><td>0.02 <b>(+21.80%)</b></td><td>0.01 (-3.07%)</td><td>0.01 (-6.78%)</td><td>564.60 (+3.16%)</td><td>415.30 (-8.74%)</td><td>402.80 (-17.88%)</td><td>250.10 (+5.75%)</td><td>139.13 (+11.19%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.30 (n/a)</td><td>455.06 (n/a)</td><td>490.50 (n/a)</td><td>236.50 (n/a)</td><td>125.12 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (-1.78%)</td><td>0.02 (-5.78%)</td><td>0.02 (-1.47%)</td><td>0.01 (+3.64%)</td><td>0.01 (-7.58%)</td><td>638.50 (-3.51%)</td><td>496.82 (+4.29%)</td><td>515.90 (+1.50%)</td><td>283.60 (+1.79%)</td><td>134.01 (-12.64%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>661.70 (n/a)</td><td>476.38 (n/a)</td><td>508.30 (n/a)</td><td>278.60 (n/a)</td><td>153.40 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-2.20%)</td><td>0.02 (+3.61%)</td><td>0.02 (+10.91%)</td><td>0.01 (+0.13%)</td><td>0.00 (-16.30%)</td><td>679.60 (-0.13%)</td><td>505.68 (-5.20%)</td><td>483.80 (-9.84%)</td><td>358.80 (+2.25%)</td><td>115.97 (-16.12%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>680.50 (n/a)</td><td>533.44 (n/a)</td><td>536.60 (n/a)</td><td>350.90 (n/a)</td><td>138.25 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (+10.93%)</td><td>0.05 (-6.63%)</td><td>0.04 <b>(-20.69%)</b></td><td>0.04 (+9.74%)</td><td>0.02 <b>(+24.96%)</b></td><td>437.50 (-8.87%)</td><td>344.22 (+9.15%)</td><td>395.00 <b>(+26.08%)</b></td><td>192.80 (-9.86%)</td><td>101.78 (+0.22%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>480.10 (n/a)</td><td>315.36 (n/a)</td><td>313.30 (n/a)</td><td>213.90 (n/a)</td><td>101.55 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (+0.70%)</td><td>0.05 (+14.80%)</td><td>0.06 <b>(+54.31%)</b></td><td>0.03 (-14.79%)</td><td>0.02 (+19.10%)</td><td>646.90 (+17.36%)</td><td>376.60 (-8.35%)</td><td>279.90 <b>(-35.19%)</b></td><td>243.60 (-0.69%)</td><td>176.59 <b>(+31.20%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>551.20 (n/a)</td><td>410.92 (n/a)</td><td>431.90 (n/a)</td><td>245.30 (n/a)</td><td>134.60 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (+12.00%)</td><td>0.04 (-15.47%)</td><td>0.03 <b>(-42.21%)</b></td><td>0.02 <b>(-21.79%)</b></td><td>0.02 <b>(+34.74%)</b></td><td>709.40 <b>(+27.84%)</b></td><td>469.68 <b>(+26.71%)</b></td><td>524.00 <b>(+73.05%)</b></td><td>228.50 (-10.74%)</td><td>183.48 <b>(+46.38%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>554.90 (n/a)</td><td>370.68 (n/a)</td><td>302.80 (n/a)</td><td>256.00 (n/a)</td><td>125.34 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.06 (-6.40%)</td><td>0.04 (-18.47%)</td><td>0.05 (-5.88%)</td><td>0.01 <b>(-71.11%)</b></td><td>0.02 <b>(+56.49%)</b></td><td>1839.00 <b>(+246.13%)</b></td><td>646.22 <b>(+88.92%)</b></td><td>306.40 (+6.28%)</td><td>273.80 (+6.83%)</td><td>674.36 <b>(+488.32%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>531.30 (n/a)</td><td>342.06 (n/a)</td><td>288.30 (n/a)</td><td>256.30 (n/a)</td><td>114.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.06 (-15.78%)</td><td>0.04 (-8.38%)</td><td>0.04 (+10.96%)</td><td>0.03 (-10.76%)</td><td>0.01 <b>(-33.47%)</b></td><td>619.90 (+12.06%)</td><td>416.88 (+2.03%)</td><td>432.90 (-9.87%)</td><td>257.90 (+18.74%)</td><td>139.45 (-14.19%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>553.20 (n/a)</td><td>408.58 (n/a)</td><td>480.30 (n/a)</td><td>217.20 (n/a)</td><td>162.50 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 <b>(+46.41%)</b></td><td>0.05 (+1.18%)</td><td>0.04 <b>(-21.45%)</b></td><td>0.03 (-11.11%)</td><td>0.02 <b>(+92.93%)</b></td><td>513.60 (+12.51%)</td><td>365.32 (+5.69%)</td><td>378.60 <b>(+27.30%)</b></td><td>187.00 <b>(-31.70%)</b></td><td>118.14 <b>(+38.36%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>456.50 (n/a)</td><td>345.64 (n/a)</td><td>297.40 (n/a)</td><td>273.80 (n/a)</td><td>85.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 <b>(+20.53%)</b></td><td>0.05 (+16.40%)</td><td>0.03 (-4.72%)</td><td>0.02 (-5.64%)</td><td>0.03 <b>(+46.50%)</b></td><td>670.10 (+5.98%)</td><td>437.52 (-5.20%)</td><td>500.00 (+4.95%)</td><td>196.30 (-17.07%)</td><td>197.91 <b>(+35.20%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>632.30 (n/a)</td><td>461.54 (n/a)</td><td>476.40 (n/a)</td><td>236.70 (n/a)</td><td>146.38 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (+15.01%)</td><td>0.06 <b>(+67.64%)</b></td><td>0.06 <b>(+86.49%)</b></td><td>0.04 <b>(+446.52%)</b></td><td>0.01 <b>(-40.08%)</b></td><td>384.20 <b>(-81.70%)</b></td><td>281.54 <b>(-62.82%)</b></td><td>271.20 <b>(-46.38%)</b></td><td>209.60 (-13.07%)</td><td>65.73 <b>(-91.36%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2099.60 (n/a)</td><td>757.24 (n/a)</td><td>505.80 (n/a)</td><td>241.10 (n/a)</td><td>760.61 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.06 (-11.96%)</td><td>0.04 (+6.09%)</td><td>0.04 (+4.41%)</td><td>0.03 <b>(+278.00%)</b></td><td>0.01 <b>(-56.96%)</b></td><td>537.80 <b>(-73.54%)</b></td><td>415.52 <b>(-42.27%)</b></td><td>405.20 (-4.23%)</td><td>293.30 (+13.55%)</td><td>90.36 <b>(-87.88%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2032.80 (n/a)</td><td>719.78 (n/a)</td><td>423.10 (n/a)</td><td>258.30 (n/a)</td><td>745.30 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 <b>(-21.18%)</b></td><td>0.04 (-7.38%)</td><td>0.04 (+9.71%)</td><td>0.03 (+11.56%)</td><td>0.01 <b>(-48.91%)</b></td><td>557.10 (-10.38%)</td><td>438.34 (+0.88%)</td><td>435.20 (-8.86%)</td><td>332.90 <b>(+26.87%)</b></td><td>86.94 <b>(-40.38%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>621.60 (n/a)</td><td>434.50 (n/a)</td><td>477.50 (n/a)</td><td>262.40 (n/a)</td><td>145.81 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (-9.79%)</td><td>0.04 (+2.74%)</td><td>0.04 (+17.41%)</td><td>0.03 (-3.57%)</td><td>0.01 <b>(-29.02%)</b></td><td>567.90 (+3.71%)</td><td>404.70 (-5.03%)</td><td>375.20 (-14.84%)</td><td>317.20 (+10.83%)</td><td>95.90 (-15.45%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>547.60 (n/a)</td><td>426.14 (n/a)</td><td>440.60 (n/a)</td><td>286.20 (n/a)</td><td>113.43 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 <b>(-32.14%)</b></td><td>0.03 <b>(-31.89%)</b></td><td>0.03 <b>(-45.38%)</b></td><td>0.03 (-6.50%)</td><td>0.01 <b>(-57.30%)</b></td><td>629.00 (+6.94%)</td><td>516.22 <b>(+33.04%)</b></td><td>532.70 <b>(+83.12%)</b></td><td>371.10 <b>(+47.38%)</b></td><td>115.76 <b>(-31.57%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.20 (n/a)</td><td>388.02 (n/a)</td><td>290.90 (n/a)</td><td>251.80 (n/a)</td><td>169.16 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 <b>(+26.16%)</b></td><td>0.07 (-15.35%)</td><td>0.06 <b>(-36.24%)</b></td><td>0.02 (-3.43%)</td><td>0.04 <b>(+22.14%)</b></td><td>1948.50 (+3.56%)</td><td>757.56 (+16.38%)</td><td>549.70 <b>(+56.83%)</b></td><td>233.60 <b>(-20.73%)</b></td><td>678.75 (-1.45%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1881.50 (n/a)</td><td>650.96 (n/a)</td><td>350.50 (n/a)</td><td>294.70 (n/a)</td><td>688.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (-17.03%)</td><td>0.12 (-0.14%)</td><td>0.12 (-6.06%)</td><td>0.10 <b>(+40.23%)</b></td><td>0.01 <b>(-65.98%)</b></td><td>331.20 <b>(-28.68%)</b></td><td>282.30 (-6.33%)</td><td>276.40 (+6.43%)</td><td>254.00 <b>(+20.55%)</b></td><td>29.04 <b>(-70.98%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>464.40 (n/a)</td><td>301.38 (n/a)</td><td>259.70 (n/a)</td><td>210.70 (n/a)</td><td>100.05 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.11 <b>(-33.36%)</b></td><td>0.08 <b>(-28.37%)</b></td><td>0.07 <b>(-42.34%)</b></td><td>0.06 (+3.18%)</td><td>0.02 <b>(-59.28%)</b></td><td>527.70 (-3.09%)</td><td>440.46 <b>(+22.79%)</b></td><td>464.20 <b>(+73.47%)</b></td><td>300.20 <b>(+50.02%)</b></td><td>86.16 <b>(-48.03%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>544.50 (n/a)</td><td>358.70 (n/a)</td><td>267.60 (n/a)</td><td>200.10 (n/a)</td><td>165.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 <b>(-42.63%)</b></td><td>0.10 <b>(-21.03%)</b></td><td>0.11 (-3.58%)</td><td>0.06 (-18.99%)</td><td>0.03 <b>(-49.50%)</b></td><td>559.00 <b>(+23.43%)</b></td><td>374.46 (+18.43%)</td><td>296.40 (+3.71%)</td><td>274.50 <b>(+74.29%)</b></td><td>127.57 (+1.24%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>452.90 (n/a)</td><td>316.20 (n/a)</td><td>285.80 (n/a)</td><td>157.50 (n/a)</td><td>126.00 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.16 (-4.84%)</td><td>0.09 (-5.24%)</td><td>0.08 <b>(-21.14%)</b></td><td>0.05 (-9.82%)</td><td>0.05 (+4.70%)</td><td>677.30 (+10.89%)</td><td>421.96 (+9.79%)</td><td>425.30 <b>(+26.80%)</b></td><td>201.90 (+5.10%)</td><td>193.10 <b>(+20.49%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>610.80 (n/a)</td><td>384.32 (n/a)</td><td>335.40 (n/a)</td><td>192.10 (n/a)</td><td>160.26 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (-15.47%)</td><td>0.09 <b>(-23.19%)</b></td><td>0.10 (-13.76%)</td><td>0.02 <b>(-70.11%)</b></td><td>0.05 (-0.88%)</td><td>1906.60 <b>(+234.61%)</b></td><td>650.60 <b>(+91.54%)</b></td><td>315.10 (+15.97%)</td><td>239.90 (+18.29%)</td><td>710.16 <b>(+334.83%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>569.80 (n/a)</td><td>339.66 (n/a)</td><td>271.70 (n/a)</td><td>202.80 (n/a)</td><td>163.32 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 <b>(-28.82%)</b></td><td>0.10 (+6.44%)</td><td>0.12 <b>(+49.88%)</b></td><td>0.03 <b>(-25.31%)</b></td><td>0.04 <b>(-29.16%)</b></td><td>1116.80 <b>(+33.88%)</b></td><td>442.56 (-3.26%)</td><td>280.80 <b>(-33.29%)</b></td><td>250.80 <b>(+40.50%)</b></td><td>377.21 <b>(+44.53%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>834.20 (n/a)</td><td>457.46 (n/a)</td><td>420.90 (n/a)</td><td>178.50 (n/a)</td><td>261.00 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (+6.24%)</td><td>0.09 (-11.05%)</td><td>0.11 (+8.62%)</td><td>0.01 <b>(-83.28%)</b></td><td>0.05 <b>(+105.70%)</b></td><td>2519.80 <b>(+498.10%)</b></td><td>757.74 <b>(+127.32%)</b></td><td>288.60 (-7.91%)</td><td>226.30 (-5.87%)</td><td>989.71 <b>(+1116.69%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>421.30 (n/a)</td><td>333.34 (n/a)</td><td>313.40 (n/a)</td><td>240.40 (n/a)</td><td>81.34 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 <b>(+53.68%)</b></td><td>0.11 <b>(+34.11%)</b></td><td>0.11 <b>(+52.30%)</b></td><td>0.06 (-4.54%)</td><td>0.05 <b>(+109.84%)</b></td><td>567.20 (+4.75%)</td><td>343.50 (-17.43%)</td><td>286.50 <b>(-34.35%)</b></td><td>193.60 <b>(-34.92%)</b></td><td>156.12 <b>(+48.19%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>541.50 (n/a)</td><td>416.00 (n/a)</td><td>436.40 (n/a)</td><td>297.50 (n/a)</td><td>105.35 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (-5.84%)</td><td>0.10 (+6.63%)</td><td>0.12 <b>(+50.91%)</b></td><td>0.06 (-12.89%)</td><td>0.03 <b>(+23.15%)</b></td><td>551.80 (+14.79%)</td><td>368.76 (-1.02%)</td><td>267.00 <b>(-33.75%)</b></td><td>253.00 (+6.21%)</td><td>148.00 <b>(+50.80%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>480.70 (n/a)</td><td>372.56 (n/a)</td><td>403.00 (n/a)</td><td>238.20 (n/a)</td><td>98.15 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (+19.04%)</td><td>0.09 <b>(+20.67%)</b></td><td>0.08 (-14.84%)</td><td>0.07 <b>(+66.95%)</b></td><td>0.03 (-3.15%)</td><td>462.90 <b>(-40.10%)</b></td><td>369.86 <b>(-22.57%)</b></td><td>421.40 (+17.41%)</td><td>244.50 (-16.01%)</td><td>98.19 <b>(-52.01%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>772.80 (n/a)</td><td>477.68 (n/a)</td><td>358.90 (n/a)</td><td>291.10 (n/a)</td><td>204.62 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 <b>(-37.04%)</b></td><td>0.09 (-10.29%)</td><td>0.10 (+19.70%)</td><td>0.05 (+5.34%)</td><td>0.03 <b>(-43.41%)</b></td><td>630.40 (-5.07%)</td><td>395.78 (+2.19%)</td><td>328.70 (-16.45%)</td><td>270.50 <b>(+58.84%)</b></td><td>154.91 (-14.46%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>664.10 (n/a)</td><td>387.30 (n/a)</td><td>393.40 (n/a)</td><td>170.30 (n/a)</td><td>181.10 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-18.18%)</td><td>0.01 <b>(-26.20%)</b></td><td>0.01 <b>(-37.23%)</b></td><td>0.01 <b>(-35.21%)</b></td><td>0.00 (-0.28%)</td><td>743.10 <b>(+54.33%)</b></td><td>470.98 <b>(+45.81%)</b></td><td>479.30 <b>(+59.34%)</b></td><td>244.30 <b>(+22.21%)</b></td><td>207.62 <b>(+82.23%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>481.50 (n/a)</td><td>323.00 (n/a)</td><td>300.80 (n/a)</td><td>199.90 (n/a)</td><td>113.94 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (+5.87%)</td><td>0.02 (-0.05%)</td><td>0.02 <b>(+40.77%)</b></td><td>0.00 <b>(-70.74%)</b></td><td>0.01 <b>(+64.60%)</b></td><td>1971.30 <b>(+241.71%)</b></td><td>659.70 <b>(+68.93%)</b></td><td>267.70 <b>(-28.95%)</b></td><td>243.10 (-5.56%)</td><td>746.06 <b>(+436.83%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.90 (n/a)</td><td>390.52 (n/a)</td><td>376.80 (n/a)</td><td>257.40 (n/a)</td><td>138.97 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-11.80%)</td><td>0.01 (-7.59%)</td><td>0.01 (-13.21%)</td><td>0.01 (-8.27%)</td><td>0.00 (-6.03%)</td><td>610.10 (+9.02%)</td><td>461.66 (+9.38%)</td><td>567.90 (+15.22%)</td><td>254.50 (+13.36%)</td><td>176.16 (+14.21%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.60 (n/a)</td><td>422.06 (n/a)</td><td>492.90 (n/a)</td><td>224.50 (n/a)</td><td>154.24 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 <b>(+36.90%)</b></td><td>0.01 (+10.54%)</td><td>0.01 (+3.17%)</td><td>0.00 <b>(-77.30%)</b></td><td>0.01 <b>(+161.75%)</b></td><td>2479.60 <b>(+340.43%)</b></td><td>748.52 <b>(+75.95%)</b></td><td>365.00 (-3.08%)</td><td>237.80 <b>(-26.94%)</b></td><td>969.64 <b>(+841.15%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.00 (n/a)</td><td>425.42 (n/a)</td><td>376.60 (n/a)</td><td>325.50 (n/a)</td><td>103.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (-16.70%)</td><td>0.01 (+13.43%)</td><td>0.01 (+12.58%)</td><td>0.01 <b>(+210.89%)</b></td><td>0.00 <b>(-41.36%)</b></td><td>619.10 <b>(-67.83%)</b></td><td>401.30 <b>(-41.59%)</b></td><td>358.70 (-11.17%)</td><td>289.10 <b>(+20.06%)</b></td><td>135.96 <b>(-80.52%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1924.70 (n/a)</td><td>687.04 (n/a)</td><td>403.80 (n/a)</td><td>240.80 (n/a)</td><td>698.08 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 <b>(+22.37%)</b></td><td>0.02 <b>(+38.72%)</b></td><td>0.02 <b>(+69.77%)</b></td><td>0.01 (+6.30%)</td><td>0.01 <b>(+34.83%)</b></td><td>590.00 (-5.93%)</td><td>363.58 <b>(-23.57%)</b></td><td>305.70 <b>(-41.11%)</b></td><td>189.90 (-18.29%)</td><td>170.45 (+15.84%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.20 (n/a)</td><td>475.72 (n/a)</td><td>519.10 (n/a)</td><td>232.40 (n/a)</td><td>147.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (-13.83%)</td><td>0.01 (+1.16%)</td><td>0.01 <b>(+25.41%)</b></td><td>0.01 <b>(+27.68%)</b></td><td>0.00 <b>(-52.88%)</b></td><td>484.90 <b>(-21.68%)</b></td><td>382.46 (-10.42%)</td><td>373.10 <b>(-20.26%)</b></td><td>288.10 (+16.08%)</td><td>70.34 <b>(-55.78%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.10 (n/a)</td><td>426.96 (n/a)</td><td>467.90 (n/a)</td><td>248.20 (n/a)</td><td>159.07 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (-5.38%)</td><td>0.01 (-5.00%)</td><td>0.01 (+7.92%)</td><td>0.01 <b>(+28.76%)</b></td><td>0.00 <b>(-22.56%)</b></td><td>509.30 <b>(-22.34%)</b></td><td>416.98 (-1.89%)</td><td>419.80 (-7.33%)</td><td>237.40 (+5.70%)</td><td>109.83 <b>(-36.27%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.80 (n/a)</td><td>425.00 (n/a)</td><td>453.00 (n/a)</td><td>224.60 (n/a)</td><td>172.35 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (+4.25%)</td><td>0.01 (+17.26%)</td><td>0.01 <b>(+47.61%)</b></td><td>0.01 (-8.11%)</td><td>0.00 <b>(+47.78%)</b></td><td>595.80 (+8.82%)</td><td>388.36 (-9.97%)</td><td>294.80 <b>(-32.25%)</b></td><td>279.50 (-4.08%)</td><td>143.77 <b>(+55.41%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.50 (n/a)</td><td>431.38 (n/a)</td><td>435.10 (n/a)</td><td>291.40 (n/a)</td><td>92.51 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.02 (+18.27%)</td><td>0.01 (+7.72%)</td><td>0.01 (+12.01%)</td><td>0.01 (+3.45%)</td><td>0.00 <b>(+33.04%)</b></td><td>515.80 (-3.32%)</td><td>424.46 (-4.71%)</td><td>436.80 (-10.71%)</td><td>224.90 (-15.45%)</td><td>117.83 (+5.60%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>533.50 (n/a)</td><td>445.46 (n/a)</td><td>489.20 (n/a)</td><td>266.00 (n/a)</td><td>111.58 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.01 (+6.41%)</td><td>0.01 <b>(+29.72%)</b></td><td>0.01 <b>(+52.67%)</b></td><td>0.01 <b>(+43.98%)</b></td><td>0.00 <b>(-38.32%)</b></td><td>435.00 <b>(-30.54%)</b></td><td>342.82 <b>(-28.06%)</b></td><td>342.40 <b>(-34.49%)</b></td><td>275.50 (-6.04%)</td><td>60.60 <b>(-59.83%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>626.30 (n/a)</td><td>476.54 (n/a)</td><td>522.70 (n/a)</td><td>293.20 (n/a)</td><td>150.87 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (+17.95%)</td><td>0.03 <b>(+27.75%)</b></td><td>0.03 <b>(+23.05%)</b></td><td>0.02 <b>(+46.13%)</b></td><td>0.01 (-18.38%)</td><td>347.30 <b>(-31.57%)</b></td><td>261.04 <b>(-25.82%)</b></td><td>246.20 (-18.75%)</td><td>196.00 (-15.19%)</td><td>55.64 <b>(-53.25%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.50 (n/a)</td><td>351.90 (n/a)</td><td>303.00 (n/a)</td><td>231.10 (n/a)</td><td>119.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.05 (+19.69%)</td><td>0.04 <b>(+35.27%)</b></td><td>0.05 <b>(+83.83%)</b></td><td>0.02 <b>(+39.41%)</b></td><td>0.01 (+5.68%)</td><td>550.20 <b>(-28.28%)</b></td><td>321.56 <b>(-28.68%)</b></td><td>247.30 <b>(-45.60%)</b></td><td>232.70 (-16.45%)</td><td>134.72 <b>(-32.59%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>767.10 (n/a)</td><td>450.86 (n/a)</td><td>454.60 (n/a)</td><td>278.50 (n/a)</td><td>199.83 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (+13.07%)</td><td>0.03 (+19.09%)</td><td>0.03 <b>(+42.32%)</b></td><td>0.01 <b>(+218.89%)</b></td><td>0.01 (-8.93%)</td><td>595.90 <b>(-68.64%)</b></td><td>374.02 <b>(-42.66%)</b></td><td>266.20 <b>(-29.74%)</b></td><td>201.50 (-11.58%)</td><td>191.36 <b>(-72.96%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1900.20 (n/a)</td><td>652.32 (n/a)</td><td>378.90 (n/a)</td><td>227.90 (n/a)</td><td>707.73 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.06 <b>(+46.41%)</b></td><td>0.03 (+18.79%)</td><td>0.02 <b>(-24.89%)</b></td><td>0.02 (+18.51%)</td><td>0.02 <b>(+79.95%)</b></td><td>514.90 (-15.63%)</td><td>371.08 (-9.36%)</td><td>442.80 <b>(+33.13%)</b></td><td>181.90 <b>(-31.72%)</b></td><td>149.45 (+2.72%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>610.30 (n/a)</td><td>409.38 (n/a)</td><td>332.60 (n/a)</td><td>266.40 (n/a)</td><td>145.49 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (-7.97%)</td><td>0.02 <b>(-34.18%)</b></td><td>0.02 <b>(-42.01%)</b></td><td>0.01 <b>(-58.75%)</b></td><td>0.01 <b>(+35.81%)</b></td><td>1014.80 <b>(+142.43%)</b></td><td>569.96 <b>(+79.42%)</b></td><td>527.80 <b>(+72.48%)</b></td><td>238.00 (+8.63%)</td><td>289.58 <b>(+244.43%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>418.60 (n/a)</td><td>317.66 (n/a)</td><td>306.00 (n/a)</td><td>219.10 (n/a)</td><td>84.07 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (+17.06%)</td><td>0.03 <b>(+34.65%)</b></td><td>0.03 <b>(+36.28%)</b></td><td>0.02 <b>(+66.69%)</b></td><td>0.01 <b>(-28.07%)</b></td><td>492.70 <b>(-40.01%)</b></td><td>357.76 <b>(-32.05%)</b></td><td>321.70 <b>(-26.64%)</b></td><td>283.50 (-14.56%)</td><td>81.64 <b>(-61.96%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>821.30 (n/a)</td><td>526.52 (n/a)</td><td>438.50 (n/a)</td><td>331.80 (n/a)</td><td>214.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (+11.71%)</td><td>0.03 <b>(+28.31%)</b></td><td>0.03 <b>(+50.24%)</b></td><td>0.02 <b>(+24.97%)</b></td><td>0.01 (+1.55%)</td><td>538.60 (-19.98%)</td><td>329.44 <b>(-23.98%)</b></td><td>272.40 <b>(-33.45%)</b></td><td>232.90 (-10.49%)</td><td>124.37 <b>(-24.80%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.10 (n/a)</td><td>433.34 (n/a)</td><td>409.30 (n/a)</td><td>260.20 (n/a)</td><td>165.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (+12.05%)</td><td>0.03 <b>(+32.00%)</b></td><td>0.03 <b>(+59.64%)</b></td><td>0.02 <b>(+34.00%)</b></td><td>0.01 (-12.70%)</td><td>425.40 <b>(-25.37%)</b></td><td>304.94 <b>(-27.17%)</b></td><td>288.10 <b>(-37.36%)</b></td><td>238.70 (-10.77%)</td><td>75.79 <b>(-40.72%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>570.00 (n/a)</td><td>418.68 (n/a)</td><td>459.90 (n/a)</td><td>267.50 (n/a)</td><td>127.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (-4.47%)</td><td>0.03 <b>(-22.11%)</b></td><td>0.03 (-3.57%)</td><td>0.00 <b>(-83.31%)</b></td><td>0.01 <b>(+212.45%)</b></td><td>1839.30 <b>(+499.32%)</b></td><td>594.06 <b>(+133.66%)</b></td><td>250.40 (+3.69%)</td><td>229.00 (+4.66%)</td><td>700.35 <b>(+1882.18%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>306.90 (n/a)</td><td>254.24 (n/a)</td><td>241.50 (n/a)</td><td>218.80 (n/a)</td><td>35.33 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.03 (+15.07%)</td><td>0.02 (+9.57%)</td><td>0.02 (+10.38%)</td><td>0.02 <b>(+26.86%)</b></td><td>0.00 (-14.80%)</td><td>464.70 <b>(-21.17%)</b></td><td>397.90 (-11.15%)</td><td>402.10 (-9.40%)</td><td>288.60 (-13.12%)</td><td>67.80 <b>(-41.31%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>589.50 (n/a)</td><td>447.82 (n/a)</td><td>443.80 (n/a)</td><td>332.20 (n/a)</td><td>115.52 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.04 (+18.71%)</td><td>0.03 (-0.32%)</td><td>0.03 (+15.09%)</td><td>0.01 <b>(-36.55%)</b></td><td>0.01 <b>(+141.66%)</b></td><td>604.00 <b>(+57.62%)</b></td><td>383.88 (+15.23%)</td><td>303.50 (-13.11%)</td><td>224.20 (-15.75%)</td><td>175.43 <b>(+225.56%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>383.20 (n/a)</td><td>333.14 (n/a)</td><td>349.30 (n/a)</td><td>266.10 (n/a)</td><td>53.88 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 <b>(+23.58%)</b></td><td>0.05 (-5.46%)</td><td>0.05 (-0.88%)</td><td>0.03 <b>(-30.87%)</b></td><td>0.02 <b>(+110.44%)</b></td><td>598.40 <b>(+44.68%)</b></td><td>380.12 <b>(+21.69%)</b></td><td>307.10 (+0.89%)</td><td>203.90 (-19.09%)</td><td>177.43 <b>(+165.53%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>413.60 (n/a)</td><td>312.36 (n/a)</td><td>304.40 (n/a)</td><td>252.00 (n/a)</td><td>66.82 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 (+12.29%)</td><td>0.09 <b>(+47.02%)</b></td><td>0.09 <b>(+72.99%)</b></td><td>0.07 <b>(+48.24%)</b></td><td>0.01 <b>(-23.61%)</b></td><td>362.40 <b>(-32.54%)</b></td><td>283.18 <b>(-34.14%)</b></td><td>262.20 <b>(-42.20%)</b></td><td>242.60 (-10.94%)</td><td>48.07 <b>(-50.71%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>537.20 (n/a)</td><td>429.98 (n/a)</td><td>453.60 (n/a)</td><td>272.40 (n/a)</td><td>97.53 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (-4.99%)</td><td>0.06 (-4.34%)</td><td>0.06 (-4.28%)</td><td>0.04 <b>(+42.48%)</b></td><td>0.01 <b>(-22.81%)</b></td><td>423.10 <b>(-29.81%)</b></td><td>307.70 (-3.15%)</td><td>265.80 (+4.48%)</td><td>229.20 (+5.23%)</td><td>85.79 <b>(-46.60%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>602.80 (n/a)</td><td>317.70 (n/a)</td><td>254.40 (n/a)</td><td>217.80 (n/a)</td><td>160.67 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (-3.76%)</td><td>0.06 (+13.44%)</td><td>0.07 <b>(+53.26%)</b></td><td>0.04 <b>(+30.15%)</b></td><td>0.02 <b>(-24.63%)</b></td><td>503.80 <b>(-23.17%)</b></td><td>357.14 (-19.92%)</td><td>312.20 <b>(-34.75%)</b></td><td>245.60 (+3.94%)</td><td>125.27 <b>(-37.24%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>655.70 (n/a)</td><td>445.96 (n/a)</td><td>478.50 (n/a)</td><td>236.30 (n/a)</td><td>199.60 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (+1.58%)</td><td>0.05 (+6.30%)</td><td>0.06 <b>(+42.56%)</b></td><td>0.04 (-2.18%)</td><td>0.01 (-1.10%)</td><td>455.10 (+2.22%)</td><td>340.50 (-5.81%)</td><td>287.30 <b>(-29.86%)</b></td><td>246.70 (-1.56%)</td><td>97.01 (+3.55%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>445.20 (n/a)</td><td>361.50 (n/a)</td><td>409.60 (n/a)</td><td>250.60 (n/a)</td><td>93.68 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 <b>(+34.67%)</b></td><td>0.07 <b>(+62.43%)</b></td><td>0.07 <b>(+93.42%)</b></td><td>0.04 <b>(+97.41%)</b></td><td>0.02 <b>(+27.76%)</b></td><td>547.60 <b>(-49.34%)</b></td><td>349.66 <b>(-41.92%)</b></td><td>277.30 <b>(-48.30%)</b></td><td>228.90 <b>(-25.73%)</b></td><td>139.61 <b>(-52.93%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1081.00 (n/a)</td><td>602.08 (n/a)</td><td>536.40 (n/a)</td><td>308.20 (n/a)</td><td>296.59 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (-2.99%)</td><td>0.05 (+7.47%)</td><td>0.04 (+9.77%)</td><td>0.03 (+11.97%)</td><td>0.02 (-16.18%)</td><td>547.70 (-10.70%)</td><td>388.24 (-11.27%)</td><td>394.60 (-8.91%)</td><td>243.60 (+3.09%)</td><td>120.95 <b>(-26.42%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>613.30 (n/a)</td><td>437.56 (n/a)</td><td>433.20 (n/a)</td><td>236.30 (n/a)</td><td>164.39 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 <b>(+65.53%)</b></td><td>0.04 (+8.39%)</td><td>0.04 (-5.34%)</td><td>0.03 (-11.59%)</td><td>0.02 <b>(+252.44%)</b></td><td>635.40 (+13.10%)</td><td>480.64 (+0.93%)</td><td>494.20 (+5.64%)</td><td>247.40 <b>(-39.58%)</b></td><td>142.63 <b>(+122.79%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>561.80 (n/a)</td><td>476.22 (n/a)</td><td>467.80 (n/a)</td><td>409.50 (n/a)</td><td>64.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (+5.12%)</td><td>0.04 (-17.55%)</td><td>0.04 <b>(-38.94%)</b></td><td>0.01 <b>(-73.43%)</b></td><td>0.03 <b>(+52.26%)</b></td><td>1956.10 <b>(+276.39%)</b></td><td>700.22 <b>(+94.47%)</b></td><td>434.30 <b>(+63.76%)</b></td><td>234.50 (-4.87%)</td><td>721.74 <b>(+405.26%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>519.70 (n/a)</td><td>360.06 (n/a)</td><td>265.20 (n/a)</td><td>246.50 (n/a)</td><td>142.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (-18.42%)</td><td>0.05 (+13.61%)</td><td>0.06 <b>(+37.77%)</b></td><td>0.04 (+19.96%)</td><td>0.01 <b>(-39.60%)</b></td><td>491.10 (-16.65%)</td><td>356.34 (-18.52%)</td><td>316.00 <b>(-27.41%)</b></td><td>254.90 <b>(+22.55%)</b></td><td>97.21 <b>(-34.10%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>589.20 (n/a)</td><td>437.32 (n/a)</td><td>435.30 (n/a)</td><td>208.00 (n/a)</td><td>147.52 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (+4.81%)</td><td>0.04 (+9.92%)</td><td>0.04 (+17.72%)</td><td>0.03 (+17.87%)</td><td>0.02 (-3.26%)</td><td>516.10 (-15.17%)</td><td>397.18 (-11.17%)</td><td>370.90 (-15.07%)</td><td>229.40 (-4.58%)</td><td>116.73 <b>(-20.92%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>608.40 (n/a)</td><td>447.14 (n/a)</td><td>436.70 (n/a)</td><td>240.40 (n/a)</td><td>147.62 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (+6.21%)</td><td>0.09 (-5.71%)</td><td>0.10 (-11.48%)</td><td>0.06 (+2.44%)</td><td>0.03 (+0.75%)</td><td>521.70 (-2.39%)</td><td>387.72 (+6.06%)</td><td>335.30 (+12.97%)</td><td>259.90 (-5.87%)</td><td>115.81 (+0.14%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>534.50 (n/a)</td><td>365.56 (n/a)</td><td>296.80 (n/a)</td><td>276.10 (n/a)</td><td>115.65 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 <b>(-23.45%)</b></td><td>0.09 (-13.24%)</td><td>0.07 <b>(-38.97%)</b></td><td>0.06 <b>(+138.92%)</b></td><td>0.03 <b>(-42.95%)</b></td><td>578.40 <b>(-58.14%)</b></td><td>423.42 <b>(-20.07%)</b></td><td>463.50 <b>(+63.84%)</b></td><td>272.60 <b>(+30.68%)</b></td><td>142.92 <b>(-71.04%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1381.90 (n/a)</td><td>529.74 (n/a)</td><td>282.90 (n/a)</td><td>208.60 (n/a)</td><td>493.60 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.15 (-12.61%)</td><td>0.09 (-13.51%)</td><td>0.08 (-13.44%)</td><td>0.05 <b>(-33.91%)</b></td><td>0.04 (+2.72%)</td><td>848.80 <b>(+51.30%)</b></td><td>526.98 <b>(+23.36%)</b></td><td>533.60 (+15.52%)</td><td>280.20 (+14.41%)</td><td>236.36 <b>(+64.12%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>561.00 (n/a)</td><td>427.18 (n/a)</td><td>461.90 (n/a)</td><td>244.90 (n/a)</td><td>144.02 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (-8.85%)</td><td>0.07 <b>(-24.24%)</b></td><td>0.07 <b>(-41.34%)</b></td><td>0.05 (-11.13%)</td><td>0.02 <b>(-20.09%)</b></td><td>600.50 (+12.52%)</td><td>470.40 <b>(+29.07%)</b></td><td>497.80 <b>(+70.48%)</b></td><td>283.20 (+9.72%)</td><td>118.11 (-6.36%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>533.70 (n/a)</td><td>364.44 (n/a)</td><td>292.00 (n/a)</td><td>258.10 (n/a)</td><td>126.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (-19.05%)</td><td>0.10 (-17.65%)</td><td>0.09 <b>(-27.33%)</b></td><td>0.08 (+2.41%)</td><td>0.02 <b>(-42.83%)</b></td><td>546.00 (-2.36%)</td><td>425.34 (+14.54%)</td><td>444.20 <b>(+37.61%)</b></td><td>305.20 <b>(+23.51%)</b></td><td>91.77 <b>(-31.61%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>559.20 (n/a)</td><td>371.34 (n/a)</td><td>322.80 (n/a)</td><td>247.10 (n/a)</td><td>134.18 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 <b>(+31.51%)</b></td><td>0.08 (+10.30%)</td><td>0.07 (+8.49%)</td><td>0.05 (+6.10%)</td><td>0.03 <b>(+52.55%)</b></td><td>633.10 (-5.75%)</td><td>439.22 (-6.71%)</td><td>438.60 (-7.82%)</td><td>256.20 <b>(-23.98%)</b></td><td>133.45 (+4.23%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>671.70 (n/a)</td><td>470.82 (n/a)</td><td>475.80 (n/a)</td><td>337.00 (n/a)</td><td>128.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (-9.07%)</td><td>0.08 (-8.29%)</td><td>0.07 (+1.25%)</td><td>0.06 (-4.38%)</td><td>0.02 <b>(-20.47%)</b></td><td>595.70 (+4.58%)</td><td>475.92 (+6.93%)</td><td>495.60 (-1.22%)</td><td>319.40 (+9.99%)</td><td>121.04 (-6.27%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>569.60 (n/a)</td><td>445.06 (n/a)</td><td>501.70 (n/a)</td><td>290.40 (n/a)</td><td>129.14 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (+4.12%)</td><td>0.08 (+13.44%)</td><td>0.07 <b>(+21.65%)</b></td><td>0.02 <b>(-44.78%)</b></td><td>0.04 <b>(+22.06%)</b></td><td>1923.60 <b>(+81.10%)</b></td><td>692.10 (+18.19%)</td><td>450.70 (-17.80%)</td><td>246.90 (-3.93%)</td><td>696.78 <b>(+137.18%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1062.20 (n/a)</td><td>585.58 (n/a)</td><td>548.30 (n/a)</td><td>257.00 (n/a)</td><td>293.78 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.12 (-5.82%)</td><td>0.09 (+5.80%)</td><td>0.08 (+7.14%)</td><td>0.08 <b>(+38.06%)</b></td><td>0.02 <b>(-38.45%)</b></td><td>459.40 <b>(-27.56%)</b></td><td>415.06 (-11.14%)</td><td>441.60 (-6.66%)</td><td>298.10 (+6.20%)</td><td>67.64 <b>(-53.61%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>634.20 (n/a)</td><td>467.10 (n/a)</td><td>473.10 (n/a)</td><td>280.70 (n/a)</td><td>145.80 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 <b>(-32.58%)</b></td><td>0.06 <b>(-22.98%)</b></td><td>0.06 <b>(-20.77%)</b></td><td>0.06 (-16.41%)</td><td>0.01 <b>(-63.80%)</b></td><td>572.80 (+19.63%)</td><td>515.40 <b>(+27.05%)</b></td><td>518.40 <b>(+26.22%)</b></td><td>447.30 <b>(+48.31%)</b></td><td>45.83 <b>(-36.86%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>478.80 (n/a)</td><td>405.66 (n/a)</td><td>410.70 (n/a)</td><td>301.60 (n/a)</td><td>72.58 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (+12.48%)</td><td>0.07 <b>(+50.37%)</b></td><td>0.07 <b>(+59.93%)</b></td><td>0.05 <b>(+371.13%)</b></td><td>0.01 <b>(-45.37%)</b></td><td>403.20 <b>(-78.77%)</b></td><td>296.68 <b>(-56.98%)</b></td><td>277.20 <b>(-37.47%)</b></td><td>244.50 (-11.09%)</td><td>65.63 <b>(-90.40%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1899.50 (n/a)</td><td>689.62 (n/a)</td><td>443.30 (n/a)</td><td>275.00 (n/a)</td><td>683.95 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (+13.68%)</td><td>0.07 <b>(+44.99%)</b></td><td>0.07 <b>(+90.77%)</b></td><td>0.04 <b>(+26.47%)</b></td><td>0.02 (-9.63%)</td><td>503.00 <b>(-20.92%)</b></td><td>321.30 <b>(-33.70%)</b></td><td>285.40 <b>(-47.58%)</b></td><td>251.90 (-12.05%)</td><td>102.81 <b>(-34.49%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>636.10 (n/a)</td><td>484.62 (n/a)</td><td>544.40 (n/a)</td><td>286.40 (n/a)</td><td>156.93 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (-2.47%)</td><td>0.05 <b>(-22.57%)</b></td><td>0.04 <b>(-36.92%)</b></td><td>0.03 (+3.18%)</td><td>0.02 (+0.45%)</td><td>607.90 (-3.09%)</td><td>477.22 <b>(+28.45%)</b></td><td>507.10 <b>(+58.52%)</b></td><td>238.40 (+2.54%)</td><td>145.57 (-7.12%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>627.30 (n/a)</td><td>371.52 (n/a)</td><td>319.90 (n/a)</td><td>232.50 (n/a)</td><td>156.73 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 <b>(+31.17%)</b></td><td>0.06 <b>(+26.25%)</b></td><td>0.06 <b>(+21.64%)</b></td><td>0.03 <b>(+217.02%)</b></td><td>0.03 (+10.86%)</td><td>792.60 <b>(-68.46%)</b></td><td>426.70 <b>(-47.01%)</b></td><td>361.40 (-17.79%)</td><td>226.90 <b>(-23.76%)</b></td><td>231.27 <b>(-75.85%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2512.70 (n/a)</td><td>805.24 (n/a)</td><td>439.60 (n/a)</td><td>297.60 (n/a)</td><td>957.48 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (+13.53%)</td><td>0.07 <b>(+74.57%)</b></td><td>0.08 <b>(+134.94%)</b></td><td>0.04 <b>(+103.89%)</b></td><td>0.02 (-6.07%)</td><td>535.30 <b>(-50.95%)</b></td><td>313.82 <b>(-48.57%)</b></td><td>247.80 <b>(-57.44%)</b></td><td>242.00 (-11.94%)</td><td>125.83 <b>(-58.48%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1091.40 (n/a)</td><td>610.24 (n/a)</td><td>582.20 (n/a)</td><td>274.80 (n/a)</td><td>303.07 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (-1.75%)</td><td>0.06 (+2.73%)</td><td>0.05 (-1.85%)</td><td>0.04 (-0.01%)</td><td>0.02 (+1.58%)</td><td>543.90 (+0.02%)</td><td>378.10 (-2.50%)</td><td>404.90 (+1.89%)</td><td>244.00 (+1.79%)</td><td>123.83 (-0.02%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>543.80 (n/a)</td><td>387.80 (n/a)</td><td>397.40 (n/a)</td><td>239.70 (n/a)</td><td>123.85 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 <b>(+22.26%)</b></td><td>0.08 (-2.45%)</td><td>0.06 <b>(-32.45%)</b></td><td>0.04 (-12.30%)</td><td>0.04 <b>(+56.69%)</b></td><td>615.40 (+14.03%)</td><td>388.34 (+12.33%)</td><td>430.40 <b>(+48.06%)</b></td><td>194.70 (-18.23%)</td><td>171.44 <b>(+38.96%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>539.70 (n/a)</td><td>345.72 (n/a)</td><td>290.70 (n/a)</td><td>238.10 (n/a)</td><td>123.37 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (+4.90%)</td><td>0.07 <b>(+20.06%)</b></td><td>0.08 <b>(+38.96%)</b></td><td>0.05 (+4.01%)</td><td>0.02 (+15.46%)</td><td>526.80 (-3.85%)</td><td>373.90 (-15.27%)</td><td>312.30 <b>(-28.02%)</b></td><td>261.60 (-4.66%)</td><td>118.58 (+11.50%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>547.90 (n/a)</td><td>441.30 (n/a)</td><td>433.90 (n/a)</td><td>274.40 (n/a)</td><td>106.35 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (-1.55%)</td><td>0.07 <b>(+51.40%)</b></td><td>0.07 <b>(+49.74%)</b></td><td>0.06 <b>(+459.14%)</b></td><td>0.01 <b>(-51.88%)</b></td><td>445.40 <b>(-82.11%)</b></td><td>345.34 <b>(-60.29%)</b></td><td>357.70 <b>(-33.22%)</b></td><td>266.20 (+1.56%)</td><td>68.90 <b>(-92.46%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2490.20 (n/a)</td><td>869.72 (n/a)</td><td>535.60 (n/a)</td><td>262.10 (n/a)</td><td>913.62 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 (+3.39%)</td><td>0.06 (-4.07%)</td><td>0.05 (-2.52%)</td><td>0.04 (-19.96%)</td><td>0.02 (+9.75%)</td><td>688.80 <b>(+24.92%)</b></td><td>458.40 (+7.39%)</td><td>471.60 (+2.57%)</td><td>253.40 (-3.28%)</td><td>170.17 <b>(+26.39%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>551.40 (n/a)</td><td>426.84 (n/a)</td><td>459.80 (n/a)</td><td>262.00 (n/a)</td><td>134.63 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 (+3.44%)</td><td>0.08 (+16.44%)</td><td>0.08 <b>(+43.36%)</b></td><td>0.05 (-6.90%)</td><td>0.02 (+18.67%)</td><td>509.70 (+7.42%)</td><td>353.30 (-11.83%)</td><td>312.90 <b>(-30.23%)</b></td><td>241.00 (-3.33%)</td><td>116.80 <b>(+24.65%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>474.50 (n/a)</td><td>400.72 (n/a)</td><td>448.50 (n/a)</td><td>249.30 (n/a)</td><td>93.71 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 <b>(-22.01%)</b></td><td>0.08 (-13.20%)</td><td>0.08 (-18.35%)</td><td>0.05 <b>(+35.30%)</b></td><td>0.02 <b>(-48.78%)</b></td><td>454.90 <b>(-26.09%)</b></td><td>338.68 (+0.24%)</td><td>291.90 <b>(+22.49%)</b></td><td>252.70 <b>(+28.21%)</b></td><td>91.62 <b>(-49.37%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>615.50 (n/a)</td><td>337.86 (n/a)</td><td>238.30 (n/a)</td><td>197.10 (n/a)</td><td>180.97 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 (-9.22%)</td><td>0.05 (-1.20%)</td><td>0.05 <b>(+22.19%)</b></td><td>0.03 (+2.92%)</td><td>0.02 <b>(-22.71%)</b></td><td>579.30 (-2.85%)</td><td>384.46 (-5.10%)</td><td>402.80 (-18.16%)</td><td>236.70 (+10.14%)</td><td>145.79 (-16.92%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>596.30 (n/a)</td><td>405.12 (n/a)</td><td>492.20 (n/a)</td><td>214.90 (n/a)</td><td>175.48 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 <b>(+20.11%)</b></td><td>0.06 <b>(+49.90%)</b></td><td>0.06 <b>(+82.58%)</b></td><td>0.04 <b>(+35.83%)</b></td><td>0.01 (-12.21%)</td><td>418.90 <b>(-26.38%)</b></td><td>306.68 <b>(-35.36%)</b></td><td>288.80 <b>(-45.22%)</b></td><td>246.40 (-16.73%)</td><td>65.55 <b>(-44.62%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>569.00 (n/a)</td><td>474.46 (n/a)</td><td>527.20 (n/a)</td><td>295.90 (n/a)</td><td>118.37 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.09 (+11.42%)</td><td>0.05 (+9.93%)</td><td>0.04 (+4.28%)</td><td>0.03 (-5.95%)</td><td>0.02 <b>(+28.75%)</b></td><td>642.50 (+6.32%)</td><td>427.72 (-3.40%)</td><td>446.40 (-4.10%)</td><td>213.60 (-10.25%)</td><td>177.28 <b>(+26.96%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.30 (n/a)</td><td>442.76 (n/a)</td><td>465.50 (n/a)</td><td>238.00 (n/a)</td><td>139.64 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (-2.89%)</td><td>0.05 (-19.14%)</td><td>0.05 (-13.85%)</td><td>0.01 <b>(-77.83%)</b></td><td>0.03 <b>(+100.46%)</b></td><td>2006.70 <b>(+351.15%)</b></td><td>732.84 <b>(+110.66%)</b></td><td>372.00 (+16.07%)</td><td>251.40 (+2.95%)</td><td>742.09 <b>(+772.97%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>444.80 (n/a)</td><td>347.88 (n/a)</td><td>320.50 (n/a)</td><td>244.20 (n/a)</td><td>85.01 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.07 (+12.90%)</td><td>0.05 (+17.42%)</td><td>0.04 (+5.54%)</td><td>0.03 (+10.99%)</td><td>0.02 <b>(+24.54%)</b></td><td>535.50 (-9.91%)</td><td>381.84 (-13.46%)</td><td>414.90 (-5.23%)</td><td>246.30 (-11.43%)</td><td>114.33 (+1.39%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>594.40 (n/a)</td><td>441.22 (n/a)</td><td>437.80 (n/a)</td><td>278.10 (n/a)</td><td>112.76 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.08 <b>(+21.00%)</b></td><td>0.05 (+12.55%)</td><td>0.04 (-10.43%)</td><td>0.03 (-5.33%)</td><td>0.02 <b>(+79.73%)</b></td><td>605.60 (+5.63%)</td><td>400.42 (-2.12%)</td><td>417.50 (+11.66%)</td><td>223.70 (-17.36%)</td><td>167.91 <b>(+48.65%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>573.30 (n/a)</td><td>409.08 (n/a)</td><td>373.90 (n/a)</td><td>270.70 (n/a)</td><td>112.96 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.46 <b>(+46.75%)</b></td><td>0.29 <b>(+27.57%)</b></td><td>0.28 <b>(+32.45%)</b></td><td>0.17 (+1.70%)</td><td>0.12 <b>(+113.95%)</b></td><td>595.60 (-1.67%)</td><td>387.38 (-13.56%)</td><td>352.70 <b>(-24.51%)</b></td><td>213.60 <b>(-31.84%)</b></td><td>162.95 <b>(+47.04%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>605.70 (n/a)</td><td>448.14 (n/a)</td><td>467.20 (n/a)</td><td>313.40 (n/a)</td><td>110.82 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.40 (+17.98%)</td><td>0.33 <b>(+31.79%)</b></td><td>0.34 <b>(+61.05%)</b></td><td>0.18 (-1.39%)</td><td>0.09 <b>(+21.41%)</b></td><td>552.80 (+1.41%)</td><td>329.40 <b>(-22.58%)</b></td><td>290.00 <b>(-37.90%)</b></td><td>245.00 (-15.25%)</td><td>127.68 (+9.29%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>545.10 (n/a)</td><td>425.46 (n/a)</td><td>467.00 (n/a)</td><td>289.10 (n/a)</td><td>116.84 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.39 (+10.62%)</td><td>0.28 <b>(+26.55%)</b></td><td>0.24 (+10.85%)</td><td>0.19 <b>(+105.37%)</b></td><td>0.09 (-11.10%)</td><td>520.60 <b>(-51.31%)</b></td><td>379.02 <b>(-30.85%)</b></td><td>416.20 (-9.78%)</td><td>250.20 (-9.61%)</td><td>114.68 <b>(-63.43%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.36 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>1069.20 (n/a)</td><td>548.10 (n/a)</td><td>461.30 (n/a)</td><td>276.80 (n/a)</td><td>313.55 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.30 <b>(+72.75%)</b></td><td>0.20 <b>(+45.44%)</b></td><td>0.25 <b>(+95.92%)</b></td><td>0.03 <b>(-73.99%)</b></td><td>0.11 <b>(+346.40%)</b></td><td>2515.30 <b>(+284.43%)</b></td><td>770.12 <b>(+36.88%)</b></td><td>296.20 <b>(-48.96%)</b></td><td>246.60 <b>(-42.11%)</b></td><td>980.36 <b>(+984.65%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>654.30 (n/a)</td><td>562.64 (n/a)</td><td>580.30 (n/a)</td><td>426.00 (n/a)</td><td>90.38 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.31 (-5.07%)</td><td>0.25 <b>(+30.95%)</b></td><td>0.25 <b>(+83.43%)</b></td><td>0.18 <b>(+45.15%)</b></td><td>0.05 <b>(-45.18%)</b></td><td>418.70 <b>(-31.11%)</b></td><td>306.74 <b>(-31.38%)</b></td><td>293.40 <b>(-45.50%)</b></td><td>240.90 (+5.33%)</td><td>67.07 <b>(-59.16%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.32 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>607.80 (n/a)</td><td>446.98 (n/a)</td><td>538.30 (n/a)</td><td>228.70 (n/a)</td><td>164.20 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.26 (-10.37%)</td><td>0.19 (-0.95%)</td><td>0.17 (-0.69%)</td><td>0.14 (+14.64%)</td><td>0.06 (-18.66%)</td><td>530.50 (-12.78%)</td><td>415.70 (-2.49%)</td><td>443.50 (+0.70%)</td><td>284.50 (+11.57%)</td><td>117.81 <b>(-20.23%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>608.20 (n/a)</td><td>426.30 (n/a)</td><td>440.40 (n/a)</td><td>255.00 (n/a)</td><td>147.69 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.10 <b>(-36.56%)</b></td><td>0.08 (+9.28%)</td><td>0.08 (+15.39%)</td><td>0.06 <b>(+232.32%)</b></td><td>0.01 <b>(-78.11%)</b></td><td>583.10 <b>(-69.91%)</b></td><td>447.40 <b>(-54.57%)</b></td><td>437.60 (-13.33%)</td><td>381.60 <b>(+57.62%)</b></td><td>80.53 <b>(-90.80%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1937.90 (n/a)</td><td>984.76 (n/a)</td><td>504.90 (n/a)</td><td>242.10 (n/a)</td><td>875.31 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (+11.38%)</td><td>0.12 (+18.05%)</td><td>0.13 (+11.85%)</td><td>0.08 (+7.25%)</td><td>0.03 (+7.01%)</td><td>454.60 (-6.77%)</td><td>308.72 (-15.31%)</td><td>278.60 (-10.59%)</td><td>256.00 (-10.21%)</td><td>82.36 (-7.22%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>487.60 (n/a)</td><td>364.54 (n/a)</td><td>311.60 (n/a)</td><td>285.10 (n/a)</td><td>88.78 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (+0.51%)</td><td>0.08 (-10.92%)</td><td>0.08 (-3.40%)</td><td>0.02 <b>(-74.44%)</b></td><td>0.04 <b>(+72.38%)</b></td><td>2108.90 <b>(+291.33%)</b></td><td>764.18 <b>(+69.18%)</b></td><td>473.80 (+3.52%)</td><td>294.30 (-0.47%)</td><td>757.48 <b>(+682.40%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>538.90 (n/a)</td><td>451.70 (n/a)</td><td>457.70 (n/a)</td><td>295.70 (n/a)</td><td>96.82 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.15 (-10.21%)</td><td>0.12 (+2.01%)</td><td>0.14 (+13.03%)</td><td>0.07 (+1.85%)</td><td>0.04 (-7.52%)</td><td>494.10 (-1.81%)</td><td>345.84 (-2.90%)</td><td>265.30 (-11.54%)</td><td>248.10 (+11.41%)</td><td>120.84 (-4.28%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>503.20 (n/a)</td><td>356.16 (n/a)</td><td>299.90 (n/a)</td><td>222.70 (n/a)</td><td>126.24 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.16 (+9.12%)</td><td>0.10 (+4.71%)</td><td>0.07 (+10.62%)</td><td>0.03 <b>(-44.48%)</b></td><td>0.05 <b>(+32.71%)</b></td><td>1103.30 <b>(+80.10%)</b></td><td>526.46 (+13.41%)</td><td>516.60 (-9.61%)</td><td>231.40 (-8.36%)</td><td>352.06 <b>(+100.04%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>612.60 (n/a)</td><td>464.20 (n/a)</td><td>571.50 (n/a)</td><td>252.50 (n/a)</td><td>176.00 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.16 (+9.48%)</td><td>0.10 (+15.16%)</td><td>0.08 (-6.14%)</td><td>0.06 (-1.26%)</td><td>0.05 <b>(+44.40%)</b></td><td>574.30 (+1.29%)</td><td>412.82 (-7.23%)</td><td>481.40 (+6.55%)</td><td>235.40 (-8.69%)</td><td>162.20 <b>(+25.22%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>567.00 (n/a)</td><td>444.98 (n/a)</td><td>451.80 (n/a)</td><td>257.80 (n/a)</td><td>129.53 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.18 (+8.92%)</td><td>0.12 (+14.31%)</td><td>0.13 <b>(+46.63%)</b></td><td>0.07 (-16.99%)</td><td>0.05 <b>(+37.76%)</b></td><td>605.90 <b>(+20.46%)</b></td><td>395.94 (-5.34%)</td><td>321.00 <b>(-31.80%)</b></td><td>226.50 (-8.19%)</td><td>171.39 <b>(+63.92%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>503.00 (n/a)</td><td>418.26 (n/a)</td><td>470.70 (n/a)</td><td>246.70 (n/a)</td><td>104.56 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.15 <b>(+20.46%)</b></td><td>0.11 (+18.50%)</td><td>0.09 (+9.41%)</td><td>0.07 (-8.88%)</td><td>0.04 <b>(+92.25%)</b></td><td>569.00 (+9.76%)</td><td>408.84 (-9.73%)</td><td>461.40 (-8.60%)</td><td>265.30 (-16.96%)</td><td>137.07 <b>(+60.87%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>518.40 (n/a)</td><td>452.92 (n/a)</td><td>504.80 (n/a)</td><td>319.50 (n/a)</td><td>85.21 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.16 (+18.61%)</td><td>0.15 <b>(+72.04%)</b></td><td>0.15 <b>(+57.30%)</b></td><td>0.14 <b>(+562.38%)</b></td><td>0.01 <b>(-70.65%)</b></td><td>296.70 <b>(-84.90%)</b></td><td>274.34 <b>(-62.01%)</b></td><td>277.70 <b>(-36.44%)</b></td><td>249.30 (-15.69%)</td><td>22.90 <b>(-96.73%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1965.20 (n/a)</td><td>722.20 (n/a)</td><td>436.90 (n/a)</td><td>295.70 (n/a)</td><td>699.66 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 (+2.49%)</td><td>0.12 (-7.66%)</td><td>0.15 (-3.44%)</td><td>0.06 (+6.12%)</td><td>0.05 (+10.14%)</td><td>639.30 (-5.76%)</td><td>379.00 (+8.50%)</td><td>282.40 (+3.56%)</td><td>246.80 (-2.45%)</td><td>172.50 (-6.37%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>678.40 (n/a)</td><td>349.30 (n/a)</td><td>272.70 (n/a)</td><td>253.00 (n/a)</td><td>184.22 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 (+15.53%)</td><td>0.11 (+6.57%)</td><td>0.09 (-2.41%)</td><td>0.08 (-8.19%)</td><td>0.04 <b>(+60.51%)</b></td><td>487.50 (+8.91%)</td><td>387.96 (-1.78%)</td><td>431.20 (+2.47%)</td><td>239.20 (-13.43%)</td><td>109.61 <b>(+58.69%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>447.60 (n/a)</td><td>394.98 (n/a)</td><td>420.80 (n/a)</td><td>276.30 (n/a)</td><td>69.07 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 (+10.56%)</td><td>0.13 (+17.07%)</td><td>0.13 <b>(+36.26%)</b></td><td>0.08 (-12.12%)</td><td>0.04 <b>(+27.44%)</b></td><td>541.20 (+13.77%)</td><td>348.54 (-12.07%)</td><td>321.50 <b>(-26.60%)</b></td><td>245.50 (-9.54%)</td><td>118.47 <b>(+28.78%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>475.70 (n/a)</td><td>396.38 (n/a)</td><td>438.00 (n/a)</td><td>271.40 (n/a)</td><td>91.99 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.15 <b>(+30.08%)</b></td><td>0.14 <b>(+42.88%)</b></td><td>0.14 <b>(+21.88%)</b></td><td>0.11 <b>(+83.66%)</b></td><td>0.01 <b>(-50.60%)</b></td><td>302.90 <b>(-45.54%)</b></td><td>259.52 <b>(-35.30%)</b></td><td>253.60 (-17.96%)</td><td>227.30 <b>(-23.13%)</b></td><td>28.62 <b>(-79.27%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>556.20 (n/a)</td><td>401.14 (n/a)</td><td>309.10 (n/a)</td><td>295.70 (n/a)</td><td>138.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (-13.36%)</td><td>0.11 (+7.82%)</td><td>0.11 (+9.94%)</td><td>0.07 (+7.49%)</td><td>0.02 <b>(-29.47%)</b></td><td>490.60 (-6.96%)</td><td>335.70 (-10.60%)</td><td>320.10 (-9.04%)</td><td>268.30 (+15.45%)</td><td>90.20 <b>(-23.51%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>527.30 (n/a)</td><td>375.52 (n/a)</td><td>351.90 (n/a)</td><td>232.40 (n/a)</td><td>117.92 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.17 <b>(+45.77%)</b></td><td>0.10 (+11.37%)</td><td>0.08 (-0.05%)</td><td>0.07 (-8.05%)</td><td>0.04 <b>(+101.92%)</b></td><td>508.60 (+8.74%)</td><td>379.64 (-2.66%)</td><td>437.20 (+0.05%)</td><td>202.00 <b>(-31.39%)</b></td><td>131.29 <b>(+54.68%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>467.70 (n/a)</td><td>390.02 (n/a)</td><td>437.00 (n/a)</td><td>294.40 (n/a)</td><td>84.88 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.22 <b>(+180.39%)</b></td><td>0.10 <b>(+51.44%)</b></td><td>0.10 <b>(+55.77%)</b></td><td>0.02 <b>(-65.73%)</b></td><td>0.09 <b>(+790.31%)</b></td><td>1911.30 <b>(+191.80%)</b></td><td>908.78 <b>(+68.33%)</b></td><td>336.40 <b>(-35.80%)</b></td><td>155.40 <b>(-64.33%)</b></td><td>902.39 <b>(+1036.38%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>655.00 (n/a)</td><td>539.88 (n/a)</td><td>524.00 (n/a)</td><td>435.70 (n/a)</td><td>79.41 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 (-4.38%)</td><td>0.09 (-8.69%)</td><td>0.08 (+4.44%)</td><td>0.01 <b>(-72.84%)</b></td><td>0.06 <b>(+44.41%)</b></td><td>2385.10 <b>(+268.13%)</b></td><td>798.52 <b>(+89.07%)</b></td><td>449.70 (-4.26%)</td><td>243.20 (+4.60%)</td><td>904.40 <b>(+448.80%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>647.90 (n/a)</td><td>422.34 (n/a)</td><td>469.70 (n/a)</td><td>232.50 (n/a)</td><td>164.80 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.14 <b>(+64.59%)</b></td><td>0.12 <b>(+67.80%)</b></td><td>0.14 <b>(+94.00%)</b></td><td>0.08 <b>(+20.92%)</b></td><td>0.03 <b>(+226.20%)</b></td><td>446.20 (-17.31%)</td><td>296.80 <b>(-37.71%)</b></td><td>250.60 <b>(-48.47%)</b></td><td>240.50 <b>(-39.24%)</b></td><td>87.20 <b>(+67.59%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>539.60 (n/a)</td><td>476.50 (n/a)</td><td>486.30 (n/a)</td><td>395.80 (n/a)</td><td>52.03 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.51 (-6.46%)</td><td>0.46 (-0.17%)</td><td>0.48 (+9.43%)</td><td>0.33 <b>(-20.93%)</b></td><td>0.08 <b>(+35.06%)</b></td><td>397.50 <b>(+26.47%)</b></td><td>292.46 (+1.78%)</td><td>275.30 (-8.63%)</td><td>256.10 (+6.93%)</td><td>59.45 <b>(+84.96%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.44 (n/a)</td><td>0.42 (n/a)</td><td>0.06 (n/a)</td><td>314.30 (n/a)</td><td>287.34 (n/a)</td><td>301.30 (n/a)</td><td>239.50 (n/a)</td><td>32.15 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.48 (-3.78%)</td><td>0.28 <b>(-39.22%)</b></td><td>0.26 <b>(-46.45%)</b></td><td>0.19 <b>(-54.09%)</b></td><td>0.11 <b>(+197.58%)</b></td><td>676.20 <b>(+117.85%)</b></td><td>513.18 <b>(+80.74%)</b></td><td>503.40 <b>(+86.72%)</b></td><td>273.50 (+3.95%)</td><td>154.69 <b>(+539.93%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.50 (n/a)</td><td>0.46 (n/a)</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.04 (n/a)</td><td>310.40 (n/a)</td><td>283.94 (n/a)</td><td>269.60 (n/a)</td><td>263.10 (n/a)</td><td>24.17 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.54 (+15.91%)</td><td>0.31 (-0.93%)</td><td>0.22 <b>(-25.09%)</b></td><td>0.20 <b>(-21.04%)</b></td><td>0.15 <b>(+72.43%)</b></td><td>667.70 <b>(+26.65%)</b></td><td>496.96 (+13.03%)</td><td>600.30 <b>(+33.49%)</b></td><td>242.10 (-13.72%)</td><td>194.04 <b>(+104.52%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>527.20 (n/a)</td><td>439.68 (n/a)</td><td>449.70 (n/a)</td><td>280.60 (n/a)</td><td>94.87 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+83.33%)</b></td><td>0.00 <b>(+250.00%)</b></td><td>0.00 <b>(+150.00%)</b></td><td>0.00 <b>(-56.28%)</b></td><td>8087.11 <b>(-61.93%)</b></td><td>6234.32 <b>(-59.48%)</b></td><td>5699.64 <b>(-69.90%)</b></td><td>5088.66 (-5.14%)</td><td>1223.48 <b>(-82.10%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21243.41 (n/a)</td><td>15385.94 (n/a)</td><td>18935.86 (n/a)</td><td>5364.12 (n/a)</td><td>6835.82 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.00 <b>(-60.00%)</b></td><td>0.00 <b>(-41.86%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-81.53%)</b></td><td>21217.65 (+6.02%)</td><td>17144.41 <b>(+30.02%)</b></td><td>17130.72 (+4.56%)</td><td>13779.24 <b>(+151.16%)</b></td><td>3326.43 <b>(-52.38%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20013.74 (n/a)</td><td>13185.76 (n/a)</td><td>16384.24 (n/a)</td><td>5486.26 (n/a)</td><td>6985.77 (n/a)</td>
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
<td><code>9c70ba8</code> — 2026-06-29 16:39:58</td><td>0.13 (+9.27%)</td><td>0.10 (+12.72%)</td><td>0.10 (+17.64%)</td><td>0.07 (-2.37%)</td><td>0.03 <b>(+39.76%)</b></td><td>28335.83 (+2.47%)</td><td>22321.49 (-9.03%)</td><td>21680.22 (-15.03%)</td><td>16019.55 (-8.52%)</td><td>5672.15 <b>(+37.71%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>27652.54 (n/a)</td><td>24536.30 (n/a)</td><td>25515.81 (n/a)</td><td>17511.68 (n/a)</td><td>4118.96 (n/a)</td>
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
