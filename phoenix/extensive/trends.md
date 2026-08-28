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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(+28.22%)</b></td><td>0.02 (+16.07%)</td><td>0.02 (+7.55%)</td><td>0.02 <b>(+20.00%)</b></td><td>0.00 <b>(+29.94%)</b></td><td>334.10 (-16.68%)</td><td>272.46 (-13.70%)</td><td>269.30 (-7.04%)</td><td>212.40 <b>(-22.03%)</b></td><td>45.95 (-15.33%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>401.00 (n/a)</td><td>315.70 (n/a)</td><td>289.70 (n/a)</td><td>272.40 (n/a)</td><td>54.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-0.80%)</td><td>0.01 (-10.80%)</td><td>0.01 <b>(-26.30%)</b></td><td>0.01 (-3.53%)</td><td>0.01 (+15.75%)</td><td>605.90 (+3.66%)</td><td>490.88 (+16.59%)</td><td>580.80 <b>(+35.70%)</b></td><td>250.30 (+0.81%)</td><td>156.64 <b>(+30.22%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.50 (n/a)</td><td>421.02 (n/a)</td><td>428.00 (n/a)</td><td>248.30 (n/a)</td><td>120.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (+1.84%)</td><td>0.01 (-13.64%)</td><td>0.01 (-6.89%)</td><td>0.00 <b>(-67.03%)</b></td><td>0.01 <b>(+53.53%)</b></td><td>1748.00 <b>(+203.31%)</b></td><td>656.40 <b>(+65.82%)</b></td><td>413.30 (+7.41%)</td><td>270.00 (-1.78%)</td><td>618.66 <b>(+404.66%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.30 (n/a)</td><td>395.86 (n/a)</td><td>384.80 (n/a)</td><td>274.90 (n/a)</td><td>122.59 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(+24.82%)</b></td><td>0.02 (+19.22%)</td><td>0.02 <b>(+36.47%)</b></td><td>0.01 (-11.28%)</td><td>0.01 <b>(+93.02%)</b></td><td>517.40 (+12.70%)</td><td>364.60 (-11.25%)</td><td>312.80 <b>(-26.73%)</b></td><td>242.20 (-19.85%)</td><td>117.07 <b>(+82.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>459.10 (n/a)</td><td>410.82 (n/a)</td><td>426.90 (n/a)</td><td>302.20 (n/a)</td><td>64.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-18.87%)</td><td>0.02 (+8.49%)</td><td>0.02 <b>(+27.25%)</b></td><td>0.01 <b>(+21.98%)</b></td><td>0.00 <b>(-41.89%)</b></td><td>511.90 (-18.02%)</td><td>402.12 (-13.89%)</td><td>401.60 <b>(-21.41%)</b></td><td>290.30 <b>(+23.27%)</b></td><td>91.75 <b>(-36.30%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>624.40 (n/a)</td><td>467.00 (n/a)</td><td>511.00 (n/a)</td><td>235.50 (n/a)</td><td>144.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (-16.35%)</td><td>0.02 (+1.83%)</td><td>0.01 <b>(+44.30%)</b></td><td>0.01 (-10.14%)</td><td>0.01 <b>(-23.13%)</b></td><td>706.80 (+11.27%)</td><td>433.08 (-7.61%)</td><td>419.40 <b>(-30.70%)</b></td><td>234.40 (+19.53%)</td><td>193.05 (-6.74%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>635.20 (n/a)</td><td>468.76 (n/a)</td><td>605.20 (n/a)</td><td>196.10 (n/a)</td><td>207.00 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 <b>(+20.08%)</b></td><td>0.04 (+11.02%)</td><td>0.04 <b>(+74.07%)</b></td><td>0.01 <b>(-73.45%)</b></td><td>0.02 <b>(+62.79%)</b></td><td>1957.20 <b>(+276.60%)</b></td><td>620.76 <b>(+54.66%)</b></td><td>275.40 <b>(-42.55%)</b></td><td>209.80 (-16.71%)</td><td>750.61 <b>(+476.19%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.70 (n/a)</td><td>401.38 (n/a)</td><td>479.40 (n/a)</td><td>251.90 (n/a)</td><td>130.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 <b>(+49.22%)</b></td><td>0.05 <b>(+42.42%)</b></td><td>0.05 <b>(+60.11%)</b></td><td>0.02 (-4.51%)</td><td>0.02 <b>(+86.81%)</b></td><td>514.50 (+4.72%)</td><td>298.72 <b>(-24.91%)</b></td><td>266.30 <b>(-37.55%)</b></td><td>181.20 <b>(-32.96%)</b></td><td>126.57 <b>(+40.38%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>491.30 (n/a)</td><td>397.84 (n/a)</td><td>426.40 (n/a)</td><td>270.30 (n/a)</td><td>90.16 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 <b>(+33.99%)</b></td><td>0.04 <b>(+22.78%)</b></td><td>0.05 <b>(+29.28%)</b></td><td>0.02 <b>(+27.30%)</b></td><td>0.02 <b>(+26.56%)</b></td><td>562.20 <b>(-21.45%)</b></td><td>339.06 (-18.87%)</td><td>272.20 <b>(-22.65%)</b></td><td>175.40 <b>(-25.39%)</b></td><td>158.20 <b>(-21.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>715.70 (n/a)</td><td>417.92 (n/a)</td><td>351.90 (n/a)</td><td>235.10 (n/a)</td><td>202.60 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (+8.70%)</td><td>0.03 (-2.98%)</td><td>0.03 (+9.13%)</td><td>0.01 <b>(-69.23%)</b></td><td>0.02 <b>(+65.52%)</b></td><td>1895.00 <b>(+224.99%)</b></td><td>671.36 <b>(+59.05%)</b></td><td>387.20 (-8.36%)</td><td>244.50 (-8.01%)</td><td>692.90 <b>(+437.21%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>583.10 (n/a)</td><td>422.10 (n/a)</td><td>422.50 (n/a)</td><td>265.80 (n/a)</td><td>128.98 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 <b>(+45.21%)</b></td><td>0.04 <b>(+40.08%)</b></td><td>0.04 <b>(+65.53%)</b></td><td>0.02 (-8.48%)</td><td>0.01 <b>(+127.22%)</b></td><td>600.60 (+9.26%)</td><td>376.80 <b>(-22.86%)</b></td><td>304.40 <b>(-39.58%)</b></td><td>240.80 <b>(-31.14%)</b></td><td>145.58 <b>(+77.34%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>549.70 (n/a)</td><td>488.44 (n/a)</td><td>503.80 (n/a)</td><td>349.70 (n/a)</td><td>82.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (-3.99%)</td><td>0.03 <b>(+34.99%)</b></td><td>0.03 <b>(+20.56%)</b></td><td>0.02 <b>(+225.37%)</b></td><td>0.01 (-18.08%)</td><td>606.60 <b>(-69.26%)</b></td><td>439.14 <b>(-45.00%)</b></td><td>470.80 (-17.05%)</td><td>275.10 (+4.17%)</td><td>154.91 <b>(-76.95%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1973.60 (n/a)</td><td>798.46 (n/a)</td><td>567.60 (n/a)</td><td>264.10 (n/a)</td><td>672.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (+13.50%)</td><td>0.08 (+7.89%)</td><td>0.09 (+3.00%)</td><td>0.04 <b>(-30.37%)</b></td><td>0.02 <b>(+45.37%)</b></td><td>612.40 <b>(+43.62%)</b></td><td>336.80 (-0.50%)</td><td>273.80 (-2.91%)</td><td>244.80 (-11.91%)</td><td>154.85 <b>(+94.38%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>426.40 (n/a)</td><td>338.50 (n/a)</td><td>282.00 (n/a)</td><td>277.90 (n/a)</td><td>79.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (+0.08%)</td><td>0.08 (+11.67%)</td><td>0.10 <b>(+43.18%)</b></td><td>0.05 (+5.31%)</td><td>0.02 (-2.50%)</td><td>479.50 (-5.05%)</td><td>312.20 (-11.02%)</td><td>244.70 <b>(-30.15%)</b></td><td>238.40 (-0.04%)</td><td>105.31 (-6.40%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>505.00 (n/a)</td><td>350.86 (n/a)</td><td>350.30 (n/a)</td><td>238.50 (n/a)</td><td>112.51 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (-4.31%)</td><td>0.05 (-9.37%)</td><td>0.06 <b>(+21.53%)</b></td><td>0.01 <b>(-75.16%)</b></td><td>0.03 <b>(+22.25%)</b></td><td>2433.70 <b>(+302.60%)</b></td><td>807.34 <b>(+75.20%)</b></td><td>446.40 (-17.71%)</td><td>258.00 (+4.50%)</td><td>913.20 <b>(+505.74%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>604.50 (n/a)</td><td>460.80 (n/a)</td><td>542.50 (n/a)</td><td>246.90 (n/a)</td><td>150.76 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (+12.60%)</td><td>0.07 (+11.09%)</td><td>0.06 (-0.65%)</td><td>0.05 (+14.44%)</td><td>0.02 (+16.21%)</td><td>504.70 (-12.62%)</td><td>372.78 (-9.74%)</td><td>412.30 (+0.66%)</td><td>241.30 (-11.19%)</td><td>105.24 (-11.12%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.60 (n/a)</td><td>413.00 (n/a)</td><td>409.60 (n/a)</td><td>271.70 (n/a)</td><td>118.40 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 <b>(+34.65%)</b></td><td>0.07 <b>(+33.82%)</b></td><td>0.08 <b>(+57.46%)</b></td><td>0.04 (-3.97%)</td><td>0.03 <b>(+134.12%)</b></td><td>604.40 (+4.14%)</td><td>380.78 (-16.89%)</td><td>294.60 <b>(-36.49%)</b></td><td>242.50 <b>(-25.73%)</b></td><td>166.10 <b>(+84.15%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>580.40 (n/a)</td><td>458.16 (n/a)</td><td>463.90 (n/a)</td><td>326.50 (n/a)</td><td>90.20 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 <b>(+27.06%)</b></td><td>0.07 (+19.46%)</td><td>0.06 (+8.13%)</td><td>0.05 <b>(+34.69%)</b></td><td>0.02 <b>(+34.21%)</b></td><td>477.80 <b>(-25.76%)</b></td><td>386.74 (-16.00%)</td><td>395.50 (-7.51%)</td><td>279.30 <b>(-21.30%)</b></td><td>92.79 <b>(-20.23%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>643.60 (n/a)</td><td>460.38 (n/a)</td><td>427.60 (n/a)</td><td>354.90 (n/a)</td><td>116.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.20 (-2.55%)</td><td>0.17 (+16.49%)</td><td>0.17 (+19.96%)</td><td>0.10 (+0.30%)</td><td>0.04 (-10.33%)</td><td>480.30 (-0.31%)</td><td>310.00 (-15.40%)</td><td>291.40 (-16.65%)</td><td>240.70 (+2.60%)</td><td>98.32 (-10.53%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>481.80 (n/a)</td><td>366.44 (n/a)</td><td>349.60 (n/a)</td><td>234.60 (n/a)</td><td>109.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.17 (-9.31%)</td><td>0.13 (-2.47%)</td><td>0.12 (-2.92%)</td><td>0.09 (+0.44%)</td><td>0.04 (-16.96%)</td><td>526.00 (-0.44%)</td><td>404.02 (+0.26%)</td><td>425.60 (+3.00%)</td><td>287.40 (+10.24%)</td><td>107.19 (-13.41%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>528.30 (n/a)</td><td>402.96 (n/a)</td><td>413.20 (n/a)</td><td>260.70 (n/a)</td><td>123.79 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.19 (-7.61%)</td><td>0.12 (+1.25%)</td><td>0.09 (-13.75%)</td><td>0.08 (-5.75%)</td><td>0.05 (+12.33%)</td><td>650.40 (+6.10%)</td><td>464.94 (+3.82%)</td><td>530.60 (+15.95%)</td><td>261.70 (+8.23%)</td><td>180.16 <b>(+35.35%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>613.00 (n/a)</td><td>447.84 (n/a)</td><td>457.60 (n/a)</td><td>241.80 (n/a)</td><td>133.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.17 <b>(-30.52%)</b></td><td>0.14 (-17.29%)</td><td>0.16 <b>(-21.41%)</b></td><td>0.11 (+12.25%)</td><td>0.02 <b>(-63.62%)</b></td><td>449.20 (-10.91%)</td><td>348.46 (+7.02%)</td><td>311.40 <b>(+27.21%)</b></td><td>293.20 <b>(+43.94%)</b></td><td>66.33 <b>(-54.20%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>504.20 (n/a)</td><td>325.60 (n/a)</td><td>244.80 (n/a)</td><td>203.70 (n/a)</td><td>144.83 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.27 <b>(+20.16%)</b></td><td>0.15 (+12.42%)</td><td>0.14 (+10.79%)</td><td>0.09 (-1.61%)</td><td>0.07 <b>(+37.22%)</b></td><td>524.20 (+1.65%)</td><td>365.18 (-6.79%)</td><td>359.70 (-9.74%)</td><td>183.90 (-16.79%)</td><td>129.42 <b>(+20.32%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>515.70 (n/a)</td><td>391.80 (n/a)</td><td>398.50 (n/a)</td><td>221.00 (n/a)</td><td>107.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.22 (+5.45%)</td><td>0.14 (+9.43%)</td><td>0.12 (+13.36%)</td><td>0.09 <b>(+241.80%)</b></td><td>0.05 <b>(-26.35%)</b></td><td>536.50 <b>(-70.74%)</b></td><td>403.50 <b>(-39.12%)</b></td><td>403.60 (-11.78%)</td><td>223.20 (-5.14%)</td><td>136.48 <b>(-79.50%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1833.80 (n/a)</td><td>662.78 (n/a)</td><td>457.50 (n/a)</td><td>235.30 (n/a)</td><td>665.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (-1.70%)</td><td>0.01 (-12.82%)</td><td>0.01 (-15.53%)</td><td>0.00 (-13.05%)</td><td>0.00 (-9.11%)</td><td>560.80 (+15.01%)</td><td>436.74 (+14.49%)</td><td>486.20 (+18.38%)</td><td>275.30 (+1.74%)</td><td>112.64 (+8.07%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.60 (n/a)</td><td>381.46 (n/a)</td><td>410.70 (n/a)</td><td>270.60 (n/a)</td><td>104.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 <b>(+27.26%)</b></td><td>0.01 <b>(+31.70%)</b></td><td>0.01 <b>(+52.58%)</b></td><td>0.00 <b>(+83.08%)</b></td><td>0.00 (+5.22%)</td><td>576.10 <b>(-45.38%)</b></td><td>348.54 <b>(-32.71%)</b></td><td>269.50 <b>(-34.48%)</b></td><td>197.30 <b>(-21.43%)</b></td><td>165.21 <b>(-50.69%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1054.70 (n/a)</td><td>517.96 (n/a)</td><td>411.30 (n/a)</td><td>251.10 (n/a)</td><td>335.06 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (-1.17%)</td><td>0.01 (-1.15%)</td><td>0.01 (-18.93%)</td><td>0.00 <b>(+210.37%)</b></td><td>0.00 (-19.85%)</td><td>596.60 <b>(-67.78%)</b></td><td>457.36 <b>(-30.30%)</b></td><td>505.20 <b>(+23.34%)</b></td><td>230.80 (+1.18%)</td><td>154.08 <b>(-77.13%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1851.60 (n/a)</td><td>656.16 (n/a)</td><td>409.60 (n/a)</td><td>228.10 (n/a)</td><td>673.68 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (+16.66%)</td><td>0.01 (+4.07%)</td><td>0.01 (-18.50%)</td><td>0.00 (+15.59%)</td><td>0.00 <b>(+39.02%)</b></td><td>582.50 (-13.49%)</td><td>430.08 (+0.21%)</td><td>503.90 <b>(+22.69%)</b></td><td>221.00 (-14.27%)</td><td>154.92 (+2.35%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>673.30 (n/a)</td><td>429.20 (n/a)</td><td>410.70 (n/a)</td><td>257.80 (n/a)</td><td>151.36 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 <b>(+45.78%)</b></td><td>0.01 <b>(+24.78%)</b></td><td>0.01 <b>(+24.58%)</b></td><td>0.00 (-9.09%)</td><td>0.00 <b>(+156.45%)</b></td><td>591.20 (+9.99%)</td><td>364.88 (-14.67%)</td><td>330.50 (-19.74%)</td><td>253.20 <b>(-31.40%)</b></td><td>130.57 <b>(+102.04%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>537.50 (n/a)</td><td>427.60 (n/a)</td><td>411.80 (n/a)</td><td>369.10 (n/a)</td><td>64.63 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (+18.82%)</td><td>0.01 (+9.91%)</td><td>0.01 (+8.77%)</td><td>0.00 (+0.95%)</td><td>0.00 <b>(+36.38%)</b></td><td>609.00 (-0.94%)</td><td>471.98 (-5.81%)</td><td>514.70 (-8.06%)</td><td>256.50 (-15.85%)</td><td>145.60 (+14.66%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>614.80 (n/a)</td><td>501.12 (n/a)</td><td>559.80 (n/a)</td><td>304.80 (n/a)</td><td>126.98 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(+22.12%)</b></td><td>0.02 (-12.41%)</td><td>0.02 (-12.03%)</td><td>0.01 <b>(-50.05%)</b></td><td>0.01 <b>(+353.41%)</b></td><td>581.00 <b>(+100.21%)</b></td><td>337.22 <b>(+29.13%)</b></td><td>292.30 (+13.69%)</td><td>196.00 (-18.09%)</td><td>146.82 <b>(+670.87%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>290.20 (n/a)</td><td>261.14 (n/a)</td><td>257.10 (n/a)</td><td>239.30 (n/a)</td><td>19.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-10.13%)</td><td>0.02 (-8.96%)</td><td>0.02 (-8.58%)</td><td>0.01 (-10.70%)</td><td>0.00 (-9.50%)</td><td>518.10 (+11.97%)</td><td>361.80 (+9.88%)</td><td>293.80 (+9.38%)</td><td>254.20 (+11.25%)</td><td>117.13 (+11.17%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>462.70 (n/a)</td><td>329.26 (n/a)</td><td>268.60 (n/a)</td><td>228.50 (n/a)</td><td>105.36 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 <b>(-40.06%)</b></td><td>0.01 <b>(-41.62%)</b></td><td>0.01 <b>(-38.02%)</b></td><td>0.01 <b>(-36.49%)</b></td><td>0.00 <b>(-46.50%)</b></td><td>588.40 <b>(+57.45%)</b></td><td>476.86 <b>(+69.86%)</b></td><td>466.80 <b>(+61.30%)</b></td><td>364.10 <b>(+66.79%)</b></td><td>88.93 <b>(+43.63%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>373.70 (n/a)</td><td>280.74 (n/a)</td><td>289.40 (n/a)</td><td>218.30 (n/a)</td><td>61.92 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 <b>(-23.20%)</b></td><td>0.01 <b>(-25.19%)</b></td><td>0.01 (-10.07%)</td><td>0.00 <b>(-41.31%)</b></td><td>0.00 <b>(-28.17%)</b></td><td>1070.90 <b>(+70.39%)</b></td><td>549.32 <b>(+38.54%)</b></td><td>449.10 (+11.22%)</td><td>308.80 <b>(+30.24%)</b></td><td>300.20 <b>(+85.23%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.50 (n/a)</td><td>396.52 (n/a)</td><td>403.80 (n/a)</td><td>237.10 (n/a)</td><td>162.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 <b>(-35.23%)</b></td><td>0.01 <b>(-21.40%)</b></td><td>0.01 (-14.36%)</td><td>0.01 (-9.43%)</td><td>0.00 <b>(-57.99%)</b></td><td>608.00 (+10.42%)</td><td>469.68 <b>(+20.92%)</b></td><td>445.90 (+16.79%)</td><td>381.90 <b>(+54.43%)</b></td><td>85.98 <b>(-26.44%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>550.60 (n/a)</td><td>388.42 (n/a)</td><td>381.80 (n/a)</td><td>247.30 (n/a)</td><td>116.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(+131.50%)</b></td><td>0.02 <b>(+77.96%)</b></td><td>0.01 <b>(+42.42%)</b></td><td>0.01 <b>(+102.85%)</b></td><td>0.01 <b>(+147.63%)</b></td><td>877.90 <b>(-50.70%)</b></td><td>464.62 <b>(-41.34%)</b></td><td>374.90 <b>(-29.79%)</b></td><td>173.90 <b>(-56.81%)</b></td><td>282.53 <b>(-50.19%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1780.90 (n/a)</td><td>792.10 (n/a)</td><td>534.00 (n/a)</td><td>402.60 (n/a)</td><td>567.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (-16.40%)</td><td>0.03 (+19.22%)</td><td>0.03 <b>(+34.66%)</b></td><td>0.03 <b>(+78.89%)</b></td><td>0.00 <b>(-60.85%)</b></td><td>399.70 <b>(-44.10%)</b></td><td>323.48 <b>(-25.36%)</b></td><td>318.40 <b>(-25.73%)</b></td><td>275.70 (+19.61%)</td><td>47.35 <b>(-73.40%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>715.00 (n/a)</td><td>433.40 (n/a)</td><td>428.70 (n/a)</td><td>230.50 (n/a)</td><td>177.99 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 <b>(+27.98%)</b></td><td>0.03 <b>(+26.67%)</b></td><td>0.03 <b>(+58.29%)</b></td><td>0.01 <b>(-22.76%)</b></td><td>0.01 <b>(+74.26%)</b></td><td>743.80 <b>(+29.47%)</b></td><td>408.18 (-11.96%)</td><td>330.70 <b>(-36.83%)</b></td><td>232.40 <b>(-21.88%)</b></td><td>206.09 <b>(+80.96%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>574.50 (n/a)</td><td>463.62 (n/a)</td><td>523.50 (n/a)</td><td>297.50 (n/a)</td><td>113.89 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (+13.27%)</td><td>0.03 <b>(+22.37%)</b></td><td>0.04 <b>(+47.34%)</b></td><td>0.02 (+10.20%)</td><td>0.01 (+16.05%)</td><td>512.30 (-9.25%)</td><td>347.24 (-17.75%)</td><td>296.20 <b>(-32.13%)</b></td><td>232.70 (-11.72%)</td><td>121.70 (-7.14%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>564.50 (n/a)</td><td>422.16 (n/a)</td><td>436.40 (n/a)</td><td>263.60 (n/a)</td><td>131.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (-9.67%)</td><td>0.02 (-7.10%)</td><td>0.02 (+7.34%)</td><td>0.01 <b>(-24.26%)</b></td><td>0.01 (+9.81%)</td><td>776.80 <b>(+32.04%)</b></td><td>506.24 (+12.05%)</td><td>432.10 (-6.83%)</td><td>330.90 (+10.71%)</td><td>176.84 <b>(+71.04%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>588.30 (n/a)</td><td>451.78 (n/a)</td><td>463.80 (n/a)</td><td>298.90 (n/a)</td><td>103.39 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (-6.30%)</td><td>0.03 (+12.18%)</td><td>0.04 <b>(+63.69%)</b></td><td>0.02 (+5.80%)</td><td>0.01 (-10.10%)</td><td>582.30 (-5.49%)</td><td>385.10 (-12.81%)</td><td>289.60 <b>(-38.90%)</b></td><td>275.30 (+6.75%)</td><td>143.11 (-10.85%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>616.10 (n/a)</td><td>441.66 (n/a)</td><td>474.00 (n/a)</td><td>257.90 (n/a)</td><td>160.53 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(+38.34%)</b></td><td>0.02 (+2.87%)</td><td>0.02 (-14.50%)</td><td>0.02 (-7.28%)</td><td>0.01 <b>(+136.78%)</b></td><td>683.50 (+7.84%)</td><td>541.32 (+2.81%)</td><td>609.10 (+16.98%)</td><td>320.80 <b>(-27.72%)</b></td><td>144.72 <b>(+82.38%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>633.80 (n/a)</td><td>526.52 (n/a)</td><td>520.70 (n/a)</td><td>443.80 (n/a)</td><td>79.35 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (+0.37%)</td><td>0.06 (+15.76%)</td><td>0.07 <b>(+64.45%)</b></td><td>0.04 (+10.26%)</td><td>0.02 (-15.60%)</td><td>523.30 (-9.31%)</td><td>366.66 (-16.69%)</td><td>306.30 <b>(-39.20%)</b></td><td>269.20 (-0.37%)</td><td>112.71 <b>(-23.44%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.00 (n/a)</td><td>440.14 (n/a)</td><td>503.80 (n/a)</td><td>270.20 (n/a)</td><td>147.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (+15.34%)</td><td>0.06 (+9.86%)</td><td>0.06 (+18.98%)</td><td>0.03 (-9.12%)</td><td>0.02 <b>(+22.18%)</b></td><td>634.30 (+10.05%)</td><td>385.84 (-5.88%)</td><td>373.80 (-15.94%)</td><td>243.90 (-13.30%)</td><td>152.58 <b>(+24.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>576.40 (n/a)</td><td>409.96 (n/a)</td><td>444.70 (n/a)</td><td>281.30 (n/a)</td><td>122.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (+2.85%)</td><td>0.05 (-3.68%)</td><td>0.06 (-0.90%)</td><td>0.01 <b>(-59.33%)</b></td><td>0.03 <b>(+38.17%)</b></td><td>1904.00 <b>(+145.87%)</b></td><td>652.26 <b>(+51.34%)</b></td><td>341.30 (+0.89%)</td><td>278.70 (-2.76%)</td><td>703.53 <b>(+244.75%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>774.40 (n/a)</td><td>430.98 (n/a)</td><td>338.30 (n/a)</td><td>286.60 (n/a)</td><td>204.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (-11.67%)</td><td>0.06 (-2.36%)</td><td>0.05 (+1.34%)</td><td>0.04 (-2.79%)</td><td>0.02 (-16.43%)</td><td>569.90 (+2.87%)</td><td>406.84 (+0.88%)</td><td>420.40 (-1.31%)</td><td>286.40 (+13.25%)</td><td>115.18 (-4.39%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>554.00 (n/a)</td><td>403.28 (n/a)</td><td>426.00 (n/a)</td><td>252.90 (n/a)</td><td>120.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 <b>(+61.88%)</b></td><td>0.06 <b>(+62.32%)</b></td><td>0.05 <b>(+21.05%)</b></td><td>0.03 <b>(+237.82%)</b></td><td>0.03 <b>(+37.37%)</b></td><td>601.70 <b>(-70.40%)</b></td><td>370.50 <b>(-52.08%)</b></td><td>383.30 (-17.39%)</td><td>222.50 <b>(-38.21%)</b></td><td>152.58 <b>(-78.47%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2032.80 (n/a)</td><td>773.14 (n/a)</td><td>464.00 (n/a)</td><td>360.10 (n/a)</td><td>708.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (-3.59%)</td><td>0.05 (-0.04%)</td><td>0.06 (+15.55%)</td><td>0.03 (-11.33%)</td><td>0.02 (+0.39%)</td><td>651.20 (+12.78%)</td><td>422.38 (+1.43%)</td><td>371.70 (-13.46%)</td><td>288.70 (+3.74%)</td><td>143.90 <b>(+21.62%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.40 (n/a)</td><td>416.44 (n/a)</td><td>429.50 (n/a)</td><td>278.30 (n/a)</td><td>118.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.50 (n/a)</td><td>359.44 (n/a)</td><td>251.40 (n/a)</td><td>229.70 (n/a)</td><td>167.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.40 (n/a)</td><td>399.66 (n/a)</td><td>414.40 (n/a)</td><td>329.90 (n/a)</td><td>64.00 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>670.10 (n/a)</td><td>454.66 (n/a)</td><td>460.40 (n/a)</td><td>241.90 (n/a)</td><td>191.50 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>660.30 (n/a)</td><td>446.90 (n/a)</td><td>424.80 (n/a)</td><td>268.40 (n/a)</td><td>174.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>639.80 (n/a)</td><td>412.34 (n/a)</td><td>401.70 (n/a)</td><td>270.00 (n/a)</td><td>150.72 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>558.70 (n/a)</td><td>424.80 (n/a)</td><td>440.00 (n/a)</td><td>311.60 (n/a)</td><td>103.69 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1937.10 (n/a)</td><td>587.30 (n/a)</td><td>246.80 (n/a)</td><td>238.70 (n/a)</td><td>754.69 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>527.30 (n/a)</td><td>314.76 (n/a)</td><td>267.70 (n/a)</td><td>231.40 (n/a)</td><td>121.35 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>600.10 (n/a)</td><td>406.32 (n/a)</td><td>409.40 (n/a)</td><td>246.80 (n/a)</td><td>142.91 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.20 (-4.31%)</td><td>0.16 (+1.88%)</td><td>0.16 (-2.39%)</td><td>0.10 (-2.51%)</td><td>0.04 (-17.25%)</td><td>471.40 (+2.57%)</td><td>323.88 (-4.30%)</td><td>309.50 (+2.45%)</td><td>243.50 (+4.51%)</td><td>93.09 (-15.77%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>459.60 (n/a)</td><td>338.44 (n/a)</td><td>302.10 (n/a)</td><td>233.00 (n/a)</td><td>110.52 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>604.40 (n/a)</td><td>382.10 (n/a)</td><td>381.80 (n/a)</td><td>209.90 (n/a)</td><td>160.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>507.40 (n/a)</td><td>317.12 (n/a)</td><td>265.30 (n/a)</td><td>236.20 (n/a)</td><td>111.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>537.20 (n/a)</td><td>344.86 (n/a)</td><td>255.60 (n/a)</td><td>238.10 (n/a)</td><td>136.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.20 (n/a)</td><td>377.50 (n/a)</td><td>297.80 (n/a)</td><td>239.70 (n/a)</td><td>153.53 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1942.50 (n/a)</td><td>751.56 (n/a)</td><td>432.20 (n/a)</td><td>212.50 (n/a)</td><td>721.87 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.20 (n/a)</td><td>299.92 (n/a)</td><td>232.40 (n/a)</td><td>206.70 (n/a)</td><td>136.40 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1918.40 (n/a)</td><td>672.90 (n/a)</td><td>368.20 (n/a)</td><td>238.10 (n/a)</td><td>707.88 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1357.70 (n/a)</td><td>657.64 (n/a)</td><td>609.40 (n/a)</td><td>305.20 (n/a)</td><td>425.15 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>615.10 (n/a)</td><td>399.22 (n/a)</td><td>325.60 (n/a)</td><td>290.10 (n/a)</td><td>139.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>456.00 (n/a)</td><td>324.92 (n/a)</td><td>261.50 (n/a)</td><td>234.30 (n/a)</td><td>103.33 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>560.20 (n/a)</td><td>368.28 (n/a)</td><td>293.50 (n/a)</td><td>242.70 (n/a)</td><td>148.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>533.70 (n/a)</td><td>322.46 (n/a)</td><td>256.30 (n/a)</td><td>225.30 (n/a)</td><td>126.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>516.20 (n/a)</td><td>324.98 (n/a)</td><td>247.80 (n/a)</td><td>202.60 (n/a)</td><td>133.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>499.20 (n/a)</td><td>312.86 (n/a)</td><td>297.30 (n/a)</td><td>215.10 (n/a)</td><td>114.30 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.90 (n/a)</td><td>318.74 (n/a)</td><td>268.00 (n/a)</td><td>239.80 (n/a)</td><td>119.61 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1132.80 (n/a)</td><td>556.42 (n/a)</td><td>543.20 (n/a)</td><td>223.10 (n/a)</td><td>360.54 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.20 (n/a)</td><td>367.32 (n/a)</td><td>312.80 (n/a)</td><td>225.50 (n/a)</td><td>134.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>769.70 (n/a)</td><td>426.06 (n/a)</td><td>417.90 (n/a)</td><td>229.80 (n/a)</td><td>219.54 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.00 (n/a)</td><td>470.46 (n/a)</td><td>541.80 (n/a)</td><td>251.20 (n/a)</td><td>136.52 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>410.30 (n/a)</td><td>309.24 (n/a)</td><td>295.20 (n/a)</td><td>242.20 (n/a)</td><td>64.59 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.10 (n/a)</td><td>346.68 (n/a)</td><td>326.30 (n/a)</td><td>197.20 (n/a)</td><td>142.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.70 (n/a)</td><td>387.20 (n/a)</td><td>353.80 (n/a)</td><td>245.60 (n/a)</td><td>117.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>747.70 (n/a)</td><td>429.58 (n/a)</td><td>295.30 (n/a)</td><td>244.00 (n/a)</td><td>219.89 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.90 (n/a)</td><td>338.72 (n/a)</td><td>288.60 (n/a)</td><td>262.10 (n/a)</td><td>96.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>498.40 (n/a)</td><td>378.00 (n/a)</td><td>374.20 (n/a)</td><td>275.80 (n/a)</td><td>83.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>522.50 (n/a)</td><td>330.50 (n/a)</td><td>299.40 (n/a)</td><td>250.70 (n/a)</td><td>109.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>540.10 (n/a)</td><td>348.18 (n/a)</td><td>299.30 (n/a)</td><td>245.50 (n/a)</td><td>125.12 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>458.30 (n/a)</td><td>324.16 (n/a)</td><td>250.70 (n/a)</td><td>242.70 (n/a)</td><td>105.92 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>288.90 (n/a)</td><td>271.32 (n/a)</td><td>273.50 (n/a)</td><td>241.60 (n/a)</td><td>19.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>546.50 (n/a)</td><td>368.24 (n/a)</td><td>288.00 (n/a)</td><td>242.40 (n/a)</td><td>152.43 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>665.20 (n/a)</td><td>498.40 (n/a)</td><td>542.10 (n/a)</td><td>284.50 (n/a)</td><td>158.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>659.60 (n/a)</td><td>392.64 (n/a)</td><td>309.70 (n/a)</td><td>186.30 (n/a)</td><td>208.16 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>534.20 (n/a)</td><td>398.14 (n/a)</td><td>345.30 (n/a)</td><td>264.90 (n/a)</td><td>121.44 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>616.30 (n/a)</td><td>375.12 (n/a)</td><td>285.40 (n/a)</td><td>257.40 (n/a)</td><td>156.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>573.70 (n/a)</td><td>415.60 (n/a)</td><td>427.90 (n/a)</td><td>215.50 (n/a)</td><td>129.92 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1920.40 (n/a)</td><td>637.80 (n/a)</td><td>319.00 (n/a)</td><td>231.80 (n/a)</td><td>722.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>717.80 (n/a)</td><td>546.20 (n/a)</td><td>516.40 (n/a)</td><td>453.10 (n/a)</td><td>107.17 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.51 (-17.56%)</td><td>0.39 (-5.44%)</td><td>0.34 (-8.41%)</td><td>0.33 (-1.28%)</td><td>0.08 <b>(-31.46%)</b></td><td>662.60 (+1.28%)</td><td>584.86 (+3.89%)</td><td>655.20 (+9.18%)</td><td>435.30 <b>(+21.29%)</b></td><td>106.18 (-9.43%)</td><td>21.68 (-17.56%)</td><td>16.62 (-5.44%)</td><td>14.40 (-8.41%)</td><td>14.24 (-1.28%)</td><td>3.37 <b>(-31.46%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.62 (n/a)</td><td>0.41 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>654.20 (n/a)</td><td>562.98 (n/a)</td><td>600.10 (n/a)</td><td>358.90 (n/a)</td><td>117.23 (n/a)</td><td>26.30 (n/a)</td><td>17.58 (n/a)</td><td>15.73 (n/a)</td><td>14.43 (n/a)</td><td>4.92 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.58 (+18.63%)</td><td>0.43 <b>(+23.25%)</b></td><td>0.47 <b>(+39.92%)</b></td><td>0.19 <b>(+52.67%)</b></td><td>0.15 (+2.92%)</td><td>1170.20 <b>(-34.50%)</b></td><td>600.26 <b>(-25.62%)</b></td><td>471.20 <b>(-28.53%)</b></td><td>381.90 (-15.71%)</td><td>324.49 <b>(-41.71%)</b></td><td>24.71 (+18.63%)</td><td>18.40 <b>(+23.25%)</b></td><td>20.03 <b>(+39.92%)</b></td><td>8.06 <b>(+52.67%)</b></td><td>6.40 (+2.92%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.49 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>1786.60 (n/a)</td><td>807.02 (n/a)</td><td>659.30 (n/a)</td><td>453.10 (n/a)</td><td>556.67 (n/a)</td><td>20.83 (n/a)</td><td>14.93 (n/a)</td><td>14.31 (n/a)</td><td>5.28 (n/a)</td><td>6.22 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.31 (-0.29%)</td><td>0.30 (-1.01%)</td><td>0.30 (-1.49%)</td><td>0.29 (-2.52%)</td><td>0.01 <b>(+57.70%)</b></td><td>86059.70 (+2.58%)</td><td>82842.22 (+1.05%)</td><td>82613.50 (+1.52%)</td><td>80821.30 (+0.29%)</td><td>2134.93 <b>(+61.87%)</b></td><td>212.57 (-0.29%)</td><td>207.49 (-1.01%)</td><td>207.95 (-1.49%)</td><td>199.63 (-2.52%)</td><td>5.28 <b>(+57.70%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83893.30 (n/a)</td><td>81978.16 (n/a)</td><td>81379.50 (n/a)</td><td>80588.50 (n/a)</td><td>1318.91 (n/a)</td><td>213.18 (n/a)</td><td>209.61 (n/a)</td><td>211.11 (n/a)</td><td>204.78 (n/a)</td><td>3.35 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>1.03 (+0.65%)</td><td>1.00 (-1.32%)</td><td>0.99 (-2.52%)</td><td>0.97 (-2.57%)</td><td>0.02 <b>(+150.33%)</b></td><td>25909.30 (+2.64%)</td><td>25278.74 (+1.37%)</td><td>25487.50 (+2.59%)</td><td>24523.30 (-0.64%)</td><td>576.93 <b>(+154.80%)</b></td><td>700.55 (+0.65%)</td><td>679.90 (-1.32%)</td><td>674.05 (-2.52%)</td><td>663.08 (-2.57%)</td><td>15.62 <b>(+150.32%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25244.00 (n/a)</td><td>24935.88 (n/a)</td><td>24845.20 (n/a)</td><td>24681.70 (n/a)</td><td>226.43 (n/a)</td><td>696.06 (n/a)</td><td>689.01 (n/a)</td><td>691.48 (n/a)</td><td>680.55 (n/a)</td><td>6.24 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.82 (-0.99%)</td><td>0.81 (+0.72%)</td><td>0.82 (+1.47%)</td><td>0.80 (+1.70%)</td><td>0.01 <b>(-41.82%)</b></td><td>94368.70 (-1.67%)</td><td>93000.88 (-0.74%)</td><td>92403.60 (-1.45%)</td><td>91966.30 (+1.00%)</td><td>1206.81 <b>(-42.26%)</b></td><td>747.22 (-0.99%)</td><td>739.01 (+0.72%)</td><td>743.69 (+1.47%)</td><td>728.20 (+1.70%)</td><td>9.55 <b>(-41.82%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.83 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.02 (n/a)</td><td>95975.80 (n/a)</td><td>93695.72 (n/a)</td><td>93761.90 (n/a)</td><td>91052.40 (n/a)</td><td>2090.20 (n/a)</td><td>754.72 (n/a)</td><td>733.73 (n/a)</td><td>732.91 (n/a)</td><td>716.01 (n/a)</td><td>16.42 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.78 (-0.15%)</td><td>0.76 (-1.70%)</td><td>0.75 (-2.67%)</td><td>0.73 (-2.33%)</td><td>0.02 <b>(+71.18%)</b></td><td>103383.10 (+2.38%)</td><td>99908.88 (+1.78%)</td><td>100492.00 (+2.75%)</td><td>97007.80 (+0.15%)</td><td>2835.09 <b>(+73.94%)</b></td><td>708.39 (-0.15%)</td><td>688.27 (-1.70%)</td><td>683.83 (-2.67%)</td><td>664.71 (-2.33%)</td><td>19.55 <b>(+71.18%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100975.30 (n/a)</td><td>98166.04 (n/a)</td><td>97806.90 (n/a)</td><td>96859.60 (n/a)</td><td>1629.90 (n/a)</td><td>709.48 (n/a)</td><td>700.18 (n/a)</td><td>702.60 (n/a)</td><td>680.56 (n/a)</td><td>11.42 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.81 (+0.70%)</td><td>0.80 (+0.70%)</td><td>0.80 (+0.81%)</td><td>0.79 (+0.17%)</td><td>0.01 <b>(+26.81%)</b></td><td>95544.00 (-0.17%)</td><td>94425.70 (-0.69%)</td><td>94437.60 (-0.80%)</td><td>93492.30 (-0.69%)</td><td>738.81 <b>(+25.94%)</b></td><td>735.03 (+0.70%)</td><td>727.80 (+0.70%)</td><td>727.67 (+0.81%)</td><td>719.24 (+0.17%)</td><td>5.68 <b>(+26.81%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95708.40 (n/a)</td><td>95081.36 (n/a)</td><td>95200.40 (n/a)</td><td>94143.10 (n/a)</td><td>586.64 (n/a)</td><td>729.95 (n/a)</td><td>722.77 (n/a)</td><td>721.84 (n/a)</td><td>718.01 (n/a)</td><td>4.48 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.28 <b>(+28.53%)</b></td><td>3.57 (-1.79%)</td><td>4.10 (+12.80%)</td><td>2.17 <b>(-20.72%)</b></td><td>1.36 <b>(+144.98%)</b></td><td>4101.70 <b>(+26.14%)</b></td><td>2839.62 (+13.39%)</td><td>2175.90 (-11.35%)</td><td>1686.50 <b>(-22.20%)</b></td><td>1152.81 <b>(+161.25%)</b></td><td>318.34 <b>(+28.53%)</b></td><td>215.12 (-1.79%)</td><td>246.73 (+12.80%)</td><td>130.89 <b>(-20.72%)</b></td><td>81.70 <b>(+144.98%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>4.11 (n/a)</td><td>3.64 (n/a)</td><td>3.63 (n/a)</td><td>2.74 (n/a)</td><td>0.55 (n/a)</td><td>3251.80 (n/a)</td><td>2504.40 (n/a)</td><td>2454.40 (n/a)</td><td>2167.60 (n/a)</td><td>441.27 (n/a)</td><td>247.68 (n/a)</td><td>219.04 (n/a)</td><td>218.74 (n/a)</td><td>165.10 (n/a)</td><td>33.35 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>4.92 (+3.18%)</td><td>2.92 (-16.41%)</td><td>2.26 <b>(-40.17%)</b></td><td>2.18 (-0.62%)</td><td>1.17 (-2.12%)</td><td>4084.90 (+0.62%)</td><td>3364.74 (+18.45%)</td><td>3935.80 <b>(+67.13%)</b></td><td>1811.40 (-3.08%)</td><td>986.06 (-6.91%)</td><td>296.39 (+3.18%)</td><td>175.81 (-16.41%)</td><td>136.41 <b>(-40.17%)</b></td><td>131.43 (-0.62%)</td><td>70.62 (-2.12%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>4.77 (n/a)</td><td>3.49 (n/a)</td><td>3.78 (n/a)</td><td>2.20 (n/a)</td><td>1.20 (n/a)</td><td>4059.60 (n/a)</td><td>2840.62 (n/a)</td><td>2354.90 (n/a)</td><td>1868.90 (n/a)</td><td>1059.24 (n/a)</td><td>287.26 (n/a)</td><td>210.32 (n/a)</td><td>227.98 (n/a)</td><td>132.25 (n/a)</td><td>72.15 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.97 <b>(-29.30%)</b></td><td>3.10 <b>(-30.69%)</b></td><td>3.46 <b>(-34.10%)</b></td><td>2.15 (-1.62%)</td><td>0.86 <b>(-38.81%)</b></td><td>4151.70 (+1.64%)</td><td>3081.24 <b>(+36.85%)</b></td><td>2575.70 <b>(+51.75%)</b></td><td>2247.10 <b>(+41.44%)</b></td><td>934.91 (-11.13%)</td><td>238.92 <b>(-29.30%)</b></td><td>186.82 <b>(-30.69%)</b></td><td>208.44 <b>(-34.10%)</b></td><td>129.31 (-1.62%)</td><td>52.03 <b>(-38.81%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.61 (n/a)</td><td>4.48 (n/a)</td><td>5.25 (n/a)</td><td>2.18 (n/a)</td><td>1.41 (n/a)</td><td>4084.60 (n/a)</td><td>2251.52 (n/a)</td><td>1697.30 (n/a)</td><td>1588.70 (n/a)</td><td>1051.95 (n/a)</td><td>337.94 (n/a)</td><td>269.56 (n/a)</td><td>316.30 (n/a)</td><td>131.44 (n/a)</td><td>85.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>6.53 (+0.14%)</td><td>5.76 (+5.57%)</td><td>5.62 (+3.94%)</td><td>4.96 <b>(+25.39%)</b></td><td>0.67 <b>(-39.01%)</b></td><td>7036.40 <b>(-20.25%)</b></td><td>6123.12 (-7.57%)</td><td>6207.20 (-3.79%)</td><td>5342.20 (-0.14%)</td><td>712.40 <b>(-50.70%)</b></td><td>401.99 (+0.14%)</td><td>354.55 (+5.57%)</td><td>345.96 (+3.94%)</td><td>305.20 <b>(+25.39%)</b></td><td>41.24 <b>(-39.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>6.52 (n/a)</td><td>5.45 (n/a)</td><td>5.40 (n/a)</td><td>3.95 (n/a)</td><td>1.10 (n/a)</td><td>8822.80 (n/a)</td><td>6624.28 (n/a)</td><td>6452.00 (n/a)</td><td>5349.80 (n/a)</td><td>1445.09 (n/a)</td><td>401.41 (n/a)</td><td>335.85 (n/a)</td><td>332.84 (n/a)</td><td>243.40 (n/a)</td><td>67.62 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.13 (-8.02%)</td><td>4.21 (-16.38%)</td><td>4.09 <b>(-21.64%)</b></td><td>3.60 (-5.69%)</td><td>0.57 (-18.64%)</td><td>9688.90 (+6.03%)</td><td>8390.16 (+18.97%)</td><td>8528.40 <b>(+27.61%)</b></td><td>6790.20 (+8.71%)</td><td>1051.84 (-10.82%)</td><td>316.26 (-8.02%)</td><td>259.44 (-16.38%)</td><td>251.80 <b>(-21.64%)</b></td><td>221.64 (-5.69%)</td><td>35.04 (-18.64%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.58 (n/a)</td><td>5.04 (n/a)</td><td>5.22 (n/a)</td><td>3.82 (n/a)</td><td>0.70 (n/a)</td><td>9137.50 (n/a)</td><td>7052.52 (n/a)</td><td>6683.00 (n/a)</td><td>6245.90 (n/a)</td><td>1179.52 (n/a)</td><td>343.82 (n/a)</td><td>310.25 (n/a)</td><td>321.34 (n/a)</td><td>235.02 (n/a)</td><td>43.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.51 (-13.87%)</td><td>5.09 (-8.40%)</td><td>5.25 (-4.10%)</td><td>4.40 (-14.46%)</td><td>0.43 (-14.66%)</td><td>7918.50 (+16.90%)</td><td>6898.50 (+9.17%)</td><td>6639.10 (+4.28%)</td><td>6331.10 (+16.10%)</td><td>628.90 (+17.03%)</td><td>339.20 (-13.87%)</td><td>313.24 (-8.40%)</td><td>323.46 (-4.10%)</td><td>271.20 (-14.46%)</td><td>26.70 (-14.66%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>6.39 (n/a)</td><td>5.55 (n/a)</td><td>5.48 (n/a)</td><td>5.15 (n/a)</td><td>0.51 (n/a)</td><td>6773.50 (n/a)</td><td>6318.76 (n/a)</td><td>6366.90 (n/a)</td><td>5453.10 (n/a)</td><td>537.40 (n/a)</td><td>393.81 (n/a)</td><td>341.98 (n/a)</td><td>337.29 (n/a)</td><td>317.04 (n/a)</td><td>31.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.79 (+1.71%)</td><td>0.76 (+0.29%)</td><td>0.76 (+0.14%)</td><td>0.73 (-0.22%)</td><td>0.02 <b>(+34.60%)</b></td><td>102870.50 (+0.23%)</td><td>99080.76 (-0.26%)</td><td>98889.20 (-0.14%)</td><td>95744.00 (-1.68%)</td><td>2602.27 <b>(+32.22%)</b></td><td>717.74 (+1.71%)</td><td>693.95 (+0.29%)</td><td>694.91 (+0.14%)</td><td>668.02 (-0.22%)</td><td>18.13 <b>(+34.60%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>102639.10 (n/a)</td><td>99341.16 (n/a)</td><td>99029.40 (n/a)</td><td>97381.20 (n/a)</td><td>1968.20 (n/a)</td><td>705.67 (n/a)</td><td>691.97 (n/a)</td><td>693.93 (n/a)</td><td>669.53 (n/a)</td><td>13.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.78 (+1.05%)</td><td>0.75 (-2.26%)</td><td>0.75 (-1.99%)</td><td>0.71 (-6.69%)</td><td>0.02 <b>(+744.81%)</b></td><td>105986.20 (+7.17%)</td><td>100741.64 (+2.40%)</td><td>100307.80 (+2.04%)</td><td>97024.30 (-1.04%)</td><td>3312.77 <b>(+800.62%)</b></td><td>708.27 (+1.05%)</td><td>682.72 (-2.26%)</td><td>685.09 (-1.99%)</td><td>648.38 (-6.69%)</td><td>22.03 <b>(+744.81%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.00 (n/a)</td><td>98891.10 (n/a)</td><td>98383.70 (n/a)</td><td>98306.90 (n/a)</td><td>98043.70 (n/a)</td><td>367.83 (n/a)</td><td>700.91 (n/a)</td><td>698.49 (n/a)</td><td>699.03 (n/a)</td><td>694.90 (n/a)</td><td>2.61 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.81 (+0.46%)</td><td>0.81 (+0.51%)</td><td>0.81 (+0.63%)</td><td>0.80 (+0.39%)</td><td>0.00 (+3.53%)</td><td>94167.40 (-0.39%)</td><td>93360.92 (-0.51%)</td><td>93262.90 (-0.63%)</td><td>92860.10 (-0.46%)</td><td>529.97 (+2.70%)</td><td>740.03 (+0.46%)</td><td>736.08 (+0.51%)</td><td>736.84 (+0.63%)</td><td>729.76 (+0.39%)</td><td>4.17 (+3.53%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94533.80 (n/a)</td><td>93837.96 (n/a)</td><td>93854.20 (n/a)</td><td>93287.70 (n/a)</td><td>516.06 (n/a)</td><td>736.64 (n/a)</td><td>732.34 (n/a)</td><td>732.19 (n/a)</td><td>726.93 (n/a)</td><td>4.02 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.93 (-1.87%)</td><td>2.11 (-17.61%)</td><td>2.03 (+7.58%)</td><td>1.04 <b>(-32.25%)</b></td><td>1.11 (-1.32%)</td><td>7752.90 <b>(+47.59%)</b></td><td>4658.58 <b>(+27.62%)</b></td><td>3969.00 (-7.05%)</td><td>2051.90 (+1.90%)</td><td>2159.12 <b>(+51.62%)</b></td><td>1030.25 (-1.87%)</td><td>552.03 (-17.61%)</td><td>532.60 (+7.58%)</td><td>272.66 <b>(-32.25%)</b></td><td>291.56 (-1.32%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>4.00 (n/a)</td><td>2.56 (n/a)</td><td>1.89 (n/a)</td><td>1.53 (n/a)</td><td>1.13 (n/a)</td><td>5253.00 (n/a)</td><td>3650.26 (n/a)</td><td>4270.00 (n/a)</td><td>2013.60 (n/a)</td><td>1424.00 (n/a)</td><td>1049.83 (n/a)</td><td>670.05 (n/a)</td><td>495.07 (n/a)</td><td>402.43 (n/a)</td><td>295.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.25 (+14.05%)</td><td>0.21 (+12.12%)</td><td>0.20 (+8.39%)</td><td>0.18 <b>(+32.09%)</b></td><td>0.03 (-18.95%)</td><td>6858.50 <b>(-24.29%)</b></td><td>6024.78 (-12.13%)</td><td>6142.20 (-7.74%)</td><td>4973.90 (-12.32%)</td><td>679.20 <b>(-48.50%)</b></td><td>13.49 (+14.05%)</td><td>11.26 (+12.12%)</td><td>10.93 (+8.39%)</td><td>9.78 <b>(+32.09%)</b></td><td>1.36 (-18.95%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>9059.20 (n/a)</td><td>6856.64 (n/a)</td><td>6657.20 (n/a)</td><td>5672.70 (n/a)</td><td>1318.84 (n/a)</td><td>11.83 (n/a)</td><td>10.04 (n/a)</td><td>10.08 (n/a)</td><td>7.41 (n/a)</td><td>1.68 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.77 (n/a)</td><td>3.69 (n/a)</td><td>3.68 (n/a)</td><td>3.55 (n/a)</td><td>0.08 (n/a)</td><td>3.76 (n/a)</td><td>3.68 (n/a)</td><td>3.68 (n/a)</td><td>3.55 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>7.01 (+0.12%)</td><td>6.26 (+2.74%)</td><td>6.67 (+14.42%)</td><td>5.34 (-3.68%)</td><td>0.81 <b>(+36.02%)</b></td><td>7.00 (+0.12%)</td><td>6.26 (+2.74%)</td><td>6.67 (+14.42%)</td><td>5.34 (-3.68%)</td><td>0.81 <b>(+36.02%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>7.00 (n/a)</td><td>6.09 (n/a)</td><td>5.83 (n/a)</td><td>5.55 (n/a)</td><td>0.60 (n/a)</td><td>6.99 (n/a)</td><td>6.09 (n/a)</td><td>5.83 (n/a)</td><td>5.54 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>12.50 (-11.77%)</td><td>9.52 (-4.38%)</td><td>9.05 (+8.26%)</td><td>8.16 (+9.73%)</td><td>1.74 <b>(-42.91%)</b></td><td>12.49 (-11.77%)</td><td>9.52 (-4.38%)</td><td>9.04 (+8.26%)</td><td>8.15 (+9.73%)</td><td>1.73 <b>(-42.91%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>14.17 (n/a)</td><td>9.96 (n/a)</td><td>8.36 (n/a)</td><td>7.44 (n/a)</td><td>3.04 (n/a)</td><td>14.16 (n/a)</td><td>9.95 (n/a)</td><td>8.35 (n/a)</td><td>7.43 (n/a)</td><td>3.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.73 (n/a)</td><td>3.54 (n/a)</td><td>3.56 (n/a)</td><td>3.30 (n/a)</td><td>0.19 (n/a)</td><td>3.73 (n/a)</td><td>3.54 (n/a)</td><td>3.55 (n/a)</td><td>3.30 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>7.38 (+4.72%)</td><td>6.34 (-3.73%)</td><td>5.82 (-16.07%)</td><td>5.63 (-4.99%)</td><td>0.86 <b>(+52.48%)</b></td><td>7.37 (+4.72%)</td><td>6.33 (-3.73%)</td><td>5.81 (-16.07%)</td><td>5.63 (-4.99%)</td><td>0.86 <b>(+52.48%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>7.04 (n/a)</td><td>6.58 (n/a)</td><td>6.93 (n/a)</td><td>5.93 (n/a)</td><td>0.57 (n/a)</td><td>7.04 (n/a)</td><td>6.58 (n/a)</td><td>6.93 (n/a)</td><td>5.93 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>14.05 <b>(+64.38%)</b></td><td>10.46 <b>(+30.55%)</b></td><td>10.27 <b>(+27.95%)</b></td><td>6.99 (-4.94%)</td><td>2.98 <b>(+537.91%)</b></td><td>14.05 <b>(+64.38%)</b></td><td>10.45 <b>(+30.55%)</b></td><td>10.26 <b>(+27.95%)</b></td><td>6.99 (-4.94%)</td><td>2.98 <b>(+537.91%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>8.55 (n/a)</td><td>8.01 (n/a)</td><td>8.02 (n/a)</td><td>7.36 (n/a)</td><td>0.47 (n/a)</td><td>8.54 (n/a)</td><td>8.01 (n/a)</td><td>8.02 (n/a)</td><td>7.35 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>2.83 (-11.78%)</td><td>2.04 (-6.89%)</td><td>2.49 (-8.08%)</td><td>1.02 (-1.55%)</td><td>0.89 (-16.87%)</td><td>2.83 (-11.78%)</td><td>2.03 (-6.89%)</td><td>2.49 (-8.08%)</td><td>1.01 (-1.55%)</td><td>0.88 (-16.87%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.21 (n/a)</td><td>2.19 (n/a)</td><td>2.71 (n/a)</td><td>1.03 (n/a)</td><td>1.07 (n/a)</td><td>3.20 (n/a)</td><td>2.18 (n/a)</td><td>2.71 (n/a)</td><td>1.03 (n/a)</td><td>1.06 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.57 (+12.71%)</td><td>0.39 (-7.00%)</td><td>0.42 (-15.52%)</td><td>0.09 <b>(-67.57%)</b></td><td>0.19 <b>(+72.31%)</b></td><td>0.57 (+12.71%)</td><td>0.38 (-7.00%)</td><td>0.41 (-15.52%)</td><td>0.09 <b>(-67.57%)</b></td><td>0.19 <b>(+72.31%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.49 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td><td>0.50 (n/a)</td><td>0.41 (n/a)</td><td>0.48 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.79 (+6.88%)</td><td>0.52 (+10.73%)</td><td>0.48 (+8.15%)</td><td>0.32 <b>(+309.33%)</b></td><td>0.20 <b>(-23.58%)</b></td><td>0.78 (+6.88%)</td><td>0.51 (+10.73%)</td><td>0.47 (+8.15%)</td><td>0.31 <b>(+309.33%)</b></td><td>0.19 <b>(-23.58%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.74 (n/a)</td><td>0.47 (n/a)</td><td>0.44 (n/a)</td><td>0.08 (n/a)</td><td>0.26 (n/a)</td><td>0.73 (n/a)</td><td>0.46 (n/a)</td><td>0.43 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>2.63 (+11.15%)</td><td>2.44 <b>(+28.30%)</b></td><td>2.46 <b>(+27.52%)</b></td><td>2.29 <b>(+53.05%)</b></td><td>0.13 <b>(-62.53%)</b></td><td>2.59 (+11.15%)</td><td>2.40 <b>(+28.30%)</b></td><td>2.42 <b>(+27.52%)</b></td><td>2.26 <b>(+53.05%)</b></td><td>0.13 <b>(-62.53%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>2.37 (n/a)</td><td>1.90 (n/a)</td><td>1.93 (n/a)</td><td>1.50 (n/a)</td><td>0.35 (n/a)</td><td>2.33 (n/a)</td><td>1.87 (n/a)</td><td>1.90 (n/a)</td><td>1.47 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>471.80 (n/a)</td><td>381.30 (n/a)</td><td>382.10 (n/a)</td><td>276.40 (n/a)</td><td>90.65 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.80 (n/a)</td><td>418.04 (n/a)</td><td>439.20 (n/a)</td><td>248.40 (n/a)</td><td>149.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.00 (n/a)</td><td>430.24 (n/a)</td><td>472.40 (n/a)</td><td>257.50 (n/a)</td><td>104.10 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1870.40 (n/a)</td><td>730.16 (n/a)</td><td>484.60 (n/a)</td><td>237.50 (n/a)</td><td>651.43 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>584.10 (n/a)</td><td>428.82 (n/a)</td><td>454.10 (n/a)</td><td>273.10 (n/a)</td><td>126.79 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>708.30 (n/a)</td><td>428.66 (n/a)</td><td>317.00 (n/a)</td><td>259.80 (n/a)</td><td>201.06 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.00 (n/a)</td><td>406.60 (n/a)</td><td>477.30 (n/a)</td><td>247.70 (n/a)</td><td>136.00 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.20 (n/a)</td><td>324.28 (n/a)</td><td>249.20 (n/a)</td><td>238.00 (n/a)</td><td>127.70 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>426.50 (n/a)</td><td>302.16 (n/a)</td><td>278.10 (n/a)</td><td>221.80 (n/a)</td><td>82.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>315.70 (n/a)</td><td>252.58 (n/a)</td><td>262.50 (n/a)</td><td>153.00 (n/a)</td><td>64.02 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.20 (n/a)</td><td>400.32 (n/a)</td><td>340.80 (n/a)</td><td>206.90 (n/a)</td><td>194.18 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2429.50 (n/a)</td><td>869.88 (n/a)</td><td>547.80 (n/a)</td><td>273.30 (n/a)</td><td>880.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>585.00 (n/a)</td><td>416.92 (n/a)</td><td>397.90 (n/a)</td><td>260.40 (n/a)</td><td>155.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>523.90 (n/a)</td><td>324.88 (n/a)</td><td>292.20 (n/a)</td><td>248.40 (n/a)</td><td>113.62 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>660.30 (n/a)</td><td>376.86 (n/a)</td><td>300.90 (n/a)</td><td>190.70 (n/a)</td><td>192.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1983.50 (n/a)</td><td>727.62 (n/a)</td><td>538.50 (n/a)</td><td>229.10 (n/a)</td><td>719.86 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>560.00 (n/a)</td><td>361.24 (n/a)</td><td>302.40 (n/a)</td><td>290.70 (n/a)</td><td>114.76 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1305.70 (n/a)</td><td>635.76 (n/a)</td><td>471.30 (n/a)</td><td>421.40 (n/a)</td><td>376.37 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>682.90 (n/a)</td><td>456.42 (n/a)</td><td>450.00 (n/a)</td><td>278.30 (n/a)</td><td>159.55 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2495.40 (n/a)</td><td>805.28 (n/a)</td><td>463.50 (n/a)</td><td>254.70 (n/a)</td><td>951.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>556.20 (n/a)</td><td>403.48 (n/a)</td><td>408.10 (n/a)</td><td>238.70 (n/a)</td><td>141.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>567.40 (n/a)</td><td>481.32 (n/a)</td><td>481.10 (n/a)</td><td>415.40 (n/a)</td><td>56.79 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>497.20 (n/a)</td><td>411.76 (n/a)</td><td>459.00 (n/a)</td><td>293.50 (n/a)</td><td>86.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>747.30 (n/a)</td><td>548.32 (n/a)</td><td>552.60 (n/a)</td><td>374.50 (n/a)</td><td>135.68 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-11.82%)</td><td>0.01 (-5.92%)</td><td>0.01 <b>(+34.32%)</b></td><td>0.01 <b>(-33.88%)</b></td><td>0.01 (-2.61%)</td><td>715.00 <b>(+51.26%)</b></td><td>394.44 (+14.78%)</td><td>284.10 <b>(-25.55%)</b></td><td>202.10 (+13.41%)</td><td>218.36 <b>(+66.43%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>472.70 (n/a)</td><td>343.64 (n/a)</td><td>381.60 (n/a)</td><td>178.20 (n/a)</td><td>131.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-14.42%)</td><td>0.01 <b>(-28.87%)</b></td><td>0.01 <b>(-45.40%)</b></td><td>0.01 (-6.18%)</td><td>0.00 (-18.37%)</td><td>594.30 (+6.60%)</td><td>444.92 <b>(+37.84%)</b></td><td>452.10 <b>(+83.11%)</b></td><td>243.80 (+16.87%)</td><td>148.15 (+2.79%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.50 (n/a)</td><td>322.78 (n/a)</td><td>246.90 (n/a)</td><td>208.60 (n/a)</td><td>144.13 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-3.72%)</td><td>0.01 (-4.67%)</td><td>0.01 <b>(-32.76%)</b></td><td>0.01 (+12.84%)</td><td>0.01 (+0.07%)</td><td>538.10 (-11.38%)</td><td>382.84 (+3.08%)</td><td>452.90 <b>(+48.74%)</b></td><td>231.30 (+3.86%)</td><td>142.17 (-14.21%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.20 (n/a)</td><td>371.40 (n/a)</td><td>304.50 (n/a)</td><td>222.70 (n/a)</td><td>165.73 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 <b>(+24.73%)</b></td><td>0.01 <b>(+21.24%)</b></td><td>0.01 <b>(+54.78%)</b></td><td>0.01 (-5.87%)</td><td>0.00 <b>(+56.40%)</b></td><td>570.90 (+6.23%)</td><td>355.94 (-12.13%)</td><td>274.20 <b>(-35.38%)</b></td><td>232.20 (-19.82%)</td><td>147.57 <b>(+37.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.40 (n/a)</td><td>405.08 (n/a)</td><td>424.30 (n/a)</td><td>289.60 (n/a)</td><td>107.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (+18.07%)</td><td>0.01 (+11.51%)</td><td>0.01 <b>(+22.34%)</b></td><td>0.01 (-12.48%)</td><td>0.00 <b>(+58.78%)</b></td><td>503.40 (+14.25%)</td><td>345.92 (-6.00%)</td><td>310.50 (-18.25%)</td><td>235.20 (-15.30%)</td><td>114.13 <b>(+50.67%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>440.60 (n/a)</td><td>368.00 (n/a)</td><td>379.80 (n/a)</td><td>277.70 (n/a)</td><td>75.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-2.96%)</td><td>0.01 (-12.69%)</td><td>0.01 <b>(-24.17%)</b></td><td>0.01 <b>(-32.76%)</b></td><td>0.00 <b>(+67.50%)</b></td><td>581.50 <b>(+48.72%)</b></td><td>420.48 <b>(+25.43%)</b></td><td>452.80 <b>(+31.86%)</b></td><td>248.40 (+3.07%)</td><td>151.66 <b>(+159.51%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>391.00 (n/a)</td><td>335.22 (n/a)</td><td>343.40 (n/a)</td><td>241.00 (n/a)</td><td>58.44 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 <b>(+21.15%)</b></td><td>0.02 (-19.19%)</td><td>0.02 <b>(-41.83%)</b></td><td>0.01 <b>(-33.99%)</b></td><td>0.02 <b>(+78.14%)</b></td><td>599.70 <b>(+51.48%)</b></td><td>430.44 <b>(+44.30%)</b></td><td>483.20 <b>(+71.90%)</b></td><td>156.40 (-17.47%)</td><td>165.52 <b>(+95.96%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>395.90 (n/a)</td><td>298.30 (n/a)</td><td>281.10 (n/a)</td><td>189.50 (n/a)</td><td>84.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (-8.08%)</td><td>0.02 <b>(-26.08%)</b></td><td>0.02 <b>(-29.02%)</b></td><td>0.01 <b>(-48.81%)</b></td><td>0.01 <b>(+34.05%)</b></td><td>777.20 <b>(+95.37%)</b></td><td>419.40 <b>(+53.85%)</b></td><td>340.30 <b>(+40.85%)</b></td><td>235.80 (+8.81%)</td><td>219.73 <b>(+189.73%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>397.80 (n/a)</td><td>272.60 (n/a)</td><td>241.60 (n/a)</td><td>216.70 (n/a)</td><td>75.84 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(-20.04%)</b></td><td>0.02 (-9.36%)</td><td>0.02 <b>(-22.15%)</b></td><td>0.01 <b>(+30.54%)</b></td><td>0.01 <b>(-47.04%)</b></td><td>599.00 <b>(-23.40%)</b></td><td>393.22 (-3.61%)</td><td>348.50 <b>(+28.46%)</b></td><td>307.60 <b>(+25.09%)</b></td><td>120.28 <b>(-47.36%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>782.00 (n/a)</td><td>407.96 (n/a)</td><td>271.30 (n/a)</td><td>245.90 (n/a)</td><td>228.51 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (-17.71%)</td><td>0.02 (-5.15%)</td><td>0.02 (+2.30%)</td><td>0.02 <b>(+28.55%)</b></td><td>0.01 <b>(-37.20%)</b></td><td>501.10 <b>(-22.20%)</b></td><td>374.82 (-5.76%)</td><td>389.30 (-2.24%)</td><td>242.10 <b>(+21.54%)</b></td><td>113.48 <b>(-38.89%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>644.10 (n/a)</td><td>397.72 (n/a)</td><td>398.20 (n/a)</td><td>199.20 (n/a)</td><td>185.69 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (+1.00%)</td><td>0.02 (-19.87%)</td><td>0.02 <b>(-37.90%)</b></td><td>0.01 <b>(-22.12%)</b></td><td>0.01 (+4.05%)</td><td>734.50 <b>(+28.41%)</b></td><td>458.76 <b>(+28.50%)</b></td><td>462.80 <b>(+61.03%)</b></td><td>254.00 (-0.97%)</td><td>179.94 <b>(+33.94%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.00 (n/a)</td><td>357.02 (n/a)</td><td>287.40 (n/a)</td><td>256.50 (n/a)</td><td>134.35 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (+2.17%)</td><td>0.02 (-19.13%)</td><td>0.02 <b>(-35.00%)</b></td><td>0.01 (-9.15%)</td><td>0.01 (+4.69%)</td><td>687.00 (+10.08%)</td><td>496.64 <b>(+25.33%)</b></td><td>514.00 <b>(+53.85%)</b></td><td>235.70 (-2.12%)</td><td>176.72 (+8.25%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>624.10 (n/a)</td><td>396.26 (n/a)</td><td>334.10 (n/a)</td><td>240.80 (n/a)</td><td>163.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (+9.98%)</td><td>0.02 (+5.67%)</td><td>0.02 (+10.30%)</td><td>0.00 <b>(-66.42%)</b></td><td>0.01 <b>(+51.82%)</b></td><td>1846.50 <b>(+197.77%)</b></td><td>667.38 <b>(+46.04%)</b></td><td>474.80 (-9.32%)</td><td>210.60 (-9.11%)</td><td>674.68 <b>(+325.26%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.10 (n/a)</td><td>456.98 (n/a)</td><td>523.60 (n/a)</td><td>231.70 (n/a)</td><td>158.65 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(+32.42%)</b></td><td>0.02 (+5.39%)</td><td>0.02 <b>(-23.99%)</b></td><td>0.01 (+10.83%)</td><td>0.01 <b>(+63.55%)</b></td><td>599.00 (-9.78%)</td><td>469.48 (-1.54%)</td><td>545.70 <b>(+31.56%)</b></td><td>273.50 <b>(-24.49%)</b></td><td>136.58 (+10.34%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>663.90 (n/a)</td><td>476.82 (n/a)</td><td>414.80 (n/a)</td><td>362.20 (n/a)</td><td>123.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (-6.37%)</td><td>0.04 <b>(-23.74%)</b></td><td>0.03 <b>(-47.80%)</b></td><td>0.03 <b>(-25.63%)</b></td><td>0.02 <b>(+52.61%)</b></td><td>589.20 <b>(+34.46%)</b></td><td>428.70 <b>(+45.29%)</b></td><td>523.10 <b>(+91.54%)</b></td><td>244.40 (+6.82%)</td><td>169.25 <b>(+101.79%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>438.20 (n/a)</td><td>295.06 (n/a)</td><td>273.10 (n/a)</td><td>228.80 (n/a)</td><td>83.87 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (+7.05%)</td><td>0.06 <b>(+37.00%)</b></td><td>0.07 <b>(+91.22%)</b></td><td>0.04 <b>(+483.28%)</b></td><td>0.02 <b>(-37.63%)</b></td><td>426.70 <b>(-82.85%)</b></td><td>309.68 <b>(-60.97%)</b></td><td>250.10 <b>(-47.69%)</b></td><td>222.40 (-6.59%)</td><td>97.65 <b>(-89.79%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2488.60 (n/a)</td><td>793.40 (n/a)</td><td>478.10 (n/a)</td><td>238.10 (n/a)</td><td>956.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (-9.25%)</td><td>0.04 <b>(-23.05%)</b></td><td>0.04 <b>(-23.24%)</b></td><td>0.01 <b>(-67.43%)</b></td><td>0.02 (+13.74%)</td><td>1842.10 <b>(+207.02%)</b></td><td>703.80 <b>(+77.77%)</b></td><td>401.40 <b>(+30.28%)</b></td><td>267.80 (+10.21%)</td><td>650.34 <b>(+303.10%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>600.00 (n/a)</td><td>395.90 (n/a)</td><td>308.10 (n/a)</td><td>243.00 (n/a)</td><td>161.34 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 <b>(+25.49%)</b></td><td>0.06 <b>(+37.88%)</b></td><td>0.06 <b>(+72.61%)</b></td><td>0.03 <b>(+55.45%)</b></td><td>0.02 (+19.40%)</td><td>512.90 <b>(-35.67%)</b></td><td>328.36 <b>(-29.72%)</b></td><td>273.00 <b>(-42.06%)</b></td><td>197.20 <b>(-20.29%)</b></td><td>132.19 <b>(-37.15%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>797.30 (n/a)</td><td>467.24 (n/a)</td><td>471.20 (n/a)</td><td>247.40 (n/a)</td><td>210.34 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (+5.90%)</td><td>0.04 (-14.55%)</td><td>0.03 <b>(-35.44%)</b></td><td>0.03 (-8.00%)</td><td>0.02 <b>(+23.05%)</b></td><td>590.00 (+8.70%)</td><td>445.72 <b>(+22.16%)</b></td><td>476.40 <b>(+54.93%)</b></td><td>229.70 (-5.55%)</td><td>155.34 <b>(+27.10%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>542.80 (n/a)</td><td>364.86 (n/a)</td><td>307.50 (n/a)</td><td>243.20 (n/a)</td><td>122.22 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(-47.49%)</b></td><td>0.02 <b>(-40.71%)</b></td><td>0.03 (-12.09%)</td><td>0.01 <b>(-61.19%)</b></td><td>0.01 <b>(-39.43%)</b></td><td>1548.30 <b>(+157.66%)</b></td><td>861.74 <b>(+79.66%)</b></td><td>644.30 (+13.75%)</td><td>522.00 <b>(+90.44%)</b></td><td>431.12 <b>(+182.71%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>600.90 (n/a)</td><td>479.66 (n/a)</td><td>566.40 (n/a)</td><td>274.10 (n/a)</td><td>152.49 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (-8.12%)</td><td>0.09 <b>(-25.92%)</b></td><td>0.07 <b>(-49.41%)</b></td><td>0.07 <b>(+21.97%)</b></td><td>0.03 <b>(-21.76%)</b></td><td>500.30 (-18.01%)</td><td>397.34 <b>(+26.44%)</b></td><td>459.40 <b>(+97.68%)</b></td><td>236.80 (+8.82%)</td><td>116.42 <b>(-30.61%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>610.20 (n/a)</td><td>314.24 (n/a)</td><td>232.40 (n/a)</td><td>217.60 (n/a)</td><td>167.76 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.17 <b>(+28.63%)</b></td><td>0.09 <b>(-25.21%)</b></td><td>0.07 <b>(-39.40%)</b></td><td>0.04 <b>(-60.20%)</b></td><td>0.06 <b>(+229.01%)</b></td><td>921.10 <b>(+151.25%)</b></td><td>535.06 <b>(+85.58%)</b></td><td>456.20 <b>(+64.99%)</b></td><td>194.80 <b>(-22.27%)</b></td><td>324.83 <b>(+579.59%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>366.60 (n/a)</td><td>288.32 (n/a)</td><td>276.50 (n/a)</td><td>250.60 (n/a)</td><td>47.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (-8.63%)</td><td>0.10 <b>(+20.42%)</b></td><td>0.11 <b>(+50.44%)</b></td><td>0.05 (-9.03%)</td><td>0.03 (-8.07%)</td><td>638.60 (+9.93%)</td><td>360.00 (-16.07%)</td><td>294.70 <b>(-33.52%)</b></td><td>265.40 (+9.44%)</td><td>157.01 (+19.03%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>580.90 (n/a)</td><td>428.94 (n/a)</td><td>443.30 (n/a)</td><td>242.50 (n/a)</td><td>131.91 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.17 <b>(+21.59%)</b></td><td>0.09 (-19.47%)</td><td>0.07 <b>(-46.58%)</b></td><td>0.01 <b>(-77.49%)</b></td><td>0.06 <b>(+69.78%)</b></td><td>2508.50 <b>(+344.22%)</b></td><td>795.12 <b>(+134.78%)</b></td><td>485.50 <b>(+87.23%)</b></td><td>197.00 (-17.75%)</td><td>968.15 <b>(+589.11%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>564.70 (n/a)</td><td>338.66 (n/a)</td><td>259.30 (n/a)</td><td>239.50 (n/a)</td><td>140.49 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (+17.65%)</td><td>0.09 <b>(+32.80%)</b></td><td>0.07 (+3.82%)</td><td>0.06 <b>(+257.53%)</b></td><td>0.03 (-12.07%)</td><td>549.60 <b>(-72.03%)</b></td><td>400.46 <b>(-46.31%)</b></td><td>459.70 (-3.69%)</td><td>255.20 (-14.99%)</td><td>129.28 <b>(-81.35%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1965.00 (n/a)</td><td>745.92 (n/a)</td><td>477.30 (n/a)</td><td>300.20 (n/a)</td><td>693.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 <b>(-33.66%)</b></td><td>0.01 <b>(-22.57%)</b></td><td>0.01 <b>(-29.65%)</b></td><td>0.01 (-11.33%)</td><td>0.00 <b>(-53.54%)</b></td><td>512.40 (+12.76%)</td><td>402.64 <b>(+21.16%)</b></td><td>413.80 <b>(+42.15%)</b></td><td>299.00 <b>(+50.78%)</b></td><td>83.06 <b>(-27.00%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>454.40 (n/a)</td><td>332.32 (n/a)</td><td>291.10 (n/a)</td><td>198.30 (n/a)</td><td>113.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-2.55%)</td><td>0.01 (+15.69%)</td><td>0.01 (+4.46%)</td><td>0.01 <b>(+418.79%)</b></td><td>0.00 <b>(-59.51%)</b></td><td>364.40 <b>(-80.73%)</b></td><td>287.48 <b>(-51.79%)</b></td><td>274.50 (-4.29%)</td><td>229.80 (+2.64%)</td><td>51.33 <b>(-92.91%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1890.60 (n/a)</td><td>596.30 (n/a)</td><td>286.80 (n/a)</td><td>223.90 (n/a)</td><td>724.20 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-10.79%)</td><td>0.01 <b>(-21.11%)</b></td><td>0.01 <b>(-29.62%)</b></td><td>0.01 (+0.29%)</td><td>0.00 <b>(-20.55%)</b></td><td>496.50 (-0.28%)</td><td>404.26 <b>(+23.98%)</b></td><td>421.00 <b>(+42.09%)</b></td><td>263.90 (+12.06%)</td><td>87.92 (-16.05%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>497.90 (n/a)</td><td>326.08 (n/a)</td><td>296.30 (n/a)</td><td>235.50 (n/a)</td><td>104.73 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (+5.20%)</td><td>0.01 (+10.81%)</td><td>0.02 <b>(+51.25%)</b></td><td>0.00 <b>(-73.97%)</b></td><td>0.01 <b>(+49.51%)</b></td><td>1994.90 <b>(+284.08%)</b></td><td>604.84 <b>(+60.33%)</b></td><td>268.40 <b>(-33.89%)</b></td><td>217.20 (-4.95%)</td><td>777.55 <b>(+521.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.40 (n/a)</td><td>377.24 (n/a)</td><td>406.00 (n/a)</td><td>228.50 (n/a)</td><td>125.06 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 <b>(+100.90%)</b></td><td>0.01 <b>(+26.02%)</b></td><td>0.01 (-2.85%)</td><td>0.01 (-12.48%)</td><td>0.01 <b>(+631.50%)</b></td><td>562.40 (+14.26%)</td><td>408.24 (-7.37%)</td><td>459.50 (+2.93%)</td><td>196.70 <b>(-50.23%)</b></td><td>159.23 <b>(+326.71%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>492.20 (n/a)</td><td>440.74 (n/a)</td><td>446.40 (n/a)</td><td>395.20 (n/a)</td><td>37.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 <b>(+36.44%)</b></td><td>0.01 (+1.70%)</td><td>0.01 (-15.13%)</td><td>0.01 <b>(-23.73%)</b></td><td>0.00 <b>(+275.37%)</b></td><td>516.00 <b>(+31.13%)</b></td><td>374.18 (+8.71%)</td><td>406.70 (+17.85%)</td><td>225.50 <b>(-26.69%)</b></td><td>129.00 <b>(+259.04%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>393.50 (n/a)</td><td>344.20 (n/a)</td><td>345.10 (n/a)</td><td>307.60 (n/a)</td><td>35.93 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-6.29%)</td><td>0.01 (-4.93%)</td><td>0.01 (-16.54%)</td><td>0.01 (-9.97%)</td><td>0.00 <b>(-22.58%)</b></td><td>572.10 (+11.07%)</td><td>351.46 (+2.21%)</td><td>301.50 (+19.83%)</td><td>259.50 (+6.70%)</td><td>128.80 (-3.80%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.10 (n/a)</td><td>343.86 (n/a)</td><td>251.60 (n/a)</td><td>243.20 (n/a)</td><td>133.89 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-4.25%)</td><td>0.01 (-4.60%)</td><td>0.01 (-11.10%)</td><td>0.01 (+12.82%)</td><td>0.00 (-14.39%)</td><td>542.70 (-11.37%)</td><td>384.86 (+1.55%)</td><td>412.60 (+12.49%)</td><td>259.60 (+4.47%)</td><td>113.57 <b>(-21.90%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>612.30 (n/a)</td><td>378.98 (n/a)</td><td>366.80 (n/a)</td><td>248.50 (n/a)</td><td>145.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (-16.35%)</td><td>0.01 (-11.08%)</td><td>0.01 (-9.08%)</td><td>0.01 (+4.08%)</td><td>0.00 <b>(-32.21%)</b></td><td>573.80 (-3.92%)</td><td>443.18 (+6.49%)</td><td>505.60 (+9.98%)</td><td>291.40 (+19.52%)</td><td>122.90 (-19.95%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>597.20 (n/a)</td><td>416.18 (n/a)</td><td>459.70 (n/a)</td><td>243.80 (n/a)</td><td>153.54 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-1.91%)</td><td>0.01 <b>(+35.19%)</b></td><td>0.01 <b>(+51.95%)</b></td><td>0.01 <b>(+103.39%)</b></td><td>0.00 <b>(-28.58%)</b></td><td>545.00 <b>(-50.83%)</b></td><td>376.94 <b>(-36.67%)</b></td><td>346.10 <b>(-34.18%)</b></td><td>253.20 (+1.93%)</td><td>115.76 <b>(-63.52%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1108.50 (n/a)</td><td>595.18 (n/a)</td><td>525.80 (n/a)</td><td>248.40 (n/a)</td><td>317.31 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 <b>(-40.63%)</b></td><td>0.01 <b>(-20.94%)</b></td><td>0.01 <b>(+25.14%)</b></td><td>0.00 <b>(-46.11%)</b></td><td>0.00 <b>(-42.99%)</b></td><td>1147.90 <b>(+85.56%)</b></td><td>532.02 <b>(+29.74%)</b></td><td>380.50 <b>(-20.10%)</b></td><td>288.70 <b>(+68.44%)</b></td><td>351.89 <b>(+100.14%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.60 (n/a)</td><td>410.06 (n/a)</td><td>476.20 (n/a)</td><td>171.40 (n/a)</td><td>175.82 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (+19.64%)</td><td>0.01 (-7.58%)</td><td>0.01 (-16.43%)</td><td>0.01 (+0.29%)</td><td>0.00 <b>(+45.51%)</b></td><td>653.70 (-0.29%)</td><td>518.12 (+13.37%)</td><td>560.30 (+19.67%)</td><td>249.20 (-16.43%)</td><td>155.51 (+13.33%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>655.60 (n/a)</td><td>457.02 (n/a)</td><td>468.20 (n/a)</td><td>298.20 (n/a)</td><td>137.22 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (-5.37%)</td><td>0.03 (-1.86%)</td><td>0.03 <b>(+31.84%)</b></td><td>0.02 (+1.21%)</td><td>0.01 <b>(-22.57%)</b></td><td>459.50 (-1.20%)</td><td>348.14 (-1.14%)</td><td>306.60 <b>(-24.17%)</b></td><td>236.80 (+5.67%)</td><td>99.21 (-12.15%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.10 (n/a)</td><td>352.16 (n/a)</td><td>404.30 (n/a)</td><td>224.10 (n/a)</td><td>112.93 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(-25.56%)</b></td><td>0.02 (-6.38%)</td><td>0.03 <b>(+42.24%)</b></td><td>0.01 (+11.92%)</td><td>0.01 <b>(-37.98%)</b></td><td>628.90 (-10.65%)</td><td>395.44 (-3.42%)</td><td>300.50 <b>(-29.69%)</b></td><td>262.80 <b>(+34.36%)</b></td><td>158.75 <b>(-22.29%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>703.90 (n/a)</td><td>409.46 (n/a)</td><td>427.40 (n/a)</td><td>195.60 (n/a)</td><td>204.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (+5.21%)</td><td>0.02 (-1.74%)</td><td>0.02 (-12.36%)</td><td>0.01 <b>(-24.75%)</b></td><td>0.01 <b>(+40.00%)</b></td><td>612.40 <b>(+32.87%)</b></td><td>396.50 (+9.27%)</td><td>441.70 (+14.10%)</td><td>242.00 (-4.95%)</td><td>156.98 <b>(+62.53%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>460.90 (n/a)</td><td>362.86 (n/a)</td><td>387.10 (n/a)</td><td>254.60 (n/a)</td><td>96.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (-8.95%)</td><td>0.03 (-11.91%)</td><td>0.03 (-11.18%)</td><td>0.01 (-17.16%)</td><td>0.01 (-5.47%)</td><td>647.80 <b>(+20.72%)</b></td><td>357.64 (+15.56%)</td><td>294.20 (+12.59%)</td><td>266.50 (+9.85%)</td><td>162.75 <b>(+27.87%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.60 (n/a)</td><td>309.48 (n/a)</td><td>261.30 (n/a)</td><td>242.60 (n/a)</td><td>127.28 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (-6.37%)</td><td>0.02 (+3.90%)</td><td>0.03 <b>(+35.43%)</b></td><td>0.01 <b>(-23.09%)</b></td><td>0.01 (+3.76%)</td><td>597.80 <b>(+30.04%)</b></td><td>359.96 (-0.92%)</td><td>293.80 <b>(-26.16%)</b></td><td>265.00 (+6.77%)</td><td>140.21 <b>(+44.37%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>459.70 (n/a)</td><td>363.30 (n/a)</td><td>397.90 (n/a)</td><td>248.20 (n/a)</td><td>97.12 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (-10.95%)</td><td>0.02 (-2.50%)</td><td>0.02 (+19.15%)</td><td>0.01 <b>(-32.31%)</b></td><td>0.01 (-6.86%)</td><td>759.90 <b>(+47.73%)</b></td><td>398.72 (+7.77%)</td><td>329.00 (-16.07%)</td><td>264.80 (+12.30%)</td><td>204.06 <b>(+72.30%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.40 (n/a)</td><td>369.96 (n/a)</td><td>392.00 (n/a)</td><td>235.80 (n/a)</td><td>118.43 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 <b>(+25.40%)</b></td><td>0.03 <b>(+55.52%)</b></td><td>0.03 <b>(+56.59%)</b></td><td>0.02 <b>(+259.49%)</b></td><td>0.01 (-11.99%)</td><td>544.90 <b>(-72.18%)</b></td><td>335.14 <b>(-54.20%)</b></td><td>302.40 <b>(-36.14%)</b></td><td>224.80 <b>(-20.26%)</b></td><td>123.91 <b>(-82.10%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1958.90 (n/a)</td><td>731.76 (n/a)</td><td>473.50 (n/a)</td><td>281.90 (n/a)</td><td>692.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 <b>(+65.46%)</b></td><td>0.03 (+12.44%)</td><td>0.02 (-3.69%)</td><td>0.00 <b>(-68.40%)</b></td><td>0.02 <b>(+109.40%)</b></td><td>1948.80 <b>(+216.52%)</b></td><td>652.16 <b>(+56.82%)</b></td><td>422.60 (+3.83%)</td><td>143.40 <b>(-39.54%)</b></td><td>735.74 <b>(+339.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.70 (n/a)</td><td>415.86 (n/a)</td><td>407.00 (n/a)</td><td>237.20 (n/a)</td><td>167.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(+34.24%)</b></td><td>0.02 <b>(+46.65%)</b></td><td>0.02 <b>(+28.68%)</b></td><td>0.02 <b>(+381.10%)</b></td><td>0.01 (-10.07%)</td><td>519.90 <b>(-79.22%)</b></td><td>409.42 <b>(-54.08%)</b></td><td>438.70 <b>(-22.29%)</b></td><td>275.80 <b>(-25.50%)</b></td><td>116.45 <b>(-87.14%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2501.40 (n/a)</td><td>891.62 (n/a)</td><td>564.50 (n/a)</td><td>370.20 (n/a)</td><td>905.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(-25.40%)</b></td><td>0.02 (-17.02%)</td><td>0.02 <b>(-28.95%)</b></td><td>0.01 (-16.51%)</td><td>0.01 <b>(-28.42%)</b></td><td>614.60 (+19.78%)</td><td>423.30 (+18.00%)</td><td>434.60 <b>(+40.74%)</b></td><td>285.80 <b>(+34.05%)</b></td><td>132.82 (+7.68%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.10 (n/a)</td><td>358.74 (n/a)</td><td>308.80 (n/a)</td><td>213.20 (n/a)</td><td>123.35 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (-17.20%)</td><td>0.02 (+16.42%)</td><td>0.03 <b>(+68.56%)</b></td><td>0.01 <b>(-31.85%)</b></td><td>0.01 (+0.27%)</td><td>1020.40 <b>(+46.74%)</b></td><td>472.36 (-3.56%)</td><td>288.70 <b>(-40.68%)</b></td><td>263.20 <b>(+20.79%)</b></td><td>324.79 <b>(+84.48%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>695.40 (n/a)</td><td>489.80 (n/a)</td><td>486.70 (n/a)</td><td>217.90 (n/a)</td><td>176.06 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (+8.82%)</td><td>0.02 (+16.83%)</td><td>0.03 <b>(+29.21%)</b></td><td>0.01 (-0.93%)</td><td>0.01 (+19.78%)</td><td>553.30 (+0.93%)</td><td>362.64 (-12.92%)</td><td>305.00 <b>(-22.61%)</b></td><td>257.50 (-8.10%)</td><td>125.14 (+6.31%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.20 (n/a)</td><td>416.44 (n/a)</td><td>394.10 (n/a)</td><td>280.20 (n/a)</td><td>117.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (+18.45%)</td><td>0.05 <b>(+30.06%)</b></td><td>0.05 <b>(+40.90%)</b></td><td>0.03 <b>(+29.29%)</b></td><td>0.01 <b>(+25.05%)</b></td><td>505.90 <b>(-22.66%)</b></td><td>357.74 <b>(-22.83%)</b></td><td>330.90 <b>(-29.04%)</b></td><td>250.30 (-15.58%)</td><td>107.22 (-17.35%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>654.10 (n/a)</td><td>463.58 (n/a)</td><td>466.30 (n/a)</td><td>296.50 (n/a)</td><td>129.73 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 <b>(+34.84%)</b></td><td>0.06 <b>(+41.22%)</b></td><td>0.07 <b>(+67.59%)</b></td><td>0.04 (+5.95%)</td><td>0.01 <b>(+113.15%)</b></td><td>424.00 (-5.63%)</td><td>278.50 <b>(-26.54%)</b></td><td>236.20 <b>(-40.32%)</b></td><td>231.50 <b>(-25.85%)</b></td><td>82.81 <b>(+52.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>449.30 (n/a)</td><td>379.12 (n/a)</td><td>395.80 (n/a)</td><td>312.20 (n/a)</td><td>54.48 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (+17.12%)</td><td>0.04 (-1.72%)</td><td>0.03 (-10.05%)</td><td>0.02 <b>(-42.09%)</b></td><td>0.02 <b>(+71.18%)</b></td><td>1007.70 <b>(+72.67%)</b></td><td>517.82 <b>(+22.06%)</b></td><td>484.80 (+11.17%)</td><td>243.80 (-14.64%)</td><td>305.04 <b>(+149.71%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>583.60 (n/a)</td><td>424.24 (n/a)</td><td>436.10 (n/a)</td><td>285.60 (n/a)</td><td>122.15 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (-17.81%)</td><td>0.05 (-2.56%)</td><td>0.03 <b>(-32.52%)</b></td><td>0.03 <b>(+106.55%)</b></td><td>0.02 <b>(-26.13%)</b></td><td>503.10 <b>(-51.58%)</b></td><td>396.76 (-14.82%)</td><td>484.60 <b>(+48.20%)</b></td><td>239.80 <b>(+21.66%)</b></td><td>136.33 <b>(-59.07%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1039.10 (n/a)</td><td>465.78 (n/a)</td><td>327.00 (n/a)</td><td>197.10 (n/a)</td><td>333.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (+18.32%)</td><td>0.05 <b>(+46.89%)</b></td><td>0.06 <b>(+74.57%)</b></td><td>0.03 (+17.01%)</td><td>0.02 (+19.74%)</td><td>598.80 (-14.54%)</td><td>334.42 <b>(-31.13%)</b></td><td>280.00 <b>(-42.71%)</b></td><td>247.60 (-15.47%)</td><td>148.63 (-8.00%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>700.70 (n/a)</td><td>485.60 (n/a)</td><td>488.70 (n/a)</td><td>292.90 (n/a)</td><td>161.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 <b>(-27.27%)</b></td><td>0.05 (+2.09%)</td><td>0.06 (+5.41%)</td><td>0.03 <b>(+26.05%)</b></td><td>0.01 <b>(-48.91%)</b></td><td>489.90 <b>(-20.66%)</b></td><td>315.76 (-12.85%)</td><td>280.40 (-5.14%)</td><td>249.10 <b>(+37.47%)</b></td><td>98.59 <b>(-42.41%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>617.50 (n/a)</td><td>362.32 (n/a)</td><td>295.60 (n/a)</td><td>181.20 (n/a)</td><td>171.20 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 <b>(+67.87%)</b></td><td>0.05 <b>(+61.28%)</b></td><td>0.06 <b>(+86.34%)</b></td><td>0.04 <b>(+38.34%)</b></td><td>0.01 <b>(+153.11%)</b></td><td>460.40 <b>(-27.71%)</b></td><td>337.94 <b>(-35.68%)</b></td><td>283.60 <b>(-46.34%)</b></td><td>254.30 <b>(-40.44%)</b></td><td>93.85 (+10.89%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>636.90 (n/a)</td><td>525.38 (n/a)</td><td>528.50 (n/a)</td><td>427.00 (n/a)</td><td>84.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (+14.01%)</td><td>0.06 <b>(+31.14%)</b></td><td>0.07 <b>(+103.34%)</b></td><td>0.03 (+19.70%)</td><td>0.02 <b>(+24.88%)</b></td><td>479.80 (-16.45%)</td><td>329.12 <b>(-22.52%)</b></td><td>240.10 <b>(-50.83%)</b></td><td>231.10 (-12.30%)</td><td>126.67 (-6.35%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>574.30 (n/a)</td><td>424.78 (n/a)</td><td>488.30 (n/a)</td><td>263.50 (n/a)</td><td>135.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 <b>(+43.56%)</b></td><td>0.04 <b>(+43.19%)</b></td><td>0.03 <b>(+23.67%)</b></td><td>0.03 <b>(+284.71%)</b></td><td>0.02 (+15.56%)</td><td>632.60 <b>(-74.00%)</b></td><td>467.36 <b>(-48.58%)</b></td><td>493.00 (-19.14%)</td><td>253.00 <b>(-30.34%)</b></td><td>160.50 <b>(-81.33%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2433.50 (n/a)</td><td>908.96 (n/a)</td><td>609.70 (n/a)</td><td>363.20 (n/a)</td><td>859.63 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 <b>(+62.95%)</b></td><td>0.05 <b>(+36.12%)</b></td><td>0.06 <b>(+56.96%)</b></td><td>0.03 (-19.04%)</td><td>0.02 <b>(+314.94%)</b></td><td>638.20 <b>(+23.51%)</b></td><td>368.50 (-15.78%)</td><td>282.60 <b>(-36.28%)</b></td><td>227.70 <b>(-38.63%)</b></td><td>173.03 <b>(+213.31%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>516.70 (n/a)</td><td>437.56 (n/a)</td><td>443.50 (n/a)</td><td>371.00 (n/a)</td><td>55.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.05 (+0.77%)</td><td>0.03 (-16.12%)</td><td>0.03 <b>(-26.56%)</b></td><td>0.01 <b>(-73.03%)</b></td><td>0.02 <b>(+65.52%)</b></td><td>2395.40 <b>(+270.80%)</b></td><td>826.74 <b>(+91.76%)</b></td><td>486.50 <b>(+36.16%)</b></td><td>306.10 (-0.75%)</td><td>887.30 <b>(+519.64%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>646.00 (n/a)</td><td>431.14 (n/a)</td><td>357.30 (n/a)</td><td>308.40 (n/a)</td><td>143.20 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 <b>(+24.18%)</b></td><td>0.05 <b>(+51.90%)</b></td><td>0.05 <b>(+66.24%)</b></td><td>0.02 <b>(+203.47%)</b></td><td>0.02 (+2.80%)</td><td>671.70 <b>(-67.05%)</b></td><td>379.60 <b>(-51.58%)</b></td><td>305.20 <b>(-39.84%)</b></td><td>190.40 (-19.49%)</td><td>184.43 <b>(-74.33%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2038.60 (n/a)</td><td>784.02 (n/a)</td><td>507.30 (n/a)</td><td>236.50 (n/a)</td><td>718.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (-0.59%)</td><td>0.12 <b>(+40.98%)</b></td><td>0.14 <b>(+89.30%)</b></td><td>0.07 (+7.61%)</td><td>0.03 (-2.77%)</td><td>499.60 (-7.07%)</td><td>297.78 <b>(-29.21%)</b></td><td>240.80 <b>(-47.18%)</b></td><td>233.80 (+0.60%)</td><td>114.02 (-0.91%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>537.60 (n/a)</td><td>420.64 (n/a)</td><td>455.90 (n/a)</td><td>232.40 (n/a)</td><td>115.06 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (-3.86%)</td><td>0.11 (+6.48%)</td><td>0.12 (-2.66%)</td><td>0.07 (+10.97%)</td><td>0.03 <b>(-22.53%)</b></td><td>502.00 (-9.89%)</td><td>318.94 (-10.33%)</td><td>275.80 (+2.76%)</td><td>243.10 (+4.02%)</td><td>105.75 <b>(-25.21%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>557.10 (n/a)</td><td>355.70 (n/a)</td><td>268.40 (n/a)</td><td>233.70 (n/a)</td><td>141.40 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 <b>(-24.18%)</b></td><td>0.06 (-19.95%)</td><td>0.07 (+2.37%)</td><td>0.01 <b>(-76.63%)</b></td><td>0.03 <b>(+64.53%)</b></td><td>2428.30 <b>(+327.82%)</b></td><td>863.00 <b>(+85.82%)</b></td><td>467.50 (-2.30%)</td><td>449.80 <b>(+31.87%)</b></td><td>875.24 <b>(+871.49%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>567.60 (n/a)</td><td>464.42 (n/a)</td><td>478.50 (n/a)</td><td>341.10 (n/a)</td><td>90.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (-14.20%)</td><td>0.09 (-7.19%)</td><td>0.07 (+1.74%)</td><td>0.06 (+4.61%)</td><td>0.03 <b>(-26.33%)</b></td><td>516.50 (-4.40%)</td><td>392.12 (+2.10%)</td><td>445.40 (-1.70%)</td><td>255.10 (+16.54%)</td><td>123.95 (-16.86%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>540.30 (n/a)</td><td>384.04 (n/a)</td><td>453.10 (n/a)</td><td>218.90 (n/a)</td><td>149.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 (-15.36%)</td><td>0.10 (-1.23%)</td><td>0.09 <b>(-20.92%)</b></td><td>0.06 (+8.98%)</td><td>0.04 <b>(-20.19%)</b></td><td>580.80 (-8.23%)</td><td>369.44 (-6.84%)</td><td>376.60 <b>(+26.46%)</b></td><td>209.60 (+18.15%)</td><td>154.34 <b>(-25.13%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>632.90 (n/a)</td><td>396.58 (n/a)</td><td>297.80 (n/a)</td><td>177.40 (n/a)</td><td>206.15 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 (-13.93%)</td><td>0.11 <b>(+20.03%)</b></td><td>0.11 <b>(+54.33%)</b></td><td>0.07 (+19.66%)</td><td>0.04 <b>(-29.53%)</b></td><td>456.10 (-16.43%)</td><td>328.72 <b>(-22.94%)</b></td><td>297.60 <b>(-35.21%)</b></td><td>200.20 (+16.19%)</td><td>114.47 <b>(-22.59%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>545.80 (n/a)</td><td>426.60 (n/a)</td><td>459.30 (n/a)</td><td>172.30 (n/a)</td><td>147.88 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (-8.66%)</td><td>0.10 (-13.55%)</td><td>0.11 (-10.47%)</td><td>0.06 (-17.49%)</td><td>0.03 (-6.19%)</td><td>569.20 <b>(+21.21%)</b></td><td>380.26 (+17.64%)</td><td>305.90 (+11.72%)</td><td>233.20 (+9.48%)</td><td>146.72 <b>(+26.94%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>469.60 (n/a)</td><td>323.24 (n/a)</td><td>273.80 (n/a)</td><td>213.00 (n/a)</td><td>115.59 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 <b>(-32.87%)</b></td><td>0.10 (+3.73%)</td><td>0.11 <b>(+48.46%)</b></td><td>0.07 <b>(+20.25%)</b></td><td>0.03 <b>(-48.85%)</b></td><td>471.70 (-16.85%)</td><td>348.88 (-13.94%)</td><td>299.70 <b>(-32.64%)</b></td><td>237.30 <b>(+48.96%)</b></td><td>112.71 <b>(-25.24%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>567.30 (n/a)</td><td>405.38 (n/a)</td><td>444.90 (n/a)</td><td>159.30 (n/a)</td><td>150.77 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 <b>(+64.33%)</b></td><td>0.07 (+8.63%)</td><td>0.07 (+0.53%)</td><td>0.01 <b>(-67.23%)</b></td><td>0.05 <b>(+167.70%)</b></td><td>2417.10 <b>(+205.15%)</b></td><td>817.12 <b>(+57.44%)</b></td><td>492.90 (-0.52%)</td><td>220.80 <b>(-39.16%)</b></td><td>902.19 <b>(+449.04%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>792.10 (n/a)</td><td>519.02 (n/a)</td><td>495.50 (n/a)</td><td>362.90 (n/a)</td><td>164.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (+1.40%)</td><td>0.09 (+0.35%)</td><td>0.07 <b>(-20.64%)</b></td><td>0.05 <b>(+318.01%)</b></td><td>0.04 <b>(-22.15%)</b></td><td>604.10 <b>(-76.08%)</b></td><td>440.68 <b>(-43.30%)</b></td><td>500.70 <b>(+26.03%)</b></td><td>239.00 (-1.40%)</td><td>172.77 <b>(-82.40%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2525.10 (n/a)</td><td>777.24 (n/a)</td><td>397.30 (n/a)</td><td>242.40 (n/a)</td><td>981.86 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (-19.35%)</td><td>0.08 (-0.27%)</td><td>0.09 <b>(+35.44%)</b></td><td>0.05 (+3.91%)</td><td>0.02 (-19.22%)</td><td>639.50 (-3.76%)</td><td>460.12 (-1.35%)</td><td>366.00 <b>(-26.17%)</b></td><td>356.20 <b>(+23.98%)</b></td><td>138.61 (-4.27%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>664.50 (n/a)</td><td>466.44 (n/a)</td><td>495.70 (n/a)</td><td>287.30 (n/a)</td><td>144.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (-17.00%)</td><td>0.07 <b>(-24.55%)</b></td><td>0.06 (-17.92%)</td><td>0.05 <b>(-29.98%)</b></td><td>0.02 (-19.41%)</td><td>696.00 <b>(+42.83%)</b></td><td>530.94 <b>(+32.55%)</b></td><td>562.70 <b>(+21.85%)</b></td><td>319.00 <b>(+20.47%)</b></td><td>137.39 <b>(+27.17%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>487.30 (n/a)</td><td>400.56 (n/a)</td><td>461.80 (n/a)</td><td>264.80 (n/a)</td><td>108.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (+3.29%)</td><td>0.01 (-1.94%)</td><td>0.01 (-4.01%)</td><td>0.01 <b>(-29.16%)</b></td><td>0.01 <b>(+37.47%)</b></td><td>751.20 <b>(+41.15%)</b></td><td>448.66 (+13.97%)</td><td>470.50 (+4.16%)</td><td>235.50 (-3.17%)</td><td>217.59 <b>(+73.62%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.20 (n/a)</td><td>393.66 (n/a)</td><td>451.70 (n/a)</td><td>243.20 (n/a)</td><td>125.33 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(+36.78%)</b></td><td>0.02 <b>(+29.16%)</b></td><td>0.02 (+10.14%)</td><td>0.01 (+13.29%)</td><td>0.01 <b>(+29.06%)</b></td><td>445.90 (-11.72%)</td><td>281.10 <b>(-22.19%)</b></td><td>258.60 (-9.20%)</td><td>193.80 <b>(-26.87%)</b></td><td>98.99 (-14.93%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>505.10 (n/a)</td><td>361.26 (n/a)</td><td>284.80 (n/a)</td><td>265.00 (n/a)</td><td>116.36 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 <b>(-22.25%)</b></td><td>0.01 (+13.72%)</td><td>0.02 <b>(+104.11%)</b></td><td>0.01 <b>(+77.67%)</b></td><td>0.00 <b>(-37.20%)</b></td><td>578.40 <b>(-43.71%)</b></td><td>369.70 <b>(-28.85%)</b></td><td>267.90 <b>(-51.01%)</b></td><td>253.20 <b>(+28.66%)</b></td><td>150.29 <b>(-54.00%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1027.60 (n/a)</td><td>519.60 (n/a)</td><td>546.90 (n/a)</td><td>196.80 (n/a)</td><td>326.69 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-6.90%)</td><td>0.01 (-0.04%)</td><td>0.01 (-12.66%)</td><td>0.01 <b>(+233.39%)</b></td><td>0.01 <b>(-25.24%)</b></td><td>587.00 <b>(-70.00%)</b></td><td>434.56 <b>(-35.41%)</b></td><td>525.50 (+14.51%)</td><td>236.60 (+7.40%)</td><td>173.97 <b>(-76.12%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1956.90 (n/a)</td><td>672.84 (n/a)</td><td>458.90 (n/a)</td><td>220.30 (n/a)</td><td>728.64 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-10.93%)</td><td>0.01 (-19.43%)</td><td>0.01 <b>(-43.85%)</b></td><td>0.01 <b>(+55.84%)</b></td><td>0.01 (-17.23%)</td><td>511.40 <b>(-35.83%)</b></td><td>372.76 (+8.53%)</td><td>435.00 <b>(+78.13%)</b></td><td>205.90 (+12.27%)</td><td>142.10 <b>(-44.68%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>796.90 (n/a)</td><td>343.46 (n/a)</td><td>244.20 (n/a)</td><td>183.40 (n/a)</td><td>256.89 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 <b>(-22.37%)</b></td><td>0.01 <b>(-39.08%)</b></td><td>0.01 <b>(-49.09%)</b></td><td>0.00 <b>(-54.27%)</b></td><td>0.01 (-2.76%)</td><td>1069.30 <b>(+118.67%)</b></td><td>618.04 <b>(+82.95%)</b></td><td>578.80 <b>(+96.40%)</b></td><td>274.20 <b>(+28.79%)</b></td><td>295.39 <b>(+161.49%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>489.00 (n/a)</td><td>337.82 (n/a)</td><td>294.70 (n/a)</td><td>212.90 (n/a)</td><td>112.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 <b>(-22.89%)</b></td><td>0.01 (-13.18%)</td><td>0.01 <b>(+21.54%)</b></td><td>0.01 (-5.94%)</td><td>0.00 <b>(-42.66%)</b></td><td>598.80 (+6.32%)</td><td>430.76 (+3.88%)</td><td>431.00 (-17.73%)</td><td>262.30 <b>(+29.66%)</b></td><td>133.60 <b>(-23.77%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.20 (n/a)</td><td>414.66 (n/a)</td><td>523.90 (n/a)</td><td>202.30 (n/a)</td><td>175.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-10.51%)</td><td>0.01 (+1.97%)</td><td>0.01 <b>(+20.66%)</b></td><td>0.01 (-0.19%)</td><td>0.00 (-16.75%)</td><td>554.90 (+0.20%)</td><td>383.68 (-3.17%)</td><td>347.70 (-17.12%)</td><td>270.80 (+11.76%)</td><td>111.59 (-2.54%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.80 (n/a)</td><td>396.24 (n/a)</td><td>419.50 (n/a)</td><td>242.30 (n/a)</td><td>114.49 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.02 (-10.40%)</td><td>0.01 (+2.61%)</td><td>0.01 (+15.14%)</td><td>0.01 <b>(+33.05%)</b></td><td>0.00 (-17.51%)</td><td>521.00 <b>(-24.84%)</b></td><td>354.22 (-8.66%)</td><td>274.90 (-13.17%)</td><td>246.80 (+11.57%)</td><td>131.55 <b>(-31.44%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>693.20 (n/a)</td><td>387.80 (n/a)</td><td>316.60 (n/a)</td><td>221.20 (n/a)</td><td>191.88 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 <b>(-35.89%)</b></td><td>0.01 (-19.11%)</td><td>0.01 (-15.51%)</td><td>0.01 (+0.07%)</td><td>0.00 <b>(-71.58%)</b></td><td>544.60 (-0.07%)</td><td>490.32 (+15.89%)</td><td>505.20 (+18.37%)</td><td>411.80 <b>(+55.98%)</b></td><td>51.33 <b>(-57.40%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.00 (n/a)</td><td>423.10 (n/a)</td><td>426.80 (n/a)</td><td>264.00 (n/a)</td><td>120.48 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.01 (-12.36%)</td><td>0.01 (+7.74%)</td><td>0.01 <b>(+27.99%)</b></td><td>0.01 <b>(+21.00%)</b></td><td>0.00 <b>(-37.41%)</b></td><td>531.90 (-17.36%)</td><td>408.54 (-13.39%)</td><td>381.30 <b>(-21.88%)</b></td><td>290.90 (+14.12%)</td><td>94.95 <b>(-40.70%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>643.60 (n/a)</td><td>471.72 (n/a)</td><td>488.10 (n/a)</td><td>254.90 (n/a)</td><td>160.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (-1.43%)</td><td>0.03 <b>(+25.52%)</b></td><td>0.03 <b>(+61.30%)</b></td><td>0.02 (+11.49%)</td><td>0.01 (-17.41%)</td><td>530.50 (-10.30%)</td><td>317.60 <b>(-24.49%)</b></td><td>268.30 <b>(-38.01%)</b></td><td>235.60 (+1.42%)</td><td>123.53 <b>(-25.85%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.40 (n/a)</td><td>420.60 (n/a)</td><td>432.80 (n/a)</td><td>232.30 (n/a)</td><td>166.61 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 <b>(-38.72%)</b></td><td>0.03 <b>(-40.04%)</b></td><td>0.02 <b>(-52.06%)</b></td><td>0.02 (-9.88%)</td><td>0.01 <b>(-58.77%)</b></td><td>521.20 (+10.96%)</td><td>460.26 <b>(+48.81%)</b></td><td>493.40 <b>(+108.63%)</b></td><td>290.70 <b>(+63.13%)</b></td><td>96.50 <b>(-32.03%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>469.70 (n/a)</td><td>309.30 (n/a)</td><td>236.50 (n/a)</td><td>178.20 (n/a)</td><td>141.98 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(-25.47%)</b></td><td>0.02 (+13.56%)</td><td>0.02 <b>(+48.03%)</b></td><td>0.01 (+2.07%)</td><td>0.01 <b>(-45.90%)</b></td><td>603.40 (-2.03%)</td><td>385.90 <b>(-20.04%)</b></td><td>373.50 <b>(-32.46%)</b></td><td>270.20 <b>(+34.16%)</b></td><td>129.52 <b>(-22.74%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.90 (n/a)</td><td>482.60 (n/a)</td><td>553.00 (n/a)</td><td>201.40 (n/a)</td><td>167.63 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 <b>(-21.13%)</b></td><td>0.03 (-13.93%)</td><td>0.02 (-18.80%)</td><td>0.02 (-8.51%)</td><td>0.01 (-18.54%)</td><td>527.30 (+9.28%)</td><td>412.64 (+15.77%)</td><td>433.90 <b>(+23.13%)</b></td><td>281.50 <b>(+26.80%)</b></td><td>115.80 (+14.01%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>482.50 (n/a)</td><td>356.44 (n/a)</td><td>352.40 (n/a)</td><td>222.00 (n/a)</td><td>101.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (+12.16%)</td><td>0.02 (+1.95%)</td><td>0.03 (-2.27%)</td><td>0.01 (+19.93%)</td><td>0.01 (+18.65%)</td><td>557.70 (-16.61%)</td><td>372.94 (-1.58%)</td><td>308.90 (+2.32%)</td><td>231.00 (-10.85%)</td><td>143.90 (-13.70%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>668.80 (n/a)</td><td>378.94 (n/a)</td><td>301.90 (n/a)</td><td>259.10 (n/a)</td><td>166.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 <b>(-37.08%)</b></td><td>0.03 (-19.99%)</td><td>0.02 (-16.67%)</td><td>0.02 <b>(-25.56%)</b></td><td>0.01 <b>(-32.10%)</b></td><td>636.30 <b>(+34.33%)</b></td><td>427.56 <b>(+23.07%)</b></td><td>504.30 <b>(+20.01%)</b></td><td>233.70 <b>(+58.98%)</b></td><td>182.80 <b>(+31.13%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>473.70 (n/a)</td><td>347.40 (n/a)</td><td>420.20 (n/a)</td><td>147.00 (n/a)</td><td>139.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 <b>(+99.20%)</b></td><td>0.03 <b>(+79.45%)</b></td><td>0.03 <b>(+84.14%)</b></td><td>0.02 <b>(+84.93%)</b></td><td>0.01 <b>(+104.42%)</b></td><td>532.40 <b>(-45.93%)</b></td><td>310.20 <b>(-43.85%)</b></td><td>257.40 <b>(-45.70%)</b></td><td>194.70 <b>(-49.81%)</b></td><td>132.20 <b>(-45.91%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>984.70 (n/a)</td><td>552.44 (n/a)</td><td>474.00 (n/a)</td><td>387.90 (n/a)</td><td>244.40 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 (+3.27%)</td><td>0.02 (+6.91%)</td><td>0.02 (-4.32%)</td><td>0.02 (+9.87%)</td><td>0.01 (+15.23%)</td><td>577.30 (-8.99%)</td><td>437.12 (-4.83%)</td><td>482.60 (+4.50%)</td><td>269.60 (-3.16%)</td><td>135.77 (+5.51%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.30 (n/a)</td><td>459.32 (n/a)</td><td>461.80 (n/a)</td><td>278.40 (n/a)</td><td>128.67 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 <b>(+44.57%)</b></td><td>0.03 <b>(+40.52%)</b></td><td>0.03 <b>(+91.78%)</b></td><td>0.02 (+7.41%)</td><td>0.01 <b>(+53.57%)</b></td><td>545.20 (-6.90%)</td><td>341.18 <b>(-25.33%)</b></td><td>272.70 <b>(-47.85%)</b></td><td>206.90 <b>(-30.85%)</b></td><td>149.17 (+2.41%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.60 (n/a)</td><td>456.92 (n/a)</td><td>522.90 (n/a)</td><td>299.20 (n/a)</td><td>145.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 (+1.76%)</td><td>0.03 (+9.01%)</td><td>0.03 <b>(+20.36%)</b></td><td>0.02 (+3.78%)</td><td>0.01 (+0.31%)</td><td>551.40 (-3.65%)</td><td>386.62 (-8.51%)</td><td>331.40 (-16.90%)</td><td>219.90 (-1.74%)</td><td>143.86 (-3.51%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.30 (n/a)</td><td>422.58 (n/a)</td><td>398.80 (n/a)</td><td>223.80 (n/a)</td><td>149.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.04 <b>(+88.78%)</b></td><td>0.02 <b>(+49.34%)</b></td><td>0.02 <b>(+32.30%)</b></td><td>0.02 <b>(+36.36%)</b></td><td>0.01 <b>(+199.61%)</b></td><td>447.20 <b>(-26.66%)</b></td><td>357.66 <b>(-29.54%)</b></td><td>390.50 <b>(-24.41%)</b></td><td>224.60 <b>(-47.03%)</b></td><td>97.80 <b>(+21.94%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.80 (n/a)</td><td>507.64 (n/a)</td><td>516.60 (n/a)</td><td>424.00 (n/a)</td><td>80.20 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 <b>(+38.76%)</b></td><td>0.04 <b>(+24.86%)</b></td><td>0.04 <b>(+21.77%)</b></td><td>0.02 (-16.18%)</td><td>0.01 <b>(+154.69%)</b></td><td>680.30 (+19.29%)</td><td>409.02 (-12.57%)</td><td>386.20 (-17.88%)</td><td>272.00 <b>(-27.93%)</b></td><td>165.15 <b>(+116.38%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>570.30 (n/a)</td><td>467.84 (n/a)</td><td>470.30 (n/a)</td><td>377.40 (n/a)</td><td>76.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (+17.49%)</td><td>0.07 (+17.54%)</td><td>0.08 <b>(+43.99%)</b></td><td>0.05 (-12.27%)</td><td>0.02 <b>(+129.58%)</b></td><td>535.80 (+14.00%)</td><td>368.28 (-8.22%)</td><td>290.10 <b>(-30.56%)</b></td><td>264.60 (-14.86%)</td><td>131.83 <b>(+124.43%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>470.00 (n/a)</td><td>401.28 (n/a)</td><td>417.80 (n/a)</td><td>310.80 (n/a)</td><td>58.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (-7.52%)</td><td>0.05 <b>(+57.56%)</b></td><td>0.05 <b>(+102.72%)</b></td><td>0.03 <b>(+407.89%)</b></td><td>0.01 <b>(-46.53%)</b></td><td>487.50 <b>(-80.31%)</b></td><td>359.26 <b>(-68.51%)</b></td><td>300.30 <b>(-50.67%)</b></td><td>263.90 (+8.16%)</td><td>111.17 <b>(-89.25%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2476.00 (n/a)</td><td>1141.00 (n/a)</td><td>608.80 (n/a)</td><td>244.00 (n/a)</td><td>1034.37 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (-6.63%)</td><td>0.06 (+15.06%)</td><td>0.06 <b>(+35.18%)</b></td><td>0.03 (-7.26%)</td><td>0.02 (-4.57%)</td><td>647.70 (+7.82%)</td><td>395.28 (-11.93%)</td><td>342.30 <b>(-26.02%)</b></td><td>257.10 (+7.13%)</td><td>157.54 <b>(+20.50%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>600.70 (n/a)</td><td>448.82 (n/a)</td><td>462.70 (n/a)</td><td>240.00 (n/a)</td><td>130.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 (-8.37%)</td><td>0.03 <b>(-34.74%)</b></td><td>0.03 <b>(-48.86%)</b></td><td>0.01 (+4.22%)</td><td>0.02 (-14.26%)</td><td>1950.20 (-4.05%)</td><td>976.80 <b>(+46.61%)</b></td><td>516.90 <b>(+95.57%)</b></td><td>262.60 (+9.10%)</td><td>805.28 (+4.04%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2032.50 (n/a)</td><td>666.26 (n/a)</td><td>264.30 (n/a)</td><td>240.70 (n/a)</td><td>774.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 <b>(+20.32%)</b></td><td>0.06 (-1.86%)</td><td>0.04 <b>(-27.30%)</b></td><td>0.03 <b>(-23.08%)</b></td><td>0.03 <b>(+96.40%)</b></td><td>713.70 <b>(+30.00%)</b></td><td>447.06 (+17.42%)</td><td>521.50 <b>(+37.56%)</b></td><td>232.10 (-16.87%)</td><td>206.09 <b>(+94.00%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>549.00 (n/a)</td><td>380.72 (n/a)</td><td>379.10 (n/a)</td><td>279.20 (n/a)</td><td>106.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.03 <b>(-47.63%)</b></td><td>0.03 <b>(-42.25%)</b></td><td>0.03 <b>(-47.51%)</b></td><td>0.01 <b>(+64.83%)</b></td><td>0.01 <b>(-64.95%)</b></td><td>1119.90 <b>(-39.33%)</b></td><td>616.14 (+5.89%)</td><td>501.80 <b>(+90.51%)</b></td><td>471.00 <b>(+90.92%)</b></td><td>282.24 <b>(-60.08%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1845.90 (n/a)</td><td>581.86 (n/a)</td><td>263.40 (n/a)</td><td>246.70 (n/a)</td><td>707.00 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (-17.47%)</td><td>0.06 (+9.63%)</td><td>0.06 <b>(+40.86%)</b></td><td>0.03 (-3.57%)</td><td>0.01 <b>(-24.18%)</b></td><td>557.80 (+3.70%)</td><td>347.24 (-10.90%)</td><td>283.80 <b>(-29.00%)</b></td><td>274.50 <b>(+21.14%)</b></td><td>120.75 (-3.43%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>537.90 (n/a)</td><td>389.70 (n/a)</td><td>399.70 (n/a)</td><td>226.60 (n/a)</td><td>125.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (+18.46%)</td><td>0.05 (+12.97%)</td><td>0.04 (+9.01%)</td><td>0.04 (+17.26%)</td><td>0.02 <b>(+29.64%)</b></td><td>459.50 (-14.72%)</td><td>350.38 (-10.20%)</td><td>382.10 (-8.26%)</td><td>219.40 (-15.58%)</td><td>100.98 (-5.53%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>538.80 (n/a)</td><td>390.18 (n/a)</td><td>416.50 (n/a)</td><td>259.90 (n/a)</td><td>106.89 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (+17.83%)</td><td>0.05 (-11.81%)</td><td>0.04 <b>(-20.97%)</b></td><td>0.03 (-14.72%)</td><td>0.02 <b>(+78.28%)</b></td><td>553.10 (+17.28%)</td><td>429.38 <b>(+20.42%)</b></td><td>434.70 <b>(+26.51%)</b></td><td>231.60 (-15.13%)</td><td>122.81 <b>(+65.74%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>471.60 (n/a)</td><td>356.58 (n/a)</td><td>343.60 (n/a)</td><td>272.90 (n/a)</td><td>74.10 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (+17.60%)</td><td>0.05 (-4.67%)</td><td>0.04 <b>(-25.69%)</b></td><td>0.03 (-2.36%)</td><td>0.02 <b>(+44.52%)</b></td><td>472.90 (+2.40%)</td><td>366.80 (+8.15%)</td><td>412.20 <b>(+34.57%)</b></td><td>222.60 (-14.97%)</td><td>99.39 <b>(+22.29%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>461.80 (n/a)</td><td>339.16 (n/a)</td><td>306.30 (n/a)</td><td>261.80 (n/a)</td><td>81.28 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (+9.54%)</td><td>0.09 (-3.93%)</td><td>0.07 <b>(-42.90%)</b></td><td>0.05 <b>(+169.45%)</b></td><td>0.04 (-19.34%)</td><td>704.90 <b>(-62.89%)</b></td><td>439.36 <b>(-31.17%)</b></td><td>471.40 <b>(+75.11%)</b></td><td>236.10 (-8.70%)</td><td>190.68 <b>(-73.24%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1899.30 (n/a)</td><td>638.32 (n/a)</td><td>269.20 (n/a)</td><td>258.60 (n/a)</td><td>712.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (-19.98%)</td><td>0.08 <b>(-21.54%)</b></td><td>0.07 <b>(-37.31%)</b></td><td>0.05 (-1.89%)</td><td>0.02 <b>(-41.12%)</b></td><td>623.90 (+1.91%)</td><td>435.30 (+17.32%)</td><td>443.50 <b>(+59.53%)</b></td><td>281.40 <b>(+24.96%)</b></td><td>124.84 <b>(-26.05%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>612.20 (n/a)</td><td>371.04 (n/a)</td><td>278.00 (n/a)</td><td>225.20 (n/a)</td><td>168.81 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.20 <b>(+20.09%)</b></td><td>0.12 (+8.12%)</td><td>0.08 <b>(-22.34%)</b></td><td>0.07 (+11.25%)</td><td>0.06 <b>(+32.21%)</b></td><td>585.50 (-10.12%)</td><td>425.52 (-2.52%)</td><td>535.00 <b>(+28.76%)</b></td><td>206.10 (-16.73%)</td><td>190.56 (+1.46%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>651.40 (n/a)</td><td>436.52 (n/a)</td><td>415.50 (n/a)</td><td>247.50 (n/a)</td><td>187.82 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (-10.88%)</td><td>0.08 <b>(-25.16%)</b></td><td>0.07 <b>(-40.44%)</b></td><td>0.06 (+0.31%)</td><td>0.03 (-13.79%)</td><td>527.80 (-0.32%)</td><td>412.30 <b>(+31.24%)</b></td><td>463.20 <b>(+67.89%)</b></td><td>264.90 (+12.20%)</td><td>110.44 (-9.22%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>529.50 (n/a)</td><td>314.16 (n/a)</td><td>275.90 (n/a)</td><td>236.10 (n/a)</td><td>121.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.17 (-2.42%)</td><td>0.09 (-19.32%)</td><td>0.08 <b>(-21.40%)</b></td><td>0.04 <b>(-35.58%)</b></td><td>0.05 <b>(+20.02%)</b></td><td>1107.60 <b>(+55.23%)</b></td><td>577.18 <b>(+41.41%)</b></td><td>488.10 <b>(+27.21%)</b></td><td>235.10 (+2.48%)</td><td>336.99 <b>(+84.48%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>713.50 (n/a)</td><td>408.16 (n/a)</td><td>383.70 (n/a)</td><td>229.40 (n/a)</td><td>182.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (-11.84%)</td><td>0.08 (-13.41%)</td><td>0.06 <b>(-27.99%)</b></td><td>0.05 (-3.06%)</td><td>0.03 (-1.90%)</td><td>614.70 (+3.15%)</td><td>472.24 (+17.41%)</td><td>545.90 <b>(+38.87%)</b></td><td>273.50 (+13.44%)</td><td>150.32 (+18.15%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>595.90 (n/a)</td><td>402.20 (n/a)</td><td>393.10 (n/a)</td><td>241.10 (n/a)</td><td>127.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (+14.36%)</td><td>0.09 (-3.87%)</td><td>0.07 <b>(-32.79%)</b></td><td>0.06 (-10.97%)</td><td>0.04 <b>(+70.01%)</b></td><td>657.10 (+12.31%)</td><td>476.54 (+15.60%)</td><td>544.30 <b>(+48.80%)</b></td><td>257.50 (-12.56%)</td><td>197.29 <b>(+64.04%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>585.10 (n/a)</td><td>412.24 (n/a)</td><td>365.80 (n/a)</td><td>294.50 (n/a)</td><td>120.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 <b>(-27.82%)</b></td><td>0.09 (-17.54%)</td><td>0.09 (-16.85%)</td><td>0.05 (-1.62%)</td><td>0.02 <b>(-42.58%)</b></td><td>602.30 (+1.65%)</td><td>410.18 (+12.24%)</td><td>360.10 <b>(+20.27%)</b></td><td>274.80 <b>(+38.51%)</b></td><td>128.70 (-19.84%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>592.50 (n/a)</td><td>365.46 (n/a)</td><td>299.40 (n/a)</td><td>198.40 (n/a)</td><td>160.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 <b>(+31.10%)</b></td><td>0.11 <b>(+33.74%)</b></td><td>0.13 <b>(+74.84%)</b></td><td>0.06 (-11.11%)</td><td>0.03 <b>(+175.68%)</b></td><td>572.10 (+12.49%)</td><td>381.64 (-18.98%)</td><td>284.50 <b>(-42.81%)</b></td><td>278.10 <b>(-23.72%)</b></td><td>139.32 <b>(+131.04%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>508.60 (n/a)</td><td>471.06 (n/a)</td><td>497.50 (n/a)</td><td>364.60 (n/a)</td><td>60.30 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (+13.97%)</td><td>0.07 <b>(-27.38%)</b></td><td>0.06 <b>(-42.81%)</b></td><td>0.01 <b>(-80.89%)</b></td><td>0.04 <b>(+96.22%)</b></td><td>2410.80 <b>(+423.29%)</b></td><td>839.68 <b>(+133.71%)</b></td><td>534.90 <b>(+74.86%)</b></td><td>244.60 (-12.24%)</td><td>890.89 <b>(+864.14%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>460.70 (n/a)</td><td>359.28 (n/a)</td><td>305.90 (n/a)</td><td>278.70 (n/a)</td><td>92.40 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (+3.15%)</td><td>0.06 (-1.10%)</td><td>0.04 (-9.86%)</td><td>0.03 (-8.61%)</td><td>0.02 (+14.21%)</td><td>602.10 (+9.41%)</td><td>411.72 (+4.60%)</td><td>470.40 (+10.94%)</td><td>224.30 (-3.03%)</td><td>154.95 (+19.82%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>550.30 (n/a)</td><td>393.62 (n/a)</td><td>424.00 (n/a)</td><td>231.30 (n/a)</td><td>129.33 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (-9.77%)</td><td>0.07 (+0.65%)</td><td>0.07 (+0.46%)</td><td>0.06 (+16.43%)</td><td>0.00 <b>(-61.77%)</b></td><td>317.20 (-14.11%)</td><td>295.92 (-2.03%)</td><td>296.50 (-0.47%)</td><td>273.30 (+10.83%)</td><td>15.73 <b>(-64.02%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>369.30 (n/a)</td><td>302.06 (n/a)</td><td>297.90 (n/a)</td><td>246.60 (n/a)</td><td>43.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.11 <b>(+36.98%)</b></td><td>0.08 <b>(+53.49%)</b></td><td>0.08 <b>(+37.24%)</b></td><td>0.04 <b>(+324.80%)</b></td><td>0.02 (-15.69%)</td><td>468.50 <b>(-76.46%)</b></td><td>290.82 <b>(-58.69%)</b></td><td>255.70 <b>(-27.13%)</b></td><td>185.70 <b>(-26.98%)</b></td><td>107.18 <b>(-85.40%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1990.10 (n/a)</td><td>704.06 (n/a)</td><td>350.90 (n/a)</td><td>254.30 (n/a)</td><td>734.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (+6.31%)</td><td>0.06 (+0.94%)</td><td>0.04 <b>(-43.97%)</b></td><td>0.03 <b>(+75.08%)</b></td><td>0.03 (+1.79%)</td><td>590.30 <b>(-42.88%)</b></td><td>426.86 (-11.46%)</td><td>528.10 <b>(+78.47%)</b></td><td>237.50 (-5.94%)</td><td>173.38 <b>(-47.51%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1033.50 (n/a)</td><td>482.12 (n/a)</td><td>295.90 (n/a)</td><td>252.50 (n/a)</td><td>330.28 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 (+8.51%)</td><td>0.06 (+7.71%)</td><td>0.07 <b>(+40.83%)</b></td><td>0.03 (-13.66%)</td><td>0.03 <b>(+34.13%)</b></td><td>700.10 (+15.81%)</td><td>405.60 (+0.98%)</td><td>300.20 <b>(-29.00%)</b></td><td>230.60 (-7.83%)</td><td>201.46 <b>(+46.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.50 (n/a)</td><td>401.68 (n/a)</td><td>422.80 (n/a)</td><td>250.20 (n/a)</td><td>137.12 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 (-0.39%)</td><td>0.06 (-18.54%)</td><td>0.05 <b>(-32.55%)</b></td><td>0.04 <b>(-26.97%)</b></td><td>0.02 <b>(+47.37%)</b></td><td>521.10 <b>(+36.92%)</b></td><td>382.04 <b>(+27.53%)</b></td><td>396.30 <b>(+48.26%)</b></td><td>266.40 (+0.41%)</td><td>101.90 <b>(+101.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>380.60 (n/a)</td><td>299.56 (n/a)</td><td>267.30 (n/a)</td><td>265.30 (n/a)</td><td>50.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 <b>(-24.21%)</b></td><td>0.07 <b>(-20.83%)</b></td><td>0.08 (-9.21%)</td><td>0.05 (-4.72%)</td><td>0.02 <b>(-20.52%)</b></td><td>538.00 (+4.96%)</td><td>393.82 <b>(+25.21%)</b></td><td>325.40 (+10.12%)</td><td>282.70 <b>(+31.98%)</b></td><td>128.09 (+9.40%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>512.60 (n/a)</td><td>314.54 (n/a)</td><td>295.50 (n/a)</td><td>214.20 (n/a)</td><td>117.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.11 (-9.53%)</td><td>0.08 (+1.92%)</td><td>0.09 (+2.82%)</td><td>0.06 <b>(+52.70%)</b></td><td>0.02 <b>(-22.57%)</b></td><td>416.40 <b>(-34.52%)</b></td><td>306.90 (-9.43%)</td><td>267.50 (-2.73%)</td><td>233.30 (+10.52%)</td><td>85.53 <b>(-49.45%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>635.90 (n/a)</td><td>338.84 (n/a)</td><td>275.00 (n/a)</td><td>211.10 (n/a)</td><td>169.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (+1.63%)</td><td>0.07 (+7.69%)</td><td>0.09 <b>(+54.81%)</b></td><td>0.04 (-9.15%)</td><td>0.03 <b>(+23.19%)</b></td><td>597.70 (+10.07%)</td><td>391.28 (-1.29%)</td><td>284.10 <b>(-35.40%)</b></td><td>247.80 (-1.59%)</td><td>174.81 <b>(+40.86%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>543.00 (n/a)</td><td>396.38 (n/a)</td><td>439.80 (n/a)</td><td>251.80 (n/a)</td><td>124.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (-1.11%)</td><td>0.06 (+2.91%)</td><td>0.05 (-11.75%)</td><td>0.04 (+4.77%)</td><td>0.03 (+9.47%)</td><td>624.60 (-4.57%)</td><td>438.20 (-0.89%)</td><td>474.40 (+13.30%)</td><td>245.60 (+1.15%)</td><td>166.24 (+4.83%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>654.50 (n/a)</td><td>442.14 (n/a)</td><td>418.70 (n/a)</td><td>242.80 (n/a)</td><td>158.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.11 (-8.30%)</td><td>0.07 (+19.03%)</td><td>0.07 <b>(+48.15%)</b></td><td>0.05 (+18.07%)</td><td>0.03 <b>(-24.24%)</b></td><td>511.40 (-15.30%)</td><td>383.14 <b>(-21.21%)</b></td><td>359.60 <b>(-32.49%)</b></td><td>224.50 (+9.09%)</td><td>126.20 <b>(-21.65%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>603.80 (n/a)</td><td>486.26 (n/a)</td><td>532.70 (n/a)</td><td>205.80 (n/a)</td><td>161.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.10 (+1.90%)</td><td>0.07 (+13.19%)</td><td>0.08 (+19.92%)</td><td>0.04 (+4.22%)</td><td>0.02 (+6.71%)</td><td>605.60 (-4.04%)</td><td>374.22 (-11.28%)</td><td>290.60 (-16.61%)</td><td>254.50 (-1.89%)</td><td>148.81 (-2.95%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>631.10 (n/a)</td><td>421.78 (n/a)</td><td>348.50 (n/a)</td><td>259.40 (n/a)</td><td>153.33 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (-0.49%)</td><td>0.04 <b>(-27.14%)</b></td><td>0.04 <b>(-38.77%)</b></td><td>0.01 <b>(-70.48%)</b></td><td>0.02 <b>(+43.58%)</b></td><td>1849.70 <b>(+238.83%)</b></td><td>734.12 <b>(+103.21%)</b></td><td>448.80 <b>(+63.32%)</b></td><td>267.20 (+0.49%)</td><td>658.60 <b>(+405.47%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>545.90 (n/a)</td><td>361.26 (n/a)</td><td>274.80 (n/a)</td><td>265.90 (n/a)</td><td>130.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (+3.26%)</td><td>0.05 (+11.47%)</td><td>0.05 <b>(+43.46%)</b></td><td>0.03 (+5.84%)</td><td>0.02 (-0.25%)</td><td>606.30 (-5.52%)</td><td>406.26 (-10.78%)</td><td>341.70 <b>(-30.29%)</b></td><td>270.90 (-3.18%)</td><td>149.79 (-5.26%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>641.70 (n/a)</td><td>455.36 (n/a)</td><td>490.20 (n/a)</td><td>279.80 (n/a)</td><td>158.10 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 <b>(+38.86%)</b></td><td>0.07 <b>(+63.58%)</b></td><td>0.07 <b>(+68.86%)</b></td><td>0.03 <b>(+254.72%)</b></td><td>0.02 (-7.51%)</td><td>552.50 <b>(-71.81%)</b></td><td>301.76 <b>(-57.90%)</b></td><td>256.80 <b>(-40.77%)</b></td><td>196.60 <b>(-27.99%)</b></td><td>142.50 <b>(-79.89%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1959.80 (n/a)</td><td>716.78 (n/a)</td><td>433.60 (n/a)</td><td>273.00 (n/a)</td><td>708.58 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.08 <b>(+22.02%)</b></td><td>0.06 <b>(+42.72%)</b></td><td>0.07 <b>(+68.65%)</b></td><td>0.04 (+2.14%)</td><td>0.02 <b>(+59.29%)</b></td><td>496.60 (-2.09%)</td><td>305.40 <b>(-27.22%)</b></td><td>256.00 <b>(-40.70%)</b></td><td>243.10 (-18.07%)</td><td>108.00 <b>(+34.62%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>507.20 (n/a)</td><td>419.60 (n/a)</td><td>431.70 (n/a)</td><td>296.70 (n/a)</td><td>80.22 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.06 <b>(-21.21%)</b></td><td>0.04 (-15.36%)</td><td>0.05 (-16.19%)</td><td>0.03 (-10.96%)</td><td>0.01 <b>(-21.63%)</b></td><td>600.50 (+12.31%)</td><td>440.90 (+17.37%)</td><td>409.60 (+19.31%)</td><td>318.10 <b>(+26.94%)</b></td><td>118.12 (+11.35%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>534.70 (n/a)</td><td>375.64 (n/a)</td><td>343.30 (n/a)</td><td>250.60 (n/a)</td><td>106.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (+19.02%)</td><td>0.05 <b>(+29.65%)</b></td><td>0.06 <b>(+54.70%)</b></td><td>0.02 (-3.53%)</td><td>0.02 <b>(+50.06%)</b></td><td>832.50 (+3.66%)</td><td>446.02 (-14.68%)</td><td>310.30 <b>(-35.35%)</b></td><td>246.00 (-15.98%)</td><td>251.75 <b>(+28.93%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>803.10 (n/a)</td><td>522.74 (n/a)</td><td>480.00 (n/a)</td><td>292.80 (n/a)</td><td>195.26 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.43 (+5.96%)</td><td>0.33 (+13.89%)</td><td>0.37 <b>(+29.55%)</b></td><td>0.17 (-9.99%)</td><td>0.10 <b>(+20.70%)</b></td><td>573.90 (+11.09%)</td><td>326.36 (-8.61%)</td><td>268.80 <b>(-22.83%)</b></td><td>227.40 (-5.60%)</td><td>140.71 <b>(+35.25%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>516.60 (n/a)</td><td>357.12 (n/a)</td><td>348.30 (n/a)</td><td>240.90 (n/a)</td><td>104.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.40 (-0.50%)</td><td>0.28 (+4.16%)</td><td>0.25 (+13.34%)</td><td>0.16 (-9.29%)</td><td>0.10 (-5.34%)</td><td>607.40 (+10.24%)</td><td>387.86 (-4.36%)</td><td>397.40 (-11.79%)</td><td>242.90 (+0.50%)</td><td>142.33 (+4.49%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.41 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>551.00 (n/a)</td><td>405.56 (n/a)</td><td>450.50 (n/a)</td><td>241.70 (n/a)</td><td>136.22 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.40 <b>(-21.92%)</b></td><td>0.27 (+15.69%)</td><td>0.32 <b>(+80.39%)</b></td><td>0.04 (-16.89%)</td><td>0.15 (-15.69%)</td><td>2467.70 <b>(+20.32%)</b></td><td>755.86 (-0.42%)</td><td>306.10 <b>(-44.57%)</b></td><td>244.70 <b>(+28.12%)</b></td><td>961.68 <b>(+30.18%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.51 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>0.17 (n/a)</td><td>2050.90 (n/a)</td><td>759.08 (n/a)</td><td>552.20 (n/a)</td><td>191.00 (n/a)</td><td>738.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.29 (+7.62%)</td><td>0.19 (+11.27%)</td><td>0.16 (-2.29%)</td><td>0.15 <b>(+409.79%)</b></td><td>0.06 <b>(-37.76%)</b></td><td>485.10 <b>(-80.38%)</b></td><td>406.42 <b>(-48.66%)</b></td><td>455.00 (+2.36%)</td><td>254.90 (-7.11%)</td><td>94.50 <b>(-89.98%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>0.09 (n/a)</td><td>2473.10 (n/a)</td><td>791.64 (n/a)</td><td>444.50 (n/a)</td><td>274.40 (n/a)</td><td>943.24 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.30 (-11.81%)</td><td>0.25 (-2.17%)</td><td>0.25 (-4.30%)</td><td>0.20 <b>(+44.70%)</b></td><td>0.04 <b>(-49.00%)</b></td><td>371.90 <b>(-30.90%)</b></td><td>296.08 (-5.78%)</td><td>292.00 (+4.51%)</td><td>249.90 (+13.38%)</td><td>50.06 <b>(-61.51%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>538.20 (n/a)</td><td>314.24 (n/a)</td><td>279.40 (n/a)</td><td>220.40 (n/a)</td><td>130.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.28 (-13.40%)</td><td>0.19 <b>(-23.03%)</b></td><td>0.16 <b>(-35.44%)</b></td><td>0.12 <b>(-26.83%)</b></td><td>0.07 <b>(+20.61%)</b></td><td>606.80 <b>(+36.67%)</b></td><td>436.76 <b>(+36.62%)</b></td><td>471.70 <b>(+54.91%)</b></td><td>267.30 (+15.46%)</td><td>140.68 <b>(+82.51%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>444.00 (n/a)</td><td>319.70 (n/a)</td><td>304.50 (n/a)</td><td>231.50 (n/a)</td><td>77.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (-1.23%)</td><td>0.14 (-1.61%)</td><td>0.13 (-12.62%)</td><td>0.13 <b>(+26.69%)</b></td><td>0.01 <b>(-47.93%)</b></td><td>291.30 <b>(-21.06%)</b></td><td>271.18 (-0.46%)</td><td>280.00 (+14.43%)</td><td>242.00 (+1.26%)</td><td>22.80 <b>(-58.63%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>369.00 (n/a)</td><td>272.44 (n/a)</td><td>244.70 (n/a)</td><td>239.00 (n/a)</td><td>55.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (+15.45%)</td><td>0.11 (-4.44%)</td><td>0.12 (+0.53%)</td><td>0.06 <b>(-24.19%)</b></td><td>0.04 <b>(+114.22%)</b></td><td>596.70 <b>(+31.93%)</b></td><td>396.34 (+17.27%)</td><td>303.90 (-0.52%)</td><td>243.90 (-13.39%)</td><td>171.35 <b>(+150.99%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>452.30 (n/a)</td><td>337.96 (n/a)</td><td>305.50 (n/a)</td><td>281.60 (n/a)</td><td>68.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (-2.54%)</td><td>0.09 (-14.92%)</td><td>0.07 <b>(-32.94%)</b></td><td>0.07 (+4.38%)</td><td>0.03 (+2.97%)</td><td>547.60 (-4.20%)</td><td>441.50 (+17.76%)</td><td>498.50 <b>(+49.12%)</b></td><td>258.30 (+2.62%)</td><td>120.07 (-2.11%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>571.60 (n/a)</td><td>374.92 (n/a)</td><td>334.30 (n/a)</td><td>251.70 (n/a)</td><td>122.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (+4.62%)</td><td>0.11 (+18.76%)</td><td>0.12 <b>(+48.48%)</b></td><td>0.07 (+16.25%)</td><td>0.03 (+16.00%)</td><td>553.60 (-13.98%)</td><td>375.32 (-15.16%)</td><td>305.30 <b>(-32.65%)</b></td><td>277.70 (-4.41%)</td><td>123.70 (-6.81%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>643.60 (n/a)</td><td>442.38 (n/a)</td><td>453.30 (n/a)</td><td>290.50 (n/a)</td><td>132.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (-17.73%)</td><td>0.09 (-9.43%)</td><td>0.07 (-14.79%)</td><td>0.06 <b>(+285.30%)</b></td><td>0.04 <b>(-38.68%)</b></td><td>629.10 <b>(-74.05%)</b></td><td>481.56 <b>(-37.86%)</b></td><td>521.90 (+17.36%)</td><td>243.50 <b>(+21.57%)</b></td><td>144.89 <b>(-84.39%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2424.10 (n/a)</td><td>774.98 (n/a)</td><td>444.70 (n/a)</td><td>200.30 (n/a)</td><td>928.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (-18.86%)</td><td>0.10 (-10.20%)</td><td>0.09 (-3.17%)</td><td>0.07 (-1.79%)</td><td>0.04 <b>(-26.05%)</b></td><td>532.80 (+1.82%)</td><td>405.68 (+6.88%)</td><td>430.80 (+3.26%)</td><td>260.40 <b>(+23.24%)</b></td><td>132.46 (-7.86%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>523.30 (n/a)</td><td>379.58 (n/a)</td><td>417.20 (n/a)</td><td>211.30 (n/a)</td><td>143.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 (+3.12%)</td><td>0.10 (-14.93%)</td><td>0.09 <b>(-25.90%)</b></td><td>0.02 <b>(-78.65%)</b></td><td>0.06 <b>(+57.37%)</b></td><td>2467.20 <b>(+368.52%)</b></td><td>792.22 <b>(+106.39%)</b></td><td>438.40 <b>(+34.98%)</b></td><td>254.70 (-3.01%)</td><td>942.80 <b>(+626.05%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>526.60 (n/a)</td><td>383.84 (n/a)</td><td>324.80 (n/a)</td><td>262.60 (n/a)</td><td>129.85 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 <b>(+28.99%)</b></td><td>0.11 (+17.62%)</td><td>0.11 (+15.73%)</td><td>0.07 (-13.25%)</td><td>0.04 <b>(+107.57%)</b></td><td>586.00 (+15.26%)</td><td>399.92 (-9.61%)</td><td>388.20 (-13.58%)</td><td>256.00 <b>(-22.47%)</b></td><td>129.66 <b>(+90.15%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>508.40 (n/a)</td><td>442.42 (n/a)</td><td>449.20 (n/a)</td><td>330.20 (n/a)</td><td>68.19 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 <b>(-22.48%)</b></td><td>0.10 <b>(-23.54%)</b></td><td>0.09 <b>(-40.14%)</b></td><td>0.07 <b>(+235.98%)</b></td><td>0.03 <b>(-50.82%)</b></td><td>567.10 <b>(-70.24%)</b></td><td>446.50 <b>(-25.04%)</b></td><td>478.60 <b>(+67.05%)</b></td><td>275.80 <b>(+29.00%)</b></td><td>118.64 <b>(-83.81%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1905.30 (n/a)</td><td>595.68 (n/a)</td><td>286.50 (n/a)</td><td>213.80 (n/a)</td><td>732.82 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (+0.03%)</td><td>0.12 <b>(+59.63%)</b></td><td>0.13 <b>(+77.48%)</b></td><td>0.07 <b>(+326.83%)</b></td><td>0.04 <b>(-30.87%)</b></td><td>581.70 <b>(-76.57%)</b></td><td>393.00 <b>(-65.08%)</b></td><td>304.00 <b>(-43.65%)</b></td><td>273.40 (-0.04%)</td><td>148.63 <b>(-85.23%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2482.90 (n/a)</td><td>1125.36 (n/a)</td><td>539.50 (n/a)</td><td>273.50 (n/a)</td><td>1006.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.18 (+6.96%)</td><td>0.14 <b>(+30.19%)</b></td><td>0.16 <b>(+80.57%)</b></td><td>0.09 <b>(+29.66%)</b></td><td>0.04 <b>(-24.43%)</b></td><td>466.20 <b>(-22.88%)</b></td><td>303.14 <b>(-29.02%)</b></td><td>251.50 <b>(-44.62%)</b></td><td>231.60 (-6.50%)</td><td>96.54 <b>(-42.67%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>604.50 (n/a)</td><td>427.06 (n/a)</td><td>454.10 (n/a)</td><td>247.70 (n/a)</td><td>168.40 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 <b>(+46.94%)</b></td><td>0.11 <b>(+38.64%)</b></td><td>0.09 (+12.49%)</td><td>0.07 <b>(+61.30%)</b></td><td>0.04 <b>(+66.72%)</b></td><td>619.20 <b>(-38.01%)</b></td><td>412.20 <b>(-27.49%)</b></td><td>460.70 (-11.10%)</td><td>252.60 <b>(-31.93%)</b></td><td>154.41 <b>(-38.14%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>998.90 (n/a)</td><td>568.44 (n/a)</td><td>518.20 (n/a)</td><td>371.10 (n/a)</td><td>249.60 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (-2.69%)</td><td>0.09 (-15.17%)</td><td>0.11 (-10.67%)</td><td>0.03 <b>(-49.16%)</b></td><td>0.04 <b>(+38.60%)</b></td><td>1114.50 <b>(+96.66%)</b></td><td>483.98 <b>(+42.67%)</b></td><td>312.40 (+11.93%)</td><td>276.50 (+2.75%)</td><td>358.05 <b>(+179.49%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>566.70 (n/a)</td><td>339.22 (n/a)</td><td>279.10 (n/a)</td><td>269.10 (n/a)</td><td>128.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.09 <b>(-27.13%)</b></td><td>0.08 (-11.51%)</td><td>0.07 (-11.08%)</td><td>0.07 <b>(+42.71%)</b></td><td>0.01 <b>(-67.40%)</b></td><td>523.90 <b>(-29.93%)</b></td><td>455.42 (+0.85%)</td><td>477.00 (+12.45%)</td><td>371.80 <b>(+37.25%)</b></td><td>59.46 <b>(-68.64%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>747.70 (n/a)</td><td>451.60 (n/a)</td><td>424.20 (n/a)</td><td>270.90 (n/a)</td><td>189.61 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.13 (-15.88%)</td><td>0.09 <b>(-29.44%)</b></td><td>0.07 <b>(-39.39%)</b></td><td>0.07 <b>(-41.22%)</b></td><td>0.03 <b>(+60.04%)</b></td><td>533.20 <b>(+70.13%)</b></td><td>411.86 <b>(+51.93%)</b></td><td>477.50 <b>(+65.00%)</b></td><td>261.00 (+18.91%)</td><td>125.55 <b>(+223.78%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>313.40 (n/a)</td><td>271.08 (n/a)</td><td>289.40 (n/a)</td><td>219.50 (n/a)</td><td>38.77 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (-1.10%)</td><td>0.12 (+17.95%)</td><td>0.13 (+8.87%)</td><td>0.08 <b>(+32.19%)</b></td><td>0.02 <b>(-32.24%)</b></td><td>426.50 <b>(-24.34%)</b></td><td>296.86 <b>(-20.94%)</b></td><td>275.90 (-8.16%)</td><td>242.40 (+1.08%)</td><td>74.63 <b>(-48.04%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>563.70 (n/a)</td><td>375.50 (n/a)</td><td>300.40 (n/a)</td><td>239.80 (n/a)</td><td>143.61 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (+2.14%)</td><td>0.08 <b>(-20.45%)</b></td><td>0.07 <b>(-35.53%)</b></td><td>0.06 <b>(-22.79%)</b></td><td>0.04 <b>(+29.14%)</b></td><td>628.90 <b>(+29.51%)</b></td><td>465.92 <b>(+31.91%)</b></td><td>482.90 <b>(+55.07%)</b></td><td>240.20 (-2.12%)</td><td>141.49 <b>(+48.15%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>485.60 (n/a)</td><td>353.22 (n/a)</td><td>311.40 (n/a)</td><td>245.40 (n/a)</td><td>95.51 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.12 (+7.83%)</td><td>0.10 (+13.65%)</td><td>0.11 <b>(+33.50%)</b></td><td>0.07 (-7.93%)</td><td>0.03 <b>(+63.29%)</b></td><td>494.70 (+8.63%)</td><td>375.26 (-8.31%)</td><td>318.80 <b>(-25.09%)</b></td><td>279.50 (-7.24%)</td><td>109.16 <b>(+73.39%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>455.40 (n/a)</td><td>409.28 (n/a)</td><td>425.60 (n/a)</td><td>301.30 (n/a)</td><td>62.96 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.53 (+15.48%)</td><td>0.33 (-2.81%)</td><td>0.29 <b>(-20.00%)</b></td><td>0.21 (-4.85%)</td><td>0.13 <b>(+38.58%)</b></td><td>623.50 (+5.09%)</td><td>449.18 (+8.26%)</td><td>445.10 <b>(+24.99%)</b></td><td>246.90 (-13.43%)</td><td>164.21 <b>(+28.14%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.46 (n/a)</td><td>0.34 (n/a)</td><td>0.37 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>593.30 (n/a)</td><td>414.90 (n/a)</td><td>356.10 (n/a)</td><td>285.20 (n/a)</td><td>128.15 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.62 <b>(+25.92%)</b></td><td>0.43 (+3.99%)</td><td>0.46 (-2.01%)</td><td>0.24 <b>(+23.75%)</b></td><td>0.14 (+12.16%)</td><td>550.70 (-19.18%)</td><td>336.86 (-6.49%)</td><td>287.40 (+2.06%)</td><td>210.50 <b>(-20.60%)</b></td><td>129.51 <b>(-28.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.49 (n/a)</td><td>0.41 (n/a)</td><td>0.47 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>681.40 (n/a)</td><td>360.24 (n/a)</td><td>281.60 (n/a)</td><td>265.10 (n/a)</td><td>179.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.56 (+17.65%)</td><td>0.33 (+4.05%)</td><td>0.26 <b>(-38.46%)</b></td><td>0.23 <b>(+237.03%)</b></td><td>0.14 <b>(-22.99%)</b></td><td>562.30 <b>(-70.33%)</b></td><td>435.96 <b>(-36.62%)</b></td><td>504.10 <b>(+62.51%)</b></td><td>233.30 (-15.01%)</td><td>137.94 <b>(-80.11%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.48 (n/a)</td><td>0.32 (n/a)</td><td>0.42 (n/a)</td><td>0.07 (n/a)</td><td>0.18 (n/a)</td><td>1895.10 (n/a)</td><td>687.86 (n/a)</td><td>310.20 (n/a)</td><td>274.50 (n/a)</td><td>693.60 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.00 (-14.29%)</td><td>0.00 <b>(+40.00%)</b></td><td>0.00 <b>(+150.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-8.35%)</td><td>22498.87 (+3.45%)</td><td>13101.30 <b>(-23.27%)</b></td><td>7619.61 <b>(-60.05%)</b></td><td>7203.67 <b>(+24.74%)</b></td><td>7897.51 <b>(+22.38%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21748.18 (n/a)</td><td>17075.31 (n/a)</td><td>19071.51 (n/a)</td><td>5775.14 (n/a)</td><td>6453.48 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.00 (+10.00%)</td><td>0.00 <b>(+21.43%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+6.41%)</td><td>20888.31 (-9.36%)</td><td>13452.45 <b>(-22.92%)</b></td><td>13505.60 <b>(-36.91%)</b></td><td>7299.37 (-7.94%)</td><td>5319.49 <b>(-20.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23044.48 (n/a)</td><td>17451.74 (n/a)</td><td>21405.97 (n/a)</td><td>7929.23 (n/a)</td><td>6656.52 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.14 (+1.30%)</td><td>0.09 (-3.61%)</td><td>0.07 (-15.04%)</td><td>0.07 (-8.67%)</td><td>0.03 (+17.56%)</td><td>30184.63 (+9.49%)</td><td>25327.87 (+6.54%)</td><td>29701.07 (+17.71%)</td><td>14927.20 (-1.29%)</td><td>6782.68 <b>(+34.60%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27568.84 (n/a)</td><td>23772.59 (n/a)</td><td>25231.90 (n/a)</td><td>15121.81 (n/a)</td><td>5039.14 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.02 <b>(+31.09%)</b></td><td>1.76 (+4.62%)</td><td>1.78 (+0.83%)</td><td>0.56 <b>(-45.71%)</b></td><td>0.98 <b>(+109.13%)</b></td><td>1866.00 <b>(+84.19%)</b></td><td>840.32 <b>(+25.94%)</b></td><td>588.00 (-0.83%)</td><td>347.50 <b>(-23.71%)</b></td><td>618.39 <b>(+190.66%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>2.30 (n/a)</td><td>1.69 (n/a)</td><td>1.77 (n/a)</td><td>1.04 (n/a)</td><td>0.47 (n/a)</td><td>1013.10 (n/a)</td><td>667.26 (n/a)</td><td>592.90 (n/a)</td><td>455.50 (n/a)</td><td>212.76 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.43 (-7.00%)</td><td>1.83 (-19.29%)</td><td>1.59 (-5.71%)</td><td>0.30 <b>(-78.03%)</b></td><td>1.23 (+15.20%)</td><td>3454.50 <b>(+355.14%)</b></td><td>1137.92 <b>(+109.69%)</b></td><td>661.00 (+6.05%)</td><td>305.90 (+7.52%)</td><td>1314.07 <b>(+499.80%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.69 (n/a)</td><td>2.27 (n/a)</td><td>1.68 (n/a)</td><td>1.38 (n/a)</td><td>1.06 (n/a)</td><td>759.00 (n/a)</td><td>542.68 (n/a)</td><td>623.30 (n/a)</td><td>284.50 (n/a)</td><td>219.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.85 (+18.71%)</td><td>1.78 (-4.75%)</td><td>1.43 <b>(-39.28%)</b></td><td>0.56 <b>(+73.00%)</b></td><td>1.26 (-5.33%)</td><td>1860.30 <b>(-42.20%)</b></td><td>869.62 <b>(-29.31%)</b></td><td>731.50 <b>(+64.72%)</b></td><td>272.60 (-15.76%)</td><td>606.69 <b>(-52.23%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.24 (n/a)</td><td>1.87 (n/a)</td><td>2.36 (n/a)</td><td>0.33 (n/a)</td><td>1.33 (n/a)</td><td>3218.50 (n/a)</td><td>1230.12 (n/a)</td><td>444.10 (n/a)</td><td>323.60 (n/a)</td><td>1269.93 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.44 <b>(+29.80%)</b></td><td>1.75 (-18.88%)</td><td>1.44 <b>(-41.31%)</b></td><td>1.15 <b>(-20.19%)</b></td><td>0.96 <b>(+78.02%)</b></td><td>915.40 <b>(+25.29%)</b></td><td>704.10 <b>(+36.85%)</b></td><td>729.60 <b>(+70.39%)</b></td><td>304.80 <b>(-22.97%)</b></td><td>249.83 <b>(+69.96%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>2.65 (n/a)</td><td>2.16 (n/a)</td><td>2.45 (n/a)</td><td>1.44 (n/a)</td><td>0.54 (n/a)</td><td>730.60 (n/a)</td><td>514.52 (n/a)</td><td>428.20 (n/a)</td><td>395.70 (n/a)</td><td>146.99 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>4.21 <b>(+23.04%)</b></td><td>3.07 <b>(+75.38%)</b></td><td>3.45 <b>(+218.21%)</b></td><td>0.70 <b>(+25.62%)</b></td><td>1.38 (-0.11%)</td><td>2980.00 <b>(-20.39%)</b></td><td>1059.48 <b>(-48.51%)</b></td><td>608.70 <b>(-68.58%)</b></td><td>498.20 (-18.73%)</td><td>1075.23 <b>(-25.69%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.42 (n/a)</td><td>1.75 (n/a)</td><td>1.08 (n/a)</td><td>0.56 (n/a)</td><td>1.38 (n/a)</td><td>3743.40 (n/a)</td><td>2057.46 (n/a)</td><td>1937.00 (n/a)</td><td>613.00 (n/a)</td><td>1447.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.31 (+5.80%)</td><td>2.63 (+19.82%)</td><td>2.18 <b>(+100.03%)</b></td><td>0.59 (-0.07%)</td><td>2.18 (+7.18%)</td><td>3549.80 (+0.06%)</td><td>1767.14 (-11.53%)</td><td>961.70 <b>(-50.01%)</b></td><td>395.20 (-5.48%)</td><td>1601.03 (+5.09%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.02 (n/a)</td><td>2.19 (n/a)</td><td>1.09 (n/a)</td><td>0.59 (n/a)</td><td>2.03 (n/a)</td><td>3547.50 (n/a)</td><td>1997.54 (n/a)</td><td>1923.70 (n/a)</td><td>418.10 (n/a)</td><td>1523.52 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.10 (+1.77%)</td><td>3.44 (+17.31%)</td><td>3.16 (+12.05%)</td><td>1.89 <b>(+218.72%)</b></td><td>1.20 <b>(-28.18%)</b></td><td>1107.60 <b>(-68.63%)</b></td><td>679.90 <b>(-44.58%)</b></td><td>664.10 (-10.75%)</td><td>411.30 (-1.74%)</td><td>264.96 <b>(-79.64%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.01 (n/a)</td><td>2.93 (n/a)</td><td>2.82 (n/a)</td><td>0.59 (n/a)</td><td>1.67 (n/a)</td><td>3530.20 (n/a)</td><td>1226.80 (n/a)</td><td>744.10 (n/a)</td><td>418.60 (n/a)</td><td>1301.22 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.93 (-15.24%)</td><td>4.00 (-15.08%)</td><td>3.59 <b>(-36.88%)</b></td><td>2.23 <b>(+164.02%)</b></td><td>1.64 <b>(-38.14%)</b></td><td>939.80 <b>(-62.12%)</b></td><td>603.34 <b>(-26.72%)</b></td><td>584.40 <b>(+58.42%)</b></td><td>353.70 (+17.98%)</td><td>249.44 <b>(-73.43%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>6.99 (n/a)</td><td>4.71 (n/a)</td><td>5.69 (n/a)</td><td>0.85 (n/a)</td><td>2.65 (n/a)</td><td>2481.30 (n/a)</td><td>823.30 (n/a)</td><td>368.90 (n/a)</td><td>299.80 (n/a)</td><td>938.66 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>4.52 (+0.91%)</td><td>2.12 <b>(-42.99%)</b></td><td>1.81 <b>(-56.39%)</b></td><td>0.60 <b>(-78.84%)</b></td><td>1.45 <b>(+80.79%)</b></td><td>3514.60 <b>(+372.71%)</b></td><td>1486.64 <b>(+153.57%)</b></td><td>1156.60 <b>(+129.30%)</b></td><td>464.20 (-0.92%)</td><td>1175.12 <b>(+765.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>4.48 (n/a)</td><td>3.73 (n/a)</td><td>4.16 (n/a)</td><td>2.82 (n/a)</td><td>0.80 (n/a)</td><td>743.50 (n/a)</td><td>586.28 (n/a)</td><td>504.40 (n/a)</td><td>468.50 (n/a)</td><td>135.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.31 (-10.43%)</td><td>3.88 (+15.40%)</td><td>3.90 (+10.28%)</td><td>2.71 <b>(+364.58%)</b></td><td>1.10 <b>(-44.98%)</b></td><td>773.20 <b>(-78.47%)</b></td><td>576.78 <b>(-50.92%)</b></td><td>538.20 (-9.32%)</td><td>395.20 (+11.64%)</td><td>164.71 <b>(-87.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.92 (n/a)</td><td>3.37 (n/a)</td><td>3.53 (n/a)</td><td>0.58 (n/a)</td><td>2.00 (n/a)</td><td>3592.00 (n/a)</td><td>1175.24 (n/a)</td><td>593.50 (n/a)</td><td>354.00 (n/a)</td><td>1363.35 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>5.07 (+0.30%)</td><td>3.61 (-18.34%)</td><td>4.71 (+6.01%)</td><td>1.68 <b>(-57.66%)</b></td><td>1.75 <b>(+323.03%)</b></td><td>2490.70 <b>(+136.17%)</b></td><td>1503.46 <b>(+57.36%)</b></td><td>891.40 (-5.67%)</td><td>826.60 (-0.30%)</td><td>881.76 <b>(+927.96%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>5.06 (n/a)</td><td>4.42 (n/a)</td><td>4.44 (n/a)</td><td>3.98 (n/a)</td><td>0.41 (n/a)</td><td>1054.60 (n/a)</td><td>955.44 (n/a)</td><td>945.00 (n/a)</td><td>829.10 (n/a)</td><td>85.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>8.56 (-2.40%)</td><td>5.11 (+0.02%)</td><td>4.90 <b>(-24.75%)</b></td><td>1.69 <b>(+44.19%)</b></td><td>2.94 (-19.26%)</td><td>2475.90 <b>(-30.65%)</b></td><td>1169.94 <b>(-31.81%)</b></td><td>855.70 <b>(+32.89%)</b></td><td>489.90 (+2.47%)</td><td>826.89 <b>(-48.18%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>8.77 (n/a)</td><td>5.11 (n/a)</td><td>6.51 (n/a)</td><td>1.17 (n/a)</td><td>3.65 (n/a)</td><td>3569.90 (n/a)</td><td>1715.66 (n/a)</td><td>643.90 (n/a)</td><td>478.10 (n/a)</td><td>1595.76 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>7.94 (-11.24%)</td><td>4.37 <b>(-42.97%)</b></td><td>3.86 <b>(-50.55%)</b></td><td>1.26 <b>(-78.94%)</b></td><td>2.95 <b>(+164.90%)</b></td><td>3335.80 <b>(+374.91%)</b></td><td>1545.74 <b>(+177.00%)</b></td><td>1086.20 <b>(+102.20%)</b></td><td>528.30 (+12.67%)</td><td>1194.16 <b>(+1241.16%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>8.94 (n/a)</td><td>7.66 (n/a)</td><td>7.81 (n/a)</td><td>5.97 (n/a)</td><td>1.11 (n/a)</td><td>702.40 (n/a)</td><td>558.02 (n/a)</td><td>537.20 (n/a)</td><td>468.90 (n/a)</td><td>89.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>10.09 (-2.38%)</td><td>6.78 <b>(-23.36%)</b></td><td>7.23 <b>(-22.74%)</b></td><td>1.26 <b>(-80.69%)</b></td><td>3.31 <b>(+129.26%)</b></td><td>3337.20 <b>(+418.04%)</b></td><td>1086.72 <b>(+123.60%)</b></td><td>580.00 <b>(+29.44%)</b></td><td>415.60 (+2.44%)</td><td>1260.01 <b>(+1254.06%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>10.34 (n/a)</td><td>8.85 (n/a)</td><td>9.36 (n/a)</td><td>6.51 (n/a)</td><td>1.45 (n/a)</td><td>644.20 (n/a)</td><td>486.02 (n/a)</td><td>448.10 (n/a)</td><td>405.70 (n/a)</td><td>93.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>6.77 <b>(-27.75%)</b></td><td>4.13 <b>(-32.01%)</b></td><td>5.30 <b>(-20.73%)</b></td><td>1.20 <b>(-62.10%)</b></td><td>2.70 (+8.79%)</td><td>3485.70 <b>(+163.87%)</b></td><td>1786.18 <b>(+122.11%)</b></td><td>792.00 <b>(+26.15%)</b></td><td>619.70 <b>(+38.39%)</b></td><td>1490.57 <b>(+313.25%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>9.37 (n/a)</td><td>6.07 (n/a)</td><td>6.68 (n/a)</td><td>3.18 (n/a)</td><td>2.48 (n/a)</td><td>1321.00 (n/a)</td><td>804.20 (n/a)</td><td>627.80 (n/a)</td><td>447.80 (n/a)</td><td>360.69 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>9.28 (+10.40%)</td><td>5.82 (+7.49%)</td><td>6.67 (+3.10%)</td><td>1.18 (+8.25%)</td><td>3.20 (+14.84%)</td><td>3551.20 (-7.62%)</td><td>1236.06 (-5.82%)</td><td>629.30 (-3.01%)</td><td>451.80 (-9.40%)</td><td>1311.64 (-7.91%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>8.41 (n/a)</td><td>5.41 (n/a)</td><td>6.46 (n/a)</td><td>1.09 (n/a)</td><td>2.79 (n/a)</td><td>3844.30 (n/a)</td><td>1312.38 (n/a)</td><td>648.80 (n/a)</td><td>498.70 (n/a)</td><td>1424.25 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>1.47 (-9.77%)</td><td>0.75 <b>(-42.22%)</b></td><td>0.59 <b>(-58.36%)</b></td><td>0.27 <b>(-70.61%)</b></td><td>0.54 <b>(+81.53%)</b></td><td>1923.20 <b>(+240.27%)</b></td><td>1097.86 <b>(+161.33%)</b></td><td>883.90 <b>(+140.12%)</b></td><td>356.60 (+10.81%)</td><td>757.05 <b>(+629.59%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>1.63 (n/a)</td><td>1.31 (n/a)</td><td>1.42 (n/a)</td><td>0.93 (n/a)</td><td>0.30 (n/a)</td><td>565.20 (n/a)</td><td>420.10 (n/a)</td><td>368.10 (n/a)</td><td>321.80 (n/a)</td><td>103.76 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>2.92 (+8.27%)</td><td>1.67 (-18.55%)</td><td>2.37 (+2.55%)</td><td>0.30 <b>(-30.05%)</b></td><td>1.26 <b>(+37.66%)</b></td><td>3449.50 <b>(+42.97%)</b></td><td>1616.90 <b>(+95.63%)</b></td><td>443.20 (-2.49%)</td><td>359.00 (-7.64%)</td><td>1651.73 <b>(+86.18%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>2.70 (n/a)</td><td>2.05 (n/a)</td><td>2.31 (n/a)</td><td>0.43 (n/a)</td><td>0.92 (n/a)</td><td>2412.80 (n/a)</td><td>826.52 (n/a)</td><td>454.50 (n/a)</td><td>388.70 (n/a)</td><td>887.19 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>3.15 (-6.59%)</td><td>2.05 (-2.80%)</td><td>2.11 (-10.37%)</td><td>0.87 <b>(+44.49%)</b></td><td>0.90 <b>(-20.06%)</b></td><td>2421.60 <b>(-30.79%)</b></td><td>1252.02 (-13.85%)</td><td>996.20 (+11.57%)</td><td>664.80 (+7.05%)</td><td>705.79 <b>(-40.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>3.38 (n/a)</td><td>2.11 (n/a)</td><td>2.35 (n/a)</td><td>0.60 (n/a)</td><td>1.12 (n/a)</td><td>3499.00 (n/a)</td><td>1453.32 (n/a)</td><td>892.90 (n/a)</td><td>621.00 (n/a)</td><td>1194.68 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>2.90 <b>(+107.72%)</b></td><td>1.52 <b>(+58.08%)</b></td><td>1.46 <b>(+61.21%)</b></td><td>0.82 (+9.90%)</td><td>0.83 <b>(+216.05%)</b></td><td>641.80 (-9.00%)</td><td>420.02 <b>(-26.90%)</b></td><td>358.80 <b>(-37.97%)</b></td><td>180.70 <b>(-51.86%)</b></td><td>183.64 <b>(+39.84%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>1.40 (n/a)</td><td>0.96 (n/a)</td><td>0.91 (n/a)</td><td>0.74 (n/a)</td><td>0.26 (n/a)</td><td>705.30 (n/a)</td><td>574.62 (n/a)</td><td>578.40 (n/a)</td><td>375.40 (n/a)</td><td>131.33 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.15 (+6.70%)</td><td>0.11 (+18.76%)</td><td>0.13 <b>(+76.87%)</b></td><td>0.05 <b>(-25.04%)</b></td><td>0.05 <b>(+41.10%)</b></td><td>636.10 <b>(+33.41%)</b></td><td>352.36 (-6.88%)</td><td>250.10 <b>(-43.45%)</b></td><td>212.50 (-6.26%)</td><td>183.57 <b>(+69.00%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>476.80 (n/a)</td><td>378.38 (n/a)</td><td>442.30 (n/a)</td><td>226.70 (n/a)</td><td>108.62 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.16 <b>(+34.02%)</b></td><td>0.11 <b>(+32.69%)</b></td><td>0.13 <b>(+69.41%)</b></td><td>0.05 (-8.51%)</td><td>0.05 <b>(+91.65%)</b></td><td>723.60 (+9.31%)</td><td>393.68 (-11.81%)</td><td>259.40 <b>(-40.98%)</b></td><td>202.90 <b>(-25.38%)</b></td><td>228.37 <b>(+59.30%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>662.00 (n/a)</td><td>446.38 (n/a)</td><td>439.50 (n/a)</td><td>271.90 (n/a)</td><td>143.36 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.25 (+5.41%)</td><td>0.20 (-5.11%)</td><td>0.19 (-14.39%)</td><td>0.16 (+7.93%)</td><td>0.04 (+6.20%)</td><td>412.20 (-7.35%)</td><td>337.50 (+5.28%)</td><td>342.30 (+16.79%)</td><td>261.50 (-5.12%)</td><td>64.85 (-8.57%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>444.90 (n/a)</td><td>320.56 (n/a)</td><td>293.10 (n/a)</td><td>275.60 (n/a)</td><td>70.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.26 (+12.90%)</td><td>0.21 <b>(+24.51%)</b></td><td>0.22 <b>(+30.47%)</b></td><td>0.13 (+6.63%)</td><td>0.05 (+10.47%)</td><td>517.50 (-6.22%)</td><td>339.86 (-19.86%)</td><td>304.10 <b>(-23.34%)</b></td><td>249.90 (-11.41%)</td><td>107.94 (-12.11%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>551.80 (n/a)</td><td>424.10 (n/a)</td><td>396.70 (n/a)</td><td>282.10 (n/a)</td><td>122.81 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.25 (+0.30%)</td><td>0.15 (-13.91%)</td><td>0.13 (-13.80%)</td><td>0.03 <b>(-69.76%)</b></td><td>0.09 <b>(+54.91%)</b></td><td>1913.00 <b>(+230.74%)</b></td><td>703.78 <b>(+73.78%)</b></td><td>502.70 (+16.02%)</td><td>264.20 (-0.30%)</td><td>686.88 <b>(+448.30%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>578.40 (n/a)</td><td>404.98 (n/a)</td><td>433.30 (n/a)</td><td>265.00 (n/a)</td><td>125.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.50 (+12.14%)</td><td>0.37 <b>(+30.25%)</b></td><td>0.45 <b>(+80.27%)</b></td><td>0.20 <b>(+190.99%)</b></td><td>0.14 (-11.07%)</td><td>649.80 <b>(-65.63%)</b></td><td>400.94 <b>(-43.55%)</b></td><td>293.20 <b>(-44.53%)</b></td><td>264.50 (-10.82%)</td><td>174.95 <b>(-73.88%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>0.15 (n/a)</td><td>1890.80 (n/a)</td><td>710.22 (n/a)</td><td>528.60 (n/a)</td><td>296.60 (n/a)</td><td>669.83 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.42 <b>(-33.46%)</b></td><td>0.26 (-10.32%)</td><td>0.24 (-11.39%)</td><td>0.16 <b>(+156.19%)</b></td><td>0.10 <b>(-53.31%)</b></td><td>810.50 <b>(-60.97%)</b></td><td>559.10 <b>(-28.09%)</b></td><td>550.50 (+12.85%)</td><td>311.90 <b>(+50.24%)</b></td><td>181.92 <b>(-75.49%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.63 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>0.21 (n/a)</td><td>2076.40 (n/a)</td><td>777.54 (n/a)</td><td>487.80 (n/a)</td><td>207.60 (n/a)</td><td>742.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.69 <b>(+30.04%)</b></td><td>0.39 <b>(+21.48%)</b></td><td>0.27 (-0.73%)</td><td>0.23 (+8.84%)</td><td>0.20 <b>(+53.38%)</b></td><td>571.40 (-8.14%)</td><td>409.64 (-11.33%)</td><td>491.50 (+0.74%)</td><td>188.80 <b>(-23.10%)</b></td><td>170.74 (+11.39%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.53 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>622.00 (n/a)</td><td>461.98 (n/a)</td><td>487.90 (n/a)</td><td>245.50 (n/a)</td><td>153.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 18:54:45</td><td>0.07 (+15.50%)</td><td>0.04 (-8.44%)</td><td>0.03 (-14.66%)</td><td>0.01 <b>(-78.69%)</b></td><td>0.03 <b>(+98.01%)</b></td><td>2526.60 <b>(+369.28%)</b></td><td>842.46 <b>(+100.68%)</b></td><td>515.40 (+17.16%)</td><td>235.50 (-13.42%)</td><td>957.30 <b>(+707.51%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:14:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>538.40 (n/a)</td><td>419.80 (n/a)</td><td>439.90 (n/a)</td><td>272.00 (n/a)</td><td>118.55 (n/a)</td>
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
