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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (+2.58%)</td><td>0.02 (+4.23%)</td><td>0.02 (-5.57%)</td><td>0.02 (+2.97%)</td><td>0.00 <b>(+22.21%)</b></td><td>324.50 (-2.87%)</td><td>263.70 (-3.22%)</td><td>285.20 (+5.90%)</td><td>207.10 (-2.50%)</td><td>51.45 (+11.98%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>334.10 (n/a)</td><td>272.46 (n/a)</td><td>269.30 (n/a)</td><td>212.40 (n/a)</td><td>45.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 <b>(+21.26%)</b></td><td>0.02 <b>(+40.33%)</b></td><td>0.02 <b>(+86.06%)</b></td><td>0.01 (+15.77%)</td><td>0.01 <b>(+30.76%)</b></td><td>523.40 (-13.62%)</td><td>360.22 <b>(-26.62%)</b></td><td>312.20 <b>(-46.25%)</b></td><td>206.50 (-17.50%)</td><td>152.07 (-2.92%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.90 (n/a)</td><td>490.88 (n/a)</td><td>580.80 (n/a)</td><td>250.30 (n/a)</td><td>156.64 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 <b>(+50.02%)</b></td><td>0.02 <b>(+43.16%)</b></td><td>0.02 <b>(+48.33%)</b></td><td>0.01 <b>(+191.97%)</b></td><td>0.01 <b>(+34.53%)</b></td><td>598.70 <b>(-65.75%)</b></td><td>368.76 <b>(-43.82%)</b></td><td>278.60 <b>(-32.59%)</b></td><td>180.00 <b>(-33.33%)</b></td><td>189.86 <b>(-69.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1748.00 (n/a)</td><td>656.40 (n/a)</td><td>413.30 (n/a)</td><td>270.00 (n/a)</td><td>618.66 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (-4.14%)</td><td>0.02 (-12.72%)</td><td>0.01 <b>(-35.61%)</b></td><td>0.01 (-15.32%)</td><td>0.01 (+7.83%)</td><td>611.10 (+18.11%)</td><td>428.84 (+17.62%)</td><td>485.90 <b>(+55.34%)</b></td><td>252.60 (+4.29%)</td><td>146.83 <b>(+25.42%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>517.40 (n/a)</td><td>364.60 (n/a)</td><td>312.80 (n/a)</td><td>242.20 (n/a)</td><td>117.07 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 <b>(+20.37%)</b></td><td>0.02 <b>(+26.83%)</b></td><td>0.02 <b>(+42.13%)</b></td><td>0.01 (-7.25%)</td><td>0.01 <b>(+49.01%)</b></td><td>551.90 (+7.81%)</td><td>331.22 (-17.63%)</td><td>282.50 <b>(-29.66%)</b></td><td>241.20 (-16.91%)</td><td>127.10 <b>(+38.53%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.90 (n/a)</td><td>402.12 (n/a)</td><td>401.60 (n/a)</td><td>290.30 (n/a)</td><td>91.75 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 <b>(-23.67%)</b></td><td>0.02 (-2.48%)</td><td>0.02 (+18.55%)</td><td>0.01 <b>(+23.66%)</b></td><td>0.00 <b>(-47.33%)</b></td><td>571.60 (-19.13%)</td><td>397.92 (-8.12%)</td><td>353.80 (-15.64%)</td><td>307.10 <b>(+31.02%)</b></td><td>110.08 <b>(-42.98%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>706.80 (n/a)</td><td>433.08 (n/a)</td><td>419.40 (n/a)</td><td>234.40 (n/a)</td><td>193.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (-15.19%)</td><td>0.04 (+4.03%)</td><td>0.04 (-6.00%)</td><td>0.02 <b>(+236.30%)</b></td><td>0.01 <b>(-45.93%)</b></td><td>582.00 <b>(-70.26%)</b></td><td>344.28 <b>(-44.54%)</b></td><td>293.00 (+6.39%)</td><td>247.30 (+17.87%)</td><td>135.83 <b>(-81.90%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1957.20 (n/a)</td><td>620.76 (n/a)</td><td>275.40 (n/a)</td><td>209.80 (n/a)</td><td>750.61 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 <b>(-26.89%)</b></td><td>0.04 <b>(-23.18%)</b></td><td>0.03 <b>(-32.83%)</b></td><td>0.03 (+8.71%)</td><td>0.01 <b>(-37.86%)</b></td><td>473.30 (-8.01%)</td><td>366.66 <b>(+22.74%)</b></td><td>396.50 <b>(+48.89%)</b></td><td>247.80 <b>(+36.75%)</b></td><td>91.67 <b>(-27.57%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>514.50 (n/a)</td><td>298.72 (n/a)</td><td>266.30 (n/a)</td><td>181.20 (n/a)</td><td>126.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 <b>(-29.88%)</b></td><td>0.04 (-18.19%)</td><td>0.04 (-8.58%)</td><td>0.02 (-7.46%)</td><td>0.01 <b>(-33.67%)</b></td><td>607.50 (+8.06%)</td><td>394.98 (+16.49%)</td><td>297.70 (+9.37%)</td><td>250.20 <b>(+42.65%)</b></td><td>160.95 (+1.74%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>562.20 (n/a)</td><td>339.06 (n/a)</td><td>272.20 (n/a)</td><td>175.40 (n/a)</td><td>158.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (+0.64%)</td><td>0.04 <b>(+29.39%)</b></td><td>0.04 <b>(+31.27%)</b></td><td>0.02 <b>(+243.76%)</b></td><td>0.01 <b>(-38.55%)</b></td><td>551.30 <b>(-70.91%)</b></td><td>335.48 <b>(-50.03%)</b></td><td>294.90 <b>(-23.84%)</b></td><td>242.90 (-0.65%)</td><td>122.70 <b>(-82.29%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1895.00 (n/a)</td><td>671.36 (n/a)</td><td>387.20 (n/a)</td><td>244.50 (n/a)</td><td>692.90 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 <b>(-43.93%)</b></td><td>0.02 <b>(-42.74%)</b></td><td>0.02 <b>(-49.74%)</b></td><td>0.01 <b>(-41.62%)</b></td><td>0.01 <b>(-49.81%)</b></td><td>1028.90 <b>(+71.31%)</b></td><td>643.68 <b>(+70.83%)</b></td><td>605.60 <b>(+98.95%)</b></td><td>429.50 <b>(+78.36%)</b></td><td>228.89 <b>(+57.22%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.60 (n/a)</td><td>376.80 (n/a)</td><td>304.40 (n/a)</td><td>240.80 (n/a)</td><td>145.58 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (-18.68%)</td><td>0.03 (-16.66%)</td><td>0.02 (-9.68%)</td><td>0.02 (+5.24%)</td><td>0.01 <b>(-49.68%)</b></td><td>576.40 (-4.98%)</td><td>487.72 (+11.06%)</td><td>521.30 (+10.73%)</td><td>338.30 <b>(+22.97%)</b></td><td>92.63 <b>(-40.20%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>606.60 (n/a)</td><td>439.14 (n/a)</td><td>470.80 (n/a)</td><td>275.10 (n/a)</td><td>154.91 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (+3.72%)</td><td>0.07 (-19.12%)</td><td>0.05 <b>(-41.42%)</b></td><td>0.04 (+9.53%)</td><td>0.03 (+9.63%)</td><td>559.10 (-8.70%)</td><td>416.14 <b>(+23.56%)</b></td><td>467.30 <b>(+70.67%)</b></td><td>236.10 (-3.55%)</td><td>141.49 (-8.63%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>612.40 (n/a)</td><td>336.80 (n/a)</td><td>273.80 (n/a)</td><td>244.80 (n/a)</td><td>154.85 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (+1.74%)</td><td>0.08 (-2.36%)</td><td>0.08 (-19.00%)</td><td>0.05 (-7.30%)</td><td>0.02 (-0.85%)</td><td>517.30 (+7.88%)</td><td>321.36 (+2.93%)</td><td>302.10 <b>(+23.46%)</b></td><td>234.30 (-1.72%)</td><td>115.29 (+9.48%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>479.50 (n/a)</td><td>312.20 (n/a)</td><td>244.70 (n/a)</td><td>238.40 (n/a)</td><td>105.31 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (-1.95%)</td><td>0.07 <b>(+22.83%)</b></td><td>0.07 <b>(+20.00%)</b></td><td>0.04 <b>(+284.46%)</b></td><td>0.02 <b>(-27.12%)</b></td><td>633.00 <b>(-73.99%)</b></td><td>408.38 <b>(-49.42%)</b></td><td>372.00 (-16.67%)</td><td>263.10 (+1.98%)</td><td>149.23 <b>(-83.66%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2433.70 (n/a)</td><td>807.34 (n/a)</td><td>446.40 (n/a)</td><td>258.00 (n/a)</td><td>913.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (-9.08%)</td><td>0.06 <b>(-20.61%)</b></td><td>0.05 (-19.04%)</td><td>0.04 (-14.25%)</td><td>0.02 (-4.48%)</td><td>588.60 (+16.62%)</td><td>473.70 <b>(+27.07%)</b></td><td>509.20 <b>(+23.50%)</b></td><td>265.40 (+9.99%)</td><td>123.71 (+17.55%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>504.70 (n/a)</td><td>372.78 (n/a)</td><td>412.30 (n/a)</td><td>241.30 (n/a)</td><td>105.24 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (-8.92%)</td><td>0.06 <b>(-23.52%)</b></td><td>0.05 <b>(-42.40%)</b></td><td>0.05 (+11.88%)</td><td>0.02 <b>(-29.26%)</b></td><td>540.20 (-10.62%)</td><td>464.34 <b>(+21.94%)</b></td><td>511.50 <b>(+73.63%)</b></td><td>266.20 (+9.77%)</td><td>113.18 <b>(-31.86%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>604.40 (n/a)</td><td>380.78 (n/a)</td><td>294.60 (n/a)</td><td>242.50 (n/a)</td><td>166.10 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 <b>(+61.50%)</b></td><td>0.08 (+12.39%)</td><td>0.05 (-14.50%)</td><td>0.05 (-12.24%)</td><td>0.04 <b>(+139.35%)</b></td><td>544.50 (+13.96%)</td><td>389.44 (+0.70%)</td><td>462.50 (+16.94%)</td><td>173.00 <b>(-38.06%)</b></td><td>150.51 <b>(+62.20%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>477.80 (n/a)</td><td>386.74 (n/a)</td><td>395.50 (n/a)</td><td>279.30 (n/a)</td><td>92.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.21 (+4.12%)</td><td>0.17 (-1.66%)</td><td>0.19 (+10.06%)</td><td>0.06 <b>(-40.70%)</b></td><td>0.06 <b>(+50.96%)</b></td><td>810.00 <b>(+68.64%)</b></td><td>368.52 (+18.88%)</td><td>264.80 (-9.13%)</td><td>231.20 (-3.95%)</td><td>248.16 <b>(+152.39%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>480.30 (n/a)</td><td>310.00 (n/a)</td><td>291.40 (n/a)</td><td>240.70 (n/a)</td><td>98.32 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.17 (-0.16%)</td><td>0.11 (-13.04%)</td><td>0.09 <b>(-24.23%)</b></td><td>0.08 (-15.26%)</td><td>0.04 (+11.64%)</td><td>620.70 (+18.00%)</td><td>479.00 (+18.56%)</td><td>561.70 <b>(+31.98%)</b></td><td>287.90 (+0.17%)</td><td>147.11 <b>(+37.24%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>526.00 (n/a)</td><td>404.02 (n/a)</td><td>425.60 (n/a)</td><td>287.40 (n/a)</td><td>107.19 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.20 (+3.89%)</td><td>0.12 (-4.12%)</td><td>0.10 (+6.91%)</td><td>0.09 (+19.71%)</td><td>0.04 (-18.19%)</td><td>543.30 (-16.47%)</td><td>453.92 (-2.37%)</td><td>496.30 (-6.46%)</td><td>251.90 (-3.74%)</td><td>115.30 <b>(-36.00%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>650.40 (n/a)</td><td>464.94 (n/a)</td><td>530.60 (n/a)</td><td>261.70 (n/a)</td><td>180.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.21 <b>(+27.47%)</b></td><td>0.14 (-4.96%)</td><td>0.11 <b>(-27.15%)</b></td><td>0.07 <b>(-32.29%)</b></td><td>0.07 <b>(+168.60%)</b></td><td>663.40 <b>(+47.68%)</b></td><td>432.74 <b>(+24.19%)</b></td><td>427.50 <b>(+37.28%)</b></td><td>230.00 <b>(-21.56%)</b></td><td>199.66 <b>(+201.02%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>449.20 (n/a)</td><td>348.46 (n/a)</td><td>311.40 (n/a)</td><td>293.20 (n/a)</td><td>66.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.23 (-12.46%)</td><td>0.14 (-7.73%)</td><td>0.11 <b>(-22.96%)</b></td><td>0.10 (+5.11%)</td><td>0.06 (-14.77%)</td><td>498.70 (-4.86%)</td><td>389.28 (+6.60%)</td><td>466.90 <b>(+29.80%)</b></td><td>210.10 (+14.25%)</td><td>126.82 (-2.01%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>524.20 (n/a)</td><td>365.18 (n/a)</td><td>359.70 (n/a)</td><td>183.90 (n/a)</td><td>129.42 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.18 (-17.64%)</td><td>0.12 (-13.33%)</td><td>0.10 (-16.16%)</td><td>0.08 (-13.95%)</td><td>0.04 (-16.53%)</td><td>623.50 (+16.22%)</td><td>464.92 (+15.22%)</td><td>481.30 (+19.25%)</td><td>271.00 <b>(+21.42%)</b></td><td>159.30 (+16.72%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>536.50 (n/a)</td><td>403.50 (n/a)</td><td>403.60 (n/a)</td><td>223.20 (n/a)</td><td>136.48 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (-0.38%)</td><td>0.01 (+0.43%)</td><td>0.01 (+7.42%)</td><td>0.00 (+5.31%)</td><td>0.00 (-3.90%)</td><td>532.50 (-5.05%)</td><td>432.20 (-1.04%)</td><td>452.60 (-6.91%)</td><td>276.30 (+0.36%)</td><td>105.49 (-6.34%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>560.80 (n/a)</td><td>436.74 (n/a)</td><td>486.20 (n/a)</td><td>275.30 (n/a)</td><td>112.64 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (-14.98%)</td><td>0.01 (-12.86%)</td><td>0.01 <b>(-21.21%)</b></td><td>0.01 (+12.79%)</td><td>0.00 <b>(-32.87%)</b></td><td>510.70 (-11.35%)</td><td>367.22 (+5.36%)</td><td>342.10 <b>(+26.94%)</b></td><td>232.10 (+17.64%)</td><td>115.86 <b>(-29.87%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>576.10 (n/a)</td><td>348.54 (n/a)</td><td>269.50 (n/a)</td><td>197.30 (n/a)</td><td>165.21 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (-11.71%)</td><td>0.01 (+16.32%)</td><td>0.01 <b>(+74.64%)</b></td><td>0.00 (-11.16%)</td><td>0.00 (-1.53%)</td><td>671.60 (+12.57%)</td><td>402.58 (-11.98%)</td><td>289.30 <b>(-42.74%)</b></td><td>261.40 (+13.26%)</td><td>185.17 <b>(+20.18%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>596.60 (n/a)</td><td>457.36 (n/a)</td><td>505.20 (n/a)</td><td>230.80 (n/a)</td><td>154.08 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (-12.43%)</td><td>0.01 <b>(+23.94%)</b></td><td>0.01 <b>(+73.77%)</b></td><td>0.01 (+19.31%)</td><td>0.00 <b>(-37.82%)</b></td><td>488.20 (-16.19%)</td><td>320.26 <b>(-25.53%)</b></td><td>290.00 <b>(-42.45%)</b></td><td>252.40 (+14.21%)</td><td>95.81 <b>(-38.16%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>582.50 (n/a)</td><td>430.08 (n/a)</td><td>503.90 (n/a)</td><td>221.00 (n/a)</td><td>154.92 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (-2.05%)</td><td>0.01 (-6.44%)</td><td>0.01 (+3.17%)</td><td>0.00 (-16.22%)</td><td>0.00 <b>(+20.23%)</b></td><td>705.70 (+19.37%)</td><td>409.82 (+12.32%)</td><td>320.40 (-3.06%)</td><td>258.50 (+2.09%)</td><td>181.97 <b>(+39.37%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>591.20 (n/a)</td><td>364.88 (n/a)</td><td>330.50 (n/a)</td><td>253.20 (n/a)</td><td>130.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (+6.13%)</td><td>0.01 (-1.97%)</td><td>0.00 (-7.93%)</td><td>0.00 (+0.94%)</td><td>0.00 (+11.82%)</td><td>603.40 (-0.92%)</td><td>487.84 (+3.36%)</td><td>559.00 (+8.61%)</td><td>241.70 (-5.77%)</td><td>146.65 (+0.72%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>609.00 (n/a)</td><td>471.98 (n/a)</td><td>514.70 (n/a)</td><td>256.50 (n/a)</td><td>145.60 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 <b>(-22.44%)</b></td><td>0.02 (-13.93%)</td><td>0.02 (-2.09%)</td><td>0.01 (-2.03%)</td><td>0.00 <b>(-23.07%)</b></td><td>593.00 (+2.07%)</td><td>382.08 (+13.30%)</td><td>298.50 (+2.12%)</td><td>252.70 <b>(+28.93%)</b></td><td>144.17 (-1.80%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.00 (n/a)</td><td>337.22 (n/a)</td><td>292.30 (n/a)</td><td>196.00 (n/a)</td><td>146.82 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+0.19%)</td><td>0.01 (-6.98%)</td><td>0.02 (-2.08%)</td><td>0.00 <b>(-54.24%)</b></td><td>0.01 <b>(+49.11%)</b></td><td>1132.20 <b>(+118.53%)</b></td><td>490.72 <b>(+35.63%)</b></td><td>300.00 (+2.11%)</td><td>253.80 (-0.16%)</td><td>372.16 <b>(+217.73%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.10 (n/a)</td><td>361.80 (n/a)</td><td>293.80 (n/a)</td><td>254.20 (n/a)</td><td>117.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 <b>(+39.93%)</b></td><td>0.02 <b>(+45.66%)</b></td><td>0.02 <b>(+69.82%)</b></td><td>0.01 (+14.04%)</td><td>0.00 <b>(+110.57%)</b></td><td>515.90 (-12.32%)</td><td>342.86 <b>(-28.10%)</b></td><td>274.90 <b>(-41.11%)</b></td><td>260.20 <b>(-28.54%)</b></td><td>112.90 <b>(+26.95%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.40 (n/a)</td><td>476.86 (n/a)</td><td>466.80 (n/a)</td><td>364.10 (n/a)</td><td>88.93 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 <b>(+32.14%)</b></td><td>0.01 <b>(+24.16%)</b></td><td>0.01 (-3.54%)</td><td>0.01 <b>(+97.38%)</b></td><td>0.01 <b>(+22.17%)</b></td><td>542.60 <b>(-49.33%)</b></td><td>411.04 <b>(-25.17%)</b></td><td>465.60 (+3.67%)</td><td>233.70 <b>(-24.32%)</b></td><td>128.49 <b>(-57.20%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1070.90 (n/a)</td><td>549.32 (n/a)</td><td>449.10 (n/a)</td><td>308.80 (n/a)</td><td>300.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 <b>(+40.22%)</b></td><td>0.02 <b>(+34.51%)</b></td><td>0.02 <b>(+51.82%)</b></td><td>0.01 (+2.08%)</td><td>0.00 <b>(+148.44%)</b></td><td>595.60 (-2.04%)</td><td>374.88 <b>(-20.18%)</b></td><td>293.70 <b>(-34.13%)</b></td><td>272.30 <b>(-28.70%)</b></td><td>141.10 <b>(+64.10%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.00 (n/a)</td><td>469.68 (n/a)</td><td>445.90 (n/a)</td><td>381.90 (n/a)</td><td>85.98 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 <b>(-52.07%)</b></td><td>0.01 <b>(-29.36%)</b></td><td>0.01 <b>(-21.72%)</b></td><td>0.01 (+10.24%)</td><td>0.00 <b>(-68.24%)</b></td><td>796.40 (-9.28%)</td><td>517.40 (+11.36%)</td><td>479.00 <b>(+27.77%)</b></td><td>362.90 <b>(+108.68%)</b></td><td>170.57 <b>(-39.63%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>877.90 (n/a)</td><td>464.62 (n/a)</td><td>374.90 (n/a)</td><td>173.90 (n/a)</td><td>282.53 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (+9.17%)</td><td>0.03 (-16.66%)</td><td>0.03 (-0.23%)</td><td>0.00 <b>(-83.58%)</b></td><td>0.01 <b>(+223.37%)</b></td><td>2434.40 <b>(+509.06%)</b></td><td>749.32 <b>(+131.64%)</b></td><td>319.10 (+0.22%)</td><td>252.50 (-8.41%)</td><td>944.41 <b>(+1894.42%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>399.70 (n/a)</td><td>323.48 (n/a)</td><td>318.40 (n/a)</td><td>275.70 (n/a)</td><td>47.35 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (-4.24%)</td><td>0.03 (-5.45%)</td><td>0.02 <b>(-26.27%)</b></td><td>0.02 <b>(+36.17%)</b></td><td>0.01 (-13.81%)</td><td>546.20 <b>(-26.57%)</b></td><td>403.48 (-1.15%)</td><td>448.60 <b>(+35.65%)</b></td><td>242.70 (+4.43%)</td><td>132.27 <b>(-35.82%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>743.80 (n/a)</td><td>408.18 (n/a)</td><td>330.70 (n/a)</td><td>232.40 (n/a)</td><td>206.09 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (-10.21%)</td><td>0.03 (+4.24%)</td><td>0.04 (+4.86%)</td><td>0.02 (-2.00%)</td><td>0.01 <b>(-22.40%)</b></td><td>522.70 (+2.03%)</td><td>324.76 (-6.47%)</td><td>282.50 (-4.63%)</td><td>259.10 (+11.35%)</td><td>111.18 (-8.64%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.30 (n/a)</td><td>347.24 (n/a)</td><td>296.20 (n/a)</td><td>232.70 (n/a)</td><td>121.70 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (+9.78%)</td><td>0.03 <b>(+26.02%)</b></td><td>0.03 <b>(+22.00%)</b></td><td>0.02 <b>(+72.27%)</b></td><td>0.01 <b>(-27.94%)</b></td><td>450.90 <b>(-41.95%)</b></td><td>377.48 <b>(-25.43%)</b></td><td>354.20 (-18.03%)</td><td>301.50 (-8.88%)</td><td>68.41 <b>(-61.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>776.80 (n/a)</td><td>506.24 (n/a)</td><td>432.10 (n/a)</td><td>330.90 (n/a)</td><td>176.84 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 <b>(-33.67%)</b></td><td>0.02 <b>(-30.80%)</b></td><td>0.02 <b>(-41.29%)</b></td><td>0.02 (-8.08%)</td><td>0.00 <b>(-62.40%)</b></td><td>633.50 (+8.79%)</td><td>516.52 <b>(+34.13%)</b></td><td>493.20 <b>(+70.30%)</b></td><td>415.00 <b>(+50.74%)</b></td><td>91.70 <b>(-35.92%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>582.30 (n/a)</td><td>385.10 (n/a)</td><td>289.60 (n/a)</td><td>275.30 (n/a)</td><td>143.11 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 <b>(+26.40%)</b></td><td>0.03 <b>(+60.19%)</b></td><td>0.03 <b>(+94.05%)</b></td><td>0.02 <b>(+47.37%)</b></td><td>0.01 (-1.88%)</td><td>463.80 <b>(-32.14%)</b></td><td>327.10 <b>(-39.57%)</b></td><td>313.90 <b>(-48.46%)</b></td><td>253.80 <b>(-20.89%)</b></td><td>80.93 <b>(-44.08%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>683.50 (n/a)</td><td>541.32 (n/a)</td><td>609.10 (n/a)</td><td>320.80 (n/a)</td><td>144.72 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (+12.58%)</td><td>0.07 (+9.80%)</td><td>0.07 (+1.84%)</td><td>0.04 (-2.61%)</td><td>0.02 (+6.89%)</td><td>537.40 (+2.69%)</td><td>335.92 (-8.38%)</td><td>300.80 (-1.80%)</td><td>239.10 (-11.18%)</td><td>116.89 (+3.71%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>523.30 (n/a)</td><td>366.66 (n/a)</td><td>306.30 (n/a)</td><td>269.20 (n/a)</td><td>112.71 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (-4.08%)</td><td>0.06 (+3.39%)</td><td>0.07 <b>(+32.20%)</b></td><td>0.03 (-0.91%)</td><td>0.02 (+7.37%)</td><td>640.20 (+0.93%)</td><td>381.00 (-1.25%)</td><td>282.70 <b>(-24.37%)</b></td><td>254.30 (+4.26%)</td><td>166.81 (+9.33%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>634.30 (n/a)</td><td>385.84 (n/a)</td><td>373.80 (n/a)</td><td>243.90 (n/a)</td><td>152.58 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (-3.65%)</td><td>0.04 <b>(-26.98%)</b></td><td>0.04 <b>(-36.98%)</b></td><td>0.01 (-2.44%)</td><td>0.02 (-17.66%)</td><td>1951.50 (+2.49%)</td><td>783.86 <b>(+20.18%)</b></td><td>541.70 <b>(+58.72%)</b></td><td>289.20 (+3.77%)</td><td>663.77 (-5.65%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1904.00 (n/a)</td><td>652.26 (n/a)</td><td>341.30 (n/a)</td><td>278.70 (n/a)</td><td>703.53 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (+6.49%)</td><td>0.05 (-12.11%)</td><td>0.04 (-11.28%)</td><td>0.03 <b>(-23.93%)</b></td><td>0.02 (+19.59%)</td><td>749.20 <b>(+31.46%)</b></td><td>482.94 (+18.71%)</td><td>473.90 (+12.73%)</td><td>268.90 (-6.11%)</td><td>172.61 <b>(+49.86%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>569.90 (n/a)</td><td>406.84 (n/a)</td><td>420.40 (n/a)</td><td>286.40 (n/a)</td><td>115.18 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 <b>(-21.80%)</b></td><td>0.07 (+2.26%)</td><td>0.07 <b>(+27.49%)</b></td><td>0.05 <b>(+40.30%)</b></td><td>0.01 <b>(-59.89%)</b></td><td>428.90 <b>(-28.72%)</b></td><td>325.14 (-12.24%)</td><td>300.70 <b>(-21.55%)</b></td><td>284.50 <b>(+27.87%)</b></td><td>59.61 <b>(-60.93%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>601.70 (n/a)</td><td>370.50 (n/a)</td><td>383.30 (n/a)</td><td>222.50 (n/a)</td><td>152.58 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (+0.36%)</td><td>0.05 (-15.61%)</td><td>0.04 <b>(-26.96%)</b></td><td>0.03 (-2.99%)</td><td>0.02 (+2.77%)</td><td>671.30 (+3.09%)</td><td>500.82 (+18.57%)</td><td>508.90 <b>(+36.91%)</b></td><td>287.70 (-0.35%)</td><td>141.84 (-1.43%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>651.20 (n/a)</td><td>422.38 (n/a)</td><td>371.70 (n/a)</td><td>288.70 (n/a)</td><td>143.90 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>477.40 (n/a)</td><td>384.12 (n/a)</td><td>387.00 (n/a)</td><td>285.90 (n/a)</td><td>90.36 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.40 (n/a)</td><td>368.44 (n/a)</td><td>298.60 (n/a)</td><td>237.40 (n/a)</td><td>157.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.30 (n/a)</td><td>444.92 (n/a)</td><td>473.90 (n/a)</td><td>243.80 (n/a)</td><td>117.98 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>547.50 (n/a)</td><td>390.70 (n/a)</td><td>394.10 (n/a)</td><td>271.10 (n/a)</td><td>111.97 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.00 (n/a)</td><td>411.48 (n/a)</td><td>465.70 (n/a)</td><td>286.60 (n/a)</td><td>114.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>583.80 (n/a)</td><td>463.30 (n/a)</td><td>508.00 (n/a)</td><td>191.20 (n/a)</td><td>155.68 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>559.50 (n/a)</td><td>431.30 (n/a)</td><td>457.90 (n/a)</td><td>273.30 (n/a)</td><td>115.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>537.40 (n/a)</td><td>373.72 (n/a)</td><td>325.50 (n/a)</td><td>264.00 (n/a)</td><td>115.66 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>632.00 (n/a)</td><td>432.00 (n/a)</td><td>486.70 (n/a)</td><td>227.50 (n/a)</td><td>168.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.24 (+17.54%)</td><td>0.15 (-9.63%)</td><td>0.13 (-19.98%)</td><td>0.08 <b>(-24.47%)</b></td><td>0.07 <b>(+76.50%)</b></td><td>624.10 <b>(+32.39%)</b></td><td>413.18 <b>(+27.57%)</b></td><td>386.70 <b>(+24.94%)</b></td><td>207.20 (-14.91%)</td><td>196.16 <b>(+110.72%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>471.40 (n/a)</td><td>323.88 (n/a)</td><td>309.50 (n/a)</td><td>243.50 (n/a)</td><td>93.09 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>670.40 (n/a)</td><td>480.80 (n/a)</td><td>564.20 (n/a)</td><td>275.00 (n/a)</td><td>188.48 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>687.80 (n/a)</td><td>538.04 (n/a)</td><td>602.20 (n/a)</td><td>251.10 (n/a)</td><td>181.64 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.80 (n/a)</td><td>460.58 (n/a)</td><td>493.00 (n/a)</td><td>244.60 (n/a)</td><td>144.37 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.40 (n/a)</td><td>410.14 (n/a)</td><td>316.80 (n/a)</td><td>245.40 (n/a)</td><td>181.02 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>557.20 (n/a)</td><td>444.04 (n/a)</td><td>494.60 (n/a)</td><td>268.80 (n/a)</td><td>112.89 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>783.10 (n/a)</td><td>496.52 (n/a)</td><td>449.00 (n/a)</td><td>335.50 (n/a)</td><td>172.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2444.50 (n/a)</td><td>738.52 (n/a)</td><td>293.50 (n/a)</td><td>235.50 (n/a)</td><td>957.82 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>585.50 (n/a)</td><td>462.02 (n/a)</td><td>467.90 (n/a)</td><td>294.30 (n/a)</td><td>111.78 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>536.40 (n/a)</td><td>396.08 (n/a)</td><td>457.50 (n/a)</td><td>238.00 (n/a)</td><td>127.35 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>476.40 (n/a)</td><td>391.78 (n/a)</td><td>441.00 (n/a)</td><td>285.60 (n/a)</td><td>92.18 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>828.60 (n/a)</td><td>531.32 (n/a)</td><td>492.00 (n/a)</td><td>240.50 (n/a)</td><td>216.29 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>531.50 (n/a)</td><td>380.44 (n/a)</td><td>302.80 (n/a)</td><td>289.10 (n/a)</td><td>119.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>622.20 (n/a)</td><td>429.74 (n/a)</td><td>451.10 (n/a)</td><td>225.40 (n/a)</td><td>167.73 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1041.10 (n/a)</td><td>506.58 (n/a)</td><td>378.70 (n/a)</td><td>291.80 (n/a)</td><td>313.28 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.10 (n/a)</td><td>405.64 (n/a)</td><td>414.10 (n/a)</td><td>265.70 (n/a)</td><td>126.21 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>622.20 (n/a)</td><td>493.70 (n/a)</td><td>519.60 (n/a)</td><td>290.10 (n/a)</td><td>123.01 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.90 (n/a)</td><td>375.40 (n/a)</td><td>312.10 (n/a)</td><td>250.70 (n/a)</td><td>151.67 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.10 (n/a)</td><td>405.56 (n/a)</td><td>397.60 (n/a)</td><td>216.50 (n/a)</td><td>161.85 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>663.30 (n/a)</td><td>491.90 (n/a)</td><td>457.00 (n/a)</td><td>401.50 (n/a)</td><td>108.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>489.60 (n/a)</td><td>327.88 (n/a)</td><td>304.30 (n/a)</td><td>237.60 (n/a)</td><td>99.22 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1104.70 (n/a)</td><td>509.96 (n/a)</td><td>439.80 (n/a)</td><td>212.70 (n/a)</td><td>360.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>490.40 (n/a)</td><td>391.42 (n/a)</td><td>470.70 (n/a)</td><td>222.10 (n/a)</td><td>122.49 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>445.60 (n/a)</td><td>297.02 (n/a)</td><td>244.70 (n/a)</td><td>239.30 (n/a)</td><td>88.82 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>310.40 (n/a)</td><td>277.82 (n/a)</td><td>278.80 (n/a)</td><td>249.60 (n/a)</td><td>27.65 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>505.80 (n/a)</td><td>370.74 (n/a)</td><td>340.50 (n/a)</td><td>305.50 (n/a)</td><td>82.87 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>615.90 (n/a)</td><td>368.62 (n/a)</td><td>266.50 (n/a)</td><td>243.40 (n/a)</td><td>164.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>601.40 (n/a)</td><td>412.00 (n/a)</td><td>441.80 (n/a)</td><td>249.70 (n/a)</td><td>147.59 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>577.90 (n/a)</td><td>355.04 (n/a)</td><td>301.30 (n/a)</td><td>196.70 (n/a)</td><td>152.09 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>524.40 (n/a)</td><td>408.46 (n/a)</td><td>484.40 (n/a)</td><td>253.00 (n/a)</td><td>136.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>497.30 (n/a)</td><td>367.94 (n/a)</td><td>341.70 (n/a)</td><td>272.20 (n/a)</td><td>88.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1929.40 (n/a)</td><td>645.06 (n/a)</td><td>347.70 (n/a)</td><td>251.00 (n/a)</td><td>719.27 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>625.40 (n/a)</td><td>378.34 (n/a)</td><td>299.40 (n/a)</td><td>243.00 (n/a)</td><td>160.21 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>540.30 (n/a)</td><td>361.62 (n/a)</td><td>314.10 (n/a)</td><td>245.80 (n/a)</td><td>133.21 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2478.50 (n/a)</td><td>965.18 (n/a)</td><td>703.60 (n/a)</td><td>277.30 (n/a)</td><td>868.60 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>499.00 (n/a)</td><td>393.40 (n/a)</td><td>472.30 (n/a)</td><td>244.50 (n/a)</td><td>124.02 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>493.20 (n/a)</td><td>357.36 (n/a)</td><td>316.10 (n/a)</td><td>240.10 (n/a)</td><td>109.25 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2520.80 (n/a)</td><td>909.08 (n/a)</td><td>450.70 (n/a)</td><td>370.40 (n/a)</td><td>916.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.58 (+13.73%)</td><td>0.40 (+2.09%)</td><td>0.37 (+8.87%)</td><td>0.17 <b>(-48.95%)</b></td><td>0.16 <b>(+108.48%)</b></td><td>1298.00 <b>(+95.89%)</b></td><td>670.78 (+14.69%)</td><td>601.90 (-8.13%)</td><td>382.80 (-12.06%)</td><td>370.31 <b>(+248.77%)</b></td><td>24.65 (+13.73%)</td><td>16.97 (+2.09%)</td><td>15.68 (+8.87%)</td><td>7.27 <b>(-48.95%)</b></td><td>7.03 <b>(+108.48%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>662.60 (n/a)</td><td>584.86 (n/a)</td><td>655.20 (n/a)</td><td>435.30 (n/a)</td><td>106.18 (n/a)</td><td>21.68 (n/a)</td><td>16.62 (n/a)</td><td>14.40 (n/a)</td><td>14.24 (n/a)</td><td>3.37 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.66 (+14.34%)</td><td>0.47 (+8.52%)</td><td>0.45 (-4.54%)</td><td>0.35 <b>(+84.60%)</b></td><td>0.12 <b>(-22.22%)</b></td><td>633.90 <b>(-45.83%)</b></td><td>493.56 (-17.78%)</td><td>493.60 (+4.75%)</td><td>334.00 (-12.54%)</td><td>107.41 <b>(-66.90%)</b></td><td>28.25 (+14.34%)</td><td>19.97 (+8.52%)</td><td>19.12 (-4.54%)</td><td>14.89 <b>(+84.60%)</b></td><td>4.98 <b>(-22.22%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.58 (n/a)</td><td>0.43 (n/a)</td><td>0.47 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>1170.20 (n/a)</td><td>600.26 (n/a)</td><td>471.20 (n/a)</td><td>381.90 (n/a)</td><td>324.49 (n/a)</td><td>24.71 (n/a)</td><td>18.40 (n/a)</td><td>20.03 (n/a)</td><td>8.06 (n/a)</td><td>6.40 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.31 (-1.53%)</td><td>0.30 (-1.09%)</td><td>0.30 (-0.68%)</td><td>0.29 (+0.16%)</td><td>0.01 <b>(-22.79%)</b></td><td>85918.90 (-0.16%)</td><td>83740.02 (+1.08%)</td><td>83180.90 (+0.69%)</td><td>82078.30 (+1.56%)</td><td>1673.53 <b>(-21.61%)</b></td><td>209.31 (-1.53%)</td><td>205.22 (-1.09%)</td><td>206.54 (-0.68%)</td><td>199.95 (+0.16%)</td><td>4.08 <b>(-22.79%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>86059.70 (n/a)</td><td>82842.22 (n/a)</td><td>82613.50 (n/a)</td><td>80821.30 (n/a)</td><td>2134.93 (n/a)</td><td>212.57 (n/a)</td><td>207.49 (n/a)</td><td>207.95 (n/a)</td><td>199.63 (n/a)</td><td>5.28 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>1.03 (+0.67%)</td><td>1.01 (+0.96%)</td><td>1.00 (+1.69%)</td><td>0.98 (+1.01%)</td><td>0.02 (-19.40%)</td><td>25649.70 (-1.00%)</td><td>25033.34 (-0.97%)</td><td>25064.20 (-1.66%)</td><td>24359.40 (-0.67%)</td><td>457.29 <b>(-20.74%)</b></td><td>705.27 (+0.67%)</td><td>686.46 (+0.96%)</td><td>685.43 (+1.69%)</td><td>669.79 (+1.01%)</td><td>12.59 (-19.40%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>0.99 (n/a)</td><td>0.97 (n/a)</td><td>0.02 (n/a)</td><td>25909.30 (n/a)</td><td>25278.74 (n/a)</td><td>25487.50 (n/a)</td><td>24523.30 (n/a)</td><td>576.93 (n/a)</td><td>700.55 (n/a)</td><td>679.90 (n/a)</td><td>674.05 (n/a)</td><td>663.08 (n/a)</td><td>15.62 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.83 (+0.50%)</td><td>0.81 (+0.27%)</td><td>0.82 (+0.72%)</td><td>0.79 (-1.26%)</td><td>0.02 <b>(+45.24%)</b></td><td>95569.70 (+1.27%)</td><td>92768.46 (-0.25%)</td><td>91742.00 (-0.72%)</td><td>91507.00 (-0.50%)</td><td>1762.71 <b>(+46.06%)</b></td><td>750.98 (+0.50%)</td><td>740.97 (+0.27%)</td><td>749.05 (+0.72%)</td><td>719.05 (-1.26%)</td><td>13.87 <b>(+45.24%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94368.70 (n/a)</td><td>93000.88 (n/a)</td><td>92403.60 (n/a)</td><td>91966.30 (n/a)</td><td>1206.81 (n/a)</td><td>747.22 (n/a)</td><td>739.01 (n/a)</td><td>743.69 (n/a)</td><td>728.20 (n/a)</td><td>9.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.77 (-0.54%)</td><td>0.77 (+1.49%)</td><td>0.77 (+2.45%)</td><td>0.75 (+2.89%)</td><td>0.01 <b>(-56.58%)</b></td><td>100482.70 (-2.81%)</td><td>98393.80 (-1.52%)</td><td>98093.30 (-2.39%)</td><td>97531.00 (+0.54%)</td><td>1211.70 <b>(-57.26%)</b></td><td>704.59 (-0.54%)</td><td>698.50 (+1.49%)</td><td>700.55 (+2.45%)</td><td>683.89 (+2.89%)</td><td>8.49 <b>(-56.58%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103383.10 (n/a)</td><td>99908.88 (n/a)</td><td>100492.00 (n/a)</td><td>97007.80 (n/a)</td><td>2835.09 (n/a)</td><td>708.39 (n/a)</td><td>688.27 (n/a)</td><td>683.83 (n/a)</td><td>664.71 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.80 (-0.38%)</td><td>0.79 (-0.86%)</td><td>0.80 (-0.28%)</td><td>0.78 (-1.36%)</td><td>0.01 <b>(+88.10%)</b></td><td>96866.20 (+1.38%)</td><td>95261.30 (+0.88%)</td><td>94707.40 (+0.29%)</td><td>93847.80 (+0.38%)</td><td>1415.60 <b>(+91.60%)</b></td><td>732.24 (-0.38%)</td><td>721.51 (-0.86%)</td><td>725.60 (-0.28%)</td><td>709.43 (-1.36%)</td><td>10.68 <b>(+88.10%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95544.00 (n/a)</td><td>94425.70 (n/a)</td><td>94437.60 (n/a)</td><td>93492.30 (n/a)</td><td>738.81 (n/a)</td><td>735.03 (n/a)</td><td>727.80 (n/a)</td><td>727.67 (n/a)</td><td>719.24 (n/a)</td><td>5.68 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>4.20 <b>(-20.57%)</b></td><td>3.38 (-5.46%)</td><td>3.85 (-5.94%)</td><td>2.19 (+0.68%)</td><td>0.88 <b>(-35.31%)</b></td><td>4073.80 (-0.68%)</td><td>2813.62 (-0.92%)</td><td>2313.30 (+6.31%)</td><td>2123.20 <b>(+25.89%)</b></td><td>843.94 <b>(-26.79%)</b></td><td>252.86 <b>(-20.57%)</b></td><td>203.38 (-5.46%)</td><td>232.08 (-5.94%)</td><td>131.78 (+0.68%)</td><td>52.85 <b>(-35.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.28 (n/a)</td><td>3.57 (n/a)</td><td>4.10 (n/a)</td><td>2.17 (n/a)</td><td>1.36 (n/a)</td><td>4101.70 (n/a)</td><td>2839.62 (n/a)</td><td>2175.90 (n/a)</td><td>1686.50 (n/a)</td><td>1152.81 (n/a)</td><td>318.34 (n/a)</td><td>215.12 (n/a)</td><td>246.73 (n/a)</td><td>130.89 (n/a)</td><td>81.70 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>5.19 (+5.56%)</td><td>3.61 <b>(+23.82%)</b></td><td>2.92 <b>(+28.74%)</b></td><td>2.47 (+13.23%)</td><td>1.21 (+2.89%)</td><td>3607.50 (-11.69%)</td><td>2681.74 <b>(-20.30%)</b></td><td>3057.30 <b>(-22.32%)</b></td><td>1715.90 (-5.27%)</td><td>815.51 (-17.30%)</td><td>312.88 (+5.56%)</td><td>217.69 <b>(+23.82%)</b></td><td>175.60 <b>(+28.74%)</b></td><td>148.82 (+13.23%)</td><td>72.66 (+2.89%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>4.92 (n/a)</td><td>2.92 (n/a)</td><td>2.26 (n/a)</td><td>2.18 (n/a)</td><td>1.17 (n/a)</td><td>4084.90 (n/a)</td><td>3364.74 (n/a)</td><td>3935.80 (n/a)</td><td>1811.40 (n/a)</td><td>986.06 (n/a)</td><td>296.39 (n/a)</td><td>175.81 (n/a)</td><td>136.41 (n/a)</td><td>131.43 (n/a)</td><td>70.62 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>5.55 <b>(+40.02%)</b></td><td>4.11 <b>(+32.62%)</b></td><td>3.40 (-1.72%)</td><td>2.94 <b>(+37.17%)</b></td><td>1.30 <b>(+50.58%)</b></td><td>3026.70 <b>(-27.10%)</b></td><td>2337.48 <b>(-24.14%)</b></td><td>2620.80 (+1.75%)</td><td>1604.80 <b>(-28.58%)</b></td><td>677.05 <b>(-27.58%)</b></td><td>334.54 <b>(+40.02%)</b></td><td>247.76 <b>(+32.62%)</b></td><td>204.85 (-1.72%)</td><td>177.38 <b>(+37.17%)</b></td><td>78.34 <b>(+50.58%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.97 (n/a)</td><td>3.10 (n/a)</td><td>3.46 (n/a)</td><td>2.15 (n/a)</td><td>0.86 (n/a)</td><td>4151.70 (n/a)</td><td>3081.24 (n/a)</td><td>2575.70 (n/a)</td><td>2247.10 (n/a)</td><td>934.91 (n/a)</td><td>238.92 (n/a)</td><td>186.82 (n/a)</td><td>208.44 (n/a)</td><td>129.31 (n/a)</td><td>52.03 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>6.51 (-0.19%)</td><td>5.60 (-2.72%)</td><td>6.28 (+11.79%)</td><td>4.26 (-14.11%)</td><td>1.08 <b>(+60.97%)</b></td><td>8192.00 (+16.42%)</td><td>6432.66 (+5.06%)</td><td>5552.40 (-10.55%)</td><td>5352.50 (+0.19%)</td><td>1342.60 <b>(+88.46%)</b></td><td>401.21 (-0.19%)</td><td>344.91 (-2.72%)</td><td>386.77 (+11.79%)</td><td>262.14 (-14.11%)</td><td>66.38 <b>(+60.97%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>6.53 (n/a)</td><td>5.76 (n/a)</td><td>5.62 (n/a)</td><td>4.96 (n/a)</td><td>0.67 (n/a)</td><td>7036.40 (n/a)</td><td>6123.12 (n/a)</td><td>6207.20 (n/a)</td><td>5342.20 (n/a)</td><td>712.40 (n/a)</td><td>401.99 (n/a)</td><td>354.55 (n/a)</td><td>345.96 (n/a)</td><td>305.20 (n/a)</td><td>41.24 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>4.63 (-9.78%)</td><td>3.84 (-8.83%)</td><td>4.10 (+0.19%)</td><td>3.01 (-16.45%)</td><td>0.65 (+14.56%)</td><td>11595.90 (+19.68%)</td><td>9301.48 (+10.86%)</td><td>8511.90 (-0.19%)</td><td>7526.20 (+10.84%)</td><td>1652.06 <b>(+57.06%)</b></td><td>285.33 (-9.78%)</td><td>236.54 (-8.83%)</td><td>252.29 (+0.19%)</td><td>185.19 (-16.45%)</td><td>40.14 (+14.56%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.13 (n/a)</td><td>4.21 (n/a)</td><td>4.09 (n/a)</td><td>3.60 (n/a)</td><td>0.57 (n/a)</td><td>9688.90 (n/a)</td><td>8390.16 (n/a)</td><td>8528.40 (n/a)</td><td>6790.20 (n/a)</td><td>1051.84 (n/a)</td><td>316.26 (n/a)</td><td>259.44 (n/a)</td><td>251.80 (n/a)</td><td>221.64 (n/a)</td><td>35.04 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>6.79 <b>(+23.24%)</b></td><td>5.94 (+16.81%)</td><td>6.42 <b>(+22.25%)</b></td><td>4.87 (+10.62%)</td><td>0.90 <b>(+107.86%)</b></td><td>7158.20 (-9.60%)</td><td>5985.08 (-13.24%)</td><td>5430.90 (-18.20%)</td><td>5137.40 (-18.85%)</td><td>957.46 <b>(+52.25%)</b></td><td>418.01 <b>(+23.24%)</b></td><td>365.90 (+16.81%)</td><td>395.42 <b>(+22.25%)</b></td><td>300.00 (+10.62%)</td><td>55.50 <b>(+107.86%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.51 (n/a)</td><td>5.09 (n/a)</td><td>5.25 (n/a)</td><td>4.40 (n/a)</td><td>0.43 (n/a)</td><td>7918.50 (n/a)</td><td>6898.50 (n/a)</td><td>6639.10 (n/a)</td><td>6331.10 (n/a)</td><td>628.90 (n/a)</td><td>339.20 (n/a)</td><td>313.24 (n/a)</td><td>323.46 (n/a)</td><td>271.20 (n/a)</td><td>26.70 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.78 (-0.83%)</td><td>0.77 (+0.42%)</td><td>0.76 (+0.05%)</td><td>0.76 (+2.93%)</td><td>0.01 <b>(-44.57%)</b></td><td>99947.00 (-2.84%)</td><td>98629.16 (-0.46%)</td><td>98835.00 (-0.05%)</td><td>96545.80 (+0.84%)</td><td>1412.77 <b>(-45.71%)</b></td><td>711.78 (-0.83%)</td><td>696.86 (+0.42%)</td><td>695.30 (+0.05%)</td><td>687.56 (+2.93%)</td><td>10.05 <b>(-44.57%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>102870.50 (n/a)</td><td>99080.76 (n/a)</td><td>98889.20 (n/a)</td><td>95744.00 (n/a)</td><td>2602.27 (n/a)</td><td>717.74 (n/a)</td><td>693.95 (n/a)</td><td>694.91 (n/a)</td><td>668.02 (n/a)</td><td>18.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.77 (-0.85%)</td><td>0.76 (+0.72%)</td><td>0.76 (+1.44%)</td><td>0.72 (+1.17%)</td><td>0.02 (-15.43%)</td><td>104762.80 (-1.15%)</td><td>99995.42 (-0.74%)</td><td>98887.20 (-1.42%)</td><td>97853.70 (+0.85%)</td><td>2789.77 (-15.79%)</td><td>702.27 (-0.85%)</td><td>687.64 (+0.72%)</td><td>694.93 (+1.44%)</td><td>655.95 (+1.17%)</td><td>18.63 (-15.43%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.71 (n/a)</td><td>0.02 (n/a)</td><td>105986.20 (n/a)</td><td>100741.64 (n/a)</td><td>100307.80 (n/a)</td><td>97024.30 (n/a)</td><td>3312.77 (n/a)</td><td>708.27 (n/a)</td><td>682.72 (n/a)</td><td>685.09 (n/a)</td><td>648.38 (n/a)</td><td>22.03 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.81 (+0.07%)</td><td>0.80 (-0.57%)</td><td>0.81 (-0.52%)</td><td>0.79 (-1.30%)</td><td>0.01 <b>(+81.15%)</b></td><td>95411.00 (+1.32%)</td><td>93904.70 (+0.58%)</td><td>93751.30 (+0.52%)</td><td>92794.20 (-0.07%)</td><td>973.34 <b>(+83.66%)</b></td><td>740.56 (+0.07%)</td><td>731.86 (-0.57%)</td><td>733.00 (-0.52%)</td><td>720.25 (-1.30%)</td><td>7.55 <b>(+81.15%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94167.40 (n/a)</td><td>93360.92 (n/a)</td><td>93262.90 (n/a)</td><td>92860.10 (n/a)</td><td>529.97 (n/a)</td><td>740.03 (n/a)</td><td>736.08 (n/a)</td><td>736.84 (n/a)</td><td>729.76 (n/a)</td><td>4.17 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>3.75 (-4.64%)</td><td>2.23 (+5.79%)</td><td>1.74 (-14.35%)</td><td>1.56 <b>(+50.12%)</b></td><td>0.91 (-18.49%)</td><td>5164.40 <b>(-33.39%)</b></td><td>4011.94 (-13.88%)</td><td>4634.00 (+16.75%)</td><td>2151.60 (+4.86%)</td><td>1232.42 <b>(-42.92%)</b></td><td>982.49 (-4.64%)</td><td>583.97 (+5.79%)</td><td>456.18 (-14.35%)</td><td>409.33 <b>(+50.12%)</b></td><td>237.65 (-18.49%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.93 (n/a)</td><td>2.11 (n/a)</td><td>2.03 (n/a)</td><td>1.04 (n/a)</td><td>1.11 (n/a)</td><td>7752.90 (n/a)</td><td>4658.58 (n/a)</td><td>3969.00 (n/a)</td><td>2051.90 (n/a)</td><td>2159.12 (n/a)</td><td>1030.25 (n/a)</td><td>552.03 (n/a)</td><td>532.60 (n/a)</td><td>272.66 (n/a)</td><td>291.56 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.28 (+11.47%)</td><td>0.20 (-6.58%)</td><td>0.21 (+1.51%)</td><td>0.11 <b>(-36.94%)</b></td><td>0.06 <b>(+137.60%)</b></td><td>10876.70 <b>(+58.59%)</b></td><td>6950.02 (+15.36%)</td><td>6050.90 (-1.49%)</td><td>4462.10 (-10.29%)</td><td>2422.28 <b>(+256.64%)</b></td><td>15.04 (+11.47%)</td><td>10.52 (-6.58%)</td><td>11.09 (+1.51%)</td><td>6.17 <b>(-36.94%)</b></td><td>3.24 <b>(+137.60%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>6858.50 (n/a)</td><td>6024.78 (n/a)</td><td>6142.20 (n/a)</td><td>4973.90 (n/a)</td><td>679.20 (n/a)</td><td>13.49 (n/a)</td><td>11.26 (n/a)</td><td>10.93 (n/a)</td><td>9.78 (n/a)</td><td>1.36 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>3.82 (n/a)</td><td>3.66 (n/a)</td><td>3.72 (n/a)</td><td>3.34 (n/a)</td><td>0.19 (n/a)</td><td>3.82 (n/a)</td><td>3.66 (n/a)</td><td>3.72 (n/a)</td><td>3.34 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>7.58 (+8.16%)</td><td>6.65 (+6.28%)</td><td>6.58 (-1.39%)</td><td>5.81 (+8.76%)</td><td>0.68 (-16.95%)</td><td>7.57 (+8.16%)</td><td>6.65 (+6.28%)</td><td>6.58 (-1.39%)</td><td>5.81 (+8.76%)</td><td>0.68 (-16.95%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>7.01 (n/a)</td><td>6.26 (n/a)</td><td>6.67 (n/a)</td><td>5.34 (n/a)</td><td>0.81 (n/a)</td><td>7.00 (n/a)</td><td>6.26 (n/a)</td><td>6.67 (n/a)</td><td>5.34 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>13.73 (+9.82%)</td><td>11.08 (+16.30%)</td><td>11.70 <b>(+29.33%)</b></td><td>8.58 (+5.11%)</td><td>2.20 <b>(+26.80%)</b></td><td>13.72 (+9.82%)</td><td>11.07 (+16.30%)</td><td>11.70 <b>(+29.33%)</b></td><td>8.57 (+5.11%)</td><td>2.20 <b>(+26.80%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>12.50 (n/a)</td><td>9.52 (n/a)</td><td>9.05 (n/a)</td><td>8.16 (n/a)</td><td>1.74 (n/a)</td><td>12.49 (n/a)</td><td>9.52 (n/a)</td><td>9.04 (n/a)</td><td>8.15 (n/a)</td><td>1.73 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>3.81 (n/a)</td><td>3.73 (n/a)</td><td>3.77 (n/a)</td><td>3.57 (n/a)</td><td>0.10 (n/a)</td><td>3.80 (n/a)</td><td>3.73 (n/a)</td><td>3.76 (n/a)</td><td>3.57 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>6.82 (-7.54%)</td><td>5.86 (-7.51%)</td><td>5.82 (+0.05%)</td><td>4.75 (-15.61%)</td><td>0.75 (-13.69%)</td><td>6.82 (-7.54%)</td><td>5.86 (-7.51%)</td><td>5.82 (+0.05%)</td><td>4.75 (-15.61%)</td><td>0.75 (-13.69%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>7.38 (n/a)</td><td>6.34 (n/a)</td><td>5.82 (n/a)</td><td>5.63 (n/a)</td><td>0.86 (n/a)</td><td>7.37 (n/a)</td><td>6.33 (n/a)</td><td>5.81 (n/a)</td><td>5.63 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>14.13 (+0.57%)</td><td>9.53 (-8.91%)</td><td>8.48 (-17.37%)</td><td>7.36 (+5.28%)</td><td>2.80 (-5.93%)</td><td>14.13 (+0.57%)</td><td>9.52 (-8.91%)</td><td>8.48 (-17.37%)</td><td>7.36 (+5.28%)</td><td>2.80 (-5.93%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>14.05 (n/a)</td><td>10.46 (n/a)</td><td>10.27 (n/a)</td><td>6.99 (n/a)</td><td>2.98 (n/a)</td><td>14.05 (n/a)</td><td>10.45 (n/a)</td><td>10.26 (n/a)</td><td>6.99 (n/a)</td><td>2.98 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.99 (+5.65%)</td><td>2.44 (+19.94%)</td><td>2.76 (+10.86%)</td><td>1.11 (+9.24%)</td><td>0.76 (-14.22%)</td><td>2.98 (+5.65%)</td><td>2.44 (+19.94%)</td><td>2.76 (+10.86%)</td><td>1.11 (+9.24%)</td><td>0.76 (-14.22%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>2.83 (n/a)</td><td>2.04 (n/a)</td><td>2.49 (n/a)</td><td>1.02 (n/a)</td><td>0.89 (n/a)</td><td>2.83 (n/a)</td><td>2.03 (n/a)</td><td>2.49 (n/a)</td><td>1.01 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.53 (-7.11%)</td><td>0.29 <b>(-25.03%)</b></td><td>0.36 (-13.17%)</td><td>0.08 (-10.04%)</td><td>0.20 (+6.37%)</td><td>0.52 (-7.11%)</td><td>0.29 <b>(-25.03%)</b></td><td>0.35 (-13.17%)</td><td>0.08 (-10.04%)</td><td>0.20 (+6.37%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.57 (n/a)</td><td>0.39 (n/a)</td><td>0.42 (n/a)</td><td>0.09 (n/a)</td><td>0.19 (n/a)</td><td>0.57 (n/a)</td><td>0.38 (n/a)</td><td>0.41 (n/a)</td><td>0.09 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.72 (-9.71%)</td><td>0.52 (-0.30%)</td><td>0.50 (+5.60%)</td><td>0.34 (+7.43%)</td><td>0.17 (-12.83%)</td><td>0.71 (-9.71%)</td><td>0.51 (-0.30%)</td><td>0.50 (+5.60%)</td><td>0.34 (+7.43%)</td><td>0.17 (-12.83%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.79 (n/a)</td><td>0.52 (n/a)</td><td>0.48 (n/a)</td><td>0.32 (n/a)</td><td>0.20 (n/a)</td><td>0.78 (n/a)</td><td>0.51 (n/a)</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.48 (-5.57%)</td><td>1.33 <b>(-45.61%)</b></td><td>0.77 <b>(-68.76%)</b></td><td>0.43 <b>(-81.04%)</b></td><td>0.93 <b>(+611.23%)</b></td><td>2.44 (-5.57%)</td><td>1.30 <b>(-45.61%)</b></td><td>0.76 <b>(-68.76%)</b></td><td>0.43 <b>(-81.04%)</b></td><td>0.92 <b>(+611.23%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>2.63 (n/a)</td><td>2.44 (n/a)</td><td>2.46 (n/a)</td><td>2.29 (n/a)</td><td>0.13 (n/a)</td><td>2.59 (n/a)</td><td>2.40 (n/a)</td><td>2.42 (n/a)</td><td>2.26 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>691.30 (n/a)</td><td>540.32 (n/a)</td><td>564.20 (n/a)</td><td>246.80 (n/a)</td><td>175.75 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>642.20 (n/a)</td><td>443.90 (n/a)</td><td>491.90 (n/a)</td><td>240.00 (n/a)</td><td>183.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.00 (n/a)</td><td>451.16 (n/a)</td><td>527.30 (n/a)</td><td>272.60 (n/a)</td><td>161.29 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1899.20 (n/a)</td><td>749.28 (n/a)</td><td>544.20 (n/a)</td><td>276.10 (n/a)</td><td>652.90 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>506.40 (n/a)</td><td>427.24 (n/a)</td><td>439.20 (n/a)</td><td>281.10 (n/a)</td><td>86.43 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.60 (n/a)</td><td>447.96 (n/a)</td><td>509.10 (n/a)</td><td>285.10 (n/a)</td><td>140.49 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.70 (n/a)</td><td>321.02 (n/a)</td><td>293.80 (n/a)</td><td>240.70 (n/a)</td><td>95.87 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.90 (n/a)</td><td>360.44 (n/a)</td><td>276.80 (n/a)</td><td>233.80 (n/a)</td><td>150.91 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.20 (n/a)</td><td>438.62 (n/a)</td><td>471.00 (n/a)</td><td>205.60 (n/a)</td><td>134.70 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.30 (n/a)</td><td>413.04 (n/a)</td><td>368.30 (n/a)</td><td>270.40 (n/a)</td><td>154.87 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.30 (n/a)</td><td>455.88 (n/a)</td><td>462.20 (n/a)</td><td>292.50 (n/a)</td><td>99.92 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>639.30 (n/a)</td><td>482.84 (n/a)</td><td>490.40 (n/a)</td><td>248.90 (n/a)</td><td>157.30 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>492.70 (n/a)</td><td>350.84 (n/a)</td><td>291.10 (n/a)</td><td>252.40 (n/a)</td><td>115.71 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>550.00 (n/a)</td><td>398.32 (n/a)</td><td>434.90 (n/a)</td><td>230.90 (n/a)</td><td>134.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>317.00 (n/a)</td><td>277.84 (n/a)</td><td>270.60 (n/a)</td><td>246.00 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>556.30 (n/a)</td><td>405.36 (n/a)</td><td>425.70 (n/a)</td><td>266.10 (n/a)</td><td>120.29 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2089.00 (n/a)</td><td>698.68 (n/a)</td><td>352.00 (n/a)</td><td>228.20 (n/a)</td><td>788.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>432.20 (n/a)</td><td>392.12 (n/a)</td><td>420.70 (n/a)</td><td>302.30 (n/a)</td><td>53.69 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>484.00 (n/a)</td><td>337.06 (n/a)</td><td>312.70 (n/a)</td><td>270.20 (n/a)</td><td>85.90 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1039.60 (n/a)</td><td>491.26 (n/a)</td><td>355.40 (n/a)</td><td>251.30 (n/a)</td><td>322.43 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>607.00 (n/a)</td><td>394.88 (n/a)</td><td>312.40 (n/a)</td><td>286.40 (n/a)</td><td>138.87 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>687.50 (n/a)</td><td>386.54 (n/a)</td><td>265.10 (n/a)</td><td>244.10 (n/a)</td><td>196.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>522.50 (n/a)</td><td>436.92 (n/a)</td><td>495.00 (n/a)</td><td>274.00 (n/a)</td><td>108.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>721.40 (n/a)</td><td>524.74 (n/a)</td><td>557.20 (n/a)</td><td>279.10 (n/a)</td><td>169.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (-16.20%)</td><td>0.01 (+0.41%)</td><td>0.01 (-6.17%)</td><td>0.01 <b>(+58.05%)</b></td><td>0.00 <b>(-46.74%)</b></td><td>452.40 <b>(-36.73%)</b></td><td>331.64 (-15.92%)</td><td>302.80 (+6.58%)</td><td>241.10 (+19.30%)</td><td>87.14 <b>(-60.09%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>715.00 (n/a)</td><td>394.44 (n/a)</td><td>284.10 (n/a)</td><td>202.10 (n/a)</td><td>218.36 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 <b>(-39.32%)</b></td><td>0.01 <b>(-27.49%)</b></td><td>0.01 (-19.62%)</td><td>0.00 <b>(-45.23%)</b></td><td>0.00 <b>(-41.81%)</b></td><td>1085.10 <b>(+82.58%)</b></td><td>616.98 <b>(+38.67%)</b></td><td>562.50 <b>(+24.42%)</b></td><td>401.70 <b>(+64.77%)</b></td><td>270.44 <b>(+82.55%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.30 (n/a)</td><td>444.92 (n/a)</td><td>452.10 (n/a)</td><td>243.80 (n/a)</td><td>148.15 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (-3.31%)</td><td>0.01 (+9.42%)</td><td>0.01 <b>(+54.36%)</b></td><td>0.01 (+12.89%)</td><td>0.00 <b>(-26.81%)</b></td><td>476.70 (-11.41%)</td><td>329.28 (-13.99%)</td><td>293.40 <b>(-35.22%)</b></td><td>239.20 (+3.42%)</td><td>101.39 <b>(-28.68%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>538.10 (n/a)</td><td>382.84 (n/a)</td><td>452.90 (n/a)</td><td>231.30 (n/a)</td><td>142.17 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (-8.36%)</td><td>0.01 (-17.60%)</td><td>0.01 <b>(-36.37%)</b></td><td>0.01 (+12.54%)</td><td>0.00 <b>(-28.42%)</b></td><td>507.30 (-11.14%)</td><td>406.66 (+14.25%)</td><td>430.90 <b>(+57.15%)</b></td><td>253.40 (+9.13%)</td><td>101.22 <b>(-31.41%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.90 (n/a)</td><td>355.94 (n/a)</td><td>274.20 (n/a)</td><td>232.20 (n/a)</td><td>147.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (-9.99%)</td><td>0.01 <b>(-25.96%)</b></td><td>0.01 <b>(-42.86%)</b></td><td>0.01 (-15.78%)</td><td>0.00 (-6.93%)</td><td>597.70 (+18.73%)</td><td>472.22 <b>(+36.51%)</b></td><td>543.30 <b>(+74.98%)</b></td><td>261.30 (+11.10%)</td><td>139.55 <b>(+22.27%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>503.40 (n/a)</td><td>345.92 (n/a)</td><td>310.50 (n/a)</td><td>235.20 (n/a)</td><td>114.13 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 <b>(-32.02%)</b></td><td>0.01 <b>(-21.72%)</b></td><td>0.01 (-6.69%)</td><td>0.01 (+0.04%)</td><td>0.00 <b>(-63.84%)</b></td><td>581.30 (-0.03%)</td><td>487.94 (+16.04%)</td><td>485.30 (+7.18%)</td><td>365.40 <b>(+47.10%)</b></td><td>79.33 <b>(-47.69%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>581.50 (n/a)</td><td>420.48 (n/a)</td><td>452.80 (n/a)</td><td>248.40 (n/a)</td><td>151.66 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 (-7.04%)</td><td>0.03 (+7.83%)</td><td>0.02 (+9.10%)</td><td>0.01 (+4.00%)</td><td>0.01 (-9.27%)</td><td>576.70 (-3.84%)</td><td>395.84 (-8.04%)</td><td>442.90 (-8.34%)</td><td>168.30 (+7.61%)</td><td>175.83 (+6.23%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>599.70 (n/a)</td><td>430.44 (n/a)</td><td>483.20 (n/a)</td><td>156.40 (n/a)</td><td>165.52 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (+4.36%)</td><td>0.03 (+14.84%)</td><td>0.03 (+17.71%)</td><td>0.02 <b>(+79.24%)</b></td><td>0.01 <b>(-29.71%)</b></td><td>433.60 <b>(-44.21%)</b></td><td>321.62 <b>(-23.31%)</b></td><td>289.10 (-15.05%)</td><td>225.90 (-4.20%)</td><td>83.40 <b>(-62.05%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>777.20 (n/a)</td><td>419.40 (n/a)</td><td>340.30 (n/a)</td><td>235.80 (n/a)</td><td>219.73 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 <b>(+34.43%)</b></td><td>0.02 (-7.32%)</td><td>0.02 <b>(-28.07%)</b></td><td>0.01 (+5.51%)</td><td>0.01 <b>(+68.13%)</b></td><td>567.70 (-5.23%)</td><td>446.12 (+13.45%)</td><td>484.40 <b>(+39.00%)</b></td><td>228.80 <b>(-25.62%)</b></td><td>137.00 (+13.91%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.00 (n/a)</td><td>393.22 (n/a)</td><td>348.50 (n/a)</td><td>307.60 (n/a)</td><td>120.28 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (+2.36%)</td><td>0.02 (-7.61%)</td><td>0.02 (-13.61%)</td><td>0.02 (-5.99%)</td><td>0.01 (+3.97%)</td><td>533.00 (+6.37%)</td><td>409.22 (+9.18%)</td><td>450.60 (+15.75%)</td><td>236.50 (-2.31%)</td><td>122.56 (+8.00%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.10 (n/a)</td><td>374.82 (n/a)</td><td>389.30 (n/a)</td><td>242.10 (n/a)</td><td>113.48 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 <b>(+28.64%)</b></td><td>0.03 <b>(+36.31%)</b></td><td>0.03 <b>(+54.40%)</b></td><td>0.01 <b>(+21.13%)</b></td><td>0.01 <b>(+24.62%)</b></td><td>606.30 (-17.45%)</td><td>339.28 <b>(-26.04%)</b></td><td>299.80 <b>(-35.22%)</b></td><td>197.40 <b>(-22.28%)</b></td><td>155.59 (-13.53%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>734.50 (n/a)</td><td>458.76 (n/a)</td><td>462.80 (n/a)</td><td>254.00 (n/a)</td><td>179.94 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 <b>(+21.32%)</b></td><td>0.03 <b>(+35.72%)</b></td><td>0.03 <b>(+63.66%)</b></td><td>0.02 <b>(+36.89%)</b></td><td>0.01 (+12.61%)</td><td>501.80 <b>(-26.96%)</b></td><td>357.32 <b>(-28.05%)</b></td><td>314.10 <b>(-38.89%)</b></td><td>194.20 (-17.61%)</td><td>128.83 <b>(-27.10%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>687.00 (n/a)</td><td>496.64 (n/a)</td><td>514.00 (n/a)</td><td>235.70 (n/a)</td><td>176.72 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (-19.92%)</td><td>0.02 (+1.50%)</td><td>0.02 <b>(+29.93%)</b></td><td>0.01 <b>(+225.62%)</b></td><td>0.01 <b>(-49.71%)</b></td><td>567.10 <b>(-69.29%)</b></td><td>407.60 <b>(-38.93%)</b></td><td>365.40 <b>(-23.04%)</b></td><td>263.00 <b>(+24.88%)</b></td><td>132.00 <b>(-80.43%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1846.50 (n/a)</td><td>667.38 (n/a)</td><td>474.80 (n/a)</td><td>210.60 (n/a)</td><td>674.68 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (-11.91%)</td><td>0.02 (+4.00%)</td><td>0.02 (+14.48%)</td><td>0.01 (+5.57%)</td><td>0.01 (-10.82%)</td><td>567.40 (-5.28%)</td><td>445.70 (-5.07%)</td><td>476.60 (-12.66%)</td><td>310.50 (+13.53%)</td><td>128.01 (-6.28%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.00 (n/a)</td><td>469.48 (n/a)</td><td>545.70 (n/a)</td><td>273.50 (n/a)</td><td>136.58 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (-11.17%)</td><td>0.06 <b>(+24.34%)</b></td><td>0.06 <b>(+76.46%)</b></td><td>0.05 <b>(+86.55%)</b></td><td>0.00 <b>(-86.14%)</b></td><td>315.80 <b>(-46.40%)</b></td><td>295.94 <b>(-30.97%)</b></td><td>296.40 <b>(-43.34%)</b></td><td>275.10 (+12.56%)</td><td>14.89 <b>(-91.20%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>589.20 (n/a)</td><td>428.70 (n/a)</td><td>523.10 (n/a)</td><td>244.40 (n/a)</td><td>169.25 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (-7.59%)</td><td>0.05 (-13.04%)</td><td>0.05 (-16.07%)</td><td>0.03 <b>(-25.15%)</b></td><td>0.02 (-2.54%)</td><td>570.00 <b>(+33.58%)</b></td><td>364.46 (+17.69%)</td><td>297.90 (+19.11%)</td><td>240.70 (+8.23%)</td><td>135.49 <b>(+38.76%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>426.70 (n/a)</td><td>309.68 (n/a)</td><td>250.10 (n/a)</td><td>222.40 (n/a)</td><td>97.65 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (+4.34%)</td><td>0.04 <b>(+23.30%)</b></td><td>0.04 (-9.46%)</td><td>0.04 <b>(+299.06%)</b></td><td>0.01 <b>(-37.92%)</b></td><td>461.60 <b>(-74.94%)</b></td><td>387.44 <b>(-44.95%)</b></td><td>443.30 (+10.44%)</td><td>256.70 (-4.14%)</td><td>90.35 <b>(-86.11%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1842.10 (n/a)</td><td>703.80 (n/a)</td><td>401.40 (n/a)</td><td>267.80 (n/a)</td><td>650.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 <b>(-35.38%)</b></td><td>0.04 <b>(-25.31%)</b></td><td>0.05 <b>(-23.52%)</b></td><td>0.03 (-14.82%)</td><td>0.01 <b>(-46.82%)</b></td><td>602.10 (+17.39%)</td><td>414.58 <b>(+26.26%)</b></td><td>356.90 <b>(+30.73%)</b></td><td>305.10 <b>(+54.72%)</b></td><td>124.77 (-5.62%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>512.90 (n/a)</td><td>328.36 (n/a)</td><td>273.00 (n/a)</td><td>197.20 (n/a)</td><td>132.19 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (-0.26%)</td><td>0.04 (-8.20%)</td><td>0.03 (-8.53%)</td><td>0.02 (-12.97%)</td><td>0.02 (+5.10%)</td><td>677.90 (+14.90%)</td><td>496.70 (+11.44%)</td><td>520.80 (+9.32%)</td><td>230.30 (+0.26%)</td><td>178.47 (+14.89%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.00 (n/a)</td><td>445.72 (n/a)</td><td>476.40 (n/a)</td><td>229.70 (n/a)</td><td>155.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 <b>(+148.89%)</b></td><td>0.04 <b>(+80.26%)</b></td><td>0.03 <b>(+23.75%)</b></td><td>0.03 <b>(+150.73%)</b></td><td>0.02 <b>(+143.65%)</b></td><td>617.50 <b>(-60.12%)</b></td><td>471.08 <b>(-45.33%)</b></td><td>520.60 (-19.20%)</td><td>209.70 <b>(-59.83%)</b></td><td>158.75 <b>(-63.18%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1548.30 (n/a)</td><td>861.74 (n/a)</td><td>644.30 (n/a)</td><td>522.00 (n/a)</td><td>431.12 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (+8.80%)</td><td>0.08 (-10.46%)</td><td>0.07 (-4.77%)</td><td>0.06 (-14.49%)</td><td>0.04 <b>(+25.92%)</b></td><td>585.10 (+16.95%)</td><td>465.04 (+17.04%)</td><td>482.40 (+5.01%)</td><td>217.60 (-8.11%)</td><td>148.11 <b>(+27.23%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>500.30 (n/a)</td><td>397.34 (n/a)</td><td>459.40 (n/a)</td><td>236.80 (n/a)</td><td>116.42 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (-10.07%)</td><td>0.10 (+15.34%)</td><td>0.09 <b>(+23.92%)</b></td><td>0.06 <b>(+70.47%)</b></td><td>0.04 <b>(-37.84%)</b></td><td>540.40 <b>(-41.33%)</b></td><td>360.84 <b>(-32.56%)</b></td><td>368.20 (-19.29%)</td><td>216.60 (+11.19%)</td><td>123.49 <b>(-61.98%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>921.10 (n/a)</td><td>535.06 (n/a)</td><td>456.20 (n/a)</td><td>194.80 (n/a)</td><td>324.83 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (-2.87%)</td><td>0.08 <b>(-22.28%)</b></td><td>0.07 <b>(-39.75%)</b></td><td>0.06 (+18.85%)</td><td>0.02 (-15.09%)</td><td>537.30 (-15.86%)</td><td>444.22 <b>(+23.39%)</b></td><td>489.10 <b>(+65.97%)</b></td><td>273.30 (+2.98%)</td><td>108.24 <b>(-31.06%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>638.60 (n/a)</td><td>360.00 (n/a)</td><td>294.70 (n/a)</td><td>265.40 (n/a)</td><td>157.01 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (-16.85%)</td><td>0.09 (+4.90%)</td><td>0.08 (+17.57%)</td><td>0.06 <b>(+331.03%)</b></td><td>0.04 <b>(-39.54%)</b></td><td>582.00 <b>(-76.80%)</b></td><td>405.18 <b>(-49.04%)</b></td><td>412.90 (-14.95%)</td><td>236.90 <b>(+20.25%)</b></td><td>150.67 <b>(-84.44%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.06 (n/a)</td><td>2508.50 (n/a)</td><td>795.12 (n/a)</td><td>485.50 (n/a)</td><td>197.00 (n/a)</td><td>968.15 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (-18.24%)</td><td>0.07 <b>(-22.31%)</b></td><td>0.06 (-11.60%)</td><td>0.06 (-7.03%)</td><td>0.02 <b>(-36.92%)</b></td><td>591.20 (+7.57%)</td><td>493.18 <b>(+23.15%)</b></td><td>520.10 (+13.14%)</td><td>312.10 <b>(+22.30%)</b></td><td>106.07 (-17.96%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>549.60 (n/a)</td><td>400.46 (n/a)</td><td>459.70 (n/a)</td><td>255.20 (n/a)</td><td>129.28 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+12.73%)</td><td>0.01 <b>(+32.87%)</b></td><td>0.01 <b>(+44.60%)</b></td><td>0.01 <b>(+47.75%)</b></td><td>0.00 <b>(-31.44%)</b></td><td>346.80 <b>(-32.32%)</b></td><td>295.54 <b>(-26.60%)</b></td><td>286.20 <b>(-30.84%)</b></td><td>265.20 (-11.30%)</td><td>34.25 <b>(-58.76%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.40 (n/a)</td><td>402.64 (n/a)</td><td>413.80 (n/a)</td><td>299.00 (n/a)</td><td>83.06 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+2.67%)</td><td>0.01 <b>(-26.08%)</b></td><td>0.01 <b>(-34.48%)</b></td><td>0.01 <b>(-28.93%)</b></td><td>0.00 <b>(+72.56%)</b></td><td>512.80 <b>(+40.72%)</b></td><td>415.96 <b>(+44.69%)</b></td><td>418.90 <b>(+52.60%)</b></td><td>223.80 (-2.61%)</td><td>116.66 <b>(+127.26%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>364.40 (n/a)</td><td>287.48 (n/a)</td><td>274.50 (n/a)</td><td>229.80 (n/a)</td><td>51.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+13.70%)</td><td>0.01 <b>(+21.39%)</b></td><td>0.02 <b>(+57.44%)</b></td><td>0.01 (-16.07%)</td><td>0.00 <b>(+65.45%)</b></td><td>591.50 (+19.13%)</td><td>363.48 (-10.09%)</td><td>267.40 <b>(-36.48%)</b></td><td>232.10 (-12.05%)</td><td>158.34 <b>(+80.09%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.50 (n/a)</td><td>404.26 (n/a)</td><td>421.00 (n/a)</td><td>263.90 (n/a)</td><td>87.92 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (-11.23%)</td><td>0.01 (-6.80%)</td><td>0.01 (-7.65%)</td><td>0.01 <b>(+280.97%)</b></td><td>0.00 <b>(-40.80%)</b></td><td>523.70 <b>(-73.75%)</b></td><td>361.24 <b>(-40.28%)</b></td><td>290.70 (+8.31%)</td><td>244.70 (+12.66%)</td><td>124.30 <b>(-84.01%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1994.90 (n/a)</td><td>604.84 (n/a)</td><td>268.40 (n/a)</td><td>217.20 (n/a)</td><td>777.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 <b>(-25.97%)</b></td><td>0.01 (-6.77%)</td><td>0.01 <b>(+30.16%)</b></td><td>0.01 (-12.37%)</td><td>0.00 <b>(-27.57%)</b></td><td>641.80 (+14.12%)</td><td>425.86 (+4.32%)</td><td>353.10 <b>(-23.16%)</b></td><td>265.70 <b>(+35.08%)</b></td><td>176.21 (+10.66%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.40 (n/a)</td><td>408.24 (n/a)</td><td>459.50 (n/a)</td><td>196.70 (n/a)</td><td>159.23 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (-1.26%)</td><td>0.01 (-7.65%)</td><td>0.01 (+9.80%)</td><td>0.01 (-3.51%)</td><td>0.00 (-12.15%)</td><td>534.70 (+3.62%)</td><td>396.88 (+6.07%)</td><td>370.40 (-8.93%)</td><td>228.30 (+1.24%)</td><td>120.52 (-6.58%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>516.00 (n/a)</td><td>374.18 (n/a)</td><td>406.70 (n/a)</td><td>225.50 (n/a)</td><td>129.00 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+2.87%)</td><td>0.01 (-11.42%)</td><td>0.01 <b>(-29.33%)</b></td><td>0.01 (-6.13%)</td><td>0.00 <b>(+34.01%)</b></td><td>609.50 (+6.54%)</td><td>419.86 (+19.46%)</td><td>426.60 <b>(+41.49%)</b></td><td>252.30 (-2.77%)</td><td>166.20 <b>(+29.04%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.10 (n/a)</td><td>351.46 (n/a)</td><td>301.50 (n/a)</td><td>259.50 (n/a)</td><td>128.80 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+7.57%)</td><td>0.01 (-0.51%)</td><td>0.01 (-8.10%)</td><td>0.01 (+10.37%)</td><td>0.00 (+15.45%)</td><td>491.70 (-9.40%)</td><td>392.42 (+1.96%)</td><td>449.00 (+8.82%)</td><td>241.30 (-7.05%)</td><td>117.53 (+3.49%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>542.70 (n/a)</td><td>384.86 (n/a)</td><td>412.60 (n/a)</td><td>259.60 (n/a)</td><td>113.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+19.12%)</td><td>0.01 (+2.02%)</td><td>0.01 (+13.81%)</td><td>0.01 (-16.23%)</td><td>0.00 <b>(+32.54%)</b></td><td>685.00 (+19.38%)</td><td>453.02 (+2.22%)</td><td>444.20 (-12.14%)</td><td>244.70 (-16.03%)</td><td>160.09 <b>(+30.26%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.80 (n/a)</td><td>443.18 (n/a)</td><td>505.60 (n/a)</td><td>291.40 (n/a)</td><td>122.90 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+1.12%)</td><td>0.01 (-3.52%)</td><td>0.01 <b>(-20.96%)</b></td><td>0.01 (-1.95%)</td><td>0.00 (+12.99%)</td><td>555.90 (+2.00%)</td><td>397.38 (+5.42%)</td><td>437.90 <b>(+26.52%)</b></td><td>250.40 (-1.11%)</td><td>126.55 (+9.32%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.00 (n/a)</td><td>376.94 (n/a)</td><td>346.10 (n/a)</td><td>253.20 (n/a)</td><td>115.76 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (-4.97%)</td><td>0.01 (-2.17%)</td><td>0.01 (-18.39%)</td><td>0.01 <b>(+83.15%)</b></td><td>0.00 <b>(-31.88%)</b></td><td>626.80 <b>(-45.40%)</b></td><td>460.08 (-13.52%)</td><td>466.20 <b>(+22.52%)</b></td><td>303.80 (+5.23%)</td><td>125.73 <b>(-64.27%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1147.90 (n/a)</td><td>532.02 (n/a)</td><td>380.50 (n/a)</td><td>288.70 (n/a)</td><td>351.89 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+8.48%)</td><td>0.01 <b>(+40.09%)</b></td><td>0.01 <b>(+50.47%)</b></td><td>0.01 <b>(+26.89%)</b></td><td>0.00 (-5.54%)</td><td>515.20 <b>(-21.19%)</b></td><td>356.34 <b>(-31.22%)</b></td><td>372.40 <b>(-33.54%)</b></td><td>229.80 (-7.78%)</td><td>112.90 <b>(-27.40%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>653.70 (n/a)</td><td>518.12 (n/a)</td><td>560.30 (n/a)</td><td>249.20 (n/a)</td><td>155.51 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (-10.44%)</td><td>0.02 (-1.30%)</td><td>0.03 (+4.13%)</td><td>0.02 (-10.45%)</td><td>0.01 (-6.68%)</td><td>513.10 (+11.66%)</td><td>353.26 (+1.47%)</td><td>294.50 (-3.95%)</td><td>264.40 (+11.66%)</td><td>108.05 (+8.92%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>459.50 (n/a)</td><td>348.14 (n/a)</td><td>306.60 (n/a)</td><td>236.80 (n/a)</td><td>99.21 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (-0.64%)</td><td>0.03 (+10.14%)</td><td>0.03 (+2.54%)</td><td>0.02 <b>(+27.39%)</b></td><td>0.01 <b>(-25.48%)</b></td><td>493.70 <b>(-21.50%)</b></td><td>337.62 (-14.62%)</td><td>293.10 (-2.46%)</td><td>264.50 (+0.65%)</td><td>94.46 <b>(-40.50%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.90 (n/a)</td><td>395.44 (n/a)</td><td>300.50 (n/a)</td><td>262.80 (n/a)</td><td>158.75 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (-3.58%)</td><td>0.02 (-8.03%)</td><td>0.02 (-8.14%)</td><td>0.02 (+15.95%)</td><td>0.01 (-17.35%)</td><td>528.20 (-13.75%)</td><td>415.36 (+4.76%)</td><td>480.90 (+8.87%)</td><td>251.00 (+3.72%)</td><td>131.41 (-16.29%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.40 (n/a)</td><td>396.50 (n/a)</td><td>441.70 (n/a)</td><td>242.00 (n/a)</td><td>156.98 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (+5.34%)</td><td>0.03 (-1.63%)</td><td>0.03 (-5.52%)</td><td>0.02 <b>(+29.47%)</b></td><td>0.01 (-17.90%)</td><td>500.40 <b>(-22.75%)</b></td><td>343.76 (-3.88%)</td><td>311.40 (+5.85%)</td><td>252.90 (-5.10%)</td><td>96.01 <b>(-41.01%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>647.80 (n/a)</td><td>357.64 (n/a)</td><td>294.20 (n/a)</td><td>266.50 (n/a)</td><td>162.75 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 <b>(+36.44%)</b></td><td>0.03 (+2.14%)</td><td>0.03 (-1.88%)</td><td>0.01 (-9.47%)</td><td>0.01 <b>(+60.17%)</b></td><td>660.30 (+10.46%)</td><td>385.74 (+7.16%)</td><td>299.50 (+1.94%)</td><td>194.30 <b>(-26.68%)</b></td><td>187.96 <b>(+34.06%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.80 (n/a)</td><td>359.96 (n/a)</td><td>293.80 (n/a)</td><td>265.00 (n/a)</td><td>140.21 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 <b>(-26.90%)</b></td><td>0.02 (-18.34%)</td><td>0.02 <b>(-21.70%)</b></td><td>0.02 <b>(+58.41%)</b></td><td>0.00 <b>(-71.71%)</b></td><td>479.70 <b>(-36.87%)</b></td><td>428.98 (+7.59%)</td><td>420.10 <b>(+27.69%)</b></td><td>362.20 <b>(+36.78%)</b></td><td>46.01 <b>(-77.46%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>759.90 (n/a)</td><td>398.72 (n/a)</td><td>329.00 (n/a)</td><td>264.80 (n/a)</td><td>204.06 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 <b>(-24.07%)</b></td><td>0.02 <b>(-30.75%)</b></td><td>0.02 <b>(-37.92%)</b></td><td>0.01 (-9.79%)</td><td>0.01 <b>(-27.47%)</b></td><td>604.00 (+10.85%)</td><td>473.46 <b>(+41.27%)</b></td><td>487.10 <b>(+61.08%)</b></td><td>296.10 <b>(+31.72%)</b></td><td>124.65 (+0.59%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.90 (n/a)</td><td>335.14 (n/a)</td><td>302.40 (n/a)</td><td>224.80 (n/a)</td><td>123.91 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 <b>(-42.60%)</b></td><td>0.03 (+3.72%)</td><td>0.03 <b>(+44.45%)</b></td><td>0.01 <b>(+237.72%)</b></td><td>0.01 <b>(-63.82%)</b></td><td>577.00 <b>(-70.39%)</b></td><td>338.68 <b>(-48.07%)</b></td><td>292.60 <b>(-30.76%)</b></td><td>249.70 <b>(+74.13%)</b></td><td>134.60 <b>(-81.71%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1948.80 (n/a)</td><td>652.16 (n/a)</td><td>422.60 (n/a)</td><td>143.40 (n/a)</td><td>735.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (+5.64%)</td><td>0.02 (+1.91%)</td><td>0.02 (-10.91%)</td><td>0.02 (-4.50%)</td><td>0.01 <b>(+30.00%)</b></td><td>544.40 (+4.71%)</td><td>419.28 (+2.41%)</td><td>492.40 (+12.24%)</td><td>261.10 (-5.33%)</td><td>145.16 <b>(+24.65%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.90 (n/a)</td><td>409.42 (n/a)</td><td>438.70 (n/a)</td><td>275.80 (n/a)</td><td>116.45 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (+19.61%)</td><td>0.03 <b>(+20.43%)</b></td><td>0.03 <b>(+45.42%)</b></td><td>0.02 <b>(+28.50%)</b></td><td>0.01 (+11.85%)</td><td>478.20 <b>(-22.19%)</b></td><td>348.34 (-17.71%)</td><td>298.90 <b>(-31.22%)</b></td><td>238.90 (-16.41%)</td><td>103.58 <b>(-22.02%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.60 (n/a)</td><td>423.30 (n/a)</td><td>434.60 (n/a)</td><td>285.80 (n/a)</td><td>132.82 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 (-10.39%)</td><td>0.02 (-13.63%)</td><td>0.02 <b>(-35.09%)</b></td><td>0.01 <b>(+85.54%)</b></td><td>0.01 <b>(-50.80%)</b></td><td>550.00 <b>(-46.10%)</b></td><td>436.88 (-7.51%)</td><td>444.80 <b>(+54.07%)</b></td><td>293.70 (+11.59%)</td><td>98.80 <b>(-69.58%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1020.40 (n/a)</td><td>472.36 (n/a)</td><td>288.70 (n/a)</td><td>263.20 (n/a)</td><td>324.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 <b>(-32.48%)</b></td><td>0.02 <b>(-27.29%)</b></td><td>0.02 <b>(-34.19%)</b></td><td>0.02 (+5.23%)</td><td>0.00 <b>(-69.56%)</b></td><td>525.80 (-4.97%)</td><td>463.98 <b>(+27.95%)</b></td><td>463.40 <b>(+51.93%)</b></td><td>381.40 <b>(+48.12%)</b></td><td>53.04 <b>(-57.62%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.30 (n/a)</td><td>362.64 (n/a)</td><td>305.00 (n/a)</td><td>257.50 (n/a)</td><td>125.14 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (+0.15%)</td><td>0.05 (-3.75%)</td><td>0.04 <b>(-24.99%)</b></td><td>0.03 (+1.36%)</td><td>0.02 (+18.23%)</td><td>499.20 (-1.32%)</td><td>379.96 (+6.21%)</td><td>441.20 <b>(+33.33%)</b></td><td>249.90 (-0.16%)</td><td>119.31 (+11.28%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>505.90 (n/a)</td><td>357.74 (n/a)</td><td>330.90 (n/a)</td><td>250.30 (n/a)</td><td>107.22 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (-5.35%)</td><td>0.05 (-11.63%)</td><td>0.06 (-15.33%)</td><td>0.03 <b>(-29.66%)</b></td><td>0.02 (+15.80%)</td><td>602.80 <b>(+42.17%)</b></td><td>333.46 (+19.73%)</td><td>278.90 (+18.08%)</td><td>244.60 (+5.66%)</td><td>151.34 <b>(+82.75%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>424.00 (n/a)</td><td>278.50 (n/a)</td><td>236.20 (n/a)</td><td>231.50 (n/a)</td><td>82.81 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (+6.22%)</td><td>0.05 (+18.63%)</td><td>0.05 <b>(+54.21%)</b></td><td>0.02 (-3.21%)</td><td>0.02 (-3.73%)</td><td>1041.10 (+3.31%)</td><td>445.62 (-13.94%)</td><td>314.40 <b>(-35.15%)</b></td><td>229.60 (-5.82%)</td><td>335.27 (+9.91%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1007.70 (n/a)</td><td>517.82 (n/a)</td><td>484.80 (n/a)</td><td>243.80 (n/a)</td><td>305.04 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (-2.10%)</td><td>0.05 (+13.62%)</td><td>0.06 <b>(+71.57%)</b></td><td>0.02 <b>(-35.91%)</b></td><td>0.02 (+1.93%)</td><td>784.90 <b>(+56.01%)</b></td><td>375.38 (-5.39%)</td><td>282.40 <b>(-41.73%)</b></td><td>245.00 (+2.17%)</td><td>230.36 <b>(+68.98%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>503.10 (n/a)</td><td>396.76 (n/a)</td><td>484.60 (n/a)</td><td>239.80 (n/a)</td><td>136.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (+10.21%)</td><td>0.05 (-8.71%)</td><td>0.05 <b>(-22.25%)</b></td><td>0.03 <b>(+20.85%)</b></td><td>0.02 (+7.06%)</td><td>495.50 (-17.25%)</td><td>359.30 (+7.44%)</td><td>360.10 <b>(+28.61%)</b></td><td>224.70 (-9.25%)</td><td>113.81 <b>(-23.43%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>598.80 (n/a)</td><td>334.42 (n/a)</td><td>280.00 (n/a)</td><td>247.60 (n/a)</td><td>148.63 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (-12.91%)</td><td>0.04 <b>(-24.81%)</b></td><td>0.04 <b>(-34.83%)</b></td><td>0.03 (+2.88%)</td><td>0.01 <b>(-26.55%)</b></td><td>476.20 (-2.80%)</td><td>409.38 <b>(+29.65%)</b></td><td>430.30 <b>(+53.46%)</b></td><td>286.00 (+14.81%)</td><td>74.46 <b>(-24.48%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>489.90 (n/a)</td><td>315.76 (n/a)</td><td>280.40 (n/a)</td><td>249.10 (n/a)</td><td>98.59 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (-7.96%)</td><td>0.04 (-18.42%)</td><td>0.04 <b>(-34.53%)</b></td><td>0.03 (-2.81%)</td><td>0.01 <b>(-23.42%)</b></td><td>473.70 (+2.89%)</td><td>405.44 (+19.97%)</td><td>433.20 <b>(+52.75%)</b></td><td>276.30 (+8.65%)</td><td>76.40 (-18.60%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>460.40 (n/a)</td><td>337.94 (n/a)</td><td>283.60 (n/a)</td><td>254.30 (n/a)</td><td>93.85 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 <b>(-22.43%)</b></td><td>0.04 <b>(-31.78%)</b></td><td>0.04 <b>(-43.62%)</b></td><td>0.03 <b>(-23.36%)</b></td><td>0.01 <b>(-37.50%)</b></td><td>626.00 <b>(+30.47%)</b></td><td>465.72 <b>(+41.50%)</b></td><td>425.90 <b>(+77.38%)</b></td><td>297.90 <b>(+28.91%)</b></td><td>138.02 (+8.96%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>479.80 (n/a)</td><td>329.12 (n/a)</td><td>240.10 (n/a)</td><td>231.10 (n/a)</td><td>126.67 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 <b>(+21.84%)</b></td><td>0.04 (+8.83%)</td><td>0.04 (+11.77%)</td><td>0.03 (+6.44%)</td><td>0.02 <b>(+26.96%)</b></td><td>594.30 (-6.05%)</td><td>434.86 (-6.95%)</td><td>441.00 (-10.55%)</td><td>207.70 (-17.91%)</td><td>141.94 (-11.56%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>632.60 (n/a)</td><td>467.36 (n/a)</td><td>493.00 (n/a)</td><td>253.00 (n/a)</td><td>160.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (-17.15%)</td><td>0.04 (-16.97%)</td><td>0.04 <b>(-26.31%)</b></td><td>0.03 (+13.17%)</td><td>0.01 <b>(-39.92%)</b></td><td>564.00 (-11.63%)</td><td>406.36 (+10.27%)</td><td>383.50 <b>(+35.70%)</b></td><td>274.80 <b>(+20.69%)</b></td><td>112.15 <b>(-35.18%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>638.20 (n/a)</td><td>368.50 (n/a)</td><td>282.60 (n/a)</td><td>227.70 (n/a)</td><td>173.03 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (+8.47%)</td><td>0.04 (+9.46%)</td><td>0.04 (+6.25%)</td><td>0.02 <b>(+225.72%)</b></td><td>0.01 <b>(-34.06%)</b></td><td>735.40 <b>(-69.30%)</b></td><td>475.98 <b>(-42.43%)</b></td><td>457.90 (-5.88%)</td><td>282.20 (-7.81%)</td><td>163.17 <b>(-81.61%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2395.40 (n/a)</td><td>826.74 (n/a)</td><td>486.50 (n/a)</td><td>306.10 (n/a)</td><td>887.30 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 <b>(-28.46%)</b></td><td>0.05 (-6.22%)</td><td>0.05 (-1.37%)</td><td>0.03 <b>(+20.41%)</b></td><td>0.01 <b>(-36.10%)</b></td><td>557.90 (-16.94%)</td><td>371.36 (-2.17%)</td><td>309.40 (+1.38%)</td><td>266.20 <b>(+39.81%)</b></td><td>129.72 <b>(-29.66%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>671.70 (n/a)</td><td>379.60 (n/a)</td><td>305.20 (n/a)</td><td>190.40 (n/a)</td><td>184.43 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (+12.72%)</td><td>0.11 (-8.41%)</td><td>0.11 <b>(-20.21%)</b></td><td>0.07 (-0.27%)</td><td>0.04 (+17.50%)</td><td>500.90 (+0.26%)</td><td>329.72 (+10.73%)</td><td>301.80 <b>(+25.33%)</b></td><td>207.40 (-11.29%)</td><td>117.19 (+2.79%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>499.60 (n/a)</td><td>297.78 (n/a)</td><td>240.80 (n/a)</td><td>233.80 (n/a)</td><td>114.02 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (+6.41%)</td><td>0.12 (+5.55%)</td><td>0.12 (+1.68%)</td><td>0.06 (-4.29%)</td><td>0.03 (+14.62%)</td><td>524.50 (+4.48%)</td><td>308.56 (-3.25%)</td><td>271.20 (-1.67%)</td><td>228.40 (-6.05%)</td><td>122.08 (+15.44%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>502.00 (n/a)</td><td>318.94 (n/a)</td><td>275.80 (n/a)</td><td>243.10 (n/a)</td><td>105.75 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 <b>(+82.21%)</b></td><td>0.10 <b>(+66.98%)</b></td><td>0.10 <b>(+49.76%)</b></td><td>0.06 <b>(+358.81%)</b></td><td>0.03 <b>(+33.11%)</b></td><td>529.30 <b>(-78.20%)</b></td><td>374.48 <b>(-56.61%)</b></td><td>312.20 <b>(-33.22%)</b></td><td>246.90 <b>(-45.11%)</b></td><td>139.89 <b>(-84.02%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2428.30 (n/a)</td><td>863.00 (n/a)</td><td>467.50 (n/a)</td><td>449.80 (n/a)</td><td>875.24 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (-5.80%)</td><td>0.09 (-7.13%)</td><td>0.07 (-5.85%)</td><td>0.07 (+4.89%)</td><td>0.02 <b>(-24.36%)</b></td><td>492.50 (-4.65%)</td><td>407.94 (+4.03%)</td><td>473.00 (+6.20%)</td><td>270.80 (+6.15%)</td><td>100.94 (-18.57%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>516.50 (n/a)</td><td>392.12 (n/a)</td><td>445.40 (n/a)</td><td>255.10 (n/a)</td><td>123.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 <b>(-44.40%)</b></td><td>0.07 <b>(-31.18%)</b></td><td>0.07 (-18.14%)</td><td>0.06 (+5.99%)</td><td>0.01 <b>(-76.10%)</b></td><td>548.00 (-5.65%)</td><td>470.80 <b>(+27.44%)</b></td><td>460.10 <b>(+22.17%)</b></td><td>377.00 <b>(+79.87%)</b></td><td>65.48 <b>(-57.58%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>580.80 (n/a)</td><td>369.44 (n/a)</td><td>376.60 (n/a)</td><td>209.60 (n/a)</td><td>154.34 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.18 (+11.02%)</td><td>0.11 (-0.74%)</td><td>0.10 (-8.65%)</td><td>0.07 (-3.17%)</td><td>0.05 (+16.34%)</td><td>471.10 (+3.29%)</td><td>337.22 (+2.59%)</td><td>325.80 (+9.48%)</td><td>180.30 (-9.94%)</td><td>119.17 (+4.10%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>456.10 (n/a)</td><td>328.72 (n/a)</td><td>297.60 (n/a)</td><td>200.20 (n/a)</td><td>114.47 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (-2.07%)</td><td>0.09 (-11.86%)</td><td>0.06 <b>(-40.38%)</b></td><td>0.03 <b>(-43.81%)</b></td><td>0.05 <b>(+33.97%)</b></td><td>1012.90 <b>(+77.95%)</b></td><td>509.84 <b>(+34.08%)</b></td><td>513.10 <b>(+67.73%)</b></td><td>238.20 (+2.14%)</td><td>314.18 <b>(+114.14%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>569.20 (n/a)</td><td>380.26 (n/a)</td><td>305.90 (n/a)</td><td>233.20 (n/a)</td><td>146.72 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 <b>(-53.53%)</b></td><td>0.06 <b>(-42.31%)</b></td><td>0.06 <b>(-46.49%)</b></td><td>0.05 <b>(-21.86%)</b></td><td>0.00 <b>(-88.51%)</b></td><td>603.70 <b>(+27.98%)</b></td><td>559.10 <b>(+60.26%)</b></td><td>560.00 <b>(+86.85%)</b></td><td>510.60 <b>(+115.17%)</b></td><td>33.42 <b>(-70.35%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>471.70 (n/a)</td><td>348.88 (n/a)</td><td>299.70 (n/a)</td><td>237.30 (n/a)</td><td>112.71 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 (-11.00%)</td><td>0.10 <b>(+29.51%)</b></td><td>0.11 <b>(+70.03%)</b></td><td>0.05 <b>(+291.61%)</b></td><td>0.04 <b>(-23.55%)</b></td><td>617.20 <b>(-74.47%)</b></td><td>399.96 <b>(-51.05%)</b></td><td>289.90 <b>(-41.18%)</b></td><td>248.10 (+12.36%)</td><td>178.56 <b>(-80.21%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2417.10 (n/a)</td><td>817.12 (n/a)</td><td>492.90 (n/a)</td><td>220.80 (n/a)</td><td>902.19 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (+0.69%)</td><td>0.12 <b>(+37.03%)</b></td><td>0.12 <b>(+89.36%)</b></td><td>0.09 <b>(+62.20%)</b></td><td>0.02 <b>(-45.23%)</b></td><td>372.40 <b>(-38.35%)</b></td><td>284.80 <b>(-35.37%)</b></td><td>264.40 <b>(-47.19%)</b></td><td>237.40 (-0.67%)</td><td>56.79 <b>(-67.13%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>604.10 (n/a)</td><td>440.68 (n/a)</td><td>500.70 (n/a)</td><td>239.00 (n/a)</td><td>172.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 <b>(+39.88%)</b></td><td>0.09 <b>(+24.36%)</b></td><td>0.09 (-2.31%)</td><td>0.07 <b>(+38.77%)</b></td><td>0.03 <b>(+23.85%)</b></td><td>460.90 <b>(-27.93%)</b></td><td>365.68 <b>(-20.53%)</b></td><td>374.60 (+2.35%)</td><td>254.70 <b>(-28.50%)</b></td><td>92.37 <b>(-33.36%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>639.50 (n/a)</td><td>460.12 (n/a)</td><td>366.00 (n/a)</td><td>356.20 (n/a)</td><td>138.61 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 <b>(+37.37%)</b></td><td>0.08 <b>(+25.85%)</b></td><td>0.10 <b>(+65.29%)</b></td><td>0.01 <b>(-72.25%)</b></td><td>0.06 <b>(+173.76%)</b></td><td>2507.70 <b>(+260.30%)</b></td><td>878.06 <b>(+65.38%)</b></td><td>340.40 <b>(-39.51%)</b></td><td>232.20 <b>(-27.21%)</b></td><td>974.63 <b>(+609.39%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>696.00 (n/a)</td><td>530.94 (n/a)</td><td>562.70 (n/a)</td><td>319.00 (n/a)</td><td>137.39 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+11.73%)</td><td>0.01 <b>(+20.32%)</b></td><td>0.01 <b>(+49.56%)</b></td><td>0.01 <b>(+63.90%)</b></td><td>0.00 <b>(-32.32%)</b></td><td>458.30 <b>(-38.99%)</b></td><td>322.70 <b>(-28.07%)</b></td><td>314.60 <b>(-33.13%)</b></td><td>210.70 (-10.53%)</td><td>88.26 <b>(-59.44%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>751.20 (n/a)</td><td>448.66 (n/a)</td><td>470.50 (n/a)</td><td>235.50 (n/a)</td><td>217.59 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 <b>(-22.74%)</b></td><td>0.02 <b>(-29.91%)</b></td><td>0.01 <b>(-37.75%)</b></td><td>0.01 <b>(-21.16%)</b></td><td>0.01 (-14.98%)</td><td>565.60 <b>(+26.84%)</b></td><td>406.14 <b>(+44.48%)</b></td><td>415.40 <b>(+60.63%)</b></td><td>250.80 <b>(+29.41%)</b></td><td>133.47 <b>(+34.84%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>445.90 (n/a)</td><td>281.10 (n/a)</td><td>258.60 (n/a)</td><td>193.80 (n/a)</td><td>98.99 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (-3.28%)</td><td>0.01 (-16.05%)</td><td>0.01 <b>(-36.95%)</b></td><td>0.01 (+10.09%)</td><td>0.00 <b>(-24.52%)</b></td><td>525.40 (-9.16%)</td><td>418.54 (+13.21%)</td><td>425.00 <b>(+58.64%)</b></td><td>261.80 (+3.40%)</td><td>112.07 <b>(-25.43%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.40 (n/a)</td><td>369.70 (n/a)</td><td>267.90 (n/a)</td><td>253.20 (n/a)</td><td>150.29 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (-14.50%)</td><td>0.01 (+0.35%)</td><td>0.01 <b>(+35.36%)</b></td><td>0.01 (+2.32%)</td><td>0.00 <b>(-35.37%)</b></td><td>573.70 (-2.27%)</td><td>398.00 (-8.41%)</td><td>388.20 <b>(-26.13%)</b></td><td>276.80 (+16.99%)</td><td>124.45 <b>(-28.46%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.00 (n/a)</td><td>434.56 (n/a)</td><td>525.50 (n/a)</td><td>236.60 (n/a)</td><td>173.97 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (-9.28%)</td><td>0.01 (-7.94%)</td><td>0.01 <b>(+43.59%)</b></td><td>0.00 <b>(-50.67%)</b></td><td>0.01 (-1.58%)</td><td>1036.70 <b>(+102.72%)</b></td><td>466.54 <b>(+25.16%)</b></td><td>302.90 <b>(-30.37%)</b></td><td>227.00 (+10.25%)</td><td>332.21 <b>(+133.78%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>511.40 (n/a)</td><td>372.76 (n/a)</td><td>435.00 (n/a)</td><td>205.90 (n/a)</td><td>142.10 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+6.62%)</td><td>0.01 <b>(+24.77%)</b></td><td>0.01 <b>(+23.81%)</b></td><td>0.01 <b>(+119.01%)</b></td><td>0.00 <b>(-22.26%)</b></td><td>488.30 <b>(-54.33%)</b></td><td>432.16 <b>(-30.08%)</b></td><td>467.40 (-19.25%)</td><td>257.20 (-6.20%)</td><td>98.28 <b>(-66.73%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1069.30 (n/a)</td><td>618.04 (n/a)</td><td>578.80 (n/a)</td><td>274.20 (n/a)</td><td>295.39 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 <b>(+33.18%)</b></td><td>0.01 (-2.54%)</td><td>0.01 <b>(-23.93%)</b></td><td>0.01 (-7.54%)</td><td>0.01 <b>(+75.71%)</b></td><td>647.60 (+8.15%)</td><td>495.38 (+15.00%)</td><td>566.60 <b>(+31.46%)</b></td><td>197.00 <b>(-24.90%)</b></td><td>190.79 <b>(+42.81%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.80 (n/a)</td><td>430.76 (n/a)</td><td>431.00 (n/a)</td><td>262.30 (n/a)</td><td>133.60 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 (-19.29%)</td><td>0.01 <b>(-23.87%)</b></td><td>0.01 <b>(-25.68%)</b></td><td>0.01 (-8.93%)</td><td>0.00 <b>(-25.40%)</b></td><td>609.30 (+9.80%)</td><td>496.96 <b>(+29.52%)</b></td><td>467.90 <b>(+34.57%)</b></td><td>335.50 <b>(+23.89%)</b></td><td>114.31 (+2.44%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>554.90 (n/a)</td><td>383.68 (n/a)</td><td>347.70 (n/a)</td><td>270.80 (n/a)</td><td>111.59 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 (+18.28%)</td><td>0.01 (+10.87%)</td><td>0.01 (-9.35%)</td><td>0.01 (-9.03%)</td><td>0.00 (+16.17%)</td><td>572.70 (+9.92%)</td><td>326.64 (-7.79%)</td><td>303.30 (+10.33%)</td><td>208.70 (-15.44%)</td><td>145.40 (+10.53%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.00 (n/a)</td><td>354.22 (n/a)</td><td>274.90 (n/a)</td><td>246.80 (n/a)</td><td>131.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.02 <b>(+55.24%)</b></td><td>0.01 (+12.78%)</td><td>0.01 (+13.12%)</td><td>0.01 <b>(-24.49%)</b></td><td>0.00 <b>(+283.94%)</b></td><td>721.20 <b>(+32.43%)</b></td><td>478.32 (-2.45%)</td><td>446.60 (-11.60%)</td><td>265.30 <b>(-35.58%)</b></td><td>165.70 <b>(+222.82%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>544.60 (n/a)</td><td>490.32 (n/a)</td><td>505.20 (n/a)</td><td>411.80 (n/a)</td><td>51.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.01 <b>(-29.24%)</b></td><td>0.01 <b>(-32.57%)</b></td><td>0.01 (-19.66%)</td><td>0.00 <b>(-48.19%)</b></td><td>0.00 (+13.18%)</td><td>1026.70 <b>(+93.03%)</b></td><td>677.26 <b>(+65.78%)</b></td><td>474.70 <b>(+24.50%)</b></td><td>411.10 <b>(+41.32%)</b></td><td>308.37 <b>(+224.79%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.90 (n/a)</td><td>408.54 (n/a)</td><td>381.30 (n/a)</td><td>290.90 (n/a)</td><td>94.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 <b>(+51.09%)</b></td><td>0.04 <b>(+28.93%)</b></td><td>0.03 (+8.61%)</td><td>0.02 <b>(+30.01%)</b></td><td>0.01 <b>(+66.19%)</b></td><td>408.00 <b>(-23.09%)</b></td><td>253.44 <b>(-20.20%)</b></td><td>247.10 (-7.90%)</td><td>156.00 <b>(-33.79%)</b></td><td>100.96 (-18.27%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.50 (n/a)</td><td>317.60 (n/a)</td><td>268.30 (n/a)</td><td>235.60 (n/a)</td><td>123.53 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 <b>(-30.37%)</b></td><td>0.03 (-6.46%)</td><td>0.03 (+7.07%)</td><td>0.02 (-11.04%)</td><td>0.00 <b>(-58.78%)</b></td><td>585.90 (+12.41%)</td><td>475.22 (+3.25%)</td><td>460.80 (-6.61%)</td><td>417.50 <b>(+43.62%)</b></td><td>66.57 <b>(-31.01%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.20 (n/a)</td><td>460.26 (n/a)</td><td>493.40 (n/a)</td><td>290.70 (n/a)</td><td>96.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (+17.84%)</td><td>0.03 <b>(+40.36%)</b></td><td>0.03 <b>(+52.82%)</b></td><td>0.03 <b>(+92.99%)</b></td><td>0.00 <b>(-40.64%)</b></td><td>312.60 <b>(-48.19%)</b></td><td>258.32 <b>(-33.06%)</b></td><td>244.40 <b>(-34.56%)</b></td><td>229.30 (-15.14%)</td><td>33.06 <b>(-74.48%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.40 (n/a)</td><td>385.90 (n/a)</td><td>373.50 (n/a)</td><td>270.20 (n/a)</td><td>129.52 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (-2.91%)</td><td>0.03 (-2.87%)</td><td>0.02 (-7.00%)</td><td>0.02 (-7.93%)</td><td>0.01 (+0.51%)</td><td>572.70 (+8.61%)</td><td>426.98 (+3.48%)</td><td>466.60 (+7.54%)</td><td>289.90 (+2.98%)</td><td>124.17 (+7.23%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.30 (n/a)</td><td>412.64 (n/a)</td><td>433.90 (n/a)</td><td>281.50 (n/a)</td><td>115.80 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 <b>(+22.12%)</b></td><td>0.03 (+12.25%)</td><td>0.03 <b>(+24.24%)</b></td><td>0.01 <b>(-25.35%)</b></td><td>0.01 <b>(+49.69%)</b></td><td>747.10 <b>(+33.96%)</b></td><td>380.66 (+2.07%)</td><td>248.70 (-19.49%)</td><td>189.20 (-18.10%)</td><td>232.89 <b>(+61.84%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.70 (n/a)</td><td>372.94 (n/a)</td><td>308.90 (n/a)</td><td>231.00 (n/a)</td><td>143.90 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 <b>(-20.12%)</b></td><td>0.03 (-1.65%)</td><td>0.03 <b>(+37.82%)</b></td><td>0.02 <b>(+37.26%)</b></td><td>0.01 <b>(-60.95%)</b></td><td>463.60 <b>(-27.14%)</b></td><td>374.90 (-12.32%)</td><td>365.90 <b>(-27.44%)</b></td><td>292.50 <b>(+25.16%)</b></td><td>71.74 <b>(-60.76%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>636.30 (n/a)</td><td>427.56 (n/a)</td><td>504.30 (n/a)</td><td>233.70 (n/a)</td><td>182.80 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (-9.23%)</td><td>0.03 (+2.84%)</td><td>0.03 (+0.62%)</td><td>0.02 (+11.19%)</td><td>0.01 <b>(-20.09%)</b></td><td>478.80 (-10.07%)</td><td>290.60 (-6.32%)</td><td>255.80 (-0.62%)</td><td>214.50 (+10.17%)</td><td>106.74 (-19.26%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.40 (n/a)</td><td>310.20 (n/a)</td><td>257.40 (n/a)</td><td>194.70 (n/a)</td><td>132.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (+14.95%)</td><td>0.02 (-9.85%)</td><td>0.02 (+1.46%)</td><td>0.00 <b>(-69.53%)</b></td><td>0.01 <b>(+53.13%)</b></td><td>1894.90 <b>(+228.23%)</b></td><td>705.24 <b>(+61.34%)</b></td><td>475.70 (-1.43%)</td><td>234.60 (-12.98%)</td><td>673.29 <b>(+395.92%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>577.30 (n/a)</td><td>437.12 (n/a)</td><td>482.60 (n/a)</td><td>269.60 (n/a)</td><td>135.77 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (-6.24%)</td><td>0.02 <b>(-26.32%)</b></td><td>0.02 <b>(-46.77%)</b></td><td>0.01 (-7.09%)</td><td>0.01 (-11.23%)</td><td>586.80 (+7.63%)</td><td>453.62 <b>(+32.96%)</b></td><td>512.30 <b>(+87.86%)</b></td><td>220.70 (+6.67%)</td><td>142.89 (-4.21%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.20 (n/a)</td><td>341.18 (n/a)</td><td>272.70 (n/a)</td><td>206.90 (n/a)</td><td>149.17 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.04 (+7.13%)</td><td>0.02 (-12.54%)</td><td>0.02 <b>(-37.91%)</b></td><td>0.02 (-8.93%)</td><td>0.01 <b>(+21.46%)</b></td><td>605.50 (+9.81%)</td><td>462.92 (+19.74%)</td><td>533.70 <b>(+61.04%)</b></td><td>205.30 (-6.64%)</td><td>169.07 (+17.52%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>551.40 (n/a)</td><td>386.62 (n/a)</td><td>331.40 (n/a)</td><td>219.90 (n/a)</td><td>143.86 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.03 <b>(-24.53%)</b></td><td>0.02 (-18.20%)</td><td>0.02 (-14.89%)</td><td>0.01 <b>(-29.71%)</b></td><td>0.01 (-19.58%)</td><td>636.20 <b>(+42.26%)</b></td><td>441.24 <b>(+23.37%)</b></td><td>458.80 (+17.49%)</td><td>297.60 <b>(+32.50%)</b></td><td>138.96 <b>(+42.08%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>447.20 (n/a)</td><td>357.66 (n/a)</td><td>390.50 (n/a)</td><td>224.60 (n/a)</td><td>97.80 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (+11.50%)</td><td>0.04 (-5.83%)</td><td>0.05 (+10.19%)</td><td>0.01 <b>(-66.40%)</b></td><td>0.02 <b>(+50.13%)</b></td><td>2024.90 <b>(+197.65%)</b></td><td>679.36 <b>(+66.09%)</b></td><td>350.50 (-9.24%)</td><td>244.00 (-10.29%)</td><td>756.80 <b>(+358.26%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>680.30 (n/a)</td><td>409.02 (n/a)</td><td>386.20 (n/a)</td><td>272.00 (n/a)</td><td>165.15 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (+7.51%)</td><td>0.06 (-12.08%)</td><td>0.05 <b>(-42.48%)</b></td><td>0.05 (+1.05%)</td><td>0.02 (+5.49%)</td><td>530.20 (-1.05%)</td><td>422.06 (+14.60%)</td><td>504.40 <b>(+73.87%)</b></td><td>246.10 (-6.99%)</td><td>136.02 (+3.18%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>535.80 (n/a)</td><td>368.28 (n/a)</td><td>290.10 (n/a)</td><td>264.60 (n/a)</td><td>131.83 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (-8.93%)</td><td>0.04 <b>(-20.15%)</b></td><td>0.03 <b>(-36.33%)</b></td><td>0.03 (-10.18%)</td><td>0.01 <b>(-25.37%)</b></td><td>542.80 (+11.34%)</td><td>438.52 <b>(+22.06%)</b></td><td>471.70 <b>(+57.08%)</b></td><td>289.70 (+9.78%)</td><td>95.91 (-13.73%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>487.50 (n/a)</td><td>359.26 (n/a)</td><td>300.30 (n/a)</td><td>263.90 (n/a)</td><td>111.17 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (+8.24%)</td><td>0.05 (-11.13%)</td><td>0.04 <b>(-33.48%)</b></td><td>0.01 <b>(-65.49%)</b></td><td>0.03 <b>(+70.71%)</b></td><td>1877.00 <b>(+189.79%)</b></td><td>689.72 <b>(+74.49%)</b></td><td>514.50 <b>(+50.31%)</b></td><td>237.50 (-7.62%)</td><td>681.30 <b>(+332.46%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>647.70 (n/a)</td><td>395.28 (n/a)</td><td>342.30 (n/a)</td><td>257.10 (n/a)</td><td>157.54 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (+10.81%)</td><td>0.05 <b>(+65.57%)</b></td><td>0.06 <b>(+83.56%)</b></td><td>0.03 <b>(+263.16%)</b></td><td>0.02 (-18.73%)</td><td>537.00 <b>(-72.46%)</b></td><td>368.62 <b>(-62.26%)</b></td><td>281.60 <b>(-45.52%)</b></td><td>237.00 (-9.75%)</td><td>151.05 <b>(-81.24%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1950.20 (n/a)</td><td>976.80 (n/a)</td><td>516.90 (n/a)</td><td>262.60 (n/a)</td><td>805.28 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (-11.38%)</td><td>0.06 (+2.38%)</td><td>0.07 <b>(+72.80%)</b></td><td>0.03 (-4.44%)</td><td>0.02 (-13.28%)</td><td>746.90 (+4.65%)</td><td>432.50 (-3.26%)</td><td>301.80 <b>(-42.13%)</b></td><td>261.90 (+12.84%)</td><td>222.14 (+7.79%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>713.70 (n/a)</td><td>447.06 (n/a)</td><td>521.50 (n/a)</td><td>232.10 (n/a)</td><td>206.09 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 <b>(+129.06%)</b></td><td>0.04 <b>(+41.93%)</b></td><td>0.04 (+10.70%)</td><td>0.03 <b>(+87.10%)</b></td><td>0.02 <b>(+153.39%)</b></td><td>598.50 <b>(-46.56%)</b></td><td>450.84 <b>(-26.83%)</b></td><td>453.30 (-9.67%)</td><td>205.60 <b>(-56.35%)</b></td><td>158.16 <b>(-43.96%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1119.90 (n/a)</td><td>616.14 (n/a)</td><td>501.80 (n/a)</td><td>471.00 (n/a)</td><td>282.24 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 <b>(-23.53%)</b></td><td>0.04 <b>(-27.50%)</b></td><td>0.04 <b>(-32.70%)</b></td><td>0.03 (-0.02%)</td><td>0.01 <b>(-45.06%)</b></td><td>557.90 (+0.02%)</td><td>459.30 <b>(+32.27%)</b></td><td>421.60 <b>(+48.56%)</b></td><td>359.00 <b>(+30.78%)</b></td><td>89.53 <b>(-25.86%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>557.80 (n/a)</td><td>347.24 (n/a)</td><td>283.80 (n/a)</td><td>274.50 (n/a)</td><td>120.75 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.06 (-18.92%)</td><td>0.05 (-1.06%)</td><td>0.05 (+19.18%)</td><td>0.03 (-6.54%)</td><td>0.01 <b>(-35.79%)</b></td><td>491.70 (+7.01%)</td><td>342.62 (-2.21%)</td><td>320.60 (-16.10%)</td><td>270.60 <b>(+23.34%)</b></td><td>88.08 (-12.77%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>459.50 (n/a)</td><td>350.38 (n/a)</td><td>382.10 (n/a)</td><td>219.40 (n/a)</td><td>100.98 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (-10.65%)</td><td>0.04 (-10.58%)</td><td>0.03 (-19.24%)</td><td>0.01 <b>(-71.19%)</b></td><td>0.03 <b>(+35.66%)</b></td><td>1919.40 <b>(+247.03%)</b></td><td>718.22 <b>(+67.27%)</b></td><td>538.30 <b>(+23.83%)</b></td><td>259.20 (+11.92%)</td><td>687.20 <b>(+459.54%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>553.10 (n/a)</td><td>429.38 (n/a)</td><td>434.70 (n/a)</td><td>231.60 (n/a)</td><td>122.81 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (-11.60%)</td><td>0.04 <b>(-21.55%)</b></td><td>0.03 (-19.37%)</td><td>0.02 <b>(-39.34%)</b></td><td>0.02 (+9.21%)</td><td>779.60 <b>(+64.86%)</b></td><td>504.32 <b>(+37.49%)</b></td><td>511.30 <b>(+24.04%)</b></td><td>251.80 (+13.12%)</td><td>201.52 <b>(+102.75%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>472.90 (n/a)</td><td>366.80 (n/a)</td><td>412.20 (n/a)</td><td>222.60 (n/a)</td><td>99.39 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (+16.27%)</td><td>0.10 (+9.15%)</td><td>0.07 (+0.05%)</td><td>0.06 <b>(+35.97%)</b></td><td>0.04 (+7.58%)</td><td>518.40 <b>(-26.46%)</b></td><td>390.46 (-11.13%)</td><td>471.20 (-0.04%)</td><td>203.10 (-13.98%)</td><td>138.99 <b>(-27.11%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>704.90 (n/a)</td><td>439.36 (n/a)</td><td>471.40 (n/a)</td><td>236.10 (n/a)</td><td>190.68 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 <b>(+25.52%)</b></td><td>0.11 <b>(+41.02%)</b></td><td>0.11 <b>(+53.46%)</b></td><td>0.08 <b>(+53.40%)</b></td><td>0.02 (+3.09%)</td><td>406.70 <b>(-34.81%)</b></td><td>300.26 <b>(-31.02%)</b></td><td>289.00 <b>(-34.84%)</b></td><td>224.20 <b>(-20.33%)</b></td><td>68.25 <b>(-45.32%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>623.90 (n/a)</td><td>435.30 (n/a)</td><td>443.50 (n/a)</td><td>281.40 (n/a)</td><td>124.84 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 <b>(-20.51%)</b></td><td>0.08 <b>(-32.19%)</b></td><td>0.08 (+2.18%)</td><td>0.04 <b>(-46.54%)</b></td><td>0.05 <b>(-22.93%)</b></td><td>1095.30 <b>(+87.07%)</b></td><td>675.30 <b>(+58.70%)</b></td><td>523.60 (-2.13%)</td><td>259.30 <b>(+25.81%)</b></td><td>374.83 <b>(+96.70%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>585.50 (n/a)</td><td>425.52 (n/a)</td><td>535.00 (n/a)</td><td>206.10 (n/a)</td><td>190.56 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.11 (-8.47%)</td><td>0.07 (-12.90%)</td><td>0.07 (-3.80%)</td><td>0.05 (-14.97%)</td><td>0.02 (-9.67%)</td><td>620.80 (+17.62%)</td><td>473.42 (+14.82%)</td><td>481.50 (+3.95%)</td><td>289.40 (+9.25%)</td><td>124.34 (+12.59%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>527.80 (n/a)</td><td>412.30 (n/a)</td><td>463.20 (n/a)</td><td>264.90 (n/a)</td><td>110.44 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (-14.10%)</td><td>0.11 (+15.51%)</td><td>0.09 (+12.28%)</td><td>0.07 <b>(+99.50%)</b></td><td>0.04 <b>(-32.27%)</b></td><td>555.20 <b>(-49.87%)</b></td><td>417.08 <b>(-27.74%)</b></td><td>434.70 (-10.94%)</td><td>273.60 (+16.38%)</td><td>130.72 <b>(-61.21%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1107.60 (n/a)</td><td>577.18 (n/a)</td><td>488.10 (n/a)</td><td>235.10 (n/a)</td><td>336.99 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 <b>(-21.63%)</b></td><td>0.08 (-0.56%)</td><td>0.07 <b>(+24.88%)</b></td><td>0.06 (+14.08%)</td><td>0.01 <b>(-55.91%)</b></td><td>538.90 (-12.33%)</td><td>439.60 (-6.91%)</td><td>437.10 (-19.93%)</td><td>349.00 <b>(+27.61%)</b></td><td>73.07 <b>(-51.39%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>614.70 (n/a)</td><td>472.24 (n/a)</td><td>545.90 (n/a)</td><td>273.50 (n/a)</td><td>150.32 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 <b>(-27.77%)</b></td><td>0.09 (-6.76%)</td><td>0.09 <b>(+31.75%)</b></td><td>0.07 <b>(+22.91%)</b></td><td>0.02 <b>(-63.94%)</b></td><td>534.60 (-18.64%)</td><td>443.80 (-6.87%)</td><td>413.10 <b>(-24.10%)</b></td><td>356.50 <b>(+38.45%)</b></td><td>83.64 <b>(-57.60%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>657.10 (n/a)</td><td>476.54 (n/a)</td><td>544.30 (n/a)</td><td>257.50 (n/a)</td><td>197.29 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.11 (-5.54%)</td><td>0.08 (-4.71%)</td><td>0.11 <b>(+20.16%)</b></td><td>0.02 <b>(-67.59%)</b></td><td>0.04 <b>(+69.00%)</b></td><td>1858.30 <b>(+208.53%)</b></td><td>659.00 <b>(+60.66%)</b></td><td>299.60 (-16.80%)</td><td>291.00 (+5.90%)</td><td>679.37 <b>(+427.86%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>602.30 (n/a)</td><td>410.18 (n/a)</td><td>360.10 (n/a)</td><td>274.80 (n/a)</td><td>128.70 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.11 (-17.02%)</td><td>0.08 <b>(-24.74%)</b></td><td>0.07 <b>(-42.46%)</b></td><td>0.07 (+3.08%)</td><td>0.02 <b>(-46.48%)</b></td><td>555.10 (-2.97%)</td><td>476.72 <b>(+24.91%)</b></td><td>494.50 <b>(+73.81%)</b></td><td>335.20 <b>(+20.53%)</b></td><td>90.47 <b>(-35.06%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>572.10 (n/a)</td><td>381.64 (n/a)</td><td>284.50 (n/a)</td><td>278.10 (n/a)</td><td>139.32 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 <b>(-35.84%)</b></td><td>0.07 (-1.49%)</td><td>0.07 (+14.57%)</td><td>0.05 <b>(+269.35%)</b></td><td>0.01 <b>(-71.37%)</b></td><td>652.70 <b>(-72.93%)</b></td><td>492.28 <b>(-41.37%)</b></td><td>466.90 (-12.71%)</td><td>381.20 <b>(+55.85%)</b></td><td>99.56 <b>(-88.82%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2410.80 (n/a)</td><td>839.68 (n/a)</td><td>534.90 (n/a)</td><td>244.60 (n/a)</td><td>890.89 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (-3.30%)</td><td>0.07 <b>(+22.82%)</b></td><td>0.07 <b>(+70.83%)</b></td><td>0.04 <b>(+23.29%)</b></td><td>0.02 <b>(-28.97%)</b></td><td>488.40 (-18.88%)</td><td>312.96 <b>(-23.99%)</b></td><td>275.40 <b>(-41.45%)</b></td><td>231.90 (+3.39%)</td><td>100.95 <b>(-34.85%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>602.10 (n/a)</td><td>411.72 (n/a)</td><td>470.40 (n/a)</td><td>224.30 (n/a)</td><td>154.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (-11.50%)</td><td>0.05 <b>(-31.38%)</b></td><td>0.05 <b>(-34.22%)</b></td><td>0.03 <b>(-49.03%)</b></td><td>0.01 <b>(+221.43%)</b></td><td>622.30 <b>(+96.19%)</b></td><td>452.02 <b>(+52.75%)</b></td><td>450.70 <b>(+52.01%)</b></td><td>308.80 (+12.99%)</td><td>111.94 <b>(+611.66%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>317.20 (n/a)</td><td>295.92 (n/a)</td><td>296.50 (n/a)</td><td>273.30 (n/a)</td><td>15.73 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 <b>(-25.23%)</b></td><td>0.05 <b>(-28.87%)</b></td><td>0.04 <b>(-47.18%)</b></td><td>0.04 (-12.40%)</td><td>0.02 (-15.81%)</td><td>534.80 (+14.15%)</td><td>412.08 <b>(+41.70%)</b></td><td>484.00 <b>(+89.28%)</b></td><td>248.40 <b>(+33.76%)</b></td><td>133.03 <b>(+24.12%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>468.50 (n/a)</td><td>290.82 (n/a)</td><td>255.70 (n/a)</td><td>185.70 (n/a)</td><td>107.18 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (+4.04%)</td><td>0.05 (-14.14%)</td><td>0.04 (+3.79%)</td><td>0.04 (+2.81%)</td><td>0.02 (-13.29%)</td><td>574.10 (-2.74%)</td><td>475.06 (+11.29%)</td><td>508.80 (-3.65%)</td><td>228.20 (-3.92%)</td><td>142.94 (-17.56%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>590.30 (n/a)</td><td>426.86 (n/a)</td><td>528.10 (n/a)</td><td>237.50 (n/a)</td><td>173.38 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (-18.67%)</td><td>0.06 (-7.32%)</td><td>0.07 (-1.37%)</td><td>0.03 (+7.90%)</td><td>0.02 <b>(-23.89%)</b></td><td>648.90 (-7.31%)</td><td>412.62 (+1.73%)</td><td>304.40 (+1.40%)</td><td>283.60 <b>(+22.98%)</b></td><td>167.78 (-16.72%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>700.10 (n/a)</td><td>405.60 (n/a)</td><td>300.20 (n/a)</td><td>230.60 (n/a)</td><td>201.46 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (-11.26%)</td><td>0.05 <b>(-20.80%)</b></td><td>0.04 <b>(-23.82%)</b></td><td>0.03 (-13.67%)</td><td>0.01 (-9.61%)</td><td>603.60 (+15.83%)</td><td>484.12 <b>(+26.72%)</b></td><td>520.20 <b>(+31.26%)</b></td><td>300.20 (+12.69%)</td><td>120.10 (+17.86%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>521.10 (n/a)</td><td>382.04 (n/a)</td><td>396.30 (n/a)</td><td>266.40 (n/a)</td><td>101.90 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (+4.21%)</td><td>0.08 (+14.33%)</td><td>0.08 (+8.27%)</td><td>0.04 (-3.66%)</td><td>0.02 (-5.08%)</td><td>558.50 (+3.81%)</td><td>341.88 (-13.19%)</td><td>300.60 (-7.62%)</td><td>271.30 (-4.03%)</td><td>121.84 (-4.88%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>538.00 (n/a)</td><td>393.82 (n/a)</td><td>325.40 (n/a)</td><td>282.70 (n/a)</td><td>128.09 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 <b>(-22.05%)</b></td><td>0.06 <b>(-27.03%)</b></td><td>0.06 <b>(-35.78%)</b></td><td>0.04 <b>(-35.56%)</b></td><td>0.02 (-9.79%)</td><td>646.30 <b>(+55.21%)</b></td><td>433.00 <b>(+41.09%)</b></td><td>416.50 <b>(+55.70%)</b></td><td>299.30 <b>(+28.29%)</b></td><td>146.57 <b>(+71.37%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>416.40 (n/a)</td><td>306.90 (n/a)</td><td>267.50 (n/a)</td><td>233.30 (n/a)</td><td>85.53 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (+3.61%)</td><td>0.06 (-16.41%)</td><td>0.06 <b>(-34.20%)</b></td><td>0.04 (-5.15%)</td><td>0.02 (-13.21%)</td><td>630.20 (+5.44%)</td><td>447.24 (+14.30%)</td><td>431.80 <b>(+51.99%)</b></td><td>239.20 (-3.47%)</td><td>142.57 (-18.44%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>597.70 (n/a)</td><td>391.28 (n/a)</td><td>284.10 (n/a)</td><td>247.80 (n/a)</td><td>174.81 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.05 <b>(-50.01%)</b></td><td>0.04 <b>(-30.49%)</b></td><td>0.05 (-9.22%)</td><td>0.04 (-4.84%)</td><td>0.01 <b>(-81.26%)</b></td><td>656.40 (+5.09%)</td><td>557.20 <b>(+27.16%)</b></td><td>522.60 (+10.16%)</td><td>491.20 <b>(+100.00%)</b></td><td>66.90 <b>(-59.76%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>624.60 (n/a)</td><td>438.20 (n/a)</td><td>474.40 (n/a)</td><td>245.60 (n/a)</td><td>166.24 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 (-9.47%)</td><td>0.07 (+1.57%)</td><td>0.08 (+16.76%)</td><td>0.04 (-8.10%)</td><td>0.03 (+1.08%)</td><td>556.50 (+8.82%)</td><td>386.00 (+0.75%)</td><td>308.00 (-14.35%)</td><td>248.00 (+10.47%)</td><td>152.90 <b>(+21.16%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>511.40 (n/a)</td><td>383.14 (n/a)</td><td>359.60 (n/a)</td><td>224.50 (n/a)</td><td>126.20 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 (-3.27%)</td><td>0.06 (-13.39%)</td><td>0.08 (-0.82%)</td><td>0.01 <b>(-66.36%)</b></td><td>0.04 <b>(+49.42%)</b></td><td>1800.40 <b>(+197.29%)</b></td><td>658.02 <b>(+75.84%)</b></td><td>293.00 (+0.83%)</td><td>263.10 (+3.38%)</td><td>659.16 <b>(+342.97%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>605.60 (n/a)</td><td>374.22 (n/a)</td><td>290.60 (n/a)</td><td>254.50 (n/a)</td><td>148.81 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.09 <b>(+30.25%)</b></td><td>0.06 <b>(+43.34%)</b></td><td>0.05 <b>(+27.77%)</b></td><td>0.04 <b>(+269.84%)</b></td><td>0.02 (-6.13%)</td><td>500.10 <b>(-72.96%)</b></td><td>357.06 <b>(-51.36%)</b></td><td>351.20 <b>(-21.75%)</b></td><td>205.10 <b>(-23.24%)</b></td><td>134.11 <b>(-79.64%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1849.70 (n/a)</td><td>734.12 (n/a)</td><td>448.80 (n/a)</td><td>267.20 (n/a)</td><td>658.60 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (+18.78%)</td><td>0.05 (-0.06%)</td><td>0.04 <b>(-26.82%)</b></td><td>0.03 (+0.34%)</td><td>0.02 <b>(+39.25%)</b></td><td>604.20 (-0.35%)</td><td>432.48 (+6.45%)</td><td>466.90 <b>(+36.64%)</b></td><td>228.10 (-15.80%)</td><td>178.81 (+19.38%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>606.30 (n/a)</td><td>406.26 (n/a)</td><td>341.70 (n/a)</td><td>270.90 (n/a)</td><td>149.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (-18.21%)</td><td>0.05 <b>(-25.80%)</b></td><td>0.04 <b>(-40.40%)</b></td><td>0.04 (+5.56%)</td><td>0.02 (-17.24%)</td><td>523.40 (-5.27%)</td><td>394.40 <b>(+30.70%)</b></td><td>430.90 <b>(+67.80%)</b></td><td>240.40 <b>(+22.28%)</b></td><td>125.12 (-12.19%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>552.50 (n/a)</td><td>301.76 (n/a)</td><td>256.80 (n/a)</td><td>196.60 (n/a)</td><td>142.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (+5.57%)</td><td>0.06 (-13.65%)</td><td>0.06 (-14.72%)</td><td>0.03 (-8.31%)</td><td>0.02 (+18.65%)</td><td>541.60 (+9.06%)</td><td>364.56 (+19.37%)</td><td>300.20 (+17.27%)</td><td>230.30 (-5.27%)</td><td>133.11 <b>(+23.25%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>496.60 (n/a)</td><td>305.40 (n/a)</td><td>256.00 (n/a)</td><td>243.10 (n/a)</td><td>108.00 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 <b>(+29.28%)</b></td><td>0.05 (+12.19%)</td><td>0.05 (+0.83%)</td><td>0.03 (+9.93%)</td><td>0.02 <b>(+51.72%)</b></td><td>546.20 (-9.04%)</td><td>406.50 (-7.80%)</td><td>406.20 (-0.83%)</td><td>246.10 <b>(-22.63%)</b></td><td>128.44 (+8.74%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>600.50 (n/a)</td><td>440.90 (n/a)</td><td>409.60 (n/a)</td><td>318.10 (n/a)</td><td>118.12 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.08 (+0.71%)</td><td>0.05 (+0.43%)</td><td>0.05 (-19.95%)</td><td>0.03 <b>(+47.34%)</b></td><td>0.02 (-14.83%)</td><td>565.00 <b>(-32.13%)</b></td><td>401.92 (-9.89%)</td><td>387.70 <b>(+24.94%)</b></td><td>244.30 (-0.69%)</td><td>148.75 <b>(-40.91%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>832.50 (n/a)</td><td>446.02 (n/a)</td><td>310.30 (n/a)</td><td>246.00 (n/a)</td><td>251.75 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.41 (-5.41%)</td><td>0.29 (-12.67%)</td><td>0.32 (-12.55%)</td><td>0.18 (+7.90%)</td><td>0.10 (+4.37%)</td><td>531.90 (-7.32%)</td><td>376.54 (+15.38%)</td><td>307.40 (+14.36%)</td><td>240.40 (+5.72%)</td><td>143.57 (+2.03%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.37 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>573.90 (n/a)</td><td>326.36 (n/a)</td><td>268.80 (n/a)</td><td>227.40 (n/a)</td><td>140.71 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.33 (-17.59%)</td><td>0.27 (-5.20%)</td><td>0.30 <b>(+22.91%)</b></td><td>0.17 (+3.61%)</td><td>0.07 <b>(-23.38%)</b></td><td>586.30 (-3.47%)</td><td>397.64 (+2.52%)</td><td>323.40 (-18.62%)</td><td>294.80 <b>(+21.37%)</b></td><td>127.59 (-10.36%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>607.40 (n/a)</td><td>387.86 (n/a)</td><td>397.40 (n/a)</td><td>242.90 (n/a)</td><td>142.33 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.22 <b>(-44.00%)</b></td><td>0.20 <b>(-24.51%)</b></td><td>0.21 <b>(-35.08%)</b></td><td>0.16 <b>(+302.27%)</b></td><td>0.03 <b>(-81.08%)</b></td><td>613.40 <b>(-75.14%)</b></td><td>499.62 <b>(-33.90%)</b></td><td>471.50 <b>(+54.03%)</b></td><td>437.00 <b>(+78.59%)</b></td><td>74.83 <b>(-92.22%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.40 (n/a)</td><td>0.27 (n/a)</td><td>0.32 (n/a)</td><td>0.04 (n/a)</td><td>0.15 (n/a)</td><td>2467.70 (n/a)</td><td>755.86 (n/a)</td><td>306.10 (n/a)</td><td>244.70 (n/a)</td><td>961.68 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.34 (+16.51%)</td><td>0.25 <b>(+28.42%)</b></td><td>0.24 <b>(+45.46%)</b></td><td>0.16 (+8.32%)</td><td>0.07 (+19.37%)</td><td>447.90 (-7.67%)</td><td>318.66 <b>(-21.59%)</b></td><td>312.80 <b>(-31.25%)</b></td><td>218.80 (-14.16%)</td><td>90.14 (-4.62%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>485.10 (n/a)</td><td>406.42 (n/a)</td><td>455.00 (n/a)</td><td>254.90 (n/a)</td><td>94.50 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.44 <b>(+48.43%)</b></td><td>0.21 (-15.65%)</td><td>0.13 <b>(-47.20%)</b></td><td>0.10 <b>(-48.51%)</b></td><td>0.15 <b>(+265.81%)</b></td><td>722.30 <b>(+94.22%)</b></td><td>477.92 <b>(+61.42%)</b></td><td>553.00 <b>(+89.38%)</b></td><td>168.40 <b>(-32.61%)</b></td><td>254.78 <b>(+408.93%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>371.90 (n/a)</td><td>296.08 (n/a)</td><td>292.00 (n/a)</td><td>249.90 (n/a)</td><td>50.06 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.36 <b>(+31.89%)</b></td><td>0.22 <b>(+21.22%)</b></td><td>0.17 (+8.59%)</td><td>0.13 (+6.91%)</td><td>0.10 <b>(+56.44%)</b></td><td>567.50 (-6.48%)</td><td>382.96 (-12.32%)</td><td>434.40 (-7.91%)</td><td>202.70 <b>(-24.17%)</b></td><td>154.21 (+9.62%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>606.80 (n/a)</td><td>436.76 (n/a)</td><td>471.70 (n/a)</td><td>267.30 (n/a)</td><td>140.68 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (-7.08%)</td><td>0.10 <b>(-30.14%)</b></td><td>0.12 (-12.51%)</td><td>0.03 <b>(-72.83%)</b></td><td>0.05 <b>(+286.62%)</b></td><td>1072.10 <b>(+268.04%)</b></td><td>510.74 <b>(+88.34%)</b></td><td>320.10 (+14.32%)</td><td>260.40 (+7.60%)</td><td>343.25 <b>(+1405.58%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>291.30 (n/a)</td><td>271.18 (n/a)</td><td>280.00 (n/a)</td><td>242.00 (n/a)</td><td>22.80 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (+5.63%)</td><td>0.10 (-3.23%)</td><td>0.11 (-7.41%)</td><td>0.06 (-0.40%)</td><td>0.04 (+2.11%)</td><td>599.10 (+0.40%)</td><td>411.02 (+3.70%)</td><td>328.30 (+8.03%)</td><td>230.90 (-5.33%)</td><td>174.97 (+2.11%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>596.70 (n/a)</td><td>396.34 (n/a)</td><td>303.90 (n/a)</td><td>243.90 (n/a)</td><td>171.35 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (+6.20%)</td><td>0.11 <b>(+26.20%)</b></td><td>0.12 <b>(+66.43%)</b></td><td>0.06 (-3.45%)</td><td>0.04 (+18.44%)</td><td>567.20 (+3.58%)</td><td>358.96 (-18.70%)</td><td>299.50 <b>(-39.92%)</b></td><td>243.20 (-5.85%)</td><td>137.43 (+14.46%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>547.60 (n/a)</td><td>441.50 (n/a)</td><td>498.50 (n/a)</td><td>258.30 (n/a)</td><td>120.07 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (+15.10%)</td><td>0.12 (+9.39%)</td><td>0.13 (+6.22%)</td><td>0.08 (+13.13%)</td><td>0.04 (+19.06%)</td><td>489.40 (-11.60%)</td><td>346.76 (-7.61%)</td><td>287.40 (-5.86%)</td><td>241.30 (-13.11%)</td><td>118.48 (-4.22%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>553.60 (n/a)</td><td>375.32 (n/a)</td><td>305.30 (n/a)</td><td>277.70 (n/a)</td><td>123.70 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (+7.83%)</td><td>0.09 (+5.06%)</td><td>0.07 (-5.77%)</td><td>0.06 (+8.66%)</td><td>0.04 (+13.38%)</td><td>579.00 (-7.96%)</td><td>467.54 (-2.91%)</td><td>553.90 (+6.13%)</td><td>225.80 (-7.27%)</td><td>152.39 (+5.18%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>629.10 (n/a)</td><td>481.56 (n/a)</td><td>521.90 (n/a)</td><td>243.50 (n/a)</td><td>144.89 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (+6.88%)</td><td>0.10 (-4.80%)</td><td>0.08 (-6.55%)</td><td>0.07 (+2.21%)</td><td>0.03 (-6.14%)</td><td>521.30 (-2.16%)</td><td>417.62 (+2.94%)</td><td>461.00 (+7.01%)</td><td>243.70 (-6.41%)</td><td>111.29 (-15.98%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>532.80 (n/a)</td><td>405.68 (n/a)</td><td>430.80 (n/a)</td><td>260.40 (n/a)</td><td>132.46 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (-0.24%)</td><td>0.12 <b>(+25.72%)</b></td><td>0.13 <b>(+37.86%)</b></td><td>0.07 <b>(+299.34%)</b></td><td>0.04 <b>(-38.72%)</b></td><td>617.80 <b>(-74.96%)</b></td><td>361.04 <b>(-54.43%)</b></td><td>318.00 <b>(-27.46%)</b></td><td>255.30 (+0.24%)</td><td>146.10 <b>(-84.50%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2467.20 (n/a)</td><td>792.22 (n/a)</td><td>438.40 (n/a)</td><td>254.70 (n/a)</td><td>942.80 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (-0.02%)</td><td>0.13 (+17.71%)</td><td>0.14 <b>(+31.79%)</b></td><td>0.09 <b>(+25.04%)</b></td><td>0.03 <b>(-23.41%)</b></td><td>468.70 <b>(-20.02%)</b></td><td>326.12 (-18.45%)</td><td>294.50 <b>(-24.14%)</b></td><td>256.00 (+0.00%)</td><td>83.34 <b>(-35.73%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>586.00 (n/a)</td><td>399.92 (n/a)</td><td>388.20 (n/a)</td><td>256.00 (n/a)</td><td>129.66 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 (+6.17%)</td><td>0.12 <b>(+22.88%)</b></td><td>0.14 <b>(+60.42%)</b></td><td>0.05 <b>(-26.12%)</b></td><td>0.04 <b>(+37.67%)</b></td><td>767.60 <b>(+35.36%)</b></td><td>398.04 (-10.85%)</td><td>298.30 <b>(-37.67%)</b></td><td>259.80 (-5.80%)</td><td>213.24 <b>(+79.73%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>567.10 (n/a)</td><td>446.50 (n/a)</td><td>478.60 (n/a)</td><td>275.80 (n/a)</td><td>118.64 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.17 (+11.13%)</td><td>0.12 (+0.25%)</td><td>0.10 <b>(-28.55%)</b></td><td>0.08 (+9.00%)</td><td>0.04 (+2.08%)</td><td>533.60 (-8.27%)</td><td>385.28 (-1.96%)</td><td>425.50 <b>(+39.97%)</b></td><td>246.10 (-9.99%)</td><td>121.70 (-18.12%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>581.70 (n/a)</td><td>393.00 (n/a)</td><td>304.00 (n/a)</td><td>273.40 (n/a)</td><td>148.63 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (-14.54%)</td><td>0.09 <b>(-35.78%)</b></td><td>0.08 <b>(-52.93%)</b></td><td>0.07 <b>(-23.01%)</b></td><td>0.03 (-4.57%)</td><td>605.50 <b>(+29.88%)</b></td><td>481.38 <b>(+58.80%)</b></td><td>534.30 <b>(+112.45%)</b></td><td>271.00 (+17.01%)</td><td>133.78 <b>(+38.57%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>466.20 (n/a)</td><td>303.14 (n/a)</td><td>251.50 (n/a)</td><td>231.60 (n/a)</td><td>96.54 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.17 (+3.85%)</td><td>0.12 (+11.12%)</td><td>0.14 <b>(+53.29%)</b></td><td>0.08 (+13.86%)</td><td>0.04 (-2.72%)</td><td>543.90 (-12.16%)</td><td>365.86 (-11.24%)</td><td>300.50 <b>(-34.77%)</b></td><td>243.20 (-3.72%)</td><td>137.80 (-10.76%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>619.20 (n/a)</td><td>412.20 (n/a)</td><td>460.70 (n/a)</td><td>252.60 (n/a)</td><td>154.41 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (-3.51%)</td><td>0.09 (-4.44%)</td><td>0.07 <b>(-32.71%)</b></td><td>0.07 <b>(+122.43%)</b></td><td>0.03 <b>(-35.02%)</b></td><td>501.10 <b>(-55.04%)</b></td><td>410.40 (-15.20%)</td><td>464.30 <b>(+48.62%)</b></td><td>286.60 (+3.65%)</td><td>106.51 <b>(-70.25%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1114.50 (n/a)</td><td>483.98 (n/a)</td><td>312.40 (n/a)</td><td>276.50 (n/a)</td><td>358.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 <b>(+44.17%)</b></td><td>0.08 (+5.76%)</td><td>0.07 (+2.47%)</td><td>0.06 (-10.77%)</td><td>0.03 <b>(+185.49%)</b></td><td>587.20 (+12.08%)</td><td>461.90 (+1.42%)</td><td>465.50 (-2.41%)</td><td>257.90 <b>(-30.63%)</b></td><td>128.40 <b>(+115.96%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>523.90 (n/a)</td><td>455.42 (n/a)</td><td>477.00 (n/a)</td><td>371.80 (n/a)</td><td>59.46 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.12 (-9.53%)</td><td>0.08 (-16.12%)</td><td>0.07 (-6.83%)</td><td>0.06 (-10.76%)</td><td>0.03 <b>(-20.79%)</b></td><td>597.50 (+12.06%)</td><td>480.24 (+16.60%)</td><td>512.50 (+7.33%)</td><td>288.50 (+10.54%)</td><td>118.21 (-5.84%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>533.20 (n/a)</td><td>411.86 (n/a)</td><td>477.50 (n/a)</td><td>261.00 (n/a)</td><td>125.55 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 <b>(-29.57%)</b></td><td>0.06 <b>(-50.98%)</b></td><td>0.08 <b>(-36.37%)</b></td><td>0.01 <b>(-82.76%)</b></td><td>0.04 <b>(+67.41%)</b></td><td>2474.10 <b>(+480.09%)</b></td><td>1116.30 <b>(+276.04%)</b></td><td>433.60 <b>(+57.16%)</b></td><td>344.20 <b>(+42.00%)</b></td><td>1007.66 <b>(+1250.26%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>426.50 (n/a)</td><td>296.86 (n/a)</td><td>275.90 (n/a)</td><td>242.40 (n/a)</td><td>74.63 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.15 (+3.24%)</td><td>0.10 <b>(+26.28%)</b></td><td>0.10 <b>(+36.65%)</b></td><td>0.08 <b>(+41.17%)</b></td><td>0.03 <b>(-24.21%)</b></td><td>445.50 <b>(-29.16%)</b></td><td>347.34 <b>(-25.45%)</b></td><td>353.40 <b>(-26.82%)</b></td><td>232.70 (-3.12%)</td><td>76.74 <b>(-45.76%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>628.90 (n/a)</td><td>465.92 (n/a)</td><td>482.90 (n/a)</td><td>240.20 (n/a)</td><td>141.49 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.16 <b>(+26.89%)</b></td><td>0.11 (+7.85%)</td><td>0.09 <b>(-20.61%)</b></td><td>0.06 (-13.50%)</td><td>0.05 <b>(+73.47%)</b></td><td>571.90 (+15.61%)</td><td>378.38 (+0.83%)</td><td>401.60 <b>(+25.97%)</b></td><td>220.20 <b>(-21.22%)</b></td><td>154.22 <b>(+41.27%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>494.70 (n/a)</td><td>375.26 (n/a)</td><td>318.80 (n/a)</td><td>279.50 (n/a)</td><td>109.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.40 <b>(-24.39%)</b></td><td>0.31 (-6.25%)</td><td>0.26 (-13.29%)</td><td>0.25 (+17.18%)</td><td>0.08 <b>(-40.06%)</b></td><td>532.10 (-14.66%)</td><td>445.86 (-0.74%)</td><td>513.30 (+15.32%)</td><td>326.60 <b>(+32.28%)</b></td><td>106.41 <b>(-35.20%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.53 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>623.50 (n/a)</td><td>449.18 (n/a)</td><td>445.10 (n/a)</td><td>246.90 (n/a)</td><td>164.21 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.45 <b>(-27.82%)</b></td><td>0.31 <b>(-26.98%)</b></td><td>0.26 <b>(-43.29%)</b></td><td>0.19 <b>(-20.39%)</b></td><td>0.11 (-18.16%)</td><td>691.70 <b>(+25.60%)</b></td><td>464.84 <b>(+37.99%)</b></td><td>506.80 <b>(+76.34%)</b></td><td>291.60 <b>(+38.53%)</b></td><td>166.34 <b>(+28.45%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.62 (n/a)</td><td>0.43 (n/a)</td><td>0.46 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>550.70 (n/a)</td><td>336.86 (n/a)</td><td>287.40 (n/a)</td><td>210.50 (n/a)</td><td>129.51 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.47 (-16.11%)</td><td>0.32 (-4.57%)</td><td>0.29 (+12.97%)</td><td>0.17 <b>(-28.46%)</b></td><td>0.12 (-15.66%)</td><td>786.00 <b>(+39.78%)</b></td><td>464.52 (+6.55%)</td><td>446.20 (-11.49%)</td><td>278.20 (+19.25%)</td><td>196.87 <b>(+42.72%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.56 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>562.30 (n/a)</td><td>435.96 (n/a)</td><td>504.10 (n/a)</td><td>233.30 (n/a)</td><td>137.94 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.00 (+0.00%)</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-60.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+6.90%)</td><td>17970.45 <b>(-20.13%)</b></td><td>12860.09 (-1.84%)</td><td>16487.71 <b>(+116.39%)</b></td><td>6525.30 (-9.42%)</td><td>5748.02 <b>(-27.22%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22498.87 (n/a)</td><td>13101.30 (n/a)</td><td>7619.61 (n/a)</td><td>7203.67 (n/a)</td><td>7897.51 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.00 (+0.00%)</td><td>0.00 (-5.88%)</td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.65%)</td><td>18371.92 (-12.05%)</td><td>14533.95 (+8.04%)</td><td>17350.31 <b>(+28.47%)</b></td><td>7241.89 (-0.79%)</td><td>4744.93 (-10.80%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20888.31 (n/a)</td><td>13452.45 (n/a)</td><td>13505.60 (n/a)</td><td>7299.37 (n/a)</td><td>5319.49 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.14 (-1.35%)</td><td>0.10 (+15.21%)</td><td>0.09 <b>(+28.61%)</b></td><td>0.07 (+1.87%)</td><td>0.03 (+3.23%)</td><td>29619.26 (-1.87%)</td><td>21969.03 (-13.26%)</td><td>23085.78 <b>(-22.27%)</b></td><td>15129.46 (+1.35%)</td><td>6477.14 (-4.50%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>30184.63 (n/a)</td><td>25327.87 (n/a)</td><td>29701.07 (n/a)</td><td>14927.20 (n/a)</td><td>6782.68 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.78 (-7.89%)</td><td>2.10 (+19.13%)</td><td>2.55 <b>(+43.04%)</b></td><td>0.30 <b>(-46.49%)</b></td><td>1.02 (+4.43%)</td><td>3487.20 <b>(+86.88%)</b></td><td>1027.50 <b>(+22.27%)</b></td><td>411.00 <b>(-30.10%)</b></td><td>377.30 (+8.58%)</td><td>1375.29 <b>(+122.40%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.02 (n/a)</td><td>1.76 (n/a)</td><td>1.78 (n/a)</td><td>0.56 (n/a)</td><td>0.98 (n/a)</td><td>1866.00 (n/a)</td><td>840.32 (n/a)</td><td>588.00 (n/a)</td><td>347.50 (n/a)</td><td>618.39 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.69 <b>(-21.63%)</b></td><td>1.77 (-3.27%)</td><td>1.64 (+3.32%)</td><td>1.00 <b>(+229.92%)</b></td><td>0.64 <b>(-47.45%)</b></td><td>1047.10 <b>(-69.69%)</b></td><td>660.60 <b>(-41.95%)</b></td><td>639.80 (-3.21%)</td><td>390.30 <b>(+27.59%)</b></td><td>251.28 <b>(-80.88%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.43 (n/a)</td><td>1.83 (n/a)</td><td>1.59 (n/a)</td><td>0.30 (n/a)</td><td>1.23 (n/a)</td><td>3454.50 (n/a)</td><td>1137.92 (n/a)</td><td>661.00 (n/a)</td><td>305.90 (n/a)</td><td>1314.07 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.68 <b>(-30.43%)</b></td><td>1.69 (-4.95%)</td><td>1.26 (-12.13%)</td><td>1.14 <b>(+102.04%)</b></td><td>0.68 <b>(-46.16%)</b></td><td>920.80 <b>(-50.50%)</b></td><td>694.34 <b>(-20.16%)</b></td><td>832.50 (+13.81%)</td><td>391.90 <b>(+43.76%)</b></td><td>235.52 <b>(-61.18%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.85 (n/a)</td><td>1.78 (n/a)</td><td>1.43 (n/a)</td><td>0.56 (n/a)</td><td>1.26 (n/a)</td><td>1860.30 (n/a)</td><td>869.62 (n/a)</td><td>731.50 (n/a)</td><td>272.60 (n/a)</td><td>606.69 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>3.77 (+9.47%)</td><td>2.49 <b>(+42.12%)</b></td><td>2.30 <b>(+60.28%)</b></td><td>1.87 <b>(+63.47%)</b></td><td>0.78 (-19.03%)</td><td>560.00 <b>(-38.82%)</b></td><td>449.78 <b>(-36.12%)</b></td><td>455.20 <b>(-37.61%)</b></td><td>278.50 (-8.63%)</td><td>117.67 <b>(-52.90%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.44 (n/a)</td><td>1.75 (n/a)</td><td>1.44 (n/a)</td><td>1.15 (n/a)</td><td>0.96 (n/a)</td><td>915.40 (n/a)</td><td>704.10 (n/a)</td><td>729.60 (n/a)</td><td>304.80 (n/a)</td><td>249.83 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>3.70 (-12.14%)</td><td>2.71 (-11.59%)</td><td>2.90 (-15.96%)</td><td>1.10 <b>(+56.90%)</b></td><td>1.07 <b>(-22.14%)</b></td><td>1899.40 <b>(-36.26%)</b></td><td>940.12 (-11.27%)</td><td>724.30 (+18.99%)</td><td>567.00 (+13.81%)</td><td>555.46 <b>(-48.34%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>4.21 (n/a)</td><td>3.07 (n/a)</td><td>3.45 (n/a)</td><td>0.70 (n/a)</td><td>1.38 (n/a)</td><td>2980.00 (n/a)</td><td>1059.48 (n/a)</td><td>608.70 (n/a)</td><td>498.20 (n/a)</td><td>1075.23 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>5.34 (+0.68%)</td><td>2.84 (+8.00%)</td><td>3.52 <b>(+61.22%)</b></td><td>0.58 (-2.40%)</td><td>2.16 (-0.66%)</td><td>3637.00 (+2.46%)</td><td>1744.20 (-1.30%)</td><td>596.50 <b>(-37.97%)</b></td><td>392.50 (-0.68%)</td><td>1709.44 (+6.77%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.31 (n/a)</td><td>2.63 (n/a)</td><td>2.18 (n/a)</td><td>0.59 (n/a)</td><td>2.18 (n/a)</td><td>3549.80 (n/a)</td><td>1767.14 (n/a)</td><td>961.70 (n/a)</td><td>395.20 (n/a)</td><td>1601.03 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>4.72 (-7.40%)</td><td>2.22 <b>(-35.29%)</b></td><td>2.11 <b>(-33.08%)</b></td><td>0.63 <b>(-66.69%)</b></td><td>1.54 <b>(+28.33%)</b></td><td>3325.20 <b>(+200.22%)</b></td><td>1437.16 <b>(+111.38%)</b></td><td>992.30 <b>(+49.42%)</b></td><td>444.20 (+8.00%)</td><td>1119.05 <b>(+322.35%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.10 (n/a)</td><td>3.44 (n/a)</td><td>3.16 (n/a)</td><td>1.89 (n/a)</td><td>1.20 (n/a)</td><td>1107.60 (n/a)</td><td>679.90 (n/a)</td><td>664.10 (n/a)</td><td>411.30 (n/a)</td><td>264.96 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>6.63 (+11.87%)</td><td>3.69 (-7.72%)</td><td>2.86 <b>(-20.28%)</b></td><td>2.12 (-5.12%)</td><td>1.79 (+8.99%)</td><td>990.50 (+5.39%)</td><td>661.66 (+9.67%)</td><td>733.10 <b>(+25.44%)</b></td><td>316.20 (-10.60%)</td><td>256.49 (+2.83%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.93 (n/a)</td><td>4.00 (n/a)</td><td>3.59 (n/a)</td><td>2.23 (n/a)</td><td>1.64 (n/a)</td><td>939.80 (n/a)</td><td>603.34 (n/a)</td><td>584.40 (n/a)</td><td>353.70 (n/a)</td><td>249.44 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>6.03 <b>(+33.57%)</b></td><td>1.68 <b>(-21.11%)</b></td><td>0.59 <b>(-67.70%)</b></td><td>0.58 (-2.61%)</td><td>2.44 <b>(+68.27%)</b></td><td>3608.90 (+2.68%)</td><td>2934.08 <b>(+97.36%)</b></td><td>3580.50 <b>(+209.57%)</b></td><td>347.60 <b>(-25.12%)</b></td><td>1446.05 <b>(+23.06%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>4.52 (n/a)</td><td>2.12 (n/a)</td><td>1.81 (n/a)</td><td>0.60 (n/a)</td><td>1.45 (n/a)</td><td>3514.60 (n/a)</td><td>1486.64 (n/a)</td><td>1156.60 (n/a)</td><td>464.20 (n/a)</td><td>1175.12 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>5.82 (+9.71%)</td><td>3.06 <b>(-21.12%)</b></td><td>3.94 (+1.19%)</td><td>0.59 <b>(-78.31%)</b></td><td>2.36 <b>(+114.19%)</b></td><td>3564.80 <b>(+361.05%)</b></td><td>1690.00 <b>(+193.01%)</b></td><td>531.90 (-1.17%)</td><td>360.30 (-8.83%)</td><td>1689.10 <b>(+925.51%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.31 (n/a)</td><td>3.88 (n/a)</td><td>3.90 (n/a)</td><td>2.71 (n/a)</td><td>1.10 (n/a)</td><td>773.20 (n/a)</td><td>576.78 (n/a)</td><td>538.20 (n/a)</td><td>395.20 (n/a)</td><td>164.71 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>5.26 (+3.75%)</td><td>4.59 <b>(+27.22%)</b></td><td>5.23 (+11.17%)</td><td>3.50 <b>(+108.06%)</b></td><td>0.91 <b>(-48.09%)</b></td><td>1197.10 <b>(-51.94%)</b></td><td>945.48 <b>(-37.11%)</b></td><td>801.80 (-10.05%)</td><td>796.70 (-3.62%)</td><td>202.43 <b>(-77.04%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.07 (n/a)</td><td>3.61 (n/a)</td><td>4.71 (n/a)</td><td>1.68 (n/a)</td><td>1.75 (n/a)</td><td>2490.70 (n/a)</td><td>1503.46 (n/a)</td><td>891.40 (n/a)</td><td>826.60 (n/a)</td><td>881.76 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>7.26 (-15.18%)</td><td>5.59 (+9.41%)</td><td>5.92 <b>(+20.70%)</b></td><td>3.82 <b>(+125.59%)</b></td><td>1.69 <b>(-42.69%)</b></td><td>1097.50 <b>(-55.67%)</b></td><td>812.96 <b>(-30.51%)</b></td><td>708.90 (-17.16%)</td><td>577.60 (+17.90%)</td><td>261.82 <b>(-68.34%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>8.56 (n/a)</td><td>5.11 (n/a)</td><td>4.90 (n/a)</td><td>1.69 (n/a)</td><td>2.94 (n/a)</td><td>2475.90 (n/a)</td><td>1169.94 (n/a)</td><td>855.70 (n/a)</td><td>489.90 (n/a)</td><td>826.89 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>7.72 (-2.76%)</td><td>6.17 <b>(+41.33%)</b></td><td>6.55 <b>(+69.52%)</b></td><td>3.83 <b>(+204.25%)</b></td><td>1.47 <b>(-49.98%)</b></td><td>1096.40 <b>(-67.13%)</b></td><td>720.66 <b>(-53.38%)</b></td><td>640.80 <b>(-41.01%)</b></td><td>543.30 (+2.84%)</td><td>219.05 <b>(-81.66%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>7.94 (n/a)</td><td>4.37 (n/a)</td><td>3.86 (n/a)</td><td>1.26 (n/a)</td><td>2.95 (n/a)</td><td>3335.80 (n/a)</td><td>1545.74 (n/a)</td><td>1086.20 (n/a)</td><td>528.30 (n/a)</td><td>1194.16 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>10.83 (+7.26%)</td><td>7.69 (+13.41%)</td><td>6.92 (-4.27%)</td><td>4.08 <b>(+224.52%)</b></td><td>2.86 (-13.83%)</td><td>1028.30 <b>(-69.19%)</b></td><td>619.04 <b>(-43.04%)</b></td><td>605.80 (+4.45%)</td><td>387.50 (-6.76%)</td><td>259.64 <b>(-79.39%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>10.09 (n/a)</td><td>6.78 (n/a)</td><td>7.23 (n/a)</td><td>1.26 (n/a)</td><td>3.31 (n/a)</td><td>3337.20 (n/a)</td><td>1086.72 (n/a)</td><td>580.00 (n/a)</td><td>415.60 (n/a)</td><td>1260.01 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>9.68 <b>(+43.03%)</b></td><td>7.62 <b>(+84.72%)</b></td><td>8.55 <b>(+61.51%)</b></td><td>3.96 <b>(+228.80%)</b></td><td>2.42 (-10.20%)</td><td>1060.10 <b>(-69.59%)</b></td><td>615.48 <b>(-65.54%)</b></td><td>490.30 <b>(-38.09%)</b></td><td>433.30 <b>(-30.08%)</b></td><td>263.69 <b>(-82.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>6.77 (n/a)</td><td>4.13 (n/a)</td><td>5.30 (n/a)</td><td>1.20 (n/a)</td><td>2.70 (n/a)</td><td>3485.70 (n/a)</td><td>1786.18 (n/a)</td><td>792.00 (n/a)</td><td>619.70 (n/a)</td><td>1490.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>9.48 (+2.16%)</td><td>5.17 (-11.18%)</td><td>4.40 <b>(-34.00%)</b></td><td>1.69 <b>(+43.41%)</b></td><td>2.94 (-7.97%)</td><td>2476.20 <b>(-30.27%)</b></td><td>1124.10 (-9.06%)</td><td>953.40 <b>(+51.50%)</b></td><td>442.20 (-2.12%)</td><td>797.65 <b>(-39.19%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>9.28 (n/a)</td><td>5.82 (n/a)</td><td>6.67 (n/a)</td><td>1.18 (n/a)</td><td>3.20 (n/a)</td><td>3551.20 (n/a)</td><td>1236.06 (n/a)</td><td>629.30 (n/a)</td><td>451.80 (n/a)</td><td>1311.64 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>1.69 (+14.76%)</td><td>1.55 <b>(+105.68%)</b></td><td>1.59 <b>(+168.79%)</b></td><td>1.33 <b>(+387.77%)</b></td><td>0.13 <b>(-74.99%)</b></td><td>394.30 <b>(-79.50%)</b></td><td>339.98 <b>(-69.03%)</b></td><td>328.80 <b>(-62.80%)</b></td><td>310.70 (-12.87%)</td><td>32.06 <b>(-95.76%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>1.47 (n/a)</td><td>0.75 (n/a)</td><td>0.59 (n/a)</td><td>0.27 (n/a)</td><td>0.54 (n/a)</td><td>1923.20 (n/a)</td><td>1097.86 (n/a)</td><td>883.90 (n/a)</td><td>356.60 (n/a)</td><td>757.05 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.72 (-7.00%)</td><td>2.31 <b>(+38.40%)</b></td><td>2.41 (+1.79%)</td><td>1.51 <b>(+397.98%)</b></td><td>0.46 <b>(-63.41%)</b></td><td>692.70 <b>(-79.92%)</b></td><td>474.20 <b>(-70.67%)</b></td><td>435.40 (-1.76%)</td><td>386.00 (+7.52%)</td><td>123.82 <b>(-92.50%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>2.92 (n/a)</td><td>1.67 (n/a)</td><td>2.37 (n/a)</td><td>0.30 (n/a)</td><td>1.26 (n/a)</td><td>3449.50 (n/a)</td><td>1616.90 (n/a)</td><td>443.20 (n/a)</td><td>359.00 (n/a)</td><td>1651.73 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>4.11 <b>(+30.25%)</b></td><td>2.78 <b>(+35.30%)</b></td><td>2.99 <b>(+41.90%)</b></td><td>0.98 (+12.74%)</td><td>1.30 <b>(+45.74%)</b></td><td>2148.00 (-11.30%)</td><td>993.68 <b>(-20.63%)</b></td><td>702.00 <b>(-29.53%)</b></td><td>510.40 <b>(-23.23%)</b></td><td>680.91 (-3.53%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.15 (n/a)</td><td>2.05 (n/a)</td><td>2.11 (n/a)</td><td>0.87 (n/a)</td><td>0.90 (n/a)</td><td>2421.60 (n/a)</td><td>1252.02 (n/a)</td><td>996.20 (n/a)</td><td>664.80 (n/a)</td><td>705.79 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>2.23 <b>(-23.25%)</b></td><td>1.08 <b>(-28.95%)</b></td><td>0.84 <b>(-42.79%)</b></td><td>0.60 <b>(-26.83%)</b></td><td>0.66 <b>(-21.00%)</b></td><td>877.10 <b>(+36.66%)</b></td><td>593.76 <b>(+41.36%)</b></td><td>627.20 <b>(+74.80%)</b></td><td>235.40 <b>(+30.27%)</b></td><td>234.68 <b>(+27.79%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>2.90 (n/a)</td><td>1.52 (n/a)</td><td>1.46 (n/a)</td><td>0.82 (n/a)</td><td>0.83 (n/a)</td><td>641.80 (n/a)</td><td>420.02 (n/a)</td><td>358.80 (n/a)</td><td>180.70 (n/a)</td><td>183.64 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.10 <b>(-31.91%)</b></td><td>0.08 <b>(-27.09%)</b></td><td>0.08 <b>(-38.03%)</b></td><td>0.07 <b>(+32.67%)</b></td><td>0.01 <b>(-67.96%)</b></td><td>479.50 <b>(-24.62%)</b></td><td>412.46 (+17.06%)</td><td>403.60 <b>(+61.38%)</b></td><td>312.10 <b>(+46.87%)</b></td><td>67.33 <b>(-63.32%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>636.10 (n/a)</td><td>352.36 (n/a)</td><td>250.10 (n/a)</td><td>212.50 (n/a)</td><td>183.57 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.13 (-18.34%)</td><td>0.09 (-12.51%)</td><td>0.10 <b>(-21.67%)</b></td><td>0.06 <b>(+38.29%)</b></td><td>0.03 <b>(-40.92%)</b></td><td>523.20 <b>(-27.69%)</b></td><td>385.62 (-2.05%)</td><td>331.20 <b>(+27.68%)</b></td><td>248.40 <b>(+22.42%)</b></td><td>126.99 <b>(-44.39%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>723.60 (n/a)</td><td>393.68 (n/a)</td><td>259.40 (n/a)</td><td>202.90 (n/a)</td><td>228.37 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.25 (-1.59%)</td><td>0.19 (-3.40%)</td><td>0.19 (-0.54%)</td><td>0.15 (-7.79%)</td><td>0.04 (-2.08%)</td><td>447.00 (+8.44%)</td><td>349.90 (+3.67%)</td><td>344.20 (+0.56%)</td><td>265.70 (+1.61%)</td><td>70.14 (+8.16%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>412.20 (n/a)</td><td>337.50 (n/a)</td><td>342.30 (n/a)</td><td>261.50 (n/a)</td><td>64.85 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.32 <b>(+22.07%)</b></td><td>0.21 (+3.23%)</td><td>0.22 (+0.70%)</td><td>0.14 (+8.27%)</td><td>0.07 <b>(+27.65%)</b></td><td>478.00 (-7.63%)</td><td>333.20 (-1.96%)</td><td>301.90 (-0.72%)</td><td>204.70 (-18.09%)</td><td>102.45 (-5.08%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>517.50 (n/a)</td><td>339.86 (n/a)</td><td>304.10 (n/a)</td><td>249.90 (n/a)</td><td>107.94 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.26 (+2.87%)</td><td>0.18 (+18.26%)</td><td>0.15 (+14.72%)</td><td>0.11 <b>(+220.50%)</b></td><td>0.06 <b>(-25.53%)</b></td><td>596.90 <b>(-68.80%)</b></td><td>406.92 <b>(-42.18%)</b></td><td>438.20 (-12.83%)</td><td>256.90 (-2.76%)</td><td>141.17 <b>(-79.45%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>0.09 (n/a)</td><td>1913.00 (n/a)</td><td>703.78 (n/a)</td><td>502.70 (n/a)</td><td>264.20 (n/a)</td><td>686.88 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.58 (+17.23%)</td><td>0.48 <b>(+27.58%)</b></td><td>0.53 (+17.68%)</td><td>0.29 <b>(+43.72%)</b></td><td>0.12 (-9.51%)</td><td>452.10 <b>(-30.42%)</b></td><td>294.06 <b>(-26.66%)</b></td><td>249.20 (-15.01%)</td><td>225.60 (-14.71%)</td><td>95.52 <b>(-45.40%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.45 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>649.80 (n/a)</td><td>400.94 (n/a)</td><td>293.20 (n/a)</td><td>264.50 (n/a)</td><td>174.95 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.49 (+16.70%)</td><td>0.32 <b>(+22.78%)</b></td><td>0.26 (+10.22%)</td><td>0.20 <b>(+22.39%)</b></td><td>0.13 <b>(+33.44%)</b></td><td>662.20 (-18.30%)</td><td>469.44 (-16.04%)</td><td>499.40 (-9.28%)</td><td>267.30 (-14.30%)</td><td>175.20 (-3.69%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>810.50 (n/a)</td><td>559.10 (n/a)</td><td>550.50 (n/a)</td><td>311.90 (n/a)</td><td>181.92 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.44 <b>(-36.61%)</b></td><td>0.33 (-15.12%)</td><td>0.35 <b>(+32.33%)</b></td><td>0.20 (-12.91%)</td><td>0.10 <b>(-51.49%)</b></td><td>656.10 (+14.82%)</td><td>434.94 (+6.18%)</td><td>371.40 <b>(-24.44%)</b></td><td>297.80 <b>(+57.73%)</b></td><td>147.92 (-13.37%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.69 (n/a)</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>571.40 (n/a)</td><td>409.64 (n/a)</td><td>491.50 (n/a)</td><td>188.80 (n/a)</td><td>170.74 (n/a)</td>
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
<td><code>9b92482</code> — 2026-08-28 20:16:07</td><td>0.07 (-3.02%)</td><td>0.05 <b>(+25.41%)</b></td><td>0.04 <b>(+37.60%)</b></td><td>0.03 <b>(+313.31%)</b></td><td>0.02 <b>(-27.96%)</b></td><td>611.30 <b>(-75.81%)</b></td><td>386.92 <b>(-54.07%)</b></td><td>374.60 <b>(-27.32%)</b></td><td>242.90 (+3.14%)</td><td>156.08 <b>(-83.70%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2526.60 (n/a)</td><td>842.46 (n/a)</td><td>515.40 (n/a)</td><td>235.50 (n/a)</td><td>957.30 (n/a)</td>
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
