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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 <b>(+25.02%)</b></td><td>0.02 <b>(+96.05%)</b></td><td>0.03 <b>(+154.94%)</b></td><td>0.02 <b>(+107.73%)</b></td><td>0.00 <b>(-32.05%)</b></td><td>344.50 <b>(-51.86%)</b></td><td>263.30 <b>(-52.76%)</b></td><td>243.80 <b>(-60.77%)</b></td><td>236.00 <b>(-20.00%)</b></td><td>45.64 <b>(-71.52%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>715.60 (n/a)</td><td>557.32 (n/a)</td><td>621.50 (n/a)</td><td>295.00 (n/a)</td><td>160.24 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (+14.32%)</td><td>0.02 (+5.81%)</td><td>0.02 (-9.81%)</td><td>0.01 (-9.69%)</td><td>0.01 <b>(+59.43%)</b></td><td>481.50 (+10.72%)</td><td>341.40 (-1.16%)</td><td>345.60 (+10.88%)</td><td>233.30 (-12.52%)</td><td>107.86 <b>(+41.80%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>434.90 (n/a)</td><td>345.42 (n/a)</td><td>311.70 (n/a)</td><td>266.70 (n/a)</td><td>76.07 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (-0.01%)</td><td>0.02 (+16.77%)</td><td>0.03 <b>(+98.53%)</b></td><td>0.01 <b>(-46.45%)</b></td><td>0.01 <b>(+31.25%)</b></td><td>1071.40 <b>(+86.75%)</b></td><td>439.88 (+6.18%)</td><td>245.40 <b>(-49.62%)</b></td><td>230.60 (+0.00%)</td><td>360.38 <b>(+147.81%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>573.70 (n/a)</td><td>414.26 (n/a)</td><td>487.10 (n/a)</td><td>230.60 (n/a)</td><td>145.43 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (+17.72%)</td><td>0.02 <b>(+42.47%)</b></td><td>0.02 <b>(+52.63%)</b></td><td>0.01 <b>(+148.24%)</b></td><td>0.00 <b>(-33.62%)</b></td><td>419.30 <b>(-59.72%)</b></td><td>319.46 <b>(-42.30%)</b></td><td>335.40 <b>(-34.49%)</b></td><td>240.00 (-15.04%)</td><td>74.93 <b>(-76.08%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1040.90 (n/a)</td><td>553.64 (n/a)</td><td>512.00 (n/a)</td><td>282.50 (n/a)</td><td>313.24 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (+7.67%)</td><td>0.02 (+5.17%)</td><td>0.01 (+5.84%)</td><td>0.01 (+13.07%)</td><td>0.01 (+0.86%)</td><td>534.10 (-11.54%)</td><td>400.48 (-6.36%)</td><td>465.40 (-5.52%)</td><td>224.90 (-7.14%)</td><td>152.83 (-11.27%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.80 (n/a)</td><td>427.68 (n/a)</td><td>492.60 (n/a)</td><td>242.20 (n/a)</td><td>172.24 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (-9.09%)</td><td>0.02 (-10.55%)</td><td>0.01 <b>(-35.03%)</b></td><td>0.01 <b>(+45.19%)</b></td><td>0.01 <b>(-28.48%)</b></td><td>546.20 <b>(-31.12%)</b></td><td>419.88 (-1.54%)</td><td>502.70 <b>(+53.92%)</b></td><td>247.80 (+10.04%)</td><td>137.60 <b>(-43.24%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>793.00 (n/a)</td><td>426.46 (n/a)</td><td>326.60 (n/a)</td><td>225.20 (n/a)</td><td>242.41 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (+12.96%)</td><td>0.05 (+18.96%)</td><td>0.05 <b>(+32.25%)</b></td><td>0.03 <b>(+37.66%)</b></td><td>0.01 (+3.02%)</td><td>391.00 <b>(-27.35%)</b></td><td>281.68 (-18.18%)</td><td>228.40 <b>(-24.40%)</b></td><td>203.40 (-11.49%)</td><td>88.54 <b>(-31.20%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.20 (n/a)</td><td>344.26 (n/a)</td><td>302.10 (n/a)</td><td>229.80 (n/a)</td><td>128.69 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (-16.92%)</td><td>0.03 <b>(-29.98%)</b></td><td>0.03 <b>(-34.85%)</b></td><td>0.02 <b>(-38.00%)</b></td><td>0.01 (+7.88%)</td><td>615.10 <b>(+61.27%)</b></td><td>420.62 <b>(+48.25%)</b></td><td>416.40 <b>(+53.48%)</b></td><td>279.10 <b>(+20.35%)</b></td><td>126.66 <b>(+110.14%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>381.40 (n/a)</td><td>283.72 (n/a)</td><td>271.30 (n/a)</td><td>231.90 (n/a)</td><td>60.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 <b>(+138.56%)</b></td><td>0.04 <b>(+85.53%)</b></td><td>0.05 <b>(+96.52%)</b></td><td>0.01 <b>(-67.59%)</b></td><td>0.02 <b>(+942.20%)</b></td><td>1863.90 <b>(+208.54%)</b></td><td>570.52 (+5.44%)</td><td>272.20 <b>(-49.11%)</b></td><td>197.40 <b>(-58.07%)</b></td><td>724.41 <b>(+1392.20%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>604.10 (n/a)</td><td>541.06 (n/a)</td><td>534.90 (n/a)</td><td>470.80 (n/a)</td><td>48.55 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (-4.17%)</td><td>0.04 (-4.01%)</td><td>0.04 (+2.15%)</td><td>0.02 (+8.09%)</td><td>0.01 (-1.02%)</td><td>502.10 (-7.48%)</td><td>352.72 (+4.19%)</td><td>290.30 (-2.12%)</td><td>237.60 (+4.35%)</td><td>126.99 (-1.05%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.70 (n/a)</td><td>338.54 (n/a)</td><td>296.60 (n/a)</td><td>227.70 (n/a)</td><td>128.33 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (-4.07%)</td><td>0.04 (+10.57%)</td><td>0.04 <b>(+24.12%)</b></td><td>0.02 <b>(+254.95%)</b></td><td>0.01 <b>(-31.02%)</b></td><td>527.40 <b>(-71.83%)</b></td><td>366.78 <b>(-42.30%)</b></td><td>285.70 (-19.43%)</td><td>241.10 (+4.24%)</td><td>139.95 <b>(-79.93%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1872.00 (n/a)</td><td>635.70 (n/a)</td><td>354.60 (n/a)</td><td>231.30 (n/a)</td><td>697.40 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 <b>(-46.05%)</b></td><td>0.02 <b>(-35.16%)</b></td><td>0.02 <b>(-48.40%)</b></td><td>0.02 (-6.56%)</td><td>0.00 <b>(-67.98%)</b></td><td>644.50 (+7.01%)</td><td>556.06 <b>(+40.50%)</b></td><td>611.70 <b>(+93.82%)</b></td><td>443.70 <b>(+85.34%)</b></td><td>93.98 <b>(-39.30%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>602.30 (n/a)</td><td>395.78 (n/a)</td><td>315.60 (n/a)</td><td>239.40 (n/a)</td><td>154.81 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (+16.79%)</td><td>0.09 <b>(+21.27%)</b></td><td>0.09 (+9.39%)</td><td>0.06 (+16.75%)</td><td>0.02 (+12.60%)</td><td>406.80 (-14.34%)</td><td>287.44 (-18.43%)</td><td>264.60 (-8.60%)</td><td>214.50 (-14.37%)</td><td>82.89 <b>(-24.11%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>474.90 (n/a)</td><td>352.38 (n/a)</td><td>289.50 (n/a)</td><td>250.50 (n/a)</td><td>109.23 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (-18.95%)</td><td>0.07 (-5.29%)</td><td>0.08 <b>(+37.80%)</b></td><td>0.04 (-5.78%)</td><td>0.02 <b>(-28.99%)</b></td><td>577.20 (+6.14%)</td><td>385.48 (+1.87%)</td><td>308.60 <b>(-27.44%)</b></td><td>275.50 <b>(+23.38%)</b></td><td>132.25 (-3.63%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>543.80 (n/a)</td><td>378.40 (n/a)</td><td>425.30 (n/a)</td><td>223.30 (n/a)</td><td>137.23 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 <b>(+36.58%)</b></td><td>0.07 <b>(+33.14%)</b></td><td>0.06 <b>(+20.68%)</b></td><td>0.05 (+14.35%)</td><td>0.04 <b>(+52.31%)</b></td><td>541.00 (-12.54%)</td><td>395.38 <b>(-20.82%)</b></td><td>439.70 (-17.15%)</td><td>186.10 <b>(-26.76%)</b></td><td>149.53 (+3.97%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>618.60 (n/a)</td><td>499.36 (n/a)</td><td>530.70 (n/a)</td><td>254.10 (n/a)</td><td>143.82 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (-15.99%)</td><td>0.06 (-6.39%)</td><td>0.05 <b>(-20.31%)</b></td><td>0.05 <b>(+262.92%)</b></td><td>0.03 <b>(-38.29%)</b></td><td>535.50 <b>(-72.44%)</b></td><td>437.72 <b>(-34.81%)</b></td><td>504.90 <b>(+25.47%)</b></td><td>224.00 (+19.02%)</td><td>128.91 <b>(-82.14%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1943.30 (n/a)</td><td>671.48 (n/a)</td><td>402.40 (n/a)</td><td>188.20 (n/a)</td><td>721.77 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.10 (+9.04%)</td><td>0.08 (-2.66%)</td><td>0.09 (+7.34%)</td><td>0.04 (-10.32%)</td><td>0.03 <b>(+45.76%)</b></td><td>596.10 (+11.50%)</td><td>369.18 (+8.95%)</td><td>270.80 (-6.85%)</td><td>249.80 (-8.30%)</td><td>153.50 <b>(+39.39%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>534.60 (n/a)</td><td>338.86 (n/a)</td><td>290.70 (n/a)</td><td>272.40 (n/a)</td><td>110.12 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 <b>(+31.29%)</b></td><td>0.06 (-4.59%)</td><td>0.05 (-8.71%)</td><td>0.04 (-18.01%)</td><td>0.04 <b>(+60.08%)</b></td><td>630.60 <b>(+21.97%)</b></td><td>467.52 (+15.36%)</td><td>510.80 (+9.54%)</td><td>192.60 <b>(-23.81%)</b></td><td>175.83 <b>(+41.49%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>517.00 (n/a)</td><td>405.28 (n/a)</td><td>466.30 (n/a)</td><td>252.80 (n/a)</td><td>124.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.21 (-12.52%)</td><td>0.13 (-14.31%)</td><td>0.10 (-7.18%)</td><td>0.08 (-17.47%)</td><td>0.06 <b>(-21.16%)</b></td><td>632.90 <b>(+21.18%)</b></td><td>429.82 (+13.88%)</td><td>476.10 (+7.71%)</td><td>235.20 (+14.34%)</td><td>163.78 (+8.21%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>522.30 (n/a)</td><td>377.42 (n/a)</td><td>442.00 (n/a)</td><td>205.70 (n/a)</td><td>151.35 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.26 (+9.73%)</td><td>0.18 <b>(+45.95%)</b></td><td>0.17 <b>(+84.55%)</b></td><td>0.10 (+11.57%)</td><td>0.06 (-6.08%)</td><td>510.90 (-10.37%)</td><td>303.62 <b>(-33.56%)</b></td><td>283.30 <b>(-45.81%)</b></td><td>189.50 (-8.89%)</td><td>123.26 (-15.19%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>570.00 (n/a)</td><td>456.98 (n/a)</td><td>522.80 (n/a)</td><td>208.00 (n/a)</td><td>145.33 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.25 <b>(+23.48%)</b></td><td>0.18 <b>(+56.69%)</b></td><td>0.17 <b>(+66.21%)</b></td><td>0.10 <b>(+410.02%)</b></td><td>0.06 (-15.91%)</td><td>487.70 <b>(-80.39%)</b></td><td>296.62 <b>(-63.46%)</b></td><td>296.90 <b>(-39.83%)</b></td><td>198.00 (-19.02%)</td><td>117.65 <b>(-87.57%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>2487.40 (n/a)</td><td>811.72 (n/a)</td><td>493.40 (n/a)</td><td>244.50 (n/a)</td><td>946.76 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.20 (-17.32%)</td><td>0.15 (-0.18%)</td><td>0.16 (+17.94%)</td><td>0.10 (-8.57%)</td><td>0.04 <b>(-29.62%)</b></td><td>497.60 (+9.39%)</td><td>342.70 (-2.64%)</td><td>302.60 (-15.19%)</td><td>242.80 <b>(+20.92%)</b></td><td>99.05 (-5.57%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>454.90 (n/a)</td><td>352.00 (n/a)</td><td>356.80 (n/a)</td><td>200.80 (n/a)</td><td>104.89 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.22 <b>(+51.26%)</b></td><td>0.17 <b>(+53.41%)</b></td><td>0.18 <b>(+79.57%)</b></td><td>0.09 (+3.62%)</td><td>0.06 <b>(+125.12%)</b></td><td>545.10 (-3.49%)</td><td>330.38 <b>(-29.50%)</b></td><td>276.20 <b>(-44.30%)</b></td><td>220.70 <b>(-33.88%)</b></td><td>137.74 <b>(+36.50%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>564.80 (n/a)</td><td>468.64 (n/a)</td><td>495.90 (n/a)</td><td>333.80 (n/a)</td><td>100.91 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.23 <b>(+64.50%)</b></td><td>0.18 <b>(+78.48%)</b></td><td>0.18 <b>(+86.08%)</b></td><td>0.15 <b>(+71.60%)</b></td><td>0.03 <b>(+47.36%)</b></td><td>336.90 <b>(-41.72%)</b></td><td>272.80 <b>(-44.28%)</b></td><td>274.10 <b>(-46.25%)</b></td><td>214.60 <b>(-39.21%)</b></td><td>45.08 <b>(-45.58%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>578.10 (n/a)</td><td>489.56 (n/a)</td><td>510.00 (n/a)</td><td>353.00 (n/a)</td><td>82.83 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (+4.40%)</td><td>0.01 <b>(+24.24%)</b></td><td>0.01 (+14.30%)</td><td>0.01 <b>(+123.84%)</b></td><td>0.00 <b>(-64.07%)</b></td><td>266.60 <b>(-55.32%)</b></td><td>248.76 <b>(-27.13%)</b></td><td>255.50 (-12.50%)</td><td>218.10 (-4.22%)</td><td>20.70 <b>(-85.80%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>596.70 (n/a)</td><td>341.38 (n/a)</td><td>292.00 (n/a)</td><td>227.70 (n/a)</td><td>145.75 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (+6.08%)</td><td>0.01 (+19.60%)</td><td>0.01 <b>(+62.90%)</b></td><td>0.01 (+18.76%)</td><td>0.00 (-8.99%)</td><td>485.50 (-15.78%)</td><td>340.64 (-19.24%)</td><td>290.70 <b>(-38.62%)</b></td><td>233.20 (-5.74%)</td><td>108.99 <b>(-25.25%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>576.50 (n/a)</td><td>421.80 (n/a)</td><td>473.60 (n/a)</td><td>247.40 (n/a)</td><td>145.81 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (+12.88%)</td><td>0.01 (+12.43%)</td><td>0.01 (+7.00%)</td><td>0.00 (-8.85%)</td><td>0.00 <b>(+31.86%)</b></td><td>617.10 (+9.71%)</td><td>391.26 (-5.54%)</td><td>410.60 (-6.53%)</td><td>204.80 (-11.42%)</td><td>173.92 (+19.44%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>562.50 (n/a)</td><td>414.20 (n/a)</td><td>439.30 (n/a)</td><td>231.20 (n/a)</td><td>145.61 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 <b>(+23.69%)</b></td><td>0.01 (+15.19%)</td><td>0.01 (+18.54%)</td><td>0.00 (+8.96%)</td><td>0.00 <b>(+21.55%)</b></td><td>539.70 (-8.21%)</td><td>375.86 (-13.16%)</td><td>405.00 (-15.64%)</td><td>193.60 (-19.16%)</td><td>128.13 (-15.03%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>588.00 (n/a)</td><td>432.84 (n/a)</td><td>480.10 (n/a)</td><td>239.50 (n/a)</td><td>150.80 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 <b>(+75.04%)</b></td><td>0.01 <b>(+78.61%)</b></td><td>0.01 <b>(+101.09%)</b></td><td>0.00 <b>(+77.53%)</b></td><td>0.00 <b>(+113.20%)</b></td><td>556.80 <b>(-43.67%)</b></td><td>354.04 <b>(-40.65%)</b></td><td>254.60 <b>(-50.27%)</b></td><td>202.90 <b>(-42.86%)</b></td><td>167.70 <b>(-29.93%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>988.40 (n/a)</td><td>596.50 (n/a)</td><td>512.00 (n/a)</td><td>355.10 (n/a)</td><td>239.34 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 <b>(-20.31%)</b></td><td>0.01 (-10.77%)</td><td>0.01 (-5.63%)</td><td>0.00 (-12.06%)</td><td>0.00 <b>(-32.13%)</b></td><td>624.00 (+13.70%)</td><td>497.32 (+9.28%)</td><td>507.70 (+5.97%)</td><td>321.30 <b>(+25.51%)</b></td><td>112.85 (-1.86%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>548.80 (n/a)</td><td>455.10 (n/a)</td><td>479.10 (n/a)</td><td>256.00 (n/a)</td><td>114.99 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(-22.64%)</b></td><td>0.01 (-6.30%)</td><td>0.02 (+7.25%)</td><td>0.01 (+18.92%)</td><td>0.00 <b>(-58.11%)</b></td><td>412.00 (-15.92%)</td><td>355.74 (+1.25%)</td><td>343.50 (-6.76%)</td><td>293.90 <b>(+29.30%)</b></td><td>45.64 <b>(-53.65%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>490.00 (n/a)</td><td>351.36 (n/a)</td><td>368.40 (n/a)</td><td>227.30 (n/a)</td><td>98.47 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(-25.73%)</b></td><td>0.01 (-1.23%)</td><td>0.01 (+18.64%)</td><td>0.01 (-8.30%)</td><td>0.01 <b>(-37.93%)</b></td><td>613.40 (+9.05%)</td><td>421.06 (-7.17%)</td><td>422.10 (-15.70%)</td><td>223.40 <b>(+34.66%)</b></td><td>156.39 (-5.13%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.50 (n/a)</td><td>453.58 (n/a)</td><td>500.70 (n/a)</td><td>165.90 (n/a)</td><td>164.84 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (-6.38%)</td><td>0.02 (+9.68%)</td><td>0.02 <b>(+57.63%)</b></td><td>0.01 (+4.46%)</td><td>0.00 (-11.93%)</td><td>470.40 (-4.27%)</td><td>345.76 (-10.49%)</td><td>290.90 <b>(-36.57%)</b></td><td>245.40 (+6.79%)</td><td>111.57 (-8.87%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>491.40 (n/a)</td><td>386.28 (n/a)</td><td>458.60 (n/a)</td><td>229.80 (n/a)</td><td>122.43 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (-3.11%)</td><td>0.01 <b>(-29.11%)</b></td><td>0.01 <b>(-42.81%)</b></td><td>0.01 <b>(-25.50%)</b></td><td>0.01 <b>(+28.01%)</b></td><td>584.60 <b>(+34.24%)</b></td><td>459.90 <b>(+50.00%)</b></td><td>539.50 <b>(+74.88%)</b></td><td>242.60 (+3.23%)</td><td>146.23 <b>(+81.56%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>435.50 (n/a)</td><td>306.60 (n/a)</td><td>308.50 (n/a)</td><td>235.00 (n/a)</td><td>80.54 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(+58.35%)</b></td><td>0.01 <b>(+57.75%)</b></td><td>0.02 <b>(+50.09%)</b></td><td>0.01 <b>(+314.38%)</b></td><td>0.00 (+5.90%)</td><td>574.90 <b>(-75.87%)</b></td><td>400.90 <b>(-54.05%)</b></td><td>339.70 <b>(-33.38%)</b></td><td>291.20 <b>(-36.85%)</b></td><td>127.07 <b>(-84.95%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2382.40 (n/a)</td><td>872.46 (n/a)</td><td>509.90 (n/a)</td><td>461.10 (n/a)</td><td>844.35 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(+42.97%)</b></td><td>0.02 <b>(+33.00%)</b></td><td>0.02 <b>(+38.98%)</b></td><td>0.01 (-4.87%)</td><td>0.00 <b>(+194.40%)</b></td><td>563.20 (+5.11%)</td><td>365.56 (-18.91%)</td><td>327.50 <b>(-28.05%)</b></td><td>254.40 <b>(-30.07%)</b></td><td>130.07 <b>(+111.81%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>535.80 (n/a)</td><td>450.78 (n/a)</td><td>455.20 (n/a)</td><td>363.80 (n/a)</td><td>61.41 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (-15.94%)</td><td>0.03 (-12.95%)</td><td>0.03 <b>(-29.86%)</b></td><td>0.02 (+15.22%)</td><td>0.01 <b>(-33.68%)</b></td><td>516.70 (-13.20%)</td><td>369.12 (+4.73%)</td><td>351.90 <b>(+42.59%)</b></td><td>242.90 (+18.95%)</td><td>117.38 <b>(-32.28%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>595.30 (n/a)</td><td>352.46 (n/a)</td><td>246.80 (n/a)</td><td>204.20 (n/a)</td><td>173.33 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (-18.13%)</td><td>0.03 (+15.57%)</td><td>0.03 <b>(+24.61%)</b></td><td>0.02 <b>(+199.07%)</b></td><td>0.01 <b>(-53.99%)</b></td><td>626.10 <b>(-66.56%)</b></td><td>404.30 <b>(-48.28%)</b></td><td>333.40 (-19.74%)</td><td>296.00 <b>(+22.11%)</b></td><td>136.00 <b>(-80.59%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1872.50 (n/a)</td><td>781.72 (n/a)</td><td>415.40 (n/a)</td><td>242.40 (n/a)</td><td>700.78 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (-17.41%)</td><td>0.03 <b>(-23.18%)</b></td><td>0.02 <b>(-33.03%)</b></td><td>0.01 <b>(-64.82%)</b></td><td>0.01 (+16.30%)</td><td>1933.50 <b>(+184.21%)</b></td><td>682.06 <b>(+84.85%)</b></td><td>444.20 <b>(+49.31%)</b></td><td>283.00 <b>(+21.04%)</b></td><td>704.38 <b>(+293.07%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>680.30 (n/a)</td><td>368.98 (n/a)</td><td>297.50 (n/a)</td><td>233.80 (n/a)</td><td>179.20 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 <b>(+41.81%)</b></td><td>0.03 (+4.26%)</td><td>0.02 (+0.35%)</td><td>0.02 (-4.72%)</td><td>0.01 <b>(+75.26%)</b></td><td>523.40 (+4.95%)</td><td>420.60 (+1.43%)</td><td>472.10 (-0.34%)</td><td>212.70 <b>(-29.50%)</b></td><td>123.51 <b>(+24.38%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.70 (n/a)</td><td>414.68 (n/a)</td><td>473.70 (n/a)</td><td>301.70 (n/a)</td><td>99.30 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (-17.27%)</td><td>0.02 (+13.23%)</td><td>0.02 (+13.45%)</td><td>0.02 <b>(+111.73%)</b></td><td>0.00 <b>(-69.42%)</b></td><td>479.70 <b>(-52.77%)</b></td><td>437.38 <b>(-23.37%)</b></td><td>453.90 (-11.85%)</td><td>364.30 <b>(+20.91%)</b></td><td>43.93 <b>(-83.53%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1015.70 (n/a)</td><td>570.80 (n/a)</td><td>514.90 (n/a)</td><td>301.30 (n/a)</td><td>266.71 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (+8.50%)</td><td>0.02 (-0.04%)</td><td>0.02 (+6.70%)</td><td>0.02 (-18.75%)</td><td>0.01 <b>(+67.63%)</b></td><td>676.10 <b>(+23.08%)</b></td><td>522.16 (+3.25%)</td><td>489.30 (-6.28%)</td><td>364.90 (-7.85%)</td><td>122.54 <b>(+95.64%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>549.30 (n/a)</td><td>505.70 (n/a)</td><td>522.10 (n/a)</td><td>396.00 (n/a)</td><td>62.63 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (+7.09%)</td><td>0.07 <b>(+24.09%)</b></td><td>0.08 <b>(+24.69%)</b></td><td>0.04 (+14.71%)</td><td>0.02 (-1.75%)</td><td>521.30 (-12.83%)</td><td>315.66 <b>(-21.05%)</b></td><td>260.60 (-19.82%)</td><td>245.80 (-6.61%)</td><td>117.12 <b>(-20.15%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>598.00 (n/a)</td><td>399.84 (n/a)</td><td>325.00 (n/a)</td><td>263.20 (n/a)</td><td>146.68 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (+5.26%)</td><td>0.05 (-18.04%)</td><td>0.04 (-13.29%)</td><td>0.02 <b>(-51.58%)</b></td><td>0.02 <b>(+50.82%)</b></td><td>955.90 <b>(+106.50%)</b></td><td>541.56 <b>(+40.74%)</b></td><td>486.40 (+15.32%)</td><td>236.90 (-4.97%)</td><td>262.45 <b>(+184.46%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>462.90 (n/a)</td><td>384.80 (n/a)</td><td>421.80 (n/a)</td><td>249.30 (n/a)</td><td>92.26 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 <b>(+22.51%)</b></td><td>0.09 <b>(+23.19%)</b></td><td>0.09 (+2.56%)</td><td>0.07 <b>(+94.30%)</b></td><td>0.02 <b>(-33.82%)</b></td><td>300.10 <b>(-48.54%)</b></td><td>242.84 <b>(-26.71%)</b></td><td>245.30 (-2.50%)</td><td>185.60 (-18.35%)</td><td>42.04 <b>(-72.13%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>583.20 (n/a)</td><td>331.32 (n/a)</td><td>251.60 (n/a)</td><td>227.30 (n/a)</td><td>150.82 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (-6.12%)</td><td>0.06 (+14.19%)</td><td>0.06 <b>(+50.25%)</b></td><td>0.04 (+7.14%)</td><td>0.02 <b>(-22.80%)</b></td><td>554.20 (-6.67%)</td><td>378.58 (-16.53%)</td><td>352.20 <b>(-33.43%)</b></td><td>279.40 (+6.52%)</td><td>113.87 <b>(-26.39%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>593.80 (n/a)</td><td>453.54 (n/a)</td><td>529.10 (n/a)</td><td>262.30 (n/a)</td><td>154.69 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 <b>(-34.94%)</b></td><td>0.05 (+1.61%)</td><td>0.05 (+9.38%)</td><td>0.04 <b>(+238.31%)</b></td><td>0.01 <b>(-70.07%)</b></td><td>571.50 <b>(-70.44%)</b></td><td>473.34 <b>(-35.65%)</b></td><td>457.10 (-8.56%)</td><td>372.50 <b>(+53.74%)</b></td><td>83.79 <b>(-87.67%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1933.50 (n/a)</td><td>735.56 (n/a)</td><td>499.90 (n/a)</td><td>242.30 (n/a)</td><td>679.62 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (+2.96%)</td><td>0.06 <b>(+30.56%)</b></td><td>0.06 <b>(+30.92%)</b></td><td>0.05 <b>(+324.79%)</b></td><td>0.01 <b>(-51.17%)</b></td><td>458.30 <b>(-76.46%)</b></td><td>368.34 <b>(-48.99%)</b></td><td>372.80 <b>(-23.62%)</b></td><td>274.40 (-2.90%)</td><td>66.92 <b>(-90.32%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1947.00 (n/a)</td><td>722.14 (n/a)</td><td>488.10 (n/a)</td><td>282.60 (n/a)</td><td>691.00 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.60 (n/a)</td><td>375.96 (n/a)</td><td>297.30 (n/a)</td><td>221.40 (n/a)</td><td>174.35 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.30 (n/a)</td><td>439.46 (n/a)</td><td>522.80 (n/a)</td><td>217.50 (n/a)</td><td>183.17 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>653.30 (n/a)</td><td>436.48 (n/a)</td><td>492.60 (n/a)</td><td>195.30 (n/a)</td><td>192.52 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>519.10 (n/a)</td><td>444.52 (n/a)</td><td>441.40 (n/a)</td><td>350.70 (n/a)</td><td>70.91 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>548.00 (n/a)</td><td>398.54 (n/a)</td><td>411.10 (n/a)</td><td>218.50 (n/a)</td><td>119.05 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>552.10 (n/a)</td><td>412.56 (n/a)</td><td>438.20 (n/a)</td><td>208.30 (n/a)</td><td>125.87 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>534.80 (n/a)</td><td>379.06 (n/a)</td><td>344.60 (n/a)</td><td>240.50 (n/a)</td><td>135.86 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2395.60 (n/a)</td><td>751.48 (n/a)</td><td>358.30 (n/a)</td><td>219.50 (n/a)</td><td>927.16 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>591.80 (n/a)</td><td>394.78 (n/a)</td><td>348.50 (n/a)</td><td>274.00 (n/a)</td><td>124.39 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.18 (+2.43%)</td><td>0.13 (-3.75%)</td><td>0.12 (-4.63%)</td><td>0.08 (-16.42%)</td><td>0.05 <b>(+35.61%)</b></td><td>631.70 (+19.66%)</td><td>433.74 (+10.60%)</td><td>409.30 (+4.84%)</td><td>273.70 (-2.39%)</td><td>166.33 <b>(+56.89%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>527.90 (n/a)</td><td>392.16 (n/a)</td><td>390.40 (n/a)</td><td>280.40 (n/a)</td><td>106.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>581.20 (n/a)</td><td>403.46 (n/a)</td><td>367.70 (n/a)</td><td>236.10 (n/a)</td><td>159.97 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>585.90 (n/a)</td><td>447.88 (n/a)</td><td>421.20 (n/a)</td><td>248.40 (n/a)</td><td>138.39 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>301.10 (n/a)</td><td>266.52 (n/a)</td><td>271.30 (n/a)</td><td>218.00 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.80 (n/a)</td><td>365.52 (n/a)</td><td>268.60 (n/a)</td><td>220.70 (n/a)</td><td>162.67 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>509.60 (n/a)</td><td>430.20 (n/a)</td><td>489.40 (n/a)</td><td>205.50 (n/a)</td><td>127.52 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.00 (n/a)</td><td>378.18 (n/a)</td><td>380.80 (n/a)</td><td>206.10 (n/a)</td><td>130.03 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>558.00 (n/a)</td><td>431.48 (n/a)</td><td>488.60 (n/a)</td><td>266.70 (n/a)</td><td>121.62 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>556.60 (n/a)</td><td>421.66 (n/a)</td><td>444.50 (n/a)</td><td>301.00 (n/a)</td><td>98.71 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1948.10 (n/a)</td><td>732.58 (n/a)</td><td>495.70 (n/a)</td><td>285.00 (n/a)</td><td>686.70 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1919.50 (n/a)</td><td>708.40 (n/a)</td><td>464.70 (n/a)</td><td>247.90 (n/a)</td><td>693.26 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>585.10 (n/a)</td><td>402.30 (n/a)</td><td>353.20 (n/a)</td><td>252.80 (n/a)</td><td>145.25 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>580.90 (n/a)</td><td>378.62 (n/a)</td><td>390.10 (n/a)</td><td>237.50 (n/a)</td><td>146.26 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2015.90 (n/a)</td><td>754.62 (n/a)</td><td>486.30 (n/a)</td><td>320.30 (n/a)</td><td>709.22 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.50 (n/a)</td><td>403.82 (n/a)</td><td>421.90 (n/a)</td><td>295.50 (n/a)</td><td>96.38 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>656.20 (n/a)</td><td>408.52 (n/a)</td><td>396.90 (n/a)</td><td>196.50 (n/a)</td><td>185.52 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.20 (n/a)</td><td>378.62 (n/a)</td><td>263.10 (n/a)</td><td>242.20 (n/a)</td><td>191.14 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>805.10 (n/a)</td><td>430.88 (n/a)</td><td>382.00 (n/a)</td><td>238.30 (n/a)</td><td>230.89 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2006.80 (n/a)</td><td>729.82 (n/a)</td><td>500.70 (n/a)</td><td>250.20 (n/a)</td><td>726.28 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.80 (n/a)</td><td>465.30 (n/a)</td><td>494.10 (n/a)</td><td>216.60 (n/a)</td><td>154.47 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.40 (n/a)</td><td>355.86 (n/a)</td><td>278.40 (n/a)</td><td>238.80 (n/a)</td><td>132.36 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>957.10 (n/a)</td><td>579.70 (n/a)</td><td>527.40 (n/a)</td><td>316.00 (n/a)</td><td>233.83 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.00 (n/a)</td><td>411.50 (n/a)</td><td>384.10 (n/a)</td><td>249.20 (n/a)</td><td>169.89 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.10 (n/a)</td><td>454.12 (n/a)</td><td>495.00 (n/a)</td><td>250.40 (n/a)</td><td>117.22 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.30 (n/a)</td><td>481.44 (n/a)</td><td>533.40 (n/a)</td><td>230.60 (n/a)</td><td>159.52 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>623.10 (n/a)</td><td>530.00 (n/a)</td><td>593.10 (n/a)</td><td>339.00 (n/a)</td><td>117.44 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>487.10 (n/a)</td><td>341.42 (n/a)</td><td>307.50 (n/a)</td><td>283.30 (n/a)</td><td>82.64 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>527.60 (n/a)</td><td>373.28 (n/a)</td><td>303.90 (n/a)</td><td>280.80 (n/a)</td><td>110.46 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>674.00 (n/a)</td><td>479.22 (n/a)</td><td>557.30 (n/a)</td><td>249.20 (n/a)</td><td>189.66 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>681.80 (n/a)</td><td>432.48 (n/a)</td><td>432.40 (n/a)</td><td>234.70 (n/a)</td><td>183.67 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.70 (n/a)</td><td>334.96 (n/a)</td><td>290.50 (n/a)</td><td>277.50 (n/a)</td><td>83.10 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>611.80 (n/a)</td><td>466.04 (n/a)</td><td>438.70 (n/a)</td><td>276.00 (n/a)</td><td>131.87 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>660.30 (n/a)</td><td>435.04 (n/a)</td><td>315.60 (n/a)</td><td>288.70 (n/a)</td><td>179.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>614.70 (n/a)</td><td>501.46 (n/a)</td><td>500.80 (n/a)</td><td>374.80 (n/a)</td><td>93.04 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>767.90 (n/a)</td><td>543.86 (n/a)</td><td>540.70 (n/a)</td><td>288.80 (n/a)</td><td>173.73 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>448.00 (n/a)</td><td>363.40 (n/a)</td><td>343.00 (n/a)</td><td>268.70 (n/a)</td><td>76.42 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>547.60 (n/a)</td><td>414.40 (n/a)</td><td>454.60 (n/a)</td><td>222.40 (n/a)</td><td>122.11 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>486.00 (n/a)</td><td>424.06 (n/a)</td><td>462.80 (n/a)</td><td>263.60 (n/a)</td><td>91.67 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.44 <b>(-22.98%)</b></td><td>0.40 (+17.56%)</td><td>0.41 (+15.67%)</td><td>0.36 <b>(+187.05%)</b></td><td>0.03 <b>(-80.21%)</b></td><td>609.80 <b>(-65.17%)</b></td><td>552.76 <b>(-34.22%)</b></td><td>535.50 (-13.55%)</td><td>497.70 <b>(+29.85%)</b></td><td>46.59 <b>(-91.41%)</b></td><td>18.96 <b>(-22.98%)</b></td><td>17.17 (+17.56%)</td><td>17.62 (+15.67%)</td><td>15.47 <b>(+187.05%)</b></td><td>1.44 <b>(-80.21%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.58 (n/a)</td><td>0.34 (n/a)</td><td>0.36 (n/a)</td><td>0.13 (n/a)</td><td>0.17 (n/a)</td><td>1750.60 (n/a)</td><td>840.34 (n/a)</td><td>619.40 (n/a)</td><td>383.30 (n/a)</td><td>542.69 (n/a)</td><td>24.62 (n/a)</td><td>14.61 (n/a)</td><td>15.24 (n/a)</td><td>5.39 (n/a)</td><td>7.25 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.59 (+5.25%)</td><td>0.47 <b>(+20.80%)</b></td><td>0.46 <b>(+21.92%)</b></td><td>0.34 <b>(+53.08%)</b></td><td>0.11 (-10.19%)</td><td>645.50 <b>(-34.68%)</b></td><td>495.66 <b>(-20.63%)</b></td><td>476.20 (-17.98%)</td><td>374.00 (-5.00%)</td><td>117.39 <b>(-46.54%)</b></td><td>25.23 (+5.25%)</td><td>19.90 <b>(+20.80%)</b></td><td>19.82 <b>(+21.92%)</b></td><td>14.62 <b>(+53.08%)</b></td><td>4.61 (-10.19%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>988.20 (n/a)</td><td>624.50 (n/a)</td><td>580.60 (n/a)</td><td>393.70 (n/a)</td><td>219.59 (n/a)</td><td>23.97 (n/a)</td><td>16.48 (n/a)</td><td>16.25 (n/a)</td><td>9.55 (n/a)</td><td>5.13 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.31 (-0.30%)</td><td>0.31 (-0.42%)</td><td>0.31 (-0.64%)</td><td>0.30 (-0.41%)</td><td>0.00 (+10.59%)</td><td>83273.80 (+0.41%)</td><td>82128.88 (+0.42%)</td><td>82142.30 (+0.64%)</td><td>81250.00 (+0.30%)</td><td>855.65 (+11.21%)</td><td>211.44 (-0.30%)</td><td>209.20 (-0.42%)</td><td>209.15 (-0.64%)</td><td>206.31 (-0.41%)</td><td>2.18 (+10.59%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>82936.50 (n/a)</td><td>81784.84 (n/a)</td><td>81616.10 (n/a)</td><td>81004.90 (n/a)</td><td>769.42 (n/a)</td><td>212.08 (n/a)</td><td>210.08 (n/a)</td><td>210.50 (n/a)</td><td>207.14 (n/a)</td><td>1.97 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>1.03 (-2.27%)</td><td>0.99 (-2.32%)</td><td>1.01 (-2.31%)</td><td>0.90 (-3.64%)</td><td>0.05 (+9.85%)</td><td>27900.10 (+3.78%)</td><td>25505.46 (+2.42%)</td><td>24947.40 (+2.37%)</td><td>24505.80 (+2.32%)</td><td>1364.21 (+17.00%)</td><td>701.05 (-2.27%)</td><td>675.03 (-2.32%)</td><td>688.64 (-2.32%)</td><td>615.76 (-3.64%)</td><td>33.93 (+9.85%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>1.05 (n/a)</td><td>1.01 (n/a)</td><td>1.03 (n/a)</td><td>0.94 (n/a)</td><td>0.05 (n/a)</td><td>26885.00 (n/a)</td><td>24902.40 (n/a)</td><td>24369.90 (n/a)</td><td>23950.10 (n/a)</td><td>1165.96 (n/a)</td><td>717.32 (n/a)</td><td>691.04 (n/a)</td><td>704.96 (n/a)</td><td>639.01 (n/a)</td><td>30.88 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.82 (+0.71%)</td><td>0.81 (+1.46%)</td><td>0.81 (+2.02%)</td><td>0.80 (+1.13%)</td><td>0.01 (-19.95%)</td><td>94836.80 (-1.12%)</td><td>93450.38 (-1.44%)</td><td>93471.90 (-1.98%)</td><td>91832.30 (-0.71%)</td><td>1114.15 <b>(-21.42%)</b></td><td>748.31 (+0.71%)</td><td>735.44 (+1.46%)</td><td>735.19 (+2.02%)</td><td>724.61 (+1.13%)</td><td>8.80 (-19.95%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95909.80 (n/a)</td><td>94818.64 (n/a)</td><td>95362.90 (n/a)</td><td>92485.00 (n/a)</td><td>1417.88 (n/a)</td><td>743.03 (n/a)</td><td>724.88 (n/a)</td><td>720.61 (n/a)</td><td>716.50 (n/a)</td><td>10.99 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.78 (+0.09%)</td><td>0.76 (+0.05%)</td><td>0.77 (-0.77%)</td><td>0.74 (+0.34%)</td><td>0.01 (-15.88%)</td><td>101769.50 (-0.34%)</td><td>98877.68 (-0.06%)</td><td>98413.70 (+0.78%)</td><td>97086.50 (-0.09%)</td><td>1854.68 (-15.99%)</td><td>707.82 (+0.09%)</td><td>695.19 (+0.05%)</td><td>698.27 (-0.77%)</td><td>675.25 (+0.34%)</td><td>12.89 (-15.88%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>102118.70 (n/a)</td><td>98938.66 (n/a)</td><td>97655.50 (n/a)</td><td>97169.60 (n/a)</td><td>2207.65 (n/a)</td><td>707.21 (n/a)</td><td>694.84 (n/a)</td><td>703.69 (n/a)</td><td>672.94 (n/a)</td><td>15.32 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.80 (-0.71%)</td><td>0.79 (-0.75%)</td><td>0.79 (+0.03%)</td><td>0.77 (-1.75%)</td><td>0.01 <b>(+42.04%)</b></td><td>98129.60 (+1.79%)</td><td>95997.50 (+0.76%)</td><td>95392.00 (-0.03%)</td><td>94804.10 (+0.71%)</td><td>1305.32 <b>(+45.93%)</b></td><td>724.86 (-0.71%)</td><td>715.95 (-0.75%)</td><td>720.39 (+0.03%)</td><td>700.29 (-1.75%)</td><td>9.63 <b>(+42.04%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96407.90 (n/a)</td><td>95274.10 (n/a)</td><td>95424.80 (n/a)</td><td>94132.00 (n/a)</td><td>894.47 (n/a)</td><td>730.03 (n/a)</td><td>721.33 (n/a)</td><td>720.14 (n/a)</td><td>712.80 (n/a)</td><td>6.78 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.63 (-2.39%)</td><td>4.03 (+16.26%)</td><td>4.09 <b>(+41.89%)</b></td><td>2.20 (+12.11%)</td><td>1.22 (-18.99%)</td><td>4048.60 (-10.80%)</td><td>2429.78 (-17.72%)</td><td>2178.50 <b>(-29.52%)</b></td><td>1582.30 (+2.45%)</td><td>940.70 (-18.59%)</td><td>339.30 (-2.39%)</td><td>242.67 (+16.26%)</td><td>246.44 <b>(+41.89%)</b></td><td>132.61 (+12.11%)</td><td>73.39 (-18.99%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.77 (n/a)</td><td>3.47 (n/a)</td><td>2.88 (n/a)</td><td>1.96 (n/a)</td><td>1.50 (n/a)</td><td>4539.00 (n/a)</td><td>2953.00 (n/a)</td><td>3091.10 (n/a)</td><td>1544.40 (n/a)</td><td>1155.51 (n/a)</td><td>347.62 (n/a)</td><td>208.74 (n/a)</td><td>173.68 (n/a)</td><td>118.28 (n/a)</td><td>90.59 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>4.84 (+5.24%)</td><td>3.69 <b>(+28.80%)</b></td><td>4.65 <b>(+113.55%)</b></td><td>2.07 (-3.04%)</td><td>1.47 <b>(+36.83%)</b></td><td>4304.90 (+3.14%)</td><td>2836.40 (-16.84%)</td><td>1915.30 <b>(-53.17%)</b></td><td>1842.80 (-4.98%)</td><td>1319.65 <b>(+30.29%)</b></td><td>291.34 (+5.24%)</td><td>222.19 <b>(+28.80%)</b></td><td>280.30 <b>(+113.55%)</b></td><td>124.71 (-3.04%)</td><td>88.46 <b>(+36.83%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>4.60 (n/a)</td><td>2.86 (n/a)</td><td>2.18 (n/a)</td><td>2.14 (n/a)</td><td>1.07 (n/a)</td><td>4173.90 (n/a)</td><td>3410.96 (n/a)</td><td>4090.20 (n/a)</td><td>1939.30 (n/a)</td><td>1012.85 (n/a)</td><td>276.84 (n/a)</td><td>172.51 (n/a)</td><td>131.26 (n/a)</td><td>128.63 (n/a)</td><td>64.65 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.31 <b>(+25.23%)</b></td><td>3.65 (+5.18%)</td><td>3.89 (-0.59%)</td><td>1.84 (-14.90%)</td><td>1.27 <b>(+39.80%)</b></td><td>4853.80 (+17.51%)</td><td>2765.62 (+0.69%)</td><td>2289.10 (+0.60%)</td><td>1677.00 <b>(-20.15%)</b></td><td>1233.63 <b>(+41.76%)</b></td><td>320.13 <b>(+25.23%)</b></td><td>220.05 (+5.18%)</td><td>234.54 (-0.59%)</td><td>110.61 (-14.90%)</td><td>76.75 <b>(+39.80%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>4.24 (n/a)</td><td>3.47 (n/a)</td><td>3.92 (n/a)</td><td>2.16 (n/a)</td><td>0.91 (n/a)</td><td>4130.70 (n/a)</td><td>2746.58 (n/a)</td><td>2275.50 (n/a)</td><td>2100.10 (n/a)</td><td>870.21 (n/a)</td><td>255.64 (n/a)</td><td>209.21 (n/a)</td><td>235.93 (n/a)</td><td>129.97 (n/a)</td><td>54.90 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>6.64 (-0.16%)</td><td>5.09 (+0.60%)</td><td>4.82 (-2.65%)</td><td>3.82 (-0.30%)</td><td>1.19 (+15.62%)</td><td>9119.70 (+0.30%)</td><td>7153.54 (+0.53%)</td><td>7238.30 (+2.72%)</td><td>5253.10 (+0.16%)</td><td>1628.19 (+16.73%)</td><td>408.81 (-0.16%)</td><td>313.43 (+0.60%)</td><td>296.68 (-2.65%)</td><td>235.48 (-0.30%)</td><td>73.37 (+15.62%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>6.65 (n/a)</td><td>5.06 (n/a)</td><td>4.95 (n/a)</td><td>3.83 (n/a)</td><td>1.03 (n/a)</td><td>9092.20 (n/a)</td><td>7115.54 (n/a)</td><td>7046.60 (n/a)</td><td>5244.90 (n/a)</td><td>1394.85 (n/a)</td><td>409.44 (n/a)</td><td>311.56 (n/a)</td><td>304.75 (n/a)</td><td>236.19 (n/a)</td><td>63.46 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>6.08 (+3.52%)</td><td>5.14 (-1.75%)</td><td>5.21 (-1.47%)</td><td>3.74 (-19.49%)</td><td>0.95 <b>(+99.87%)</b></td><td>9325.70 <b>(+24.20%)</b></td><td>6999.16 (+4.28%)</td><td>6690.80 (+1.49%)</td><td>5735.50 (-3.40%)</td><td>1452.76 <b>(+138.49%)</b></td><td>374.42 (+3.52%)</td><td>316.43 (-1.75%)</td><td>320.96 (-1.47%)</td><td>230.28 (-19.49%)</td><td>58.46 <b>(+99.87%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.87 (n/a)</td><td>5.23 (n/a)</td><td>5.29 (n/a)</td><td>4.64 (n/a)</td><td>0.47 (n/a)</td><td>7508.50 (n/a)</td><td>6712.18 (n/a)</td><td>6592.60 (n/a)</td><td>5937.30 (n/a)</td><td>609.15 (n/a)</td><td>361.69 (n/a)</td><td>322.05 (n/a)</td><td>325.74 (n/a)</td><td>286.01 (n/a)</td><td>29.25 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.86 (-9.11%)</td><td>5.28 (-8.77%)</td><td>5.44 (-7.56%)</td><td>4.62 (-5.80%)</td><td>0.47 <b>(-22.12%)</b></td><td>7540.50 (+6.16%)</td><td>6652.48 (+9.32%)</td><td>6405.50 (+8.18%)</td><td>5950.20 (+10.02%)</td><td>614.71 (-8.73%)</td><td>360.91 (-9.11%)</td><td>324.96 (-8.77%)</td><td>335.26 (-7.56%)</td><td>284.80 (-5.80%)</td><td>29.23 <b>(-22.12%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>6.45 (n/a)</td><td>5.78 (n/a)</td><td>5.89 (n/a)</td><td>4.91 (n/a)</td><td>0.61 (n/a)</td><td>7103.00 (n/a)</td><td>6085.26 (n/a)</td><td>5921.20 (n/a)</td><td>5408.30 (n/a)</td><td>673.50 (n/a)</td><td>397.07 (n/a)</td><td>356.21 (n/a)</td><td>362.68 (n/a)</td><td>302.33 (n/a)</td><td>37.53 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.79 (+1.15%)</td><td>0.77 (+0.81%)</td><td>0.78 (+1.86%)</td><td>0.74 (-0.07%)</td><td>0.02 <b>(+21.85%)</b></td><td>101526.30 (+0.07%)</td><td>98098.44 (-0.78%)</td><td>97332.20 (-1.82%)</td><td>95164.60 (-1.14%)</td><td>2476.47 <b>(+20.83%)</b></td><td>722.11 (+1.15%)</td><td>700.87 (+0.81%)</td><td>706.03 (+1.86%)</td><td>676.86 (-0.07%)</td><td>17.59 <b>(+21.85%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>101456.40 (n/a)</td><td>98874.14 (n/a)</td><td>99140.40 (n/a)</td><td>96263.30 (n/a)</td><td>2049.57 (n/a)</td><td>713.87 (n/a)</td><td>695.26 (n/a)</td><td>693.15 (n/a)</td><td>677.33 (n/a)</td><td>14.43 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.77 (+1.21%)</td><td>0.75 (-0.70%)</td><td>0.75 (-0.65%)</td><td>0.72 (-3.41%)</td><td>0.02 <b>(+159.57%)</b></td><td>104466.10 (+3.53%)</td><td>100839.40 (+0.74%)</td><td>101131.90 (+0.66%)</td><td>97743.10 (-1.19%)</td><td>2480.29 <b>(+165.63%)</b></td><td>703.06 (+1.21%)</td><td>681.80 (-0.70%)</td><td>679.50 (-0.65%)</td><td>657.82 (-3.41%)</td><td>16.68 <b>(+159.57%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100907.60 (n/a)</td><td>100095.42 (n/a)</td><td>100471.10 (n/a)</td><td>98924.30 (n/a)</td><td>933.73 (n/a)</td><td>694.67 (n/a)</td><td>686.59 (n/a)</td><td>683.97 (n/a)</td><td>681.01 (n/a)</td><td>6.42 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.81 (+0.68%)</td><td>0.80 (+0.99%)</td><td>0.80 (+1.31%)</td><td>0.80 (+1.19%)</td><td>0.01 <b>(-23.12%)</b></td><td>94754.00 (-1.18%)</td><td>94072.42 (-0.98%)</td><td>94091.30 (-1.29%)</td><td>93404.60 (-0.67%)</td><td>619.76 <b>(-24.48%)</b></td><td>735.72 (+0.68%)</td><td>730.52 (+0.99%)</td><td>730.35 (+1.31%)</td><td>725.24 (+1.19%)</td><td>4.81 <b>(-23.12%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95884.80 (n/a)</td><td>95006.92 (n/a)</td><td>95320.80 (n/a)</td><td>94036.00 (n/a)</td><td>820.68 (n/a)</td><td>730.78 (n/a)</td><td>723.35 (n/a)</td><td>720.93 (n/a)</td><td>716.69 (n/a)</td><td>6.26 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>1.89 (-18.00%)</td><td>1.61 (-7.94%)</td><td>1.51 <b>(-20.58%)</b></td><td>1.45 (+15.04%)</td><td>0.19 <b>(-60.09%)</b></td><td>5555.50 (-13.07%)</td><td>5046.36 (+3.24%)</td><td>5336.70 <b>(+25.92%)</b></td><td>4255.10 <b>(+21.94%)</b></td><td>545.59 <b>(-60.04%)</b></td><td>496.80 (-18.00%)</td><td>423.11 (-7.94%)</td><td>396.11 <b>(-20.58%)</b></td><td>380.51 (+15.04%)</td><td>48.79 <b>(-60.09%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>2.31 (n/a)</td><td>1.75 (n/a)</td><td>1.90 (n/a)</td><td>1.26 (n/a)</td><td>0.47 (n/a)</td><td>6390.80 (n/a)</td><td>4887.86 (n/a)</td><td>4238.30 (n/a)</td><td>3489.40 (n/a)</td><td>1365.52 (n/a)</td><td>605.82 (n/a)</td><td>459.59 (n/a)</td><td>498.77 (n/a)</td><td>330.78 (n/a)</td><td>122.26 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.24 <b>(-23.69%)</b></td><td>0.20 (-17.92%)</td><td>0.20 (-9.28%)</td><td>0.14 <b>(-27.58%)</b></td><td>0.04 <b>(-31.17%)</b></td><td>8860.00 <b>(+38.09%)</b></td><td>6452.14 <b>(+21.22%)</b></td><td>6287.20 (+10.23%)</td><td>5171.70 <b>(+31.04%)</b></td><td>1437.74 <b>(+27.38%)</b></td><td>12.98 <b>(-23.69%)</b></td><td>10.76 (-17.92%)</td><td>10.67 (-9.28%)</td><td>7.57 <b>(-27.58%)</b></td><td>2.05 <b>(-31.17%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>6416.30 (n/a)</td><td>5322.76 (n/a)</td><td>5703.60 (n/a)</td><td>3946.70 (n/a)</td><td>1128.71 (n/a)</td><td>17.00 (n/a)</td><td>13.11 (n/a)</td><td>11.77 (n/a)</td><td>10.46 (n/a)</td><td>2.98 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>3.85 (n/a)</td><td>3.65 (n/a)</td><td>3.58 (n/a)</td><td>3.46 (n/a)</td><td>0.17 (n/a)</td><td>3.84 (n/a)</td><td>3.64 (n/a)</td><td>3.57 (n/a)</td><td>3.46 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>7.19 (+7.49%)</td><td>6.20 (+1.83%)</td><td>5.78 (-12.09%)</td><td>5.69 (+16.47%)</td><td>0.67 (-17.07%)</td><td>7.19 (+7.49%)</td><td>6.19 (+1.83%)</td><td>5.78 (-12.09%)</td><td>5.69 (+16.47%)</td><td>0.67 (-17.07%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>6.69 (n/a)</td><td>6.09 (n/a)</td><td>6.58 (n/a)</td><td>4.89 (n/a)</td><td>0.81 (n/a)</td><td>6.69 (n/a)</td><td>6.08 (n/a)</td><td>6.57 (n/a)</td><td>4.88 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>13.93 (-0.06%)</td><td>9.53 (+1.95%)</td><td>8.43 (-2.25%)</td><td>7.37 (+7.35%)</td><td>2.62 (-2.90%)</td><td>13.92 (-0.06%)</td><td>9.52 (+1.95%)</td><td>8.43 (-2.25%)</td><td>7.36 (+7.35%)</td><td>2.62 (-2.90%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>13.94 (n/a)</td><td>9.35 (n/a)</td><td>8.63 (n/a)</td><td>6.86 (n/a)</td><td>2.70 (n/a)</td><td>13.93 (n/a)</td><td>9.34 (n/a)</td><td>8.62 (n/a)</td><td>6.86 (n/a)</td><td>2.70 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>3.85 (n/a)</td><td>3.63 (n/a)</td><td>3.67 (n/a)</td><td>3.37 (n/a)</td><td>0.18 (n/a)</td><td>3.85 (n/a)</td><td>3.63 (n/a)</td><td>3.66 (n/a)</td><td>3.37 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>6.51 (-8.78%)</td><td>5.93 (-4.98%)</td><td>5.88 (-10.21%)</td><td>5.47 (+8.50%)</td><td>0.39 <b>(-55.01%)</b></td><td>6.51 (-8.78%)</td><td>5.93 (-4.98%)</td><td>5.88 (-10.21%)</td><td>5.47 (+8.50%)</td><td>0.39 <b>(-55.01%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>7.14 (n/a)</td><td>6.24 (n/a)</td><td>6.55 (n/a)</td><td>5.05 (n/a)</td><td>0.87 (n/a)</td><td>7.13 (n/a)</td><td>6.24 (n/a)</td><td>6.55 (n/a)</td><td>5.04 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>9.93 <b>(-25.55%)</b></td><td>8.94 (-11.02%)</td><td>8.56 (-14.78%)</td><td>8.10 (-0.59%)</td><td>0.91 <b>(-55.91%)</b></td><td>9.92 <b>(-25.55%)</b></td><td>8.94 (-11.02%)</td><td>8.56 (-14.78%)</td><td>8.09 (-0.59%)</td><td>0.91 <b>(-55.91%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>13.33 (n/a)</td><td>10.05 (n/a)</td><td>10.05 (n/a)</td><td>8.15 (n/a)</td><td>2.06 (n/a)</td><td>13.32 (n/a)</td><td>10.05 (n/a)</td><td>10.04 (n/a)</td><td>8.14 (n/a)</td><td>2.05 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>3.08 (-0.71%)</td><td>2.16 (+14.23%)</td><td>2.71 <b>(+85.77%)</b></td><td>1.03 (+2.36%)</td><td>0.95 (-6.76%)</td><td>3.07 (-0.71%)</td><td>2.16 (+14.23%)</td><td>2.71 <b>(+85.77%)</b></td><td>1.03 (+2.36%)</td><td>0.95 (-6.76%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.10 (n/a)</td><td>1.89 (n/a)</td><td>1.46 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td><td>3.09 (n/a)</td><td>1.89 (n/a)</td><td>1.46 (n/a)</td><td>1.01 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.50 (-7.40%)</td><td>0.33 (-19.03%)</td><td>0.40 (+14.20%)</td><td>0.08 <b>(-76.52%)</b></td><td>0.17 <b>(+85.12%)</b></td><td>0.49 (-7.40%)</td><td>0.32 (-19.03%)</td><td>0.40 (+14.20%)</td><td>0.07 <b>(-76.52%)</b></td><td>0.17 <b>(+85.12%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.54 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>0.53 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.68 <b>(+21.60%)</b></td><td>0.46 <b>(+80.03%)</b></td><td>0.63 <b>(+734.91%)</b></td><td>0.08 (+4.80%)</td><td>0.27 (+8.32%)</td><td>0.67 <b>(+21.60%)</b></td><td>0.46 <b>(+80.03%)</b></td><td>0.63 <b>(+734.91%)</b></td><td>0.08 (+4.80%)</td><td>0.27 (+8.32%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.56 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td><td>0.55 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>2.59 (-3.21%)</td><td>1.06 <b>(-36.25%)</b></td><td>0.78 <b>(-66.09%)</b></td><td>0.45 (+6.75%)</td><td>0.87 <b>(-23.44%)</b></td><td>2.55 (-3.21%)</td><td>1.04 <b>(-36.25%)</b></td><td>0.76 <b>(-66.09%)</b></td><td>0.44 (+6.75%)</td><td>0.85 <b>(-23.44%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>2.67 (n/a)</td><td>1.66 (n/a)</td><td>2.29 (n/a)</td><td>0.42 (n/a)</td><td>1.13 (n/a)</td><td>2.63 (n/a)</td><td>1.64 (n/a)</td><td>2.25 (n/a)</td><td>0.41 (n/a)</td><td>1.11 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.20 (n/a)</td><td>378.36 (n/a)</td><td>329.60 (n/a)</td><td>219.80 (n/a)</td><td>143.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.70 (n/a)</td><td>355.96 (n/a)</td><td>271.70 (n/a)</td><td>252.80 (n/a)</td><td>128.44 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.70 (n/a)</td><td>381.14 (n/a)</td><td>296.30 (n/a)</td><td>239.50 (n/a)</td><td>154.16 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>803.10 (n/a)</td><td>472.12 (n/a)</td><td>390.60 (n/a)</td><td>237.90 (n/a)</td><td>226.40 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>752.90 (n/a)</td><td>467.30 (n/a)</td><td>520.40 (n/a)</td><td>229.90 (n/a)</td><td>229.16 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.30 (n/a)</td><td>484.82 (n/a)</td><td>494.60 (n/a)</td><td>350.40 (n/a)</td><td>83.25 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.70 (n/a)</td><td>430.88 (n/a)</td><td>507.10 (n/a)</td><td>255.80 (n/a)</td><td>150.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>472.60 (n/a)</td><td>371.00 (n/a)</td><td>380.70 (n/a)</td><td>255.20 (n/a)</td><td>100.79 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.00 (n/a)</td><td>458.24 (n/a)</td><td>488.70 (n/a)</td><td>290.20 (n/a)</td><td>136.93 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>652.70 (n/a)</td><td>480.26 (n/a)</td><td>499.90 (n/a)</td><td>226.70 (n/a)</td><td>160.37 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>494.50 (n/a)</td><td>420.14 (n/a)</td><td>442.40 (n/a)</td><td>312.00 (n/a)</td><td>80.51 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>624.40 (n/a)</td><td>445.84 (n/a)</td><td>469.90 (n/a)</td><td>219.80 (n/a)</td><td>146.22 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>443.10 (n/a)</td><td>314.30 (n/a)</td><td>267.80 (n/a)</td><td>239.50 (n/a)</td><td>85.71 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>584.40 (n/a)</td><td>418.88 (n/a)</td><td>399.20 (n/a)</td><td>280.20 (n/a)</td><td>117.54 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1081.60 (n/a)</td><td>557.20 (n/a)</td><td>491.30 (n/a)</td><td>239.10 (n/a)</td><td>312.80 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>607.20 (n/a)</td><td>456.46 (n/a)</td><td>513.70 (n/a)</td><td>264.10 (n/a)</td><td>139.37 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>577.40 (n/a)</td><td>400.30 (n/a)</td><td>453.20 (n/a)</td><td>201.20 (n/a)</td><td>182.11 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1970.90 (n/a)</td><td>747.72 (n/a)</td><td>443.30 (n/a)</td><td>275.80 (n/a)</td><td>693.82 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>699.10 (n/a)</td><td>439.72 (n/a)</td><td>483.20 (n/a)</td><td>242.90 (n/a)</td><td>188.98 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>658.20 (n/a)</td><td>446.08 (n/a)</td><td>328.80 (n/a)</td><td>292.80 (n/a)</td><td>180.56 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>568.00 (n/a)</td><td>410.48 (n/a)</td><td>456.80 (n/a)</td><td>202.20 (n/a)</td><td>164.40 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>542.70 (n/a)</td><td>423.50 (n/a)</td><td>443.80 (n/a)</td><td>249.10 (n/a)</td><td>120.86 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1083.50 (n/a)</td><td>564.18 (n/a)</td><td>437.50 (n/a)</td><td>369.10 (n/a)</td><td>296.11 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>546.00 (n/a)</td><td>443.08 (n/a)</td><td>437.20 (n/a)</td><td>369.80 (n/a)</td><td>65.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (+12.98%)</td><td>0.01 (-12.56%)</td><td>0.01 <b>(-27.36%)</b></td><td>0.00 <b>(-73.43%)</b></td><td>0.01 <b>(+86.29%)</b></td><td>1869.50 <b>(+276.31%)</b></td><td>656.46 <b>(+84.12%)</b></td><td>407.80 <b>(+37.63%)</b></td><td>230.30 (-11.49%)</td><td>687.79 <b>(+541.59%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.80 (n/a)</td><td>356.54 (n/a)</td><td>296.30 (n/a)</td><td>260.20 (n/a)</td><td>107.20 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 <b>(-24.59%)</b></td><td>0.01 (+0.48%)</td><td>0.01 (-8.52%)</td><td>0.01 <b>(+312.43%)</b></td><td>0.00 <b>(-62.05%)</b></td><td>608.00 <b>(-75.75%)</b></td><td>524.84 <b>(-39.52%)</b></td><td>557.60 (+9.31%)</td><td>371.40 <b>(+32.60%)</b></td><td>94.65 <b>(-89.74%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2507.50 (n/a)</td><td>867.76 (n/a)</td><td>510.10 (n/a)</td><td>280.10 (n/a)</td><td>922.63 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(-25.90%)</b></td><td>0.01 (-10.01%)</td><td>0.01 (+3.75%)</td><td>0.01 (-5.28%)</td><td>0.00 <b>(-38.43%)</b></td><td>632.70 (+5.59%)</td><td>471.70 (+4.66%)</td><td>472.90 (-3.61%)</td><td>269.90 <b>(+34.95%)</b></td><td>141.54 (-5.40%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.20 (n/a)</td><td>450.70 (n/a)</td><td>490.60 (n/a)</td><td>200.00 (n/a)</td><td>149.61 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(+52.86%)</b></td><td>0.01 (+16.81%)</td><td>0.01 (+9.58%)</td><td>0.01 <b>(+37.29%)</b></td><td>0.01 <b>(+62.93%)</b></td><td>797.00 <b>(-27.15%)</b></td><td>519.68 (-12.58%)</td><td>533.80 (-8.74%)</td><td>204.80 <b>(-34.57%)</b></td><td>210.40 <b>(-30.97%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1094.10 (n/a)</td><td>594.48 (n/a)</td><td>584.90 (n/a)</td><td>313.00 (n/a)</td><td>304.80 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (+5.51%)</td><td>0.01 (-5.68%)</td><td>0.01 (+14.41%)</td><td>0.00 <b>(-67.91%)</b></td><td>0.01 <b>(+24.36%)</b></td><td>2021.80 <b>(+211.62%)</b></td><td>698.46 <b>(+59.56%)</b></td><td>437.10 (-12.60%)</td><td>233.00 (-5.21%)</td><td>748.71 <b>(+323.09%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>648.80 (n/a)</td><td>437.74 (n/a)</td><td>500.10 (n/a)</td><td>245.80 (n/a)</td><td>176.96 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 <b>(-30.31%)</b></td><td>0.01 (-7.70%)</td><td>0.01 (+3.83%)</td><td>0.01 (-0.92%)</td><td>0.00 <b>(-57.32%)</b></td><td>589.00 (+0.93%)</td><td>458.64 (+3.13%)</td><td>442.90 (-3.70%)</td><td>375.30 <b>(+43.46%)</b></td><td>79.01 <b>(-31.67%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.60 (n/a)</td><td>444.70 (n/a)</td><td>459.90 (n/a)</td><td>261.60 (n/a)</td><td>115.63 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 <b>(-29.69%)</b></td><td>0.03 (+11.02%)</td><td>0.03 <b>(+44.39%)</b></td><td>0.02 <b>(+22.54%)</b></td><td>0.01 <b>(-49.42%)</b></td><td>515.00 (-18.38%)</td><td>335.64 (-18.34%)</td><td>293.10 <b>(-30.74%)</b></td><td>285.70 <b>(+42.21%)</b></td><td>100.34 <b>(-38.39%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>631.00 (n/a)</td><td>411.00 (n/a)</td><td>423.20 (n/a)</td><td>200.90 (n/a)</td><td>162.87 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (-6.00%)</td><td>0.02 <b>(-22.44%)</b></td><td>0.02 <b>(-40.33%)</b></td><td>0.00 <b>(-68.79%)</b></td><td>0.01 (+3.47%)</td><td>1903.50 <b>(+220.35%)</b></td><td>687.70 <b>(+76.05%)</b></td><td>467.70 <b>(+67.57%)</b></td><td>260.10 (+6.42%)</td><td>685.72 <b>(+282.28%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.20 (n/a)</td><td>390.62 (n/a)</td><td>279.10 (n/a)</td><td>244.40 (n/a)</td><td>179.37 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (-4.03%)</td><td>0.02 (-5.29%)</td><td>0.03 <b>(+20.32%)</b></td><td>0.02 (+0.89%)</td><td>0.01 (-18.18%)</td><td>515.90 (-0.86%)</td><td>379.80 (+3.19%)</td><td>321.60 (-16.90%)</td><td>244.20 (+4.18%)</td><td>121.13 (-5.05%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.40 (n/a)</td><td>368.06 (n/a)</td><td>387.00 (n/a)</td><td>234.40 (n/a)</td><td>127.57 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (+0.96%)</td><td>0.02 (+4.81%)</td><td>0.03 <b>(+38.89%)</b></td><td>0.01 (-13.39%)</td><td>0.01 (+14.55%)</td><td>590.00 (+15.46%)</td><td>375.94 (-1.83%)</td><td>294.50 <b>(-28.00%)</b></td><td>281.90 (-0.95%)</td><td>132.64 <b>(+36.01%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.00 (n/a)</td><td>382.96 (n/a)</td><td>409.00 (n/a)</td><td>284.60 (n/a)</td><td>97.52 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (-16.90%)</td><td>0.02 (-17.76%)</td><td>0.02 <b>(-31.21%)</b></td><td>0.02 (+13.16%)</td><td>0.01 <b>(-42.43%)</b></td><td>526.70 (-11.63%)</td><td>425.56 (+12.15%)</td><td>433.70 <b>(+45.39%)</b></td><td>286.70 <b>(+20.36%)</b></td><td>92.39 <b>(-40.96%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.00 (n/a)</td><td>379.46 (n/a)</td><td>298.30 (n/a)</td><td>238.20 (n/a)</td><td>156.49 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 <b>(+43.73%)</b></td><td>0.02 <b>(+53.30%)</b></td><td>0.02 <b>(+24.15%)</b></td><td>0.01 <b>(+90.34%)</b></td><td>0.01 <b>(+60.81%)</b></td><td>571.10 <b>(-47.46%)</b></td><td>403.98 <b>(-35.48%)</b></td><td>440.80 (-19.44%)</td><td>248.20 <b>(-30.44%)</b></td><td>144.95 <b>(-47.06%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1087.00 (n/a)</td><td>626.16 (n/a)</td><td>547.20 (n/a)</td><td>356.80 (n/a)</td><td>273.81 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (+13.26%)</td><td>0.02 (+15.18%)</td><td>0.02 (+11.23%)</td><td>0.01 (-3.38%)</td><td>0.01 <b>(+30.93%)</b></td><td>653.30 (+3.50%)</td><td>449.68 (-9.74%)</td><td>434.10 (-10.11%)</td><td>263.80 (-11.71%)</td><td>162.77 (+19.31%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>631.20 (n/a)</td><td>498.22 (n/a)</td><td>482.90 (n/a)</td><td>298.80 (n/a)</td><td>136.42 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (-15.33%)</td><td>0.02 (+7.53%)</td><td>0.02 (+2.15%)</td><td>0.02 <b>(+91.99%)</b></td><td>0.00 <b>(-54.90%)</b></td><td>503.90 <b>(-47.92%)</b></td><td>405.16 <b>(-21.40%)</b></td><td>411.50 (-2.09%)</td><td>319.60 (+18.11%)</td><td>74.67 <b>(-73.17%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>967.50 (n/a)</td><td>515.50 (n/a)</td><td>420.30 (n/a)</td><td>270.60 (n/a)</td><td>278.32 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (-1.04%)</td><td>0.05 <b>(-24.60%)</b></td><td>0.04 <b>(-39.99%)</b></td><td>0.03 <b>(-33.62%)</b></td><td>0.02 <b>(+101.49%)</b></td><td>507.50 <b>(+50.64%)</b></td><td>394.04 <b>(+42.60%)</b></td><td>450.10 <b>(+66.64%)</b></td><td>246.40 (+1.07%)</td><td>119.89 <b>(+211.63%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>336.90 (n/a)</td><td>276.32 (n/a)</td><td>270.10 (n/a)</td><td>243.80 (n/a)</td><td>38.47 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 <b>(-28.84%)</b></td><td>0.03 <b>(-44.52%)</b></td><td>0.03 <b>(-55.59%)</b></td><td>0.01 <b>(-66.52%)</b></td><td>0.02 (-14.79%)</td><td>1907.90 <b>(+198.72%)</b></td><td>751.88 <b>(+127.55%)</b></td><td>567.70 <b>(+125.19%)</b></td><td>311.20 <b>(+40.50%)</b></td><td>655.81 <b>(+274.91%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>638.70 (n/a)</td><td>330.42 (n/a)</td><td>252.10 (n/a)</td><td>221.50 (n/a)</td><td>174.92 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (+14.83%)</td><td>0.05 (+11.85%)</td><td>0.06 <b>(+45.85%)</b></td><td>0.03 (-5.71%)</td><td>0.02 <b>(+32.77%)</b></td><td>574.30 (+6.06%)</td><td>368.10 (-6.07%)</td><td>286.90 <b>(-31.45%)</b></td><td>224.10 (-12.90%)</td><td>149.13 <b>(+29.58%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>541.50 (n/a)</td><td>391.88 (n/a)</td><td>418.50 (n/a)</td><td>257.30 (n/a)</td><td>115.09 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 <b>(-26.54%)</b></td><td>0.03 <b>(-33.79%)</b></td><td>0.03 <b>(-44.50%)</b></td><td>0.02 (-11.72%)</td><td>0.01 <b>(-46.55%)</b></td><td>778.10 (+13.28%)</td><td>554.94 <b>(+37.50%)</b></td><td>545.90 <b>(+80.17%)</b></td><td>332.40 <b>(+36.12%)</b></td><td>158.61 (-19.05%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>686.90 (n/a)</td><td>403.60 (n/a)</td><td>303.00 (n/a)</td><td>244.20 (n/a)</td><td>195.94 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (-4.51%)</td><td>0.04 <b>(-20.65%)</b></td><td>0.03 <b>(-34.81%)</b></td><td>0.03 (+7.71%)</td><td>0.01 (-9.74%)</td><td>570.40 (-7.16%)</td><td>462.68 <b>(+23.05%)</b></td><td>484.80 <b>(+53.42%)</b></td><td>270.30 (+4.73%)</td><td>113.96 <b>(-20.20%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>614.40 (n/a)</td><td>376.02 (n/a)</td><td>316.00 (n/a)</td><td>258.10 (n/a)</td><td>142.80 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 <b>(-21.31%)</b></td><td>0.03 (-13.79%)</td><td>0.03 (-2.53%)</td><td>0.03 (-10.70%)</td><td>0.01 <b>(-35.07%)</b></td><td>629.80 (+11.98%)</td><td>495.26 (+11.68%)</td><td>508.00 (+2.61%)</td><td>315.80 <b>(+27.08%)</b></td><td>114.36 (-12.00%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>562.40 (n/a)</td><td>443.46 (n/a)</td><td>495.10 (n/a)</td><td>248.50 (n/a)</td><td>129.96 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (-15.29%)</td><td>0.08 (-12.10%)</td><td>0.08 <b>(-31.47%)</b></td><td>0.06 <b>(+21.31%)</b></td><td>0.02 <b>(-44.91%)</b></td><td>524.70 (-17.56%)</td><td>409.22 (+1.66%)</td><td>435.60 <b>(+45.88%)</b></td><td>285.40 (+18.08%)</td><td>96.26 <b>(-48.36%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>636.50 (n/a)</td><td>402.54 (n/a)</td><td>298.60 (n/a)</td><td>241.70 (n/a)</td><td>186.40 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.10 <b>(-22.11%)</b></td><td>0.07 (-11.25%)</td><td>0.07 (-9.65%)</td><td>0.05 <b>(+268.64%)</b></td><td>0.02 <b>(-53.56%)</b></td><td>664.70 <b>(-72.87%)</b></td><td>492.54 <b>(-37.03%)</b></td><td>492.20 (+10.68%)</td><td>312.20 <b>(+28.37%)</b></td><td>131.34 <b>(-85.99%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2450.20 (n/a)</td><td>782.16 (n/a)</td><td>444.70 (n/a)</td><td>243.20 (n/a)</td><td>937.24 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.15 (+16.31%)</td><td>0.11 (+19.50%)</td><td>0.13 <b>(+40.34%)</b></td><td>0.07 (+14.52%)</td><td>0.04 <b>(+27.65%)</b></td><td>490.40 (-12.68%)</td><td>330.04 (-14.29%)</td><td>259.00 <b>(-28.75%)</b></td><td>214.40 (-14.03%)</td><td>128.00 (-0.70%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>561.60 (n/a)</td><td>385.06 (n/a)</td><td>363.50 (n/a)</td><td>249.40 (n/a)</td><td>128.90 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (+12.34%)</td><td>0.10 (-5.91%)</td><td>0.10 (-10.73%)</td><td>0.05 <b>(-44.26%)</b></td><td>0.03 <b>(+77.67%)</b></td><td>702.20 <b>(+79.41%)</b></td><td>382.70 (+18.41%)</td><td>334.60 (+12.02%)</td><td>236.10 (-11.01%)</td><td>184.74 <b>(+197.42%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>391.40 (n/a)</td><td>323.20 (n/a)</td><td>298.70 (n/a)</td><td>265.30 (n/a)</td><td>62.11 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 <b>(+24.77%)</b></td><td>0.09 (+8.26%)</td><td>0.10 (+9.44%)</td><td>0.02 <b>(-39.35%)</b></td><td>0.05 <b>(+56.95%)</b></td><td>1859.90 <b>(+64.87%)</b></td><td>664.16 <b>(+27.42%)</b></td><td>343.40 (-8.65%)</td><td>246.50 (-19.86%)</td><td>684.63 <b>(+98.19%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1128.10 (n/a)</td><td>521.24 (n/a)</td><td>375.90 (n/a)</td><td>307.60 (n/a)</td><td>345.44 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (-17.50%)</td><td>0.01 (-15.04%)</td><td>0.01 <b>(-23.84%)</b></td><td>0.01 (-4.17%)</td><td>0.00 <b>(-42.89%)</b></td><td>547.10 (+4.35%)</td><td>413.44 (+10.55%)</td><td>406.50 <b>(+31.30%)</b></td><td>296.60 <b>(+21.21%)</b></td><td>92.79 <b>(-32.26%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.30 (n/a)</td><td>374.00 (n/a)</td><td>309.60 (n/a)</td><td>244.70 (n/a)</td><td>136.98 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (-0.79%)</td><td>0.01 (-0.89%)</td><td>0.01 (-1.06%)</td><td>0.01 (+6.56%)</td><td>0.00 (-2.21%)</td><td>495.00 (-6.16%)</td><td>362.60 (+0.48%)</td><td>280.00 (+1.05%)</td><td>273.50 (+0.77%)</td><td>117.36 (-3.38%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.50 (n/a)</td><td>360.88 (n/a)</td><td>277.10 (n/a)</td><td>271.40 (n/a)</td><td>121.46 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (-8.79%)</td><td>0.01 (-4.37%)</td><td>0.01 (-10.83%)</td><td>0.00 <b>(+129.26%)</b></td><td>0.00 <b>(-32.10%)</b></td><td>1069.70 <b>(-56.38%)</b></td><td>639.46 <b>(-26.01%)</b></td><td>560.40 (+12.15%)</td><td>410.10 (+9.65%)</td><td>259.53 <b>(-70.83%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2452.50 (n/a)</td><td>864.28 (n/a)</td><td>499.70 (n/a)</td><td>374.00 (n/a)</td><td>889.58 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (+2.67%)</td><td>0.01 (+0.03%)</td><td>0.02 (-3.53%)</td><td>0.01 <b>(-25.52%)</b></td><td>0.00 (+7.16%)</td><td>653.80 <b>(+34.28%)</b></td><td>342.64 (+5.36%)</td><td>268.60 (+3.67%)</td><td>233.80 (-2.62%)</td><td>175.06 <b>(+56.97%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>486.90 (n/a)</td><td>325.20 (n/a)</td><td>259.10 (n/a)</td><td>240.10 (n/a)</td><td>111.52 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (+3.43%)</td><td>0.01 (+16.09%)</td><td>0.01 (+3.03%)</td><td>0.01 (+4.54%)</td><td>0.00 <b>(+29.09%)</b></td><td>525.00 (-4.34%)</td><td>407.10 (-11.14%)</td><td>460.00 (-2.93%)</td><td>271.50 (-3.31%)</td><td>125.91 <b>(+20.78%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.80 (n/a)</td><td>458.14 (n/a)</td><td>473.90 (n/a)</td><td>280.80 (n/a)</td><td>104.25 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (+6.48%)</td><td>0.01 <b>(-30.94%)</b></td><td>0.01 <b>(-40.43%)</b></td><td>0.00 <b>(-77.67%)</b></td><td>0.01 <b>(+91.67%)</b></td><td>1840.90 <b>(+347.91%)</b></td><td>677.40 <b>(+132.42%)</b></td><td>494.00 <b>(+67.86%)</b></td><td>213.70 (-6.11%)</td><td>663.88 <b>(+788.22%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>411.00 (n/a)</td><td>291.46 (n/a)</td><td>294.30 (n/a)</td><td>227.60 (n/a)</td><td>74.74 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(+107.29%)</b></td><td>0.01 <b>(+77.94%)</b></td><td>0.01 <b>(+25.23%)</b></td><td>0.01 <b>(+304.64%)</b></td><td>0.01 <b>(+72.99%)</b></td><td>598.40 <b>(-75.29%)</b></td><td>387.08 <b>(-56.53%)</b></td><td>429.80 <b>(-20.16%)</b></td><td>216.70 <b>(-51.75%)</b></td><td>155.12 <b>(-81.90%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2421.30 (n/a)</td><td>890.44 (n/a)</td><td>538.30 (n/a)</td><td>449.10 (n/a)</td><td>856.87 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(-29.32%)</b></td><td>0.01 <b>(-27.66%)</b></td><td>0.01 <b>(-43.27%)</b></td><td>0.01 <b>(-23.51%)</b></td><td>0.01 (-9.11%)</td><td>790.40 <b>(+30.73%)</b></td><td>478.92 <b>(+45.42%)</b></td><td>503.10 <b>(+76.28%)</b></td><td>252.40 <b>(+41.48%)</b></td><td>229.68 <b>(+42.46%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.60 (n/a)</td><td>329.34 (n/a)</td><td>285.40 (n/a)</td><td>178.40 (n/a)</td><td>161.23 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (+4.50%)</td><td>0.01 (+2.65%)</td><td>0.01 <b>(-26.82%)</b></td><td>0.01 (+6.50%)</td><td>0.00 (+0.97%)</td><td>521.90 (-6.10%)</td><td>374.98 (-4.43%)</td><td>421.60 <b>(+36.66%)</b></td><td>240.20 (-4.30%)</td><td>119.00 (-19.10%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>555.80 (n/a)</td><td>392.38 (n/a)</td><td>308.50 (n/a)</td><td>251.00 (n/a)</td><td>147.09 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (+17.79%)</td><td>0.01 (-9.38%)</td><td>0.01 (-8.32%)</td><td>0.00 <b>(-75.86%)</b></td><td>0.01 <b>(+169.13%)</b></td><td>1887.40 <b>(+314.27%)</b></td><td>656.74 <b>(+80.84%)</b></td><td>372.60 (+9.07%)</td><td>239.60 (-15.10%)</td><td>694.23 <b>(+940.89%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>455.60 (n/a)</td><td>363.16 (n/a)</td><td>341.60 (n/a)</td><td>282.20 (n/a)</td><td>66.70 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(+32.93%)</b></td><td>0.01 <b>(+23.03%)</b></td><td>0.01 (+0.41%)</td><td>0.00 <b>(+33.29%)</b></td><td>0.00 <b>(+44.41%)</b></td><td>827.50 <b>(-24.97%)</b></td><td>515.34 (-17.34%)</td><td>523.70 (-0.40%)</td><td>268.00 <b>(-24.76%)</b></td><td>224.32 <b>(-23.24%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1102.90 (n/a)</td><td>623.46 (n/a)</td><td>525.80 (n/a)</td><td>356.20 (n/a)</td><td>292.23 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (-6.75%)</td><td>0.01 (-9.94%)</td><td>0.01 (+7.92%)</td><td>0.00 (+5.97%)</td><td>0.00 (-16.46%)</td><td>1856.70 (-5.63%)</td><td>734.08 (+0.54%)</td><td>489.20 (-7.33%)</td><td>273.20 (+7.22%)</td><td>639.07 (-9.52%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1967.50 (n/a)</td><td>730.16 (n/a)</td><td>527.90 (n/a)</td><td>254.80 (n/a)</td><td>706.29 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (+3.82%)</td><td>0.03 (+8.88%)</td><td>0.03 (+7.01%)</td><td>0.02 (-1.52%)</td><td>0.01 (-8.01%)</td><td>536.80 (+1.55%)</td><td>334.12 (-9.14%)</td><td>291.20 (-6.55%)</td><td>243.10 (-3.68%)</td><td>115.89 (-4.95%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.60 (n/a)</td><td>367.72 (n/a)</td><td>311.60 (n/a)</td><td>252.40 (n/a)</td><td>121.92 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (+18.19%)</td><td>0.03 <b>(+30.38%)</b></td><td>0.03 <b>(+50.24%)</b></td><td>0.01 (-10.71%)</td><td>0.01 <b>(+27.90%)</b></td><td>626.80 (+11.99%)</td><td>333.30 (-19.52%)</td><td>272.80 <b>(-33.43%)</b></td><td>226.20 (-15.38%)</td><td>167.07 <b>(+24.81%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.70 (n/a)</td><td>414.16 (n/a)</td><td>409.80 (n/a)</td><td>267.30 (n/a)</td><td>133.87 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (+15.51%)</td><td>0.02 <b>(-20.17%)</b></td><td>0.02 <b>(-39.97%)</b></td><td>0.01 <b>(-21.20%)</b></td><td>0.01 <b>(+45.29%)</b></td><td>667.50 <b>(+26.90%)</b></td><td>517.26 <b>(+35.68%)</b></td><td>531.60 <b>(+66.59%)</b></td><td>222.50 (-13.42%)</td><td>178.27 <b>(+44.53%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.00 (n/a)</td><td>381.24 (n/a)</td><td>319.10 (n/a)</td><td>257.00 (n/a)</td><td>123.35 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (-4.90%)</td><td>0.03 (+3.57%)</td><td>0.03 (-2.14%)</td><td>0.02 (-0.21%)</td><td>0.01 (-16.35%)</td><td>479.30 (+0.21%)</td><td>308.66 (-6.49%)</td><td>296.20 (+2.21%)</td><td>190.50 (+5.19%)</td><td>106.02 (-12.78%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.30 (n/a)</td><td>330.08 (n/a)</td><td>289.80 (n/a)</td><td>181.10 (n/a)</td><td>121.56 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (+15.68%)</td><td>0.02 <b>(-22.14%)</b></td><td>0.01 <b>(-45.45%)</b></td><td>0.01 <b>(-20.67%)</b></td><td>0.01 <b>(+61.54%)</b></td><td>627.50 <b>(+26.05%)</b></td><td>485.98 <b>(+38.33%)</b></td><td>552.40 <b>(+83.28%)</b></td><td>236.90 (-13.57%)</td><td>153.28 <b>(+66.13%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.80 (n/a)</td><td>351.32 (n/a)</td><td>301.40 (n/a)</td><td>274.10 (n/a)</td><td>92.26 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 <b>(-27.21%)</b></td><td>0.02 (-16.21%)</td><td>0.02 <b>(-24.91%)</b></td><td>0.02 (+11.82%)</td><td>0.01 <b>(-35.00%)</b></td><td>503.50 (-10.57%)</td><td>403.14 (+13.50%)</td><td>458.70 <b>(+33.15%)</b></td><td>287.30 <b>(+37.40%)</b></td><td>103.82 <b>(-22.77%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.00 (n/a)</td><td>355.20 (n/a)</td><td>344.50 (n/a)</td><td>209.10 (n/a)</td><td>134.43 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (-6.12%)</td><td>0.02 <b>(+33.11%)</b></td><td>0.02 <b>(+38.95%)</b></td><td>0.02 <b>(+99.14%)</b></td><td>0.01 <b>(-24.97%)</b></td><td>535.10 <b>(-49.78%)</b></td><td>389.08 <b>(-34.58%)</b></td><td>418.30 <b>(-28.03%)</b></td><td>269.00 (+6.53%)</td><td>115.27 <b>(-61.30%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1065.60 (n/a)</td><td>594.72 (n/a)</td><td>581.20 (n/a)</td><td>252.50 (n/a)</td><td>297.85 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (-11.90%)</td><td>0.02 (-9.21%)</td><td>0.02 (-12.95%)</td><td>0.00 (-0.94%)</td><td>0.01 (-3.72%)</td><td>1878.90 (+0.95%)</td><td>711.42 (+7.85%)</td><td>487.10 (+14.85%)</td><td>259.80 (+13.50%)</td><td>671.43 (-1.13%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1861.30 (n/a)</td><td>659.64 (n/a)</td><td>424.10 (n/a)</td><td>228.90 (n/a)</td><td>679.10 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (+15.40%)</td><td>0.02 <b>(+22.15%)</b></td><td>0.02 (+15.62%)</td><td>0.01 <b>(+289.73%)</b></td><td>0.01 <b>(-24.89%)</b></td><td>583.90 <b>(-74.34%)</b></td><td>430.54 <b>(-46.22%)</b></td><td>433.60 (-13.52%)</td><td>271.50 (-13.34%)</td><td>130.66 <b>(-84.29%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2275.70 (n/a)</td><td>800.56 (n/a)</td><td>501.40 (n/a)</td><td>313.30 (n/a)</td><td>831.63 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (-3.00%)</td><td>0.02 (-0.24%)</td><td>0.02 (+12.69%)</td><td>0.01 (+5.50%)</td><td>0.01 <b>(-21.45%)</b></td><td>563.70 (-5.21%)</td><td>421.70 (-3.65%)</td><td>414.90 (-11.25%)</td><td>274.40 (+3.08%)</td><td>110.60 <b>(-23.75%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.70 (n/a)</td><td>437.68 (n/a)</td><td>467.50 (n/a)</td><td>266.20 (n/a)</td><td>145.05 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(-34.13%)</b></td><td>0.02 <b>(-28.56%)</b></td><td>0.02 <b>(-38.20%)</b></td><td>0.02 (+19.38%)</td><td>0.00 <b>(-70.69%)</b></td><td>517.90 (-16.22%)</td><td>464.04 <b>(+26.33%)</b></td><td>473.00 <b>(+61.82%)</b></td><td>370.40 <b>(+51.80%)</b></td><td>55.65 <b>(-64.04%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.20 (n/a)</td><td>367.32 (n/a)</td><td>292.30 (n/a)</td><td>244.00 (n/a)</td><td>154.76 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 <b>(+44.32%)</b></td><td>0.02 (+17.70%)</td><td>0.02 (+7.16%)</td><td>0.01 (+0.75%)</td><td>0.01 <b>(+84.00%)</b></td><td>800.30 (-0.73%)</td><td>500.18 (-8.03%)</td><td>500.60 (-6.67%)</td><td>241.10 <b>(-30.70%)</b></td><td>204.88 <b>(+21.32%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>806.20 (n/a)</td><td>543.84 (n/a)</td><td>536.40 (n/a)</td><td>347.90 (n/a)</td><td>168.87 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (+3.74%)</td><td>0.05 (+9.88%)</td><td>0.05 (+10.24%)</td><td>0.04 (-0.86%)</td><td>0.01 <b>(+25.10%)</b></td><td>439.60 (+0.85%)</td><td>317.28 (-7.87%)</td><td>308.00 (-9.28%)</td><td>260.00 (-3.60%)</td><td>73.47 <b>(+20.41%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>435.90 (n/a)</td><td>344.40 (n/a)</td><td>339.50 (n/a)</td><td>269.70 (n/a)</td><td>61.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (+2.29%)</td><td>0.05 (+4.93%)</td><td>0.05 (+19.16%)</td><td>0.02 <b>(-28.47%)</b></td><td>0.02 <b>(+48.89%)</b></td><td>716.60 <b>(+39.82%)</b></td><td>404.50 (+8.02%)</td><td>304.40 (-16.10%)</td><td>228.40 (-2.23%)</td><td>209.34 <b>(+109.24%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>512.50 (n/a)</td><td>374.46 (n/a)</td><td>362.80 (n/a)</td><td>233.60 (n/a)</td><td>100.05 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (-8.71%)</td><td>0.05 <b>(+27.59%)</b></td><td>0.04 (+18.92%)</td><td>0.03 <b>(+267.64%)</b></td><td>0.02 <b>(-34.83%)</b></td><td>513.50 <b>(-72.80%)</b></td><td>383.54 <b>(-50.61%)</b></td><td>452.20 (-15.92%)</td><td>241.10 (+9.54%)</td><td>127.92 <b>(-81.22%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1887.80 (n/a)</td><td>776.50 (n/a)</td><td>537.80 (n/a)</td><td>220.10 (n/a)</td><td>681.03 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (+7.90%)</td><td>0.05 <b>(+35.04%)</b></td><td>0.06 <b>(+48.11%)</b></td><td>0.04 <b>(+392.11%)</b></td><td>0.01 <b>(-36.99%)</b></td><td>425.70 <b>(-79.68%)</b></td><td>321.32 <b>(-55.39%)</b></td><td>271.00 <b>(-32.49%)</b></td><td>230.00 (-7.33%)</td><td>92.56 <b>(-88.12%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2094.70 (n/a)</td><td>720.30 (n/a)</td><td>401.40 (n/a)</td><td>248.20 (n/a)</td><td>778.90 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (+16.91%)</td><td>0.04 (-10.61%)</td><td>0.03 <b>(-20.82%)</b></td><td>0.02 (+15.91%)</td><td>0.02 (+7.89%)</td><td>660.70 (-13.72%)</td><td>486.08 (+9.39%)</td><td>481.10 <b>(+26.31%)</b></td><td>230.20 (-14.46%)</td><td>163.75 <b>(-21.50%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>765.80 (n/a)</td><td>444.34 (n/a)</td><td>380.90 (n/a)</td><td>269.10 (n/a)</td><td>208.59 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 <b>(+30.99%)</b></td><td>0.05 <b>(+40.45%)</b></td><td>0.05 <b>(+41.08%)</b></td><td>0.03 <b>(+173.87%)</b></td><td>0.02 (-0.68%)</td><td>651.60 <b>(-63.49%)</b></td><td>378.46 <b>(-45.76%)</b></td><td>307.00 <b>(-29.13%)</b></td><td>223.90 <b>(-23.66%)</b></td><td>167.36 <b>(-73.03%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1784.60 (n/a)</td><td>697.78 (n/a)</td><td>433.20 (n/a)</td><td>293.30 (n/a)</td><td>620.52 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 <b>(+49.15%)</b></td><td>0.04 <b>(+23.74%)</b></td><td>0.03 (+13.77%)</td><td>0.01 (+1.12%)</td><td>0.03 <b>(+61.80%)</b></td><td>1922.40 (-1.11%)</td><td>740.26 (-6.54%)</td><td>530.60 (-12.09%)</td><td>184.80 <b>(-32.97%)</b></td><td>679.03 (+2.86%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1943.90 (n/a)</td><td>792.10 (n/a)</td><td>603.60 (n/a)</td><td>275.70 (n/a)</td><td>660.13 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (+1.82%)</td><td>0.04 (-9.45%)</td><td>0.04 <b>(-22.81%)</b></td><td>0.03 (+19.20%)</td><td>0.01 (-11.14%)</td><td>533.10 (-16.11%)</td><td>400.24 (+6.37%)</td><td>399.50 <b>(+29.54%)</b></td><td>256.90 (-1.80%)</td><td>101.53 <b>(-32.51%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>635.50 (n/a)</td><td>376.28 (n/a)</td><td>308.40 (n/a)</td><td>261.60 (n/a)</td><td>150.45 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (+2.75%)</td><td>0.04 (+6.83%)</td><td>0.05 <b>(+30.33%)</b></td><td>0.02 <b>(-33.08%)</b></td><td>0.01 <b>(+71.95%)</b></td><td>828.70 <b>(+49.42%)</b></td><td>456.20 (+3.65%)</td><td>352.20 <b>(-23.27%)</b></td><td>311.60 (-2.66%)</td><td>218.41 <b>(+153.05%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>554.60 (n/a)</td><td>440.12 (n/a)</td><td>459.00 (n/a)</td><td>320.10 (n/a)</td><td>86.31 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (+8.87%)</td><td>0.04 (-8.54%)</td><td>0.03 (-6.27%)</td><td>0.02 <b>(-22.94%)</b></td><td>0.01 <b>(+51.13%)</b></td><td>665.50 <b>(+29.75%)</b></td><td>496.78 (+14.13%)</td><td>485.70 (+6.68%)</td><td>306.30 (-8.16%)</td><td>137.98 <b>(+76.24%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>512.90 (n/a)</td><td>435.28 (n/a)</td><td>455.30 (n/a)</td><td>333.50 (n/a)</td><td>78.29 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 <b>(+28.29%)</b></td><td>0.04 (+15.45%)</td><td>0.03 (+14.77%)</td><td>0.02 (-4.90%)</td><td>0.02 <b>(+63.90%)</b></td><td>656.00 (+5.15%)</td><td>446.58 (-6.76%)</td><td>471.10 (-12.87%)</td><td>250.90 <b>(-22.03%)</b></td><td>176.36 <b>(+33.58%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>623.90 (n/a)</td><td>478.96 (n/a)</td><td>540.70 (n/a)</td><td>321.80 (n/a)</td><td>132.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 <b>(-25.76%)</b></td><td>0.04 <b>(-33.59%)</b></td><td>0.03 <b>(-47.33%)</b></td><td>0.02 <b>(-30.37%)</b></td><td>0.01 (-5.04%)</td><td>684.50 <b>(+43.59%)</b></td><td>504.32 <b>(+57.59%)</b></td><td>580.40 <b>(+89.86%)</b></td><td>297.90 <b>(+34.67%)</b></td><td>173.42 <b>(+77.50%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.70 (n/a)</td><td>320.02 (n/a)</td><td>305.70 (n/a)</td><td>221.20 (n/a)</td><td>97.70 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.15 <b>(+22.84%)</b></td><td>0.10 (-8.16%)</td><td>0.11 (-7.23%)</td><td>0.06 (-10.47%)</td><td>0.04 <b>(+64.86%)</b></td><td>559.00 (+11.71%)</td><td>386.00 (+17.46%)</td><td>306.20 (+7.78%)</td><td>225.20 (-18.61%)</td><td>154.02 <b>(+59.59%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>500.40 (n/a)</td><td>328.62 (n/a)</td><td>284.10 (n/a)</td><td>276.70 (n/a)</td><td>96.51 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (+9.05%)</td><td>0.11 <b>(+50.45%)</b></td><td>0.12 <b>(+109.02%)</b></td><td>0.07 <b>(+354.94%)</b></td><td>0.03 <b>(-40.61%)</b></td><td>454.20 <b>(-78.02%)</b></td><td>321.12 <b>(-58.06%)</b></td><td>283.40 <b>(-52.15%)</b></td><td>243.80 (-8.31%)</td><td>88.12 <b>(-88.16%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2066.30 (n/a)</td><td>765.60 (n/a)</td><td>592.30 (n/a)</td><td>265.90 (n/a)</td><td>744.09 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (+6.86%)</td><td>0.09 (-2.01%)</td><td>0.08 <b>(-22.48%)</b></td><td>0.06 (+6.92%)</td><td>0.02 (+0.74%)</td><td>512.60 (-6.48%)</td><td>389.90 (+1.30%)</td><td>411.60 <b>(+28.99%)</b></td><td>275.40 (-6.45%)</td><td>101.65 (-11.98%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>548.10 (n/a)</td><td>384.90 (n/a)</td><td>319.10 (n/a)</td><td>294.40 (n/a)</td><td>115.48 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (+14.68%)</td><td>0.08 (+5.32%)</td><td>0.06 <b>(-21.13%)</b></td><td>0.04 <b>(+137.31%)</b></td><td>0.03 (-6.32%)</td><td>814.70 <b>(-57.86%)</b></td><td>498.96 <b>(-29.10%)</b></td><td>505.10 <b>(+26.78%)</b></td><td>260.40 (-12.79%)</td><td>206.38 <b>(-70.14%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1933.40 (n/a)</td><td>703.74 (n/a)</td><td>398.40 (n/a)</td><td>298.60 (n/a)</td><td>691.05 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (-19.49%)</td><td>0.08 (-10.72%)</td><td>0.08 <b>(+21.25%)</b></td><td>0.05 (-1.49%)</td><td>0.03 <b>(-36.05%)</b></td><td>611.90 (+1.51%)</td><td>464.42 (+4.16%)</td><td>429.20 (-17.52%)</td><td>278.50 <b>(+24.22%)</b></td><td>137.48 (-19.86%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>602.80 (n/a)</td><td>445.86 (n/a)</td><td>520.40 (n/a)</td><td>224.20 (n/a)</td><td>171.54 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (-15.74%)</td><td>0.10 (-2.25%)</td><td>0.11 (+6.55%)</td><td>0.07 (+1.91%)</td><td>0.03 (-19.19%)</td><td>450.40 (-1.87%)</td><td>342.78 (+0.89%)</td><td>297.00 (-6.16%)</td><td>256.20 (+18.67%)</td><td>92.64 (-3.79%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>459.00 (n/a)</td><td>339.74 (n/a)</td><td>316.50 (n/a)</td><td>215.90 (n/a)</td><td>96.29 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (-16.84%)</td><td>0.08 <b>(-22.14%)</b></td><td>0.06 <b>(-31.49%)</b></td><td>0.06 (-10.21%)</td><td>0.02 <b>(-25.55%)</b></td><td>529.20 (+11.36%)</td><td>459.54 <b>(+25.86%)</b></td><td>515.10 <b>(+45.96%)</b></td><td>290.80 <b>(+20.26%)</b></td><td>101.40 (-4.96%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>475.20 (n/a)</td><td>365.12 (n/a)</td><td>352.90 (n/a)</td><td>241.80 (n/a)</td><td>106.69 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 <b>(-26.39%)</b></td><td>0.08 (-11.02%)</td><td>0.08 (-1.60%)</td><td>0.06 (+12.36%)</td><td>0.02 <b>(-47.48%)</b></td><td>520.10 (-10.99%)</td><td>418.44 (+4.26%)</td><td>415.00 (+1.64%)</td><td>283.20 <b>(+35.83%)</b></td><td>90.56 <b>(-34.95%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>584.30 (n/a)</td><td>401.34 (n/a)</td><td>408.30 (n/a)</td><td>208.50 (n/a)</td><td>139.23 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 <b>(-30.52%)</b></td><td>0.07 <b>(-28.63%)</b></td><td>0.07 <b>(-34.72%)</b></td><td>0.05 (-10.68%)</td><td>0.03 <b>(-44.53%)</b></td><td>627.60 (+11.95%)</td><td>472.84 <b>(+27.81%)</b></td><td>480.90 <b>(+53.20%)</b></td><td>271.40 <b>(+43.98%)</b></td><td>129.94 <b>(-21.53%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>560.60 (n/a)</td><td>369.96 (n/a)</td><td>313.90 (n/a)</td><td>188.50 (n/a)</td><td>165.60 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (+2.06%)</td><td>0.09 (+3.69%)</td><td>0.09 (-6.19%)</td><td>0.06 <b>(+36.81%)</b></td><td>0.03 <b>(-22.23%)</b></td><td>584.80 <b>(-26.90%)</b></td><td>411.96 (-15.44%)</td><td>381.30 (+6.60%)</td><td>241.80 (-2.03%)</td><td>146.35 <b>(-45.48%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>800.00 (n/a)</td><td>487.18 (n/a)</td><td>357.70 (n/a)</td><td>246.80 (n/a)</td><td>268.46 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 <b>(-30.96%)</b></td><td>0.07 (-19.91%)</td><td>0.07 (+18.27%)</td><td>0.06 (+8.49%)</td><td>0.02 <b>(-55.69%)</b></td><td>595.70 (-7.83%)</td><td>469.54 (+5.41%)</td><td>455.70 (-15.44%)</td><td>287.90 <b>(+44.82%)</b></td><td>118.60 <b>(-42.92%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>646.30 (n/a)</td><td>445.46 (n/a)</td><td>538.90 (n/a)</td><td>198.80 (n/a)</td><td>207.77 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.11 (-3.08%)</td><td>0.06 (-12.47%)</td><td>0.05 (-10.84%)</td><td>0.02 <b>(-50.08%)</b></td><td>0.04 (+16.13%)</td><td>1893.90 <b>(+100.33%)</b></td><td>798.62 <b>(+43.10%)</b></td><td>604.70 (+12.17%)</td><td>302.30 (+3.17%)</td><td>639.85 <b>(+151.94%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>945.40 (n/a)</td><td>558.08 (n/a)</td><td>539.10 (n/a)</td><td>293.00 (n/a)</td><td>253.97 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (-1.71%)</td><td>0.01 (-8.55%)</td><td>0.01 (-14.26%)</td><td>0.01 (+2.99%)</td><td>0.00 <b>(-21.91%)</b></td><td>531.40 (-2.91%)</td><td>415.62 (+4.99%)</td><td>432.00 (+16.63%)</td><td>264.40 (+1.73%)</td><td>102.22 <b>(-25.59%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.30 (n/a)</td><td>395.86 (n/a)</td><td>370.40 (n/a)</td><td>259.90 (n/a)</td><td>137.37 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (-6.27%)</td><td>0.02 (-15.30%)</td><td>0.02 (-17.32%)</td><td>0.01 (-2.62%)</td><td>0.01 (+2.17%)</td><td>562.10 (+2.69%)</td><td>400.32 (+19.56%)</td><td>355.00 <b>(+20.95%)</b></td><td>253.30 (+6.70%)</td><td>139.24 (+12.19%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.40 (n/a)</td><td>334.82 (n/a)</td><td>293.50 (n/a)</td><td>237.40 (n/a)</td><td>124.10 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (-16.57%)</td><td>0.01 (+3.91%)</td><td>0.01 <b>(+43.01%)</b></td><td>0.01 (+10.67%)</td><td>0.00 <b>(-24.17%)</b></td><td>559.40 (-9.64%)</td><td>386.26 (-10.36%)</td><td>367.10 <b>(-30.08%)</b></td><td>240.30 (+19.85%)</td><td>147.78 (-19.86%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.10 (n/a)</td><td>430.90 (n/a)</td><td>525.00 (n/a)</td><td>200.50 (n/a)</td><td>184.39 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (-14.81%)</td><td>0.02 (+12.46%)</td><td>0.02 <b>(+37.84%)</b></td><td>0.01 (+19.19%)</td><td>0.00 <b>(-40.72%)</b></td><td>456.50 (-16.10%)</td><td>325.78 (-16.92%)</td><td>304.80 <b>(-27.46%)</b></td><td>267.10 (+17.41%)</td><td>78.05 <b>(-41.32%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>544.10 (n/a)</td><td>392.14 (n/a)</td><td>420.20 (n/a)</td><td>227.50 (n/a)</td><td>133.01 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (-2.38%)</td><td>0.01 <b>(+34.82%)</b></td><td>0.02 <b>(+100.63%)</b></td><td>0.01 <b>(+22.39%)</b></td><td>0.00 (-15.47%)</td><td>513.60 (-18.28%)</td><td>309.56 <b>(-31.07%)</b></td><td>251.10 <b>(-50.15%)</b></td><td>219.30 (+2.48%)</td><td>124.87 <b>(-33.13%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.50 (n/a)</td><td>449.12 (n/a)</td><td>503.70 (n/a)</td><td>214.00 (n/a)</td><td>186.74 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (-3.04%)</td><td>0.01 (-18.82%)</td><td>0.01 <b>(-41.18%)</b></td><td>0.01 (+17.09%)</td><td>0.00 <b>(-22.59%)</b></td><td>548.00 (-14.59%)</td><td>443.30 (+14.48%)</td><td>467.90 <b>(+70.02%)</b></td><td>246.80 (+3.13%)</td><td>121.48 <b>(-33.04%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>641.60 (n/a)</td><td>387.22 (n/a)</td><td>275.20 (n/a)</td><td>239.30 (n/a)</td><td>181.43 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(+91.12%)</b></td><td>0.01 <b>(+101.89%)</b></td><td>0.01 <b>(+94.16%)</b></td><td>0.01 <b>(+315.32%)</b></td><td>0.00 <b>(+24.78%)</b></td><td>506.40 <b>(-75.92%)</b></td><td>346.68 <b>(-60.97%)</b></td><td>298.00 <b>(-48.50%)</b></td><td>239.20 <b>(-47.68%)</b></td><td>107.11 <b>(-84.55%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2103.30 (n/a)</td><td>888.20 (n/a)</td><td>578.60 (n/a)</td><td>457.20 (n/a)</td><td>693.24 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (+3.07%)</td><td>0.01 <b>(-22.59%)</b></td><td>0.01 <b>(-38.49%)</b></td><td>0.00 <b>(-71.95%)</b></td><td>0.01 <b>(+36.56%)</b></td><td>1890.40 <b>(+256.54%)</b></td><td>692.58 <b>(+89.52%)</b></td><td>462.20 <b>(+62.57%)</b></td><td>236.70 (-2.95%)</td><td>678.81 <b>(+409.44%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.20 (n/a)</td><td>365.44 (n/a)</td><td>284.30 (n/a)</td><td>243.90 (n/a)</td><td>133.25 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (+10.20%)</td><td>0.01 (+14.41%)</td><td>0.01 (-3.77%)</td><td>0.01 (-5.66%)</td><td>0.00 <b>(+39.55%)</b></td><td>635.90 (+6.00%)</td><td>409.74 (-7.03%)</td><td>454.90 (+3.91%)</td><td>236.10 (-9.23%)</td><td>163.47 <b>(+34.69%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.90 (n/a)</td><td>440.72 (n/a)</td><td>437.80 (n/a)</td><td>260.10 (n/a)</td><td>121.37 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 <b>(-45.50%)</b></td><td>0.01 <b>(-28.53%)</b></td><td>0.01 <b>(-31.36%)</b></td><td>0.01 (+0.76%)</td><td>0.00 <b>(-71.70%)</b></td><td>514.20 (-0.75%)</td><td>441.72 <b>(+26.23%)</b></td><td>427.20 <b>(+45.70%)</b></td><td>369.60 <b>(+83.52%)</b></td><td>67.83 <b>(-49.84%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>518.10 (n/a)</td><td>349.92 (n/a)</td><td>293.20 (n/a)</td><td>201.40 (n/a)</td><td>135.24 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.01 (-12.23%)</td><td>0.01 (-2.88%)</td><td>0.01 (-8.14%)</td><td>0.01 (-18.38%)</td><td>0.00 (+5.15%)</td><td>688.70 <b>(+22.50%)</b></td><td>487.88 (+7.69%)</td><td>539.10 (+8.87%)</td><td>282.70 (+13.95%)</td><td>184.81 <b>(+44.98%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.20 (n/a)</td><td>453.06 (n/a)</td><td>495.20 (n/a)</td><td>248.10 (n/a)</td><td>127.47 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 (+3.92%)</td><td>0.02 (-4.65%)</td><td>0.02 <b>(-32.24%)</b></td><td>0.02 (-5.99%)</td><td>0.01 <b>(+30.41%)</b></td><td>541.80 (+6.36%)</td><td>416.04 (+12.01%)</td><td>529.10 <b>(+47.59%)</b></td><td>225.30 (-3.76%)</td><td>163.71 <b>(+34.28%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>509.40 (n/a)</td><td>371.42 (n/a)</td><td>358.50 (n/a)</td><td>234.10 (n/a)</td><td>121.92 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (-7.92%)</td><td>0.03 <b>(-28.25%)</b></td><td>0.03 <b>(-46.84%)</b></td><td>0.02 (-10.03%)</td><td>0.01 (-15.17%)</td><td>611.50 (+11.16%)</td><td>457.10 <b>(+36.69%)</b></td><td>478.40 <b>(+88.12%)</b></td><td>255.80 (+8.57%)</td><td>128.03 (-3.95%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>550.10 (n/a)</td><td>334.40 (n/a)</td><td>254.30 (n/a)</td><td>235.60 (n/a)</td><td>133.29 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (-0.08%)</td><td>0.02 (+16.45%)</td><td>0.02 (+5.93%)</td><td>0.01 <b>(+309.94%)</b></td><td>0.01 <b>(-26.29%)</b></td><td>602.60 <b>(-75.61%)</b></td><td>433.72 <b>(-48.32%)</b></td><td>499.30 (-5.60%)</td><td>247.50 (+0.08%)</td><td>156.44 <b>(-83.11%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2470.30 (n/a)</td><td>839.22 (n/a)</td><td>528.90 (n/a)</td><td>247.30 (n/a)</td><td>926.47 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (-3.98%)</td><td>0.03 (+0.07%)</td><td>0.03 (-17.34%)</td><td>0.02 <b>(+27.83%)</b></td><td>0.01 <b>(-22.25%)</b></td><td>468.30 <b>(-21.77%)</b></td><td>334.42 (-9.45%)</td><td>303.40 <b>(+20.97%)</b></td><td>210.70 (+4.15%)</td><td>117.69 <b>(-37.94%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>598.60 (n/a)</td><td>369.34 (n/a)</td><td>250.80 (n/a)</td><td>202.30 (n/a)</td><td>189.63 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 <b>(+49.84%)</b></td><td>0.03 (+2.22%)</td><td>0.03 (-1.93%)</td><td>0.01 (-4.99%)</td><td>0.01 <b>(+94.23%)</b></td><td>593.80 (+5.25%)</td><td>369.06 (+10.50%)</td><td>295.90 (+1.96%)</td><td>163.40 <b>(-33.25%)</b></td><td>179.11 <b>(+36.24%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.20 (n/a)</td><td>334.00 (n/a)</td><td>290.20 (n/a)</td><td>244.80 (n/a)</td><td>131.47 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(-46.20%)</b></td><td>0.02 <b>(-51.75%)</b></td><td>0.02 <b>(-56.05%)</b></td><td>0.00 <b>(-77.47%)</b></td><td>0.01 <b>(-40.46%)</b></td><td>2462.40 <b>(+343.76%)</b></td><td>935.28 <b>(+164.65%)</b></td><td>568.80 <b>(+127.52%)</b></td><td>415.80 <b>(+85.87%)</b></td><td>859.88 <b>(+448.01%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>554.90 (n/a)</td><td>353.40 (n/a)</td><td>250.00 (n/a)</td><td>223.70 (n/a)</td><td>156.91 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 (+2.49%)</td><td>0.02 (+7.82%)</td><td>0.02 (+11.79%)</td><td>0.01 (-3.14%)</td><td>0.01 (+16.39%)</td><td>1079.30 (+3.24%)</td><td>554.02 (-4.24%)</td><td>427.40 (-10.55%)</td><td>413.70 (-2.43%)</td><td>293.79 (+12.12%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1045.40 (n/a)</td><td>578.58 (n/a)</td><td>477.80 (n/a)</td><td>424.00 (n/a)</td><td>262.03 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 (-15.64%)</td><td>0.02 (-17.87%)</td><td>0.02 (+8.93%)</td><td>0.01 <b>(-49.22%)</b></td><td>0.01 (-13.57%)</td><td>1055.10 <b>(+96.92%)</b></td><td>538.82 <b>(+30.98%)</b></td><td>411.20 (-8.19%)</td><td>315.20 (+18.54%)</td><td>296.17 <b>(+122.23%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.80 (n/a)</td><td>411.38 (n/a)</td><td>447.90 (n/a)</td><td>265.90 (n/a)</td><td>133.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.02 <b>(-24.44%)</b></td><td>0.02 (-18.09%)</td><td>0.02 <b>(-22.00%)</b></td><td>0.01 (-4.38%)</td><td>0.00 <b>(-53.15%)</b></td><td>547.10 (+4.57%)</td><td>460.34 (+18.03%)</td><td>471.50 <b>(+28.19%)</b></td><td>385.20 <b>(+32.33%)</b></td><td>63.33 <b>(-35.34%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.20 (n/a)</td><td>390.02 (n/a)</td><td>367.80 (n/a)</td><td>291.10 (n/a)</td><td>97.94 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.04 <b>(+81.74%)</b></td><td>0.03 <b>(+42.40%)</b></td><td>0.02 (+14.23%)</td><td>0.02 (+10.03%)</td><td>0.01 <b>(+281.40%)</b></td><td>560.50 (-9.11%)</td><td>413.40 <b>(-20.90%)</b></td><td>456.90 (-12.45%)</td><td>222.20 <b>(-44.97%)</b></td><td>155.57 <b>(+101.98%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.70 (n/a)</td><td>522.60 (n/a)</td><td>521.90 (n/a)</td><td>403.80 (n/a)</td><td>77.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.03 <b>(+29.44%)</b></td><td>0.02 <b>(+32.64%)</b></td><td>0.02 <b>(+30.81%)</b></td><td>0.01 <b>(+162.35%)</b></td><td>0.01 (+13.06%)</td><td>688.80 <b>(-61.89%)</b></td><td>470.38 <b>(-37.67%)</b></td><td>419.00 <b>(-23.57%)</b></td><td>249.30 <b>(-22.75%)</b></td><td>182.69 <b>(-69.43%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1807.20 (n/a)</td><td>754.66 (n/a)</td><td>548.20 (n/a)</td><td>322.70 (n/a)</td><td>597.65 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (+14.93%)</td><td>0.05 (+11.97%)</td><td>0.04 (+4.30%)</td><td>0.03 (+12.17%)</td><td>0.02 <b>(+20.44%)</b></td><td>534.10 (-10.85%)</td><td>383.28 (-9.13%)</td><td>455.60 (-4.12%)</td><td>209.60 (-12.99%)</td><td>147.40 (-5.43%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.10 (n/a)</td><td>421.78 (n/a)</td><td>475.20 (n/a)</td><td>240.90 (n/a)</td><td>155.87 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.10 (+16.17%)</td><td>0.09 <b>(+27.76%)</b></td><td>0.08 (+4.87%)</td><td>0.08 <b>(+99.40%)</b></td><td>0.01 <b>(-58.04%)</b></td><td>311.30 <b>(-49.85%)</b></td><td>287.30 <b>(-30.47%)</b></td><td>301.50 (-4.65%)</td><td>236.10 (-13.93%)</td><td>30.81 <b>(-82.03%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>620.70 (n/a)</td><td>413.22 (n/a)</td><td>316.20 (n/a)</td><td>274.30 (n/a)</td><td>171.48 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 <b>(+58.78%)</b></td><td>0.05 <b>(+77.99%)</b></td><td>0.05 <b>(+94.46%)</b></td><td>0.03 <b>(+279.35%)</b></td><td>0.02 (+19.28%)</td><td>551.70 <b>(-73.64%)</b></td><td>385.92 <b>(-55.86%)</b></td><td>303.50 <b>(-48.58%)</b></td><td>256.90 <b>(-37.00%)</b></td><td>142.03 <b>(-79.75%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2093.00 (n/a)</td><td>874.36 (n/a)</td><td>590.20 (n/a)</td><td>407.80 (n/a)</td><td>701.51 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 <b>(+55.29%)</b></td><td>0.05 <b>(+27.25%)</b></td><td>0.05 (+7.41%)</td><td>0.04 <b>(+21.10%)</b></td><td>0.02 <b>(+164.01%)</b></td><td>575.10 (-17.43%)</td><td>440.66 (-16.54%)</td><td>451.10 (-6.91%)</td><td>297.50 <b>(-35.59%)</b></td><td>137.15 <b>(+39.19%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>696.50 (n/a)</td><td>527.96 (n/a)</td><td>484.60 (n/a)</td><td>461.90 (n/a)</td><td>98.53 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (+0.84%)</td><td>0.04 <b>(+23.81%)</b></td><td>0.03 (-5.41%)</td><td>0.03 <b>(+265.61%)</b></td><td>0.02 <b>(-39.54%)</b></td><td>531.20 <b>(-72.65%)</b></td><td>432.54 <b>(-55.30%)</b></td><td>470.00 (+5.74%)</td><td>242.50 (-0.86%)</td><td>110.76 <b>(-86.89%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1942.20 (n/a)</td><td>967.74 (n/a)</td><td>444.50 (n/a)</td><td>244.60 (n/a)</td><td>844.78 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (+9.51%)</td><td>0.06 (+12.95%)</td><td>0.07 <b>(+30.09%)</b></td><td>0.03 (-7.34%)</td><td>0.02 (+7.16%)</td><td>628.30 (+7.94%)</td><td>380.38 (-10.70%)</td><td>314.90 <b>(-23.14%)</b></td><td>235.20 (-8.70%)</td><td>157.34 (+3.09%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>582.10 (n/a)</td><td>425.94 (n/a)</td><td>409.70 (n/a)</td><td>257.60 (n/a)</td><td>152.63 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 <b>(+20.96%)</b></td><td>0.04 (-17.60%)</td><td>0.03 <b>(-44.22%)</b></td><td>0.03 (-0.77%)</td><td>0.02 <b>(+46.39%)</b></td><td>617.40 (+0.78%)</td><td>495.36 <b>(+28.89%)</b></td><td>565.70 <b>(+79.30%)</b></td><td>212.50 (-17.35%)</td><td>162.66 (+12.75%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>612.60 (n/a)</td><td>384.32 (n/a)</td><td>315.50 (n/a)</td><td>257.10 (n/a)</td><td>144.26 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (-8.41%)</td><td>0.05 (-0.08%)</td><td>0.04 (+3.19%)</td><td>0.03 (+17.88%)</td><td>0.01 <b>(-31.52%)</b></td><td>536.50 (-15.18%)</td><td>418.14 (-4.83%)</td><td>423.30 (-3.11%)</td><td>292.50 (+9.18%)</td><td>89.65 <b>(-37.46%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>632.50 (n/a)</td><td>439.36 (n/a)</td><td>436.90 (n/a)</td><td>267.90 (n/a)</td><td>143.34 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (+3.96%)</td><td>0.04 (-0.23%)</td><td>0.04 (-12.55%)</td><td>0.03 <b>(+22.72%)</b></td><td>0.02 (-3.11%)</td><td>630.00 (-18.52%)</td><td>441.00 (-4.70%)</td><td>455.10 (+14.38%)</td><td>214.00 (-3.82%)</td><td>172.09 <b>(-24.99%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>773.20 (n/a)</td><td>462.74 (n/a)</td><td>397.90 (n/a)</td><td>222.50 (n/a)</td><td>229.41 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.06 (-8.07%)</td><td>0.05 (+4.17%)</td><td>0.04 (+9.38%)</td><td>0.03 (-13.62%)</td><td>0.02 (+2.38%)</td><td>640.50 (+15.78%)</td><td>443.48 (-2.75%)</td><td>481.90 (-8.58%)</td><td>298.10 (+8.80%)</td><td>145.26 (+15.73%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>553.20 (n/a)</td><td>456.00 (n/a)</td><td>527.10 (n/a)</td><td>274.00 (n/a)</td><td>125.51 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 (+9.92%)</td><td>0.04 <b>(+23.69%)</b></td><td>0.04 <b>(+33.19%)</b></td><td>0.03 <b>(+91.25%)</b></td><td>0.01 <b>(-35.38%)</b></td><td>538.30 <b>(-47.71%)</b></td><td>453.76 <b>(-26.55%)</b></td><td>465.30 <b>(-24.92%)</b></td><td>337.20 (-9.04%)</td><td>77.16 <b>(-69.87%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1029.40 (n/a)</td><td>617.82 (n/a)</td><td>619.70 (n/a)</td><td>370.70 (n/a)</td><td>256.06 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 <b>(+64.92%)</b></td><td>0.09 <b>(+36.39%)</b></td><td>0.08 <b>(+29.85%)</b></td><td>0.05 (+8.26%)</td><td>0.03 <b>(+149.02%)</b></td><td>640.00 (-7.63%)</td><td>407.02 <b>(-21.39%)</b></td><td>392.60 <b>(-22.99%)</b></td><td>254.60 <b>(-39.37%)</b></td><td>150.03 <b>(+38.83%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>692.90 (n/a)</td><td>517.78 (n/a)</td><td>509.80 (n/a)</td><td>419.90 (n/a)</td><td>108.07 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (-4.90%)</td><td>0.10 (+5.67%)</td><td>0.07 (+13.30%)</td><td>0.07 <b>(+25.72%)</b></td><td>0.04 (-14.23%)</td><td>480.60 <b>(-20.46%)</b></td><td>373.74 (-10.17%)</td><td>437.00 (-11.75%)</td><td>231.90 (+5.17%)</td><td>122.08 <b>(-26.16%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>604.20 (n/a)</td><td>416.04 (n/a)</td><td>495.20 (n/a)</td><td>220.50 (n/a)</td><td>165.32 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.16 (-4.22%)</td><td>0.12 (-7.62%)</td><td>0.11 <b>(-30.85%)</b></td><td>0.09 <b>(+26.39%)</b></td><td>0.03 <b>(-35.75%)</b></td><td>457.70 <b>(-20.88%)</b></td><td>374.14 (-0.90%)</td><td>389.90 <b>(+44.62%)</b></td><td>258.80 (+4.40%)</td><td>89.34 <b>(-45.47%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>578.50 (n/a)</td><td>377.54 (n/a)</td><td>269.60 (n/a)</td><td>247.90 (n/a)</td><td>163.82 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (+4.50%)</td><td>0.10 <b>(+74.59%)</b></td><td>0.11 <b>(+105.43%)</b></td><td>0.06 <b>(+338.88%)</b></td><td>0.04 <b>(-22.70%)</b></td><td>568.80 <b>(-77.22%)</b></td><td>372.80 <b>(-67.42%)</b></td><td>291.20 <b>(-51.32%)</b></td><td>242.80 (-4.30%)</td><td>154.25 <b>(-84.56%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2496.50 (n/a)</td><td>1144.38 (n/a)</td><td>598.20 (n/a)</td><td>253.70 (n/a)</td><td>999.15 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.16 <b>(+26.78%)</b></td><td>0.11 <b>(+31.05%)</b></td><td>0.08 (+8.44%)</td><td>0.08 <b>(+31.20%)</b></td><td>0.04 <b>(+61.90%)</b></td><td>523.10 <b>(-23.78%)</b></td><td>409.50 <b>(-20.23%)</b></td><td>484.30 (-7.77%)</td><td>249.40 <b>(-21.13%)</b></td><td>138.40 (+3.02%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>686.30 (n/a)</td><td>513.38 (n/a)</td><td>525.10 (n/a)</td><td>316.20 (n/a)</td><td>134.34 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 <b>(+66.30%)</b></td><td>0.11 <b>(+78.89%)</b></td><td>0.12 <b>(+84.52%)</b></td><td>0.08 <b>(+147.66%)</b></td><td>0.02 <b>(+23.70%)</b></td><td>434.70 <b>(-59.63%)</b></td><td>304.38 <b>(-48.20%)</b></td><td>267.10 <b>(-45.80%)</b></td><td>242.40 <b>(-39.85%)</b></td><td>78.15 <b>(-71.73%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1076.70 (n/a)</td><td>587.58 (n/a)</td><td>492.80 (n/a)</td><td>403.00 (n/a)</td><td>276.50 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 <b>(+43.47%)</b></td><td>0.09 <b>(+27.55%)</b></td><td>0.08 (+11.47%)</td><td>0.08 <b>(+29.92%)</b></td><td>0.02 <b>(+69.24%)</b></td><td>475.80 <b>(-23.02%)</b></td><td>410.32 <b>(-20.81%)</b></td><td>445.60 (-10.29%)</td><td>302.50 <b>(-30.30%)</b></td><td>73.53 (-9.29%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>618.10 (n/a)</td><td>518.12 (n/a)</td><td>496.70 (n/a)</td><td>434.00 (n/a)</td><td>81.06 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.16 (+8.46%)</td><td>0.11 (-5.76%)</td><td>0.12 (-10.93%)</td><td>0.07 (+17.02%)</td><td>0.04 (-1.29%)</td><td>492.10 (-14.54%)</td><td>325.06 (+3.04%)</td><td>278.90 (+12.28%)</td><td>204.20 (-7.81%)</td><td>114.55 <b>(-23.00%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>575.80 (n/a)</td><td>315.48 (n/a)</td><td>248.40 (n/a)</td><td>221.50 (n/a)</td><td>148.78 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.16 <b>(+89.71%)</b></td><td>0.07 <b>(+25.21%)</b></td><td>0.06 (+4.09%)</td><td>0.02 <b>(-45.55%)</b></td><td>0.05 <b>(+194.91%)</b></td><td>1913.50 <b>(+83.65%)</b></td><td>786.08 (+16.05%)</td><td>638.40 (-3.93%)</td><td>233.30 <b>(-47.29%)</b></td><td>654.59 <b>(+190.76%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>1041.90 (n/a)</td><td>677.34 (n/a)</td><td>664.50 (n/a)</td><td>442.60 (n/a)</td><td>225.13 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 <b>(+25.69%)</b></td><td>0.09 (+7.88%)</td><td>0.08 (-18.27%)</td><td>0.06 <b>(+38.91%)</b></td><td>0.03 (+9.48%)</td><td>526.20 <b>(-28.02%)</b></td><td>393.26 (-10.19%)</td><td>425.60 <b>(+22.33%)</b></td><td>244.70 <b>(-20.42%)</b></td><td>115.52 <b>(-36.13%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>731.00 (n/a)</td><td>437.88 (n/a)</td><td>347.90 (n/a)</td><td>307.50 (n/a)</td><td>180.86 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (-6.41%)</td><td>0.05 (-0.15%)</td><td>0.04 (+8.73%)</td><td>0.01 <b>(-56.60%)</b></td><td>0.03 (+19.58%)</td><td>1731.30 <b>(+130.44%)</b></td><td>653.20 <b>(+34.94%)</b></td><td>468.50 (-8.03%)</td><td>257.10 (+6.86%)</td><td>614.42 <b>(+206.07%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>751.30 (n/a)</td><td>484.06 (n/a)</td><td>509.40 (n/a)</td><td>240.60 (n/a)</td><td>200.75 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 <b>(-26.68%)</b></td><td>0.05 (-10.30%)</td><td>0.05 (+0.94%)</td><td>0.04 (+13.93%)</td><td>0.01 <b>(-50.32%)</b></td><td>539.90 (-12.23%)</td><td>434.80 (-0.49%)</td><td>447.50 (-0.91%)</td><td>294.80 <b>(+36.42%)</b></td><td>103.50 <b>(-42.34%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>615.10 (n/a)</td><td>436.94 (n/a)</td><td>451.60 (n/a)</td><td>216.10 (n/a)</td><td>179.51 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (-14.67%)</td><td>0.05 <b>(-26.35%)</b></td><td>0.04 <b>(-42.07%)</b></td><td>0.04 (-11.12%)</td><td>0.02 (-14.43%)</td><td>558.90 (+12.50%)</td><td>458.82 <b>(+35.32%)</b></td><td>515.70 <b>(+72.65%)</b></td><td>273.50 (+17.18%)</td><td>118.71 (+10.84%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>496.80 (n/a)</td><td>339.06 (n/a)</td><td>298.70 (n/a)</td><td>233.40 (n/a)</td><td>107.10 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (-9.01%)</td><td>0.05 (+10.25%)</td><td>0.04 (+19.56%)</td><td>0.03 <b>(+22.56%)</b></td><td>0.02 <b>(-25.74%)</b></td><td>593.10 (-18.41%)</td><td>430.04 (-16.04%)</td><td>473.70 (-16.35%)</td><td>248.80 (+9.89%)</td><td>130.59 <b>(-31.99%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>726.90 (n/a)</td><td>512.22 (n/a)</td><td>566.30 (n/a)</td><td>226.40 (n/a)</td><td>192.01 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (-1.90%)</td><td>0.05 (+0.36%)</td><td>0.04 <b>(-20.27%)</b></td><td>0.04 (+11.51%)</td><td>0.02 (-2.22%)</td><td>550.10 (-10.32%)</td><td>427.02 (-1.89%)</td><td>517.10 <b>(+25.42%)</b></td><td>236.40 (+1.94%)</td><td>149.14 (-12.25%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>613.40 (n/a)</td><td>435.26 (n/a)</td><td>412.30 (n/a)</td><td>231.90 (n/a)</td><td>169.95 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 <b>(+44.85%)</b></td><td>0.05 (+2.47%)</td><td>0.04 (-16.93%)</td><td>0.03 <b>(+61.13%)</b></td><td>0.02 <b>(+39.36%)</b></td><td>672.80 <b>(-37.94%)</b></td><td>519.96 (-5.72%)</td><td>581.30 <b>(+20.38%)</b></td><td>242.00 <b>(-30.98%)</b></td><td>167.24 <b>(-45.17%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1084.10 (n/a)</td><td>551.52 (n/a)</td><td>482.90 (n/a)</td><td>350.60 (n/a)</td><td>305.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 <b>(-44.76%)</b></td><td>0.05 <b>(-30.69%)</b></td><td>0.05 (-19.49%)</td><td>0.04 (-6.32%)</td><td>0.01 <b>(-65.69%)</b></td><td>602.70 (+6.75%)</td><td>506.94 <b>(+30.14%)</b></td><td>537.70 <b>(+24.21%)</b></td><td>370.50 <b>(+81.00%)</b></td><td>100.34 <b>(-31.81%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>564.60 (n/a)</td><td>389.54 (n/a)</td><td>432.90 (n/a)</td><td>204.70 (n/a)</td><td>147.14 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 (-11.53%)</td><td>0.06 (-12.63%)</td><td>0.05 (-3.96%)</td><td>0.05 (+3.75%)</td><td>0.02 <b>(-29.44%)</b></td><td>545.90 (-3.62%)</td><td>442.86 (+8.76%)</td><td>455.30 (+4.12%)</td><td>271.50 (+13.03%)</td><td>106.80 <b>(-24.91%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>566.40 (n/a)</td><td>407.20 (n/a)</td><td>437.30 (n/a)</td><td>240.20 (n/a)</td><td>142.22 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 <b>(-26.30%)</b></td><td>0.06 <b>(-23.96%)</b></td><td>0.05 (-16.53%)</td><td>0.05 (-2.25%)</td><td>0.02 <b>(-43.59%)</b></td><td>546.00 (+2.29%)</td><td>456.00 <b>(+20.83%)</b></td><td>486.70 (+19.82%)</td><td>267.50 <b>(+35.72%)</b></td><td>108.68 <b>(-26.99%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>533.80 (n/a)</td><td>377.40 (n/a)</td><td>406.20 (n/a)</td><td>197.10 (n/a)</td><td>148.86 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 <b>(-27.42%)</b></td><td>0.06 <b>(-23.54%)</b></td><td>0.06 <b>(-20.35%)</b></td><td>0.04 (-4.67%)</td><td>0.01 <b>(-45.12%)</b></td><td>575.40 (+4.89%)</td><td>440.20 <b>(+23.68%)</b></td><td>397.60 <b>(+25.54%)</b></td><td>322.20 <b>(+37.75%)</b></td><td>113.29 (-15.88%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>548.60 (n/a)</td><td>355.92 (n/a)</td><td>316.70 (n/a)</td><td>233.90 (n/a)</td><td>134.68 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 <b>(+60.29%)</b></td><td>0.06 (+17.55%)</td><td>0.06 (+5.70%)</td><td>0.01 <b>(-66.61%)</b></td><td>0.03 <b>(+328.56%)</b></td><td>1862.30 <b>(+199.50%)</b></td><td>673.08 <b>(+35.38%)</b></td><td>428.60 (-5.39%)</td><td>269.00 <b>(-37.62%)</b></td><td>673.28 <b>(+729.56%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>621.80 (n/a)</td><td>497.18 (n/a)</td><td>453.00 (n/a)</td><td>431.20 (n/a)</td><td>81.16 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (-18.86%)</td><td>0.06 (-0.44%)</td><td>0.06 <b>(+26.75%)</b></td><td>0.04 (+10.43%)</td><td>0.01 <b>(-44.13%)</b></td><td>573.50 (-9.44%)</td><td>444.84 (-6.96%)</td><td>431.40 <b>(-21.10%)</b></td><td>312.30 <b>(+23.24%)</b></td><td>99.67 <b>(-38.53%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>633.30 (n/a)</td><td>478.10 (n/a)</td><td>546.80 (n/a)</td><td>253.40 (n/a)</td><td>162.14 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.05 <b>(-26.26%)</b></td><td>0.04 (-9.01%)</td><td>0.04 (+5.21%)</td><td>0.04 (+14.27%)</td><td>0.00 <b>(-73.45%)</b></td><td>485.00 (-12.49%)</td><td>435.12 (+3.39%)</td><td>416.00 (-4.96%)</td><td>398.10 <b>(+35.59%)</b></td><td>38.28 <b>(-67.48%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>554.20 (n/a)</td><td>420.84 (n/a)</td><td>437.70 (n/a)</td><td>293.60 (n/a)</td><td>117.72 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 <b>(+24.38%)</b></td><td>0.04 <b>(-26.58%)</b></td><td>0.04 <b>(-35.30%)</b></td><td>0.01 <b>(-74.96%)</b></td><td>0.03 <b>(+125.49%)</b></td><td>1934.30 <b>(+299.40%)</b></td><td>716.18 <b>(+116.20%)</b></td><td>454.90 <b>(+54.57%)</b></td><td>218.30 (-19.59%)</td><td>693.91 <b>(+685.13%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>484.30 (n/a)</td><td>331.26 (n/a)</td><td>294.30 (n/a)</td><td>271.50 (n/a)</td><td>88.38 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 (-19.25%)</td><td>0.05 (-17.64%)</td><td>0.06 (-7.70%)</td><td>0.03 (-15.19%)</td><td>0.02 <b>(-24.76%)</b></td><td>604.00 (+17.90%)</td><td>404.66 (+19.71%)</td><td>319.10 (+8.32%)</td><td>277.20 <b>(+23.86%)</b></td><td>147.54 (+14.17%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>512.30 (n/a)</td><td>338.04 (n/a)</td><td>294.60 (n/a)</td><td>223.80 (n/a)</td><td>129.23 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 <b>(+40.26%)</b></td><td>0.05 <b>(+25.78%)</b></td><td>0.04 (+7.68%)</td><td>0.03 (-9.18%)</td><td>0.02 <b>(+112.55%)</b></td><td>647.60 (+10.10%)</td><td>412.20 (-11.17%)</td><td>436.40 (-7.13%)</td><td>217.30 <b>(-28.68%)</b></td><td>174.22 <b>(+69.21%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.20 (n/a)</td><td>464.02 (n/a)</td><td>469.90 (n/a)</td><td>304.70 (n/a)</td><td>102.96 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.07 <b>(-25.19%)</b></td><td>0.05 (-14.04%)</td><td>0.04 (-10.84%)</td><td>0.03 (-2.68%)</td><td>0.02 <b>(-28.23%)</b></td><td>615.00 (+2.76%)</td><td>449.30 (+12.44%)</td><td>479.40 (+12.17%)</td><td>275.00 <b>(+33.62%)</b></td><td>152.83 (-0.12%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>598.50 (n/a)</td><td>399.60 (n/a)</td><td>427.40 (n/a)</td><td>205.80 (n/a)</td><td>153.02 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (-4.29%)</td><td>0.05 (-2.20%)</td><td>0.04 <b>(-20.79%)</b></td><td>0.03 (+10.31%)</td><td>0.02 (-2.17%)</td><td>594.70 (-9.36%)</td><td>420.06 (+1.19%)</td><td>427.70 <b>(+26.24%)</b></td><td>226.50 (+4.52%)</td><td>165.02 (-7.71%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>656.10 (n/a)</td><td>415.10 (n/a)</td><td>338.80 (n/a)</td><td>216.70 (n/a)</td><td>178.80 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.37 <b>(-38.04%)</b></td><td>0.27 (+2.79%)</td><td>0.28 <b>(+60.06%)</b></td><td>0.17 <b>(+233.49%)</b></td><td>0.09 <b>(-58.96%)</b></td><td>576.40 <b>(-70.02%)</b></td><td>402.76 <b>(-44.39%)</b></td><td>350.00 <b>(-37.53%)</b></td><td>264.00 <b>(+61.37%)</b></td><td>140.60 <b>(-79.93%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.60 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>0.22 (n/a)</td><td>1922.30 (n/a)</td><td>724.24 (n/a)</td><td>560.30 (n/a)</td><td>163.60 (n/a)</td><td>700.55 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.34 (-6.82%)</td><td>0.30 <b>(+42.15%)</b></td><td>0.34 <b>(+84.65%)</b></td><td>0.18 (+19.36%)</td><td>0.07 <b>(-21.10%)</b></td><td>541.50 (-16.23%)</td><td>343.18 <b>(-32.09%)</b></td><td>292.20 <b>(-45.85%)</b></td><td>287.10 (+7.33%)</td><td>111.03 <b>(-22.89%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.37 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>646.40 (n/a)</td><td>505.32 (n/a)</td><td>539.60 (n/a)</td><td>267.50 (n/a)</td><td>143.98 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.38 <b>(+45.33%)</b></td><td>0.23 (+13.40%)</td><td>0.20 (+6.40%)</td><td>0.15 (-3.52%)</td><td>0.09 <b>(+86.34%)</b></td><td>667.90 (+3.65%)</td><td>475.10 (-6.97%)</td><td>488.00 (-6.03%)</td><td>259.10 <b>(-31.20%)</b></td><td>148.38 <b>(+26.12%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>644.40 (n/a)</td><td>510.70 (n/a)</td><td>519.30 (n/a)</td><td>376.60 (n/a)</td><td>117.65 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.25 (-11.90%)</td><td>0.19 (-6.49%)</td><td>0.17 (-18.14%)</td><td>0.14 <b>(+23.96%)</b></td><td>0.05 <b>(-33.27%)</b></td><td>525.40 (-19.33%)</td><td>416.32 (-0.87%)</td><td>423.90 <b>(+22.16%)</b></td><td>290.30 (+13.53%)</td><td>107.74 <b>(-38.55%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>651.30 (n/a)</td><td>419.98 (n/a)</td><td>347.00 (n/a)</td><td>255.70 (n/a)</td><td>175.33 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.27 <b>(-28.77%)</b></td><td>0.16 <b>(-36.12%)</b></td><td>0.14 <b>(-43.37%)</b></td><td>0.04 <b>(-72.62%)</b></td><td>0.09 (-14.14%)</td><td>1971.90 <b>(+265.23%)</b></td><td>738.04 <b>(+112.18%)</b></td><td>509.70 <b>(+76.61%)</b></td><td>269.50 <b>(+40.36%)</b></td><td>700.26 <b>(+364.83%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.38 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>539.90 (n/a)</td><td>347.84 (n/a)</td><td>288.60 (n/a)</td><td>192.00 (n/a)</td><td>150.65 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.26 (-3.68%)</td><td>0.17 (-18.54%)</td><td>0.16 <b>(-27.26%)</b></td><td>0.11 (-14.85%)</td><td>0.06 (-17.39%)</td><td>663.70 (+17.45%)</td><td>478.50 <b>(+20.24%)</b></td><td>471.20 <b>(+37.46%)</b></td><td>285.10 (+3.79%)</td><td>137.22 (-2.65%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>565.10 (n/a)</td><td>397.96 (n/a)</td><td>342.80 (n/a)</td><td>274.70 (n/a)</td><td>140.95 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (-3.89%)</td><td>0.10 (+6.16%)</td><td>0.08 (-0.48%)</td><td>0.07 <b>(+61.67%)</b></td><td>0.03 <b>(-20.14%)</b></td><td>496.80 <b>(-38.15%)</b></td><td>390.84 (-14.42%)</td><td>441.90 (+0.50%)</td><td>255.20 (+4.04%)</td><td>119.00 <b>(-46.88%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>803.20 (n/a)</td><td>456.70 (n/a)</td><td>439.70 (n/a)</td><td>245.30 (n/a)</td><td>224.00 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (-1.70%)</td><td>0.10 (-8.74%)</td><td>0.10 (-18.52%)</td><td>0.08 (-6.87%)</td><td>0.03 <b>(+35.86%)</b></td><td>480.90 (+7.37%)</td><td>374.34 (+12.90%)</td><td>382.20 <b>(+22.74%)</b></td><td>263.20 (+1.74%)</td><td>100.78 <b>(+43.33%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>447.90 (n/a)</td><td>331.58 (n/a)</td><td>311.40 (n/a)</td><td>258.70 (n/a)</td><td>70.32 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (-17.49%)</td><td>0.10 (-12.34%)</td><td>0.08 <b>(-30.45%)</b></td><td>0.07 (-4.26%)</td><td>0.03 (-17.94%)</td><td>508.80 (+4.45%)</td><td>388.92 (+12.14%)</td><td>435.80 <b>(+43.78%)</b></td><td>266.70 <b>(+21.17%)</b></td><td>109.59 (-4.27%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>487.10 (n/a)</td><td>346.82 (n/a)</td><td>303.10 (n/a)</td><td>220.10 (n/a)</td><td>114.47 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.13 (+1.72%)</td><td>0.10 (+19.99%)</td><td>0.08 (+3.89%)</td><td>0.07 <b>(+387.42%)</b></td><td>0.03 <b>(-41.77%)</b></td><td>512.10 <b>(-79.49%)</b></td><td>393.96 <b>(-52.12%)</b></td><td>442.20 (-3.72%)</td><td>274.60 (-1.68%)</td><td>102.60 <b>(-89.13%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2496.30 (n/a)</td><td>822.88 (n/a)</td><td>459.30 (n/a)</td><td>279.30 (n/a)</td><td>943.56 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 <b>(-31.66%)</b></td><td>0.08 (-16.07%)</td><td>0.08 <b>(-34.44%)</b></td><td>0.05 <b>(+264.73%)</b></td><td>0.02 <b>(-71.10%)</b></td><td>680.50 <b>(-72.58%)</b></td><td>479.58 <b>(-37.93%)</b></td><td>444.80 <b>(+52.54%)</b></td><td>400.10 <b>(+46.34%)</b></td><td>114.77 <b>(-88.07%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2482.00 (n/a)</td><td>772.64 (n/a)</td><td>291.60 (n/a)</td><td>273.40 (n/a)</td><td>961.62 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.18 (+18.52%)</td><td>0.08 <b>(-31.31%)</b></td><td>0.06 <b>(-49.85%)</b></td><td>0.02 <b>(-67.42%)</b></td><td>0.06 <b>(+51.13%)</b></td><td>2044.30 <b>(+206.91%)</b></td><td>806.92 <b>(+113.36%)</b></td><td>607.90 <b>(+99.38%)</b></td><td>206.40 (-15.65%)</td><td>712.89 <b>(+307.46%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>666.10 (n/a)</td><td>378.20 (n/a)</td><td>304.90 (n/a)</td><td>244.70 (n/a)</td><td>174.96 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.17 (-0.16%)</td><td>0.11 (+12.87%)</td><td>0.08 (+11.17%)</td><td>0.07 <b>(+26.84%)</b></td><td>0.05 (-6.35%)</td><td>613.10 <b>(-21.16%)</b></td><td>419.96 (-16.35%)</td><td>489.40 (-10.05%)</td><td>237.40 (+0.17%)</td><td>162.01 <b>(-28.18%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>777.70 (n/a)</td><td>502.02 (n/a)</td><td>544.10 (n/a)</td><td>237.00 (n/a)</td><td>225.58 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (-11.23%)</td><td>0.10 <b>(-23.33%)</b></td><td>0.09 <b>(-29.68%)</b></td><td>0.07 (-13.64%)</td><td>0.02 (-5.53%)</td><td>546.40 (+15.81%)</td><td>438.08 <b>(+30.66%)</b></td><td>446.40 <b>(+42.21%)</b></td><td>301.00 (+12.65%)</td><td>87.89 (+11.49%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>471.80 (n/a)</td><td>335.28 (n/a)</td><td>313.90 (n/a)</td><td>267.20 (n/a)</td><td>78.83 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.16 <b>(-21.61%)</b></td><td>0.11 (-9.42%)</td><td>0.09 (-12.97%)</td><td>0.06 <b>(-21.36%)</b></td><td>0.04 <b>(-20.81%)</b></td><td>636.20 <b>(+27.16%)</b></td><td>429.32 (+10.50%)</td><td>473.20 (+14.91%)</td><td>250.50 <b>(+27.55%)</b></td><td>155.86 <b>(+27.34%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>500.30 (n/a)</td><td>388.54 (n/a)</td><td>411.80 (n/a)</td><td>196.40 (n/a)</td><td>122.40 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.15 (+10.98%)</td><td>0.10 (-1.57%)</td><td>0.10 (+7.02%)</td><td>0.02 <b>(-64.71%)</b></td><td>0.05 <b>(+54.99%)</b></td><td>1778.50 <b>(+183.34%)</b></td><td>672.74 <b>(+45.63%)</b></td><td>428.20 (-6.57%)</td><td>273.60 (-9.88%)</td><td>632.65 <b>(+299.14%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>627.70 (n/a)</td><td>461.96 (n/a)</td><td>458.30 (n/a)</td><td>303.60 (n/a)</td><td>158.50 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.19 (-10.36%)</td><td>0.13 (+10.06%)</td><td>0.13 <b>(+31.36%)</b></td><td>0.08 <b>(+22.85%)</b></td><td>0.04 <b>(-32.98%)</b></td><td>490.30 (-18.60%)</td><td>332.42 (-18.00%)</td><td>324.60 <b>(-23.87%)</b></td><td>212.00 (+11.52%)</td><td>104.45 <b>(-39.24%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>602.30 (n/a)</td><td>405.40 (n/a)</td><td>426.40 (n/a)</td><td>190.10 (n/a)</td><td>171.93 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.10 <b>(-30.79%)</b></td><td>0.09 (-5.68%)</td><td>0.09 (+4.00%)</td><td>0.08 <b>(+21.58%)</b></td><td>0.01 <b>(-67.60%)</b></td><td>521.10 (-17.76%)</td><td>464.86 (+0.16%)</td><td>433.60 (-3.84%)</td><td>424.40 <b>(+44.45%)</b></td><td>49.91 <b>(-60.65%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>633.60 (n/a)</td><td>464.14 (n/a)</td><td>450.90 (n/a)</td><td>293.80 (n/a)</td><td>126.83 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (+2.17%)</td><td>0.09 (-0.39%)</td><td>0.08 (+0.17%)</td><td>0.03 <b>(-50.07%)</b></td><td>0.05 <b>(+57.35%)</b></td><td>1037.10 <b>(+100.29%)</b></td><td>511.04 <b>(+23.31%)</b></td><td>436.80 (-0.18%)</td><td>242.50 (-2.10%)</td><td>321.79 <b>(+220.51%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>517.80 (n/a)</td><td>414.44 (n/a)</td><td>437.60 (n/a)</td><td>247.70 (n/a)</td><td>100.40 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (-15.34%)</td><td>0.10 (-0.04%)</td><td>0.08 (+15.43%)</td><td>0.07 (+12.25%)</td><td>0.03 <b>(-37.59%)</b></td><td>482.30 (-10.92%)</td><td>384.62 (-7.15%)</td><td>426.50 (-13.37%)</td><td>254.90 (+18.12%)</td><td>90.68 <b>(-36.86%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>541.40 (n/a)</td><td>414.22 (n/a)</td><td>492.30 (n/a)</td><td>215.80 (n/a)</td><td>143.63 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.15 (-2.29%)</td><td>0.10 <b>(+41.92%)</b></td><td>0.08 (+16.19%)</td><td>0.06 <b>(+250.74%)</b></td><td>0.04 <b>(-29.23%)</b></td><td>547.90 <b>(-71.49%)</b></td><td>401.58 <b>(-59.43%)</b></td><td>422.60 (-13.93%)</td><td>233.90 (+2.32%)</td><td>147.42 <b>(-82.60%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1921.60 (n/a)</td><td>989.88 (n/a)</td><td>491.00 (n/a)</td><td>228.60 (n/a)</td><td>847.46 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (+12.37%)</td><td>0.10 (-3.23%)</td><td>0.11 (-7.70%)</td><td>0.05 <b>(-21.86%)</b></td><td>0.04 <b>(+25.81%)</b></td><td>752.10 <b>(+27.97%)</b></td><td>431.94 (+11.92%)</td><td>314.40 (+8.34%)</td><td>244.50 (-10.99%)</td><td>219.31 <b>(+49.32%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.70 (n/a)</td><td>385.92 (n/a)</td><td>290.20 (n/a)</td><td>274.70 (n/a)</td><td>146.87 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.18 <b>(+142.34%)</b></td><td>0.09 <b>(+37.90%)</b></td><td>0.07 (+7.82%)</td><td>0.07 (+15.11%)</td><td>0.05 <b>(+684.79%)</b></td><td>529.30 (-13.13%)</td><td>432.36 (-17.32%)</td><td>473.10 (-7.25%)</td><td>195.40 <b>(-58.74%)</b></td><td>135.33 <b>(+161.84%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>609.30 (n/a)</td><td>522.96 (n/a)</td><td>510.10 (n/a)</td><td>473.60 (n/a)</td><td>51.68 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.09 <b>(-50.70%)</b></td><td>0.07 <b>(-47.51%)</b></td><td>0.07 <b>(-52.18%)</b></td><td>0.06 (-4.63%)</td><td>0.01 <b>(-72.62%)</b></td><td>577.20 (+4.85%)</td><td>492.64 <b>(+68.65%)</b></td><td>522.40 <b>(+109.13%)</b></td><td>370.50 <b>(+102.79%)</b></td><td>78.46 <b>(-47.03%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>550.50 (n/a)</td><td>292.10 (n/a)</td><td>249.80 (n/a)</td><td>182.70 (n/a)</td><td>148.13 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.44 (-7.50%)</td><td>0.29 <b>(-27.67%)</b></td><td>0.30 <b>(-30.22%)</b></td><td>0.14 <b>(-41.84%)</b></td><td>0.11 <b>(+20.90%)</b></td><td>908.00 <b>(+71.94%)</b></td><td>518.12 <b>(+50.21%)</b></td><td>437.60 <b>(+43.33%)</b></td><td>296.60 (+8.09%)</td><td>236.21 <b>(+125.86%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.48 (n/a)</td><td>0.40 (n/a)</td><td>0.43 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>528.10 (n/a)</td><td>344.92 (n/a)</td><td>305.30 (n/a)</td><td>274.40 (n/a)</td><td>104.58 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.44 (-8.37%)</td><td>0.33 (-5.83%)</td><td>0.38 (+7.53%)</td><td>0.16 <b>(-26.69%)</b></td><td>0.13 (+17.56%)</td><td>797.10 <b>(+36.42%)</b></td><td>467.60 (+14.12%)</td><td>348.30 (-7.02%)</td><td>300.00 (+9.17%)</td><td>220.27 <b>(+66.41%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>584.30 (n/a)</td><td>409.74 (n/a)</td><td>374.60 (n/a)</td><td>274.80 (n/a)</td><td>132.37 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.46 (+2.03%)</td><td>0.31 (+9.18%)</td><td>0.32 <b>(+20.48%)</b></td><td>0.12 <b>(-24.65%)</b></td><td>0.13 (+16.47%)</td><td>1069.50 <b>(+32.71%)</b></td><td>520.62 (+0.35%)</td><td>409.90 (-16.99%)</td><td>282.90 (-2.01%)</td><td>318.92 <b>(+59.38%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.45 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>805.90 (n/a)</td><td>518.82 (n/a)</td><td>493.80 (n/a)</td><td>288.70 (n/a)</td><td>200.10 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+26.32%)</b></td><td>0.00 <b>(+66.67%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (-7.00%)</td><td>14035.81 <b>(-22.24%)</b></td><td>9627.90 <b>(-26.02%)</b></td><td>8532.56 <b>(-45.78%)</b></td><td>5870.03 (-4.22%)</td><td>3752.14 <b>(-25.24%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18051.22 (n/a)</td><td>13013.80 (n/a)</td><td>15737.41 (n/a)</td><td>6128.38 (n/a)</td><td>5018.61 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.00 <b>(+27.27%)</b></td><td>0.00 (+12.77%)</td><td>0.00 (-9.09%)</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+2.65%)</td><td>13827.01 <b>(-30.86%)</b></td><td>8505.76 (-16.21%)</td><td>7851.58 (+4.37%)</td><td>5918.64 <b>(-20.77%)</b></td><td>3137.80 <b>(-43.11%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19999.75 (n/a)</td><td>10150.68 (n/a)</td><td>7522.72 (n/a)</td><td>7470.09 (n/a)</td><td>5515.22 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (-0.90%)</td><td>0.10 (-0.62%)</td><td>0.08 (+11.55%)</td><td>0.07 (+11.00%)</td><td>0.03 <b>(-22.86%)</b></td><td>28090.42 (-9.86%)</td><td>23103.50 (-4.09%)</td><td>25865.94 (-10.34%)</td><td>14674.80 (+0.87%)</td><td>5502.74 <b>(-30.86%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>31163.29 (n/a)</td><td>24087.57 (n/a)</td><td>28847.96 (n/a)</td><td>14548.21 (n/a)</td><td>7959.40 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>2.68 (-0.79%)</td><td>1.70 (+3.65%)</td><td>1.40 (-7.74%)</td><td>1.35 <b>(+32.52%)</b></td><td>0.56 (-10.44%)</td><td>776.30 <b>(-24.54%)</b></td><td>658.26 (-6.53%)</td><td>747.70 (+8.39%)</td><td>391.20 (+0.80%)</td><td>161.47 <b>(-29.10%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>2.70 (n/a)</td><td>1.64 (n/a)</td><td>1.52 (n/a)</td><td>1.02 (n/a)</td><td>0.63 (n/a)</td><td>1028.80 (n/a)</td><td>704.28 (n/a)</td><td>689.80 (n/a)</td><td>388.10 (n/a)</td><td>227.73 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>2.55 <b>(-20.41%)</b></td><td>2.03 (+0.90%)</td><td>2.16 (+1.88%)</td><td>1.34 (+18.45%)</td><td>0.50 <b>(-37.56%)</b></td><td>784.10 (-15.57%)</td><td>545.36 (-7.81%)</td><td>484.90 (-1.84%)</td><td>410.80 <b>(+25.63%)</b></td><td>153.79 <b>(-34.94%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.21 (n/a)</td><td>2.02 (n/a)</td><td>2.12 (n/a)</td><td>1.13 (n/a)</td><td>0.80 (n/a)</td><td>928.70 (n/a)</td><td>591.58 (n/a)</td><td>494.00 (n/a)</td><td>327.00 (n/a)</td><td>236.41 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>2.77 (-8.03%)</td><td>1.63 (-1.71%)</td><td>1.39 (-12.49%)</td><td>0.50 <b>(+66.50%)</b></td><td>0.87 (-10.62%)</td><td>2086.70 <b>(-39.94%)</b></td><td>899.06 <b>(-21.68%)</b></td><td>754.20 (+14.27%)</td><td>379.00 (+8.72%)</td><td>687.11 <b>(-47.47%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.01 (n/a)</td><td>1.66 (n/a)</td><td>1.59 (n/a)</td><td>0.30 (n/a)</td><td>0.97 (n/a)</td><td>3474.20 (n/a)</td><td>1147.94 (n/a)</td><td>660.00 (n/a)</td><td>348.60 (n/a)</td><td>1308.08 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>3.42 (-2.09%)</td><td>2.61 (+7.24%)</td><td>2.81 (+18.36%)</td><td>1.43 (+19.40%)</td><td>0.74 (-15.01%)</td><td>733.80 (-16.25%)</td><td>438.68 (-10.83%)</td><td>373.40 (-15.52%)</td><td>307.00 (+2.13%)</td><td>170.01 <b>(-25.26%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.49 (n/a)</td><td>2.44 (n/a)</td><td>2.37 (n/a)</td><td>1.20 (n/a)</td><td>0.87 (n/a)</td><td>876.20 (n/a)</td><td>491.94 (n/a)</td><td>442.00 (n/a)</td><td>300.60 (n/a)</td><td>227.47 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>4.69 (+8.34%)</td><td>2.21 <b>(-35.61%)</b></td><td>2.02 <b>(-45.94%)</b></td><td>0.56 <b>(-77.57%)</b></td><td>1.77 <b>(+122.61%)</b></td><td>3730.40 <b>(+345.85%)</b></td><td>1883.40 <b>(+194.57%)</b></td><td>1038.70 <b>(+84.99%)</b></td><td>447.40 (-7.70%)</td><td>1616.72 <b>(+929.04%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>4.33 (n/a)</td><td>3.44 (n/a)</td><td>3.73 (n/a)</td><td>2.51 (n/a)</td><td>0.79 (n/a)</td><td>836.70 (n/a)</td><td>639.38 (n/a)</td><td>561.50 (n/a)</td><td>484.70 (n/a)</td><td>157.11 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.63 (-3.18%)</td><td>2.61 <b>(-25.13%)</b></td><td>2.57 <b>(-32.82%)</b></td><td>0.63 (+5.30%)</td><td>1.99 (+4.80%)</td><td>3333.50 (-5.04%)</td><td>1439.04 <b>(+28.38%)</b></td><td>816.70 <b>(+48.84%)</b></td><td>372.60 (+3.30%)</td><td>1231.58 (-8.12%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.81 (n/a)</td><td>3.49 (n/a)</td><td>3.82 (n/a)</td><td>0.60 (n/a)</td><td>1.90 (n/a)</td><td>3510.30 (n/a)</td><td>1120.90 (n/a)</td><td>548.70 (n/a)</td><td>360.70 (n/a)</td><td>1340.49 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>4.08 <b>(-23.31%)</b></td><td>3.12 (+0.49%)</td><td>3.40 (-0.17%)</td><td>1.54 <b>(+170.76%)</b></td><td>0.97 <b>(-43.82%)</b></td><td>1359.00 <b>(-63.07%)</b></td><td>755.24 <b>(-37.76%)</b></td><td>616.00 (+0.18%)</td><td>514.50 <b>(+30.39%)</b></td><td>344.47 <b>(-75.15%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.32 (n/a)</td><td>3.11 (n/a)</td><td>3.41 (n/a)</td><td>0.57 (n/a)</td><td>1.72 (n/a)</td><td>3679.80 (n/a)</td><td>1213.44 (n/a)</td><td>614.90 (n/a)</td><td>394.60 (n/a)</td><td>1385.99 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>7.13 <b>(+20.79%)</b></td><td>4.15 (+17.08%)</td><td>3.45 (-1.92%)</td><td>2.90 <b>(+378.78%)</b></td><td>1.75 (-11.89%)</td><td>722.50 <b>(-79.11%)</b></td><td>563.74 <b>(-49.30%)</b></td><td>608.00 (+1.95%)</td><td>294.20 (-17.22%)</td><td>176.30 <b>(-86.63%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.90 (n/a)</td><td>3.54 (n/a)</td><td>3.52 (n/a)</td><td>0.61 (n/a)</td><td>1.99 (n/a)</td><td>3459.30 (n/a)</td><td>1111.94 (n/a)</td><td>596.40 (n/a)</td><td>355.40 (n/a)</td><td>1319.00 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.14 (-16.70%)</td><td>3.53 <b>(+34.56%)</b></td><td>4.16 <b>(+137.44%)</b></td><td>0.60 (+1.13%)</td><td>1.79 <b>(-25.83%)</b></td><td>3516.50 (-1.12%)</td><td>1110.32 <b>(-38.57%)</b></td><td>504.50 <b>(-57.88%)</b></td><td>408.20 <b>(+20.02%)</b></td><td>1348.55 (-13.89%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>6.17 (n/a)</td><td>2.62 (n/a)</td><td>1.75 (n/a)</td><td>0.59 (n/a)</td><td>2.42 (n/a)</td><td>3556.20 (n/a)</td><td>1807.38 (n/a)</td><td>1197.90 (n/a)</td><td>340.10 (n/a)</td><td>1566.00 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>6.20 <b>(+58.57%)</b></td><td>2.44 (-13.03%)</td><td>1.92 <b>(-39.13%)</b></td><td>0.59 (-1.67%)</td><td>2.25 <b>(+76.08%)</b></td><td>3577.20 (+1.70%)</td><td>1636.40 <b>(+35.43%)</b></td><td>1094.50 <b>(+64.29%)</b></td><td>338.40 <b>(-36.94%)</b></td><td>1319.71 (+2.13%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.91 (n/a)</td><td>2.80 (n/a)</td><td>3.15 (n/a)</td><td>0.60 (n/a)</td><td>1.28 (n/a)</td><td>3517.40 (n/a)</td><td>1208.32 (n/a)</td><td>666.20 (n/a)</td><td>536.60 (n/a)</td><td>1292.14 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>5.89 (+16.19%)</td><td>2.70 <b>(-31.99%)</b></td><td>1.31 <b>(-65.30%)</b></td><td>1.18 <b>(-63.08%)</b></td><td>2.12 <b>(+172.29%)</b></td><td>3563.30 <b>(+170.87%)</b></td><td>2387.74 <b>(+119.22%)</b></td><td>3213.60 <b>(+188.19%)</b></td><td>712.00 (-13.94%)</td><td>1371.36 <b>(+578.90%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>5.07 (n/a)</td><td>3.97 (n/a)</td><td>3.76 (n/a)</td><td>3.19 (n/a)</td><td>0.78 (n/a)</td><td>1315.50 (n/a)</td><td>1089.22 (n/a)</td><td>1115.10 (n/a)</td><td>827.30 (n/a)</td><td>202.00 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>8.85 <b>(+20.59%)</b></td><td>5.95 (-7.40%)</td><td>4.98 <b>(-31.68%)</b></td><td>3.36 (-3.83%)</td><td>2.67 <b>(+60.82%)</b></td><td>1250.00 (+3.98%)</td><td>830.28 (+16.90%)</td><td>842.50 <b>(+46.37%)</b></td><td>474.10 (-17.07%)</td><td>354.30 <b>(+28.38%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>7.34 (n/a)</td><td>6.42 (n/a)</td><td>7.29 (n/a)</td><td>3.49 (n/a)</td><td>1.66 (n/a)</td><td>1202.10 (n/a)</td><td>710.26 (n/a)</td><td>575.60 (n/a)</td><td>571.70 (n/a)</td><td>275.97 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>8.63 (+3.37%)</td><td>5.99 (+14.48%)</td><td>6.00 (-0.27%)</td><td>3.12 <b>(+153.93%)</b></td><td>1.99 <b>(-27.60%)</b></td><td>1345.80 <b>(-60.62%)</b></td><td>782.94 <b>(-38.04%)</b></td><td>699.10 (+0.26%)</td><td>486.20 (-3.26%)</td><td>330.15 <b>(-72.99%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>8.35 (n/a)</td><td>5.23 (n/a)</td><td>6.02 (n/a)</td><td>1.23 (n/a)</td><td>2.75 (n/a)</td><td>3417.30 (n/a)</td><td>1263.66 (n/a)</td><td>697.30 (n/a)</td><td>502.60 (n/a)</td><td>1222.54 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>9.23 <b>(-24.47%)</b></td><td>7.99 <b>(+37.56%)</b></td><td>8.93 <b>(+112.93%)</b></td><td>6.27 <b>(+425.00%)</b></td><td>1.46 <b>(-65.58%)</b></td><td>668.90 <b>(-80.95%)</b></td><td>540.48 <b>(-58.34%)</b></td><td>469.50 <b>(-53.04%)</b></td><td>454.50 <b>(+32.39%)</b></td><td>105.58 <b>(-91.72%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>12.22 (n/a)</td><td>5.81 (n/a)</td><td>4.20 (n/a)</td><td>1.19 (n/a)</td><td>4.23 (n/a)</td><td>3511.50 (n/a)</td><td>1297.24 (n/a)</td><td>999.70 (n/a)</td><td>343.30 (n/a)</td><td>1274.57 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>7.19 <b>(-38.84%)</b></td><td>4.77 (-19.59%)</td><td>4.29 (-3.65%)</td><td>1.72 <b>(-56.04%)</b></td><td>2.18 <b>(-33.86%)</b></td><td>2442.00 <b>(+127.46%)</b></td><td>1132.86 <b>(+36.64%)</b></td><td>978.80 (+3.79%)</td><td>583.30 <b>(+63.53%)</b></td><td>757.22 <b>(+169.93%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>11.76 (n/a)</td><td>5.93 (n/a)</td><td>4.45 (n/a)</td><td>3.91 (n/a)</td><td>3.29 (n/a)</td><td>1073.60 (n/a)</td><td>829.08 (n/a)</td><td>943.10 (n/a)</td><td>356.70 (n/a)</td><td>280.52 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>9.87 (+16.93%)</td><td>7.71 <b>(+38.09%)</b></td><td>7.35 (+10.82%)</td><td>6.64 <b>(+244.56%)</b></td><td>1.28 <b>(-49.88%)</b></td><td>631.70 <b>(-70.98%)</b></td><td>555.04 <b>(-43.86%)</b></td><td>570.40 (-9.76%)</td><td>424.90 (-14.47%)</td><td>80.59 <b>(-88.36%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>8.44 (n/a)</td><td>5.58 (n/a)</td><td>6.64 (n/a)</td><td>1.93 (n/a)</td><td>2.56 (n/a)</td><td>2176.60 (n/a)</td><td>988.72 (n/a)</td><td>632.10 (n/a)</td><td>496.80 (n/a)</td><td>692.49 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>1.38 (-16.77%)</td><td>1.06 (-19.83%)</td><td>0.96 <b>(-36.36%)</b></td><td>0.77 (+1.60%)</td><td>0.24 <b>(-38.58%)</b></td><td>678.80 (-1.58%)</td><td>517.24 (+18.78%)</td><td>544.20 <b>(+57.15%)</b></td><td>380.10 <b>(+20.13%)</b></td><td>117.32 <b>(-26.87%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>1.66 (n/a)</td><td>1.32 (n/a)</td><td>1.51 (n/a)</td><td>0.76 (n/a)</td><td>0.39 (n/a)</td><td>689.70 (n/a)</td><td>435.46 (n/a)</td><td>346.30 (n/a)</td><td>316.40 (n/a)</td><td>160.42 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>2.52 (-17.78%)</td><td>1.31 <b>(-28.06%)</b></td><td>1.59 (-7.27%)</td><td>0.30 (-3.04%)</td><td>0.98 (-3.35%)</td><td>3545.50 (+3.14%)</td><td>1710.74 <b>(+56.65%)</b></td><td>660.80 (+7.83%)</td><td>416.10 <b>(+21.63%)</b></td><td>1593.16 <b>(+21.04%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>3.07 (n/a)</td><td>1.82 (n/a)</td><td>1.71 (n/a)</td><td>0.31 (n/a)</td><td>1.01 (n/a)</td><td>3437.70 (n/a)</td><td>1092.10 (n/a)</td><td>612.80 (n/a)</td><td>342.10 (n/a)</td><td>1316.21 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>4.50 (+2.87%)</td><td>2.32 (-19.21%)</td><td>2.46 (-12.40%)</td><td>0.56 <b>(-63.85%)</b></td><td>1.60 <b>(+38.72%)</b></td><td>3761.20 <b>(+176.60%)</b></td><td>1572.20 <b>(+86.91%)</b></td><td>854.20 (+14.15%)</td><td>466.20 (-2.79%)</td><td>1378.94 <b>(+284.25%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>4.37 (n/a)</td><td>2.87 (n/a)</td><td>2.80 (n/a)</td><td>1.54 (n/a)</td><td>1.15 (n/a)</td><td>1359.80 (n/a)</td><td>841.16 (n/a)</td><td>748.30 (n/a)</td><td>479.60 (n/a)</td><td>358.87 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>1.73 (+1.35%)</td><td>1.04 (-17.40%)</td><td>0.99 <b>(-26.24%)</b></td><td>0.69 (-11.19%)</td><td>0.41 (-2.22%)</td><td>764.80 (+12.59%)</td><td>554.22 <b>(+20.89%)</b></td><td>531.70 <b>(+35.57%)</b></td><td>303.00 (-1.34%)</td><td>170.88 (+3.57%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>1.71 (n/a)</td><td>1.26 (n/a)</td><td>1.34 (n/a)</td><td>0.77 (n/a)</td><td>0.41 (n/a)</td><td>679.30 (n/a)</td><td>458.44 (n/a)</td><td>392.20 (n/a)</td><td>307.10 (n/a)</td><td>165.00 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.12 (-19.13%)</td><td>0.09 (-14.44%)</td><td>0.09 (-16.58%)</td><td>0.05 (-8.06%)</td><td>0.03 (-3.14%)</td><td>606.80 (+8.77%)</td><td>422.44 (+19.45%)</td><td>370.30 (+19.84%)</td><td>279.00 <b>(+23.67%)</b></td><td>157.89 <b>(+25.70%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>557.90 (n/a)</td><td>353.66 (n/a)</td><td>309.00 (n/a)</td><td>225.60 (n/a)</td><td>125.61 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.14 (+14.55%)</td><td>0.09 <b>(+41.95%)</b></td><td>0.07 (+18.12%)</td><td>0.06 <b>(+370.81%)</b></td><td>0.03 <b>(-33.21%)</b></td><td>514.00 <b>(-78.76%)</b></td><td>392.12 <b>(-64.29%)</b></td><td>458.80 (-15.33%)</td><td>230.60 (-12.72%)</td><td>124.53 <b>(-87.77%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2420.00 (n/a)</td><td>1098.04 (n/a)</td><td>541.90 (n/a)</td><td>264.20 (n/a)</td><td>1017.97 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.25 (+13.36%)</td><td>0.18 (-0.56%)</td><td>0.15 <b>(-25.12%)</b></td><td>0.14 (+1.23%)</td><td>0.05 <b>(+40.25%)</b></td><td>485.40 (-1.22%)</td><td>389.44 (+3.41%)</td><td>434.20 <b>(+33.56%)</b></td><td>265.20 (-11.81%)</td><td>107.14 <b>(+22.18%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>491.40 (n/a)</td><td>376.60 (n/a)</td><td>325.10 (n/a)</td><td>300.70 (n/a)</td><td>87.69 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.26 (+13.51%)</td><td>0.23 <b>(+46.06%)</b></td><td>0.25 <b>(+60.37%)</b></td><td>0.13 <b>(+115.73%)</b></td><td>0.06 (-17.94%)</td><td>497.10 <b>(-53.64%)</b></td><td>311.18 <b>(-41.13%)</b></td><td>262.00 <b>(-37.65%)</b></td><td>248.60 (-11.91%)</td><td>105.93 <b>(-66.92%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>1072.30 (n/a)</td><td>528.58 (n/a)</td><td>420.20 (n/a)</td><td>282.20 (n/a)</td><td>320.24 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.27 (+16.97%)</td><td>0.18 (+9.31%)</td><td>0.13 (-8.02%)</td><td>0.11 <b>(+44.23%)</b></td><td>0.08 (+14.34%)</td><td>585.70 <b>(-30.67%)</b></td><td>430.66 (-10.45%)</td><td>523.50 (+8.72%)</td><td>241.40 (-14.49%)</td><td>164.05 <b>(-28.49%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>844.80 (n/a)</td><td>480.90 (n/a)</td><td>481.50 (n/a)</td><td>282.30 (n/a)</td><td>229.41 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.55 <b>(+33.55%)</b></td><td>0.42 <b>(+40.10%)</b></td><td>0.42 <b>(+59.11%)</b></td><td>0.26 <b>(+25.98%)</b></td><td>0.11 <b>(+32.68%)</b></td><td>501.20 <b>(-20.61%)</b></td><td>333.92 <b>(-28.29%)</b></td><td>310.40 <b>(-37.14%)</b></td><td>237.40 <b>(-25.13%)</b></td><td>103.73 (-18.12%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>631.30 (n/a)</td><td>465.64 (n/a)</td><td>493.80 (n/a)</td><td>317.10 (n/a)</td><td>126.68 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.57 (+6.62%)</td><td>0.33 (+12.16%)</td><td>0.28 <b>(+21.01%)</b></td><td>0.18 (-5.05%)</td><td>0.15 (+5.28%)</td><td>727.70 (+5.33%)</td><td>451.50 (-10.08%)</td><td>462.00 (-17.37%)</td><td>228.90 (-6.23%)</td><td>184.07 (+5.60%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.54 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>690.90 (n/a)</td><td>502.12 (n/a)</td><td>559.10 (n/a)</td><td>244.10 (n/a)</td><td>174.31 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.49 (+8.99%)</td><td>0.40 <b>(+38.09%)</b></td><td>0.43 <b>(+72.19%)</b></td><td>0.29 <b>(+35.48%)</b></td><td>0.08 <b>(-22.10%)</b></td><td>455.60 <b>(-26.18%)</b></td><td>340.76 <b>(-30.82%)</b></td><td>308.10 <b>(-41.91%)</b></td><td>267.30 (-8.27%)</td><td>73.46 <b>(-47.07%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.45 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>617.20 (n/a)</td><td>492.56 (n/a)</td><td>530.40 (n/a)</td><td>291.40 (n/a)</td><td>138.78 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:10:56</td><td>0.08 (+16.47%)</td><td>0.05 (+9.21%)</td><td>0.06 (+17.51%)</td><td>0.02 <b>(-39.90%)</b></td><td>0.02 <b>(+76.76%)</b></td><td>799.10 <b>(+66.41%)</b></td><td>385.92 (+8.89%)</td><td>259.90 (-14.90%)</td><td>213.00 (-14.15%)</td><td>244.59 <b>(+147.55%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:40:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>480.20 (n/a)</td><td>354.42 (n/a)</td><td>305.40 (n/a)</td><td>248.10 (n/a)</td><td>98.81 (n/a)</td>
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
