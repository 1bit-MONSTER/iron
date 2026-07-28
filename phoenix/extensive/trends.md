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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (+11.65%)</td><td>0.02 (+9.31%)</td><td>0.02 (+2.29%)</td><td>0.01 <b>(+20.45%)</b></td><td>0.01 (-1.40%)</td><td>521.20 (-16.97%)</td><td>362.60 (-10.88%)</td><td>366.00 (-2.24%)</td><td>234.20 (-10.41%)</td><td>105.20 <b>(-27.42%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.70 (n/a)</td><td>406.88 (n/a)</td><td>374.40 (n/a)</td><td>261.40 (n/a)</td><td>144.93 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(-20.50%)</b></td><td>0.02 <b>(-24.45%)</b></td><td>0.02 <b>(-24.25%)</b></td><td>0.01 (-1.31%)</td><td>0.00 <b>(-26.24%)</b></td><td>536.50 (+1.32%)</td><td>398.14 <b>(+28.91%)</b></td><td>322.10 <b>(+32.01%)</b></td><td>300.20 <b>(+25.82%)</b></td><td>118.52 (-5.40%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>529.50 (n/a)</td><td>308.84 (n/a)</td><td>244.00 (n/a)</td><td>238.60 (n/a)</td><td>125.29 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(-44.92%)</b></td><td>0.01 <b>(-30.33%)</b></td><td>0.01 <b>(-39.52%)</b></td><td>0.01 <b>(+75.91%)</b></td><td>0.00 <b>(-67.52%)</b></td><td>610.30 <b>(-43.15%)</b></td><td>473.50 (+4.62%)</td><td>428.10 <b>(+65.35%)</b></td><td>362.70 <b>(+81.53%)</b></td><td>120.52 <b>(-66.92%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1073.50 (n/a)</td><td>452.58 (n/a)</td><td>258.90 (n/a)</td><td>199.80 (n/a)</td><td>364.35 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (-9.85%)</td><td>0.02 (+11.28%)</td><td>0.02 <b>(+44.91%)</b></td><td>0.01 (-4.73%)</td><td>0.01 <b>(-20.01%)</b></td><td>592.30 (+4.96%)</td><td>393.76 (-13.29%)</td><td>362.50 <b>(-30.99%)</b></td><td>221.90 (+10.89%)</td><td>146.10 (-3.73%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.30 (n/a)</td><td>454.12 (n/a)</td><td>525.30 (n/a)</td><td>200.10 (n/a)</td><td>151.76 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(-39.19%)</b></td><td>0.01 <b>(-25.49%)</b></td><td>0.01 (-19.47%)</td><td>0.01 (+9.13%)</td><td>0.00 <b>(-59.61%)</b></td><td>636.70 (-8.36%)</td><td>539.86 <b>(+20.99%)</b></td><td>599.10 <b>(+24.17%)</b></td><td>381.00 <b>(+64.44%)</b></td><td>114.15 <b>(-36.33%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>694.80 (n/a)</td><td>446.20 (n/a)</td><td>482.50 (n/a)</td><td>231.70 (n/a)</td><td>179.29 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-15.82%)</td><td>0.02 <b>(+21.42%)</b></td><td>0.02 <b>(+48.83%)</b></td><td>0.01 <b>(+103.50%)</b></td><td>0.00 <b>(-51.06%)</b></td><td>480.90 <b>(-50.86%)</b></td><td>378.76 <b>(-33.23%)</b></td><td>330.80 <b>(-32.82%)</b></td><td>287.70 (+18.84%)</td><td>89.38 <b>(-70.71%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>978.60 (n/a)</td><td>567.24 (n/a)</td><td>492.40 (n/a)</td><td>242.10 (n/a)</td><td>305.16 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 <b>(-26.95%)</b></td><td>0.04 <b>(+22.68%)</b></td><td>0.05 <b>(+81.30%)</b></td><td>0.02 <b>(+55.91%)</b></td><td>0.01 <b>(-43.65%)</b></td><td>533.30 <b>(-35.86%)</b></td><td>305.58 <b>(-31.11%)</b></td><td>248.50 <b>(-44.84%)</b></td><td>236.50 <b>(+36.86%)</b></td><td>128.10 <b>(-48.10%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>831.40 (n/a)</td><td>443.56 (n/a)</td><td>450.50 (n/a)</td><td>172.80 (n/a)</td><td>246.81 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (+16.20%)</td><td>0.04 <b>(+32.52%)</b></td><td>0.04 <b>(+52.16%)</b></td><td>0.02 (-4.91%)</td><td>0.01 <b>(+36.53%)</b></td><td>623.90 (+5.18%)</td><td>366.36 <b>(-21.15%)</b></td><td>294.80 <b>(-34.27%)</b></td><td>244.60 (-13.96%)</td><td>157.12 (+19.69%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>593.20 (n/a)</td><td>464.62 (n/a)</td><td>448.50 (n/a)</td><td>284.30 (n/a)</td><td>131.27 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (+18.71%)</td><td>0.04 (+18.67%)</td><td>0.04 <b>(+31.47%)</b></td><td>0.03 (+8.25%)</td><td>0.01 <b>(+41.18%)</b></td><td>466.00 (-7.63%)</td><td>331.88 (-12.86%)</td><td>297.30 <b>(-23.94%)</b></td><td>222.40 (-15.76%)</td><td>113.53 (+12.67%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.50 (n/a)</td><td>380.88 (n/a)</td><td>390.90 (n/a)</td><td>264.00 (n/a)</td><td>100.77 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (-4.79%)</td><td>0.03 (+13.52%)</td><td>0.03 (+10.16%)</td><td>0.02 <b>(+148.03%)</b></td><td>0.01 <b>(-31.92%)</b></td><td>546.40 <b>(-59.68%)</b></td><td>406.24 <b>(-32.71%)</b></td><td>449.80 (-9.22%)</td><td>257.00 (+5.03%)</td><td>128.17 <b>(-71.42%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1355.20 (n/a)</td><td>603.72 (n/a)</td><td>495.50 (n/a)</td><td>244.70 (n/a)</td><td>448.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (-4.72%)</td><td>0.03 (-11.80%)</td><td>0.03 <b>(-29.79%)</b></td><td>0.02 (-8.74%)</td><td>0.01 (+17.70%)</td><td>645.00 (+9.56%)</td><td>465.38 (+18.43%)</td><td>465.10 <b>(+42.41%)</b></td><td>280.60 (+4.94%)</td><td>173.88 <b>(+34.00%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>588.70 (n/a)</td><td>392.96 (n/a)</td><td>326.60 (n/a)</td><td>267.40 (n/a)</td><td>129.76 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (-0.92%)</td><td>0.03 (-10.90%)</td><td>0.03 <b>(-21.55%)</b></td><td>0.02 <b>(+32.02%)</b></td><td>0.01 <b>(-23.55%)</b></td><td>608.80 <b>(-24.26%)</b></td><td>433.78 (+0.97%)</td><td>397.80 <b>(+27.46%)</b></td><td>243.80 (+0.91%)</td><td>157.02 <b>(-35.57%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>803.80 (n/a)</td><td>429.62 (n/a)</td><td>312.10 (n/a)</td><td>241.60 (n/a)</td><td>243.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 <b>(-20.78%)</b></td><td>0.07 (-9.92%)</td><td>0.07 (+4.03%)</td><td>0.04 (-6.72%)</td><td>0.02 <b>(-38.09%)</b></td><td>585.10 (+7.20%)</td><td>376.90 (+4.13%)</td><td>354.10 (-3.88%)</td><td>246.80 <b>(+26.24%)</b></td><td>127.12 (-12.38%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>545.80 (n/a)</td><td>361.96 (n/a)</td><td>368.40 (n/a)</td><td>195.50 (n/a)</td><td>145.08 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (-17.14%)</td><td>0.08 (-3.21%)</td><td>0.09 (+1.17%)</td><td>0.03 <b>(-38.23%)</b></td><td>0.03 (-1.93%)</td><td>846.50 <b>(+61.89%)</b></td><td>382.46 (+14.53%)</td><td>271.00 (-1.13%)</td><td>243.40 <b>(+20.73%)</b></td><td>260.02 <b>(+99.06%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>522.90 (n/a)</td><td>333.94 (n/a)</td><td>274.10 (n/a)</td><td>201.60 (n/a)</td><td>130.63 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (+17.16%)</td><td>0.06 (+7.07%)</td><td>0.06 (+3.56%)</td><td>0.02 <b>(-48.57%)</b></td><td>0.03 <b>(+99.10%)</b></td><td>1068.50 <b>(+94.41%)</b></td><td>504.44 (+16.36%)</td><td>439.90 (-3.42%)</td><td>244.60 (-14.62%)</td><td>332.33 <b>(+246.16%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>549.60 (n/a)</td><td>433.50 (n/a)</td><td>455.50 (n/a)</td><td>286.50 (n/a)</td><td>96.00 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 <b>(-34.27%)</b></td><td>0.07 <b>(-29.78%)</b></td><td>0.07 <b>(-26.38%)</b></td><td>0.05 <b>(-20.90%)</b></td><td>0.02 <b>(-37.80%)</b></td><td>512.80 <b>(+26.43%)</b></td><td>392.52 <b>(+40.35%)</b></td><td>351.80 <b>(+35.83%)</b></td><td>259.40 <b>(+52.14%)</b></td><td>110.63 <b>(+27.24%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>405.60 (n/a)</td><td>279.68 (n/a)</td><td>259.00 (n/a)</td><td>170.50 (n/a)</td><td>86.95 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 <b>(-21.38%)</b></td><td>0.06 (-12.00%)</td><td>0.06 (+10.95%)</td><td>0.04 (-10.31%)</td><td>0.02 <b>(-33.55%)</b></td><td>594.70 (+11.49%)</td><td>460.94 (+9.63%)</td><td>431.80 (-9.87%)</td><td>301.70 <b>(+27.19%)</b></td><td>126.65 (-4.61%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>533.40 (n/a)</td><td>420.44 (n/a)</td><td>479.10 (n/a)</td><td>237.20 (n/a)</td><td>132.77 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 <b>(+55.31%)</b></td><td>0.07 <b>(+31.39%)</b></td><td>0.07 <b>(+50.10%)</b></td><td>0.03 <b>(-30.99%)</b></td><td>0.03 <b>(+232.93%)</b></td><td>772.20 <b>(+44.91%)</b></td><td>419.00 (-11.60%)</td><td>343.50 <b>(-33.38%)</b></td><td>251.80 <b>(-35.62%)</b></td><td>214.74 <b>(+205.44%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>532.90 (n/a)</td><td>473.96 (n/a)</td><td>515.60 (n/a)</td><td>391.10 (n/a)</td><td>70.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.23 (-0.48%)</td><td>0.13 <b>(-33.90%)</b></td><td>0.11 <b>(-44.04%)</b></td><td>0.08 <b>(-22.31%)</b></td><td>0.06 <b>(+24.56%)</b></td><td>579.00 <b>(+28.70%)</b></td><td>439.64 <b>(+59.66%)</b></td><td>431.50 <b>(+78.67%)</b></td><td>212.40 (+0.47%)</td><td>144.40 <b>(+46.53%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>449.90 (n/a)</td><td>275.36 (n/a)</td><td>241.50 (n/a)</td><td>211.40 (n/a)</td><td>98.55 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.22 (+14.70%)</td><td>0.15 (-3.09%)</td><td>0.13 <b>(-24.70%)</b></td><td>0.07 <b>(-32.84%)</b></td><td>0.06 <b>(+42.35%)</b></td><td>718.60 <b>(+48.90%)</b></td><td>401.82 (+13.56%)</td><td>388.20 <b>(+32.81%)</b></td><td>224.80 (-12.83%)</td><td>198.30 <b>(+74.29%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>482.60 (n/a)</td><td>353.84 (n/a)</td><td>292.30 (n/a)</td><td>257.90 (n/a)</td><td>113.78 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.36 <b>(+105.65%)</b></td><td>0.19 <b>(+40.43%)</b></td><td>0.17 (+4.55%)</td><td>0.03 <b>(-68.34%)</b></td><td>0.12 <b>(+158.37%)</b></td><td>1844.60 <b>(+215.86%)</b></td><td>553.12 <b>(+38.23%)</b></td><td>280.90 (-4.36%)</td><td>137.10 <b>(-51.38%)</b></td><td>724.79 <b>(+366.16%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>584.00 (n/a)</td><td>400.14 (n/a)</td><td>293.70 (n/a)</td><td>282.00 (n/a)</td><td>155.48 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.18 (+7.88%)</td><td>0.12 (+0.23%)</td><td>0.13 <b>(+26.01%)</b></td><td>0.05 <b>(-46.55%)</b></td><td>0.05 <b>(+49.33%)</b></td><td>1068.20 <b>(+87.11%)</b></td><td>522.30 (+17.10%)</td><td>372.60 <b>(-20.62%)</b></td><td>266.40 (-7.31%)</td><td>320.11 <b>(+177.13%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>570.90 (n/a)</td><td>446.02 (n/a)</td><td>469.40 (n/a)</td><td>287.40 (n/a)</td><td>115.51 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.12 <b>(-30.89%)</b></td><td>0.07 <b>(-43.34%)</b></td><td>0.08 <b>(-28.19%)</b></td><td>0.03 <b>(-69.08%)</b></td><td>0.04 (-5.50%)</td><td>1901.20 <b>(+223.44%)</b></td><td>934.64 <b>(+126.87%)</b></td><td>612.20 <b>(+39.26%)</b></td><td>401.30 <b>(+44.66%)</b></td><td>642.01 <b>(+379.13%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>587.80 (n/a)</td><td>411.98 (n/a)</td><td>439.60 (n/a)</td><td>277.40 (n/a)</td><td>134.00 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.26 (+3.47%)</td><td>0.14 (-15.44%)</td><td>0.13 <b>(-23.26%)</b></td><td>0.08 (+1.56%)</td><td>0.07 (+9.84%)</td><td>640.90 (-1.52%)</td><td>404.86 (+18.36%)</td><td>384.10 <b>(+30.34%)</b></td><td>188.30 (-3.34%)</td><td>166.33 (-7.00%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>650.80 (n/a)</td><td>342.06 (n/a)</td><td>294.70 (n/a)</td><td>194.80 (n/a)</td><td>178.84 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (+10.19%)</td><td>0.01 <b>(+34.40%)</b></td><td>0.01 <b>(+39.55%)</b></td><td>0.00 <b>(+263.13%)</b></td><td>0.00 (-7.62%)</td><td>535.40 <b>(-72.46%)</b></td><td>362.12 <b>(-47.85%)</b></td><td>302.70 <b>(-28.34%)</b></td><td>215.80 (-9.25%)</td><td>146.86 <b>(-79.13%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1944.20 (n/a)</td><td>694.40 (n/a)</td><td>422.40 (n/a)</td><td>237.80 (n/a)</td><td>703.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 <b>(-20.66%)</b></td><td>0.01 (-14.58%)</td><td>0.01 <b>(-23.70%)</b></td><td>0.01 (+15.84%)</td><td>0.00 <b>(-51.46%)</b></td><td>500.40 (-13.66%)</td><td>409.64 (+5.15%)</td><td>382.60 <b>(+31.07%)</b></td><td>297.30 <b>(+26.08%)</b></td><td>86.86 <b>(-49.00%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>579.60 (n/a)</td><td>389.58 (n/a)</td><td>291.90 (n/a)</td><td>235.80 (n/a)</td><td>170.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (-1.27%)</td><td>0.01 (-2.18%)</td><td>0.01 (+5.93%)</td><td>0.01 (+13.11%)</td><td>0.00 <b>(-24.88%)</b></td><td>508.20 (-11.59%)</td><td>408.16 (-4.00%)</td><td>450.30 (-5.60%)</td><td>249.90 (+1.30%)</td><td>103.43 <b>(-33.76%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>574.80 (n/a)</td><td>425.18 (n/a)</td><td>477.00 (n/a)</td><td>246.70 (n/a)</td><td>156.14 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (-14.72%)</td><td>0.01 (-2.41%)</td><td>0.01 (-16.71%)</td><td>0.00 (+1.02%)</td><td>0.00 <b>(-34.51%)</b></td><td>564.00 (-1.00%)</td><td>333.40 (-6.88%)</td><td>298.10 <b>(+20.06%)</b></td><td>223.10 (+17.30%)</td><td>133.79 <b>(-25.31%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>569.70 (n/a)</td><td>358.02 (n/a)</td><td>248.30 (n/a)</td><td>190.20 (n/a)</td><td>179.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (-14.66%)</td><td>0.01 (-8.87%)</td><td>0.01 <b>(-28.72%)</b></td><td>0.00 (+16.07%)</td><td>0.00 <b>(-33.43%)</b></td><td>552.30 (-13.85%)</td><td>432.06 (+0.31%)</td><td>484.70 <b>(+40.29%)</b></td><td>298.20 (+17.17%)</td><td>119.35 <b>(-38.46%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>641.10 (n/a)</td><td>430.72 (n/a)</td><td>345.50 (n/a)</td><td>254.50 (n/a)</td><td>193.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (-18.92%)</td><td>0.00 <b>(-38.35%)</b></td><td>0.00 <b>(-41.82%)</b></td><td>0.00 <b>(-49.00%)</b></td><td>0.00 (+11.85%)</td><td>997.00 <b>(+96.07%)</b></td><td>617.52 <b>(+74.01%)</b></td><td>545.40 <b>(+71.89%)</b></td><td>358.90 <b>(+23.33%)</b></td><td>238.60 <b>(+168.34%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>508.50 (n/a)</td><td>354.88 (n/a)</td><td>317.30 (n/a)</td><td>291.00 (n/a)</td><td>88.92 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-9.93%)</td><td>0.02 <b>(-21.21%)</b></td><td>0.02 <b>(-24.70%)</b></td><td>0.01 <b>(-35.55%)</b></td><td>0.00 <b>(+53.78%)</b></td><td>476.50 <b>(+55.16%)</b></td><td>351.30 <b>(+31.51%)</b></td><td>335.80 <b>(+32.78%)</b></td><td>261.20 (+11.01%)</td><td>87.77 <b>(+161.46%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>307.10 (n/a)</td><td>267.12 (n/a)</td><td>252.90 (n/a)</td><td>235.30 (n/a)</td><td>33.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-1.43%)</td><td>0.01 (-13.21%)</td><td>0.01 (-16.60%)</td><td>0.01 <b>(-22.75%)</b></td><td>0.01 (+4.26%)</td><td>606.10 <b>(+29.45%)</b></td><td>423.26 (+19.34%)</td><td>445.30 (+19.93%)</td><td>239.80 (+1.44%)</td><td>155.31 <b>(+38.56%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>468.20 (n/a)</td><td>354.66 (n/a)</td><td>371.30 (n/a)</td><td>236.40 (n/a)</td><td>112.08 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-13.90%)</td><td>0.02 <b>(-21.33%)</b></td><td>0.01 <b>(-35.63%)</b></td><td>0.01 (+7.44%)</td><td>0.01 (-15.83%)</td><td>522.80 (-6.93%)</td><td>378.26 <b>(+23.20%)</b></td><td>364.80 <b>(+55.37%)</b></td><td>251.30 (+16.13%)</td><td>125.96 (-13.23%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.70 (n/a)</td><td>307.02 (n/a)</td><td>234.80 (n/a)</td><td>216.40 (n/a)</td><td>145.17 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-2.16%)</td><td>0.02 (+1.70%)</td><td>0.02 (-2.22%)</td><td>0.01 (+2.51%)</td><td>0.00 (+2.13%)</td><td>486.60 (-2.45%)</td><td>351.26 (-1.48%)</td><td>319.80 (+2.27%)</td><td>247.50 (+2.19%)</td><td>104.11 (+0.26%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>498.80 (n/a)</td><td>356.52 (n/a)</td><td>312.70 (n/a)</td><td>242.20 (n/a)</td><td>103.84 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (+15.91%)</td><td>0.01 (+1.59%)</td><td>0.01 <b>(+20.59%)</b></td><td>0.00 <b>(-67.14%)</b></td><td>0.01 <b>(+52.21%)</b></td><td>1940.70 <b>(+204.28%)</b></td><td>700.00 <b>(+47.80%)</b></td><td>437.70 (-17.07%)</td><td>220.40 (-13.70%)</td><td>703.50 <b>(+353.88%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.80 (n/a)</td><td>473.60 (n/a)</td><td>527.80 (n/a)</td><td>255.40 (n/a)</td><td>155.00 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (-2.34%)</td><td>0.01 (-11.70%)</td><td>0.01 (-15.64%)</td><td>0.01 (-16.56%)</td><td>0.00 <b>(+60.20%)</b></td><td>557.50 (+19.84%)</td><td>474.04 (+14.41%)</td><td>490.60 (+18.53%)</td><td>386.00 (+2.39%)</td><td>64.21 <b>(+93.54%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>465.20 (n/a)</td><td>414.32 (n/a)</td><td>413.90 (n/a)</td><td>377.00 (n/a)</td><td>33.18 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (-9.14%)</td><td>0.03 (-13.68%)</td><td>0.03 <b>(-26.62%)</b></td><td>0.02 (-12.26%)</td><td>0.01 (-7.83%)</td><td>520.30 (+13.98%)</td><td>383.04 (+16.07%)</td><td>379.40 <b>(+36.28%)</b></td><td>270.50 (+10.05%)</td><td>104.11 (+12.83%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>456.50 (n/a)</td><td>330.00 (n/a)</td><td>278.40 (n/a)</td><td>245.80 (n/a)</td><td>92.27 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 <b>(-31.36%)</b></td><td>0.03 (-11.88%)</td><td>0.03 <b>(-32.46%)</b></td><td>0.02 <b>(+363.52%)</b></td><td>0.00 <b>(-87.71%)</b></td><td>435.00 <b>(-78.43%)</b></td><td>410.50 <b>(-38.88%)</b></td><td>416.90 <b>(+48.05%)</b></td><td>359.40 <b>(+45.68%)</b></td><td>29.98 <b>(-96.07%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2016.40 (n/a)</td><td>671.58 (n/a)</td><td>281.60 (n/a)</td><td>246.70 (n/a)</td><td>763.41 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (+13.63%)</td><td>0.03 (-17.49%)</td><td>0.02 <b>(-51.88%)</b></td><td>0.01 <b>(-71.87%)</b></td><td>0.02 <b>(+41.96%)</b></td><td>1933.20 <b>(+255.50%)</b></td><td>688.30 <b>(+92.35%)</b></td><td>505.90 <b>(+107.85%)</b></td><td>193.50 (-12.01%)</td><td>714.99 <b>(+322.18%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.80 (n/a)</td><td>357.84 (n/a)</td><td>243.40 (n/a)</td><td>219.90 (n/a)</td><td>169.36 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (+6.48%)</td><td>0.03 (+8.61%)</td><td>0.03 <b>(+41.89%)</b></td><td>0.01 <b>(-73.92%)</b></td><td>0.02 <b>(+75.78%)</b></td><td>1902.10 <b>(+283.41%)</b></td><td>649.94 <b>(+52.30%)</b></td><td>325.40 <b>(-29.51%)</b></td><td>231.10 (-6.06%)</td><td>709.59 <b>(+586.26%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.10 (n/a)</td><td>426.76 (n/a)</td><td>461.60 (n/a)</td><td>246.00 (n/a)</td><td>103.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 <b>(+42.09%)</b></td><td>0.03 (-14.02%)</td><td>0.02 <b>(-45.95%)</b></td><td>0.02 <b>(-27.81%)</b></td><td>0.02 <b>(+134.06%)</b></td><td>607.00 <b>(+38.52%)</b></td><td>403.56 <b>(+38.31%)</b></td><td>469.00 <b>(+85.01%)</b></td><td>169.20 <b>(-29.62%)</b></td><td>182.13 <b>(+119.50%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>438.20 (n/a)</td><td>291.78 (n/a)</td><td>253.50 (n/a)</td><td>240.40 (n/a)</td><td>82.98 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (-8.47%)</td><td>0.03 (+10.09%)</td><td>0.03 (+8.77%)</td><td>0.02 <b>(+40.21%)</b></td><td>0.01 <b>(-31.93%)</b></td><td>502.10 <b>(-28.68%)</b></td><td>354.20 (-15.43%)</td><td>334.70 (-8.07%)</td><td>282.40 (+9.25%)</td><td>88.99 <b>(-48.62%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>704.00 (n/a)</td><td>418.80 (n/a)</td><td>364.10 (n/a)</td><td>258.50 (n/a)</td><td>173.21 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 <b>(+58.11%)</b></td><td>0.07 <b>(+42.10%)</b></td><td>0.06 <b>(+24.11%)</b></td><td>0.04 <b>(+30.75%)</b></td><td>0.02 <b>(+107.78%)</b></td><td>497.30 <b>(-23.52%)</b></td><td>334.40 <b>(-26.95%)</b></td><td>342.40 (-19.42%)</td><td>224.60 <b>(-36.75%)</b></td><td>107.44 (-5.38%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>650.20 (n/a)</td><td>457.78 (n/a)</td><td>424.90 (n/a)</td><td>355.10 (n/a)</td><td>113.55 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (+15.81%)</td><td>0.06 (-7.66%)</td><td>0.05 <b>(-33.52%)</b></td><td>0.04 (-11.50%)</td><td>0.02 <b>(+31.20%)</b></td><td>573.10 (+12.99%)</td><td>409.16 (+13.74%)</td><td>439.30 <b>(+50.39%)</b></td><td>226.00 (-13.64%)</td><td>151.13 <b>(+28.27%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>507.20 (n/a)</td><td>359.74 (n/a)</td><td>292.10 (n/a)</td><td>261.70 (n/a)</td><td>117.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (+1.11%)</td><td>0.07 (-11.11%)</td><td>0.07 <b>(-20.26%)</b></td><td>0.05 (+17.64%)</td><td>0.01 <b>(-22.39%)</b></td><td>414.20 (-15.00%)</td><td>328.12 (+8.66%)</td><td>312.80 <b>(+25.42%)</b></td><td>239.70 (-1.07%)</td><td>67.51 <b>(-35.70%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>487.30 (n/a)</td><td>301.98 (n/a)</td><td>249.40 (n/a)</td><td>242.30 (n/a)</td><td>104.99 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 <b>(+37.32%)</b></td><td>0.06 (-4.10%)</td><td>0.06 (+11.34%)</td><td>0.02 <b>(-55.09%)</b></td><td>0.03 <b>(+113.36%)</b></td><td>1055.80 <b>(+122.65%)</b></td><td>510.56 <b>(+37.67%)</b></td><td>373.80 (-10.19%)</td><td>197.70 <b>(-27.18%)</b></td><td>344.16 <b>(+273.66%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>474.20 (n/a)</td><td>370.86 (n/a)</td><td>416.20 (n/a)</td><td>271.50 (n/a)</td><td>92.11 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 <b>(+23.45%)</b></td><td>0.07 <b>(+27.13%)</b></td><td>0.07 <b>(+37.21%)</b></td><td>0.05 <b>(+23.61%)</b></td><td>0.02 <b>(+35.80%)</b></td><td>465.70 (-19.09%)</td><td>329.76 <b>(-20.41%)</b></td><td>298.20 <b>(-27.13%)</b></td><td>232.10 (-18.99%)</td><td>95.98 (-10.34%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>575.60 (n/a)</td><td>414.32 (n/a)</td><td>409.20 (n/a)</td><td>286.50 (n/a)</td><td>107.05 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (-6.50%)</td><td>0.04 (-12.37%)</td><td>0.04 (-16.92%)</td><td>0.03 (-5.95%)</td><td>0.01 (-4.05%)</td><td>647.30 (+6.32%)</td><td>499.20 (+14.23%)</td><td>503.90 <b>(+20.38%)</b></td><td>360.40 (+6.94%)</td><td>112.35 (+6.42%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>608.80 (n/a)</td><td>437.02 (n/a)</td><td>418.60 (n/a)</td><td>337.00 (n/a)</td><td>105.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.10 (n/a)</td><td>339.64 (n/a)</td><td>315.10 (n/a)</td><td>258.60 (n/a)</td><td>84.04 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.30 (n/a)</td><td>388.96 (n/a)</td><td>314.60 (n/a)</td><td>246.70 (n/a)</td><td>154.39 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1899.10 (n/a)</td><td>703.48 (n/a)</td><td>407.60 (n/a)</td><td>240.70 (n/a)</td><td>679.74 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>297.00 (n/a)</td><td>258.30 (n/a)</td><td>261.80 (n/a)</td><td>230.80 (n/a)</td><td>26.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>645.00 (n/a)</td><td>405.50 (n/a)</td><td>386.60 (n/a)</td><td>191.80 (n/a)</td><td>162.71 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>651.70 (n/a)</td><td>463.76 (n/a)</td><td>465.60 (n/a)</td><td>298.60 (n/a)</td><td>160.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>631.40 (n/a)</td><td>455.32 (n/a)</td><td>544.00 (n/a)</td><td>238.80 (n/a)</td><td>188.96 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>498.00 (n/a)</td><td>392.56 (n/a)</td><td>434.40 (n/a)</td><td>203.00 (n/a)</td><td>118.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>629.10 (n/a)</td><td>366.58 (n/a)</td><td>304.20 (n/a)</td><td>250.40 (n/a)</td><td>151.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (+9.68%)</td><td>0.14 (+4.38%)</td><td>0.16 (+9.30%)</td><td>0.09 (+7.23%)</td><td>0.04 <b>(+24.37%)</b></td><td>556.10 (-6.74%)</td><td>370.90 (-2.85%)</td><td>299.00 (-8.51%)</td><td>281.80 (-8.83%)</td><td>121.77 (-0.12%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>596.30 (n/a)</td><td>381.80 (n/a)</td><td>326.80 (n/a)</td><td>309.10 (n/a)</td><td>121.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.08 (n/a)</td><td>2449.30 (n/a)</td><td>783.34 (n/a)</td><td>460.90 (n/a)</td><td>225.10 (n/a)</td><td>940.15 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>584.80 (n/a)</td><td>396.18 (n/a)</td><td>400.10 (n/a)</td><td>233.10 (n/a)</td><td>161.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>533.10 (n/a)</td><td>367.42 (n/a)</td><td>385.30 (n/a)</td><td>217.20 (n/a)</td><td>142.24 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.80 (n/a)</td><td>389.06 (n/a)</td><td>416.10 (n/a)</td><td>231.30 (n/a)</td><td>143.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>534.60 (n/a)</td><td>401.56 (n/a)</td><td>426.30 (n/a)</td><td>279.60 (n/a)</td><td>109.46 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>422.70 (n/a)</td><td>287.88 (n/a)</td><td>284.30 (n/a)</td><td>166.00 (n/a)</td><td>94.88 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1838.30 (n/a)</td><td>640.52 (n/a)</td><td>295.80 (n/a)</td><td>246.00 (n/a)</td><td>679.88 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>538.10 (n/a)</td><td>372.88 (n/a)</td><td>357.90 (n/a)</td><td>184.70 (n/a)</td><td>153.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>480.20 (n/a)</td><td>350.36 (n/a)</td><td>308.40 (n/a)</td><td>232.60 (n/a)</td><td>102.23 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>461.20 (n/a)</td><td>306.94 (n/a)</td><td>280.70 (n/a)</td><td>224.00 (n/a)</td><td>90.23 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>523.00 (n/a)</td><td>407.24 (n/a)</td><td>471.00 (n/a)</td><td>228.80 (n/a)</td><td>120.96 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>363.30 (n/a)</td><td>281.84 (n/a)</td><td>286.10 (n/a)</td><td>222.40 (n/a)</td><td>54.37 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1396.30 (n/a)</td><td>632.34 (n/a)</td><td>422.50 (n/a)</td><td>296.00 (n/a)</td><td>444.28 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1041.30 (n/a)</td><td>508.00 (n/a)</td><td>450.80 (n/a)</td><td>227.70 (n/a)</td><td>330.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1040.10 (n/a)</td><td>574.22 (n/a)</td><td>537.10 (n/a)</td><td>282.70 (n/a)</td><td>282.61 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>525.30 (n/a)</td><td>359.78 (n/a)</td><td>395.10 (n/a)</td><td>172.30 (n/a)</td><td>155.32 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>842.40 (n/a)</td><td>406.60 (n/a)</td><td>307.10 (n/a)</td><td>249.00 (n/a)</td><td>245.92 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.70 (n/a)</td><td>394.40 (n/a)</td><td>329.70 (n/a)</td><td>225.30 (n/a)</td><td>165.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1026.40 (n/a)</td><td>517.08 (n/a)</td><td>489.00 (n/a)</td><td>228.40 (n/a)</td><td>307.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>393.40 (n/a)</td><td>336.18 (n/a)</td><td>314.80 (n/a)</td><td>293.90 (n/a)</td><td>44.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>657.10 (n/a)</td><td>429.14 (n/a)</td><td>338.10 (n/a)</td><td>276.40 (n/a)</td><td>172.22 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.70 (n/a)</td><td>340.34 (n/a)</td><td>277.20 (n/a)</td><td>242.20 (n/a)</td><td>156.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1025.70 (n/a)</td><td>556.04 (n/a)</td><td>525.00 (n/a)</td><td>276.50 (n/a)</td><td>307.68 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>441.10 (n/a)</td><td>342.04 (n/a)</td><td>345.70 (n/a)</td><td>224.20 (n/a)</td><td>93.88 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.30 (n/a)</td><td>432.70 (n/a)</td><td>390.80 (n/a)</td><td>362.70 (n/a)</td><td>102.42 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>630.50 (n/a)</td><td>369.20 (n/a)</td><td>293.90 (n/a)</td><td>248.10 (n/a)</td><td>155.35 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1992.30 (n/a)</td><td>697.40 (n/a)</td><td>436.00 (n/a)</td><td>232.70 (n/a)</td><td>733.18 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>613.80 (n/a)</td><td>479.22 (n/a)</td><td>507.60 (n/a)</td><td>229.10 (n/a)</td><td>146.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>558.10 (n/a)</td><td>388.06 (n/a)</td><td>425.70 (n/a)</td><td>237.90 (n/a)</td><td>135.96 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1035.10 (n/a)</td><td>531.64 (n/a)</td><td>467.30 (n/a)</td><td>268.90 (n/a)</td><td>305.26 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>611.10 (n/a)</td><td>447.84 (n/a)</td><td>461.80 (n/a)</td><td>305.70 (n/a)</td><td>117.64 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>492.80 (n/a)</td><td>400.70 (n/a)</td><td>462.50 (n/a)</td><td>232.20 (n/a)</td><td>115.62 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>537.30 (n/a)</td><td>331.30 (n/a)</td><td>300.00 (n/a)</td><td>199.00 (n/a)</td><td>124.78 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>590.20 (n/a)</td><td>420.68 (n/a)</td><td>413.20 (n/a)</td><td>283.20 (n/a)</td><td>131.31 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>378.50 (n/a)</td><td>309.76 (n/a)</td><td>314.60 (n/a)</td><td>249.70 (n/a)</td><td>59.21 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>620.10 (n/a)</td><td>448.14 (n/a)</td><td>443.90 (n/a)</td><td>285.30 (n/a)</td><td>141.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.68 (+9.14%)</td><td>0.38 (-16.69%)</td><td>0.36 (-15.84%)</td><td>0.13 <b>(-60.86%)</b></td><td>0.20 <b>(+60.26%)</b></td><td>1698.60 <b>(+155.47%)</b></td><td>770.62 <b>(+50.46%)</b></td><td>619.00 (+18.81%)</td><td>323.10 (-8.37%)</td><td>533.72 <b>(+307.40%)</b></td><td>29.21 (+9.14%)</td><td>16.24 (-16.69%)</td><td>15.24 (-15.84%)</td><td>5.56 <b>(-60.86%)</b></td><td>8.44 <b>(+60.26%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.63 (n/a)</td><td>0.46 (n/a)</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.12 (n/a)</td><td>664.90 (n/a)</td><td>512.16 (n/a)</td><td>521.00 (n/a)</td><td>352.60 (n/a)</td><td>131.01 (n/a)</td><td>26.77 (n/a)</td><td>19.49 (n/a)</td><td>18.11 (n/a)</td><td>14.19 (n/a)</td><td>5.27 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.79 <b>(+32.74%)</b></td><td>0.38 (-6.83%)</td><td>0.32 <b>(-25.06%)</b></td><td>0.12 (+11.60%)</td><td>0.27 <b>(+42.63%)</b></td><td>1788.50 (-10.40%)</td><td>877.82 (+12.57%)</td><td>696.20 <b>(+33.42%)</b></td><td>279.60 <b>(-24.66%)</b></td><td>604.09 (-11.83%)</td><td>33.75 <b>(+32.74%)</b></td><td>16.15 (-6.83%)</td><td>13.55 <b>(-25.06%)</b></td><td>5.28 (+11.60%)</td><td>11.32 <b>(+42.63%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.60 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.11 (n/a)</td><td>0.19 (n/a)</td><td>1996.00 (n/a)</td><td>779.80 (n/a)</td><td>521.80 (n/a)</td><td>371.10 (n/a)</td><td>685.12 (n/a)</td><td>25.43 (n/a)</td><td>17.33 (n/a)</td><td>18.09 (n/a)</td><td>4.73 (n/a)</td><td>7.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.31 (-0.55%)</td><td>0.30 (-1.07%)</td><td>0.31 (-0.93%)</td><td>0.29 (-3.32%)</td><td>0.01 <b>(+128.64%)</b></td><td>85776.40 (+3.43%)</td><td>82920.94 (+1.10%)</td><td>82487.50 (+0.94%)</td><td>81840.40 (+0.55%)</td><td>1631.01 <b>(+138.40%)</b></td><td>209.92 (-0.55%)</td><td>207.25 (-1.07%)</td><td>208.27 (-0.93%)</td><td>200.29 (-3.32%)</td><td>3.98 <b>(+128.64%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>82928.50 (n/a)</td><td>82016.36 (n/a)</td><td>81720.70 (n/a)</td><td>81393.50 (n/a)</td><td>684.15 (n/a)</td><td>211.07 (n/a)</td><td>209.48 (n/a)</td><td>210.23 (n/a)</td><td>207.16 (n/a)</td><td>1.74 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>1.05 (+2.41%)</td><td>1.02 (+0.95%)</td><td>1.02 (+1.58%)</td><td>1.00 (-0.43%)</td><td>0.02 <b>(+70.56%)</b></td><td>25291.40 (+0.43%)</td><td>24619.66 (-0.92%)</td><td>24615.00 (-1.55%)</td><td>23901.60 (-2.35%)</td><td>515.47 <b>(+67.43%)</b></td><td>718.77 (+2.41%)</td><td>698.06 (+0.95%)</td><td>697.94 (+1.58%)</td><td>679.28 (-0.43%)</td><td>14.66 <b>(+70.56%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25183.00 (n/a)</td><td>24848.72 (n/a)</td><td>25003.30 (n/a)</td><td>24477.30 (n/a)</td><td>307.87 (n/a)</td><td>701.87 (n/a)</td><td>691.46 (n/a)</td><td>687.10 (n/a)</td><td>682.20 (n/a)</td><td>8.59 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.82 (+0.38%)</td><td>0.81 (+0.85%)</td><td>0.82 (+0.39%)</td><td>0.79 (+4.93%)</td><td>0.01 <b>(-47.18%)</b></td><td>95048.20 (-4.70%)</td><td>93214.16 (-0.91%)</td><td>92479.70 (-0.39%)</td><td>91612.30 (-0.38%)</td><td>1616.11 <b>(-49.95%)</b></td><td>750.11 (+0.38%)</td><td>737.40 (+0.85%)</td><td>743.08 (+0.39%)</td><td>723.00 (+4.93%)</td><td>12.73 <b>(-47.18%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.76 (n/a)</td><td>0.03 (n/a)</td><td>99738.80 (n/a)</td><td>94069.52 (n/a)</td><td>92837.30 (n/a)</td><td>91958.60 (n/a)</td><td>3228.92 (n/a)</td><td>747.29 (n/a)</td><td>731.18 (n/a)</td><td>740.21 (n/a)</td><td>688.99 (n/a)</td><td>24.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.77 (-0.50%)</td><td>0.76 (+0.04%)</td><td>0.77 (+0.18%)</td><td>0.75 (+0.01%)</td><td>0.01 (-15.55%)</td><td>100859.80 (-0.01%)</td><td>98961.86 (-0.04%)</td><td>98586.80 (-0.18%)</td><td>97981.30 (+0.50%)</td><td>1111.65 (-14.98%)</td><td>701.35 (-0.50%)</td><td>694.47 (+0.04%)</td><td>697.05 (+0.18%)</td><td>681.34 (+0.01%)</td><td>7.71 (-15.55%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100865.80 (n/a)</td><td>99005.60 (n/a)</td><td>98768.60 (n/a)</td><td>97489.40 (n/a)</td><td>1307.49 (n/a)</td><td>704.89 (n/a)</td><td>694.19 (n/a)</td><td>695.76 (n/a)</td><td>681.30 (n/a)</td><td>9.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.80 (+0.34%)</td><td>0.79 (+0.47%)</td><td>0.79 (-0.16%)</td><td>0.79 (+1.18%)</td><td>0.01 <b>(-26.32%)</b></td><td>95689.80 (-1.17%)</td><td>95077.52 (-0.47%)</td><td>95282.10 (+0.16%)</td><td>94235.00 (-0.34%)</td><td>658.28 <b>(-27.45%)</b></td><td>729.24 (+0.34%)</td><td>722.80 (+0.47%)</td><td>721.22 (-0.16%)</td><td>718.15 (+1.18%)</td><td>5.01 <b>(-26.32%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96823.10 (n/a)</td><td>95529.10 (n/a)</td><td>95128.30 (n/a)</td><td>94556.50 (n/a)</td><td>907.33 (n/a)</td><td>726.76 (n/a)</td><td>719.41 (n/a)</td><td>722.39 (n/a)</td><td>709.74 (n/a)</td><td>6.81 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.63 <b>(+33.97%)</b></td><td>4.05 (+17.57%)</td><td>4.11 (+1.63%)</td><td>2.15 (+10.19%)</td><td>1.60 <b>(+64.39%)</b></td><td>4152.80 (-9.25%)</td><td>2543.96 (-9.75%)</td><td>2169.50 (-1.60%)</td><td>1584.30 <b>(-25.36%)</b></td><td>1120.85 (+7.20%)</td><td>338.86 <b>(+33.97%)</b></td><td>244.01 (+17.57%)</td><td>247.46 (+1.63%)</td><td>129.28 (+10.19%)</td><td>96.18 <b>(+64.39%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>4.20 (n/a)</td><td>3.45 (n/a)</td><td>4.04 (n/a)</td><td>1.95 (n/a)</td><td>0.97 (n/a)</td><td>4575.90 (n/a)</td><td>2818.66 (n/a)</td><td>2204.80 (n/a)</td><td>2122.50 (n/a)</td><td>1045.60 (n/a)</td><td>252.94 (n/a)</td><td>207.54 (n/a)</td><td>243.50 (n/a)</td><td>117.33 (n/a)</td><td>58.51 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>4.40 (-7.67%)</td><td>2.72 <b>(-31.54%)</b></td><td>2.23 <b>(-47.99%)</b></td><td>2.05 <b>(-32.27%)</b></td><td>0.97 (+13.91%)</td><td>4352.00 <b>(+47.66%)</b></td><td>3541.38 <b>(+51.61%)</b></td><td>3993.70 <b>(+92.25%)</b></td><td>2025.20 (+8.31%)</td><td>934.82 <b>(+74.59%)</b></td><td>265.10 (-7.67%)</td><td>163.79 <b>(-31.54%)</b></td><td>134.43 <b>(-47.99%)</b></td><td>123.36 <b>(-32.27%)</b></td><td>58.63 (+13.91%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>4.77 (n/a)</td><td>3.97 (n/a)</td><td>4.29 (n/a)</td><td>3.02 (n/a)</td><td>0.85 (n/a)</td><td>2947.40 (n/a)</td><td>2335.78 (n/a)</td><td>2077.30 (n/a)</td><td>1869.90 (n/a)</td><td>535.43 (n/a)</td><td>287.11 (n/a)</td><td>239.27 (n/a)</td><td>258.45 (n/a)</td><td>182.15 (n/a)</td><td>51.47 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.66 (-7.60%)</td><td>2.89 (+3.96%)</td><td>2.94 <b>(+35.51%)</b></td><td>2.19 (+13.94%)</td><td>0.62 <b>(-35.41%)</b></td><td>4068.00 (-12.24%)</td><td>3203.74 (-8.65%)</td><td>3030.30 <b>(-26.20%)</b></td><td>2435.20 (+8.23%)</td><td>701.43 <b>(-35.85%)</b></td><td>220.47 (-7.60%)</td><td>174.08 (+3.96%)</td><td>177.17 <b>(+35.51%)</b></td><td>131.97 (+13.94%)</td><td>37.45 <b>(-35.41%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.96 (n/a)</td><td>2.78 (n/a)</td><td>2.17 (n/a)</td><td>1.92 (n/a)</td><td>0.96 (n/a)</td><td>4635.30 (n/a)</td><td>3507.28 (n/a)</td><td>4106.30 (n/a)</td><td>2250.00 (n/a)</td><td>1093.39 (n/a)</td><td>238.61 (n/a)</td><td>167.46 (n/a)</td><td>130.74 (n/a)</td><td>115.82 (n/a)</td><td>57.99 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>6.35 (-5.40%)</td><td>4.96 (-2.57%)</td><td>4.80 (+0.54%)</td><td>4.38 (+1.59%)</td><td>0.81 (-13.55%)</td><td>7966.20 (-1.56%)</td><td>7156.78 (+2.18%)</td><td>7267.20 (-0.53%)</td><td>5490.00 (+5.71%)</td><td>1001.25 (-7.44%)</td><td>391.16 (-5.40%)</td><td>305.61 (-2.57%)</td><td>295.50 (+0.54%)</td><td>269.57 (+1.59%)</td><td>49.77 (-13.55%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>6.71 (n/a)</td><td>5.09 (n/a)</td><td>4.77 (n/a)</td><td>4.31 (n/a)</td><td>0.93 (n/a)</td><td>8092.60 (n/a)</td><td>7004.30 (n/a)</td><td>7306.10 (n/a)</td><td>5193.60 (n/a)</td><td>1081.73 (n/a)</td><td>413.49 (n/a)</td><td>313.66 (n/a)</td><td>293.93 (n/a)</td><td>265.36 (n/a)</td><td>57.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.43 (-10.87%)</td><td>4.44 (-18.99%)</td><td>4.49 (-19.94%)</td><td>3.07 <b>(-29.03%)</b></td><td>0.87 <b>(+26.09%)</b></td><td>11374.10 <b>(+40.91%)</b></td><td>8145.20 <b>(+26.18%)</b></td><td>7758.80 <b>(+24.90%)</b></td><td>6422.20 (+12.20%)</td><td>1898.99 <b>(+103.07%)</b></td><td>334.39 (-10.87%)</td><td>273.49 (-18.99%)</td><td>276.78 (-19.94%)</td><td>188.80 <b>(-29.03%)</b></td><td>53.52 <b>(+26.09%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>6.09 (n/a)</td><td>5.48 (n/a)</td><td>5.61 (n/a)</td><td>4.32 (n/a)</td><td>0.69 (n/a)</td><td>8071.70 (n/a)</td><td>6455.20 (n/a)</td><td>6211.90 (n/a)</td><td>5724.10 (n/a)</td><td>935.14 (n/a)</td><td>375.17 (n/a)</td><td>337.58 (n/a)</td><td>345.70 (n/a)</td><td>266.05 (n/a)</td><td>42.44 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.71 (-14.40%)</td><td>5.29 (-1.02%)</td><td>5.22 (-0.65%)</td><td>4.62 (+3.99%)</td><td>0.44 <b>(-46.50%)</b></td><td>7550.70 (-3.84%)</td><td>6632.52 (-0.18%)</td><td>6677.60 (+0.66%)</td><td>6110.70 (+16.82%)</td><td>584.49 <b>(-39.23%)</b></td><td>351.43 (-14.40%)</td><td>325.70 (-1.02%)</td><td>321.59 (-0.65%)</td><td>284.41 (+3.99%)</td><td>27.35 <b>(-46.50%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>6.67 (n/a)</td><td>5.34 (n/a)</td><td>5.26 (n/a)</td><td>4.44 (n/a)</td><td>0.83 (n/a)</td><td>7852.20 (n/a)</td><td>6644.36 (n/a)</td><td>6633.90 (n/a)</td><td>5230.90 (n/a)</td><td>961.75 (n/a)</td><td>410.54 (n/a)</td><td>329.07 (n/a)</td><td>323.71 (n/a)</td><td>273.49 (n/a)</td><td>51.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.78 (-0.43%)</td><td>0.77 (-0.31%)</td><td>0.77 (-1.37%)</td><td>0.77 (+2.07%)</td><td>0.01 <b>(-51.16%)</b></td><td>98446.60 (-2.03%)</td><td>97633.30 (+0.29%)</td><td>98042.80 (+1.39%)</td><td>96444.20 (+0.43%)</td><td>859.71 <b>(-52.10%)</b></td><td>712.53 (-0.43%)</td><td>703.90 (-0.31%)</td><td>700.91 (-1.37%)</td><td>698.04 (+2.07%)</td><td>6.22 <b>(-51.16%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100485.30 (n/a)</td><td>97346.86 (n/a)</td><td>96701.70 (n/a)</td><td>96033.90 (n/a)</td><td>1794.72 (n/a)</td><td>715.57 (n/a)</td><td>706.11 (n/a)</td><td>710.63 (n/a)</td><td>683.88 (n/a)</td><td>12.74 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.76 (-1.79%)</td><td>0.75 (-1.07%)</td><td>0.75 (-1.51%)</td><td>0.74 (+0.70%)</td><td>0.01 <b>(-50.01%)</b></td><td>102154.30 (-0.70%)</td><td>100579.66 (+1.06%)</td><td>100438.80 (+1.53%)</td><td>99747.00 (+1.82%)</td><td>965.14 <b>(-49.66%)</b></td><td>688.94 (-1.79%)</td><td>683.28 (-1.07%)</td><td>684.19 (-1.51%)</td><td>672.70 (+0.70%)</td><td>6.51 <b>(-50.01%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.01 (n/a)</td><td>102870.90 (n/a)</td><td>99523.38 (n/a)</td><td>98926.30 (n/a)</td><td>97964.80 (n/a)</td><td>1917.35 (n/a)</td><td>701.47 (n/a)</td><td>690.69 (n/a)</td><td>694.65 (n/a)</td><td>668.02 (n/a)</td><td>13.01 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.81 (+0.10%)</td><td>0.80 (+0.54%)</td><td>0.80 (+0.13%)</td><td>0.79 (+1.38%)</td><td>0.01 <b>(-35.44%)</b></td><td>95586.60 (-1.36%)</td><td>94338.44 (-0.55%)</td><td>94529.80 (-0.13%)</td><td>93320.10 (-0.10%)</td><td>957.37 <b>(-36.38%)</b></td><td>736.38 (+0.10%)</td><td>728.50 (+0.54%)</td><td>726.96 (+0.13%)</td><td>718.92 (+1.38%)</td><td>7.39 <b>(-35.44%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96907.00 (n/a)</td><td>94860.40 (n/a)</td><td>94653.90 (n/a)</td><td>93415.30 (n/a)</td><td>1504.77 (n/a)</td><td>735.63 (n/a)</td><td>724.57 (n/a)</td><td>726.01 (n/a)</td><td>709.13 (n/a)</td><td>11.44 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.95 (+7.38%)</td><td>2.56 (-11.00%)</td><td>2.05 <b>(-41.62%)</b></td><td>1.24 <b>(-29.89%)</b></td><td>1.27 <b>(+30.56%)</b></td><td>6515.50 <b>(+42.64%)</b></td><td>3873.12 <b>(+23.70%)</b></td><td>3932.50 <b>(+71.28%)</b></td><td>2041.40 (-6.87%)</td><td>1897.45 <b>(+57.11%)</b></td><td>1035.52 (+7.38%)</td><td>670.81 (-11.00%)</td><td>537.56 <b>(-41.62%)</b></td><td>324.44 <b>(-29.89%)</b></td><td>332.62 <b>(+30.56%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.68 (n/a)</td><td>2.87 (n/a)</td><td>3.51 (n/a)</td><td>1.76 (n/a)</td><td>0.97 (n/a)</td><td>4567.70 (n/a)</td><td>3130.94 (n/a)</td><td>2296.00 (n/a)</td><td>2192.10 (n/a)</td><td>1207.73 (n/a)</td><td>964.36 (n/a)</td><td>753.71 (n/a)</td><td>920.72 (n/a)</td><td>462.80 (n/a)</td><td>254.76 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.21 <b>(-27.64%)</b></td><td>0.19 (-13.43%)</td><td>0.19 (-1.57%)</td><td>0.15 (-7.83%)</td><td>0.02 <b>(-57.56%)</b></td><td>8178.00 (+8.49%)</td><td>6647.66 (+11.77%)</td><td>6524.70 (+1.60%)</td><td>5852.20 <b>(+38.20%)</b></td><td>903.81 <b>(-34.01%)</b></td><td>11.47 <b>(-27.64%)</b></td><td>10.23 (-13.43%)</td><td>10.29 (-1.57%)</td><td>8.21 (-7.83%)</td><td>1.24 <b>(-57.56%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>7537.90 (n/a)</td><td>5947.84 (n/a)</td><td>6422.20 (n/a)</td><td>4234.60 (n/a)</td><td>1369.57 (n/a)</td><td>15.85 (n/a)</td><td>11.82 (n/a)</td><td>10.45 (n/a)</td><td>8.90 (n/a)</td><td>2.92 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.73 (n/a)</td><td>3.55 (n/a)</td><td>3.70 (n/a)</td><td>3.16 (n/a)</td><td>0.25 (n/a)</td><td>3.73 (n/a)</td><td>3.54 (n/a)</td><td>3.70 (n/a)</td><td>3.16 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>7.03 (-6.90%)</td><td>6.14 (-7.97%)</td><td>5.99 (-16.65%)</td><td>5.45 (-3.02%)</td><td>0.61 <b>(-36.98%)</b></td><td>7.03 (-6.90%)</td><td>6.14 (-7.97%)</td><td>5.98 (-16.65%)</td><td>5.45 (-3.02%)</td><td>0.61 <b>(-36.98%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>7.55 (n/a)</td><td>6.68 (n/a)</td><td>7.18 (n/a)</td><td>5.62 (n/a)</td><td>0.96 (n/a)</td><td>7.55 (n/a)</td><td>6.67 (n/a)</td><td>7.18 (n/a)</td><td>5.61 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>10.90 <b>(+24.74%)</b></td><td>8.60 (+7.79%)</td><td>8.29 (+1.69%)</td><td>6.89 (-4.45%)</td><td>1.53 <b>(+124.20%)</b></td><td>10.89 <b>(+24.74%)</b></td><td>8.59 (+7.79%)</td><td>8.28 (+1.69%)</td><td>6.89 (-4.45%)</td><td>1.53 <b>(+124.20%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>8.73 (n/a)</td><td>7.98 (n/a)</td><td>8.15 (n/a)</td><td>7.22 (n/a)</td><td>0.68 (n/a)</td><td>8.73 (n/a)</td><td>7.97 (n/a)</td><td>8.15 (n/a)</td><td>7.21 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.61 (n/a)</td><td>3.52 (n/a)</td><td>3.58 (n/a)</td><td>3.36 (n/a)</td><td>0.10 (n/a)</td><td>3.61 (n/a)</td><td>3.52 (n/a)</td><td>3.58 (n/a)</td><td>3.36 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>6.13 (-11.62%)</td><td>5.46 (-11.25%)</td><td>5.67 (-12.39%)</td><td>4.27 (-8.65%)</td><td>0.70 <b>(-23.94%)</b></td><td>6.12 (-11.62%)</td><td>5.46 (-11.25%)</td><td>5.67 (-12.39%)</td><td>4.27 (-8.65%)</td><td>0.70 <b>(-23.94%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>6.93 (n/a)</td><td>6.15 (n/a)</td><td>6.48 (n/a)</td><td>4.68 (n/a)</td><td>0.92 (n/a)</td><td>6.93 (n/a)</td><td>6.15 (n/a)</td><td>6.47 (n/a)</td><td>4.68 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>14.08 (-0.11%)</td><td>11.17 (-13.46%)</td><td>11.76 (-15.33%)</td><td>7.65 (-17.17%)</td><td>3.01 <b>(+45.33%)</b></td><td>14.07 (-0.11%)</td><td>11.16 (-13.46%)</td><td>11.75 (-15.33%)</td><td>7.64 (-17.17%)</td><td>3.01 <b>(+45.33%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>14.10 (n/a)</td><td>12.91 (n/a)</td><td>13.88 (n/a)</td><td>9.23 (n/a)</td><td>2.07 (n/a)</td><td>14.09 (n/a)</td><td>12.90 (n/a)</td><td>13.88 (n/a)</td><td>9.22 (n/a)</td><td>2.07 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.25 (+7.60%)</td><td>1.64 (-19.94%)</td><td>1.24 <b>(-39.45%)</b></td><td>1.03 (-5.52%)</td><td>0.92 (+5.27%)</td><td>3.25 (+7.60%)</td><td>1.63 (-19.94%)</td><td>1.24 <b>(-39.45%)</b></td><td>1.03 (-5.52%)</td><td>0.92 (+5.27%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.03 (n/a)</td><td>2.04 (n/a)</td><td>2.05 (n/a)</td><td>1.09 (n/a)</td><td>0.87 (n/a)</td><td>3.02 (n/a)</td><td>2.04 (n/a)</td><td>2.05 (n/a)</td><td>1.09 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.48 <b>(+39.23%)</b></td><td>0.31 <b>(+74.81%)</b></td><td>0.32 <b>(+254.21%)</b></td><td>0.07 (+2.25%)</td><td>0.16 (+17.33%)</td><td>0.47 <b>(+39.23%)</b></td><td>0.31 <b>(+74.81%)</b></td><td>0.31 <b>(+254.21%)</b></td><td>0.07 (+2.25%)</td><td>0.16 (+17.33%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.35 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.14 (n/a)</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.74 (+14.86%)</td><td>0.46 (-4.36%)</td><td>0.39 (-6.96%)</td><td>0.35 (+0.11%)</td><td>0.16 <b>(+29.20%)</b></td><td>0.73 (+14.86%)</td><td>0.46 (-4.36%)</td><td>0.39 (-6.96%)</td><td>0.35 (+0.11%)</td><td>0.16 <b>(+29.20%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.64 (n/a)</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.13 (n/a)</td><td>0.63 (n/a)</td><td>0.48 (n/a)</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>2.18 (-6.77%)</td><td>1.45 <b>(-20.48%)</b></td><td>1.46 <b>(-36.51%)</b></td><td>0.46 (+3.55%)</td><td>0.63 <b>(-22.60%)</b></td><td>2.15 (-6.77%)</td><td>1.43 <b>(-20.48%)</b></td><td>1.44 <b>(-36.51%)</b></td><td>0.45 (+3.55%)</td><td>0.62 <b>(-22.60%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>2.34 (n/a)</td><td>1.82 (n/a)</td><td>2.30 (n/a)</td><td>0.44 (n/a)</td><td>0.82 (n/a)</td><td>2.30 (n/a)</td><td>1.79 (n/a)</td><td>2.26 (n/a)</td><td>0.44 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.80 (n/a)</td><td>407.10 (n/a)</td><td>434.20 (n/a)</td><td>195.20 (n/a)</td><td>165.18 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.20 (n/a)</td><td>446.04 (n/a)</td><td>474.50 (n/a)</td><td>174.30 (n/a)</td><td>165.77 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.30 (n/a)</td><td>350.18 (n/a)</td><td>296.00 (n/a)</td><td>267.60 (n/a)</td><td>93.86 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>497.40 (n/a)</td><td>401.16 (n/a)</td><td>473.40 (n/a)</td><td>226.90 (n/a)</td><td>123.36 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.70 (n/a)</td><td>400.92 (n/a)</td><td>427.30 (n/a)</td><td>242.70 (n/a)</td><td>106.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.10 (n/a)</td><td>429.60 (n/a)</td><td>425.10 (n/a)</td><td>256.60 (n/a)</td><td>113.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>326.00 (n/a)</td><td>306.94 (n/a)</td><td>303.70 (n/a)</td><td>284.00 (n/a)</td><td>16.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.40 (n/a)</td><td>477.54 (n/a)</td><td>534.80 (n/a)</td><td>196.40 (n/a)</td><td>163.62 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.90 (n/a)</td><td>445.32 (n/a)</td><td>478.90 (n/a)</td><td>252.10 (n/a)</td><td>118.88 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1037.00 (n/a)</td><td>474.42 (n/a)</td><td>417.50 (n/a)</td><td>207.90 (n/a)</td><td>333.21 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.90 (n/a)</td><td>511.96 (n/a)</td><td>497.50 (n/a)</td><td>423.00 (n/a)</td><td>86.47 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.60 (n/a)</td><td>426.36 (n/a)</td><td>390.50 (n/a)</td><td>326.00 (n/a)</td><td>131.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>310.00 (n/a)</td><td>283.58 (n/a)</td><td>283.10 (n/a)</td><td>241.10 (n/a)</td><td>26.49 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.40 (n/a)</td><td>425.38 (n/a)</td><td>441.00 (n/a)</td><td>244.50 (n/a)</td><td>160.19 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>669.40 (n/a)</td><td>417.62 (n/a)</td><td>276.00 (n/a)</td><td>264.40 (n/a)</td><td>204.24 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>577.70 (n/a)</td><td>395.62 (n/a)</td><td>338.60 (n/a)</td><td>243.40 (n/a)</td><td>138.33 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>541.10 (n/a)</td><td>362.36 (n/a)</td><td>276.50 (n/a)</td><td>241.00 (n/a)</td><td>137.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>642.50 (n/a)</td><td>483.86 (n/a)</td><td>502.20 (n/a)</td><td>347.40 (n/a)</td><td>127.27 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (-9.52%)</td><td>0.08 (-2.32%)</td><td>0.10 (+12.31%)</td><td>0.05 (+0.09%)</td><td>0.02 (-12.73%)</td><td>667.30 (-0.10%)</td><td>427.64 (+1.01%)</td><td>344.90 (-10.95%)</td><td>316.40 (+10.51%)</td><td>149.79 (-3.70%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>668.00 (n/a)</td><td>423.36 (n/a)</td><td>387.30 (n/a)</td><td>286.30 (n/a)</td><td>155.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>553.70 (n/a)</td><td>484.84 (n/a)</td><td>533.90 (n/a)</td><td>390.10 (n/a)</td><td>82.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1305.50 (n/a)</td><td>587.16 (n/a)</td><td>443.00 (n/a)</td><td>220.20 (n/a)</td><td>425.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>590.50 (n/a)</td><td>438.00 (n/a)</td><td>412.30 (n/a)</td><td>302.20 (n/a)</td><td>125.42 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>637.00 (n/a)</td><td>478.76 (n/a)</td><td>535.60 (n/a)</td><td>292.50 (n/a)</td><td>173.06 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>703.50 (n/a)</td><td>487.14 (n/a)</td><td>454.20 (n/a)</td><td>364.10 (n/a)</td><td>141.37 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 <b>(-23.50%)</b></td><td>0.01 <b>(-30.81%)</b></td><td>0.01 <b>(-30.16%)</b></td><td>0.01 <b>(-29.04%)</b></td><td>0.00 <b>(-21.50%)</b></td><td>580.50 <b>(+40.93%)</b></td><td>443.22 <b>(+45.33%)</b></td><td>450.80 <b>(+43.16%)</b></td><td>284.30 <b>(+30.71%)</b></td><td>109.99 <b>(+42.62%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>411.90 (n/a)</td><td>304.98 (n/a)</td><td>314.90 (n/a)</td><td>217.50 (n/a)</td><td>77.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-14.63%)</td><td>0.01 (-14.68%)</td><td>0.01 (-15.38%)</td><td>0.01 (-14.46%)</td><td>0.00 (-8.16%)</td><td>598.60 (+16.91%)</td><td>408.58 (+19.45%)</td><td>361.40 (+18.18%)</td><td>251.50 (+17.14%)</td><td>168.06 <b>(+27.22%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.00 (n/a)</td><td>342.06 (n/a)</td><td>305.80 (n/a)</td><td>214.70 (n/a)</td><td>132.10 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(+31.20%)</b></td><td>0.02 <b>(+24.39%)</b></td><td>0.02 (+11.98%)</td><td>0.01 (-1.65%)</td><td>0.01 <b>(+21.40%)</b></td><td>605.00 (+1.68%)</td><td>311.94 (-17.96%)</td><td>272.10 (-10.70%)</td><td>173.90 <b>(-23.76%)</b></td><td>170.47 (-0.69%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.00 (n/a)</td><td>380.24 (n/a)</td><td>304.70 (n/a)</td><td>228.10 (n/a)</td><td>171.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(+26.45%)</b></td><td>0.01 <b>(+25.89%)</b></td><td>0.01 <b>(+55.75%)</b></td><td>0.01 (+14.00%)</td><td>0.01 <b>(+39.64%)</b></td><td>533.00 (-12.28%)</td><td>355.64 (-16.37%)</td><td>286.00 <b>(-35.80%)</b></td><td>188.60 <b>(-20.89%)</b></td><td>159.43 (+7.14%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>607.60 (n/a)</td><td>425.24 (n/a)</td><td>445.50 (n/a)</td><td>238.40 (n/a)</td><td>148.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 <b>(-32.29%)</b></td><td>0.01 (-14.11%)</td><td>0.01 (-12.67%)</td><td>0.01 <b>(+367.39%)</b></td><td>0.00 <b>(-65.38%)</b></td><td>523.80 <b>(-78.60%)</b></td><td>459.40 <b>(-41.20%)</b></td><td>516.80 (+14.51%)</td><td>299.10 <b>(+47.70%)</b></td><td>96.54 <b>(-89.75%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2448.20 (n/a)</td><td>781.34 (n/a)</td><td>451.30 (n/a)</td><td>202.50 (n/a)</td><td>942.27 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (-1.67%)</td><td>0.01 (+8.82%)</td><td>0.01 (-5.42%)</td><td>0.01 <b>(+259.98%)</b></td><td>0.00 <b>(-30.76%)</b></td><td>612.90 <b>(-72.22%)</b></td><td>517.36 <b>(-36.92%)</b></td><td>567.20 (+5.72%)</td><td>295.20 (+1.69%)</td><td>130.02 <b>(-83.40%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2206.20 (n/a)</td><td>820.18 (n/a)</td><td>536.50 (n/a)</td><td>290.30 (n/a)</td><td>783.25 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (-3.29%)</td><td>0.03 (+1.06%)</td><td>0.03 (-2.66%)</td><td>0.02 (+9.07%)</td><td>0.01 (-11.38%)</td><td>527.00 (-8.33%)</td><td>330.88 (-3.76%)</td><td>299.90 (+2.74%)</td><td>235.90 (+3.37%)</td><td>118.81 (-16.41%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.90 (n/a)</td><td>343.82 (n/a)</td><td>291.90 (n/a)</td><td>228.20 (n/a)</td><td>142.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (-3.73%)</td><td>0.03 <b>(+21.61%)</b></td><td>0.03 <b>(+92.89%)</b></td><td>0.01 <b>(+25.84%)</b></td><td>0.01 (-3.98%)</td><td>593.20 <b>(-20.53%)</b></td><td>340.12 <b>(-20.89%)</b></td><td>234.60 <b>(-48.17%)</b></td><td>227.60 (+3.88%)</td><td>161.87 <b>(-22.38%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>746.40 (n/a)</td><td>429.92 (n/a)</td><td>452.60 (n/a)</td><td>219.10 (n/a)</td><td>208.53 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (+1.86%)</td><td>0.03 (+5.05%)</td><td>0.03 (+13.03%)</td><td>0.02 <b>(-26.95%)</b></td><td>0.01 <b>(+31.75%)</b></td><td>544.20 <b>(+36.91%)</b></td><td>316.88 (+0.32%)</td><td>260.20 (-11.56%)</td><td>237.70 (-1.82%)</td><td>128.81 <b>(+79.89%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>397.50 (n/a)</td><td>315.88 (n/a)</td><td>294.20 (n/a)</td><td>242.10 (n/a)</td><td>71.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 <b>(+34.23%)</b></td><td>0.03 (+16.44%)</td><td>0.03 <b>(+46.60%)</b></td><td>0.01 <b>(-24.33%)</b></td><td>0.01 <b>(+105.05%)</b></td><td>563.70 <b>(+32.17%)</b></td><td>355.44 (+1.32%)</td><td>264.60 <b>(-31.79%)</b></td><td>171.10 <b>(-25.48%)</b></td><td>184.15 <b>(+122.94%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>426.50 (n/a)</td><td>350.82 (n/a)</td><td>387.90 (n/a)</td><td>229.60 (n/a)</td><td>82.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (+0.67%)</td><td>0.02 (-5.13%)</td><td>0.03 (-0.86%)</td><td>0.01 <b>(-35.42%)</b></td><td>0.01 <b>(+21.72%)</b></td><td>831.10 <b>(+54.85%)</b></td><td>440.84 (+16.61%)</td><td>289.90 (+0.87%)</td><td>263.70 (-0.68%)</td><td>247.67 <b>(+74.80%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.70 (n/a)</td><td>378.06 (n/a)</td><td>287.40 (n/a)</td><td>265.50 (n/a)</td><td>141.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (+16.12%)</td><td>0.02 (-2.03%)</td><td>0.03 (+0.71%)</td><td>0.01 <b>(-34.26%)</b></td><td>0.01 <b>(+89.70%)</b></td><td>800.50 <b>(+52.13%)</b></td><td>444.68 (+18.22%)</td><td>320.30 (-0.71%)</td><td>259.80 (-13.86%)</td><td>235.01 <b>(+144.69%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.20 (n/a)</td><td>376.14 (n/a)</td><td>322.60 (n/a)</td><td>301.60 (n/a)</td><td>96.04 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (+16.71%)</td><td>0.02 (-5.74%)</td><td>0.02 (-15.83%)</td><td>0.00 <b>(-70.57%)</b></td><td>0.01 <b>(+71.74%)</b></td><td>1836.10 <b>(+239.83%)</b></td><td>660.08 <b>(+68.04%)</b></td><td>406.70 (+18.81%)</td><td>207.00 (-14.32%)</td><td>672.67 <b>(+393.52%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.30 (n/a)</td><td>392.80 (n/a)</td><td>342.30 (n/a)</td><td>241.60 (n/a)</td><td>136.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (+15.73%)</td><td>0.02 (-11.72%)</td><td>0.01 <b>(-24.09%)</b></td><td>0.01 (-15.07%)</td><td>0.01 <b>(+46.17%)</b></td><td>700.60 (+17.75%)</td><td>545.32 (+17.38%)</td><td>576.10 <b>(+31.74%)</b></td><td>318.00 (-13.59%)</td><td>140.76 <b>(+40.16%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>595.00 (n/a)</td><td>464.56 (n/a)</td><td>437.30 (n/a)</td><td>368.00 (n/a)</td><td>100.42 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (-1.21%)</td><td>0.05 (-14.19%)</td><td>0.06 (+3.03%)</td><td>0.03 <b>(-48.06%)</b></td><td>0.02 <b>(+276.68%)</b></td><td>610.80 <b>(+92.50%)</b></td><td>379.12 <b>(+29.56%)</b></td><td>287.30 (-2.94%)</td><td>264.60 (+1.22%)</td><td>152.18 <b>(+615.74%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>317.30 (n/a)</td><td>292.62 (n/a)</td><td>296.00 (n/a)</td><td>261.40 (n/a)</td><td>21.26 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (-8.52%)</td><td>0.05 <b>(-20.60%)</b></td><td>0.03 <b>(-36.81%)</b></td><td>0.03 <b>(-23.63%)</b></td><td>0.02 <b>(+25.79%)</b></td><td>641.60 <b>(+30.94%)</b></td><td>419.74 <b>(+35.71%)</b></td><td>468.50 <b>(+58.28%)</b></td><td>235.10 (+9.30%)</td><td>172.15 <b>(+61.35%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>490.00 (n/a)</td><td>309.30 (n/a)</td><td>296.00 (n/a)</td><td>215.10 (n/a)</td><td>106.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (-1.68%)</td><td>0.05 (+11.75%)</td><td>0.06 <b>(+44.47%)</b></td><td>0.03 (+15.10%)</td><td>0.02 (-10.17%)</td><td>514.40 (-13.11%)</td><td>356.58 (-13.07%)</td><td>286.10 <b>(-30.78%)</b></td><td>246.00 (+1.69%)</td><td>123.84 (-18.20%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>592.00 (n/a)</td><td>410.20 (n/a)</td><td>413.30 (n/a)</td><td>241.90 (n/a)</td><td>151.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (+13.45%)</td><td>0.05 (+17.82%)</td><td>0.04 (+10.19%)</td><td>0.03 (+3.59%)</td><td>0.02 <b>(+34.99%)</b></td><td>521.40 (-3.46%)</td><td>368.36 (-10.94%)</td><td>438.80 (-9.25%)</td><td>202.90 (-11.86%)</td><td>145.68 (+9.68%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>540.10 (n/a)</td><td>413.62 (n/a)</td><td>483.50 (n/a)</td><td>230.20 (n/a)</td><td>132.83 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (-3.52%)</td><td>0.05 <b>(+20.07%)</b></td><td>0.05 <b>(+60.62%)</b></td><td>0.04 <b>(+28.66%)</b></td><td>0.01 <b>(-38.82%)</b></td><td>461.80 <b>(-22.27%)</b></td><td>320.34 <b>(-23.42%)</b></td><td>298.10 <b>(-37.74%)</b></td><td>245.80 (+3.63%)</td><td>82.33 <b>(-46.44%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>594.10 (n/a)</td><td>418.30 (n/a)</td><td>478.80 (n/a)</td><td>237.20 (n/a)</td><td>153.72 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (-18.94%)</td><td>0.03 <b>(-25.12%)</b></td><td>0.03 (-15.66%)</td><td>0.03 (-15.19%)</td><td>0.01 <b>(-39.18%)</b></td><td>627.60 (+17.90%)</td><td>523.76 <b>(+27.07%)</b></td><td>561.10 (+18.58%)</td><td>322.10 <b>(+23.36%)</b></td><td>117.97 (-14.53%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>532.30 (n/a)</td><td>412.18 (n/a)</td><td>473.20 (n/a)</td><td>261.10 (n/a)</td><td>138.02 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.15 (+6.06%)</td><td>0.10 (-9.83%)</td><td>0.08 <b>(-27.84%)</b></td><td>0.06 (-11.78%)</td><td>0.04 <b>(+55.02%)</b></td><td>548.10 (+13.36%)</td><td>379.70 (+19.35%)</td><td>397.40 <b>(+38.56%)</b></td><td>224.50 (-5.71%)</td><td>145.31 <b>(+51.17%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>483.50 (n/a)</td><td>318.14 (n/a)</td><td>286.80 (n/a)</td><td>238.10 (n/a)</td><td>96.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (+5.07%)</td><td>0.11 (-0.97%)</td><td>0.11 (-0.18%)</td><td>0.06 (-11.77%)</td><td>0.04 <b>(+40.90%)</b></td><td>557.20 (+13.34%)</td><td>351.92 (+7.54%)</td><td>285.70 (+0.18%)</td><td>226.80 (-4.79%)</td><td>145.91 <b>(+45.46%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>491.60 (n/a)</td><td>327.26 (n/a)</td><td>285.20 (n/a)</td><td>238.20 (n/a)</td><td>100.31 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 <b>(+50.95%)</b></td><td>0.09 <b>(+37.54%)</b></td><td>0.10 <b>(+35.36%)</b></td><td>0.05 <b>(+222.53%)</b></td><td>0.03 (+16.69%)</td><td>656.60 <b>(-68.99%)</b></td><td>421.46 <b>(-45.40%)</b></td><td>338.80 <b>(-26.11%)</b></td><td>242.30 <b>(-33.74%)</b></td><td>176.45 <b>(-76.65%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>2117.60 (n/a)</td><td>771.92 (n/a)</td><td>458.50 (n/a)</td><td>365.70 (n/a)</td><td>755.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 <b>(+23.47%)</b></td><td>0.10 <b>(+30.01%)</b></td><td>0.12 <b>(+88.75%)</b></td><td>0.03 <b>(-47.94%)</b></td><td>0.04 <b>(+67.59%)</b></td><td>1115.20 <b>(+92.08%)</b></td><td>438.82 (-1.18%)</td><td>270.80 <b>(-47.03%)</b></td><td>248.00 (-19.01%)</td><td>378.55 <b>(+194.07%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>580.60 (n/a)</td><td>444.08 (n/a)</td><td>511.20 (n/a)</td><td>306.20 (n/a)</td><td>128.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.12 <b>(+30.46%)</b></td><td>0.08 (+7.25%)</td><td>0.07 (+16.28%)</td><td>0.02 <b>(-67.30%)</b></td><td>0.04 <b>(+116.51%)</b></td><td>1895.20 <b>(+205.83%)</b></td><td>691.18 <b>(+41.07%)</b></td><td>467.80 (-13.99%)</td><td>274.80 <b>(-23.35%)</b></td><td>680.92 <b>(+462.54%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>619.70 (n/a)</td><td>489.96 (n/a)</td><td>543.90 (n/a)</td><td>358.50 (n/a)</td><td>121.05 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (+7.74%)</td><td>0.01 (+8.86%)</td><td>0.01 <b>(+36.22%)</b></td><td>0.01 (-6.18%)</td><td>0.00 <b>(+38.63%)</b></td><td>522.50 (+6.59%)</td><td>359.20 (-3.77%)</td><td>293.90 <b>(-26.58%)</b></td><td>240.80 (-7.17%)</td><td>127.47 <b>(+42.95%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>490.20 (n/a)</td><td>373.28 (n/a)</td><td>400.30 (n/a)</td><td>259.40 (n/a)</td><td>89.17 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(+41.10%)</b></td><td>0.01 <b>(+24.48%)</b></td><td>0.01 (+9.92%)</td><td>0.01 (+11.19%)</td><td>0.00 <b>(+107.05%)</b></td><td>509.20 (-10.07%)</td><td>359.58 (-13.65%)</td><td>355.80 (-9.03%)</td><td>218.70 <b>(-29.13%)</b></td><td>132.57 <b>(+30.35%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.20 (n/a)</td><td>416.40 (n/a)</td><td>391.10 (n/a)</td><td>308.60 (n/a)</td><td>101.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(+59.77%)</b></td><td>0.01 <b>(+71.15%)</b></td><td>0.02 <b>(+83.51%)</b></td><td>0.01 <b>(+220.02%)</b></td><td>0.00 <b>(+47.85%)</b></td><td>663.80 <b>(-68.75%)</b></td><td>375.70 <b>(-53.12%)</b></td><td>268.40 <b>(-45.51%)</b></td><td>242.00 <b>(-37.40%)</b></td><td>182.40 <b>(-75.39%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2124.20 (n/a)</td><td>801.44 (n/a)</td><td>492.60 (n/a)</td><td>386.60 (n/a)</td><td>741.08 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (+8.18%)</td><td>0.01 (-7.38%)</td><td>0.01 <b>(-23.08%)</b></td><td>0.00 <b>(-49.57%)</b></td><td>0.01 <b>(+63.23%)</b></td><td>1045.40 <b>(+98.29%)</b></td><td>493.60 <b>(+35.20%)</b></td><td>424.00 <b>(+30.02%)</b></td><td>226.30 (-7.56%)</td><td>333.96 <b>(+180.57%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.20 (n/a)</td><td>365.08 (n/a)</td><td>326.10 (n/a)</td><td>244.80 (n/a)</td><td>119.03 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (+8.22%)</td><td>0.01 <b>(+28.98%)</b></td><td>0.01 <b>(+60.40%)</b></td><td>0.01 (-5.45%)</td><td>0.00 <b>(+38.90%)</b></td><td>651.80 (+5.78%)</td><td>390.18 (-16.31%)</td><td>299.50 <b>(-37.66%)</b></td><td>240.20 (-7.62%)</td><td>183.73 <b>(+41.70%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.20 (n/a)</td><td>466.24 (n/a)</td><td>480.40 (n/a)</td><td>260.00 (n/a)</td><td>129.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(+22.20%)</b></td><td>0.01 <b>(+36.53%)</b></td><td>0.01 <b>(+30.03%)</b></td><td>0.01 <b>(+247.98%)</b></td><td>0.00 <b>(-29.52%)</b></td><td>535.00 <b>(-71.26%)</b></td><td>359.24 <b>(-49.88%)</b></td><td>366.30 <b>(-23.08%)</b></td><td>239.60 (-18.17%)</td><td>112.57 <b>(-82.88%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1861.70 (n/a)</td><td>716.72 (n/a)</td><td>476.20 (n/a)</td><td>292.80 (n/a)</td><td>657.71 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-14.19%)</td><td>0.01 <b>(+33.42%)</b></td><td>0.01 <b>(+78.95%)</b></td><td>0.01 (-8.58%)</td><td>0.00 <b>(-23.26%)</b></td><td>621.40 (+9.38%)</td><td>341.12 <b>(-26.96%)</b></td><td>290.10 <b>(-44.10%)</b></td><td>243.30 (+16.58%)</td><td>158.56 (+5.89%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.10 (n/a)</td><td>467.06 (n/a)</td><td>519.00 (n/a)</td><td>208.70 (n/a)</td><td>149.74 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (+0.36%)</td><td>0.01 (+3.16%)</td><td>0.01 (-15.17%)</td><td>0.00 <b>(-40.40%)</b></td><td>0.01 <b>(+39.96%)</b></td><td>1070.20 <b>(+67.77%)</b></td><td>537.70 (+18.19%)</td><td>533.20 (+17.89%)</td><td>232.20 (-0.34%)</td><td>341.08 <b>(+118.13%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>637.90 (n/a)</td><td>454.94 (n/a)</td><td>452.30 (n/a)</td><td>233.00 (n/a)</td><td>156.37 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(+20.18%)</b></td><td>0.01 (+10.81%)</td><td>0.01 (-3.37%)</td><td>0.01 (-0.73%)</td><td>0.00 <b>(+26.97%)</b></td><td>540.50 (+0.73%)</td><td>355.78 (-8.10%)</td><td>341.50 (+3.48%)</td><td>214.60 (-16.76%)</td><td>120.34 (+2.98%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.60 (n/a)</td><td>387.12 (n/a)</td><td>330.00 (n/a)</td><td>257.80 (n/a)</td><td>116.86 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-3.26%)</td><td>0.01 (+7.79%)</td><td>0.01 (+14.08%)</td><td>0.01 <b>(+28.67%)</b></td><td>0.00 (-11.41%)</td><td>499.50 <b>(-22.28%)</b></td><td>377.18 (-10.47%)</td><td>371.10 (-12.33%)</td><td>254.60 (+3.37%)</td><td>113.14 <b>(-26.85%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>642.70 (n/a)</td><td>421.30 (n/a)</td><td>423.30 (n/a)</td><td>246.30 (n/a)</td><td>154.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(+22.51%)</b></td><td>0.01 (+16.09%)</td><td>0.01 <b>(+55.08%)</b></td><td>0.01 (-1.77%)</td><td>0.01 <b>(+49.19%)</b></td><td>627.80 (+1.80%)</td><td>403.90 (-6.76%)</td><td>304.60 <b>(-35.52%)</b></td><td>224.40 (-18.37%)</td><td>184.37 <b>(+35.97%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.70 (n/a)</td><td>433.16 (n/a)</td><td>472.40 (n/a)</td><td>274.90 (n/a)</td><td>135.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 (-17.91%)</td><td>0.01 (-6.48%)</td><td>0.01 (-3.10%)</td><td>0.01 (+7.94%)</td><td>0.00 <b>(-30.80%)</b></td><td>601.80 (-7.36%)</td><td>457.04 (+1.87%)</td><td>506.10 (+3.20%)</td><td>308.10 <b>(+21.83%)</b></td><td>122.64 <b>(-21.79%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>649.60 (n/a)</td><td>448.66 (n/a)</td><td>490.40 (n/a)</td><td>252.90 (n/a)</td><td>156.81 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (+8.53%)</td><td>0.02 (-0.37%)</td><td>0.03 (+17.60%)</td><td>0.00 <b>(-72.36%)</b></td><td>0.01 <b>(+90.80%)</b></td><td>1889.90 <b>(+261.77%)</b></td><td>631.70 <b>(+75.61%)</b></td><td>266.80 (-14.98%)</td><td>216.20 (-7.88%)</td><td>716.55 <b>(+521.78%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.40 (n/a)</td><td>359.72 (n/a)</td><td>313.80 (n/a)</td><td>234.70 (n/a)</td><td>115.24 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (+6.66%)</td><td>0.03 <b>(+26.46%)</b></td><td>0.03 <b>(+52.48%)</b></td><td>0.02 (+3.45%)</td><td>0.01 (-5.30%)</td><td>497.30 (-3.32%)</td><td>312.06 <b>(-22.07%)</b></td><td>288.20 <b>(-34.43%)</b></td><td>224.70 (-6.26%)</td><td>107.52 (-11.57%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.40 (n/a)</td><td>400.42 (n/a)</td><td>439.50 (n/a)</td><td>239.70 (n/a)</td><td>121.59 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 <b>(+34.50%)</b></td><td>0.02 (+18.11%)</td><td>0.02 (+15.24%)</td><td>0.01 (+1.95%)</td><td>0.01 <b>(+53.29%)</b></td><td>609.00 (-1.92%)</td><td>418.24 (-9.30%)</td><td>463.30 (-13.22%)</td><td>220.30 <b>(-25.65%)</b></td><td>174.86 (+15.48%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.90 (n/a)</td><td>461.12 (n/a)</td><td>533.90 (n/a)</td><td>296.30 (n/a)</td><td>151.42 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (+17.45%)</td><td>0.03 <b>(+46.97%)</b></td><td>0.03 <b>(+67.07%)</b></td><td>0.02 <b>(+271.22%)</b></td><td>0.01 <b>(-30.17%)</b></td><td>502.00 <b>(-73.06%)</b></td><td>318.86 <b>(-53.53%)</b></td><td>279.60 <b>(-40.15%)</b></td><td>240.30 (-14.85%)</td><td>105.10 <b>(-84.20%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1863.50 (n/a)</td><td>686.18 (n/a)</td><td>467.20 (n/a)</td><td>282.20 (n/a)</td><td>665.11 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (+5.02%)</td><td>0.02 <b>(-20.75%)</b></td><td>0.02 <b>(-39.74%)</b></td><td>0.01 (-6.83%)</td><td>0.01 (-3.92%)</td><td>587.60 (+7.32%)</td><td>451.70 <b>(+23.42%)</b></td><td>448.80 <b>(+65.98%)</b></td><td>215.30 (-4.78%)</td><td>150.26 (-9.25%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.50 (n/a)</td><td>365.98 (n/a)</td><td>270.40 (n/a)</td><td>226.10 (n/a)</td><td>165.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (+6.15%)</td><td>0.03 (+16.71%)</td><td>0.03 <b>(+48.95%)</b></td><td>0.01 (-2.38%)</td><td>0.01 <b>(+21.16%)</b></td><td>560.10 (+2.45%)</td><td>370.46 (-11.15%)</td><td>310.40 <b>(-32.87%)</b></td><td>231.60 (-5.78%)</td><td>155.31 (+14.57%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.70 (n/a)</td><td>416.94 (n/a)</td><td>462.40 (n/a)</td><td>245.80 (n/a)</td><td>135.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(-30.80%)</b></td><td>0.02 (-18.86%)</td><td>0.02 <b>(-41.13%)</b></td><td>0.01 <b>(+116.99%)</b></td><td>0.00 <b>(-62.19%)</b></td><td>604.80 <b>(-53.92%)</b></td><td>488.26 (-11.20%)</td><td>523.90 <b>(+69.88%)</b></td><td>356.60 <b>(+44.49%)</b></td><td>109.94 <b>(-75.43%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1312.50 (n/a)</td><td>549.84 (n/a)</td><td>308.40 (n/a)</td><td>246.80 (n/a)</td><td>447.38 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (+8.59%)</td><td>0.02 (-7.97%)</td><td>0.03 (+0.80%)</td><td>0.01 <b>(-23.95%)</b></td><td>0.01 <b>(+86.12%)</b></td><td>599.80 <b>(+31.51%)</b></td><td>396.10 <b>(+20.00%)</b></td><td>300.70 (-0.79%)</td><td>244.50 (-7.91%)</td><td>165.73 <b>(+125.53%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>456.10 (n/a)</td><td>330.08 (n/a)</td><td>303.10 (n/a)</td><td>265.50 (n/a)</td><td>73.48 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (-3.70%)</td><td>0.02 (+3.77%)</td><td>0.03 <b>(+64.70%)</b></td><td>0.01 (-2.62%)</td><td>0.01 (-4.35%)</td><td>618.80 (+2.69%)</td><td>420.36 (-2.59%)</td><td>299.50 <b>(-39.27%)</b></td><td>275.20 (+3.85%)</td><td>176.94 (+13.78%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.60 (n/a)</td><td>431.52 (n/a)</td><td>493.20 (n/a)</td><td>265.00 (n/a)</td><td>155.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (-10.49%)</td><td>0.02 (-14.50%)</td><td>0.02 <b>(-42.41%)</b></td><td>0.02 (-4.28%)</td><td>0.01 (-8.40%)</td><td>541.30 (+4.48%)</td><td>425.34 (+16.16%)</td><td>498.10 <b>(+73.61%)</b></td><td>273.40 (+11.73%)</td><td>132.37 (+0.67%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.10 (n/a)</td><td>366.18 (n/a)</td><td>286.90 (n/a)</td><td>244.70 (n/a)</td><td>131.50 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 <b>(+39.08%)</b></td><td>0.02 <b>(+56.30%)</b></td><td>0.03 <b>(+72.19%)</b></td><td>0.01 <b>(+111.80%)</b></td><td>0.01 <b>(+32.08%)</b></td><td>992.60 <b>(-52.79%)</b></td><td>456.46 <b>(-44.28%)</b></td><td>319.50 <b>(-41.93%)</b></td><td>287.50 <b>(-28.09%)</b></td><td>302.87 <b>(-58.04%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2102.40 (n/a)</td><td>819.14 (n/a)</td><td>550.20 (n/a)</td><td>399.80 (n/a)</td><td>721.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 <b>(-21.12%)</b></td><td>0.02 <b>(-28.24%)</b></td><td>0.02 <b>(-33.28%)</b></td><td>0.00 <b>(-64.73%)</b></td><td>0.01 (-12.20%)</td><td>1883.70 <b>(+183.52%)</b></td><td>732.56 <b>(+76.35%)</b></td><td>537.50 <b>(+49.89%)</b></td><td>315.10 <b>(+26.80%)</b></td><td>651.96 <b>(+253.72%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>664.40 (n/a)</td><td>415.40 (n/a)</td><td>358.60 (n/a)</td><td>248.50 (n/a)</td><td>184.32 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 <b>(-34.54%)</b></td><td>0.04 <b>(-24.53%)</b></td><td>0.04 <b>(-34.35%)</b></td><td>0.03 <b>(+37.43%)</b></td><td>0.00 <b>(-71.06%)</b></td><td>473.00 <b>(-27.24%)</b></td><td>437.46 (+18.63%)</td><td>465.30 <b>(+52.31%)</b></td><td>354.60 <b>(+52.78%)</b></td><td>50.02 <b>(-69.69%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>650.10 (n/a)</td><td>368.76 (n/a)</td><td>305.50 (n/a)</td><td>232.10 (n/a)</td><td>165.04 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 <b>(+36.77%)</b></td><td>0.05 (+9.72%)</td><td>0.06 (+8.59%)</td><td>0.03 (-12.24%)</td><td>0.02 <b>(+75.94%)</b></td><td>567.10 (+13.94%)</td><td>353.30 (-2.26%)</td><td>289.90 (-7.91%)</td><td>210.00 <b>(-26.88%)</b></td><td>140.38 <b>(+52.83%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>497.70 (n/a)</td><td>361.48 (n/a)</td><td>314.80 (n/a)</td><td>287.20 (n/a)</td><td>91.86 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (+1.48%)</td><td>0.05 (+2.23%)</td><td>0.05 (+6.32%)</td><td>0.03 (+0.55%)</td><td>0.02 <b>(+22.03%)</b></td><td>615.30 (-0.55%)</td><td>402.74 (+3.30%)</td><td>299.10 (-5.94%)</td><td>238.00 (-1.45%)</td><td>185.47 <b>(+23.90%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>618.70 (n/a)</td><td>389.88 (n/a)</td><td>318.00 (n/a)</td><td>241.50 (n/a)</td><td>149.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (-6.12%)</td><td>0.05 (+6.35%)</td><td>0.03 (+1.53%)</td><td>0.03 <b>(+44.27%)</b></td><td>0.02 (-15.43%)</td><td>511.50 <b>(-30.68%)</b></td><td>398.36 (-11.90%)</td><td>478.70 (-1.52%)</td><td>238.20 (+6.53%)</td><td>128.12 <b>(-34.84%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>737.90 (n/a)</td><td>452.16 (n/a)</td><td>486.10 (n/a)</td><td>223.60 (n/a)</td><td>196.62 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 <b>(+27.59%)</b></td><td>0.07 <b>(+64.80%)</b></td><td>0.07 <b>(+97.01%)</b></td><td>0.06 <b>(+105.43%)</b></td><td>0.01 <b>(-34.22%)</b></td><td>295.80 <b>(-51.32%)</b></td><td>251.92 <b>(-44.47%)</b></td><td>239.50 <b>(-49.25%)</b></td><td>203.40 <b>(-21.65%)</b></td><td>38.06 <b>(-75.21%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>607.60 (n/a)</td><td>453.70 (n/a)</td><td>471.90 (n/a)</td><td>259.60 (n/a)</td><td>153.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 <b>(+20.32%)</b></td><td>0.05 <b>(+35.46%)</b></td><td>0.05 <b>(+73.73%)</b></td><td>0.03 (+4.46%)</td><td>0.01 (+11.56%)</td><td>553.00 (-4.28%)</td><td>336.94 <b>(-25.95%)</b></td><td>301.00 <b>(-42.44%)</b></td><td>244.30 (-16.90%)</td><td>123.36 (-5.32%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>577.70 (n/a)</td><td>455.04 (n/a)</td><td>522.90 (n/a)</td><td>294.00 (n/a)</td><td>130.29 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 <b>(-20.01%)</b></td><td>0.04 (-2.55%)</td><td>0.03 (-2.68%)</td><td>0.03 (-14.99%)</td><td>0.02 (-13.40%)</td><td>604.40 (+17.63%)</td><td>437.56 (+3.49%)</td><td>500.30 (+2.75%)</td><td>262.80 <b>(+25.02%)</b></td><td>157.79 <b>(+23.54%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>513.80 (n/a)</td><td>422.80 (n/a)</td><td>486.90 (n/a)</td><td>210.20 (n/a)</td><td>127.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (-0.22%)</td><td>0.04 (+0.12%)</td><td>0.05 (+4.12%)</td><td>0.03 (+10.32%)</td><td>0.01 (-5.22%)</td><td>605.60 (-9.34%)</td><td>410.32 (-1.63%)</td><td>332.80 (-3.95%)</td><td>293.00 (+0.21%)</td><td>136.51 (-13.13%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>668.00 (n/a)</td><td>417.12 (n/a)</td><td>346.50 (n/a)</td><td>292.40 (n/a)</td><td>157.15 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (-2.34%)</td><td>0.05 <b>(+32.32%)</b></td><td>0.05 <b>(+83.78%)</b></td><td>0.03 (+15.29%)</td><td>0.02 (-8.50%)</td><td>540.60 (-13.25%)</td><td>382.30 <b>(-25.92%)</b></td><td>306.60 <b>(-45.58%)</b></td><td>247.80 (+2.40%)</td><td>142.04 (-8.56%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>623.20 (n/a)</td><td>516.04 (n/a)</td><td>563.40 (n/a)</td><td>242.00 (n/a)</td><td>155.34 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 <b>(+49.59%)</b></td><td>0.05 <b>(+43.48%)</b></td><td>0.05 <b>(+56.16%)</b></td><td>0.03 (-0.81%)</td><td>0.01 <b>(+142.02%)</b></td><td>558.20 (+0.81%)</td><td>343.36 <b>(-26.02%)</b></td><td>300.50 <b>(-35.97%)</b></td><td>241.40 <b>(-33.17%)</b></td><td>123.46 <b>(+80.06%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>553.70 (n/a)</td><td>464.12 (n/a)</td><td>469.30 (n/a)</td><td>361.20 (n/a)</td><td>68.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 <b>(+21.70%)</b></td><td>0.04 <b>(+31.28%)</b></td><td>0.03 (+11.50%)</td><td>0.03 <b>(+206.21%)</b></td><td>0.01 (-13.26%)</td><td>627.40 <b>(-67.35%)</b></td><td>492.00 <b>(-40.76%)</b></td><td>493.80 (-10.32%)</td><td>289.40 (-17.81%)</td><td>132.68 <b>(-78.99%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1921.30 (n/a)</td><td>830.56 (n/a)</td><td>550.60 (n/a)</td><td>352.10 (n/a)</td><td>631.50 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (-10.47%)</td><td>0.04 (-19.60%)</td><td>0.03 <b>(-28.12%)</b></td><td>0.01 <b>(-79.05%)</b></td><td>0.02 <b>(+59.07%)</b></td><td>2458.50 <b>(+377.19%)</b></td><td>814.08 <b>(+111.81%)</b></td><td>482.40 <b>(+39.10%)</b></td><td>287.70 (+11.73%)</td><td>926.33 <b>(+744.92%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>515.20 (n/a)</td><td>384.34 (n/a)</td><td>346.80 (n/a)</td><td>257.50 (n/a)</td><td>109.64 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 <b>(+20.66%)</b></td><td>0.09 (-9.20%)</td><td>0.07 <b>(-30.18%)</b></td><td>0.06 (-8.13%)</td><td>0.03 <b>(+61.76%)</b></td><td>539.90 (+8.85%)</td><td>396.78 (+15.07%)</td><td>442.60 <b>(+43.19%)</b></td><td>249.00 (-17.14%)</td><td>118.90 <b>(+40.44%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>496.00 (n/a)</td><td>344.82 (n/a)</td><td>309.10 (n/a)</td><td>300.50 (n/a)</td><td>84.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 <b>(+21.59%)</b></td><td>0.11 <b>(+26.97%)</b></td><td>0.12 <b>(+26.96%)</b></td><td>0.07 <b>(+33.61%)</b></td><td>0.03 (+10.65%)</td><td>481.60 <b>(-25.15%)</b></td><td>310.12 <b>(-22.67%)</b></td><td>271.90 <b>(-21.23%)</b></td><td>241.00 (-17.78%)</td><td>99.28 <b>(-31.03%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>643.40 (n/a)</td><td>401.04 (n/a)</td><td>345.20 (n/a)</td><td>293.10 (n/a)</td><td>143.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 <b>(+23.09%)</b></td><td>0.10 <b>(+27.07%)</b></td><td>0.07 (-1.97%)</td><td>0.05 <b>(+208.44%)</b></td><td>0.05 (+11.38%)</td><td>633.00 <b>(-67.58%)</b></td><td>407.18 <b>(-42.05%)</b></td><td>449.00 (+2.02%)</td><td>196.10 (-18.77%)</td><td>173.41 <b>(-75.37%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1952.30 (n/a)</td><td>702.68 (n/a)</td><td>440.10 (n/a)</td><td>241.40 (n/a)</td><td>704.17 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.15 (+0.29%)</td><td>0.09 (+6.37%)</td><td>0.07 (-6.86%)</td><td>0.07 <b>(+29.99%)</b></td><td>0.03 (-1.34%)</td><td>489.60 <b>(-23.07%)</b></td><td>378.80 (-7.76%)</td><td>440.60 (+7.36%)</td><td>223.30 (-0.31%)</td><td>116.14 <b>(-21.62%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>636.40 (n/a)</td><td>410.68 (n/a)</td><td>410.40 (n/a)</td><td>224.00 (n/a)</td><td>148.17 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 <b>(+21.79%)</b></td><td>0.11 (+15.30%)</td><td>0.12 (+7.48%)</td><td>0.05 (-4.74%)</td><td>0.05 <b>(+46.75%)</b></td><td>601.00 (+5.00%)</td><td>345.38 (-6.30%)</td><td>274.60 (-6.95%)</td><td>190.90 (-17.89%)</td><td>173.72 <b>(+23.08%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>572.40 (n/a)</td><td>368.60 (n/a)</td><td>295.10 (n/a)</td><td>232.50 (n/a)</td><td>141.15 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 (+17.27%)</td><td>0.09 <b>(+23.76%)</b></td><td>0.07 (-13.52%)</td><td>0.06 <b>(+233.10%)</b></td><td>0.05 (+6.56%)</td><td>590.90 <b>(-69.98%)</b></td><td>411.74 <b>(-41.67%)</b></td><td>502.00 (+15.64%)</td><td>206.50 (-14.74%)</td><td>171.11 <b>(-76.04%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1968.20 (n/a)</td><td>705.84 (n/a)</td><td>434.10 (n/a)</td><td>242.20 (n/a)</td><td>714.16 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (-19.14%)</td><td>0.10 (-7.20%)</td><td>0.07 <b>(-33.21%)</b></td><td>0.05 (-18.33%)</td><td>0.05 (-7.37%)</td><td>624.90 <b>(+22.46%)</b></td><td>400.58 (+11.76%)</td><td>478.40 <b>(+49.69%)</b></td><td>194.90 <b>(+23.67%)</b></td><td>188.16 <b>(+26.18%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>510.30 (n/a)</td><td>358.44 (n/a)</td><td>319.60 (n/a)</td><td>157.60 (n/a)</td><td>149.12 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (-17.79%)</td><td>0.07 (-1.53%)</td><td>0.07 (-5.71%)</td><td>0.05 (+18.23%)</td><td>0.01 <b>(-46.95%)</b></td><td>602.50 (-15.41%)</td><td>486.42 (-6.44%)</td><td>485.10 (+6.06%)</td><td>348.50 <b>(+21.64%)</b></td><td>92.05 <b>(-50.14%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>712.30 (n/a)</td><td>519.90 (n/a)</td><td>457.40 (n/a)</td><td>286.50 (n/a)</td><td>184.61 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (-9.00%)</td><td>0.09 <b>(+35.63%)</b></td><td>0.09 <b>(+45.83%)</b></td><td>0.06 <b>(+224.40%)</b></td><td>0.03 <b>(-33.67%)</b></td><td>593.90 <b>(-69.17%)</b></td><td>399.68 <b>(-47.26%)</b></td><td>353.80 <b>(-31.42%)</b></td><td>291.90 (+9.90%)</td><td>129.38 <b>(-80.52%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1926.60 (n/a)</td><td>757.90 (n/a)</td><td>515.90 (n/a)</td><td>265.60 (n/a)</td><td>664.31 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (+7.45%)</td><td>0.08 (+15.05%)</td><td>0.11 <b>(+96.37%)</b></td><td>0.01 <b>(-71.26%)</b></td><td>0.05 <b>(+78.39%)</b></td><td>2387.40 <b>(+247.97%)</b></td><td>853.30 <b>(+63.86%)</b></td><td>298.50 <b>(-49.09%)</b></td><td>248.80 (-6.96%)</td><td>922.23 <b>(+459.53%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>686.10 (n/a)</td><td>520.74 (n/a)</td><td>586.30 (n/a)</td><td>267.40 (n/a)</td><td>164.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (-19.54%)</td><td>0.06 (-10.00%)</td><td>0.06 (-11.49%)</td><td>0.05 <b>(+66.19%)</b></td><td>0.01 <b>(-59.62%)</b></td><td>637.10 <b>(-39.83%)</b></td><td>526.08 (-6.41%)</td><td>530.80 (+12.98%)</td><td>393.20 <b>(+24.27%)</b></td><td>97.06 <b>(-68.44%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1058.80 (n/a)</td><td>562.10 (n/a)</td><td>469.80 (n/a)</td><td>316.40 (n/a)</td><td>307.52 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 <b>(+25.05%)</b></td><td>0.09 (+10.69%)</td><td>0.09 (+19.65%)</td><td>0.06 (-9.68%)</td><td>0.03 <b>(+76.95%)</b></td><td>582.70 (+10.72%)</td><td>414.88 (-4.75%)</td><td>382.80 (-16.42%)</td><td>253.30 <b>(-20.04%)</b></td><td>129.78 <b>(+61.09%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>526.30 (n/a)</td><td>435.58 (n/a)</td><td>458.00 (n/a)</td><td>316.80 (n/a)</td><td>80.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-7.59%)</td><td>0.01 (-17.52%)</td><td>0.01 (-18.94%)</td><td>0.01 (+0.31%)</td><td>0.00 (-0.34%)</td><td>544.20 (-0.31%)</td><td>372.36 <b>(+22.54%)</b></td><td>301.50 <b>(+23.36%)</b></td><td>212.90 (+8.18%)</td><td>151.65 (+8.61%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.90 (n/a)</td><td>303.86 (n/a)</td><td>244.40 (n/a)</td><td>196.80 (n/a)</td><td>139.63 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-8.94%)</td><td>0.02 (+10.62%)</td><td>0.02 <b>(+61.80%)</b></td><td>0.01 (+5.76%)</td><td>0.00 (-7.19%)</td><td>458.50 (-5.46%)</td><td>346.98 (-10.21%)</td><td>275.40 <b>(-38.18%)</b></td><td>271.70 (+9.82%)</td><td>100.00 (-4.07%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>485.00 (n/a)</td><td>386.44 (n/a)</td><td>445.50 (n/a)</td><td>247.40 (n/a)</td><td>104.24 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.01 <b>(-21.66%)</b></td><td>0.01 <b>(-36.03%)</b></td><td>0.01 <b>(-46.41%)</b></td><td>0.01 <b>(-41.37%)</b></td><td>0.00 (-9.05%)</td><td>776.00 <b>(+70.55%)</b></td><td>552.16 <b>(+62.83%)</b></td><td>571.40 <b>(+86.55%)</b></td><td>277.70 <b>(+27.68%)</b></td><td>182.04 <b>(+75.48%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>455.00 (n/a)</td><td>339.10 (n/a)</td><td>306.30 (n/a)</td><td>217.50 (n/a)</td><td>103.74 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (+6.98%)</td><td>0.01 <b>(+21.92%)</b></td><td>0.01 (+6.37%)</td><td>0.01 (+18.16%)</td><td>0.01 <b>(+22.23%)</b></td><td>519.80 (-15.37%)</td><td>401.26 (-16.04%)</td><td>470.10 (-6.00%)</td><td>243.40 (-6.53%)</td><td>137.93 (+2.36%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.20 (n/a)</td><td>477.90 (n/a)</td><td>500.10 (n/a)</td><td>260.40 (n/a)</td><td>134.75 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-10.33%)</td><td>0.01 <b>(+28.22%)</b></td><td>0.01 <b>(+31.75%)</b></td><td>0.01 <b>(+271.10%)</b></td><td>0.00 <b>(-41.72%)</b></td><td>516.50 <b>(-73.05%)</b></td><td>350.04 <b>(-49.53%)</b></td><td>291.00 <b>(-24.10%)</b></td><td>268.80 (+11.54%)</td><td>107.08 <b>(-84.59%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1916.80 (n/a)</td><td>693.56 (n/a)</td><td>383.40 (n/a)</td><td>241.00 (n/a)</td><td>694.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-0.27%)</td><td>0.02 <b>(+44.66%)</b></td><td>0.02 <b>(+118.10%)</b></td><td>0.01 <b>(+46.82%)</b></td><td>0.00 (-18.61%)</td><td>433.80 <b>(-31.88%)</b></td><td>325.72 <b>(-35.36%)</b></td><td>273.50 <b>(-54.15%)</b></td><td>241.10 (+0.29%)</td><td>96.51 <b>(-42.29%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.80 (n/a)</td><td>503.92 (n/a)</td><td>596.50 (n/a)</td><td>240.40 (n/a)</td><td>167.23 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(-42.59%)</b></td><td>0.01 <b>(-22.88%)</b></td><td>0.01 (-16.19%)</td><td>0.01 (-13.16%)</td><td>0.00 <b>(-53.21%)</b></td><td>580.60 (+15.15%)</td><td>454.70 (+16.26%)</td><td>527.00 (+19.31%)</td><td>244.70 <b>(+74.16%)</b></td><td>152.06 (+4.09%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>504.20 (n/a)</td><td>391.12 (n/a)</td><td>441.70 (n/a)</td><td>140.50 (n/a)</td><td>146.09 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (-0.75%)</td><td>0.01 (+0.74%)</td><td>0.01 (-19.84%)</td><td>0.01 <b>(+43.51%)</b></td><td>0.00 <b>(-22.41%)</b></td><td>468.60 <b>(-30.32%)</b></td><td>393.04 (-9.35%)</td><td>443.90 <b>(+24.76%)</b></td><td>234.10 (+0.77%)</td><td>98.21 <b>(-48.66%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>672.50 (n/a)</td><td>433.56 (n/a)</td><td>355.80 (n/a)</td><td>232.30 (n/a)</td><td>191.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(-41.53%)</b></td><td>0.01 <b>(-21.92%)</b></td><td>0.01 (-6.98%)</td><td>0.01 (+14.45%)</td><td>0.00 <b>(-59.17%)</b></td><td>537.10 (-12.62%)</td><td>433.62 (+5.99%)</td><td>481.10 (+7.51%)</td><td>247.80 <b>(+71.01%)</b></td><td>112.50 <b>(-40.00%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.70 (n/a)</td><td>409.10 (n/a)</td><td>447.50 (n/a)</td><td>144.90 (n/a)</td><td>187.49 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 (+17.02%)</td><td>0.01 <b>(+21.07%)</b></td><td>0.01 (+16.77%)</td><td>0.01 (-1.15%)</td><td>0.00 <b>(+58.37%)</b></td><td>610.40 (+1.16%)</td><td>450.22 (-12.18%)</td><td>458.40 (-14.35%)</td><td>276.20 (-14.54%)</td><td>159.84 <b>(+45.75%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.40 (n/a)</td><td>512.68 (n/a)</td><td>535.20 (n/a)</td><td>323.20 (n/a)</td><td>109.67 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(+40.42%)</b></td><td>0.01 <b>(+23.41%)</b></td><td>0.01 <b>(+24.10%)</b></td><td>0.00 <b>(-66.05%)</b></td><td>0.01 <b>(+173.27%)</b></td><td>1915.00 <b>(+194.52%)</b></td><td>663.22 <b>(+34.41%)</b></td><td>430.30 (-19.42%)</td><td>241.20 <b>(-28.77%)</b></td><td>708.45 <b>(+482.58%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>650.20 (n/a)</td><td>493.42 (n/a)</td><td>534.00 (n/a)</td><td>338.60 (n/a)</td><td>121.61 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (-4.32%)</td><td>0.03 (+16.97%)</td><td>0.03 <b>(+72.47%)</b></td><td>0.00 <b>(-66.91%)</b></td><td>0.01 <b>(+22.98%)</b></td><td>1844.50 <b>(+202.18%)</b></td><td>574.08 <b>(+36.04%)</b></td><td>260.20 <b>(-42.01%)</b></td><td>246.50 (+4.54%)</td><td>710.27 <b>(+313.22%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.40 (n/a)</td><td>421.98 (n/a)</td><td>448.70 (n/a)</td><td>235.80 (n/a)</td><td>171.88 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (+0.19%)</td><td>0.04 (+14.29%)</td><td>0.05 (+16.22%)</td><td>0.03 <b>(+35.90%)</b></td><td>0.01 (-17.49%)</td><td>433.20 <b>(-26.41%)</b></td><td>325.54 (-18.13%)</td><td>261.00 (-13.95%)</td><td>248.10 (-0.20%)</td><td>97.61 <b>(-41.57%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>588.70 (n/a)</td><td>397.64 (n/a)</td><td>303.30 (n/a)</td><td>248.60 (n/a)</td><td>167.05 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 <b>(+57.08%)</b></td><td>0.03 <b>(+33.42%)</b></td><td>0.03 <b>(+24.25%)</b></td><td>0.01 (+2.22%)</td><td>0.01 <b>(+47.82%)</b></td><td>581.10 (-2.17%)</td><td>302.20 <b>(-21.79%)</b></td><td>253.60 (-19.54%)</td><td>154.60 <b>(-36.35%)</b></td><td>162.44 (-0.85%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.00 (n/a)</td><td>386.38 (n/a)</td><td>315.20 (n/a)</td><td>242.90 (n/a)</td><td>163.84 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (-14.07%)</td><td>0.03 (+4.91%)</td><td>0.04 <b>(+70.98%)</b></td><td>0.02 (-11.93%)</td><td>0.01 (-19.75%)</td><td>581.20 (+13.54%)</td><td>356.68 (-7.00%)</td><td>267.40 <b>(-41.53%)</b></td><td>234.40 (+16.33%)</td><td>148.59 (+2.73%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.90 (n/a)</td><td>383.54 (n/a)</td><td>457.30 (n/a)</td><td>201.50 (n/a)</td><td>144.63 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 <b>(+20.28%)</b></td><td>0.03 <b>(+20.77%)</b></td><td>0.03 <b>(+25.18%)</b></td><td>0.01 <b>(+81.02%)</b></td><td>0.01 <b>(+23.10%)</b></td><td>570.20 <b>(-44.75%)</b></td><td>367.72 <b>(-22.42%)</b></td><td>293.00 <b>(-20.12%)</b></td><td>205.20 (-16.86%)</td><td>171.71 <b>(-45.98%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1032.10 (n/a)</td><td>473.96 (n/a)</td><td>366.80 (n/a)</td><td>246.80 (n/a)</td><td>317.89 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 (-4.25%)</td><td>0.03 <b>(+40.43%)</b></td><td>0.04 <b>(+100.17%)</b></td><td>0.02 <b>(+41.49%)</b></td><td>0.01 <b>(-25.59%)</b></td><td>434.00 <b>(-29.33%)</b></td><td>324.02 <b>(-34.13%)</b></td><td>270.80 <b>(-50.05%)</b></td><td>229.00 (+4.42%)</td><td>97.33 <b>(-39.93%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>614.10 (n/a)</td><td>491.90 (n/a)</td><td>542.10 (n/a)</td><td>219.30 (n/a)</td><td>162.04 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 <b>(-35.41%)</b></td><td>0.02 <b>(-27.54%)</b></td><td>0.02 <b>(-33.16%)</b></td><td>0.02 (-13.17%)</td><td>0.00 <b>(-53.99%)</b></td><td>513.80 (+15.18%)</td><td>400.16 <b>(+30.18%)</b></td><td>413.50 <b>(+49.60%)</b></td><td>293.70 <b>(+54.82%)</b></td><td>83.40 <b>(-20.50%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>446.10 (n/a)</td><td>307.40 (n/a)</td><td>276.40 (n/a)</td><td>189.70 (n/a)</td><td>104.90 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.05 (+7.05%)</td><td>0.03 <b>(+50.11%)</b></td><td>0.04 <b>(+114.46%)</b></td><td>0.02 <b>(+86.58%)</b></td><td>0.01 (-1.55%)</td><td>583.80 <b>(-46.41%)</b></td><td>343.96 <b>(-39.77%)</b></td><td>249.10 <b>(-53.37%)</b></td><td>200.10 (-6.58%)</td><td>164.77 <b>(-48.42%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1089.30 (n/a)</td><td>571.10 (n/a)</td><td>534.20 (n/a)</td><td>214.20 (n/a)</td><td>319.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.02 <b>(-30.96%)</b></td><td>0.02 (-12.82%)</td><td>0.02 (+4.51%)</td><td>0.01 (-9.16%)</td><td>0.00 <b>(-43.20%)</b></td><td>622.80 (+10.07%)</td><td>494.26 (+11.56%)</td><td>434.00 (-4.32%)</td><td>393.30 <b>(+44.81%)</b></td><td>107.46 (-3.79%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.80 (n/a)</td><td>443.04 (n/a)</td><td>453.60 (n/a)</td><td>271.60 (n/a)</td><td>111.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 <b>(+53.11%)</b></td><td>0.03 <b>(+47.66%)</b></td><td>0.03 <b>(+76.27%)</b></td><td>0.02 <b>(+22.68%)</b></td><td>0.01 <b>(+121.97%)</b></td><td>533.50 (-18.50%)</td><td>367.86 <b>(-26.96%)</b></td><td>274.80 <b>(-43.28%)</b></td><td>237.10 <b>(-34.68%)</b></td><td>147.24 <b>(+24.42%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>654.60 (n/a)</td><td>503.64 (n/a)</td><td>484.50 (n/a)</td><td>363.00 (n/a)</td><td>118.34 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.03 (-10.15%)</td><td>0.02 (-9.90%)</td><td>0.02 (-2.10%)</td><td>0.01 <b>(-21.35%)</b></td><td>0.01 (+1.39%)</td><td>669.30 <b>(+27.15%)</b></td><td>471.72 (+14.12%)</td><td>433.60 (+2.17%)</td><td>289.90 (+11.29%)</td><td>147.08 <b>(+53.40%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.40 (n/a)</td><td>413.34 (n/a)</td><td>424.40 (n/a)</td><td>260.50 (n/a)</td><td>95.88 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 <b>(+82.32%)</b></td><td>0.06 <b>(+60.07%)</b></td><td>0.07 <b>(+94.31%)</b></td><td>0.03 (+2.32%)</td><td>0.03 <b>(+182.34%)</b></td><td>599.00 (-2.28%)</td><td>358.60 <b>(-25.26%)</b></td><td>251.70 <b>(-48.54%)</b></td><td>167.00 <b>(-45.17%)</b></td><td>192.52 <b>(+73.45%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>613.00 (n/a)</td><td>479.82 (n/a)</td><td>489.10 (n/a)</td><td>304.60 (n/a)</td><td>110.99 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (-3.95%)</td><td>0.08 (+17.90%)</td><td>0.07 (+15.16%)</td><td>0.06 <b>(+22.40%)</b></td><td>0.02 (-14.42%)</td><td>438.10 (-18.31%)</td><td>344.86 (-17.87%)</td><td>374.60 (-13.17%)</td><td>253.50 (+4.11%)</td><td>83.98 <b>(-30.76%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>536.30 (n/a)</td><td>419.92 (n/a)</td><td>431.40 (n/a)</td><td>243.50 (n/a)</td><td>121.29 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (-8.96%)</td><td>0.05 (-12.96%)</td><td>0.04 <b>(-38.09%)</b></td><td>0.03 (+5.16%)</td><td>0.01 <b>(-35.22%)</b></td><td>471.50 (-4.92%)</td><td>366.00 (+7.90%)</td><td>400.70 <b>(+61.51%)</b></td><td>263.80 (+9.83%)</td><td>88.06 <b>(-33.41%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>495.90 (n/a)</td><td>339.20 (n/a)</td><td>248.10 (n/a)</td><td>240.20 (n/a)</td><td>132.23 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (-5.45%)</td><td>0.05 (-5.39%)</td><td>0.05 (+2.81%)</td><td>0.03 (-14.35%)</td><td>0.02 (+4.68%)</td><td>667.70 (+16.75%)</td><td>476.26 (+9.40%)</td><td>443.70 (-2.72%)</td><td>263.60 (+5.78%)</td><td>165.89 <b>(+42.45%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>571.90 (n/a)</td><td>435.32 (n/a)</td><td>456.10 (n/a)</td><td>249.20 (n/a)</td><td>116.46 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (-11.79%)</td><td>0.03 (-17.86%)</td><td>0.03 (-19.12%)</td><td>0.02 <b>(-48.75%)</b></td><td>0.02 (+6.59%)</td><td>1056.70 <b>(+95.14%)</b></td><td>578.00 <b>(+35.19%)</b></td><td>526.40 <b>(+23.63%)</b></td><td>273.20 (+13.36%)</td><td>290.88 <b>(+149.42%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>541.50 (n/a)</td><td>427.54 (n/a)</td><td>425.80 (n/a)</td><td>241.00 (n/a)</td><td>116.62 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (-19.87%)</td><td>0.06 (-4.50%)</td><td>0.07 (+9.90%)</td><td>0.04 (+12.78%)</td><td>0.02 <b>(-35.58%)</b></td><td>528.90 (-11.33%)</td><td>355.46 (-2.41%)</td><td>308.80 (-9.02%)</td><td>263.60 <b>(+24.81%)</b></td><td>111.18 <b>(-28.36%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>596.50 (n/a)</td><td>364.24 (n/a)</td><td>339.40 (n/a)</td><td>211.20 (n/a)</td><td>155.19 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 (-5.26%)</td><td>0.05 (-1.26%)</td><td>0.06 <b>(+20.32%)</b></td><td>0.03 <b>(-29.84%)</b></td><td>0.02 <b>(+30.83%)</b></td><td>652.10 <b>(+42.54%)</b></td><td>393.36 (+8.22%)</td><td>294.80 (-16.89%)</td><td>270.40 (+5.54%)</td><td>164.03 <b>(+87.17%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>457.50 (n/a)</td><td>363.48 (n/a)</td><td>354.70 (n/a)</td><td>256.20 (n/a)</td><td>87.64 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (-7.48%)</td><td>0.04 (-14.49%)</td><td>0.03 <b>(-34.78%)</b></td><td>0.02 <b>(+118.33%)</b></td><td>0.02 <b>(-22.01%)</b></td><td>1092.50 <b>(-54.20%)</b></td><td>566.20 <b>(-23.95%)</b></td><td>548.40 <b>(+53.36%)</b></td><td>278.40 (+8.07%)</td><td>317.31 <b>(-65.47%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2385.20 (n/a)</td><td>744.52 (n/a)</td><td>357.60 (n/a)</td><td>257.60 (n/a)</td><td>919.08 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (+0.04%)</td><td>0.05 (-2.83%)</td><td>0.05 (-8.19%)</td><td>0.03 (+16.38%)</td><td>0.01 (-10.52%)</td><td>495.00 (-14.06%)</td><td>376.64 (+0.17%)</td><td>359.20 (+8.91%)</td><td>244.30 (-0.04%)</td><td>100.37 <b>(-23.66%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>576.00 (n/a)</td><td>376.00 (n/a)</td><td>329.80 (n/a)</td><td>244.40 (n/a)</td><td>131.47 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (+5.76%)</td><td>0.04 (+3.47%)</td><td>0.04 (+14.89%)</td><td>0.01 <b>(-66.17%)</b></td><td>0.03 <b>(+36.02%)</b></td><td>1908.30 <b>(+195.59%)</b></td><td>709.40 <b>(+40.44%)</b></td><td>501.80 (-12.97%)</td><td>233.10 (-5.44%)</td><td>684.52 <b>(+311.72%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>645.60 (n/a)</td><td>505.14 (n/a)</td><td>576.60 (n/a)</td><td>246.50 (n/a)</td><td>166.26 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.04 <b>(-24.72%)</b></td><td>0.03 <b>(-22.91%)</b></td><td>0.03 <b>(-32.78%)</b></td><td>0.03 (+10.00%)</td><td>0.01 <b>(-44.22%)</b></td><td>617.10 (-9.09%)</td><td>516.20 <b>(+22.52%)</b></td><td>565.50 <b>(+48.74%)</b></td><td>382.90 <b>(+32.81%)</b></td><td>107.48 <b>(-32.15%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>678.80 (n/a)</td><td>421.32 (n/a)</td><td>380.20 (n/a)</td><td>288.30 (n/a)</td><td>158.40 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (+1.07%)</td><td>0.09 (-4.09%)</td><td>0.09 (-14.34%)</td><td>0.05 <b>(+175.29%)</b></td><td>0.03 <b>(-22.88%)</b></td><td>682.10 <b>(-63.67%)</b></td><td>411.64 <b>(-32.14%)</b></td><td>358.50 (+16.74%)</td><td>256.00 (-1.08%)</td><td>177.35 <b>(-75.05%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1877.70 (n/a)</td><td>606.64 (n/a)</td><td>307.10 (n/a)</td><td>258.80 (n/a)</td><td>710.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 <b>(+25.09%)</b></td><td>0.09 (-1.80%)</td><td>0.08 <b>(-30.82%)</b></td><td>0.06 <b>(+24.98%)</b></td><td>0.04 (+18.49%)</td><td>544.40 (-19.99%)</td><td>399.36 (+1.05%)</td><td>422.70 <b>(+44.56%)</b></td><td>201.70 <b>(-20.02%)</b></td><td>149.78 (-19.39%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>680.40 (n/a)</td><td>395.22 (n/a)</td><td>292.40 (n/a)</td><td>252.20 (n/a)</td><td>185.81 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 (-2.88%)</td><td>0.11 (+4.36%)</td><td>0.11 <b>(+41.83%)</b></td><td>0.07 (-1.80%)</td><td>0.04 (-14.47%)</td><td>628.60 (+1.85%)</td><td>417.00 (-6.79%)</td><td>375.20 <b>(-29.49%)</b></td><td>264.10 (+2.96%)</td><td>151.68 (-7.68%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>617.20 (n/a)</td><td>447.36 (n/a)</td><td>532.10 (n/a)</td><td>256.50 (n/a)</td><td>164.30 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (+6.65%)</td><td>0.09 (+5.08%)</td><td>0.08 (-10.79%)</td><td>0.05 (+1.63%)</td><td>0.03 (+14.70%)</td><td>613.30 (-1.60%)</td><td>406.18 (-3.12%)</td><td>434.50 (+12.10%)</td><td>232.70 (-6.24%)</td><td>143.85 (+5.02%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>623.30 (n/a)</td><td>419.24 (n/a)</td><td>387.60 (n/a)</td><td>248.20 (n/a)</td><td>136.97 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.19 (-1.10%)</td><td>0.14 <b>(+48.12%)</b></td><td>0.14 <b>(+90.94%)</b></td><td>0.09 <b>(+33.93%)</b></td><td>0.04 <b>(-33.70%)</b></td><td>453.10 <b>(-25.34%)</b></td><td>308.90 <b>(-38.95%)</b></td><td>295.20 <b>(-47.63%)</b></td><td>217.10 (+1.12%)</td><td>88.17 <b>(-46.23%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>606.90 (n/a)</td><td>505.94 (n/a)</td><td>563.70 (n/a)</td><td>214.70 (n/a)</td><td>163.97 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (+3.79%)</td><td>0.07 <b>(-31.45%)</b></td><td>0.06 <b>(-55.03%)</b></td><td>0.05 <b>(-32.84%)</b></td><td>0.04 (+8.17%)</td><td>710.80 <b>(+48.89%)</b></td><td>512.42 <b>(+52.52%)</b></td><td>557.10 <b>(+122.31%)</b></td><td>235.40 (-3.64%)</td><td>175.07 <b>(+43.17%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>477.40 (n/a)</td><td>335.96 (n/a)</td><td>250.60 (n/a)</td><td>244.30 (n/a)</td><td>122.28 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (+14.87%)</td><td>0.10 <b>(+25.13%)</b></td><td>0.11 <b>(+45.35%)</b></td><td>0.07 (+4.02%)</td><td>0.03 <b>(+28.19%)</b></td><td>542.10 (-3.87%)</td><td>388.88 (-18.22%)</td><td>337.50 <b>(-31.21%)</b></td><td>260.30 (-12.94%)</td><td>121.35 (+13.56%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>563.90 (n/a)</td><td>475.52 (n/a)</td><td>490.60 (n/a)</td><td>299.00 (n/a)</td><td>106.86 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (+1.79%)</td><td>0.08 (-14.99%)</td><td>0.07 <b>(-20.38%)</b></td><td>0.03 <b>(-59.40%)</b></td><td>0.04 <b>(+59.05%)</b></td><td>1150.30 <b>(+146.32%)</b></td><td>544.86 <b>(+46.67%)</b></td><td>481.50 <b>(+25.59%)</b></td><td>259.00 (-1.75%)</td><td>360.06 <b>(+274.57%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>467.00 (n/a)</td><td>371.48 (n/a)</td><td>383.40 (n/a)</td><td>263.60 (n/a)</td><td>96.13 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 <b>(-36.71%)</b></td><td>0.07 <b>(-30.08%)</b></td><td>0.07 (-15.50%)</td><td>0.02 (+1.35%)</td><td>0.04 <b>(-43.99%)</b></td><td>1869.80 (-1.34%)</td><td>758.44 (+11.48%)</td><td>554.90 (+18.34%)</td><td>255.70 <b>(+58.03%)</b></td><td>634.97 (-9.22%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.23 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.08 (n/a)</td><td>1895.10 (n/a)</td><td>680.36 (n/a)</td><td>468.90 (n/a)</td><td>161.80 (n/a)</td><td>699.43 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 <b>(+94.94%)</b></td><td>0.08 <b>(+39.17%)</b></td><td>0.07 (+14.31%)</td><td>0.04 (-12.07%)</td><td>0.04 <b>(+359.51%)</b></td><td>794.90 (+13.72%)</td><td>489.04 (-15.09%)</td><td>485.90 (-12.51%)</td><td>247.80 <b>(-48.70%)</b></td><td>225.14 <b>(+159.95%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>699.00 (n/a)</td><td>575.98 (n/a)</td><td>555.40 (n/a)</td><td>483.00 (n/a)</td><td>86.61 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 (-6.89%)</td><td>0.06 (-2.67%)</td><td>0.05 (+11.58%)</td><td>0.04 (-10.23%)</td><td>0.02 (-4.40%)</td><td>581.40 (+11.40%)</td><td>416.52 (+4.02%)</td><td>411.60 (-10.37%)</td><td>230.70 (+7.40%)</td><td>151.83 (+17.89%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>521.90 (n/a)</td><td>400.44 (n/a)</td><td>459.20 (n/a)</td><td>214.80 (n/a)</td><td>128.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (-3.77%)</td><td>0.07 (+17.48%)</td><td>0.07 (+0.12%)</td><td>0.06 <b>(+55.91%)</b></td><td>0.01 <b>(-58.36%)</b></td><td>352.40 <b>(-35.86%)</b></td><td>300.46 <b>(-22.08%)</b></td><td>307.70 (-0.13%)</td><td>259.70 (+3.92%)</td><td>36.22 <b>(-73.93%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>549.40 (n/a)</td><td>385.60 (n/a)</td><td>308.10 (n/a)</td><td>249.90 (n/a)</td><td>138.93 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 <b>(+28.83%)</b></td><td>0.07 <b>(+23.25%)</b></td><td>0.08 (+18.48%)</td><td>0.04 <b>(+51.52%)</b></td><td>0.03 <b>(+23.10%)</b></td><td>529.50 <b>(-34.00%)</b></td><td>336.78 <b>(-21.18%)</b></td><td>244.70 (-15.62%)</td><td>189.00 <b>(-22.38%)</b></td><td>157.71 <b>(-32.96%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>802.30 (n/a)</td><td>427.28 (n/a)</td><td>290.00 (n/a)</td><td>243.50 (n/a)</td><td>235.26 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (+6.58%)</td><td>0.06 (-4.57%)</td><td>0.05 <b>(-20.58%)</b></td><td>0.04 (+7.89%)</td><td>0.02 (+19.73%)</td><td>482.90 (-7.31%)</td><td>380.98 (+5.89%)</td><td>393.10 <b>(+25.91%)</b></td><td>272.70 (-6.19%)</td><td>98.12 (+2.66%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>521.00 (n/a)</td><td>359.80 (n/a)</td><td>312.20 (n/a)</td><td>290.70 (n/a)</td><td>95.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (-18.96%)</td><td>0.06 (-11.23%)</td><td>0.05 (-19.79%)</td><td>0.04 (-11.58%)</td><td>0.02 (-11.15%)</td><td>576.30 (+13.09%)</td><td>396.00 (+12.96%)</td><td>435.70 <b>(+24.66%)</b></td><td>242.00 <b>(+23.41%)</b></td><td>149.10 (+13.41%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>509.60 (n/a)</td><td>350.58 (n/a)</td><td>349.50 (n/a)</td><td>196.10 (n/a)</td><td>131.47 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (-18.27%)</td><td>0.05 (-7.51%)</td><td>0.05 <b>(+29.67%)</b></td><td>0.01 <b>(-69.92%)</b></td><td>0.03 (+2.88%)</td><td>1949.60 <b>(+232.41%)</b></td><td>668.80 <b>(+58.24%)</b></td><td>392.00 <b>(-22.88%)</b></td><td>248.80 <b>(+22.38%)</b></td><td>722.83 <b>(+331.54%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>586.50 (n/a)</td><td>422.66 (n/a)</td><td>508.30 (n/a)</td><td>203.30 (n/a)</td><td>167.50 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (-0.57%)</td><td>0.07 (-17.32%)</td><td>0.08 (-13.93%)</td><td>0.04 <b>(-32.91%)</b></td><td>0.02 <b>(+51.76%)</b></td><td>567.90 <b>(+49.06%)</b></td><td>376.78 <b>(+29.20%)</b></td><td>306.40 (+16.19%)</td><td>247.70 (+0.57%)</td><td>134.08 <b>(+134.42%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>381.00 (n/a)</td><td>291.62 (n/a)</td><td>263.70 (n/a)</td><td>246.30 (n/a)</td><td>57.19 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (+6.42%)</td><td>0.07 (+3.37%)</td><td>0.07 (-18.69%)</td><td>0.05 <b>(+95.12%)</b></td><td>0.02 <b>(-25.52%)</b></td><td>545.60 <b>(-48.75%)</b></td><td>376.40 <b>(-21.28%)</b></td><td>377.20 <b>(+22.99%)</b></td><td>229.30 (-6.02%)</td><td>123.26 <b>(-64.28%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1064.50 (n/a)</td><td>478.14 (n/a)</td><td>306.70 (n/a)</td><td>244.00 (n/a)</td><td>345.11 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.06 <b>(-27.60%)</b></td><td>0.05 <b>(-28.41%)</b></td><td>0.05 <b>(-43.01%)</b></td><td>0.04 (-2.34%)</td><td>0.01 <b>(-49.94%)</b></td><td>576.40 (+2.38%)</td><td>500.16 <b>(+34.24%)</b></td><td>532.20 <b>(+75.47%)</b></td><td>403.40 <b>(+38.10%)</b></td><td>82.76 <b>(-28.38%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>563.00 (n/a)</td><td>372.60 (n/a)</td><td>303.30 (n/a)</td><td>292.10 (n/a)</td><td>115.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.09 <b>(+39.11%)</b></td><td>0.07 <b>(+22.15%)</b></td><td>0.08 <b>(+40.10%)</b></td><td>0.04 (-18.61%)</td><td>0.03 <b>(+257.33%)</b></td><td>641.30 <b>(+22.88%)</b></td><td>429.96 (-5.95%)</td><td>327.40 <b>(-28.61%)</b></td><td>265.70 <b>(-28.11%)</b></td><td>192.54 <b>(+236.11%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>521.90 (n/a)</td><td>457.14 (n/a)</td><td>458.60 (n/a)</td><td>369.60 (n/a)</td><td>57.28 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (+7.85%)</td><td>0.07 (-0.98%)</td><td>0.05 (-9.89%)</td><td>0.04 (-9.49%)</td><td>0.03 (+19.73%)</td><td>630.20 (+10.48%)</td><td>411.94 (+5.63%)</td><td>469.00 (+10.98%)</td><td>235.20 (-7.29%)</td><td>167.34 <b>(+23.49%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>570.40 (n/a)</td><td>389.98 (n/a)</td><td>422.60 (n/a)</td><td>253.70 (n/a)</td><td>135.51 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.12 <b>(+21.84%)</b></td><td>0.09 <b>(+28.43%)</b></td><td>0.08 <b>(+26.70%)</b></td><td>0.06 <b>(+47.11%)</b></td><td>0.02 (-19.05%)</td><td>414.20 <b>(-32.02%)</b></td><td>301.10 <b>(-28.62%)</b></td><td>292.20 <b>(-21.09%)</b></td><td>207.00 (-17.92%)</td><td>74.06 <b>(-57.00%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>609.30 (n/a)</td><td>421.82 (n/a)</td><td>370.30 (n/a)</td><td>252.20 (n/a)</td><td>172.21 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 <b>(+61.90%)</b></td><td>0.06 <b>(+50.65%)</b></td><td>0.05 <b>(+35.07%)</b></td><td>0.04 (+13.98%)</td><td>0.02 <b>(+222.10%)</b></td><td>477.70 (-12.27%)</td><td>357.24 <b>(-27.96%)</b></td><td>390.10 <b>(-25.96%)</b></td><td>231.40 <b>(-38.24%)</b></td><td>119.17 <b>(+68.91%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>544.50 (n/a)</td><td>495.86 (n/a)</td><td>526.90 (n/a)</td><td>374.70 (n/a)</td><td>70.55 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (+12.32%)</td><td>0.06 (-11.36%)</td><td>0.04 <b>(-41.65%)</b></td><td>0.03 (-8.16%)</td><td>0.04 <b>(+42.71%)</b></td><td>638.30 (+8.89%)</td><td>432.82 <b>(+28.77%)</b></td><td>511.90 <b>(+71.38%)</b></td><td>169.40 (-10.94%)</td><td>214.14 <b>(+39.41%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>586.20 (n/a)</td><td>336.12 (n/a)</td><td>298.70 (n/a)</td><td>190.20 (n/a)</td><td>153.61 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 (+14.57%)</td><td>0.06 (+8.31%)</td><td>0.06 (+0.12%)</td><td>0.04 (+14.58%)</td><td>0.02 <b>(+20.87%)</b></td><td>465.30 (-12.72%)</td><td>333.92 (-6.87%)</td><td>301.60 (-0.13%)</td><td>221.00 (-12.72%)</td><td>105.34 (-7.07%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>533.10 (n/a)</td><td>358.56 (n/a)</td><td>302.00 (n/a)</td><td>253.20 (n/a)</td><td>113.36 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (-7.80%)</td><td>0.06 (-7.94%)</td><td>0.07 (-5.63%)</td><td>0.03 (-14.42%)</td><td>0.02 (-4.37%)</td><td>558.30 (+16.85%)</td><td>357.24 (+9.92%)</td><td>268.60 (+5.96%)</td><td>254.30 (+8.49%)</td><td>138.72 (+18.99%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>477.80 (n/a)</td><td>325.00 (n/a)</td><td>253.50 (n/a)</td><td>234.40 (n/a)</td><td>116.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (-14.37%)</td><td>0.05 (-16.47%)</td><td>0.04 <b>(-42.92%)</b></td><td>0.03 (+0.60%)</td><td>0.02 <b>(-29.83%)</b></td><td>612.70 (-0.58%)</td><td>425.74 (+10.71%)</td><td>473.70 <b>(+75.18%)</b></td><td>274.50 (+16.76%)</td><td>142.76 <b>(-23.44%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>616.30 (n/a)</td><td>384.54 (n/a)</td><td>270.40 (n/a)</td><td>235.10 (n/a)</td><td>186.48 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.08 <b>(+21.61%)</b></td><td>0.05 (-15.54%)</td><td>0.04 <b>(-30.64%)</b></td><td>0.03 <b>(-20.70%)</b></td><td>0.02 <b>(+61.24%)</b></td><td>624.30 <b>(+26.10%)</b></td><td>442.28 <b>(+26.79%)</b></td><td>430.50 <b>(+44.17%)</b></td><td>223.10 (-17.77%)</td><td>147.33 <b>(+57.07%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>495.10 (n/a)</td><td>348.82 (n/a)</td><td>298.60 (n/a)</td><td>271.30 (n/a)</td><td>93.80 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.47 <b>(+22.21%)</b></td><td>0.33 <b>(+53.34%)</b></td><td>0.35 <b>(+76.13%)</b></td><td>0.18 <b>(+375.29%)</b></td><td>0.13 (-1.06%)</td><td>531.90 <b>(-78.96%)</b></td><td>347.08 <b>(-58.95%)</b></td><td>278.60 <b>(-43.22%)</b></td><td>208.70 (-18.16%)</td><td>148.45 <b>(-84.36%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.39 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>0.13 (n/a)</td><td>2528.00 (n/a)</td><td>845.58 (n/a)</td><td>490.70 (n/a)</td><td>255.00 (n/a)</td><td>949.24 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.38 <b>(+48.10%)</b></td><td>0.28 <b>(+33.51%)</b></td><td>0.27 <b>(+36.44%)</b></td><td>0.17 (-4.46%)</td><td>0.08 <b>(+165.80%)</b></td><td>585.50 (+4.67%)</td><td>382.76 <b>(-20.31%)</b></td><td>359.20 <b>(-26.69%)</b></td><td>257.40 <b>(-32.48%)</b></td><td>126.71 <b>(+95.69%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>559.40 (n/a)</td><td>480.32 (n/a)</td><td>490.00 (n/a)</td><td>381.20 (n/a)</td><td>64.75 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.39 <b>(+84.70%)</b></td><td>0.32 <b>(+61.52%)</b></td><td>0.35 <b>(+77.62%)</b></td><td>0.17 (-6.55%)</td><td>0.09 <b>(+587.23%)</b></td><td>595.60 (+7.01%)</td><td>342.72 <b>(-31.99%)</b></td><td>279.90 <b>(-43.69%)</b></td><td>251.60 <b>(-45.86%)</b></td><td>143.24 <b>(+316.62%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>556.60 (n/a)</td><td>503.90 (n/a)</td><td>497.10 (n/a)</td><td>464.70 (n/a)</td><td>34.38 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.30 (+6.37%)</td><td>0.24 <b>(+26.98%)</b></td><td>0.24 (+11.76%)</td><td>0.16 <b>(+323.32%)</b></td><td>0.05 <b>(-47.04%)</b></td><td>453.70 <b>(-76.38%)</b></td><td>322.58 <b>(-50.83%)</b></td><td>306.20 (-10.52%)</td><td>248.00 (-5.99%)</td><td>77.95 <b>(-89.02%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>0.09 (n/a)</td><td>1920.50 (n/a)</td><td>656.00 (n/a)</td><td>342.20 (n/a)</td><td>263.80 (n/a)</td><td>709.85 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.27 (-15.58%)</td><td>0.22 (-8.87%)</td><td>0.24 (-1.94%)</td><td>0.13 (+1.55%)</td><td>0.06 (-17.35%)</td><td>563.20 (-1.52%)</td><td>365.38 (+7.38%)</td><td>304.20 (+1.98%)</td><td>276.00 (+18.45%)</td><td>119.30 (-10.24%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>571.90 (n/a)</td><td>340.26 (n/a)</td><td>298.30 (n/a)</td><td>233.00 (n/a)</td><td>132.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.27 <b>(-25.53%)</b></td><td>0.16 <b>(-34.87%)</b></td><td>0.14 <b>(-47.19%)</b></td><td>0.03 <b>(-77.83%)</b></td><td>0.10 (+4.41%)</td><td>2450.60 <b>(+351.06%)</b></td><td>841.46 <b>(+144.67%)</b></td><td>531.70 <b>(+89.35%)</b></td><td>270.30 <b>(+34.28%)</b></td><td>913.84 <b>(+527.69%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.37 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>543.30 (n/a)</td><td>343.92 (n/a)</td><td>280.80 (n/a)</td><td>201.30 (n/a)</td><td>145.59 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.15 (-6.22%)</td><td>0.12 (+5.17%)</td><td>0.12 (-0.24%)</td><td>0.07 (+10.89%)</td><td>0.03 (-6.95%)</td><td>510.10 (-9.81%)</td><td>323.02 (-6.48%)</td><td>307.10 (+0.23%)</td><td>243.60 (+6.61%)</td><td>109.21 (-15.22%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>565.60 (n/a)</td><td>345.42 (n/a)</td><td>306.40 (n/a)</td><td>228.50 (n/a)</td><td>128.81 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (+11.67%)</td><td>0.13 <b>(+30.13%)</b></td><td>0.13 <b>(+39.30%)</b></td><td>0.11 <b>(+65.77%)</b></td><td>0.01 <b>(-60.38%)</b></td><td>326.90 <b>(-39.68%)</b></td><td>293.28 <b>(-28.12%)</b></td><td>294.80 <b>(-28.20%)</b></td><td>255.60 (-10.47%)</td><td>26.30 <b>(-78.14%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>541.90 (n/a)</td><td>408.02 (n/a)</td><td>410.60 (n/a)</td><td>285.50 (n/a)</td><td>120.29 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.12 <b>(-21.23%)</b></td><td>0.08 <b>(-29.67%)</b></td><td>0.08 <b>(-34.14%)</b></td><td>0.04 <b>(-52.78%)</b></td><td>0.03 (-11.17%)</td><td>1025.30 <b>(+111.80%)</b></td><td>538.24 <b>(+54.06%)</b></td><td>464.50 <b>(+51.85%)</b></td><td>311.30 <b>(+26.96%)</b></td><td>279.45 <b>(+157.17%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>484.10 (n/a)</td><td>349.38 (n/a)</td><td>305.90 (n/a)</td><td>245.20 (n/a)</td><td>108.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.15 (+12.71%)</td><td>0.12 <b>(+26.55%)</b></td><td>0.13 <b>(+33.69%)</b></td><td>0.06 (+11.73%)</td><td>0.03 (-0.39%)</td><td>574.30 (-10.50%)</td><td>342.46 <b>(-23.00%)</b></td><td>282.90 <b>(-25.22%)</b></td><td>252.30 (-11.29%)</td><td>134.53 <b>(-22.05%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>641.70 (n/a)</td><td>444.78 (n/a)</td><td>378.30 (n/a)</td><td>284.40 (n/a)</td><td>172.58 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (+3.79%)</td><td>0.10 <b>(+30.48%)</b></td><td>0.12 <b>(+59.28%)</b></td><td>0.06 <b>(+307.44%)</b></td><td>0.03 <b>(-28.26%)</b></td><td>600.80 <b>(-75.45%)</b></td><td>399.48 <b>(-52.13%)</b></td><td>304.90 <b>(-37.22%)</b></td><td>290.40 (-3.65%)</td><td>143.43 <b>(-84.25%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2447.70 (n/a)</td><td>834.46 (n/a)</td><td>485.70 (n/a)</td><td>301.40 (n/a)</td><td>910.94 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.10 (-5.33%)</td><td>0.07 (-11.29%)</td><td>0.06 <b>(-21.58%)</b></td><td>0.06 (+0.09%)</td><td>0.02 (+2.50%)</td><td>624.70 (-0.08%)</td><td>542.00 (+13.31%)</td><td>613.30 <b>(+27.51%)</b></td><td>371.30 (+5.63%)</td><td>111.11 (+10.42%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>625.20 (n/a)</td><td>478.34 (n/a)</td><td>481.00 (n/a)</td><td>351.50 (n/a)</td><td>100.62 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (-3.05%)</td><td>0.14 <b>(+25.36%)</b></td><td>0.16 <b>(+86.35%)</b></td><td>0.07 (-7.47%)</td><td>0.04 (-11.17%)</td><td>595.70 (+8.07%)</td><td>325.76 <b>(-21.17%)</b></td><td>256.50 <b>(-46.35%)</b></td><td>246.70 (+3.14%)</td><td>151.56 (+1.47%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>551.20 (n/a)</td><td>413.24 (n/a)</td><td>478.10 (n/a)</td><td>239.20 (n/a)</td><td>149.37 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 (+3.18%)</td><td>0.13 (+5.90%)</td><td>0.14 (+5.78%)</td><td>0.10 <b>(+33.33%)</b></td><td>0.02 (-19.11%)</td><td>422.80 <b>(-25.00%)</b></td><td>325.86 (-8.85%)</td><td>301.00 (-5.46%)</td><td>257.90 (-3.08%)</td><td>65.18 <b>(-44.55%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>563.70 (n/a)</td><td>357.48 (n/a)</td><td>318.40 (n/a)</td><td>266.10 (n/a)</td><td>117.56 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.18 <b>(+26.87%)</b></td><td>0.13 <b>(+38.23%)</b></td><td>0.15 <b>(+83.58%)</b></td><td>0.06 <b>(+218.52%)</b></td><td>0.05 (+8.88%)</td><td>638.40 <b>(-68.60%)</b></td><td>397.08 <b>(-46.15%)</b></td><td>278.30 <b>(-45.54%)</b></td><td>229.10 <b>(-21.16%)</b></td><td>201.16 <b>(-72.61%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2033.40 (n/a)</td><td>737.40 (n/a)</td><td>511.00 (n/a)</td><td>290.60 (n/a)</td><td>734.35 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (-4.48%)</td><td>0.11 (+9.82%)</td><td>0.08 (+3.67%)</td><td>0.07 (-1.76%)</td><td>0.04 (-2.54%)</td><td>615.80 (+1.79%)</td><td>432.92 (-8.62%)</td><td>482.30 (-3.54%)</td><td>243.10 (+4.69%)</td><td>157.75 (+4.92%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>605.00 (n/a)</td><td>473.78 (n/a)</td><td>500.00 (n/a)</td><td>232.20 (n/a)</td><td>150.35 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.17 (-1.13%)</td><td>0.12 (+10.11%)</td><td>0.12 (+16.94%)</td><td>0.07 (-2.22%)</td><td>0.04 (-10.87%)</td><td>623.70 (+2.26%)</td><td>379.84 (-11.71%)</td><td>349.60 (-14.50%)</td><td>243.70 (+1.16%)</td><td>150.05 (-11.20%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>609.90 (n/a)</td><td>430.24 (n/a)</td><td>408.90 (n/a)</td><td>240.90 (n/a)</td><td>168.98 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (-7.64%)</td><td>0.11 (+6.25%)</td><td>0.12 <b>(+24.18%)</b></td><td>0.08 (-0.96%)</td><td>0.03 (-8.75%)</td><td>543.50 (+0.97%)</td><td>379.12 (-6.32%)</td><td>329.20 (-19.45%)</td><td>296.50 (+8.25%)</td><td>104.10 (-0.48%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>538.30 (n/a)</td><td>404.70 (n/a)</td><td>408.70 (n/a)</td><td>273.90 (n/a)</td><td>104.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 <b>(+21.27%)</b></td><td>0.10 (-7.20%)</td><td>0.10 (-12.08%)</td><td>0.05 <b>(-36.67%)</b></td><td>0.04 <b>(+76.99%)</b></td><td>702.10 <b>(+57.92%)</b></td><td>398.48 <b>(+20.95%)</b></td><td>347.80 (+13.73%)</td><td>211.50 (-17.54%)</td><td>187.81 <b>(+138.70%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>444.60 (n/a)</td><td>329.46 (n/a)</td><td>305.80 (n/a)</td><td>256.50 (n/a)</td><td>78.68 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.16 (-8.75%)</td><td>0.12 (-6.67%)</td><td>0.11 (-7.45%)</td><td>0.06 <b>(-23.89%)</b></td><td>0.04 (+5.49%)</td><td>567.60 <b>(+31.39%)</b></td><td>332.44 (+11.80%)</td><td>312.30 (+8.02%)</td><td>212.10 (+9.61%)</td><td>138.38 <b>(+58.99%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>432.00 (n/a)</td><td>297.34 (n/a)</td><td>289.10 (n/a)</td><td>193.50 (n/a)</td><td>87.04 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.19 <b>(+146.95%)</b></td><td>0.10 <b>(+76.39%)</b></td><td>0.08 (+12.65%)</td><td>0.06 <b>(+228.57%)</b></td><td>0.06 <b>(+119.02%)</b></td><td>595.20 <b>(-69.57%)</b></td><td>407.14 <b>(-49.48%)</b></td><td>428.70 (-11.24%)</td><td>179.60 <b>(-59.49%)</b></td><td>177.42 <b>(-72.76%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1955.80 (n/a)</td><td>805.88 (n/a)</td><td>483.00 (n/a)</td><td>443.40 (n/a)</td><td>651.27 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.18 <b>(+48.02%)</b></td><td>0.11 <b>(+24.86%)</b></td><td>0.10 (+19.96%)</td><td>0.07 (+12.58%)</td><td>0.04 <b>(+55.28%)</b></td><td>530.50 (-11.18%)</td><td>345.96 (-17.71%)</td><td>340.60 (-16.62%)</td><td>193.90 <b>(-32.46%)</b></td><td>121.02 (-6.79%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>597.30 (n/a)</td><td>420.44 (n/a)</td><td>408.50 (n/a)</td><td>287.10 (n/a)</td><td>129.84 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (-2.77%)</td><td>0.08 (+14.85%)</td><td>0.08 (+18.97%)</td><td>0.05 <b>(+140.92%)</b></td><td>0.03 <b>(-29.42%)</b></td><td>773.20 <b>(-58.49%)</b></td><td>469.66 <b>(-36.07%)</b></td><td>428.90 (-15.95%)</td><td>275.80 (+2.83%)</td><td>183.73 <b>(-71.53%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1862.70 (n/a)</td><td>734.68 (n/a)</td><td>510.30 (n/a)</td><td>268.20 (n/a)</td><td>645.26 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.11 (+10.60%)</td><td>0.08 (+5.25%)</td><td>0.07 (+15.08%)</td><td>0.06 (-2.18%)</td><td>0.02 (+10.52%)</td><td>612.00 (+2.22%)</td><td>465.64 (-4.69%)</td><td>471.40 (-13.11%)</td><td>304.90 (-9.61%)</td><td>111.67 (-1.60%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>598.70 (n/a)</td><td>488.54 (n/a)</td><td>542.50 (n/a)</td><td>337.30 (n/a)</td><td>113.49 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.49 <b>(+21.83%)</b></td><td>0.42 <b>(+28.79%)</b></td><td>0.41 (+3.46%)</td><td>0.36 <b>(+72.21%)</b></td><td>0.05 <b>(-48.41%)</b></td><td>365.10 <b>(-41.93%)</b></td><td>314.38 <b>(-27.95%)</b></td><td>318.80 (-3.34%)</td><td>267.30 (-17.93%)</td><td>37.90 <b>(-74.72%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.40 (n/a)</td><td>0.33 (n/a)</td><td>0.40 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>628.70 (n/a)</td><td>436.36 (n/a)</td><td>329.80 (n/a)</td><td>325.70 (n/a)</td><td>149.87 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.41 (-6.39%)</td><td>0.28 <b>(-21.67%)</b></td><td>0.26 <b>(-33.31%)</b></td><td>0.20 <b>(-20.87%)</b></td><td>0.08 (-3.94%)</td><td>649.30 <b>(+26.37%)</b></td><td>498.56 <b>(+28.50%)</b></td><td>511.20 <b>(+49.96%)</b></td><td>319.70 (+6.82%)</td><td>117.31 <b>(+21.94%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>513.80 (n/a)</td><td>387.98 (n/a)</td><td>340.90 (n/a)</td><td>299.30 (n/a)</td><td>96.20 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.41 (-4.41%)</td><td>0.24 <b>(-30.66%)</b></td><td>0.25 <b>(-39.51%)</b></td><td>0.06 <b>(-72.04%)</b></td><td>0.12 (+17.35%)</td><td>2170.20 <b>(+257.71%)</b></td><td>819.94 <b>(+98.92%)</b></td><td>514.60 <b>(+65.31%)</b></td><td>323.20 (+4.60%)</td><td>760.86 <b>(+432.41%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.42 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>606.70 (n/a)</td><td>412.20 (n/a)</td><td>311.30 (n/a)</td><td>309.00 (n/a)</td><td>142.91 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.00 (+16.67%)</td><td>0.00 <b>(+23.53%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+11.21%)</td><td>17308.17 (-14.03%)</td><td>12025.76 (-16.31%)</td><td>14282.19 <b>(-22.02%)</b></td><td>6249.35 (-12.73%)</td><td>5282.80 (-17.77%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20132.05 (n/a)</td><td>14370.03 (n/a)</td><td>18314.19 (n/a)</td><td>7160.57 (n/a)</td><td>6424.79 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.00 (+16.67%)</td><td>0.00 (+7.69%)</td><td>0.00 <b>(+66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+24.14%)</b></td><td>22078.52 (+7.82%)</td><td>12948.70 (+2.03%)</td><td>8546.00 <b>(-39.36%)</b></td><td>5947.46 (-12.69%)</td><td>7596.55 <b>(+35.81%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20477.80 (n/a)</td><td>12690.65 (n/a)</td><td>14092.58 (n/a)</td><td>6811.57 (n/a)</td><td>5593.36 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (-10.79%)</td><td>0.10 (+4.90%)</td><td>0.09 (+10.69%)</td><td>0.07 (-2.39%)</td><td>0.03 (-13.16%)</td><td>28586.24 (+2.52%)</td><td>21421.34 (-5.72%)</td><td>23027.80 (-9.60%)</td><td>15184.85 (+12.10%)</td><td>5730.03 (-4.23%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27884.22 (n/a)</td><td>22721.62 (n/a)</td><td>25473.99 (n/a)</td><td>13546.16 (n/a)</td><td>5983.28 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>2.59 <b>(+48.54%)</b></td><td>1.69 <b>(+24.80%)</b></td><td>1.70 (+12.03%)</td><td>0.31 <b>(-24.67%)</b></td><td>0.89 <b>(+66.95%)</b></td><td>3357.60 <b>(+32.75%)</b></td><td>1104.04 (+6.76%)</td><td>615.10 (-10.74%)</td><td>405.60 <b>(-32.67%)</b></td><td>1265.57 <b>(+51.28%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>1.74 (n/a)</td><td>1.36 (n/a)</td><td>1.52 (n/a)</td><td>0.41 (n/a)</td><td>0.54 (n/a)</td><td>2529.20 (n/a)</td><td>1034.18 (n/a)</td><td>689.10 (n/a)</td><td>602.40 (n/a)</td><td>836.60 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.53 <b>(+43.52%)</b></td><td>2.04 (+10.48%)</td><td>2.34 <b>(+36.07%)</b></td><td>0.29 <b>(-70.30%)</b></td><td>1.19 <b>(+97.43%)</b></td><td>3602.90 <b>(+236.72%)</b></td><td>1087.44 <b>(+71.28%)</b></td><td>447.40 <b>(-26.51%)</b></td><td>297.10 <b>(-30.32%)</b></td><td>1411.99 <b>(+441.95%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>2.46 (n/a)</td><td>1.84 (n/a)</td><td>1.72 (n/a)</td><td>0.98 (n/a)</td><td>0.60 (n/a)</td><td>1070.00 (n/a)</td><td>634.90 (n/a)</td><td>608.80 (n/a)</td><td>426.40 (n/a)</td><td>260.54 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.96 <b>(+52.25%)</b></td><td>2.39 (+9.70%)</td><td>2.11 (-12.56%)</td><td>1.59 (-0.85%)</td><td>0.94 <b>(+93.07%)</b></td><td>659.50 (+0.86%)</td><td>483.08 (-3.73%)</td><td>496.30 (+14.35%)</td><td>264.60 <b>(-34.33%)</b></td><td>149.97 <b>(+24.06%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>2.60 (n/a)</td><td>2.18 (n/a)</td><td>2.42 (n/a)</td><td>1.60 (n/a)</td><td>0.48 (n/a)</td><td>653.90 (n/a)</td><td>501.82 (n/a)</td><td>434.00 (n/a)</td><td>402.90 (n/a)</td><td>120.88 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>2.66 <b>(-29.11%)</b></td><td>1.86 <b>(-24.60%)</b></td><td>1.77 <b>(-39.89%)</b></td><td>1.08 <b>(+92.07%)</b></td><td>0.61 <b>(-50.56%)</b></td><td>973.40 <b>(-47.94%)</b></td><td>621.44 (-7.84%)</td><td>592.00 <b>(+66.34%)</b></td><td>394.20 <b>(+41.09%)</b></td><td>224.03 <b>(-66.76%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.75 (n/a)</td><td>2.46 (n/a)</td><td>2.95 (n/a)</td><td>0.56 (n/a)</td><td>1.23 (n/a)</td><td>1869.60 (n/a)</td><td>674.32 (n/a)</td><td>355.90 (n/a)</td><td>279.40 (n/a)</td><td>674.06 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.64 (-5.99%)</td><td>2.15 <b>(-27.54%)</b></td><td>2.65 <b>(-20.19%)</b></td><td>0.86 <b>(+47.63%)</b></td><td>1.21 (-10.31%)</td><td>2442.40 <b>(-32.26%)</b></td><td>1372.48 (+14.86%)</td><td>790.30 <b>(+25.31%)</b></td><td>576.20 (+6.39%)</td><td>901.56 <b>(-33.13%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>3.87 (n/a)</td><td>2.96 (n/a)</td><td>3.32 (n/a)</td><td>0.58 (n/a)</td><td>1.35 (n/a)</td><td>3605.70 (n/a)</td><td>1194.90 (n/a)</td><td>630.70 (n/a)</td><td>541.60 (n/a)</td><td>1348.28 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.97 (+1.77%)</td><td>3.17 <b>(-22.43%)</b></td><td>2.52 <b>(-38.61%)</b></td><td>1.92 <b>(-27.06%)</b></td><td>1.60 (+14.46%)</td><td>1091.20 <b>(+37.10%)</b></td><td>764.46 <b>(+35.11%)</b></td><td>832.10 <b>(+62.90%)</b></td><td>351.40 (-1.73%)</td><td>269.34 <b>(+36.47%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>5.86 (n/a)</td><td>4.09 (n/a)</td><td>4.11 (n/a)</td><td>2.63 (n/a)</td><td>1.40 (n/a)</td><td>795.90 (n/a)</td><td>565.80 (n/a)</td><td>510.80 (n/a)</td><td>357.60 (n/a)</td><td>197.36 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.99 <b>(-27.98%)</b></td><td>1.89 <b>(-53.62%)</b></td><td>0.63 <b>(-83.58%)</b></td><td>0.58 <b>(-79.70%)</b></td><td>1.78 <b>(+75.84%)</b></td><td>3627.80 <b>(+392.57%)</b></td><td>2324.98 <b>(+330.66%)</b></td><td>3320.40 <b>(+508.91%)</b></td><td>525.80 <b>(+38.84%)</b></td><td>1626.45 <b>(+1115.47%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>5.54 (n/a)</td><td>4.08 (n/a)</td><td>3.85 (n/a)</td><td>2.85 (n/a)</td><td>1.01 (n/a)</td><td>736.50 (n/a)</td><td>539.86 (n/a)</td><td>545.30 (n/a)</td><td>378.70 (n/a)</td><td>133.81 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>4.47 (-17.89%)</td><td>3.21 (+1.43%)</td><td>2.98 (-0.74%)</td><td>1.99 <b>(+235.83%)</b></td><td>1.03 <b>(-44.34%)</b></td><td>1054.50 <b>(-70.22%)</b></td><td>712.24 <b>(-40.22%)</b></td><td>703.00 (+0.75%)</td><td>469.20 <b>(+21.78%)</b></td><td>236.58 <b>(-82.15%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>5.44 (n/a)</td><td>3.16 (n/a)</td><td>3.01 (n/a)</td><td>0.59 (n/a)</td><td>1.84 (n/a)</td><td>3541.20 (n/a)</td><td>1191.52 (n/a)</td><td>697.80 (n/a)</td><td>385.30 (n/a)</td><td>1325.73 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.63 (-12.48%)</td><td>3.61 (+10.49%)</td><td>3.22 (+11.58%)</td><td>2.82 <b>(+369.92%)</b></td><td>1.17 <b>(-46.95%)</b></td><td>744.90 <b>(-78.72%)</b></td><td>619.58 <b>(-48.44%)</b></td><td>651.20 (-10.39%)</td><td>372.30 (+14.24%)</td><td>151.96 <b>(-88.37%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>6.44 (n/a)</td><td>3.27 (n/a)</td><td>2.89 (n/a)</td><td>0.60 (n/a)</td><td>2.20 (n/a)</td><td>3500.30 (n/a)</td><td>1201.66 (n/a)</td><td>726.70 (n/a)</td><td>325.90 (n/a)</td><td>1307.07 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>6.44 <b>(+29.42%)</b></td><td>2.96 (-1.46%)</td><td>2.51 <b>(-22.72%)</b></td><td>0.57 (-1.10%)</td><td>2.58 <b>(+47.07%)</b></td><td>3651.90 (+1.11%)</td><td>1755.78 <b>(+41.01%)</b></td><td>836.40 <b>(+29.39%)</b></td><td>325.60 <b>(-22.73%)</b></td><td>1680.09 <b>(+24.93%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>4.98 (n/a)</td><td>3.00 (n/a)</td><td>3.24 (n/a)</td><td>0.58 (n/a)</td><td>1.75 (n/a)</td><td>3611.90 (n/a)</td><td>1245.14 (n/a)</td><td>646.40 (n/a)</td><td>421.40 (n/a)</td><td>1344.86 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>5.11 (+10.51%)</td><td>3.77 (+5.13%)</td><td>4.07 (+1.41%)</td><td>1.40 (+4.55%)</td><td>1.40 (+3.72%)</td><td>2993.30 (-4.36%)</td><td>1375.30 (-4.97%)</td><td>1030.00 (-1.40%)</td><td>820.40 (-9.51%)</td><td>908.92 (-4.26%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>4.63 (n/a)</td><td>3.59 (n/a)</td><td>4.02 (n/a)</td><td>1.34 (n/a)</td><td>1.35 (n/a)</td><td>3129.60 (n/a)</td><td>1447.18 (n/a)</td><td>1044.60 (n/a)</td><td>906.60 (n/a)</td><td>949.33 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>7.86 (-4.61%)</td><td>6.85 <b>(+105.29%)</b></td><td>7.42 <b>(+328.65%)</b></td><td>4.67 <b>(+276.48%)</b></td><td>1.29 <b>(-55.60%)</b></td><td>898.90 <b>(-73.44%)</b></td><td>635.10 <b>(-67.97%)</b></td><td>565.10 <b>(-76.67%)</b></td><td>533.80 (+4.83%)</td><td>151.42 <b>(-86.91%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>8.24 (n/a)</td><td>3.34 (n/a)</td><td>1.73 (n/a)</td><td>1.24 (n/a)</td><td>2.91 (n/a)</td><td>3384.20 (n/a)</td><td>1982.88 (n/a)</td><td>2422.20 (n/a)</td><td>509.20 (n/a)</td><td>1157.21 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>6.43 (-18.09%)</td><td>4.19 (-16.62%)</td><td>5.82 <b>(+29.67%)</b></td><td>1.17 <b>(-32.66%)</b></td><td>2.53 (+3.93%)</td><td>3598.80 <b>(+48.50%)</b></td><td>1628.70 <b>(+47.58%)</b></td><td>721.00 <b>(-22.87%)</b></td><td>652.50 <b>(+22.08%)</b></td><td>1338.37 <b>(+74.51%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>7.85 (n/a)</td><td>5.03 (n/a)</td><td>4.49 (n/a)</td><td>1.73 (n/a)</td><td>2.44 (n/a)</td><td>2423.40 (n/a)</td><td>1103.58 (n/a)</td><td>934.80 (n/a)</td><td>534.50 (n/a)</td><td>766.92 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>7.03 (-11.94%)</td><td>5.38 (+0.53%)</td><td>6.69 (+3.98%)</td><td>2.02 (+17.18%)</td><td>2.17 (-11.79%)</td><td>2075.00 (-14.66%)</td><td>976.24 (-7.52%)</td><td>627.00 (-3.82%)</td><td>596.30 (+13.58%)</td><td>633.03 <b>(-20.04%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>7.99 (n/a)</td><td>5.35 (n/a)</td><td>6.43 (n/a)</td><td>1.73 (n/a)</td><td>2.46 (n/a)</td><td>2431.40 (n/a)</td><td>1055.62 (n/a)</td><td>651.90 (n/a)</td><td>525.00 (n/a)</td><td>791.70 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>6.87 <b>(-24.94%)</b></td><td>5.18 (+16.10%)</td><td>5.07 <b>(+29.01%)</b></td><td>3.55 <b>(+212.41%)</b></td><td>1.41 <b>(-60.20%)</b></td><td>1180.10 <b>(-67.99%)</b></td><td>861.66 <b>(-54.08%)</b></td><td>827.70 <b>(-22.49%)</b></td><td>610.80 <b>(+33.22%)</b></td><td>239.84 <b>(-85.12%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>9.15 (n/a)</td><td>4.46 (n/a)</td><td>3.93 (n/a)</td><td>1.14 (n/a)</td><td>3.54 (n/a)</td><td>3686.80 (n/a)</td><td>1876.32 (n/a)</td><td>1067.80 (n/a)</td><td>458.50 (n/a)</td><td>1611.66 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>9.21 (-6.53%)</td><td>5.14 (-18.10%)</td><td>4.86 <b>(-34.76%)</b></td><td>1.17 (-5.96%)</td><td>3.01 (-7.36%)</td><td>3595.30 (+6.33%)</td><td>1327.06 (+16.00%)</td><td>863.70 <b>(+53.27%)</b></td><td>455.50 (+7.00%)</td><td>1289.95 (+2.57%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>9.85 (n/a)</td><td>6.27 (n/a)</td><td>7.44 (n/a)</td><td>1.24 (n/a)</td><td>3.25 (n/a)</td><td>3381.20 (n/a)</td><td>1144.00 (n/a)</td><td>563.50 (n/a)</td><td>425.70 (n/a)</td><td>1257.69 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>1.42 <b>(-27.67%)</b></td><td>0.77 <b>(-41.25%)</b></td><td>0.71 <b>(-33.73%)</b></td><td>0.16 <b>(-81.66%)</b></td><td>0.48 (+0.34%)</td><td>3309.00 <b>(+445.32%)</b></td><td>1180.32 <b>(+168.18%)</b></td><td>741.20 <b>(+50.90%)</b></td><td>369.60 <b>(+38.27%)</b></td><td>1212.86 <b>(+734.10%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>1.96 (n/a)</td><td>1.32 (n/a)</td><td>1.07 (n/a)</td><td>0.86 (n/a)</td><td>0.48 (n/a)</td><td>606.80 (n/a)</td><td>440.12 (n/a)</td><td>491.20 (n/a)</td><td>267.30 (n/a)</td><td>145.41 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>2.58 (-3.22%)</td><td>1.76 (-17.67%)</td><td>1.85 <b>(-28.23%)</b></td><td>0.31 <b>(-45.00%)</b></td><td>0.90 (+1.26%)</td><td>3375.40 <b>(+81.82%)</b></td><td>1086.02 <b>(+54.12%)</b></td><td>566.60 <b>(+39.32%)</b></td><td>406.80 (+3.33%)</td><td>1283.72 <b>(+99.18%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>2.66 (n/a)</td><td>2.13 (n/a)</td><td>2.58 (n/a)</td><td>0.56 (n/a)</td><td>0.89 (n/a)</td><td>1856.50 (n/a)</td><td>704.64 (n/a)</td><td>406.70 (n/a)</td><td>393.70 (n/a)</td><td>644.51 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>3.13 <b>(-22.92%)</b></td><td>1.95 <b>(-26.86%)</b></td><td>1.91 <b>(-28.27%)</b></td><td>0.57 (-15.17%)</td><td>0.98 <b>(-26.23%)</b></td><td>3652.70 (+17.88%)</td><td>1517.44 <b>(+28.52%)</b></td><td>1099.60 <b>(+39.42%)</b></td><td>670.30 <b>(+29.73%)</b></td><td>1222.17 (+12.67%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>4.06 (n/a)</td><td>2.66 (n/a)</td><td>2.66 (n/a)</td><td>0.68 (n/a)</td><td>1.33 (n/a)</td><td>3098.60 (n/a)</td><td>1180.74 (n/a)</td><td>788.70 (n/a)</td><td>516.70 (n/a)</td><td>1084.76 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>1.23 <b>(-39.23%)</b></td><td>1.01 <b>(-35.36%)</b></td><td>0.96 <b>(-40.21%)</b></td><td>0.78 <b>(-23.19%)</b></td><td>0.18 <b>(-53.55%)</b></td><td>667.90 <b>(+30.19%)</b></td><td>532.78 <b>(+50.27%)</b></td><td>544.50 <b>(+67.23%)</b></td><td>424.70 <b>(+64.55%)</b></td><td>94.48 (-3.74%)</td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>2.03 (n/a)</td><td>1.56 (n/a)</td><td>1.61 (n/a)</td><td>1.02 (n/a)</td><td>0.38 (n/a)</td><td>513.00 (n/a)</td><td>354.56 (n/a)</td><td>325.60 (n/a)</td><td>258.10 (n/a)</td><td>98.15 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.14 (+2.37%)</td><td>0.09 <b>(-28.40%)</b></td><td>0.13 (+0.46%)</td><td>0.02 <b>(-86.73%)</b></td><td>0.06 <b>(+1320.12%)</b></td><td>1973.40 <b>(+653.78%)</b></td><td>674.78 <b>(+170.84%)</b></td><td>247.20 (-0.48%)</td><td>236.30 (-2.36%)</td><td>749.66 <b>(+9491.45%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>261.80 (n/a)</td><td>249.14 (n/a)</td><td>248.40 (n/a)</td><td>242.00 (n/a)</td><td>7.82 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.13 (-4.50%)</td><td>0.11 (-8.75%)</td><td>0.12 (+3.92%)</td><td>0.05 <b>(-38.90%)</b></td><td>0.03 <b>(+55.35%)</b></td><td>605.00 <b>(+63.65%)</b></td><td>343.98 (+18.46%)</td><td>283.50 (-3.80%)</td><td>251.50 (+4.70%)</td><td>147.69 <b>(+184.12%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>369.70 (n/a)</td><td>290.38 (n/a)</td><td>294.70 (n/a)</td><td>240.20 (n/a)</td><td>51.98 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.23 (-17.48%)</td><td>0.16 <b>(-29.98%)</b></td><td>0.11 <b>(-50.47%)</b></td><td>0.11 <b>(-22.23%)</b></td><td>0.06 (+13.58%)</td><td>602.90 <b>(+28.58%)</b></td><td>470.14 <b>(+50.77%)</b></td><td>571.20 <b>(+101.91%)</b></td><td>290.20 <b>(+21.17%)</b></td><td>160.49 <b>(+72.43%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>468.90 (n/a)</td><td>311.82 (n/a)</td><td>282.90 (n/a)</td><td>239.50 (n/a)</td><td>93.08 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.19 <b>(-34.39%)</b></td><td>0.14 <b>(-37.17%)</b></td><td>0.13 <b>(-38.46%)</b></td><td>0.11 (-2.82%)</td><td>0.03 <b>(-53.42%)</b></td><td>599.00 (+2.92%)</td><td>489.34 <b>(+47.76%)</b></td><td>490.10 <b>(+62.50%)</b></td><td>340.50 <b>(+52.42%)</b></td><td>97.71 <b>(-32.37%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>582.00 (n/a)</td><td>331.18 (n/a)</td><td>301.60 (n/a)</td><td>223.40 (n/a)</td><td>144.48 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.29 (+6.03%)</td><td>0.21 (+9.62%)</td><td>0.20 (+9.95%)</td><td>0.14 <b>(+22.21%)</b></td><td>0.07 (-4.28%)</td><td>478.40 (-18.17%)</td><td>350.94 (-11.82%)</td><td>320.60 (-9.05%)</td><td>225.00 (-5.70%)</td><td>121.27 <b>(-24.25%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>584.60 (n/a)</td><td>397.98 (n/a)</td><td>352.50 (n/a)</td><td>238.60 (n/a)</td><td>160.08 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.46 (-8.79%)</td><td>0.25 <b>(-32.68%)</b></td><td>0.26 <b>(-42.67%)</b></td><td>0.07 <b>(-67.73%)</b></td><td>0.14 (-0.22%)</td><td>1876.50 <b>(+209.86%)</b></td><td>761.28 <b>(+88.33%)</b></td><td>513.80 <b>(+74.41%)</b></td><td>282.70 (+9.66%)</td><td>635.74 <b>(+262.50%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.44 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>605.60 (n/a)</td><td>404.22 (n/a)</td><td>294.60 (n/a)</td><td>257.80 (n/a)</td><td>175.38 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.56 (+16.32%)</td><td>0.40 (+11.08%)</td><td>0.43 (+1.18%)</td><td>0.27 <b>(+22.56%)</b></td><td>0.12 (-3.50%)</td><td>482.40 (-18.40%)</td><td>352.34 (-13.20%)</td><td>305.90 (-1.16%)</td><td>235.70 (-14.01%)</td><td>106.80 <b>(-31.35%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.48 (n/a)</td><td>0.36 (n/a)</td><td>0.42 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>591.20 (n/a)</td><td>405.94 (n/a)</td><td>309.50 (n/a)</td><td>274.10 (n/a)</td><td>155.57 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.54 (+7.45%)</td><td>0.35 (+1.54%)</td><td>0.32 (+9.30%)</td><td>0.22 (-8.33%)</td><td>0.13 (+19.70%)</td><td>600.50 (+9.08%)</td><td>418.16 (+1.77%)</td><td>407.50 (-8.49%)</td><td>240.60 (-6.96%)</td><td>146.04 <b>(+24.06%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.51 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>550.50 (n/a)</td><td>410.90 (n/a)</td><td>445.30 (n/a)</td><td>258.60 (n/a)</td><td>117.72 (n/a)</td>
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
<td><code>826c238</code> — 2026-07-28 16:25:47</td><td>0.07 (-4.83%)</td><td>0.06 <b>(+36.20%)</b></td><td>0.07 <b>(+103.18%)</b></td><td>0.04 <b>(+43.02%)</b></td><td>0.01 <b>(-39.26%)</b></td><td>406.20 <b>(-30.09%)</b></td><td>283.18 <b>(-33.54%)</b></td><td>247.80 <b>(-50.78%)</b></td><td>236.90 (+5.10%)</td><td>71.08 <b>(-55.23%)</b></td>
</tr>
<tr>
<td><code>dac2841</code> — 2026-07-24 20:57:54</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>581.00 (n/a)</td><td>426.06 (n/a)</td><td>503.50 (n/a)</td><td>225.40 (n/a)</td><td>158.77 (n/a)</td>
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
